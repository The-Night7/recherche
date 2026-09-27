---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 99 à 110 (ancien TD9-10, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD7 — Dérivées de composées et résolution d'EDP (corrigé)

## Exercice 1 : Dérivée le long d'un chemin

**Énoncé.** Soit $f(x, y) = xy$ une fonction dépendant des variables $x$ et $y$, qui sont paramétrées par $t$ : $x(t) = \cos(t)$, $y(t) = \sin(t)$. Déterminer de deux façons différentes $g'(t)$, où $g(t) = f\big(x(t), y(t)\big)$.

**Correction.**

> **Complément :** l'ancienne correction ne traitait pas cette question (seules les questions voisines de l'ancien exercice 1 étaient corrigées) ; elle a été rédigée pour cette transcription.

*Première façon : explicitement.* $g(t) = \cos(t)\sin(t) = \frac{1}{2}\sin(2t)$, donc $g'(t) = \cos(2t)$.

*Deuxième façon : avec la règle de la chaîne.* Si $f$ est $C^1$ et $x, y$ sont dérivables,
$$g'(t) = \frac{\partial f}{\partial x}\big(x(t), y(t)\big)\, x'(t) + \frac{\partial f}{\partial y}\big(x(t), y(t)\big)\, y'(t)$$
Ici $\partial_x f = y$, $\partial_y f = x$, $x'(t) = -\sin t$ et $y'(t) = \cos t$, donc
$$g'(t) = \sin(t)\cdot(-\sin t) + \cos(t)\cdot\cos(t) = \cos^2 t - \sin^2 t = \cos(2t)$$
Les deux méthodes donnent bien le même résultat.

*Généralisation (ancien exercice 1).* Pour $g(t) = f(2t, 1 + t^2)$, la même règle donne $g'(t) = 2\,\partial_x f(2t, 1 + t^2) + 2t\,\partial_y f(2t, 1 + t^2)$ ; et pour $g(t) = f(x_1 + t h_1, \dots, x_n + t h_n)$, on obtient $g'(t) = \sum_{i=1}^n h_i\, \partial_{x_i} f(x_1 + t h_1, \dots, x_n + t h_n)$.

## Exercice 2 : Dérivées partielles d'une composée

**Énoncé.** Soit $f : (x, y) \mapsto x^2 + y^2 + x$ et $g : (u, v) \mapsto f(uv, u - v)$.

1. Justifier que $g$ est $C^1$ sur $\mathbb{R}^2$.
2. Calculer de deux façons différentes les dérivées partielles de $g$ en fonction de celles de $f$.

**Correction.**

> **Complément :** cet exercice n'a pas d'équivalent dans l'ancienne correction ; la correction a été rédigée pour cette transcription.

**1.** $g = f \circ \phi$ avec $\phi(u, v) = (uv, u - v)$. Les composantes de $\phi$ sont des polynômes, donc $\phi$ est $C^1$ ; $f$ est un polynôme, donc $C^1$. Par composition, $g$ est $C^1$ sur $\mathbb{R}^2$. (Plus directement : $g$ est elle-même un polynôme en $u$ et $v$.)

**2.** *Première façon : explicitement.* $g(u, v) = u^2 v^2 + (u - v)^2 + uv$, donc
$$\frac{\partial g}{\partial u} = 2uv^2 + 2(u - v) + v \qquad \frac{\partial g}{\partial v} = 2u^2 v - 2(u - v) + u$$

*Deuxième façon : règle de la chaîne.* Avec $x = uv$ et $y = u - v$ :
$$\frac{\partial g}{\partial u} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial u} = v\,\frac{\partial f}{\partial x}(uv, u - v) + \frac{\partial f}{\partial y}(uv, u - v)$$
$$\frac{\partial g}{\partial v} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial v} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial v} = u\,\frac{\partial f}{\partial x}(uv, u - v) - \frac{\partial f}{\partial y}(uv, u - v)$$
Avec $\partial_x f = 2x + 1$ et $\partial_y f = 2y$ : $\frac{\partial g}{\partial u} = v(2uv + 1) + 2(u - v)$ et $\frac{\partial g}{\partial v} = u(2uv + 1) - 2(u - v)$, ce qui coïncide avec le calcul direct.

## Exercice 3 : Un jacobien nul

**Énoncé.** On considère l'application $f$ de $\mathbb{R}^2$ dans $\mathbb{R}^2$ définie par
$$f(x, y) = \Big(x\sqrt{1 + y^2} + y\sqrt{1 + x^2}\ ;\ \big(x + \sqrt{1 + x^2}\big)\big(y + \sqrt{1 + y^2}\big)\Big)$$

1. Montrer que $f$ est de classe $C^1$ sur $\mathbb{R}^2$.
2. Calculer le jacobien de $f$ en tout point $(x, y) \in \mathbb{R}^2$. Qu'en déduit-on pour $f$ ?

**Correction.** Notons $w(t) = \sqrt{1 + t^2}$, de sorte que $w'(t) = \frac{t}{w(t)}$, et $f = (f_1, f_2)$ avec
$$f_1(x, y) = x\,w(y) + y\,w(x) \qquad f_2(x, y) = \big(x + w(x)\big)\big(y + w(y)\big) = xy + w(x)w(y) + f_1(x, y)$$

**1.** $w$ est $C^1$ sur $\mathbb{R}$ ($1 + t^2 > 0$ ne s'annule jamais) ; $f_1$ et $f_2$ sont des sommes et produits de fonctions $C^1$ : $f$ est $C^1$ sur $\mathbb{R}^2$.

**2.** On calcule, en simplifiant à chaque fois avec l'expression de $f_2 - f_1 = xy + w(x)w(y)$ :
$$\frac{\partial f_1}{\partial x} = w(y) + \frac{xy}{w(x)} = \frac{f_2 - f_1}{w(x)} \qquad \frac{\partial f_1}{\partial y} = \frac{xy}{w(y)} + w(x) = \frac{f_2 - f_1}{w(y)}$$
$$\frac{\partial f_2}{\partial x} = \Big(1 + \frac{x}{w(x)}\Big)\big(y + w(y)\big) = \frac{f_2}{w(x)} \qquad \frac{\partial f_2}{\partial y} = \frac{f_2}{w(y)}$$
Le jacobien (déterminant de la matrice jacobienne) vaut
$$\det J_f(x, y) = \frac{f_2 - f_1}{w(x)}\cdot\frac{f_2}{w(y)} - \frac{f_2 - f_1}{w(y)}\cdot\frac{f_2}{w(x)} = 0$$
en tout point. Un $C^1$-difféomorphisme a une matrice jacobienne inversible en tout point : $f$ n'est donc **pas** un $C^1$-difféomorphisme (ni même un difféomorphisme local, nulle part).

> **Remarque :** on peut comprendre ce résultat. En posant $x = \operatorname{sh} a$ et $y = \operatorname{sh} b$ (alors $w(x) = \operatorname{ch} a$), on trouve $f_1 = \operatorname{sh} a \operatorname{ch} b + \operatorname{sh} b \operatorname{ch} a = \operatorname{sh}(a + b)$ et $f_2 = e^a e^b = e^{a+b}$. $f$ ne dépend que de $a + b$ : elle écrase le plan sur la courbe $\{(\operatorname{sh} s, e^s)\}$, et n'est pas injective.

## Exercice 4 : Résolution d'une EDP par changement de variables direct

**Énoncé.** On cherche toutes les fonctions $f$ de $\mathbb{R}^2$ dans $\mathbb{R}$, $C^1$ sur $\mathbb{R}^2$, telles que
$$(E) : \quad \forall (x, y) \in \mathbb{R}^2,\quad \frac{\partial f}{\partial x}(x, y) + 2x\,\frac{\partial f}{\partial y}(x, y) = 0$$
On considère l'application $\varphi$ qui à $(u, v) \in \mathbb{R}^2$ associe $\varphi(u, v) = (u, v + u^2)$.

1. Montrer que $\varphi$ est bijective de classe $C^1$ sur $\mathbb{R}^2$.
2. Montrer que $\varphi^{-1}$ est de classe $C^1$ sur $\mathbb{R}^2$.
3. Que peut-on en déduire pour $\varphi$ ?
4. On introduit la fonction $g = f \circ \varphi$.
    a) Montrer que $g$ est de classe $C^1$ sur $\mathbb{R}^2$.
    b) Montrer que $f$ est solution de $(E)$ si et seulement si $\dfrac{\partial g}{\partial u}(u, v) = 0$ pour tout $(u, v)$.
5. En déduire que $f(x, y) = h(y - x^2)$, où $h$ est $C^1$ sur $\mathbb{R}$, est solution de $(E)$.

**Correction.**

**1.** Les composantes de $\varphi$ sont des polynômes : $\varphi$ est $C^1$. Pour $(x, y) \in \mathbb{R}^2$ :
$$\varphi(u, v) = (x, y) \iff \begin{cases} u = x \\ v + u^2 = y \end{cases} \iff \begin{cases} u = x \\ v = y - x^2 \end{cases}$$
Chaque $(x, y)$ a exactement un antécédent : $\varphi$ est bijective, et $\varphi^{-1}(x, y) = (x, y - x^2)$.

**2.** Les composantes de $\varphi^{-1}$ sont des polynômes : $\varphi^{-1}$ est $C^1$.

**3.** $\varphi$ est un $C^1$-difféomorphisme de $\mathbb{R}^2$ sur $\mathbb{R}^2$.

**4. a)** $f$ et $\varphi$ sont $C^1$, donc $g = f \circ \varphi$ l'est aussi.

**4. b)** Avec $x = u$ et $y = v + u^2$, la règle de la chaîne donne
$$\frac{\partial g}{\partial u}(u, v) = \frac{\partial f}{\partial x}\big(\varphi(u, v)\big)\cdot 1 + \frac{\partial f}{\partial y}\big(\varphi(u, v)\big)\cdot 2u = \Big(\frac{\partial f}{\partial x} + 2x\,\frac{\partial f}{\partial y}\Big)\big(\varphi(u, v)\big)$$
puisque $x = u$. Ainsi $\partial_u g(u, v)$ est exactement le membre de gauche de $(E)$ évalué au point $\varphi(u, v)$. Comme $\varphi$ est bijective, quand $(u, v)$ parcourt $\mathbb{R}^2$, $\varphi(u, v)$ parcourt tout $\mathbb{R}^2$ : $(E)$ est vraie en tout point si et seulement si $\partial_u g = 0$ en tout point.

**5.** $\partial_u g = 0$ sur $\mathbb{R}^2$ signifie que, pour chaque $v$ fixé, $u \mapsto g(u, v)$ est de dérivée nulle sur l'intervalle $\mathbb{R}$, donc constante : $g(u, v) = h(v)$ avec $h(v) = g(0, v)$, qui est $C^1$. Alors
$$f(x, y) = g\big(\varphi^{-1}(x, y)\big) = g(x, y - x^2) = h(y - x^2)$$
Réciproquement, toute fonction $f(x, y) = h(y - x^2)$ avec $h$ de classe $C^1$ vérifie $(E)$ : $\partial_x f = -2x\,h'(y - x^2)$ et $\partial_y f = h'(y - x^2)$, donc $\partial_x f + 2x\,\partial_y f = 0$. Les solutions de $(E)$ sont exactement ces fonctions.

> **Précision ajoutée :** l'ancienne correction ne montrait que le sens « $f$ solution $\Rightarrow \partial_u g = 0$ » à la question 4.b ; la bijectivité de $\varphi$ donne l'équivalence.

## Exercice 5 : Résolution d'EDP par changement de variables indirect

**Énoncé.** Résoudre les équations aux dérivées partielles du premier ordre suivantes, d'inconnue $f : U \to \mathbb{R}$ de classe $C^1$, à l'aide du changement de variables fourni.

1. $U = \mathbb{R}^2$ ; $\dfrac{\partial f}{\partial x} - 3\dfrac{\partial f}{\partial y} = 0$ ; changement de variables : $(u, v) = (2x + y, 3x + y)$.
2. $U = \mathbb{R}_+^* \times \mathbb{R}$ ; $x\dfrac{\partial f}{\partial x} + y\dfrac{\partial f}{\partial y} = 0$ ; changement de variables : $(u, v) = (x, y/x)$.
3. $U = \mathbb{R}_+^* \times \mathbb{R}$ ; $x\dfrac{\partial f}{\partial x} + y\dfrac{\partial f}{\partial y} = \sqrt{x^4 + y^4}$ ; changement de variables : $(u, v) = (y/x, x^2 + y^2)$.
4. $U = \mathbb{R}_+^* \times \mathbb{R}$ ; $x\dfrac{\partial f}{\partial x} - y\dfrac{\partial f}{\partial y} = xy^2$ ; changement de variables : $(u, v) = (x, yx)$.

**Correction.** Méthode commune : on note $\varphi(x, y) = (u, v)$ le changement de variables, on vérifie que c'est un $C^1$-difféomorphisme de $U$ sur son image $V$, et on pose $g = f \circ \varphi^{-1}$, c'est-à-dire $f = g \circ \varphi$ : $f(x, y) = g\big(u(x, y), v(x, y)\big)$. La règle de la chaîne donne
$$\frac{\partial f}{\partial x} = \frac{\partial g}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial g}{\partial v}\frac{\partial v}{\partial x} \qquad \frac{\partial f}{\partial y} = \frac{\partial g}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial g}{\partial v}\frac{\partial v}{\partial y}$$
On réécrit l'équation en fonction de $g$, qui devient une équation simple à intégrer.

**1.** $\varphi(x, y) = (2x + y, 3x + y)$ est linéaire, de déterminant $2 \cdot 1 - 1 \cdot 3 = -1 \ne 0$ : c'est une bijection de $\mathbb{R}^2$ sur $\mathbb{R}^2$, $C^1$ ainsi que sa réciproque. Avec $f(x, y) = g(2x + y, 3x + y)$ :
$$\frac{\partial f}{\partial x} = 2\frac{\partial g}{\partial u} + 3\frac{\partial g}{\partial v} \qquad \frac{\partial f}{\partial y} = \frac{\partial g}{\partial u} + \frac{\partial g}{\partial v}$$
donc $\partial_x f - 3\,\partial_y f = -\partial_u g$. L'équation équivaut à $\partial_u g = 0$ sur $\mathbb{R}^2$, soit $g(u, v) = h(v)$ avec $h$ de classe $C^1$ sur $\mathbb{R}$. Les solutions sont
$$f(x, y) = h(3x + y), \quad h \in C^1(\mathbb{R})$$
(Vérification : $\partial_x f = 3h'$ et $\partial_y f = h'$, donc $3h' - 3h' = 0$.)

> **Complément :** cette équation n'était pas dans l'ancienne feuille ; sa correction a été rédigée pour cette transcription.

**2.** $\varphi(x, y) = (x, \frac{y}{x})$ est $C^1$ sur $U$, bijective de $U$ sur $V = U$, de réciproque $(u, v) \mapsto (u, uv)$, elle aussi $C^1$. Avec $f(x, y) = g(x, \frac{y}{x})$ :
$$\frac{\partial f}{\partial x} = \frac{\partial g}{\partial u} - \frac{y}{x^2}\frac{\partial g}{\partial v} \qquad \frac{\partial f}{\partial y} = \frac{1}{x}\frac{\partial g}{\partial v}$$
donc $x\,\partial_x f + y\,\partial_y f = x\,\partial_u g = u\,\partial_u g$. Comme $u > 0$, l'équation équivaut à $\partial_u g = 0$, soit $g(u, v) = h(v)$ (pour $v$ fixé, $u$ parcourt l'intervalle $]0, +\infty[$). Les solutions sont
$$f(x, y) = h\Big(\frac{y}{x}\Big), \quad h \in C^1(\mathbb{R})$$

**3.** $\varphi(x, y) = (\frac{y}{x}, x^2 + y^2)$ est $C^1$ sur $U$, à valeurs dans $V = \mathbb{R} \times \mathbb{R}_+^*$. Elle est bijective : $(u, v) = \varphi(x, y)$ équivaut à $y = ux$ et $x^2(1 + u^2) = v$, soit, avec $x > 0$,
$$x = \sqrt{\frac{v}{1 + u^2}}, \qquad y = u\sqrt{\frac{v}{1 + u^2}}$$
qui est $C^1$ sur $V$. Avec $f(x, y) = g\big(\frac{y}{x}, x^2 + y^2\big)$ :
$$\frac{\partial f}{\partial x} = -\frac{y}{x^2}\frac{\partial g}{\partial u} + 2x\frac{\partial g}{\partial v} \qquad \frac{\partial f}{\partial y} = \frac{1}{x}\frac{\partial g}{\partial u} + 2y\frac{\partial g}{\partial v}$$
donc $x\,\partial_x f + y\,\partial_y f = 2(x^2 + y^2)\,\partial_v g = 2v\,\partial_v g$. D'autre part $x^4 + y^4 = x^4(1 + u^4)$ et $x^2 = \frac{v}{1 + u^2}$, donc $\sqrt{x^4 + y^4} = \dfrac{v\sqrt{1 + u^4}}{1 + u^2}$. L'équation devient
$$2v\,\frac{\partial g}{\partial v} = \frac{v\sqrt{1 + u^4}}{1 + u^2} \iff \frac{\partial g}{\partial v} = \frac{\sqrt{1 + u^4}}{2(1 + u^2)}$$
d'où $g(u, v) = \dfrac{v\sqrt{1 + u^4}}{2(1 + u^2)} + h(u)$. En revenant à $x, y$ (avec $\frac{x^2 + y^2}{1 + y^2/x^2} = x^2$ et $\sqrt{1 + y^4/x^4} = \frac{\sqrt{x^4 + y^4}}{x^2}$) :
$$f(x, y) = \frac{1}{2}\sqrt{x^4 + y^4} + h\Big(\frac{y}{x}\Big), \quad h \in C^1(\mathbb{R})$$

**4.** $\varphi(x, y) = (x, xy)$ est $C^1$ et bijective de $U$ sur $U$, de réciproque $(u, v) \mapsto (u, \frac{v}{u})$, $C^1$ sur $U$. Avec $f(x, y) = g(x, xy)$ :
$$\frac{\partial f}{\partial x} = \frac{\partial g}{\partial u} + y\frac{\partial g}{\partial v} \qquad \frac{\partial f}{\partial y} = x\frac{\partial g}{\partial v}$$
donc $x\,\partial_x f - y\,\partial_y f = x\,\partial_u g = u\,\partial_u g$. L'équation devient $u\,\partial_u g = xy^2 = u\,\frac{v^2}{u^2}$, soit $\partial_u g = \frac{v^2}{u^2}$, d'où $g(u, v) = -\frac{v^2}{u} + h(v)$. Les solutions sont
$$f(x, y) = -\frac{(xy)^2}{x} + h(xy) = -xy^2 + h(xy), \quad h \in C^1(\mathbb{R})$$
(Vérification : pour $f = -xy^2$, $x\,\partial_x f - y\,\partial_y f = -xy^2 + 2xy^2 = xy^2$.)
