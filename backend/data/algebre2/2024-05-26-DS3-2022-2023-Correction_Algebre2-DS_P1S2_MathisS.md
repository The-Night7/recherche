---
title: DS3 2022 2023 Correction
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

$$\ker g = \left\{ \lambda(1,1,1)\  \right|\ \forall\lambda \in \mathbb{R\}}$$

Soit $w = (1,1,1)$

$\ker g = Vect\left( (w) \right)$

Alors $(w)$ est une base de $\ker g$ et $\dim\left( \ker g \right) = 1$

### 2\.

La famille $\left( w,(1,0,0),(0,0,1) \right)$ est une famille libre
composée de 3 vecteurs, elle engendre donc $\mathbb{R}^{3}$

Ainsi, $V = Vect\left( (1,0,0),(0,0,1) \right)$ est un supplémentaire de
$\ker g$ dans $\mathbb{R}^{3}$

### 3\.

$(1,1,1) \in \ker g$ donc $g(1,1,1) = 0$

$g(1,1,1) = g(1,0,0) + g(0,1,0) + g(0,0,1)\ \text{car}\ g\ \text{est linéair}\text{e}$

$g(1,0,0) + g(0,1,0) + g(0,0,1) = 0$

$(3,1,0) + (1,2,0) = - g(0,1,0)$

$- (4,3,0) = g(0,1,0)$

$g(0,1,0) = ( - 4, - 3,0)$

### 4\.

$$M_{\mathcal{B}_{c}}(g) = \begin{pmatrix}
3 & - 4 & 1 \\
1 & - 3 & 2 \\
0 & 0 & 0
\end{pmatrix}$$

### 5\.

$$g(x,y,z) = (3x - 4y + z,x - 3y + 2z,0)$$

## Exercice 2 :

### 1\.

$$M_{\mathcal{B}_{c}}(f) = \begin{pmatrix}
2 & 0 & 0 \\
0 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix}$$

### 2\.

On développe selon la première ligne.

$$\det(A) = 2\left| \begin{matrix}
1 & 1 \\
1 & 1
\end{matrix} \right| = 0$$

La matrice $A$ n'est pas inversible donc $f$ n'est pas un isomorphisme
de $\mathbb{R}^{3}$.

### 3\.

Si $(x,y,z) \in \ker f$,

$$\left\{ \begin{array}{r}
2x = 0 \\
y + z = 0 \\
x + y + z = 0
\end{array} \right\}$$

$$\left\{ \begin{array}{r}
x = 0 \\
z = - y
\end{array} \right\}$$

$$\ker f = \left\{ (0,y, - y),\ (x,y,z) \in \mathbb{R}^{3} \right\} = \left\{ y(0,1, - 1),\ (x,y,z) \in \mathbb{R}^{3} \right\} = Vect\left( (0,1, - 1) \right)$$

Posons $w = (0,1, - 1)$

Alors $(w)$ est une base de $\ker(f)$

$\dim\left( \ker f \right) = 1$

D'après le théorème du rang,
$rg(f) = \dim\left( \mathbb{R}^{3} \right) - \dim\left( \ker f \right) = 2$

Pour trouver une base de $Im(f)$, nous devons extraire deux vecteurs
libres des colonnes de $M_{\mathcal{B}_{c}}(f)$.

On pose $u = (2,0,1) \in Im(f)$ et $v = (0,1,1) \in Im(f)$. La famille
$(u,v)$ est libre, or $rg(f) = 2$, donc elle engendre $Im(f)$.

Alors $(u,v)$ est une base de $Im(f)$.

### 4\.

Soit $\mathcal{F}$ la famille $(u,v,w)$

$$Mat_{\mathcal{B}_{c}}\left( \mathcal{F} \right) = \begin{pmatrix}
2 & 0 & 0 \\
0 & 1 & 1 \\
1 & 1 & - 1
\end{pmatrix}\sim_{L}\begin{pmatrix}
2 & 0 & 0 \\
0 & 1 & 1 \\
0 & 1 & - 1
\end{pmatrix}\sim_{L}\begin{pmatrix}
2 & 0 & 0 \\
0 & 1 & 1 \\
0 & 0 & - 2
\end{pmatrix}$$

$$rg\left( Mat_{\mathcal{B}_{c}}\left( \mathcal{F} \right) \right) = 3,Mat_{\mathcal{B}_{c}}\left( \mathcal{F} \right)$$
est inversible donc $\mathcal{F}$ est libre.

$\mathcal{F}$ est une famille libre de 3 vecteurs de $\mathbb{R}^{3}$
donc elle engendre $\mathbb{R}^{3}$

Ainsi $\ker(f) + Im(f) = \mathbb{R}^{3}$

Or
$\dim\left( \ker(f) \right) + \dim\left( Im(f) \right) = \dim\left( \mathbb{R}^{3} \right)$

Donc $\mathbb{R}^{3} = \ker(f) \oplus Im(f)$

### 5a.

$$Mat_{\mathcal{B}_{c}}\left( \mathcal{B} \right) = \begin{pmatrix}
0 & 0 & 2 \\
 - 1 & 1 & - 1 \\
1 & 1 & 0
\end{pmatrix}\sim_{L}\begin{pmatrix}
1 & 1 & 0 \\
 - 1 & 1 & - 1 \\
0 & 0 & 2
\end{pmatrix}\sim_{L}\begin{pmatrix}
1 & 1 & 0 \\
0 & 2 & - 1 \\
0 & 0 & 2
\end{pmatrix}$$

$$rg\left( Mat_{\mathcal{B}_{c}}\left( \mathcal{B} \right) \right) = 3$$

Donc $\mathcal{B}$ est une base de $\mathbb{R}^{3}$

### 5b.

$$f\left( v_{1} \right) = f(0, - 1,1) = 0$$

$$f\left( v_{2} \right) = (0,2,2) = 2v_{2}$$

$$f\left( v_{3} \right) = (4, - 1,1) = (4, - 2,0) + (0,1,1) = v2 + 2v_{3}$$

$$T = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2 & 1 \\
0 & 0 & 2
\end{pmatrix}$$

### 5c.

La propriété est vérifiée pour $n = 1$

Supposons qu'elle est vraie pour $k \geq 1$ et montrons qu'elle est
vraie pour $k + 1$

$$T^{k + 1} = T\left( T^{k} \right) = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2 & 1 \\
0 & 0 & 2
\end{pmatrix}\begin{pmatrix}
0 & 0 & 0 \\
0 & 2^{k} & k2^{k - 1} \\
0 & 0 & 2^{k}
\end{pmatrix} = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2 \times 2^{k} & 2\left( k2^{k - 1} \right) + 2^{k} \\
0 & 0 & 2 \times 2^{k}
\end{pmatrix} = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2^{k + 1} & (k + 1)2^{k} \\
0 & 0 & 2^{k + 1}
\end{pmatrix}$$

Par récurrence, pour tout $n \in \mathbb{N}^{*}$,

$$T^{n} = \begin{pmatrix}
0 & 0 & 0 \\
0 & 2^{n} & n2^{n - 1} \\
0 & 0 & 2^{n}
\end{pmatrix}$$

### 6a.

$$P = \begin{pmatrix}
0 & 0 & 2 \\
 - 1 & 1 & - 1 \\
1 & 1 & 0
\end{pmatrix}$$

$$e_{3} = \frac{v_{1} + v_{2}}{2}$$

$$e_{2} = \frac{v_{2} - v_{1}}{2}$$

$$e_{1} = \frac{v_{3}}{2} + \frac{e_{2}}{2} = \frac{v_{3}}{2} + \frac{v_{2}}{4} - \frac{v_{1}}{4}$$

$$P^{- 1} = \begin{pmatrix}
 - \frac{1}{4} & - \frac{1}{2} & \frac{1}{2} \\
\frac{1}{4} & \frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & 0 & 0
\end{pmatrix}$$

### 6b.

$$A = PTP^{- 1}$$

### 6c.

Utilisons l'algorithme de Gauss-Jordan.

$$\begin{pmatrix}
0 & 0 & 2 & 1 & 0 & 0 \\
 - 1 & 1 & - 1 & 0 & 1 & 0 \\
1 & 1 & 0 & 0 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
1 & 1 & 0 & 0 & 0 & 1 \\
 - 1 & 1 & - 1 & 0 & 1 & 0 \\
0 & 0 & 2 & 1 & 0 & 0
\end{pmatrix}\ L_{1} \leftrightarrow L_{3}$$

$$\begin{pmatrix}
1 & 1 & 0 & 0 & 0 & 1 \\
0 & 2 & - 1 & 0 & 1 & 1 \\
0 & 0 & 2 & 1 & 0 & 0
\end{pmatrix}\ L_{2} \leftarrow L_{2} + L_{1}$$

$$\begin{pmatrix}
1 & 1 & 0 & 0 & 0 & 1 \\
0 & 4 & - 2 & 0 & 2 & 2 \\
0 & 0 & 2 & 1 & 0 & 0
\end{pmatrix}\ L_{2} \leftarrow 2L_{2}$$

$$\begin{pmatrix}
4 & 4 & 0 & 0 & 0 & 4 \\
0 & 4 & 0 & 1 & 2 & 2 \\
0 & 0 & 2 & 1 & 0 & 0
\end{pmatrix}\ L_{1} \leftarrow 4L_{1},\ L_{2} \leftarrow L_{2} + L_{3}$$

$$\begin{pmatrix}
4 & 0 & 0 & - 1 & - 2 & 2 \\
0 & 4 & 0 & 1 & 2 & 2 \\
0 & 0 & 2 & 1 & 0 & 0
\end{pmatrix}\ L_{1} \leftarrow L_{1} - L_{2}$$

$$\begin{pmatrix}
1 & 0 & 0 & - \frac{1}{4} & - \frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 & \frac{1}{4} & \frac{1}{2} & \frac{1}{2} \\
0 & 0 & 1 & \frac{1}{2} & 0 & 0
\end{pmatrix}\ L_{1} \leftarrow \frac{L_{1}}{4},\ L_{2} \leftarrow \frac{L_{2}}{4},\ L_{3} \leftarrow \frac{L_{3}}{2}$$

$$P^{- 1} = \begin{pmatrix}
 - \frac{1}{4} & - \frac{1}{2} & \frac{1}{2} \\
\frac{1}{4} & \frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & 0 & 0
\end{pmatrix}$$