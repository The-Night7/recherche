# -*- coding: utf-8 -*-
"""
Recherche sémantique "from scratch" (TF-IDF + similarité cosinus,
tout codé à la main) dans le cours d'Analyse dans ℝⁿ.

Usage:
    python3 search.py "définition d'une norme"
    python3 search.py "extremums locaux" --k 5
"""
import argparse
import json

import numpy as np

from text_utils import tokenize


def load_index(index_path="index.npz", vocab_path="vocab.json", chunks_path="chunks.json"):
    data = np.load(index_path)
    tfidf = data["tfidf"]
    idf = data["idf"]
    vocab = json.load(open(vocab_path, encoding="utf-8"))
    chunks = json.load(open(chunks_path, encoding="utf-8"))
    return tfidf, idf, vocab, chunks


def query_vector(question, vocab, idf):
    toks = tokenize(question)
    v = np.zeros(len(vocab), dtype=np.float32)
    for w in toks:
        if w in vocab:
            v[vocab[w]] += 1.0
    v = v * idf
    n = np.linalg.norm(v)
    if n > 0:
        v = v / n
    return v, toks


def search(question, tfidf, idf, vocab, chunks, k=3):
    qvec, toks = query_vector(question, vocab, idf)
    if not toks:
        return [], toks
    # tfidf est déjà normalisé par ligne -> le produit scalaire = cosinus
    scores = tfidf @ qvec
    order = np.argsort(-scores)[:k]
    results = [(chunks[i], float(scores[i])) for i in order if scores[i] > 0]
    return results, toks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", type=str)
    ap.add_argument("--k", type=int, default=3)
    args = ap.parse_args()

    tfidf, idf, vocab, chunks = load_index()
    results, toks = search(args.question, tfidf, idf, vocab, chunks, k=args.k)

    if not toks:
        print("Question trop courte / aucun mot reconnu.")
        return
    if not results:
        print(f"Aucun passage pertinent trouvé pour : {toks}")
        return

    for rank, (chunk, score) in enumerate(results, 1):
        print(f"\n{'=' * 70}")
        print(f"#{rank}  [{chunk['label']}]  (score={score:.3f})")
        print('-' * 70)
        print(chunk["text"])


if __name__ == "__main__":
    main()
