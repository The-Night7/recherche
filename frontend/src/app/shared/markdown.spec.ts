import { renderMd } from './markdown';

const render = (text: string, terms: string[] = []) => renderMd(text, terms);
const count = (html: string, re: RegExp) => (html.match(re) || []).length;

describe('renderMd', () => {
  it('keeps formulas, escaped pipes and safe text in transcription tables', () => {
    const html = render('Valeurs\n| $x$ | Valeur |\n| --- | --- |\n| $|x|$ | **maximum** |\n| a\\|b | <script>x</script> |');
    expect(html).toMatch(/<p class="prose">Valeurs<\/p><div class="md-table"><table>/);
    expect(count(html, /<tr>/g)).toBe(3);
    expect(count(html, /<td>/g)).toBe(4);
    expect(html).toContain('<td>$|x|$</td>');
    expect(html).toContain('<td>a|b</td>');
    expect(html).toContain('<strong>maximum</strong>');
    expect(html).toContain('&lt;script&gt;');
    expect(html).not.toContain('<script>');
  });

  it('leaves ordinary pipes and fenced tables as text', () => {
    expect(render('a | b\nc | d')).not.toContain('<table>');
    const html = render('```text\n| a | b |\n| --- | --- |\n```');
    expect(html).not.toContain('<table>');
    expect(html).toContain('<pre class="code-block">');
  });

  it('keeps paragraphs and calculations inside their numbered question', () => {
    const html = render('1. Première étape\n\n   $$x=1$$\n\n   Explication.\n\n   - Détail\n\n2. Suite');
    expect(count(html, /<ol /g)).toBe(1);
    expect(html).toMatch(/<li value="1">.*math-block.*Explication.*<ul>.*Détail.*<\/ul><\/li><li value="2">/s);
  });

  it('keeps display formulas that directly follow a list marker inside it', () => {
    const html = render('1. $$x=1$$\n2. \\[y=2\\]');
    expect(html).toMatch(/<li value="1"><div class="math-block">.*<\/div><\/li><li value="2"><div class="math-block">/s);
    expect(count(html, /<ol /g)).toBe(1);
  });

  it('keeps blank lines and alignment inside LaTeX', () => {
    const math = '$$\\begin{aligned}\nx &= 1 \\\\\n\ny &= 2\n\\end{aligned}$$';
    const html = render('Intro\n' + math + '\nConclusion');
    expect(count(html, /class="math-block"/g)).toBe(1);
    expect(html).toContain('x &amp;= 1 \\\\\n\ny &amp;= 2');
    expect(html).toContain('<p class="prose">Conclusion</p>');
  });

  it('keeps source numbering even with gaps', () => {
    expect(render('3. Troisième\n5. Cinquième')).toMatch(/<ol start="3"><li value="3">.*<li value="5">/s);
  });

  it('does not require a blank line after a heading', () => {
    expect(render('## Réponse 4\nLe calcul.')).toMatch(/<h4>Réponse 4<\/h4><p/);
  });

  it('highlights without touching LaTeX, and escapes source HTML', () => {
    const html = render('convergence $convergence_n$ <script>alert(1)</script>', ['convergence']);
    expect(html).toContain('<mark>convergence</mark>');
    expect(html).toContain('$convergence_n$');
    expect(html).not.toContain('<script>');
  });

  it('groups lettered questions into one list with their full expression', () => {
    const html = render('a)\n\n   $$\\lim_{x\\to0}\\frac{\\sin(x)}{x}$$\n\nb)\n\n   $$\\cosh(x)$$');
    expect(html).toMatch(/<ol type="a" start="1"><li value="1"><div class="math-block">.*<\/li><li value="2"><div class="math-block">/s);
    expect(count(html, /<ol/g)).toBe(1);
    expect(count(html, /class="math-block"/g)).toBe(2);
    expect(html).not.toContain('class="prose"');
  });

  it('offers unreadable PDF source on demand, closed by default', () => {
    const html = render(
      'a)\n\n   ```pdf\n   limx→0\n   $x$\n   ## titre\n   1. fragment\n   <script>danger</script>\n   ```\n\nb)\n\n   $$y=1$$',
      ['fragment'],
    );
    expect(html).toMatch(
      /<li value="1"><details class="source-excerpt"><summary>Afficher l’expression d’origine<\/summary><pre>limx→0\n\$x\$\n## titre\n1\. fragment\n&lt;script&gt;/s,
    );
    expect(html).not.toMatch(/<h4>|<script>|<mark>|<details[^>]*\bopen\b|math-source|à vérifier/);
    expect(count(html, /class="source-excerpt"/g)).toBe(1);
    expect(html).toMatch(/<li value="2"><div class="math-block">/);
  });

  it('nests numbered and lettered lists without changing their markers', () => {
    const html = render('1. Question\n\n   a) Premier calcul\n\n      $$x=1$$\n\n   b) Deuxième calcul\n\n2. Suite');
    expect(html).toMatch(/<ol start="1">.*<ol type="a" start="1">.*<li value="2">.*<\/ol><\/li><li value="2">/s);
  });

  it('accepts source fences containing shorter backtick sequences', () => {
    expect(render('````pdf\nsource ``` littérale\n````')).toContain('<pre>source ``` littérale</pre>');
  });

  it('collapses uncertain intermediate steps beside the readable calculation', () => {
    const html = render('1. Calcul\n\n   $$\\int_0^1 dt = 1$$\n\n   ```pdf-steps\n   (ln t)\n   0\n   <script>danger</script>\n   ```');
    expect(html).toContain('class="math-block"');
    expect(html).toContain('<details class="source-excerpt"><summary>Étapes intermédiaires à vérifier</summary>');
    expect(html).not.toMatch(/<details[^>]*\bopen\b|<script>/);
    expect(html).toContain('&lt;script&gt;');
  });

  it('turns https images and http(s) links into elements, leaving unsafe schemes as text', () => {
    const html = render(
      '![page 1](https://exemple.fr/DS1-2023/p10.jpg)\n\nVoir [le cours](https://exemple.fr/c?a=1&b=2) et [x](javascript:alert(1)) ![y](http://exemple.fr/y.jpg)',
      ['page', 'cours'],
    );
    expect(html).toContain('<img loading="lazy" referrerpolicy="no-referrer" alt="page 1" src="https://exemple.fr/DS1-2023/p10.jpg">');
    expect(html).not.toMatch(/src="[^"]*<mark>/);
    expect(html).toMatch(/<a href="https:\/\/exemple\.fr\/c\?a=1&amp;b=2" target="_blank" rel="noopener noreferrer">le cours<\/a>/); // le libellé d'un lien n'est pas surligné
    expect(html).not.toMatch(/href="javascript:|src="http:\/\//);
  });

  it('shows the printed formula for a located PDF block, with the extracted text folded', () => {
    const html = render('Ainsi\n\n```pdf crop=doc=TD&n=29&box=10,20,110,40\nH = ∪n∈Z\nB∞\n```');
    expect(html).toMatch(/<figure class="source-crop"><img [^>]*style="width:160px" src="\/api\/crop\?doc=TD&amp;n=29&amp;box=10,20,110,40"/);
    expect(html).toContain('<details class="source-excerpt"><summary>Texte extrait</summary><pre>H = ∪n∈Z\nB∞</pre>');
    expect(render('```pdf\nx\n```')).not.toContain('source-crop');
  });

  it('frames transcription notes and keeps their formulas', () => {
    const html = render('Texte.\n\n> **Erreur corrigée :** il manque un facteur $2$.\n> Suite de la note.\n\nAprès.');
    expect(html).toContain(
      '<div class="note"><p class="prose"><strong>Erreur corrigée :</strong> il manque un facteur $2$. Suite de la note.</p></div>',
    );
    expect(html).toContain('<p class="prose">Après.</p>');
  });

  it('allows a formula inside bold text', () => {
    const html = render('**1. $A = [0, 1[$ : ni ouvert, ni fermé.** Suite.');
    expect(html).toContain('<strong>1. $A = [0, 1[$ : ni ouvert, ni fermé.</strong> Suite.');
    expect(html).not.toContain('**');
  });
});
