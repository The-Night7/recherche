import { Directive, ElementRef, OnDestroy, OnInit, inject } from '@angular/core';

/**
 * Remplace une image de carte qui ne charge pas par une note.
 * L'événement `error` ne remonte pas : on l'écoute en phase de capture sur le conteneur.
 */
@Directive({ selector: '[appImageFallback]' })
export class ImageFallbackDirective implements OnInit, OnDestroy {
  private readonly host = inject<ElementRef<HTMLElement>>(ElementRef).nativeElement;
  private readonly onError = (e: Event) => {
    const img = e.target;
    if (!(img instanceof HTMLImageElement) || !img.closest('.md-image, .pdf-page')) return;
    const note = document.createElement('p');
    note.className = 'image-missing';
    note.textContent = 'Image indisponible' + (img.alt ? ' (' + img.alt + ')' : '') + ' : ';
    const wrapper = img.closest('.md-image');
    if (wrapper) {
      const link = document.createElement('a');
      link.href = img.src;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.textContent = 'ouvrir le lien';
      note.appendChild(link);
    } else note.textContent = (note.textContent ?? '').replace(/ : $/, '.');
    (wrapper ?? img).replaceWith(note);
  };

  ngOnInit(): void {
    this.host.addEventListener('error', this.onError, true);
  }

  ngOnDestroy(): void {
    this.host.removeEventListener('error', this.onError, true);
  }
}
