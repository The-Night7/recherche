---
source: "PREING2-S1/Electromagnetisme/CM-BIS-Chapitre2-Biot-Savart_2024-2025_Electromagnetisme_P2S1_EDupont.pdf"
pages: 35
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Loi de Biot et Savart — superposition, symétries et théorème d’Ampère (2024–2025)

## Page 1

Électromagnétisme — Chapitre 2 : Loi de Biot et Savart, théorème de superposition et symétries.

Physique 2024–2025. Présentation rédigée par Émilie Dupont (Cergy), emilie.dupont@cyu.fr, CY308. Illustration : domaines magnétiques, flèches parallèles au sein de chaque domaine.

Annotation sous le titre : « Théorème d’Ampère ».

## Page 2

Programme de magnétostatique :

- Chapitre 1 : Champ magnétique — Force de Lorentz.
- Chapitre 2 : Loi de Biot et Savart — Théorème de superposition et symétries.
- Chapitre 3 : Équations de Maxwell.

## Page 3

But : calcul du champ magnétique en régime permanent et dans l'approximation des régimes quasi stationnaires (ARQS), régimes lentement variables : magnétostatique.

Le ferromagnétisme et le diamagnétisme ne sont pas au programme. Domaines de Weiss : les schémas montrent des orientations différentes d'un domaine à l'autre puis leur alignement sous un champ extérieur $\vec B_{\rm ext}$. Annotation : $I=\dot Q(t)$. Micrographie NdFeB, échelle $20\,\mu\mathrm m$ ; référence affichée : en.wikipedia.org/wiki/Magnetic_domain.

## Page 4

### 2.2.0 Notion de distribution de courant

**Principe de superposition : distribution discrète.** $N$ particules de charges $q_i$, situées aux points $P_i$, de vitesses $\vec v_i$ :

$$\vec B(M)=\frac{\mu_0}{4\pi}\sum_{i=1}^{N}\frac{q_i\vec v_i\wedge\overrightarrow{P_iM}}{\|\overrightarrow{P_iM}\|^3}.$$

Toutes les charges créent un champ électrique, mais seules les charges en mouvement (courant) créent un champ magnétique.

**Distribution continue.** Le schéma place un élément de charge $dq$ de vitesse $\vec v$ au point $P$ dans le volume $V$. Le vecteur $\overrightarrow{PM}$ relie cet élément au point d'observation $M$ ; sa contribution est $d\vec B(M)$. Annotations : $\rho(P)$, densité ; $d\tau$, volume élémentaire. [3, 4]

## Page 5

Dans un volume infinitésimal $d\tau$ contenant plusieurs types de particules :

$$dq\,\vec v=\sum_\alpha\rho_\alpha q_\alpha\vec v_\alpha\,d\tau,\qquad
\vec j=\sum_\alpha\rho_\alpha q_\alpha\vec v_\alpha.$$

$\rho_\alpha$ : densité de particules de type $\alpha$, de charge $q_\alpha$ ; $\vec v_\alpha$ : vitesse de ces particules. $\vec j$ est la densité de courant, flux de charges par unité de temps. Le dessin distingue trois espèces $\alpha_1,\alpha_2,\alpha_3$ et leurs vitesses.

Distribution volumique quelconque de charges en mouvement :

$$\vec B(M)=\frac{\mu_0}{4\pi}\iiint_V\frac{\vec j(P)\wedge\overrightarrow{PM}}{PM^3}\,d\tau.$$

Annotation : $\rho_\alpha q_\alpha$ est la densité de charge de l’espèce $\alpha$. [2]

## Page 6

### 2.2.1 Loi de Biot et Savart — a) Énoncé

Loi postulée par Jean-Baptiste Biot et Félix Savart (1820) à partir d'observations expérimentales. Un fil filiforme parcouru par un courant $I$ crée en $M$, par son élément $I\,d\vec\ell(P)$ en $P$, le champ élémentaire :

$$d\vec B_P(M)=\frac{\mu_0}{4\pi}\frac{I\,d\vec\ell(P)\wedge\overrightarrow{PM}}{PM^3}.$$

Le sens est celui du produit vectoriel : dans le schéma, $d\vec B_P$ entre dans la feuille. $\mu_0$ est la perméabilité du vide : valeur donnée $\mu_0=4\pi\times10^{-7}\,\mathrm{H\,m^{-1}}$, également en $\mathrm{kg\,m\,A^{-2}\,s^{-2}}$ ou $\mathrm{T\,m\,A^{-1}}$ ($H$ : henry). $\varepsilon_0\mu_0c^2=1$ en SI, $c$ vitesse de la lumière dans le vide.

Le dessin du fil indique $d\tau=dS\,d\ell=dS\,v\,dt$. Annotation : fil filiforme, modèle à une dimension. [2, 3, 4]

## Page 7

### Démonstration et champ total

Avec $d\tau=dS\,d\ell$, $\vec j=j\,d\vec\ell/d\ell$ et $\iint_Sj(P)\,dS=I$ :

$$\begin{aligned}
\vec B(M)&=\frac{\mu_0}{4\pi}\iiint\frac{\vec j(P)\wedge\overrightarrow{PM}}{PM^3}\,d\tau\\
&=\frac{\mu_0}{4\pi}\oint_{\rm circuit}d\ell\iint_S\frac{\vec j(P)\wedge\overrightarrow{PM}}{PM^3}\,dS\\
&=\frac{\mu_0}{4\pi}\oint_{\rm circuit}\frac{\left[\iint_Sj(P)\,dS\right]d\vec\ell\wedge\overrightarrow{PM}}{PM^3}.
\end{aligned}$$

Ainsi :

$$\vec B(M)=\int_{P\in\mathrm{fil}}d\vec B_P(M)
=\frac{\mu_0}{4\pi}\int_{P\in\mathrm{fil}}\frac{I\,d\vec\ell(P)\wedge\overrightarrow{PM}}{PM^3}
=\frac{\mu_0}{4\pi}\int_{P\in\mathrm{fil}}\frac{I\,d\vec\ell\wedge\vec u_{PM}}{r^2},$$

avec $\vec u_{PM}=\overrightarrow{PM}/PM$ et $r=PM$. Le champ magnétique n'est pas défini, donc pas continu, aux points où se trouve un courant filiforme. [2, 3, 4]

Annotations : $I=\iint_S\vec j\cdot d\vec S$ par définition ; calcul de $I$ pour un fil ; sur le fil, $r=0$.

## Page 8

### b) Continuité et discontinuité du champ

- $\vec B(M)$ est continu dans une distribution volumique de courant.
- Il est discontinu sur une nappe de courant surfacique.
- Il diverge sur une distribution linéique de courant.

### c) Transformation des vecteurs axiaux

Le dessin représente un vecteur axial et son image par réflexion : sa composante normale au plan est conservée, sa composante tangentielle change de signe.

Si la distribution de courant possède un plan de symétrie $\Pi$, alors le champ $\vec B$ est perpendiculaire à ce plan aux points du plan. Pour un plan d'antisymétrie $\Pi^*$, il est contenu dans ce plan. Les croquis opposent deux fils de courants de même sens (symétrie) et de sens opposés (antisymétrie). [2, 3, 4]

## Page 9

### 2.2.2 Invariances d'une distribution de courant — a) Densité de courant

L'intensité $I$ est la charge qui traverse une section $S$ du fil par unité de temps : $I=dQ/dt$. En régime permanent, $I$ est indépendant de $t$ ; en ARQS, $I(t)$ varie lentement.

**Courant volumique :**

$$I=\iint_S\vec j\cdot d\vec S=\Phi(\vec j).$$

Charges mobiles identiques de même vitesse : $\vec j=nq\vec v$, où $n$ est la densité de porteurs mobiles de charge $q$ et vitesse $\vec v$.

Plusieurs types de charges : $\vec j=\sum_kn_kq_k\vec v_k$.

Annotations : $[\vec j]=QL^{-2}T^{-1}$, à partir de $\vec j=nq\vec v$ ; $[n]=L^{-3}$, densité de porteurs par unité de volume. L'unité manuscrite $\mathrm{C\,m^{-2}\,s^{-2}}$ est incorrecte : la dimension correcte est $QL^{-2}T^{-1}$, soit $\mathrm{A\,m^{-2}}$. Le produit $\vec j\cdot d\vec S$ est scalaire ; l'ARQS compare des échelles de temps. [2]

## Page 10

**a.2) Courant surfacique.** Une des trois dimensions est très petite devant les deux autres : nappe de courant d'épaisseur négligeable. Vecteur densité surfacique $\vec j_s$ :

$$I=\int_L\vec j_s\cdot(dL\,\vec n),$$

$L$ largeur du fil et $\vec n$ vecteur unitaire perpendiculaire à $L$, dans la nappe, suivant le sens de franchissement.

**a.3) Courant linéique.** Deux dimensions sont très petites devant la troisième : modèle de courant linéique. [2]

## Page 11

### b) Invariances et symétries d'une distribution de courant

Une distribution peut être invariante par translation et/ou rotation autour d'un axe.

**Plan de symétrie $\Pi$.** Pour tous points $M,M'$ symétriques par rapport à $\Pi$, le courant $I\,d\vec\ell(M')$ est le symétrique de $I\,d\vec\ell(M)$.

**Plan d'antisymétrie $\Pi^*$.** Le courant en $M'$ est l'opposé du symétrique du courant en $M$ : $-I\,d\vec\ell(M')$ est le symétrique de $I\,d\vec\ell(M)$. Le schéma compare les éléments de deux fils de part et d'autre du plan. [2]

## Page 12

### c) Conservation de la charge et loi des nœuds

$Q$ est la charge contenue à l'intérieur de la surface fermée $S$ :

$$-\frac{dQ}{dt}=I_{\rm sortant}=\oiint_S\vec j\cdot d\vec S.$$

En régime permanent, pour toute surface fermée :

$$\oiint_S\vec j\cdot d\vec S=0.$$

Le courant est constant le long d'un fil. Au nœud $N$ du schéma, $I_1$ entre, $I_2$ et $I_3$ sortent : $I_1=I_2+I_3$. Annotations : en régime permanent, $-dQ/dt=0$ ; somme des courants sortants = somme des courants entrants. [2]

## Page 13

### 2.2.3 Direction de $\vec B$ en un point d'un plan de symétrie ou d'antisymétrie — a) Symétries

Distribution de courant symétrique par rapport à $\Pi$ :

1. En tout point $M$ de $\Pi$, $\vec B(M)$ est perpendiculaire à $\Pi$.
2. Si $M,M'$ sont symétriques par rapport à $\Pi$, $\vec B(M')$ est l'opposé du symétrique de $\vec B(M)$.

Les contributions des éléments $I\,d\vec\ell$ placés en $P,P'$ annulent leurs composantes tangentielles lorsque $M$ appartient au plan. Les annotations encadrent $\vec B\perp\Pi$. [2]

## Page 14

### b) Antisymétries

Distribution antisymétrique par rapport à $\Pi^*$ :

1. Le champ en tout point du plan appartient à $\Pi^*$ (le support dit « colinéaire à $\Pi^*$ »).
2. Pour $M,M'$ symétriques, $\vec B(M')$ est le symétrique de $\vec B(M)$.

Annotation : $\vec B\in\Pi^*$.

### c) Invariances

- Translation suivant $(Oz)$ : champ indépendant de $z$ ; de même suivant $(Ox)$ ou $(Oy)$.
- Rotation autour de $(Oz)$ : $B(M)=\|\vec B(M)\|$ indépendant de $\theta$ en coordonnées cylindriques.
- Rotation autour du point $O$ : norme indépendante de $\theta$ et $\varphi$ en coordonnées sphériques centrées en $O$. [2]

## Page 15

### Symétries et antisymétries — récapitulatif

1. La direction du champ en $M$ est orthogonale à tout plan de symétrie de la distribution passant par $M$ : $\vec B\perp\Pi$.
2. Le champ en $M$ est inclus dans tout plan d'antisymétrie passant par $M$ : $\vec B\in\Pi^*$.
3. Deux plans d'antisymétrie distincts passant par $M$ donnent pour direction du champ leur droite d'intersection.

Schéma : circuit rectangulaire fermé parcouru par $I$ ; deux plans d'antisymétrie $\Pi',\Pi''$ se coupent selon l'axe portant $\vec B$. Les annotations repèrent la direction commune et la règle du tire-bouchon ; vue d'un fil, $I$ entrant ou sortant donne des sens de rotation opposés. [2]

> L'annotation finale écrit $\vec B\in(\Pi'\cup\Pi'')$ ; l'intersection $\Pi'\cap\Pi''$ est requise, conformément à la propriété 3 et au dessin.

## Page 16

### Exemple : fil rectiligne infini parcouru par $I$

Symétrie axiale : coordonnées cylindriques $(r,\theta,z)$ autour du fil $(Oz)$. Invariance par rotation : la norme ne dépend pas de $\theta$ ; invariance par translation : elle ne dépend pas de $z$.

Les lignes de champ sont circulaires, de norme constante sur chaque cercle :

$$\vec B(r)=B(r)\vec e_\theta.$$

Annotations : $I\,d\vec\ell=I\,dz\,\vec e_z$ ; $\overrightarrow{PM}=\overrightarrow{OM}+\overrightarrow{PO}$ ; $\vec e_z\wedge\vec e_r=\vec e_\theta$, $\vec e_z\wedge\vec e_z=\vec0$. Le plan $(M,\vec e_r,\vec e_z)$ est un plan de symétrie ; le plan $(M,\vec e_r,\vec e_\theta)$ est d'antisymétrie. La direction obtenue est orthoradiale. [2]

## Page 17

### d) Lignes et tubes de champ

Une ligne de champ de $\vec B$ est une courbe tangente en tous ses points $M$ à $\vec B(M)$. Un tube de champ est un ensemble de lignes s'appuyant sur un contour fermé $C$.

Deux lignes ne peuvent se couper, sauf en un point où $B=0$. Le support indique que les lignes sont fermées et tournent autour des sources de $\vec B$ (courants), selon la règle de la main droite ou du tire-bouchon.

Exemple : fil infini à courant uniforme, $\vec B=B(r)\vec e_\theta$. Pour $r=r_1$, $B(r_1)$ est constant ; les lignes sont des cercles concentriques autour du fil. [1, 2]

> La fermeture des lignes décrit les exemples illustrés ; $\operatorname{div}\vec B=0$ ne garantit pas que toute ligne de champ quelconque soit une courbe fermée.

## Page 18

### Exemples de lignes de champ

- **Aimant :** spectre de limaille et lignes sortant du pôle nord, rentrant au pôle sud à l'extérieur de l'aimant.
- **Spire :** deux vues de sens de courant opposés ; on « voit » respectivement le pôle nord et le pôle sud. Les lignes traversent l'axe de la spire puis se referment autour d'elle.
- **Solénoïde :** nombreuses spires jointives, champ axial à l'intérieur, lignes de retour à l'extérieur. [2]

## Page 19

### 2.2.4 Flux de $\vec B$ — Théorème d'Ampère — a) Contours et surfaces orientés

Un contour fermé $C$ borde une surface $\Sigma$ de forme quelconque. On oriente le contour et la surface de manière cohérente. Les dessins montrent un disque et une surface bombée de même bord, pour les deux orientations possibles.

Annotation : la normale $\vec n$ sort de la surface dans le sens défini par l'orientation positive du contour, suivant la règle du tire-bouchon. [3]

## Page 20

### b) Flux du champ magnétique à travers une surface

$$\phi=\iint_S\vec B\cdot d\vec S=\iint_S\vec B\cdot\vec n\,dS.$$

$\vec n$ est la normale unitaire à l'élément $dS$ ; le point désigne un produit scalaire. Si $\vec B$ et $\vec n$ ont le même sens, $\phi>0$ ; s'ils sont opposés, $\phi<0$. Le schéma montre deux normales locales sur une surface bordée par un contour orienté. [3]

## Page 21

### Flux à travers une surface fermée

Théorème de Green–Ostrogradski, pour $\Sigma=\partial V$ :

$$\oiint_\Sigma\vec B\cdot d\vec S=\iiint_V\operatorname{div}\vec B\,d\tau=0.$$

Forme locale, en tout point de l'espace : $\operatorname{div}\vec B=0$ (équation de Maxwell).

**Conséquence 1 :** $\vec B$ est à flux conservatif. Le flux est constant entre les sections d'un même tube de champ. Pour un contour fermé $C$ fixé, le flux à travers toute surface délimitée par $C$ est le même, avec orientations cohérentes.

**Conséquence 2 :** il n'existe pas de monopôle magnétique dans ce modèle. Le dessin représente un tube dont les sections ont des aires différentes.

## Page 22

### c) Circulation du champ magnétique

$$\mathcal C=\int_\Gamma\vec B\cdot d\vec\ell.$$

Le sens de $d\vec\ell$ dépend de l'orientation de $\Gamma$. Si $\Gamma$ est une ligne de champ orientée dans le sens du champ, $\vec B\cdot d\vec\ell=B\,d\ell$ ; pour $B$ constant sur sa longueur $L$ :

$$\mathcal C=\int_\Gamma B\,d\ell=BL.$$

Annotations : contour $\Gamma$ orienté, $\vec B$ tangent et de norme constante pour cette simplification. [3]

## Page 23

### d) Théorème d'Ampère

La circulation le long d'une courbe où le module de $\vec B$ est constant peut aider à déterminer le champ. André-Marie Ampère (1775–1836), mathématicien et physicien.

En régime permanent, ou dans l'ARQS magnétique utilisée ici, pour tout contour **fermé** $C$ :

$$\oint_C\vec B(M)\cdot d\vec\ell(M)=\mu_0 I_{\rm enlacés}=\mu_0\sum_k\gamma_k I_k,$$

$\gamma_k=+1$ ou $-1$ selon le sens du courant relativement à l'orientation du contour (règle de la main droite ou du tire-bouchon). Le schéma donne $I_{\rm enlacés}=I_1+I_3-I_2$.

La circulation de $\vec B$ n'est pas conservative en général, contrairement à celle de $\vec E$ en électrostatique ; $\vec B$ ne dérive donc pas en général d'un potentiel scalaire. [3]

## Page 24

### Distribution volumique de courant

En régime permanent et dans l'ARQS utilisée dans le cours, pour tout contour fermé $C$ et toute surface $S$ délimitée par $C$ :

$$\oint_C\vec B\cdot d\vec\ell=\mu_0 I_{\rm enlacés}=\mu_0\iint_S\vec j\cdot d\vec S.$$

Le sens de $d\vec S$ est fixé par celui de $d\vec\ell$, suivant la main droite. Forme locale :

$$\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j.$$

Le courant algébrique est positif s'il traverse $S$ dans le sens de sa normale. Exemple dessiné : $I_2$ traverse deux fois en sens opposés,

$$\oint_C\vec B\cdot d\vec\ell=\mu_0(-I_1+I_2-I_2+I_3)=\mu_0(-I_1+I_3).$$

[2, 3]

Annotations : courant $I_4$ extérieur au contour, donc non enlacé ; seuls les franchissements de la surface comptent.

## Page 25

### 2.2.5 Exemples — méthode d'application du théorème d'Ampère

1. Choisir un système de coordonnées adapté ; analyser symétries et invariances pour déterminer direction et dépendances du champ.
2. Choisir un contour fermé $C$ passant par $M$, où la circulation est simple : généralement $\vec B\perp d\vec\ell$ ou $\vec B\parallel d\vec\ell$.
3. Calculer le courant enlacé $I_{\rm enlacé}$.
4. Écrire $\oint_C\vec B(P)\cdot d\vec\ell(P)=\mu_0I_{\rm enlacé}$ et en déduire $\vec B(M)$.

[2]

## Page 26

### a) Loi d'Ohm locale

$$\vec j=\gamma\vec E.$$

$\vec E$ : champ électrostatique ($\mathrm{V\,m^{-1}}$ ou $\mathrm{N\,C^{-1}}$) ; $\vec j$ : densité de courant ; $\gamma$ : coefficient de conductivité dépendant du milieu et de la température ; $1/\gamma$ : résistivité en $\Omega\,\mathrm m$.

$$\vec j=nq\vec v=\rho_m\vec v,\qquad I=\int di=\iint_S\vec j\cdot d\vec S.$$

$nq=\rho_m$ est la densité volumique de charge des porteurs mobiles de vitesse $\vec v$. Annotation : $I=\Phi(\vec j)=\iint_S\vec j\cdot d\vec S$ dans le conducteur.

> Le texte imprimé donne « Siemens » pour l'unité de $\gamma$. Il faut $\mathrm{S\,m^{-1}}$ pour la conductivité volumique ; le siemens seul est l'unité de conductance. [2]

## Page 27

### Loi d'Ohm locale ou globale ? Force de Laplace

Résistance d'un conducteur de section $S$ :

$$R=\frac{V_A-V_B}{I}=\frac{\displaystyle\int_A^B\vec E\cdot d\vec\ell}{\displaystyle\iint_S\vec j\cdot d\vec S}.$$

La force de Laplace est subie par un conducteur parcouru par un courant dans un champ magnétique :

$$d\vec F_\ell=I\,d\vec\ell\wedge\vec B,\qquad \frac{d\vec F_\ell}{d\tau}=\vec j\wedge\vec B.$$

Le dessin montre les forces élémentaires sur les côtés d'un cadre parcouru par un courant. [2]

Annotations : $\vec E=-\overrightarrow{\operatorname{grad}}V=\vec j/\gamma$, $d\tau=dS\,d\ell$ et

$$\Delta V=V_A-V_B=\int_B^A\overrightarrow{\operatorname{grad}}V\cdot d\vec\ell=-\int_B^A\vec E\cdot d\vec\ell=-\int_B^A\frac{\vec j}{\gamma}\cdot d\vec\ell.$$

## Page 28

### b) Fil rectiligne infini — invariances

Le fil est modélisé par un cylindre infini de rayon $R$, axe $(Oz)$, parcouru par $I$. Coordonnées cylindriques $(r,\theta,z)$ et base $(\vec u_r,\vec u_\theta,\vec u_z)$.

1. La distribution de courant est invariante par rotation autour de $(Oz)$ : $B$ indépendant de $\theta$.
2. Elle est invariante par translation suivant $\vec u_z$ : $B$ indépendant de $z$.

Le graphique annoté donne

$$B(r\le R)=\frac{\mu_0 I}{2\pi}\frac r{R^2},\qquad B(r\ge R)=\frac{\mu_0 I}{2\pi r},\qquad B(R)=\frac{\mu_0I}{2\pi R}.$$

Le champ est continu en $R$, croît linéairement à l'intérieur et décroît en $1/r$ à l'extérieur. Le texte imprimé affiche la formule extérieure $\vec B=\mu_0I\vec e_\theta/(2\pi r)$. [2]

## Page 29

### Fil rectiligne — symétries et contour d'Ampère

Tout plan $\Pi=(M,\vec u_r,\vec u_z)$ contenant $M$ et l'axe est un plan de symétrie, donc $\vec B\perp\Pi$ :

$$\vec B=B(r)\vec u_\theta.$$

À $r$ constant, $B(r)$ est constant ; les lignes de champ sont des cercles autour de $(Oz)$. Le plan $(M,\vec u_r,\vec u_\theta)$ est d'antisymétrie et contient $\vec B$.

Contour $C$ : cercle de rayon $r$ centré sur l'axe. Théorème d'Ampère :

$$\oint_C\vec B\cdot d\vec\ell=\mu_0I_{\rm enlacé}=\mu_0\iint_S\vec j\cdot d\vec S.$$

Le dessin distingue $C_1$ pour $r>R$ et $C_2$ pour $r<R$, avec la surface bordée par chaque contour. [2]

## Page 30

### Fil rectiligne — calcul du champ

$$\oint_C\vec B\cdot d\vec\ell=\int_0^{2\pi}B(r)r\,d\theta=2\pi rB(r),\qquad B(r)=\frac{\mu_0I_{\rm enlacé}}{2\pi r}.$$

Densité volumique uniforme $\vec j=j\vec u_z$ :

- $r>R$ : $I_{\rm enlacé}=I_{\rm total}=I=j\pi R^2$, le courant étant nul hors du cylindre. Donc $B(r)=\mu_0I/(2\pi r)$.
- $r<R$ : $I_{\rm enlacé}=j\pi r^2=Ir^2/R^2$, puisque $j=I/(\pi R^2)$. Donc $B(r)=\mu_0Ir/(2\pi R^2)$.

Les schémas montrent les disques de rayons $r$ et $R$. Annotation : $B$ continu sur tout l'espace. [2]

## Page 31

### c) Expériences sur le champ magnétique et les courants

Le titre est accompagné d'une zone d'image corrompue (bandes colorées, également observées avec deux moteurs de rendu). Le contenu visuel de l'expérience n'est pas récupérable dans ce PDF ; aucun contenu n'est reconstitué par supposition. [2]

## Page 32

### d) Solénoïde

Solénoïde rectiligne infini, parcouru par un courant $I$. Le texte utilise $N$, puis $n$, pour le nombre de spires par unité de longueur.

$$\vec B_{\rm extérieur}=\vec0,\qquad \vec B_{\rm intérieur}=\mu_0nI\vec u.$$

$\vec u$ est le vecteur unitaire de l'axe orienté selon le courant par la règle de la main droite ou du tire-bouchon. Le dessin montre le champ intérieur parallèle à l'axe $(Oz)$.

## Page 33

### d) Solénoïde — suite

Espace ligné vide : aucun calcul n'est renseigné.

## Page 34

### d) Solénoïde — suite

Espace ligné vide : aucun calcul n'est renseigné. [2]

## Page 35

Bibliographie  - [1] Polycopié de cours - [2] CUPGE - CY : Introduction à l’électromagnétisme - [3] Cours LP 203 - Champs électrique et magnétique de Nicolas MENGUY - [4] Cours de Luc Tremblay, collège Mérici - « Électricité et magnétisme ». - [5]  David Sénéchal - « Histoire des sciences » PHQ399 Université de Sherbrooke, QC - [6]  pour la suite : Khan Academy , Unisciel  etc.
