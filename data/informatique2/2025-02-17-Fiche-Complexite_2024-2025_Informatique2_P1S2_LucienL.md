---
title: Fiche Complexité Algorithmique en C
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---
# Fiche de Révision : Complexité Algorithmique en C


## 1. Introduction à la Complexité

La complexité algorithmique permet de mesurer l'efficacité d'un algorithme en termes de **temps d'exécution** et **d'utilisation mémoire**.

### Pourquoi étudier la complexité ?
- Comparer plusieurs algorithmes pour un même problème.
- Optimiser les performances en choisissant l’algorithme le plus adapté.
- Prédire le temps d'exécution et la mémoire utilisée en fonction de la taille des données.

### Complexité temporelle vs. spatiale
- **Complexité temporelle** : Nombre d'opérations exécutées en fonction de la taille de l’entrée.
- **Complexité spatiale** : Quantité de mémoire requise pour exécuter l’algorithme.
- **Principe espace-temps** : Pour accélérer un algorithme, il est souvent nécessaire d’utiliser plus de mémoire (ex : stockage de résultats intermédiaires).



## 2. Classes de Complexité Courantes

| Complexité         | Notation     | Exemples d'algorithmes                      |
|--------------------|--------------|---------------------------------------------|
| Constante          | O(1)         | Accès à un élément d’un tableau             |
| Logarithmique      | O(log n)     | Recherche dichotomique                      |
| Linéaire           | O(n)         | Parcours d'un tableau                       |
| Quasi-linéaire     | O(n log n)   | QuickSort, MergeSort                        |
| Quadratique        | O(n²)        | Tri par insertion, Tri à bulles             |
| Polynomiale        | O(nᵃ)        | Algorithme de Floyd-Warshall                |
| Exponentielle      | O(2ⁿ)        | Algorithmes de bruteforce                   |
| Factorielle        | O(n!)        | Problèmes combinatoires                     |



## 3. Comparaison des Algorithmes

**Exemple :** Recherche d'un mot dans un dictionnaire de 1 million de mots :

- **Recherche séquentielle (O(n))** :
  - Meilleur cas : 1 milliseconde.
  - Pire cas : 16 minutes.
  
- **Recherche dichotomique (O(log n))** :
  - Pire cas : 20 millisecondes.

**➡️ Conclusion :** Une amélioration de la complexité réduit drastiquement le temps d'exécution.



## 4. Calcul de la Complexité

Un algorithme est composé d’opérations élémentaires :
- **Affectations** : stockage de valeurs
- **Opérations arithmétiques** : +, -, *, /
- **Comparaisons** : ==, <, >, etc.

### Exemple d’algorithme itératif

- Nombre d'affectations : O(1)  
- Nombre de comparaisons : O(n)  
- Nombre d’additions : O(n)  

**➡️ Complexité totale : O(n)**

### Exemple d’algorithme récursif

- Nombre d’appels récursifs : n  
**➡️ Complexité totale : O(n)**



## 5. Algorithmes à Complexité Exponentielle

Un algorithme est dit exponentiel s’il double le nombre d’opérations à chaque nouvelle entrée.

### Exemple : Fibonacci naïf — **O(2ⁿ)**

**Problème :** Pour n = 50, il effectue plus de 10¹² opérations !

**✅ Solution :** Optimiser avec la **programmation dynamique** ➡️ O(n)



## 6. Erreurs Courantes

- Sous-estimer l'importance du **pire cas**.
- Ignorer les **constantes cachées** : O(1000n) vs O(2n).
- Utiliser un algorithme **inadapté** (ex : tri O(n²) au lieu de O(n log n)).
- Négliger la **complexité spatiale** : Un gain de temps peut entraîner une forte consommation mémoire.



## 7. Bonnes Pratiques

- Éviter les **boucles inutiles** ➡️ Réduction possible de O(n²) à O(n log n).
- Privilégier les **algorithmes optimisés** (ex : QuickSort vs Tri à bulles).
- Utiliser la **mémorisation** et la **programmation dynamique** pour éviter les recalculs inutiles.
- Viser une complexité **inférieure à O(n²)** quand c'est possible.

❌ **À éviter** : Les algorithmes exponentiels sont impraticables pour de grandes entrées.

