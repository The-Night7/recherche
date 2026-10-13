---
source: TD05-ABR_2023-2024_Informatique3_P2S1_DInformatique.pdf, page 1 (identique à TD5-ABR_2022-2023)
transcription: manuelle
corrections: rédigées
---

# TD 05 : Arbres binaires de recherche (corrigé)

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

> **Complément :** le document d'origine ne contient que les énoncés ; toutes les corrections ont été rédigées pour cette transcription. Les codes C99 ont été compilés avec `gcc -std=c99 -Wall -Wextra` et testés. Comme dans le cours, un ABR contient des éléments **uniques** : les valeurs du sous-arbre gauche sont strictement inférieures à la racine, celles du sous-arbre droit strictement supérieures.

## Exercice 1 : Question de cours

**Énoncé.**

1. Construire un arbre binaire de recherche en insérant les éléments dans cet ordre : 10, 3, 5, 15, 20, 12, 7, 45, 9.
2. Construire un second arbre binaire de recherche en insérant les éléments dans l'ordre inverse du précédent. Obtient-on le même arbre ?
3. Effectuer un parcours infixe sur ces deux arbres. Que remarque-t-on ?
4. Supprimer l'élément 5 puis 12 du premier arbre.

**Correction.**

**1.** Chaque élément descend depuis la racine (à gauche s'il est plus petit, à droite s'il est plus grand) jusqu'à une place vide. Par exemple 9 : $9 < 10$ à gauche, $9 > 3$ à droite, $9 > 5$ à droite, $9 > 7$ à droite.

```
        10
      /    \
     3      15
      \    /  \
       5  12   20
        \        \
         7        45
          \
           9
```

**2.** Ordre inverse : 9, 45, 7, 12, 20, 15, 5, 3, 10.

```
          9
       /     \
      7       45
     /       /
    5       12
   /       /  \
  3       10   20
               /
              15
```

Ce n'est **pas** le même arbre (la racine est 9 et non 10) : la forme d'un ABR dépend de l'ordre d'insertion.

**3.** Les deux parcours infixes (gauche, racine, droite) donnent `3 5 7 9 10 12 15 20 45`. Le parcours infixe d'un ABR donne toujours ses éléments **dans l'ordre croissant**, quelle que soit sa forme.

**4.** Suppression de 5 : il n'a qu'un fils (7, à droite), on le remplace par ce fils. Suppression de 12 : c'est une feuille, on la retire.

```
        10
      /    \
     3      15
      \       \
       7       20
        \        \
         9        45
```

(Pour un nœud à deux fils, on le remplacerait par son prédécesseur, le maximum de son sous-arbre gauche : voir l'exercice 2.)

## Exercice 2 : Construction d'un ABR

**Énoncé.** Les versions pseudo-code des fonctions demandées aux questions 2, 3 et 5 sont dans le cours.

1. Définir la structure permettant de construire un arbre binaire contenant des entiers.
2. Écrire la fonction `recherche(pArbre a, int e)` indiquant si l'élément `e` appartient à l'ABR pointé par `a`.
3. Écrire la fonction récursive `insertABR(pArbre a, int e)` permettant d'insérer l'élément `e` dans l'ABR. Attention, l'insertion doit respecter les règles des ABR !
4. Écrire une version itérative de la fonction d'insertion écrite précédemment.
5. Écrire les fonctions nécessaires à la suppression d'un élément dans un ABR.
6. Créer un ABR et insérer les éléments suivants dans cet ordre : 10, 3, 5, 15, 20, 12, 7, 45, 9. Afficher l'arbre et vérifier qu'il s'agit bien d'un ABR.
7. Vérifier si les éléments 13 et 12 appartiennent à l'arbre.
8. Supprimer l'élément 15 et vérifier que l'arbre est toujours un ABR.

**Correction.**

**1.**

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

typedef struct Arbre {
    int elmt;
    struct Arbre *fg;
    struct Arbre *fd;
} Arbre;

typedef Arbre *pArbre;

pArbre creerArbre(int e) {
    pArbre a = malloc(sizeof(Arbre));
    if (a == NULL) {
        fprintf(stderr, "Erreur d'allocation\n");
        exit(EXIT_FAILURE);
    }
    a->elmt = e;
    a->fg = NULL;
    a->fd = NULL;
    return a;
}
```

**2.** On ne descend que dans **un** sous-arbre : le coût est proportionnel à la hauteur $h$, soit $O(\log n)$ pour un arbre équilibré et $O(n)$ dans le pire cas (arbre filiforme).

```c
int recherche(pArbre a, int e) {
    if (a == NULL) {
        return 0;
    }
    if (a->elmt == e) {
        return 1;
    }
    if (e < a->elmt) {
        return recherche(a->fg, e);
    }
    return recherche(a->fd, e);
}
```

**3.** On retourne la racine (elle change quand l'arbre est vide). Si `e` est déjà présent, on ne fait rien.

```c
pArbre insertABR(pArbre a, int e) {
    if (a == NULL) {
        return creerArbre(e);
    }
    if (e < a->elmt) {
        a->fg = insertABR(a->fg, e);
    } else if (e > a->elmt) {
        a->fd = insertABR(a->fd, e);
    }
    return a;
}
```

**4.** On descend avec un pointeur jusqu'au nœud dont le fils voulu est vide, et on y accroche le nouveau nœud.

```c
pArbre insertABRIter(pArbre a, int e) {
    if (a == NULL) {
        return creerArbre(e);
    }
    pArbre p = a;
    while (1) {
        if (e == p->elmt) {
            return a;                        /* déjà présent */
        } else if (e < p->elmt) {
            if (p->fg == NULL) {
                p->fg = creerArbre(e);
                return a;
            }
            p = p->fg;
        } else {
            if (p->fd == NULL) {
                p->fd = creerArbre(e);
                return a;
            }
            p = p->fd;
        }
    }
}
```

**5.** Algorithme du cours : on cherche `e` ; s'il n'a pas de fils gauche, on le remplace par son fils droit (éventuellement vide) ; sinon on le remplace par son **prédécesseur**, le maximum de son sous-arbre gauche, que `suppMax` retire et renvoie par l'adresse `pe`. Ce maximum est le nœud le plus à droite ; il n'a pas de fils droit, on le remplace donc par son fils gauche.

```c
pArbre suppMax(pArbre a, int *pe) {          /* a non vide */
    if (a->fd != NULL) {
        a->fd = suppMax(a->fd, pe);
        return a;
    }
    *pe = a->elmt;
    pArbre g = a->fg;
    free(a);
    return g;
}

pArbre suppression(pArbre a, int e) {
    if (a == NULL) {
        return NULL;                         /* e absent : rien à faire */
    }
    if (e > a->elmt) {
        a->fd = suppression(a->fd, e);
    } else if (e < a->elmt) {
        a->fg = suppression(a->fg, e);
    } else if (a->fg == NULL) {
        pArbre d = a->fd;
        free(a);
        return d;
    } else {
        a->fg = suppMax(a->fg, &a->elmt);    /* le prédécesseur prend la place de e */
    }
    return a;
}
```

**6.** Pour afficher la forme de l'arbre, on l'imprime « couché » (sous-arbre droit en haut, décalage proportionnel à la profondeur) ; l'infixe croissant et la fonction `estABR` de l'exercice 4 confirment que c'est un ABR.

```c
void affiche(pArbre a, int niveau) {
    if (a == NULL) {
        return;
    }
    affiche(a->fd, niveau + 1);
    for (int i = 0; i < niveau; i++) {
        printf("    ");
    }
    printf("%d\n", a->elmt);
    affiche(a->fg, niveau + 1);
}

void infixe(pArbre a) {
    if (a == NULL) {
        return;
    }
    infixe(a->fg);
    printf("%d ", a->elmt);
    infixe(a->fd);
}

void liberer(pArbre a) {
    if (a == NULL) {
        return;
    }
    liberer(a->fg);
    liberer(a->fd);
    free(a);
}

int main(void) {
    int v[] = {10, 3, 5, 15, 20, 12, 7, 45, 9};
    pArbre a = NULL;
    for (int i = 0; i < 9; i++) {
        a = insertABR(a, v[i]);
    }
    affiche(a, 0);
    infixe(a);                                       /* 3 5 7 9 10 12 15 20 45 */
    printf("\n13 : %d, 12 : %d\n", recherche(a, 13), recherche(a, 12));
    a = suppression(a, 15);
    affiche(a, 0);
    liberer(a);
    return 0;
}
```

On obtient l'arbre de l'exercice 1, question 1.

**7.** `recherche(a, 13)` vaut 0 (13 est absent : $13 > 10$, $13 < 15$, $13 > 12$, fils droit de 12 vide) et `recherche(a, 12)` vaut 1.

**8.** 15 a deux fils : il est remplacé par le maximum de son sous-arbre gauche, 12 (qui est une feuille). Résultat :

```
        10
      /    \
     3      12
      \       \
       5       20
        \        \
         7        45
          \
           9
```

Le parcours infixe `3 5 7 9 10 12 20 45` est toujours croissant : c'est encore un ABR.

## Exercice 3 : Test des fonctions de recherche

**Énoncé.** Pour cet exercice, on travaille sur l'arbre construit dans l'exercice précédent.

1. Modifier la fonction `recherche(pArbre a, int e)` pour qu'elle retourne le nombre de nœuds qui auront été parcourus lors de cette recherche. Si un élément n'appartient pas à l'arbre, on affichera que l'élément recherché n'existe pas, mais on retournera tout de même le nombre de nœuds visités.
2. Proposer une modification de la fonction de parcours préfixe de l'arbre pour que cette dernière serve à rechercher si un élément existe dans l'arbre, en parcourant l'arbre et en s'arrêtant lorsque l'élément est trouvé. Comme pour la question précédente, la fonction doit afficher le nombre de nœuds parcourus.
3. Afficher le nombre de nœuds parcourus pour les deux fonctions lors de la recherche des éléments suivants : 10, 20, 22.

> **Note :** on utilise l'arbre complet de la question 6 de l'exercice 2 (avant la suppression de 15).

**Correction.**

**1.** Version itérative : on compte chaque nœud visité le long du chemin.

```c
int rechercheCompte(pArbre a, int e) {
    int nb = 0;
    while (a != NULL) {
        nb++;
        if (a->elmt == e) {
            return nb;
        }
        a = (e < a->elmt) ? a->fg : a->fd;
    }
    printf("%d n'existe pas dans l'arbre\n", e);
    return nb;
}
```

**2.** Le parcours préfixe n'utilise pas l'ordre de l'ABR : il visite la racine, puis tout le sous-arbre gauche, puis le droit. Grâce à l'évaluation paresseuse de `||`, le sous-arbre droit n'est pas exploré si l'élément a été trouvé à gauche. Le compteur est passé par adresse.

```c
int prefixeRecherche(pArbre a, int e, int *nb) {
    if (a == NULL) {
        return 0;
    }
    (*nb)++;
    if (a->elmt == e) {
        return 1;
    }
    return prefixeRecherche(a->fg, e, nb) || prefixeRecherche(a->fd, e, nb);
}

int rechercheParPrefixe(pArbre a, int e) {
    int nb = 0;
    if (!prefixeRecherche(a, e, &nb)) {
        printf("%d n'existe pas dans l'arbre\n", e);
    }
    return nb;
}
```

**3.** L'ordre préfixe de l'arbre est `10 3 5 7 9 15 12 20 45`.

- 10 : recherche ABR **1** nœud (la racine) ; préfixe **1** nœud.
- 20 : recherche ABR **3** nœuds (10, 15, 20) ; préfixe **8** nœuds (20 est le 8e de l'ordre préfixe).
- 22 : absent ; recherche ABR **4** nœuds (10, 15, 20, 45, puis fils gauche de 45 vide) ; préfixe **9** nœuds (tout l'arbre).

La recherche dans un ABR suit un seul chemin (au plus $h + 1$ nœuds) alors que le parcours préfixe peut visiter tout l'arbre ($n$ nœuds).

## Exercice 4 : ABR ?

**Énoncé.** Proposer une fonction permettant de vérifier si un arbre binaire est un ABR ou non.

**Correction.**

Il ne suffit pas de comparer chaque nœud avec ses deux fils : dans l'arbre `10 -> fg 5 -> fd 12`, chaque père est bien placé par rapport à ses fils, mais 12 est dans le sous-arbre gauche de 10. Il faut que **toutes** les valeurs du sous-arbre gauche soient inférieures à la racine.

Méthode : on descend en transmettant l'intervalle ouvert $]\min, \max[$ dans lequel doivent se trouver les valeurs du sous-arbre. En allant à gauche d'un nœud $x$, la borne supérieure devient $x$ ; à droite, la borne inférieure devient $x$. On utilise des `long long` pour pouvoir partir de bornes strictement en dehors des valeurs possibles d'un `int`. Chaque nœud est visité une fois : $O(n)$.

```c
int estABRBornes(pArbre a, long long min, long long max) {
    if (a == NULL) {
        return 1;
    }
    if (a->elmt <= min || a->elmt >= max) {
        return 0;
    }
    return estABRBornes(a->fg, min, a->elmt) && estABRBornes(a->fd, a->elmt, max);
}

int estABR(pArbre a) {
    return estABRBornes(a, (long long)INT_MIN - 1, (long long)INT_MAX + 1);
}
```

Autre méthode équivalente : vérifier que le parcours infixe est strictement croissant. Tests : l'arbre de l'exercice 2 donne 1, l'arbre `10 -> fg 5 -> fd 12` donne 0.

## Exercice 5 : D'arbre binaire à ABR

**Énoncé.** Proposer une ou plusieurs fonctions qui permettent de construire un ABR à partir d'un arbre binaire simple.

**Correction.**

On parcourt l'arbre binaire (ici en préfixe) et on insère chaque élément dans un nouvel ABR, initialement vide. Les doublons éventuels ne sont insérés qu'une fois. L'arbre d'origine n'est pas modifié (il faudra libérer les deux arbres).

```c
pArbre ajouterTous(pArbre abr, pArbre a) {
    if (a == NULL) {
        return abr;
    }
    abr = insertABR(abr, a->elmt);
    abr = ajouterTous(abr, a->fg);
    abr = ajouterTous(abr, a->fd);
    return abr;
}

pArbre versABR(pArbre a) {
    return ajouterTous(NULL, a);
}
```

Coût : $n$ insertions, soit $O(n \log n)$ si l'ABR reste à peu près équilibré et $O(n^2)$ dans le pire cas. Autre méthode : copier les éléments dans un tableau, le trier, puis construire un ABR **équilibré** en prenant l'élément du milieu comme racine et en recommençant récursivement sur chaque moitié.

## Exercice 6 : Tri de tableau

**Énoncé.**

1. Déclarer un tableau de taille 15 et le remplir avec des valeurs saisies différentes.
2. Construire un ABR à partir de ce tableau.
3. Trier ce tableau en vous basant sur un parcours de l'ABR.
4. Bonus : reprendre la question 1, mais les valeurs du tableau sont aléatoires entre 0 et 100 et ne doivent pas avoir de doublons !

**Correction.**

**1.** Saisie en refusant les doublons (on les détecte avec l'ABR lui-même, ce qui prépare la question 2).

```c
#define TAILLE 15

pArbre saisirTableau(int *tab, int n) {
    pArbre abr = NULL;
    int k = 0;
    while (k < n) {
        int x;
        printf("Valeur %d : ", k + 1);
        if (scanf("%d", &x) != 1) {
            while (getchar() != '\n') {
            }                              /* vide la saisie invalide */
            continue;
        }
        if (recherche(abr, x)) {
            printf("Valeur déjà saisie\n");
        } else {
            tab[k] = x;
            k++;
            abr = insertABR(abr, x);
        }
    }
    return abr;
}
```

**2. et 3.** L'ABR est construit en insérant les cases une à une (fait ci-dessus, ou avec la boucle de `triABR` ci-dessous). Le **parcours infixe** donne les valeurs dans l'ordre croissant : on les réécrit dans le tableau avec un indice passé par adresse.

```c
void remplirInfixe(pArbre a, int *tab, int *i) {
    if (a == NULL) {
        return;
    }
    remplirInfixe(a->fg, tab, i);
    tab[*i] = a->elmt;
    (*i)++;
    remplirInfixe(a->fd, tab, i);
}

void triABR(int *tab, int n) {
    pArbre abr = NULL;
    for (int k = 0; k < n; k++) {
        abr = insertABR(abr, tab[k]);
    }
    int i = 0;
    remplirInfixe(abr, tab, &i);
    liberer(abr);
}
```

Ce « tri par ABR » coûte $O(n \log n)$ en moyenne et $O(n^2)$ dans le pire cas (tableau déjà trié : l'arbre est filiforme). Il suppose des valeurs distinctes, sinon les doublons seraient perdus.

**4.** On tire des valeurs avec `rand() % 101` et on rejette celles déjà tirées (il faut $n \le 101$ pour que la boucle termine).

```c
void remplirAleatoireSansDoublon(int *tab, int n) {
    pArbre deja = NULL;
    int k = 0;
    while (k < n) {
        int x = rand() % 101;
        if (!recherche(deja, x)) {
            deja = insertABR(deja, x);
            tab[k] = x;
            k++;
        }
    }
    liberer(deja);
}
```

Exemple testé : `61 42 67 27 17 75 56 93 76 46 63 55 70 59 98` devient, après `triABR`, `17 27 42 46 55 56 59 61 63 67 70 75 76 93 98`.
