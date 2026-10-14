# Déploiement

## Docker compose (recommandé)

```bash
docker compose up --build        # http://localhost:8080
docker compose logs -f backend   # le chargement de l'index prend quelques secondes
```

Seul `frontend` (nginx, port 8080) est exposé ; il relaie `/api/` vers `backend`.
Le backend a une sonde de santé (`/api/health`).

## Un seul service (Render)

Le `Dockerfile` à la racine construit l'application Angular puis lance le backend, qui
sert l'API **et** l'interface sur le même port (`PORT`, fixé par Render). C'est la
configuration la plus simple : une seule URL, pas de CORS, pas de nginx.

Sur Render : *New → Blueprint* (lit `render.yaml`), ou dans le service existant,
*Settings* : **Runtime** `Docker`, **Root Directory** vide, **Dockerfile Path** `./Dockerfile`,
**Branch** `poc-pro` (ou `main` après fusion), **Health Check Path** `/api/health`.
Un service configuré avant la réorganisation (racine du dépôt, `python3 server.py`,
`pip install -r requirements.txt`) ne fonctionne plus : ces fichiers sont dans `backend/`.

### Service Render en runtime Python (sans Docker)

Un service existant en runtime **Python** ne peut pas passer en Docker : il faut en créer
un nouveau (Blueprint) ou rester en Python en compilant le front dans la commande de build.
Réglages, **Root Directory vide** (le build lit `frontend/` et `backend/`) :

- **Build Command** : `pip install -r backend/requirements.txt && cd frontend && npm ci && npm run build`
- **Start Command** : `cd backend && python3 server.py`

Ce mode est **vérifié en production** (octobre 2026) : l'image Python de Render fournit
Node.js (version 24 au moment du test), donc `npm ci` et `ng build` s'exécutent pendant le
build. Il n'installe pas `pdftoppm` : les pages PDF d'origine ne s'affichent pas (sans effet
si les PDF ne sont pas dans le dépôt).

Symptôme d'un backend lancé sans le build du front : `/api/*` répond, mais `/` renvoie
une page 404 vide.

## Hébergeur

Le backend est un **processus Python qui reste actif** : il charge en mémoire, au démarrage,
environ 37 Mo de fichiers d'index (`chunks.json`, `index.npz`, `vocab.json`) et appelle `pdftoppm` (outil système) pour afficher des
pages de PDF. Il lui faut donc un hébergeur de conteneurs ou de processus longs.

| Option | Backend | Frontend | Commentaire |
| --- | --- | --- | --- |
| **Render, deux services Docker** | Web Service, racine `backend/` | Web Service, racine `frontend/` | Cohérent avec l'existant ; le front doit joindre le backend (voir ci-dessous) |
| **Un VPS + `docker compose`** | conteneur | conteneur | Le plus proche du développement local ; tout est dans `docker-compose.yml` |
| Vercel (front) + Render (back) | Render | Vercel | CDN et prévisualisations pour le front ; configurer `CORS_ORIGIN` ou une réécriture `/api` |
| Vercel seul | non adapté | — | Fonctions serverless : index rechargé à froid, pas de `pdftoppm` |

### Render : deux services

- **Backend** : *Root Directory* `backend`, runtime Docker. Variables : `WEB_DIR=none`
  (et `CORS_ORIGIN=https://<url du front>` si le front est sur un autre domaine).
- **Frontend** : *Root Directory* `frontend`, runtime Docker. Le `nginx.conf` de l'image
  pointe sur `http://backend:8000`, nom valable **dans docker compose uniquement**.
  Sur Render, remplacer cette cible par l'URL interne du service backend
  (par exemple via un `nginx.conf` dédié ou une variable injectée au démarrage).

### Vercel pour le front (backend sur Render)

Vercel détecte deux dossiers dans le dépôt (`frontend`, `backend`) : **n'importer que
`frontend`**. Le backend reste sur Render (processus long, index en mémoire : voir le
tableau ci-dessus).

- *Root Directory* : `frontend` ; le reste est lu dans `frontend/vercel.json`
  (installation, build, sortie `dist/tuteur/browser`).
- `frontend/vercel.json` réécrit `/api/*` vers `https://recherche-du60.onrender.com/api/*` :
  le navigateur ne parle qu'à Vercel, donc **pas de CORS** et aucune variable à définir.
  Si l'URL du backend change, modifier cette ligne.
- Le premier appel après une période d'inactivité réveille le service Render (offre
  gratuite) et peut durer environ une minute : l'interface affiche « Recherche… » pendant ce temps.
- Render continue de servir aussi sa propre copie de l'interface ; elle peut être ignorée.
