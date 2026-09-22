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


def tokenize(text):
    text = strip_accents(text.lower())
    words = re.findall(r"[a-z0-9]+", text)
    return [w for w in words if len(w) > 2 and w not in STOPWORDS]
