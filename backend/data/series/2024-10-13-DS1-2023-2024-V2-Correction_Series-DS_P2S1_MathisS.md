---
title: DS1 2023 2024 V2 Correction
author: [MathisS]
date: 2024-10-13 01:00:00 +0100
categories: [PREING2 S1,Series-DS]
tags: [PREING2 S1,Series-DS,DS1,Mathis S.]
division_title : DS1
math: true
---

*Correction proposée par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La plupart des résultats ont été vérifiés par l'outil informatique,
mais si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-info }

## Exercice 1 :

### 1\.

L'affirmation est fausse. En effet,

$$\sum_{}^{}\frac{( - 1)^{n}}{n}\ \text{est convergente }\text{car série de Riemann alternée avec}\ \alpha = 1 > 0$$

$$\text{Mais n'est pas absolument convergente car}\ \sum_{}^{}\frac{1}{n}\ \text{diverge}\text{ (série harmonique)}$$

### 2\.

L'affirmation est fausse. En effet,

$$\frac{1}{n^{2}} = o\left( \frac{1}{n} \right)\ \text{au voisinage de} + \infty\ \text{mais}\ \sum_{}^{}\frac{1}{n^{2}}\ \text{est convergente}\text{ (série de Riemann avec}\ \alpha = 2 > 1)$$

### 3\.

L'affirmation est fausse. En effet,

$$\sum_{}^{}\frac{1}{n^{2}}\ \text{est convergente mais}\frac{1}{n^{2}} > \frac{1}{2}\ \text{pour}\ n = 1$$

*Cette question est mal formulée.*

## Exercice 2 :

### 1\.

$$\sum_{}^{}\frac{\tan^{n}\left( \frac{\pi}{7} \right)}{3^{n + 2}} = \frac{1}{9}\sum_{}^{}\left( \frac{\tan\left( \frac{\pi}{7} \right)}{3} \right)^{n}$$

$$0 < \frac{\pi}{7} < \frac{\pi}{4}$$

$$0 < \tan\left( \frac{\pi}{7} \right) < \tan\left( \frac{\pi}{4} \right)\ \text{par stricte croissance de tangente}\text{ sur}\ \rbrack - \frac{\pi}{2};\frac{\pi}{2}\lbrack$$

$$0 < \frac{\tan\left( \frac{\pi}{7} \right)}{3} < \frac{1}{3} < 1$$

$$\text{Donc}\ \sum_{}^{}\left( \frac{\tan\left( \frac{\pi}{7} \right)}{3} \right)^{n}\text{est une série géométrique convergente}$$

$$\text{Donc}\ \sum_{}^{}\frac{\tan^{n}\left( \frac{\pi}{7} \right)}{3^{n + 2}}\ \text{converge}$$

### 2\.

$$\sum_{}^{}\frac{2^{n}}{3^{n - 2}} = 9\sum_{}^{}\left( \frac{2}{3} \right)^{n}$$

$$0 < \frac{2}{3} < 1$$

$$\text{Donc}\ \sum_{}^{}\left( \frac{2}{3} \right)^{n}\text{est une série géométrique convergente}$$

$$\text{Donc}\ \sum_{}^{}\frac{2^{n}}{3^{n - 2}}\ \text{converge}$$

### 3\.

Montrons que la série est absolument convergente.

$$\left| \frac{\cos(n)}{n^{3} + n} \right| = \frac{\left| \cos(n) \right|}{n^{3} + n}$$

$$\lim_{n \rightarrow + \infty}{n^{2}\left( \frac{\left| \cos(n) \right|}{n^{3} + n} \right)} = \lim_{n \rightarrow + \infty}{\left| \cos(n) \right| \times \frac{1}{n + \frac{1}{n}}} = 0$$

D'après la règle de $n^{\alpha}$,

$$\sum_{}^{}\left| \frac{\cos(n)}{n^{3} + n} \right|\ \text{converge}$$

$$\sum_{}^{}\frac{\cos(n)}{n^{3} + n}\ \text{converge (absolument)}$$

### 4\.

$$\forall n,\cos\left( \frac{1}{n} \right) < 1$$

$$1 - \cos\left( \frac{1}{n} \right) > 0$$

$$\exp\left( \frac{1}{n} \right) > \exp(0)$$

$$\exp\left( \frac{1}{n} \right) - 1 > 0$$

$$\text{Donc}\ \sum_{}^{}\frac{1 - \cos\left( \frac{1}{n} \right)}{\exp\left( \frac{1}{n} \right) - 1}\ \text{est une série à termes positifs}$$

$$1 - \cos\left( \frac{1}{n} \right)\ \sim\frac{1}{2n^{2}}$$

$$\exp\left( \frac{1}{n} \right) - 1\ \sim\frac{1}{n}$$

$$\frac{1 - \cos\left( \frac{1}{n} \right)}{\exp\left( \frac{1}{n} \right) - 1}\ \sim\frac{1}{2n}$$

$$\sum_{}^{}\frac{1}{2n}\ \text{diverge (série harmonique) donc par équivalence}\ \sum_{}^{}\frac{1 - \cos\left( \frac{1}{n} \right)}{\exp\left( \frac{1}{n} \right) - 1}\ \text{diverge}$$

### 5\.

Appliquons le critère spécial des séries alternées. Posons
$a_{n} = \frac{n^{3}}{n\ !}\forall n$

$$\lim_{n \rightarrow + \infty}a_{n} = 0\ \text{(croissance comparée)}$$

$$\frac{a_{n + 1}}{a_{n}} = \frac{(n + 1)^{3}}{(n + 1)!} \times \frac{n!}{n^{3}} = \frac{(n + 1)^{2}}{n^{3}} < 1\ \text{à partir d'un certain rang}$$

Donc $\left( a_{n} \right)$ est décroissante.

D'après le critère spécial des séries alternées,

$$\sum_{}^{}{( - 1)^{n}\frac{n^{3}}{n!}}\ \text{converge}$$

## Exercice 3 :

### 1\.

$$\text{Posons}\ u_{n} = \frac{1}{n(n + 1)(n + 2)}$$

$$\text{Posons}\ a,b,c\ \text{tels que}\ \forall n\mathbb{\in N,\ }u_{n} = \frac{a}{n} + \frac{b}{n + 1} + \frac{c}{n + 2}$$

$$\frac{1}{n(n + 1)(n + 2)} = \frac{a}{n} + \frac{b}{n + 1} + \frac{c}{n + 2}$$

$$\text{En multipliant par}\ n\ \text{et posant}\ n = 0,\ \text{on obtient}\ a = \frac{1}{2}$$

$$\text{En multipliant par}\ n + 1\ \text{et posant}\ n = - 1,\ \text{on obtient}\ b = - 1$$

$$\text{En multipliant par}\ n + 2\ \text{et posant}\ n = - 2,\ \text{on obtient}\ c = \frac{1}{2}$$

$$u_{n} = \frac{1}{2n} - \frac{1}{n + 1} + \frac{1}{2(n + 2)}$$

$$u_{n} = \frac{1}{2}\left( \frac{1}{n} - \frac{1}{n + 1} \right) + \frac{1}{2}\left( \frac{1}{n + 2} - \frac{1}{n + 1} \right)$$

$$\sum_{k = 1}^{n}u_{k} = \frac{1}{2}\sum_{k = 1}^{n}\left( \frac{1}{k} - \frac{1}{k + 1} \right) + \frac{1}{2}\sum_{k = 1}^{n}\left( \frac{1}{k + 2} - \frac{1}{k + 1} \right)$$

$$\sum_{k = 1}^{n}u_{k} = \frac{1}{2}\left( 1 - \frac{1}{n + 1} \right) + \frac{1}{2}\left( \frac{1}{n + 2} - \frac{1}{2} \right)$$

$$\sum_{n \geq 1}^{}u_{n} = \lim_{n \rightarrow + \infty}{\sum_{k = 1}^{n}u_{k}} = \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$$

$$\sum_{n \geq 1}^{}u_{n} = \frac{1}{4}$$

### 2\.

$$\sum_{n \geq 0}^{}\frac{n^{2} - 2}{n!}$$

$$= \sum_{n \geq 0}^{}\frac{n(n - 1) + n - 2}{n!}$$

$$= \sum_{n \geq 0}^{}\frac{n(n - 1)}{n!} + \sum_{n \geq 0}^{}\frac{n}{n!} - 2\sum_{n \geq 0}^{}\frac{1}{n!}
$$

$$\text{Or}\ \sum_{n \geq 0}^{}\frac{n(n - 1)}{n!} = \sum_{n \geq 2}^{}\frac{n(n - 1)}{n!}\ \text{car les deux premiers termes sont nuls}$$

$$\text{Et}\ \sum_{n \geq 0}^{}\frac{n}{n!} = \sum_{n \geq 1}^{}\frac{n}{n!}\ \text{car le premier terme est nul}$$

$$= \sum_{n \geq 2}^{}\frac{1}{(n - 2)!} + \sum_{n \geq 1}^{}\frac{1}{(n - 1)!} - 2e$$

$$= \sum_{n \geq 0}^{}\frac{1}{n!} + \sum_{n \geq 0}^{}\frac{1}{n!} - 2e$$

$$= 2e - 2e = 0$$

$$\sum_{n \geq 0}^{}\frac{n^{2} - 2}{n!} = 0$$

## Exercice 4 :

### 1\.

$$u_{n} = \ln(n) + a\ln(n + 1) + b\ln(n + 2)$$

$$u_{n} = \ln(n) + a\left( \ln(n) + \ln\left( 1 + \frac{1}{n} \right) \right) + b\left( \ln(n) + \ln\left( 1 + \frac{2}{n} \right) \right)$$

$$u_{n} = (1 + a + b)\ln(n) + a\ln\left( 1 + \frac{1}{n} \right) + b\ln\left( 1 + \frac{2}{n} \right)$$

$$u_{n} = (1 + a + b)\ln(n) + a\left( \frac{1}{n} - \frac{1}{2n^{2}} + o\left( \frac{1}{n^{2}} \right) \right) + b\left( \frac{2}{n} - \frac{1}{n^{2}} + o\left( \frac{1}{n^{2}} \right) \right)$$

$$u_{n} = (1 + a + b)\ln(n) + \frac{a + 2b}{n} - \frac{a + 2b}{2n^{2}} + o\left( \frac{1}{n^{2}} \right)$$

$$\text{On pose}\ \alpha = 1 + a + b,\ \beta = a + 2b,\ \gamma = - \frac{a + 2b}{2}$$

$$u_{n} = \alpha\ln(n) + \frac{\beta}{n} + \frac{\gamma}{n^{2}} + o\left( \frac{1}{n^{2}} \right)$$

### 2\.

$$\text{Si}\ \alpha \neq 0,\ \text{alors}\lim_{n \rightarrow + \infty}u_{n} = \pm \infty\ \text{et}\ \sum_{}^{}u_{n}\ \text{diverge grossièrement}$$

Donc $\alpha = 0$ est une condition nécessaire à la convergence de la
série.

$$\sum_{}^{}u_{n} = \beta\sum_{}^{}\frac{1}{n} + \gamma\sum_{}^{}\frac{1}{n^{2}} + \sum_{}^{}{o\left( \frac{1}{n^{2}} \right)}$$

$$\sum_{}^{}\frac{1}{n^{2}}\ \text{converge car série de Riemann avec}\ \alpha > 1,\ \text{donc}\ \sum_{}^{}{o\left( \frac{1}{n^{2}} \right)}\ \text{converge aussi}$$

$$\sum_{}^{}\frac{1}{n}\ \text{diverge car série harmonique}$$

Donc la série converge si et seulement si $\alpha = \beta = 0$

$$\left\{ \begin{array}{r}
a + b = - 1 \\
a + 2b = 0
\end{array} \right\}$$

La série converge si et seulement si $a = - 2$ et $b = 1$

### 3\.

En cas de convergence,

$$u_{n} = \ln(n) - 2\ln(n + 1) + \ln(n + 2)$$

$$u_{n} = \left( \ln(n) - \ln(n + 1) \right) + \left( \ln(n + 2) - \ln(n + 1) \right)$$

$$S_{N} = \sum_{n = 1}^{N}u_{N} = \sum_{n = 1}^{N}\left( \ln(n) - \ln(n + 1) \right) + \sum_{n = 1}^{N}\left( \ln(n + 2) - \ln(n + 1) \right)$$

$$S_{N} = - \ln(N + 1) + \ln(N + 2) - \ln(2)$$

$$S_{N} = - \ln(2) + \ln\left( \frac{N + 2}{N + 1} \right)$$

### 4\.

$$S = \lim_{n \rightarrow + \infty}S_{N} = - \ln(2)$$