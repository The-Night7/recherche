import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { courseDomain, courseSym } from '../../core/course-meta';
import { FiltersStore } from '../../core/filters.store';
import { Filters } from '../../core/models';
import { SearchStore } from '../../core/search.store';
import { yearLabel } from '../../shared/text';

type Option = readonly [value: string, label: string];

/** Panneau « Où chercher » : chaque modification passe par le store puis relance la vue courante. */
@Component({
  selector: 'app-filters',
  templateUrl: './filters-panel.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FiltersPanel {
  protected readonly store = inject(FiltersStore);
  private readonly search = inject(SearchStore);

  /** Panneau déplié (mobile uniquement : sur grand écran il est toujours visible). */
  protected readonly open = signal(false);

  protected readonly courseSym = courseSym;
  protected readonly courseDomain = courseDomain;
  protected readonly yearLabel = yearLabel;
  protected readonly counts = [3, 5, 10];
  protected readonly versionOptions: Option[] = [['enonce', 'Énoncés'], ['corrige', 'Corrigés']];

  protected readonly programOptions = computed<Option[]>(() => [
    ['all', 'Tous'],
    ...Object.entries(this.store.meta()?.programs ?? {}),
  ]);
  protected readonly studyYearOptions: Option[] = [['all', 'Toutes'], ['1', 'Année 1'], ['2', 'Année 2']];
  protected readonly semesterOptions = computed<Option[]>(() => [['all', 'Tous'], ...this.store.semesterOptions()]);
  protected readonly trackOptions = computed<Option[]>(() => [
    ['all', 'Tous'],
    ...this.store.availableTracks().map((t): Option => [t, t.toUpperCase()]),
  ]);

  protected readonly kindOptions = computed(() => {
    const scope = this.store.coursesInScope();
    return Object.entries(this.store.meta()?.kinds ?? {}).map(([id, label]) => ({
      id,
      label,
      // un type absent de la sélection est grisé
      disabled: scope.reduce((n, c) => n + (c.kinds[id] || 0), 0) === 0,
    }));
  });

  /** Matières, avec un titre à chaque changement de contexte (cycle / année / semestre). */
  protected readonly courseEntries = computed(() => {
    const available = this.store.availableCourses();
    const total = available.reduce((s, c) => s + c.count, 0);
    let group: string | null = null;
    const entries = [{ id: 'all', name: 'Toutes les matières', count: total, heading: null as string | null }];
    for (const c of available) {
      let heading: string | null = null;
      if (c.curriculum && c.curriculum !== group) {
        group = c.curriculum;
        heading = c.curriculum_label;
      }
      entries.push({ id: c.id, name: c.name, count: c.count, heading });
    }
    return entries;
  });

  protected yearId = (y: number | null): string => (y === null ? 'none' : String(y));
  protected yearText = (y: number | null): string => (y === null ? 'sans date' : yearLabel(y));
  protected symLength = (id: string): number => (id === 'all' ? 1 : [...courseSym(id)].length);

  /** Applique un changement de filtre, puis rafraîchit la vue (résultats ou accueil). */
  protected change(change: Partial<Filters>): void {
    this.store.patch(change);
    this.search.refresh();
  }

  protected chooseCourse(id: string): void {
    this.change({ course: id, years: [] });
  }

  protected toggle(field: 'kinds' | 'versions' | 'years', value: string): void {
    this.store.toggleIn(field, value);
    this.search.refresh();
  }

  protected reset(): void {
    this.store.reset();
    this.search.refresh();
  }
}
