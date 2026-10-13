---
title: DS2 2024 2025 V1 Correction
author: [MathisS]
date: 2024-12-04 01:00:00 +0100
categories: [PREING2 S1,Informatique3-DS]
tags: [PREING2 S1,Informatique3-DS,Mathis S.,DS2]
division_title : DS2
---

Exercices : [1](#exercice-1) [1](#exercice-2) [1](#exercice-3) 

Correction proposée par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)

+ On écrit les fonctions de base pour tout le DS

```c 
#include <stdio.h>
#include <stdlib.h>

int max(int a,int b) {
    return a > b ? a : b;
}
int min(int a,int b) {
    return a > b ? b : a;
}

typedef struct Arbre
{
    int data;
    struct Arbre* fg;
    struct Arbre* fd;
}
Arbre;

Arbre* creerNoeud(int elmt)
{
    Arbre* a = malloc(sizeof(Arbre));
    a->data = elmt;
    a->fg = NULL;
    a->fd = NULL;
    return a;
}
```

## Exercice 1

```c
int afficherAncetres(Arbre* racine, int elmt)
{
    if (racine == NULL)
    {
        return 0;
    }
    if (racine->data == elmt)
    {
        return 1;
    }
    if (afficherAncetres(racine->fg, elmt) || afficherAncetres(racine->fd, elmt))
    {
        printf("%d\n", racine->data);
        return 1;
    }
    return 0;
}
```

## Exercice 2

```c
int hauteur(Arbre* a)
{
    if (a == NULL)
    {
        return -1;
    }
    return 1 + max(hauteur(a->fg), hauteur(a->fd));
}

int equilibreNoeud(Arbre* a)
{
    if (a == NULL)
    {
        return 0;
    }
    return hauteur(a->fd) - hauteur(a->fg);
}
// ComplexitÃ© O(n)

int equilibre(Arbre* a, Arbre** lePire)
{
    int eqfg;
    int eqfd;
    int eq, eq_pire;

    if (a == NULL)
    {
        return 1;
    }

    eqfg = equilibre(a->fg, lePire);
    eqfd = equilibre(a->fd, lePire);
    eq = equilibreNoeud(a);
    eq = (eq < 0) ? (-eq) : eq;
    eq_pire = equilibreNoeud(*lePire);
    eq_pire = (eq_pire < 0) ? (-eq_pire) : eq_pire;

    if (*lePire == NULL)
    {
        *lePire = a;
    }
    else if (equilibreNoeud(*lePire) < eq)
    {
        *lePire = a;
    }

    return (eq == 0) && eqfg && eqfd;
}

int max3(int a, int b, int c)
{
    return max(max(a,b), c);
}

int diametre(Arbre* a)
{
    if (a == NULL)
    {
        return -1;
    }
    return max3(diametre(a->fg), diametre(a->fd), hauteur(a->fg) + hauteur(a->fd) + 1);
}
```


## Exercice 3

```c
int recherche(Arbre* pA, int valeur);
Arbre* ajout(Arbre* pA, int valeur);

void intersectionABR(Arbre* a1, Arbre* a2, Arbre** pa3)
{
    if (pa3 == NULL)
    {
        exit(2);
    }
    if (a1 != NULL)
    {
        if (recherche(a2, a1->data))
        {
            *pa3 = ajout(*pa3, a1->data);
        }
        intersectionABR(a1->fg, a2, pa3);
        intersectionABR(a1->fd, a2, pa3);
    }
}
```

Exercices : [1](#exercice-1) [1](#exercice-2) [1](#exercice-3) 