---
source: TD3-Liste-Piles-Files_2024-2025_Informatique3_P2S1_DInformatique.pdf, pages 1-2 (identique à TD03-Liste-Piles-Files_2023-2024)
transcription: manuelle
---

# TD 03 : Piles et files (2)

> **Note :** la correction de ce TD est rédigée dans le document 2024-10-04-TD3-Liste-Piles-Files-Correction_2024-2025 (AhmedA) ; le même énoncé corrigé se trouve aussi dans la transcription de TD3-Pile-File-Listes_2022-2023.

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

## Exercice 1 : Liste doublement chaînée

**Énoncé.** On rappelle que les chaînons des listes doublement chaînées possèdent un pointeur vers le chaînon suivant et un pointeur vers le chaînon précédent. Il est donc possible de parcourir une telle liste dans les deux sens.

1. Déclarer une structure de liste doublement chaînée permettant de stocker des mots de 20 caractères maximum.
2. Écrire une fonction `compareMot(char *mot1, char *mot2)` qui retourne 1 si `mot1` est avant `mot2` dans l'ordre alphabétique et 0 sinon.
3. Écrire une fonction `insertListe(char *mot1, liste *pliste)` qui ajoute à la liste doublement chaînée pointée par `pliste`, de mots classés dans l'ordre alphabétique, un nouveau chaînon contenant `mot1`.
4. Écrire une procédure `affiche(liste *pliste)` qui affiche dans l'ordre les mots contenus dans la liste.
5. Écrire une procédure `afficheInv(liste *pliste)` qui affiche dans l'ordre inverse les mots contenus dans la liste.
6. Déclarer une nouvelle liste et la remplir avec une vingtaine de mots. Afficher cette liste de mots dans l'ordre alphabétique et anti-alphabétique.

## Exercice 2 : Tri de crêpes

**Énoncé.** (Extrait du rattrapage de 2021-2022.) On souhaite écrire un algorithme qui va pouvoir modéliser le comportement d'un tas de crêpes qui sera trié par un humain (par ordre croissant de diamètre, la plus petite sur le dessus, la plus grande tout en bas du tas).

L'humain ne dispose que d'un seul outil pour trier ses crêpes : une spatule qu'il peut insérer entre 2 crêpes (sans les abîmer), et retourner le tas au-dessus de la spatule. Cette opération inverse donc la partie supérieure du tas uniquement.

Exemple (tas écrit du dessus vers le dessous) : `3 6 2 9 7 4 5`. En plaçant la spatule entre la crêpe de diamètre 9 (la plus grande) et la crêpe de diamètre 7, on inverse l'ordre des crêpes placées au-dessus de la spatule : la crêpe 9 se retrouve au-dessus, `9 2 6 3 7 4 5`. Il faut ensuite placer la crêpe 9 tout en bas : pour cela, on réalise la même opération pour tout le tas (spatule sous la crêpe 5). En 2 coups de spatule, la crêpe la plus grande est tout en bas : `5 4 7 3 6 2 9`.

Il ne reste plus qu'à vérifier si le tas est correctement trié. Si ce n'est pas le cas, il faut recommencer avec les N-1 crêpes supérieures (la crêpe 9 n'a plus besoin d'être touchée), sinon le tri est terminé. Étapes suivantes pour ce tas, avec le nombre de crêpes correctement placées en bas :

```
5 4 7 3 6 2 9   (1)
7 4 5 3 6 2 9   (1)
2 6 3 5 4 7 9   (2)
6 2 3 5 4 7 9   (2)
4 5 3 2 6 7 9   (3)
5 4 3 2 6 7 9   (3)
2 3 4 5 6 7 9   (7)
```

> **Note :** dans le document, les tas sont dessinés verticalement, avec la position de la spatule à chaque étape ; ils sont ici écrits en ligne, du dessus (à gauche) vers le fond (à droite).

Dans notre algorithme, on définira notre tas de crêpes par une pile d'entiers.

1. Définir une structure `Crepe` qui contient un entier (le diamètre de la crêpe) et un pointeur vers la crêpe suivante : cette structure permet donc d'avoir une liste chaînée de crêpes. Définir également un nouveau type `Pcrepe`, pointeur sur `Crepe`.
2. Créer une fonction `Pcrepe inserFile(Pcrepe tete, Crepe c)` qui simule l'insertion d'une crêpe dans une FILE dont la tête est pointée par `tete`.
3. Créer une fonction `Pcrepe suppFile(Pcrepe tete)` qui simule le retrait d'une crêpe dans une FILE dont la tête est pointée par `tete`.
4. Créer une fonction `Pcrepe inserPile(Pcrepe tete)` qui simule l'insertion d'une crêpe dans une PILE dont la tête est pointée par `tete`.
5. Créer une fonction `Pcrepe suppPile(Pcrepe tete)` qui simule le retrait d'une crêpe dans une PILE dont le premier élément est pointé par `tete`.
6. Créer une fonction `int triCrepe(Pcrepe tete)` qui retourne 1 si la PILE de crêpes dont la tête est indiquée par `tete` est triée par ordre croissant, 0 sinon.
7. Créer une fonction `Pcrepe invCrepe(Pcrepe tete, int M)` qui va inverser les M premiers éléments d'une PILE (on pourra utiliser une FILE temporaire pour cela) et qui retourne la nouvelle tête de la pile.
8. Créer une fonction `int indMax(Pcrepe tete)` qui retourne l'indice de l'élément le plus grand d'une PILE de crêpes (-1 si la pile est vide).
9. Créer une fonction `Pcrepe spatule(Pcrepe tete, int M)` qui va rechercher la crêpe la plus grande parmi les M premiers éléments d'une PILE et qui va inverser ces M éléments. La fonction retourne le pointeur sur la tête de la PILE modifiée.
10. Créer une fonction ou procédure qui va utiliser les fonctions précédentes afin de réaliser l'objectif demandé : à partir d'une PILE de crêpes quelconque, placer une à une, dans l'ordre, les crêpes les plus grandes tout en bas de la pile.

> **Note :** le document écrit `Pcrepre` au lieu de `Pcrepe` dans plusieurs prototypes ; c'est corrigé ici.
