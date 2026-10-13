# Algèbre 1 — Correction du DS3 de janvier 2020

> Source : `PREING1-S1/Algebre1-DS/DS3-2019-2020-Correction_Algebre1-DS_P1S1_Inconnu.pdf`, 12 pages, dont la dernière est blanche. Corrigé manuscrit sans auteur identifié.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale des douze pages ; calculs, divisions euclidiennes et factorisations restitués en LaTeX. Les divisions posées sont présentées par leurs soustractions successives. Les erreurs de signe ou d’exposant relevées sont signalées séparément. On note $j=e^{2i\pi/3}$ et $\overline j=j^2$.

## Exercice 1 — Linéarisation (page 1)

### 1. Puissance cinquième du cosinus

$$
\begin{aligned}
\cos^5x
&=\frac1{2^5}(e^{ix}+e^{-ix})^5\\
&=\frac1{2^5}\left(e^{5ix}+5e^{3ix}+10e^{ix}+10e^{-ix}+5e^{-3ix}+e^{-5ix}\right)\\
&=\frac1{2^5}\left(e^{5ix}+e^{-5ix}+5(e^{3ix}+e^{-3ix})+10(e^{ix}+e^{-ix})\right)\\
&=\boxed{\frac1{2^4}\left(\cos5x+5\cos3x+10\cos x\right)}.
\end{aligned}
$$

### 2. Produit $\sin^2x\cos^3x$

$$
\begin{aligned}
\sin^2x\cos^3x
&=\frac1{(2i)^2}(e^{ix}-e^{-ix})^2\frac1{2^3}(e^{ix}+e^{-ix})^3\\
&=-\frac1{2^5}\left[(e^{ix}-e^{-ix})(e^{ix}+e^{-ix})\right]^2(e^{ix}+e^{-ix})\\
&=-\frac1{2^5}(e^{2ix}-e^{-2ix})^2(e^{ix}+e^{-ix})\\
&=-\frac1{2^5}(e^{4ix}+e^{-4ix}-2)(e^{ix}+e^{-ix})\\
&=-\frac1{2^5}\left(e^{5ix}+e^{-5ix}+e^{3ix}+e^{-3ix}-2(e^{ix}+e^{-ix})\right)\\
&=\boxed{-\frac1{16}(\cos5x+\cos3x-2\cos x)}.
\end{aligned}
$$

## Exercice 2 — Factorisations de polynômes (pages 1–3)

### 1. $P(X)=X^4+X^2+1$

$$P(X)=X^4+2X^2+1-X^2=(X^2+1)^2-X^2=(X^2+X+1)(X^2-X+1).$$

C’est la factorisation en facteurs irréductibles dans $\mathbb R[X]$.

Dans $\mathbb C[X]$, les racines de $X^2+X+1$ sont $j$ et $\overline j=j^2$ ; celles de $X^2-X+1$ sont $(1+i\sqrt3)/2$ et $(1-i\sqrt3)/2$. Donc :

$$P(X)=(X-j)(X-j^2)\left(X-\left(\frac12+i\frac{\sqrt3}2\right)\right)\left(X-\left(\frac12-i\frac{\sqrt3}2\right)\right).$$

**Note sur la source.** La première ligne manuscrite porte $X^4-2X^2+1-X^2$, incompatible avec la ligne suivante ; le signe de $2X^2$ est rétabli ci-dessus.

### 2. $P(X)=X^{2m}+1$, $m\in\mathbb N^*$

Posons $z=re^{i\theta}$. Alors :

$$z^{2m}+1=0\Longleftrightarrow r^{2m}e^{2im\theta}=e^{i\pi}\Longleftrightarrow\begin{cases}r=1,\\\theta=\dfrac\pi{2m}+\dfrac{2k\pi}{2m},\quad k\in\mathbb Z.\end{cases}$$

Les solutions distinctes sont :

$$w_k=e^{i(\pi/(2m)+2k\pi/(2m))},\qquad k\in\{0,\ldots,2m-1\}.$$

Dans $\mathbb C[X]$ :

$$P(X)=\prod_{k=0}^{2m-1}(X-w_k).$$

Dans $\mathbb R[X]$, remarquons que $w_{2m-1-k}=\overline{w_k}$ pour $0\leq k\leq m-1$. Ainsi :

$$
\begin{aligned}
P(X)
&=\prod_{k=0}^{m-1}(X-w_k)(X-\overline{w_k})\\
&=\prod_{k=0}^{m-1}\left(X^2-2\operatorname{Re}(w_k)X+|w_k|^2\right)\\
&=\boxed{\prod_{k=0}^{m-1}\left(X^2-2\cos\left(\frac\pi{2m}+\frac{2k\pi}{2m}\right)X+1\right)}.
\end{aligned}
$$

### 3. $P(X)=X^4-5X^3+7X^2-5X+6$

$P(i)=1+5i-7-5i+6=0$. De plus :

$$P'(X)=4X^3-15X^2+14X-5,\qquad P'(i)=-4i+15+14i-5=10+10i\neq0.$$

Ainsi $i$ est racine simple. Puisque $P\in\mathbb R[X]$, $-i=\overline i$ est aussi racine simple ; donc $X^2+1$ divise $P$.

Division euclidienne par $X^2+1$ :

$$
\begin{aligned}
P-X^2(X^2+1)&=-5X^3+6X^2-5X+6,\\
(-5X^3+6X^2-5X+6)-(-5X)(X^2+1)&=6X^2+6,\\
(6X^2+6)-6(X^2+1)&=0.
\end{aligned}
$$

D’où $P=(X^2-5X+6)(X^2+1)$. Les racines de $X^2-5X+6$ sont 2 et 3.

- Dans $\mathbb C[X]$ : $P(X)=(X-i)(X+i)(X-2)(X-3)$.
- Dans $\mathbb R[X]$ : $P(X)=(X^2+1)(X-2)(X-3)$.

**Note sur la source.** Le calcul manuscrit de $P'(i)$ écrit $-15$ au lieu de $+15$ ; le résultat « non nul » reste valable. Les lignes de division ci-dessus explicitent les soustractions dont certains signes sont peu soignés dans la division posée.

## Exercice 3 — Restes et divisibilité (pages 3–5)

### 1. Reste de $A(X)=X^{2020}-X^3+X$ modulo $B(X)=X^2+1$

Puisque $\deg B=2$, le reste a degré au plus 1 : $R(X)=aX+b$ avec $a,b\in\mathbb R$. Écrivons $A=BQ+R$.

Les racines de $B$ sont $i$ et $-i$, donc :

$$
\begin{cases}
A(i)=B(i)Q(i)+R(i)=R(i),\\
A(-i)=B(-i)Q(-i)+R(-i)=R(-i).
\end{cases}
$$

Ainsi :

$$
\begin{cases}
ai+b=i^{2020}-i^3+i=1+2i,\\
-ai+b=(-i)^{2020}-(-i)^3-i=1-2i.
\end{cases}
$$

On obtient $a=2$, $b=1$, donc $R(X)=2X+1$.

### 2. Divisibilité de $P(X)=X^{2m}+X^m+1$ par $X^2+X+1$

a. Sens direct :

$$X^2+X+1\mid P\ \Longrightarrow\ P(j)=j^{2m}+j^m+1=0\ \Longrightarrow\ j^m\text{ est racine de }X^2+X+1.$$

Réciproquement, si $j^m$ est racine de $X^2+X+1$, alors $j^{2m}+j^m+1=0$. Donc $j$ est racine de $P$. Comme $P$ est réel, $\overline j$ est aussi racine de $P$, d’où $(X-j)(X-\overline j)=X^2+X+1\mid P$.

b. D’après a :

$$
\begin{aligned}
X^2+X+1\mid P
&\Longleftrightarrow j^m=j\text{ ou }j^m=j^2\\
&\Longleftrightarrow m=3k+1\text{ ou }m=3k+2,\quad k\in\mathbb Z\\
&\Longleftrightarrow\boxed{m\equiv1\pmod3\text{ ou }m\equiv2\pmod3}.
\end{aligned}
$$

### 3. $P(X)=X^4+X^3+aX^2+bX+2$

a. Division par $X^2+2$ :

$$
\begin{aligned}
P-X^2(X^2+2)&=X^3+(a-2)X^2+bX+2,\\
\bigl(X^3+(a-2)X^2+bX+2\bigr)-X(X^2+2)&=(a-2)X^2+(b-2)X+2,\\
\bigl((a-2)X^2+(b-2)X+2\bigr)-(a-2)(X^2+2)&=(b-2)X+6-2a.
\end{aligned}
$$

Donc $Q=X^2+X+a-2$ et $R=(b-2)X+6-2a$.

b. $X^2+2\mid P\Longleftrightarrow R=0\Longleftrightarrow b=2\text{ et }a=3$.

## Exercice 4 — Racines d’un polynôme construit avec $i$ (pages 5–7)

### 1. Résolution de $(z+i)^m=(z-i)^m$, $m\in\mathbb N^*$

Ni $i$ ni $-i$ ne sont solutions. On peut donc écrire :

$$(z+i)^m=(z-i)^m\Longleftrightarrow\left(\frac{z+i}{z-i}\right)^m=1.$$

Posons $Z=(z+i)/(z-i)$. Alors $z=i(Z+1)/(Z-1)$ avec $Z\neq1$. Les solutions de $Z^m=1$ sont :

$$Z_k=e^{2ik\pi/m},\qquad k\in\{0,\ldots,m-1\}.$$

L’équation $(z+i)/(z-i)=1=Z_0$ n’a pas de solution : elle donnerait $z-i=z+i$, donc $-i=i$.

Les solutions de l’équation initiale sont donc :

$$\boxed{z_k=i\frac{Z_k+1}{Z_k-1}=i\frac{e^{2ik\pi/m}+1}{e^{2ik\pi/m}-1},\qquad k\in\{1,\ldots,m-1\}.}$$

### 2. Polynôme $P(X)=(X+i)^m-(X-i)^m$

a. Développement par le binôme :

$$P(X)=\sum_{k=0}^m\binom mk\bigl(i^{m-k}-(-i)^{m-k}\bigr)X^k.$$

Posons $a_k=\binom mk(i^{m-k}-(-i)^{m-k})$. Alors :

$$a_m=\binom mm(i^0-(-i)^0)=0,\qquad a_{m-1}=\binom m{m-1}(i-(-i))=2im\neq0.$$

Donc $\deg P=m-1$.

b. Ses racines sont les solutions trouvées en 1. Par conséquent :

$$\boxed{P(X)=2im\prod_{k=1}^{m-1}(X-z_k),\qquad z_k=i\frac{e^{2ik\pi/m}+1}{e^{2ik\pi/m}-1}.}$$

## Exercice 5 — Relations entre coefficients et racines (pages 7–8)

### 1–2. Factorisation et identification

Pour un polynôme de degré 3, de coefficient dominant $a\neq0$ et de racines $z_1,z_2,z_3$ :

$$P(z)=a(z-z_1)(z-z_2)(z-z_3)=az^3+bz^2+cz+d.$$

En développant :

$$P(z)=a\left[z^3-(z_1+z_2+z_3)z^2+(z_1z_2+z_1z_3+z_2z_3)z-z_1z_2z_3\right].$$

Par identification :

$$\boxed{z_1+z_2+z_3=-\frac ba,\qquad z_1z_2+z_1z_3+z_2z_3=\frac ca,\qquad z_1z_2z_3=-\frac da.}$$

### 3. Sommes des carrés et des cubes

a. On a :

$$(z_1+z_2+z_3)^2=z_1^2+z_2^2+z_3^2+2(z_1z_2+z_1z_3+z_2z_3).$$

Donc $b^2/a^2=z_1^2+z_2^2+z_3^2+2c/a$, soit :

$$\boxed{z_1^2+z_2^2+z_3^2=\frac{b^2-2ac}{a^2}.}$$

b. $P(z_1)+P(z_2)+P(z_3)=0$, donc :

$$a(z_1^3+z_2^3+z_3^3)+b(z_1^2+z_2^2+z_3^2)+c(z_1+z_2+z_3)+3d=0.$$

Ainsi :

$$
\begin{aligned}
z_1^3+z_2^3+z_3^3
&=\frac1a\left[-b\frac{b^2-2ac}{a^2}+c\frac ba-3d\right]\\
&=\boxed{\frac{-b^3+3abc-3a^2d}{a^3}}.
\end{aligned}
$$

**Note sur la source.** Une ligne intermédiaire porte $z_3^2$ au lieu de $z_3^3$ ; la somme des cubes est bien celle utilisée dans le calcul.

### 3, à nouveau dans le manuscrit — Racines non nulles

a. $0$ est racine de $P\Longleftrightarrow P(0)=0\Longleftrightarrow d=0$.

b. Si $0$ n’est pas racine, alors $d\neq0$ et :

$$\frac1{z_1}+\frac1{z_2}+\frac1{z_3}=\frac{z_2z_3+z_1z_3+z_1z_2}{z_1z_2z_3}=\frac{c/a}{-d/a}=\boxed{-\frac cd}.$$

## Exercice 6 — Éléments simples (pages 9–11)

### 1. Formes des décompositions

La fraction concernée est :

$$F(X)=\frac{X^{11}}{(X-1)^3(X^2+1)^2(X^2+X+1)^2}.$$

a. Dans $\mathbb R(X)$ :

$$
\begin{aligned}
F(X)=E
&+\frac{a_1}{X-1}+\frac{a_2}{(X-1)^2}+\frac{a_3}{(X-1)^3}\\
&+\frac{\alpha_1X+\beta_1}{X^2+1}+\frac{\alpha_2X+\beta_2}{(X^2+1)^2}\\
&+\frac{\lambda_1X+\gamma_1}{X^2+X+1}+\frac{\lambda_2X+\gamma_2}{(X^2+X+1)^2}.
\end{aligned}
$$

b. Dans $\mathbb C(X)$ :

$$
\begin{aligned}
F(X)=E
&+\frac{a_1}{X-1}+\frac{a_2}{(X-1)^2}+\frac{a_3}{(X-1)^3}\\
&+\frac{b_1}{X-i}+\frac{b_2}{(X-i)^2}+\frac{\overline b_1}{X+i}+\frac{\overline b_2}{(X+i)^2}\\
&+\frac{c_1}{X-j}+\frac{c_2}{(X-j)^2}+\frac{\overline c_1}{X-\overline j}+\frac{\overline c_2}{(X-\overline j)^2}.
\end{aligned}
$$

$E$ est le quotient de la division euclidienne de $X^{11}$ par $(X-1)^3(X^2+1)^2(X^2+X+1)^2$. Les coefficients $a_1,a_2,a_3,\alpha_1,\alpha_2,\beta_1,\beta_2,\lambda_1,\lambda_2,\gamma_1,\gamma_2$ sont réels ; $b_1,b_2,c_1,c_2$ sont complexes. Le manuscrit donne les formes de décomposition, sans calculer ces coefficients.

### 2. Décomposition de $F(X)=(X^4+1)/(X(X-1)^2)$

La fraction est irréductible. Son degré est $4-3=1\geq0$, donc sa partie entière $E$ n’est pas nulle. Elle a un pôle simple en 0 et un pôle double en 1.

$$F(X)=E+\frac aX+\frac b{X-1}+\frac c{(X-1)^2},\qquad a,b,c\in\mathbb R.$$

$E\in\mathbb R[X]$ est le quotient de $X^4+1$ par $X^3-2X^2+X$. Division :

$$
\begin{aligned}
(X^4+1)-X(X^3-2X^2+X)&=2X^3-X^2+1,\\
(2X^3-X^2+1)-2(X^3-2X^2+X)&=3X^2-2X+1.
\end{aligned}
$$

Donc $E=X+2$. Par évaluation après simplification des pôles :

$$a=\left.XF(X)\right|_{X=0}=1,\qquad c=\left.(X-1)^2F(X)\right|_{X=1}=2.$$

Enfin :

$$F(-1)=\frac2{(-1)(-2)^2}=-\frac12,$$

et, dans la décomposition :

$$F(-1)=-1+2+\frac a{-1}+\frac b{-2}+\frac c4=1-1-\frac b2+\frac24.$$

Donc $b=2$. Finalement :

$$\boxed{F(X)=X+2+\frac1X+\frac2{X-1}+\frac2{(X-1)^2}.}$$

## Page 12

Page blanche, sans contenu pédagogique.
