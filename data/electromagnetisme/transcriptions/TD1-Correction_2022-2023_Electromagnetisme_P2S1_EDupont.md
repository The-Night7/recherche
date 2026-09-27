---
source: TD1-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 6 (correction manuscrite)
transcription: manuelle
---

# TD1 — Calculs de charges et forces électromagnétiques (corrigé)

> **Note :** la correction manuscrite suit l'ordre 1, 2, 5, 6, 4, 3 des exercices ; cet ordre et cette numérotation sont conservés. Dans le recueil d'énoncés 2023-2024, l'exercice 3 (charges ponctuelles) a été déplacé au début du chapitre 2, et les exercices 5, 6 et 4 sont devenus 3, 4 et 5.

## Exercice 1 : Calculs d'aire et de volume

**Énoncé.** En choisissant le système de coordonnées approprié :

1. Calculer, en utilisant une intégrale double, la surface d'un disque de rayon $R$.
2. Calculer, en utilisant une intégrale double, la surface de la paroi latérale d'un cylindre de hauteur $h$ et de rayon $R$.
3. Calculer, en utilisant une intégrale triple, le volume d'un cylindre de hauteur $h$ et de rayon $R$.

**Correction.** Les trois objets ont un axe de révolution $(Oz)$ : on utilise les **coordonnées cylindriques** $(\rho, \theta, z)$, avec $\overrightarrow{OM} = \rho\,\vec e_\rho + z\,\vec e_z$.

Le déplacement élémentaire est $d\overrightarrow{OM} = d\rho\,\vec e_\rho + \rho\,d\theta\,\vec e_\theta + dz\,\vec e_z$. Un élément de surface est le produit de deux déplacements élémentaires perpendiculaires (norme d'un produit vectoriel $\vec a \wedge \vec b$ avec $\vec a \perp \vec b$) :

- $dS_\rho = \rho\,d\theta\,dz$ (surface perpendiculaire à $\vec e_\rho$, sur un cylindre $\rho = $ cte) ;
- $dS_\theta = d\rho\,dz$ (perpendiculaire à $\vec e_\theta$) ;
- $dS_z = \rho\,d\rho\,d\theta$ (perpendiculaire à $\vec e_z$, dans un plan $z = $ cte).

> **Note :** les figures montrent le disque dans le plan $(Oxy)$ avec l'élément $dS_z$ hachuré, puis le cylindre d'axe $(Oz)$ compris entre $z = -h/2$ et $z = h/2$, et sa paroi latérale « déroulée » en un rectangle de côtés $h$ et $2\pi R$.

**1.** Le disque est dans un plan $z = $ cte : on intègre $dS_z$ pour $\rho \in [0, R]$ et $\theta \in [0, 2\pi]$. Les variables sont séparables :
$$S = \iint_{\text{disque}} \rho\,d\rho\,d\theta = \left[\frac{\rho^2}{2}\right]_0^R \times \big[\theta\big]_0^{2\pi} = \frac{R^2}{2} \times 2\pi = \pi R^2$$

**2.** Sur la paroi latérale, $\rho = R$ est fixé : on intègre $dS_\rho = R\,d\theta\,dz$ pour $\theta \in [0, 2\pi]$ et $z \in [-h/2, h/2]$ :
$$S = R \int_{-h/2}^{h/2} dz \int_0^{2\pi} d\theta = R\,\Big(\frac{h}{2} + \frac{h}{2}\Big)\,(2\pi - 0) = 2\pi R h$$

C'est l'aire du rectangle obtenu en déroulant la paroi : périmètre $2\pi R$ fois hauteur $h$.

**3.** Le volume élémentaire est $dV = d\rho \times \rho\,d\theta \times dz$ :
$$V = \int_0^R \rho\,d\rho \int_0^{2\pi} d\theta \int_{-h/2}^{h/2} dz = \frac{R^2}{2} \times 2\pi \times h = \pi R^2 h$$

(aire de la base fois hauteur).

## Exercice 2 : Calculs de charge totale

**Énoncé.** En choisissant le système de coordonnées approprié :

1. Calculer la charge totale contenue dans un disque de rayon $R$ uniformément chargé en surface dont la densité surfacique vaut $\sigma_0$.
2. Calculer la charge totale contenue dans un fil de longueur $L$ uniformément chargé dont la densité linéique vaut $\lambda_0$.
3. Calculer la charge totale contenue dans une sphère de rayon $R$ uniformément chargée en volume dont la densité volumique vaut $\rho_0$.

**Correction.**

**1.** Par définition de la densité surfacique de charge, $\sigma = \dfrac{dq}{dS}$ (en $\mathrm{C \cdot m^{-2}}$). La charge est uniforme, $\sigma = \sigma_0$ constante, donc
$$Q = \iint_{\text{disque}} dq = \iint_{\text{disque}} \sigma_0\,dS = \sigma_0 \iint_{\text{disque}} dS = \sigma_0\,\pi R^2$$

en utilisant l'aire du disque calculée à l'exercice 1.

**2.** Densité linéique : $\lambda = \dfrac{dq}{d\ell}$ (en $\mathrm{C \cdot m^{-1}}$), ici constante égale à $\lambda_0$ :
$$Q = \int_{\text{fil}} \lambda_0\,d\ell = \lambda_0 L$$

**3.** On utilise les **coordonnées sphériques** $(r, \theta, \varphi)$, avec $\overrightarrow{OM} = r\,\vec e_r$ :
$$d\overrightarrow{OM} = dr\,\vec e_r + r\,d\theta\,\vec e_\theta + r\sin\theta\,d\varphi\,\vec e_\varphi$$

d'où les éléments de surface $dS_r = r^2 \sin\theta\,d\theta\,d\varphi$, $dS_\theta = r\sin\theta\,dr\,d\varphi$, $dS_\varphi = r\,dr\,d\theta$, et le volume élémentaire $dV = r^2 \sin\theta\,dr\,d\theta\,d\varphi$, avec $r \in [0, R]$, $\theta \in [0, \pi]$, $\varphi \in [0, 2\pi]$.

Volume de la boule :
$$V = \int_0^R r^2\,dr \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\varphi = \frac{R^3}{3} \times \big[-\cos\theta\big]_0^\pi \times 2\pi = \frac{R^3}{3} \times 2 \times 2\pi = \frac{4}{3}\pi R^3$$

Avec $\rho = \dfrac{dq}{dV} = \rho_0$ constante :
$$Q = \iiint \rho_0\,dV = \rho_0 V = \frac{4}{3}\pi R^3 \rho_0$$

## Exercice 5 : Charge totale d'une distribution surfacique non uniforme

**Énoncé.** On considère une sphère de centre $O$ et de rayon $R$ portant en sa surface une densité de charges
$$\sigma = \sigma_0 (1 + \cos\theta)$$

où $\theta = (\overrightarrow{Oz}, \overrightarrow{OP})$. Calculer la charge totale portée par la distribution.

**Correction.** Par définition $\sigma = \dfrac{dq}{dS}$, donc $Q = \iint_{P \in S} \sigma\,dS_r$. Sur la sphère, $r = R$ et $dS_r = R^2 \sin\theta\,d\theta\,d\varphi$ :
$$Q = \int_0^\pi \int_0^{2\pi} \sigma_0 (1 + \cos\theta)\,R^2 \sin\theta\,d\theta\,d\varphi = \sigma_0 R^2\, I_\theta \times 2\pi$$

avec, en posant $u = \cos\theta$, $du = -\sin\theta\,d\theta$ :
$$I_\theta = \int_0^\pi (1 + \cos\theta)\sin\theta\,d\theta = \int_{-1}^{1} (1 + u)\,du = \left[u + \frac{u^2}{2}\right]_{-1}^{1} = \frac{3}{2} - \Big(-\frac{1}{2}\Big) = 2$$

Donc
$$Q = 4\pi R^2 \sigma_0$$

C'est la même charge que si la densité valait $\sigma_0$ partout : le terme $\sigma_0 \cos\theta$ est positif sur l'hémisphère nord et négatif sur l'hémisphère sud, et sa contribution totale est nulle ($\int_0^\pi \cos\theta \sin\theta\,d\theta = 0$).

## Exercice 6 : Noyaux atomiques

**Énoncé.** (*) Du point de vue du potentiel et du champ électrique qu'ils créent, les noyaux de certains atomes légers peuvent être modélisés par une distribution volumique de charge à l'intérieur d'une sphère de centre $O$ et de rayon $a$. On désigne par $\vec r = \overrightarrow{OP}$ le vecteur position d'un point $P$ quelconque de l'espace. Pour $r < a$, la charge volumique $\rho(P)$ qui représente le noyau varie en fonction de $r$ suivant la loi :
$$\rho(r) = \rho_0 \left(1 - \frac{r^2}{a^2}\right)$$

où $\rho_0$ est une constante positive.

1. Donner les symétries et invariances de cette distribution de charges.
2. Exprimer la charge totale $Q$ du noyau.

**Correction.**

**1.** *Invariances.* La densité ne dépend que de $r$ : la distribution est invariante par toute rotation autour de $O$, c'est-à-dire par variation de $\theta$ et de $\varphi$. Le champ en $M$ ne dépend donc que de $r$ : $\vec E(r, \theta, \varphi) = \vec E(r)$.

*Symétries.* Tout plan passant par $O$ (et par $M$) est un plan de symétrie de la distribution. Le champ en $M$ appartient à tous ces plans, donc à leur intersection, la droite $(OM)$ :
$$\vec E = E(r)\,\vec e_r$$

**2.** En coordonnées sphériques, pour $r < a$ :
$$Q = \iiint_{r < a} \rho(r)\,dV = \rho_0 \int_0^a \Big(1 - \frac{r^2}{a^2}\Big) r^2\,dr \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\varphi$$

avec
$$I_r = \int_0^a \Big(r^2 - \frac{r^4}{a^2}\Big) dr = \frac{a^3}{3} - \frac{a^3}{5} = \frac{2a^3}{15}$$

d'où
$$Q = \rho_0 \times \frac{2a^3}{15} \times 2 \times 2\pi = \frac{8\pi \rho_0 a^3}{15}$$

Contrôle : c'est $\frac{2}{5}$ de la charge $\frac{4}{3}\pi a^3 \rho_0$ qu'aurait une boule uniforme de densité $\rho_0$, ce qui est cohérent puisque $\rho$ décroît de $\rho_0$ au centre à $0$ au bord.

## Exercice 4 : Masse volumique de la Terre

**Énoncé.** On peut supposer, dans un modèle grossier, que la répartition de la masse de la Terre (assimilée à une sphère de rayon $R$) n'est pas uniforme : le noyau terrestre, principalement formé de fer et de nickel, est plus dense que la croûte. La masse volumique $\rho$ dépend donc de la distance $r$ au centre $C$ :
$$\rho(r) = \rho_0 \left(1 - \frac{r}{2R}\right)$$

Données : la densité du fer vaut environ 8 et celle des roches granitiques vaut environ 4.

1. Exprimer la masse $M$ de la Terre en fonction de $R$ et $\rho_0$.
2. Calculer numériquement la masse volumique au centre et à la surface de la Terre. Commenter. On donne $M = 6{,}0 \times 10^{24}\ \mathrm{kg}$ et $R = 6{,}4 \times 10^{3}\ \mathrm{km}$.

**Correction.**

**1.** Même méthode qu'à l'exercice 6, avec $\rho = \dfrac{dm}{dV}$ :
$$M = \iiint_{\text{Terre}} \rho(r)\,dV = \int_0^R \rho_0 \Big(1 - \frac{r}{2R}\Big) r^2\,dr \times \int_0^\pi \sin\theta\,d\theta \times \int_0^{2\pi} d\varphi$$

$$I_r = \rho_0 \int_0^R \Big(r^2 - \frac{r^3}{2R}\Big) dr = \rho_0 \Big(\frac{R^3}{3} - \frac{R^3}{8}\Big) = \frac{5}{24}\rho_0 R^3$$

$$M = \frac{5}{24}\rho_0 R^3 \times 4\pi = \frac{5\pi}{6}\rho_0 R^3$$

**2.** On en tire $\rho_0 = \dfrac{6M}{5\pi R^3}$, avec $R = 6{,}4 \times 10^6\ \mathrm{m}$ :
$$\rho_0 = \frac{6 \times 6{,}0 \times 10^{24}}{5\pi \times (6{,}4 \times 10^6)^3} = \frac{3{,}6 \times 10^{25}}{4{,}12 \times 10^{21}} \approx 8{,}7 \times 10^3\ \mathrm{kg \cdot m^{-3}}$$

- au centre : $\rho(0) = \rho_0 \approx 8\,742\ \mathrm{kg \cdot m^{-3}}$, soit une densité d'environ $8{,}7$, proche de celle du fer ($8$) ;
- à la surface : $\rho(R) = \rho_0/2 \approx 4\,371\ \mathrm{kg \cdot m^{-3}}$, soit une densité d'environ $4{,}4$, proche de celle des roches granitiques ($4$).

Le modèle, bien que grossier, est donc cohérent avec la composition de la Terre (noyau métallique dense, croûte rocheuse plus légère).

## Exercice 3 : Distribution discrète de charges ponctuelles

**Énoncé.** Quatre charges électriques ponctuelles, de valeur absolue $q$, sont placées aux sommets d'un carré $ABCD$ de côté $2a$, de centre $O$ et appartenant au plan $Oxz$. Déterminer l'expression de la force subie par la charge électrique $Q$ placée en un point $M$ quelconque de l'axe $Oy$.

> **Note :** la figure montre les charges $+q$ en $A(a, 0, a)$ et $C(-a, 0, -a)$, $-q$ en $B(a, 0, -a)$ et $D(-a, 0, a)$, et la charge $Q$ en $M(0, y, 0)$ sur l'axe $Oy$ ; les quatre forces exercées sur $Q$ y sont dessinées.

**Correction.** *Par le calcul.* La force totale est la somme des quatre forces de Coulomb :
$$\vec F = \vec F_{A \to M} + \vec F_{B \to M} + \vec F_{C \to M} + \vec F_{D \to M}, \qquad \vec F_{A \to M} = \frac{1}{4\pi\varepsilon_0} \frac{q_A Q}{AM^3}\,\overrightarrow{AM}$$

et de même pour les autres. Les quatre sommets sont à la même distance de $M$ :
$$AM = BM = CM = DM = r = \big(2a^2 + y^2\big)^{1/2}$$

Avec $\overrightarrow{AM} = (-a, y, -a)$, $\overrightarrow{BM} = (-a, y, a)$, $\overrightarrow{CM} = (a, y, a)$, $\overrightarrow{DM} = (a, y, -a)$ et $q_A = q_C = +q$, $q_B = q_D = -q$ :
$$\vec F = \frac{qQ}{4\pi\varepsilon_0 r^3}\Big[\overrightarrow{AM} - \overrightarrow{BM} + \overrightarrow{CM} - \overrightarrow{DM}\Big]$$

- selon $x$ : $-a + a + a - a = 0$ ;
- selon $y$ : $y - y + y - y = 0$ ;
- selon $z$ : $-a - a + a + a = 0$.

Donc $\vec F = \vec 0$ pour tout point $M$ de l'axe $Oy$.

*Par les symétries.* Le plan $P_1 = (M, \vec e_y, \vec e_z)$ (plan $x = 0$) échange $A(+q)$ et $D(-q)$, $B(-q)$ et $C(+q)$ : c'est un plan d'**antisymétrie** de la distribution. De même, le plan $P_2 = (M, \vec e_x, \vec e_y)$ (plan $z = 0$) échange $A(+q)$ et $B(-q)$, $C(+q)$ et $D(-q)$ : plan d'antisymétrie. En un point d'un plan d'antisymétrie, le champ électrique est perpendiculaire à ce plan. En $M \in P_1 \cap P_2$, $\vec E(M)$ devrait donc être à la fois selon $\vec e_x$ et selon $\vec e_z$ : la seule possibilité est $\vec E(M) = \vec 0$, et donc $\vec F = Q\,\vec E(M) = \vec 0$.
