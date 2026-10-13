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

Exercices : [1](#1) [2](#2) [3](#3) [4](#7)

## Exercice 1 :

<div id="1"></div>

![page 1](https://data2.cy.deltahmed.fr/DATA/imgofpdf/DS1-2023-2024-V1-Correction_Serie-DSp2s1-2024-2025/DS1-2023-2024-V1-Correction_Serie-DSp2s10.jpg)

## Exercice 2 :

<div id="2"></div>

![page 2](https://data2.cy.deltahmed.fr/DATA/imgofpdf/DS1-2023-2024-V1-Correction_Serie-DSp2s1-2024-2025/DS1-2023-2024-V1-Correction_Serie-DSp2s11.jpg)

## Exercice 3 :

<div id="3"></div>

![page 3](https://data2.cy.deltahmed.fr/DATA/imgofpdf/DS1-2023-2024-V1-Correction_Serie-DSp2s1-2024-2025/DS1-2023-2024-V1-Correction_Serie-DSp2s12.jpg)

<div id="4"></div>

![page 4](https://data2.cy.deltahmed.fr/DATA/imgofpdf/DS1-2023-2024-V1-Correction_Serie-DSp2s1-2024-2025/DS1-2023-2024-V1-Correction_Serie-DSp2s13.jpg)

<div id="5"></div>

![page 5](https://data2.cy.deltahmed.fr/DATA/imgofpdf/DS1-2023-2024-V1-Correction_Serie-DSp2s1-2024-2025/DS1-2023-2024-V1-Correction_Serie-DSp2s14.jpg)

<div id="6"></div>

![page 6](https://data2.cy.deltahmed.fr/DATA/imgofpdf/DS1-2023-2024-V1-Correction_Serie-DSp2s1-2024-2025/DS1-2023-2024-V1-Correction_Serie-DSp2s15.jpg)

<div id="7"></div>

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

On ne peut pas aller plus loin a cause d'une erreur dans l’énoncé.

Pages : Exercices : [1](#1) [2](#2) [3](#3) [4](#7)
