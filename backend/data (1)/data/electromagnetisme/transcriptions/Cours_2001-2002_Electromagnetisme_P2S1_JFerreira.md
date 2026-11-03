# Cours de magnétostatique — Jonathan Ferreira (2001–2002)

> Source : `PREING2-S1/Electromagnetisme/Cours_2001-2002_Electromagnetisme_P2S1_JFerreira.pdf`, 49 pages PDF : couverture, plan, 46 pages numérotées et formulaire final.
> Université Joseph Fourier, DEUG Sma – SP2-2, année universitaire 2001–2002.
> Transcription achevée le 11 octobre 2026 : texte natif remis en forme, formules retranscrites en LaTeX et comparaison aux pages rendues. Les schémas sont décrits dans les passages correspondants ; les développements sont regroupés par sous-section. Les erreurs relevées sont signalées. Les valeurs, définitions métrologiques et repères historiques sont ceux de cette édition ; ils ne constituent pas une mise à jour du cours.

## Plan — page PDF 2

1. Le champ magnétique : introduction ; expressions du champ ; symétries ; fil, spire et solénoïde.
2. Lois fondamentales de la magnétostatique : flux ; circulation et théorème d’Ampère ; dipôle magnétique.
3. Actions et énergie magnétiques : force de Lorentz ; actions sur un circuit ; énergie potentielle et règle du flux maximum.
4. Induction électromagnétique : lois de Faraday et de Lenz ; induction mutuelle et auto-induction ; régimes variables et bilan énergétique.

## I.1. Introduction — pages PDF 3–5 (pages imprimées 1–3)

### Aperçu historique

La magnétite, connue depuis l’Antiquité et associée à la ville de Magnesia en Turquie, a donné son nom au magnétisme. Le cours décrit les premières boussoles chinoises : une aiguille de magnétite posée sur de la paille flottant dans un récipient d’eau gradué.

Franklin établit en 1752 la nature électrique de la foudre. Les marins observaient que les orages perturbent les boussoles et que la foudre peut aimanter les objets métalliques d’un navire : Franklin suggéra une parenté entre électricité et magnétisme. Le texte cite ensuite les expériences de Coulomb (1785) et la décroissance des forces en $1/r^2$.

En 1820, Oersted fait passer un courant dans un fil au-dessus d’une boussole. L’aiguille dévie ; inverser le courant inverse la déviation, et la force observée n’est pas radiale. Biot et Savart étudient les oscillations d’une aiguille en fonction de sa distance à un courant rectiligne : la force est perpendiculaire à la droite joignant le pôle au conducteur et varie comme l’inverse de la distance. Laplace en déduit la loi aujourd’hui appelée loi de Biot et Savart. Davy montre en 1821 qu’un aimant peut dévier un arc électrique.

Le cours cite Oersted, Ampère, Arago, Faraday, Foucault, Henry, Lenz, Maxwell, Weber, Helmholtz, Hertz et Lorentz ; il situe la mise en équations par Maxwell en 1873 et l’interprétation relativiste en 1905. Les trois premiers chapitres étudient la production de champs magnétiques par des courants permanents ; le quatrième aborde la production d’électricité par induction.

### Nature des effets magnétiques

Pour deux charges immobiles, $\vec F_{1/2}=q_2\vec E_1(M_2)$ et $\vec F_{1/2}=d\vec p_2/dt\simeq\Delta\vec p_2/\Delta t$. L’action nécessite une propagation de l’information à vitesse finie $c$. Le schéma compare les positions présentes et passées de deux charges mobiles, leurs déplacements $\vec v_1dt$, $\vec v_2dt$ et la distance parcourue par l’information $c\,dt$. Il sert d’introduction qualitative au retard des interactions.

La formule admise dans le cours, dans l’approximation des faibles vitesses, est
$$\vec F_{1/2}=\frac{q_1q_2}{4\pi\varepsilon_0r^2}\left[\vec u_{12}+\frac{\vec v_2}{c}\times\left(\frac{\vec v_1}{c}\times\vec u_{12}\right)\right]
=q_2(\vec E_1+\vec v_2\times\vec B_1).$$
Le terme magnétique est d’ordre $(v/c)^2$ relativement au terme de Coulomb si les vitesses sont du même ordre. Le champ magnétique dépend du référentiel. Cette introduction n’est pas une dérivation des champs retardés exacts.

## I.2. Expressions du champ magnétique — pages PDF 5–12

### I.2.1. Une charge en mouvement

Dans un référentiel galiléen, une charge $q$ placée en $P$ et animée de la vitesse $\vec v$ crée, dans le cadre de l’approximation précédente,
$$\vec B(M)=\frac{\mu_0}{4\pi}\frac{q\vec v\times\overrightarrow{PM}}{PM^3}.$$
Le champ est perpendiculaire au plan de $\vec v$ et $\overrightarrow{PM}$. Son unité SI est le tesla (T) ; $1\ \mathrm G=10^{-4}\ \mathrm T$.

Le cours utilise $\mu_0=4\pi\times10^{-7}\ \mathrm{H/m}$, qualifiée d’exacte dans la convention métrologique de cette édition, et
$$\mu_0\varepsilon_0c^2=1,\qquad \varepsilon_0\simeq\frac{10^{-9}}{36\pi}\ \mathrm{F/m}.$$
Il relie ces constantes à l’unification de l’électricité, du magnétisme et de la lumière. **Les remarques de la source sur la définition de l’ampère et l’exactitude des constantes sont conservées comme contenu historique.**

Le principe de superposition s’applique : les champs s’additionnent vectoriellement. Le produit vectoriel fait de $\vec B$ un pseudo-vecteur.

Ordres de grandeur donnés par la source : aimant courant $10\ \mathrm{mT}$ ; électroaimant ordinaire environ $1\ \mathrm T$ ; bobine supraconductrice $20\ \mathrm T$ ; bobine résistive « 30 à 1000 T » ; milieu interstellaire $1\ \mu\mathrm G$ ; tache solaire $1\ \mathrm{kG}\simeq0{,}1\ \mathrm T$ ; champ terrestre vertical $0{,}4\ \mathrm G$ et horizontal $0{,}3\ \mathrm G$ ; étoile à neutrons $10^8\ \mathrm T$. La plage des bobines résistives est reproduite sans précision de régime, absente de la source.

### I.2.2. Ensemble de charges et distribution continue

Pour $N$ particules :
$$\vec B(M)=\frac{\mu_0}{4\pi}\sum_{i=1}^N\frac{q_i\vec v_i\times\overrightarrow{P_iM}}{P_iM^3}.$$
À une échelle grande devant les distances interparticulaires, on assimile un volume élémentaire $d^3V$ à une charge $dq$ de vitesse moyenne $\vec v$. Pour plusieurs espèces de densités numériques $n_\alpha$, charges $q_\alpha$ et vitesses $\vec v_\alpha$ :
$$dq\,\vec v=\sum_\alpha n_\alpha q_\alpha\vec v_\alpha\,d^3V=\vec j\,d^3V.$$
Ainsi
$$\vec B(M)=\frac{\mu_0}{4\pi}\iiint_V\frac{\vec j(P')\times\overrightarrow{P'M}}{P'M^3}\,d^3V.$$
La somme porte sur les espèces et non sur les particules. Cette forme convient à un conducteur de géométrie quelconque dans le cadre stationnaire du cours.

### I.2.3. Circuit filiforme : Biot et Savart

Un fil mince parcouru par un courant permanent $I$ est décomposé en sections $d^2S$ et longueurs $dl$, avec $d^3V=d^2S\,dl$. Le schéma distingue $P$, centre d’une section, et $P'$ dans cette section. À grande distance devant l’épaisseur du fil, $\overrightarrow{P'M}\simeq\overrightarrow{PM}$. Le courant vaut
$$I=\iint_{\text{section}}\vec j\cdot d\vec S.$$
En orientant $d\vec l=d\overrightarrow{OP}$ dans le sens du courant, l’intégrale de volume devient
$$\boxed{\vec B(M)=\frac{\mu_0 I}{4\pi}\oint_C\frac{d\vec l\times\overrightarrow{PM}}{PM^3}.}$$
Chaque élément contribue pour $d\vec B=(\mu_0 I/4\pi)(d\vec l\times\overrightarrow{PM})/PM^3$ ; il faut additionner les vecteurs, avec une orientation cohérente du circuit. Le cours rappelle les règles des trois doigts de la main droite, du bonhomme d’Ampère, du tire-bouchon et des pôles magnétiques. Il distingue l’établissement expérimental de la loi en 1820 de l’interprétation ultérieure du courant par le déplacement de charges.

### I.2.4. Symétries et pseudo-vecteurs

Un vecteur polaire (vitesse, champ électrique, densité de courant) et un vecteur axial (rotation, champ magnétique, normale orientée à une surface) se transforment de la même manière sous une rotation propre ou une translation. Par réflexion, un vecteur polaire devient son symétrique ; un vecteur axial devient l’opposé de son symétrique. Le schéma représente $\vec c=\vec a\times\vec b$ de part et d’autre d’un miroir.

> **Rectification de la page imprimée 7 :** le texte intervertit deux règles de produit vectoriel. Les règles correctes sont : polaire × polaire = axial ; axial × axial = axial ; polaire × axial = polaire. Elles sont compatibles avec la force $q\vec v\times\vec B$, qui est polaire.

Pour un miroir plan, la composante parallèle d’un vecteur polaire est conservée et sa composante normale change de signe ; pour un vecteur axial, la composante normale est conservée et les composantes parallèles changent de signe.

**Principe de Curie.** Les symétries des causes se retrouvent dans les effets. Dans un espace homogène et isotrope, transformer la distribution de charges ou de courants transforme les champs suivant leur caractère polaire ou axial.

| Symétrie des sources | Conséquence pour les composantes du champ dans la base adaptée |
| --- | --- |
| Translation suivant $Oz$ | Indépendance en $z$ |
| Rotation autour de $Oz$ | Indépendance en $\theta$ en coordonnées cylindriques |
| Translation et rotation autour de $Oz$ | Dépendance seulement en $\rho$ |
| Toutes les rotations autour de $O$ | Dépendance radiale dans la base sphérique |
| Plan de symétrie | Effet polaire tangent au plan, effet axial normal, aux points du plan |
| Plan d’antisymétrie | Effet polaire normal au plan, effet axial tangent, aux points du plan |

Dans les configurations axisymétriques décrites, un courant poloïdal (composantes $\vec u_\rho,\vec u_z$) produit un champ toroïdal ($\vec u_\theta$), et un courant toroïdal un champ poloïdal. Les figures montrent un courant cylindrique traversant un plan d’antisymétrie et une distribution de charges opposées dans deux hémisphères.

**Justifications.** Pour une translation infinitésimale selon $x_1$, on écrit composante par composante
$$A_i(x_1+dx_1,x_2,x_3)=A_i(x_1,x_2,x_3)+\frac{\partial A_i}{\partial x_1}dx_1+o(dx_1).$$
L’invariance impose $\partial A_i/\partial x_1=0$. Pour les plans, on combine la transformation par réflexion avec l’égalité des sources réfléchies aux sources initiales (symétrie), ou à leurs opposées (antisymétrie). Les conclusions de direction s’appliquent aux points du plan. **Précision :** la source parle de l’égalité de « toute fonction » et omet parfois cette restriction aux points du plan ; on doit appliquer le raisonnement aux champs produits et à leurs lois de transformation.

## I.3. Champs de configurations simples — pages PDF 12–13

### Fil rectiligne infini

Le fil est l’axe $Oz$ et porte un courant $I$. Les symétries donnent $\vec j=j(\rho)\vec u_z$ et $\vec B=B(\rho)\vec u_\theta$. Pour un point $M$ à distance $a$ de l’axe, le schéma définit $OP=a\tan\alpha$, $PM=a/\cos\alpha$, donc $dOP=a\,d\alpha/\cos^2\alpha$.
$$dB_\theta=\frac{\mu_0I}{4\pi}\frac{dOP\cos\alpha}{PM^2},\qquad
B=\frac{\mu_0I}{4\pi a}\int_{-\pi/2}^{\pi/2}\cos\alpha\,d\alpha=\frac{\mu_0I}{2\pi a}.$$

### Spire circulaire, sur son axe

Une spire de rayon $R$ porte $I$. Le courant toroïdal donne un champ poloïdal ; sur l’axe, les composantes transversales se compensent. Avec $\sin\alpha=R/\sqrt{R^2+z^2}$ et $dOP=R\,d\theta$ :
$$dB_z=\frac{\mu_0I}{4\pi R}\sin^3\alpha\,d\theta,$$
$$B_z=\frac{\mu_0I}{2R}\sin^3\alpha=\frac{\mu_0IR^2}{2(R^2+z^2)^{3/2}}.$$

### Solénoïde infini, sur son axe

Le solénoïde est modélisé par des spires coaxiales, à raison de $N$ spires **par unité de longueur**. Une tranche $dz$ contient $N\,dz$ spires et crée
$$dB=\frac{\mu_0NI}{2R}\sin^3\alpha\,dz.$$
Avec les angles aux deux extrémités et l’orientation du schéma, l’intégration donne
$$B=\frac{\mu_0NI}{2}\int_{\alpha_1}^{\alpha_2}\sin\alpha\,d\alpha
=\frac{\mu_0NI}{2}(\cos\alpha_1-\cos\alpha_2).$$
Pour une longueur infinie, $\alpha_1\to0$, $\alpha_2\to\pi$, donc $B=\mu_0NI$ sur l’axe.

> Le signe de $dz$ dépend de la coordonnée choisie : la source écrit à la fois $\tan\alpha=R/z$ et $dz=+R\,d\alpha/\sin^2\alpha$. La dérivée algébrique de cette première relation est négative ; la formule intégrée suppose une orientation et des bornes cohérentes.

## II.1. Flux du champ magnétique — pages PDF 14–16

Les lois fondamentales sont présentées comme des résultats expérimentaux, dont la formulation ultérieure est celle des équations de Maxwell.

### Conservation du flux

Pour toute surface fermée $S$, orientée vers l’extérieur,
$$\boxed{\oiint_S\vec B\cdot d\vec S=0.}$$
Cette loi reste valable en régime variable. À la différence de $\oiint_S\vec E\cdot d\vec S=Q_{\mathrm{int}}/\varepsilon_0$, elle ne fait intervenir aucune charge magnétique : le cours rappelle l’absence de monopôle observé et l’impossibilité de dissocier les deux pôles d’un aimant.

Le dessin ferme un même contour $C$ par deux surfaces $S_1,S_2$. Avec les normales extérieures, $\Phi_{S_1}+\Phi_{S_2}=0$ ; si l’on oriente les deux surfaces à partir du même contour, leurs flux sont égaux. Le flux à travers une surface bordée par $C$ ne dépend donc pas du choix de cette surface.

### Lignes de champ et tubes de flux

La limaille de fer révèle les directions du champ. Une ligne de champ est une courbe partout tangente au champ :
$$\vec B\times d\vec l=\vec0.$$
En coordonnées cartésiennes puis sphériques :
$$\frac{dx}{B_x}=\frac{dy}{B_y}=\frac{dz}{B_z},\qquad
\frac{dr}{B_r}=\frac{r\,d\theta}{B_\theta}=\frac{r\sin\theta\,d\varphi}{B_\varphi}.$$
Ces écritures par quotients s’utilisent là où les dénominateurs conviennent ; l’équation vectorielle reste la formulation générale.

> **Précision :** la source déduit que toutes les lignes se referment sur elles-mêmes. La divergence nulle interdit des sources et puits magnétiques, mais n’impose pas que chaque ligne soit une courbe fermée ; certaines peuvent se prolonger à l’infini.

Un tube de flux est engendré par les lignes passant par le bord d’une section. Sur sa paroi latérale $S_L$, le champ est tangent et le flux nul. Pour une portion fermée par $S_1,S_3$, la conservation du flux donne l’égalité des flux à travers les deux sections orientées dans le sens du champ. Le dessin ajoute une section rétrécie $S_2$ : à flux constant, le champ y est plus intense. Des lignes plus resserrées représentent un champ plus fort. Les taches solaires sont citées comme exemple naturel de tubes de flux.

## II.2. Circulation du champ magnétique — pages PDF 16–20

### Fil infini et théorème d’Ampère

Pour $\vec B=\mu_0I\vec u_\theta/(2\pi\rho)$ et $d\vec l=d\rho\vec u_\rho+\rho d\theta\vec u_\theta+dz\vec u_z$ :
$$\oint_C\vec B\cdot d\vec l=\frac{\mu_0I}{2\pi}\oint_C d\theta.$$
L’intégrale angulaire vaut $0$ si le contour n’enlace pas le fil, $2\pi$ pour un enlacement positif, $2N\pi$ pour $N$ enlacements algébriques. Cela conduit au résultat général admis :
$$\boxed{\oint_C\vec B\cdot d\vec l=\mu_0 I_{\mathrm{int}}.}$$
Le contour d’Ampère est fermé et orienté ; $I_{\mathrm{int}}$ est la somme algébrique des courants traversant une surface qu’il borde. Cette forme est utilisée en régime permanent. Le choix d’orientation est libre, puis la règle du tire-bouchon fixe les signes. Le schéma donne $I_{\mathrm{int}}=-I_1+I_2-I_2=-I_1$ : un courant entrant puis sortant s’annule dans la somme. Le théorème et Biot et Savart expriment la même physique ; ils ne doivent pas être utilisés avec des orientations incompatibles.

### Solénoïde infini

Pour $N$ spires par unité de longueur, $\vec j=j(\rho)\vec u_\theta$ et $\vec B=B(\rho)\vec u_z$. Le schéma montre trois contours rectangulaires de longueur axiale $l$.

1. Entièrement à l’intérieur : aucun courant enlacé, donc $B_{AB}l-B_{DC}l=0$ ; le champ intérieur est uniforme.
2. Entièrement à l’extérieur : même raisonnement ; le champ extérieur est uniforme, puis nul avec la condition à l’infini retenue dans le cours.
3. Traversant la nappe de spires : le courant enlacé est $NlI$ en valeur absolue ; le côté extérieur ne contribue pas. Donc $B_{\mathrm{int}}l=\mu_0NlI$ et $B_{\mathrm{int}}=\mu_0NI$.

### Continuité à travers une nappe de courant

La nappe porte une densité surfacique $\vec j_s$. La normale $\vec n_{12}$ est orientée de la région 1 vers la région 2. Une petite boîte traversant la nappe, dont la hauteur tend vers zéro, donne
$$\iint(\vec B_2-\vec B_1)\cdot\vec n_{12}\,dS=0,$$
donc $(\vec B_2-\vec B_1)\cdot\vec n_{12}=0$ : **la composante normale est continue**.

Un contour rectangulaire traversant la nappe est ensuite aplati. Le courant vaut l’intégrale de $\vec j_s$ dans la direction transverse au segment de longueur $dl$ ; Ampère donne
$$(\vec B_1-\vec B_2)\times\vec n_{12}=\mu_0\vec j_s,$$
soit $\vec n_{12}\times(\vec B_2-\vec B_1)=\mu_0\vec j_s$. **La composante tangentielle présente un saut** lié au courant surfacique.

### Choix de la méthode de calcul

- Biot et Savart est pratique quand on sait additionner les contributions vectorielles, notamment pour un circuit filiforme.
- La conservation du flux permet de prolonger une information connue dans une autre région.
- Ampère est efficace lorsqu’une symétrie rend la circulation calculable sur un contour choisi.

Toujours commencer par les symétries des courants. La rubrique est imprimée « III.2.4 » par erreur ; elle appartient au chapitre II.

## II.3. Dipôle magnétique — pages PDF 20–24

### Développement du champ d’une spire lointaine

Une spire plane quelconque, centrée en $O$, porte un courant permanent $I$. Poser $\vec r=\overrightarrow{OM}$, $\vec\rho=\overrightarrow{OP}$, $\vec r'=\overrightarrow{PM}=\vec r-\vec\rho$, $\vec u=\vec r/r$. Pour $r\gg\rho$ :
$$\frac{\vec r'}{r'^3}=\frac{\vec u}{r^2}-\frac{\vec\rho}{r^3}+\frac{3(\vec u\cdot\vec\rho)\vec u}{r^3}+O(\rho^2/r^4).$$
Dans Biot et Savart, le premier terme donne $\oint d\vec\rho\times\vec u=\vec0$. Le second utilise
$$\frac12\oint\vec\rho\times d\vec\rho=S\vec n,$$
car $\vec\rho\times d\vec\rho/2$ représente l’aire orientée d’un triangle élémentaire.

Pour le troisième, dans une base $(\vec e_1,\vec e_2)$ du plan de la spire, on utilise $\oint d(xy)=0$, donc $\oint x\,dy=-\oint y\,dx$, et $\oint x\,dx=\oint y\,dy=0$. On obtient
$$\oint d\vec\rho\,(\vec\rho\cdot\vec u)=S\vec n\times\vec u,$$
puis
$$\vec B(M)\simeq\frac{\mu_0I}{4\pi r^3}\left[2S\vec n-3\vec u\times(S\vec n\times\vec u)\right].$$
Définir le moment dipolaire magnétique $\vec{\mathcal M}=IS\vec n$. Avec $\vec u\times(\vec{\mathcal M}\times\vec u)=\vec{\mathcal M}-\vec u(\vec u\cdot\vec{\mathcal M})$ :
$$\boxed{\vec B(M)=\frac{\mu_0}{4\pi r^3}\left[3\vec u(\vec{\mathcal M}\cdot\vec u)-\vec{\mathcal M}\right]
=-\frac{\mu_0}{4\pi}\operatorname{grad}\frac{\vec{\mathcal M}\cdot\vec u}{r^2}.}$$
Le signe égal désigne ici le champ dans l’approximation dipolaire. Les termes multipolaires négligés deviennent significatifs près de la spire.

En coordonnées sphériques, avec l’axe polaire porté par $\vec{\mathcal M}$ :
$$B_r=\frac{\mu_0}{4\pi r^3}2\mathcal M\cos\theta,\quad B_\theta=\frac{\mu_0}{4\pi r^3}\mathcal M\sin\theta,\quad B_\varphi=0.$$
L’équation des lignes $dr/B_r=r\,d\theta/B_\theta$ donne $dr/r=2\cot\theta\,d\theta$ et
$$r=r_0\left(\frac{\sin\theta}{\sin\theta_0}\right)^2.$$
Le cours demande surtout de comprendre et reproduire la démonstration. Les lignes de champ ne sont pas des lignes de norme constante.

### Modèle du dipôle en physique

Le champ a la même structure que celui du dipôle électrique $\vec p=q\vec d$ :
$$\vec E=-\frac1{4\pi\varepsilon_0}\operatorname{grad}\frac{\vec p\cdot\vec u}{r^2}.$$
En magnétisme, le dipôle n’est pas décomposable en deux charges magnétiques isolées ; il constitue le premier terme de la description des sources localisées.

Dans le modèle de Bohr, l’électron de charge $q=-e$ tourne à vitesse angulaire $\omega$ sur un cercle de rayon $a_0$. Sur des temps longs devant $T=2\pi/\omega$, il équivaut à un courant $I=q/T=q\omega/(2\pi)$. Ainsi
$$\vec{\mathcal M}=\frac{q\omega a_0^2}{2}\vec n=\frac q{2m}\vec L.$$
$q/(2m)$ est le facteur gyromagnétique orbital de ce modèle. Un objet neutre peut avoir un moment magnétique : il suffit que les mouvements des charges positives et négatives ne se compensent pas.

Le texte présente trois catégories : diamagnétiques, décrits comme sans champ intrinsèque et avec des moments aléatoires ; paramagnétiques, dont les moments s’orientent sous champ extérieur ; ferromagnétiques, avec orientation persistante et aimantation permanente.

> **Rectification conceptuelle :** la description du diamagnétisme par des moments permanents simplement aléatoires est insuffisante et se confond avec le paramagnétisme sans champ. Le diamagnétisme correspond à une réponse induite opposée au champ appliqué. La classification très schématique de la source est conservée ci-dessus comme telle.

Le cours évoque le champ approximativement dipolaire terrestre, l’effet dynamo associé aux courants internes des astres, les inversions solaires tous les onze ans et une inversion terrestre située « environ 700 000 ans » auparavant. Il cite des variations de l’axe terrestre d’environ $15'$ par an, un décalage d’une dizaine de degrés avec l’axe de rotation, et donne « $90^\circ$ pour Neptune ». **Ces valeurs et le bilan des questions alors ouvertes sont ceux du texte de 2001–2002, sans actualisation ni validation astrophysique dans cette transcription.**

## III.1. Force sur une particule chargée — pages PDF 25–28

Historiquement, l’action macroscopique de Laplace fut observée avant la force microscopique de Lorentz ; le cours adopte l’ordre inverse pour la présentation.

### Force de Lorentz

Dans un référentiel galiléen,
$$\vec F=q(\vec E+\vec v\times\vec B)=\vec F_e+\vec F_m,\quad \vec F_e=q\vec E,\quad \vec F_m=q\vec v\times\vec B.$$
La partie magnétique ne travaille pas :
$$\frac d{dt}\left(\frac12mv^2\right)=m\vec v\cdot\frac{d\vec v}{dt}=q\vec v\cdot(\vec v\times\vec B)=0$$
lorsqu’elle est la seule force. Le cours rappelle l’estimation en $(v/c)^2$ de l’interaction entre charges mobiles.

Les forces magnétiques instantanées entre deux particules ne satisfont pas, prises seules, à l’action-réaction : si la particule 1 se dirige vers 2, $\vec v_1\times\vec u_{12}=0$, donc $\vec B_1(M_2)=0$ ; avec une autre direction de $\vec v_2$, l’action réciproque peut être non nulle. **Précision :** cette observation ne supprime pas la conservation de la quantité de mouvement du système complet, qui inclut le champ.

### Trajectoire dans un champ uniforme

Décomposer $\vec v=\vec v_\parallel+\vec v_\perp$. Alors $d\vec v_\parallel/dt=0$ et $d\vec v_\perp/dt=(q/m)\vec v_\perp\times\vec B$. Pour $\vec B=B\vec e_z$ :
$$\dot v_x=\omega v_y,\quad \dot v_y=-\omega v_x,\quad \omega=\frac{qB}{m}.$$
Les composantes satisfont $\ddot v_i=-\omega^2v_i$. Avec $\vec v_\perp(0)=v_{\perp0}\vec e_x$ :
$$v_x=v_{\perp0}\cos\omega t,\quad v_y=-v_{\perp0}\sin\omega t,$$
$$x=\frac{v_{\perp0}}\omega\sin\omega t,\qquad y=\frac{v_{\perp0}}\omega\cos\omega t,$$
avec le choix d’origine employé dans la source. Le mouvement transverse est circulaire, de rayon de Larmor $R_L=m v_{\perp0}/(|q|B)$ et de pulsation positive $|q|B/m$ ; le sens dépend du signe de $q$. Le dessin montre un électron tournant dans le sens direct. En ajoutant la vitesse parallèle constante, la trajectoire générale est une hélice.

Le rayon augmente avec la quantité de mouvement transverse et diminue lorsque $B$ augmente. Le cours parle de piégeage transverse ; cela n’empêche pas la translation suivant le champ. Le champ propre de la particule est négligé dans ce calcul.

### Champ électrique et changement de référentiel

Dans un référentiel où la particule est momentanément au repos, le terme $q\vec v\times\vec B$ disparaît, tandis qu’une action électrique subsiste. La source introduit le champ électromoteur $\vec E_m=\vec v\times\vec B$ par la relation de faible vitesse
$$\vec E'\simeq\vec E_s+\vec v\times\vec B.$$
Elle en tire deux points : un champ électrique général peut avoir une circulation non nulle, contrairement à un champ électrostatique ; les champs électrique et magnétique se mélangent lors d’un changement de référentiel, qui relève des transformations de Lorentz. Le calcul classique des trajectoires est réservé ici à $v\ll c$. Le texte admet l’invariance de la charge et distingue « masse au repos » et « masse dynamique » (impulsion divisée par la vitesse).

> **Limites du raisonnement source :** l’égalité $\vec F'=\vec F$ n’est pas une loi relativiste générale. Un référentiel lié à une particule accélérée n’est pas globalement galiléen ; on doit parler de référentiel inertiel instantanément comobile. La formule ci-dessus restitue l’approximation utilisée, sans la présenter comme transformation relativiste exacte.

## III.2. Actions sur un circuit fermé — pages PDF 28–33

### Force de Laplace

Pour des espèces de porteurs $(n_\alpha,q_\alpha,\vec v_\alpha)$, $\vec j=\sum_\alpha n_\alpha q_\alpha\vec v_\alpha$. La force sur $d^3V$ est
$$d^3\vec F=\sum_\alpha n_\alpha q_\alpha(\vec E+\vec v_\alpha\times\vec B)\,d^3V.$$
Dans un conducteur localement neutre à l’échelle considérée, $\sum n_\alpha q_\alpha=0$, donc
$$d^3\vec F=(\vec j\times\vec B)\,d^3V.$$
Pour un fil mince où le champ est pratiquement constant sur une section, $d^3V=dS\,dl$ et l’intégration sur la section donne
$$d\vec F=I\,d\vec l\times\vec B,\qquad \vec F=I\oint_C d\vec l\times\vec B.$$
Le circuit est un solide ; chaque force élémentaire s’applique au milieu de l’élément correspondant. La présentation suppose des courants permanents et insiste sur l’intégration sur le circuit fermé. Pour une forme complexe, la méthode énergétique est souvent plus simple.

Le cours explique le travail macroscopique de Laplace par la transmission de l’action des porteurs au réseau du conducteur, avec apparition du champ de Hall. Il distingue ainsi la force sur le solide de la force magnétique microscopique, dont la puissance sur une charge est nulle. Il annonce aussi que, pour deux circuits fermés parcourus par des courants permanents, l’action-réaction est retrouvée.

### Deux fils infinis et ancienne définition de l’ampère

Deux fils parallèles séparés de $d$ portent $I_1,I_2$. Si $\vec u_{12}$ va du fil 1 vers le fil 2, les courants de même sens donnent
$$\frac{d\vec F_{1/2}}{dl}=-\frac{\mu_0I_1I_2}{2\pi d}\vec u_{12}=-\frac{d\vec F_{2/1}}{dl}.$$
Ils s’attirent ; des courants opposés se repoussent. **La ligne finale du PDF omet le facteur $dl$ tout en conservant $d\vec F$ : la formule est ici écrite par unité de longueur.**

L’édition définit l’ampère à partir de deux fils parallèles à un mètre l’un de l’autre exerçant une force de $2\times10^{-7}\ \mathrm{N/m}$. Cette définition métrologique est rapportée dans son contexte historique.

### Moment des forces et dynamique de rotation

Pour le centre d’inertie $O$ :
$$\vec\Gamma_O=\oint_C\overrightarrow{OP}\times d\vec F,\qquad
\vec J_O=\int\overrightarrow{OP}\times\vec v\,dm.$$
Dans les axes principaux d’inertie retenus,
$$\vec J_O=\sum_{i=1}^3 I_i\Omega_i\vec u_i=[I]\vec\Omega,\quad I_i=\int r_i^2\,dm,$$
où $r_i$ est la distance à l’axe $\Delta_i$. Le théorème du moment cinétique donne $d\vec J_O/dt=\sum\vec\Gamma_{\mathrm{ext}}$. Pour une rotation autour du seul axe $Oz$, avec $I_z$ constant :
$$I_z\ddot\theta=\sum\Gamma_z.$$
Les titres « II.2.3 » à « II.2.5 » imprimés dans cette partie relèvent du chapitre III.

### Dipôle dans un champ uniforme

La résultante vaut $\vec F=I(\oint d\vec l)\times\vec B=\vec0$. Le couple, lui, n’est pas nécessairement nul :
$$\vec\Gamma=I\oint\overrightarrow{OP}\times(d\overrightarrow{OP}\times\vec B)
=I\oint d\overrightarrow{OP}\,(\overrightarrow{OP}\cdot\vec B),$$
car $\oint\overrightarrow{OP}\cdot d\overrightarrow{OP}=0$. Dans le plan $(x,y)$ de la spire, $\oint x\,dy=S$ et $\oint y\,dx=-S$ donnent
$$\vec\Gamma=IS(B_x\vec e_y-B_y\vec e_x)=\vec{\mathcal M}\times\vec B.$$
Le schéma montre une spire inclinée : le couple tend à aligner son moment dipolaire avec le champ. Le mot « couple » évite de confondre le moment des forces avec le moment dipolaire. Le cours relie cette rotation à l’orientation macroscopique d’un aimant dans un champ extérieur.

### Complément : action-réaction entre circuits

Pour deux circuits disjoints $C_1,C_2$, poser $r=P_1P_2$ et $\vec u_{12}=\overrightarrow{P_1P_2}/r$. En combinant Laplace et Biot et Savart :
$$\vec F_{1/2}=\frac{\mu_0I_1I_2}{4\pi}\oint_{C_2}\oint_{C_1}\frac{d\vec P_2\times(d\vec P_1\times\vec u_{12})}{r^2}.$$
Le double produit est $d\vec P_1(d\vec P_2\cdot\vec u_{12})-\vec u_{12}(d\vec P_2\cdot d\vec P_1)$. Le premier terme s’annule après intégration sur le circuit fermé : à $P_1$ fixé,
$$\oint_{C_2}\frac{d\vec P_2\cdot\vec u_{12}}{r^2}=\oint\frac{dr}{r^2}=0.$$
Il reste
$$\vec F_{1/2}=-\frac{\mu_0I_1I_2}{4\pi}\oint_{C_1}\oint_{C_2}\frac{\vec u_{12}}{r^2}(d\vec P_1\cdot d\vec P_2)=-\vec F_{2/1}.$$

> **Coquille rectifiée :** les dernières intégrales imprimées page 31 perdent le dénominateur $r^2$ ; il doit être conservé. L’échange des intégrales se justifie ici pour des circuits disjoints réguliers, sans exiger la « symétrie de la fonction » évoquée dans le texte.

## III.3. Énergie potentielle d’interaction — pages PDF 34–38

### Théorème de Maxwell et flux coupé

Lors d’un déplacement $d\vec r$ d’un élément $d\vec l$ :
$$d^2W=(I\,d\vec l\times\vec B)\cdot d\vec r
=I\vec B\cdot(d\vec r\times d\vec l)=I\,d^2\Phi_c.$$
La surface balayée par l’élément définit le flux coupé. En sommant sur le circuit, $dW=I\,d\Phi_c$, puis, pour un courant constant,
$$W=I\Phi_c.$$
Le dessin montre le ruban balayé par un élément et son orientation $(d\vec r,d\vec l,\vec n)$.

Pour un champ extérieur statique, les surfaces initiale $S_i$, finale $S_f$ et balayée $S_d$ ferment un volume. La conservation du flux, puis la remise en cohérence des orientations avec celle du circuit, donnent
$$\Phi_c=\Phi_f-\Phi_i=\Delta\Phi.$$
Le signe est algébrique ; cette identification avec la variation totale du flux suppose que le champ ne varie pas pendant le déplacement.

### Énergie potentielle

Le théorème de l’énergie cinétique donne $\Delta E_c=W=I\Delta\Phi$. À courant maintenu constant, on définit une énergie potentielle mécanique d’interaction telle que $dW_m=-dW$ :
$$W_m=-I\Phi+\text{constante}.$$
Le choix de zéro est libre, souvent à l’infini lorsque cela convient à la configuration.

### Force, couple et travaux virtuels

Pour une translation du circuit :
$$dW_m=\sum_i\frac{\partial W_m}{\partial x_i}dx_i=-\sum_iF_i\,dx_i,$$
d’où
$$F_i=-\frac{\partial W_m}{\partial x_i},\qquad \vec F=-\operatorname{grad}W_m=I\operatorname{grad}\Phi.$$
La dérivation se fait à courant fixé. Des déformations du circuit peuvent aussi modifier le flux, même sans déplacement de son centre.

Pour une rotation infinitésimale $d\vec\alpha=\sum_i d\alpha_i\vec u_i$, $d\vec r=d\vec\alpha\times\vec r$. Alors
$$dW=\int d\vec F\cdot d\vec r=\sum_i\Gamma_i\,d\alpha_i=I\,d\Phi,$$
donc $\Gamma_i=I\,\partial\Phi/\partial\alpha_i$.

Pour un petit dipôle de moment fixé, $I\Phi=\vec{\mathcal M}\cdot\vec B$ et
$$\vec F=\operatorname{grad}(\vec{\mathcal M}\cdot\vec B),\quad
\vec\Gamma=\vec{\mathcal M}\times\vec B.$$
La seconde relation vient de $d\vec{\mathcal M}=d\vec\alpha\times\vec{\mathcal M}$ ; cette voie est plus rapide que l’intégration directe.

### Règle du flux maximum

Un déplacement à partir d’un équilibre stable doit rencontrer une force de rappel : le travail magnétique est négatif, donc $I\,\Delta\Phi<0$. En orientant le circuit pour $I>0$, l’équilibre stable correspond à un maximum local du flux, ou à un minimum de $W_m=-I\Phi$. Cette règle concerne les degrés de liberté accessibles au circuit.

## IV.1. Lois de l’induction — pages PDF 39–43

### Expériences de Faraday

Sur un même cylindre, deux enroulements sont disposés : l’un est relié à une pile et un interrupteur, l’autre à un galvanomètre. Un courant constant dans le premier ne produit pas de courant permanent dans le second. Une déviation transitoire apparaît à la fermeture ou à l’ouverture de l’interrupteur, ainsi que lors du déplacement du second circuit.

Une seconde expérience approche ou éloigne un aimant d’une boucle conductrice reliée au galvanomètre. L’aimant immobile ne provoque pas de courant ; son déplacement en produit un, dont le sens change avec celui du mouvement et dont l’amplitude augmente avec la rapidité. Changer la résistance du circuit modifie $I$, mais pas la force électromotrice $e=RI$ dans l’expérience décrite.

**Loi de Faraday :**
$$\boxed{e=-\frac{d\Phi}{dt}.}$$
Le phénomène dépend intrinsèquement du temps et dépasse donc la magnétostatique stricte.

### Force électromotrice et force de Lorentz

La puissance transmise aux porteurs par une force motrice s’écrit, avec $\vec j=nq\vec v$,
$$P=\iiint n\vec F\cdot\vec v\,dV
=I\oint_C\frac{\vec F}{q}\cdot d\vec l=Ie.$$
Ainsi $e=P/I=\oint(\vec F/q)\cdot d\vec l$. Un champ purement électrostatique a une circulation nulle sur un circuit fermé : $\oint\vec E_s\cdot d\vec l=V(A)-V(A)=0$. Il faut donc une action électromotrice pour entretenir le courant.

Pour un circuit en mouvement, l’expression utilisée est
$$e=\oint_C(\vec E+\vec v\times\vec B)\cdot d\vec l,$$
où $\vec v$ désigne la vitesse locale du conducteur. Dans des champs statiques, $\oint\vec E_s\cdot d\vec l=0$ et
$$e=-\frac1{dt}\oint\vec B\cdot(\vec v\,dt\times d\vec l)=-\frac{d\Phi_c}{dt}.$$
Pour un contour matériel fermé déplacé ou déformé dans un champ statique, $d\Phi_c=d\Phi$, ce qui redonne Faraday. Le schéma décrit le ruban de surface balayé par un déplacement $d\vec r=\vec v\,dt$.

### Deux difficultés et leur résolution

**Roue de Barlow.** Un disque métallique tourne autour d’un axe fixe, dans un champ magnétique, avec un contact glissant sur son bord (cuve de mercure dans l’expérience décrite) et une connexion électrique à l’axe. Un courant apparaît alors que le flux géométrique à travers le disque ne change pas. Il faut revenir à la force de Lorentz et tenir compte des portions conductrices mobiles et des contacts : le contour du circuit n’est pas un unique contour matériel transporté avec le disque. Le flux total de la roue seul ne suffit pas au calcul.

**Circuit fixe, champ variable.** Approcher un aimant d’une boucle immobile crée une fém bien que le flux coupé par déplacement soit nul. La variation du champ engendre un champ électrique non électrostatique :
$$\oint_C\vec E\cdot d\vec l=-\iint_S\frac{\partial\vec B}{\partial t}\cdot d\vec S.$$
Pour un circuit matériel mobile dans un champ variable, les deux effets se combinent :
$$e=\oint_C(\vec E+\vec v\times\vec B)\cdot d\vec l
=-\iint_{S(t)}\frac{\partial\vec B}{\partial t}\cdot d\vec S-\frac{d\Phi_c}{dt}
=-\frac{d\Phi}{dt}.$$
Le premier terme est lié à la variation temporelle du champ ; le second au mouvement ou à la déformation du circuit. La source note que la vitesse de dérive des porteurs dans le fil n’est pas la vitesse d’ensemble : sa force magnétique transverse est compensée, dans le modèle quasi statique présenté, par le champ de Hall.

### Loi de Lenz et signes

Les effets de l’induction s’opposent à la variation qui les produit. Cette loi exprime le signe moins de Faraday. En approchant un circuit du pôle nord d’un aimant, le courant induit crée un champ qui réduit l’augmentation du flux et une action mécanique qui s’oppose au rapprochement.

Pour déterminer le signe : choisir un sens de parcours ; en déduire la normale par la règle du tire-bouchon ; calculer le flux algébrique ; appliquer $e=-d\Phi/dt$ ; déterminer le courant par l’équation électrique (par $I=e/R$ dans le cas résistif simple). Lenz permet de vérifier le sens physique obtenu.

## IV.2. Induction mutuelle et auto-induction — pages PDF 43–45

Pour deux circuits orientés, le champ créé par le premier donne à travers le second
$$\Phi_{12}=\iint_{S_2}\vec B_1\cdot d\vec S_2
=\left[\frac{\mu_0}{4\pi}\iint_{S_2}\oint_{C_1}\frac{d\vec l\times\overrightarrow{PM}}{PM^3}\cdot d\vec S_2\right]I_1=M_{12}I_1.$$
En échangeant les indices, $\Phi_{21}=M_{21}I_2$. Ces coefficients dépendent de la géométrie, de la distance et des orientations des circuits ; le dessin choisit des orientations donnant des coefficients négatifs.

Le résultat de réciprocité est $M_{12}=M_{21}=M$, en henrys. L’argument énergétique du cours compare les travaux de deux déplacements relatifs :
$$dW_2=I_2d\Phi_{12}=I_1I_2dM_{12},\qquad dW_1=I_1d\Phi_{21}=I_1I_2dM_{21}.$$
L’égalité des variations de l’interaction donne $dM_{12}=dM_{21}$, puis l’annulation à séparation infinie fixe la constante à zéro. L’énergie potentielle mécanique d’interaction à courants fixés est
$$W_{\mathrm{int}}=-MI_1I_2+\text{constante}.$$

Un circuit crée aussi un flux à travers lui-même : $\Phi=LI$. $L$, l’auto-inductance ou « self », s’exprime en henrys et est positive pour le circuit physique. La source la décrit par la géométrie ; en présence de matériaux magnétiques, leur réponse intervient également. La formule filiforme idéale exige une taille de fil non nulle pour traiter convenablement le flux propre.

## IV.3. Régimes variables et énergie — pages PDF 45–48

### Régime quasi statique

L’établissement du champ sur un circuit de taille $l$ prend un temps de l’ordre de $l/c$. Pour des variations de période caractéristique $T$, le critère retenu est
$$T\gg l/c.$$
Les champs suivent alors les courants suffisamment vite pour employer les relations de magnétostatique à chaque instant dans l’approximation du cours.

### Fém induites

À géométrie fixe, $L$ constant : $e=-L\,dI/dt$. La self s’oppose aux variations du courant. Une bobine augmente le flux lié au circuit ; un noyau de fer doux peut amplifier le champ. Pour $N$ spires identiques couplées au même flux,
$$e_{\mathrm{circuit}}=N e_{\mathrm{spire}},\qquad \Phi_{\mathrm{circuit}}=N\Phi_{\mathrm{spire}}.$$
Pour deux circuits à coefficients constants :
$$\Phi_1=L_1I_1+MI_2,\quad \Phi_2=L_2I_2+MI_1,$$
$$e_1=-L_1\frac{dI_1}{dt}-M\frac{dI_2}{dt},\quad e_2=-M\frac{dI_1}{dt}-L_2\frac{dI_2}{dt}.$$
Une variation du courant dans le premier peut ainsi créer un courant dans un second circuit fermé non alimenté, qui réagit à son tour sur le premier.

### Énergie stockée

L’énergie $-I\Phi_{\mathrm{ext}}$ d’interaction mécanique ne doit pas être appliquée au flux propre comme s’il s’agissait d’un champ extérieur indépendant. Pour établir le courant d’une self sans pertes, le générateur doit fournir
$$P_m=-ei=L i\frac{di}{dt}=\frac d{dt}\left(\frac12Li^2\right).$$
À partir d’un courant nul, l’énergie stockée est
$$\boxed{W_m=\frac12LI^2.}$$
L’analogie électrostatique est $W_e=Q^2/(2C)$. Les pertes exigent un travail fourni supérieur à l’énergie stockée.

La source écrit, lorsqu’un champ extérieur est supposé indépendant du circuit, $W_m=LI^2/2-I\Phi_{\mathrm{ext}}$. **Cette écriture combine énergie propre et potentiel mécanique d’interaction sous l’hypothèse indiquée ; elle ne doit pas être confondue avec l’énergie du champ de deux circuits alimentés que l’on établit ensemble.**

Pour deux circuits linéaires à géométrie fixe, l’intégration de la puissance d’établissement donne
$$W_m=-\int(e_1I_1+e_2I_2)\,dt
=\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2.$$
Les termes croisés sont $M(I_1\,dI_2+I_2\,dI_1)=M\,d(I_1I_2)$. **Coquille rectifiée page imprimée 45 :** la première ligne répète $e_1I_1$ dans la deuxième intégrale ; il faut $e_2I_2$. Le signe positif du terme croisé correspond ici à l’énergie stockée, tandis que $-MI_1I_2$ était le potentiel mécanique à courants maintenus constants.

### Bilan d’un circuit électrique

La convention du cours est $V_A-V_B=RI-e$, avec le courant de $A$ vers $B$. Pour une self, on obtient $V_A-V_B=RI+L\,dI/dt$.

> **Erreur de signe page imprimée 46 :** la source ajoute un terme $-d\Phi_{\mathrm{ext}}/dt$ à ce dernier membre. Avec les conventions immédiatement précédentes, $e_{\mathrm{ext}}=-d\Phi_{\mathrm{ext}}/dt$ et donc $RI-e$ donne au contraire **$+d\Phi_{\mathrm{ext}}/dt$**. L’orientation du flux doit rester la même dans les deux relations.

Pour un circuit série RLC alimenté par $U$, avec $I=dQ/dt$ :
$$U=RI+L\frac{dI}{dt}+\frac QC,$$
$$UI=RI^2+\frac d{dt}\left(\frac12LI^2\right)+\frac d{dt}\left(\frac{Q^2}{2C}\right)
=P_J+\frac d{dt}(W_m+W_e).$$
Une partie de la puissance est dissipée par effet Joule, le reste modifie l’énergie électromagnétique. Pour le circuit libre $U=0$, cette énergie décroît et se transforme en chaleur si $R>0$.

## Formulaire de magnétostatique — page PDF 49

Les domaines d’application et orientations sont ceux des sections précédentes.

| Rubrique | Formule |
| --- | --- |
| Charge mobile | $\vec B(M)=\dfrac{\mu_0q}{4\pi}\dfrac{\vec v\times\overrightarrow{PM}}{PM^3}$ |
| Ensemble de charges | $\vec B(M)=\sum_i\dfrac{\mu_0q_i}{4\pi}\dfrac{\vec v_i\times\overrightarrow{P_iM}}{P_iM^3}$ |
| Distribution continue | $\vec B(M)=\dfrac{\mu_0}{4\pi}\iiint\dfrac{\vec j(P)\times\overrightarrow{PM}}{PM^3}\,d^3V$ |
| Circuit filiforme | $\vec B(M)=\dfrac{\mu_0I}{4\pi}\oint\dfrac{d\vec l\times\overrightarrow{PM}}{PM^3}$ |
| Flux conservatif | $\oiint_S\vec B\cdot d\vec S=0$ |
| Ampère | $\oint_C\vec B\cdot d\vec l=\mu_0I_{\mathrm{int}}$ |
| Moment dipolaire | $\vec{\mathcal M}=IS\vec n$ |
| Couple sur un dipôle | $\vec\Gamma=\vec{\mathcal M}\times\vec B$ |
| Force sur un dipôle | $\vec F=\operatorname{grad}(\vec{\mathcal M}\cdot\vec B)$ |
| Lorentz | $\vec F=q(\vec E+\vec v\times\vec B)$ |
| Laplace | $\vec F=I\oint_C d\vec l\times\vec B$ |
| Force par l’énergie, courant fixé | $\vec F=-\operatorname{grad}W_m=I\operatorname{grad}\Phi$ |
| Couple par l’énergie | $\vec\Gamma=\sum_i\Gamma_i\vec u_i$, $\Gamma_i=I\,\partial\Phi/\partial\alpha_i$ |
| Maxwell | $dW=\vec F\cdot d\vec r=I\,d\Phi_c$ (translation) |
| Potentiel d’interaction | $W_m=-I\Phi+\mathrm{Cst}$ |
| Énergie propre stockée | $W_m=LI^2/2$ |
| Induction mutuelle | $M=\Phi_{12}/I_1=\Phi_{21}/I_2$ |
| Auto-inductance | $L=\Phi/I$ |

La loi de Faraday est donnée sous ses formes équivalentes pour un contour matériel :
$$e=-\frac{d\Phi}{dt}=-\iint_S\frac{\partial\vec B}{\partial t}\cdot d\vec S-\frac{d\Phi_c}{dt}
=\oint_C(\vec E+\vec v\times\vec B)\cdot d\vec l.$$
