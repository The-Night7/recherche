# -*- coding: utf-8 -*-
"""Matières et rattachement explicite au cycle, à une année, un semestre et un parcours.
`year` reste l'année scolaire du document, indépendante de `study_year`.
"""
import re
import unicodedata
from pathlib import Path

PROGRAMS = {"preing": "Préing", "ing": "Ing"}

CURRICULA = {
    f"preing-{year}-s{semester}": {
        "id": f"preing-{year}-s{semester}",
        "label": f"Préing {year} — semestre {semester}",
        "program": "preing", "study_year": year, "semester": semester, "track": None,
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
# Les parcours restent ceux des dossiers fournis : aucun parcours n'est
# supposé pour Ing 2. Les documents de rentrée d'Ing 1 n'ont pas de semestre.
ING_SUBJECTS = {
    "ing-1": (1, None, None, {"informations": ("Informations générales", "Informations générales")}),
    "ing-1-s1-gm": (1, 1, "gm", {
        "algebre": ("Algèbre", "ALGEBRE"),
        "algorithmique": ("Algorithmique", "ALGO"),
        "bdd": ("Bases de données", "BDD"),
        "cef": ("CEF", "CEF"),
        "data-exploration": ("Data exploration", "DATA EXPLORATION"),
        "design": ("Histoire du design", "DESIGN"),
        "ethique": ("Éthique", "ETHIQUE"),
        "mesures-integration": ("Mesures et intégration", "MESURE INTÉ"),
        "optimisation": ("Optimisation", "OPTIMISATION"),
        "probabilites": ("Probabilités", "PROBA"),
        "programmation-procedurale": ("Programmation procédurale", "PROGRAMMATION PROCEDURAL"),
        "unix": ("Unix", "UNIX"),
        "informations": ("Informations générales", "Informations générales"),
    }),
    "ing-1-s1-info": (1, 1, "info", {
        "bdd": ("Bases de données", "BDD"),
        "complement-maths": ("Compléments de mathématiques", "Complement-Maths"),
        "data-exploration": ("Data exploration", "Data-Exploration"),
        "mesures-integration": ("Mesures et intégration", "Mesures-et-integration"),
        "probabilites": ("Probabilités", "Proba"),
        "systeme-exploitation": ("Systèmes d'exploitation", "Systeme-Exploitation"),
        "unix": ("Unix", "Unix"),
    }),
    "ing-1-s2-data": (1, 2, "data", {
        "analyse-numerique": ("Analyse numérique", "Analyse numérique"),
        "data-mining": ("Data mining", "Data Mining"),
        "equations-differentielles": ("Équations différentielles", "Equation différentielles"),
        "gestion-entreprise": ("Gestion d'entreprise", "Gestion Entreprise"),
        "projet": ("Projet GM", "Projet GM"),
        "statistique-inferentielle": ("Statistique inférentielle", "Statistique inférentielle"),
        "systeme-exploitation": ("Systèmes d'exploitation", "Système d_exploitation"),
        "theorie-graphes": ("Théorie des graphes", "Théorie des graphes"),
        "theorie-langages": ("Théorie des langages", "Théorie des langages"),
        "informations": ("Informations générales", "Informations générales"),
    }),
    "ing-2-s1": (2, 1, None, {
        "anglais": ("Anglais", "Anglais"),
        "architecture-reseau": ("Architecture réseau", "Architecture réseau"),
        "communication-interculturelle": ("Communication interculturelle", "Communication InterCulturelle"),
        "data-mining": ("Data mining 2", "Data Mining 2"),
        "decidabilite-complexite": ("Décidabilité et complexité", "Décidabilité & Complexité"),
        "ece": ("ECE", "ECE"),
        "modele-lineaire": ("Modèle linéaire", "Modéle linéaire"),
        "optimisation-deterministe": ("Optimisation déterministe", "Optimisation déterministe"),
        "programmation-fonctionnelle": ("Programmation fonctionnelle", "Programmation fonctionelle"),
        "traitement-signal": ("Traitement du signal", "Traitement du signal"),
        "economie": ("Économie", "Économie"),
    }),
    "ing-2-s2": (2, 2, None, {
        "compressive-sensing": ("Compressive sensing", "Compressive Sensing"),
        "design-decision": ("Design de la décision", "Design de la décision"),
        "edp": ("Équations aux dérivées partielles", "EDP"),
        "ia": ("Intelligence artificielle", "IA"),
        "methodes-agiles": ("Méthodes agiles", "Methodes Agile"),
        "programmation-parallele": ("Programmation parallèle", "Programmation Parralèle"),
        "series-temporelles": ("Séries temporelles", "Série temporelle"),
    }),
}
for context, (year, semester, track, subjects) in ING_SUBJECTS.items():
    label = f"Ing {year}" + (f" — semestre {semester}" if semester else " — hors semestre")
    if track:
        label += f" — {track.upper()}"
    CURRICULA[context] = dict(id=context, label=label, program="ing", study_year=year, semester=semester, track=track)
    SUBJECTS[context] = {f"{context}-{cid}": entry for cid, entry in subjects.items()}

COURSES = {cid: name for subjects in SUBJECTS.values() for cid, (name, _) in subjects.items()}
COURSE_CURRICULA = {cid: ctx for ctx, subjects in SUBJECTS.items() for cid in subjects}
PLAIN_TEXT_COURSES = {"informatique1", "informatique2", "informatique3", "informatique4",
                      "shs", "ethique", "histoire-du-design", "cef1", "ic1", "projet1-s1", "projet1-s2"}
PLAIN_TEXT_COURSES.update(
    f"{context}-{cid}" for context, (_, _, _, subjects) in ING_SUBJECTS.items() for cid in subjects
    if cid in {"algorithmique", "bdd", "cef", "design", "ethique", "programmation-procedurale", "unix",
               "informations", "projet", "systeme-exploitation", "theorie-langages", "anglais", "architecture-reseau",
               "communication-interculturelle", "ece", "programmation-fonctionnelle", "economie", "design-decision",
               "methodes-agiles", "programmation-parallele"}
)
KINDS = {"cours": "Cours", "td": "TD", "tp": "TP", "ds": "DS", "cc": "CC", "qcm": "QCM", "projet": "Projets", "ressource": "Ressources", "infos": "Informations"}


def normalized(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", value)


def course_context(course):
    return CURRICULA[COURSE_CURRICULA[course]]


def subject_in_context(name, context):
    name = re.sub(r"(?:ds|cc|projets?|tp)$", "", normalized(name))
    if context == "ing-2-s1" and name == "modelelineairebis":
        name = "modelelineaire"
    for cid, (_, alias) in SUBJECTS.get(context, {}).items():
        if name in (normalized(alias), normalized(cid)):
            return cid
    return None


def detect_course(stem):
    match = re.search(r"_([^_]+)_+P([12])S([12])(?:_|$)", stem, re.I)
    if match:
        return subject_in_context(match[1], f"preing-{match[2]}-s{match[3]}")
    return None


def ing_source_context(path):
    parts = Path(path).parts
    for i, part in enumerate(parts[:-1]):
        match = re.fullmatch(r"ING[ -]?([12])", part.strip(), re.I)
        if not match:
            continue
        year = int(match[1])
        if i + 2 == len(parts):
            return (f"ing-{year}", parts[i + 1:])
        semester = re.fullmatch(r"(?:S|Semestre\s*)([12])(?:\s+(GM|INFO|DATA))?", parts[i + 1].strip(), re.I)
        if not semester:
            return None
        track = semester[2].lower() if semester[2] else None
        context = f"ing-{year}-s{semester[1]}" + (f"-{track}" if track else "")
        return context, parts[i + 2:]
    return None


def ing_source_course(path):
    found = ing_source_context(path)
    if not found:
        return None
    context, tail = found
    if context not in SUBJECTS:
        return None
    if len(tail) == 1:
        if context == "ing-2-s2" and normalized(tail[0]).startswith("methodesagile"):
            return context + "-methodes-agiles"
        return context + "-informations" if context + "-informations" in SUBJECTS[context] else None
    if context == "ing-1-s1-gm" and normalized(tail[0]) == "examen":
        name = normalized(Path(path).stem)
        for hint, cid in {"design": "design", "algo": "algorithmique", "optimisation": "optimisation", "proba": "probabilites",
                          "algebre": "algebre", "unix": "unix", "ethique": "ethique", "bdd": "bdd", "information": "informations"}.items():
            if hint in name:
                return context + "-" + cid
        return None
    return subject_in_context(tail[0], context)


def source_course(path):
    """Le dossier PREINGx-Sy/Matière fait foi, même si un nom est mal étiqueté."""
    ing_course = ing_source_course(path)
    if ing_course:
        return ing_course
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
    chunk.update(curriculum=context["id"], program=context["program"], study_year=context["study_year"],
                 semester=context["semester"], track=context["track"])
    return chunk
