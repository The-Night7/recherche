---
source: énoncés de la feuille 2025-2026 et de l'ancien TD11-12 (TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 153 et 154), qui ne contenait aucune correction de ces exercices
transcription: correction entièrement rédigée pour cette transcription
---

# TD9 — Recherche d'extremums (corrigé)

## Exercice 1 : Points critiques et extrema

**Énoncé.** Déterminer les points critiques et les extrema des fonctions $f : \mathbb{R}^2 \to \mathbb{R}$ suivantes :

1. $f(x, y) = x^2 + xy + y^2 - 3x - 6y$
2. $f(x, y) = x^2 + 2y^2 - 2xy - 2y + 5$
3. $f(x, y) = x^3 + y^3$
4. $f(x, y) = (x - y)^2 + (x + y)^3$
5. $f(x, y) = x^3 + y^3 - 3xy$
6. $f(x, y) = x\big(\ln^2(x) + y^2\big)$ (sur le demi-plan $x > 0$)

**Correction.**

> **Complément :** l'ancienne correction ne contenait que l'énoncé de cet exercice ; toute la correction a été rédigée pour cette transcription.

*Méthode.* Sur un ouvert, un extremum local d'une fonction $C^1$ est un **point critique** : $\nabla f = 0$. En un point critique d'une fonction $C^2$, on note $r = \partial_x^2 f$, $s = \partial_x\partial_y f$ et $t = \partial_y^2 f$ :

- si $rt - s^2 > 0$ et $r > 0$ : minimum local ;
- si $rt - s^2 > 0$ et $r < 0$ : maximum local ;
- si $rt - s^2 < 0$ : point col (pas d'extremum) ;
- si $rt - s^2 = 0$ : on ne peut pas conclure, il faut étudier $f$ directement (le signe de $f - f(a)$ près du point $a$).

Pour un extremum **global**, il faut une inégalité valable sur tout le domaine.

**1.** $\nabla f = (2x + y - 3,\ x + 2y - 6) = 0$ donne $y = 3 - 2x$, puis $x + 6 - 4x - 6 = 0$ : un seul point critique, $(0, 3)$. Là, $r = 2$, $s = 1$, $t = 2$ : $rt - s^2 = 3 > 0$ et $r > 0$, **minimum local**, $f(0, 3) = -9$.

Il est **global** : en posant $Y = y - 3$, $f(x, y) = x^2 + xY + Y^2 - 9$, et $x^2 + xY + Y^2 = \big(x + \frac{Y}{2}\big)^2 + \frac{3}{4}Y^2 \ge 0$. Donc $f \ge -9$ partout.

**2.** $\nabla f = (2x - 2y,\ 4y - 2x - 2) = 0$ donne $x = y$, puis $2y - 2 = 0$ : point critique $(1, 1)$. $r = 2$, $s = -2$, $t = 4$ : $rt - s^2 = 4 > 0$, $r > 0$, **minimum local**, $f(1, 1) = 4$.

Il est **global** : avec $X = x - 1$ et $Y = y - 1$, $f = X^2 - 2XY + 2Y^2 + 4 = (X - Y)^2 + Y^2 + 4 \ge 4$.

**3.** $\nabla f = (3x^2, 3y^2) = 0$ seulement en $(0, 0)$, où toutes les dérivées secondes sont nulles : on ne peut pas conclure avec $rt - s^2$. Mais $f(t, 0) = t^3$ change de signe autour de $0$ : **pas d'extremum**.

**4.** $\partial_x f = 2(x - y) + 3(x + y)^2$ et $\partial_y f = -2(x - y) + 3(x + y)^2$. En les additionnant, $6(x + y)^2 = 0$, donc $y = -x$, puis $4x = 0$ : seul point critique $(0, 0)$. Là, $r = t = 2$ et $s = -2$, donc $rt - s^2 = 0$ : on étudie directement. Sur la droite $y = x$, $f(x, x) = 8x^3$ change de signe : **pas d'extremum**.

**5.** $\nabla f = (3x^2 - 3y,\ 3y^2 - 3x) = 0$ donne $y = x^2$ et $x = y^2 = x^4$, soit $x(x^3 - 1) = 0$ : points critiques $(0, 0)$ et $(1, 1)$. Avec $r = 6x$, $s = -3$, $t = 6y$ :

- en $(0,0)$ : $rt - s^2 = -9 < 0$, **point col** ;
- en $(1,1)$ : $rt - s^2 = 36 - 9 = 27 > 0$ et $r = 6 > 0$, **minimum local**, $f(1, 1) = -1$.

Ce minimum n'est pas global : $f(t, 0) = t^3 \to -\infty$ quand $t \to -\infty$.

**6.** Sur $x > 0$ : $\partial_x f = \ln^2 x + 2\ln x + y^2$ et $\partial_y f = 2xy$. $\partial_y f = 0$ impose $y = 0$, puis $\ln x(\ln x + 2) = 0$ : $x = 1$ ou $x = e^{-2}$. Points critiques $(1, 0)$ et $(e^{-2}, 0)$. Avec $r = \frac{2(\ln x + 1)}{x}$, $s = 2y$, $t = 2x$ :

- en $(1, 0)$ : $r = 2$, $s = 0$, $t = 2$, $rt - s^2 = 4 > 0$, **minimum local**, $f(1, 0) = 0$. Il est **global** : $f(x, y) = x(\ln^2 x + y^2) \ge 0$ pour $x > 0$.
- en $(e^{-2}, 0)$ : $r = -2e^2 < 0$ et $t = 2e^{-2} > 0$, donc $rt - s^2 < 0$ : **point col**.

## Exercice 2 : Extrema locaux et globaux

**Énoncé.** Déterminer les extrema locaux et globaux des applications suivantes.

> **Note :** la liste de la feuille 2025-2026 n'a pas pu être extraite ; c'est celle de l'ancienne feuille (ancien exercice 11). Les fonctions $f_9$ à $f_{12}$ reprennent l'exercice 1.

1. $f_1(x, y) = 2x^4 - 3x^2 y$ sur $\mathbb{R}^2$
2. $f_2(x, y) = (y^2 - x^2)(y^2 - 2x^2)$ sur $\mathbb{R}^2$
3. $f_3(x, y) = (x + y)^2 - (x^4 + y^4)$ sur $\mathbb{R}^2$
4. $f_4(x, y) = 4xy + \frac{1}{x} + \frac{1}{y}$ sur $(\mathbb{R}_+^*)^2$
5. $f_5(x, y) = x^4 + y^4 - 2(x - y)^2$ sur $\mathbb{R}^2$
6. $f_6(x, y) = 3xy - x^3 - y^3$ sur $\mathbb{R}^2$
7. $f_7(x, y) = x^3 + y^3 - 9xy + 27$ sur $\mathbb{R}^2$
8. $f_8(x, y) = x\ln(y) - y\ln(x)$ sur $(\mathbb{R}_+^*)^2$
9. $f_9(x, y) = x^2 + xy + y^2 - 3x - 6y$
10. $f_{10}(x, y) = x^2 + 2y^2 - 2xy - 2y + 5$
11. $f_{11}(x, y) = x^3 + y^3$
12. $f_{12}(x, y) = (x - y)^2 + (x + y)^3$
13. $f_{13}(x, y) = x^4 + y^4 - 4xy$

**Correction.** Même méthode qu'à l'exercice 1.

> **Complément :** l'ancienne correction ne contenait que l'énoncé de cet exercice ; toute la correction a été rédigée pour cette transcription.

**1. $f_1 = x^2(2x^2 - 3y)$.** $\partial_x f_1 = 8x^3 - 6xy$ et $\partial_y f_1 = -3x^2$ : les points critiques sont **tous les points $(0, y_0)$** de l'axe des ordonnées, où $f_1 = 0$. Là $r = -6y_0$, $s = 0$, $t = 0$ : $rt - s^2 = 0$, on étudie le signe de $f_1 = x^2(2x^2 - 3y)$ :

- si $y_0 > 0$ : près de $(0, y_0)$, $y > \frac{y_0}{2}$ et $x^2 < \frac{3y_0}{4}$, donc $2x^2 - 3y < 0$ et $f_1 \le 0$ : **maximum local** (non strict) ;
- si $y_0 < 0$ : de même $f_1 \ge 0$ près du point : **minimum local** (non strict) ;
- si $y_0 = 0$ : $f_1(x, 0) = 2x^4 > 0$ et $f_1(x, x^2) = -x^4 < 0$ : pas d'extremum.

Pas d'extremum global : $f_1(x, 0) \to +\infty$ et $f_1(1, y) = 2 - 3y \to -\infty$.

**2. $f_2 = y^4 - 3x^2y^2 + 2x^4$.** $\partial_x f_2 = 2x(4x^2 - 3y^2)$ et $\partial_y f_2 = 2y(2y^2 - 3x^2)$. Si $x = 0$, alors $y = 0$ ; si $4x^2 = 3y^2$ avec $x \ne 0$, alors $\partial_y f_2 = 2y\big(2y^2 - \frac{9}{4}y^2\big) = -\frac{y^3}{2} = 0$ impose $y = 0$, puis $x = 0$ : contradiction. Seul point critique : $(0, 0)$, où $f_2 = 0$ et toutes les dérivées secondes sont nulles. Mais $f_2(x, 0) = 2x^4 > 0$, tandis que sur les droites $y = \pm\sqrt{3/2}\,x$ (situées entre les droites $y = \pm x$ et $y = \pm\sqrt{2}\,x$, où $f_2$ s'annule), $f_2 = \frac{1}{2}x^2 \cdot \big(-\frac{1}{2}x^2\big) = -\frac{x^4}{4} < 0$ : **pas d'extremum**, ni local ni global.

**3.** $\partial_x f_3 = 2(x + y) - 4x^3$ et $\partial_y f_3 = 2(x + y) - 4y^3$. Leur différence donne $x^3 = y^3$, donc $x = y$, puis $4x - 4x^3 = 0$ : points critiques $(0, 0)$, $(1, 1)$ et $(-1, -1)$. Avec $r = 2 - 12x^2$, $s = 2$, $t = 2 - 12y^2$ :

- en $(\pm 1, \pm 1)$ : $r = t = -10$, $rt - s^2 = 96 > 0$, $r < 0$ : **maximum local**, de valeur $4 - 2 = 2$ ;
- en $(0, 0)$ : $rt - s^2 = 0$ ; $f_3(x, -x) = -2x^4 < 0$ et $f_3(x, x) = 4x^2 - 2x^4 > 0$ pour $x$ petit : pas d'extremum.

Le maximum $2$ est **global** : $(x + y)^2 \le 2(x^2 + y^2)$ et, comme $(x^2 - 1)^2 \ge 0$, $x^4 \ge 2x^2 - 1$ ; donc
$$f_3 \le 2(x^2 + y^2) - \big(2x^2 - 1 + 2y^2 - 1\big) = 2$$
Pas de minimum global : $f_3(x, 0) = x^2 - x^4 \to -\infty$.

**4.** $\partial_x f_4 = 4y - \frac{1}{x^2}$ et $\partial_y f_4 = 4x - \frac{1}{y^2}$. Donc $y = \frac{1}{4x^2}$ et $x = \frac{1}{4y^2} = 4x^4$, soit $x^3 = \frac{1}{4}$ ; puis $y = x$. Seul point critique : $x = y = 4^{-1/3}$. Là, $r = \frac{2}{x^3} = 8$, $t = 8$, $s = 4$ : $rt - s^2 = 48 > 0$, $r > 0$, **minimum local**, de valeur $4x^2 + \frac{2}{x} = 3 \cdot 4^{1/3} = 3\sqrt[3]{4}$.

Il est **global** : par l'inégalité arithmético-géométrique appliquée aux trois nombres positifs $4xy$, $\frac{1}{x}$, $\frac{1}{y}$, dont le produit vaut $4$,
$$4xy + \frac{1}{x} + \frac{1}{y} \ge 3\sqrt[3]{4xy \cdot \frac{1}{x} \cdot \frac{1}{y}} = 3\sqrt[3]{4}$$
Pas de maximum ($f_4(x, x) \to +\infty$ quand $x \to 0^+$).

**5.** $\partial_x f_5 = 4x^3 - 4(x - y)$ et $\partial_y f_5 = 4y^3 + 4(x - y)$. En les additionnant, $x^3 + y^3 = 0$, donc $y = -x$, puis $x^3 - 2x = 0$ : points critiques $(0, 0)$, $(\sqrt{2}, -\sqrt{2})$ et $(-\sqrt{2}, \sqrt{2})$. Avec $r = 12x^2 - 4$, $s = 4$, $t = 12y^2 - 4$ :

- en $(\pm\sqrt{2}, \mp\sqrt{2})$ : $r = t = 20$, $rt - s^2 = 384 > 0$ : **minimum local**, de valeur $4 + 4 - 2 \cdot 8 = -8$ ;
- en $(0, 0)$ : $rt - s^2 = 0$ ; $f_5(x, x) = 2x^4 > 0$ et $f_5(x, 0) = x^4 - 2x^2 < 0$ pour $x$ petit : pas d'extremum.

Le minimum $-8$ est **global** : $(x - y)^2 \le 2(x^2 + y^2)$, donc
$$f_5 \ge x^4 + y^4 - 4x^2 - 4y^2 = (x^2 - 2)^2 + (y^2 - 2)^2 - 8 \ge -8$$
Pas de maximum global ($f_5(x, x) = 2x^4 \to +\infty$).

**6. $f_6 = -(x^3 + y^3 - 3xy)$** : d'après l'exercice 1.5, les points critiques sont $(0, 0)$ (**col**) et $(1, 1)$, où $r = -6$, $s = 3$, $t = -6$ : $rt - s^2 = 27 > 0$, $r < 0$, **maximum local**, $f_6(1, 1) = 1$. Pas global : $f_6(x, 0) = -x^3 \to +\infty$ quand $x \to -\infty$.

**7.** $\nabla f_7 = (3x^2 - 9y,\ 3y^2 - 9x) = 0$ donne $y = \frac{x^2}{3}$ et $x = \frac{y^2}{3} = \frac{x^4}{27}$, soit $x(x^3 - 27) = 0$ : points critiques $(0, 0)$ et $(3, 3)$. Avec $r = 6x$, $s = -9$, $t = 6y$ :

- en $(0, 0)$ : $rt - s^2 = -81 < 0$, **col** ;
- en $(3, 3)$ : $rt - s^2 = 324 - 81 = 243 > 0$, $r > 0$, **minimum local**, $f_7(3, 3) = 0$. Pas global : $f_7(x, 0) = x^3 + 27 \to -\infty$.

**8.** $\partial_x f_8 = \ln y - \frac{y}{x}$ et $\partial_y f_8 = \frac{x}{y} - \ln x$. Un point critique vérifie $\ln y = \frac{y}{x}$ et $\ln x = \frac{x}{y}$. Posons $\tau = \frac{y}{x} > 0$ : alors $\ln y = \tau$ et $\ln x = \frac{1}{\tau}$, donc $\tau = \frac{y}{x} = e^{\tau - 1/\tau}$, soit $\ln\tau = \tau - \frac{1}{\tau}$. La fonction $\tau \mapsto \tau - \frac{1}{\tau} - \ln\tau$ a pour dérivée $\frac{\tau^2 - \tau + 1}{\tau^2} > 0$ et s'annule en $\tau = 1$ : c'est la seule solution. D'où $x = y = e$. En $(e, e)$ : $r = \frac{y}{x^2} = \frac{1}{e}$, $t = -\frac{x}{y^2} = -\frac{1}{e}$, $s = \frac{1}{y} - \frac{1}{x} = 0$ : $rt - s^2 < 0$, **col**. $f_8$ n'a aucun extremum.

**9 à 12.** Voir l'exercice 1 :

- $f_9$ : minimum global $-9$ en $(0, 3)$ ;
- $f_{10}$ : minimum global $4$ en $(1, 1)$ ;
- $f_{11}$ et $f_{12}$ : aucun extremum.

**13.** $\nabla f_{13} = (4x^3 - 4y,\ 4y^3 - 4x) = 0$ donne $y = x^3$ et $x = y^3 = x^9$, soit $x(x^8 - 1) = 0$ : points critiques $(0, 0)$, $(1, 1)$ et $(-1, -1)$. Avec $r = 12x^2$, $s = -4$, $t = 12y^2$ :

- en $(0, 0)$ : $rt - s^2 = -16 < 0$, **col** ;
- en $(\pm 1, \pm 1)$ : $rt - s^2 = 144 - 16 > 0$, $r > 0$, **minimum local**, de valeur $1 + 1 - 4 = -2$.

Il est **global** : comme $x^4 + y^4 \ge 2x^2y^2$ (car $(x^2 - y^2)^2 \ge 0$),
$$f_{13} + 2 \ge 2x^2y^2 - 4xy + 2 = 2(xy - 1)^2 \ge 0$$
Pas de maximum global ($f_{13}(x, 0) = x^4 \to +\infty$).
