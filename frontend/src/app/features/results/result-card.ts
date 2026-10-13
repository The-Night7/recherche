import { ChangeDetectionStrategy, Component, computed, input, output, signal } from '@angular/core';
import { pageUrl } from '../../core/api.service';
import { courseDomain, courseSym } from '../../core/course-meta';
import { SearchResult } from '../../core/models';
import { TrustedHtmlPipe } from '../../shared/html.pipe';
import { ImageFallbackDirective } from '../../shared/image-fallback.directive';
import { KatexDirective } from '../../shared/katex.directive';
import { renderBlocks } from '../../shared/markdown';
import { cleanTitle } from '../../shared/text';

interface CardView {
  label: string;
  hint: string;
  html: string;
}

/** Un passage de cours : en-tête, onglets (page d'origine / texte / formules), vidéos liées. */
@Component({
  selector: 'app-result-card',
  imports: [TrustedHtmlPipe, KatexDirective, ImageFallbackDirective],
  templateUrl: './result-card.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ResultCard {
  readonly result = input.required<SearchResult>();
  /** Mots à surligner. */
  readonly terms = input<readonly string[]>([]);
  /** Le classement tient compte de la récence (affiché dans l'infobulle du score). */
  readonly recent = input(true);
  readonly openDoc = output<string>();

  protected readonly active = signal(0);
  protected readonly pageUrl = pageUrl;
  protected readonly courseSym = courseSym;
  protected readonly courseDomain = courseDomain;
  protected readonly cleanTitle = cleanTitle;

  protected readonly views = computed<CardView[]>(() => {
    const r = this.result();
    const terms = this.terms();
    const views: CardView[] = [];
    if (r.pdf) views.push({ label: 'Page d’origine', hint: 'La page du PDF, exactement comme dans le document', html: '' });
    views.push({ label: 'Texte', hint: 'Texte extrait du document, mots cherchés surlignés', html: renderBlocks(r.blocks, terms) });
    if (r.alt)
      views.push({
        label: 'Formules mises en forme',
        hint: 'Formules reconstruites à partir du texte extrait : peut se tromper',
        html: renderBlocks(r.alt, terms),
      });
    return views;
  });

  protected readonly pages = computed(() => {
    const pdf = this.result().pdf;
    return pdf ? { shown: pdf.pages.slice(0, 3), rest: pdf.pages.slice(3), doc: pdf.doc } : null;
  });

  protected readonly percent = computed(() => Math.round(Math.min(1, this.result().score ?? 0) * 100));
  protected readonly tip = computed(
    () =>
      ((this.result().score ?? 0) >= 1 ? 'Référence exacte (1 + cosinus des autres mots)' : 'Similarité cosinus') +
      (this.recent() ? ' × bonus de récence' : ''),
  );

  /** Ancienne correction : on nomme l'exercice comme dans la feuille 2025-2026. */
  protected readonly sectionTitle = computed(() => {
    const r = this.result();
    const title = cleanTitle(r.section || r.label);
    if (!r.current) return title;
    return (
      `TD${r.current.td} 2025-2026, exercice ${r.current.exercise}${r.current.partial ? ' (corrigé en partie)' : ''}` +
      ` — ${title.toLowerCase()} de l’ancienne correction`
    );
  });
}
