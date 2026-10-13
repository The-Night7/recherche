import { Injectable, computed, signal } from '@angular/core';
import { CourseMeta, Curriculum, Filters, Meta } from './models';

const STORAGE_KEY = 'tuteur-filtres';

export const defaultFilters = (): Filters => ({
  program: 'all', study_year: 'all', semester: 'all', track: 'all', course: 'all',
  kinds: [], versions: [], years: [], k: 5, recent: true,
});

const semesterKey = (v: number | null): string => String(v ?? 'none');

/**
 * État des filtres (cycle, année, semestre, parcours, matière, types…) et tout ce qui
 * s'en déduit. Le résultat de chaque modification est « normalisé » : un filtre devenu
 * incohérent avec les autres (une matière hors du semestre choisi, par exemple) est
 * remis à « tous ». L'état est mémorisé dans localStorage.
 */
@Injectable({ providedIn: 'root' })
export class FiltersStore {
  readonly meta = signal<Meta | null>(null);
  readonly filters = signal<Filters>(this.restore());

  /** Matières visibles avec les filtres cycle / année / semestre / parcours. */
  readonly availableCourses = computed<CourseMeta[]>(() => {
    const meta = this.meta();
    return meta ? this.coursesFor(meta, this.filters()) : [];
  });

  /** Matière(s) réellement interrogée(s) : la matière choisie, ou toutes les visibles. */
  readonly coursesInScope = computed<CourseMeta[]>(() => {
    const course = this.filters().course;
    return this.availableCourses().filter((c) => course === 'all' || c.id === course);
  });

  readonly contextChoices = computed<Curriculum[]>(() => {
    const meta = this.meta();
    return meta ? this.contextFor(meta, this.filters()) : [];
  });

  readonly availableTracks = computed<string[]>(() => {
    const meta = this.meta();
    return meta ? this.tracksFor(meta, this.filters()) : [];
  });

  readonly semesterOptions = computed<[string, string][]>(() =>
    [...new Set(this.contextChoices().map((c) => semesterKey(c.semester)))]
      .sort()
      .map((value) => [value, value === 'none' ? 'Hors semestre' : `Semestre ${value}`]),
  );

  /** Années scolaires de la sélection, la plus récente d'abord (`null` = sans date). */
  readonly yearsInScope = computed<(number | null)[]>(() =>
    [...new Set(this.coursesInScope().flatMap((c) => c.years))].sort((a, b) => (b ?? 0) - (a ?? 0)),
  );

  readonly chosenCourse = computed(() => this.meta()?.courses.find((c) => c.id === this.filters().course));

  readonly scopeLabel = computed<string>(() => {
    const meta = this.meta();
    const f = this.filters();
    if (!meta) return '';
    const chosen = this.chosenCourse();
    if (chosen) return chosen.curriculum_label;
    const programs = [...new Set(this.availableCourses().map((c) => c.program))];
    const year = programs
      .map((p) => meta.programs[p] + (f.study_year === 'all' ? '' : ` ${f.study_year}`))
      .join(' et ');
    const semester =
      f.semester === 'all' ? 'tous les semestres' : f.semester === 'none' ? 'hors semestre' : `semestre ${f.semester}`;
    return `${year || 'Tous les cycles'} — ${semester}${f.track === 'all' ? '' : ` — ${f.track.toUpperCase()}`}`;
  });

  /** Résumé d'une ligne affiché sur mobile quand le panneau est replié. */
  readonly scopeSummary = computed<string>(() => {
    const meta = this.meta();
    const f = this.filters();
    if (!meta) return 'toutes les matières';
    const chosen = this.chosenCourse();
    const parts = [chosen?.curriculum_label || this.scopeLabel(), chosen?.name || 'toutes les matières'];
    if (f.kinds.length) parts.push(f.kinds.map((k) => meta.kinds[k]).join('+'));
    if (f.versions.length === 1) parts.push(f.versions[0] === 'corrige' ? 'corrigés' : 'énoncés');
    if (f.years.length) parts.push(f.years.length + ' année(s) scolaire(s)');
    return parts.join(', ');
  });

  /** Appelé une fois, quand `/api/meta` est arrivé. */
  setMeta(meta: Meta): void {
    this.meta.set(meta);
    this.filters.update((f) => this.normalize(f));
    this.persist();
  }

  /** Modifie des filtres, remet l'ensemble en cohérence et mémorise. */
  patch(change: Partial<Filters>): void {
    this.filters.update((f) => this.normalize({ ...f, ...change }));
    this.persist();
  }

  reset(): void {
    this.filters.set(defaultFilters());
    this.persist();
  }

  toggleIn(field: 'kinds' | 'versions' | 'years', value: string): void {
    const list = this.filters()[field];
    this.patch({ [field]: list.includes(value) ? list.filter((v) => v !== value) : [...list, value] });
  }

  /** Mêmes règles que `filter_mask` (backend/search.py), appliquées aux documents. */
  docMatches(d: { kind: string; corrige: boolean; with_correction: boolean; year: number | null }): boolean {
    const f = this.filters();
    const versions = d.with_correction ? ['enonce', 'corrige'] : [d.corrige ? 'corrige' : 'enonce'];
    return (
      (!f.kinds.length || f.kinds.includes(d.kind)) &&
      (!f.versions.length || versions.some((v) => f.versions.includes(v))) &&
      (!f.years.length || f.years.includes(String(d.year ?? 'none')))
    );
  }

  /** Retire les valeurs qui ne correspondent plus à rien dans les données. */
  private normalize(input: Filters): Filters {
    const meta = this.meta();
    if (!meta) return input;
    const f = { ...input };
    const scoped = (g: Filters) => this.coursesFor(meta, g);
    if (f.program !== 'all' && !meta.programs[f.program]) f.program = 'all';
    if (!['all', '1', '2'].includes(f.study_year)) f.study_year = 'all';
    if (!this.contextFor(meta, f).some((c) => semesterKey(c.semester) === f.semester)) f.semester = 'all';
    if (!this.tracksFor(meta, f).includes(f.track)) f.track = 'all';
    if (!scoped(f).some((c) => c.id === f.course)) f.course = 'all';
    const courses = scoped(f).filter((c) => f.course === 'all' || c.id === f.course);
    f.kinds = f.kinds.filter((k) => courses.some((c) => c.kinds[k]));
    f.years = f.years.filter((y) => courses.some((c) => c.years.some((v) => String(v ?? 'none') === y)));
    return f;
  }

  private coursesFor(meta: Meta, f: Filters): CourseMeta[] {
    return meta.courses.filter(
      (c) =>
        (f.program === 'all' || c.program === f.program) &&
        (f.study_year === 'all' || String(c.study_year) === f.study_year) &&
        (f.semester === 'all' || semesterKey(c.semester) === f.semester) &&
        (f.track === 'all' || c.track === f.track),
    );
  }

  private contextFor(meta: Meta, f: Filters): Curriculum[] {
    return meta.curricula.filter(
      (c) =>
        c.count > 0 &&
        (f.program === 'all' || c.program === f.program) &&
        (f.study_year === 'all' || String(c.study_year) === f.study_year),
    );
  }

  private tracksFor(meta: Meta, f: Filters): string[] {
    return [
      ...new Set(
        this.contextFor(meta, f)
          .filter((c) => f.semester === 'all' || semesterKey(c.semester) === f.semester)
          .map((c) => c.track)
          .filter((t): t is string => !!t),
      ),
    ];
  }

  private restore(): Filters {
    const f = defaultFilters();
    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}') as Partial<Filters>;
      Object.assign(f, saved);
      if (!('program' in saved) && f.study_year !== 'all') f.program = 'preing';
    } catch {
      /* stockage absent ou illisible : filtres par défaut */
    }
    return f;
  }

  private persist(): void {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.filters()));
    } catch {
      /* ignoré */
    }
  }
}
