---
title: DS3 2023 2024 EVAL MI 5 Correction
author: [MathisS]
date: 2024-05-26 01:00:00 +0100
categories: [PREING1 S2,Algebre2-DS]
tags: [PREING1 S2,Algebre2-DS,Mathis S.,DS3]
division_title : DS3
math: true
---

*Correction par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La plupart des résultats ont été vérifiés par l'outil informatique,
mais si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-info }

## Exercice 1 :

### 1\.

On dit qu'une famille de vecteurs est liée si l'un de ses vecteurs peut
s'exprimer comme combinaisons linéaires des autres. Dans le cas
contraire, il s'agit d'une famille de vecteurs linéairement
indépendants.

### 2\.

Soit $F$ et $G$ des sous-espaces vectoriels de dimension finie d'un
espace vectoriel.

D'après la formule de Grassmann,

$$\dim(F + G) = \dim(F) + \dim(G) - \dim(F \cap G)$$

### 3\.

Soit $E$ et $F$ des espaces vectoriels et $f$ une application linéaire
de $E$ dans $F$. Si $E$ est de dimension finie, d'après le théorème du
rang :

$$\dim(E) = \dim\left( \ker f \right) + \dim(Im\ f) = \dim\left( \ker f \right) + rg(f)$$

## Exercice 2 :

### 1\.

$$A = \begin{pmatrix}
1 & 3 & 5 & - 1 \\
2 & - 1 & - 3 & 4 \\
5 & 1 & - 1 & 7 \\
7 & 7 & 9 & 1
\end{pmatrix}$$

Echelonnons la matrice $A$ en lignes pour en déterminer son rang.

$$A\sim\begin{pmatrix}
1 & 3 & 5 & - 1 \\
0 & - 7 & - 13 & 6 \\
0 & - 14 & - 26 & 12 \\
0 & - 14 & - 26 & 8
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
1 & 3 & 5 & - 1 \\
0 & - 7 & - 13 & 6 \\
0 & 0 & 0 & 0 \\
0 & - 7 & - 13 & 4
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
1 & 3 & 5 & - 1 \\
0 & - 7 & - 13 & 6 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{pmatrix}$$

On trouve $rg(A) = 3$. ${Dim}\left( Im(f) \right) = 3$

Une base de $Im(f)$ est formée des vecteurs des colonnes de $A$
correspondant aux colonnes contenant les pivots dans la matrice
échelonnée en lignes.

Soit
$u_{1} = (1,2,5,7),u_{2} = (3, - 1,1,7),\ u_{3} = (5, - 3, - 1,9),\ u_{4} = ( - 1,4,7,1)$

Alors une base de $Im(f)$ est $\left( u_{1},u_{2},u_{4} \right)$

**Complément :** On peut établir la relation de liaison via la
matrice échelonnée : $u_{3} = xu_{1} + yu_{2}$ avec

$$\left\{ \begin{array}{r}
x + 3y = 5 \\
 - 7y = - 13
\end{array} \right.\ $$

$$u_{3} = \frac{13}{7}u_{2} - \frac{4}{7}u_{1}$$

### 2\.

D'après le théorème du rang,

$$\dim\left( \ker f \right) = \dim\left( \mathbb{R}^{4} \right) - rg(f) = 4 - 3 = 1$$

$\dim\left( \ker f \right) > 0$ donc $f$ n'est pas bijective, donc $A$
n'est pas inversible, donc $\det(A) = 0$

## Exercice 3 :

### 1\.

Soit $P = a + bX + cX^{2} \in \mathbb{R}_{2}\lbrack X\rbrack$

$P^{'} = b + 2cX$

$P^{''} = 2c$

$f(P) = 2c\left( X^{2} - 1 \right) + (2X + 1)(b + 2cX) = 2cX^{2} - 2c + 2bX + 4cX^{2} + b + 2cX$

$f(P) = (b - 2c) + (2b + 2c)X + 6cX^{2}$

$f(P) \in \mathbb{R}_{2}\lbrack X\rbrack$

Soit
$\phi\ :\mathbb{R}^{3} \rightarrow \mathbb{R}_{2}\lbrack X\rbrack,\ (a,b,c) \rightarrow a + bX + cX^{2}$

On a
$\phi^{- 1}\ :\mathbb{R}_{2}\lbrack X\rbrack \rightarrow \mathbb{R}^{3},\ a + bX + cX^{2} \rightarrow (a,b,c)$

Soit
$g\ :\mathbb{R}^{3} \rightarrow \mathbb{R}^{3},\ (a,b,c) \rightarrow (b - 2c,2b + 2c,6c)$

Alors $\phi,\phi^{- 1},g$ sont des applications linéaires

$f = \phi \circ g \circ \phi^{- 1}$ est une application linéaire.

$f$ est donc un endomorphisme de $\mathbb{R}_{2}\lbrack X\rbrack$

### 2\.

Soit $\mathcal{B =}\left( 1,X,X^{2} \right)$ la base canonique de
$\mathbb{R}_{2}\lbrack X\rbrack$

Dans ce cas,

$$A = \begin{pmatrix}
0 & 1 & - 2 \\
0 & 2 & 2 \\
0 & 0 & 6
\end{pmatrix}$$

### 3\.

Si on écrit $Mat_{\mathcal{B}}\left( \mathcal{C} \right)$ la matrice de
la famille $\mathcal{C}$ dans la base canonique $\mathcal{B}$

$$Mat_{\mathcal{B}}\left( \mathcal{C} \right) = \begin{pmatrix}
1 & 1 & 1 \\
0 & 2 & - 2 \\
0 & 0 & - 4
\end{pmatrix}$$

$\mathcal{C}$ est une base si et seulement si cette matrice est
inversible.

Or,
$\det\left( Mat_{\mathcal{B}}\left( \mathcal{C} \right) \right) = - 8$

Donc cette matrice est inversible, $\mathcal{C}$ est bien une base de
$\mathbb{R}_{2}\lbrack X\rbrack$

### 4\.

**Première méthode : On calcule**
$f\left( P_{1} \right),\ f\left( P_{2} \right),\ f\left( P_{3} \right)$
et on les exprime dans la base $\mathcal{C}$

$f\left( P_{1} \right) = f(1) = 0$

$f\left( P_{2} \right) = f(1 + 2X) = 2 + 4X = 2P_{2}$

$f\left( P_{3} \right) = f\left( 1 - 2X - 4X^{2} \right) = 6 - 12X - 24X^{2} = 6P_{3}$

Pour déterminer la matrice $D$, on met les vecteurs
$f\left( P_{1} \right),f\left( P_{2} \right),f\left( P_{3} \right)$ en
colonnes avec leurs vecteurs exprimés dans la base $\mathcal{C}$

$$D = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 6
\end{pmatrix}$$

**Deuxième méthode : On calcule les matrices de passage**

Soit $T$ la matrice de passage de la base $\mathcal{B}$ vers la base
$\mathcal{C}$

$$T = \begin{pmatrix}
1 & 1 & 1 \\
0 & 2 & - 2 \\
0 & 0 & - 4
\end{pmatrix}$$

Calculons $T^{- 1}$ en utilisant l'algorithme de Gauss-Jordan

$$\begin{pmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 2 & - 2 & 0 & 1 & 0 \\
0 & 0 & - 4 & 0 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & - 1 & 0 & \frac{1}{2} & 0 \\
0 & 0 & 1 & 0 & 0 & - \frac{1}{4}
\end{pmatrix}$$

$$\begin{pmatrix}
1 & 1 & 0 & 1 & 0 & \frac{1}{4} \\
0 & 1 & 0 & 0 & \frac{1}{2} & - \frac{1}{4} \\
0 & 0 & 1 & 0 & 0 & - \frac{1}{4}
\end{pmatrix}$$

$$\begin{pmatrix}
1 & 0 & 0 & 1 & - \frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & 0 & \frac{1}{2} & - \frac{1}{4} \\
0 & 0 & 1 & 0 & 0 & - \frac{1}{4}
\end{pmatrix}$$

$$T^{- 1} = \frac{1}{4}\begin{pmatrix}
4 & - 2 & 2 \\
0 & 2 & - 1 \\
0 & 0 & - 1
\end{pmatrix}$$

$$D = T^{- 1}AT = \frac{1}{4}\begin{pmatrix}
4 & - 2 & 2 \\
0 & 2 & - 1 \\
0 & 0 & - 1
\end{pmatrix}\begin{pmatrix}
0 & 1 & - 2 \\
0 & 2 & 2 \\
0 & 0 & 6
\end{pmatrix}\begin{pmatrix}
1 & 1 & 1 \\
0 & 2 & - 2 \\
0 & 0 & - 4
\end{pmatrix}$$

$$D = \frac{1}{4}\begin{pmatrix}
0 & 0 & 0 \\
0 & 4 & - 2 \\
0 & 0 & - 6
\end{pmatrix}\begin{pmatrix}
1 & 1 & 1 \\
0 & 2 & - 2 \\
0 & 0 & - 4
\end{pmatrix}$$

$$D = \frac{1}{4}\begin{pmatrix}
0 & 0 & 0 \\
0 & 8 & 0 \\
0 & 0 & 24
\end{pmatrix}$$

$$D = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 6
\end{pmatrix}$$

### 5\.

$$f\left( xP_{1} + yP_{2} + zP_{3} \right) = 0P_{1} + 2yP_{2} + 6zP_{3}$$

$$Im\ f = \left\{ Q \in \mathbb{R}_{2}\lbrack X\rbrack,\ \exists P \in \mathbb{R}_{2}\lbrack X\rbrack,\ Q = f(P) \right\}$$

$$Im\ f = \left\{ aP_{1} + bP_{2} + cP_{3} \in \mathbb{R}_{2}\lbrack X\rbrack,\ \exists\left( xP_{1} + yP_{2} + zP_{3} \right) \in \mathbb{R}_{2}\lbrack X\rbrack,aP_{1} + bP_{2} + cP_{3} = 2yP_{2} + 6zP_{3} \right\}$$

$$Im\ f = \left\{ 2yP_{2} + 6zP_{3},\ (y,z) \in \mathbb{R}^{2} \right\}$$

$$Im\ f = \left\{ y^{'}P_{2} + z^{'}P_{3},\ (y',z') \in \mathbb{R}^{2} \right\}$$

$$Im\ f = Vect\left\{ P_{2},P_{3} \right\}$$

### 6\.

Soit $P = aP_{1} + bP_{2} + cP_{3} \in \ker f$

$$f(P) = DP = 0$$

$$\left\{ \begin{array}{r}
2b = 0 \\
6c = 0
\end{array} \right\}$$

$$b = 0,\ c = 0$$

$$\ker f = \left\{ aP_{1},\ a \in \mathbb{R} \right\} = Vect\left\{ P_{1} \right\}$$

$\ker f$ et $Im\ f$ sont des sous-espaces vectoriels de
$\mathbb{R}_{2}\lbrack X\rbrack$

Hors $P_{1},P_{2},P_{3}$ est une famille libre donc

$$\ker f \cap Im\ f = 0$$

$$\ker f + Im\ f = Vect\left\{ P_{1} \right\} + Vect\left\{ P_{2},P_{3} \right\} = Vect\left\{ P_{1},P_{2},P_{3} \right\} = \mathbb{R}_{2}\lbrack X\rbrack$$

$\ker f$ et $Im\ f$ sont supplémentaires dans
$\mathbb{R}_{2}\lbrack X\rbrack$

## Exercice 4 :

$$A = \begin{pmatrix}
1 & 2 & m \\
1 & m & 2 \\
2 & 1 & 2
\end{pmatrix}$$

### 1\.

**Première méthode : Echelonnement**

$$\det(A) = \left| \begin{matrix}
1 & 2 & m \\
0 & m - 2 & 2 - m \\
0 & - 3 & 2 - 2m
\end{matrix} \right| = (m - 2)(2 - 2m) + 3(2 - m) = 2m - 2m^{2} - 4 + 4m + 6 - 3m = - 2m^{2} + 3m + 2$$

**Deuxième méthode : Développement selon la première colonne**

$$\det(A) = \left| \begin{matrix}
m & 2 \\
1 & 2
\end{matrix} \right| - \left| \begin{matrix}
2 & m \\
1 & 2
\end{matrix} \right| + 2\left| \begin{matrix}
2 & m \\
m & 2
\end{matrix} \right| = 2m - 2 - 4 + m + 8 - 2m^{2} = - 2m^{2} + 3m + 2$$

$$\det(A) = - 2m^{2} + 3m + 2$$

### 2\.

$A$ est inversible si et seulement si $\det(A) \neq 0$

Déterminons les valeurs de $m$ telles que $\det(A) = 0$

$$m = \frac{- 3 \pm \sqrt{9 + 16}}{- 4} = \frac{3 \pm 5}{4} = - \frac{1}{2}\ ou\ 2$$

$A$ est inversible si et seulement si $m \neq - \frac{1}{2}$ et
$m \neq 2$

### 3\.

$$A = \begin{pmatrix}
1 & 2 & 1 \\
1 & 1 & 2 \\
2 & 1 & 2
\end{pmatrix}$$

Utilisons l'algorithme de Gauss-Jordan

$$\begin{pmatrix}
1 & 2 & 1 & 1 & 0 & 0 \\
1 & 1 & 2 & 0 & 1 & 0 \\
2 & 1 & 2 & 0 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
1 & 2 & 1 & 1 & 0 & 0 \\
0 & - 1 & 1 & - 1 & 1 & 0 \\
0 & - 3 & 0 & - 2 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
1 & 2 & 1 & 1 & 0 & 0 \\
0 & - 1 & 1 & - 1 & 1 & 0 \\
0 & 0 & - 3 & 1 & - 3 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
3 & 6 & 3 & 3 & 0 & 0 \\
0 & - 3 & 3 & - 3 & 3 & 0 \\
0 & 0 & - 3 & 1 & - 3 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
3 & 6 & 0 & 4 & - 3 & 1 \\
0 & - 3 & 0 & - 2 & 0 & 1 \\
0 & 0 & - 3 & 1 & - 3 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
3 & 0 & 0 & 0 & - 3 & 3 \\
0 & - 3 & 0 & - 2 & 0 & 1 \\
0 & 0 & - 3 & 1 & - 3 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
3 & 0 & 0 & 0 & - 3 & 3 \\
0 & 3 & 0 & 2 & 0 & - 1 \\
0 & 0 & 3 & - 1 & 3 & - 1
\end{pmatrix}$$

$$A^{- 1} = \frac{1}{3}\begin{pmatrix}
0 & - 3 & 3 \\
2 & 0 & - 1 \\
 - 1 & 3 & - 1
\end{pmatrix}$$