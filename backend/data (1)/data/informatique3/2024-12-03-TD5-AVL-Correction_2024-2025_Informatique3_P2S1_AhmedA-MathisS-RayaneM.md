---
title: TD06 AVL Correction
author: [AhmedA,MathisS,RayaneM] 
date: 2024-12-03 01:00:00 +0100
categories: [PREING2 S1,Informatique3]
tags: [PREING2 S1,Informatique3,Ahmed A.,Mathis S.,Rayane M.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

Exercices : [1](#1) [2](#2) [3](#3) 


> Attention au plagiat pour vos projets : les professeurs sont très vigilants sur cela, même si je reprenend dans cette correction les mêmes fonctions que celles vues en cours.
{: .prompt-danger }

<div id="1"></div>

## Exercice 1

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/TD6-AVL_Informatique3p2s1-2024-2025/exo1.jpg){: .w-75 .shadow .rounded-10 }


<div id="2"></div>

## Exercice 2


![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/TD6-AVL_Informatique3p2s1-2024-2025/exo2.jpg){: .w-75 .shadow .rounded-10 }

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/TD6-AVL_Informatique3p2s1-2024-2025/exo2_2.jpg){: .w-75 .shadow .rounded-10 }



+  On définit de la structure pour un nœud AVL
 

```c 
#include <stdio.h>
#include <stdlib.h>

typedef struct avl_struct
{
    int value;             // La valeur du nœud
    int eq;                // Facteur d'équilibre (balance factor)
    struct avl_struct *fg; // Pointeur vers le fils gauche
    struct avl_struct *fd; // Pointeur vers le fils droit
} AVL;

``` 



+  On crée la fonction pour créer un nouveau nœud AVL
 

```c 
AVL* creerAVL(int e)
{
    // Alloue de la mémoire pour un nouveau nœud
    AVL* new = (AVL* )malloc(sizeof(AVL));
    if (new == NULL)
    {
        exit(EXIT_FAILURE); // Arrêt immédiat en cas d'erreur d'allocation
    }
    new->value = e; // Initialisation de la valeur
    new->fg = NULL; // Pas de fils gauche
    new->fd = NULL; // Pas de fils droit
    new->eq = 0;    // Facteur d'équilibre initialisé à 0
    return new;
}

``` 



+  Rotation gauche : 
 

```c 
AVL* rotationGauche(AVL* a)
{
    AVL* pivot = a->fd; // Le fils droit devient le pivot
    int eq_a = a->eq, eq_p = pivot->eq;

    a->fd = pivot->fg; // Le sous-arbre gauche du pivot devient le fils droit de `a`
    pivot->fg = a;     // `a` devient le fils gauche du pivot

    // Mise à jour des facteurs d'équilibre
    a->eq = eq_a - max(eq_p, 0) - 1;
    pivot->eq = min3(eq_a - 2, eq_a + eq_p - 2, eq_p - 1);

    return pivot; // Le pivot devient la nouvelle racine
}

``` 



+  Rotation droite :
 

```c 
AVL* rotationDroite(AVL* a)
{
    AVL* pivot = a->fg; // Le fils gauche devient le pivot
    int eq_a = a->eq, eq_p = pivot->eq;

    a->fg = pivot->fd; // Le sous-arbre droit du pivot devient le fils gauche de `a`
    pivot->fd = a;     // `a` devient le fils droit du pivot

    // Mise à jour des facteurs d'équilibre
    a->eq = eq_a - min(eq_p, 0) + 1;
    pivot->eq = max3(eq_a + 2, eq_a + eq_p + 2, eq_p + 1);

    return pivot; // Le pivot devient la nouvelle racine
}

``` 



+  Double rotation gauche : une rotation droite suivie d'une rotation gauche
 

```c 
AVL* doubleRotationGauche(AVL* a)
{
    a->fd = rotationDroite(a->fd);
    return rotationGauche(a);
}

``` 



+  Double rotation droite : une rotation gauche suivie d'une rotation droite
 

```c 
AVL* doubleRotationDroite(AVL* a)
{
    a->fg = rotationGauche(a->fg);
    return rotationDroite(a);
}

``` 



+  Fonction pour rééquilibrer un arbre AVL
 

```c 
AVL* equilibrerAVL(AVL* a)
{
    if (a->eq >= 2)
    { // Cas où l'arbre est déséquilibré à droite
        if (a->fd->eq >= 0)
        {
            return rotationGauche(a); // Rotation simple gauche
        }
        else
        {
            return doubleRotationGauche(a); // Double rotation gauche
        }
    }
    else if (a->eq <= -2)
    { // Cas où l'arbre est déséquilibré à gauche
        if (a->fg->eq <= 0)
        {
            return rotationDroite(a); // Rotation simple droite
        }
        else
        {
            return doubleRotationDroite(a); // Double rotation droite
        }
    }
    return a; // Aucun rééquilibrage nécessaire
}

``` 



+  Fonction pour insérer un élément dans un arbre AVL
 

```c 
AVL* insertionAVL(AVL* a, int e, int *h)
{
    if (a == NULL)
    {           // Si l'arbre est vide, crée un nouveau nœud
        *h = 1; // La hauteur a augmenté
        return creerAVL(e);
    }
    else if (e < a->value)
    { // Si l'élément est plus petit, insérer à gauche
        a->fg = insertionAVL(a->fg, e, h);
        *h = -*h; // Inverse l'impact de la hauteur
    }
    else if (e > a->value)
    { // Si l'élément est plus grand, insérer à droite
        a->fd = insertionAVL(a->fd, e, h);
    }
    else
    { // Élément déjà présent
        *h = 0;
        return a;
    }

    // Mise à jour du facteur d'équilibre et rééquilibrage si nécessaire
    if (*h != 0)
    {
        a->eq += *h;
        a = equilibrerAVL(a);
        *h = (a->eq == 0) ? 0 : 1; // Mise à jour de la hauteur
    }
    return a;
}

``` 



+  Suppression du plus petit élément dans un AVL
 

```c 
AVL* suppMinAVL(AVL* a, int *h, int *pe)
{
    AVL* temp;
    if (a->fg == NULL)
    {                   // Trouvé le plus petit élément
        *pe = a->value; // Sauvegarde la valeur
        *h = -1;        // Réduction de la hauteur
        temp = a;
        a = a->fd; // Le sous-arbre droit devient la racine
        free(temp);
        return a;
    }
    else
    {
        a->fg = suppMinAVL(a->fg, h, pe); // Recherche récursive à gauche
        *h = -*h;
    }

    // Mise à jour et rééquilibrage après suppression
    if (*h != 0)
    {
        a->eq += *h;
        a = equilibrerAVL(a);
        *h = (a->eq == 0) ? -1 : 0;
    }
    return a;
}

``` 



+  Suppression d'un élément dans un AVL
 

```c 
AVL* suppressionAVL(AVL* a, int e, int *h)
{
    AVL* temp;
    if (a == NULL)
    { // Élément introuvable
        *h = 0; //attenttion faute dans le CM
        return a;
    }
    if (e > a->value)
    { // Recherche dans le sous-arbre droit
        a->fd = suppressionAVL(a->fd, e, h);
    }
    else if (e < a->value)
    { // Recherche dans le sous-arbre gauche
        a->fg = suppressionAVL(a->fg, e, h);
        *h = -*h;
    }
    else if (a->fd != NULL)
    { // Si le nœud a un fils droit
        a->fd = suppMinAVL(a->fd, h, &(a->value));
    }
    else
    { // Cas du nœud feuille ou avec un seul fils gauche
        temp = a;
        a = a->fg;
        free(temp);
        *h = -1;
        return a;
    }
    if (a==NULL)
    {
        return a;
    }
    // Mise à jour et rééquilibrage après suppression
    if (*h != 0)
    {
        a->eq += *h;
        a = equilibrerAVL(a);
        *h = (a->eq == 0) ? -1 : 0;
    }
    return a;
}

``` 


<div id="3"></div>

## Exercice 3

![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/TD6-AVL_Informatique3p2s1-2024-2025/exo3.jpg){: .w-75 .shadow .rounded-10 }

Exercices : [1](#1) [2](#2) [3](#3) 
