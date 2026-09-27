# -*- coding: utf-8 -*-
"""
Ajout de documents de cours (Séries, Analyse dans ℝⁿ…) en une commande.

    python3 ingest.py sync <lien d'un dossier Drive> [<autre lien>...]
        télécharge le dossier (partagé « tous les utilisateurs disposant du
        lien ») dans data/_drive/, ajoute ce qui n'est pas encore indexé,
        puis reconstruit l'index. Les sous-dossiers sont parcourus.

    python3 ingest.py add <fichiers ou dossiers>...
        pareil à partir de fichiers locaux (PDF, .md, .txt, .docx), par exemple un
        dossier Drive téléchargé et dézippé à la main.

    python3 ingest.py status <fichiers ou dossiers>...
        affiche ce qui serait ajouté, sans rien modifier.

    python3 ingest.py build
        re-découpe tout data/<cours>/ et reconstruit l'index (après une
        transcription ou une modification à la main).

Le cours est déduit du nom de fichier, au format du dossier partagé :
    TD4_2024-2025_Series_P2S1_DMaths.pdf
    DS1-2023-2024-V4-Correction_Series-DS_P2S1_EMasnada.pdf
    DS2-2024-2025-V1_Analyse-dans-RN-DS_P2S1_DMaths.pdf
Un fichier déjà indexé (même nom, tirets et majuscules ignorés, ou même
contenu dans la même matière et le même semestre) n'est pas réajouté.
Les dossiers PREING1-S1, PREING1-S2, PREING2-S1 et PREING2-S2 permettent
de classer les documents par sous-dossier de matière, même sans nom normalisé.

PDF scanné (aucun texte extractible) : il est signalé « à transcrire ».
Mettre la transcription Markdown + LaTeX dans
data/<cours>/transcriptions/<nom du PDF>.md puis lancer `build`.
"""
import hashlib
import inspect
import json
import os
import re
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from clean_extraction import clean_text, strip_control_chars
from courses import COURSES, PLAIN_TEXT_COURSES, course_context, source_course, ensure_meta
from document_sources import CODE_EXTS, OFFICE_EXTS, IMAGE_EXTS, ReadableHTML, extract_office, source_metadata, storage_stem

DATA_ROOT = "data"
DRIVE_DIR = os.path.join(DATA_ROOT, "_drive")
PAGE_SEP = "\n<<<PAGE>>>\n"
SOURCE_EXTS = {".pdf", ".md", ".txt", ".docx", ".html"} | CODE_EXTS | OFFICE_EXTS | IMAGE_EXTS

# documents volontairement ignorés, par cours (noms comparés sans tirets ni casse)
SKIP = {
    "series": {
        "CM-Annotee_2022-2023_Series_P2S1_MX": "notes manuscrites, OCR illisible",
    },
    "analyse-rn": {
        "CM-Annotee_2022-2023_Analyse-dans-RN_P2S1_MX": "notes manuscrites, OCR illisible",
        # le poly et les corrections de TD sont déjà dans chunks.json (ancien
        # format, sans fichier source) : les réajouter ferait des doublons
        "CM_2022-2023_Analyse-dans-RN_P2S1_EMasnada": "poly déjà indexé (Chapitres 1 à 6)",
        "CM_2023-2024_Analyse-dans-RN_P2S1": "poly déjà indexé (Chapitres 1 à 6)",
        "CM_2024-2025_Analyse-dans-RN_P2S1_EMasnada": "poly déjà indexé (Chapitres 1 à 6)",
        "TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada": "déjà indexé (ancienne correction)",
        "TD-Correction_2024-2025_Analyse-dans-RN_P2S1_EMasnada": "déjà indexé (ancienne correction)",
    },
}

MAX_CHARS = 2400
MIN_CHARS = 250


def key(stem):
    """Clé de comparaison : \"DS1-2023-2024-V4\" == \"DS120232024V4\"."""
    return re.sub(r"[^a-z0-9]", "", stem.lower())


def course_dir(course):
    return os.path.join(DATA_ROOT, course)


def transcriptions_dir(course):
    return os.path.join(course_dir(course), "transcriptions")


def skip_reason(course, stem):
    return {key(k): v for k, v in SKIP.get(course, {}).items()}.get(key(stem))


# --------------------------------------------------------------------------
# 1) Extraction
# --------------------------------------------------------------------------

def extract_file(path):
    ext = Path(path).suffix.lower()
    if ext in OFFICE_EXTS:
        return extract_office(path, PAGE_SEP)
    if ext == '.html':
        parser = ReadableHTML()
        parser.feed(Path(path).read_text(encoding='utf-8', errors='replace'))
        return ''.join(parser.parts)
    if str(path).lower().endswith('.docx'):
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        # Conserver les paragraphes, tableaux et retours à la ligne du document.
        return '\n\n'.join(''.join(
            node.text or '' if node.tag.endswith('}t') else '\n' if node.tag.endswith('}br') else '\t'
            for node in para.iter() if node.tag.rsplit('}', 1)[-1] in ('t', 'br', 'tab')
        ) for para in root.findall('.//w:p', ns))
    raw = Path(path).read_bytes()
    if raw[:2] == b"PK":  # export "zip" (pages .txt + images) du dossier partagé
        z = zipfile.ZipFile(path)
        pages = sorted(
            (n for n in z.namelist() if n.endswith(".txt")),
            key=lambda n: int(os.path.splitext(os.path.basename(n))[0]),
        )
        return PAGE_SEP.join(z.read(n).decode("utf-8", "replace") for n in pages)
    if raw[:5] == b"%PDF-":
        try:
            from pypdf import PdfReader
        except ImportError:
            sys.exit("pip install pypdf --break-system-packages  (nécessaire pour lire les PDF)")
        reader = PdfReader(path)
        return PAGE_SEP.join((p.extract_text() or "") for p in reader.pages)
    return raw.decode("utf-8", "replace")


def collect(paths):
    """Fichiers sources sous les chemins donnés (dossiers parcourus récursivement)."""
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                out += [os.path.join(root, f) for f in sorted(files)]
        elif os.path.isfile(p):
            out.append(p)
        else:
            print(f"  introuvable  {p}")
    # la copie la plus récente d'abord : c'est elle qui est gardée en cas de doublon
    year = lambda f: max((int(y) for y in re.findall(r"20\d{2}", os.path.basename(f))), default=0)
    return sorted(out, key=lambda f: (-year(f), os.path.basename(f)))


class Library:
    """Ce qui est déjà dans data/<cours>/ (textes, transcriptions, empreintes des sources)."""

    def __init__(self):
        self.known = {}   # cours -> {clé: nom affiché}
        self.hashes = {}  # cours -> {empreinte du texte: nom}
        for course in COURSES:
            names = {}
            for folder in (course_dir(course), transcriptions_dir(course)):
                if os.path.isdir(folder):
                    for f in os.listdir(folder):
                        stem, ext = os.path.splitext(f)
                        if ext in (".txt", ".md") and not f.startswith("README"):
                            names[key(stem)] = stem
            self.known[course] = names
            self.hashes[course] = self._load_hashes(course)

    @staticmethod
    def _hash_file(course):
        return os.path.join(course_dir(course), "sources.json")

    def _load_hashes(self, course):
        try:
            return json.loads(Path(self._hash_file(course)).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}

    def save(self):
        for course, hashes in self.hashes.items():
            if hashes:
                os.makedirs(course_dir(course), exist_ok=True)
                with open(self._hash_file(course), "w", encoding="utf-8") as f:
                    json.dump(hashes, f, ensure_ascii=False, indent=1, sort_keys=True)


def cmd_add(paths, dry_run=False):
    """Retourne le nombre de documents ajoutés."""
    lib = Library()
    added, report = 0, {"déjà là": 0, "autre cours": 0, "doublon": 0, "à transcrire": 0, "erreur": 0, "annexe": 0}
    details = []
    def record(path, status, course=None, **extra):
        details.append(dict(source=str(path), status=status, course=course, **extra))
    for path in collect(paths):
        stem, ext = os.path.splitext(os.path.basename(path))
        if ext.lower() not in SOURCE_EXTS:
            report['annexe'] += 1
            record(path, 'annexe non indexée', source_course(path), reason='format de données, audio ou archive')
            continue
        course = source_course(path)
        if course is None:
            report["autre cours"] += 1
            record(path, "matière inconnue")
            continue
        stem = storage_stem(path, course)
        tag = f"[{course}]"
        reason = skip_reason(course, stem)
        if reason:
            print(f"  ignoré        {tag} {stem} ({reason})")
            record(path, "ignoré", course, reason=reason)
            continue
        if key(stem) in lib.known[course]:
            report["déjà là"] += 1
            record(path, "déjà là", course)
            continue
        if ext.lower() in IMAGE_EXTS:
            report["à transcrire"] += 1
            record(path, "à transcrire", course)
            print(f"  à transcrire  {tag} {stem} (image)")
            continue
        try:
            text = extract_file(path).replace("\r\n", "\n")
        except Exception as error:
            report["erreur"] += 1
            record(path, "erreur", course, reason=str(error))
            print(f"  erreur        {tag} {stem}: {error}")
            continue
        # empreinte du texte (et non du fichier) : deux exports du même PDF comptent comme un doublon
        digest = hashlib.sha256(re.sub(r"\s+", " ", text).strip().encode("utf-8")).hexdigest()
        if digest in lib.hashes[course]:
            report["doublon"] += 1
            record(path, "doublon", course, duplicate_of=lib.hashes[course][digest])
            print(f"  doublon       {tag} {stem} (même texte que {lib.hashes[course][digest]})")
            continue
        letters = sum(ch.isalpha() for ch in text.replace(PAGE_SEP, ""))
        if letters < (150 if ext.lower() == '.pdf' else 10):
            report["à transcrire"] += 1
            record(path, "à transcrire", course)
            print(f"  à transcrire  {tag} {stem}  (PDF scanné -> data/{course}/transcriptions/{stem}.md)")
            continue
        print(f"  {'à ajouter' if dry_run else 'ajouté':<13} {tag} {stem} ({letters} lettres)")
        lib.known[course][key(stem)] = stem
        lib.hashes[course][digest] = stem
        added += 1
        record(path, "ajouté", course, doc=stem)
        if not dry_run:
            os.makedirs(course_dir(course), exist_ok=True)
            out_ext = ".md" if ext.lower() == ".md" else ".txt"
            with open(os.path.join(course_dir(course), stem + out_ext), "w", encoding="utf-8") as f:
                f.write(text)
            meta_path = Path(course_dir(course)) / 'source_meta.json'
            source_meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
            source_meta[stem] = source_metadata(path, course)
            meta_path.write_text(json.dumps(source_meta, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"\n  {added} {'à ajouter' if dry_run else 'ajouté(s)'}, {report['déjà là']} déjà indexé(s), "
          f"{report['doublon']} doublon(s), {report['à transcrire']} à transcrire, "
          f"{report['erreur']} erreur(s), {report['autre cours']} matière(s) inconnue(s), "
          f"{report['annexe']} annexe(s) non indexée(s)")
    if not dry_run:
        lib.save()
        Path(DATA_ROOT, 'import-report.json').write_text(json.dumps(details, ensure_ascii=False, indent=2), encoding='utf-8')
    return added


def cmd_sync(urls):
    try:
        import gdown
    except ImportError:
        sys.exit("pip install gdown --break-system-packages  (nécessaire pour télécharger depuis Drive)")
    os.makedirs(DRIVE_DIR, exist_ok=True)
    for url in urls:
        print(f"Téléchargement de {url} …")
        # les options de gdown changent d'une version à l'autre : on ne passe que celles qu'il connaît
        wanted = {"output": DRIVE_DIR, "quiet": False, "resume": True, "remaining_ok": True, "retries": 3}
        params = inspect.signature(gdown.download_folder).parameters
        try:
            files = gdown.download_folder(url, **{k: v for k, v in wanted.items() if k in params})
        except Exception as e:
            files = None
            print(f"  erreur : {e}")
        if not files:
            sys.exit("Échec du téléchargement.\nLe dossier doit être partagé à « tous les "
                     "utilisateurs disposant du lien ». Sinon : télécharge-le depuis Drive, "
                     "dézippe, puis `python3 ingest.py add <dossier>`.")
    if cmd_add([DRIVE_DIR]):
        cmd_build()
    else:
        print("Rien de nouveau : index inchangé.")


# --------------------------------------------------------------------------
# 2) Métadonnées depuis le nom de fichier
# --------------------------------------------------------------------------

YEAR_RE = re.compile(r"(20\d{2})\D?(20\d{2})")
AUTHOR_RE = re.compile(r"_P\dS\d_+([A-Z][a-z]?)([A-Z][A-Za-z]+)")
COURSE_TITLES = {  # début du nom (sans tirets, minuscules) -> titre
    "cmderivation": "Dérivation",
    "cmcomparaisonlocale": "Comparaison locale des fonctions",
    "cmannotee": "Notes de cours annotées",
    "feuillecours": "Feuille de cours",
}


def parse_meta(stem, course):
    name = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)  # préfixe de date des notes .md
    name = re.sub(r'^ORIGINAL-', '', name, flags=re.I)
    year = None
    for m in YEAR_RE.finditer(stem):
        a, b = int(m.group(1)), int(m.group(2))
        if b == a + 1:
            year = a
            break

    upper = name.upper()
    if upper.startswith("QCM"):
        kind = "qcm"
    elif upper.startswith("DS"):
        kind = "ds"
    elif upper.startswith("CC") or re.match(r"RAT+RAPAGE", upper):
        kind = "cc"
    elif upper.startswith("TD"):
        kind = "td"
    elif upper.startswith("TP"):
        kind = "tp"
    elif course.startswith('projet') or upper.startswith(('PROJET', 'SUITE_PROJET')):
        kind = "projet"
    else:
        kind = "cours"

    corrige = bool(re.search(r'correction|corrig[eé]', name, re.I))
    author = None
    m = AUTHOR_RE.search(stem)
    if m and m.group(2) not in ("Maths", "Inconnu"):
        last = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", m.group(2))  # ElAmine -> El Amine
        author = f"{m.group(1)}. {last}"

    if kind == "td":
        m = re.match(r"TD-?\(?(\d+[ab]?)(?:-(\d+))?\)?", name)
        if m:
            title = f"TD{m.group(1)}" + (f"-{m.group(2)}" if m.group(2) else "")
        else:  # recueil de toutes les feuilles de TD
            title = "Feuilles de TD"
    elif kind in ("ds", "cc"):
        m = re.match(r"(?:DS|CC)[-_]?(\d+)", name, re.I)
        title = f"{kind.upper()}{m.group(1)}" if m else "Rattrapage"
        v = re.search(r"V(\d)", name)
        if v:
            title += f" V{v.group(1)}"
        if m and re.search(r"rat+rapage", name, re.I):
            title += " rattrapage"
    elif kind == "qcm":
        number = re.match(r"QCM[-_]?(\d+)", name, re.I)
        title = "QCM" + (number[1] if number else '')
    else:
        raw_prefix = name.split("_")[0]
        prefix = key(raw_prefix)
        title = COURSE_TITLES.get(prefix, raw_prefix.replace("-", " ") if prefix != "cm" else "Notes de cours")
    if author and kind in ("cours", "td") and not title.startswith(("TD", "DS")):
        title += f" ({author})"

    years_txt = f"{year}-{year + 1}" if year else "année inconnue"
    return {
        "course": course,
        "curriculum": course_context(course)["id"],
        "program": course_context(course)["program"],
        "track": course_context(course)["track"],
        "study_year": course_context(course)["study_year"],
        "semester": course_context(course)["semester"],
        "kind": kind,
        "corrige": corrige,
        "year": year,
        "doc": stem,
        "title": title,
        "doc_label": f"{title}{' — corrigé' if corrige else ''} · {years_txt}",
    }


# --------------------------------------------------------------------------
# 3) Nettoyage spécifique aux PDF LaTeX (glyphes de la police cmex, etc.)
# --------------------------------------------------------------------------

GLYPHS = {
    "\x00": "(", "\x01": ")", "\x10": "(", "\x11": ")", "\x12": "(", "\x13": ")",
    "\x14": "[", "\x15": "]",
    "\x0c": "|", "\x1a": "{", "\x02": "", "\x1b": "ff", "\x1d": "fl", "\x1e": "ffi",
}


LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}


def fix_ligatures(text):
    return text.translate(str.maketrans(LIGATURES))


ACCENT_MARKS = {"´": "\u0301", "`": "\u0300", "ˆ": "\u0302", "¨": "\u0308"}


ACCENT_RE = re.compile(r"([A-Za-zÀ-ÿ]?)([´`ˆ¨]) ?([aeiouyıAEIOUY])")
GRAVE_RE = re.compile(r"[A-Za-zÀ-ÿ]` ?[aeiouAEIOU]|(?<=\s)` a(?=\s)")


def fix_accents(text):
    """Recompose les accents séparés par les PDF LaTeX : « Th´ eorie » -> « Théorie »."""
    def fix_line(line):
        # un accent grave n'est recomposé que si tous les backticks de la ligne en sont (pas de code inline)
        grave_ok = line.count("`") == len(GRAVE_RE.findall(line))

        def compose(m):
            before, mark, vowel = m.groups()
            if mark == "`" and not (before and grave_ok):
                return m[0]
            return before + unicodedata.normalize("NFC", vowel.replace("ı", "i") + ACCENT_MARKS[mark])
        line = ACCENT_RE.sub(compose, line)
        return re.sub(r"(?<=\s)` a(?=\s)", "à", line) if grave_ok else line
    return "\n".join(fix_line(line) for line in text.split("\n"))


def fix_spacing(text):
    """« deA », « matriceA » : l'extraction a collé un mot et le nom d'une variable."""
    return re.sub(r"(?<=[a-zéèêàâîôûç]{2})([A-Z][a-z]?)(?=[\s.,;:)=∈∼≤≥<>])", r" \1", text)


def fix_glyphs(text):
    """À appliquer AVANT clean_text (qui supprime les caractères de contrôle)."""
    text = fix_spacing(fix_accents(text))
    text = re.sub(r"(?<=[A-Za-zé])\x1c(?=[a-zé])", "fi", text)
    for k, v in GLYPHS.items():
        text = text.replace(k, v)
    text = re.sub(r"(?<=\s)6=(?=\s|\d)", "≠", text)
    return text.replace("7−→", "↦").replace("7→", "↦").replace("−→", "→")


def fix_sums(text):
    """Grand symbole de somme : "X" (display) ou "P" (inline) seul sur sa
    ligne, suivi de l'indice de sommation sur la ligne suivante."""
    text = re.sub(r"(?m)(^|\s)[XP]\n(?=[nkijp]\s?[≥∈=>])", r"\1∑", text)
    text = re.sub(r"∑\n([nkijp]\s?[≥∈=>][^\n]{0,8})\n", r"∑_{\1} ", text)
    text = re.sub(r"(?m)(^|\s)X([n+N][∞]?)\n([nkijp]=\d)\n", r"\1∑_{\3}^{\2} ", text)
    return text


KEEP_LINE_RE = re.compile(
    r"^(Remarque|Exemple|Démonstration|Définition|Propriété|Théorème|Proposition|"
    r"Corollaire|Preuve|Attention|Exercice|Question|Réponse|Méthode)"
)


def drop_running_lines(pages, whole_text=False):
    """Retire les lignes répétées sur beaucoup de pages (menus de
    navigation des diapos beamer, pieds de page "Romain Dujol 25"...).
    Sans séparateur de pages (whole_text=True, réservé aux diapos de cours),
    on compte les répétitions dans tout le texte."""
    # Retirer les pieds de page avant de fusionner les exposants : "k\n3"
    # en bas de la page 3 ne doit pas devenir k³.
    if len(pages) > 1:
        for number, page in enumerate(pages, 1):
            lines = page.rstrip().split("\n")
            if lines[-1].strip() == str(number):
                pages[number - 1] = "\n".join(lines[:-1])
    if len(pages) < 4 and not whole_text:
        return pages
    norm = lambda s: re.sub(r"\d+", "#", s.strip())
    counts = {}
    for p in pages:
        seen = [norm(l) for l in p.split("\n") if l.strip()]
        for line in (set(seen) if len(pages) >= 4 else seen):
            counts[line] = counts.get(line, 0) + 1
    threshold = max(3, 0.3 * len(pages)) if len(pages) >= 4 else 6
    frequent = {
        l for l, c in counts.items()
        if c >= threshold and len(l) < 90 and not KEEP_LINE_RE.match(l)
        # Une expression répétée (k=1, n + 1, un =…) n'est pas un en-tête.
        and re.search(r"[A-Za-zÀ-ÿ]{4,}", l)
    }
    return ["\n".join(l for l in p.split("\n") if norm(l) not in frequent) for p in pages]


# --------------------------------------------------------------------------
# 4) Découpage en passages
# --------------------------------------------------------------------------

def split_long(label, text):
    """Coupe un passage trop long sur des lignes vides / fins de phrase."""
    if len(text) <= MAX_CHARS:
        return [(label, text)]
    parts, buf = [], ""
    for para in re.split(r"(\n\s*\n)", text):
        if len(buf) + len(para) > MAX_CHARS and len(buf) > MIN_CHARS:
            parts.append(buf)
            buf = ""
        buf += para
    if buf.strip():
        parts.append(buf)
    # Limite souple : ne pas couper une fraction ou une démonstration au
    # milieu de ses lignes pour respecter un nombre arbitraire de caractères.
    out = parts
    if len(out) == 1:
        return [(label, out[0])]
    return [(f"{label} ({i}/{len(out)})", p) for i, p in enumerate(out, 1)]


def merged_label(labels):
    """"IV. DSE › Proposition" + "IV. DSE › Définition" -> "IV. DSE › Proposition, Définition"."""
    if len(labels) == 1:
        return labels[0]
    paths = [l.split(" › ") for l in labels]
    common = []
    for parts in zip(*paths):
        if len(set(parts)) != 1:
            break
        common.append(parts[0])
    leaves = []
    for p in paths:
        leaf = " › ".join(p[len(common):]) or p[-1]
        if leaf not in leaves:
            leaves.append(leaf)
    shown = ", ".join(leaves[:3]) + ("…" if len(leaves) > 3 else "")
    return " › ".join(common + [shown]) if common else shown


def merge_small(sections):
    groups = []
    for label, text in sections:
        if groups and len(groups[-1][1]) < MIN_CHARS:
            groups[-1][0].append(label)
            groups[-1][1] += "\n\n" + text
        else:
            groups.append([[label], text])
    return [(merged_label(labels), text) for labels, text in groups]


EXO_RE = re.compile(r"(?m)^(Exercice|Ex\.|Question|Probl[èe]me)\s*(\d+)\b.*$")


def sections_exercises(text, qcm=False):
    """TD / DS / QCM : un passage par exercice ; la "Réponse N" d'un
    corrigé reste dans le passage de son exercice."""
    text = re.sub(r"(?m)^Réponse\s*(\d+)", r"Réponse \1", text)
    marks = list(EXO_RE.finditer(text))
    if not marks:
        return [("Document", text)]
    secs = []
    intro = text[: marks[0].start()].strip()
    if len(intro) > 120 and not qcm:
        secs.append(("Consignes / en-tête", intro))
    seen = set()
    for i, m in enumerate(marks):
        body = text[m.start(): marks[i + 1].start() if i + 1 < len(marks) else len(text)].strip()
        # clé = début de l'énoncé seulement (les choix du QCM sont mélangés d'une copie à l'autre)
        key = re.sub(r"\s+", " ", body.split("\n", 1)[-1])[:70]
        if qcm and key in seen:  # QCM : chaque copie d'étudiant répète les questions
            continue
        seen.add(key)
        body = re.split(r"\n(?:②|\+\d+/\d+/\d+\+)", body)[0]  # cases à cocher AMC
        word = "Exercice" if m.group(1) == "Ex." else m.group(1)
        # QCM : les copies mélangent l'ordre -> numérotation par ordre d'apparition
        num = len(seen) if qcm else m.group(2)
        secs.append((f"{word} {num}", body))
    return secs


SEC_RE = re.compile(r"(?m)^((?:Thème\s+no\s*\d+)|(?:\d+(?:\.\d+){1,2})\s+[A-ZÉÈÀ][^\n]{2,80})$")


def sections_course_pdf(text):
    """Poly de cours : coupe sur les titres numérotés "2.3 Séries de
    référence" (en ignorant la table des matières)."""
    text = re.sub(r"(?m)^.*(?:\. ){4,}.*$\n?", "", text)  # lignes de sommaire
    marks = list(SEC_RE.finditer(text))
    if len(marks) < 3:
        # diapos : on garde l'ordre des pages, découpées par taille
        return [("Diapos", text)]
    secs = []
    for i, m in enumerate(marks):
        body = text[m.start(): marks[i + 1].start() if i + 1 < len(marks) else len(text)]
        secs.append((m.group(1).strip(), body.strip()))
    return secs


MD_HEAD_RE = re.compile(r"(?m)^(#{1,4})[ \t]+(.+?)[ \t]*$")


def sections_markdown(text):
    text = re.sub(r"(?s)^---\n.*?\n---\n", "", text)  # front-matter
    # Les commentaires et directives dans un programme ne sont pas des titres.
    heading_text = re.sub(r"(?ms)^[ \t]*(`{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*(?=\n|$)",
                          lambda m: re.sub(r"[^\n]", " ", m.group()), text)
    marks = list(MD_HEAD_RE.finditer(heading_text))
    if not marks:
        return [("Document", text)]
    secs, path = [], {}
    for i, m in enumerate(marks):
        level = len(m.group(1))
        # "3\." (échappement Markdown) -> "3." ; les commandes LaTeX (\alpha) restent
        title = re.sub(r"\\([.\-#()\[\]!+])", r"\1", re.sub(r"[*_`]", "", m.group(2))).strip(" :")
        if i == 0 and level == 1:  # titre du document ("CM Séries"), déjà dans doc_label
            continue
        path = {k: v for k, v in path.items() if k < level}
        path[level] = title
        body = text[m.end(): marks[i + 1].start() if i + 1 < len(marks) else len(text)].strip()
        if not body:
            continue
        # chemin sans le numéro de niveau 1 trop long : "5. Règle d'Alembert… › Exemple"
        label = " › ".join(path[k] for k in sorted(path))
        secs.append((label, body))
    return secs


def is_binary_noise(text):
    """Octets d'un fichier binaire (PDF brut, archive) lus comme du texte : plus de 5 % de caractères invalides."""
    bad = sum(1 for ch in text if ch == "\ufffd" or (ord(ch) < 32 and ch not in "\n\r\t"))
    return bad >= 20 and bad > 0.05 * len(text)


def norm_words(text):
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.findall(r"[a-z0-9]+", folded)


def word_grams(text):
    words = norm_words(text)
    return {tuple(words[i:i + 3]) for i in range(len(words) - 2)}


def page_index(raw):
    """gram de 3 mots -> pages du PDF où il apparaît (les pages sont séparées par PAGE_SEP)."""
    index = {}
    for number, page in enumerate(raw.split(PAGE_SEP), 1):
        for gram in word_grams(page):
            index.setdefault(gram, []).append(number)
    return index


def locate_pages(text, index, limit=6):
    grams = word_grams(text)
    hits = {}
    for gram in grams:
        for number in index.get(gram, ()):
            hits[number] = hits.get(number, 0) + 1
    if not hits:
        return []
    floor = min(2, len(grams)) if len(grams) < 10 else max(2, 0.2 * len(grams))
    kept = sorted(n for n, h in hits.items() if h >= floor)
    if not kept:
        best = max(hits, key=hits.get)
        kept = [best] if hits[best] >= 2 else []
    return kept[:limit]


def chunk_document(path, course):
    stem, ext = os.path.splitext(os.path.basename(path))
    meta = parse_meta(stem, course)
    meta_path = Path(course_dir(course)) / 'source_meta.json'
    if meta_path.exists():
        meta.update(json.loads(meta_path.read_text(encoding='utf-8')).get(stem, {}))
    with open(path, encoding="utf-8") as source:
        raw = fix_ligatures(source.read())
    fmt = "md" if ext == ".md" else "pdf"
    if fmt == "md":
        secs = sections_markdown(raw)
    else:
        if course in PLAIN_TEXT_COURSES or meta.get('source_format') in ('code', 'text') or meta.get('source', '').lower().endswith(('.docx', '.pptx', '.txt')):
            # Garder le code, ses indentations et les textes de SHS : les
            # heuristiques de fractions/indices sont propres aux maths.
            fmt = "code" if meta.get('source_format') == 'code' else "text"
            text = strip_control_chars(raw.replace(PAGE_SEP, "\n\n"))
            if fmt == "text":
                text = fix_spacing(fix_accents(text))
        else:
            pages = drop_running_lines(fix_glyphs(raw).split(PAGE_SEP), whole_text=meta["kind"] == "cours")
            text = fix_sums(clean_text("\n\n".join(pages)))
        text = re.sub(r"\n{3,}", "\n\n", text)
        secs = (sections_exercises(text, qcm=meta["kind"] == "qcm")
                if meta["kind"] != "cours" else sections_course_pdf(text))
    secs = [(l, t) for l, t in secs if t.strip()]
    if meta["kind"] == "cours":
        secs = merge_small(secs)
    pages_of_pdf = page_index(raw) if ext == ".txt" and meta.get("source", "").lower().endswith(".pdf") and PAGE_SEP in raw else None
    chunks = []
    for label, body in secs:
        # Un corrigé reste entier, même si ses calculs dépassent MAX_CHARS.
        if meta['kind'] == 'ressource':
            # Les tableaux et sources de code sont découpés entre leurs lignes.
            lines, groups, size = [], [], 0
            for line in body.splitlines(keepends=True):
                if size + len(line) > MAX_CHARS and lines:
                    groups.append(''.join(lines)); lines, size = [], 0
                lines.append(line); size += len(line)
            if lines:
                groups.append(''.join(lines))
            parts = [(f'{label} ({i}/{len(groups)})', text) for i, text in enumerate(groups, 1)]
        else:
            parts = split_long(label, body) if meta["kind"] in ('cours', 'infos') else [(label, body)]
        for sub_label, sub in parts:
            if not sub.strip() or (meta["kind"] == "cours" and len(sub.strip()) < 40) or is_binary_noise(sub):
                continue
            if sub_label.startswith("Diapos"):  # pas de titres : 1re ligne parlante
                first = next((l.strip() for l in sub.split("\n") if len(l.strip()) > 12), "")
                sub_label = first[:70] + ("…" if len(first) > 70 else "")
            chunk = {
                **meta,
                "fmt": fmt,
                "section": sub_label,
                "label": f"{meta['doc_label']} — {sub_label}",
                "text": sub.strip(),
            }
            if pages_of_pdf:
                pages = locate_pages(chunk["text"], pages_of_pdf)
                if pages:
                    chunk["pages"] = pages
            chunks.append(chunk)
    return chunks


SUPERSCRIPT_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
COURSE_BLOCK_RE = re.compile(r"\n(?=(?:D[ée]finition|Propri[ée]t[ée]|Th[ée]or[èe]me|Proposition|Exemple|"
                             r"Remarque|D[ée]monstration|M[ée]thode)s?\b)")


def strip_page_numbers(pages):
    """Numéro de page en fin de page : ligne « 23 » ou exposant collé (« ⊂ A²² »).
    Seulement s'il suit la numérotation : « r² » en fin de page 21 est un carré.
    Un numéro sauté (28 puis 30) a été placé ailleurs par l'extraction : on
    retire la ligne « 29 » seule restée dans les pages intermédiaires."""
    out, last, since = [], None, 0
    for page in pages:
        page = page.rstrip()
        m = re.search(r"\n(\d{1,3})$", page) or re.search(r"(?<=\S)([⁰¹²³⁴⁵⁶⁷⁸⁹]{2,3})$", page)
        number = int(m.group(1).translate(SUPERSCRIPT_DIGITS)) if m else None
        if number is not None and ((last is None and number <= 300) or (last is not None and last < number <= last + 12)):
            page = page[:m.start()].rstrip()
            out.append(page)
            for missing in range(last + 1, number) if last is not None else ():
                line = re.compile(r"(?m)^%d\n" % missing)
                for k in range(len(out) - 1, since - 1, -1):
                    found = list(line.finditer(out[k]))
                    if found:
                        out[k] = out[k][:found[-1].start()] + out[k][found[-1].end():]
                        break
            last, since = number, len(out)
            continue
        out.append(page)
    return out


def resplit_legacy(chunks):
    """Les passages de l'ancien format (poly et TD d'Analyse dans ℝⁿ, sans
    fichier source) étaient coupés par page ou par taille, au milieu des
    phrases et des calculs. On recolle chaque document et on le redécoupe
    comme les autres : un passage par exercice, par section pour le cours.
    Un document déjà redécoupé (« resplit ») est gardé tel quel."""
    docs, done = {}, []
    for chunk in chunks:
        if chunk.get("resplit"):
            done.append(chunk)
            continue
        docs.setdefault(chunk["doc_label"], []).append(chunk)
    out = done
    for doc_label, parts in docs.items():
        first = parts[0]
        title = first["section"].split(" › ")[0] if first["kind"] == "cours" else ""
        text = "\n".join(strip_page_numbers([part["text"] for part in parts]))
        if first["kind"] == "cours":
            # Les longues sections se coupent entre deux définitions, jamais dans une preuve.
            secs = merge_small(sections_course_pdf(COURSE_BLOCK_RE.sub("\n\n", text)))
            secs = [piece for label, body in secs for piece in split_long(label, body)]
        else:
            secs = sections_exercises(text)
        for label, body in secs:
            if not body.strip():
                continue
            if label.startswith("Diapos"):
                label = (title or doc_label) + label[len("Diapos"):]
            elif title and not label.startswith(title):
                label = f"{title} › {label}"
            meta = {k: v for k, v in first.items() if k not in ("label", "section", "text")}
            out.append({**meta, "section": label, "label": f"{doc_label} — {label}", "text": body.strip(),
                        "resplit": True})
    return out


# Les anciennes corrections d'Analyse dans ℝⁿ ne suivent pas la numérotation
# des feuilles 2025-2026 : l'exercice 2 du TD2 actuel est l'exercice 3 de
# l'ancien TD2, le TD6 actuel reprend l'ancien TD8... Table vérifiée à la main
# (énoncés comparés un à un) : (ancien TD, ancien exercice) -> (TD, exercice
# 2025-2026, correction partielle). Un ancien exercice absent n'a pas
# d'équivalent dans les feuilles actuelles.
LEGACY_ALIGNMENT = {
    ("TD1 1", 1): (1, 1, False), ("TD1 1", 3): (1, 2, False), ("TD1 1", 4): (1, 3, False),
    ("TD1 1", 8): (1, 4, False), ("TD1 1", 9): (1, 5, False),
    ("TD2", 2): (2, 1, False), ("TD2", 3): (2, 2, False), ("TD2", 4): (2, 3, False),
    ("TD3", 1): (3, 1, False), ("TD3", 2): (3, 2, False), ("TD3", 3): (3, 3, False), ("TD3", 5): (3, 4, False),
    ("TD4", 3): (4, 1, False), ("TD4", 2): (4, 2, False), ("TD4", 4): (4, 3, False),
    ("TD5", 6): (5, 1, False), ("TD5", 1): (5, 2, False), ("TD5", 2): (5, 3, False), ("TD5", 4): (5, 4, True),
    ("TD5", 7): (5, 5, False), ("TD6 − 7", 1): (5, 6, False), ("TD5", 3): (5, 7, False),
    ("TD8", 3): (6, 1, False), ("TD8", 4): (6, 2, False), ("TD8", 7): (6, 3, False), ("TD8", 5): (6, 4, False),
    ("TD8", 6): (6, 5, False), ("TD8", 9): (6, 6, False), ("TD8", 10): (6, 7, False),
    ("TD9 − 10", 1): (7, 1, True), ("TD9 − 10", 6): (7, 3, False), ("TD9 − 10", 8): (7, 4, False),
    ("TD9 − 10", 9): (7, 5, True),
    ("TD11 − 12", 2): (8, 1, False), ("TD11 − 12", 3): (8, 2, False), ("TD11 − 12", 6): (8, 3, False),
    ("TD11 − 12", 7): (8, 4, False), ("TD11 − 12", 8): (8, 5, False), ("TD11 − 12", 9): (8, 6, False),
    ("TD11 − 12", 10): (9, 1, False), ("TD11 − 12", 11): (9, 2, False),
}


def align_legacy(chunks):
    """Indique sur chaque exercice d'une ancienne correction l'exercice des
    feuilles 2025-2026 qu'il corrige (champ « current »)."""
    for chunk in chunks:
        chunk.pop("current", None)
        m = re.fullmatch(r"Exercice (\d+)", chunk.get("section", ""))
        if not (chunk.get("resplit") and chunk.get("corrige") and m):
            continue
        chunk["label"] = f"{chunk['doc_label']} — {chunk['section']}"
        target = LEGACY_ALIGNMENT.get((chunk["doc_label"].split(":")[0].strip(), int(m[1])))
        if target:
            td, exercise, partial = target
            chunk["current"] = {"td": td, "exercise": exercise, "partial": partial}
            chunk["label"] += f" · {'en partie ' if partial else ''}= TD{td} 2025-2026, exercice {exercise}"
        else:
            chunk["label"] += " · hors feuilles 2025-2026"
    return chunks


def cmd_build():
    new_chunks = []
    for course in COURSES:
        docs = {}
        # une transcription remplace le texte extrait du même document
        for folder in (course_dir(course), transcriptions_dir(course)):
            if not os.path.isdir(folder):
                continue
            for f in sorted(os.listdir(folder)):
                stem, ext = os.path.splitext(f)
                if ext in (".txt", ".md") and not f.startswith("README") and not skip_reason(course, stem):
                    docs[key(stem)] = os.path.join(folder, f)
        if not docs:
            continue
        print(f"\n{COURSES[course]}")
        for _, path in sorted(docs.items()):
            c = chunk_document(path, course)
            print(f"  {len(c):3d} passages  {os.path.splitext(os.path.basename(path))[0]}")
            new_chunks += c

    chunks = json.load(open("chunks.json", encoding="utf-8"))
    # passages de l'ancien format, sans fichier source dans data/ (poly et TD d'Analyse dans ℝⁿ)
    legacy = align_legacy(resplit_legacy([ensure_meta(c) for c in chunks if not c.get("doc")]))
    merged = [ensure_meta(c) for c in legacy + new_chunks]
    json.dump(merged, open("chunks.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"\n{len(new_chunks)} passages depuis data/ + {len(legacy)} anciens = {len(merged)}")

    import build_index
    build_index.main()


if __name__ == "__main__":
    cmd, args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else (None, [])
    if cmd == "sync" and args:
        cmd_sync(args)
    elif cmd == "add" and args:
        if cmd_add(args):
            cmd_build()
    elif cmd == "status" and args:
        cmd_add(args, dry_run=True)
    elif cmd == "build" and not args:
        cmd_build()
    else:
        print(__doc__)
