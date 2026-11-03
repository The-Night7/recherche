---
source: DS1-2023-2024-V1_Series-DS_P2S1_DMaths.pdf, page 1 (scan)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 1 (2023/2024, mardi 24 octobre) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Série géométrique

**Énoncé.** Soit $q \in \mathbb{R}$, à quelle condition sur $q$ la série $\sum_{n\geq 0} q^n$ converge-t-elle ? Le démontrer, et calculer sa valeur.

**Correction.**

> **Complément :** le sujet n'a pas de corrigé officiel ; toute la correction est rédigée pour cette transcription.

**La série converge si et seulement si $|q| < 1$, et alors $\sum_{n=0}^{+\infty} q^n = \frac{1}{1-q}$.**

- Si $|q| \geq 1$ : $|q^n| = |q|^n \geq 1$ pour tout $n$, donc $q^n$ ne tend pas vers $0$ et la série **diverge grossièrement**.
- Si $|q| < 1$ : on a $q \neq 1$ et, pour tout $N$,
$$S_N = \sum_{n=0}^{N} q^n = \frac{1 - q^{N+1}}{1 - q}$$
(on le vérifie en développant $(1 - q)S_N = S_N - qS_N = 1 - q^{N+1}$, somme télescopique). Comme $|q| < 1$, $q^{N+1} \to 0$, donc $S_N \to \frac{1}{1-q}$ : la série **converge** et sa somme vaut $\frac{1}{1-q}$.

## Exercice 2 : Une somme télescopique

**Énoncé.** L'objectif de cet exercice est de calculer
$$S = \sum_{k=1}^{+\infty} \frac{2k^2-1}{k^2(k+1)^2}$$

1. Montrer que l'égalité ci-dessus définit bien un réel $S \in \mathbb{R}$.
2. Montrer que $\dfrac{2k^2-1}{k^2(k+1)^2} = \dfrac{2k-1}{k^2} - \dfrac{2k+1}{(k+1)^2}$.
3. En déduire la valeur de $S \in \mathbb{R}$.

**Correction.**

**1.** Pour $k \geq 1$, $2k^2 - 1 > 0$ : la série est à termes positifs. De plus
$$\frac{2k^2-1}{k^2(k+1)^2} \underset{+\infty}{\sim} \frac{2k^2}{k^4} = \frac{2}{k^2}$$
et $\sum \frac{1}{k^2}$ converge (Riemann, $\alpha = 2 > 1$). Par le théorème des équivalents, la série converge : $S$ est bien un réel.

**2.** On réduit au même dénominateur $k^2(k+1)^2$ :
$$(2k-1)(k+1)^2 - (2k+1)k^2 = (2k^3 + 4k^2 + 2k - k^2 - 2k - 1) - (2k^3 + k^2) = 2k^2 - 1$$
d'où l'égalité.

**3.** Posons $v_k = \frac{2k-1}{k^2}$ ; d'après 2., le terme général vaut $v_k - v_{k+1}$. La somme partielle est télescopique :
$$\sum_{k=1}^{n}\frac{2k^2-1}{k^2(k+1)^2} = v_1 - v_{n+1} = 1 - \frac{2n+1}{(n+1)^2} \xrightarrow[n\to+\infty]{} 1$$
Donc $S = 1$.

## Exercice 3 : Nature de quatre séries

**Énoncé.** Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\geq 1} n\ln\left(1+\frac{1}{n}\right) - \cos\left(\frac{1}{\sqrt{n}}\right)$
2. $\displaystyle\sum_{n\geq 1} \ln\left(1+\frac{(-1)^n}{2n+1}\right)$
3. $\displaystyle\sum_{n\geq 1} \left(\cos\left(\frac{1}{n}\right)\right)^{n^3}$
4. $\displaystyle\sum_{n\geq 0} \left(\frac{4n+1}{3n+2}\right)^n$

**Correction.**

**1.** Développements limités quand $n \to +\infty$ :
$$n\ln\left(1+\frac{1}{n}\right) = 1 - \frac{1}{2n} + \frac{1}{3n^2} + o\left(\frac{1}{n^2}\right)$$
$$\cos\left(\frac{1}{\sqrt n}\right) = 1 - \frac{1}{2n} + \frac{1}{24n^2} + o\left(\frac{1}{n^2}\right)$$
Le terme général vaut donc $\left(\frac{1}{3} - \frac{1}{24}\right)\frac{1}{n^2} + o\left(\frac{1}{n^2}\right)$, c'est-à-dire qu'il est équivalent à $\frac{7}{24n^2} > 0$. Par comparaison à la série de Riemann $\sum \frac{1}{n^2}$, la série **converge**.

**2.** Avec $\ln(1+x) = x - \frac{x^2}{2} + O(x^3)$ et $x = \frac{(-1)^n}{2n+1} \to 0$ :
$$\ln\left(1+\frac{(-1)^n}{2n+1}\right) = \frac{(-1)^n}{2n+1} - \frac{1}{2(2n+1)^2} + O\left(\frac{1}{n^3}\right)$$

- $\sum \frac{(-1)^n}{2n+1}$ converge par le critère des séries alternées ($\frac{1}{2n+1}$ décroît vers $0$) ;
- $\frac{1}{2(2n+1)^2} \sim \frac{1}{8n^2}$ : la série correspondante converge ;
- le reste $O\left(\frac{1}{n^3}\right)$ est le terme d'une série absolument convergente.

Somme de trois séries convergentes : la série **converge**. (On ne peut pas utiliser un équivalent, le terme général n'étant pas de signe constant.)

**3.** Pour $n \geq 1$, $\cos\frac{1}{n} \in \,]0, 1[$ et $u_n = \exp\left(n^3\ln\cos\frac{1}{n}\right) > 0$. Comme $\ln(\cos x) = -\frac{x^2}{2} + O(x^4)$,
$$n^3\ln\left(\cos\frac{1}{n}\right) = -\frac{n}{2} + O\left(\frac{1}{n}\right)$$
donc $u_n = e^{-n/2}e^{O(1/n)} \underset{+\infty}{\sim} \left(e^{-1/2}\right)^n$, terme général d'une série géométrique convergente (raison $e^{-1/2} < 1$). La série **converge**. (Autre méthode : règle de Cauchy, $\sqrt[n]{u_n} = \exp\left(n^2\ln\cos\frac{1}{n}\right) \to e^{-1/2} < 1$.)

**4.** Règle de Cauchy : $\sqrt[n]{u_n} = \frac{4n+1}{3n+2} \to \frac{4}{3} > 1$, donc la série **diverge** (grossièrement : $u_n \to +\infty$).

## Exercice 4 : Équivalent de ln(n!)

**Énoncé.** Le but de cet exercice est de montrer $\ln(n!) \sim n\ln(n)$. Pour tout $k, n \in \mathbb{N}^*$, on pose $u_k := \ln(k)$ et $S_n := \sum_{k=1}^{n} u_k$.

1. Montrer que : $\forall n \in \mathbb{N}^*,\ \int_1^n \ln(t)\,dt \leq S_n \leq \int_1^{n+1} \ln(t)\,dt$.
2. En déduire : $n\ln(n) \leq S_n \leq (n+1)\ln(n+1)$ (on pourra effectuer une intégration par parties pour calculer les intégrales).
3. Montrer que $S_n = \ln(n!)$ et en déduire $\ln(n!) \sim n\ln(n)$.

> **Erreur corrigée :** la minoration $n\ln(n) \leq S_n$ demandée au 2. est fausse (par exemple $S_2 = \ln 2 < 2\ln 2$ ; en fait $\ln(n!) < n\ln n$ pour $n \geq 2$). La question 1 donne seulement $n\ln(n) - n + 1 \leq S_n$, ce qui suffit pour conclure au 3.

**Correction.**

**1.** La fonction $\ln$ est croissante sur $[1, +\infty[$.

- Pour $k \geq 1$ et $t \in [k, k+1]$, $\ln k \leq \ln t$, donc $\ln k \leq \int_k^{k+1}\ln t\,dt$. En sommant pour $k = 1, \dots, n$ : $S_n \leq \int_1^{n+1}\ln t\,dt$.
- Pour $k \geq 2$ et $t \in [k-1, k]$, $\ln t \leq \ln k$, donc $\int_{k-1}^{k}\ln t\,dt \leq \ln k$. En sommant pour $k = 2, \dots, n$ et comme $u_1 = \ln 1 = 0$ : $\int_1^n \ln t\,dt \leq S_n$ (pour $n = 1$ les deux membres sont nuls).

**2.** Par intégration par parties ($u' = 1$, $v = \ln t$), une primitive de $\ln$ est $t\ln t - t$. Donc
$$\int_1^n \ln t\,dt = n\ln n - n + 1, \qquad \int_1^{n+1}\ln t\,dt = (n+1)\ln(n+1) - n$$
et la question 1 donne
$$n\ln n - n + 1 \leq S_n \leq (n+1)\ln(n+1) - n \leq (n+1)\ln(n+1)$$

**3.** $S_n = \sum_{k=1}^{n}\ln k = \ln\left(\prod_{k=1}^{n} k\right) = \ln(n!)$. Pour $n \geq 2$, divisons l'encadrement par $n\ln n > 0$ :
$$1 - \frac{1}{\ln n} + \frac{1}{n\ln n} \leq \frac{\ln(n!)}{n\ln n} \leq \frac{n+1}{n}\cdot\frac{\ln(n+1)}{\ln n}$$
Le membre de gauche tend vers $1$. À droite, $\frac{n+1}{n} \to 1$ et $\frac{\ln(n+1)}{\ln n} = 1 + \frac{\ln(1 + 1/n)}{\ln n} \to 1$. Par encadrement, $\frac{\ln(n!)}{n\ln n} \to 1$, c'est-à-dire
$$\ln(n!) \underset{+\infty}{\sim} n\ln(n)$$
