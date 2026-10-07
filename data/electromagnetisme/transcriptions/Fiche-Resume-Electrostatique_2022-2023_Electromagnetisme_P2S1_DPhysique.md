---
source: "PREING2-S1/Electromagnetisme/Fiche-Resume-Electrostatique_2022-2023_Electromagnetisme_P2S1_DPhysique.pdf"
pages: 23
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des 23 pages ; texte et formules saisis manuellement (encodage du texte natif défectueux) ; erreurs du support signalées séparément
---

# Fiches de cours — électrostatique, dipôles, particules chargées, magnétostatique et induction

## Page 1

### Résumé du cours d'électrostatique — 1. Calcul direct du champ et du potentiel

L2S3, version du 7 novembre 2013. Charges ponctuelles $q_i$ en $P_i$ (Coulomb) :

$$\vec E(M)=\sum_i\frac{q_i}{4\pi\varepsilon_0}\frac{\overrightarrow{P_iM}}{P_iM^3}=\sum_i\frac{q_i}{4\pi\varepsilon_0}\frac{\vec u_{P_iM}}{P_iM^2},\qquad
\phi(M)=\sum_i\frac{q_i}{4\pi\varepsilon_0P_iM},$$

avec potentiel nul à l'infini.

Pour une distribution continue :

$$d\vec E_P(M)=\frac{dq(P)}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3}=\frac{dq(P)}{4\pi\varepsilon_0}\frac{\vec u_{PM}}{PM^2},$$

$$\vec E(M)=\int_{P\in D}d\vec E_P(M),\qquad \phi(M)=\int_{P\in D}\frac{dq(P)}{4\pi\varepsilon_0PM}.$$

Distribution linéique : $dq=\lambda(P)\,d\ell(P)$, intégrale simple ; surfacique : $dq=\sigma(P)\,dS(P)$, intégrale double ; volumique : $dq=\rho(P)\,d\tau(P)$, intégrale triple. Le schéma relie l'élément de charge en $P$ au point $M$ par $\vec u_{PM}$.

Force sur une charge $Q$ placée en $M$ : $\vec F=Q\vec E(M)$.

**Symétries.** Si $\Pi$ est un plan de symétrie des charges :

1. Pour $M\in\Pi$, $\vec E(M)\parallel\Pi$. Les charges égales en $P,P'$ symétriques donnent une somme $d\vec E_P(M)+d\vec E_{P'}(M)$ parallèle au plan.
2. Pour $M,M'$ symétriques par rapport à $\Pi$, $\vec E(M')$ est le symétrique de $\vec E(M)$. Le dessin représente les contributions des mêmes charges en $P,P'$ aux deux points d'observation.

## Page 2

### Antisymétries, invariances et potentiel

Si $\Pi^*$ est un plan d'antisymétrie des charges :

1. Pour $M\in\Pi^*$, $\vec E(M)\perp\Pi^*$. Les charges opposées en $P,P'$ donnent une somme normale au plan.
2. Pour $M,M'$ symétriques, $-\vec E(M')$ est le symétrique de $\vec E(M)$.

> Le texte explicatif sous la seconde propriété recopie « même charge » et $\Pi$ ; dans cette partie, il s'agit de charges opposées et du plan $\Pi^*$, conformément à la propriété encadrée.

**Invariances.** Si la distribution est invariante par toute translation suivant un axe, la norme de $\vec E$ et $\phi$ ne dépendent pas de la coordonnée correspondante. Si elle est invariante par toute rotation autour d'un axe, ils ne dépendent pas de l'angle de rotation autour de cet axe.

**Lien champ–potentiel :**

$$\vec E=-\overrightarrow{\operatorname{grad}}\phi,\qquad d\phi=\overrightarrow{\operatorname{grad}}\phi\cdot d\vec\ell=-\vec E\cdot d\vec\ell.$$

En cartésiennes : $\overrightarrow{\operatorname{grad}}\phi=\partial_x\phi\,\vec u_x+\partial_y\phi\,\vec u_y+\partial_z\phi\,\vec u_z$. En cylindriques ou sphériques, si $\phi$ dépend seulement de $r$, $\overrightarrow{\operatorname{grad}}\phi=(d\phi/dr)\vec u_r$.

Circulation de $A$ à $B$ suivant $\Gamma$ :

$$C_{\Gamma,A B}(\vec E)=\int_{\Gamma,A\to B}\vec E\cdot d\vec\ell=-\int_A^B d\phi=\phi(A)-\phi(B).$$

Elle ne dépend pas du chemin : circulation conservative. Sur un contour fermé : $\oint_\Gamma\vec E\cdot d\vec\ell=0$.

## Page 3

### Lignes de champ, équipotentielles et 2. Théorème de Gauss

Une ligne de champ est une courbe tangente au champ en chacun de ses points et orientée dans son sens. Si deux lignes se croisent en $M$, $\vec E(M)=\vec0$ ou le champ n'est pas défini (diverge). Un tube de champ est un ensemble de lignes s'appuyant sur un contour fermé ; le dessin montre un tube s'élargissant.

Une surface équipotentielle réunit les points de même potentiel. Elle est perpendiculaire aux lignes de champ ; le potentiel décroît dans le sens de $\vec E$, direction de sa plus grande diminution.

Flux d'un champ $\vec A$ à travers $S$ :

$$\Phi=\iint_S\vec A(M)\cdot d\vec S(M),\qquad \|d\vec S\|=dS.$$

$d\vec S$ est normal à la surface élémentaire ; son sens est au choix pour une surface ouverte. Pour une surface fermée entourant un volume fini, la normale est obligatoirement sortante et l'intégrale est notée $\oiint$.

**Théorème de Gauss :**

$$\oiint_S\vec E(P)\cdot d\vec S(P)=\frac{Q_{\rm int}}{\varepsilon_0},$$

$Q_{\rm int}$ étant la charge intérieure. Méthode : rechercher les symétries pour la direction du champ ; utiliser les invariances pour sa norme ; choisir une surface de Gauss fermée passant par $M$, où le champ est tangent ou normal ; calculer le flux et la charge intérieure pour déterminer $\vec E(M)$.

## Page 4

### Continuité et 3. Formes locales

$\phi$ est continu lorsqu'il ne diverge pas, en particulier pour des charges volumiques ou surfaciques régulières. Il diverge sur les charges idéalisées ponctuelles ou linéiques. $\vec E$ est continu dans une distribution volumique régulière ou en l'absence de charges, discontinu sur une charge surfacique, divergent sur une charge ponctuelle ou linéique.

**Divergence :** pour un volume élémentaire $d\tau$ entourant $M$, bordé par $S$ :

$$\oiint_S\vec A(P)\cdot d\vec S(P)=\operatorname{div}\vec A\,d\tau,\qquad
\operatorname{div}\vec A=\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}.$$

Le support donne, pour $\vec A=A(r)\vec u_r$ en cylindriques et sphériques, $\operatorname{div}\vec A=\partial A/\partial r$.

> Cette dernière formule omet le facteur géométrique. Il faut $(1/r)d(rA)/dr$ en cylindriques et $(1/r^2)d(r^2A)/dr$ en sphériques.

**Laplacien :** $\Delta f=\operatorname{div}(\overrightarrow{\operatorname{grad}}f)$ ; en cartésiennes, $\Delta f=\partial_x^2f+\partial_y^2f+\partial_z^2f$.

**Rotationnel :** pour une surface élémentaire $d\vec S$ bordée par $\Gamma$, orientée selon la règle de la main droite :

$$\oint_\Gamma\vec A(P)\cdot d\vec\ell(P)=\overrightarrow{\operatorname{rot}}\vec A\cdot d\vec S,$$

$$\overrightarrow{\operatorname{rot}}\vec A=(\partial_yA_z-\partial_zA_y)\vec u_x+(\partial_zA_x-\partial_xA_z)\vec u_y+(\partial_xA_y-\partial_yA_x)\vec u_z.$$

| Loi | Forme globale | Forme locale |
| --- | --- | --- |
| Circulation électrostatique | $\oint_\Gamma\vec E\cdot d\vec\ell=0$ | $\overrightarrow{\operatorname{rot}}\vec E=\vec0$ |
| Gauss | $\oiint_S\vec E\cdot d\vec S=Q_{\rm int}/\varepsilon_0$ | $\operatorname{div}\vec E=\rho/\varepsilon_0$ |

Équation de Poisson : $\Delta\phi+\rho/\varepsilon_0=0$.

## Page 5

### 4. Conducteurs et condensateurs

Dans un conducteur parfait à l'équilibre électrostatique, des charges mobiles peuvent se déplacer librement ; $\vec E_{\rm intérieur}=\vec0$, $\phi_{\rm intérieur}$ constant, $\rho_{\rm intérieur}=0$ (charges mobiles et fixes réunies). La charge nette est sur la surface, de densité $\sigma$.

**Théorème de Coulomb :** juste à l'extérieur, près du point $P$ de la surface,

$$\vec E=\frac{\sigma(P)}{\varepsilon_0}\vec n,$$

$\vec n$ normale unitaire sortante.

Un condensateur comporte deux conducteurs parfaits à l'équilibre dont deux surfaces $S_1,S_2$ sont en influence totale : toute ligne partant de l'une arrive sur l'autre et réciproquement. Leurs charges sont opposées : $Q_2=-Q_1$.

La capacité positive $C$, dépendant de la géométrie dans le milieu considéré, vérifie :

$$Q_1=C\bigl(\phi_1-\phi_2\bigr)=CU,\qquad U=\phi_1-\phi_2.$$

Énergie : $E_{\rm pot}=CU^2/2=Q^2/(2C)$. Condensateur plan : $C=\varepsilon_0S/e$, $S$ aire, $e$ épaisseur.

En série : $1/C_{\rm eq}=1/C_1+1/C_2$. En parallèle (dérivation) : $C_{\rm eq}=C_1+C_2$.

## Page 6

### Le dipôle électrostatique — I. Modèle et II. Action exercée

L2S3 — Électromagnétisme. Les formules à connaître par cœur sont entourées.

Dipôle : deux charges ponctuelles $+q$ en $P$ et $-q$ en $N$, de séparation $NP$ petite devant les autres distances. Moment électrique :

$$\vec p=q\overrightarrow{NP}\quad(\mathrm{C\,m}).$$

Molécule neutre polarisée : barycentres des charges positives et négatives distincts. Exemples HCl, H₂O. Les dessins opposent H₂O coudée, polaire, à CO₂ linéaire, non polaire. Dans H₂O, chaque H porte $\delta^+$ et O porte $2\delta^-$ ; dans CO₂, les oxygènes portent $\delta^-$ et le carbone $2\delta^+$, avec barycentres confondus.

Unité chimique : debye, $1\,\mathrm D=(1/3)10^{-29}\,\mathrm{C\,m}$. Valeurs données : $p(\mathrm{H_2O})=1{,}82\,\mathrm D$, $p(\mathrm{HCl})=1{,}08\,\mathrm D$. Les molécules apolaires peuvent se polariser dans un champ extérieur. Dipôle rigide : distance $NP$ fixe.

**Approximation dipolaire :** $NP\ll OM$, donc $NP/OM\ll1$. On développe potentiel et champ au plus bas ordre en ce rapport.

## Page 7

### Potentiel et champ d'un dipôle — calculs faits en TD

Coordonnées sphériques d'axe $(Oz)=(NP)$, $O$ milieu de $[NP]$ : $\vec r=\overrightarrow{OM}=r\vec u_r$, $\vec r_P=\overrightarrow{PM}$, $\vec r_N=\overrightarrow{NM}$, $\vec p=qNP\vec u_z$.

$$V(M)=\frac1{4\pi\varepsilon_0}\left(-\frac q{r_N}+\frac q{r_P}\right).$$

$$\vec r_N=\frac12\overrightarrow{NP}+\vec r,\quad r_N=\sqrt{\frac14NP^2+r^2+\overrightarrow{NP}\cdot\vec r},$$

$$\frac1{r_N}=\frac1r\left(1+\frac14\frac{NP^2}{r^2}+\frac{\overrightarrow{NP}\cdot\vec r}{r^2}\right)^{-1/2}
\simeq\frac1r\left(1-\frac{\overrightarrow{NP}\cdot\vec r}{2r^2}+\cdots\right)=\frac1r\left(1-\frac{NP}{2r}\cos\theta+\cdots\right).$$

De même :

$$\vec r_P=-\frac12\overrightarrow{NP}+\vec r,\quad r_P=\sqrt{\frac14NP^2+r^2-\overrightarrow{NP}\cdot\vec r},$$

$$\frac1{r_P}=\frac1r\left(1+\frac14\frac{NP^2}{r^2}-\frac{\overrightarrow{NP}\cdot\vec r}{r^2}\right)^{-1/2}
\simeq\frac1r\left(1+\frac{\overrightarrow{NP}\cdot\vec r}{2r^2}+\cdots\right)=\frac1r\left(1+\frac{NP}{2r}\cos\theta+\cdots\right).$$

Ainsi $V(M)\simeq qNP\cos\theta/(4\pi\varepsilon_0r^2)=\vec p\cdot\vec r/(4\pi\varepsilon_0r^3)$ (résultat non exigé par cœur).

Champ :

$$\vec E(M)=\frac q{4\pi\varepsilon_0}\left(\frac{\vec r_P}{r_P^3}-\frac{\vec r_N}{r_N^3}\right),$$

$$\frac{\vec r_P}{r_P^3}\simeq\left(\vec r-\frac{\overrightarrow{NP}}2\right)\frac1{r^3}\left(1+\frac{3NP}{2r}\cos\theta+\cdots\right),\quad
\frac{\vec r_N}{r_N^3}\simeq\left(\vec r+\frac{\overrightarrow{NP}}2\right)\frac1{r^3}\left(1-\frac{3NP}{2r}\cos\theta+\cdots\right).$$

## Page 8

### Champ dipolaire et lignes de champ

$$\vec E(M)\simeq\frac q{4\pi\varepsilon_0r^3}\left(3\frac{NP}{r}\cos\theta\,\vec r-\overrightarrow{NP}\right)
=\frac1{4\pi\varepsilon_0r^3}\left(3\frac{\vec p\cdot\vec r}{r^2}\vec r-\vec p\right),$$

soit

$$\vec E(M)\simeq\frac p{4\pi\varepsilon_0r^3}(2\cos\theta\vec u_r+\sin\theta\vec u_\theta).$$

> Dans l'expression vectorielle intermédiaire du PDF, le facteur $q$ est conservé à tort alors que $\vec p=q\overrightarrow{NP}$ est déjà introduit ; la formule ci-dessus et la formule sphérique imprimée utilisent le coefficient correct.

Cette formule n'est pas à connaître par cœur. On peut la retrouver par $\vec E=-\overrightarrow{\operatorname{grad}}V$. Pour le dipôle : $V\sim1/r^2$, $E\sim1/r^3$ ; pour une charge ponctuelle : $V\sim1/r$, $E\sim1/r^2$.

Le plan contenant $M$ et $(NP)$ est un plan de symétrie ; $\vec E(M)$ lui appartient. Symétrie de rotation autour de $(NP)$.

Figures : lignes de champ rouges, équipotentielles bleues, orthogonales. Une vue à grande distance représente l'approximation dipolaire ; une autre montre séparément les deux charges au voisinage. Attention : les lignes électriques ne se referment pas sur elles-mêmes.

Référence affichée : http://www.sciences.univ-nantes.fr/sites/genevieve_tulloue/Elec/Champs/Index_Champs.html.

## Page 9

### III. Dipôle dans un champ uniforme et IV. Champ non uniforme

**Dipôle rigide, champ extérieur uniforme $\vec E$ :** résultante $\vec F=\vec F_P+\vec F_N=\vec0$ (couple), moment $\vec{\mathcal M}=\vec p\wedge\vec E$. À l'équilibre, le moment est nul : le dipôle libre s'aligne. Équilibre stable si $\vec p$ et $\vec E$ sont de même sens, instable s'ils sont opposés.

Dipôle non rigide : $\vec p$ dépend de $\vec E$. Polarisation induite (hors programme L2S3) d'un atome ou d'une molécule apolaire : pour un système isotrope, $\vec p_{\rm induit}=\alpha\varepsilon_0\vec E$, $\alpha$ polarisabilité.

Énergie d'un dipôle permanent : $E_{\rm pot}=-\vec p\cdot\vec E+\text{constante}$.

**Champ extérieur non uniforme**, $O$ milieu de $[NP]$ :

$$\vec F=q\bigl(\vec E(P)-\vec E(N)\bigr)=q\Delta\vec E,\qquad \vec{\mathcal M}\simeq\vec p\wedge\vec E(O).$$

Le dipôle libre tend à s'aligner dans le champ local et à se déplacer vers les régions de champ intense. Pour $NP$ petit : $\Delta\vec E\simeq d\vec E$,

$$E_{\rm pot}\simeq-\vec p\cdot\vec E(O)+\text{constante},\qquad \vec F=-\overrightarrow{\operatorname{grad}}E_{\rm pot}\simeq\overrightarrow{\operatorname{grad}}(\vec p\cdot\vec E).$$

## Page 10

### Mouvement d'une particule chargée dans $\vec E$ et $\vec B$

Les formules à connaître par cœur sont encadrées.

**1. Force de Lorentz**, particule de masse $m$, charge $q$, vitesse $\vec v$ :

$$\vec F=q\vec E+q\vec v\wedge\vec B=\vec F_e+\vec F_m,\qquad \mathcal P=\vec F\cdot\vec v=q\vec E\cdot\vec v.$$

La force magnétique ne travaille pas. Pour les particules étudiées (électron, ion, molécule chargée), le poids est négligé devant la force de Lorentz.

**2. Champ électrostatique uniforme stationnaire :**

$$m\vec a=q\vec E,\quad \vec v=\frac qm\vec E\,t+\vec v_0,\quad \overrightarrow{OM}=\frac q{2m}\vec E\,t^2+\vec v_0t+\overrightarrow{OM}_0.$$

Mouvement parabolique. $E_{\rm pot}=q\phi+\text{constante}$, $\vec E=-\overrightarrow{\operatorname{grad}}\phi$ ; énergie mécanique conservée :

$$E_m=E_c+E_{\rm pot}=\frac12mv^2+q\phi=\text{constante}.$$

**3. Champ magnétique uniforme stationnaire :**

$$m\vec a=q\vec v\wedge\vec B,\qquad \vec B=B\vec u_z\ \Longrightarrow\ \vec a=\frac{qB}{m}\vec v\wedge\vec u_z.$$

## Page 11

### Mouvement dans un champ magnétique — énergie et exemples

$E_m=E_c$ est constant, donc $\|\vec v\|=v$ constant.

- Si $\vec B\parallel\vec v_0$, $\vec F_m=\vec0$ : mouvement rectiligne uniforme, $\vec v(t)=\vec v_0$.
- Si $\vec B\perp\vec v_0$, mouvement circulaire uniforme :

$$R=\frac{mv_0}{|q|B},\qquad \omega=\frac{|q|B}{m},\qquad T=\frac{2\pi}{\omega}=\frac{2\pi m}{|q|B}.$$

Cas quelconque (exercice) : trajectoire en hélice, rayon $R=mv_{0\perp}/(|q|B)$, avec $\vec v_0=\vec v_{0\perp}+\vec v_{0\parallel}$, $\vec v_{0\parallel}\parallel\vec B$, $\vec v_{0\perp}\perp\vec B$.

Les figures montrent les sens de courbure opposés des ions et électrons dans un champ sortant de la feuille, puis une hélice autour de l'axe du champ.

## Page 12

### 4. Cyclotron et synchrotron — 5. Loi d'Ohm

Principe des accélérateurs (non exigé par cœur) :

- **Cyclotron :** champ magnétique uniforme dans les deux demi-disques, région de champ électrique dans l'entrefer, trajectoire en spirale des protons accélérés jusqu'à leur sortie à grande vitesse.
- **Synchrotron :** source d'ions, accélérateur linéaire, injecteur, aimants disposés sur un anneau, cavités accélératrices et aimants d'extraction donnant les faisceaux d'ions. Photo : ESRF Grenoble. Schéma : Encyclopædia Britannica, 2009.

Application à l'électrostatique des milieux conducteurs :

**Loi d'Ohm locale**, conducteur ohmique isotrope : $\vec j=\gamma\vec E$, $\gamma$ conductivité, $\rho=1/\gamma$ résistivité.

**Loi d'Ohm globale :** pour un conducteur parcouru par $I$, de différence de potentiel $U$, il existe une résistance positive $R$ telle que $U=RI$. Le dessin utilise la convention récepteur.

## Page 13

### Résistance et 6. Force de Laplace

Unité SI de résistance : ohm, $\Omega=\mathrm V/\mathrm A$. Fil de section constante $S$, longueur $L$ et résistivité $\rho$ : $R=\rho L/S$.

Deux résistances en série : $R=R_1+R_2$ ; en parallèle : $1/R=1/R_1+1/R_2$.

Force de Laplace sur le circuit filiforme $AC$ parcouru par $I$ :

$$\vec F_{\rm Laplace}=\int_{P\in\mathrm{circuit}}I\,d\vec\ell(P)\wedge\vec B(P).$$

Si $\vec B$ est uniforme :

$$\vec F_{\rm Laplace}=I\left(\int_{A}^{C}d\vec\ell\right)\wedge\vec B=I\overrightarrow{AC}\wedge\vec B.$$

## Page 14

### Champ magnétique — calcul et propriétés — 1. Distribution de courant

But : calcul en régime permanent et dans l'ARQS, régimes lentement variables : magnétostatique. Les formules à connaître par cœur sont encadrées.

Toutes les charges créent un champ électrique ; les charges en mouvement créent un champ magnétique. Le support considère un conducteur parcouru par un courant, globalement neutre : charges fixes compensant les porteurs mobiles. Dans ce modèle, il crée un champ magnétique sans champ électrique dû à une charge nette.

**Intensité :** charge traversant la section $S$ par unité de temps, $I=dQ/dt$. En régime permanent, $I$ est indépendant de $t$ ; en ARQS, $I(t)$ varie lentement.

**Densité volumique :**

$$I=\iint_S\vec j\cdot d\vec S,\qquad \vec j=nq\vec v\quad\text{(porteurs identiques de même vitesse)},\qquad \vec j=\sum_kn_kq_k\vec v_k.$$

$n$ ou $n_k$ est le nombre de porteurs mobiles par unité de volume.

**Courant surfacique** (groupe prépa-ENSI seulement) : une dimension très petite devant les deux autres ; nappe d'épaisseur négligeable. Le schéma montre la largeur $L$, la normale dans la nappe et $\vec j_s$.

## Page 15

### Distribution de courant — suite, symétries et conservation

Densité surfacique : $I=\int_L\vec j_s\cdot\vec n\,dL$, $L$ largeur, $\vec n$ unitaire perpendiculaire à $L$. Courant linéique : deux dimensions très petites devant la troisième.

Une transformation laisse la distribution invariante si elle reste identique à elle-même. Invariances possibles : translation, rotation autour d'un axe. Pour $M,M'$ symétriques :

- Plan de symétrie $\Pi$ : $I\,d\vec\ell(M')$ est le symétrique de $I\,d\vec\ell(M)$.
- Plan d'antisymétrie $\Pi^*$ : $-I\,d\vec\ell(M')$ est le symétrique de $I\,d\vec\ell(M)$.

Conservation de la charge $Q$ intérieure à $S$ :

$$-\frac{dQ}{dt}=I_{\rm sortant}=\oiint_S\vec j\cdot d\vec S,\qquad \operatorname{div}\vec j+\frac{\partial\rho}{\partial t}=0.$$

En régime permanent, $\oiint_S\vec j\cdot d\vec S=0$ pour toute surface fermée. Le courant est constant le long d'un fil. Loi des nœuds sur la figure : $I_1=I_2+I_3$ ($I_1$ entrant, $I_2,I_3$ sortants).

## Page 16

### 2. Loi de Biot et Savart

Postulée en 1820 par Jean-Baptiste Biot et Félix Savart à partir de l'expérience. Un élément de courant $I\,d\vec\ell(P)$ produit :

$$d\vec B_P(M)=\frac{\mu_0}{4\pi}\frac{I\,d\vec\ell(P)\wedge\overrightarrow{PM}}{PM^3}.$$

Perméabilité du vide donnée : $\mu_0=4\pi\times10^{-7}\,\mathrm{H\,m^{-1}}=4\pi\times10^{-7}\,\mathrm{kg\,m\,A^{-2}\,s^{-2}}$, unité également $\mathrm{T\,m\,A^{-1}}$ ; H : henry. $\varepsilon_0\mu_0c^2=1$.

Avec $r=PM$ et $\vec u_{PM}=\overrightarrow{PM}/PM$ :

$$\vec B(M)=\int_{P\in\mathrm{fil}}d\vec B_P(M)=\frac{\mu_0}{4\pi}\int_{\rm fil}\frac{I\,d\vec\ell\wedge\overrightarrow{PM}}{PM^3}=\frac{\mu_0}{4\pi}\int_{\rm fil}\frac{I\,d\vec\ell\wedge\vec u_{PM}}{r^2}.$$

Distributions non linéiques (prépa-ENSI seulement) :

$$\vec B(M)=\frac{\mu_0}{4\pi}\iiint_D\frac{\vec j(P)\wedge\overrightarrow{PM}}{PM^3}\,d\tau=\frac{\mu_0}{4\pi}\iiint_D\frac{\vec j\wedge\vec u_{PM}}{r^2}\,d\tau,$$

$$\vec B(M)=\frac{\mu_0}{4\pi}\iint_D\frac{\vec j_s(P)\wedge\overrightarrow{PM}}{PM^3}\,dS=\frac{\mu_0}{4\pi}\iint_D\frac{\vec j_s\wedge\vec u_{PM}}{r^2}\,dS.$$

Continuité : $\vec B$ continu dans une distribution volumique, discontinu sur une nappe surfacique, divergent sur une distribution linéique. Les modèles surfaciques et linéiques idéalisent respectivement une et deux dimensions négligeables.

> La dernière phrase imprimée inverse « une » et « deux » pour ces modèles ; les définitions précédentes donnent l'ordre correct.

## Page 17

### 3. Topographie, invariances et symétries du champ magnétique

Ligne de champ : courbe tangente à $\vec B$ en tout point. Tube : ensemble de lignes s'appuyant sur un contour fermé $C$. Deux lignes ne peuvent se couper, sauf si $B=0$. Le support décrit des lignes fermées tournant autour des courants selon la règle de la main droite ou du tire-bouchon.

> Cette description de lignes fermées concerne les exemples usuels : la divergence nulle n'impose pas que toute ligne soit fermée.

**Invariances :** translation suivant $(Oz)$, champ indépendant de $z$ (idem $x,y$) ; rotation autour de $(Oz)$, norme indépendante de $\theta$ en cylindriques ; rotations autour de $O$, norme indépendante de $\theta,\varphi$ en sphériques.

**Symétrie de la distribution par rapport à $\Pi$ :** en $M\in\Pi$, $\vec B(M)\perp\Pi$ ; si $M,M'$ sont symétriques, $\vec B(M')$ est l'opposé du symétrique de $\vec B(M)$. Les dessins montrent la compensation des composantes des contributions de $P,P'$.

**Antisymétrie par rapport à $\Pi^*$ :** en $M\in\Pi^*$, le champ est dans le plan ; pour deux points symétriques, $\vec B(M')$ est le symétrique de $\vec B(M)$. Le mot « colinéaire » dans le support signifie ici « contenu dans le plan ».

## Page 18

### 4. Propriétés du champ magnétique

**Flux :** $F_B(S)=\iint_S\vec B\cdot d\vec S$, unité weber (Wb). Pour toute surface fermée :

$$\oiint_S\vec B\cdot d\vec S=0,\qquad \operatorname{div}\vec B=0.$$

Postulat de l'électromagnétisme, valable aussi en régime variable. Le champ est à flux conservatif : même flux à travers les différentes sections d'un tube, et à travers les surfaces de même contour orienté. Il n'existe pas de monopôle magnétique dans ce modèle.

**Théorème d'Ampère**, André-Marie Ampère (1775–1836) : en régime permanent ou dans l'ARQS considérée, pour tout contour fermé $C$ :

$$\oint_C\vec B\cdot d\vec\ell=\mu_0 I_{\rm enlacés}=\mu_0\sum_k\gamma_kI_k,$$

$\gamma_k=+1$ ou $-1$ selon le sens de $I_k$ par rapport à l'orientation du contour (main droite). La circulation de $\vec B$ n'est pas conservative en général ; il ne dérive pas en général d'un potentiel scalaire.

Distribution volumique :

$$\oint_C\vec B\cdot d\vec\ell=\mu_0\iint_S\vec j\cdot d\vec S,$$

pour toute surface $S$ bordée par $C$, orientée suivant le sens de $d\vec\ell$.

## Page 19

### Application d'Ampère et 5. Dipôle magnétique

Méthode : analyser symétries et invariances ; choisir un contour fermé passant par $M$ où la circulation est simple (champ tangent ou normal) ; calculer $I_{\rm enlacé}$ ; appliquer $\oint_C\vec B\cdot d\vec\ell=\mu_0I_{\rm enlacé}$.

Exemples : fil infini rectiligne (voir TD) ; solénoïde infini, sans effets de bord :

$$\vec B_{\rm extérieur}=\vec0,\qquad \vec B_{\rm intérieur}=\mu_0nI\vec u,$$

$n$ spires par unité de longueur, $\vec u$ axial orienté par le courant (main droite).

**Vecteur surface** d'une surface $S$ bordée par le contour orienté $C$ :

$$\vec S=\iint_Sd\vec S.$$

Il dépend de $C$, pas du choix de surface. Pour un cercle de rayon $R$ : $\vec S=\vec n\pi R^2$. Ne pas confondre $\vec S$ et l'aire $S=\iint_SdS$ ; pour une surface non plane, $\|\vec S\|\ne S$ en général.

**Moment magnétique** d'un circuit filiforme plan fermé parcouru par $I$ dans le sens de $C$ : $\vec\mu=I\vec S$.

**Dipôle magnétique :** distribution de courants permanents de moment non nul, de dimensions petites devant la distance d'observation (approximation dipolaire). Les figures montrent l'orientation commune de la normale, du vecteur surface et du moment.

## Page 20

### Champ et lignes d'un dipôle magnétique — hors programme

À grande distance, le champ dépend des coordonnées de $M$ et du moment $\vec\mu$. Modèle : spire circulaire d'axe $(Oz)$, $\theta$ angle polaire, $\varphi$ azimut :

$$\vec B(M)=\frac{\mu_0\mu}{4\pi r^3}(2\cos\theta\vec u_r+\sin\theta\vec u_\theta)
=\frac{\mu_0}{4\pi r^3}\bigl(3(\vec\mu\cdot\vec u_r)\vec u_r-\vec\mu\bigr)
=\frac{\mu_0}{4\pi}\frac{3(\vec\mu\cdot\vec r)\vec r-r^2\vec\mu}{r^5}.$$

Les spectres illustrent la similitude à grande distance entre les lignes du dipôle électrique et celles du dipôle magnétique. Les expressions ont la même structure, avec leurs constantes respectives. Une spire est équivalente à grande distance à un aimant simple : le sens du moment pointe vers le pôle nord de l'aimant ; l'autre extrémité est le pôle sud.

## Page 21

### Dipôle magnétique dans un champ extérieur — hors programme

Dans $\vec B_0$ :

$$\vec{\mathcal M}=\vec\mu\wedge\vec B_0\quad\text{(forces de Laplace)},\qquad E_{\rm pot}=-\vec\mu\cdot\vec B_0+\text{constante},\qquad \vec F=\overrightarrow{\operatorname{grad}}(\vec\mu\cdot\vec B_0).$$

Le dipôle mobile s'oriente parallèlement à $\vec B_0$, dans son sens. Exemple : une boussole, assimilable à une spire, s'oriente dans le champ terrestre. Son pôle nord se dirige vers le pôle sud magnétique terrestre, situé près du pôle nord géographique.

## Page 22

### Résumé du cours d'induction — L2S4, version du 7 mars 2014

**Loi générale :**

$$\overrightarrow{\operatorname{rot}}\vec E=-\frac{\partial\vec B}{\partial t},\qquad \vec E=-\overrightarrow{\operatorname{grad}}\phi-\frac{\partial\vec A}{\partial t}.$$

Le support définit $\vec E_{\rm statique}=-\overrightarrow{\operatorname{grad}}\phi$ et le champ électromoteur de Neumann $\vec E_{\rm Neumann}=-\partial_t\vec A$.

Force de Lorentz sur une charge mobile :

$$\vec F=q\vec E+q\vec v\wedge\vec B=q\vec E_{\rm statique}+\vec F_{\rm induit},\qquad \vec F_{\rm induit}=-q\frac{\partial\vec A}{\partial t}+q\vec v\wedge\vec B.$$

**Force électromotrice (f.e.m.) :** travail de la force d'induction par unité de charge sur le circuit,

$$e=\oint_{\rm circuit}\frac{\vec F_{\rm induit}}q\cdot d\vec\ell.$$

Deux cas indiqués : circuit mobile et $\vec B$ permanent ; circuit fixe. Le support donne dans les deux cas

$$e=-\frac{\partial}{\partial t}\iint_{S(\rm circuit)}\vec B\cdot d\vec S,$$

puis affirme que cette formule n'est pas valable en général pour un circuit mobile et un champ non permanent. La f.e.m. agit comme un générateur de tension ; son signe positif suit l'orientation du contour associée à $d\vec S$.

> Précision : avec une dérivée **totale** du flux à travers une surface mobile, la loi du flux $e=-d\Phi_B/dt$ inclut les deux contributions pour un circuit matériel fermé dans les conditions usuelles. La dérivée partielle seule ne rend pas compte du déplacement du contour.

**Loi de Lenz :** champs et courants induits s'opposent à la cause qui les fait naître ; dans un circuit, à la variation du flux magnétique.

**Inductance mutuelle**, circuits $C_1,C_2$ :

$$F_1(C_2)=\iint_{S(C_2)}\vec B_{I_1}\cdot d\vec S=MI_1,\qquad e_2=-M\frac{dI_1}{dt}.$$

Le support qualifie $M$ de constante positive, appelée coefficient d'inductance mutuelle.

> Le signe de l'inductance mutuelle dépend en réalité des orientations choisies pour les deux circuits ; $M$ n'est pas nécessairement positif.

## Page 23

### Inductance mutuelle et auto-induction — suite

Réciprocité : $M(\text{circuit 1 dans circuit 2})=M(\text{circuit 2 dans circuit 1})$.

L'inductance d'un circuit dans lui-même est notée $L$, inductance ou coefficient d'auto-induction. Pour une géométrie fixe :

$$e=-L\frac{dI}{dt},$$

avec $e$ comptée positivement dans le même sens que $I$. Le support indique que l'auto-induction est généralement négligeable sauf dans les bobines.

Exemple donné pour un solénoïde sans effets de bord :

$$L=\mu_0n^2\pi R^2,$$

$n$ nombre de spires par unité de longueur, $R$ rayon d'une spire.

> Il manque la longueur $\ell$ pour une inductance totale : $L=\mu_0n^2\pi R^2\ell$. La formule imprimée correspond à l'inductance **par unité de longueur**.
