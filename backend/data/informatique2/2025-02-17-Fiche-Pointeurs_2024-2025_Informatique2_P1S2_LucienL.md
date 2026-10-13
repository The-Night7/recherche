---
title: Fiche Les Pointeurs en C
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

# Fiche de révisions : Les Pointeurs en C

## 1. Qu'est-ce qu'un pointeur?

Un pointeur est une variable qui stocke l'adresse mémoire d'une autre variable. Il permet d'accéder et de manipuler directement la mémoire, ce qui rend la gestion des données plus efficace et permet de manipuler des structures complexes.

## 2. Déclaration et initialisation d'un pointeur

```c
int *ptr;  // ptr est un pointeur vers un entier
int var = 10;
ptr = &var;  // ptr est initialisé avec l'adresse de var
```


## 3. Accès a la valeur d'un pointeur

L'opérateur `*` permet d'accéder à la valeur stockée à l'adresse pointée.

```c
int value = *ptr;  // value est maintenant 10
```

## 4. Pointeurs et tableaux

Le nom d'un tableau agit comme un pointeur vers son premier élément.

```c
int arr[3] = {1, 2, 3};
int *ptr = arr;  // ptr pointe vers le premier élément de arr
```

## 5. Arithmétique des pointeurs

Les pointeurs supportent certaines opérations arithmétiques :
+ **Incrémentation** (`++`) : fait pointer le pointeur vers l'élément suivant.
+ **Décrémentation** (`--`) : fait pointer le pointeur vers l'élément précédent.

```c
int arr[] = {10, 20, 30};
int *p = arr;  // p pointe vers arr[0]
p++;
printf("%d", *p);  // Affiche 20
```

## 6. Pointeurs et fonctions

Les pointeurs sont utilisés pour passer des arguments par référence, permettant à une fonction de modifier la variable originale.

```c
void increment(int *num) {
    (*num)++;
}
int main() {
    int value = 5;
    increment(&value);
    printf("%d", value);  // Affiche 6
}
```

## 7. Pointeurs de pointeurs

Un pointeur peut stocker l'adresse d'un autre pointeur.

```c
int val = 5;
int *ptr = &val;
int **ptr_to_ptr = &ptr;
printf("%d", **ptr_to_ptr);  // Affiche 5
```

## 8. Allocation dynamique de mémoire

Les pointeurs permettent de gérer la mémoire dynamiquement.

```c
int *ptr = (int *)malloc(sizeof(int));
*ptr = 10;
free(ptr);  // Libération de la mémoire allouée
```

## 9. Pointeurs et structures


Les pointeurs peuvent être utilisés pour manipuler des structures de données complexes.

```c
struct Point {
    int x;
    int y;
};

struct Point p1 = {10, 20};
struct Point *p = &p1;
printf("%d", p->x);  // Affiche 10
```

## 10. Pointeurs NULL

Un pointeur peut être initialisé à NULL pour indiquer qu'il ne pointe vers aucune adresse valide.

```c
int *p = NULL;
```

## 11. Erreurs courantes

+   **Déréférencement d'un pointeur NULL** :
    ```c
    int *p = NULL;
    printf("%d", *p);  // Erreur !
    ```
+   **Fuite mémoire** : Ne pas libérer une mémoire allouée dynamiquement.
+   **Accès à une mémoire libérée** :
    ```c
    free(p);
    printf("%d", *p);  // Comportement indéfini
    ```

## 12. Bonnes pratiques


+ Toujours initialiser les pointeurs (`int *p = NULL;`).
+ Toujours libérer la mémoire allouée (`free(ptr);`).
+ Utiliser const si le pointeur ne doit pas modifier la valeur pointée.


