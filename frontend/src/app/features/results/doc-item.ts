import { ChangeDetectionStrategy, Component, computed, input, output } from '@angular/core';
import { DocInfo } from '../../core/models';
import { cleanTitle, yearLabel } from '../../shared/text';

/** Une ligne de liste de documents (exploration des fichiers et accueil). */
@Component({
  selector: 'app-doc-item',
  template: `<button type="button" class="doc-item" (click)="open.emit(doc().key)">
    <span class="doc-name">{{ title() }}</span><small>{{ details() }}</small></button>`,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DocItem {
  readonly doc = input.required<DocInfo>();
  readonly open = output<string>();

  protected readonly title = computed(() => cleanTitle(this.doc().label));
  protected readonly details = computed(() => {
    const d = this.doc();
    // l'année est souvent déjà dans le titre (« … · 2024-2025 ») : on ne la répète pas
    const year = d.year == null || /\d{4}-\d{4}/.test(d.label) ? '' : yearLabel(d.year);
    return [year, d.corrige && !/corrig/i.test(d.label) ? 'corrigé' : '', `${d.count} passage${d.count > 1 ? 's' : ''}`]
      .filter(Boolean)
      .join(' · ');
  });
}
