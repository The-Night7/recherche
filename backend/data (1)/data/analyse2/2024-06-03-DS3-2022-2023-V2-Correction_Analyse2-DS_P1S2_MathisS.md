---
title: DS3 2022 2023 V2 Correction
author: [MathisS]
date: 2024-06-03 01:00:00 +0100
categories: [PREING1 S2,Analyse2-DS]
tags: [PREING1 S2,Analyse2-DS,Mathis S.,DS3]
division_title : DS3
math: true
---


*Correction proposée par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La correction a été faite dans la précipitation (merci au gatekeep...) et peut contenir quelques erreurs, il est donc normal que la correction ne soit pas ultra détaillée, si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-warning }

## Exercice 1 :

### 1\.

$$P_{1} = \int_{}^{}{\frac{x^{2}}{\left( x^{2} + 1 \right)(x - 1)}dx}$$

$$\frac{x^{2}}{\left( x^{2} + 1 \right)(x - 1)} = \frac{ax + b}{x^{2} + 1} + \frac{c}{x - 1}$$

$$x^{2} = (ax + b)(x - 1) + c\left( x^{2} + 1 \right)$$

$$x^{2} = ax^{2} - ax + bx - b + cx^{2} + c$$

$$x^{2} = (a + c)x^{2} + (b - a)x + c - b$$

$$\left\{ \begin{array}{r}
a + c = 1 \\
b = a \\
c = b
\end{array} \right\}$$

$$a = b = c = \frac{1}{2}$$

$$\frac{x^{2}}{\left( x^{2} + 1 \right)(x - 1)} = \frac{1}{2}\left( \frac{x + 1}{x^{2} + 1} + \frac{1}{x - 1} \right)$$

$$\frac{x^{2}}{\left( x^{2} + 1 \right)(x - 1)} = \frac{1}{2}\left( \frac{x}{x^{2} + 1} + \frac{1}{x^{2} + 1} + \frac{1}{x - 1} \right)$$

$$P_{1} = \frac{1}{2}\int_{}^{}{\frac{x}{x^{2} + 1}dx} + \frac{1}{2}\int_{}^{}\frac{dx}{x^{2} + 1} + \frac{1}{2}\int_{}^{}\frac{dx}{x - 1}$$

$$P_{1}(x) = \frac{1}{4}\ln\left( x^{2} + 1 \right) + \frac{1}{2}\arctan(x) + \frac{1}{2}\ln|x - 1| + k$$

### 2\.

$$P_{2} = \int_{}^{}{x\cos(x)dx}$$

$$u(x) = x,\ u^{'}(x) = 1$$

$$v^{'}(x) = \cos(x),\ v(x) = \sin(x)$$

$$P_{2} = x\sin(x) - \int_{}^{}{\sin(x)dx}$$

$$P_{2}(x) = x\sin(x) + \cos(x) + k$$

## Exercice 2 :

### 1\.

$$I_{1} = \int_{1}^{4}{\frac{x - 1}{\sqrt{x} + 1}dx}$$

$$t = \sqrt{x}$$

$$t^{2} = x$$

$$2tdt = dx$$

$$I_{1} = \int_{1}^{2}{\frac{t^{2} - 1}{t + 1}2tdt}$$

$$I_{1} = 2\int_{1}^{2}{t(t - 1)dt}$$

$$I_{1} = 2\int_{1}^{2}{\left( t^{2} - t \right)dt}$$

$$I_{1} = 2\left\lbrack \frac{t^{3}}{3} - \frac{t^{2}}{2} \right\rbrack_{1}^{2} = 2\left( \frac{2}{3} + \frac{1}{6} \right) = \frac{5}{3}$$

### 2\.

$$I_{2} = \int_{1}^{2}{x^{3}\ln(x)dx}$$

$$u(x) = \ln(x),\ u^{'}(x) = \frac{1}{x}$$

$$v^{'}(x) = x^{3},\ v(x) = \frac{x^{4}}{4}$$

$$I_{2} = \left\lbrack \frac{x^{4}}{4}\ln(x) \right\rbrack_{1}^{2} - \frac{1}{4}\int_{}^{}{x^{3}dx}$$

$$I_{2} = \left\lbrack \frac{x^{4}}{4}\ln(x) \right\rbrack_{1}^{2} - \frac{1}{4}\left\lbrack \frac{x^{4}}{4} \right\rbrack_{1}^{2}$$

$$I_{2} = 4\ln(2) - 1 + \frac{1}{16} = 4\ln(2) - \frac{15}{16}$$

## Exercice 3 :

$$A_{n} = \sum_{k = 1}^{n}\frac{1}{k + 5n}$$

$$A_{n} = \frac{1}{n}\sum_{k = 1}^{n}\frac{1}{\left( \frac{k}{n} \right) + 5}$$

$$\text{On pose }f(x) = \frac{1}{x + 5}$$

Par somme de Riemann,

$$S = \int_{0}^{1}\frac{dx}{x + 5} = \left\lbrack \ln(x + 5) \right\rbrack_{0}^{1} = \ln\left( \frac{6}{5} \right)$$

## Exercice 4 :

### 1\.

$$y^{'} + 2xy = e^{- x^{2}}\left( \sin(x) + \cos(x) \right)$$

### Etape 1 :

On cherche à résoudre $y^{'} + 2xy = 0$

On pose $a(x) = 2x$

$$A(x) = x^{2},\ A^{'} = a$$

$$y_{H} = \lambda e^{- A} = \lambda e^{- x^{2}},\ \lambda \in \mathbb{R}$$

### Etape 2 :

On cherche une solution particulière de l'équation.

$$y_{P} = \lambda(x)e^{- x^{2}}$$

$$y_{P}^{'}(x) = \lambda^{'}(x)e^{- x^{2}} - 2x\lambda(x)e^{- x^{2}}$$

$$y_{P}^{'} + 2xy_{P} = e^{- x^{2}}\left( \sin(x) + \cos(x) \right)$$

$$\lambda^{'}(x)e^{- x^{2}} - 2x\lambda(x)e^{- x^{2}} + 2x\lambda(x)e^{- x^{2}} = e^{- x^{2}}\left( \sin(x) + \cos(x) \right)$$

$$\lambda^{'}(x) = \sin(x) + \cos(x)$$

$$\lambda(x) = - \cos(x) + \sin(x)$$

$$y_{P} = \left( \sin(x) - \cos(x) \right)e^{- x^{2}}$$

### Etape 3 :

Les solutions de l'équation différentielle sont les fonctions

$$y:\mathbb{R \rightarrow R}$$

$$x \rightarrow e^{- x^{2}}\left( \lambda + \sin(x) - \cos(x) \right)$$

## Exercice 5 :

### 1\.

L'équation se réécrit :

$$y^{'} - \frac{2x}{1 + x^{2}}y = \frac{x}{1 + x^{2}}$$

### Etape 1 :

On cherche à résoudre l'équation :

$$y^{'} - \frac{2x}{1 + x^{2}}y = 0$$

$$\text{On pose}\ a(x) = - \frac{2x}{1 + x^{2}}$$

$$A(x) = - \ln\left( 1 + x^{2} \right),\ A^{'} = a$$

$$y_{H} = \lambda e^{- A} = \lambda\left( 1 + x^{2} \right)$$

### Etape 2 :



On cherche une solution particulière de l'équation.

$$y_{P}(x) = \lambda(x)\left( 1 + x^{2} \right)$$

$$y_{P}^{'}(x) = \lambda^{'}(x)\left( 1 + x^{2} \right) + 2x\lambda(x)$$

$$y_{P}^{'} - \frac{2x}{1 + x^{2}}y_{P} = \frac{x}{1 + x^{2}}$$

$$\lambda^{'}(x)\left( 1 + x^{2} \right) + 2x\lambda(x) - \frac{2x}{1 + x^{2}}\lambda(x)\left( 1 + x^{2} \right) = \frac{x}{1 + x^{2}}$$

$$\lambda^{'}(x)\left( 1 + x^{2} \right) = \frac{x}{1 + x^{2}}$$

$$\lambda^{'}(x) = \frac{x}{\left( 1 + x^{2} \right)^{2}}$$

$$\lambda^{'}(x) = \frac{1}{2}\left( \frac{2x}{\left( 1 + x^{2} \right)^{2}} \right)$$

$$\lambda(x) = - \frac{1}{2\left( 1 + x^{2} \right)}$$

$$y_{P} = - \frac{1}{2}$$

### Etape 3 :

Les solutions de l'équation différentielle sont les fonctions

$$y:\mathbb{R \rightarrow R}$$

$$x \rightarrow \lambda\left( 1 + x^{2} \right) - \frac{1}{2}$$

### Etape 4 :

D'après le théorème de Cauchy-Lipschitz, il existe une unique fonction
$h$ satisfaisant le problème de Cauchy.

$h$ est solution de l'équation différentielle,

$$\exists\mu \in \mathbb{R,\ }\mu\left( 1 + x^{2} \right) - \frac{1}{2} = h(x)$$

Aussi $h(1) = 0$

$$2\mu - \frac{1}{2} = 0$$

$$\mu = \frac{1}{4}$$

$$h(x) = \frac{1}{4}\left( 1 + x^{2} \right) - \frac{1}{2} = \frac{1}{4}x^{2} - \frac{1}{4}$$

$h(x)$ est la solution du problème de Cauchy.

**Vérif :**

$$h^{'}(x) = \frac{x}{2}$$

$$\left( 1 + x^{2} \right)h^{'} - 2xh = \frac{\left( 1 + x^{2} \right)x}{2} - 2x\left( \frac{1}{4}x^{2} - \frac{1}{4} \right) = \frac{x}{2} + \frac{x^{3}}{2} - \frac{x^{3}}{2} + \frac{x}{2} = x$$