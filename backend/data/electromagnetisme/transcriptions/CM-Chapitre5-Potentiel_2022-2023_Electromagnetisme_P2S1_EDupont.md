---
source: "PREING2-S1/Electromagnetisme/CM-Chapitre5-Potentiel_2022-2023_Electromagnetisme_P2S1_EDupont.pdf"
pages: 17
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des pages rendues et comparaison avec le texte natif ; formules restituées en LaTeX
---

# Électromagnétisme — Chapitre 5 : potentiel électrostatique, annoté (2022-2023)

## Page 1

Électromagnétisme — Chapitre 5 : potentiel électrostatique.

Physique, 2021-2022. Présentation rédigée par Émilie Dupont (Cergy), emilie.dupont@cyu.fr, CY308. CY Tech, Cergy Paris Université.

**Figure de couverture.** Un volume chargé $v$ contient un élément de volume $dv$ au point $P$. Le point d’observation $M$ se trouve à la distance $r=PM$ ; la contribution au potentiel y est notée $dV$.

La date de couverture est 2021-2022 ; le fichier est classé sous 2022-2023.

## Page 2

### Programme d’électrostatique

1. Force entre deux charges.
2. Champ électrostatique.
3. Théorème de superposition et symétries.
4. Théorème de Gauss.
5. Potentiel électrostatique.
6. Conducteurs en équilibre électrostatique.

**Annotation.** Le potentiel est relié à la tension : $U=V_1-V_2$.

## Page 3

### 1.5.0. Notions mathématiques : le gradient

La variation du champ scalaire $V(M)$ est

$$dV(M)=\sum_{i=1}^3\frac{\partial V}{\partial x_i}\,dx_i
=\overrightarrow{\mathrm{grad}}V\cdot d\overrightarrow{OM}.$$

Le vecteur $\overrightarrow{\mathrm{grad}}V$ est le gradient du champ scalaire $V$ ; le point représente un produit scalaire.

En coordonnées cartésiennes :

$$\overrightarrow{\mathrm{grad}}V
=\frac{\partial V}{\partial x}\vec u_x
+\frac{\partial V}{\partial y}\vec u_y
+\frac{\partial V}{\partial z}\vec u_z,$$

$$d\overrightarrow{OM}=dx\,\vec u_x+dy\,\vec u_y+dz\,\vec u_z,$$

$$dV=\frac{\partial V}{\partial x}dx
+\frac{\partial V}{\partial y}dy
+\frac{\partial V}{\partial z}dz.$$

En coordonnées cylindriques :

$$\overrightarrow{\mathrm{grad}}V
=\frac{\partial V}{\partial r}\vec u_r
+\frac1r\frac{\partial V}{\partial\theta}\vec u_\theta
+\frac{\partial V}{\partial z}\vec u_z,$$

$$d\overrightarrow{OM}=dr\,\vec u_r+r\,d\theta\,\vec u_\theta+dz\,\vec u_z.$$

En coordonnées sphériques :

$$\overrightarrow{\mathrm{grad}}V
=\frac{\partial V}{\partial r}\vec u_r
+\frac1r\frac{\partial V}{\partial\theta}\vec u_\theta
+\frac1{r\sin\theta}\frac{\partial V}{\partial\varphi}\vec u_\varphi,$$

$$d\overrightarrow{OM}=dr\,\vec u_r+r\,d\theta\,\vec u_\theta
+r\sin\theta\,d\varphi\,\vec u_\varphi.$$

Les annotations font correspondre, par des couleurs, les composantes du déplacement et celles du gradient.

**Annotations complémentaires.** $x_1=x$, $x_2=y$, $x_3=z$. Le symbole $\partial/\partial x$ désigne une dérivée partielle.

## Page 4

### Relation entre champ et potentiel

Dans le cas de l’électrostatique, sans déplacement de charges, le champ électrostatique est lié au potentiel par

$$\boxed{\vec E=-\overrightarrow{\mathrm{grad}}V.}$$

Le signe moins est ajouté en rouge sur le document.

Une surface équipotentielle $S$ est une surface telle qu’en tout point $M$ qui lui appartient, $V(M)$ prend la même valeur $V_0$.

**Croquis manuscrit.** Deux courbes équipotentielles distinctes sont notées $V_0$ et $V_1$.

## Page 5

### Gradient normal aux équipotentielles

Le vecteur gradient est normal à la surface équipotentielle passant par $M$ de la fonction scalaire $V(M)$.

Le long d’une équipotentielle :

$$dV=0,\qquad dV(M)=V_0-V_0
=\overrightarrow{\mathrm{grad}}V\cdot d\overrightarrow{OM}=0.$$

Par conséquent,

$$\overrightarrow{\mathrm{grad}}V\perp d\overrightarrow{OM}.$$

**Figure [7].** Une carte de potentiel comporte des courbes équipotentielles. Au point $M$, le déplacement $d\overrightarrow{OM}$ est tangent à une équipotentielle, le gradient $\nabla V=\overrightarrow{\mathrm{grad}}V$ lui est normal, et le champ $\vec E=-\overrightarrow{\mathrm{grad}}V$ est opposé au gradient. Des lignes de champ sont ajoutées en vert, perpendiculairement aux équipotentielles. L’annotation rappelle l’autre notation $\overrightarrow{\mathrm{grad}}V=\nabla V$.

> Coquille manuscrite : après $V(M)=V_0$, une ligne écrit $dV=V_0$. Il faut lire $dV=0$ le long de l’équipotentielle, conformément à l’équation imprimée juste au-dessus.

## Page 6

### Complément sur les lignes de champ et les surfaces équipotentielles

1. En chaque point $M$ d’une ligne de champ, le vecteur $\vec E$ lui est tangent : $\vec E\wedge d\vec\ell=\vec 0$.
2. Une surface équipotentielle est l’ensemble des points où le potentiel est invariant : $V=V_0$ constant, donc $dV=0$.
3. Les lignes de champ sont en tout point perpendiculaires aux équipotentielles, car pour un déplacement sur une équipotentielle, $\vec E\cdot d\vec\ell=-dV=0$.
4. Si le déplacement suit une ligne de champ dans le sens du champ, de $M_1$ vers $M_2$, alors

$$\int_{M_1}^{M_2}\vec E\cdot d\vec\ell>0.$$

Le long d’une ligne de champ, le champ est dirigé vers les potentiels décroissants.

**Exemple : fil infini de densité linéique $\lambda$.** Les équipotentielles sont des cylindres coaxiaux au fil, représentés par des cercles concentriques en vue de dessus. Le champ est radial vers l’extérieur dans la figure. Deux cercles portent $V_1$ et $V_2$, avec $V_2<V_1$ pour le cercle extérieur. Les annotations indiquent le gradient vers le fil et le potentiel décroissant vers l’extérieur. Un autre croquis représente le trajet de $M_1$ à $M_2$ suivant le champ.

## Page 7

### Exemples d’équipotentielles

**Charge ponctuelle positive.** Le champ est radial, suivant $\vec u_r$ ; les équipotentielles sont des sphères concentriques. Les flèches de champ partent de la charge.

**Condensateur plan.** Les deux armatures sont des plans chargés de signes opposés. Les lignes de champ sont des droites perpendiculaires aux armatures, orientées de la plaque positive vers la plaque négative. Les équipotentielles sont des plans parallèles aux armatures.

Figures issues de [7].

## Page 8

### 1.5.1. Énergie potentielle électrique

**Travail de la force électrostatique de Coulomb.** Pour une charge $q$ au point $M$, $\vec F=q\vec E(M)$. Le travail élémentaire est

$$\begin{aligned}
dW&=\vec F\cdot d\vec\ell=q\vec E\cdot d\vec\ell\\
&=-q\overrightarrow{\mathrm{grad}}V\cdot d\vec\ell\\
&=-\overrightarrow{\mathrm{grad}}(qV)\cdot d\vec\ell
=-d(qV).
\end{aligned}$$

Entre $A$ et $B$ :

$$W_{AB}=\int_A^B dW=-\int_A^B d(qV)
=-[qV]_A^B=q[V(A)-V(B)].$$

L’énergie potentielle d’interaction entre une charge $q$ et un champ électrostatique créant le potentiel $V$ est

$$\boxed{E_p=\varepsilon_p=qV+K,}$$

à une constante $K$ près. La force de Coulomb dérive d’une énergie potentielle :

$$\vec F=-\overrightarrow{\mathrm{grad}}\varepsilon_p.$$

**Annotations.** $dW=-dE_p$. Le calcul du travail est détaillé sous la forme $-qV_B-(-qV_A)$ ; on retrouve

$$dW=-d(qV)=-\overrightarrow{\mathrm{grad}}(qV)\cdot d\vec\ell
=-\overrightarrow{\mathrm{grad}}\varepsilon_p\cdot d\vec\ell.$$

## Page 9

### Énergie d’interaction de deux charges ponctuelles

Deux charges $q_1$ et $q_2$ se trouvent en $M_1$ et $M_2$, avec $M_1M_2=r_{12}$.

Énergie potentielle de $q_1$ dans le potentiel créé par $q_2$ :

$$\varepsilon_{p1}=q_1V_2+K
=\frac{q_1q_2}{4\pi\varepsilon_0r_{12}}+K.$$

Énergie potentielle de $q_2$ dans le potentiel créé par $q_1$ :

$$\varepsilon_{p2}=q_2V_1+K
=\frac{q_1q_2}{4\pi\varepsilon_0r_{12}}+K.$$

Donc $\varepsilon_{p1}=\varepsilon_{p2}$.

L’énergie potentielle d’interaction est le travail fourni par un opérateur pour amener les charges depuis des positions infiniment éloignées, où elles n’interagissent pas, jusqu’à des positions de voisinage où chacune est soumise au champ de l’autre :

$$\varepsilon_p=\frac{q_1q_2}{4\pi\varepsilon_0r_{12}}+K
=\varepsilon_{p1}=\varepsilon_{p2}.$$

**Annotations.** Le champ créé par $q_1$ est écrit

$$\vec E_1=\frac{q_1}{4\pi\varepsilon_0r_{12}^2}\vec u_{12}
=-\overrightarrow{\mathrm{grad}}V_1,\qquad
V_1=\frac{q_1}{4\pi\varepsilon_0r_{12}}.$$

La force sur $q_2$ vaut $q_2\vec E_1$ (le manuscrit la note $\vec F_1$).

## Page 10

### 1.5.2. Circulation du champ électrique

**1. Définition.** La circulation $C$ du champ de vecteurs $\vec E$ le long d’un chemin $\Gamma$, orienté de $A$ vers $B$, est

$$C=\int_A^B\vec E\cdot d\vec\ell.$$

La figure représente $d\vec\ell$ tangent au chemin ; l’annotation rappelle le produit scalaire.

**2. Champ d’une charge ponctuelle $q$ en $O$.**

$$\vec E=\frac{q}{4\pi\varepsilon_0r^2}\vec u_r.$$

Le schéma décompose le petit déplacement $\overrightarrow{NM}$ en

$$d\vec\ell=dr\,\vec u_r+r\,d\theta\,\vec u_\theta.$$

La composante angulaire ne contribue pas au produit scalaire. Ainsi,

$$\begin{aligned}
C&=\int_{M_1}^{M_2}dC
=\int_{r_1}^{r_2}\frac{q}{4\pi\varepsilon_0r^2}\,dr\\
&=\int_{r_1}^{r_2}-d\left(\frac{q}{4\pi\varepsilon_0r}\right)
=\frac{q}{4\pi\varepsilon_0r_1}-\frac{q}{4\pi\varepsilon_0r_2}.
\end{aligned}$$

La circulation ne dépend que des positions des points de départ et d’arrivée, et non du chemin suivi : le champ est à circulation conservative.

**Annotation du calcul.**

$$C=\int_{M_1}^{M_2}\frac{q}{4\pi\varepsilon_0r^2}\vec u_r\cdot d\vec\ell
=\int_{r_1}^{r_2}\frac{q}{4\pi\varepsilon_0r^2}\,dr
=-\frac{q}{4\pi\varepsilon_0}\left[\frac1r\right]_{r_1}^{r_2}.$$

## Page 11

### Définition du potentiel électrostatique

Le champ est à circulation conservative et la fonction potentiel électrostatique est définie par

$$\vec E=-\overrightarrow{\mathrm{grad}}V.$$

$\vec E$ s’exprime en $\mathrm{V\,m^{-1}}$, $V$ en volts.

D’après cette relation :

$$C=\int_A^B\vec E\cdot d\vec\ell
=\int_A^B-\overrightarrow{\mathrm{grad}}V\cdot d\vec\ell
=\int_A^B-dV=V(A)-V(B).$$

La circulation $C$ se mesure donc en volts (V).

**Annotations.** $\int_A^B-dV=[-V]_A^B=-V(B)-(-V(A))$. Un croquis rappelle le trajet orienté de $A$ à $B$ et le déplacement tangent $d\vec\ell$.

## Page 12

### 1.5.3. Potentiel d’une ou de plusieurs charges ponctuelles

Une charge $q$ placée en $O$ crée au point $M$, à distance $r=OM$, le potentiel

$$V(M)=\frac{q}{4\pi\varepsilon_0r}+V_0.$$

$V(M)$ est le potentiel en volts ; $V_0$ est une constante d’intégration en volts, généralement choisie nulle ; $r$ est en mètres.

Pour un ensemble de $n$ charges ponctuelles :

$$V(M)=\sum_{i=1}^n\frac{q_i}{4\pi\varepsilon_0r_i}+V_0.$$

Le potentiel est défini et continu en tout point, sauf aux points où se trouvent les charges ponctuelles.

**Annotations.** $V$ est défini à une constante $V_0$ près. Un croquis représente les charges $q_1,q_2,q_3,q_4,q_i$ et un point $M$ ; la distance de $M$ à $q_3$ est notée $r_3$.

## Page 13

### 1.5.4. Potentiel d’une distribution continue — distribution linéique

$$V(M)=\int_{P\in\Gamma}\frac{\lambda\,d\ell}{4\pi\varepsilon_0r}+V_0.$$

**Figure.** Une courbe chargée $\Gamma$ contient un élément $d\ell$ au point $P$ ; le point $M$ est à distance $r=PM$ et reçoit la contribution $dV$.

Dans le cas d’une distribution linéique, le potentiel n’est pas défini sur les points où se trouvent les charges.

## Page 14

### Distributions surfacique et volumique

**c) Distribution surfacique.**

$$V(M)=\iint_{P\in S}\frac{\sigma\,dS}{4\pi\varepsilon_0r}+V_0.$$

**Figure.** Un élément $dS$ de la surface $S$, au point $P$, contribue au potentiel en $M$, situé à la distance $r=PM$.

Le potentiel est défini sur la surface chargée et il est continu à la traversée de cette surface.

**d) Distribution volumique.**

$$V(M)=\iiint_{P\in v}\frac{\rho\,dv}{4\pi\varepsilon_0r}+V_0.$$

**Figure.** Un volume $v$ contient l’élément $dv$ au point $P$ ; $r=PM$ est la distance au point d’observation.

Attention à ne pas confondre $V$, le potentiel, et $v$, le volume. Le support emploie aussi $dV$ pour l’élément de volume dans l’intégrale ; on le note $dv$ ici pour lever cette ambiguïté.

Pour une distribution volumique, le potentiel est défini et continu en tout point de l’espace.

**Annotation pour la surface chargée placée en $z=0$.** $V(0^+)=V(0^-)$.

## Page 15

### 1.5.5. Détermination de $V$ à partir de $\vec E$

**Énoncé.** Un cylindre de rayon $R$ et de hauteur infinie est uniformément chargé avec une densité volumique $\rho$. Déterminer le potentiel créé par ce système.

**Calcul manuscrit.** Par invariance et symétrie,

$$\vec E=E(r)\vec u_r.$$

On utilise un cylindre de Gauss coaxial, de rayon $r$ et de hauteur $h$. Le dessin distingue le rayon physique $R$ du rayon de Gauss $r$ ; les bases portent les normales $\vec n_1,\vec n_2$ et la surface latérale $\vec n_3$. Le champ radial ne traverse que la surface latérale.

$$\begin{aligned}
\Phi&=\oiint_{S_G}\vec E\cdot d\vec S
=\int_0^{2\pi}\int_0^h E(r)r\,dz\,d\theta\\
&=2\pi rhE(r)=\frac{q_{\mathrm{int}}}{\varepsilon_0}.
\end{aligned}$$

La charge intérieure vaut

$$q_{\mathrm{int}}=\begin{cases}
\rho\pi r^2h,&r<R,\\
\rho\pi R^2h,&r>R.
\end{cases}$$

D’où

$$E(r)=\begin{cases}
\dfrac{\rho r}{2\varepsilon_0},&r\le R,\\[4pt]
\dfrac{\rho R^2}{2\varepsilon_0r},&r\ge R.
\end{cases}$$

## Page 16

### Cylindre uniformément chargé — potentiel

Énoncé rappelé : cylindre infini de rayon $R$, uniformément chargé avec une densité volumique $\rho$ ; déterminer le potentiel.

Le champ vaut

$$\vec E(M)=E(r)\vec u_r,\qquad
\vec E(r\ge R)=\frac{\rho R^2}{2\varepsilon_0r}\vec u_r,\qquad
\vec E(r\le R)=\frac{\rho r}{2\varepsilon_0}\vec u_r.$$

Puisque $r$ est la seule variable,

$$E_r=-\frac{\partial V}{\partial r}=-\frac{dV}{dr}.$$

On intègre séparément dans les deux régions :

$$V(r\ge R)=\int-\frac{\rho R^2}{2\varepsilon_0r}\,dr+K,
\qquad
V(r\le R)=\int-\frac{\rho r}{2\varepsilon_0}\,dr+K'.$$

La continuité en $R$ donne

$$V(R^+)=V(R^-)
=-\frac{\rho R^2}{2\varepsilon_0}\ln R+K
=-\frac{\rho R^2}{4\varepsilon_0}+K'.$$

On obtient finalement

$$\boxed{V(r\ge R)=\frac{\rho R^2}{2\varepsilon_0}\ln\left(\frac Rr\right)
-\frac{\rho R^2}{4\varepsilon_0}+K',}$$

$$\boxed{V(r\le R)=-\frac{\rho r^2}{4\varepsilon_0}+K'.}$$

**Annotations.** $\vec E=-\overrightarrow{\mathrm{grad}}V=-(\partial V/\partial r)\vec u_r$. Le potentiel est continu ; la continuité relie $K$ et $K'$, et $K'$ est déterminé par une condition sur $V$.

> Coquille de cette version : dans le dernier encadré imprimé, le potentiel intérieur porte un signe positif. La primitive et la condition de continuité données plus haut imposent le signe négatif restitué ici : $V(r\le R)=-\rho r^2/(4\varepsilon_0)+K'$.

## Page 17

### Bibliographie

- [1] Polycopié de cours.
- [2] [CUPGE — CY : Introduction à l’électromagnétisme](https://cpinettes.u-cergy.fr/S3-Electromag.html).
- [3] Wikipédia.
- [4] [Encyclopédie Universalis](https://www.universalis.fr/encyclopedie).
- [5] David Sénéchal, [Histoire des sciences, PHQ399](https://www.physique.usherbrooke.ca/pages/node/7930), Université de Sherbrooke, Québec.
- [6] Pour la suite : [Khan Academy](https://fr.khanacademy.org/science/physics), [Unisciel](http://www.unisciel.fr/etudiants/), etc.
- [7] Nicolas Menguy, [LP 203 — Champs électrique et magnétique](http://www-ext.impmc.upmc.fr/~menguy/Cours_LP203.html).
