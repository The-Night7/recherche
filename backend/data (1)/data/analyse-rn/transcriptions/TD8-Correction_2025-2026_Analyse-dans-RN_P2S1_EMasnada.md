---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 121 à 153 (ancien TD11-12, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD8 — Dérivées partielles d'ordre 2 et plus, EDP (corrigé)

## Exercice 1 : Dérivées secondes et théorème de Schwarz

**Énoncé.** Pour toutes les fonctions suivantes, calculer l'expression de toutes les dérivées secondes en précisant les domaines d'existence, et vérifier le théorème de Schwarz (à faire partiellement en classe) :

1. $f(x, y) = x^2 y + x\sqrt{y}$
2. $f(x, y) = \sin(x + y) + \cos(x - y)$
3. $f(x, y) = (x^2 + y^2)^{3/2}$
4. $f(x, y) = \cos^2(5x + 2y)$

**Correction.** Notation : $\dfrac{\partial^2 f}{\partial x \partial y} = \dfrac{\partial}{\partial x}\Big(\dfrac{\partial f}{\partial y}\Big)$. Le théorème de Schwarz dit que si $f$ est $C^2$ sur un ouvert, les deux dérivées croisées y sont égales.

**1.** $f$ est définie pour $y \ge 0$ ; ses dérivées, pour $y > 0$.
$$\frac{\partial f}{\partial x} = 2xy + \sqrt{y} \qquad \frac{\partial f}{\partial y} = x^2 + \frac{x}{2\sqrt{y}}$$
$$\frac{\partial^2 f}{\partial x^2} = 2y \qquad \frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y} = 2x + \frac{1}{2\sqrt{y}} \qquad \frac{\partial^2 f}{\partial y^2} = -\frac{x}{4y^{3/2}}$$
sur $\mathbb{R} \times \mathbb{R}_+^*$ : les dérivées croisées sont bien égales.

**2.** Sur $\mathbb{R}^2$ :
$$\frac{\partial f}{\partial x} = \cos(x + y) - \sin(x - y) \qquad \frac{\partial f}{\partial y} = \cos(x + y) + \sin(x - y)$$
$$\frac{\partial^2 f}{\partial x^2} = \frac{\partial^2 f}{\partial y^2} = -\sin(x + y) - \cos(x - y) \qquad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = -\sin(x + y) + \cos(x - y)$$

**3.** Notons $r = \sqrt{x^2 + y^2}$, de sorte que $f = r^3$ et $\partial_x r = \frac{x}{r}$. Sur $\mathbb{R}^2$ :
$$\frac{\partial f}{\partial x} = 3xr \qquad \frac{\partial f}{\partial y} = 3yr$$
(en $(0,0)$ aussi, car $\frac{f(t, 0)}{t} = \frac{|t|^3}{t} \to 0$). Sur $\mathbb{R}^2 \setminus \{(0,0)\}$ :
$$\frac{\partial^2 f}{\partial x^2} = 3r + \frac{3x^2}{r} \qquad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = \frac{3xy}{r} \qquad \frac{\partial^2 f}{\partial y^2} = 3r + \frac{3y^2}{r}$$
Ces expressions tendent vers $0$ en $(0,0)$ (elles sont majorées par $6r$), et les dérivées secondes en $(0,0)$ valent $0$ (par exemple $\frac{\partial_x f(t, 0)}{t} = 3|t| \to 0$) : $f$ est même $C^2$ sur $\mathbb{R}^2$.

> **Erreur corrigée :** l'ancienne correction avait un facteur $\frac{1}{2}$ en trop : $\frac{3x^2}{2r}$, $\frac{3xy}{2r}$ et $\frac{3y^2}{2r}$. En dérivant $3xr$ par rapport à $y$, on obtient $3x \cdot \frac{y}{r}$, sans $\frac{1}{2}$.

**4.** Sur $\mathbb{R}^2$, avec $2\sin a \cos a = \sin(2a)$ et $\cos^2 a - \sin^2 a = \cos(2a)$ :
$$\frac{\partial f}{\partial x} = -10\sin(5x + 2y)\cos(5x + 2y) = -5\sin(10x + 4y) \qquad \frac{\partial f}{\partial y} = -2\sin(10x + 4y)$$
$$\frac{\partial^2 f}{\partial x^2} = -50\cos(10x + 4y) \qquad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = -20\cos(10x + 4y) \qquad \frac{\partial^2 f}{\partial y^2} = -8\cos(10x + 4y)$$
(Avec $\cos(10x + 4y) = \cos^2(5x + 2y) - \sin^2(5x + 2y)$.)

> **Erreur corrigée :** l'ancienne correction écrivait $-20\cos(5x + 2y) + 20\sin(5x + 2y)$ pour les dérivées croisées : il manquait les carrés, c'est $-20\cos^2(5x + 2y) + 20\sin^2(5x + 2y)$.

## Exercice 2 : Dérivées partielles d'ordre 3

**Énoncé.** Pour chaque fonction, déterminer la dérivée partielle indiquée (à faire partiellement en classe) :

1. $\dfrac{\partial^3 f}{\partial x^3}$ pour $f(x, y) = x^2 y^4 + 2x^4 y$
2. $\dfrac{\partial^3 f}{\partial x^2 \partial y}$ pour $f(x, y) = e^{xy^2}$
3. $\dfrac{\partial^3 f}{\partial z \partial y \partial x}$ pour $f(x, y, z) = x^5 + 4x^4 y^4 z^3 + yz^2$
4. $\dfrac{\partial^3 f}{\partial x \partial y \partial z}$ pour $f(x, y, z) = \ln(x + 2y^2 + 3z^2)$

**Correction.** On dérive de droite à gauche : $\frac{\partial^3 f}{\partial x^2 \partial y}$ signifie qu'on dérive d'abord par rapport à $y$, puis deux fois par rapport à $x$. Toutes ces fonctions sont $C^3$ sur leur domaine, donc l'ordre n'importe pas (Schwarz) : on choisit le plus simple.

**1.** $\partial_x f = 2xy^4 + 8x^3 y$, $\ \partial_x^2 f = 2y^4 + 24x^2 y$, $\ \dfrac{\partial^3 f}{\partial x^3} = 48xy$.

**2.** $\partial_y f = 2xy\, e^{xy^2}$, puis $\dfrac{\partial^2 f}{\partial x \partial y} = (2y + 2xy^3)\, e^{xy^2}$, puis
$$\frac{\partial^3 f}{\partial x^2 \partial y} = 2y^3 e^{xy^2} + (2y + 2xy^3)\, y^2 e^{xy^2} = (4y^3 + 2xy^5)\, e^{xy^2}$$

> **Erreur corrigée :** l'ancienne correction donnait $4y^3 e^{xy^2} + 2y^5 e^{xy^2}$ ; il manque le facteur $x$ dans le second terme.

**3.** $\partial_x f = 5x^4 + 16x^3 y^4 z^3$, $\ \partial_y \partial_x f = 64x^3 y^3 z^3$, $\ \dfrac{\partial^3 f}{\partial z \partial y \partial x} = 192x^3 y^3 z^2$.

**4.** Sur le domaine $x + 2y^2 + 3z^2 > 0$, notons $D = x + 2y^2 + 3z^2$. En dérivant d'abord par rapport à $z$, puis $y$, puis $x$ :
$$\frac{\partial f}{\partial z} = \frac{6z}{D} \qquad \frac{\partial^2 f}{\partial y \partial z} = -\frac{6z \cdot 4y}{D^2} = -\frac{24yz}{D^2} \qquad \frac{\partial^3 f}{\partial x \partial y \partial z} = \frac{48yz}{D^3} = \frac{48yz}{(x + 2y^2 + 3z^2)^3}$$

> **Complément :** ce calcul n'était pas corrigé dans l'ancienne correction.

## Exercice 3 : Dérivées croisées différentes

**Énoncé.** Soit $f(x, y) = \dfrac{xy^3}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$.

1. Montrer que $f$ est $C^1$ sur $\mathbb{R}^2$.
2. Montrer que $\dfrac{\partial^2 f}{\partial x \partial y}$ et $\dfrac{\partial^2 f}{\partial y \partial x}$ sont définies en $(0, 0)$ mais n'ont pas même valeur.
3. Que peut-on en déduire ?

**Correction.**

**1.** *Hors de $(0,0)$*, $f$ est une fraction rationnelle dont le dénominateur ne s'annule pas : elle est $C^1$ (et même $C^\infty$), avec
$$\frac{\partial f}{\partial x} = \frac{y^3(x^2 + y^2) - 2x^2 y^3}{(x^2 + y^2)^2} = \frac{y^5 - x^2 y^3}{(x^2 + y^2)^2} \qquad \frac{\partial f}{\partial y} = \frac{3x^3 y^2 + xy^4}{(x^2 + y^2)^2}$$
*En $(0,0)$* : $f(t, 0) = f(0, t) = 0$, donc $\partial_x f(0,0) = \partial_y f(0,0) = 0$.

*Continuité des dérivées en $(0,0)$* : en polaires, $\partial_x f = \rho\sin^3\theta(\sin^2\theta - \cos^2\theta)$ et $\partial_y f = \rho(3\cos^3\theta\sin^2\theta + \cos\theta\sin^4\theta)$, majorées en valeur absolue par $\rho$ et $4\rho$, qui tendent vers $0$ indépendamment de $\theta$. Les dérivées partielles sont continues sur $\mathbb{R}^2$ : $f$ est $C^1$ sur $\mathbb{R}^2$.

**2.** Par définition, en utilisant $\partial_y f(t, 0) = 0$ et $\partial_x f(0, t) = \frac{t^5}{t^4} = t$ :
$$\frac{\partial^2 f}{\partial x \partial y}(0,0) = \lim_{t \to 0} \frac{\partial_y f(t, 0) - \partial_y f(0, 0)}{t} = 0 \qquad \frac{\partial^2 f}{\partial y \partial x}(0,0) = \lim_{t \to 0} \frac{\partial_x f(0, t) - \partial_x f(0,0)}{t} = 1$$
Les deux dérivées croisées existent mais sont différentes.

**3.** Si $f$ était $C^2$ sur un voisinage de $(0,0)$, le théorème de Schwarz donnerait l'égalité des dérivées croisées. Donc $f$ n'est pas $C^2$ : ses dérivées secondes croisées ne sont pas continues en $(0,0)$. $f$ est exactement de classe $C^1$.

## Exercice 4 : Dérivées croisées égales, mais pas C²

**Énoncé.** Soit $f(x, y) = \dfrac{y^4}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$.

1. Montrer que $f$ est $C^1$ sur $\mathbb{R}^2$.
2. Montrer que $\dfrac{\partial^2 f}{\partial x \partial y}$ et $\dfrac{\partial^2 f}{\partial y \partial x}$ sont définies en $(0, 0)$ et ont même valeur.
3. Que peut-on en déduire ?

**Correction.**

**1.** *Hors de $(0,0)$* :
$$\frac{\partial f}{\partial x} = -\frac{2xy^4}{(x^2 + y^2)^2} \qquad \frac{\partial f}{\partial y} = \frac{4x^2 y^3 + 2y^5}{(x^2 + y^2)^2}$$
*En $(0,0)$* : $f(t, 0) = 0$ donne $\partial_x f(0,0) = 0$ ; $f(0, t) = t^2$ donne $\frac{t^2}{t} = t \to 0$, donc $\partial_y f(0,0) = 0$.

*Continuité* : en polaires, $\partial_x f = -2\rho\cos\theta\sin^4\theta$ et $\partial_y f = \rho(4\cos^2\theta\sin^3\theta + 2\sin^5\theta)$, majorées par $2\rho$ et $6\rho$ : elles tendent vers $0$. $f$ est $C^1$ sur $\mathbb{R}^2$.

**2.** $\partial_y f(t, 0) = 0$ et $\partial_x f(0, t) = 0$, donc
$$\frac{\partial^2 f}{\partial x \partial y}(0,0) = \lim_{t \to 0}\frac{0 - 0}{t} = 0 = \frac{\partial^2 f}{\partial y \partial x}(0,0)$$

**3.** On **ne peut rien en déduire** sur le caractère $C^2$ : l'égalité des dérivées croisées en un point est une conséquence du théorème de Schwarz, pas une réciproque. Ici d'ailleurs $f$ n'est pas $C^2$ : hors de $(0,0)$,
$$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = -\frac{8x^3 y^3}{(x^2 + y^2)^3}$$
qui vaut $-\frac{8x^6}{8x^6} = -1$ sur la diagonale $y = x$ : elle ne tend pas vers $0$ en $(0,0)$ et n'y est pas continue.

> **Erreur corrigée :** l'ancienne correction trouvait $+1$ sur la diagonale ; le signe est $-1$. La conclusion ne change pas.

## Exercice 5 : Classe exacte

**Énoncé.** Déterminer la classe exacte des applications suivantes (toutes prolongées par $0$ en $(0,0)$) :

1. $f(x, y) = \dfrac{(x^2 - y^2)^2}{x^2 + y^2}$
2. $f(x, y) = \dfrac{xy^2}{x^2 + (y - x^2)^2}$
3. $f(x, y) = \dfrac{(e^{x^2} - 1)(e^{y^2} - 1)}{x^2 + y^2}$

**Correction.** Chaque fonction est $C^\infty$ sur $\mathbb{R}^2 \setminus \{(0,0)\}$ (dénominateur non nul) ; on étudie $(0,0)$ en testant successivement la continuité, le caractère $C^1$, puis $C^2$.

**1. Classe $C^1$ exactement.** Comme $(x^2 - y^2)^2 = (x^2 + y^2)^2 - 4x^2y^2$,
$$f(x, y) = x^2 + y^2 - 4\,\frac{x^2 y^2}{x^2 + y^2}$$

- *Continue* : $|f| \le x^2 + y^2 \to 0$.
- *$C^1$* : hors de $(0,0)$, $\partial_x f = \dfrac{2x(x^2 - y^2)(x^2 + 3y^2)}{(x^2 + y^2)^2}$ et $\partial_y f = \dfrac{-2y(x^2 - y^2)(3x^2 + y^2)}{(x^2 + y^2)^2}$ ; en $(0,0)$, $f(t, 0) = f(0, t) = t^2$ donne des dérivées nulles. En majorant, $|\partial_x f| \le \frac{2|x|(x^2 + y^2) \cdot 3(x^2 + y^2)}{(x^2 + y^2)^2} = 6|x| \to 0$, et de même pour $\partial_y f$ : elles sont continues.
- *Pas $C^2$* : hors de $(0,0)$, $\dfrac{\partial^2 f}{\partial x \partial y} = -4\,\dfrac{8x^3 y^3}{(x^2 + y^2)^3} = -\dfrac{32x^3 y^3}{(x^2 + y^2)^3}$ (même calcul qu'à l'exercice 4), qui vaut $-4$ sur la diagonale et $0$ sur les axes : pas de limite en $(0,0)$.

**2. Classe $C^0$ exactement.**

- *Continue* : en polaires, le dénominateur vaut $\rho^2(1 + \rho\,a(\rho, \theta))$ avec $a = \rho\cos^4\theta - 2\cos^2\theta\sin\theta$, et $|a| \le \rho + 2$. Pour $\rho \le \frac{1}{4}$, $1 + \rho a \ge 1 - \frac{1}{4}\cdot\frac{9}{4} = \frac{7}{16}$, donc
$$|f| = \frac{\rho\,|\cos\theta\sin^2\theta|}{1 + \rho a} \le \frac{16}{7}\rho \le 3\rho \to 0$$
- *Pas $C^1$* : $f(t, 0) = 0$ et $f(0, t) = 0$, donc $\partial_x f(0,0) = \partial_y f(0,0) = 0$. Mais sur l'axe $x = 0$, pour $y \ne 0$ :
$$\frac{\partial f}{\partial x}(0, y) = \frac{y^2}{0 + y^2} - 0 = 1$$
(le second terme de la dérivée contient le facteur $x$). Donc $\partial_x f(0, y) \to 1 \ne 0 = \partial_x f(0,0)$ : $\partial_x f$ n'est pas continue en $(0,0)$.

**3. Classe $C^1$ exactement.** Posons $\psi(s) = \frac{e^s - 1}{s}$ (et $\psi(0) = 1$), fonction $C^\infty$ qui vaut $1$ en $0$. Alors
$$f(x, y) = \psi(x^2)\,\psi(y^2)\,\frac{x^2 y^2}{x^2 + y^2}$$

- *Continue* : $\frac{x^2 y^2}{x^2 + y^2} \le \frac{x^2 + y^2}{4} \to 0$, et les $\psi$ tendent vers $1$.
- *$C^1$* : les dérivées en $(0,0)$ sont nulles ($f(t, 0) = 0$). Hors de $(0,0)$,
$$\frac{\partial f}{\partial x} = \frac{2xe^{x^2}(e^{y^2} - 1)}{x^2 + y^2} - \frac{2x(e^{x^2} - 1)(e^{y^2} - 1)}{(x^2 + y^2)^2}$$
Près de $(0,0)$, $|e^{s} - 1| \le 2|s|$ ; donc le premier terme est majoré par $4|x|e^{x^2}\frac{y^2}{x^2 + y^2} \le 4|x|e^{x^2}$ et le second par $\frac{8|x|\,x^2 y^2}{(x^2 + y^2)^2} \le 2|x|$. Les deux tendent vers $0$ : $\partial_x f$ est continue, et de même $\partial_y f$.
- *Pas $C^2$* : le facteur $\frac{x^2 y^2}{x^2 + y^2}$ n'est pas $C^2$ (sa dérivée croisée $\frac{8x^3 y^3}{(x^2 + y^2)^3}$ vaut $1$ sur la diagonale et $0$ sur les axes), et $\psi(x^2)\psi(y^2)$ vaut $1$ en $(0,0)$. Concrètement, la dérivée croisée de $f$ tend vers $1$ le long de la diagonale, alors qu'elle vaut $0$ en $(0,0)$ (car $\partial_y f(t, 0) = 0$ pour tout $t$).

## Exercice 6 : EDP du second ordre

**Énoncé.** Résoudre les EDP du second ordre d'inconnue $f : U \to \mathbb{R}$ de classe $C^2$, à l'aide du changement de variables fourni :

1. $U = \mathbb{R}^2$ : $\dfrac{\partial^2 f}{\partial x^2} - \dfrac{\partial^2 f}{\partial y^2} = 0$ ; $(u, v) = (x + y, x - y)$
2. $U = \mathbb{R}_+^* \times \mathbb{R}$ : $x^2\dfrac{\partial^2 f}{\partial x^2} + 2xy\dfrac{\partial^2 f}{\partial x \partial y} + y^2\dfrac{\partial^2 f}{\partial y^2} = 0$ ; $(u, v) = (x, y/x)$
3. $U = \mathbb{R}_+^* \times \mathbb{R}$ : $\dfrac{\partial^2 f}{\partial x^2} - 4x^2\dfrac{\partial^2 f}{\partial y^2} - \dfrac{1}{x}\dfrac{\partial f}{\partial x} = 0$ ; $(u, v) = (x^2 - y, x^2 + y)$
4. $U = \mathbb{R}^2$ : $\dfrac{\partial^2 f}{\partial x^2} - 2\dfrac{\partial^2 f}{\partial x \partial y} + \dfrac{\partial^2 f}{\partial y^2} = 0$ ; $(u, v) = (x, x + y)$

**Correction.** Méthode en cinq étapes :

1. vérifier que $\varphi : (x, y) \mapsto (u, v)$ est un $C^2$-difféomorphisme de $U$ sur son image $V$ ;
2. poser $g = f \circ \varphi^{-1}$, c'est-à-dire $f(x, y) = g\big(u(x, y), v(x, y)\big)$, qui est $C^2$ sur $V$ ;
3. exprimer les dérivées de $f$ en fonction de celles de $g$ (règle de la chaîne, deux fois) ;
4. réécrire l'EDP en une EDP simple sur $g$ et la résoudre ;
5. revenir à $f$.

**1. L'équation des ondes.** $\varphi(x, y) = (x + y, x - y)$ est linéaire bijective, de réciproque $(u, v) \mapsto \big(\frac{u + v}{2}, \frac{u - v}{2}\big)$ : c'est un $C^2$-difféomorphisme de $\mathbb{R}^2$. Avec $f(x, y) = g(x + y, x - y)$ :
$$\frac{\partial f}{\partial x} = g_u + g_v \qquad \frac{\partial f}{\partial y} = g_u - g_v$$
$$\frac{\partial^2 f}{\partial x^2} = g_{uu} + 2g_{uv} + g_{vv} \qquad \frac{\partial^2 f}{\partial y^2} = g_{uu} - 2g_{uv} + g_{vv}$$
L'équation devient $4g_{uv} = 0$. Alors $\partial_v(g_u) = 0$ : $g_u$ ne dépend que de $u$, $g_u = k'(u)$, puis $g(u, v) = k(u) + h(v)$ avec $h, k$ de classe $C^2$. Les solutions sont
$$f(x, y) = k(x + y) + h(x - y), \quad h, k \in C^2(\mathbb{R})$$

**2.** $\varphi(x, y) = (x, \frac{y}{x})$ est un $C^2$-difféomorphisme de $U$ sur $U$, de réciproque $(u, v) \mapsto (u, uv)$. Avec $f(x, y) = g(x, \frac{y}{x})$ :
$$f_x = g_u - \frac{y}{x^2}g_v \qquad f_y = \frac{1}{x}g_v$$
$$f_{xx} = g_{uu} - \frac{2y}{x^2}g_{uv} + \frac{y^2}{x^4}g_{vv} + \frac{2y}{x^3}g_v$$
$$f_{xy} = \frac{1}{x}g_{uv} - \frac{1}{x^2}g_v - \frac{y}{x^3}g_{vv} \qquad f_{yy} = \frac{1}{x^2}g_{vv}$$
En remplaçant, tous les termes se simplifient sauf un : $x^2 f_{xx} + 2xy f_{xy} + y^2 f_{yy} = x^2 g_{uu} = u^2 g_{uu}$. Comme $u > 0$, l'équation équivaut à $g_{uu} = 0$ : pour chaque $v$, $u \mapsto g(u, v)$ est affine, $g(u, v) = u\,h(v) + k(v)$. Les solutions sont
$$f(x, y) = x\,h\Big(\frac{y}{x}\Big) + k\Big(\frac{y}{x}\Big), \quad h, k \in C^2(\mathbb{R})$$

**3.** $\varphi(x, y) = (x^2 - y, x^2 + y)$ est $C^2$ sur $U$. On a $u + v = 2x^2 > 0$, et réciproquement, pour $(u, v)$ avec $u + v > 0$ :
$$x = \sqrt{\frac{u + v}{2}}, \qquad y = \frac{v - u}{2}$$
qui est $C^2$ (puisque $u + v > 0$). Donc $\varphi$ est un $C^2$-difféomorphisme de $U$ sur $V = \{(u, v) \,/\, u + v > 0\}$. Avec $f(x, y) = g(x^2 - y, x^2 + y)$ :
$$f_x = 2x(g_u + g_v) \qquad f_y = -g_u + g_v$$
$$f_{xx} = 2(g_u + g_v) + 4x^2(g_{uu} + 2g_{uv} + g_{vv}) \qquad f_{yy} = g_{uu} - 2g_{uv} + g_{vv}$$
donc $f_{xx} - 4x^2 f_{yy} - \frac{1}{x}f_x = 16x^2 g_{uv}$. Comme $x \ne 0$, l'équation équivaut à $g_{uv} = 0$ sur $V$ ; pour $u$ fixé, $v$ parcourt l'intervalle $]-u, +\infty[$, donc comme à la question 1, $g(u, v) = K(u) + L(v)$. Les solutions sont
$$f(x, y) = K(x^2 - y) + L(x^2 + y), \quad K, L \in C^2(\mathbb{R})$$

> **Erreur corrigée :** l'ancienne correction affirmait que $\varphi$ est une bijection de $U$ sur $\mathbb{R}^2$ ; son image est le demi-plan $\{u + v > 0\}$.

**4.** $\varphi(x, y) = (x, x + y)$ est linéaire bijective, de réciproque $(u, v) \mapsto (u, v - u)$. Avec $f(x, y) = g(x, x + y)$ :
$$f_x = g_u + g_v \qquad f_y = g_v$$
$$f_{xx} = g_{uu} + 2g_{uv} + g_{vv} \qquad f_{xy} = g_{uv} + g_{vv} \qquad f_{yy} = g_{vv}$$
donc $f_{xx} - 2f_{xy} + f_{yy} = g_{uu}$. L'équation équivaut à $g_{uu} = 0$, soit $g(u, v) = u\,C(v) + D(v)$. Les solutions sont
$$f(x, y) = x\,C(x + y) + D(x + y), \quad C, D \in C^2(\mathbb{R})$$
