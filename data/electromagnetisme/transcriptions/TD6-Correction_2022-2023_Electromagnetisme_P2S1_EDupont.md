---
source: "PREING2-S1/Electromagnetisme/TD6-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf"
pages: 13
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des treize pages ; intégrales, orientations des courants et calculs vectoriels restitués et vérifiés
---

# TD 6 — Biot et Savart, superposition et symétries — correction 2022–2023

## Page 1

# Loi de Biot et Savart — Théorème de superposition et symétries

Ressource indiquée : https://cpinettes.u-cergy.fr/S3-Electromag.html

### Rappel des symétries

| | Champ électrique $\vec E$ | Champ magnétique $\vec B$ |
| --- | --- | --- |
| Sources | Charges $q_i$ | Courants $I$, $\vec j$ |
| Plan $\Pi$ de symétrie des sources | $\vec E\in\Pi$ ; deux plans donnent une direction commune. | $\vec B\perp\Pi$ ; un plan suffit à donner la direction. |
| Plan $\Pi^*$ d’antisymétrie des sources | $\vec E\perp\Pi^*$ ; un plan suffit à donner la direction. | $\vec B\in\Pi^*$ ; deux plans donnent une direction commune. |

Ces propriétés du champ s’appliquent au point d’observation appartenant aux plans considérés. Les petits dessins représentent des charges réfléchies de même signe ou de signe opposé, et des courants réfléchis avec ou sans inversion de leur sens. La marge rappelle le choix des coordonnées et l’étude des invariances.

### Exercice 1 — Fil rectiligne infiniment long

**a.** Calculer, par intégration en utilisant la loi de Biot et Savart, le champ magnétique $\vec B$ créé en un point $M$ quelconque par un fil rectiligne infiniment long défini par l’axe $(Oz)$.

Le courant $I$ est orienté vers $+Oz$. Un élément du fil est repéré par $P$ et $I\,\mathrm d\vec\ell$. Le champ en $M$ est indiqué tangentiellement autour du fil.

**Loi de Biot et Savart :**

$$
\vec B(M)=\int_{P\in\mathrm{fil}}\mathrm d\vec B_P(M)
=\frac{\mu_0}{4\pi}\int_{P\in\mathrm{fil}}
\frac{I\,\mathrm d\vec\ell(P)\wedge\overrightarrow{PM}}{PM^3}
=\frac{\mu_0}{4\pi}\int_{P\in\mathrm{fil}}
\frac{I\,\mathrm d\vec\ell\wedge\vec u_{PM}}{r^2}.
$$

Dans cette dernière écriture générale, $r=PM$.

- $\vec B(M)$ est continu lorsque $M$ est dans une distribution volumique de courant.
- Il est discontinu lorsque $M$ est sur une nappe de courant surfacique.
- Il diverge lorsque $M$ est sur une distribution linéique de courant.

Une vignette porte la formule $\vec B(r)=\mu_0I\vec e_\theta/(2\pi r)$ et un graphe croissant jusqu’à un rayon $R$, puis décroissant. Ce graphe possède une région intérieure de rayon non nul ; il ne représente pas le fil idéal de rayon nul de l’énoncé.

## Page 2

### Définition, invariances et direction

0. **Définition et continuité.** Pour la distribution linéique de courant, $\vec B$ diverge sur le fil, c’est-à-dire à $r=0$.
1. **Coordonnées cylindriques.** Base $(\vec u_r,\vec u_\theta,\vec u_z)$. On peut choisir l’origine $O$ n’importe où sur le fil infini, notamment au projeté orthogonal $H$ de $M$ sur l’axe. $z_H=z_M$.
2. **Invariances.** La distribution de courant est invariante par rotation autour de $Oz$, donc les composantes du champ sont indépendantes de $\theta$. Elle est aussi invariante par translation selon $z$, donc elles sont indépendantes de $z$. La dépendance restante est en $r$.
3. **Symétries.** Le plan $\Pi^*=(M,\vec u_r,\vec u_\theta)$, perpendiculaire au fil, est un plan d’antisymétrie des courants : $\vec B\in\Pi^*$. Le plan $\Pi=(M,\vec u_z,\vec u_r)$ contenant le fil est un plan de symétrie : $\vec B\perp\Pi$.

On obtient

$$\vec B(M)=B(r)\vec u_\theta.$$

Les lignes de champ sont des cercles centrés sur l’axe du fil, à altitude fixée. Le champ est constant en norme le long de chaque cercle et orthoradial. Le sens suit la règle de la main droite autour du courant.

4. **Théorème d’Ampère**, résultat annoncé :

$$\vec B(r)=\frac{\mu_0I}{2\pi r}\vec u_\theta.$$

La démonstration est donnée après le calcul par Biot et Savart.

## Page 3

### Calcul par la loi de Biot et Savart

Le champ magnétique élémentaire vaut

$$
\mathrm d\vec B(M)=\frac{\mu_0}{4\pi}
\frac{I\,\mathrm d\vec\ell\wedge\overrightarrow{PM}}
{\|\overrightarrow{PM}\|^3}.
$$

Le champ total est la somme vectorielle des champs élémentaires créés par tous les points $P$ du fil.

On choisit $O$ au projeté de $M$ sur le fil, et $z=z_P$. Alors

$$
\overrightarrow{OM}=r\vec u_r,\quad
\overrightarrow{OP}=z\vec u_z,\quad
I\,\mathrm d\vec\ell=I\,\mathrm dz\vec u_z,
$$

$$
\overrightarrow{PM}=\overrightarrow{PO}+\overrightarrow{OM}
=-z\vec u_z+r\vec u_r,
\qquad\|\overrightarrow{PM}\|^2=z^2+r^2.
$$

D’où

$$
\vec B(M)=\frac{\mu_0I}{4\pi}
\int_{-\infty}^{+\infty}
\frac{\mathrm dz\vec u_z\wedge(-z\vec u_z+r\vec u_r)}
{(z^2+r^2)^{3/2}}.
$$

La base cylindrique est orthonormée directe :

$$\vec u_z\wedge\vec u_z=\vec0,\qquad
\vec u_z\wedge\vec u_r=\vec u_\theta.$$

Ainsi

$$
\vec B(M)=\frac{\mu_0I}{4\pi}
\left[\int_{-\infty}^{+\infty}
\frac{r\,\mathrm dz}{(z^2+r^2)^{3/2}}\right]\vec u_\theta.
$$

Quel que soit le point $P$, donc quel que soit $z$, le vecteur $\vec u_\theta$ en $M$ ne change pas. Il sort de l’intégrale.

On note l’intégrale entre crochets $K$. Pour le changement de variable,

$$\tan\theta=\frac zr,\qquad
z\in\mathbb R\Longleftrightarrow\theta\in\left]-\frac\pi2,\frac\pi2\right[.$$

> Ici $\theta$ est l’angle du triangle $MOP$ utilisé dans le changement de variable, distinct de l’azimut de la base cylindrique.

## Page 4

### Évaluation de l’intégrale

$$
K=\int_{-\infty}^{+\infty}\frac{r\,\mathrm dz}{(r^2+z^2)^{3/2}},
\qquad
\vec B(M)=\frac{\mu_0I}{4\pi}K\vec u_\theta.
$$

Avec $z=r\tan\theta$,

$$
\mathrm dz=\frac{\partial z}{\partial\theta}\,\mathrm d\theta
=r\frac{\mathrm d\theta}{\cos^2\theta},
\qquad r\,\mathrm dz=\frac{r^2\,\mathrm d\theta}{\cos^2\theta}.
$$

Les bornes deviennent $-\pi/2$ et $+\pi/2$. Comme

$$1+\tan^2\theta=\frac1{\cos^2\theta},$$

et $\cos\theta>0$ sur cet intervalle,

$$
\cos^2\theta(1+\tan^2\theta)^{3/2}=\frac1{\cos\theta}.
$$

Donc

$$
K=\int_{-\pi/2}^{\pi/2}
\frac{r^2\,\mathrm d\theta}
{r^3\cos^2\theta(1+\tan^2\theta)^{3/2}}
=\frac1r\int_{-\pi/2}^{\pi/2}\cos\theta\,\mathrm d\theta
=\frac2r.
$$

Finalement

$$
\boxed{\vec B(M)=\frac{\mu_0I}{4\pi}\frac2r\vec u_\theta
=\frac{\mu_0I}{2\pi r}\vec u_\theta}.
$$

**b.** Retrouver ce champ magnétique en appliquant le théorème d’Ampère.

## Page 5

### Théorème d’Ampère

Pour une distribution volumique de courant, le théorème d’Ampère s’écrit en régime permanent et dans l’ARQS : quel que soit le contour fermé $C$ et quelle que soit la surface $S$ délimitée par $C$,

$$
\oint_{M\in C}\vec B(M)\cdot\mathrm d\vec\ell(M)
=\mu_0 I_{\mathrm{enlacés}}
=\mu_0\iint_S\vec j\cdot\mathrm d\vec S.
$$

Le sens de $\mathrm d\vec S$ est fixé par celui de $\mathrm d\vec\ell$ avec la règle de la main droite, ou du tire-bouchon.

L’exemple dessiné donne une somme algébrique

$$I_{\mathrm{enlacés}}=I_2+I_3-I_1-I_2=-I_1+I_3.$$

Le même courant $I_2$ traverse la surface une fois dans chaque sens : ses contributions se compensent.

- Bien choisir le contour fermé, par exemple une ligne de champ sur laquelle $B$ est constant.
- Orienter le contour pour fixer la normale $\vec n$.
- Compter positivement un courant traversant la surface dans le sens de $\vec n$, négativement dans le sens opposé.

### Application au fil infini

On choisit un cercle $C$ d’axe $Oz$, de rayon $r$, à altitude fixée. C’est une ligne de champ et $B(r)$ y est constant.

$$\vec B=B(r)\vec u_\theta,\qquad
\mathrm d\vec\ell=\mathrm d\ell_\theta\vec u_\theta
=r\,\mathrm d\theta\vec u_\theta.$$

Le théorème s’écrit $\oint_C\vec B\cdot\mathrm d\vec\ell=\mu_0I_{\mathrm{enlacé}}$.

## Page 6

### Fin de l’application au fil

$$
\oint_C\vec B\cdot\mathrm d\vec\ell
=\int_0^{2\pi}B(r)\vec u_\theta\cdot r\,\mathrm d\theta\vec u_\theta
=rB(r)\int_0^{2\pi}\mathrm d\theta
=2\pi rB(r).
$$

Avec l’orientation choisie, $I_{\mathrm{enlacé}}=+I$. Donc

$$2\pi rB(r)=\mu_0I,\qquad
\boxed{\vec B=\frac{\mu_0I}{2\pi r}\vec u_\theta}.$$

### Exercice 3 — Spire

Calculer, par intégration en utilisant la loi de Biot et Savart, le champ magnétique (direction, sens et module) créé en un point $M$ de l’axe de révolution d’une spire de centre $O$ et de rayon $R$, parcourue par un courant d’intensité $I$ constante.

Le dessin place la spire dans un plan perpendiculaire à $Oz$ et $M$ sur l’axe. Un point $P$ de la spire porte $I\,\mathrm d\vec\ell$. L’angle $\alpha$ sous lequel on voit le rayon de la spire depuis $M$ vérifie $\sin\alpha=R/PM$.

0. Le champ est défini et continu sauf sur la spire idéale.
1. On utilise les coordonnées cylindriques : $\vec B(r,\theta,z)$.
2. La distribution de courant est invariante par rotation : les composantes de $\vec B$ sont indépendantes de $\theta$. Sur l’axe, $r=0$ ; il reste une dépendance en $z$.
3. Deux plans contenant l’axe, notés $\Pi_1^*=(M,\vec u_r,\vec u_z)$ et $\Pi_2^*=(M,\vec u_\theta,\vec u_z)$, sont des plans d’antisymétrie. $\vec B$ appartient aux deux :

$$\boxed{\vec B=B(z)\vec u_z}.$$

> La numérotation du support passe ici de l’exercice 1 à l’exercice 3 ; l’exercice 2 apparaît page 8.

## Page 7

### Champ de la spire sur son axe

$$\vec B=\int_{\mathrm{spire}}\mathrm d\vec B
=\frac{\mu_0}{4\pi}\int_{\mathrm{spire}}
\frac{I\,\mathrm d\vec\ell\wedge\overrightarrow{PM}}{\|\overrightarrow{PM}\|^3}.$$

Avec l’orientation du dessin,

$$
\mathrm d\vec\ell=R\,\mathrm d\theta\vec u_\theta,\qquad
\overrightarrow{PM}=-R\vec u_r-z\vec u_z,
\qquad PM^2=R^2+z^2.
$$

Le dessin situe $M$ du côté négatif de l’axe ; $z$ dans cette décomposition est la distance axiale positive représentée. Le résultat final dépend de $z^2$ et s’applique de part et d’autre de la spire.

Les produits vectoriels sont

$$\vec u_\theta\wedge\vec u_r=-\vec u_z,\qquad
\vec u_\theta\wedge\vec u_z=\vec u_r.$$

Ainsi

$$
\vec B=\frac{\mu_0IR}{4\pi(R^2+z^2)^{3/2}}
\left[\int_0^{2\pi}R\,\mathrm d\theta\vec u_z
+\int_0^{2\pi}(-z)\,\mathrm d\theta\vec u_r\right].
$$

La seconde intégrale est nulle par compensation des directions radiales. En effet,

$$\vec u_r=\cos\theta\vec u_x+\sin\theta\vec u_y,$$

$$
\int_0^{2\pi}\vec u_r\,\mathrm d\theta
=\left[\sin\theta\right]_0^{2\pi}\vec u_x
+\left[-\cos\theta\right]_0^{2\pi}\vec u_y=\vec0.
$$

D’où

$$
\boxed{\vec B=
\frac{\mu_0IR^2}{4\pi(R^2+z^2)^{3/2}}
\int_0^{2\pi}\mathrm d\theta\vec u_z
=\frac{\mu_0I}{2}\frac{R^2}{(R^2+z^2)^{3/2}}\vec u_z}.
$$

Or

$$\sin\alpha=\frac R{\sqrt{R^2+z^2}},\qquad
\sin^3\alpha=\frac{R^3}{(R^2+z^2)^{3/2}}.$$

Donc, en $M$ sur l’axe de la spire,

$$\boxed{\vec B(M)=\frac{\mu_0I}{2R}\sin^3\alpha\vec u_z}.$$

Vérification dimensionnelle : $[B]=[\mu_0][I]/L$.

## Page 8

### Exercice 2 — Flux du champ magnétique pour un fil

Déterminer l’expression du flux $\Phi(\vec B)$ du champ magnétique créé par un fil rectiligne infini parcouru par un courant d’intensité $I$, à travers un rectangle dont le plan contient le fil, de dimensions $h$ (parallèle au fil) et $b$ (perpendiculaire au fil). Le côté le plus proche se trouve à la distance $a$, avec $a<b<h$.

Le schéma oriente la surface suivant le champ, normal au rectangle. En coordonnées cylindriques,

$$\mathrm d\ell_r=\mathrm dr,\quad
\mathrm d\ell_\theta=r\,\mathrm d\theta,\quad
\mathrm d\ell_z=\mathrm dz,$$

$$\mathrm dS_r=r\,\mathrm d\theta\,\mathrm dz,\quad
\mathrm dS_\theta=\mathrm dr\,\mathrm dz,\quad
\mathrm dS_z=r\,\mathrm dr\,\mathrm d\theta.$$

Le flux élémentaire est

$$\mathrm d\Phi=\vec B\cdot\mathrm d\vec S
=B(r)\,\mathrm dS_\theta=B(r)\,\mathrm dr\,\mathrm dz.$$

Par conséquent,

$$
\Phi=\int_a^{a+b}\frac{\mu_0I}{2\pi r}\,\mathrm dr
\int_0^h\mathrm dz
=\frac{\mu_0Ih}{2\pi}\int_a^{a+b}\frac{\mathrm dr}{r}
=\boxed{\frac{\mu_0Ih}{2\pi}\ln\!\left(\frac{a+b}{a}\right)}.
$$

> Dans le rappel manuscrit du champ placé en haut de la page, le facteur $I$ est omis. Il est bien présent dans l’intégrale de flux et dans le résultat.

### Exercice 4 — Tore circulaire

On étudie le champ magnétique créé par une distribution de courants sur un tore circulaire de rayon $R$, à section circulaire de rayon $a$. $O$ est le centre du tore et $(Oz)$ son axe de révolution. Une chambre à air gonflée de vélo est un exemple de tore.

La distribution est constituée d’un enroulement d’un grand nombre $N$ de spires jointives circulaires de rayon $a$, enroulées sur toute la surface du tore. On néglige l’épaisseur des fils. Soit $M$ un point de l’espace où l’on cherche le champ.

Les dessins montrent une vue en coupe et une vue de dessus. Le rayon intérieur est $R-a$ et l’épaisseur de la section vaut $2a$. En vue de dessus, les flèches du courant sur la partie supérieure vont de l’extérieur vers l’intérieur du tore.

## Page 9

### Exercice 4 — Étude qualitative

**1 a. Domaine de définition.** Le champ est défini et continu dans tout l’espace sauf sur les spires idéales parcourues par le courant. Dans la suite, $M$ appartient à ce domaine.

**1 b. Direction en $M$.** Tous les plans passant par $M$ et contenant l’axe $Oz$ sont des plans de symétrie. Pour $M$ hors de l’axe, le plan méridien est

$$\Pi=(M,\vec u_r,\vec u_z).$$

Comme $\vec B\perp\Pi$,

$$\vec B=B(r,\theta,z)\vec u_\theta.$$

**1 c. Champ en $O$.** Le champ doit être perpendiculaire à chacun des plans méridiens passant par $O$. La seule possibilité est

$$\boxed{\vec B(O)=\vec0}.$$

**1 d. Coordonnées et dépendances.** L’axe de révolution du tore est $Oz$ : on choisit les coordonnées cylindriques d’axe $(O,z)$. La distribution de courant est invariante par rotation autour de cet axe, donc le module est indépendant de $\theta$ :

$$\vec B=B(r,z)\vec u_\theta.$$

Les lignes de champ sont des cercles centrés sur l’axe $Oz$. Pour $r$ et $z$ fixés, $B(r,z)$ est constant sur chaque ligne de champ. Le dessin distingue trois contours : un grand cercle à l’extérieur du tore (a), un cercle traversant son intérieur (b), et un petit cercle dans le trou central (c).

> Le raisonnement emploie l’idéalisation usuelle d’un enroulement jointif assimilé à une distribution axisymétrique.

## Page 10

### Exercice 4 — Théorème d’Ampère

**2. Montrer que le champ est nul à l’extérieur du tore.**

On choisit $\Gamma$, cercle de rayon $r$, à altitude $z$, centré sur l’axe $Oz$. La surface $\Sigma$ est le disque délimité par ce cercle.

$$\oint_\Gamma\vec B\cdot\mathrm d\vec\ell=\mu_0\sum I_{\mathrm{alg}}.$$

- **Cas (c), trou central :** aucun courant ne traverse le disque ; $\sum I_{\mathrm{alg}}=0$, donc $\vec B=\vec0$.
- **Cas (a), disque entourant tout le tore :** il y a autant de courants entrants que sortants. La somme est $(i-i)+(i-i)+\cdots=0$, donc $\vec B=\vec0$.

**3. Champ à l’intérieur du tore.**

$$
\oint_\Gamma\vec B\cdot\mathrm d\vec\ell
=\oint_\Gamma B(r,z)\vec u_\theta\cdot r\,\mathrm d\theta\vec u_\theta
=B(r,z)r\int_0^{2\pi}\mathrm d\theta
=2\pi rB(r,z).
$$

Dans le cas (b), le disque est coupé par $N$ spires dont le courant est descendant, dans le sens opposé à la normale $\vec n=\vec u_z$. Ainsi

$$I_{\mathrm{alg}}=N(-i).$$

Le théorème d’Ampère donne

$$2\pi rB(r,z)=\mu_0(-Ni),$$

soit

$$\boxed{\vec B=-\frac{\mu_0Ni}{2\pi r}\vec u_\theta}.$$

Le signe moins est lié au sens de l’enroulement représenté.

## Page 11

### Exercice 5 — Solénoïde fini

On considère un solénoïde fini de longueur $L$ comprenant $N$ spires, chacune parcourue par un courant d’intensité $I$ constante. Les spires, circulaires de rayon $R$, sont régulièrement enroulées sur un cylindre de révolution autour de l’axe $(z'z)$.

On cherche à déterminer complètement $\vec B(M)$ en un point $M$ quelconque de l’axe. Le courant et l’axe sont orientés de manière directe, selon la règle du tire-bouchon. Le dessin montre le champ dirigé vers $+Oz$.

**1.** Sur une longueur élémentaire $\mathrm dz$, combien de spires $\mathrm dN$ se trouvent entre les cotes $z$ et $z+\mathrm dz$ ?

La répartition est uniforme : $N$ spires sur $L$, $\mathrm dN$ sur $\mathrm dz$. Donc

$$N\,\mathrm dz=L\,\mathrm dN,\qquad
\boxed{\mathrm dN=\frac NL\,\mathrm dz}.$$

**2.** Calculer le champ élémentaire créé en $M$ par ces $\mathrm dN$ spires.

Pour une seule spire, avec $M$ sur son axe,

$$\vec B_{1\ \mathrm{spire}}(M)=\frac{\mu_0I}{2R}\sin^3\alpha\vec u_z,
\qquad\sin\alpha=\frac R{\sqrt{R^2+z^2}}.$$

$\alpha$ est le demi-angle sous lequel, depuis $M$, on voit la spire ; $z$ désigne ici l’écart axial à cette spire.

Par superposition,

$$
\boxed{\mathrm d\vec B(M)
=\vec B_{1\ \mathrm{spire}}(M)\,\mathrm dN
=\frac{\mu_0IN}{2RL}\sin^3\alpha\,\mathrm dz\vec u_z}.
$$

## Page 12

### Intégration sur le solénoïde

**3.** En déduire $B(z)$ au point $M(z)$. Faire apparaître les angles $\alpha_1$ et $\alpha_2$ sous lesquels on voit, du point $M$, la spire d’entrée et la spire de sortie du solénoïde.

Le dessin place $M$ à gauche du solénoïde et les deux angles entre l’axe et les segments joignant $M$ aux extrémités de l’enroulement.

$$
\vec B(M)=\int_{\mathrm{solénoïde}}\mathrm d\vec B(M)
=\frac{\mu_0IN}{2RL}\vec u_z
\int_{\mathrm{solénoïde}}\sin^3\alpha\,\mathrm dz.
$$

Le vecteur $\vec u_z$ est constant. Posons $K=\int\sin^3\alpha\,\mathrm dz$. La géométrie donne

$$\tan\alpha=\frac Rz,\qquad
z=\frac R{\tan\alpha}=R\frac{\cos\alpha}{\sin\alpha}.$$

Donc

$$
\mathrm dz
=R\frac{-\sin^2\alpha-\cos^2\alpha}{\sin^2\alpha}\,\mathrm d\alpha
=-\frac R{\sin^2\alpha}\,\mathrm d\alpha.
$$

Ainsi

$$
K=\int_{\alpha_1}^{\alpha_2}\sin^3\alpha
\left(-\frac R{\sin^2\alpha}\right)\mathrm d\alpha
=-R\int_{\alpha_1}^{\alpha_2}\sin\alpha\,\mathrm d\alpha
=R(\cos\alpha_2-\cos\alpha_1).
$$

Finalement

$$
\boxed{\vec B(M)=\frac{\mu_0IN}{2L}
(\cos\alpha_2-\cos\alpha_1)\vec u_z}.
$$

Les cosinus et $N$ sont sans dimension ; $[B]=[\mu_0I]/L$.

## Page 13

### Limite du solénoïde infini

**4.** Retrouver l’expression du champ magnétique à l’intérieur d’un solénoïde infiniment long en utilisant le résultat précédent.

$$\alpha_1\longrightarrow\pi,\qquad\alpha_2\longrightarrow0,$$

donc

$$\cos\alpha_2-\cos\alpha_1=1-(-1)=2.$$

Par conséquent,

$$\boxed{\vec B(M)=\mu_0I\frac NL\vec u_z
=\mu_0nI\vec u_z}.$$

$n=N/L$ est le nombre de spires par unité de longueur, en spires par mètre. Le dessin rappelle la correspondance entre le sens du courant dans les spires et le champ suivant $+Oz$.
