---
source: TD2-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 14 (correction manuscrite ; page 15 vierge) ; exercice 9 : TD2-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 3 ; énoncés : TD_2024-2025_Electromagnetisme_P2S1_DPhysique.pdf, pages 7 à 9
transcription: manuelle
---

# TD2 — Champ électrostatique (corrigé)

> **Note :** la correction manuscrite traite les exercices dans l'ordre 1, 2, 3, 4, 8, 5, 6, 7 (l'exercice 8 y est présenté comme la suite de l'exercice 4) ; cet ordre est conservé. La correction de l'exercice 7 s'arrête au milieu du théorème de Gauss, et les exercices 9 et 10 ne sont pas corrigés : ces parties ont été complétées, l'exercice 9 à partir de la correction 2022-2023 (où il portait le numéro 6). Les calculs communs aux deux années sont identiques.

## Exercice 1 : Distribution discrète de charges ponctuelles

**Énoncé.** Quatre charges électriques ponctuelles, de valeur absolue $q$, sont placées aux sommets d'un carré $ABCD$. Ce carré a pour côté $2a$, centre $O$ et appartient au plan $Oxz$, comme le montre la figure. Déterminer l'expression de la force subie par la charge électrique $Q$ placée en un point $M$ quelconque de l'axe $Oy$.

> **Note :** la figure montre $+q$ en $A(a, 0, a)$ et en $C(-a, 0, -a)$, $-q$ en $B(a, 0, -a)$ et en $D(-a, 0, a)$, et la charge $Q$ en $M$ sur l'axe $Oy$. La correction y ajoute les quatre forces (attractives pour $B$ et $D$, répulsives pour $A$ et $C$ si $Q > 0$) et deux plans $P_1$, $P_2$ contenant l'axe $Oy$ et les diagonales du carré.

**Correction.** On a $|q_A| = |q_B| = |q_C| = |q_D| = q > 0$, et on travaille en coordonnées cartésiennes.

*Théorème de superposition :* la force exercée sur $Q$ en $M$ est la somme des forces exercées par chaque charge :
$$\vec F_{\to Q} = \vec F_{q_A \to Q} + \vec F_{q_B \to Q} + \vec F_{q_C \to Q} + \vec F_{q_D \to Q} \qquad (\mathrm{I})$$

Pour la charge en $A$ (loi de Coulomb), avec $k = \frac{1}{4\pi\varepsilon_0}$, $r_{AM} = \|\overrightarrow{AM}\|$ et $\vec u_{A \to M} = \overrightarrow{AM}/\|\overrightarrow{AM}\|$ :
$$\vec F_{q_A \to Q} = k\,\frac{q_A Q}{r_{AM}^2}\,\vec u_{A \to M} = k\,\frac{q_A Q}{\|\overrightarrow{AM}\|^3}\,\overrightarrow{AM}$$

et de même pour $q_B$, $q_C$, $q_D$.

*Coordonnées.* $A = (a, 0, a)$ ; $B = (a, 0, -a)$ est le symétrique de $A$ par rapport à l'axe $Ox$ ; $C = (-a, 0, -a)$ est le symétrique de $A$ par rapport à $O$ ; $D = (-a, 0, a)$ est le symétrique de $B$ par rapport à $O$ ; $M = (0, y, 0)$. Donc
$$\overrightarrow{AM} = (-a, y, -a), \quad \overrightarrow{BM} = (-a, y, a), \quad \overrightarrow{CM} = (a, y, a), \quad \overrightarrow{DM} = (a, y, -a)$$

Les quatre distances sont égales (pyramide à base carrée de sommet $M$) :
$$r^2 = (-a)^2 + y^2 + (-a)^2 = 2a^2 + y^2, \qquad r = (y^2 + 2a^2)^{1/2}$$

Le facteur $k\,Q/r^3$ est commun aux quatre forces, et (I) donne, avec $q_A = q_C = +q$ et $q_B = q_D = -q$ :
$$\vec F_{\to Q} = k\,\frac{Qq}{r^3}\Big[\overrightarrow{AM} - \overrightarrow{BM} + \overrightarrow{CM} - \overrightarrow{DM}\Big]$$

Composante par composante : selon $x$, $-a + a + a - a = 0$ ; selon $y$, $y - y + y - y = 0$ ; selon $z$, $-a - a + a + a = 0$. Donc
$$\vec F_{\to Q} = \vec 0$$

*Contrôle par les symétries.* Les plans $P_1$ et $P_2$ contenant $Oy$ et une diagonale du carré sont des plans de symétrie (par exemple, le plan contenant $Oy$ et $(BD)$ échange $A$ et $C$, qui portent la même charge $+q$). Le champ en $M$ appartient à $P_1 \cap P_2 = Oy$ : $\vec E(M)$ est selon $\vec e_y$. De plus, les plans $x = 0$ (qui échange $A(+q)$ et $D(-q)$) et $z = 0$ (qui échange $A(+q)$ et $B(-q)$) sont des plans d'**antisymétrie** : en $M$, le champ doit leur être perpendiculaire, donc à la fois selon $\vec e_x$ et selon $\vec e_z$. Il ne peut être aussi selon $\vec e_y$ que s'il est nul, ce qui confirme $\vec E(M) = \vec 0$ et $\vec F = Q\vec E(M) = \vec 0$.

## Exercice 2 : Symétrie sphérique

**Énoncé.** Soit une sphère, de rayon $R$, chargée uniformément. En commençant par une étude de symétrie et d'invariance, calculer le flux de $\vec E$ à travers la surface $\Sigma$ d'une sphère de rayon $r$. Les deux sphères ont le même centre.

> **Note :** la figure montre la sphère chargée de rayon $R$ (chargée en volume avec $\rho = \rho_0$ constante, ou en surface avec $\sigma = \sigma_0$ constante) et la sphère $\Sigma$ de rayon $r$, avec les coordonnées sphériques d'un point $M$ et le volume élémentaire $dr \times r\,d\theta \times r\sin\theta\,d\varphi$.

**Correction.**

*Système de coordonnées :* sphériques $\{O, (\vec e_r, \vec e_\theta, \vec e_\varphi)\}$, avec $\overrightarrow{OM} = r\,\vec e_r$ et
$$d\vec\ell = dr\,\vec e_r + r\,d\theta\,\vec e_\theta + r\sin\theta\,d\varphi\,\vec e_\varphi$$

d'où $dS_r = r^2\sin\theta\,d\theta\,d\varphi$, $dS_\theta = r\sin\theta\,dr\,d\varphi$, $dS_\varphi = r\,dr\,d\theta$. A priori, $\vec E(M) = E(r, \theta, \varphi)\,\vec u$.

*Invariances :* la sphère est uniformément chargée, la distribution reste la même quand on fait varier $\theta$ et $\varphi$ : $E$ ne dépend que de $r$.

*Symétries* (elles donnent la direction de $\vec E$) : tout plan $P$ passant par $M$ et par le centre $O$ de la sphère est un plan de symétrie de la distribution. Il y en a une infinité, $\vec E$ appartient à chacun, et leur direction commune est $\vec e_r$ : $\vec u = \vec e_r$.
$$\vec E(M) = E(r)\,\vec e_r$$

*Flux.* Le flux élémentaire à travers $d\vec S = dS\,\vec n$ est $d\Phi = \vec E \cdot d\vec S$. Sur $\Sigma$, $\vec n = \vec e_r$ et $d\Phi = E(r)\,dS_r$, avec $r$ constant :
$$\Phi(\vec E) = E(r)\,r^2 \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\varphi = 4\pi r^2 E(r)$$

Unité : $E$ en $\mathrm{V \cdot m^{-1}}$ (car $\vec E = -\overrightarrow{\operatorname{grad}}\,V$), donc $\Phi$ en $\mathrm{V \cdot m}$ ; $[\Phi] = [E]\,L^2 = \frac{[Q]}{[\varepsilon_0]}$.

## Exercice 3 : Symétrie cylindrique

**Énoncé.** Soit un cylindre, de rayon $R$ et de hauteur supposée infinie, chargé uniformément. En commençant par une étude de symétrie et d'invariance, calculer le flux de $\vec E$ à travers la surface $\Sigma$ d'un cylindre de rayon $r$ et de hauteur $h$. Les deux cylindres ont le même axe.

> **Note :** la figure montre le cylindre chargé d'axe $(Oz)$, de rayon $R$, le cylindre $\Sigma$ de rayon $r$ et de hauteur $h$ (bases $S_1$ et $S_2$, surface latérale $S_L$), et les plans de symétrie $P_1$ et $P_2$ passant par $M$.

**Correction.**

*Coordonnées :* cylindriques $\{O, (\vec e_\rho, \vec e_\theta, \vec e_z)\}$, avec $\overrightarrow{OM} = \rho\,\vec e_\rho + z\,\vec e_z$. A priori $\vec E = E(\rho, \theta, z)\,\vec u$.

*Invariances :*

- le cylindre est infini selon $(Oz)$ : la distribution est invariante par translation selon $z$, et $E$ ne dépend pas de $z$ ;
- la distribution est uniforme : elle est invariante par rotation autour de $(Oz)$, et $E$ ne dépend pas de $\theta$.

Donc $\vec E = E(\rho)\,\vec u$.

*Symétries :* $P_1 = (M, \vec e_\rho, \vec e_\theta)$ et $P_2 = (M, \vec e_\rho, \vec e_z)$ sont des plans de symétrie de la distribution. $\vec E \in P_1 \cap P_2$, donc
$$\vec E = E(\rho)\,\vec e_\rho$$

*Flux* à travers la surface fermée $\Sigma$ (cylindre de hauteur $h$, de rayon $r$, de même axe) : sur les bases, $d\vec S$ est selon $\pm\vec e_z$, perpendiculaire à $\vec E$ ; seule la surface latérale ($\rho = r$ constant, $dS_\rho = r\,d\theta\,dz$) contribue :
$$\Phi(\vec E) = \oint_\Sigma E(\rho)\,\vec e_\rho \cdot d\vec S = \int_0^{2\pi} \int_{-h/2}^{h/2} r\,E(r)\,d\theta\,dz = 2\pi r h\,E(r)$$

c'est-à-dire $E(r)$ multiplié par l'aire latérale $2\pi r \times h$.

## Exercice 4 : Symétrie plane

**Énoncé.** Soit un plan infini chargé uniformément de densité $\sigma$. En commençant par une étude de symétrie et d'invariance, calculer le flux de $\vec E$ à travers la surface $\Sigma$ d'un cylindre de rayon $r$ et de hauteur $h$. L'axe du cylindre est perpendiculaire au plan chargé (il serait intéressant de prendre $h/2$ de part et d'autre du plan).

> **Note :** la figure montre le plan chargé ($\sigma > 0$) et le cylindre $\Sigma$ d'axe $(Oz)$, de rayon $r$, s'étendant de $-h/2$ à $h/2$, avec ses bases $S_1$ (en haut), $S_2$ (en bas) et sa surface latérale $S_L$.

**Correction.** Ici $\sigma = \dfrac{dq}{dS} = \sigma_0$ est constante.

*Coordonnées :* cylindriques $\{O, (\vec u_r, \vec u_\theta, \vec u_z)\}$, avec $(Oz)$ perpendiculaire au plan. A priori $\vec E = E(r, \theta, z)\,\vec u$.

*Invariances :* le plan est infini et uniformément chargé, la distribution est invariante (a) par rotation autour de $(Oz)$ et (b) par translation selon $\vec u_r$. Donc $E$ ne dépend ni de $\theta$ ni de $r$ : $\vec E = E(z)\,\vec u$.

*Symétries :* $P_1 = (M, \vec u_r, \vec u_z)$ et $P_2 = (M, \vec u_\theta, \vec u_z)$ sont des plans de symétrie de la distribution ; $\vec E$ appartient à leur intersection, de direction $\vec u_z$ :
$$\vec E = E(z)\,\vec u_z$$

Le plan chargé est lui-même un plan de symétrie : $E(z < 0) = -E(z > 0)$ (pour $\sigma > 0$, le champ s'éloigne du plan des deux côtés).

*Flux.* $\Sigma = S_1 \cup S_2 \cup S_L$ avec les normales **sortantes** $\vec n_1 = +\vec u_z$ (base $S_1$ en $z = h/2$), $\vec n_2 = -\vec u_z$ (base $S_2$ en $z = -h/2$) et $\vec n_L = \vec u_r$. Le flux latéral est nul car $\vec u_r \cdot \vec u_z = 0$. Avec $dS_z = r'\,dr'\,d\theta$ :
$$\Phi_1 = \iint_{S_1} E(z > 0)\,dS_z, \qquad \Phi_2 = \iint_{S_2} E(z < 0)\,\vec u_z \cdot (-\vec u_z)\,dS_z = \iint_{S_2} E(z > 0)\,dS_z = \Phi_1$$

$$\Phi(\vec E) = 2\Phi_1 = 2\,E(z > 0) \int_0^r r'\,dr' \int_0^{2\pi} d\theta = 2\pi r^2\,E(z > 0)$$

> **Erreur corrigée :** la correction manuscrite oriente la base inférieure par $d\vec S_2 = dS_2\,\vec u_z$ et écrit $\Phi_2 = \iint_{S_2} E(z)\,dS_z$. Avec cette orientation (non sortante), on trouverait $\Phi_2 = -\Phi_1$ et un flux total nul. La normale sortante de $S_2$ est $-\vec u_z$, ce qui donne bien $\Phi_2 = \Phi_1$ et le résultat final de la correction, $\Phi = 2\pi r^2 E(z > 0)$.

## Exercice 8 : Plan infini uniformément chargé

**Énoncé.** Soit un plan infini uniformément chargé en surface, de densité surfacique de charge $\sigma$ séparant l'espace en deux demi-espaces $z > 0$ et $z < 0$. Appliquer le théorème de Gauss pour calculer le champ électrostatique $\vec E$ engendré par cette distribution en tout point $M$ de l'espace. Remarquer la discontinuité du champ $\vec E$ en $z = z_{\text{plan}}$ ($= 0$ ici).

> **Note :** la figure montre le plan chargé $\sigma$ et l'axe $(Oz)$ perpendiculaire.

**Correction.** C'est la suite de l'exercice 4 ($\sigma = \sigma_0$ constante) : on sait que $\vec E = E(z)\,\vec u_z$, que $E(z < 0) = -E(z > 0)$, et que le flux à travers le cylindre $\Sigma$ vaut $\Phi(\vec E) = 2\pi r^2\,E(z > 0)$.

*Théorème de Gauss :* le flux de $\vec E$ à travers une surface **fermée** $\Sigma$ est proportionnel à la charge $q_{\text{int}}$ contenue dans le volume délimité par $\Sigma$ :
$$\Phi(\vec E) = \oint_\Sigma \vec E \cdot d\vec S = \frac{q_{\text{int}}}{\varepsilon_0}$$

La surface de Gauss $\Sigma$ est choisie « astucieusement », en respectant les symétries : c'est le cylindre de l'exercice 4.

*Charge intérieure :* la seule charge contenue dans $\Sigma$ est celle du disque de rayon $r$ découpé dans le plan :
$$q_{\text{int}} = \iint_{\text{disque}} \sigma\,dS = \sigma \pi r^2$$

D'où
$$2\pi r^2\,E(z > 0) = \frac{\sigma \pi r^2}{\varepsilon_0} \quad \Longrightarrow \quad E(z > 0) = \frac{\sigma}{2\varepsilon_0}, \qquad E(z < 0) = -\frac{\sigma}{2\varepsilon_0}$$

Le champ est uniforme dans chaque demi-espace et dirigé en s'éloignant du plan si $\sigma > 0$ (vers le plan si $\sigma < 0$).

*Discontinuité* à la traversée de la surface chargée :
$$E(z = 0^+) - E(z = 0^-) = \frac{\sigma}{\varepsilon_0}$$

> **Note :** la correction trace $E(z)$ : $-\frac{\sigma}{2\varepsilon_0}$ pour $z < 0$, $+\frac{\sigma}{2\varepsilon_0}$ pour $z > 0$, avec un saut de $\frac{\sigma}{\varepsilon_0}$ en $z = 0$.

## Exercice 5 : Sphère uniformément chargée en volume

**Énoncé.** Une sphère de centre $O$ et de rayon $R$ porte une densité volumique de charge uniforme $\rho$.

1. Quelle est l'expression de la charge totale, notée $Q$, contenue dans la sphère ?
2. Calculer le champ électrostatique $\vec E(M)$ en considérant le point $M$ :
    a) à l'intérieur de la sphère : $r < R$ ;
    b) à l'extérieur de la sphère : $r > R$.
3. Le champ est-il continu à la traversée de la sphère ? À commenter.
4. Tracer l'allure de $E(r)$.

**Correction.**

**1.** $\rho = \dfrac{dq}{dV}$ est uniforme :
$$Q = \iiint_{V_R} \rho\,dV = \frac{4}{3}\pi R^3 \rho$$

**2.** La distribution est volumique : $\vec E$ est défini et continu partout. En coordonnées sphériques, la distribution est invariante par rotation ($\theta$, $\varphi$) : $\vec E = \vec E(r)$ ; tout plan passant par $M$ et $O$ est plan de symétrie : $\vec E = E(r)\,\vec e_r$ (radial).

*Surface de Gauss :* la sphère $S_G$ de centre $O$ et de rayon $r$. Comme à l'exercice 2,
$$\Phi(\vec E) = \oint_{S_G} E(r)\,dS_r = 4\pi r^2 E(r) = \frac{q_{\text{int}}}{\varepsilon_0}$$

*Charge intérieure :*

- si $r \ge R$ : toute la boule est à l'intérieur, $q_{\text{int}} = Q = \frac{4}{3}\pi R^3 \rho$ ;
- si $r \le R$ : seule une partie de la charge est intérieure, $q_{\text{int}} = \iiint \rho\,dV = \frac{4}{3}\pi r^3 \rho = \big(\frac{r}{R}\big)^3 Q$.

D'où $E(r) = \dfrac{q_{\text{int}}}{4\pi\varepsilon_0 r^2}$ :

- a) $r < R$ : $E(r) = \dfrac{1}{4\pi\varepsilon_0 r^2} \cdot \dfrac{4}{3}\pi r^3 \rho = \dfrac{\rho\,r}{3\varepsilon_0}$ ;
- b) $r > R$ : $E(r) = \dfrac{1}{4\pi\varepsilon_0 r^2} \cdot \dfrac{4}{3}\pi R^3 \rho = \dfrac{\rho R^3}{3\varepsilon_0 r^2} = \dfrac{Q}{4\pi\varepsilon_0 r^2}$.

À l'extérieur, la boule crée le même champ qu'une charge ponctuelle $Q$ placée en $O$. Homogénéité : $[E] = \frac{[q]}{[\varepsilon_0]L^2}$ et $[\rho\,r] = \frac{[q]}{L^3}L = \frac{[q]}{L^2}$ : c'est cohérent.

**3.** En $r = R$ : $E(R^-) = E(R^+) = \dfrac{\rho R}{3\varepsilon_0}$. Le champ est **continu** à la traversée de la sphère, ce qui est attendu pour une distribution volumique (pas de charge surfacique).

**4.** $E(r)$ croît linéairement de $0$ (en $r = 0$) à $\frac{\rho R}{3\varepsilon_0}$ (en $r = R$), puis décroît en $1/r^2$ vers $0$ quand $r \to \infty$.

## Exercice 6 : Sphère uniformément chargée en surface

**Énoncé.** Une sphère de centre $O$ et de rayon $R$ porte une densité surfacique de charge uniforme $\sigma$.

1. Quelle est l'expression de la charge totale, notée $Q$, sur la sphère ?
2. Calculer le champ électrostatique $\vec E(M)$ en considérant le point $M$ :
    a) à l'intérieur de la sphère : $r < R$ ;
    b) à l'extérieur de la sphère : $r > R$.
3. Le champ est-il continu à la traversée de la sphère ? À commenter.
4. Tracer l'allure de $E(r)$.

**Correction.**

**1.** Sur la sphère ($r = R$), $dS_r = R^2 \sin\theta\,d\theta\,d\varphi$ :
$$Q = \iint \sigma\,dS_r = \sigma R^2 \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\varphi = 4\pi R^2 \sigma$$

**2.** La distribution est surfacique : $\vec E$ est défini et continu partout sauf à la traversée de la surface chargée. Les invariances et symétries sont les mêmes qu'à l'exercice 5 : $\vec E = E(r)\,\vec e_r$. Avec la sphère de Gauss de rayon $r$ :
$$4\pi r^2 E(r) = \frac{q_{\text{int}}}{\varepsilon_0}$$

- a) $r < R$ : la sphère de Gauss ne contient aucune charge, $q_{\text{int}} = 0$, donc $E(r) = 0$ ;
- b) $r > R$ : $q_{\text{int}} = Q = 4\pi R^2 \sigma$, donc $E(r) = \dfrac{4\pi R^2 \sigma}{4\pi\varepsilon_0 r^2} = \dfrac{\sigma}{\varepsilon_0}\dfrac{R^2}{r^2}$.

**3.** **Non** : $E(R^-) = 0$ et $E(R^+) = \dfrac{\sigma}{\varepsilon_0}$. Le champ est discontinu à la traversée de la surface chargée, et le saut vaut $\dfrac{\sigma}{\varepsilon_0}$ (même valeur que pour le plan infini de l'exercice 8).

**4.** $E(r)$ est nul pour $r < R$, saute à $\frac{\sigma}{\varepsilon_0}$ en $r = R$, puis décroît en $1/r^2$.

## Exercice 7 : Fil infini uniformément chargé

**Énoncé.**

1. Calculer par intégration le champ électrostatique $\vec E$ créé en un point $M$ quelconque de l'espace par une distribution linéique de charges de densité $\lambda$ uniforme et répartie le long de l'axe des $z$.
2. Retrouver ce résultat en calculant $\vec E$ en appliquant le théorème de Gauss.

**Correction.**

**1.** On note $r$ la distance de $M$ à l'axe. Un élément $dz$ du fil, centré en $P$ de cote $z$, porte la charge $dq = \lambda\,dz$ et crée en $M$ (loi de Coulomb)
$$d\vec E = \frac{dq}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3} = \frac{\lambda\,dz}{4\pi\varepsilon_0}\frac{\overrightarrow{PM}}{PM^3}$$

avec $\overrightarrow{PM} = \overrightarrow{PO} + \overrightarrow{OM} = r\,\vec e_r - z\,\vec e_z$ et $PM^2 = r^2 + z^2$ (on a placé l'origine $O$ au pied de la perpendiculaire issue de $M$).

Les plans $P_1 = (M, \vec e_r, \vec e_\theta)$ et $P_2 = (M, \vec e_r, \vec e_z)$ sont des plans de symétrie, donc $\vec E \in P_1 \cap P_2$ et $\vec E = E_r\,\vec e_r$ : il suffit de sommer les composantes radiales (les composantes selon $\vec e_z$ de deux éléments symétriques par rapport à $P_1$ se compensent).

> **Erreur corrigée :** la correction manuscrite écrit $\vec E \in (P_1 \cup P_2)$ ; le champ appartient à chacun des deux plans, donc à leur intersection $P_1 \cap P_2$, de direction $\vec e_r$.

$$E_r = \frac{\lambda}{4\pi\varepsilon_0}\int_{-\infty}^{+\infty} \frac{r\,dz}{(r^2 + z^2)^{3/2}}$$

*Changement de variable :* $z = r\tan\alpha$, où $\alpha$ est l'angle sous lequel on voit $P$ depuis $M$, $\alpha \in \,]-\frac{\pi}{2}, \frac{\pi}{2}[$. Alors $dz = \dfrac{r\,d\alpha}{\cos^2\alpha}$ (car $\frac{d}{d\alpha}\tan\alpha = 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}$) et $r^2 + z^2 = \dfrac{r^2}{\cos^2\alpha}$, d'où
$$\frac{r\,dz}{(r^2 + z^2)^{3/2}} = \frac{r \cdot r\,d\alpha / \cos^2\alpha}{r^3/\cos^3\alpha} = \frac{\cos\alpha\,d\alpha}{r}$$

$$E_r = \frac{\lambda}{4\pi\varepsilon_0 r}\int_{-\pi/2}^{\pi/2} \cos\alpha\,d\alpha = \frac{\lambda}{4\pi\varepsilon_0 r}\big[\sin\alpha\big]_{-\pi/2}^{\pi/2} = \frac{\lambda}{2\pi\varepsilon_0 r}$$

$$\vec E = \frac{\lambda}{2\pi\varepsilon_0 r}\,\vec e_r$$

**2.**

- *Définition :* $\vec E$ est défini et continu partout sauf sur le fil (où se trouvent les charges).
- *Coordonnées :* cylindriques $(O, \vec u_r, \vec u_\theta, \vec u_z)$.
- *Invariances :* fil infini et uniforme, invariance par translation selon $z$ et par rotation autour de $(Oz)$ : $\vec E(r, \theta, z) = \vec E(r)$.
- *Symétries :* $P_1 = (M, \vec u_r, \vec u_\theta)$ et $P_2 = (M, \vec u_r, \vec u_z)$ sont plans de symétrie : $\vec E = E(r)\,\vec u_r$.

*Surface de Gauss :* elle doit être fermée, de dimensions finies, contenir une partie de la distribution et respecter la géométrie du problème. On prend le cylindre $\Sigma$ d'axe $(Oz)$, de rayon $r$ et de hauteur $h$, formé des bases $S_1$ ($\vec n_1 = +\vec u_z$), $S_2$ ($\vec n_2 = -\vec u_z$) et de la surface latérale $S_3$ ($\vec n_3 = +\vec u_r$). Les flux à travers $S_1$ et $S_2$ sont nuls ($\vec u_r \cdot \vec n = 0$), et
$$\Phi(\vec E) = \iint_{S_3} E(r)\,r\,d\theta\,dz = 2\pi r h\,E(r)$$

> **Complément :** la correction manuscrite s'arrête après la décomposition du flux ; la fin du calcul (charge intérieure et conclusion) a été rédigée pour cette transcription.

*Charge intérieure :* $q_{\text{int}} = \int_0^h \lambda\,dz = \lambda h$.

*Théorème de Gauss :* $2\pi r h\,E(r) = \dfrac{\lambda h}{\varepsilon_0}$, d'où
$$\vec E = \frac{\lambda}{2\pi\varepsilon_0 r}\,\vec u_r$$

On retrouve le même résultat, indépendant de $h$ comme il se doit.

## Exercice 9 : Lecture d'une carte de champ

**Énoncé.** (*) On donne ci-contre les lignes de champ électrostatique générées par une distribution de charges ponctuelles. Les charges sont numérotées de 1 à 5 de gauche à droite.

1. Donner le signe de chacune des charges.
2. Déterminer les éventuels plans de symétrie et d'anti-symétrie de la distribution de charge. Exprimer les charges $q_4$ et $q_5$ en fonction des autres.
3. D'après les lignes du champ électrostatique $\vec E$, que peut-on dire de $\vec E \cdot d\vec S$ en tout point de la surface $S$ ?
4. En déduire $q_3$ en fonction des autres charges.

> **Note :** la figure est une carte de lignes de champ dans le plan $(xOy)$ ($x$ et $y$ entre $-4$ et $4\ \mathrm{m}$) : cinq charges alignées sur l'axe $y = 0$, aux abscisses $-3$, $-1{,}5$, $0$, $1{,}5$ et $3\ \mathrm{m}$ environ, et une courbe fermée ovale $S$ qui entoure les charges 2, 3 et 4 et qu'aucune ligne de champ ne traverse.

**Correction.**

> **Complément :** la correction 2024-2025 ne traite pas cet exercice ; cette correction reprend celle de 2022-2023 (exercice 6), dont la question 3 était formulée autrement (« on admet que le champ est nul en tout point de $S$ »).

**1.** Une ligne de champ est tangente à $\vec E$ en chacun de ses points ($\vec E \wedge d\vec\ell = \vec 0$) et orientée dans le sens de $\vec E$ ; les lignes partent des charges positives et arrivent sur les charges négatives. Sur la carte, elles partent de $q_1$, $q_2$, $q_4$, $q_5$ et convergent vers $q_3$ :
$$q_1, q_2, q_4, q_5 > 0 \qquad \text{et} \qquad q_3 < 0$$

**2.** La carte est symétrique par rapport au plan $x = 0$ : c'est un plan de **symétrie** de la distribution. Le plan $y = 0$, qui contient toutes les charges, est aussi plan de symétrie. Il n'y a pas de plan d'antisymétrie. La symétrie $x \mapsto -x$ échange $q_1$ et $q_5$, $q_2$ et $q_4$ :
$$q_5 = q_1 \qquad \text{et} \qquad q_4 = q_2$$

**3.** Aucune ligne de champ ne traverse $S$ : en tout point de $S$, $\vec E$ est soit nul, soit tangent à $S$. Dans les deux cas,
$$\vec E \cdot d\vec S = 0 \quad \text{en tout point de } S$$

($d\vec S$ est normal à la surface).

**4.** On applique le théorème de Gauss à la surface fermée $S$, qui contient $q_2$, $q_3$ et $q_4$ :
$$\oint_S \vec E \cdot d\vec S = 0 = \frac{q_2 + q_3 + q_4}{\varepsilon_0}$$

Avec $q_4 = q_2$ : $2q_2 + q_3 = 0$, soit
$$q_3 = -2q_2$$

ce qui est cohérent avec $q_3 < 0$.

## Exercice 10 : Sphère chargée avec une cavité

**Énoncé.** Une sphère de rayon $R$ porte une densité volumique de charge constante $\rho$, sauf dans une cavité sphérique (de rayon $a$ et dont le centre est à la distance $d$ du centre de la grande sphère) creusée dans la sphère. Calculer le champ électrique dans la cavité.

**Correction.**

> **Complément :** cet exercice n'est pas corrigé dans le document ; la correction suivante a été rédigée pour cette transcription.

La distribution n'a plus la symétrie sphérique, mais on peut l'écrire comme une **superposition** de deux distributions à symétrie sphérique :

- une boule pleine de centre $O$, de rayon $R$, de densité $+\rho$ ;
- une boule de centre $O'$ (centre de la cavité, $OO' = d$), de rayon $a$, de densité $-\rho$.

Dans la cavité, leurs densités s'additionnent en $\rho - \rho = 0$ ; ailleurs dans la grande sphère, on retrouve $\rho$.

*Champ d'une boule uniforme en un point intérieur.* D'après l'exercice 5, une boule de centre $C$ et de densité $\rho$ crée en un point intérieur $M$ le champ $\vec E = \dfrac{\rho\,r}{3\varepsilon_0}\vec e_r$, c'est-à-dire, sous forme vectorielle,
$$\vec E(M) = \frac{\rho}{3\varepsilon_0}\,\overrightarrow{CM}$$

*Superposition.* Un point $M$ de la cavité est intérieur aux deux boules :
$$\vec E(M) = \frac{\rho}{3\varepsilon_0}\,\overrightarrow{OM} + \frac{-\rho}{3\varepsilon_0}\,\overrightarrow{O'M} = \frac{\rho}{3\varepsilon_0}\big(\overrightarrow{OM} - \overrightarrow{O'M}\big) = \frac{\rho}{3\varepsilon_0}\,\overrightarrow{OO'}$$

Le champ dans la cavité est **uniforme** : il est dirigé selon $\overrightarrow{OO'}$ (du centre de la sphère vers le centre de la cavité, si $\rho > 0$) et sa norme vaut
$$E = \frac{\rho\,d}{3\varepsilon_0}$$

Cas limite : si $d = 0$ (cavité centrée), le champ est nul dans la cavité, comme le donne directement le théorème de Gauss (aucune charge à l'intérieur d'une sphère de rayon $r < a$).
