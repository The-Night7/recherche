---
source: CC3-2023-2024-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 14 (grille de réponses page 10, rédactions manuscrites pages 11 à 14)
transcription: manuelle
---

# CC3 d'Électromagnétisme — 18 janvier 2024 (corrigé)

> **Note :** contrôle sans document ni calculatrice, 20 questions. Une seule bonne réponse par question à choix multiples, pas de point négatif. Les questions 13, 15, 17 et 20 sont à rédiger. Les réponses sont celles de la grille corrigée et des rédactions manuscrites de l'enseignant, vérifiées et détaillées.

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

**Correction.**

1. **B.** $\vec B$, pseudo-vecteur, est orthogonal aux plans de symétrie des courants.
2. **D.** $\oint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ : une circulation sur un contour fermé (intégrale simple).
3. **B.** $d\vec B = \dfrac{\mu_0 I}{4\pi}\dfrac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$.
4. **B.** En un point d'un plan d'antisymétrie des courants, $\vec B$ est contenu dans ce plan.
5. **A.** $\varepsilon_0\mu_0 c^2 = 1$ ; numériquement, $\frac{1}{\sqrt{8{,}85 \times 10^{-12} \times 4\pi \times 10^{-7}}} \approx 3{,}0 \times 10^8\ \mathrm{m/s}$.
6. **C.** $\operatorname{div}\vec j + \dfrac{\partial\rho}{\partial t} = 0$.
7. **C.** Maxwell-Gauss, Maxwell-flux, Maxwell-Faraday (avec le signe moins) et Maxwell-Ampère.

## Exercice 1 : Cylindre parcouru par un courant

**Énoncé.** (7 points) Un cylindre plein infiniment long, d'axe $(Oz)$ et de rayon $R$, est parcouru par un courant $I$ constant, réparti uniformément et dirigé selon sa longueur. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$ et on cherche le champ magnétique $\vec B(M)$.

1. (Question 8, 0,5 point) La densité de courant $\vec j$ s'écrit en fonction de $I$ : A) $\dfrac{I}{\pi R^2}\vec u_r$ ; B) $\dfrac{I}{\pi r^2}\vec u_z$ ; C) $\dfrac{I}{\pi R^2}\vec u_z$ ; D) $\dfrac{I}{\pi r^2}\vec u_z$ ; E) aucune des réponses précédentes.
2. (Question 9, 0,5 point) En regardant les invariances, $B(r, \theta, z)$ ne dépend que de : A) $\varphi$ ; B) $r$ ; C) $z$ ; D) $\theta$ ; E) aucune des réponses précédentes.
3. (Question 10, 1 point) Du fait des plans de symétrie, $\vec B(M)$ s'écrit : A) $B(z)\,\vec u_r$ et $\vec B(0) \ne \vec 0$ ; B) $B(r)\,\vec u_\theta$ et $\vec B(0) \ne \vec 0$ ; C) $B(z)\,\vec u_z$ et $\vec B(0) \ne \vec 0$ ; D) $B(\theta)\,\vec u_\theta$ et $\vec B(0) = \vec 0$ ; E) $B(r)\,\vec u_\theta$ et $\vec B(0) = \vec 0$ ; F) aucune des réponses précédentes.
4. (Question 11, 1 point) En utilisant une des équations de Maxwell, pour $r \le R$ : A) $\vec B = \dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_\theta$ ; B) $\dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; C) $\dfrac{\mu_0 I}{2\pi r}\vec u_z$ ; D) $\dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_z$ ; E) aucune des réponses précédentes.
5. (Question 12, 1 point) Pour $r \ge R$ : A) $\vec B = \dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; B) $\dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_z$ ; C) $\dfrac{\mu_0 I}{2\pi R^2}r\,\vec u_\theta$ ; D) $\dfrac{\mu_0 I}{2\pi r}\vec u_z$ ; E) aucune des réponses précédentes.
6. (Question 13, 3 points) Par le théorème d'Ampère, démontrer l'expression de $\vec B(M)$ pour $r \ge R$, en détaillant les calculs (symétries, invariances, contour d'Ampère…).

> **Note :** l'énoncé de la question 8 parle de « densité de courant surfacique » ; il s'agit de la densité **volumique** de courant $\vec j$ (en $\mathrm{A\,m^{-2}}$), le courant étant réparti dans tout le volume du cylindre.

**Correction.**

1. **C.** Le courant est uniformément réparti sur la section $\pi R^2$ : $\vec j = \dfrac{I}{\pi R^2}\vec u_z$ (constante ; les réponses en $1/r^2$ ne sont pas uniformes).
2. **B.**
3. **E.** $\vec B = B(r)\,\vec u_\theta$ (question 13). Sur l'axe, tout plan contenant l'axe est plan de symétrie, donc $\vec B(0)$ serait orthogonal à tous ces plans à la fois : $\vec B(0) = \vec 0$ (ce que confirme la question 11).
4. **A.** Contour d'Ampère de rayon $r \le R$ : $I_{\text{enlacé}} = j\pi r^2 = I\dfrac{r^2}{R^2}$, donc $2\pi r B = \mu_0 I\dfrac{r^2}{R^2}$ et $\vec B = \dfrac{\mu_0 I r}{2\pi R^2}\vec u_\theta$.
5. **A.** Voir la question 13.
6. *Invariances.* Le cylindre étant infini, la distribution de courant est invariante par translation selon $(Oz)$ ($B$ indépendant de $z$) et par rotation autour de $(Oz)$ ($B$ indépendant de $\theta$).

    *Symétries.* Le plan $\Pi^* = (M, \vec u_r, \vec u_\theta)$, perpendiculaire aux courants, est un plan d'antisymétrie : $\vec B \in \Pi^*$. Le plan $\Pi = (M, \vec u_r, \vec u_z)$, qui contient l'axe, est un plan de symétrie : $\vec B \perp \Pi$. Donc $\vec B = B(r)\,\vec u_\theta$ ; les lignes de champ sont des cercles d'axe $(Oz)$.

    *Théorème d'Ampère.* Contour $\mathcal C$ : cercle de rayon $r$ d'axe $(Oz)$, orienté selon $\vec u_\theta$ :
$$\oint_{\mathcal C}\vec B \cdot d\vec l = \int_0^{2\pi} B(r)\, r\, d\theta = 2\pi r B(r) = \mu_0 I_{\text{enlacé}} = \mu_0\iint_S \vec j \cdot d\vec S$$
    Pour $r \ge R$, tout le courant traverse le disque : $I_{\text{enlacé}} = j\pi R^2 = I$, d'où
$$\vec B(r \ge R) = \frac{\mu_0 I}{2\pi r}\,\vec u_\theta$$
    À l'extérieur, le cylindre se comporte comme un fil infini ; les expressions intérieure et extérieure se raccordent en $r = R$ (valeur $\frac{\mu_0 I}{2\pi R}$).

> **Note :** la rédaction manuscrite est illustrée par le cylindre, le contour d'Ampère circulaire $\mathcal C$ passant par $M$ et les lignes de champ circulaires.

## Exercice 2 : Solénoïde infini parcouru par un courant

**Énoncé.** (4 points) Un solénoïde de rayon $a$, de longueur considérée comme infinie, comportant $n$ spires par unité de longueur, est parcouru par un courant d'intensité $I$ constante. Son axe coïncide avec l'axe $Oz$ du repère cylindrique $(O ; \vec u_r, \vec u_\theta, \vec u_z)$. On connaît le potentiel vecteur $\vec A$ en un point à la distance $r$ de l'axe :

- si $r < a$ : $\vec A(M) = \dfrac{\mu_0 n I}{2}r\,\vec u_\theta$ ;
- si $r > a$ : $\vec A(M) = \dfrac{\mu_0 n I}{2r}a^2\,\vec u_\theta$.

On cherche le champ magnétostatique $\vec B(M)$ en tout point.

1. (Question 14, 1 point) Pour $r < a$ : A) $\vec B = \vec 0$ ; B) $\vec B = \dfrac{\mu_0 n I}{r}\vec u_z$ ; C) $\vec B = \mu_0 n I r\,\vec u_z$ ; D) $\vec B = \mu_0 n I\,\vec u_z$ ; E) aucune des réponses précédentes.
2. (Question 15, 1 point) Démontrer l'expression de $\vec B(M)$ pour $r < a$ en détaillant les calculs (potentiel vecteur $\vec A$, puis calcul de $\vec B$).
3. (Question 16, 1 point) Pour $r > a$ : A) $\vec B = \vec 0$ ; B) $\vec B = \mu_0 n I\,\vec u_z$ ; C) $\vec B = \mu_0 n I r\,\vec u_z$ ; D) $\vec B = \dfrac{\mu_0 n I}{r}\vec u_z$ ; E) aucune des réponses précédentes.
4. (Question 17, 1 point) Démontrer l'expression de $\vec B(M)$ pour $r > a$ en détaillant les calculs.

**Correction.**

1. **D.**
2. On calcule $\vec B = \overrightarrow{\operatorname{rot}}\,\vec A$ avec la formule donnée. Ici $A_r = 0$, $A_z = 0$ et $A_\theta = \dfrac{\mu_0 n I}{2}r$ ne dépend que de $r$ : toutes les dérivées par rapport à $\theta$ et $z$ sont nulles, ainsi que $\frac{\partial A_z}{\partial r}$. Il reste la composante selon $\vec u_z$ :
$$\frac{\partial(rA_\theta)}{\partial r} = \frac{\partial}{\partial r}\left(\frac{\mu_0 n I}{2}r^2\right) = \mu_0 n I r \quad\Longrightarrow\quad \vec B = \frac1r\frac{\partial(rA_\theta)}{\partial r}\vec u_z = \mu_0 n I\,\vec u_z$$
    Le champ est uniforme à l'intérieur du solénoïde.
3. **A.**
4. Pour $r > a$, $rA_\theta = \dfrac{\mu_0 n I}{2}a^2$ est constant, donc $\dfrac{\partial(rA_\theta)}{\partial r} = 0$ ; les autres termes sont nuls comme précédemment. Donc $\vec B = \vec 0$ à l'extérieur du solénoïde infini.

    *Vérification.* Le saut de $B_z$ à la traversée de la nappe de courant ($\mu_0 n I$, avec la densité surfacique de courant $nI$) est bien celui attendu ; et $\vec A$ est continu en $r = a$ (les deux expressions valent $\frac{\mu_0 n I a}{2}$).

## Exercice 3 : Spire circulaire

**Énoncé.** (6 points) Une spire de centre $O$ et de rayon $R$ est parcourue par un courant d'intensité $I$ constante. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$ et on cherche le champ magnétique $\vec B(M)$ en un point $M$ de l'axe de révolution de la spire.

> **Note :** la figure 1 montre la spire dans un plan perpendiculaire à l'axe $Oz$, un point $P$ de la spire avec l'élément $d\vec l$, le point $M$ de l'axe à la distance $z$ de $O$, l'angle $\alpha$ en $M$ entre l'axe et la droite $(MP)$, et la contribution $d\vec B$ en $M$.

1. (Question 18, 1 point) Du fait des invariances, $\vec B(M)$ ne dépend que de : A) $\theta$ ; B) $\varphi$ ; C) $r$ ; D) $z$ ; E) aucune des réponses précédentes.
2. (Question 19, 1 point) Du fait des symétries, $\vec B(M)$ : A) est radial ; B) est orthoradial ; C) a une composante radiale et une orthoradiale ; D) est selon $(Oz)$ ; E) aucune des réponses précédentes.
3. (Question 20, 4 points) Démontrer que le champ en un point $M$ de l'axe s'écrit $\vec B(M) = \dfrac{\mu_0 I}{2R}\sin^3\alpha\,\vec u_z$, en détaillant les calculs (symétries, invariances…).

**Correction.**

1. **D.**
2. **D.**
3. *Symétries.* Les plans $\Pi_1^* = (M, \vec u_r, \vec u_z)$ et $\Pi_2^* = (M, \vec u_\theta, \vec u_z)$ contiennent l'axe ; ce sont des plans d'antisymétrie de la spire (la réflexion retourne le sens du courant). $\vec B(M)$ est contenu dans les deux, donc porté par leur intersection, l'axe : $\vec B$ est selon $\vec u_z$.

    *Invariances.* La spire est invariante par rotation autour de $Oz$ : $\vec B$ ne dépend pas de $\theta$. Sur l'axe, $r = 0$, donc $\vec B = B(z)\,\vec u_z$.

    *Biot et Savart.* Pour $P$ repéré par l'angle $\theta$ :
$$d\vec l = R\, d\theta\,\vec u_\theta, \qquad \overrightarrow{PM} = \overrightarrow{PO} + \overrightarrow{OM} = -R\,\vec u_r + z\,\vec u_z, \qquad PM^2 = R^2 + z^2$$
    Avec $\vec u_\theta \wedge \vec u_r = -\vec u_z$ et $\vec u_\theta \wedge \vec u_z = \vec u_r$ :
$$\vec B = \frac{\mu_0 I}{4\pi}\oint\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3} = \frac{\mu_0 I}{4\pi(R^2 + z^2)^{3/2}}\left[R^2\,\vec u_z\int_0^{2\pi} d\theta + Rz\int_0^{2\pi}\vec u_r\, d\theta\right]$$
    Comme $\vec u_r = \cos\theta\,\vec u_x + \sin\theta\,\vec u_y$, $\int_0^{2\pi}\vec u_r\, d\theta = \big[\sin\theta\big]_0^{2\pi}\vec u_x - \big[\cos\theta\big]_0^{2\pi}\vec u_y = \vec 0$. Il reste
$$\vec B = \frac{\mu_0 I}{2}\,\frac{R^2}{(R^2 + z^2)^{3/2}}\,\vec u_z$$
    et, avec $\sin\alpha = \dfrac{R}{\sqrt{R^2 + z^2}}$ :
$$\vec B(M) = \frac{\mu_0 I}{2R}\sin^3\alpha\;\vec u_z$$

> **Erreur corrigée :** la rédaction manuscrite écrit $\overrightarrow{PM} = -R\,\vec u_r - z\,\vec u_z$ ; avec $\overrightarrow{OM} = z\,\vec u_z$, c'est $+z\,\vec u_z$. L'erreur ne porte que sur la composante radiale, dont l'intégrale est nulle : le résultat n'est pas modifié.
