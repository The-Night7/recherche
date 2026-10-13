---
source: "PREING2-S1/Electromagnetisme/CM-BIS-Chapitre4_2024-2025_Electromagnetisme_P2S1_ABoumiz.pdf"
pages: 14
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Électromagnétisme — Équations locales de Maxwell, énergie et propagation

## Page 1

Abdelaziz Boumiz — Chapitre 5 : équations locales de l’électromagnétisme. Le nom du fichier indique « Chapitre 4 », mais le titre et les pieds de page portent « Chapitre 5 ».

### I. Introduction

L’électromagnétisme est fondé sur les quatre équations de Maxwell et l’expression de la force de Lorentz. Le champ électromagnétique est solution des quatre équations locales suivantes, dont la justification, l’interprétation et le contenu physique font l’objet du chapitre :

$$\overrightarrow{\operatorname{rot}}\vec E=-\frac{\partial\vec B}{\partial t},\qquad
\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j+\varepsilon_0\mu_0\frac{\partial\vec E}{\partial t},\qquad
\operatorname{div}\vec E=\frac\rho{\varepsilon_0},\qquad\operatorname{div}\vec B=0.$$

Historiquement, ces équations ont été étudiées séparément pour rendre compte de phénomènes physiques donnés. Maxwell les a considérées comme un ensemble indissociable. La mention « Les quatre équations de Maxwell » est répétée, suivie d’un espace vide.

### II. Conservation de la charge

**1) Équation de conservation de la charge.** Soit $\rho$ la densité volumique de charge. La charge totale est $Q(t)=\iiint\rho\,d\tau$. L’équation de conservation est

$$\frac{d\rho}{dt}=-\operatorname{div}\vec j,\qquad\vec j=\rho\vec v.$$

$\vec j$ est la densité de courant, $\rho$ la densité volumique de charge et $\vec v$ la vitesse de la charge élémentaire, supposée constante. Note de notation : le polycopié emploie ici $d\rho/dt$ pour la dérivée temporelle locale $\partial\rho/\partial t$ ; la divergence, scalaire, est parfois égale à un zéro muni à tort d’une flèche dans la source.

## Page 2

L’équation de conservation peut être obtenue par un bilan de charge dans un volume élémentaire ou à partir des équations de Maxwell.

**2) Démonstration à partir du bilan de charge.** Considérons un tube de courant cylindrique de volume $V$, de longueur $dl$ et de section de base $S$. La mention « sens du courant $I$ » est présente, mais l’emplacement du dessin est vide.

La charge contenue dans le tube vaut $Q=\iiint_V\rho\,d\tau$. L’intensité sortante est la charge sortante par unité de temps, soit $-dQ/dt$ :

$$-\frac d{dt}\iiint_V\rho\,d\tau=\iint_{\partial V}\vec j\cdot d\vec S.$$

Par Ostrogradsky :

$$\iint_{\partial V}\vec j\cdot d\vec S=\iiint_V\operatorname{div}\vec j\,d\tau,$$

$$-\frac d{dt}\iiint_V\rho\,d\tau=\iiint_V\operatorname{div}\vec j\,d\tau,
\qquad\frac{d\rho}{dt}=-\operatorname{div}\vec j.$$

**3) Régime permanent.** Toutes les grandeurs sont indépendantes du temps : $d\rho/dt=0$, donc $\operatorname{div}\vec j=0$. La densité de courant est à flux conservatif, l’intensité est la même en tout point d’une branche : régime continu. La loi des nœuds en découle :

$$\oiint\vec j\cdot d\vec S=0\quad\Rightarrow\quad\sum_k i_k=0.$$

## Page 3

La somme des intensités algébriques dans un nœud est égale à zéro.

### III. Les équations de Maxwell et la force de Lorentz

**1) Équations de Maxwell.** Le champ électromagnétique est solution des quatre équations locales :

$$\begin{aligned}
\operatorname{div}\vec B&=0 &&\text{(Maxwell–flux magnétique)},\\
\operatorname{div}\vec E&=\rho/\varepsilon_0 &&\text{(Maxwell–Gauss)},\\
\overrightarrow{\operatorname{rot}}\vec B&=\mu_0\vec j+\varepsilon_0\mu_0\partial_t\vec E &&\text{(Maxwell–Ampère)},\\
\overrightarrow{\operatorname{rot}}\vec E&=-\partial_t\vec B &&\text{(Maxwell–Faraday)}.
\end{aligned}$$

**2) Force de Lorentz.** Le champ $[\vec E(M,t),\vec B(M,t)]$ est créé par les sources $\rho(M',t)$, densité volumique de charge, et $\vec j(M',t)$, densité de courant. Une charge ponctuelle $q$ de vitesse $\vec v$ subit :

$$\vec f=q[\vec E(M,t)+\vec v(M,t)\wedge\vec B(M,t)].$$

**3) Propriétés et conséquences. 3.1) Superposition.** Les équations sont linéaires en $\vec E,\vec B,\vec j,\rho$. Si les sources $(\vec j_1,\rho_1)$ et $(\vec j_2,\rho_2)$ produisent respectivement $(\vec E_1,\vec B_1)$ et $(\vec E_2,\vec B_2)$, les sources $(\vec j_1+\vec j_2,\rho_1+\rho_2)$ produisent $(\vec E_1+\vec E_2,\vec B_1+\vec B_2)$.

**3.2) Validité.** Les équations sont valables dans tous les milieux ; en pratique, on les utilise dans le vide, les plasmas et les métaux.

**3.3) Le champ électromagnétique est une entité indissociable.** Suite page suivante.

## Page 4

Les champs électrique et magnétique sont les composantes d’une entité unique : le champ électromagnétique. En régime permanent, on peut étudier séparément l’électrostatique et la magnétostatique.

Chaque équation caractérise un phénomène :

- création d’un champ électrique par les charges : $\operatorname{div}\vec E=\rho/\varepsilon_0$ ;
- absence de charge magnétique : $\operatorname{div}\vec B=0$ ;
- création d’un champ magnétique par un courant : $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j+\varepsilon_0\mu_0\partial_t\vec E$ ;
- induction électromagnétique.

**3.4) Cohérence.** L’étude groupée des équations rend compte d’autres phénomènes, dont la conservation de la charge. Prenons la divergence de Maxwell–Ampère :

$$\operatorname{div}(\overrightarrow{\operatorname{rot}}\vec B)
=\operatorname{div}(\mu_0\vec j+\varepsilon_0\mu_0\partial_t\vec E)=0.$$

La divergence d’un rotationnel est nulle. Les opérateurs divergence et dérivée temporelle commutent :

$$\operatorname{div}(\varepsilon_0\mu_0\partial_t\vec E)
=\varepsilon_0\mu_0\partial_t(\operatorname{div}\vec E).$$

Avec Maxwell–Gauss, $\operatorname{div}\vec E=\rho/\varepsilon_0$, on obtient $\operatorname{div}\vec j+d\rho/dt=0$. La conservation de la charge est donc contenue dans Maxwell.

**3.5) Constantes et unités.** Deux lignes portent « est la perméabilité magnétique, elle caractérise la faculté d’un matériau à modifier un champ magnétique » et « est la permittivité du vide ». Les expressions qui devraient précéder ces descriptions sont absentes du PDF.

## Page 5

Suite de 3.5 : « est la vitesse de la lumière dans le vide ». L’expression précédant cette description est absente.

### IV. Cas particulier des régimes permanents

Le support pose $\partial/\partial t=0$, $\vec B=\vec0$ et $\vec j=\vec0$, puis écrit :

$$\overrightarrow{\operatorname{rot}}\vec E=\vec0,\qquad\operatorname{div}\vec E=\rho/\varepsilon_0.$$

Note : l’annulation de $\vec B$ et de $\vec j$ est ici une hypothèse électrostatique supplémentaire, pas une conséquence générale du régime permanent.

**1) Conséquences en électrostatique. 1.1) Théorème de Gauss.**

$$\oiint_S\vec E\cdot d\vec S=\iiint_V\operatorname{div}\vec E\,d\tau
=\iiint_V\frac\rho{\varepsilon_0}\,d\tau=\frac{Q_i}{\varepsilon_0}.$$

**1.2) Circulation conservative.** Avec $\overrightarrow{\operatorname{rot}}\vec E=\vec0$ et Stokes : $\oint_\Gamma\vec E\cdot d\vec\ell=0$.

**1.3) Potentiel et équation de Poisson.** $dV=-dC$, où $dC=\vec E\cdot d\vec\ell$ est la circulation élémentaire ;

$$C=V(P)-V(Q)=\int_P^Q\vec E\cdot d\vec\ell.$$

Avec $\vec E=-\overrightarrow{\operatorname{grad}}V$ :

$$\operatorname{div}\vec E=-\operatorname{div}(\overrightarrow{\operatorname{grad}}V)=-\Delta V,
\qquad\Delta V+\rho/\varepsilon_0=0.$$

Le cours donne la solution :

$$V(M)=\frac1{4\pi\varepsilon_0}\iiint_\tau\frac{\rho(P)\,d\tau}{\|\overrightarrow{MP}\|}.$$

Puis il imprime :

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\iiint_\tau\frac{\rho(P)\overrightarrow{MP}\,d\tau}{\|\overrightarrow{MP}\|^3}.$$

Ces expressions sont présentées comme le fondement de l’électrostatique (chapitre 6).

Note : le numérateur de la dernière formule doit utiliser $\overrightarrow{PM}$, ou un signe moins devant $\overrightarrow{MP}$. Le potentiel intégral suppose aussi une condition de référence à l’infini ; ce n’est pas la solution générale sans conditions aux limites.

## Page 6

Sans charges ($\rho=0$), Poisson devient l’équation de Laplace : $\Delta V=0$.

**2) Conséquences en magnétostatique.** Le cas choisi impose $\partial_t=0$ et $\vec E=\vec0$ :

- conservation de la charge : $d\rho/dt=-\operatorname{div}\vec j\Rightarrow\operatorname{div}\vec j=0$ ;
- Maxwell–Gauss : $\operatorname{div}\vec E=\rho/\varepsilon_0\Rightarrow\rho=0$ ;
- Maxwell–Ampère : $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j$ ;
- $\operatorname{div}\vec B=0$, donc $\vec B$ est à flux conservatif :

$$\iiint_V\operatorname{div}\vec B\,d\tau=\oiint_S\vec B\cdot d\vec S=0.$$

**2.1) Ampère.** Par Stokes :

$$\oint_\Gamma\vec B\cdot d\vec\ell=\iint_S\overrightarrow{\operatorname{rot}}\vec B\cdot d\vec S
=\iint_S\mu_0\vec j\cdot d\vec S.$$

**2.2) Potentiel vecteur.** $\operatorname{div}\vec B=0$ implique l’existence d’un champ $\vec A$ tel que $\vec B=\overrightarrow{\operatorname{rot}}\vec A$. Si $\vec A'=\vec A+\overrightarrow{\operatorname{grad}}f$, alors

$$\overrightarrow{\operatorname{rot}}\vec A'=\overrightarrow{\operatorname{rot}}(\vec A+\overrightarrow{\operatorname{grad}}f)=\overrightarrow{\operatorname{rot}}\vec A,$$

puisque le rotationnel d’un gradient est nul. Le cours introduit une condition de jauge pour fixer le potentiel : jauge de Coulomb $\operatorname{div}\vec A=0$ (avec des conditions aux limites appropriées pour l’unicité).

Pour obtenir $\vec A(M)$, on prend le rotationnel :

$$\overrightarrow{\operatorname{rot}}(\overrightarrow{\operatorname{rot}}\vec A)=\overrightarrow{\operatorname{rot}}\vec B.$$

## Page 7

Avec l’identité

$$\overrightarrow{\operatorname{rot}}(\overrightarrow{\operatorname{rot}}\vec A)
=\overrightarrow{\operatorname{grad}}(\operatorname{div}\vec A)-\Delta\vec A,$$

la jauge $\operatorname{div}\vec A=0$ et Maxwell–Ampère, on obtient $\Delta\vec A+\mu_0\vec j=\vec0$.

La solution admise est

$$\vec A(M)=\frac{\mu_0}{4\pi}\iiint_\tau\frac{\vec j(P)}{\|\overrightarrow{MP}\|}\,d\tau.$$

Son rotationnel donne

$$\vec B(M)=\frac{\mu_0}{4\pi}\iiint_\tau\frac{\vec j(P)\wedge\overrightarrow{PM}}{\|\overrightarrow{PM}\|^3}\,d\tau.$$

On retrouve Biot et Savart, loi d’origine expérimentale présentée au début de la magnétostatique (chapitre 6).

### V. Contenus physiques des équations de Maxwell

**1) Gauss.** Le texte appelle « conservation de la charge » la relation $\operatorname{div}\vec E=\rho/\varepsilon_0$ ; il s’agit précisément de Maxwell–Gauss. Avec Ostrogradsky :

$$\Phi=\oiint_S\vec E\cdot d\vec S=\iiint_V\operatorname{div}\vec E\,d\tau
=\iiint_V\frac\rho{\varepsilon_0}\,d\tau=\frac{Q_{\mathrm{int}}}{\varepsilon_0}.$$

Gauss reste valable en électromagnétisme, même si les charges sont en mouvement.

**2) Ampère généralisé.** Pour un contour $C=\Gamma$ bordant $S$, Maxwell–Ampère puis Stokes donnent

$$\oint_\Gamma\vec B\cdot d\vec\ell=\iint_S\overrightarrow{\operatorname{rot}}\vec B\cdot d\vec S
=\iint_S(\mu_0\vec j+\varepsilon_0\mu_0\partial_t\vec E)\cdot d\vec S.$$

$$i=\iint_S\vec j\cdot d\vec S,\qquad
\oint_\Gamma\vec B\cdot d\vec\ell=\mu_0\left(i+\iint_S\varepsilon_0\partial_t\vec E\cdot d\vec S\right).$$

$i_D=\iint_S\varepsilon_0\partial_t\vec E\cdot d\vec S$ est le courant de déplacement.

## Page 8

En régime permanent, on retrouve Ampère classique : $\oint_\Gamma\vec B\cdot d\vec\ell=\mu_0i$.

**3) Flux magnétique conservatif.** Maxwell–flux et Ostrogradsky donnent

$$\oiint_S\vec B\cdot d\vec S=\iiint_V\operatorname{div}\vec B\,d\tau=0.$$

Le flux se conserve à chaque instant à travers toute section d’un tube de champ : $\Phi_1=\Phi_2$. On peut définir le flux traversant un contour $\Gamma$ sans préciser la surface $S$ s’appuyant sur lui.

**4) Maxwell–Faraday et loi de Faraday.** On évalue la circulation $e$ sur un contour fermé $\Gamma$ bordant $S$ :

$$\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B,$$

$$\oint_\Gamma\vec E\cdot d\vec\ell=\iint_S\overrightarrow{\operatorname{rot}}\vec E\cdot d\vec S
=\iint_S(-\partial_t\vec B)\cdot d\vec S=-\frac d{dt}\iint_S\vec B\cdot d\vec S.$$

$$e=\oint_\Gamma\vec E\cdot d\vec\ell,\qquad\Phi=\iint_S\vec B\cdot d\vec S,\qquad e=-\frac{d\Phi}{dt}.$$

En permanent : $e=0$, $\overrightarrow{\operatorname{rot}}\vec E=\vec0$ ; le champ est à circulation conservative et $\vec E=-\overrightarrow{\operatorname{grad}}V$. En régime non permanent, la circulation s’identifie à la f.é.m. induite (suite page 9). Cette dérivation suppose un contour fixe.

## Page 9

La f.é.m. induite sur $\Gamma$ obéit à $e=-d\Phi/dt$, loi dégagée expérimentalement par Faraday en 1831.

### VI. Existence des potentiels $\vec A$ et $V$, jauge de Lorentz, cas de l’ARQS

**1) Rappels mathématiques.**

$$\vec a=\overrightarrow{\operatorname{grad}}f\Rightarrow\overrightarrow{\operatorname{rot}}\vec a=\vec0,
\qquad\vec c=\overrightarrow{\operatorname{rot}}\vec d\Rightarrow\operatorname{div}\vec c=0.$$

Réciproquement, le cours indique qu’un champ de rotationnel nul est le gradient d’au moins un champ scalaire et qu’un champ de divergence nulle est le rotationnel d’au moins un champ vectoriel. Note : ces réciproques globales demandent des hypothèses sur le domaine, non précisées ici.

**2) Définition des potentiels.** De $\operatorname{div}\vec B=0$, on définit $\vec B=\overrightarrow{\operatorname{rot}}\vec A$. Maxwell–Faraday devient

$$\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B=-\partial_t(\overrightarrow{\operatorname{rot}}\vec A),$$

$$\overrightarrow{\operatorname{rot}}(\vec E+\partial_t\vec A)=\vec0.$$

Il existe donc au moins un champ scalaire, noté $-V$ à la page suivante. Le titre mentionne une jauge de Lorentz, mais aucune condition explicite de cette jauge n’est écrite dans cette section.

## Page 10

$V$ est appelé potentiel scalaire :

$$\vec E+\partial_t\vec A=-\overrightarrow{\operatorname{grad}}V,
\qquad\vec E=-\partial_t\vec A-\overrightarrow{\operatorname{grad}}V.$$

En permanent, $\partial_t\vec A=\vec0$ et on retrouve $\vec E=-\overrightarrow{\operatorname{grad}}V$.

### VII. Maxwell dans un conducteur et relations de passage

**1) Dans un conducteur.** Dans le cadre de l’ARQS retenu :

$$\operatorname{div}\vec E=0,\qquad\operatorname{div}\vec B=0,\qquad
\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B,\qquad
\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j.$$

L’ARQS ne diffère des régimes stationnaires que par la prise en compte de l’induction (Maxwell–Faraday).

**2) Relations de passage. 2.1) Champ électrique.**

$$\Delta\vec E=\vec E_2-\vec E_1=\frac\sigma{\varepsilon_0}\vec n_{1\to2}.$$

$\sigma$ est la densité surfacique de charge ; $\vec n_{1\to2}$ la normale unitaire orientée du milieu 1 vers le milieu 2. Seule la composante normale est discontinue ; la composante tangentielle est continue.

**2.2) Champ magnétique.**

$$\Delta\vec B=\vec B_2-\vec B_1=\mu_0\vec j_s\wedge\vec n_{1\to2}.$$

La composante normale est continue, la composante tangentielle discontinue.

### VIII. Densité volumique d’énergie électromagnétique, vecteur de Poynting, conservation de l’énergie

Développement page suivante.

## Page 11

**1) Puissance volumique cédée par le champ à la matière.** Le champ interagit avec les particules chargées et leur fournit de l’énergie. Pour une charge $q$, la puissance de Lorentz est

$$P_L=q(\vec E+\vec v\wedge\vec B)\cdot\vec v=q\vec E\cdot\vec v.$$

**2) Équation locale de conservation de l’énergie.** Par analogie avec les conservations de charge, masse, diffusion et chaleur, on cherche

$$\partial_t e_{\mathrm{em}}+\operatorname{div}\vec\pi=-\vec j\cdot\vec E.$$

$e_{\mathrm{em}}$ est l’énergie volumique du champ ; $\vec\pi$, vecteur de Poynting, donne le sens des échanges d’énergie, notamment par son flux. L’énergie totale dans $V$ vaut

$$E_m(t)=\iiint_Ve_{\mathrm{em}}\,d\tau.$$

**Démonstration.** Rappel de conservation de la charge : $\operatorname{div}\vec j+d\rho/dt=0$. À partir de Maxwell–Ampère :

$$\vec j\cdot\vec E=\frac{\vec E}{\mu_0}\cdot(\overrightarrow{\operatorname{rot}}\vec B-\varepsilon_0\mu_0\partial_t\vec E).$$

Or

$$\operatorname{div}(\vec E\wedge\vec B)
=\vec B\cdot\overrightarrow{\operatorname{rot}}\vec E-\vec E\cdot\overrightarrow{\operatorname{rot}}\vec B
=-\vec B\cdot\partial_t\vec B-\vec E\cdot\overrightarrow{\operatorname{rot}}\vec B.$$

D’où

$$\vec E\cdot\overrightarrow{\operatorname{rot}}\vec B=-\frac12\partial_t B^2-\operatorname{div}(\vec E\wedge\vec B).$$

## Page 12

Le premier calcul de cette page imprime :

$$\vec j\cdot\vec E=-\frac1{2\mu_0}\partial_tB^2-\operatorname{div}(\vec E\wedge\vec B)-\frac{\varepsilon_0}2\partial_tE^2.$$

Note : il manque $1/\mu_0$ devant la divergence dans cette ligne. La ligne suivante du support le rétablit :

$$\partial_t\left(\frac{\varepsilon_0}2E^2+\frac1{2\mu_0}B^2\right)
=-\frac{\operatorname{div}(\vec E\wedge\vec B)}{\mu_0}-\vec j\cdot\vec E.$$

On pose

$$e_{\mathrm{em}}=\frac{\varepsilon_0}2E^2+\frac1{2\mu_0}B^2,\qquad\vec\pi=\frac{\vec E\wedge\vec B}{\mu_0}.$$

Bilan local puis intégral :

$$\partial_t e_{\mathrm{em}}=-\operatorname{div}\vec\pi-\vec j\cdot\vec E,$$

$$\frac\partial{\partial t}\iiint_Ve_{\mathrm{em}}\,d\tau
=-\oiint_{\partial V}\vec\pi\cdot d\vec S-\iiint_V\vec j\cdot\vec E\,d\tau.$$

**Remarque : vitesse de propagation de l’énergie.** Par analogie avec la conservation de la charge, on définit $\vec u=\vec\pi/e_{\mathrm{em}}$.

### IX. Équations de propagation du champ électromagnétique

Une distribution de charges localisées autour de $O$, de densités variables dans le temps (exemple : antenne métallique), est source de champs $\vec E,\vec B$ dans le voisinage de $O$, selon Maxwell–Gauss et Maxwell–Ampère.

**1) Obtention.** On calcule le rotationnel de Maxwell–Faraday.

## Page 13

$$\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B
\Rightarrow\overrightarrow{\operatorname{rot}}(\overrightarrow{\operatorname{rot}}\vec E)
=-\partial_t(\overrightarrow{\operatorname{rot}}\vec B).$$

Or $\overrightarrow{\operatorname{rot}}(\overrightarrow{\operatorname{rot}}\vec E)=\overrightarrow{\operatorname{grad}}(\operatorname{div}\vec E)-\Delta\vec E$, avec $\operatorname{div}\vec E=\rho/\varepsilon_0$ et $\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j+\varepsilon_0\mu_0\partial_t\vec E$ :

$$\overrightarrow{\operatorname{grad}}(\rho/\varepsilon_0)-\Delta\vec E
=-\partial_t(\mu_0\vec j+\varepsilon_0\mu_0\partial_t\vec E).$$

Finalement :

$$\Delta\vec E-\varepsilon_0\mu_0\partial_t^2\vec E
=\frac1{\varepsilon_0}\overrightarrow{\operatorname{grad}}\rho+\mu_0\partial_t\vec j.$$

Pour le champ magnétique :

$$\overrightarrow{\operatorname{rot}}(\overrightarrow{\operatorname{rot}}\vec B)
=\overrightarrow{\operatorname{grad}}(\operatorname{div}\vec B)-\Delta\vec B
=\mu_0\overrightarrow{\operatorname{rot}}\vec j+\varepsilon_0\mu_0\partial_t(\overrightarrow{\operatorname{rot}}\vec E),$$

$$\Delta\vec B-\varepsilon_0\mu_0\partial_t^2\vec B=-\mu_0\overrightarrow{\operatorname{rot}}\vec j.$$

**2) Vide sans charges ni courants.** $\rho=0$, $\vec j=\vec0$ :

$$\Delta\vec E-\varepsilon_0\mu_0\partial_t^2\vec E=\vec0,\qquad
\Delta\vec B-\varepsilon_0\mu_0\partial_t^2\vec B=\vec0.$$

Ce sont les équations de d’Alembert.

### X. Effet de peau dans un conducteur ohmique — longueur de pénétration dans un métal

Un champ pénètre dans un bon conducteur de conductivité $\sigma$. Les électrons accélérés par le champ électrique cèdent une partie de leur énergie cinétique par chocs avec les ions positifs du réseau métallique. L’énergie de l’onde est dissipée par effet Joule, ce qui l’amortit.

## Page 14

On cherche la distance caractéristique d’amortissement ou profondeur de pénétration dans un métal de conductivité $\sigma$, pour des champs sinusoïdaux de pulsation $\omega$ :

$$\vec E=E_0f(x)e^{i(kx-\omega t)}\vec u_z.$$

Maxwell–Faraday donne $\overrightarrow{\operatorname{rot}}\vec E=-\partial_t\vec B$, soit $\vec\nabla\wedge\vec E=i\omega\vec B$. Le support imprime :

$$\vec B=\frac{E_0}\omega[-kf(x)+if'(x)]e^{i(kx-\omega t)}\vec u_z.$$

Note : avec $\vec E$ porté par $\vec u_z$ et dépendant de $x$, le rotationnel est porté par $\vec u_y$ ; le dernier vecteur devrait donc être $\vec u_y$. La direction imprimée est conservée pour identifier l’erreur.

Le texte affirme que les résultats restent valables en géométrie cylindrique : un câble homogène de section circulaire est parcouru par des courants dans une zone superficielle d’épaisseur de quelques $\delta$ ; il indique qu’il ne sert à rien de prendre un rayon nettement supérieur à $\delta$ pour transporter un courant sinusoïdal.

La source se termine ici : elle ne donne ni la suite du calcul de $f(x)$ ni l’expression de $\delta$. Aucun développement manquant n’a été ajouté.
