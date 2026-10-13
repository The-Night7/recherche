# Frontend — Angular

Interface de recherche dans les documents de cours. Angular 20, composants
*standalone*, signaux, sans zone.js, TypeScript strict. Architecture générale :
[`docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md).

## Commandes

```bash
npm install
npm start          # http://localhost:4200, /api relayé vers localhost:8000 (proxy.conf.json)
npm test           # Karma + Jasmine, Chrome headless (CHROME_BIN si Chrome n'est pas dans le PATH)
npm run build      # dist/tuteur/browser
```

Le backend doit tourner : `cd ../backend && python3 server.py`.

## Structure de `src/app/`

```
app.ts, app.html          coque : en-tête, recherche, raccourcis clavier (/ et b)
app.config.ts             providers (HttpClient, détection de changement sans zone)
core/                     logique et état, sans affichage
  models.ts               types de l'API (miroir de backend/server.py)
  api.service.ts          seul accès à /api/*
  filters.store.ts        filtres + valeurs dérivées + persistance
  search.store.ts         vue courante, recherche, ouverture d'un document
  theme.service.ts        thème clair / sombre
  course-meta.ts          symbole, domaine, exemples de chaque matière
features/
  filters/                panneau « Où chercher »
  results/                accueil, résultats, carte de passage, ligne de document
  browser/                dialogue « Parcourir les fichiers »
shared/
  markdown.ts             Markdown + LaTeX → HTML (fonctions pures)
  text.ts                 échappement, regex insensible aux accents
  katex.directive.ts      rendu des formules
  image-fallback.directive.ts, html.pipe.ts
```

## Conventions

- Les composants affichent et délèguent : l'état est dans les stores (`core/`).
- Un nouvel appel API passe par `ApiService` ; son type de réponse va dans `models.ts`.
- `innerHTML` n'est utilisé que pour la sortie de `markdown.ts` (via `trustedHtml`) :
  toute nouvelle fonction de rendu échappe ses entrées et a un test dans `markdown.spec.ts`.
- Pas de styles de composant : les styles sont dans `src/styles.css` (variables CSS,
  thème via `data-theme`).
