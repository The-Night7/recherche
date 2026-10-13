import { Pipe, PipeTransform, inject } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

/**
 * Marque une chaîne comme HTML fiable.
 *
 * À n'utiliser que sur la sortie de `markdown.ts`, qui échappe tout texte source : le
 * sanitizer d'Angular supprimerait sinon les attributs `style`, `loading`, etc. dont le
 * rendu a besoin (images recadrées, liens externes).
 */
@Pipe({ name: 'trustedHtml' })
export class TrustedHtmlPipe implements PipeTransform {
  private readonly sanitizer = inject(DomSanitizer);

  transform(html: string): SafeHtml {
    return this.sanitizer.bypassSecurityTrustHtml(html);
  }
}
