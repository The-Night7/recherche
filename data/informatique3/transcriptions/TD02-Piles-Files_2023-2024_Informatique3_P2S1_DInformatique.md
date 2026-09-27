---
source: TD02-Piles-Files_2023-2024_Informatique3_P2S1_DInformatique.pdf, pages 1-2 (identique à TD2-Pile-File_2022-2023)
transcription: manuelle
corrections: rédigées
---

# TD 02 : Piles et files (1) (corrigé)

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

> **Complément :** le document d'origine ne contient que les énoncés ; toutes les corrections ont été rédigées pour cette transcription. Les codes C99 ont été compilés avec `gcc -std=c99 -Wall -Wextra` et testés.

## Exercice 1 : Application du cours

**Énoncé.**

1. Soit la pile suivante : `[2, 5, 9, 10, 1, -3]`, avec `-3` le haut de la pile. Indiquer l'état de la pile une fois les opérations suivantes effectuées : dépiler ; dépiler ; empiler 12 ; dépiler ; empiler 8 ; empiler 7.
    a) dans cet ordre ;
    b) dans l'ordre inverse.
2. Mêmes questions si la liste présentée est une file, avec l'équivalence empiler/enfiler, dépiler/défiler.
3. Comment pourrait-on simuler une file à l'aide de piles ?

**Correction.**

**1. a)** Dans l'ordre (le sommet est à droite) :

```
départ        [2, 5, 9, 10, 1, -3]
dépiler       [2, 5, 9, 10, 1]          (-3 sort)
dépiler       [2, 5, 9, 10]             (1 sort)
empiler 12    [2, 5, 9, 10, 12]
dépiler       [2, 5, 9, 10]             (12 sort)
empiler 8     [2, 5, 9, 10, 8]
empiler 7     [2, 5, 9, 10, 8, 7]
```

État final : `[2, 5, 9, 10, 8, 7]`, sommet 7.

**1. b)** Ordre inverse : empiler 7, empiler 8, dépiler, empiler 12, dépiler, dépiler.

```
départ        [2, 5, 9, 10, 1, -3]
empiler 7     [2, 5, 9, 10, 1, -3, 7]
empiler 8     [2, 5, 9, 10, 1, -3, 7, 8]
dépiler       [2, 5, 9, 10, 1, -3, 7]   (8 sort)
empiler 12    [2, 5, 9, 10, 1, -3, 7, 12]
dépiler       [2, 5, 9, 10, 1, -3, 7]   (12 sort)
dépiler       [2, 5, 9, 10, 1, -3]      (7 sort)
```

État final : la pile de départ `[2, 5, 9, 10, 1, -3]`.

**2.** Pour la file, on garde la même lecture : `-3` est le dernier arrivé (queue, à droite) et `2` le premier arrivé (tête, à gauche) ; on défile à gauche et on enfile à droite.

> **Note :** l'énoncé ne précise pas quel bout de la liste est la tête de la file ; on a choisi la convention la plus naturelle (même sens que la pile : les éléments entrent à droite).

a) Dans l'ordre :

```
départ        [2, 5, 9, 10, 1, -3]
défiler       [5, 9, 10, 1, -3]         (2 sort)
défiler       [9, 10, 1, -3]            (5 sort)
enfiler 12    [9, 10, 1, -3, 12]
défiler       [10, 1, -3, 12]           (9 sort)
enfiler 8     [10, 1, -3, 12, 8]
enfiler 7     [10, 1, -3, 12, 8, 7]
```

b) Dans l'ordre inverse :

```
départ        [2, 5, 9, 10, 1, -3]
enfiler 7     [2, 5, 9, 10, 1, -3, 7]
enfiler 8     [2, 5, 9, 10, 1, -3, 7, 8]
défiler       [5, 9, 10, 1, -3, 7, 8]   (2 sort)
enfiler 12    [5, 9, 10, 1, -3, 7, 8, 12]
défiler       [9, 10, 1, -3, 7, 8, 12]  (5 sort)
défiler       [10, 1, -3, 7, 8, 12]     (9 sort)
```

Contrairement à la pile, l'ordre inverse ne ramène pas à l'état initial : dans une file, les éléments retirés sont toujours les plus anciens.

**3.** Avec deux piles, `entree` et `sortie` :

- **enfiler** $x$ : empiler $x$ sur `entree` ;
- **défiler** : si `sortie` est vide, on dépile un à un tous les éléments de `entree` en les empilant sur `sortie` (ce transvasement retourne l'ordre : le plus ancien se retrouve au sommet de `sortie`) ; puis on dépile `sortie`.

La file est vide quand les deux piles sont vides. Chaque élément est empilé et dépilé au plus deux fois, donc le coût moyen (amorti) d'une opération est $O(1)$, même si un défilement isolé peut coûter $O(n)$.

## Exercice 2 : Gestion de piles

**Énoncé.**

1. Déclarer la structure `PileDyn` permettant de gérer une pile dynamique contenant des entiers.
2. Écrire une fonction `empiler(int nb, PileDyn* ppile)` permettant d'empiler `nb` sur la pile dynamique pointée par `ppile`.
3. Déclarer une nouvelle pile `p1` et lui empiler les nombres entiers de 1 à 20 dans l'ordre croissant. Que vaudra le sommet de la pile ?
4. Écrire une procédure `affichePile(PileDyn * ppile)` permettant d'afficher le contenu d'une pile de manière récursive. Afficher `p1`.
5. Écrire une fonction `depile(PileDyn * ppile, int *pnmb)` permettant de dépiler une pile d'entiers passée en paramètre et de modifier la valeur de la variable pointée par `pnmb` avec la valeur stockée dans l'élément supprimé.
6. Déclarer deux autres piles `pilePair` et `pileImpair` qui seront remplies à partir de `p1` de la manière suivante : `p1` est dépilée ; si l'élément dépilé est pair, il est empilé dans `pilePair` ; s'il est impair, il est empilé dans `pileImpair`. À quoi vont ressembler ces deux piles ? Vérifier grâce à `affichePile`.
7. Réécrire le programme en utilisant une pile statique.

**Correction.**

**1.** Une pile dynamique est une liste chaînée dont la tête est le sommet : empiler et dépiler se font en $O(1)$ en tête de liste.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Element {
    int valeur;
    struct Element *suivant;   /* élément situé en dessous */
} Element;

typedef struct {
    Element *sommet;           /* NULL si la pile est vide */
    int taille;
} PileDyn;

void initPile(PileDyn *ppile) {
    ppile->sommet = NULL;
    ppile->taille = 0;
}

int estVide(PileDyn *ppile) {
    return ppile == NULL || ppile->sommet == NULL;
}
```

**2.** La fonction retourne 1 en cas de succès et 0 en cas d'erreur (pile inexistante ou allocation impossible).

```c
int empiler(int nb, PileDyn *ppile) {
    if (ppile == NULL) {
        return 0;
    }
    Element *e = malloc(sizeof(Element));
    if (e == NULL) {
        return 0;
    }
    e->valeur = nb;
    e->suivant = ppile->sommet;
    ppile->sommet = e;
    ppile->taille++;
    return 1;
}
```

**3.**

```c
PileDyn p1;
initPile(&p1);
for (int i = 1; i <= 20; i++) {
    empiler(i, &p1);
}
```

Le dernier entier empilé est au sommet : **le sommet vaut 20**.

**4.** La récursion porte sur les éléments : on affiche l'élément courant puis, récursivement, ceux qui sont en dessous. Le cas de base est l'élément `NULL` (fond de la pile).

```c
void afficheElements(Element *e) {
    if (e == NULL) {
        return;
    }
    printf("%d ", e->valeur);
    afficheElements(e->suivant);
}

void affichePile(PileDyn *ppile) {
    if (ppile == NULL) {
        return;
    }
    printf("sommet -> ");
    afficheElements(ppile->sommet);
    printf("\n");
}
```

`affichePile(&p1)` affiche `sommet -> 20 19 18 ... 2 1`.

**5.** Dépiler une pile vide est impossible : la fonction le signale en retournant 0 (et ne touche pas à `*pnmb`) ; elle retourne 1 sinon. L'élément retiré est libéré.

```c
int depile(PileDyn *ppile, int *pnmb) {
    if (estVide(ppile) || pnmb == NULL) {
        return 0;
    }
    Element *e = ppile->sommet;
    *pnmb = e->valeur;
    ppile->sommet = e->suivant;
    ppile->taille--;
    free(e);
    return 1;
}
```

**6.** `p1` est dépilée dans l'ordre 20, 19, …, 1. Les pairs sont donc empilés dans l'ordre 20, 18, …, 2 : le dernier empilé, 2, est au sommet. De même 1 est au sommet de `pileImpair`.

```c
PileDyn pilePair, pileImpair;
initPile(&pilePair);
initPile(&pileImpair);
int x;
while (depile(&p1, &x)) {
    if (x % 2 == 0) {
        empiler(x, &pilePair);
    } else {
        empiler(x, &pileImpair);
    }
}
affichePile(&pilePair);     /* sommet -> 2 4 6 ... 20 */
affichePile(&pileImpair);   /* sommet -> 1 3 5 ... 19 */
```

Chaque pile est dans l'ordre inverse de celui de `p1`, et `p1` est vide à la fin. On libère enfin les deux piles en les dépilant jusqu'au bout (`while (depile(&pilePair, &x)) {}`).

**7.** Pile statique : un tableau de taille maximale fixe et le nombre d'éléments. Il faut maintenant tester la pile **pleine** avant d'empiler.

```c
#define TMAX 100

typedef struct {
    int tab[TMAX];
    int nb;          /* nombre d'éléments ; le sommet est tab[nb-1] */
} PileStat;

void initPileStat(PileStat *p) {
    p->nb = 0;
}

int empilerStat(int x, PileStat *p) {
    if (p == NULL || p->nb == TMAX) {
        return 0;                    /* pile pleine */
    }
    p->tab[p->nb] = x;
    p->nb++;
    return 1;
}

int depileStat(PileStat *p, int *px) {
    if (p == NULL || p->nb == 0 || px == NULL) {
        return 0;                    /* pile vide */
    }
    p->nb--;
    *px = p->tab[p->nb];
    return 1;
}

void afficheStatRec(PileStat *p, int i) {   /* tab[i], tab[i-1], ..., tab[0] */
    if (i < 0) {
        return;
    }
    printf("%d ", p->tab[i]);
    afficheStatRec(p, i - 1);
}

void affichePileStat(PileStat *p) {
    printf("sommet -> ");
    afficheStatRec(p, p->nb - 1);
    printf("\n");
}
```

Le programme principal est identique en remplaçant `PileDyn`, `empiler`, `depile`, `affichePile` par leurs versions statiques ; les affichages obtenus sont les mêmes. Aucune libération n'est nécessaire (pas de `malloc`).

## Exercice 3 : Simulation des clients d'un supermarché

**Énoncé.** Nous allons simuler le passage de clients d'un supermarché en caisse de paiement. Chaque client sera simulé par un entier contenant le nombre d'articles de son caddie. Le but de cet exercice sera d'afficher l'ensemble des caddies des clients en train de patienter à une caisse.

1. Quelle structure (tableau, liste chaînée, pile, file) semble la plus appropriée pour ce type d'exercice ?
2. Déclarer ce type de structure avec comme type d'élément un entier.
3. Créer une fonction qui va créer une instance d'un client avec une valeur entière aléatoire entre 1 et 50 (simulant le nombre d'articles dans son caddie).
4. Créer une fonction qui va afficher tous les clients dans l'ordre d'arrivée en caisse.
5. Créer un programme qui va simuler l'arrivée de clients à la caisse :
    - ajouter 3 clients en caisse ;
    - dans une boucle infinie, au début de chaque tour, on enlève le client le plus proche de la caisse (le prochain à payer ses achats), s'il existe ;
    - ensuite il y a 33 % de chances d'ajouter de nouveaux clients en caisse ;
    - si on ajoute des clients, suite au point précédent, on en ajoute entre 1 et 3 (de manière aléatoire) ;
    - à la fin de la boucle, on affiche le client qui a payé ses achats et on affiche en dessous le reste des clients (dans l'ordre d'arrivée à la caisse) ;
    - s'il n'y a plus de clients en caisse, on arrête le programme.
6. Proposer un algorithme pour modifier le programme précédent de la façon suivante :
    - en commençant par les clients les plus proches de la caisse, déterminer ceux qui voudraient changer de caisse si la somme des articles des autres clients situés devant dépasse un certain seuil ;
    - est-ce que la structure choisie est appropriée pour ce type de calcul ? Justifier la réponse.

**Correction.**

**1.** Une **file** (premier arrivé, premier servi) : les clients arrivent en queue et sortent en tête.

**2.** File dynamique : liste chaînée avec un pointeur sur la tête (prochain client) et un sur la queue (dernier arrivé), pour enfiler et défiler en $O(1)$.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Client {
    int articles;
    struct Client *suivant;
} Client;

typedef struct {
    Client *tete;    /* prochain client à passer */
    Client *queue;   /* dernier arrivé */
} File;

void initFile(File *f) {
    f->tete = NULL;
    f->queue = NULL;
}

int enfiler(File *f, int articles) {
    if (f == NULL) {
        return 0;
    }
    Client *c = malloc(sizeof(Client));
    if (c == NULL) {
        return 0;
    }
    c->articles = articles;
    c->suivant = NULL;
    if (f->queue == NULL) {
        f->tete = c;             /* file vide : c est aussi la tête */
    } else {
        f->queue->suivant = c;
    }
    f->queue = c;
    return 1;
}

int defiler(File *f, int *particles) {
    if (f == NULL || f->tete == NULL || particles == NULL) {
        return 0;
    }
    Client *c = f->tete;
    *particles = c->articles;
    f->tete = c->suivant;
    if (f->tete == NULL) {
        f->queue = NULL;         /* la file est devenue vide */
    }
    free(c);
    return 1;
}
```

Le point délicat est la mise à jour de `queue` quand la file devient vide : sinon `queue` pointerait vers un client libéré.

**3.** `rand() % 50` est entre 0 et 49, donc `1 + rand() % 50` est entre 1 et 50.

```c
int nouveauClient(void) {
    return 1 + rand() % 50;
}
```

**4.** On parcourt de la tête vers la queue, c'est-à-dire dans l'ordre d'arrivée.

```c
void afficheFile(File *f) {
    for (Client *c = f->tete; c != NULL; c = c->suivant) {
        printf("[%d] ", c->articles);
    }
    printf("\n");
}
```

**5.** « 33 % de chances » : `rand() % 3 == 0` est vrai une fois sur trois. Le nombre de nouveaux clients est tiré **une seule fois** avant la boucle d'ajout (le tirer dans la condition du `for` le changerait à chaque tour). La « boucle infinie » s'arrête quand la file est vide.

```c
int main(void) {
    srand(time(NULL));
    File caisse;
    initFile(&caisse);
    for (int i = 0; i < 3; i++) {
        enfiler(&caisse, nouveauClient());
    }
    while (caisse.tete != NULL) {
        int paye;
        int aPaye = defiler(&caisse, &paye);
        if (rand() % 3 == 0) {
            int nb = 1 + rand() % 3;          /* 1 à 3 clients */
            for (int i = 0; i < nb; i++) {
                enfiler(&caisse, nouveauClient());
            }
        }
        if (aPaye) {
            printf("Client payé : %d articles\n", paye);
        }
        printf("En attente : ");
        afficheFile(&caisse);
    }
    return 0;                                  /* la file est vide : rien à libérer */
}
```

Le programme se termine avec probabilité 1 : à chaque tour, on retire un client et on en ajoute en moyenne $\frac{1}{3} \times 2 = \frac{2}{3}$.

**6.** Algorithme : on parcourt la file depuis la tête en tenant la somme `devant` des articles des clients déjà vus.

```
devant <- 0
pour chaque client c, de la tête vers la queue :
    si devant > seuil : c veut changer de caisse
    devant <- devant + c.articles
```

Coût $O(n)$. Une **file** au sens strict n'est pas adaptée : on ne peut accéder qu'à la tête, donc pour parcourir il faudrait défiler tous les clients puis les réenfiler, et on ne peut pas retirer un client situé au milieu (celui qui change de caisse). Il vaut mieux utiliser la **liste chaînée** sous-jacente (parcours et suppression au milieu possibles), en gardant l'accès à la tête et à la queue pour le fonctionnement normal de la caisse.

## Exercice 4 : Vérification du parenthésage

**Énoncé.** La plupart des traitements de texte ou de calculs sont capables d'analyser la syntaxe et d'indiquer un problème de parenthésage. Pour vérifier qu'un texte ou une expression contient des parenthèses correctes, il ne suffit pas que le nombre de parenthèses ouvrantes soit le même que le nombre de parenthèses fermantes : l'ordre dans lequel on rencontre les parenthèses fermantes doit correspondre à l'ordre dans lequel on a rencontré les parenthèses ouvrantes.

Exemple : `"Je suis Luffy )le futur roi des pirates( !"` a un mauvais parenthésage bien qu'il y ait une parenthèse ouvrante et une fermante.

1. Quelle structure (tableau, liste chaînée, pile, file) est la plus adaptée pour vérifier le parenthésage d'une phrase ?
2. Déclarer ce type de structure qui contiendra des caractères.
3. Écrire un programme permettant de vérifier le bon parenthésage d'une chaîne de caractères. Vérifier votre algorithme en saisissant une formule mathématique.
4. Faire de même pour des phrases pouvant contenir deux types de symboles : les parenthèses `()` et les crochets `[]`. Les règles sont les suivantes : comme précédemment, les symboles fermants doivent correspondre à l'ordre dans lequel on a rencontré les symboles ouvrants ; le type (parenthèse ou crochet) d'un symbole fermant doit toujours correspondre au type du dernier symbole ouvrant rencontré (et non encore fermé). Exemples : `"a(b[c()e]f)g"` est bien parenthésé, `"a(b[c)d]e"` ne l'est pas.

> **Note :** dans le document d'origine, une adresse de projet Overleaf a été collée par erreur au début de la règle de la question 4 ; elle a été retirée.

**Correction.**

**1.** Une **pile** : un symbole fermant doit correspondre au **dernier** ouvrant non encore fermé (dernier entré, premier sorti).

**2.**

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Car {
    char c;
    struct Car *suivant;
} Car;

typedef Car *PileCar;          /* une pile = adresse de son sommet */

int empilerCar(PileCar *p, char c) {
    Car *e = malloc(sizeof(Car));
    if (e == NULL) {
        return 0;
    }
    e->c = c;
    e->suivant = *p;
    *p = e;
    return 1;
}

int depilerCar(PileCar *p, char *c) {
    if (*p == NULL) {
        return 0;              /* pile vide */
    }
    Car *e = *p;
    *c = e->c;
    *p = e->suivant;
    free(e);
    return 1;
}

void viderCar(PileCar *p) {
    char c;
    while (depilerCar(p, &c)) {
    }
}
```

**3.** On lit la chaîne de gauche à droite : on empile chaque `(` ; à chaque `)`, on dépile, et si la pile est vide la chaîne est mal parenthésée (fermante sans ouvrante). À la fin, la pile doit être **vide** (sinon une ouvrante n'a pas été fermée, comme dans `((a)`).

```c
int bienParenthese(const char *s) {
    PileCar p = NULL;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            empilerCar(&p, '(');
        } else if (s[i] == ')') {
            char c;
            if (!depilerCar(&p, &c)) {
                return 0;
            }
        }
    }
    int ok = (p == NULL);
    viderCar(&p);              /* libère les ouvrantes restantes */
    return ok;
}
```

Pour une seule sorte de symbole, un simple compteur suffirait (il ne doit jamais devenir négatif et doit finir à 0) ; la pile devient indispensable à la question 4. Tests : la phrase de Luffy donne 0, `((a)` donne 0, `(a+b)*(c-(d))` donne 1.

**4.** On empile le symbole ouvrant lui-même ; à la fermeture, le symbole dépilé doit être du même type.

```c
int bienParentheseCrochets(const char *s) {
    PileCar p = NULL;
    for (int i = 0; s[i] != '\0'; i++) {
        char x = s[i];
        if (x == '(' || x == '[') {
            if (!empilerCar(&p, x)) {
                viderCar(&p);
                return 0;
            }
        } else if (x == ')' || x == ']') {
            char o;
            if (!depilerCar(&p, &o)) {
                return 0;          /* rien à fermer */
            }
            if ((x == ')' && o != '(') || (x == ']' && o != '[')) {
                viderCar(&p);
                return 0;          /* mauvais type */
            }
        }
    }
    int ok = (p == NULL);
    viderCar(&p);
    return ok;
}
```

Tests : `a(b[c()e]f)g` donne 1 ; `a(b[c)d]e` donne 0 (la `)` rencontre le `[` au sommet) ; `[(])` donne 0 ; `[()]` donne 1 ; `((` donne 0. Coût : $O(n)$ pour une chaîne de longueur $n$.
