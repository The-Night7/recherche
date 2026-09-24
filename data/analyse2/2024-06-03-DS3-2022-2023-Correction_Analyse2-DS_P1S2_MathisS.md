---
title: DS3 2022 2023 Correction
author: [MathisS]
date: 2024-06-03 01:00:00 +0100
categories: [PREING1 S2,Analyse2-DS]
tags: [PREING1 S2,Analyse2-DS,Mathis S.,DS3]
division_title : DS3
math: true
---

*Correction par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La plupart des résultats ont été vérifiés par l'outil informatique,
mais si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-info }

## Exercice 1 :

### 1\.

$$A = \int_{0}^{1}{(2x - 4)e^{x}dx}$$

On pose $u(x) = 2x - 4,\ u^{'}(x) = 2$

$$v^{'}(x) = e^{x},\ v(x) = e^{x}$$

Par intégration par parties,

$$A = \lbrack uv\rbrack_{0}^{1} - \int_{0}^{1}{u^{'}v}$$

$$A = \left\lbrack (2x - 4)e^{x} \right\rbrack_{0}^{1} - \int_{0}^{1}{2e^{x}dx}$$

$$A = \left\lbrack (2x - 4)e^{x} \right\rbrack_{0}^{1} - 2\left\lbrack e^{x} \right\rbrack_{0}^{1}$$

$$A = ( - 2e + 4) - 2(e - 1)$$

$$A = - 4e + 6$$

### 2\.

$$B = \int_{0}^{1}{x\sqrt{1 + x^{2}}dx}$$

On pose $u = 1 + x^{2}$

$$du = 2xdx$$

$$B = \int_{1}^{2}{\frac{1}{2}\sqrt{u}du} = \frac{1}{2}\int_{1}^{2}{u^{\frac{1}{2}}du} = \frac{1}{2}\left\lbrack \frac{2}{3}u^{\frac{3}{2}} \right\rbrack_{1}^{2}$$

$$B = \frac{1}{2}\left( \frac{2}{3}2\sqrt{2} - \frac{2}{3} \right) = \frac{2\sqrt{2} - 1}{3}$$

### 3\.

$$C = \int_{0}^{\frac{\pi}{2}}{x\sin(x)dx}$$

On pose

$$u(x) = x,\ u^{'}(x) = 1$$

$$v^{'}(x) = \sin(x),\ v(x) = - \cos(x)$$

$$C = \lbrack uv\rbrack_{0}^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}}{u^{'}v}$$

$$C = - \left\lbrack x\cos(x) \right\rbrack_{0}^{\frac{\pi}{2}} + \int_{0}^{\frac{\pi}{2}}{\cos(x)dx}$$

$$C = - \left\lbrack x\cos(x) \right\rbrack_{0}^{\frac{\pi}{2}} + \left\lbrack \sin(x) \right\rbrack_{0}^{\frac{\pi}{2}}$$

$$C = 1$$

## Exercice 2 :

### 1\.

$$\frac{1}{x(x + 1)} = \frac{a}{x} + \frac{b}{x - 1}$$

$$\frac{1}{x(x + 1)} = \frac{a(x - 1) + bx}{x(x - 1)}$$

$$ax - a + bx = 1$$

$$(a + b)x - a = 1$$

$a + b = 0$ et $- a = 1$

$b = - a$ et $a = - 1$

$a = - 1$ et $b = 1$

$$f(x) = - \frac{1}{x} + \frac{1}{x - 1}$$

### 2\.

$$F(x) = \int_{}^{}{f(x)dx}$$

$$F(x) = - \int_{}^{}\frac{dx}{x} + \int_{}^{}\frac{dx}{x - 1}$$

$$F(x) = - \ln(x) + \ln(x - 1)$$

$$F(x) = \ln(x - 1) - \ln(x) = \ln\left( \frac{x - 1}{x} \right)$$

### 3.a.

$(S)$ se réécrit, $\forall x > 1,$

$$y^{'} - \frac{1}{x(x - 1)}y = \frac{1}{x - 1}$$

On cherche à résoudre l'équation homogène associée :

$$y^{'} - \frac{1}{x(x - 1)}y = 0$$

Il s'agit d'une équation de la forme $y^{'} + ay = 0$ avec $a = - f$

Soit $A = - F$ telle que $A^{'} = a$

Alors l'ensemble des solutions de l'équation homogène s'écrit

$$\mathcal{S}_{y^{'} + ay} = \left\{ \lambda e^{- A},\lambda \in \mathbb{R} \right\} = \left\{ \lambda e^{F},\lambda \in \mathbb{R} \right\}$$

Ces fonctions sont de la forme

$$\lambda e^{\ln\left( 1 - \frac{1}{x} \right)} = \lambda\left( \frac{x - 1}{x} \right)$$

$$\mathcal{S}_{y^{'} + ay} = \left\{ x \rightarrow \lambda\left( \frac{x - 1}{x} \right),\ \lambda \in \mathbb{R} \right\}$$

### 3.b.

$$g^{'}(x) = \frac{1}{x} + \frac{1}{x^{2}}\ln(x - 1)$$

$$x(x - 1)g^{'}(x) - g(x) = (x - 1) + \left( \frac{x - 1}{x} \right)\ln(x - 1) + 1 - \left( \frac{x - 1}{x} \right)\ln(x - 1) = x$$

Donc $g$ est solution de $(S)$

### 3.c.

La solution générale de $(S)$ est la somme d'une solution générale de
l'équation homogène et d'une solution particulière de $(S)$

$$\mathcal{S}_{(S)} = \left\{ x \rightarrow \lambda\left( \frac{x - 1}{x} \right) - 1 + \left( \frac{x - 1}{x} \right)\ln(x - 1),\ \lambda \in \mathbb{R} \right\}$$

$$\mathcal{S}_{(S)} = \left\{ x \rightarrow \left( \frac{x - 1}{x} \right)\left( \lambda + \ln(x - 1) \right) - 1,\ \lambda \in \mathbb{R} \right\}$$

### 4\.

D'après le théorème de Cauchy-Lipschitz, il existe une unique solution
$h$ satisfaisant l'équation $(S)$ et $y(2) = 1$

$$h \in \mathcal{S}_{(S)}\text{ }\text{donc}\ \exists\mu \in \mathbb{R,}\ h(x) = \left( \frac{x - 1}{x} \right)\left( \mu + \ln(x - 1) \right) - 1$$

Aussi, $h(2) = 1$

Donc,

$$\frac{2 - 1}{2}\left( \mu + \ln(2 - 1) \right) - 1 = 1$$

$$\frac{\mu}{2} - 1 = 1$$

$$\frac{\mu}{2} = 2$$

$$\mu = 4$$

$$h(x) = \left( \frac{x - 1}{x} \right)\left( 4 + \ln(x - 1) \right) - 1$$

## Exercice 3 :

### 1\.

On cherche à résoudre :

$$y^{''} - 4y^{'} + 4y = 0$$

On pose $y = e^{rx}$ avec $r$ réel

$$\left( r^{2} - 4r + 4 \right)e^{rx} = 0$$

$$r^{2} - 4r + 4 = 0$$

$$(r - 2)^{2} = 0$$

D'après le théorème du cours,

$$\mathcal{S}_{y^{''} - 4y^{'} + 4y} = \left\{ x \rightarrow (\lambda x + \mu)e^{2x},(\lambda,\mu) \in \mathbb{R}^{2} \right\}$$

### 2\.

$d(x)$ est de la forme $e^{\alpha x}$ avec $\alpha = - 2$ n'est pas une
racine de l'équation caractéristique.

On cherche une solution particulière de la forme
$y_{1} = \beta e^{- 2x}$

$$y_{1}^{'} = - 2\beta e^{- 2x}$$

$$y_{1}^{''} = 4\beta e^{- 2x}$$

$$y_{1}^{''} - 4y_{1}^{'} + 4y_{1} = e^{- 2x}$$

$$(4\beta + 8\beta + 4\beta)e^{- 2x} = e^{- 2x}$$

$$16\beta e^{- 2x} = e^{- 2x}$$

$$\beta = \frac{1}{16}$$

$$y_{1} = \frac{e^{- 2x}}{16}\ \text{est une solution particulière de}\ (E)\ \text{avec}\ d(x) = e^{- 2x}$$

### 3\.

$d(x)$ est de la forme $e^{\alpha x}$ avec $\alpha = 2$ est une racine
double de l'équation caractéristique.

On cherche une solution particulière de la forme
$y_{2} = \gamma x^{2}e^{2x}$

$$y_{2}^{'} = \gamma(2x)e^{2x} + \gamma x^{2}\left( 2e^{2x} \right) = 2\gamma e^{2x}\left( x^{2} + x \right)$$

$$y_{2}^{''} = 2\gamma\left( (2x + 1)e^{2x} + \left( x^{2} + x \right)2e^{2x} \right)$$

$$y_{2}^{''} = 2\gamma e^{2x}\left( 2x^{2} + 4x + 1 \right)$$

$$y_{2}^{''} - 4y_{2}^{'} + 4y_{2} = e^{2x}$$

$$2\gamma e^{2x}\left( 2x^{2} + 4x + 1 \right) - 8\gamma e^{2x}\left( x^{2} + x \right) + 4\gamma x^{2}e^{2x} = e^{2x}$$

$$\gamma e^{2x}(2) = e^{2x}$$

$$\gamma = \frac{1}{2}$$

$$y_{2} = \frac{1}{2}x^{2}e^{2x}\ \text{est une solution particulière de}\ (E)\ \text{avec}\ d(x) = e^{2x}$$

### 4\.

Par superposition, une solution particulière $y_{P}$ de $(E)$ est

$$y_{P} = \frac{1}{4}\left( y_{1} + y_{2} \right)$$

$$y_{P} = \frac{1}{8}\left( x^{2}e^{2x} + \frac{e^{- 2x}}{8} \right)\ \text{est une solution particulière de}\ (E)\ \text{avec}\ d(x) = \frac{e^{2x} + e^{- 2x}}{4}$$

### 5\.

La solution générale de $(E)$ est la somme d'une solution générale de
l'équation homogène et d'une solution particulière de $(E)$

$$\mathcal{S}_{(E)} = \left\{ x \rightarrow \left( \lambda x + \mu + \frac{x^{2}}{8} \right)e^{2x} + \frac{e^{- 2x}}{64} \right\}$$
