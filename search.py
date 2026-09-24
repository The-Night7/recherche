# -*- coding: utf-8 -*-
"""
Recherche sémantique "from scratch" (TF-IDF + similarité cosinus,
tout codé à la main) dans les cours indexés (Analyse dans ℝⁿ, Séries).

Filtres : cours, type de document (cours/td/ds/qcm), énoncés/corrigés,
années. Les documents récents sont favorisés : le score cosinus est
multiplié par (1 + RECENT_BOOST × r), où r ∈ [0, 1] place l'année du
document entre la plus ancienne (0) et la plus récente (1) de son cours
(0.5 si l'année est inconnue).

Usage:
    python3 search.py "définition d'une norme"
    python3 search.py "critère de d'Alembert" --cours series --type td,ds --k 5
    python3 search.py "rayon de convergence" --cours series --annees 2024,2023
"""
import argparse
import json
from pathlib import Path

import numpy as np

from courses import COURSES, course_context, ensure_meta
from references import annotate, describe, highlight_terms, match, parse_reference
from text_utils import expand_query, tokenize

RECENT_BOOST = 0.25


class SparseIndex:
    """Produit matrice-vecteur NumPy sans matérialiser tous les zéros du corpus."""
    def __init__(self, rows, cols, vals, shape):
        self.rows, self.cols, self.vals = rows, cols, vals
        self.shape = tuple(int(n) for n in shape)

    def __matmul__(self, vector):
        return np.bincount(self.rows, weights=self.vals * vector[self.cols],
                           minlength=self.shape[0]).astype(np.float32)


def load_index(index_path="index.npz", vocab_path="vocab.json", chunks_path="chunks.json"):
    with np.load(index_path) as data:
        idf = data["idf"]
        if "tfidf" in data:  # ancien format (matrice dense)
            tfidf = data["tfidf"]
        else:
            tfidf = SparseIndex(data["rows"], data["cols"], data["vals"], data["shape"])
    vocab = json.loads(Path(vocab_path).read_text(encoding="utf-8"))
    chunks = annotate([ensure_meta(c) for c in json.loads(Path(chunks_path).read_text(encoding="utf-8"))])
    return tfidf, idf, vocab, chunks


def recency(chunks):
    """r ∈ [0, 1] par passage, calculé cours par cours."""
    r = np.full(len(chunks), 0.5, dtype=np.float32)
    for course in {c["course"] for c in chunks}:
        years = [c["year"] for c in chunks if c["course"] == course and c["year"]]
        if not years:
            continue
        lo, hi = min(years), max(years)
        for i, c in enumerate(chunks):
            if c["course"] == course and c["year"]:
                r[i] = 1.0 if hi == lo else (c["year"] - lo) / (hi - lo)
    return r


def query_vector(question, vocab, idf):
    toks = tokenize(question)
    v = np.zeros(len(vocab), dtype=np.float32)
    for w, weight in expand_query(toks):
        if w in vocab:
            v[vocab[w]] += weight
    v = v * idf
    n = np.linalg.norm(v)
    if n > 0:
        v = v / n
    return v, toks


def filter_mask(chunks, courses=None, kinds=None, versions=None, years=None,
                study_years=None, semesters=None):
    """courses/kinds : ensembles d'identifiants ; versions ⊂ {"enonce", "corrige"} ;
    years ⊂ années (int) ou "none" pour les documents sans année. None = pas de filtre."""
    mask = np.ones(len(chunks), dtype=bool)
    for i, c in enumerate(chunks):
        if courses and c["course"] not in courses:
            mask[i] = False
        elif kinds and c["kind"] not in kinds:
            mask[i] = False
        elif versions and ("corrige" if c["corrige"] else "enonce") not in versions:
            mask[i] = False
        elif years and (c["year"] if c["year"] else "none") not in years:
            mask[i] = False
        elif study_years and c["study_year"] not in study_years:
            mask[i] = False
        elif semesters and c["semester"] not in semesters:
            mask[i] = False
    return mask


def search(question, tfidf, idf, vocab, chunks, k=3, mask=None, recent=None, boost=RECENT_BOOST,
           with_info=False):
    """Recherche TF-IDF, précédée d'une lecture des références structurées
    ("td 1 exercice 2") qui deviennent un filtre exact.
    -> (résultats, tokens) ou, avec with_info=True, (résultats, tokens, info)
    info = {"reference": str|None, "relaxed": bool, "highlight": [...]}"""
    info = {"reference": None, "relaxed": False, "highlight": []}
    ref, rest = parse_reference(question)
    base = mask if mask is not None else np.ones(len(chunks), dtype=bool)

    if ref:
        info["reference"] = describe(ref)
        info["highlight"] = highlight_terms(ref)
        ref_mask = np.array([match(c, ref) for c in chunks]) & base
        if not ref_mask.any() and ref["kind"] and ref["exercises"]:
            # exercice introuvable dans ce document : on montre le document entier
            ref_mask = np.array([match(c, ref, use_exercises=False) for c in chunks]) & base
            info["relaxed"] = True
        if not ref_mask.any():
            ref = None  # rien ne correspond : recherche plein texte classique
            rest = question
        else:
            base = ref_mask

    qvec, toks = query_vector(rest, vocab, idf)
    rec = recent if recent is not None else np.zeros(len(chunks), dtype=np.float32)
    shown = [info["reference"]] if ref else []

    if ref:
        # les passages qui correspondent à la référence passent tous ;
        # les mots restants ("convergence", "d'Alembert"...) les départagent
        cos = tfidf @ qvec if toks else np.zeros(len(chunks), dtype=np.float32)
        cos = np.clip(cos, 0, None)
        scores = (1.0 + cos) * (1.0 + boost * rec)
        scores[~base] = -1.0
        # à score égal : énoncé avant corrigé, puis ordre du document
        tie = np.array([1 if c["corrige"] else 0 for c in chunks])
        order = np.lexsort((np.arange(len(chunks)), tie, -np.round(scores, 6)))
        order = [i for i in order if base[i]][:k]
        results = [(chunks[i], float(scores[i])) for i in order]
    else:
        if not toks:
            return ([], toks, info) if with_info else ([], toks)
        # tfidf est déjà normalisé par ligne -> le produit scalaire = cosinus
        cos = tfidf @ qvec
        scores = cos * (1.0 + boost * rec)
        scores[cos <= 0] = 0.0
        scores[~base] = 0.0
        order = np.argsort(-scores)[:k]
        results = [(chunks[i], float(scores[i])) for i in order if scores[i] > 0]

    toks = shown + toks
    return (results, toks, info) if with_info else (results, toks)


def parse_list(s):
    return {x.strip() for x in s.split(",") if x.strip()} if s else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", type=str)
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--cours", help=f"parmi {', '.join(COURSES)} (séparés par des virgules)")
    ap.add_argument("--type", help="parmi cours, td, tp, ds, cc, qcm, projet")
    ap.add_argument("--preing", help="année de Préing : 1,2")
    ap.add_argument("--semestre", help="semestre : 1,2")
    ap.add_argument("--version", help="enonce, corrige")
    ap.add_argument("--annees", help="ex: 2024,2023 (année de début)")
    ap.add_argument("--sans-recence", action="store_true", help="ne pas favoriser les documents récents")
    args = ap.parse_args()

    tfidf, idf, vocab, chunks = load_index()
    years = parse_list(args.annees)
    mask = filter_mask(
        chunks, parse_list(args.cours), parse_list(args.type), parse_list(args.version),
        {int(y) if y.isdigit() else y for y in years} if years else None,
        study_years={int(y) for y in parse_list(args.preing)} if args.preing else None,
        semesters={int(s) for s in parse_list(args.semestre)} if args.semestre else None,
    )
    rec = None if args.sans_recence else recency(chunks)
    results, toks, info = search(args.question, tfidf, idf, vocab, chunks, k=args.k, mask=mask,
                                 recent=rec, with_info=True)
    if info["reference"]:
        print(f"Référence détectée : {info['reference']}"
              + (" (exercice introuvable, document entier)" if info["relaxed"] else ""))

    if not toks:
        print("Question trop courte / aucun mot reconnu.")
        return
    if not results:
        print(f"Aucun passage pertinent trouvé pour : {toks}")
        return

    for rank, (chunk, score) in enumerate(results, 1):
        print(f"\n{'=' * 70}")
        print(f"#{rank}  [{course_context(chunk['course'])['label']} · {COURSES[chunk['course']]}] {chunk['label']}  (score={score:.3f})")
        print('-' * 70)
        print(chunk["text"])


if __name__ == "__main__":
    main()
