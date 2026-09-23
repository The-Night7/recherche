const $ = id => document.getElementById(id);
const COURSE_SYM = { "analyse-rn": "ℝⁿ", "series": "Σ" };
const DEFAULT = () => ({ course: "all", kinds: [], versions: [], years: [], k: 5, recent: true });
let META = null;
let state = DEFAULT();

try { Object.assign(state, JSON.parse(localStorage.getItem("tuteur-filtres") || "{}")); } catch (e) {}
function save(){ try { localStorage.setItem("tuteur-filtres", JSON.stringify(state)); } catch (e) {} }

function escapeHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function reEscape(s){ return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

/* ---------- panneau de filtres ---------- */
function chip(label, pressed, onClick, disabled){
  const b = document.createElement("button");
  b.className = "chip"; b.textContent = label;
  b.setAttribute("aria-pressed", pressed ? "true" : "false");
  b.disabled = !!disabled;
  b.onclick = onClick;
  return b;
}
function toggleIn(list, v){ const i = list.indexOf(v); i < 0 ? list.push(v) : list.splice(i, 1); }

function coursesInScope(){
  return state.course === "all" ? META.courses : META.courses.filter(c => c.id === state.course);
}

function renderFilters(){
  // cours
  const box = $("courses"); box.innerHTML = "";
  const total = META.courses.reduce((s, c) => s + c.count, 0);
  const entries = [{ id: "all", name: "Tous les cours", count: total }, ...META.courses];
  entries.forEach(c => {
    const b = document.createElement("button");
    b.className = "course"; b.dataset.id = c.id;
    b.setAttribute("aria-pressed", state.course === c.id ? "true" : "false");
    b.innerHTML = `<span class="sym">${c.id === "all" ? "∗" : COURSE_SYM[c.id] || "·"}</span>
      <span class="name">${escapeHtml(c.name)}<small>${c.count} passages</small></span>`;
    b.onclick = () => { state.course = c.id; state.years = []; update(); };
    box.appendChild(b);
  });

  // types : on grise ceux absents du/des cours choisis
  const scope = coursesInScope();
  const kinds = $("kinds"); kinds.innerHTML = "";
  Object.entries(META.kinds).forEach(([id, label]) => {
    const n = scope.reduce((s, c) => s + (c.kinds[id] || 0), 0);
    kinds.appendChild(chip(label, state.kinds.includes(id), () => { toggleIn(state.kinds, id); update(); }, n === 0));
  });

  const versions = $("versions"); versions.innerHTML = "";
  [["enonce", "Énoncés"], ["corrige", "Corrigés"]].forEach(([id, label]) =>
    versions.appendChild(chip(label, state.versions.includes(id), () => { toggleIn(state.versions, id); update(); })));

  // années du/des cours choisis, la plus récente d'abord
  const years = [...new Set(scope.flatMap(c => c.years))].sort((a, b) => (b ?? 0) - (a ?? 0));
  const yb = $("years"); yb.innerHTML = "";
  years.forEach(y => {
    const id = y === null ? "none" : String(y);
    const label = y === null ? "sans date" : `${y}-${String(y + 1).slice(2)}`;
    yb.appendChild(chip(label, state.years.includes(id), () => { toggleIn(state.years, id); update(); }));
  });

  const ks = $("ks"); ks.innerHTML = "";
  [3, 5, 10].forEach(k => ks.appendChild(chip(String(k), state.k === k, () => { state.k = k; update(); })));

  $("recent").checked = state.recent;

  // résumé (mobile)
  const parts = [state.course === "all" ? "tous les cours" : META.courses.find(c => c.id === state.course)?.name];
  if (state.kinds.length) parts.push(state.kinds.map(k => META.kinds[k]).join("+"));
  if (state.versions.length === 1) parts.push(state.versions[0] === "corrige" ? "corrigés" : "énoncés");
  if (state.years.length) parts.push(state.years.length + " année(s)");
  $("scope-summary").textContent = parts.join(", ");
}

function update(){
  save(); renderFilters();
  if ($("q").value.trim()) doSearch();
}

/* ---------- rendu des passages ---------- */
// sépare le texte en morceaux maths ($$…$$, $…$, \(…\), \[…\]) et texte ordinaire
const MATH_RE = /(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$(?:\\\$|[^$\n])+?\$)/g;

function highlightPlain(text, terms){
  let html = escapeHtml(text);
  terms.forEach(t => {
    if (t.length < 3) return;
    const re = /\d$/.test(t)
      ? new RegExp('(' + reEscape(t).replace(/ /g, '\\s+') + ')(?!\\d)', 'gi')   // "exercice 2" ≠ "exercice 21"
      : new RegExp('(' + reEscape(t) + '[\\wÀ-ÿ]*)', 'gi');
    html = html.replace(re, '<mark>$1</mark>');
  });
  return html;
}
function inlineMd(html){
  return html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
             .replace(/(^|[^*\w])\*([^*\n]+)\*(?!\*)/g, '$1<em>$2</em>');
}
// texte + surlignage, sans toucher aux formules (KaTeX les rend ensuite)
function richText(text, terms){
  return text.split(MATH_RE).map((part, i) =>
    i % 2 ? escapeHtml(part) : inlineMd(highlightPlain(part, terms))
  ).join('');
}
// mini-Markdown : titres, listes, paragraphes
function renderMd(text, terms){
  const out = []; let list = null;
  const closeList = () => { if (list) { out.push(`</${list}>`); list = null; } };
  text.split(/\n\s*\n/).forEach(para => {
    const lines = para.split('\n');
    if (lines.every(l => /^\s*([-*]|\d+[.)])\s+/.test(l) || /^\s{2,}\S/.test(l))) {
      lines.forEach(l => {
        const m = l.match(/^\s*([-*]|\d+[.)])\s+(.*)$/);
        if (!m) { if (out.length) out[out.length - 1] = out[out.length - 1].replace(/<\/li>$/, ' ' + richText(l.trim(), terms) + '</li>'); return; }
        const tag = /\d/.test(m[1]) ? 'ol' : 'ul';
        if (list !== tag) {
          closeList(); list = tag;
          out.push(tag === 'ol' ? `<ol start="${parseInt(m[1], 10) || 1}">` : '<ul>');
        }
        out.push(`<li>${richText(m[2], terms)}</li>`);
      });
      return;
    }
    closeList();
    const h = para.match(/^#{1,6}\s+(.*)$/);
    if (h && lines.length === 1) { out.push(`<h4>${richText(h[1].replace(/\*\*/g, ''), terms)}</h4>`); return; }
    out.push(`<p class="prose">${richText(para.replace(/\n/g, ' '), terms)}</p>`);
  });
  closeList();
  return `<div class="md">${out.join('')}</div>`;
}

function renderMath(el){
  if (window.renderMathInElement) {
    renderMathInElement(el, {
      delimiters: [
        { left: "$$", right: "$$", display: true }, { left: "\\[", right: "\\]", display: true },
        { left: "$", right: "$", display: false }, { left: "\\(", right: "\\)", display: false },
      ],
      throwOnError: false,
    });
  }
}

function renderCard(r, i, tokens){
  const body = r.blocks.map(b => {
    if (b.type === "md") return renderMd(b.text, tokens);
    if (b.type === "formula") return `<div class="formula"><pre>${escapeHtml(b.text)}</pre></div>`;
    return `<p class="prose">${highlightPlain(b.text, tokens)}</p>`;
  }).join('');
  const pct = Math.round(Math.min(1, r.score) * 100);
  const tip = (r.score >= 1 ? 'Référence exacte (1 + cosinus des autres mots)' : 'Similarité cosinus')
            + (state.recent ? ' × bonus de récence' : '');
  return `
    <article class="card" data-course="${r.course}">
      <div class="card-head">
        <div class="doc">
          <span class="badge" aria-hidden="true">${COURSE_SYM[r.course] || "·"}</span>
          <span><b>${escapeHtml(r.course_name)}</b>, ${escapeHtml(r.doc_label)}</span>
          ${r.corrige ? '<span class="tag">corrigé</span>' : ''}
        </div>
        <h3 class="section">${escapeHtml(r.section || r.label)}</h3>
        <div class="score" title="${tip}">
          <span class="meter"><i style="width:${pct}%"></i></span>${r.score.toFixed(3)}
        </div>
      </div>
      <div class="card-body">${body}</div>
    </article>`;
}

/* ---------- recherche ---------- */
async function doSearch(){
  const q = $("q").value.trim();
  if (!q) return;
  const p = new URLSearchParams({ q, k: state.k, recent: state.recent ? 1 : 0 });
  if (state.course !== "all") p.set("course", state.course);
  if (state.kinds.length) p.set("kinds", state.kinds.join(","));
  if (state.versions.length) p.set("versions", state.versions.join(","));
  if (state.years.length) p.set("years", state.years.join(","));
  $("results").innerHTML = '<p class="hint loading">Recherche…</p>';
  try {
    const data = await (await fetch('/api/search?' + p)).json();
    if (data.error) { $("results").innerHTML = `<p class="empty">${escapeHtml(data.error)}</p>`; return; }
    if (!data.tokens.length) { $("results").innerHTML = '<p class="empty">Question trop courte : ajoute un mot du cours (3 lettres ou plus).</p>'; return; }
    if (!data.results.length) {
      $("results").innerHTML = `<p class="empty">Aucun passage trouvé pour <b>${data.tokens.map(escapeHtml).join(', ')}</b> avec ces filtres.
        Élargis la recherche (autre cours, plus de types ou d'années) ou reformule avec le vocabulaire du cours.</p>`;
      return;
    }
    const hl = data.highlight || data.tokens;
    const ref = data.reference
      ? `, référence <b>${escapeHtml(data.reference)}</b>${data.relaxed ? ' <span class="relaxed">(exercice introuvable, document entier)</span>' : ''}`
      : '';
    $("results").innerHTML = `<p class="count"><b>${data.results.length}</b> passage(s) sur ${data.searched} dans la sélection${ref}</p>` +
      data.results.map((r, i) => renderCard(r, i, hl)).join('');
    renderMath($("results"));
  } catch (e) {
    $("results").innerHTML = '<p class="empty">Le serveur ne répond pas. Lance <b>python3 server.py</b> puis recharge la page.</p>';
  }
}


const EXAMPLES = ["critère de d'Alembert", "rayon de convergence", "norme équivalente", "série géométrique", "différentiabilité"];
function showWelcome(){
  $("results").innerHTML = `<div class="hint">
    <p>Choisis <b>où chercher</b> (un cours, des TD, les DS d'une année…), puis tape ta question et Entrée.</p>
    <div class="examples">${EXAMPLES.map(e => `<button class="example">${escapeHtml(e)}</button>`).join('')}</div>
  </div>`;
  document.querySelectorAll(".example").forEach(b => b.onclick = () => { $("q").value = b.textContent; doSearch(); });
}

$("theme").onclick = () => {
  const root = document.documentElement;
  const cur = root.dataset.theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  root.dataset.theme = cur === "dark" ? "light" : "dark";
  try { localStorage.setItem("tuteur-theme", root.dataset.theme); } catch (e) {}
};
if (!document.documentElement.dataset.theme)
  document.documentElement.dataset.theme = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";

document.addEventListener("keydown", e => {
  if (e.key === "/" && document.activeElement !== $("q")) { e.preventDefault(); $("q").focus(); $("q").select(); }
});

$("go").onclick = doSearch;
$("q").addEventListener("keydown", e => { if (e.key === "Enter") doSearch(); });
$("recent").onchange = e => { state.recent = e.target.checked; update(); };
$("reset").onclick = () => { state = DEFAULT(); update(); };
$("toggle-filters").onclick = () => {
  const open = $("aside").classList.toggle("open");
  $("toggle-filters").setAttribute("aria-expanded", open);
};

fetch('/api/meta').then(r => r.json()).then(meta => {
  META = meta;
  if (state.course !== "all" && !META.courses.some(c => c.id === state.course)) state.course = "all";
  renderFilters();
  showWelcome();
}).catch(() => {
  $("results").innerHTML = '<p class="empty">Le serveur ne répond pas. Lance <b>python3 server.py</b> puis recharge la page.</p>';
});
