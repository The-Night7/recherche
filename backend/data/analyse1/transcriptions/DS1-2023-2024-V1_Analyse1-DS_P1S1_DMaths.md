# Analyse 1 — DS1 2023–2024, sujet corrigé (13 novembre 2023)

> Sources : `PREING1-S1/Analyse1-DS/DS1-2023-2024-V1_Analyse1-DS_P1S1_DMaths.pdf` et `PREING1-S1/Analyse1-DS/DS1-2023-2024_Analyse1-DS_P1S1_DMaths.pdf`, copies binaires identiques ; 5 pages (PDF natif).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. Dans la source, les énoncés sont en noir et les solutions en rouge. Ici, les énoncés sont en **gras** et les solutions en texte courant.
> Vérification : les calculs ont été refaits et les résultats sont justes. Lacunes de la source :
> - **Exercice 2.1** : la phrase « Soit $r=$. » est incomplète ; il faut lire « Soit $r=2{,}71\overline{18}$ ». La fraction $\frac{26847}{9900}$ n’est pas réduite : elle vaut $\frac{2983}{1100}$.
> - **Exercice 4.2** : la source ne dit pas que $A$ n’a pas de plus grand élément ($8\notin A$).
> - Coquilles conservées : « $A=,\{\dots\}$ », « dont les développement décimal périodiques », « décaler de 2 chiffre », « possede », « majorée par par ».

**Préing 1 — Devoir Surveillé 1 — Analyse I**

| Date | Durée | Nombre de pages |
| --- | --- | --- |
| 13/11/2023 | 1 h 00 | 2 |

L’usage de tout appareil électronique est interdit.

**Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.** *Le sujet comporte 4 exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.*

## Exercice 1 (4 points)

**Choisir deux des trois questions suivants. Résoudre, dans $\mathbb R$, les équations et inéquations suivantes :**

### 1. $\sin\left(2x-\frac\pi3\right)=\cos\left(\frac x3\right)$.

**Solutions :** Nous avons

$$\sin\left(2x-\frac\pi3\right)=\cos\left(\frac x3\right)=\sin\left(\frac\pi2-\frac x3\right).$$

Par conséquent, $\sin\left(2x-\frac\pi3\right)=\cos\left(\frac x3\right)$ si et seulement si

$$\begin{aligned}
&2x-\frac\pi3\equiv\frac\pi2-\frac x3\ [2\pi]\ \text{ ou }\ 2x-\frac\pi3\equiv\pi-\frac\pi2+\frac x3\ [2\pi]\\
\iff&\frac{7x}3=\frac{5\pi}6+2k\pi,\ k\in\mathbb Z\ \text{ ou }\ \frac{5x}3=\frac{5\pi}6+2k\pi,\ k\in\mathbb Z\\
\iff&x=\frac{5\pi}{14}+\frac{6k\pi}7,\ k\in\mathbb Z\ \text{ ou }\ x=\frac\pi2+\frac{6k\pi}5,\ k\in\mathbb Z
\end{aligned}$$

### 2. $2\cos^2(x)+9\cos(x)+4=0$.

**Solutions :** Nous avons

$$0=2\cos^2(x)+9\cos(x)+4=2(\cos(x)+4)\left(\cos(x)+\frac12\right)$$

Ainsi

$$\begin{aligned}
0=2\cos^2(x)+9\cos(x)+4&\iff\cos x=-\frac12=\cos\left(\frac{2\pi}3\right)\\
&\iff x=\frac{2\pi}3+2k\pi,\ k\in\mathbb Z\quad\text{ou}\quad x=-\frac{2\pi}3+2k\pi,\ k\in\mathbb Z
\end{aligned}$$

### 3. $|x-2|+|x+3|\le1$.

**Solutions :** Nous avons

$$|x-2|+|x+3|\le1\iff|x+3|\le1-|x-2|\iff-1+|x-2|\le x+3\le1-|x-2|$$

Si $x\ge2$, alors

$$|x-2|+|x+3|\le1\iff-1+x-2\le x+3\le1-x+2\iff x-3\le x+3\le-x+3\iff2x-6\le2x\le0.$$

Ce qui est impossible car $x\ge2$, donc il n’y a pas de solution sur l’intervalle $[2,+\infty[$. Si $x<2$, alors

$$|x-2|+|x+3|\le1\iff-1-x+2\le x+3\le1+x-2\iff-x+1\le x+3\le x-1\iff-2x-2\le0\le-4.$$

Ce qui est impossible, il n’y a donc pas de solution sur l’intervalle $]-\infty,2[$.

## Exercice 2 (5 points)

### 1. Trouver sous la forme $\frac pq$, le rationnel $x$ dont les développement décimal périodiques est donné par : $2{,}71\overline{18}$.

**Solution :** Soit $r=$. L’idée est d’abord de faire apparaître la partie périodique juste après la virgule. Ici la période commence deux chiffres après la virgule, donc on multiplie par $100$ :

$$100r=271{,}\overline{18}.\tag{1}$$

Maintenant on va décaler tout vers la gauche de la longueur d’une période, donc ici on multiplie par $100$ pour décaler de 2 chiffre :

$$100\times100r=27118{,}\overline{18}\tag{2}$$

Les parties après la virgule des lignes (1) et (2) sont les mêmes, donc si on les soustrait en faisant (2)-(1) alors les parties décimales s’annulent :

$$100\times100r-100r=27118-271.$$

Donc $9900r=26847$ et

$$2{,}71\overline{18}=\frac{26847}{9900}.$$

### 2. On considère la fonction :

$$f(x)=\frac{E(x)}{2E(x)-1},$$

**où $E(x)$ désigne la partie entière de $x$.**

**(a) Justifier que $f$ est définie sur $\mathbb R$ tout entier.**

**Solution :** Nous avons

$$2E(x)-1=0\iff E(x)=\frac12.$$

Ce qui est impossible car $E(x)\in\mathbb Z$. Donc $f$ est définie sur $\mathbb R$ tout entier.

**(b) Déterminer, s’il en existe, tous les antécédents de $1$. Autrement dit, déterminer la solution de l’équation $f(x)=1$.**

**Solution :** Nous avons

$$f(x)=1\iff\frac{E(x)}{2E(x)-1}=1\iff E(x)=2E(x)-1\iff E(x)=1$$

Donc $x\in[1,2[$.

**(c) Déterminer, s’il en existe, tous les antécédents de $-3$. Autrement dit, déterminer la solution de l’équation $f(x)=-3$.**

**Solution :** Nous avons

$$f(x)=-3\iff\frac{E(x)}{2E(x)-1}=-3\iff E(x)=-6E(x)+3\iff E(x)=\frac37.$$

Or $E(x)\in\mathbb Z$, donc il n’y a pas d’antécédent pour $-3$.

## Exercice 3 (4 points)

**Choisir deux des trois questions suivants. Calculer les sommes et les produits suivants :**

### 1. $\displaystyle\sum_{k=1}^{n}3^{2k}$

**Solution :** Nous avons

$$\sum_{k=1}^{n}3^{2k}=\sum_{k=1}^{n}9^k=\sum_{k=0}^{n}9^k-9^0=\frac{9^{n+1}-1}{9-1}-1=\frac{9(9^n-1)}8$$

### 2. $\displaystyle\sum_{k=0}^{n-1}\frac{(-1)^k}{3^k}\binom nk$

**Solution :** Nous avons

$$\begin{aligned}
\sum_{k=0}^{n-1}\frac{(-1)^k}{3^k}\binom nk&=\sum_{k=0}^{n-1}\binom nk\left(-\frac13\right)^k\\
&=\sum_{k=0}^{n-1}\binom nk1^{n-k}\left(-\frac13\right)^k\\
&=\sum_{k=0}^{n}\binom nk1^{n-k}\left(-\frac13\right)^k-\left(-\frac13\right)^n\\
&=\left(1-\frac13\right)^n-\left(-\frac13\right)^n=\left(\frac23\right)^n-\left(-\frac13\right)^n.
\end{aligned}$$

### 3. $\displaystyle\prod_{k=0}^{n}(2k+1)$

**Solution :** Nous avons

$$\begin{aligned}
\prod_{k=0}^{n}(2k+1)&=\left(\prod_{k=1}^{2n+1}k\right)\cdot\left(\prod_{k=1}^{n}2k\right)^{-1}\\
&=\left(\prod_{k=1}^{2n+1}k\right)\cdot\left(\prod_{k=1}^{n}k\right)^{-1}\cdot\left(\prod_{k=1}^{n}2\right)^{-1}\\
&=(2n+1)!\cdot\frac1{n!}\cdot\frac1{2^n}\\
&=\frac{(2n+1)!}{2^nn!}
\end{aligned}$$

## Exercice 4 (7 points)

**On considère les ensembles $A$ et $B$ suivants**

$$A=,\left\{x\in\mathbb R\setminus\{1\}:\frac2{x-1}\le2x-5<11\right\}\quad;\quad B=\left\{\frac{2^n}{2^n-1}:\ n\in\mathbb N^*\right\}.$$

### 1. Les ensembles $A$ et $B$ sont-ils majorés, minorés ? Justifier votre réponse.

**Solution :** Commençons par étudier l’ensemble $A$. Nous avons

$$\begin{aligned}
x\in A\iff\frac2{x-1}\le2x-5<11&\iff0\le\frac{(2x-5)(x-1)-2}{x-1}\quad\text{et}\quad x<8\\
&\iff0\le\frac{2x^2-7x+3}{x-1}\quad\text{et}\quad x<8\\
&\iff0\le\frac{(2x-1)(x-3)}{x-1}\quad\text{et}\quad x<8
\end{aligned}$$

En faisant un tableau de signe, nous pouvons conclure que

$$x\in A\iff x\in\left(\left[\frac12,1\right[\cup[3,+\infty[\right)\cap\,]-\infty,8[.$$

Ainsi

$$A=\left[\frac12,1\right[\cup[3,8[.$$

Par conséquent, $A$ est majorée par tout réel supérieur ou égal à $8$, et $A$ est minorée par tout réel inférieur ou égal à $\frac12$.

**Solution :** Pour $B$, nous avons

$$\frac{2^n}{2^n-1}=\frac{2^n-1+1}{2^n-1}=1+\frac1{2^n-1}>1.$$

De plus

$$\frac1{2^n-1}\le1\implies1+\frac1{2^n-1}\le2.$$

Ainsi, $B$ est minorée par tout réel inférieur ou égal à $1$ et majorée par par tout réel supérieur ou égal à $2$.

### 2. Pour chaque ensemble $A$ et $B$ déterminer, s’il existe, les bornes supérieure et inférieure ainsi que le plus grand et le plus petit élément. Justifier votre réponse.

**Solutions :** Commençons par étudier l’ensemble $A$. D’après la question précédente, nous avons

$$A=\left[\frac12,1\right[\cup[3,8[.$$

Donc

$$\sup A=8\quad\text{et}\quad\min A=\inf A=\frac12.$$

Étudions maintenant l’ensemble $B$. D’après la question précédente, nous avons

$$\forall n\in\mathbb N^*,\ 1<\frac{2^n}{2^n-1}\le2.$$

Or

$$2=\frac{2^1}{2^1-1}\implies2\in B.$$

Ainsi, $2$ est un majorant de $B$ qui appartient à $B$. Ce qui nous permet de conclure

$$\max(B)=\sup(B)=2.$$

Finalement, pour tout $n\in\mathbb N^*$ on a

$$\frac{2^n}{2^n-1}\ge\inf(B).$$

Donc par passage à la limite, on obtient

$$1=\lim_{n\to+\infty}\frac{2^n}{2^n-1}\ge\lim_{n\to+\infty}\inf(B)=\inf(B).$$

Or, on sait que $1\le\inf(B)$. Par conséquent

$$\inf(B)=1.$$

Notons que $1\notin B$, donc $B$ ne possede pas de minimum.
