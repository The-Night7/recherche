---
source: "PREING2-S1/Electromagnetisme/CM-BIS-Chapitre3-Maxwell_2023-2024_Electromagnetisme_P2S1_EDupont.pdf"
pages: 19
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Électromagnétisme — Équations de Maxwell (2023–2024)

## Page 1

Physique - 2023-2024 Électromagnétisme Chapitre 4 –  Équations de Maxwell Présentation rédigée par Lucie Desplat (Pau)

Note : le nom du fichier indique « Chapitre 3 » et Émilie Dupont ; la couverture porte « Chapitre 4 » et Lucie Desplat (Pau).

## Page 2

- Chapitre 1 – Champ magnétique - Force de Lorentz - Chapitre 2 – Loi de Biot et Savart - Théorème d’Ampère - Chapitre 3 – Électrocinétique - Chapitre 4 – Équations de Maxwell - Chapitre 5 – Induction électromagnétique Programme de Magnétostatique

## Page 3

Dans ce chapitre, on se propose d’étudier l’électromagnétisme : les grandeurs physiques étudiées pourront dépendre de la position spatiale et du temps. Pour ce faire, on va présenter les 4 équations de Maxwell qui sont des lois fondamentales de la physique. Elles permettent de décrire mathématiquement l’onde électromagnétique constituée de deux parties indissociables : magnétique et électrique. Les voici:

$$\begin{aligned}
\operatorname{div}\vec E&=\rho/\varepsilon_0 &&\text{(Maxwell–Gauss)},\\
\operatorname{div}\vec B&=0 &&\text{(Maxwell–flux)},\\
\overrightarrow{\operatorname{rot}}\vec E&=-\frac{\partial\vec B}{\partial t} &&\text{(Maxwell–Faraday)},\\
\overrightarrow{\operatorname{rot}}\vec B&=\mu_0\vec j+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t} &&\text{(Maxwell–Ampère)}.
\end{aligned}$$

## Page 4

$$\begin{aligned}
\operatorname{div}\vec E&=\rho/\varepsilon_0 &&\text{(Maxwell–Gauss)},\\
\operatorname{div}\vec B&=0 &&\text{(Maxwell–flux)},\\
\overrightarrow{\operatorname{rot}}\vec E&=-\frac{\partial\vec B}{\partial t} &&\text{(Maxwell–Faraday)},\\
\overrightarrow{\operatorname{rot}}\vec B&=\mu_0\vec j+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t} &&\text{(Maxwell–Ampère)}.
\end{aligned}$$

Le support imprime $\mu_0=4\times10^{-7}$ SI pour la perméabilité magnétique et $\varepsilon_0=10^{-9}/(36\pi)$ SI pour la permittivité du vide. $B$ : champ magnétique en teslas ; $E$ : champ électrique en V/m.

Question : que deviennent ces relations exprimées dans le vide ? Voir le polycopié de cours.

Note de transcription : le facteur $\pi$ manque dans la valeur usuelle approchée de $\mu_0$, soit $4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$. La valeur fautive imprimée est conservée ci-dessus.

## Page 5

Le champ électromagnétique exerce sur une particule chargée de charge q placée en M et animée d’une vitesse v une force appelée force de Lorentz : Force de Lorentz

$$\vec F=q\vec E+q(\vec v\wedge\vec B).$$

## Page 6

• Un champ uniforme est un champ indépendant du vecteur position • Un champ stationnaire ou permanent est un champ indépendant du temps. • Un champ constant est un champ indépendant du temps et de la position. Rappels

## Page 7

### 2.4.2. Conservation de la charge

Soit $\rho$ la densité volumique de charges dans un milieu, et $\vec j=\rho\vec v$. L’équation de conservation de la charge s’écrit :

$$\frac{\partial\rho}{\partial t}+\operatorname{div}\vec j=0.$$

Pour la démonstration, voir le polycopié de cours.

## Page 8

### 2.4.3. Contenu physique des équations de Maxwell

Les équations de Maxwell sont locales. Par intégration, on obtient des lois et théorèmes connus, par exemple ceux de Gauss et d’Ampère.

**Maxwell–Gauss et théorème de Gauss.** Intégration dans un volume $V$ quelconque, délimité par $S$ :

$$\iiint_V\operatorname{div}\vec E\,d\tau=\iiint_V\frac\rho{\varepsilon_0}\,d\tau.$$

Le théorème d’Ostrogradsky donne :

$$\iiint_V\operatorname{div}\vec E\,d\tau=\oiint_S\vec E\cdot d\vec S.$$

Ainsi :

$$\oiint_S\vec E\cdot d\vec S=\frac{Q_{\mathrm{int}}}{\varepsilon_0},\qquad Q_{\mathrm{int}}=\iiint_V\rho\,d\tau.$$

On retrouve Gauss : les charges électriques sont à l’origine de $\vec E$, divergent ou convergent selon le signe de $\rho$. Le théorème de Gauss est valable en régime permanent et en régime variable.

## Page 9

Le théorème d’Ampère généralisé  On calcule la circulation à un instant donné du champ magnétique le long d’un contour fermé  C sur lequel s’appuie une surface S à travers l’application du théorème de Stokes :

$$\oint_C\vec B\cdot d\vec\ell=\iint_S\overrightarrow{\operatorname{rot}}\vec B\cdot d\vec S
=\iint_S\left(\mu_0\vec j+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}\right)\cdot d\vec S.$$

$$\oint_C\vec B\cdot d\vec\ell=\mu_0\left(i+\iint_S\varepsilon_0\frac{\partial\vec E}{\partial t}\cdot d\vec S\right),\qquad i=\iint_S\vec j\cdot d\vec S.$$

$i$ est l’intensité en ampères. On pose $i_D=\iint_S\varepsilon_0(\partial\vec E/\partial t)\cdot d\vec S$, interprété comme le courant de déplacement à travers $S$.

## Page 10

Équation du flux magnétique et champ magnétique à flux conservatif  En intégrant dans un volume V l’équation de Maxwell Flux, on a : Ensuite en appliquant le théorème d’Ostrogradsky, il vient : Le flux de $\vec B$ est nul. Autrement dit, $\vec B$ est à flux conservatif. Plusieurs interprétations : 1. Il n’existe pas de "charge magnétique" à l’origine de B . 2. Pas de divergence (ni convergence) des lignes de champ magnétique.

$$\iiint_V\operatorname{div}\vec B\,d\tau=0\quad\Longrightarrow\quad\oiint_S\vec B\cdot d\vec S=0.$$

## Page 11

**Maxwell–Faraday et loi de Faraday.** On évalue la circulation $e$ du champ électrique le long d’un contour fermé $C$ sur lequel s’appuie une surface $S$ :

$$e=\oint_C\vec E\cdot d\vec\ell.$$

Par Stokes puis Maxwell–Faraday :

$$e=\iint_S\overrightarrow{\operatorname{rot}}\vec E\cdot d\vec S
=\iint_S\left(-\frac{\partial\vec B}{\partial t}\right)\cdot d\vec S
=-\frac{d}{dt}\iint_S\vec B\cdot d\vec S.$$

$$\Phi=\iint_S\vec B\cdot d\vec S,\qquad e=-\frac{d\Phi}{dt}.$$

$\Phi$ est le flux du champ magnétique à travers $S$ ; $e$ est la force électromotrice (f.é.m.), en volts. Cette loi de Faraday traduit le phénomène d’induction, étudié au chapitre suivant. La dérivation ci-dessus concerne un contour fixe.

## Page 12

Principe de superposition  Les équations de Maxwell sont des équations linéaires Cohérence des équations  Chacune des équations de Maxwell étudiée séparément permet de rendre compte de phénomènes physiques (voir section 3). En considérant l’ensemble de ces 4 équations comme une unité permettant de décrire le comportement de l’onde EM, on observe que d’autres informations sont contenues. Ainsi,on va démontrer qu’on retrouve l’équation de conservation de la charge dans les équations de Maxwell : voir poly de cours pour la démo

## Page 13

**Existence d’ondes électromagnétiques.** En électrostatique, le champ électrique est dû aux charges électriques. En magnétostatique, le champ magnétique est dû aux courants électriques. En régime variable :

$$\overrightarrow{\operatorname{rot}}\vec E=-\frac{\partial\vec B}{\partial t}.$$

Si le champ magnétique dépend du temps, on peut avoir un champ électrique avec une densité de charge $\rho$ nulle. Le support indique qu’il suffit d’un courant électrique : « $\vec j$ dépend de $t$, ainsi $\vec E$ dépend de $t$, ainsi $\vec B$ dépend de $t$. »

## Page 14

### 2.4.5. Existence des potentiels $V$ et $\vec A$

Maxwell–flux permet de définir un champ vectoriel $\vec A$, appelé potentiel vecteur :

$$\vec B=\overrightarrow{\operatorname{rot}}\vec A.$$

Rappel : pour tout $\vec A$, $\operatorname{div}(\overrightarrow{\operatorname{rot}}\vec A)=0$.

Avec Maxwell–Faraday :

$$\overrightarrow{\operatorname{rot}}\vec E=-\frac{\partial\vec B}{\partial t}
=-\frac\partial{\partial t}(\overrightarrow{\operatorname{rot}}\vec A)
\quad\Rightarrow\quad
\overrightarrow{\operatorname{rot}}\left(\vec E+\frac{\partial\vec A}{\partial t}\right)=\vec0.$$

$$\vec E=-\overrightarrow{\operatorname{grad}}V-\frac{\partial\vec A}{\partial t}.$$

## Page 15

### 2.4.6. Cas particulier des régimes permanents

Conservation de la charge :

$$\frac{\partial\rho}{\partial t}=0\quad\Rightarrow\quad\operatorname{div}\vec j=0.$$

$\vec j$ est donc à flux conservatif. L’intensité est la même en tout point d’une branche : c’est le cas du régime continu.

La loi des nœuds découle de la même équation : $\sum_k i_k=0$, somme des intensités algébriques dans un nœud.

## Page 16

**Maxwell en régime permanent.**

$$\operatorname{div}\vec E=\frac\rho{\varepsilon_0},\quad\operatorname{div}\vec B=0,\quad
\overrightarrow{\operatorname{rot}}\vec E=\vec0,\quad\overrightarrow{\operatorname{rot}}\vec B=\mu_0\vec j.$$

Voir le polycopié pour plus de détails.

**Potentiel scalaire et potentiel vecteur.** $\partial\vec A/\partial t=\vec0$, donc $\vec E=-\overrightarrow{\operatorname{grad}}V$.

## Page 17

**Équations de Poisson.** En régime permanent :

$$\Delta V+\frac\rho{\varepsilon_0}=0,\qquad\Delta\vec A+\mu_0\vec j=\vec0.$$

Voir TD pour établir ces équations à partir de Maxwell.

Note de transcription : la forme donnée pour $\vec A$ utilise la jauge de Coulomb $\operatorname{div}\vec A=0$.

## Page 18

### 2.4.7. Relations de passage du champ électromagnétique

**Champ électrique.** Deux milieux 1 et 2 séparés par une surface chargée $\sigma$ :

$$\Delta\vec E=\vec E_2-\vec E_1=\frac\sigma{\varepsilon_0}\vec n_{1\to2}.$$

Seule la composante normale est discontinue ; la composante tangentielle est continue.

**Champ magnétique.** Deux milieux séparés par une surface parcourue par des courants surfaciques de densité $\vec j_s$ :

$$\Delta\vec B=\vec B_2-\vec B_1=\mu_0\vec j_s\wedge\vec n_{1\to2}.$$

Continuité de la composante normale et discontinuité de la composante tangentielle. Les expressions sont celles du support, dans le cadre des constantes du vide utilisées dans ce chapitre.

## Page 19

Bibliographie  - [1] Polycopié de cours, Abdelaziz Boumiz Polycopiés d’électromagnétisme II, EISTI - [2] CUPGE - CY : Introduction à l’électromagnétisme - [3] Cours LP 203 - Champs électrique et magnétique de Nicolas MENGUY - [4] Cours de Luc Tremblay, collège Mérici - « Électricité et magnétisme ». - [5]  David Sénéchal - « Histoire des sciences » PHQ399 Université de Sherbrooke, QC - [6]  pour la suite : Khan Academy , Unisciel  etc. - [7] Polycopié de Lucie Desplat – Pau - [8] Jean-Marie BREBEC, Électromagnétisme 1ère année MPSI PCSI PTSI , Hachette
