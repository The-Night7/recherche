---
title: DS3 2019 2020 Correction (1, 2 et 3p1)
author: [MathisS]
date: 2024-06-02 01:00:00 +0100
categories: [PREING1 S2,Algebre2-DS]
tags: [PREING1 S2,Algebre2-DS,Mathis S.,DS3]
division_title : DS3
math: true
---



*Correction proposée par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La correction a été faite dans la précipitation, il est donc normal que la correction ne soit pas ultra détaillée, si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-warning }

## Exercice 1 :

### 1\.

$$M_{a} = \begin{pmatrix}
1 & a & 1 & 0 \\
a & a & 0 & 0 \\
0 & 1 & 1 & 1 \\
a & a & 0 & 1
\end{pmatrix}$$

Si $a = 0$, la $2^{eme}$ ligne est nulle. ${Det}\left( M_{0} \right) = 0$

Sinon,

$$\det\left( M_{a} \right) = \left| \begin{matrix}
1 & a & 1 & 0 \\
a & a & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1
\end{matrix} \right|$$

$$\det\left( M_{a} \right) = - \left| \begin{matrix}
1 & a & 1 \\
a & a & 0 \\
0 & 1 & 1
\end{matrix} \right|$$

$$\det\left( M_{a} \right) = - \left( - \left| \begin{matrix}
1 & 1 \\
a & 0
\end{matrix} \right| + \left| \begin{matrix}
1 & a \\
a & a
\end{matrix} \right| \right) = - \left( a + a - a^{2} \right) = - \left( 2a - a^{2} \right) = - a(2 - a)$$

### 2\.

Si $\det\left( M_{a} \right) \neq 0$,

$a \notin \{ 0,2  \},\ rg ( M_{a} ) = 4$

Si $a = 2$

$$M\sim\begin{pmatrix}
1 & 2 & 1 & 0 \\
2 & 2 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

$$M\sim\begin{pmatrix}
2 & 4 & 2 & 0 \\
2 & 2 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

$$M\sim\begin{pmatrix}
2 & 4 & 2 & 0 \\
0 & - 2 & - 2 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

$$M\sim\begin{pmatrix}
2 & 4 & 2 & 0 \\
0 & - 2 & - 2 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

$$M\sim\begin{pmatrix}
2 & 4 & 2 & 0 \\
0 & - 2 & - 2 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

$$rg\left( M_{2} \right) = 3$$

## Exercice 2 :

### 1\.

$$A = \begin{pmatrix}
 - 1 & 2 & - 1 & - 1 \\
 - 1 & 2 & - 1 & - 1 \\
 - 1 & 1 & 0 & 0 \\
0 & 1 & - 1 & - 1
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
1 & - 2 & 1 & 1 \\
 - 1 & 2 & - 1 & - 1 \\
 - 1 & 1 & 0 & 0 \\
0 & 1 & - 1 & - 1
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
1 & - 2 & 1 & 1 \\
0 & 0 & 0 & 0 \\
0 & - 1 & 1 & 1 \\
0 & 1 & - 1 & - 1
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
1 & - 2 & 1 & 1 \\
0 & 1 & - 1 & - 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
1 & 0 & - 1 & - 1 \\
0 & 1 & - 1 & - 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}$$

$$\ker(f) = Vect\left\{ (1,1,1,0),(1,1,0,1) \right\}$$

$$Im(f) = Vect\left\{ (1,1,1,0),(2,2,1,1) \right\}$$

$$u_{1} = (1,1,1,0),u2 ≔ (1,1,0,1),u3 = (2,2,1,1)$$

### 3\.

On procède par double inclusion

Montrons $Im\ f \subset \ker f$

$$u_{3} = u_{1} + u_{2},$$

Par combinaisons linéaires de combinaisons linéaires, tout vecteur de
$Im\ f$ peut s'écrire comme combinaisons linéaires de vecteurs de la
base de $\ker f$

Montrons $\ker f \subset Im\ f$

$$u_{2} = u_{3} - u_{1}$$

Par combinaisons linéaires de combinaisons linéaires, tout vecteur de
$Ker\ f$ peut s'écrire comme combinaisons linéaires de vecteurs de la
base de ${Im}f$

### 4\.

Trouvons une telle base $\left( v_{1},v_{2},v_{3},v_{4} \right)$

$$f\left( v_{1} \right) = f\left( v_{2} \right) = 0$$

Donc $v_{1},v_{2} \in \ker f$

Posons $v_{1} = u_{1}$ et $v_{2} = u_{2}$

$$f\left( v_{3} \right) = v_{1} = u_{1} = (1,1,1,0)$$

$$f\left( v_{4} \right) = v_{2} = u_{2} = (1,1,0,1)$$

$$v_{3} = ( - 1,0,0,0),\ f\left( v_{3} \right) = u_{1}$$

$$v_{4} = (0,0, - 1,0),\ f\left( v_{4} \right) = u_{2}$$

$$v_{1} = (1,1,1,0)$$

$$v_{2} = (1,1,0,1)$$

$$v_{3} = ( - 1,0,0,0)$$

$$v_{4} = (0,0, - 1,0)$$

### 5\.

Dans la base $\left( v_{1},v_{2},v_{3},v_{4} \right)$, la matrice de
l'endomorphisme $f \circ f$ est donnée par

$$\begin{pmatrix}
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}^{2} = 0$$

$$f \circ f = 0$$

### 6\.

On procède par double implication.

$\Longrightarrow$ :

Supposons que $\ker g = Im\ g$

Montrons que $g \circ g = 0$ et $n = 2\ rg(g)$

Soit $u \in E,\ v = g(u),\ w = (g \circ g)(u)$

$v \in Im\ g$ donc $v \in \ker g$ donc $w = 0\forall u \in E$

Donc $g \circ g = 0$

On sait que $\ker g \oplus Im\ g = E$

D'après la formule de Grassmann, $\dim\left( \ker g \right) + rg(g) = n$

Or $\ker g = Im\ g$

$\dim\left( \ker g \right) = rg(g)$

$2\ rg(g) = n$

$\Longleftarrow$ :

Supposons que $g \circ g = 0$ et $n = 2\ rg(g)$

Montrons que $\ker g = Im\ g$

Soit $u \in E,\ v = g(u),\ w = (g \circ g)(u)$

On sait que $\ker g \oplus Im\ g = E$

D'après la formule de Grassmann, $\dim\left( \ker g \right) + rg(g) = n$

Or $n = 2rg(g)$

Donc $\dim\left( \ker g \right) = rg(g) = \dim(Im\ g)$

$Im\ g \subset \ker(g)$

Pourquoi ? $v \in Im\ g,\ or\ g(v) = 0,\ donc\ v \in \ker g$

$Im\ g \subset \ker g$ et $\dim(Im\ g) = \dim\left( \ker g \right)$ donc
$\ker g = Im\ g$

CQFD.

## Exercice 3 : Partie 1.

### 

### 1\.

Soit $A$ la matrice de $\varphi$ dans la base canonique.

$$A = \begin{pmatrix}
3 & 4 & - 4 \\
2 & 2 & - 1 \\
2 & 3 & - 2
\end{pmatrix}$$

### 2\.

$$A\sim\begin{pmatrix}
6 & 8 & - 8 \\
6 & 6 & - 3 \\
6 & 9 & - 6
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
6 & 8 & - 8 \\
0 & - 2 & 5 \\
0 & 1 & 2
\end{pmatrix}$$

$$A\sim\begin{pmatrix}
6 & 8 & - 8 \\
0 & - 2 & 5 \\
0 & 0 & 1
\end{pmatrix}$$

$rg(A) = 3,\ A$ est inversible, $\varphi$ est bijective.

### 3.a.

Soit $B$ la matrice de $\varphi - 3Id_{\mathbb{R}^{3}}$

$$B = \begin{pmatrix}
0 & 4 & - 4 \\
2 & - 1 & - 1 \\
2 & 3 & - 5
\end{pmatrix}$$

$$B\sim\begin{pmatrix}
2 & - 1 & - 1 \\
2 & 3 & - 5 \\
0 & 4 & - 4
\end{pmatrix}$$

$$B\sim\begin{pmatrix}
2 & - 1 & - 1 \\
0 & 4 & - 4 \\
0 & 4 & - 4
\end{pmatrix}$$

$$B\sim\begin{pmatrix}
2 & - 1 & - 1 \\
0 & 1 & - 1 \\
0 & 0 & 0
\end{pmatrix}$$

$$B\sim\begin{pmatrix}
2 & 0 & - 2 \\
0 & 1 & - 1 \\
0 & 0 & 0
\end{pmatrix}$$

$$B\sim\begin{pmatrix}
1 & 0 & - 1 \\
0 & 1 & - 1 \\
0 & 0 & 0
\end{pmatrix}$$

$$(\varphi - 3Id)(x,y,z) = 0 \Longleftrightarrow (x,y,z) = (z,z,z)$$

$$Ker(\varphi - 3Id) = Vect\left\{ (1,1,1) \right\}$$

### 3.b.

Soit $u \in Ker(\varphi - 3Id)$

$$f(u) = 0 \in Ker(\varphi - 3Id)$$

Donc $Ker(\varphi - 3Id)$ est stable par $\varphi$

### 4.a.

$$F = \left\{ (x,y,x + y),\ (x,y) \in \mathbb{R}^{2} \right\}$$

$$F = \left\{ x(1,0,1) + y(0,1,1),\ (x,y) \in \mathbb{R}^{2} \right\}$$

$$F = Vect\left\{ (1,0,1),(0,1,1) \right\}$$

$F$ est un sev de $\mathbb{R}^{3}$

Une base de $F$ est $\left\{ (1,0,1),(0,1,1) \right\}$

Soit $v = (1,0,1),w = (0,1,1)$

### 4.b.

Soit $u = \lambda v + \mu w \in F$

$$\varphi(u) = \varphi(\lambda v + \mu w) = \lambda\varphi(v) + \mu\varphi(w)$$

$$\varphi(v) = \varphi(1,0,1) = ( - 1,1,0) = w - v$$

$$\varphi(w) = \varphi(0,1,1) = (0,1,1) = w$$

$$\phi(u) = \lambda(w - v) + \mu w = - \lambda v + (\lambda + \mu)w \in F$$

Donc $F$ est stable par $\varphi$

### 4.c.

$$\dim(F) + \dim\left( Ker(\varphi - 3Id) \right) = 2 + 1 = 3 = \dim\left( \mathbb{R}^{3} \right)$$

Montrons alors que $F + Ker(\varphi - 3Id) = \mathbb{R}^{3}$, il suffit
de montrer que $\left( v,w,(1,1,1) \right)$ est une famille génératrice,
donc que le rang de la matrice de cette famille est 3.

$$\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix}\sim\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
0 & 1 & 0
\end{pmatrix}\sim\begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
0 & 0 & - 1
\end{pmatrix}$$

Le rang de la matrice de cette faille est bien 3, alors on a bien
$F \oplus Ker(\varphi - 3Id) = \mathbb{R}^{3}$