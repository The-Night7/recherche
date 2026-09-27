---
source: DS2-2023-2024-V1_Series-DS_P2S1_DMaths.pdf, page 1 (scan)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 2 (2023/2024, mercredi 29 novembre) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Somme de deux suites uniformément convergentes

**Énoncé.** Soit $(f_n)_{n\in\mathbb{N}}$ et $(g_n)_{n\in\mathbb{N}}$ deux suites d'applications définies sur une partie $D$ de $\mathbb{R}$ et qui convergent uniformément respectivement vers des fonctions $f$ et $g$.

1. Expliciter la définition de « $(f_n)_{n\in\mathbb{N}}$ converge uniformément vers $f$ ».
2. Montrer qu'alors la suite d'applications $(f_n+g_n)_{n\in\mathbb{N}}$ converge uniformément vers la fonction $(f+g)$.

**Correction.**

> **Complément :** le sujet n'a pas de corrigé officiel ; toute la correction est rédigée pour cette transcription.

**1.** $(f_n)$ converge uniformément vers $f$ sur $D$ si
$$\forall \varepsilon > 0,\ \exists N \in \mathbb{N},\ \forall n \geq N,\ \forall x \in D,\quad |f_n(x) - f(x)| \leq \varepsilon$$
Le rang $N$ ne dépend que de $\varepsilon$, pas de $x$. De façon équivalente : $\sup_{x\in D}|f_n(x) - f(x)| \xrightarrow[n\to+\infty]{} 0$.

**2.** Soit $\varepsilon > 0$. Par convergence uniforme de $(f_n)$ et de $(g_n)$, il existe $N_1$ et $N_2$ tels que
$$\forall n \geq N_1,\ \forall x \in D,\ |f_n(x) - f(x)| \leq \frac{\varepsilon}{2} \qquad\text{et}\qquad \forall n \geq N_2,\ \forall x \in D,\ |g_n(x) - g(x)| \leq \frac{\varepsilon}{2}$$
Posons $N = \max(N_1, N_2)$. Pour $n \geq N$ et $x \in D$, par l'inégalité triangulaire :
$$\big|(f_n + g_n)(x) - (f + g)(x)\big| \leq |f_n(x) - f(x)| + |g_n(x) - g(x)| \leq \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$
Donc $(f_n + g_n)$ converge uniformément vers $f + g$ sur $D$.

## Exercice 2 : Suite de fonctions √n arctan(x/n)

**Énoncé.** On pose, pour tout $n \in \mathbb{N}^*$ et $x \in \mathbb{R}$, $f_n(x) := \sqrt{n}\arctan\frac{x}{n}$.

1. Montrer que, pour tout $n \in \mathbb{N}^*$ et tout $x \in \mathbb{R}$, $f_n'(x) = \frac{1}{\sqrt{n}}\cdot\frac{1}{1+\frac{x^2}{n^2}}$. En déduire que la suite de fonctions $(f_n')_{n\in\mathbb{N}^*}$ converge uniformément vers une fonction que l'on déterminera.
2. Montrer que, pour tout $n \in \mathbb{N}^*$ et tout $x \in \mathbb{R}$ : $f_n(x) = \int_0^x f_n'(t)\,dt$. En déduire que $(f_n)_{n\in\mathbb{N}}$ converge uniformément vers la fonction nulle sur tout intervalle borné de $\mathbb{R}$.
3. Montrer que $(f_n)_{n\in\mathbb{N}}$ ne converge pas uniformément sur $\mathbb{R}$.

**Correction.**

**1.** $f_n$ est dérivable sur $\mathbb{R}$ (composée de fonctions dérivables) et, puisque $\arctan' (u) = \frac{1}{1+u^2}$,
$$f_n'(x) = \sqrt n\cdot\frac{1}{n}\cdot\frac{1}{1 + \frac{x^2}{n^2}} = \frac{1}{\sqrt n}\cdot\frac{1}{1 + \frac{x^2}{n^2}}$$
Pour tout $x \in \mathbb{R}$, $0 < f_n'(x) \leq \frac{1}{\sqrt n}$, donc $\sup_{\mathbb{R}}|f_n' - 0| \leq \frac{1}{\sqrt n} \to 0$ : $(f_n')$ converge **uniformément vers la fonction nulle** sur $\mathbb{R}$.

**2.** $f_n$ est de classe $C^1$ et $f_n(0) = \sqrt n\arctan 0 = 0$, donc par le théorème fondamental de l'analyse $f_n(x) = f_n(0) + \int_0^x f_n'(t)\,dt = \int_0^x f_n'(t)\,dt$.

Soit $I$ un intervalle borné, contenu dans $[-A, A]$ avec $A > 0$. Pour $x \in I$ :
$$|f_n(x)| = \left|\int_0^x f_n'(t)\,dt\right| \leq |x|\cdot\sup_{\mathbb{R}}|f_n'| \leq \frac{A}{\sqrt n}$$
Donc $\sup_I |f_n| \leq \frac{A}{\sqrt n} \to 0$ : $(f_n)$ converge **uniformément vers $0$** sur $I$.

**3.** Pour tout $n$, $f_n(n) = \sqrt n\arctan 1 = \frac{\pi\sqrt n}{4}$, donc $\sup_{\mathbb{R}}|f_n - 0| \geq \frac{\pi\sqrt n}{4} \to +\infty$. La suite $(f_n)$ converge simplement vers $0$ (d'après 2.) mais **pas uniformément** sur $\mathbb{R}$.

## Exercice 3 : Suite de fonctions « bosse » sur [0 ; 2/n]

**Énoncé.** Soit $(f_n)_{n\geq 2}$ la suite de fonctions définie sur $[0,1]$ par :
$$f_n(x) = \begin{cases} -n^3x^2 + 2n^2x & \text{si } x \in \left[0, \frac{2}{n}\right] \\ 0 & \text{si } x \in \left[\frac{2}{n}, 1\right] \end{cases}$$

1. Étudier la convergence simple de cette suite, vers une fonction que l'on déterminera.
2. Calculer $\lim_{n\to\infty} \int_0^1 f_n(t)\,dt$.
3. Est-ce que $(f_n)_{n\geq 2}$ converge uniformément ?
4. Montrer que $(f_n)_{n\geq 2}$ converge uniformément sur $[a,1]$ pour $a \in \,]0,1[$.

**Correction.** Sur $[0, \frac{2}{n}]$, $f_n(x) = n^2x(2 - nx) \geq 0$, et $f_n\left(\frac{2}{n}\right) = 0$ : les deux expressions coïncident en $\frac{2}{n}$ et $f_n$ est continue.

**1.** $f_n(0) = 0$. Soit $x \in \,]0, 1]$ : dès que $n > \frac{2}{x}$, on a $x > \frac{2}{n}$ donc $f_n(x) = 0$. Ainsi $(f_n)$ converge simplement vers la **fonction nulle** sur $[0, 1]$.

**2.**
$$\int_0^1 f_n(t)\,dt = \int_0^{2/n}\left(2n^2t - n^3t^2\right)dt = n^2\cdot\frac{4}{n^2} - n^3\cdot\frac{8}{3n^3} = 4 - \frac{8}{3} = \frac{4}{3}$$
L'intégrale est constante : $\lim_{n\to\infty}\int_0^1 f_n(t)\,dt = \frac{4}{3}$.

**3.** Non. Si $(f_n)$ convergeait uniformément vers $0$ sur le segment $[0, 1]$, le théorème d'interversion limite-intégrale donnerait $\int_0^1 f_n \to 0 \neq \frac{4}{3}$. (Directement : $f_n$ atteint son maximum en $x = \frac{1}{n}$, où $f_n\left(\frac{1}{n}\right) = n \to +\infty$.)

**4.** Soit $a \in \,]0, 1[$. Pour $n > \frac{2}{a}$, $\frac{2}{n} < a$, donc $f_n$ est nulle sur $[a, 1]$ et $\sup_{[a,1]}|f_n| = 0$. La convergence vers $0$ est **uniforme** sur $[a, 1]$.
