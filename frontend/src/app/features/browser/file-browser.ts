import {
  ChangeDetectionStrategy, Component, ElementRef, Injector, afterNextRender, computed, effect, inject, signal, viewChild,
} from '@angular/core';
import { courseDomain, courseSym } from '../../core/course-meta';
import { FiltersStore } from '../../core/filters.store';
import { DocInfo } from '../../core/models';
import { SERVER_DOWN, SearchStore } from '../../core/search.store';
import { accentInsensitive, cleanTitle, yearLabel } from '../../shared/text';
import { DocItem } from '../results/doc-item';

interface DocGroup {
  title: string;
  docs: DocInfo[];
}

/** Fenêtre « Parcourir les fichiers » : une matière à gauche, ses documents à droite. */
@Component({
  selector: 'app-file-browser',
  imports: [DocItem],
  templateUrl: './file-browser.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FileBrowser {
  protected readonly filters = inject(FiltersStore);
  protected readonly search = inject(SearchStore);

  private readonly dialog = viewChild.required<ElementRef<HTMLDialogElement>>('dialog');
  private readonly filterInput = viewChild.required<ElementRef<HTMLInputElement>>('filterInput');

  protected readonly text = signal('');
  private readonly chosen = signal<string | null>(null);
  private readonly injector = inject(Injector);

  protected readonly courseSym = courseSym;
  protected readonly courseDomain = courseDomain;
  protected readonly symLength = (id: string): number => [...courseSym(id)].length;

  /** Matières de la sélection qui ont des documents, avec un titre à chaque changement de contexte. */
  protected readonly courses = computed(() => {
    const tree = this.search.tree();
    let group: string | null = null;
    return this.filters
      .availableCourses()
      .filter((c) => tree?.[c.id])
      .map((c) => {
        const heading = c.curriculum !== group ? c.curriculum_label : null;
        group = c.curriculum;
        return { id: c.id, name: c.name, heading, count: tree![c.id].length };
      });
  });

  /** Matière affichée : celle du document ouvert, sinon celle des filtres, sinon la précédente, sinon la première. */
  protected readonly current = computed<string | null>(() => {
    const open = this.search.openDoc();
    const ids = new Set(this.courses().map((c) => c.id));
    const wanted = [open && this.search.courseOf(open), this.filters.filters().course, this.chosen()];
    return wanted.find((id): id is string => !!id && ids.has(id)) ?? this.courses()[0]?.id ?? null;
  });

  protected readonly groups = computed<DocGroup[]>(() => {
    const tree = this.search.tree();
    const meta = this.filters.meta();
    const filter = this.text().trim();
    if (!tree || !meta) return [];
    const kindLabel = (k: string) => meta.kinds[k] || k;
    if (filter) {
      // filtre : dans toutes les matières de la sélection, mots dans n'importe quel ordre, sans accents
      const words = filter.split(/\s+/).map((w) => new RegExp(accentInsensitive(w), 'i'));
      return this.filters
        .availableCourses()
        .filter((c) => tree[c.id])
        .map((c) => ({
          title: c.name,
          docs: tree[c.id].filter((d) =>
            words.every((re) => re.test(`${cleanTitle(d.label)} ${kindLabel(d.kind)} ${yearLabel(d.year)}`)),
          ),
        }))
        .filter((g) => g.docs.length);
    }
    const course = this.current();
    if (!course) return [];
    const byKind: Record<string, DocInfo[]> = {};
    tree[course].forEach((d) => (byKind[d.kind] ||= []).push(d));
    return [
      ...Object.keys(meta.kinds).filter((k) => byKind[k]).map((k) => ({ title: kindLabel(k), docs: byKind[k] })),
      ...Object.keys(byKind).filter((k) => !meta.kinds[k]).map((k) => ({ title: k, docs: byKind[k] })),
    ];
  });

  constructor() {
    // Ouvre / ferme le <dialog> natif selon le signal partagé (bouton, raccourci « b », « ← Fichiers »).
    effect(() => {
      const wanted = this.search.browserOpen();
      const dialog = this.dialog().nativeElement;
      if (wanted && !dialog.open) {
        this.text.set('');
        // l'arbre des documents est chargé à la demande
        this.search.loadTree().subscribe({
          next: () => {
            dialog.showModal();
            this.filterInput().nativeElement.focus();
            afterNextRender(() => dialog.querySelector('#browser-courses [aria-pressed="true"]')?.scrollIntoView({ block: 'nearest' }), {
              injector: this.injector,
            });
          },
          error: () => {
            this.search.browserOpen.set(false);
            this.search.view.set({ kind: 'error', text: SERVER_DOWN });
          },
        });
      } else if (!wanted && dialog.open) dialog.close();
    });
  }

  protected choose(id: string): void {
    this.chosen.set(id);
    this.text.set('');
  }

  protected onBackdrop(e: MouseEvent): void {
    if (e.target === this.dialog().nativeElement) this.search.browserOpen.set(false);
  }

  protected firstDoc(): void {
    this.dialog().nativeElement.querySelector<HTMLButtonElement>('#browser-docs .doc-item')?.click();
  }
}
