---
title: TD05 ABR Correction
author: [AhmedA,MathisS,RayaneM,SergueïM] 
date: 2024-12-03 01:00:00 +0100
categories: [PREING2 S1,Informatique3]
tags: [PREING2 S1,Informatique3,Ahmed A.,Mathis S.,Rayane M.,Sergueï M.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) [6](#6) 

<div id="1"></div>

## Exercice 1

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo1.jpg){: .w-75 .shadow .rounded-10 }

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo2.c){:target="_blank"} 

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo2.jpg){: .w-75 .shadow .rounded-10 }

+  On définit une structure représentant un nœud dans un arbre binaire
 

```c 
#include <stdio.h>  
#include <stdlib.h> 

typedef struct arbre_struct
{
    int value;               // La valeur contenue dans le nœud
    struct arbre_struct *fd; // Pointeur vers le sous-arbre droit
    struct arbre_struct *fg; // Pointeur vers le sous-arbre gauche
} Arbre;

typedef Arbre *pArbre;

``` 



+  On crée la fonction pour créer un nouveau nœud dans l'arbre
 

```c 
pArbre creeArbre(int e)
{
    // Allocation dynamique d'un nouveau nœud
    pArbre new = malloc(sizeof(Arbre));
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




+  On crée la fonction pour rechercher une valeur dans un arbre binaire
 

```c 
int recherche(pArbre a, int e)
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

``` 



+  On crée la fonction pour insérer une valeur dans un arbre binaire de recherche (récursive)
 

```c 
pArbre insertionABR(pArbre a, int e)
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

``` 



+  On crée la fonction pour insérer une valeur dans un arbre binaire de recherche (itérative)
 

```c 
pArbre insertionABR_iter(pArbre a, int e)
{
    if (a == NULL)
    { // Si l'arbre est vide, créer un nouveau nœud
        return creeArbre(e);
    }
    pArbre actual = a; // Initialisation d'un pointeur pour parcourir l'arbre
    while (actual != NULL)
    { // Boucle pour trouver la bonne position d'insertion
        if (e < actual->value)
        { // Explorer le sous-arbre gauche
            if (actual->fg == NULL)
            { // Si le sous-arbre gauche est vide, insérer ici
                actual->fg = creeArbre(e);
                break;
            }
            else
            {
                actual = actual->fg;
            }
        }
        else
        { // Explorer le sous-arbre droit
            if (actual->fd == NULL)
            { // Si le sous-arbre droit est vide, insérer ici
                actual->fd = creeArbre(e);
                break;
            }
            else
            {
                actual = actual->fd;
            }
        }
    }
    return a; // Retourner l'arbre modifié
}

``` 



+  On crée la fonction pour supprimer le plus grand élément dans un sous-arbre
 

```c 
pArbre suppMax(pArbre a, int *pe)
{
    pArbre tmp;
    if (a->fd != NULL)
    { // Si le sous-arbre droit existe, continuer à descendre
        a->fd = suppMax(a->fd, pe);
    }
    else
    {                   // Si le nœud courant est le plus grand
        *pe = a->value; // Stocker la valeur du nœud
        tmp = a;        // Sauvegarder l'adresse du nœud à libérer
        a = a->fg;      // Remonter le sous-arbre gauche
        free(tmp);      // Libérer la mémoire du nœud supprimé
    }
    return a; // Retourner le sous-arbre modifié
}

``` 



+  On crée la fonction pour supprimer une valeur dans un arbre binaire de recherche
 

```c 
pArbre supprimerABR(pArbre a, int e)
{
    pArbre tmp;
    if (a == NULL)
    { // Si l'arbre est vide, rien à supprimer
        return a;
    }
    if (e < a->value)
    { // Explorer le sous-arbre gauche si la valeur est plus petite
        a->fg = supprimerABR(a->fg, e);
    }
    else if (e > a->value)
    { // Explorer le sous-arbre droit si la valeur est plus grande
        a->fd = supprimerABR(a->fd, e);
    }
    else
    { // Si la valeur est trouvée
        if (a->fg == NULL)
        { // Si le sous-arbre gauche est vide
            tmp = a;
            a = a->fd; // Remonter le sous-arbre droit
            free(tmp); // Libérer la mémoire du nœud supprimé
        }
        else
        {                                      // Si le sous-arbre gauche existe
            a->fg = suppMax(a->fg, &a->value); // Remplacer avec le plus grand élément du sous-arbre gauche
        }
    }
    return a; // Retourner l'arbre modifié
}

``` 


<div id="3"></div>

## Exercice 3

![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo3.jpg){: .w-75 .shadow .rounded-10 }

<div id="4"></div>

## Exercice 4
[Télécharger l'exercice exo4.c](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo4.c){:target="_blank"} 

![exercice 4](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo4.jpg){: .w-75 .shadow .rounded-10 }

+  On définit d'une structure représentant un nœud d'un arbre binaire
 

```c 
#include <stdio.h> 
#include <stdlib.h>

typedef struct arbre_struct {
    int value; // La valeur contenue dans le nœud
    struct arbre_struct *fd; // Pointeur vers le sous-arbre droit
    struct arbre_struct *fg; // Pointeur vers le sous-arbre gauche
} Arbre;

typedef Arbre* pArbre;

``` 

+  On crée la fonction pour créer un nouveau nœud dans l'arbre
 

```c 
pArbre creeArbre(int e) {
    // Allocation dynamique pour un nouveau nœud
    pArbre new = malloc(sizeof(Arbre));
    if (new == NULL) { // Vérification de l'échec de l'allocation
        exit(EXIT_FAILURE); // Arrêt immédiat en cas d'erreur
    }
    // Initialisation du nœud avec la valeur donnée et des sous-arbres vides
    new->value = e;
    new->fd = NULL;
    new->fg = NULL;
    return new; // Retourne le nouveau nœud
}

``` 



+  On crée la fonction récursive pour vérifier si un sous-arbre droit respecte la propriété de l'ABR, Chaque nœud dans le sous-arbre droit doit être strictement supérieur à une valeur minimale `min`
 

```c 
int verifierDroit(Arbre *a, int min) {
    if (a == NULL) { // Si le sous-arbre est vide, il respecte la propriété
        return 1;
    }
    // Vérifie si le nœud courant respecte la propriété et applique la vérification récursive
    return (a->value > min) && verifierDroit(a->fg, min) && verifierDroit(a->fd, min);
}

``` 



+  On crée la fonction récursive pour vérifier si un sous-arbre gauche respecte la propriété de l'ABR, Chaque nœud dans le sous-arbre gauche doit être strictement inférieur à une valeur maximale `max`
 

```c 
int verifierGauche(Arbre *a, int max) {
    if (a == NULL) { // Si le sous-arbre est vide, il respecte la propriété
        return 1;
    }
    // Vérifie si le nœud courant respecte la propriété et applique la vérification récursive
    return (a->value < max) && verifierGauche(a->fg, max) && verifierGauche(a->fd, max);
}

``` 


+  On crée la fonction principale pour vérifier si un arbre est un ABR (Arbre Binaire de Recherche)
 

```c 
int estABR(pArbre a) {
    if (a == NULL) { // Si l'arbre est vide, c'est un ABR valide
        return 1;
    }
    // Vérifie si les sous-arbres gauche et droit respectent les propriétés de l'ABR
    if (!verifierGauche(a->fg, a->value) || !verifierDroit(a->fd, a->value)) {
        return 0; // Si une des propriétés est violée, ce n'est pas un ABR
    }
    // Vérifie récursivement les sous-arbres
    return estABR(a->fg) && estABR(a->fd);
}

``` 


<div id="5"></div>

## Exercice 5

![exercice 5](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo5.jpg){: .w-75 .shadow .rounded-10 }

<div id="6"></div>

## Exercice 6

![exercice 6](https://data2.cy.deltahmed.fr/DATA/info/TD5-ABR_Informatique3p2s1-2024-2025/exo6.jpg){: .w-75 .shadow .rounded-10 }

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) [6](#6) 
