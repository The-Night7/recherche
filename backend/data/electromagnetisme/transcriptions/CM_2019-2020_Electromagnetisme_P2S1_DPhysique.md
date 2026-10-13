# Électromagnétisme — Première partie (EISTI, cycle préparatoire)

> Source : `PREING2-S1/Electromagnetisme/CM_2019-2020_Electromagnetisme_P2S1_DPhysique.pdf`, 125 pages. L’année 2019–2020 est celle du nom de fichier ; aucune date n’est indiquée sur la couverture.
> Transcription structurée achevée le 12 octobre 2026 : lecture visuelle des 125 pages, texte remis en forme, formules en LaTeX et schémas décrits ; les répétitions et transitions sont regroupées par section. Les valeurs numériques et affirmations historiques sont celles de la source ; les erreurs relevées et observations éditoriales sont signalées séparément. Les pages sans contenu sont indiquées. Cette transcription ne constitue pas une actualisation du cours.

## Couverture, bibliographie et sommaire — pages 1–6

La couverture porte « Électromagnétisme — 1ière Partie ». Les pages 2 et 6 ne contiennent que les en-têtes et pieds de page.

Bibliographie du cours, annoncée pour les chapitres 1 à 13 :

- P. Krempf, *Les Nouveaux Précis Bréal : Physique — Électromagnétisme MPSI*, Bréal, référence 209.0343.
- P. Krempf, *Les Nouveaux Précis Bréal : Physique — Électromagnétisme MP*, Bréal, référence 209.0359.
- José-Philippe Perez, Robert Carles, Robert Fleckinger, *Électromagnétisme : Fondements et applications*, premiers cycles–licence, Masson Sciences, Dunod, 4e édition.
- Jean-Marie Brébec, Thierry Desmarais, Alain Favier, Marc Ménètrier, Bruno Noël, Régine Noël, Claude Orsini, Jean-Marc Vanhaecke, *H Prépa : Nouveau Programme — Électromagnétisme 2e année MP–MP*–PC–PC*–PSI–PSI*–PT–PT*, Hachette Supérieur.

Le présent PDF contient les chapitres 0 à 7 :

| Chapitre | Parties annoncées et pages |
| --- | --- |
| 0. Introduction générale | 7 |
| 1. Notion de charge élémentaire | Introduction 9 ; historique 10 ; charges et loi de Coulomb 12 |
| 2. Étude générale du champ électrostatique | Introduction 21 ; rappels 22 ; champ créé par des charges 23 |
| 3. Potentiel et énergie potentielle électrostatiques | Introduction 41 ; gradient 42 ; potentiel 44 ; énergie potentielle 50 |
| 4. Conducteurs en équilibre électrostatique dans le vide | Introduction 57 ; isolants et conducteurs 58 ; grandeurs à l’équilibre 59 ; champ au voisinage de la surface 61 ; électrisation 65 ; condensateurs 69 |
| 5. Dipôle électrostatique | Introduction 77 ; définitions 78 ; dipôle actif 79 ; dipôle passif 83 ; intérêt de la notion 87 |
| 6. Champ magnétique et mouvement de particules chargées : introduction | Introduction 94 ; mise en évidence 95 ; lignes de champ 98 ; flux et circulation 99 ; théorème d’Ampère 101 ; Lorentz 105 ; Laplace 107 ; définition de l’ampère 108 |
| 7. Mouvements de particules chargées | Introduction 110 ; Lorentz 111 ; champ électrique uniforme 112 ; champ magnétique uniforme 115 ; mise en œuvre 120 |

## Chapitre 0 — Introduction générale (pages 7–8)

Dans cette partie de la physique, on découvre l’électrostatique et le magnétisme, réunis dans l’électromagnétisme. L’électrostatique étudie les phénomènes dus aux charges électriques au repos et appartient à cette théorie plus vaste.

Le premier schéma associe à la théorie de l’électricité quatre grandeurs : la charge $q$, la densité de courant $\vec J$, le champ électrique $\vec E$ et le champ magnétique $\vec B$. Le second relie ces grandeurs par les lois et théorèmes de Coulomb, Gauss, Laplace, Ampère, Faraday et Ampère–Maxwell. Il distingue les domaines de l’électrostatique et du magnétisme au sein de l’électromagnétisme ; une flèche oblique relie aussi le champ électrique à la densité de courant, sans nom de loi.

Avant le magnétisme, on étudie la charge électrique, le champ électrostatique et les conducteurs. La page 8 ne contient que le pied de page.

## Chapitre 1 — Notion de charge élémentaire (pages 9–20)

### I. Introduction — page 9

La loi de Coulomb traduit l’interaction entre deux charges électriques ponctuelles. La définition de la charge et cette loi permettent d’établir la théorie de l’électrostatique. Les outils nécessaires sont les repères cartésien, cylindrique et sphérique et les intégrales multiples.

### II. Historique : découverte des particules chargées — pages 10–11

La chronologie de la source est la suivante :

- Vers −600, Thalès de Milet (625–547) observe l’électrisation en frottant de l’ambre jaune avec une peau de chat ; il attribue aux objets « une âme et un souffle » pour expliquer le phénomène.
- En 1600, William Gilbert introduit le mot « électrique », en souvenir de l’ambre, *êlecktron* en grec.
- La ligne suivante est aussi datée « 1600 » : Otto Van Guerick (1602–1686) invente une machine électrostatique comportant une boule de soufre en rotation, frottée par une main ou un tissu ; un globe de verre remplace ensuite la boule de soufre.
- Au début du XVIIIe siècle, Charles François de Cisternay du Fay (1698–1737) distingue l’électricité vitreuse, positive, et résineuse, négative.
- En 1746, la bouteille de Leyde, aux Pays-Bas, permet de stocker les charges. Le condensateur décrit est une bouteille remplie d’eau dans laquelle plonge une tige métallique traversant le bouchon.
- En 1776, Jesse Ramsden (1735–1800) construit une machine constituée d’un disque de verre entraîné par une manivelle et frotté par quatre coussins de cuir remplis de crin. Les charges positives du disque électrisent par influence deux tubes métalliques creux.
- En 1785, Charles Augustin de Coulomb (1736–1806) établit que les forces entre particules chargées sont proportionnelles aux charges et inversement proportionnelles au carré de la distance.
- Sous l’entrée « XXe siècle », le document attribue à Joseph John Thomson (1856–1940) la découverte du proton.
- En 1911, Ernest Rutherford (1871–1937) met en évidence le noyau atomique. Environ vingt ans plus tard, les noyaux sont décrits comme composés de protons positifs et de neutrons neutres.

> **Observations sur la source :** la date « 1600 » donnée pour la machine de Van Guerick précède sa naissance indiquée dans la même ligne. L’attribution du proton à Thomson est reproduite comme affirmation du document, sans la valider. Cette chronologie n’a pas fait l’objet d’une vérification historique externe.

Les deux interactions alors connues, gravitation et électromagnétisme, ne suffisent pas à expliquer la cohésion du noyau : la gravitation est trop faible, les neutrons sont neutres et les protons se repoussent. Il faut introduire une force nucléaire, de *nucleus*, noyau.

En 1935, Hideki Yukawa propose une interaction entre protons et neutrons par l’intermédiaire d’une particule lourde, le pion. La masse non nulle du médiateur doit expliquer la courte portée. Le pion est découvert quelques années plus tard, mais cette théorie ne donne pas des résultats suffisamment satisfaisants ; beaucoup d’autres particules sensibles à la force nucléaire apparaissent. Au début des années 1960, la description reste incomplète.

En 1964, Murray Gell-Mann et George Zweig proposent que protons, neutrons et autres particules soient constitués de quarks. Le texte situe entre 1967 et 1970 l’apparition de la chromodynamique quantique, QCD. L’interaction forte lie les quarks pour former les hadrons, dont les protons, neutrons et pions. La force nucléaire devient une interaction résiduelle entre hadrons, par analogie avec les forces de van der Waals et l’électromagnétisme. Le document renvoie à `http://www.cerimes.fr/e_doc/forces/forte.htm`.

Le texte revient ensuite sur l’ancienneté des phénomènes électriques : éclairs avant l’apparition de la vie, rôle de l’électricité dans le vivant, observations antiques et développement des expériences au XVIIe siècle, initialement sans applications pratiques. En 1729, Stephen Gray (1666–1736) observe qu’un corps touchant un corps chargé devient chargé, première approche de la conductibilité. En 1800, la pile de Volta permet d’obtenir des courants ; les domaines de l’électricité et du magnétisme se rejoignent. La source évoque enfin les « courants d’inductivité » et Foucault vers 1850.

### III.1. Énoncé de la loi de Coulomb — pages 12–13

La loi de Coulomb décrit l’interaction entre deux charges ponctuelles immobiles dans le vide ; on assimile souvent l’air au vide. La charge $q_1$ est en $M_1$, la charge $q_2$ en $M_2$. La force de $q_1$ sur $q_2$, appliquée en $M_2$, vaut

$$\vec F_{1/2}=k\frac{q_1q_2}{r_{12}^2}\vec u_{1\to2}.$$

$\vec F_{1/2}$ s’exprime en newtons, $q_1,q_2$ en coulombs, $r_{12}=M_1M_2$ en mètres ; $\vec u_{1\to2}$ est un vecteur unitaire sans dimension dirigé de $M_1$ vers $M_2$. La constante dépend du milieu. Dans le vide,

$$k=\frac1{4\pi\varepsilon_0}\simeq9\times10^9\ \mathrm{kg\,m^3\,s^{-4}\,A^{-2}},$$

où $\varepsilon_0$ est la permittivité absolue du vide. La force réciproque, appliquée en $M_1$, est

$$\vec F_{2/1}=k\frac{q_2q_1}{r_{21}^2}\vec u_{2\to1}
=-k\frac{q_2q_1}{r_{21}^2}\vec u_{1\to2}=-\vec F_{1/2}.$$

Deux charges de même signe se repoussent ; deux charges de signes opposés s’attirent. Les deux schémas montrent les forces opposées sur la droite $M_1M_2$, dirigées vers l’extérieur pour la répulsion et l’une vers l’autre pour l’attraction.

### III.2. Charge totale d’une distribution — pages 13–18

Une distribution est une répartition de charges dans une région de l’espace : ponctuelle, linéique, surfacique ou volumique. Pour les distributions continues, on définit une densité considérée constante sur l’élément infinitésimal.

| Distribution | Densité et unité | Charge élémentaire | Charge totale |
| --- | --- | --- | --- |
| Ligne $\Gamma$ | $\lambda$, en $\mathrm{C\,m^{-1}}$ | $dq=\lambda\,dl$ | $Q=\int_\Gamma dq=\int_\Gamma\lambda\,dl$ |
| Surface $S$ | $\sigma$, en $\mathrm{C\,m^{-2}}$ | $dq=\sigma\,dS$ | $Q=\iint_S dq=\iint_S\sigma\,dS$ |
| Volume $V$ | $\rho$, en $\mathrm{C\,m^{-3}}$ | $dq=\rho\,dV$ | $Q=\iiint_V dq=\iiint_V\rho\,dV$ |

Les dessins localisent un segment $dl$ autour de $P$ sur la courbe $\Gamma$, une parcelle $dS$ sur une surface et un petit volume $dV$ dans le volume chargé. Si chaque densité est uniforme sur toute sa distribution,

$$Q=\lambda\int_\Gamma dl=\lambda L,\qquad
Q=\sigma\iint_S dS=\sigma S,\qquad
Q=\rho\iiint_V dV=\rho V.$$

#### Intégrales multiples — page 16

Intégrer sur une surface ou un volume fait varier plusieurs coordonnées. Si l’intégrande est un produit de fonctions de chacune des coordonnées et que les bornes de chaque variable sont indépendantes des autres variables, l’intégrale multiple est le produit d’intégrales simples :

$$\iiint f(x)g(y)h(z)\,dx\,dy\,dz
=\left(\int f(x)\,dx\right)\left(\int g(y)\,dy\right)\left(\int h(z)\,dz\right).$$

Le calcul des charges mobilise des intégrales simples, doubles ou triples et un système de coordonnées pour définir positions, longueurs et éléments géométriques.

#### Coordonnées cartésiennes — page 16

Le point $M$ a pour coordonnées $(x,y,z)$ dans la base $(\vec e_x,\vec e_y,\vec e_z)$ :

$$\overrightarrow{OM}=x\vec e_x+y\vec e_y+z\vec e_z,\qquad dV=dx\,dy\,dz.$$

Le dessin représente le parallélépipède élémentaire d’arêtes $dx$, $dy$, $dz$ et les projections de $M$ sur les axes.

#### Coordonnées cylindriques — page 17

$M'$ est la projection de $M$ sur le plan $Oxy$. Avec $(\rho,\theta,z)$,

$$\overrightarrow{OM}=\overrightarrow{OM'}+\overrightarrow{M'M}
=\rho\vec e_\rho+z\vec e_z,\qquad dV=d\rho\,(\rho\,d\theta)\,dz.$$

L’élément de volume a pour arêtes $d\rho$, $\rho\,d\theta$, $dz$. Le schéma montre $\rho=OM'$, l’angle azimutal $\theta$ et la base locale $(\vec e_\rho,\vec e_\theta,\vec e_z)$.

> **Coquille de la source :** la phrase sous le titre « Coordonnées cylindriques » appelle à tort $(\rho,\theta,z)$ des coordonnées « cartésiennes ».

#### Coordonnées sphériques — page 18

Avec $(r,\theta,\varphi)$, $\theta$ est l’angle polaire depuis $Oz$ et $\varphi$ l’angle azimutal dans $Oxy$ :

$$\overrightarrow{OM}=r\vec e_r,\qquad OM'=r\sin\theta.$$

$\vec e_r$ est colinéaire à $\overrightarrow{OM}$ ; $\vec e_\theta$ appartient au plan méridien $(OM,OM')$ ; $\vec e_\varphi$ est parallèle au plan $Oxy$. Les trois vecteurs forment un trièdre direct orthonormé. L’élément de volume a pour côtés $dr$, $r\,d\theta$ et $r\sin\theta\,d\varphi$ :

$$dV=dr\,(r\,d\theta)\,(r\sin\theta\,d\varphi)
=r^2\sin\theta\,dr\,d\theta\,d\varphi.$$

### III.3. Propriétés fondamentales liées aux charges électriques — pages 19–20

**a) Conservation.** La charge d’un système fermé, qui n’échange pas de matière avec l’extérieur, se conserve : elle reste constante et indépendante du référentiel d’étude.

**b) Superposition.** La force totale subie par $q_3$ sous l’action de $q_1$ et de $q_2$ est la somme des forces individuelles :

$$\vec F_{\text{élec}}=\vec F_{1/3}+\vec F_{2/3}.$$

La somme des causes produit un effet égal à la somme des effets individuels. Le dessin construit la résultante comme diagonale du parallélogramme des deux forces.

**c) Signes.** La charge existe sous deux formes, positive et négative. Attribuer une charge négative à l’électron est une convention.

**d) Extensivité.** La charge d’un système est la somme algébrique des charges qui le constituent.

**e) Quantification.** La charge varie par multiples entiers d’une charge élémentaire. Valeurs indiquées dans cette édition :

$$e=1{,}60217733\times10^{-19}\simeq1{,}6\times10^{-19}\ \mathrm C,
\qquad Q=Ze,\quad Z\in\mathbb Z.$$

| Porteur | Charge | Masse donnée par la source |
| --- | --- | --- |
| Électron | $-e$ | $m_e=0{,}91091\times10^{-30}\ \mathrm{kg}$ |
| Proton | $+e$ | $m_p=1{,}6725\times10^{-27}\ \mathrm{kg}$ |

La source décrit le proton comme environ 2000 fois plus lourd que l’électron.

## Chapitre 2 — Étude générale du champ électrostatique (pages 21–40)

### I–II. Introduction et rappels — pages 21–22

L’interaction électrostatique obéit à des lois quantitatives interprétées par Coulomb en 1785 à partir de la charge électrique. La loi de Coulomb met en évidence le champ électrique, dit électrostatique lorsqu’il ne varie pas dans le temps. Le théorème de Gauss permet également de le calculer.

Pour deux charges ponctuelles immobiles $q_A$ et $q_B$ dans le vide,

$$\vec F_{A\to B}=\frac1{4\pi\varepsilon_0}\frac{q_Aq_B}{AB^2}\vec e_r
=\frac1{4\pi\varepsilon_0}\frac{q_Aq_B}{AB^3}\overrightarrow{AB},
\qquad \vec e_r=\frac{\overrightarrow{AB}}{AB}.$$

Le coefficient $1/(4\pi\varepsilon_0)$ vaut environ $9\times10^9$ en unités SI ; la norme de la force varie comme l’inverse du carré de $AB$.

### III.1–2. Définition et champ d’une charge ponctuelle — pages 23–24

Si une particule ponctuelle de charge $q$, immobile en $M$, subit une force $\vec F$ autre que son poids, nulle lorsque $q$ est nul, on définit le champ électrostatique en $M$ par

$$\vec F=q\vec E.$$

La force est en newtons, la charge en coulombs, le champ en $\mathrm{N\,C^{-1}}$ ou $\mathrm{V\,m^{-1}}$.

Une charge $q$ en $P$ exerce sur une charge $q'$ en $M$ la force

$$\vec F=\frac1{4\pi\varepsilon_0}\frac{qq'}{r^2}\vec e_{PM}
=\frac1{4\pi\varepsilon_0}\frac{qq'}{PM^3}\overrightarrow{PM}=q'\vec E.$$

Le champ créé par $q$ est donc

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\frac q{r^2}\vec e_{PM}
=\frac1{4\pi\varepsilon_0}\frac q{PM^3}\overrightarrow{PM},\qquad r=PM.$$

Les schémas distinguent $q>0$, pour lequel le champ est dirigé de $P$ vers $M$, et $q<0$, pour lequel il est de sens opposé.

### III.3. Ensemble de charges ponctuelles — page 25

Pour $N$ charges distinctes $q_i$ situées en $P_i$, la superposition vectorielle donne

$$\vec E(M)=\sum_{i=1}^N\vec E_i(M)
=\sum_{i=1}^N\frac{q_i}{4\pi\varepsilon_0}\frac{\vec u_i}{r_i^2}
=\sum_{i=1}^N\frac{q_i}{4\pi\varepsilon_0}\frac{\overrightarrow{P_iM}}{P_iM^3},$$

où $\vec u_i=\overrightarrow{P_iM}/P_iM=\vec r_i/r_i$ est dirigé de $P_i$ vers $M$.

### III.4–6. Distributions continues uniformes — pages 26–28

Pour chaque distribution, un élément autour du point source $P$ est assimilé à une charge ponctuelle $dq$. Il produit en $M$, situé à la distance $r=PM$,

$$d\vec E=\frac{dq}{4\pi\varepsilon_0r^2}\vec u,
\qquad \vec u=\frac{\overrightarrow{PM}}{PM}=\frac{\vec r}r.$$

Le champ total est la somme de tous les champs élémentaires. Les dessins montrent le point $P$ sur la courbe, sur la surface ou dans le volume, puis le vecteur $d\vec E$ porté par $PM$ au point $M$.

**Distribution linéique $\Gamma$, densité uniforme $\lambda$.** Pour l’élément $dl$,

$$dq=\lambda\,dl,\qquad d\vec E=\frac{\lambda\,dl}{4\pi\varepsilon_0r^2}\vec u,$$
$$\vec E(M)=\int_\Gamma d\vec E
=\int_{P\in\Gamma}\frac{dq}{4\pi\varepsilon_0r^2}\vec u
=\int_{P\in\Gamma}\frac{\lambda\,dl}{4\pi\varepsilon_0r^2}\vec u.$$

**Distribution surfacique $S$, densité uniforme $\sigma$.** Pour l’élément $dS$,

$$dq=\sigma\,dS,\qquad d\vec E=\frac{\sigma\,dS}{4\pi\varepsilon_0r^2}\vec u,$$
$$\vec E(M)=\iint_Sd\vec E
=\iint_{P\in S}\frac{dq}{4\pi\varepsilon_0r^2}\vec u
=\iint_{P\in S}\frac{\sigma\,dS}{4\pi\varepsilon_0r^2}\vec u.$$

**Distribution volumique $V$, densité uniforme $\rho$.** Pour l’élément $dV$,

$$dq=\rho\,dV,\qquad d\vec E=\frac{\rho\,dV}{4\pi\varepsilon_0r^2}\vec u,$$
$$\vec E(M)=\iiint_Vd\vec E
=\iiint_{P\in V}\frac{dq}{4\pi\varepsilon_0r^2}\vec u
=\iiint_{P\in V}\frac{\rho\,dV}{4\pi\varepsilon_0r^2}\vec u.$$

### III.7. Définition et continuité du champ — page 29

Pour une collection de charges ponctuelles, le champ est défini et continu partout sauf sur les charges. Pour une distribution linéique, il est défini et continu sauf sur les points de la distribution. Pour une distribution surfacique, il est défini et continu en dehors de la surface et présente une discontinuité à sa traversée. Pour une distribution volumique, le cours indique un champ défini et continu en tout point de l’espace.

### III.8. Distribution quelconque — pages 29–30

Dans le cas volumique général, la densité n’est plus uniforme : $\rho=\rho(P)$. Pour un point source $P$ dans le volume et un point d’observation $M$ hors de la distribution,

$$\vec E(M)=\frac1{4\pi\varepsilon_0}\iiint_{P\in V}
\frac{\overrightarrow{PM}}{PM^3}\rho(P)\,dV.$$

L’intégration porte sur les variables du point $P$. En posant $\vec r=\overrightarrow{OM}$ et $\vec r'=\overrightarrow{OP}$,

$$\vec E(\vec r)=\frac1{4\pi\varepsilon_0}\iiint_{P\in V}
\frac{\vec r-\vec r'}{\|\vec r-\vec r'\|^3}\rho(\vec r')\,dV.$$

### III.9. Symétries — pages 30–32

Le champ, effet de la distribution de charges, porte les symétries des causes qui le produisent. Le principe de Curie affirme que les éléments de symétrie des causes se retrouvent dans les effets. On étudie donc les isométries, transformations conservant les distances, pour simplifier le calcul du champ.

1. **Translation.** Si le système est invariant par toute translation parallèle à $Oz$, ses effets ne dépendent pas de $z$.
2. **Symétrie axiale.** L’invariance par toute rotation d’angle $\theta$ autour de $Oz$ supprime la dépendance en $\theta$ des composantes cylindriques.
3. **Symétrie cylindrique.** L’invariance par translation suivant $Oz$ et rotation autour de cet axe réduit la dépendance à la distance $\rho$ à l’axe.
4. **Symétrie sphérique.** L’invariance par toute rotation autour d’un point $O$ réduit la dépendance à la distance $r$ au centre.
5. **Plan de symétrie $\Pi$.** En tout point du plan, le champ électrostatique appartient à ce plan.
6. Si $M'$ est le symétrique de $M$ par rapport au plan de symétrie $\Pi$, $\vec E(M')$ est le symétrique de $\vec E(M)$.
7. **Plan d’antisymétrie $\Pi'$.** Si la réflexion transforme la distribution $S$ en $-S$, le champ est perpendiculaire au plan en chacun de ses points.

Les dessins opposent le champ réfléchi de part et d’autre d’un plan de symétrie à son opposé réfléchi de part et d’autre d’un plan d’antisymétrie.

La remarque en gris de la page 32 qualifie $\vec E$ de « vrai vecteur » ou vecteur polaire ; le champ magnétique est un pseudo-vecteur. Un produit vectoriel de deux vrais vecteurs est un pseudo-vecteur ; celui d’un vrai vecteur et d’un pseudo-vecteur est un vrai vecteur.

### III.10. Calcul du champ par le théorème de Gauss — pages 32–38

Le théorème fournit une méthode utile lorsque le champ présente des symétries particulières. On choisit une surface adaptée, dite surface de Gauss, et l’on calcule le flux du champ à travers cette surface.

#### a–b) Flux élémentaire et flux total — pages 32–33

Sur un élément infinitésimal $dS$, le champ est considéré uniforme. Avec $\vec n$ normale unitaire,

$$d\vec S=\vec n\,dS,\qquad d\Phi=\vec E\cdot d\vec S=\vec E\cdot\vec n\,dS.$$

$dS$ est en $\mathrm{m^2}$, $\vec E$ en $\mathrm{V\,m^{-1}}$ et le flux en $\mathrm{V\,m}$. Pour une surface $S$,

$$\Phi=\iint_S d\Phi=\iint_S\vec E\cdot d\vec S
=\iint_S\vec E\cdot\vec n\,dS.$$

#### c) Théorème de Gauss — page 33

Le flux du champ à travers une surface fermée $S_{\mathrm{Gauss}}$ est proportionnel à la charge $q_{\mathrm{int}}$ contenue dans le volume qu’elle délimite :

$$\Phi=\oiint_{S_{\mathrm{Gauss}}}\vec E\cdot d\vec S
=\frac{q_{\mathrm{int}}}{\varepsilon_0}.$$

Le cercle sur l’intégrale double indique une surface fermée. $q_{\mathrm{int}}$ est en coulombs et $\varepsilon_0$ la permittivité absolue du vide.

#### d1) Plan infini uniformément chargé — pages 34–35

Le plan $\Pi$ porte une densité surfacique uniforme $\sigma$. Tous les plans perpendiculaires à $\Pi$ passant par $M$ sont des plans de symétrie : le champ est normal à $\Pi$. Si $\Pi$ est le plan $Oxy$,

$$\vec E(M)=E_z(x,y,z)\vec k=E_z(z)\vec k,$$

la seconde égalité résultant de l’invariance par translation suivant $x$ et $y$. Une surface de Gauss cylindrique traverse le plan et possède deux bases de même aire $S$, placées aux hauteurs opposées $z$ et $-z$. Par symétrie, les normes sont égales et $\vec E(-z)=-\vec E(z)$ ; les normales aux deux bases sont également opposées. Le flux latéral est nul :

$$\Phi=\Phi_{S_1}+\Phi_{S_2}+\Phi_{S_3}=ES+ES+0=2ES.$$

La charge enfermée est $\sigma S$. Ainsi

$$2ES=\frac{\sigma S}{\varepsilon_0},\qquad E=\frac{\sigma}{2\varepsilon_0}.$$

Le champ est dirigé suivant $Oz$, avec les orientations opposées indiquées de part et d’autre du plan. Dans le dessin, les flèches sont sortantes, correspondant à une charge positive.

#### d2) Fil rectiligne infini uniformément chargé — pages 35–36

Le fil porte une densité linéique constante $\lambda$. Les symétries et invariances imposent, en coordonnées cylindriques,

$$\vec E(r)=E(r)\vec u_r.$$

La surface de Gauss est un cylindre coaxial de rayon $r$ et de hauteur $h$. Les bases $S_1,S_2$ ont un flux nul, car le champ est perpendiculaire à leurs normales. Sur la surface latérale $S_3$,

$$\Phi_3=\iint_{S_3}E(r)\,dS=E(r)\,2\pi rh.$$

La charge intérieure est $\lambda h$, d’où

$$\Phi=\Phi_1+\Phi_2+\Phi_3=\Phi_3=\frac{\lambda h}{\varepsilon_0},$$
$$E(r)\,2\pi rh=\frac{\lambda h}{\varepsilon_0},\qquad
\boxed{\vec E(r)=\frac{\lambda}{2\pi\varepsilon_0r}\vec u_r.}$$

#### d3) Boule uniformément chargée — pages 37–38

Une boule de centre $O$ et de rayon $R$ porte une densité volumique uniforme $\rho$. La symétrie sphérique donne $\vec E(r)=E(r)\vec u_r$. On choisit une sphère de Gauss de rayon $r$ :

$$\Phi=\oiint_S\vec E\cdot d\vec S=E(r)\,4\pi r^2
=\frac{q_{\mathrm{int}}}{\varepsilon_0}.$$

**À l’extérieur, $r>R$.** La charge intérieure est la charge totale :

$$q_{\mathrm{int}}=Q=\iiint_{\text{boule}}\rho\,dV
=\rho\frac{4\pi R^3}3,$$
$$E(r)\,4\pi r^2=\frac{\rho\,4\pi R^3}{3\varepsilon_0},\qquad
E(r)=\frac Q{4\pi\varepsilon_0r^2}=\frac{\rho R^3}{3\varepsilon_0r^2}.$$

**À l’intérieur, $r<R$.** Seule la charge dans la sphère de Gauss intervient :

$$q_{\mathrm{int}}=\iiint_{\text{sphère de Gauss}}\rho\,dV
=\rho\frac{4\pi r^3}3,$$
$$E(r)\,4\pi r^2=\frac{\rho\,4\pi r^3}{3\varepsilon_0},\qquad
E(r)=\frac{\rho r}{3\varepsilon_0}.$$

Les deux expressions se raccordent en $r=R$ : $E(R)=\rho R/(3\varepsilon_0)$. Le champ est continu.

> **Précisions de transcription :** plusieurs expressions des pages 31–40 ont été déplacées dans la marge supérieure du PDF, laissant des cadres vides dans le corps du texte ; elles sont replacées auprès de leurs calculs. L’équivalence avec une charge ponctuelle $Q$ en $O$, affirmée sans restriction à la page 38, vaut à l’extérieur de la boule. L’inégalité $q_{\mathrm{int}}<Q$ écrite pour $r<R$ suppose ici $\rho>0$.

#### e) Lignes de champ — pages 38–40

Une ligne de champ d’un champ vectoriel est une courbe $C$ à laquelle le vecteur est tangent en chaque point. Elle permet de visualiser l’évolution spatiale du champ. La définition s’écrit

$$\vec E\wedge d\vec l=\vec0,$$

car $d\vec l$ est parallèle à $\vec E$.

| Coordonnées | Composantes de $d\vec l$ dans la base locale | Équations des lignes de champ |
| --- | --- | --- |
| Cartésiennes | $(dx,dy,dz)$ | $\dfrac{dx}{E_x}=\dfrac{dy}{E_y}=\dfrac{dz}{E_z}$ |
| Cylindriques | $(d\rho,\rho\,d\theta,dz)$ | $\dfrac{d\rho}{E_\rho}=\dfrac{\rho\,d\theta}{E_\theta}=\dfrac{dz}{E_z}$ |
| Sphériques | $(dr,r\,d\theta,r\sin\theta\,d\varphi)$ | $\dfrac{dr}{E_r}=\dfrac{r\,d\theta}{E_\theta}=\dfrac{r\sin\theta\,d\varphi}{E_\varphi}$ |

La justification cartésienne développe le produit vectoriel. Sa troisième composante est $E_x\,dy-E_y\,dx=0$, ce qui donne $dx/E_x=dy/E_y$ ; les autres composantes donnent la troisième égalité. Le rappel utilisé est

$$\vec A\wedge\vec B=\|\vec A\|\,\|\vec B\|\sin(\widehat{\vec A,\vec B})\,\vec u.$$

L’exemple de la charge ponctuelle en $O$, ou du champ extérieur d’une boule uniformément chargée, a $\vec E(r)=E(r)\vec u_r$. Les lignes de champ sont des droites passant par $O$, représentées par des flèches radiales. Le chapitre suivant relie ces lignes aux équipotentielles et au potentiel électrique.

> Les écritures sous forme de rapports sont à lire là où les dénominateurs ne sont pas nuls ; la relation vectorielle reste la définition générale.

## Chapitre 3 — Potentiel et énergie potentielle électrostatiques (pages 41–56)

### I. Introduction — page 41

Le champ électrostatique introduit par la force de Coulomb satisfait le théorème de Gauss, propriété reliée à la dépendance en $1/r^2$. La circulation du champ permet maintenant de calculer le potentiel, avec la notion de gradient, puis de définir les surfaces équipotentielles et l’énergie potentielle.

### II. Le gradient — pages 42–43

Pour un champ scalaire $V(M)$ et un déplacement infinitésimal de $M$ à un point voisin $M'$, la différentielle totale est

$$dV(M)=\sum_{i=1}^3\frac{\partial V}{\partial x_i}\,dx_i
=\overrightarrow{\mathrm{grad}}V\cdot d\overrightarrow{OM}.$$

En coordonnées cartésiennes,

$$d\overrightarrow{OM}=dx\,\vec i+dy\,\vec j+dz\,\vec k,\qquad
dV=\frac{\partial V}{\partial x}dx+\frac{\partial V}{\partial y}dy+\frac{\partial V}{\partial z}dz,$$
$$\overrightarrow{\mathrm{grad}}V=
\frac{\partial V}{\partial x}\vec e_x+
\frac{\partial V}{\partial y}\vec e_y+
\frac{\partial V}{\partial z}\vec e_z.$$

En coordonnées cylindriques, dans la base locale,

$$\overrightarrow{\mathrm{grad}}V=
\frac{\partial V}{\partial r}\vec e_r+
\frac1r\frac{\partial V}{\partial\theta}\vec e_\theta+
\frac{\partial V}{\partial z}\vec e_z.$$

En coordonnées sphériques,

$$\overrightarrow{\mathrm{grad}}V=
\frac{\partial V}{\partial r}\vec e_r+
\frac1r\frac{\partial V}{\partial\theta}\vec e_\theta+
\frac1{r\sin\theta}\frac{\partial V}{\partial\varphi}\vec e_\varphi.$$

Une surface équipotentielle $S$ est telle que $V(M)=V_0$ en chacun de ses points. Pour un déplacement sur $S$,

$$dV(M)=V_0-V_0=\overrightarrow{\mathrm{grad}}V\cdot d\overrightarrow{OM}=0.$$

Le gradient est donc normal à la surface équipotentielle passant par $M$.

### III.1–2. Circulation du champ — pages 44–45

Pour une courbe $\Gamma$ reliant $A$ à $B$, la circulation du champ de $A$ vers $B$ est

$$C=\int_A^B\vec E\cdot d\vec l,$$

où $d\vec l$ désigne le déplacement élémentaire le long de $\Gamma$.

Pour une charge $q$ en $O$ et deux points voisins $N,M$, la figure décompose le déplacement en une partie radiale et une partie tangentielle :

$$\overrightarrow{NM}=\overrightarrow{NP}+\overrightarrow{PM}
=dr\,\vec u_r+r\,d\theta\,\vec u_\theta,\qquad
\vec E=\frac q{4\pi\varepsilon_0r^2}\vec u_r.$$

La circulation élémentaire vaut

$$dC=\vec E\cdot\overrightarrow{NM}
=\frac q{4\pi\varepsilon_0r^2}\vec u_r\cdot
(dr\,\vec u_r+r\,d\theta\,\vec u_\theta)
=\frac q{4\pi\varepsilon_0r^2}\,dr
=-d\left(\frac q{4\pi\varepsilon_0r}\right).$$

Pour deux points éloignés $M_1,M_2$, avec $r_1=OM_1$, $r_2=OM_2$,

$$C=\int_{M_1}^{M_2}dC
=\int_{r_1}^{r_2}-d\left(\frac q{4\pi\varepsilon_0r}\right)
=\frac q{4\pi\varepsilon_0r_1}-\frac q{4\pi\varepsilon_0r_2}.$$

La superposition généralise ce résultat aux distributions de charges. La circulation ne dépend que des positions de départ et d’arrivée, et non du chemin suivi : le champ est à circulation conservative.

### III.3. Définition du potentiel — page 46

Le potentiel électrostatique $V$ est défini par

$$\boxed{\vec E=-\overrightarrow{\mathrm{grad}}V.}$$

$\vec E$ est en $\mathrm{V\,m^{-1}}$ et $V$ en volts. La circulation devient

$$C=\int_A^B\vec E\cdot d\vec l
=-\int_A^B\overrightarrow{\mathrm{grad}}V\cdot d\vec l
=-\int_A^B dV=V(A)-V(B),$$

et se mesure elle aussi en volts. Pour une charge $q$ en $O$,

$$dV(M)=-\vec E\cdot d\overrightarrow{OM}
=-\frac q{4\pi\varepsilon_0r^2}\,dr,$$
$$V(M)=\frac q{4\pi\varepsilon_0r}+V_0,$$

où $r=OM$ et $V_0$ est une constante d’intégration, généralement choisie nulle. La vérification donne bien

$$V(M_1)-V(M_2)=
\left(\frac q{4\pi\varepsilon_0r_1}+V_0\right)
-\left(\frac q{4\pi\varepsilon_0r_2}+V_0\right).$$

### III.4. Potentiels de différentes distributions — pages 47–48

**a) Charges ponctuelles.** Pour $n$ charges $q_i$,

$$\vec E=\sum_{i=1}^n\vec E_i,\qquad
V(M)=\sum_{i=1}^n V_i(M)
=\sum_{i=1}^n\frac{q_i}{4\pi\varepsilon_0r_i}+V_0,$$

où $r_i$ est la distance de $q_i$ à $M$. Le potentiel est défini et continu sauf aux points où se trouvent les charges.

**b) Distribution linéique.** Avec $r=PM$ et $dq=\lambda\,dl$,

$$V(M)=\int_\Gamma dV
=\int_{P\in\Gamma}\frac{dq}{4\pi\varepsilon_0r}+V_0
=\int_{P\in\Gamma}\frac{\lambda\,dl}{4\pi\varepsilon_0r}+V_0.$$

Le potentiel n’est pas défini sur les points où se trouvent les charges de la ligne.

**c) Distribution surfacique.** Pour $dq=\sigma\,dS$,

$$V(M)=\iint_SdV
=\iint_{P\in S}\frac{dq}{4\pi\varepsilon_0r}+V_0
=\iint_{P\in S}\frac{\sigma\,dS}{4\pi\varepsilon_0r}+V_0.$$

Le potentiel est défini sur la surface chargée et continu à sa traversée.

**d) Distribution volumique.** Pour $dq=\rho\,d\tau$,

$$V(M)=\iiint_{\mathcal V}dV
=\iiint_{P\in\mathcal V}\frac{dq}{4\pi\varepsilon_0r}+V_0
=\iiint_{P\in\mathcal V}\frac{\rho\,d\tau}{4\pi\varepsilon_0r}+V_0.$$

Le potentiel est défini et continu en tout point. La source avertit de ne pas confondre $V$, potentiel, avec le symbole du volume ; $\mathcal V$ et $d\tau$ les distinguent ici.

### III.5. Lignes de champ et équipotentielles — page 49

1. En chaque point d’une ligne de champ, $\vec E$ est tangent à la ligne.
2. Une surface équipotentielle est l’ensemble des points où le potentiel a une valeur constante.
3. Les lignes de champ sont perpendiculaires aux équipotentielles, car, sur celles-ci, $\vec E\cdot d\vec l=-dV=0$.
4. Le long d’une ligne parcourue dans le sens du champ de $M_1$ vers $M_2$, $\int_{M_1}^{M_2}\vec E\cdot d\vec l>0$. Donc $V(M_1)-V(M_2)>0$ : le champ est dirigé vers les potentiels décroissants.

La figure prend l’exemple d’un fil infini chargé de densité $\lambda$ : les équipotentielles sont représentées par des cylindres coaxiaux, et en coupe par des cercles concentriques ; les flèches du champ sont radiales.

### IV.1. Travail et énergie potentielle — pages 50–51

Comme pour la gravitation, on étudie le travail nécessaire pour déplacer une charge ou un système. Pour une charge fixe $q$ et $\vec F=q\vec E$,

$$dW=\vec F\cdot d\vec l=q\vec E\cdot d\vec l
=-q\overrightarrow{\mathrm{grad}}V\cdot d\vec l
=-\overrightarrow{\mathrm{grad}}(qV)\cdot d\vec l=-d(qV).$$

De $A$ à $B$,

$$W_{AB}=-\int_A^B d(qV)=-q\int_A^BdV=q[V(A)-V(B)].$$

Le travail ne dépend pas du chemin. L’énergie potentielle d’interaction est

$$E_p=\varepsilon_p=qV+K,$$

et le travail de la force est l’opposé de sa variation :

$$\vec F\cdot d\vec l=-d\varepsilon_p,\qquad
W_{AB}=\varepsilon_p(A)-\varepsilon_p(B)=-\Delta\varepsilon_p.$$

La force dérive de l’énergie potentielle :

$$\vec F=-\overrightarrow{\mathrm{grad}}\varepsilon_p,$$

car $-\overrightarrow{\mathrm{grad}}(qV+K)=q(-\overrightarrow{\mathrm{grad}}V)=q\vec E$.

Pour deux charges $q_1,q_2$ séparées par $r_{12}$,

$$\varepsilon_{p1}=q_1V_2+K=\frac{q_1q_2}{4\pi\varepsilon_0r_{12}}+K,$$
$$\varepsilon_{p2}=q_2V_1+K=\frac{q_1q_2}{4\pi\varepsilon_0r_{12}}+K=\varepsilon_{p1}.$$

L’énergie d’interaction est le travail fourni par un opérateur pour rapprocher les charges depuis l’infini, où elles n’interagissent pas, jusqu’à leurs positions finales. Elle est $\varepsilon_p=q_1q_2/(4\pi\varepsilon_0r_{12})+K$, et non la somme des deux écritures précédentes qui décrivent la même interaction.

### Application 1 — Potentiel d’un cylindre infini uniformément chargé (page 52)

**Énoncé.** Un cylindre de rayon $R$ et de hauteur infinie porte une densité volumique uniforme $\rho$. Déterminer son potentiel.

Le champ, annoncé comme déterminé en TD par Gauss, est radial :

$$\vec E(r)=E(r)\vec u_r,\qquad
E(r)=\begin{cases}
\dfrac{\rho r}{2\varepsilon_0},&r\le R,\\
\dfrac{\rho R^2}{2\varepsilon_0r},&r\ge R.
\end{cases}$$

Les invariances réduisent la dépendance à $r$, donc $E_r=-\partial V/\partial r=-dV/dr$. L’intégration donne deux constantes a priori distinctes :

$$V(r\ge R)=-\frac{\rho R^2}{2\varepsilon_0}\ln r+K,\qquad
V(r\le R)=-\frac{\rho r^2}{4\varepsilon_0}+K'.$$

La continuité en $R$ impose

$$-\frac{\rho R^2}{2\varepsilon_0}\ln R+K
=-\frac{\rho R^2}{4\varepsilon_0}+K',$$
$$K=-\frac{\rho R^2}{4\varepsilon_0}+K'
+\frac{\rho R^2}{2\varepsilon_0}\ln R.$$

Ainsi

$$V(r)=\begin{cases}
-\dfrac{\rho r^2}{4\varepsilon_0}+K',&r\le R,\\
\dfrac{\rho R^2}{2\varepsilon_0}\ln\!\left(\dfrac Rr\right)
-\dfrac{\rho R^2}{4\varepsilon_0}+K',&r\ge R.
\end{cases}$$

La source compare ensuite avec une tentative de calcul direct :

$$V(M)=\iiint_{P\in\mathcal V}\frac{\rho\,d\tau}{4\pi\varepsilon_0PM}+K.$$

On place $O$ au projeté orthogonal de $M$ sur l’axe du cylindre, et $Ox$ sur $OM$. Le point source $P$ a les coordonnées cylindriques $(r',\theta,z)$ :

$$\overrightarrow{PM}=\overrightarrow{PO}+\overrightarrow{OM}
=-r'\cos\theta\,\vec u_x-r'\sin\theta\,\vec u_y-z\vec u_z+r\vec u_x,$$
$$PM=\sqrt{(r-r'\cos\theta)^2+(r'\sin\theta)^2+z^2}
=\sqrt{r^2+r'^2-2rr'\cos\theta+z^2}.$$

L’intégrale écrite dans le PDF devient

$$V(M)=\iiint_{P\in\mathcal V}
\frac{\rho r'\,dr'\,d\theta\,dz}
{4\pi\varepsilon_0\sqrt{r^2+r'^2-2rr'\cos\theta+z^2}}.$$

Le texte la qualifie d’« absolument incalculable à la main » et recommande, pour les fortes symétries, de calculer d’abord le champ par Gauss, puis une primitive.

> **Erreur de la source :** pour un cylindre chargé infini, cette intégrale du potentiel référencé à l’infini diverge ; il ne s’agit pas seulement d’une difficulté de calcul. Les différences de potentiel et les expressions obtenues par intégration du champ restent définies, à une constante de référence près.

### Application 2 — Trois charges aux sommets d’un triangle (page 53)

**Énoncé.** Déterminer l’énergie potentielle de trois charges identiques $q$ aux sommets $A,B,C$ d’un triangle équilatéral de côté $2a$.

On fixe d’abord la charge en $A$, puis on amène la deuxième en $B$. Le potentiel en $B$ dû à $A$ vaut $V_A(B)=q/(8\pi\varepsilon_0a)$ ; le travail de l’opérateur est

$$W=q_BV_A(B)=\frac{q^2}{8\pi\varepsilon_0a}.$$

La troisième charge est amenée en $C$, où le potentiel des deux premières est

$$V(C)=V_A(C)+V_B(C)
=\frac q{8\pi\varepsilon_0a}+\frac q{8\pi\varepsilon_0a}
=\frac q{4\pi\varepsilon_0a}.$$

Le travail correspondant est $W'=q_CV(C)=q^2/(4\pi\varepsilon_0a)$. L’énergie d’interaction totale vaut donc

$$E_p=W+W'
=\frac{q^2}{8\pi\varepsilon_0a}+\frac{q^2}{4\pi\varepsilon_0a}
=\boxed{\frac{3q^2}{8\pi\varepsilon_0a}}.$$

Le cas de l’énergie d’une distribution continue de charges est annoncé hors programme. Les pages 54–56 ne contiennent que les pieds de page.

## Chapitre 4 — Conducteurs en équilibre électrostatique dans le vide (pages 57–76)

### I–II. Introduction, isolants, conducteurs et conservation — pages 57–58

On étudie les conducteurs comme milieux dans lesquels l’électrisation peut se transmettre, en appliquant les lois générales des chapitres précédents, puis leurs applications, notamment les condensateurs.

Un isolant conserve l’électrisation là où elle apparaît. Un conducteur permet sa transmission hors de la région initiale. Le cours relie ces définitions aux électrons libres des matériaux et aux notions d’électronique, dont les diodes et diodes Zener.

L’état électrique global d’un corps électriquement isolé est invariable : c’est la conservation de l’électricité. Un conducteur est en équilibre électrostatique lorsque ses porteurs de charges libres n’ont aucun mouvement d’ensemble à l’échelle macroscopique. Les lois de l’électrostatique dans le vide s’appliquent alors comme aux chapitres 1 à 3.

### III. Grandeurs et propriétés à l’équilibre — pages 59–60

**1. Nullité du champ.** Le champ électrique est uniformément nul dans la matière conductrice à l’équilibre. Sinon, les porteurs libres seraient soumis à des forces produisant un mouvement d’ensemble incompatible avec l’équilibre : $\vec E=\vec0$.

**2. Potentiel.** Comme $\vec E=-\overrightarrow{\mathrm{grad}}V=\vec0$, toutes les dérivées partielles de $V$ sont nulles. Le potentiel est uniforme dans tout le volume conducteur et sur sa surface, qui est donc équipotentielle.

**3. Charge volumique.** Une petite surface fermée entièrement dans la matière délimite un volume $dV$. Gauss donne

$$\Phi=\frac{q_{\mathrm{int}}}{\varepsilon_0}=\frac{\rho\,dV}{\varepsilon_0}
=\oiint_S\vec E\cdot d\vec S=0.$$

Donc $\rho=0$ : l’électrisation d’un conducteur en équilibre ne peut être que superficielle.

### IV.1. Champ au voisinage immédiat : théorème de Coulomb — pages 61–63

La surface électrisée est une couche de densité surfacique $\sigma$, généralement non uniforme. Au point $M$, on définit la normale unitaire sortante $\vec n$, dirigée de la région intérieure $R_1$ vers le vide extérieur $R_2$. Les points $M_1$ et $M_2$ approchent $M$ respectivement depuis l’intérieur et l’extérieur.

À l’intérieur, $\vec E_1=\vec0$. En appliquant Gauss à un petit volume traversant la surface, le flux extérieur est $E_2S=\sigma S/\varepsilon_0$. Ainsi

$$\boxed{\vec E_2=\frac\sigma{\varepsilon_0}\vec n,\qquad
\vec E_2-\vec E_1=\frac\sigma{\varepsilon_0}\vec n_{1\to2}.}$$

Cette relation de passage entraîne que les lignes de champ sont normales à la surface au voisinage immédiat. Elles sortent pour $\sigma>0$ et rentrent pour $\sigma<0$. Le champ présente une discontinuité à la surface. S’il existe plusieurs corps, il faut les considérer ensemble : la densité $\sigma(M)$ dépend de l’électrisation de tous les corps présents, par influence.

### IV.2. Pression électrostatique — hors programme (pages 63–64)

L’élément de charge $dQ=\sigma\,dS$ subit, de la part du champ extérieur à cet élément, $d\vec F=dQ\vec E$. En utilisant le champ $\sigma\vec n/(2\varepsilon_0)$ agissant sur la couche,

$$d\vec F=\frac{\sigma^2}{2\varepsilon_0}\vec n\,dS.$$

Par analogie avec la force pressante $d\vec F=p\vec n\,dS$, on pose

$$p=\frac{\sigma^2}{2\varepsilon_0}
=\frac{\varepsilon_0}2E_{\text{extérieur}}^2.$$

**Application 1.** Un champ de $10^4\ \mathrm{V\,m^{-1}}$ règne près d’un conducteur. Calculer $|\sigma|$ et le nombre surfacique d’électrons correspondant. La source utilise $\varepsilon_0\simeq1/(36\pi\times10^9)$ :

$$|\sigma|=\varepsilon_0E=\frac{10^4}{36\pi\times10^9}
\simeq8{,}84\times10^{-8}\ \mathrm{C\,m^{-2}},$$
$$n=\frac{8{,}84\times10^{-12}}{1{,}6\times10^{-19}}
=55{,}25\times10^6\ \text{électrons/cm}^2
=5{,}525\times10^{11}\ \text{électrons/m}^2.$$

**Application 2.** Pour le même champ, calculer la pression :

$$p=\frac{\sigma^2}{2\varepsilon_0}=\frac{\varepsilon_0E^2}2
\simeq18\pi\times10^9\sigma^2
=\frac{E^2}{72\pi\times10^9}
=\frac1{720\pi}\ \mathrm{Pa}.$$

Le PDF conclut par $p=1{,}4\times10^{-3}\ \mathrm{Pa}$ et la compare à la pression atmosphérique normale $p_0\simeq10^5\ \mathrm{Pa}$.

> **Erreur numérique de la source :** $1/(720\pi)\simeq4{,}42\times10^{-4}$, et non $1{,}4\times10^{-3}$. La conclusion qualitative d’une pression très faible reste valable.

### V.1. Conducteurs creux — pages 65–66

Un conducteur creux $C$ entoure une cavité sans charge. Dans cette cavité, le potentiel est uniformément égal au potentiel $V_0$ de la matière conductrice, donc $\overrightarrow{\mathrm{grad}}V=-\vec E=\vec0$.

La relation de passage sur la surface intérieure $S_{0I}$ est

$$\vec E_2-\vec E_1=\frac{\sigma_{0I}}{\varepsilon_0}\vec n_{1\to2}.$$

Le champ est nul dans la cavité comme dans le conducteur : $\sigma_{0I}=0$. Seule la surface extérieure $S_{0E}$ peut être électrisée. L’électrisation est identique à celle d’un conducteur plein ayant la même surface extérieure.

**Cage de Faraday.** Un conducteur à parois en treillage se comporte approximativement comme un conducteur creux sans lacune ; l’approximation s’améliore lorsque le treillage devient plus fin. Le dessin représente une cage métallique sur un socle isolant. La charge est sur la surface extérieure, le champ extérieur peut être non nul, et le champ intérieur est nul. Le cours prend pour exemple une voiture pendant un orage : sa carcasse métallique joue le rôle de cage et le texte conseille de rester à l’intérieur. Cette application est reproduite comme contenu du cours.

### V.2. Conducteur seul dans l’espace — pages 67–68

Les observations suivantes sont données sans démonstration. L’électrisation, superficielle, est partout de même signe. La charge $Q$, la densité $\sigma(M)$ et le potentiel $V$ ont le même signe :

- $V>0$, $\sigma(M)>0$, $Q>0$ : lignes sortantes ;
- $V<0$, $\sigma(M)<0$, $Q<0$ : lignes entrantes.

Les lignes sont normales à la surface et orientées vers les potentiels décroissants. Aucune ligne de champ ne peut relier deux points de la surface équipotentielle du conducteur.

La charge est proportionnelle au potentiel. On définit la capacité propre du conducteur isolé dans l’espace illimité par

$$C=\frac QV>0,$$

exprimée en farads (F). La densité $\sigma(M)$ n’est généralement pas uniforme, sauf pour une sphère seule. Sa valeur absolue est faible dans les régions à faible courbure et forte dans les régions à forte courbure : c’est le pouvoir des pointes. Le schéma elliptique illustre cette différence.

**Application.** Pour une sphère de rayon $R$,

$$V=\frac Q{4\pi\varepsilon_0R},\qquad C=4\pi\varepsilon_0R.$$

Une capacité de $1\ \mathrm F$ demanderait

$$R=\frac1{4\pi\varepsilon_0}\simeq9\times10^9\ \mathrm m
=9\times10^6\ \mathrm{km},$$

rayon qualifié d’énorme. En pratique, le cours cite les sous-multiples $\mu\mathrm F$ et $\mathrm{nF}$.

### VI. Condensateurs électriques — pages 69–73

Deux conducteurs isolés $A,B$ portent les charges opposées $+Q,-Q$ après transfert de charge. Les charges sont sur leurs surfaces. Les lignes du champ partent du conducteur positif et rejoignent le négatif. Chaque conducteur est une armature équipotentielle. Pour $Q\ne0$, les potentiels diffèrent, celui de l’armature positive étant le plus élevé.

La tension, ou différence de potentiel, est $U=V_A-V_B$, en volts. La relation d’état du condensateur est

$$Q=CU.$$

La capacité $C$, en farads, dépend de la géométrie : forme et dimensions des armatures, distance entre elles, et propriétés diélectriques du milieu. La méthode de calcul est : déterminer la répartition de charge grâce à la géométrie ; calculer le champ avec Gauss ; intégrer $dV=-\vec E\cdot d\vec l$ ; relier la différence de potentiel à $Q=CU$.

#### Condensateur plan — pages 70–72

Deux armatures parallèles de même aire $A$ sont séparées par $d$. Le premier dessin montre les lignes courbées aux bords ; le modèle idéal assimile les plaques à des plans infinis et néglige ces effets de bord. Entre les plaques, le champ est uniforme et perpendiculaire :

$$E=\frac\sigma{\varepsilon_0}=\frac Q{\varepsilon_0A}.$$

L’axe $x$ va de l’armature positive $x=0$ à l’armature négative $x=d$ :

$$d\vec l=dx\,\vec i,\qquad \vec E=\frac\sigma{\varepsilon_0}\vec i,$$
$$dV=-E\,dx=-\frac Q{\varepsilon_0A}\,dx,\qquad
V(x)=-\frac Q{\varepsilon_0A}x+\mathrm{constante}.$$

Ainsi

$$U=V(0)-V(d)=\frac{Qd}{\varepsilon_0A},\qquad
\boxed{C=\frac{\varepsilon_0A}d.}$$

L’énergie potentielle du condensateur vaut

$$\boxed{E_p=\frac12QU=\frac{Q^2}{2C}=\frac12CU^2.}$$

$E_p$ est en joules, $Q$ en coulombs, $U$ en volts et $C$ en farads. Le cours mentionne aussi les condensateurs cylindriques, sphériques et bifilaires. Un diélectrique isolant autre que le vide peut remplir l’espace entre les armatures et modifier la capacité.

#### Application : condensateur cylindrique — page 73

Les armatures sont deux cylindres coaxiaux de rayons $R_1<R_2$, de hauteur $h$, portant respectivement $+q$ et $-q$ avec des densités surfaciques uniformes. On utilise l’approximation de cylindres infiniment hauts.

Le rappel pour une coquille cylindrique de rayon $R$ et de densité $\sigma$ est

$$\vec E(r<R)=\vec0,\qquad
\vec E(r>R)=\frac{\sigma R}{\varepsilon_0r}\vec u_r.$$

Entre les armatures, le cylindre extérieur ne crée pas de champ ; seul intervient le cylindre intérieur :

$$\vec E=\frac{\sigma_1R_1}{\varepsilon_0r}\vec u_r,\qquad R_1<r<R_2.$$

Sa surface est $S_1=2\pi R_1h$, donc $q=\sigma_1\,2\pi R_1h$. La circulation peut être calculée sur tout chemin ; on choisit une ligne radiale avec $d\vec l=dr\,\vec u_r$ pour rendre champ et déplacement colinéaires :

$$\int_1^2\vec E\cdot d\vec l
=\int_{R_1}^{R_2}\frac{\sigma_1R_1}{\varepsilon_0r}\,dr
=\frac{\sigma_1R_1}{\varepsilon_0}\ln\frac{R_2}{R_1}.$$

D’autre part,

$$\int_1^2\vec E\cdot d\vec l
=-\int_1^2\overrightarrow{\mathrm{grad}}V\cdot d\vec l
=-\int_1^2dV=V_1-V_2=U.$$

Comme $\sigma_1R_1=q/(2\pi h)$,

$$U=\frac q{2\pi\varepsilon_0h}\ln\frac{R_2}{R_1}=\frac qC,
\qquad \boxed{C=\frac{2\pi\varepsilon_0h}{\ln(R_2/R_1)}.}$$

Les pages 74–76 ne contiennent que les en-têtes et pieds de page.

## Chapitre 5 — Dipôle électrostatique (pages 77–93)

### I–II. Introduction et définitions — pages 77–78

Un dipôle a une charge totale nulle mais peut créer un champ non nul. Cette situation apparaît lorsque les barycentres des charges positives et négatives sont décalés, comme dans la molécule d’eau. De nombreuses distributions peuvent être assimilées à un dipôle.

Un doublet est formé de deux charges opposées liées, $-q$ en $A$ et $+q$ en $B$, dont la distance $a=AB$ reste constante. Un dipôle est un doublet dont la séparation est petite.

Il est étudié comme **actif** lorsque $a$ est petit devant les distances du point d’observation aux deux charges ; il est **passif** lorsque le champ extérieur varie assez peu sur son étendue pour être considéré localement uniforme. Le moment dipolaire est

$$\boxed{\vec p=q\overrightarrow{AB},\qquad p=qa.}$$

Il pointe de la charge négative vers la positive et se mesure en $\mathrm{C\,m}$ ou en debyes, la conversion arrondie donnée étant $1\ \mathrm D=\frac13\times10^{-29}\ \mathrm{C\,m}$.

> L’écriture « $r=AM=BM$ » de la page 78 exprime l’approximation de grande distance ; ces distances ne sont pas exactement égales dans la géométrie générale.

### III.1. Potentiel du dipôle actif — pages 79–80

Le plan $Oxy$ contient $A,B,M$, avec $O$ milieu de $AB$. L’axe $Ox$ est orienté dans le sens du moment dipolaire. Les coordonnées sont

$$A=(-a/2,0,0),\quad B=(a/2,0,0),\quad
M=(r\cos\theta,r\sin\theta,0).$$

Le potentiel choisi nul à l’infini est la somme des deux contributions :

$$V(M)=-\frac q{4\pi\varepsilon_0AM}+\frac q{4\pi\varepsilon_0BM}.$$

Dans le triangle $AOM$, $\alpha=\pi-\theta$ et $AO=BO=a/2$. Le théorème de Pythagore généralisé donne

$$AM^2=AO^2+OM^2-2AO\,OM\cos\alpha
=\frac{a^2}4+r^2+ar\cos\theta,$$
$$BM^2=BO^2+OM^2-2BO\,OM\cos\theta
=\frac{a^2}4+r^2-ar\cos\theta.$$

Pour $a\ll r$, le développement limité au premier ordre en $a/r$ conduit à

$$\frac1{AM}=\frac1r\left(1+\frac{a^2}{4r^2}+\frac ar\cos\theta\right)^{-1/2}
\simeq\frac1r\left(1-\frac a{2r}\cos\theta\right),$$
$$\frac1{BM}=\frac1r\left(1+\frac{a^2}{4r^2}-\frac ar\cos\theta\right)^{-1/2}
\simeq\frac1r\left(1+\frac a{2r}\cos\theta\right).$$

En soustrayant,

$$\boxed{V(M)\simeq\frac{qa\cos\theta}{4\pi\varepsilon_0r^2}
=\frac{\vec p\cdot\vec u_r}{4\pi\varepsilon_0r^2}
=\frac{\vec p\cdot\overrightarrow{OM}}{4\pi\varepsilon_0r^3}.}$$

### III.2–3. Champ et diagramme électrique — pages 81–82

La constante additive est choisie nulle, comme le potentiel à l’infini. Avec $\vec p=p\vec u_x$,

$$\vec E=-\frac{\partial V}{\partial r}\vec u_r
-\frac1r\frac{\partial V}{\partial\theta}\vec u_\theta,$$
$$\boxed{E_r\simeq\frac{2p\cos\theta}{4\pi\varepsilon_0r^3},\qquad
E_\theta\simeq\frac{p\sin\theta}{4\pi\varepsilon_0r^3}.}$$

Le champ est dans le plan $Oxy$, conformément à la superposition. Les équipotentielles non nulles ont pour équation

$$r^2=k\cos\theta,\qquad k=\frac p{4\pi\varepsilon_0V}.$$

L’équipotentielle $V=0$ est le plan $Oyz$, projeté sur $Oy$ dans le dessin : $\cos\theta=0$, soit $\theta=\pm\pi/2$. Le diagramme distingue les lignes de champ en bleu et les équipotentielles en rouge. Les deux familles sont orthogonales. Les lignes de champ vérifient

$$r=k'\sin^2\theta,$$

avec $k'$ constant ; la démonstration est annoncée hors programme. La page 82 ne contient que cette fin de formule et la mention « démonstration hors programme », en plus du pied de page.

### IV.0. Dipôle passif : moment d’une force et produit vectoriel — page 83

On recherche la résultante et le moment des forces que subit le doublet dans un champ extérieur. Une force peut produire une translation ou une rotation. Le moment d’une force $\vec F$ appliquée en $M$, calculé en $O$, est

$$\vec M_O(\vec F)=\overrightarrow{OM}\wedge\vec F.$$

Pour $\vec V_1=(X_1,Y_1,Z_1)$ et $\vec V_2=(X_2,Y_2,Z_2)$,

$$\vec V_1\wedge\vec V_2=
(Y_1Z_2-Y_2Z_1)\vec i+(Z_1X_2-Z_2X_1)\vec j
+(X_1Y_2-X_2Y_1)\vec k.$$

Le produit est perpendiculaire au plan des deux vecteurs. Le trièdre formé par $\vec V_1$, $\vec V_2$, $\vec V_1\wedge\vec V_2$ est direct ; le sens se retrouve par la règle du tire-bouchon. La norme est l’aire du parallélogramme, soit $\|\vec V_1\|\,\|\vec V_2\|\,|\sin\theta|$.

### IV.1. Champ extérieur uniforme : force et moment — page 84

La résultante est nulle :

$$\vec F=\vec F_A+\vec F_B=-q\vec E+q\vec E=\vec0.$$

En un point quelconque $C$,

$$\vec M_C=\overrightarrow{CA}\wedge\vec F_A+
\overrightarrow{CB}\wedge\vec F_B
=(-\overrightarrow{CA}+\overrightarrow{CB})\wedge q\vec E
=q\overrightarrow{AB}\wedge\vec E
=\vec p\wedge\vec E.$$

Le moment ne dépend pas de $C$ : le dipôle subit un couple, de résultante nulle. Son sens indique celui de la rotation spontanée ; le moment dipolaire tend à s’orienter dans le sens du champ extérieur.

> La source qualifie le moment de « non nul » sans préciser l’orientation. La formule montre qu’il s’annule lorsque $\vec p$ et $\vec E$ sont colinéaires.

### IV.2. Énergie dans le champ extérieur — pages 84–85

On amène le dipôle entier depuis une région où le champ extérieur est nul jusqu’à sa position finale, en gardant ses deux charges liées. Si $V_A,V_B$ sont les potentiels extérieurs aux deux charges,

$$E_p=(-q)V_A+qV_B=q(V_B-V_A).$$

Dans un champ uniforme,

$$\int_A^B\vec E\cdot d\vec l
=\vec E\cdot\int_A^B d\vec l=\vec E\cdot\overrightarrow{AB},$$
$$\int_A^B\vec E\cdot d\vec l
=-\int_A^B dV=V_A-V_B.$$

Donc

$$\boxed{E_p=q(V_B-V_A)=-q\vec E\cdot\overrightarrow{AB}
=-\vec p\cdot\vec E.}$$

### IV.3. Champ extérieur non uniforme — pages 85–86

Sur la petite étendue du dipôle, les variations sont faibles, d’où l’approximation $\int_A^B\vec E\cdot d\vec l\simeq\vec E\cdot\overrightarrow{AB}$ et l’expression dipolaire $E_p\simeq-\vec p\cdot\vec E$.

Cependant, négliger ces variations dans le calcul de la résultante donnerait zéro : il faut conserver leur effet pour déterminer la force. Comme la force est conservative,

$$\boxed{\vec F=-\overrightarrow{\mathrm{grad}}E_p
=\overrightarrow{\mathrm{grad}}(\vec p\cdot\vec E).}$$

Son travail entre deux positions est

$$W=\int_1^2\vec F\cdot d\vec l
=-\int_1^2\overrightarrow{\mathrm{grad}}E_p\cdot d\vec l
=-\int_1^2dE_p=E_{p1}-E_{p2}.$$

Le déplacement spontané correspond à un travail moteur positif et à une diminution d’énergie. Dans un champ uniforme, l’énergie est minimale lorsque $\vec p$ et $\vec E$ sont colinéaires et de même sens. Dans un champ non uniforme, le dipôle s’oriente dans le sens du champ et tend vers les régions où sa norme augmente.

### V.1. Distribution de charges à grande distance — pages 87–88

On considère $N$ charges $q_i$ en $O_i$, un point $O$ voisin de la distribution et un point d’observation $M$ très éloigné. On pose $r=OM\gg a_i=OO_i$, $r_i=O_iM$, $\vec a_i=\overrightarrow{OO_i}$ et $\vec r=\overrightarrow{OM}$.

Le potentiel est $V=\sum_iq_i/(4\pi\varepsilon_0r_i)+\mathrm{constante}$. En prenant la référence nulle à l’infini,

$$\frac1{r_i}=\frac1{\|\vec r-\vec a_i\|}
=\frac1r\left(1-2\frac{\vec a_i\cdot\vec r}{r^2}
+\frac{a_i^2}{r^2}\right)^{-1/2}.$$

Le développement au premier ordre donne

$$\frac1{r_i}\simeq\frac1r\left(1+\frac{\vec a_i\cdot\vec r}{r^2}\right)
=\frac1r+\frac{\vec a_i\cdot\vec r}{r^3}
=\frac1r+\frac{\vec a_i\cdot\vec u}{r^2},\qquad \vec u=\frac{\vec r}r.$$

Ainsi

$$V(M)=\frac{\sum_iq_i}{4\pi\varepsilon_0r}
+\frac{\vec u\cdot\sum_iq_i\vec a_i}{4\pi\varepsilon_0r^2}+\cdots.$$

Les termes d’ordre supérieur ne sont pas écrits. À grande distance, le premier terme non nul domine.

- Si $Q=\sum_iq_i\ne0$, $V\simeq Q/(4\pi\varepsilon_0r)$ : au premier ordre, la distribution se comporte comme une charge ponctuelle $Q$ en $O$.
- Si $\sum_iq_i=0$ mais $\vec p=\sum_iq_i\vec a_i\ne\vec0$, $V\simeq\vec u\cdot\vec p/(4\pi\varepsilon_0r^2)$ : la distribution est dipolaire.
- Si $\sum_iq_i=0$ et $\vec p=\vec0$, les deux premiers termes sont nuls ; la source parle de distribution multipolaire, cas non étudié.

> **Restriction omise dans l’introduction de la page 87 :** une distribution quelconque n’est pas toujours équivalente à un dipôle. Les trois cas détaillés à la page suivante précisent les conditions nécessaires.

### V.2. Structure des molécules — page 89

La valeur $p=\|\vec p\|$ renseigne sur les structures moléculaires. Le dioxygène et le dichlore ne sont pas polaires, alors que l’eau l’est. Si l’on connaît la longueur des liaisons O–H, la mesure de $p$ permet de retrouver l’angle entre elles.

Le document prend ensuite le dinitrobenzène, décrit comme un explosif dont les propriétés dépendent de sa structure, avec les moments mesurés suivants : ortho, $5{,}8\ \mathrm D$ ; méta, $3{,}5\ \mathrm D$ ; para, $0$.

### Application : charges $+q,-2q,+q$ — pages 90–91

**Énoncé.** $A$ et $B$ sont symétriques par rapport à $O$, avec $AO=OB=a$. Les points $A,B$ portent chacun $+q$ et $O$ porte $-2q$. Un point éloigné $M$ situé sur l’axe $Oz$, perpendiculaire à $AB$, voit-il un dipôle ? Si oui, donner son moment.

1. La charge totale est nulle : cela rend une équivalence dipolaire possible, mais ne suffit pas à l’établir.
2. Avec le potentiel nul à l’infini,
   $$V(M)=\frac q{4\pi\varepsilon_0AM}-\frac{2q}{4\pi\varepsilon_0OM}
   +\frac q{4\pi\varepsilon_0BM}.$$
   Or $OM=|z|$ et $AM=BM=\sqrt{a^2+z^2}$, donc
   $$V(M)=\frac q{2\pi\varepsilon_0}\left(\frac1{\sqrt{a^2+z^2}}-\frac1{|z|}\right).$$
3. Pour $|z|\gg a$,
   $$V(M)=\frac q{2\pi\varepsilon_0|z|}
   \left[\left(1+\frac{a^2}{z^2}\right)^{-1/2}-1\right]
   \simeq\frac q{2\pi\varepsilon_0|z|}
   \left(1-\frac{a^2}{2z^2}-1\right)
   =-\frac{qa^2}{4\pi\varepsilon_0|z|z^2}.$$
4. Le potentiel décroît comme $1/r^3$, avec $r=OM$, tandis que le terme dipolaire décroît comme $1/r^2$ : ce système n’a pas de terme dipolaire non nul.
5. Vérification :
   $$\sum_iq_i\vec a_i=q\overrightarrow{OA}-2q\overrightarrow{OO}
   +q\overrightarrow{OB}=q(\overrightarrow{OA}+\overrightarrow{OB})=\vec0.$$
   Il s’agit du cas multipolaire.

Les pages 92–93 ne contiennent que les pieds de page.

## Chapitre 6 — Champ magnétique et mouvement de particules chargées : introduction (pages 94–109)

### I. Introduction — page 94

La force de Lorentz met en évidence le champ magnétique. La magnétostatique étudie les champs produits par des courants indépendants du temps. On peut les calculer par Biot et Savart, ou utiliser les symétries, les invariances et le théorème d’Ampère. L’étude du mouvement des porteurs dans les conducteurs conduit également à la loi d’Ohm et au calcul d’une résistance.

### II. Mise en évidence et calcul du champ — pages 95–97

Une charge $q$, immobile en $M$ et ne subissant que son poids, peut subir une force supplémentaire lorsqu’elle passe au même point avec une vitesse $\vec v$. Le champ magnétique $\vec B$ est alors défini par

$$\vec f=q\vec v\wedge\vec B.$$

$\vec f$ est en newtons, $q$ en coulombs, $\vec B$ en teslas (T), $\vec v$ en $\mathrm{m\,s^{-1}}$.

La loi de Biot et Savart pour un circuit filiforme $\Gamma$ parcouru par un courant $I$ est

$$\vec B(M)=\int_\Gamma d\vec B
=\int_\Gamma\frac{\mu_0I}{4\pi}
\frac{d\vec l\wedge\overrightarrow{PM}}{PM^3}
=\int_\Gamma\frac{\mu_0I}{4\pi}
\frac{d\vec l\wedge\vec u}{r^2},$$

avec $r=PM$ et $\vec u=\overrightarrow{PM}/PM$. La source emploie $\mu_0=4\pi\times10^{-7}$ en unités SI. Le champ n’est pas défini sur les points du courant filiforme idéal.

Le calcul direct peut être difficile. Les propriétés utilisées sont :

1. En un point d’un plan de symétrie de la distribution de courants, le champ magnétique est perpendiculaire au plan.
2. En un point d’un plan d’antisymétrie, le champ appartient au plan.
3. À l’intersection de deux plans d’antisymétrie, le champ est dirigé suivant leur droite d’intersection.
4. Une invariance par translation ou rotation supprime la dépendance en la coordonnée correspondante.

**Exemple : fil infini parcouru par un courant uniforme.** Les plans de symétrie et d’antisymétrie fixent la direction du champ. En coordonnées cylindriques, l’invariance suivant $Oz$ donne $B(r,\theta,z)=B(r,\theta)$, puis la rotation autour du fil donne $B(r,\theta)=B(r)$. $r=HM$ est la distance au fil. Le sens est déterminé par la règle du tire-bouchon ou du bonhomme d’Ampère. Les dessins utilisent un point dans un cercle pour une direction sortante de la page et une croix pour une direction entrante.

### III. Lignes de champ — page 98

En chaque point $M$ d’une ligne de champ magnétique, $\vec B$ est tangent à la ligne. Pour le fil infini,

$$\vec B=B(r)\vec u_\theta.$$

Le champ est orthoradial. Les lignes sont des cercles centrés sur le fil, représentés en perspective et en vue de dessus par des cercles concentriques orientés. Comme pour le champ électrique, on définit flux et circulation.

### IV. Flux et circulation — pages 99–100

**Flux.** À travers une surface $S$ de normale unitaire $\vec n$,

$$\Phi=\iint_S\vec B\cdot d\vec S=\iint_S\vec B\cdot\vec n\,dS.$$

Le flux à travers toute surface fermée est nul : $\oiint_S\vec B\cdot d\vec S=0$. Pour une surface ouverte, il ne dépend que de son contour fermé $\Gamma$.

**Circulation.** Les symétries permettent de connaître la forme des lignes de champ. On choisit un contour fermé $\Gamma$ constitué soit d’une ligne de champ fermée, soit d’une portion de ligne complétée par un chemin orthogonal au champ, de contribution nulle. Sur la portion de longueur $L$ parcourue dans le sens du champ,

$$C=\int_\Gamma\vec B\cdot d\vec l=\int_\Gamma B\,dl=BL,$$

si $B$ y reste constant. Le signe dépend de l’orientation du contour.

### V. Théorème d’Ampère — pages 101–104

La circulation le long d’un contour fermé $\Gamma$ est reliée au courant algébrique qui traverse une surface $S$ s’appuyant sur ce contour. Les courants sont comptés positivement dans le sens de la normale orientée à $S$ :

$$\boxed{\oint_\Gamma\vec B\cdot d\vec l=\mu_0\sum I_{\mathrm{alg}}.}$$

Le dessin donne l’exemple $\mu_0(I_1-I_2+I_3)$ pour trois intensités positives, dont la deuxième traverse la surface en sens opposé. Le cours souligne l’analogie avec Gauss. Les symétries déterminent la direction de $\vec B$ et les règles du tire-bouchon ou d’Ampère son sens.

#### Application 1 : fil rectiligne infini — page 102

Le fil est l’axe $Oz$, et $\vec B(M)=B(r)\vec u_\theta$. Une ligne de champ circulaire de rayon $r$ sert de contour ; le disque qu’elle borde est traversé par le courant. Le contour est orienté de sorte que $\vec B$ et $d\vec l$ aient le même sens, et la normale au disque est choisie en conséquence.

$$\oint_\Gamma\vec B\cdot d\vec l
=\oint_\Gamma B\,dl=B\oint_\Gamma dl=2\pi rB.$$

Le courant traverse le disque dans le sens positif, donc $2\pi rB=\mu_0I$ et

$$\boxed{\vec B(M)=\frac{\mu_0I}{2\pi r}\vec u_\theta.}$$

#### Application 2 : solénoïde infini — pages 103–104

Le cours renvoie à l’exercice 5 de la série 6 pour un calcul par Biot et Savart sur l’axe d’un solénoïde cylindrique infini de section circulaire :

$$B=\mu_0nI,\qquad \vec B=\mu_0nI\vec u_z,$$

où $n$ est le nombre de spires par mètre. Ce champ est indépendant du rayon.

Le système est invariant par translation suivant $Oz$ et rotation autour de $Oz$. Le plan perpendiculaire à l’axe passant par $M$ est un plan de symétrie ; le champ y est normal :

$$\vec B(r,\theta,z)=B(r)\vec u_z.$$

> **Coquille de la page 103 :** le texte appelle alors les lignes de champ des « cylindres ». La formule et le schéma montrent des droites parallèles à $Oz$, situées à distance radiale constante.

On choisit un contour rectangulaire dans un plan contenant l’axe, avec deux côtés parallèles à $Oz$, de longueur $\ell$ et de distances $r_1,r_2$ à l’axe, et deux côtés perpendiculaires. Ces derniers ne contribuent pas à la circulation :

$$\oint_C\vec B\cdot d\vec l=B(r_1)\ell-B(r_2)\ell
=\mu_0I_{\mathrm{alg}}.$$

Trois cas :

- $r_1<r_2<R$ : aucun courant enlacé, donc $B(r_1)=B(r_2)$ ; le champ intérieur est uniforme, noté $B_{\mathrm{int}}$.
- $R<r_1<r_2$ : aucun courant enlacé, donc champ extérieur uniforme, noté $B_{\mathrm{ext}}$.
- $r_1<R<r_2$ : $I_{\mathrm{alg}}=nI\ell$, avec l’orientation positive choisie, d’où $(B_{\mathrm{int}}-B_{\mathrm{ext}})\ell=\mu_0nI\ell$.

Le résultat déjà connu sur l’axe fixe $B_{\mathrm{int}}=\mu_0nI$, donc

$$\boxed{B_{\mathrm{ext}}=0.}$$

Le cours propose aussi de voir le solénoïde comme la limite d’une bobine torique de rayon infini, en référence à l’exercice 3 de la série 5.

### VI. Force de Lorentz et conduction — pages 105–106

Dans un champ électromagnétique $(\vec E,\vec B)$, la force généralisée est

$$\boxed{\vec f=q(\vec E+\vec v\wedge\vec B).}$$

On néglige ici le poids devant les forces électromagnétiques. Dans un champ électrostatique uniforme, la trajectoire est parabolique si vitesse initiale et champ ne sont pas colinéaires ; sinon, elle est rectiligne avec accélération constante. La vitesse peut varier avec l’énergie potentielle $E_p=qV$. Dans un champ magnétique seul, uniforme et stationnaire, la norme de la vitesse reste constante.

La loi d’Ohm locale écrite pour un conducteur est

$$\vec j=\gamma\vec E,$$

où $\gamma$ est la conductivité, dépendant du milieu et de la température, et $1/\gamma$ la résistivité, en $\Omega\,\mathrm m$. Le vecteur densité de courant s’écrit, pour des porteurs de densité numérique $n$ et vitesse moyenne $\vec v$,

$$\vec j=nq\vec v=\rho_m\vec v,\qquad \rho_m=nq.$$

L’intensité traversant une section $S$ vaut

$$I=\iint_S\vec j\cdot d\vec S,$$

en ampères. En régime stationnaire, la loi d’Ohm globale définit

$$R=\frac{V_A-V_B}{I}
=\frac{\displaystyle\int_A^B\vec E\cdot d\vec l}
{\displaystyle\iint_S\vec j\cdot d\vec S}.$$

Pour un barreau cylindrique de longueur $\ell$, de section $S$ et de conductivité $\gamma$,

$$R=\rho\frac\ell S,\qquad \rho=\frac1\gamma.$$

> **Erreur d’unité de la source :** la page 106 donne le siemens pour la conductivité $\gamma$. La relation locale et la résistivité en $\Omega\,\mathrm m$ imposent le siemens par mètre, $\mathrm{S\,m^{-1}}$. Le siemens seul est une unité de conductance.

### VII. Force de Laplace — page 107

Un circuit filiforme parcouru par $I$ et placé dans un champ magnétique subit la force élémentaire

$$d\vec F_L=I\,d\vec l\wedge\vec B.$$

La densité volumique correspondante est

$$\frac{d\vec F_L}{d\tau}=\vec j\wedge\vec B.$$

### VIII. Définition de l’ampère donnée dans cette édition — page 108

La définition reproduite repose sur l’interaction de deux fils infinis parallèles séparés par $d$. Le fil 1 crée

$$\vec B_1(M)=\frac{\mu_0I_1}{2\pi r}\vec u_\theta.$$

Une longueur $\ell$ du fil 2 subit

$$\vec F_{1\to2}=I_2\ell\vec u_z\wedge
\frac{\mu_0I_1}{2\pi d}\vec u_\theta
=-\frac{\mu_0I_1I_2}{2\pi}\frac\ell d\vec u_r.$$

La source définit l’ampère comme l’intensité constante qui, circulant dans deux conducteurs rectilignes, infinis, parallèles, de section circulaire négligeable et distants de $1\ \mathrm m$, produit une force de $2\times10^{-7}\ \mathrm N$ par mètre de conducteur. Elle fixe simultanément $\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$. Cette convention métrologique est restituée comme contenu de l’édition, sans mise à jour.

La page 109 ne contient que l’en-tête et le pied de page.

## Chapitre 7 — Mouvements de particules chargées (pages 110–125)

### I–II. Introduction et cadre de l’étude — pages 110–111

Les grands accélérateurs ont permis des découvertes sur la structure de la matière, notamment les quarks, situées par le texte dans les années 1970. Le chapitre étudie le mouvement des particules dans des champs électromagnétiques, sans reprendre la physique des collisions. Il utilise des champs uniformes et stationnaires et la force de Lorentz

$$\vec f=q(\vec E+\vec v\wedge\vec B).$$

L’étude relève de la mécanique newtonienne : les vitesses sont très petites devant celle de la lumière. On applique le principe fondamental de la dynamique dans un référentiel galiléen, sans changement de référentiel. Le référentiel terrestre est pris comme galiléen pour ces mouvements de quelques secondes, durée petite devant celle de rotation de la Terre. Le poids est négligé devant la force électromagnétique dans les situations étudiées.

### III.1. Champ électrostatique uniforme : lois horaires et trajectoire — pages 112–113

Dans le vide, sans pesanteur ni champ magnétique, une particule de masse $m$ et de charge $q$ vérifie

$$m\vec a=\vec f=q\vec E,\qquad \vec a=\frac{q\vec E}m.$$

Le mouvement est à accélération constante. Deux intégrations donnent

$$\vec v(t)=\frac{q\vec E}m t+\vec v_0,\qquad
\vec r(t)=\frac{q\vec E}{2m}t^2+\vec v_0t+\vec r_0.$$

La trajectoire reste dans le plan défini par la position initiale, $\vec E$ et $\vec v_0$. On choisit la position initiale comme origine, $Ox$ suivant $\vec E=E\vec u_x$, et $Oz$ perpendiculaire à ce plan. Alors

$$\vec v_0=v_{0x}\vec u_x+v_{0y}\vec u_y,\qquad
\begin{cases}
x(t)=\dfrac{qE}{2m}t^2+v_{0x}t,\\
y(t)=v_{0y}t.
\end{cases}$$

Si $v_{0y}\ne0$, on élimine $t=y/v_{0y}$ :

$$x=\frac{qE}{2mv_{0y}^2}y^2+\frac{v_{0x}}{v_{0y}}y.$$

La trajectoire est parabolique. Si $v_{0y}=0$, elle est rectiligne le long de $Ox$ : vitesse initiale et champ sont alors colinéaires.

### III.2. Étude énergétique — pages 113–114

La puissance de la force de Coulomb est $P=q\vec E\cdot\vec v$. En général, elle est non nulle et fait varier l’énergie cinétique. Avec $m\,d\vec v/dt=\vec f$,

$$P=\vec f\cdot\vec v=m\frac{d\vec v}{dt}\cdot\vec v
=\frac d{dt}\left(\frac12mv^2\right).$$

Entre deux points du mouvement,

$$\int_1^2P\,dt=\frac12mv_2^2-\frac12mv_1^2
=\int_1^2\vec f\cdot d\vec r=W_{1\to2}(\vec f),$$
$$\int_1^2P\,dt=q\int_1^2\vec E\cdot d\vec r
=-q\int_1^2\overrightarrow{\mathrm{grad}}V\cdot d\vec r
=-q\int_1^2dV=q(V_1-V_2).$$

Donc

$$\frac12mv_2^2-\frac12mv_1^2=q(V_1-V_2).$$

Pour $q>0$, le déplacement vers les potentiels décroissants $V_1>V_2$ augmente la vitesse et correspond à un travail moteur positif. On peut aussi écrire

$$\frac12mv_2^2+qV_2=\frac12mv_1^2+qV_1=E_c+E_p=E_m.$$

L’énergie mécanique est conservée puisque seule la force conservative de Coulomb travaille ; $E_p=qV$.

### IV.1. Champ magnétique uniforme : lois horaires — pages 115–117

Le champ est $\vec B=B\vec u_z$, avec $B>0$, uniforme et stationnaire ; il n’y a ni champ électrique ni pesanteur. La particule est en $O$ à $t=0$, et les axes $Ox,Oy$ sont choisis pour que $\vec v_0$ soit dans $Oyz$.

Le principe fondamental s’écrit

$$m\frac{d\vec v}{dt}=q\vec v\wedge\vec B.$$

Dans la base cartésienne, $\vec v\wedge\vec B=(Bv_y,-Bv_x,0)$, d’où

$$m\frac{dv_x}{dt}=qBv_y\quad(1),\qquad
m\frac{dv_y}{dt}=-qBv_x\quad(2),\qquad
m\frac{dv_z}{dt}=0\quad(3).$$

En dérivant (1), puis en utilisant (2),

$$m\frac{d^2v_x}{dt^2}=qB\frac{dv_y}{dt}
=-\frac{q^2B^2}m v_x,\qquad
\frac{d^2v_x}{dt^2}+\frac{q^2B^2}{m^2}v_x=0.$$

De même,

$$m\frac{d^2v_y}{dt^2}=-qB\frac{dv_x}{dt}
=-\frac{q^2B^2}m v_y,\qquad
\frac{d^2v_y}{dt^2}+\frac{q^2B^2}{m^2}v_y=0.$$

Le cours pose $\omega=qB/m$, grandeur algébrique appelée pulsation cyclotron. Les solutions s’écrivent

$$v_x=A\cos(\omega t)+H\sin(\omega t),\quad
v_y=D\cos(\omega t)+F\sin(\omega t),\quad v_z=G.$$

Les conditions initiales sont $v_x(0)=0$, $v_y(0)=v_0\cos\theta$, $v_z(0)=v_0\sin\theta$. Les équations du premier ordre donnent aussi

$$v_x'(0)=\omega v_0\cos\theta,\qquad v_y'(0)=0.$$

Ainsi $A=0$, $H=D=v_0\cos\theta$, $F=0$ et $G=v_0\sin\theta$, donc

$$v_x=v_0\cos\theta\sin(\omega t),\quad
v_y=v_0\cos\theta\cos(\omega t),\quad
v_z=v_0\sin\theta.$$

Une nouvelle intégration donne

$$x=-\frac{v_0\cos\theta}{\omega}\cos(\omega t)+X,\quad
y=\frac{v_0\cos\theta}{\omega}\sin(\omega t)+Y,\quad
z=v_0\sin\theta\,t+Z.$$

La position initiale nulle impose $X=v_0\cos\theta/\omega$, $Y=Z=0$ :

$$\boxed{\begin{aligned}
x(t)&=\frac{v_0\cos\theta}{\omega}[1-\cos(\omega t)],\\
y(t)&=\frac{v_0\cos\theta}{\omega}\sin(\omega t),\\
z(t)&=v_0\sin\theta\,t.
\end{aligned}}$$

### IV.1.2. Trajectoire — pages 118–119

Le mouvement selon $Oz$ est uniforme. Dans le plan $Oxy$, on élimine le temps en écrivant

$$\cos(\omega t)=1-\frac{\omega x}{v_0\cos\theta},\qquad
\sin(\omega t)=\frac{\omega y}{v_0\cos\theta}.$$

L’identité trigonométrique donne

$$\left(1-\frac{\omega x}{v_0\cos\theta}\right)^2
+\left(\frac{\omega y}{v_0\cos\theta}\right)^2=1,$$
$$\left(x-\frac{v_0\cos\theta}{\omega}\right)^2+y^2
=\left(\frac{v_0\cos\theta}{\omega}\right)^2.$$

La projection est un cercle parcouru uniformément, de centre

$$x_C=\frac{v_0\cos\theta}{\omega}=\frac{mv_0\cos\theta}{qB},\qquad y_C=0.$$

Lorsque les composantes parallèle et perpendiculaire de la vitesse sont non nulles, la trajectoire spatiale est une hélice circulaire de pas constant. Si $\sin\theta=0$, le mouvement est circulaire dans un plan orthogonal à $\vec B$. La source écrit le rayon $R=v_0\cos\theta/\omega=mv_0\cos\theta/(qB)$.

Si $\cos\theta=0$, vitesse et champ sont colinéaires, la force est nulle et le mouvement est rectiligne uniforme. Le pas est la distance parcourue suivant $Oz$ pendant un tour. Avec la convention algébrique $\omega t=2\pi$ du document,

$$p=v_0\sin\theta\frac{2\pi}{\omega}
=\frac{2\pi mv_0}{qB}\sin\theta.$$

Si $\sin\theta=0$, le pas est nul et l’on retrouve le cercle.

> **Rectifications de la source :** à la page 119, « suivant l’axe $Oy$ » doit être « suivant $Oz$ », comme l’imposent $\vec B=B\vec u_z$ et $z(t)=v_0\sin\theta\,t$. Le rayon géométrique est positif : $R=m|v_0\cos\theta|/(|q|B)$. La période physique est $T=2\pi/|\omega|$ ; le déplacement axial en une période vaut $v_0\sin\theta\,T$. Enfin, l’angle du cercle doit être mesuré entre $\overrightarrow{CO}$ et $\overrightarrow{CM}$ ; la source écrit $\overrightarrow{OM}$ dans cette phrase.

### IV.2. Énergie dans un champ magnétique — page 119

La puissance est nulle :

$$P=(q\vec v\wedge\vec B)\cdot\vec v=0,$$

le produit vectoriel étant perpendiculaire à $\vec v$. La force magnétique ne travaille pas :

$$\frac12mv_2^2-\frac12mv_1^2=W_{1\to2}(\vec f)
=\int_1^2P\,dt=0,\qquad v_2=v_1.$$

Le mouvement dans ce champ magnétique uniforme et stationnaire s’effectue à norme de vitesse constante.

### V. Méthode de résolution — page 120

Pour une particule de masse $m$, de charge $q$, placée dans des champs uniformes stationnaires et avec des conditions initiales données :

1. Faire le bilan des forces.
2. Écrire le principe fondamental de la dynamique, le projeter sur les trois axes et obtenir les équations différentielles des composantes de la vitesse.
3. Écrire les solutions générales et compter les constantes d’intégration.
4. Exprimer les conditions initiales, vérifier qu’elles permettent de fixer toutes les constantes, puis déterminer les lois horaires de la vitesse.
5. Intégrer pour obtenir la position ; les trois nouvelles constantes sont fixées par la position initiale.
6. Tracer la trajectoire.

### Application : champs électrique et magnétique croisés — pages 120–124

**Énoncé.** Une particule de masse $m$ et de charge $q>0$ est dans $\vec E=E\vec u_x$ et $\vec B=B\vec u_z$, uniformes. À $t=0$, elle est en $O$ sans vitesse initiale. Déterminer sa trajectoire.

Le poids est négligé. La seule force est $q(\vec E+\vec v\wedge\vec B)$. Comme $\vec v\wedge\vec B=(Bv_y,-Bv_x,0)$,

$$m\frac{dv_x}{dt}=qBv_y+qE\quad(1),\qquad
m\frac{dv_y}{dt}=-qBv_x\quad(2),\qquad
m\frac{dv_z}{dt}=0\quad(3).$$

En dérivant (2) et en utilisant (1),

$$m\frac{d^2v_y}{dt^2}=-qB\frac{dv_x}{dt}
=-qB\frac{qBv_y+qE}m,$$
$$\frac{d^2v_y}{dt^2}+\left(\frac{qB}m\right)^2v_y
=-\frac{q^2EB}{m^2}.$$

De même,

$$\frac{d^2v_x}{dt^2}+\left(\frac{qB}m\right)^2v_x=0.$$

En notant $\omega=qB/m$, la solution générale est

$$v_z=A,\qquad v_x=C\cos(\omega t)+C'\sin(\omega t).$$

Pour $v_y$, on additionne la solution de l’équation homogène et une solution particulière constante $v_{y2}=-E/B$ :

$$v_y=D\cos(\omega t)+D'\sin(\omega t)-\frac EB.$$

Il y a cinq constantes $A,C,C',D,D'$. Les trois conditions $v_x(0)=v_y(0)=v_z(0)=0$ sont complétées par les équations du mouvement au temps initial :

$$v_x'(0)=\frac{qE}m,\qquad v_y'(0)=0.$$

Elles donnent $A=C=D'=0$, $C'=D=E/B$. Ainsi

$$v_x(t)=\frac EB\sin(\omega t),\qquad
v_y(t)=\frac EB[\cos(\omega t)-1],\qquad v_z(t)=0.$$

L’intégration conduit à

$$x(t)=-\frac{mE}{qB^2}\cos(\omega t)+C'',$$
$$y(t)=\frac{mE}{qB^2}\sin(\omega t)-\frac EBt+D'',\qquad z(t)=A''.$$

La position initiale nulle impose $A''=D''=0$ et $C''=mE/(qB^2)$. Les lois horaires finales sont

$$\boxed{\begin{aligned}
x(t)&=\frac{mE}{qB^2}\left[1-\cos\!\left(\frac{qB}mt\right)\right],\\
y(t)&=\frac{mE}{qB^2}\sin\!\left(\frac{qB}mt\right)-\frac EBt,\\
z(t)&=0.
\end{aligned}}$$

La trajectoire reste dans le plan $Oxy$. Le document propose de la tracer à l’aide d’un tableur : on reconnaît une cycloïde. La page 125 ne contient que l’en-tête et le pied de page.
