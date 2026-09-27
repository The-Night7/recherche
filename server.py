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
import hashlib
import html
import json
import os
import re
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from reflow import to_md_blocks
from document_sources import find_source
from pdf_crops import with_crops
from courses import COURSES, CURRICULA, PROGRAMS, KINDS, course_context
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
        context = course_context(cid)
        courses.append({"id": cid, "name": name, "curriculum": context["id"],
                        "program": context["program"], "track": context["track"],
                        "study_year": context["study_year"], "semester": context["semester"],
                        "curriculum_label": context["label"],
                        "count": len(cs), "kinds": kinds, "years": years})
    contexts = [dict(ctx, count=sum(c['count'] for c in courses if c['curriculum'] == ctx['id']))
                for ctx in CURRICULA.values()]
    return {"courses": courses, "kinds": KINDS, "curricula": contexts, "programs": PROGRAMS}


META = build_meta()

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE_CACHE = os.path.join(ROOT, ".pagecache")
# PDF d'origine, seulement pour les documents indexés dont le fichier est présent sur cette machine
SOURCES = {}
for _chunk in CHUNKS:
    if _chunk.get("pages") and _chunk.get("doc") and _chunk.get("source") and _chunk["doc"] not in SOURCES:
        _path = find_source(_chunk["source"], ROOT)
        if _path:
            SOURCES[_chunk["doc"]] = _path


def render_page(doc, number):
    """JPEG de la page `number` (à partir de 1) du PDF de `doc`, mis en cache ; None si impossible."""
    if doc not in SOURCES or not 1 <= number <= 5000:
        return None
    out = os.path.join(PAGE_CACHE, f"{hashlib.sha1(doc.encode()).hexdigest()[:16]}-{number}.jpg")
    if not os.path.isfile(out):
        os.makedirs(PAGE_CACHE, exist_ok=True)
        base = f"{out[:-4]}.{os.getpid()}"
        try:
            subprocess.run(["pdftoppm", "-jpeg", "-jpegopt", "quality=85", "-r", "110", "-f", str(number),
                            "-l", str(number), "-singlefile", SOURCES[doc], base],
                           check=True, capture_output=True, timeout=60)
            os.replace(base + ".jpg", out)
        except (subprocess.SubprocessError, OSError):
            return None
    with open(out, "rb") as f:
        return f.read()


CROP_DPI = 200


def render_crop(doc, number, box):
    """PNG d'une zone (en points PDF : x0, y0, x1, y1) de la page `number`, mis en cache ; None si impossible."""
    if doc not in SOURCES or not 1 <= number <= 5000:
        return None
    try:
        x0, y0, x1, y1 = (float(v) for v in box.split(","))
    except ValueError:
        return None
    if not (0 <= x0 < x1 <= 2000 and 0 <= y0 < y1 <= 3000):
        return None
    scale = CROP_DPI / 72
    key = hashlib.sha1(f"{doc}|{number}|{box}".encode()).hexdigest()[:20]
    out = os.path.join(PAGE_CACHE, f"crop-{key}.png")
    if not os.path.isfile(out):
        os.makedirs(PAGE_CACHE, exist_ok=True)
        base = f"{out[:-4]}.{os.getpid()}"
        try:
            subprocess.run(["pdftoppm", "-png", "-r", str(CROP_DPI), "-f", str(number), "-l", str(number),
                            "-x", str(int(x0 * scale)), "-y", str(int(y0 * scale)),
                            "-W", str(int((x1 - x0) * scale) + 1), "-H", str(int((y1 - y0) * scale) + 1),
                            "-singlefile", SOURCES[doc], base],
                           check=True, capture_output=True, timeout=60)
            os.replace(base + ".png", out)
        except (subprocess.SubprocessError, OSError):
            return None
    with open(out, "rb") as f:
        return f.read()


def clean_md(text):
    """Retire ce qui n'est pas du contenu : balises Jekyll, iframes, ancres, enveloppes <p>."""
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.S)
    text = re.sub(r"<iframe\b.*?</iframe>", "", text, flags=re.S | re.I)
    text = re.sub(r"<div\s+id=\"[^\"]*\"\s*></div>", "", text, flags=re.I)
    text = re.sub(r"<a\s+[^>]*href=\"(https?://[^\"]+)\"[^>]*>(.*?)</a>", r"[\2](\1)", text, flags=re.S | re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</?p>", "", text, flags=re.I)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def md_blocks(text):
    # un seul bloc : le rendu Markdown côté page gère paragraphes, listes et $…$
    return [{"type": "md", "text": clean_md(text)}]


def is_ing_pdf(chunk):
    return chunk.get("fmt") == "pdf" and chunk.get("program") == "ing"


def cropped(chunk, blocks):
    """Formules non reconstruites : image découpée dans la page du PDF, quand il est là."""
    if chunk.get("doc") not in SOURCES or not chunk.get("pages"):
        return blocks
    return [{**b, "text": with_crops(b["text"], chunk["doc"], SOURCES[chunk["doc"]], chunk["pages"])}
            if b.get("type") == "md" and "```pdf" in b["text"] else b for b in blocks]


def alt_blocks(chunk):
    """Version reformatée (formules reconstruites), proposée à la demande."""
    return cropped(chunk, to_md_blocks(chunk["text"])) if is_ing_pdf(chunk) else None


def content_blocks(chunk):
    if chunk.get("fmt") == "md":
        return md_blocks(chunk["text"])
    # PDF Ing : texte fidèle par défaut, la mise en forme des formules est devinée (voir alt_blocks).
    if is_ing_pdf(chunk):
        return [{"type": "slides", "text": chunk["text"]}]
    if chunk.get("fmt") == "text":
        return [{"type": "text", "text": chunk["text"]}]
    if chunk.get("fmt") == "code":
        return [{"type": "code", "text": chunk["text"]}]
    return cropped(chunk, to_md_blocks(chunk["text"]))


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

    def send(self, body, ctype, cache=None):
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        if cache:
            self.send_header("Cache-Control", cache)
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

        if parsed.path == "/api/page":
            qs = parse_qs(parsed.query)
            number = qs.get("n", [""])[0]
            image = render_page(qs.get("doc", [""])[0], int(number)) if number.isdigit() else None
            if image is None:
                self.send_response(404)
                self.end_headers()
            else:
                self.send(image, "image/jpeg", cache="public, max-age=86400")
            return

        if parsed.path == "/api/crop":
            qs = parse_qs(parsed.query)
            number = qs.get("n", [""])[0]
            image = render_crop(qs.get("doc", [""])[0], int(number), qs.get("box", [""])[0]) if number.isdigit() else None
            if image is None:
                self.send_response(404)
                self.end_headers()
            else:
                self.send(image, "image/png", cache="public, max-age=86400")
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
                study_years={int(y) if y.isdigit() else y for y in csv_param(qs, "study_year") or []} or None,
                semesters={int(s) if s.isdigit() else s for s in csv_param(qs, "semester") or []} or None,
                programs=csv_param(qs, "program"),
                tracks=csv_param(qs, "track"),
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
                        "current": c.get("current"),
                        "course_name": COURSES.get(c["course"], c["course"]),
                        "curriculum": c["curriculum"],
                        "curriculum_label": course_context(c["course"])["label"],
                        "study_year": c["study_year"], "semester": c["semester"],
                        "program": c["program"], "track": c["track"],
                        "kind": c["kind"], "corrige": c["corrige"], "year": c["year"],
                        "with_correction": bool(c.get("with_correction")),
                        "score": score,
                        "blocks": content_blocks(c), "alt": alt_blocks(c),
                        "pdf": {"doc": c["doc"], "pages": c["pages"]} if c.get("doc") in SOURCES and c.get("pages") else None,
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
