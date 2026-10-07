---
source: "PREING2-S1/Electromagnetisme/CM-Rappels_2022-2023_Electromagnetisme_P2S1_DPhysique.pdf"
pages: 22
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Rappels — repérage spatial, coordonnées et produits de vecteurs

## Page 1

Chapitre 0 — Repérage spatial. CY Tech, CY Cergy Paris Université.

Source indiquée : polycopié, https://www.equipes.lps.u-psud.fr/PASQUIER/enseignement/mecaS2/Mecanique_chap1_coordonnees.pdf.

## Page 2

### Se repérer dans l'espace

Un labyrinthe vu du dessus illustre trois repérages : coordonnées cartésiennes $(x,y)$, polaires $(r,\theta)$ et abscisse curviligne $s$ le long d'un chemin.

Plan du support : coordonnées cartésiennes ; cylindriques ; sphériques ; applications ; coordonnées intrinsèques ; résumé ; produit scalaire et produit vectoriel. Le menu latéral répète ces rubriques.

## Page 3

### 1. Coordonnées cartésiennes — position

$M(x,y,z)$ a pour vecteur position $\vec r=\overrightarrow{OM}$ :

$$\overrightarrow{OM}=x\vec e_x+y\vec e_y+z\vec e_z.$$

$M'(x+dx,y+dy,z+dz)$ est un point voisin, de position $\vec r+d\vec r$. Déplacement élémentaire :

$$d\vec r=\overrightarrow{MM'}=d\vec\ell=dx\vec e_x+dy\vec e_y+dz\vec e_z.$$

Les vecteurs de base sont constants. Le dessin montre les trois arêtes $dx,dy,dz$ du petit parallélépipède au voisinage de $M$.

## Page 4

### Coordonnées cartésiennes — aire et volume

| Plan (ou tout plan parallèle) | Élément d'aire |
| --- | --- |
| $z=0$ | $dS=d\ell_xd\ell_y=dx\,dy$ |
| $y=0$ | $dS=d\ell_xd\ell_z=dx\,dz$ |
| $x=0$ | $dS=d\ell_yd\ell_z=dy\,dz$ |

Élément de volume : $d\tau=dx\,dy\,dz$.

## Page 5

### 2. Coordonnées cylindriques

Bien adaptées pour repérer un point sur un cylindre. Une photo d'escalier hélicoïdal repère l'angle $\theta(t)$ et la hauteur $z(t)$. Le schéma cylindrique représente la distance $r$ à l'axe, l'angle $\theta$ dans le plan horizontal, la hauteur $z$ et la base locale $(\vec e_r,\vec e_\theta,\vec e_z)$.

## Page 6

### Coordonnées cylindriques — position

$M'$ est ici la projection de $M$ sur le plan horizontal :

$$\overrightarrow{OM}=\overrightarrow{OM'}+\overrightarrow{M'M}=\rho\vec e_\rho+z\vec e_z.$$

Élément différentiel de position :

$$d\vec\ell=d\rho\vec e_\rho+\rho\,d\theta\vec e_\theta+dz\vec e_z.$$

Les trois arêtes infinitésimales du schéma ont pour longueurs $d\rho$, $\rho\,d\theta$, $dz$.

## Page 7

### Coordonnées cylindriques — aire et volume

| Plan local | Élément d'aire |
| --- | --- |
| $(\vec e_\rho,\vec e_\theta)$ | $dS=\rho\,d\rho\,d\theta$ |
| $(\vec e_\rho,\vec e_z)$ | $dS=d\rho\,dz$ |
| $(\vec e_\theta,\vec e_z)$ | $dS=\rho\,d\theta\,dz$ |

Le cadre de volume porte : $d\tau=d\ell_\rho d\ell_\theta d\ell_z=\rho\,d\rho\,dz$.

> Coquille du support : il manque $d\theta$ dans la dernière expression. Le produit des trois longueurs vaut $d\tau=\rho\,d\rho\,d\theta\,dz$.

## Page 8

### 3. Coordonnées sphériques

Bien adaptées pour repérer un point sur une sphère. Le schéma utilise $r$, l'angle polaire $\theta$ depuis l'axe vertical et l'azimut $\varphi$.

Exemple GPS : 11 rue Waldeck-Rousseau, 69006 Lyon ; latitude $45{,}769209^\circ=90^\circ-\theta$ et longitude $4{,}858459^\circ=\varphi$. Rayon de la Terre donné : $r=6400\,\mathrm{km}$.

## Page 9

### Coordonnées sphériques — position

$$\overrightarrow{OM}=r\vec e_r,\qquad d\vec\ell=dr\vec e_r+r\,d\theta\vec e_\theta+r\sin\theta\,d\varphi\vec e_\varphi.$$

Figure d'un élément d'aire sphérique : $\rho=HM=r\sin\theta$, $d\ell_\theta=r\,d\theta$, $d\ell_\varphi=\rho\,d\varphi$, donc $dS=d\ell_\theta d\ell_\varphi=r^2\sin\theta\,d\theta\,d\varphi$.

Référence de la figure : *Électromagnétisme 1 — 1re année*, H. Gié et J.-P. Sarmant, Tec&Doc.

## Page 10

### Coordonnées sphériques — aire et volume

| Plan local | Élément d'aire |
| --- | --- |
| $(\vec e_r,\vec e_\theta)$ | $dS=r\,dr\,d\theta$ |
| $(\vec e_r,\vec e_\varphi)$ | $dS=r\sin\theta\,dr\,d\varphi$ |
| $(\vec e_\theta,\vec e_\varphi)$ | $dS=r^2\sin\theta\,d\theta\,d\varphi$ |

$$d\tau=d\ell_r d\ell_\theta d\ell_\varphi=r^2\sin\theta\,dr\,d\theta\,d\varphi.$$

## Page 11

### 4. Applications

1. Volume d'une sphère pleine de centre $O$ et de rayon $R$.
2. Surface d'une sphère pleine de centre $O$ et de rayon $R$.

Les espaces sous les deux énoncés sont vides dans le PDF ; aucune solution n'y est renseignée.

## Page 12

### 4. Applications — 3) Angle solide

$S$ est une surface dont le signe des faces découle de l'orientation du contour $C$. Le cône $K$ issu de $O$ et s'appuyant sur $C$ découpe sur la sphère de centre $O$, rayon $R$, une aire $\Sigma$. Angle solide sous lequel on voit $S$ depuis $O$ :

$$\Omega=\frac{\Sigma}{R^2}.$$

$\Omega$ est indépendant de $R$. Angle solide élémentaire :

$$d\Omega=d\vec S\cdot\frac{\vec e_r}{r^2},\qquad d\Omega=\sin\theta\,d\theta\,d\varphi\quad\text{en coordonnées sphériques}.$$

Sans dimension ; unité : stéradian (sr). Ensemble de l'espace : $\Omega_0=4\pi$.

## Page 13

### 4. Applications — 4) Angle solide d'un cône de révolution

Le dessin montre deux cônes coaxiaux d'angles $\theta$ et $\theta+d\theta$, issus de $O$, découpant une couronne sphérique. L'angle solide entre les cônes est :

$$\delta\Omega=2\pi\sin\theta\,d\theta.$$

Figure : *Électromagnétisme 1 — 1re année*, H. Gié et J.-P. Sarmant, Tec&Doc. Aucun calcul intégré supplémentaire n'apparaît.

## Page 14

### 5. Coordonnées intrinsèques

« Ce que mesure le compteur kilométrique d'une voiture… » Longueur du chemin entre $\Omega$ et $M$ : $s$, abscisse curviligne, notée $\widehat{\Omega M}$ le long de la trajectoire.

Carte : trajet entre la gare RER de Bures-sur-Yvette ($\Omega$) et le bâtiment 333, avec le point $M$ sur le chemin. Le support pose $\overrightarrow{OM}(t)=\,?$ et définit :

- $\vec u_t$ : vecteur tangent à la trajectoire.
- $\vec u_n$ : vecteur normal à la trajectoire.
- Angle orienté $(\vec u_t,\vec u_n)=+\pi/2$.

Un compteur kilométrique illustre la mesure de $s$.

## Page 15

### 6. Résumé

Dans un plan :

$$\overrightarrow{OM}=x\vec i+y\vec j\quad\text{(cartésiennes)},\qquad \overrightarrow{OM}=r\vec u_r\quad\text{(polaires)},$$

$$\vec u_r=\cos\theta\vec i+\sin\theta\vec j,\qquad \vec u_\theta=-\sin\theta\vec i+\cos\theta\vec j.$$

Dans l'espace :

$$\begin{aligned}
\overrightarrow{OM}&=x\vec i+y\vec j+z\vec k&&\text{(cartésiennes)},\\
\overrightarrow{OM}&=r\vec u_r^{\,\rm plan}+z\vec k&&\text{(cylindriques)},\\
\overrightarrow{OM}&=r\vec u_r^{\,\rm espace}&&\text{(sphériques)}.
\end{aligned}$$

Attention : les deux vecteurs radiaux, dans le plan et dans l'espace, ne sont pas identiques. On peut aussi repérer un point par son abscisse curviligne $s$ (compteur kilométrique).

## Page 16

### 7. Produit scalaire et produit vectoriel

En Mécanique 1 et 2, on modélise les mouvements et leurs causes, les forces, par des vecteurs.

Afin de résoudre les problèmes de mécanique, d'électromagnétisme, etc., on a besoin de projeter les vecteurs sur des directions particulières en utilisant les produits scalaires.

En présence de rotations, on utilise également le produit vectoriel, rencontré souvent en Électromagnétisme 1 et 2 lorsqu'on s'intéresse au champ magnétique.

## Page 17

### Produit scalaire de deux vecteurs

Le produit scalaire mesure l'intensité de la projection d'un vecteur sur l'autre. C'est un nombre positif ou négatif :

$$\vec A\cdot\vec B=\|\vec A\|\,\|\vec B\|\cos\widehat{(\vec A,\vec B)}.$$

Le dessin montre une projection positive pour $\vec B$ et négative pour $\vec C$ sur la direction de $\vec A$. Les flèches projetées sont étiquetées $(\vec A\cdot\vec B)\vec A$ et $(\vec A\cdot\vec C)\vec A$.

> Ces étiquettes supposent $\vec A$ unitaire ; dans le cas général, il faut diviser par $\|\vec A\|^2$. Le produit scalaire peut aussi être nul.

## Page 18

### Produit vectoriel de deux vecteurs

Le produit vectoriel est un vecteur. Sa norme mesure l'aire du parallélogramme construit sur les deux vecteurs :

$$\vec\Pi=\vec A\wedge\vec B=\vec A\times\vec B,\qquad
\|\vec\Pi\|=\|\vec A\|\,\|\vec B\|\left|\sin\widehat{(\vec A,\vec B)}\right|.$$

$\times$ est la notation anglo-saxonne. Le dessin place $\vec\Pi$ perpendiculairement au parallélogramme. Règle des trois doigts de la main droite : $\vec A$, $\vec B$, puis $\vec\Pi$.

## Page 19

### Propriétés des deux produits

| Propriété | Produit scalaire | Produit vectoriel |
| --- | --- | --- |
| Notation | $\vec A\cdot\vec B$ | $\vec\Pi=\vec A\wedge\vec B$ |
| Nature | Scalaire (nombre) | Vecteur |
| Valeur ou norme | $\|\vec A\|\|\vec B\|\cos\widehat{(\vec A,\vec B)}$ | $\|\vec A\|\|\vec B\|\lvert\sin\widehat{(\vec A,\vec B)}\rvert$ |
| Commutation | $\vec B\cdot\vec A=\vec A\cdot\vec B$ | $\vec B\wedge\vec A=-\vec A\wedge\vec B$ |
| Ligne intitulée « Associativité » | $\vec A\cdot(\vec B+\vec C)=\vec A\cdot\vec B+\vec A\cdot\vec C$ | $\vec A\wedge(\vec B+\vec C)=\vec A\wedge\vec B+\vec A\wedge\vec C$ |
| Produit avec lui-même | $\vec A\cdot\vec A=\|\vec A\|^2$ | $\vec A\wedge\vec A=\vec0$ |

> La ligne nommée « Associativité » exprime en réalité la distributivité. Le signe moins du produit vectoriel est mis en évidence dans le support.

## Page 20

### Propriétés — suite et coordonnées

Pour deux vecteurs non nuls :

- $\vec A\cdot\vec B=0$ si et seulement si $\vec A\perp\vec B$.
- $\vec A\wedge\vec B=\vec0$ si et seulement si $\vec A\parallel\vec B$.
- Le support donne le maximum scalaire $\vec A\cdot\vec B=\|\vec A\|\|\vec B\|$ pour des vecteurs parallèles ; ils doivent être **de même sens** pour cette valeur positive.
- La norme du produit vectoriel est maximale, $\|\vec A\wedge\vec B\|=\|\vec A\|\|\vec B\|$, lorsque les vecteurs sont perpendiculaires.

Pour $\vec A=(A_x,A_y,A_z)$ et $\vec B=(B_x,B_y,B_z)$ :

$$\vec A\cdot\vec B=A_xB_x+A_yB_y+A_zB_z.$$

Le support imprime :

$$\vec A\wedge\vec B=\begin{pmatrix}A_yB_z-A_zB_y\\A_xB_z-A_zB_x\\A_xB_y-A_yB_x\end{pmatrix}.$$

> La deuxième composante a le signe inversé. La composante correcte est $A_zB_x-A_xB_z$.

## Page 21

### Produit vectoriel en coordonnées cartésiennes

Base orthonormée directe $(\vec i,\vec j,\vec k)$ :

$$\vec k=\vec i\wedge\vec j,\qquad \vec i=\vec j\wedge\vec k,\qquad \vec j=\vec k\wedge\vec i.$$

Le schéma repère $M(X,Y,Z)$ par ses projections sur les trois axes.

## Page 22

### Produit vectoriel en coordonnées cylindriques

$$\vec u_r=\cos\theta\vec i+\sin\theta\vec j,\qquad \vec u_\theta=-\sin\theta\vec i+\cos\theta\vec j.$$

Dans la base cylindrique directe :

$$\vec k=\vec u_r\wedge\vec u_\theta,\qquad
\vec u_r=\vec u_\theta\wedge\vec k,\qquad
\vec u_\theta=\vec k\wedge\vec u_r.$$

La dernière identité est soulignée par deux flèches. Le schéma représente la base locale en $M$ sur un cylindre.
