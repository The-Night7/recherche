"""Lecture passive des supports Ing et métadonnées de leur arborescence."""
import hashlib
import re
import zipfile
import unicodedata
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

from courses import ing_source_context, normalized

CODE_EXTS = {'.py', '.c', '.r', '.sql', '.scala'}
OFFICE_EXTS = {'.pptx', '.xlsx'}
IMAGE_EXTS = {'.png', '.jpg', '.jpeg'}


def storage_stem(path, course):
    """Deux TD1 dans des chapitres distincts restent deux documents."""
    stem = Path(path).stem
    if not course.startswith('ing-'):
        return stem
    context, tail = ing_source_context(path)
    identity = context + '/' + '/'.join(tail)
    suffix = hashlib.sha256(identity.encode('utf-8')).hexdigest()[:12]
    return f'{stem[:80]}--{suffix}'


def source_metadata(path, course):
    extra = {'source': str(path)}
    if not course.startswith('ing-'):
        if any(re.search(r'(?:^|-)projets?$', p, re.I) for p in Path(path).parts[:-1]):
            extra['kind'] = 'projet'
        return extra
    path = Path(path)
    name = path.stem
    _, tail = ing_source_context(path)
    folders = [normalized(p) for p in tail[:-1]]
    tokens = re.sub(r'[^a-z0-9]+', ' ', unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode().lower())
    kind = 'cours'
    if course.endswith('-informations'):
        kind = 'infos'
    elif path.suffix.lower() in CODE_EXTS | {'.xlsx'}:
        kind = 'ressource'
    elif re.search(r'\b(fiche|brouillon|revision)\b', tokens):
        kind = 'cours'
    elif re.search(r'\bqcm\b', tokens):
        kind = 'qcm'
    elif re.search(r'\b(ds\d*|examen|exam|partiel|rattrapage)\b', tokens) or any(re.search(r'examen|annale|exam$|^ds', f) for f in folders):
        kind = 'ds'
    elif re.search(r'\b(interro(?:gation)?|cc)\s*\d*\b', tokens):
        kind = 'cc'
    elif 'projet' in tokens or any('projet' in f for f in folders):
        kind = 'projet'
    elif re.search(r'\btp\s*\d*', tokens):
        kind = 'tp'
    elif re.search(r'\btd\s*\d*', tokens):
        kind = 'td'
    elif any(re.fullmatch(r'tps?\d*', f) for f in folders):
        kind = 'tp'
    elif any(re.fullmatch(r'tds?\d*', f) for f in folders):
        kind = 'td'
    corrige = bool(re.search(r'corrig|correction|solutions?|\bcor\b', tokens) or
                   any(f.startswith(('corrig', 'correction', 'solutions')) for f in folders))
    # Une année isolée n'indique pas avec certitude l'année scolaire.
    year = None
    for component in [name, *reversed(tail[:-1])]:
        for match in re.finditer(r'(?<!\d)(20\d{2}|\d{2})[-_ /]?(20\d{2}|\d{2})(?!\d)', component):
            a, b = (int(v) for v in match.groups())
            a = a + 2000 if a < 100 else a
            b = b + 2000 if b < 100 else b
            if 2000 <= a <= 2098 and b == a + 1:
                year = a
                break
        if year:
            break
    title = name.replace('_', ' ')
    years = f'{year}-{year + 1}' if year else 'année inconnue'
    extra.update(original_stem=name, title=title, kind=kind, corrige=corrige, year=year,
                 doc_label=f"{title}{' — corrigé' if corrige else ''} · {years}")
    if path.suffix.lower() in CODE_EXTS:
        extra['source_format'] = 'code'
    elif path.suffix.lower() in {'.xlsx', '.html'}:
        extra['source_format'] = 'text'
    return extra


class ReadableHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.hidden = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'head'):
            self.hidden += 1
        if not self.hidden and tag in ('p', 'div', 'li', 'h1', 'h2', 'h3', 'pre', 'tr', 'br'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'head'):
            self.hidden = max(0, self.hidden - 1)
        if not self.hidden and tag in ('p', 'div', 'li', 'h1', 'h2', 'h3', 'pre', 'tr'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def extract_office(path, page_sep):
    with zipfile.ZipFile(path) as archive:
        if Path(path).suffix.lower() == '.pptx':
            slides = sorted((n for n in archive.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)),
                            key=lambda n: int(re.search(r'slide(\d+)\.xml', n)[1]))
            ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            return page_sep.join('\n'.join(''.join(p.itertext()) for p in ET.fromstring(archive.read(n)).findall('.//a:p', ns)) for n in slides)
        ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        shared = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            shared = [''.join(t.itertext()) for t in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('s:si', ns)]
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        relationships = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
        targets = {r.get('Id'): r.get('Target') for r in relationships}
        parts = []
        for sheet in workbook.findall('s:sheets/s:sheet', ns):
            rid = sheet.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            target = targets[rid]
            target = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            rows = []
            for row in ET.fromstring(archive.read(target)).findall('.//s:row', ns):
                cells = []
                for cell in row.findall('s:c', ns):
                    value = cell.findtext('s:v', default='', namespaces=ns)
                    if cell.get('t') == 's' and value:
                        value = shared[int(value)]
                    elif cell.get('t') == 'inlineStr':
                        value = ''.join(cell.find('s:is', ns).itertext())
                    elif not value:
                        value = cell.findtext('s:f', default='', namespaces=ns)
                    if value:
                        cells.append(f"{cell.get('r', '')}: {value}")
                if cells:
                    rows.append(' | '.join(cells))
            parts.append(sheet.get('name', '') + '\n' + '\n'.join(rows))
        return page_sep.join(parts)
