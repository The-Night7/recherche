---
source: DS1-2024-2025-V1_Series-DS_P2S1_DMaths.pdf, page 1 (scan)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 1 (2024/2025, mercredi 16 octobre) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits. Barème sur 18 points, complété par 2 points de QCM en cours magistral.

## Exercice 1 : Semi-convergence et comparaison

**Énoncé.** (3 pts)

1. Énoncer la définition d'une série numérique semi-convergente.
2. Soient $\sum u_n$ et $\sum v_n$ deux séries numériques à termes positifs telles que $u_n \underset{+\infty}{=} O(v_n)$. On suppose que la série $\sum v_n$ est convergente. Montrer que la série $\sum u_n$ est convergente.

**Correction.**

> **Complément :** le sujet n'a pas de corrigé officiel ; toute la correction est rédigée pour cette transcription.

**1.** Une série $\sum u_n$ est **semi-convergente** si elle est convergente sans être absolument convergente : $\sum u_n$ converge et $\sum |u_n|$ diverge. (Exemple : $\sum \frac{(-1)^n}{n}$.)

**2.** Par définition de $u_n = O(v_n)$, il existe $C > 0$ et $n_0 \in \mathbb{N}$ tels que pour tout $n \geq n_0$, $0 \leq u_n \leq C v_n$. Pour $N \geq n_0$ :
$$\sum_{n=n_0}^{N} u_n \leq C\sum_{n=n_0}^{N} v_n \leq C\sum_{n=n_0}^{+\infty} v_n$$
car les $v_n$ sont positifs et $\sum v_n$ converge. La suite des sommes partielles de $\sum u_n$ est croissante (termes positifs) et majorée : elle converge. Donc $\sum u_n$ **converge**.

## Exercice 2 : Nature de trois séries

**Énoncé.** (6 pts) Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\geq 0} \ln\left(1+\frac{2}{n^2+1}\right)$
2. $\displaystyle\sum_{n\geq 1} \frac{n^{\ln(n)}}{n!}$
3. $\displaystyle\sum_{n\geq 2} \frac{1}{\sqrt{n^2-1}} - \frac{1}{\sqrt{n^2+1}}$

**Correction.**

**1.** $\frac{2}{n^2+1} \to 0$, donc $\ln\left(1 + \frac{2}{n^2+1}\right) \sim \frac{2}{n^2+1} \sim \frac{2}{n^2}$, termes positifs. Par comparaison avec la série de Riemann $\sum \frac{1}{n^2}$ ($\alpha = 2 > 1$), la série **converge**.

**2.** $u_n = \frac{n^{\ln n}}{n!} = \frac{e^{(\ln n)^2}}{n!} > 0$. Règle de d'Alembert :
$$\frac{u_{n+1}}{u_n} = \frac{e^{(\ln(n+1))^2 - (\ln n)^2}}{n+1}$$
Or $(\ln(n+1))^2 - (\ln n)^2 = \big(\ln(n+1) - \ln n\big)\big(\ln(n+1) + \ln n\big) = \ln\left(1 + \frac{1}{n}\right)\big(\ln(n+1) + \ln n\big) \sim \frac{2\ln n}{n} \to 0$. Donc l'exponentielle tend vers $1$ et $\frac{u_{n+1}}{u_n} \sim \frac{1}{n+1} \to 0 < 1$ : la série **converge**.

**3.** Pour $n \geq 2$, $\sqrt{n^2-1} < \sqrt{n^2+1}$ donc le terme est positif. En factorisant par $\frac{1}{n}$ et avec $(1+x)^{-1/2} = 1 - \frac{x}{2} + O(x^2)$ :
$$\frac{1}{\sqrt{n^2-1}} - \frac{1}{\sqrt{n^2+1}} = \frac{1}{n}\left[\left(1 - \frac{1}{n^2}\right)^{-1/2} - \left(1 + \frac{1}{n^2}\right)^{-1/2}\right] = \frac{1}{n}\left[\frac{1}{n^2} + O\left(\frac{1}{n^4}\right)\right]$$
Le terme est équivalent à $\frac{1}{n^3}$ : par comparaison avec $\sum \frac{1}{n^3}$, la série **converge**.

## Exercice 3 : Une somme télescopique

**Énoncé.** (4 pts) On considère la série de terme général
$$u_n = \ln\left(\frac{(n+1)^2}{n(n+2)}\right)$$

1. Déterminer la nature de la série $\sum_{n\geq 1} u_n$.
2. Calculer la somme $\displaystyle\sum_{n=1}^{+\infty} u_n$.

**Correction.**

**1.** $\frac{(n+1)^2}{n(n+2)} = \frac{n^2 + 2n + 1}{n^2 + 2n} = 1 + \frac{1}{n(n+2)}$, donc
$$u_n = \ln\left(1 + \frac{1}{n(n+2)}\right) \underset{+\infty}{\sim} \frac{1}{n(n+2)} \sim \frac{1}{n^2}$$
Termes positifs, série de Riemann convergente : $\sum u_n$ **converge**.

**2.** $u_n = 2\ln(n+1) - \ln n - \ln(n+2) = \big(\ln(n+1) - \ln n\big) - \big(\ln(n+2) - \ln(n+1)\big)$. Par télescopage, pour $N \geq 1$ :
$$\sum_{n=1}^{N} u_n = \big(\ln(N+1) - \ln 1\big) - \big(\ln(N+2) - \ln 2\big) = \ln 2 + \ln\left(\frac{N+1}{N+2}\right) \xrightarrow[N\to+\infty]{} \ln 2$$
Donc $\sum_{n=1}^{+\infty} u_n = \ln 2$.

## Exercice 4 : Série (n sin(1/n))^(nᵃ)

**Énoncé.** (5 pts) Soit $a \in \mathbb{R}$. On considère la série numérique de terme général :
$$\forall n \in \mathbb{N}^*,\quad u_n = \left(n\sin\left(\frac{1}{n}\right)\right)^{n^a}$$

1. Donner un développement asymptotique de la suite $\ln(u_n)$ sous la forme $\ln(u_n) = \lambda n^{a-2} + o\left(n^{a-2}\right)$, où $\lambda \in \mathbb{R}$ à déterminer.
2. Déterminer la nature de la série $\sum_{n\geq 1} u_n$ dans le cas où $a < 2$.
3. Montrer que la série $\sum_{n\geq 1} u_n$ converge dans le cas où $a > 2$.

**Correction.** Pour $n \geq 1$, $\frac{1}{n} \in \,]0, 1]$ et $0 < \sin x < x$ pour $x > 0$, donc $n\sin\frac{1}{n} \in \,]0, 1[$ : $u_n > 0$ est bien défini.

**1.** $\sin x = x - \frac{x^3}{6} + O(x^5)$ donne $n\sin\frac{1}{n} = 1 - \frac{1}{6n^2} + O\left(\frac{1}{n^4}\right)$, puis
$$\ln(u_n) = n^a\ln\left(1 - \frac{1}{6n^2} + O\left(\frac{1}{n^4}\right)\right) = n^a\left(-\frac{1}{6n^2} + O\left(\frac{1}{n^4}\right)\right) = -\frac{1}{6}n^{a-2} + o\left(n^{a-2}\right)$$
Donc $\lambda = -\frac{1}{6}$.

**2.** Si $a < 2$, $n^{a-2} \to 0$, donc $\ln(u_n) \to 0$ et $u_n \to 1 \neq 0$ : la série **diverge grossièrement**.

**3.** Si $a > 2$, posons $\delta = a - 2 > 0$. D'après 1, $\ln(u_n) = -\frac{n^\delta}{6}(1 + o(1))$, donc
$$\ln(n^2u_n) = 2\ln n - \frac{n^\delta}{6}(1 + o(1)) = n^\delta\left(\frac{2\ln n}{n^\delta} - \frac{1}{6} + o(1)\right) \xrightarrow[n\to+\infty]{} -\infty$$
car $\frac{\ln n}{n^\delta} \to 0$ (croissances comparées). Ainsi $n^2u_n \to 0$, c'est-à-dire $u_n = o\left(\frac{1}{n^2}\right)$ : par la règle de Riemann ($\alpha = 2 > 1$), la série **converge**.

> **Note :** le cas $a = 2$, non demandé, donne $\ln(u_n) \to -\frac{1}{6}$, donc $u_n \to e^{-1/6} \neq 0$ et la série diverge grossièrement.
