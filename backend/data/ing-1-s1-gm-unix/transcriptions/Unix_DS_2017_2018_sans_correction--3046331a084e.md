---
source: "ING 1/S1 GM /UNIX/Examen/Unix_DS_2017_2018_sans_correction.pdf"
pages: 2
transcription: énoncés et tableau transcrits et relus, sans ajout de solutions
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle des deux pages du PDF
---

# Commandes Unix — Examen de janvier 2019, sans correction

EISTI, Cergy–Pau. Cycle ingénieur, première année. L’équipe enseignante. Durée : une heure.

**Écarts du support :** le nom du fichier indique 2017–2018 ; l’en-tête indique janvier 2019. Le PDF contient deux pages physiques, bien que l’en-tête annonce trois pages et que la dernière porte aussi le repère « −3/3− ». Le document contient uniquement les énoncés, sans solutions.

## Page 1

## Modalités

- Durée : 1 heure.
- Type : papier.
- Aucun document n’est autorisé.
- Vous devez rédiger votre copie à l’aide d’un stylo à encre exclusivement.
- Les déplacements et les échanges ne sont pas autorisés.
- Aucune question ne peut être posée aux enseignants, posez des hypothèses en cas de doute.

## Exercice 1 — 11 points

Vous venez de vous connecter au système utilisateur en tant que Jimmy. Vous vous trouvez dans /home/Jimmy.

1. Afficher le contenu de /home/Jimmy de telle sorte que les fichiers récemment modifiés apparaissent en premier (0.5 pt).
2. Créer en une seule commande un répertoire Cours avec un sous-répertoire Unix (1 pt).
3. Créer 4 fichiers à l’intérieur du sous-répertoire Cours s’appelant TD1 - TD2 - TD3 - TD4 (1 pt).
4. Modifier les droits de l’ensemble de ces fichiers en une seule commande de la manière suivante : rwxr–r– (1 pt).
5. Écrire le texte « Para bailar » dans TD1 et le texte « La Bamba » dans TD2 (1 pt).
6. Compter le nombre de lignes dans le fichier TD1 (0.5 pt).
7. Afficher le contenu du répertoire Cours/Unix avec des signes distinctifs qui permettent d’identifier plus vite le type de fichier (0.5 pt).
8. Supprimer le fichier TD1 (0.5 pt).
9. Renommer le fichier TD3 en Rictchie (1 pt).
10. Copier le fichier « Ritchie » dans le répertoire Cours (1 pt).
11. Rechercher le fichier TD4 et renommer ce fichier en « notes ». Réaliser cette opération en une et une seule commande. (1.5 pt).
12. Rechercher dans etc/ et dans ses sous-répertoires, si un ou des fichiers contient le mot Jimmy (1.5 pt).

## Page 2

## Exercice 2 — 5 points

Soit le fichier de notes de l’étudiant Jimmy : « notes.txt »

| Identifiant de matière | Intitulé | Note | Classement |
| --- | --- | ---: | ---: |
| 5896 | Java | 14 | 15 |
| 4589 | BD | 20 | 1 |
| 7415 | Algorithme | 17 | 3 |
| 4568 | Pascal | 8 | 20 |
| 4567 | Web | 15 | 7 |

NB : la première colonne désigne l’identifiant de la matière, la deuxième colonne l’intitulé de la matière, la troisième colonne la note obtenue, et la quatrième colonne le classement de l’étudiant dans la matière.

1. Trier le fichier par note décroissante (1 pt).
2. Trier le fichier par ordre sur l’intitulé des matières (1 pt).
3. Trier le fichier par ordre croissant du classement (quatrième colonne) et n’afficher que les matières (1.5 pt).
4. Chercher la matière Algorithme et afficher le résultat en majuscule (1.5 pt).

## Exercice 3 — 4 points

Écrire un script shell prenant en argument un fichier F1.txt. Par exemple : ./test.sh F1.txt. Ce script doit réaliser les actions suivantes :

1. Afficher le nombre d’arguments passés en paramètre et vérifier qu’il est égal à 1 (2 pt).
2. Créer un répertoire « Partiel » puis chercher dans le répertoire courant le fichier passé en argument et le déplacer dans le répertoire « Partiel » (2 pt).

**Note de transcription :** l’énoncé alterne les noms « Rictchie » et « Ritchie » et indique les permissions sous la forme typographique `rwxr–r–`, correspondant à `rwxr--r--`. Ces écarts sont conservés.
