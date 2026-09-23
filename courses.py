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
