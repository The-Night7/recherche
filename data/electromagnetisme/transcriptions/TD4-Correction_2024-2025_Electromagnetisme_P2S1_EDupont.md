---
source: TD4-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 6 (correction manuscrite)
transcription: manuelle
---

# TD4 — Conducteurs à l'équilibre électrostatique (corrigé)

> **Note :** mêmes calculs que la correction 2022-2023, avec une numérotation différente (les exercices 3, 4 et 2 de 2022-2023 sont devenus 2, 3 et 4). L'application numérique du condensateur cylindrique, fausse en 2022-2023, est juste ici.

## Exercice 1 : Conducteur creux

**Énoncé.** Soit $A$ un conducteur creux. On place en son sein un second conducteur noté $B$ portant une charge $+Q$.

1. Retrouver le fait que $Q_{A,\text{int}} = -Q_B = -Q$ en utilisant le théorème de Gauss. On note $Q_{A,\text{int}}$ la charge surfacique présente au niveau de la surface intérieure de $A$.
2. Calculer la charge extérieure $Q_{A,\text{ext}}$ (c'est-à-dire la charge surfacique présente au niveau de la surface extérieure de $A$) dans les cas suivants :
    a) $A$ est isolé et initialement neutre ;
    b) $A$ porte une charge initiale $q$.

> **Note :** la figure montre le conducteur creux $A$ (couronne grisée), le conducteur $B$ (charge $+Q = Q_B$) dans la cavité vide, et la surface de Gauss $\Sigma$ (en pointillés) tracée **dans la matière** de $A$, où $\vec E = \vec 0$.

**Correction.**

**1.** On choisit comme surface de Gauss une surface fermée $\Sigma$ située entièrement dans le conducteur $A$ et entourant la cavité. Théorème de Gauss :
$$\Phi(\vec E) = \oint_\Sigma \vec E \cdot d\vec S = \frac{q_{\text{int}}}{\varepsilon_0}$$

Or, dans un conducteur à l'équilibre électrostatique, le champ est nul à l'intérieur de la matière : $\vec E = \vec 0$ en tout point de $\Sigma$. Donc $\Phi(\vec E) = 0$ et $q_{\text{int}} = 0$. La charge intérieure à $\Sigma$ est celle de $B$ plus celle portée par la surface intérieure de $A$ :
$$q_{\text{int}} = Q_{A,\text{int}} + Q_B = 0 \quad \Longrightarrow \quad Q_{A,\text{int}} = -Q_B = -Q$$

**2.** La charge totale de $A$ se répartit entre ses deux surfaces : $Q_A = Q_{A,\text{int}} + Q_{A,\text{ext}}$.

- a) $A$ isolé et initialement neutre : sa charge totale reste nulle, $Q_A = 0$, donc
$$Q_{A,\text{ext}} = 0 - Q_{A,\text{int}} = +Q$$
- b) $A$ porte la charge $q$ : $Q_A = q$, donc
$$Q_{A,\text{ext}} = q - Q_{A,\text{int}} = q + Q$$

## Exercice 2 : Condensateur plan

**Énoncé.** Un condensateur plan, placé dans le vide ($\varepsilon_0$), est constitué de deux armatures conductrices planes de surface $S$, parallèles entre elles, et séparées d'une distance $e$ l'une de l'autre. Dans cette étude, on se place dans l'approximation d'un condensateur plan infini.

1. En utilisant le théorème de Gauss, déterminer le champ électrostatique $\vec E$ créé par un plan infini chargé avec une densité de charge surfacique uniforme ($+\sigma$).
2. Déduire le champ entre les deux armatures du condensateur en fonction de la charge surfacique ($+\sigma$) puis en fonction de la charge totale ($+Q$) portée par l'armature n° 1.
3. En déduire la différence de potentiel $\Delta V = V_1 - V_2$ entre les armatures n° 1 et n° 2, puis la capacité $C$ du condensateur en fonction de $S$, $e$ et $\varepsilon_0$.
4. Application numérique : pendant un orage, la surface de la Terre et la surface inférieure des nuages forment, avec une assez bonne approximation, un condensateur plan. On suppose que le nuage se trouve à $1000$ mètres d'altitude et qu'il couvre une surface d'environ $20\ \mathrm{km^2}$. Quelle est la valeur de la capacité du condensateur formé par le système « Terre − Nuage » ? Donnée : $\varepsilon_0 = 8{,}85 \times 10^{-12}$ SI.

> **Note :** la figure montre les deux armatures horizontales : l'armature n° 1 (charge $+Q$) en haut, à la cote $z = e$, et l'armature n° 2 (charge $-Q$) en bas, en $z = 0$ (origine choisie sur la plaque du bas).

**Correction.** On note $\Delta V = V_1 - V_2$ la tension entre l'armature n° 1 (charge $+Q$) et l'armature n° 2, de sorte que $Q = C\,\Delta V$ avec $C > 0$.

> **Note :** la correction manuscrite écrit au début de cette partie « $Q = CU$, $U = V_2 - V_1$ », puis utilise $\Delta V = V_1 - V_2$ ; c'est cette seconde convention (tension de l'armature positive par rapport à l'armature négative) qui donne $C > 0$.

**1.** (Voir TD2, exercices 4 et 8.) La densité est surfacique : $\vec E$ est défini et continu partout sauf à la traversée du plan, où $\vec E(0^+) - \vec E(0^-) = \frac{\sigma}{\varepsilon_0}\vec e_z$. En coordonnées cylindriques d'axe $(Oz)$ perpendiculaire au plan $\Pi$ :

- *invariances :* rotation autour de $(Oz)$ et translation selon $\vec e_r$, donc $\vec E = \vec E(z)$ ;
- *symétries :* $P_1 = (M, \vec e_r, \vec e_z)$ et $P_2 = (M, \vec e_\theta, \vec e_z)$ sont plans de symétrie, donc $\vec E = E(z)\,\vec e_z$ ; le plan chargé $\Pi$ est lui aussi un plan de **symétrie** de la distribution, donc $E(z < 0) = -E(z > 0)$.

> **Erreur corrigée :** la correction manuscrite écrit $\vec E \in P_1 \cup P_2$ ; le champ appartient aux deux plans, donc à leur intersection $P_1 \cap P_2$, de direction $\vec e_z$.

*Théorème de Gauss* avec un cylindre $S_G$ de section $S$ symétrique par rapport au plan (bases $S_1$ et $S_2$ de normales $\vec n_1 = \vec e_z$ et $\vec n_2 = -\vec n_1$, surface latérale $S_3$ de normale $\vec n_3 \perp \vec e_z$) :
$$\Phi = \iint_{S_1} \vec E \cdot \vec n_1\,dS + \iint_{S_2} \vec E \cdot \vec n_2\,dS + \iint_{S_3} \vec E \cdot \vec n_3\,dS = E(z)\,S + E(z)\,S + 0 = 2\,E(z > 0)\,S$$

avec $q_{\text{int}} = \sigma S$ :
$$2S\,E(z > 0) = \frac{\sigma S}{\varepsilon_0} \quad \Longrightarrow \quad E(z > 0) = \frac{\sigma}{2\varepsilon_0}, \qquad E(z < 0) = -\frac{\sigma}{2\varepsilon_0}$$

**2.** L'armature n° 1 ($z = e$) porte $+Q = +\sigma S$, l'armature n° 2 ($z = 0$) porte $-Q = -\sigma S$. Par superposition des champs de deux plans infinis :

- l'armature 1 crée $+\frac{\sigma}{2\varepsilon_0}\vec e_z$ au-dessus d'elle et $-\frac{\sigma}{2\varepsilon_0}\vec e_z$ en dessous ;
- l'armature 2 (densité $-\sigma$) crée $-\frac{\sigma}{2\varepsilon_0}\vec e_z$ au-dessus d'elle et $+\frac{\sigma}{2\varepsilon_0}\vec e_z$ en dessous.

Donc :

- entre les armatures ($0 < z < e$) : $\vec E = -\dfrac{\sigma}{2\varepsilon_0} \times 2\,\vec e_z = -\dfrac{\sigma}{\varepsilon_0}\vec e_z$ ;
- pour $z > e$ : $\vec E = +\frac{\sigma}{2\varepsilon_0}\vec e_z - \frac{\sigma}{2\varepsilon_0}\vec e_z = \vec 0$ ; de même pour $z < 0$ : le champ est nul à l'extérieur.

Avec $Q = \sigma S$ :
$$\vec E(0 < z < e) = -\frac{\sigma}{\varepsilon_0}\vec e_z = -\frac{Q}{\varepsilon_0 S}\vec e_z$$

Le champ est dirigé de l'armature positive vers l'armature négative.

**3.** $\vec E = E(z)\,\vec e_z = -\overrightarrow{\operatorname{grad}} V = -\dfrac{dV}{dz}\vec e_z$, donc entre les armatures $\dfrac{dV}{dz} = \dfrac{\sigma}{\varepsilon_0}$ (constante). En intégrant de $z = 0$ ($V = V_2$) à $z = e$ ($V = V_1$) :
$$\Delta V = V_1 - V_2 = \int_0^e \frac{\sigma}{\varepsilon_0}dz = \frac{\sigma e}{\varepsilon_0} = Q\,\frac{e}{\varepsilon_0 S}$$

La capacité est définie par $Q = C\,\Delta V$, d'où
$$C = \frac{\varepsilon_0 S}{e}$$

Analyse dimensionnelle : $[\Delta V] = \frac{[q]}{[\varepsilon_0]L} = \frac{[q]}{[C]}$, donc $[C] = [\varepsilon_0]\,L$.

**4.** $e = 10^3\ \mathrm{m}$ et $S = 20\ \mathrm{km^2} = 20 \times (10^3)^2\ \mathrm{m^2} = 2 \times 10^7\ \mathrm{m^2}$ :
$$C = \frac{\varepsilon_0 S}{e} = \frac{8{,}85 \times 10^{-12} \times 2 \times 10^7}{10^3} = 1{,}77 \times 10^{-7}\ \mathrm{F} \approx 177\ \mathrm{nF}$$

## Exercice 3 : Condensateur cylindrique

**Énoncé.** Un condensateur cylindrique à air est formé de deux armatures coaxiales, de rayons notés $R_1$ et $R_2$ avec $R_1 < R_2$. Ces deux cylindres infinis coaxiaux sont uniformément chargés en surface avec une charge $Q_1$ et $Q_2$ respectivement, telles que $Q_1 = -Q_2 = Q$.

1. On suppose ici que ce conducteur est de longueur infinie. Déterminer $\vec E$ en un point $M$ situé à la distance $r$ de l'axe, avec $R_1 < r < R_2$.
2. En déduire l'expression de la capacité $C$ de ce condensateur. A.N. : $R_2 = 20\ \mathrm{cm}$, $R_1 = 10\ \mathrm{cm}$ et $h = 50\ \mathrm{cm}$.
3. Que devient l'expression de la capacité $C$ lorsque les rayons sont voisins, c'est-à-dire $R_2 - R_1 = e \ll R_1$ ?

> **Note :** la figure montre les deux cylindres coaxiaux d'axe $(Oz)$ et de hauteur $h$ : l'armature intérieure de rayon $R_1$ (potentiel $V_1$, charge $Q$) et l'armature extérieure de rayon $R_2$ (potentiel $V_2$), avec un cylindre de Gauss de rayon $r$ et de hauteur $H$ entre les deux.

**Correction.**

**1.** Par les mêmes invariances et symétries que pour un cylindre chargé (TD2), $\vec E = E(r)\,\vec e_r$ est radial. Surface de Gauss $\Sigma_G$ : cylindre de même axe, de rayon $r$ ($R_1 < r < R_2$) et de hauteur $H$. Le flux à travers les bases est nul, et sur la surface latérale $dS_r = r\,d\theta\,dz$ :
$$\Phi(\vec E) = \int_0^{2\pi}\int_0^H E(r)\,r\,d\theta\,dz = 2\pi r H\,E(r) = \frac{Q_{\text{int}}}{\varepsilon_0}$$

$$\vec E(r) = \frac{Q_{\text{int}}}{2\pi\varepsilon_0 H r}\,\vec e_r$$

où $Q_{\text{int}}$ est la charge portée par la hauteur $H$ de l'armature intérieure (l'armature extérieure est à l'extérieur de $\Sigma_G$).

**2.** On prend $H = h$ : $Q_{\text{int}} = Q$, charge de l'armature intérieure. Alors
$$\vec E = -\overrightarrow{\operatorname{grad}} V = -\frac{dV}{dr}\vec e_r = \frac{Q}{2\pi\varepsilon_0 h r}\vec e_r$$

En intégrant, $V(r) = -\dfrac{Q}{2\pi\varepsilon_0 h}\ln r + \text{cte}$, d'où
$$\Delta V = V(R_1) - V(R_2) = -\int_{R_2}^{R_1} \frac{Q}{2\pi\varepsilon_0 h}\frac{dr}{r} = \frac{Q}{2\pi\varepsilon_0 h}\ln\frac{R_2}{R_1}$$

Par définition $Q = C\,\Delta V$, donc
$$C = \frac{2\pi\varepsilon_0 h}{\ln(R_2/R_1)}$$

(on vérifie $[C] = [\varepsilon_0]\,L$, comme pour $\varepsilon_0 S/e$).

*Application numérique :*
$$C = \frac{2\pi \times 8{,}85 \times 10^{-12} \times 0{,}5}{\ln 2} = \frac{2{,}78 \times 10^{-11}}{0{,}693} \approx 4{,}0 \times 10^{-11}\ \mathrm{F} = 40\ \mathrm{pF}$$

**3.** $R_2 = R_1 + e$, donc $\dfrac{R_2}{R_1} = 1 + \dfrac{e}{R_1}$ avec $\dfrac{e}{R_1} \ll 1$. À l'ordre 1, $\ln\big(1 + \frac{e}{R_1}\big) \approx \frac{e}{R_1}$ :
$$C \approx \frac{2\pi\varepsilon_0 h R_1}{e} = \frac{\varepsilon_0 S_1}{e}$$

où $S_1 = 2\pi R_1 h$ est la surface latérale de l'armature intérieure : on retrouve la capacité d'un condensateur plan de surface $S_1$ et d'épaisseur $e$, ce qui est logique puisque les armatures sont alors très proches l'une de l'autre.

## Exercice 4 : Deux boules conductrices reliées par un fil

**Énoncé.** (*) On considère deux boules conductrices de rayons $R_1$ et $R_2$ dont les centres sont à une distance $d$ grande devant $R_1$ et $R_2$. Elles portent les charges respectives $Q_1$ et $Q_2$, distribuées uniformément.

1. Calculer les potentiels $V_1$ et $V_2$ de chacune des boules, en leur centre.
2. On relie les boules par un fil conducteur. Calculer les charges $Q_1'$ et $Q_2'$, ainsi que les potentiels notés $V_1'$ et $V_2'$.
3. En déduire la capacité de ce conducteur constitué des deux boules reliées par le fil conducteur.

**Correction.** Les boules sont conductrices : à l'équilibre, leurs charges se répartissent sur leur surface (des « sphères pleines » chargées en surface). On rappelle qu'une charge $q$ placée en $P$ crée en $M$ le potentiel $V(M) = \dfrac{q}{4\pi\varepsilon_0 PM}$ (nul à l'infini).

**1.** Pour la première sphère conductrice, les charges $Q_1$ sont réparties en surface, toutes à la distance $R_1$ du centre $O_1$. Elles créent en $O_1$ le potentiel
$$V_1^{(a)} = \frac{Q_1}{4\pi\varepsilon_0 R_1}$$

Les charges $Q_2$ de la deuxième sphère sont toutes à une distance de $O_1$ égale à $d$ à des termes près en $R_2$, négligeables puisque $d \gg R_2$. Elles créent en $O_1$
$$V_1^{(b)} = \frac{Q_2}{4\pi\varepsilon_0 d}$$

D'où, en échangeant les rôles de 1 et 2 pour $V_2$ :
$$V_1 = \frac{1}{4\pi\varepsilon_0}\Big(\frac{Q_1}{R_1} + \frac{Q_2}{d}\Big), \qquad V_2 = \frac{1}{4\pi\varepsilon_0}\Big(\frac{Q_2}{R_2} + \frac{Q_1}{d}\Big)$$

(chaque sphère étant un conducteur à l'équilibre, ce potentiel est aussi celui de toute la sphère).

**2.** En reliant les sphères par un fil conducteur, on permet l'écoulement des charges d'une sphère à l'autre, jusqu'à ce que l'ensemble forme un seul conducteur à l'équilibre, donc au même potentiel :
> **Erreur corrigée :** la correction manuscrite écrit « $V' = V_1' + V_2'$ » : c'est une coquille pour $V' = V_1' = V_2'$ (égalité des potentiels), comme l'utilise la suite du calcul.

$$(1) \quad V' = V_1' = V_2' \qquad\qquad (2) \quad Q_1 + Q_2 = Q_1' + Q_2' \ \text{(conservation de la charge)}$$

La condition (1) s'écrit
$$\frac{Q_1'}{R_1} + \frac{Q_2'}{d} = \frac{Q_2'}{R_2} + \frac{Q_1'}{d} \quad \Longleftrightarrow \quad Q_1'\Big(\frac{1}{R_1} - \frac{1}{d}\Big) = Q_2'\Big(\frac{1}{R_2} - \frac{1}{d}\Big)$$

En reportant dans (2) :
$$Q_1'\left[1 + \frac{1/R_1 - 1/d}{1/R_2 - 1/d}\right] = Q_1 + Q_2$$

$$Q_1' = (Q_1 + Q_2)\,\frac{1/R_2 - 1/d}{1/R_1 + 1/R_2 - 2/d}, \qquad Q_2' = (Q_1 + Q_2)\,\frac{1/R_1 - 1/d}{1/R_1 + 1/R_2 - 2/d}$$

Potentiel commun :
$$V' = \frac{1}{4\pi\varepsilon_0}\Big(\frac{Q_1'}{R_1} + \frac{Q_2'}{d}\Big) = \frac{Q_1 + Q_2}{4\pi\varepsilon_0} \cdot \frac{\frac{1}{R_1 R_2} - \frac{1}{R_1 d} + \frac{1}{R_1 d} - \frac{1}{d^2}}{\frac{1}{R_1} + \frac{1}{R_2} - \frac{2}{d}}$$

En multipliant numérateur et dénominateur par $R_1 R_2$ :
$$V' = \frac{Q_1 + Q_2}{4\pi\varepsilon_0} \cdot \frac{1 - \frac{R_1 R_2}{d^2}}{R_1 + R_2 - \frac{2R_1 R_2}{d}}$$

Comme $d \gg R_1, R_2$, le terme $\frac{R_1 R_2}{d^2}$ est du second ordre et négligeable devant $1$ ; on ne conserve que les termes du premier ordre en $R_{1,2}/d$ :
$$V' = V_1' = V_2' = \frac{Q_1 + Q_2}{4\pi\varepsilon_0} \cdot \frac{1}{R_1 + R_2 - \frac{2R_1 R_2}{d}}$$

(Analyse dimensionnelle : le crochet est l'inverse d'une longueur, et $[V'] = \frac{[q]}{[\varepsilon_0]}L^{-1}$.)

À l'ordre le plus bas, $\frac{Q_1'}{Q_2'} \approx \frac{R_1}{R_2}$ : la plus grosse sphère porte la plus grande charge.

**3.** Le conducteur formé par les deux sphères et le fil porte la charge $Q = Q_1 + Q_2 = Q_1' + Q_2'$ et se trouve au potentiel $V'$ (par rapport à l'infini). Sa capacité est définie par la relation linéaire $Q = C\,V'$ (comme pour un condensateur, $Q = C\,\Delta V$). D'après la question 2, $V' = \dfrac{Q}{4\pi\varepsilon_0}\cdot\dfrac{1}{R_1 + R_2 - 2R_1 R_2/d}$, donc
$$C = 4\pi\varepsilon_0\Big(R_1 + R_2 - \frac{2R_1 R_2}{d}\Big)$$

C'est un peu moins que la somme $4\pi\varepsilon_0(R_1 + R_2)$ des capacités des deux sphères isolées, et $C$ augmente avec $d$ (l'influence mutuelle diminue). Dimension : $[C] = [\varepsilon_0]\,L$, comme pour le condensateur plan $C = \varepsilon_0 S/e$ de l'exercice 2.
