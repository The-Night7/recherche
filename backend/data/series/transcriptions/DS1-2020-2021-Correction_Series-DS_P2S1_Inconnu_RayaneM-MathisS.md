---
source: DS1-2020-2021-Correction_Series-DS_P2S1_Inconnu_RayaneM-MathisS.pdf, pages 1 à 9 (corrigé manuscrit avec barème ; énoncés : DS1-2020-2021_Series-DS_P2S1_KGuezguez-AElJanati-AHajej.pdf, pages 1 et 2)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (novembre 2020) (corrigé)

Devoir du jeudi 5 novembre 2020 (A. El Janati, K. Guezguez, A. Hajej). Durée 1 h 30, appareils électroniques et documents interdits. Barème du corrigé : $4 + 3 + 4 + 5 + 5{,}5$ points.

## Exercice 1 : Nature de quatre séries

**Énoncé.** (4 points) Préciser la nature de chacune des séries suivantes :
$$(1)\ \sum_{n\geq 1} n\sin\left(\frac{1}{n}\right) \qquad (2)\ \sum_{n\geq 1}\frac{1}{\sqrt{n(n + \ln n)}}$$
$$(3)\ \sum_{n\geq 2}\frac{1}{n\ln(n)} \qquad (4)\ \sum_{n\geq 1}\left(e - \left(1 + \frac{1}{n}\right)^n\right)$$

**Correction.**

**(1)** $n\sin\left(\frac{1}{n}\right) \underset{+\infty}{\sim} n\cdot\frac{1}{n} = 1$, donc le terme général tend vers $1 \neq 0$ : la série **diverge grossièrement**.

**(2)** $\frac{1}{\sqrt{n(n + \ln n)}} = \frac{1}{n\sqrt{1 + \frac{\ln n}{n}}} \underset{+\infty}{\sim} \frac{1}{n}$. Les termes sont positifs et la série de Riemann $\sum \frac{1}{n}$ diverge : par le théorème des équivalents, la série **diverge**.

**(3)** La fonction $f : x \mapsto \frac{1}{x\ln x}$ est positive et décroissante sur $[2, +\infty[$ (produit de deux fonctions positives croissantes au dénominateur). Pour $n \geq 2$ et $x \in [n, n+1]$, $f(x) \leq f(n)$, donc
$$\frac{1}{n\ln n} \geq \int_n^{n+1}\frac{dx}{x\ln x}$$
En sommant de $n = 2$ à $N$, et comme une primitive de $f$ est $\ln(\ln x)$ :
$$S_N = \sum_{n=2}^{N}\frac{1}{n\ln n} \geq \int_2^{N+1}\frac{dx}{x\ln x} = \ln\big(\ln(N+1)\big) - \ln(\ln 2) \xrightarrow[N\to+\infty]{} +\infty$$
Les sommes partielles tendent vers $+\infty$ : la série **diverge** (série de Bertrand).

**(4)** On écrit $\left(1 + \frac{1}{n}\right)^n = e^{n\ln(1 + 1/n)}$ et
$$n\ln\left(1 + \frac{1}{n}\right) = n\left(\frac{1}{n} - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right)\right) = 1 - \frac{1}{2n} + o\left(\frac{1}{n}\right)$$
donc
$$\left(1 + \frac{1}{n}\right)^n = e\cdot e^{-\frac{1}{2n} + o(1/n)} = e\left(1 - \frac{1}{2n} + o\left(\frac{1}{n}\right)\right)$$
et $u_n = e - \left(1 + \frac{1}{n}\right)^n \underset{+\infty}{\sim} \frac{e}{2n} > 0$. La série $\sum \frac{1}{n}$ diverge : par équivalence, la série **diverge**.

> **Erreur corrigée :** le corrigé d'origine donne l'équivalent $\frac{1}{2n}$ au lieu de $\frac{e}{2n}$ ; la conclusion est la même.

## Exercice 2 : Vrai ou faux

**Énoncé.** (3 points) Soit $\sum_{n\geq 0} u_n$ une série à termes réels strictement positifs. Les affirmations suivantes sont-elles vraies ou fausses ?

1. Les séries de terme général $u_n$ et $\sqrt{u_n}$ respectivement sont de même nature.
2. Les séries de terme général $u_n$ et $\ln(1 + u_n)$ respectivement sont de même nature.

Justifier vos réponses : si l'affirmation est vraie, en donner une démonstration et si elle est fausse, produire un contre-exemple.

**Correction.**

1. **Faux.** Contre-exemple : $u_n = \frac{1}{n^2}$ ($n \geq 1$). La série $\sum \frac{1}{n^2}$ converge (Riemann, $\alpha = 2 > 1$) mais $\sum \sqrt{u_n} = \sum \frac{1}{n}$ diverge (Riemann, $\alpha = 1 \leq 1$).

2. **Vrai.** Deux cas.
    - Si $u_n$ ne tend pas vers $0$ : $\sum u_n$ diverge grossièrement. Alors $\ln(1 + u_n)$ ne tend pas vers $0$ non plus (sinon $u_n = e^{\ln(1+u_n)} - 1 \to 0$), et $\sum \ln(1+u_n)$ diverge grossièrement.
    - Si $u_n \to 0$ : $\ln(1 + u_n) \underset{+\infty}{\sim} u_n$, et les deux suites sont positives. Par le théorème des équivalents, les deux séries sont de même nature.

> **Complément :** le corrigé d'origine ne traite que le cas $u_n \to 0$ ; le cas où $u_n$ ne tend pas vers $0$ a été ajouté.

## Exercice 3 : Somme d'une série rationnelle

**Énoncé.** (3,5 points) On considère la suite définie pour tout entier naturel $n \geq 2$ par $u_n = \dfrac{n}{(n^2-1)^2}$.

1. Étudier la convergence de la série numérique $\sum_{n\geq 2} u_n$.
2. Décomposer le terme général $u_n$ en fonction de $\frac{1}{(n+1)^2}$ et $\frac{1}{(n-1)^2}$.
3. En déduire la somme de la série $\sum_{n\geq 2} u_n$.

**Correction.**

**1.** $0 < u_n \underset{+\infty}{\sim} \frac{n}{n^4} = \frac{1}{n^3}$ et la série de Riemann $\sum \frac{1}{n^3}$ converge ($\alpha = 3 > 1$) : par le théorème des équivalents, $\sum u_n$ **converge**.

**2.** Soit $F(X) = \frac{X}{(X^2-1)^2} = \frac{X}{(X-1)^2(X+1)^2}$. On cherche
$$F(X) = \frac{a}{X-1} + \frac{b}{(X-1)^2} + \frac{c}{X+1} + \frac{d}{(X+1)^2}$$

- $b = (X-1)^2F(X)\big|_{X=1} = \frac{1}{4}$ et $d = (X+1)^2F(X)\big|_{X=-1} = \frac{-1}{4}$ ;
- $\lim_{x\to+\infty} xF(x) = 0$ donne $a + c = 0$ ;
- $F(0) = 0$ donne $-a + b + c + d = 0$, soit $c - a = 0$.

Donc $a = c = 0$ et
$$u_n = \frac{1}{4}\cdot\frac{1}{(n-1)^2} - \frac{1}{4}\cdot\frac{1}{(n+1)^2}$$
(Vérification : $(n+1)^2 - (n-1)^2 = 4n$.)

**3.** Pour $n \geq 2$, en décalant les indices :
$$S_n = \sum_{k=2}^{n} u_k = \frac{1}{4}\sum_{k=1}^{n-1}\frac{1}{k^2} - \frac{1}{4}\sum_{k=3}^{n+1}\frac{1}{k^2}$$
Les termes d'indice $3$ à $n-1$ se simplifient :
$$S_n = \frac{1}{4}\left(1 + \frac{1}{4} - \frac{1}{n^2} - \frac{1}{(n+1)^2}\right) = \frac{5}{16} - \frac{1}{4}\left(\frac{1}{n^2} + \frac{1}{(n+1)^2}\right)$$
En faisant tendre $n$ vers $+\infty$ :
$$\sum_{n=2}^{+\infty}\frac{n}{(n^2-1)^2} = \frac{5}{16}$$

## Exercice 4 : Série de Bertrand et comparaison série-intégrale

**Énoncé.** (5 points) On considère la fonction
$$F : [3, +\infty[ \to \mathbb{R}, \quad x \mapsto \ln(\ln x)$$

1. Déterminer $\lim_{x\to+\infty} F(x)$. Quelle est la dérivée $f$ de $F$ ? Montrer que $f$ est décroissante et positive sur $[3, +\infty[$.
2. On considère la série $\sum_{n\geq 3}\frac{1}{n\ln n}$. Soit $S_N$ la somme partielle d'ordre $N$. Encadrer $S_N$ par deux intégrales.
3. En déduire un équivalent de $S_N$.

**Correction.** On note $S_N = \sum_{n=3}^{N}\frac{1}{n\ln n}$ pour $N \geq 3$.

**1.** $\ln x \to +\infty$ quand $x \to +\infty$, donc $F(x) = \ln(\ln x) \to +\infty$. Par dérivation d'une composée,
$$f(x) = F'(x) = \frac{1}{x}\cdot\frac{1}{\ln x} = \frac{1}{x\ln x}$$
Pour $x \geq 3$, $x\ln x > 0$ donc $f(x) > 0$. De plus
$$f'(x) = -\frac{(x\ln x)'}{(x\ln x)^2} = -\frac{\ln x + 1}{(x\ln x)^2} < 0$$
donc $f$ est décroissante sur $[3, +\infty[$.

**2.** *Minoration.* Pour $n \geq 3$ et $x \in [n, n+1]$, $f(x) \leq f(n)$, donc $\int_n^{n+1} f(x)\,dx \leq f(n)$. En sommant de $n = 3$ à $N$ :
$$\int_3^{N+1} f(x)\,dx \leq S_N$$
*Majoration.* Pour $n \geq 4$ et $x \in [n-1, n]$, $f(n) \leq f(x)$, donc $f(n) \leq \int_{n-1}^{n} f(x)\,dx$. En sommant de $n = 4$ à $N$ : $S_N - f(3) \leq \int_3^N f(x)\,dx$. D'où
$$\int_3^{N+1} f(x)\,dx \leq S_N \leq \int_3^{N} f(x)\,dx + \frac{1}{3\ln 3}$$

**3.** Avec la primitive $F$ :
$$\ln(\ln(N+1)) - \ln(\ln 3) \leq S_N \leq \ln(\ln N) - \ln(\ln 3) + \frac{1}{3\ln 3}$$
Or $\ln(N+1) = \ln N + \ln\left(1 + \frac{1}{N}\right)$, donc $\ln(\ln(N+1)) = \ln(\ln N) + \ln\left(1 + \frac{\ln(1 + 1/N)}{\ln N}\right) = \ln(\ln N) + o(1)$. Les deux bornes s'écrivent donc $\ln(\ln N) + O(1)$ ; en divisant par $\ln(\ln N) \to +\infty$, elles tendent toutes deux vers $1$, et par encadrement
$$S_N \underset{+\infty}{\sim} \ln(\ln N)$$
En particulier $S_N \to +\infty$ et la série $\sum \frac{1}{n\ln n}$ diverge.

> **Note :** le corrigé d'origine conclut $S_N \sim \ln(\ln N) - \ln(\ln 3)$, ce qui est équivalent mais moins simple.

## Exercice 5 : Série de logarithmes à deux paramètres

**Énoncé.** (5,5 points) Soit $a$ et $b$ deux réels. On considère la série numérique :
$$\sum_{n\geq 1}\big(\ln(n) + a\ln(n+1) + b\ln(n+2)\big)$$

1. Donner un développement asymptotique du terme général de cette série sous la forme :
$$\ln(n) + a\ln(n+1) + b\ln(n+2) = \alpha\ln(n) + \frac{\beta}{n} + \frac{\gamma}{n^2} + o\left(\frac{1}{n^2}\right)$$
où $\alpha, \beta, \gamma$ sont des réels à déterminer en fonction de $a$ et de $b$.
2. En déduire les valeurs de $a$ et de $b$ pour que la série converge.
3. Pour ces valeurs de $a$ et de $b$, calculer alors $S_N = \sum_{n=1}^{N}\big(\ln(n) + a\ln(n+1) + b\ln(n+2)\big)$.
4. En déduire la somme de la série.

**Correction.** On note $u_n$ le terme général.

**1.** $\ln(n+1) = \ln n + \ln\left(1 + \frac{1}{n}\right)$ et $\ln(n+2) = \ln n + \ln\left(1 + \frac{2}{n}\right)$, avec
$$\ln\left(1 + \frac{1}{n}\right) = \frac{1}{n} - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right), \qquad \ln\left(1 + \frac{2}{n}\right) = \frac{2}{n} - \frac{2}{n^2} + o\left(\frac{1}{n^2}\right)$$
Donc
$$u_n = (1 + a + b)\ln n + \frac{a + 2b}{n} - \frac{\frac{a}{2} + 2b}{n^2} + o\left(\frac{1}{n^2}\right)$$
soit $\alpha = 1 + a + b$, $\beta = a + 2b$, $\gamma = -\left(\frac{a}{2} + 2b\right)$.

**2.**

- Si $\alpha \neq 0$ : $|u_n| \to +\infty$, la série diverge grossièrement.
- Si $\alpha = 0$, c'est-à-dire $b = -1 - a$ : alors $\beta = a - 2 - 2a = -a - 2$ et $\gamma = -\frac{a}{2} + 2 + 2a = \frac{3a}{2} + 2$, donc
$$u_n = \frac{-a-2}{n} + \frac{\frac{3a}{2} + 2}{n^2} + o\left(\frac{1}{n^2}\right)$$
    - si $a \neq -2$ : $u_n \sim \frac{-a-2}{n}$, de signe constant, et $\sum \frac{1}{n}$ diverge : la série diverge ;
    - si $a = -2$ (donc $b = 1$) : $\gamma = -3 + 2 = -1$ et $u_n \sim -\frac{1}{n^2}$, de signe constant ; $\sum \frac{1}{n^2}$ converge, donc la série converge.

Conclusion : la série converge **si et seulement si $a = -2$ et $b = 1$**.

> **Erreur corrigée :** le corrigé d'origine écrit $\gamma = -\left(\frac{3}{2}a - 2\right)$ au lieu de $\frac{3a}{2} + 2$ (erreur de signe) ; il annonce néanmoins le bon équivalent $u_n \sim -\frac{1}{n^2}$. Contrôle direct : $\ln n - 2\ln(n+1) + \ln(n+2) = \ln\left(1 - \frac{1}{(n+1)^2}\right) \sim -\frac{1}{n^2}$.

**3.** Pour $a = -2$, $b = 1$, on regroupe en deux sommes télescopiques :
$$S_N = \sum_{n=1}^{N}\big(\ln n - \ln(n+1)\big) + \sum_{n=1}^{N}\big(\ln(n+2) - \ln(n+1)\big)$$
$$S_N = \big(\ln 1 - \ln(N+1)\big) + \big(\ln(N+2) - \ln 2\big) = \ln\left(\frac{N+2}{N+1}\right) - \ln 2$$

**4.** $\frac{N+2}{N+1} \to 1$, donc
$$\sum_{n=1}^{+\infty}\big(\ln n - 2\ln(n+1) + \ln(n+2)\big) = -\ln 2$$
