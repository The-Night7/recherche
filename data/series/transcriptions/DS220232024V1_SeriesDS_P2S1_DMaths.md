---
source: DS220232024V1_SeriesDS_P2S1_DMaths.pdf (scan)
transcription: manuelle
---

# Séries — Devoir surveillé 2 (2023/2024, mercredi 29 novembre)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1

Soit $(f_n)_{n\in\mathbb{N}}$ et $(g_n)_{n\in\mathbb{N}}$ deux suites d'applications définies sur une partie $D$ de $\mathbb{R}$ et qui convergent uniformément respectivement vers des fonctions $f$ et $g$.

1. Expliciter la définition de « $(f_n)_{n\in\mathbb{N}}$ converge uniformément vers $f$ ».
2. Montrer qu'alors la suite d'applications $(f_n+g_n)_{n\in\mathbb{N}}$ converge uniformément vers la fonction $(f+g)$.

## Exercice 2

On pose, pour tout $n \in \mathbb{N}^*$ et $x \in \mathbb{R}$, $f_n(x) := \sqrt{n}\arctan\frac{x}{n}$.

1. Montrer que, pour tout $n \in \mathbb{N}^*$ et tout $x \in \mathbb{R}$, $f_n'(x) = \frac{1}{\sqrt{n}}\cdot\frac{1}{1+\frac{x^2}{n^2}}$. En déduire que la suite de fonctions $(f_n')_{n\in\mathbb{N}^*}$ converge uniformément vers une fonction que l'on déterminera.
2. Montrer que, pour tout $n \in \mathbb{N}^*$ et tout $x \in \mathbb{R}$ : $f_n(x) = \int_0^x f_n'(t)\,dt$. En déduire que $(f_n)_{n\in\mathbb{N}}$ converge uniformément vers la fonction nulle sur tout intervalle borné de $\mathbb{R}$.
3. Montrer que $(f_n)_{n\in\mathbb{N}}$ ne converge pas uniformément sur $\mathbb{R}$.

## Exercice 3

Soit $(f_n)_{n\geq 2}$ la suite de fonctions définie sur $[0,1]$ par :
$$f_n(x) = \begin{cases} -n^3x^2 + 2n^2x & \text{si } x \in \left[0, \frac{2}{n}\right] \\ 0 & \text{si } x \in \left[\frac{2}{n}, 1\right] \end{cases}$$

1. Étudier la convergence simple de cette suite, vers une fonction que l'on déterminera.
2. Calculer $\lim_{n\to\infty} \int_0^1 f_n(t)\,dt$.
3. Est-ce que $(f_n)_{n\geq 2}$ converge uniformément ?
4. Montrer que $(f_n)_{n\geq 2}$ converge uniformément sur $[a,1]$ pour $a \in ]0,1[$.
