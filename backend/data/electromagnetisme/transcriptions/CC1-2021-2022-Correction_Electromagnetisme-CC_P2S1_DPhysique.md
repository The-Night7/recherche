---
source: CC1-2021-2022-Correction_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 7 (page 8 blanche)
transcription: manuelle
---

# CC1 d'Électromagnétisme — 28 octobre 2021 (corrigé)

> **Note :** contrôle d'une heure, sans document ni calculatrice. Les questions à choix multiples n'ont qu'une seule bonne réponse, sans point négatif. La correction d'origine consiste en cases noircies et en réponses manuscrites ; elle est retranscrite et justifiée ici.

## Questions de cours : loi de Coulomb et champ électrostatique

**Énoncé.** (7 points) Pour chaque question, choisir l'unique bonne réponse.

> **Note :** trois figures de cours accompagnent ces questions : (1) deux charges $q_1$ en $M_1$ et $q_2$ en $M_2$, avec le vecteur unitaire $\vec u_{1\to2}$ dirigé de $M_1$ vers $M_2$ et la force $\vec F_{1/2}$ appliquée en $M_2$ ; (2) un volume $V$ chargé, un point courant $P$ repéré par $\vec{r}\,{}'$, un point $M$ repéré par $\vec r$, à la distance $\|\vec r - \vec{r}\,{}'\|$ de $P$ ; (3) la charge $dq = \rho\, dV$ en $P$ crée en $M$ le champ $d\vec E$ dirigé de $P$ vers $M$.

1. (Q.1) En s'aidant de la figure sur la loi de Coulomb, donner l'expression de la force $\vec F_{1/2}$ exercée par la charge ponctuelle $q_1$ sur la charge ponctuelle $q_2$, située à la distance $r_{12}$ :
    a) aucune de ces réponses n'est correcte ;
    b) $\vec F_{2/1} = k \left(\dfrac{q_1 q_2}{r_{12}^2}\right) \vec u_{1\to2}$ ;
    c) $\vec F_{1/2} = k \left(\dfrac{q_1 q_2}{r_{12}^3}\right) \vec u_{1\to2}$ ;
    d) $\vec F_{1/2} = k \left(\dfrac{q_1 q_2}{r_{12}^2}\right) \vec u_{1\to2}$.
2. (Q.2) Un volume $V$ porte une distribution volumique de charges de densité $\rho$. La charge totale $Q$ vaut : a) $Q = \iint_S \rho\, dV$ ; b) $Q = \iint_V \rho\, dV$ ; c) $Q = \iiint_V \rho\, dV$.
3. (Q.3) Le volume élémentaire en coordonnées sphériques s'écrit : a) $dV = r \sin\theta\, dr\, d\theta\, d\varphi$ ; b) $dV = r^2\, dr\, d\theta\, d\varphi$ ; c) $dV = r^2 \sin\theta\, dr\, d\theta\, d\varphi$.
4. (Q.4) Pour une distribution surfacique de densité $\sigma$ uniforme et constante, la charge totale d'une surface d'aire $S$ est : a) $Q = \rho S$ ; b) $Q = \sigma V$ ; c) $Q = \sigma S$.
5. (Q.5) Le facteur $k$ de la loi de Coulomb dépend du milieu. Dans le vide, il vaut : a) $k = 1/(4\pi\varepsilon_0)$ ; b) $k = 1/(4\pi\varepsilon)$ ; c) $k = 1/(\pi\varepsilon_0)$.
6. (Q.6) En étudiant les plans de symétrie de la distribution de charges, on trouve que :
    a) la direction du champ $\vec E$ en $M$ est celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    b) la direction de $\vec E$ en $M$ est celle de la droite intersection d'au moins deux plans d'antisymétrie passant par $M$ ;
    c) le champ $\vec E$ en $M$ est contenu dans tout plan $\Pi$ de symétrie passant par $M$.
7. (Q.7) Une particule ponctuelle de charge $q'$, en un point $M$, est soumise à une force $\vec F$ (autre que son poids, et nulle si $q' = 0$). Le champ électrostatique en $M$ vérifie : a) $\vec F = q\vec E$ ; b) $\vec F = q'\vec E$ ; c) $\vec F = \vec E / q'$.
8. (Q.8) Le champ électrostatique créé par une distribution volumique de charges peut s'écrire :
    a) $\vec E(M) = \displaystyle\iiint_{P \in V} \frac{\rho\, dV}{4\pi\varepsilon_0 r^2}\, \vec u$ ;
    b) $\vec E(M) = \displaystyle\iiint_{M \in V} \frac{\rho\, dV}{4\pi\varepsilon_0 r^2}\, \vec u$ ;
    c) $\vec E(M) = \displaystyle\iiint_{P \in V} \frac{\rho\, dV}{4\pi\varepsilon_0 r^3}\, \vec u$.
9. (Q.9) Soient les charges $q'$ en $M$ et $q$ en $P$. Le champ électrostatique en $M$ s'écrit : a) $\vec E = \dfrac{1}{4\pi\varepsilon_0} \dfrac{q'}{PM^3} \overrightarrow{PM}$ ; b) $\vec E = \dfrac{1}{4\pi\varepsilon_0} \dfrac{q}{PM^3} \overrightarrow{PM}$ ; c) $\vec E = \dfrac{1}{4\pi\varepsilon_0} \dfrac{q}{PM^2} \overrightarrow{PM}$.
10. (Q.10) À partir du schéma correspondant, le champ créé par une distribution quelconque de charges s'écrit :
    a) $\vec E(M) = \dfrac{1}{4\pi\varepsilon_0} \displaystyle\iiint_{P \in V} \frac{\vec r - \vec{r}\,{}'}{\|\vec r - \vec{r}\,{}'\|^2} \rho(\vec{r}\,{}')\, dV$ ;
    b) $\vec E(M) = \dfrac{1}{4\pi\varepsilon_0} \displaystyle\iiint_{P \in V} \frac{\vec r - \vec{r}\,{}'}{\|\vec r - \vec{r}\,{}'\|^3} \rho(\vec{r}\,{}')\, dV$ ;
    c) $\vec E(M) = \dfrac{1}{4\pi\varepsilon_0} \displaystyle\iiint_{P \in V} \frac{\vec r - \vec{r}\,{}'}{\|\vec r - \vec{r}\,{}'\|^3} \rho(\vec r)\, dV$.

**Correction.**

1. **Réponse d).** La force exercée par $q_1$ sur $q_2$ est portée par $\vec u_{1\to2}$ (de $q_1$ vers $q_2$) et varie en $1/r_{12}^2$ : $\vec F_{1/2} = \dfrac{q_1 q_2}{4\pi\varepsilon_0 r_{12}^2}\, \vec u_{1\to2}$. Elle est répulsive si $q_1 q_2 > 0$. La réponse c) n'est pas homogène (avec un vecteur unitaire, il faut $r^2$ au dénominateur) et b) désigne l'autre force.
2. **Réponse c).** Une charge volumique s'intègre sur le volume : $Q = \iiint_V \rho\, dV$ (intégrale triple).
3. **Réponse c).** $dV = dr \times r\, d\theta \times r\sin\theta\, d\varphi = r^2 \sin\theta\, dr\, d\theta\, d\varphi$.
4. **Réponse c).** Pour $\sigma$ uniforme, $Q = \iint_S \sigma\, dS = \sigma S$.
5. **Réponse a).** $k = \dfrac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9\ \mathrm{N\,m^2\,C^{-2}}$.
6. **Réponse c).** Principe de Curie : en un point $M$ d'un plan de symétrie de la distribution, $\vec E(M)$ est contenu dans ce plan. (En un point d'un plan d'antisymétrie, $\vec E$ est au contraire orthogonal au plan ; les propositions a) et b) inversent ces deux règles.)
7. **Réponse b).** Par définition du champ, $\vec F = q'\vec E(M)$, où $q'$ est la charge placée en $M$.
8. **Réponse a).** On somme les contributions $d\vec E = \dfrac{\rho\, dV}{4\pi\varepsilon_0 r^2} \vec u$ des charges $dq = \rho\, dV$ situées aux points $P$ **de la distribution** ($P \in V$), avec $r = PM$ et $\vec u$ unitaire de $P$ vers $M$.
9. **Réponse b).** Le champ en $M$ est créé par la charge **source** $q$ placée en $P$ : $\vec E = \dfrac{q}{4\pi\varepsilon_0 PM^2}\dfrac{\overrightarrow{PM}}{PM} = \dfrac{q}{4\pi\varepsilon_0 PM^3}\overrightarrow{PM}$.
10. **Réponse b).** C'est la même formule qu'en 9, avec $\overrightarrow{PM} = \vec r - \vec{r}\,{}'$ et $dq = \rho(\vec{r}\,{}')\, dV$ : la densité est évaluée au point source $P$, pas en $M$.

## Exercice 1 : Quatre charges aux sommets d'un carré

**Énoncé.** (7 points) Quatre charges ponctuelles $q_A$, $q_B$, $q_C$ et $q_D$ sont placées aux sommets $A$, $B$, $C$, $D$ d'un carré $ABCD$ de centre $O$, de côté $2a$, contenu dans le plan $(Oxz)$. On s'intéresse à une charge $Q$ placée en un point $M$ quelconque de l'axe $(Oy)$.

> **Note :** d'après la figure (et les coordonnées de la correction), $A = (a, 0, a)$, $B = (a, 0, -a)$, $C = (-a, 0, -a)$ et $D = (-a, 0, a)$ ; $M = (0, y, 0)$.

1. (Q.11, 1 point) Donner l'expression littérale de la force totale $\vec F_{/Q}$ exercée sur $Q$ par les charges $q_A$, $q_B$, $q_C$ et $q_D$. On notera $k = \frac{1}{4\pi\varepsilon_0}$.
2. (Q.12, 2 points) Donner les vecteurs $\overrightarrow{AM}$, $\overrightarrow{BM}$, $\overrightarrow{CM}$ et $\overrightarrow{DM}$ dans le repère $(O ; \vec u_x, \vec u_y, \vec u_z)$.
3. (Q.13, 2 points) La norme commune de ces vecteurs vaut : a) $\sqrt{2a^2 - y^2}$ ; b) $\sqrt{4a^2 + y^2}$ ; c) $\sqrt{a^2 + y^2}$ ; d) $\sqrt{2a^2 + y^2}$ ; e) aucune de ces réponses.
4. (Q.14, 2 points) Les charges valent $q_A = q_C = +q$ et $q_B = q_D = -q$. Montrer que la force subie par $Q$ est nulle.

**Correction.**

1. Par superposition, $\vec F_{/Q} = \vec F_{q_A \to Q} + \vec F_{q_B \to Q} + \vec F_{q_C \to Q} + \vec F_{q_D \to Q}$, avec $\vec F_{q_i \to Q} = k\dfrac{q_i Q}{r^3}\overrightarrow{P_iM}$. Les quatre sommets sont à la même distance $r = AM = BM = CM = DM$ de $M$, d'où
$$\vec F_{/Q} = \frac{kQ}{r^3}\left[q_A \overrightarrow{AM} + q_B \overrightarrow{BM} + q_C \overrightarrow{CM} + q_D \overrightarrow{DM}\right]$$

2. Avec $\overrightarrow{P_iM} = \overrightarrow{OM} - \overrightarrow{OP_i}$ :
$$\overrightarrow{AM} = \begin{pmatrix} -a \\ y \\ -a \end{pmatrix},\quad \overrightarrow{BM} = \begin{pmatrix} -a \\ y \\ a \end{pmatrix},\quad \overrightarrow{CM} = \begin{pmatrix} a \\ y \\ a \end{pmatrix},\quad \overrightarrow{DM} = \begin{pmatrix} a \\ y \\ -a \end{pmatrix}$$

3. **Réponse d).** $\|\overrightarrow{AM}\| = \sqrt{a^2 + y^2 + a^2} = \sqrt{2a^2 + y^2}$, et de même pour les trois autres. Vérification : en $y = 0$, on retrouve la demi-diagonale du carré, $a\sqrt 2$.

4. Avec les charges données :
$$\vec F_{/Q} = \frac{kQq}{r^3}\left[\overrightarrow{AM} - \overrightarrow{BM} + \overrightarrow{CM} - \overrightarrow{DM}\right]$$
Composante par composante : sur $x$, $-a + a + a - a = 0$ ; sur $y$, $y - y + y - y = 0$ ; sur $z$, $-a - a + a + a = 0$. Donc $\vec F_{/Q} = \vec 0$ pour tout $M$ de l'axe $(Oy)$.

Interprétation : le plan $(Oyz)$ ($x \to -x$) échange $A \leftrightarrow D$ et $B \leftrightarrow C$, donc des charges opposées : c'est un plan d'antisymétrie, et le champ en $M$ (qui appartient à ce plan) lui est orthogonal, donc porté par $\vec u_x$. De même, $(Oxy)$ ($z \to -z$) échange $A \leftrightarrow B$ et $C \leftrightarrow D$ : c'est aussi un plan d'antisymétrie, et le champ doit être porté par $\vec u_z$. Un vecteur à la fois colinéaire à $\vec u_x$ et à $\vec u_z$ est nul.

> **Note :** le barème accordait les 2 points à une démonstration par le calcul ou par un schéma montrant les quatre forces $\vec F_{q_i \to Q}$.

## Exercice 2 : Symétrie et antisymétrie du champ électrique

**Énoncé.** (6 points)

> **Note :** figure a : quatre charges aux sommets d'un carré centré en $O$ dans le plan $(Oxy)$ : $+q$ en haut à gauche $(-a, a)$, $-q$ en haut à droite $(a, a)$, $-q$ en bas à gauche $(-a, -a)$, $+q$ en bas à droite $(a, -a)$ ; les diagonales du carré sont tracées. Figure b : un cercle de centre $O$ dans le plan $(Oxy)$, dont la moitié gauche ($x < 0$) porte la densité linéique $-\lambda$ et la moitié droite ($x > 0$) la densité $+\lambda$ ; l'axe $Oz$ sort du plan.

1. (Q.15) Sur la figure a, les plans de symétrie sont : a) $(Oyz)$, $y = x$ et $y = -x$ ; b) $(Oyz)$ et $(Oxz)$ ; c) $(Oxy)$, $y = x$ et $y = -x$ ; d) $(Oxy)$ et $(Oxz)$ ; e) aucune de ces réponses.
2. (Q.16) Sur la figure a, les plans d'antisymétrie sont : a) $(Oxy)$ et $(Oxz)$ ; b) $(Oxy)$, $y = x$ et $y = -x$ ; c) aucune de ces réponses ; d) $(Oyz)$ et $(Oxz)$ ; e) $(Oyz)$, $y = x$ et $y = -x$.
3. (Q.17) Sur la figure b, les plans de symétrie sont : a) $(Oxy)$, $(Oyz)$ et $(Oxz)$ ; b) le plan $(Oyz)$ ; c) aucune de ces réponses ; d) $(Oxy)$ et $(Oxz)$.
4. (Q.18) Sur la figure b, les plans d'antisymétrie sont : a) aucune de ces réponses ; b) $(Oxy)$ et $(Oxz)$ ; c) $(Oxy)$, $(Oyz)$ et $(Oxz)$ ; d) le plan $(Oyz)$.
5. (Q.19, 2 points) Tracer le champ électrique en $M'$, symétrique de $M$ par rapport à $\Pi$ (plan de symétrie de la distribution) ou à $\Pi^*$ (plan d'antisymétrie).

> **Note :** la figure de Q.19 montre deux fois un point $M$ au-dessus d'un plan horizontal ($\Pi$ à gauche, $\Pi^*$ à droite), avec un champ $\vec E(M)$ dirigé vers le haut et la droite ; $M'$ est le symétrique de $M$ sous le plan.

**Correction.** On teste chaque plan en regardant si la réflexion envoie chaque charge sur une charge **égale** (symétrie) ou **opposée** (antisymétrie).

1. **Réponse c).** Le plan $(Oxy)$ contient toutes les charges : il est de symétrie. La réflexion par $y = x$ échange $(-a, a)$ et $(a, -a)$, deux charges $+q$, et laisse fixes $(a, a)$ et $(-a, -a)$ : symétrie. La réflexion par $y = -x$ échange $(a, a)$ et $(-a, -a)$, deux charges $-q$ : symétrie.
2. **Réponse d).** La réflexion $x \to -x$ (plan $(Oyz)$) échange $(-a, a)$, $+q$, et $(a, a)$, $-q$ : antisymétrie. La réflexion $y \to -y$ (plan $(Oxz)$) échange $(-a, a)$, $+q$, et $(-a, -a)$, $-q$ : antisymétrie.
3. **Réponse d).** $(Oxy)$ contient le cercle ; $(Oxz)$ ($y \to -y$) envoie chaque demi-cercle sur lui-même. $(Oyz)$ n'est pas de symétrie car il échange les deux moitiés.
4. **Réponse d).** La réflexion par $(Oyz)$ échange la moitié $+\lambda$ et la moitié $-\lambda$ : c'est le seul plan d'antisymétrie.
5. Si $\Pi$ est un plan de **symétrie**, $\vec E(M')$ est le **symétrique** de $\vec E(M)$ par rapport à $\Pi$ : sur la figure, la composante parallèle au plan est conservée et la composante normale est inversée, donc $\vec E(M')$ pointe vers le bas et la droite.

    Si $\Pi^*$ est un plan d'**antisymétrie**, on prend le symétrique $\vec E_1(M')$ de $\vec E(M)$ par rapport à $\Pi^*$, puis son **opposé** : $\vec E(M') = -\vec E_1(M')$, car la réflexion change le signe des charges. Sur la figure, $\vec E(M')$ pointe vers le haut et la gauche : la composante normale au plan est conservée et la composante parallèle est inversée.
