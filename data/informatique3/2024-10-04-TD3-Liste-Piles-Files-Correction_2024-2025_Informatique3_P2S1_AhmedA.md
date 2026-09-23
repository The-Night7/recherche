---
title: TD03 Liste Piles Files Correction
author: [AhmedA] 
date: 2024-10-04 01:00:00 +0100
categories: [PREING2 S1,Informatique3]
tags: [PREING2 S1,Informatique3,Ahmed A.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---



Exercices : [1](#1) [2](#2) 

<div id="1"></div>

## Exercice 1
[Télécharger l'exercice exo1.c](https://data2.cy.deltahmed.fr/DATA/info/TD3-Liste-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo1.c){:target="_blank"} 

![exercice 1](https://data2.cy.deltahmed.fr/DATA/info/TD3-Liste-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo1.jpg){: .w-75 .shadow .rounded-10 }

+  On reprend le code du TD1 et on l'adapte pour la liste doublement chaînée de chaine de char
 

```c 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_C 20  // Définit la taille maximale d'une chaîne de caractères à 20

typedef struct chainon_struct {
    char value[MAX_C];                // Le contenu du chainon, ici une chaîne de caractères
    struct chainon_struct* previous;  // Pointeur vers l'élément précédent dans la liste
    struct chainon_struct* next;      // Pointeur vers l'élément suivant dans la liste
} Chainon;


typedef struct liste_struct {
    Chainon* tete;  // Pointeur vers le premier élément de la liste
    Chainon* fin;   // Pointeur vers le dernier élément de la liste
} Liste;

Chainon* creationChainon(char* str) {
    // Vérification si la chaîne d'entrée est nulle
    if (str == NULL) {
        exit(EXIT_FAILURE);  // Si oui, on quitte le programme
    }
    // Vérification que la chaîne ne dépasse pas la taille maximale
    if (strlen(str) > MAX_C) {
        exit(EXIT_FAILURE);  // Si oui, on quitte le programme
    }

    Chainon* nouveau = malloc(sizeof(Chainon));
    if (nouveau == NULL) {
        exit(EXIT_FAILURE);  // Si l'allocation échoue, on quitte le programme
    }

    // Copier la chaîne de caractères dans le nouveau chainon
    strcpy(nouveau->value, str);
    nouveau->previous = NULL;  // Le pointeur vers le chainon précédent est initialisé à NULL
    nouveau->next = NULL;      // Le pointeur vers le chainon suivant est initialisé à NULL
    return nouveau;            // Retourne le nouveau chainon créé
}

Liste creationListe() {
    Liste lst;
    lst.tete = NULL;  // Initialise la tête de la liste à NULL (liste vide)
    lst.fin = NULL;   // Initialise la fin de la liste à NULL (liste vide)
    return lst;       // Retourne la liste vide créée
}

``` 


+  On crée la fonction pour comparer deux chaînes de caractères (mot1 et mot2) la fonction retourne 1 si mot1 est avant mot2 dans l'ordre alphabétique, sinon 0
 

```c 
int compareMot(char *mot1, char* mot2) {
    // Vérification que les chaînes ne sont pas nulles
    if (mot1 == NULL || mot2 == NULL) {
        exit(EXIT_FAILURE);  // Si oui, on quitte le programme
    }
    // Vérification que les chaînes ne dépassent pas la taille maximale autorisée
    if (strlen(mot1) > MAX_C-1 || strlen(mot2) > MAX_C-1) {
        exit(EXIT_FAILURE);  // Si oui, on quitte le programme
    }
    // Comparaison des chaînes de caractères
    if (strcmp(mot1, mot2) < 0) {
        return 1;  // mot1 est avant mot2 dans l'ordre alphabétique
    } else {
        return 0;  // mot1 n'est pas avant mot2
    }
}

``` 


+  On crée la fonction qui insère un chainon au début de la liste
 

```c 
Chainon* insertDebut(Chainon* pliste, char* a) {
    // Vérification que la chaîne n'est pas nulle et ne dépasse pas la taille maximale
    if (a == NULL || strlen(a) > MAX_C) {
        exit(EXIT_FAILURE);  // Si oui, on quitte le programme
    }
    // Si la liste est vide, on crée le premier chainon
    if (pliste == NULL) {
        pliste = creationChainon(a);
    } else {
        // Sinon, on crée un nouveau chainon et on le place en tête
        Chainon* nouveau = creationChainon(a);
        nouveau->next = pliste;  // Le nouveau chainon pointe vers l'ancien premier chainon
        nouveau->previous = NULL;  // Le nouveau chainon n'a pas de précédent
        pliste = nouveau;  // On met à jour la tête de la liste
    }
    return pliste;  // Retourne la nouvelle tête de la liste
}

``` 


+  On crée la fonction pour insérer un mot dans la liste de manière triée
 

```c 
void insertListe(char* mot1, Liste* pliste) {
    // Vérification que la chaîne n'est pas nulle et que la liste n'est pas nulle
    if (mot1 == NULL || pliste == NULL || strlen(mot1) >= MAX_C) {
        exit(EXIT_FAILURE);  // Si oui, on quitte le programme
    }

    // Si la liste est vide, on insère le premier chainon
    if (pliste->tete == NULL) {
        pliste->tete = creationChainon(mot1);
        pliste->fin = pliste->tete;  // La tête et la fin sont identiques car il n'y a qu'un élément
        return;
    }

    // Si le mot doit être inséré au début de la liste
    if (compareMot(mot1, pliste->tete->value)) {
        pliste->tete = insertDebut(pliste->tete, mot1);  // On insère le mot en tête
        return;
    }

    // Recherche de la bonne position dans la liste pour insérer le mot
    Chainon* borne1 = pliste->tete;  // borne1 commence à la tête de la liste
    Chainon* borne2 = pliste->tete->next;  // borne2 pointe sur l'élément suivant
    while (borne2 != NULL) {
        // Si mot1 doit être inséré entre borne1 et borne2
        if (compareMot(borne1->value, mot1) && compareMot(mot1, borne2->value)) {
            Chainon* new = creationChainon(mot1);  // Crée un nouveau chainon
            new->previous = borne1;  // Mise à jour des liens
            new->next = borne2;
            borne1->next = new;
            borne2->previous = new;
            return;
        }
        // Avance dans la liste
        borne1 = borne2;
        borne2 = borne2->next;
    }

    // Si le mot doit être inséré à la fin de la liste
    pliste->fin->next = creationChainon(mot1);  // Insère le nouveau chainon après l'actuelle fin
    pliste->fin->next->previous = pliste->fin;  // Met à jour les liens
    pliste->fin = pliste->fin->next;  // Le nouveau chainon devient la nouvelle fin de la liste
}

``` 


+  On crée la fonction pour afficher la liste dans l'ordre croissant (de la tête à la fin)
 

```c 
void affiche(Liste *pliste) {
    if (pliste == NULL) {
        exit(EXIT_FAILURE);  // Si la liste est nulle, on quitte le programme
    }

    // Si la liste est vide, on affiche des crochets vides
    if (pliste->tete == NULL) {
        printf("[]\n");
        return;
    }

    Chainon* actual = pliste->tete;  // Commence à la tête de la liste
    printf("[");
    // Parcourt chaque chainon de la liste
    while (actual->next != NULL) {  
        printf("%s, ",actual->value);  // Affiche la valeur du chainon courant
        actual = actual->next;  // Passe au chainon suivant
    }
    // Affiche le dernier élément sans virgule
    printf("%s]\n",actual->value);
}

``` 


+  On crée la fonction pour afficher la liste dans l'ordre inverse (de la fin à la tête)
 

```c 
void afficheInv(Liste *pliste) {
    if (pliste == NULL) {
        exit(EXIT_FAILURE);  // Si la liste est nulle, on quitte le programme
    }

    // Si la liste est vide, on affiche des crochets vides
    if (pliste->tete == NULL) {
        printf("[]\n");
        return;
    }

    Chainon* actual = pliste->fin;  // Commence à la fin de la liste
    printf("[");
    // Parcourt chaque chainon de la liste à l'envers
    while (actual->previous != NULL) {  
        printf("%s, ",actual->value);  // Affiche la valeur du chainon courant
        actual = actual->previous;  // Passe au chainon précédent
    }
    // Affiche le dernier élément sans virgule
    printf("%s]\n",actual->value);
}

``` 


+  On teste dans le main l'insertion de mots et leur affichage
 

```c 
int main() {
    Liste l = creationListe();  // Crée une liste vide

    // Insertion de 20 mots dans la liste
    insertListe("popito", &l);
    insertListe("chat", &l);
    insertListe("chainon", &l);
    insertListe("article", &l);
    insertListe("zoo", &l);
    insertListe("tete", &l);
    insertListe("valeur", &l);
    insertListe("inspiration", &l);
    insertListe("insertion", &l);
    insertListe("vinland", &l);
    insertListe("interpole", &l);
    insertListe("microphone", &l);
    insertListe("raciste", &l);
    insertListe("rattrapage", &l);
    insertListe("file", &l);
    insertListe("pile", &l);
    insertListe("kebab", &l);
    insertListe("flemme", &l);
    insertListe("procrastination", &l);
    insertListe("affichage", &l);

    // Affichage de la liste dans l'ordre croissant
    affiche(&l);

    // Affichage de la liste dans l'ordre décroissant
    afficheInv(&l);

    return 0;  // Fin du programme
}

``` 

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/TD3-Liste-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo2.c){:target="_blank"} 

![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/TD3-Liste-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo2.jpg)![exercice 2](https://data2.cy.deltahmed.fr/DATA/info/TD3-Liste-Piles-Files-Correction_Informatique3p2s1-2024-2025/exo2_2.jpg){: .w-75 .shadow .rounded-10 }
#include <stdio.h>
#include <stdlib.h>


+  On définition de la structure Crepe pour représenter une crêpe avec son diamètre
 

```c 
typedef struct crepe_struct {
    int diametre;
    struct crepe_struct* next;
} Crepe;

typedef Crepe* Pcrepe;

``` 


+  On crée la fonction pour insérer une crêpe dans une file
 

```c 
Pcrepe inserFile(Pcrepe tete, Crepe* crepe) {
    if (tete == NULL) {
        return crepe; // Si la file est vide, la crêpe devient la tête
    }
    Pcrepe temp = tete;
    while (temp->next != NULL) {
        temp = temp->next; // Parcours jusqu'à la fin de la file
    }
    temp->next = crepe;
    return tete;
}

``` 


+  On crée la fonction pour supprimer une crêpe dans une FILE
 

```c 
Pcrepe suppFile(Pcrepe tete) {
    if (tete == NULL) {
        return NULL; // Si la file est vide
    }
    Pcrepe temp = tete->next;
    free(tete); // Libération de la mémoire
    return temp; // Le suivant devient la nouvelle tête
}

``` 


+  On crée la fonction pour insérer une crêpe dans une PILE
 

```c 
Pcrepe inserPile(Pcrepe tete, Crepe* crepe) {
    crepe->next = tete; // La nouvelle crêpe pointe sur l'ancienne tête
    return crepe; // La nouvelle crêpe devient la tête
}

``` 


+  On crée la fonction pour supprimer une crêpe dans une PILE
 

```c 
Pcrepe suppPile(Pcrepe tete) {
    return suppFile(tete); // Exactement la même que suppfile donc on peut juste reutiliser la fonction
}

``` 


+  On crée la fonction pour vérifier si la pile est triée par ordre croissant
 

```c 
int triCrepe(Pcrepe tete) {
    if (tete == NULL || tete->next == NULL) {
        return 1; // Une pile vide ou avec une seule crêpe est forcément triée
    }
    while (tete->next != NULL) {
        if (tete->diametre > tete->next->diametre) {
            return 0; // Si un diamètre est plus grand que le suivant, la pile n'est pas triée
        }
        tete = tete->next;
    }
    return 1;
}

``` 


+  On crée la fonction pour inverser les M premiers éléments d'une pile
 

```c 
Pcrepe invCrepe(Pcrepe tete, int M) {
    Pcrepe file = NULL;
    Pcrepe temp = tete;
    Pcrepe temp2;
    int i = 0;
    
    // Transférer les M premiers éléments dans une file
    while (i < M && temp != NULL)
    {
        Pcrepe actual = (Pcrepe)malloc(sizeof(Crepe));
        if (actual == NULL)
        {
            exit(EXIT_FAILURE);
        }
        
        actual->diametre = temp->diametre;
        actual->next = NULL;
        file = inserFile(file, actual);
        temp = temp->next;
        tete = suppPile(tete);
        
        i++;
    }
    // Remettre les éléments de la file dans la pile pour les inverser
    while (file != NULL) {
        Pcrepe crepe = (Pcrepe)malloc(sizeof(Crepe));
        if (crepe == NULL)
        {
            exit(EXIT_FAILURE);
        }
        
        crepe->diametre = file->diametre;
        tete = inserPile(tete, crepe);
        file = suppFile(file);
    }
    return tete;
}

``` 


+  On crée la fonction pour trouver l'indice de la crêpe la plus grande dans une pile de taille M
 

```c 
int indMax(Pcrepe tete, int M) {
    if (tete == NULL){
        return -1;
    }
    

    int max = tete->diametre;
    int index = 0;
    int i = 0;
    Pcrepe temp = tete;

    // Parcourir la pile pour trouver le maximum
    while (temp != NULL && i < M) {
        if (temp->diametre > max) {
            max = temp->diametre;
            index = i;
        }
        i++;
        temp = temp->next;
    }
    return index;
}

``` 


+  On crée la fonction pour inverser les M premières crêpes où la plus grande se trouve
 

```c 
Pcrepe spatule(Pcrepe tete, int M) {
    int index = indMax(tete, M);
    tete = invCrepe(tete, index + 1);
    tete = invCrepe(tete, M);
    return tete;
}

``` 


+  On crée la fonction principale pour trier les crêpes
 

```c 
void objectif(Pcrepe* tete) {
    Pcrepe temp = *tete;
    int taille = 0;
    
    // Calculer la taille de la pile
    while (temp != NULL) {
        taille++;
        temp = temp->next;
    }

    // Trier les crêpes en inversant les plus grandes à chaque itération
    for (int i = taille; i > 1; i--) {
        *tete = spatule(*tete, i);
    }
}

``` 



+  On teste le tout dans main
 

```c 
int main() {
    // Exemple de pile de crêpes non triées
    Pcrepe pile = NULL;
    
    int tailles[] = {3, 6, 2, 9, 7, 4, 5};
    for (int i = 6; i >= 0; i--) {
        Pcrepe crepe = (Pcrepe)malloc(sizeof(Crepe));
        if (crepe == NULL)
        {
            exit(EXIT_FAILURE);
        }
        
        crepe->diametre = tailles[i];
        crepe->next = NULL;
        pile = inserPile(pile, crepe); // Insérer chaque crêpe dans la pile
    }

    // Trier les crêpes
    objectif(&pile);
    
    // Affichage des crêpes triées
    Pcrepe temp = pile;
    printf("Crêpes triées par ordre croissant de diamètre:\n");
    while (temp != NULL) {
        printf("%d\n", temp->diametre); // Affichage de chaque crêpe triée
        temp = temp->next;
    }

    return 0;
}

``` 

Exercices : [1](#1) [2](#2) 
