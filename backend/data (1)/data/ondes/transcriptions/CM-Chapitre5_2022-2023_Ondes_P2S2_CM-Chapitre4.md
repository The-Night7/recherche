---
source: "PREING2-S2/Ondes/CM-Chapitre5_2022-2023_Ondes_P2S2_CM-Chapitre4.pdf"
pages: 13
transcription: manuelle
transcription_date: 2026-10-04
verification: lecture visuelle des treize pages ; formules vérifiées ; erreurs et figures absentes signalées
---

# Chapitre 5 — Ondes en dimension 2 et 3

## Section 5.1 — Ondes scalaires ; dimension 2 (page 1)

Les vibrations d’une peau de tambour sont décrites par l’équation :

$$
\frac1{c^2}\frac{\partial^2F(x,y,t)}{\partial t^2}
-\frac{\partial^2F(x,y,t)}{\partial x^2}
-\frac{\partial^2F(x,y,t)}{\partial y^2}=0,
\qquad c^2=\frac{N}{\rho h}.
$$

$\rho$ est la densité de masse de la membrane, $h$ son épaisseur et $N$ la tension dans la membrane.

## Solutions progressives (pages 2 et 3)

Pour toute fonction $F(z)$ deux fois dérivable, en évaluant $F'$ et $F''$ en $ct-\alpha x-\beta y$ :

$$
\begin{aligned}
\partial_tF(ct-\alpha x-\beta y)&=cF',&\partial_t^2F(ct-\alpha x-\beta y)&=c^2F'',\\
\partial_xF(ct-\alpha x-\beta y)&=-\alpha F',&\partial_x^2F(ct-\alpha x-\beta y)&=\alpha^2F'',\\
\partial_yF(ct-\alpha x-\beta y)&=-\beta F',&\partial_y^2F(ct-\alpha x-\beta y)&=\beta^2F''.
\end{aligned}
$$

L’équation d’onde devient $(1-\alpha^2-\beta^2)F''=0$. Pour tout vecteur $\vec k=(k_x,k_y)$ de norme 1 et toute fonction deux fois dérivable, $F(ct-\vec k\cdot\vec r)$, avec $\vec r=(x,y)$, est donc solution. $\vec k$ indique la direction de propagation.

## Séparation des variables (pages 3 et 4)

On cherche une solution sous la forme $\phi(x,y,t)=X(x)Y(y)T(t)$ :

$$
XY\frac{T''}{c^2}-YTX''-XTY''=0.
$$

En divisant par $XYT$ :

$$
\frac{T''}{Tc^2}=\frac{X''}{X}+\frac{Y''}{Y}.
$$

Posons $T''/(Tc^2)=-\omega^2/c^2$. Il existe $k_x,k_y,\omega$ tels que :

$$
k_x^2+k_y^2=\frac{\omega^2}{c^2},
\qquad
\begin{cases}T''=-\omega^2T,\\X''=-k_x^2X,\\Y''=-k_y^2Y.\end{cases}
$$

On obtient trois oscillateurs harmoniques. La source présente la superposition :

$$
\begin{aligned}
\phi(x,y,t)=\sum_{k_x,k_y}\bigl(&A_{k_x,k_y}e^{i(\omega t-\vec k\cdot\vec r)}
+B_{k_x,k_y}e^{i(\omega t+\vec k\cdot\vec r)}\\
&+C_{k_x,k_y}e^{-i(\omega t-\vec k\cdot\vec r)}
+D_{k_x,k_y}e^{-i(\omega t+\vec k\cdot\vec r)}\bigr).
\end{aligned}
$$

Relation de dispersion : $\omega^2=c^2(k_x^2+k_y^2)$.

> La notation $\vec k$ change de sens : c’était un vecteur **unitaire** page 3 ; dans les exponentielles et la relation de dispersion, c’est le vecteur d’onde, de norme $\omega/c$.

## Conditions aux bords (pages 5 et 6)

En une dimension, on devait spécifier $\phi(a,t)$ et $\phi(b,t)$ pour tout $t$, ainsi que $\phi(x,0)$ et $\partial_t\phi(x,0)$ pour tout $x\in[a,b]$.

En deux dimensions, le cours demande $\phi(x,y,t)$ sur le bord $S_1$ du domaine. Exemple :

$$
S_1=\{(x,y): (|x|=a,\ |y|\le b)\ \text{ou}\ (|y|=b,\ |x|\le a)\},
$$

$$
V_1=\{(x,y,t):|x|\le a,\ |y|\le b\}.
$$

$\phi(x,y,0)$ et $\partial_t\phi(x,y,0)$ doivent être données sur l’intersection de $V_1$ avec un plan $(x,y,t_0)$, $t_0$ constant : ce sont les conditions initiales.

> Les mentions « Fig » page 5 et « EX : figure » page 6 sont présentes, mais aucune figure n’est insérée dans ces deux pages.

## Exemple de modes séparés (page 7)

La source utilise la lettre minuscule $x$ à la fois pour la coordonnée et pour la fonction $X$. En distinguant ces deux objets :

$$
X''=-k_x^2X,\qquad X(a)=X(-a)=0,
\qquad X(x)=A_x\sin\left(\frac{n\pi x}{a}\right).
$$

De même, $Y(y)=A_y\sin(m\pi y/b)$. Ainsi :

$$
\phi(x,y,t)=\sum_{n,m}\sin\left(\frac{n\pi x}{a}\right)
\sin\left(\frac{m\pi y}{b}\right)
\left[A_{n,m}\cos(\omega_{n,m}t)+B_{n,m}\sin(\omega_{n,m}t)\right],
$$

$$
\omega_{n,m}=\pi c\sqrt{\frac{n^2}{a^2}+\frac{m^2}{b^2}}.
$$

> Limite de la source : ces sinus satisfont les bords en $\pm a$ et $\pm b$, mais ne constituent pas la base complète sur le rectangle centré $[-a,a]\times[-b,b]$. Une base complète utilise $\sin[n\pi(x+a)/(2a)]\sin[m\pi(y+b)/(2b)]$, avec $n,m\ge1$. La formule du cours est en revanche la base usuelle sur $[0,a]\times[0,b]$.

## Section V.1.2 — Coordonnées polaires (page 8)

Différents choix de coordonnées peuvent produire des conditions aux bords simples ou complexes selon la forme de la surface délimitant le domaine de l’onde. Les coordonnées polaires facilitent la description d’un bord circulaire.

La source affiche :

$$
r=\sqrt{x^2+y^2},\qquad x=r\cos\theta,\qquad y=r\cos\theta,
\qquad\theta=\arccos(x/r).
$$

> Coquille : $y=r\sin\theta$. L’expression $\arccos(x/r)$ seule ne distingue pas les deux demi-plans ; le choix de l’angle doit aussi tenir compte du signe de $y$.

## Changement des opérateurs de dérivation (page 9)

Que devient l’équation d’onde ? Par la règle de la chaîne :

$$
\begin{aligned}
\frac\partial{\partial x}
&=\frac{\partial r}{\partial x}\frac\partial{\partial r}
+\frac{\partial\theta}{\partial x}\frac\partial{\partial\theta}
=\cos\theta\frac\partial{\partial r}-\frac{\sin\theta}{r}\frac\partial{\partial\theta},\\
\frac\partial{\partial y}
&=\frac{\partial r}{\partial y}\frac\partial{\partial r}
+\frac{\partial\theta}{\partial y}\frac\partial{\partial\theta}
=\sin\theta\frac\partial{\partial r}+\frac{\cos\theta}{r}\frac\partial{\partial\theta}.
\end{aligned}
$$

La page développe ensuite le carré de l’opérateur $\partial_x$. Pour transcrire les lignes compactes, notons $D_r=\partial_r$ et $D_\theta=\partial_\theta$ ; les produits d’opérateurs ci-dessous désignent leur composition. Les lignes **telles qu’imprimées** sont :

$$
\begin{aligned}
\partial_x^2
&=\left(\cos\theta D_r-\frac{\sin\theta}{r}D_\theta\right)^2\\
&=\cos^2\theta D_r^2
+\cos\theta D_r\left(\frac{\sin\theta}{r}D_\theta\right)
-\frac{\sin\theta}{r}D_\theta(\cos\theta D_r)
+\frac{\sin\theta}{r}D_\theta\left(\frac{\sin\theta}{r}D_\theta\right)\\
&=\cos^2\theta D_r^2
+\frac{\cos\theta\sin\theta}{r^2}D_\theta
-\frac{\cos\theta\sin\theta}{r}D_rD_\theta
-\frac{\cos\theta\sin\theta}{r}D_\theta D_r\\
&\quad+\frac{\sin^2\theta}{r}D_\theta D_r
+\frac{\sin^2\theta}{r^2}D_\theta^2
+\frac{\cos\theta\sin\theta}{r^2}D_\theta^2\\
&=\cos^2\theta D_r^2
+2\frac{\cos\theta\sin\theta}{r^2}D_\theta
+\frac{\sin^2\theta}{r}D_\theta D_r
+\frac{\sin^2\theta}{r^2}D_\theta^2.
\end{aligned}
$$

> Ce développement comporte plusieurs erreurs de signes et d’ordres de dérivation. L’expression corrigée est :

$$
\partial_x^2=
\cos^2\theta\,\partial_r^2
-\frac{2\sin\theta\cos\theta}{r}\,\partial_r\partial_\theta
+\frac{\sin^2\theta}{r^2}\,\partial_\theta^2
+\frac{\sin^2\theta}{r}\,\partial_r
+\frac{2\sin\theta\cos\theta}{r^2}\,\partial_\theta.
$$

## Équation d’onde en coordonnées polaires (page 10)

La conclusion de la source pour le laplacien est correcte :

$$
\partial_x^2+\partial_y^2
=\partial_r^2+\frac1r\partial_r+\frac1{r^2}\partial_\theta^2.
$$

D’où :

$$
\frac1{c^2}\frac{\partial^2\phi}{\partial t^2}
-\left(\frac{\partial^2\phi}{\partial r^2}
+\frac1r\frac{\partial\phi}{\partial r}
+\frac1{r^2}\frac{\partial^2\phi}{\partial\theta^2}\right)=0.
$$

On sépare les variables : $\phi(r,\theta,t)=F(r,\theta)G(t)$.

## Séparation temporelle et spatiale (page 11)

$$
\frac1{G(t)c^2}\frac{d^2G}{dt^2}
-\frac1F\left(\partial_r^2+\frac1r\partial_r+\frac1{r^2}\partial_\theta^2\right)F=0.
$$

L’opérateur $\Delta=\partial_r^2+r^{-1}\partial_r+r^{-2}\partial_\theta^2$ est le laplacien. On obtient :

$$
\frac{d^2G}{dt^2}=-k^2c^2G(t),
\qquad\Delta F(r,\theta)=-k^2F(r,\theta).
$$

On sépare à nouveau : $F(r,\theta)=R(r)\psi(\theta)$.

## Séparation radiale et angulaire (page 12)

$$
\frac1R\frac{d^2R}{dr^2}+\frac1{rR}\frac{dR}{dr}
+\frac1{\psi r^2}\frac{d^2\psi}{d\theta^2}=-k^2,
$$

$$
\left(\frac{r^2}{R}\frac{d^2R}{dr^2}+\frac rR\frac{dR}{dr}+k^2r^2\right)
+\frac1\psi\frac{d^2\psi}{d\theta^2}=0.
$$

Il en résulte :

$$
\frac{d^2\psi}{d\theta^2}=-\lambda^2\psi,
\qquad
r^2\frac{d^2R}{dr^2}+r\frac{dR}{dr}+k^2r^2R=\lambda^2R.
$$

> La première ligne de la source porte par erreur $\partial^2R(r)/\partial t^2$ ; la variable est bien $r$, comme dans les lignes suivantes.

## Partie angulaire et partie radiale (page 13)

$$
\psi''(\theta)=-\lambda^2\psi(\theta)
\quad\Longrightarrow\quad
\psi(\theta)=B\cos(\lambda\theta)+C\sin(\lambda\theta).
$$

On doit avoir $\psi(\theta)=\psi(\theta+2\pi)$. La source écrit :

$$
\psi(0)=B=\psi(2\pi)=B\cos(2\pi\lambda)+C\sin(2\pi\lambda),
$$

puis conclut que $\lambda$ est un entier.

> Cette conclusion provient de la périodicité pour tout $\theta$ d’une solution non nulle, et pas de la seule égalité aux deux extrémités. Pour $\lambda=0$, la solution périodique est constante.

La partie radiale est écrite, en renommant $R$ en $F$ :

$$
r^2F''+rF'+k^2r^2F=\lambda^2F.
$$

Le document s’arrête ici ; il ne contient pas de développement supplémentaire en dimension 3 malgré son titre.
