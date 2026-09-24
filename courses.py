# -*- coding: utf-8 -*-
"""Matières et rattachement explicite à une année de Préing et un semestre.
`year` reste l'année scolaire du document, indépendante de `study_year`.
"""
import re
import unicodedata
from pathlib import Path

CURRICULA = {
    f"preing-{year}-s{semester}": {
        "id": f"preing-{year}-s{semester}",
        "label": f"Préing {year} — semestre {semester}",
        "study_year": year, "semester": semester,
    }
    for year in (1, 2) for semester in (1, 2)
}
# Contexte des anciens passages d'Analyse dans ℝⁿ, sans métadonnées.
CURRICULUM = CURRICULA["preing-2-s1"]
SUBJECTS = {
    "preing-1-s1": {
        "algebre1": ("Algèbre 1", "Algebre1"),
        "analyse1": ("Analyse 1", "Analyse1"),
        "cef1": ("CEF 1", "CEF1"),
        "ic1": ("IC 1", "IC1"),
        "informatique1": ("Informatique 1", "Informatique1"),
        "physique1": ("Physique 1", "Physique1"),
        "projet1-s1": ("Projet 1", "Projet1"),
    },
    "preing-1-s2": {
        "algebre2": ("Algèbre 2", "Algebre2"),
        "analyse2": ("Analyse 2", "Analyse2"),
        "informatique2": ("Informatique 2", "Informatique2"),
        "mecanique-du-point": ("Mécanique du point", "Mecanique-du-point"),
        "projet1-s2": ("Projet 1", "Projet1"),
    },
    "preing-2-s1": {
        "analyse-rn": ("Analyse dans ℝⁿ", "Analyse-dans-RN"),
        "series": ("Séries", "Series"),
        "informatique3": ("Informatique 3", "Informatique3"),
        "electromagnetisme": ("Électromagnétisme", "Electromagnetisme"),
        "shs": ("SHS", "SHS"),
    },
    "preing-2-s2": {
        "algebre-lineaire": ("Algèbre linéaire", "Algebre-lineaire"),
        "ethique": ("Éthique", "Etique"),
        "histoire-du-design": ("Histoire du design", "Histoire-du-design"),
        "informatique4": ("Informatique 4", "Informatique4"),
        "integration-proba": ("Intégration et probabilités", "Integration-proba"),
        "ondes": ("Ondes", "Ondes"),
        "physique-moderne": ("Physique moderne", "Physique-moderne"),
    },
}
COURSES = {cid: name for subjects in SUBJECTS.values() for cid, (name, _) in subjects.items()}
COURSE_CURRICULA = {cid: ctx for ctx, subjects in SUBJECTS.items() for cid in subjects}
PLAIN_TEXT_COURSES = {"informatique1", "informatique2", "informatique3", "informatique4",
                      "shs", "ethique", "histoire-du-design", "cef1", "ic1", "projet1-s1", "projet1-s2"}
KINDS = {"cours": "Cours", "td": "TD", "tp": "TP", "ds": "DS", "cc": "CC", "qcm": "QCM", "projet": "Projets"}


def normalized(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", value)


def course_context(course):
    return CURRICULA[COURSE_CURRICULA[course]]


def subject_in_context(name, context):
    name = re.sub(r"(?:ds|cc|projets?|tp)$", "", normalized(name))
    for cid, (_, alias) in SUBJECTS.get(context, {}).items():
        if name in (normalized(alias), normalized(cid)):
            return cid
    return None


def detect_course(stem):
    match = re.search(r"_([^_]+)_+P([12])S([12])(?:_|$)", stem, re.I)
    if match:
        return subject_in_context(match[1], f"preing-{match[2]}-s{match[3]}")
    return None


def source_course(path):
    """Le dossier PREINGx-Sy/Matière fait foi, même si un nom est mal étiqueté."""
    parts = Path(path).parts
    for i, part in enumerate(parts[:-1]):
        match = re.fullmatch(r"PREING([12])-S([12])", part, re.I)
        if not match:
            continue
        context = f"preing-{match[1]}-s{match[2]}"
        if i + 2 < len(parts):
            return subject_in_context(parts[i + 1], context)
        # Fiches Word déposées directement à la racine du semestre.
        name = normalized(Path(path).stem)
        if context == "preing-2-s2":
            if "algebre" in name:
                return "algebre-lineaire"
            if "probabilit" in name or "integration" in name:
                return "integration-proba"
        cid = detect_course(Path(path).stem)
        return cid if cid and COURSE_CURRICULA[cid] == context else None
    return detect_course(Path(path).stem)


def ensure_meta(chunk):
    if "course" not in chunk:
        label = chunk["label"]
        match = re.search(r"(20\d{2})-(20\d{2})", label)
        chunk.update({
            "course": "analyse-rn", "kind": "td" if label.startswith("TD") else "cours",
            "corrige": "correction" in label.lower(), "year": int(match[1]) if match else None,
            "fmt": "pdf", "doc_label": label.split(" — ")[0],
            "section": label.split(" — ", 1)[1] if " — " in label else "",
        })
    context = course_context(chunk["course"])
    chunk.update(curriculum=context["id"], study_year=context["study_year"], semester=context["semester"])
    return chunk
