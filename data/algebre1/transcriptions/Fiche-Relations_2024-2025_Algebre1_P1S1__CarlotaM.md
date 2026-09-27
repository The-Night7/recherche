---
source: PREING1-S1/Algebre1/Fiche-Relations_2024-2025_Algebre1_P1S1__CarlotaM.pdf
pages: 1-2
transcription: manuelle
---

# Algèbre 1 — Relations binaires et applications

## Définition d'une relation

Une relation $\mathcal R$ de $E$ vers $F$ est définie par une partie $R\subseteq E\times F$, appelée son graphe. Pour $x\in E$ et $y\in F$,

$$x\mathcal R y\iff(x,y)\in R.$$

La fiche étudie ensuite les relations sur un même ensemble $E$.

Exemples : l'inclusion sur $\mathcal P(E)$, la divisibilité sur $\mathbb Z$, l'égalité, les relations $\le$ et $<$ sur les réels. Pour la divisibilité, $m\mathcal R n\iff m\mid n$.

## Propriétés d'une relation

- **Réflexive :** $\forall x\in E,\ x\mathcal R x$.
- **Transitive :** $x\mathcal R y$ et $y\mathcal R z$ impliquent $x\mathcal R z$.
- **Symétrique :** $x\mathcal R y$ implique $y\mathcal R x$.
- **Antisymétrique :** $x\mathcal R y$ et $y\mathcal R x$ impliquent $x=y$.

L'inclusion et $\le$ sont réflexives, transitives et antisymétriques. La relation stricte $<$ n'est pas réflexive.

## Relations d'équivalence

Une relation d'équivalence est réflexive, symétrique et transitive. La classe d'équivalence de $a$ est

$$\operatorname{cl}(a)=[a]=\overline a=\{x\in E:a\mathcal R x\}.$$

Chaque classe est non vide, puisqu'elle contient son représentant. Deux classes sont soit égales, soit disjointes :

$$\operatorname{cl}(x)\ne\operatorname{cl}(y)
\Longrightarrow\operatorname{cl}(x)\cap\operatorname{cl}(y)=\varnothing.$$

Leur réunion est $E$ : $E=\bigcup_{x\in E}\operatorname{cl}(x)$.

**Exemple : congruence modulo 3.** $n\equiv3\pmod3$ signifie que $n-3$ est divisible par 3. On a notamment $4\mathcal R1$, $4\mathcal R7$, $7\mathcal R10$, mais pas $4\mathcal R5$.

## Relations d'ordre

Une relation d'ordre est réflexive, antisymétrique et transitive. On note $(E,\preceq)$ l'ensemble ordonné.

Un ordre est **total** si deux éléments quelconques sont comparables :

$$\forall x,y\in E,\quad x\preceq y\text{ ou }y\preceq x.$$

Exemples d'ordres totaux : $\le$ sur $\mathbb N,\mathbb Z,\mathbb Q,\mathbb R$.

L'inclusion sur $\mathcal P(E)$ n'est généralement pas totale. Sur $\mathbb R^2$, l'ordre produit est défini par

$$ (x,y)\preceq(x',y')\iff x\le x'\text{ et }y\le y'.$$

Les couples $(1,3)$ et $(3,1)$ ne sont pas comparables.

La relation stricte associée à $\preceq$ est donnée par

$$x\prec y\iff x\preceq y\text{ et }x\ne y.$$

## Préordres

Un préordre est une relation réflexive et transitive. Un ordre est un préordre antisymétrique ; une équivalence est un préordre symétrique.

La divisibilité sur $\mathbb Z$ est un préordre, mais n'est ni symétrique ($3\mid9$ et $9\nmid3$), ni antisymétrique ($-1\mid1$ et $1\mid-1$ alors que $-1\ne1$).

> **Rectification de la fiche :** une annotation antérieure attribue l'antisymétrie à la divisibilité sur $\mathbb Z$. Le contre-exemple donné dans la partie « préordres » montre qu'elle est fausse sur $\mathbb Z$ ; la divisibilité est en revanche un ordre sur $\mathbb N$.

## Majorants, minorants et bornes

Pour $A\subseteq E$, $M\in E$ est un majorant si $x\preceq M$ pour tout $x\in A$. De même, $m$ est un minorant si $m\preceq x$ pour tout $x\in A$. La partie $A$ est bornée si elle est majorée et minorée. Un majorant ou minorant n'appartient pas nécessairement à $A$.

Pour l'ordre de divisibilité sur $\mathbb N$, $\{8,10,12\}$ est minoré par $1$ et $2$, et majoré par $120$, $240$, etc.

Un **plus grand élément** est un majorant appartenant à $A$ ; un **plus petit élément** est un minorant appartenant à $A$. Lorsqu'ils existent, ils sont uniques et se notent $\max A$, $\min A$.

La **borne inférieure** est le plus grand minorant, et la **borne supérieure** le plus petit majorant, lorsqu'ils existent. Si le maximum existe, $\sup A=\max A$ ; si le minimum existe, $\inf A=\min A$.

> Les deux dernières égalités de la fiche supposent l'existence du maximum ou du minimum, condition explicitée ici.

## Applications et familles

Une application $f:E\to F$ associe à chaque $x\in E$ un unique $y\in F$, noté $y=f(x)$. $E$ est l'ensemble de départ et $F$ l'ensemble d'arrivée. $y$ est l'image de $x$ ; $x$ est un antécédent de $y$.

L'ensemble des applications de $E$ vers $F$ se note $\mathcal F(E,F)$ ou $F^E$.

Une famille $(x_i)_{i\in I}$ d'éléments de $E$ est une application de $I$ dans $E$, $i\mapsto x_i$. Une suite réelle est une famille indexée par $\mathbb N$.

Deux applications sont égales si elles ont les mêmes ensembles de départ et d'arrivée et les mêmes valeurs en chaque point.

## Applications particulières

**Identité :** $\operatorname{Id}_E:E\to E$, $x\mapsto x$.

**Application constante :** il existe $\alpha\in F$ tel que $f(x)=\alpha$ pour tout $x\in E$.

**Indicatrice d'une partie $A\subseteq E$ :**

$$\mathbf1_A:E\to\{0,1\},\qquad
\mathbf1_A(x)=\begin{cases}1&\text{si }x\in A,\\0&\text{si }x\notin A.\end{cases}$$

## Image directe et image réciproque

Pour $A\subseteq E$,

$$f(A)=\{y\in F:\exists a\in A,\ y=f(a)\}=\{f(a):a\in A\}.$$

L'image de $f$ est $\operatorname{Im}f=f(E)$. Dire que $f$ est à valeurs dans $B$ revient à dire $\operatorname{Im}f\subseteq B$.

Pour $B\subseteq F$, l'image réciproque est

$$f^{-1}(B)=\{x\in E:f(x)\in B\}.$$

Elle contient les antécédents des éléments de $B$.

## Composition

Si $f:E\to F$ et $g:F\to G$, alors $g\circ f:E\to G$ est définie par $(g\circ f)(x)=g(f(x))$.

$$f\circ\operatorname{Id}_E=f,\qquad\operatorname{Id}_F\circ f=f,$$

$$ (h\circ g)\circ f=h\circ(g\circ f).$$

> Le domaine de l'identité à gauche est $F$, ensemble d'arrivée de $f$ ; l'indice $E$ écrit à cet endroit sur la fiche est rectifié.

## Injections, surjections, bijections

- **Injectivité :** $f(x_1)=f(x_2)\Longrightarrow x_1=x_2$.
- **Surjectivité :** $\forall y\in F,\ \exists x\in E,\ f(x)=y$.
- **Bijectivité :** $f$ est à la fois injective et surjective.
