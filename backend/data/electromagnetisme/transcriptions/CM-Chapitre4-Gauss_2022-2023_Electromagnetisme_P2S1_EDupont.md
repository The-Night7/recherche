---
source: "PREING2-S1/Electromagnetisme/CM-Chapitre4-Gauss_2022-2023_Electromagnetisme_P2S1_EDupont.pdf"
pages: 15
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des pages rendues et comparaison avec le texte natif ; formules restituées en LaTeX
---

# Électromagnétisme — Chapitre 4 : théorème de Gauss, annoté

## Page 1

Électromagnétisme — Chapitre 4 — Théorème de Gauss.

Physique, 2021-2022. Présentation rédigée par Émilie Dupont (Cergy), emilie.dupont@cyu.fr, CY308. CY Tech, Cergy Paris Université.

**Schéma de couverture.** Un fil de densité linéique $\lambda$ traverse suivant son axe un cylindre de hauteur $h$ et de rayon $r$. Les bases sont $S_1$ et $S_2$, la surface latérale $S_3$. Les normales sortantes $\vec n_1$ et $\vec n_2$ sont axiales et opposées ; $\vec n_3$ est radiale. Le champ $\vec E$ est représenté radialement, notamment au point $M$ de la surface latérale.

La date ci-dessus est celle de la couverture ; le fichier source est classé sous 2022-2023.

## Page 2

### Programme d’électrostatique

1. Force entre deux charges.
2. Champ électrostatique.
3. Théorème de superposition et symétries.
4. Théorème de Gauss.
5. Potentiel électrostatique.
6. Conducteurs en équilibre électrostatique.

## Page 3

### 1.4.1. Flux du champ d’une charge à travers une surface

**Flux élémentaire.** Une surface élémentaire $dS$ est orientée par sa normale unitaire $\vec n$ :

$$d\vec S=\vec n\,dS.$$

Le flux élémentaire du champ $\vec E$ à travers $dS$ est défini par le produit scalaire

$$d\Phi=\vec E\cdot d\vec S=\vec E\cdot\vec n\,dS.$$

Unités : $dS$ en $\mathrm{m^2}$, $d\Phi$ en $\mathrm{V\,m}$ et $\vec E$ en $\mathrm{V\,m^{-1}}$.

**Figure.** La normale $d\vec S$ est perpendiculaire à la petite surface ; le vecteur champ est incliné par rapport à cette normale.

**Annotations.** $\vec n$ est un vecteur unitaire perpendiculaire à la surface. La figure compare les orientations du champ : le flux est maximal pour un champ dirigé suivant la normale, diminue avec l’inclinaison et s’annule pour un champ tangent. Le produit scalaire est souligné.

## Page 4

### Flux total à travers une surface

$$\Phi=\iint_S d\Phi
=\iint_S\vec E\cdot d\vec S
=\iint_S\vec E\cdot\vec n\,dS.$$

La figure rappelle $d\vec S=\vec n\,dS$ et l’inclinaison possible du champ par rapport à la normale.

**Annotation.** Le flux total est la somme continue des flux élémentaires. Un croquis décompose une surface courbe en éléments $dS$ munis de leur normale.

## Page 5

### 1.4.2. Théorème de Gauss

Le flux $\Phi$ du champ $\vec E$ à travers une surface fermée $S$ est proportionnel à la charge $q_{\mathrm{int}}$ contenue dans le volume $V$ délimité par cette surface :

$$\boxed{\Phi=\oiint_S\vec E\cdot d\vec S=\frac{q_{\mathrm{int}}}{\varepsilon_0}.}$$

| Symbole | Grandeur | Unité indiquée |
| --- | --- | --- |
| $\Phi$ | Flux | $\mathrm{V\,m}$ |
| $q_{\mathrm{int}}$ | Charge intérieure | $\mathrm C$ |
| $\varepsilon_0$ | Permittivité absolue du vide | SI |

Les normales de la surface fermée sont orientées vers l’extérieur.

**Annotations.** Choisir une surface de Gauss $S_G$ fermée contenant une portion de la distribution. Souvent, on choisit $S_G$ telle que la norme du champ soit constante sur les parties utiles de la surface (par exemple une sphère). Le croquis distingue la charge totale $Q$ de la charge intérieure $q_{\mathrm{int}}$ ; lorsque toute la distribution est enfermée, $q_{\mathrm{int}}=Q$.

## Page 6

### 1.4.3. Distribution linéique uniformément chargée

La symétrie cylindrique et l’invariance par translation conduisent, en coordonnées cylindriques, à

$$\vec E(M)=E(r)\vec u_r.$$

**Schéma.** Un fil rectiligne infini de densité linéique uniforme $\lambda$ ; $M$ se trouve à distance $r$ du fil.

**Annotations.** Base cylindrique $(\vec u_r,\vec u_\theta,\vec u_z)$ ; les dépendances en $\theta$ et $z$ sont barrées. Pour les symétries, voir le chapitre 3.

## Page 7

### Fil infini — application du théorème de Gauss

On choisit un cylindre fermé coaxial au fil, de rayon $r$ et de hauteur $h$. Il est constitué de la base supérieure $S_1$, de la base inférieure $S_2$ et de la surface latérale $S_3$. Les normales sortantes des bases sont opposées, la normale latérale est radiale.

Le champ est perpendiculaire aux normales des bases :

$$\Phi_1=\iint_{S_1}\vec E\cdot\vec n_1\,dS=0,
\qquad
\Phi_2=\iint_{S_2}\vec E\cdot\vec n_2\,dS=0.$$

Sur la surface latérale :

$$\Phi_3=\iint_{S_3}\vec E\cdot\vec n_3\,dS
=\iint_{S_3}E(r)\,dS
=E(r)\iint_{S_3}dS
=E(r)\,2\pi rh.$$

Ainsi,

$$\Phi=\Phi_1+\Phi_2+\Phi_3=\Phi_3
=\frac{q_{\mathrm{int}}}{\varepsilon_0}
=\frac{\lambda h}{\varepsilon_0}.$$

$$E(r)\,2\pi rh=\frac{\lambda h}{\varepsilon_0}
\quad\Longrightarrow\quad
\boxed{E(r)=\frac{\lambda}{2\pi\varepsilon_0r}.}$$

**Annotations.** $S_G=S_1\cup S_2\cup S_3$ ; $\lambda=dq/d\ell$. Le centre du cylindre est placé à $z=0$, les bases à $z=\pm h/2$, et $\vec n_3=\vec u_r$.

## Page 8

### Fil — détail manuscrit du flux latéral

$$\Phi_3=\iint_{S_3}E(r)\vec u_r\cdot dS_r\vec u_r
=\iint_{S_3}E(r)\,dS_r.$$

Le déplacement élémentaire en coordonnées cylindriques a pour composantes

$$(dr,\ r\,d\theta,\ dz).$$

Les éléments de surface associés sont

$$dS_r=r\,d\theta\,dz,\qquad dS_\theta=dr\,dz,\qquad dS_z=r\,dr\,d\theta.$$

Sur la surface latérale, $r$ est constant, égal au rayon du cylindre :

$$\begin{aligned}
\Phi_3
&=\int_0^{2\pi}\int_{-h/2}^{h/2}E(r)r\,dz\,d\theta\\
&=E(r)r\left(\int_0^{2\pi}d\theta\right)
\left(\int_{-h/2}^{h/2}dz\right)
=2\pi rhE(r).
\end{aligned}$$

La portion de fil enfermée a pour longueur $h$, d’où $q_{\mathrm{int}}=\lambda h$.

## Page 9

### Plan infini uniformément chargé

Un plan infini $\Pi$ porte une densité surfacique uniforme $\sigma$. Les plans de symétrie imposent que le champ soit perpendiculaire à $\Pi$ :

$$\vec E=E_z(x,y,z)\vec k.$$

Les translations selon $x$ et $y$ donnent $\vec E=E_z(z)\vec k$.

On utilise un cylindre fermé traversant le plan, avec deux bases de même aire $S$, symétriques par rapport à $\Pi$. Le champ est tangent à la surface latérale, dont le flux est nul. Les normales des bases sont opposées, et

$$\vec E(-z)=-\vec E(z),\qquad \vec n_2=-\vec n_1.$$

Donc

$$\begin{aligned}
\Phi&=\iint_{S_1}\vec E\cdot\vec n_1\,dS
+\iint_{S_2}\vec E\cdot\vec n_2\,dS
+\iint_{S_3}\vec E\cdot\vec n_3\,dS\\
&=ES+ES+0=2ES,
\end{aligned}$$

et

$$\boxed{E=\frac{\sigma}{2\varepsilon_0}.}$$

> Précision de notation : le support écrit $E(z)S+E(-z)S$. Dans cette ligne, les deux termes sont les composantes suivant les normales sortantes, donc égales ; les composantes suivant le même axe $Oz$ sont, elles, opposées.

**Annotations.** La surface de Gauss est un cylindre de rayon $r$ et de hauteur $h$. Sous le plan, le champ est opposé au champ au-dessus : $E_z(-z)=-E_z(z)$. Les flèches vertes corrigent le sens du champ sous le plan chargé positivement.

## Page 10

### Plan — charge intérieure et discontinuité

Le théorème de Gauss donne

$$\Phi=2ES=\frac{q_{\mathrm{int}}}{\varepsilon_0},\qquad
q_{\mathrm{int}}=\sigma S.$$

La charge intérieure est portée par la portion de plan découpée par le cylindre. Ainsi,

$$2ES=\frac{\sigma S}{\varepsilon_0},\qquad
E(z>0)=\frac{\sigma}{2\varepsilon_0}.$$

**Remarque manuscrite.** Les paramètres arbitraires de $S_G$, ici l’aire $S$, doivent se simplifier et ne pas apparaître dans le champ final.

À la traversée de la surface chargée :

$$E_z(0^+)-E_z(0^-)=\frac{\sigma}{\varepsilon_0}.$$

**Graphe.** $E_z$ vaut $-\sigma/(2\varepsilon_0)$ pour $z<0$ et $+\sigma/(2\varepsilon_0)$ pour $z>0$ : saut de $\sigma/\varepsilon_0$ en $z=0$.

## Page 11

### Boule uniformément chargée

Une boule de rayon $R$, de densité volumique uniforme $\rho$, est centrée en $O$. Sa symétrie sphérique impose

$$\vec E(r)=E(r)\vec u_r.$$

On choisit une sphère de Gauss de rayon $r$ centrée en $O$. Sur cette sphère :

$$\begin{aligned}
\Phi&=\oiint_{S_G}\vec E\cdot d\vec S
=\oiint_{S_G}\vec E\cdot\vec n\,dS\\
&=\oiint_{S_G}E(r)\,dS
=E(r)\oiint_{S_G}dS
=E(r)\,4\pi r^2.
\end{aligned}$$

Ainsi,

$$\Phi=\frac{q_{\mathrm{int}}}{\varepsilon_0}
=\frac{\rho V}{\varepsilon_0}
=E(r)\,4\pi r^2,$$

où $V$ désigne ici le volume chargé enfermé par la surface de Gauss.

**Figure.** Boule de rayon $R$ en rouge et sphère de Gauss de rayon $r$ en bleu, avec le point $M$ sur cette dernière et les axes $x,y,z$.

**Annotation.** $S_G$ est une sphère de rayon $r$ centrée en $O$.

## Page 12

### Boule chargée — champ intérieur et extérieur

**Si $r>R$**, la sphère de Gauss enferme toute la charge $Q=\rho V$ :

$$\boxed{E(r)=\frac{Q}{4\pi\varepsilon_0r^2}.}$$

**Si $r<R$**, elle enferme seulement la charge du volume de rayon $r$ :

$$\boxed{E(r)=\frac{\rho r}{3\varepsilon_0}.}$$

La figure reprend les deux sphères concentriques et leurs rayons $R$ et $r$.

**Calculs manuscrits et correction de coquilles.** Le manuscrit écrit des puissances $R^2$ et $r^2$ pour les volumes, ainsi qu’un résultat extérieur proportionnel à $R^2/r^2$, puis omet $r$ dans une ligne du résultat intérieur. Les volumes et les formules imprimées donnent :

$$Q=\rho\frac{4\pi R^3}{3},\qquad
E(r>R)=\frac{\rho R^3}{3\varepsilon_0r^2},$$

$$q_{\mathrm{int}}(r<R)=\rho\frac{4\pi r^3}{3},\qquad
E(r<R)=\frac{q_{\mathrm{int}}}{\varepsilon_0}\frac1{4\pi r^2}
=\frac{\rho r}{3\varepsilon_0}.$$

Ces expressions corrigées sont signalées ici pour distinguer les coquilles manuscrites des deux résultats imprimés exacts.

## Page 13

### Boule — démarche et calcul du flux

1. Domaine de définition : distribution volumique ; le champ est défini et continu en tout point de l’espace.
2. Coordonnées sphériques et base $(\vec u_r,\vec u_\theta,\vec u_\varphi)$.
3. Invariance suivant $\theta$ et $\varphi$ : la norme ne dépend que de $r$.
4. Tout plan passant par $O$ et $M$ est un plan de symétrie : $\vec E=E(r)\vec u_r$.
5. Application du théorème de Gauss.

Le déplacement élémentaire a pour composantes

$$(dr,\ r\,d\theta,\ r\sin\theta\,d\varphi),$$

d’où, sur une sphère,

$$dS_r=r^2\sin\theta\,d\theta\,d\varphi.$$

À $r$ fixé, $r^2E(r)$ est constant :

$$\begin{aligned}
\Phi&=\oiint_{S_G}E(r)\vec u_r\cdot d\vec S\\
&=\int_0^\pi\int_0^{2\pi}r^2E(r)\sin\theta\,d\varphi\,d\theta\\
&=4\pi r^2E(r)=\frac{q_{\mathrm{int}}}{\varepsilon_0}.
\end{aligned}$$

## Page 14

### Lignes de champ

Les lignes de champ produites par une charge ponctuelle placée en $O$ sont des droites passant par $O$.

**Figure.** Une sphère centrée en $O$, de rayon $r$, est traversée par des lignes de champ radiales, avec des flèches dirigées vers l’extérieur.

Une seconde illustration représente une boule rose accompagnée de trois directions radiales sur fond noir.

## Page 15

### Bibliographie

- [1] Polycopié de cours.
- [2] [CUPGE — CY : Introduction à l’électromagnétisme](https://cpinettes.u-cergy.fr/S3-Electromag.html).
- [3] Wikipédia.
- [4] [Encyclopédie Universalis](https://www.universalis.fr/encyclopedie).
- [5] David Sénéchal, [Histoire des sciences, PHQ399](https://www.physique.usherbrooke.ca/pages/node/7930), Université de Sherbrooke, Québec.
- [6] Pour la suite : [Khan Academy](https://fr.khanacademy.org/science/physics), [Unisciel](http://www.unisciel.fr/etudiants/), etc.
