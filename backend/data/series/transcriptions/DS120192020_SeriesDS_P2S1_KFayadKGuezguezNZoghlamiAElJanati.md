---
source: DS1-2019-2020_Series-DS_P2S1_KFayad-KGuezguez-NZoghlami-AElJanati.pdf, pages 1 et 2 (corrigé dans DS1-2019-2020-Correction_Series-DS_P2S1_Inconnu_RayaneM-MathisS)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (octobre 2019)

Devoir du vendredi 18 octobre 2019 (A. El Janati, K. Fayad, K. Guezguez, N. Zoghlami). Durée 2 heures, appareils électroniques et documents interdits.

> **Note :** l'en-tête du sujet porte « Devoir surveillé 2 », mais il s'agit bien du premier devoir du semestre (18 octobre).

## Exercice 1 : Séries de terme général uₙ^α

**Énoncé.** Soit $\sum_{n\geq 1} u_n$ une série à termes positifs et $\alpha > 0$.

1. On suppose dans cette question que $\sum_{n\geq 1} u_n$ converge.
    a) Montrer que $u_n \leq 1$ à partir d'un certain rang.
    b) En déduire que si $\alpha \geq 1$, alors la série $\sum_{n\geq 1} u_n^\alpha$ converge.
2. On suppose dans cette question que $\sum_{n\geq 1} u_n$ diverge. Montrer que si $\alpha \leq 1$, alors la série $\sum_{n\geq 1} u_n^\alpha$ diverge. *On pourra raisonner selon si la divergence est grossière ou pas.*

## Exercice 2 : Série dépendant de deux paramètres

**Énoncé.** Soit $(a, b) \in \mathbb{R}^2$ tel que $a \geq b$. Le but de cet exercice est d'étudier la série numérique de terme général
$$u_n = \left(\sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1}\right)^n$$
définie à partir d'un certain rang.

1. Donner le développement limité en $\frac{1}{n}$ à l'ordre 1 au voisinage de $+\infty$ de $\sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1}$.
2. On suppose dans cette question que $a - b \neq 2$. Étudier la nature de la série $\sum u_n$.
3. On suppose dans cette question que $a - b = 2$.
    a) Calculer $\lim_{n\to+\infty} \ln(n u_n)$.
    b) Que peut-on en déduire ?

## Exercice 3 : Une somme télescopique et cinq séries

**Énoncé.**

1. Montrer la convergence et calculer la somme de la série
$$\sum_{n\geq 1} \ln\left(\frac{(n+1)^2}{n(n+2)}\right)$$
2. Étudier la nature de la série numérique $\sum_{n\geq 1} u_n$ dans chacun des cas suivants :
    a) $u_n = n^{\frac{1}{n^2}} - 1$
    b) $u_n = \left(\cos\left(\frac{1}{n}\right)\right)^n - 1$
    c) $u_n = \dfrac{\ln(n)}{n^2}$
    d) $u_n = \sqrt{n^2 + n} - n$
    e) $u_n = \dfrac{(n!)^2}{(2n)!}$

## Exercice 4 : Série harmonique et constante d'Euler

**Énoncé.** Soit $f$ la fonction décroissante définie sur $[1, +\infty[$ par $f(x) = \frac{1}{x}$. Pour $n \in \mathbb{N}^*$, on pose
$$S_n = \sum_{k=1}^{n} f(k)$$

1. Montrer que pour tout $n \in \mathbb{N}^*$,
$$\int_1^{n+1} f(x)\,dx \leq S_n \leq 1 + \int_1^{n} f(x)\,dx$$
2. En calculant les intégrales, déduire un équivalent simple de $S_n$ puis la nature de la série $\sum_{n\geq 1} \frac{1}{n}$.
3. Pour $n \geq 1$, on pose $a_n = S_n - \ln(n)$ et $b_n = S_n - \ln(n+1)$.
    a) Montrer que les deux suites $(a_n)_{n\geq 1}$ et $(b_n)_{n\geq 1}$ sont adjacentes. *Leur limite commune est notée $\gamma$ et est appelée la constante d'Euler.*
    b) Montrer que $S_n = \ln(n) + \gamma + o(1)$.
4. Pour $n \in \mathbb{N}^*$, on pose $u_n = \frac{1}{n(2n+1)}$.
    a) Justifier que la série $\sum_{n\geq 1} u_n$ converge.
    b) Décomposer en éléments simples la fraction rationnelle $F(X) = \frac{1}{X(2X+1)}$.
    c) Soit $N \in \mathbb{N}^*$. En regroupant les entiers pairs et impairs dans la somme $\sum_{n=1}^{2N+1} \frac{1}{n}$, et en utilisant la fraction rationnelle $F$, montrer que
$$\frac{1}{2}\sum_{n=1}^{N} \frac{1}{n(2n+1)} = S_N - S_{2N+1} + 1$$
    d) En déduire que
$$\sum_{n=1}^{+\infty} \frac{1}{n(2n+1)} = 2 - 2\ln(2)$$

> **Erreur corrigée :** le sujet d'origine écrit $\sum_{n=1}^{2N+1} \frac{1}{N}$ (au lieu de $\frac{1}{n}$) et « $= S_N - S_{2N+1} + 2$ » au 4.c) ; la bonne constante est $+1$ (sinon la limite du d) serait $4 - 2\ln 2$).
