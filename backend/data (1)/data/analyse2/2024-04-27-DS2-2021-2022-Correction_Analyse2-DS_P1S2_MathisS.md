---
title: DS2 2021 2022 Correction
author: [MathisS]
date: 2024-04-27 01:00:00 +0100
categories: [PREING1 S2,Analyse2-DS]
tags: [PREING1 S2,Analyse2-DS,Mathis S.,DS2]
division_title : DS2
math: true
---

*Correction du DS2 d'Analyse 2 de 2021/2022 par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La plupart des résultats ont été vérifiés par l'outil informatique,
mais si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-info }

## Exercice 1 : 

### 1.

$\sqrt{n^{4} + 1} - n^{2} = n^{2}\left( \sqrt{1 + \frac{1}{n^{4}}} - 1 \right)$

$\text{Or, avec}\ X \rightarrow 0,\ \left( \sqrt{1 + X} - 1 \right)\ \sim\frac{X}{2},\ \text{donc}\ \left( \sqrt{1 + \frac{1}{n^{4}}} - 1 \right)\ \sim\frac{1}{2n^{4}}$

$\text{Ainsi}\ \left( \sqrt{n^{4} + 1} - n^{2} \right)\ \sim\frac{1}{2n^{2}}$

$\text{Aussi}\text{, avec}\ X \rightarrow 0,\ (e^{X} - 1)\ \sim\ X,\ \text{donc}\ \left( \exp\left( \frac{( - 1)^{n}}{n} \right) - 1 \right)\ \sim\frac{( - 1)^{n}}{n}$

Par quotient,

$u_{n}\ \sim\frac{( - 1)^{n}}{2n}$

### 2.

$\ln\left( 1 + \sin(x) \right)\ \sim_{x \rightarrow 0}\sin(x)\ \sim_{x \rightarrow 0}\ x$

$\sin\left( \pi x^{2} \right)\ \sim_{0}\ \pi x^{2}$

$f(x)\ \sim_{x \rightarrow 0}\frac{1}{\pi x}$

### 3.

$g(x) = \frac{\sin(x)\left( \cos(x) - 1 \right)}{\left( x^{4} + x^{5} \right)\left( \cos(\pi x) \right)}$

$\sin(x)\ \sim_{0}\ x$

$\cos(x) - 1\ \sim_{0}\ \left( - \frac{x^{2}}{2} \right)$

$\left( x^{4} + x^{5} \right)\ \sim_{0}\ x^{4}$

$\cos(\pi x)\ \sim_{0}\ 1$

$g(x)\ \sim_{0}\ x\left( - \frac{x^{2}}{2} \right)\left( \frac{1}{x^{4}} \right) = - \frac{1}{2x}$

$g(x)\ \sim_{x \rightarrow 0}\left( - \frac{1}{2x} \right)$

## Exercice 2 : 

###  1.a.

$\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^{2}}{8} + o\left( x^{2} \right)$

$\frac{1}{1 + x + x^{2}} = 1 - \left( x + x^{2} \right) + \left( x + x^{2} \right)^{2} + o\left( x^{2} \right) = 1 - x + o\left( x^{2} \right)$

$\frac{\sqrt{1 + x}}{1 + x + x^{2}} = \left( 1 + \frac{x}{2} - \frac{x^{2}}{8} \right)(1 - x) + o\left( x^{2} \right) = 1 - x + \frac{x}{2} - \frac{x^{2}}{2} - \frac{x^{2}}{8} + o\left( x^{2} \right)$

$g_{1}(x) = 1 - \frac{x}{2} - \frac{5x^{2}}{8} + o\left( x^{2} \right)$

### 1.b.

$f(x) = - \frac{5x^{2}}{8} + o\left( x^{2} \right)$

$f(x)\ \sim_{x \rightarrow 0} - \frac{5x^{2}}{8}$

### 2.

$g_{2}(x) = e^{\frac{\ln(1 + x)}{x}}$

$\ln(1 + x) = x - \frac{x^{2}}{2} + \frac{x^{3}}{3} + o\left( x^{3} \right)$

$\frac{\ln(1 + x)}{x} = 1 - \frac{x}{2} + \frac{x^{2}}{3} + o\left( x^{2} \right)$

$\text{On pose}\ X = - \frac{x}{2} + \frac{x^{2}}{3} + o\left( x^{2} \right)$

$e^{\frac{\ln(1 + x)}{x}} = e^{1 + X} = e\left( e^{X} \right) = e\left( 1 + X + \frac{X^{2}}{2} + o\left( X^{2} \right) \right)$

$g_{2}(x) = e\left( 1 + \left( - \frac{x}{2} + \frac{x^{2}}{3} \right) + \frac{1}{2}\left( - \frac{x}{2} + \frac{x^{2}}{3} \right)^{2} \right) + o\left( x^{2} \right)$

$g_{2}(x) = e\left( 1 - \frac{x}{2} + \frac{x^{2}}{3} + \frac{x^{2}}{8} \right) + o\left( x^{2} \right)$

$g_{2}(x) = e - \frac{e}{2}x + \frac{11e}{24}x^{2} + o\left( x^{2} \right)$

### 3.

Faire un DL de $g_{3}(x)$ au voisinage de $\frac{\pi}{2}$ revient à
faire un DL de $g_{3}\left( x + \frac{\pi}{2} \right)$ en 0.

$g_{3}\left( x + \frac{\pi}{2} \right) = e^{x + \frac{\pi}{2}}\sin\left( x + \frac{\pi}{2} \right) = e^{\frac{\pi}{2}}e^{x}\cos(x)$

$e^{x} = 1 + x + \frac{x^{2}}{2} + o\left( x^{2} \right)$

$\cos(x) = 1 - \frac{x^{2}}{2} + o\left( x^{2} \right)$

$g_{3}\left( x + \frac{\pi}{2} \right) = e^{\frac{\pi}{2}}\left( 1 + x + \frac{x^{2}}{2} \right)\left( 1 - \frac{x^{2}}{2} \right) + o\left( x^{2} \right)$

$g_{3}\left( x + \frac{\pi}{2} \right) = e^{\frac{\pi}{2}}\left( 1 - \frac{x^{2}}{2} + x + \frac{x^{2}}{2} \right) + o\left( x^{2} \right)$

$g_{3}\left( x + \frac{\pi}{2} \right) = e^{\frac{\pi}{2}} + e^{\frac{\pi}{2}}x + o\left( x^{2} \right)$

$g_{3}(x) = e^{\frac{\pi}{2}} + e^{\frac{\pi}{2}}\left( x - \frac{\pi}{2} \right) + o\left( \left( x - \frac{\pi}{2} \right)^{2} \right)$

## Exercice 3 : 

### 1.

$\cos\left( \frac{1}{n^{2}} \right) - 1\ \sim - \frac{1}{2n^{4}}$

$n^{2}\left( \cos\left( \frac{1}{n^{2}} \right) - 1 \right)\ \sim - \frac{1}{2n^{2}}$

$\lim_{n \rightarrow + \infty}{\ln\left( 1 + \frac{1}{n} \right)} = 0,\ \text{donc}\sin\left( \ln\left( 1 + \frac{1}{n} \right) \right)\ \sim\ln\left( 1 + \frac{1}{n} \right)\ \sim\frac{1}{n}$

$\frac{n^{2}\left( \cos\left( \frac{1}{n^{2}} \right) - 1 \right)}{\sin\left( \ln\left( 1 + \frac{1}{n} \right) \right)}\ \sim - \frac{1}{2n}$

$\lim_{n \rightarrow + \infty}\frac{n^{2}\left( \cos\left( \frac{1}{n^{2}} \right) - 1 \right)}{\sin\left( \ln\left( 1 + \frac{1}{n} \right) \right)} = 0$

### 2.

$\sin\left( \frac{\pi}{n} \right)\ \sim\frac{\pi}{n}$

$\ln\left( 1 + \frac{2}{n} \right)\ \sim\frac{2}{n}$

$\ln\left( 1 + \frac{3}{n} \right)\ \sim\frac{3}{n}$

$\frac{n\sin\left( \frac{\pi}{n} \right)\ln\left( 1 + \frac{2}{n} \right)}{\ln\left( 1 + \frac{3}{n} \right)}\ \sim\frac{2\pi}{3}$

$\lim_{n \rightarrow + \infty}\frac{n\sin\left( \frac{\pi}{n} \right)\ln\left( 1 + \frac{2}{n} \right)}{\ln\left( 1 + \frac{3}{n} \right)} = \frac{2\pi}{3}$

### 3.

$\sin(x) = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} + o\left( x^{5} \right)$

$\cos(x) = 1 - \frac{x^{2}}{2} + \frac{x^{4}}{4!} + o\left( x^{4} \right)$

$3\sin(x) - x\cos(x) - 2x = 3x - \frac{x^{3}}{2} + \frac{x^{5}}{40} - x + \frac{x^{3}}{2} - \frac{x^{5}}{24} - 2x + o\left( x^{5} \right)$

$3\sin(x) - x\cos(x) - 2x = x^{5}\left( \frac{1}{40} - \frac{1}{24} \right) = - \frac{x^{5}}{60} + o\left( x^{5} \right) = x^{5}\left( - \frac{1}{60} + o(1) \right)$

$\pi x^{5} + x^{6} = x^{5}(\pi + x)$

$\frac{3\sin(x) - x\cos(x) - 2x}{\pi x^{5} + x^{6}} = \frac{- \frac{1}{60} + o(1)}{\pi + x}$

$\lim_{x \rightarrow 0}\frac{3\sin(x) - x\cos(x) - 2x}{\pi x^{5} + x^{6}} = - \frac{1}{60\pi}$

### 4.

$\ln(1 + 2x) = 2x - \frac{(2x)^{2}}{2} + o\left( x^{2} \right) = 2x - 2x^{2} + o\left( x^{2} \right)$

$e^{2x} = 1 + 2x + \frac{(2x)^{2}}{2} = 1 + 2x + 2x^{2} + o\left( x^{2} \right)$

$1 - \cos(x) = \frac{x^{2}}{2} + o\left( x^{2} \right)$

$1 + \ln(1 + 2x) - e^{2x} = - 4x^{2} + o\left( x^{2} \right)$

$\frac{1 + \ln(1 + 2x) - e^{2x}}{1 - \cos(x)} = \frac{- 4x^{2} + o\left( x^{2} \right)}{\frac{x^{2}}{2} + o\left( x^{2} \right)} = \frac{- 4 + o(1)}{\frac{1}{2} + o(1)}$

$\lim_{x \rightarrow 0}\frac{1 + \ln(1 + 2x) - e^{2x}}{1 - \cos(x)} = - 8$

## Exercice 4 : 

### 1.

$f(x) = \sqrt{\frac{\left( \frac{1}{v} \right)^{3}}{\frac{1}{v} + 1}} = \sqrt{\frac{1}{v^{2} + v^{3}}}$

$f(x) = \sqrt{\frac{1}{v^{2}(1 + v)}}$

$f(x) = \frac{1}{v}\sqrt{\frac{1}{1 + v}}$

$f(x) = \frac{1}{v}\sqrt{1 - v + v^{2} + o_{v \rightarrow 0}\left( v^{2} \right)}$

Soit $u = - v + v^{2} + o_{v \rightarrow 0}\left( v^{2} \right)$

$\sqrt{1 + u} = 1 + \frac{u}{2} - \frac{u^{2}}{8} + o_{u \rightarrow 0}\left( u^{2} \right)$

$\sqrt{1 - v + v^{2} + o_{v \rightarrow 0}\left( v^{2} \right)} = 1 + \frac{1}{2}\left( - v + v^{2} \right) - \frac{1}{8}\left( - v + v^{2} \right)^{2} + o_{v \rightarrow 0}\left( v^{2} \right)$

$\sqrt{1 - v + v^{2} + o_{v \rightarrow 0}\left( v^{2} \right)} = 1 - \frac{v}{2} + \frac{3}{8}v^{2} + o_{v \rightarrow 0}\left( v^{2} \right)$

$f(x) = \frac{1}{v} - \frac{1}{2} + \frac{3}{8}v + o_{v \rightarrow 0}(v)$

$f(x) = x - \frac{1}{2} + \frac{3}{8x} + o_{x \rightarrow + \infty}\left( \frac{1}{x} \right)$

### 2.

Une asymptote oblique de $C_{f}$ en $+ \infty$ est de forme :

$y = x - \frac{1}{2}$

### 3.

$f(x) - \left( x - \frac{1}{2} \right) = \frac{3}{8x} + o\left( \frac{1}{x} \right)\ \sim\frac{3}{8x} > 0$

Donc $C_{f}$ est au-dessus de l'asymptote oblique.

