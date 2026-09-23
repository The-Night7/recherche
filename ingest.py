# -*- coding: utf-8 -*-
"""
Ajout de documents de cours (Séries, Analyse dans ℝⁿ…) en une commande.

    python3 ingest.py sync <lien d'un dossier Drive> [<autre lien>...]
        télécharge le dossier (partagé « tous les utilisateurs disposant du
        lien ») dans data/_drive/, ajoute ce qui n'est pas encore indexé,
        puis reconstruit l'index. Les sous-dossiers sont parcourus.

    python3 ingest.py add <fichiers ou dossiers>...
        pareil à partir de fichiers locaux (PDF, .md, .txt), par exemple un
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
contenu) n'est pas réajouté. Les autres cours du dossier sont ignorés.

PDF scanné (aucun texte extractible) : il est signalé « à transcrire ».
Mettre la transcription Markdown + LaTeX dans
data/<cours>/transcriptions/<nom du PDF>.md puis lancer `build`.
"""
import hashlib
import json
import os
import re
import sys
import zipfile

from clean_extraction import clean_text
from courses import COURSES, detect_course

DATA_ROOT = "data"
DRIVE_DIR = os.path.join(DATA_ROOT, "_drive")
PAGE_SEP = "\n<<<PAGE>>>\n"
SOURCE_EXTS = (".pdf", ".md", ".txt")

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


def collect(paths):
    """Fichiers sources sous les chemins donnés (dossiers parcourus récursivement)."""
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                out += [os.path.join(root, f) for f in sorted(files)
                        if os.path.splitext(f)[1].lower() in SOURCE_EXTS]
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
            return json.load(open(self._hash_file(course), encoding="utf-8"))
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
    added, report = 0, {"déjà là": 0, "autre cours": 0}
    for path in collect(paths):
        stem, ext = os.path.splitext(os.path.basename(path))
        course = detect_course(stem)
        if course is None:
            report["autre cours"] += 1
            continue
        tag = f"[{course}]"
        reason = skip_reason(course, stem)
        if reason:
            print(f"  ignoré        {tag} {stem} ({reason})")
            continue
        if key(stem) in lib.known[course]:
            report["déjà là"] += 1
            continue
        text = extract_file(path).replace("\r\n", "\n")
        # empreinte du texte (et non du fichier) : deux exports du même PDF comptent comme un doublon
        digest = hashlib.sha256(re.sub(r"\s+", " ", text).strip().encode("utf-8")).hexdigest()
        if digest in lib.hashes[course]:
            print(f"  doublon       {tag} {stem} (même texte que {lib.hashes[course][digest]})")
            continue
        letters = sum(ch.isalpha() for ch in text.replace(PAGE_SEP, ""))
        if letters < 150:
            print(f"  à transcrire  {tag} {stem}  (PDF scanné -> data/{course}/transcriptions/{stem}.md)")
            continue
        print(f"  {'à ajouter' if dry_run else 'ajouté':<13} {tag} {stem} ({letters} lettres)")
        lib.known[course][key(stem)] = stem
        lib.hashes[course][digest] = stem
        added += 1
        if not dry_run:
            os.makedirs(course_dir(course), exist_ok=True)
            out_ext = ".md" if ext.lower() == ".md" else ".txt"
            with open(os.path.join(course_dir(course), stem + out_ext), "w", encoding="utf-8") as f:
                f.write(text)

    print(f"\n  {added} {'à ajouter' if dry_run else 'ajouté(s)'}, {report['déjà là']} déjà indexé(s), "
          f"{report['autre cours']} fichier(s) d'autres matières ignoré(s)")
    if not dry_run:
        lib.save()
    return added


def cmd_sync(urls):
    try:
        import gdown
    except ImportError:
        sys.exit("pip install gdown --break-system-packages  (nécessaire pour télécharger depuis Drive)")
    os.makedirs(DRIVE_DIR, exist_ok=True)
    for url in urls:
        print(f"Téléchargement de {url} …")
        try:
            gdown.download_folder(url, output=DRIVE_DIR, quiet=True, remaining_ok=True, resume=True)
        except TypeError:  # anciennes versions de gdown, sans resume
            gdown.download_folder(url, output=DRIVE_DIR, quiet=True, remaining_ok=True)
        except Exception as e:
            sys.exit(f"Échec du téléchargement ({e}).\nLe dossier doit être partagé à « tous les "
                     f"utilisateurs disposant du lien ». Sinon : télécharge-le depuis Drive, "
                     f"dézippe, puis `python3 ingest.py add <dossier>`.")
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
        last = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", m.group(2))  # ElAmine -> El Amine
        author = f"{m.group(1)}. {last}"

    if kind == "td":
        m = re.match(r"TD-?\(?(\d+[ab]?)(?:-(\d+))?\)?", name)
        if m:
            title = f"TD{m.group(1)}" + (f"-{m.group(2)}" if m.group(2) else "")
        else:  # recueil de toutes les feuilles de TD
            title = "Feuilles de TD"
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
        prefix = key(name.split("_")[0])
        title = COURSE_TITLES.get(prefix, "Notes de cours")
    if author and kind in ("cours", "td") and not title.startswith(("TD", "DS")):
        title += f" ({author})"

    years_txt = f"{year}-{year + 1}" if year else "année inconnue"
    return {
        "course": course,
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
        if c >= threshold and len(l) < 90 and not KEEP_LINE_RE.match(l) and len(l) > 2
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
    # un seul gros paragraphe (texte PDF sans lignes vides) : coupe aux lignes
    out = []
    for p in parts:
        while len(p) > MAX_CHARS * 1.3:
            cut = p.rfind("\n", 0, MAX_CHARS)
            cut = cut if cut > MIN_CHARS else MAX_CHARS
            out.append(p[:cut])
            p = p[cut:]
        out.append(p)
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
        if key in seen:  # QCM : chaque copie d'étudiant répète les questions
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


def chunk_document(path, course):
    stem, ext = os.path.splitext(os.path.basename(path))
    meta = parse_meta(stem, course)
    raw = open(path, encoding="utf-8").read()
    fmt = "md" if ext == ".md" else "pdf"
    if fmt == "md":
        secs = sections_markdown(raw)
    else:
        pages = drop_running_lines(fix_glyphs(raw).split(PAGE_SEP), whole_text=meta["kind"] == "cours")
        text = fix_sums(clean_text("\n\n".join(pages)))
        text = re.sub(r"\n{3,}", "\n\n", text)
        secs = (sections_exercises(text, qcm=meta["kind"] == "qcm")
                if meta["kind"] != "cours" else sections_course_pdf(text))
    secs = merge_small([(l, t) for l, t in secs if t.strip()])
    chunks = []
    for label, body in secs:
        for sub_label, sub in split_long(label, body):
            if len(sub.strip()) < 40:
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
    legacy = [c for c in chunks if not c.get("doc")]
    merged = legacy + new_chunks
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
