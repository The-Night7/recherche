---
source: "PREING2-S1/Series-DS/DS3-2022-2023-Correction_Series-DS_P2S1__RayaneM.pdf"
pages: 5
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des cinq pages ; limites, sommes géométriques et indices vérifiés ; erreurs manuscrites signalées
---

# Séries — DS 3, 2022–2023 — corrigé manuscrit

> Le document contient cinq pages de calculs manuscrits, sans les énoncés complets. Les numérotations et résultats présents sont conservés. Les erreurs de sommation et les conditions manquantes sont signalées séparément.

## Page 1 — Exercice 1 : rayons de convergence

### 1 a. Critère du quotient

Le calcul porte sur les coefficients dont le quotient s’écrit

$$
\left|\frac{a_{n+1}}{a_n}\right|
=\frac{(n+1)!}{3^{3(n+1)}\sqrt[3]{(3n+3)!}}
\frac{3^{3n}\sqrt[3]{(3n)!}}{n!}
=\frac{n+1}{3^3\sqrt[3]{(3n+1)(3n+2)(3n+3)}}.
$$

En factorisant $3n$ dans chaque facteur,

$$
\left|\frac{a_{n+1}}{a_n}\right|
=\frac1{3^4}
\frac{1+1/n}{\sqrt[3]{(1+1/(3n))(1+2/(3n))(1+1/n)}}
\longrightarrow\frac1{81}.
$$

Donc $\boxed{R=81}$.

### 1 b. Critère de la racine

$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}
=\lim_{n\to\infty}\exp\left[n\ln\left(1-\frac1{2n}\right)\right]
=\lim_{n\to\infty}\exp\left[-\frac12
\frac{\ln(1-1/(2n))}{-1/(2n)}\right]
=e^{-1/2},
$$

car $\ln(1+u)/u\to1$ lorsque $u\to0$. Donc $\boxed{R=\sqrt e}$.

### 1 c

$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}
=\lim_{n\to\infty}n\ln\left(1+\frac1n\right)
=\lim_{n\to\infty}\frac{\ln(1+1/n)}{1/n}=1.
$$

Donc $\boxed{R=1}$.

### 1 d

$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}
=\lim_{n\to\infty}
\exp\left[\frac{(-1)^n\ln\sqrt n}{n}\right]=1.
$$

Donc $\boxed{R=1}$.

### 2. Comparaison

Si $|a_n|\leq|b_n|$, alors

$$\sqrt[n]{|a_n|}\leq\sqrt[n]{|b_n|}.$$

Le manuscrit passe aux limites $\ell\leq\ell'$, puis inverse : $1/\ell'\leq1/\ell$. Ainsi les rayons vérifient $R'\leq R$.

> La preuve écrite suppose l’existence des limites des racines. En général, le même résultat s’établit avec les limites supérieures de Cauchy-Hadamard, avec les conventions usuelles pour $0$ et $+\infty$.

## Page 2 — Exercice 2 : suite de fonctions

Les calculs utilisent

$$f_n(x)=n^a x^n(1-x),\qquad x\in[0,1].$$

### 1. Convergence simple

Pour $x=0$, $f_n(x)=0$. Pour $0<x<1$,

$$f_n(x)=n^a e^{n\ln x}(1-x)\longrightarrow0,$$

par croissance comparée : l’exponentielle décroissante l’emporte sur la puissance de $n$. À $x=1$, la fonction vaut également zéro. Donc $f_n$ converge simplement vers $f=0$ sur $[0,1]$.

### 2. Norme uniforme

Puisque $f_n\geq0$,

$$|f_n(x)-f(x)|=f_n(x).$$

La dérivée vaut

$$
f_n'(x)=n^{a+1}x^{n-1}(1-x)-n^ax^n
=n^ax^{n-1}[n(1-x)-x]
=n^ax^{n-1}(n+1)\left(\frac n{n+1}-x\right).
$$

Le tableau de variations donne une croissance jusqu’à $n/(n+1)$, puis une décroissance jusqu’à $1$. Les valeurs aux extrémités sont nulles. Donc

$$
\|f_n\|_\infty=f_n\left(\frac n{n+1}\right)
=\frac{n^a}{n+1}\left(\frac n{n+1}\right)^n.
$$

### 3. Limite auxiliaire

$$
\left(\frac n{n+1}\right)^n
=\exp\left[n\ln\left(1-\frac1{n+1}\right)\right]
\longrightarrow e^{-1}.
$$

On utilise $n/(n+1)\to1$ et $\ln(1+u)/u\to1$.

### 4. Convergence uniforme

$$
f_n\longrightarrow0\text{ uniformément sur }[0,1]
\Longleftrightarrow\|f_n\|_\infty\longrightarrow0
\Longleftrightarrow\frac{n^a}{n+1}\longrightarrow0.
$$

## Page 3 — Fin de l’exercice 2 et début de l’exercice 3

$$\frac{n^a}{n+1}=\frac{n^{a-1}}{1+1/n}\longrightarrow0
\Longleftrightarrow a-1<0.$$

Le manuscrit rappelle dans cet exercice $a\in\mathbb R_+^*$, d’où $\boxed{0<a<1}$.

### Exercice 3 — Série de fonctions $\sum_{n\geq1}f_n$

#### 1. Convergence simple

Pour $x\in[0,1]$ fixé,

$$\sum_{n\geq1}f_n(x)=(1-x)\sum_{n\geq1}n^ax^n.$$

Pour $0<x<1$,

$$n^2f_n(x)=(1-x)\frac{n^{a+2}}{e^{n\ln(1/x)}}\longrightarrow0.$$

Par comparaison à $1/n^2$, la série converge. Aux deux extrémités, tous les termes sont nuls. Ainsi la série converge simplement sur $[0,1]$.

#### 2. Convergence normale

D’après l’exercice 2,

$$\sum_{n\geq1}\|f_n\|_\infty
=\sum_{n\geq1}\frac{n^a}{n+1}\left(\frac n{n+1}\right)^n,$$

et

$$\|f_n\|_\infty\sim e^{-1}n^{a-1}=\frac{e^{-1}}{n^{1-a}}.$$

- Si $a\geq0$, $1-a\leq1$ : cette série de Riemann diverge, donc il n’y a pas convergence normale.
- Si $a<0$, $1-a>1$ : elle converge, donc la série converge normalement sur $[0,1]$.

> La première ligne de cet exercice mentionne $a\in\mathbb R_+^*$, mais les questions suivantes traitent aussi $a=0$ et $a<0$. La discussion ci-dessus restitue les cas effectivement étudiés dans le manuscrit.

#### 3 a. Cas $a=0$

Alors $f_n(x)=x^n(1-x)$. Le calcul de la somme se poursuit page suivante.

## Page 4 — Somme pour $a=0$ et restes pour $a>0$

### 3 a. Calcul tel qu’écrit dans le manuscrit

$$
S=\lim_{n\to\infty}\sum_{k=1}^n x^k(1-x)
=\lim_{n\to\infty}(1-x)\frac{1-x^n}{1-x}
=\lim_{n\to\infty}(1-x^n).
$$

Le manuscrit en déduit $S(x)=1$ sur $[0,1[$ et $S(1)=0$.

> **Erreur de somme géométrique :** la somme commence à $k=1$ ; le facteur $x$ manque. Pour $0\leq x<1$, $\sum_{k=1}^n x^k=x(1-x^n)/(1-x)$, donc la somme correcte est $S(x)=x$ sur $[0,1[$ et $S(1)=0$.

### 3 b. Absence de convergence uniforme

Chaque $f_n$ est continue en $1$, alors que la somme ne l’est pas. La série ne converge donc pas uniformément sur $[0,1]$. Cette conclusion reste valable avec la somme corrigée.

### 4 a. Minoration pour $a>0$

Pour $n\geq1$ et $x\in[0,1]$,

$$n^a\geq1\quad\Longrightarrow\quad
n^ax^n(1-x)\geq x^n(1-x),$$

car $x^n(1-x)\geq0$.

### 4 b. Minoration du reste

Les trois étiquettes ajoutées sur la photographie indiquent $x^{n+k}$. On lit

$$f_{n+k}(x)=(n+k)^a x^{n+k}(1-x)\geq x^{n+k}(1-x),$$

puis

$$R_n(x)\geq\sum_{k=1}^{\infty}x^{n+k}(1-x).$$

## Page 5 — Restes et convergence uniforme

Pour une somme partielle de $p$ termes, le manuscrit écrit

$$\sum_{k=1}^p f_{n+k}(x)
\geq\sum_{k=1}^p x^{n+k}(1-x)
\geq x^n(1-x)\frac{1-x^p}{1-x}
=x^n(1-x^p).$$

Il choisit $x_n=1-1/n$, fait tendre $p$ vers $+\infty$ et annonce

$$R_n(x_n)\geq\left(1-\frac1n\right)^n,$$

puis une limite minorée par $e^{-1}$.

> **Correction d’indice :** avec $k$ commençant à $1$, $\sum_{k=1}^p x^{n+k}(1-x)=x^{n+1}(1-x^p)$. La minoration justifiée est donc $R_n(x_n)\geq(1-1/n)^{n+1}$ pour $n\geq2$. Son membre de droite tend aussi vers $e^{-1}$, donc $\liminf\|R_n\|_\infty\geq e^{-1}>0$. Cela suffit à exclure la convergence uniforme pour $a>0$, sans supposer l’existence de la limite des restes. La page s’arrête après la minoration annoncée.
