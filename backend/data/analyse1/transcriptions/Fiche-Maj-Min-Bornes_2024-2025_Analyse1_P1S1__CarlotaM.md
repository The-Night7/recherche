---
source: PREING1-S1/Analyse1/Fiche-Maj-Min-Bornes_2024-2025_Analyse1_P1S1__CarlotaM.pdf
pages: 1
transcription: manuelle
---

# Analyse 1 — Majorants, minorants, bornes et densité

## Majorant, minorant, maximum et minimum

Pour une partie $A$ de $\mathbb R$ :

- $M$ est un **majorant** si $x\le M$ pour tout $x\in A$.
- $m$ est un **minorant** si $m\le x$ pour tout $x\in A$.
- $A$ est **bornée** s'il existe $m,M$ tels que $m\le x\le M$ pour tout $x\in A$.
- Un **maximum** est un majorant de $A$ appartenant à $A$.
- Un **minimum** est un minorant de $A$ appartenant à $A$.

**Unicité du maximum.** Si $M,M'$ sont deux plus grands éléments de $A$, alors $M'\le M$, car $M$ majore $A$, et $M\le M'$, car $M'$ majore $A$. Donc $M=M'$.

## Borne supérieure et borne inférieure

$\sup A$ est le plus petit des majorants ; $\inf A$ est le plus grand des minorants. Ces bornes n'appartiennent pas nécessairement à $A$ : par exemple, pour $A=]a,b[$ avec $a<b$, les bornes sont $a$ et $b$.

Si $A$ possède un maximum, $\sup A=\max A$. Si elle possède un minimum, $\inf A=\min A$. Lorsque les bornes existent,

$$A\text{ possède un maximum}\iff\sup A\in A,$$

$$A\text{ possède un minimum}\iff\inf A\in A.$$

> **Rectification de la source :** la deuxième ligne manuscrite répète « plus grand élément » à côté de $\inf A$ ; il faut « plus petit élément ».

| Ensemble $A$ | $\min A$ | $\inf A$ | $\max A$ | $\sup A$ |
| --- | --- | --- | --- | --- |
| $\{1\}$ | $1$ | $1$ | $1$ | $1$ |
| $\{2,4\}$ | $2$ | $2$ | $4$ | $4$ |
| $[-5,0[$ | $-5$ | $-5$ | n'existe pas | $0$ |
| $\{1/n:n\in\mathbb N^*\}$ | n'existe pas | $0$ | $1$ | $1$ |

**Caractérisation.** $M=\sup A$ signifie que $M$ majore $A$ et que tout majorant $M'$ vérifie $M\le M'$. De façon équivalente, $M$ majore $A$ et

$$\forall y<M,\ \exists x\in A:\ y<x,$$

ou encore

$$\forall\varepsilon>0,\ \exists x\in A:\ M-\varepsilon<x.$$

## Opérations sur les bornes supérieures

Pour des ensembles non vides et majorés $A,B$, et $\lambda>0$ :

$$A\subseteq B\Longrightarrow\sup A\le\sup B,$$

$$\sup(A\cup B)=\max(\sup A,\sup B),$$

$$\sup(A+B)=\sup A+\sup B,\qquad A+B=\{a+b:a\in A,b\in B\},$$

$$\sup(\lambda A)=\lambda\sup A,\qquad\lambda A=\{\lambda a:a\in A\}.$$

**Méthode indiquée sur la fiche.** Pour passer d'une majoration valable pour chaque $b\in B$ à une majoration de $\sup B$, on utilise que $\sup B$ est le plus petit majorant. Ainsi, si tout $b\in B$ vérifie $b\le\sup(A+B)-\sup A$, alors $\sup B\le\sup(A+B)-\sup A$.

## Propriété d'Archimède et partie entière

Pour tout $x\in\mathbb R$, il existe un unique entier $n$ tel que

$$n\le x<n+1.$$

Cet entier est la **partie entière** de $x$, notée $E(x)$, $[x]$ ou $\lfloor x\rfloor$. On a

$$x-1<\lfloor x\rfloor\le x<\lfloor x\rfloor+1.$$

**Unicité.** Si $n_1\le x<n_1+1$ et $n_2\le x<n_2+1$, alors $-1<n_1-n_2<1$. Puisque $n_1-n_2$ est entier, il vaut zéro.

Le graphique représente la fonction en escalier $x\mapsto\lfloor x\rfloor$, constante sur chaque $[n,n+1[$.

## Densité et approximations décimales

Une partie $A\subseteq\mathbb R$ est **dense** dans $\mathbb R$ si tout intervalle ouvert non vide contient un élément de $A$ :

$$\forall x<y,\ \exists a\in A:\ x<a<y.$$

De façon équivalente,

$$\forall x\in\mathbb R,\ \forall\varepsilon>0,\ \exists u\in A:\ |u-x|<\varepsilon.$$

> **Rectification de la source :** les éléments approchants doivent appartenir à $A$, et pas seulement à $\mathbb R$.

$\mathbb Q$ et $\mathbb R\setminus\mathbb Q$ sont denses dans $\mathbb R$.

Posons $p_n=\lfloor10^n x\rfloor$. Alors

$$p_n\le10^n x<p_n+1\quad\Longrightarrow\quad
\frac{p_n}{10^n}\le x<\frac{p_n+1}{10^n}.$$

Le premier quotient est l'approximation décimale par défaut à la précision $10^{-n}$ ; le second donne une approximation par excès.

Exemples d'écritures décimales indiqués : écriture finie $0{,}56$, écriture infinie non périodique $\pi$, écriture périodique $0{,}\overline3$.
