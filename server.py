# -*- coding: utf-8 -*-
"""
Petit serveur web local pour interroger l'index TF-IDF avec une
interface propre, sans dépendance externe (juste la bibliothèque
standard de Python + numpy pour la recherche).

Usage:
    python3 server.py
    -> ouvre http://localhost:8000 dans le navigateur
"""
import html
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from search import load_index, search
from clean_extraction import to_blocks

PORT = 8000

print("Chargement de l'index...")
TFIDF, IDF, VOCAB, CHUNKS = load_index()
print(f"{len(CHUNKS)} passages indexés, vocabulaire de {len(VOCAB)} mots.")

PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tuteur "from scratch" — Analyse dans ℝⁿ</title>
<style>
  :root{
    --bg:#161821; --panel:#1e2130; --panel2:#242840; --ink:#eef0f8;
    --ink-soft:#9a9fc0; --accent:#8b9bff; --accent2:#c79bff;
    --border:#31354d; --score:#5fd0a0;
  }
  *{box-sizing:border-box;}
  body{
    margin:0; background:var(--bg); color:var(--ink);
    font-family:'Segoe UI', system-ui, sans-serif;
    min-height:100vh;
  }
  ::selection{ background:#4a4420; color:#ffe08a; }
  header{
    padding:22px 24px 16px; text-align:center;
    border-bottom:1px solid var(--border);
  }
  header h1{ margin:0 0 4px; font-size:20px; font-weight:600; }
  header p{ margin:0; color:var(--ink-soft); font-size:13px; }
  #searchbar{
    max-width:720px; margin:20px auto 0; padding:0 20px;
    display:flex; gap:10px;
  }
  #q{
    flex:1; padding:12px 16px; border-radius:10px; border:1px solid var(--border);
    background:var(--panel); color:var(--ink); font-size:15px;
  }
  #q:focus{ outline:none; border-color:var(--accent); }
  #go{
    padding:12px 20px; border-radius:10px; border:none; cursor:pointer;
    background:linear-gradient(135deg, var(--accent), var(--accent2));
    color:#12131c; font-weight:600; font-size:14px;
  }
  #go:hover{ opacity:0.9; }
  #results{ max-width:720px; margin:26px auto 60px; padding:0 20px; }
  .card{
    background:var(--panel); border:1px solid var(--border); border-radius:14px;
    padding:20px 22px; margin-bottom:18px;
  }
  .card-head{
    display:flex; justify-content:space-between; align-items:baseline;
    margin-bottom:14px; gap:10px; padding-bottom:10px;
    border-bottom:1px solid var(--border);
  }
  .card-head .label{ font-weight:600; font-size:13.5px; color:var(--accent2); }
  .card-head .score{ font-size:11px; color:var(--score); white-space:nowrap;
    background:#1a2b24; padding:3px 8px; border-radius:999px; }
  .rank{ color:var(--ink-soft); font-size:12px; margin-right:6px; }

  /* paragraphes de prose : police lisible, texte qui coule normalement */
  .prose{
    margin:0 0 14px; font-family:'Georgia','Liberation Serif', serif;
    font-size:15.5px; line-height:1.75; color:var(--ink);
  }
  .prose:last-child{ margin-bottom:0; }

  /* formules / listes : bloc distinct, police mono, fond légèrement différent */
  .formula{
    margin:10px 0; padding:10px 14px; background:var(--panel2);
    border-left:3px solid var(--accent); border-radius:6px;
    overflow-x:auto;
  }
  .formula pre{
    margin:0; white-space:pre-wrap; word-break:break-word;
    font-family:'Cascadia Code','Fira Code', ui-monospace, monospace;
    font-size:13.5px; line-height:1.6; color:#d6d9ff;
  }

  mark{ background:#4a4420; color:#ffe08a; border-radius:3px; padding:0 2px; }
  .empty, .hint{ text-align:center; color:var(--ink-soft); font-size:13.5px; margin-top:40px; }
  .count{ color:var(--ink-soft); font-size:12.5px; margin:0 0 14px; text-align:center; }
</style>
</head>
<body>
<header>
  <h1>∫ Tuteur "from scratch" — Analyse dans ℝⁿ</h1>
  <p>Recherche TF-IDF codée à la main (NumPy) · 100% local, aucune IA générative</p>
</header>
<div id="searchbar">
  <input id="q" type="text" placeholder="Ex: définition d'une norme, matrice jacobienne..." autofocus>
  <button id="go">Rechercher</button>
</div>
<div id="results"><p class="hint">Tape une question sur le cours, puis Entrée.</p></div>

<script>
const qEl = document.getElementById('q');
const goEl = document.getElementById('go');
const resultsEl = document.getElementById('results');

function escapeHtml(s){
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function highlight(text, terms){
  let escaped = escapeHtml(text);
  terms.forEach(t => {
    if(t.length < 3) return;
    // surligne le mot entier (racine + terminaison), pas juste le radical de la recherche
    const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + '\\\\w*)', 'gi');
    escaped = escaped.replace(re, '<mark>$1</mark>');
  });
  return escaped;
}

async function doSearch(){
  const q = qEl.value.trim();
  if(!q) return;
  resultsEl.innerHTML = '<p class="hint">Recherche…</p>';
  try{
    const res = await fetch('/api/search?q=' + encodeURIComponent(q));
    const data = await res.json();
    if(data.error){
      resultsEl.innerHTML = '<p class="empty">' + escapeHtml(data.error) + '</p>';
      return;
    }
    if(!data.results.length){
      resultsEl.innerHTML = '<p class="empty">Aucun passage pertinent trouvé pour : ' + data.tokens.map(escapeHtml).join(', ') + '</p>';
      return;
    }
    const count = `<p class="count">${data.results.length} passage(s) trouvé(s)</p>`;
    resultsEl.innerHTML = count + data.results.map((r, i) => {
      const blocksHtml = r.blocks.map(b => {
        if(b.type === 'formula'){
          return `<div class="formula"><pre>${escapeHtml(b.text)}</pre></div>`;
        }
        return `<p class="prose">${highlight(b.text, data.tokens)}</p>`;
      }).join('');
      return `
        <div class="card">
          <div class="card-head">
            <span><span class="rank">#${i+1}</span><span class="label">${escapeHtml(r.label)}</span></span>
            <span class="score">score ${r.score.toFixed(3)}</span>
          </div>
          ${blocksHtml}
        </div>
      `;
    }).join('');
  }catch(e){
    resultsEl.innerHTML = '<p class="empty">Erreur de connexion au serveur.</p>';
  }
}

goEl.addEventListener('click', doSearch);
qEl.addEventListener('keydown', e => { if(e.key === 'Enter') doSearch(); });
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence les logs par défaut, un peu bruyants

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/":
            body = PAGE.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if parsed.path == "/api/search":
            qs = parse_qs(parsed.query)
            question = qs.get("q", [""])[0]
            results, tokens = search(question, TFIDF, IDF, VOCAB, CHUNKS, k=3)
            payload = {
                "tokens": tokens,
                "results": [
                    {"label": c["label"], "score": score, "blocks": to_blocks(c["text"])}
                    for c, score in results
                ],
            }
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()


def main():
    server = ThreadingHTTPServer(("localhost", PORT), Handler)
    print(f"\nOuvre http://localhost:{PORT} dans ton navigateur.")
    print("Ctrl+C pour arrêter le serveur.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.")


if __name__ == "__main__":
    main()
