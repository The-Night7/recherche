# Tuteur "from scratch" — recherche sémantique (TF-IDF)

Cours de **Préing 1 et Préing 2, semestres 1 et 2** (CM, TD, TP, DS, CC, QCM, projets, corrigés).
L'interface web distingue **l'année de Préing**, **le semestre**, **la matière** et
**l'année scolaire du document**. Chaque résultat rappelle sa formation et sa matière.
À pertinence proche, les
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

L'affichage sépare les explications des calculs, aligne les égalités et conserve
les paragraphes dans chaque question numérotée. Les formules longues défilent
horizontalement sur mobile. Les exercices et leurs corrigés restent entiers
dans l'index, même lorsqu'ils dépassent la taille habituelle d'un passage.
Les expressions répétées dans les PDF sont conservées lors du nettoyage.
La reconstruction reste heuristique : les formules dont l'extraction a perdu
des symboles peuvent nécessiter une transcription Markdown/LaTeX.
Les titres (`Ex.5`, `Exercice 5`…) et les questions (`a)`, `b)`, `1.`…)
sont délimités avant la reconstruction des maths. Une limite reste avec son
expression et un exercice court conserve son propre résultat de recherche.
Les grandes parenthèses extraites comme des espaces et des points d'exclamation
sont restaurées lorsque leurs paires sont identifiables. Les longues égalités
sont réparties entre leurs termes, sans couper les fractions ni les sommes.
Les bornes d'intégrale et d'évaluation sont séparées des fractions ; les
logarithmes compactés (`tln2t`) et les fractions commencées dans une phrase
restent regroupés. Lorsqu'une étape de dérivation a perdu ses signes, le
calcul affiche ses égalités lisibles et conserve l'extrait complet dans
« Étapes intermédiaires à vérifier », replié par défaut.
Pour les ambiguïtés restantes (portée d'une racine perdue, limite fragmentée…),
l'expression source est accessible via « Afficher l’expression d’origine »,
replié par défaut. Une transcription du PDF permet de retrouver un rendu
mathématique fiable pour ces passages.

Après une modification du nettoyage, reconstruire les données avec
`python3 ingest.py build`, puis redémarrer `python3 server.py`.

Vérifications du rendu et de l'import :

```bash
python3 -m unittest discover -s tests
node tests/test_rendering.js
```

## Utilisation

```bash
pip install numpy --break-system-packages

python3 build_index.py          # à refaire seulement si chunks.json change
python3 search.py "définition d'une norme"
python3 search.py "règle d'Alembert" --cours series --type td,ds --annees 2024,2023
python3 search.py "matrice" --preing 1 --semestre 2 --cours algebre2
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

## Ajouter des documents

Depuis la racine du projet, importer un fichier ou un dossier complet :

```bash
python3 ingest.py add /chemin/vers/le/dossier
```

L'import accepte les PDF, Markdown, textes et Word (`.docx`). Les matières sont
déclarées dans `courses.py`, avec un rattachement à l'un des quatre semestres.

| Année de Préing | Semestre | Matières |
| --- | --- | --- |
| Préing 1 | S1 | Algèbre 1, Analyse 1, CEF 1, IC 1, Informatique 1, Physique 1, Projet 1 |
| Préing 1 | S2 | Algèbre 2, Analyse 2, Informatique 2, Mécanique du point, Projet 1 |
| Préing 2 | S1 | Analyse dans ℝⁿ, Séries, Informatique 3, Électromagnétisme, SHS |
| Préing 2 | S2 | Algèbre linéaire, Informatique 4, Intégration et probabilités, Ondes, Physique moderne |

Pour importer des dossiers complets :

```bash
python3 ingest.py add PREING1-S1 PREING1-S2 PREING2-S2
```

La structure `PREING1-S2/Analyse2/…` indique explicitement l'année, le semestre
et la matière, même pour un fichier au nom libre. Elle prime sur les noms de fichiers
mal étiquetés. Hors de cette structure, utiliser le format
`TD1_2024-2025_Analyse2_P1S2_DMaths.pdf` : les repères `_P1S1_`, `_P1S2_`,
`_P2S1_` et `_P2S2_` sont reconnus, ainsi que les suffixes `-DS`, `-CC`, `-PROJET`.
Les deux « Projet 1 » sont stockés séparément (`projet1-s1`, `projet1-s2`).
Une matière sans document exploitable n'est pas proposée : les deux sujets
d'Éthique sont des scans à transcrire et le dossier
`PREING2-S2/Histoire-du-design-DS` est actuellement vide. Leur rattachement est
déjà déclaré dans le registre pour les prochains imports ou transcriptions.

L'index est reconstruit automatiquement ; redémarrer ensuite `python3 server.py`.
Les doublons sont ignorés au sein de la même matière et du même semestre.
Les scans sans texte et les images sont signalés pour transcription ;
le bilan détaillé du dernier import se trouve dans `data/import-report.json`.
Les PDF d'informatique et de sciences humaines conservent leur texte et leurs retours à la ligne ;
les notes Markdown conservent leurs blocs de code.
L'index reste creux en mémoire : le chargement de plusieurs semestres ne crée pas
de matrice dense de plusieurs gigaoctets.

Pour reconstruire après une modification d'un texte ou d'une transcription :

```bash
python3 ingest.py build
```

## Import historique de Séries (`ingest_series.py`)

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
