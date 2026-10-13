import { DOCUMENT } from '@angular/common';
import { Injectable, inject } from '@angular/core';

const STORAGE_KEY = 'tuteur-theme';

/** Thème clair / sombre, mémorisé dans localStorage (attribut `data-theme` sur <html>). */
@Injectable({ providedIn: 'root' })
export class ThemeService {
  private readonly root = inject(DOCUMENT).documentElement;

  constructor() {
    let saved: string | null = null;
    try {
      saved = localStorage.getItem(STORAGE_KEY);
    } catch {
      /* stockage indisponible : on suit le thème du système */
    }
    this.root.dataset['theme'] = saved || this.systemTheme();
  }

  toggle(): void {
    const next = this.root.dataset['theme'] === 'dark' ? 'light' : 'dark';
    this.root.dataset['theme'] = next;
    try {
      localStorage.setItem(STORAGE_KEY, next);
    } catch {
      /* ignoré : le thème reste appliqué pour la session */
    }
  }

  private systemTheme(): string {
    return matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
}
