"""
Charge le modèle entraîné et génère la suite d'un texte de départ.

Usage:
    python3 generate.py "Soit E un espace vectoriel"
    python3 generate.py "Soit E un espace vectoriel" --n 400 --temperature 0.6
"""
import argparse
import json

from vocab import CharVocab
from model import CharMLP


def load_vocab(path="vocab_char.json"):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    v = CharVocab("")  # vocabulaire vide, on le remplit à la main
    v.stoi = data["stoi"]
    v.itos = {int(k): c for k, c in data["itos"].items()}
    v.size = len(v.stoi)
    v.chars = [v.itos[i] for i in range(v.size)]
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", type=str)
    ap.add_argument("--n", type=int, default=300, help="nombre de caractères à générer")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--checkpoint", default="checkpoint.npz")
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()

    vocab = load_vocab()
    model = CharMLP.load(args.checkpoint)

    seed_ids = vocab.encode(args.prompt)
    if not seed_ids:
        print("Le prompt ne contient aucun caractère connu du vocabulaire du modèle.")
        return

    out_ids = model.generate(seed_ids, n_new=args.n, temperature=args.temperature, seed=args.seed)
    print(vocab.decode(out_ids))


if __name__ == "__main__":
    main()
