# Électromagnétisme 1 — Chapitre 1 : le champ électrostatique

> Source : `PREING2-S1/Electromagnetisme/CM-Chapitre1-champ_2024-2025_Electromagnetisme_P2S1_ABoumiz.pdf`, 41 pages. Attribution et année d’après le nom du fichier.
> Vérification du 10 octobre 2026 : lecture des 41 pages rendues et confrontation au texte natif ; formules incorporées en images (pages 26–27 notamment) retranscrites en LaTeX, figures décrites, animations regroupées. Les lacunes et les rectifications sont explicites.

## I. Force électrostatique — pages 2–9

### 1. Loi de Coulomb — pages 2–4

Deux charges ponctuelles $q_1$ en $A$ et $q_2$ en $B$, séparées par $r$, exercent l’une sur l’autre des forces électrostatiques. Le dessin montre $q_1>0$, $q_2<0$ et deux forces dirigées l’une vers l’autre.

La force exercée par la charge 1 sur la charge 2 est
$$\vec F_{1/2}=K\frac{q_1q_2}{r^2}\vec u,$$
avec $\vec u$ un vecteur unitaire de la droite $(AB)$, orienté de $A$ vers $B$ pour cette convention. Dans l’air assimilé au vide,
$$K=9\times10^9\ \mathrm{N\,m^2\,C^{-2}}=\frac1{4\pi\varepsilon_0}.$$
$\varepsilon_0$ est la permittivité du vide. Les normes des deux forces sont égales :
$$\|\vec F_{1/2}\|=\|\vec F_{2/1}\|=K\frac{|q_1q_2|}{r^2}.$$

### 2. Analogie avec la gravitation — page 5

Pour deux masses ponctuelles $m_1,m_2$ distantes de $r$ :
$$F_{\mathrm{gravi}}=G\frac{m_1m_2}{r^2},\qquad F_{\mathrm{Coulomb}}=K\frac{|q_1q_2|}{r^2}.$$
$G$ est la constante gravitationnelle. Les dessins représentent les deux objets reliés par un segment de longueur $r$.

### 3. Exemples — pages 6–9

**Exemple 1.** Calculer la force de répulsion entre deux particules $\alpha$ (noyaux d’hélium contenant deux protons et deux neutrons), distantes de $10^{-11}\ \mathrm{cm}$. La valeur absolue de la charge élémentaire est $e=1{,}6\times10^{-19}\ \mathrm C$.

Le schéma porte $q_1=q_2=2e$ et rappelle que deux charges de même signe se repoussent. L’application de Coulomb donne $F=K(2e)^2/r^2$. La valeur affichée est $F=92\times10^{-3}\ \mathrm N$.

> **Précision de notation et contrôle numérique :** avec $r=10^{-11}\ \mathrm{cm}=10^{-13}\ \mathrm m$, on obtient $F=9{,}216\times10^{-2}\ \mathrm N$, soit $92{,}16\times10^{-3}\ \mathrm N$ : l’arrondi affiché est cohérent. En revanche, la notation « charge de l’électron $e^-=+1{,}6\times10^{-19}$ C » désigne ici sa valeur absolue ; la charge de l’électron est négative. Aucune modification de l’unité de distance n’est nécessaire.

**Exemple 2.** Quelle charge doit porter une particule de masse $m=2\ \mathrm g$ pour rester en équilibre dans un champ électrostatique vertical dirigé vers le bas, de norme $500\ \mathrm{V/m}$ ? On donne $g=9{,}8\ \mathrm{m/s^2}$.

Le dessin montre le poids vers le bas et la force électrique vers le haut. La seule relation fournie est
$$m\vec g+\vec F_{\mathrm{électrostatique}}=\vec0.$$
**Le calcul numérique de la charge n’est pas donné dans le PDF.**

## II. Champ électrostatique — pages 10–14

### 1. Charge ponctuelle — pages 10–11

Une charge $q$ placée en $P$ crée au point $M$, avec $r=PM$ et $\vec u=\overrightarrow{PM}/PM$,
$$\vec E(M)=\frac1{4\pi\varepsilon_0}\frac q{r^2}\vec u.$$
Le champ est dirigé de $P$ vers $M$ pour $q>0$, et de $M$ vers $P$ pour $q<0$ ; les deux schémas illustrent ces sens.

### 2. Distribution de charges ponctuelles — page 12

Chaque charge $q_i$ est reliée à $M$ par un segment de longueur $r_i$ et de direction unitaire $\vec u_i$. Par superposition :
$$\vec E(M)=\sum_{i=1}^n\frac1{4\pi\varepsilon_0}\frac{q_i}{r_i^2}\vec u_i.$$

### 3. Distribution continue — pages 13–14

**3.1. Distribution linéaire.** Un élément de longueur $dl$ d’un fil porte $dq=\lambda\,dl$, où $\lambda$ est la densité linéique de charge. Cet élément, en $P$, crée en $M$ le champ élémentaire $d\vec E$, dirigé selon $\overrightarrow{PM}$ pour une charge positive. Ainsi
$$\vec E(M)=\frac1{4\pi\varepsilon_0}\int_{\text{fil}}\frac{\lambda\,dl}{r^2}\vec u.$$

**3.2. Distributions surfaciques de charges.** **3.3. Distributions volumiques de charges.** Ces deux titres apparaissent seuls page 14 : aucune définition ni formule n’est fournie sous ces rubriques.

## III. Symétries des distributions de charges — pages 15–16

**1. Symétrie cylindrique :** $\rho(r,\theta,z)=\rho(r)$. La distribution est invariante par rotation autour de $(Oz)$ et par translation le long de cet axe.

**2. Symétrie sphérique :** $\rho(r,\theta,\varphi)=\rho(r)$. La distribution est invariante par rotation autour du centre.

**3. Exemple.** Le dessin page 16 est un cercle centré en $O$, dans le plan $(x,y)$, partagé en deux demi-cercles : la moitié gauche porte $+\lambda$, la moitié droite $-\lambda$. Les axes $x$ et $y$ sont dessinés horizontalement et verticalement ; $z$ est indiqué au centre. Aucun calcul ni commentaire supplémentaire n’accompagne cet exemple.

## IV. Propriétés de symétrie du champ — pages 17–18

**Symétrie plane.** Le champ électrostatique appartient au plan de symétrie de la distribution de charges en chacun des points de ce plan où le champ est défini.

**Antisymétrie plane.** Le champ électrostatique est perpendiculaire au plan d’antisymétrie de la distribution en chacun des points de ce plan où il est défini.

## V. Lignes et tubes de champ — pages 19–21

Une ligne de champ est une courbe tangente en chacun de ses points au vecteur champ électrostatique ; elle est orientée dans le sens du champ. Le schéma page 19 montre plusieurs vecteurs tangents à une même courbe.

La planche page 20 présente quatre illustrations : une paire de charges opposées avec des flèches de champ, un tracé légendé « charges ponctuelles opposées », quatre charges ponctuelles aux sommets d’un carré et deux fils parallèles de même charge. Les tracés montrent aussi des familles de courbes transversales ; les légendes ne donnent pas d’équations ni de valeurs numériques.

L’ensemble de lignes de champ passant par le contour d’une section engendre une surface appelée tube de champ. Le dessin page 21 montre deux sections circulaires reliées par des lignes orientées de gauche à droite.

## VI. Champ sur l’axe d’une spire circulaire — pages 22–27

**Énoncé.** Une spire circulaire de rayon $R$ porte une densité linéique uniforme $\lambda>0$.

1. À partir des symétries, déterminer la direction du champ en tout point de son axe.
2. Déterminer son expression.

**Symétrie.** Pour $M$ sur l’axe $(Oz)$, tous les plans contenant $(OM)$ sont des plans de symétrie de charge. Le champ appartient à chacun de ces plans :
$$\vec E(M)=E_z\vec u_z.$$

**Calcul.** Le dessin place $M$ à l’altitude $z$, $P$ sur la spire, $PM=r=\sqrt{R^2+z^2}$, et $\alpha$ entre la direction de $d\vec E$ et l’axe. Un élément $dl$ porte $dq=\lambda\,dl$. Sa contribution axiale est
$$dE_z=\frac{dq}{4\pi\varepsilon_0r^2}\cos\alpha,\qquad \cos\alpha=\frac z{\sqrt{R^2+z^2}}=\frac zr.$$
Donc
$$dE_z=\frac{\lambda\,dl}{4\pi\varepsilon_0}\frac z{(R^2+z^2)^{3/2}}.$$
$z$ et $r$ sont constants lors de l’intégration sur la spire, et $\int_0^{2\pi R}dl=2\pi R$ :
$$E_z=\frac{\lambda R}{2\varepsilon_0}\frac z{(R^2+z^2)^{3/2}}.$$
La dernière page écrit également, pour $z\ne0$,
$$E_z=\frac{\lambda R}{2\varepsilon_0z^2}\cos^3\alpha.$$

## VII. Circulation et potentiel électrostatique — pages 28–30

Une charge $q$ est placée en $O$. Pour un déplacement élémentaire de $M$ vers un point voisin $M'$, la circulation élémentaire vaut
$$dC=\vec E\cdot\overrightarrow{MM'}=K\frac q{r^2}\,dr=d\!\left(-\frac{Kq}{r}\right).$$
Entre deux points à distances $r_1,r_2$ de $O$ :
$$C=-\frac q{4\pi\varepsilon_0}\int_{r_1}^{r_2}d\!\left(\frac1r\right)
=-\frac q{4\pi\varepsilon_0}\left(\frac1{r_2}-\frac1{r_1}\right).$$
La circulation est indépendante du chemin suivi ; elle dépend seulement des points de départ et d’arrivée. En posant
$$V(M)=\frac q{4\pi\varepsilon_0r},$$
on obtient $dC=-dV$.

## VIII. Théorème de Gauss — pages 31–41

### 1. Flux du champ électrostatique — pages 31–33

Le flux élémentaire de $\vec E(M)$ à travers une surface élémentaire $dS$ est
$$d\Phi=\vec E(M)\cdot d\vec S,\qquad d\vec S=\vec n\,dS.$$
Le schéma définit $\theta$ comme l’angle entre la normale $\vec n$ et $\vec E$. Pour une surface fermée, la normale est choisie vers l’extérieur ; le flux sortant est
$$\Phi=\oiint_S\vec E\cdot d\vec S.$$

### 2. Théorème — pages 34–38

Le flux sortant d’une surface fermée s’exprime en fonction des charges qu’elle contient. Pour une charge ponctuelle $q$ placée en $O$, choisir la sphère de centre $O$ et de rayon $r$ comme surface de Gauss. Le champ radial est parallèle à la normale et son coefficient radial est constant sur cette sphère :
$$\Phi=E(r)\oiint_S dS=E(r)4\pi r^2
=\frac1{4\pi\varepsilon_0}\frac q{r^2}\,4\pi r^2=\frac q{\varepsilon_0}.$$

**Énoncé général.** Le flux du champ électrostatique sortant d’une surface fermée est égal à la charge intérieure divisée par $\varepsilon_0$ :
$$\boxed{\oiint_S\vec E\cdot d\vec S=\frac{Q_{\mathrm{int}}}{\varepsilon_0}.}$$

### 3. Exemple : sphère pleine uniformément chargée — pages 39–41

Une sphère pleine, de centre $O$ et de rayon $R$, porte une charge totale $Q$ de densité volumique $\rho$ constante positive. Exprimer les résultats en fonction de $R$ et de $Q$.

1. À partir des symétries, déterminer la direction du champ en un point $M$ à distance $r$ du centre ; étudier les invariances (cette dernière demande figure page 39).
2. Par le théorème de Gauss, déterminer le champ à l’intérieur, puis à l’extérieur de la sphère.
3. En déduire le potentiel en tout point de l’espace.
4. Tracer l’allure de la norme du champ en fonction de $r$.

Les trois dernières pages ajoutent progressivement les questions. **Aucune correction de cet exemple n’est présente dans ce PDF.**
