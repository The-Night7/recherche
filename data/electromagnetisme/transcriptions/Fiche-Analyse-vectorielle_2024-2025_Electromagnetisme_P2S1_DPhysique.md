---
source: PREING2-S1/Electromagnetisme/Fiche-Analyse-vectorielle_2024-2025_Electromagnetisme_P2S1_DPhysique.pdf
pages: 1
transcription: manuelle
verification: lecture intégrale de la source
---

# Électromagnétisme — Formulaire d’analyse vectorielle

## Calcul vectoriel

$$\operatorname{rot}(\operatorname{grad}V)=\vec0,\qquad
\operatorname{div}(\operatorname{rot}\vec A)=0,$$

$$\operatorname{div}(\operatorname{grad}V)=\Delta V,\qquad
\operatorname{rot}(\operatorname{rot}\vec A)=\operatorname{grad}(\operatorname{div}\vec A)-\Delta\vec A.$$

$$\operatorname{grad}(V_1V_2)=V_1\operatorname{grad}V_2+V_2\operatorname{grad}V_1,$$

$$\operatorname{rot}(V\vec A)=V\operatorname{rot}\vec A+\operatorname{grad}V\wedge\vec A,$$

$$\operatorname{div}(V\vec A)=V\operatorname{div}\vec A+\operatorname{grad}V\cdot\vec A,$$

$$\operatorname{div}(\vec A_1\wedge\vec A_2)
=\vec A_2\cdot\operatorname{rot}\vec A_1-\vec A_1\cdot\operatorname{rot}\vec A_2.$$

## Coordonnées cartésiennes

Le schéma représente $M(x,y,z)$ et sa projection $m$ sur le plan $(x,y)$.

$$\operatorname{grad}V=\frac{\partial V}{\partial x}\vec u_x+
\frac{\partial V}{\partial y}\vec u_y+\frac{\partial V}{\partial z}\vec u_z,$$

$$\operatorname{div}\vec A=\frac{\partial A_x}{\partial x}+
\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z},$$

$$\begin{aligned}
\operatorname{rot}\vec A={}&\left(\frac{\partial A_z}{\partial y}-\frac{\partial A_y}{\partial z}\right)\vec u_x\\
&+\left(\frac{\partial A_x}{\partial z}-\frac{\partial A_z}{\partial x}\right)\vec u_y\\
&+\left(\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}\right)\vec u_z,
\end{aligned}$$

$$\Delta V=\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}.$$

L’annotation manuscrite ajoute :

$$\Delta\vec A=(\Delta A_x)\vec u_x+(\Delta A_y)\vec u_y+(\Delta A_z)\vec u_z.$$

## Coordonnées cylindriques

Le schéma indique le rayon $r$ dans le plan $(x,y)$, l’angle azimutal $\theta$, la hauteur $z$ et la base locale $(\vec u_r,\vec u_\theta,\vec u_z)$.

$$\operatorname{grad}V=\frac{\partial V}{\partial r}\vec u_r+
\frac1r\frac{\partial V}{\partial\theta}\vec u_\theta+
\frac{\partial V}{\partial z}\vec u_z,$$

$$\operatorname{div}\vec A=\frac1r\frac{\partial(rA_r)}{\partial r}+
\frac1r\frac{\partial A_\theta}{\partial\theta}+\frac{\partial A_z}{\partial z},$$

$$\begin{aligned}
\operatorname{rot}\vec A={}&\left(\frac1r\frac{\partial A_z}{\partial\theta}-\frac{\partial A_\theta}{\partial z}\right)\vec u_r\\
&+\left(\frac{\partial A_r}{\partial z}-\frac{\partial A_z}{\partial r}\right)\vec u_\theta\\
&+\frac1r\left(\frac{\partial(rA_\theta)}{\partial r}-\frac{\partial A_r}{\partial\theta}\right)\vec u_z,
\end{aligned}$$

$$\Delta V=\frac1r\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right)+
\frac1{r^2}\frac{\partial^2V}{\partial\theta^2}+\frac{\partial^2V}{\partial z^2}.$$

## Coordonnées sphériques

Le schéma indique $r=OM$, l’angle polaire $\theta$ mesuré depuis l’axe $z$, l’angle azimutal $\phi$ dans le plan $(x,y)$ et la base locale $(\vec u_r,\vec u_\theta,\vec u_\phi)$.

$$\operatorname{grad}V=\frac{\partial V}{\partial r}\vec u_r+
\frac1r\frac{\partial V}{\partial\theta}\vec u_\theta+
\frac1{r\sin\theta}\frac{\partial V}{\partial\phi}\vec u_\phi,$$

$$\operatorname{div}\vec A=\frac1{r^2}\frac{\partial(r^2A_r)}{\partial r}+
\frac1{r\sin\theta}\frac{\partial(\sin\theta A_\theta)}{\partial\theta}+
\frac1{r\sin\theta}\frac{\partial A_\phi}{\partial\phi},$$

$$\begin{aligned}
\operatorname{rot}\vec A={}&\frac1{r\sin\theta}\left(\frac{\partial(\sin\theta A_\phi)}{\partial\theta}-\frac{\partial A_\theta}{\partial\phi}\right)\vec u_r\\
&+\frac1r\left(\frac1{\sin\theta}\frac{\partial A_r}{\partial\phi}-\frac{\partial(rA_\phi)}{\partial r}\right)\vec u_\theta\\
&+\frac1r\left(\frac{\partial(rA_\theta)}{\partial r}-\frac{\partial A_r}{\partial\theta}\right)\vec u_\phi,
\end{aligned}$$

$$\Delta V=\frac1r\frac{\partial^2(rV)}{\partial r^2}+
\frac1{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial V}{\partial\theta}\right)+
\frac1{r^2\sin^2\theta}\frac{\partial^2V}{\partial\phi^2}.$$

## Théorèmes

### Théorème d’Ostrogradsky–Green

$S$ étant une surface fermée, et $\tau$ le volume intérieur à $S$,

$$\oiint_S\vec A\cdot d\vec S=\iiint_\tau\operatorname{div}\vec A\,d\tau.$$

### Théorème de Stokes–Ampère

$C$ étant une courbe fermée bordant une surface $S$,

$$\oint_C\vec A\cdot d\vec\ell=\iint_S\operatorname{rot}\vec A\cdot d\vec S.$$

> Les parenthèses des dérivées de produits, notamment $\partial(rA_r)$, $\partial(r^2A_r)$ et $\partial^2(rV)$, explicitent la portée indiquée dans le formulaire. Les intégrales surfaciques et volumiques sont écrites avec leurs notations multiples usuelles.
