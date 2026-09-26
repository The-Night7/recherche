const $ = id => document.getElementById(id);
const COURSE_SYM = {
  "algebre1": "⊕", "algebre2": "⊕", "algebre-lineaire": "⊕", "algebre": "⊕",
  "analyse1": "∫", "analyse2": "∫", "analyse-rn": "ℝⁿ", "series": "Σ",
  "cef1": "¶", "cef": "¶", "ic1": "✎", "shs": "§", "ethique": "§", "design": "✎", "histoire-du-design": "✎",
  "informatique1": "⌘", "informatique2": "⌘", "informatique3": "⌘", "informatique4": "⌘",
  "physique1": "F", "mecanique-du-point": "→", "electromagnetisme": "Φ", "ondes": "∿", "physique-moderne": "Ψ",
  "projet1-s1": "◇", "projet1-s2": "◇", "projet": "◇", "integration-proba": "μ",
  "algorithmique": "⟳", "bdd": "▤", "data-exploration": "▦", "mesures-integration": "μ", "optimisation": "∇",
  "probabilites": "ℙ", "programmation-procedurale": "{ }", "unix": "$", "informations": "i",
  "complement-maths": "∀", "systeme-exploitation": ">_",
  "analyse-numerique": "≈", "data-mining": "◈", "equations-differentielles": "y′", "gestion-entreprise": "€",
  "statistique-inferentielle": "x̄", "theorie-graphes": "⊶", "theorie-langages": "L",
  "anglais": "Aa", "architecture-reseau": "⇄", "communication-interculturelle": "@", "decidabilite-complexite": "⊥",
  "ece": "¶", "modele-lineaire": "β", "optimisation-deterministe": "∇", "programmation-fonctionnelle": "λ",
  "traitement-signal": "∿", "economie": "€", "compressive-sensing": "ℓ₁", "design-decision": "◆",
  "edp": "∂", "ia": "AI", "methodes-agiles": "⟲", "programmation-parallele": "∥", "series-temporelles": "t",
};
const DOMAINS = {
  math: "algebre1 algebre2 algebre-lineaire algebre analyse1 analyse2 analyse-rn series integration-proba complement-maths mesures-integration probabilites optimisation optimisation-deterministe analyse-numerique equations-differentielles statistique-inferentielle modele-lineaire edp series-temporelles compressive-sensing data-exploration data-mining",
  info: "informatique1 informatique2 informatique3 informatique4 algorithmique bdd programmation-procedurale programmation-fonctionnelle programmation-parallele unix systeme-exploitation theorie-graphes theorie-langages decidabilite-complexite architecture-reseau ia methodes-agiles",
  physics: "physique1 mecanique-du-point electromagnetisme ondes physique-moderne traitement-signal",
};
const DOMAIN_OF = Object.fromEntries(Object.entries(DOMAINS).flatMap(([d, ids]) => ids.split(" ").map(id => [id, d])));
const baseId = id => id.replace(/^(?:ing-1-s\d-(?:gm|info|data)|ing-\d(?:-s\d)?)-/, "");
const courseSym = id => COURSE_SYM[baseId(id)] || "·";
const courseDomain = id => DOMAIN_OF[baseId(id)] || "shs";
const DEFAULT = () => ({ program: "all", study_year: "all", semester: "all", track: "all", course: "all", kinds: [], versions: [], years: [], k: 5, recent: true });
let META = null;
let state = DEFAULT();

try {
  const saved = JSON.parse(localStorage.getItem("tuteur-filtres") || "{}");
  Object.assign(state, saved);
  if (!("program" in saved) && state.study_year !== "all") state.program = "preing";
} catch (e) {}
function save(){ try { localStorage.setItem("tuteur-filtres", JSON.stringify(state)); } catch (e) {} }

const cleanTitle = s => (s || "").replace(/\s*·\s*année inconnue\s*$/, "").replace(/\s+--?\s+/g, " — ").replace(/[_\s]+/g, " ").trim();
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
  return availableCourses().filter(c => state.course === "all" || c.id === state.course);
}

function availableCourses(){
  return META.courses.filter(c => (state.program === "all" || c.program === state.program)
    && (state.study_year === "all" || String(c.study_year) === state.study_year)
    && (state.semester === "all" || String(c.semester ?? "none") === state.semester)
    && (state.track === "all" || c.track === state.track));
}

function contextChoices(){
  return META.curricula.filter(c => c.count > 0 && (state.program === "all" || c.program === state.program)
    && (state.study_year === "all" || String(c.study_year) === state.study_year));
}

function availableTracks(){
  return [...new Set(contextChoices().filter(c => state.semester === "all" || String(c.semester ?? "none") === state.semester)
    .map(c => c.track).filter(Boolean))];
}

function scopeLabel(){
  const chosen = META.courses.find(c => c.id === state.course);
  if (chosen) return chosen.curriculum_label;
  const programs = [...new Set(availableCourses().map(c => c.program))];
  const year = programs.map(p => META.programs[p] + (state.study_year === "all" ? "" : ` ${state.study_year}`)).join(" et ");
  const semester = state.semester === "all" ? "tous les semestres" : state.semester === "none" ? "hors semestre" : `semestre ${state.semester}`;
  return `${year || "Tous les cycles"} — ${semester}${state.track === "all" ? "" : ` — ${state.track.toUpperCase()}`}`;
}

function normalizeScope(){
  if (state.program !== "all" && !META.programs[state.program]) state.program = "all";
  if (!["all", "1", "2"].includes(state.study_year)) state.study_year = "all";
  if (!contextChoices().some(c => String(c.semester ?? "none") === state.semester)) state.semester = "all";
  if (!availableTracks().includes(state.track)) state.track = "all";
  if (!availableCourses().some(c => c.id === state.course)) state.course = "all";
  const courses = coursesInScope();
  state.kinds = state.kinds.filter(k => courses.some(c => c.kinds[k]));
  state.years = state.years.filter(y => courses.some(c => c.years.some(v => String(v ?? "none") === y)));
}

function renderFilters(){
  const programOptions = [["all", "Tous"], ...Object.entries(META.programs)];
  const semesterOptions = [...new Set(contextChoices().map(c => String(c.semester ?? "none")))].sort()
    .map(value => [value, value === "none" ? "Hors semestre" : `Semestre ${value}`]);
  const tracks = availableTracks();
  $("track-field").hidden = tracks.length === 0;
  [["programs", "program", programOptions],
   ["study-years", "study_year", [["all", "Toutes"], ["1", "Année 1"], ["2", "Année 2"]]],
   ["semesters", "semester", [["all", "Tous"], ...semesterOptions]],
   ["tracks", "track", [["all", "Tous"], ...tracks.map(t => [t, t.toUpperCase()])]]].forEach(([id, field, options]) => {
    const container = $(id); container.innerHTML = "";
    options.forEach(([value, label]) => container.appendChild(chip(label,
      state[field] === value, () => { state[field] = value; normalizeScope(); update(); })));
  });
  $("curriculum").textContent = scopeLabel();
  // cours
  const box = $("courses"); box.innerHTML = "";
  const available = availableCourses();
  const total = available.reduce((s, c) => s + c.count, 0);
  const entries = [{ id: "all", name: "Toutes les matières", count: total }, ...available];
  let group = null;
  entries.forEach(c => {
    if (c.curriculum && c.curriculum !== group) {
      group = c.curriculum;
      const heading = document.createElement("h2");
      heading.className = "course-group";
      heading.textContent = c.curriculum_label;
      box.appendChild(heading);
    }
    const b = document.createElement("button");
    b.className = "course"; b.dataset.id = c.id;
    if (c.id !== "all") b.dataset.domain = courseDomain(c.id);
    b.setAttribute("aria-pressed", state.course === c.id ? "true" : "false");
    b.innerHTML = `<span class="sym" data-len="${c.id === "all" ? 1 : [...courseSym(c.id)].length}">${c.id === "all" ? "∗" : courseSym(c.id)}</span>
      <span class="name">${escapeHtml(c.name)}<small>${c.count} passages</small></span>`;
    b.onclick = () => {
      state.course = c.id;
      state.years = [];
      normalizeScope();
      update();
    };
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
  const chosen = META.courses.find(c => c.id === state.course);
  const parts = [chosen?.curriculum_label || scopeLabel(), chosen?.name || "toutes les matières"];
  if (state.kinds.length) parts.push(state.kinds.map(k => META.kinds[k]).join("+"));
  if (state.versions.length === 1) parts.push(state.versions[0] === "corrige" ? "corrigés" : "énoncés");
  if (state.years.length) parts.push(state.years.length + " année(s) scolaire(s)");
  $("scope-summary").textContent = parts.join(", ");
}

function update(){
  save(); renderFilters();
  if ($("q").value.trim()) doSearch();
  else showWelcome();
}

/* ---------- rendu des passages ---------- */
// sépare le texte en morceaux maths ($$…$$, $…$, \(…\), \[…\]) et texte ordinaire
const MATH_RE = /(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$(?:\\\$|[^$\n])+?\$)/g;

const ACCENT_CLASS = { a: "aàâä", e: "eéèêë", i: "iîï", o: "oôö", u: "uùûü", c: "cç", y: "yÿ" };
const accentInsensitive = s => [...s].map(ch => ACCENT_CLASS[ch.toLowerCase()] ? "[" + ACCENT_CLASS[ch.toLowerCase()] + "]" : reEscape(ch)).join("");
function highlightPlain(text, terms){
  let html = escapeHtml(text);
  terms.forEach(t => {
    if (t.length < 3) return;
    const re = /\d$/.test(t)
      ? new RegExp('(' + accentInsensitive(t).replace(/ /g, '\\s+') + ')(?!\\d)', 'gi')   // "exercice 2" ≠ "exercice 21"
      : new RegExp('(' + accentInsensitive(t) + '[\\wÀ-ÿ]*)', 'gi');
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
// Mini-Markdown : les formules sont protégées avant le découpage en blocs.
// Une question peut contenir plusieurs paragraphes, calculs et sous-listes.
function renderMd(text, terms){
  const maths = [];
  const sources = [];
  // Protéger le texte source avant les maths : aucun symbole n'y est interprété.
  const protectedText = text.replace(/^([ \t]*)(`{3,})([\w-]*)[^\S\n]*\n([\s\S]*?)\n[ \t]*\2[ \t]*(?=\n|$)/gm,
    (_, indent, fence, language, source) => {
      const value = source.split('\n').map(line => line.startsWith(indent) ? line.slice(indent.length) : line).join('\n');
      return indent + `\u0001${sources.push({language, value}) - 1}\u0001`;
    }).replace(MATH_RE, value => {
    const id = maths.push(value) - 1;
    return `\u0000${id}\u0000`;
  });
  const restore = s => s.replace(/\u0000(\d+)\u0000/g, (_, i) => maths[Number(i)]);
  const inline = s => richText(restore(s), terms);
  const item = line => line.match(/^(\s*)([-*]|\d+[.)]|[a-z]\))(?:\s+(.*)|$)/);
  const listType = marker => /^[a-z]/.test(marker) ? 'a' : /^\d/.test(marker) ? '1' : null;
  const listValue = marker => listType(marker) === 'a' ? marker.charCodeAt(0) - 96 : parseInt(marker, 10);
  const sourceBlock = line => line.trim().match(/^\u0001(\d+)\u0001$/);
  const display = line => {
    const m = line.trim().match(/^\u0000(\d+)\u0000$/);
    return m && /^(\$\$|\\\[)/.test(maths[Number(m[1])]);
  };
  function blocks(lines){
    const out = [];
    let i = 0;
    while (i < lines.length){
      const line = lines[i];
      if (!line.trim()){ i++; continue; }
      const source = sourceBlock(line);
      if (source){
        const {language, value} = sources[Number(source[1])];
        const pdfSource = language === 'pdf' || language === 'pdf-steps' || language === 'pdf-matrix';
        const summary = language === 'pdf-steps' ? 'Étapes intermédiaires à vérifier' : 'Afficher l’expression d’origine';
        out.push(pdfSource
          ? `<details class="source-excerpt"${language === 'pdf-matrix' ? " open" : ""}><summary>${summary}</summary><pre>${escapeHtml(value)}</pre></details>`
          : `<pre class="code-block">${escapeHtml(value)}</pre>`);
        i++; continue;
      }
      if (display(line)){
        out.push(`<div class="math-block">${escapeHtml(restore(line.trim()))}</div>`);
        i++; continue;
      }
      const h = line.match(/^#{1,6}\s+(.+)$/);
      if (h){ out.push(`<h4>${inline(h[1])}</h4>`); i++; continue; }
      const first = item(line);
      if (first){
        const type = listType(first[2]);
        const ordered = type !== null;
        const tag = ordered ? 'ol' : 'ul';
        const indent = first[1].length;
        out.push(ordered ? `<ol${type === 'a' ? ' type="a"' : ''} start="${listValue(first[2])}">` : '<ul>');
        while (i < lines.length){
          const m = item(lines[i]);
          if (!m || m[1].length !== indent || listType(m[2]) !== type) break;
          const content = [m[3] || ''];
          const width = m[1].length + m[2].length + 1;
          i++;
          while (i < lines.length){
            const next = lines[i];
            if (!next.trim()){ content.push(''); i++; continue; }
            if (next.search(/\S/) <= indent) break;
            content.push(next.slice(Math.min(width, next.search(/\S/))));
            i++;
          }
          out.push(`<li${ordered ? ` value="${listValue(m[2])}"` : ''}>${blocks(content)}</li>`);
        }
        out.push(`</${tag}>`);
        continue;
      }
      const para = [line.trim()];
      i++;
      while (i < lines.length && lines[i].trim() && !item(lines[i])
             && !/^#{1,6}\s/.test(lines[i]) && !display(lines[i]) && !sourceBlock(lines[i])){
        para.push(lines[i++].trim());
      }
      out.push(`<p class="prose">${inline(para.join(' '))}</p>`);
    }
    return out.join('');
  }
  const lines = [];
  for (const line of protectedText.split('\n')){
    const parts = line.split(/(\u0000\d+\u0000)/);
    if (!parts.some(display)){ lines.push(line); continue; }
    const m = item(line);
    const indent = m ? ' '.repeat(m[1].length + m[2].length + 1) : line.match(/^\s*/)[0];
    let pending = '';
    for (const part of parts){
      if (display(part)){
        if (pending.trim()) lines.push(pending);
        lines.push(indent + part);
        pending = indent;
      } else pending += part;
    }
    if (pending.trim()) lines.push(pending);
  }
  return `<div class="md">${blocks(lines)}</div>`;
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

function renderBlocks(blocks, tokens){
  return blocks.map(b => {
    if (b.type === "md") return renderMd(b.text, tokens);
    if (b.type === "text") return `<pre class="text-excerpt">${escapeHtml(b.text)}</pre>`;
    if (b.type === "slides") return `<pre class="text-excerpt">${highlightPlain(b.text, tokens)}</pre>`;
    if (b.type === "code") return `<pre class="code-block">${escapeHtml(b.text)}</pre>`;
    if (b.type === "formula") return `<div class="formula"><pre>${escapeHtml(b.text)}</pre></div>`;
    return `<p class="prose">${highlightPlain(b.text, tokens)}</p>`;
  }).join('');
}
function renderCard(r, i, tokens){
  const body = renderBlocks(r.blocks, tokens);
  const alt = r.alt ? renderBlocks(r.alt, tokens) : "";
  const pct = Math.round(Math.min(1, r.score) * 100);
  const tip = (r.score >= 1 ? 'Référence exacte (1 + cosinus des autres mots)' : 'Similarité cosinus')
            + (state.recent ? ' × bonus de récence' : '');
  return `
    <article class="card" data-course="${r.course}" data-domain="${courseDomain(r.course)}">
      <div class="card-head">
        <div class="doc">
          <span class="badge" aria-hidden="true">${courseSym(r.course)}</span>
          ${r.curriculum_label ? `<span class="context-tag">${escapeHtml(r.curriculum_label)}</span>` : ''}
          <span><b>${escapeHtml(r.course_name)}</b>, ${escapeHtml(cleanTitle(r.doc_label))}</span>
          ${r.corrige ? '<span class="tag">corrigé</span>' : ''}
          ${alt ? '<button type="button" class="view-toggle" aria-pressed="false" title="Reconstruit les formules à partir du texte extrait : peut se tromper">Mettre en forme</button>' : ''}
        </div>
        <h3 class="section">${escapeHtml(cleanTitle(r.section || r.label))}</h3>
        <div class="score" title="${tip}">
          <span class="meter"><i style="width:${pct}%"></i></span>${r.score.toFixed(3)}
        </div>
      </div>
      <div class="card-body">${body}</div>
      ${alt ? `<div class="card-body" hidden>${alt}</div>` : ''}
    </article>`;
}

/* ---------- recherche ---------- */
let searchSequence = 0;
async function doSearch(){
  const q = $("q").value.trim();
  if (!q) return;
  const sequence = ++searchSequence;
  const p = new URLSearchParams({ q, k: state.k, recent: state.recent ? 1 : 0 });
  if (state.course !== "all") p.set("course", state.course);
  if (state.program !== "all") p.set("program", state.program);
  if (state.track !== "all") p.set("track", state.track);
  if (state.study_year !== "all") p.set("study_year", state.study_year);
  if (state.semester !== "all") p.set("semester", state.semester);
  if (state.kinds.length) p.set("kinds", state.kinds.join(","));
  if (state.versions.length) p.set("versions", state.versions.join(","));
  if (state.years.length) p.set("years", state.years.join(","));
  $("results").innerHTML = '<p class="hint loading">Recherche…</p>';
  try {
    const data = await (await fetch('/api/search?' + p)).json();
    if (sequence !== searchSequence) return;
    if (data.error) { $("results").innerHTML = `<p class="empty">${escapeHtml(data.error)}</p>`; return; }
    if (!data.tokens.length) { $("results").innerHTML = '<p class="empty">Question trop courte : ajoute un mot du cours (3 lettres ou plus).</p>'; return; }
    if (!data.results.length) {
      $("results").innerHTML = `<p class="empty">Aucun passage trouvé pour <b>${data.tokens.map(escapeHtml).join(', ')}</b> avec ces filtres.
        Élargis la recherche (autre matière, plus de types ou d'années) ou reformule avec le vocabulaire du cours.</p>`;
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
    if (sequence !== searchSequence) return;
    $("results").innerHTML = '<p class="empty">Le serveur ne répond pas. Lance <b>python3 server.py</b> puis recharge la page.</p>';
  }
}


const EXAMPLES = {
  "analyse-rn": ["norme équivalente", "différentiabilité"],
  "series": ["critère de d'Alembert", "rayon de convergence"],
  "informatique3": ["listes chaînées", "arbres binaires", "piles et files"],
  "electromagnetisme": ["théorème de Gauss", "champ magnétique"],
  "shs": ["recherche documentaire", "méthodes"],
  "algebre1": ["nombres complexes", "polynômes"],
  "analyse1": ["limites", "suites"],
  "informatique1": ["boucles", "HTML"],
  "physique1": ["mécanique", "énergie"],
  "cef1": ["communication"],
  "ic1": ["ingénieur"],
  "projet1-s1": ["projet"],
  "algebre2": ["applications linéaires", "matrices"],
  "analyse2": ["intégrales", "développements limités"],
  "informatique2": ["pointeurs", "fonctions"],
  "mecanique-du-point": ["énergie cinétique"],
  "projet1-s2": ["projet"],
  "algebre-lineaire": ["diagonalisation", "produit scalaire"],
  "ethique": ["éthique"],
  "informatique4": ["classes", "héritage"],
  "integration-proba": ["variables aléatoires", "intégration"],
  "ondes": ["propagation", "interférences"],
  "physique-moderne": ["quantique", "fonction d'onde"],
};
const ING_EXAMPLES = {
  "algebre": ["diagonalisation"], "algorithmique": ["complexité"], "bdd": ["requêtes SQL"],
  "data-exploration": ["régression"], "mesures-integration": ["fonctions mesurables"],
  "probabilites": ["variables aléatoires"], "optimisation": ["simplexe"],
  "programmation-procedurale": ["pointeurs"], "unix": ["commandes shell"],
  "analyse-numerique": ["interpolation"], "data-mining": ["classification"],
  "equations-differentielles": ["équations différentielles"], "statistique-inferentielle": ["estimation"],
  "systeme-exploitation": ["processus"], "theorie-graphes": ["plus court chemin"],
  "theorie-langages": ["automates"], "architecture-reseau": ["adressage IP"],
  "decidabilite-complexite": ["machine de Turing"], "modele-lineaire": ["régression linéaire"],
  "optimisation-deterministe": ["gradient"], "programmation-fonctionnelle": ["Scala"],
  "traitement-signal": ["transformée de Fourier"], "economie": ["marché"],
  "compressive-sensing": ["parcimonie"], "edp": ["différences finies"],
  "ia": ["apprentissage par renforcement"], "programmation-parallele": ["OpenMP"],
  "series-temporelles": ["moyenne mobile"], "methodes-agiles": ["Scrum"],
};
function courseExamples(id){
  return EXAMPLES[id] || ING_EXAMPLES[id.replace(/^ing-[12](?:-s[12])?(?:-(?:gm|info|data))?-/, "")] || [];
}
function showWelcome(){
  ++searchSequence;
  const courses = coursesInScope();
  const examples = state.course === "all"
    ? [...new Set(courses.map(c => courseExamples(c.id)[0]).filter(Boolean))].slice(0, 8)
    : courseExamples(state.course);
  $("results").innerHTML = `<div class="hint">
    <p>Retrouve les cours et exercices de <b>${escapeHtml(courses.length === 1 ? courses[0].curriculum_label : scopeLabel())}</b>.</p>
    <p>Choisis ton cycle, ton année, ton semestre et ta matière, puis tape une notion ou une référence comme « TD1 exercice 2 ».</p>
    <div class="examples">${examples.map(e => `<button class="example">${escapeHtml(e)}</button>`).join('')}</div>
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

$("results").addEventListener("click", e => {
  const button = e.target.closest(".view-toggle");
  if (!button) return;
  const bodies = button.closest(".card").querySelectorAll(".card-body");
  const formatted = button.getAttribute("aria-pressed") !== "true";
  button.setAttribute("aria-pressed", formatted);
  button.textContent = formatted ? "Texte d’origine" : "Mettre en forme";
  bodies[0].hidden = formatted;
  bodies[1].hidden = !formatted;
});

fetch('/api/meta').then(r => r.json()).then(meta => {
  META = meta;
  normalizeScope();
  renderFilters();
  showWelcome();
}).catch(() => {
  $("results").innerHTML = '<p class="empty">Le serveur ne répond pas. Lance <b>python3 server.py</b> puis recharge la page.</p>';
});
