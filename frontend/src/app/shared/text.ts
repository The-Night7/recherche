/** Utilitaires de texte purs (échappement HTML, expressions régulières). */

export function escapeHtml(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

export const escapeAttr = (s: string): string => escapeHtml(s).replace(/"/g, '&quot;');

export function reEscape(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

const ACCENT_CLASS: Record<string, string> = {
  a: 'aàâä', e: 'eéèêë', i: 'iîï', o: 'oôö', u: 'uùûü', c: 'cç', y: 'yÿ',
};

/** Expression régulière insensible aux accents : « etude » trouve « étude ». */
export const accentInsensitive = (s: string): string =>
  [...s]
    .map((ch) => {
      const accents = ACCENT_CLASS[ch.toLowerCase()];
      return accents ? '[' + accents + ']' : reEscape(ch);
    })
    .join('');

export const cleanTitle = (s: string | null | undefined): string =>
  (s || '')
    .replace(/\s*·\s*année inconnue\s*$/, '')
    .replace(/\s+--?\s+/g, ' — ')
    .replace(/[_\s]+/g, ' ')
    .trim();

export const yearLabel = (y: number | null): string =>
  y === null ? '' : `${y}-${String(y + 1).slice(2)}`;
