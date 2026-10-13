---
source: "PREING2-S2/Ondes/CM-Chapitre3_2022-2023_Ondes_P2S2_ABoumiz.pdf"
pages: 15
transcription: manuelle
transcription_date: 2026-10-04
verification: lecture visuelle de toutes les pages ; matrices et formules vérifiées ; formule coupée et erreurs originales signalées
---

# Chapitre 3 — Oscillations couplées et modes normaux

## Section I — Deux oscillateurs couplés (page 1)

Soient deux blocs de masses $m_1$ et $m_2$ posés sur un plan horizontal, liés par un ressort idéal de constante de raideur $k$ et de longueur au repos $L_0$. On néglige les forces de frottement.

La page 1 ne comporte pas de schéma dans cette version.

## Équations du mouvement (page 2)

Forces exercées sur les masses :

$$
\vec F_1=k(x_2-x_1)\vec u_x,
\qquad \vec F_2=k(x_1-x_2)\vec u_x.
$$

Deuxième loi de Newton :

$$
\begin{cases}
m_1\ddot x_1=k(x_2-x_1),\\
m_2\ddot x_2=k(x_1-x_2).
\end{cases}
$$

Posons $\omega_1^2=k/m_1$ et $\omega_2^2=k/m_2$ :

$$
\frac{d^2}{dt^2}\begin{pmatrix}x_1\\x_2\end{pmatrix}
=\begin{pmatrix}-\omega_1^2&\omega_1^2\\\omega_2^2&-\omega_2^2\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}.\tag{*}
$$

Pour résoudre ce système d’équations différentielles, on cherche les modes propres, ou modes normaux.

> Les forces écrites supposent que $x_1$ et $x_2$ désignent les déplacements par rapport à une configuration où le ressort est à sa longueur à vide. Pour des abscisses absolues, l’allongement serait $x_2-x_1-L_0$.

## Recherche des modes propres (page 3)

$$
\begin{pmatrix}x_1\\x_2\end{pmatrix}
=e^{i\omega t}\begin{pmatrix}A\\B\end{pmatrix},
\qquad
\frac{d^2}{dt^2}\begin{pmatrix}x_1\\x_2\end{pmatrix}
=-\omega^2\begin{pmatrix}x_1\\x_2\end{pmatrix}.
$$

En notant $M=\begin{pmatrix}-\omega_1^2&\omega_1^2\\\omega_2^2&-\omega_2^2\end{pmatrix}$, l’équation (*) donne :

$$
-\omega^2\begin{pmatrix}x_1\\x_2\end{pmatrix}
=M\begin{pmatrix}x_1\\x_2\end{pmatrix},
\qquad M\begin{pmatrix}A\\B\end{pmatrix}
=-\omega^2\begin{pmatrix}A\\B\end{pmatrix}.
$$

$\binom AB$ est un vecteur propre de $M$ de valeur propre $-\omega^2$. Il faut donc $\det(M+\omega^2I)=0$.

## Pulsations et solution (page 4)

$$
\begin{aligned}
0&=\det\begin{pmatrix}-\omega_1^2+\omega^2&\omega_1^2\\\omega_2^2&-\omega_2^2+\omega^2\end{pmatrix}\\
&=(-\omega_1^2+\omega^2)(-\omega_2^2+\omega^2)-\omega_1^2\omega_2^2\\
&=\omega^4-\omega_1^2\omega^2-\omega_2^2\omega^2\\
&=\omega^2(\omega^2-\omega_1^2-\omega_2^2).
\end{aligned}
$$

Ainsi, $\omega^2=0$ ou $\omega^2=\omega_1^2+\omega_2^2$.

Le bas de la page commence la solution générale :

$$
\begin{pmatrix}x_1\\x_2\end{pmatrix}
=\left(A_+e^{i\omega_+t}+B_+e^{-i\omega_+t}\right)\vec V_+
+\left(A_-e^{i\omega_-t}+\cdots\right).
$$

> La formule originale est coupée après le signe $+$ suivant $A_-e^{i\omega_-t}$ : la suite n’est pas visible dans le PDF. De plus, le mode de pulsation nulle ne se décrit pas par deux exponentielles indépendantes. Pour ce mode, la solution générale comporte $(C+Dt)\binom11$. Le mode non nul a la pulsation $\sqrt{k/m_1+k/m_2}$ et un vecteur propre proportionnel à $\binom{m_2}{-m_1}$. Ces précisions sont des corrections explicatives, et non du texte visible au bas de la page.

## Section II — $n$ oscillateurs couplés (page 5)

Plus généralement, les équations du mouvement de $n$ oscillateurs couplés linéairement sont de la forme :

$$
M\frac{d^2\vec X}{dt^2}+K\vec X=\vec0,
\qquad\vec X=(x_1,x_2,\ldots,x_n)^T.
$$

**Couplage linéaire :** l’interaction peut être décrite par un potentiel $V(\vec X)$ qui est un polynôme d’ordre 2 en $x_1,x_2,\ldots$ :

$$
V(\vec X)=\sum_{i,j}k^{i,j}x_ix_j.
$$

Puisque $x_ix_j=x_jx_i$, le cours choisit $k$ symétrique. $M$ est ici la matrice de masse, symétrique, d’ordre $n$ :

$$
M=\begin{pmatrix}M_1&0&0\\0&M_2&0\\0&0&\ddots\end{pmatrix}.
$$

> La lettre $M$ désigne maintenant la matrice de masse, et non la matrice dynamique de la section I. La source emploie indifféremment $k$ et $K$ pour la matrice de raideur. Pour obtenir exactement la force $-K\vec X$, le potentiel est $V=\frac12\vec X^TK\vec X$ ; avec la somme écrite sans $1/2$, $K$ vaut deux fois la matrice symétrique des coefficients $k^{i,j}$. Seule la partie symétrique contribue à la forme quadratique.

## Section II.1 — Méthodes générales (pages 6 et 7)

L’équation du mouvement peut s’écrire :

$$
\ddot{\vec X}+(M^{-1}K)\vec X=\vec0.\tag{*}
$$

La source introduit un ensemble complet de vecteurs propres orthonormés $\{\vec Y_i\}_{i=1,\ldots,n}$ de $M^{-1}K$ :

$$
M^{-1}K\vec Y_i=\lambda_i\vec Y_i,
\qquad \vec Y_i^T\vec Y_j=\delta_{ij}
=\begin{cases}0&i\ne j,\\1&i=j.\end{cases}
$$

Il existe donc des coefficients $\alpha_i(t)$ tels que :

$$
\vec X=\sum_{j=1}^n\alpha_j\vec Y_j.
$$

En remplaçant dans (*) :

$$
\sum_{j=1}^n\ddot\alpha_j\vec Y_j
+\sum_{j=1}^n\alpha_jM^{-1}K\vec Y_j=\vec0,
$$

$$
\sum_{j=1}^n(\ddot\alpha_j+\alpha_j\lambda_j)\vec Y_j=\vec0
\quad\Longrightarrow\quad
\forall j,\quad\ddot\alpha_j+\lambda_j\alpha_j=0.
$$

Les $\alpha_j$ sont les **coordonnées normales**. Les coefficients se comportent comme des oscillateurs harmoniques simples de pulsation $\omega_j=\sqrt{\lambda_j}$.

Remarque 1 : $\{\vec Y_i\}_{i=1,\ldots,n}$ est une base de $\mathbb R^n$. Remarque 2 : on ne peut pas être certain que $\lambda_j>0$.

> Rectification : $M^{-1}K$ n’est généralement pas symétrique pour le produit scalaire euclidien. Pour $M$ diagonale positive et $K$ symétrique, on peut choisir les modes **orthonormés pour la masse**, $\vec Y_i^TM\vec Y_j=\delta_{ij}$, ou diagonaliser la matrice symétrique $M^{-1/2}KM^{-1/2}$. Les projections euclidiennes de la source ne sont donc pas valables en général. L’interprétation harmonique suppose $\lambda_j>0$ ; $\lambda_j=0$ donne une fonction affine du temps et $\lambda_j<0$ des exponentielles réelles.

## Section II.2 — Valeurs initiales (page 8)

On résout $\ddot{\vec X}+M^{-1}K\vec X=\vec0$, avec $\vec X(0)=\vec X_0$ et $\dot{\vec X}(0)=\vec V_0$.

En termes des $\alpha_j$, la source écrit $\alpha_j(t)=\vec Y_j^T\vec X(t)$.

La source écrit ensuite :

$$
\alpha_j(t)=\vec Y_j^T\vec X_0,
\qquad\dot\alpha_j(t)=\vec Y_j^T\vec V_0.
$$

> Dans ces deux conditions **initiales**, lire $0$ à la place de $t$. Avec les modes orthonormés pour la masse, les projections correctes sont $\alpha_j(0)=\vec Y_j^TM\vec X_0$ et $\dot\alpha_j(0)=\vec Y_j^TM\vec V_0$.

## Section II.3 — Frottements (page 9)

$$
\ddot{\vec X}+\Gamma\dot{\vec X}+M^{-1}K\vec X=\vec0,\tag{**}
$$

où $\Gamma$ est une matrice. Posons $\vec X(t)=e^{-i\omega t}\vec X(0)$, où $\vec X(0)$ est indépendant du temps :

$$
\left(-\omega^2I-i\omega\Gamma+M^{-1}K\right)\vec X(0)=\vec0.
$$

$I$ est la matrice identité. Pour une solution non nulle, $\vec X(0)$ est un vecteur propre de valeur propre nulle de la matrice $-\omega^2I-i\omega\Gamma+M^{-1}K$.

## Section II.4 — Oscillations entretenues (pages 10 et 11)

Soit $\vec F(t)$ une force externe appliquée au système :

$$
\ddot{\vec X}+\Gamma\dot{\vec X}+M^{-1}K\vec X=M^{-1}\vec F(t).
$$

On suppose $\vec F(t)=\vec F_0e^{-i\omega_dt}$. Si la force n’oscille pas dans la même direction sur toutes les composantes, on utilise le principe de superposition.

Posons $\vec X(t)=\vec A e^{-i\omega_dt}$. La source donne :

$$
\vec A=\left(-\omega^2I-i\omega\Gamma+M^{-1}K\right)^{-1}\vec F_0.
$$

Remarque 1 : si la matrice $-\omega^2I-i\omega\Gamma+M^{-1}K$ n’est pas inversible, le cours indique « résonance ».

Remarque 2 : la solution générale est la somme de la solution générale de l’équation homogène et d’une solution particulière, par exemple $\vec X(t)=\vec A e^{-i\omega_dt}$.

> La source emploie $\omega$ à la place de $\omega_d$ dans cette formule. La formule de $\vec A$ omet le facteur $M^{-1}$ devant $\vec F_0$. Pour l’équation écrite page 10, il faut $\vec A=(-\omega_d^2I-i\omega_d\Gamma+M^{-1}K)^{-1}M^{-1}\vec F_0$. La non-inversibilité signale un mode propre à la fréquence considérée ; l’excitation résonante dépend aussi de la projection de la force sur ce mode.

## Rappel — Oscillateur harmonique simple (pages 11 et 12)

$$
\ddot X+\omega^2X=0,
\qquad X(t)=A\cos(\omega t)+B\sin(\omega t),
$$

où $\omega$ est la pulsation. Avec friction :

$$
\ddot X+\Gamma\dot X+\omega_0^2X=0.\tag{*}
$$

La solution générale est :

$$
x(t)=e^{-\Gamma t/2}
\begin{cases}
Ae^{\omega t}+Be^{-\omega t},&\omega=\sqrt{\Gamma^2/4-\omega_0^2},\quad\text{surcritique (apériodique)},\\
A+Bt,&\text{critique},\\
A\cos(\omega t)+B\sin(\omega t),&\omega=\sqrt{\omega_0^2-\Gamma^2/4},\quad\text{sous-critique (pseudopériodique)}.
\end{cases}
$$

## Rappel — Oscillateur entretenu (page 13)

$$
\ddot X+\Gamma\dot X+\omega_0^2X=F(t)/M.\tag{**}
$$

Solution générale : $X_0(t)+X_F(t)$, où $X_0(t)$ est la solution générale de (*) et $X_F(t)$ une solution particulière de (**).

## Rappel — Système de $n$ oscillateurs (page 14)

$$
M\frac{d^2\vec X}{dt^2}+K\vec X=\vec0,
\qquad\vec X=(x_1,x_2,\ldots,x_n)^T.
$$

$M$ est la matrice de masse. La source présente :

$$
\vec X(t)=\sum_{j=1}^n\left(A_je^{i\omega_jt}+B_je^{-i\omega_jt}\right)\vec V_j,
\qquad\vec X_j^{\,\pm}=e^{\pm i\omega_jt}\vec V_j.
$$

$\vec V_j$ est un vecteur propre de $M^{-1}K$ ; la source donne sa valeur propre comme $\omega_j$.

> Coquille : cette valeur propre est $\omega_j^2$. La formule exponentielle affichée suppose des modes de pulsation non nulle ; les modes nuls nécessitent des termes affines en $t$.

## Fin du document (page 15)

La page 15 est blanche.
