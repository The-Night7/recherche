---
source: Rattrapage-2023-2024-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 13 (grille de réponses page 9, rédactions manuscrites pages 10 à 13)
transcription: manuelle
---

# Rattrapage d'Électromagnétisme — 7 février 2024 (corrigé)

> **Note :** épreuve de 1 h 30, sans document ni calculatrice, 21 questions. Une seule bonne réponse par question à choix multiples, pas de point négatif. Les questions 4, 10, 13 et 21 sont à rédiger. Les réponses sont celles de la grille corrigée et des rédactions manuscrites de l'enseignant, vérifiées et détaillées.

## Exercice 1 : Champ créé par trois charges ponctuelles

**Énoncé.** (4 points) Trois charges ponctuelles $+q$ (en $A$), $-q$ (en $B$) et $-q$ (en $C$) sont placées aux sommets d'un triangle équilatéral de côté $a$. On cherche le champ électrostatique $\vec E(O)$ créé au centre $O$ du triangle par ces trois charges.

> **Note :** la figure montre $A$ ($+q$) en haut, $C$ ($-q$) en bas à gauche et $B$ ($-q$) en bas à droite ; l'axe $y$ est vertical, dirigé vers le haut (de $O$ vers $A$), l'axe $x$ horizontal.

1. (Question 1, 1 point) L'expression littérale du champ total $\vec E(O)$ s'écrit :
    A) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^2} - \dfrac{\overrightarrow{BO}}{BO^2} + \dfrac{\overrightarrow{CO}}{CO^2}\right]$ ;
    B) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^2} + \dfrac{\overrightarrow{BO}}{BO^2} - \dfrac{\overrightarrow{CO}}{CO^2}\right]$ ;
    C) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^3} - \dfrac{\overrightarrow{BO}}{BO^3} - \dfrac{\overrightarrow{CO}}{CO^3}\right]$ ;
    D) $\dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{\overrightarrow{AO}}{AO^3} + \dfrac{\overrightarrow{BO}}{BO^3} + \dfrac{\overrightarrow{CO}}{CO^3}\right]$ ;
    E) aucune des réponses précédentes.
2. (Question 2, 1 point) Retrouver la distance $AO$ en fonction de $a$, à l'aide des propriétés du triangle équilatéral : A) $\dfrac{a}{2}$ ; B) $\dfrac{a}{3}$ ; C) $\dfrac{2a}{\sqrt3}$ ; D) $\dfrac{a}{\sqrt3}$ ; E) aucune des réponses précédentes.
3. (Question 3, 0,5 point) En déduire que le champ total $\vec E(O)$ vaut : A) $-\dfrac{3q}{2\pi\varepsilon_0 a^3}\vec u_y$ ; B) $\dfrac{q}{\pi\varepsilon_0 a^2}\vec u_y$ ; C) $\dfrac{3q}{2\pi\varepsilon_0 a^2}\vec u_y$ ; D) $-\dfrac{3q}{2\pi\varepsilon_0 a^2}\vec u_y$ ; E) $-\dfrac{q}{\pi\varepsilon_0 a^2}\vec u_y$ ; F) aucune des réponses précédentes.
4. (Question 4, 1,5 point) Détailler les calculs donnant $\vec E(O)$.

**Correction.**

1. **C.** Chaque charge $q_i$ en $P_i$ crée en $O$ le champ $\dfrac{q_i}{4\pi\varepsilon_0}\dfrac{\overrightarrow{P_iO}}{P_iO^3}$, avec $q_A = +q$ et $q_B = q_C = -q$.
2. **D.** $AO = \dfrac{a}{\sqrt3}$ (question 4).
3. **D.** $\vec E(O) = -\dfrac{3q}{2\pi\varepsilon_0 a^2}\vec u_y$ (question 4).
4. *Distances.* Le triangle étant équilatéral, $AO = BO = CO$. Soit $H$ le milieu de $[BC]$ : $AH^2 + \left(\frac a2\right)^2 = a^2$, donc $AH = \frac{\sqrt3}{2}a$, et le centre est aux deux tiers de la médiane :
$$AO = \frac23 AH = \frac{a}{\sqrt3}$$

    *Champ.* Avec $-\overrightarrow{BO} = \overrightarrow{OB}$ et $-\overrightarrow{CO} = \overrightarrow{OC}$ :
$$\vec E(O) = \frac{q}{4\pi\varepsilon_0 AO^3}\left[\overrightarrow{AO} + \overrightarrow{OB} + \overrightarrow{OC}\right]$$
    Or $\overrightarrow{OB} + \overrightarrow{OC} = 2\overrightarrow{OH} = \overrightarrow{AO}$ (car $OH = \frac12 AO$, dans le prolongement de $[AO]$). Avec $2\overrightarrow{AO} = -\dfrac{2a}{\sqrt3}\vec u_y$ :
$$\vec E(O) = \frac{q}{4\pi\varepsilon_0}\cdot\frac{3\sqrt3}{a^3}\cdot\left(-\frac{2a}{\sqrt3}\right)\vec u_y = -\frac{3q}{2\pi\varepsilon_0 a^2}\,\vec u_y$$
    *Vérification.* $+q$ repousse vers le bas avec la norme $\frac{3q}{4\pi\varepsilon_0 a^2}$ ; les deux $-q$ attirent vers $B$ et $C$ : leurs composantes horizontales se compensent et chacune apporte $\frac{3q}{4\pi\varepsilon_0 a^2}\sin 30°$ vers le bas. Total : $\frac{3q}{4\pi\varepsilon_0 a^2} \times 2 = \frac{3q}{2\pi\varepsilon_0 a^2}$, vers $-\vec u_y$.

## Exercice 2 : Sphère chargée uniformément en surface

**Énoncé.** (6 points) Pour rappel, la loi de Coulomb et le théorème de Gauss permettent de calculer un champ électrique à partir d'une distribution de charges.

1. (Question 5, 0,5 point) La loi de Coulomb donne la force $\vec F_{1/2}$ exercée par la charge ponctuelle $q_1$ sur la charge ponctuelle $q_2$, située à la distance $r_{12}$ : A) $\vec F_{2/1} = k\left(\dfrac{q_1q_2}{r_{12}^2}\right)\vec u_{1\to2}$ ; B) $\vec F_{1/2} = k\left(\dfrac{q_1q_2}{r_{12}^3}\right)\vec u_{1\to2}$ ; C) $\vec F_{1/2} = k\left(\dfrac{q_1q_2}{r_{12}^2}\right)\vec u_{1\to2}$ ; D) aucune des réponses précédentes.
2. (Question 6, 0,5 point) Le théorème de Gauss relie le flux $\Phi$ de $\vec E$ à travers une surface fermée $S$ à la charge intérieure $q_{\text{int}}$ : A) $\oiint_S \vec E \cdot d\vec S = q_{\text{int}}$ ; B) $\oiint_S \vec E \cdot d\vec S = \dfrac{q_{\text{int}}}{\varepsilon_0}$ ; C) $\iiint_V \vec E \cdot d\vec V = \dfrac{q_{\text{int}}}{\varepsilon_0}$ ; D) aucune des réponses précédentes.
3. (Question 7, 0,5 point) En étudiant les plans de symétrie d'une distribution de charges, on trouve que :
    A) le champ $\vec E$ en $M$ est contenu dans tout plan $\Pi$ de symétrie passant par $M$ ;
    B) la direction de $\vec E$ en $M$ est celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    C) la direction de $\vec E$ en $M$ est celle de la droite intersection d'au moins deux plans d'antisymétrie passant par $M$ ;
    D) aucune des réponses précédentes.

On considère maintenant une sphère de centre $O$ et de rayon $R$ portant une distribution surfacique de charges de densité $\sigma$ uniforme, et l'on cherche le champ $\vec E(M)$ qu'elle crée.

4. (Question 8, 0,5 point) Le champ $\vec E(M)$ créé par cette distribution est : A) continu partout sauf sur les charges ; B) continu partout sauf à la traversée de la surface chargée ; C) continu partout ; D) aucune des réponses précédentes.
5. (Question 9, 1 point) La direction de $\vec E$ en $M$ est radiale car :
    A) tous les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_\theta, \vec u_z)$ sont des plans de symétrie ;
    B) tous les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_\theta, \vec u_\varphi)$ sont des plans de symétrie ;
    C) tous les plans passant par $O$ et par $M$ sont des plans de symétrie ;
    D) aucune des réponses précédentes.
6. (Question 10, 3 points) Donner l'expression de $\vec E$ pour $r > R$ par le théorème de Gauss, en détaillant les calculs (symétries, invariances…).

**Correction.**

1. **C.**
2. **B.**
3. **A.**
4. **B.** Discontinuité de $\sigma/\varepsilon_0$ de la composante normale à la traversée de la surface.
5. **C.** Tout plan contenant $O$ et $M$ est un plan de symétrie ; $\vec E(M)$ est dans leur intersection, la droite $(OM)$.
6. *Définition et continuité.* Distribution surfacique : $\vec E$ est défini et continu partout sauf à la traversée de la sphère.

    *Coordonnées et invariances.* Sphériques $(O, \vec e_r, \vec e_\theta, \vec e_\varphi)$ ; a priori $\vec E(r, \theta, \varphi)$, mais la distribution est invariante par rotation en $\theta$ et en $\varphi$ : seule la dépendance en $r$ subsiste.

    *Symétries.* Tout plan passant par $M$ et $O$, par exemple $(M, \vec e_r, \vec e_\theta)$ et $(M, \vec e_r, \vec e_\varphi)$, est un plan de symétrie : $\vec E = E(r)\,\vec e_r$, radial.

    *Théorème de Gauss.* $S_G$ : sphère de centre $O$ et de rayon $r$ ; avec $dS = r^2\sin\theta\, d\theta\, d\varphi$ :
$$\Phi = \oiint_{S_G} E(r)\, dS = r^2 E(r)\int_0^\pi \sin\theta\, d\theta\int_0^{2\pi} d\varphi = 4\pi r^2 E(r)$$
    Pour $r > R$, $q_{\text{int}} = Q = 4\pi R^2\sigma$, donc $4\pi r^2 E(r) = \dfrac{4\pi R^2\sigma}{\varepsilon_0}$ et
$$\vec E(r > R) = \frac{\sigma}{\varepsilon_0}\,\frac{R^2}{r^2}\,\vec e_r$$
    (Pour $r < R$, $q_{\text{int}} = 0$ et $\vec E = \vec 0$.)

> **Note :** la rédaction manuscrite est illustrée par la sphère chargée de rayon $R$ et deux sphères de Gauss, l'une intérieure (a, $q_{\text{int}} = 0$), l'autre extérieure (b).

## Exercice 3 : Condensateur cylindrique

**Énoncé.** (6 points) Un condensateur cylindrique à air est formé de deux armatures coaxiales de rayons $R_1 < R_2$. Ces deux cylindres infinis sont uniformément chargés en surface, avec les charges $Q_1$ et $Q_2$ telles que $Q_1 = -Q_2 = Q_{\text{int}}$ ; $Q_{\text{int}}$ est la charge portée par la surface du cylindre intérieur de rayon $R_1$ sur la hauteur $h$. On suppose ce conducteur de longueur infinie ($h \gg R_2 > R_1$).

1. (Question 11, 1 point) Le champ $\vec E$ en un point $M$ à la distance $r$ de l'axe, avec $R_1 < r < R_2$, vaut : A) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 r}\vec u_r$ ; B) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 r^2}\vec u_r$ ; C) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 h r}\vec u_r$ ; D) aucune des réponses précédentes.
2. (Question 12, 2 points) La capacité $C$ vaut : A) $\dfrac{2\pi\varepsilon_0 h}{\ln(R_2/R_1)}$ ; B) $\dfrac{2\pi\varepsilon_0 h}{R_2/R_1}$ ; C) $\dfrac{2\pi\varepsilon_0 h}{\ln(R_1/R_2)}$ ; D) aucune des réponses précédentes.
3. (Question 13, 2 points) Donner l'expression de cette capacité $C$ en détaillant.
4. (Question 14, 1 point) Pour $R_2 - R_1 = e \ll R_1$, la capacité se simplifie en : A) $\dfrac{2\pi\varepsilon_0 e h}{R_1}$ ; B) $\dfrac{2\pi\varepsilon_0 R_1 e}{h}$ ; C) $\dfrac{2\pi\varepsilon_0 R_1 h}{e}$ ; D) aucune des réponses précédentes.

> **Note :** la figure représente les deux cylindres coaxiaux de rayons $R_1$ et $R_2$ et de hauteur $h$.

**Correction.**

1. **C.** Théorème de Gauss sur un cylindre coaxial de rayon $r$ et de hauteur $h$, avec $\vec E = E(r)\,\vec u_r$ (symétries et invariances du cylindre infini) : $2\pi r h E(r) = \dfrac{Q_{\text{int}}}{\varepsilon_0}$. Les réponses A et B ne sont pas homogènes à un champ.
2. **A.**
3. Entre les armatures, $\vec E(M) = E(r)\,\vec u_r = \dfrac{Q_1}{2\pi\varepsilon_0 h r}\vec u_r$ ($R_1 < r < R_2$). Avec $\vec E = -\overrightarrow{\operatorname{grad}}\, V$, $dV = -\vec E \cdot d\vec r = -E(r)\, dr = -\dfrac{Q_1}{2\pi\varepsilon_0 h}\dfrac{dr}{r}$. En intégrant de l'armature 2 à l'armature 1 :
$$V_1 - V_2 = -\frac{Q_1}{2\pi\varepsilon_0 h}\big[\ln r\big]_{R_2}^{R_1} = \frac{Q_1}{2\pi\varepsilon_0 h}\ln\frac{R_2}{R_1}$$
    Comme $Q_1 = C(V_1 - V_2)$ :
$$C = \frac{2\pi\varepsilon_0 h}{\ln(R_2/R_1)}$$
4. **C.** $\ln\left(1 + \frac{e}{R_1}\right) \approx \frac{e}{R_1}$, d'où $C \approx \dfrac{2\pi\varepsilon_0 R_1 h}{e} = \dfrac{\varepsilon_0 S}{e}$ avec $S = 2\pi R_1 h$ (condensateur plan).

## Exercice 4 : Fil infini parcouru par un courant

**Énoncé.** (6 points) Pour rappel, la loi de Biot et Savart et le théorème d'Ampère permettent de calculer un champ magnétique à partir d'une distribution de courant.

1. (Question 15, 0,5 point) La loi de Biot et Savart donne le champ $\vec B$ en $M$ créé par un fil parcouru par un courant $I$ : A) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ ; B) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^2}$ ; C) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{MP}}{MP^2}$ ; D) aucune des réponses précédentes.
2. (Question 16, 0,5 point) Le théorème d'Ampère relie $\vec B$ et les intensités $I_i$ (comptées algébriquement) traversant toute surface ouverte $S$ s'appuyant sur un contour $\Gamma$ : A) $\oint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; B) $\oiint_\Gamma \vec B \cdot d\vec S = \mu_0\sum_i I_i$ ; C) $\oint_\Gamma \vec B \wedge d\vec l = \mu_0\sum_i I_i$ ; D) $\oiint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; E) aucune des réponses précédentes.
3. (Question 17, 0,5 point) En étudiant les plans de symétrie d'une distribution de courant, la direction de $\vec B$ en $M$ est :
    A) incluse dans tout plan $\Pi$ de symétrie passant par $M$ ;
    B) celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    C) celle de la droite intersection d'au moins deux plans de symétrie passant par $M$ ;
    D) aucune des réponses précédentes.
4. (Question 18, 0,5 point) En étudiant les plans d'antisymétrie d'une distribution de courant, $\vec B$ en $M$ :
    A) a la direction de la droite orthogonale à un plan $\Pi'$ d'antisymétrie passant par $M$ ;
    B) a la direction de la droite intersection d'un plan de symétrie et d'un plan d'antisymétrie passant par $M$ ;
    C) est inclus dans tout plan $\Pi'$ d'antisymétrie passant par $M$ ;
    D) aucune des réponses précédentes.

On considère maintenant un fil de longueur infinie, confondu avec l'axe $(Oz)$, parcouru par un courant $I$ constant orienté vers les $z$ croissants. On repère $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$.

5. (Question 19, 1 point) Du fait des symétries et des invariances, $\vec B(M)$ s'écrit : A) $B(r)\,\vec u_\theta$ ; B) $B(z)\,\vec u_z$ ; C) $B(z)\,\vec u_r$ ; D) $B(\theta)\,\vec u_\theta$ ; E) aucune des réponses précédentes.
6. (Question 20, 1 point) Par le théorème d'Ampère : A) $\dfrac{\mu_0 I}{\pi z}\vec u_\theta$ ; B) $\dfrac{\mu_0 I}{\pi z}\vec u_r$ ; C) $\dfrac{2\mu_0 I}{\pi r}\vec u_z$ ; D) $\dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; E) aucune des réponses précédentes.
7. (Question 21, 2 points) Donner l'expression de $\vec B(M)$ par le théorème d'Ampère, en détaillant les calculs (symétries, invariances…).

**Correction.**

1. **A.**
2. **A.**
3. **B.**
4. **C.**
5. **A.**
6. **D.**
7. *Coordonnées.* Cylindriques $(O, \vec u_r, \vec u_\theta, \vec u_z)$, avec $d\vec l = dr\,\vec u_r + r\, d\theta\,\vec u_\theta + dz\,\vec u_z$ ; a priori $\vec B = B(r, \theta, z)\,\vec u$.

    *Invariances.* Fil infini : invariance par translation selon $\vec u_z$ ($B$ indépendant de $z$) et par rotation autour de $(Oz)$ ($B$ indépendant de $\theta$).

    *Symétries.* Le plan $\Pi = (M, \vec u_r, \vec u_z)$, qui contient le fil, est un plan de symétrie de la distribution de courant : $\vec B \perp \Pi$, donc $\vec B = B(r)\,\vec u_\theta$.

    *Théorème d'Ampère.* Contour $\mathcal C$ : cercle de rayon $r$ d'axe $(Oz)$, orienté selon $\vec u_\theta$, de sorte que $I_{\text{enlacé}} = +I$. Sur ce cercle, $B(r)$ est constant et $\vec B \cdot d\vec l = B(r)\, r\, d\theta$ :
$$\oint_{\mathcal C}\vec B \cdot d\vec l = B(r)\, r\int_0^{2\pi} d\theta = 2\pi r B(r) = \mu_0 I \quad\Longrightarrow\quad \vec B = \frac{\mu_0 I}{2\pi r}\,\vec u_\theta$$
