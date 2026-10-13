import { ChangeDetectionStrategy, Component, HostListener, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FiltersStore } from './core/filters.store';
import { SearchStore } from './core/search.store';
import { ThemeService } from './core/theme.service';
import { FileBrowser } from './features/browser/file-browser';
import { FiltersPanel } from './features/filters/filters-panel';
import { Results } from './features/results/results';

/** Coque de l'application : en-tête (recherche, fichiers, thème) + filtres + résultats. */
@Component({
  selector: 'app-root',
  imports: [FormsModule, FiltersPanel, Results, FileBrowser],
  templateUrl: './app.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class App {
  protected readonly filters = inject(FiltersStore);
  protected readonly search = inject(SearchStore);
  private readonly theme = inject(ThemeService);

  constructor() {
    this.search.init();
  }

  protected toggleTheme(): void {
    this.theme.toggle();
  }

  /** Raccourcis : « / » met le focus sur la recherche, « b » ouvre les fichiers. */
  @HostListener('document:keydown', ['$event'])
  protected onKey(e: KeyboardEvent): void {
    const target = e.target as HTMLElement | null;
    if (target?.closest?.('input, textarea') || this.search.browserOpen()) return;
    if (e.key === '/') {
      e.preventDefault();
      const input = document.getElementById('q') as HTMLInputElement | null;
      input?.focus();
      input?.select();
    } else if (e.key === 'b' && this.filters.meta() && !e.ctrlKey && !e.metaKey && !e.altKey) {
      e.preventDefault();
      this.search.browserOpen.set(true);
    }
  }
}
