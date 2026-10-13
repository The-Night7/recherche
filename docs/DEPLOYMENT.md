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

Symptôme d'un backend lancé sans le build du front : `/api/*` répond, mais `/` renvoie
une page 404 vide.

## Hébergeur

Le backend est un **processus Python qui reste actif** : il charge un index d'environ
40 Mo en mémoire au démarrage et appelle `pdftoppm` (outil système) pour afficher des
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

### Vercel pour le front

Si le front passe sur Vercel : *Framework Preset* Angular, dossier racine `frontend`,
sortie `dist/tuteur/browser`. Ajouter dans `frontend/vercel.json` une réécriture
`/api/:path*` vers l'URL publique du backend, ce qui évite le CORS ; sinon définir
`CORS_ORIGIN` côté backend et préfixer les appels dans `ApiService`.
