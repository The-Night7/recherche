---
title: DS1 2022 2023 Correction (DS4)
author:  [AhmedA]
date: 2024-03-20 01:00:00 +0100
categories: [PREING1 S2,Informatique2-DS]
tags: [PREING1 S2,Informatique2-DS,Ahmed A.,DS1]
division_title : DS1
---

Exercices : [1](#1) [2](#2) [3](#3) 

DS1-2022-2023-Correction-(DS4)_Informatique2-DS_P1S2_AhmedA

<div id="1"></div>

## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/DS1-2022-2023-Correction-(DS4-Anciennement)_Informatique2-DSp1s2/exo1.jpg){: .w-75 .shadow .rounded-10 }

![exercice 12](https://data.cy.deltahmed.fr/DATA/DS1-2022-2023-Correction-(DS4-Anciennement)_Informatique2-DSp1s2/exo1_2.jpg){: .w-75 .shadow .rounded-10 }


+ On inclue les bibliothèque et on definie les variables utiles
 

```c 
#include <stdio.h> 
#include <stdlib.h>
#include <string.h> 

#define MAX_CHAR 100 // Définition de la taille maximale d'une chaîne de caractères

``` 


+  On définie la structure pour la date
 

```c 
typedef struct {
    int jour;
    int mois;
    int annee;
} Date;
``` 


+  On définie la structure pour la adresse
 

```c 
typedef struct {
    int numeroRue;
    char nomRue[MAX_CHAR];
    char nomVille[MAX_CHAR];
} Adresse;
``` 


+  On définie la structure pour le client
 

```c 
typedef struct {
    char nom[MAX_CHAR];
    char prenom[MAX_CHAR];
    Adresse adresse;
    int points_fidel;
    Date dateNaissance;
    Date dateAdhesion;
} Client;
``` 


+  On créer la fonction pour afficher une adresse
 

```c 
void afficheAdresse(Adresse adr) {
    printf("%d %s, %s\n", adr.numeroRue, adr.nomRue, adr.nomVille);
}
``` 


+  On créer la fonction pour vérifier si deux dates sont identiques
 

```c 
int memeDate(Date date1, Date date2) {
    return (date1.jour == date2.jour) && (date1.mois == date2.mois);
}
``` 


+  On créer la fonction pour calculer le nombre d'années entre deux dates
 

```c 
int nombreAnnees(Date date1, Date date2) {
    int ans = date2.annee - date1.annee;
    if (date2.mois < date1.mois || (date2.mois == date1.mois && date2.jour < date1.jour)) {
        ans--;
    }
    return ans;
}
``` 


+  On créer la fonction pour comparer deux chaînes de caractères
 

```c 
int memeMot(char mot1[], char mot2[]) {
    int i = 0;
    while (mot1[i] == mot2[i]) {
        if (mot1[i] == '\0' && mot2[i] == '\0')
            return 1;
        i++;
    }
    return 0;
}

``` 


+  Deuxième méthode (utilisation de strcmp car l'utilisation n'est pas interdite)
 

```c 
int memeMot(char mot1[], char mot2[]) {
    return !strcmp(mot1, mot2); // Utilisation de la fonction strcmp de la bibliothèque string.h
}
``` 


+  On créer une fonction pour saisir les entiers naturels
 

```c 
int better_scan(char * message){
    int var = -1;
    int ret_var = 0;
    while (ret_var != 0 || var < 0)
    {   
        printf(message); // Affichage du message
        ret_var = scanf("%d", &var); // Lecture de l'entier
        while(getchar()!='\n'){} // Vidage du tampon d'entrée (ligne facultative)
    }
    return var;
}
``` 


> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }


+  On créer une fonction pour saisir les entiers naturels (avec une valeur maximale)
 

```c 
int better_scan_val_max(char * message, int max){
    int var = -1;
    int ret_var = 0;
    while (ret_var != 0 || var < 0 && var > max)
    {   
        printf(message); // Affichage du message
        ret_var = scanf("%d", &var); // Lecture de l'entier
        while(getchar()!='\n'){} // Vidage du tampon d'entrée (ligne facultative)
    }
    return var;
}
``` 


> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }



+  On créer la fonction pour saisir les informations d'un client
 

```c 
Client saisirClient() {
    Client client;
    // Lecture du nom avec fgets pour éviter les problèmes de débordement de mémoire (on peut utiliser aussi un scanf)
    printf("Nom: ");
    if (fgets(client.nom , MAX_CHAR, stdin) == NULL) {
        exit(1);
    }
    client.nom[strlen(client.nom)-1] = '\0';

    printf("Prénom: ");
    if (fgets(client.prenom , MAX_CHAR, stdin) == NULL) {
        exit(1);
    }
    client.prenom[strlen(client.prenom)-1] = '\0';

    client.adresse.numeroRue = better_scan("Numéro de rue:");

    printf("Rue : ");
    if (fgets(client.adresse.nomRue , MAX_CHAR, stdin) == NULL) {
        exit(1);
    }
    client.adresse.nomRue[strlen(client.adresse.nomRue)-1] = '\0';

    printf("Nom de ville: ");
    if (fgets(client.adresse.nomVille , MAX_CHAR, stdin) == NULL) {
        exit(1);
    }
    client.adresse.nomVille[strlen(client.adresse.nomVille)-1] = '\0';

    client.points_fidel = better_scan("Points de fidélité (0 au départ): ");
    printf("Date de naissance (jj/mm/aaaa): ");
    client.dateNaissance.jour = better_scan_val_max("Date de naissance jj: ", 31);
    client.dateNaissance.mois = better_scan_val_max("Date de naissance mm: ", 12);
    client.dateNaissance.annee = better_scan("Date de naissance aaaa: ");

    // Utilisation de la date actuelle pour la date d'adhésion
    client.dateAdhesion.jour = 23;
    client.dateAdhesion.mois = 2;
    client.dateAdhesion.annee = 2023;
    return client;  // Retourne le client saisi
}
``` 


> `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fonction renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`.
{: .prompt-info }


+  On créer la fonction pour mettre à jour les points de fidélité d'un client en fonction d'un montant d'achat
 

```c 
void majPoint(Client *client, int montantAchat) {
    client->points_fidel += montantAchat / 100;
}
``` 


+  deuxième methode car l'énoncé n'est pas clair (retourne une copie modifiée du client)
 

```c 
void majPoint(Client client, int montantAchat) {
    client.points_fidel += montantAchat / 100;
    return client; // Cette fonction devrait retourner un Client* pour modifier le client passé par référence
}
``` 


+  On créer la fonction pour calculer le taux de réduction applicable à un client
 

```c 
float reduction(Client client) {
    Date dateActuelle = {19, 3, 2024}; // Date actuelle

    float tauxReduction = nombreAnnees(client.dateAdhesion, dateActuelle) * 0.05; // 5% par année de fidélité
    
    tauxReduction += client.points_fidel * 0.01; // 1% par point de fidélité

    if (tauxReduction > 0.5){
        tauxReduction = 0.5; // Plafonnement à 50%
    }
    return tauxReduction; // Retourne le taux de réduction calculé
}
``` 


+  On créer la fonction pour afficher les clients dont c'est l'anniversaire aujourd'hui
 

```c 
void anniversaire(Client tableau[], int taille, Date date) {
    for (int i = 0; i < taille; i++) {
        if (tableau[i].dateNaissance.jour == date.jour && tableau[i].dateNaissance.mois == date.mois)
            printf("%s %s\n", tableau[i].prenom, tableau[i].nom);
    }
}
``` 


+  On créer la fonction pour afficher les adresses des clients dans une ville donnée
 

```c 
void adressePublicite(Client tableau[], int taille, char ville[]) {
    for (int i = 0; i < taille; i++) {
        if (memeMot(tableau[i].adresse.nomVille, ville))
            afficheAdresse(tableau[i].adresse);
    }
}

``` 



<div id="2"></div>

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/DS1-2022-2023-Correction-(DS4-Anciennement)_Informatique2-DSp1s2/exo2.jpg){: .w-75 .shadow .rounded-10 }



+  On créer une fonction tableauCroissant qui vas verifier si un tableau est croissant 
 

```c 
int tableauCroissant(char * tab, int taille){
    for (int i = 0; i < taille-1; i++)
    {
        if (*(tab+i) > *(tab+i+1))
        {
            return 0;
        }
        
    }
    return 1;
    
}
``` 

<div id="3"></div>

## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/DS1-2022-2023-Correction-(DS4-Anciennement)_Informatique2-DSp1s2/exo3.jpg){: .w-75 .shadow .rounded-10 }



+  Déclaration de la fonction pour trier les trois valeurs
 

```c 
#include <stdio.h>

void traitement(float *a, float *b, float *c) {
    float temp;
    // Tri des valeurs pour s'assurer que a <= b <= c
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if (*b > *c) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
}
``` 


+  On créer une fonction pour saisir les entiers naturels
 

```c 
float better_scan(char * message){
    float var;
    int ret_var = 0;
    while (ret_var != 0)
    {   
        printf(message); // Affichage du message
        ret_var = scanf("%f", &var); // Lecture de l'entier
        while(getchar()!='\n'){} // Vidage du tampon d'entrée (ligne facultative)
    }
    return var;
}
``` 


> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }


+  On test le tout dans le main
 

```c 
int main() {
    float a, b, c;

    // Demande à l'utilisateur de saisir les trois valeurs
    a = better_scan("Entrez a : \n");
    b = better_scan("Entrez b : \n");
    c = better_scan("Entrez v : \n");

    // Appel de la fonction de traitement pour trier les valeurs
    traitement(&a, &b, &c);

    // Affichage des valeurs triées
    printf("Les valeurs triées sont : %f, %f, %f\n", a, b, c);

    return 0;
}

``` 

Exercices : [1](#1) [2](#2) [3](#3) 
