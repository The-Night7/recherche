---
source: TD3-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf, pages 1 à 5 (correction manuscrite)
transcription: manuelle
---

# TD3 — Potentiel électrostatique (corrigé)

> **Note :** la correction traite les exercices dans l'ordre 1, 2, 5, 3, 4, conservé ici. Les calculs sont ceux de la correction 2022-2023 (où ces exercices portaient les numéros 1-2, 3, 4, 6 et 5), en plus condensé ; la seule différence de fond est la discussion des symétries à l'exercice 1.

## Exercice 1 : Coordonnées de gradients

**Énoncé.** Déterminer les coordonnées de $\overrightarrow{\operatorname{grad}} f$ où $f$ est le champ scalaire suivant :

1. $f(x, y, z) = xy^2 - yz^2$
2. $f(x, y, z) = xyz \times \sin(xy)$
3. On donne le champ scalaire $f(x, y, z) = x^2 + y^2 + z^2$. Calculer $\overrightarrow{\operatorname{grad}} f$. Discuter les symétries et invariances des champs $f$ et $\overrightarrow{\operatorname{grad}} f$.

**Correction.** Par définition, $df = \overrightarrow{\operatorname{grad}} f \cdot d\vec\ell$. En coordonnées cartésiennes, $d\vec\ell = (dx, dy, dz)$ et les composantes du gradient sont les dérivées partielles $\big(\frac{\partial f}{\partial x}\big)_{y,z}$, $\big(\frac{\partial f}{\partial y}\big)_{x,z}$, $\big(\frac{\partial f}{\partial z}\big)_{x,y}$ (les variables en indice sont gardées constantes).

**1.** $f = xy^2 - yz^2$ :
$$\overrightarrow{\operatorname{grad}} f = \big(y^2,\ 2xy - z^2,\ -2yz\big)$$

**2.** $f = xyz\sin(xy)$ (dérivée d'un produit) :

- $\dfrac{\partial f}{\partial x} = yz\sin(xy) + xyz \times y\cos(xy) = yz\sin(xy) + xy^2 z\cos(xy)$ ;
- $\dfrac{\partial f}{\partial y} = xz\sin(xy) + xyz \times x\cos(xy) = xz\sin(xy) + x^2 yz\cos(xy)$ ;
- $\dfrac{\partial f}{\partial z} = xy\sin(xy)$.

**3.** En cartésiennes : $\overrightarrow{\operatorname{grad}} f = (2x, 2y, 2z) = 2\,\overrightarrow{OM}$.

En sphériques, $r^2 = x^2 + y^2 + z^2$, donc $f = r^2$ et, avec $d\vec\ell = (dr, r\,d\theta, r\sin\theta\,d\varphi)$ :
$$\overrightarrow{\operatorname{grad}} f = \frac{\partial f}{\partial r}\vec e_r + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec e_\theta + \frac{1}{r\sin\theta}\frac{\partial f}{\partial \varphi}\vec e_\varphi = 2r\,\vec e_r = 2\,\overrightarrow{OM}$$

*Symétries et invariances.*

- $f$ ne dépend que de $r$ : il est invariant par toute rotation autour de $O$ (variations de $\theta$ et $\varphi$), et symétrique par rapport à $O$ ($x \to -x$, $y \to -y$, $z \to -z$ laisse $f$ inchangé).
- $\overrightarrow{\operatorname{grad}} f = 2r\,\vec e_r$ a une norme $2r$ qui ne dépend que de $r$, mais sa direction $\vec e_r$ change avec $\theta$ et $\varphi$. C'est un champ **radial** qui a la même symétrie sphérique que $f$ : tout plan passant par $O$ et $M$ contient le vecteur $\overrightarrow{\operatorname{grad}} f(M)$. Par la symétrie de centre $O$, il est changé en son opposé : $\overrightarrow{\operatorname{grad}} f(-\overrightarrow{OM}) = -\overrightarrow{\operatorname{grad}} f(\overrightarrow{OM})$.

> **Note :** la correction manuscrite résume en disant que $\overrightarrow{\operatorname{grad}} f$ « dépend de $\theta$ et $\varphi$ » et n'a « pas de symétrie ». C'est à nuancer : seule la direction de $\vec e_r$ dépend de $\theta$ et $\varphi$, et le champ de gradient a la même symétrie sphérique que $f$ (c'est d'ailleurs ce qu'on utilise pour dire qu'un champ électrique qui dérive d'un potentiel $V(r)$ est radial).

## Exercice 2 : Calcul de potentiel électrique

**Énoncé.** Le potentiel créé par une charge ponctuelle en un point $M$, situé à la distance $r$ de la charge $q$, est (à une constante additive près) :
$$V(M) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$$

Calculer le champ électrostatique $\vec E$ qui dérive du potentiel $V$.

**Correction.** Par définition, $\vec E = -\overrightarrow{\operatorname{grad}} V$. En coordonnées sphériques centrées sur la charge (au point $P$) :

- $E_r = -\dfrac{\partial V}{\partial r} = -\dfrac{q}{4\pi\varepsilon_0}\dfrac{d}{dr}\Big(\dfrac{1}{r}\Big) = -\dfrac{q}{4\pi\varepsilon_0}\Big(-\dfrac{1}{r^2}\Big) = \dfrac{q}{4\pi\varepsilon_0 r^2}$ ;
- $E_\theta = -\dfrac{1}{r}\dfrac{\partial V}{\partial \theta} = 0$ et $E_\varphi = -\dfrac{1}{r\sin\theta}\dfrac{\partial V}{\partial \varphi} = 0$.

$$\vec E = \frac{q}{4\pi\varepsilon_0 r^2}\,\vec u_{PM}$$

C'est la loi de Coulomb (pour $q > 0$, le champ est dirigé de $P$ vers $M$).

## Exercice 5 : Symétrie axiale

**Énoncé.** (*) Un champ de vecteur $\vec E$ dérive d'un potentiel $V$ qui a la symétrie de révolution autour de l'axe $(Oz)$. On se place dans un plan contenant l'axe $(Oz)$. Dans ce plan, on adopte les coordonnées polaires, et l'on pose $\theta = (\overrightarrow{Oz}, \overrightarrow{OM})$. Le potentiel $V$ a alors pour expression :
$$V = \frac{K}{r^3}\left(3\cos^2\theta - 1\right)$$

Déterminer les composantes du champ $\vec E$.

**Correction.** On utilise les coordonnées sphériques $\{O ; (\vec e_r, \vec e_\theta, \vec e_\varphi)\}$ ; $V = V(r, \theta)$ ne dépend pas de $\varphi$ (symétrie de révolution).
$$E_r = -\frac{\partial V}{\partial r} = +\frac{3K}{r^4}(3\cos^2\theta - 1)$$

$$E_\theta = -\frac{1}{r}\frac{\partial V}{\partial \theta} = -\frac{K}{r^4}\big[3 \times (-\sin\theta) \times 2\cos\theta\big] = \frac{6K}{r^4}\sin\theta\cos\theta$$

$$E_\varphi = -\frac{1}{r\sin\theta}\frac{\partial V}{\partial \varphi} = 0$$

(sinon $V$ n'aurait pas la symétrie de révolution).

## Exercice 3 : Symétrie sphérique

**Énoncé.** Soit une sphère de centre $O$ et de rayon $R$ (cf. exercice 6 du TD2). Déterminer le potentiel électrostatique créé par la distribution surfacique de charges de densité $\sigma$ répartie uniformément sur la surface de cette sphère.

**Correction.** *Champ (TD2, exercice 6)* : en coordonnées sphériques, $\vec E = E(r)\,\vec u_r$ avec

- $r < R$ : $q_{\text{int}} = 0$, donc $E_1 = 0$ ;
- $r > R$ : $q_{\text{int}} = Q = 4\pi R^2\sigma$, donc $E_2 = \dfrac{\sigma}{\varepsilon_0}\dfrac{R^2}{r^2}$,

avec une discontinuité à la traversée de la surface chargée.

*Potentiel.* $\vec E = -\overrightarrow{\operatorname{grad}} V$ : les composantes selon $\vec e_\theta$ et $\vec e_\varphi$ sont nulles, donc $V = V(r)$ et $\dfrac{dV}{dr} = -E(r)$.

- $r < R$ : $\dfrac{dV}{dr} = 0$, donc $V = K$ constante ;
- $r > R$ : $\dfrac{dV}{dr} = -\dfrac{\sigma}{\varepsilon_0}\dfrac{R^2}{r^2}$, donc $V = \dfrac{\sigma}{\varepsilon_0}\dfrac{R^2}{r} + K'$.

$V$ est continu et défini dans tout l'espace : $V(R^-) = K = V(R^+) = \dfrac{\sigma R}{\varepsilon_0} + K'$.

Il n'y a pas de charges à l'infini, on peut donc choisir $V(\infty) = 0$ : $\lim_{r \to \infty}\big(\frac{\sigma R^2}{\varepsilon_0 r} + K'\big) = K' = 0$.
$$V(r \le R) = \frac{\sigma R}{\varepsilon_0}, \qquad V(r \ge R) = \frac{\sigma}{\varepsilon_0}\frac{R^2}{r}$$

Le potentiel est constant dans la sphère, puis décroît en $1/r$ (comme celui d'une charge ponctuelle $Q = 4\pi R^2\sigma$ placée en $O$).

## Exercice 4 : Symétrie cylindrique

**Énoncé.** Soit un cylindre de rayon $R$ et de hauteur infinie. Déterminer le potentiel électrostatique créé par la distribution surfacique de charges de densité $\sigma$ répartie uniformément sur la surface de ce cylindre.

**Correction.** *Champ (TD2, exercice 3, complété par le théorème de Gauss)* : $\vec E = E(r)\,\vec u_r$, et avec un cylindre de Gauss de rayon $r$ et de hauteur $h$ :

- $r < R$ : $q_{\text{int}} = 0$, donc $\vec E_1 = \vec 0$ ;
- $r > R$ : $q_{\text{int}} = 2\pi R h\sigma$ et $2\pi r h\,E = \frac{2\pi R h\sigma}{\varepsilon_0}$, donc $\vec E_2 = \dfrac{\sigma}{\varepsilon_0}\dfrac{R}{r}\,\vec u_r$.

*Potentiel.* En coordonnées cylindriques, $\vec E = -\dfrac{dV}{dr}\vec u_r$ :

- $r < R$ : $V = K$ ;
- $r > R$ : $\dfrac{dV}{dr} = -\dfrac{\sigma R}{\varepsilon_0 r}$, donc $V = -\dfrac{\sigma}{\varepsilon_0}R\ln r + K'$.

$V$ est continu en $r = R$ : $K = -\dfrac{\sigma R}{\varepsilon_0}\ln R + K'$. En revanche on ne peut pas imposer $V(\infty) = 0$, car la distribution s'étend jusqu'à l'infini (et $\ln r \to \infty$). Il reste donc une constante arbitraire $K$ :
$$V(r \le R) = K, \qquad V(r \ge R) = \frac{\sigma R}{\varepsilon_0}\ln\frac{R}{r} + K$$

> **Erreur corrigée :** la correction manuscrite écrit la condition de continuité $K = -\frac{\sigma}{\varepsilon_0}\ln(R) + K'$ et le résultat $V(r \ge R) = \frac{\sigma}{\varepsilon_0}\ln\frac{R}{r} + K$ : il manque le facteur $R$ (l'expression n'est alors pas homogène à un potentiel). Le résultat correct est $V = \frac{\sigma R}{\varepsilon_0}\ln\frac{R}{r} + K$, comme dans la correction 2022-2023.

> **Note :** la correction trace $V(r)$ : constant égal à $K$ pour $r \le R$, puis décroissant pour $r > R$ (si $\sigma > 0$).
