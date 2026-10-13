---
title: DS2 2023 2024 V1 Correction 
author: [MathisS]
date: 2024-04-29 01:00:00 +0100
categories: [PREING1 S2,Analyse2-DS]
tags: [PREING1 S2,Analyse2-DS,Mathis S.,DS2]
division_title : DS2
math: true
---


*Correction du DS2 d'Analyse 2 de 2023/2024 par [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*

>  *La plupart des résultats ont été vérifiés par l'outil informatique,
mais si vous constatez une erreur, merci de contacter [Mathis S.](https://cy.deltahmed.fr/contributeurs/#MathisS)*
{: .prompt-info }

## Exercice 1 : 

### 1a.

$g(x) = \frac{\left( 1 - \cos(x) \right)\ln\left( 1 + ex^{3} \right)}{x^{3}\tan(x)}$

$1 - \cos(x)\ \sim\frac{x^{2}}{2}$

$\ln\left( 1 + ex^{3} \right)\ \sim\ ex^{3}$

$\tan(x)\ \sim\ x$

$g(x)\ \sim\frac{ex}{2}$

### 1b.

$h(x) = \frac{\cos x - 1}{e^{x} - 1}$

$\cos(x) - 1\ \sim - \frac{x^{2}}{2}$

$e^{x} - 1\ \sim\ x$

$h(x)\ \sim - \frac{x}{2}$

### 2

$\lim_{x \rightarrow 0}\frac{g(x)}{h(x)} = \lim_{x \rightarrow 0}{\left( \frac{ex}{2} \right)\left( - \frac{2}{x} \right)} = \lim_{x \rightarrow 0}{- e} = - e$

## Exercice 2 : 

### 1

$x\ln(1 - x) = x\left( ( - x) - \frac{( - x)^{2}}{2} + \frac{( - x)^{3}}{3} + o\left( x^{3} \right) \right)$

$x\ln(1 - x) = x\left( - x - \frac{x^{2}}{2} - \frac{x^{3}}{3} + o\left( x^{3} \right) \right)$

$x\ln(1 - x) = - x^{2} - \frac{x^{3}}{2} - \frac{x^{4}}{3} + o\left( x^{4} \right)$

$\ln\left( \cos(x) \right) = \ln\left( 1 - \frac{x^{2}}{2} + \frac{x^{4}}{4!} + o\left( x^{4} \right) \right)$

$\text{Soit}\ u = - \frac{x^{2}}{2} + \frac{x^{4}}{4!} + o\left( x^{4} \right)$

$\ln\left( \cos(x) \right) = u - \frac{u^{2}}{2} + o\left( u^{2} \right)$

$\ln\left( \cos(x) \right) = - \frac{x^{2}}{2} + \frac{x^{4}}{4!} - \frac{x^{4}}{8} + o\left( x^{4} \right)$

$\ln\left( \cos(x) \right) = - \frac{x^{2}}{2} - \frac{x^{4}}{12} + o\left( x^{4} \right)$

$\frac{\ln\left( \cos(x) \right)}{x\ln(1 - x)} = \frac{- \frac{x^{2}}{2} - \frac{x^{4}}{12} + o\left( x^{4} \right)}{- x^{2} - \frac{x^{3}}{2} - \frac{x^{4}}{3} + o\left( x^{4} \right)}$

$f(x) = \frac{\left( - \frac{1}{2} - \frac{x^{2}}{12} + o\left( x^{2} \right) \right)}{- 1 - \frac{x}{2} - \frac{x^{2}}{3} + o\left( x^{2} \right)} = \frac{\left( \frac{1}{2} + \frac{x^{2}}{12} + o\left( x^{2} \right) \right)}{1 + \frac{x}{2} + \frac{x^{2}}{3} + o\left( x^{2} \right)}$

$\text{Soit}\ v = \frac{x}{2} + \frac{x^{2}}{3} + o\left( x^{2} \right)$

$\frac{1}{1 + v} = 1 - v + v^{2} + o\left( v^{2} \right)$

$\frac{1}{1 + v} = 1 - \frac{x}{2} - \frac{x^{2}}{3} + \frac{x^{2}}{4} + o\left( x^{2} \right) = 1 - \frac{x}{2} - \frac{x^{2}}{12} + o\left( x^{2} \right)$

$f(x) = \left( \frac{1}{2} + \frac{x^{2}}{12} + o\left( x^{2} \right) \right)\left( 1 - \frac{x}{2} - \frac{x^{2}}{12} + o\left( x^{2} \right) \right)$

$f(x) = \frac{1}{2} - \frac{x}{4} - \frac{x^{2}}{24} + \frac{2x^{2}}{24} + o\left( x^{2} \right)$

$f(x) = \frac{1}{2} - \frac{x}{4} + \frac{x^{2}}{24} + o\left( x^{2} \right)$

### 2

$\sin(x) = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} + o\left( x^{5} \right)$

$\sin^{2}(x) = x^{2} - \frac{2x^{4}}{3!} + o\left( x^{5} \right)$

$e^{x^{2}} = 1 + x^{2} + \frac{x^{4}}{2} + o\left( x^{5} \right)$

$e^{x^{2}} - 1 = x^{2} + \frac{x^{4}}{2} + o\left( x^{5} \right)$

$g(x) = \left( x^{2} - \frac{2x^{4}}{3!} + o\left( x^{5} \right) \right)\left( x^{2} + \frac{x^{4}}{2} + o\left( x^{5} \right) \right)$

$g(x) = x^{4} + o\left( x^{5} \right)$

## Exercice 3 : 

### 1

$f\ \sim_{x_{0}}g\ \text{donc}\lim_{x \rightarrow x_{0}}\frac{f(x)}{g(x)} = 1$

$g\ \sim_{x_{0}}h\ \text{donc}\lim_{x \rightarrow x_{0}}\frac{g(x)}{h(x)} = 1$

$\lim_{x \rightarrow x_{0}}\frac{f(x)}{h(x)} = \lim_{x \rightarrow x_{0}}{\frac{f(x)}{g(x)} \times \frac{g(x)}{h(x)}} = 1$

Donc $f\ \sim_{x_{0}}h$

### 2

$f(x) = o\left( x^{n} \right)$

$\lim_{x \rightarrow 0}\frac{f(x)}{x^{n}} = 0$

$m \leq n \Rightarrow n = m + p\ \text{où}\ p \geq 0$

$\lim_{x \rightarrow 0}\frac{f(x)}{x^{m}} = \lim_{x \rightarrow 0}\frac{f(x)}{x^{n - p}} = \lim_{x \rightarrow 0}\frac{f(x)x^{p}}{x^{n}} = \lim_{x \rightarrow 0}\frac{f(x)}{x^{n}} \times \lim_{x \rightarrow 0}x^{p} = 0 \times \lim_{x \rightarrow 0}x^{p} = 0$

$\text{Donc}\ f(x) = o\left( x^{m} \right)$

### 3

Soit $u = \frac{1}{x}$

$\lim_{x \rightarrow + \infty}\left( \frac{\sqrt{1 + x}}{x} \right) = \lim_{x \rightarrow + \infty}\frac{\sqrt{x\left( 1 + \frac{1}{x} \right)}}{x} = \lim_{x \rightarrow + \infty}{\left( \frac{\sqrt{x}}{x} \right)\sqrt{1 + \frac{1}{x}}} = \lim_{x \rightarrow + \infty}{\left( \frac{1}{\sqrt{x}} \right)\sqrt{1 + \frac{1}{x}}} = 0$

$\text{Donc}\ \sqrt{1 + x} = o(x)$

$\ln\left( x + \sqrt{1 + x} \right) = \ln\left( x + o_{+ \infty}(x) \right) = \ln\left( x\left( 1 + o_{+ \infty}(1) \right) \right) = \ln(x) + \ln\left( 1 + o_{+ \infty}(1) \right)$

$\lim_{x \rightarrow + \infty}\frac{\ln\left( x + \sqrt{1 + x} \right)}{\ln(x)} = \lim_{x \rightarrow + \infty}\frac{\ln(x) + \ln\left( 1 + o_{+ \infty}(1) \right)}{\ln(x)} = \lim_{x \rightarrow + \infty}{1 + \frac{\ln\left( 1 + o_{+ \infty}(1) \right)}{\ln(x)}} = 1$

$\text{Donc }\ln\left( x + \sqrt{1 + x} \right)\sim\ln(x)$

## Exercice 4 : 

### 1

$\forall n \geq 2,\ \ \ln(n + 1)u_{n} - \ln(n)u_{n - 1} = n$

$u_{1} = 0$

$2 = \ln(3)u_{2} - \ln(2)u_{1}$

$3 = \ln(4)u_{3} - \ln(3)u_{2}$

$n - 1 = \ln(n)u_{n - 1} - \ln(n - 1)u_{n - 2}$

$n = \ln(n + 1)u_{n} - \ln(n)u_{n - 1}$

Par somme,

$\sum_{k = 2}^{n}k = \ln(n + 1)u_{n} - \ln(2)u_{1}$

$\sum_{k = 2}^{n}k = \ln(n + 1)u_{n}$

$u_{n} = \left( \frac{1}{\ln(n + 1)} \right)\sum_{k = 2}^{n}k$

$\sum_{k = 2}^{n}k = \frac{n(n + 1)}{2} - 1\ \sim_{+ \infty}\frac{n^{2}}{2}$

$\ln(n + 1)\ \sim_{+ \infty}\ln(n)$

$u_{n}\ \sim_{+ \infty}\frac{n^{2}}{2\ln(n)}$

### 2

$\left( \begin{array}{r}
n \\
5
\end{array} \right) = \frac{n!}{5!(n - 5)!} = \frac{n(n - 1)(n - 2)(n - 3)(n - 4)}{5!}$

$n(n - 1)(n - 2)(n - 3)(n - 4) = n^{5} + o_{+ \infty}\left( n^{5} \right)$

$n(n - 1)(n - 2)(n - 3)(n - 4)\ \sim_{+ \infty}\ n^{5}$

$5! = 120$

$\left( \begin{array}{r}
n \\
5
\end{array} \right)\sim_{+ \infty}\frac{n^{5}}{120}$

### 3

$v_{n} = 4n\left( 1 - \cos\left( \frac{1}{n^{3}} \right) \right)$

$1 - \cos(X)\ \sim_{0}\frac{X^{2}}{2}$

$1 - \cos\left( \frac{1}{n^{3}} \right)\ \sim_{+ \infty}\frac{1}{2n^{6}}$

$v_{n}\sim_{+ \infty}\frac{2}{n^{5}}$

### 4

$\lim_{n \rightarrow + \infty}{\left( \begin{array}{r}
n \\
5
\end{array} \right)v_{n}}\ $

$\left( \begin{array}{r}
n \\
5
\end{array} \right)v_{n}\ \sim\frac{1}{60}$

$\lim_{n \rightarrow + \infty}{\left( \begin{array}{r}
n \\
5
\end{array} \right)v_{n}} = \frac{1}{60}$