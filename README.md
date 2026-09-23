# Tuteur "from scratch" — recherche sémantique (TF-IDF)

Cours indexés : **Analyse dans ℝⁿ** et **Séries** (CM, TD, DS, QCM, corrigés).
L'interface web permet de choisir où chercher : un cours ou tous, le type de
document, énoncés et/ou corrigés, les années. À pertinence proche, les
documents les plus récents passent devant.

Contrairement à `ml_project/` (réseau de neurones génératif), celui-ci
ne génère rien : il **retrouve le bon passage du cours** pour une
question, via un moteur de recherche TF-IDF codé à la main (NumPy
seul, pas de scikit-learn, pas d'API, pas de réseau).

Résultat : c'est cohérent par construction (c'est le vrai texte du
cours), au prix de ne pas "répondre" à une question comme le ferait
un LLM — ça renvoie le(s) passage(s) les plus proches (définitions,
théorèmes, extraits de TD).

## Les maths (tout est dans `build_index.py`)
- TF(mot, doc) = nombre d'occurrences du mot dans le passage
- IDF(mot) = log((1+N)/(1+DF(mot))) + 1
- TF-IDF = TF × IDF, puis normalisation L2 de chaque vecteur
- similarité(question, passage) = produit scalaire des vecteurs
  normalisés = cosinus de l'angle entre eux

## Nettoyage du texte source (`clean_extraction.py`)
Le texte brut extrait des PDF contient des artefacts (en-têtes de page
répétés, exposants coupés sur la ligne suivante comme "R" puis "n" au
lieu de "Rⁿ"). `clean_extraction.py` répare ça avant l'indexation :
suppression des en-têtes/numéros de page répétés, fusion des exposants
coupés. Ce n'est pas parfait (formules multi-lignes complexes) mais
nettement plus lisible.

## Utilisation

```bash
pip install numpy --break-system-packages

python3 build_index.py          # à refaire seulement si chunks.json change
python3 search.py "définition d'une norme"
python3 search.py "règle d'Alembert" --cours series --type td,ds --annees 2024,2023
python3 ask.py                  # mode interactif (terminal)
python3 server.py               # interface web sur http://localhost:8000
```

`server.py` ne dépend de rien d'autre que la bibliothèque standard de
Python (`http.server`) + numpy pour la recherche : pas de Flask, pas
de framework JS, page HTML/CSS/JS auto-contenue servie directement.

## Limites
- Ça ne répond qu'avec des passages existants du cours, mot pour mot
  (pas de reformulation, pas de raisonnement, pas de résolution
  d'exercice inédit).
- La pertinence dépend du vocabulaire employé : une question formulée
  très différemment du cours (synonymes non couverts) peut ne rien
  trouver de pertinent.

## Ajouter des documents au cours de Séries (`ingest_series.py`)

```bash
pip install pypdf --break-system-packages               # lecture des PDF
python3 ingest_series.py extract ~/Cours/Series/*.pdf   # texte -> data/series/
python3 ingest_series.py build                          # découpage + chunks.json + index
```

Les métadonnées viennent du nom de fichier (`TD4_20242025_Series_…`,
`DS120232024V4Correction_…`, `QCM1-2022-2023_…`). Un PDF scanné (sans texte)
est signalé par `extract` : mettre sa transcription Markdown/LaTeX dans
`data/series/transcriptions/<même nom>.md` puis relancer `build`.

Découpage : un passage par exercice pour les TD/DS/QCM (la réponse d'un
corrigé reste avec son exercice, les questions de QCM répétées sur chaque
copie sont dédoublonnées), par section numérotée pour le poly de cours, par
titre pour les notes Markdown. Les formules `$…$` / `$$…$$` des notes sont
rendues avec KaTeX dans l'interface.

## Récence

score = cos(question, passage) × (1 + 0.25 × r), avec r ∈ [0, 1] la position
de l'année du document entre la plus ancienne et la plus récente de son cours
(0.5 si l'année est inconnue). Désactivable dans l'interface ou avec
`--sans-recence`.


## Pour extraire le contenu d'un pdf :

```
pip install pypdf --break-system-packages   # une seule fois
python3 ingest_series.py extract ~/Cours/Series/TD5_20252026_Series_P2S1_DMaths.pdf
python3 ingest_series.py build
```