/**
 * Mini-moteur Markdown du site, pur et sans dépendance au DOM (testable seul).
 *
 * Il produit une chaîne HTML à partir du texte renvoyé par l'API. Tout texte source
 * est échappé ici ; les formules ($…$, $$…$$, \(…\), \[…\]) sont laissées telles quelles
 * pour que KaTeX les rende ensuite (voir `KatexDirective`).
 */
import { Block } from '../core/models';
import { accentInsensitive, escapeAttr, escapeHtml } from './text';

/** Sépare le texte en morceaux maths ($$…$$, $…$, \(…\), \[…\]) et texte ordinaire. */
const MATH_RE = /(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$(?:\\\$|[^$\n])+?\$)/g;

/** Surligne les mots cherchés dans un texte brut (sans accents, sans casse). */
export function highlightPlain(text: string, terms: readonly string[]): string {
  let html = escapeHtml(text);
  for (const t of terms) {
    if (t.length < 3) continue;
    const re = /\d$/.test(t)
      ? new RegExp('(' + accentInsensitive(t).replace(/ /g, '\\s+') + ')(?!\\d)', 'gi') // « exercice 2 » ≠ « exercice 21 »
      : new RegExp('(' + accentInsensitive(t) + '[\\wÀ-ÿ]*)', 'gi');
    html = html.replace(re, '<mark>$1</mark>');
  }
  return html;
}

function inlineMd(html: string): string {
  return html
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*\w])\*([^*\n]+)\*(?!\*)/g, '$1<em>$2</em>');
}

/**
 * ![alt](https://…) et [texte](https://…) : protégés avant le surlignage, sinon
 * <mark> casserait l'adresse. Seuls http(s) sont transformés en éléments.
 */
function linkify(part: string, terms: readonly string[]): string {
  const stash: string[] = [];
  const keep = (html: string) => `\u0002${stash.push(html) - 1}\u0002`;
  const text = part
    .replace(/!\[([^\]]*)\]\((https:\/\/[^\s)]+)\)/g, (_, alt: string, url: string) =>
      keep(
        `<a class="md-image" href="${escapeAttr(url)}" target="_blank" rel="noopener noreferrer"><img loading="lazy" referrerpolicy="no-referrer" alt="${escapeAttr(alt)}" src="${escapeAttr(url)}"></a>`,
      ),
    )
    .replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, (_, label: string, url: string) =>
      keep(
        `<a href="${escapeAttr(url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(label)}</a>`,
      ),
    );
  return inlineMd(highlightPlain(text, terms)).replace(/\u0002(\d+)\u0002/g, (_, i: string) => stash[Number(i)]);
}

/** Texte + surlignage, sans toucher aux formules. */
function richText(text: string, terms: readonly string[]): string {
  return text
    .split(MATH_RE)
    .map((part, i) => (i % 2 ? escapeHtml(part) : linkify(part, terms)))
    .join('');
}

interface SourceBlock {
  language: string;
  value: string;
  crop?: string;
}

/**
 * Mini-Markdown : les formules sont protégées avant le découpage en blocs.
 * Une question peut contenir plusieurs paragraphes, calculs et sous-listes.
 */
export function renderMd(text: string, terms: readonly string[]): string {
  const maths: string[] = [];
  const sources: SourceBlock[] = [];

  // Protéger le texte source avant les maths : aucun symbole n'y est interprété.
  // « ```pdf crop=doc=…&n=…&box=… » : zone de la page PDF où se trouve ce bloc (voir backend/pdf_crops.py).
  const protectedText = text
    .replace(
      /^([ \t]*)(`{3,})([\w-]*)(?:[^\S\n]+crop=(\S+))?[^\S\n]*\n([\s\S]*?)\n[ \t]*\2[ \t]*(?=\n|$)/gm,
      (_, indent: string, _fence: string, language: string, crop: string | undefined, source: string) => {
        const value = source
          .split('\n')
          .map((line) => (line.startsWith(indent) ? line.slice(indent.length) : line))
          .join('\n');
        return indent + `\u0001${sources.push({ language, value, crop }) - 1}\u0001`;
      },
    )
    .replace(MATH_RE, (value) => `\u0000${maths.push(value) - 1}\u0000`);

  const restore = (s: string) => s.replace(/\u0000(\d+)\u0000/g, (_, i: string) => maths[Number(i)]);

  // Le gras peut entourer une formule (« **1. $A = [0, 1[$ : ouvert.** ») : on le repère
  // avant de rendre les formules, sinon chaque morceau de texte serait traité séparément.
  const inline = (s: string) =>
    s
      .split(/\*\*(?=\S)([^*]*?\S)\*\*/)
      .map((part, i) =>
        i % 2 ? `<strong>${richText(restore(part), terms)}</strong>` : richText(restore(part), terms),
      )
      .join('');

  const item = (line: string) => line.match(/^(\s*)([-*]|\d+[.)]|[a-z]\))(?:\s+(.*)|$)/);
  const listType = (marker: string) => (/^[a-z]/.test(marker) ? 'a' : /^\d/.test(marker) ? '1' : null);
  const listValue = (marker: string) =>
    listType(marker) === 'a' ? marker.charCodeAt(0) - 96 : parseInt(marker, 10);
  const sourceBlock = (line: string) => line.trim().match(/^\u0001(\d+)\u0001$/);

  // Les formules sont déjà protégées : leurs barres verticales ne coupent pas les cellules.
  const tableCells = (line: string) =>
    line
      .trim()
      .replace(/^\|/, '')
      .replace(/(?<!\\)\|$/, '')
      .split(/(?<!\\)\|/)
      .map((cell) => cell.trim().replace(/\\\|/g, '|'));
  const tableStart = (lines: string[], i: number) =>
    i + 1 < lines.length &&
    lines[i].includes('|') &&
    lines[i + 1].includes('|') &&
    tableCells(lines[i + 1]).every((cell) => /^:?-{3,}:?$/.test(cell)) &&
    tableCells(lines[i]).length === tableCells(lines[i + 1]).length;
  const display = (line: string) => {
    const m = line.trim().match(/^\u0000(\d+)\u0000$/);
    return !!m && /^(\$\$|\\\[)/.test(maths[Number(m[1])]);
  };

  function renderSource({ language, value, crop }: SourceBlock): string {
    const pdfSource = language === 'pdf' || language === 'pdf-steps' || language === 'pdf-matrix';
    const summary =
      language === 'pdf-steps' ? 'Étapes intermédiaires à vérifier' : 'Afficher l’expression d’origine';
    if (pdfSource && crop) {
      // La formule telle qu'imprimée ; le texte extrait reste consultable.
      // Taille à l'échelle du texte : 1,6 px par point PDF (le PNG est rendu à 200 dpi pour rester net).
      const box = (new URLSearchParams(crop).get('box') || '').split(',').map(Number);
      const width = box.length === 4 && box.every(Number.isFinite) ? Math.round((box[2] - box[0]) * 1.6) : 0;
      return (
        `<figure class="source-crop"><img loading="lazy" decoding="async"${width ? ` style="width:${width}px"` : ''} src="/api/crop?${escapeHtml(crop)}"` +
        ` alt="${escapeHtml(value.replace(/\s+/g, ' '))}"><figcaption>formule du document d’origine</figcaption></figure>` +
        `<details class="source-excerpt"><summary>Texte extrait</summary><pre>${escapeHtml(value)}</pre></details>`
      );
    }
    return pdfSource
      ? `<details class="source-excerpt"${language === 'pdf-matrix' ? ' open' : ''}><summary>${summary}</summary><pre>${escapeHtml(value)}</pre></details>`
      : `<pre class="code-block">${escapeHtml(value)}</pre>`;
  }

  function blocks(lines: string[]): string {
    const out: string[] = [];
    let i = 0;
    while (i < lines.length) {
      const line = lines[i];
      if (!line.trim()) {
        i++;
        continue;
      }
      const source = sourceBlock(line);
      if (source) {
        out.push(renderSource(sources[Number(source[1])]));
        i++;
        continue;
      }
      if (display(line)) {
        out.push(`<div class="math-block">${escapeHtml(restore(line.trim()))}</div>`);
        i++;
        continue;
      }
      const h = line.match(/^#{1,6}\s+(.+)$/);
      if (h) {
        out.push(`<h4>${inline(h[1])}</h4>`);
        i++;
        continue;
      }
      if (tableStart(lines, i)) {
        const headings = tableCells(line);
        const row = (cells: string[], tag: string) =>
          '<tr>' + headings.map((_, col) => `<${tag}>${inline(cells[col] || '')}</${tag}>`).join('') + '</tr>';
        out.push('<div class="md-table"><table><thead>' + row(headings, 'th') + '</thead><tbody>');
        i += 2;
        while (i < lines.length && lines[i].trim() && lines[i].includes('|')) {
          out.push(row(tableCells(lines[i++]), 'td'));
        }
        out.push('</tbody></table></div>');
        continue;
      }
      // « > … » : remarque d'une transcription (erreur corrigée, complément rédigé)
      if (/^\s*>/.test(line)) {
        const note: string[] = [];
        while (i < lines.length && /^\s*>/.test(lines[i])) note.push(lines[i++].replace(/^\s*> ?/, ''));
        out.push(`<div class="note">${blocks(note)}</div>`);
        continue;
      }
      const first = item(line);
      if (first) {
        const type = listType(first[2]);
        const ordered = type !== null;
        const tag = ordered ? 'ol' : 'ul';
        const indent = first[1].length;
        out.push(ordered ? `<ol${type === 'a' ? ' type="a"' : ''} start="${listValue(first[2])}">` : '<ul>');
        while (i < lines.length) {
          const m = item(lines[i]);
          if (!m || m[1].length !== indent || listType(m[2]) !== type) break;
          const content = [m[3] || ''];
          const width = m[1].length + m[2].length + 1;
          i++;
          while (i < lines.length) {
            const next = lines[i];
            if (!next.trim()) {
              content.push('');
              i++;
              continue;
            }
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
      while (
        i < lines.length &&
        lines[i].trim() &&
        !item(lines[i]) &&
        !/^#{1,6}\s/.test(lines[i]) &&
        !/^\s*>/.test(lines[i]) &&
        !display(lines[i]) &&
        !sourceBlock(lines[i]) &&
        !tableStart(lines, i)
      ) {
        para.push(lines[i++].trim());
      }
      out.push(`<p class="prose">${inline(para.join(' '))}</p>`);
    }
    return out.join('');
  }

  // Une formule en display au milieu d'une ligne passe sur sa propre ligne, indentée comme l'élément de liste.
  const lines: string[] = [];
  for (const line of protectedText.split('\n')) {
    const parts = line.split(/(\u0000\d+\u0000)/);
    if (!parts.some(display)) {
      lines.push(line);
      continue;
    }
    const m = item(line);
    const indent = m ? ' '.repeat(m[1].length + m[2].length + 1) : (line.match(/^\s*/) as RegExpMatchArray)[0];
    let pending = '';
    for (const part of parts) {
      if (display(part)) {
        if (pending.trim()) lines.push(pending);
        lines.push(indent + part);
        pending = indent;
      } else pending += part;
    }
    if (pending.trim()) lines.push(pending);
  }
  return `<div class="md">${blocks(lines)}</div>`;
}

/** HTML d'une liste de blocs (texte, code, formules, Markdown) renvoyée par l'API. */
export function renderBlocks(blocks: readonly Block[], terms: readonly string[]): string {
  return blocks
    .map((b) => {
      switch (b.type) {
        case 'md':
          return renderMd(b.text, terms);
        case 'text':
          return `<pre class="text-excerpt">${escapeHtml(b.text)}</pre>`;
        case 'slides':
          return `<pre class="text-excerpt">${highlightPlain(b.text, terms)}</pre>`;
        case 'code':
          return `<pre class="code-block">${escapeHtml(b.text)}</pre>`;
      }
    })
    .join('');
}
