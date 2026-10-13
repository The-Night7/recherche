---
title: Fiche Algorithmes de Tri en C
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

# Fiche de Révision : Algorithmes de Tri en C

## 1. Introduction

Un algorithme de tri permet d'ordonner une liste d'éléments selon un critère donné (ordre croissant ou décroissant).

Les tris se divisent en deux grandes catégories :
- **Tris lents** : Complexité élevée (**O(n²)**), adaptés aux petites listes.
- **Tris rapides** : Complexité plus optimisée (**O(n log n)**), adaptés aux grandes listes.

## 2. Tris Lents (O(n²))

Les tris lents sont simples à implémenter mais inefficaces pour de grandes données.

### Tri par Sélection
- Trouve le plus petit élément et le place à sa position définitive.
- **Complexité** : O(n²) dans tous les cas.
- **Peu efficace**, sauf si les échanges sont plus coûteux que les comparaisons.

### Tri à Bulles
- Compare et échange les éléments adjacents pour les placer dans l'ordre.
- **Complexité** : O(n²) dans le pire cas, **O(n)** si déjà trié.
- **Peu performant**, rarement utilisé en pratique.

### Tri par Insertion
- Parcourt la liste en insérant chaque élément à sa position correcte.
- **Complexité** : O(n²) dans le pire cas, **O(n)** si la liste est déjà triée.
- **Adapté** aux petites listes ou aux données presque triées.

## 3. Tris Rapides (O(n log n))

Les tris rapides sont plus efficaces pour les grandes quantités de données.

### Tri Fusion (Merge Sort)
- Divise récursivement la liste en sous-listes puis fusionne les éléments triés.
- **Complexité** : O(n log n) dans tous les cas.
- **Stable**, efficace pour les grandes listes et utilisé en tri externe.

### Tri Rapide (QuickSort)
- Choisit un pivot, divise la liste en deux sous-listes et trie récursivement.
- **Complexité** : O(n log n) en moyenne, **O(n²)** dans le pire cas (pivot mal choisi).
- Très efficace pour les grandes listes en mémoire.

## 4. Comparaison des Algorithmes

| Tri        | Complexité Moyenne | Complexité Pire Cas | Stable ? | Mémoire Supplémentaire | Utilisation             |
|------------|--------------------|---------------------|----------|-------------------------|--------------------------|
| Sélection  | O(n²)              | O(n²)               | ❌        | ❌                      | Peu utilisé              |
| Bulles     | O(n²)              | O(n²)               | ✅        | ❌                      | Très lent                |
| Insertion  | O(n²)              | O(n²)               | ✅        | ❌                      | Petites listes           |
| Fusion     | O(n log n)         | O(n log n)          | ✅        | ✅ (O(n))               | Grandes listes           |
| Rapide     | O(n log n)         | O(n²)               | ❌        | ❌                      | Très efficace en mémoire |

✅ **Stable** : conserve l'ordre relatif des éléments égaux.  
❌ **Non stable** : peut changer l'ordre relatif des éléments égaux.

## 5. Choix du Bon Algorithme

- **Petites listes ou données déjà triées** → Tri par insertion.
- **Grandes listes** → Tri rapide (QuickSort) ou Tri fusion.
- **Besoins spécifiques** (tri en place, mémoire limitée) → Heap Sort (non abordé ici).
- **Peu d’échanges mais coût de comparaison important** → Tri par sélection.

## 6. Implémentation en Pseudo-code

### Tri par Insertion

```pseudo
pour i de 1 à longueur(tableau) - 1
    clé = tableau[i]
    j = i - 1
    tant que j >= 0 et tableau[j] > clé
        tableau[j + 1] = tableau[j]
        j = j - 1
    tableau[j + 1] = clé
```

### Tri par Sélection

```pseudo
pour i de 0 à longueur(tableau) - 1
    min = i
    pour j de i + 1 à longueur(tableau)
        si tableau[j] < tableau[min]
            min = j
    échanger tableau[i] et tableau[min]
```

### Tri à Bulles

```pseudo
pour i de 0 à longueur(tableau) - 1
    pour j de 0 à longueur(tableau) - i - 1
        si tableau[j] > tableau[j + 1]
            échanger tableau[j] et tableau[j + 1]
```

### Quicksort

```pseudo
fonction quicksort(tableau, bas, haut)
    si bas < haut
        pivot = partition(tableau, bas, haut)
        quicksort(tableau, bas, pivot - 1)
        quicksort(tableau, pivot + 1, haut)

fonction partition(tableau, bas, haut)
    pivot = tableau[haut]
    i = bas - 1
    pour j de bas à haut - 1
        si tableau[j] < pivot
            i = i + 1
            échanger tableau[i] et tableau[j]
    échanger tableau[i + 1] et tableau[haut]
    retourner i + 1
```

### Tri Fusion

```pseudo
fonction triFusion(tableau)
    si longueur(tableau) > 1
        milieu = longueur(tableau) / 2
        gauche = tableau[0..milieu - 1]
        droite = tableau[milieu..longueur(tableau) - 1]

        triFusion(gauche)
        triFusion(droite)

        i = j = k = 0

        tant que i < longueur(gauche) et j < longueur(droite)
            si gauche[i] < droite[j]
                tableau[k] = gauche[i]
                i = i + 1
            sinon
                tableau[k] = droite[j]
                j = j + 1
            k = k + 1

        tant que i < longueur(gauche)
            tableau[k] = gauche[i]
            i = i + 1
            k = k + 1

        tant que j < longueur(droite)
            tableau[k] = droite[j]
            j = j + 1
            k = k + 1
```
