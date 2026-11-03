---
title: TD7 Fichier Correction
author: [AhmedA]
date: 2024-05-05 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Ahmed A.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---



Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) 



> Regarder la correction uniquement après avoir travaillé par vous-même, car si vous ne le faites pas, c’est le meilleur moyen de rater vos DS/CC.
{: .prompt-danger }



<div id="1"></div>

## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD7-Fichier_Informatique2p1s2/exo1.jpg){: .w-75 .shadow .rounded-10 }


+  On créer une fonction qui va verifier si le fichier a bien été ouvert
 

```c

#include <stdio.h>
#include <stdlib.h>

void check_error(FILE * file){
    if (file == NULL) {
        printf("Erreur lors de l'ouverture du fichier\n");
        exit(EXIT_FAILURE);
    }
}
```


+  1\. Voici les instructions pour créer et écrire dans le fichier texte.txt
 

```c 
int main() {

    FILE* fichier1 = fopen("texte.txt", "w");
    check_error(fichier1);

    fputs("Je suis ton père\n", fichier1);
    fclose(fichier1);

``` 


>  `fputs` permet d'écrire une chaîne de caractères sur un flux donné, si vous souhaitez manipuler des chaînes de caractères non formatées, alors cette fonction est préférable par rapport au `fprintf`. Effectivement, aucune recherche du caractère % ne sera effectuée. Il en résultera donc un temps d'exécution plus rapide.
{: .prompt-tip }


+  2\. Voici les instructions pour ouvrir le fichier en mode lecture
 

```c 
    FILE* fichier2 = fopen("texte.txt", "r");
    check_error(fichier2);

``` 


+  3\. Voici les instructions pour récupérer et afficher le premier caractère
 

```c 
    int premierchar = fgetc(fichier2);
    printf("Premier caractère: %c\n", premierchar);

``` 


>  `fgetc` ou `getc ` permettent de lire un caractère à la position courante du flux (la ou ets le curseur), on utilise un int ici car en cas d'erreur les deux fonctions retourne une valeur en dehors de l'intervale [0,256[ (`EOF`)
{: .prompt-tip }


+  4\. Voici les instructions pour récupérer et afficher la phrase entière
 

```c 
    fseek(fichier2, 0, SEEK_SET); // Retourner au début du fichier
    char phrase[100];
    if (fgets(phrase, 100, fichier2)==NULL){
        exit(EXIT_FAILURE);
    }
    printf("Phrase: %s", phrase);

``` 


+  5\. Voici les instructions pour écrire le mot "Luke" en début de fichier
 

```c 
    fseek(fichier2, 0, SEEK_SET); // Retourner au début du fichier
    fputs("Luke ", fichier2);
    fclose(fichier2);

``` 


+  6\. Créer et écrire dans le fichier chiffre.txt
 

```c 
    FILE* fichier3 = fopen("chiffre.txt", "w");
    check_error(fichier3);
    fputs("42 7 2.5", fichier3);
    fclose(fichier3);

``` 



+  7\. Voici les instructions pour faire la somme du premier et dernier nombre du fichier
 

```c 
    FILE* fichier4 = fopen("chiffre.txt", "r");
    check_error(fichier4);

    float nbdebut, nbfin, nbactuel;
    fscanf(fichier4, "%f", &nbdebut);

    while (fscanf(fichier4, "%f", &nbactuel) != EOF) {
        nbfin = nbactuel;
    }
    printf("Somme du premier et dernier nombre: %f\n", nbdebut + nbfin);

    fclose(fichier4);
    return 0;
}

``` 

<div id="2"></div>

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD7-Fichier_Informatique2p1s2/exo2.jpg){: .w-75 .shadow .rounded-10 }



+  On créer une fonction pour compter le nombre de caractères dans un fichier
 

```c 
#include <stdio.h>
#include <stdlib.h>

int file_len(FILE* file) {
    int count = 0;
    fseek(file, 0, SEEK_SET); // Se mettre au début du fichier
    while (fgetc(file) != EOF) { //fgetc decale a chaque fois la tête de lecture de 1
        count++;
    }
    fseek(file, 0, SEEK_SET); // Retourner au début du fichier
    return count;
}

``` 


+  On créer la fonction pour compter le nombre d'occurrences d'un caractère donné dans un fichier
 

```c 
int nmbCaractere(FILE* file, char a) {
    int count = 0;
    fseek(file, 0, SEEK_SET); // Se mettre au début du fichier
    int caractere = fgetc(file);
    while (caractere != EOF) {
        if (caractere == a) {
            count++;
        }
        caractere = fgetc(file);
    }
    fseek(file, 0, SEEK_SET); // Retourner au début du fichier
    return count;
}

``` 


+  On peut mainteant tout faire dans le `main`. 
 

```c 
int main() {
    // 1.
    FILE *fichier = fopen("harry_potter.txt", "r");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier harry_potter.txt\n");
        exit(EXIT_FAILURE);
    }

    // 2. 
    int nb = file_len(fichier);
    printf("Le nombre de caractères dans le fichier est : %d\n", nb);

    // 3. 
    char lettre1 = 'h';
    char lettre2 = 'H';
    printf("Le nombre d'occurrences de '%c' dans le fichier est : %d\n", 'h', nmbCaractere(fichier, lettre1));
    printf("Le nombre d'occurrences de '%c' dans le fichier est : %d\n", 'H', nmbCaractere(fichier, lettre2));

    // 4. 
    int occurrences[256] = {0}; // tableau pour chaque caractère ASCII (voir note bas de page pour l'explication de la notation occurrences[256] = {0})
    int caractere = fgetc(fichier);
    // cette methode est beaucoup plus optimisé que d'utiliser 256 fois la fonction nmbCaractere
    while (caractere != EOF) {
        occurrences[caractere]++;
        caractere = fgetc(fichier);
    }
    

    // 5.
    int total = nb;
    float proba[256];
    for (int i = 0; i < 256; i++) {
        if (proba[i] > 0 && total > 0)
        {
            proba[i] = (float)occurrences[i] / total;
        }
        
        
    }

    // Afficher chaque proba
    printf("\nProbabilités d'apparition :\n");
    for (int i = 0; i < 256; i++) {
        if (proba[i] > 0) {
            printf("\'%c\' : %.6f %%\n", i, proba[i] * 100);
        }
    }

    fclose(fichier);

    return 0;
}

``` 


>  `int occurrences[256] = {0};` est une notation qui permet d'initialiser tout les elements du tableau a 0 c'est equivalent a `int occurrences[256] = {0,0,0,0,0,0...};`256 fois
{: .prompt-tip }


>  Attention sur windows les caractères risque de mal se calculer
{: .prompt-warning }

<div id="3"></div>

## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD7-Fichier_Informatique2p1s2/exo3.jpg){: .w-75 .shadow .rounded-10 }

+ On fait la structure Etudiant et le remplissage du tableau d'étudiants (jsp de quel TD l'exo parle)
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ETUDIANTS 100
#define MAX_CHAR 50
#define FILE_ETU "etudiants.txt"
#define FILE_ETU_BIN "etudiants.bin"

typedef struct {
    char nom[MAX_CHAR];
    char prenom[MAX_CHAR];
    int age;
    float moyenne;
} Etudiant;

int better_scan(char * message){
    int ret_var = 0;
    int value = 1;
    while (ret_var != 1 || value < 0)
    {   
        printf("%s", message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}

float fbetter_scan(char * message){
    int ret_var = 0;
    float value = 1;
    while (ret_var != 1 || value < 0)
    {   
        printf("%s", message);
        ret_var = scanf("%f", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}

void remplirTableauEtudiants(Etudiant tab[], int *nb_etu) {
    *nb_etu = better_scan("Combien d'etudiants souhaitez-vous ajouter ? \n");

    for (int i = 0; i < *nb_etu; i++) {
        printf("Etudiant %d :\n", i + 1);

        printf("Nom : \n");
        if (fgets(tab[i].nom, MAX_CHAR, stdin) == NULL){
            exit(EXIT_FAILURE);
        }
        tab[i].nom[strlen(tab[i].nom) - 1] = '\0';

        printf("Prenom : \n");
        if (fgets(tab[i].prenom, MAX_CHAR, stdin) == NULL){
            exit(EXIT_FAILURE);
        }
        tab[i].prenom[strlen(tab[i].prenom) - 1] = '\0';

        tab[i].age = better_scan("Age : \n");
        tab[i].moyenne = better_scan("Moyenne : \n");
    }
}

``` 


+  On crée la fonction `ecrireEtudiant`
 

```c 

void ecrireEtudiant(Etudiant tab[], int nb_etu) {
    FILE *fichier = fopen(FILE_ETU, "w");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < nb_etu; i++) {
        fprintf(fichier, "%s %s, %d ans\n", tab[i].nom, tab[i].prenom, tab[i].age);
    }

    fclose(fichier);
}

``` 


+  On crée la fonction `lireEtudiant`
 

```c 

Etudiant *lireEtudiant(int *nb_etu) {
    FILE *fichier = fopen(FILE_ETU, "r");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return NULL;
    }

    // nombre d'étudiants dans le fichier
    *nb_etu = 0;
    char c;
    while ((c = fgetc(fichier)) != EOF) {
        if (c == '\n') {
            (*nb_etu)++;
        }
    }
    fseek(fichier, 0, SEEK_SET); // Se mettre au début du fichier

    // tab des etudiants 
    Etudiant *tab = malloc(*nb_etu * sizeof(Etudiant));

    // lecture
    for (int i = 0; i < *nb_etu; i++) {
        fscanf(fichier, "%s %s, %d ans\n", tab[i].nom, tab[i].prenom, &tab[i].age);
    }

    fclose(fichier);
    return tab;
}

``` 


+  On recrée la fonction pour intégrer la moyenne 
 

```c 

void ecrireEtudiant_moyenne(Etudiant tab[], int nb_etu) {
    FILE *fichier = fopen(FILE_ETU, "w");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return;
    }

    for (int i = 0; i < nb_etu; i++) {
        fprintf(fichier, "%s %s, %d ans, moyenne=%.2f\n", tab[i].nom, tab[i].prenom, tab[i].age, tab[i].moyenne);
    }

    fclose(fichier);
}

``` 



+  On ecrit les versions pour les fichiers bianires les versions des fonctions pour des fichiers binaires
 

```c 

void ecrireEtudiant_bin(Etudiant tab[], int nb_etu) {
    FILE *fichier = fopen(FILE_ETU_BIN, "wb");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return;
    }

    fwrite(tab, sizeof(Etudiant), nb_etu, fichier);

    fclose(fichier);
}

Etudiant *lireEtudiant_bin(int *nb_etu) {
    FILE *fichier = fopen(FILE_ETU_BIN, "rb");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return NULL;
    }

    // nombre d'étudiants dans le fichier
    fseek(fichier, 0, SEEK_END);
    long taille = ftell(fichier);
    *nb_etu = taille / sizeof(Etudiant);
    rewind(fichier); // Retourner au début du fichier

    // tableau d'étudiants
    Etudiant *tab = malloc(*nb_etu * sizeof(Etudiant));

    // Lire les étudiants depuis le fichier
    fread(tab, sizeof(Etudiant), *nb_etu, fichier);

    fclose(fichier);
    return tab;
}


``` 

<div id="4"></div>

## Exercice 4

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD7-Fichier_Informatique2p1s2/exo4.jpg){: .w-75 .shadow .rounded-10 }

+  On implemente cet exo directement
 

```c 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NB_CARACTERES 256 // Nombre de caractères possibles (ASCII)
#define LONGUEUR_TEXTE 1000 // Longueur du texte à générer

int main() {
    srand(time(NULL)); 
    // Ouvrir le fichier
    FILE *fichier = fopen("harry_potter.txt", "r");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return 1;
    }

    //  tableau 2D pour les occurrences des couples de caractères
    int occurrences_couples[NB_CARACTERES][NB_CARACTERES] = {0}; // (voir note bas de page pour l'explication de la notation = {0})

    // on rempklie le tableau des occurrences des couples de caractères
    int caractere_precedent = fgetc(fichier); // Lire le premier caractère
    int caractere_actuel = fgetc(fichier);
    while (caractere_actuel != EOF) {
        occurrences_couples[caractere_precedent][caractere_actuel]++;
        caractere_precedent = caractere_actuel;
        caractere_actuel = fgetc(fichier);
    }
    fclose(fichier);

    // tableau 2D pour les probabilités cumulées des couples de caractères
    float probabilites_cumulees[NB_CARACTERES][NB_CARACTERES] = {0.0}; // (voir note bas de page pour l'explication de la notation = {0.0})
    for (int i = 0; i < NB_CARACTERES; i++) {
        int total_occurrences = 0;
        for (int j = 0; j < NB_CARACTERES; j++) {
            total_occurrences += occurrences_couples[i][j];
        }
        if (total_occurrences > 0) {
            for (int j = 0; j < NB_CARACTERES; j++) {
                probabilites_cumulees[i][j] = (float)occurrences_couples[i][j] / total_occurrences;
            }
        }
    }

    // Généreration aléatoire du texte en utilisant les probabilités cumulées des couples de caractères
    int caractere_initial = ' ';  // peut être n'importe quel caractère
    printf("Texte genere :\n");
    for (int i = 0; i < LONGUEUR_TEXTE; i++) {
        int caractere_suivant = caractere_initial;
        while (caractere_suivant == caractere_initial) {
            float random_probabilite = (float)rand() / RAND_MAX; // Générer un nombre aléatoire entre 0 et 1
            float probabilite_cumulee = 0.0;
            for (int j = 0; j < NB_CARACTERES; j++) {
                probabilite_cumulee += probabilites_cumulees[caractere_initial][j];
                if (random_probabilite <= probabilite_cumulee) {
                    caractere_suivant = j;
                    break;
                }
            }
        }
        printf("%c", caractere_suivant);
        caractere_initial = caractere_suivant;
    }
    printf("\n");

    return 0;
}

``` 
>  ` = {0};` est une notation qui permet d'initialiser tout les elements du tableau a 0
{: .prompt-tip }

<div id="5"></div>

## Exercice 5

![exercice 5](https://data.cy.deltahmed.fr/DATA/TD7-Fichier_Informatique2p1s2/exo5.jpg)![exercice 5](https://data.cy.deltahmed.fr/DATA/TD7-Fichier_Informatique2p1s2/exo5_2.jpg){: .w-75 .shadow .rounded-10 }

+  Exemple d'implementation d’écriture en JSON
 

```c 

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char *nom;
    char *prenom;
    int groupe;
    float notes[6];
} Etudiant;

void ecrireJSON(Etudiant *etudiants, int nombreEtudiants) {
    FILE *fichier = fopen("etudiants.json", "w");
    if (fichier == NULL) {
        printf("Erreur lors de l'ouverture du fichier.\n");
        return;
    }

    fprintf(fichier, "[\n");
    for (int i = 0; i < nombreEtudiants; i++) {
        fprintf(fichier, "\t{\n");
        fprintf(fichier, "\t\t\"nom\" : \"%s\",\n", etudiants[i].nom);
        fprintf(fichier, "\t\t\"prenom\" : \"%s\",\n", etudiants[i].prenom);
        fprintf(fichier, "\t\t\"groupe\" : %d,\n", etudiants[i].groupe);
        fprintf(fichier, "\t\t\"notes\" : [");
        for (int j = 0; j < 6; j++) {
            fprintf(fichier, "%.2f", etudiants[i].notes[j]);
            if (j < 5) {
                fprintf(fichier, ", ");
            }
        }
        fprintf(fichier, "]\n");
        fprintf(fichier, "\t}");
        if (i < nombreEtudiants - 1) {
            fprintf(fichier, ",");
        }
        fprintf(fichier, "\n");
    }
    fprintf(fichier, "]\n");

    fclose(fichier);
}

int main() {
    Etudiant etudiants[3] = {
        {"Kamal", "ibn el kadi mansour", 1, {12.57, 16.58, 13.2, 5.7, 8.8, 19.5}},
        {"Quandale", "Dingle", 2, {2.57, 6.58, 3.2, 15.7, 18.8, 9.5}},
        {"Zied", "Anas", 4, {11.1, 12.2, 13.3, 14.4, 15.0, 20.0}}
    };

    ecrireJSON(etudiants, 3);

    return 0;
}


``` 

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) 
