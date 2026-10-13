---
source: CC3-2024-2025-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 15 (réponses cochées dans l'énoncé et sur la grille page 12, rédactions manuscrites pages 13 à 15)
transcription: manuelle
---

# CC3 d'Électromagnétisme — 16 janvier 2025 (corrigé)

> **Note :** contrôle de 1 h 30, sans document ni calculatrice, 19 questions. Une seule bonne réponse par question à choix multiples ; les questions 8, 13 et 17 sont à rédiger. Les réponses sont celles cochées par l'enseignant et de ses rédactions manuscrites, vérifiées et détaillées.

## Questions de cours : Ampère, Maxwell, conservation de la charge

**Énoncé.** (4 points)

1. (0,5 point) Le théorème d'Ampère relie le champ $\vec B$ et les intensités $I_i$ (comptées algébriquement) qui traversent toute surface ouverte $S$ s'appuyant sur un contour $\Gamma$. Il s'énonce : A) $\oint_\Gamma \vec B \wedge d\vec l = \mu_0\sum_i I_i$ ; B) $\oiint_\Gamma \vec B \cdot d\vec S = \mu_0\sum_i I_i$ ; C) $\oint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; D) $\oiint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; E) aucune des réponses précédentes.
2. (0,5 point) En étudiant les plans d'antisymétrie de la distribution de courant, on trouve que $\vec B$ en $M$ :
    A) a la direction de la droite intersection d'un plan de symétrie et d'un plan d'antisymétrie passant par $M$ ;
    B) est inclus dans tout plan $\Pi'$ d'antisymétrie passant par $M$ ;
    C) a la direction de la droite orthogonale à un plan $\Pi'$ d'antisymétrie passant par $M$ ;
    D) aucune des réponses précédentes.
3. (1 point) Les quatre équations de Maxwell sont :
    A) $\operatorname{div}\vec E = \rho$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = \dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    B) $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = \dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    C) $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = -\dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    D) aucune des réponses précédentes.
4. (1 point) L'équation locale de conservation de la charge s'écrit : A) $\operatorname{div}\vec j - \varepsilon_0\dfrac{\partial\rho}{\partial t} = 0$ ; B) $\operatorname{div}\vec j + \varepsilon_0\dfrac{\partial\rho}{\partial t} = 0$ ; C) $\operatorname{div}\vec j + \dfrac{\partial\rho}{\partial t} = 0$ ; D) $\operatorname{div}\vec j - \dfrac{\partial\rho}{\partial t} = 0$ ; E) aucune des réponses précédentes.
5. (1 point) La circulation $C$ du champ magnétique $\vec B$ sur le contour orienté $\Gamma$ de la figure vaut : A) $I_1 + 2I_2 - I_3 + 3I_4$ ; B) $-I_1 + I_3 - 3I_4$ ; C) $I_1 - I_3 - 3I_4$ ; D) $-I_1 + I_3 + 3I_4$ ; E) $I_1 + 2I_2 - I_3 - I_4$ ; F) $-I_1 + I_3 + 3I_4 - I_5 + I_6$ ; G) aucune des réponses précédentes.

> **Note :** la figure de la question 5 montre un contour fermé $\Gamma$ vu en perspective, parcouru vers la droite sur sa partie avant, et six courants : $I_1$ le traverse en montant ; $I_2$ monte à travers la surface puis redescend à travers elle en formant une boucle ; $I_3$ le traverse en descendant ; $I_4$ s'enroule autour du bord droit du contour ; $I_5$ est une petite boucle fermée à l'intérieur ; $I_6$ passe à l'extérieur.

**Correction.**

1. **C.** $\oint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$.
2. **B.** En un point d'un plan d'antisymétrie des courants, $\vec B$ est contenu dans ce plan.
3. **C.**
4. **C.** $\operatorname{div}\vec j + \dfrac{\partial\rho}{\partial t} = 0$.
5. **C** (à un facteur $\mu_0$ près, voir l'encadré). L'orientation de $\Gamma$ fixe, par la règle de la main droite, le sens positif de traversée de la surface qu'il délimite : ici vers le haut. $I_1$ traverse dans le sens positif ($+I_1$) ; $I_3$ dans le sens négatif ($-I_3$) ; $I_2$ traverse deux fois en sens opposés (contribution nulle) ; $I_5$ (boucle fermée qui ne traverse pas la surface) et $I_6$ (extérieur) ne sont pas enlacés ; $I_4$ s'enroule autour du contour et le corrigé compte trois traversées dans le sens négatif ($-3I_4$). D'où
$$\oint_\Gamma \vec B \cdot d\vec l = \mu_0\left(I_1 - I_3 - 3I_4\right)$$

> **Erreur corrigée :** les propositions omettent le facteur $\mu_0$ : la circulation de $\vec B$ vaut $\mu_0(I_1 - I_3 - 3I_4)$, pas $I_1 - I_3 - 3I_4$ (qui est homogène à un courant). La réponse C du corrigé correspond au courant enlacé.

## Exercice 1 : Fil rectiligne de longueur infinie

**Énoncé.** (5 points) Un fil rectiligne infini est parcouru par un courant $I$ uniforme et constant. On se place dans la base cartésienne $(\vec e_x, \vec e_y, \vec e_z)$. Soient le point $M$ de coordonnées $(x, 0, 0)$ et le point $P$ de coordonnées $(0, y, 0)$, associé à l'élément de courant $I\,d\vec l$.

> **Note :** la figure montre le fil confondu avec l'axe $Oy$, le courant $I$ dirigé vers les $y$ croissants, le point $P$ sur le fil, le point $M$ sur l'axe $Ox$ ($x > 0$) et l'axe $Oz$ pointant vers l'observateur (repère direct).

1. (Question 6, 1 point) La loi de Biot et Savart s'énonce : A) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{MP}}{MP^2}$ ; B) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^2}$ ; C) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}}\frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ ; D) aucune des réponses précédentes.
2. (Question 7, 1 point) Par la loi de Biot et Savart, le champ élémentaire $d\vec B(M)$ s'écrit :
    A) $\dfrac{\mu_0 I}{4\pi}\dfrac{x}{(x^2 + y^2)^{3/2}}dy\,\vec e_z$ ;
    B) $-\dfrac{\mu_0 I}{4\pi}\dfrac{x}{(x^2 + y^2)^{3/2}}dy\,\vec e_x$ ;
    C) $-\dfrac{\mu_0 I}{4\pi}\dfrac{x}{(x^2 + y^2)^{3/2}}dy\,\vec e_z$ ;
    D) $\dfrac{\mu_0 I}{4\pi}\dfrac{x}{(x^2 + y^2)^{3/2}}dy\,\vec e_x$ ;
    E) aucune des réponses précédentes.
3. (Question 8, 2 points) Démontrer l'expression du champ élémentaire $d\vec B(M)$.
4. (Question 9, 1 point) Sachant que $\displaystyle\int_{-\infty}^{+\infty}\frac{x}{(x^2 + y^2)^{3/2}}dy = \frac{2}{x}$, le champ total $\vec B$ vaut : A) $\dfrac{\mu_0 I}{2\pi x}\vec e_x$ ; B) $\dfrac{\mu_0 I}{2\pi x}\vec e_z$ ; C) $-\dfrac{\mu_0 I}{2\pi y}\vec e_z$ ; D) $\dfrac{\mu_0 I}{2\pi y}\vec e_z$ ; E) $-\dfrac{\mu_0 I}{2\pi y}\vec e_x$ ; F) $-\dfrac{\mu_0 I}{2\pi x}\vec e_z$ ; G) $\dfrac{\mu_0 I}{2\pi y}\vec e_x$ ; H) $-\dfrac{\mu_0 I}{2\pi x}\vec e_x$ ; I) aucune des réponses précédentes.

**Correction.**

1. **C.**
2. **C.** Voir la question 8.
3. $d\vec B(M) = \dfrac{\mu_0 I}{4\pi}\dfrac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ avec
$$d\vec l = dy\,\vec e_y, \qquad \overrightarrow{PM} = \begin{pmatrix} x \\ -y \\ 0 \end{pmatrix}, \qquad PM^2 = x^2 + y^2$$
$$d\vec l \wedge \overrightarrow{PM} = \begin{pmatrix} 0 \\ dy \\ 0 \end{pmatrix} \wedge \begin{pmatrix} x \\ -y \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -x\, dy \end{pmatrix}$$
    donc
$$d\vec B(M) = -\frac{\mu_0 I}{4\pi}\,\frac{x}{(x^2 + y^2)^{3/2}}\,dy\;\vec e_z$$
4. **F.** On intègre sur tout le fil :
$$\vec B = -\frac{\mu_0 I}{4\pi}\,\frac{2}{x}\,\vec e_z = -\frac{\mu_0 I}{2\pi x}\,\vec e_z$$
    On retrouve le champ $\frac{\mu_0 I}{2\pi d}$ d'un fil infini à la distance $d = x$ ; son sens ($-\vec e_z$) est bien celui de la règle de la main droite pour un courant selon $+\vec e_y$ vu depuis un point de l'axe $+Ox$ ($\vec e_y \wedge \vec e_x = -\vec e_z$).

> **Note :** l'intégrale donnée dans l'énoncé est mal extraite du PDF ; sa valeur $\frac{2}{x}$ (pour $x > 0$) a été vérifiée : une primitive de $\frac{x}{(x^2 + y^2)^{3/2}}$ en $y$ est $\frac{y}{x\sqrt{x^2 + y^2}}$, qui vaut $\pm\frac1x$ en $\pm\infty$.

## Exercice 2 : Force de Lorentz

**Énoncé.** (3 points)

1. (Question 10, 0,5 point) En présence d'un champ magnétique $\vec B$ et sans champ électrique, une charge $q$ de vitesse $\vec v$ est soumise à la force de Lorentz : A) $\vec f_L = q\,\vec v \wedge \vec B$ ; B) $\vec f_L = q\,\vec v \cdot \vec B$ ; C) $\vec f_L = qB\vec v$ ; D) $\vec f_L = qv\vec B$ ; E) aucune des réponses précédentes.
2. (Question 11, 0,5 point) Trois particules de même masse arrivent avec la même vitesse dans une région où règne un champ magnétique $\vec B$ uniforme et constant, sortant de la feuille. La particule qui a une charge positive est la : A) 2 ; B) 3 ; C) 1 ; D) aucune des réponses précédentes.
3. Des particules de charge $q > 0$ pénètrent avec la vitesse $\vec v = v_y\,\vec e_y$ ($v_y > 0$) dans un champ magnétique constant et uniforme $\vec B = B_z\,\vec e_z$ ($B_z > 0$), dans un repère orthonormé direct $(O ; x, y, z)$.
    a) (Question 12, 1 point) La force de Lorentz vaut : A) $-qv_yB_z\,\vec e_x$ ; B) $qv_yB_z\,\vec e_z$ ; C) $qv_yB_z\,\vec e_x$ ; D) $-qv_yB_z\,\vec e_y$ ; E) $-qv_yB_z\,\vec e_z$ ; F) $qv_yB_z\,\vec e_y$ ; G) aucune des réponses précédentes.
    b) (Question 13, 1 point) Détailler le calcul de cette force.

> **Note :** la figure de la question 11 montre les points du champ $\vec B$ sortant et trois trajectoires partant du même point vers la droite : les particules 1 et 2 sont déviées vers le haut (1 plus fortement que 2), la particule 3 vers le bas.

**Correction.**

1. **A.**
2. **B.** Prenons $\vec v = v\,\vec e_x$ (vers la droite) et $\vec B = B\,\vec e_z$ (sortant). Pour $q > 0$, $\vec f_L = qvB\,(\vec e_x \wedge \vec e_z) = -qvB\,\vec e_y$ : la particule est déviée vers le bas. C'est la particule 3 ; les particules 1 et 2, déviées vers le haut, sont négatives.
3.
    a) **C.**
    b) Avec $\vec v = (0, v_y, 0)$ et $\vec B = (0, 0, B_z)$ :
$$\vec F_L = q\,\vec v \wedge \vec B = q\begin{pmatrix} v_y B_z - 0 \\ 0 - 0 \\ 0 - 0 \end{pmatrix} = q v_y B_z\,\vec e_x$$
    (en accord avec $\vec e_y \wedge \vec e_z = \vec e_x$).

## Exercice 3 : Relation de dispersion

**Énoncé.** (4 points) Donnée : rotationnel en coordonnées cartésiennes,
$$\begin{aligned}\overrightarrow{\operatorname{rot}}\,\vec U = {} & \left(\frac{\partial U_z}{\partial y} - \frac{\partial U_y}{\partial z}\right)\vec u_x + \left(\frac{\partial U_x}{\partial z} - \frac{\partial U_z}{\partial x}\right)\vec u_y \\ & + \left(\frac{\partial U_y}{\partial x} - \frac{\partial U_x}{\partial y}\right)\vec u_z\end{aligned}$$
On considère dans le vide le champ électrique $\vec E = E_0\, e^{\alpha t - \beta x}\,\vec e_z$ ($\alpha, \beta \in \mathbb{C}$).

1. (Question 14, 1 point) Le rotationnel de $\vec E$ vaut : A) $\beta E_y\,\vec e_z$ ; B) $\beta E_y\,\vec e_y$ ; C) $\beta E_z\,\vec e_z$ ; D) $\beta E_z\,\vec e_y$ ; E) aucune des réponses précédentes.
2. (Question 15, 1 point) Par une des équations de Maxwell, le champ magnétique vaut : A) $-\dfrac{\alpha}{\beta}E_y\,\vec e_z$ ; B) $-\dfrac{\alpha}{\beta}E_z\,\vec e_y$ ; C) $\dfrac{\beta}{\alpha}E_z\,\vec e_y$ ; D) $\dfrac{\alpha}{\beta}E_z\,\vec e_y$ ; E) $\dfrac{\alpha}{\beta}E_y\,\vec e_z$ ; F) $\dfrac{\beta}{\alpha}E_y\,\vec e_z$ ; G) $-\dfrac{\beta}{\alpha}E_y\,\vec e_z$ ; H) $-\dfrac{\beta}{\alpha}E_z\,\vec e_y$ ; I) aucune des réponses précédentes.
3. (Question 16, 1 point) Le rotationnel de $\vec B$ vaut donc : A) $\dfrac{\beta}{\alpha}\vec E$ ; B) $\dfrac{\alpha}{\beta}\vec E$ ; C) $-\dfrac{\beta}{\alpha}\vec E$ ; D) $-\dfrac{\beta^2}{\alpha}\vec E$ ; E) $\dfrac{\beta^2}{\alpha}\vec E$ ; F) $-\dfrac{\alpha}{\beta}\vec E$ ; G) aucune des réponses précédentes.
4. (Question 17, 3 points) Détailler le calcul de $\vec B$, en expliquant comment vous avez obtenu $\overrightarrow{\operatorname{rot}}\,\vec E$.

**Correction.**

1. **D.**
2. **H.**
3. **E.**
4. *Rotationnel de $\vec E$.* Seule la composante $E_z = E_0 e^{\alpha t - \beta x}$ est non nulle, et elle ne dépend que de $x$ (et de $t$). Dans la formule, il ne reste que le terme $-\dfrac{\partial E_z}{\partial x}\vec u_y$ :
$$\overrightarrow{\operatorname{rot}}\,\vec E = -\frac{\partial E_z}{\partial x}\,\vec e_y = \beta E_0 e^{\alpha t - \beta x}\,\vec e_y = \beta E_z\,\vec e_y$$

    *Champ magnétique.* L'équation de Maxwell-Faraday $\overrightarrow{\operatorname{rot}}\,\vec E = -\dfrac{\partial\vec B}{\partial t}$ donne $\dfrac{\partial\vec B}{\partial t} = -\beta E_0 e^{\alpha t - \beta x}\,\vec e_y$. On intègre par rapport au temps, en ne retenant que la partie variable (on ignore un éventuel champ statique) :
$$\vec B = -\frac{\beta}{\alpha}E_0 e^{\alpha t - \beta x}\,\vec e_y = -\frac{\beta}{\alpha}E_z\,\vec e_y$$

    *Rotationnel de $\vec B$ (question 16).* $\vec B$ n'a qu'une composante $B_y = -\frac{\beta}{\alpha}E_z$, fonction de $x$ : $\overrightarrow{\operatorname{rot}}\,\vec B = \dfrac{\partial B_y}{\partial x}\vec e_z = -\dfrac{\beta}{\alpha}(-\beta)E_z\,\vec e_z = \dfrac{\beta^2}{\alpha}\vec E$.

    > **Complément :** c'est ce qui donne la relation de dispersion annoncée par le titre. Dans le vide, Maxwell-Ampère s'écrit $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t} = \mu_0\varepsilon_0\alpha\vec E$. En comparant, $\dfrac{\beta^2}{\alpha} = \dfrac{\alpha}{c^2}$, soit $\beta^2 = \dfrac{\alpha^2}{c^2}$. Pour une onde plane progressive harmonique, $\alpha = i\omega$ et $\beta = ik$, et l'on retrouve $k^2 = \dfrac{\omega^2}{c^2}$.

## Exercice 4 : Pavé infini parcouru par un courant

**Énoncé.** (2 points) Un pavé d'épaisseur $e$, de largeur et de longueur infinies, est parcouru par un courant de densité $\vec j$ uniforme et constante, dirigée selon l'axe $(Oy)$. On repère un point $M$ dans la base cartésienne $(\vec u_x, \vec u_y, \vec u_z)$ ; le plan $Oxy$ est le plan médian du pavé, l'axe $Oz$ est perpendiculaire à ses faces. On note $\vec B(M)$ le champ créé en un point $M(x, y, z)$.

> **Note :** la figure montre le pavé d'épaisseur $e$ selon $z$, le vecteur $\vec j$ selon $+\vec u_y$ et un point $M$ au-dessus du pavé.

1. (Question 18, 1 point) En cherchant les plans de symétrie et d'antisymétrie, on trouve que :
    A) le plan parallèle à $(yOz)$ passant par $M$ est un plan d'antisymétrie ;
    B) $\vec B(M)$ est perpendiculaire au plan parallèle à $(xOz)$ passant par $M$ ;
    C) le plan parallèle à $(xOz)$ passant par $M$ est un plan de symétrie ;
    D) $\vec B(M)$ est perpendiculaire au plan $(yOz)$ passant par $M$ ;
    E) aucune de ces réponses.
2. (Question 19, 1 point) En regardant les invariances, $\vec B(M)$ s'écrit : A) $B(z)\,\vec u_y$ ; B) $B(x, y)\,\vec u_z$ ; C) $B(z)\,\vec u_x$ ; D) $B(x, y)\,\vec u_x$ ; E) aucune de ces réponses.

**Correction.**

1. **D.** Le plan $x = x_M$ contient la direction $\vec u_y$ du courant : c'est un plan de symétrie, et $\vec B$ lui est orthogonal ($\vec B \parallel \vec u_x$). Le plan $y = y_M$, perpendiculaire au courant, est un plan d'antisymétrie qui contient $\vec B$ ; les propositions A, B et C inversent ces rôles.
2. **C.** Invariance par translation selon $x$ et $y$ : $\vec B = B(z)\,\vec u_x$ (avec $B(-z) = -B(z)$, le plan $z = 0$ étant plan de symétrie).
