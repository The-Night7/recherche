const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const { test } = require('node:test');
const context = { document: { getElementById: () => null }, localStorage: { getItem: () => null } };
vm.createContext(context);
vm.runInContext(fs.readFileSync('web/app.js', 'utf8').split('/* ---------- recherche ---------- */')[0], context);
const render = (text, terms = []) => context.renderMd(text, terms);

test('paragraphs and calculations belong to their numbered question', () => {
  const html = render('1. Première étape\n\n   $$x=1$$\n\n   Explication.\n\n   - Détail\n\n2. Suite');
  assert.equal((html.match(/<ol /g) || []).length, 1);
  assert.match(html, /<li value="1">.*math-block.*Explication.*<ul>.*Détail.*<\/ul><\/li><li value="2">/s);
});

test('display formulas directly after a list marker stay inside it', () => {
  const html = render('1. $$x=1$$\n2. \\[y=2\\]');
  assert.match(html, /<li value="1"><div class="math-block">.*<\/div><\/li><li value="2"><div class="math-block">/s);
  assert.equal((html.match(/<ol /g) || []).length, 1);
});

test('blank lines and alignment inside LaTeX survive Markdown', () => {
  const math = '$$\\begin{aligned}\nx &= 1 \\\\\n\ny &= 2\n\\end{aligned}$$';
  const html = render('Intro\n' + math + '\nConclusion');
  assert.equal((html.match(/class="math-block"/g) || []).length, 1);
  assert.match(html, /x &amp;= 1 \\\\\n\ny &amp;= 2/);
  assert.match(html, /<p class="prose">Conclusion<\/p>/);
});

test('lists keep source numbering even with gaps', () => {
  assert.match(render('3. Troisième\n5. Cinquième'), /<ol start="3"><li value="3">.*<li value="5">/s);
});

test('headings do not require a blank line', () => {
  assert.match(render('## Réponse 4\nLe calcul.'), /<h4>Réponse 4<\/h4><p/);
});

test('highlighting leaves LaTeX intact and source HTML is escaped', () => {
  const html = render('convergence $convergence_n$ <script>alert(1)</script>', ['convergence']);
  assert.match(html, /<mark>convergence<\/mark>/);
  assert.match(html, /\$convergence_n\$/);
  assert.doesNotMatch(html, /<script>/);
});
