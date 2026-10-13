---
source: CC2-2022-2023-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 12 (grille de réponses page 9, rédactions manuscrites pages 10 à 12)
transcription: manuelle
---

# CC2 d'Électromagnétisme — 8 décembre 2022 (corrigé)

> **Note :** contrôle de 1 h 30, sans document ni calculatrice. Une seule bonne réponse par question à choix multiples ; les questions marquées ♣ sont à rédiger. Les réponses sont celles de la grille corrigée et des rédactions manuscrites de l'enseignant, vérifiées et détaillées.

## Questions de cours : Biot et Savart, symétries, potentiel, conducteurs

**Énoncé.** (5 points)

1. (0,5 point) La loi de Biot et Savart donne le champ magnétique $\vec B$ d'une distribution linéique de courant $I$ le long d'un circuit $\Gamma$, $P$ étant un point du circuit. Elle s'énonce : A) $\vec B(M) = \displaystyle\oint_\Gamma \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^2}$ ; B) $\vec B(M) = \displaystyle\oint_\Gamma \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ ; C) $\vec B(M) = \displaystyle\oint_\Gamma \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{MP}}{MP^2}$ ; D) aucune de ces réponses.
2. (0,5 point) En étudiant les plans d'antisymétrie de la distribution de courant, on trouve que le champ $\vec B$ en $M$ :
    A) a la direction de la droite intersection d'un plan de symétrie et d'un plan d'antisymétrie passant par $M$ ;
    B) est inclus dans tout plan $\Pi'$ d'antisymétrie passant par $M$ ;
    C) a la direction de la droite orthogonale à un plan $\Pi'$ d'antisymétrie passant par $M$ ;
    D) aucune de ces réponses.
3. (0,5 point) En étudiant les plans de symétrie de la distribution de courant, on trouve que la direction de $\vec B$ en $M$ est :
    A) celle de la droite intersection d'au moins deux plans de symétrie passant par $M$ ;
    B) incluse dans tout plan $\Pi$ de symétrie passant par $M$ ;
    C) celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    D) aucune de ces réponses.
4. (0,5 point) Puisque $\vec E$ est à circulation conservative, on définit le potentiel électrostatique $V$ par : A) $\vec V = \overrightarrow{\operatorname{grad}}\, E$ ; B) $\vec E = -\overrightarrow{\operatorname{grad}}\, V$ ; C) $\vec E = \overrightarrow{\operatorname{grad}}\, V$ ; D) aucune de ces réponses.
5. (0,5 point) Dans le cas d'une distribution volumique de charges, le potentiel électrostatique : A) n'est pas défini aux points où se trouvent les charges ; B) est défini et continu en tout point de l'espace ; C) est défini sur la surface chargée et non continu à la traversée de la surface ; D) aucune de ces réponses.
6. (0,5 point) Les lignes de champ de $\vec E$ sont : A) en tout point perpendiculaires aux équipotentielles ; B) en tout point confondues avec les équipotentielles ; C) en tout point perpendiculaires au champ $\vec E$ ; D) aucune de ces réponses.
7. (0,5 point) L'énergie potentielle d'interaction entre une charge $q$ et un champ $\vec E$ dérivant du potentiel $V$ est : A) $E_p = qV + K$ ; B) $E_p = -qV + K$ ; C) $E_p = qE + K$ ; D) aucune de ces réponses.
8. (1 point) Il y a une différence de potentiel de $10\ \mathrm V$ entre deux plaques distantes de $1\ \mathrm{cm}$. La norme du champ électrique entre les plaques vaut : A) $500\ \mathrm{V/m}$ ; B) $250\ \mathrm{V/m}$ ; C) $10\ \mathrm{V/m}$ ; D) $1000\ \mathrm{V/m}$ ; E) aucune de ces réponses.
9. (0,5 point) À l'intérieur d'un conducteur en équilibre électrostatique : A) le champ créé par les charges du conducteur est nul ; B) le champ créé par toutes les charges (du conducteur et extérieures) est nul ; C) le champ créé par les charges extérieures au conducteur est nul ; D) aucune de ces réponses.

**Correction.**

1. **B.** $d\vec B = \dfrac{\mu_0}{4\pi}\dfrac{I\, d\vec l \wedge \overrightarrow{PM}}{PM^3}$ : $\overrightarrow{PM}$ n'étant pas unitaire, la puissance est 3.
2. **B.** $\vec B$ est un pseudo-vecteur : en un point d'un plan d'**antisymétrie** des courants, il est contenu dans ce plan.
3. **C.** En un point d'un plan de **symétrie** des courants, $\vec B$ est orthogonal à ce plan (c'est l'inverse du champ électrique).
4. **B.** $\vec E = -\overrightarrow{\operatorname{grad}}\, V$.
5. **B.** Densité volumique finie : $V$ défini et continu partout.
6. **A.** $\vec E = -\overrightarrow{\operatorname{grad}}\, V$ est normal aux surfaces $V = \text{cste}$ ; les lignes de champ, tangentes à $\vec E$, coupent donc les équipotentielles à angle droit.
7. **A.** $E_p = qV + K$.
8. **D.** Entre deux plaques parallèles, le champ est uniforme : $E = \dfrac{U}{d} = \dfrac{10\ \mathrm V}{10^{-2}\ \mathrm m} = 1000\ \mathrm{V/m}$.
9. **B.** À l'équilibre, les charges libres du conducteur ne bougent pas : le champ **total** y est nul (les charges du conducteur se répartissent en surface de façon à compenser exactement le champ extérieur).

## Exercice 1 : Sphères chargées

**Énoncé.** (9 points) Une sphère pleine de centre $O$ et de rayon $R_1$ porte la densité volumique de charge $\rho(r) = \dfrac{A}{r^2}$, où $A$ est une constante. Elle est à l'intérieur d'une sphère creuse de même centre, de rayon $R_2 > R_1$, chargée uniformément en surface avec la densité $\sigma_0$ (constante).

1. (Question 10, 1 point) La dimension de $A$ est ($Q$ : charge, $L$ : longueur) : A) $Q^{-1}L$ ; B) $QL^{-1}$ ; C) $QL^{-2}$ ; D) $Q^{-1}L^{-1}$ ; E) aucune de ces réponses.
2. (Question 11, 1 point) Les charges totales $Q_1$ et $Q_2$ des deux sphères valent : A) $Q_1 = 4\pi A R_1$ et $Q_2 = 4\pi\sigma_0 R_2^2$ ; B) $Q_1 = 4\pi A R_1^2$ et $Q_2 = 4\pi\sigma_0 R_2$ ; C) $Q_1 = \pi A R_1^{-2}$ et $Q_2 = \pi\sigma_0 R_2^{-2}$ ; D) $Q_1 = \pi A R_1^{-1}$ et $Q_2 = \pi\sigma_0 R_2$ ; E) aucune de ces réponses.
3. (Question 12, 1 point) Le champ $\vec E(r)$ à la distance $r$ de $O$, pour $0 < r \le R_1$, vaut : A) $\dfrac{AR_1 + \sigma_0 R_2^2}{\varepsilon_0 r^2}\vec u_r$ ; B) $\dfrac{AR_1}{\varepsilon_0 r^2}\vec u_r$ ; C) $-\dfrac{A}{\varepsilon_0 r}\vec u_r$ ; D) $\dfrac{A}{\varepsilon_0 r}\vec u_r$ ; E) aucune de ces réponses.
4. (Question 13, 1 point) Pour $R_1 \le r < R_2$ : A) $\dfrac{AR_1 + \sigma_0 R_2^2}{\varepsilon_0 r^2}\vec u_r$ ; B) $\dfrac{A}{\varepsilon_0 r}\vec u_r$ ; C) $\dfrac{AR_1}{\varepsilon_0 r^2}\vec u_r$ ; D) $-\dfrac{A}{\varepsilon_0 r}\vec u_r$ ; E) aucune de ces réponses.
5. (Question 14, 1 point) Pour $r > R_2$ : A) $-\dfrac{A}{\varepsilon_0 r}\vec u_r$ ; B) $\dfrac{AR_1 + \sigma_0 R_2^2}{\varepsilon_0 r^2}\vec u_r$ ; C) $\dfrac{A}{\varepsilon_0 r}\vec u_r$ ; D) $\dfrac{AR_1}{\varepsilon_0 r^2}\vec u_r$ ; E) aucune de ces réponses.
6. (Question 15 ♣, 3 points) Détailler les calculs donnant $\vec E(r)$ pour $0 < r \le R_1$.
7. (Question 16, 1 point) Le potentiel étant nul à l'infini, le potentiel $V(r)$ pour $0 < r \le R_1$ vaut : A) $\dfrac{A}{\varepsilon_0}\dfrac{R_1}{r} + \dfrac{A}{\varepsilon_0}$ ; B) $\dfrac{A}{\varepsilon_0}\ln\dfrac{R_1}{r} - \dfrac{A}{\varepsilon_0}$ ; C) $-\dfrac{A}{\varepsilon_0}\left(\dfrac{R_1}{r}\right)^2 + \dfrac{A + \sigma_0 R_2}{\varepsilon_0}$ ; D) $\dfrac{A}{\varepsilon_0}\ln\dfrac{R_1}{r} + \dfrac{A + \sigma_0 R_2}{\varepsilon_0}$ ; E) aucune de ces réponses.

**Correction.**

1. **B.** $A = \rho r^2$ : $[A] = QL^{-3} \cdot L^2 = QL^{-1}$ (des $\mathrm{C\,m^{-1}}$).
2. **A.** $Q_1 = \displaystyle\int_0^{R_1}\frac{A}{r^2}\,4\pi r^2\, dr = 4\pi A R_1$ et $Q_2 = \sigma_0 \cdot 4\pi R_2^2$. Les deux sont bien homogènes à une charge.
3. **D.** Voir la question 15 : $\vec E = \dfrac{A}{\varepsilon_0 r}\vec u_r$.
4. **C.** La sphère de Gauss contient $Q_1$ : $E = \dfrac{Q_1}{4\pi\varepsilon_0 r^2} = \dfrac{AR_1}{\varepsilon_0 r^2}$.
5. **B.** Elle contient $Q_1 + Q_2$ : $E = \dfrac{4\pi AR_1 + 4\pi\sigma_0 R_2^2}{4\pi\varepsilon_0 r^2} = \dfrac{AR_1 + \sigma_0 R_2^2}{\varepsilon_0 r^2}$.
6. *Symétries.* Tous les plans contenant la droite $(OM)$ sont des plans de symétrie de la distribution : $\vec E = E(r, \theta, \varphi)\,\vec u_r$.

    *Invariances.* La distribution est invariante par toute rotation autour de $O$ : $E(r, \theta, \varphi) = E(r)$, donc $\vec E(M) = E(r)\,\vec u_r$.

    *Théorème de Gauss.* Surface de Gauss : sphère $S(r)$ de centre $O$ et de rayon $r$. Avec $d\vec S = r^2\sin\theta\, d\theta\, d\varphi\,\vec u_r$ :
$$\oiint_{S(r)} \vec E \cdot d\vec S = 4\pi r^2 E(r) = \frac{Q(r)}{\varepsilon_0} \quad\Longrightarrow\quad \vec E(M) = \frac{Q(r)}{4\pi\varepsilon_0 r^2}\vec u_r$$
    où $Q(r)$ est la charge intérieure à $S(r)$. Pour $0 < r \le R_1$ :
$$Q(r) = \int_0^r \frac{A}{r'^2}\, r'^2\, dr' \int_0^\pi \sin\theta\, d\theta \int_0^{2\pi} d\varphi = Ar \times 2 \times 2\pi = 4\pi A r$$
    d'où
$$\vec E(M) = \frac{A}{\varepsilon_0 r}\,\vec u_r \qquad (0 < r \le R_1)$$
    En $r = R_1$, on retrouve $\frac{AR_1}{\varepsilon_0 R_1^2}$ : le champ est continu (distribution volumique).
7. **D.** On intègre $E = -\dfrac{dV}{dr}$ de l'infini vers le centre, en imposant la continuité de $V$ aux surfaces $r = R_2$ et $r = R_1$ :
    - $r \ge R_2$ : $V(r) = \dfrac{AR_1 + \sigma_0 R_2^2}{\varepsilon_0 r}$ (nul à l'infini) ;
    - $R_1 \le r \le R_2$ : $V(r) = \dfrac{AR_1}{\varepsilon_0 r} + C_2$, et la continuité en $R_2$ donne $C_2 = \dfrac{\sigma_0 R_2}{\varepsilon_0}$ ;
    - $0 < r \le R_1$ : $V(r) = -\dfrac{A}{\varepsilon_0}\ln r + C_3$ ; en $R_1$, $V(R_1) = \dfrac{A}{\varepsilon_0} + \dfrac{\sigma_0 R_2}{\varepsilon_0}$, donc
$$V(r) = \frac{A}{\varepsilon_0}\ln\frac{R_1}{r} + \frac{A + \sigma_0 R_2}{\varepsilon_0}$$

## Exercice 2 : Condensateur cylindrique

**Énoncé.** (6 points) Un condensateur cylindrique à air est formé de deux armatures coaxiales de rayons $R_1 < R_2$. On note $Q_{\text{int}}$ la charge portée par la surface du cylindre intérieur, de rayon $R_1$ et de hauteur $h$. On suppose ce conducteur de longueur infinie ($h \gg R_2 > R_1$).

1. (Question 17, 1 point) Le champ $\vec E$ en un point $M$ à la distance $r$ de l'axe, avec $R_1 < r < R_2$, vaut : A) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 r^2}\vec u_r$ ; B) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 h r}\vec u_r$ ; C) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 r}\vec u_r$ ; D) aucune de ces réponses.
2. (Question 18, 2 points) La capacité $C$ de ce condensateur vaut : A) $\dfrac{2\pi\varepsilon_0 h}{\ln(R_1/R_2)}$ ; B) $\dfrac{2\pi\varepsilon_0 h}{R_2/R_1}$ ; C) $\dfrac{2\pi\varepsilon_0 h}{\ln(R_2/R_1)}$ ; D) aucune de ces réponses.
3. (Question 19 ♣, 2 points) Donner l'expression de cette capacité $C$, en détaillant.
4. (Question 20, 1 point) Pour $R_2 - R_1 = e \ll R_1$, la capacité se simplifie en : A) $\dfrac{2\pi\varepsilon_0 e h}{R_1}$ ; B) $\dfrac{2\pi\varepsilon_0 R_1 h}{e}$ ; C) $\dfrac{2\pi\varepsilon_0 R_1 e}{h}$ ; D) aucune de ces réponses.

**Correction.**

1. **B.** Par symétrie (plans contenant l'axe et plans perpendiculaires à l'axe) et invariance (rotation autour de l'axe et translation le long de l'axe), $\vec E = E(r)\,\vec u_r$. Le théorème de Gauss sur un cylindre coaxial de rayon $r$ et de hauteur $h$ donne $2\pi r h\, E(r) = \dfrac{Q_{\text{int}}}{\varepsilon_0}$, d'où $\vec E = \dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 h r}\vec u_r$. (Les réponses A et C ne sont pas homogènes à un champ.)
2. **C.** Voir la question 19. (La réponse A donnerait une capacité négative, puisque $\ln(R_1/R_2) < 0$.)
3. Entre les armatures, $\vec E = \dfrac{Q_1}{2\pi\varepsilon_0 h r}\vec u_r$ (avec $Q_1 = Q_{\text{int}}$). Comme $\vec E = -\overrightarrow{\operatorname{grad}}\, V$, on a $dV = -\vec E \cdot d\vec r = -E(r)\, dr$, soit
$$dV = -\frac{Q_1}{2\pi\varepsilon_0 h}\frac{dr}{r}$$
    On intègre de l'armature 2 ($r = R_2$) à l'armature 1 ($r = R_1$) :
$$V_1 - V_2 = -\frac{Q_1}{2\pi\varepsilon_0 h}\big[\ln r\big]_{R_2}^{R_1} = \frac{Q_1}{2\pi\varepsilon_0 h}\ln\frac{R_2}{R_1}$$
    Par définition $Q_1 = C(V_1 - V_2)$, donc
$$C = \frac{2\pi\varepsilon_0 h}{\ln(R_2/R_1)}$$
4. **B.** $\ln\dfrac{R_2}{R_1} = \ln\left(1 + \dfrac{e}{R_1}\right) \approx \dfrac{e}{R_1}$, donc $C \approx \dfrac{2\pi\varepsilon_0 R_1 h}{e}$. C'est la formule du condensateur plan $\varepsilon_0 S/e$ avec la surface $S = 2\pi R_1 h$ des armatures.

## Exercice 3 : Force de Lorentz

**Énoncé.** (5 points) Un proton ($q = 1{,}6 \times 10^{-19}\ \mathrm C$, $m = 1{,}67 \times 10^{-27}\ \mathrm{kg}$) se déplace dans un champ magnétique uniforme et constant $\vec B = B\,\vec u_x$, avec $B = 0{,}5\ \mathrm T$. À $t = 0$, sa vitesse a pour composantes $v_x = 1{,}5 \times 10^5\ \mathrm{m/s}$, $v_y = 0$, $v_z = 2{,}0 \times 10^5\ \mathrm{m/s}$, et sa position est $\vec r(0) = \vec 0$. Pour $t > 0$, la vitesse a trois composantes non nulles ; $\vec B$ est toujours uniforme, constant, orienté suivant $x$.

1. (Question 21, 1 point) Les équations différentielles du premier ordre régissant les composantes de la vitesse sont :
    A) $\dot v_x = 0$, $\dot v_y = +\dfrac{qB}{m}v_z$ et $\dot v_z = +\dfrac{qB}{m}v_x$ ;
    B) $\dot v_x = -\dfrac{qB}{m}v_y$, $\dot v_y = +\dfrac{qB}{m}v_x$ et $\dot v_z = 0$ ;
    C) $\dot v_x = +\dfrac{qB}{m}v_y$, $\dot v_y = -\dfrac{qB}{m}v_x$ et $\dot v_z = 0$ ;
    D) $\dot v_x = 0$, $\dot v_y = +\dfrac{qB}{m}v_z$ et $\dot v_z = -\dfrac{qB}{m}v_y$ ;
    E) aucune de ces réponses.
2. (Question 22 ♣, 2 points) Détailler les calculs donnant ces équations différentielles.
3. (Question 23, 2 points) Avec $\Omega = \dfrac{q}{m}B$, on trouve que la trajectoire du proton est une hélice d'axe la droite ($z = 0$ ; $y = R$), et :
    A) de rayon $R = \dfrac{v_z(0)}{2\pi\Omega}$ et de pas $p = \dfrac{2\pi v_z(0)}{\Omega}$ ;
    B) de rayon $R = \dfrac{v_z(0)}{\Omega}$ et de pas $p = v_z(0)\dfrac{2\pi}{\Omega}$ ;
    C) de rayon $R = v_z(0)\,\Omega$ et de pas $p = 2\pi\Omega\, v_z(0)$ ;
    D) de rayon $R = \dfrac{2\pi\Omega}{v_z(0)}$ et de pas $p = v_z(0)\dfrac{2\pi}{\Omega}$ ;
    E) aucune de ces réponses.

**Correction.**

1. **D.** Voir la question 22.
2. Deuxième loi de Newton (le poids est négligeable devant la force magnétique) : $m\dfrac{d\vec v}{dt} = q\,\vec v \wedge \vec B$, avec $\vec B = B\,\vec u_x$ :
$$\vec v \wedge \vec B = \begin{pmatrix} v_x \\ v_y \\ v_z \end{pmatrix} \wedge \begin{pmatrix} B \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} v_y \cdot 0 - v_z \cdot 0 \\ v_z B - v_x \cdot 0 \\ v_x \cdot 0 - v_y B \end{pmatrix} = \begin{pmatrix} 0 \\ v_z B \\ -v_y B \end{pmatrix}$$
    d'où
$$\dot v_x = 0, \qquad \dot v_y = \frac{qB}{m}v_z, \qquad \dot v_z = -\frac{qB}{m}v_y$$
    Donc $v_x = v_x(0)$ est constant, et en dérivant une seconde fois : $\ddot v_y = -\left(\frac{qB}{m}\right)^2 v_y$ et $\ddot v_z = -\left(\frac{qB}{m}\right)^2 v_z$ : $v_y$ et $v_z$ oscillent à la pulsation $\Omega = \frac{qB}{m}$.
3. **E** (la case cochée dans le corrigé est B, voir l'encadré).

    Avec $v_y(0) = 0$ et $v_z(0) = v_{z0}$, les solutions sont $v_y = v_{z0}\sin\Omega t$ et $v_z = v_{z0}\cos\Omega t$ (on vérifie : $\dot v_y = \Omega v_{z0}\cos\Omega t = \Omega v_z$ et $\dot v_z = -\Omega v_y$). En intégrant avec $\vec r(0) = \vec 0$ :
$$x = v_{x0}\, t, \qquad y = \frac{v_{z0}}{\Omega}\left(1 - \cos\Omega t\right), \qquad z = \frac{v_{z0}}{\Omega}\sin\Omega t$$
    Donc $(y - R)^2 + z^2 = R^2$ avec $R = \dfrac{v_{z0}}{\Omega}$ : dans le plan $(y, z)$ le proton décrit un cercle de centre $(y = R, z = 0)$, pendant qu'il avance uniformément selon $x$. C'est une hélice d'axe ($z = 0$ ; $y = R$), de rayon $R = \dfrac{v_z(0)}{\Omega}$, et de **pas** égal à la distance parcourue selon $x$ pendant une période $T = \dfrac{2\pi}{\Omega}$ :
$$p = v_x(0)\,\frac{2\pi}{\Omega}$$

    Applications numériques : $\Omega = \dfrac{1{,}6 \times 10^{-19} \times 0{,}5}{1{,}67 \times 10^{-27}} \approx 4{,}8 \times 10^7\ \mathrm{rad/s}$, $R = \dfrac{2{,}0 \times 10^5}{4{,}8 \times 10^7} \approx 4{,}2\ \mathrm{mm}$ et $p = \dfrac{2\pi \times 1{,}5 \times 10^5}{4{,}8 \times 10^7} \approx 2{,}0\ \mathrm{cm}$.

> **Erreur corrigée :** le corrigé coche la réponse B, dont le rayon est juste mais dont le pas, $v_z(0)\frac{2\pi}{\Omega}$, utilise la mauvaise composante de la vitesse : le pas d'une hélice est l'avancée **le long du champ** $\vec B = B\,\vec u_x$ pendant un tour, soit $p = v_x(0)\frac{2\pi}{\Omega} \approx 2{,}0\ \mathrm{cm}$ (et non $v_z(0)\frac{2\pi}{\Omega} \approx 2{,}6\ \mathrm{cm}$). Aucune des propositions n'est donc exacte.
