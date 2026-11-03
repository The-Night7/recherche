---
source: "PREING2-S2/Integration-proba/TD4-Correction_2021-2022_Integration-proba_P2S2_NArancibia.pdf"
pages: 73
transcription: manuelle
transcription_date: 2026-10-02
verification: lecture visuelle intégrale des 73 diapositives, comparaison avec le texte natif et vérification des formules
---

# TD Intégration et probabilités — Intégrales curvilignes — Corrigé

CY Tech, deuxième semestre 2021–2022.

Les énoncés, démonstrations et calculs des diapositives sont regroupés par exercice. Les titres et pieds de page répétés sont retirés. La source emploie trois fois « Exercice 6 » pour trois problèmes distincts : ils sont distingués ici par les lettres A, B et C. Les erreurs mathématiques repérées sont signalées dans des notes, à côté des expressions rectifiées.

## Exercice 1 — Forme exacte sur un demi-plan (pages 2 à 6)

On considère la forme différentielle de degré 1

$$
\omega=\frac{2x}{y}\,dx-\frac{x^2}{y^2}\,dy,
\qquad U=\{(x,y)\in\mathbb R^2:y>0\}.
$$

1. Montrer que $\omega$ est fermée sur $U$.
2. Montrer de deux façons différentes que $\omega$ est exacte.
3. Calculer $\int_C\omega$, où $C$ est une courbe $C^1$ par morceaux d’origine $A=(1,2)$ et d’extrémité $B=(3,8)$.

### 1. Fermeture

Posons $P(x,y)=2x/y$ et $Q(x,y)=-x^2/y^2$. Alors

$$\frac{\partial P}{\partial y}=-\frac{2x}{y^2}=\frac{\partial Q}{\partial x}.$$

Donc $\omega$ est fermée sur $U$.

### 2. Exactitude par calcul d’une primitive

Cherchons $f:U\to\mathbb R$ telle que $df=\omega$, c’est-à-dire

$$\frac{\partial f}{\partial x}=\frac{2x}{y},\qquad\frac{\partial f}{\partial y}=-\frac{x^2}{y^2}.$$

La première équation donne $f(x,y)=x^2/y+g(y)$, donc

$$\frac{\partial f}{\partial y}=-\frac{x^2}{y^2}+g'(y).$$

La deuxième impose $g'(y)=0$. Ainsi $g$ est constante et $f(x,y)=x^2/y$ est une primitive ; $\omega$ est exacte.

### 2. Exactitude par le théorème de Poincaré

La forme est fermée, et l’ouvert $U$ est étoilé : par exemple, pour $A=(0,1)$ et tout $P\in U$, le segment $[A,P]$ reste entièrement dans $U$. Le théorème de Poincaré donne l’exactitude.

### 3. Intégrale

L’intégrale d’une forme exacte ne dépend que des extrémités :

$$\int_C\omega=f(3,8)-f(1,2)=\frac98-\frac12=\frac58.$$

## Exercice 2 — Intégrales sur des cercles (pages 7 à 10)

1. Soit $\omega=x^2\,dx+y^2\,dy$. Calculer son intégrale le long de tout cercle du plan parcouru une fois dans le sens trigonométrique.
2. Soit $\omega=(y+z)\,dx+(z+x)\,dy+(x+y)\,dz$. Calculer son intégrale le long du cercle

$$C:\quad x^2+y^2+z^2=1,\qquad x+y+z=0.$$

### Solution

1. La forme est $C^1$ et fermée sur $\mathbb R^2$, puisque $\partial_y(x^2)=0=\partial_x(y^2)$. Comme $\mathbb R^2$ est étoilé, elle est exacte. Un cercle est une courbe fermée, donc l’intégrale vaut **zéro**.

2. Posons $P=y+z$, $Q=z+x$, $R=x+y$. On a

$$\partial_yP=1=\partial_xQ,\qquad\partial_zP=1=\partial_xR,\qquad\partial_zQ=1=\partial_yR.$$

La forme est donc fermée sur $\mathbb R^3$, ouvert étoilé ; elle y est exacte par Poincaré. Son intégrale sur le cercle fermé $C$ est **nulle**.

> **Erreur de la source, page 9.** Le corrigé qualifie le plan $x+y+z=0$ d’« ouvert étoilé ». Il n’est pas ouvert dans $\mathbb R^3$. On applique ici Poincaré à $\mathbb R^3$, où la forme est définie, puis on intègre sur $C$.

## Exercice 3 — Cercles et ellipses (pages 11 à 18)

Calculer $\int_\Gamma y^2\,dx+x^2\,dy$ pour les trois courbes suivantes :

1. $x^2+y^2-ay=0$.
2. $x^2/a^2+y^2/b^2-1=0$.
3. $x^2/a^2+y^2/b^2-2x/a-2y/b=0$.

> **Convention du corrigé :** les paramétrages ci-dessous sont parcourus pour $0\le t\le2\pi$. La présentation des demi-axes comme $a,b$ et du rayon comme $a/2$ suppose $a,b>0$ ; l’énoncé n’explicite pas cette hypothèse. Sans elle, le rayon géométrique est $|a|/2$ et les demi-axes sont des valeurs absolues. Les formules d’intégrales ci-dessous correspondent aux paramétrages indiqués.

### 1. Cercle décentré

On complète le carré :

$$x^2+y^2-ay=x^2+(y-a/2)^2-a^2/4.$$

Le cercle a pour centre $(0,a/2)$. On pose

$$x=\frac a2\cos t,\qquad y=\frac a2(1+\sin t),\qquad dx=-\frac a2\sin t\,dt,\quad dy=\frac a2\cos t\,dt.$$

Alors

$$
\begin{aligned}
\int_\Gamma y^2\,dx+x^2\,dy
&=\frac{a^3}8\int_0^{2\pi}\big(-(1+\sin t)^2\sin t+\cos^3t\big)\,dt\\
&=\frac{a^3}8\int_0^{2\pi}\big(-\sin^3t-2\sin^2t-\sin t+\cos^3t\big)\,dt\\
&=\frac{a^3}8\int_0^{2\pi}\big(-(1-\cos2t)-2\sin t+\cos^2t\sin t+\cos t-\sin^2t\cos t\big)\,dt\\
&=\frac{a^3}8\left[-t+\frac{\sin2t}2+2\cos t-\frac{\cos^3t}3+\sin t-\frac{\sin^3t}3\right]_0^{2\pi}\\
&=-\frac{\pi a^3}4.
\end{aligned}
$$

La source omet l’argument $t$ dans un terme $\cos^3t$ de la primitive (page 13).

### 2. Ellipse centrée à l’origine

On paramètre par $x=a\cos t$, $y=b\sin t$, donc $dx=-a\sin t\,dt$, $dy=b\cos t\,dt$.

$$
\begin{aligned}
\int_\Gamma y^2\,dx+x^2\,dy
&=\int_0^{2\pi}(-ab^2\sin^3t+a^2b\cos^3t)\,dt\\
&=\int_0^{2\pi}\big(-ab^2(\sin t-\cos^2t\sin t)+a^2b(\cos t-\sin^2t\cos t)\big)\,dt\\
&=\left[-ab^2\left(-\cos t+\frac{\cos^3t}3\right)+a^2b\left(\sin t-\frac{\sin^3t}3\right)\right]_0^{2\pi}=0.
\end{aligned}
$$

### 3. Ellipse translatée

On écrit

$$\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{2x}a-\frac{2y}b
=\left(\frac xa-1\right)^2+\left(\frac yb-1\right)^2-2.$$

Ainsi,

$$\left(\frac xa-1\right)^2+\left(\frac yb-1\right)^2=2.$$

> **Erreur de la source, page 16 :** le centre est $(a,b)$, et non $(1,1)$ dans les coordonnées $(x,y)$.

On pose $x=a(1+\sqrt2\cos t)$, $y=b(1+\sqrt2\sin t)$, d’où $dx=-a\sqrt2\sin t\,dt$ et $dy=b\sqrt2\cos t\,dt$. On obtient

$$
\begin{aligned}
\int_\Gamma y^2\,dx+x^2\,dy
&=\int_0^{2\pi}\big[-ab^2\sqrt2\sin t(1+\sqrt2\sin t)^2
+a^2b\sqrt2\cos t(1+\sqrt2\cos t)^2\big]dt\\
&=\int_0^{2\pi}\big[-ab^2\sqrt2(2\sin^3t+2\sqrt2\sin^2t+\sin t)\\
&\hspace{5em}+a^2b\sqrt2(2\cos^3t+2\sqrt2\cos^2t+\cos t)\big]dt\\
&=\int_0^{2\pi}\big[-ab^2\sqrt2(3\sin t-2\sin t\cos^2t+\sqrt2(1-\cos2t))\\
&\hspace{5em}+a^2b\sqrt2(3\cos t-2\cos t\sin^2t+\sqrt2(1+\cos2t))\big]dt.
\end{aligned}
$$

Une primitive de l’intégrande est

$$
\begin{aligned}
&-ab^2\sqrt2\left(-3\cos t+\frac{2\cos^3t}3+\sqrt2\left(t-\frac{\sin2t}2\right)\right)\\
&\quad+a^2b\sqrt2\left(3\sin t-\frac{2\sin^3t}3+\sqrt2\left(t+\frac{\sin2t}2\right)\right).
\end{aligned}
$$

Son évaluation de $0$ à $2\pi$ donne **$4\pi ab(a-b)$**.

## Exercice 4 — Chemin polygonal (pages 19 et 20)

Calculer $\int_\Gamma(xy^2+y)\,dx+x^2\,dy$, où $\Gamma$ est le chemin $ACB$ avec $A=(1,1)$, $C=(2,1)$ et $B=(2,2)$.

### Solution

On décompose l’intégrale sur $AC$ et $CB$. Sur $AC$, $y=1$ et $dy=0$ ; sur $CB$, $x=2$ et $dx=0$. Donc

$$
\begin{aligned}
\int_\Gamma(xy^2+y)\,dx+x^2\,dy
&=\int_1^2(x\cdot1^2+1)\,dx+\int_1^2 2^2\,dy\\
&=\left[\frac{x^2}2+x\right]_1^2+4[y]_1^2=\frac52+4=\frac{13}2.
\end{aligned}
$$

## Exercice 5 — Quart d’ellipse, deux méthodes (pages 21 à 28)

Calculer de deux façons

$$I=\iint_\Delta(2x^3-y)\,dx\,dy,\qquad
\Delta=\left\{(x,y)\in\mathbb R^2:x\ge0,\ y\ge0,\ \frac{x^2}{a^2}+\frac{y^2}{b^2}\le1\right\}.$$

On reprend la convention $a,b>0$ utilisée pour les axes et les bornes dans le corrigé.

### Première méthode — Changement de variables

Posons $x=ar\cos\theta$, $y=br\sin\theta$, avec $0\le r\le1$, $0\le\theta\le\pi/2$ et jacobien $abr$.

$$
\begin{aligned}
I&=\int_0^{\pi/2}\int_0^1(2a^3r^3\cos^3\theta-br\sin\theta)abr\,dr\,d\theta\\
&=\int_0^{\pi/2}\int_0^1(2a^4br^4\cos^3\theta-ab^2r^2\sin\theta)\,dr\,d\theta\\
&=\frac{2a^4b}5\int_0^{\pi/2}\cos^3\theta\,d\theta-\frac{ab^2}3\int_0^{\pi/2}\sin\theta\,d\theta\\
&=\frac{2a^4b}5\left([\sin\theta]_0^{\pi/2}-\left[\frac{\sin^3\theta}3\right]_0^{\pi/2}\right)
-\frac{ab^2}3[-\cos\theta]_0^{\pi/2}\\
&=\frac{4a^4b}{15}-\frac{ab^2}3.
\end{aligned}
$$

La source omet l’argument $\theta$ dans un terme $\sin^3\theta$ à la page 22.

### Deuxième méthode — Green–Riemann

Choisissons $Q(x,y)=x^4/2$ et $P(x,y)=y^2/2$, de sorte que $\partial_xQ-\partial_yP=2x^3-y$. Alors

$$I=\int_\Gamma\frac{y^2}2\,dx+\frac{x^4}2\,dy,$$

où $\Gamma$ est la frontière orientée positivement : $\Gamma_1$ est le segment de $(0,0)$ à $(a,0)$, $\Gamma_2$ le quart d’ellipse de $(a,0)$ à $(0,b)$, et $\Gamma_3$ le segment de $(0,b)$ à $(0,0)$.

Sur $\Gamma_1$, $y=0$ et $dy=0$ ; sur $\Gamma_3$, $x=0$ et $dx=0$. Les deux contributions sont nulles. Sur $\Gamma_2$, on pose $x=a\cos t$, $y=b\sin t$, $0\le t\le\pi/2$, donc

$$
\begin{aligned}
I&=\int_0^{\pi/2}\left(\frac{b^2}2\sin^2t(-a\sin t)+\frac{a^4}2\cos^4t(b\cos t)\right)dt\\
&=-\frac{ab^2}2\int_0^{\pi/2}\sin^3t\,dt+\frac{a^4b}2\int_0^{\pi/2}\cos^5t\,dt.
\end{aligned}
$$

Or

$$\int_0^{\pi/2}(1-\cos^2t)\sin t\,dt
=[-\cos t]_0^{\pi/2}-\left[-\frac{\cos^3t}3\right]_0^{\pi/2}=1-\frac13=\frac23.$$

Avec $u=\sin t$, $du=\cos t\,dt$,

$$\int(1-\sin^2t)^2\cos t\,dt=\int(1-2u^2+u^4)\,du
=u-\frac{2u^3}3+\frac{u^5}5.$$

L’intégrale entre $0$ et $\pi/2$ vaut donc $1-2/3+1/5=8/15$. Finalement,

$$I=-\frac{ab^2}2\frac23+\frac{a^4b}2\frac8{15}
=\frac{4a^4b}{15}-\frac{ab^2}3.$$

> **Coquille sans effet sur le résultat, page 25 :** dans le calcul de la contribution nulle de $\Gamma_3$, le PDF écrit $x^2/2$ au lieu de $y^2/2$ devant $dx=0$. Les différentielles $dt$ omises dans le paramétrage sont explicitées ici.

## Exercice 6 A — Courbe logarithmique (pages 29 à 31)

Calculer

$$\int_\Gamma\sqrt x\,dy-\sqrt x\ln(x+1)\,dx,
\qquad\Gamma=\{(x,y):0\le x\le1,\ y=(x-1)\ln(x+1)\}.$$

Le corrigé parcourt la courbe dans le sens des $x$ croissants.

### Solution

Sur $\Gamma$,

$$dy=\left(\ln(x+1)+\frac{x-1}{x+1}\right)dx.$$

Les termes logarithmiques s’annulent, donc

$$I=\int_0^1\sqrt x\,\frac{x-1}{x+1}\,dx.$$

Avec $u=\sqrt x$, $x=u^2$ et $dx=2u\,du$,

$$
\begin{aligned}
I&=2\int_0^1u^2\frac{u^2-1}{u^2+1}\,du
=2\int_0^1\left(u^2-\frac{2u^2}{u^2+1}\right)du\\
&=2\int_0^1\left(u^2-2+\frac2{u^2+1}\right)du\\
&=2\left[\frac{u^3}3-2u+2\arctan u\right]_0^1
=\frac23-4+4\arctan1=\pi-\frac{10}3.
\end{aligned}
$$

## Exercice 6 B — Boucle formée de deux paraboles (pages 32 à 35)

Calculer

$$I=\int_\Gamma(2xy-x^2)\,dx+(x+y^2)\,dy,$$

où $\Gamma$ est la boucle fermée constituée par $y=x^2$ et $x=y^2$, parcourue dans le sens direct. Vérifier avec Green–Riemann.

### Calcul direct

Les courbes se coupent en $(0,0)$ et $(1,1)$. Sur $\Gamma_1$, on suit $y=x^2$ de $x=0$ à $x=1$, donc $dy=2x\,dx$ :

$$
\begin{aligned}
\int_{\Gamma_1}\omega
&=\int_0^1\big(2x\cdot x^2-x^2+(x+x^4)2x\big)\,dx\\
&=\int_0^1(x^2+2x^3+2x^5)\,dx
=\left[\frac{x^3}3+\frac{x^4}2+\frac{x^6}3\right]_0^1=\frac76.
\end{aligned}
$$

Sur $\Gamma_2$, on suit $x=y^2$ de $y=1$ à $y=0$, donc $dx=2y\,dy$ :

$$
\begin{aligned}
\int_{\Gamma_2}\omega
&=\int_1^0\big((2y^3-y^4)2y+y^2+y^2\big)\,dy\\
&=\int_1^0(2y^2+4y^4-2y^5)\,dy
=\left[\frac{2y^3}3+\frac{4y^5}5-\frac{y^6}3\right]_1^0=-\frac{17}{15}.
\end{aligned}
$$

Donc $I=7/6-17/15=1/30$.

### Green–Riemann

On a $\partial_x(x+y^2)-\partial_y(2xy-x^2)=1-2x$. Le domaine intérieur est

$$D=\{(x,y):0\le x\le1,\ x^2\le y\le\sqrt x\}.$$

Ainsi

$$
\begin{aligned}
I&=\int_0^1\int_{x^2}^{\sqrt x}(1-2x)\,dy\,dx\\
&=\int_0^1(\sqrt x-2x\sqrt x-x^2+2x^3)\,dx\\
&=\left[\frac23x^{3/2}-\frac45x^{5/2}-\frac{x^3}3+\frac{x^4}2\right]_0^1
=\frac23-\frac45-\frac13+\frac12=\frac1{30}.
\end{aligned}
$$

## Exercice 6 C — Quart de disque (pages 36 à 39)

Calculer $\iint_D(x^2-y^2)\,dx\,dy$, avec

$$D=\{(x,y)\in\mathbb R^2:x\ge0,\ y\ge0,\ x^2+y^2\le R^2\}.$$

### Solution

Pour appliquer Green–Riemann, posons $Q=x^3/3$ et $P=y^3/3$, donc $\partial_xQ-\partial_yP=x^2-y^2$. Alors

$$\iint_D(x^2-y^2)\,dx\,dy=\int_\Gamma\frac{y^3}3\,dx+\frac{x^3}3\,dy.$$

La frontière positive est formée du segment $\Gamma_1$ sur l’axe $Ox$, de $(0,0)$ à $(R,0)$ ; du quart de cercle $\Gamma_2$ de $(R,0)$ à $(0,R)$ ; et du segment $\Gamma_3$ de $(0,R)$ à $(0,0)$. Les contributions des axes sont nulles : $y=dy=0$ sur $\Gamma_1$, $x=dx=0$ sur $\Gamma_3$.

Sur $\Gamma_2$, $x=R\cos t$, $y=R\sin t$, $0\le t\le\pi/2$, d’où

$$
\begin{aligned}
\iint_D(x^2-y^2)\,dx\,dy
&=\frac{R^4}3\int_0^{\pi/2}(\cos^4t-\sin^4t)\,dt\\
&=\frac{R^4}3\int_0^{\pi/2}(\cos^2t-\sin^2t)(\cos^2t+\sin^2t)\,dt\\
&=\frac{R^4}3\int_0^{\pi/2}\cos2t\,dt
=\frac{R^4}3\left[\frac{\sin2t}2\right]_0^{\pi/2}=0.
\end{aligned}
$$

## Exercice 7 — Extérieur du quart de disque dans le carré (pages 40 à 43)

Soit $D=\{(x,y):0<x<1,\ 0<y<1,\ x^2+y^2>1\}$. Calculer avec Green–Riemann

$$I=\iint_D\frac{xy}{(1+x^2+y^2)^2}\,dx\,dy.$$

### Solution

Posons $Q=0$ et $P=x/[2(1+x^2+y^2)]$. On a

$$\frac{\partial P}{\partial y}=-\frac{xy}{(1+x^2+y^2)^2},\qquad
I=\int_\Gamma\frac{x}{2(1+x^2+y^2)}\,dx.$$

La frontière positive se compose de $\Gamma_1$ : $x=1$, $y$ de $0$ à $1$ ; $\Gamma_2$ : $y=1$, $x$ de $1$ à $0$ ; et $\Gamma_3$ : l’arc unité de $(0,1)$ à $(1,0)$, parcouru avec $t$ de $\pi/2$ à $0$ dans $(\cos t,\sin t)$.

Sur $\Gamma_1$, $dx=0$, donc l’intégrale est nulle. Sur $\Gamma_2$,

$$\int_1^0\frac{x}{2(2+x^2)}\,dx
=\left[\frac14\ln(2+x^2)\right]_1^0=\frac14\ln\frac23.$$

Sur $\Gamma_3$,

$$\int_{\pi/2}^0\frac{\cos t}{2(1+\cos^2t+\sin^2t)}(-\sin t)\,dt
=\frac14\int_0^{\pi/2}\sin t\cos t\,dt
=\frac14\left[\frac{\sin^2t}2\right]_0^{\pi/2}=\frac18.$$

Finalement,

$$I=\frac14\ln\frac23+\frac18.$$

## Exercice 8 — Forme fermée non exacte (pages 44 à 46)

On considère

$$\omega=-\frac{y}{x^2+y^2}\,dx+\frac{x}{x^2+y^2}\,dy.$$

1. Sur quel domaine est-elle définie ?
2. Calculer son intégrale sur le cercle unité $C$ centré en $O$, parcouru dans le sens direct.
3. Est-elle exacte ?

### Solution

1. Puisque $x^2+y^2=0$ équivaut à $x=y=0$, le domaine est $\mathbb R^2\setminus\{(0,0)\}$.

2. Posons $x=\cos t$, $y=\sin t$, $0\le t\le2\pi$. Alors

$$\int_C\omega
=\int_0^{2\pi}\left(-\frac{\sin t(-\sin t)}{\sin^2t+\cos^2t}+\frac{\cos^2t}{\sin^2t+\cos^2t}\right)dt
=\int_0^{2\pi}1\,dt=2\pi.$$

3. Une forme exacte aurait une intégrale nulle sur toute courbe fermée. Comme l’intégrale vaut $2\pi$, $\omega$ n’est pas exacte. Elle est pourtant fermée, car

$$\frac{\partial}{\partial x}\left(\frac{x}{x^2+y^2}\right)
=\frac{y^2-x^2}{(x^2+y^2)^2}
=\frac{\partial}{\partial y}\left(-\frac{y}{x^2+y^2}\right).$$

Cet exemple montre que l’on ne peut pas supprimer sans précaution l’hypothèse de domaine étoilé du théorème de Poincaré : le plan privé de l’origine est un domaine troué et n’est pas étoilé.

## Exercice 9 — Fermeture, exactitude et primitive (pages 47 à 51)

Déterminer si les formes suivantes sont fermées et exactes ; dans le cas exact, donner une primitive :

1. $\omega=(x^2+3y)\,dx-y^3\,dy$.
2. $\omega=xy\,dx-z\,dy+xz\,dz$.
3. $\omega=x^3\,dx+y^3\,dy+z^3\,dz$.

**Rappel.** Pour une forme $C^1$ définie sur un ouvert étoilé, « exacte » équivaut à « fermée ». Dans tous les cas, « exacte » implique « fermée », donc une forme non fermée n’est pas exacte.

### 1. Première forme

$$\partial_y(x^2+3y)=3\ne0=\partial_x(-y^3).$$

La forme n’est pas fermée, donc n’est pas exacte.

### 2. Deuxième forme

$$\partial_z(xy)=0,\qquad\partial_x(xz)=z.$$

Ces fonctions ne sont pas identiques sur $\mathbb R^3$. La forme n’est donc ni fermée ni exacte.

### 3. Troisième forme

Les dérivées croisées sont toutes nulles :

$$\partial_z(x^3)=\partial_x(z^3)=0,\quad
\partial_x(y^3)=\partial_y(x^3)=0,\quad
\partial_y(z^3)=\partial_z(y^3)=0.$$

La forme est fermée sur $\mathbb R^3$, ouvert étoilé, donc exacte.

Par définition, une forme $\omega=A_1\,dx+A_2\,dy+A_3\,dz$ est exacte s’il existe $F\in C^1$ telle que $\partial_xF=A_1$, $\partial_yF=A_2$, $\partial_zF=A_3$. Ici,

$$\partial_xF=x^3\implies F=\frac{x^4}4+h(y,z).$$

Puis $\partial_yF=y^3$ impose $h(y,z)=y^4/4+g(z)$, et $\partial_zF=z^3$ impose $g(z)=z^4/4+C$. Une primitive est donc

$$F(x,y,z)=\frac{x^4}4+\frac{y^4}4+\frac{z^4}4.$$

## Exercice 10 — Facteur intégrant (pages 52 à 56)

Pour $a\in\mathbb R^*$, soit

$$\omega=(x^2+y^2-a^2)\,dx-2ay\,dy.$$

1. Prouver que $\omega$ n’est pas exacte.
2. Pour $f\in C^1(\mathbb R,\mathbb R)$, on pose $\alpha(x,y)=f(x)\omega(x,y)$. Quelle condition doit vérifier $f$ pour que $\alpha$ soit exacte ? Est-elle suffisante ? Donner une fonction qui la satisfait.
3. Calculer une primitive de $\alpha$ sur $\mathbb R^2$.
4. Calculer $\int_\Gamma\alpha$ sur le cercle de centre $(0,0)$ et de rayon $R$.

### 1. Non-exactitude

On a $\partial_y(x^2+y^2-a^2)=2y$ et $\partial_x(-2ay)=0$. Ces fonctions ne sont pas identiques sur $\mathbb R^2$ : $\omega$ n’est pas fermée, donc pas exacte.

### 2. Condition sur $f$

La forme $\alpha$ est $C^1$ sur $\mathbb R^2$, ouvert étoilé. Donc

$$
\begin{aligned}
\alpha\text{ exacte}
&\iff\alpha\text{ fermée}\\
&\iff\partial_y\big(f(x)(x^2+y^2-a^2)\big)=\partial_x\big(-2ayf(x)\big)\\
&\iff 2yf(x)=-2ayf'(x)\quad\text{pour tous }x,y\\
&\iff f'(x)=-\frac{f(x)}a\quad\text{pour tout }x.
\end{aligned}
$$

Les solutions sont $f(x)=Ce^{-x/a}$, avec $C\in\mathbb R$. On peut prendre $f(x)=e^{-x/a}$.

> **Erreur de la source, page 54 :** la solution générale est imprimée $e^{-x/a}+\mathrm{cte}$. La constante est multiplicative, pas additive. Le choix particulier $e^{-x/a}$ fait ensuite dans le PDF est correct.

### 3. Primitive pour $f(x)=e^{-x/a}$

On cherche $F$ telle que

$$\partial_xF=e^{-x/a}(x^2+y^2-a^2),\qquad\partial_yF=-2aye^{-x/a}.$$

La seconde équation donne $F(x,y)=-ay^2e^{-x/a}+h(x)$. En dérivant par rapport à $x$,

$$y^2e^{-x/a}+h'(x)=e^{-x/a}(x^2+y^2-a^2),$$

d’où $h'(x)=e^{-x/a}(x^2-a^2)$. En intégrant, comme le demande le corrigé,

$$h(x)=(-ax^2-2a^2x-a^3)e^{-x/a}+C.$$

Ainsi,

$$F(x,y)=(-ax^2-2a^2x-ay^2-a^3)e^{-x/a}+C.$$

> **Erreur de la source, page 55 :** la dernière ligne donne $(-ax^2-2a^2x-ay e^{-x/a}-a^3)e^{-x/a}+\mathrm{cte}$. Le terme correct à l’intérieur de la parenthèse est $-ay^2$, conformément à la ligne précédente et à la vérification de $\partial_yF$.

### 4. Intégrale sur le cercle

La forme $\alpha$ est exacte et $\Gamma$ est fermée : **$\int_\Gamma\alpha=0$**.

## Exercice 11 — Calculs d’aires avec Green–Riemann (pages 57 à 62)

Calculer avec la formule de Green :

1. L’aire de $x^2/a^2+y^2/b^2\le1$.
2. L’aire du domaine délimité par les axes $Ox$, $Oy$ et $x=a\cos^3t$, $y=a\sin^3t$, $0\le t\le\pi/2$.

Les axes $a,b$ sont pris positifs dans le corrigé.

### 1. Ellipse

L’aire vaut $\iint_D1\,dx\,dy$. Choisissons $P=-y/2$ et $Q=x/2$, puisque $\partial_xQ-\partial_yP=1/2-(-1/2)=1$. Alors

$$\operatorname{Aire}(D)=\frac12\int_\Gamma(-y\,dx+x\,dy).$$

Avec $x=a\cos t$, $y=b\sin t$, $0\le t\le2\pi$,

$$\operatorname{Aire}(D)=\frac12\int_0^{2\pi}ab(\sin^2t+\cos^2t)\,dt
=\frac12\int_0^{2\pi}ab\,dt=\pi ab.$$

### 2. Quart d’astroïde

On utilise encore $\operatorname{Aire}(D)=\frac12\int_\Gamma(-y\,dx+x\,dy)$. La frontière comporte l’arc $\Gamma_1$ paramétré par $(a\cos^3t,a\sin^3t)$, le segment $\Gamma_2$ sur $Ox$ et le segment $\Gamma_3$ sur $Oy$.

Les contributions des deux segments sont nulles : sur $Ox$, $y=dy=0$ ; sur $Oy$, $x=dx=0$. Sur l’arc, $dx=-3a\sin t\cos^2t\,dt$ et $dy=3a\cos t\sin^2t\,dt$. Donc

$$
\begin{aligned}
\operatorname{Aire}(D)
&=\frac12\int_0^{\pi/2}\big(-a\sin^3t(-3a\sin t\cos^2t)+a\cos^3t(3a\cos t\sin^2t)\big)dt\\
&=\frac{3a^2}2\int_0^{\pi/2}(\sin^4t\cos^2t+\cos^4t\sin^2t)\,dt\\
&=\frac{3a^2}2\int_0^{\pi/2}\sin^2t\cos^2t(\sin^2t+\cos^2t)\,dt\\
&=\frac{3a^2}8\int_0^{\pi/2}\sin^2(2t)\,dt\\
&=\frac{3a^2}8\int_0^{\pi/2}\left(1-\frac{1+\cos4t}2\right)dt\\
&=\frac{3a^2}{16}\int_0^{\pi/2}(1-\cos4t)\,dt
=\frac{3\pi a^2}{32}.
\end{aligned}
$$

## Exercice 12 — Intégrale de Dirichlet (pages 63 à 73)

Soient $0<r<R$ et

$$\omega=\frac{e^{-y}}{x^2+y^2}\big((x\sin x-y\cos x)\,dx+(x\cos x+y\sin x)\,dy\big).$$

1. Calculer son intégrale sur le contour $\Gamma=\Gamma_1\cup\Gamma_2\cup\Gamma_3\cup\Gamma_4$, orienté dans le sens direct autour du demi-anneau supérieur.
2. En déduire une expression de $\int_r^R\sin x/x\,dx$ en fonction d’autres intégrales.
3. Faire tendre $r$ vers $0$ et $R$ vers $+\infty$ pour déterminer $\int_0^{+\infty}\sin x/x\,dx$.

On suit la numérotation des arcs employée dans les calculs des pages 66 à 69 :

- $\Gamma_1$ : $(t,0)$, de $t=r$ à $t=R$.
- $\Gamma_2$ : $(R\cos t,R\sin t)$, de $t=0$ à $t=\pi$.
- $\Gamma_3$ : $(t,0)$, de $t=-R$ à $t=-r$.
- $\Gamma_4$ : $(r\cos t,r\sin t)$, de $t=\pi$ à $t=0$.

> **Incohérence de la source :** l’énoncé de la page 63 attribue le rayon $r$ à $\Gamma_2$ et $R$ à $\Gamma_4$, tandis que la résolution fait l’inverse. Le contour géométrique est le même ; la numérotation est uniformisée ici selon la résolution. L’arc intérieur est parcouru dans le sens horaire.

### 1. Fermeture et exactitude sur un domaine adapté

La forme est $C^1$ sur $\mathbb R^2\setminus\{(0,0)\}$. Posons

$$P(x,y)=\frac{e^{-y}(x\sin x-y\cos x)}{x^2+y^2},\qquad Q(x,y)=\frac{e^{-y}(x\cos x+y\sin x)}{x^2+y^2}.$$

En dérivant,

$$
\begin{aligned}
\frac{\partial Q}{\partial x}
&=-\frac{2xe^{-y}}{(x^2+y^2)^2}(x\cos x+y\sin x)
+\frac{e^{-y}}{x^2+y^2}(-x\sin x+\cos x+y\cos x)\\
&=\frac{e^{-y}}{(x^2+y^2)^2}\big[-2x(x\cos x+y\sin x)\\
&\hspace{7em}+(x^2+y^2)(-x\sin x+\cos x+y\cos x)\big]\\
&=\frac{e^{-y}}{(x^2+y^2)^2}\big[(-x^2+y^2+x^2y+y^3)\cos x+(-2xy-x^3-xy^2)\sin x\big].
\end{aligned}
$$

De même,

$$
\begin{aligned}
\frac{\partial P}{\partial y}
&=-\frac{2ye^{-y}}{(x^2+y^2)^2}(x\sin x-y\cos x)
+\frac{e^{-y}}{x^2+y^2}(-x\sin x+y\cos x-\cos x)\\
&=\frac{e^{-y}}{(x^2+y^2)^2}\big[-(x^2+y^2)(x\sin x-y\cos x)\\
&\hspace{7em}-2y(x\sin x-y\cos x)-(x^2+y^2)\cos x\big]\\
&=\frac{e^{-y}}{(x^2+y^2)^2}\big[(-x^2+y^2+x^2y+y^3)\cos x+(-2xy-x^3-xy^2)\sin x\big].
\end{aligned}
$$

Donc $\partial_xQ=\partial_yP$ et $\omega$ est fermée.

> **Coquilles des pages 64 et 65 :** dans la première ligne de chaque dérivée, le dénominateur du terme venant de la dérivation de $1/(x^2+y^2)$ doit être $(x^2+y^2)^2$. À la page 65, le terme provenant de la dérivation de $e^{-y}$ porte aussi un signe erroné dans la première ligne. Les développements finaux du PDF et l’égalité des dérivées sont corrects ; les lignes intermédiaires sont rectifiées ci-dessus.

On choisit

$$\Omega=\mathbb R^2\setminus\{(0,y):y\le0\}.$$

Cet ouvert est étoilé par rapport à tout point $(0,y_0)$ avec $y_0>0$, et contient tout le contour $\Gamma$. Par Poincaré, $\omega$ est exacte sur $\Omega$. Comme $\Gamma$ est fermée,

$$\int_\Gamma\omega=0.$$

### 2. Calcul sur les quatre morceaux

Sur $\Gamma_1$, $y=0$ et $dy=0$, donc

$$\int_{\Gamma_1}\omega=\int_r^R\frac{\sin t}t\,dt.$$

Sur $\Gamma_3$, le changement de variable $u=-t$ donne

$$\int_{\Gamma_3}\omega=\int_{-R}^{-r}\frac{\sin t}t\,dt
=-\int_R^r\frac{\sin u}u\,du=\int_r^R\frac{\sin u}u\,du.$$

Ainsi,

$$0=2\int_r^R\frac{\sin t}t\,dt+\int_{\Gamma_2}\omega+\int_{\Gamma_4}\omega.$$

Sur $\Gamma_2$, substituons $x=R\cos t$, $y=R\sin t$. Les termes contenant $\sin(R\cos t)$ s’annulent et il reste

$$
\begin{aligned}
\int_{\Gamma_2}\omega
&=\int_0^\pi e^{-R\sin t}(\sin^2t+\cos^2t)\cos(R\cos t)\,dt\\
&=\int_0^\pi e^{-R\sin t}\cos(R\cos t)\,dt.
\end{aligned}
$$

De même, en tenant compte de l’orientation de $\Gamma_4$,

$$\int_{\Gamma_4}\omega=\int_\pi^0e^{-r\sin t}\cos(r\cos t)\,dt
=-\int_0^\pi e^{-r\sin t}\cos(r\cos t)\,dt.$$

Donc

$$\int_r^R\frac{\sin t}t\,dt
=\frac12\left(\int_0^\pi e^{-r\sin t}\cos(r\cos t)\,dt
-\int_0^\pi e^{-R\sin t}\cos(R\cos t)\,dt\right).$$

> **Coquilles des pages 66 et 68 :** le calcul sur le segment $\Gamma_1$ est noté $\Gamma_2$ dans une ligne de la page 66. La substitution détaillée sur l’arc de rayon $R$ mélange $r$ et $R$ et permute des sinus et cosinus ; le résultat simplifié reproduit ci-dessus est correct.

### 3. Passage aux limites

Pour $R>0$, en utilisant $|\cos(R\cos t)|\le1$, la symétrie du sinus autour de $\pi/2$ et $\sin t\ge2t/\pi$ sur $[0,\pi/2]$,

$$
\begin{aligned}
\left|\int_0^\pi e^{-R\sin t}\cos(R\cos t)\,dt\right|
&\le\int_0^\pi e^{-R\sin t}\,dt\\
&=2\int_0^{\pi/2}e^{-R\sin t}\,dt\\
&\le2\int_0^{\pi/2}e^{-2Rt/\pi}\,dt
=\frac\pi R(1-e^{-R})\le\frac\pi R.
\end{aligned}
$$

> **Coquille de la source, page 70 :** le PDF évalue la dernière intégrale en $\frac\pi R(1-e^{-2R})$. La valeur est $\frac\pi R(1-e^{-R})$ ; la majoration finale $\pi/R$ reste valable.

Par encadrement, l’intégrale sur l’arc extérieur tend vers $0$. Pour tout $r>0$, l’intégrale impropre existe et

$$\int_r^{+\infty}\frac{\sin t}t\,dt=\frac12\int_0^\pi e^{-r\sin t}\cos(r\cos t)\,dt.$$

Pour la limite $r\to0^+$, considérons $f(r,t)=e^{-r\sin t}\cos(r\cos t)$ sur $[0,+\infty[\times[0,\pi]$. Pour chaque $r$, elle est continue en $t$ ; pour chaque $t$, elle est continue en $r$ ; et $|f(r,t)|\le1$, majorant intégrable sur $[0,\pi]$. Le théorème de continuité des intégrales à paramètre permet de passer la limite sous l’intégrale. Finalement,

$$
\begin{aligned}
\int_0^{+\infty}\frac{\sin t}t\,dt
&=\lim_{r\to0^+}\int_r^{+\infty}\frac{\sin t}t\,dt\\
&=\frac12\int_0^\pi\lim_{r\to0^+}e^{-r\sin t}\cos(r\cos t)\,dt\\
&=\frac12\int_0^\pi1\,dt=\frac\pi2.
\end{aligned}
$$

**Précision sur la page 72.** Le PDF dit « continue par morceaux » pour la dépendance en $r$ ; la fonction affichée est en réalité continue, ce qui justifie le théorème de continuité utilisé. Le symbole $F(r,t)$ de la majoration désigne la même fonction $f(r,t)$.
