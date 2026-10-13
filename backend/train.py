"""
Entraîne le petit réseau de neurones (model.CharMLP) sur le corpus
du cours d'Analyse dans ℝⁿ (data/corpus.txt).

Usage:
    python3 train.py [--steps 20000] [--batch 128]
"""
import argparse
import time

import numpy as np

from vocab import CharVocab, load_corpus
from model import CharMLP


def build_dataset(ids, block_size):
    """Construit toutes les paires (contexte de block_size caractères -> caractère suivant)."""
    X, Y = [], []
    for i in range(len(ids) - block_size):
        X.append(ids[i:i + block_size])
        Y.append(ids[i + block_size])
    return np.array(X), np.array(Y)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default="data/corpus.txt")
    ap.add_argument("--block_size", type=int, default=8)
    ap.add_argument("--emb_dim", type=int, default=24)
    ap.add_argument("--hidden", type=int, default=200)
    ap.add_argument("--steps", type=int, default=20000)
    ap.add_argument("--batch", type=int, default=128)
    ap.add_argument("--lr", type=float, default=3e-3)
    ap.add_argument("--weight_decay", type=float, default=0.0)
    ap.add_argument("--out", default="checkpoint.npz")
    args = ap.parse_args()

    text = load_corpus(args.corpus)
    vocab = CharVocab(text)
    print(f"Corpus: {len(text)} caractères, vocabulaire: {vocab.size} caractères distincts")

    ids = vocab.encode(text)
    X, Y = build_dataset(ids, args.block_size)
    n = len(X)
    n_val = max(1000, n // 20)
    perm = np.random.default_rng(0).permutation(n)
    val_idx, train_idx = perm[:n_val], perm[n_val:]
    Xtr, Ytr = X[train_idx], Y[train_idx]
    Xval, Yval = X[val_idx], Y[val_idx]
    print(f"Exemples d'entraînement: {len(Xtr)}, validation: {len(Xval)}")

    model = CharMLP(vocab.size, block_size=args.block_size,
                     emb_dim=args.emb_dim, hidden=args.hidden)

    rng = np.random.default_rng(42)
    t0 = time.time()
    best_val = float("inf")
    best_step = 0
    for step in range(1, args.steps + 1):
        batch_idx = rng.integers(0, len(Xtr), size=args.batch)
        Xb, Yb = Xtr[batch_idx], Ytr[batch_idx]

        logits, cache = model.forward(Xb)
        loss, probs = model.loss(logits, Yb)
        grads = model.backward(cache, probs, Yb)
        model.step(grads, lr=args.lr, weight_decay=args.weight_decay)

        if step % 500 == 0 or step == 1:
            val_logits, _ = model.forward(Xval[:2000])
            val_loss, _ = model.loss(val_logits, Yval[:2000])
            dt = time.time() - t0
            flag = ""
            if val_loss < best_val:
                best_val = val_loss
                best_step = step
                model.save(args.out)  # on ne garde que le meilleur checkpoint (early stopping)
                flag = "  <- meilleur, sauvegardé"
            print(f"step {step:6d} | train loss {loss:.3f} | val loss {val_loss:.3f} | {dt:.1f}s{flag}")

    print(f"\nMeilleur modèle: step {best_step} (val loss {best_val:.3f}), sauvegardé dans {args.out}")
    # on recharge le meilleur checkpoint pour la démo de génération ci-dessous
    model = CharMLP.load(args.out)

    # petite démo de génération
    import json
    with open("vocab_char.json", "w", encoding="utf-8") as f:
        json.dump({"stoi": vocab.stoi, "itos": {str(k): v for k, v in vocab.itos.items()}},
                   f, ensure_ascii=False)

    seed_text = "Soit E un espace vectoriel"
    seed_ids = vocab.encode(seed_text)
    out_ids = model.generate(seed_ids, n_new=300, temperature=0.7, seed=0)
    print("\n--- Génération (température 0.7) ---")
    print(vocab.decode(out_ids))


if __name__ == "__main__":
    main()
