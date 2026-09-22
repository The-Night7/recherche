"""
Mode interactif : charge le modèle une seule fois, puis tu tapes
autant de débuts de phrase que tu veux (Ctrl+D ou "exit" pour sortir).

Usage:
    python3 chat.py
    python3 chat.py --temperature 0.5 --n 250
"""
import argparse

from generate import load_vocab
from model import CharMLP


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=300, help="caractères générés par réponse")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--checkpoint", default="checkpoint.npz")
    args = ap.parse_args()

    print("Chargement du modèle...")
    vocab = load_vocab()
    model = CharMLP.load(args.checkpoint)
    print(f"Modèle chargé ({model.vocab_size} caractères, contexte {model.block_size}).")
    print("Tape un début de phrase (ou 'exit' pour quitter, 'temp=0.5' pour changer la température).\n")

    temperature = args.temperature
    while True:
        try:
            prompt = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not prompt:
            continue
        if prompt.lower() in ("exit", "quit"):
            break
        if prompt.startswith("temp="):
            try:
                temperature = float(prompt.split("=", 1)[1])
                print(f"(température réglée à {temperature})")
            except ValueError:
                print("Format attendu: temp=0.6")
            continue

        seed_ids = vocab.encode(prompt)
        if not seed_ids:
            print("(aucun caractère connu du modèle dans ce prompt)")
            continue

        out_ids = model.generate(seed_ids, n_new=args.n, temperature=temperature)
        print(vocab.decode(out_ids))
        print()


if __name__ == "__main__":
    main()
