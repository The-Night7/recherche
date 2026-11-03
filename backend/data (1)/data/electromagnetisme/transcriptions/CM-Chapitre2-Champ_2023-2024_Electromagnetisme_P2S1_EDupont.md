---
source: "PREING2-S1/Electromagnetisme/CM-Chapitre2-Champ_2023-2024_Electromagnetisme_P2S1_EDupont.pdf"
pages: 18
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-06
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Électromagnétisme — Chapitre 2 : champ électrostatique (2023–2024)

## Page 1

Électromagnétisme — Chapitre 2 : champ électrostatique.

Physique 2023–2024. Présentation rédigée par Émilie Dupont (Cergy), emilie.dupont@cyu.fr, CY308.

Figure : fil de densité linéique $\lambda$, entouré d’un cylindre de rayon $r$ et de hauteur $h$. Les bases $S_1,S_2$ ont des normales verticales opposées ; la surface latérale $S_3$ a une normale radiale, parallèle au champ $\vec E$ en $M$.

## Page 2

Programme d’électrostatique : 1. Force entre deux charges ; 2. Champ électrostatique (chapitre étudié) ; 3. Théorème de superposition et symétries ; 4. Théorème de Gauss ; 5. Potentiel électrostatique ; 6. Conducteurs en équilibre électrostatique.

## Page 3

### 1.2.1. Unités rationalisées

Loi de Coulomb. Soient $q_1$ en $M_1$ et $q_2$ en $M_2$. La force exercée par $q_1$ sur $q_2$ est

$$\vec F_{1/2}=k\frac{q_1q_2}{r_{12}^2}\vec u_{1\to2}.$$

Force en newtons, charges en coulombs, $r_{12}=M_1M_2$ en mètres ; $\vec u_{1\to2}$ est un vecteur unitaire sans dimension dirigé de $M_1$ vers $M_2$.

$k$ dépend du milieu, en $\mathrm{kg\,m^3\,s^{-4}\,A^{-2}}$. Dans le vide, $k=1/(4\pi\varepsilon_0)=9\times10^9$ en unités SI ; $\varepsilon_0$ est la permittivité absolue du vide.

## Page 4

### 1.2.2. Lignes de champ

Une ligne de champ d’un champ de vecteurs quelconque est une courbe $C$ définie dans l’espace telle qu’en chacun de ses points le vecteur y soit tangent :

$$\vec E\wedge d\vec\ell=\vec0.$$

$d\vec\ell$ est le vecteur élémentaire tangent à la ligne de champ.

| Coordonnées | Composantes de $d\vec\ell$ | Équations des lignes de champ |
| --- | --- | --- |
| Cartésiennes | $(dx,dy,dz)$ | $dx/E_x=dy/E_y=dz/E_z$ |
| Cylindriques | $(d\rho,\rho\,d\theta,dz)$ | $d\rho/E_\rho=\rho\,d\theta/E_\theta=dz/E_z$ |
| Sphériques | $(dr,r\,d\theta,r\sin\theta\,d\varphi)$ | $dr/E_r=r\,d\theta/E_\theta=r\sin\theta\,d\varphi/E_\varphi$ |

## Page 5

Les lignes de champ permettent de visualiser l’allure du champ électrique. Par construction : elles sont tangentes au vecteur $\vec E(\vec r)$ ; elles sont orientées dans le sens de $\vec E(\vec r)$ ; elles ne se croisent jamais.

Exemples : autour d’une charge ponctuelle positive, les lignes sont radiales sortantes ; autour d’une charge négative, elles sont radiales entrantes.

Référence [7] : www.edu.upmc.fr/uel/physique/elecstat/observer/champ/lc.htm

## Page 6

Lignes de champ — exemples [7].

- Dipôle : les lignes vont de la charge $+q$ vers la charge $-q$. La figure donne $\vec E=\vec E_-+\vec E_+$, addition vectorielle des deux champs.
- Deux charges opposées et différentes en valeur absolue : $+2q$ et $-q$ ; une partie des lignes issues de la charge positive rejoint la charge négative, les autres vont vers l’infini.
- Ensemble de deux charges positives égales : lignes sortantes s’écartant de la région intermédiaire ; $E_A<E_B$ ; $E_C=0$ (plan médian), comme indiqué sur la figure. Le point $C$ est au milieu des deux charges.

## Page 7

Deux plans chargés : le champ est uniforme entre les deux plaques. Le dessin montre une plaque supérieure positive et une plaque inférieure négative, avec des flèches parallèles de la première vers la seconde. Aux bords, les lignes s’incurvent (effets de bord). [7]

## Page 8

### 1.2.3. Champ électrostatique d’une distribution continue de charges

**1. Définition.** Si une particule ponctuelle de charge $q$, immobile en un point $M$ de l’espace, est soumise à une force $\vec F$ autre que son poids et nulle si $q$ est nulle, il existe un champ électrostatique $\vec E$ au point $M$ tel que

$$\vec F=q\vec E.$$

$\vec F$ en N, $q$ en C, $\vec E$ en $\mathrm{N\,C^{-1}}$ ou $\mathrm{V\,m^{-1}}$.

**2. Champ créé par une charge ponctuelle.** Une charge $q'$ en $M$ subit, de la part d’une charge $q$ en $P$, la force de Coulomb

$$\vec F=\frac1{4\pi\varepsilon_0}\frac{qq'}{r^2}\vec e_{PM}=\frac1{4\pi\varepsilon_0}\frac{qq'}{PM^3}\overrightarrow{PM}=q'\vec E(M).$$

Les charges $q$ et $q'$ sont en interaction coulombienne.

## Page 9

Champ créé par une charge $q$ en $P$ :

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\frac{q}{r^2}\vec u=\frac1{4\pi\varepsilon_0}\frac{q}{PM^3}\overrightarrow{PM}.$$

$r=PM$ ; $\varepsilon_0$ : permittivité du vide.

Si $q>0$, le champ en $M$ est dirigé de $P$ vers $M$. Si $q<0$, il est dirigé de $M$ vers $P$. Le vecteur unitaire $\vec u$ conserve dans les deux cas le sens $P\to M$.

## Page 10

**3. Champ créé par un ensemble de charges ponctuelles (distribution discrète).**

$$\vec E(M)=\sum_{i=1}^N\frac{q_i}{4\pi\varepsilon_0}\frac{\vec u_i}{r_i^2},\qquad
\vec u_i=\frac{\overrightarrow{P_iM}}{\|\overrightarrow{P_iM}\|}=\frac{\vec r_i}{r_i}.$$

$\vec u_i$ est le vecteur unitaire de la droite $(P_iM)$ dirigé de $P_i$ vers $M$ ; la charge $q_i$ est en $P_i$.

Distribution discrète : ensemble de charges discernables par un observateur, $q_1,q_2,q_3,\ldots,q_n$. Le dessin compare la taille d’un atome ou d’une molécule ($r\approx10^{-10}$ m) à une distance d’observation $d=1$ m.

## Page 11

Jusqu’à présent, nous avons étudié la force et le champ électrostatiques dans le cas des distributions de charges discrètes. Grâce au **principe de superposition**, qui traduit la **linéarité** et l’**additivité** des interactions électrostatiques, il est possible de généraliser les différents résultats précédemment obtenus aux distributions de charges quelconques. [7]

## Page 12

Distribution volumique :

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\iiint_{P\in V}\frac{\overrightarrow{PM}}{PM^3}\rho(P)\,dV.$$

La nouveauté est la densité volumique de charges $\rho(P)$.

Avec $\vec r=\overrightarrow{OM}$ et $\vec r'=\overrightarrow{OP}$ :

$$\vec E(\vec r)=\frac1{4\pi\varepsilon_0}\iiint_{P\in V}\frac{\vec r-\vec r'}{\|\vec r-\vec r'\|^3}\rho(\vec r')\,dV.$$

Le schéma place $P$ dans le volume chargé, $M$ à l’extérieur, et donne $\overrightarrow{PM}=\vec r-\vec r'$.

## Page 13

Contribution élémentaire :

$$d\vec E=\frac{dq}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3}
=\frac{\rho(P)\,dV}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3}.$$

Distribution volumique :

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\iiint_V\frac{\rho(P)}{PM^2}\frac{\overrightarrow{PM}}{PM}\,d\tau.$$

Distribution surfacique :

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\iint_S\frac{\sigma(P)}{PM^2}\frac{\overrightarrow{PM}}{PM}\,dS.$$

Distribution linéique :

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\int_L\frac{\lambda(P)}{PM^2}\frac{\overrightarrow{PM}}{PM}\,d\ell.$$

Annotations : $\rho\,dV=dq$, $\sigma\,dS=dq$, $\overrightarrow{PM}/PM$ est le vecteur unitaire. La notation $d\tau$ désigne ici l’élément de volume. [7]

## Page 14

**4. Champ créé par une distribution linéique.**

$$\vec E(M)=\int_\Gamma d\vec E=\int_{P\in\Gamma}\frac{dq}{4\pi\varepsilon_0r^2}\vec u
=\int_{P\in\Gamma}\frac{\lambda\,dl}{4\pi\varepsilon_0r^2}\vec u,
\qquad\vec u=\frac{\vec r}{r}=\frac{\overrightarrow{PM}}{PM}.$$

On définit la densité linéique :

$$\lambda=\lim_{\Delta l\to0}\frac{\Delta Q}{\Delta l}=\frac{dQ}{dl}\quad\text{en }\mathrm{C\,m^{-1}}.$$

Le schéma montre $dq=\lambda dl$ autour de $P$ sur $\Gamma$, et le champ élémentaire en $M$ dans la direction $PM$. [7]

## Page 15

**5. Champ créé par une distribution surfacique.**

$$\vec E(M)=\iint_Sd\vec E=\iint_{P\in S}\frac{dq}{4\pi\varepsilon_0r^2}\vec u
=\iint_{P\in S}\frac{\sigma\,dS}{4\pi\varepsilon_0r^2}\vec u,
\qquad\vec u=\frac{\vec r}{r}=\frac{\overrightarrow{PM}}{PM}.$$

$$\sigma=\lim_{\Delta S\to0}\frac{\Delta Q}{\Delta S}=\frac{dQ}{dS}\quad\text{en }\mathrm{C\,m^{-2}}.$$

Schémas : charges positives sur un plan ; élément $dq=\sigma dS$ au point $P$ d’une surface courbe et contribution $d\vec E$ en $M$. [7]

## Page 16

**6. Champ créé par une distribution volumique.**

$$\rho=\lim_{\Delta V\to0}\frac{\Delta Q}{\Delta V}=\frac{dQ}{dV}\quad\text{en }\mathrm{C\,m^{-3}}.$$

$$\vec E(M)=\iiint_Vd\vec E=\iiint_{P\in V}\frac{dq}{4\pi\varepsilon_0r^2}\vec u
=\iiint_{P\in V}\frac{\rho\,dV}{4\pi\varepsilon_0r^2}\vec u,
\qquad\vec u=\frac{\vec r}{r}=\frac{\overrightarrow{PM}}{PM}.$$

Schéma : élément de volume autour de $P$, $dq=\rho dV$, et champ élémentaire en $M$. [7]

## Page 17

**Définition et continuité du champ électrostatique.**

- Collection de charges ponctuelles : le champ créé est défini et continu en tout point de l’espace, sauf sur les charges.
- Distribution linéique : le champ créé est défini et continu en tout point de l’espace, sauf sur les points de la distribution.
- Distribution surfacique : le champ créé est défini et continu en tout point de l’espace, sauf sur les points de la distribution ; il est donc discontinu à la traversée de la surface.
- Distribution volumique : le champ créé est défini et continu en tout point de l’espace.

## Page 18

Bibliographie : [1] Polycopié de cours ; [2] CUPGE–CY, Introduction à l’électromagnétisme ; [3] Wikipédia ; [4] Encyclopédie Universalis ; [5] David Sénéchal, « Histoire des sciences », PHQ399, Université de Sherbrooke, QC ; [6] Khan Academy, Unisciel ; [7] Nicolas Menguy, cours LP 203 — Champs électrique et magnétique.
