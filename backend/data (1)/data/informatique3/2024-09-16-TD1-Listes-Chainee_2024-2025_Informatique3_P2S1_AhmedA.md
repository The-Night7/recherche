---
title: TD01 Listes Chainees Correction
author: [AhmedA] 
date: 2024-09-16 01:00:00 +0100
categories: [PREING2 S1,Informatique3]
tags: [PREING2 S1,Informatique3,Ahmed A.,2024/2025]
math: true
mermaid: true

division_title : 2024/2025
---

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) 

<div id="1"></div>

## Exercice 1
[Télécharger l'exercice exo1.c](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo1.c){:target="_blank"} 

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo1.jpg){: .w-75 .shadow .rounded-10 }

+  On inclue les bibliothèques utiles
 

```c 
#include <stdio.h>
#include <stdlib.h>

``` 


+  On définie la structure Chainon pour représenter un élément d'une liste chaînée
 

```c 
typedef struct chainon_struct
{
    int value; // Valeur stockée dans le chainon
    struct chainon_struct* next; // Pointeur vers le prochain chainon
} Chainon;

``` 


+  On crée la fonction qui crée un nouveau chainon avec la valeur 'a' et renvoie un pointeur vers celui-ci
 

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

``` 


+  On crée la fonction pour insérer un chainon au début de la liste
 

```c 
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

``` 


+  On crée la fonction pour insérer un chainon à la fin de la liste
 

```c 
Chainon* insertFin(Chainon* pliste, int a){
    if (pliste == NULL) // Si la liste est vide
    {
        pliste = creationChainon(a); // Créer un nouveau chainon
    } else {
        Chainon* actual = pliste; // Commencer au début de la liste
        while (actual->next != NULL) // Parcourir la liste jusqu'à la fin
        {
            actual = actual->next;
        }
        actual->next = creationChainon(a); // Ajouter le nouveau chainon à la fin
    }
    return pliste; // Retourner la tête de la liste
}

``` 


+  On crée la fonction pour afficher la liste chainée
 

```c 
void afficheListe(Chainon* pliste){
    if (pliste == NULL) // Si la liste est vide
    {
        printf("liste vide\n"); // Afficher un message
    }
    Chainon* actual = pliste; // Commencer au début de la liste
    while (actual->next != NULL) // Parcourir la liste jusqu'à l'avant-dernier élément
    {  
        printf("%d -> ", actual->value); // Afficher la valeur de chaque chainon
        actual = actual->next;
    }
    printf("%d", actual->value); // Afficher la dernière valeur sans flèche
    printf("\n");
}

``` 


+  On crée la fonction pour lire un entier sécurisé depuis l'utilisateur
 

```c 
int better_scan(const char * message){
    int ret_var = 0; // Variable pour capturer le résultat de scanf
    int value = 1; // Initialisation de la variable à retourner
    while (ret_var != 1) // Boucle jusqu'à obtenir une saisie valide
    {   
        if (message != NULL)
        {
            printf("%s", message); // Afficher le message si non nul
        }
        ret_var = scanf("%d", &value); // Lecture de la valeur
        while(getchar()!='\n'){} // Vider le buffer de saisie (sécurisation)
    }
    return value; // Retourner la valeur saisie
}

``` 


+  On teste le tout dans la fonction principale
 

```c 
int main(){
    
    Chainon* pliste = NULL; // Initialiser la liste vide
    int nb = 0; // Variable de contrôle de la boucle
    int i = 1; // Compteur pour les valeurs insérées
    while (nb == 0) // Tant que l'utilisateur souhaite ajouter des éléments
    {   
        pliste = insertFin(pliste, i); // Insérer la valeur i à la fin de la liste
        afficheListe(pliste); // Afficher la liste actuelle
        i = i * 2; // Doubler la valeur de i pour la prochaine insertion
        nb = better_scan("Nombre suivant ? \n0 - oui \nautre - non\n"); // Demander à l'utilisateur s'il veut continuer
    }
    
    // On libére la mémoire allouée pour la liste
    Chainon* actual = pliste;
    while (pliste != NULL)
    {
        actual = pliste->next; // Sauvegarder le prochain chainon
        free(pliste); // Libérer la mémoire du chainon actuel
        pliste = actual; // Passer au chainon suivant
    }
    
    return 0; // Fin du programme
}

``` 

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo2.c){:target="_blank"} 

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo2.jpg){: .w-75 .shadow .rounded-10 }

+ On utilise les fonctions et structures précédentes 
 

```c 

#include <stdio.h>
#include <stdlib.h>
...

``` 


+  On crée la fonction pour insérer un élément dans une liste triée
 

```c 
Chainon* InsertTrie(Chainon* pliste, int a) {
    if ( pliste == NULL || a <= pliste->value) { // Si l'élément est plus petit ou égal à la première valeur
        return insertDebut(pliste, a); // Insère au début de la liste
    }

    Chainon* borne1 = pliste; // Pointeur sur l'élément actuel
    Chainon* borne2 = pliste->next; // Pointeur sur l'élément suivant

    while (borne2 != NULL) { // Parcourt la liste jusqu'à trouver la bonne position pour insérer 'a'
        if (borne1->value < a && a <= borne2->value) { // Si 'a' est compris entre les deux valeurs
            Chainon* a_chainon = creationChainon(a); // Crée un nouveau chainon avec la valeur 'a'
            a_chainon->next = borne2; // Le nouveau chainon pointe vers 'borne2'
            borne1->next = a_chainon; // 'borne1' pointe maintenant vers le nouveau chainon
            return pliste; // Retourne la tête de la liste
        }
        borne1 = borne2; // Passe la borne1 à l'élément suivant a chaque tour de bouvle
        borne2 = borne2->next; // Passe la borne2 à l'élément suivant a chaque tour de boucle
    }

    return insertFin(pliste, a); // Si 'a' est plus grand que toutes les valeurs, insère à la fin
}

``` 


+  On teste le tout dans la fonction principale
 

```c 
int main() {
    Chainon* pliste = NULL; // Initialise la liste à vide
    for (int i = 0; i < 20; i += 5) { // Insère des multiples de 5 dans la liste
        pliste = insertFin(pliste, i); // Insère chaque élément à la fin
    }
    afficheListe(pliste); // Affiche la liste après insertion

    pliste = InsertTrie(pliste, 2); // Insère 2 dans la liste
    pliste = InsertTrie(pliste, 12); // Insère 12 dans la liste
    pliste = InsertTrie(pliste, 22); // Insère 22 dans la liste

    afficheListe(pliste); // Affiche la liste après les insertions triées

    Chainon* actual = pliste;
    while (pliste != NULL)
    {
        actual = pliste->next; // Sauvegarder le prochain chainon
        free(pliste); // Libérer la mémoire du chainon actuel
        pliste = actual; // Passer au chainon suivant
    }
    
    return 0; // Fin du programme
}

``` 

<div id="3"></div>

## Exercice 3
[Télécharger l'exercice exo3.c](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo3.c){:target="_blank"} 

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo3.jpg){: .w-75 .shadow .rounded-10 }

+ On utilise les fonctions et structures précédentes 
 

```c 
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
...

``` 


+  On crée la fonction pour supprimer la première occurrence d'un élément 'a' dans la liste
 

```c 
Chainon* SupprimerPremier(Chainon* pliste, int a){
    if (pliste == NULL){
        return pliste; // Liste vide
    }

    if (pliste->value == a){// Cas où le premier élément de la liste doit être supprimé
        Chainon* suppr = pliste; // Stocke l'élément à supprimer
        pliste = pliste->next; // Le suivant devient le premier élément
        free(suppr); // Libère la mémoire
        return pliste; // Retourne la nouvelle tête de liste
    }

    Chainon* actual = pliste;
    Chainon* suppr = NULL;
    
    while (actual->next != NULL){
        if (actual->next->value == a){ // Trouve l'élément à supprimer
            suppr = actual->next; // Stocke l'élément à supprimer
            actual->next = actual->next->next; // Saute cet élément dans la liste
            free(suppr); // Libère la mémoire
            return pliste; // Retourne la tête de la liste
        }
        actual = actual->next; // Continue à parcourir la liste
    }
    return pliste; // Retourne la liste si l'élément n'a pas été trouvé
}

``` 


+  On crée la fonction pour supprimer toutes les occurrences d'un élément 'a' dans la liste
 

```c 
Chainon* SupprimerTout(Chainon* pliste, int a){
    if (pliste == NULL){
        return pliste; // Liste vide
    }

    
    while (pliste != NULL && pliste->value == a){// Cas où le premier élément doit être supprimé (si c'est 'a')
        Chainon* suppr = pliste;
        pliste = pliste->next; // Le suivant devient le premier
        free(suppr); // Libère la mémoire du chainon supprimé
    }

    Chainon* actual = pliste;
    Chainon* suppr = NULL;
    
    
    while (actual != NULL && actual->next != NULL){// Parcourt la liste à partir du deuxième élément
        if (actual->next->value == a){ // Trouve l'élément à supprimer
            suppr = actual->next;
            actual->next = actual->next->next; // Saute l'élément dans la chaîne
            free(suppr); // Libère la mémoire
        } else {
            actual = actual->next; // Passe au chainon suivant
        }
    }
    return pliste; // Retourne la tête de la liste modifiée
}

``` 


+  On teste le tout dans la fonction principale
 

```c 
int main(){
    srand(time(NULL)); 
    Chainon* pliste = NULL;
    
    for (int i = 0; i < 10; i++){
        pliste = insertFin(pliste, rand() % 6);
    }
    
   
    afficheListe(pliste);
    
   
    pliste = SupprimerPremier(pliste, 2);
    afficheListe(pliste); 

    pliste = SupprimerTout(pliste, 5);
    afficheListe(pliste); 

    Chainon* actual = pliste;
    while (pliste != NULL){
        actual = pliste->next;
        free(pliste);
        pliste = actual;
    }
    
    return 0;
}

``` 

<div id="4"></div>

## Exercice 4
[Télécharger l'exercice exo4.c](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo4.c){:target="_blank"} 

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo4.jpg){: .w-75 .shadow .rounded-10 }

+ On utilise les fonctions et structures précédentes 
 

```c 
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

...

``` 


+  On crée la fonction pour inverser la liste en créant une nouvelle liste
 

```c 
Chainon* Inverse(Chainon* pliste){
    Chainon* newliste = NULL; // Nouvelle liste initialement vide

    Chainon* actual = pliste; // Commence à parcourir la liste originale
    while (actual != NULL){
        newliste = insertDebut(newliste, actual->value); // Insère au début de la nouvelle liste
        actual = actual->next; // Passe au chainon suivant
    }
    return newliste; // Retourne la nouvelle liste inversée
}

``` 


+  On crée la fonction pour inverser la liste en modifiant les pointeurs directement sans passer par une liste intermédiaire 
 

```c 
Chainon* Inverse2(Chainon* pliste){
    if (pliste == NULL){
        return NULL; // Retourne NULL si la liste est vide
    }

    Chainon* previous = pliste->next; // Pointeur sur le deuxième élément
    Chainon* actual = pliste; // Pointeur sur le premier élément
    Chainon* tmp = NULL; // Variable temporaire pour la manipulation des pointeurs
    actual->next = NULL; // Le premier élément devient le dernier, donc son pointeur 'next' est NULL

    while (previous != NULL){
        tmp = previous->next; // Sauvegarde le prochain élément
        previous->next = actual; // Inverse le pointeur du chainon actuel
        actual = previous; // Avance le chainon actuel
        previous = tmp; // Passe au chainon suivant
    }
    return actual; // Retourne la nouvelle tête de la liste inversée
}

``` 


+  On test le tout dans la fonction principale sans oublier de free les différentes listes a la fin
 

```c 
int main(){
    srand(time(NULL));
    Chainon* pliste = NULL;
    

    for (int i = 0; i < 10; i++){
        pliste = insertFin(pliste, rand() % 6);
    }
    
    afficheListe(pliste); 

    Chainon* pliste2 = Inverse(pliste); 
    afficheListe(pliste2); 
    
    pliste2 = Inverse2(pliste2); 
    afficheListe(pliste2); 


    Chainon* actual = pliste;
    while (pliste != NULL){
        actual = pliste->next;
        free(pliste);
        pliste = actual;
    }
    actual = pliste2;
    while (pliste2 != NULL){
        actual = pliste2->next;
        free(pliste2);
        pliste2 = actual;
    }
    
    return 0;
}

``` 

<div id="5"></div>

## Exercice 5
[Télécharger l'exercice exo5.c](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo5.c){:target="_blank"} 

![exercice 5](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo5.jpg)

![exercice 5](https://data.cy.deltahmed.fr/DATA/TD1-Listes-Chainee_Informatique3p2s1/exo5_2.jpg){: .w-75 .shadow .rounded-10 }

+ On definie les différentes structure/definitions/fonctions utiles pour le programme 
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define Nb_notes 10

typedef struct etudiant_struct {
    char nom[50];
    char prenom[50];
    int groupe;
    int notes[Nb_notes];
} Etudiant;

typedef struct chainon_struct {
    Etudiant etudiant;
    struct chainon_struct* next;
} Chainon;

int better_scan(const char * message){
    int ret_var = 0;
    int value = 1;
    while (ret_var != 1)
    {   
        if (message != NULL)
        {
            printf("%s", message);
        }
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}

``` 


+  On crée la fonction pour créer un nouvel étudiant
 

```c 
Etudiant creerEtudiant() {
    Etudiant etudiant;
    printf("Nom: ");
    if (fgets(etudiant.nom, 50, stdin) == NULL){
        exit(EXIT_FAILURE); 
    }
    etudiant.nom[strlen(etudiant.nom)-1] = '\0';
    printf("Prenom: ");
    if (fgets(etudiant.prenom, 50, stdin) == NULL){
        exit(EXIT_FAILURE); 
    }
    etudiant.prenom[strlen(etudiant.prenom)-1] = '\0';
    printf("Groupe: ");
    etudiant.groupe = better_scan("Saisir numero grp :\n");
    
    for (int i = 0; i < Nb_notes; i++) {
        etudiant.notes[i] = rand() % 21; // Notes entre 0 et 20
    }
    return etudiant;
}

``` 


+  On crée la fonction pour ajouter un étudiant à la fin de la liste
 

```c 
void saisirEtudiant(Chainon** lst) { //on utilise un double pointeur pour ne pas avoir besoin de retourner la liste
    Chainon* nouveau = (Chainon*)malloc(sizeof(Chainon));
    if (nouveau == NULL) {
        printf("Erreur d'allocation mémoire.\n");
        exit(EXIT_FAILURE);
    }
    nouveau->etudiant = creerEtudiant();
    nouveau->next = NULL;

    if (*lst == NULL) {
        *lst = nouveau;
    } else {
        Chainon* tmp = *lst;
        while (tmp->next != NULL) {
            tmp = tmp->next;
        }
        tmp->next = nouveau;
    }
}

``` 


+  On crée la fonction pour afficher les étudiants par groupe
 

```c 
void listeParGroupe(Chainon* lst, int groupe) {
    Chainon* tmp = lst;
    while (tmp != NULL) {
        if (tmp->etudiant.groupe == groupe) {
            printf("%s %s\n", tmp->etudiant.nom, tmp->etudiant.prenom);
        }
        tmp = tmp->next;
    }
}

``` 


+  On crée la fonction pour calculer la moyenne d'un tableau de notes
 

```c 
float moyTab(int* tab) {
    float somme = 0;
    for (int i = 0; i < Nb_notes; i++) {
        somme += tab[i];
    }
    return somme / Nb_notes;
}

``` 


+  On crée la fonction pour trouver un étudiant par nom et prénom
 

```c 
Chainon* trouveEtudiant(char* nom, char* prenom, Chainon* lst) {
    Chainon* tmp = lst;
    while (tmp != NULL) {
        if (strcmp(tmp->etudiant.nom, nom) == 0 && strcmp(tmp->etudiant.prenom, prenom) == 0) {
            return tmp;
        }
        tmp = tmp->next;
    }
    return NULL;
}

``` 


+  On crée la fonction pour calculer la moyenne d'un étudiant spécifique
 

```c 
void moyenneEtudiant(Chainon* lst, char* nom, char* prenom) {
    Chainon* etudiant = trouveEtudiant(nom, prenom, lst);
    if (etudiant) {
        printf("Moyenne de %s %s: %f\n", nom, prenom, moyTab(etudiant->etudiant.notes));
    } else {
        printf("Erreur: aucun étudiant avec le nom %s %s trouvé.\n", nom, prenom);
    }
}

``` 


+  On crée la fonction pour calculer la moyenne de toute la promotion
 

```c 
float moyennePromotion(Chainon* lst) {
    float somme = 0;
    int count = 0;
    Chainon* tmp = lst;
    while (tmp != NULL) {
        somme += moyTab(tmp->etudiant.notes);
        count++;
        tmp = tmp->next;
    }

    return count ? somme / count : 0;
}

``` 


+  On crée la fonction pour afficher l'étudiant avec la plus mauvaise moyenne
 

```c 
void etudiantPireMoyenne(Chainon* lst) {
    if (lst == NULL) {
        printf("Pas d'étudiants dans la liste.\n");
        return;
    }

    Chainon* tmp = lst;
    Chainon* pire = lst;
    float pireMoyenne = moyTab(tmp->etudiant.notes);

    while (tmp != NULL) { //calcul classique de minimum
        float moyenneActuelle = moyTab(tmp->etudiant.notes);
        if (moyenneActuelle < pireMoyenne) {
            pire = tmp;
            pireMoyenne = moyenneActuelle;
        }
        tmp = tmp->next;
    }

    printf("L'étudiant avec la plus mauvaise moyenne est %s %s avec %f de moyenne.\n", pire->etudiant.nom, pire->etudiant.prenom, pireMoyenne);
}

``` 


+ On crée le main pour choisir ce que l'on veut faire
 

```c 
int main() {
    srand(time(NULL));
    Chainon* etudiant_plist = NULL;
    int choix, groupe;
    char nom[50], prenom[50];

    do {
        printf("\nMenu:\n");
        printf("1. Saisir un nouvel étudiant\n");
        printf("2. Afficher les étudiants par groupe\n");
        printf("3. Calculer la moyenne d'un étudiant\n");
        printf("4. Calculer la moyenne de la promotion\n");
        printf("5. Afficher l'étudiant avec la plus mauvaise moyenne\n");
        printf("6. Quitter\n");
        printf("Votre choix: ");
        choix = better_scan("Votre choix: ");

        switch (choix) {
            case 1:
                saisirEtudiant(&etudiant_plist);
                break;
            case 2:
                groupe = better_scan("Entrez le numéro du groupe: ");
                listeParGroupe(etudiant_plist, groupe);
                break;
            case 3:
                printf("Entrez le nom de l'étudiant: ");
                if (fgets(nom, 50, stdin) == NULL){
                    exit(EXIT_FAILURE); 
                }
                nom[strlen(nom)-1] = '\0';
                printf("Entrez le prénom de l'étudiant: ");
                if (fgets(prenom, 50, stdin) == NULL){
                    exit(EXIT_FAILURE); 
                }
                prenom[strlen(prenom)-1] = '\0';
                moyenneEtudiant(etudiant_plist, nom, prenom);
                break;
            case 4:
                printf("Moyenne de la promotion: %f\n", moyennePromotion(etudiant_plist));
                break;
            case 5:
                etudiantPireMoyenne(etudiant_plist);
                break;
            case 6:
                printf("Salem !\n");
                break;
            default:
                printf("Choix invalide!\n");
                break;
        }
    } while (choix != 6);

    Chainon* actual = etudiant_plist; //On oublie pas de free la memoire
    while (etudiant_plist != NULL){
        actual = etudiant_plist->next;
        free(etudiant_plist);
        etudiant_plist = actual;
    }
    return 0;
}

``` 

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) 
