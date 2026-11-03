---
source: PREING2-S1/Series-DS/DS2-2023-2024-V4-Correction_Series-DS_P2S1_DMaths.pdf
pages: 1-2
transcription: manuelle
---

# Séries — DS2, version 4, corrigé (2023/2024)

## Consignes

Mardi 28 novembre 2023. Durée : 60 minutes. Documents et supports électroniques interdits. Exercices indépendants ; barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 : Questions de cours

1. Énoncer la définition de la convergence uniforme d'une suite de fonctions.
2. Énoncer le théorème d'inversion limite-intégrale.

> Le PDF ne donne pas de réponse à cet exercice.

## Exercice 2 : Limite simple discontinue

**Énoncé.** Sur $[0,1]$, on considère

$$f_n(x)=\frac{1-x^n}{1+x^{2n}}.$$

1. Montrer que $(f_n)$ converge simplement sur $[0,1]$ vers une limite $f$ à déterminer.
2. La convergence est-elle uniforme sur $[0,1]$ ?
3. Est-elle localement uniforme sur $[0,1[$ ?

**1.** Pour $x\in[0,1[$, $x^n\to0$, donc $f_n(x)\to1$. Pour $x=1$, $f_n(1)=0$. Ainsi

$$f(x)=\begin{cases}1&\text{si }0\le x<1,\\0&\text{si }x=1.\end{cases}$$

**2.** Chaque $f_n$ est continue sur $[0,1]$ comme quotient de fonctions continues à dénominateur non nul. La limite simple $f$ est discontinue ; la convergence n'est donc pas uniforme sur $[0,1]$.

**3.** Fixons $a\in]0,1[$. Pour $x\in[0,a]$ et $n\ge1$,

$$\begin{aligned}
|f_n(x)-f(x)|&=\left|\frac{1-x^n}{1+x^{2n}}-1\right|\\
&=\frac{x^n(1+x^n)}{1+x^{2n}}\le a^n(1+a^n).
\end{aligned}$$

Comme $a^n\to0$, le supremum de cette différence sur $[0,a]$ tend vers zéro. La convergence est uniforme sur chaque $[0,a]$, donc localement uniforme sur $[0,1[$.

## Exercice 3 : Convergence locale et défaut de convergence uniforme

**Énoncé.** Sur $[0,2]$, on définit

$$f_n(x)=n^2x(1-x)^n.$$

1. Déterminer le domaine de convergence et la limite simple $f$.
2. Pour $\alpha\in]0,1[$, montrer que la convergence est uniforme sur $[\alpha,2-\alpha]$.
3. Calculer $\int_0^1 f_n(x)\,dx$. Indication : intégration par parties ou changement de variable $y=1-x$.
4. La convergence est-elle uniforme sur $[0,1]$ ?

**1.** $f_n(0)=0$. Pour $0<x<2$, on a $|1-x|<1$, donc $n^2(1-x)^n\to0$ et $f_n(x)\to0$. En revanche, $f_n(2)=2n^2(-1)^n$ n'a pas de limite. Le domaine de convergence est $[0,2[$ et la limite simple y est nulle.

> **Rectification de la source :** le corrigé écrit $|1-x|<1$ pour tout $x\in[0,2[$. Le point $x=0$ doit être traité séparément, comme ci-dessus.

**2.** Pour $x\in[\alpha,2-\alpha]$, on a $x\le2-\alpha$ et $|1-x|\le1-\alpha<1$. Ainsi

$$|f_n(x)|\le n^2(2-\alpha)(1-\alpha)^n.$$

Ce majorant tend vers zéro. La convergence est donc uniforme sur $[\alpha,2-\alpha]$.

**3.** Avec $y=1-x$,

$$\begin{aligned}
\int_0^1 f_n(x)\,dx
&=n^2\int_0^1 x(1-x)^n\,dx\\
&=n^2\int_0^1 y^n(1-y)\,dy\\
&=n^2\left[\frac{y^{n+1}}{n+1}-\frac{y^{n+2}}{n+2}\right]_0^1\\
&=\frac{n^2}{(n+1)(n+2)}.
\end{aligned}$$

**4.** Toutes les fonctions $f_n$ sont continues sur $[0,1]$, mais

$$\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=1\ne0=\int_0^1\lim_{n\to\infty}f_n(x)\,dx.$$

Par contraposée du théorème d'inversion limite-intégrale, la convergence n'est pas uniforme sur $[0,1]$.
