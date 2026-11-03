---
title: Fiche Allocation Dynamique
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---
# Fiche de révision : Allocation Dynamique en C
## 1. Introduction à l'Allocation Dynamique 
En C, la mémoire peut être allouée de deux manières : 

- **Allocation statique :** La mémoire est allouée au moment de la compilation. La taille  est fixe et connue à l'avance. 

- **Allocation dynamique :** La mémoire est allouée pendant l'exécution du programme. La taille peut être déterminée à l'exécution. 

L'allocation dynamique est utile lorsque la taille des données n'est pas connue à l'avance ou lorsque la taille peut varier pendant l'exécution du programme. 

## 2. Fonctions d'allocation dynamique 
### `malloc (Memory Allocation) `

- **Syntaxe :** `void* malloc(size_t size);` 
- Description : Alloue un bloc de mémoire de taille size octets et retourne un pointeur  vers le début de ce bloc. 
- Retour : Retourne un pointeur de type `void*` (pointeur générique) qui doit être casté dans le type approprié. Retourne `NULL` si l'allocation échoue. 
-   Exemple : 
    ```c
    malloc(sizeof(int) * 10); // Alloue un tableau de 10 entiers
    ```

### `free (Libération de Mémoire)`

- Syntaxe : `void free(void* ptr); `
- Description : Libère la mémoire précédemment allouée par malloc. 
-   Exemple :
    ```c
    free(ptr); // Libère la mémoire allouée
    ptr = NULL; // Bonne pratique pour éviter les erreurs de double libération
    ```

## 3. Exemple d'utilisation 

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;
    
    arr = (int*)malloc(n * sizeof(int));
    if (arr == NULL) { //verification importante et fait gagner des points
        printf("Échec de l'allocation mémoire\n");
        return 1;
    }
    
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;
    }
    
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    free(arr);
    arr = NULL;
    
    return 0;
}
```

## 4. Erreurs courantes 
- **Oublier de libérer la mémoire :** Cela conduit à des fuites de mémoire. 
- **Utiliser un pointeur après l'avoir libéré :** Peut causer des comportements indéfinis. 
- **Allouer trop de mémoire :** Peut entraîner une saturation de la mémoire disponible. 
## 5. Bonnes pratiques 
- **Vérifier le retour de malloc :** Toujours vérifier si malloc, calloc, ou realloc retournent NULL avant d'utiliser la mémoire allouée. 
- **Libérer la mémoire :** Toujours libérer la mémoire allouée dynamiquement avec free pour éviter les fuites de mémoire. 
- **Initialiser les pointeurs après free :** Assigner NULL après free pour éviter les erreurs de double libération. 
- **Éviter les déréférencements de pointeurs invalides :** Ne jamais utiliser un pointeur après l'avoir libéré.