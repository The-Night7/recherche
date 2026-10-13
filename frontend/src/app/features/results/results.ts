import { ChangeDetectionStrategy, Component, computed, inject } from '@angular/core';
import { courseExamples } from '../../core/course-meta';
import { FiltersStore } from '../../core/filters.store';
import { DocInfo } from '../../core/models';
import { SearchStore } from '../../core/search.store';
import { TrustedHtmlPipe } from '../../shared/html.pipe';
import { cleanTitle, yearLabel } from '../../shared/text';
import { DocItem } from './doc-item';
import { ResultCard } from './result-card';

/** Zone principale : accueil, résultats de recherche, ou document ouvert en entier. */
@Component({
  selector: 'app-results',
  imports: [ResultCard, DocItem, TrustedHtmlPipe],
  templateUrl: './results.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Results {
  protected readonly store = inject(SearchStore);
  protected readonly filters = inject(FiltersStore);
  protected readonly cleanTitle = cleanTitle;
  protected readonly yearLabel = yearLabel;

  protected readonly view = this.store.view;

  protected readonly welcomeTitle = computed(() => {
    const courses = this.filters.coursesInScope();
    return courses.length === 1 ? courses[0].curriculum_label : this.filters.scopeLabel();
  });

  protected readonly examples = computed(() => {
    const f = this.filters.filters();
    return f.course === 'all'
      ? [...new Set(this.filters.coursesInScope().map((c) => courseExamples(c.id)[0]).filter(Boolean))].slice(0, 8)
      : courseExamples(f.course);
  });

  /** Documents de la sélection (barre de recherche vide), regroupés par matière ou par type. */
  protected readonly filteredDocs = computed(() => {
    const tree = this.store.tree();
    const meta = this.filters.meta();
    if (!tree || !meta) return null;
    const groups = this.filters
      .coursesInScope()
      .filter((c) => tree[c.id])
      .map((c) => ({ course: c, docs: tree[c.id].filter((d) => this.filters.docMatches(d)) }))
      .filter((g) => g.docs.length);
    const total = groups.reduce((s, g) => s + g.docs.length, 0);
    const single = this.filters.filters().course !== 'all';
    const kindOrder = Object.keys(meta.kinds);
    const byKind: { kind: string; label: string; docs: DocInfo[] }[] = [];
    if (single && groups.length) {
      const map = new Map<string, DocInfo[]>();
      groups[0].docs.forEach((d) => map.set(d.kind, [...(map.get(d.kind) ?? []), d]));
      [...map.keys()]
        .sort((a, b) => kindOrder.indexOf(a) - kindOrder.indexOf(b))
        .forEach((kind) => byKind.push({ kind, label: meta.kinds[kind] || kind, docs: map.get(kind)! }));
    }
    return { total, single, groups, byKind, open: groups.length <= 3 };
  });

  /** Navigation précédent / suivant dans la matière du document ouvert. */
  protected docNav(key: string) {
    const course = this.store.courseOf(key) ?? '';
    const docs = this.store.docsOf(course);
    const i = docs.findIndex((d) => d.key === key);
    const meta = this.filters.meta();
    const doc = docs[i];
    const kindLabel = doc ? meta?.kinds[doc.kind] || doc.kind : '';
    const year = doc && !(doc.year == null || /\d{4}-\d{4}/.test(doc.label)) ? yearLabel(doc.year) : '';
    return {
      title: cleanTitle(doc?.label || key),
      course: meta?.courses.find((c) => c.id === course)?.name || course,
      kind: kindLabel,
      year,
      position: i + 1,
      total: docs.length,
      prev: docs[i - 1] as DocInfo | undefined,
      next: docs[i + 1] as DocInfo | undefined,
    };
  }
}
