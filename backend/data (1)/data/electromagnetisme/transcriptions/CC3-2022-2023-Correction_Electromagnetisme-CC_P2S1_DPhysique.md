---
source: CC3-2022-2023-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 9 (grille de réponses page 7, rédactions manuscrites pages 8 et 9)
transcription: manuelle
---

# CC3 d'Électromagnétisme — 26 janvier 2023 (corrigé)

> **Note :** contrôle sans document ni calculatrice. Une seule bonne réponse par question à choix multiples ; les questions marquées ♣ sont à rédiger. Les réponses sont celles de la grille corrigée et des rédactions manuscrites de l'enseignant, vérifiées et détaillées.

## Questions de cours : Biot et Savart, Ampère, équations de Maxwell

**Énoncé.** (5 points, 1 point par question)

1. La loi de Biot et Savart donne le champ magnétique $\vec B$ en $M$ créé par un fil parcouru par un courant $I$. Elle s'énonce : A) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}} \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ ; B) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}} \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^2}$ ; C) $\vec B(M) = \displaystyle\oint_{P \in \text{fil}} \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{MP}}{MP^2}$ ; D) aucune de ces réponses.
2. Le théorème d'Ampère relie le champ $\vec B$ et les intensités $I_i$ (comptées algébriquement) qui traversent toute surface ouverte $S$ s'appuyant sur un contour $\Gamma$. Il s'énonce : A) $\oint_\Gamma \vec B \cdot d\vec l = \mu_0 \sum_i I_i$ ; B) $\oiint_\Gamma \vec B \cdot d\vec l = \mu_0\sum_i I_i$ ; C) $\oint_\Gamma \vec B \wedge d\vec l = \mu_0\sum_i I_i$ ; D) $\oiint_\Gamma \vec B \cdot d\vec S = \mu_0\sum_i I_i$ ; E) aucune de ces réponses.
3. Soient la densité de courant $\vec j$ et la densité volumique de charge $\rho$. L'équation locale de conservation de la charge s'écrit : A) $\operatorname{div}\vec j - \dfrac{\partial\rho}{\partial t} = 0$ ; B) $\operatorname{div}\vec j + \varepsilon_0\dfrac{\partial\rho}{\partial t} = 0$ ; C) $\operatorname{div}\vec j - \varepsilon_0\dfrac{\partial\rho}{\partial t} = 0$ ; D) $\operatorname{div}\vec j + \dfrac{\partial\rho}{\partial t} = 0$ ; E) aucune de ces réponses.
4. Les quatre équations de Maxwell sont :
    A) $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = \dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    B) $\operatorname{div}\vec E = \dfrac{\rho}{\varepsilon_0}$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = -\dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    C) $\operatorname{div}\vec E = \rho$ ; $\operatorname{div}\vec B = 0$ ; $\overrightarrow{\operatorname{rot}}\,\vec E = \dfrac{\partial\vec B}{\partial t}$ ; $\overrightarrow{\operatorname{rot}}\,\vec B = \mu_0\vec j + \mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$ ;
    D) aucune de ces réponses.
5. La loi d'Ohm locale, pour un conducteur de conductivité $\gamma$, s'écrit : A) $\vec j = \gamma^2\vec E$ ; B) $\vec j = \gamma\vec E$ ; C) $\vec j = \dfrac{\vec E}{\gamma}$ ; D) aucune de ces réponses.

**Correction.**

1. **A.** $\vec B(M) = \dfrac{\mu_0 I}{4\pi}\displaystyle\oint \frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ (avec $\overrightarrow{PM}$ non unitaire, la puissance est 3).
2. **A.** La circulation de $\vec B$ sur le contour fermé $\Gamma$ (intégrale simple) vaut $\mu_0$ fois le courant enlacé.
3. **D.** $\operatorname{div}\vec j + \dfrac{\partial\rho}{\partial t} = 0$ : si des charges sortent d'un volume ($\operatorname{div}\vec j > 0$), sa charge diminue.
4. **B.** Le signe moins de l'équation de Maxwell-Faraday traduit la loi de Lenz.
5. **B.** $\vec j = \gamma\vec E$, avec $\gamma$ en $\mathrm{S\,m^{-1}}$.

## Exercice 1 : Pavé infini parcouru par un courant

**Énoncé.** (2 points) Un pavé d'épaisseur $e$, de dimensions infinies dans les autres directions, est parcouru par un courant uniforme et constant, de densité $\vec j$ constante. On repère un point $M$ dans la base $(\vec u_x, \vec u_y, \vec u_z)$. Le plan $Oxy$ est le plan médian du pavé ; l'axe $Oz$ est perpendiculaire à ses faces. Le courant circule dans le sens de l'axe $(Oy)$. On note $\vec B(M)$ le champ magnétique créé en un point $M(x, y, z)$.

> **Note :** l'énoncé parle de « coordonnées cylindriques » mais donne la base cartésienne $(\vec u_x, \vec u_y, \vec u_z)$ ; ce sont bien des coordonnées cartésiennes. La figure montre le pavé d'épaisseur $e$ selon $z$, le vecteur $\vec j$ selon $+\vec u_y$ et un point $M$ au-dessus du pavé.

1. (Question 6, 1 point) En cherchant les plans de symétrie et d'antisymétrie de la distribution, on trouve que :
    A) $\vec B(M)$ est perpendiculaire au plan parallèle à $(xOz)$ passant par $M$ ;
    B) $\vec B(M)$ est perpendiculaire au plan parallèle à $(yOz)$ passant par $M$ ;
    C) le plan parallèle à $(yOz)$ passant par $M$ est un plan d'antisymétrie ;
    D) le plan parallèle à $(xOz)$ passant par $M$ est un plan de symétrie ;
    E) aucune de ces réponses.
2. (Question 7, 1 point) De plus, en regardant les invariances, $\vec B(M)$ s'écrit : A) $B(z)\,\vec u_x$ ; B) $B(z)\,\vec u_y$ ; C) $B(x, y)\,\vec u_z$ ; D) $B(x, y)\,\vec u_x$ ; E) aucune de ces réponses.

**Correction.**

1. **B.** Le plan $x = x_M$ (parallèle à $(yOz)$) contient la direction du courant $\vec u_y$ : la réflexion $x \to -x$ (par rapport à ce plan) laisse la distribution inchangée, c'est un plan de **symétrie**, et $\vec B(M)$ lui est orthogonal : $\vec B \parallel \vec u_x$. Le plan $y = y_M$ (parallèle à $(xOz)$) est perpendiculaire au courant, qu'il retourne : c'est un plan d'**antisymétrie**, qui contient $\vec B$ (ce qui exclut A, C et D).
2. **A.** La distribution est invariante par translation selon $x$ et selon $y$ : $B$ ne dépend que de $z$, et $\vec B = B(z)\,\vec u_x$. (Le plan $z = 0$ étant plan de symétrie des courants, $B(-z) = -B(z)$.)

## Exercice 2 : Électrocinétique

**Énoncé.** (4 points) Un circuit comprend un générateur de courant ($I = 1\ \mathrm{mA}$) et deux résistances $R_1 = 1\ \mathrm{k\Omega}$ et $R_2 = 2\ \mathrm{k\Omega}$.

> **Note :** sur la figure, le générateur (tension $V$ fléchée vers le haut) alimente $R_1$ (tension $V_1$) puis $R_2$ (tension $V_2$), branchées en série et reliées à la masse ; les trois éléments forment une seule maille.

1. (Question 8, 1 point) La loi des mailles s'écrit : A) $V = V_1 - V_2$ ; B) $V = V_1 + V_2$ ; C) $V + V_1 + V_2 = 0$ ; D) aucune de ces réponses.
2. (Question 9, 1 point) En appliquant la loi d'Ohm, la tension $V$ aux bornes du générateur s'écrit : A) $\dfrac{I}{R_1} - \dfrac{I}{R_2}$ ; B) $R_1 I + R_2 I$ ; C) $\dfrac{I}{R_1} + \dfrac{I}{R_2}$ ; D) $R_1 I - R_2 I$ ; E) aucune de ces réponses.
3. (Question 10, 1 point) La valeur de $V$ est alors : A) $3\ \mathrm{kV}$ ; B) $0{,}5\ \mathrm V$ ; C) $3\ \mathrm V$ ; D) $2\ \mathrm V$ ; E) $2\ \mathrm{kV}$ ; F) $1{,}5\ \mathrm V$ ; G) aucune de ces réponses.
4. (Question 11, 1 point) On considère le réseau de résistances décrit ci-dessous. La résistance équivalente $R_{AB}$ entre $A$ et $B$ vaut : A) $1\ \mathrm{k\Omega}$ ; B) $1{,}5\ \mathrm{k\Omega}$ ; C) $2\ \mathrm{k\Omega}$ ; D) $2{,}5\ \mathrm{k\Omega}$ ; E) aucune de ces réponses.

> **Note :** réseau de la question 11 : de $A$, une résistance de $1\ \mathrm{k\Omega}$ mène à un nœud $N_1$. De $N_1$ partent trois branches : deux (deux résistances de $1\ \mathrm{k\Omega}$ en série ; une résistance de $2\ \mathrm{k\Omega}$) aboutissent à un nœud $N_2$, relié à $B$ par une résistance de $1\ \mathrm{k\Omega}$ ; la troisième (deux résistances de $1\ \mathrm{k\Omega}$ en série) va directement de $N_1$ à $B$.

**Correction.**

1. **B.** Le générateur (convention générateur) fournit la tension qui se répartit sur les deux résistances en série : $V = V_1 + V_2$.
2. **B.** Le même courant $I$ traverse $R_1$ et $R_2$ : $V_1 = R_1 I$, $V_2 = R_2 I$, donc $V = (R_1 + R_2)I$.
3. **C.** $V = (1 + 2) \times 10^3\ \Omega \times 10^{-3}\ \mathrm A = 3\ \mathrm V$.
4. **C.** Entre $N_1$ et $N_2$ : $2\ \mathrm{k\Omega} \parallel 2\ \mathrm{k\Omega} = 1\ \mathrm{k\Omega}$ ; en série avec la résistance $N_2B$ : $2\ \mathrm{k\Omega}$. Cette branche est en parallèle avec la branche directe $N_1B$ de $2\ \mathrm{k\Omega}$ : $2 \parallel 2 = 1\ \mathrm{k\Omega}$. Enfin, avec la résistance $AN_1$ : $R_{AB} = 1 + 1 = 2\ \mathrm{k\Omega}$.

## Exercice 3 : Fil infini

**Énoncé.** (5 points) Un fil de longueur infinie, confondu avec l'axe $(Oz)$, est parcouru par un courant $I$ constant orienté vers les $z$ croissants. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$ et on cherche le champ magnétique $\vec B(M)$ créé par le fil.

1. (Question 12, 1 point) En regardant les invariances, $\vec B(M)$ ne dépend que de : A) $\theta$ ; B) $z$ ; C) $\varphi$ ; D) $r$ ; E) aucune de ces réponses.
2. (Question 13, 1 point) Du fait des symétries, $\vec B(M)$ s'écrit : A) $B(\theta)\,\vec u_\theta$ ; B) $B(r)\,\vec u_\theta$ ; C) $B(z)\,\vec u_z$ ; D) $B(z)\,\vec u_r$ ; E) aucune de ces réponses.
3. (Question 14, 1 point) Par le théorème d'Ampère : A) $\dfrac{\mu_0 I}{\pi z}\vec u_r$ ; B) $\dfrac{\mu_0 I}{\pi z}\vec u_\theta$ ; C) $\dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; D) $\dfrac{2\mu_0 I}{\pi r}\vec u_z$ ; E) aucune de ces réponses.
4. (Question 15 ♣, 2 points) Détailler les calculs donnant $\vec B(M)$.

**Correction.**

1. **D.**
2. **B.**
3. **C.**
4. *Définition.* Distribution linéique de courant : $\vec B$ n'est pas défini sur le fil ($r = 0$).

    *Coordonnées.* Cylindriques, d'origine $O$ sur le fil (choisie à la hauteur de $M$, ce qui est possible car le fil est infini) ; base $(\vec u_r, \vec u_\theta, \vec u_z)$.

    *Invariances.* La distribution de courant est invariante par rotation autour de $(Oz)$ ($\vec B$ indépendant de $\theta$) et, le fil étant infini, par translation selon $(Oz)$ ($\vec B$ indépendant de $z$) : $\vec B = \vec B(r)$.

    *Symétries.* $\Pi = (M, \vec u_r, \vec u_z)$, qui contient le fil, est un plan de symétrie : $\vec B \perp \Pi$. $\Pi^* = (M, \vec u_r, \vec u_\theta)$, perpendiculaire au fil, est un plan d'antisymétrie : $\vec B \in \Pi^*$. Donc $\vec B = B(r)\,\vec u_\theta$.

    *Théorème d'Ampère.* Contour $\mathcal C$ : cercle d'axe $(Oz)$ et de rayon $r$ passant par $M$, orienté selon $\vec u_\theta$ (le courant $I$, dirigé selon $+\vec u_z$, est alors compté positivement) :
$$\oint_{\mathcal C}\vec B \cdot d\vec l = \int_0^{2\pi} B(r)\,\vec u_\theta \cdot r\, d\theta\,\vec u_\theta = 2\pi r B(r) = \mu_0 I_{\text{enlacé}} = \mu_0 I$$
    d'où
$$\vec B(M) = \frac{\mu_0 I}{2\pi r}\,\vec u_\theta$$

## Exercice 4 : Spire circulaire

**Énoncé.** (6 points) Une spire de centre $O$ et de rayon $R$ est parcourue par un courant d'intensité $I$ constante. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$ et on cherche le champ magnétique $\vec B(M)$ en un point $M$ de l'axe de révolution de la spire.

> **Note :** la figure montre la spire dans un plan perpendiculaire à l'axe $Oz$, un point $P$ de la spire avec l'élément $d\vec l$, le point $M$ de l'axe à la distance $z$ de $O$, l'angle $\alpha$ sous lequel on voit le rayon $R$ depuis $M$ (angle en $M$ entre l'axe et la droite $(MP)$), et la contribution $d\vec B$ en $M$.

1. (Question 16, 1 point) Du fait des invariances, $\vec B(M)$ ne dépend que de : A) $r$ ; B) $\varphi$ ; C) $\theta$ ; D) $z$ ; E) aucune de ces réponses.
2. (Question 17, 1 point) Du fait des symétries, $\vec B(M)$ est de la forme : A) $B(\theta)\,\vec u_\theta$ ; B) $B(r)\,\vec u_r$ ; C) $B(r)\,\vec u_z$ ; D) $B(z)\,\vec u_z$ ; E) aucune de ces réponses.
3. (Question 18, 2 points) Par intégration de la loi de Biot et Savart, le champ en un point de l'axe à la distance $z$ s'écrit : A) $\dfrac{\mu_0 I}{R}\sin^3\alpha\,\vec u_\theta$ ; B) $\dfrac{2\mu_0 I}{R}\sin^3\alpha\,\vec u_z$ ; C) $\dfrac{\mu_0 I}{2R}\sin^3\alpha\,\vec u_z$ ; D) $\dfrac{\mu_0 I}{R}\sin^3\alpha\,\vec u_r$ ; E) aucune de ces réponses.
4. (Question 19 ♣, 2 points) Détailler les calculs donnant $\vec B(M)$.

**Correction.**

1. **D.** Sur l'axe, seule la cote $z$ varie ; la spire est invariante par rotation autour de l'axe.
2. **D.** Tout plan contenant l'axe (donc $M$) est un plan d'antisymétrie de la spire (il retourne le sens du courant) : $\vec B(M)$ est contenu dans tous ces plans, donc porté par leur intersection, l'axe : $\vec B = B(z)\,\vec u_z$.
3. **C.** Voir la question 19.
4. *Biot et Savart.* $\vec B = \displaystyle\oint_{\text{spire}} \frac{\mu_0}{4\pi}\frac{I\, d\vec l \wedge \overrightarrow{PM}}{PM^3}$, avec, pour un point $P$ de la spire repéré par $\theta$ :
$$d\vec l = R\, d\theta\,\vec u_\theta, \qquad \overrightarrow{PM} = \overrightarrow{PO} + \overrightarrow{OM} = -R\,\vec u_r + z\,\vec u_z, \qquad PM^2 = R^2 + z^2$$
    Avec $\vec u_\theta \wedge \vec u_r = -\vec u_z$ et $\vec u_\theta \wedge \vec u_z = \vec u_r$ :
$$d\vec l \wedge \overrightarrow{PM} = R\, d\theta\left(R\,\vec u_z + z\,\vec u_r\right)$$
    $PM$ étant constant sur la spire :
$$\vec B = \frac{\mu_0 I R}{4\pi(R^2 + z^2)^{3/2}}\left[R\,\vec u_z\int_0^{2\pi} d\theta + z\int_0^{2\pi}\vec u_r(\theta)\, d\theta\right]$$
    Or $\vec u_r = \cos\theta\,\vec u_x + \sin\theta\,\vec u_y$, donc $\int_0^{2\pi}\vec u_r\, d\theta = \vec 0$ (les contributions radiales se compensent deux à deux, comme le prévoyaient les symétries). Il reste
$$\vec B = \frac{\mu_0 I R^2}{4\pi(R^2 + z^2)^{3/2}} \cdot 2\pi\,\vec u_z = \frac{\mu_0 I}{2}\,\frac{R^2}{(R^2 + z^2)^{3/2}}\,\vec u_z$$
    Avec $\sin\alpha = \dfrac{R}{PM} = \dfrac{R}{\sqrt{R^2 + z^2}}$, on a $\dfrac{R^2}{(R^2 + z^2)^{3/2}} = \dfrac{\sin^3\alpha}{R}$, d'où
$$\vec B(M) = \frac{\mu_0 I}{2R}\sin^3\alpha\;\vec u_z$$
    Vérification : au centre ($z = 0$, $\alpha = \frac{\pi}{2}$), $B = \dfrac{\mu_0 I}{2R}$, le résultat classique.

> **Erreur corrigée :** la rédaction manuscrite écrit $\overrightarrow{PM} = -R\,\vec u_r - z\,\vec u_z$ ; comme $\overrightarrow{OM} = z\,\vec u_z$, c'est $+z\,\vec u_z$. Le terme concerné est la composante radiale, dont l'intégrale est nulle : le résultat final n'est pas affecté.
