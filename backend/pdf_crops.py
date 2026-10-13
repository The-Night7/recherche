# -*- coding: utf-8 -*-
"""
Image d'une formule découpée dans la page du PDF d'origine.

Quand reflow ne sait pas reconstruire une formule (grandes parenthèses,
fractions imbriquées...), il la garde en bloc source « pdf ». Si le PDF est
présent sur la machine, on retrouve ce bloc dans la page grâce aux positions
des mots (pdftotext -bbox-layout) et on affiche la zone de la page elle-même :
c'est la formule telle qu'elle est imprimée, sans interprétation.
"""
import difflib
import html
import re
import subprocess
import unicodedata
from collections import Counter
from functools import lru_cache
from urllib.parse import urlencode

WORD_RE = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>')
FENCE_RE = re.compile(r"^([ \t]*)(`{3,})(pdf(?:-steps|-matrix)?)[ \t]*\n(.*?)\n[ \t]*\2[ \t]*$", re.M | re.S)
MARGIN = 4.0      # points autour de la zone
STACK = 12.0      # hauteur d'un numérateur / dénominateur au-dessus ou au-dessous de la ligne
ROW_GAP = 16.0    # interligne au-delà duquel deux groupes de mots sont distincts
MIN_FOUND = 0.8     # part du bloc extrait qui doit être retrouvée dans la page
MIN_SHOWN = 0.7     # part de l'image qui doit venir du bloc
LINE_HEIGHT = 16.0  # hauteur maximale d'une ligne du bloc extrait, en points
CHAR_WIDTH = 9.0   # largeur maximale d'un caractère du bloc extrait, en points
GAP = 14.0        # espace maximal entre deux morceaux d'une même formule sur une ligne


def norm(text):
    """Comparaison insensible aux espaces et aux exposants (n² du texte extrait = n 2 du PDF)."""
    text = unicodedata.normalize("NFKC", html.unescape(text)).replace("−", "-")
    return re.sub(r"\s+", "", text)


@lru_cache(maxsize=256)
def page_words(path, number):
    """[(texte, x0, y0, x1, y1)] dans l'ordre de lecture de pdftotext, ou ()."""
    try:
        out = subprocess.run(["pdftotext", "-bbox-layout", "-f", str(number), "-l", str(number), path, "-"],
                             capture_output=True, timeout=60, check=True).stdout.decode("utf-8", "replace")
    except (subprocess.SubprocessError, OSError):
        return ()
    return tuple((m[5], float(m[1]), float(m[2]), float(m[3]), float(m[4])) for m in WORD_RE.finditer(out))


def locate(words, source):
    """(part du bloc retrouvée, zone (x0, y0, x1, y1)) du bloc `source` dans la page, ou None."""
    target = norm(source)
    if len(target) < 3:
        return None
    chars, owner = [], []
    for i, word in enumerate(words):
        for ch in norm(word[0]):
            chars.append(ch)
            owner.append(i)
    page = "".join(chars)
    matcher = difflib.SequenceMatcher(None, page, target, autojunk=False)
    # Un caractère isolé (« 1 », « = », « x ») se retrouve partout : seuls les
    # morceaux d'au moins deux caractères situent le bloc.
    blocks = [b for b in matcher.get_matching_blocks() if b.size >= 2]
    if not blocks:
        return None
    anchor = max(blocks, key=lambda b: b.size)
    if anchor.size < 3:
        return None
    near = [b for b in blocks if abs(b.a - anchor.a) <= len(target)]
    matched = {}
    for b in near:
        for k in range(b.size):
            matched[owner[b.a + k]] = matched.get(owner[b.a + k], 0) + 1
    # Garder le groupe de lignes le plus fourni : un morceau retrouvé dans le
    # paragraphe voisin, séparé par un interligne, n'appartient pas à la formule.
    rows = sorted(matched, key=lambda i: words[i][2])
    groups, current = [], [rows[0]]
    for i in rows[1:]:
        if words[i][2] - max(words[j][4] for j in current) > ROW_GAP:
            groups.append(current)
            current = []
        current.append(i)
    groups.append(current)
    hit = max(groups, key=lambda g: sum(matched[i] for i in g))
    x0 = min(words[i][1] for i in hit)
    y0 = min(words[i][2] for i in hit)
    x1 = max(words[i][3] for i in hit)
    y1 = max(words[i][4] for i in hit)
    # Numérateurs, dénominateurs, indices et grandes parenthèses : les mots
    # juste au-dessus / au-dessous, ou collés à droite / à gauche sur les mêmes
    # lignes, en font partie. La bande verticale reste celle des mots retrouvés :
    # l'extension ne doit pas remonter de ligne en ligne dans le paragraphe voisin.
    top, bottom = y0 - STACK, y1 + STACK
    changed = True
    while changed:
        changed = False
        for _, a, b, c, d in words:
            inside = a >= x0 - GAP and c <= x1 + GAP and b >= top and d <= bottom
            if inside and (a < x0 or b < y0 or c > x1 or d > y1):
                x0, y0, x1, y1 = min(x0, a), min(y0, b), max(x1, c), max(y1, d)
                changed = True
    # Un mot à moitié dans la zone serait coupé en deux dans l'image : on
    # l'inclut, en une seule passe (sinon la zone s'étendrait de proche en proche).
    grown = [x0, y0, x1, y1]
    for _, a, b, c, d in words:
        overlap = min(d, y1) - max(b, y0)
        if a < x1 + MARGIN and c > x0 - MARGIN and overlap >= 0.5 * (d - b) and (b < y0 or d > y1 or a < x0 or c > x1):
            grown = [min(grown[0], a), min(grown[1], b), max(grown[2], c), max(grown[3], d)]
    x0, y0, x1, y1 = grown
    # Une zone bien plus grande que le bloc extrait contient autre chose que
    # la formule (le paragraphe autour) : mieux vaut garder le texte.
    lines = sum(1 for line in source.split("\n") if line.strip())
    if y1 - y0 > LINE_HEIGHT * lines + 24 or x1 - x0 > max(120, CHAR_WIDTH * len(target)):
        return None
    # Validation sans tenir compte de l'ordre (pdftotext lit les numérateurs,
    # puis la ligne, puis les dénominateurs) : l'image doit contenir presque tout
    # le bloc, et presque rien d'autre.
    inside = Counter("".join(norm(w[0]) for w in words if w[1] >= x0 and w[3] <= x1 and w[2] >= y0 and w[4] <= y1))
    common = sum((inside & Counter(target)).values())
    score = common / len(target)
    if score < MIN_FOUND or common < MIN_SHOWN * sum(inside.values()):
        return None
    return score, (round(x0 - MARGIN, 1), round(y0 - MARGIN, 1), round(x1 + MARGIN, 1), round(y1 + MARGIN, 1))


def crop_query(doc, path, pages, source):
    """Paramètres de /api/crop pour ce bloc (la page où il est le mieux retrouvé), ou None."""
    found = [(located, number) for number in pages for located in [locate(page_words(path, number), source)] if located]
    if not found:
        return None
    (_, box), number = max(found, key=lambda f: f[0][0])
    return urlencode({"doc": doc, "n": number, "box": ",".join(map(str, box))})


def with_crops(markdown, doc, path, pages):
    """Ajoute « crop=… » à la ligne d'ouverture des blocs source « pdf » retrouvés dans la page."""
    def fence(m):
        indent, ticks, language, body = m.groups()
        source = "\n".join(line[len(indent):] if line.startswith(indent) else line for line in body.split("\n"))
        query = crop_query(doc, path, pages, source)
        head = f"{indent}{ticks}{language}" + (f" crop={query}" if query else "")
        return f"{head}\n{body}\n{indent}{ticks}"
    return FENCE_RE.sub(fence, markdown)
