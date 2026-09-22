# -*- coding: utf-8 -*-
"""
Construit un index TF-IDF "from scratch" (juste NumPy, pas de
scikit-learn) à partir de data/chunks.json, et le sauvegarde dans
index.npz + vocab.json.

Rappel des maths (tout est codé ici à la main) :
  - TF(mot, doc)  = nombre d'occurrences du mot dans le document
  - IDF(mot)      = log((1 + N) / (1 + DF(mot))) + 1
                    (N = nb de documents, DF = nb de documents contenant le mot)
  - TF-IDF(mot, doc) = TF(mot, doc) * IDF(mot)
  - chaque vecteur document est ensuite normalisé (norme L2 = 1)
    pour que le produit scalaire entre deux vecteurs normalisés
    donne directement la similarité cosinus.

Usage:
    python3 build_index.py
"""
import json

import numpy as np

from text_utils import tokenize


def main(chunks_path="chunks.json", out_index="index.npz", out_vocab="vocab.json"):
    chunks = json.load(open(chunks_path, encoding="utf-8"))
    docs_tokens = [tokenize(c["text"]) for c in chunks]

    # --- vocabulaire ---
    vocab = {}
    for toks in docs_tokens:
        for w in toks:
            if w not in vocab:
                vocab[w] = len(vocab)
    V = len(vocab)
    N = len(chunks)
    print(f"{N} documents, vocabulaire de {V} mots")

    # --- TF (comptage brut par document) ---
    tf = np.zeros((N, V), dtype=np.float32)
    for i, toks in enumerate(docs_tokens):
        for w in toks:
            tf[i, vocab[w]] += 1.0

    # --- DF puis IDF ---
    df = (tf > 0).sum(axis=0)                        # (V,)
    idf = np.log((1.0 + N) / (1.0 + df)) + 1.0        # lissage type sklearn

    # --- TF-IDF puis normalisation L2 ---
    tfidf = tf * idf[np.newaxis, :]
    norms = np.linalg.norm(tfidf, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    tfidf_norm = tfidf / norms

    np.savez(out_index, tfidf=tfidf_norm.astype(np.float32), idf=idf.astype(np.float32))
    json.dump(vocab, open(out_vocab, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"Index sauvegardé dans {out_index} et {out_vocab}")


if __name__ == "__main__":
    main()
