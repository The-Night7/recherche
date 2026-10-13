# Structure du dépôt

```
backend/    API Python (server.py, search.py, ingest.py…), données (data/, chunks.json, index.npz), tests, Dockerfile
frontend/   application Angular (TypeScript), nginx.conf, Dockerfile
docs/       ARCHITECTURE.md (architecture détaillée), DEPLOYMENT.md (déploiement)
docker-compose.yml
```

- **Documentation** : [passation](docs/PASSATION.md) · [architecture](docs/ARCHITECTURE.md) · [déploiement](docs/DEPLOYMENT.md) ·
  [frontend](frontend/README.md) · [backend](backend/README.md).
- **Développement** (deux terminaux) : `cd backend && python3 server.py`, puis
  `cd frontend && npm install && npm start` → http://localhost:4200.
- **Docker** : `docker compose up --build` puis http://localhost:8080 (nginx sert le front et relaie `/api/` vers le backend).
- **Une seule commande sans Docker** : `cd frontend && npm run build`, puis `cd backend && python3 server.py` sert aussi le build sur http://localhost:8000.
- Toutes les commandes Python ci-dessous se lancent **depuis `backend/`**.
- **Intégration continue** : GitHub Actions (`.github/workflows/ci.yml`), voir [passation](docs/PASSATION.md).
- **Tests** : `cd backend && python3 -m unittest discover -s tests` ; `cd frontend && npm test`.

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
# depuis backend/
python3 -m unittest discover -s tests
# depuis frontend/ (rendu du Markdown, composants, filtres)
npm test
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
pip install -r requirements.txt   # depuis backend/

python3 build_index.py          # à refaire seulement si chunks.json change
python3 search.py "définition d'une norme"
python3 search.py "règle d'Alembert" --cours series --type td,ds --annees 2024,2023
python3 search.py "matrice" --preing 1 --semestre 2 --cours algebre2
python3 ask.py                  # mode interactif (terminal)
python3 server.py               # interface web sur http://localhost:8000
```

`server.py` ne dépend de rien d'autre que la bibliothèque standard de
Python (`http.server`) + numpy pour la recherche : pas de Flask. L'interface est
l'application Angular de `frontend/` (voir [l'architecture](docs/ARCHITECTURE.md)).

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

Ordre de finalisation des transcriptions : **P2 → P1 → ING 1 → ING 2**, tous semestres compris. Terminer une année avant de passer à la suivante. **Dans P2, priorité aux mathématiques, en commençant par les séries.** Mettre à jour ce README après chaque document terminé, ainsi que le [bilan détaillé](backend/TRANSCRIPTIONS.md) et le [rapport par source](backend/data/transcription-report.json).

### Avancement P2 — 12 octobre 2026

**P2 est terminée dans le périmètre de l’inventaire : aucun document restant.** Une extraction brute ne compte pas comme une transcription achevée.

| Matière | Documents restants |
| --- | ---: |
| series | 0 |
| analyse-rn | 0 |
| electromagnetisme | 0 |
| informatique3 | 0 |

### Finalisation globale — 12 octobre 2026

P2 est terminée dans le périmètre de l’inventaire. Priorité actuelle : **P1 — Préing 1**. Il reste **655 documents** : P1 — Préing 1 : 175, ING 1 : 258, ING 2 : 222.

Cette suite ajoute **5 transcription(s), couvrant 136 pages PDF** ; le rattrapage de séries de 2 pages est compté dans le lot Séries/2627 ci-dessous.

- [CM_2019-2020_Electromagnetisme_P2S1_DPhysique](backend/data/electromagnetisme/transcriptions/CM_2019-2020_Electromagnetisme_P2S1_DPhysique.md)
- [DS1-2018-2019-Correction_Algebre1-DS_P1S1_Kfayad](backend/data/algebre1/transcriptions/DS1-2018-2019-Correction_Algebre1-DS_P1S1_Kfayad.md)
- [DS1-2020-2021-Correction_Algebre1-DS_P1S1_NArancibia-MBahtiti-KGuezguez-AHajej-BLaquerriere-JMasereel](backend/data/algebre1/transcriptions/DS1-2020-2021-Correction_Algebre1-DS_P1S1_NArancibia-MBahtiti-KGuezguez-AHajej-BLaquerriere-JMasereel.md)
- [DS1-2021-2022-V2-Correction_Algebre1-DS_P1S1_DMaths](backend/data/algebre1/transcriptions/DS1-2021-2022-V2-Correction_Algebre1-DS_P1S1_DMaths.md)
- [DS1-2024-2025-V3-Correction_Algebre1-DS_P1S1__LucienL](backend/data/algebre1/transcriptions/DS1-2024-2025-V3-Correction_Algebre1-DS_P1S1__LucienL.md)

### Finalisation globale — 13 octobre 2026

P2 est terminée dans le périmètre de l’inventaire. Priorité actuelle : **P1 — Préing 1**. Il reste **636 documents** : P1 — Préing 1 : 156, ING 1 : 258, ING 2 : 222.

Cette suite ajoute **19 transcription(s), couvrant 165 pages PDF** ; le rattrapage de séries de 2 pages est compté dans le lot Séries/2627 ci-dessous.

- [DS2-2018-2019-Correction_Algebre1-DS_P1S1_DMaths](backend/data/algebre1/transcriptions/DS2-2018-2019-Correction_Algebre1-DS_P1S1_DMaths.md)
- [DS3-2019-2020-Correction_Algebre1-DS_P1S1_Inconnu](backend/data/algebre1/transcriptions/DS3-2019-2020-Correction_Algebre1-DS_P1S1_Inconnu.md)
- [DS1-2024-2025-V3-Correction_Analyse1-DS_P1S1_PAfsharijoo](backend/data/analyse1/transcriptions/DS1-2024-2025-V3-Correction_Analyse1-DS_P1S1_PAfsharijoo.md)
- [CM1_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM1_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [CM2_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM2_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [CM3_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM3_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [CM4_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM4_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [CM5_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM5_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [CM6_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM6_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [CM_2013-2014_Mecanique-du-point_P1S2_DPhysique](backend/data/mecanique-du-point/transcriptions/CM_2013-2014_Mecanique-du-point_P1S2_DPhysique.md)
- [Theme1-Normes-powerpoint_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme1-Normes-powerpoint_2023-2024_CEF1_P1S1_DH&D.md)
- [Theme2-Definition-Communication_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme2-Definition-Communication_2023-2024_CEF1_P1S1_DH&D.md)
- [Theme4-Ecrit-professionnel-Exercices_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme4-Ecrit-professionnel-Exercices_2023-2024_CEF1_P1S1_DH&D.md)
- [Theme1-Faire-une-presentation-powerpoint_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme1-Faire-une-presentation-powerpoint_2023-2024_CEF1_P1S1_DH&D.md)
- [Theme5-Technique-de-redac-resume_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme5-Technique-de-redac-resume_2023-2024_CEF1_P1S1_DH&D.md)
- [Normes-Bibliographie_2024-2025_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Normes-Bibliographie_2024-2025_CEF1_P1S1_DH&D.md)
- [Theme1-Communication-par-image_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme1-Communication-par-image_2023-2024_CEF1_P1S1_DH&D.md)
- [Theme3-Normes-Etat-de-Art_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme3-Normes-Etat-de-Art_2023-2024_CEF1_P1S1_DH&D.md)
- [Theme4-Ecrit-professionnel_2023-2024_CEF1_P1S1_DH&D](backend/data/cef1/transcriptions/Theme4-Ecrit-professionnel_2023-2024_CEF1_P1S1_DH&D.md)


### Finalisation globale — suite du soir, 13 octobre 2026

P2 est terminée dans le périmètre de l’inventaire. Priorité actuelle : **P1 — Préing 1**. Il reste **628 documents** : P1 — Préing 1 : 148, ING 1 : 258, ING 2 : 222.

Cette suite ajoute **8 transcription(s) de l’inventaire, couvrant 28 pages PDF** :

- [Fiche-Analyse-dimensionnelle_2024-2025_Physique1_P1S1_DPhysique](backend/data/physique1/transcriptions/Fiche-Analyse-dimensionnelle_2024-2025_Physique1_P1S1_DPhysique.md)
- [TD1-Prerequis-Correction-_2023-2024_Physique1_P1S1_EDupont](backend/data/physique1/transcriptions/TD1-Prerequis-Correction-_2023-2024_Physique1_P1S1_EDupont.md)
- [DS2-2018-2019-Correction_Algebre2-DS_P1S2_KFayad](backend/data/algebre2/transcriptions/DS2-2018-2019-Correction_Algebre2-DS_P1S2_KFayad.md)
- [DM1-Continuite_2021-2022_Analyse2_P1S2_DMaths](backend/data/analyse2/transcriptions/DM1-Continuite_2021-2022_Analyse2_P1S2_DMaths.md)
- [TD5-Matrice-Correction_2023-2024_Algebre2_P1S2_DMaths](backend/data/algebre2/transcriptions/TD5-Matrice-Correction_2023-2024_Algebre2_P1S2_DMaths.md)
- [TD6-Inverser-une-matrice-Correction_2023-2024_Algebre2_P1S2_DMaths](backend/data/algebre2/transcriptions/TD6-Inverser-une-matrice-Correction_2023-2024_Algebre2_P1S2_DMaths.md)
- [TD8-Representation-matricielle-Correction(10-12)_2023-2024_Algebre2_P1S2_DMaths](backend/data/algebre2/transcriptions/TD8-Representation-matricielle-Correction%2810-12%29_2023-2024_Algebre2_P1S2_DMaths.md)
- [DS2-2022-2023-V1-Correction_Algebre2-DS_P1S2_MDebyaoui](backend/data/algebre2/transcriptions/DS2-2022-2023-V1-Correction_Algebre2-DS_P1S2_MDebyaoui.md)

**13 transcriptions hors inventaire** (dossier `PREING1-S1/Analyse1-DS`). Ce sont des sujets de DS, ou des corrigés dont le nom de fichier ne contient pas « Correction ». L’inventaire, limité aux cours et corrigés identifiés par leur nom, ne les compte pas : le reliquat n’en est pas modifié. Plusieurs fichiers ont un titre interne différent de leur nom (« DS 4 », « Corrigé du DM 3 », « Devoir Surveillé 2 », « Examen ») ; l’écart est signalé dans chaque transcription. `DS1-2023-2024` et `DS1-2023-2024-V1` sont des copies binaires identiques.

- [DS1-2024-2025-V3_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2024-2025-V3_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2024-2025-V1_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2024-2025-V1_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2024-2025-V2_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2024-2025-V2_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2023-2024-V2_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2023-2024-V2_Analyse1-DS_P1S1_DMaths.md)
- [DS3-2021-2022_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS3-2021-2022_Analyse1-DS_P1S1_DMaths.md)
- [DS3-2023-2024_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS3-2023-2024_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2020-2021-V3_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2020-2021-V3_Analyse1-DS_P1S1_DMaths.md)
- [DS3-2020-2021-V2_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS3-2020-2021-V2_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2020-2021_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2020-2021_Analyse1-DS_P1S1_DMaths.md)
- [DS3-2020-2021_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS3-2020-2021_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2021-2022_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2021-2022_Analyse1-DS_P1S1_DMaths.md)
- [DS2-2023-2024_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS2-2023-2024_Analyse1-DS_P1S1_DMaths.md)
- [DS1-2023-2024-V1_Analyse1-DS_P1S1_DMaths](backend/data/analyse1/transcriptions/DS1-2023-2024-V1_Analyse1-DS_P1S1_DMaths.md)
### Séries — documents mis à disposition en 2026–2027

Le dossier `PREING2-S1/Series/2627` contient **17 PDF (35 pages)**. **16 nouvelles transcriptions (34 pages)** sont terminées ; **1 sujet déjà transcrit** est réutilisé sans duplication. **Tous les documents de ce dossier sont transcrits.** Les annales conservent leur année réelle (2024–2025 ou 2025–2026). Le lot Séries/2627 est terminé ; la reprise globale suit l’ordre P2 → P1 → ING 1 → ING 2.

- [DS1-SujetB_2024-2025](backend/data/series/transcriptions/DS1-SujetB_2024-2025_Series_P2S1_DMaths.md) — 1 page(s).
- [DS1-SujetC_2024-2025](backend/data/series/transcriptions/DS1-SujetC_2024-2025_Series_P2S1_DMaths.md) — 1 page(s).
- [DS2-SujetA_2024-2025](backend/data/series/transcriptions/DS2-SujetA_2024-2025_Series_P2S1_DMaths.md) — 1 page(s).
- [DS2-SujetB_2024-2025](backend/data/series/transcriptions/DS2-SujetB_2024-2025_Series_P2S1_DMaths.md) — 1 page(s).
- [DS2-SujetC_2024-2025](backend/data/series/transcriptions/DS2-SujetC_2024-2025_Series_P2S1_DMaths.md) — 1 page(s).
- [DS3_2024-2025](backend/data/series/transcriptions/DS3_2024-2025_Series_P2S1_DMaths.md) — 2 page(s).
- [CC1_2025-2026](backend/data/series/transcriptions/CC1_2025-2026_Series_P2S1_DMaths.md) — 1 page(s).
- [CC1-Correction_2025-2026](backend/data/series/transcriptions/CC1-Correction_2025-2026_Series_P2S1_DMaths.md) — 4 page(s).
- [CC2_2025-2026](backend/data/series/transcriptions/CC2_2025-2026_Series_P2S1_DMaths.md) — 1 page(s).
- [CC2-Correction_2025-2026](backend/data/series/transcriptions/CC2-Correction_2025-2026_Series_P2S1_DMaths.md) — 4 page(s).
- [CC3_2025-2026](backend/data/series/transcriptions/CC3_2025-2026_Series_P2S1_DMaths.md) — 2 page(s).
- [CC3-Correction_2025-2026](backend/data/series/transcriptions/CC3-Correction_2025-2026_Series_P2S1_DMaths.md) — 7 page(s).
- [Rattrapage_2025-2026](backend/data/series/transcriptions/Rattrapage_2025-2026_Series_P2S1_DMaths.md) — 2 pages.
- [Fiche-Developpements-limites_2026-2027](backend/data/series/transcriptions/Fiche-Developpements-limites_2026-2027_Series_P2S1_DMaths.md) — 2 page(s).
- [TD0_2026-2027](backend/data/series/transcriptions/TD0_2026-2027_Series_P2S1_DMaths.md) — 1 page(s).
- [TD1_2026-2027](backend/data/series/transcriptions/TD1_2026-2027_Series_P2S1_DMaths.md) — 3 page(s).

Le lot des 10–12 octobre ajoute **11 transcription(s), couvrant 1329 pages PDF**. Les erreurs et réponses absentes des sources sont signalées.

- [TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada](backend/data/analyse-rn/transcriptions/TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.md)
- [CM-Chapitre1-champ_2024-2025_Electromagnetisme_P2S1_ABoumiz](backend/data/electromagnetisme/transcriptions/CM-Chapitre1-champ_2024-2025_Electromagnetisme_P2S1_ABoumiz.md)
- [Cours_2001-2002_Electromagnetisme_P2S1_JFerreira](backend/data/electromagnetisme/transcriptions/Cours_2001-2002_Electromagnetisme_P2S1_JFerreira.md)
- [CM1-Listes-Chainee_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon](backend/data/informatique3/transcriptions/CM1-Listes-Chainee_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon.md)
- [CM1-Listes-Chaines_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM1-Listes-Chaines_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)
- [CM2-Files-Piles_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM2-Files-Piles_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)
- [CM3-Arbres_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM3-Arbres_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)
- [CM3-Arbres_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM3-Arbres_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)
- [CM4-ABR_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM4-ABR_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)
- [CM5-AVL_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM5-AVL_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)
- [CM6-Unix-Shell_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin](backend/data/informatique3/transcriptions/CM6-Unix-Shell_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.md)

Le lot du 9 octobre ajoute **3 transcriptions (1847 pages PDF)** : [CM_2024-2025_Analyse-dans-RN_P2S1_EMasnada](backend/data/analyse-rn/transcriptions/CM_2024-2025_Analyse-dans-RN_P2S1_EMasnada.md). [CM_2023-2024_Analyse-dans-RN_P2S1](backend/data/analyse-rn/transcriptions/CM_2023-2024_Analyse-dans-RN_P2S1.md). Les animations sont regroupées en sections avec renvois au PDF ; les variantes ont été vérifiées visuellement. Le [polycopié de cours](backend/data/analyse-rn/transcriptions/Feuille-Cours_2022-2023_Analyse-dans-RN_P2S1_EMasnada.md) (127 pages) est également transcrit et vérifié.

Le lot du 8 octobre contient **37 nouveaux documents (1402 pages)**. Deux transcriptions de potentiel déjà présentes ont également été réintégrées au bilan, sans nouvelle relecture. Les erreurs et lacunes des PDF sont signalées dans les transcriptions.

Documents terminés dans le lot du 8 octobre :

- [CM-Annotee_2022-2023_Analyse-dans-RN_P2S1_MX](backend/data/analyse-rn/transcriptions/CM-Annotee_2022-2023_Analyse-dans-RN_P2S1_MX.md)
- [CM_2022-2023_Analyse-dans-RN_P2S1_EMasnada](backend/data/analyse-rn/transcriptions/CM_2022-2023_Analyse-dans-RN_P2S1_EMasnada.md)
- [DS1-2020-2021-Correction_Analyse-dans-RN-DS_P2S1_EMasnada](backend/data/analyse-rn/transcriptions/DS1-2020-2021-Correction_Analyse-dans-RN-DS_P2S1_EMasnada.md)
- [DS1-2021-2022-Correction_Analyse-dans-RN-DS_P2S1_Inconnu](backend/data/analyse-rn/transcriptions/DS1-2021-2022-Correction_Analyse-dans-RN-DS_P2S1_Inconnu.md)
- [DS1-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_DMaths](backend/data/analyse-rn/transcriptions/DS1-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_DMaths.md)
- [DS1-2023-2024-V2-Correction_Analyse-dans-RN-DS_P2S1_DMaths](backend/data/analyse-rn/transcriptions/DS1-2023-2024-V2-Correction_Analyse-dans-RN-DS_P2S1_DMaths.md)
- [DS2-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_DMaths](backend/data/analyse-rn/transcriptions/DS2-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_DMaths.md)
- [DS3-2021-2022-Correction_Analyse-dans-RN-DS_P2S1_Inconnu](backend/data/analyse-rn/transcriptions/DS3-2021-2022-Correction_Analyse-dans-RN-DS_P2S1_Inconnu.md)
- [DS3-2022-2023-Correction_Analyse-dans-RN-DS_P2S1__RayaneM](backend/data/analyse-rn/transcriptions/DS3-2022-2023-Correction_Analyse-dans-RN-DS_P2S1__RayaneM.md)
- [DS3-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_EMasnada](backend/data/analyse-rn/transcriptions/DS3-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_EMasnada.md)
- [TD-(6-7)-Correction_2024-2025_Analyse-dans-RN_P2S1_KElAmine](backend/data/analyse-rn/transcriptions/TD-%286-7%29-Correction_2024-2025_Analyse-dans-RN_P2S1_KElAmine.md)
- [slides_de_cours_MI_version_imprimable_2026_2027](backend/data/analyse-rn/transcriptions/slides_de_cours_MI_version_imprimable_2026_2027.md)
- [sujet_TD_2026_2027](backend/data/analyse-rn/transcriptions/sujet_TD_2026_2027.md)
- [CM-BIS-Chapitre1-Champ_2024-2025_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre1-Champ_2024-2025_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre1_2023-2024_Electromagnetisme_P2S1_ABoumiz](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre1_2023-2024_Electromagnetisme_P2S1_ABoumiz.md)
- [CM-BIS-Chapitre1_2024-2025_Electromagnetisme_P2S1_ABoumiz](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre1_2024-2025_Electromagnetisme_P2S1_ABoumiz.md)
- [CM-BIS-Chapitre2-Biot-Savart_2023-2024_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre2-Biot-Savart_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre2-Biot-Savart_2024-2025_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre2-Biot-Savart_2024-2025_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre3-Maxwell_2023-2024_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre3-Maxwell_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-BIS-Chapitre3-Maxwell_2024-2025_Electromagnetisme_P2S1_EDupont-LDesplat](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre3-Maxwell_2024-2025_Electromagnetisme_P2S1_EDupont-LDesplat.md)
- [CM-BIS-Chapitre4_2024-2025_Electromagnetisme_P2S1_ABoumiz](backend/data/electromagnetisme/transcriptions/CM-BIS-Chapitre4_2024-2025_Electromagnetisme_P2S1_ABoumiz.md)
- [CM-Chapitre1-Force_2022-2023_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre1-Force_2022-2023_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre1-Force_2023-2024_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre1-Force_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre1-champ_2023-2024_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre1-champ_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre2-Champ_2022-2023_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre2-Champ_2022-2023_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre2-Champ_2023-2024_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre2-Champ_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre6-Conducteurs_2022-2023_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre6-Conducteurs_2022-2023_Electromagnetisme_P2S1_EDupont.md)
- [CM-Chapitre6-Conducteurs_2023-2024_Electromagnetisme_P2S1_EDupont](backend/data/electromagnetisme/transcriptions/CM-Chapitre6-Conducteurs_2023-2024_Electromagnetisme_P2S1_EDupont.md)
- [CM-Rappels_2022-2023_Electromagnetisme_P2S1_DPhysique](backend/data/electromagnetisme/transcriptions/CM-Rappels_2022-2023_Electromagnetisme_P2S1_DPhysique.md)
- [Fiche-Resume-Electrostatique_2022-2023_Electromagnetisme_P2S1_DPhysique](backend/data/electromagnetisme/transcriptions/Fiche-Resume-Electrostatique_2022-2023_Electromagnetisme_P2S1_DPhysique.md)
- [CM-Annotee_2022-2023_Series_P2S1_MX](backend/data/series/transcriptions/CM-Annotee_2022-2023_Series_P2S1_MX.md)
- [CM-Comparaison-locale_2024-2025_Series_P2S1_DCransac](backend/data/series/transcriptions/CM-Comparaison-locale_2024-2025_Series_P2S1_DCransac.md)
- [CM-Derivation_2024-2025_Series_P2S1_DCransac](backend/data/series/transcriptions/CM-Derivation_2024-2025_Series_P2S1_DCransac.md)
- [CM_2022-2023_Series_P2S1_RDujol](backend/data/series/transcriptions/CM_2022-2023_Series_P2S1_RDujol.md)
- [TD1-Correction_2022-2023_Series_P2S1_Inconnu](backend/data/series/transcriptions/TD1-Correction_2022-2023_Series_P2S1_Inconnu.md)
- [TD2a-Correction_2022-2023_Series_P2S1_Inconnu](backend/data/series/transcriptions/TD2a-Correction_2022-2023_Series_P2S1_Inconnu.md)
- [TD2b-Correction_2022-2023_Series_P2S1_Inconnu](backend/data/series/transcriptions/TD2b-Correction_2022-2023_Series_P2S1_Inconnu.md)

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
