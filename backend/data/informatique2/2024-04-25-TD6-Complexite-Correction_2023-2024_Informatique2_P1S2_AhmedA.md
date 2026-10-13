---
title: TD6 Complexite Correction
author: [AhmedA]
date: 2024-04-25 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Ahmed A.,2023/2024]
math: true
mermaid: true
division_title : 2023/2024
---

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) 

<div id="1"></div>



## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo1.jpg){: .w-75 .shadow .rounded-10 }


+  On nous demandera jamais ce genre de questions la formule du cours c'est :

$$\exists c \in \mathbb{R}^{+},\exists n_{0} \in \mathbb{N}^{+}, \forall n \ge n_{0}, g(n) \le c \times f(n) $$
 
+ Amusez vous bien 



<div id="2"></div>

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo2.jpg){: .w-75 .shadow .rounded-10 }

+ Les sommes sont du au fait que la boucle `pour j` vas de $0$ a $i$ et donc comme i varie le nombre d'iterations varie

| lignes | comparaison                                          | affectations                                                       | opérations             |
| ------ | ---------------------------------------------------- | ------------------------------------------------------------------ | ---------------------- |
| 1      |                                                      | $1$                                                                |                        |
| 2      | $5+1   $                                             |                                                                    |                        |
| 3      |                                                      | $5$                                                                |                        |
| 4      | $$\sum_{k=0}^{5} (k+1)$$                             | $$\sum_{k=0}^{5} (k+1)$$                                           |                        |
| 6      |                                                      | $$\sum_{k=0}^{5} (k)$$                                             | $$\sum_{k=0}^{5} (k)$$ |
| 7      |                                                      | $5$                                                                | $5$                    |
| Total  | $$5+1 \\ + 5+1 \\+ 4+1 \\+ 3+1 \\+ 2+1 \\+ 1+1 = 26$$ | $$1 +\sum_{k=0}^{5} (k+1) \\+ 5 + \sum_{k=0}^{5} (k) \\+ 5 = 46 $$ | $20$                   |
 


<div id="3"></div>

## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo3.jpg){: .w-75 .shadow .rounded-10 }

+   si $n$ est une puissance de 2 alors $ex(n)$ vaut pour $n=2^{k}, ex(n) = k$ 
+   si $n$ est un nombre quelconque alors $ex(n)$ vaut le $k$ du nombre arrondi a la puissance de deux au dessus $2^{k-1} < n \le 2^{k}, ex(n) = k$ 


| lignes | comparaison   | affectations     | opérations      |
| ------ | ------------- | ---------------- | --------------- |
| 1      |               | $2$              |                 |
| 2      | $\log_{2}(n)$ |                  |                 |
| 3      |               | $\log_{2}(n)-1$  | $\log_{2}(n)-1$ |
| 4      |               | $\log_{2}(n)-1$  |                 |
| 6      |               | $1$              |                 |
| Total  | $\log_{2}(n)$ | $2\log_{2}(n)+1$ | $\log_{2}(n)-1$ |

+ Ici on utilise $\log_{2}(n)$ car on fait $k$ iterations pour $2^{k-1} < n \le 2^{k}$ une manière de comprendre plus simple ce serait de faire en fonction de $k$ 

| lignes | comparaison | affectations | opérations |
| ------ | ----------- | ------------ | ---------- |
| 1      |             | $2$          |            |
| 2      | $k$         |              |            |
| 3      |             | $k-1$        | $k-1$      |
| 4      |             | $k-1$        |            |
| 6      |             | $1$          |            |
| Total  | $k$         | $2k+1$       | $k-1$      |

+ C'est comme si on avais juste remplacer $k$ par $\log_{2}(n)$


<div id="4"></div>

## Exercice 4

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo4.jpg)![exercice 4](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo4_2.jpg){: .w-75 .shadow .rounded-10 }

+ a) $O(n \times m)$
+ b) $O(n+m)$
+ c) On a $7\times(4 \times \text{constante})$ donc on a $O(1)$
+ d) dans la première boucle on fait $\min(n,m)$ iterations dans la deuxième on fait soit $0$ soit $m-n$ iterations dans la 3eme on fait $0$ soit $n-m$ iterations donc ont fait $\min(n,m) + \vert n-m \vert$ iterations donc :

$$\min(n,m) + \vert n-m \vert = \frac{n+m - \vert n-m \vert}{2} + \vert n-m \vert$$

$$= \frac{n+m + \vert n-m \vert}{2}= \Biggl \{ \begin{matrix} \frac{1}{2}(n+m + n-m ) && n-m \ge 0 \\ \frac{1}{2}(n+m -n+m ) && n-m < 0 \end{matrix}$$

$$= \Biggl \{ \begin{matrix} \frac{1}{2}(2n) = n && n-m \ge 0 \\ \frac{1}{2}(2m)=m && n-m < 0 \end{matrix}$$

+ Donc si $n \ge m$ alors l'ordre est de $O(n)$ et si $n < m$ alors l'ordre est de $O(m)$



<div id="5"></div>

## Exercice 5

![exercice 5](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo5.jpg)![exercice 5](https://data.cy.deltahmed.fr/DATA/TD6-Complexite_Informatique2p1s2/exo5_2.jpg){: .w-75 .shadow .rounded-10 }

### 1

+ a) $n$ additions pour incrémenté $i$(aucun nombre au carré sont inférieure a $100$)
+ b) $2n$ incrémentations de $i$ et addition (tout les nombre au carré sont inférieure a $100$)
+ c) en supposant que les valeurs de $T$ sont aléatoires équiprobables entre $1$ et $100$ inclus on a donc le nombre d'addition égal a $\frac{(n+2n)}{2} = \frac{3}{2}n $

### 2
 
+ il est evident que l'on vas faire $k$ fois la multiplication par exemple et donc que l'algorithme est en $O(k)$

+ Dans le deuxième cas on divise pour effectuer moins d'opérations en utilisant la propriété $n^{k}= \sqrt{(n^k)^2} = (n^2)^{k/2}$ sa complexité est donc logarithmique par rapport a $k$ et donc est en $O(\log k)$

Exercices : [1](#1) [2](#2) [3](#3) [4](#4) [5](#5) 
