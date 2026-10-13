import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { provideZonelessChangeDetection } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { App } from './app';

describe('App', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideZonelessChangeDetection(), provideHttpClient(), provideHttpClientTesting()],
    });
  });

  it('shows a helpful message when the backend is unreachable', async () => {
    const fixture = TestBed.createComponent(App);
    TestBed.inject(HttpTestingController).expectOne('/api/meta').error(new ProgressEvent('error'));
    await fixture.whenStable();
    expect((fixture.nativeElement as HTMLElement).querySelector('#results .empty')?.textContent).toContain('Le serveur ne répond pas');
  });
});
