---
source: DS2-2023-2024-V2_Series-DS_P2S1_DMaths.pdf, page 1 (scan)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 2 (2023/2024, vendredi 1 décembre) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Convergence et intégrale d'une suite de fonctions

**Énoncé.** On considère la suite $(f_n)_{n\geq 0}$ définie sur $[0,1]$ par
$$f_n(x) = \frac{n\left(3x^3 - \frac{7}{4}x\right)e^{4x}}{2xn+1}$$

1. Montrer que la suite $(f_n)$ converge simplement vers une limite $f$ à déterminer.
2. Montrer que la suite $(f_n)$ converge uniformément sur tout intervalle $[a,1]$ avec $a \in \,]0,1[$. A-t-on convergence uniforme sur $[0,1]$ ?
3. Tout en démontrant, trouver une constante explicite $C > 0$ telle que pour tout $x \in [0,1]$ on a $|f_n(x) - f(x)| \leq C$.
4. Déduire des questions précédentes la nature de la suite $(u_n)_{n\geq 0}$ définie par $\forall n \in \mathbb{N},\ u_n = \int_0^1 f_n(x)\,dx$. Vous devez justifier votre réponse.
5. Si vous montrez que $u$ est convergente, que vaut sa limite simplifiée ?

**Correction.**

> **Complément :** le sujet n'a pas de corrigé officiel ; toute la correction est rédigée pour cette transcription.

On écrit $3x^3 - \frac{7}{4}x = x\,h(x)$ avec $h(x) = 3x^2 - \frac{7}{4}$, de sorte que $f_n(x) = \dfrac{nx}{2nx+1}\,h(x)e^{4x}$.

**1.** Pour $x = 0$, $f_n(0) = 0$. Pour $x \in \,]0, 1]$, $\frac{nx}{2nx+1} \to \frac{1}{2}$, donc $(f_n)$ converge simplement vers
$$f(x) = \begin{cases} \dfrac{1}{2}\left(3x^2 - \dfrac{7}{4}\right)e^{4x} & \text{si } x \in \,]0, 1] \\ 0 & \text{si } x = 0 \end{cases}$$

**2.** Pour $x \in \,]0, 1]$ :
$$f_n(x) - f(x) = h(x)e^{4x}\left(\frac{nx}{2nx+1} - \frac{1}{2}\right) = -\frac{h(x)e^{4x}}{2(2nx+1)}$$
Sur $[0, 1]$, $3x^2 - \frac{7}{4} \in \left[-\frac{7}{4}, \frac{5}{4}\right]$, donc $|h(x)| \leq \frac{7}{4}$, et $e^{4x} \leq e^4$. Pour $x \in [a, 1]$, $2nx + 1 \geq 2na + 1$, d'où
$$\sup_{x\in[a,1]}|f_n(x) - f(x)| \leq \frac{7e^4}{8(2na+1)} \xrightarrow[n\to+\infty]{} 0$$
La convergence est **uniforme sur $[a, 1]$**.

Sur $[0, 1]$ : chaque $f_n$ est continue, mais $f$ ne l'est pas en $0$, car $\lim_{x\to 0^+} f(x) = -\frac{7}{8} \neq 0 = f(0)$. Une limite uniforme de fonctions continues étant continue, il n'y a **pas convergence uniforme sur $[0, 1]$**.

**3.** D'après le calcul du 2., pour $x \in \,]0, 1]$, $|f_n(x) - f(x)| = \frac{|h(x)|e^{4x}}{2(2nx+1)} \leq \frac{7}{4}\cdot\frac{e^4}{2} = \frac{7e^4}{8}$ (car $2nx + 1 \geq 1$), et pour $x = 0$ l'écart est nul. La constante $C = \frac{7e^4}{8}$ convient.

**4.** $f$ est continue sur $]0, 1]$ et bornée, donc intégrable sur $[0, 1]$ (sa valeur en $0$ ne compte pas) ; notons $I = \int_0^1 f$. Soit $a \in \,]0, 1[$. En coupant l'intégrale en $a$ :
$$|u_n - I| \leq \int_0^a |f_n - f| + \int_a^1 |f_n - f| \leq Ca + (1 - a)\sup_{[a,1]}|f_n - f|$$
Le second terme tend vers $0$ d'après 2. Donc pour tout $\varepsilon > 0$, en choisissant $a = \frac{\varepsilon}{2C}$ (si $< 1$), puis $n$ assez grand pour que le second terme soit $\leq \frac{\varepsilon}{2}$, on obtient $|u_n - I| \leq \varepsilon$. La suite $(u_n)$ **converge** vers $I = \int_0^1 f(x)\,dx$.

(La convergence n'étant pas uniforme sur $[0, 1]$, on ne peut pas appliquer directement le théorème d'interversion : c'est la borne $C$ de la question 3 qui contrôle le morceau $[0, a]$.)

**5.** Par intégration par parties (deux fois), une primitive de $x^2e^{4x}$ est $e^{4x}\left(\frac{x^2}{4} - \frac{x}{8} + \frac{1}{32}\right)$, donc
$$\int_0^1 x^2e^{4x}\,dx = \frac{5e^4 - 1}{32}, \qquad \int_0^1 e^{4x}\,dx = \frac{e^4 - 1}{4}$$
Ainsi
$$\int_0^1\left(3x^2 - \frac{7}{4}\right)e^{4x}\,dx = \frac{15e^4 - 3}{32} - \frac{14e^4 - 14}{32} = \frac{e^4 + 11}{32}$$
et
$$\lim_{n\to+\infty} u_n = \frac{1}{2}\cdot\frac{e^4 + 11}{32} = \frac{e^4 + 11}{64} \approx 1{,}025$$

## Exercice 2 : Suite de fonctions nᵃ xⁿ (1 − x)

**Énoncé.** Soit $a \geq 0$. On définit la suite de fonctions $(f_n)$ sur $[0,1]$ par $f_n(x) = n^a x^n (1-x)$.

1. Montrer que la suite $(f_n)$ converge simplement vers $0$ sur $[0,1]$.
2. Pour tout $n \in \mathbb{N}$ calculer $\|f_n\|_\infty$ en donnant une expression simplifiée en termes de $a$ et de $n$.
3. Trouver l'ensemble des valeurs de $a$ telles que la suite $(f_n)_{n\geq 0}$ converge uniformément.

**Correction.**

**1.** $f_n(1) = 0$. Pour $x \in [0, 1[$, $n^ax^n = e^{a\ln n + n\ln x} \to 0$ (croissances comparées, $\ln x < 0$ ; et $f_n(0) = 0$ pour $n \geq 1$). Donc $f_n(x) \to 0$ pour tout $x \in [0, 1]$.

**2.** Pour $n \geq 1$, $f_n \geq 0$ et $f_n'(x) = n^a x^{n-1}\big(n(1 - x) - x\big) = n^a x^{n-1}\big(n - (n+1)x\big)$ : $f_n$ croît sur $\left[0, \frac{n}{n+1}\right]$ et décroît ensuite. Donc
$$\|f_n\|_\infty = f_n\left(\frac{n}{n+1}\right) = n^a\left(\frac{n}{n+1}\right)^n\frac{1}{n+1} = \frac{n^a}{n+1}\left(1 + \frac{1}{n}\right)^{-n}$$
(Pour $n = 0$, $f_0(x) = 1 - x$ et $\|f_0\|_\infty = 1$.)

**3.** $\left(1 + \frac{1}{n}\right)^{-n} \to e^{-1}$ et $\frac{n^a}{n+1} \sim n^{a-1}$, donc $\|f_n\|_\infty \sim \frac{n^{a-1}}{e}$. Cette quantité tend vers $0$ si et seulement si $a < 1$ (elle tend vers $\frac{1}{e}$ si $a = 1$ et vers $+\infty$ si $a > 1$). La convergence est uniforme sur $[0, 1]$ **si et seulement si $a \in [0, 1[$**.

## Exercice 3 : Suite de fonctions à support dans [0 ; 1/n]

**Énoncé.** Soit $(f_n)$ la suite de fonctions définie sur $[0,1]$ par $f_n(x) = n^2x(1-nx)$ si $x \in [0, 1/n]$ et $f_n(x) = 0$ sinon.

1. Étudier la limite simple de la suite $(f_n)_{n\geq 1}$.
2. Calculer $\int_0^1 f_n(t)\,dt$. Y a-t-il convergence uniforme sur $[0,1]$ ?
3. Étudier la convergence uniforme sur $[a,1]$ pour $a \in \,]0,1]$.

**Correction.**

**1.** $f_n(0) = 0$ ; pour $x \in \,]0, 1]$, dès que $n > \frac{1}{x}$, $f_n(x) = 0$. La suite converge simplement vers la **fonction nulle**.

**2.**
$$\int_0^1 f_n(t)\,dt = n^2\int_0^{1/n}(t - nt^2)\,dt = n^2\left(\frac{1}{2n^2} - \frac{1}{3n^2}\right) = \frac{1}{6}$$
Si la convergence était uniforme sur le segment $[0, 1]$, on aurait $\int_0^1 f_n \to 0$ : ce n'est pas le cas, donc il n'y a **pas convergence uniforme** sur $[0, 1]$. (D'ailleurs $\max f_n = f_n\left(\frac{1}{2n}\right) = \frac{n}{4} \to +\infty$.)

**3.** Soit $a \in \,]0, 1]$. Pour $n > \frac{1}{a}$, $f_n$ est nulle sur $[a, 1]$ (car $\frac{1}{n} < a$) : la convergence est **uniforme** sur $[a, 1]$.
