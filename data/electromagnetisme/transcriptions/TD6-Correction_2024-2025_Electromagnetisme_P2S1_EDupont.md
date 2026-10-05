---
source: "PREING2-S1/Electromagnetisme/TD6-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf"
pages: 12
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des douze pages ; intégrales et orientations vérifiées ; renvoi au cours et erreurs de formulation conservés et signalés
---

# TD 6 — Champ magnétostatique — correction 2024–2025

## Page 1

### Exercice 1 — Fil rectiligne infiniment long

1. Calculer, par intégration avec la loi de Biot et Savart, le champ magnétique créé en un point $M$ quelconque par un fil rectiligne infiniment long défini par l’axe $(Oz)$.

On choisit les coordonnées cylindriques $(O,\vec u_r,\vec u_\theta,\vec u_z)$. La base est directe ; le courant est orienté selon $+Oz$. $P$ est le point courant du fil, de cote $z=z(P)$ ; $O$ est le projeté de $M$ sur le fil.

Le champ élémentaire est

$$\mathrm d\vec B_P(M)=\frac{\mu_0}{4\pi}
\frac{I\,\mathrm d\vec\ell\wedge\overrightarrow{PM}}{\|\overrightarrow{PM}\|^3}.$$

Attention : le champ du fil idéal n’est pas défini sur le fil. Le champ total vaut

$$
\vec B(M)=\int_{P\in\mathrm{fil}}\mathrm d\vec B_P(M)
=\frac{\mu_0}{4\pi}\int_{P\in\mathrm{fil}}
\frac{I\,\mathrm d\vec\ell(P)\wedge\overrightarrow{PM}}{PM^3}
=\frac{\mu_0}{4\pi}\int_{P\in\mathrm{fil}}
\frac{I\,\mathrm d\vec\ell\wedge\vec u_{PM}}{PM^2}.
$$

$I$ est constant. On a

$$I\,\mathrm d\vec\ell=I\,\mathrm dz\vec u_z,\qquad
\overrightarrow{PM}=-z\vec u_z+r\vec u_r,\qquad PM^2=z^2+r^2.$$

Comme $\vec u_z\wedge\vec u_z=\vec0$ et $\vec u_z\wedge\vec u_r=\vec u_\theta$,

$$
\vec B(M)=\frac{\mu_0I}{4\pi}\int_{-\infty}^{+\infty}
\frac{\mathrm dz\vec u_z\wedge(-z\vec u_z+r\vec u_r)}{(z^2+r^2)^{3/2}}
=\frac{\mu_0I}{4\pi}
\left(\int_{-\infty}^{+\infty}\frac{r\,\mathrm dz}{(z^2+r^2)^{3/2}}\right)\vec u_\theta.
$$

Le vecteur $\vec u_\theta$ en $M$ reste constant quand $z(P)$ varie. On note $K$ l’intégrale scalaire.

## Page 2

### Changement de variable

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



2. Retrouver ce champ magnétique en appliquant le théorème d’Ampère.

L’exemple de contour orienté dessiné donne

$$\oint_C\vec B\cdot\mathrm d\vec\ell
=\mu_0(-I_1+I_2-I_2+I_3)=\mu_0(-I_1+I_3).$$

La normale est orientée par le sens de parcours de $C$. On choisit une ligne de champ où $B$ est constant.

**Définition et continuité :** $\vec B$ est défini et continu sauf sur le fil.

**Invariances de la distribution de courant :**

- Translation selon $\vec u_z$, car le fil est infini : le champ est indépendant de $z$.
- Rotation autour de $Oz$ : ses composantes sont indépendantes de $\theta$.

La dépendance restante est $\vec B(r)$.

## Page 3

### Symétries et théorème d’Ampère

Le plan $\Pi_1=(M,\vec u_r,\vec u_\theta)$ est un plan d’antisymétrie des courants : $\vec B\in\Pi_1$. Le plan $\Pi_2=(M,\vec u_r,\vec u_z)$ est un plan de symétrie : $\vec B\perp\Pi_2$. Donc

$$\vec B=B(r)\vec u_\theta.$$

Les lignes de champ sont des cercles centrés sur le fil. Sur le cercle $C$ de rayon $r$ choisi,

$$\mathrm d\vec\ell=r\,\mathrm d\theta\vec u_\theta,
\qquad I_{\mathrm{enlacés}}=I.$$

Ainsi

$$
\oint_C\vec B\cdot\mathrm d\vec\ell
=\int_{-\pi}^{\pi}B(r)\vec u_\theta\cdot r\,\mathrm d\theta\vec u_\theta
=rB(r)\int_{-\pi}^{\pi}\mathrm d\theta
=2\pi rB(r)=\mu_0I.
$$

$$\boxed{\vec B=\frac{\mu_0I}{2\pi r}\vec u_\theta}.$$

### Exercice 2 — Spire

Calculer, par intégration en utilisant la loi de Biot et Savart, le champ magnétique (direction, sens et module) créé en un point $M$ de l’axe de révolution d’une spire de centre $O$, de rayon $R$, parcourue par un courant d’intensité $I$ constante.

## Page 4

### Spire — Invariances et symétries

Le dessin représente la spire dans le plan $(Oxy)$, avec $M$ sur l’axe de révolution $Oz$, $P$ sur la spire, les bases cylindriques et deux plans contenant $Oz$. L’angle $\alpha$ se situe entre l’axe et le segment $MP$.

On utilise $(O,\vec u_r,\vec u_\theta,\vec u_z)$.

0. **Invariances.** La distribution du courant est invariante par rotation autour de $Oz$, donc les composantes du champ sont indépendantes de $\theta$. Sur l’axe, $r=0$ : elles ne dépendent que de $z$.
1. **Symétries.** Tout plan contenant l’axe de révolution est un plan d’antisymétrie de la distribution du courant. Par exemple,

$$\Pi_1=(M,\vec u_r,\vec u_z),\qquad
\Pi_2=(M,\vec u_\theta,\vec u_z).$$

Le champ appartient aux deux plans ; leur direction commune est $\vec u_z$. Ainsi

$$\boxed{\vec B(M)=B(z)\vec u_z}.$$

2. **Loi de Biot et Savart.**

$$\mathrm d\vec B_P(M)=\frac{\mu_0}{4\pi}
\frac{I\,\mathrm d\vec\ell(P)\wedge\overrightarrow{PM}}{PM^3}.$$

Vérification des dimensions :

$$[\mathrm dB_P]=[B]=[\mu_0]\frac{I L^2}{L^3}
=[\mu_0]\frac IL.$$

## Page 5

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

La seconde intégrale est nulle ; le calcul est détaillé page 6. La base radiale s’écrit

$$\vec u_r=\cos\theta\vec u_x+\sin\theta\vec u_y,$$

On note $I_1=\int_0^{2\pi}\vec u_r\,\mathrm d\theta=\vec0$ et $I_2=\int_0^{2\pi}R\,\mathrm d\theta\vec u_z=2\pi R\vec u_z$.

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

Vérification dimensionnelle : $[B]=[\mu_0][I]L^{-1}$.

Le dessin porte aussi $\tan\alpha=R/OM$ et $\sin\alpha=R/PM$.

## Page 6

### Remarque sur l’intégrale radiale

La base cylindrique locale dépend de $\theta$, alors que $\vec u_x$ et $\vec u_y$ sont fixes :

$$\vec u_r(\theta)=\cos\theta\vec u_x+\sin\theta\vec u_y.$$

Donc

$$
I_1=\int_0^{2\pi}\vec u_r(\theta)\,\mathrm d\theta
=\left(\int_0^{2\pi}\cos\theta\,\mathrm d\theta\right)\vec u_x
+\left(\int_0^{2\pi}\sin\theta\,\mathrm d\theta\right)\vec u_y
=\left[\sin\theta\right]_0^{2\pi}\vec u_x
-\left[\cos\theta\right]_0^{2\pi}\vec u_y
=\vec0.
$$

### Exercice 3 — Solénoïde fini

On considère un solénoïde fini de longueur $L$, comprenant $N$ spires, chacune parcourue par un courant d’intensité $I$ constante. Les spires sont circulaires, de rayon $R$, régulièrement enroulées sur un cylindre de révolution autour de l’axe $(z'z)$.

On cherche à déterminer complètement le champ $\vec B(M)$ en un point $M$ quelconque de l’axe. Le courant et l’axe sont orientés de manière directe selon la règle du tire-bouchon. Une note renvoie à l’exercice 2 et à une « vidéo tournée au Québec », sans autre référence dans le PDF.

Le dessin repère $M$, $P$, les angles $\alpha_1$, $\alpha_2$ et $\alpha$, et une tranche de spires entre $z$ et $z+\mathrm dz$.

1. Quel nombre élémentaire de spires se trouve dans une longueur $\mathrm dz$ ?

La proportionnalité donne

$$L\,\mathrm dN=N\,\mathrm dz,\qquad
\boxed{\mathrm dN=\frac NL\,\mathrm dz}.$$

## Page 7

2. Calculer le champ élémentaire créé en $M$ par ces $\mathrm dN$ spires.

Pour une seule spire,

$$\vec B_{1\ \mathrm{spire}}(M)=\frac{\mu_0I}{2R}\sin^3\alpha\vec u_z,
\qquad\sin\alpha=\frac R{\sqrt{R^2+z^2}}.$$

$R$ est le rayon de la spire et $\alpha$ le demi-angle sous lequel, depuis $M$, on voit la spire. Pour $\mathrm dN$ spires parcourues par le même courant,

$$\boxed{\mathrm d\vec B(M)=\vec B_{1\ \mathrm{spire}}(M)\mathrm dN
=\frac{\mu_0I}{2R}\frac NL\sin^3\alpha\,\mathrm dz\vec u_z}.$$

3. En déduire $B(z)$ au point $M(z)$, en faisant apparaître les angles $\alpha_1$ et $\alpha_2$ de la spire d’entrée et de celle de sortie.

$$
\vec B(M)=\int_{\mathrm{solénoïde}}\mathrm d\vec B(M)
=\frac{\mu_0I}{2R}\frac NL\vec u_z
\int_{\mathrm{solénoïde}}\sin^3\alpha\,\mathrm dz.
$$

On note $K$ cette intégrale. On garde la variable $\alpha$ et on exprime $z(\alpha)$ et $\mathrm dz$ :

$$\sin\alpha=\frac R{PM}=\frac R{\sqrt{R^2+z^2}},\quad
\tan\alpha=\frac Rz,\quad\cos\alpha=\frac z{\sqrt{R^2+z^2}},$$

$$z=\frac R{\tan\alpha}=R\frac{\cos\alpha}{\sin\alpha}.$$

La marge réécrit $\cos\alpha=1/\sqrt{1+x^2}$ avec $x=R/z$ sans dimension. Cette écriture suppose $z>0$, comme sur le dessin considéré ; en général il faut tenir compte du signe de $z$.

## Page 8

### Changement de variable et intégration

Comme $R$ est constant,

$$\mathrm d(\tan\alpha)=\mathrm d\left(\frac Rz\right)
=-\frac R{z^2}\mathrm dz.$$

Par la dérivée d’un quotient,

$$
\frac{\mathrm d}{\mathrm d\alpha}\left(\frac{\sin\alpha}{\cos\alpha}\right)
=\frac{\cos^2\alpha+\sin^2\alpha}{\cos^2\alpha}
=\frac1{\cos^2\alpha}.
$$

Ainsi

$$\frac{\mathrm d\alpha}{\cos^2\alpha}=-\frac R{z^2}\mathrm dz,
\qquad\mathrm dz=-\frac{z^2}{R\cos^2\alpha}\mathrm d\alpha
=\boxed{-\frac R{\sin^2\alpha}\mathrm d\alpha}.$$

D’où

$$
K=\int\sin^3\alpha\,\mathrm dz
=R\int_{\alpha_1}^{\alpha_2}(-\sin\alpha)\,\mathrm d\alpha
=R[\cos\alpha]_{\alpha_1}^{\alpha_2}
=R(\cos\alpha_2-\cos\alpha_1).
$$

$$
\boxed{\vec B(M)=\frac{\mu_0I}{2}\frac NL
(\cos\alpha_2-\cos\alpha_1)\vec u_z}.\tag{I}
$$

Avec $n=N/L$, nombre de spires par unité de longueur, la vérification dimensionnelle donne $[B]=[\mu_0]I L^{-1}$.

4. Retrouver le champ à l’intérieur d’un solénoïde infiniment long avec ce résultat.

Dans cette limite, $\alpha_1\to\pi$, $\alpha_2\to0$, et

$$\cos\alpha_2-\cos\alpha_1=1-(-1)=2.$$

Le dessin étend le solénoïde vers $-\infty$ et $+\infty$, avec $\vec B=B(z)\vec u_z$ et $B(z)>0$.

## Page 9

### Solénoïde infini

$$\boxed{\vec B(M)=\mu_0nI\vec u_z},\qquad n=\frac NL.$$

Le champ est indépendant de $z$ par invariance du solénoïde infini.

5. Retrouver le champ à l’intérieur et à l’extérieur d’un solénoïde infiniment long avec le théorème d’Ampère.

**Seule réponse manuscrite :** « cf CM ». La démonstration n’est pas développée dans ce corrigé.

### Pour aller plus loin — Exercice 4 : tore circulaire

On veut étudier le champ magnétique créé par une distribution de courants présente sur un tore circulaire de rayon $R$, à section circulaire de rayon $a$. $O$ est le centre du tore et $Oz$ son axe de révolution. Une chambre à air gonflée de vélo constitue un tel tore.

La distribution est constituée d’un enroulement d’un grand nombre $N$ de spires jointives circulaires de rayon $a$, sur toute la surface du tore. Le sens du courant est donné par la figure. On néglige l’épaisseur des fils. $M$ est un point quelconque où l’on cherche le champ.

On utilise les coordonnées cylindriques ; a priori $\vec B(M)=B(r,\theta,z)\vec u$, de direction à déterminer.

**1 a. Domaine de définition.** Le champ est continu et défini dans tout l’espace sauf sur les spires. Le corrigé exclut les points appartenant à la surface du tore dans son modèle d’enroulement jointif.

**1 b.** Quelle est la direction de $\vec B$ en $M$ ? Justifier. La réponse se poursuit page suivante.

## Page 10

### Tore — Symétries et invariances

Le dessin en perspective repère le rayon $R$, la section de rayon $a$, un point $M$, sa base cylindrique, un plan méridien $\Pi$ et un contour circulaire $C$.

Tout plan contenant $M$ et l’axe de révolution $Oz$ est un plan de symétrie de la distribution de courant. Pour $M$ hors de l’axe,

$$\Pi=(M,\vec u_r,\vec u_z),\qquad\vec B\perp\Pi,$$

donc $\vec B=B(r,\theta,z)\vec u_\theta$.

**1 c. Champ en $O$.** Il est perpendiculaire à tous les plans méridiens, d’où

$$\boxed{\vec B(O)=\vec0}.$$

La vue de dessus montre ces plans et trois contours : $C_1$ dans le trou central, $C_2$ entourant tout le tore, $C_3$ à l’intérieur de l’enroulement. Les flèches du courant sur la partie supérieure du tore vont vers le centre.

**1 d. Coordonnées et dépendances.** L’axe de révolution $Oz$ est privilégié ; le tore est circulaire. Les coordonnées cylindriques s’imposent par la symétrie du bobinage. La distribution de courant est invariante par rotation autour de $Oz$, donc $B$ est indépendant de $\theta$ :

$$\vec B(M)=B(r,z)\vec u_\theta.$$

Le raisonnement utilise le modèle axisymétrique du bobinage jointif.

## Page 11

### Tore — Calcul par Ampère

À $z$ fixé et $r$ fixé, les lignes de champ sont des cercles centrés sur $Oz$, et la norme du champ y est constante.

2. Montrer que le champ est nul en tout point à l’extérieur du tore.
3. Déterminer le champ à l’intérieur du tore.

Le rappel imprimé parle d’une circulation « le long d’une courbe $C$ fermée ou non, le long de laquelle le module de $B$ reste constant », puis affiche le théorème d’Ampère :

$$\oint_{M\in C}\vec B(M)\cdot\mathrm d\vec\ell(M)
=\mu_0I_{\mathrm{enlacés}}=\mu_0\sum_k\gamma_kI_k.$$

> Précision : le théorème d’Ampère sous cette forme s’applique à un **contour fermé**. Les annotations choisissent effectivement une ligne de champ fermée et le disque $\Sigma$ qu’elle délimite.

Sur ce cercle orienté,

$$\mathrm d\vec\ell=r\,\mathrm d\theta\vec u_\theta,$$

$$
\oint_C\vec B\cdot\mathrm d\vec\ell
=\oint_C B(r,z)\,r\,\mathrm d\theta
=B(r,z)r\int_0^{2\pi}\mathrm d\theta
=2\pi rB(r,z).
$$

À l’extérieur du tore, soit aucun courant ne traverse le disque ($C_1$), soit il y a autant de courants sortants que de courants entrants ($C_2$).

## Page 12

### Tore — Champ extérieur et intérieur

Pour le grand contour extérieur,

$$I_{\mathrm{enlacés}}=0+\sum_{\text{N spires}}(i-i)=0.$$

Donc $B(r,z)=0$ à l’extérieur.

À l’intérieur, on utilise le contour $C_3$ orienté et une surface $\Sigma$ s’appuyant sur ce contour. Le courant enlacé est

$$I_{\mathrm{enlacés}}=\iint_\Sigma\vec j\cdot\mathrm d\vec S,
\qquad\mathrm d\vec S=\mathrm dS\vec n.$$

L’orientation choisie donne $\vec n=+\vec u_z$ ; chaque spire traverse dans le sens négatif, donc

$$I_{\mathrm{enlacés}}=\sum_{\text{N spires}}(-i)=-Ni.$$

Par conséquent,

$$2\pi rB(r,z)=\mu_0(-Ni),\qquad
B(r,z)=-\frac{\mu_0Ni}{2\pi r}.$$

Il n’y a pas de dépendance en $z$. Le module diminue lorsque $r$ augmente. La direction est donnée par la règle de la main droite :

$$\boxed{\vec B=N\left(\frac{\mu_0(-i)}{2\pi r}\right)\vec u_\theta}.$$

> Les sommes manuscrites sont parfois indexées de $0$ à $N$ tout en comptant « $N$ fois ». La somme est ici explicitement prise sur les $N$ spires, conformément au résultat du support.
