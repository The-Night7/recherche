---
source: CC2-2021-2022-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 8
transcription: manuelle
---

# CC2 d'Électromagnétisme — 2 décembre 2021 (corrigé)

> **Note :** contrôle de 1 h 30, sans document ni calculatrice. Une seule bonne réponse par question à choix multiples. Les questions 13, 14, 20 et 21 sont à rédiger. Les réponses sont celles des cases noircies et des rédactions manuscrites de l'enseignant, vérifiées et détaillées.

## Questions de cours : circulation, potentiel, théorème de Gauss

**Énoncé.** (3 points, 0,5 point par question)

1. (Q.1) La circulation $C$ du champ électrostatique $\vec E$ est donnée par : a) $C = \iint_S \vec E \cdot d\vec S$ ; b) $C = \iiint_V \vec E \cdot d\vec V$ ; c) $C = \int_A^B \vec E \cdot d\vec l$ ; d) aucune de ces réponses.
2. (Q.2) Puisque $\vec E$ est à circulation conservative, on définit le potentiel électrostatique par : a) $\vec E = -\overrightarrow{\operatorname{grad}}\, V$ ; b) $\vec E = \overrightarrow{\operatorname{grad}}\, V$ ; c) $\vec V = \overrightarrow{\operatorname{grad}}\, E$ ; d) aucune de ces réponses.
3. (Q.3) Le théorème de Gauss relie le flux $\Phi$ de $\vec E$ à travers une surface fermée $S$ à la charge intérieure $q_{\text{int}}$ : a) $\Phi = \oiint_S \vec E \cdot d\vec S = q_{\text{int}}$ ; b) $\Phi = \iiint_V \vec E \cdot d\vec V = \dfrac{q_{\text{int}}}{\varepsilon_0}$ ; c) $\Phi = \oiint_S \vec E \cdot d\vec S = \dfrac{q_{\text{int}}}{\varepsilon_0}$ ; d) aucune de ces réponses.
4. (Q.4) La variation d'un champ scalaire $V(M)$ est $dV(M) = \overrightarrow{\operatorname{grad}}\, V \cdot d\overrightarrow{OM}$. Le vecteur $\overrightarrow{\operatorname{grad}}\, V$ est donc :
    a) tangent à la surface équipotentielle passant par $M$ ;
    b) un vecteur directeur de la surface équipotentielle passant par $M$ ;
    c) normal à la surface équipotentielle passant par $M$ ;
    d) aucune de ces réponses.
5. (Q.5) Dans le cas d'une distribution volumique de charges, le potentiel électrique est :
    a) défini sur la surface chargée et non continu à la traversée de la surface ;
    b) non défini aux points où se trouvent les charges ;
    c) défini et continu en tout point de l'espace ;
    d) aucune de ces réponses.
6. (Q.6) L'énergie potentielle d'interaction entre une charge $q$ et un champ $\vec E$ créant le potentiel $V$ est : a) $E_p = qV + K$ ; b) $E_p = qE + K$ ; c) $E_p = -qV + K$ ; d) aucune de ces réponses.

**Correction.**

1. **c).** La circulation se calcule le long d'une courbe : $C = \int_A^B \vec E \cdot d\vec l$.
2. **a).** $\vec E = -\overrightarrow{\operatorname{grad}}\, V$, ce qui équivaut à $C = \int_A^B \vec E \cdot d\vec l = V(A) - V(B)$.
3. **c).** $\oiint_S \vec E \cdot d\vec S = \dfrac{q_{\text{int}}}{\varepsilon_0}$.
4. **c).** Pour un déplacement $d\overrightarrow{OM}$ sur l'équipotentielle, $dV = 0$ : le gradient est orthogonal à tout vecteur tangent, il est **normal** à la surface équipotentielle (et dirigé vers les $V$ croissants).
5. **c).** Pour une distribution volumique (densité finie), le potentiel est défini et continu partout ; il est même de classe $C^1$ (le champ est continu).
6. **a).** $E_p = qV + K$ ($K$ constante), de sorte que la force $\vec F = -\overrightarrow{\operatorname{grad}}\, E_p = q\vec E$.

## Exercice 1 : Cylindre chargé en volume

**Énoncé.** (9 points) Une distribution volumique uniforme de charges est répartie dans un cylindre plein de rayon $R$ et de longueur infinie. La densité $\rho$ est constante et positive.

1. (Q.7, 1 point) Dans la base cylindrique, le champ $\vec E$ créé par cette distribution est : a) dirigé selon $(Oz)$ ; b) de direction quelconque ; c) radial ; d) contenu dans les plans d'antisymétrie ; e) aucune de ces réponses.
2. (Q.8, 1 point) Par le théorème de Gauss, l'expression de $E(r)$ à la distance $r$ de l'axe, pour $M$ **à l'extérieur** du cylindre, est : a) $\dfrac{\rho R^2}{2\varepsilon_0 r}$ ; b) $\dfrac{\rho r}{2\varepsilon_0}$ ; c) $\dfrac{\rho R^2}{4\varepsilon_0 r}$ ; d) $\dfrac{\rho R^2}{3\varepsilon_0 r}$ ; e) aucune de ces réponses.
3. (Q.9, 1 point) Même question pour $M$ **à l'intérieur** du cylindre : a) $\dfrac{\rho R^2}{2\varepsilon_0 r}$ ; b) $\dfrac{\rho r^2}{2\varepsilon_0}$ ; c) $\dfrac{\rho r}{2\varepsilon_0}$ ; d) $\dfrac{\rho r}{\varepsilon_0}$ ; e) aucune de ces réponses.
4. (Q.10, 1 point) Le potentiel en tout point $M$ **à l'intérieur** du cylindre a pour expression : a) $V(r) = -\dfrac{\rho R^2}{2\varepsilon_0}\ln r + \text{cste}$ ; b) $V(r) = \dfrac{\rho r^2}{4\varepsilon_0} + \text{cste}$ ; c) $V(r) = -\dfrac{\rho r^2}{4\varepsilon_0} + \text{cste}$ ; d) $V(r) = \dfrac{\rho r^2}{\varepsilon_0} + \text{cste}$ ; e) aucune de ces réponses.
5. (Q.11, 1 point) Le potentiel en tout point $M$ **à l'extérieur** du cylindre a pour expression : a) $V(r) = -\dfrac{\rho R^2}{\varepsilon_0}\ln r + \text{cste}$ ; b) $V(r) = -\dfrac{\rho R^2}{2\varepsilon_0}\ln r + \text{cste}$ ; c) $V(r) = \dfrac{\rho R^2}{\varepsilon_0 r} + \text{cste}$ ; d) $V(r) = -\dfrac{\rho r^2}{4\varepsilon_0} + \text{cste}$ ; e) aucune de ces réponses.
6. (Q.12, 1 point) Si l'on fixe $V(r = R) = 0$, la constante du potentiel à l'intérieur du cylindre vaut : a) $-\dfrac{\rho R^2}{4\varepsilon_0}$ ; b) $-\dfrac{\rho R^2}{\varepsilon_0}$ ; c) $\dfrac{\rho R^2}{4\varepsilon_0}$ ; d) $\dfrac{\rho R^2}{2\varepsilon_0}\ln R$ ; e) aucune de ces réponses.
7. (Q.13, 2 points) Retrouver l'expression de $\vec E$ par application du théorème de Gauss, à l'intérieur et à l'extérieur du cylindre.
8. (Q.14, 1 point) Tracer la courbe des variations de $E$ en fonction de la position de $M$, pour $r$ variant de $0$ à l'infini (et en $R$).

**Correction.**

1. **c).** Voir la question 13 : $\vec E = E(r)\,\vec u_r$.
2. **a).** $E(r) = \dfrac{\rho R^2}{2\varepsilon_0 r}$ pour $r \ge R$.
3. **c).** $E(r) = \dfrac{\rho r}{2\varepsilon_0}$ pour $r \le R$.
4. **c).** $E = -\dfrac{dV}{dr}$, donc $V(r) = -\displaystyle\int \frac{\rho r}{2\varepsilon_0}\, dr = -\frac{\rho r^2}{4\varepsilon_0} + \text{cste}$.
5. **b).** $V(r) = -\displaystyle\int \frac{\rho R^2}{2\varepsilon_0 r}\, dr = -\frac{\rho R^2}{2\varepsilon_0}\ln r + \text{cste}$. Pour que l'argument du logarithme soit sans dimension, on écrit plutôt $-\frac{\rho R^2}{2\varepsilon_0}\ln\frac{r}{r_0}$ ; on ne peut pas prendre le potentiel nul à l'infini, car la distribution s'étend elle-même à l'infini.
6. **c).** $V(R) = -\dfrac{\rho R^2}{4\varepsilon_0} + \text{cste} = 0$, donc $\text{cste} = \dfrac{\rho R^2}{4\varepsilon_0}$ et $V(r) = \dfrac{\rho}{4\varepsilon_0}(R^2 - r^2)$ à l'intérieur.
7. *Définition et continuité.* Distribution volumique : $\vec E$ est défini et continu partout.

    *Coordonnées.* Cylindriques $(O, \vec u_r, \vec u_\theta, \vec u_z)$, avec $d\vec l = dr\,\vec u_r + r\,d\theta\,\vec u_\theta + dz\,\vec u_z$ ; a priori $\vec E(r, \theta, z)$.

    *Invariances.* La distribution est inchangée par rotation d'angle $\theta$ autour de $Oz$ et, le cylindre étant infini, par translation selon $Oz$ : $\vec E$ ne dépend que de $r$.

    *Symétries.* Tout plan $P_1 = (M, \vec u_r, \vec u_\theta)$ (perpendiculaire à l'axe) et tout plan $P_2 = (M, \vec u_r, \vec u_z)$ (contenant l'axe) sont des plans de symétrie. $\vec E$ est dans leur intersection : $\vec E = E(r)\,\vec u_r$.

    *Théorème de Gauss.* Surface de Gauss $\Sigma$ : cylindre fermé coaxial de rayon $r$ et de hauteur $h$. Le flux à travers les bases est nul ($\vec E \perp \vec u_z$) ; à travers la surface latérale, il vaut $2\pi r h\, E(r)$. Donc $E(r) = \dfrac{q_{\text{int}}}{2\pi r h\,\varepsilon_0}$.

    - $r \ge R$ : $q_{\text{int}} = \rho\pi R^2 h$ (toute la charge sur la hauteur $h$), d'où $\vec E = \dfrac{\rho R^2}{2\varepsilon_0 r}\vec u_r$.
    - $r \le R$ : $q_{\text{int}} = \rho\pi r^2 h$, d'où $\vec E = \dfrac{\rho r}{2\varepsilon_0}\vec u_r$.
8. $E$ croît **linéairement** de $0$ (en $r = 0$) à $\dfrac{\rho R}{2\varepsilon_0}$ (en $r = R$), puis décroît en $\dfrac{1}{r}$ vers $0$ quand $r \to \infty$. La courbe est continue en $R$ (distribution volumique), avec un point anguleux (maximum) en $r = R$.

> **Note :** la rédaction manuscrite de la question 13 est illustrée par le cylindre chargé de rayon $R$ et le cylindre de Gauss de rayon $r$ et de hauteur $h$ (bases $S_1$, $S_2$ et surface latérale) ; la question 14 par la courbe décrite ci-dessus, avec la valeur $\frac{\rho R}{2\varepsilon_0}$ marquée sur l'axe vertical.

## Exercice 2 : Potentiel d'une sphère chargée en volume

**Énoncé.** (8 points) On considère une sphère de centre $O$ et de rayon $R$, portant une distribution volumique de charges de densité $\rho$ uniforme.

1. (Q.15, 1 point) Le champ $\vec E$ créé par cette distribution est : a) défini partout sauf à la traversée de la surface de la sphère ; b) défini en tout point de l'espace ; c) défini partout sauf aux points de la distribution ; d) aucune de ces réponses.
2. (Q.16, 1 point) La direction de $\vec E$ est radiale car :
    a) tous les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_\theta, \vec u_\varphi)$ sont des plans de symétrie ;
    b) tous les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_\theta, \vec u_z)$ sont des plans de symétrie ;
    c) tous les plans passant par $O$ et par $M$ sont des plans de symétrie ;
    d) aucune de ces réponses.
3. (Q.17, 1 point) Par le théorème de Gauss : a) $r < R$ : $\vec E = \dfrac{\rho r}{3\varepsilon_0}\vec u_r$ ; b) $r < R$ : $\vec E = \dfrac{\rho r}{\varepsilon_0}\vec u_r$ ; c) $r < R$ : $\vec E = -\dfrac{\rho r}{3\varepsilon_0}\vec u_r$ ; d) aucune de ces réponses.
4. (Q.18, 1 point) Par le théorème de Gauss : a) $r > R$ : $\vec E = -\dfrac{\rho R^3}{3\varepsilon_0 r^2}\vec u_r$ ; b) $r > R$ : $\vec E = \dfrac{\rho R^3}{\varepsilon_0 r^2}\vec u_r$ ; c) $r > R$ : $\vec E = \dfrac{\rho R^3}{3\varepsilon_0 r^2}\vec u_r$ ; d) aucune de ces réponses.
5. (Q.19, 1 point) Le potentiel $V$ créé par cette distribution : a) est défini et continu partout sauf à la traversée de la surface de la sphère ; b) est défini et continu en tout point de l'espace ; c) n'est pas défini aux points où se trouvent les charges ; d) aucune de ces réponses.
6. (Q.20, 2 points) À partir de l'expression de $\vec E$, donner l'expression du potentiel $V$ (nul à l'infini) pour $r < R$ et pour $r > R$.
7. (Q.21, 1 point) Tracer la courbe des variations de $V$ en fonction de la position de $M$, pour $r$ variant de $0$ à l'infini (et en $R$).

**Correction.**

1. **b).** Distribution volumique : $\vec E$ est défini (et continu) partout.
2. **c).** Tout plan contenant $O$ et $M$ est un plan de symétrie de la boule uniformément chargée ; $\vec E(M)$ est dans leur intersection, la droite $(OM)$.
3. **a).** Sphère de Gauss de rayon $r < R$ : $4\pi r^2 E(r) = \dfrac{\rho\,\frac43\pi r^3}{\varepsilon_0}$, donc $E(r) = \dfrac{\rho r}{3\varepsilon_0}$ (positif, dirigé vers l'extérieur pour $\rho > 0$).
4. **c).** Pour $r > R$ : $q_{\text{int}} = Q = \rho\,\frac43\pi R^3$, donc $E(r) = \dfrac{Q}{4\pi\varepsilon_0 r^2} = \dfrac{\rho R^3}{3\varepsilon_0 r^2}$.
5. **b).** Pour une distribution volumique, $V$ est défini et continu partout.
6. On intègre $E = -\dfrac{dV}{dr}$ dans chaque région :
$$V(r \ge R) = \frac{\rho R^3}{3\varepsilon_0 r} + K', \qquad V(r \le R) = -\frac{\rho r^2}{6\varepsilon_0} + K''$$
    - Potentiel nul à l'infini (la distribution est bornée) : $K' = 0$.
    - Continuité en $r = R$ : $\dfrac{\rho R^2}{3\varepsilon_0} = -\dfrac{\rho R^2}{6\varepsilon_0} + K''$, donc $K'' = \dfrac{\rho R^2}{\varepsilon_0}\left(\dfrac13 + \dfrac16\right) = \dfrac{\rho R^2}{2\varepsilon_0}$.

    Finalement :
$$V(r \ge R) = \frac{\rho R^3}{3\varepsilon_0 r}, \qquad V(r \le R) = \frac{\rho}{6\varepsilon_0}\left(3R^2 - r^2\right)$$
    Vérification : à l'extérieur, $V = \dfrac{Q}{4\pi\varepsilon_0 r}$ avec $Q = \frac43\pi R^3\rho$, le potentiel d'une charge ponctuelle.
7. $V$ vaut $\dfrac{\rho R^2}{2\varepsilon_0}$ en $r = 0$ (maximum, tangente horizontale), décroît comme une parabole jusqu'à $\dfrac{\rho R^2}{3\varepsilon_0}$ en $r = R$, puis décroît en $\dfrac1r$ vers $0$ à l'infini. La courbe est continue et sans point anguleux en $R$, car le champ $E = -\frac{dV}{dr}$ y est continu.

> **Note :** la correction de la question 20 rappelle dans un encadré les résultats de Gauss ($E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}$ avec $Q = \rho V$ pour $r \ge R$, $E(r) = \frac{\rho r}{3\varepsilon_0}$ pour $r \le R$) ; celle de la question 21 est la courbe décrite ci-dessus, avec les valeurs $\frac{\rho R^2}{2\varepsilon_0}$ et $\frac{\rho R^2}{3\varepsilon_0}$ marquées sur l'axe vertical.
