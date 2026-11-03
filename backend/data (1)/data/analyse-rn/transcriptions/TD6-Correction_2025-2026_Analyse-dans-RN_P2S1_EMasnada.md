---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 80 à 98 (ancien TD8, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD6 — Dérivées partielles premières (corrigé)

## Exercice 1 : Calculs de dérivées partielles

**Énoncé.** Calculer toutes les dérivées partielles d'ordre 1, sans se préoccuper de leur domaine de définition (à faire partiellement en classe).

> **Note :** la liste des fonctions de la feuille 2025-2026 n'a pas pu être extraite ; c'est celle de l'ancienne feuille, dont cet exercice est repris.

1. $f(x,y) = xy$
2. $f(x,y) = \ln(xy)$
3. $f(x,y) = \dfrac{-3y}{x^2 + y^2 + 1}$
4. $f(x,y) = \dfrac{x^2 - y^2}{x^2 + y^2}$
5. $f(x,y) = \dfrac{\sin(x) - \sin(y)}{x - y}$
6. $f(x,y) = \dfrac{4xy(x^2 - y^2)}{x^2 + y^2}$
7. $f(x,y) = \operatorname{Arctan}\big(\frac{y}{x}\big)$
8. $f(x,y) = \operatorname{Arctan}\Big(\dfrac{x + y}{1 - xy}\Big)$
9. $f(x,y) = (x^2 + y^2)^{1/3}$
10. $f(x,y) = x^y$ (avec $x > 0$)
11. $f(x,y) = \cos(x + y^2)$
12. $f(x,y) = e^{\sin(y/x)}$
13. $f(x,y) = \ln\big(x + \sqrt{x^2 + y^2}\big)$
14. $f(x,y) = \dfrac{x}{\sqrt{x^2 - y}}$
15. $f(x,y,z) = x^2 y z^3 + xy - z$
16. $f(x,y,z) = x\sqrt{yz}$
17. $f(x,y,z) = x^{y/z}$
18. $f(x,y,z,t) = \dfrac{x - y}{z - t}$
19. $f(x,y,z,t) = xy^2 z^3 t^4$
20. $f(x,y) = y^5 - 3xy$
21. $f(x,y) = x^2 + 3xy - 6y^5$
22. $f(x,y) = x\cos(e^{xy})$
23. $f(x,y) = \dfrac{x}{y}$
24. $f(x,y) = x^y$
25. $f(x,y,z) = x\cos(xz) + \ln\big(2 - \sin^2(y + z)\big)$

**Correction.** On dérive par rapport à une variable en considérant les autres comme des constantes.

1. $\partial_x f = y$, $\quad \partial_y f = x$.
2. $\partial_x f = \frac{1}{x}$, $\quad \partial_y f = \frac{1}{y}$.
3. $\partial_x f = \dfrac{6xy}{(x^2 + y^2 + 1)^2}$, $\quad \partial_y f = \dfrac{-3(x^2 + y^2 + 1) + 6y^2}{(x^2 + y^2 + 1)^2} = \dfrac{-3x^2 + 3y^2 - 3}{(x^2 + y^2 + 1)^2}$.
4. $\partial_x f = \dfrac{2x(x^2 + y^2) - 2x(x^2 - y^2)}{(x^2 + y^2)^2} = \dfrac{4xy^2}{(x^2 + y^2)^2}$, $\quad \partial_y f = \dfrac{-4x^2 y}{(x^2 + y^2)^2}$.
5. $\partial_x f = \dfrac{(x - y)\cos(x) - (\sin x - \sin y)}{(x - y)^2}$, $\quad \partial_y f = \dfrac{-(x - y)\cos(y) + (\sin x - \sin y)}{(x - y)^2}$.
6. $\partial_x f = \dfrac{4x^4 y + 16x^2 y^3 - 4y^5}{(x^2 + y^2)^2}$, $\quad \partial_y f = \dfrac{4x^5 - 16x^3 y^2 - 4xy^4}{(x^2 + y^2)^2}$.
7. $\partial_x f = \dfrac{-y/x^2}{1 + (y/x)^2} = -\dfrac{y}{x^2 + y^2}$, $\quad \partial_y f = \dfrac{1/x}{1 + (y/x)^2} = \dfrac{x}{x^2 + y^2}$.
8. Avec $u = \frac{x + y}{1 - xy}$, $\partial_x u = \frac{1 + y^2}{(1 - xy)^2}$, et $(1 - xy)^2 + (x + y)^2 = (1 + x^2)(1 + y^2)$ ; donc $\partial_x f = \dfrac{\partial_x u}{1 + u^2} = \dfrac{1}{1 + x^2}$ et de même $\partial_y f = \dfrac{1}{1 + y^2}$.
9. $\partial_x f = \frac{2}{3}x(x^2 + y^2)^{-2/3}$, $\quad \partial_y f = \frac{2}{3}y(x^2 + y^2)^{-2/3}$.
10. $f = e^{y\ln x}$ : $\partial_x f = \frac{y}{x}e^{y\ln x} = yx^{y-1}$, $\quad \partial_y f = \ln(x)\, x^y$.
11. $\partial_x f = -\sin(x + y^2)$, $\quad \partial_y f = -2y\sin(x + y^2)$.
12. $\partial_x f = -\frac{y}{x^2}\cos\big(\frac{y}{x}\big)e^{\sin(y/x)}$, $\quad \partial_y f = \frac{1}{x}\cos\big(\frac{y}{x}\big)e^{\sin(y/x)}$.
13. $\partial_x f = \dfrac{1 + \frac{x}{\sqrt{x^2 + y^2}}}{x + \sqrt{x^2 + y^2}} = \dfrac{1}{\sqrt{x^2 + y^2}}$, $\quad \partial_y f = \dfrac{y}{\sqrt{x^2 + y^2}\,\big(x + \sqrt{x^2 + y^2}\big)}$.
14. $\partial_x f = \dfrac{(x^2 - y) - x^2}{(x^2 - y)^{3/2}} = -\dfrac{y}{(x^2 - y)^{3/2}}$, $\quad \partial_y f = \dfrac{x}{2(x^2 - y)^{3/2}}$.
15. $\partial_x f = 2xyz^3 + y$, $\quad \partial_y f = x^2 z^3 + x$, $\quad \partial_z f = 3x^2 y z^2 - 1$.
16. $\partial_x f = \sqrt{yz}$, $\quad \partial_y f = \dfrac{x\sqrt{z}}{2\sqrt{y}}$, $\quad \partial_z f = \dfrac{x\sqrt{y}}{2\sqrt{z}}$.
17. $f = e^{\frac{y}{z}\ln x}$ : $\partial_x f = \frac{y}{xz}x^{y/z}$, $\quad \partial_y f = \frac{1}{z}\ln(x)\, x^{y/z}$, $\quad \partial_z f = -\frac{y}{z^2}\ln(x)\, x^{y/z}$.
18. $\partial_x f = \frac{1}{z - t}$, $\quad \partial_y f = -\frac{1}{z - t}$, $\quad \partial_z f = -\frac{x - y}{(z - t)^2}$, $\quad \partial_t f = \frac{x - y}{(z - t)^2}$.
19. $\partial_x f = y^2 z^3 t^4$, $\quad \partial_y f = 2xyz^3 t^4$, $\quad \partial_z f = 3xy^2 z^2 t^4$, $\quad \partial_t f = 4xy^2 z^3 t^3$.
20. $\partial_x f = -3y$, $\quad \partial_y f = 5y^4 - 3x$.
21. $\partial_x f = 2x + 3y$, $\quad \partial_y f = 3x - 30y^4$.
22. $\partial_x f = \cos(e^{xy}) - xye^{xy}\sin(e^{xy})$, $\quad \partial_y f = -x^2 e^{xy}\sin(e^{xy})$.
23. $\partial_x f = \frac{1}{y}$, $\quad \partial_y f = -\frac{x}{y^2}$.
24. Comme 10 : $\partial_x f = yx^{y-1}$, $\quad \partial_y f = \ln(x)\, x^y$.
25. $\partial_x f = \cos(xz) - xz\sin(xz)$, $\quad \partial_y f = \dfrac{-2\sin(y + z)\cos(y + z)}{2 - \sin^2(y + z)}$, $\quad \partial_z f = -x^2\sin(xz) - \dfrac{2\sin(y + z)\cos(y + z)}{2 - \sin^2(y + z)}$.

> **Précision ajoutée :** au n° 8, l'ancienne correction s'arrêtait à $\frac{1 + y^2}{(1 - xy)^2 + (x + y)^2}$ ; l'identité $(1 - xy)^2 + (x + y)^2 = (1 + x^2)(1 + y^2)$ donne la forme simple $\frac{1}{1 + x^2}$.

## Exercice 2 : Dérivées partielles et fonctions d'une variable

**Énoncé.** Soient $f$ et $g$ deux fonctions d'une variable réelle, à valeurs dans $\mathbb{R}$ et dérivables sur $\mathbb{R}$. Pour chacune des fonctions de deux variables $F_i$ suivantes, déterminer les dérivées partielles en fonction de $f'$ et $g'$.

1. $F_1(x, y) = f(x) + g(y)$
2. $F_2(x, y) = f(x)\,g(y)$
3. $F_3(x, y) = \dfrac{f(x)}{g(y)}$

**Correction.** Quand on dérive par rapport à $x$, $g(y)$ est une constante, et inversement.

1. $\partial_x F_1 = f'(x)$ et $\partial_y F_1 = g'(y)$.
2. $\partial_x F_2 = f'(x)\,g(y)$ et $\partial_y F_2 = f(x)\,g'(y)$.
3. Là où $g(y) \ne 0$ : $\partial_x F_3 = \dfrac{f'(x)}{g(y)}$ et $\partial_y F_3 = -\dfrac{f(x)\,g'(y)}{g(y)^2}$.

## Exercice 3 : Continuité et dérivées partielles en (0, 0)

**Énoncé.** Étudier la continuité des fonctions suivantes, ainsi que l'existence et la continuité de leurs dérivées partielles premières :

1. $f_1(x, y) = \dfrac{(x + y)^2}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f_1(0, 0) = 0$ ;
2. $f_2(x, y) = (x^2 + y^2)\sin\Big(\dfrac{1}{\sqrt{x^2 + y^2}}\Big)$ si $(x, y) \ne (0, 0)$, et $f_2(0, 0) = 0$.

**Correction.** Hors de $(0, 0)$, ces fonctions sont des quotients et composées de fonctions $C^1$ dont le dénominateur ne s'annule pas : elles y sont $C^1$. Tout se joue en $(0, 0)$.

**1. $f_1$.**

- *Continuité en $(0,0)$* : en polaires, $f_1 = (\cos\theta + \sin\theta)^2 = 1 + \sin(2\theta)$, qui dépend de $\theta$ : pas de limite, $f_1$ n'est **pas continue** en $(0, 0)$.
- *Dérivées partielles hors de $(0,0)$* : en écrivant $f_1 = 1 + \frac{2xy}{x^2 + y^2}$,
$$\partial_x f_1 = \frac{2y(y^2 - x^2)}{(x^2 + y^2)^2} \qquad \partial_y f_1 = \frac{2x(x^2 - y^2)}{(x^2 + y^2)^2}$$
- *En $(0,0)$* : $f_1(t, 0) = 1$ pour $t \ne 0$, donc $\dfrac{f_1(t, 0) - f_1(0,0)}{t} = \dfrac{1}{t}$ n'a pas de limite finie : $\partial_x f_1(0,0)$ **n'existe pas**. De même $f_1(0, t) = 1$, donc $\partial_y f_1(0,0)$ n'existe pas.

Bilan : $f_1$ est $C^1$ sur $\mathbb{R}^2 \setminus \{(0,0)\}$, mais n'est ni continue ni dérivable (partiellement) en $(0,0)$.

> **Erreurs corrigées :** l'ancienne correction concluait que la dérivée partielle « n'est pas continue » en $(0,0)$, alors qu'elle n'y existe pas (la limite vaut $\pm\infty$), puis écrivait « $f_1$ n'est continue sur $\mathbb{R}^2$ » au lieu de « n'est pas continue ».

**2. $f_2$.** Notons $r = \sqrt{x^2 + y^2}$.

- *Continuité* : $|f_2(x, y)| \le r^2 \to 0 = f_2(0,0)$. Donc $f_2$ est continue sur $\mathbb{R}^2$.
- *Dérivées partielles hors de $(0,0)$* : comme $\partial_x r = \frac{x}{r}$,
$$\partial_x f_2 = 2x\sin\Big(\frac{1}{r}\Big) - \frac{x}{r}\cos\Big(\frac{1}{r}\Big) \qquad \partial_y f_2 = 2y\sin\Big(\frac{1}{r}\Big) - \frac{y}{r}\cos\Big(\frac{1}{r}\Big)$$
- *En $(0,0)$* : $\dfrac{f_2(t, 0) - 0}{t} = t\sin\Big(\dfrac{1}{|t|}\Big) \to 0$, donc $\partial_x f_2(0,0) = 0$, et de même $\partial_y f_2(0,0) = 0$.
- *Continuité des dérivées partielles en $(0,0)$* : avec $u_n = (\frac{1}{n}, 0) \to (0,0)$, on a $r = \frac{1}{n}$ et $\partial_x f_2(u_n) = \frac{2}{n}\sin(n) - \cos(n)$, qui n'a pas de limite. Donc $\partial_x f_2$ n'est pas continue en $(0,0)$ ; de même pour $\partial_y f_2$ avec $(0, \frac{1}{n})$.

Bilan : $f_2$ est continue sur $\mathbb{R}^2$, a des dérivées partielles partout, mais n'est pas $C^1$ sur $\mathbb{R}^2$ (elle l'est sur $\mathbb{R}^2 \setminus \{(0,0)\}$).

> **Remarque :** $f_2$ est pourtant **différentiable** en $(0,0)$, de différentielle nulle, car $|f_2(h, k)| \le h^2 + k^2 = o\big(\|(h,k)\|\big)$. C'est l'exemple classique d'une fonction différentiable qui n'est pas $C^1$.

## Exercice 4 : Continuité et dérivées partielles de xy/(|x| + |y|)

**Énoncé.** Soit $f$ la fonction de $\mathbb{R}^2$ dans $\mathbb{R}$ définie par $f(x, y) = \dfrac{xy}{|x| + |y|}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$.

1. Justifier que $f$ est continue sur $\mathbb{R}^2$.
2. Étudier les dérivées partielles de $f$ en $(0, 0)$.

**Correction.**

**1.** Sur $\mathbb{R}^2 \setminus \{(0,0)\}$, $f$ est un quotient de fonctions continues dont le dénominateur ne s'annule pas : elle y est continue. En $(0,0)$ :
$$|f(x, y) - 0| = |x| \cdot \frac{|y|}{|x| + |y|} \le |x| \to 0$$
car $\frac{|y|}{|x| + |y|} \le 1$. Donc $f$ est continue sur $\mathbb{R}^2$.

**2.** Il faut revenir à la définition : $f(t, 0) = 0$ pour tout $t$, donc
$$\partial_x f(0,0) = \lim_{t \to 0} \frac{f(t, 0) - f(0, 0)}{t} = 0$$
et de même $f(0, t) = 0$ donne $\partial_y f(0,0) = 0$.

> **Erreur corrigée :** l'énoncé de l'ancienne feuille demandait « continue sur $\mathbb{R}$ » ; il s'agit de $\mathbb{R}^2$.

## Exercice 5 : Dérivées partielles d'un minimum

**Énoncé.** Calculer les dérivées partielles de $f(x, y) = \min(x, y^2)$, avec $x, y \ge 0$.

**Correction.** On découpe le quart de plan en deux régions, séparées par la courbe $x = y^2$ (soit $y = \sqrt{x}$) :

- région I, $x < y^2$ : $f(x, y) = x$, donc $\partial_x f = 1$ et $\partial_y f = 0$ ;
- région II, $x > y^2$ : $f(x, y) = y^2$, donc $\partial_x f = 0$ et $\partial_y f = 2y$.

(Chaque région est un ouvert : au voisinage d'un de ses points, $f$ est donnée par une seule formule.)

*Sur la courbe $x_0 = y_0^2$ avec $x_0 > 0$.* On a $f(x_0, y_0) = x_0 = y_0^2$.

- Par rapport à $x$ : pour $t > 0$, $x_0 + t > y_0^2$, donc $f(x_0 + t, y_0) = y_0^2$ et le taux d'accroissement vaut $0$ ; pour $t < 0$, $f(x_0 + t, y_0) = x_0 + t$ et il vaut $1$. Les limites à droite et à gauche diffèrent : $\partial_x f(x_0, y_0)$ n'existe pas.
- Par rapport à $y$ : pour $t > 0$, $f(x_0, y_0 + t) = x_0$, taux $0$ ; pour $t < 0$ (petit), $f(x_0, y_0 + t) = (y_0 + t)^2$, taux $\to 2y_0 \ne 0$. $\partial_y f(x_0, y_0)$ n'existe pas.

*En $(0, 0)$* (dérivées à droite, puisque $x, y \ge 0$) : $f(t, 0) = \min(t, 0) = 0$ et $f(0, t) = \min(0, t^2) = 0$, donc les deux dérivées partielles valent $0$.

> **Erreur corrigée :** l'ancienne correction définissait les deux régions par la même inégalité $x < y^2$ ; la région II est $x > y^2$.

## Exercice 6 : Différentiabilité

**Énoncé.**

1. Soit $a$ un réel non nul. Étudier la différentiabilité au point $(a, 0)$ de la fonction $f$ définie sur $\mathbb{R}^2 \setminus \{(0,0)\}$ par $f(x, y) = \dfrac{x^2 y}{x^2 + |y|}$.
2. Discuter selon la valeur du réel $\alpha$ de la différentiabilité au point $(0,0)$ de $g(x, y) = \dfrac{x^\alpha y}{x^2 + |y|}$ si $(x, y) \ne (0, 0)$, et $g(0, 0) = 0$.

**Correction.** Rappel : $f$ est différentiable en $p$ si ses dérivées partielles existent en $p$ et si
$$\varepsilon(h, k) = \frac{f(p + (h, k)) - f(p) - h\,\partial_x f(p) - k\,\partial_y f(p)}{\|(h, k)\|_2} \xrightarrow[(h,k) \to (0,0)]{} 0$$

**1.** *Dérivées partielles en $(a, 0)$.* $f(x, 0) = 0$ pour tout $x \ne 0$, donc $\partial_x f(a, 0) = 0$. Et
$$\frac{f(a, k) - f(a, 0)}{k} = \frac{a^2}{a^2 + |k|} \xrightarrow[k \to 0]{} 1 \quad (a \ne 0)$$
donc $\partial_y f(a, 0) = 1$.

*Reste.* Comme $f(a, 0) = 0$ :
$$f(a + h, k) - k = k\,\frac{(a + h)^2 - (a + h)^2 - |k|}{(a + h)^2 + |k|} = \frac{-k\,|k|}{(a + h)^2 + |k|}$$
donc, puisque $|k| \le \|(h,k)\|_2$,
$$|\varepsilon(h, k)| = \frac{k^2}{\big((a + h)^2 + |k|\big)\|(h, k)\|_2} \le \frac{|k|}{(a + h)^2} \xrightarrow[(h,k) \to (0,0)]{} \frac{0}{a^2} = 0$$
$f$ est différentiable en $(a, 0)$ et $df_{(a,0)}(h, k) = k$.

**2.** Pour que $x^\alpha$ ait un sens pour tout réel $\alpha$, on lit $|x|^\alpha$ (ou on se restreint à $x > 0$), comme dans l'ancienne correction.

- **$\alpha \le 0$ : pas continue, donc pas différentiable.** $g(\frac{1}{n}, \frac{1}{n}) = \dfrac{n^{-\alpha}\cdot\frac{1}{n}}{\frac{1}{n^2} + \frac{1}{n}} = \dfrac{n^{-\alpha}\, n}{n + 1} \sim n^{-\alpha}$, qui tend vers $1$ si $\alpha = 0$ et vers $+\infty$ si $\alpha < 0$, mais pas vers $g(0,0) = 0$.
- **$\alpha > 0$ : continue.** $|g(x, y)| \le \dfrac{|x|^\alpha |y|}{|y|} = |x|^\alpha \to 0$ (pour $y \ne 0$ ; et $g(x, 0) = 0$). De plus $g(h, 0) = g(0, k) = 0$, donc $\partial_x g(0,0) = \partial_y g(0,0) = 0$ : si $g$ est différentiable en $(0,0)$, sa différentielle est nulle, et il faut étudier $\varepsilon(h, k) = \dfrac{g(h, k)}{\sqrt{h^2 + k^2}}$.
    - **$\alpha > 1$ : différentiable.** $|\varepsilon(h, k)| \le \dfrac{|h|^\alpha}{\sqrt{h^2 + k^2}} \le \dfrac{|h|^\alpha}{|h|} = |h|^{\alpha - 1} \to 0$, et $dg_{(0,0)} = 0$. (On peut aussi montrer que les dérivées partielles sont continues : $g$ est $C^1$.)
    - **$0 < \alpha \le 1$ : pas différentiable.** Sur la diagonale, pour $h > 0$ : $\varepsilon(h, h) = \dfrac{h^{\alpha + 1}}{(h^2 + h)\sqrt{2}\,h} = \dfrac{h^{\alpha - 1}}{\sqrt{2}(1 + h)}$, qui tend vers $\frac{1}{\sqrt{2}}$ si $\alpha = 1$ et vers $+\infty$ si $\alpha < 1$ : pas vers $0$.

## Exercice 7 : Continuité, différentiabilité, gradient

**Énoncé.** Étudier la continuité et la différentiabilité, puis calculer le gradient (lorsqu'il existe), des fonctions suivantes.

> **Note :** la liste de la feuille 2025-2026 n'a pas pu être extraite ; c'est celle de l'ancienne feuille, dont cet exercice est repris.

1. $f_1(x, y) = x^3 + xy$ sur $\mathbb{R}^2$
2. $f_2(x, y) = e^{-x^2 - y^2}$ sur $\mathbb{R}^2$
3. $f_3(x, y) = \ln(1 - x^2 - y^2)$ sur $U = \{x^2 + y^2 < 1\}$
4. $f_4(x, y) = \sqrt{x^2 + y^2 - 1}$ sur $U = \{x^2 + y^2 \ge 1\}$
5. $f_5(x, y) = \sqrt{(x - a)^2 + (y - b)^2}$ sur $\mathbb{R}^2$
6. $f_6(x, y) = \sqrt{x^2 + (1 - y)^2} + \sqrt{(1 - x)^2 + y^2}$ sur $\mathbb{R}^2$
7. $f_7(x, y) = \dfrac{x^3 - y^3}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, $f_7(0, 0) = 0$
8. $f_8(x, y) = \dfrac{\sin(x) - \sin(y)}{x - y}$ si $x \ne y$, $f_8(x, x) = \cos(x)$

**Correction.** Outil principal : une fonction dont les dérivées partielles existent et sont continues sur un ouvert est $C^1$, donc différentiable, sur cet ouvert.

**1.** Polynôme, donc continu. $\partial_x f_1 = 3x^2 + y$ et $\partial_y f_1 = x$ sont continues : $f_1$ est $C^1$ sur $\mathbb{R}^2$ et $\nabla f_1(x, y) = (3x^2 + y,\ x)$.

**2.** Composée de fonctions continues. $\partial_x f_2 = -2x e^{-x^2 - y^2}$ et $\partial_y f_2 = -2y e^{-x^2 - y^2}$ sont continues : $f_2$ est $C^1$ et $\nabla f_2(x, y) = -2e^{-x^2 - y^2}(x,\ y)$.

**3.** Continue sur $U$ (composée, $1 - x^2 - y^2 > 0$). $\partial_x f_3 = \dfrac{-2x}{1 - x^2 - y^2}$ et $\partial_y f_3 = \dfrac{-2y}{1 - x^2 - y^2}$ sont continues sur $U$ : $f_3$ est $C^1$ sur $U$ et $\nabla f_3 = -\dfrac{2}{1 - x^2 - y^2}(x,\ y)$.

**4.** Continue sur $U$ (composée).

- Sur l'intérieur $\{x^2 + y^2 > 1\}$ : $\partial_x f_4 = \dfrac{x}{f_4}$, $\partial_y f_4 = \dfrac{y}{f_4}$, continues : $f_4$ y est $C^1$ et $\nabla f_4 = \dfrac{1}{\sqrt{x^2 + y^2 - 1}}(x,\ y)$.
- Sur le cercle $a^2 + b^2 = 1$ : $\dfrac{f_4(a + h, b) - f_4(a, b)}{h} = \dfrac{\sqrt{2ah + h^2}}{h}$. Si $a = 0$, cela vaut $\frac{|h|}{h} = \pm 1$ selon le signe de $h$ : pas de dérivée partielle (seulement des dérivées à droite et à gauche différentes). Si $a \ne 0$, le taux se comporte comme $\frac{\sqrt{2|a||h|}}{|h|} \to +\infty$ (du côté où il est défini) : pas de dérivée partielle. Même chose par rapport à $y$ : $f_4$ n'est pas différentiable sur le cercle.

**5.** $f_5(M) = \|\overrightarrow{AM}\|_2$ avec $A = (a, b)$ : continue sur $\mathbb{R}^2$.

- Sur $U = \mathbb{R}^2 \setminus \{A\}$ : $\partial_x f_5 = \dfrac{x - a}{f_5}$, $\partial_y f_5 = \dfrac{y - b}{f_5}$, continues : $f_5$ est $C^1$ sur $U$ et $\nabla f_5 = \dfrac{\overrightarrow{AM}}{\|\overrightarrow{AM}\|_2}$ (vecteur unitaire dirigé de $A$ vers $M$).
- En $A$ : $\dfrac{f_5(a + h, b) - 0}{h} = \dfrac{|h|}{h} = \pm 1$ : pas de dérivée partielle, donc pas différentiable.

**6.** $f_6(M) = \|\overrightarrow{AM}\|_2 + \|\overrightarrow{BM}\|_2$ avec $A = (0, 1)$ et $B = (1, 0)$ : continue.

- Sur $U = \mathbb{R}^2 \setminus \{A, B\}$, $f_6$ est $C^1$ et
$$\partial_x f_6 = \frac{x}{\sqrt{x^2 + (y - 1)^2}} + \frac{x - 1}{\sqrt{(x - 1)^2 + y^2}} \qquad \partial_y f_6 = \frac{y - 1}{\sqrt{x^2 + (y - 1)^2}} + \frac{y}{\sqrt{(x - 1)^2 + y^2}}$$
- En $A = (0, 1)$ : $f_6(0, 1) = \sqrt{2}$ et
$$\frac{f_6(h, 1) - f_6(0, 1)}{h} = \frac{|h|}{h} + \frac{\sqrt{h^2 - 2h + 2} - \sqrt{2}}{h} \xrightarrow[h \to 0^\pm]{} \pm 1 - \frac{1}{\sqrt{2}}$$
Les limites à droite et à gauche diffèrent : pas de dérivée partielle par rapport à $x$, donc pas différentiable en $A$. Même chose en $B$.

**7.** *Continuité* : en polaires, $|f_7| = \rho\,|\cos^3\theta - \sin^3\theta| \le 2\rho \to 0$, donc $f_7$ est continue sur $\mathbb{R}^2$.

- Sur $U = \mathbb{R}^2 \setminus \{(0,0)\}$, $f_7$ est $C^1$ et
$$\partial_x f_7 = \frac{x^4 + 3x^2 y^2 + 2xy^3}{(x^2 + y^2)^2} \qquad \partial_y f_7 = -\frac{y^4 + 3x^2 y^2 + 2x^3 y}{(x^2 + y^2)^2}$$
- En $(0,0)$ : $\frac{f_7(h, 0)}{h} = \frac{h^3}{h^3} = 1$ et $\frac{f_7(0, k)}{k} = -1$, donc $\partial_x f_7(0,0) = 1$ et $\partial_y f_7(0,0) = -1$. Si $f_7$ était différentiable en $(0,0)$, on aurait $df(h, k) = h - k$. Or
$$\varepsilon(h, k) = \frac{f_7(h, k) - h + k}{\sqrt{h^2 + k^2}} = \frac{hk(h - k)}{(h^2 + k^2)^{3/2}}$$
et $\varepsilon(h, -h) = \dfrac{-2h^3}{2\sqrt{2}\,|h|^3} = \mp\dfrac{1}{\sqrt{2}}$, qui ne tend pas vers $0$ : $f_7$ n'est pas différentiable en $(0,0)$ (et ses dérivées partielles n'y sont pas continues).

**8.** Posons $a \in \mathbb{R}$.

- *Continuité* : hors de la diagonale, $f_8$ est un quotient de fonctions continues. En $(a, a)$ : $\sin x - \sin y = 2\cos\big(\frac{x+y}{2}\big)\sin\big(\frac{x-y}{2}\big)$, donc pour $x \ne y$,
$$f_8(x, y) = \cos\Big(\frac{x + y}{2}\Big)\frac{\sin\big(\frac{x - y}{2}\big)}{\frac{x - y}{2}} \xrightarrow[(x,y) \to (a,a)]{} \cos(a)$$
et sur la diagonale $f_8(x, x) = \cos x \to \cos a$. Donc $f_8$ est continue sur $\mathbb{R}^2$.
- Sur $U = \{x \ne y\}$, $f_8$ est $C^1$ avec
$$\partial_x f_8 = \frac{\cos x}{x - y} - \frac{\sin x - \sin y}{(x - y)^2} \qquad \partial_y f_8 = \frac{-\cos y}{x - y} + \frac{\sin x - \sin y}{(x - y)^2}$$
- En $(a, a)$, dérivée partielle par rapport à $x$ :
$$\frac{f_8(a + h, a) - \cos a}{h} = \frac{\sin(a)(\cos h - 1) + \cos(a)(\sin h - h)}{h^2} \xrightarrow[h \to 0]{} -\frac{\sin a}{2}$$
et de même $\partial_y f_8(a, a) = -\frac{\sin a}{2}$.
- *Différentiabilité en $(a, a)$.* Posons $\varphi(t) = \sin(a + t) - \sin a - t\cos a + \frac{t^2}{2}\sin a$. Par Taylor, $\varphi'(t) = \cos(a + t) - \cos a + t\sin a = O(t^2)$. Pour $h \ne k$, par le théorème des accroissements finis appliqué à $\varphi$ entre $h$ et $k$ :
$$f_8(a + h, a + k) - \cos a + \frac{h + k}{2}\sin a = \frac{\varphi(h) - \varphi(k)}{h - k} = \varphi'(\xi) = O\big(\max(h^2, k^2)\big)$$
avec $\xi$ entre $h$ et $k$ ; pour $h = k$, c'est $\cos(a + h) - \cos a + h\sin a = O(h^2)$. Dans les deux cas, le reste est $o\big(\|(h, k)\|\big)$ : $f_8$ est différentiable en $(a, a)$, avec $df_{(a,a)}(h, k) = -\frac{\sin a}{2}(h + k)$.

> **Précision ajoutée :** l'ancienne correction faisait un développement limité de $\sin(a + h) - \sin(a + k)$ puis divisait par $h - k$ : le reste $o(h^2) + o(k^2)$, divisé par $h - k$ (qui peut être beaucoup plus petit), n'est pas contrôlé. Le passage par $\varphi$ et les accroissements finis règle ce point. Elle notait aussi $\partial_x f_8(0,0)$ au lieu de $\partial_x f_8(a,a)$.
