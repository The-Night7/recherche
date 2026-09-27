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

test('lettered questions form one list with their full expression', () => {
  const html = render('a)\n\n   $$\\lim_{x\\to0}\\frac{\\sin(x)}{x}$$\n\nb)\n\n   $$\\cosh(x)$$');
  assert.match(html, /<ol type="a" start="1"><li value="1"><div class="math-block">.*<\/li><li value="2"><div class="math-block">/s);
  assert.equal((html.match(/<ol/g) || []).length, 1);
  assert.equal((html.match(/class="math-block"/g) || []).length, 2);
  assert.doesNotMatch(html, /class="prose"/);
});

test('unreadable PDF source is available on demand, closed by default', () => {
  const html = render('a)\n\n   ```pdf\n   limx→0\n   $x$\n   ## titre\n   1. fragment\n   <script>danger</script>\n   ```\n\nb)\n\n   $$y=1$$', ['fragment']);
  assert.match(html, /<li value="1"><details class="source-excerpt"><summary>Afficher l’expression d’origine<\/summary><pre>limx→0\n\$x\$\n## titre\n1\. fragment\n&lt;script&gt;/s);
  assert.doesNotMatch(html, /<h4>|<script>|<mark>|<details[^>]*\bopen\b|math-source|à vérifier/);
  assert.equal((html.match(/class="source-excerpt"/g) || []).length, 1);
  assert.match(html, /<li value="2"><div class="math-block">/);
});

test('numbered and lettered lists nest without changing their markers', () => {
  const html = render('1. Question\n\n   a) Premier calcul\n\n      $$x=1$$\n\n   b) Deuxième calcul\n\n2. Suite');
  assert.match(html, /<ol start="1">.*<ol type="a" start="1">.*<li value="2">.*<\/ol><\/li><li value="2">/s);
});

test('source fences can contain shorter backtick sequences', () => {
  const html = render('````pdf\nsource ``` littérale\n````');
  assert.match(html, /<pre>source ``` littérale<\/pre>/);
});

test('uncertain intermediate steps are collapsed beside the readable calculation', () => {
  const html = render('1. Calcul\n\n   $$\\int_0^1 dt = 1$$\n\n   ```pdf-steps\n   (ln t)\n   0\n   <script>danger</script>\n   ```');
  assert.match(html, /class="math-block"/);
  assert.match(html, /<details class="source-excerpt"><summary>Étapes intermédiaires à vérifier<\/summary>/);
  assert.doesNotMatch(html, /<details[^>]*\bopen\b|<script>/);
  assert.match(html, /&lt;script&gt;/);
});

test('computer science excerpts preserve code without interpreting math or HTML', () => {
  const result = {
    course: 'informatique3', course_name: 'Informatique 3', doc_label: 'TD2', section: 'Exercice 1', score: 1,
    curriculum_label: 'Préing 2 — semestre 1',
    blocks: [{type:'text', text:'int n = 2;\n    p->next = NULL;\n#include <stdio.h>\n$x$'}]
  };
  const html = context.renderCard(result, 0, ['int']);
  assert.match(html, /<pre class="text-excerpt">int n = 2;\n    p-&gt;next = NULL;/);
  assert.match(html, /#include &lt;stdio.h&gt;\n\$x\$<\/pre>/);
  assert.doesNotMatch(html, /math-block|<mark>|<stdio/);
  assert.match(html, /class="context-tag">Préing 2 — semestre 1<\/span>/);
});

test('markdown images and links become elements, unsafe schemes stay text', () => {
  const html = render('![page 1](https://exemple.fr/DS1-2023/p10.jpg)\n\nVoir [le cours](https://exemple.fr/c?a=1&b=2) et [x](javascript:alert(1)) ![y](http://exemple.fr/y.jpg)', ['page', 'cours']);
  assert.match(html, /<img loading="lazy" referrerpolicy="no-referrer" alt="page 1" src="https:\/\/exemple\.fr\/DS1-2023\/p10\.jpg">/);
  assert.doesNotMatch(html, /src="[^"]*<mark>/);
  assert.match(html, /<a href="https:\/\/exemple\.fr\/c\?a=1&amp;b=2" target="_blank" rel="noopener noreferrer">le <mark>cours<\/mark><\/a>|<a href="https:\/\/exemple\.fr\/c\?a=1&amp;b=2" target="_blank" rel="noopener noreferrer">le cours<\/a>/);
  assert.doesNotMatch(html, /href="javascript:|src="http:\/\//);
});
