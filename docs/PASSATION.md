# Passation

Ce qu'il faut savoir pour reprendre le projet. Le détail technique est dans
[ARCHITECTURE.md](ARCHITECTURE.md) ; le déploiement dans [DEPLOYMENT.md](DEPLOYMENT.md).

## Où tourne le site

- **Render**, un service web Python natif (pas Docker), dépôt `The-Night7/recherche`,
  branche `main`, déploiement automatique à chaque fusion sur `main`.
- **Root Directory** : vide. **Build Command** :
  `pip install -r backend/requirements.txt && cd frontend && npm ci && npm run build`.
  **Start Command** : `cd backend && python3 server.py`.
- Node.js est fourni par l'image Python de Render (v24 au dernier déploiement) : c'est ce qui permet de compiler Angular pendant le build.
- Sonde : `/api/health`. Après une période d'inactivité (offre gratuite), le premier
  chargement prend environ une minute.
- Le `Dockerfile` racine, `render.yaml` et `docker-compose.yml` sont prêts mais
  **n'ont jamais été exécutés** : à valider (`docker compose up --build`) avant de s'y fier.

## Tâches courantes

| Je veux… | Je fais |
| --- | --- |
| Lancer en local | `cd backend && python3 server.py` et `cd frontend && npm install && npm start` (http://localhost:4200) |
| Ajouter des documents | `cd backend && python3 ingest.py add <dossier>`, commit de `data/`, `chunks.json`, `index.npz`, fusion sur `main` |
| Ajouter une matière | l'enregistrer dans `backend/courses.py` (symbole et exemples dans `frontend/src/app/core/course-meta.ts`) |
| Changer l'API | modifier `backend/server.py` **et** `frontend/src/app/core/models.ts` (types recopiés à la main) |
| Lancer les tests | `cd backend && python3 -m unittest discover -s tests` ; `cd frontend && npm test` |
| Déployer | fusionner sur `main` ; Render redéploie |

`npm test` utilise Chrome en mode headless ; si Chrome n'est pas dans le `PATH`, définir
`CHROME_BIN`. En conteneur root, le lanceur `ChromeHeadlessCI` (`karma.conf.js`) ajoute
`--no-sandbox`.

## Points de vigilance

- **Les PDF d'origine ne sont pas dans le dépôt** (`.gitignore`). Sans eux, les onglets
  « Page d'origine » et les images de formules n'apparaissent pas. Sur Render,
  `pdftoppm` n'est de toute façon pas installé.
- **`chunks.json` (32 Mo) et `index.npz` sont versionnés** : chaque réimport alourdit
  l'historique git. Pas de solution en place (Git LFS ou génération au build à étudier).
- **Après un import, il faut redémarrer le serveur** : l'index est chargé une fois.
- **Pas de test de bout en bout** : après un changement important, vérifier à la main
  l'accueil, une recherche avec formules, l'ouverture d'un document et la fenêtre « Fichiers ».
- **`models.ts` et `server.py` peuvent diverger** sans qu'aucun test ne le détecte.
- **Historique git** : le premier commit de la branche a été réécrit (identité) ;
  les fusions sur `main` se font par pull request.
- Le code de réseau de neurones (`model.py`, `train.py`, `chat.py`, `generate.py`,
  `vocab.py`) n'est pas utilisé par le site.

## Ce qui n'est pas fait

- Docker / docker compose non testés.
- Aucune intégration continue : rien n'exécute les tests à chaque push.
- Aucune authentification ni limitation de débit sur l'API.
- Pas de surveillance du service au-delà de la sonde `/api/health`.
