---
title: DS1 2023 2024 Correction
author: [AhmedA]
date: 2024-03-19 01:00:00 +0100
categories: [PREING1 S2,Informatique2-DS]
tags: [PREING1 S2,Informatique2-DS,DS1,Ahmed A.]
division_title : DS1
---


Exercices : [1](#1) [2](#2)

<div id="1"></div>

## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/DS1-2023-2024-Correction_Informatique2-DSp1s2/exo1.jpg){: .w-75 .shadow .rounded-10 }

![exercice 1 fgg](https://data.cy.deltahmed.fr/DATA/DS1-2023-2024-Correction_Informatique2-DSp1s2/exo1_2.jpg){: .w-75 .shadow .rounded-10 }

+  On définie les structures et les constantes utiles
 

```c 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXCHAR 50 // Définition de la taille maximale d'une chaîne de caractères

typedef enum {
    FOOTBALL,
    PATINOIRE,
    OMNISPORT,
    PISCINE
} Type; // Déclaration d'une énumération pour les différents types de stades

typedef struct
{
    char nom[MAXCHAR]; // Nom de la ville
    int codepostal; // Code postal de la ville
    int pop; // Population de la ville
} Ville; // Déclaration de la structure pour une ville

typedef struct 
{
    char nom[MAXCHAR]; // Nom du stade
    int cap_max; // Capacité maximale du stade
    int surface; // Surface du stade
    int annee_constru; // Année de construction du stade
    Ville ville; // Ville où se trouve le stade
    Type type; // Type du stade
} Stade; // Déclaration de la structure pour un stade

``` 



+  On créer la fonction pour afficher les détails d'une ville
 

```c 
void afficheVille(Ville ville){
    printf("nom : %s \n code postal : %d \n population %d\n", ville.nom, ville.codepostal, ville.pop);
}

``` 


+  On créer la fonction pour calculer le ratio population/capacité maximale d'un stade
 

```c 
float calculerRatio(Stade stade){
    return stade.ville.pop / stade.cap_max;
}

``` 


+  On créer la fonction pour comparer deux stades en fonction de leur capacité maximale et de leur surface
 

```c 
int compareStade(Stade s1, Stade s2){
    if (s1.cap_max > s2.cap_max){
        return 1;
    } else if (s1.cap_max < s2.cap_max)
    {
        return -1;
    } else {
        if (s1.surface > s2.surface){
            return 1;
        } else if (s1.surface < s2.surface)
        {
            return -1;
        } else {
            return 0;
        }
    }
}

``` 


+  On créer la fonction pour vérifier si deux villes sont identiques
 

```c 
int memeVille(Ville v1, Ville v2){
    if (v1.nom == NULL || v2.nom == NULL){
        return -1;
    }
    return !strcmp(v1.nom, v2.nom) && ( v1.codepostal == v2.codepostal);
}

``` 


+  On créer la fonction pour vérifier si un stade est valide pour accueillir un certain type d'événement
 

```c 
int stadeValide(Stade stade){
    switch (stade.type)
    {
    case FOOTBALL:
        return stade.cap_max > (stade.ville.pop * 0.01);
    case PATINOIRE:
        return stade.surface > 1800;
    case OMNISPORT:
        return (stade.cap_max > (stade.ville.pop * 0.01)) && (stade.surface > 10000 );
    case PISCINE :
        return stade.surface > 1250;
    default:
        return 0;
    }
}

``` 


+  On créer la fonction pour vérifier si une ville est candidate pour accueillir les jeux olympiques
 

```c 
int villeOlympiques(Ville ville, Stade TabStade[], int taille){
    int nb_types[] = {0,0,0,0};
    for (int i = 0; i < taille; i++)
    {   
        if (stadeValide(TabStade[i]) && (memeVille(ville, TabStade[i].ville) == 1) ){
            nb_types[TabStade[i].type] += 1;
        }
    }
    for (int i = 0; i < 4; i++)
    {
        if (nb_types[i] == 0){
            return 0;
        }
    }
    return 1;
}

``` 


+  On créer la fonction pour afficher les villes candidates à accueillir les jeux olympiques
 

```c 
void villesCandidates(Ville Tabville[], int nb_villes, Stade TabStade[], int nb_stade ){
    for (int i = 0; i < nb_villes; i++)
    {
        if (villeOlympiques(Tabville[i], TabStade, nb_stade))
        {
            afficheVille(Tabville[i]);
        }
        
    }
    
}

``` 



+  Si vous voulez tester le code n'oublier pas de rajouter une fonction `main`
 

```c 
int main() {
    return 0;
}

``` 

<div id="2"></div>

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/DS1-2023-2024-Correction_Informatique2-DSp1s2/exo2.jpg){: .w-75 .shadow .rounded-10 }



+  On définie les structures et les constantes utiles
 

```c 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

``` 

+  On créer la fonction pour créer un tableau de scores initialisé à zéro pour un nombre de joueurs donné
 

```c 
int* Tableau_des_score(int nb_joueur){
    // Vérification du nombre de joueurs minimum
    if (nb_joueur < 50){
        printf("Pas assez de joueurs");
        exit(EXIT_FAILURE);
    }
    // Allocation dynamique de mémoire pour le tableau des scores
    int* TabScore = (int*)malloc(sizeof(int)*nb_joueur); //le (int*) est pas obligatoire
    // Vérification de l'allocation mémoire
    if (TabScore == NULL){
        printf("Erreur d'allocation memoire");
        exit(EXIT_FAILURE);
    }
    // Initialisation de tous les scores à zéro
    for (int i = 0; i < nb_joueur; i++)
    {
        TabScore[i] = 0;
    }
    
    return TabScore;
}

``` 


>  On peut aussi utiliser `calloc`, la boucle est donc inutile si on utilise `calloc` car `calloc` initialise de base tout a 0
{: .prompt-info }


> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-tip }


+  On créer la fonction pour mettre à jour le score d'un joueur donné
 

```c 
void majScore(int* TabScore, int numero_joueur, int valeur){
    *(TabScore + numero_joueur) += valeur;
}
```

+  On créer la fonction pour réallouer de la mémoire pour un tableau de scores en ajoutant des joueurs
 

```c 
int* reallocScore(int* TabScore, int Nb_joueur, int nb_a_ajouter){
    // Création d'un nouveau tableau de scores avec la taille mise à jour
    int* NewTabScore = Tableau_des_score( Nb_joueur + nb_a_ajouter );
    // Copie des scores du tableau initial vers le nouveau tableau
    for (int i = 0; i < Nb_joueur; i++)
    {
        NewTabScore[i] = TabScore[i];
    }
    // Libération de la mémoire du tableau initial
    free(TabScore);
    return NewTabScore;
    
}

``` 


>  On peut aussi utiliser `memcpy` pour faire la copie du tableau 
{: .prompt-info }


+  On créer la fonction pour déterminer le joueur avec le score le plus élevé
 

```c 
void HighScore(int* TabScore, int Taille, int* score_max, int* numero_joueur){
    // Initialisation du score maximum et du numéro de joueur
    *score_max = TabScore[0];
    *numero_joueur = 0;
    // Parcours de tous les scores pour trouver le maximum
    for (int i = 0; i < Taille; i++)
    {
        if (*score_max < TabScore[i]){
            *score_max = TabScore[i];
            *numero_joueur = i;
        }
        
    }
    
}

``` 


Exercices : [1](#1) [2](#2)