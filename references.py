# -*- coding: utf-8 -*-
"""
Références structurées dans une question : "td 1 exercice 2", "TD1 ex 2",
"ds1 v2 exo 3", "qcm 4", "exercice 5"...

Le TF-IDF ne peut pas les traiter : "td", "1", "2" font moins de 3
caractères et sont jetés par tokenize(), il ne reste que "exercice",
présent dans presque tous les passages de TD -> résultats au hasard
(tirés par le bonus de récence). On les extrait donc de la question et
on les applique comme un filtre exact sur les métadonnées des passages.
"""
import re

from text_utils import strip_accents

KIND_ALIASES = {"td": "td", "ds": "ds", "qcm": "qcm", "cc": "ds", "partiel": "ds", "examen": "ds"}

# td 1 / td1 / td n°1 / td-2a / ds1 v2
DOC_RE = re.compile(
    r"\b(td|ds|qcm|cc|partiel|examen)\s*(?:n\s*[o°]?\s*|[-.#]\s*)?(\d{1,2})([a-d])?\b"
    r"(?:\s*(?:version\s*|v\s*)(\d))?"
)
# exercice 2 / exercices 2 et 3 / ex 2 / exo2 / ex. 2 / exercice n°2
EX_RE = re.compile(
    r"\b(?:exercices?|exos?|ex)\s*(?:n\s*[o°]?\s*|[-.#]\s*)?(\d{1,2}(?:\s*(?:,|et|&|-|a)\s*\d{1,2})*)\b"
)
VERSION_RE = re.compile(r"\b(?:version\s*|v)(\d)\b")

# titre d'un document : "TD1", "TD2a", "DS1 V2", "DS3 rattrapage", "QCM4",
# ou label de l'ancien format "TD1 : Normes, ..." / "TD1 1 : ..."
TITLE_RE = re.compile(r"^(TD|DS|QCM)\s*(\d+)([a-d])?(?:\s+V(\d+))?", re.I)
SECTION_EX_RE = re.compile(r"exercice\s+(\d+)", re.I)
HEADER_EX_RE = re.compile(r"^\s*exercice\s+(\d+)\b", re.I | re.M)


def _numbers(s):
    out = set()
    for part in re.split(r"\s*(?:,|et|&)\s*", s):
        m = re.fullmatch(r"(\d+)\s*(?:-|a)\s*(\d+)", part.strip())
        if m:
            lo, hi = int(m.group(1)), int(m.group(2))
            if lo <= hi <= lo + 20:
                out.update(range(lo, hi + 1))
        elif part.strip().isdigit():
            out.add(int(part))
    return out


def parse_reference(question):
    """-> (ref, reste de la question). ref = dict ou None :
    {"kind", "num", "variant", "version", "exercises"} (valeurs None si absentes)."""
    q = strip_accents(question.lower())
    ref = {"kind": None, "num": None, "variant": None, "version": None, "exercises": None}

    m = DOC_RE.search(q)
    if m:
        ref["kind"] = KIND_ALIASES[m.group(1)]
        ref["num"] = int(m.group(2))
        ref["variant"] = m.group(3)
        ref["version"] = int(m.group(4)) if m.group(4) else None
        q = q[:m.start()] + " " + q[m.end():]

    m = EX_RE.search(q)
    if m:
        ref["exercises"] = _numbers(m.group(1)) or None
        q = q[:m.start()] + " " + q[m.end():]

    if ref["kind"] and ref["version"] is None:
        m = VERSION_RE.search(q)
        if m:
            ref["version"] = int(m.group(1))
            q = q[:m.start()] + " " + q[m.end():]

    if ref["kind"] is None and ref["exercises"] is None:
        return None, question
    return ref, q


def describe(ref):
    parts = []
    if ref["kind"]:
        d = f"{ref['kind'].upper()}{ref['num']}{ref['variant'] or ''}"
        if ref["version"]:
            d += f" V{ref['version']}"
        parts.append(d)
    if ref["exercises"]:
        ex = sorted(ref["exercises"])
        parts.append(("exercice " if len(ex) == 1 else "exercices ") + ", ".join(map(str, ex)))
    return " · ".join(parts)


def highlight_terms(ref):
    """termes à surligner dans l'interface (\"exercice 2\")."""
    return [f"exercice {n}" for n in sorted(ref["exercises"] or [])]


def annotate(chunks):
    """Ajoute à chaque passage :
      _doc = (kind, num, variant, version) ou None
      _ex  = ensemble des numéros d'exercice couverts
    Pour l'ancien format (Analyse dans Rⁿ), les exercices ne sont pas dans
    la section : on lit les en-têtes "Exercice N" du texte, et un passage qui
    ne commence pas par un en-tête continue l'exercice du passage précédent."""
    prev_label, current = None, None
    for c in chunks:
        m = TITLE_RE.match(c.get("title") or c.get("label", ""))
        c["_doc"] = (
            (m.group(1).lower(), int(m.group(2)), (m.group(3) or "").lower() or None,
             int(m.group(4)) if m.group(4) else None)
            if m else None
        )

        sec_nums = {int(n) for n in SECTION_EX_RE.findall(c.get("section", ""))}
        if sec_nums:
            c["_ex"] = sec_nums
            prev_label, current = c.get("label"), max(sec_nums)
            continue

        if c.get("label") != prev_label:
            current = None
        text = c.get("text", "")
        headers = [int(n) for n in HEADER_EX_RE.findall(text)]
        ex = set(headers)
        first = HEADER_EX_RE.search(text)
        if current is not None and (not first or text[:first.start()].strip()):
            ex.add(current)  # début du passage = suite de l'exercice précédent
        c["_ex"] = ex
        if headers:
            current = headers[-1]
        prev_label = c.get("label")
    return chunks


def match(chunk, ref, use_exercises=True):
    d = chunk.get("_doc")
    if ref["kind"]:
        if not d or d[0] != ref["kind"] or d[1] != ref["num"]:
            return False
        if ref["variant"] and d[2] != ref["variant"]:
            return False
        if ref["version"] and d[3] != ref["version"]:
            return False
    if use_exercises and ref["exercises"]:
        if not (chunk.get("_ex") or set()) & ref["exercises"]:
            return False
    return True
