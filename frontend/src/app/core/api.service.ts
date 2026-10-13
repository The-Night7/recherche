import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { DocResponse, Meta, SearchResponse, Tree } from './models';

/**
 * Seul point d'accès au backend. Les URL sont relatives (`/api/...`) :
 * en développement le proxy d'`ng serve` les relaie (proxy.conf.json),
 * en production nginx le fait (nginx.conf).
 */
@Injectable({ providedIn: 'root' })
export class ApiService {
  private readonly http = inject(HttpClient);

  meta(): Observable<Meta> {
    return this.http.get<Meta>('/api/meta');
  }

  tree(): Observable<Tree> {
    return this.http.get<Tree>('/api/tree');
  }

  doc(key: string): Observable<DocResponse> {
    return this.http.get<DocResponse>('/api/doc', { params: { key } });
  }

  search(params: HttpParams): Observable<SearchResponse> {
    return this.http.get<SearchResponse>('/api/search', { params });
  }
}

/** URL d'image de page PDF (servie par le backend, mise en cache côté serveur). */
export const pageUrl = (doc: string, n: number): string =>
  `/api/page?doc=${encodeURIComponent(doc)}&n=${n}`;
