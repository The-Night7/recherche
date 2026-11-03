---
source: "PREING2-S1/Analyse-dans-RN-DS/DS3-2021-2022-Correction_Analyse-dans-RN-DS_P2S1_Inconnu.pdf"
pages: 10
transcription: manuelle, depuis les pages manuscrites et énoncés imprimés
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 10 pages ; énoncés, calculs et barèmes transcrits, divergences entre énoncé et correction signalées
---

# Analyse dans Rn — DS3 2021–2022 : correction manuscrite

## Page 1

### Correction du DS3 — Analyse dans Rn (2021–2022)

Le barème manuscrit totalise $22=3+4+6+9$ points.

### Exercice 1 — Résoudre le système (3 points)

$$\begin{cases}\partial_xf=\tfrac12y^2+2xy+e^x+\sin(2x),\\\partial_yf=y^2+xy+x^2.\end{cases}$$
Les dérivées croisées des membres de droite valent toutes deux $y+2x$ (0,5 point). En intégrant la seconde équation par rapport à $y$,
$$f(x,y)=\frac12xy^2+\frac13y^3+x^2y+K(x),$$
où $K$ est de classe $C^1$ (1 point). En dérivant en $x$ et en comparant à la première équation,
$$\frac12y^2+2xy+K'(x)=\frac12y^2+2xy+e^x+\sin(2x),$$
donc $K'(x)=e^x+\sin(2x)$ (1 point).

## Page 2

**Exercice 1 — solution.** $K(x)=e^x-\tfrac12\cos(2x)+C$, $C\in\mathbb R$, d’où
$$f(x,y)=\frac12xy^2+\frac13y^3+x^2y+e^x-\frac12\cos(2x)+C$$
(0,5 point).

### Exercice 2 — Changement de variables (4 points)

Soit $D=\{(x,y)\in\mathbb R^2:y\ne0,\ y\ne x\}$. Trouver les fonctions $f\in C^1(D)$ vérifiant
$$x\partial_xf+y\partial_yf=(x+y)^2,$$
avec le changement $(u,v)=(x/y,x-y)$.

L’application $\varphi(x,y)=(x/y,x-y)$ est de classe $C^1$ sur $D$. Les équations $x=uy$, $x-y=v$ donnent
$$y=\frac v{u-1},\qquad x=\frac{uv}{u-1}.$$
Donc
$$\varphi(D)=Z=\{(u,v):u\ne1,\ v\ne0\},\qquad\varphi^{-1}(u,v)=\left(\frac{uv}{u-1},\frac v{u-1}\right).$$
L’inverse est de classe $C^1$ sur $Z$ : $\varphi$ est un $C^1$-difféomorphisme (1 point).

## Page 3

**Exercice 2 — résolution.** Posons $f(x,y)=g(u,v)$. La chaîne donne
$$\partial_xf=\frac1y g_u+g_v,\qquad\partial_yf=-\frac{x}{y^2}g_u-g_v$$
(1 point). En substituant,
$$x\partial_xf+y\partial_yf=(x-y)g_v=vg_v=(x+y)^2=v^2\left(\frac{u+1}{u-1}\right)^2.$$
Comme $v\ne0$,
$$g_v=\left(\frac{u+1}{u-1}\right)^2v,$$
puis
$$g(u,v)=\frac12\left(\frac{u+1}{u-1}\right)^2v^2+h(u)$$
(1 point). Le corrigé conclut
$$f(x,y)=\frac{(x+y)^2}{2}+h(x/y)\quad(1\text{ point}).$$

**Précision sur le domaine.** Le manuscrit demande $h\in C^1(\mathbb R)$, ce qui donne des solutions mais ne les décrit pas toutes sur $D$. Le domaine transformé est séparé par $u=1$ et $v=0$ : on peut choisir indépendamment une fonction $h_+\in C^1(\mathbb R\setminus\{1\})$ pour $v>0$ et $h_-\in C^1(\mathbb R\setminus\{1\})$ pour $v<0$. Aucun raccord au travers des droites exclues n’est imposé.

## Page 4

### Exercice 3 — Continuité et dérivée seconde (6 points)

$$f(x,y)=\begin{cases}\dfrac{(x+y)^4}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$
1. Montrer que $f$ est continue sur $\mathbb R^2$ (1,5 point).
2. Calculer $\partial_xf$ et $\partial_{xx}f$ sur $\mathbb R^2$ et en déduire que $f$ n’est pas de classe $C^2$ (4,5 points).

**1.** Hors de l’origine, la fraction est de classe $C^\infty$. En polaires,
$$f(r\cos\theta,r\sin\theta)=r^2(\cos\theta+\sin\theta)^4\to0=f(0,0).$$
Le facteur angulaire est borné par $4$, ce qui justifie la limite pour toutes les approches, au-delà de l’angle fixe écrit dans le manuscrit. Donc $f$ est continue sur $\mathbb R^2$ (1,5 point).

**2.** Hors de zéro,
$$\partial_xf=\frac{4(x+y)^3}{x^2+y^2}-\frac{2x(x+y)^4}{(x^2+y^2)^2}.$$

## Page 5

**Exercice 3 — dérivée première en zéro.**
$$\partial_xf(0,0)=\lim_{t\to0}\frac{f(t,0)-f(0,0)}t=\lim_{t\to0}t=0.$$
Ainsi la formule de la page précédente est prolongée par zéro à l’origine (1 point).

**Dérivée seconde hors de zéro.** En dérivant les deux termes puis en regroupant,
$$\partial_{xx}f(x,y)=\frac{12(x+y)^2}{x^2+y^2}-\frac{16x(x+y)^3}{(x^2+y^2)^2}-\frac{2(x+y)^4}{(x^2+y^2)^2}+\frac{8x^2(x+y)^4}{(x^2+y^2)^3}.$$

## Page 6

**Exercice 3 — dérivée seconde à l’origine.** Comme $\partial_xf(t,0)=2t$,
$$\partial_{xx}f(0,0)=\lim_{t\to0}\frac{2t-0}t=2$$
(1,5 point).

**Continuité de la dérivée seconde.** En posant $c=\cos\theta$, $s=\sin\theta$, la formule hors de zéro devient
$$12(c+s)^2-16c(c+s)^3-2(c+s)^4+8c^2(c+s)^4,$$
indépendante du rayon. Pour $\theta=0$, sa valeur est $12-16-2+8=2$. Le manuscrit donne ensuite la valeur $34$ pour $\theta=\pi$.

**Correction du second angle :** pour $\theta=\pi$, $c=-1$, $s=0$ et la valeur est encore $2$, pas $34$. En revanche, pour $\theta=\pi/2$, la formule vaut $12-2=10$. Les limites sur l’axe horizontal et l’axe vertical diffèrent : la dérivée seconde n’a pas de limite à l’origine.

## Page 7

**Exercice 3 — conclusion.** $\partial_{xx}f$ n’est pas continue à l’origine ; $f$ n’est donc pas de classe $C^2$ sur $\mathbb R^2$ (2 points).

### Exercice 4 — Changement de variables linéaire (9 points)

Pour $a\in\mathbb R\setminus\{0,2,-2\}$, on définit
$$\varphi(x,y)=(x+2y,x-ay)=(u,v),\qquad f=g\circ\varphi.$$
1. Trouver $\varphi^{-1}$.
2. Exprimer $g_u,g_v,g_{uu},g_{uv}$ en fonction des dérivées de $f$, en utilisant les variables $x,y$.
3. Trouver $f\in C^2(\mathbb R^2)$ vérifiant l’équation **imprimée**
$$a f_{xx}+(2-a)f_{xy}-f_{yy}=(a+2)^3(x+y).$$

**1.** Le déterminant de $\begin{pmatrix}1&2\\1&-a\end{pmatrix}$ est $-(a+2)\ne0$. En combinant les équations,
$$au+2v=(a+2)x,\qquad u-v=(a+2)y,$$
donc
$$\varphi^{-1}(u,v)=\left(\frac{au+2v}{a+2},\frac{u-v}{a+2}\right)$$
(1 point).

**Incohérence de l’énoncé et du corrigé :** la suite manuscrite traite $2a f_{xx}$ au lieu du terme $a f_{xx}$ imprimé. Ces deux équations sont distinctes ; cette modification est signalée dans la suite.

## Page 8

**Exercice 4 — 2, dérivées par la chaîne.** Le manuscrit calcule les dérivées de $f$ à partir de celles de $g$ :
$$f_x=g_u+g_v,\qquad f_y=2g_u-ag_v,$$
$$f_{xx}=g_{uu}+2g_{uv}+g_{vv},$$
$$f_{yy}=4g_{uu}-4ag_{uv}+a^2g_{vv},$$
$$f_{xy}=2g_{uu}+(2-a)g_{uv}-ag_{vv}.$$
Chaque groupe de calculs est annoté sur 1 point.

**Formules dans le sens demandé par la question imprimée**, obtenues à l’aide de l’inverse :
$$g_u=\frac{af_x+f_y}{a+2},\qquad g_v=\frac{2f_x-f_y}{a+2},$$
$$g_{uu}=\frac{a^2f_{xx}+2af_{xy}+f_{yy}}{(a+2)^2},\qquad g_{uv}=\frac{2af_{xx}+(2-a)f_{xy}-f_{yy}}{(a+2)^2}.$$
Les dérivées de $g$ sont évaluées en $(u,v)=\varphi(x,y)$ et celles de $f$ en $(x,y)$.

La dernière ligne manuscrite pose l’équation modifiée
$$2af_{xx}+(2-a)f_{xy}-f_{yy}=(a+2)^3(x+y).$$

## Page 9

**Exercice 4 — 3, résolution de l’équation manuscrite avec $2a$.** En substituant les expressions de la page précédente, les coefficients de $g_{uu}$ et $g_{vv}$ s’annulent. Celui de $g_{uv}$ vaut
$$4a+(2-a)^2+4a=(a+2)^2.$$
Donc
$$(a+2)^2g_{uv}=(a+2)^3(x+y),$$
puis
$$g_{uv}=(a+2)(x+y)=(a+1)u+v$$
(1 point pour la simplification, 1 pour la transformation du second membre).

**Pour l’équation imprimée avec $a$**, le calcul donnerait au contraire
$$-a g_{uu}+(a^2+2a+4)g_{uv}-a g_{vv}=(a+2)^2((a+1)u+v).$$
La réduction à une seule dérivée mixte n’est donc pas valide pour cette version.

## Page 10

**Exercice 4 — 3, intégration de l’équation avec $2a$.** De $g_{uv}=(a+1)u+v$, on obtient
$$g_u=(a+1)uv+\frac12v^2+h(u),$$
puis
$$g(u,v)=\frac{a+1}{2}u^2v+\frac12uv^2+H(u)+K(v),$$
où $H$ et $K$ sont de classe $C^2$ (1 point). En revenant à $x,y$,
$$f(x,y)=\frac{a+2}{2}(x+2y)(x-ay)(x+y)+H(x+2y)+K(x-ay)$$
(1 point).

**Portée de cette solution :** cette famille résout l’équation manuscrite avec le coefficient $2a$ devant $f_{xx}$. Elle ne constitue pas la solution générale de l’équation imprimée avec le coefficient $a$. Le document source ne résout pas cette dernière version.
