---
title: Fiche Pointeurs dans les Structures
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

# Fiche de Révision : Pointeurs dans les Structures en C

## 1. Introduction aux Pointeurs dans les Structures

Les structures en C permettent de regrouper plusieurs variables sous un même type.L'utilisation de pointeurs dans une structure permet de manipuler dynamiquement des données et d'optimiser la gestion de la mémoire.

**Pourquoi utiliser des pointeurs dans les structures ?**
- ✔ Permet d’allouer dynamiquement des tableaux ou des objets de taille variable.
- ✔ Facilite la gestion et la modification des structures via des références.
- ✔ Optimise la mémoire en évitant des copies inutiles.

## 2. Déclaration d’une Structure avec un Pointeur

Une structure peut contenir un pointeur pour stocker des données allouées dynamiquement.

```c
typedef struct {
    char nom[50];
    int age;
    float *notes; // Pointeur vers un tableau de notes
} Etudiant;
```

## 3. Allocation Dynamique avec `malloc()`

Les pointeurs dans les structures nécessitent souvent une allocation dynamique de mémoire.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nom[50];
    int age;
    float *notes;
} Etudiant;

int main() {
    Etudiant e;
    e.age = 20;
    e.notes = (float*) malloc(3 * sizeof(float)); // Allocation pour 3 notes

    if (e.notes == NULL) {
        printf("Échec d'allocation mémoire\n");
        return 1;
    }

    e.notes[0] = 12.5;
    e.notes[1] = 15.0;
    e.notes[2] = 17.5;

    printf("Première note : %.2f\n", e.notes[0]);

    free(e.notes); // Libération de la mémoire
    return 0;
}
```

## 4. Utilisation d’un Pointeur vers une Structure

Un pointeur peut être utilisé pour accéder et modifier une structure.

```c
#include <stdio.h>

typedef struct {
    char nom[50];
    int age;
    float *notes;
} Etudiant;

int main() {
    Etudiant e1, *ptr;
    ptr = &e1;
    ptr->age = 22; // Équivaut à (*ptr).age = 22;

    printf("Âge : %d\n", ptr->age);
    return 0;
}
```
## 5. Allocation Dynamique d’une Structure

Une structure peut être allouée dynamiquement pour optimiser la gestion mémoire.
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nom[50];
    int age;
    float *notes;
} Etudiant;

int main() {
    Etudiant *etudiant = (Etudiant*) malloc(sizeof(Etudiant));

    if (etudiant == NULL) {
        printf("Échec d'allocation mémoire\n");
        return 1;
    }

    etudiant->age = 21;
    printf("Âge : %d\n", etudiant->age);

    free(etudiant); // Libération de mémoire
    return 0;
}
```
## 6. Tableaux de Structures Dynamiques

On peut allouer un tableau de structures dynamiquement.
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nom[50];
    int age;
    float *notes;
} Etudiant;

int main() {
    Etudiant *classe;
    int n = 2; // Nombre d'étudiants
    classe = (Etudiant*) malloc(n * sizeof(Etudiant));

    if (classe == NULL) {
        printf("Échec d'allocation mémoire\n");
        return 1;
    }

    classe[0].age = 19;
    classe[1].age = 20;

    printf("Âge du premier étudiant : %d\n", classe[0].age);
    printf("Âge du deuxième étudiant : %d\n", classe[1].age);

    free(classe);
    return 0;
}
```
## 7. Erreurs Courantes

- **Oublier de libérer la mémoire** → Risque de fuite mémoire.
- **Déréférencer un pointeur `NULL`** → Peut entraîner un plantage du programme.
- **Utiliser un pointeur après l’avoir libéré** → Peut causer un comportement indéfini.

## 8. Bonnes Pratiques

- Toujours vérifier le retour de `malloc()`.
- Libérer la mémoire avec `free()` après utilisation.
- Assigner `NULL` au pointeur après `free()` pour éviter les erreurs.
- Utiliser `ptr->membre` au lieu de `(*ptr)`.membre pour plus de clarté.