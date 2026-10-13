---
source: TD3-Pile-File-Listes_2022-2023_Informatique3_P2S1_DInformatique.pdf, pages 1-2
transcription: manuelle
corrections: rédigées
---

# TD 03 : Piles et files (2) (corrigé)

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

> **Complément :** le document d'origine ne contient que les énoncés ; toutes les corrections ont été rédigées pour cette transcription. Les codes C99 ont été compilés avec `gcc -std=c99 -Wall -Wextra` et testés.

## Exercice 1 : Liste doublement chaînée

**Énoncé.** On rappelle que les chaînons des listes doublement chaînées possèdent un pointeur vers le chaînon suivant et un pointeur vers le chaînon précédent. Il est donc possible de parcourir une telle liste dans les deux sens.

1. Déclarer une structure de liste doublement chaînée permettant de stocker des mots de 20 caractères maximum.
2. Écrire une fonction `compareMot(char *mot1, char *mot2)` qui retourne 1 si `mot1` est avant `mot2` dans l'ordre alphabétique et 0 sinon.
3. Écrire une fonction `insertListe(char *mot1, liste *pliste)` qui ajoute à la liste doublement chaînée pointée par `pliste`, de mots classés dans l'ordre alphabétique, un nouveau chaînon contenant `mot1`.
4. Écrire une procédure `affiche(liste *pliste)` qui affiche dans l'ordre les mots contenus dans la liste.
5. Écrire une procédure `afficheInv(liste *pliste)` qui affiche dans l'ordre inverse les mots contenus dans la liste.
6. Déclarer une nouvelle liste et la remplir avec une vingtaine de mots. Afficher cette liste de mots dans l'ordre alphabétique et anti-alphabétique.

**Correction.**

**1.** Un mot de 20 caractères occupe 21 octets avec le `'\0'` final. La structure `liste` garde la tête **et** la queue, pour pouvoir parcourir dans les deux sens.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXMOT 20

typedef struct Chainon {
    char mot[MAXMOT + 1];
    struct Chainon *prec;
    struct Chainon *suiv;
} Chainon;

typedef struct {
    Chainon *tete;
    Chainon *queue;
} liste;
```

Une liste vide se déclare `liste l = {NULL, NULL};`.

**2.** `strcmp(a, b)` est strictement négatif si `a` est avant `b` dans l'ordre lexicographique (ordre des codes ASCII, donc correct pour des mots en minuscules sans accents).

```c
int compareMot(char *mot1, char *mot2) {
    return strcmp(mot1, mot2) < 0;
}
```

**3.** On cherche le premier chaînon `p` dont le mot n'est **pas** avant le nouveau, et on insère juste avant `p`. Les quatre cas (liste vide, en tête, au milieu, en fin) se ramènent à deux tests : `p == NULL` (insertion en fin, la queue change) et `c->prec == NULL` (insertion en tête, la tête change). Il faut mettre à jour **les deux** liens de chaque voisin, sinon le parcours à l'envers est faux. Les doublons sont acceptés (insérés devant le mot égal).

```c
int insertListe(char *mot1, liste *pliste) {
    if (mot1 == NULL || pliste == NULL) {
        return 0;
    }
    Chainon *c = malloc(sizeof(Chainon));
    if (c == NULL) {
        return 0;
    }
    strncpy(c->mot, mot1, MAXMOT);
    c->mot[MAXMOT] = '\0';             /* tronque à 20 caractères */

    Chainon *p = pliste->tete;
    while (p != NULL && compareMot(p->mot, c->mot)) {
        p = p->suiv;
    }
    c->suiv = p;                       /* c se place juste avant p */
    if (p == NULL) {                   /* en fin (ou liste vide) */
        c->prec = pliste->queue;
        pliste->queue = c;
    } else {
        c->prec = p->prec;
        p->prec = c;
    }
    if (c->prec == NULL) {             /* en tête */
        pliste->tete = c;
    } else {
        c->prec->suiv = c;
    }
    return 1;
}
```

**4. et 5.** Parcours de la tête vers la queue avec `suiv`, ou de la queue vers la tête avec `prec`.

```c
void affiche(liste *pliste) {
    for (Chainon *p = pliste->tete; p != NULL; p = p->suiv) {
        printf("%s ", p->mot);
    }
    printf("\n");
}

void afficheInv(liste *pliste) {
    for (Chainon *p = pliste->queue; p != NULL; p = p->prec) {
        printf("%s ", p->mot);
    }
    printf("\n");
}
```

**6.**

```c
void libereListe(liste *pliste) {
    Chainon *p = pliste->tete;
    while (p != NULL) {
        Chainon *s = p->suiv;
        free(p);
        p = s;
    }
    pliste->tete = NULL;
    pliste->queue = NULL;
}

int main(void) {
    liste l = {NULL, NULL};
    char *mots[] = {"pile", "file", "arbre", "zebre", "chat", "noeud", "liste",
                    "arbre", "maison", "banane", "tete", "queue", "racine",
                    "feuille", "hauteur", "avl", "rotation", "pointeur",
                    "malloc", "structure"};
    for (int i = 0; i < 20; i++) {
        insertListe(mots[i], &l);
    }
    affiche(&l);
    afficheInv(&l);
    libereListe(&l);
    return 0;
}
```

Sortie : `arbre arbre avl banane chat feuille file hauteur liste maison malloc noeud pile pointeur queue racine rotation structure tete zebre`, puis la même liste à l'envers.

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

**Correction.**

**1.**

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Crepe {
    int diametre;
    struct Crepe *suivant;
} Crepe;

typedef Crepe *Pcrepe;

Pcrepe nouvelleCrepe(Crepe c) {
    Pcrepe n = malloc(sizeof(Crepe));
    if (n == NULL) {
        fprintf(stderr, "Erreur d'allocation\n");
        exit(EXIT_FAILURE);
    }
    n->diametre = c.diametre;
    n->suivant = NULL;
    return n;
}
```

**2. et 3.** Avec seulement un pointeur de tête, une file s'implémente en ajoutant **en fin** (parcours en $O(n)$) et en retirant **en tête** ($O(1)$). On alloue une copie de la crêpe `c` reçue par valeur ; le retrait libère la crêpe.

```c
Pcrepe inserFile(Pcrepe tete, Crepe c) {
    Pcrepe n = nouvelleCrepe(c);
    if (tete == NULL) {
        return n;
    }
    Pcrepe p = tete;
    while (p->suivant != NULL) {
        p = p->suivant;
    }
    p->suivant = n;
    return tete;
}

Pcrepe suppFile(Pcrepe tete) {
    if (tete == NULL) {
        return NULL;
    }
    Pcrepe s = tete->suivant;
    free(tete);
    return s;
}
```

**4. et 5.** Pour une pile, ajout et retrait se font en tête. Le retrait est donc exactement le même que pour la file.

> **Erreur corrigée :** le prototype `Pcrepe inserPile(Pcrepe tete)` de l'énoncé ne reçoit pas la crêpe à insérer ; on ajoute le paramètre `Crepe c`, comme pour `inserFile`.

```c
Pcrepe inserPile(Pcrepe tete, Crepe c) {
    Pcrepe n = nouvelleCrepe(c);
    n->suivant = tete;
    return n;
}

Pcrepe suppPile(Pcrepe tete) {
    return suppFile(tete);
}
```

**6.** Le tas est trié si chaque crêpe est plus petite (ou égale) que celle du dessous. Une pile vide ou d'une crêpe est triée.

```c
int triCrepe(Pcrepe tete) {
    for (Pcrepe p = tete; p != NULL && p->suivant != NULL; p = p->suivant) {
        if (p->diametre > p->suivant->diametre) {
            return 0;
        }
    }
    return 1;
}
```

**7.** On dépile les M crêpes du dessus en les enfilant : la file contient alors, de la tête à la queue, l'ancien sommet puis les suivantes. On les défile et on les rempile dans cet ordre : l'ancien sommet est rempilé en premier, il se retrouve le plus bas des M ; l'ordre est bien inversé. Si la pile a moins de M crêpes, on inverse toute la pile.

```c
Pcrepe invCrepe(Pcrepe tete, int M) {
    Pcrepe file = NULL;
    for (int i = 0; i < M && tete != NULL; i++) {
        Crepe c = *tete;
        tete = suppPile(tete);
        file = inserFile(file, c);
    }
    while (file != NULL) {
        Crepe c = *file;
        file = suppFile(file);
        tete = inserPile(tete, c);
    }
    return tete;
}
```

**8.** On numérote à partir de 0 depuis le sommet. On écrit une version qui ne regarde que les M premières crêpes (utile pour la question 9) ; `indMax` l'appelle sans limite.

```c
int indMaxN(Pcrepe tete, int M) {
    if (tete == NULL || M <= 0) {
        return -1;
    }
    int iMax = 0;
    int max = tete->diametre;
    int i = 0;
    for (Pcrepe p = tete; p != NULL && i < M; p = p->suivant, i++) {
        if (p->diametre > max) {
            max = p->diametre;
            iMax = i;
        }
    }
    return iMax;
}

int indMax(Pcrepe tete) {
    return indMaxN(tete, INT_MAX);
}
```

**9.** Deux coups de spatule : sous la plus grande (indice $i$, donc $i+1$ crêpes retournées), elle remonte au sommet ; puis sous la M-ième crêpe, elle descend en position M.

```c
Pcrepe spatule(Pcrepe tete, int M) {
    int i = indMaxN(tete, M);
    if (i < 0) {
        return tete;
    }
    tete = invCrepe(tete, i + 1);
    tete = invCrepe(tete, M);
    return tete;
}
```

**10.** Pour M allant du nombre total de crêpes jusqu'à 2, on place la plus grande des M premières en position M ; on s'arrête dès que le tas est trié.

```c
void affichePile(Pcrepe tete) {
    for (Pcrepe p = tete; p != NULL; p = p->suivant) {
        printf("%d ", p->diametre);
    }
    printf("\n");
}

Pcrepe triTas(Pcrepe tete) {
    int n = 0;
    for (Pcrepe p = tete; p != NULL; p = p->suivant) {
        n++;
    }
    for (int M = n; M > 1 && !triCrepe(tete); M--) {
        tete = spatule(tete, M);
        affichePile(tete);
    }
    return tete;
}

int main(void) {
    int t[] = {3, 6, 2, 9, 7, 4, 5};          /* du dessus vers le fond */
    Pcrepe pile = NULL;
    for (int i = 6; i >= 0; i--) {            /* on empile d'abord le fond */
        Crepe c = {t[i], NULL};
        pile = inserPile(pile, c);
    }
    pile = triTas(pile);
    while (pile != NULL) {                    /* libération */
        pile = suppPile(pile);
    }
    return 0;
}
```

Sur l'exemple, le programme affiche `5 4 7 3 6 2 9`, `2 6 3 5 4 7 9`, `4 5 3 2 6 7 9`, `2 3 4 5 6 7 9` : ce sont exactement les tas obtenus après chaque paire de coups de spatule dans l'énoncé. Pour n crêpes, il faut au plus $2(n-1)$ coups de spatule.
