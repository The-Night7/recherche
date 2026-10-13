---
source: TD3-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 8 (correction manuscrite)
transcription: manuelle
---

# TD3 — Potentiel électrique (corrigé)

> **Note :** la correction suit l'ordre 1, 2, 3, 6, 4, 5 et la numérotation de la feuille 2022-2023, conservés ici. Dans le recueil 2023-2024, les exercices 1 et 2 sont regroupés dans l'exercice 5, et les exercices 3, 6, 4, 5 sont devenus 1, 3, 4, 2.

## Exercice 1 : Coordonnées d'un gradient

**Énoncé.** Déterminer les coordonnées de $\overrightarrow{\operatorname{grad}} f$ où $f$ est le champ scalaire suivant :

1. $f(x, y, z) = xy^2 - yz^2$
2. $f(x, y, z) = xyz \sin(xy)$

**Correction.** Pour un champ scalaire $f(x, y, z)$, la différentielle s'écrit
$$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz = \overrightarrow{\operatorname{grad}} f \cdot d\vec\ell$$

avec, en coordonnées cartésiennes, $d\vec\ell = (dx, dy, dz)$ et $\overrightarrow{\operatorname{grad}} f = \Big(\dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}, \dfrac{\partial f}{\partial z}\Big)$. Chaque dérivée partielle se calcule en gardant les deux autres variables constantes.

**1.** $f = xy^2 - yz^2$ :

- $\dfrac{\partial f}{\partial x} = y^2$ ;
- $\dfrac{\partial f}{\partial y} = 2xy - z^2$ ;
- $\dfrac{\partial f}{\partial z} = -2yz$.

**2.** $f = xyz\sin(xy)$ : on dérive un produit, et $\frac{\partial}{\partial x}\sin(xy) = y\cos(xy)$, $\frac{\partial}{\partial y}\sin(xy) = x\cos(xy)$ :

- $\dfrac{\partial f}{\partial x} = yz\sin(xy) + xy^2 z\cos(xy)$ ;
- $\dfrac{\partial f}{\partial y} = xz\sin(xy) + x^2 yz\cos(xy)$ ;
- $\dfrac{\partial f}{\partial z} = xy\sin(xy)$.

## Exercice 2 : Gradient de x² + y² + z²

**Énoncé.** On donne le champ scalaire $f(x, y, z) = x^2 + y^2 + z^2$. Calculer $\overrightarrow{\operatorname{grad}} f$.

**Correction.** *En coordonnées cartésiennes :*
$$\overrightarrow{\operatorname{grad}} f = (2x, 2y, 2z) = 2\,\overrightarrow{OM}$$

*En coordonnées sphériques :* $f = r^2$ ne dépend que de $r$. Avec
$$\overrightarrow{\operatorname{grad}} f = \frac{\partial f}{\partial r}\vec e_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec e_\theta + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \varphi}\vec e_\varphi$$

on trouve $\overrightarrow{\operatorname{grad}} f = 2r\,\vec e_r = 2\,\overrightarrow{OM}$ : les deux calculs concordent.

## Exercice 3 : Champ d'une charge ponctuelle à partir du potentiel

**Énoncé.** Le potentiel créé par une charge ponctuelle en un point $M$, situé à la distance $r$ de la charge $q$, est :
$$V(M) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$$

Calculer le champ électrostatique $\vec E$ qui dérive du potentiel $V$.

**Correction.** Par définition, $\vec E = -\overrightarrow{\operatorname{grad}} V$. En coordonnées sphériques centrées sur la charge (placée en $P$), $V$ ne dépend que de $r$ :

- $E_r = -\dfrac{\partial V}{\partial r} = -\dfrac{q}{4\pi\varepsilon_0}\dfrac{d}{dr}\Big(\dfrac{1}{r}\Big) = \dfrac{q}{4\pi\varepsilon_0 r^2}$ ;
- $E_\theta = -\dfrac{1}{r}\dfrac{\partial V}{\partial \theta} = 0$ ;
- $E_\varphi = -\dfrac{1}{r\sin\theta}\dfrac{\partial V}{\partial \varphi} = 0$.

$$\vec E = \frac{q}{4\pi\varepsilon_0 r^2}\,\vec e_r = \frac{q}{4\pi\varepsilon_0 r^2}\,\vec u_{PM}$$

On retrouve la loi de Coulomb.

## Exercice 6 : Potentiel d'une sphère chargée en surface

**Énoncé.** Reprendre l'exercice 8 du TD2 de la sphère chargée uniformément en surface de densité $\sigma$ et calculer le potentiel engendré par une telle distribution en tout point de l'espace.

**Correction.** *Rappel du TD2 :* $\vec E = E(r)\,\vec u_r$ avec

- $r < R$ : $q_{\text{int}} = 0$, donc $E = 0$ ;
- $r > R$ : $q_{\text{int}} = Q = 4\pi R^2\sigma$, donc $E = \dfrac{\sigma}{\varepsilon_0}\dfrac{R^2}{r^2}$,

avec une discontinuité à la traversée de la surface chargée.

*Potentiel.* En coordonnées sphériques, $\vec E = -\overrightarrow{\operatorname{grad}} V$ donne
$$-\frac{\partial V}{\partial r} = E(r), \qquad -\frac{1}{r}\frac{\partial V}{\partial \theta} = 0, \qquad -\frac{1}{r\sin\theta}\frac{\partial V}{\partial \varphi} = 0$$

donc $V = V(r)$ et $\dfrac{dV}{dr} = -E(r)$. Le potentiel n'est défini qu'à une constante près : il y a une constante d'intégration dans chaque région.

- $r < R$ : $\dfrac{dV}{dr} = 0$, donc $V = K_1$ (constante) ;
- $r > R$ : $\dfrac{dV}{dr} = -\dfrac{\sigma R^2}{\varepsilon_0 r^2}$, donc $V = \dfrac{\sigma R^2}{\varepsilon_0 r} + K_2$.

*Conditions pour fixer les constantes :*

- pour une distribution **surfacique**, le potentiel est défini sur la surface et **continu** à sa traversée : $V(R^-) = V(R^+)$, soit $K_1 = \dfrac{\sigma R}{\varepsilon_0} + K_2$ ;
- la distribution est bornée (pas de charges à l'infini) : on peut prendre $V(\infty) = 0$, d'où $K_2 = 0$.

$$V(r \le R) = \frac{\sigma R}{\varepsilon_0}, \qquad V(r \ge R) = \frac{\sigma R^2}{\varepsilon_0 r}$$

*Remarques.*

- Pour $r \gg R$, la sphère se comporte comme une charge ponctuelle $Q = 4\pi R^2\sigma$ : $V = \dfrac{Q}{4\pi\varepsilon_0 r}$, ce qui est bien le cas.
- Analyse dimensionnelle : $[V] = [E]\,L = \dfrac{[q]}{[\varepsilon_0]L^2}L$, et avec $\sigma = \dfrac{dq}{dS}$, $\Big[\dfrac{\sigma R}{\varepsilon_0}\Big] = \dfrac{[q]}{L^2[\varepsilon_0]}L$ : c'est homogène.

> **Note :** la correction trace $E(r)$ (nul pour $r < R$, saut à $\frac{\sigma}{\varepsilon_0}$ puis décroissance en $1/r^2$) et, sur la même figure, $-E$.

## Exercice 4 : Symétrie axiale

**Énoncé.** (*) Un champ de vecteur $\vec E$ dérive d'un potentiel $V$ qui a la symétrie de révolution autour de l'axe $(Oz)$. On se place dans un plan contenant l'axe $(Oz)$. Dans ce plan, on adopte les coordonnées polaires, et l'on pose $\theta = (\overrightarrow{Oz}, \overrightarrow{OM})$. Le potentiel $V$ a alors pour expression :
$$V = \frac{K}{r^3}\left(3\cos^2\theta - 1\right)$$

Déterminer les composantes du champ $\vec E$.

**Correction.** $\theta$ est l'angle des coordonnées sphériques, avec $d\overrightarrow{OM} = dr\,\vec e_r + r\,d\theta\,\vec e_\theta + r\sin\theta\,d\varphi\,\vec e_\varphi$, et $V(r, \theta)$ ne dépend pas de $\varphi$. Dans le plan considéré, $\vec E = -\overrightarrow{\operatorname{grad}} V$ a deux composantes. Avec $\frac{d}{dr}(r^{-3}) = -3r^{-4}$ et $\frac{d}{d\theta}(\cos^2\theta) = -2\sin\theta\cos\theta$ :
$$E_r = -\frac{\partial V}{\partial r} = -K(-3)r^{-4}(3\cos^2\theta - 1) = \frac{3K}{r^4}(3\cos^2\theta - 1)$$

$$E_\theta = -\frac{1}{r}\frac{\partial V}{\partial \theta} = -\frac{K}{r^4} \times 3 \times 2(-\sin\theta)\cos\theta = \frac{3K}{r^4}(2\sin\theta\cos\theta)$$

(et $E_\varphi = 0$). Contrôle dimensionnel : $[V] = [E]\,L$, donc $[E] = [V]/L$ ; ici $V \propto K/r^3$ et $E \propto K/r^4$ : c'est cohérent.

## Exercice 5 : Symétrie cylindrique

**Énoncé.** Soit un cylindre de rayon $R$ et de hauteur infinie. Déterminer le potentiel électrostatique créé par la distribution surfacique de charges de densité $\sigma$ répartie uniformément sur la surface de ce cylindre.

> **Note :** l'énoncé imprimé dans la correction dit « répartie uniformément dans ce cylindre », mais parle d'une densité surfacique $\sigma$ ; la correction traite bien une charge répartie sur la surface.

**Correction.**

*Définition et continuité :* $\sigma = \dfrac{dq}{dS}$ est surfacique, donc $\vec E$ est défini et continu partout sauf à la traversée de la surface chargée ; $V$ est défini et continu partout, même sur la surface.

*Coordonnées :* cylindriques $\{O, (\vec e_r, \vec e_\theta, \vec e_z)\}$ ; a priori $\vec E(r, \theta, z)$.

*Invariances :* le cylindre est infini selon $Oz$ (invariance par translation selon $\vec e_z$) et uniformément chargé (invariance par rotation autour de $Oz$) : $\vec E = \vec E(r)$.

*Symétries :* $\vec E$ appartient à tout plan de symétrie et est perpendiculaire à tout plan d'antisymétrie. $P_1 = (M, \vec e_r, \vec e_\theta)$ et $P_2 = (M, \vec e_r, \vec e_z)$ sont plans de symétrie ; le plan $(M, \vec e_z, \vec e_\theta)$, tangent au cylindre passant par $M$, n'en est pas un. $\vec E \in P_1 \cap P_2$ :
$$\vec E = E(r)\,\vec e_r \quad \text{(champ radial)}$$

> **Erreur corrigée :** la correction écrit $\vec E \in (P_1 \cup P_2)$ ; c'est l'intersection $P_1 \cap P_2$, de direction $\vec e_r$.

*Théorème de Gauss.* Surface de Gauss : cylindre fermé $S_G$ de même axe, de hauteur $h$ et de rayon $r$ (bases $S_1$, $S_2$, surface latérale $S_3$). Le flux à travers les bases est nul ($\vec E \perp \vec n$), et sur $S_3$, $dS_r = r\,d\theta\,dz$ :
$$\Phi(\vec E) = \int_0^{2\pi}\int_{-h/2}^{h/2} E(r)\,r\,d\theta\,dz = 2\pi r h\,E(r)$$

*Charge intérieure :*

- $r < R$ : $q_{\text{int}} = 0$ ;
- $r > R$ : $q_{\text{int}}$ est la charge d'une portion de hauteur $h$ de la surface chargée, $q_{\text{int}} = \sigma \times 2\pi R h$.

Donc
$$\vec E(r < R) = \vec 0, \qquad \vec E(r > R) = \frac{\sigma}{\varepsilon_0}\frac{R}{r}\,\vec e_r$$

(homogène : $[E] = \frac{[\sigma]}{[\varepsilon_0]} = \frac{[q]}{L^2[\varepsilon_0]}$).

*Potentiel.* $\vec E = -\overrightarrow{\operatorname{grad}} V$ donne $\frac{\partial V}{\partial \theta} = \frac{\partial V}{\partial z} = 0$, donc $V = V(r)$, et $E_r = -\dfrac{dV}{dr}$ :

- (1) $0 \le r < R$ : $\dfrac{dV}{dr} = 0$, donc $V = K_1$ ;
- (2) $r > R$ : $\dfrac{dV}{dr} = -\dfrac{\sigma R}{\varepsilon_0 r}$, donc
$$V(r) = -\frac{\sigma R}{\varepsilon_0}\int_R^r \frac{du}{u} + K_2 = -\frac{\sigma R}{\varepsilon_0}\ln\frac{r}{R} + K_2 = \frac{\sigma R}{\varepsilon_0}\ln\frac{R}{r} + K_2$$

*Conditions aux limites.* On ne peut **pas** imposer $V(\infty) = 0$ : la distribution s'étend à l'infini (cylindre de hauteur infinie), et $\ln(R/r) \to -\infty$. Il ne reste que la continuité en $r = R$ : $V(R^-) = V(R^+)$ donne $K_1 = K_2$ (car $\ln 1 = 0$). Il reste une constante arbitraire $K_1$ :
$$V(r \le R) = K_1, \qquad V(r \ge R) = K_1 + \frac{\sigma R}{\varepsilon_0}\ln\frac{R}{r}$$

(Si l'on intègre sans bornes, $V = -\frac{\sigma R}{\varepsilon_0}\ln r + K_2$, et la continuité donne $K_2 = K_1 + \frac{\sigma R}{\varepsilon_0}\ln R$ : même résultat.)

> **Note :** la correction trace $E(r)$ (nul pour $r < R$, saut à $\frac{\sigma}{\varepsilon_0}$ en $R$, puis décroissance en $1/r$) et $V(r)$ (constant égal à $K_1$ pour $r \le R$, puis décroissant comme $\ln(1/r)$ si $\sigma > 0$).
