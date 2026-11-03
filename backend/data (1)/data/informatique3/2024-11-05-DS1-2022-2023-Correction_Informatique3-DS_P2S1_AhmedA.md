---
title: DS1 2022 2023 Correction
author: [AhmedA] 
date: 2024-11-05 01:00:00 +0100
categories: [PREING2 S1,Informatique3-DS]
tags: [PREING2 S1,Informatique3-DS,Ahmed A.,DS1]
math: true
mermaid: true
division_title : DS1
---

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 

<div id="1"></div>

## Exercice 1

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo1.jpg){: .w-75 .shadow .rounded-10 }

$$  \begin{pmatrix} 
    P1 \\
    23 \\
    \downarrow  \\
    67 \\
    \downarrow  \\
    51 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 1  \rightarrow  17  \rightarrow   28  \rightarrow   59  \rightarrow   60  \rightarrow   57 
}}$$


$$  \begin{pmatrix} 
    P1 \\
    67 \\
    \downarrow  \\
    51 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 1  \rightarrow  17  \rightarrow   28  \rightarrow   59  \rightarrow   60  \rightarrow   57 \rightarrow 23
}}$$

$$  \begin{pmatrix} 
    P1 \\
    1 \\
    \downarrow  \\
    67 \\
    \downarrow  \\
    51 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 17  \rightarrow   28  \rightarrow   59  \rightarrow   60  \rightarrow   57 \rightarrow 23
}}$$

$$  \begin{pmatrix} 
    P1 \\
    51 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 17  \rightarrow   28  \rightarrow   59  \rightarrow   60  \rightarrow   57 \rightarrow 23
}}$$

$$  \begin{pmatrix} 
    P1 \\
    51 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 59  \rightarrow   60  \rightarrow   57 \rightarrow 23
}}$$


$$  \begin{pmatrix} 
    P1 \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 59  \rightarrow   60  \rightarrow   57 \rightarrow 23 \rightarrow 51
}}$$


$$  \begin{pmatrix} 
    P1 \\
    59 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 60  \rightarrow   57 \rightarrow 23 \rightarrow 51
}}$$


$$  \begin{pmatrix} 
    P1 \\
    59 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 60  \rightarrow   57 \rightarrow 23 \rightarrow 51 \rightarrow 99
}}$$

$$  \begin{pmatrix} 
    P1 \\
    60 \\ 
    \downarrow  \\
    59 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 57 \rightarrow 23 \rightarrow 51 \rightarrow 99
}}$$

$$  \begin{pmatrix} 
    P1 \\
    59 \\ 
    \downarrow  \\
    42 \\ 
    \downarrow  \\
    14 \\ 
    \downarrow  \\
    5 \\
\end{pmatrix}  
\overline{\underline{
    F1: 57 \rightarrow 23 \rightarrow 51 \rightarrow 99 \rightarrow 60
}}$$

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo2.c){:target="_blank"} 

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo2.jpg){: .w-75 .shadow .rounded-10 }

+  On définit la structure ChainonD pour représenter un élément d'une liste chaînée doublement chaînée
 

```c 
#include <stdlib.h>
#include <stdio.h>

typedef struct ChainonD_struct
{
    char value; // Valeur stockée dans le chainon
    struct ChainonD_struct* prev; // Pointeur vers le chaînon précédent
    struct ChainonD_struct* next; // Pointeur vers le prochain chaînon
} ChainonD;

``` 


+  On crée la fonction qui alloue et initialise un nouveau chainon avec la valeur 'nb'
 

```c 
ChainonD* creationChainonD(char nb) {
    ChainonD* new = malloc(sizeof(ChainonD)); // Allocation mémoire pour un nouveau chainon
    if (new == NULL) // Vérification si l'allocation a échoué
    {
        exit(EXIT_FAILURE); // Quitte le programme en cas d'échec
    }
    new->next = NULL; // Initialisation du pointeur suivant à NULL
    new->prev = NULL; // Initialisation du pointeur précédent à NULL
    new->value = nb; // Assignation de la valeur au chainon
    return new; // Retourne un pointeur vers le nouveau chainon
}

``` 


+  On crée la fonction qui insère un élément à une position donnée dans la liste chaînée
 

```c 
ChainonD* insertPos(ChainonD* tete, int pos, char c) {
    if (tete == NULL) // Si la liste est vide
    {
        return creationChainonD(c); // Crée un nouveau chainon qui sera la tête
    }
    
    ChainonD* actual = tete; // Pointeur pour parcourir la liste
    int i = 0; // Compteur pour la position
    // On parcourt la liste jusqu'à la position désirée ou la fin de la liste
    while (actual->next != NULL && i < pos - 1) 
    {   
        actual = actual->next; // Avance au chainon suivant
        i++; // Incrémente le compteur
    }
    
    ChainonD* tmp = actual->next; // Sauvegarde le chainon suivant à la position d'insertion
    actual->next = creationChainonD(c); // Crée et insère le nouveau chainon
    actual->next->next = tmp; // Lie le nouveau chainon au chainon suivant
    actual->next->prev = actual; // Lie le nouveau chainon au chainon précédent

    if (tmp != NULL) // Si un chainon suivant existe
    {
        tmp->prev = actual->next; // Met à jour le lien du chainon suivant
    }
    
    return tete; // Retourne la tête de la liste (inchangée)
}

``` 


+  On crée la fonction qui affiche les caractères majuscules de la liste chaînée
 

```c 
void afficheMaj(ChainonD* tete) {
    ChainonD* actual = tete; // Pointeur pour parcourir la liste
    while (actual != NULL) // Parcourt tous les chainons de la liste
    {   
        // Vérifie si le caractère est une lettre majuscule
        if ('A' <= actual->value && actual->value < 'Z') 
        {
            printf("%c \n", actual->value); // Affiche le caractère
        }
        
        actual = actual->next; // Avance au chainon suivant
    }
}

``` 

<div id="3"></div>

## Exercice 3
[Télécharger l'exercice exo3.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo3.c){:target="_blank"} 

![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo3.jpg){: .w-75 .shadow .rounded-10 }

![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo3_2.jpg){: .w-75 .shadow .rounded-10 }

+ La structure la plus adaptée est une pile

+  On définie la structure Disque pour représenter un disque
 

```c 
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

typedef struct chainon_struct
{
    int value; // Valeur (diamètre) du disque
    struct chainon_struct* next; // Pointeur vers le disque suivant
} Disque;

``` 


+  On définie la structure Tour pour représenter une tour de disques
 

```c 
typedef struct tour_struct
{
    Disque* tete; // Pointeur vers le disque du dessus de la tour
    int len; // Longueur (nombre de disques) de la tour
} Tour;

``` 


+  On crée la fonction qui enlève le disque du dessus de la tour et retourne sa valeur
 

```c 
int enleverDisque(Tour* ptour){
    if (ptour == NULL) // Vérifie si la tour est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    if (ptour->tete == NULL || ptour->len < 1 ) // Vérifie si la tour est vide
    {
        return 0; // Retourne 0 si la tour est vide
    }
    
    int val = ptour->tete->value; // Sauvegarde la valeur du disque
    Disque* tmp = ptour->tete->next; // Sauvegarde le pointeur vers le disque suivant
    free(ptour->tete); // Libère la mémoire allouée pour le disque du dessus
    ptour->tete = tmp; // Met à jour le pointeur vers le disque du dessus
    ptour->len--; // Réduit la longueur de la tour
    return val; // Retourne la valeur du disque enlevé
}

``` 


+  On crée la fonction qui crée un nouveau disque avec le diamètre spécifié
 

```c 
Disque* creerDisque(int diam){
    Disque* d = (Disque*)malloc(sizeof(Disque)); // Allocation mémoire pour un nouveau disque
    if (d == NULL) // Vérification si l'allocation a échoué
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'échec
    }
    d->next = NULL; // Le disque n'a pas de disque suivant
    d->value = diam; // Assigne la valeur (diamètre) du disque
    return d; // Retourne un pointeur vers le disque créé
}

``` 


+  On crée la fonction qui ajoute un disque à une tour en respectant l'ordre décroissant des diamètres
 

```c 
int ajouterDisque(Tour* ptour, int diam){
    if (ptour == NULL) // Vérifie si la tour est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    if (ptour->tete == NULL) // Si la tour est vide
    {
        ptour->tete = creerDisque(diam); // Crée le premier disque et le place en tête
        ptour->len++; // Augmente la longueur de la tour
        return 1;
    }
    if (ptour->tete->value > diam) // Si le disque à ajouter est plus petit que celui du dessus
    {
        Disque* d = creerDisque(diam); // Crée un nouveau disque
        d->next = ptour->tete; // Relie le nouveau disque au disque du dessus
        ptour->tete = d; // Le nouveau disque devient le disque du dessus
        ptour->len++; // Augmente la longueur de la tour
        return 1;
    }
    return 0; // Retourne 0 si l'ajout du disque échoue (disque trop grand)
}

``` 


+  On crée la fonction qui affiche tous les disques d'une tour
 

```c 
void afficheTour(Tour* ptour){
    if (ptour == NULL) // Vérifie si la tour est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    Disque* actual = ptour->tete; // Pointeur pour parcourir les disques de la tour
    while (actual != NULL) // Parcourt tous les disques de la tour
    {     
        printf("%d \n", actual->value); // Affiche la valeur (diamètre) du disque
        actual = actual->next; // Avance au disque suivant
    }
}

``` 


+  On crée la fonction qui effectue une lecture sécurisée d'un entier dans une plage de nombre spécifiée
 

```c 
int better_scan(char* message, int min, int max){
    if (message == NULL)   // Vérifie si le message est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    
    int retvar = 0;
    int value = min-1;
    // C'est mieux d'utiliser un do while, c'est une mauvaise habitude de ma part
    while (min > value || value > max || retvar != 1 )
    {   
        printf("%s", message); // Affiche le message pour demander la valeur
        retvar = scanf("%d", &value); // Lit l'entier entré par l'utilisateur
        while (getchar()!='\n'); // Nettoie le buffer pour éviter des entrées incorrectes
    }
    return value; // Retourne la valeur valide entrée par l'utilisateur
}

``` 


>  `while (getchar()!='\n');` est equivalent a `while (getchar()!='\n'){}`
{: .prompt-tip }


+  On crée la fonction principale pour résoudre le problème des tours de Hanoi avec 3 tours
 

```c 
int main(){
    srand(time(NULL)); // Initialise le générateur de nombres aléatoires
    
    Tour tours[3]; // Déclaration de 3 tours
    for (int i = 0; i < 3; i++)
    {
        tours[i].tete = NULL; // Initialisation de la tête des tours à NULL
        tours[i].len = 0; // Initialisation de la longueur des tours à 0
    }
    
    int nb = better_scan("Entrer Nombre de disques \n", 3, 10); // Demande à l'utilisateur le nombre de disques
    int tour_dep, tour_fin;
    int disque;
    // On ajoute les disques sur la première tour en ordre décroissant
    for (int i = nb; i > 0; i--)
    {  
        ajouterDisque(tours,  i); // Ajoute un disque sur la première tour
    }
    
    // On commence à déplacer les disques jusqu'à ce que la dernière tour ait tous les disques
    while (tours[2].len < nb)
    {   
        // Demande à l'utilisateur de sélectionner une tour de départ
        tour_dep = better_scan("Entrer le numero de tour 1-3 ou on enlève un disque\n", 1, 3);
        tour_dep--;
        disque = enleverDisque(tours + tour_dep); // Enlève un disque de la tour sélectionnée
        if (disque) // Si un disque a été enlevé
        {
            // Demande à l'utilisateur de sélectionner une tour de destination
            tour_fin = better_scan("Entrer le numero de tour 1-3 ou on ajoute un disque\n", 1, 3);
            tour_fin--;
            if (!ajouterDisque(tours + tour_fin, disque)) // Si l'ajout du disque échoue (disque trop grand)
            {
                printf("Le disque est plus grand que le disque en dessous \n");
                ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
            }
        } else
        {
            printf("La tour est vide \n");
            ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
        }
        
        // Affiche l'état actuel des 3 tours
        for (int i = 0; i < 3; i++)
        {   
            printf("Tour %d :\n", i+1);
            afficheTour(tours+i);
        }
    }

    return 0;
}

``` 


+  On crée la fonction principale avec un nombre variable de tours
 

```c 
int main(){
    srand(time(NULL)); // Initialise le générateur de nombres aléatoires

    int nb_tours = better_scan("Entrer Nombre de Tours \n", 3, 20); // Demande à l'utilisateur le nombre de tours
    Tour* tours = malloc(sizeof(int) * 20); // Allocation mémoire pour un tableau de tours (max 20)
    for (int i = 0; i < nb_tours; i++)
    {
        tours[i].tete = NULL; // Initialisation de la tête des tours à NULL
        tours[i].len = 0; // Initialisation de la longueur des tours à 0
    }
    
    int nb = better_scan("Entrer Nombre de disques \n", 3, 500); // Demande à l'utilisateur le nombre de disques
    int tour_dep, tour_fin;
    int disque;
    // On ajoute les disques sur la première tour en ordre décroissant
    for (int i = nb; i > 0; i--)
    {  
        ajouterDisque(tours,  i); // Ajoute un disque sur la première tour
    }
    
    // On commence à déplacer les disques jusqu'à ce que la dernière tour ait tous les disques
    while (tours[nb_tours-1].len < nb)
    {   
        // Demande à l'utilisateur de sélectionner une tour de départ
        tour_dep = better_scan("Entrer le numero de tour 1-nb_tours ou on enlève un disque\n", 1, nb_tours);
        tour_dep--;
        disque = enleverDisque(tours + tour_dep); // Enlève un disque de la tour sélectionnée
        if (disque) // Si un disque a été enlevé
        {
            // Demande à l'utilisateur de sélectionner une tour de destination
            tour_fin = better_scan("Entrer le numero de tour 1-nb_tours ou on ajoute un disque\n", 1, nb_tours);
            tour_fin--;
            if (!ajouterDisque(tours + tour_fin, disque)) // Si l'ajout du disque échoue (disque trop grand)
            {
                printf("Le disque est plus grand que le disque en dessous \n");
                ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
            }
        } else
        {
            printf("La tour est vide \n");
            ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
        }
        
        // Affiche l'état actuel des tours
        for (int i = 0; i < nb_tours; i++)
        {   
            printf("Tour %d :\n", i+1);
            afficheTour(tours+i);
        }
    }

    return 0;
}

``` 

<div id="4"></div>

## Exercice 4
[Télécharger l'exercice exo4.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo4.c){:target="_blank"} 

![exercice 4](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo4.jpg){: .w-75 .shadow .rounded-10 }



+  On définit la structure chainon
 

```c 
#include <stdio.h>
#include <stdlib.h>
typedef struct chainon_struct {
    int value; 
    struct chainon_struct* next; // Pointeur vers le prochain élément
} Chainon;

``` 


+  On nous donne la fonction taille qui retourne la taille de la liste chaînée comme deja écrite 
 

```c 
int taille(Chainon* p);
``` 


+  On crée la fonction qui coupe une liste chaînée en deux parties égales
 

```c 
int coupeEn2(Chainon* pliste, Chainon** liste1, Chainon** liste2) {
    // Vérification si les pointeurs pour les sous-listes sont valides
    if (liste1 == NULL || liste2 == NULL) {
        exit(EXIT_FAILURE); // Quitte le programme si l'un des pointeurs est NULL
    }
    
    // Récupération de la taille de la liste
    int taille_v = taille(pliste);
    
    // Si la taille de la liste est impair, la division en deux échoue
    if (taille_v % 2) {
        return 0; // Retourne 0 pour indiquer l'échec
    }
    
    // Si la liste d'origine est vide
    if (pliste == NULL) {
        *liste2 = NULL; // Initialise la deuxième liste à NULL
    } else {
        int pos = taille_v / 2; // Calcule la position pour couper la liste
        Chainon* actual = pliste; // Pointeur pour parcourir la liste
        int i = 0; // Compteur pour la position
        
        // On parcourt la liste jusqu'à la position désirée
        for (int i = 0; i < pos - 1; i++) {
            actual = actual->next; // Avance dans la liste
        }
        
        // On effectue la coupe de la liste
        Chainon* tmp = actual->next; // Stocke le début de la deuxième sous-liste
        actual->next = NULL; // Coupe la liste à la position trouvée
        *liste2 = tmp; // Assigne la deuxième liste à partir de l'élément suivant
        
    }
    
    *liste1 = pliste; // Assigne la première sous-liste à la liste d'origine
    return 1; // Retourne 1 pour indiquer le succès
}

``` 

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 
