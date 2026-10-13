---
title: TD02 Piles Files Correction
author: [AhmedA] 
date: 2024-09-27 01:00:00 +0100
categories: [PREING2 S1,Informatique3]
tags: [PREING2 S1,Informatique3,Ahmed A.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---


Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 

<div id="1"></div>

## Exercice 1

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo1.jpg){: .w-75 .shadow .rounded-10 }

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo2.c){:target="_blank"} 

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo2.jpg){: .w-75 .shadow .rounded-10 }

+ Il existe milles et une façon de declarer une pile dynamique, j'utilise une liste chaînée.
 

```c 

#include <stdio.h>
#include <stdlib.h>

typedef struct chainon_struct
{
    int value;
    struct chainon_struct* next;
}Chainon;

typedef struct pile_struct
{
    Chainon* tete; // Pointeur vers le sommet de la pile
    // On peut aussi ajouter int len; pour traquer le nombre d'element dans la pile
}Pile;


``` 


+  réutilise les fonctions du [TD1](https://cy.deltahmed.fr/posts/TD1-Listes-Chainee_Informatique3p2s1/) d'informatique
 

```c 
Chainon* creationChainon(int a){...}
Chainon* insertDebut(Chainon* pliste, int a){...}
Chainon* insertFin(Chainon* pliste, int a){...}
void afficheListe(Chainon* pliste){...}
``` 



+  On crée une fonction pour crée une pile
 

```c 
Pile* creationPile(){
    Pile* new = malloc(sizeof(Pile)); // Alloue de la mémoire pour une nouvelle pile
    if (new == NULL) {
        exit(EXIT_FAILURE); // Sort du programme en cas d'échec de l'allocation mémoire
    }
    new->tete = NULL; // Initialise la pile comme vide
    return new; // Retourne la nouvelle pile
}
``` 


+  On crée la fonction qui permet d'empiler une valeur sur la pile
 

```c 
Pile* empiler(int nb, Pile* ppile){
    if (ppile == NULL)
    {
        exit(EXIT_FAILURE);
    }
    ppile->tete = insertDebut(ppile->tete, nb); // Insère l'élément au sommet de la pile
    return ppile; // Retourne la pile mise à jour
}
``` 


+  On crée la fonction qui permet d'afficher la pile
 

```c 
void affichePile(Pile* ppile){
    afficheListe(ppile->tete); // Affiche les éléments de la pile en utilisant afficheListe
}
void affichePile_REC(Chainon* actual){ //version recursive
    if (actual != NULL)
    {
        printf("%d\n", actual->value);
        affichePile_REC(actual->next);
    }
    
}
``` 


+  On crée la fonction qui permet de dépiler une valeur sur la pile
 

```c 
Pile* depiler(Pile* ppile, int* pnmb){
    if (ppile == NULL)
    {
        exit(EXIT_FAILURE);
    }
    if (ppile->tete == NULL) {
        return ppile; // Si la pile est vide, il n'y a rien à dépiler
    }
    Chainon* tmp = ppile->tete->next; // Sauvegarde le deuxième élément
    *pnmb = ppile->tete->value; // Stocke la valeur de l'élément dépilé
    free(ppile->tete); // Libère la mémoire de l'élément dépilé
    ppile->tete = tmp; // Met à jour le sommet de la pile
    return ppile; // Retourne la pile mise à jour
}
``` 


+  On crée tout le programme en version statique
 

```c 
typedef struct pile2_struct
{
    int pile[50]; // Tableau pour stocker les éléments
    int tete; // Indice du sommet de la pile
}PileStat;

PileStat creationPileStat(){
    PileStat new;
    new.tete = -1; // Initialise la pile comme vide (indice du sommet à -1)
    return new; // Retourne la nouvelle pile statique

}

int depilerPileStat(PileStat* ppile){
    if (ppile == NULL || ppile->tete == -1) {
        exit(EXIT_FAILURE); // Sort si la pile est vide ou non initialisée
    }
    ppile->tete--; // Décrémente l'indice du sommet
    return ppile->pile[ppile->tete + 1]; // Retourne l'élément dépilé
}

void empilerPileStat(int nb, PileStat* ppile){
    if (ppile == NULL) {
        exit(EXIT_FAILURE); // Sort en cas d'erreur
    }
    ppile->tete += 1; // Incrémente l'indice du sommet
    ppile->pile[ppile->tete] = nb; // Stocke l'élément au sommet de la pile
}

void affichePileStat(PileStat ppile){
    if (ppile.tete == -1)
    {
        printf("[]");
    }
    printf("[");
    for (int i = 0; i < ppile.tete+1; i++)
    {
        printf("%d,", ppile.pile[i]);
    }
    printf("]");
    
}
``` 




+  On écrit dans le main la question 3, 6 
 

```c
int main() {
    Pile* p1 = creationPile();
    for (int i = 1; i < 21; i++)
    {
        empiler(i, p1);
    }
    affichePile(p1);

    Pile* pPaire = creationPile();
    Pile* pImpaire = creationPile();
    int nb;
    while (p1->tete != NULL)
    {   
        p1 = depiler(p1, &nb);
        if (nb%2 == 0)
        {   
            
            empiler(nb, pPaire);
        } else {
            empiler(nb, pImpaire);
        }
    }

    affichePile(pPaire);
    affichePile(pImpaire);
    
    // version statique

    PileStat p1_stat = creationPileStat();
    for (int i = 1; i < 21; i++)
    {
        empilerPileStat(i, &p1_stat);
    }
    affichePileStat(p1_stat);

    PileStat pPaire_stat = creationPileStat();
    PileStat pImpaire_stat = creationPileStat();
    while (p1_stat.tete > -1)
    {
        if (p1_stat.pile[p1_stat.tete]%2 == 0)
        {
            empilerPileStat(p1_stat.pile[p1_stat.tete], &pPaire_stat);
        } else {
            empilerPileStat(p1_stat.pile[p1_stat.tete], &pImpaire_stat);
        }
        depilerPileStat(&p1_stat);
    }
    

    affichePileStat(pPaire_stat);
    affichePileStat(pImpaire_stat);

    
    return 0; // Fin du programme
}
``` 

<div id="3"></div>

## Exercice 3
[Télécharger l'exercice exo3.c](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo3.c){:target="_blank"} 

![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo3.jpg)![exercice 3](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo3_2.jpg){: .w-75 .shadow .rounded-10 }

+ Il existe milles et une façon de declarer une file dynamique, j'utilise une liste chaînée.
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct chainon_struct
{
    int value;
    struct chainon_struct* next;
}Chainon;

typedef struct file_struct
{
    Chainon* tete; // Pointeur vers le sommet de la file
    Chainon* fin; // Pointeur vers la fin de la file
    // On peut aussi ajouter int len; pour traquer le nombre d'element dans la pile
}File;

File creationFile() { // Fonction pour créer une nouvelle file vide
    File nouvelleFile;
    nouvelleFile.tete = NULL; // Initialise la tête à NULL
    nouvelleFile.fin = NULL;  // Initialise la fin à NULL
    return nouvelleFile;      // Retourne la file vide
}
```

+  On réutilise les fonctions du [TD1](https://cy.deltahmed.fr/posts/TD1-Listes-Chainee_Informatique3p2s1/) d'informatique
 

```c 
Chainon* creationChainon(int a){...}

void afficheListe(Chainon* pliste){...}
``` 


+  On crée la fonction qui permet de créer un client (représenté par un nombre d'articles)
 

```c 
int randint(int a, int b){ // fonction pour générer un nombre aléatoire entre a et b
    return a + rand()%(b-a+1);
}

int creeClient(){
    return randint(1,50); // Un client a entre 1 et 50 articles
}
``` 


+  On crée la fonction pour enfiler un entier sur la file
 

```c 
void enfiler(File* pfile, int nb) {
    if (pfile == NULL) {
        exit(EXIT_FAILURE); // Vérification si la file existe
    }
    if (pfile->fin == NULL) { // Si la file est vide
        pfile->fin = creationChainon(nb); // Crée un nouveau chaînon
        pfile->tete = pfile->fin; // La tête et la fin pointent sur le même élément
    } else {
        pfile->fin->next = creationChainon(nb); // Ajoute un chaînon à la fin
        pfile->fin = pfile->fin->next; // Met à jour la fin de la file
    }
}
``` 


+  On crée la fonction pour defiler un entier sur la file
 

```c 
int defiler(File* pfile, int* nb) {
    if (pfile == NULL) {
        exit(EXIT_FAILURE); // Vérifie si la file existe
    }
    if (pfile->tete == NULL) { // Si la file est vide
        return -1; // Retourne -1 si aucun élément à défiler
    }

    Chainon* tmp = pfile->tete->next; // Sauvegarde l'élément suivant
    *nb = pfile->tete->value; // Stocke la valeur de l'élément à défiler
    free(pfile->tete); // Libère l'élément défiler
    pfile->tete = tmp; // Met à jour la tête de la file
    if (pfile->tete == NULL)
    {
        pfile->fin = NULL;
    }
    return 0; // Succès
}
``` 


+  La fonction affichage de la file appelle juste la fonction afficheListe crée plus tôt
 

```c 
void afficheFile(File* pfile){
    if (pfile == NULL)
    {
        exit(EXIT_FAILURE); // Vérifie si la file existe
    }
    if (pfile->tete == NULL || pfile->fin == NULL) // Si la file est vide
    {
        printf("[]\n"); // On gère les files vides
    } else {
        afficheListe(pfile->tete);
    }
}
``` 



+  On crée le programme de simulation de clients
 

```c 
int main() {
    srand(time(NULL)); // Initialisation de la génération de nombres aléatoires
    File pfile = creationFile(); // Création de la file

    // Ajoute 3 clients initiaux dans la file
    for (int i = 0; i < 3; i++) {
        enfiler(&pfile, creeClient()); // Ajoute un client avec un nombre d'articles aléatoire
    }

    int client_paye; // Variable pour stocker le client qui paye
    int ret_var;     // Variable pour stocker le retour de defiler
    afficheFile(&pfile); // Affiche l'état initial de la file
    
    // Boucle jusqu'à ce que la file soit vide
    while (pfile.tete != NULL && pfile.fin != NULL) {
        ret_var = defiler(&pfile, &client_paye); // Retire un client de la file
        if (ret_var) {
            return 1; // Sort en cas d'erreur
        }

        // Simule l'arrivée aléatoire de nouveaux clients
        if (randint(1, 3) == 1) { // Un client sur trois fait arriver de nouveaux clients
            for (int i = 0; i < randint(1, 3); i++) { // Ajoute entre 1 et 3 nouveaux clients
                enfiler(&pfile, creeClient());
            }
        }

        // Affiche le client qui passe à la caisse
        printf("%d passe a la caisse\n", client_paye);
        afficheFile(&pfile); // Affiche l'état de la file après chaque passage
    }

    return 0; // Fin du programme
}

``` 



+ Question 6 :
    +  il suffit de sommer les première clients jusqu'au seuil et de ne pas prendre en compte les derniers clients
 
    +  La structure de donnée la plus adapté est une liste chaînée pas une file (conceptuel) 


<div id="4"></div>

## Exercice 4
[Télécharger l'exercice exo4.c](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo4.c){:target="_blank"} 

![exercice 4](https://data2.cy.deltahmed.fr/DATA/info/TD2-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo4.jpg){: .w-75 .shadow .rounded-10 }

+ On reprend le code de [l'exo2](#2) en adaptant aux characters
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct chainon_struct
{
    char value; // On change le type par un char
    struct chainon_struct* next;
}Chainon;

typedef struct pile_struct
{
    Chainon* tete;
}Pile;

Chainon* creationChainon(char a){...}
Chainon* insertDebut(Chainon* pliste, char a){...}
Chainon* insertFin(Chainon* pliste, char a){...}
void afficheListe(Chainon* pliste){
    if (pliste == NULL)
    {
        printf("[]\n");
    }
    Chainon* actual = pliste;
    printf("[");
    while (actual->next != NULL)
    {  
        printf("%c, ",actual->value); // %d devient %c
        actual = actual->next;
    }
    printf("%c]\n",actual->value);
}
Pile* creationPile(){...}
Pile* empiler(char nb, Pile* ppile){...}
void affichePile(Pile* ppile){...}
Pile* depiler(Pile* ppile, char* pnmb){...}

``` 


+  On creer la fonction qui permet de verifier tout type de parenthésage (3 et 4)
 

```c 
char inverse_parenthesage(char a){ // Fonction pour retourner le caractère fermant correspondant à un caractère ouvrant
    switch (a) {
        case '(': return ')';
        case '[': return ']';
        case '{': return '}';
        default:  return 0; // Retourne 0 si aucun match
    }
}

int parenthesage(char * str){
    if (str == NULL) {
        exit(EXIT_FAILURE); // Quitte si la chaîne est NULL
    }
    
    Pile* ppile = creationPile(); // Crée une pile pour stocker les caractères ouvrants
    int len = strlen(str);        // Longueur de la chaîne
    char depile_var;              // Variable pour stocker les valeurs dépilées

    // Parcourt chaque caractère de la chaîne
    for (int i = 0; i < len; i++) {
        switch (str[i]) {
            // Si on rencontre une parenthèse, un crochet ou une accolade ouvrante
            case '(':
            case '[':
            case '{':
                empiler(str[i], ppile); // Empile le caractère ouvrant
                break;

            // Si on rencontre une parenthèse, un crochet ou une accolade fermante
            case ')':
            case ']':
            case '}':
                depiler(ppile, &depile_var); // Dépile un caractère ouvrant
                if (str[i] != inverse_parenthesage(depile_var)) {   
                    printf("%s faux \n", str); // Si le caractère fermant ne correspond pas, affiche "faux"
                    return 0; // Retourne 0 pour indiquer que la chaîne est mal parenthésée
                }
                break;
        
            // Ignore les autres caractères
            default:
                break;
        }
    }

    // Si la chaîne est bien parenthésée
    printf("%s vrai \n", str);
    return 1; // Retourne 1 pour indiquer que la chaîne est correctement parenthésée
}

int main() {
    // Test des chaînes avec différentes combinaisons de parenthèses, crochets et accolades
    char c1[] = "Je suis Luffy )le futur roi des pirates( !";
    parenthesage(c1);

    char c2[] = "a(b[c()e]f)g";
    parenthesage(c2);

    char c3[] = "a(b[c)d]e";
    parenthesage(c3);

    char c4[] = "dfg.dfgg.gfggg( cy.deltahmed.fr/egg/hehe.gif )sd.gwdf.gdd";
    parenthesage(c4);

    char c5[] = "x(1+2)([2+5]*3)";
    parenthesage(c5);

    return 0; // Fin du programme
}
```

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 
