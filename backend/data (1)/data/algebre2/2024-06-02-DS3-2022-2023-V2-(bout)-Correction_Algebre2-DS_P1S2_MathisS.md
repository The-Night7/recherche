---
title: DS3 2022 2023 V2 (bout) Correction
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


### 1\.

### a\.

$$M = \begin{pmatrix}
2 & 4 & - 2 \\
 - 1 & - t & 1 \\
 - 1 & 0 & t
\end{pmatrix}$$

### 1.a.

**Méthode 1 :**
$$M\sim\begin{pmatrix}
1 & 2 & - 1 \\
 - 1 & - t & 1 \\
 - 1 & 0 & t
\end{pmatrix},\det(M) = 2\left| \begin{matrix}
1 & 2 & - 1 \\
 - 1 & - t & 1 \\
 - 1 & 0 & t
\end{matrix} \right|$$

$$M\sim\begin{pmatrix}
1 & 2 & - 1 \\
0 & 2 - t & 0 \\
0 & 2 & t - 1
\end{pmatrix},\det(M) = 2\left| \begin{pmatrix}
1 & 2 & - 1 \\
0 & 2 - t & 0 \\
0 & 2 & t - 1
\end{pmatrix} \right|$$

$$M\sim\begin{pmatrix}
1 & 2 & - 1 \\
0 & 2 & t - 1 \\
0 & 2 - t & 0
\end{pmatrix},\det(M) = - 2\left| \begin{matrix}
1 & 2 & - 1 \\
0 & 2 & t - 1 \\
0 & 2 - t & 0
\end{matrix} \right|$$

$$\det(M) = - 2\left| \begin{matrix}
2 & t - 1 \\
2 - t & 0
\end{matrix} \right| = 2(t - 1)(2 - t)$$

$$\det(2M) = 2^{3}\det(M) = 8\det(M) = 16(t - 1)(2 - t)$$

$$\det\left( M^{2} \right) = {\det(M)}^{2} = 4(t - 1)^{2}(2 - t)^{2}$$

**Methode 2 :**

$$\det(M) = - 2t^{2} - 4( - t + 1) - 2( - t) = - 2t^{2} + 4t - 4 + 2t = - 2t^{2} + 6t - 4$$

### b\.

Si $t = 2$, $rg(M) = 2$

Si $t \neq 2$

$$M\sim\begin{pmatrix}
1 & 2 & - 1 \\
0 & 2(2 - t) & (t - 1)(2 - t) \\
0 & 2(2 - t) & 0
\end{pmatrix}$$

$$M\sim\begin{pmatrix}
1 & 2 & - 1 \\
0 & 2(2 - t) & (t - 1)(2 - t) \\
0 & 0 & (t - 1)(2 - t)
\end{pmatrix}$$

SI $t = 1$, $rg(M) = 2$

Si $t \neq 2,\ t \neq 1,\ rg(M) = 3$

### c\.

$f$ est injective/surjective/bijective si et seulement si

$t \notin \{ 1,2 \}$

### 2.a.

$$f(x,y,z) = (2x + 4y - 2z, - x - y + z, - x + z)$$

### 2.b.

$$rg(f) = rg(M) = 2$$

D'après le théorème du rang,

$$\dim\left( \ker f \right) = \dim\left( \mathbb{R}^{3} \right) - rg(f) = 1$$