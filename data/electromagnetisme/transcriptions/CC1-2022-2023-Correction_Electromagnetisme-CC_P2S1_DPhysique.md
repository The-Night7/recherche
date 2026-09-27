---
source: CC1-2022-2023-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 11 (grille de réponses page 7, rédactions manuscrites pages 8 à 11)
transcription: manuelle
---

# CC1 d'Électromagnétisme — 27 octobre 2022 (corrigé)

> **Note :** contrôle de 1 h 30, sans document ni calculatrice, 20 questions. Les questions à choix multiples n'ont qu'une bonne réponse ; les questions marquées ♣ sont à rédiger. Les réponses ci-dessous sont celles de la grille corrigée et des rédactions manuscrites de l'enseignant, vérifiées et détaillées.

## Questions de cours : potentiel, loi de Coulomb, théorème de Gauss

**Énoncé.** (5 points)

1. (0,5 point) Pour une distribution surfacique de charges, le potentiel électrique $V$ est :
    A) défini et continu en tout point de l'espace ;
    B) défini sur la surface chargée et non continu à la traversée de la surface ;
    C) non défini aux points où se trouvent les charges ;
    D) aucune de ces réponses n'est correcte.
2. (0,5 point) Le volume élémentaire en coordonnées cylindriques s'écrit : A) $dV = r^2\, dr\, d\theta\, dz$ ; B) $dV = r\, dr\, d\theta\, dz$ ; C) $dV = r^2 \sin\theta\, dr\, d\theta\, dz$ ; D) aucune de ces réponses.
3. (1 point) La force $\vec F_{1/2}$ exercée par la charge ponctuelle $q_1$ sur la charge ponctuelle $q_2$, située à la distance $r_{12}$, vaut :
    A) $\vec F_{1/2} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1 q_2}{r_{12}^3}\vec u_{1\to2}$ ;
    B) $\vec F_{2/1} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1 q_2}{r_{12}^2}\vec u_{1\to2}$ ;
    C) $\vec F_{1/2} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1 q_2}{r_{12}^2}\vec u_{1\to2}$ ;
    D) aucune de ces réponses.
4. (1 point) Soient les charges $q'$ en $M$ et $q$ en $P$. Le champ électrostatique en $M$ s'écrit : A) $\vec E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{PM^2}\overrightarrow{PM}$ ; B) $\vec E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q'}{PM^3}\overrightarrow{PM}$ ; C) $\vec E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{PM^3}\overrightarrow{PM}$ ; D) aucune de ces réponses.
5. (0,5 point) Puisque le champ $\vec E$ est à circulation conservative, on définit le potentiel électrostatique par : A) $\vec V = \overrightarrow{\operatorname{grad}}\, E$ ; B) $\vec E = -\overrightarrow{\operatorname{grad}}\, V$ ; C) $\vec E = \overrightarrow{\operatorname{grad}}\, V$ ; D) aucune de ces réponses.
6. (1 point) En étudiant les plans de symétrie de la distribution de charges, on trouve que :
    A) le champ $\vec E$ en $M$ est contenu dans tout plan $\Pi$ de symétrie passant par $M$ ;
    B) la direction de $\vec E$ en $M$ est celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    C) la direction de $\vec E$ en $M$ est celle de la droite intersection d'au moins deux plans d'antisymétrie passant par $M$ ;
    D) aucune de ces réponses.
7. (0,5 point) Le théorème de Gauss relie le flux $\Phi$ de $\vec E$ à travers une surface fermée $S$ à la charge intérieure $q_{\text{int}}$ contenue dans le volume $V$ délimité par $S$ : A) $\Phi = \oiint_S \vec E \cdot d\vec S = \dfrac{q_{\text{int}}}{\varepsilon_0}$ ; B) $\Phi = \iiint_V \vec E \cdot d\vec V = \dfrac{q_{\text{int}}}{\varepsilon_0}$ ; C) $\Phi = \oiint_S \vec E \cdot d\vec S = q_{\text{int}}$ ; D) aucune de ces réponses.

**Correction.**

1. **A.** Pour une distribution surfacique (densité $\sigma$ finie), le potentiel est défini et continu partout, y compris à la traversée de la surface ; c'est le **champ** qui subit une discontinuité ($\sigma/\varepsilon_0$ sur sa composante normale). Le potentiel n'est pas défini sur une charge ponctuelle ou linéique, pas sur une surface.
2. **B.** $dV = dr \times r\, d\theta \times dz = r\, dr\, d\theta\, dz$.
3. **C.** La force exercée par $q_1$ sur $q_2$ est portée par $\vec u_{1\to2}$, en $1/r_{12}^2$.
4. **C.** $\vec E(M) = \dfrac{q}{4\pi\varepsilon_0 PM^2}\dfrac{\overrightarrow{PM}}{PM} = \dfrac{q}{4\pi\varepsilon_0 PM^3}\overrightarrow{PM}$ : c'est la charge source $q$ en $P$ qui crée le champ.
5. **B.** $\vec E = -\overrightarrow{\operatorname{grad}}\, V$ : le champ est dirigé vers les potentiels décroissants.
6. **A.** En un point d'un plan de symétrie, $\vec E$ est contenu dans ce plan (en un point d'un plan d'antisymétrie, il lui est orthogonal).
7. **A.** $\oiint_S \vec E \cdot d\vec S = \dfrac{q_{\text{int}}}{\varepsilon_0}$ (le flux est une intégrale de surface ; la proposition C n'est pas homogène).

## Exercice 1 : Champ créé par trois charges ponctuelles

**Énoncé.** (7 points) Trois charges ponctuelles $+q$ (en $A$), $-q$ (en $B$) et $-q$ (en $C$) sont placées aux sommets d'un triangle équilatéral de côté $a$. On cherche le champ électrostatique $\vec E(O)$ créé au centre $O$ du triangle par ces trois charges.

> **Note :** la figure montre $A$ ($+q$) en haut, $C$ ($-q$) en bas à gauche et $B$ ($-q$) en bas à droite ; l'axe $y$ est vertical, dirigé vers le haut (de $O$ vers $A$), l'axe $x$ horizontal.

1. (Question 8, 1 point) L'expression littérale du champ total $\vec E(O)$ s'écrit :
    A) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^3} + \dfrac{\overrightarrow{BO}}{BO^3} + \dfrac{\overrightarrow{CO}}{CO^3}\right]$ ;
    B) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^2} - \dfrac{\overrightarrow{BO}}{BO^2} + \dfrac{\overrightarrow{CO}}{CO^2}\right]$ ;
    C) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^2} + \dfrac{\overrightarrow{BO}}{BO^2} - \dfrac{\overrightarrow{CO}}{CO^2}\right]$ ;
    D) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^3} - \dfrac{\overrightarrow{BO}}{BO^3} - \dfrac{\overrightarrow{CO}}{CO^3}\right]$ ;
    E) aucune de ces réponses.
2. (Question 9, 1 point) Retrouver la distance $AO$ en fonction de $a$, à l'aide des propriétés du triangle équilatéral : A) $\dfrac{a}{2}$ ; B) $\dfrac{2a}{\sqrt 3}$ ; C) $\dfrac{a}{\sqrt 3}$ ; D) $\dfrac{a}{3}$ ; E) aucune de ces réponses.
3. (Question 10, 2 points) En déduire que le champ total $\vec E(O)$ vaut : A) $-\dfrac{3q}{2\pi\varepsilon_0 a^3}\vec u_y$ ; B) $-\dfrac{q}{\pi\varepsilon_0 a^2}\vec u_y$ ; C) $\dfrac{3q}{2\pi\varepsilon_0 a^2}\vec u_y$ ; D) $-\dfrac{3q}{2\pi\varepsilon_0 a^2}\vec u_y$ ; E) $\dfrac{q}{\pi\varepsilon_0 a^2}\vec u_y$ ; F) aucune de ces réponses.
4. (Question 11 ♣, 3 points) Détailler les calculs permettant d'obtenir $\vec E(O)$.

**Correction.**

1. **D.** Chaque charge $q_i$ en $P_i$ crée en $O$ le champ $\dfrac{q_i}{4\pi\varepsilon_0}\dfrac{\overrightarrow{P_iO}}{P_iO^3}$ ; avec $q_A = +q$ et $q_B = q_C = -q$, on obtient la réponse D.
2. **C.** Voir la question 11 : $AO = \dfrac{a}{\sqrt 3}$.
3. **D.** Voir la question 11 : $\vec E(O) = -\dfrac{3q}{2\pi\varepsilon_0 a^2}\vec u_y$.
4. *Distances.* Le triangle étant équilatéral, $O$ est à la fois centre de gravité et centre du cercle circonscrit : $AO = BO = CO$. Soit $H$ le milieu de $[BC]$ ; la hauteur $AH$ vérifie (Pythagore dans $ABH$) $AH^2 + \left(\frac a2\right)^2 = a^2$, donc $AH = \dfrac{\sqrt 3}{2}a$. Le centre de gravité est aux deux tiers de la médiane :
$$AO = \frac23 AH = \frac23 \cdot \frac{\sqrt3}{2}a = \frac{a}{\sqrt 3}$$

    *Champ.* Avec la réponse de la question 8 et $-\overrightarrow{BO} = \overrightarrow{OB}$ :
$$\vec E(O) = \frac{q}{4\pi\varepsilon_0 AO^3}\left[\overrightarrow{AO} + \overrightarrow{OB} + \overrightarrow{OC}\right]$$
    Or $\overrightarrow{OB} + \overrightarrow{OC} = 2\overrightarrow{OH}$, et $OH = \frac13 AH = \frac12 AO$ avec $H$ dans le prolongement de $[AO]$ : $2\overrightarrow{OH} = \overrightarrow{AO}$. Donc
$$\vec E(O) = \frac{q}{4\pi\varepsilon_0}\left(\frac{\sqrt 3}{a}\right)^3 \cdot 2\overrightarrow{AO}, \qquad 2\overrightarrow{AO} = -\frac{2a}{\sqrt 3}\vec u_y$$
    d'où
$$\vec E(O) = -\frac{q}{4\pi\varepsilon_0}\cdot\frac{3\sqrt 3}{a^3}\cdot\frac{2a}{\sqrt 3}\,\vec u_y = -\frac{3q}{2\pi\varepsilon_0 a^2}\,\vec u_y$$

    *Vérification physique.* La charge $+q$ en $A$ repousse vers le bas, avec une norme $\frac{q}{4\pi\varepsilon_0 AO^2} = \frac{3q}{4\pi\varepsilon_0 a^2}$. Les charges $-q$ attirent vers $B$ et vers $C$ ; leurs composantes horizontales se compensent (le plan vertical passant par $A$ et $H$ est un plan de symétrie, $\vec E(O)$ y est contenu), et chacune a une composante verticale $\frac{3q}{4\pi\varepsilon_0 a^2}\sin 30° $ vers le bas. Total : $\frac{3q}{4\pi\varepsilon_0 a^2}(1 + 2 \times \frac12) = \frac{3q}{2\pi\varepsilon_0 a^2}$, dirigé vers $-\vec u_y$. Le résultat est bien homogène à un champ ($\mathrm{C}/(\mathrm{F\,m^{-1}} \cdot \mathrm{m^2}) = \mathrm{V\,m^{-1}}$).

## Exercice 2 : Sphère chargée uniformément en surface

**Énoncé.** (6 points) On considère une sphère de centre $O$ et de rayon $R$, portant une distribution surfacique de charges de densité $\sigma$ uniforme.

1. (Question 12, 1 point) Le champ $\vec E$ créé par cette distribution est :
    A) continu en tout point de l'espace ;
    B) continu en tout point de l'espace sauf à la traversée de la surface chargée ;
    C) continu en tout point de l'espace sauf sur les charges ;
    D) aucune de ces réponses.
2. (Question 13, 1 point) La direction de $\vec E$ au point $M$ est radiale car :
    A) tous les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_\theta, \vec u_\varphi)$ sont des plans de symétrie ;
    B) tous les plans passant par $O$ et par $M$ sont des plans de symétrie ;
    C) tous les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_\theta, \vec u_z)$ sont des plans de symétrie ;
    D) aucune de ces réponses.
3. (Question 14, 1 point) Par le théorème de Gauss, pour $r < R$, le champ vaut : A) $\dfrac{\sigma R^2}{\varepsilon_0 r^2}\vec u_r$ ; B) $\dfrac{\sigma}{\varepsilon_0}\vec u_r$ ; C) $\vec 0$ ; D) aucune de ces réponses.
4. (Question 15, 1 point) Même question pour $r > R$, avec les mêmes propositions.
5. (Question 16 ♣, 2 points) Donner l'expression de $\vec E$ pour $r < R$ et pour $r > R$, en détaillant.

**Correction.**

1. **B.** Une distribution surfacique crée un champ défini et continu partout sauf à la traversée de la surface chargée, où sa composante normale saute de $\sigma/\varepsilon_0$.
2. **B.** Tout plan contenant $O$ et $M$ contient la droite $(OM)$ et est un plan de symétrie de la sphère uniformément chargée ; $\vec E(M)$ est contenu dans tous ces plans, donc dans leur intersection, la droite $(OM)$ : $\vec E = E\,\vec u_r$. (Les plans $(M, \vec u_\theta, \vec u_\varphi)$ de la réponse A ne passent pas par $O$ et ne sont pas des plans de symétrie.)
3. **C.** $\vec E = \vec 0$ (voir la question 16).
4. **A.** $\vec E = \dfrac{\sigma R^2}{\varepsilon_0 r^2}\vec u_r$ (voir la question 16).
5. *Définition et continuité.* Distribution surfacique : $\vec E$ est défini et continu partout sauf en $r = R$.

    *Coordonnées et invariances.* En coordonnées sphériques $(O, \vec u_r, \vec u_\theta, \vec u_\varphi)$, a priori $\vec E(r, \theta, \varphi)$ ; la distribution est invariante par toute rotation autour de $O$ (en $\theta$ et en $\varphi$), donc les composantes ne dépendent que de $r$.

    *Symétries.* Les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_r, \vec u_\varphi)$ passent par $O$ et sont des plans de symétrie : $\vec E = E(r)\,\vec u_r$, radial.

    *Théorème de Gauss.* Surface de Gauss : sphère $S_G$ de centre $O$ et de rayon $r$. Sur $S_G$, $d\vec S = r^2 \sin\theta\, d\theta\, d\varphi\, \vec u_r$ et $E(r)$ est constant :
$$\Phi = \oiint_{S_G} E(r)\, dS = E(r)\, r^2 \int_0^\pi \sin\theta\, d\theta \int_0^{2\pi} d\varphi = 4\pi r^2 E(r)$$
    Charge intérieure : si $r < R$, $q_{\text{int}} = 0$ ; si $r > R$, $q_{\text{int}} = Q = 4\pi R^2 \sigma$. Avec $\Phi = q_{\text{int}}/\varepsilon_0$ :
$$\vec E(r < R) = \vec 0, \qquad \vec E(r > R) = \frac{4\pi R^2 \sigma}{4\pi\varepsilon_0 r^2}\vec u_r = \frac{\sigma}{\varepsilon_0}\frac{R^2}{r^2}\vec u_r$$
    À l'extérieur, c'est le champ d'une charge ponctuelle $Q$ placée en $O$. Vérification : le saut en $r = R$ vaut $\frac{\sigma}{\varepsilon_0} - 0 = \frac{\sigma}{\varepsilon_0}$, comme attendu.

> **Note :** la rédaction manuscrite est accompagnée d'un schéma : la sphère chargée de rayon $R$ et deux sphères de Gauss, l'une intérieure (a, $q_{\text{int}} = 0$), l'autre extérieure (b).

## Exercice 3 : Plan infini uniformément chargé

**Énoncé.** (6 points) On considère un plan infini $z = 0$, uniformément chargé en surface avec la densité $\sigma$, qui sépare l'espace en deux demi-espaces $z < 0$ et $z > 0$.

1. (Question 17 ♣, 1 point) Donner les invariances du champ $\vec E$, en détaillant.
2. (Question 18 ♣, 2 points) Donner les symétries du champ $\vec E$, en détaillant.
3. (Question 19, 1 point) On choisit comme surface de Gauss fermée un cylindre d'axe $Oz$ et de rayon $r$. Le flux $\Phi(\vec E)$ vaut : A) $\dfrac{2\sigma\pi r^2}{\varepsilon_0}$ ; B) $\dfrac{\sigma}{\varepsilon_0}$ ; C) $\dfrac{\sigma\pi r^2}{\varepsilon_0}$ ; D) $\dfrac{\sigma\pi r^2}{2\varepsilon_0}$ ; E) aucune de ces réponses.
4. (Question 20 ♣, 2 points) Donner l'expression du champ $\vec E$, en détaillant.

**Correction.**

1. En coordonnées cylindriques $(O, \vec u_r, \vec u_\theta, \vec u_z)$, a priori $\vec E(r, \theta, z)$. Le plan infini uniformément chargé est invariant par rotation autour de $Oz$ et par toute translation parallèle au plan (selon $\vec u_x$ et $\vec u_y$, donc en particulier selon $\vec u_r$) : le champ ne dépend que de $z$, $\vec E(z)$.
2. Pour un point $M$ quelconque, les plans $P_1 = (M, \vec u_r, \vec u_z)$ et $P_2 = (M, \vec u_\theta, \vec u_z)$ sont perpendiculaires au plan chargé et sont des plans de symétrie : $\vec E$ appartient à leur intersection, la droite parallèle à $Oz$ passant par $M$. Donc $\vec E = E(z)\,\vec u_z$.

    De plus, le plan chargé $z = 0$ est lui-même un plan de symétrie : le champ en $M'$, symétrique de $M$, est le symétrique de $\vec E(M)$, ce qui donne $E(-z) = -E(z)$ (le champ s'éloigne du plan de part et d'autre si $\sigma > 0$).

    > **Note :** la figure manuscrite montre le plan chargé, un point $M$ au-dessus, les plans $P_1$ et $P_2$ passant par $M$ et le champ $\vec E = E(z)\,\vec u_z$. Le barème accordait 1 point pour la parité, en question 18 ou 20.
3. **C.** Le cylindre de rayon $r$ découpe sur le plan un disque d'aire $\pi r^2$ : $q_{\text{int}} = \sigma\pi r^2$ et $\Phi = \dfrac{\sigma\pi r^2}{\varepsilon_0}$.
4. *Surface de Gauss.* Cylindre $S_G$ d'axe $Oz$, de rayon $r$, de hauteur $2z$ (bases $S_1$ en $z$ et $S_2$ en $-z$, surface latérale $S_3$), symétrique par rapport au plan.

    *Flux.* Sur $S_3$, $d\vec S$ est porté par $\vec u_r$, orthogonal à $\vec E$ : flux nul. Sur $S_1$ (normale $+\vec u_z$), le flux vaut $E(z)\pi r^2$ ; sur $S_2$ (normale $-\vec u_z$), il vaut $-E(-z)\pi r^2 = E(z)\pi r^2$ par parité. D'où, pour $z > 0$ :
$$\Phi = 2\pi r^2 E(z)$$

    *Charge intérieure.* $q_{\text{int}} = \iint \sigma\, dS = \sigma\pi r^2$ ($\sigma$ constant).

    *Conclusion.* $2\pi r^2 E(z) = \dfrac{\sigma\pi r^2}{\varepsilon_0}$, donc
$$\vec E = \begin{cases} \dfrac{\sigma}{2\varepsilon_0}\vec u_z & \text{si } z > 0 \\[2mm] -\dfrac{\sigma}{2\varepsilon_0}\vec u_z & \text{si } z < 0 \end{cases}$$
    Le champ est uniforme dans chaque demi-espace et saute de $\sigma/\varepsilon_0$ à la traversée du plan.

> **Note :** la figure de la question 20 montre le plan $\Pi$ chargé ($\sigma > 0$), le cylindre de Gauss de hauteur $h$ et de rayon $r$ centré en $O$, avec ses bases $S_1$ (normale $\vec n_1 = +\vec u_z$) et $S_2$ (normale $\vec n_2 = -\vec u_z$) et sa surface latérale $S_3$ (normale $\vec u_r$).
