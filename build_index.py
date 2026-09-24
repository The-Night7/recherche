# -*- coding: utf-8 -*-
"""
Construit un index TF-IDF "from scratch" (juste NumPy, pas de
scikit-learn) à partir de chunks.json (tous les cours), et le sauvegarde dans
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
from collections import Counter
from pathlib import Path

import numpy as np

from text_utils import tokenize


def main(chunks_path="chunks.json", out_index="index.npz", out_vocab="vocab.json"):
    chunks = json.loads(Path(chunks_path).read_text(encoding="utf-8"))
    # le titre de section est indexé avec le texte : "Règle d'Alembert" est
    # souvent seulement dans le titre, pas dans le corps du passage
    docs_tokens = [tokenize(c.get("section", "") + " " + c["text"]) for c in chunks]

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
    rows, cols, values = [], [], []
    df = np.zeros(V, dtype=np.int64)
    for i, toks in enumerate(docs_tokens):
        for word, count in Counter(toks).items():
            col = vocab[word]
            rows.append(i)
            cols.append(col)
            values.append(count)
            df[col] += 1
    rows = np.asarray(rows, dtype=np.int32)
    cols = np.asarray(cols, dtype=np.int32)

    # --- DF puis IDF ---
    idf = np.log((1.0 + N) / (1.0 + df)) + 1.0        # lissage type sklearn

    # --- TF-IDF puis normalisation L2 ---
    tfidf = np.asarray(values, dtype=np.float64) * idf[cols]
    norms = np.sqrt(np.bincount(rows, weights=tfidf ** 2, minlength=N))
    norms[norms == 0] = 1.0
    tfidf_norm = tfidf / norms[rows]

    # stockage creux (lignes, colonnes, valeurs non nulles) : la matrice
    # dense N x V dépasserait vite les 40 Mo avec plusieurs cours
    np.savez_compressed(
        out_index,
        rows=rows.astype(np.int32), cols=cols.astype(np.int32),
        vals=tfidf_norm.astype(np.float32),
        shape=np.array([N, V], dtype=np.int64), idf=idf.astype(np.float32),
    )
    Path(out_vocab).write_text(json.dumps(vocab, ensure_ascii=False), encoding="utf-8")
    print(f"Index sauvegardé dans {out_index} et {out_vocab}")


if __name__ == "__main__":
    main()
