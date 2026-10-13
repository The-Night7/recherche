# Backend — API de recherche

Serveur Python (bibliothèque standard + NumPy) qui charge l'index TF-IDF au démarrage
et répond aux routes `/api/*`. Détails : [`docs/ARCHITECTURE.md`](../docs/ARCHITECTURE.md).
Toutes les commandes se lancent depuis ce dossier.

```bash
pip install -r requirements.txt
python3 server.py                                  # http://localhost:8000
python3 search.py "règle d'Alembert" --cours series  # recherche en ligne de commande
python3 ingest.py add /chemin/vers/documents       # importer des documents (reconstruit l'index)
python3 -m unittest discover -s tests              # tests
```

Variables d'environnement : `PORT`, `HOST`, `WEB_DIR` (`none` désactive le service des
fichiers statiques), `CORS_ORIGIN`. Contenu des dossiers et formats : voir le
[README du dépôt](../README.md) (sections « Ajouter des documents » et « Utilisation »).
