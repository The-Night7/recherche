import { AfterViewChecked, Directive, ElementRef, inject } from '@angular/core';
import renderMathInElement from 'katex/contrib/auto-render';

/**
 * Rend les formules LaTeX ($…$, $$…$$, \(…\), \[…\]) du contenu de l'élément avec KaTeX.
 * Les formules déjà rendues (`.katex`) sont ignorées par KaTeX, donc l'appel répété est sans effet.
 */
@Directive({ selector: '[appKatex]' })
export class KatexDirective implements AfterViewChecked {
  private readonly host = inject<ElementRef<HTMLElement>>(ElementRef);

  ngAfterViewChecked(): void {
    renderMathInElement(this.host.nativeElement, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\(', right: '\\)', display: false },
      ],
      throwOnError: false,
    });
  }
}
