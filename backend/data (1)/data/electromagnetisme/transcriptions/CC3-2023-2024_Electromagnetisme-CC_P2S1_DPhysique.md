---
source: CC3-2023-2024_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 8 (énoncés ; la feuille-réponse et les cadres de rédaction des pages 9 à 16 ne sont pas reproduits)
transcription: manuelle
---

# CC3 d'Électromagnétisme — 18 janvier 2024

> **Note :** contrôle sans document ni calculatrice, 20 questions. Une seule bonne réponse par question à choix multiples, pas de point négatif. Les questions 13, 15, 17 et 20 sont à rédiger. Les corrections se trouvent dans la transcription du corrigé.

**Donnée.** Rotationnel d'un champ $\vec U$ en coordonnées cylindriques $(\vec u_r, \vec u_\theta, \vec u_z)$ :
$$\begin{aligned}\overrightarrow{\operatorname{rot}}\,\vec U = {} & \left(\frac1r\frac{\partial U_z}{\partial\theta} - \frac{\partial U_\theta}{\partial z}\right)\vec u_r + \left(\frac{\partial U_r}{\partial z} - \frac{\partial U_z}{\partial r}\right)\vec u_\theta \\ & + \frac1r\left(\frac{\partial(rU_\theta)}{\partial r} - \frac{\partial U_r}{\partial\theta}\right)\vec u_z\end{aligned}$$

## Questions de cours : symétries, Ampère, Biot et Savart, Maxwell

**Énoncé.** (5 points)

1. (0,5 point) En étudiant les plans de symétrie de la distribution de courant, on trouve que la direction de $\vec B$ en $M$ est :
    A) incluse dans tout plan $\Pi$ de symétrie passant par $M$ ;
    B) celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    C) celle de la droite intersection d'au moins deux plans de symétrie passant par $M$ ;
    D) aucune des réponses précédentes.
2. (0,5 point) Le théorème d'Ampère relie le champ $\vec B$ et les intensités $I_i$ (comptées algébriquement) qui traversent toute surface ouverte $S$ s'appuyant sur un contour $\Gamma$. Il s'énonce : A) $\oiint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; B) $\oint_\Gamma \vec B \wedge d\vec l = \mu_0\sum_i I_i$ ; C) $\oiint_\Gamma \vec B \cdot d\vec S = \mu_0\sum_i I_i$ ; D) $\oint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; E) aucune des réponses précédentes.
3. (1 point) La loi de Biot et Savart donne le champ $\vec B$ en $M$ créé par un fil parcouru par un courant $I$ : A) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{MP}}{MP^2}$ ; B) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ ; C) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^2}$ ; D) aucune des réponses précédentes.
4. (0,5 point) En étudiant les plans d'antisymétrie de la distribution de courant, on trouve que $\vec B$ en $M$ :
    A) a la direction de la droite orthogonale à un plan $\Pi'$ d'antisymétrie passant par $M$ ;
    B) est inclus dans tout plan $\Pi'$ d'antisymétrie passant par $M$ ;
    C) a la direction de la droite intersection d'un plan de symétrie et d'un plan d'antisymétrie passant par $M$ ;
    D) aucune des réponses précédentes.
5. (0,5 point) La vitesse $c$ de la lumière dans le vide s'exprime en fonction de $\varepsilon_0$ et $\mu_0$ par : A) $c^2 = \dfrac{1}{\varepsilon_0\mu_0}$ ; B) $c = \varepsilon_0\mu_0$ ; C) $c = \dfrac{1}{\varepsilon_0\mu_0}$ ; D) $c^2 = \varepsilon_0\mu_0$ ; E) aucune des réponses précédentes.
6. (1 point) Soient la densité de courant $\vec j$ et la densité volumique de charge $\rho$. L'équation locale de conservation de la charge s'écrit : A) $\operatorname{div}\vec j - \dfrac{\partial\rho}{\partial t} = 0$ ; B) $\operatorname{div}\vec j - \varepsilon_0\dfrac{\partial\rho}{\partial t} = 0$ ; C) $\operatorname{div}\vec j + \dfrac{\partial\rho}{\partial t} = 0$ ; D) $\operatorname{div}\vec j + \varepsilon_0\dfrac{\partial\rho}{\partial t} = 0$ ; E) aucune des réponses précédentes.
7. (1 point) Les quatre équations de Maxwell sont :
    A) $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = \dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    B) $\operatorname{div}\vec E = \rho$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = \dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    C) $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = -\dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    D) aucune des réponses précédentes.

## Exercice 1 : Cylindre parcouru par un courant

**Énoncé.** (7 points) Un cylindre plein infiniment long, d'axe $(Oz)$ et de rayon $R$, est parcouru par un courant $I$ constant, réparti uniformément et dirigé selon sa longueur. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$ et on cherche le champ magnétique $\vec B(M)$.

1. (Question 8, 0,5 point) La densité de courant $\vec j$ s'écrit en fonction de $I$ : A) $\dfrac{I}{\pi R^2}\vec u_r$ ; B) $\dfrac{I}{\pi r^2}\vec u_z$ ; C) $\dfrac{I}{\pi R^2}\vec u_z$ ; D) $\dfrac{I}{\pi r^2}\vec u_z$ ; E) aucune des réponses précédentes.
2. (Question 9, 0,5 point) En regardant les invariances, $B(r, \theta, z)$ ne dépend que de : A) $\varphi$ ; B) $r$ ; C) $z$ ; D) $\theta$ ; E) aucune des réponses précédentes.
3. (Question 10, 1 point) Du fait des plans de symétrie, $\vec B(M)$ s'écrit : A) $B(z)\,\vec u_r$ et $\vec B(0) \ne \vec 0$ ; B) $B(r)\,\vec u_\theta$ et $\vec B(0) \ne \vec 0$ ; C) $B(z)\,\vec u_z$ et $\vec B(0) \ne \vec 0$ ; D) $B(\theta)\,\vec u_\theta$ et $\vec B(0) = \vec 0$ ; E) $B(r)\,\vec u_\theta$ et $\vec B(0) = \vec 0$ ; F) aucune des réponses précédentes.
4. (Question 11, 1 point) En utilisant une des équations de Maxwell, pour $r \le R$ : A) $\vec B = \dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_\theta$ ; B) $\dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; C) $\dfrac{\mu_0 I}{2\pi r}\vec u_z$ ; D) $\dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_z$ ; E) aucune des réponses précédentes.
5. (Question 12, 1 point) Pour $r \ge R$ : A) $\vec B = \dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; B) $\dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_z$ ; C) $\dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_\theta$ ; D) $\dfrac{\mu_0 I}{2\pi r}\vec u_z$ ; E) aucune des réponses précédentes.
6. (Question 13, 3 points) Par le théorème d'Ampère, démontrer l'expression de $\vec B(M)$ pour $r \ge R$, en détaillant les calculs (symétries, invariances, contour d'Ampère…).

> **Note :** l'énoncé de la question 8 parle de « densité de courant surfacique » ; il s'agit de la densité **volumique** de courant $\vec j$ (en $\mathrm{A\,m^{-2}}$), le courant étant réparti dans tout le volume du cylindre.

## Exercice 2 : Solénoïde infini parcouru par un courant

**Énoncé.** (4 points) Un solénoïde de rayon $a$, de longueur considérée comme infinie, comportant $n$ spires par unité de longueur, est parcouru par un courant d'intensité $I$ constante. Son axe coïncide avec l'axe $Oz$ du repère cylindrique $(O ; \vec u_r, \vec u_\theta, \vec u_z)$. On connaît le potentiel vecteur $\vec A$ en un point à la distance $r$ de l'axe :

- si $r < a$ : $\vec A(M) = \dfrac{\mu_0 n I}{2}r\,\vec u_\theta$ ;
- si $r > a$ : $\vec A(M) = \dfrac{\mu_0 n I}{2r}a^2\,\vec u_\theta$.

On cherche le champ magnétostatique $\vec B(M)$ en tout point.

1. (Question 14, 1 point) Pour $r < a$ : A) $\vec B = \vec 0$ ; B) $\vec B = \dfrac{\mu_0 n I}{r}\vec u_z$ ; C) $\vec B = \mu_0 n I r\,\vec u_z$ ; D) $\vec B = \mu_0 n I\,\vec u_z$ ; E) aucune des réponses précédentes.
2. (Question 15, 1 point) Démontrer l'expression de $\vec B(M)$ pour $r < a$ en détaillant les calculs (potentiel vecteur $\vec A$, puis calcul de $\vec B$).
3. (Question 16, 1 point) Pour $r > a$ : A) $\vec B = \vec 0$ ; B) $\vec B = \mu_0 n I\,\vec u_z$ ; C) $\vec B = \mu_0 n I r\,\vec u_z$ ; D) $\vec B = \dfrac{\mu_0 n I}{r}\vec u_z$ ; E) aucune des réponses précédentes.
4. (Question 17, 1 point) Démontrer l'expression de $\vec B(M)$ pour $r > a$ en détaillant les calculs.

## Exercice 3 : Spire circulaire

**Énoncé.** (6 points) Une spire de centre $O$ et de rayon $R$ est parcourue par un courant d'intensité $I$ constante. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$ et on cherche le champ magnétique $\vec B(M)$ en un point $M$ de l'axe de révolution de la spire.

> **Note :** la figure 1 montre la spire dans un plan perpendiculaire à l'axe $Oz$, un point $P$ de la spire avec l'élément $d\vec l$, le point $M$ de l'axe à la distance $z$ de $O$, l'angle $\alpha$ en $M$ entre l'axe et la droite $(MP)$, et la contribution $d\vec B$ en $M$.

1. (Question 18, 1 point) Du fait des invariances, $\vec B(M)$ ne dépend que de : A) $\theta$ ; B) $\varphi$ ; C) $r$ ; D) $z$ ; E) aucune des réponses précédentes.
2. (Question 19, 1 point) Du fait des symétries, $\vec B(M)$ : A) est radial ; B) est orthoradial ; C) a une composante radiale et une orthoradiale ; D) est selon $(Oz)$ ; E) aucune des réponses précédentes.
3. (Question 20, 4 points) Démontrer que le champ en un point $M$ de l'axe s'écrit $\vec B(M) = \dfrac{\mu_0 I}{2R}\sin^3\alpha\,\vec u_z$, en détaillant les calculs (symétries, invariances…).
