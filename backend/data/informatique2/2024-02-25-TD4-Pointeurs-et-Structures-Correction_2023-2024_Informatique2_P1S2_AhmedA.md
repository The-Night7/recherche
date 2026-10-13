---
title: TD4 Pointeurs et Structures Correction
author: [AhmedA]
date: 2024-02-25 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Ahmed A.,2023/2024]
math: true
mermaid: true
division_title : 2023/2024
---

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 

<div id="1"></div>

## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD4-Pointeurs-et-Structures_Informatique2p1s2/exo1.jpg){: .w-75 .shadow .rounded-10 }

+  on inclue les différentes bibliothèques utiles puis on créer la structure Complex qui stock un nombre complex de la forme $a + ib$
 

```c 
#include <stdio.h>
#include <math.h>

typedef struct
{
    float a;
    float b;
} Complex;

``` 


+  On reprend la fonction de [l'exercice 5 du TD2](https://cy.deltahmed.fr/posts/TD2-Pointeur_Informatique2p1s2/#exercice-5) et on modifie pour coller a l'exercice
 

```c 
int resoudre(float a, float b, float c, Complex *res1, Complex *res2) {
    float discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
        res1->a = (-b + sqrt(discriminant)) / (2 * a);
        res2->a = (-b - sqrt(discriminant)) / (2 * a);
        res1->b = 0;
        res2->b = 0;
        return 2; // Deux solutions distinctes
    } else if (discriminant == 0) {
        res1->a = -b / (2 * a);
        res2->a = -b / (2 * a);
        res1->b = 0;
        res2->b = 0;
        return 2;
    } else {
        res1->a = -b / (2 * a);
        res1->b = sqrt(-discriminant) / (2 * a);
        res2->a = -b / (2 * a);
        res2->b = -sqrt(-discriminant) / (2 * a);
        return 2;
    }
}

``` 

<div id="2"></div>

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD4-Pointeurs-et-Structures_Informatique2p1s2/exo2.jpg){: .w-75 .shadow .rounded-10 }



+  On créer la structure qui représente un nombre rationnel sous la forme $$\frac{\text{den}}{\text{num}}$$
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{   
    int den; // Dénominateur
    int num; // Numérateur
    
} NmbRationnel;

``` 


+  On créer la procédure pour afficher un nombre rationnel
 

```c 
void afficheNum(NmbRationnel * nb){
    printf("%d/%d \n", nb->num, nb->den);
}

``` 


+  On créer la fonction pour additionner ou multiplier deux nombres rationnels comme demandé dans l'exercice
 

```c 
void addMult(NmbRationnel *num1, NmbRationnel *num2){
    // Calcul des produits
    int num_multi = num1->num * num2->num;
    int den_multi = num1->den * num2->den;
    int den_add, num_add;
    
    // Traitement des cas spéciaux et calcules des sommes
    if (num_multi == 0){
        num_add = 0;
        den_add = den_multi;
    }
    else if (num1->den == num2->den){
        num_add = num1->num + num2->num;
        den_add = num1->den;
    }
    else {
        num_add = num1->den * num2->num + num2->den * num1->num;
        den_add = den_multi;
    }
    
    // Mise à jour des valeurs des nombres rationnels
    num1->num = num_multi;
    num1->den = den_multi;
    num2->num = num_add;
    num2->den = den_add;
}

``` 


+  On créer une fonction facultative sécurisée pour le `scanf`
 

```c 
int better_scan(char * message){
    int ret_var = 0;
    int value = 1;
    
    while (ret_var != 1)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;  
}

``` 


> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }


+  Fonction pour créer un nombre rationnel
 

```c 
NmbRationnel* creerRationnel(){
    // Allocation dynamique de mémoire
    NmbRationnel* new = (NmbRationnel*)malloc(sizeof(NmbRationnel));
    new->num = better_scan("Saisir le numérateur : \n");
    new->den = better_scan("Saisir le dénominateur : \n");
    return new;
}

``` 


+  On teste le tout dans le `main`
 

```c 
int main(){
    // Création de deux nombres rationnels
    NmbRationnel* r1 = creerRationnel();
    afficheNum(r1);
    NmbRationnel* r2 = creerRationnel();
    afficheNum(r2);
    
    // Addition/multiplication des deux nombres rationnels
    addMult(r1,r2);
    
    // Affichage des résultats
    printf("Produit : ");
    afficheNum(r1);
    printf("Somme : ");
    afficheNum(r2);
}

``` 

<div id="3"></div>

## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD4-Pointeurs-et-Structures_Informatique2p1s2/exo3.jpg){: .w-75 .shadow .rounded-10 }
![exercice 3](https://data.cy.deltahmed.fr/DATA/TD4-Pointeurs-et-Structures_Informatique2p1s2/exo3_2.jpg){: .w-75 .shadow .rounded-10 }

+  On inclue les bibliothèques et on définie les constante utiles 
 

```c 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define NB_NOTES 6
#define MAX_LENGTH 50

``` 


+  On créer la structure représentant un étudiant
 

```c 
typedef struct {
    char nom[MAX_LENGTH];
    char prenom[MAX_LENGTH];
    int numero_groupe;
    float notes[NB_NOTES];
} Etudiant;

``` 


+  On créer une fonction facultative sécurisée pour le `scanf`
 

```c 
int better_scan(char * message){
    int ret_var = 0;
    int value = -1;
    
    while (ret_var != 1 || value < 0)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;  
}

``` 


> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }


+  On créer la procédure pour créer un étudiant avec des notes aléatoires
 

```c 
void creerEtudiant(Etudiant *etudiant) {

    printf("Nom de famille de l'etudiant : ");
    if (fgets(etudiant->nom, MAX_LENGTH, stdin) == NULL){
        exit(EXIT_FAILURE); 
    }
    etudiant->nom[strcspn(etudiant->nom, "\n")] = 0;

    printf("Prenom de l'etudiant : ");
    if (fgets(etudiant->prenom, MAX_LENGTH, stdin) == NULL){
        exit(EXIT_FAILURE); 
    }
    etudiant->prenom[strcspn(etudiant->prenom, "\n")] = 0;

    etudiant->numero_groupe = better_scan("Numero de groupe : ");
    
    // Remplissage aléatoire des notes
    for (int i = 0; i < NB_NOTES; i++) {
        etudiant->notes[i] = (float)(rand() % 20) + (float)rand()/RAND_MAX; // Note entre 0 et 20
    }
}

``` 


> `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fonction renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`, `strcspn` prend en argument une chaîne de char et une liste (chaîne de char) de rejet, Elle Renvoie la longueur de la plus grande sous-chaîne (en partant du début de la chaîne initiale) ne contenant aucun des caractères spécifiés dans la liste des caractères en rejet, ici elle permet de trouver l'index avant le `\n`.
{: .prompt-info }


> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-tip }


+  On créer la procédure pour afficher les informations d'un étudiant
 

```c 
void afficherEtudiant(Etudiant etudiant) {
    printf("Nom : %s\n", etudiant.nom);
    printf("Prenom : %s\n", etudiant.prenom);
    printf("Numero de groupe : %d\n", etudiant.numero_groupe);
    printf("Notes : ");
    for (int i = 0; i < NB_NOTES; i++) {
        printf("%.2f ", etudiant.notes[i]); // %.2f affiche deux chiffre après la virgule
    }
    printf("\n");
}

``` 


>  %.2f affiche deux chiffre après la virgule
{: .prompt-tip }


+  On créer la procédure pour afficher les informations de tous les étudiants d'un tableau
 

```c 
void afficherTabEtudiants(Etudiant *tab, int taille) {
    for (int i = 0; i < taille; i++) {
        printf("Etudiant %d :\n", i + 1);
        afficherEtudiant(tab[i]);
    }
}

``` 


+  On créer la fonction pour calculer la moyenne des étudiants d'un groupe donné
 

```c 
float moyGroupe(Etudiant *tab, int groupe, int taille) {
    float somme = 0;
    int count = 0;
    for (int i = 0; i < taille; i++) {
        if (tab[i].numero_groupe == groupe) {
            for (int j = 0; j < NB_NOTES; j++) {
                somme += tab[i].notes[j];
            }
            count++;
        }
    }
    if (count == 0) { // on evite la division par zéro
        return 0;
    } 
    return somme / (count * NB_NOTES);
}

``` 


+  Procédure pour vérifier et corriger les noms de famille des étudiants
 

```c 
void verifMaj(Etudiant *tab, int taille) {
    for (int i = 0; i < taille; i++) {
        if (tab[i].nom[0] >= 'a' && tab[i].nom[0] <= 'z') {
            tab[i].nom[0] -= 32; // Convertir en majuscule
        }
    }
}

``` 


+  Procédure pour trier les étudiants par la première lettre de leur nom avec l'algorithme du bubble sort
 

```c 
void tri_premiere_lettre(Etudiant *tab, int taille) {
    Etudiant temp;
    for (int i = 0; i < taille - 1; i++) {
        for (int j = 0; j < taille - i - 1; j++) {
            if (tab[j].nom[0] > tab[j + 1].nom[0]) {
                temp = tab[j];
                tab[j] = tab[j + 1];
                tab[j + 1] = temp;
            }
        }
    }
}

``` 


+  Procédure pour trier les étudiants par leur nom complet avec l'algorithme du bubble sort
 

```c 
void tri_nom(Etudiant *tab, int taille) {
    Etudiant temp;
    for (int i = 0; i < taille - 1; i++) {
        for (int j = 0; j < taille - i - 1; j++) {
            if (strcmp(tab[j].nom, tab[j + 1].nom) > 0) {
                temp = tab[j];
                tab[j] = tab[j + 1];
                tab[j + 1] = temp;
            }
        }
    }
}

``` 



+  Pour ceux qui n'ont pas fait NSI en terminale voici le pseudo code du bubble sort
 

```

tri_à_bulles(Tableau T)
   pour i allant de (taille de T)-1 à 1
       pour j allant de 0 à i-1
           si T[j+1] < T[j]
               (T[j+1], T[j]) ← (T[j], T[j+1])

``` 



>  cette fonction permet de comparer deux chaînes de caractères et de savoir si la première est inférieure, égale ou supérieure à la seconde. Cette comparaison sera réalisée en utilisant l'ordre lexicographique et donc, en tenant compte des valeurs numérique des codes ASCII (ou Unicode, selon l'encodage utilisé) des différents caractères comparés.
{: .prompt-tip }


+  On peut utiliser le tout dans le `main`
 

```c 
int main() {
    srand(time(NULL)); // Initialisation du générateur de nombres aléatoires
    
    int effectif = better_scan("Saisir l'effectif de la promotion : ");
    
    Etudiant *promo = (Etudiant *)malloc(effectif * sizeof(Etudiant));
    
    // Création des étudiants et remplissage des informations
    for (int i = 0; i < effectif; i++) {
        printf("\nEtudiant %d :\n", i + 1);
        creerEtudiant(&promo[i]);
    }
    
    // Affichage des informations de tous les étudiants
    printf("\nInformations de tous les etudiants :\n");
    afficherTabEtudiants(promo, effectif);
    
    // Calcul et affichage de la moyenne du groupe 1
    printf("\nMoyenne du groupe 1 : %.2f\n", moyGroupe(promo, 1, effectif));
    
    // Vérification et correction des noms de famille
    verifMaj(promo, effectif);
    printf("\nNoms de famille vérifiés :\n");
    afficherTabEtudiants(promo, effectif);
    
    // Tri par la première lettre du nom
    tri_premiere_lettre(promo, effectif);
    printf("\nEtudiants triés par la première lettre de leur nom :\n");
    afficherTabEtudiants(promo, effectif);
    
    // Tri par le nom complet
    tri_nom(promo, effectif);
    printf("\nEtudiants triés par leur nom complet :\n");
    afficherTabEtudiants(promo, effectif);
    
    free(promo); // Libération de la mémoire allouée pour le tableau d'étudiants
    
    return 0;
}

``` 

<div id="4"></div>

## Exercice 4

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD4-Pointeurs-et-Structures_Informatique2p1s2/exo4.jpg){: .w-75 .shadow .rounded-10 }

+  On créer la structure représentant les statistiques pour une heure donnée après avoir definie `NB_HEURES`
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NB_HEURES 24

typedef struct {
    int heure;
    int mobile;
    int ordinateur;
} Stats;

``` 

+  On créer une fonction pour générer une valeur aléatoire entre min et max inclus
 

```c 
int random_int(int min, int max) {
    return rand() % (max - min + 1) + min;
}

``` 

+  On créer la fonction pour créer une liste de statistiques pour chaque heure de la journée
 

```c 
Stats *Stats_init() {
    Stats *liste_stats = malloc(NB_HEURES * sizeof(Stats));

    for (int i = 0; i < NB_HEURES; i++) {
        liste_stats[i].heure = i;
        liste_stats[i].mobile = random_int(0, 100);
        liste_stats[i].ordinateur = 100 - liste_stats[i].mobile;
    }

    return liste_stats;
}

``` 

+  On créer la procedure d'affichage des stats
 

```c 
void affficher_graphique(Stats *liste_stats) {
    printf("--------------------------------------------------------------\n");
    printf("| 100%%     MOBILES       0%% |    | 0%%    ORDINATEURS    100%% |\n");
    printf("--------------------------------------------------------------\n");

    for (int i = 23; i >= 0; i--) {
        printf("|");

        // Affichage des pourcentages de mobiles
        printf(" ");
        
        for (int j = liste_stats[i].mobile / 4; j < 25; j++) {
            printf(" ");
        }
        for (int j = 0; j < liste_stats[i].mobile / 4; j++) {
            printf("#");
        }
        
        printf(" | %2d | ", liste_stats[i].heure);

        // Affichage des pourcentages d'ordinateurs
        for (int j = 0; j < liste_stats[i].ordinateur / 4; j++) {
            printf("#");
        }
        for (int j = liste_stats[i].ordinateur / 4; j < 25; j++) {
            printf(" ");
        }
        printf(" |\n");
    }

    printf("--------------------------------------------------------------\n");
}

``` 

+  On test le tout dans le `main`
 

```c 
int main() {
    srand(time(NULL)); // Initialisation du générateur de nombres aléatoires
    
    // Création des statistiques pour chaque heure de la journée
    Stats *liste_stats = Stats_init();
    
    // Affichage du graphique pyramidal des statistiques
    affficher_graphique(liste_stats);

    // Libération de la mémoire allouée pour la liste des statistiques
    free(liste_stats);

    return 0;
}

``` 

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) 
