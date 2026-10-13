---
title: DS3 2021 2022 Correction
author: [MathisS]
date: 2024-05-28 01:00:00 +0100
categories: [PREING1 S2,Analyse2-DS]
tags: [PREING1 S2,Analyse2-DS,Mathis S.,DS3]
division_title : DS3
math: true
---

*Correction proposée par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La plupart des résultats ont été vérifiés par l'outil informatique,
mais si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-info }

## Exercice 1 :

### 1\.

$\forall x \in \rbrack - 1,1\lbrack$, le problème se réécrit :

$$y^{'} - \frac{2x}{1 - x^{2}}y = \frac{1}{1 - x^{2}}$$

Il s'agit d'une équation différentielle linéaire du premier ordre.

$$a(x) = - \frac{2x}{1 - x^{2}}$$

$$A(x) = \ln\left( 1 - x^{2} \right)$$

$$b(x) = \frac{1}{1 - x^{2}}$$

**Calculons les solutions de l'équation homogène associée :**

Les solutions sont de la forme :

$$y_{H} = \lambda e^{- A(x)} = \lambda e^{- \ln\left( 1 - x^{2} \right)} = \lambda\left( e^{\ln\left( 1 - x^{2} \right)} \right)^{- 1} = \frac{\lambda}{1 - x^{2}}$$

$$y_{H} = \frac{\lambda}{1 - x^{2}}$$

**Calculons une solution particulière de cette équation, par variation de
la constante :**

$$y_{P} = \frac{\lambda(x)}{1 - x^{2}}$$

$$y_{P}^{'}(x) = \frac{\lambda^{'}(x)\left( 1 - x^{2} \right) + 2x\lambda(x)}{\left( 1 - x^{2} \right)^{2}} = \frac{\lambda^{'}(x)}{1 - x^{2}} + \lambda(x)\frac{2x}{\left( 1 - x^{2} \right)^{2}}$$

$$y_{P}^{'} - \frac{2x}{1 - x^{2}}y_{P} = \frac{1}{1 - x^{2}}$$

$$\frac{\lambda^{'}(x)}{1 - x^{2}} + \lambda(x)\frac{2x}{\left( 1 - x^{2} \right)^{2}} - \left( \frac{2x}{1 - x^{2}} \right)\left( \frac{\lambda(x)}{1 - x^{2}} \right) = \frac{1}{1 - x^{2}}$$

$$\frac{\lambda^{'}(x)}{1 - x^{2}} = \frac{1}{1 - x^{2}}$$

$$\lambda^{'}(x) = 1$$

$$\lambda(x) = x$$

$$y_{P} = \frac{x}{1 - x^{2}}$$

**Détermination de l'ensemble des solutions de l'équation
différentielle**

$$y_{G} = y_{H} + y_{P}$$

$$y_{G} = \frac{\lambda + x}{1 - x^{2}}$$

**Vérification :**

$$y^{'}(x) = \frac{1 - x^{2} + 2x(\lambda + x)}{\left( 1 - x^{2} \right)^{2}} = \frac{\left( 1 - x^{2} + 2\lambda x + 2x^{2} \right)}{\left( 1 - x^{2} \right)^{2}} = \frac{x^{2} + 2\lambda x + 1}{\left( 1 - x^{2} \right)^{2}}$$

$$\left( 1 - x^{2} \right)y^{'} - 2xy = \frac{x^{2} + 2\lambda x + 1 - 2\lambda x - 2x^{2}}{1 - x^{2}} = \frac{1 - x^{2}}{1 - x^{2}} = 1$$

**Résolution du problème de Cauchy**

$$y(0) = \lambda = 1$$

$$y = \frac{1 + x}{1 - x^{2}} = \frac{1}{1 - x}$$

### 2\.

$$y^{''} - 6y^{'} + 13y = 29e^{- 2x}$$

Il s'agit d'une équation différentielle linéaire du deuxième ordre.

**Calculons les solutions de l'équation homogène associée :**

$$y^{''} - 6y^{'} + 13y = 0$$

Soit $y = e^{rx},\ y^{'} = re^{rx},\ y^{''} = r^{2}e^{rx}$

$$\left( r^{2} - 6r + 13 \right)e^{rx} = 0$$

$$r^{2} - 6r + 13 = 0$$

$$r^{2} - 2(3r) + 9 + 4 = 0$$

$$(r - 3)^{2} = - 4$$

$$r = 3 \pm 2i$$

$$y = e^{3x}\left( \lambda\cos(2x) + \mu\sin(2x) \right)$$

**Calcul d'une solution particulière :**

$$g(x) = 29e^{- 2x}$$

$g(x)$ est de la forme $e^{\alpha x}$ avec $\alpha = - 2$ n'est pas
racine de l'équation caractéristique. On cherche des solutions de la
forme :

$$y_{P} = \delta e^{- 2x}$$

$$y_{P}^{'} = - 2\delta e^{- 2x}$$

$$y_{P}^{''} = 4\delta e^{- 2x}$$

$$y_{P}^{''} - 6y_{P}^{'} + 13y_{P} = 29e^{- 2x}$$

$$e^{- 2x}\delta(4 + 12 + 13) = 29e^{- 2x}$$

$$29e^{- 2x}\delta = 29e^{- 2x}$$

$$\delta = 1$$

Donc une solution particulière de l'équation différentielle est
$y_{P} = e^{- 2x}$

**Détermination de l'ensemble des solutions de l'équation
différentielle**

$$y_{G} = y_{H} + y_{P}$$

$$y_{G} = e^{3x}\left( \lambda\cos(2x) + \mu\sin(2x) \right) + e^{- 2x}$$

**Vérification :**

$$y_{G}^{'} = 3e^{3x}\left( \lambda\cos(2x) + \mu\sin(2x) \right) + e^{3x}\left( 2\mu\cos(2x) - 2\lambda\sin(2x) \right) - 2e^{- 2x}$$

$$y_{G}^{'} = e^{3x}((3\lambda + 2\mu)\cos(2x) + (3\mu - 2\lambda)\sin(2x)) - 2e^{- 2x}$$

$$y_{G}^{''} = 3e^{3x}\left( (3\lambda + 2\mu)\cos(2x) + (3\mu - 2\lambda)\sin(2x) \right) + e^{3x}\left( (6\mu - 4\lambda)\cos(2x) - (6\lambda + 4\mu)\sin(2x) \right) + 4e^{- 2x}$$

$$y_{G}^{''} = e^{3x}\left( (5\lambda + 12\mu)\cos(2x) + (5\mu - 12\lambda)\sin(2x) \right) + 4e^{- 2x}$$

$$y_{G}^{''} - 6y_{G}^{'} + 13y_{G} = e^{3x}\left( (5\lambda + 12\mu - 18\lambda - 12\mu + 13\lambda)\cos(2x) + (5\mu - 12\lambda - 18\mu + 12\lambda + 13\mu)\sin(2x) \right) + (4 + 12 + 13)e^{- 2x} = e^{3x}\left( 0\cos(2x) + 0\sin(2x) \right) + 29e^{- 2x}$$

**Résolution du problème de Cauchy**

$$y(0) = \lambda + 1 = 0 \rightarrow \lambda = - 1$$

$$y^{'} = e^{3x}\left( (2\mu - 3)\cos(2x) + (3\mu + 2)\sin(2x) \right) - 2e^{- 2x}$$

$$y^{'}(0) = (2\mu - 3) - 2 = 0$$

$$2\mu = 5$$

$$\mu = \frac{5}{2}$$

$$y = e^{3x}\left( \frac{5}{2}\sin(2x) - \cos(2x) \right) + e^{- 2x}$$

## Exercice 2 :

### 1\.

$$I = \int_{0}^{1}{\frac{1}{x^{2} + 1}dx} = \left\lbrack \arctan(x) \right\rbrack_{0}^{1} = \arctan(1) = \frac{\pi}{4}$$

### 2\.

$$S_{n} = \sum_{k = 1}^{n}\frac{n}{k^{2} + n^{2}} = \sum_{k = 1}^{n}\frac{n}{n^{2}\left( \left( \frac{k}{n} \right)^{2} + 1 \right)} = \frac{1}{n}\sum_{k = 1}^{n}\frac{1}{\left( \frac{k}{n} \right)^{2} + 1}$$

Par somme de Riemann :

$$S_{n} = \int_{0}^{1}{\frac{1}{x^{2} + 1}dx} = I = \frac{\pi}{4}$$

## Exercice 3 :

### I.1.

$$I_{1} = \int_{0}^{1}{\frac{e^{2x}}{e^{x} + 1}dx}$$

On pose $u = e^{x}$

$$du = e^{x}dx$$

$$I_{1} = \int_{1}^{e}{\frac{u}{1 + u}du} = \int_{1}^{e}{\frac{1 + u}{1 + u}du} - \int_{1}^{e}{\frac{1}{1 + u}du} = \left\lbrack u - \ln(1 + u) \right\rbrack_{1}^{e} = e - \ln(1 + e) - 1 + \ln(2) = e - 1 + \ln\left( \frac{2}{1 + e} \right)$$

### I.2.

$$I_{2} = \int_{0}^{1}{x^{3}e^{x^{2}}dx}$$

On pose $t = x^{2}$

$$dt = 2x\ dx$$

$$x^{3}e^{x^{2}}dx = x^{2}e^{x^{2}}\ xdx = \frac{1}{2}te^{t}dt$$

$$I_{2} = \frac{1}{2}\int_{0}^{1}{te^{t}dt}$$

On pose

$$u(t) = t,\ u^{'}(t) = 1$$

$$v^{'}(t) = e^{t},\ v(t) = e^{t}$$

Par intégration par parties,

$$I_{2} = \frac{1}{2}\left\lbrack te^{t} \right\rbrack_{0}^{1} - \frac{1}{2}\int_{0}^{1}{e^{t}dt}$$

$$I_{2} = \frac{1}{2}\left\lbrack te^{t} - e^{t} \right\rbrack_{0}^{1} = \frac{1}{2}$$

### II\.

$$\text{Posons}\ f(x) = \frac{2x + 1}{x^{2} + 3x + 2}$$

$$x^{2} + 3x + 2 = (x + 1)(x + 2)$$

$$f(x) = \frac{\alpha}{x + 1} + \frac{\beta}{x + 2},\ \alpha,\beta \in \mathbb{R}$$

$$2x + 1 = \alpha(x + 2) + \beta(x + 1)$$

Avec $x = - 1,\  - 1 = \alpha$

Avec $x = - 2,\  - 3 = - \beta,\ \beta = 3$

$$f(x) = - \frac{1}{x + 1} + \frac{3}{x + 2}$$

$$P = - \int_{}^{}\frac{dx}{x + 1} + 3\int_{}^{}\frac{dx}{x + 2}$$

$$P = - \ln|x + 1| + 3\ln|x + 2|$$

## Exercice 4 :

### 1\.

Utilisons le changement de variable $t = \frac{\pi}{2} - x$

$$\int_{0}^{\frac{\pi}{2}}{\frac{\cos(x)}{\sin(x) + \cos(x)}dx} = \int_{0}^{\frac{\pi}{2}}{\frac{\sin\left( \frac{\pi}{2} - x \right)}{\cos\left( \frac{\pi}{2} - x \right) + \sin\left( \frac{\pi}{2} - x \right)}dx} = \int_{\frac{\pi}{2}}^{0}{\frac{\sin(t)}{\sin(t) + \cos(t)}( - dt)} = \int_{0}^{\frac{\pi}{2}}{\frac{\sin(t)}{\sin(t) + \cos(t)}dt}$$

Donc

$$I = \int_{0}^{\frac{\pi}{2}}{\frac{\cos(x)}{\sin(x) + \cos(x)}dx} = \int_{0}^{\frac{\pi}{2}}{\frac{\sin(x)}{\sin(x) + \cos(x)}dx}$$

$$2I = \int_{0}^{\frac{\pi}{2}}{\frac{\cos(x)}{\sin(x) + \cos(x)}dx} + \int_{0}^{\frac{\pi}{2}}{\frac{\sin(x)}{\sin(x) + \cos(x)}dx}$$

$$2I = \int_{0}^{\frac{\pi}{2}}{1dx} = \frac{\pi}{2}$$

$$I = \frac{\pi}{4}$$

### 2\.

$$t = \cos(x)$$

$$dt = - \sin(x)dx$$

$$\int_{0}^{1}\frac{dt}{t + \sqrt{1 - t^{2}}} = \int_{\frac{\pi}{2}}^{0}{\frac{- \sin(x)}{\cos(x) + \sin(x)}dx} = \int_{0}^{\frac{\pi}{2}}{\frac{\sin(x)}{\sin(x) + \cos(x)}dx} = \frac{\pi}{4}$$
