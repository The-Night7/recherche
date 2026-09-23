# -*- coding: utf-8 -*-
"""
Registre des cours indexés et métadonnées communes à tous les passages :
  course  : identifiant du cours ("analyse-rn", "series")
  kind    : "cours" | "td" | "ds" | "qcm"
  corrige : True pour une correction / un corrigé
  year    : année de début de l'année scolaire (2024 pour 2024-2025) ou None
"""
import re

COURSES = {
    "analyse-rn": "Analyse dans ℝⁿ",
    "series": "Séries",
}
KINDS = {"cours": "Cours", "td": "TD", "ds": "DS", "qcm": "QCM"}

# nom du cours dans les fichiers du dossier partagé (sans tirets ni casse)
# -> identifiant ; "_Series-DS_" et "_SeriesDS_" donnent le même cours
COURSE_ALIASES = {
    "series": "series",
    "analysedansrn": "analyse-rn",
}
_COURSE_IN_NAME = re.compile(r"_([A-Za-z-]+?)(?:-?DS)?_+P\dS\d")


def detect_course(stem):
    """"DS2-2024-2025-V1_Analyse-dans-RN-DS_P2S1_DMaths" -> "analyse-rn" (None si inconnu)."""
    m = _COURSE_IN_NAME.search(stem)
    if not m:
        return None
    return COURSE_ALIASES.get(re.sub(r"[^a-z0-9]", "", m.group(1).lower()))


def ensure_meta(chunk):
    """Complète les passages de l'ancien format (label + text seulement),
    qui sont tous issus du cours d'Analyse dans ℝⁿ."""
    if "course" in chunk:
        return chunk
    label = chunk["label"]
    m = re.search(r"(20\d{2})-(20\d{2})", label)
    chunk.update({
        "course": "analyse-rn",
        "kind": "td" if label.startswith("TD") else "cours",
        "corrige": "correction" in label.lower(),
        "year": int(m.group(1)) if m else None,
        "fmt": "pdf",
        "doc_label": label.split(" — ")[0],
        "section": label.split(" — ", 1)[1] if " — " in label else "",
    })
    return chunk
