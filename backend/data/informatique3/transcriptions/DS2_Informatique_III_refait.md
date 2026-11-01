---
source: "PREING2-S1/Informatique3-DS/cc-2025-2026/DS2_Informatique_III_refait.pdf"
archive: "cc 2025 2026.zip"
pages: 2
semestre: "P2S1"
transcription: texte natif restructuré et contrôlé sur le rendu PDF
transcription_date: 2026-11-01
verification: comparaison du texte extrait avec le rendu des pages du PDF fourni
---

# DS2 Informatique III refait

## Page 1

CY TECH

DS N° 2 — INFORMATIQUE III Pré-ING2 · Semestre 1 · 2025/2026 · Langage C obligatoire

Calculatrice et documents non autorisés. Attention à la robustesse du programme. Vous pouvez définir autant de fonctions que vous le souhaitez. Une question ne correspond pas nécessairement à une fonction.

### Exercice 1 — Opérations sur des ABR (4 points)

On considère dans cet exercice que les arbres sont des ABR permettant de stocker des entiers.

1. Écrire la fonction d’insertion d’un élément dans un ABR.

2. Écrire une fonction qui prend deux ABR en paramètres et qui va créer et retourner l’adresse d’un troisième arbre comportant toutes les valeurs des deux premiers. Ce troisième arbre doit également être un ABR.

3. Écrire une fonction qui va afficher tous les éléments d’un ABR, triés dans l’ordre décroissant. Cette fonction prendra en paramètre le nœud racine de l’arbre et renverra comme valeur de retour le nombre de nœuds parcourus.

### Exercice 2 — Arbre multiplicatif (6 points)

On définit une nouvelle structure d’arbre, appelée multiplicatif, qui respecte les règles suivantes :

— C’est un arbre ternaire, chaque nœud possède trois enfants : gauche, milieu et droit. La valeur stockée dans un nœud est un entier.

— Les feuilles contiennent des entiers strictement positifs et premiers.

— Chaque nœud interne contient la valeur égale au produit exact de ses trois enfants. Si le nœud n’a pas trois enfants, on fera le produit de ses enfants existants (deux enfants : produit de ces deux enfants, un enfant : valeur de cet enfant).

— Aucun nœud (feuille ou interne) ne peut contenir la valeur 0.

1. Écrire la structure permettant de représenter un arbre multiplicatif.

2. Écrire une fonction est_multiplicatif(...) qui prendra en paramètre un arbre et retournera 1 s’il est multiplicatif, 0 sinon.

### Exercice 3 — Affichage d’un arbre sans récursivité (7 points)

Dans cet exercice, nous considérons des arbres binaires dont chaque nœud contient une valeur réelle. Nous supposons que la structure suivante est déjà définie :

```c

typedef struct arbre { float valeur; struct arbre* fg; struct arbre* fd; } Arbre;

```

1. Écrire la ou les structures permettant de gérer une PILE contenant des pointeurs vers des structures Arbre.

2. Écrire la fonction de dépilage d’une telle PILE.

3. Écrire uniquement le prototype de la fonction permettant d’empiler un pointeur dans une telle PILE. On émet l’hypothèse que cette fonction est déjà codée et prête à être utilisée.

4. Écrire une procédure permettant d’afficher le parcours préfixe d’un arbre passé en paramètre. Cette procédure devra obligatoirement être itérative et pour cela utiliser les fonctions définies précédemment.

Habituellement, le parcours préfixe est codé de manière récursive et il utilise une pile pour se souvenir des ancêtres du nœud courant pour remonter l’historique : cette pile est la pile d’appels récursifs. Mais comme ici on souhaite coder en itératif, il faudra gérer la pile manuellement.

## Page 2

ATTENTION : si cette procédure est récursive, elle n’accordera aucun point.

### Exercice 4 — Rotation droite d’un AVL (4 points)

1. Écrire la fonction permettant d’effectuer une rotation droite. Argumenter le choix des instructions qui modifient les facteurs d’équilibre. Utiliser pour cela la structure suivante :

```c

typedef struct avl { int valeur; int equilibre; struct avl* fg; struct avl* fd; } AVL;

```

2. Indiquer dans quels cas une rotation droite doit être effectuée dans un AVL (on donnera pour chaque cas un exemple d’arbre).
