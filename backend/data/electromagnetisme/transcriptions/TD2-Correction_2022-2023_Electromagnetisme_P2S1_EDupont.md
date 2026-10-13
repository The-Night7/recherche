---
source: TD2-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 14 (correction manuscrite)
transcription: manuelle
---

# TD2 — Champ électrostatique et théorème de Gauss (corrigé)

> **Note :** la correction suit l'ordre 6, 1, 2, 3, 4, 5, 7, 8 et la numérotation de la feuille 2022-2023, conservés ici. Dans le recueil 2023-2024, ces exercices sont numérotés 9, 2, 3, 4, 7, 8, 5, 6 (l'exercice 1 y est la distribution discrète de charges, corrigée dans le TD1 2022-2023).

## Exercice 6 : Lecture d'une carte de champ

**Énoncé.** (*) On donne ci-contre les lignes de champ électrostatique générées par une distribution de charges ponctuelles. Les charges sont numérotées de 1 à 5 de gauche à droite.

1. Donner le signe de chacune des charges.
2. Déterminer les éventuels plans de symétrie et d'anti-symétrie de la distribution de charge. Exprimer les charges $q_4$ et $q_5$ en fonction des autres.
3. On admet que le champ est nul en tout point de la surface $S$ : comment cela se traduit-il sur les lignes de champ ?
4. En déduire $q_3$ en fonction des autres charges.

> **Note :** la figure est une carte de lignes de champ dans le plan $(xOy)$, pour $x$ et $y$ entre $-4$ et $4\ \mathrm{m}$. Cinq charges sont alignées sur l'axe $y = 0$, aux abscisses $-3$, $-1{,}5$, $0$, $1{,}5$ et $3\ \mathrm{m}$ environ. Une courbe fermée ovale $S$ entoure les charges 2, 3 et 4 ; aucune ligne de champ ne la traverse.

**Correction.**

**1.** Une ligne de champ est tangente à $\vec E$ en chacun de ses points ($\vec E \wedge d\vec\ell = \vec 0$) et orientée dans le sens de $\vec E$. Les lignes de champ **partent** des charges positives et **arrivent** sur les charges négatives. Sur la carte, les lignes partent de $q_1$, $q_2$, $q_4$, $q_5$ et convergent vers $q_3$ :
$$q_1, q_2, q_4, q_5 > 0 \qquad \text{et} \qquad q_3 < 0$$

**2.** La carte de champ est symétrique par rapport au plan $P_1$ ($x = 0$) : ce plan est un plan de **symétrie** de la distribution (une charge et son image sont égales). Le plan $P_2$ ($y = 0$), qui contient toutes les charges, est aussi un plan de symétrie. Il n'y a pas de plan d'antisymétrie. La symétrie par rapport à $P_1$ échange $q_1$ et $q_5$, $q_2$ et $q_4$ :
$$q_5 = q_1 \qquad \text{et} \qquad q_4 = q_2$$

**3.** Si $\vec E = \vec 0$ en tout point de $S$, aucune ligne de champ ne traverse $S$ : les lignes issues de l'intérieur restent à l'intérieur, celles de l'extérieur restent à l'extérieur, et $S$ est une « frontière » qui sépare les deux familles de lignes (les lignes de champ ne se croisent pas).

**4.** *Théorème de Gauss.* Le flux élémentaire de $\vec E$ à travers une surface élémentaire $d\vec S = dS\,\vec n$ est $d\Phi = \vec E \cdot d\vec S$. Pour une surface **fermée** $S_G$ (surface de Gauss) :
$$\Phi(\vec E) = \oint_{S_G} \vec E(M) \cdot d\vec S = \frac{q_{\text{int}}}{\varepsilon_0}$$

où $q_{\text{int}}$ est la somme des charges situées à l'intérieur de $S_G$.

On prend pour surface de Gauss la surface fermée $S$, qui contient $q_2$, $q_3$ et $q_4$. Puisque $\vec E = \vec 0$ sur $S$, $\Phi(\vec E) = 0$, donc $q_{\text{int}} = 0$ :
$$q_2 + q_3 + q_4 = 0$$

Avec $q_4 = q_2$ : $2q_2 + q_3 = 0$, soit
$$q_3 = -2q_2$$

La distribution est donc $(q_1, q_2, -2q_2, q_2, q_1)$, ce qui est cohérent avec $q_3 < 0$.

## Exercice 1 : Symétrie sphérique

**Énoncé.** Soit une sphère, de rayon $R$, chargée uniformément. En commençant par une étude de symétrie et d'invariance, calculer le flux de $\vec E$ à travers la surface $\Sigma$ d'une sphère de rayon $r$ (les deux sphères ont le même centre).

> **Note :** la figure montre la sphère chargée de rayon $R$ et, autour, la sphère $\Sigma$ de rayon $r$, avec les coordonnées sphériques $(r, \theta, \varphi)$ d'un point $M$ de $\Sigma$.

**Correction.**

*Système de coordonnées :* sphériques, $(O, \vec e_r, \vec e_\theta, \vec e_\varphi)$. A priori $\vec E = \vec E(r, \theta, \varphi)$.

*Invariances :* la sphère est uniformément chargée, la distribution est inchangée quand on fait varier $\theta$ et $\varphi$ (rotations autour de $O$) : $\vec E = \vec E(r)$.

*Symétries :* tout plan passant par $M$ et par le centre $O$ est un plan de symétrie de la distribution. Il y en a une infinité ; leur direction commune est $\vec e_r$. Donc
$$\vec E = E(r)\,\vec e_r$$

(comme pour une charge ponctuelle, cas $R \to 0$ : le champ est radial).

*Flux.* Sur $\Sigma$, $d\vec S = dS_r\,\vec e_r$ avec $dS_r = r^2 \sin\theta\,d\theta\,d\varphi$, et $E(r)$ est constant puisque $r$ est fixé :
$$\Phi(\vec E) = \oint_\Sigma E(r)\,\vec e_r \cdot d\vec S = E(r)\,r^2 \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\varphi = 4\pi r^2 E(r)$$

## Exercice 2 : Symétrie cylindrique

**Énoncé.** Soit un cylindre, de rayon $R$ et de hauteur supposée infinie, chargé uniformément. En commençant par une étude de symétrie et d'invariance, calculer le flux de $\vec E$ à travers la surface $\Sigma$ d'un cylindre de rayon $r$ et de hauteur $h$ (les deux cylindres ont le même axe).

> **Note :** la figure montre le cylindre chargé d'axe $(Oz)$ et de rayon $R$, et le cylindre $\Sigma$ de rayon $r$ et de hauteur $h$ (de $z = -h/2$ à $z = h/2$), fermé par deux disques $\Sigma_1$ (en haut) et $\Sigma_2$ (en bas) ; $\Sigma_3$ désigne la surface latérale.

**Correction.**

*Coordonnées :* cylindriques $(O, \vec e_r, \vec e_\theta, \vec e_z)$.

*Invariances :* le cylindre est infini et uniforme ; la distribution est inchangée par translation selon $(Oz)$ et par rotation autour de $(Oz)$ : $\vec E = \vec E(r)$.

*Symétries :* les plans $P_1 = (M, \vec e_r, \vec e_\theta)$ (perpendiculaire à l'axe) et $P_2 = (M, \vec e_r, \vec e_z)$ (contenant l'axe) sont des plans de symétrie. $\vec E$ appartient aux deux, donc à leur direction commune :
$$\vec E = E(r)\,\vec e_r$$

*Flux.* On décompose la surface fermée $\Sigma$ :
$$\Phi(\vec E) = \iint_{\Sigma_1} \vec E \cdot \vec n_1\,dS + \iint_{\Sigma_2} \vec E \cdot \vec n_2\,dS + \iint_{\Sigma_3} \vec E \cdot \vec n_3\,dS$$

Sur les bases, $\vec n_1 = +\vec e_z$ et $\vec n_2 = -\vec e_z$ sont perpendiculaires à $\vec E$ : flux nul. Sur la surface latérale, $\vec n_3 = \vec e_r$ et $dS_r = r\,d\theta\,dz$ :
$$\Phi(\vec E) = \int_{-h/2}^{h/2} \int_0^{2\pi} E(r)\,r\,d\theta\,dz = r\,E(r) \times h \times 2\pi = 2\pi r h\,E(r)$$

## Exercice 3 : Symétrie plane

**Énoncé.** Soit un plan infini chargé uniformément de densité $\sigma$. En commençant par une étude de symétrie et d'invariance, calculer le flux de $\vec E$ à travers la surface $\Sigma$ d'un cylindre de rayon $r$ et de hauteur $h$. L'axe du cylindre est perpendiculaire au plan chargé.

> **Note :** la figure montre le plan chargé $\sigma$ et le cylindre $\Sigma$ d'axe $(Oz)$ perpendiculaire au plan, placé symétriquement ($h/2$ de chaque côté).

**Correction.**

*Coordonnées :* cylindriques $(O, \vec e_r, \vec e_\theta, \vec e_z)$ avec $(Oz)$ perpendiculaire au plan.

*Invariances :* le plan est infini et uniformément chargé ; la distribution est invariante par rotation autour de $(Oz)$ et par translation selon $\vec e_r$ (toute translation parallèle au plan) : $\vec E = \vec E(z)$.

*Symétries :* les plans $P_1 = (M, \vec e_r, \vec e_z)$ et $P_2 = (M, \vec e_\theta, \vec e_z)$, perpendiculaires au plan chargé, sont des plans de symétrie ; $\vec E$ appartient aux deux :
$$\vec E = E(z)\,\vec e_z$$

De plus, le plan chargé lui-même ($z = 0$) est un plan de symétrie : le champ au point symétrique est le symétrique du champ, donc $E(-z) = -E(z)$.

*Flux.* On prend $\Sigma$ entre $z = -h/2$ et $z = +h/2$, avec $\Sigma_1$ la base supérieure ($\vec n_1 = \vec e_z$), $\Sigma_2$ la base inférieure ($\vec n_2 = -\vec e_z$), $\Sigma_3$ la surface latérale ($\vec n_3 = \vec e_r \perp \vec E$, flux nul) :
$$\Phi_1 = \iint_{\Sigma_1} E(h/2)\,dS_z, \qquad \Phi_2 = \iint_{\Sigma_2} E(-h/2)\,\vec e_z \cdot (-\vec e_z)\,dS_z = \iint_{\Sigma_2} E(h/2)\,dS_z = \Phi_1$$

Avec $dS_z = r'\,dr'\,d\theta$ ($r'$ de $0$ à $r$) :
$$\Phi(\vec E) = 2\,E(h/2) \int_0^r r'\,dr' \int_0^{2\pi} d\theta = 2\pi r^2\,E(h/2)$$

où $E(h/2)$ est la valeur du champ du côté $z > 0$.

## Exercice 4 : Distribution linéique de charges

**Énoncé.**

1. Calculer par intégration le champ électrostatique $\vec E$ créé en un point $M$ quelconque de l'espace par une distribution linéique de charges de densité $\lambda$ uniforme et répartie le long de l'axe des $z$.
2. Retrouver ce résultat en calculant $\vec E$ en appliquant le théorème de Gauss.

**Correction.**

**1.** On note $r$ la distance de $M$ à l'axe. Un élément $dz$ du fil, centré en $P$ de cote $z$, porte la charge $dq = \lambda\,dz$ et crée en $M$ (loi de Coulomb)
$$d\vec E = \frac{dq}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3} = \frac{\lambda\,dz}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3}$$

avec $\overrightarrow{PM} = \overrightarrow{PO} + \overrightarrow{OM} = r\,\vec e_r - z\,\vec e_z$ et $PM^2 = r^2 + z^2$ (on a placé l'origine $O$ au pied de la perpendiculaire issue de $M$).

Les plans $P_1 = (M, \vec e_r, \vec e_\theta)$ et $P_2 = (M, \vec e_r, \vec e_z)$ sont des plans de symétrie, donc $\vec E = E_r\,\vec e_r$ : il suffit de sommer les composantes radiales (les composantes selon $\vec e_z$ de deux éléments symétriques par rapport à $P_1$ se compensent).
$$E_r = \frac{\lambda}{4\pi\varepsilon_0}\int_{-\infty}^{+\infty} \frac{r\,dz}{(r^2 + z^2)^{3/2}}$$

*Changement de variable :* $z = r\tan\alpha$, où $\alpha$ est l'angle sous lequel on voit $P$ depuis $M$, $\alpha \in \,]-\frac{\pi}{2}, \frac{\pi}{2}[$. Alors $dz = \dfrac{r\,d\alpha}{\cos^2\alpha}$ (car $\frac{d}{d\alpha}\tan\alpha = 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}$) et $r^2 + z^2 = \dfrac{r^2}{\cos^2\alpha}$, d'où
$$\frac{r\,dz}{(r^2 + z^2)^{3/2}} = \frac{r \cdot r\,d\alpha / \cos^2\alpha}{r^3/\cos^3\alpha} = \frac{\cos\alpha\,d\alpha}{r}$$

$$E_r = \frac{\lambda}{4\pi\varepsilon_0 r}\int_{-\pi/2}^{\pi/2} \cos\alpha\,d\alpha = \frac{\lambda}{4\pi\varepsilon_0 r}\big[\sin\alpha\big]_{-\pi/2}^{\pi/2} = \frac{\lambda}{2\pi\varepsilon_0 r}$$

$$\vec E = \frac{\lambda}{2\pi\varepsilon_0 r}\,\vec e_r$$

**2.**

- *Définition :* $\vec E$ est défini et continu partout sauf sur le fil (où se trouvent les charges).
- *Coordonnées :* cylindriques $(O, \vec u_r, \vec u_\theta, \vec u_z)$.
- *Invariances :* fil infini et uniforme, invariance par translation selon $z$ et par rotation autour de $(Oz)$ : $\vec E(r, \theta, z) = \vec E(r)$.
- *Symétries :* $P_1 = (M, \vec u_r, \vec u_\theta)$ et $P_2 = (M, \vec u_r, \vec u_z)$ sont plans de symétrie : $\vec E = E(r)\,\vec u_r$.

*Surface de Gauss :* elle doit être fermée, de dimensions finies, contenir une partie de la distribution et respecter la géométrie du problème. On prend le cylindre $\Sigma$ d'axe $(Oz)$, de rayon $r$ et de hauteur $h$, formé des bases $S_1$ ($\vec n_1 = +\vec u_z$), $S_2$ ($\vec n_2 = -\vec u_z$) et de la surface latérale $S_3$ ($\vec n_3 = +\vec u_r$). Les flux à travers $S_1$ et $S_2$ sont nuls ($\vec u_r \cdot \vec n = 0$), et
$$\Phi(\vec E) = \iint_{S_3} E(r)\,r\,d\theta\,dz = 2\pi r h\,E(r)$$

*Charge intérieure :* $q_{\text{int}} = \int_0^h \lambda\,dz = \lambda h$.

*Théorème de Gauss :* $2\pi r h\,E(r) = \dfrac{\lambda h}{\varepsilon_0}$, d'où
$$\vec E = \frac{\lambda}{2\pi\varepsilon_0 r}\,\vec u_r$$

On retrouve le même résultat, indépendant de $h$ comme il se doit.

## Exercice 5 : Plan infini uniformément chargé

**Énoncé.** Soit un plan infini uniformément chargé en surface, de densité surfacique de charge $\sigma$, séparant l'espace en deux demi-espaces $z > 0$ et $z < 0$. Appliquer le théorème de Gauss pour calculer le champ électrostatique $\vec E$ engendré par cette distribution en tout point $M$ de l'espace.

> **Note :** la figure montre le plan chargé $\sigma$ (plan $z = 0$) et l'axe $(Oz)$ qui lui est perpendiculaire.

**Correction.**

- *Définition :* la densité est surfacique, donc $\vec E$ est défini et continu partout sauf à la traversée de la surface chargée ($z = 0$), où il subit la discontinuité $\vec E(0^+) - \vec E(0^-) = \dfrac{\sigma}{\varepsilon_0}\vec e_z$ (qu'on retrouvera).
- *Coordonnées :* cylindriques $(O, \vec e_r, \vec e_\theta, \vec e_z)$.
- *Invariances :* distribution uniforme sur un plan infini, invariance par rotation autour de $(Oz)$ et par translation selon $\vec e_r$ : $\vec E = \vec E(z)$.
- *Symétries :* $P_1 = (M, \vec e_r, \vec e_z)$ et $P_2 = (M, \vec e_\theta, \vec e_z)$ sont plans de symétrie : $\vec E = E(z)\,\vec e_z$. Le plan chargé $(z = 0)$ est aussi plan de symétrie, donc $E(-z) = -E(z)$.

*Théorème de Gauss.* Surface de Gauss $S_G$ : cylindre d'axe $(Oz)$, de rayon $r$ et de hauteur $h$, symétrique par rapport au plan ; $S_G = S_1 \cup S_2 \cup S_3$ avec $\vec n_1 = +\vec e_z$ (base en $z > 0$), $\vec n_2 = -\vec e_z$ (base en $z < 0$) et $S_3$ la surface latérale (flux nul car $\vec e_z \cdot \vec e_r = 0$).
$$\Phi_1 = \iint_{S_1} E(z > 0)\,dS_z = \pi r^2\,E(z > 0), \qquad \Phi_2 = \iint_{S_2} E(z < 0)\,\vec e_z \cdot (-\vec e_z)\,dS_z = \Phi_1$$

puisque $E(z < 0) = -E(z > 0)$. Donc $\Phi = 2\pi r^2\,E(z > 0)$.

La charge intérieure est celle du disque de rayon $r$ découpé dans le plan : $q_{\text{int}} = \iint \sigma\,dS = \sigma \pi r^2$. D'où
$$2\pi r^2\,E(z > 0) = \frac{\sigma \pi r^2}{\varepsilon_0} \quad \Longrightarrow \quad E(z > 0) = \frac{\sigma}{2\varepsilon_0}$$

$$\vec E = \frac{\sigma}{2\varepsilon_0}\,\vec e_z \ \ (z > 0), \qquad \vec E = -\frac{\sigma}{2\varepsilon_0}\,\vec e_z \ \ (z < 0)$$

Le champ est uniforme dans chaque demi-espace (pour $\sigma > 0$, il s'éloigne du plan de part et d'autre). *Discontinuité :*
$$E(0^+) - E(0^-) = \frac{\sigma}{2\varepsilon_0} - \Big(-\frac{\sigma}{2\varepsilon_0}\Big) = \frac{\sigma}{\varepsilon_0}$$

> **Note :** la correction trace $E(z)$ : une marche valant $-\frac{\sigma}{2\varepsilon_0}$ pour $z < 0$ et $+\frac{\sigma}{2\varepsilon_0}$ pour $z > 0$, avec un saut de $\frac{\sigma}{\varepsilon_0}$ en $z = 0$.

## Exercice 7 : Sphère uniformément chargée en volume

**Énoncé.** Une sphère de centre $O$ et de rayon $R$ porte une densité volumique de charge uniforme $\rho$.

1. Quelle est l'expression de la charge totale, notée $Q$, contenue dans la sphère ?
2. Calculer le champ électrostatique $\vec E(M)$ en considérant le point $M$ :
    a) à l'intérieur de la sphère : $r < R$ ;
    b) à l'extérieur de la sphère : $r > R$.
3. Le champ est-il continu à la traversée de la sphère ? À commenter.
4. Tracer l'allure de $E(r)$.

**Correction.**

**1.** $\rho = \dfrac{dq}{dV}$ est uniforme :
$$Q = \iiint_{V_R} \rho\,dV = \frac{4}{3}\pi R^3 \rho$$

**2.** La distribution est volumique : $\vec E$ est défini et continu partout. En coordonnées sphériques, la distribution est invariante par rotation ($\theta$, $\varphi$) : $\vec E = \vec E(r)$ ; tout plan passant par $M$ et $O$ est plan de symétrie : $\vec E = E(r)\,\vec e_r$ (radial).

*Surface de Gauss :* la sphère $S_G$ de centre $O$ et de rayon $r$. Comme à l'exercice 1,
$$\Phi(\vec E) = \oint_{S_G} E(r)\,dS_r = 4\pi r^2 E(r) = \frac{q_{\text{int}}}{\varepsilon_0}$$

*Charge intérieure :*

- si $r \ge R$ : toute la boule est à l'intérieur, $q_{\text{int}} = Q = \frac{4}{3}\pi R^3 \rho$ ;
- si $r \le R$ : seule une partie de la charge est intérieure, $q_{\text{int}} = \iiint \rho\,dV = \frac{4}{3}\pi r^3 \rho = \big(\frac{r}{R}\big)^3 Q$.

D'où $E(r) = \dfrac{q_{\text{int}}}{4\pi\varepsilon_0 r^2}$ :

- a) $r < R$ : $E(r) = \dfrac{1}{4\pi\varepsilon_0 r^2} \cdot \dfrac{4}{3}\pi r^3 \rho = \dfrac{\rho\,r}{3\varepsilon_0}$ ;
- b) $r > R$ : $E(r) = \dfrac{1}{4\pi\varepsilon_0 r^2} \cdot \dfrac{4}{3}\pi R^3 \rho = \dfrac{\rho R^3}{3\varepsilon_0 r^2} = \dfrac{Q}{4\pi\varepsilon_0 r^2}$.

À l'extérieur, la boule crée le même champ qu'une charge ponctuelle $Q$ placée en $O$. Homogénéité : $[E] = \frac{[q]}{[\varepsilon_0]L^2}$ et $[\rho\,r] = \frac{[q]}{L^3}L = \frac{[q]}{L^2}$ : c'est cohérent.

**3.** En $r = R$ : $E(R^-) = E(R^+) = \dfrac{\rho R}{3\varepsilon_0}$. Le champ est **continu** à la traversée de la sphère, ce qui est attendu pour une distribution volumique (pas de charge surfacique).

**4.** $E(r)$ croît linéairement de $0$ (en $r = 0$) à $\frac{\rho R}{3\varepsilon_0}$ (en $r = R$), puis décroît en $1/r^2$ vers $0$ quand $r \to \infty$.

## Exercice 8 : Sphère uniformément chargée en surface

**Énoncé.** Une sphère de centre $O$ et de rayon $R$ porte une densité surfacique de charge uniforme $\sigma$.

1. Quelle est l'expression de la charge totale, notée $Q$, contenue dans la sphère ?
2. Calculer le champ électrostatique $\vec E(M)$ en considérant le point $M$ :
    a) à l'intérieur de la sphère : $r < R$ ;
    b) à l'extérieur de la sphère : $r > R$.
3. Le champ est-il continu à la traversée de la sphère ? À commenter.
4. Tracer l'allure de $E(r)$.

**Correction.**

**1.** Sur la sphère ($r = R$), $dS_r = R^2 \sin\theta\,d\theta\,d\varphi$ :
$$Q = \iint \sigma\,dS_r = \sigma R^2 \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\varphi = 4\pi R^2 \sigma$$

**2.** La distribution est surfacique : $\vec E$ est défini et continu partout sauf à la traversée de la surface chargée. Les invariances et symétries sont les mêmes qu'à l'exercice 7 : $\vec E = E(r)\,\vec e_r$. Avec la sphère de Gauss de rayon $r$ :
$$4\pi r^2 E(r) = \frac{q_{\text{int}}}{\varepsilon_0}$$

- a) $r < R$ : la sphère de Gauss ne contient aucune charge, $q_{\text{int}} = 0$, donc $E(r) = 0$ ;
- b) $r > R$ : $q_{\text{int}} = Q = 4\pi R^2 \sigma$, donc $E(r) = \dfrac{4\pi R^2 \sigma}{4\pi\varepsilon_0 r^2} = \dfrac{\sigma}{\varepsilon_0}\dfrac{R^2}{r^2}$.

**3.** **Non** : $E(R^-) = 0$ et $E(R^+) = \dfrac{\sigma}{\varepsilon_0}$. Le champ est discontinu à la traversée de la surface chargée, et le saut vaut $\dfrac{\sigma}{\varepsilon_0}$ (même valeur que pour le plan infini de l'exercice 5).

**4.** $E(r)$ est nul pour $r < R$, saute à $\frac{\sigma}{\varepsilon_0}$ en $r = R$, puis décroît en $1/r^2$.
