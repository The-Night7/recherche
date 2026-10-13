---
title: Fiche Récursivité
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025, Récursivité]
math: true
mermaid: true
division_title : 2024/2025
---
# Fiche de Révision : La Récursivité en C


## 1. Introduction à la Récursivité

La récursivité est une technique de programmation où une fonction s'appelle elle-même pour résoudre un problème. Elle repose sur des relations de récurrence et agit comme une boucle implicite.

**Pourquoi utiliser la récursivité ?**
- Permet de résoudre des problèmes naturellement récursifs (ex. : suites, arbres).
- Offre une écriture plus intuitive et élégante.
- Peut être plus efficace pour certains algorithmes (ex. : parcours d'arbres). 
- Remplace parfois les boucles pour des tâches répétitives. 
- Tout algorithme récursif peut être transformé en version itérative.

## 2. Composantes d’une Fonction Récursive

Une fonction récursive comporte toujours : 
- **Une condition d'arrêt (cas de base)** pour éviter une boucle infinie. 
- **Un appel récursif** qui ramène le problème à une version plus simple.

Forme générale :
```c
f(x) = si c(x) alors g(x) // condition d'arrêt
       sinon h(f(s(x)), x) // appel récursif
```
Avec :
- `c(x)`: condition d'arrêt.
- `g(x)`: cas trivial retournant une valeur constante.
- `s(x)`: fonction successeur de x.
- `h(f(s(x)),x)`: appel récursif.

**Types de récursivité :**
- **Simple :** Un seul appel récursif dans la fonction.
- **Multiple :** Plusieurs appels récursifs (ex. : Fibonacci).
- **Terminale :** L'appel récursif est la dernière instruction (optimisable).
- **Non Terminale :** L'appel récursif est suivi d'une opération.
- **Croisée :** Deux fonctions s'appellent mutuellement.

## 3. Exemples de Fonctions Récursives

### 3.1 Factorielle d’un Nombre (Récursivité Non Terminale)

La factorielle suit la relation : $N! = N × (N-1)!$ avec $1! = 1$.
```c
#include <stdio.h>

int factorielle(int n) {
    if (n == 1) {
        return 1; // Cas de base
    }
    return n * factorielle(n - 1); // Récursivité
}

int main() {
    int nombre = 5;
    printf("Factorielle de %d = %d\n", nombre, factorielle(nombre));
    return 0;
}
```

### 3.2 Factorielle en Récursivité Terminale

La version terminale évite de stocker des appels récursifs dans la pile.

```c
#include <stdio.h>

int factorielleRT(int n, int acc) {
    if (n == 0) return acc;
    return factorielleRT(n - 1, acc * n);
}

int main() {
    int nombre = 5;
    printf("Factorielle de %d = %d\n", nombre, factorielleRT(nombre, 1));
    return 0;
}
```

### 3.3 Suite de Fibonacci (Récursivité Multiple)

```c
#include <stdio.h>

int fibonacci(int n) {
    if (n < 2) return n;
    return fibonacci(n - 1) + fibonacci(n - 2); // Appels multiples
}

int main() {
    int nombre = 6;
    printf("Fibonacci(%d) = %d\n", nombre, fibonacci(nombre));
    return 0;
}
```

## 4. Arbres de Récursivité

Un **arbre de récursivité** permet de visualiser l’enchaînement des appels récursifs d’une fonction.

**Exemple : `factorielle(5)`**

```c
factorielle(5)
└── 5 * factorielle(4)
    └── 4 * factorielle(3)
        └── 3 * factorielle(2)
            └── 2 * factorielle(1)
                └── 1 (cas de base)
```

Chaque nœud représente un appel de la fonction. Lorsque le cas de base est atteint, les résultats sont remontés pour produire la réponse finale.

## 5. Erreurs courantes

- **Oublier le cas de base** → Boucle infinie entraînant un dépassement de pile. 
- **Récursivité non optimisée** → Complexité exponentielle dans certains cas.
- **Stack Overflow** → Trop d’appels récursifs profonds sans optimisation. 
- **Utiliser une récursivité inefficace** → Peut ralentir le programme (ex. : Fibonacci naïf).

## 6. Bonnes Pratiques

- Toujours définir un **cas de base** clair. 
- Utiliser la récursivité terminale quand c'est possible. 
- Optimiser avec la **mémorisation (memoization)** pour éviter les recalculs inutiles. 
- Vérifier la **profondeur de récursion** pour éviter les erreurs de dépassement de pile. 
- Évaluer si une **solution itérative** est plus efficace.