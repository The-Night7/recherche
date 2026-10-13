import { provideZonelessChangeDetection } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { FiltersStore } from './filters.store';
import { CourseMeta, Meta } from './models';

const course = (id: string, semester: number, extra: Partial<CourseMeta> = {}): CourseMeta => ({
  id, name: id, curriculum: `preing-1-s${semester}`, curriculum_label: `Préing 1 — S${semester}`, program: 'preing',
  track: null, study_year: 1, semester, count: 10, kinds: { td: 5 }, years: [2024, null], ...extra,
});

const meta: Meta = {
  courses: [course('algebre1', 1), course('algebre2', 2, { kinds: { cm: 3 } })],
  kinds: { cm: 'CM', td: 'TD' },
  programs: { preing: 'Préing' },
  curricula: [
    { id: 'preing-1-s1', program: 'preing', track: null, study_year: 1, semester: 1, label: 'Préing 1 — S1', count: 10 },
    { id: 'preing-1-s2', program: 'preing', track: null, study_year: 1, semester: 2, label: 'Préing 1 — S2', count: 10 },
  ],
};

describe('FiltersStore', () => {
  let store: FiltersStore;

  beforeEach(() => {
    localStorage.clear();
    TestBed.configureTestingModule({ providers: [provideZonelessChangeDetection()] });
    store = TestBed.inject(FiltersStore);
    store.setMeta(meta);
  });

  it('lists every course when nothing is filtered', () => {
    expect(store.availableCourses().map((c) => c.id)).toEqual(['algebre1', 'algebre2']);
  });

  it('narrows courses to the chosen semester', () => {
    store.patch({ semester: '2' });
    expect(store.availableCourses().map((c) => c.id)).toEqual(['algebre2']);
  });

  it('resets a course that falls outside the new semester', () => {
    store.patch({ course: 'algebre1' });
    store.patch({ semester: '2' });
    expect(store.filters().course).toBe('all');
  });

  it('drops document types absent from the selection', () => {
    store.patch({ kinds: ['td', 'cm'] });
    store.patch({ course: 'algebre2' });
    expect(store.filters().kinds).toEqual(['cm']);
  });

  it('applies the same version rules as the backend to documents', () => {
    store.patch({ versions: ['corrige'] });
    expect(store.docMatches({ kind: 'td', corrige: true, with_correction: false, year: 2024 })).toBeTrue();
    expect(store.docMatches({ kind: 'td', corrige: false, with_correction: false, year: 2024 })).toBeFalse();
    expect(store.docMatches({ kind: 'td', corrige: false, with_correction: true, year: 2024 })).toBeTrue();
  });

  it('persists filters in localStorage', () => {
    store.patch({ k: 10 });
    expect(JSON.parse(localStorage.getItem('tuteur-filtres')!).k).toBe(10);
  });
});
