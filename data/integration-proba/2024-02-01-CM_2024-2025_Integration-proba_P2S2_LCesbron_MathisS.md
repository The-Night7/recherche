---
title: CM Intégration et probabilités
author: [MathisS]
cyauthor: [LCesbron]
date: 2025-02-25 15:30:18 +0100
categories: [PREING2 S2,Integration-proba]
tags: [PREING2 S2,Algebre-lineaire,2024/2025,Mathis S.,L. Cesbron]
math: true
division_title : 2024/2025
---

# Chapitre 1 : Intégration

## I.  Intégrale généralisée

<!-- -->

### 1.  Notion d'intégrale généralisée

**Définition :**

Soient $- \infty \leq a < b \leq + \infty$ et $f$ une fonction continue
(ou continue par morceaux) sur $\rbrack a,b\lbrack$. On appelle
intégrale impropre (ou généralisée) de $f$ sur $\rbrack a,b\lbrack$
l'intégrale :

$$\int_{a}^{b}{f(t)dt}$$

**Notations :**

$$\int_{a}^{b}{f(t)dt}\ \text{ou}\ \int_{a}^{b}f$$

**Intégrale généralisée : Borne supérieure**

On considère les intervalles $\lbrack a,b\lbrack$ avec
$b \in \rbrack a\ ; + \infty\rbrack$

Toutes les définitions et propriétés peuvent être définies de façon
analogue dans le cas d'un intervalle $\rbrack a,b\rbrack$ avec
$a \in \lbrack - \infty\ ;b\lbrack$

**Définition :**

Soit $f$ une fonction continue de $\lbrack a,b\lbrack$ dans
$\mathbb{R}$. Soit $F$ la fonction définie par :

$$F(x) = \int_{a}^{x}{f(t)dt}$$

Si $\lim_{x \rightarrow b^{-}}{F(x)}$ existe, alors on dit que
$\int_{a}^{b}f$ est convergente. Dans le cas contraire, elle est dite
divergente.

Donner la nature d'une intégrale est dire si elle est convergente ou
divergente.

**Exemple :**

1.  Déterminer la nature de $\int_{0}^{1}{\frac{1}{\sqrt{1 - t}}dt}$

Pour tout $x \in \lbrack 0,1\lbrack$, on note
$F:x \rightarrow \int_{0}^{1}{\frac{1}{\sqrt{1 - t}}dt}$.

On a
$F(x) = \int_{0}^{x}{\frac{1}{\sqrt{1 - t}}dt} = \left\lbrack - 2\sqrt{1 - t} \right\rbrack_{0}^{x} = - 2\sqrt{1 - x} + 2$
et $\lim_{x \rightarrow 1^{-}}{F(x)} = 2$

$F$ admet une limite quand $x \rightarrow 1^{-}$ donc
$\int_{0}^{1}{\frac{1}{\sqrt{1 - t}}dt}$ est convergente

$$\int_{0}^{1}{\frac{1}{\sqrt{1 - t}}dt} = 2$$

2.  Déterminer la nature $\int_{1}^{+ \infty}{\frac{1}{\sqrt{t}}dt}$

Pour tout $x \in \rbrack 1\ ; + \infty\lbrack$, on pose
$F\ :x \rightarrow \int_{1}^{x}{\frac{1}{\sqrt{t}}dt}$

On a
$F(x) = \int_{1}^{x}{\frac{1}{\sqrt{t}}dt} = \left\lbrack 2\sqrt{t} \right\rbrack_{1}^{x} = 2\sqrt{x} - 2$
et $\lim_{x \rightarrow + \infty}{F(x)} = + \infty$ donc l'intégrale
$\int_{1}^{+ \infty}{\frac{1}{\sqrt{t}}dt}$ est divergente.

**Proposition :**

Soit $f$ une fonction continue sur $\lbrack a,b\lbrack$.

$$\forall c \in \lbrack a,b\lbrack,\ \text{la nature de}\ \int_{c}^{b}f\ \text{ne dépend pas de}\ c$$

**Remarque :**

La nature ne dépend pas de $c$ mais en cas de convergence la valeur en
dépend.

**Intégrale généralisée : Intervalle quelconque**

**Définition :**

Soient $a,b \in \overline{\mathbb{R}}$
($\overline{\mathbb{R}}\mathbb{= R \cup}\left\lbrace  - \infty, + \infty \right\rbrace $).

Soit $f$ une fonction continue sur $\rbrack a,b\lbrack$

On dit que l'intégrale généralisée $\int_{a}^{b}f$ converge s'il existe
un $c \in \rbrack a,b\lbrack$ tel que $\int_{a}^{c}f$ et $\int_{c}^{b}f$
convergent.

Dans le cas contraire, on dit que $\int_{a}^{b}f$ diverge.

La nature de l'intégrale ne dépend pas du $c$.

**Remarque :**

On définit par convention
$\forall a\mathbb{\in R,}\int_{a}^{a}f = 0,\ \int_{b}^{a}f = - \int_{a}^{b}f$

**Exemples :**

...

**Remarque :**

Si $f$ est continue sur $\lbrack a,c\lbrack \cup \rbrack c,b\rbrack$ et
$\int_{a}^{c}f$ et $\int_{c}^{b}f$ convergent alors $\int_{a}^{b}f$
converge.

**Propriété :** Linéarité de l'intégration

Soient $f$ et $g$ deux fonctions continues sur $\rbrack a,b\lbrack$
($a,b\mathbb{\in R,\ }a < b$). Soit $\lambda\mathbb{\in R}$

Si $\int_{a}^{b}{\ f}$ et $\int_{a}^{b}g$ convergent alors
$\int_{a}^{b}{\lambda f + g}$ converge et

$$\int_{a}^{b}{\lambda f + g} = \lambda\int_{a}^{b}f + \int_{a}^{b}g$$

**Remarque :**

La réciproque est fausse. On peut avoir $\int_{a}^{b}{\lambda f + g}$
convergente mais $\int_{a}^{b}f$ et $\int_{a}^{b}g$ divergentes.

**Proposition :** Prolongement par continuité

Soit $a,b\mathbb{\in R}$ et $f$ une fonction continue sur
$\lbrack a,b\lbrack$

Si $f$ admet un prolongement par continuité en $b$, càd il existe une
fonction $\widetilde{f}$ continue sur $\lbrack a,b\lbrack$ telle que :

$$\left\lbrace  \begin{array}{r}
\forall x \in \lbrack a,b\lbrack,\ f(x) = \widetilde{f}(x) \\
\lim_{x \rightarrow b^{-}}{f(x)} = \widetilde{f}(b)
\end{array} \right. $$

Alors $\int_{a}^{b}f$ converge et
$\int_{a}^{b}f = \int_{a}^{b}\widetilde{f}$

**Exemple :**

$$\int_{0}^{1}{\frac{\sin(t)}{t}dt}$$

$f:t \rightarrow \frac{\sin(t)}{t}$ est continue sur
$\rbrack 0,1\rbrack$ et
$\lim_{t \rightarrow 0^{+}}\frac{\sin(t)}{t} = 1$ donc $f$ est
prolongeable par continuité en

$$\widetilde{f}:t \rightarrow \left\lbrace  \begin{array}{r}
\frac{\sin(t)}{t}\ \text{si}\ t \in \text{[}0,1\text{[} \\
1\ \text{si}\ t = 0
\end{array} \right. $$

### 2.  Intégrales généralisées usuelles

**Proposition :** Intégrale de Riemann

Soit $\alpha\mathbb{\in R}$

$$\text{L'intégrale}\ \int_{0}^{1}{\frac{1}{t^{\alpha}}dt}\ \text{converge si et seulement si}\ \alpha < 1$$

$$\text{L'intégrale}\ \int_{1}^{+ \infty}{\frac{1}{t^{\alpha}}dt}\ \text{converge si et seulement si}\ \alpha > 1$$

**Démonstration :**

...

**Corollaire :**

Soit $\alpha\mathbb{\in R}$. Soit $a,b \in \mathbb{R}_{+}^{*}$

$$\int_{a}^{b}{\frac{1}{(t - a)^{\alpha}}dt}\ \text{converge si et seulement si}\ \alpha < 1$$

$$\int_{a}^{b}{\frac{1}{(b - t)^{\alpha}}dt}\ \text{converge si et seulement si}\ \alpha < 1$$

**Proposition :** Intégrale logarithmique

L'intégrale $\int_{0}^{1}{\ln(t)dt}$ converge et
$\int_{0}^{1}{\ln(t)dt} = - 1$

L'intégrale $\int_{1}^{+ \infty}{\ln(t)dt}\ \text{diverge}$

**Démonstration :**

Calcul direct. Une primitive de $t \rightarrow \ln(t)$ est
$t \rightarrow t\ln(t) - t$

**Proposition :** Intégrale exponentielle

Soit $\alpha\mathbb{\in R}$

L'intégrale $\int_{0}^{+ \infty}{e^{- \alpha t}dt}$ converge si et
seulement si $\alpha > 0$

**Démonstration :** Calcul direct

### 3.  Intégrales de fonctions de signe constant

Dans toute cette partie, on considère un intervalle $\lbrack a,b\lbrack$
avec $b \in \rbrack a\ ; + \infty\rbrack$, $a\mathbb{\in R}$

Toutes les propositions peuvent être écrites de façon analogue pour des
intervalles $\rbrack a,b\rbrack$ ou $\rbrack a,b\lbrack$

**Proposition :** Monotonie de l'intégrale de fonctions
positives

Soit $f$ une fonction continue et positive sur $\lbrack a,b\lbrack$.

L'intégrale $\int_{a}^{b}f$ converge si et seulement si la fonction
$F\ :x \rightarrow \int_{a}^{x}f$ est majorée sur $\lbrack a,b\lbrack$

**Démonstration :**

...

**Théorème :** Comparaison des intégrales de fonctions
positives

Soit un intervalle $\lbrack a,b\lbrack$ avec
$b \in \rbrack a\ ; + \infty\rbrack,$ $a\mathbb{\in R}$

Soient $f$ et $g$ deux fonctions continues et positives sur
$\lbrack a,b\lbrack$

Si $\forall t \in \lbrack a,b\lbrack,\ f(t) \leq g(t)$, alors :

-   Si $\int_{a}^{b}g$ converge alors $\int_{a}^{b}f$ converge

-   Si $\int_{a}^{b}f$ diverge alors $\int_{a}^{b}g$ diverge

**Démonstration :**

...

**Remarque :**

-   Si $f$ et $g$ sont négatives sur $\lbrack a,b\lbrack$, alors la
    propriété reste vraie en inversant les inégalités

-   Le résultat reste vrai si les hypothèses sont vérifiées sur un
    voisinage de $b$

**Exemples :**

...

**Lemme de Riemann :**

Soit $f$ une fonction continue et positive sur $\rbrack 0\ ;1\rbrack$

S'il existe $\alpha < 1$ tel que
$\lim_{t \rightarrow 0}{t^{\alpha}f(t)} = l\mathbb{\in R}$, alors
$\int_{0}^{1}f$ converge.

S'il existe $\alpha \geq 1$ tel que
$\lim_{t \rightarrow 0}{t^{\alpha}f(t)}$ existe et
$\lim_{t \rightarrow 0}{t^{\alpha}f(t)} = l \neq 0$, alors
$\int_{0}^{1}f$ diverge.

Soit $f$ une fonction continue et positive sur
$\lbrack 1\ ; + \infty\lbrack$

S'il existe $\alpha > 1$ tel que
$\lim_{t \rightarrow + \infty}{t^{\alpha}f(t)} = l\mathbb{\in R}$, alors
$\int_{1}^{+ \infty}f$ converge.

S'il existe $\alpha \leq 1$ tel que
$\lim_{t \rightarrow 0}{t^{\alpha}f(t)}$ existe et
$\lim_{t \rightarrow 0}{t^{\alpha}f(t)} = l \neq 0$, alors
$\int_{1}^{+ \infty}f$ diverge.

**Théorème :** Equivalence par l'intégrale de fonction de
signe constant

Soit un intervalle $\lbrack a,b\lbrack$ avec
$b \in \rbrack a\ ; + \infty\rbrack,\ a\mathbb{\in R}$

Soient $f$ et $g$ deux fonctions continues sur $\lbrack a,b\lbrack$, de
signe constant et non-nulles au voisinage de $b$.

Si $f(t)\ \sim_{t \rightarrow b}\ g(t)$, alors $\int_{a}^{b}f$ et
$\int_{a}^{b}g$ sont de même nature.

**Corollaire du théorème de comparaison :** Condition
nécessaire de convergence

Soit $f$ une fonction continue sur $\lbrack a, + \infty\lbrack$ et
$a\mathbb{\in R}$

Si $\lim_{t \rightarrow + \infty}{f(t)} \neq 0$, alors
$\int_{a}^{+ \infty}f$ diverge.

**Exemple :**

$$\int_{1}^{+ \infty}{\left( e^{6} - \left( 1 + \frac{3}{t} \right)^{2t} \right)dt}$$

$$\text{Posons}\ f:t \rightarrow e^{6} - \left( 1 + \frac{3}{t} \right)^{2t}$$

Cherchons un équivalent de $f$ lorsque $t \rightarrow + \infty$.

$$\left( 1 + \frac{3}{t} \right)^{2t} = e^{2t\ln\left( 1 + \frac{3}{t} \right)} = e^{2t\left( \frac{3}{t} - \frac{1}{2}\left( \frac{3}{t} \right)^{2} + o\left( \frac{1}{t^{2}} \right) \right)} = e^{6 - \frac{9}{t} + o\left( \frac{1}{t} \right)}$$

$$f(t) = e^{6} - e^{6 - \frac{9}{t} + o\left( \frac{1}{t} \right)} = e^{6}\left( 1 - e^{- \frac{9}{t} + o\left( \frac{1}{t} \right)} \right) = e^{6}\left( 1 - \left( 1 - \frac{9}{t} + o\left( \frac{1}{t} \right) \right) \right) = \frac{9e^{6}}{t} + o\left( \frac{1}{t} \right)$$

$$\text{On en déduit que}\ f(t)\sim_{t \rightarrow + \infty}\frac{9e^{6}}{t} = g(t)\ \text{où}\ g\ \text{est une fonctions de signe constant}\ ( > 0)\text{ et non-nulle}$$

Or $\int_{1}^{+ \infty}g$ diverge car intégrale de Riemann avec
$\alpha = 1 \leq 1$

Donc, d'après le théorème d'équivalence.

### 4.  Calcul intégral

**Proposition :** Relation de Chasles

Soient $a,b \in \overline{\mathbb{R}}$ et $f$ une fonction continue sur
$\rbrack a,b\lbrack$.

Si $\int_{a}^{b}f$ converge, alors
$\forall c \in \rbrack a,b\lbrack,\ \int_{a}^{b}f = \int_{a}^{c}f + \int_{c}^{b}f$

**Proposition :** Changement de variable

Soient $a,b \in \overline{\mathbb{R}}$ et $f$ une fonction continue sur
$\rbrack a,b\lbrack$.

Soit $\varphi:\rbrack\alpha,\beta\lbrack,\ \rbrack a,b\lbrack$ est une
bijection de classe $C^{1}$ sur $\rbrack a,b\lbrack$

Alors $\int_{a}^{b}f$ et
$\int_{\alpha}^{\beta}{f\left( \varphi(u) \right)\varphi^{'}(u)du}$ sont
de même nature. En cas de convergence,

$$\int_{a}^{b}f = \int_{\alpha}^{\beta}{f\left( \varphi(u) \right)\varphi^{'}(u)du}$$

**Remarque :**

Si $\varphi$ est strictement monotone sur $\rbrack\alpha,\beta\lbrack$,
alors elle est bijective.

Si $\varphi$ est croissante ($\varphi^{'}(u) > 0$),
$\varphi(\alpha) = a$ et $\varphi(\beta) = b$

Si $\varphi$ est décroissante ($\varphi^{'}(u) < 0$),
$\varphi(\alpha) = b$ et $\varphi(\beta) = a$

**Exercice :**

$$\text{Calculer}\ \int_{0}^{1}{\frac{t}{\sqrt{1 - t^{2}}}dt}$$

Avec le changement de variable $u = t^{2}$

La fonction $\varphi\ :u \rightarrow \sqrt{u}$ est bien bijective est
$C^{1}$ sur $\rbrack 0\ ;1\rbrack$

$$\varphi^{'}(u) = \frac{1}{2\sqrt{u}},\ \varphi(0) = 0,\ \varphi(1) = 1$$

On s'intéresse à l'intégrale :

$$\int_{0}^{1}{\frac{\sqrt{u}}{\sqrt{1 - u}} \times \frac{1}{2\sqrt{u}}du} = \frac{1}{2}\int_{0}^{1}{\frac{1}{\sqrt{1 - u}}du}$$

On reconnait une intégrale de Riemann en 0 avec
$\alpha = \frac{1}{2} < 1$ donc $\int_{0}^{1}\frac{1}{\sqrt{1 - u}}$
converge.

Alors :

$$\int_{0}^{1}{\frac{t}{\sqrt{1 - t^{2}}}dt} = \frac{1}{2}\int_{0}^{1}{\frac{1}{\sqrt{1 - u}}du} = \left\lbrack - \sqrt{1 - u} \right\rbrack_{0}^{1} = 1$$

**Proposition :** Intégration par parties

Soient $a,b \in \overline{\mathbb{R}}$ et deux fonctions $f$ et $g$ deux
fonctions $C^{1}$ sur $\rbrack a,b\lbrack$.

Si le produit $fg$ admet des limites en $a$ et $b\ $:

$\lim_{t \rightarrow a^{+}}{f(t)g(t)} = l_{a}\mathbb{\in R}$ et
$\lim_{t \rightarrow b^{-}}{f(t)g(t)} = l_{b}\mathbb{\in R}$, alors :

Alors $\int_{a}^{b}{f^{'}g}$ et $\int_{a}^{b}{fg^{'}}$ sont de même
nature et

$$\int_{a}^{b}{f^{'}g} = \lbrack fg\rbrack_{a}^{b} - \int_{a}^{b}{fg^{'}}$$

**Démonstration :**

Soient $\alpha,\beta\mathbb{\in R}$ tels que $a < \alpha < \beta < b$.

Les fonctions $f$ et $g$ sont $C^{1}$ sur $\lbrack\alpha,\beta\rbrack$
donc on peut faire une intégration par parties sur ce segment :

$$\int_{\alpha}^{\beta}{f^{'}g} = \lbrack fg\rbrack_{\alpha}^{\beta} - \int_{\alpha}^{\beta}{fg^{'}}$$

Si $\lim_{\alpha \rightarrow a^{+}}{f(\alpha)g(\alpha)}$ et
$\lim_{\beta \rightarrow b^{-}}{f(\beta)g(\beta)}$ existent toutes les
deux, alors $\int_{a}^{b}{f^{'}g}$ et $\int_{a}^{b}{fg^{'}}$ ont la même
nature puisque leur somme est un nombre réel $( < + \infty)$.

Si elles convergent, on peut passer à la limite dans l'égalité :

$$\int_{a}^{b}{f^{'}g} = \lbrack fg\rbrack_{a}^{b} - \int_{a}^{b}{fg^{'}}$$

**Exemple :**

$$\int_{0}^{+ \infty}{te^{- t}dt}$$

### 5.  Fonctions intégrables

Dans cette section, $I$ est un intervalle, $a$ et $b$ sont ses bornes
inférieures et supérieures ($\in \overline{\mathbb{R}}$).

**Définition :**

Soit $f$ une fonction continue sur $I$.

On dit que $f$ est intégrable sur $I$ si $\int_{a}^{b}\vert f\vert $ converge.

**Attention :**

$\int_{a}^{b}f$ convergente n'implique pas que $f$ est intégrable.

**Proposition :** Inégalité triangulaire

Soit $I$ un intervalle et $f$ continue et intégrable sur $I$. On a :

$$\left\vert  \int_{I}^{}f \right\vert  \leq \int_{I}^{}\vert f\vert $$

**Démonstration :**

On peut décomposer toute fonction continue $f$ de manière unique en sa
partie positive $f_{+}$ et sa partie négative $f_{-}\ $:
$f = f_{+} - f_{-}$ avec $f_{\pm} > 0$

$$\left\vert  \int_{I}^{}f \right\vert  = \left\vert  \int_{I}^{}f_{+} - \int_{I}^{}f_{-} \right\vert  \leq \left\vert  \int_{I}^{}f_{+} \right\vert  + \left\vert  \int_{I}^{}f_{-} \right\vert  = \int_{I}^{}f_{+} + \int_{I}^{}f_{-} = \int_{I}^{}{f_{+} + f_{-}} = \int_{I}^{}\vert f\vert $$

**Exemples :**

$t \rightarrow e^{- t}$ est intégrable sur $\mathbb{R}_{+}$

$t \rightarrow \frac{1}{t^{2}}$ est intégrable sur
$\lbrack 1\ ; + \infty\lbrack$ et non-intégrable sur
$\rbrack 0\ ;1\rbrack$

$t \rightarrow \frac{\sin\left( e^{t} \right)}{1 + t^{2}}$ est
intégrable sur $\mathbb{R}$ par équivalence avec une inégalité de
Riemann convergente.

**Proposition :**

Soit $f$ une fonction continue sur $I$. Si $f$ est intégrable, alors
$\int_{I}^{}f$ converge.

**Attention :** La réciproque est fausse.

**Proposition :**

L'ensemble des fonctions continues et intégrables sur $I$ et à valeurs
dans $\mathbb{K}$ est un $\mathbb{K}$-espace vectoriel noté
$L^{1}\left( I,\mathbb{K} \right)$

**Proposition :**

Soient $f$ et $g \in L^{1}\left( I\mathbb{,R} \right)$.

-   Si $f$ est positive sur $I$, alors $\int_{I}^{}f \geq 0$

-   Si $\forall t\mathbb{\in R}$, $f(t) \leq g(t)$, alors
    $\int_{I}^{}f \leq \int_{I}^{}g$

**Proposition :** Stricte positivité

Soit $f \in L^{1}\left( I\mathbb{,R} \right)$.

$\int_{I}^{}\vert f\vert  = 0 \Leftrightarrow f(t) = 0\ \forall t\mathbb{\in R}$
(f est la fonction nulle).

**Démonstration :** Par l'absurde

Supposons qu'il existe $f$ qui n'est pas la fonction nulle sur $I$ mais
telle que $\int_{I}^{}\vert f\vert  = 0$

Alors $\exists c \in I,\ f(c) = m \neq 0$

Par continuité,
$\forall\varepsilon > 0,\exists\delta > 0,\ \vert t - c\vert  < \delta \Rightarrow f(t) \geq m - \varepsilon$

$$\int_{I}^{}\vert f\vert  = \int_{c - \delta}^{c + \delta}\vert f\vert  + \int_{I\backslash\lbrack c - \delta,c + \delta\rbrack}^{}\vert f\vert $$

$$\int_{I}^{}\vert f\vert  \geq \int_{c - \delta}^{c + \delta}{(m - \varepsilon)dt} = 2\delta(m - \varepsilon) > 0\ \text{(pour}\ \varepsilon\ \text{assez petit})\ \text{donc}$$

$$\int_{I}^{}\vert f\vert  > 0$$

Ce qui est absurde.

**Théorème de comparaison :**

Soient $a\mathbb{\in R,}b \in \rbrack a, + \infty\rbrack$, $f$ et $g$
deux fonctions continues sur $\lbrack a,b\lbrack$.

Si $g$ est intégrable sur $\lbrack a,b\lbrack$ et
$f(t) = Ο_{t \rightarrow b^{-}}\left( g(t) \right)$ alors $f$ est
intégrable sur $\lbrack a,b\lbrack$.

Si $g$ est intégrable sur $\lbrack a,b\lbrack$ et
$f(t) = o_{t \rightarrow b^{-}}\left( g(t) \right)$ alors $f$ est
intégrable sur $\lbrack a,b\lbrack$.

**Remarque :** On peut écrire en analyse ce théorème sur un
intervalle de la forme
$\rbrack a,b\rbrack,b\mathbb{\in R,}a \in \lbrack - \infty,b\rbrack$.

**Exemple :**

$$\text{Etudions l’intégrabilité de}\ t \rightarrow \frac{\sin^{2}(t)}{t^{2}}$$

$$\text{Notons}\ f:t \rightarrow \frac{\sin^{2}(t)}{t^{2}}$$

$f$ est continue sur $\mathbb{R}_{+}^{*}$ par quotient de fonctions
continues dont le dénominateur ne s'annule jamais.

On peut remarquer que
$\lim_{t \rightarrow 0^{+}}\frac{\sin^{2}(t)}{t^{2}} = \lim_{t \rightarrow 0}\frac{t^{2}}{t^{2}} = 1$
car $\sin(t)\ \sim_{t \rightarrow 0}\ t$

Donc $f$ est prolongeable par continuité en 0 donc intégrable au
voisinage de 0.

De plus, pour $t$ grand,

$$\left\vert  \frac{\sin^{2}(t)}{t^{2}} \right\vert  \leq \frac{1}{t^{2}}\ \text{donc}\ f(t) =_{t \rightarrow + \infty}Ο\left( \frac{1}{t^{2}} \right)$$

$$\text{Or}\ t \rightarrow \frac{1}{t^{2}}\ \text{est intégrable sur}\ \lbrack 1; + \infty\lbrack\ \text{comme intégrale de Riemann avec}\ \alpha = 2 > 1$$

Par le théorème de comparaison, on en déduit que $f$ est intégrable.

**Exemple :**

$$\text{Etudions l'intégrabilité de}\ f:t \rightarrow \frac{\sin(t)}{t}\ \text{sur}\ \rbrack 0; + \infty\lbrack.$$

$f$ est prolongeable par continuité en 0 :
$\lim_{t \rightarrow 0^{+}}{f(t)} = 1$

Donc $f$ est intégrable au voisinage de 0.

Pour $t \in \left\lbrack \frac{\pi}{4},\frac{3\pi}{4} \right\rbrack,$

$$\frac{1}{\sqrt{2}} \leq \sin(t) \leq 1$$

$$\frac{\pi}{4} \leq t \leq \frac{3\pi}{4}$$

$$\frac{4}{3\pi\sqrt{2}} \leq \frac{\sin(t)}{t} \leq \frac{4}{\pi}$$

$$\int_{0}^{\pi}{\left\vert  \frac{\sin(t)}{t} \right\vert dt} = \int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}{\left\vert  \frac{\sin(t)}{t} \right\vert dt} + \int_{0}^{\frac{\pi}{4}}{\left\vert  \frac{\sin(t)}{t} \right\vert dt} + \int_{\frac{3\pi}{4}}^{\pi}{\left\vert  \frac{\sin(t)}{t} \right\vert dt}$$

$$\int_{0}^{\pi}{\left\vert  \frac{\sin(t)}{t} \right\vert dt} \geq \int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}{\left\vert  \frac{\sin(t)}{t} \right\vert dt} \geq \int_{\frac{\pi}{4}}^{\frac{3\pi}{4}}{\frac{4}{3\pi\sqrt{2}}dt} = \frac{4}{3\pi\sqrt{2}}\left( \frac{3\pi}{4} - \frac{\pi}{4} \right) = \frac{2}{3\sqrt{2}} = \frac{\sqrt{2}}{3}$$

**Généralisation :** Soit $k\mathbb{\in N}$ et
$t \in \left\lbrack k\pi + \frac{\pi}{4};k\pi + \frac{3\pi}{4} \right\rbrack$

$$\frac{1}{\sqrt{2}} \leq \left\vert  \sin(t) \right\vert  \leq 1$$

$$k\pi + \frac{\pi}{4} \leq t \leq k\pi + \frac{3\pi}{4}$$

$$\frac{4}{\sqrt{2}\left( k\pi + \frac{3\pi}{4} \right)} \leq \left\vert  \frac{\sin(t)}{t} \right\vert $$

Ainsi, $\forall N\mathbb{\in N}$

$$\int_{0}^{N\pi}\left\vert  \frac{\sin(t)}{t} \right\vert  = \sum_{k = 0}^{N - 1}{\int_{k\pi}^{(k + 1)\pi}{\left\vert  \frac{\sin(t)}{t} \right\vert dt}} \geq \sum_{k = 0}^{N - 1}{\int_{k\pi + \frac{\pi}{4}}^{k\pi + \frac{3\pi}{4}}{\left\vert  \frac{\sin(t)}{t} \right\vert dt}} \geq \sum_{k = 0}^{N - 1}{\int_{k\pi + \frac{\pi}{4}}^{k\pi + \frac{3\pi}{4}}{\frac{1}{\sqrt{2}\left( k\pi + \frac{3\pi}{4} \right)}dt}} = \sum_{k = 0}^{N - 1}\frac{\pi}{2\sqrt{2}\left( k\pi + \frac{3\pi}{4} \right)}$$

On reconnait un équivalent de la série harmonique, qui diverge.

Donc
$\lim_{N \rightarrow + \infty}{\int_{0}^{N\pi}\left\vert  \frac{\sin(t)}{t} \right\vert } = + \infty$

On en conclut que $f$ n'est pas intégrable sur
$\rbrack 0\ ; + \infty\lbrack$

Etudions la nature de $\int_{0}^{+ \infty}{\frac{\sin(t)}{t}dt}$

$$f(t) \rightarrow \frac{\sin(t)}{t}\ \text{est prolongeable par continuité en}\ 0\ \text{donc son intégrale au voisinage de 0}\ \text{converge}$$

-   Intégration par parties sur $\lbrack 1; + \infty\lbrack$

$$u^{'}(t) = \sin(t),\ \ u(t) = - \cos(t)$$

$$v(t) = \frac{1}{t},\ \ v^{'}(t) = - \frac{1}{t^{2}}$$

On a :

$$\lim_{t \rightarrow 1}{- \frac{\cos(t)}{t}} = - \cos(1)\mathbb{\in R,}\lim_{t \rightarrow + \infty}{- \frac{\cos(t)}{t}} = 0 \in \mathbb{R}$$

On en déduit que $\int_{1}^{+ \infty}{\frac{\sin(t)}{t}dt}$ et
$\int_{1}^{+ \infty}{\frac{\cos(t)}{t^{2}}dt}$ sont de même nature.

$$\text{Or}\ \left\vert  \frac{\cos(t)}{t^{2}} \right\vert  \leq \frac{1}{t^{2}}\ \text{et}\ t \rightarrow \frac{1}{t^{2}}\ \text{est intégrable sur}\ \lbrack 1; + \infty\lbrack\ \text{donc par comparaison}\ t \rightarrow \left\vert  \frac{\cos(t)}{t^{2}} \right\vert \ \text{est intégrable sur}\ \lbrack 1; + \infty\lbrack$$

On en déduit que $\int_{1}^{+ \infty}{\frac{\cos(t)}{t^{2}}dt}$ converge
donc $\int_{1}^{+ \infty}{\frac{\sin(t)}{t}dt}$ converge.

Comme $\int_{0}^{1}{\frac{\sin(t)}{t}dt}$ converge par prolongement par
continuité, on en conclut que :

$$\int_{0}^{+ \infty}{\frac{\sin(t)}{t}dt}\ \text{converge}$$

## II. Intégrale à paramètre

**Définition :** On appelle intégrale à paramètre les
intégrales du type :

$$\int_{I}^{}{f(t,x)dt}$$

Où $f\mathbb{:R \times}A\mathbb{\rightarrow R}$, $x \in A$ est appelé
paramètre de l'intégrale.

On s'intéresse aux propriétés de la fonction
$x \rightarrow \int_{I}^{}{f(t,x)dt}$

Le domaine de définition de cette fonction est l'ensemble des $x$ tels
que $\int_{I}^{}{f(t,x)dt}$ converge.

**Théorème : Convergence dominée pour une limite**

Soient $I$ et $A$ deux intervalles,
$a \in \overline{A},\ f\ :I \times A\mathbb{\rightarrow R}$

Si :

-   $\forall x \in A,$ la fonction $t \rightarrow f(t,x)$ est continue
    sur $I$

-   $\forall t \in I,\lim_{x \rightarrow a}{f(t,x)} = l(t)\mathbb{\in R}$

-   La fonction $t \rightarrow l(t)$ est continue sur $I$

-   Il existe une fonction intégrable
    $\varphi\ :I\mathbb{\rightarrow R}$ telle que
    $\forall(t,x) \in I \times A,\ \left\vert  f(t,x) \right\vert  \leq \varphi(t)$

Alors $l$ est intégrable sur $I$ et
$\lim_{x \rightarrow a}{\int_{I}^{}{f(t,x)dt}} = \int_{I}^{}{l(t)dt}\left( = \int_{I}^{}{\lim_{x \rightarrow a}{f(t,x)dt}} \right)$

**Corollaire :** Convergence dominée pour les suites de
fonctions

Soient $I$ intervalle de $\mathbb{R}$, $\left( f_{n} \right)$ une suite
de fonctions de $I\mathbb{\rightarrow R}$. Soit
$f:I\mathbb{\rightarrow R}$

Si :

-   $\forall n\mathbb{\in N}$, $f_{n}$ est continue sur $I$

-   $\left( f_{n} \right)$ converge simplement vers une fonction $f$ sur
    $I$

-   $f$ est continue sur $I$

-   Il existe une fonction intégrable
    $\varphi\ :I\mathbb{\rightarrow R}$ telle que
    $\forall t \in I,\ \forall n\mathbb{\in N,}\left\vert  f_{n}(t) \right\vert  \leq \varphi(t)$

Alors $f$ est intégrable sur $I$ et
$\lim_{n \rightarrow + \infty}{\int_{I}^{}{f_{n}(t)dt}} = \int_{I}^{}{f(t)dt\ }$

**Exemple :**

$$\text{Calculer}\lim_{x \rightarrow 1}{\int_{0}^{2}{\frac{e^{- tx^{2}}}{1 + x^{2}}dt}}$$

Utilisons le théorème de convergence dominée : soit
$f\ :(t,x) \rightarrow \frac{e^{- tx^{2}}}{1 + x^{2}}$ définie sur
$\lbrack 0,2\rbrack \times \lbrack 0,1\rbrack$

Pour $x \in \lbrack 0,1\rbrack$ fixé, la fonction
$t \rightarrow \frac{e^{- tx^{2}}}{1 + x^{2}}$ est continue sur
$\lbrack 0,1\rbrack$ car l'exponentielle est continue sur $\mathbb{R}$.

Pour $t \in \lbrack 0,2\rbrack$ fixé,
$\lim_{x \rightarrow 1}{f(t,x)} = \lim_{x \rightarrow 1}\frac{e^{- tx^{2}}}{1 + x^{2}} = \frac{e^{- t}}{2} = l(t)\mathbb{\in R}$

La fonction $l\ :t \rightarrow \frac{e^{- t}}{2}$ est continue sur
$\lbrack 0,2\rbrack$

Posons $\varphi\ :t \rightarrow 1$. $\phi$ est intégrable sur
$\lbrack 0,2\rbrack$ et
$\forall t \in \lbrack 0,2\rbrack,\forall x \in \lbrack 0,1\rbrack,$

$$\left\vert  f(t,x) \right\vert  = \frac{e^{- tx}}{1 + x^{2}} \leq 1 \leq \varphi(t)$$

Conclusion : la fonction $l:t \rightarrow \frac{e^{- t}}{2}$ est
intégrable et :

$$\lim_{x \rightarrow 1}{\int_{0}^{2}{\frac{e^{- tx^{2}}}{1 + x^{2}}dt}} = \int_{0}^{2}{\frac{e^{- t}}{2}dt} = \frac{1}{2}\left\lbrack - e^{- t} \right\rbrack_{0}^{2} = \frac{1 - e^{- 2}}{2}$$

**Théorème :** Convergence dominée pour la continuité

Soient $I$ et $A$ deux intervalles de $\mathbb{R}$

$$f\mathbb{:R \times}A\mathbb{\rightarrow R}$$

Si :

-   $\forall x \in A$, la fonction $t \rightarrow f(t,x)$ est continue
    sur $\mathbb{R}$

-   $\forall t \in I$, la fonction $x \rightarrow f(t,x)$ est continue
    sur $A$

-   Il existe une fonction $\varphi\ :I\mathbb{\rightarrow R}$
    intégrable sur $I$ telle que
    $\forall x \in A,\forall t\mathbb{\in R}$,
    $\left\vert  f(t,x) \right\vert  \leq \varphi(t)$

-   Alors la fonction $x \rightarrow \int_{I}^{}{f(t,x)dt}$ est définie
    et continue sur $A$.

**Exemple :**

Soit $g:x \rightarrow \int_{0}^{+ \infty}{e^{- t}\sin(tx)}$.

Montrer que $g$ est continue sur $\mathbb{R}$.

Utilisons le théorème de convergence dominée pour la continuité des
intégrales à paramètre. On note $f(t,x) = e^{- t}\sin(tx)$

$\forall x\mathbb{\in R}$, la fonction $t \rightarrow e^{- t}\sin(tx)$
est continue sur $\mathbb{R}^{+}$ comme produit de fonctions continues
sur $\mathbb{R}^{+}$

$\forall t\mathbb{\in R,}$ la fonction $x \rightarrow e^{- t}\sin(tx)$
est continue sur $\mathbb{R}$ par continuité du sinus.

La fonction $\varphi\ :t \rightarrow e^{- t}$ est intégrable sur
$\mathbb{R}^{+}$ (intégrale généralisée de référence) et
$\forall x\mathbb{\in R,\forall}t \in \mathbb{R}_{+}$,
$\left\vert  f(t,x) \right\vert  = \left\vert  e^{- t}\sin(tx) \right\vert  \leq e^{- t}$
car $\sin(tx) \leq 1$

Donc $g$ est continue sur $\mathbb{R}$

**Théorème :** Convergence dominée pour la dérivation d'une
intégrale à paramètre

Soient $I$ et $A$ deux intervalles de $\mathbb{R}$ et
$f\ :I \times A\mathbb{\rightarrow R}$

Si :

-   $\forall t \in I$, la fonction $x \rightarrow f(t,x)$ est $C^{1}$
    sur $A$

-   $\forall x \in A$, la fonction $t \rightarrow f(t,x)$ est intégrable
    sur $I$

-   $\forall x \in A$, la fonction $\frac{\partial f}{\partial x}(t,x)$
    est continue sur $\mathbb{R}$

-   Il existe une fonction $\varphi\ :I\mathbb{\rightarrow R}$
    intégrable telle que $\forall x \in A,\forall t\mathbb{\in R}$,
    $\left\vert  \frac{\partial f}{\partial x}(t,x) \right\vert  \leq \varphi(t)$

Alors la fonction $g:x \rightarrow \int_{I}^{}{f(t,x)dt}$ est $C^{1}$
sur $A$ et
$\forall x \in A,\ g^{'}(x) = \int_{I}^{}{\frac{\partial f}{\partial x}(t,x)dt}$

**Corollaire :** extension à la classe $C^{k}$

Soient $I$ et $A$ deux intervalles de $\mathbb{R}$,
$f\ :I \times A\mathbb{\rightarrow R}$

Si :

-   $\forall t \in I$, la fonction $x \rightarrow f(t,x)$ est $C^{k}$
    sur $A$

-   $\forall j \in \left. ⟦0,\ k - 1 \right.⟧,\ \forall x \in A$, la
    fonction $t \rightarrow \frac{\partial^{j}f}{\partial x^{j}}$ est
    intégrable sur $I$

-   $\forall x \in A$, la fonction
    $t \rightarrow \frac{\partial^{k}f}{\partial x^{k}}$ est continue
    sur $I$

-   Il existe une fonction $\varphi\ :I\mathbb{\rightarrow R}$
    intégrable telle que
    $\forall x \in A,\ \forall t \in I,\ \left\vert  \frac{\partial^{k}f}{\partial x^{k}}(t,x) \right\vert  \leq \varphi(t)$

Alors la fonction $g = x \rightarrow \int_{I}^{}{f(t,x)dt}$ est $C^{k}$
sur $A$ et
$\forall x \in A,\ g^{(k)}(x) = \int_{I}^{}{\frac{\partial^{k}f}{\partial x^{k}}(t,x)dt}$

## III. Intégrales doubles

**Objectif :**

Soit $D \subset \mathbb{R}^{2}$ et $f\ :D\mathbb{\rightarrow R}$

On veut définir et calculer $\iint_{D}^{}{f(x,y)dxdy} = \iint_{D}^{}f$

### 1.  Définitions et propriétés

**Introduction :**

Soit $D = \lbrack a,b\rbrack \times \lbrack c,d\rbrack$ et $f$ une
fonction constante sur $D$.

$$\forall x,y \in D,\ f(x,y) = \lambda\mathbb{\in R}$$

Alors le volumen entre la surface (plan) de $f$ et le plan $(Oxy)$ est
le volume d'un parallélépipède rectangle : $(b - a)(d - c)\lambda$

**Définition :**

Soit $D$ une partie de $\mathbb{R}^{2}$ et $f:D\mathbb{\rightarrow R}$
continue.

On appelle intégrale double de $f$ sur $D$, et on note $\iint_{D}^{}f$
ou $\iint_{D}^{}{f(x,y)dxdy}$ le volume (algébrique) de la partie de
$\mathbb{R}^{3}$ délimitée par $D$ et la surface d'équation $z = f(x,y)$

**Proposition :**

Soit $D \in \mathbb{R}^{2},\ \iint_{D}^{}{dxdy} = Aire(D)$

**Exemple :**

Si $D = D(0,R)$ disque de centre $(0,0)$ et de rayon $R$, alors
$\iint_{D}^{}{dxdy} = \pi R^{2}$

**Proposition :**

Soient $D \subset \mathbb{R}^{2}$, $f$ et $g$ deux fonctions continues
sur $D$ et $\lambda \in \mathbb{R}$

$$\iint_{D}^{}{\lambda f + g} = \lambda\iint_{D}^{}f + \iint_{D}^{}g$$

**Proposition :**

Soient $D_{1}$ et $D_{2}$ deux ensembles de $\mathbb{R}^{2}$.

Soit $f:\mathbb{R}^{2}\mathbb{\rightarrow R}$ continue sur $D_{1}$ et
$D_{2}$

$$\iint_{D_{1} \cup D_{2}}^{}f = \iint_{D_{1}}^{}f + \iint_{D_{2}}^{}f - \iint_{D_{1} \cap D_{2}}^{}f$$

**Exemple :**

Soient $C_{1} = \lbrack - 4,2\rbrack \times \lbrack - 2,4\rbrack$,
$C_{2} = \lbrack 0,5\rbrack \times \lbrack - 3,2\rbrack$

$$\text{Calculer}\iint_{C_{1} \cup C_{2}}^{}{dxdy}$$

$$= \iint_{C_{1}}^{}{dxdy} + + \iint_{C_{2}}^{}{dxdy} - \iint_{C_{1} \cap C_{2}}^{}{dxdy}$$

Où $C_{1} \cap C_{2} = \lbrack 0,2\rbrack \times \lbrack - 2,2\rbrack$

$$= 6 \times 6 + 5 \times 5 - 2 \times 4 = 53$$

**Proposition : Positivité et croissance**

Soient $D \subset \mathbb{R}^{2}$, $D_{1} \subset \mathbb{R}^{2}$, $f$
et $g$ deux fonctions continues sur $D$.

-   Si $f \geq 0$ sur $D$ alors $\iint_{D}^{}f \geq 0$

-   Si $f \leq g$ sur $D$ alors $\iint_{D}^{}f \leq \iint_{D}^{}g$

-   $Aire(D)\inf_{D}f \leq \iint_{D}^{}f \leq Aire(D)\sup_{D}f$

-   Si $f \geq 0$ sur $D$ et $D_{1} \subset D$ alors
    $\iint_{D_{1}}^{}f \leq \iint_{D}^{}f$

-   Si $f$ est continue sur $D$ alors $\vert f\vert $ aussi et :

$$\left\vert  \iint_{D}^{}f \right\vert  \leq \iint_{D}^{}\vert f\vert $$

**Propriété :** Inégalité de Cauchy-Schwartz

Soient $D \in \mathbb{R}^{2}$, $f$ et $g$ deux fonctions continues sur
$D$.

$$\left( \iint_{D}^{}{fg} \right)^{2} \leq \left( \iint_{D}^{}f^{2} \right)\left( \iint_{D}^{}g^{2} \right)$$

### 2.  Intégration par piles et par tranches

**Théorème :** Fubini par piles

Soient $a,b \in \mathbb{R}$, $a < b$, $\left\lbrace  \begin{array}{r}
\varphi_{1}\ :\lbrack a,b\rbrack\mathbb{\rightarrow R} \\
\varphi_{2}\ :\lbrack a,b\rbrack\mathbb{\rightarrow R}
\end{array} \right. $ avec $\varphi_{1}$ et $\varphi_{2}$ continues
telle que
$\forall x \in \lbrack a,b\rbrack,\ \varphi_{1}(x) \leq \varphi_{2}(x)$

On note $D$ l'ensemble :

$$D = \left\lbrace  (x,y) \in \mathbb{R}^{2},\ a \leq x \leq b\ \text{et}\ \varphi_{1}(x) \leq y \leq \varphi_{2}(x) \right\rbrace $$

Alors, pour $f:\mathbb{R}^{2}\mathbb{\rightarrow R}$ continue sur $D$,
on a :

$$\iint_{D}^{}{f(x,y)dxdy} = \int_{a}^{b}{\left( \int_{\varphi_{1}(x)}^{\varphi_{2}(x)}{f(x,y)dy} \right)dx}$$

**Exemple :**

Soit
$D = \left\lbrace  (x,y) \in \mathbb{R}^{2},\ 0 \leq x \leq 2,\ e^{- x} \leq y \leq e^{x} \right\rbrace $

Soit $f\ :(x,y) \rightarrow xy$

On peut calculer par piles :

$$\iint_{D}^{}{f(x,y)dxdy} = \int_{0}^{2}{\left( \int_{e^{- x}}^{e^{x}}{xydy} \right)dx} = \int_{0}^{2}{x\left\lbrack \frac{1}{2}y^{2} \right\rbrack_{y = e^{- x}}^{y = e^{x}}dx} = \int_{0}^{2}{\frac{x}{2}\left( e^{2x} - e^{- 2x} \right)dx} = \left\lbrack \frac{x\left( e^{2x} + e^{- 2x} \right)}{4} \right\rbrack_{0}^{2} - \int_{0}^{2}{\frac{e^{2x} + e^{- 2x}}{4}dx} = \frac{e^{4} - e^{- 4}}{2} - \left\lbrack \frac{e^{2x} - e^{- 2x}}{8} \right\rbrack_{0}^{2} = \ldots = 3\frac{e^{4} - e^{- 4}}{4}$$

**Remarque :**

On ne peut pas intégrer par piles sur des domaines du type :

On ne peut pas intégrer une droite $\left\lbrace  x = cst \right\rbrace $ dans
$\mathbb{R}^{2}$ qui coupe $D$ en plus de deux points (mais pas une
infinité).

**Théorème :** Fubini par tranches

Soient $c,d\mathbb{\in R}$, $c < d$, $\left\lbrace  \begin{array}{r}
\psi_{1}\ :\lbrack c,d\rbrack\mathbb{\rightarrow R} \\
\psi_{2}\ :\lbrack c,d\rbrack\mathbb{\rightarrow R}
\end{array} \right. $ avec $\psi_{1}$ et $\psi_{2}$ continues telle que
$\forall y \in \lbrack c,d\rbrack,\ \psi_{1}(x) \leq \psi_{2}(x)$

On note $D$ l'ensemble :

$$D = \left\lbrace  (x,y) \in \mathbb{R}^{2},\ c \leq y \leq d\ \text{et}\ \psi_{1}(y) \leq x \leq \psi_{2}(x) \right\rbrace $$

Alors, pour $f:\mathbb{R}^{2}\mathbb{\rightarrow R}$ continue sur $D$,
on a :

$$\iint_{D}^{}{f(x,y)dxdy} = \int_{c}^{d}{\left( \int_{\psi_{1}(x)}^{\psi_{2}(x)}{f(x,y)dx} \right)dy}$$

**Corollaire :**

Si $D = \lbrack a,b\rbrack \times \lbrack c,d\rbrack$ alors on peut
intégrer par piles et par tranches, et on a :

$$\iint_{D}^{}{f(x,y)dxdy} = \int_{a}^{b}{\left( \int_{c}^{d}{f(x,y)dy} \right)dx} = \int_{c}^{d}{\left( \int_{a}^{b}{f(x,y)dx} \right)dy}$$

**Exercice :**

Calculer

$$I = \iint_{\lbrack 0,2\rbrack \times \lbrack 1,3\rbrack}^{}{\left( 2x^{2}y - 3x \right)dxdy}$$

**Par piles :**

$$I = \int_{0}^{2}{\left( \int_{1}^{3}{\left( 2x^{2}y - 3x \right)dy} \right)dx} = \int_{0}^{2}{\left\lbrack 2x^{2}\frac{y^{2}}{2} - 3xy \right\rbrack_{y = 1}^{y = 3}dx} = \int_{0}^{2}{\left( 9x^{2} - 9x \right) - \left( x^{2} - 3x \right)dx} = \int_{0}^{2}{\left( 8x^{2} - 6x \right)dx} = \left\lbrack \frac{8}{3}x^{3} - 3x^{2} \right\rbrack_{0}^{2} = \frac{64}{3} - 12 = \frac{28}{3}$$

**Par tranches :**

$$I = \int_{1}^{3}{\left( \int_{0}^{2}{\left( 2x^{2}y - 3x \right)dx} \right)dy} = \int_{1}^{3}{\left\lbrack \frac{2}{3}x^{2}y - \frac{3x^{2}}{2} \right\rbrack_{x = 0}^{x = 2}dy} = \int_{1}^{3}{\left( \frac{16}{3}y - 6 \right)dy} = \left\lbrack \frac{8}{3}y^{2} - 6y \right\rbrack_{1}^{3} = (24 - 18) - \left( \frac{8}{3} - 6 \right) = 12 - \frac{10}{3} = \frac{28}{3}$$

**Corollaire :**

Si $D = \lbrack a,b\rbrack \times \lbrack c,d\rbrack$ et $f$ est une
fonction à variables séparées, càd $f(x,y) = u(x)v(y)$, avec
$u:\lbrack a,b\rbrack\mathbb{\rightarrow R,\ }v:\lbrack c,d\rbrack\mathbb{\rightarrow R}$
continues.

Alors :

$$\iint_{D}^{}{f(x,y)dxdy} = \left( \int_{a}^{b}{u(x)dx} \right)\left( \int_{c}^{d}{v(y)dy} \right)$$

**Exercice :**

$$\int_{\lbrack - 1,1\rbrack \times \lbrack 0,3\rbrack}^{}{y^{2}e^{x}dxdy} = \left( \int_{- 1}^{1}{e^{x}dx} \right)\left( \int_{0}^{3}{y^{2}dy} \right)$$

### 3.  Changement de variables

**Théorème :**

Soient $U$ et $V$ deux ouverts de $\mathbb{R}^{2}$ et
$\varphi:U \rightarrow V$ un $C^{1} -$ difféomorphisme.

Soient $D$ une partie bornée incluse dans $U\ $: $D \subset U$ et
$f\ :\varphi(D)\mathbb{\rightarrow R}$

Alors :

$$\iint_{\varphi(D)}^{}{f(x,y)dxdy} = \iint_{D}^{}{f\left( \varphi(u,v) \right)\left\vert  J_{\varphi}(u,v) \right\vert dxdy}$$

Où
$\left\vert  J_{\varphi}(u,v) \right\vert  = \det\left( J_{\varphi}(u,v) \right)$

Où $J_{\varphi}$ est la jacobienne.

**Corollaire :** Changement de variables affines

Soit le $C^{1} -$ difféomorphisme $\varphi$ donné par :

$$\varphi:(u,v) \rightarrow \left\lbrace  \begin{array}{r}
x = au + bv \\
y = cu + dv
\end{array} \right. $$

On a :

$J_{\varphi}(u,v) = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix},\ \left\vert  J_{\varphi}(u,v) \right\vert  = ad - bc$ avec
$ad - bc \neq 0$ car $\varphi$ est un $C^{1} -$ difféomorphisme.

**Exemple :**

1\.

$$\Delta = \left\lbrace  (x,y) \in \mathbb{R}^{2},\ 0 \leq x + y \leq 4,\ \ x \leq y,\ \ xy \geq 1 \right\rbrace $$

Calculer :

$$\iint_{\Delta}^{}{\left( x^{2} - y^{2} \right)\cos(xy)dxdy}$$

Avec le changement de variables : $\left\lbrace  \begin{array}{r}
u = x + y \\
v = x - y
\end{array} \right. $

Le difféomorphisme est
$\varphi\ :(u,v) \rightarrow \left\lbrace  \begin{array}{r}
x = \frac{u + v}{2} \\
y = \frac{u - v}{2}
\end{array} \right. $

Donc
$\left\vert  J_{\varphi}(u,v) \right\vert  = \frac{1}{2} \times \left( - \frac{1}{2} \right) - \frac{1}{2} \times \frac{1}{2} = - \frac{1}{2}$

Déterminons $\varphi^{- 1}(\Delta)$

$$0 \leq x + y \leq 4 \Leftrightarrow 0 \leq u \leq 4$$

$$x \leq y \Leftrightarrow x - y \leq 0 \Leftrightarrow v \leq 0$$

$$xy \geq 1 \Leftrightarrow \left( \frac{u + v}{2} \right)\left( \frac{u - v}{2} \right) \geq 1 \Leftrightarrow u^{2} - v^{2} \geq 4$$

$$2 \leq u \leq 4$$

$$- \sqrt{u^{2} - 4} \leq v \leq 0$$

$$\Leftrightarrow \left\lbrace  \begin{array}{r}
2 \leq u \leq 4 \\
 - \sqrt{u^{2} - 4} \leq v \leq 0
\end{array} \right.  $$

Calcul de $\left\vert  J_{\varphi}(u,v) \right\vert $ avec
$\varphi(u,v) = \begin{pmatrix}
\frac{u + v}{2} \\
\frac{u - v}{2}
\end{pmatrix}$

$$J_{\varphi}(u,v) = \begin{pmatrix}
\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2}
\end{pmatrix}\ \text{donc}\ \left\vert  J_{\varphi}(u,v) \right\vert  = - \frac{1}{2}$$

Le changement de variable donne donc :

$$x^{2} - y^{2} = \left( \frac{u + v}{2} \right)^{2} - \left( \frac{u - v}{2} \right)^{2} = \frac{u^{2} + 2uv + v^{2} - u^{2} + 2uv - v^{2}}{4} = uv$$

$$\iint_{D}^{}{\left( x^{2} - y^{2} \right)\cos(xy)dxdy} = \int_{2}^{4}{\left( \int_{- \sqrt{u^{2} - 4}}^{0}{uv\cos\left( \frac{u^{2} - v^{2}}{4} \right)dv} \right)du}$$

$$= \int_{2}^{4}{u\left( \left\lbrack - 2\sin\left( \frac{u^{2} - v^{2}}{4} \right) \right\rbrack_{v = - \sqrt{u^{2} - 4}}^{0} \right)du} = \int_{2}^{4}{u\left( - 2\sin\left( \frac{u^{2}}{4} \right) + 2\sin(1) \right)du}$$

$$= \left\lbrack 4\cos\left( \frac{u^{2}}{4} \right) + 2\sin(1)\frac{u^{2}}{2} \right\rbrack_{2}^{4}$$

$$\iint_{D}^{}{\left( x^{2} - y^{2} \right)\cos(xy)dxdy} = 4\cos(4) + 16\sin(1) - 4\cos(1) - 4\sin(1)$$

**Exemple :**

$$I_{2} = \iint_{\Delta}^{}{\frac{y}{x + 1}dxdy}$$

Avec
$\Delta = \left\lbrace  (x,y) \in \mathbb{R}^{2},\ x \geq 0,\ x^{2} + y^{2} \leq 1 \right\rbrace $

On propose comme changement de variables :

$$\left\lbrace  \begin{array}{r}
u = x \\
v = - y
\end{array} \right.  $$

$\varphi(u,v) = \begin{pmatrix}
u \\
v
\end{pmatrix}$ d'où
$\left\vert  J_{\varphi}(u,v) \right\vert  = \left\vert  \left\vert  \begin{matrix}
1 & 0 \\
0 & - 1
\end{matrix} \right\vert  \right\vert  = 1$

Et :

$$\left\lbrace  \begin{array}{r}
x \geq 0 \\
x^{2} + y^{2} \leq 1
\end{array} \right.   \Leftrightarrow \left\lbrace  \begin{array}{r}
u \geq 0 \\
u^{2} + v^{2} \leq 1
\end{array} \right.  $$

$$I_{2} = \iint_{\Delta}^{}{- \frac{v}{u^{2} + 1}dudv} = - \iint_{\Delta}^{}{\frac{v}{u^{2} + 1}dudv} = - I_{2}$$

Donc $I_{2} = 0$

**Changement de variables polaires :**

$$\left\lbrace  \begin{array}{r}
x = \rho\cos(\theta) \\
y = \rho\sin(\theta)
\end{array} \right.  $$

$$\varphi:(\rho,\theta) \rightarrow \begin{pmatrix}
\rho\cos\theta \\
\rho\sin\theta
\end{pmatrix}$$

$$J_{\varphi}(\rho,\theta) = \begin{pmatrix}
\cos\theta & \rho\sin\theta \\
\sin\theta & \rho\cos\theta
\end{pmatrix}$$

$$\det\left( J_{\varphi} \right) = \rho\cos^{2}\theta + \rho\sin^{2}\theta = \rho$$

$$dxdy \rightarrow \rho d\rho d\theta$$

**Exemple :**

Calculer $I = \iint_{D}^{}{x^{2}y^{2}dxdy}$ avec
$D = \left\lbrace  (x,y) \in \mathbb{R}^{2},\ x^{2} + y^{2} \leq 1 \right\rbrace $

Changement de variables polaire :

$$x^{2} + y^{2} \leq 1 \Leftrightarrow \rho \leq 1$$

Donc le domaine d'intégration devient
$\Delta = \lbrack 0,1\rbrack \times \lbrack 0,2\pi\rbrack$

Le changement de variables donne donc :

$$I = \iint_{\Delta}^{}{\left( \rho\cos\theta \right)^{2}\left( \rho\sin\theta \right)^{2}\rho d\rho d\theta}$$

On reconnait une fonction à variables séparées :

$$I = \left( \int_{0}^{1}{\rho^{5}dt} \right)\left( \int_{0}^{2\pi}{\cos^{2}\theta\sin^{2}\theta d\theta} \right)$$

$$I = \left( \int_{0}^{1}{\rho^{5}dt} \right)\left( \int_{0}^{2\pi}{\left( \frac{\sin(2\theta)}{2} \right)^{2}d\theta} \right)$$

$$I = \left\lbrack \frac{\rho^{6}}{6} \right\rbrack_{0}^{1}\frac{1}{4}\int_{0}^{2\pi}{\frac{1 - \cos(4\theta)}{2}d\theta}$$

$$I = \frac{1}{24}\int_{0}^{2\pi}{\frac{1}{2} - \frac{1}{2}\cos(4\theta)d\theta} = \frac{1}{48}\left\lbrack \theta - \frac{\sin(4\theta)}{4} \right\rbrack_{0}^{\pi} = \frac{\pi}{24}$$

# Chapitre 2 : Probabilités

## I.  Dénombrement et Espace de probabilité

**Exemple 1 :** On lancer un dé noir et un dé blanc (à 6
faces)

Le résultat de l'expérience aléatoire est la donnée de 2 informations :
le chiffre du dé noir et le chiffre du dé blanc.

**Exemple 2 :** On tire au hasard, successivement et sans
remise, deux boules dans une urne qui contient 10 boules numérotées de 1
à 10.

Le résultat de l'expérience aléatoire est la donnée des deux numéros
tirés.

**Définition :** On appelle univers d'une expérience
aléatoire, noté $\Omega$, l'ensemble des résultats possibles d'une
expérience.

Exemple 1 : $\Omega = \left\lbrace  (1,1),(1,2),(2,1),\ldots,(6,6) \right\rbrace $

$$\Omega = \left\lbrace  (a,b)\mathbb{\in N,}\ 1 \leq a,b \leq 6 \right\rbrace $$

Exemple 2 :

$$\Omega = \left\lbrace  (n,m)\mathbb{\in N,}\ 1 \leq n,m \leq 10,\ n \neq m \right\rbrace $$

**Définition :** On appelle cardinal d'un ensemble $Ε$ le
nombre d'éléments qu'il contient. Ιl est noté $Card(E)$ ou $\vert E\vert $

**Définition :** On dit qu'un ensemble est dénombrable s'il
existe une bijection entre une partie de $\mathbb{Z}$ et lui.

### 1.  Dénombrement

**Principe du dénombrement :** Si on considère un couple
d'expériences telles que la première admet $n$ issues possibles et la
seconde en admet $m$, alors le coupe d'expérience admet $n \times m$
issues.

**Exemple 1 :**

Le couple d'expérience (lancer du dé noir (6 issues), lancer du dé blanc
(6 issues)) donne :

$$\vert \Omega\vert  = 6 \times 6 = 36$$

**Exemple 2 :**

Le couple d'expérience (tirage de la 1^ère^ boule (10 issues), tirage de
la 2^nde^ boule (9 issues)) donne :

$$\vert \Omega\vert  = 10 \times 9 = 90$$

Pour définir les notions fondamentales du dénombrement, on considère les
types de tirage suivant :

- Tirage avec remise et avec ordre

- Tirage sans remise et avec ordre

- Tirage sans remise et sans ordre

- (Tirage avec remise et sans ordre)

On tire $k$ boules dans une urne de $n$ boules numérotées de $1$ à $n$.

#### A.  Tirage avec remise et avec ordre

On tire $k$ fois une boule parmi les $n$ boules numérotées.

- 1^er^ tirage : $n$ issues possibles

- 2^e^ tirage : $n$ issues possibles (car remise)

- ...

- $k^{e}$ tirage : $n$ issues possibles

Principe du dénombrement :

$$\vert \Omega\vert  = n \times n \times \ldots \times n = n^{k}$$

#### B.  Tirage sans remise et sans ordre

On tire $k$ fois une boule dans une urne de $n$ boules sans remise.

- 1^er^ tirage : $n$ issues possibles

- 2^e^ tirage : $n - 1$ issues possibles

- ...

- $k^{e}$ tirage : $n - k + 1$ issues possibles

Principe du dénombrement :

$$\vert \Omega\vert  = n \times (n - 1) \times \ldots \times (n - k + 1) = \frac{n!}{(n - k)!}$$

**Définition :**

Soit $E$ un ensemble. On appelle $k -$ arrangement de $E$ tous les $k -$
uplets d'éléments de $E$.

Si $\vert E\vert  = n$, alors un note $A_{n}^{k}$ le nombre de $k -$ arrangements
de $E$ et on a :

$$A_{n}^{k} = \frac{n!}{(n - k)!}$$


#### C.  **Tirage sans remise et sans ordre**

On tire $k$ boules sans remise mais on ne distingue pas l'ordre.

Par exemple, tirer Bleu-Rouge-Vert est identique à tirer Rouge-Bleu-Vert.

Pour savoir combien d'issues j'ai identifiées, on se demande combien il y a de façon d'ordonner un $k -$ uplet.

**Définition :** On appelle permutations les ordonnements d'un $k -$ uplet.

Il y a $k!$ permutations d'un $k -$ uplet.

Pour le tirage sans remise et sans ordre, on a donc :

$$\vert \Omega\vert  = \frac{A_{n}^{k}}{\text{nombre de permutations de }k - \text{uplets}}$$

$$\vert \Omega\vert  = \frac{n!}{k!(n - k)!}$$

On note $\begin{pmatrix}
n \\
k
\end{pmatrix}$ et on appelle coefficient binomial ce facteur :

$$\begin{pmatrix}
n \\
k
\end{pmatrix} = \frac{n!}{k!(n - k)!}$$

**Proposition :** Rappel sur les coefficients binomiaux

-   $\begin{pmatrix}
    n + 1 \\
    k
    \end{pmatrix} = \begin{pmatrix}
    n \\
    k
    \end{pmatrix} + \begin{pmatrix}
    n \\
    k - 1
    \end{pmatrix}$

-   $\begin{pmatrix}
    n \\
    0
    \end{pmatrix} = \begin{pmatrix}
    n \\
    n
    \end{pmatrix} = 1$

-   $\begin{pmatrix}
    n \\
    1
    \end{pmatrix} = \begin{pmatrix}
    n \\
    n - 1
    \end{pmatrix} = n$

-   $\begin{pmatrix}
    n \\
    k
    \end{pmatrix} = \begin{pmatrix}
    n \\
    n - k
    \end{pmatrix}$

-   $\forall a,b\mathbb{\in R,\forall\ }n\mathbb{\in N,\ }(a + b)^{n} = \sum_{k = 0}^{n}{\begin{pmatrix}
    n \\
    k
    \end{pmatrix}a^{k}b^{n - k}}$

### 2.  Evénements

**Définition :** On appelle événement toute partie de $\Omega$.

En principe, un événement est une propriété (ou qualité) qui sera satisfaire par certaines issues de l'expérience.

On note $\mathcal{P}(\Omega)$ l'ensemble des parties de $\Omega$.

**Remarque :** On préfère dire « Soit un évènement $A \in \mathcal{P}(\Omega)$ » plutôt que « Soit un événement $A \subset \Omega$ ».

**Définition :** On définit deux opérations élémentaires sur les événements

Soient $A$ et $B$ deux évènements de $\mathcal{P}(\Omega)$

-   L'union $A \cup B\ $: « $A$ ou $B$ »

-   L'union $A \cap B\ $: « $A$ et $B$ »

**On appelle :**

-   Evènement certain : un évènement vérifié par toutes les issues : $A = \Omega$

-   Evènement impossible : un évènement vérifié par aucune issue : $A = \varnothing$

-   Evènement complémentaire de $A \in \mathcal{P}(\Omega)$, noté $\overline{A}$, l'évènement « non $A$ » : $\overline{A} = \Omega\backslash A$

-   Evènement élémentaire un élément vérifié par une seule issue : $A = \left\lbrack  \omega \right\rbrack ,\ \omega \in \Omega$

-   Deux évènements incompatibles si $A \cap B = \varnothing$

-   Un système complet d'évènements est une suite finie d'évènements $A_{1},\ldots,\ A_{p}$ incompatibles deux à deux tels que toute issue de l'expérience satisfait un (et un seul) de ces évènements

$$\Leftrightarrow \left\lbrack  \begin{array}{r}
\forall j \neq k:A_{j} \cap A_{k} = \varnothing \\
\bigcup_{i = 1}^{p}A_{i} = \Omega
\end{array} \right.  $$

**Propositions :** Lois de de Morgan

-   $\overline{A \cup B} = \overline{A} \cap \overline{B}$

-   $\overline{A \cap B} = \overline{A} \cup \overline{B}$

### 3.  Probabilités sur un univers fini

Dans cette section, $\Omega$ est un univers fini : $\vert \Omega\vert  < + \infty$

**Définition : Probabilité sur un univers fini**

Une probabilité sur l'univers fini $\Omega$ est une application $\mathbb{P:}\mathcal{P}(\Omega) \rightarrow \lbrack 0,1\rbrack$ telle que :

-   $\forall A \in \mathcal{P}(\Omega),\ 0 \leq \mathbb{P}(A) \leq 1$

-   $\mathbb{P}(\Omega) = 1$

-   $\forall A,B \in \mathcal{P}(\Omega)$, si $A \cap B = \varnothing$, alors $\mathbb{P}(A \cup B)\mathbb{= P}(A)\mathbb{+ P}(B)$

Pour tout évènement $A \in \mathcal{P}(A)\mathbb{,\ P}(A)$ est appelé probabilité de $A$.

**Exemples :**

-   On lance un dé équilibré à 6 faces. On a : $\Omega = \left. ⟦1,6 \right.⟧$

On définit une probabilité $\mathbb{P\ :}\mathcal{P}(\Omega) \rightarrow \lbrack 0,1\rbrack$ telle que $\forall\omega \in \Omega\mathbb{,P}\left( \left\lbrack  \omega \right\rbrack  \right) = \frac{1}{6}$

-   On fait un pile ou face avec une pièce déséquilibrée. On note $P$ l'issue pile et $F$ l'issue face.

On a : $\Omega = \left\lbrack  P,F \right\rbrack $ et pour une pièce déséquilibrée, on pourrait avoir $\mathbb{P}\left( \left\lbrack  P \right\rbrack  \right) = \frac{1}{4}$

On a nécessairement $\mathbb{P}\left( \left\lbrack  F \right\rbrack  \right) = 1 - \mathbb{P}\left( \left\lbrack  P \right\rbrack  \right) = \frac{3}{4}$

**Remarque :** Abus de notation

Pour les évènements élémentaires, on s'autorisé à noter $\mathbb{P}(\omega)$ à la place de $\mathbb{P}\left( \left\lbrack  \omega \right\rbrack  \right)$

**Proposition :**

Soit $A \in \mathcal{P}(\Omega)$ et $\mathbb{P}$ une probabilité sur $\Omega$

Si $A = \left\lbrack  \omega_{1},\ldots,\ \omega_{n} \right\rbrack $ alors $\mathbb{P}(A) = \sum_{k = 1}^{n}{\mathbb{P}\left( \omega_{k} \right)}$

**Elément de preuve :** Les évènements sont incompatibles deux à deux.

**Définition : Probabilité uniforme**

On dit que $\mathbb{P}$ est uniforme sur l'univers $\Omega$ si tous les évènements élémentaires ont la même probabilité.

Si $\Omega = \left\lbrack  \omega_{1},\ldots,\ \omega_{n} \right\rbrack $, alors $\forall i,j \in \left. ⟦1,n \right.⟧\mathbb{,\ P}\left( \omega_{i} \right)\mathbb{= P}\left( \omega_{j} \right)$

**Proposition :**

Soit $\mathbb{P}$ la probabilité uniforme sur $\Omega\ $:

-   $\forall\omega \in \Omega\mathbb{,\ P}(\omega) = \frac{1}{\vert \Omega\vert }$

-   $\forall A \in \mathcal{P}(\Omega)\mathbb{,\ P}(A) = \frac{\vert A\vert }{\vert \Omega\vert }$

**Proposition :**

Soit $\Omega$ un univers fini, $\mathbb{P}$ une probabilité sur $\Omega$ et $A,B \in \mathcal{P}(\Omega)$

-   $\mathbb{P}(\varnothing) = 0$

-   $\mathbb{P}\left( \overline{A} \right) = 1 - \mathbb{P}(A)$

-   $\mathbb{P}(A \cup B)\mathbb{= P}(A)\mathbb{+ P}(B)\mathbb{- P}(A \cap B)$

-   $A \subseteq B$ alors $\mathbb{P}(A)\mathbb{\leq P}(B)$

**Démonstration :**

-   $\varnothing \cup \varnothing = \varnothing$ et $\varnothing \cap \varnothing = \varnothing$, donc $\varnothing$ est incompatible avec $\varnothing$

Alors $\mathbb{P}(\varnothing \cup \varnothing)\mathbb{= P}(\varnothing)$ et $\mathbb{P}(\varnothing \cup \varnothing)\mathbb{= P}(\varnothing)\mathbb{+ P}(\varnothing)$ (d'après la propriété 3).

Donc $\mathbb{P}(\varnothing) = 0$

-   Par définition, $A \cap \overline{A} = \varnothing$ donc $A$ et $\overline{A}$ sont incompatibles et $A \cup \overline{A} = \Omega$

Donc $1 = \mathbb{P}(\Omega)\mathbb{= P}\left( A \cup \overline{A} \right)\mathbb{= P}(A)\mathbb{+ P}\left( \overline{A} \right)$, donc $P\left( \overline{A} \right) = 1 - \mathbb{P}(A)$

-   $\forall A,B \in \mathcal{P}(\Omega)$,

$$A \cup B = \left( A \cap \overline{B} \right) \cup \left( B \cap \overline{A} \right) \cup (A \cap B)$$

Ces trois évènements sont incompatibles 2 à 2 donc $\mathbb{P}(A \cup B)\mathbb{= P}(A \cap B)\mathbb{+ P}\left( B \cap \overline{A} \right)\mathbb{+ P}\left( A \cap \overline{B} \right)$

De plus, $A = (A \cap B) \cup \left( A \cap \overline{B} \right)$, ces deux évènements sont incompatibles.

$\mathbb{P}(A)\mathbb{= P}(A \cap B)\mathbb{+ P}\left( A \cap \overline{B} \right)$, $P\left( A \cap \overline{B} \right)\mathbb{= P}(A)\mathbb{- P}(A \cap B)$

Idem, $\mathbb{P}\left( B \cap \overline{A} \right)\mathbb{= P}(B)\mathbb{- P}(A \cap B)$

On en déduit que $\mathbb{P}(A \cup B)\mathbb{= P}(A)\mathbb{- P}(A \cap B)\mathbb{+ P}(B)\mathbb{- P}(A \cap B)\mathbb{+ P}(A \cap B)$

-   Si $A \subseteq B$ alors $B = A \cup \left( B \cap \overline{A} \right)$ où $A$ et $B \cap \overline{A}$ sont incompatibles, donc $\mathbb{P}(B)\mathbb{= P}(A)\mathbb{+ P}\left( B \cap \overline{A} \right)$ donc $\mathbb{P}(B)\mathbb{\geq P}(A)$

**Exemple :**

On tire une carte d'un jeu de 32 cartes, $\mathbb{P}$ est la probabilité uniforme sur $\Omega$ (8 cartes de chaque couleur, numérotées ici de 1 à 8).

On définit un évènement :

$A =$ « la carte tirée est un trèfle »

$B =$ « la carte tirée est un 2 »

**On peut calculer :**

-   $\mathbb{P}(A) = \frac{\vert A\vert }{\vert \Omega\vert } = \frac{8}{32} = \frac{1}{4}$

-   $\overline{A}\ $: « la carte tirée n'est pas un trèfle »

Donc $\mathbb{P}\left( \overline{A} \right) = \frac{\left\vert  \overline{A} \right\vert }{\vert \Omega\vert } = \frac{24}{32} = \frac{3}{4}$

Et $\mathbb{P}\left( \overline{A} \right) = 1 - \mathbb{P}(A)$

-   $A \cup B\ $: « la carte tirée est un trèfle ou un 2 »

$$\mathbb{P}(A \cup B) = \frac{\vert A \cup B\vert }{\vert \Omega\vert } = \frac{11}{32}$$

$$\mathbb{P}(A \cup B)\mathbb{= P}(A)\mathbb{+ P}(B)\mathbb{- P}(A \cap B) = \frac{8}{32} + \frac{4}{32} - \frac{1}{32} = \frac{11}{32}$$

**Définition :**

Soit $\mathbb{P}$ une probabilité sur $\Omega$.

Un évènement $A$ est dit :

-   Négligeable si $\mathbb{P}(A) = 0$

-   $\mathbb{P}$-presque sûr si $\mathbb{P}(A) = 1$

10. Probabilités sur un univers infini (dénombrable)

Soit $\Omega$ un univers infini dénombrable.

**Définition : Probabilité sur un univers infini dénombrable**

Une probabilité $\mathbb{P}$ sur $\Omega$ est une fonction $\mathbb{P:}\mathcal{P}(\Omega)\mathbb{\rightarrow R}$ telle que :

-   $\forall A \in \mathcal{P}(\Omega),\ 0 \leq \mathbb{P}(A) \leq 1$

-   $\mathbb{P}(\Omega) = 1$

-   Pour toute suite d'évènements $\left( A_{n} \right)$ ($\forall n\mathbb{\in N,\ }A_{n}\mathcal{\in P}(\Omega)$) disjoints deux à deux : $\forall i,j\mathbb{\in N,\ }i \neq j,\ A_{i} \cap A_{j} = \varnothing$, on a

$$\mathbb{P}\left( \bigcup_{n\mathbb{\in N}}^{}A_{n} \right) = \sum_{n = 0}^{+ \infty}{\mathbb{P}\left( A_{n} \right)}\ \text{(}\text{σ}\text{-additivité)}$$

### 4. Probabilités conditionnelles et indépendance

Dans cette section, on considère un espace de probabilité $\left( \Omega\mathbb{,P} \right)$

**Exemple :**

On considère un jeu de 52 cartes sans les têtes (jeu de 40 cartes). On tire une carte au hasard dans ce jeu.

On s'intéresse aux évènements :

-   $A =$ « La carte tirée est rouge »

-   $B =$ « La carte tirée est paire »

-   $C =$ « La carte tirée est $\geq 8$ »

Univers $\Omega = \left\lbrack  \text{40 cartes} \right\rbrack $

$\mathbb{P}$ est la probabilité uniforme sur $\Omega$

Probabilités des trois évènements :

-   $\mathbb{P}(A) = \frac{20}{40} = \frac{1}{2}$

-   $\mathbb{P}(B) = \frac{20}{40} = \frac{1}{2}$

-   $\mathbb{P}(C) = \frac{12}{40} = \frac{3}{10}$

**Question 1 :** $Tapez\ une\ équation\ ici.$

Si on sait que $A$ est réalisé, quelle est la probabilité que $B$ se réalise aussi ?

-   Si $A$ est réalisée, cela signifie qu'on a tiré l'une des 20 cartes rouges du jeu.

-   La probabilité que $B$ se réalise aussi est la probabilité que la carte rouge est aussi paire

-   $\frac{10}{20} = \frac{1}{2}$

On retrouve $\frac{1}{2}\mathbb{= P}(B)$ donc le fait que $A$ ait été réalisé n'a pas impacté la probabilité que $B$ se réalise.

**Question 2 :**

Si $B$ est réalisé, quelle est la probabilité que $C$ se réalise ?

$$\frac{8}{20} = \frac{2}{5} \neq \frac{3}{10}\mathbb{= P}(C)$$

**Probabilités conditionnelles**

**Définition : Probabilité conditionnelle**

Soient $A$ et $B$ deux évènements tels que $\mathbb{P}(B) \neq 0$.

On appelle probabilité conditionnelle de $A$ sachant $B$, notée $\mathbb{P}\left( A \middle\vert  B \right)$ ou $\mathbb{P}_{B}(A)$ la probabilité :

$$\mathbb{P}\left( A \middle\vert  B \right) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

**Exemple :**

$$\mathbb{P}\left( B \middle\vert  A \right) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)} = \frac{10/40}{1/2} = \frac{1}{2}$$

$$\mathbb{P}\left( C \middle\vert  B \right) = \frac{\mathbb{P}(B \cap C)}{\mathbb{P}(B)} = \frac{8/40}{1/2} = \frac{2}{5}$$

**Théorème : Formule des probabilités totales**

**Cas particulier :** Soient $A,B \in \mathcal{P}(\Omega)$

$$\mathbb{P}(A)\mathbb{= P}\left( A \middle\vert  B \right)\mathbb{+ P}\left( A \middle\vert  \overline{B} \right)$$

**Cas général :** Soient $$A \in \mathcal{P}(\Omega)$ et $\left( C_{i} \right)_{i \in I}$$ un système complet d'évènements ($$\forall i \neq j \in I,\ C_{i} \cap C_{j} = \varnothing,\ \bigcup_{i \in I}^{}C_{i} = \Omega$$)

$$\mathbb{P}(A) = \sum_{i \in I}^{}{\mathbb{P}\left( A \middle\vert  C_{i} \right)\mathbb{P}\left( C_{i} \right)}$$

**Théorème : Formule de Bayes**

**Cas particulier :** Soient $A,B \in \mathcal{P}(\Omega)$

$$\mathbb{P}\left( A \middle\vert  B \right)\mathbb{P}(B)\mathbb{= P}\left( B \middle\vert  A \right)\mathbb{P}(A)$$

**Cas général :** Soient $A \in \mathcal{P}(\Omega)$ et $\left( C_{i} \right)_{i \in I}$ un système complet d'évènements

$$\forall i \in I\mathbb{,\ P}\left( C_{i} \middle\vert  A \right) = \frac{\mathbb{P}\left( A \middle\vert  C_{i} \right)\mathbb{P}\left( C_{i} \right)}{\sum_{j \in I}^{}{\mathbb{P}\left( A \middle\vert  C_{j} \right)\mathbb{P}\left( C_{j} \right)}}$$

**Indépendance**

**Définition : Evènements indépendants**

On dit que deux évènements $A$ et $B$ sont indépendants si $\mathbb{P}\left( A \middle\vert  B \right)\mathbb{= P}(A)$, ou, de façon équivalente, $\mathbb{P}\left( B \middle\vert  A \right)\mathbb{= P}(B)$

**Proposition :** Deux évènements $A,B \in \mathcal{P}(\Omega)$ sont indépendants si et seulement si $\mathbb{P}(A \cap B)\mathbb{= P}(A)\mathbb{P}(B)$

**Attention :** L'indépendance n'est pas une notion ensembliste. La notion d'incompatibilité n'a rien à voir avec la notion d'indépendance.

**Remarque :** Si $A \cap B = \varnothing$, alors ils sont indépendants si et seulement si $\mathbb{P}(A) = 0$ ou $\mathbb{P}(B) = 0$

**Exemple :** Voir exemple en début de section

-   $\mathbb{P}(A \cap B) = \frac{1}{4}\mathbb{= P}(A)\mathbb{P}(B)$

Donc $A$ et $B$ sont indépendants.

-   $\mathbb{P}\left( C \middle\vert  B \right) = \frac{2}{5} \neq \frac{3}{10}\mathbb{= P}(C)$

Donc $B$ et $C$ ne sont pas indépendants.

-   $\mathbb{P}(A \cap C) = \frac{6}{40} = \frac{3}{20}\mathbb{= P}(A)\mathbb{\times P}(C)$

Donc $A$ et $C$ sont indépendants.

**Proposition :**

Si $A$ et $B$ sont indépendants, alors :

-   $A$ et $\overline{B}$ sont indépendants

-   $\overline{A}$ et $B$ sont indépendants

-   $\overline{A}$ et $\overline{B}$ sont indépendants

**Définition :**

Une suite d'évènements $$\left( A_{i} \right)_{i \in I}$$ est dite indépendante si $$\mathbb{P}\left( A_{i_{1}} \cap \ldots \cap A_{i_{k}} \right)\mathbb{= P}\left( A_{i_{1}} \right)\mathbb{\times \ldots \times P}\left( A_{i_{k}} \right)$$

Pour tout sous-ensemble d'indice $\left( i_{1},\ldots,i_{k} \right) \in I$

**Cas particulier pour un triplet** $(A,B,C)\ $**:**

$$\left\lbrack  \begin{array}{r}
\mathbb{P}(A \cap B \cap C)\mathbb{= P}(A)\mathbb{P}(B)\mathbb{P}(C) \\
\mathbb{P}(A \cap B)\mathbb{= P}(A)\mathbb{P}(B) \\
\mathbb{P}(B \cap C)\mathbb{= P}(B)\mathbb{P}(C) \\
\mathbb{P}(C \cap A)\mathbb{= P}(C)\mathbb{P}(A)
\end{array} \right.  $$

**Exemple :**

On considère un lancer de deux dés.

On s'intéresse uniquement à la somme de deux dés.

$$X:\Omega \rightarrow \left. ⟦2,12 \right.⟧$$

On s'intéresse à la probabilité des événements « $X = k$ », $k \in ⟦2,12⟧$.

| $X$               | 2                | 3                | 4                | 5                | 6                | 7                | 8                | 9                | 10               | 11               | 12               |
|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|
| Probabilité       | $\frac{1}{36}$     | $\frac{2}{36}$     | $\frac{3}{36}$     | $\frac{4}{36}$     | $\frac{5}{36}$     | $\frac{6}{36}$     | $\frac{5}{36}$     | $\frac{4}{36}$     | $\frac{3}{36}$     | $\frac{2}{36}$     | $\frac{1}{36}$     |

**Exemple :**

On considère une urne avec 3 boules bleues, 5 boules vertes et 4 boules rouges.

On joue au jeu suivant : on tire 3 boules sans remise :

-   Pour chaque boule bleue : on gagne 1€

-   Pour chaque boule verte : pas d'effet

-   Pour chaque boule rouge : on perd 1€

On pose :

$X:\Omega \rightarrow X(\Omega)$ le gain final.
Gain final : $X : \Omega \rightarrow X(\Omega)$

|     $X$     |      $-3$       |       $-2$       |       $-1$       |   $0$    |   $1$    |   $2$    |       $3$       |
| :---------: | :-------------: | :--------------: | :--------------: | :------: | :------: | :------: | :-------------: |
| Probabilité | $\frac{4}{220}$ | $\frac{30}{220}$ | $\frac{58}{220}$ | $\ldots$ | $\ldots$ | $\ldots$ | $\frac{1}{220}$ |


**Exemple :**

On considère une urne avec 7 boules vertes et 3 boules rouges.

On joue au jeu suivant : on fait des tirages successifs sans remise :

-   Si on tire une boule verte, on gagne un point

-   Si on tire une boule rouge, le jeu est fini

On pose $X:\Omega \rightarrow X(\Omega)$ le nombre de points obtenus.

| $X$               | $0$              | $1$              | $2$              | $3$             | $4$              | $5$              | $6$              | $7$               |
|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:---------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|
| Probabilité       | $\frac{3}{10}$     | $\frac{7}{30}$     | $\frac{7}{40}$     | $\frac{1}{8}$    | $\frac{1}{12}$     | $\frac{1}{20}$     | $\frac{1}{40}$     | $\frac{1}{120}$     |

## IV. Variables aléatoires réelles discrètes

Dans toute cette section, $\left( \Omega\mathbb{,P} \right)$ est un espace de probabilité dénombrable.

### 1.  Variable aléatoire

Voir exemples introductifs.

**Définition :**

On appelle variable aléatoire réelle (v.a.r.) toute application $X:\Omega\mathbb{\rightarrow R}$.

On dit qu'une variable $X$ est discrète si l'ensemble des valeurs possible de $X\ $: $X(\Omega)$ est dénombrable.

**Remarque :**

Si $\Omega$ est dénombrable, alors toute v.a.r. sur $\Omega$ est discrète.

**Définition :**

Soit $X$ une variable aléatoire sur $\left( \Omega\mathbb{,P} \right)$.

Pour tout $k \in X(\Omega)$, on note « $X = k$ » l'évènement $X^{- 1}(k)\mathcal{\in P}(\Omega)$

Où $X^{- 1}(k) = \left\lbrack  \omega \in \Omega,\ X(\omega) = k \right\rbrack $

On définit de façon analogue les évènements « $X \leq k$ », « $X < k$ », « $X \geq k$ », « $X > k$ ».

**Exemple :**

Pour l'exemple où on regarde la somme de deux dés :

$$X^{- 1}(6) = \left\lbrack  (1,5),(2,4),(3,3),(4,2),(5,1) \right\rbrack $$

**Définition :**

Soit $X$ une v.a.r. sur $$\left( \Omega\mathbb{,P} \right)$$. On note $$\mathbb{P}_{X}\mathcal{:P}\left( X(\Omega) \right)\mathbb{\rightarrow R}$$ définie par $$\forall B \in \mathcal{P}(\Omega),\ \mathbb{P}_{X}(B)\mathbb{= P}\left( X^{- 1}(B) \right)\mathbb{= P}\left( \left\lbrack  \omega \in \Omega,\ X(\omega) \in B\  \right\rbrack  \right)$$

On l'appelle loi de la variable aléatoire $X$. $\mathbb{P}_{x}$ est une probabilité sur $X(\Omega)$

Donner la loi d'une variable $X$, c'est donner 2 informations :

-   Toutes les valeurs possibles de $X(\Omega)$

-   La probabilité de chaque évènement « $X = k$ », $k \in X(\Omega)$

Voir tableaux donnés en exemples

**Proposition :**

Soit $X$ une v.a.r. sur $\Omega$ avec $X(\Omega) = \left\lbrack  a_{i} \right\rbrack _{i \in I}$

Comme $$\mathbb{P}_{x}$$ est une probabilité sur $X(\Omega)$ et l'ensemble des évènements « $$X = a_{i}$$ » ($i \in I$) est un système complet d'évènements, on a :

$$\sum_{i \in I}^{}{\mathbb{P}\left( X = a_{i} \right)} = 1$$

### 2. Espérance

On appelle espérance d'une v.a.r. sa valeur moyenne sur un grand nombre d'itérations de l'expérience.

**Définition :**

Si $\Omega$ est fini et $X$ est une v.a.r. sur $\Omega$, on définit l'espérance de $X$ notée $\mathbb{E}(X)$ par :

$$\mathbb{E}(X) = \sum_{a \in X(\Omega)}^{}{a\mathbb{P}(X = a)}$$

En d'autres termes, si $\Omega = \left\lbrack  a_{1},\ldots,a_{n} \right\rbrack $, alors :

$$\mathbb{E}(X) = \sum_{i = 1}^{n}{a_{i}\mathbb{P}\left( X = a_{i} \right)}$$

**Exemple :**

1.  Somme de deux dés :

$$\mathbb{E}(X) = 2 \times \frac{1}{36} + 3 \times \frac{2}{36} + 4 \times \frac{3}{36} + 5 \times \frac{4}{36} + \ldots$$

$$\mathbb{E}(X) = 7$$

2.  Tirage de trois boules

$$\mathbb{E}(X) = - \frac{1}{4}$$

3.  Tirages de boules vertes et rouges

$$\mathbb{E}(X) = 1.75$$

**Définition :**

Si $\Omega$ est infini dénombrable, et $X$ une v.a.r sur $\Omega$.

Si la série numérique $\sum_{\omega \in \Omega}^{}{\mathbb{P}\left( \left\lbrack  \omega \right\rbrack  \right)\left\vert  X(\omega) \right\vert }$ converge, alors on dit que $X$ admet une espérance, ou encore que $X$ est intégrable.

On note $L^{1}\left( \Omega\mathbb{,P} \right)$ l'ensemble des v.a.r. intégrables sur $\Omega$ pour la probabilité $\mathbb{P}$.

Si $X \in L^{1}\left( \Omega\mathbb{,P} \right)$ alors

$$\mathbb{E}(X) = \sum_{a \in X(\Omega)}^{}{a\mathbb{P}(X = a)}$$

**Proposition :**

Soient $X$ et $Y$ deux v.a.r. sur $\Omega$ et $\lambda,\nu$ deux réels.

-   Linéarité

Si $X$ et $Y$ sont intégrables, alors $\mathbb{E}(\lambda X + \mu y) = \lambda\mathbb{E}(X) + \mu\mathbb{E}(y)$

-   $X \in L^{1} \Leftrightarrow \vert X\vert  \in L^{1}$ et $\left\vert  \mathbb{E}(X) \right\vert \mathbb{\leq E}\left( \vert X\vert  \right)$

-   Si $\forall\omega \in \Omega,\ X(\omega) \geq 0$, alors $\mathbb{E}(X) \geq 0$

-   Si $\forall\omega \in \Omega,\ X(\omega) \leq Y(\omega)$ alors $\mathbb{E}(X)\mathbb{\leq E}(y)$

-   Si $X$ est bornée, càd $\exists M \in \mathbb{R}_{+},\ \forall\omega \in \Omega,\ \left\vert  X(\omega) \right\vert  \leq M$, alors $X$ est intégrable

-   Si $X$ est constante, càd $\exists k\mathbb{\in R}$, $\forall\omega \in \Omega,\ X(\omega) = k$, alors $\mathbb{E}(X) = k$

**Remarque :** En général, $\mathbb{E}(XY)\mathbb{\neq E}(X)\mathbb{E}(Y)$

**Théorème :** Théorème du transfert

Soient $(\Omega\mathbb{,P)}$ un espace de probabilité dénombrable, $X$ une variable aléatoire sur $\Omega$ et $f\mathbb{:R \rightarrow R}$.

Si $X$ est intégrable et si la variable $Y = f(X)$ est aussi intégrable ($f \in L^{1}\left( X(\Omega),\mathbb{P}_{X} \right)$) ; alors :

$$\mathbb{E}\left( f(x) \right) = \sum_{a \in X(\Omega)}^{}{f(a)\mathbb{P}(X = a)}$$

### 4. Variance et écart-type

L'écart-type est une propriété qui « synthétise » le caractère dispersé/condensé des valeurs prises par $X$.

**Définition :**

On note $L^{2}\left( \Omega\mathbb{,P} \right)$ l'ensemble des v.a.r. de carré intégrable, càd telle que $X^{2} \in L^{1}\left( \Omega\mathbb{,R} \right)$

**Propriété :**

$L^{2}\left( \Omega\mathbb{,P} \right)$ est un s.e.v. de $L^{1}\left( \Omega\mathbb{,P} \right)$

**Définition :**

Soit $X \in L^{2}\left( \Omega\mathbb{,P} \right)$.

On appelle variance de $X$, notées $\mathbb{V}(X)$, la quantité :

$$\mathbb{V}(X)\mathbb{= E}\left( \left( X - \mathbb{E}(X) \right)^{2} \right)$$

Par le théorème du transfert, une définition équivalente est :

$$\mathbb{V}(X) = \sum_{a \in X(\Omega)}^{}{\left( a - \mathbb{E}(X) \right)^{2}\mathbb{P}(X = a)}$$

On appelle écart-type et on note $\sigma(X) = \sqrt{\mathbb{V}(X)}$

**Théorème :** Théorème de Koenig-Huygens

Soit $\left( \Omega\mathbb{,P} \right)$ un espace de probabilité dénombrable et $X$ une variable aléatoire $X \in L^{2}\left( \Omega\mathbb{,P} \right)$. On a :

$$\mathbb{V}(X)\mathbb{= E}\left( X^{2} \right) - \left( \mathbb{E}(X) \right)^{2}$$

Par le théorème du transfert :

$$\mathbb{E}\left( X^{2} \right) = \sum_{a \in X(\Omega)}^{}{a^{2}\mathbb{P}(x = a)}$$

**Proposition :**

Soit $X \in L^{2}\left( \Omega\mathbb{,P} \right)$

-   $\mathbb{V}(X) \geq 0$

-   $\mathbb{V}(X) = 0 \Leftrightarrow \mathbb{P}\left( X = \mathbb{E}(X) \right) = 1$

La variance est nulle si et seulement si $X$ ne prend qu'une seule valeur (qui est donc son espérance)

**Proposition :**

Soient $X \in L^{2}\left( \Omega\mathbb{,P} \right)$, $\lambda,\mu\mathbb{\in R}$

-   $\mathbb{V}(\lambda X) = \lambda^{2}\mathbb{V}(X)$ (homogénéité de degré 2)

-   $\mathbb{V}(X + \mu)\mathbb{= V}(X)$ (invariance par translation)

La variance n'est pas linéaire. En général, $\mathbb{V}(X + Y)\mathbb{\neq V}(X)\mathbb{+ V}(Y)$

**Corollaire :**

Soient $X \in L^{2}\left( \Omega\mathbb{,P} \right)$, $\lambda,\mu\mathbb{\in R}$

$$\sigma(\lambda Χ + \mu) = \vert \lambda\vert \sigma(X)$$

**Exemple :**

1.  Somme de deux dés

$$\sigma(X) \approx 2.4$$

2.  Tirage de 3 boules

$$\sigma(X) \approx 1.19$$

3.  Tirage de boules vertes et rouges

$$\sigma(X) \approx 1.67$$


$$\sigma(X) \approx 1.67$$

## V.  Couple de variables aléatoires

On peut être amené à considérer deux variables aléatoires réelles pour une même expérience aléatoire

**Exemple :**

On considère un lancer de deux dés à 6 faces.

Soit $X$ la variable qui rend la somme des deux dés, $Y$ la variable qui rend le plus grand des deux dés.

$$X(\Omega) = \left. ⟦2,12 \right.⟧,\ Y(\Omega) = \left. ⟦1,6 \right.⟧$$

$$(X,Y):\Omega \rightarrow \left. ⟦2,12 \right.⟧ \times \left. ⟦1,6 \right.⟧$$

$$\omega \rightarrow \left( X(\omega),Y(\omega) \right)$$

**Définition :**

Soit $\left( \Omega\mathbb{,P} \right)$ un espace de probabilité, $X$ et $Y$ deux v.a.r. sur $\left( \Omega\mathbb{,P} \right)$.

On appelle couple de v.a.r., et on note $(X,Y)$ la v.a.r. sur $\Omega$ donnée par

$$(X,Y):\Omega \rightarrow X(\Omega) \times Y(\Omega)$$

$$\omega \rightarrow \left( X(\omega),Y(\omega) \right)$$

-   Donner la loi de $Z = (X,Y)$, c'est donner $X(\Omega) \times Y(\Omega)$, soit toutes les valeurs que peut prendre $Z$, et

$\forall k \in X(\Omega),\forall j \in Y(\Omega)$, donner $\mathbb{P}\left( Z = (k,j) \right)$ soit $\mathbb{P}\left( X = k\ \text{et}\ Y = j \right)$


| $$Y \backslash X$$ | 2             | 3             | 4             | 5             | 6             | 7             | 8             | 9             | 10            | 11            | 12            |
|--------------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
| 1                  | $$\frac{1}{36}$$ | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             |
| 2                  | 0             | $$\frac{1}{18}$$ | $$\frac{1}{36}$$ | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             |
| 3                  | 0             | 0             | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{36}$$ | 0             | 0             | 0             | 0             | 0             | 0             |
| 4                  | 0             | 0             | 0             | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{36}$$ | 0             | 0             | 0             | 0             |
| 5                  | 0             | 0             | 0             | 0             | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{36}$$ | 0             | 0             |
| 6                  | 0             | 0             | 0             | 0             | 0             | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{18}$$ | $$\frac{1}{36}$$ |


$$k\left( \begin{array}{r}
n \\
k
\end{array} \right) = \frac{kn!}{k!(n - k)!} = \frac{n}{k} \times k \times \frac{(n - 1)!}{(k - 1)!(n - k)!} = n\left( \begin{array}{r}
n - 1 \\
k - 1
\end{array} \right)$$

**Définition :**

Soit $\left( \Omega\mathbb{,P} \right)$ un espace de probabilité et $(X,Y)$ un couple de variable distinctes sur $\Omega$.

On appelle lois marginales du couple $(X,Y)$ les lois de $X$ et $Y$.

$$\forall x \in X(\Omega)\mathbb{,\ P}(X = x) = \sum_{y \in Y(\Omega)}^{}{\mathbb{P}\left( (X,Y) = (x,y) \right)}$$

$$\forall y \in Y(\Omega)\mathbb{,P}(Y = y) = \sum_{x \in X(\Omega)}^{}{\mathbb{P}\left( (X,Y) = (x,y) \right)}$$

**Remarques :**

-   La définition d'une loi marginale repose sur le fait que $\left\lbrack  \text{"}Y = y\text{"},\ y \in Y(\Omega) \right\rbrack $ forme un système complet d'évènements.

-   Connaitre la loi du couple $(X,Y)$ suffit pour connaitre les lois de $X$ et de $Y$ mais l'inverse est faux.

**Définition :**

Soient $X$ et $Y$ deux variables distinctes sur $\Omega$ avec $\left( \Omega\mathbb{,P} \right)$ un espace de probabilité.

On dit que les variables $X$ et $Y$ sont indépendantes si :

$\forall x \in X(\Omega)$ et $\forall y \in Y(\Omega)$, $\mathbb{P}\left( (X,Y) = (x,y) \right)\mathbb{= P}(X = x)\mathbb{\times P}(Y = y)$

**Proposition :**

Soient $X$ et $Y$ deux variables indépendantes, alors :

-   $\mathbb{E}(XY)\mathbb{= E}(X)\mathbb{\times E}(Y)$

-   $\mathbb{V}(X + Y)\mathbb{= V}(X)\mathbb{+ V}(Y)$

**Preuve :**

$$\mathbb{E}(XY) = \sum_{x \in X(\Omega),y \in Y(\Omega)}^{}{xy\mathbb{P}\left( X = x\ \text{et}\ Y = y \right)}$$

$$\mathbb{E}(XY) = \sum_{x \in X(\Omega),y \in Y(\Omega)}^{}{xy\mathbb{P}(X = x)\mathbb{P}(Y = y)}$$

$$\mathbb{E}(XY) = \left( \sum_{x \in X(\Omega)}^{}{x\mathbb{P}(X = x)} \right)\left( \sum_{y \in Y(\Omega)}^{}{y\mathbb{P}(Y = y)} \right)$$

$$\mathbb{E}(XY)\mathbb{= E}(X)\mathbb{E}(Y)$$

Pour déterminer $\mathbb{V}(X + Y)$, calculons d'abord $\mathbb{E}\left( (X + Y)^{2} \right)$

$$\mathbb{E}\left( (X + Y)^{2} \right)\mathbb{= E}\left( X^{2} + 2XY + Y^{2} \right)$$

$$\mathbb{E}\left( (X + Y)^{2} \right)\mathbb{= E}\left( X^{2} \right) + 2\mathbb{E}(XY)\mathbb{+ E}\left( Y^{2} \right)$$

$$\mathbb{E(}(X + Y)^{2}\mathbb{)) = E(}X²) + 2\mathbb{E(}X)\mathbb{E(}Y) + \mathbb{E(}Y²)$$

On en déduit que :

$$\mathbb{V}(X + Y)\mathbb{= E}\left( (X + Y)^{2} \right)\mathbb{- E}(X + Y)^{2}$$

$$\mathbb{V}(X + Y)\mathbb{= E}\left( X^{2} \right) + 2\mathbb{E}(X)\mathbb{E}(Y)\mathbb{+ E}\left( Y^{2} \right) - \left( \mathbb{E}(X)^{2} + 2\mathbb{E}(X)\mathbb{E}(Y)\mathbb{+ E}(Y)^{2} \right)$$

$$\mathbb{V}(X + Y)\mathbb{= E}\left( X^{2} \right)\mathbb{- E}(X)^{2}\mathbb{+ E}\left( Y^{2} \right)\mathbb{- E}(Y)^{2}$$

$$\mathbb{V}(X + Y)\mathbb{= V}(X)\mathbb{+ V}(Y)$$

**Remarque :**

La réciproque est fausse.

**Définition :**

Soient $X$ et $Y$ deux variables distinctes sur $\Omega$.

La covariance de $X$ et $Y$, notée $Cov(X,Y)$, est :

$$Cov(X,Y)\mathbb{= E}\left( \left( X - \mathbb{E}(X) \right)\left( Y - \mathbb{E}(Y) \right) \right)$$

**Propositions :**

Soient $X$ et $Y$ deux variables distinctes sur $\Omega$.

-   $Cov(X,Y)\mathbb{= E}(XY)\mathbb{- E}(X)\mathbb{E}(Y)$

-   $Cov(X,X)\mathbb{= V}(X)$

-   $\mathbb{V}(X + Y)\mathbb{= V}(X) + 2Cov(X,Y)\mathbb{+ V}(Y)$

-   Si $X$ et $Y$ sont indépendantes alors $Cov(X,Y) = 0$

**Remarque :**

-   Comme Koenig -- Huygens pour la variance, la formule $Cov(X,Y)\mathbb{= E}(XY)\mathbb{- E}(X)\mathbb{E}(Y)$ est plus pratique pour les calculs.

-   La réciproque de la quatrième proposition est fausse, on peut avoir $Cov(X,Y) = 0$ mais $X$ et $Y$ non indépendantes

**Preuve :**

-   $$Cov(X,Y)\mathbb{= E}\left( \left( X - \mathbb{E}(X) \right)\left( Y - \mathbb{E}(Y) \right) \right)\mathbb{= E}\left( XY - \mathbb{E}(X)Y - \mathbb{E}(Y)X + \mathbb{E}(X)\mathbb{E}(Y) \right)\mathbb{= E}(XY)\mathbb{- E}(X)\mathbb{E}(Y)\mathbb{- E}(Y)\mathbb{E}(X)\mathbb{+ E}(X)\mathbb{E}(Y)\mathbb{= E}(XY)\mathbb{- E}(X)\mathbb{E}(Y)$$

-   Corollaire de la première proposition

-   $$\mathbb{V}(X + Y)\mathbb{= E}\left( (X + Y)^{2} \right)\mathbb{- E}(X + Y)^{2}\mathbb{= E}\left( X^{2} \right) + 2\mathbb{E}(XY)\mathbb{+ E}\left( Y^{2} \right)\mathbb{- E}(X)^{2} - 2\mathbb{E}(X)\mathbb{E}(Y)\mathbb{- E}(Y)^{2}\mathbb{= V}(X) + 2Cov(X,Y)\mathbb{+ V}(Y)$$

-   Corollaire de la proposition précédente

## VI. Probabilités continues

<!-- -->

### 1.  Généralités

On appelle variable aléatoire continue une variable aléatoire qui prend un nombre indénombrable de valeurs, en particulier des variables telles que $X(\Omega) = I$ intervalle de $\mathbb{R}$ ou $X(\Omega) = \lbrack a,b\rbrack\mathbb{\subset R}$.

**Définition :**

On dit qu'une variable aléatoire réelle est continue si elle peut prendre toutes les valeurs d'un intervalle (borné ou non) de $\mathbb{R}$.

Pour définir la loi d'une v.a.r. continue, on introduit d'abord la notion de densité.

**Définition :**

Soit $f:\mathbb{R \rightarrow R}$, on dit que $f$ est une densité si elle vérifie :

-   $\forall x \in \mathbb{R,\ }f(x) \geq 0$

-   $f$ est intégrable sur $\mathbb{R}$

-   $\int_{\mathbb{R}}^{}{f(t)dt} = 1$

**Définition :**

On dit que $X$ est une variable aléatoire continue de densité $f$ si $\forall a,b \in \mathbb{R,\ }a \leq b,\ $

$$\mathbb{P}(a \leq X \leq b) = \int_{a}^{b}{f(t)dt}$$

**Cas particuliers :**

$$\mathbb{P}(X \geq a) = \int_{a}^{+ \infty}{f(t)dt}$$

$$\mathbb{P}(X \leq b) = \int_{- \infty}^{b}{f(t)dt}$$

**Définition :**

Soit $X$ une v.a.r. continue de densité $f$.

On appelle fonction de répartition de $X$ la fonction $F$ donnée par

$$\forall x \in \mathbb{R,\ }F(x) = P(X \leq x) = \int_{- \infty}^{x}{f(t)dt}$$

**Proposition :**

Soit $X$ une variable aléatoire réelle de densité $f$ et de fonction de répartition $F$

-   $F$ est continue et dérivable, avec $F^{'} = f$

-   $$\forall x\mathbb{\in R,\ }F(x) \geq 0\ \text{et}\         \left\lbrack  \begin{array}{r} \lim_{x \rightarrow - \infty}{F(x)} = 0 \\ \lim_{x \rightarrow + \infty}{F(x)} = 1 \end{array} \right. $$

-   $F$ est croissante sur $\mathbb{R}$

-   $\forall a,b\mathbb{\in R,\ P}(a \leq X \leq b) = F(b) - F(a)$

**Preuve :**

-   Corollaire de la définition de $F$

-   Corollaire de la définition de $F$

-   Déduit de la positivité de $f$

-   Théorème fondamental de l'analyse

**Définition :**

Soit $X$ une v.a.r. continue.

-   L'espérance de $X$, si elle existe, est donnée par :

$$\mathbb{E}(X) = \int_{\mathbb{R}}^{}{tf(t)dt}$$

-   La variance de $X$, si elle existe, est donnée par :

$$\mathbb{V}(X) = \int_{\mathbb{R}}^{}{t^{2}f(t)dt} - \left( \int_{\mathbb{R}}^{}{tf(t)dt} \right)^{2}$$

Et on écart-type est $\sigma(X) = \sqrt{\mathbb{V}(X)}$

### 2. Variables aléatoires continues usuelles

#### A.  Loi uniforme

**Définition :**

On dit qu'une v.a.r $X$ suit une loi uniforme sur un intervalle $\lbrack a,b\rbrack$, noté $X \hookrightarrow \mathcal{U}_{\lbrack a,b\rbrack}$, si la densité $f$ de $X$ est :

$$f:t \rightarrow \left\lbrack  \begin{array}{r}
\frac{1}{b - a}\ \text{si}\ t \in \lbrack a,b\rbrack \\
0\ \text{sinon}
\end{array} \right. $$

**Proposition :**

Soit $X \hookrightarrow \mathcal{U}_{\lbrack a,b\rbrack},\ a < b\mathbb{\in R}$

-   $\forall c,d\mathbb{\in R,\ }a \leq c < d \leq b$,

$$\mathbb{P}(c \leq X \leq d) = \int_{c}^{d}{f(t)dt} = \int_{c}^{d}{\frac{1}{b - a}dt} = \frac{d - c}{b - a}$$

-   $X$ admet une espérance et

$$\mathbb{E}(X) = \frac{a + b}{2}$$

-   $X$ admet une variance et

$$\mathbb{V}(X) = \frac{(b - a)^{2}}{12}$$

**Preuve :**

-   Par définition :

$$\mathbb{E}(X) = \int_{\mathbb{R}}^{}{tf(t)dt} = \int_{a}^{b}{tf(t)dt} = \int_{a}^{b}{t\frac{1}{b - a}dt} = \frac{1}{b - a}\left\lbrack \frac{1}{2}t^{2} \right\rbrack_{a}^{b} = \frac{b^{2} - a^{2}}{2(b - a)} = \frac{a + b}{2}$$

-   Commençons par calculer $\int_{a}^{b}{t^{2}f(t)dt}$

$$\int_{\mathbb{R}}^{}{t^{2}f(t)dt} = \int_{a}^{b}{t^{2}\frac{1}{b - a}dt} = \frac{1}{b - a}\left\lbrack \frac{1}{3}t^{3} \right\rbrack_{a}^{b} = \frac{b^{3} - a^{3}}{3(b - a)} = \frac{a^{2} + ab + b^{2}}{3}$$

$$\text{Donc}\mathbb{\ V}(X) = \frac{a^{2} + ab + b^{2}}{3} - \left( \frac{a + b}{2} \right)^{2} = \frac{4a^{2} + 4ab + 4b^{2} - 3a^{2} - 6ab - 3b^{2}}{12} = \frac{b^{2} - 2ab + a^{2}}{12} = \frac{(b - a)^{2}}{12}$$

#### B.  Loi exponentielle de paramètre $\lambda$

La loi exponentielle sert à modéliser des phénomènes « sans mémoire », par exemple, la durée de vie de phénomène sans usure et sans vieillissement (par exemple, ampoule, radioactivité).

Le paramètre $\lambda$ est tel que la durée de vie moyenne du phénomène est $\frac{1}{\lambda}$

**Définition :**

On dit qu'une v.a.r. continue $X$ suit la loi exponentielle de paramètre $\lambda > 0$, notée $X\mathcal{\hookrightarrow E}(\lambda)$, si la densité de $X$ est :

$$f:t \rightarrow \left\lbrack  \begin{array}{r}
0\ \text{si}\ t < 0 \\
\lambda e^{- \lambda t}\ \text{si}\ t \geq 0
\end{array} \right. $$

**Remarque :**

On a bien défini une densité puisque $\forall\lambda > 0$, $\int_{\mathbb{R}}^{}{f(t)dt} = \int_{0}^{+ \infty}{\lambda e^{- \lambda t}dt} = \lambda\left\lbrack \frac{e^{- \lambda t}}{- \lambda} \right\rbrack_{0}^{+ \infty} = 1$

**Proposition :**

Soit $X\mathcal{\hookrightarrow E}(\lambda),\ \lambda > 0$

-   La fonction de répartition de $X$ est :

$$F(x) = 1 - e^{- \lambda x}$$

-   $X$ admet une espérance et $\mathbb{E}(X) = \frac{1}{\lambda}$

-   $X$ admet une variance et $\mathbb{V}(X) = \frac{1}{\lambda^{2}}$

**Preuve :**

-   Calcul de l'espérance

$$\mathbb{E}(X) = \int_{\mathbb{R}}^{}{tf(t)dt} = \int_{0}^{+ \infty}{t\lambda e^{- \lambda t}dt} =^{IPP}\lambda\left( \left\lbrack \frac{te^{- \lambda t}}{- \lambda} \right\rbrack_{0}^{+ \infty} - \int_{0}^{+ \infty}{\frac{e^{- \lambda t}}{- \lambda}dt} \right) = \int_{0}^{+ \infty}{e^{- \lambda t}dt} = \left\lbrack \frac{e^{- \lambda t}}{- \lambda} \right\rbrack_{0}^{+ \infty} = \frac{1}{\lambda}$$

-   Calcul de $\int_{\mathbb{R}}^{}{t^{2}f(t)dt}$

$$\int_{\mathbb{R}}^{}{t^{2}f(t)dt} = \int_{0}^{+ \infty}{t^{2}\lambda e^{- \lambda t}dt} = \lambda\left( \left\lbrack \frac{t^{2}e^{- \lambda t}}{- \lambda} \right\rbrack_{0}^{+ \infty} - \int_{0}^{+ \infty}{\frac{2te^{- \lambda t}}{- \lambda}dt} \right) = 2\int_{0}^{+ \infty}{te^{- \lambda t}dt} = \frac{2}{\lambda}\mathbb{E}(X) = \frac{2}{\lambda^{2}}$$

Donc :

$$\mathbb{V}(X) = \frac{2}{\lambda^{2}} - \left( \frac{1}{\lambda} \right)^{2} = \frac{1}{\lambda^{2}}$$

**Proposition :**

Soit $X\mathcal{\hookrightarrow E}(\lambda),\ \lambda > 0$

Pour tout $T$ et $x\mathbb{\in R}$,

$$\mathbb{P}\left( X \leq T + x \middle\vert  X \geq T \right)\mathbb{= P}(X \leq x)$$

(La loi est sans mémoire).

**Preuve :**

Par la définition des probabilités conditionnelles :

$$\mathbb{P}\left( X \leq T + x \middle\vert  X \geq T \right) = \frac{\mathbb{P}(X \leq T + x \cap X \geq T)}{\mathbb{P}(X \geq T)} = \frac{\mathbb{P}(T \leq X \leq T + x)}{\mathbb{P}(X \geq T)}$$

$$\mathbb{P}\left( X \leq T + x \middle\vert  X \geq T \right) = \frac{F(T + x) - F(T)}{1 - F(T)} = \frac{1 - e^{- \lambda(T + x)} - \left( 1 - e^{- \lambda T} \right)}{1 - \left( 1 - e^{- \lambda T} \right)} = \frac{e^{- \lambda T} - e^{- \lambda T - \lambda x}}{e^{- \lambda T}} = 1 - e^{- \lambda x} = F(x)\mathbb{= P}(X \leq x)$$

#### C.  Loi normale de paramètres $\mu$ et $\sigma^{2}$

Omniprésente dans les sciences naturelles, elle modélise des phénomènes qui sont conséquences d'une multitude de mécanismes élémentaires.

**Définition :**

On dit qu'une variable $X$ suit une loi Normale de paramètres $\mu$ et $\sigma^{2}$, $\mu\mathbb{\in R}$ et $\sigma\mathbb{\in R}$, notée $X \hookrightarrow \mathcal{N}\left( \mu,\sigma^{2} \right)$ si la densité de $X$ est :

$$f:t \rightarrow \frac{1}{\sqrt{2\pi\sigma^{2}}}e^{- \frac{(t - \mu)^{2}}{2\sigma^{2}}}$$

Cas particulier : On appelle loi normale centrée réduite la loi $\mathcal{N}(0,1)$ de densité gaussienne :

$$f(t) = \frac{1}{\sqrt{2\pi}}e^{- t^{2}}$$

**Proposition :**

Si $X \hookrightarrow \mathcal{N}\left( \mu,\sigma^{2} \right)$ alors :

-   $X$ admet une espérance et $\mathbb{E}(X) = \mu$

-   $X$ admet une variance et $\mathbb{V}(X) = \sigma^{2}$

**Proposition :**

-   Si $X \hookrightarrow \mathcal{N}\left( \mu,\sigma^{2} \right)$ et $Y \hookrightarrow \mathcal{N}\left( \mu^{'},{\sigma^{'}}^{2} \right)$, alors la variable $Z = X + Y$ suit une loi normale et :

$$Z \hookrightarrow \mathcal{N}\left( \mu + \mu^{'},\ \sigma^{2} + {\sigma^{'}}^{2} \right)$$

-   Si $X \hookrightarrow \mathcal{N}\left( \mu,\sigma^{2} \right)$ alors la variable $Y = \frac{X - \mu}{\sigma}$ suit une loi normale centrée réduite.

-   Si $X \hookrightarrow \mathcal{N}(0,1)$ et $\varphi$ est sa fonction de répartition :

<!-- -->

-   $\forall x\mathbb{\in R,\ }\varphi(x) + \varphi( - x) = 1$

-   $\forall x > 0,\ \mathbb{P}\left( \vert X \vert \leq x \right) = 2\varphi(x) - 1$
