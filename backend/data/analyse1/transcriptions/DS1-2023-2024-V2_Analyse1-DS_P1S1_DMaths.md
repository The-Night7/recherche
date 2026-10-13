# Analyse 1 — DS 2023–2024, sujet (fichier « DS1 V2 »)

> Source : `PREING1-S1/Analyse1-DS/DS1-2023-2024-V2_Analyse1-DS_P1S1_DMaths.pdf`, 2 pages (scans du sujet imprimé).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX.
> **Écart de nommage :** l’en-tête du sujet indique « Devoir Surveillé 2 », daté du 12/12/2023, alors que le fichier est nommé DS1. Le nom du fichier est conservé pour la traçabilité. Dans l’exercice 3, l’exposant de $k^3$ est surchargé sur la source ; la lecture $k^3$ est retenue.

**Préing 1 — Devoir Surveillé 2 — Analyse I**

| Date | Durée | Nombre de pages |
| --- | --- | --- |
| 12/12/2023 | 1 h 00 | 2 |

L’usage de tout appareil électronique est interdit.

**Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.** *Le sujet comporte 4 exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.*

## Exercice 1 (6 points)

Déterminer, si elle existe, la limite de chacune des suites suivantes. Sinon, justifier pourquoi il n’y a pas de limite.

1. $\forall n\in\mathbb N,\ u_n=\sqrt{n^4+3n^2}-\sqrt{n^4+n-1}$.
2. $\forall n\in\mathbb N^*,\ v_n=\dfrac{E(\ln(n))}{n}$.
3. $\forall n\in\mathbb N,\ z_n=\dfrac{(-1)^n n^2+n^3}{1+3n^3}+i\cdot\dfrac{n^2+2n}{3n^2+2i}$.

## Exercice 2 (4 points)

Montrer, en revenant à la définition de la limite, que :

1. $\displaystyle\lim_{n\to+\infty}u_n=2$, pour $u_n=\dfrac{2n^3-3}{n^3+1}$.
2. $\displaystyle\lim_{n\to+\infty}v_n=-\infty$, pour $v_n=-2\ln(3n+1)$.

## Exercice 3 (4 points)

Pour tout $n\in\mathbb N^*$, on pose

$$a_n=\sum_{k=1}^{n}\frac1{k^3}\quad\text{et}\quad b_n=a_n+\frac1{n^2}.$$

1. Montrer que les suites $(a_n)_{n\in\mathbb N}$ et $(b_n)_{n\in\mathbb N}$ sont adjacentes.
2. En déduire la convergence des suites $(a_n)_{n\in\mathbb N}$ et $(b_n)_{n\in\mathbb N}$. Qu’est-ce qu’on peut dire à propos de la valeur de leur limite ?

## Exercice 4 (6 points)

On considère la suite $(u_n)_{n\in\mathbb N}$ définie par récurrence de la manière suivante :

$$u_0=6\quad\text{et}\quad u_{n+1}=4-\frac{18}{2u_n+12}.$$

On se placera dans $I=[0,18]$. On pose

$$f : I\longrightarrow\mathbb R,\qquad x\longmapsto 4-\frac{18}{2x+12}.$$

1. Déterminer le sens de variation de la fonction $f$.
2. Montrer que l’intervalle $I$ est stable par $f$.
3. Déterminer le(s) point(s) fixe(s) de $f$ dans cet intervalle.
4. Déterminer le sens de variation de la suite $(u_n)_{n\in\mathbb N}$.
5. Étudier la convergence de la suite $(u_n)_{n\in\mathbb N}$.
