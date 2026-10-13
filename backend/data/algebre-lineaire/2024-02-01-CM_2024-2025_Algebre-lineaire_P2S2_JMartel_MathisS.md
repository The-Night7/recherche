---
title: CM Algèbre linéaire et bilinéaire
author: [MathisS]
cyauthor: [JMartel]
date: 2024-02-01 01:00:00 +0100
categories: [PREING2 S2, Algebre-lineaire]
tags: [PREING2 S2,Algebre-lineaire,2024/2025,Mathis S.,J. Martel]
math: true
division_title : 2024/2025
---

# Chapitre 1 : Algèbre linéaire

**Rappel :**

Un $\mathbb{K}$-e.v. $(E, + , \bullet )$ vérifie

$$\forall x,y \in E,\ \forall\lambda,\mu\mathbb{\in K,\ }\lambda x + \mu y \in E$$

Soit $f:E \rightarrow F$ avec $E$ et $F$ des $\mathbb{K}$-e.v.

$f$ est linéaire si et seulement si $\forall x,y \in E,\ \forall\lambda,\mu \in \mathbb{K,\ }f(\lambda x + \mu y) = \lambda f(x) + \mu f(y)$

**Exemple :**

Soit $f\ :\mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$

$$(x,\ y) \rightarrow  \left( 2x,\frac{1}{3}y \right)$$

Soit $v = (0,1)$ alors $f(v) =  \left( 0,\frac{1}{3} \right)$

Soit $u = (1,0)$ alors $f(u) = (2,0)$

Soit $w = (1,1)$ alors $f(w) =  \left( 2,\frac{1}{3} \right)$

Soit $f:\mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$

$$(x,y) \rightarrow (x + y,x - y)$$

$$f(1,0) = (1,1)$$

$$f(0,1) = (1, - 1)$$

Soit $\varepsilon_{1} =  \left( 1 + \sqrt{2},\ 1 \right)$ et $\varepsilon_{2} =  \left( 1 - \sqrt{2},\ 1 \right)$

$$f \left( \varepsilon_{1} \right) =  \left( 2 + \sqrt{2},\ \sqrt{2} \right) = \sqrt{2} \left( 1 + \sqrt{2},\ 1 \right) = \sqrt{2}\varepsilon_{1}$$

$$f \left( \varepsilon_{2} \right) =  \left( 2 - \sqrt{2},\  - \sqrt{2} \right) = - \sqrt{2} \left( 1 - \sqrt{2},\ 1 \right) = - \sqrt{2}\varepsilon_{2}$$

Soit $u = \alpha\varepsilon_{1} + \beta\varepsilon_{2}$

Alors $f(u) = \alpha f \left( \varepsilon_{1} \right) + \beta f \left( \varepsilon_{2} \right) = \alpha\varepsilon_{1}\sqrt{2} - \beta\varepsilon_{2}\sqrt{2}$

## I.  Eléments propres

**Rappel :**

Un endomorphisme $f\mathcal{\in L}(E)$ est une application linéaire $f:E \rightarrow E$

### 1.  Valeurs propres et vecteurs propres

**Définition :** Valeurs propres

Soit $f\mathcal{\in L}(E)$ (un endomorphisme de $E$) et $\lambda \in \mathbb{K}$

On dit que $\lambda$ est une valeur propre de $f$ si et seulement s'il existe $v \in E\backslash \left\lbrace 0_{E} \right\rbrace$ tel que $f(v) = \lambda v$

**Remarque :** 

$$f \left( 0_{E} \right) = 0_{E} = \lambda 0_{E}\ \forall\lambda\mathbb{\in K}$$

-   Le vecteur $v$ est alors appelé vecteur propre de $f$ associé à la valeur propre $\lambda$.

-   L'ensemble des valeurs propres de $f$ est appelé le spectre de $f$ noté $Sp(f)$

-   Soit $v \in E\backslash\left\lbrace 0_{E}\right\rbrace$. $v$ est un vecteur propre de $f$ si et seulement si $\exists\lambda\mathbb{\in K,\ }f(v) = \lambda v$

-   Les valeurs propres et les vecteurs propres sont les éléments propres de $f$

**Exemple :**

$$f:\mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$$

$$(x,y) \rightarrow  \left( x - \frac{y}{2},\  - \frac{x}{2} + y \right)$$

Montrer que $v_{1} = (1,1)$ est un vecteur propre de $f$ associé à la valeur propre $\lambda_{1} = \frac{1}{2}$.

$$f \left( v_{1} \right) =  \left( \frac{1}{2},\frac{1}{2} \right) = \frac{1}{2}(1,1) = \lambda_{1}v_{1}$$

Soit $v_{2} = (1, - 1)$. On a $f \left( v_{2} \right) = \frac{3}{2}v_{2}$

**Rappel :**

$F \subset E$ est un sous-espace vectoriel si :

-   C'est un espace vectoriel

-   $\forall x,y \in F,\ \forall\lambda,\mu\mathbb{\in K,\ }\lambda x + \mu y \in F$

### 2.  Sous-espaces propres

Rappel : $\ker f =  \left\lbrace x \in E,\ f(x) = 0_{E} \right\rbrace$, $\ker f$ est un s.e.v. de $E$

**Proposition :**

Soit $f\mathcal{\in L}(E)$ et $\lambda \in \mathbb{K}$

L'ensemble $E_{\lambda}$ défini par $E_{\lambda} =  \left\lbrace x \in E,\ f(x) = \lambda x \right\rbrace$ est un sous-espace vectoriel.

En particulier, il est égal à $E_{\lambda} = \ker(f - \lambda Ιd)$

**Démonstration :** Montrons que $E_{\lambda} = \ker(f - \lambda Id)$

$$x \in E_{\lambda}$$

$$\Leftrightarrow (x) = \lambda x \Leftrightarrow f(x) - \lambda x = 0_{E} \Leftrightarrow (f - \lambda Id)(x) = 0$$

$$\Leftrightarrow x \in \ker(f - \lambda Id)$$

Donc $E_{\lambda}$ est un s.e.v.

**Définition :**

Si 
$$E_{\lambda} \neq  \left\lbrace 0_{E} \right\rbrace$$
alors $E_{\lambda}$ est appelé sous-espace propre associé à $\lambda$.

**Rappel :**

$f$ est injective si et seulement si $f(x) = f(y) \Rightarrow x = y$

Si $f:E \rightarrow F$ est une application linéaire, alors $f$ est injective si et seulement si $\ker f =  \left\lbrace 0_{E} \right\rbrace$

$f$ est surjective si et seulement si $\forall y \in F,\ \exists x \in E,\ f(x) = y$

Si $f\ :E \rightarrow F$ est une application linéaire, alors $f$ est surjective si et seulement si $\text{Im}\ f = F$ avec $\text{Im}\ f ≔ f(E) =  \left\lbrace f(x),\ x \in E \right\rbrace \subset F
\text{Im}\ f$ est un s.e.v. de $F$.

**Proposition :**

Soit $f\mathcal{\in L}(E),\ \lambda\mathbb{\in K}$

$$\lambda \in Sp(f) \Leftrightarrow E_{\lambda} \neq  \left\lbrace 0_{E} \right\rbrace \Leftrightarrow (f - \lambda Id)\ \text{n'est pas injective}$$

**Démonstration :**

$$\lambda \in Sp(f) \Leftrightarrow \exists x \in E\backslash \left\lbrace 0_{E} \right\rbrace,\ f(x) = \lambda x \Leftrightarrow x \in E_{\lambda} \Leftrightarrow E_{\lambda} \neq  \left\lbrace 0_{E} \right\rbrace$$

Or $E_{\lambda} = \ker(f - \lambda Id)$ donc $E_{\lambda} \neq  \left\lbrace 0_{E} \right\rbrace \Leftrightarrow (f - \lambda Id)\ \text{n'est pas injective}$

**Proposition :**

Soit $f\mathcal{\in L}(E)$, $v_{1}$ et $v_{2}$ deux vecteurs propres de $f$ associés à $\lambda_{1}$ et $\lambda_{2}\mathbb{\in K}$ tels que $\lambda_{1} \neq \lambda_{2}$

Alors $v_{1}$ et $v_{2}$ sont libres (non colinéaires).

**Démonstration :**

Montrons que $v_{1}$ et $v_{2}$ ne sont pas colinéaires. $v_{1}$ et $v_{2}$ sont colinéaires si et seulement si $\exists\alpha\mathbb{\in K,\ }v_{1} = \alpha v_{2}$

Par l'absurde, supposons que $v_{1}$ et $v_{2}$ sont colinéaires, $v_{1} = \alpha v_{2},\ \alpha\mathbb{\in K}$

$$f \left( v_{1} \right) = \lambda_{1}v_{1},\ f \left( v_{2} \right) = \lambda_{2}v_{2}$$

Aussi, $f \left( v_{1} \right) = f \left( \alpha v_{2} \right) = \alpha f \left( v_{2} \right) = \alpha\lambda_{2}v_{2}$

Ainsi $\lambda_{1}v_{1} = \alpha\lambda_{2}v_{2}$

Si $\lambda_{1} \neq 0$

Donc $v_{1} = \alpha \left( \frac{\lambda_{2}}{\lambda_{1}} \right)v_{2}$ et $v_{1} = \alpha v_{2}$

Donc $\frac{\lambda_{2}}{\lambda_{1}} = 1,\ \lambda_{1} = \lambda_{2}$, ce qui est absurde.

Si $\lambda_{1} = 0$, alors $\lambda_{2} \neq 0$

$$f \left( v_{2} \right) = f \left( \frac{1}{\alpha}v_{1} \right) = \frac{1}{\alpha}f \left( v_{2} \right) = \frac{1}{\alpha}\lambda_{1}v_{1}$$

$$f \left( v_{2} \right) = \lambda_{2}v_{2}$$

$$v_{2} = \frac{1}{\alpha}\frac{\lambda_{1}}{\lambda_{2}}v_{1} = \frac{1}{\alpha}v_{1}$$

Donc $\lambda_{1} = \lambda_{2}$ ce qui est absurde.

**Rappel :**

Soit $U =  \left\lbrace u_{1},\ldots,u_{n} \right\rbrace$ famille de vecteurs d'un e.v. $E$.

$U$ est une famille libre de $E$ si et seulement si

$$\alpha_{1}u_{1} + \ldots + \alpha_{n}u_{n} \Rightarrow \alpha_{1} = \ldots = \alpha_{n} = 0$$

Une famille est liée si elle n'est pas libre.

**Théorème :**

Soit $v_{1},\ldots,v_{p}$ $p$ vecteurs propres de $f$ associés aux valeurs propres $\lambda_{1},\ldots,\lambda_{p}$ tels que les $\lambda_{i}$ sont différents deux à deux (uniques).

Alors la famille $ \left\lbrace v_{1},\ldots,v_{p} \right\rbrace$ est libre.

**Démonstration :** Par récurrence

Le cas $p = 2$ est la proposition précédente.

Supposons $ \left\lbrace v_{1},\ \ldots,\ v_{p + 1} \right\rbrace$ des vecteurs propres associés à $\lambda_{1},\ldots,\lambda_{p + 1}\mathbb{\in K}$

Alors $\left\lbrace v_{1},\ldots,v_{p}\right\rbrace$ sont des vecteurs propres de $f$ et par hypothèse de récurrence ils forment une famille libre.

Soit $\alpha_{1},\ldots,\alpha_{p + 1}\mathbb{\in K}$ tels que $\alpha_{1}v_{1} + \ldots + \alpha_{p + 1}v_{p + 1} = 0_{E}\ (*)$

On applique $f$ à $(*)\ $:

$$f \left( \alpha_{1}v_{1} + \ldots + \alpha_{p + 1}v_{p + 1} \right) = f \left( 0_{E} \right) = 0_{E}$$

Par linéarité de $f$,

$$\alpha_{1}f \left( v_{1} \right) + \ldots + \alpha_{p + 1}f \left( v_{p + 1} \right) = 0_{E}$$

$$\alpha_{1}\lambda_{1}v_{1} + \ldots + \alpha_{p + 1}\lambda_{p + 1}v_{p + 1} = 0_{E}\ (1)$$

En multipliant $(*)$ par $\lambda_{p + 1}$,

$$\lambda_{p + 1} \left( \alpha_{1}v_{1} + \ldots + \alpha_{p + 1}v_{p + 1} \right) = 0_{E}\ (2)$$

Avec $(1) - (2)$

$$ \left( \alpha_{1}\lambda_{1}v_{1} + \ldots + \alpha_{p + 1}\lambda_{p + 1}v_{p + 1} \right) -  \left( \alpha_{1}\lambda_{p + 1}v_{1} + \ldots + \alpha_{p + 1}\lambda_{p + 1}v_{p + 1} \right) = 0_{E}$$

$$ \left( \alpha_{1}\lambda_{1}v_{1} + \ldots + \alpha_{p}\lambda_{p}v_{p} \right) -  \left( \alpha_{1}\lambda_{p + 1}v_{1} + \ldots + \alpha_{p}\lambda_{p + 1}v_{p} \right) = 0_{E}$$

$$ \alpha_{1} \left( \lambda_{1} - \lambda_{p + 1} \right)v_{1} + \ldots + \alpha_{p} \left( \lambda_{p} - \lambda_{p + 1} \right)v_{p} = 0_{E} $$

Or, par hypothèse de récurrence, $ \left\lbrace v_{1},\ldots,v_{p} \right\rbrace$ est une famille libre.

$$\alpha_{1} \left( \lambda_{1} - \lambda_{p + 1} \right) = \ldots = \alpha_{p} \left( \lambda_{p} - \lambda_{p + 1} \right) = 0$$

Or les $\lambda_{i}$ sont distincts deux à deux, $\forall i \in  \left. ⟦1,p \right.⟧,\ \lambda_{i} - \lambda_{p + 1} \neq 0$

$$\alpha_{1} = \ldots = \alpha_{p} = 0$$

Donc d'après $(*)$, $\alpha_{p + 1}v_{p + 1} = 0$

Or $v_{p + 1} \neq 0_{E}$ 

donc $\alpha_{p + 1} = 0$

Donc $\alpha_{1} = \ldots = \alpha_{p + 1} = 0$

Donc $\left\lbrace v_{1},\ldots,v_{p + 1}\right\rbrace$ est une famille libre.

**Rappel :** Espaces vectoriels en somme directe

Soit $F_{1}$ et $F_{2}$ des sous-espaces vectoriels de $E$.

$$F_{1} + F_{2} =  \left\lbrace x \in E,\ x = x_{1} + x_{2},\ x_{1} \in F_{1},\ x_{2} \in F_{2} \right\rbrace$$

-   $F_{1} + F_{2}$ est un s.e.v. de $E$.

-   $\dim \left( F_{1} + F_{2} \right) = \dim \left( F_{1} \right) + \dim \left( F_{2} \right) - \dim \left( F_{1} \cap F_{2} \right)$

$F_{1}$ et $F_{2}$ sont en somme directe si et seulement si 

$F_{1} \cap F_{2} =  \left\lbrace 0_{E} \right\rbrace$

On note alors leur somme $F_{1} \oplus F_{2}$

Alors $\dim \left( F_{1} \oplus F_{2} \right) = \dim \left( F_{1} \right) + \dim \left( F_{2} \right)$

**Rappel :** Espaces vectoriels supplémentaires

Si $F_{1} \oplus F_{2} = E$, on dit que $F_{1}$ et $F_{2}$ sont supplémentaires, ou que $F_{2}$ est un supplémentaire de $F_{1}$.

Il faut vérifier :

-   $F_{1} \cap F_{2} =  \left\lbrace 0_{E} \right\rbrace$

-   $F_{1} + F_{2} = E$

**Théorème :**

$F_{1}$ et $F_{2}$ sont supplémentaires dans $E$ si et seulement si l'une des assertions suivantes et équivalentes est vérifiée :

-   $\forall x \in E,\ \exists! \left( x_{1},x_{2} \right) \in F_{1} \times F_{2},\ x = x_{1} + x_{2}$ ($\exists!$ : il existe un unique)

-   $\dim \left( F_{1} \right) + \dim \left( F_{2} \right) = \dim(E)$ et $F_{1} \cap F_{2} = \left\lbrace 0_{E}\right\rbrace$

-   $\dim \left( F_{1} \right) + \dim \left( F_{2} \right) = \dim(E)$ et $F_{1} + F_{2} = E$

**Définition :**

Soit $E$ un espace vectoriel et $ \left\lbrace F_{1},\ldots,F_{p} \right\rbrace$ une famille de s.e.v. de $E$.

On dit que la famille $ \left\lbrace F_{1},\ldots,F_{p} \right\rbrace$ 
est en somme directe si et seulement 
si, $\forall \left( x_{1},\ldots,x_{p} \right) \in F_{1} \times \ldots \times F_{p}$, 
$x_{1} + \ldots + x_{p} = 0_{E} \Rightarrow x_{1} = \ldots = x_{p} = 0_{E}$

Dans ce cas, $F_{1} + \ldots + F_{p}$ est noté $F_{1} \oplus \ldots \oplus F_{p}$

**Proposition :**

La somme est directe si et seulement si, $\forall i \in  \left. ⟦2,n \right.⟧$,

$$F_{i} \cap \sum_{j = 1}^{i - 1}F_{j} =  \left\lbrace 0_{E} \right\rbrace$$

**Exemple :**

$F_{1},F_{2},F_{3}$ sont en somme directe si et seulement si $F_{1} \cap F_{2} =  \left\lbrace 0_{E} \right\rbrace$ et $F_{3} \cap  \left( F_{1} + F_{2} \right) =  \left\lbrace 0_{E} \right\rbrace$

**Théorème :**

Soit $f\mathcal{\in L}(E)$, soient $\lambda_{1},\ldots,\lambda_{p}$ des valeurs propres de $f$ deux à deux distinctes.

Alors les sous-espaces propres associés $E_{\lambda_{1}},\ldots,E_{\lambda_{p}}$ sont en somme directe.

**Démonstration :**

Soit $x \in E_{\lambda_{i}} \cap  \left( E_{\lambda_{1}} + \ldots + E_{\lambda_{i - 1}} \right)$. Montrons que $x = 0_{E}$.

$x \in E_{\lambda_{i}}$ et $x \in E_{\lambda_{1}} + \ldots + E_{\lambda_{i - 1}}$

$$x = x_{1} + \ldots + x_{i - 1}\ \text{où}\ x_{k} \in Ε_{\lambda_{k}}$$

$$f(x) = \lambda_{i}x\ (1)$$

$$f(x) = \lambda_{1}x_{1} + \ldots + \lambda_{i - 1}x_{i - 1}\ (2)$$

D'après $(1)$ et $(2)$,

$$\lambda_{i}x = \lambda_{1}x_{1} + \ldots + \lambda_{i - 1}x_{i - 1}$$

$$\lambda_{1}x_{1} + \ldots + \lambda_{i - 1}x_{i - 1} - \lambda_{i}x = 0\ (*)$$

Supposons que $x \neq 0_{E}$

Alors $ \left\lbrace x_{1},\ldots,x_{i - 1},x \right\rbrace$ sont des vecteurs propres associés aux valeurs propres $\lambda_{1},\ldots,\lambda_{i}$ deux à deux distincts.

D'après le théorème précédent, $ \left\lbrace x_{1},\ldots,x_{i - 1},\ x \right\rbrace$ forme une famille libre.

Par $(*),\ \lambda_{1} = \ldots = \lambda_{i} = 0$, ce qui est absurde.

Ainsi $x = 0_{E}$

## II. Représentation matricielle

**Rappels :**

Soit $E$ un espace vectoriel.

-   Si $E$ est un espace vectoriel de dimension $n\mathbb{\in N}$, alors toutes les bases de $E$ ont pour cardinal $n$.

-   Une base de $E$ est une famille libre et génératrice

-   $ \left\lbrace v_{1},\ldots,v_{n} \right\rbrace$ est génératrice de $E$ si et seulement si $\forall x \in E,\ \exists\lambda_{1},\ldots,\lambda_{n}$ tels que $x = \lambda_{1}v_{1} + \ldots + \lambda_{n}v_{n}$. Si $ \left( v_{1},\ldots,v_{n} \right)$ est une base, alors les $\lambda_{1},\ldots,\lambda_{n}$ sont uniques et sont appelés coordonnées de $x$ dans la base $ \left( v_{1},\ldots,v_{n} \right)$

-   Si $E$ est muni d'une base $\mathcal{B =} \left( e_{1},\ldots,e_{n} \right)$, on identifie $E$ à $\mathbb{R}^{n}$ en notant les éléments de $E$ en coordonnées dans la base $\mathcal{B}$. $x = \lambda_{1}e_{1} + \ldots + \lambda_{n}e_{n} =  \left( \lambda_{1},\ldots,\lambda_{n} \right)_{\mathcal{B}}$

Soit $f\mathcal{\in L}(E)$

$$Mat_{\mathcal{B}}f =  \left( f \left( e_{1} \right)_{\mathcal{B}} \right\vert \ldots \left\vert  f \left( e_{n} \right)_{\mathcal{B}} \right)$$

Si $x =  \left( x_{1},\ldots,x_{n} \right)_{\mathcal{B}}$, 

$$f(x)_{\mathcal{B}} = Mat_{\mathcal{B}}f \times \begin{pmatrix}
x_{1} \\
 \vdots \\
x_{n}
\end{pmatrix}$$

**Définition :**

Soit $f\mathcal{\in L}(E)$, $\mathcal{B}$ une base de $E$ et $A = Mat_{\mathcal{B}}f$

-   $\lambda$ est une valeur propre de $A$ si et seulement si $\lambda$ est une valeur propre de $f$

-   $Sp(A) = Sp(f)$

-   $x \in E$ est un vecteur propre de $A$ et $x$ est un vecteur propre de $f$

**Proposition/Définition :**

$$X = \begin{pmatrix}
x_{1} \\
 \vdots \\
x_{n}
\end{pmatrix}\ \text{est un vecteur propre de}\ A\text{ si et seulement si}\ X \neq 0_{E}\ \text{et}\ AX = \lambda Χ$$

$$Ε_{\lambda} =  \left\lbrace X \in \mathbb{K}^{n},\ AX = \lambda X \right\rbrace$$

$$\lambda \in Sp(A) \Leftrightarrow E_{\lambda} \neq  \left\lbrace 0_{E} \right\rbrace \Leftrightarrow \ker \left( A - \lambda I_{n} \right) \neq  \left\lbrace 0_{E} \right\rbrace \Leftrightarrow  \left( A - \lambda Ι_{n} \right)\ \text{n'est pas inversible}$$

**Exercice :**

$$A = \begin{pmatrix}
1 & - 1 & - 1 \\ - 1 & 1 & - 1 \\ - 1 & - 1 & 1
\end{pmatrix}$$

Montrer que $v_{1} = \begin{pmatrix}
1 \\
1 \\
1
\end{pmatrix}$ est un vecteur propre de $A$. Alors $Av_{1} = \lambda v_{1}$

$$Av_{1} = \begin{pmatrix}
 - 1 \\ - 1 \\ - 1
\end{pmatrix} = - v_{1}$$

$v_{1}$ est un vecteur propre de valeur propre associée $- 1$.

**Rappel :** Changement de base

Soient deux bases 
$\mathcal{B =} \left( e_{1},e_{2},e_{3} \right)$ et $\mathcal{B}^{'} =  \left( \varepsilon_{1},\varepsilon_{2},\varepsilon_{3} \right)$ de $\mathbb{R}^{3}$

On a :

$$\varepsilon_{1} = \begin{pmatrix}
1 \\
1 \\
0
\end{pmatrix}_{\mathcal{B}},\ \varepsilon_{2} = \begin{pmatrix}
 - 2 \\
0 \\
1
\end{pmatrix}_{\mathcal{B}},\varepsilon_{3} = \begin{pmatrix}
2 \\ - 2 \\
3
\end{pmatrix}_{\mathcal{B}}$$

$$\varepsilon_{1} = e_{1} + e_{2},\ \ \varepsilon_{2} = - 2e_{1} + e_{3},\ \ \varepsilon_{3} = 2e_{1} - 2e_{2} + 3e_{3}$$

$$\varepsilon_{1} = \begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix}_{\mathcal{B}^{'}},\ \varepsilon_{2} = \begin{pmatrix}
0 \\
1 \\
0
\end{pmatrix}_{\mathcal{B}^{'}},\ \varepsilon_{3} = \begin{pmatrix}
0 \\
0 \\
1
\end{pmatrix}_{\mathcal{B}^{'}}$$

Soit 
$$u = \begin{pmatrix} 2 \\ - 4 \\ 1 \end{pmatrix}_{\mathcal{B}} = 2e_{1} - 4e_{2} + e_{3}$$

Quelles sont les coordonnées de $u$ dans la base $\mathcal{B}^{'}\ $?

**Méthode 1 :**\
Soient $\alpha,\beta,\gamma\mathbb{\in R}$ tels que $u = \alpha\varepsilon_{1} + \beta\varepsilon_{2} + \gamma\varepsilon_{3}$

Alors $2e_{1} - 4e_{2} + e_{3} = \alpha\varepsilon_{1} + \beta\varepsilon_{2} + \gamma\varepsilon_{3}$

$$\Leftrightarrow 2e_{1} - 4e_{2} + e_{3} = \alpha \left( e_{1} + e_{2} \right) + \beta \left( - 2e_{1} + e_{3} \right) + \gamma \left( 2e_{1} - 2e_{2} + 3e_{3} \right)$$

$$\Leftrightarrow 2e_{1} - 4e_{2} + e_{3} = e_{1}(\alpha - 2\beta + 2\gamma) + e_{2}(\alpha + \beta - 2\gamma) + e_{3}(\beta + 3\gamma)$$

Or, l'écriture d'un vecteur dans $\mathcal{B}$ est unique :

$$ \left\lbrace \begin{array}{r}
2 = \alpha - 2\beta + 2\gamma \\ - 4 = \alpha + \beta - 2\gamma \\
1 = \beta + 3\gamma
\end{array} \right\rbrace$$

**Méthode 2 :**

$$P =  \left\lbrack \varepsilon_{1}\ \varepsilon_{2}\ \varepsilon_{3} \right\rbrack = \begin{bmatrix}
1 & - 2 & 2 \\
1 & 0 & - 2 \\
0 & 1 & 3
\end{bmatrix}$$

Pour ne pas se tromper : $P\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix} = \begin{pmatrix}
1 \\
1 \\
0
\end{pmatrix} =  \left( \varepsilon_{1} \right)_{\mathcal{B}}$

Si $u = \alpha\varepsilon_{1} + \beta\varepsilon_{2} + \gamma\varepsilon_{3}$, $u = \begin{pmatrix}
\alpha \\
\beta \\
\gamma
\end{pmatrix}_{\mathcal{B}^{'}}$

Alors :

$$P\begin{pmatrix}
\alpha \\
\beta \\
\gamma
\end{pmatrix}_{\mathcal{B}^{'}} = \begin{pmatrix}
2 \\ - 4 \\
1
\end{pmatrix}_{\mathcal{B}}$$

$$\begin{pmatrix}
\alpha \\
\beta \\
\gamma
\end{pmatrix}_{\mathcal{B}^{'}} = P^{- 1}\begin{pmatrix}
2 \\ - 4 \\
1
\end{pmatrix}_{\mathcal{B}}$$

**Rappel :**

Soit $\mathcal{B =} \left( e_{1},e_{2},e_{3} \right)$ base de $\mathbb{R}^{3}$ et $P =  \left\lbrack \varepsilon_{1}\ \varepsilon_{2}\ \varepsilon_{3} \right\rbrack$, alors $\mathcal{B}^{'} =  \left( \varepsilon_{1},\varepsilon_{2},e_{3} \right)$ si et seulement si $P$ est inversible, ou $\det P = 0$

Alors soit $X$ un vecteur de coordonnées dans la base $\mathcal{B}$ et $X^{'}$ les coordonnées dans un même vecteur dans la base $\mathcal{B}^{'}$. Alors, $PX^{'} = X$

Soit $A = Mat_{\mathcal{B}}(f) = \begin{pmatrix}
2 & 4 & 0 \\
1 & 2 & - 1 \\
3 & - 2 & 1
\end{pmatrix} =  \left( f \left( e_{1} \right)\ f \left( e_{2} \right)\ f \left( e_{3} \right) \right)$

$$f \left( e_{1} \right) = 2e_{1} + e_{2} + 3e_{3}$$

$$f \left( e_{2} \right) = 4e_{1} + 2e_{2} - 2e_{3}$$

$$f \left( e_{3} \right) = - e_{2} + e_{3}$$

Soit $X$ le vecteur des coordonnées de $v$ dans la base $\mathcal{B}$. Alors $AX$ est le vecteur des coordonnées de $f(v)$ dans $\mathcal{B}$

Comment écrire $Mat_{\mathcal{B}^{'}}(f)\ $?

Soit $X$ et $X^{'}$ les coordonnées de $v$ dans $\mathcal{B}$ et $\mathcal{B}^{'}$, alors $PX^{'} = X$. Notons $Y$ et $Y^{'}$ les coordonnées de $f(v)$ dans la base $\mathcal{B}$ et $\mathcal{B}^{'}$. Alors $PY^{'} = Y$

$$Y = Mat_{\mathcal{B}}(f)X = Mat_{\mathcal{B}}(f)PX^{'}$$

Donc $PY^{'} = Mat_{\mathcal{B}}(f)PX^{'}$

$$Y^{'} = P^{- 1}Mat_{\mathcal{B}}(f)PX^{'} = Mat_{\mathcal{B}^{'}}(f)X^{'}$$

**Proposition :**

$$Mat_{\mathcal{B}^{'}}(f) = P^{- 1}Mat_{\mathcal{B}}(f)P$$

Comment le retrouver ?

La matrice $Mat_{\mathcal{B}^{'}}(f)$ prend des vecteurs de $\mathcal{B}^{'}$, donc la première matrice (celle à droite) prend des vecteurs de $\mathcal{B}^{'}\ $: $P$.

**Définition :**

Soient $A$ et $A^{'} \in \mathcal{M}_{n} \left( \mathbb{K} \right)$

On dit que $A$ et $A^{'}$ sont semblables si et seulement s'il existe $P \in GL_{n} \left( \mathbb{K} \right)$ tel que $A^{'} = PAP^{- 1}$

## III. Polynôme caractéristique

**Définition :**

Soit $A \in \mathcal{M}_{n} \left( \mathbb{K} \right)$.

Le polynôme caractéristique de $A$ est noté $P_{A}(\lambda)$ est défini par :

$$P_{A}(\lambda) ≔ \det \left( A - \lambda I_{n} \right)$$

$$P_{A}(\lambda)\mathbb{\in K}\lbrack\lambda\rbrack$$

L'équation $P_{A}(\lambda) = 0$ est appelée équation caractéristique.

**Proposition :**

Deux matrices semblables ont le même polynôme caractéristique.

**Démonstration :**

Soient 
$$A,B \in \mathcal{M}_{n} \left( \mathbb{K} \right)$$
$$P \in GL_{n} \left( \mathbb{K} \right)$, tels que $B = PAP^{- 1}$$

$$P_{B}(\lambda) = \det \left( B - \lambda I_{n} \right) = \det \left( PAP^{- 1} - \lambda PP^{- 1} \right) $$
$$= \det \left( P \left( AP^{- 1} - \lambda P^{- 1} \right) \right) $$
$$= \det \left( P \left( A - \lambda I_{n} \right)P^{- 1} \right) $$
$$= \det(P)\det \left( A - \lambda I_{n} \right)\det \left( P^{- 1} \right) $$
$$= \det \left( A - \lambda I_{n} \right)\det(P)\det \left( P^{- 1} \right)$$

Or $\det(P)\det \left( P^{- 1} \right) = 1$

Donc $P_{A}(\lambda) = P_{B}(\lambda)$

**Conséquence :**

Soit $f$ un endomorphisme. Quel que soit la base dans laquelle on écrit sa matrice, le polynôme caractéristique est le même. Il ne dépend pas de la base de calcul, il dépend que de $f$.

**Définition :**

Le polynôme caractéristique de $f$ est le polynôme caractéristique de $f$ dans la base $\mathcal{B}$

$P_{f}(\lambda) ≔ P_{Mat_{\mathcal{B}}(f)}(\lambda) = \det \left( Mat_{\mathcal{B}}(f) - \lambda I_{n} \right)$ où $\mathcal{B}$ est n'importe quelle base.

**Proposition :**

Soit $A \in M_{n} \left( \mathbb{K} \right),\ \lambda\mathbb{\in K}$

$$\lambda \in Sp(A) \Leftrightarrow P_{A}(\lambda) = 0$$

**Démonstration :**

$$\lambda \in Sp(A) \Leftrightarrow  \left( A - \lambda I_{n} \right)\ \text{non inversible} \Leftrightarrow \det \left( A - \lambda I_{n} \right) = 0$$

**Exemple :**

$$A = \begin{pmatrix}
0 & 0 & 4 \\
1 & 2 & 1 \\
2 & 4 & - 2
\end{pmatrix}$$

Trouver les valeurs propres de $A\ $:

$$A - \lambda I_{3} = \begin{pmatrix}
 - \lambda & 0 & 4 \\
1 & 2 - \lambda & 1 \\
2 & 4 & - 2 - \lambda
\end{pmatrix}$$

$$P_{A}(\lambda) =  \left\vert  \begin{matrix}
 - \lambda & 0 & 4 \\
1 & 2 - \lambda & 1 \\
2 & 4 & - 2 - \lambda
\end{matrix} \right\vert $$

$$P_{A}(\lambda) = - \lambda \left\vert  \begin{matrix}
2 - \lambda & 1 \\
4 & - 2 - \lambda
\end{matrix} \right\vert  + 4 \left\vert  \begin{matrix}
1 & 2 - \lambda \\
2 & 4
\end{matrix} \right\vert  = \ldots = - \lambda^{3} + 16\lambda = - \lambda(\lambda - 4)(\lambda + 4)$$

Alors $Sp(A) =  \left\lbrace - 4,0,4 \right\rbrace$

**Corollaire :**

0 est valeur propre de $A$ si et seulement si $A$ n'est pas inversible.

**Théorème :** (Admis)

Soit $A \in \mathcal{M}_{n} \left( \mathbb{K} \right)$

$$P_{A}(\lambda) = ( - 1)^{n}\lambda^{n} + ( - 1)^{n - 1}Tr(A)\lambda^{- 1} + \ldots + \det(A)$$

**Corollaire :**

Soit $A \in \mathcal{M}_{2} \left( \mathbb{K} \right)$

$$P_{A}(\lambda) = \lambda^{2} - Tr(A)\lambda + \det(A)$$

**Corollaire :**

Une matrice de $\mathcal{M}_{n} \left( \mathbb{K} \right)$ a au plus $n$ valeurs propres.

**Démonstration :**

En effet, le polynôme caractéristique d'une matrice de $\mathcal{M}_{n} \left( \mathbb{K} \right)$ est de degré $n$ donc admet au plus $n$ racines.

**Définition :**

Soit $P \in \mathbb{K}\lbrack X\rbrack$

On appelle ordre de multiplicité d'une racine $a$ de $P$ le plus petit $n \in \mathbb{N}$ tel que $P$ est divisible par $(X - a)^{n}$.

On appelle ordre de multiplicité d'une valeur propre $\lambda$ son ordre de multiplicité pour le polynôme caractéristique. Il est noté $m_{\lambda}$.

**Définition :** Polynôme scindé

Soit $P \in \mathbb{K}\lbrack X\rbrack$. $P$ est scindé s'il peut s'écrire sous la forme :

$$P = c\prod_{i = 1}^{k}(X - a)^{m}$$

Avec $a_{1},\ldots,a_{k}\mathbb{\in K}$ et $m_{1},\ldots,m_{k} \in \mathbb{N}^{*}$

$$\text{Alors}\deg P = \sum_{i = 1}^{k}m_{k}$$

$P$ est scindé s'il admet exactement $n$ racines comptées avec multiplicité.

**Exemple :**

$P = X^{2} - 5X + 6 = (X - 2)(X - 3)$ est scindé.

$P = X^{3} - 4X^{2} + 5X - 2 = (X - 1)^{2}(X - 2)$ est scindé

$P = X^{2} + 1$ n'est pas scindé dans $\mathbb{R}$ (car n'a pas de racines) mais dans $\mathbb{C}$, $P = (X - i)(X + i)\mathbb{\in C}\lbrack X\rbrack$ donc $P$ est scindé.

**Théorème de d'Alembert-Gauss :**

Tout polynôme de $\mathbb{C}\lbrack X\rbrack$ est scindé. $\mathbb{C}$ est dit « corps algébriquement clos ».

**Remarque :**

$P \in \mathbb{R}\lbrack X\rbrack\mathbb{\subset C}\lbrack X\rbrack$ donc $P$ est scindé dans $\mathbb{C}$. Il est scindé sur $\mathbb{R}$ si et seulement si toutes ses racines sont réelles.

**Corollaire :**

Si $E$ est un $\mathbb{C -}ev$ de dimension $n$ alors $f \in \mathcal{L}(E)$ admet exactement $n$ valeurs propres comptées avec multiplicité.

Si $E$ est un $\mathbb{R -}ev$ de dimension $n$ alors $f \in \mathcal{L}(E)$ admet au plus $n$ valeurs propres comptées avec multiplicité.

**Exemple :**

$$A = \begin{pmatrix}
0 & 1 \\ - 1 & 0
\end{pmatrix}$$

$$P_{A}(\lambda) = \lambda^{2} + 1$$

$$Sp_{\mathbb{R}}(A) = \varnothing,\ Sp_{\mathbb{C}}(A) =  \left\lbrace \pm i \right\rbrace$$

**Remarque :**

Soit 
$$A \in \mathcal{M}_{n} \left( \mathbb{K} \right)$$
tel que $P_{A}$ est scindé : 
$$P_{A}(\lambda) = ( - 1)^{n}\prod_{i = 0}^{h} \left( \lambda - \lambda_{i} \right)^{m_{i}}$$

Alors :

$$\sum_{i = 0}^{k}{m_{i}\lambda_{i}} = Tr(A)$$

$$\prod_{i = 0}^{h}\lambda_{i}^{m_{i}} = \det(A)$$

**Démonstration :**

On développe.

$$P_{A}(\lambda) = ( - 1)^{n}\lambda^{n} + ( - 1)^{n - 1} \left( \sum_{i = 0}^{n}{m_{i}\lambda_{i}} \right)\lambda^{n - 1} + \ldots + \prod_{i = 0}^{h}\lambda_{i}^{m_{i}}$$

**Remarque :**

Dans $\mathbb{C}$, la proposition précédente est toujours vérifiée.

**Théorème :**

Soit 

$A \in \mathcal{M}_{n} \left( \mathbb{K} \right)$ et $\lambda \in Sp(A)$

de multiplicité $m_{\lambda}$

Alors $$1 \leq \dim \left( E_{\lambda} \right) \leq m_{\lambda}$$

**Démonstration :**

Par définition : 

$\lambda \in Sp_{\mathbb{K}}(A) \Rightarrow E_{\lambda} \neq  \left\lbrace 0_{E} \right\rbrace$, 

donc $\dim \left( E_{\lambda} \right) \geq 1_{}$

Si $\dim \left( E_{\lambda} \right) = n$, alors $E_{\lambda} = E$, donc $\forall x \in E,\ Ax = \lambda x$. Alors $A = \lambda I_{n}$, $ \left( A - \lambda I_{n} \right) = 0_{n}$.

$P_{A}(X) = \det \left( A - XI_{n} \right) = \det \left( (\lambda - Χ)I_{n} \right) = (\lambda - X)^{n}$ d'où $m_{\lambda} = n$.

Si $\dim \left( E_{\lambda} \right) = d_{\lambda} < n$.

Soit $ \left( e_{1},\ldots,e_{d_{\lambda}} \right)$ une base de $E_{\lambda}$ et $ \left\lbrace e_{d_{\lambda} + 1},\ldots,e_{n} \right\rbrace$ qui la complètent en une base de $E$.

Soit $f \in \mathcal{L}(E)$ telle que $A = Mat_{\mathcal{B}_{c}}(f)$ et 

$\mathcal{B =} \left\lbrace e_{1},\ldots,e_{d_{\lambda}},e_{d_{\lambda} + 1},\ldots,e_{n} \right\rbrace$

$$B = Mat_{\mathcal{B}}(f) = \begin{bmatrix}
\lambda & 0 & \cdots & 0 \\
0 & \lambda & 0 & \vdots \\
 \vdots & 0 & \ddots & 0 \\
0 & 0 & 0 & \lambda \\
 \vdots & \vdots & 0 & 0 \\
0 & 0 & \cdots & 0
\end{bmatrix} \left\vert  ? =  \left( f \left( e_{1} \right) \right\vert f \left( e_{2} \right)\ldots f \left( e_{n} \right) \right)$$

Or $f \left( e_{1} \right) = \lambda e_{1},\ \ldots,\ f \left( e_{d_{\lambda}} \right) = \lambda e_{d_{\lambda}}$

$$P_{A}(X) = P_{B}(X) = \det \left( B - XI_{n} \right) =  \left\vert  \begin{matrix}
\lambda - X & 0 & \cdots & 0 \\
0 & \lambda - X & 0 & \vdots \\
 \vdots & 0 & \ddots & 0 \\
0 & 0 & 0 & \lambda - X \\
 \vdots & \vdots & 0 & 0 \\
0 & 0 & \cdots & 0
\end{matrix}\ \vert \begin{matrix}
\  \\
M \\
\  \\
\_\_ \\
\  \\
N
\end{matrix} \right\vert  = (\lambda - X)^{d_{\lambda}}\det(N)$$

D'où $m_{\lambda} \geq d_{\lambda}$

**Remarque :**

Pour calculer $\dim \left( E_{\lambda} \right)$, on peut aussi utiliser le théorème du rang.

$$E_{\lambda} = \ker \left( f - I_{d} \right)$$

$$\dim \left( {Im} \left( f - \lambda I_{d} \right) \right) + \dim \left( E_{\lambda} \right) = n$$

$$rg \left( f - \lambda I_{d} \right) + \dim \left( E_{\lambda} \right) = n$$

$$\dim \left( E_{\lambda} \right) = n - rg \left( f - \lambda I_{d} \right)$$

**Remarque :**

Pour déterminer $E_{\lambda}$, on résout $AX = \lambda X$

**Corollaire :**

Si $\lambda$ est de multiplicité 1, alors $\dim \left( E_{\lambda} \right) = 1$

## IV. Diagonalisation

<!-- -->

### 1.  Diagonalisation

**Définition :**

Soit $f \in \mathcal{L}(E)$. $f$ est diagonalisable s'il existe une base de $E$ formée de vecteurs propres.

**Exemple :**

Soit $f:\mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$, $(x,y) \rightarrow  \left( x - \frac{y}{2}, - \frac{x}{2} + y \right)$. Diagonaliser $f$.

$$Sp(f) =  \left\lbrace \frac{1}{2};\frac{3}{2} \right\rbrace$$

$$v_{1} = \begin{pmatrix} 1 \\ 
1 \end{pmatrix}$$ 

est vecteur propre de $\frac{1}{2}$

$$v_{2} = \begin{pmatrix} 1 \\ 
\ - 1 \end{pmatrix}$$

est vecteur propre de $\frac{3}{2}$.

$\mathcal{B} \left( v_{1},v_{2} \right)$ est une base de vecteurs propres de $\mathbb{R}_{2}$. Alors $f$ est diagonalisable.

**Proposition :**

Soit $f \in \mathcal{L}(E)$. $f$ est diagonalisable si et seulement s'il existe une base $\mathcal{B}$ de $E$ telle que $Mat_{\mathcal{B}}(f)$ est diagonale.

**Démonstration :**

$f$ est diagonalisable $\Leftrightarrow$ il existe une base
$\mathcal{B}$ de $E$ formée de vecteurs propres :
$\left\lbrace  e_{1},\ldots,e_{n} \right\rbrace $.

$$Mat_{\mathcal{B}}(f) = \left( f\left( e_{1} \right)\ldots f\left( e_{n} \right) \right)$$

Or $f\left( e_{1} \right) = \lambda_{1}e_{1}$, ...
$f\left( e_{n} \right) = \lambda_{n}e_{n}$

$$Mat_{\mathcal{B}}(f) = diag\left( \lambda_{1},\ldots,\lambda_{n} \right)$$

### 2.  Diagonalisation de matrices

**Définition :**

Soit $A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$.

$A$ est diagonalisable s'il existe une base de vecteurs propres.

$A$ est diagonalisable si elle est semblable à une matrice diagonale.

$A$ diagonalisable $\Leftrightarrow \exists D$ diagonale,
$P \in \mathcal{M}_{n}\left( \mathbb{K} \right)$ inversible telle que
$A = PDP^{- 1}$

**Théorème :**

Si $A$ admet $n$ valeurs propres distinctes, alors $A$ est
diagonalisable.

**Démonstration :**

$A$ admet $n$ valeurs propres distinctes
$\lambda_{1},\ldots,\lambda_{n}$.

Donc soit $v_{1},\ldots,v_{n}$ des vecteurs propres associés.

Les sous-espaces propres sont en somme directe, donc la famille
$\left( v_{1},\ldots,v_{n} \right)$ forme une base de $\mathbb{R}^{n}$
de vecteurs propres.

**Exemple :**

Soit 
$$A = \begin{pmatrix}
a_{11} & \ldots & a_{1n} \\
\  & \ddots & \  \\
0 & \ldots & a_{nn}
\end{pmatrix}$$

$$P_{A}(\lambda) = \det\left( A - \lambda I_{n} \right) = \left\vert  \begin{matrix}
a_{11} - \lambda & \ldots & a_{1n} \\
\  & \ddots & \  \\
0 & \ldots & a_{nn} - \lambda
\end{matrix} \right\vert  = \prod_{i = 1}^{n}\left( a_{ii} - \lambda \right)$$

Si les $a_{ii}$ sont tous deux à deux distincts alors $A$ est
diagonalisable.

$$A = \begin{pmatrix}
3 & 1 \\ - 2 & 0
\end{pmatrix}$$

$$P_{A}(\lambda) = \lambda^{2} - 3\lambda + 2 = (\lambda - 1)(\lambda - 2)$$

Donc deux valeurs propres distinctes, donc $A$ est diagonalisable.

**Trouvons les vecteurs propres :**

Soit 
$$v_{1} = \begin{pmatrix}
x \\
y
\end{pmatrix}$$ 
tels que $Av_{1} = v_{1}$

$$\Leftrightarrow \begin{pmatrix}
3x + y \\ - 2x
\end{pmatrix} = \begin{pmatrix}
x \\
y
\end{pmatrix} \Leftrightarrow \left\lbrace  \begin{array}{r}
2x = - y \\ - 2x = y
\end{array} \right.  \Leftrightarrow v_{1} = \begin{pmatrix}
1 \\ - 2
\end{pmatrix}$$

$$v_{2} = \begin{pmatrix}
1 \\ - 1
\end{pmatrix}$$ 
est vecteur propre pour la valeur propre 2

$$P = \begin{pmatrix}
1 & 1 \\ - 2 & - 1
\end{pmatrix}$$

$$A = PDP^{- 1}$$

$$D = Mat_{\mathcal{B}_{p}}f = \left( \left( f\left( v_{1} \right) \right)_{\mathcal{B}_{p}}\left( f\left( v_{2} \right) \right)_{\mathcal{B}_{p}} \right),\ f\left( v_{1} \right) = v_{1},\ f\left( v_{2} \right) = 2v_{2}$$

$$D = \begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}$$

**Remarque :**

L'ordre des colonnes de $P$ est très important, il indique l'ordre des
vecteurs de la base.

Si on a $$Q = \begin{pmatrix}
1 & 1 \\ - 1 & - 2
\end{pmatrix}$$, alors $$A = Q\begin{pmatrix}
2 & 0 \\
0 & 1
\end{pmatrix}Q^{- 1}$$

**Théorème :**

$A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$ est diagonalisable si
et seulement si la somme des dimensions des espaces propres vaut $n$.

**Démonstration :**

Si $\lambda_{1},\ldots,\lambda_{l}$ sont les valeurs propres de $A$,
alors
$E_{\lambda_{1}} \oplus \ldots \oplus E_{\lambda_{l}} \subset \mathbb{K}^{n}$

Si
$\dim\left( E_{\lambda_{1}} \oplus \ldots \oplus E_{\lambda_{l}} \right) = \dim\left( E_{\lambda_{1}} \right) + \ldots + \dim\left( E_{\lambda_{l}} \right) = n$,
alors
$E_{\lambda_{1}} \oplus \ldots \oplus E_{\lambda_{l}} = \mathbb{K}^{n}$

On prend
$$\mathcal{B}_{v_{p}}\left( v_{1},\ldots,v_{k_{1}},v_{k_{1} + 1},\ldots,v_{k_{2}},v_{k_{2} + 1},\ldots,v_{k_{l}} \right)$$

base de $E_{\lambda_{1}} \oplus \ldots \oplus E_{\lambda_{l}}$

Alors $$\mathcal{B}_{v_{p}}$$ 

est une base de vecteurs propre et $A$ est diagonale dans cette base.

**Théorème :**

$$A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$$

est diagonalisable si et seulement si

$$E_{\lambda_{1}} + \ldots + E_{\lambda_{n}} = \mathbb{K}^{n}$$

**Preuve :**

Idem

**Théorème :**

$A$ est diagonalisable si et seulement si :

-   $P_{A}$ est scindé

-   $\forall\lambda \in S_{p}(A),\dim\left( E_{\lambda} \right) = m_{\lambda}$

**Preuve :**

$$P_{A}(\lambda) = \prod_{\lambda \in Sp(A)}^{}(X - \lambda)^{m_{\lambda}}$$

**Remarque :**

$$n = \deg\left( P_{A} \right) = \sum_{\lambda \in Sp(A)}^{}m_{\lambda}$$

**Rappel :**

$$1 \leq \dim\left( E_{\lambda} \right) \leq m_{\lambda}$$

$$\dim\left( E_{\lambda_{1}} \oplus \ldots \oplus E_{\lambda_{l}} \right) = \dim\left( E_{\lambda_{1}} \right) + \ldots + \dim\left( E_{\lambda_{l}} \right)$$

$A$ diagonalisable
$\Leftrightarrow \dim\left( E_{\lambda_{1}} \right) + + \ldots + \dim\left( E_{\lambda_{l}} \right) = n$

$$\Leftrightarrow \dim\left( E_{\lambda} \right) = m_{\lambda}\forall\lambda \in Sp(A)$$

**Méthode : Diagonaliser :**

1.  Calculer $P_{A}$ (non scindé $\rightarrow$ non diagonalisable)

2.  Trouver les racines de $P_{A}\ $: trouver $Sp(A)$

3.  Trouver les bases des $E_{\lambda}$

4.  Si
    $\dim\left( E_{\lambda} \right) = m_{\lambda}\ \forall\lambda \in Sp(A)$
    alors diagonalisable, sinon non

<!-- -->

## V.  Trigonalisation

<!-- -->

### 1.  Introduction

Une matrice 
$$A = \begin{pmatrix}
a_{11} & \  & a_{1n} \\
\  & \ddots & \  \\
0 & \  & a_{nn}
\end{pmatrix}$$ 
est dite triangulaire supérieure.

**Proposition :**

Toute matrice triangulaire supérieure est semblable à une matrice
inférieure.

**Preuve :**

$$ P = \begin{pmatrix}
0 & \  & 1 \\
\  & / & \  \\
1 & \  & 0 
\end{pmatrix}$$ 
est une matrice inversible.

Alors $$A = P\begin{pmatrix}
a_{nn} & \  & 0 \\
\  & \ddots & \  \\
a_{1n} & \  & a_{11}
\end{pmatrix}P^{- 1}$$

Soit $\left( e_{1},\ldots,e_{n} \right)$ la base canonique et
$\mathcal{B}^{'} = \left( e_{n},\ldots,e_{1} \right) = \left( \varepsilon_{1},..,\varepsilon_{n} \right)$
la nouvelle base.

**Remarque :**

$P$ est la matrice de passage de $\mathcal{B}$ à $\mathcal{B}^{'}$

Si

$$A = Mat_{\mathcal{B}_{c}}(f),\ f\left( e_{1} \right) = a_{11}e_{1},\ f\left( e_{2} \right) = a_{12}e_{1} + a_{22}e_{2}$$

$$f\left( \varepsilon_{1} \right) = a_{1n}e_{1} + \ldots + a_{nn}e_{n} = a_{1n}\varepsilon_{n} + \ldots + a_{nn}\varepsilon_{1}$$

$$f\left( \varepsilon_{n} \right) = a_{11}\varepsilon_{n}$$

**Dorénavant, une matrice triangulaire fera référence avec une matrice triangulaire supérieure**

### 2.  Trigonalisation

**Définition :**

Soit $A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$.

$A$ est trigonalisable si elle est semblable à une matrice triangulaire
$T$.

Soit $f\mathcal{\in L}(E)$

$f$ est trigonalisable s'il existe une base $\mathcal{B}$ telle que
$Mat_{\mathcal{B}}(f)$ est triangulaire.

**Remarque :**

Diagonalisable $\Rightarrow$ Trigonalisable

**Théorème :**

$A$ est trigonalisable si et seulement si $P_{A}$ est scindé.

$f$ est trigonalisable si et seulement si $P_{f}$ est scindé.

**Démonstration**

Par récurrence sur $\dim(E) = n$

$H_{n}:$ « $f\mathcal{\in L}(E)$ telle que $\dim(E) = n$ : $P_{f}$
scindé $\Rightarrow$ $f$ est trigonalisable »

$$n = 1:$$

Soit $\mathcal{B}_{c}$ 

la base canonique de $\mathbb{K}$,


$Mat_{\mathcal{B}_{c}}f = (a)$

$P_{f}(\lambda) = a - \lambda$ et $P_{f}$ est scindé.

**Remarque :**

$Mat_{\mathcal{B}_{c}}(f)$ 

est diagonalisable donc trigonalisable donc
$H_{1}$ est vraie.

**Hérédité :**

On suppose $H_{n}$, montrons $H_{n + 1}$

Soit $E$ tel que $\dim(E) = n + 1$, $f\mathcal{\in L}(E)$ tel que
$P_{f}$ est scindé.

$$P_{f}(X) = \prod_{\lambda \in Sp(f)}^{}(X - \lambda)^{m_{\lambda}}$$

Donc $P_{f}$ admet au moins une racine $\lambda \in Sp(f)$, sont $v_{1}$
un vecteur propre associé.

Soit $\mathcal{B =}\left( v_{1},\ldots,v_{n + 1} \right)$ une base de
$E$.

$$E = {Vect}\left( v_{1} \right) \oplus {Vect}\left( v_{2},\ldots,v_{n + 1} \right)$$

$$Mat_{\mathcal{B}}(f) = \begin{pmatrix}
\lambda & * & * & * \\
0 & \  & \  & \  \\
 \vdots & \  & B & \  \\
0 & \  & \  & \ 
\end{pmatrix}$$

$$P_{f}(X) = \left\vert  \begin{matrix}
\lambda - X & * & * & * \\
0 & \  & \  & \  \\
 \vdots & \  & B - XI_{n} & \  \\
0 & \  & \  & \ 
\end{matrix} \right\vert  = (\lambda - X)\det\left( B - XI_{n} \right) = (\lambda - X)P_{B}(X)$$

$P_{f}$ est scindé donc $P_{B}$ aussi.

$B \in \mathcal{M}_{n}\left( \mathbb{K} \right)$ 

et $P_{B}$ est scindé.

D'après $H_{n}$, $B$ est trigonalisable.

Soit $P$ inversible telle que $PBP^{- 1} = T$ triangulaire et
$$P^{'} = \begin{pmatrix}
1 & 0 & \ldots & 0 \\
0 & \  & \  & \  \\
 \vdots & \  & P & \  \\
0 & \  & \  & \ 
\end{pmatrix} \in GL_{n + 1}\left( \mathbb{K} \right)$$

Alors :

$$P^{'}AP^{' - 1} = \begin{pmatrix}
\lambda & * & * & * \\
0 & \  & \  & \  \\
 \vdots & \  & PBP^{- 1} & \  \\
0 & \  & \  & \ 
\end{pmatrix} = \begin{pmatrix}
\lambda & * & * & * \\
0 & \  & \  & \  \\
 \vdots & \  & T & \  \\
0 & \  & \  & \ 
\end{pmatrix}$$ 
triangulaire.

D'où $f$ trigonalisable.

On a montré par récurrence que $P_{f}$ scindé $\Rightarrow f$
trigonalisable.

Pour montrer la réciproque, si $f$ est trigonalisable, il existe une
base $\mathcal{B}$ telle que $$Mat_{\mathcal{B}}(f) = \begin{pmatrix}
a_{11} & \  & a_{1n} \\
\  & \ddots & \  \\
0 & \  & a_{nn}
\end{pmatrix}$$

D'où $P_{f}(X) = \prod_{i = 1}^{n}\left( a_{ii} - X \right)$ scindé.

**Remarque :**

Si $A$ est trigonalisable, alors les valeurs de la diagonale de la
matrice triangulaire correspondante sont les valeurs propres de $A$
comptées avec multiplicité. Si $$A = P\begin{pmatrix}
\lambda_{1} & \  & * \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}
\end{pmatrix}P^{- 1}$$

$$P_{A}(X) = P_{\begin{pmatrix}
\lambda_{1} & \  & * \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}
\end{pmatrix}}(X) = \left\vert  \begin{matrix}
\lambda_{1} & \  & * \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}
\end{matrix} \right\vert  = \prod_{i = 1}^{n}\left( \lambda_{i} - X \right)$$

**Corollaire :**

Dans $\mathcal{M}_{n}\left( \mathbb{C} \right)$, toutes les matrices
sont trigonalisables.

**Démonstration :** Dans $\mathbb{C}\lbrack X\rbrack$, tous
les polynômes sont scindés.

**Classification des matrices trigonalisables de**
$\mathcal{M}_{3}\left( \mathbb{C} \right)$

Si $A = \mathcal{M}_{3}\left( \mathbb{C} \right)$, 3 cas de figure
possibles.

-   Si
    $P_{A}(X) = \left( X - \lambda_{1} \right)\left( X - \lambda_{2} \right)\left( X - \lambda_{3} \right)$
    où $\lambda_{1},\lambda_{2},\lambda_{3}$ sont distinctes, alors :

$$A = P\begin{pmatrix}
\lambda_{1} & \  & 0 \\
\  & \lambda_{2} & \  \\
0 & \  & \lambda_{3}
\end{pmatrix}P^{- 1}$$

-   Si
    $P_{A}(X) = \left( X - \lambda_{2} \right)^{2}\left( X - \lambda_{1} \right)$

<!-- -->

-   Si $\dim\left( E_{\lambda_{2}} \right) = 2$, alors
    $$A = P\begin{pmatrix}
    \lambda_{1} & \  & 0 \\
    \  & \lambda_{2} & \  \\
    0 & \  & \lambda_{2}
    \end{pmatrix}P^{- 1}$$

-   Si $\dim\left( E_{\lambda_{2}} \right) = 1$

$$A = P\begin{pmatrix}
\lambda_{1} & 0 & * \\
0 & \lambda_{2} & * \\
0 & 0 & \lambda_{2}
\end{pmatrix}P^{- 1}$$

Soit $v_{1}$ vecteur propre de $\lambda_{1}$, $v_{2}$ vecteur propre de
$\lambda_{2}$, $$P = \begin{pmatrix}
v_{1} & v_{2} & ?
\end{pmatrix}$$

-   Si $P_{A}(X) = (X - \lambda)^{3}$

<!-- -->

-   Si
    $\dim\left( E_{\lambda} \right) = 3,\ E_{\lambda} = \mathbb{R}^{3}$

$$A = \lambda I_{3}$$

Si une matrice n'est pas diagonale mais admet une valeur propre triple,
alors elle n'est pas diagonalisable.

-   Si $\dim\left( E_{\lambda} \right) = 2$

$$A = P\begin{pmatrix}
\lambda & 0 & a \\
0 & \lambda & b \\
0 & 0 & \lambda
\end{pmatrix}P^{- 1}$$ 
avec $(a,b) \neq (0,0)$

Soit $\left( v_{1},v_{2} \right)$ base de $E_{\lambda}$.
$P = (\begin{matrix}
v_{1} & v_{2} & ?
\end{matrix})$

-   Si $\dim\left( E_{\lambda} \right) = 1$

$$A = P\begin{pmatrix}
\lambda & a & b \\
0 & \lambda & c \\
0 & 0 & \lambda
\end{pmatrix}P^{- 1}$$ 
avec $a \neq 0$ et $(b,c) \neq (0,0)$

Soit $v_{1}$ un vecteur propre.

$$P = \begin{pmatrix}
v_{1} & ? & ?
\end{pmatrix}$$

**Résumé :**

$P_{A}$ scindé $\Rightarrow$ $A$ trigonalisable.

$\mathbb{K = C \Rightarrow}A$ trigonalisable.

# Chapitre 2 : Application de la diagonalisation et de la trigonalisation

**Définition :**

Soit $A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$,
$k \in \mathbb{N}$.

$A^{k} = A \times \ldots \times A\ $($k$ fois)

Si $A \in GL_{n}\left( \mathbb{K} \right)$ (matrices inversibles).

$$\forall k \in \mathbb{N,\ }A^{- k} = \left( A^{- 1} \right)^{k}$$

**Remarque :**

Si $A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}$, $A^{2} \neq \begin{pmatrix}
a^{2} & b^{2} \\
c^{2} & d^{2}
\end{pmatrix}$ en général.

On peut trouver des matrices nilpotentes : $\exists k,\ A^{k} = 0_{n}$


avec $A \neq 0_{n}$

Exemple :

$$A = \begin{pmatrix}
1 & - 1 \\
1 & - 1 
\end{pmatrix}$$

alors $$A^{2} = \begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}$$

**Proposition :**

Si $A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$ et $\lambda$ valeur
propre de $A$.

-   $\forall k \in \mathbb{N,\ }\lambda^{k}$ est valeur propre de
    $A^{k}$

-   Si $A \in GL_{n}\left( \mathbb{K} \right)$,
    $\forall k \in \mathbb{Z}$, $\lambda^{k}$ est valeur propre de
    $A^{k}$

**Preuve :** Voir TD

**Proposition :**

$\forall k,i \in \mathbb{N}$ et
$\forall A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$

$$A^{i}A^{k} = A^{i + k},\ \left( A^{i} \right)^{k} = A^{ik}$$

**Proposition :**

Soit 
$$D = \begin{pmatrix}
\lambda_{1} & \  & 0 \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}
\end{pmatrix},\ T = \begin{pmatrix}
\lambda_{1} & \  & * \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}
\end{pmatrix}$$

Alors :

$$D^{k} = \begin{pmatrix}
\lambda_{1}^{k} & \  & 0 \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}^{k}
\end{pmatrix},\ T^{k} = \begin{pmatrix}
\lambda_{1}^{k} & \  & \# \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}^{k}
\end{pmatrix}$$

**Preuve :** Produit matriciel.

## I.  Formule du binôme

<!-- -->

### 1.  Formule du binôme

**Définition :**

Soit $A \in \mathcal{M}_{n}\left( \mathbb{K} \right)$. $A$ est
nilpotente d'ordre $p \in \mathbb{N}$ si et seulement si :

$A^{p} = (0)$ et $A^{p - 1} \neq 0$

**Remarque :**

$$\begin{pmatrix}
0 & 1 \\
0 & 0
\end{pmatrix}$$ 
est nilpotente d'ordre 2.

$$\begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{pmatrix}$$ 
est nilpotente d'ordre 3.

**Exercice :**

Montrer que $$\begin{pmatrix}
0 & 1 \\
0 & 0
\end{pmatrix} $$ est nilpotente d'ordre 2.

Montrer que $$\begin{pmatrix}
0 & a & c \\
0 & 0 & b \\
0 & 0 & 0
\end{pmatrix}$$ est nilpotente d'ordre 3.

Montrer que $$\begin{pmatrix}
0 & 0 & a \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}$$ est nilpotente d'ordre 3.

$$\begin{pmatrix}
0 & a & c \\
0 & 0 & b \\
0 & 0 & 0
\end{pmatrix}^{2} = \begin{pmatrix}
0 & 0 & ab \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}$$

**Remarque :**

Toute matrice triangulaire supérieure stricte est nilpotente.

**Théorème :**

Soient $A$ et $B$ $\in \mathcal{M}_{n}\left( \mathbb{K} \right)$ telles
que $AB = BA$

$$(A + B)^{k} = \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i}B^{i}}$$

**Rappel :** $\left( \begin{array}{r}
k \\
i
\end{array} \right) = \frac{k\ !}{i\ !(k - i)\ !}$

On peut les retrouver avec le triangle de Pascal.

**Démonstration :** Par récurrence

Initialisation pour $k = 1\ $: trivial

$$\text{Supposons que}\ (A + B)^{k} = \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i}B^{i}}$$

$$(A + B)^{k + 1} = (A + B)(A + B)^{k}$$

$$(A + B)^{k + 1} = (A + B)\left( \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i}B^{i}} \right)$$

$$(A + B)^{k + 1} = \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i + 1}B^{i}} + \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)BA^{k - i}B^{i}}$$

Or $AB = BA$

$$(A + B)^{k + 1} = \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i + 1}B^{i}} + \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i}B^{i + 1}}$$

$$(A + B)^{k + 1} = \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i + 1}B^{i}} + \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i}B^{i + 1}}$$

$$(A + B)^{k + 1} = \sum_{i = 0}^{k}{\left( \begin{array}{r}
k \\
i
\end{array} \right)A^{k - i + 1}B^{i}} + \sum_{j = 1}^{k + 1}{\left( \begin{array}{r}
k \\
j - 1
\end{array} \right)A^{k - j + 1}B^{j}}$$

$$(A + B)^{k + 1} = \sum_{j = 0}^{k + 1}{\left\lbrack \left( \begin{array}{r}
k \\
j
\end{array} \right) + \left( \begin{array}{r}
k \\
j + 1
\end{array} \right) \right\rbrack A^{k - j + 1}B^{j}}$$

$$(A + B)^{k + 1} = \sum_{j = 0}^{k + 1}{\left( \begin{array}{r}
k + 1 \\
j
\end{array} \right)A^{k - j + 1}B^{j}}$$

Ce qui prouve l'hérédité.

**Attention :** La formule est fausse si $A$ et $B$ ne
commutent pas

**Remarque :**

En pratique, si $T$ est triangulaire supérieure, alors $T = D + N$, avec
$D$ diagonale et $N$ triangulaire supérieure stricte donc nilpotente et
$DN = ND$

**Exemple :**

$$A = \begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} + \begin{pmatrix}
0 & 2 \\
0 & 0
\end{pmatrix}$$

$$D^{n} = D\ \forall n \in \mathbb{N}$$

$$N^{n} = 0\ \forall n > 1$$

$$A^{n} = (D + N)^{n} = \sum_{k = 0}^{n}{\left( \begin{array}{r}
n \\
k
\end{array} \right)D^{n - k}N^{k}} = D^{n} + \left( \begin{array}{r}
n \\
1
\end{array} \right)D^{n - 1}N = \begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} + n\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}\begin{pmatrix}
0 & 2 \\
0 & 0
\end{pmatrix}$$

$$A^{n} = \begin{pmatrix}
1 & 2n \\
0 & 1
\end{pmatrix}$$

**Exemple :**

$$T = \begin{pmatrix} - 1 & 0 & 0 \\
0 & 3 & 1 \\
0 & 0 & 3
\end{pmatrix} = \begin{pmatrix} - 1 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 3
\end{pmatrix} + \begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{pmatrix}$$

### 2.  Puissance de matrices semblables


**Proposition :**

Si $A = PBP^{- 1}$

Alors :

$$A^{k} = PB^{k}P^{- 1}$$

**Démonstration :**

$$A^{2} = PBP^{- 1}PBP^{- 1} = PBIBP^{- 1} = PB^{2}P^{- 1}$$

Etc.

**Proposition :**

Si $A$ est diagonalisable : $A^{k} = PD^{k}P^{- 1}$

## VI. Suites récurrentes

**Rappel :** Soit $\left( u_{n} \right)_{n\mathbb{\in N}}$ une
suite définie par :

$$\left\lbrack  \begin{array}{r}
u_{0} \\
u_{n + 1} = au_{n} + b
\end{array} \right. $$

-   Si $a = 1$, alors $\forall n\mathbb{\in N}$, $u_{n} = u_{0} + nb$

(diverge si $b \neq 0$, $u_{n} = u_{0}$ sinon)

-   Sinon, si $u_{n}$ converge, alors $u_{n}$ converge vers une solution
    de $u = au + b \Leftrightarrow u = \frac{b}{1 - a}$

$$\forall n\mathbb{\in N,\ }u_{n} = a^{n}\left( u_{0} - u \right) + u$$

Converge vers $u$ si et seulement si $\vert a\vert  < 1$ et $u_{0} \neq u$

### 1.  Suites récurrentes linéaires du premier ordre

Soit $A = \mathcal{M}_{k}\left( \mathbb{R} \right)$ et
$B \in \mathbb{R}^{k}$

Soit $\left( X_{n} \right)_{n\mathbb{\in N}}$ une suite.

$\forall n\mathbb{\in N,\ }X_{n} \in \mathbb{R}^{k}$ et :

$$\left\lbrack  \begin{array}{r}
X_{0} \\
X_{n + 1} = AX_{n} + B
\end{array} \right. $$

**Proposition :**

Si $\left( X_{n} \right)_{n\mathbb{\in N}}$ converge, alors elle
converge vers une solution de $X = AX + B$.

**Preuve :** Si $X_{n}$ converge, alors
$\lim_{n \rightarrow + \infty}X_{n} = \lim_{n \rightarrow + \infty}X_{n + 1}$

En prenant la relation de récurrence à la limite, on obtient la
relation.

**Proposition :**

1\.

Si $I_{k} - A$ est inversible, alors
$\forall B \in \mathbb{R}^{k},\ \exists\ !X \in \mathbb{R}^{k}$ solution
de $X = AX + B$

2\.

Si $I_{k} - A$ n'est pas inversible, soit il n'existe pas de solution,
soit il en existe une infinité.

**Preuve :**

1.  Si $I_{k} - A$ est inversible,
    $X = AX + B \Leftrightarrow \left( I_{k} - A \right)X = B \Leftrightarrow X = \left( I_{k} - A \right)^{- 1}B$

2.  Supposons qu'il existe $X_{1}$ solution, tel que
    $X_{1} = AX_{1} + B$, donc il y en a une infinité.

$$\dim\left( \ker\left( I_{k} - A \right) \right) \geq 1$$

$\forall Y \in \ker\left( I_{k} - A \right),\ \left( I_{k} - A \right)X_{1} = B$
et
$\left( I_{k} - A \right)\left( X_{1} + Y \right) = \left( I_{k} - A \right)X_{1} = B$

Donc si $X_{1}$ est solution alors il y a une infinité de solutions.

**Exercice :**

Soient
$$\left( u_{n} \right)_{n\mathbb{\in N}},\ \left( v_{n} \right)_{n\mathbb{\in N}},\ \left( w_{n} \right)_{n\mathbb{\in N}}$$
trois suites réelles définies par :

$$u_{0} = 0,\ v_{0} = 22,\ w_{0} = 22$$

$$\forall n\mathbb{\in N,}\left\lbrack  \begin{array}{r}
u_{n + 1} = \frac{1}{4}\left( 2u_{n} + v_{n} + w_{n} \right) \\
v_{n + 1} = \frac{1}{3}\left( u_{n} + v_{n} + w_{n} \right) \\
w_{n + 1} = \frac{1}{4}\left( u_{n} + v_{n} + 2w_{n} \right)
\end{array} \right. \ (S)$$

On pose $\forall n\mathbb{\in N,\ }X_{n} = \begin{pmatrix}
u_{n} \\
v_{n} \\
w_{n}
\end{pmatrix}$

$$(S) \Leftrightarrow X_{n + 1} = \begin{pmatrix}
\frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\
\frac{1}{3} & \frac{1}{3} & \frac{1}{3} \\
\frac{1}{4} & \frac{1}{4} & \frac{1}{2}
\end{pmatrix}X_{n} = AX_{n}$$

$$\forall n\mathbb{\in N,\ }X_{n} = A^{n}X_{0}$$

« Connaitre le terme général de
$\left( u_{n} \right),\ \left( v_{n} \right),\ \left( w_{n} \right)$
$\Leftrightarrow$ savoir calculer le terme général de $A^{n}$ ».

$$P_{A}(X) = \left\vert  \begin{matrix}
\frac{1}{2} - X & \frac{1}{4} & \frac{1}{4} \\
\frac{1}{3} & \frac{1}{3} - X & \frac{1}{3} \\
\frac{1}{4} & \frac{1}{4} & \frac{1}{2} - X
\end{matrix} \right\vert  =_{C_{1} \leftarrow C_{1} - C_{3}}\left\vert  \begin{matrix}
\frac{1}{4} - X & \frac{1}{4} & \frac{1}{4} \\
0 & \frac{1}{3} - X & \frac{1}{3} \\
 - \frac{1}{4} + X & \frac{1}{4} & \frac{1}{2} - X
\end{matrix} \right\vert  = \left( \frac{1}{4} - X \right)\left\vert  \begin{matrix}
1 & \frac{1}{4} & \frac{1}{4} \\
0 & \frac{1}{3} - X & \frac{1}{3} \\
 - 1 & \frac{1}{4} & \frac{1}{2} - X
\end{matrix} \right\vert  =_{L_{3} \leftarrow L_{3} + 1}\left( \frac{1}{4} - X \right)\left\vert  \begin{matrix}
1 & \frac{1}{4} & \frac{1}{4} \\
0 & \frac{1}{3} - X & \frac{1}{3} \\
0 & \frac{1}{2} & \frac{3}{4} - X
\end{matrix} \right\vert  = \left( \frac{1}{4} - X \right)\left\vert  \begin{matrix}
\frac{1}{3} - X\  & \frac{1}{3} \\
\frac{1}{2} & \frac{3}{4} - X
\end{matrix} \right\vert  = \left( \frac{1}{4} - X \right)\left( \left( \frac{1}{3} - X \right)\left( \frac{3}{4} - X \right) - \frac{1}{6} \right) = \ldots = \left( \frac{1}{4} - X \right)\left( \frac{1}{12} - X \right)(1 - X)$$

$A$ est diagonalisable. $\exists P,\ A = P\begin{pmatrix}
1 & 0 & 0 \\
0 & \frac{1}{4} & 0 \\
0 & 0 & \frac{1}{12}
\end{pmatrix}P^{- 1}$

$$A^{n} = P\begin{pmatrix}
1 & 0 & 0 \\
0 & \frac{1}{4^{n}} & 0 \\
0 & 0 & \frac{1}{12^{n}}
\end{pmatrix}P^{- 1}$$

## VII. Equations différentielles linéaires du premier ordre

<!-- -->

### 1.  Equation Homogène

**Définition :** Une équation différentielle du 1^er^ ordre
linéaire homogène est de la forme :

$x^{'}(t) = a(t)x(t)\ (EH)$ avec $a$ continue sur $\mathbb{R}$

**Proposition :**

$S_{H}$ l'ensemble des solutions de $(EH)$ est un espace vectoriel.

**Preuve :** C'est un sous-espace vectoriel des fonctions
définies sur $\mathbb{R}$

$$\forall f,g \in S_{H},\ \forall\lambda,\mu\mathbb{\in R,\ }\lambda f + \mu g \in S_{H}$$

$$(\lambda f + \mu g)^{'} = \lambda f^{'} + \mu g^{'} = \lambda\left( a(t)f(t) \right) + \mu\left( a(t)g(t) \right) = a(t)\left( \lambda f(t) + \mu g(t) \right)$$

**Théorème :**

Soit $A$ une primitive de $a$. Alors
$S_{H} = {Vect}\left( t \rightarrow e^{A(t)} \right)$

**Preuve :**

$$(EH) \Rightarrow \left( x^{'}(t) - a(t)x(t) \right)e^{- A(t)} = 0 \Leftrightarrow \left( x(t)e^{- A(t)} \right)^{'} = 0 \Leftrightarrow x(t)e^{- A(t)} = C\mathbb{\in R}$$

$$x(t) = Ce^{A(t)}$$

Réciproquement $f:t \rightarrow Ce^{A(t)}$ est solution de $(EH)$.

### 2.  Equation non-homogène

**Définition :** C'est une équation différentielle de la forme
$x^{'}(t) = a(t)x(t) + b(t)\ (E)$

**Théorème :**

Soit $S$ l'ensemble de solutions de $(E)$ et
$S = \left\lbrack  f\mathbb{\ :\ R \rightarrow R,\ }t \rightarrow Ce^{A(t)} - f_{p}(t) \right\rbrack $

Où $f_{p}$ est une solution de $(E)$ (dite « particulière ») si elle
existe.

**Démonstration :**

Soit $f_{p}$ solution de $(E)$

Alors soit $x$ solution de $(E)$, posons $y = x - f_{p}$

Alors
$y^{'} = x^{'} - f_{p}^{'} = a(t)x(t) + b(t) = a(t)f_{p}(t) + b(t) = a(t)\left( x(t) - f_{p}(t) \right) = a(t)y(t)$

Finalement $x$ est solution de $(E) \Leftrightarrow y$ est solution de
$(EH)$.

**Méthode de la variation de la constante :**

Pour trouver $f_{p}$, on la cherche sous la forme :

$$f_{p}(t) = C(t)e^{A(t)}$$

$f_{p}$ solution de
$(E) \Leftrightarrow C^{'}(t)e^{A(t)} + a(t)C(t)e^{A(t)} = a(t)C(t)e^{A(t)} + b(t) \Leftrightarrow C^{'}(t) = b(t)e^{- A(t)}$

Trouver $f_{p}$ revient à intégrer $b(t)e^{- A(t)}$

**Théorème de Cauchy-Lipschitz :**

Soit $I\mathbb{\in R}$, intervalle ouvert et
$a,b \in C^{0}\left( I\mathbb{,R} \right)$

$\forall t_{0} \in I,\ \forall x_{0}\mathbb{\in R,}$ il existe une
unique solution à :

$$\left\lbrack  \begin{array}{r}
x^{'}(t) = a(t)x(t) + b(t) \\
x(0) = x_{0}
\end{array} \right. $$

## VIII. Système différentiel linéaire du premier ordre

$$X^{'}(t) = A(t)X(t) + B(t)$$

Auquel on associe une équation homogène :

$$X^{'}(t) = A(t)X(t)\ :(EH)$$

**Théorème :**

1.  L'ensemble des solutions de $EH$ noté $S_{H}$ est un espace
    vectoriel de dimension 1

2.  Les solutions de $(E)$ sont de la forme $X(t) = X_{H}(t) + X_{P}(t)$
    où $X_{H} \in S_{H}$ et $X_{P}$ est une solution particulière de
    $(E)$.

**Preuve :**

1\.

Montrons que si $X_{1}$ et $X_{2}$ sont solutions de $(EH)$ alors
$\lambda X_{1} + X_{2}$ est solution de
$(EH)\ \left( \lambda\mathbb{\in R} \right)HHHhHG$

$S_{H}\left\lbrack  \begin{array}{r}
S_{H} \rightarrow \mathbb{R}^{n} \\
X \rightarrow X\left( t_{0} \right)
\end{array} \right. $ est une application linéaire.

On admet que c'est une bijection (voir Cauchy Lipschitz).

2\.

Soit $X$ une solution de $(E)$ et $X_{P}$ une solution particulière,
alors $X - X_{P}$ est solution de $(EH)$.

**Théorème :** Cauchy-Lipschitz

$$\left\lbrack  \begin{array}{r}
X^{'}(t) = A(t)X(t) + B(t) \\
X\left( t_{0} \right) = X_{0}
\end{array} \right. $$

Admet une unique solution :

$$A \in C^{0}\left( I,\mathcal{M}_{n}\left( \mathbb{R} \right) \right),\ B \in C^{0}\left( I,\mathbb{R}^{n} \right),\ X_{0} \in \mathbb{R}^{n}$$

Preuve : admis

**Cas des coefficients constants :**

$A$ ne dépend pas de $t$.

$$X^{'}(t) = AX(t) + B(t)$$

-   **Si** $A$ **est diagonalisable**

$$A = PDP^{- 1}\ \text{avec}\ \begin{pmatrix}
\lambda_{1} & \  & 0 \\
\  & \ddots & \  \\
0 & \  & \lambda_{n}
\end{pmatrix}$$

$$(E) \Leftrightarrow X^{'}(t) = PDP^{- 1}X(t) + B(t)$$

$$\Leftrightarrow_{P^{- 1} \times}P^{- 1}X^{'}(t) = DP^{- 1}X(t) + P^{- 1}B(t)$$

On pose $Y(t) = P^{- 1}X(t) \Leftrightarrow X(t) = PY(t)$

Alors $Y^{'}(t) = P^{- 1}X^{'}(t)$

$$(E) \Leftrightarrow Y^{'}(t) = DY(t) + P^{- 1}B(t)$$

Posons $P^{- 1}B(t) = B_{2}(t)$

Alors si $Y(t) = \begin{pmatrix}
y_{1}(t) \\
 \vdots \\
y_{n}(t)
\end{pmatrix},\ B_{2}(t) = \begin{pmatrix}
b_{1}(t) \\
 \vdots \\
b_{2}(t)
\end{pmatrix}$

Alors :

$$(E) \Leftrightarrow \left\lbrack  \begin{array}{r}
y_{1}^{'}(t) = \lambda_{1}y_{1}(t) + b_{1}(t) \\
 \vdots \\
y_{n}^{'}(t) = \lambda_{n}y_{n}(t) + b_{n}(t)
\end{array} \right. $$

**Remarque :** Le système en $Y$ est devenu un système de $n$
équations différentielles **indépendantes**.

Les solutions sont de la forme $Y(t) = \begin{pmatrix}
C_{1}e^{\lambda_{1}t} + y_{1,p}(t) \\
 \vdots \\
C_{n}e^{\lambda_{n}t} + y_{n,p}(t)
\end{pmatrix}$ avec $C_{1},\ldots,C_{n}\mathbb{\in R}$ et $y_{i,p}(t)$
solution particulière de $\left( L_{i} \right)$.

Finalement, les solutions sont de la forme : $X(t) = PY(t)$

-   **Si** $A$ **est trigonalisable**

$A = PTP^{- 1}$ avec $$T = \begin{pmatrix} \lambda_{1} & \  & * \\ \  & \ddots & \  \\ 0 & \  & \lambda_{n} \end{pmatrix}$$

$$(E) \Leftrightarrow P^{- 1}X^{'}(t) = TP^{- 1}X(t) + P^{- 1}B(t)$$

On pose $Y(t) = P^{- 1}X(t)$

Le système devient :

$$Y^{'}(t) = TY(t) + P^{- 1}B(t)$$

Si $Y(t) = \begin{pmatrix}
y_{1}(t) \\
 \vdots \\
y_{n}(t)
\end{pmatrix}$

$$\left\lbrack  \begin{array}{r}
y_{1}^{'}(t) = \lambda_{1}y_{1}(t) + *y_{2}(t) + \ldots + *y_{n}(t) + b_{1}(t) \\
y_{2}^{'}(t) = \lambda_{2}y_{2}(t) + *y_{3}(t) + \ldots + *y_{n}(t) + b_{1}(t) \\
 \vdots \\
y_{n}^{'}(t) = \lambda_{n}y_{n}(t) + b_{n}(t)
\end{array} \right. $$

**Remarque :**

$\left( L_{n} \right)$ est indépendante des autres $y_{i}\ (i \neq n)$
donc on « peut » la résoudre.

$$\left( L_{n - 1} \right):y_{n - 1}^{'}(t) = \lambda_{n - 1}y_{n - 1}(t) + *y_{n}(t) + b_{n - 1}(t)$$

En injectant la forme générale de la solution trouvée pour $y_{n}$, on
« peut » résoudre $\left( L_{n - 1} \right)$

Et ainsi de suite.

On résout le système de façon rétrograde.

**Exemple :**

$$\left\lbrack  \begin{array}{r}
x_{1}^{'}(t) = 2x_{1}(t) + x_{2}(t) \\
x_{2}^{'}(t) = - x_{2}(t)
\end{array} \right. $$

$$\Leftrightarrow X^{'}(t) = \begin{pmatrix}
2 & 1 \\
0 & - 1
\end{pmatrix}X(t)$$

L'ensemble des solutions de $\left( L_{2} \right)$ est
$\left\lbrack  C_{2}e^{- t},\ C_{2}\mathbb{\in R} \right\rbrack $

$\left( L_{1} \right)$ devient $x_{1}^{'}(t) = 2x_{1}(t) + C_{2}e^{- t}$

$\left( L_{1}H \right):x_{1}^{'}(t) = 2x_{1}(t)$ a pour ensemble de
solutions $\left\lbrack  C_{1}e^{2t},\ C_{1}\mathbb{\in R} \right\rbrack $

On peut chercher une solution particulière de $L_{1}$ sous la forme
$\alpha e^{- t} + \beta e^{t}$

$$- \alpha e^{- t} + \beta e^{t} = 2\alpha e^{- t} + 2\beta e^{t} + C_{2}e^{- t}$$

# Chapitre 3 : Forme bilinéaire

**Rappel :**

Soit $\left( v_{1},\ldots,v_{n} \right)$ une famille de $n$ vecteurs.

On peut définir
$$\det\left( v_{1},\ldots,v_{n} \right) = \det\left( Mat_{\mathcal{B}_{c}}\begin{pmatrix}
v_{1} & \ldots & v_{n}
\end{pmatrix} \right)$$

Dans ce cas :

$\det\  = \left\lbrack  \begin{array}{r}
E^{n}\mathbb{\rightarrow R} \\
\left( v_{1},\ldots,v_{n} \right) \rightarrow \det\left( v_{1},\ \ldots,\ v_{n} \right)
\end{array} \right. $ est $n$-linéaire.

C'est-à-dire :
$\det\left( \lambda v_{1} + w,v_{2},\ldots,v_{n} \right) = \lambda\det\left( v_{1},v_{2},\ldots,v_{n} \right) + \det\left( w,v_{2},\ldots,v_{n} \right)$

Ou encore :
$\det\left( v_{1},\lambda v_{2} + v,v_{3},\ldots,v_{n} \right) = \lambda\det\left( v_{1},v_{2},\ldots,v_{n} \right) + \det\left( v_{1},w,\ v_{3},\ldots,v_{n} \right)$

On a :

$$\det\left( v_{1},\ldots,v_{i},\ldots,v_{j},\ldots,v_{n} \right) = - \det\left( v_{1},\ldots,v_{j},\ldots,v_{i},\ldots,v_{n} \right)$$

## I.  Forme bilinéaire

**Définition :**

Soit $E$ un $\mathbb{K}$-espace vectoriel.

Une forme est une application linéaire :
$\varphi\ :E \rightarrow \mathbb{K}$

**Définition :**

Une forme bilinéaire sur $E$ est une application
$\varphi:E \times E \rightarrow \mathbb{K}$ linéaire par rapport à
chaque variable.

C'est-à-dire :

1.  $\forall x,x^{'},y \in E,\ \lambda\mathbb{\in K}$,
    $\varphi\left( \lambda x + x^{'},y \right) = \lambda\varphi(x,y) + \varphi\left( x^{'},y \right)$

2.  $\forall x,y,y^{'} \in E,\ \lambda\mathbb{\in K,\ }\varphi\left( x,\lambda y + y^{'} \right) = \lambda\varphi(x,y) + \varphi\left( x,y^{'} \right)$

**Définition :**

Une forme $\varphi\ :E \times E\mathbb{\rightarrow R}$ est s

-   Symétrique si $\forall x,y \in E,\ \varphi(x,y) = \varphi(y,x)$

-   Antisymétrique si
    $\forall x,y \in E,\ \varphi(x,y) = - \varphi(y,x)$

**Exemple :**

$$\varphi:\mathbb{R}^{2} \times \mathbb{R}^{2}\mathbb{\rightarrow R}$$

$$\left( x_{1},x_{2} \right),\left( y_{1},y_{2} \right) \rightarrow \varphi\left( \left( x_{1},x_{2} \right),\left( y_{1},y_{2} \right) \right) = x_{1}y_{2} + x_{2}y_{1}$$

Montrer que $\varphi$ est une forme bilinéaire.

$$\varphi\left( \lambda\left( x_{1},x_{2} \right) + \left( x_{1}^{'},x_{2}^{'} \right),\left( y_{1},y_{2} \right) \right) = \left( \lambda x_{1} + x_{1}^{'} \right)y_{2} + \left( \lambda x_{2} + x_{2}^{'} \right)y_{1} = \left( \lambda x_{1}y_{2} + \lambda x_{2}y_{1} \right) + \left( x_{1}^{'}y_{2} + x_{2}^{'}y_{1} \right) = \lambda\varphi\left( \left( x_{1},x_{2} \right),\left( y_{1},y_{2} \right) \right) + \varphi\left( \left( x_{1}^{'},x_{2}^{'} \right),\left( y_{1},y_{2} \right) \right)$$

Elle est symétrique.

**Proposition :**

Si $\varphi$ est une forme bilinéaire, alors
$$\forall x,y \in E,\ \varphi\left( x,0_{E} \right) = \varphi\left( 0_{E},y \right) = 0$$.

**Preuve :**

Soient $$x,y \in E,\ y \neq 0_{E}$$, alors $$y - y = 0_{E}$$

$$\varphi\left( x,0_{E} \right) = \varphi(x,y - y) = \varphi(x,y) - \varphi(x,y) = 0$$

**Proposition :**

$$\forall x_{1},\ldots,x_{n},y_{1},\ldots,y_{n} \in E,\ \forall\alpha_{1},\ldots,\ \alpha_{n},\ \beta_{1},\ldots,\beta_{n}\mathbb{\in K,}$$

$$\varphi\left( \sum_{i = 1}^{n}{\alpha_{i}x_{i}},\sum_{j = 1}^{n}{\beta_{j}x_{j}} \right) = \sum_{i = 1}^{n}{\sum_{j = 1}^{n}{\alpha_{i}\beta_{j}\varphi\left( x_{i},y_{j} \right)}}$$

## II. Formes bilinéaires symétriques

**Proposition :**

$\varphi$ est une forme bilinéaire symétrique si et seulement si :

-   $\varphi$ est symétrique

-   $\varphi$ est linéaire par rapport à la première variable

**Preuve :**

Si $\varphi$ satisfait les deux, alors,
$\varphi\left( x,\lambda y + y^{'} \right) = \varphi\left( \lambda y + y^{'},x \right) = \lambda\varphi(y,x) + \varphi\left( y^{'},x \right) = \lambda\varphi(x,y) + \varphi\left( x,y^{'} \right)$

**Proposition :**

$\varphi:E \times E\mathbb{\rightarrow R}$ est bilinéaire antisymétrique
si et seulement si :

-   $\varphi$ est antisymétrique

-   $\varphi$ est linéaire par rapport à une variable

**Preuve :**

Si $\varphi$ est antisymétrique et linéaire par rapport à la première
variable, alors :

$$\varphi\left( x,\lambda y + y^{'} \right) = - \varphi\left( \lambda y + y^{'},x \right) = - \left( \lambda\varphi(y,x) + \varphi\left( y^{'},x \right) \right) = \lambda\varphi(x,y) + \varphi\left( x,y^{'} \right)$$

Donc $\varphi$ est bilinéaire.

**Notation :**

On note $$\mathcal{L}_{2}\left( E \times E\mathbb{,R} \right)$$ l'espace
vectoriel des formes bilinéaires, $$\mathcal{L}_{2,s}$$ celui des formes
bilinéaires symétriques, $$\mathcal{L}_{2,a}$$ celui des formes
bilinéaires antisymétriques.

**Proposition :**

$$\mathcal{L}_{2}\left( E \times E\mathbb{,R} \right) = \mathcal{L}_{2,s}\left( E \times E\mathbb{,R} \right) \oplus \mathcal{L}_{2,a}\left( E \times E\mathbb{,R} \right)$$

**Preuve :** Voir TD

$$\varphi(x,y) = \frac{\varphi(x,y) + \varphi(y,x)}{2} + \frac{\varphi(x,y) - \varphi(y,x)}{2}$$

**Définition :**

Une forme bilinéaire symétrique $\varphi$ est positive
si $\varphi(x,x) \geq 0$ $\forall x \in E$

**Définition :**

Une forme bilinéaire symétrique $\varphi$ est définie si et seulement si
$\varphi(x,x) = 0 \Rightarrow x = 0_{E}$

**Définition :**

Une forme bilinéaire symétrique $\varphi$ est définie positive si et
seulement si :

$$\forall x \neq 0_{E},\ \varphi(x,x) > 0$$

**Exemple :**

Soit
$x = \left( x_{1},x_{2} \right),\ y = \left( y_{1},y_{2} \right) \in \mathbb{R}^{2}$

Soit $\varphi(x,y) = x_{1}y_{1} - x_{2}y_{2}$

-   Elle est symétrique :
    $\varphi(y,x) = y_{1}x_{1} - y_{2}x_{2} = \varphi(x,y)$

-   Elle est linéaire par rapport à la première variable

-   Soit $x = \left( x_{1},x_{2} \right)\ $:
    $\varphi(x,x) = x_{1}^{2} - x_{2}^{2}$

Avec $x = (0,1),\ \varphi(x,x) = - 1 < 0$, donc $\varphi$ n'est pas
positive

-   Avec $x = (1,1),\ \varphi(x,x) = 0$ donc $\varphi$ n'est pas définie

En revanche, si $\varphi_{2}(x,y) = x_{1}y_{1} + x_{2}y_{2}$, alors
$\varphi_{2}$ est bilinéaire symétrique définie et positive

## III.  Formes bilinéaires de dimension finie

<!-- -->

### 1.  Matrices de formes bilinéaires

**Définition :**

Soit $\varphi:E \times E\mathbb{\rightarrow R}$ une forme bilinéaire.

On appelle matrice de $\varphi$ dans la base $\mathcal{B}$ la matrice :

$$Mat_{\mathcal{B}}(\varphi) = \left\lbrack \varphi\left( e_{i},e_{j} \right) \right\rbrack_{1 \leq i,j \leq n} = \begin{bmatrix}
\varphi\left( e_{1},e_{1} \right) & \ldots & \varphi\left( e_{1},e_{n} \right) \\
 \vdots & \  & \vdots \\
\varphi\left( e_{n},e_{1} \right) & \ldots & \varphi\left( e_{n},e_{n} \right)
\end{bmatrix}$$

$$\mathcal{B =}\left( e_{1},\ldots,e_{n} \right)$$

**Exemple :**

Cas
$E = \mathbb{R}^{2},\ x = \left( x_{1},x_{2} \right),\ y = \left( y_{1},y_{2} \right)$
dans la base canonique

$$\varphi(x,y) = ax_{1}y_{1} + bx_{1}y_{2} + cx_{2}y_{1} + dx_{2}y_{2}$$

$$Mat_{\mathcal{B}_{C}}(\varphi) = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}$$

**Remarque :**

Soit $f\ :\mathbb{R}^{2}\mathbb{\rightarrow R}$

$$H_{x,y} = \begin{pmatrix}
\frac{\partial^{2}f}{\partial x^{2}}(x,y) & \frac{\partial^{2}f}{\partial x\partial y}(x,y) \\
\frac{\partial^{2}f}{\partial y\partial x}(x,y) & \frac{\partial^{2}f}{\partial y^{2}}(x,y)
\end{pmatrix}$$

La matrice hessienne est la matrice d'une forme bilinéaire.

**Rappel :**

SI $f$ est $C^{1}$ en $(x,y)$, alors $H_{x,y}$ est symétrique.

**Proposition :**

Si $X = \begin{pmatrix}
x_{1} \\
 \vdots \\
x_{n}
\end{pmatrix},\ Y = \begin{pmatrix}
y_{1} \\
 \vdots \\
y_{n}
\end{pmatrix}$ dans la base $\mathcal{B}$, alors :

$$\varphi(X,Y) = \begin{matrix}
\ 
\end{matrix}^{T}XAY\ \text{avec}\ A = Mat_{\mathcal{B}}(\varphi)$$

**Preuve :**

$$X = x_{1}e_{1} + \ldots + x_{n}e_{n}$$

$$Y = y_{n}e_{1} + \ldots + y_{n}e_{n}$$

$$\varphi(X,Y) = \sum_{i = 1}^{n}{\sum_{j = 1}^{n}{x_{i}y_{j}\varphi\left( e_{i}e_{j} \right)}}$$

**Exercice :**

Montrer que $\begin{matrix}
\ 
\end{matrix}^{T}XAY$ donne la même chose

**Proposition :**

Réciproquement, soit $A \in \mathcal{M}_{n}\left( \mathbb{R} \right)$

$\forall x,y \in \mathbb{R}^{n},\ \varphi(X,Y) = \begin{matrix}
\ 
\end{matrix}^{T}XAY$ définit une forme bilinéaire.

**Preuve :**

$$\varphi\left( \lambda X + X^{2},Y \right) = \ ^{T}\left( \lambda X + X^{'} \right)AY = \lambda\ ^{T}XAY + \ ^{T}X^{'}AY$$

De même par rapport à la 2^e^ variable.

**Corollaire :**

Soit $\varphi:E \times E\mathbb{\rightarrow R}$

$\varphi$ est bilinéaire si et seulement s'il existe
$A \in \mathcal{M}_{n}\left( \mathbb{R} \right)$ tel que
$\forall X,Y \in E$ écrit dans une base, $\varphi(X,Y) = \ ^{T}XAY$

C'est-à-dire, si et seulement si $\exists c_{ij}\mathbb{\in R}$
($\forall i,j = 1,\ldots,n$)

Tel que
$\varphi\left( \left( x_{1},\ldots,x_{n} \right),\left( y_{1},\ldots,y_{n} \right) \right) = \sum_{i,j = 1}^{n}{c_{ij}x_{i}y_{j}}$

**Exercice :**

$$A = \begin{pmatrix}
 - 1 & 3 \\
2 & 5
\end{pmatrix}$$

Donner la forme bilinéaire dont $A$ est la matrice dans la base
canonique.

Soit $x = \left( x_{1},x_{2} \right)$ et
$y = \left( y_{1},y_{2} \right)$ dans la base canonique.

$$\varphi(x,y) = \begin{pmatrix}
x_{1} & x_{2}
\end{pmatrix}\begin{pmatrix}
 - 1 & 3 \\
2 & 5
\end{pmatrix}\begin{pmatrix}
y_{1} \\
y_{2}
\end{pmatrix} = \begin{pmatrix}
x_{1} & x_{2}
\end{pmatrix}\begin{pmatrix}
 - y_{1} + 3y_{2} \\
2y_{1} + 5y_{2}
\end{pmatrix} = x_{1}\left( - y_{1} + 3y_{2} \right) + x_{2}\left( 2y_{1} + 5y_{2} \right) = - x_{1}y_{1} + 3x_{1}y_{2} + 2x_{2}y_{1} + 5x_{2}y_{2}$$

**Proposition :**

Soit $\varphi:E \times E\mathbb{\rightarrow R}$ une forme bilinéaire et
$\mathcal{B,}\mathcal{B}^{'}$ deux bases de $Ε$.

Soit $A = Mat_{\mathcal{B}}(\varphi)$ et
$A^{'} = Mat_{\mathcal{B}^{'}}(\varphi)$

$$A^{'} = \ ^{T}PAP$$

**Preuve :**

Soient $PX^{'} = X$ et $PY^{'} = Y$ où $X$ et $X^{'}$ sont les
coordonnées de $x$ dans les bases $\mathcal{B}$ et $\mathcal{B}^{'}$
respectivement.

$$\varphi(x,y) = \ ^{T}XAY = \ ^{T}\left( PX^{'} \right)APY^{'} = \ ^{T}X^{'}\ ^{T}PAPY^{'} = \ ^{T}X^{'}A^{'}Y^{'}$$

**Exercice :**

Soit $A = \begin{pmatrix}
0 & 0 \\
1 & 1
\end{pmatrix} = Mat_{\mathcal{B}_{c}}(\varphi)$

Soit $\mathcal{B}^{'} = \begin{pmatrix}
v_{1} & v_{2}
\end{pmatrix}$ avec $v_{1} = (1,1)$ et $v_{2} = ( - 1,1)$

$$Mat_{\mathcal{B}^{'}}(\varphi) = A^{'} = \ ^{T}PAP^{- 1} = \begin{pmatrix}
1 & 1 \\
 - 1 & 1
\end{pmatrix}\begin{pmatrix}
0 & 0 \\
1 & 1
\end{pmatrix}\begin{pmatrix}
1 & - 1 \\
1 & 1
\end{pmatrix} = \begin{pmatrix}
2 & 0 \\
2 & 0
\end{pmatrix}$$

**Rappel :**

S'il existe $P$ inversible telle que $A = PBP^{- 1}$, on dit que $A$ et
$B$ sont semblables.

**Définition :**

$M$ et congrue à $M^{'}$ s'il existe $P$ inversible telle que
$M^{'} = \ ^{T}PMP$

Remarque : c'est une relation d'équivalence.

7.  Matrice de formes bilinéaires symétriques et antisymétriques

**Définition :**

$\forall$ base $\mathcal{B}$,
$\varphi \in \mathcal{L}_{2}\left( E \times E\mathbb{,R} \right)$ est :

-   Symétrique si et seulement si $Mat_{\mathcal{B}}(\varphi)$ est
    symétrique

-   Antisymétrique si et seulement si $Mat_{\mathcal{B}}(\varphi)$ est
    antisymétrique

**Rappel :**

-   $M$ est symétrique si $\ ^{T}M = M$

-   $M$ est antisymétrique si $\ ^{T}M = - M$

**Preuve :** Cas symétrique

Soit
$\varphi \in \mathcal{L}_{2,s}\left( E \times E\mathbb{\rightarrow R} \right)$

Alors, soit $\mathcal{B =}\left( e_{1},\ldots,e_{n} \right)$ une base :

$$Mat_{\mathcal{B}}(\varphi) = \left( \varphi\left( e_{i},e_{j} \right) \right) = \left( \varphi\left( e_{j},e_{i} \right) \right) = \ ^{T}\left( Mat_{\mathcal{B}}(\varphi) \right)$$

Réciproquement, si $A$ est la matrice dans une base telle que
$\ ^{T}A = A$, alors

$$\varphi(x,y) = \ ^{T}XAY = \ ^{T}\left( \ ^{T}Y\ ^{T}AX \right) = \ ^{T}\left( \ ^{T}YAX \right) = \ ^{T}YAX = \varphi(y,x)$$

**Proposition :**

Soit
$$\mathcal{S}_{n}\left( \mathbb{R} \right) \subset M_{n}\left( \mathbb{R} \right)$$
et
$$\mathcal{A}_{n}\left( \mathbb{R} \right) \subset M_{n}\left( \mathbb{R} \right)$$
l'ensemble des matrices respectivement symétriques et antisymétriques
sont des sous-espaces vectoriels.

$$\mathcal{M}_{n}\left( \mathbb{R} \right) = \mathcal{S}_{n}\left( \mathbb{R} \right) \oplus \mathcal{A}_{n}\left( \mathbb{R} \right)$$

De plus,
$$\dim\left( \mathcal{S}_{n}\left( \mathbb{R} \right) \right) = \frac{n(n + 1)}{2}$$
et
$$\dim\left( \mathcal{A}_{n}\left( \mathbb{R} \right) \right) = \frac{n(n - 1)}{2}$$

**Preuve :**

-   Ce sont des sous-espaces vectoriels : trivial

-   L'équation est équivalente à
    $$\mathcal{L}_{2}\left( E \times E\mathbb{,R} \right) = \mathcal{L}_{2,s}\left( E \times E\mathbb{,R} \right) + \mathcal{L}_{2,a}\left( E \times E\mathbb{,R} \right)$$

Soit
$$A = \left( a_{ij} \right)_{i,j \in \left. ⟦1,n \right.⟧} \in \mathcal{M}_{n}\left( \mathbb{R} \right)$$

$$A = \frac{A + \ ^{T}A}{2} + \frac{A - \ ^{T}A}{2}$$

$$S \in \mathcal{S}_{n}\left( \mathbb{R} \right),\ A^{'} \in \mathcal{A}_{n}\left( \mathbb{R} \right)$$

$$S = \left( \frac{a_{ij} + a_{ji}}{2} \right)_{i,j \in \left. ⟦1,n \right.⟧},\ A^{'} = \left( \frac{a_{ij} - a_{ji}}{2} \right)_{i,j \in \left. ⟦1,n \right.⟧}$$

Donc
$$\mathcal{M}_{n}\left( \mathbb{R} \right) = \mathcal{S}_{n}\left( \mathbb{R} \right) + \mathcal{A}_{n}\left( \mathbb{R} \right)$$

Remarque :
$$\mathcal{S}_{n}\left( \mathbb{R} \right) \cap \mathcal{A}_{n}\left( \mathbb{R} \right) = \left\lbrack  0_{n} \right\rbrack $$

-   Calculons les dimensions

Soit
$$S \in \mathcal{S}_{n}\left( \mathbb{R} \right),\ S = \left( a_{ij} \right)_{i,j \in \left. ⟦1,n \right.⟧},\ \forall i,j,\ a_{ij} = a_{ji}$$

$$S = \sum_{i = 1}^{n}{a_{ii}E_{ii}} + \sum_{1 \leq i < j \leq n}^{}{a_{ij}\left( E_{ij} + E_{ji} \right)}$$

$$S_{n}\left( \mathbb{R} \right) = {Vect}\left( E_{ii},\left( E_{ij} + E_{ji} \right) \right) ≔ {Vect}\left( \mathcal{B}_{\mathcal{S}_{n}\left( \mathbb{R} \right)} \right)$$

Montrons que
$$\mathcal{B}_{\mathcal{S}_{n}\left( \mathbb{R} \right)}$$ est une famille
libre

Soit
$\lambda_{ii}\mathbb{\in R\ }\left( i \in \left. ⟦1,n \right.⟧ \right)$
et $\lambda_{ij}\mathbb{\in R\ }(1 \leq i < j \leq n)$

$$\sum_{i = 1}^{n}{\lambda_{ii}E_{ii}} + \sum_{1 \leq i < j \leq n}^{}{\lambda_{ij}\left( E_{ij} + E_{ji} \right)} = 0_{\mathcal{M}_{n}\left( \mathbb{R} \right)}$$

$$\Leftrightarrow \sum_{i = 1}^{n}{\lambda_{ii}E_{ii}} + \sum_{1 \leq i < j \leq n}^{}{\lambda_{ij}E_{ij}} + \sum_{1 \leq i < j \leq n}^{}{\lambda_{ij}E_{ij}} = 0_{\mathcal{M}_{n}\left( \mathbb{R} \right)}$$

$$\Rightarrow \lambda_{ii} = \lambda_{ij} = 0\ \forall i,j$$

$$\mathcal{B}_{\mathcal{S}_{n}\left( \mathbb{R} \right)}$$ est une base de
$$\frac{n(n + 1)}{2}$$ vecteurs.

De même,

$$\mathcal{A}_{n}\left( \mathbb{R} \right) = {\text{Vect}\left( E_{ij} - E_{ji} \right)}_{1 \leq i < j \leq n}$$

$$\mathcal{B}_{\mathcal{A}_{n}\left( \mathbb{R} \right)}$$ est une base de
$$\frac{n(n - 1)}{2}$$ vecteurs.

**Corollaire :**

-   $$\mathcal{L}_{2,s}\left( E \times E,\mathbb{R} \right)$$ est
    isomorphe à $$\mathcal{S}_{n}\left( \mathbb{R} \right)$$

-   $$\mathcal{L}_{2,n}\left( E \times E,\mathbb{R} \right)$$ est
    isomorphe à $$\mathcal{A}_{n}\left( \mathbb{R} \right)$$

$$\dim\left( \mathcal{L}_{2,s}\left( E \times E,\mathbb{R} \right) \right) = \frac{n(n + 1)}{2},\ \dim\left( \mathcal{L}_{2,a}\left( E \times E,\mathbb{R} \right) \right) = \frac{n(n - 1)}{2}$$

8.  Matrices définies positives

**Définition :**

Soit $A \in \mathcal{S}_{n}\left( \mathbb{R} \right)$.

-   $A$ est positive si
    $$\forall X \in \mathcal{M}_{n,1}\left( \mathbb{R} \right),\ \ ^{T}XAX \geq 0$$

-   $A$ est définie si
    $$\forall X \in \mathcal{M}_{n,1}\left( \mathbb{R} \right),\ \ ^{T}XAX = 0 \Rightarrow X = 0_{n,1}$$

-   $A$ est définie positive si
    $$\forall X \in \mathcal{M}_{n,1}\left( \mathbb{R} \right),\ \ ^{T}XAX > 0 \Rightarrow X = 0_{n,1}$$

**Théorème :**

Soit $f \in \mathcal{L}_{2}\left( E \times E,\mathbb{R} \right)$ est
définie positive si et seulement si sa matrice l'est dans n'importe
quelle base.

**Preuve :**

$\varphi$ est positive si $\varphi(x,x) \geq 0$ $\forall X \in E$

Soit $\mathcal{B}$ base de $E$ et $X$ le vecteur de $x$ dans la base
$\mathcal{B}$, alors $\varphi(x,x) = \ ^{T}XMat_{\mathcal{B}}(\varphi)X$

**Théorème :**

Soit $A \in \mathcal{S}_{n}\left( \mathbb{R} \right)$

-   $Sp_{\mathbb{C}}(A)\mathbb{\subset R}$

-   Si $A$ est positive alors ses valeurs propres sont positives

-   Si $A$ est définie alors les valeurs propres sont non nulles, donc
    $A$ est inversible

**Preuve :**

-   $$A \in \mathcal{S}_{n}\left( \mathbb{R} \right)$$ donc
    $$P_{A}\mathbb{\in R}\lbrack X\rbrack$$

Si $\lambda$ est racine de $P_{A}$ alors $\overline{\lambda}$ aussi.

Donc si $\lambda \in Sp_{\mathbb{C}}(A)$ alors
$\overline{\lambda} \in Sp_{\mathbb{C}}(A)$

Soit $X$ vecteur propre associé à $\lambda$,
$\ ^{T}XAX = \lambda\sum_{}^{}\left\vert  x_{i} \right\vert ^{2}$

$$\ ^{T}\left( \overline{X} \right)AX = \ ^{T}\overline{X}\lambda X = \lambda\ ^{T}\overline{X}X = \lambda\sum_{i = 1}^{n}\left\vert  x_{i} \right\vert ^{2}$$

$$\ ^{T}\left( \ ^{T}\left( \overline{X} \right)AX \right) = \ ^{T}X\ ^{T}A\overline{X} = \ ^{T}XA\overline{X}$$

($AX = \lambda X$ donc
$\overline{AX} = \overline{\lambda}\overline{X} = A\overline{X}$ car $A$
réelle).

$$\ ^{T}X\overline{X} = \sum_{}^{}\left\vert  x_{i} \right\vert ^{2} = \ ^{T}\overline{X}X$$

Ainsi,
$\lambda\sum_{}^{}\left\vert  x_{i} \right\vert ^{2} = \ ^{T}\left( \overline{X} \right)AX = \ ^{T}\left( \ ^{T}\left( \overline{X} \right)AX \right) = \overline{\lambda}\sum_{}^{}\left\vert  x_{i} \right\vert ^{2}$

Donc $\lambda = \overline{\lambda}$

-   Soit $A$ positive, $\lambda \in Sp_{\mathbb{R}}(A)$, $X$ un vecteur
    propre associé.

Alors, $\ ^{T}XAX = \lambda\sum_{}^{}x_{i}^{2} \geq 0$ car $A$ positive

Donc $\lambda \geq 0$.

-   Soit $A$ définie, $\lambda \in Sp_{\mathbb{R}}(A)$, $X$ un vecteur
    propre associé.

Alors $\ ^{T}XAX = \lambda\sum_{}^{}x_{i}^{2}$

Si $\lambda = 0$ alors $X = 0$ car $A$ est définie.

Donc $0$ n'est pas valeur propre.

**Définition :**

Soit $A \in \mathcal{M}_{n}\left( \mathbb{R} \right)$.

On appelle sous-matrice principale d'ordre de $A$ d'ordre $k$ la
matrice :

$$A_{k} = \begin{pmatrix}
a_{11} & \ldots & a_{1k} \\
 \vdots & \  & \vdots \\
a_{k1} & \ldots & a_{kk}
\end{pmatrix}$$

**Théorème :**

$$A \in \mathcal{S}_{n}\left( \mathbb{R} \right)$$ est définie positive si
et seulement si
$$\det\left( A_{k} \right) > 0\ \forall k \in \left. ⟦1,n \right.⟧$$

**Preuve :**

Par récurrence sur $n$.

On suppose

# Chapitre 4 : Espaces Préhilbertiens

## I.  Produit scalaire et norme

<!-- -->

### 1.  Définition

**Définition :** Produit scalaire

Soit $E$ un $\mathbb{R}$-espace vectoriel

Un produit scalaire sur $E$ est une forme bilinéaire symétrique définie positive sur $E$.

**Remarques :**

-   Au lieu de $\varphi\ :E \times E\mathbb{\rightarrow R}$, on notera souvent $\varphi(x,y) = (x,y)$ ou $\left\langle x,y \right\rangle$ ou $\left\langle x\vert y \right\rangle$

-   Un produit scalaire sur $E$ induit un produit scalaire sur tout sous-espace vectoriel

**Exercice :**

Produit scalaire « canonique » sur $\mathbb{R}^{n}$

$$\mathbb{R}^{n} \times \mathbb{R}^{n}\mathbb{\rightarrow R}$$

$$\left( \left( x_{1},\ldots,x_{n} \right),\left( y_{1},\ldots,y_{n} \right) \right) \rightarrow \sum_{i = 1}^{n}{x_{i}y_{i}} = x_{1}y_{1} + \ldots + x_{n}y_{n} = \left\langle x,y \right\rangle$$

**Preuve :**

-   $\left\langle .,. \right\rangle$ est symétrique

$$\forall x,y \in \mathbb{R}^{n},\ \left\langle x,y \right\rangle = \sum_{i = 1}^{n}{x_{i}y_{i}} = \sum_{i = 1}^{n}{y_{i}x_{i}} = \left\langle y,x \right\rangle$$

-   Soir $x,x^{'},y \in \mathbb{R}^{n},\ \lambda\mathbb{\in R}$

$$\left\langle x + \lambda x^{'},y \right\rangle = \sum_{i = 1}^{n}{\left( x_{i} + \lambda x_{i}^{'} \right)y_{i}} = \sum_{i = 1}^{n}{x_{i}y_{i} + \lambda x_{i}^{'}y_{i}} = \left\langle x,y \right\rangle + \lambda\left\langle x^{'},y \right\rangle$$

D'où $\left\langle .,. \right\rangle$ est une forme bilinéaire symétrique.

Soit $x = \left( x_{1},\ldots,x_{n} \right) \in \mathbb{R}^{n}$

-   $\left\langle .,. \right\rangle$ est définie

$$\left\langle x,x \right\rangle = 0 \Rightarrow \sum_{i = 1}^{n}x_{i}^{2} = 0$$

$\Rightarrow \forall i \in \left. ⟦1,n \right.⟧,x_{i}^{2} = 0$ donc $x_{i} = 0$

$$\Rightarrow x = 0_{\mathbb{R}^{n}}$$

-   $\left\langle .,. \right\rangle$ est positive

$$\left\langle x,x \right\rangle = \sum_{i = 1}^{n}x_{i}^{2} \geq 0$$

### 2.  Exemples fondamentaux

-   Le produit scalaire canonique de $\mathbb{R}^{n}$

-   Produit scalaire canonique sur $\mathcal{M}_{n,p}\left( \mathbb{R} \right)$

$$\forall A,B \in \mathcal{M}_{n,p}\left( \mathbb{R} \right),$$

Si 
$$A = \left( a_{ij} \right)_{\begin{array}{r}
i \in \left. ⟦1,n \right.⟧ \\
j \in \left. ⟦1,p \right.⟧
\end{array}}$ et $B = \left( b_{ij} \right)_{\begin{array}{r}
i \in \left. ⟦1,n \right.⟧ \\
j \in \left. ⟦1,p \right.⟧
\end{array}}$$

$$\left\langle A,B \right\rangle = Tr\left( A\ \ ^{T}B \right) = \sum_{j = 1}^{p}{\sum_{i = 1}^{n}{a_{ij}b_{ij}}}$$

-   Produit scalaire sur $\mathbb{R}_{n}\lbrack X\rbrack$

$$P(X) = \sum_{k = 0}^{n}{a_{k}X^{k}},\ Q(X) = \sum_{k = 0}^{n}{b_{k}X^{k}}$$

$$\left\langle P,Q \right\rangle = \sum_{k = 0}^{n}{a_{k}b_{k}}$$

-   Produit scalaire canonique sur $\mathcal{C}\left( \lbrack a,b\rbrack\mathbb{,R} \right)$

Soient $f,g \in \mathcal{C}\left( \lbrack a,b\rbrack\mathbb{,R} \right)$

$$\left\langle f,g \right\rangle = \int_{a}^{b}{f(t)g(t)dt}$$

### 3. Norme associée à un produit scalaire

**Définition :** Norme sur $E$

On appelle norme sur $E$ une fonction $N:E\mathbb{\rightarrow R}$ qui vérifie :

i.  $\forall x \in E,\ \ N(x) = 0 \Rightarrow x = 0_{E}$ (séparation)

ii. $\forall\lambda\mathbb{\in R,\forall}x \in E,\ \ N(\lambda x) = \vert \lambda\vert N(x)$ (absolue homogénéité)

iii. $\forall x,y \in E,\ N(x + y) \leq N(x) + N(y)$ (inégalité triangulaire)

**Théorème :**

Soit $\left\langle .,. \right\rangle$ un produit scalaire sur $E$, alors la fonction définie par,

$$\forall x \in E,\ \left\Vert  x \right\Vert  = \sqrt{\left\langle x,x \right\rangle}$$

(bien définie car $\left\langle .,. \right\rangle$ est positive)

**Preuve :**

i.  $\left\Vert  x \right\Vert  = 0 \Rightarrow \sqrt{\left\langle x,x \right\rangle} = 0 \Rightarrow \left\langle x,x \right\rangle \Rightarrow x = 0_{E}$ (car le produit scalaire est défini)

ii. $\left\Vert  \lambda x \right\Vert  = \sqrt{\left\langle \lambda x,\lambda x \right\rangle} = \sqrt{\lambda^{2}\left\langle x,x \right\rangle} = \vert \lambda\vert \sqrt{\left\langle x,x \right\rangle} = \vert \lambda\vert \left\Vert  x \right\Vert $

iii. $\left\Vert  x + y \right\Vert  = \sqrt{\left\langle x + y,x + y \right\rangle} = \sqrt{\left\langle x,x \right\rangle + \left\langle x,y \right\rangle + \left\langle y,x \right\rangle + \left\langle y,y \right\rangle} = \sqrt{\left\langle x,x \right\rangle + 2\left\langle x,y \right\rangle + \left\langle y,y \right\rangle}$

Montrer que

$$\left\langle x,x \right\rangle + 2\left\langle x,y \right\rangle + \left\langle y,y \right\rangle \leq \left\langle x,x \right\rangle + \left\langle y,y \right\rangle + 2\sqrt{\left\langle x,x \right\rangle\left\langle y,y \right\rangle}$$

$$\left\langle x,y \right\rangle \leq \sqrt{\left\langle x,x \right\rangle\left\langle y,y \right\rangle}$$

$$\left\langle x,y \right\rangle \leq \left\Vert  x \right\Vert \left\Vert  y \right\Vert $$

On reconnait l'inégalité de Cauchy-Schwarz.

**Théorème :** Inégalité de Cauchy-Schwarz

$\forall x,y \in E$, on a $\left\vert  \left\langle x,y \right\rangle \right\vert  \leq \left\Vert  x \right\Vert \left\Vert  y \right\Vert $

De plus, il y a égalité si et seulement si $x$ et $y$ sont colinéaires.

**Preuve :** Soit $x,y \in E,\ t\mathbb{\in R}$

$$\forall t\mathbb{\in R}$$

$$0 \leq \left\Vert  x + ty \right\Vert ^{2} = \left\langle x,x \right\rangle + 2t\left\langle x,y \right\rangle + t^{2}\left\langle y,y \right\rangle$$

Donc $P$ s'annule 0 ou 1 fois. Donc son discriminant est négatif ou nul.

$$\Delta = 4\left\langle x,y \right\rangle^{2} - 4\left\langle x,x \right\rangle\left\langle y,y \right\rangle$$

$$\Delta \leq 0 \Rightarrow \left\langle x,y \right\rangle^{2} \leq \left\langle x,x \right\rangle\left\langle y,y \right\rangle \Rightarrow \left\vert  \left\langle x,y \right\rangle \right\vert  \leq \left\Vert  x \right\Vert \left\Vert  y \right\Vert $$

Il y a égalité si le déterminant s'annule, alors il existe $$t_{0}\mathbb{\in R}$$ tel que $$\left\Vert  x + t_{0}y \right\Vert  = 0 \Rightarrow x + t_{0}y = 0_{E}$$ donc $$x = - t_{0}y$$ et $x$ et $y$ sont colinéaires.

### 4. Exemples de normes

-   $\left\Vert  x \right\Vert  = \sum_{i = 1}^{n}x_{i}^{2}$

-   $\forall A \in \mathcal{M}_{n,p}\left( \mathbb{R} \right)$

$$\left\Vert  A \right\Vert  = \sqrt{Tr\left( A\ \ ^{T}A \right)} = \sum_{i = 1}^{n}{\sum_{j = 1}^{p}a_{ij}^{2}}$$

-   $\forall f \in \mathcal{C}\left( \lbrack a,b\rbrack\mathbb{,R} \right)$

$$\left\Vert  f \right\Vert  = \sqrt{\int_{a}^{b}{f(t)^{2}dt}}$$

## II. Espaces préhilbertiens réels

**Définition :**

Un espace préhilbertien réel est un $\mathbb{R}$-espace vectoriel $E$ muni d'un produit scalaire $\left\langle .,. \right\rangle$, on le note $\left( E,\left\langle .,. \right\rangle \right)$.

Un espace euclidien est un espace préhilbertien de dimension finie.

### 5.  Inégalités et identités

Soit $\left( E,\left\langle .,. \right\rangle \right)$ un espace préhilbertien réel

**Proposition :**

$$\forall x,y \in E,$$

$$\left\Vert  x + y \right\Vert ^{2} = \left\Vert  x \right\Vert ^{2} + 2\left\langle x,y \right\rangle + \left\Vert  y \right\Vert ^{2}$$

$$\left\Vert  x - y \right\Vert ^{2} = \left\Vert  x \right\Vert ^{2} - 2\left\langle x,y \right\rangle + \left\Vert  y \right\Vert ^{2}$$

**Preuve :**

$$\left\Vert  x + y \right\Vert ^{2} = \left\langle x + y,x + y \right\rangle = \left\langle x,x \right\rangle + 2\left\langle x,y \right\rangle + \left\langle y,y \right\rangle$$

**Proposition :** Identité du parallélogramme

$$\forall x,y \in E$$

$$\left\Vert  x + y \right\Vert ^{2} + \left\Vert  x - y \right\Vert ^{2} = 2\left( \left\Vert  x \right\Vert ^{2} + \left\Vert  y \right\Vert ^{2} \right)$$

**Théorème :**

Une norme qui satisfait l'inégalité du parallélogramme est préhilbertienne.

**Remarque :**

On peut utiliser ce critère pour vérifier qu'une norme provient d'un produit scalaire.

**Proposition :**

Soit $\left( E,\left\langle .,. \right\rangle \right)$ un espace préhilbertien réel.

Alors, $\forall x,y \in E$

$$\left\langle x,y \right\rangle = \frac{1}{2}\left( \left\Vert  x + y \right\Vert ^{2} - \left\Vert  x \right\Vert ^{2} - \left\Vert  y \right\Vert ^{2} \right) = \frac{1}{4}\left( \left\Vert  x + y \right\Vert ^{2} - \left\Vert  x - y \right\Vert ^{2} \right)$$

**Remarque :**

Soit $\left\Vert  . \right\Vert $ une norme sur un EVN $E$. Comment vérifier qu'elle provient d'un produit scalaire, donc que $E$ est un espace préhilbertien ?

On pose,

$$\forall x,y \in E,\ \varphi(x,y) = \frac{1}{2}\left( \left\Vert  x + y \right\Vert ^{2} - \left\Vert  x \right\Vert ^{2} - \left\Vert  y \right\Vert ^{2} \right)$$

Et on vérifie que $\varphi$ définit un produit scalaire.

En pratique, seule la linéarité par rapport à une variable peut ne pas être vérifiée.

**Théorème :**

Une norme sur $E$ vérifie l'identité du parallélogramme si et seulement si elle provient d'un produit scalaire (c'est-à-dire si $E$ est préhilbertien).

**Preuve :**

Si $E$ est préhilbertien, alors on a l'identité du parallélogramme (déjà vu).

Réciproquement, on peut montrer que $\varphi(x,y) = \frac{1}{2}\left( \left\Vert  x + y \right\Vert ^{2} - \left\Vert  x \right\Vert ^{2} - \left\Vert  y \right\Vert ^{2} \right)$ est linéaire en $x$ à l'aide de l'identité du parallélogramme.

**Théorème :** Inégalité de Cauchy-Schwarz

$\forall x,y \in E$, on a $\left\langle x,y \right\rangle^{2} \leq \left\Vert  x \right\Vert ^{2}\left\Vert  y \right\Vert ^{2}$

De plus, il y a égalité si et seulement si $x$ et $y$ sont colinéaires.

**Remarque :**

On peut aussi, de manière équivalente, exprimer cette inégalité :

$$\left\vert  \left\langle x,y \right\rangle \right\vert  \leq \left\Vert  x \right\Vert \left\Vert  y \right\Vert $$

**Exemple :**

$$\forall x_{1},\ldots,x_{n},y_{1},\ldots,y_{n} \in \mathbb{R}^{2}$$

$$\left( \sum_{k = 1}^{n}{x_{k}y_{k}} \right)^{2} \leq \left( \sum_{k = 1}^{n}x_{i}^{2} \right)\left( \sum_{k = 1}^{n}y_{i}^{2} \right)$$

$\forall A,B \in \mathcal{M}_{n,p}\left( \mathbb{R} \right)$,

$$Tr\left( A\ \ ^{T}B \right)^{2} \leq Tr\left( A\ ^{T}A \right)Tr\left( B\ ^{T}B \right)$$

$$\forall f,g \in \mathcal{C}^{0}\left( \lbrack a,b\rbrack\mathbb{,R} \right),$$

$$\left( \int_{a}^{b}{f(t)g(t)dt} \right)^{2} \leq \left( \int_{a}^{b}{f^{2}(t)dt} \right)\left( \int_{a}^{b}{g^{2}(t)dt} \right)$$

## III. Orthogonalité

**Définition :**

Soit $\left( E,\left\langle .,. \right\rangle \right)$ un espace préhilbertien, soit $x,y \in E$.

On dit que $x$ est orthogonal à $y$, et on note $x\bot y$, si $\left\langle x,y \right\rangle = 0$

**Remarque :**

$$x\bot y \Leftrightarrow y\bot x$$

Deux vecteurs peuvent être orthogonaux pour un produit scalaire mais pas pour un autre.

**Proposition :**

-   Le vecteur nul est orthogonal à tout vecteur

-   Il est le seul orthogonal à lui-même

**Preuve :**

-   $\left\langle x,0 \right\rangle = 0$ par linéarité du produit scalaire.

$$\left\langle x,0 \right\rangle = \left\langle x,0x \right\rangle = 0\left\langle x,x \right\rangle = 0$$

-   Soit $x \in E$ tel que $\left\langle x,x \right\rangle = 0$

Alors $x = 0$ car $\left\langle .,. \right\rangle$ est définie.

**Définition :**

Soit $A \subset E,\ B \subset E,x \in E$

-   On dit que $x$ est orthogonal à $A$, et on note $x\bot A$, si $\forall y \in A,\ x\bot y$

-   On dit que $A$ est orthogonal à $B$, et on note $A\bot B$, si $\forall x \in A,\forall y \in B,\ x\bot y$

**Proposition :**

Soit $F = {Vect}\left( v_{1},\ldots,v_{n} \right)$ sous-espace vectoriel de $E$.

Alors $x\bot E \Leftrightarrow x\bot v_{i}\ \forall i \in \left. ⟦1,n \right.⟧$

**Preuve :**

$\Rightarrow$ par définition

$$\Leftarrow$$

Soit $x\bot v_{i}\ \forall i \in \left. ⟦1,n \right.⟧$

$${Vect}\left( v_{1},\ldots,v_{n} \right) = \left\lbrack  \lambda_{1}v_{1} + \ldots + \lambda_{n}v_{n},\ \left( \lambda_{1},\ldots,\lambda_{n} \right)\mathbb{\in R} \right\rbrack $$

Soit $y \in F$, montrer que $\left\langle x,y \right\rangle = 0$

Soient $\lambda_{1},\ldots,\lambda_{n}\mathbb{\in R}$ tels que $y = \lambda_{1}v_{1},\ldots + \lambda_{n}v_{n}$

$$\left\langle x,y \right\rangle = \left\langle x,\lambda_{1}v_{1} + \ldots + \lambda_{n}v_{n} \right\rangle = \lambda_{1}\left\langle x,v_{1} \right\rangle + \ldots + \lambda_{n}\left\langle x,v_{n} \right\rangle = 0$$

**Proposition :**

Soit $F = {Vect}\left( u_{1},\ldots,u_{p} \right)$ et $G = {Vect}\left( v_{1},\ldots,v_{p} \right)$ deux sev de $E$.

$$F\bot G \Leftrightarrow \forall i,j \in \left. ⟦1,p \right.⟧,\ \left\langle u_{i},v_{p} \right\rangle = 0$$

**Preuve :**

$\Rightarrow$ par définition

$$\Leftarrow$$

On suppose $\forall i,j \in \left. ⟦1,p \right.⟧,\ \left\langle u_{i},v_{j} \right\rangle = 0$

Soit $x \in F,\ y \in G$

Soit $\lambda_{1},\ldots,\lambda_{n}$, $\mu_{1},\ldots,\mu_{n}\mathbb{\in R}$ tels que $x = \sum_{}^{}{\lambda_{i}u_{i}}$ et $y = \sum_{}^{}{\mu_{i}v_{i}}$

$$\left\langle x,y \right\rangle = \left\langle \sum_{}^{}{\lambda_{i}u_{i}},\sum_{}^{}{\mu_{i}v_{i}} \right\rangle = \sum_{}^{}{\lambda_{i}\mu_{j}\left\langle u_{i},v_{j} \right\rangle} = 0$$

Donc $F\bot G$

**Définition :**

Soit $A \subset E$ un sous-ensemble de $E$ (par forcément un sev).

L'orthogonal de $A$, noté $A^{\bot}$, est défini par :

$$A^{\bot} = \left\lbrack  y \in E,\ y\bot A \right\rbrack $$

**Proposition :**

$A^{\bot}$ est un sous-espace vectoriel de $E$.

**Preuve :**

Soit $x,y \in A^{\bot}$, $\lambda,\mu\mathbb{\in K}$

Montrons que $\lambda x + \mu y \in A^{\bot}$

Soit $a \in A$, montrons que $\lambda x + \mu y\bot a$

$$\left\langle \lambda x + \mu y,a \right\rangle = \lambda\left\langle x,a \right\rangle + \mu\left\langle y,a \right\rangle = 0$$

**Proposition :**

-   $\left\lbrack  0_{E} \right\rbrack ^{\bot} = E$

-   $E^{\bot} = \left\lbrack  0_{E} \right\rbrack $

**Proposition :**

-   $A^{\bot} = {Vect}(A)^{\bot}$

**Preuve :**

Montrons que $A \subset B \Rightarrow B^{\bot} \subset A^{\bot}$

Soit $x \in B^{\bot}$, montrons que $x \in A^{\bot}$

Soit $a \in A,\ \left\langle x,a \right\rangle = 0\ \text{car}\ A \subset B\ \text{donc}\ a \in B$

Donc $x \in A^{\bot}$

-   $A \subset {Vect}(A) = \left\lbrack  \lambda_{1}a_{1} + \ldots + \lambda_{k}a_{k},\ a_{1},\ldots,a_{k} \in A,\ \lambda_{1},\ldots,\lambda_{k}\mathbb{\in R} \right\rbrack $

Donc ${Vect}(A)^{\bot} \subset A^{\bot}$

-   Montrons que $A^{\bot} \subset {Vect}(A)^{\bot}$

Soit $x \in A^{\bot}$, montrer que $x \in {Vect}(A)^{\bot}$

Soit $y = \lambda_{1}a_{1} + \ldots + \lambda_{n}a_{n} \in {Vect}(A)$

$$\left\langle x,y \right\rangle = \left\langle x,\sum_{}^{}{\lambda_{i}a_{i}} \right\rangle = \sum_{}^{}{\lambda_{i}\left\langle x,a_{i} \right\rangle} = 0\ \text{car}\ x \in A^{\bot}$$

**Remarque :**

Si $F,G \in E$,

$F\bot G$ n'implique pas $F = G^{\bot}$ ou $G = F^{\bot}$

**Exemple :**

Soit $E = \mathbb{R}^{3}$

$$D_{1} = {Vect}\begin{pmatrix}
0 \\
1 \\
0
\end{pmatrix},\ D_{2} = {Vect}\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix}$$

$$D_{1}^{\bot} = {Vect}\left\lbrack  \begin{pmatrix}
1 \\
0 \\
1
\end{pmatrix},\begin{pmatrix}
0 \\
0 \\
1
\end{pmatrix} \right\rbrack $$

**Preuve :**

Soit 

$$\begin{pmatrix}
x \\
y \\
z
\end{pmatrix} \in D_{1}^{\bot}$$

Alors 

$$\forall a \in \mathbb{R,\ }\left\langle \begin{pmatrix}
x \\
y \\
z
\end{pmatrix},\ \begin{pmatrix}
0 \\
a \\
0
\end{pmatrix} \right\rangle = 0 \Leftrightarrow \forall a \in \mathbb{R,\ }ay = 0 \Leftrightarrow y = 0$$

**Proposition :**

Soit $F \subset E$ un s.e.v.

-   $F \cap F^{\bot} = \left\lbrack  0_{E} \right\rbrack $

-   $F\bot F^{\bot}$

-   $F \subset \left( F^{\bot} \right)^{\bot}$

**Preuve :**

-   Soit $x \in F \cap F^{\bot}$

Alors $\left\langle x,x \right\rangle = 0$

Donc $x \in 0_{E}$ car le produit scalaire est une forme bilinéaire définie.

-   $F\bot F^{\bot}$ évident

-   Evident

### 1. Familles orthogonales et orthonormales

**Définition :**

Soit $\left( E,\left\langle .,. \right\rangle \right)$ un espace préhilbertien réel.

Soit $$\left\lbrack  x_{i} \right\rbrack _{i \in I}$$ une famille de vecteurs de $E$.

-   $$\left\lbrack  x_{i} \right\rbrack _{i \in I}$$ est une famille orthogonale si $$\forall i \neq j \in I,\ \left\langle x_{i},x_{j} \right\rangle = 0$$

-   $$\left\lbrack  x_{i} \right\rbrack _{i \in I}$$ est une famille orthonormale si elle est orthogonale et que $$\forall i \in I,\ \sqrt{\left\langle x_{i},x_{i} \right\rangle} = \left\Vert  x_{i} \right\Vert  = 1$$

**Remarque :**

$\left\lbrack  x_{i} \right\rbrack _{i \in I}$ est une famille orthonormale si et seulement si 
$$\forall i,j \in I,\ \left\langle x_{i},x_{j} \right\rangle = \delta_{ij} = \left\lbrack  \begin{array}{r}
0\ \text{si}\ i \neq j \\
1\ \text{si}\ i = j
\end{array} \right. $$

**Proposition :**

Soit $\left\lbrack  x_{i} \right\rbrack _{i \in I}$ une famille orthogonale de $E$ composée de vecteurs tous non nuls, alors elle est libre.

**Preuve :**

Soit $\left\lbrack  x_{i} \right\rbrack _{i \in I}$ une famille orthogonale.

Soient $\lambda_{1},\ldots,\lambda_{n}\mathbb{\in R}$ tels que $\lambda_{1}x_{1} + \ldots + \lambda_{n}x_{n} = 0$

$$\forall i \in I,\ \left\langle 0_{E},x_{i} \right\rangle = 0$$

Donc $$\left\langle \lambda_{1}x_{1} + \ldots + \lambda_{n}x_{n},\ x_{i} \right\rangle = 0 \Leftrightarrow \lambda_{1}\left\langle x_{1},x_{i} \right\rangle + \ldots + \lambda_{n}\left\langle x_{n},x_{i} \right\rangle = 0 \Leftrightarrow_{i \neq j \Rightarrow \left\langle x_{i},x_{j} \right\rangle = 0}\lambda_{i}\left\langle x_{i},x_{i} \right\rangle = 0 \Leftrightarrow_{x_{i} \neq 0_{E}}\lambda_{i} = 0$$

Finalement, $\lambda_{1} = \ldots = \lambda_{n} = 0$

Donc $\left\lbrack  x_{i} \right\rbrack _{i \in I}$ est libre.

**Théorème :** Théorème de Pythagore

Soient $x,y \in E$

$$x\bot y \Leftrightarrow \left\Vert  x + y \right\Vert ^{2} = \left\Vert  x \right\Vert ^{2} + \left\Vert  y \right\Vert ^{2}$$

**Preuve :**

$$\left\Vert  x + y \right\Vert ^{2} = \left\Vert  x \right\Vert ^{2} + \left\Vert  y \right\Vert ^{2} \Leftrightarrow \left\Vert  x \right\Vert ^{2} + \left\Vert  y \right\Vert ^{2} + 2\left\langle x,y \right\rangle = \left\Vert  x \right\Vert ^{2} + \left\Vert  y \right\Vert ^{2} \Leftrightarrow \left\langle x,y \right\rangle = 0 \Leftrightarrow x\bot y$$

**Proposition :**

Soit $\left\lbrack  x_{i} \right\rbrack _{i \in I}$ une famille de $E$.

$$\left\lbrack  x_{i} \right\rbrack _{i \in I}\ \text{orthogonale} \Rightarrow \left\Vert  \sum_{i = 1}^{n}x_{i} \right\Vert ^{2} = \sum_{}^{}\left\Vert  x_{i} \right\Vert ^{2}$$

La réciproque est fausse dans le cas $n > 2$.

**Preuve :**

Soit $\left\lbrack  x_{i} \right\rbrack _{i \in I}$ une famille orthogonale.

$$\left\Vert  x_{1} + \ldots + x_{n} \right\Vert ^{2} = \left\Vert  x_{1} \right\Vert ^{2} + \left\Vert  x_{2} + \ldots + x_{n} \right\Vert ^{2} = \ldots = \left\Vert  x_{1} \right\Vert ^{2} + \ldots + \left\Vert  x_{n} \right\Vert ^{2}$$

13. Procédé d'orthogonalisation de Gram-Schmidt

**Objectif :** Soit $\left\lbrack  v_{1},\ldots,v_{p} \right\rbrack $ famille libre de $\left( E,\left\langle .,. \right\rangle \right)$

On veut construire $\left\lbrack  \varepsilon_{1},\ldots,\varepsilon_{p} \right\rbrack $ famille orthonormale telle que $\forall k \in \left. ⟦1,p \right.⟧$, ${Vect}\left( v_{1},\ldots,v_{k} \right) = {Vect}\left( \varepsilon_{1},\ldots,\varepsilon_{k} \right)$

**Exemple :**

$$v_{1} = \begin{pmatrix}
1 \\
1 \\
0
\end{pmatrix},\ v_{2} = \begin{pmatrix}
2 \\
1 \\
0
\end{pmatrix},\ v_{3} = \begin{pmatrix}
0 \\
1 \\
1
\end{pmatrix}$$

On cherche $\left\lbrack  \varepsilon_{1},\varepsilon_{2},\varepsilon_{3} \right\rbrack $ orthonormale et telle que,

$${Vect}v_{1} = {Vect}\varepsilon,{Vect}\left( v_{1},v_{2} \right) = {Vect}\left( \varepsilon_{1},\varepsilon_{2} \right),{Vect}\left( v_{1},v_{2},v_{3} \right) = {Vect}\left( \varepsilon_{1},\varepsilon_{2},\varepsilon_{3} \right)$$

**Etape 1 :** $\varepsilon_{1} = \frac{v_{1}}{\left\Vert  v_{1} \right\Vert }$

$$\varepsilon_{1} = \frac{1}{\sqrt{2}}\begin{pmatrix}
1 \\
1 \\
0
\end{pmatrix}$$

**Etape 2 :**

On cherche $\varepsilon_{2}$ tel que $\varepsilon_{1}\bot\varepsilon_{2}$ et ${Vect}\left( v_{1},v_{2} \right) = {Vect}\left( \varepsilon_{1},\varepsilon_{2} \right)$

On cherche $q_{2}$ de la forme $q_{2} = v_{2} - \alpha\varepsilon_{1}$

$\left\langle q_{2},\varepsilon_{1} \right\rangle = 0$ donc $\left\langle v_{2} - \alpha\varepsilon_{1},\varepsilon_{1} \right\rangle = 0$

Donc $\left\langle v_{2},\varepsilon_{1} \right\rangle - \alpha\left\langle \varepsilon_{1},\varepsilon_{1} \right\rangle = 0$ et $\alpha = \left\langle v_{2},\varepsilon_{1} \right\rangle$

Par construction :

$\left\langle q_{2},\ \varepsilon_{1} \right\rangle = 0$ et ${Vect}\left( q_{2},\ \varepsilon_{1} \right) = {Vect}\left( v_{1},v_{2} \right)$

(Car $\dim\left( {Vect}\left( q_{2},\varepsilon_{1} \right) \right) = \dim\left( {Vect}\left( v_{1},v_{2} \right) \right) = 2$

Et ${Vect}\left( q_{2},\varepsilon_{1} \right) \subset {Vect}\left( v_{1},v_{2} \right)$)

$$\varepsilon_{2} = \frac{1}{\left\Vert  q_{2} \right\Vert }q_{2}$$

$$\alpha = \frac{3}{\sqrt{2}}$$

$$q_{2} = \ldots$$

$$\varepsilon_{2} = \sqrt{2}\begin{pmatrix}
\frac{1}{2} \\
 - \frac{1}{2} \\
0
\end{pmatrix}$$

**Etape 3 :**

On cherche $q_{3}$ sous la forme $q_{3} = v_{3} - \beta\varepsilon_{1} - \gamma\varepsilon_{2}$

Avec $\left\langle q_{3},\varepsilon_{1} \right\rangle = \left\langle q_{3},\varepsilon_{2} \right\rangle = 0$

On trouve alors $\beta = \left\langle v_{3},\varepsilon_{1} \right\rangle$ et $\gamma = \left\langle v_{3},\varepsilon_{2} \right\rangle$

On trouve alors 
$$q_{3} = \ldots = \begin{pmatrix}
0 \\
0 \\
1
\end{pmatrix}$$

Donc $\varepsilon_{3} = q_{3}$

**Théorème : Orthogonalisation de Gram-Schmidt**

Soit $\left\lbrack  v_{1},\ldots,v_{p} \right\rbrack $ une famille libre de $\left( E,\left\langle .,. \right\rangle \right)$. La famille $\left\lbrack  q_{1},\ldots,q_{p} \right\rbrack $ définie par récurrence par :

$$\left\lbrack  \begin{array}{r}
q_{1} = v_{1} \\
\forall k \in \left. ⟦2,p \right.⟧,\ q_{k} = v_{k} - \sum_{i = 1}^{k - 1}{\frac{\left\langle v_{k},\ q_{i} \right\rangle}{\left\Vert  q_{i} \right\Vert ^{2}}q_{i}}
\end{array} \right. $$

Vérifie :

$\left\lbrack  q_{1},\ldots,q_{p} \right\rbrack $ est orthogonale

$\forall k \in \left. ⟦1,p \right.⟧$, ${Vect}\left( v_{1},\ldots,v_{p} \right) = {Vect}\left( q_{1},\ldots,q_{k} \right)$

Pour obtenir une famille orthonormale, on pose $\varepsilon_{k} = \frac{q_{k}}{\left\Vert  q_{k} \right\Vert }\forall k$
