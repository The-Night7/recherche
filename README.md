# Tuteur "from scratch" — recherche sémantique (TF-IDF)

Cours de **Préing 1 et Préing 2, semestres 1 et 2** (CM, TD, TP, DS, CC, QCM, projets, corrigés).
L'interface web distingue **l'année de Préing**, **le semestre**, **la matière** et
**l'année scolaire du document**. Chaque résultat rappelle sa formation et sa matière.
À pertinence proche, les
documents les plus récents passent devant.
Le bouton **Fichiers** (raccourci `b`) ouvre une fenêtre pour parcourir les
documents matière par matière et les lire en entier, avec document précédent/suivant.

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

## Vidéos liées

Sous chaque passage (exercice, partie de cours…), la ligne **Vidéos** donne
jusqu'à trois notions traitées. Chacune a une vidéo précise des chaînes
[Maths Adultes](https://www.youtube.com/@mathsadultes) ou
[E-learning physique](https://www.youtube.com/@e-learningphysique4910), quand
l'une d'elles traite la notion (`VIDEOS` dans `videos.py`). Entre plusieurs
vidéos d'une notion, c'est celle dont les mots-clés sont dans le passage qui est
choisie (« module » → *Nombres complexes 4/12 : Module*). Sinon, le lien ouvre
une recherche YouTube : « <notion> cours » pour un cours, « <notion> exercice
corrigé » pour un TD/DS/CC/QCM.

Les notions et leurs mots-clés sont aussi dans `videos.py`. Un passage est relié
aux notions dont les mots-clés apparaissent dans son texte ou son titre, les
notions rares passant devant (pondération IDF). Les matières sans domaine
maths/info/physique (SHS, éthique…) n'ont pas de vidéos. Après une modification
de `videos.py`, il suffit de redémarrer `server.py` (pas de reconstruction de
l'index).

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

Ordre de finalisation des transcriptions : **P2 → P1 → ING 1 → ING 2**, tous semestres compris. Terminer une année avant de passer à la suivante. **Dans P2, priorité aux mathématiques, en commençant par les séries.** Mettre à jour ce README après chaque document terminé, ainsi que le [bilan détaillé](TRANSCRIPTIONS.md) et le [rapport par source](data/transcription-report.json).

### Avancement P2 — 7 octobre 2026

**P2 n’est pas terminée : 30 documents restent à transcrire ou à vérifier.** Une extraction brute ne compte pas comme une transcription achevée.

| Matière | Documents restants |
| --- | ---: |
| series | 2 |
| analyse-rn | 17 |
| electromagnetisme | 3 |
| informatique3 | 8 |

Le lot en cours contient **22 nouveaux documents (757 pages)**. Deux transcriptions de potentiel déjà présentes ont également été réintégrées au bilan, sans nouvelle relecture. Les erreurs et lacunes des PDF sont signalées dans les transcriptions.

Documents terminés dans ce lot :

- [CM-BIS-Chapitre1-Champ_2024-2025_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-BIS-Chapitre1-Champ_2024-2025_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre1_2023-2024_Electromagnetisme_P2S1_ABoumiz](data/electromagnetisme/transcriptions/CM-BIS-Chapitre1_2023-2024_Electromagnetisme_P2S1_ABoumiz.md)
- [CM-BIS-Chapitre1_2024-2025_Electromagnetisme_P2S1_ABoumiz](data/electromagnetisme/transcriptions/CM-BIS-Chapitre1_2024-2025_Electromagnetisme_P2S1_ABoumiz.md)
- [CM-BIS-Chapitre2-Biot-Savart_2023-2024_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-BIS-Chapitre2-Biot-Savart_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre2-Biot-Savart_2024-2025_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-BIS-Chapitre2-Biot-Savart_2024-2025_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre3-Maxwell_2023-2024_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-BIS-Chapitre3-Maxwell_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre3-Maxwell_2024-2025_Electromagnetisme_P2S1_EDupont-LDesplat](data/electromagnetisme/transcriptions/CM-BIS-Chapitre3-Maxwell_2024-2025_Electromagnetisme_P2S1_EDupont-LDesplat.md)
- [CM-BIS-Chapitre4_2024-2025_Electromagnetisme_P2S1_ABoumiz](data/electromagnetisme/transcriptions/CM-BIS-Chapitre4_2024-2025_Electromagnetisme_P2S1_ABoumiz.md)
- [CM-Chapitre1-Force_2022-2023_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre1-Force_2022-2023_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre1-Force_2023-2024_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre1-Force_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre1-champ_2023-2024_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre1-champ_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre2-Champ_2022-2023_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre2-Champ_2022-2023_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre2-Champ_2023-2024_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre2-Champ_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre6-Conducteurs_2022-2023_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre6-Conducteurs_2022-2023_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre6-Conducteurs_2023-2024_Electromagnetisme_P2S1_EDupont](data/electromagnetisme/transcriptions/CM-Chapitre6-Conducteurs_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Rappels_2022-2023_Electromagnetisme_P2S1_DPhysique](data/electromagnetisme/transcriptions/CM-Rappels_2022-2023_Electromagnetisme_P2S1_DPhysique.md)
- [Fiche-Resume-Electrostatique_2022-2023_Electromagnetisme_P2S1_DPhysique](data/electromagnetisme/transcriptions/Fiche-Resume-Electrostatique_2022-2023_Electromagnetisme_P2S1_DPhysique.md)
- [CM-Annotee_2022-2023_Series_P2S1_MX](data/series/transcriptions/CM-Annotee_2022-2023_Series_P2S1_MX.md)
- [CM-Comparaison-locale_2024-2025_Series_P2S1_DCransac](data/series/transcriptions/CM-Comparaison-locale_2024-2025_Series_P2S1_DCransac.md)
- [CM-Derivation_2024-2025_Series_P2S1_DCransac](data/series/transcriptions/CM-Derivation_2024-2025_Series_P2S1_DCransac.md)
- [CM_2022-2023_Series_P2S1_RDujol](data/series/transcriptions/CM_2022-2023_Series_P2S1_RDujol.md)
- [TD1-Correction_2022-2023_Series_P2S1_Inconnu](data/series/transcriptions/TD1-Correction_2022-2023_Series_P2S1_Inconnu.md)

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
