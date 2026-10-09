# -*- coding: utf-8 -*-
"""
Ajoute le cours de Séries (CM, TD, DS, QCM, corrigés) à l'index.

Deux étapes :

  1) extraction (une seule fois, ou quand tu ajoutes des fichiers) :
         python3 ingest_series.py extract ~/Cours/Series/*.pdf ~/Cours/Series/*.md
     -> écrit le texte brut de chaque document dans data/series/<nom>.txt
        (ou .md pour les notes Markdown/LaTeX). Les PDF scannés (aucun
        texte extractible) sont signalés : il faut alors mettre une
        transcription dans data/series/transcriptions/<même nom>.md

  2) découpage + fusion + index :
         python3 ingest_series.py build
     -> découpe chaque document en passages (un exercice, une section
        de cours...), remplace les passages "series" de chunks.json,
        puis relance build_index.py.

Les métadonnées (type, numéro, année, version, corrigé) sont déduites du
nom de fichier, au format du dossier partagé :
    TD4_20242025_Series_P2S1_DMaths.pdf
    DS120232024V4Correction_SeriesDS_P2S1_EMasnada.pdf
    QCM1-2022-2023_Series-DS_P2S1_DMaths.pdf
    2024-09-17-CM_2024-2025_Series_P1S1_NZoghlami_MathisS.md
"""
import json
import os
import re
import sys
import zipfile

from clean_extraction import clean_text

COURSE = "series"
DATA_DIR = os.path.join("data", "series")
TRANSCRIPTIONS_DIR = os.path.join(DATA_DIR, "transcriptions")
PAGE_SEP = "\n<<<PAGE>>>\n"

# documents volontairement ignorés (texte extrait inexploitable)
SKIP = {
    "CMAnnotee_20222023_Series_P2S1_MX": "notes manuscrites, OCR illisible",
}

MAX_CHARS = 2400
MIN_CHARS = 250


# --------------------------------------------------------------------------
# 1) Extraction
# --------------------------------------------------------------------------

def extract_file(path):
    raw = open(path, "rb").read()
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


def cmd_extract(paths):
    os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)
    for path in paths:
        stem, ext = os.path.splitext(os.path.basename(path))
        if stem in SKIP:
            print(f"  ignoré   {stem} ({SKIP[stem]})")
            continue
        text = extract_file(path).replace("\r\n", "\n")
        letters = sum(ch.isalpha() for ch in text.replace(PAGE_SEP, ""))
        if letters < 150:
            has_tr = os.path.exists(os.path.join(TRANSCRIPTIONS_DIR, stem + ".md"))
            print(f"  scanné   {stem}" + ("  (transcription présente)" if has_tr else "  -> à transcrire"))
            continue
        out_ext = ".md" if ext.lower() == ".md" else ".txt"
        with open(os.path.join(DATA_DIR, stem + out_ext), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  ok       {stem} ({letters} lettres)")


# --------------------------------------------------------------------------
# 2) Métadonnées depuis le nom de fichier
# --------------------------------------------------------------------------

YEAR_RE = re.compile(r"(20\d{2})\D?(20\d{2})")
AUTHOR_RE = re.compile(r"_P\dS\d_+([A-Z][a-z]?)([A-Z][A-Za-z]+)")
CM_SUBJECTS = {
    "derivation": "Dérivation",
    "comparaisonlocale": "Comparaison locale des fonctions",
}


def parse_meta(stem):
    name = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)  # préfixe de date des notes .md
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
    elif upper.startswith("TD"):
        kind = "td"
    else:
        kind = "cours"

    corrige = "correction" in name.lower()
    author = None
    m = AUTHOR_RE.search(stem)
    if m and m.group(2) not in ("Maths", "Inconnu"):
        author = f"{m.group(1)}. {m.group(2)}"

    if kind == "td":
        num = re.match(r"TD(\d+[ab]?)", name).group(1)
        title = f"TD{num}"
    elif kind == "ds":
        m = re.match(r"DS[-_]?(\d)", name)
        title = f"DS{m.group(1)}"
        v = re.search(r"V(\d)", name)
        if v:
            title += f" V{v.group(1)}"
        if re.search(r"rat+rapage", name, re.I):
            title += " rattrapage"
    elif kind == "qcm":
        title = "QCM" + re.match(r"QCM(\d)", name).group(1)
    else:
        m = re.match(r"CM[-_]?([A-Za-z]+)?", name)
        sub = (m.group(1) or "").lower() if m else ""
        title = CM_SUBJECTS.get(sub, "Notes de cours")
    if author and kind == "cours":
        title += f" ({author})"

    years_txt = f"{year}-{year + 1}" if year else "année inconnue"
    return {
        "course": COURSE,
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


def fix_glyphs(text):
    """À appliquer AVANT clean_text (qui supprime les caractères de contrôle)."""
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


MD_HEAD_RE = re.compile(r"(?m)^(#{1,4})\s+(.+?)\s*$")


def sections_markdown(text):
    text = re.sub(r"(?s)^---\n.*?\n---\n", "", text)  # front-matter
    marks = list(MD_HEAD_RE.finditer(text))
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


def chunk_document(path):
    stem, ext = os.path.splitext(os.path.basename(path))
    meta = parse_meta(stem)
    with open(path, encoding="utf-8") as source:
        raw = source.read()
    fmt = "md" if ext == ".md" else "pdf"
    title = re.match(r"#\s+(.+)", raw)
    if fmt == "md" and stem.startswith("Fiche") and title:
        # fiches de révision : le titre du fichier garde les accents (« Fiche 2 : Séries de référence »)
        years_txt = f"{meta['year']}-{meta['year'] + 1}" if meta["year"] else "année inconnue"
        meta["title"] = title.group(1).strip()
        meta["doc_label"] = f"{meta['title']} · {years_txt}"
    if fmt == "md":
        secs = sections_markdown(raw)
    else:
        pages = drop_running_lines(fix_glyphs(raw).split(PAGE_SEP), whole_text=meta["kind"] == "cours")
        text = fix_sums(clean_text("\n\n".join(pages)))
        text = re.sub(r"\n{3,}", "\n\n", text)
        secs = (sections_exercises(text, qcm=meta["kind"] == "qcm")
                if meta["kind"] != "cours" else sections_course_pdf(text))
    secs = [(l, t) for l, t in secs if t.strip()]
    if meta["kind"] == "cours":
        secs = merge_small(secs)
    chunks = []
    for label, body in secs:
        # Un corrigé reste entier, même si ses calculs dépassent MAX_CHARS.
        parts = split_long(label, body) if meta["kind"] == "cours" else [(label, body)]
        for sub_label, sub in parts:
            if not sub.strip() or (meta["kind"] == "cours" and len(sub.strip()) < 40):
                continue
            if sub_label.startswith("Diapos"):  # pas de titres : 1re ligne parlante
                first = next((l.strip() for l in sub.split("\n") if len(l.strip()) > 12), "")
                sub_label = first[:70] + ("…" if len(first) > 70 else "")
            chunks.append({
                **meta,
                "fmt": fmt,
                "section": sub_label,
                "label": f"{meta['doc_label']} — {sub_label}",
                "text": sub.strip(),
            })
    return chunks


def cmd_build():
    docs = {}
    for folder in (DATA_DIR, TRANSCRIPTIONS_DIR):  # une transcription remplace le texte extrait
        if not os.path.isdir(folder):
            continue
        for f in sorted(os.listdir(folder)):
            stem, ext = os.path.splitext(f)
            if ext in (".txt", ".md") and stem not in SKIP and not f.startswith("README"):
                docs[stem] = os.path.join(folder, f)

    series_chunks = []
    for stem, path in sorted(docs.items()):
        c = chunk_document(path)
        print(f"  {len(c):3d} passages  {stem}")
        series_chunks += c

    chunks = json.load(open("chunks.json", encoding="utf-8"))
    kept = [c for c in chunks if c.get("course") != COURSE]
    merged = kept + series_chunks
    json.dump(merged, open("chunks.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"\n{len(series_chunks)} passages Séries + {len(kept)} autres = {len(merged)}")

    import build_index
    build_index.main()


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "extract":
        cmd_extract(sys.argv[2:])
    elif len(sys.argv) == 2 and sys.argv[1] == "build":
        cmd_build()
    else:
        print(__doc__)
