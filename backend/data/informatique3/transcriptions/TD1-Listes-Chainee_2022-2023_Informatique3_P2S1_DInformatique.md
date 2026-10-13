---
source: TD1-Listes-Chainee_2022-2023_Informatique3_P2S1_DInformatique.pdf, pages 1-2
transcription: manuelle
corrections: rédigées
---

# TD 01 : Listes chaînées (corrigé)

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

> **Complément :** le document d'origine ne contient que les énoncés ; toutes les corrections ont été rédigées pour cette transcription. Les codes sont en C99 et ont été compilés avec `gcc -std=c99 -Wall -Wextra` puis testés.

## Exercice 1 : Liste des puissances de deux

**Énoncé.**

1. Déclarer une structure `Chainon` permettant de construire une liste chaînée comportant des entiers.
2. Écrire une fonction `Chainon * creationChainon(int a)` qui retourne un pointeur vers un nouveau `Chainon` contenant l'entier `a`.
3. Écrire une fonction `Chainon * insertDebut(Chainon* pliste, int a)` permettant d'insérer un nouvel entier `a` en début de la liste chaînée pointée par `pliste`. Cette fonction retourne la tête de la liste chaînée.
4. Écrire une fonction `insertFin(Chainon* pliste, int a)` permettant d'insérer un nouvel entier `a` en fin de la liste chaînée pointée par `pliste`.
5. Écrire une procédure `afficheListe(Chainon* pliste)` permettant d'afficher les différents éléments de la liste chaînée pointée par `pliste`. Les entiers seront séparés par le symbole `->`. Exemple : `1 -> 10 -> 3 -> 15`.
6. Dans le programme principal, initialiser un pointeur sur une liste vide.
7. On souhaite que ce programme affiche une liste des puissances de deux dans l'ordre. La taille de cette liste sera décidée par l'utilisateur : on affiche la liste chaînée et on demande à l'utilisateur s'il souhaite voir la puissance de deux suivante ; si c'est le cas, on rajoute un `Chainon` supplémentaire à la liste et on l'affiche à nouveau, sinon on arrête le programme.

**Correction.**

**1.** Un chaînon contient une valeur et l'adresse du chaînon suivant (`NULL` pour le dernier). Une liste est représentée par l'adresse de son premier chaînon ; la liste vide est `NULL`.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Chainon {
    int valeur;
    struct Chainon *suivant;
} Chainon;
```

**2.** On alloue le chaînon avec `malloc` et on vérifie l'allocation.

```c
Chainon *creationChainon(int a) {
    Chainon *c = malloc(sizeof(Chainon));
    if (c == NULL) {
        fprintf(stderr, "Erreur d'allocation\n");
        exit(EXIT_FAILURE);
    }
    c->valeur = a;
    c->suivant = NULL;
    return c;
}
```

**3.** Le nouveau chaînon pointe vers l'ancienne tête et devient la tête. Ce code fonctionne aussi pour une liste vide (le nouveau chaînon pointe alors vers `NULL`). Coût : $O(1)$.

```c
Chainon *insertDebut(Chainon *pliste, int a) {
    Chainon *c = creationChainon(a);
    c->suivant = pliste;
    return c;                 /* nouvelle tête */
}
```

**4.** Il faut parcourir la liste jusqu'au dernier chaînon (celui dont `suivant` vaut `NULL`), ce qui coûte $O(n)$. Si la liste est vide, le nouveau chaînon devient la tête : la fonction doit donc **retourner la tête** (sinon l'appelant ne pourrait pas récupérer la nouvelle liste).

```c
Chainon *insertFin(Chainon *pliste, int a) {
    Chainon *c = creationChainon(a);
    if (pliste == NULL) {
        return c;
    }
    Chainon *p = pliste;
    while (p->suivant != NULL) {
        p = p->suivant;
    }
    p->suivant = c;
    return pliste;
}
```

**5.** On n'écrit la flèche que s'il reste un élément après ; la liste vide affiche une ligne vide (sans jamais déréférencer `NULL`).

```c
void afficheListe(Chainon *pliste) {
    Chainon *p = pliste;
    while (p != NULL) {
        printf("%d", p->valeur);
        if (p->suivant != NULL) {
            printf(" -> ");
        }
        p = p->suivant;
    }
    printf("\n");
}
```

On ajoute une procédure de libération, utilisée dans toute la suite :

```c
void libereListe(Chainon *pliste) {
    while (pliste != NULL) {
        Chainon *suiv = pliste->suivant;   /* à lire avant le free */
        free(pliste);
        pliste = suiv;
    }
}
```

**6. et 7.** La liste vide est `Chainon *liste = NULL;`. On ajoute les puissances $1, 2, 4, 8, \dots$ en fin de liste pour qu'elles apparaissent dans l'ordre croissant.

```c
int main(void) {
    Chainon *liste = NULL;        /* question 6 : liste vide */
    int puissance = 1;            /* 2^0 */
    int reponse = 1;
    while (reponse == 1) {
        liste = insertFin(liste, puissance);
        afficheListe(liste);
        puissance = puissance * 2;
        printf("Afficher la puissance suivante ? (1 = oui, 0 = non) ");
        if (scanf("%d", &reponse) != 1) {
            reponse = 0;          /* saisie invalide : on arrête */
        }
    }
    libereListe(liste);
    return 0;
}
```

Remarque : `insertFin` reparcourt toute la liste à chaque ajout. On pourrait garder un pointeur sur le dernier chaînon pour ajouter en $O(1)$. Avec un `int` sur 32 bits, $2^{31}$ dépasse la capacité : au-delà de 31 ajouts, il faudrait un `long long` ou arrêter la boucle.

## Exercice 2 : Liste croissante

**Énoncé.** Écrire un programme qui ajoute un élément dans une liste simplement chaînée et triée par ordre croissant.

**Correction.**

*Méthode.* Si la liste est vide ou si `a` est inférieur ou égal à la tête, on insère en tête. Sinon on avance un pointeur `p` tant que le chaînon **suivant** a une valeur strictement inférieure à `a` ; on insère alors le nouveau chaînon juste après `p`. Il faut s'arrêter sur le chaînon **précédent** la position d'insertion, car dans une liste simplement chaînée on ne peut pas revenir en arrière.

```c
Chainon *insertTrie(Chainon *pliste, int a) {
    if (pliste == NULL || a <= pliste->valeur) {
        return insertDebut(pliste, a);
    }
    Chainon *p = pliste;
    while (p->suivant != NULL && p->suivant->valeur < a) {
        p = p->suivant;
    }
    Chainon *c = creationChainon(a);
    c->suivant = p->suivant;   /* NULL si on insère en fin */
    p->suivant = c;
    return pliste;
}
```

L'ordre du test `p->suivant != NULL && p->suivant->valeur < a` est essentiel : grâce à l'évaluation paresseuse de `&&`, on ne lit jamais `valeur` d'un pointeur nul. Exemple testé : en insérant successivement 5, 1, 9, 3, 3, 0, 12 dans une liste vide, on obtient `0 -> 1 -> 3 -> 3 -> 5 -> 9 -> 12`. Coût : $O(n)$ dans le pire cas.

## Exercice 3 : Suppression de chaînon

**Énoncé.**

1. Définir une liste chaînée d'entiers composée de 10 `Chainon` dont les valeurs seront aléatoires entre 0 et 5 compris.
2. Écrire des fonctions prenant en paramètre un pointeur sur liste et un entier qui permettent de supprimer dans une liste :
    - le premier `Chainon` dont la valeur est égale au paramètre ;
    - tous les `Chainon` dont la valeur est égale au paramètre.
3. Tester ces fonctions avec la liste de la question 1.

**Correction.**

**1.** `rand() % 6` donne un entier entre 0 et 5. On initialise le générateur une seule fois avec `srand(time(NULL))` (bibliothèque `time.h`).

```c
Chainon *listeAleatoire(int n) {
    Chainon *l = NULL;
    for (int i = 0; i < n; i++) {
        l = insertDebut(l, rand() % 6);
    }
    return l;
}
```

**2.** Les deux fonctions retournent la nouvelle tête, car la tête elle-même peut être supprimée. On libère chaque chaînon retiré.

Suppression de la première occurrence : on traite à part le cas de la tête, puis on cherche le chaînon **précédant** celui à supprimer.

```c
Chainon *supprimePremier(Chainon *pliste, int x) {
    if (pliste == NULL) {
        return NULL;
    }
    if (pliste->valeur == x) {
        Chainon *suiv = pliste->suivant;
        free(pliste);
        return suiv;
    }
    Chainon *p = pliste;
    while (p->suivant != NULL && p->suivant->valeur != x) {
        p = p->suivant;
    }
    if (p->suivant != NULL) {      /* p->suivant contient x */
        Chainon *asupp = p->suivant;
        p->suivant = asupp->suivant;
        free(asupp);
    }
    return pliste;
}
```

Suppression de toutes les occurrences : on supprime d'abord toutes les têtes égales à `x` (il peut y en avoir plusieurs de suite), puis on parcourt en regardant le suivant. Quand on supprime `p->suivant`, on **n'avance pas** `p`, car le nouveau suivant peut lui aussi valoir `x`.

```c
Chainon *supprimeTous(Chainon *pliste, int x) {
    while (pliste != NULL && pliste->valeur == x) {
        Chainon *suiv = pliste->suivant;
        free(pliste);
        pliste = suiv;
    }
    if (pliste == NULL) {
        return NULL;
    }
    Chainon *p = pliste;           /* ici p->valeur != x */
    while (p->suivant != NULL) {
        if (p->suivant->valeur == x) {
            Chainon *asupp = p->suivant;
            p->suivant = asupp->suivant;
            free(asupp);
        } else {
            p = p->suivant;
        }
    }
    return pliste;
}
```

**3.** Programme de test :

```c
int main(void) {
    srand(time(NULL));
    Chainon *l = listeAleatoire(10);
    afficheListe(l);
    l = supprimePremier(l, 2);
    afficheListe(l);
    l = supprimeTous(l, 5);
    afficheListe(l);
    libereListe(l);
    return 0;
}
```

Exemple d'exécution : `5 -> 5 -> 0 -> 1 -> 4 -> 4 -> 3 -> 5 -> 0 -> 0` ; la suppression du premier 2 ne change rien (pas de 2) ; après suppression de tous les 5 : `0 -> 1 -> 4 -> 4 -> 3 -> 0 -> 0` (les deux 5 de tête et celui du milieu ont disparu).

## Exercice 4 : Inversion d'une liste

**Énoncé.**

- Écrire un programme qui permet de créer une liste chaînée inverse d'une autre liste (premier élément en dernier, deuxième en avant-dernier, etc.).
- Écrire un programme qui permet d'inverser une liste chaînée sans passer par une liste intermédiaire.

**Correction.**

**Avec une nouvelle liste.** On parcourt la liste d'origine et on insère chaque valeur **en tête** de la nouvelle liste : le premier élément lu finit en dernier. La liste d'origine est inchangée ; coût $O(n)$.

```c
Chainon *copieInverse(Chainon *pliste) {
    Chainon *inv = NULL;
    for (Chainon *p = pliste; p != NULL; p = p->suivant) {
        inv = insertDebut(inv, p->valeur);
    }
    return inv;
}
```

**Sur place.** On retourne les liens un à un avec trois pointeurs : `prec` (partie déjà inversée), `cour` (chaînon traité) et `suiv` (reste de la liste, à sauvegarder avant de modifier `cour->suivant`). Aucune allocation ; coût $O(n)$. La liste vide et la liste à un élément sont traitées sans cas particulier.

```c
Chainon *inverseEnPlace(Chainon *pliste) {
    Chainon *prec = NULL;
    Chainon *cour = pliste;
    while (cour != NULL) {
        Chainon *suiv = cour->suivant;
        cour->suivant = prec;
        prec = cour;
        cour = suiv;
    }
    return prec;              /* ancien dernier = nouvelle tête */
}
```

Test : à partir de `1 -> 2 -> 3 -> 4 -> 5`, les deux fonctions donnent `5 -> 4 -> 3 -> 2 -> 1`. Avec la copie, il faut libérer **les deux** listes à la fin.

## Exercice 5 : Gestion des étudiants

**Énoncé.** (Extrait du devoir de 2021/2022.) On souhaite gérer les notes et les informations de l'ensemble des étudiants de CY Tech.

1. Un étudiant de deuxième année est défini par son nom, son prénom, son groupe et ses notes. Plus précisément, chaque étudiant reçoit toujours 10 (constante) notes. Pour plus de facilité, le groupe de l'étudiant sera défini par un entier correspondant au numéro de son groupe (exemple : groupe 1, groupe 6, etc.). Définir la structure `Etudiant` permettant de stocker ces informations.
2. Comme on peut avoir des retards à l'inscription ou des étudiants qui partent en cours d'année, les étudiants vont être rangés dans une liste dynamique. Définir la ou les structures nécessaires pour construire la liste dynamique `LstEtudiants` des étudiants.
3. Écrire une fonction `saisirEtudiant(LstEtudiants lst)` qui permet de saisir les données d'un nouvel étudiant et de l'ajouter à la fin de la liste. Les notes seront aléatoires.
4. Proposer une procédure `listeParGroupe(LstEtudiants lst, int groupe)` permettant d'afficher le nom de tous les étudiants du groupe passé en paramètre.
5. Écrire une fonction `moyTab(int *tab)` qui prend en argument un tableau statique de taille N et qui renvoie la moyenne de ses éléments.
6. Écrire une fonction `trouveEtudiant(char *nom, char *prenom, LstEtudiants lst)` qui recherche un étudiant par son nom et son prénom et renvoie un pointeur sur l'étudiant ou `NULL` s'il n'existe pas.
7. Proposer un algorithme permettant de calculer la moyenne de l'élève dont le nom est « Spiruline Barnabus ». Afficher un message d'erreur si aucun élève de ce nom n'existe.
8. Calculer la moyenne de toute la promotion.
9. Afficher le nom de l'étudiant ayant la plus mauvaise moyenne de la promotion.

**Correction.**

**1.** Les notes sont dans un tableau statique de taille constante `N = 10`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 10
#define TAILLE_NOM 50

typedef struct {
    char nom[TAILLE_NOM];
    char prenom[TAILLE_NOM];
    int groupe;
    int notes[N];
} Etudiant;
```

**2.** Le prototype `saisirEtudiant(LstEtudiants lst)` reçoit la liste **par valeur** et ne retourne pas de nouvelle tête. Pour que l'ajout soit visible par l'appelant même quand la liste est vide, `LstEtudiants` est un pointeur vers une structure « descripteur » qui contient la tête (et la queue, pour ajouter en fin en $O(1)$) : on modifie le descripteur à travers le pointeur.

```c
typedef struct ChainonEtu {
    Etudiant etu;
    struct ChainonEtu *suivant;
} ChainonEtu;

typedef struct {
    ChainonEtu *tete;
    ChainonEtu *queue;
    int taille;
} Liste;

typedef Liste *LstEtudiants;

LstEtudiants creerListe(void) {
    LstEtudiants lst = malloc(sizeof(Liste));
    if (lst == NULL) {
        exit(EXIT_FAILURE);
    }
    lst->tete = NULL;
    lst->queue = NULL;
    lst->taille = 0;
    return lst;
}
```

**3.** On lit les chaînes avec `fgets` (pas de débordement) et on retire le `'\n'` final. La fonction retourne 1 en cas de succès, 0 sinon.

```c
void lireLigne(const char *message, char *buf, int taille) {
    printf("%s", message);
    if (fgets(buf, taille, stdin) == NULL) {
        buf[0] = '\0';
        return;
    }
    buf[strcspn(buf, "\n")] = '\0';
}

int saisirEtudiant(LstEtudiants lst) {
    if (lst == NULL) {
        return 0;
    }
    ChainonEtu *c = malloc(sizeof(ChainonEtu));
    if (c == NULL) {
        return 0;
    }
    char ligne[TAILLE_NOM];
    lireLigne("Nom : ", c->etu.nom, TAILLE_NOM);
    lireLigne("Prénom : ", c->etu.prenom, TAILLE_NOM);
    lireLigne("Groupe : ", ligne, TAILLE_NOM);
    c->etu.groupe = atoi(ligne);
    for (int i = 0; i < N; i++) {
        c->etu.notes[i] = rand() % 21;     /* note entre 0 et 20 */
    }
    c->suivant = NULL;
    if (lst->tete == NULL) {
        lst->tete = c;
    } else {
        lst->queue->suivant = c;
    }
    lst->queue = c;
    lst->taille++;
    return 1;
}
```

**4.**

```c
void listeParGroupe(LstEtudiants lst, int groupe) {
    if (lst == NULL) {
        return;
    }
    for (ChainonEtu *p = lst->tete; p != NULL; p = p->suivant) {
        if (p->etu.groupe == groupe) {
            printf("%s %s\n", p->etu.nom, p->etu.prenom);
        }
    }
}
```

**5.** On divise en flottant pour ne pas perdre la partie décimale.

```c
float moyTab(int *tab) {
    int somme = 0;
    for (int i = 0; i < N; i++) {
        somme += tab[i];
    }
    return (float)somme / N;
}
```

**6.** Les chaînes se comparent avec `strcmp` (et non `==`, qui comparerait des adresses).

```c
Etudiant *trouveEtudiant(char *nom, char *prenom, LstEtudiants lst) {
    if (lst == NULL) {
        return NULL;
    }
    for (ChainonEtu *p = lst->tete; p != NULL; p = p->suivant) {
        if (strcmp(p->etu.nom, nom) == 0 && strcmp(p->etu.prenom, prenom) == 0) {
            return &p->etu;
        }
    }
    return NULL;
}
```

**7.** Algorithme : chercher l'étudiant avec `trouveEtudiant` ; si le résultat est `NULL`, afficher un message d'erreur ; sinon afficher `moyTab` de ses notes.

> **Note :** on a pris « Spiruline » comme nom et « Barnabus » comme prénom ; l'énoncé ne précise pas l'ordre.

```c
void moyenneSpiruline(LstEtudiants lst) {
    Etudiant *e = trouveEtudiant("Spiruline", "Barnabus", lst);
    if (e == NULL) {
        printf("Erreur : aucun étudiant nommé Spiruline Barnabus\n");
    } else {
        printf("Moyenne de %s %s : %.2f\n", e->prenom, e->nom, moyTab(e->notes));
    }
}
```

**8.** Tous les étudiants ont le même nombre de notes, donc la moyenne de la promotion est la moyenne des moyennes individuelles. On évite la division par zéro si la liste est vide.

```c
float moyennePromo(LstEtudiants lst) {
    if (lst == NULL || lst->tete == NULL) {
        return 0;
    }
    float somme = 0;
    int nb = 0;
    for (ChainonEtu *p = lst->tete; p != NULL; p = p->suivant) {
        somme += moyTab(p->etu.notes);
        nb++;
    }
    return somme / nb;
}
```

**9.** Recherche classique d'un minimum, initialisé avec le premier étudiant.

```c
Etudiant *plusMauvais(LstEtudiants lst) {
    if (lst == NULL || lst->tete == NULL) {
        return NULL;
    }
    Etudiant *pire = &lst->tete->etu;
    float mini = moyTab(pire->notes);
    for (ChainonEtu *p = lst->tete->suivant; p != NULL; p = p->suivant) {
        float m = moyTab(p->etu.notes);
        if (m < mini) {
            mini = m;
            pire = &p->etu;
        }
    }
    return pire;
}
```

Dans le `main`, on affiche `plusMauvais(lst)->nom` après avoir vérifié que le pointeur n'est pas `NULL`, puis on libère tous les chaînons et le descripteur :

```c
void libereEtudiants(LstEtudiants lst) {
    if (lst == NULL) {
        return;
    }
    ChainonEtu *p = lst->tete;
    while (p != NULL) {
        ChainonEtu *suiv = p->suivant;
        free(p);
        p = suiv;
    }
    free(lst);
}
```
