# -*- coding: utf-8 -*-
"""
Normalisation et tokenisation du texte (français), sans dépendance
externe (pas de nltk/spacy) : on enlève les accents, on découpe sur
les caractères non-alphanumériques, on retire les mots vides.
"""
import re
import unicodedata

STOPWORDS = {
    "le", "la", "les", "un", "une", "des", "de", "du", "et", "en", "que", "qui",
    "est", "sont", "pour", "dans", "sur", "par", "avec", "au", "aux", "ce", "ces",
    "cette", "son", "sa", "ses", "je", "tu", "il", "elle", "nous", "vous", "ils",
    "elles", "mais", "ou", "donc", "or", "ni", "car", "comment", "pourquoi",
    "quel", "quelle", "quels", "quelles", "peux", "peut", "etre", "avoir",
    "fait", "faire", "comme", "plus", "tres", "bien", "alors", "ainsi", "si",
    "on", "me", "te", "se", "d", "l", "a", "ete", "not", "the", "of", "and", "to",
    "soit", "soient", "on", "y", "s", "n", "c", "j", "qu",
}


def strip_accents(s):
    return "".join(
        ch for ch in unicodedata.normalize("NFD", s)
        if unicodedata.category(ch) != "Mn"
    )


LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+")


def tokenize(text):
    # \frac, \sum, \mathbb... (notes en LaTeX) : pas des mots du cours
    text = LATEX_CMD_RE.sub(" ", text)
    text = strip_accents(text.lower())
    words = re.findall(r"[a-z0-9]+", text)
    return [w for w in words if len(w) > 2 and w not in STOPWORDS]


# Abréviations d'étudiant et variantes de vocabulaire du cours. Ajoutées à
# la question (poids réduit) : "critère de d'Alembert" doit aussi trouver
# "règle d'Alembert", "cvu" doit trouver "convergence uniforme".
SYNONYMS = {
    "critere": ["regle"], "regle": ["critere"],
    "cvs": ["convergence", "simple"], "cvu": ["convergence", "uniforme"],
    "cvn": ["convergence", "normale"], "cva": ["convergence", "absolue"],
    "dse": ["developpement", "serie", "entiere"], "dls": ["developpement", "limite"],
    "sep": ["serie", "termes", "positifs"], "tcsa": ["alternee", "leibniz"],
    "dalembert": ["alembert"], "alembert": ["dalembert"],
}


def expand_query(tokens):
    """-> liste de (mot, poids) : mots de la question (1.0) + synonymes (0.5)."""
    out = [(w, 1.0) for w in tokens]
    for w in tokens:
        out += [(s, 0.5) for s in SYNONYMS.get(w, []) if s not in tokens]
    return out
