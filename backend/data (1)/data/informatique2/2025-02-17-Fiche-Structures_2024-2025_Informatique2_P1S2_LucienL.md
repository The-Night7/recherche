---
title: Fiche Les Structures en C
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

# Fiche de révision : Les Structures en C

## 1. Qu'est-ce qu'une structure?

Une **structure** en C est un regroupement de variables de types différents sous un même nom. Elle permet de manipuler des données complexes plus facilement.

## 2. Déclaration d'une structure

Une structure est définie avec le mot-clé struct.

```c
struct Point {
    int x;
    int y;
};
```

Ici, struct Point est un type de structure contenant deux variables x et y de type int.

## 3. Déclaration et initialisation d'une variable de structure

Une variable de structure peut être déclarée de plusieurs façons :

```c
struct Point p1; // Déclaration
p1.x = 10;
p1.y = 20; // Initialisation

```

Une structure peut aussi être initialisée directement :

```c
struct Point p2 = {30, 40};
```

## 4. Accès aux membres d'une structure

L'opérateur `.` est utilisé pour accéder aux membres d'une structure.

```c
printf("x: %d, y: %d\n", p1.x, p1.y);
```


## 5. Utilisation des pointeurs avec les structures

Un pointeur vers une structure est utilisé pour éviter la copie des données.

```c
struct Point *ptr = &p1;
printf("x: %d, y: %d\n", ptr->x, ptr->y); // Utilisation de l'opérateur ->
```

## 6. Structures imbriquées

Une structure peut contenir une autre structure.

```c
struct Rectangle {
    struct Point hautGauche;
    struct Point basDroit;
};
```

## 7. Structures et fonctions

Une structure peut être passée en argument à une fonction.

```c
void afficherPoint(struct Point p) {
    printf("x: %d, y: %d\n", p.x, p.y);
}
```

Pour éviter de copier les données, on peut utiliser un pointeur :

```c
void deplacerPoint(struct Point *p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
}
```

## 8. Structures et mémoire dynamique

Les structures peuvent être allouées dynamiquement avec malloc.

```c
struct Point *p = (struct Point *)malloc(sizeof(struct Point));
p->x = 50;
p->y = 60;
free(p);
```

## 9. Type `typedef` et structures

`typedef` permet de définir un alias pour simplifier l'utilisation des structures.

```c
typedef struct {
    int x;
    int y;
} Point;

Point p3 = {70, 80};
```

## 10. Bonnes pratiques


+ Toujours initialiser les structures avant utilisation.
+ Utiliser `typedef` pour rendre le code plus lisible.
+ Libérer la mémoire allouée dynamiquement (free).
+ Privilégier les pointeurs pour éviter la copie inutile de données.
