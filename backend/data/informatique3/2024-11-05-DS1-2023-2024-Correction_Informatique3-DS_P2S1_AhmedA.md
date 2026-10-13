---
title: DS1 2023 2024 Correction
author: [AhmedA] 
date: 2024-11-05 01:00:00 +0100
categories: [PREING2 S1,Informatique3-DS]
tags: [PREING2 S1,Informatique3-DS,Ahmed A.,DS1]
math: true
mermaid: true
division_title : DS1
---

Exercices : [1](#1) [2](#2) 

<div id="1"></div>

## Exercice 1
[Télécharger l'exercice exo1.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2023-2024-Correction_Informatique3-DSp2s1/exo1.c){:target="_blank"} 

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/DS1-2023-2024-Correction_Informatique3-DSp2s1/exo1.jpg){: .w-75 .shadow .rounded-10 }

+  On inclut les bibliothèques nécessaires pour l'affichage et la gestion de la mémoire 
+ On définit la structure Chainon pour représenter un élément d'une liste chaînée, 
+ On définit la structure File pour représenter une file (queue) de chainons  
+ On crée la fonction qui crée un nouveau chainon avec la valeur 'a' et renvoie un pointeur vers celui-ci
 

```c 
#include <stdio.h>
#include <stdlib.h>

typedef struct chainon_struct
{
    int value; // Valeur stockée dans le chainon
    struct chainon_struct* next; // Pointeur vers le prochain chainon dans la liste
} Chainon;


typedef struct file_struct
{
    Chainon* tete; // Pointeur vers le sommet de la file (premier élément)
    Chainon* fin; // Pointeur vers le pied de la file (dernier élément)
    int nb; // Nombre d'éléments (personnes) dans la file
} File;


Chainon* creationChainon(int a) {
    Chainon* nouveau = malloc(sizeof(Chainon)); // Allocation mémoire pour un nouveau chainon
    if (nouveau == NULL) // Vérification de l'échec d'allocation
    {
        exit(EXIT_FAILURE); // Quitter le programme en cas d'échec
    }
    
    nouveau->value = a; // Initialisation de la valeur du chainon
    nouveau->next = NULL; // Le chainon est initialisé sans successeur
    return nouveau; // Retourne un pointeur vers le nouveau chainon
}

``` 


+  On crée la fonction pour ajouter un nouveau chainon dans la file pfile
 

```c 
void entrerFile(File* pfile) {
    int nb = 2 + rand() % 9; // Génère un nombre aléatoire entre 2 et 10 pour la taille du groupe
    if (pfile == NULL) // Vérification que la file existe
    {
        exit(EXIT_FAILURE);
    }
    if (pfile->fin == NULL) // Si la file est vide, initialise le premier élément
    {
        pfile->fin = creationChainon(nb); // Création du premier chainon
        pfile->tete = pfile->fin; // La tête et la fin pointent sur le même chainon
    } else {
        pfile->fin->next = creationChainon(nb); // Ajoute le nouveau chainon à la fin de la file
        pfile->fin = pfile->fin->next;
    }
    pfile->nb += nb; // Met à jour le nombre total dans la file
}

``` 


+  On crée la fonction qui permet de retirer le premier chainon de la file et mettre à jour le nombre de personnes
 

```c 
File* sortirFile(File* pfile, int* groupe) {
    if (pfile == NULL) // Vérifie que la file existe
    {
        exit(EXIT_FAILURE);
    }
    if (pfile->tete == NULL || pfile->fin == NULL) // Si la file est vide, renvoie la file inchangée
    {
        return pfile;
    }

    Chainon* tmp = pfile->tete->next; // Sauvegarde l'élément suivant de la tête
    *groupe = pfile->tete->value; // Stocke la valeur du premier élément
    pfile->nb -= *groupe; // Déduit ce nombre du total de la file
    free(pfile->tete); // Libère la mémoire de l'ancien premier élément
    pfile->tete = tmp; // Met à jour la tête de la file

    return pfile; // Retourne la file mise à jour
}

``` 


+  On crée la fonction qui vérifie si la file est pleine (>= 500 personnes)
 

```c 
int filePleine(File* pfile) {
    if (pfile == NULL) // Vérifie que la file existe
    {
        exit(EXIT_FAILURE);
    }
    return pfile->nb >= 500; // Retourne vrai si la file est pleine
}

``` 


+  On crée la fonction qui permet de remplir un train avec les groupes contenue dans la file
 

```c 
void remplirTrain(File* pfile) {
    if (pfile == NULL) // Vérifie que la file existe
    {
        exit(EXIT_FAILURE);
    }
    if (pfile->tete != NULL) // Si la file n'est pas vide
    {
        int groupe; // Taille du groupe retiré
        int reduction; // Facteur de réduction pour chaque rangée en fonction de la taille du groupe
        int nb_rangee = 8; // Nombre de rangées disponibles dans le train
        int nb_siege = nb_rangee * 4; // Nombre total de sièges dans le train
        
        while (nb_rangee > 0) // Tant qu'il reste des rangées
        {
            // Détermine le nombre de rangées à déduire en fonction de la taille du groupe
            if (pfile->tete->value <= 4)
            {
                reduction = 1;
            } else if (pfile->tete->value <= 8) {
                reduction = 2;
            } else {
                reduction = 3;
            }

            if (nb_rangee >= reduction) // Si assez de rangées sont disponibles
            {
                nb_rangee -= reduction; // Réduit le nombre de rangées
                sortirFile(pfile, &groupe); // Retire un groupe de la file
                nb_siege -= groupe; // Met à jour le nombre de sièges disponibles
            } else {
                nb_rangee = 0; // Si plus de rangées disponibles, sort de la boucle
            }
        }
        printf("Nombre de sièges vides : %d/%d\n", nb_siege, 4 * 8); // Affiche le nombre de sièges libres
    }
}

``` 


+  On crée la fonction qui permet de simuler une période de trois minutes dans la gestion de la file
 

```c 
void three_minutes(File* pfile) {
    if (pfile == NULL) // Vérifie que la file existe
    {
        exit(EXIT_FAILURE);
    }
    remplirTrain(pfile); // Remplit le train une première fois
    remplirTrain(pfile); // Remplit à nouveau le train
    
    for (int i = 0; i < 16; i++) // Effectue 16 entrées dans la file, sauf si elle est pleine
    {   
        if (!filePleine(pfile)) // Vérifie si la file n'est pas encore pleine
        {
            entrerFile(pfile); // Ajoute un groupe dans la file
        }
    }
}

``` 

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2023-2024-Correction_Informatique3-DSp2s1/exo2.c){:target="_blank"} 

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/DS1-2023-2024-Correction_Informatique3-DSp2s1/exo2.jpg){: .w-75 .shadow .rounded-10 }

+  On définit la structure Chainon pour représenter un élément d'une liste doublement chaînée
 

```c 
#include <stdio.h>
#include <stdlib.h>

typedef struct chainon_struct
{
    char* value; // Valeur stockée dans le chainon
    struct chainon_struct* prev; // Pointeur vers le chaînon précédent
    struct chainon_struct* next; // Pointeur vers le prochain chaînon
} Chainon;

``` 


+  On définit la structure Deque pour représenter une file doublement chaînée (Deque)
 

```c 
typedef struct deque_struct
{
    Chainon* tete; // Pointeur vers le sommet (début de la deque)
    Chainon* fin; // Pointeur vers la fin de la deque
    int nb; // Nombre d'éléments dans la deque
} Deque;

``` 


+  On nous donne les fonctions suivantes comme déjà écrites
 

```c 
Chainon* creerChainon(char* a);
void supprimerChainon(Chainon* a);

``` 


+  On crée la fonction qui ajoute un élément au début de la deque
 

```c 
void ajoutDebutDeque(Deque* pdeque, char* a) {
    if (pdeque == NULL || ((pdeque->tete == NULL) ^ (pdeque->fin == NULL)) || a == NULL) // Vérification des paramètres
    {
        exit(EXIT_FAILURE); // Quitte en cas d'erreur
    }
    if (pdeque->tete == NULL || pdeque->fin == NULL) // Si la deque est vide, initialise le premier élément
    {
        pdeque->tete = creerChainon(a); // Crée un nouveau chainon avec la valeur 'a'
        pdeque->fin = pdeque->tete; // La tête et la fin pointent sur le même chainon
    } else {
        pdeque->tete->prev = creerChainon(a); // Crée un nouveau chainon et le lie avant la tête actuelle
        pdeque->tete->prev->next = pdeque->tete; // Lie l'ancien sommet avec le nouveau chainon
        pdeque->tete = pdeque->tete->prev; // Met à jour la tête de la deque
    }
    pdeque->nb++; // Augmente le nombre d'éléments dans la deque
}

``` 



>  Le signe `^` est une operation booléenne correspond au $XOR$ appelé aussi "ou exclusif", on l'utilise car si un des deux est `NULL` et l'autre non alors il y'a un problème
{: .prompt-tip }


+  On crée la fonction qui supprime un élément de la fin de la deque
 

```c 
int supprimerFinDeque(Deque* pdeque) {
    if (pdeque == NULL || ((pdeque->tete == NULL) ^ (pdeque->fin == NULL))) // Vérification des paramètres
    {
        exit(EXIT_FAILURE);
    }
    if (pdeque->tete != NULL && pdeque->fin != NULL) // Si la deque contient des éléments
    {
        Chainon* tmp = pdeque->fin; // Sauvegarde le chainon actuel à la fin
        pdeque->fin = pdeque->fin->prev; // Déplace le pointeur de fin au chainon précédent
        free(tmp); // Libère la mémoire de l'ancien dernier chainon
        if (pdeque->fin == NULL) // Si la deque devient vide après la suppression
        {
            pdeque->tete = pdeque->fin; // Met la tête et la fin à NULL
        }
        pdeque->nb--; // Diminue le nombre d'éléments
        return 1; // Indique que la suppression a été effectuée
    }
    return 0; // Renvoie 0 si aucune suppression n'a eu lieu
}

``` 



+  On crée la fonction qui ajoute un élément en début d'historique dans la deque, et supprime l'élément le plus ancien si nécessaire
 

```c 
void ajoutHistorique(Deque* pdeque, char* a) {
    if (pdeque == NULL || ((pdeque->tete == NULL) ^ (pdeque->fin == NULL)) || a == NULL) // Vérification des paramètres
    {
        exit(EXIT_FAILURE);
    }
    ajoutDebutDeque(pdeque, a); // Ajoute l'élément en début de deque
    if (pdeque->nb > 10) // Si la deque contient plus de 10 éléments
    {
        supprimerFinDeque(pdeque); // Supprime l'élément le plus ancien (à la fin)
    }
}

``` 



+  On crée la fonction qui retourne la valeur de l'élément précédent dans l'historique
 

```c 
char* precedant(Deque* pdeque) {
    if (pdeque == NULL || ((pdeque->tete == NULL) ^ (pdeque->fin == NULL))) // Vérification des paramètres
    {
        exit(EXIT_FAILURE);
    }
    return pdeque->tete->prev->value; // Retourne la valeur de l'élément précédent en tête de la deque
}

``` 


Exercices : [1](#1) [2](#2) 
