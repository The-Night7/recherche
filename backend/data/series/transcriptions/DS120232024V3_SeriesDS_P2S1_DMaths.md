---
source: DS1-2023-2024-V3_Series-DS_P2S1_DMaths.pdf, page 1 (scan)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 1 (2023/2024, mardi 24 octobre, version 3) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Vrai ou faux

**Énoncé.** Déterminer en justifiant si les énoncés suivants sont vrais ou faux :

1. Si la suite $(u_n)$ converge vers $0$ alors la série $\sum u_n$ converge.
2. Si $u_n = v_n - v_{n-1}$ alors $\sum u_n$ et $(v_n)_n$ sont de même nature.
3. Si $\sum u_n$ est convergente alors $u_n \leq \frac{1}{2}$.

**Correction.**

> **Complément :** le sujet n'a pas de corrigé officiel ; toute la correction est rédigée pour cette transcription.

1. **Faux.** $u_n = \frac{1}{n}$ tend vers $0$ mais la série harmonique $\sum \frac{1}{n}$ diverge. (La condition $u_n \to 0$ est nécessaire, pas suffisante.)
2. **Vrai.** Pour $N \geq 1$, la somme partielle est télescopique :
$$\sum_{n=1}^{N} u_n = \sum_{n=1}^{N}(v_n - v_{n-1}) = v_N - v_0$$
Donc les sommes partielles convergent si et seulement si $(v_N)$ converge : la série et la suite sont de même nature.
3. **Faux** tel qu'énoncé (pour tout $n$) : la série de terme $u_0 = 1$, $u_n = 0$ pour $n \geq 1$ converge mais $u_0 > \frac{1}{2}$. L'énoncé est **vrai** « à partir d'un certain rang », car le terme général d'une série convergente tend vers $0$.

## Exercice 2 : Nature de cinq séries

**Énoncé.** Déterminer la nature des séries :

1. $\displaystyle\sum \left(\sin\left(\frac{1}{n}\right)\right)^n$
2. $\displaystyle\sum \frac{n}{2^n}$
3. $\displaystyle\sum \frac{1}{\ln(n^2+1)}$
4. $\displaystyle\sum \left(\exp\left(\cos\left(\frac{1}{n}\right)\right) - \exp\left(\cos\left(\frac{2}{n}\right)\right)\right)$
5. $\displaystyle\sum \left(\frac{n}{n+1}\right)^{n^2}$

**Correction.** Toutes les séries sont prises pour $n \geq 1$.

**1.** $u_n = \left(\sin\frac{1}{n}\right)^n > 0$ et $\sqrt[n]{u_n} = \sin\frac{1}{n} \to 0 < 1$ : par la règle de Cauchy, la série **converge**.

**2.** $u_n = \frac{n}{2^n} > 0$ et $\frac{u_{n+1}}{u_n} = \frac{n+1}{2n} \to \frac{1}{2} < 1$ : par la règle de d'Alembert, la série **converge**.

**3.** $u_n = \frac{1}{\ln(n^2+1)} > 0$. Comme $\ln(n^2 + 1) = 2\ln n + \ln\left(1 + \frac{1}{n^2}\right) \sim 2\ln n$, on a $u_n \sim \frac{1}{2\ln n}$. Or $\frac{n}{2\ln n} \to +\infty$, donc $\frac{1}{2\ln n} \geq \frac{1}{n}$ à partir d'un certain rang : la série $\sum \frac{1}{2\ln n}$ diverge par comparaison avec la série harmonique, et par équivalence $\sum u_n$ **diverge**.

**4.** Quand $n \to +\infty$ :
$$\cos\frac{1}{n} = 1 - \frac{1}{2n^2} + O\left(\frac{1}{n^4}\right), \qquad \cos\frac{2}{n} = 1 - \frac{2}{n^2} + O\left(\frac{1}{n^4}\right)$$
et $e^{1+h} = e\left(1 + h + O(h^2)\right)$ quand $h \to 0$, donc
$$e^{\cos(1/n)} - e^{\cos(2/n)} = e\left(-\frac{1}{2n^2} + \frac{2}{n^2}\right) + O\left(\frac{1}{n^4}\right) = \frac{3e}{2n^2} + O\left(\frac{1}{n^4}\right)$$
Le terme général est équivalent à $\frac{3e}{2n^2} > 0$ : par comparaison avec $\sum \frac{1}{n^2}$, la série **converge**. (On peut aussi remarquer directement que le terme est positif car $\cos\frac{1}{n} > \cos\frac{2}{n}$ pour $n \geq 1$, $\cos$ étant décroissante sur $[0, \pi]$.)

**5.** $u_n > 0$ et $\sqrt[n]{u_n} = \left(\frac{n}{n+1}\right)^n = \left(1 + \frac{1}{n}\right)^{-n} = e^{-n\ln(1 + 1/n)} \to e^{-1} < 1$. Par la règle de Cauchy, la série **converge**.

## Exercice 3 : Deux calculs de sommes

**Énoncé.** Calculer :

1. $\displaystyle\sum_{n\geq 3} \frac{2n-1}{n(n^2-4)}$
2. $\displaystyle\sum_{n\geq 0} \frac{n+1}{n!}$, sachant que $\displaystyle\sum_{n\geq 0}\frac{1}{n!} = e$

**Correction.**

**1.** $\frac{2n-1}{n(n^2-4)} = \frac{2n-1}{n(n-2)(n+2)}$. On décompose en éléments simples : $\frac{2n-1}{n(n-2)(n+2)} = \frac{a}{n} + \frac{b}{n-2} + \frac{c}{n+2}$, avec
$$a = \frac{-1}{(-2)(2)} = \frac{1}{4}, \qquad b = \frac{3}{2\cdot 4} = \frac{3}{8}, \qquad c = \frac{-5}{(-2)(-4)} = -\frac{5}{8}$$
(on multiplie par $n$, $n-2$, $n+2$ et on évalue en $0$, $2$, $-2$). On a bien $a + b + c = 0$, ce qui assure que $u_n = O\left(\frac{1}{n^2}\right)$ (d'ailleurs $u_n \sim \frac{2}{n^2}$) : la série converge.

Notons $H_m = \sum_{k=1}^{m}\frac{1}{k}$. Pour $N \geq 3$ :
$$\sum_{n=3}^{N}\frac{1}{n} = H_N - \frac{3}{2}, \qquad \sum_{n=3}^{N}\frac{1}{n-2} = H_{N-2}, \qquad \sum_{n=3}^{N}\frac{1}{n+2} = H_{N+2} - H_4$$
donc
$$S_N = \frac{1}{4}\left(H_N - \frac{3}{2}\right) + \frac{3}{8}H_{N-2} - \frac{5}{8}\left(H_{N+2} - H_4\right)$$
Comme $\frac{1}{4} + \frac{3}{8} - \frac{5}{8} = 0$, on peut écrire $S_N = \frac{3}{8}(H_{N-2} - H_N) - \frac{5}{8}(H_{N+2} - H_N) - \frac{3}{8} + \frac{5}{8}H_4$, où $H_{N-2} - H_N$ et $H_{N+2} - H_N$ tendent vers $0$. Avec $H_4 = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{25}{12}$ :
$$\sum_{n=3}^{+\infty}\frac{2n-1}{n(n^2-4)} = -\frac{3}{8} + \frac{5}{8}\cdot\frac{25}{12} = -\frac{36}{96} + \frac{125}{96} = \frac{89}{96}$$
(Contrôle numérique : la somme des termes jusqu'à $n = 10^6$ vaut environ $0{,}92708$.)

**2.** Pour $n \geq 1$, $\frac{n}{n!} = \frac{1}{(n-1)!}$, et le terme $n = 0$ de $\sum \frac{n}{n!}$ est nul. Les deux séries convergeant :
$$\sum_{n=0}^{+\infty}\frac{n+1}{n!} = \sum_{n=1}^{+\infty}\frac{1}{(n-1)!} + \sum_{n=0}^{+\infty}\frac{1}{n!} = e + e = 2e$$

## Exercice 4 : Série de logarithmes à deux paramètres

**Énoncé.** Soit $a$ et $b$ deux réels. On considère la série numérique de terme général :
$$\forall n \in \mathbb{N}^*,\quad u_n = \ln(n) + a\ln(n+1) + b\ln(n+2)$$

1. Donner un développement asymptotique du terme général de cette série sous la forme $u_n = \alpha\ln(n) + \frac{\beta}{n} + \frac{\gamma}{n^2} + o\left(\frac{1}{n^2}\right)$, où $\alpha, \beta, \gamma$ sont des réels à déterminer en fonction de $a$ et de $b$.
2. Déterminer les valeurs de $a$ et de $b$ pour que la série converge.
3. Pour ces valeurs de $a$ et de $b$ en cas de convergence, calculer alors $S_N = \sum_{n=1}^{N} u_n$.
4. En déduire la somme de la série.

**Correction.**

**1.** $\ln(n+1) = \ln n + \ln\left(1 + \frac{1}{n}\right)$ et $\ln(n+2) = \ln n + \ln\left(1 + \frac{2}{n}\right)$ avec
$$\ln\left(1 + \frac{1}{n}\right) = \frac{1}{n} - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right), \qquad \ln\left(1 + \frac{2}{n}\right) = \frac{2}{n} - \frac{2}{n^2} + o\left(\frac{1}{n^2}\right)$$
Donc
$$\alpha = 1 + a + b, \qquad \beta = a + 2b, \qquad \gamma = -\frac{a}{2} - 2b$$

**2.**

- Si $\alpha \neq 0$, $|u_n| \to +\infty$ : divergence grossière.
- Si $\alpha = 0$ et $\beta \neq 0$ : $u_n \sim \frac{\beta}{n}$, de signe constant ; la série diverge par comparaison avec la série harmonique.
- Si $\alpha = \beta = 0$ : $u_n = O\left(\frac{1}{n^2}\right)$, la série converge absolument.

La série converge si et seulement si $1 + a + b = 0$ et $a + 2b = 0$, soit **$a = -2$ et $b = 1$**.

**3.** Alors $u_n = \big(\ln n - \ln(n+1)\big) + \big(\ln(n+2) - \ln(n+1)\big)$ et, par télescopage,
$$S_N = -\ln(N+1) + \ln(N+2) - \ln 2 = \ln\left(\frac{N+2}{N+1}\right) - \ln 2$$

**4.** $\sum_{n=1}^{+\infty} u_n = \lim_{N\to+\infty} S_N = -\ln 2$.
