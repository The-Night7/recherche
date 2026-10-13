# Mécanique du point — Résumé 5 : travail et énergie

> Source : `PREING1-S2/Mecanique-du-point/CM5_2013-2014_Mecanique-du-point_P1S2_DPhysique.pdf`, 3 pages.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif et restitution des formules. Les précisions ajoutées aux affirmations du document sont signalées.

## Travail d’une force (page 1)

Pour un déplacement élémentaire $d\overrightarrow{OM}$ :

$$\delta W_{\vec F}=\vec F\cdot d\overrightarrow{OM}=\vec F\cdot\vec v\,dt.$$

En coordonnées cartésiennes, $\delta W_{\vec F}=F_x\,dx+F_y\,dy+F_z\,dz$. Pour un déplacement de $A$ à $B$ le long d’un chemin $\Gamma$ :

$$W_{\vec F,A\to B}=\int_A^B\delta W_{\vec F}=\int_A^B\vec F\cdot d\overrightarrow{OM},$$

l’intégrale étant prise le long de $\Gamma$. Le travail est une énergie et s’exprime en joules (J). Si $W>0$, il est moteur ; si $W<0$, il est résistant.

Les forces perpendiculaires à $\vec v$ ne travaillent pas. Le cours en déduit que la réaction normale $\vec N$ ne travaille pas, et que le frottement dynamique travaille toujours de manière résistante puisqu’il est dirigé selon $-\vec v$.

**Précision.** Ces deux conclusions sont formulées pour un support fixe dans le référentiel considéré. Sur un support mobile, il faut examiner la vitesse du point d’application et distinguer la vitesse du corps de sa vitesse de glissement relative au support.

## Puissance d’une force (page 1)

Puissance moyenne :

$$\mathcal P_{\mathrm{moy}}=\frac{W_{\vec F,A\to B}}{t_B-t_A}=\frac{W_{\vec F}}{\Delta t}.$$

Puissance instantanée :

$$\mathcal P_{\vec F}=\frac{\delta W_{\vec F}}{dt}=\vec F\cdot\vec v.$$

La puissance est une énergie divisée par un temps et s’exprime en watts (W). Inversement :

$$W_{\vec F,A\to B}=\int_{t_A}^{t_B}\mathcal P_{\vec F}(t)\,dt.$$

## Théorème de l’énergie cinétique (page 1)

L’énergie cinétique d’un point matériel de masse $m$ est $E_c=\frac12mv^2$. Dans un référentiel galiléen :

$$\Delta E_c=E_c(B)-E_c(A)=\sum W_{A\to B},\qquad\frac{dE_c}{dt}=\sum\mathcal P.$$

Les sommes portent sur les travaux et les puissances de toutes les forces appliquées au corps. Toujours préciser l’état initial et l’état final lors de l’application du théorème.

## Énergie potentielle (page 2)

La force $\vec F$ dérive d’une énergie potentielle s’il existe une fonction $E_p(M)$ telle que :

$$\delta W_{\vec F}=-dE_p.$$

L’énergie potentielle est définie à une constante additive près, choisie nulle par convention dans le cours.

- Pesanteur : $E_p=mgz$, avec l’axe $z$ orienté vers le haut.
- Ressort : $E_p=\frac12k(\ell-\ell_0)^2$.

## Forces conservatives et non conservatives (page 2)

Une force conservative dérive d’une énergie potentielle. Son travail vérifie :

$$W_{\vec F,A\to B}=-\Delta E_p=E_p(A)-E_p(B).$$

Le caractère conservatif équivaut à l’indépendance du travail par rapport au chemin suivi entre les deux points. Le poids et la force élastique du ressort sont conservatifs.

Un système est dit conservatif s’il subit uniquement des forces conservatives ou des forces qui ne travaillent pas.

Une force non conservative ne dérive pas d’une énergie potentielle ; son travail dépend du chemin. Les forces de frottement sont non conservatives.

## Théorème de l’énergie mécanique (page 2)

L’énergie mécanique est :

$$E_m=E_c+E_p,$$

où $E_p$ est la somme des énergies potentielles associées aux forces conservatives. Elle est définie à une constante additive près, choisie nulle par convention.

Dans un référentiel galiléen :

$$\Delta E_m=E_m(B)-E_m(A)=\sum W_{\mathrm{n.c.},A\to B},\qquad\frac{dE_m}{dt}=\sum\mathcal P_{\mathrm{n.c.}}.$$

Les sommes portent sur les travaux et puissances des forces non conservatives agissant pendant le déplacement. Pour un système conservatif :

$$\sum W_{\mathrm{n.c.}}=0\quad\Longrightarrow\quad E_m=\text{constante}.$$

Toujours préciser les états initial et final, répertorier les forces conservatives avec leur énergie potentielle et les éventuelles forces non conservatives.

## Positions d’équilibre et stabilité (page 3)

Une position d’équilibre vérifie $\sum\vec F=\vec0$. Le cours qualifie l’équilibre de stable si le corps, légèrement écarté, y revient ; il le qualifie d’instable si le corps s’en éloigne.

**Précision.** Dans un système conservatif, la stabilité ne signifie pas nécessairement un retour définitif au repos : le corps peut osciller au voisinage de l’équilibre.

## Système conservatif à un degré de liberté (page 3)

Pour un degré de liberté $x$, la force résultante est $\vec F(x)=F(x)\vec u_x$ avec :

$$F(x)=-\frac{dE_p}{dx},\qquad E_m(x)=E_c(x)+E_p(x)=\text{constante}.$$

Les minima de $E_p(x)$ correspondent aux équilibres stables et les maxima aux équilibres instables. Les positions accessibles vérifient $E_c(x)\geq0$, donc $E_p(x)\leq E_m$.

Le signe de la pente de $E_p$ détermine le sens de la force, opposé à cette pente puisque $F=-dE_p/dx$.

Les points de rebroussement vérifient $\vec v=\vec0$, soit $E_p(x)=E_m$ ; le corps repart dans le sens de $\vec F$. **Précision :** ce dernier énoncé concerne un point de rebroussement où la force n’est pas nulle, et non une position d’équilibre.
