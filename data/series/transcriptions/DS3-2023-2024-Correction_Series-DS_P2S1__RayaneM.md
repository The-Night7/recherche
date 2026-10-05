---
source: "PREING2-S1/Series-DS/DS3-2023-2024-Correction_Series-DS_P2S1__RayaneM.pdf"
pages: 5
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des cinq pages ; séries et primitives vérifiées ; énoncés absents et justification manquante des interversions signalés
---

# Séries — DS 3, 2023–2024 — corrigé manuscrit

> Les cinq pages photographiées contiennent les réponses manuscrites, sans les énoncés complets. Une zone blanche masque la marge droite de la page 2 ; aucun texte manquant n’est inventé.

## Page 1 — Exercice 1

### 1 a. Théorème spécial des séries alternées

Si $(a_n)$ est positive, décroissante et tend vers zéro, la série de terme général $(-1)^na_n$ converge. Son reste satisfait

$$|R_n|\leq a_{n+1},$$

et les sommes partielles encadrent la somme :

$$S_{2n+1}\leq S\leq S_{2n}.$$

### 1 b. Application

$$
(-1)^n(\sqrt{n+1}-\sqrt n)
=(-1)^n\sqrt n\left(\sqrt{1+\frac1n}-1\right)
=(-1)^n\sqrt n\left(\frac1{2n}+O\left(\frac1{n^2}\right)\right)
=\frac{(-1)^n}{2\sqrt n}+O\left(\frac1{n^{3/2}}\right).
$$

La série $\sum(-1)^n/(2\sqrt n)$ converge par le critère des séries alternées. La série du reste converge absolument par comparaison à la série de Riemann d’exposant $3/2>1$. Donc

$$\sum(-1)^n(\sqrt{n+1}-\sqrt n)\text{ converge}.$$

> Le manuscrit écrit seulement $3/2>0$ dans la justification de la série de Riemann ; le critère requis est $3/2>1$.

### 2 a. Définition de la convergence uniforme

$$
f_n\longrightarrow f\text{ uniformément sur }I
\Longleftrightarrow
\forall\varepsilon>0,\ \exists n_0\in\mathbb N,\
\forall n\geq n_0,\ \forall x\in I,
\quad|f_n(x)-f(x)|\leq\varepsilon.
$$

### 2 b. Exemple

$$f_n(x)=\frac{x^n-1}{x^n+1},\qquad x\in\mathbb R_+.$$

- Si $x=1$, $f_n(x)=0$.
- Si $0\leq x<1$, $f_n(x)\to-1$.
- Si $x>1$, $f_n(x)=(1-x^{-n})/(1+x^{-n})\to1$.

La limite simple est donc

$$f(x)=\begin{cases}-1,&0\leq x<1,\\0,&x=1,\\1,&x>1.\end{cases}$$

Elle est discontinue en $1$, tandis que toutes les $f_n$ sont continues. La convergence n’est pas uniforme sur $\mathbb R_+$.

## Page 2 — Fin de l’exercice 1 et exercice 2

### 3 a. Convergence normale

$$\sum f_n\text{ converge normalement}
\Longleftrightarrow\sum\|f_n\|_\infty\text{ converge}.$$

### 3 b. Majoration

Le manuscrit donne $|f_n|\leq1/n^2$. Comme $\sum1/n^2$ converge, la série de fonctions converge normalement sur $\mathbb R$, donc absolument en chaque point, uniformément et simplement.

> La définition de la fonction $f_n$ de cette question n’est pas reproduite dans le corrigé. Elle ne doit pas être confondue avec celle de la question 2 b.

### Exercice 2 — Série entière

1. Pour $\sum_{n\geq1}x^n/[n(n+2)]$, on pose $a_n=1/[n(n+2)]$.

$$
\left|\frac{a_{n+1}}{a_n}\right|
=\frac{n(n+2)}{(n+1)(n+3)}
=\frac{1+2/n}{(1+1/n)(1+3/n)}\longrightarrow1.
$$

Le rayon de convergence vaut $\boxed{R=1}$.

2. À $x=1$,

$$\frac1{n(n+2)}\sim\frac1{n^2}.$$

La série converge par comparaison à une série de Riemann d’exposant $2>1$.

3. Par décomposition en éléments simples,

$$
\sum_{k=1}^n\frac1{k(k+2)}
=\frac12\sum_{k=1}^n\left(\frac1k-\frac1{k+2}\right)
=\frac12\left(1+\frac12-\frac1{n+1}-\frac1{n+2}\right)
=\frac34-\frac12\left(\frac1{n+1}+\frac1{n+2}\right).
$$

Donc $\boxed{\sum_{k=1}^{\infty}1/[k(k+2)]=3/4}$.

Le titre « Exercice 3 — 1) » apparaît au bas de la page.

## Page 3 — Exercice 3 : série de fonctions et intégration

Les calculs portent sur $f_n(x)=e^{-(n+1)x}\sin x$, pour $n\geq0$ et $x>0$.

### 1. Convergence simple

Pour $x>0$ fixé,

$$n^2e^{-(n+1)x}\sin x\longrightarrow0$$

par croissance comparée. La comparaison à $1/n^2$ donne la convergence simple sur $\mathbb R_+^*$.

### 2. Somme

$$
\sum_{k=0}^n f_k(x)
=\sin x\sum_{k=0}^n(e^{-x})^{k+1}
=\sin x\,e^{-x}\frac{1-e^{-(n+1)x}}{1-e^{-x}}
=\frac{\sin x\,(1-e^{-(n+1)x})}{e^x-1}.
$$

En passant à la limite,

$$\boxed{S(x)=\frac{\sin x}{e^x-1}}.$$

### 3. Sur un segment $[A,B]$, avec $0<A<B$

La fonction $S$ est continue comme quotient de deux fonctions continues, le dénominateur ne s’annulant pas. De plus,

$$|f_n(x)|\leq e^{-(n+1)x}|\sin x|\leq e^{-(n+1)A}.$$

La majorante forme une série convergente. Le manuscrit le justifie aussi par $n^2e^{-(n+1)A}\to0$. Il y a convergence normale, donc uniforme, sur $[A,B]$. Chaque $f_n$ étant continue, on peut intégrer terme à terme :

$$\int_A^B S(x)\,\mathrm dx
=\sum_{n=0}^{\infty}\int_A^B f_n(x)\,\mathrm dx.$$

## Page 4 — Recherche d’une primitive

### 4. Dérivée

On cherche

$$F_n(x)=(\alpha_n\cos x+\beta_n\sin x)e^{-(n+1)x}.$$

Sa dérivée est

$$
F_n'(x)=(-\alpha_n\sin x+\beta_n\cos x)e^{-(n+1)x}
-(n+1)(\alpha_n\cos x+\beta_n\sin x)e^{-(n+1)x}
$$

$$
=e^{-(n+1)x}\left[(\beta_n-(n+1)\alpha_n)\cos x
-(\alpha_n+(n+1)\beta_n)\sin x\right].
$$

### 5. Identification avec $f_n$

Pour tout $x>0$, $F_n'(x)=f_n(x)$ si et seulement si

$$\begin{cases}
\beta_n-(n+1)\alpha_n=0,\\
\alpha_n+(n+1)\beta_n=-1.
\end{cases}$$

En multipliant la seconde équation par $n+1$ et en utilisant la première,

$$\beta_n[1+(n+1)^2]=-(n+1).$$

Ainsi

$$\beta_n=-\frac{n+1}{1+(n+1)^2},$$

$$\alpha_n=-1-(n+1)\beta_n
=-1+\frac{(n+1)^2}{1+(n+1)^2}
=-\frac1{1+(n+1)^2}.$$

### 6. Intégration sur le segment

$$\int_A^B f_n(x)\,\mathrm dx
=\int_A^B F_n'(x)\,\mathrm dx
=[F_n(x)]_A^B=F_n(B)-F_n(A).$$

## Page 5 — Passage à l’intégrale impropre

### 7. Limites des primitives

$$F_n(x)=\left[-\frac{\cos x}{1+(n+1)^2}
-\frac{(n+1)\sin x}{1+(n+1)^2}\right]e^{-(n+1)x}.$$

Pour chaque $n$,

$$\lim_{x\to0^+}F_n(x)=-\frac1{1+(n+1)^2},\qquad
\lim_{x\to+\infty}F_n(x)=0.$$

La seconde limite résulte du produit d’une fonction bornée par une exponentielle décroissante. Le manuscrit invoque ensuite l’interversion somme-limite :

$$\lim_{A\to0^+}\sum_{n=0}^{\infty}F_n(A)
=\sum_{n=0}^{\infty}F_n(0),$$

$$\lim_{B\to+\infty}\sum_{n=0}^{\infty}F_n(B)
=\sum_{n=0}^{\infty}\lim_{B\to+\infty}F_n(B)=0.$$

> **Justification manquante dans la source :** la convergence uniforme de $\sum f_n$ sur chaque segment $[A,B]$ ne suffit pas seule à ces passages aux bornes. Pour les primitives, en posant $m=n+1$ et en utilisant $|\sin x|\leq x$ et $mx e^{-mx}\leq e^{-1}$ pour $x\geq0$, on obtient $|F_n(x)|\leq(1+e^{-1})/[1+(n+1)^2]$. Cette majorante sommable, indépendante de $x\geq0$, justifie les deux interversions.

### 8. Résultat

$$\int_A^B S(x)\,\mathrm dx
=\sum_{n=0}^{\infty}[F_n(B)-F_n(A)].$$

En passant à $A\to0^+$ et $B\to+\infty$,

$$
\boxed{\int_0^{\infty}\frac{\sin x}{e^x-1}\,\mathrm dx
=\sum_{n=0}^{\infty}\frac1{1+(n+1)^2}
=\sum_{n=1}^{\infty}\frac1{1+n^2}}.
$$
