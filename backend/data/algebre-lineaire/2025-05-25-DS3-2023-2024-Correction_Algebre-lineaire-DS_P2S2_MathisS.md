---
title: DS3 2023 2024 Correction
author: [MathisS]
date: 2025-05-25 01:02:39 +0200
categories: [PREING2 S2,Algebre-lineaire-DS]
tags: [PREING2 S2,Algebre-lineaire-DS,DS3,Mathis S.,Correction]
division_title : DS3
math: true
---

# **Exercice 1 :**

## 1\.

$$X'(t) = AX(t) + B(t)$$

Avec 
$$X(t) = \begin{bmatrix}
x_{1}(t) \\
x_{2}(t)
\end{bmatrix},\ A = \begin{bmatrix}
0 & 2 \\ - 2 & 4
\end{bmatrix},\ B(t) = \begin{bmatrix} - 3e^{t} \\
2e^{t}
\end{bmatrix}$$

## 2\.

**Polynôme caractéristique** $P_{A}\ $**:**

$$P_{A}(\lambda) = \det\left( A - \lambda I_{2} \right) = \left\vert  \begin{matrix} - \lambda & 2 \\  - 2 & 4 - \lambda
\end{matrix} \right\vert $$

$$C_{1} \leftarrow C_{1} + C_{2}$$

$$\Leftrightarrow P_{A}(\lambda) = \left\vert  \begin{matrix}
2 - \lambda & 2 \\
2 - \lambda & 4 - \lambda
\end{matrix} \right\vert \ \begin{matrix}
\  \\
L_{2} \leftarrow L_{2} - L_{1}
\end{matrix}$$

$$\Leftrightarrow P_{A}(\lambda) = \left\vert  \begin{matrix}
2 - \lambda & 2 \\
0 & 2 - \lambda
\end{matrix} \right\vert $$

$$\Leftrightarrow P_{A}(\lambda) = (2 - \lambda)^{2}$$

$$\Leftrightarrow Sp(A) = \left\lbrack  2 \right\rbrack $$

**Sous-espace propre** $E_{2}\ $**:**

$$E_{2} = {Ker}\left( A - 2I_{2} \right)$$

Soit 
$$K = \begin{bmatrix}
a \\
b
\end{bmatrix} \in \mathcal{M}_{2,1}\left( \mathbb{R} \right)$$

$$K \in E_{2} \Leftrightarrow \left( A - 2I_{2} \right)K = 0_{2,1} \Leftrightarrow \begin{bmatrix} - 2 & 2 \\ - 2 & 2
\end{bmatrix}\begin{bmatrix}
a \\
b
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix}$$

$$\Leftrightarrow - 2a + 2b = 0$$

$$\Leftrightarrow a = b$$

$$\Leftrightarrow K = a\begin{bmatrix}
1 \\
1
\end{bmatrix},\ a \in \mathbb{R}$$

Donc $E_{2} = {Vect}\left( V_{1} \right)$ avec 

$$V_{1} = \begin{bmatrix}
1 \\
1
\end{bmatrix}$$

**Trigonalisation**

On cherche une matrice 

$$T \in \mathcal{M}_{2}\left( \mathbb{R} \right)$$,
et une matrice $$P \in GL_{2}\left( \mathbb{R} \right)$$, telles que
$A = PTP^{- 1}$, avec $T$ sous la forme :

$$T = \begin{bmatrix}
2 & c \\
0 & 2
\end{bmatrix},\ c \in \mathbb{R}$$

$T$ est la matrice de $A$ dans la base $\left( V_{1},V_{2} \right)$

On cherche $V_{2}$ tel que
$AV_{2} = cV_{1} + 2V_{2} \Leftrightarrow \left( A - 2I_{2} \right)V_{2} = cV_{1}$

Soit 
$$K = \begin{bmatrix}
a \\
b
\end{bmatrix} \in \mathcal{M}_{2,1}\left( \mathbb{R} \right)$$

$$\left( A - 2I_{2} \right)K = cV_{1} \Leftrightarrow \begin{bmatrix} - 2 & 2 \\ - 2 & 2
\end{bmatrix}\begin{bmatrix}
a \\
b
\end{bmatrix} = \begin{bmatrix}
c \\
c
\end{bmatrix}$$

$$\Leftrightarrow - 2a + 2b = c$$

$$\Leftrightarrow b = \frac{c}{2} + a$$

$$\Leftrightarrow K = a\begin{bmatrix}
1 \\
1
\end{bmatrix} + \frac{c}{2}\begin{bmatrix}
0 \\
1
\end{bmatrix},\ a \in \mathbb{R}$$

On prend $c = 2$ et 
$$V_{2} = \begin{bmatrix}
0 \\
1
\end{bmatrix}$$

On a donc :

$$T = \begin{bmatrix}
2 & 2 \\
0 & 2
\end{bmatrix},\ P = \begin{bmatrix}
V_{1} & V_{2}
\end{bmatrix} = \begin{bmatrix}
1 & 0 \\
1 & 1
\end{bmatrix}$$

$P$ est inversible car $\det(P) = 1 \neq 0$

Et $A = PTP^{- 1}$.

## 3\.

**Résolution du système par changement de variable**

$$X'(t) = AX(t) + B(t)$$

$$\Leftrightarrow X'(t) = PTP^{- 1}X(t) + B(t)$$

$$\Leftrightarrow P^{- 1}X'(t) = TP^{- 1}X(t) + P^{- 1}B(t)$$

**Calcul de** $P^{- 1}B(t)\ $**:**

$$P^{- 1} = \frac{1}{\det(P)}\begin{bmatrix}
1 & 0 \\
- 1 & 1
\end{bmatrix} = \begin{bmatrix}
1 & 0 \\
- 1 & 1
\end{bmatrix}$$

$$P^{- 1}B(t) = \begin{bmatrix}
1 & 0 \\
- 1 & 1
\end{bmatrix}\begin{bmatrix}
- 3e^{t} \\
2e^{t}
\end{bmatrix} = \begin{bmatrix}
- 3e^{t} \\
5e^{t}
\end{bmatrix}$$

On pose le changement de variable 

$$U(t) = \begin{bmatrix}
u_{1}(t) \\
u_{2}(t)
\end{bmatrix} = P^{- 1}X(t)$$

$$(S) \Leftrightarrow U'(t) = TU(t) + P^{- 1}B(t)$$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
u_{1}'(t) = 2u_{1}(t) + 2u_{2}(t) - 3e^{t} \\
u_{2}'(t) = 2u_{2}(t) + 5e^{t}
\end{array} \right. $$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
u_{1}'(t) = 2u_{1}(t) + 2u_{2}(t) - 3e^{t} \\
u_{2}(t) = C_{2}e^{2t} + C_{2}(t)e^{2t}
\end{array} \right. $$

Où $C_{2}\mathbb{\in R}$ et
$C_{2}(t) = \int_{}^{}{5e^{t}e^{- 2t}dt} = 5\int_{}^{}{e^{- t}dt} = - 5e^{- t}$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
u_{1}'(t) = 2u_{1}(t) + 2u_{2}(t) - 3e^{t} \\
u_{2}(t) = C_{2}e^{2t} - 5e^{t}
\end{array} \right. $$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
u_{1}'(t) = 2u_{1}(t) + 2C_{2}e^{2t} - 13e^{t} \\
u_{2}(t) = C_{2}e^{2t} - 5e^{t}
\end{array} \right. $$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
u_{1}(t) = C_{1}e^{2t} + C_{1}(t)e^{2t} \\
u_{2}(t) = C_{2}e^{2t} - 5e^{t}
\end{array} \right. $$

Où $C_{1}\mathbb{\in R}$ et
$C_{1}(t) = \int_{}^{}{\left( 2C_{2}e^{2t} - 13e^{t} \right)e^{- 2t}dt} = 2C_{2}\int_{}^{}{dt} - 13\int_{}^{}{e^{- t}dt} = 2C_{2}t + 13e^{- t}$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
u_{1}(t) = C_{1}e^{2t} + 2C_{2}te^{2t} + 13e^{t} \\
u_{2}(t) = C_{2}e^{2t} - 5e^{t}
\end{array} \right. $$

$$\Leftrightarrow U(t) = \begin{bmatrix}
C_{1}e^{2t} + 2C_{2}te^{2t} + 13e^{t} \\
C_{2}e^{2t} - 5e^{t}
\end{bmatrix},\ C_{1},C_{2}\mathbb{\in R}$$

$$\Leftrightarrow X(t) = PU(t) = \begin{bmatrix}
C_{1}e^{2t} + 2C_{2}te^{2t} + 13e^{t} \\
\left( C_{1} + C_{2} \right)e^{2t} + 2C_{2}te^{2t} + 8e^{t}
\end{bmatrix}$$

$$\Leftrightarrow X(t) = \begin{bmatrix}
\left( C_{1} + 2C_{2}t \right)e^{2t} + 13e^{t} \\
\left( C_{1} + C_{2} + 2C_{2}t \right)e^{2t} + 8e^{t}
\end{bmatrix}$$

## 4\.

$$X(0) = \begin{bmatrix}
C_{1} + 13 \\
C_{1} + C_{2} + 8
\end{bmatrix} = \begin{bmatrix}
14 \\
8
\end{bmatrix}$$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
C_{1} + 13 = 14 \\
C_{1} + C_{2} + 8 = 8
\end{array} \right. $$

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
C_{1} = 1 \\
C_{1} + C_{2} = 0
\end{array} \right. \ \begin{matrix}
\  \\
L_{2} \leftarrow L_{2} - L_{1}
\end{matrix}$$

$\Leftrightarrow \left\lbrack  \begin{array}{r}
C_{1} = 1 \\
C_{2} = - 1
\end{array} \right. $

L'unique solution $X(t)$ qui vérifie $X(0) = \begin{bmatrix}
14 \\
8
\end{bmatrix}$ est :

$$X(t) = \begin{bmatrix}
(1 - 2t)e^{2t} + 13e^{t} \\
 - 2te^{2t} + 8e^{t}
\end{bmatrix}$$

# **Exercice 2 :**

## 1\.

**Forme :**

$\forall(x,y) \in \mathbb{R}^{3} \times \mathbb{R}^{3}$,
$\varphi(x,y)\mathbb{\in R}$ car somme finie de produits finis de réels.

Donc $\varphi$ est une forme sur $\mathbb{R}^{3} \times \mathbb{R}^{3}$.

**Symétrie :**

$$\forall x = \left( x_{1},x_{2},x_{3} \right),\ y = \left( y_{1},y_{2},y_{3} \right) \in \mathbb{R}^{3},$$

$$\varphi(x,y) = 3x_{1}y_{1} + 2x_{2}y_{2} + 3x_{3}y_{3} + \left( x_{1}y_{3} + x_{3}y_{1} \right) $$

$$= 3y_{1}x_{1} + 2y_{2}x_{2} + 3y_{3}x_{3} + \left( y_{1}x_{3} + y_{3}x_{1} \right) = \varphi(y,x)$$

Donc $\varphi$ est symétrique.

**Bilinéarité :**

- Linéarité à gauche

$\forall x = \left( x_{1},x_{2},x_{3} \right),\ x' = \left( x_{1}',x_{2}',x_{3}' \right),y = \left( y_{1},y_{2},y_{3} \right) \in \mathbb{R}^{3},\forall\lambda\mathbb{\in R}$,

$$\varphi\left( \lambda x + x',y \right) $$
$$= 3\left( \lambda x_{1} + x_{1}' \right)y_{1} + \left( \lambda x_{1} + x_{1}' \right)y_{3} $$
$$+ 2\left( \lambda x_{2} + x_{2}' \right)y_{2} + \left( \lambda x_{3} + x_{3}' \right)y_{1} + 3\left( \lambda x_{3} + x_{3}' \right)y_{3} $$
$$= \lambda\left( 3x_{1}y_{1} + x_{1}y_{3} + 2x_{2}y_{2} + x_{3}y_{1} + 3x_{3}y_{3} \right) $$
$$+ 3x_{1}'y_{1} + x_{1}'y_{3} + 2x_{2}'y_{2} + x_{3}'y_{1} + 3x_{3}'y_{3} = \lambda\varphi(x,y) + \varphi\left( x',y \right)$$

Donc $\varphi$ est linéaire à gauche.

- Linéarité à droite

$\varphi$ est symétrique et linéaire à gauche donc $\varphi$ est
linéaire à droite.

$\varphi$ est linéaire à gauche et linéaire à droite donc $\varphi$ est
bilinéaire.

Ainsi, $\varphi$ est une forme bilinéaire symétrique sur
$\mathbb{R}^{3}$.

2\.

Soit $\mathcal{B =}\left( e_{1},e_{2},e_{3} \right)$ la base canonique
de $\mathbb{R}^{3}$.

$$Mat_{\mathcal{B}}(\varphi) = \left\lbrack \varphi\left( e_{i},e_{j} \right) \right\rbrack_{1 \leq i,j \leq 3}$$

$$Mat_{\mathcal{B}}(\varphi) = \begin{bmatrix}
3 & 0 & 1 \\
0 & 2 & 0 \\
1 & 0 & 3
\end{bmatrix}$$

3\.

$$\forall x = \left( x_{1},x_{2},x_{3} \right),$$

$$\varphi(x,x) = 3x_{1}^{2} + x_{1}x_{3} + 2x_{2}^{2} + x_{3}x_{1} + 3x_{3}^{2}$$

$$\Leftrightarrow \varphi(x,x) = 3x_{1}^{2} + 2x_{1}x_{3} + 3x_{3}^{2} + 2x_{2}^{2}$$

$$\Leftrightarrow \varphi(x,x) = \left( \sqrt{3}x_{1} \right)^{2} + 2\left( \sqrt{3} \right)\left( \frac{1}{\sqrt{3}} \right)x_{1}x_{3} + \left( \frac{1}{\sqrt{3}}x_{3} \right)^{2} + 2x_{2}^{2} + \frac{8}{3}x_{3}^{2}$$

$$\Leftrightarrow \varphi(x,x) = \left( \sqrt{3}x_{1} + \frac{x_{3}}{\sqrt{3}} \right)^{2} + 2x_{2}^{2} + \frac{8}{3}x_{3}^{2}$$

## 4\.

$\varphi$ est une forme bilinéaire symétrique.

$\varphi$ définit alors un produit scalaire si $\varphi$ est positive et
définie

**Positivité :**

$\forall x \in \mathbb{R}^{3},\ \varphi(x,x) \geq 0$ car somme de réels
positifs.

Donc $\varphi$ est positive.

**Définité :** (Vocabulaire de K. EL AMINE)

$$\forall x = \left( x_{1},x_{2},x_{3} \right) \in \mathbb{R}^{3},$$

$$\varphi(x,x) = 0 \Leftrightarrow \left( \sqrt{3}x_{1} + \frac{x_{3}}{\sqrt{3}} \right)^{2} + 2x_{2}^{2} + \frac{8}{3}x_{3}^{2} = 0 \Leftrightarrow \left\lbrack  \begin{array}{r}
\sqrt{3}x_{1} + \frac{x_{3}}{\sqrt{3}} = 0 \\
2x_{2} = 0 \\
\frac{8}{3}x_{3} = 0
\end{array} \right.  \Leftrightarrow \left\lbrack  \begin{array}{r}
x_{1} = 0 \\
x_{2} = 0 \\
x_{3} = 0
\end{array} \right.  \Leftrightarrow x = 0_{\mathbb{R}^{3}}$$

Donc $\varphi$ est définie.

$\varphi$ est une forme bilinéaire définie positive sur $\mathbb{R}^{3}$
donc $\varphi$ est un produit scalaire sur $\mathbb{R}^{3}$.

## 5\.

$\mathcal{B}'$ est une famille de trois vecteurs de $\mathbb{R}^{3}$.
$\mathcal{B}'$ est une base de $\mathbb{R}^{3}$ si et seulement si elle
est libre, soit $\det_{\mathcal{B}}(u,v,w) \neq 0$

**Rappel :**
$\det_{\mathcal{B}}{(u,v,w)} = \det\left( Mat_{\mathcal{B}}\left( \mathcal{B}' \right) \right)$

$$\det_{\mathcal{B}}(u,v,w) = \left\vert  \begin{matrix}
1 & 1 & 1 \\
1 & - 1 & - 4 \\
0 & - 1 & 5
\end{matrix} \right\vert $$

$$L_{2} \leftarrow L_{2} - L_{1}$$

$$\det_{\mathcal{B}}(u,v,w) = \left\vert  \begin{matrix}
1 & 1 & 1 \\
0 & - 2 & - 5 \\
0 & - 1 & 5
\end{matrix} \right\vert $$

$\det_{\mathcal{B}}(u,v,w) = \left\vert  \begin{matrix}- 2 & - 5 \\ - 1 & 5
\end{matrix} \right\vert  = - 15 \neq 0\ \text{donc}\ \mathcal{B}'\ \text{est libre},\ \text{donc}\ \mathcal{B}'\ \text{est une base de}\ \mathbb{R}^{3}$.

## 6\.

**Orthogonalité**

$\mathcal{B}'$ est orthogonale pour $\varphi$ si et seulement si tout
produit scalaire $\varphi$ de deux vecteurs distincts de cette base est
nul.

$$\varphi(u,v) = \varphi(v,u) = 3 - 1 - 2 + 0 + 0 = 0$$

$$\varphi(v,w) = \varphi(w,v) = 3 + 5 + 8 - 1 - 15 = 0$$

$$\varphi(w,u) = \varphi(u,w) = 3 - 8 + 5 = 0$$

Donc $\mathcal{B}'$ est orthogonale pour $\varphi$.

**Normalité**

$\mathcal{B}'$ est orthonormale pour $\varphi$ si et seulement si
$\mathcal{B}'$ est orthogonale pour $\varphi$ et tout produit scalaire
$\varphi$ d'un vecteur de cette base avec lui-même vaut 1.

$$\varphi(u,u) = 3 + 2 = 5 \neq 1$$

Donc $\mathcal{B}'$ n'est pas orthonormale pour $\varphi$.

## 7\.

$Mat_{\mathcal{B}'}(\varphi) = \left\lbrack \varphi\left( \varepsilon_{i},\varepsilon_{j} \right) \right\rbrack_{1 \leq i,j \leq 3}$
où $\varepsilon_{1} = u,\varepsilon_{2} = v,\varepsilon_{3} = w$

On a :

$\varphi(v,v) = 6$ et $\varphi(w,w) = 120$

Donc :

$$Mat_{\mathcal{B}'}(\varphi) = \begin{bmatrix}
5 & 0 & 0 \\
0 & 6 & 0 \\
0 & 0 & 120
\end{bmatrix}$$

**Remarque :** On peut aussi utiliser la formule
$Mat_{\mathcal{B}'}(\varphi) = P^{T}Mat_{\mathcal{B}}(\varphi)P$ avec
$P = \begin{bmatrix}
u & v & w
\end{bmatrix}$

# **Exercice 3 :**

## 1\.

**Forme :**

$\forall P,Q \in \mathbb{R}_{2}\lbrack X\rbrack,\ \left\langle P,Q \right\rangle\mathbb{\in R}$
car intégrale sur un segment d'une fonction réelle continue sur ce
segment.

Donc $\left\langle .,. \right\rangle$ est une forme sur
$\mathbb{R}_{2}\lbrack X\rbrack$.

**Symétrie :**

$$\forall P,Q \in \mathbb{R}_{2}\lbrack X\rbrack, $$

$$\left\langle P,Q \right\rangle = \int_{- 1}^{1}{P(x)Q(x)dx} = \int_{- 1}^{1}{Q(x)P(x)dx} = \left\langle Q,P \right\rangle$$

Donc $\left\langle .,. \right\rangle$ est symétrique

**Bilinéarité :**

- Linéarité à gauche

$\forall P_{1},P_{2},Q \in \mathbb{R}_{2}\lbrack X\rbrack,$
$\forall\lambda\mathbb{\in R}$,

$$\left\langle \lambda P_{1} + P_{2},Q \right\rangle $$
$$= \int_{- 1}^{1}{\left( \lambda P_{1}(x) + P_{2}(x) \right)Q(x)dx} $$
$$= \lambda\int_{- 1}^{1}{P_{1}(x)Q(x)dx} + \int_{- 1}^{1}{P_{2}(x)Q(x)dx} $$
$$= \lambda\left\langle P_{1},Q \right\rangle + \left\langle P_{2},Q \right\rangle$$

Donc $\left\langle .,. \right\rangle$ est linéaire à gauche.

- Linéarité à droite

$\left\langle .,. \right\rangle$ est symétrique et linéaire à gauche
donc $\left\langle .,. \right\rangle$ est linéaire à droite.

$\left\langle .,. \right\rangle$ est linéaire à gauche et linéaire à
droite donc $\left\langle .,. \right\rangle$ est bilinéaire.

**Positivité :**

$\forall P \in \mathbb{R}_{2}\lbrack X\rbrack$,

$$\left\langle P,P \right\rangle = \int_{- 1}^{1}{P^{2}(x)dx}$$

$$\forall x \in \lbrack - 1,1\rbrack,\ P^{2}(x) \geq 0\ \text{donc}\ \int_{- 1}^{1}{P^{2}(x)dx} \geq 0\ \text{par croissance de l'intégrale}$$

Donc $\left\langle P,P \right\rangle \geq 0$

Donc $\left\langle .,. \right\rangle$ est positive.

**Définité :**

$\forall P \in \mathbb{R}_{2}\lbrack X\rbrack$,

$$\left\langle P,P \right\rangle $$
$$= 0 \Leftrightarrow \int_{- 1}^{1}{P^{2}(x)} $$
$$= 0 \Leftrightarrow \forall x \in \lbrack - 1,1\rbrack,\ P^{2}(x) $$
$$= 0 \Leftrightarrow \forall x \in \lbrack - 1,1\rbrack,\ P(x) $$
$$= 0 \Leftrightarrow P\ \text{admet une infinité de racines} \Leftrightarrow P $$
$$= 0_{\mathbb{R}_{2}\lbrack X\rbrack}$$

Donc $\left\langle .,. \right\rangle$ est définie.

$\left\langle .,. \right\rangle$ est une forme bilinéaire symétrique
définie positive sur $$\mathbb{R}_{2}\lbrack X\rbrack$$ donc
$\left\langle .,. \right\rangle$ est un produit scalaire sur
$$\mathbb{R}_{2}\lbrack X\rbrack$$.

## 2\.

$$\left\Vert  1 \right\Vert  = \sqrt{\left\langle 1,1 \right\rangle} = \sqrt{\int_{- 1}^{1}{dx}} = \sqrt{2}$$

$$\text{On a donc}\ P_{1} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$$

## 3\.

$$\left\langle X,P_{1} \right\rangle = \frac{\sqrt{2}}{2}\int_{- 1}^{1}{xdx} = \frac{\sqrt{2}}{4}\left\lbrack x^{2} \right\rbrack_{- 1}^{1} = 0$$

On a donc $Q_{2} = X$ et on a bien
$\left\langle Q_{2},P_{1} \right\rangle = \left\langle X,P_{1} \right\rangle = 0$
donc $Q_{2}\bot P_{1}$ pour $\left\langle .,. \right\rangle$.

## 4\.

$$\left\Vert  Q_{2} \right\Vert  = \left\Vert  X \right\Vert  = \sqrt{\left\langle X,X \right\rangle} = \sqrt{\int_{- 1}^{1}{x^{2}dx}} = \sqrt{\frac{1}{3}\left\lbrack x^{3} \right\rbrack_{- 1}^{1}} = \frac{\sqrt{2}}{\sqrt{3}} = \frac{2}{\sqrt{6}}$$

$$\text{On a donc}\ P_{2} = \frac{\sqrt{6}}{2}X$$

## 5\.

On pose :

$$Q_{3} = X^{2} - \left\langle X^{2},P_{1} \right\rangle P_{1} - \left\langle X^{2},P_{2} \right\rangle P_{2}$$

$$\left\langle X^{2},P_{1} \right\rangle $$
$$= \frac{\sqrt{2}}{2}\int_{- 1}^{1}{x^{2}dx} $$
$$= \frac{\sqrt{2}}{6}\left\lbrack x^{3} \right\rbrack_{- 1}^{1} $$
$$= \frac{\sqrt{2}}{3}$$

$$\left\langle X^{2},P_{2} \right\rangle$$ 
$$= \frac{\sqrt{6}}{2}\int_{- 1}^{1}{x^{3}dx} $$
$$= \frac{\sqrt{6}}{8}\left\lbrack x^{4} \right\rbrack_{- 1}^{1} = 0$$

$$Q_{3} = X^{2} - \frac{\sqrt{2}}{3} \times \frac{\sqrt{2}}{2} = X^{2} - \frac{1}{3}$$

On pose :

$$P_{3} = \frac{Q_{3}}{\left\Vert  Q_{3} \right\Vert }$$

$$\left\Vert  Q_{3} \right\Vert  $$
$$= \sqrt{\int_{- 1}^{1}{\left( x^{2} - \frac{1}{3} \right)^{2}dx}} $$
$$= \sqrt{\int_{- 1}^{1}{x^{4}dx} - \int_{- 1}^{1}{\frac{2}{3}x^{2}dx} + \int_{- 1}^{1}{\frac{1}{9}dx}} $$
$$= \sqrt{\left\lbrack \frac{1}{5}x^{5} \right\rbrack_{- 1}^{1} - \left\lbrack \frac{2}{9}x^{3} \right\rbrack_{- 1}^{1} + \left\lbrack \frac{1}{9}x \right\rbrack_{- 1}^{1}} $$
$$= \sqrt{\frac{2}{5} - \frac{4}{9} + \frac{2}{9}} = \sqrt{\frac{18 - 20 + 10}{45}} = \sqrt{\frac{8}{45}} = \frac{2\sqrt{2}}{3\sqrt{5}}$$

$$P_{3} = \left( X^{2} - \frac{1}{3} \right) \times \frac{3\sqrt{5}}{2\sqrt{2}}$$

$$P_{3} = \left( X^{2} - \frac{1}{3} \right)\frac{3\sqrt{10}}{4}$$

$$P_{3} = \frac{\sqrt{10}}{4}\left( 3X^{2} - 1 \right)$$

Montrons que $\left( P_{1},P_{2},P_{3} \right)$ est une base orthonormée
de $\mathbb{R}_{2}\lbrack X\rbrack$ pour
$\left\langle .,. \right\rangle$.

- Orthogonalité

$Q_{2}\bot P_{1}$ donc $P_{2}\bot P_{1}$

$$\left\langle P_{3},P_{1} \right\rangle $$
$$= \frac{\sqrt{10}}{4}\left\langle 3X^{2} - 1,P_{1} \right\rangle $$
$$= \frac{\sqrt{10}}{4}\left( 3\left\langle X^{2},P_{1} \right\rangle - \left\langle 1,P_{1} \right\rangle \right) $$
$$= \frac{\sqrt{10}}{4} \times \left( 3 \times \frac{\sqrt{2}}{3} - \frac{\sqrt{2}}{2}\left\Vert  1 \right\Vert ^{2} \right) $$
$$= \frac{\sqrt{10}}{4} \times \left( \sqrt{2} - \sqrt{2} \right) = 0\ \text{donc}\ P_{3}\bot P_{1}$$

$$\left\langle P_{3},P_{2} \right\rangle $$
$$= \frac{\sqrt{10}}{4}\left\langle 3X^{2} - 1,P_{2} \right\rangle $$
$$= \frac{\sqrt{10}}{4}\left( 3\left\langle X^{2},P_{2} \right\rangle - \left\langle 1,P_{2} \right\rangle \right) $$
$$= \frac{\sqrt{10}}{4}\left( 0 - \frac{\sqrt{6}}{2}\int_{- 1}^{1}{xdx} \right) $$
$$= - \frac{\sqrt{60}}{16}\left\lbrack x^{2} \right\rbrack_{- 1}^{1} $$
$$= 0\ \text{donc}\ P_{3}\bot P_{2}$$

Donc $$\left( P_{1},P_{2},P_{3} \right)$$ est une famille orthogonale de
$$\mathbb{R}_{2}\lbrack X\rbrack$$ pour $\left\langle .,. \right\rangle$,
donc $$\left( P_{1},P_{2},P_{3} \right)$$ est une base orthogonale de
$$\mathbb{R}_{2}\lbrack X\rbrack$$ pour $$\left\langle .,. \right\rangle$$

- Normalité

$$\left\Vert  P_{1} \right\Vert  
= \frac{\left\Vert  1 \right\Vert }{\left\Vert  1 \right\Vert } 
= 1,\ \left\Vert  P_{2} \right\Vert  = \frac{\left\Vert  Q_{2} \right\Vert }{\left\Vert  Q_{2} \right\Vert } 
= 1,\ \left\Vert  P_{3} \right\Vert  = \frac{\left\Vert  Q_{3} \right\Vert }{\left\Vert  Q_{3} \right\Vert } = 1$$

Donc $$\left( P_{1},P_{2},P_{3} \right)$$ est une base orthonormale de
$$\mathbb{R}_{2}\lbrack X\rbrack$$ pour $\left\langle .,. \right\rangle$.