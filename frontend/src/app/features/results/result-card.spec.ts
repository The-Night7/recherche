import { provideZonelessChangeDetection } from '@angular/core';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SearchResult } from '../../core/models';
import { ResultCard } from './result-card';

const base: SearchResult = {
  course: 'informatique3', course_name: 'Informatique 3', doc_label: 'TD2', section: 'Exercice 1', label: 'TD2',
  score: 1, curriculum_label: 'Préing 2 — semestre 1', curriculum: 'preing-2-s1', study_year: 2, semester: 1,
  program: 'preing', track: null, kind: 'td', corrige: false, year: 2024, with_correction: false, doc_key: 'k',
  blocks: [{ type: 'text', text: 'int n = 2;\n    p->next = NULL;\n#include <stdio.h>\n$x$' }],
  alt: null, videos: [], pdf: null,
};

describe('ResultCard', () => {
  let fixture: ComponentFixture<ResultCard>;

  beforeEach(() => TestBed.configureTestingModule({ providers: [provideZonelessChangeDetection()] }));

  const show = (result: SearchResult, terms: string[] = []) => {
    fixture = TestBed.createComponent(ResultCard);
    fixture.componentRef.setInput('result', result);
    fixture.componentRef.setInput('terms', terms);
    fixture.detectChanges();
    return fixture.nativeElement as HTMLElement;
  };

  it('keeps computer-science excerpts as code, without interpreting math or HTML', () => {
    const el = show(base, ['int']);
    const pre = el.querySelector('pre.text-excerpt') as HTMLPreElement;
    expect(pre.textContent).toBe('int n = 2;\n    p->next = NULL;\n#include <stdio.h>\n$x$');
    expect(el.querySelector('.math-block, mark, stdio')).toBeNull();
    expect(el.querySelector('.context-tag')?.textContent).toBe('Préing 2 — semestre 1');
  });

  it('shows tabs only when a passage has several views', () => {
    expect(show(base).querySelector('.view-tabs')).toBeNull();
    const el = show({ ...base, alt: [{ type: 'md', text: 'Formules' }] });
    const tabs = el.querySelectorAll<HTMLButtonElement>('.view-tab');
    expect(tabs.length).toBe(2);
    tabs[1].click();
    fixture.detectChanges();
    const bodies = el.querySelectorAll<HTMLElement>('.card-body');
    expect(bodies[0].hidden).toBeTrue();
    expect(bodies[1].hidden).toBeFalse();
  });

  it('links a video directly, or to a YouTube search when none matches the notion', () => {
    const el = show({
      ...base,
      videos: [
        { notion: 'Normes', url: 'https://www.youtube.com/watch?v=abc', title: 'Les normes', channel: 'Maths Adultes' },
        { notion: 'Arbres', url: 'https://www.youtube.com/results?search_query=arbres', title: null, channel: null },
      ],
    });
    const links = el.querySelectorAll<HTMLAnchorElement>('.video-link');
    expect(links[0].textContent).toContain('Les normes');
    expect(links[0].classList.contains('search')).toBeFalse();
    expect(links[1].classList.contains('search')).toBeTrue();
    expect(links[1].textContent).toContain('(recherche)');
  });
});
