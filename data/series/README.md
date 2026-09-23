# Cours de Séries — textes sources

- `*.txt` : texte extrait des PDF par `python3 ingest_series.py extract <fichiers>`
  (pages séparées par `<<<PAGE>>>`).
- `*.md` : notes déjà en Markdown + LaTeX (`$...$`, `$$...$$`), rendues avec KaTeX
  dans l'interface.
- `transcriptions/<nom du PDF>.md` : transcription d'un PDF scanné (aucun texte
  extractible). Même nom que le PDF, pour que les métadonnées (type, année,
  version) soient déduites pareil. Une transcription remplace le `.txt` du même nom.

Après tout ajout : `python3 ingest_series.py build`.
