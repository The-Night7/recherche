---
source: DS1-2023-2024-V2_Series-DS_P2S1_DMaths.pdf, page 1 (scan)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 1 (2023/2024, mercredi 25 octobre) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Vrai ou faux

**Énoncé.** Déterminer en justifiant si les énoncés suivants sont vrais ou faux :

1. Si $\sum u_n$ est convergente alors $\sum u_n$ est absolument convergente.
2. Si $u_n = o\left(\frac{1}{n}\right)$ au voisinage de $+\infty$, alors $\sum u_n$ est divergente.
3. Si $\sum u_n$ est convergente alors $u_n \leq \frac{1}{2}$.

**Correction.**

> **Complément :** le sujet n'a pas de corrigé officiel ; toute la correction est rédigée pour cette transcription.

1. **Faux.** $\sum_{n\geq 1}\frac{(-1)^n}{n}$ converge (critère des séries alternées : $\frac{1}{n}$ décroît vers $0$), mais $\sum \left|\frac{(-1)^n}{n}\right| = \sum \frac{1}{n}$ diverge : elle n'est pas absolument convergente.
2. **Faux.** $u_n = \frac{1}{n^2}$ vérifie $u_n = o\left(\frac{1}{n}\right)$, et $\sum \frac{1}{n^2}$ converge (Riemann, $\alpha = 2 > 1$).
3. **Faux** tel qu'énoncé (pour tout $n$) : la série de terme $u_0 = 1$, $u_n = 0$ pour $n \geq 1$ converge (vers $1$) mais $u_0 > \frac{1}{2}$. En revanche, l'énoncé devient **vrai** « à partir d'un certain rang » : si $\sum u_n$ converge, $u_n \to 0$, donc $u_n \leq \frac{1}{2}$ pour $n$ assez grand.

## Exercice 2 : Nature de cinq séries

**Énoncé.** Déterminer la nature des séries suivantes :

1. $\displaystyle\sum \frac{\tan^n\left(\frac{\pi}{7}\right)}{3^{n+2}}$
2. $\displaystyle\sum \frac{2^n}{3^{n-2}}$
3. $\displaystyle\sum \frac{\cos(n)}{n^3+n}$
4. $\displaystyle\sum \frac{1-\cos\left(\frac{1}{n}\right)}{\exp\left(\frac{1}{n}\right)-1}$
5. $\displaystyle\sum (-1)^n \frac{n^3}{n!}$

**Correction.**

**1.** $\frac{\tan^n(\pi/7)}{3^{n+2}} = \frac{1}{9}\left(\frac{\tan(\pi/7)}{3}\right)^n$. Comme $0 < \frac{\pi}{7} < \frac{\pi}{4}$ et que $\tan$ est strictement croissante sur $]-\frac{\pi}{2}, \frac{\pi}{2}[$, $0 < \tan\frac{\pi}{7} < 1$, donc la raison $q = \frac{\tan(\pi/7)}{3} \in \,]0, \frac{1}{3}[$ : série géométrique **convergente**.

**2.** $\frac{2^n}{3^{n-2}} = 9\left(\frac{2}{3}\right)^n$ : série géométrique de raison $\frac{2}{3} \in \,]0, 1[$, **convergente**.

**3.** $\left|\frac{\cos n}{n^3+n}\right| \leq \frac{1}{n^3}$ et $\sum \frac{1}{n^3}$ converge (Riemann, $\alpha = 3 > 1$). La série est **absolument convergente**, donc convergente.

**4.** Pour $n \geq 1$, numérateur et dénominateur sont strictement positifs ($\cos\frac{1}{n} < 1$ et $e^{1/n} > 1$). Quand $n \to +\infty$ :
$$1 - \cos\frac{1}{n} \sim \frac{1}{2n^2}, \qquad e^{1/n} - 1 \sim \frac{1}{n}, \qquad \text{donc}\quad \frac{1 - \cos\frac{1}{n}}{e^{1/n} - 1} \sim \frac{1}{2n}$$
La série harmonique diverge : par équivalence (termes positifs), la série **diverge**.

**5.** Étudions la convergence absolue avec la règle de d'Alembert, pour $a_n = \frac{n^3}{n!}$ ($n \geq 1$) :
$$\frac{a_{n+1}}{a_n} = \frac{(n+1)^3}{(n+1)!}\cdot\frac{n!}{n^3} = \frac{(n+1)^2}{n^3} \xrightarrow[n\to+\infty]{} 0 < 1$$
Donc $\sum a_n$ converge : la série $\sum (-1)^n\frac{n^3}{n!}$ est **absolument convergente**, donc convergente.

## Exercice 3 : Deux calculs de sommes

**Énoncé.** Calculer :

1. $\displaystyle\sum_{n\geq 1} \frac{1}{n(n+1)(n+2)}$
2. $\displaystyle\sum_{n\geq 0} \frac{n^2-2}{n!}$, sachant que $\displaystyle\sum_{n\geq 0}\frac{1}{n!} = e$ (Indication : $n^2-2 = n(n-1)+n-2$)

**Correction.**

**1.** Décomposition en éléments simples :
$$\frac{1}{n(n+1)(n+2)} = \frac{1/2}{n} - \frac{1}{n+1} + \frac{1/2}{n+2} = \frac{1}{2}\left(\frac{1}{n} - \frac{1}{n+1}\right) - \frac{1}{2}\left(\frac{1}{n+1} - \frac{1}{n+2}\right)$$
(coefficients obtenus en multipliant par $n$, $n+1$, $n+2$ puis en évaluant en $0$, $-1$, $-2$). Par télescopage :
$$\sum_{k=1}^{n}\frac{1}{k(k+1)(k+2)} = \frac{1}{2}\left(1 - \frac{1}{n+1}\right) - \frac{1}{2}\left(\frac{1}{2} - \frac{1}{n+2}\right) \xrightarrow[n\to+\infty]{} \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$$
Donc $\sum_{n=1}^{+\infty}\frac{1}{n(n+1)(n+2)} = \frac{1}{4}$.

**2.** Les séries $\sum \frac{n(n-1)}{n!}$, $\sum \frac{n}{n!}$ et $\sum \frac{1}{n!}$ convergent (on le voit ci-dessous), donc on peut séparer :
$$\sum_{n=0}^{+\infty}\frac{n^2-2}{n!} = \sum_{n=0}^{+\infty}\frac{n(n-1)}{n!} + \sum_{n=0}^{+\infty}\frac{n}{n!} - 2\sum_{n=0}^{+\infty}\frac{1}{n!}$$
Les termes $n = 0, 1$ de la première somme et $n = 0$ de la deuxième sont nuls, et pour $n \geq 2$, $\frac{n(n-1)}{n!} = \frac{1}{(n-2)!}$, pour $n \geq 1$, $\frac{n}{n!} = \frac{1}{(n-1)!}$. Donc
$$\sum_{n=0}^{+\infty}\frac{n^2-2}{n!} = \sum_{m=0}^{+\infty}\frac{1}{m!} + \sum_{m=0}^{+\infty}\frac{1}{m!} - 2e = e + e - 2e = 0$$

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
Donc $u_n = \alpha\ln n + \frac{\beta}{n} + \frac{\gamma}{n^2} + o\left(\frac{1}{n^2}\right)$ avec
$$\alpha = 1 + a + b, \qquad \beta = a + 2b, \qquad \gamma = -\frac{a}{2} - 2b$$

**2.**

- Si $\alpha \neq 0$, $|u_n| \to +\infty$ : divergence grossière.
- Si $\alpha = 0$ et $\beta \neq 0$ : $u_n \sim \frac{\beta}{n}$, de signe constant à partir d'un certain rang ; la série harmonique diverge, donc $\sum u_n$ diverge.
- Si $\alpha = \beta = 0$ : $u_n = \frac{\gamma}{n^2} + o\left(\frac{1}{n^2}\right) = O\left(\frac{1}{n^2}\right)$, donc $\sum u_n$ converge absolument.

La série converge si et seulement si $1 + a + b = 0$ et $a + 2b = 0$, c'est-à-dire **$a = -2$ et $b = 1$** (et alors $\gamma = 1 - 2 = -1$).

**3.** Pour $a = -2$, $b = 1$ : $u_n = \big(\ln n - \ln(n+1)\big) + \big(\ln(n+2) - \ln(n+1)\big)$ et, par télescopage,
$$S_N = \big(\ln 1 - \ln(N+1)\big) + \big(\ln(N+2) - \ln 2\big) = \ln\left(\frac{N+2}{N+1}\right) - \ln 2$$

**4.** $\frac{N+2}{N+1} \to 1$, donc $\sum_{n=1}^{+\infty} u_n = -\ln 2$.
