---
source: TD06-AVL_2023-2024_Informatique3_P2S1_DInformatique.pdf, pages 1-2 (identique à TD6-AVL_2022-2023)
transcription: manuelle
corrections: rédigées
---

# TD 06 : Arbres AVL (corrigé)

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

> **Note :** l'en-tête du document porte le titre « TD 04 : Arbres AVL » ; il s'agit du sixième TD (les AVL suivent les ABR).

> **Complément :** le document d'origine ne contient que les énoncés ; toutes les corrections ont été rédigées pour cette transcription. Les codes C99 ont été compilés avec `gcc -std=c99 -Wall -Wextra` et testés (y compris par des milliers d'insertions et suppressions aléatoires, en vérifiant après chacune que l'arbre est un ABR, que tous les facteurs d'équilibre sont exacts et compris entre -1 et 1).

## Exercice 1 : Question de cours

**Énoncé.**

1. Construire un AVL en insérant les éléments dans cet ordre : 10, 3, 5, 15, 20, 12, 7, 9.
2. Construire un second AVL en insérant les éléments dans l'ordre inverse du précédent.
3. Effectuer un parcours infixe sur ces deux arbres. Que remarque-t-on ?
4. Supprimer l'élément 5 puis 12 du premier arbre. Redessiner l'arbre obtenu après chacune des suppressions.

**Correction.**

Rappels : le facteur d'équilibre d'un nœud est $\text{eq} = h(\text{sous-arbre droit}) - h(\text{sous-arbre gauche})$ ; un AVL impose $\text{eq} \in \{-1, 0, 1\}$ en tout nœud. Après une insertion, on remonte vers la racine en mettant à jour les équilibres ; au premier nœud où $|\text{eq}| = 2$ on fait :

- $\text{eq} = +2$ et fils droit d'équilibre $\ge 0$ : rotation gauche ;
- $\text{eq} = +2$ et fils droit d'équilibre $-1$ : double rotation gauche (rotation droite du fils droit, puis rotation gauche) ;
- symétriquement à gauche avec $\text{eq} = -2$.

Dans les schémas, chaque nœud est noté `valeur(équilibre)`.

**1.** Insertions de 10, 3, 5, 15, 20, 12, 7, 9 :

- 10, puis 3 : `10(-1)` avec 3 à gauche.
- 5 : il va à droite de 3. Alors 3 a l'équilibre $+1$ et 10 l'équilibre $-2$, avec un fils gauche d'équilibre $+1$ : **double rotation droite** en 10. Racine 5, fils 3 et 10.
- 15 : à droite de 10. Équilibres : 10 $(+1)$, 5 $(+1)$.
- 20 : à droite de 15. 10 passe à $+2$ avec un fils droit $(+1)$ : **rotation gauche** en 10. Le sous-arbre droit de 5 devient 15, de fils 10 et 20.
- 12 : $12 > 5$, $12 < 15$, $12 > 10$ : à droite de 10. Équilibres : 10 $(+1)$, 15 $(-1)$, 5 $(+2)$ avec un fils droit $(-1)$ : **double rotation gauche** en 5 (rotation droite en 15, puis rotation gauche en 5). Racine 10.

```
            10(0)
          /       \
       5(-1)      15(0)
       /         /    \
     3(0)     12(0)   20(0)
```

- 7 : à droite de 5, qui devient équilibré ; pas de rotation.
- 9 : à droite de 7. Équilibres : 7 $(+1)$, 5 $(+1)$, 10 $(-1)$ ; pas de rotation.

Premier AVL :

```
               10(-1)
            /          \
         5(+1)          15(0)
        /     \        /     \
     3(0)    7(+1)   12(0)   20(0)
                \
                9(0)
```

**2.** Insertions de 9, 7, 12, 20, 15, 5, 3, 10 :

- 9, 7, 12 : racine 9, fils 7 et 12, équilibré.
- 20 : à droite de 12 ; équilibres 12 $(+1)$, 9 $(+1)$.
- 15 : à gauche de 20. 20 $(-1)$, 12 $(+2)$ avec un fils droit $(-1)$ : **double rotation gauche** en 12. Le sous-arbre droit de 9 devient 15, de fils 12 et 20.
- 5 : à gauche de 7 ; équilibres 7 $(-1)$, 9 $(0)$.
- 3 : à gauche de 5. 7 passe à $-2$ avec un fils gauche $(-1)$ : **rotation droite** en 7. Le sous-arbre gauche de 9 devient 5, de fils 3 et 7.
- 10 : $10 > 9$, $10 < 15$, $10 < 12$ : à gauche de 12. Équilibres 12 $(-1)$, 15 $(-1)$, 9 $(+1)$ ; pas de rotation.

Second AVL :

```
                9(+1)
             /         \
          5(0)          15(-1)
         /    \        /      \
      3(0)   7(0)   12(-1)    20(0)
                    /
                 10(0)
```

Les deux arbres sont différents : comme pour les ABR, la forme dépend de l'ordre d'insertion.

**3.** Les deux parcours infixes donnent `3 5 7 9 10 12 15 20` : un AVL est un ABR, son parcours infixe est croissant. Les rotations préservent cet ordre.

**4.** Suppression de 5 dans le premier arbre (algorithme du cours : un nœud qui a un fils droit est remplacé par son **successeur**, le minimum de son sous-arbre droit). Le successeur de 5 est 7 : 7 prend la place de 5 et son ancien nœud est remplacé par son fils 9. Le sous-arbre gauche de 10 garde la hauteur 1, rien d'autre ne change.

```
              10(0)
            /       \
         7(0)       15(0)
        /    \      /    \
     3(0)   9(0) 12(0)  20(0)
```

Suppression de 12 : c'est une feuille. 15 passe à l'équilibre $+1$ ; la hauteur du sous-arbre de 15 ne change pas, donc 10 reste à 0. Aucune rotation.

```
              10(0)
            /       \
         7(0)       15(+1)
        /    \          \
     3(0)   9(0)        20(0)
```

## Exercice 2 : Construction d'un AVL

**Énoncé.** Les versions pseudo-code des fonctions demandées sont dans le cours.

1. On rappelle que pour construire un AVL, chaque nœud de l'arbre doit être associé à un facteur d'équilibrage dont la valeur est : équilibre = hauteur du sous-arbre droit - hauteur du sous-arbre gauche. Modifier la structure `Arbre` pour inclure ce nouveau champ.
2. Réécrire la fonction `creerArbre(x : Element)` pour inclure également ce nouveau champ et l'initialiser à la création d'un nouveau nœud de l'arbre.
3. Les opérations de rééquilibrage s'effectuent à l'aide de « rotations » des sous-arbres (cf. cours). Écrire les fonctions `RotationGauche(A : Arbre)` permettant de faire la rotation du sous-arbre A avec son fils droit, et `RotationDroite(A : Arbre)` permettant de faire la rotation du sous-arbre A avec son fils gauche.
4. Tester ces deux fonctions sur les deux arbres suivants (que vous aurez construits manuellement avec les fonctions `ajouterFilsDroit` et `ajouterFilsGauche`, en prenant soin d'indiquer les bonnes valeurs d'élément ET d'équilibre pour chaque nœud) :

```
   1                    3
    \                  /
     2                2
      \              /
       3            1
```

5. À partir des fonctions précédentes, écrire les fonctions permettant d'effectuer les doubles rotations : `DoubleRotationDroite(A : Arbre)` et `DoubleRotationGauche(A : Arbre)`.
6. Tester une de ces fonctions (la plus adaptée !) sur l'arbre suivant (construit manuellement de la même façon) :

```
          10
        /    \
       5      20
            /    \
          15      26
         /  \
       13    17
```

7. Écrire la fonction `equilibrerAVL(A : Arbre)` qui permet d'effectuer la bonne rotation de l'arbre en fonction du facteur d'équilibrage de A et de ses fils.
8. Écrire la fonction `insertionAVL(A : Arbre, e : Element, h : pointeur sur entier)` qui insère dans l'arbre un nouveau nœud contenant l'élément `e`. L'insertion de l'élément est basée sur le même principe que l'insertion dans un ABR. Il faut cependant veiller à mettre à jour le facteur d'équilibrage de chaque nœud (dont l'évolution est gérée par le paramètre `h`) et à rééquilibrer l'arbre si besoin à l'aide de la fonction `equilibrerAVL`.
9. Écrire la fonction `suppAVL(A : Arbre, e : Element, h : pointeur sur entier)` permettant de supprimer un nœud contenant l'élément `e` de l'arbre A. Le raisonnement est le même que pour la question précédente.

**Correction.**

**1. et 2.** Un nouveau nœud est une feuille : ses deux sous-arbres sont vides, son équilibre vaut 0.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Arbre {
    int elmt;
    int equilibre;              /* hauteur(fd) - hauteur(fg) */
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
    a->equilibre = 0;
    a->fg = NULL;
    a->fd = NULL;
    return a;
}

int min2(int a, int b) { return a < b ? a : b; }
int max2(int a, int b) { return a > b ? a : b; }
int min3(int a, int b, int c) { return min2(a, min2(b, c)); }
int max3(int a, int b, int c) { return max2(a, max2(b, c)); }
```

**3.** Rotation gauche de A : son fils droit P (le pivot) devient la racine, A devient le fils gauche de P, et l'ancien sous-arbre gauche de P devient le sous-arbre droit de A. L'ordre infixe est conservé.

```
       A                    P
      / \                  / \
     x   P       ->       A   z
        / \              / \
       y   z            x   y
```

Mise à jour des équilibres (formules du cours), avec $a$ et $p$ les équilibres de A et P **avant** la rotation :

$$
\text{eq}(A) = a - \max(p, 0) - 1, \qquad \text{eq}(P) = \min(a - 2,\ a + p - 2,\ p - 1)
$$

La rotation droite est symétrique :

$$
\text{eq}(A) = a - \min(p, 0) + 1, \qquad \text{eq}(P) = \max(a + 2,\ a + p + 2,\ p + 1)
$$

Justification pour la rotation gauche : notons $h_x, h_y, h_z$ les hauteurs de x, y, z. Avant, $p = h_z - h_y$ et $a = 1 + \max(h_y, h_z) - h_x$. Après, $\text{eq}(A) = h_y - h_x = a - 1 - \max(h_y, h_z) + h_y = a - 1 - \max(0, p)$. De même pour P, on obtient $\text{eq}(P) = h_z - 1 - \max(h_x, h_y)$, qui se réécrit avec les trois termes du minimum.

```c
pArbre rotationGauche(pArbre a) {
    pArbre pivot = a->fd;
    int eqA = a->equilibre;
    int eqP = pivot->equilibre;
    a->fd = pivot->fg;
    pivot->fg = a;
    a->equilibre = eqA - max2(eqP, 0) - 1;
    pivot->equilibre = min3(eqA - 2, eqA + eqP - 2, eqP - 1);
    return pivot;               /* nouvelle racine du sous-arbre */
}

pArbre rotationDroite(pArbre a) {
    pArbre pivot = a->fg;
    int eqA = a->equilibre;
    int eqP = pivot->equilibre;
    a->fg = pivot->fd;
    pivot->fd = a;
    a->equilibre = eqA - min2(eqP, 0) + 1;
    pivot->equilibre = max3(eqA + 2, eqA + eqP + 2, eqP + 1);
    return pivot;
}
```

**4.** Premier arbre : équilibres 1 $(+2)$, 2 $(+1)$, 3 $(0)$. `rotationGauche` sur 1 donne 2 à la racine, de fils 1 et 3, tous d'équilibre 0 (formules : $2 - 1 - 1 = 0$ et $\min(0, 1, 0) = 0$). Second arbre : équilibres 3 $(-2)$, 2 $(-1)$, 1 $(0)$ ; `rotationDroite` sur 3 donne le même arbre équilibré.

```c
pArbre r = creerArbre(1);
r->equilibre = 2;
r->fd = creerArbre(2);              /* ajouterFilsDroit(r, 2) */
r->fd->equilibre = 1;
r->fd->fd = creerArbre(3);          /* ajouterFilsDroit(r->fd, 3) */
r = rotationGauche(r);              /* 2(0) avec 1(0) et 3(0) */
```

**5.** Double rotation gauche : rotation droite du fils droit, puis rotation gauche de A (cas « droite puis gauche »). Double rotation droite : symétrique.

```c
pArbre doubleRotationGauche(pArbre a) {
    a->fd = rotationDroite(a->fd);
    return rotationGauche(a);
}

pArbre doubleRotationDroite(pArbre a) {
    a->fg = rotationGauche(a->fg);
    return rotationDroite(a);
}
```

**6.** Équilibres : 5, 13, 17, 26 et 15 valent 0 ; 20 vaut $1 - 2 = -1$ ; 10 vaut $3 - 1 = +2$. La racine penche à droite et son fils droit penche à gauche : c'est le cas de la **double rotation gauche**. Résultat (tous les équilibres valent 0) :

```
            15
          /    \
        10      20
       /  \    /  \
      5   13  17   26
```

**7.** On choisit la rotation selon le signe de l'équilibre du fils du côté lourd.

```c
pArbre equilibrerAVL(pArbre a) {
    if (a->equilibre >= 2) {                 /* trop lourd à droite */
        if (a->fd->equilibre >= 0) {
            return rotationGauche(a);
        }
        return doubleRotationGauche(a);
    }
    if (a->equilibre <= -2) {                /* trop lourd à gauche */
        if (a->fg->equilibre <= 0) {
            return rotationDroite(a);
        }
        return doubleRotationDroite(a);
    }
    return a;
}
```

**8.** Comme dans le cours, `*h` indique en retour si la hauteur du sous-arbre a augmenté (1) ou non (0). En remontant d'un fils gauche on change son signe, puisqu'un sous-arbre gauche plus haut **diminue** l'équilibre. Après mise à jour et rééquilibrage, la hauteur a augmenté seulement si le nœud n'est pas revenu à l'équilibre 0 (après une rotation d'insertion, l'équilibre vaut toujours 0).

```c
pArbre insertionAVL(pArbre a, int e, int *h) {
    if (a == NULL) {
        *h = 1;
        return creerArbre(e);
    }
    if (e < a->elmt) {
        a->fg = insertionAVL(a->fg, e, h);
        *h = -*h;
    } else if (e > a->elmt) {
        a->fd = insertionAVL(a->fd, e, h);
    } else {
        *h = 0;                              /* déjà présent */
        return a;
    }
    if (*h != 0) {
        a->equilibre += *h;
        a = equilibrerAVL(a);
        *h = (a->equilibre == 0) ? 0 : 1;
    }
    return a;
}
```

Appel : `int h; racine = insertionAVL(racine, 12, &h);`.

**9.** Ici `*h` vaut 1 si la hauteur du sous-arbre a **diminué**. Si le nœud à supprimer a un fils droit, on le remplace par son successeur, extrait par `suppMinAVL` (comme dans le cours) ; sinon on le remplace par son fils gauche. En remontant, un sous-arbre gauche raccourci augmente l'équilibre de 1, un droit le diminue de 1. Après rééquilibrage, la hauteur a diminué si et seulement si l'équilibre est revenu à 0.

```c
pArbre suppMinAVL(pArbre a, int *h, int *pe) {
    if (a->fg == NULL) {                     /* a contient le minimum */
        *pe = a->elmt;
        pArbre d = a->fd;
        free(a);
        *h = 1;
        return d;
    }
    a->fg = suppMinAVL(a->fg, h, pe);
    if (*h != 0) {
        a->equilibre += 1;
        a = equilibrerAVL(a);
        *h = (a->equilibre == 0) ? 1 : 0;
    }
    return a;
}

pArbre suppAVL(pArbre a, int e, int *h) {
    if (a == NULL) {
        *h = 0;                              /* e absent */
        return NULL;
    }
    if (e < a->elmt) {
        a->fg = suppAVL(a->fg, e, h);
        if (*h != 0) {
            a->equilibre += 1;
        }
    } else if (e > a->elmt) {
        a->fd = suppAVL(a->fd, e, h);
        if (*h != 0) {
            a->equilibre -= 1;
        }
    } else if (a->fd != NULL) {
        a->fd = suppMinAVL(a->fd, h, &a->elmt);
        if (*h != 0) {
            a->equilibre -= 1;
        }
    } else {                                 /* pas de fils droit */
        pArbre g = a->fg;
        free(a);
        *h = 1;
        return g;
    }
    if (*h != 0) {
        a = equilibrerAVL(a);
        *h = (a->equilibre == 0) ? 1 : 0;
    }
    return a;
}
```

Contrairement à l'insertion, une suppression peut provoquer des rotations à plusieurs niveaux en remontant ; le coût reste $O(\log n)$ car la hauteur d'un AVL est en $O(\log n)$.

## Exercice 3 : Test d'un AVL

**Énoncé.** Reprendre les questions de l'exercice 1 et construire les AVL demandés grâce aux fonctions écrites dans le TD. À chaque étape (ajout ou suppression), afficher l'arbre avec la fonction `affArbreGraphique` qui a été fournie.

**Correction.**

> **Note :** la fonction `affArbreGraphique` fournie en TD n'est pas dans le document ; on la remplace par un affichage « couché » (sous-arbre droit en haut) qui indique l'équilibre de chaque nœud.

```c
void affArbre(pArbre a, int niveau) {
    if (a == NULL) {
        return;
    }
    affArbre(a->fd, niveau + 1);
    for (int i = 0; i < niveau; i++) {
        printf("       ");
    }
    printf("%d(%+d)\n", a->elmt, a->equilibre);
    affArbre(a->fg, niveau + 1);
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
    int v[] = {10, 3, 5, 15, 20, 12, 7, 9};
    int h;
    pArbre a = NULL;
    pArbre b = NULL;
    for (int i = 0; i < 8; i++) {
        a = insertionAVL(a, v[i], &h);
        printf("Après insertion de %d :\n", v[i]);
        affArbre(a, 0);
    }
    for (int i = 7; i >= 0; i--) {
        b = insertionAVL(b, v[i], &h);
        printf("Après insertion de %d :\n", v[i]);
        affArbre(b, 0);
    }
    a = suppAVL(a, 5, &h);
    affArbre(a, 0);
    a = suppAVL(a, 12, &h);
    affArbre(a, 0);
    liberer(a);
    liberer(b);
    return 0;
}
```

L'exécution reproduit exactement les arbres et les équilibres obtenus à la main dans l'exercice 1. Par exemple, l'affichage final du premier arbre est :

```
              20(+0)
       15(+1)
10(+0)
              9(+0)
       7(+0)
              3(+0)
```
