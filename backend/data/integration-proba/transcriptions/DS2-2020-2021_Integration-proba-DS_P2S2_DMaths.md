---
source: "PREING2-S2/Integration-proba-DS/DS2-2020-2021_Integration-proba-DS_P2S2_DMaths.pdf"
pages: 6
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-14
verification: lecture visuelle des six pages ; domaines, changements de variables, primitives et intégrales vérifiés
---

# Intégration et probabilités — DS2 du 6 mai 2021 : sujet et corrigé

**PréING2 — département de mathématiques — durée : 1 h 30.** Appareils électroniques et documents interdits. Cinq exercices indépendants ; rédaction et précision des justifications prises en compte. Le PDF contient les solutions en bleu, malgré l’absence de « Correction » dans son nom.

## Exercice 1 — Intégrales doubles (pages 1–2)

**Énoncé.** Représenter chaque domaine $D\subset\mathbb R^2$ et calculer les intégrales suivantes.

**1.** $I=\iint_D(x+y)^{-2}\,dx\,dy$, avec

$$D=\{(x,y):x\ge0,\ y\ge0,\ 1\le x\le y^2\le4\}.$$

**Correction.** Le domaine est limité par $x=1$, $y=2$ et $y=\sqrt x$ :

$$D=\{1\le x\le4,\ \sqrt x\le y\le2\}
=\{1\le y\le2,\ 1\le x\le y^2\}.$$

Le dessin page 1 colorie cette région au-dessus de la courbe $y=\sqrt x$. La fonction est continue sur ce domaine compact, où $x+y>0$ ; Fubini s’applique :

$$\begin{aligned}
I&=\int_1^2\left(\int_1^{y^2}\frac{dx}{(x+y)^2}\right)dy
=\int_1^2\left(\frac1{1+y}-\frac1{y^2+y}\right)dy\\
&=\int_1^2\left(\frac2{1+y}-\frac1y\right)dy
=[2\ln(1+y)-\ln y]_1^2
=2\ln3-3\ln2.
\end{aligned}$$

> **Coquille de la source.** La description textuelle mentionne le rectangle $[0,4]\times[0,2]$ sans rappeler $x\ge1$. Le dessin et les bornes de l’intégrale sont corrects.

**2.** $J=\iint_D\dfrac{x^2+y^2}{x^2+y^2+1}\,dx\,dy$, où $D$ est le disque unité $x^2+y^2\le1$.

**Correction.** Posons $x=\rho\cos\theta$, $y=\rho\sin\theta$, avec $0\le\rho\le1$, $0\le\theta\le2\pi$ et $dx\,dy=\rho\,d\rho\,d\theta$. Ainsi

$$\begin{aligned}
J&=2\pi\int_0^1\frac{\rho^3}{1+\rho^2}\,d\rho
=2\pi\int_0^1\left(\rho-\frac{\rho}{1+\rho^2}\right)d\rho\\
&=2\pi\left[\frac{\rho^2}{2}-\frac12\ln(1+\rho^2)\right]_0^1
=\pi(1-\ln2).
\end{aligned}$$

**3.** $K=\iint_Dxy^2\,dx\,dy$, où $D$ est le disque délimité par $x^2+y^2-2Rx=0$, $R>0$.

**Correction.** L’équation du bord est $(x-R)^2+y^2=R^2$. Le disque a pour centre $(R,0)$ et pour rayon $R$. Avec

$$x=R+\rho\cos\theta,\quad y=\rho\sin\theta,\quad
0\le\rho\le R,\quad 0\le\theta\le2\pi,$$

le jacobien vaut $\rho$. On obtient

$$\begin{aligned}
K&=\int_0^R\rho^3\int_0^{2\pi}
\bigl(R\sin^2\theta+\rho\cos\theta\sin^2\theta\bigr)\,d\theta\,d\rho\\
&=\int_0^R\rho^3\left[\frac{R\theta}{2}-\frac{R\sin(2\theta)}4+\frac\rho3\sin^3\theta\right]_0^{2\pi}d\rho\\
&=\pi R\int_0^R\rho^3\,d\rho=\frac{\pi R^5}{4}.
\end{aligned}$$

> **Coquille de la source.** La primitive angulaire comporte $\rho^3\sin^3\theta/3$ au lieu de $\rho\sin^3\theta/3$. Ce terme s’annule aux deux bornes : le résultat final du PDF reste correct. L’ordre des différentielles de certaines intégrales polaires a également été aligné sur leurs bornes.

## Exercice 2 — Changement de variables (pages 2–3)

**Énoncé.** Pour $0<a<b$, on pose

$$D=\left\{(x,y)\in\mathbb R^2:a\le x+y\le b,\quad\frac13\le\frac yx\le3\right\}.$$

Calculer $I=\iint_D e^{-(x+y)}/\sqrt{xy}\,dx\,dy$. Indication : utiliser $x'=x+y$ et $y'=y/(x+y)$.

**Correction.** Le rapport $y/x$ est positif et la somme $x+y$ est positive ; donc $x,y>0$. Le changement

$$u=x+y,\quad v=\frac y{x+y},\qquad x=u(1-v),\quad y=uv$$

transforme le domaine en $\Delta=[a,b]\times[1/4,3/4]$. En effet, $1/v=1+x/y\in[4/3,4]$. Le changement et son inverse sont réguliers sur des voisinages du domaine ; le déterminant du jacobien inverse vaut

$$\det\begin{pmatrix}1-v&-u\\v&u\end{pmatrix}=u>0.$$

Ainsi,

$$\begin{aligned}
I&=\int_a^b\int_{1/4}^{3/4}\frac{e^{-u}}{u\sqrt{v(1-v)}}\,u\,dv\,du\\
&=(e^{-a}-e^{-b})\int_{1/4}^{3/4}\frac{dv}{\sqrt{v(1-v)}}.
\end{aligned}$$

En posant $w=\sqrt v$, $dv=2w\,dw$,

$$\int_{1/4}^{3/4}\frac{dv}{\sqrt{v(1-v)}}
=2\int_{1/2}^{\sqrt3/2}\frac{dw}{\sqrt{1-w^2}}
=2[\arcsin w]_{1/2}^{\sqrt3/2}=\frac\pi3.$$

Donc $\boxed{I=\frac\pi3(e^{-a}-e^{-b})}$.

## Exercice 3 — Intégrale sur une boule (page 3)

**Énoncé.** Soit $B$ la boule unité de centre $O$ et $a>1$. Calculer

$$I=\iiint_B\frac{dx\,dy\,dz}{\sqrt{x^2+y^2+(z-a)^2}}.$$

**Correction.** En coordonnées sphériques,

$$x=r\sin\varphi\cos\theta,\quad y=r\sin\varphi\sin\theta,\quad z=r\cos\varphi,$$

avec $r\in[0,1]$, $\theta\in[-\pi,\pi]$, $\varphi\in[0,\pi]$ et jacobien $r^2\sin\varphi$,

$$I=2\pi\int_0^1r^2\left(\int_0^\pi
\frac{\sin\varphi\,d\varphi}{\sqrt{r^2+a^2-2ar\cos\varphi}}\right)dr.$$

Pour $r>0$, poser $t=r^2+a^2-2ar\cos\varphi$ donne $dt=2ar\sin\varphi\,d\varphi$ et

$$\int_0^\pi\frac{\sin\varphi\,d\varphi}{\sqrt{r^2+a^2-2ar\cos\varphi}}
=\int_{(a-r)^2}^{(a+r)^2}\frac{dt}{2ar\sqrt t}
=\frac{(a+r)-(a-r)}{ar}=\frac2a.$$

On a utilisé $a>1\ge r$, donc $|a-r|=a-r$. Le point $r=0$ ne change pas l’intégrale. Finalement,

$$I=\frac{4\pi}a\int_0^1r^2\,dr=\boxed{\frac{4\pi}{3a}}.$$

## Exercice 4 — Formes différentielles (pages 4–5)

**I. Énoncé.** Dire si les formes suivantes sont fermées et exactes ; lorsqu’elles sont exactes, déterminer leurs primitives.

**a)** $\omega=2xy\,dx+x^2\,dy$.

**Correction.** Pour $\omega=P\,dx+Q\,dy$, $\partial_yP=2x=\partial_xQ$ : la forme est fermée. Elle est définie sur l’ouvert étoilé $\mathbb R^2$ ; le lemme de Poincaré la rend exacte. Chercher $df=\omega$ donne

$$\partial_xf=2xy,\qquad\partial_yf=x^2.$$

La première équation donne $f=x^2y+\psi(y)$. La seconde impose $\psi'(y)=0$, donc

$$f(x,y)=x^2y+C,\qquad C\in\mathbb R.$$

> Le PDF écrit une fois $\psi(y)=0$ au lieu de $\psi'(y)=0$. Son introduction générale en trois variables est inutile ici : les formes sont définies sur $\mathbb R^2$.

**b)** $\omega=2xe^{x^2-y}\,dx-2e^{x^2-y}\,dy$.

**Correction.** $\partial_yP=-2xe^{x^2-y}$ et $\partial_xQ=-4xe^{x^2-y}$ ne sont pas identiques. La forme n’est pas fermée et n’est donc pas exacte sur $\mathbb R^2$.

**II. Énoncé.** Soit $\omega=(x^2+y^2-1)\,dx-2y\,dy$.

**a)** Montrer qu’elle n’est pas exacte.

**Correction.** $\partial_yP=2y$ et $\partial_xQ=0$ : elle n’est pas fermée, donc pas exacte.

**b)** Déterminer $\phi$ telle que $\omega_1=\phi(x)\omega$ soit fermée.

**Correction.** La condition est

$$2y\phi(x)=-2y\phi'(x)\quad\text{pour tout }(x,y),$$

soit $\phi'=-\phi$. Les solutions sont $\phi(x)=ce^{-x}$. On choisit $\phi(x)=e^{-x}$.

**c)** Montrer que $\omega_1$ est exacte et déterminer une primitive.

**Correction.** La forme est fermée sur $\mathbb R^2$, donc exacte par Poincaré. Les équations

$$\partial_xf=(x^2+y^2-1)e^{-x},\qquad\partial_yf=-2ye^{-x}$$

donnent $f=-y^2e^{-x}+\psi(x)$ et $\psi'(x)=(x^2-1)e^{-x}$. Deux intégrations par parties donnent $\psi(x)=-(x+1)^2e^{-x}+C$, d’où

$$f(x,y)=-\bigl((x+1)^2+y^2\bigr)e^{-x}+C.$$

**d)** Calculer $\int_\Gamma\omega_1$, où $\Gamma$ est le cercle de centre $O$ et rayon $R$.

**Correction.** L’intégrale d’une forme exacte sur un lacet est nulle : $\boxed{\int_\Gamma\omega_1=0}$. La mention $\Gamma_1$ dans cette phrase du PDF est une coquille pour $\Gamma$.

## Exercice 5 — Aire d’un quart d’ellipse par Green–Riemann (pages 5–6)

**Énoncé.** Pour $a,b>0$, calculer par Green–Riemann l’aire de

$$K=\left\{(x,y):x\ge0,\ y\ge0,\ \frac{x^2}{a^2}+\frac{y^2}{b^2}\le1\right\}.$$

**Correction.** Avec $P=-y/2$ et $Q=x/2$, on a $\partial_xQ-\partial_yP=1$. Donc

$$\operatorname{Aire}(K)=\iint_K1\,dx\,dy=\frac12\oint_\Gamma(-y\,dx+x\,dy),$$

où $\Gamma$ est orienté positivement. Décomposer le bord en l’arc elliptique $\Gamma_1$, le segment vertical $\Gamma_2$ et le segment horizontal $\Gamma_3$. Les orientations compatibles sont : $(a,0)\to(0,b)$ sur l’arc, $(0,b)\to(0,0)$ sur le segment vertical, puis $(0,0)\to(a,0)$ sur le segment horizontal.

Sur $\Gamma_2$, $x=dx=0$ ; sur $\Gamma_3$, $y=dy=0$. Les deux contributions sont nulles. Sur l’arc,

$$x=a\cos t,\quad y=b\sin t,\quad dx=-a\sin t\,dt,\quad dy=b\cos t\,dt,\quad 0\le t\le\pi/2.$$

Ainsi,

$$\operatorname{Aire}(K)=\frac12\int_0^{\pi/2}ab(\sin^2t+\cos^2t)\,dt=\boxed{\frac{\pi ab}{4}}.$$

> **Coquille de la source (page 6).** La dernière intégrale curviligne est notée sur $\Gamma_3$, alors que le paramétrage et le calcul concernent l’arc $\Gamma_1$. Les orientations, implicites dans le PDF, sont explicitées ici.
