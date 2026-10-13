---
source: "PREING2-S1/Electromagnetisme/CM-Chapitre6-Conducteurs_2023-2024_Electromagnetisme_P2S1_EDupont.pdf"
pages: 18
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Électromagnétisme — Chapitre 6 : conducteurs en équilibre électrostatique (fichier 2023–2024)

## Page 1

Électromagnétisme — Chapitre 6 : conducteurs en équilibre électrostatique. Physique 2021–2022 (date imprimée ; fichier classé en 2023–2024). Émilie Dupont, Cergy, emilie.dupont@cyu.fr, CY308.

Figure : lignes de champ arrivant perpendiculairement à la surface d’un conducteur.

## Page 2

Programme d’électrostatique : force entre deux charges ; champ électrostatique ; théorème de superposition et symétries ; théorème de Gauss ; potentiel électrostatique ; **conducteurs en équilibre électrostatique**.

## Page 3

### 1.6.1. Définitions

**Milieu conducteur.** C’est un milieu qui contient des charges libres (positives ou négatives) pouvant être mises en mouvement sous l’action d’un champ électrique. Un conducteur est un corps dont l’électrisation peut se transmettre hors de la région où elle est apparue.

**Conducteurs en équilibre électrostatique.** On dit qu’un conducteur est à l’équilibre électrique lorsque les charges mobiles qu’il contient sont au repos. Ce régime est statique : on parle de conducteurs en équilibre électrostatique.

Annotations : exemples de milieux conducteurs — métaux, semi-conducteurs, électrolytes ; à l’équilibre, « vitesse d’ensemble des charges nulle ».

## Page 4

### 1.6.2. Propriétés générales des conducteurs en équilibre

Dans un conducteur à l’équilibre électrostatique, le champ électrique est nul : $\vec E_{\mathrm{int}}=\vec0$.

$$\overrightarrow{\mathrm{grad}}V=\begin{pmatrix}\partial V/\partial x\\\partial V/\partial y\\\partial V/\partial z\end{pmatrix}=\vec0.$$

Le potentiel $V$ est uniforme dans tout le volume de la matière conductrice, y compris sur la surface du conducteur. La surface du conducteur est donc une surface équipotentielle.

Annotation : $-\vec E=\overrightarrow{\mathrm{grad}}V$.

## Page 5

### 1.6.2. Équilibre électrostatique : théorème de Coulomb

$\vec E=\vec0$, donc flux $\Phi=0$, d’où $\rho\,dV=0$ et $\rho=0$ : la charge volumique est nulle en tout point.

Le support énonce : « Il ne peut y avoir de charges libres à l’intérieur d’un conducteur en équilibre et le champ électrique à l’intérieur y est toujours nul. »

**Conducteur neutre**, dans le cas présenté :

- $\rho_{\mathrm{int}}=0$ et $\sigma=0$, c’est-à-dire absence totale de charges dans le conducteur ;
- $\vec E_{\mathrm{int}}=\vec0\Rightarrow V_{\mathrm{int}}=\mathrm{cst}=V_0$ car $\vec E=-\overrightarrow{\mathrm{grad}}V$ ;
- l’ensemble du conducteur (surface extérieure et volume) est au même potentiel $V_0$ ;
- à l’extérieur, le support conclut par le théorème de Gauss que $\vec E_{\mathrm{ext}}=\vec0$.

Note de transcription : il faut comprendre « charge volumique nette nulle », les porteurs mobiles existent toujours. La neutralité globale seule n’impose pas $\sigma=0$ en présence d’une influence extérieure ; le cas décrit suppose l’absence de cette influence.

Annotations : $dE=dq/(4\pi\varepsilon_0r^2)$, puis $dq=0$ ; $\vec E_{\mathrm{int}}=\vec0$, $\rho_{\mathrm{int}}=0$. Un contour $\Sigma_G$ entoure le conducteur pour appliquer Gauss : $\Phi(\vec E_{\mathrm{ext}}-\vec E)=q_{\mathrm{int}}/\varepsilon_0=0$.

## Page 6

**Conducteur chargé.** La charge présente dans le conducteur ne peut se répartir que sur sa surface, qui est une équipotentielle.

Au voisinage de la surface, $\vec E$ est normal à celle-ci :

$$(\vec E_{\mathrm{ext}}-\vec E_{\mathrm{int}})\cdot\vec n=\frac\sigma{\varepsilon_0},\qquad
\vec E_{\mathrm{int}}=\vec0\quad\Rightarrow\quad\vec E_{\mathrm{ext}}=\frac\sigma{\varepsilon_0}\vec n.$$

Si $\sigma>0$, le champ est dirigé vers l’extérieur ; si $\sigma<0$, vers l’intérieur. Les deux schémas représentent ces sens, au contact du vide. $\sigma$ est la charge surfacique, positive ou négative.

Annotation : « discontinuité à la traversée de surface chargée ». Les schémas rappellent le champ sortant d’une charge ponctuelle positive et entrant dans une charge négative.

## Page 7

### 1.6.3. Équilibre d’un système de deux conducteurs

**a) Introduction et définitions.** Approcher un conducteur chargé $C_1$ d’un conducteur $C_2$ influence la répartition de charge sur $C_2$.

1. Si $C_2$ est isolé, sa charge totale reste constante, mais ses charges surfaciques sont modifiées.
2. Si $C_2$ est maintenu à un potentiel donné, sa charge totale est modifiée par la présence de $C_1$.

Deux conducteurs sont en état d’influence totale si toute ligne de champ partant de l’un aboutit à l’autre. Deux conducteurs en état d’influence totale portent des charges opposées. Placer un conducteur dans la cavité d’un second permet d’obtenir deux armatures métalliques en état d’influence totale.

**b) Influence totale.** Si $C_2$ entoure totalement $C_1$, il y a correspondance totale entre les charges de la surface $S_1$ de $C_1$ et celles de la surface interne $S_2$ de $C_2$ :

$$Q_1=\int_{S_1}\sigma_1\,dS_1=-\int_{S_2}\sigma_2\,dS_2\qquad\text{(théorème de Faraday)}.$$

## Page 8

Influence totale : schéma d’un conducteur 1 chargé positivement entouré par un conducteur creux 2.

- Dans la partie interne de $C_1$ : $\vec E_1=\vec0$.
- Sur la surface de $C_1$ : charge $Q_1>0$ créant le champ dans la cavité.
- Sur la surface interne de $C_2$ : charge $-Q_1$.
- Dans la partie massive de $C_2$ : $\vec E=\vec0$.
- Sur la surface externe de $C_2$ : apparition de la charge $+Q_1$ pour assurer la neutralité de $C_2$, supposé neutre au départ.
- À l’extérieur : le champ $\vec E_{\mathrm{ext}}$ est celui créé par la seule charge $Q_1$ portée par la surface externe de $C_2$.

## Page 9

**Cage de Faraday.** Elle est constituée d’une enceinte conductrice reliée à la terre de façon à maintenir son potentiel fixe ; elle est étanche aux champs électriques, que la source perturbatrice se trouve à l’intérieur ou à l’extérieur de la cage.

Schéma : conducteur creux $B$ relié à la terre, à un potentiel nul par convention ; dans sa cavité, on place un conducteur chargé $A$. Les lignes de champ vont de $A$ positif vers la face interne négative de $B$.

Le champ régnant dans le conducteur est nul et, selon le texte, « par continuité », celui à l’extérieur de $B$ est nul aussi. L’espace extérieur est protégé de l’influence de $A$ placé dans la cavité.

Note de transcription : le champ peut être discontinu à une surface chargée ; la nullité extérieure dans cette configuration repose sur les conditions aux limites et l’unicité de la solution, non sur la seule continuité du champ.

## Page 10

### 1.6.4. Condensateurs

Deux conducteurs en état d’influence totale définissent un condensateur, qui accumule des charges électriques opposées sur ses armatures lorsqu’une différence de potentiel est imposée entre celles-ci. L’armature 1 est positive : $Q_1=+Q$ ; l’armature 2 est négative : $Q_2=-Q$. L’espace entre les armatures peut être vide ou rempli d’un isolant (diélectrique).

- Si $V_1=V_2$, la solution est $V=V_1=V_2$ dans la cavité. Le champ y est nul et les charges $Q_1,Q_2$ aussi.
- Si $U=V_1-V_2$ est imposée, le champ n’est plus nul dans la cavité. Les surfaces en regard portent $Q_1$ et $Q_2=-Q_1$ ; on note $Q=Q_1=-Q_2$.

Le dessin montre les lignes orientées de l’armature $+Q$ vers l’armature $-Q$.

## Page 11

La tension aux bornes du condensateur est la différence de potentiel entre les armatures : $U=V_1-V_2$.

$$Q=CU.$$

Le coefficient $C$, toujours positif, est la capacité du condensateur, exprimée en farads (F).

- La capacité dépend de la géométrie du condensateur.
- Lorsque les armatures sont reliées par un circuit électrique, celui-ci peut libérer la charge $Q$ emmagasinée jusqu’à ce que $U=0$.
- La capacité d’un conducteur isolé portant une charge $Q$ et maintenu au potentiel $V$ vérifie $Q=CV$.
- Rappel : $\vec E=-\overrightarrow{\mathrm{grad}}V\Longleftrightarrow V_A-V_B=\int_A^B\vec E\cdot d\vec\ell$.

## Page 12

### 1.6.4. Applications — Association de condensateurs

En série : $\displaystyle\frac1C=\frac1{C_1}+\frac1{C_2}+\cdots+\frac1{C_n}$.

En parallèle : $C=C_1+C_2+\cdots+C_n$.

Les schémas représentent respectivement les condensateurs placés successivement sur un fil et ceux branchés entre deux mêmes nœuds.

## Page 13

**Capacité d’un condensateur : méthode.**

1. À partir de la forme géométrique des armatures, chercher la répartition de charge sur ces armatures.
2. Calculer le champ électrique avec la loi de Gauss.
3. Calculer le potentiel entre les armatures : $dV=-\vec E\cdot d\vec\ell$.
4. Relier le potentiel, la différence de potentiel et la relation d’état du condensateur.

**Condensateur plan.** Deux armatures planes parallèles de même section $A$ sont distantes de $d$. Le schéma montre une source de tension, une plaque positive, une plaque négative et un champ allant de la première vers la seconde.

## Page 14

Applications — condensateur plan.

Schéma : les armatures sont aux potentiels $V_1$ et $V_2$, séparées de $d$ ; $\vec i$, $\vec E$, $d\vec\ell$ et $dx$ sont orientés de la plaque positive vers la plaque négative. Le reste de la page est un emplacement ligné vierge pour le calcul.

## Page 15

Applications. Page lignée laissée vierge dans la source.

## Page 16

On cherche la capacité d’un condensateur cylindrique : ses armatures sont des cylindres coaxiaux de rayons $R_1$ et $R_2>R_1$, de hauteur $h$, portant respectivement les charges $+q$ et $-q$ sur leur surface, avec une densité surfacique uniforme. On utilisera l’approximation du cylindre infiniment haut.

L’emplacement ligné réservé au calcul est vierge dans la source.

## Page 17

Applications. Page lignée laissée vierge dans la source.

## Page 18

Bibliographie : [1] Polycopié de cours ; [2] CUPGE–CY, Introduction à l’électromagnétisme ; [3] Wikipédia ; [4] Encyclopédie Universalis ; [5] P. Krempf, *Électromagnétisme MPSI*, Les Nouveaux Précis Bréal : Physique, Bréal Éditions ; [6] Raphaële Langer, *Électromagnétisme PCSI-MPSI-PTSI*, Nathan, Classe prépa.
