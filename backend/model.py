"""
Un petit réseau de neurones "from scratch" : aucun framework de deep
learning (pas de PyTorch/TensorFlow) — juste NumPy. Le forward pass,
le backward pass (calcul des gradients) et l'optimiseur Adam sont
codés à la main.

Architecture (inspirée de Bengio et al. 2003 / "makemore") :
  - on prend les `block_size` derniers caractères comme contexte
  - chaque caractère est transformé en vecteur par une table
    d'embeddings apprise C
  - les embeddings sont concaténés puis passés dans une couche
    cachée (tanh) puis une couche de sortie (softmax sur le
    vocabulaire) qui prédit le caractère suivant.
"""

import numpy as np


class CharMLP:
    def __init__(self, vocab_size, block_size=8, emb_dim=24, hidden=200, seed=1337):
        rng = np.random.default_rng(seed)
        self.vocab_size = vocab_size
        self.block_size = block_size
        self.emb_dim = emb_dim
        self.hidden = hidden

        # Initialisation (échelle ~ 1/sqrt(n) pour éviter saturation de tanh)
        self.C = rng.normal(0, 0.1, size=(vocab_size, emb_dim))
        fan_in1 = block_size * emb_dim
        self.W1 = rng.normal(0, 1 / np.sqrt(fan_in1), size=(fan_in1, hidden))
        self.b1 = np.zeros(hidden)
        self.W2 = rng.normal(0, 1 / np.sqrt(hidden), size=(hidden, vocab_size))
        self.b2 = np.zeros(vocab_size)

        self.params = {"C": self.C, "W1": self.W1, "b1": self.b1,
                        "W2": self.W2, "b2": self.b2}
        # états Adam (moment d'ordre 1 et 2) pour chaque paramètre
        self.m = {k: np.zeros_like(v) for k, v in self.params.items()}
        self.v = {k: np.zeros_like(v) for k, v in self.params.items()}
        self.t = 0

    # ---------- forward ----------
    def forward(self, X):
        """X: (B, block_size) indices -> logits (B, vocab_size), cache pour backward."""
        B = X.shape[0]
        emb = self.C[X]                          # (B, block_size, emb_dim)
        flat = emb.reshape(B, -1)                # (B, block_size*emb_dim)
        preh = flat @ self.W1 + self.b1          # (B, hidden)
        h = np.tanh(preh)                        # (B, hidden)
        logits = h @ self.W2 + self.b2           # (B, vocab_size)
        cache = (X, emb, flat, h)
        return logits, cache

    @staticmethod
    def softmax(logits):
        z = logits - logits.max(axis=1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=1, keepdims=True)

    def loss(self, logits, Y):
        probs = self.softmax(logits)
        B = logits.shape[0]
        correct = probs[np.arange(B), Y]
        nll = -np.log(np.clip(correct, 1e-12, None))
        return nll.mean(), probs

    # ---------- backward (calculé à la main) ----------
    def backward(self, cache, probs, Y):
        X, emb, flat, h = cache
        B = X.shape[0]

        dlogits = probs.copy()
        dlogits[np.arange(B), Y] -= 1
        dlogits /= B                              # (B, vocab)

        dW2 = h.T @ dlogits                       # (hidden, vocab)
        db2 = dlogits.sum(axis=0)                 # (vocab,)

        dh = dlogits @ self.W2.T                  # (B, hidden)
        dpreh = dh * (1 - h ** 2)                 # dérivée de tanh

        dW1 = flat.T @ dpreh                      # (block*emb, hidden)
        db1 = dpreh.sum(axis=0)                   # (hidden,)

        dflat = dpreh @ self.W1.T                 # (B, block*emb)
        demb = dflat.reshape(emb.shape)           # (B, block, emb)

        dC = np.zeros_like(self.C)
        # chaque caractère du contexte a contribué à un embedding : on
        # accumule le gradient sur la bonne ligne de la table C
        np.add.at(dC, X, demb)

        return {"C": dC, "W1": dW1, "b1": db1, "W2": dW2, "b2": db2}

    # ---------- optimiseur Adam, codé à la main ----------
    def step(self, grads, lr=3e-3, beta1=0.9, beta2=0.999, eps=1e-8, weight_decay=0.0):
        self.t += 1
        for k, p in self.params.items():
            g = grads[k]
            if weight_decay > 0:
                g = g + weight_decay * p          # régularisation L2 (pénalise les grands poids)
            self.m[k] = beta1 * self.m[k] + (1 - beta1) * g
            self.v[k] = beta2 * self.v[k] + (1 - beta2) * (g ** 2)
            mhat = self.m[k] / (1 - beta1 ** self.t)
            vhat = self.v[k] / (1 - beta2 ** self.t)
            p -= lr * mhat / (np.sqrt(vhat) + eps)

    # ---------- génération ----------
    def generate(self, context_ids, n_new, temperature=0.8, seed=None):
        rng = np.random.default_rng(seed)
        ids = list(context_ids)
        for _ in range(n_new):
            ctx = ids[-self.block_size:]
            if len(ctx) < self.block_size:
                ctx = [0] * (self.block_size - len(ctx)) + ctx
            X = np.array([ctx])
            logits, _ = self.forward(X)
            probs = self.softmax(logits / temperature)[0]
            next_id = rng.choice(self.vocab_size, p=probs)
            ids.append(int(next_id))
        return ids

    def save(self, path):
        np.savez(path, C=self.C, W1=self.W1, b1=self.b1, W2=self.W2, b2=self.b2,
                 block_size=self.block_size)

    @classmethod
    def load(cls, path):
        data = np.load(path)
        vocab_size, emb_dim = data["C"].shape
        hidden = data["W1"].shape[1]
        block_size = int(data["block_size"])
        m = cls(vocab_size, block_size=block_size, emb_dim=emb_dim, hidden=hidden)
        m.C[:] = data["C"]
        m.W1[:] = data["W1"]
        m.b1[:] = data["b1"]
        m.W2[:] = data["W2"]
        m.b2[:] = data["b2"]
        return m
