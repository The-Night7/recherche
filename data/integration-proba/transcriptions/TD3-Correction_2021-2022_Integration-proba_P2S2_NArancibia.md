---
source: "PREING2-S2/Integration-proba/TD3-Correction_2021-2022_Integration-proba_P2S2_NArancibia.pdf"
pages: 54
transcription: manuelle
transcription_date: 2026-10-02
verification: lecture visuelle intégrale des 54 diapositives et vérification des domaines, formules et résultats
---

# TD Intégration et probabilités — Intégrales multiples — Corrigé

CY Tech — Deuxième semestre 2021–2022.

Les développements répartis sur plusieurs diapositives sont réunis par exercice. La source emploie deux fois le numéro « 00 » et alterne « 00 » et « 0 » pour le premier exercice ; ils sont distingués ci-dessous par leur domaine.

## Exercice 00 — Triangle unité (pages 2 à 4)

Soit

$$
D=\{(x,y)\in\mathbb R^2:x\geq0,\ y\geq0,\ x+y\leq1\}.
$$

Calculer $\iint_D f(x,y)\,dx\,dy$ pour $f(x,y)=x^2+y^2$ et pour $f(x,y)=xy(x+y)$.

**Solution.** On décrit d’abord le domaine :

$$
D=\{x\geq0,\ 0\leq y\leq1-x\}
=\{0\leq x\leq1,\ 0\leq y\leq1-x\}.
$$

Dans le premier cas,

$$
\begin{aligned}
\iint_D(x^2+y^2)\,dx\,dy
&=\int_0^1\int_0^{1-x}(x^2+y^2)\,dy\,dx\\
&=\int_0^1\left[x^2y+\frac{y^3}3\right]_0^{1-x}dx\\
&=\int_0^1\left(x^2(1-x)+\frac{(1-x)^3}3\right)dx\\
&=\int_0^1\left(-\frac43x^3+2x^2-x+\frac13\right)dx\\
&=\left[-\frac{x^4}3+\frac{2x^3}3-\frac{x^2}2+\frac x3\right]_0^1\\
&=-\frac13+\frac23-\frac12+\frac13=\frac16.
\end{aligned}
$$

Dans le second cas,

$$
\begin{aligned}
\iint_Dxy(x+y)\,dx\,dy
&=\int_0^1\int_0^{1-x}(x^2y+xy^2)\,dy\,dx\\
&=\int_0^1\left[\frac{x^2y^2}2+\frac{xy^3}3\right]_0^{1-x}dx\\
&=\int_0^1\left(\frac{x^2(1-x)^2}2+\frac{x(1-x)^3}3\right)dx
=\frac1{30}.
\end{aligned}
$$

La dernière intégration est laissée au lecteur dans la source : « à vous de faire les calculs ».

## Exercice 00 — Domaine délimité par $x+y<5$ (page 5)

Calculer

$$
\iint_D\frac{dx\,dy}{(x+y)^3},
\qquad D=\{(x,y)\in\mathbb R^2:1<x<3,\ y>2,\ x+y<5\}.
$$

**Solution.** On écrit $D=\{1<x<3,\ 2<y<5-x\}$, puis

$$
\begin{aligned}
\iint_D\frac{dx\,dy}{(x+y)^3}
&=\int_1^3\int_2^{5-x}\frac{dy\,dx}{(x+y)^3}\\
&=\int_1^3\left[-\frac1{2(x+y)^2}\right]_2^{5-x}dx\\
&=-\frac12\int_1^3\left(\frac1{25}-\frac1{(x+2)^2}\right)dx
=\frac2{75}.
\end{aligned}
$$

## Exercice 1 — Triangle $OAB$ (pages 6 et 7)

Soit $a>0$ et soit $K$ l’ensemble limité par les côtés du triangle $OAB$, avec $A=(2a,a)$ et $B=(3a,3a)$. Calculer $\iint_Kxy\,dx\,dy$.

**Solution.** Le domaine est l’union des deux triangles

$$
K_1=\{0\leq x\leq2a,\ x/2\leq y\leq x\},
\qquad K_2=\{2a\leq x\leq3a,\ 2x-3a\leq y\leq x\}.
$$

Ainsi,

$$
\begin{aligned}
\iint_Kxy\,dx\,dy
&=\iint_{K_1}xy\,dx\,dy+\iint_{K_2}xy\,dx\,dy\\
&=\int_0^{2a}\left(\int_{x/2}^xxy\,dy\right)dx
+\int_{2a}^{3a}\left(\int_{2x-3a}^xxy\,dy\right)dx\\
&=\int_0^{2a}x\left[\frac{y^2}2\right]_{x/2}^x dx
+\int_{2a}^{3a}x\left[\frac{y^2}2\right]_{2x-3a}^x dx\\
&=\int_0^{2a}\left(\frac{x^3}2-\frac{x^3}8\right)dx
+\int_{2a}^{3a}\left(\frac{x^3}2-\frac{x(2x-3a)^2}2\right)dx\\
&=\frac38\int_0^{2a}x^3\,dx
+\int_{2a}^{3a}\left(-\frac32x^3+6ax^2-\frac92a^2x\right)dx\\
&=\frac{31}8a^4.
\end{aligned}
$$

## Exercice 2 — Changement de variables (pages 8 à 12)

Soient $0<a<b$ et

$$
K=\{(x,y)\in\mathbb R^2:a\leq x+y\leq b,\ 1/3\leq y/x\leq3\}.
$$

Calculer

$$
\iint_K\frac{\exp(-(x+y))}{\sqrt{xy}}\,dx\,dy.
$$

On pourra effectuer le changement de variables $x'=x+y$, $y'=y/(x+y)$.

**Solution.** Le changement inverse est

$$
x=x'(1-y'),\qquad y=x'y'.
$$

On a $a\leq x'\leq b$ et $1/y'=1+x/y$. Comme

$$
\frac13\leq\frac yx\leq3
\Longrightarrow\frac13\leq\frac xy\leq3
\Longrightarrow\frac43\leq1+\frac xy\leq4
\Longrightarrow\frac43\leq\frac1{y'}\leq4,
$$

on obtient $1/4\leq y'\leq3/4$. Le jacobien est

$$
\det\frac{\partial(x,y)}{\partial(x',y')}
=\begin{vmatrix}1-y'&-x'\\y'&x'\end{vmatrix}
=x'>0.
$$

Par conséquent,

$$
\begin{aligned}
\iint_K\frac{e^{-(x+y)}}{\sqrt{xy}}\,dx\,dy
&=\iint_{K'}\frac{e^{-x'}}{x'\sqrt{(1-y')y'}}\,x'\,dx'\,dy'\\
&=\int_a^b e^{-x'}\left(\int_{1/4}^{3/4}
\frac{dy'}{\sqrt{(1-y')y'}}\right)dx'\\
&=\left(\int_a^b e^{-x'}dx'\right)
\left(\int_{1/4}^{3/4}\frac{dy'}{\sqrt{(1-y')y'}}\right)\\
&=(e^{-a}-e^{-b})\int_{1/4}^{3/4}\frac{dy'}{\sqrt{(1-y')y'}}.
\end{aligned}
$$

Or

$$
(1-y')y'=y'-(y')^2
=\frac14-\left(y'-\frac12\right)^2
=\frac14\left(1-(2y'-1)^2\right).
$$

Posons $u=2y'-1$, donc $du=2\,dy'$. Alors

$$
\int\frac{dy'}{\frac12\sqrt{1-(2y'-1)^2}}
=\int\frac{du}{\sqrt{1-u^2}}
=\arcsin u=\arcsin(2y'-1).
$$

Finalement,

$$
\begin{aligned}
\iint_K\frac{e^{-(x+y)}}{\sqrt{xy}}\,dx\,dy
&=(e^{-a}-e^{-b})[\arcsin(2y'-1)]_{1/4}^{3/4}\\
&=(e^{-a}-e^{-b})\left(\arcsin\frac12-\arcsin\left(-\frac12\right)\right)\\
&=2(e^{-a}-e^{-b})\arcsin\frac12
=\frac\pi3(e^{-a}-e^{-b}).
\end{aligned}
$$

## Exercice 3 — Aire entre deux paraboles (pages 13 à 15)

Soit $D$ le domaine délimité par $y^2=4x+4$ et $y^2=-4x+4$.

a) Représenter graphiquement $D$.  
b) Calculer son aire.

**Solution a).** La première courbe est définie pour $x\geq-1$ et s’écrit $y=\pm2\sqrt{x+1}$ ; la seconde est définie pour $x\leq1$ et s’écrit $y=\pm2\sqrt{1-x}$. Les régions intérieures sont

$$
D_1=\{x\geq-1,\ -2\sqrt{x+1}\leq y\leq2\sqrt{x+1}\},
$$

$$
D_2=\{x\leq1,\ -2\sqrt{1-x}\leq y\leq2\sqrt{1-x}\}.
$$

Le domaine recherché est $D=D_1\cap D_2$. Pour $x\in[-1,0]$, $2\sqrt{x+1}\leq2\sqrt{1-x}$ ; pour $x\in[0,1]$, l’inégalité est inversée. On a donc $D=U_1\cup U_2$, avec

$$
U_1=\{-1\leq x\leq0,\ -2\sqrt{x+1}\leq y\leq2\sqrt{x+1}\},
$$

$$
U_2=\{0\leq x\leq1,\ -2\sqrt{1-x}\leq y\leq2\sqrt{1-x}\}.
$$

**Solution b).**

$$
\begin{aligned}
\operatorname{Aire}(D)
&=\iint_{U_1}1\,dx\,dy+\iint_{U_2}1\,dx\,dy\\
&=\int_{-1}^0\int_{-2\sqrt{x+1}}^{2\sqrt{x+1}}1\,dy\,dx
+\int_0^1\int_{-2\sqrt{1-x}}^{2\sqrt{1-x}}1\,dy\,dx\\
&=4\int_{-1}^0\sqrt{x+1}\,dx+4\int_0^1\sqrt{1-x}\,dx\\
&=4\left[\frac23(x+1)^{3/2}\right]_{-1}^0
-4\left[\frac23(1-x)^{3/2}\right]_0^1\\
&=\frac83(1+1)=\frac{16}3.
\end{aligned}
$$

> **Coquille, page 15.** Une ligne imprime $\sqrt{x-1}$ à la place de $\sqrt{1-x}$ ; les bornes et la primitive permettent de la rectifier.

## Exercice 4 — Intégrale de Gauss (pages 16 à 21)

On se propose de calculer $\int_{-\infty}^{+\infty}e^{-x^2}\,dx$.

1. Justifier sa convergence.
2. Pour $a>0$, noter $K_a$ le carré de centre $O$ et de côté $2a$, et $C_a$ le disque de centre $O$ et de rayon $a$. Pour $f(x,y)=e^{-x^2-y^2}$, justifier

$$
\iint_{C_a}f\leq\iint_{K_a}f\leq\iint_{C_{a\sqrt2}}f.
$$

3. Calculer $\iint_{C_a}f$ en coordonnées polaires.
4. En déduire la valeur de l’intégrale initiale.

**Solution 1.** La fonction est paire : $e^{-(-x)^2}=e^{-x^2}$. Ainsi

$$
\int_{-\infty}^{+\infty}e^{-x^2}dx
=2\int_0^{+\infty}e^{-x^2}dx,
\qquad
\int_0^{+\infty}=\int_0^1+\int_1^{+\infty}.
$$

La fonction est continue et positive sur $[0,+\infty[$, donc son intégrale sur $[0,1]$ est finie. À l’infini,

$$
\frac{e^{-x^2}}{1/x^2}=\frac{x^2}{e^{x^2}}\longrightarrow0,
\qquad e^{-x^2}=o(x^{-2}).
$$

Comme $\int_1^{+\infty}dx/x^2$ converge, l’intégrale gaussienne converge.

**Solution 2.** Les inclusions $C_a\subset K_a\subset C_{a\sqrt2}$ et la positivité de $f$ donnent l’encadrement demandé.

**Solution 3.** Pour $x=r\cos\theta$, $y=r\sin\theta$,

$$
\det\frac{\partial(x,y)}{\partial(r,\theta)}
=\begin{vmatrix}\cos\theta&-r\sin\theta\\
\sin\theta&r\cos\theta\end{vmatrix}=r.
$$

Donc

$$
\begin{aligned}
\iint_{C_a}e^{-x^2-y^2}\,dx\,dy
&=\int_0^a\int_0^{2\pi}e^{-r^2}r\,d\theta\,dr\\
&=\left(\int_0^{2\pi}d\theta\right)
\left(\int_0^ae^{-r^2}r\,dr\right)\\
&=2\pi\left[-\frac{e^{-r^2}}2\right]_0^a
=\pi(1-e^{-a^2}).
\end{aligned}
$$

**Solution 4.** Le carré est $K_a=[-a,a]^2$, donc

$$
\iint_{K_a}e^{-x^2-y^2}\,dx\,dy
=\left(\int_{-a}^ae^{-x^2}dx\right)
\left(\int_{-a}^ae^{-y^2}dy\right)
=\left(\int_{-a}^ae^{-x^2}dx\right)^2.
$$

L’encadrement devient

$$
\pi(1-e^{-a^2})\leq
\left(\int_{-a}^ae^{-x^2}dx\right)^2
\leq\pi(1-e^{-2a^2}).
$$

Lorsque $a\to+\infty$, les deux bornes tendent vers $\pi$. Ainsi

$$
\left(\int_{-\infty}^{+\infty}e^{-x^2}dx\right)^2=\pi,
\qquad
\int_{-\infty}^{+\infty}e^{-x^2}dx=\sqrt\pi.
$$

## Exercice 5 — Disque décentré (pages 22 à 24)

Soit $D=\{(x,y)\in\mathbb R^2:x^2+y^2-2x\leq0\}$.

1. Montrer que $D$ est un disque.
2. Calculer $\iint_D\sqrt{x^2+y^2}\,dx\,dy$.

**Solution 1.** Puisque $x^2+y^2-2x=(x-1)^2+y^2-1$, le domaine est le disque de centre $(1,0)$ et de rayon $1$.

**Solution 2.** En coordonnées polaires $x=r\cos\theta$, $y=r\sin\theta$, de jacobien $r$,

$$
(r\cos\theta-1)^2+(r\sin\theta)^2\leq1
\Longleftrightarrow r^2-2r\cos\theta\leq0.
$$

On utilise donc $0\leq r\leq2\cos\theta$ et $-\pi/2\leq\theta\leq\pi/2$, intervalle nécessaire pour avoir $\cos\theta\geq0$. Alors

$$
\begin{aligned}
\iint_D\sqrt{x^2+y^2}\,dx\,dy
&=\int_{-\pi/2}^{\pi/2}\int_0^{2\cos\theta}\sqrt{r^2}\,r\,dr\,d\theta\\
&=\int_{-\pi/2}^{\pi/2}\int_0^{2\cos\theta}r^2\,dr\,d\theta\\
&=\int_{-\pi/2}^{\pi/2}\frac83\cos^3\theta\,d\theta.
\end{aligned}
$$

L’identité $\cos(3t)=4\cos^3t-3\cos t$ donne $\cos^3t=(3\cos t+\cos3t)/4$, d’où

$$
\iint_D\sqrt{x^2+y^2}\,dx\,dy
=\frac23\int_{-\pi/2}^{\pi/2}(3\cos\theta+\cos3\theta)\,d\theta
=\frac{32}9.
$$

> **Notation, page 24.** Les $x$ de la dernière intégrande sont remplacés par la variable d’intégration $\theta$.

## Exercice 6 — Trois intégrales doubles (pages 25 à 33)

Calculer $\iint_\Delta f(x,y)\,dx\,dy$ dans les cas suivants.

### a) Disque unité

$$
f(x,y)=\frac{(x+y)^2}{x^2+y^2+1},
\qquad\Delta=\{x^2+y^2\leq1\}.
$$

**Solution.** En coordonnées polaires de jacobien $r$,

$$
\begin{aligned}
\iint_\Delta f
&=\int_0^1\int_0^{2\pi}
\frac{r^2(\cos\theta+\sin\theta)^2}{r^2\cos^2\theta+r^2\sin^2\theta+1}
r\,d\theta\,dr\\
&=\int_0^1\int_0^{2\pi}
\frac{r^3(\cos^2\theta+2\cos\theta\sin\theta+\sin^2\theta)}{r^2+1}
\,d\theta\,dr\\
&=\left(\int_0^1\frac{r^3}{r^2+1}\,dr\right)
\left(\int_0^{2\pi}(1+\sin2\theta)\,d\theta\right)\\
&=\left(\int_0^1\frac{r(r^2+1-1)}{r^2+1}\,dr\right)
\left[\theta-\frac{\cos2\theta}2\right]_0^{2\pi}\\
&=2\pi\int_0^1\left(r-\frac r{r^2+1}\right)dr.
\end{aligned}
$$

Avec $u=r^2$,

$$
\iint_\Delta f
=2\pi\left(\left[\frac{r^2}2\right]_0^1
-\frac12\int_0^1\frac{du}{u+1}\right)
=\pi\left(1-[\ln(u+1)]_0^1\right)
=\pi-\pi\ln2.
$$

### b) Disque de centre $(R,0)$

$$
f(x,y)=xy^2,\qquad
\Delta\text{ est le disque délimité par }x^2+y^2-2Rx=0,\quad R>0.
$$

**Solution.** L’équation du cercle est $(x-R)^2+y^2=R^2$. Posons $u=x-R$, $v=y$, avec jacobien

$$
\det\frac{\partial(x,y)}{\partial(u,v)}
=\begin{vmatrix}1&0\\0&1\end{vmatrix}=1.
$$

Le domaine devient $\Delta'=\{u^2+v^2\leq R^2\}$, et

$$
\iint_\Delta xy^2\,dx\,dy
=\iint_{\Delta'}(u+R)v^2\,du\,dv.
$$

On pose ensuite $u=r\cos\theta$, $v=r\sin\theta$, de jacobien $r$. On aurait pu employer directement $x-R=r\cos\theta$, $y=r\sin\theta$. On obtient

$$
\begin{aligned}
\iint_\Delta xy^2\,dx\,dy
&=\int_0^R\int_0^{2\pi}(R+r\cos\theta)r^2\sin^2\theta\,r\,d\theta\,dr\\
&=R\left(\int_0^Rr^3dr\right)\left(\int_0^{2\pi}\sin^2\theta\,d\theta\right)
+\left(\int_0^Rr^4dr\right)
\left(\int_0^{2\pi}\cos\theta\sin^2\theta\,d\theta\right)\\
&=\frac{R^5}4\left[\frac\theta2-\frac{\sin2\theta}4\right]_0^{2\pi}
+\frac{R^5}5\int_0^{2\pi}\cos\theta\sin^2\theta\,d\theta\\
&=\frac{\pi R^5}4+\frac{R^5}5
\left[\frac{\sin^3\theta}3\right]_0^{2\pi}
=\frac{\pi R^5}4.
\end{aligned}
$$

La primitive du dernier terme vient de $w=\sin\theta$ :
$\int\cos\theta\sin^2\theta\,d\theta=\int w^2dw=w^3/3$.

> **Coquille, page 29.** Les bornes supérieures de deux intégrales radiales sont imprimées $r$ ; il s’agit de $R$, comme dans les lignes précédentes et suivantes.

### c) Domaine elliptique

$$
f(x,y)=x^2+y^2,
\qquad\Delta=\{x^2/a^2+y^2/b^2\leq1\}.
$$

**Solution.** Posons $u=x/a$, $v=y/b$. Le déterminant de la transformation inverse vaut

$$
\begin{vmatrix}a&0\\0&b\end{vmatrix}=ab.
$$

Le domaine devient le disque unité $\Delta'$. Ainsi

$$
\iint_\Delta(x^2+y^2)\,dx\,dy
=ab\iint_{\Delta'}(a^2u^2+b^2v^2)\,du\,dv.
$$

Après le changement polaire $u=r\cos\theta$, $v=r\sin\theta$, ou directement avec les coordonnées elliptiques $x=ar\cos\theta$, $y=br\sin\theta$, dont le jacobien est

$$
\begin{vmatrix}a\cos\theta&-ar\sin\theta\\
b\sin\theta&br\cos\theta\end{vmatrix}=abr,
$$

on trouve

$$
\begin{aligned}
\iint_\Delta(x^2+y^2)\,dx\,dy
&=\int_0^1\int_0^{2\pi}
(a^2r^2\cos^2\theta+b^2r^2\sin^2\theta)abr\,d\theta\,dr\\
&=ab\int_0^1r^3dr\int_0^{2\pi}
(a^2\cos^2\theta+b^2\sin^2\theta)\,d\theta\\
&=\frac{ab}4\left(
a^2\int_0^{2\pi}\frac{1+\cos2\theta}2\,d\theta
+b^2\int_0^{2\pi}\frac{1-\cos2\theta}2\,d\theta\right)\\
&=\frac{ab}4\left(
a^2\left[\frac\theta2+\frac{\sin2\theta}4\right]_0^{2\pi}
+b^2\left[\frac\theta2-\frac{\sin2\theta}4\right]_0^{2\pi}\right)\\
&=\frac{ab}4(a^2\pi+b^2\pi)
=\frac{ab\pi}4(a^2+b^2).
\end{aligned}
$$

> **Hypothèse implicite de la source.** Ce calcul emploie $a,b>0$, comme longueurs des demi-axes. Pour des paramètres non nuls de signe quelconque, le facteur de changement de variables serait $|ab|$.

## Exercice 7 — Aires et volumes (pages 34 à 42)

### a) Domaine entre $y=x^2$ et $x=y^2$

Calculer $\iint_\Delta xy\,dx\,dy$, où $\Delta$ est la région limitée par les deux courbes.

**Solution.** Le domaine est $\Delta=\{0\leq x\leq1,\ x^2\leq y\leq\sqrt x\}$. Alors

$$
\begin{aligned}
\iint_\Delta xy\,dx\,dy
&=\int_0^1\int_{x^2}^{\sqrt x}xy\,dy\,dx\\
&=\int_0^1x\left[\frac{y^2}2\right]_{x^2}^{\sqrt x}dx
=\int_0^1\left(\frac{x^2}2-\frac{x^5}2\right)dx\\
&=\left[\frac{x^3}6\right]_0^1-\left[\frac{x^6}{12}\right]_0^1
=\frac16-\frac1{12}=\frac1{12}.
\end{aligned}
$$

### b) Aire d’une ellipse

Calculer l’aire limitée par $x^2/a^2+y^2/b^2=1$, avec $a>1$, $b>1$.

**Solution.** Sur $\Delta=\{x^2/a^2+y^2/b^2\leq1\}$, les coordonnées elliptiques
$x=ar\cos\theta$, $y=br\sin\theta$ ont pour jacobien $abr$. Ainsi

$$
\begin{aligned}
\operatorname{Aire}(\Delta)
&=\iint_\Delta1\,dx\,dy
=\int_0^1\int_0^{2\pi}abr\,d\theta\,dr\\
&=ab\left(\int_0^1r\,dr\right)\left(\int_0^{2\pi}d\theta\right)
=ab\left[\frac{r^2}2\right]_0^1[\theta]_0^{2\pi}
=ab\pi.
\end{aligned}
$$

### c) Volume d’un ellipsoïde

Calculer le volume limité par $x^2/a^2+y^2/b^2+z^2/c^2=1$, avec $a,b,c>1$.

**Solution.** Le solide est

$$
\Delta=\{(x,y,z)\in\mathbb R^3:x^2/a^2+y^2/b^2+z^2/c^2\leq1\}.
$$

Le changement $u=x/a$, $v=y/b$, $w=z/c$ a pour jacobien inverse

$$
\det\frac{\partial(x,y,z)}{\partial(u,v,w)}
=\begin{vmatrix}a&0&0\\0&b&0\\0&0&c\end{vmatrix}=abc.
$$

Il transforme $\Delta$ en $\nabla=\{u^2+v^2+w^2\leq1\}$, donc

$$
\iiint_\Delta1\,dx\,dy\,dz=abc\iiint_\nabla du\,dv\,dw.
$$

Utilisons les coordonnées sphériques

$$
u=r\sin\varphi\cos\theta,\quad
v=r\sin\varphi\sin\theta,\quad w=r\cos\varphi,
$$

avec $0\leq r\leq1$, $-\pi\leq\theta\leq\pi$, $0\leq\varphi\leq\pi$ et valeur absolue du jacobien $r^2\sin\varphi$. Alors

$$
\begin{aligned}
\operatorname{Vol}(\Delta)
&=abc\int_0^1\int_{-\pi}^{\pi}\int_0^\pi
r^2\sin\varphi\,d\varphi\,d\theta\,dr\\
&=abc\left(\int_0^1r^2dr\right)
\left(\int_{-\pi}^\pi d\theta\right)
\left(\int_0^\pi\sin\varphi\,d\varphi\right)\\
&=abc\left[\frac{r^3}3\right]_0^1
[\theta]_{-\pi}^{\pi}[-\cos\varphi]_0^\pi
=\frac{4\pi}3abc.
\end{aligned}
$$

> **Précision, pages 38 et 45.** Pour l’ordre des variables $(r,\theta,\varphi)$ employé dans le PDF, le déterminant signé est $-r^2\sin\varphi$. Le facteur d’intégration est sa valeur absolue $r^2\sin\varphi$. Il est strictement positif pour $r>0$ et $0<\varphi<\pi$, et nul sur les frontières correspondantes.

### d) Volume d’un secteur sphérique

Calculer le volume limité par la sphère de centre $O$ et de rayon $R$ et le demi-cône supérieur de sommet $O$ et d’angle $2\alpha$, avec $0<\alpha<\pi/2$.

**Solution.** Le cône est $x^2+y^2=z^2\tan^2\alpha$ ; le demi-cône supérieur ajoute la condition $z\geq0$. Dans les coordonnées sphériques précédentes,

$$
r^2\sin^2\varphi(\cos^2\theta+\sin^2\theta)
=r^2\cos^2\varphi\tan^2\alpha.
$$

Hors du sommet, cela donne $\tan^2\varphi=\tan^2\alpha$ ; sur le demi-cône supérieur, $\varphi=\alpha$. Son intérieur correspond à $0\leq\varphi\leq\alpha$. La sphère est $r=R$ et son intérieur $0\leq r\leq R$. Le secteur est donc

$$
\Delta=\{0\leq r\leq R,\ -\pi\leq\theta\leq\pi,\ 0\leq\varphi\leq\alpha\}.
$$

Son volume vaut

$$
\begin{aligned}
\operatorname{Vol}(\Delta)
&=\int_0^R\int_{-\pi}^{\pi}\int_0^\alpha
r^2\sin\varphi\,d\varphi\,d\theta\,dr\\
&=\left(\int_0^Rr^2dr\right)
\left(\int_{-\pi}^{\pi}d\theta\right)
\left(\int_0^\alpha\sin\varphi\,d\varphi\right)\\
&=\frac{2\pi R^3}3(1-\cos\alpha).
\end{aligned}
$$

> **Coquilles, pages 40 et 42.** Un $\cos^2\theta$ remplace $\cos^2\varphi$ dans l’équation du cône ; le premier facteur d’intégration du volume est imprimé $r^2\cos\varphi$ au lieu de $r^2\sin\varphi$ ; l’intégrale sur $[-\pi,\pi]$ porte $d\varphi$ au lieu de $d\theta$. Le résultat final du PDF est correct.

## Exercice 8 — Trois intégrales triples (pages 43 à 47)

Calculer $\iiint_\Omega f(x,y,z)\,dx\,dy\,dz$ dans les cas suivants.

### a) Simplexe unité

$$
f(x,y,z)=\frac1{(x+y+z+1)^3},
\quad\Omega=\{x\geq0,\ y\geq0,\ z\geq0,\ x+y+z\leq1\}.
$$

**Solution.** Le domaine s’écrit d’abord
$\{x,y\geq0,\ 0\leq z\leq1-x-y,\ x+y\leq1\}$, puis

$$
\Omega=\{0\leq x\leq1,\ 0\leq y\leq1-x,\ 0\leq z\leq1-x-y\}.
$$

D’où

$$
\begin{aligned}
\iiint_\Omega f
&=\int_0^1\int_0^{1-x}\int_0^{1-x-y}
\frac{dz\,dy\,dx}{(x+y+z+1)^3}\\
&=\int_0^1\int_0^{1-x}
\left[-\frac1{2(x+y+z+1)^2}\right]_0^{1-x-y}dy\,dx\\
&=\frac12\int_0^1\int_0^{1-x}
\left(\frac1{(x+y+1)^2}-\frac14\right)dy\,dx\\
&=\frac12\int_0^1\left[-\frac1{x+y+1}-\frac y4\right]_0^{1-x}dx\\
&=\frac12\int_0^1\left(\frac1{x+1}-\frac12-\frac{1-x}4\right)dx\\
&=\frac12\left[\ln(x+1)-\frac x2+\frac{(1-x)^2}8\right]_0^1\\
&=\frac12\left(\ln2-\frac12-\frac18\right)
=\frac{\ln2}2-\frac5{16}.
\end{aligned}
$$

### b) Inverse du carré de la distance à l’origine

$$
f(x,y,z)=\frac1{x^2+y^2+z^2},
\qquad\Omega=\{x^2+y^2+z^2\leq R^2\}.
$$

**Solution.** En coordonnées sphériques,

$$
\begin{aligned}
\iiint_\Omega\frac{dx\,dy\,dz}{x^2+y^2+z^2}
&=\int_0^R\int_{-\pi}^{\pi}\int_0^\pi
\frac1{r^2}r^2\sin\varphi\,d\varphi\,d\theta\,dr\\
&=\int_0^R\int_{-\pi}^{\pi}\int_0^\pi
\sin\varphi\,d\varphi\,d\theta\,dr\\
&=[r]_0^R[\theta]_{-\pi}^{\pi}[-\cos\varphi]_0^\pi
=4\pi R.
\end{aligned}
$$

> **Précision de lecture.** L’intégrande est singulière à l’origine. Le calcul se comprend en intégrant d’abord sur $\varepsilon\leq r\leq R$, puis en faisant tendre $\varepsilon$ vers zéro ; la limite est finie.

### c) Solide entre deux plans

$$
f(x,y,z)=x^2y,
\qquad\Omega=\{0\leq y\leq1-x^2,\ |x+y+z|\leq1\}.
$$

**Solution.** L’inégalité $|x+y+z|\leq1$ signifie
$-1\leq x+y+z\leq1$. Le solide est limité par les plans $x+y+z=\pm1$ ; sa projection sur $xOy$ est

$$
\Omega_1=\{-1\leq x\leq1,\ 0\leq y\leq1-x^2\}.
$$

Alors

$$
\begin{aligned}
\iiint_\Omega x^2y\,dx\,dy\,dz
&=\int_{-1}^1\int_0^{1-x^2}\int_{-1-x-y}^{1-x-y}
x^2y\,dz\,dy\,dx\\
&=\int_{-1}^1\int_0^{1-x^2}[x^2yz]_{-1-x-y}^{1-x-y}\,dy\,dx\\
&=\int_{-1}^1\int_0^{1-x^2}
x^2y\bigl((1-x-y)-(-1-x-y)\bigr)\,dy\,dx\\
&=\int_{-1}^1\int_0^{1-x^2}2x^2y\,dy\,dx\\
&=\int_{-1}^1[x^2y^2]_0^{1-x^2}dx
=\int_{-1}^1x^2(1-x^2)^2dx\\
&=\int_{-1}^1(x^2-2x^4+x^6)dx
=2\left(\frac13-\frac25+\frac17\right)=\frac{16}{105}.
\end{aligned}
$$

## Exercice 9 — Premier octant de la boule unité (pages 48 à 50)

Calculer $\iiint_Dxyz\,dx\,dy\,dz$, où $D$ est limité par les plans $x=0$, $y=0$, $z=0$ et la sphère de centre $O$ et de rayon $1$, dans la région de coordonnées positives.

**Solution.**

$$
D=\{x,y,z\geq0,\ x^2+y^2+z^2\leq1\}.
$$

La projection sur $xOy$ est le quart de disque unité dans le premier quadrant. Ainsi

$$
D=\{0\leq x\leq1,\ 0\leq y\leq\sqrt{1-x^2},\
0\leq z\leq\sqrt{1-x^2-y^2}\}.
$$

On obtient

$$
\begin{aligned}
\iiint_Dxyz\,dx\,dy\,dz
&=\int_0^1\int_0^{\sqrt{1-x^2}}\int_0^{\sqrt{1-x^2-y^2}}
xyz\,dz\,dy\,dx\\
&=\int_0^1\int_0^{\sqrt{1-x^2}}xy
\left[\frac{z^2}2\right]_0^{\sqrt{1-x^2-y^2}}dy\,dx\\
&=\int_0^1\int_0^{\sqrt{1-x^2}}\frac{xy(1-x^2-y^2)}2\,dy\,dx\\
&=\int_0^1\frac x2\left(\int_0^{\sqrt{1-x^2}}
((1-x^2)y-y^3)\,dy\right)dx\\
&=\int_0^1\frac x2
\left[(1-x^2)\frac{y^2}2-\frac{y^4}4\right]_0^{\sqrt{1-x^2}}dx\\
&=\int_0^1\frac x2
\left(\frac{(1-x^2)^2}2-\frac{(1-x^2)^2}4\right)dx\\
&=\int_0^1\frac{x(1-x^2)^2}8\,dx
=\left[-\frac{(1-x^2)^3}{48}\right]_0^1
=\frac1{48}.
\end{aligned}
$$

## Exercice 10 — Intersection d’une boule et d’un cylindre (pages 51 à 54)

Calculer le volume limité par la sphère de centre $O$ et de rayon $1$ et le cylindre d’équation $x^2+y^2-x=0$.

**Solution.** Utilisons les coordonnées cylindriques

$$
x=r\cos\theta,\quad y=r\sin\theta,\quad z=z,
\qquad r\geq0,\quad-\pi\leq\theta\leq\pi,\quad z\in\mathbb R,
$$

de jacobien $r$ (strictement positif pour $r>0$).

La sphère $x^2+y^2+z^2=1$ devient $r^2+z^2=1$. Son intérieur est décrit par

$$
0\leq r\leq1,\quad-\pi\leq\theta\leq\pi,\quad
-\sqrt{1-r^2}\leq z\leq\sqrt{1-r^2}.
$$

Le cylindre a pour équation $(x-1/2)^2+y^2=1/4$ ; en cylindriques, sa frontière est $r=\cos\theta$, avec l’axe $r=0$ également inclus. Son intérieur s’écrit
$0\leq r\leq\cos\theta$, $-\pi/2\leq\theta\leq\pi/2$, $z\in\mathbb R$.
L’intervalle angulaire assure $\cos\theta\geq0$. Le domaine commun est donc

$$
\Delta=\{-\pi/2\leq\theta\leq\pi/2,\ 0\leq r\leq\cos\theta,\
-\sqrt{1-r^2}\leq z\leq\sqrt{1-r^2}\}.
$$

Par conséquent,

$$
\begin{aligned}
\operatorname{Vol}(\Delta)
&=\int_{-\pi/2}^{\pi/2}\int_0^{\cos\theta}
\int_{-\sqrt{1-r^2}}^{\sqrt{1-r^2}}r\,dz\,dr\,d\theta\\
&=\int_{-\pi/2}^{\pi/2}\int_0^{\cos\theta}
r[z]_{-\sqrt{1-r^2}}^{\sqrt{1-r^2}}\,dr\,d\theta\\
&=\int_{-\pi/2}^{\pi/2}\int_0^{\cos\theta}
2r\sqrt{1-r^2}\,dr\,d\theta\\
&=\int_{-\pi/2}^{\pi/2}\left[-\frac23(1-r^2)^{3/2}\right]_0^{\cos\theta}d\theta\\
&=\frac23\int_{-\pi/2}^{\pi/2}\left(1-(1-\cos^2\theta)^{3/2}\right)d\theta\\
&=\frac23\int_{-\pi/2}^{\pi/2}(1-|\sin^3\theta|)\,d\theta\\
&=\frac{2\pi}3-\frac43\int_0^{\pi/2}\sin^3\theta\,d\theta.
\end{aligned}
$$

Enfin,

$$
\begin{aligned}
\int_0^{\pi/2}\sin^3\theta\,d\theta
&=\int_0^{\pi/2}\sin\theta(1-\cos^2\theta)\,d\theta\\
&=[-\cos\theta]_0^{\pi/2}
-\left[-\frac{\cos^3\theta}3\right]_0^{\pi/2}\\
&=1-\frac13=\frac23.
\end{aligned}
$$

Donc

$$
\operatorname{Vol}(\Delta)=\frac{2\pi}3-\frac89.
$$
