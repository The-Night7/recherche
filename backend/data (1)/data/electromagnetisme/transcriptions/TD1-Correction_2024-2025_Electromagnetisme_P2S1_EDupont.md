---
source: TD1-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 8 (correction manuscrite) ; énoncé de l'exercice 5 : TD_2024-2025_Electromagnetisme_P2S1_DPhysique.pdf, page 6
transcription: manuelle
---

# TD1 — Distributions continues (corrigé)

> **Note :** par rapport à la correction 2022-2023, les exercices sont renumérotés (la distribution discrète de charges est passée au TD2) et les calculs sont les mêmes. La correction 2024-2025 s'arrête à l'exercice 4 ; la correction de l'exercice 5 a été rédigée pour cette transcription.

## Exercice 1 : Calculs d'aire et de volume

**Énoncé.** En choisissant le système de coordonnées approprié :

1. Calculer, en utilisant une intégrale double, la surface d'un disque de rayon $R$.
2. Calculer, en utilisant une intégrale double, la surface de la paroi latérale d'un cylindre de hauteur $h$ et de rayon $R$.
3. Calculer, en utilisant une intégrale triple, le volume d'un cylindre de hauteur $h$ et de rayon $R$.

**Correction.** Les trois objets ont un axe de révolution $(Oz)$ : on utilise les **coordonnées cylindriques**, de repère $\{O ; (\vec e_\rho, \vec e_\theta, \vec e_z)\}$. En notant $m$ le projeté de $M$ sur le plan $(Oxy)$ :
$$\overrightarrow{OM} = \overrightarrow{Om} + \overrightarrow{mM} = \rho\,\vec e_\rho + z\,\vec e_z$$

(le vecteur $\vec e_\rho$ varie avec $M$, le vecteur $\vec e_z$ est fixe).

*Rappel.* Si $\vec c = \vec a \wedge \vec b$, alors $\|\vec c\| = \|\vec a\|\,\|\vec b\|\,|\sin(\vec a, \vec b)|$ est l'aire du parallélogramme construit sur $\vec a$ et $\vec b$ ; pour deux vecteurs d'une base orthonormée directe, $\sin = 1$ et l'aire est le produit des longueurs.

Le déplacement élémentaire est $d\overrightarrow{OM} = d\rho\,\vec e_\rho + \rho\,d\theta\,\vec e_\theta + dz\,\vec e_z$. En multipliant deux à deux les déplacements élémentaires, on obtient les éléments de surface :

- $dS_\rho = \rho\,d\theta\,dz$ (normale $\vec e_\rho$) ;
- $dS_\theta = dz\,d\rho$ (normale $\vec e_\theta$) ;
- $dS_z = \rho\,d\theta\,d\rho$ (normale $\vec e_z$).

> **Note :** les figures montrent le repère cylindrique, un petit volume élémentaire avec ses trois faces $dS_\rho$, $dS_\theta$, $dS_z$, le cylindre entre $z = -h/2$ et $z = h/2$ et sa paroi latérale déroulée en rectangle $h \times 2\pi R$.

**1.** Les variables $\rho$, $\theta$ sont séparables :
$$S = \iint_{\text{disque}} dS_z = \left(\int_0^R \rho\,d\rho\right)\left(\int_0^{2\pi} d\theta\right) = \frac{R^2}{2} \times 2\pi = \pi R^2$$

**2.** Sur la paroi latérale, $\rho = R$ est fixé :
$$S = \iint dS_\rho = R \left(\int_0^{2\pi} d\theta\right)\left(\int_{-h/2}^{h/2} dz\right) = R \times 2\pi \times h = (2\pi R)\,h$$

soit le périmètre $2\pi R$ multiplié par la hauteur $h$.

**3.** Le volume élémentaire est $dV = d\rho\,(\rho\,d\theta)\,dz$ :
$$V = \left(\int_0^R \rho\,d\rho\right)\left(\int_0^{2\pi} d\theta\right)\left(\int_{-h/2}^{h/2} dz\right) = \frac{R^2}{2} \times 2\pi \times h = (\pi R^2)\,h$$

c'est-à-dire la surface de la base fois la hauteur.

## Exercice 2 : Calculs de charge totale

**Énoncé.** En choisissant le système de coordonnées approprié :

1. Calculer la charge totale contenue dans un fil de longueur $L$ uniformément chargé dont la densité linéique vaut $\lambda_0$.
2. Calculer la charge totale contenue dans un disque de rayon $R$ uniformément chargé en surface dont la densité surfacique vaut $\sigma_0$.
3. Calculer la charge totale contenue dans une boule de rayon $R$ uniformément chargée en volume dont la densité volumique vaut $\rho_0$.

**Correction.**

**1.** Un élément $d\ell$ du fil, autour du point $P$, porte la charge élémentaire $dq$. Par définition, la **densité linéique de charge** est
$$\lambda(P) = \frac{dq}{d\ell} \quad (\mathrm{C \cdot m^{-1}})$$

Ici le fil est uniformément chargé : $\lambda = \lambda_0$ constante, donc
$$Q = \int_{\text{fil}} dq = \int_0^L \lambda_0\,d\ell = \lambda_0 L$$

**2.** Densité surfacique : $\sigma = \dfrac{dq}{dS}$ ($\mathrm{C \cdot m^{-2}}$), ici constante égale à $\sigma_0$. Avec $\rho \in [0, R]$ et $\theta \in [0, 2\pi]$ :
$$Q = \iint_{\text{disque}} \sigma_0\,dS_z = \sigma_0 \iint_{\text{disque}} dS_z = \sigma_0\,\pi R^2$$

**3.** On utilise les **coordonnées sphériques**, de repère $\{O ; (\vec e_r, \vec e_\theta, \vec e_\varphi)\}$, avec $\overrightarrow{OM} = r\,\vec e_r$, $r = OM$. Le déplacement élémentaire $d\vec\ell = \overrightarrow{MM'}$ vers un point $M'$ infiniment proche vaut
$$d\overrightarrow{OM} = dr\,\vec e_r + r\,d\theta\,\vec e_\theta + r\sin\theta\,d\varphi\,\vec e_\varphi$$

($r\sin\theta = HM$ est la distance de $M$ à l'axe $(Oz)$). D'où :

- $dS_r = d\ell_\theta\,d\ell_\varphi = r^2 \sin\theta\,d\theta\,d\varphi$ ;
- $dS_\theta = d\ell_r\,d\ell_\varphi = r\sin\theta\,dr\,d\varphi$ ;
- $dS_\varphi = d\ell_\theta\,d\ell_r = r\,dr\,d\theta$ ;
- $dV = d\ell_r\,d\ell_\theta\,d\ell_\varphi = (r^2\,dr)(\sin\theta\,d\theta)\,d\varphi$,

avec $\theta \in [0, \pi]$ et $\varphi \in [0, 2\pi]$. Volume de la boule (variables séparables, $\frac{d\cos\theta}{d\theta} = -\sin\theta$) :
$$V = \left[\frac{r^3}{3}\right]_0^R \big[-\cos\theta\big]_0^\pi \big[\varphi\big]_0^{2\pi} = \frac{R^3}{3} \times 2 \times 2\pi = \frac{4}{3}\pi R^3$$

La densité volumique est $\rho(P) = \dfrac{dq}{dV}$ ($\mathrm{C \cdot m^{-3}}$), ici $\rho = \rho_0$ constante :
$$Q = \iiint_{\text{boule}} \rho_0\,dV = \rho_0 V = \frac{4}{3}\pi R^3 \rho_0$$

*Remarque sur l'homogénéité.* Pour une charge ponctuelle $q$, la loi de Coulomb donne $\vec E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}\vec u$, où $\vec u$ est unitaire (sans dimension) et $4\pi$ sans dimension. Donc
$$[E] = \frac{[q]}{[\varepsilon_0]\,L^2}$$

Toute expression de champ doit avoir cette dimension ; c'est un bon moyen de contrôler un résultat.

## Exercice 3 : Charge totale d'une distribution surfacique

**Énoncé.** On considère une sphère de centre $O$ et de rayon $R$ portant en sa surface une densité de charges
$$\sigma = \sigma_0 (1 + \cos\theta)$$

où $\theta = (\overrightarrow{Oz}, \overrightarrow{OP})$. Calculer la charge totale portée par la distribution.

**Correction.** La densité $\sigma(\theta)$ n'est pas uniforme : deux points $P_1$ et $P_2$ de la sphère d'angles $\theta_1 \ne \theta_2$ n'ont pas la même densité. On utilise les coordonnées sphériques, avec $r = R$ constant sur la sphère :
$$Q = \iint_{P \in S} \sigma(\theta)\,dS_r = \int_0^\pi \int_0^{2\pi} \sigma_0 (1 + \cos\theta)\,R^2 \sin\theta\,d\theta\,d\varphi = \sigma_0 R^2\, I_\theta \times 2\pi$$

*Première méthode.* On sépare les deux termes :
$$I_\theta = \int_0^\pi \sin\theta\,d\theta + \int_0^\pi \cos\theta \sin\theta\,d\theta = \big[-\cos\theta\big]_0^\pi + \int_{-1}^{1} u\,du = 2 + 0 = 2$$

(changement de variable $u = \cos\theta$, $du = -\sin\theta\,d\theta$ dans la deuxième intégrale).

*Deuxième méthode.* Avec le même changement de variable directement :
$$I_\theta = -\int_{1}^{-1} (1 + u)\,du = -\left[u + \frac{u^2}{2}\right]_1^{-1} = -\Big[\Big(-1 + \frac{1}{2}\Big) - \Big(1 + \frac{1}{2}\Big)\Big] = 2$$

**Conclusion :**
$$Q = \sigma_0 R^2 \times 2 \times 2\pi = 4\pi R^2 \sigma_0$$

C'est le même résultat que pour une densité uniforme $\sigma_0$, car $\int_0^\pi \cos\theta \sin\theta\,d\theta = 0$ : la surcharge de l'hémisphère nord compense exactement le déficit de l'hémisphère sud.

## Exercice 4 : Noyaux atomiques

**Énoncé.** (*) Du point de vue du potentiel et du champ électrique qu'ils créent, les noyaux de certains atomes légers peuvent être modélisés par une distribution volumique de charge à l'intérieur d'une sphère de centre $O$ et de rayon $a$. On désigne par $\vec r = \overrightarrow{OP}$ le vecteur position d'un point $P$ quelconque de l'espace. Pour $r < a$, la charge volumique $\rho(P)$ qui représente le noyau varie en fonction de $r$ suivant la loi :
$$\rho(r) = \rho_0 \left(1 - \frac{r^2}{a^2}\right)$$

où $\rho_0$ est une constante positive.

1. Donner les symétries et invariances de cette distribution de charges.
2. Exprimer la charge totale $Q$ du noyau.

**Correction.** Le volume $dV$ autour de $P$ porte la charge $dq = \rho(P)\,dV$.

**1.** *Choix des coordonnées :* coordonnées sphériques de centre $O$. A priori, le champ créé en $M$ s'écrit $\vec E = \vec E(r, \theta, \varphi)$.

*Invariances :* $\rho$ ne dépend ni de $\theta$ ni de $\varphi$ ; la distribution est invariante par rotation autour de $O$, donc $\vec E(r, \theta, \varphi) = \vec E(r)$.

*Symétries :* $\rho(\vec r) = \rho(-\vec r)$ et, plus généralement, tout plan passant par le centre $O$ est un plan de symétrie de la distribution (la densité décroît avec $r$ : $\rho(r_1) < \rho(r_2)$ si $r_1 > r_2$, mais elle est la même sur chaque sphère de centre $O$). Le champ en $M$ appartient à tous les plans de symétrie passant par $M$ (plans $P_1$, $P_2$, … contenant $(OM)$), donc
$$\vec E = E(r)\,\vec e_r$$

> **Note :** la correction manuscrite ajoute « $E(r)$ décroît avec $r$ ». Ce n'est vrai qu'à l'extérieur du noyau : par le théorème de Gauss (vu plus tard), pour $r < a$ on trouve $E(r) = \frac{\rho_0}{\varepsilon_0}\big(\frac{r}{3} - \frac{r^3}{5a^2}\big)$, qui est nul au centre, croît jusqu'à $r = a\sqrt{5}/3 \approx 0{,}75\,a$, puis décroît.

**2.** Pour $r > a$, $\rho = 0$ (vide) : on n'intègre que sur $r < a$.
$$Q = \iiint_{r < a} \rho(r)\,r^2 \sin\theta\,dr\,d\theta\,d\varphi = \left(\int_0^a \rho_0 \Big(1 - \frac{r^2}{a^2}\Big) r^2\,dr\right) \left(\int_0^\pi \sin\theta\,d\theta\right)\left(\int_0^{2\pi} d\varphi\right)$$

$$I_r = \int_0^a \Big(r^2 - \frac{r^4}{a^2}\Big) dr = \left[\frac{r^3}{3} - \frac{r^5}{5a^2}\right]_0^a = a^3\Big(\frac{1}{3} - \frac{1}{5}\Big) = \frac{2a^3}{15}$$

$$Q = \rho_0 I_r \times 4\pi = \frac{8\pi \rho_0 a^3}{15}$$

Homogénéité : $\rho = \dfrac{dq}{dV}$ donc $[Q] = [\rho]\,L^3$, ce qui est bien le cas.

## Exercice 5 : Masse volumique de la Terre

**Énoncé.** On peut supposer, dans un modèle grossier, que la répartition de la masse de la Terre (assimilée à une sphère de rayon $R$) n'est pas uniforme : le noyau terrestre, principalement formé de fer et de nickel, est plus dense que la croûte. La masse volumique $\rho$ dépend donc de la distance $r$ au centre $C$ :
$$\rho(r) = \rho_0 \left(1 - \frac{r}{2R}\right)$$

Données : la densité du fer vaut environ 8 et celle des roches granitiques vaut environ 4.

1. Exprimer la masse $M$ de la Terre en fonction de $R$ et $\rho_0$.
2. Calculer numériquement la masse volumique au centre et à la surface de la Terre. Commenter. On donne $M = 6{,}0 \times 10^{24}\ \mathrm{kg}$ et $R = 6{,}4 \times 10^{3}\ \mathrm{km}$.

**Correction.**

> **Complément :** la correction 2024-2025 ne traite pas cet exercice ; la correction ci-dessous reprend celle de 2022-2023 (où il portait le numéro 4), vérifiée.

**1.** Avec $\rho = \dfrac{dm}{dV}$ et les coordonnées sphériques :
$$M = \iiint_{\text{Terre}} \rho(r)\,dV = \int_0^R \rho_0 \Big(1 - \frac{r}{2R}\Big) r^2\,dr \times \int_0^\pi \sin\theta\,d\theta \times \int_0^{2\pi} d\varphi$$

$$\int_0^R \Big(r^2 - \frac{r^3}{2R}\Big) dr = \frac{R^3}{3} - \frac{R^3}{8} = \frac{5}{24}R^3$$

$$M = \frac{5}{24}\rho_0 R^3 \times 4\pi = \frac{5\pi}{6}\rho_0 R^3$$

**2.** $\rho_0 = \dfrac{6M}{5\pi R^3}$ avec $R = 6{,}4 \times 10^6\ \mathrm{m}$ :
$$\rho_0 = \frac{6 \times 6{,}0 \times 10^{24}}{5\pi \times (6{,}4 \times 10^6)^3} \approx 8{,}7 \times 10^3\ \mathrm{kg \cdot m^{-3}}$$

- au centre : $\rho(0) = \rho_0 \approx 8\,740\ \mathrm{kg \cdot m^{-3}}$ (densité $\approx 8{,}7$, proche de celle du fer) ;
- à la surface : $\rho(R) = \rho_0/2 \approx 4\,370\ \mathrm{kg \cdot m^{-3}}$ (densité $\approx 4{,}4$, proche de celle des roches granitiques).

Ce modèle grossier reproduit bien l'ordre de grandeur attendu : un cœur métallique dense et une croûte rocheuse environ deux fois moins dense.
