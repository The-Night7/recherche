---
source: ING 1/S2 DATA/Analyse numérique/TD/Correction/Correction_exo_supplementaires.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Analyse numérique — Correction des exercices supplémentaires

> Le fichier contient deux pages manuscrites de correction, sans les énoncés. Les numéros et sous-questions visibles sont conservés.

## Exercice I — Polynômes interpolateurs

**i)**

$$P_f(x)=\left(\frac1{2e}-1+\frac e2\right)x^2+
\left(\frac e2-\frac1{2e}\right)x+1.$$

**ii)** $P_f(x)=-4x^2+4x$.

**iii)** $P_f(x)=x$.

## Exercice II — Différences divisées et base de Lagrange

### 1. Différences divisées

$$f[x_0]=4,\quad f[x_1]=2,\quad f[x_2]=\frac12,\quad f[x_3]=\frac14.$$

$$f[x_0,x_1]=-8,\qquad f[x_1,x_2]=-1,\qquad f[x_2,x_3]=-\frac18.$$

$$f[x_0,x_1,x_2]=4,\qquad f[x_1,x_2,x_3]=\frac14,\qquad
f[x_0,x_1,x_2,x_3]=-1.$$

### 2. Polynôme interpolateur

$$P_f(x)=-x^3+\frac{27}{4}x^2-\frac{101}{8}x+\frac{27}{4}.$$

### 2.a. Polynômes de Lagrange

$$\begin{aligned}
\ell_0(x)&=-\frac{64}{105}\left(x^3-\frac{13}{2}x^2+11x-4\right),\\
\ell_1(x)&=\frac{16}{21}\left(x^3-\frac{25}{4}x^2+\frac{19}{2}x-2\right),\\
\ell_2(x)&=-\frac4{21}\left(x^3-\frac{19}{4}x^2+\frac{25}{8}x-\frac12\right),\\
\ell_3(x)&=\frac4{105}\left(x^3-\frac{11}{4}x^2+\frac{13}{8}x-\frac14\right).
\end{aligned}$$

## Exercice III — Reste de division et interpolation

**1.** On a $P=QT_N+R$, avec $\deg R\leq\deg T_N-1$.

Ainsi, $P(x_i)=R(x_i)$ pour tout $i$, et $\deg R\leq N$. Par unicité, $R=P_N$.

**2.** Pour $N\in\mathbb N$,

$$T_N=x(x-1)\cdots(x-N).$$

- Si $N=0$, $P_0(f)=1$.
- Si $N=1$, $x^3+1=(x^2-x)(x+1)+x+1$, donc $P_1(f)=x+1$.
- Si $N=2$, $x^3+1=(x^3-3x^2+2x)\times1+3x^2-2x+1$, donc $P_2(f)=3x^2-2x+1$.
- Si $N\geq3$, le manuscrit écrit $P_3(f)=x^3+1$ ; le polynôme interpolateur est alors le polynôme $f$ lui-même, soit $P_N(f)=x^3+1$.

## Exercice IV — Interpolation d’Hermite

### 1. Existence

$$\varphi:\mathbb R_3[X]\longrightarrow\mathbb R^4,\qquad
P\longmapsto\bigl(P(0),P'(0),P(1),P'(1)\bigr).$$

$\ker\varphi=\{0\}$, donc $\varphi$ est un isomorphisme. D’où l’existence de $P_f$.

### 2. Erreur

**a)** Les points 0 et 1 sont chacun de multiplicité 2.

**b)** $F(0)=F(u)=F(1)$. Par le théorème de Rolle, il existe $0<a<u<b<1$ tels que $F'(a)=F'(b)=0$. On a aussi $F'(0)=F'(1)=0$.

Par applications successives du théorème de Rolle, $F''$ possède trois racines distinctes, puis $F^{(3)}$ en possède deux. Enfin, il existe $\xi\in]0,1[$ tel que $F^{(4)}(\xi)=0$.

**c)**

$$F^{(4)}(\xi)=f^{(4)}(\xi)\Pi(u)-24R(u).$$

**d)**

$$|x(1-x)|\leq\frac14\quad\Longrightarrow\quad|\Pi(x)|\leq\frac1{16}.$$

**e)** D’après c) et d),

$$\forall u\in]0,1[,\qquad |R(u)|\leq\frac1{384}\|f^{(4)}\|_\infty.$$

> Les définitions de $F$, $R$ et $\Pi$ sont dans l’énoncé non inclus ; ces notations sont conservées sans reconstituer cet énoncé.

## Exercice V — Polynômes de Tchebychev

**1.**

$$\begin{aligned}
\cos(m\theta)&=\operatorname{Re}(e^{im\theta})
=\operatorname{Re}\bigl((\cos\theta+i\sin\theta)^m\bigr)\\
&=\sum_{0\leq2p\leq m}\binom m{2p}(-1)^p
(1-\cos^2\theta)^p\cos^{m-2p}\theta.
\end{aligned}$$

Le polynôme

$$T_m(x)=\sum_{0\leq2p\leq m}\binom m{2p}(-1)^p(1-x^2)^p x^{m-2p}$$

convient. Si $\widetilde T_m(\cos\theta)=\cos(m\theta)$, alors $\widetilde T_m=T_m$ sur $[-1,1]$, donc les deux polynômes sont égaux.

**2.a)** Le manuscrit s’arrête à cette mention ; aucun calcul n’est fourni après elle.
