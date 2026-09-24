---
title: DS2 2022 2023 V2
author: [MathisS]
date: 2024-04-02 01:00:00 +0100
categories: [PREING1 S2,Algebre2-DS]
tags: [PREING1 S2,Algebre2-DS,Mathis S.,DS2]
division_title : DS2
math: true
---

Correction proposée par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)

## Exercice 1 :

Dans cet exercice, on considère que $(x,y,z) \in \mathbb{R}^{3}$

### 1.

Pour montrer que $u_{1}$, $u_{3}$ et $u_{5}$ sont liés, on cherche une
solution non nulle de $xu_{1} + yu_{3} + zu_{5} = 0$

On peut le montrer en vérifiant que le rang de la matrice associée est
strictement inférieur à 3.

$$\begin{bmatrix}
1 & - 4 & - 3 \\
 - 2 & - 1 & 0 \\
3 & 3 & 1 \\
 - 1 & - 8 & - 5
\end{bmatrix}$$

$$L_{2} = L_{2} + 2L_{1},\ L_{3} = L_{3} - 3L_{1},\ L_{4} = L_{4} + L_{1}$$

$$\begin{bmatrix}
1 & - 4 & - 3 \\
0 & - 9 & - 6 \\
0 & 15 & 10 \\
0 & - 12 & - 8
\end{bmatrix}$$

$$L_{2} = \frac{L_{2}}{- 3},\ L_{3} = \frac{L_{3}}{5},\ L_{4} = \frac{L_{4}}{- 4}$$

$$\begin{bmatrix}
1 & - 4 & - 3 \\
0 & 3 & 2 \\
0 & 3 & 2 \\
0 & 3 & 2
\end{bmatrix}$$

$$L_{3} = L_{3} - L_{2},\ L_{4} = L_{4} - L_{2}$$

$$\begin{bmatrix}
1 & - 4 & - 3 \\
0 & 3 & 2 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}$$

+ Le rang de la matrice associée est $2 < 3$.

+ Il existe une solution non nulle de l'équation
+ \$$xu_{1} + yu_{3} + zu_{5} = 0$$

+ Les vecteurs $$u_{1},u_{3},u_{5}$$ sont donc liés.

### 2.

$u_{1}$ et $u_{2}$ ne sont pas colinéaires donc la famille
$$(u_{1},u_{2})$$ est libre.

Montrons que cette famille engendre $F$. Il suffit de vérifier que
$$u_{3},u_{4},u_{5} \in Vect\left( u_{1},u_{2} \right)$$

Vérifions donc, par la même méthode que la question précédente, que
($u_{1},u_{2},u_{3}$) et ($u_{1},u_{2},u_{4}$) sont des familles liées.

**Pour u3 :**

Ecrivons la matrice associée à l'équation $xu_{1} + yu_{2} + zu_{3} = 0$

$$\begin{bmatrix}
1 & 2 & - 4 \\
 - 2 & - 1 & - 1 \\
3 & 1 & 3 \\
 - 1 & 2 & - 8
\end{bmatrix}$$

$$L_{2} = L_{2} + 2L_{1},\ L_{3} = L_{3} - 3L_{1},\ L_{4} = L_{4} + L_{1}$$

$$\begin{bmatrix}
1 & 2 & - 4 \\
0 & 3 & - 9 \\
0 & - 5 & 15 \\
0 & 4 & - 12
\end{bmatrix}$$

$$L_{2} = \frac{L_{2}}{3},\ L_{3} = \frac{L_{3}}{- 5},\ L_{4} = \frac{L_{4}}{4}$$

$$\begin{bmatrix}
1 & 2 & - 4 \\
0 & 1 & - 3 \\
0 & 1 & - 3 \\
0 & 1 & - 3
\end{bmatrix} $$

$$ L_{3} = L_{3} - L_{2},\ L_{4} = L_{4} - L_{2}$$

$$\begin{bmatrix}
1 & 2 & - 4 \\
0 & 1 & - 3 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}$$

Pour l'équation $$xu_{1} + yu_{2} + zu_{3} = 0$$, le rang de la matrice
associée est $< 3$ donc il existe une solution non nulle. La famille
$$(u_{1},u_{2},u_{3})$$ est liée,
$$u_{3} \in Vect\left( u_{1},u_{2} \right)$$

**Pour u4 :**

Ecrivons la matrice associée à l'équation $xu_{1} + yu_{2} + zu_{4} = 0$

$$\begin{bmatrix}
1 & 2 & - 5 \\
 - 2 & - 1 & - 2 \\
3 & 1 & 5 \\
 - 1 & 2 & - 11
\end{bmatrix}$$

$$\begin{bmatrix}
1 & 2 & - 5 \\
0 & 3 & - 12 \\
0 & - 5 & 20 \\
0 & 4 & - 16
\end{bmatrix}\ L_{2} = L_{2} + 2L_{1},\ L_{3} = L_{3} - 3L_{1},\ L_{4} = L_{4} + L_{1}$$

$$\begin{bmatrix}
1 & 2 & - 5 \\
0 & 1 & - 4 \\
0 & 1 & - 4 \\
0 & 1 & - 4
\end{bmatrix}\ L_{2} = \frac{L_{2}}{3},\ L_{3} = \frac{L_{3}}{- 5},\ L_{4} = \frac{L_{4}}{4}$$

$$\begin{bmatrix}
1 & 2 & - 5 \\
0 & 1 & - 4 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}\ L_{3} = L_{3} - L_{2},\ L_{4} = L_{4} - L_{2}$$

De même, le rang de la matrice associée est $< 3$, donc
$u_{4} \in Vect\left( u_{1},u_{2} \right)$

Aussi, $$u_{5} \in Vect\left( u_{1},u_{3} \right)$$ et
$$u_{3} \in Vect\left( u_{1},u_{2} \right)$$ donc
$$u_{5} \in Vect\left( u_{1},u_{2} \right)$$

Ainsi, $$u_{3},u_{4},u_{5} \in Vect(u_{1},u_{2})$$ donc $$(u_{1},u_{2})$$
engendre $F$.

Ainsi, $\left( u_{1},u_{2} \right)$ est une base de $F$.

**Remarque :** On peut aussi montrer que le rang de la matrice
associée à $\left( u_{1},u_{2},u_{3},u_{4},u_{5} \right)$ est 2, donc
$\dim(F) = 2$. $$\left( u_{1},u_{2} \right)$$ est une famille libre de
deux vecteurs de $F$ donc elle engendre $F$.

## Exercice 2 :

### 1.

$$F = \left\{ (x,y,z,t) \in \mathbb{R}^{4},x + 2y + z + t = 0 \right\}$$

$$F = \left\{ (x,y,z,t) \in \mathbb{R}^{4},t = - x - 2y - z \right\}$$

$$F = \left\{ (x,y,z, - x - 2y - z),\ (x,y,z) \in \mathbb{R}^{3} \right\}$$

$$F = \left\{ (x,0,0, - x) + (0,y,0, - 2y) + (0,0,z, - z),\ (x,y,z) \in \mathbb{R}^{3} \right\}$$

$$F = \left\{ x(1,0,0, - 1) + y(0,1,0, - 2) + z(0,0,1, - 1),\ (x,y,z) \in \mathbb{R}^{3} \right\}$$

On pose $u_{1} = (1,0,0, - 1)$, $u_{2} = (0,1,0, - 2)$,
$u_{3} = (0,0,1, - 1)$

Alors $F = Vect\left( u_{1},u_{2},u_{3} \right)$

$F$ est donc un sous-espace vectoriel de $\mathbb{R}^{4}$, la famille
$$\left( u_{1},u_{2},u_{3} \right)$$ engendre $F$.

Montrons que la famille $$\left( u_{1},u_{2},u_{3} \right)$$ est libre. Si
on considère l'équation $$xu_{1} + yu_{2} + zu_{3} = 0$$, alors

$$ \left \{ \begin{matrix} 
    x = 0 \\
    y = 0 \\
    z = 0 \\
     - x - 2y - z = 0
\end{matrix} \right. $$


L'équation admet comme unique solution $(0,0,0)$ donc la famille
$$\left( u_{1},u_{2},u_{3} \right)$$ est libre.

$$\left( u_{1},u_{2},u_{3} \right)$$ est donc une base de $F$.

### 2.

$$G = \left\{ (x,y,z,t) \in \mathbb{R}^{4},x + 2y - z + t = 0\ \text{et}\ y - z = 0 \right\}$$

$$G = \left\{ (x,y,z,t) \in \mathbb{R}^{4},t = - x - 2y + z\ \text{et}\ y = z \right\}$$

$$G = \left\{ (x,y,z,t) \in \mathbb{R}^{4},t = - x - y\ \text{et}\ y = z \right\}$$

$$G = \left\{ (x,y,y, - x - y),\ (x,y) \in \mathbb{R}^{2} \right\}$$

$$G = \left\{ (x,0,0, - x) + (0,y,y, - y),\ (x,y) \in \mathbb{R}^{2} \right\}$$

$$G = \left\{ x(1,0,0, - 1) + y(0,1,1, - 1),\ (x,y) \in \mathbb{R}^{2} \right\}$$

On pose $v_{1} = (1,0,0, - 1)$ et $v_{2} = (0,1,1, - 1)$

Alors $G = Vect\left( v_{1},v_{2} \right)$

$G$ est donc un sous-espace vectoriel de $\mathbb{R}^{4}$, la famille
$$\left( v_{1},v_{2} \right)$$ engendre $G$. De plus, les vecteurs $v_{1}$
et $v_{2}$ ne sont pas colinéaires.

Ainsi, $$\left( v_{1},v_{2} \right)$$ est une base de $G$.

### 3.

$$F \cap G = \left\{ (x,y,z,t) \in \mathbb{R}^{4},\ x + 2y + z + t = 0\ \text{et}\ x + 2y - z + t = 0\ \text{et}\ y - z = 0 \right\}$$

Soit $w(x,y,z,t) \in F \cap G$

Alors $w$ vérifie le système :

$$\left \{ \begin{matrix}
    x + 2y + z + t = 0 \\
    x + 2y - z + t = 0 \\
    y = z \\
\end{matrix} \right. $$

$$E_{2} = E_{2} - E_{1}$$

$$\left \{ \begin{matrix} 
    x + 2y + z + t = 0 \\
    - 2z = 0 \\
    y = z
\end{matrix} \right. $$

$$\left \{ \begin{matrix} 
t = - x \\
y = z = 0
\end{matrix} \right. $$

$$F \cap G = \left\{ (x,0,0, - x),\ x\mathbb{\in R} \right\}$$

$$F \cap G = \left\{ x(1,0,0, - 1),\ x\mathbb{\in R} \right\}$$

$$F \cap G = Vect\left( (1,0,0, - 1) \right)$$

$F \cap G$ est un sous-espace vectoriel de $\mathbb{R}^{4}$. Une base de
$F \cap G$ est $\left\{ (1,0,0, - 1) \right\}$.

## Exercice 3 :

### 1.a.

Pour montrer que $( \mathbb{R}^{2}, + ,. )$ est un espace
vectoriel, la loi externe doit vérifier les propriétés suivantes,
$\forall(\lambda,\mu) \in \mathbb{R}^{2},\ \forall(x,y),( x^{'},y^{'} ) \in \mathbb{R}^{2}\ $:

-   \$$1.(x,y) = (x,y)$$

-   \$$\lambda.\left( \mu.(x,y) \right) = (\lambda\mu).(x,y)$$

-   \$$\lambda.\left( x + x^{'},y + y^{'} \right) = \lambda.(x,y) + \lambda.\left( x^{'},y^{'} \right)$$

-   \$$(\lambda + \mu).(x,y) = \lambda.(x,y) + \mu.(x,y)$$

### 1.b.

Montrons que la loi externe ne vérifie par le quatrième point.
$$\forall(\lambda,\mu) \in \mathbb{R}^{2},\ \forall(x,y) \in \mathbb{R}^{2}\ $$:

$$(\lambda + \mu).(x,y) = \left( (\lambda + \mu)x,y \right)$$

$$\lambda.(x,y) + \mu.(x,y) = (\lambda x,y) + (\mu x,y) = \left( (\lambda + \mu)x,2y \right)$$

Pour $y \neq 0$, $(\lambda + \mu).(x,y) \neq \lambda.(x,y) + \mu.(x,y)$

$$\left( \mathbb{R}^{2}, + ,. \right)$$ n'est pas un espace vectoriel.

### 2.

**Rappel :** L'ensemble des applications de $E$ vers $F$ est
noté $\mathcal{F}(E,F)$. D'après le cours, pour tout ensemble $A$,
$\mathcal{F}\left( A\mathbb{,\ R} \right)$ est un espace vectoriel.

Soit $F$ l'ensemble des fonctions de $\lbrack 0;1\rbrack$ dans
$\mathbb{R}$ vérifiant $f(1) = 2f(0)$

$$F = \{ f\mathcal{\in F}\left( \lbrack 0;1\rbrack,\ f(1) = 2f(0) \right\}$$

Pour montrer que $F$ est un espace vectoriel, montrons que c'est un sous
espace-vectoriel de l'espace vectoriel de référence
$$\mathcal{F}\left( \lbrack 0;1\rbrack\mathbb{,\ R} \right)$$

Nous devons vérifier 3 conditions :
$F\mathcal{\subset F}\left( \lbrack 0;1\rbrack\mathbb{,R} \right)$,
l'application nulle est incluse dans $F$ et

$$\forall\lambda,\mu\mathbb{\in R,\ \forall}f,g \in F,\ \lambda f + \mu g \in F$$

-   $F$ est incluse dans
    $\mathcal{F}\left( \lbrack 0;1\rbrack\mathbb{,R} \right)$ par
    définition

-   Si $f$ est la fonction nulle, alors $f(1) = 2f(0) = 0$ donc
    $f \in F$

-   \$$\forall\lambda,\mu\mathbb{\in R,\ \forall}f,g \in F,$$

$$(\lambda f + \mu g)(1) = \lambda f(1) + \mu g(1) = 2\lambda f(0) + 2\mu g(0) = 2\left( \lambda f(0) + \mu g(0) \right) = 2(\lambda f + \mu g)(0)$$

Donc $\lambda f + \mu g \in F$

$F$ est bien un sous espace-vectoriel de
$\mathcal{F}\left( \lbrack 0;1\rbrack\mathbb{,R} \right)$. $F$ est donc
un espace vectoriel.

## Exercice 4 :

### 1.a.

On remarque aisément que $$u_{3} = 2u_{1} - u_{2}$$

(Si on ne le voit pas on peut toujours résoudre un système simple).

### 1.b.

De même, on remarque que $$u_{4} = u_{1} - u_{2}$$

Ainsi, $$u_{1} = u_{3} - u_{4}$ et $u_{2} = u_{3} - 2u_{4}$$

On a $$u_{3},u_{4} \in Vect\left( u_{1},u_{2} \right)$$ donc
$$Vect\left( u_{3},u_{4} \right) \subset Vect\left( u_{1},u_{2} \right)$$
donc $G \subset F$

On a $u_{1},u_{2} \in Vect\left( u_{3},u_{4} \right)$ donc
$Vect\left( u_{1},u_{2} \right) \subset Vect\left( u_{3},u_{4} \right)$
donc $F \subset G$

Donc $F = G$

### 2.

On considère la famille $$\left( e_{1},u_{1},u_{2} \right)$$. Cette
famille est une base de $\mathbb{R}^{3}$ si et seulement si le rang de
la matrice homogène associée à $$\left( e_{1},u_{1},u_{2} \right)$$ est 3.

$$\begin{bmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
0 & 0 & - 2
\end{bmatrix}$$

Il apparaît immédiatement que le rang de cette matrice est 3. Ainsi,
$$\left( e_{1},u_{1},u_{2} \right)$$ est une base de $\mathbb{R}^{3}$.

