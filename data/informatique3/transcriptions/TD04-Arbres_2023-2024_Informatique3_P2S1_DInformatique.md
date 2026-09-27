---
source: TD04-Arbres_2023-2024_Informatique3_P2S1_DInformatique.pdf, pages 1-3 (identique à TD4-Arbres_2022-2023)
transcription: manuelle
corrections: rédigées
---

# TD 04 : Arbres (corrigé)

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

> **Complément :** le document d'origine ne contient que les énoncés ; toutes les corrections ont été rédigées pour cette transcription. Les codes C99 ont été compilés avec `gcc -std=c99 -Wall -Wextra` et testés.

## Exercice 1 : Question de cours

**Énoncé.** Soit l'arbre suivant :

```
                 1
       /         |         \
      2          4          6
    / | \       / \        /  \
   7  8  9    10   12     13   14
     / \               /  |  |  \
   15   16            17 18  19  20
```

> **Note :** la figure du document est redessinée ci-dessus : 1 a pour fils 2, 4 et 6 ; 2 a pour fils 7, 8, 9 ; 8 a pour fils 15 et 16 ; 4 a pour fils 10 et 12 ; 6 a pour fils 13 et 14 ; 13 a pour fils 17, 18, 19 et 20.

1. Donner :
    - l'ordre de l'arbre ;
    - le degré du nœud 4 et du nœud 2 ;
    - le nombre de feuilles ;
    - la hauteur de l'arbre.
2. Quel est le parcours en profondeur préfixe de cet arbre ?
3. Quel est le parcours en largeur de cet arbre ?

**Correction.**

**1.**

- L'**ordre** d'un arbre est le nombre maximal de fils d'un nœud : le nœud 13 a 4 fils, les autres au plus 3. L'arbre est **d'ordre 4**.
- Le **degré** d'un nœud est son nombre de fils : **degré(4) = 2** (10 et 12), **degré(2) = 3** (7, 8, 9).
- Les **feuilles** (nœuds sans fils) sont 7, 15, 16, 9, 10, 12, 17, 18, 19, 20, 14 : **11 feuilles**.
- La **hauteur** est la longueur (en nombre d'arêtes) du plus long chemin de la racine à une feuille. Les feuilles les plus profondes (15, 16, 17 à 20) sont à 3 arêtes de la racine : **hauteur 3**. (Avec la convention qui compte les niveaux, on trouverait 4 ; on garde ici la convention du cours, où l'arbre vide a la hauteur $-1$ et une feuille seule la hauteur 0.)

**2.** Parcours préfixe : on traite le nœud, puis ses sous-arbres de gauche à droite.

`1, 2, 7, 8, 15, 16, 9, 4, 10, 12, 6, 13, 17, 18, 19, 20, 14`

**3.** Parcours en largeur : niveau par niveau, de gauche à droite.

`1, 2, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20`

## Exercice 2 : Arbre binaire

**Énoncé.** Remarque : la plupart des fonctions demandées dans cet exercice sont disponibles en pseudo-code dans le cours.

1. Construction de l'arbre :
    a) Déclarer une structure `Arbre` permettant de gérer un arbre binaire contenant des entiers.
    b) Redéfinir le type pointeur sur arbre en `pArbre`.
    c) Créer la fonction `creerArbre` permettant de créer un arbre. Cette fonction prend en paramètre l'élément à insérer dans le nœud de l'arbre, initialise ses fils et retourne son adresse.
    d) Écrire la fonction `int estVide(pArbre a)` qui retourne 1 si `a` est un arbre vide, 0 sinon.
    e) Écrire la fonction `int estFeuille(pArbre a)` qui retourne 1 si l'arbre est une feuille, 0 sinon.
    f) Écrire la fonction `int element(pArbre a)` qui retourne l'élément stocké dans le nœud de `a`.
    g) Écrire une fonction `existeFilsGauche(pArbre a)` qui retourne 1 si l'arbre a un fils gauche, 0 sinon. Faire une fonction similaire `existeFilsDroit(pArbre a)`.
    h) Écrire une fonction `ajouterFilsGauche(pArbre a, int e)` qui crée à l'arbre un fils gauche qui va contenir `e`. Faire de même avec `ajouterFilsDroit(pArbre a, int e)`.
    i) À l'aide des fonctions réalisées précédemment, construire l'arbre suivant :

```
            1
         /     \
        2       8
      /   \    / \
     3     6  9   10
    / \     \
   4   5     7
```

2. Parcours de l'arbre :
    a) Écrire une fonction `traiter` qui affichera le contenu du nœud de l'arbre passé en paramètre.
    b) Écrire une procédure `parcoursPrefixe` permettant d'afficher tous les éléments d'un arbre par un parcours en profondeur préfixe.
    c) Vérifier que l'arbre que vous avez construit est correct en affichant son parcours préfixe.
    d) Écrire une procédure `parcoursPostfixe` permettant d'afficher tous les éléments d'un arbre par un parcours en profondeur postfixe. Tester la fonction sur l'arbre.
    e) Déclarer une structure permettant de gérer une FILE contenant des `pArbre`.
    f) Écrire une procédure `parcoursLargeur` permettant d'afficher tous les éléments d'un arbre par un parcours en largeur.
3. Modification de l'arbre :
    a) Écrire une fonction `pArbre modifierRacine(pArbre a, int e)` qui modifie l'élément stocké dans `a` par l'élément `e` et retourne `a`.
    b) Écrire une fonction `pArbre supprimerFilsGauche(pArbre)` qui supprime le fils gauche d'un arbre. Idem avec `supprimerFilsDroit(pArbre)`. Attention aux fuites mémoire ! (voir cours)
    c) Supprimer les nœuds 9, 15 et 3 de l'arbre. Quel devrait être son parcours en largeur ? Vérifier.
4. Analyse de l'arbre.
5. Écrire une fonction `nmbFeuille` qui retourne le nombre de feuilles d'un arbre.
6. Écrire une fonction `tailleArbre` qui retourne la taille (nombre de nœuds internes) de l'arbre.
7. *Pas facile !* Écrire une fonction `hauteur` qui retourne la hauteur d'un arbre. Elle renverra -1 si l'arbre est vide.

> **Note :** le document écrit `exitseFilsGauche` et `parbre modifierRacine` ; on a corrigé en `existeFilsGauche` et `pArbre`. Dans la figure, 7 est le fils **droit** de 6.

**Correction.**

**1. a) à c)**

```c
#include <stdio.h>
#include <stdlib.h>
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

**d) à h)** Un arbre vide est le pointeur `NULL`. Chaque fonction teste d'abord ce cas pour ne jamais déréférencer `NULL`. Les fonctions d'ajout retournent 1 en cas de succès, 0 si l'arbre est vide ou si le fils existe déjà (on n'écrase pas un sous-arbre, ce qui créerait une fuite mémoire).

```c
int estVide(pArbre a) {
    return a == NULL;
}

int estFeuille(pArbre a) {
    return a != NULL && a->fg == NULL && a->fd == NULL;
}

int element(pArbre a) {
    if (a == NULL) {
        fprintf(stderr, "element : arbre vide\n");
        exit(EXIT_FAILURE);
    }
    return a->elmt;
}

int existeFilsGauche(pArbre a) {
    return a != NULL && a->fg != NULL;
}

int existeFilsDroit(pArbre a) {
    return a != NULL && a->fd != NULL;
}

int ajouterFilsGauche(pArbre a, int e) {
    if (a == NULL || a->fg != NULL) {
        return 0;
    }
    a->fg = creerArbre(e);
    return 1;
}

int ajouterFilsDroit(pArbre a, int e) {
    if (a == NULL || a->fd != NULL) {
        return 0;
    }
    a->fd = creerArbre(e);
    return 1;
}
```

**i)**

```c
pArbre a = creerArbre(1);
ajouterFilsGauche(a, 2);
ajouterFilsDroit(a, 8);
pArbre n2 = a->fg;
pArbre n8 = a->fd;
ajouterFilsGauche(n2, 3);
ajouterFilsDroit(n2, 6);
ajouterFilsGauche(n2->fg, 4);
ajouterFilsDroit(n2->fg, 5);
ajouterFilsDroit(n2->fd, 7);      /* 7 est le fils droit de 6 */
ajouterFilsGauche(n8, 9);
ajouterFilsDroit(n8, 10);
```

**2. a) à d)** Les parcours en profondeur sont récursifs ; le cas de base est l'arbre vide.

```c
void traiter(pArbre a) {
    if (a != NULL) {
        printf("%d ", a->elmt);
    }
}

void parcoursPrefixe(pArbre a) {      /* racine, gauche, droite */
    if (a == NULL) {
        return;
    }
    traiter(a);
    parcoursPrefixe(a->fg);
    parcoursPrefixe(a->fd);
}

void parcoursPostfixe(pArbre a) {     /* gauche, droite, racine */
    if (a == NULL) {
        return;
    }
    parcoursPostfixe(a->fg);
    parcoursPostfixe(a->fd);
    traiter(a);
}
```

Sur l'arbre construit : préfixe `1 2 3 4 5 6 7 8 9 10` (ce qui confirme la construction), postfixe `4 5 3 7 6 2 9 10 8 1`.

**e) et f)** Parcours en largeur : on enfile la racine ; tant que la file n'est pas vide, on défile un nœud, on le traite et on enfile ses fils (gauche puis droit). La file contient des **pointeurs** vers les nœuds : les nœuds eux-mêmes ne sont ni copiés ni libérés.

```c
typedef struct ChainonF {
    pArbre arbre;
    struct ChainonF *suivant;
} ChainonF;

typedef struct {
    ChainonF *tete;
    ChainonF *queue;
} File;

void enfiler(File *f, pArbre a) {
    ChainonF *c = malloc(sizeof(ChainonF));
    if (c == NULL) {
        fprintf(stderr, "Erreur d'allocation\n");
        exit(EXIT_FAILURE);
    }
    c->arbre = a;
    c->suivant = NULL;
    if (f->queue == NULL) {
        f->tete = c;
    } else {
        f->queue->suivant = c;
    }
    f->queue = c;
}

pArbre defiler(File *f) {             /* à appeler sur une file non vide */
    ChainonF *c = f->tete;
    pArbre a = c->arbre;
    f->tete = c->suivant;
    if (f->tete == NULL) {
        f->queue = NULL;
    }
    free(c);
    return a;
}

void parcoursLargeur(pArbre a) {
    if (a == NULL) {
        return;
    }
    File f = {NULL, NULL};
    enfiler(&f, a);
    while (f.tete != NULL) {
        pArbre n = defiler(&f);
        traiter(n);
        if (n->fg != NULL) {
            enfiler(&f, n->fg);
        }
        if (n->fd != NULL) {
            enfiler(&f, n->fd);
        }
    }
}
```

Résultat : `1 2 8 3 6 9 10 4 5 7`.

**3. a) et b)** Pour supprimer un fils, il faut libérer **tout son sous-arbre**, avec un parcours postfixe (on libère les fils avant le père, sinon on perdrait leur adresse). On remet ensuite le pointeur à `NULL`.

```c
pArbre modifierRacine(pArbre a, int e) {
    if (a != NULL) {
        a->elmt = e;
    }
    return a;
}

void libererArbre(pArbre a) {
    if (a == NULL) {
        return;
    }
    libererArbre(a->fg);
    libererArbre(a->fd);
    free(a);
}

pArbre supprimerFilsGauche(pArbre a) {
    if (a != NULL) {
        libererArbre(a->fg);
        a->fg = NULL;
    }
    return a;
}

pArbre supprimerFilsDroit(pArbre a) {
    if (a != NULL) {
        libererArbre(a->fd);
        a->fd = NULL;
    }
    return a;
}
```

**c)** 9 est le fils gauche de 8 et 3 le fils gauche de 2 : `supprimerFilsGauche(n8)` puis `supprimerFilsGauche(n2)`. Supprimer 3 supprime aussi son sous-arbre (4 et 5).

> **Note :** il n'y a pas de nœud 15 dans cet arbre (il s'agit probablement de 5, qui disparaît de toute façon avec le sous-arbre de 3).

Arbre obtenu :

```
        1
      /   \
     2     8
      \     \
       6     10
        \
         7
```

Parcours en largeur attendu et obtenu : `1 2 8 6 10 7`.

**5. à 7.** Définitions récursives :

- nombre de feuilles : 0 pour l'arbre vide, 1 pour une feuille, sinon somme sur les deux fils ;
- taille : 0 pour l'arbre vide, sinon $1 + \text{taille}(fg) + \text{taille}(fd)$ ;
- hauteur : $-1$ pour l'arbre vide, sinon $1 + \max(h(fg), h(fd))$ (une feuille a donc la hauteur $1 + \max(-1, -1) = 0$).

> **Note :** l'énoncé définit la taille comme le « nombre de nœuds internes » ; la taille d'un arbre est usuellement son nombre **total** de nœuds. On donne les deux fonctions.

```c
int nmbFeuille(pArbre a) {
    if (a == NULL) {
        return 0;
    }
    if (estFeuille(a)) {
        return 1;
    }
    return nmbFeuille(a->fg) + nmbFeuille(a->fd);
}

int tailleArbre(pArbre a) {                /* nombre total de nœuds */
    if (a == NULL) {
        return 0;
    }
    return 1 + tailleArbre(a->fg) + tailleArbre(a->fd);
}

int nmbNoeudsInternes(pArbre a) {          /* nœuds qui ne sont pas des feuilles */
    if (a == NULL || estFeuille(a)) {
        return 0;
    }
    return 1 + nmbNoeudsInternes(a->fg) + nmbNoeudsInternes(a->fd);
}

int max2(int x, int y) {
    return x > y ? x : y;
}

int hauteur(pArbre a) {
    if (a == NULL) {
        return -1;
    }
    return 1 + max2(hauteur(a->fg), hauteur(a->fd));
}
```

Sur l'arbre complet de la question 1 i) : 5 feuilles (4, 5, 7, 9, 10), taille 10, 5 nœuds internes, hauteur 3. Après les suppressions : 2 feuilles, taille 6, hauteur 3. Chaque fonction visite chaque nœud une fois : coût $O(n)$.

## Exercice 3 : Arbre binaire filiforme

**Énoncé.** Un arbre binaire est dit *filiforme* si chaque nœud a au plus un seul fils (qu'il soit gauche ou droit).

- À quoi va ressembler un tel arbre ?
- Écrire une fonction permettant de déterminer si un arbre est filiforme (plusieurs méthodes sont possibles !).
- Un arbre est dit *peigne gauche* si les nœuds n'ont qu'un fils gauche et pas de fils droit.
    - Écrire une fonction permettant de déterminer si un arbre est peigne gauche.
    - Écrire une fonction `pArbre constrPeigneGauche(int h)` qui va créer un arbre peigne gauche de hauteur h en le remplissant avec des valeurs aléatoires entre 0 et 10. L'afficher.

**Correction.**

**Forme.** Un arbre filiforme est une simple **chaîne** de nœuds, comme une liste chaînée (qui peut partir à gauche ou à droite à chaque nœud). Il n'a qu'une feuille, et sa hauteur vaut $n - 1$ pour $n$ nœuds : c'est le cas le plus déséquilibré possible.

**Filiforme.** Méthode récursive : l'arbre vide est filiforme ; un nœud ayant deux fils ne l'est pas ; sinon, on vérifie ses sous-arbres (l'un des deux est vide). On peut aussi descendre itérativement le long de l'unique chemin.

```c
int estFiliforme(pArbre a) {
    if (a == NULL) {
        return 1;
    }
    if (a->fg != NULL && a->fd != NULL) {
        return 0;
    }
    return estFiliforme(a->fg) && estFiliforme(a->fd);
}

int estFiliformeIter(pArbre a) {
    while (a != NULL) {
        if (a->fg != NULL && a->fd != NULL) {
            return 0;
        }
        a = (a->fg != NULL) ? a->fg : a->fd;
    }
    return 1;
}
```

**Peigne gauche.** Aucun nœud n'a de fils droit.

```c
int estPeigneGauche(pArbre a) {
    if (a == NULL) {
        return 1;
    }
    if (a->fd != NULL) {
        return 0;
    }
    return estPeigneGauche(a->fg);
}
```

**Construction.** Un peigne gauche de hauteur $h$ a $h + 1$ nœuds (la hauteur compte les arêtes). Récursivement : hauteur $-1$ donne l'arbre vide, sinon une racine dont le fils gauche est un peigne de hauteur $h - 1$. `rand() % 11` donne une valeur entre 0 et 10.

```c
pArbre constrPeigneGauche(int h) {
    if (h < 0) {
        return NULL;
    }
    pArbre a = creerArbre(rand() % 11);
    a->fg = constrPeigneGauche(h - 1);
    return a;
}

int main(void) {
    srand(time(NULL));
    pArbre p = constrPeigneGauche(4);
    parcoursPrefixe(p);          /* 5 valeurs, par exemple 6 10 6 2 1 */
    printf("\n%d %d %d\n", estPeigneGauche(p), estFiliforme(p), hauteur(p));
    libererArbre(p);             /* affiche 1 1 4 */
    return 0;
}
```

## Exercice 4 : Notation polonaise inversée

**Énoncé.** (Devoir de 2021-2022.) La notation polonaise inversée (NPI), utilisée par certaines calculatrices, permet d'écrire de façon non ambiguë les formules arithmétiques sans utiliser de parenthèses. Le principe est que les opérandes précèdent toujours leurs opérateurs et peuvent être eux-mêmes des nombres ou des expressions non triviales.

Exemples : $1 + 2$ s'écrit `1 2 +` ; $((1 + 2) * 4) + 3$ s'écrit `1 2 + 4 * 3 +` ; $\dfrac{a}{a + b}$ s'écrit `a a b + /`.

Dans cet exercice, nous abordons comment construire une notation polonaise à l'aide d'un arbre binaire. Chaque nœud de cet arbre contiendra un opérateur ou un nombre. On considère les structures suivantes :

```
Structure Terme
    typeTerme : Caractere
    valeur : Reel

Structure Arbre
    terme : Structure Terme
    fg, fd : Pointeur sur Structure Arbre
```

Le champ `typeTerme` servira à définir les opérateurs ; il ne pourra prendre que les valeurs suivantes : `'+'`, `'-'`, `'x'`, `'/'` et `'='`. Si `typeTerme` vaut `'='`, c'est que le nœud permet de stocker un nombre. Si ce n'est pas le cas, le champ `valeur` vaudra 0. Chaque nœud interne contient un opérateur binaire, et ses fils gauche et droit sont respectivement l'expression à gauche et l'expression à droite de l'opérateur. Les feuilles sont donc forcément des constantes.

1. Quelle est l'écriture en NPI du calcul suivant ?
$$
5 * \dfrac{(a + 1) * (b + 1)}{a + b}
$$
2. Quelle est la valeur de l'expression polonaise inversée suivante : `1 8 2 - 7 4 - * 3 6 + / /` ?
3. L'expression $((3 - 4) * 2 + 3)$ s'écrit sous forme d'arbre comme suit (chaque nœud est noté `(typeTerme, valeur)`) :

```
              (+,0)
             /     \
         (*,0)     (=,3)
         /    \
     (-,0)    (=,2)
     /    \
  (=,3)  (=,4)
```

La notation polonaise inversée de ce calcul est `3 4 - 2 * 3 +`. À quel type de parcours d'arbre correspond la notation polonaise inversée ?

4. À partir des structures définies ci-dessus et des fonctions écrites lors des exercices précédents, construire l'arbre représenté ci-dessus.
5. Écrire la procédure `void afficherNotationPolonaiseInversee(pArbre a)` qui permet d'afficher en notation polonaise inversée l'expression mathématique définie dans l'arbre binaire.
6. Écrire la fonction `float eval(pArbre a)` qui permet de donner le résultat de l'expression mathématique définie dans l'arbre binaire. La tester avec l'arbre, puis pour vérifier votre réponse à la question 2.

> **Note :** l'énoncé parle d'« opérandes » pour désigner les opérateurs ; on a rétabli les termes. Dans la figure, la multiplication est notée `*` alors que la liste des valeurs autorisées donne `'x'` ; le code accepte les deux.

**Correction.**

**1.** L'expression est $5 * \big(P / S\big)$ avec $P = (a+1)*(b+1)$ et $S = a + b$. En NPI : $a+1$ donne `a 1 +`, $b+1$ donne `b 1 +`, donc $P$ donne `a 1 + b 1 + *` ; $S$ donne `a b +` ; puis `/` et enfin la multiplication par 5 :

`5 a 1 + b 1 + * a b + / *`

**2.** On évalue avec une pile : chaque nombre est empilé ; chaque opérateur dépile deux valeurs $y$ (sommet) puis $x$, et empile $x \text{ op } y$.

```
1 8 2      pile : 1 8 2
-          8 - 2 = 6       pile : 1 6
7 4        pile : 1 6 7 4
-          7 - 4 = 3       pile : 1 6 3
*          6 * 3 = 18      pile : 1 18
3 6 +      3 + 6 = 9       pile : 1 18 9
/          18 / 9 = 2      pile : 1 2
/          1 / 2 = 0.5     pile : 0.5
```

L'expression vaut $\dfrac{1}{\big((8-2)(7-4)\big)/(3+6)} = \dfrac{1}{2} = 0{,}5$.

**3.** La NPI écrit les deux opérandes puis l'opérateur : c'est le **parcours en profondeur postfixe** (fils gauche, fils droit, puis nœud).

**4.** Structures en C et constructeurs. On utilise un type distinct `pArbreE` pour ne pas le confondre avec l'arbre d'entiers de l'exercice 2.

```c
typedef struct {
    char typeTerme;   /* '+', '-', 'x', '/' ou '=' pour un nombre */
    float valeur;     /* 0 si ce n'est pas un nombre */
} Terme;

typedef struct ArbreE {
    Terme terme;
    struct ArbreE *fg;
    struct ArbreE *fd;
} ArbreE;

typedef ArbreE *pArbreE;

pArbreE creerNoeud(char type, float valeur, pArbreE fg, pArbreE fd) {
    pArbreE a = malloc(sizeof(ArbreE));
    if (a == NULL) {
        fprintf(stderr, "Erreur d'allocation\n");
        exit(EXIT_FAILURE);
    }
    a->terme.typeTerme = type;
    a->terme.valeur = (type == '=') ? valeur : 0;
    a->fg = fg;
    a->fd = fd;
    return a;
}

pArbreE nombre(float v) {
    return creerNoeud('=', v, NULL, NULL);
}

pArbreE operation(char op, pArbreE g, pArbreE d) {
    return creerNoeud(op, 0, g, d);
}
```

Construction de l'arbre de $((3 - 4) * 2 + 3)$ :

```c
pArbreE e = operation('+',
                operation('x',
                    operation('-', nombre(3), nombre(4)),
                    nombre(2)),
                nombre(3));
```

**5.** Parcours postfixe, en affichant le nombre ou l'opérateur.

```c
void afficherNotationPolonaiseInversee(pArbreE a) {
    if (a == NULL) {
        return;
    }
    afficherNotationPolonaiseInversee(a->fg);
    afficherNotationPolonaiseInversee(a->fd);
    if (a->terme.typeTerme == '=') {
        printf("%g ", a->terme.valeur);
    } else {
        printf("%c ", a->terme.typeTerme);
    }
}
```

**6.** Une feuille vaut sa valeur ; un nœud interne applique son opérateur aux valeurs de ses deux fils (évaluation postfixe elle aussi). On refuse la division par zéro.

```c
float eval(pArbreE a) {
    if (a == NULL) {
        fprintf(stderr, "eval : arbre vide\n");
        exit(EXIT_FAILURE);
    }
    if (a->terme.typeTerme == '=') {
        return a->terme.valeur;
    }
    float g = eval(a->fg);
    float d = eval(a->fd);
    switch (a->terme.typeTerme) {
        case '+':
            return g + d;
        case '-':
            return g - d;
        case 'x':
        case '*':
            return g * d;
        case '/':
            if (d == 0) {
                fprintf(stderr, "division par zéro\n");
                exit(EXIT_FAILURE);
            }
            return g / d;
        default:
            fprintf(stderr, "opérateur inconnu\n");
            exit(EXIT_FAILURE);
    }
}

void libererExpr(pArbreE a) {
    if (a == NULL) {
        return;
    }
    libererExpr(a->fg);
    libererExpr(a->fd);
    free(a);
}
```

Tests : l'arbre de la question 3 affiche `3 4 - 2 x 3 +` et s'évalue à $(3-4) \times 2 + 3 = 1$. L'expression de la question 2 correspond à l'arbre de racine `/` ayant pour fils gauche `1` et pour fils droit l'arbre de `((8-2) x (7-4)) / (3+6)` ; le programme affiche `1 8 2 - 7 4 - x 3 6 + / /` et la valeur `0.5`, ce qui confirme la question 2.
