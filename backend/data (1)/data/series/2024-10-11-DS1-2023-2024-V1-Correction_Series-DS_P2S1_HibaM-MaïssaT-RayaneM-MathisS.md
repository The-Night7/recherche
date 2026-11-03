---
title: DS1 2023 2024 V1 Correction
author: [HibaM,MaïssaT,RayaneM,MathisS]
date: 2024-10-11 01:00:00 +0100
categories: [PREING2 S1,Series-DS]
tags: [PREING2 S1,Series-DS,Correction,DS1,Hiba M.,Maïssa T.,Rayane M.,Mathis S.]
division_title : DS1
math: true
---
Écrit par [Hiba M.](https://cy.deltahmed.fr/contributeurs/#HibaM)

complétée par [Maïssa T.](https://cy.deltahmed.fr/contributeurs/#MaïssaT)

Vérifiée et complétée par [Rayane M.](https://cy.deltahmed.fr/contributeurs/#RayaneM) et [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)

> **Complétion du 14 octobre 2026.** Les exercices 1 à 3 n’étaient présents que sous forme de six images distantes, inaccessibles lors de cette reprise. Leurs solutions textuelles ont été reprises de `DS120232024V1_SeriesDS_P2S1_DMaths.md` et confrontées au sujet PDF local. Le texte original de l’exercice 4 est conservé, puis complété pour répondre à la dernière question. Les auteurs ci-dessus restent ceux du document initial.

## Exercice 1 : Série géométrique

**Énoncé.** Soit $q \in \mathbb{R}$, à quelle condition sur $q$ la série $\sum_{n\geq 0} q^n$ converge-t-elle ? Le démontrer, et calculer sa valeur.

**Correction.**

> **Complément rédigé :** les réponses ci-dessous proviennent de la correction rédigée à partir du sujet local, déjà présente dans le corpus. Elles ne sont pas une transcription des images distantes du corrigé étudiant.

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

## Exercice 4 :

$$u_{k} ≔ \ln(k)\ \text{et}\ S_{n} ≔ \sum_{k = 1}^{n}u_{k}$$

### 1\.

Montrer que
$\forall n \in \mathbb{N}^{*},\int_{1}^{n}{\ln(t)dt} \leq S_{n} \leq \int_{1}^{n + 1}{\ln(t)dt}$

$$\forall x \in \lbrack k;k + 1\rbrack,k \geq 1$$

$$\ln(k) \leq \ln(x)$$

$$\ln(k) \leq \int_{k}^{k + 1}{\ln(t)dt}$$

Par somme de 1 à $n$

$$\sum_{k = 1}^{n}{\ln(k)} \leq \int_{1}^{n + 1}{\ln(t)dt}$$

$$S_{n} \leq \int_{1}^{n + 1}{\ln(t)dt}$$

$$\forall x \in \lbrack k;k + 1\rbrack,k \geq 2$$

$$\ln(x - 1) \leq \ln(k)$$

$$\int_{k}^{k + 1}{\ln(t - 1)dt} \leq \ln(k)$$

$$\int_{k - 1}^{k}{\ln(t)dt} \leq \ln(k)$$

Par somme de 2 à $n$,

$$\int_{1}^{n}{\ln(t)dt} \leq \sum_{k = 2}^{n}{\ln(k)} = S_{n}\ \text{car}\ u_{1} = 0$$

$$\int_{1}^{n}{\ln(t)dt} \leq S_{n} \leq \int_{1}^{n + 1}{\ln(t)dt}$$

### 2\.

$$\int_{}^{}{\ln(t)dt} = \int_{}^{}{1 \times \ln(t)dt}$$

$$u^{'}(t) = 1,\ u(t) = t$$

$$v(t) = \ln(t),\ v^{'}(t) = \frac{1}{t}$$

$$\int_{}^{}{u^{'}v} = uv - \int_{}^{}{uv^{'}}\ \text{(intégration par parties)}$$

$$\int_{}^{}{\ln(t)dt} = t\ln(t) - \int_{}^{}1 = t\ln(t) - t + C$$

$$\int_{1}^{n}{\ln(t)dt} = \left\lbrack t\ln(t) - t \right\rbrack_{1}^{n} = n\ln(n) - n + 1 = n\left( \ln(n) - 1 \right) + 1$$

$$\int_{1}^{n + 1}{\ln(t)dt} = \left\lbrack t\ln(t) - t \right\rbrack_{1}^{n + 1} = (n + 1)\ln(n + 1) - (n + 1) + 1 = (n + 1)\ln(n + 1) - n$$

$$n\left( \ln(n) - 1 \right) + 1 \leq S_{n} \leq (n + 1)\ln(n + 1) - n \leq (n + 1)\ln(n + 1)$$

$$n\left( \ln(n) - 1 \right) + 1 \leq S_{n} \leq (n + 1)\ln(n + 1)$$

$$ n\left( \ln(n) - 1 \right) \leq n\left( \ln(n) - 1 \right) + 1 \leq S_{n} \leq (n + 1)\ln(n + 1)   $$

$$n\left( \ln(n) - 1 \right) \leq S_{n} \leq (n + 1)\ln(n + 1)$$

> **Rectification de la conclusion originale.** La minoration $n\ln n\le S_n$ demandée dans le sujet est fausse, mais l’encadrement correct obtenu ci-dessus suffit pour terminer.

### 3. Complément rédigé — équivalent de ln(n!)

On a $S_n=\sum_{k=1}^n\ln k=\ln(n!)$. Pour $n\ge2$, divisons l’encadrement par $n\ln n>0$ :

$$1-\frac1{\ln n}\le\frac{\ln(n!)}{n\ln n}\le\frac{n+1}{n}\frac{\ln(n+1)}{\ln n}.$$

Les deux bornes tendent vers $1$. Donc $\boxed{\ln(n!)\sim n\ln n}$, malgré l’erreur de la question 2.
