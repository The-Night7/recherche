---
title: DS3 2023 2024 Correction
author: [MathisS]
date: 2025-05-25 01:02:39 +0200
categories: [PREING2 S2,Integration-proba-DS]
tags: [PREING2 S2,Integration-proba-DS,DS3,Mathis S.,Correction]
division_title : DS3
math: true
---



# **Exercice 2**

## 1\.

On utilise la formule des probabilités totales. $$\left\lbrack  B_{1},B_{2},B_{3} \right\rbrack $$

$$\mathbb{P}(D)\mathbb{= P}\left( D \cap B_{1} \right)\mathbb{+ P}\left( D \cap B_{2} \right)\mathbb{+ P}\left( D \cap B_{3} \right)$$

$$\mathbb{P}(D)\mathbb{= P}\left( B_{1} \right)\mathbb{\times P}\left( D \middle\vert  B_{1} \right)\mathbb{+ P}\left( B_{2} \right)\mathbb{\times P}\left( D \middle\vert  B_{2} \right)\mathbb{+ P}\left( B_{3} \right)\mathbb{\times P}\left( D \middle\vert  B_{3} \right)$$

$$\mathbb{P}(D) = 0.15 \times 0.02 + 0.8 \times 0.01 + 0.05 \times 0.03 $$

$$\mathbb{P}(D) = 0.003 + 0.008 + 0.0015 = 0.0125 = \frac{1}{80}$$

## 2\.

$$\mathbb{P}\left( \overline{D} \right) = 1 - \mathbb{P}(D) = \frac{79}{80}$$

Le nombre de microprocesseurs reçus non défectueux est de $$2000 \times \mathbb{P}\left( \overline{D} \right) = 1975$$

## 3\.

On cherche $$\mathbb{P}\left( B_{3} \middle\vert  D \right)$$

D'après la formule de Bayes,

$$\mathbb{P}\left( B_{3} \middle\vert  D \right) = \frac{\mathbb{P}\left( D \middle\vert  B_{3} \right)\mathbb{P}\left( B_{3} \right)}{\mathbb{P}(D)} = 80 \times \frac{3}{100} \times \frac{1}{20} = \frac{12}{100} = \frac{3}{25} = 0.12$$

La probabilité qu'un microprocesseur provienne du fournisseur 3 sachant qu'il est défectueux est de $$0.12$$

## 4\.

On cherche $$\mathbb{P}\left( D \cap B_{3} \right)\mathbb{= P}\left( D \middle\vert  B_{3} \right)\mathbb{P}\left( B_{3} \right) = 0.03 \times 0.05 = 0.0015 = \frac{15}{10000} = \frac{3}{2000}$$

Le nombre de microprocesseurs défectueux provenant du fournisseur 3 est de $$2000 \times \frac{3}{2000} = 3$$

## 5\.

On cherche

$$\mathbb{P}\left( \overline{B_{3}} \middle\vert  \overline{D} \right)\mathbb{= P}\left( B_{1} \middle\vert  \overline{D} \right)\mathbb{+ P}\left( B_{2} \middle\vert  \overline{D} \right) $$
$$= \frac{\mathbb{P}\left( \overline{D} \middle\vert  B_{1} \right)\mathbb{P}\left( B_{1} \right)\mathbb{+ P}\left( \overline{D} \middle\vert  B_{2} \right)\mathbb{P}\left( B_{2} \right)}{\mathbb{P}\left( \overline{D} \right)} $$
$$= \frac{\left( 1 - \mathbb{P}\left( D \middle\vert  B_{1} \right) \right)\mathbb{P}\left( B_{1} \right) + \left( 1 - \mathbb{P}\left( D \middle\vert  B_{2} \right) \right)\mathbb{P}\left( B_{2} \right)}{1 - \mathbb{P}(D)} $$
$$= (0.98 \times 0.15 + 0.99 \times 0.8) \times \frac{80}{79} $$
$$= (0.147 + 0.792) \times \frac{80}{79} = 0.939 \times \frac{80}{79} $$
$$= \frac{939}{1000} \times \frac{80}{79} $$
$$= \frac{939 \times 8}{79 \times 100} $$
$$= \frac{939 \times 2}{79 \times 25} = \frac{1878}{1975}$$

$$\mathbb{P}\left( \overline{B_{3}} \middle\vert  \overline{D} \right) $$
$$= 1 - \mathbb{P}\left( B_{3} \middle\vert  \overline{D} \right) $$
$$= 1 - \frac{\mathbb{P}\left( \overline{D} \middle\vert  B_{3} \right)\mathbb{P}\left( B_{3}\right)}{\mathbb{P}\left( \overline{D} \right)} $$
$$= 1 - \frac{\left( 1 - \mathbb{P}\left( D \middle\vert  B_{3} \right) \right)\mathbb{P}\left( B_{3} \right)}{\mathbb{P}\left( \overline{D} \right)} $$
$$= 1 - 0.97 \times 0.05 \times \frac{80}{79} $$
$$= 1 - \frac{97 \times 5 \times 80}{10000 \times 79} = 1 - \frac{97 \times 80}{2000 \times 79} $$
$$= 1 - \frac{97 \times 8}{200 \times 79} $$
$$= 1 - \frac{97 \times 2}{50 \times 79} = 1 - \frac{97}{25 \times 79} = 1 - \frac{97}{1975} = \frac{1878}{1975}$$

# **Exercice 3 :**

## 1\.

Pour que $$\left( k,\ P_{X}(k) \right)_{k \in \left. ⟦ - 4,4 \right.⟧}$$ soit la loi de probabilité de $$X$$, on doit avoir $$\sum_{k \in \left. ⟦ - 4,4 \right.⟧}^{}{P_{X}(k)} = 1$$

$$\Leftrightarrow 0.1 + 0.15 + 0.2 + 0.05 + 0.1 + 0.15 + 0.05 + 0.1 + \beta = 1$$

$$\Leftrightarrow 0.9 + \beta = 1$$

$$\Leftrightarrow \beta = 0.1$$

## 2\.

Soit $$F\mathbb{:R \rightarrow}\lbrack 0,1\rbrack$$ la fonction de répartition de $$X$$.

$$\forall x\mathbb{\in R,\ }F(x)\mathbb{= P}(X \leq x)$$

$$\Leftrightarrow F(x) = \left\lbrack  \begin{array}{r}
0\ \text{si}\ x < - 4 \\
0.1\ \text{si}\ x \in \left\lbrack - 4, - 3 \right\lbrack \\
0.25\ \text{si}\ x \in \left\lbrack - 3, - 2 \right\lbrack \\
0.45\ \text{si}\ x \in \left\lbrack - 2, - 1 \right\lbrack \\
0.5\ \text{si}\ x \in \left\lbrack - 1,0 \right\lbrack \\
0.6\ \text{si}\ x \in \left\lbrack 0,1 \right\lbrack \\
0.75\ \text{si}\ x \in \left\lbrack 1,2 \right\lbrack \\
0.8\ \text{si}\ x \in \left\lbrack 2,3 \right\lbrack \\
0.9\ \text{si}\ x \in \left\lbrack 3,4 \right\lbrack \\
1\ \text{si}\ x \geq 4
\end{array} \right. $$

## 3\.

$$\mathbb{E}(X) = \sum_{k \in \left. ⟦ - 4,4 \right.⟧}^{}{k\mathbb{P}(X = k)} $$
$$= - 4 \times 0.1 - 3 \times 0.15 - 2 \times 0.2 - 1 \times 0.05 + 1 \times 0.15 + 2 \times 0.05 + 3 \times 0.1 + 4 \times 0.1 $$
$$= - 0.4 - 0.45 - 0.4 - 0.05 + 0.15 + 0.1 + 0.3 + 0.4 $$
$$= - 0.35$$

D'après la formule de Koenig-Huygens,

$$\mathbb{V}(X)\mathbb{= E}\left( X^{2} \right)\mathbb{- E}(X)^{2}$$

$$\mathbb{E}\left( X^{2} \right) = \sum_{k \in \left. ⟦ - 4,4 \right.⟧}^{}{k^{2}\mathbb{P}(X = k)} $$
$$= 16 \times 0.1 + 9 \times 0.15 + 4 \times 0.2 + 1 \times 0.05 + 1 \times 0.15 + 4 \times 0.05 + 9 \times 0.1 + 16 \times 0.1 $$
$$= 1.6 + 1.35 + 0.8 + 0.05 + 0.15 + 0.2 + 0.9 + 1.6 = 6.65$$

$$\mathbb{E}(X)^{2} = {0.35}^{2} = 0.1225$$

$$\mathbb{V}(X)\mathbb{= E}\left( X^{2} \right)\mathbb{- E}(X)^{2} = 6.5275$$

$$\mathbb{P}( - 1 \leq X < 4.5) = \sum_{k \in \left. ⟦ - 1,4 \right.⟧}^{}{\mathbb{P}(X = k)} = 0.05 + 0.1 + 0.15 + 0.05 + 0.1 + 0.1 = 0.55$$

$$\mathbb{P}( - 1 \leq X < 4.5) = 0.55$$

## 4\.

| $$k$$                | $$1$$      | $$2$$      | $$5$$      | $$10$$     | $$17$$     |
|:--------------------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| $$\mathbb{P}_{Z}(k)$$ | $$0.1$$    | $$0.2$$    | $$0.25$$   | $$0.25$$   | $$0.2$$    |



## 5\.

$$\mathbb{E}(Z) = \sum_{k \in \left\lbrack  1,2,5,10,17 \right\rbrack }^{}{k\mathbb{P}(Z = k)} $$
$$= 1 \times 0.1 + 2 \times 0.2 + 5 \times 0.25 + 10 \times 0.25 + 17 \times 0.2 $$
$$= 0.1 + 0.4 + 1.25 + 2.5 + 3.4 = 7.65$$

$$\text{Ou :}\mathbb{\ E}(Z)\mathbb{= E}\left( X^{2} + 1 \right)\mathbb{= E}\left( X^{2} \right)\mathbb{+ E}(1) = 6.65 + 1 = 7.65$$

# **Exercice 4 :**

On note $$A$$ la probabilité que pour tous les lancers, la somme des dés est paire.

$$\forall i,j \in \mathbb{N}^{*},\ i \neq j,\ A_{i}\ \text{et}\ A_{j}\ \text{sont incompatibles}$$

Pour chaque lancer, la probabilité d'obtenir une somme paire de dés sauf $$(4,6),(5,5),(6,4)$$ est de $$\frac{15}{36} = \frac{5}{12}$$.

$$\forall k \in \mathbb{N}^{*}\mathbb{,\ P}\left( A_{k} \right) = \frac{3}{36} \times \left( \frac{15}{36} \right)^{k - 1}$$

$$A = \bigcup_{k = 1}^{+ \infty}A_{k}$$

$$\mathbb{P}(A) = \sum_{k = 1}^{+ \infty}{\left( \frac{3}{36} \right)\left( \frac{5}{12} \right)^{k - 1}} $$
$$= \frac{3}{36}\sum_{k = 1}^{+ \infty}\left( \frac{5}{12} \right)^{k - 1} $$
$$= \frac{3}{36}\sum_{k = 0}^{+ \infty}\left( \frac{5}{12} \right)^{k} = \frac{3}{36} \times \frac{12}{7} = \frac{1}{7}$$

$$\mathbb{P}(A) = \frac{1}{7}$$
