"""
Vocabulaire au niveau caractère : construit la table char <-> id
à partir du corpus, et encode/décode du texte.
"""


class CharVocab:
    def __init__(self, text):
        chars = sorted(set(text))
        self.chars = chars
        self.stoi = {c: i for i, c in enumerate(chars)}
        self.itos = {i: c for i, c in enumerate(chars)}
        self.size = len(chars)

    def encode(self, text):
        return [self.stoi[c] for c in text if c in self.stoi]

    def decode(self, ids):
        return "".join(self.itos[i] for i in ids)


def load_corpus(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
