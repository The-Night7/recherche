---
title: DS2 2023 2024 V2 Correction
author: [AhmedA] 
date: 2024-12-04 01:00:00 +0100
categories: [PREING2 S1,Informatique3-DS]
tags: [PREING2 S1,Informatique3-DS,Ahmed A.,DS2]
math: true
mermaid: true
division_title : DS2
---

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 

<div id="1"></div>

## Exercice 1
[Télécharger l'exercice exo1.c](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo1.c){:target="_blank"} 

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo1.jpg){: .w-75 .shadow .rounded-10 }

+   1. Déclarer la structure ABR qui va contenir un entier comme valeur, et 2 pointeurs vers d’autres structures ABR.
 

```c 

#include <stdio.h>
#include <stdlib.h>

typedef struct arbre_struct
{
    int value;
    struct arbre_struct* fd;
    struct arbre_struct* fg;
} Arbre;
```

+   2. Déclarer la structure Chainon d’une liste, qui va contenir un entier comme valeur et un pointeur vers le prochain chainon de la liste.
 

```c 

typedef struct chainon_struct
{
    int value; // Valeur stockée dans le chainon
    struct chainon_struct* next; // Pointeur vers le prochain chainon
} Chainon;

``` 



+  Ecrire une fonction conversion(...) qui prend en paramètre simplement l’ABR
 

```c 

Chainon* creationChainon(int a){
    Chainon* nouveau = malloc(sizeof(Chainon)); // Allocation mémoire pour un nouveau chainon
    if (nouveau == NULL) // Vérification de l'échec d'allocation
    {
        exit(EXIT_FAILURE); // Quitter le programme en cas d'échec
    }
    
    nouveau->value = a; // Initialisation de la valeur du chainon
    nouveau->next = NULL; // Le chainon est initialisé sans successeur
    return nouveau; // Retourne un pointeur vers le nouveau chainon
}

Chainon* insertDebut(Chainon* pliste, int a){
    if (pliste == NULL) // Si la liste est vide
    {
        pliste = creationChainon(a); // Créer un nouveau chainon
    } else {
        Chainon* nouveau = creationChainon(a); // Créer un nouveau chainon
        nouveau->next = pliste; // L'ancien premier élément devient le suivant du nouveau chainon
        pliste = nouveau; // Le nouveau chainon devient le premier de la liste
    }
    return pliste; // Retourner la nouvelle tête de liste
}

Chainon* conversionREC(Arbre* a, Chainon* pliste){
    if (pliste == NULL)
    {
        exit(EXIT_FAILURE);
    }
    if (a != NULL)
    {
        pliste = conversionREC(a->fd, pliste); // inverse du parcours cars on insert au debut
        pliste = insertDebut(pliste, a);
        pliste = conversionREC(a->fg, pliste);
    }
    return pliste;
    
}

Chainon* conversion(Arbre* a){
    return conversionREC(a, NULL);
}

``` 

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo2.c){:target="_blank"} 

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo2.jpg){: .w-75 .shadow .rounded-10 }


+  En utilisant la structure ABR déclarée dans l’exercice précédente, écrire une fonction transformation(...) 
 

```c 
#include <stdio.h>
#include <stdlib.h>

typedef struct arbre_struct
{
    int value;
    struct arbre_struct* fd;
    struct arbre_struct* fg;
} Arbre;


Arbre* transformationREC(Arbre* a, int* sum){
    if (sum == NULL)
    {
        exit(EXIT_FAILURE);
    }
    int tmp;
    if (a == NULL)
    {
        return a;
    }
    transformationREC(a->fg, sum);
    tmp = *sum;
    *sum += a->value;
    a->value = tmp;
    transformationREC(a->fd, sum);
    return a;
}

Arbre* transformation(Arbre* a){
    int sum = 0;
    return transformationREC(a, &sum);
}

``` 


<div id="3"></div>

## Exercice 3
[Télécharger l'exercice exo3.c](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo3.c){:target="_blank"} 

![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo3.jpg){: .w-75 .shadow .rounded-10 }


+   Ecrire la fonction `intersection(...)`
 

```c 
#include <stdio.h>
#include <stdlib.h>

typedef struct arbre_struct
{
    int value;
    struct arbre_struct* fd;
    struct arbre_struct* fg;
} Arbre;

Arbre* creeArbre(int e)
{
    // Allocation dynamique d'un nouveau nœud
    Arbre* new = malloc(sizeof(Arbre));
    if (new == NULL)
    {                       // Vérification si l'allocation a échoué
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'échec
    }
    // Initialisation du nœud avec la valeur donnée et des sous-arbres vides
    new->value = e;
    new->fd = NULL;
    new->fg = NULL;
    return new; // Retourne le nouveau nœud
}

Arbre* insertionABR(Arbre* a, int e)
{
    if (a == NULL)
    { // Si l'arbre est vide, créer un nouveau nœud
        return creeArbre(e);
    }
    if (e < a->value)
    { // Si la valeur est plus petite, insérer dans le sous-arbre gauche
        a->fg = insertionABR(a->fg, e);
    }
    else
    { // Sinon, insérer dans le sous-arbre droit
        a->fd = insertionABR(a->fd, e);
    }
    return a; // Retourner l'arbre modifié
}

int recherche(Arbre* a, int e)
{
    if (a == NULL)
    { // Si l'arbre est vide, la valeur n'existe pas
        return 0;
    }
    if (a->value == e)
    { // Si la valeur est trouvée, retourner 1
        return 1;
    }
    if (e < a->value)
    { // Si la valeur recherchée est plus petite, explorer le sous-arbre gauche
        return recherche(a->fg, e);
    }
    // Sinon, explorer le sous-arbre droit
    return recherche(a->fd, e);
}

void intersectionREC(Arbre* src1, Arbre* src2, Arbre** dest){
    if (src1 != NULL || src2 != NULL)
    {
        if (recherche(src2, src1->value))
        {
            *dest = insertionABR(dest, src1->value);
        }
        intersectionREC(src1->fg, src2, dest);
        intersectionREC(src1->fd, src2, dest);
    }
    *dest = NULL;
}

Arbre* intersection(Arbre* src1, Arbre* src2){
    Arbre* dest = NULL;
    intersectionREC(src1, src2, &dest);
    return dest;
}
```


<div id="4"></div>

## Exercice 4
[Télécharger l'exercice exo4.c](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo4.c){:target="_blank"} 

![exercice 4](https://data2.cy.deltahmed.fr/DATA/info/DS2-2023-2024-V2_Informatique3-DSp2s1/exo4.jpg){: .w-75 .shadow .rounded-10 }

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct arbre_struct
{
    int value;
    struct arbre_struct* fd;
    struct arbre_struct* fg;
} Arbre;
```


+   1. Ecrire la fonction `CreationArbre(valeur) `
 

```c 
Arbre* CreationArbre(int e)
{
    // Allocation dynamique d'un nouveau nœud
    Arbre* new = malloc(sizeof(Arbre));
    if (new == NULL)
    {                       // Vérification si l'allocation a échoué
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'échec
    }
    // Initialisation du nœud avec la valeur donnée et des sous-arbres vides
    new->value = e;
    new->fd = NULL;
    new->fg = NULL;
    return new; // Retourne le nouveau nœud
}
```


+   2. Ecrire la fonction `AjoutNoeud(arbre,valeur)`
 

```c 

Arbre* AjoutNoeudREC(Arbre* a, int e, int div)
{
    if (a == NULL)
    { 
        return creeArbre(e);
    }
    if (e%div)
    { 
        a->fd = AjoutNoeudREC(a->fd, e, div+1);
    }
    else
    { 
        a->fg = AjoutNoeudREC(a->fg, e, div+1);
    }
    return a; 
}

Arbre* AjoutNoeud(Arbre* a, int e)
{   
    int div = 2;
    return  AjoutNoeudREC(a, e, div);
}

``` 


+  Où se trouvera un noeud contenant un nombre premier dans un tel arbre ? impossible de détérminer car si on veut inserer un x, si l'arbre à une hauteur inférieur strictement à x, x sera tout à droite, mais si l'arbre à une auteur supérieur à x alors on ne peut pas déterminer 
 

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 
