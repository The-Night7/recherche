import { HttpParams } from '@angular/common/http';
import { Injectable, inject, signal } from '@angular/core';
import { Observable, of, tap } from 'rxjs';
import { ApiService } from './api.service';
import { DocInfo, SearchResponse, SearchResult, Tree } from './models';
import { FiltersStore } from './filters.store';

/** Ce que la zone de résultats affiche (une seule vue à la fois). */
export type View =
  | { kind: 'loading'; text: string }
  | { kind: 'error'; text: string }
  | { kind: 'empty'; response: SearchResponse }
  | { kind: 'welcome' }
  | { kind: 'results'; response: SearchResponse }
  | { kind: 'doc'; key: string; results: SearchResult[] };

export const SERVER_DOWN =
  'Le serveur ne répond pas. Lance <b>python3 server.py</b> (ou <b>docker compose up</b>) puis recharge la page.';

/**
 * Orchestration de la recherche et de la navigation entre vues.
 *
 * `sequence` protège contre les réponses tardives : seule la dernière action lancée
 * a le droit d'écrire dans `view`.
 */
@Injectable({ providedIn: 'root' })
export class SearchStore {
  private readonly api = inject(ApiService);
  private readonly filters = inject(FiltersStore);

  readonly query = signal('');
  readonly view = signal<View>({ kind: 'loading', text: 'Chargement des cours…' });
  /** Arbre des documents (chargé à la demande, puis gardé). */
  readonly tree = signal<Tree | null>(null);
  readonly browserOpen = signal(false);
  /** Clé du document affiché en entier (sert à ouvrir l'explorateur sur sa matière). */
  readonly openDoc = signal<string | null>(null);

  private sequence = 0;

  /** Premier chargement : métadonnées puis page d'accueil. */
  init(): void {
    this.api.meta().subscribe({
      next: (meta) => {
        this.filters.setMeta(meta);
        this.showWelcome();
      },
      error: () => this.view.set({ kind: 'error', text: SERVER_DOWN }),
    });
  }

  /** À appeler après chaque changement de filtre. */
  refresh(): void {
    if (this.query().trim()) this.search();
    else this.showWelcome();
  }

  showWelcome(): void {
    ++this.sequence;
    this.openDoc.set(null);
    this.view.set({ kind: 'welcome' });
    this.loadTree().subscribe({ error: () => undefined }); // la liste des documents s'affiche dès qu'elle arrive
  }

  search(): void {
    const q = this.query().trim();
    if (!q) return;
    this.openDoc.set(null);
    const sequence = ++this.sequence;
    this.view.set({ kind: 'loading', text: 'Recherche…' });
    this.api.search(this.searchParams(q)).subscribe({
      next: (data) => {
        if (sequence !== this.sequence) return;
        if (!data.tokens.length || !data.results.length) this.view.set({ kind: 'empty', response: data });
        else this.view.set({ kind: 'results', response: data });
      },
      error: () => {
        if (sequence === this.sequence) this.view.set({ kind: 'error', text: SERVER_DOWN });
      },
    });
  }

  showDoc(key: string): void {
    const sequence = ++this.sequence;
    this.browserOpen.set(false);
    this.view.set({ kind: 'loading', text: 'Ouverture du document…' });
    this.loadTree().subscribe({
      next: () =>
        this.api.doc(key).subscribe({
          next: (data) => {
            if (sequence !== this.sequence) return;
            this.openDoc.set(key);
            this.view.set({ kind: 'doc', key, results: data.results });
            window.scrollTo({ top: 0 });
          },
          error: () => this.docError(sequence),
        }),
      error: () => this.docError(sequence),
    });
  }

  /** Charge l'arbre des documents une seule fois, puis le ressert depuis la mémoire. */
  loadTree(): Observable<Tree> {
    const known = this.tree();
    return known ? of(known) : this.api.tree().pipe(tap((t) => this.tree.set(t)));
  }

  /** Cours dont fait partie un document. */
  courseOf(key: string): string | undefined {
    const tree = this.tree();
    return tree ? Object.keys(tree).find((c) => tree[c].some((d) => d.key === key)) : undefined;
  }

  docsOf(course: string): DocInfo[] {
    return this.tree()?.[course] ?? [];
  }

  private docError(sequence: number): void {
    if (sequence === this.sequence)
      this.view.set({
        kind: 'error',
        text: 'Impossible d’ouvrir ce document. Vérifie que <b>le serveur</b> tourne.',
      });
  }

  private searchParams(q: string): HttpParams {
    const f = this.filters.filters();
    let p = new HttpParams().set('q', q).set('k', f.k).set('recent', f.recent ? 1 : 0);
    const set = (name: string, value: string) => {
      if (value !== 'all') p = p.set(name, value);
    };
    set('course', f.course);
    set('program', f.program);
    set('track', f.track);
    set('study_year', f.study_year);
    set('semester', f.semester);
    if (f.kinds.length) p = p.set('kinds', f.kinds.join(','));
    if (f.versions.length) p = p.set('versions', f.versions.join(','));
    if (f.years.length) p = p.set('years', f.years.join(','));
    return p;
  }
}
