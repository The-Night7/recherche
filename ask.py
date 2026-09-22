# -*- coding: utf-8 -*-
"""
Mode interactif : charge l'index TF-IDF une fois, puis tu tapes
autant de questions que tu veux (Ctrl+D ou "exit" pour sortir).

Usage:
    python3 ask.py
"""
from search import load_index, search


def main():
    print("Chargement de l'index...")
    tfidf, idf, vocab, chunks = load_index()
    print(f"{len(chunks)} passages indexés, vocabulaire de {len(vocab)} mots.")
    print("Tape ta question (ou 'exit' pour quitter).\n")

    while True:
        try:
            q = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not q:
            continue
        if q.lower() in ("exit", "quit"):
            break

        results, toks = search(q, tfidf, idf, vocab, chunks, k=3)
        if not toks:
            print("(question trop courte)")
            continue
        if not results:
            print(f"Aucun passage pertinent trouvé pour: {toks}\n")
            continue

        for rank, (chunk, score) in enumerate(results, 1):
            print(f"\n--- #{rank} [{chunk['label']}] (score={score:.3f}) ---")
            print(chunk["text"])
        print()


if __name__ == "__main__":
    main()
