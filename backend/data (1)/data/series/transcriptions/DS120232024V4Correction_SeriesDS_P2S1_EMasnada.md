---
source: DS1-2023-2024-V4-Correction_Series-DS_P2S1_EMasnada.pdf, pages 1 à 3
transcription: manuelle
---

# Séries — Devoir surveillé 1 (2023/2024, mercredi 25 octobre, version 4) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Séries alternées

**Énoncé.** (2 pts) Énoncer la définition d'une série alternée et le Théorème Spécial des Séries Alternées.

**Correction.**

> **Complément :** le corrigé d'origine ne contient pas de réponse à cet exercice de cours.

**Définition.** Une série réelle $\sum u_n$ est **alternée** si son terme général change de signe à chaque rang, c'est-à-dire s'il s'écrit $u_n = (-1)^n a_n$ (ou $u_n = (-1)^{n+1}a_n$) avec $a_n \geq 0$ pour tout $n$.

**Théorème spécial des séries alternées (TSSA).** Soit $(a_n)$ une suite réelle **décroissante** et de **limite nulle** (donc positive). Alors la série $\sum (-1)^n a_n$ converge. De plus, son reste $R_n = \sum_{k=n+1}^{+\infty}(-1)^k a_k$ vérifie $|R_n| \leq a_{n+1}$ et a le signe de son premier terme $(-1)^{n+1}a_{n+1}$.

## Exercice 2 : Somme d'une série rationnelle

**Énoncé.** (6 pts) Pour $n \geq 2$ on considère la série de terme général $u_n = \dfrac{2n+3}{n(n^2-1)}$.

1. Déterminer la nature de la série $\sum_{n\geq 2} u_n$.
2. Pour $n \geq 2$ donner la décomposition de $u_n$ en éléments simples.
3. Calculer la somme de la série $\sum_{n\geq 2} u_n$.

**Correction.**

**1.** $u_n$ est une fraction rationnelle en $n$ : $u_n \underset{+\infty}{\sim} \frac{2n}{n^3} = \frac{2}{n^2}$, de signe constant (positif) et terme d'une série de Riemann convergente ($\alpha = 2 > 1$). Par le théorème des équivalents, $\sum u_n$ **converge**.

**2.** Le dénominateur se factorise : $n(n^2-1) = (n+1)n(n-1)$. En multipliant par chaque facteur et en évaluant en sa racine ($n = -1$, $0$, $1$) :
$$u_n = \frac{1/2}{n+1} + \frac{-3}{n} + \frac{5/2}{n-1}$$
(Contrôle : $\frac{1}{2} - 3 + \frac{5}{2} = 0$, cohérent avec $u_n = O(1/n^2)$.)

**3.** Pour $n \geq 2$, la somme partielle s'écrit, après changement d'indice :
$$\sum_{k=2}^{n} u_k = \frac{1}{2}\sum_{k=3}^{n+1}\frac{1}{k} - 3\sum_{k=2}^{n}\frac{1}{k} + \frac{5}{2}\sum_{k=1}^{n-1}\frac{1}{k}$$
Les termes $\frac{1}{k}$ pour $3 \leq k \leq n-1$ ont pour coefficient total $\frac{1}{2} - 3 + \frac{5}{2} = 0$ et disparaissent. Il reste :
$$\sum_{k=2}^{n} u_k = \frac{1}{2}\left(\frac{1}{n} + \frac{1}{n+1}\right) - 3\left(\frac{1}{2} + \frac{1}{n}\right) + \frac{5}{2}\left(1 + \frac{1}{2}\right) = \frac{9}{4} + O\left(\frac{1}{n}\right)$$
En passant à la limite $n \to +\infty$ :
$$\sum_{n=2}^{+\infty} u_n = \frac{9}{4}$$

> **Erreur corrigée :** dans la première ligne du calcul, le corrigé d'origine écrit $\frac{5}{2}\sum_{k=2}^{n}\frac{1}{k+1}$ au lieu de $\frac{5}{2}\sum_{k=2}^{n}\frac{1}{k-1}$ ; la suite du calcul utilise bien $\frac{1}{k-1}$.

## Exercice 3 : Nature de trois séries

**Énoncé.** (9 pts) Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\in\mathbb{N}}\frac{(-1)^n\sqrt n}{n^2+1}$
2. $\displaystyle\sum_{n\geq 1}\frac{a^{n+1}}{n}$, $a \in \mathbb{R}$
3. $\displaystyle\sum_{n\geq 2}(-1)^n\ln\left(\frac{n+1}{n-1}\right)$

**Correction.** On note $u_n$ le terme général des séries.

**1.** $|u_n| = \frac{\sqrt n}{n^2+1} \underset{+\infty}{\sim} \frac{1}{n^{3/2}}$, terme d'une série de Riemann convergente ($\alpha = \frac{3}{2} > 1$). Par le théorème des équivalents, $\sum |u_n|$ converge : la série $\sum u_n$ **converge absolument**. (On aurait aussi pu utiliser le théorème spécial des séries alternées, en justifiant rigoureusement que $(|u_n|)$ décroît vers $0$.)

**2.** Pour $a = 0$, c'est la série nulle, convergente. Pour $a \neq 0$ et $n \geq 1$, $u_n \neq 0$ et la règle de d'Alembert donne
$$\left|\frac{u_{n+1}}{u_n}\right| = |a|\,\frac{n}{n+1} \xrightarrow[n\to+\infty]{} |a|$$
On distingue quatre cas :

- si $|a| < 1$, la série est **absolument convergente** ;
- si $|a| > 1$, $|u_n| \to +\infty$ et la série **diverge grossièrement** ;
- si $a = 1$, c'est la série harmonique, **divergente** ;
- si $a = -1$, $u_n = \frac{(-1)^{n+1}}{n}$ : série harmonique alternée, **convergente** (TSSA).

**3.** Pour $n \geq 2$, $\frac{n+1}{n-1} = 1 + \frac{2}{n-1} > 1$, donc $\ln\left(1 + \frac{2}{n-1}\right) > 0$ : la série est alternée, avec $|u_n| = \ln(v_n)$ où $v_n = 1 + \frac{2}{n-1}$. La suite $(v_n)_{n\geq 2}$ est décroissante, car
$$v_{n+1} - v_n = \frac{2}{n} - \frac{2}{n-1} = 2\left(\frac{1}{n} - \frac{1}{n-1}\right) < 0$$
et tend vers $1$. Comme $\ln$ est croissante et continue sur $\mathbb{R}_+^*$, la suite $(|u_n|)$ est décroissante de limite $\ln 1 = 0$. Par le théorème spécial des séries alternées, la série **converge**.

> **Note :** le corrigé d'origine écrit $(v_n)_{n\geq 1}$ et $\sum_{n\geq 1} u_n$ ; le terme n'est défini que pour $n \geq 2$.

## Exercice 4 : Équivalent de la somme des carrés

**Énoncé.** (4 pts) On considère la série de terme général $u_n = n^2$ et on note $(S_n)$ sa suite de sommes partielles : $S_n = \sum_{k=1}^{n} u_k$.

1. Montrer que pour tout $n \geq 1$, $\displaystyle\int_0^n t^2\,dt \leq S_n \leq \int_1^{n+1} t^2\,dt$.
2. En déduire que $S_n$ est équivalent à $\frac{1}{3}n^3$ lorsque $n \to +\infty$.

**Correction.**

**1.** La fonction $x \mapsto x^2$ est croissante sur $\mathbb{R}_+$. On en déduit que pour tout $k \geq 1$ :
$$\int_{k-1}^{k} x^2\,dx \leq u_k \leq \int_k^{k+1} x^2\,dx$$
(faire un dessin : aires sous la courbe et rectangles de largeur $1$). En sommant pour $k$ allant de $1$ à $n$, avec la relation de Chasles :
$$\int_0^n x^2\,dx \leq S_n \leq \int_1^{n+1} x^2\,dx$$

**2.** On calcule les intégrales :
$$\int_0^n x^2\,dx = \frac{n^3}{3}, \qquad \int_1^{n+1} x^2\,dx = \frac{(n+1)^3 - 1}{3}$$
Quand $n \to +\infty$, $\frac{1}{3}\big((n+1)^3 - 1\big) \sim \frac{1}{3}n^3$. En divisant l'encadrement par $\frac{n^3}{3}$, les deux bornes tendent vers $1$ : par encadrement, $S_n \sim \frac{1}{3}n^3$. (On peut vérifier avec la formule exacte $S_n = \frac{n(n+1)(2n+1)}{6}$.)
