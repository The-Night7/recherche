---
source: DS1-2020-2021_Series-DS_P2S1_KGuezguez-AElJanati-AHajej.pdf, pages 1 et 2 (corrigé dans DS1-2020-2021-Correction_Series-DS_P2S1_Inconnu_RayaneM-MathisS)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (novembre 2020)

Devoir du jeudi 5 novembre 2020 (A. El Janati, K. Guezguez, A. Hajej). Durée 1 h 30, appareils électroniques et documents interdits.

## Exercice 1 : Nature de quatre séries

**Énoncé.** (4 points) Préciser la nature de chacune des séries suivantes :
$$(1)\ \sum_{n\geq 1} n\sin\left(\frac{1}{n}\right) \qquad (2)\ \sum_{n\geq 1}\frac{1}{\sqrt{n(n + \ln n)}}$$
$$(3)\ \sum_{n\geq 2}\frac{1}{n\ln(n)} \qquad (4)\ \sum_{n\geq 1}\left(e - \left(1 + \frac{1}{n}\right)^n\right)$$

## Exercice 2 : Vrai ou faux

**Énoncé.** (3 points) Soit $\sum_{n\geq 0} u_n$ une série à termes réels strictement positifs. Les affirmations suivantes sont-elles vraies ou fausses ?

1. Les séries de terme général $u_n$ et $\sqrt{u_n}$ respectivement sont de même nature.
2. Les séries de terme général $u_n$ et $\ln(1 + u_n)$ respectivement sont de même nature.

Justifier vos réponses : si l'affirmation est vraie, en donner une démonstration et si elle est fausse, produire un contre-exemple.

## Exercice 3 : Somme d'une série rationnelle

**Énoncé.** (3,5 points) On considère la suite définie pour tout entier naturel $n \geq 2$ par $u_n = \dfrac{n}{(n^2-1)^2}$.

1. Étudier la convergence de la série numérique $\sum_{n\geq 2} u_n$.
2. Décomposer le terme général $u_n$ en fonction de $\frac{1}{(n+1)^2}$ et $\frac{1}{(n-1)^2}$.
3. En déduire la somme de la série $\sum_{n\geq 2} u_n$.

## Exercice 4 : Série de Bertrand et comparaison série-intégrale

**Énoncé.** (5 points) On considère la fonction
$$F : [3, +\infty[ \to \mathbb{R}, \quad x \mapsto \ln(\ln x)$$

1. Déterminer $\lim_{x\to+\infty} F(x)$. Quelle est la dérivée $f$ de $F$ ? Montrer que $f$ est décroissante et positive sur $[3, +\infty[$.
2. On considère la série $\sum_{n\geq 3}\frac{1}{n\ln n}$. Soit $S_N$ la somme partielle d'ordre $N$. Encadrer $S_N$ par deux intégrales.
3. En déduire un équivalent de $S_N$.

## Exercice 5 : Série de logarithmes à deux paramètres

**Énoncé.** (5,5 points) Soit $a$ et $b$ deux réels. On considère la série numérique :
$$\sum_{n\geq 1}\big(\ln(n) + a\ln(n+1) + b\ln(n+2)\big)$$

1. Donner un développement asymptotique du terme général de cette série sous la forme :
$$\ln(n) + a\ln(n+1) + b\ln(n+2) = \alpha\ln(n) + \frac{\beta}{n} + \frac{\gamma}{n^2} + o\left(\frac{1}{n^2}\right)$$
où $\alpha, \beta, \gamma$ sont des réels à déterminer en fonction de $a$ et de $b$.
2. En déduire les valeurs de $a$ et de $b$ pour que la série converge.
3. Pour ces valeurs de $a$ et de $b$, calculer alors $S_N = \sum_{n=1}^{N}\big(\ln(n) + a\ln(n+1) + b\ln(n+2)\big)$.
4. En déduire la somme de la série.
