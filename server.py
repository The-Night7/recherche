# -*- coding: utf-8 -*-
"""
Petit serveur web local pour interroger l'index TF-IDF avec une
interface propre, sans dépendance externe (juste la bibliothèque
standard de Python + numpy pour la recherche). La page est dans
web/ (index.html, style.css, app.js, theme.js) ; elle permet de choisir où chercher (cours, type de
document, énoncés/corrigés, années).

Usage:
    python3 server.py
    -> ouvre http://localhost:8000 dans le navigateur
"""
import html
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from reflow import to_md_blocks
from courses import COURSES, CURRICULUM, KINDS
from search import filter_mask, load_index, recency, search

# en local: http://localhost:8000 . En ligne (Render, Railway, etc.),
# la plateforme fixe le port et l'hôte via la variable d'env PORT.
PORT = int(os.environ.get("PORT", 8000))
HOST = os.environ.get("HOST", "0.0.0.0")

print("Chargement de l'index...")
TFIDF, IDF, VOCAB, CHUNKS = load_index()
RECENCY = recency(CHUNKS)
print(f"{len(CHUNKS)} passages indexés, vocabulaire de {len(VOCAB)} mots.")


def build_meta():
    courses = []
    for cid, name in COURSES.items():
        cs = [c for c in CHUNKS if c["course"] == cid]
        if not cs:
            continue
        kinds = {}
        for c in cs:
            kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
        years = sorted({c["year"] for c in cs}, key=lambda y: -1 if y is None else y)
        courses.append({"id": cid, "name": name, "curriculum": CURRICULUM["id"], "count": len(cs), "kinds": kinds, "years": years})
    return {"courses": courses, "kinds": KINDS, "curriculum": CURRICULUM}


META = build_meta()


def md_blocks(text):
    # un seul bloc : le rendu Markdown côté page gère paragraphes, listes et $…$
    return [{"type": "md", "text": text}]


def content_blocks(chunk):
    if chunk.get("fmt") == "md":
        return md_blocks(chunk["text"])
    if chunk.get("fmt") == "text":
        return [{"type": "text", "text": chunk["text"]}]
    return to_md_blocks(chunk["text"])


def csv_param(qs, name):
    raw = qs.get(name, [""])[0]
    return {x for x in raw.split(",") if x} or None


WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")
STATIC_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".ico": "image/x-icon",
}


def static_file(url_path):
    """Chemin du fichier de web/ demandé, ou None (inexistant / hors de web/ / type inconnu)."""
    rel = "index.html" if url_path == "/" else url_path.lstrip("/")
    full = os.path.realpath(os.path.join(WEB_DIR, rel))
    if not full.startswith(os.path.realpath(WEB_DIR) + os.sep):
        return None
    if os.path.splitext(full)[1] not in STATIC_TYPES or not os.path.isfile(full):
        return None
    return full


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence les logs par défaut, un peu bruyants

    def send(self, body, ctype):
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, payload):
        self.send(json.dumps(payload, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self):
        parsed = urlparse(self.path)

        if not parsed.path.startswith("/api/"):
            # relus à chaque requête : on peut modifier web/ sans relancer
            path = static_file(parsed.path)
            if path:
                with open(path, "rb") as f:
                    self.send(f.read(), STATIC_TYPES[os.path.splitext(path)[1]])
                return

        if parsed.path == "/api/meta":
            self.send_json(META)
            return

        if parsed.path == "/api/search":
            qs = parse_qs(parsed.query)
            question = qs.get("q", [""])[0]
            years = csv_param(qs, "years")
            mask = filter_mask(
                CHUNKS,
                courses=csv_param(qs, "course"),
                kinds=csv_param(qs, "kinds"),
                versions=csv_param(qs, "versions"),
                years={int(y) if y.isdigit() else y for y in years} if years else None,
            )
            try:
                k = max(1, min(20, int(qs.get("k", ["5"])[0])))
            except ValueError:
                k = 5
            use_recent = qs.get("recent", ["1"])[0] != "0"
            results, tokens, info = search(
                question, TFIDF, IDF, VOCAB, CHUNKS, k=k, mask=mask,
                recent=RECENCY if use_recent else None, with_info=True,
            )
            self.send_json({
                "tokens": tokens,
                "reference": info["reference"], "relaxed": info["relaxed"],
                "highlight": info["highlight"] + [t for t in tokens if t != info["reference"]],
                "searched": int(mask.sum()),
                "results": [
                    {
                        "label": c["label"], "section": c.get("section", ""),
                        "doc_label": c.get("doc_label", ""), "course": c["course"],
                        "course_name": COURSES.get(c["course"], c["course"]),
                        "curriculum": c["curriculum"],
                        "kind": c["kind"], "corrige": c["corrige"], "year": c["year"],
                        "score": score,
                        "blocks": content_blocks(c),
                    }
                    for c, score in results
                ],
            })
            return

        self.send_response(404)
        self.end_headers()


def main():
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"\nServeur lancé sur {HOST}:{PORT}")
    print(f"En local: http://localhost:{PORT}")
    print("Ctrl+C pour arrêter le serveur.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.")


if __name__ == "__main__":
    main()
