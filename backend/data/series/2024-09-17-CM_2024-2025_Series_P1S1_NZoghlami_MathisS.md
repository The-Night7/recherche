---
title: CM
author: [MathisS]
cyauthor: [NZoghlami]
date: 2024-09-17 01:00:00 +0100
categories: [PREING2 S1,Series]
tags: [PREING2 S1,Series,2024/2025,N. Zoghlami,Mathis S.]
division_title : 2024/2025
math: true
---


# **CM Séries**

Pendant les CM : Des QCM à certains CM comptent dans la note de TD.

## **Introduction**

Séries de Fourier

Séries entières

-   Série de fonctions $\sum_{n}^{}{f_{n}(x)}$

Pour étudier les séries de fonctions, étudier d'abord les séries
numériques et suites de fonctions.

Domaines d'applications : Traitement de signal, étude de convergence
(intervalle de confiance)

Outils pour ce module : Développements limités, comparaisons
(domination, négligeabilité, équivalence)

EDP : équations à dérivée partielle

EDO : équations différentielles ordinaires

## **Rappels :**

### **Négligeabilité :**

$$f =_{a}o(g) \Leftrightarrow \lim_{x \rightarrow a}\frac{f}{g} = 0$$

$$u_{n} = o\left( v_{n} \right) \Leftrightarrow \lim_{n \rightarrow + \infty}\frac{u_{n}}{v_{n}} = 0$$

Soit
$$a \in \overline{\mathbb{R}}\mathbb{= R \cup} \left\{ \pm \infty \right\} $$

On appelle voisinage de $a$ toute partie de $\mathbb{R}$ contenant un
intervalle de la forme :

-   $\rbrack a - \varepsilon;a + \varepsilon\lbrack,\ \varepsilon > 0\ \text{si}\ a\mathbb{\in R}$

-   $\rbrack A; + \infty\lbrack\ \text{si}\ a = + \infty$

-   $\rbrack - \infty;A\lbrack\ \text{si}\ a = - \infty$

$$\lim_{x \rightarrow a}{f(x)} = l \Leftrightarrow f =_{a}l + o(1)$$

$f = o(g)$ et $g = o(h)$ implique $f = o(h)$

$$f = o(g) \Rightarrow \forall\lambda \in \mathbb{R}^{*},\ f = o(\lambda g)\ \text{et}\ \lambda f = o(g)$$

$$f_{1} = o(g),\ f_{2} = o(g) \Rightarrow f_{1} + f_{2} = o(g)$$

$$f_{1} = o\left( g_{1} \right),\ f_{2} = o\left( g_{2} \right) \Rightarrow f_{1}f_{2} = o\left( g_{1}g_{2} \right)$$

$$f = o(g) \Rightarrow fh = o(gh)$$

Composition à droite autorisée

Addition et composition à gauche interdites.

### **Domination :**

$f$ est dominée par $g$ au voisinage de $a$ si $\frac{f}{g}$ est bornée
au voisinage de $a$.

On note $f =_{a}\mathcal{O}(g)\ $

Mêmes propriétés que $o$

### **Equivalence :**

$$f\sim_{a}g \Leftrightarrow \lim_{x \rightarrow a}\frac{f(x)}{g(x)} = 1$$

Relation d'équivalence.

$$\lim_{x \rightarrow a}{f(x)} = l \Leftrightarrow f\sim_{a}l$$

$$f\sim_{a}g \Leftrightarrow f = g + o(g)$$

Produit, inverse, puissance (avec $\alpha$ fixe) et composition à
droite.

Pas d'addition d'équivalences, pas de composition à gauche.

### **Exercice :**

$$\lim_{x \rightarrow 0}\frac{\sqrt[5]{(1 + 6x)} - \sqrt[3]{1 + x}}{3\sin(x) - \ln(1 + x)}$$

$$(1 + 6x)^{\frac{1}{5}} = 1 + \frac{1}{5}(6x) + o\left( x^{2} \right)$$

$$(1 + x)^{\frac{1}{3}} = 1 + \frac{1}{3}(x) + o\left( x^{2} \right)$$

$$N = \frac{6x}{5} - \frac{1}{3}x = \frac{13}{15}x + o\left( x^{2} \right)$$

$$3\sin(x) - \ln(1 + x) = 2x + o\left( x^{2} \right)$$

$$lim = \frac{13}{30}$$

### **Exercice :**

$$\left( \frac{\left( a^{\frac{1}{x}} + b^{\frac{1}{x}} \right)}{2} \right)^{x}$$

$$x \rightarrow + \infty,\forall\ a,b > 0$$

$$\ln(E) = x\left\lbrack \ln\left( a^{\frac{1}{x}} + b^{\frac{1}{x}} \right) - \ln(2) \right\rbrack$$

$$u = \frac{1}{x},\ u \rightarrow 0$$

$$\ln\left( a^{u} + b^{u} \right) = \ln\left( 1 + u\ln(a) + o\left( u^{2} \right) + 1 + u\ln(b) \right)$$

$$\ln\left( 2 + u\left( \ln(a) + \ln(b) \right) + o\left( u^{2} \right) \right)$$

$$\ln\left( 1 + u\left( \frac{\ln(a) + \ln(b)}{2} \right) + o\left( u^{2} \right) \right) + \ln(2) = u\left( \frac{\ln(a) + \ln(b)}{2} \right) + \ln(2) + o\left( u^{2} \right)$$

$$u\left( \frac{\ln(a) + \ln(b)}{2} \right) + o\left( u^{2} \right)$$

$$\frac{\ln(a) + \ln(b)}{2}$$

$$\rightarrow \frac{\ln(a) + \ln(b)}{2}$$

$$R = e^{\frac{\ln(a) + \ln(b)}{2}} = \sqrt{ab}$$

### **Exemple :**

$$S_{n} = \sum_{k = 1}^{n}\frac{1}{k}$$

$$u_{n} = \sum_{k = 1}^{n}{\frac{1}{k} - \ln(n + 1)}$$

$$v_{n} = \sum_{k = 1}^{n}{\frac{1}{k} - \ln(n)}$$

Montrer que $(u_{n})$ et $(v_{n})$ sont adjacentes

$$u_{n + 1} - u_{n} = \frac{1}{n + 1} + \ln\left( \frac{n + 1}{n + 2} \right) = \frac{1}{n + 1} - \ln\left( \frac{n + 2}{n + 1} \right) = \frac{1}{n + 1} - \ln\left( 1 + \frac{1}{n + 1} \right)$$

$$u_{n + 1} - u_{n} = \frac{1}{n + 1} - \ln\left( 1 + \frac{1}{n + 1} \right)$$

Or $\ln(1 + X) \leq X\ (\forall X > - 1)$

$$u_{n + 1} - u_{n} \geq 0$$

$\left( u_{n} \right)$ est croissante.

$$v_{n + 1} - v_{n} = \frac{1}{n + 1} - \ln\left( \frac{n + 1}{n} \right)$$

$$= \frac{1}{n + 1} - \ln\left( 1 + \frac{1}{n} \right)$$

$$= \frac{1}{n + 1} - \left( \frac{1}{n} + o\left( \frac{1}{n} \right) \right) < 0$$

$$\lim_{n \rightarrow + \infty}{u_{n} - v_{n}} = \lim_{n \rightarrow + \infty}{\ln\left( \frac{n}{n + 1} \right)} = 0$$

$(u_{n})$ et $\left( v_{n} \right)$ sont adjacentes et convergent vers
la même limite $\gamma$ (constante d'Euler)

$$v_{n} \rightarrow_{n \rightarrow + \infty}\gamma \Rightarrow v_{n} = \gamma + o(1)$$

$$v_{n}\sim\gamma$$

$$\sum_{k = 1}^{n}\frac{1}{k} = \ln(n) + \gamma + o(1) = \ln(n) + O(1)$$

$$\sum_{k = 1}^{n}\frac{1}{k}\sim_{+ \infty}\ln(n)$$

Série harmonique.$\ $

# **Chapitre 1 : Séries numériques**

$$S = \sum_{n \geq 0}^{}u_{n} = \lim_{n \rightarrow + \infty}{\sum_{k = 0}^{n}u_{k}}$$

$$S_{n} = \sum_{k = 0}^{n}u_{k}$$

## **Définition :**

Soit $\left( u_{n} \right) \in \mathbb{C}^{n}$

$\forall p\mathbb{\in N,}$ on appelle p-ème somme partielle de
$\left( u_{n} \right)$ le nombre

$$U_{p} = \sum_{k = 0}^{p}u_{k}$$

La suite $\left( U_{n} \right)$ est appelée la série de terme général
$u_{n}$ et est notée

$$\sum_{n \geq 0}^{}u_{n}\ \text{ou}\ \sum_{n = 0}^{+ \infty}u_{n}\text{ou}\ \sum_{}^{}u_{n}$$

## **Remarque :**

Mais si les séries ne sont que des suites, pourquoi se doter d'une
théorie des séries ?

La théorie des suites (préing 1) n'est pas suffisante ?

La réponse : NON

En effet, la théorie des suites : à quelle conditions la suite $(u_{n})$
converge.

La théorie des séries : à quelles conditions sur $(u_{n})$ pour que
$\sum_{}^{}u_{n}$ converge.

## **Exemples :**

$$\sum_{n \geq 1}^{}\frac{1}{n^{2}},\ \sum_{}^{}\frac{1}{n},\sum_{n \geq 0}^{}a^{n}\left( a\mathbb{\in R} \right)$$

## **Définition :**

Soit $(u_{n}) \in \mathbb{C}^{n}$. On suppose que $\sum_{}^{}u_{n}$
converge

$$\text{Le nombre}\ \sum_{k = 0}^{+ \infty}u_{k} = \lim_{n \rightarrow + \infty}{\sum_{k = 0}^{n}u_{k}}\ \text{est appelé la somme de la série}\ \sum u_{n}$$

$$\text{Le reste : }\ \forall n\mathbb{\in N,}R_{n} = \sum_{k = n + 1}^{+ \infty}u_{k} = \sum_{k = 0}^{+ \infty}u_{k} - \sum_{k = 0}^{n}u_{k}$$

## **Remarque :**

On parle du reste d'une série seulement dans le cas où elle converge.

## **Séries de référence :**

## **Définition-Théorème :**

Soit $z\mathbb{\in C,}$ la série $\sum z^{n}$, dite série géométrique de
raison $z$, est convergente si et seulement si $ \vert z \vert  < 1$

$$\text{Dans ce cas, }\ \sum_{}^{}z^{n} = \frac{1}{1 - z}$$

## **Démonstration :** Pour $z\mathbb{\in R}$

$$\text{Soit}\ S_{n} ≔ \sum_{k = 0}^{n}z^{n}$$

$$\text{Montrons que},\ \forall \vert z \vert  < 1,\lim_{n \rightarrow + \infty}S_{n} = \frac{1}{1 - z}$$

Or $\left( S_{n} \right)$ est la somme d'une suite géométrique de raison
$z$

$$S_{n} = \frac{1 - z^{n + 1}}{1 - z}\ \text{si}\ z \neq 1,\ n + 1\ \text{sinon}$$

$$S_{n} = \left\{ \begin{array}{r}
\frac{1 - z^{n + 1}}{1 - z}\ \text{si}\ z \neq 1 \\
n + 1\text{ sinon}
\end{array} \right\}$$

Si $z \neq 1$,

$$\lim_{n \rightarrow + \infty}z^{n} = \left\{ \begin{array}{r}
0\ \text{si}\  \vert z \vert  < 1 \\
 + \infty\ \text{si}\ z > 1 \\
\text{pas de limite si}\ z \leq 1
\end{array} \right\}$$

$$\lim_{n \rightarrow + \infty}S_{n} = \left\{ \begin{array}{r}
\frac{1}{1 - z}\ \text{si}\  \vert z \vert  < 1 \\
 + \infty\ \text{si}\ z \geq 1
\end{array} \right\}$$

## **Exercice :**


$$\text{Etudier}\ \sum_{}^{}\frac{1}{n}\ \text{(série harmonique)}$$

On sait que $\ln(1 + X) \leq X\ ;\ \forall X \geq - 1$

$$\frac{1}{k} \geq \ln\left( 1 + \frac{1}{k} \right)\ \forall k \in \mathbb{N}^{*}$$

$$\sum_{k = 1}^{n}\frac{1}{k} \geq \sum_{k = 1}^{n}{\ln\left( 1 + \frac{1}{k} \right)} = \sum_{k = 1}^{n}{\ln\left( \frac{k + 1}{k} \right)} = \sum_{k = 1}^{n}\left( \ln(k + 1) - \ln(k) \right) = \ln(n + 1)$$

$$S_{n} \geq \ln(n + 1)\ \text{or}\lim_{n \rightarrow + \infty}{\ln(n + 1)} = + \infty$$

D'après le théorème de minoration,

$$\lim_{n \rightarrow + \infty}{S_{n}\ } = + \infty$$

$$\sum_{}^{}\frac{1}{n}\ \text{diverge}$$

## **Définition :**

On dit qu'une série $\sum_{}^{}u_{n}$ diverge grossièrement si la suite
$\left( u_{n} \right)$ ne tend pas vers 0.

## **Théorème :** Condition nécessaire de convergence d'une série

Si $\sum_{}^{}u_{n}$ converge, alors
$\left( u_{n} \right) \rightarrow_{n \rightarrow + \infty}0$

Démonstration :

Par hypothèse, $\sum_{}^{}u_{n}$ converge. Conclusion :
$u_{n} \rightarrow 0$

$$\sum_{k = 0}^{+ \infty}u_{k} = S$$

$$u_{n} = \sum_{k = 0}^{n}u_{k} - \sum_{k = 0}^{n - 1}u_{k} = S_{n} - S_{n - 1}$$

On passe à la limite

$$\lim_{n \rightarrow + \infty}u_{n} = S - S = 0$$

**Attention :** La réciproque est fausse en général. Se tromper à ce
sujet, c'est avouer que vous n'avez absolument rien compris de la
théorie des séries.

**Exemple :** Série harmonique

## **Théorème : Critère de Cauchy**

Une série numérique $\sum_{}^{}u_{n}$ converge si et seulement si elle
satisfait le critère de Cauchy :

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall\ }p\mathbb{\in N,\forall}n \geq n_{0},\ \left \vert \sum_{k = n + 1}^{n + p}u_{k} \right \vert \leq \varepsilon$$

Démonstration : $\left( S_{n} \right)$ est une suite alors on applique
le critère de Cauchy sur la suite.

**Exemple :** Série harmonique

$$\sum_{k = n + 1}^{2n}\frac{1}{k} \geq \sum_{k = 1}^{2n}\frac{1}{2n} = \frac{1}{2n}n = \frac{1}{2}$$

Le critère de Cauchy n'est pas vérifié, donc $\sum_{}^{}\frac{1}{n}$
diverge.

## **2. Opérations sur les séries**

### **Théorème**

Soient $\left( u_{n} \right)$ et $\left( v_{n} \right)$ deux suites de
$\mathbb{K}$ ($\mathbb{R}$ ou $\mathbb{C}$).

1.  Multiplication par un scalaire

$\forall\lambda \in \mathbb{K}^{*}$, les séries $\sum u_{n}$ et
$\sum\lambda u_{n}$ sont de même nature.

2.  Somme

Si $\sum_{}^{}u_{n}$ et $\sum_{}^{}v_{n}$ convergent, la série
$\sum_{}^{}{u_{n} + v_{n}}$ converge aussi.

Si $\sum_{}^{}u_{n}$ converge et $\sum_{}^{}v_{n}$ diverge, la série
$\sum_{}^{}{u_{n} + v_{n}}$ diverge

3.  

Dans $\mathbb{C}$, $\sum_{}^{}u_{n}$ converge
$\Leftrightarrow \sum_{}^{}{Re\left( u_{n} \right)}$ et
$\sum_{}^{}{Im(u_{n})}$ convergent.

**Remarque :** L'ensemble des séries est un $\mathbb{K -}e.v.$

En particulier, l'ensemble des séries convergentes est un s.e.v.

### **Attention :**

Si $\sum_{}^{}u_{n}$ et $\sum_{}^{}v_{n}$ divergent toutes les deux, on
ne peux pas conclure en général la nature de $\sum_{}^{}u_{n} + v_{n}$

### **Exemple :**

$$u_{n} = \frac{1}{n},v_{n} = \frac{1}{n},\ \sum_{}^{}{u_{n} + v_{n}}\ \text{diverge}$$

$$u_{n} = \frac{1}{n},v_{n} = - \frac{1}{n},\ \sum_{}^{}{u_{n} + v_{n}}\ \text{converge}$$

# **3. Comparaison série-intégrale et série de Riemann**

## **Définition-Théorème**

Soit $\alpha\mathbb{\in R}$. La série de Riemann
$\sum_{}^{}\frac{1}{n^{\alpha}}$ converge si et seulement si
$\alpha > 1$

$$\sum_{}^{}\frac{1}{n^{\alpha}} = \zeta(\alpha)$$

## **Exemple :**

$$\sum_{}^{}\frac{1}{n^{2}} = \frac{\pi^{2}}{6}$$

$$\sum_{}^{}\frac{1}{n}\ \text{diverge car}\ \alpha = 1$$

## **Démonstration :**

Etudions la convergence de $\sum_{}^{}\frac{1}{n^{\alpha}}$

Si $\alpha \leq 0$,
$\lim_{n \rightarrow + \infty}\frac{1}{n^{\alpha}} \neq 0$

$$\sum_{}^{}\frac{1}{n^{\alpha}}\ \text{diverge grossièrement}$$

Si $\alpha > 0$,

On pose
$f\ :t \rightarrow \frac{1}{t^{\alpha}},\ t \in \rbrack 0\ ; + \infty\lbrack$.
$f$ est décroissante.

$$\forall k \in \mathbb{N}^{*},\ \forall t \in \lbrack k,k + 1\rbrack,\frac{1}{(k + 1)^{\alpha}} \leq \frac{1}{t^{\alpha}} \leq \frac{1}{k^{\alpha}}$$

$$\frac{1}{(k + 1)^{\alpha}} \leq \int_{k}^{k + 1}{\frac{1}{t^{\alpha}}dt} \leq \frac{1}{k^{\alpha}}$$

On somme sur $k$

$$\sum_{k = 1}^{n}\frac{1}{(k + 1)^{\alpha}} \leq \sum_{k = 1}^{n}{\int_{k}^{k + 1}{\frac{1}{t^{\alpha}}dt}} \leq \sum_{k = 1}^{n}\frac{1}{t^{\alpha}}$$

$$\sum_{k = 1}^{n}\frac{1}{(k + 1)^{\alpha}} \leq \int_{1}^{n + 1}{\frac{1}{t^{\alpha}}dt} \leq \sum_{k = 1}^{n}\frac{1}{t^{\alpha}}$$

Si $a \in \rbrack 0\ ;1\lbrack\ $

$$\sum_{k = 1}^{n}\frac{1}{k^{\alpha}} \geq \int_{1}^{n + 1}\frac{dt}{t^{\alpha}} = \frac{1}{1 - \alpha}\left\lbrack t^{1 - \alpha} \right\rbrack_{1}^{n + 1} = \frac{1}{1 - \alpha}\left( (n + 1)^{1 - \alpha} - 1 \right)$$

$$\lim_{n \rightarrow + \infty}{\frac{1}{1 - \alpha}\left( (n + 1)^{1 - \alpha} - 1 \right)} = + \infty$$

$$\text{Donc, d'après le théorème des limites monotones},\ \sum_{}^{}\frac{1}{k^{\alpha}}\ \text{diverge}$$

Si $\alpha = 1$

$$\sum_{k = 1}^{n}\frac{1}{k} \geq \int_{1}^{n + 1}\frac{dt}{t} = \ln(n + 1) \rightarrow + \infty$$

$$\text{De même},\ \sum_{}^{}\frac{1}{k}\ \text{diverge}$$

Si $\alpha > 1$

$$\sum_{k = 1}^{n}\frac{1}{(k + 1)^{\alpha}} \leq \int_{1}^{n + 1}{\frac{1}{t^{\alpha}}dt}$$

Montrons que $\left( S_{n} \right)$ converge en utilisant le théorème de
convergence monotone.

$$S_{n + 1} - S_{n} = \frac{1}{(n + 1)^{\alpha}} \geq 0\ \text{donc}\ S_{n}\ \text{est croissante}$$

$$S_{n} = \sum_{k = 1}^{n}\frac{1}{k^{\alpha}} = 1 + \sum_{k = 1}^{n - 1}\frac{1}{(k + 1)^{\alpha}} \leq 1 + \int_{1}^{n}\frac{dt}{t^{\alpha}} = 1 + \frac{1}{1 - \alpha}\left( n^{1 - \alpha} - 1 \right)$$

$$S_{n} \leq 1 + \frac{n^{1 - \alpha} - 1}{1 - \alpha}$$

$$S_{n} \leq 1 + \frac{1}{\alpha - 1} - \frac{1}{\left( n^{\alpha - 1} \right)(\alpha - 1)} \leq 1 + \frac{1}{\alpha - 1}$$

$$S_{n} \leq 1 + \frac{1}{\alpha - 1}$$

$S_{n}$ est croissante et majorée donc elle converge.

### **Exercice : Série de Bertrand** : cas particulier

$$S_{n} = \sum_{}^{}\frac{1}{n\ln n}$$

Montrer que cette série diverge.

##  **Théorème : Comparaison : Série-Intégrale**

Soient $a\mathbb{\in R}$

$f:\lbrack a\mathbb{; + \infty\lbrack \rightarrow R}$ positive et
décroissante.

$$\sum_{}^{}{f(n)}\ \text{avec}\ n \geq a\ \text{et}\ \int_{a}^{+ \infty}{f(t)dt}\ \text{sont de même nature}$$

## **Démonstration :** $a = 0$

$f$ est décroissante. Soit
$t \in \lbrack k\ ;k + 1\rbrack,k\mathbb{\in N}$

$$f(k + 1) \leq f(t) \leq f(k)$$

On intègre entre $k$ et $k + 1$ (par rapport à $t$)

$$f(k + 1) \leq \int_{k}^{k + 1}{f(t)dt} \leq f(k)$$

On somme :

$$\sum_{k = 0}^{n}{f(k + 1)} \leq \int_{0}^{n + 1}{f(t)dt} \leq \sum_{k = 0}^{n}{f(k)}$$

$$S_{n + 1} \leq \int_{0}^{n + 1}{f(t)dt} \leq S_{n}$$

Alors si $\left( S_{n} \right)$ converge, $\left( S_{n + 1} \right)_{n}$
converge et d'après le théorème d'encadrement,

$$\int_{0}^{n + 1}{f(t)dt}\ \text{converge}$$

## **Exemple :**

$$\sum_{n \geq 2}^{}\frac{1}{n\ln(n)}\ \text{diverge}$$

En effet : On pose

$$f(t) = \frac{1}{t\ln t},\ \forall t \in \lbrack 2; + \infty\lbrack$$

$f$ est positive et décroissante

Soit $t \in \lbrack k\ ;k + 1\rbrack$

$$f(k + 1) \leq f(t) \leq f(k)$$

$$\frac{1}{(k + 1)\ln(k + 1)} \leq \frac{1}{t\ln t} \leq \frac{1}{k\ln k}$$

On intègre :

$$\int_{k}^{k + 1}\frac{dt}{t\ln t} \leq \frac{1}{k\ln k}$$

On somme de $k = 2$ à $k = n$

$$\int_{2}^{n + 1}\frac{dt}{t\ln t} \leq \sum_{k = 2}^{n}\frac{1}{k\ln k}$$

$$\left\lbrack \ln\left( \ln t \right) \right\rbrack_{2}^{n + 1} = \ln\left( \ln(n + 1) \right) - \ln\left( \ln(2) \right)$$

$$S_{n} \geq \ln\left( \ln(n + 1) \right) - \ln\left( \ln(2) \right)$$

Par comparaison,

$$\lim_{n \rightarrow + \infty}S_{n} = + \infty$$

## **Définition : Série absolument convergente**

On dit que $\sum_{}^{}u_{n}$ est absolument convergente ou qu'elle
converge absolument si $\sum_{}^{}\left \vert u_{n} \right \vert$ est convergente.

## **Théorème :**

Toute série absolument convergente est convergente.

## **Démonstration :**

Par hypothèse, $\sum_{}^{}u_{n}$ converge absolument,
$\sum_{}^{}\left \vert u_{n} \right \vert$ converge. Montrer que $\sum_{}^{}u_{n}$
converge.

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}p\mathbb{\in N,\forall}n\mathbb{\in N\ }\text{et}\ n \geq n_{0} \Rightarrow \ \sum_{k = n + 1}^{n + p}\left \vert u_{k} \right \vert \leq \varepsilon$$

$\sum_{}^{}\left \vert u_{n} \right \vert$ vérifie le critère de Cauchy

$$\text{Or}\ \left \vert \sum_{k = n + 1}^{n + p}u_{k} \right \vert \leq \sum_{k = n + 1}^{n + p}\left \vert u_{k} \right \vert \leq \varepsilon$$

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}p\mathbb{\in N,\forall}n\mathbb{\in N\ }\text{et}\ n \geq n_{0} \Rightarrow \ \sum_{k = n + 1}^{n + p}u_{k} \leq \varepsilon$$

Donc $\sum u_{n}$ converge.

**Attention :**

La réciproque est fausse.

## Exemple :

$$\sum_{}^{}\frac{( - 1)^{n}}{n}\ \text{converge (démonstration dans les prochaines semaines)}$$

$$\text{Or}\ \sum_{}^{}\frac{1}{n}\ \text{diverge}$$

## Définition : Série semi-convergente

Une série numérique qui converge mais ne converge pas absolument est
dite semi-convergente.

$$\text{Exemple :}\sum_{}^{}\frac{( - 1)^{n}}{n}$$

# 4.  Série à termes positifs

On s'intéresse à présent aux séries dont le terme général est positif à
partir d'un certain rang, mais les résultats que nous allons démontrer
s'adaptent aisément au cas négatif (en remplaçant croissant par
décroissant, majoré par minoré, $+ \infty$ par $- \infty$, ...

L'essentiel est que le terme général soit de signe constant.

## Théorème :

Une série à termes positifs converge si et seulement si la somme
partielle est majorée.

En cas de divergence, $S_{n} \rightarrow + \infty$

## Démonstration :

$\left( S_{n} \right)$ est croissante car
$S_{n + 1} - S_{n} = u_{n + 1} \geq 0$

Or $\left( S_{n} \right)$ converge alors $\left( S_{n} \right)$ est
majorée.

## Théorème : Comparaison par inégalité

Soient $\sum_{}^{}u_{n}$ et $\sum_{}^{}v_{n}$ deux séries réelles à
termes positifs.

On suppose que $0 \leq u_{n} \leq v_{n}\ \forall n \geq N\mathbb{\in N}$

+ i.  Si $\sum_{}^{}v_{n}$ converge alors $\sum_{}^{}u_{n}$ converge

$$\sum_{k = 0}^{n}u_{k} \leq \sum_{k = 0}^{n}v_{k}$$

+ ii. Si $\sum_{}^{}u_{n}$ diverge alors $\sum_{}^{}v_{n}$ diverge

## Démonstration :

+ i\.

$$0 \leq u_{n} \leq v_{n}$$

On suppose que $\sum_{}^{}v_{n}$ converge

Soit $S_{n} = \sum_{k = 0}^{n}u_{k}$, $T_{n} = \sum_{k = 0}^{n}v_{n}$

$$S_{n} \leq T_{n}$$

Or $\left( T_{n} \right)$ converge, donc $\left( T_{n} \right)$ est
majorée, donc $\left( S_{n} \right)$ est majorée donc
$\left( S_{n} \right)$ converge

+ ii\.

## Exemple :

Etudier la nature des séries suivantes :

$$S_{n} = \sum_{}^{}\frac{1}{n^{3}\left( 2 + \sin\sqrt{n^{3} + n^{2} + 5} \right)}$$

$$T_{n} = \sum_{}^{}\frac{\exp\left( \cos\left( \frac{n!}{\sqrt{n^{2} + 1}} \right) \right)}{\sqrt{n}}$$

$$n^{3}\left( 2 + \sin\sqrt{n^{3} + n^{2} + 5} \right) \geq n^{3}$$

$$\frac{1}{n^{3}\left( 2 + \sin\sqrt{n^{3} + n^{2} + 5} \right)} \leq \frac{1}{n^{3}}$$

$$\text{Or}\ \sum_{}^{}\frac{1}{n^{3}}\ \text{est une série de Riemann avec}\ \alpha = 3 > 1\ \text{donc convergente alors}\ \left( S_{n} \right)\ \text{converge}$$

$$\frac{\exp\left( \cos\left( \frac{n!}{\sqrt{n^{2} + 1}} \right) \right)}{\sqrt{n}} \geq \frac{1}{e}\left( \frac{1}{\sqrt{n}} \right)$$

$$\text{Or}\ \sum_{}^{}\frac{1}{\sqrt{n}}\ \text{est une série de Riemann avec}\ \alpha = \frac{1}{2} < 1\ \text{donc divergente alors}\ \sum_{}^{}\frac{1}{e\sqrt{n}}\ \text{diverge}$$

Par comparaison, $\left( T_{n} \right)$ diverge.

## Théorème : Comparaison par des équivalents

Soient $\sum_{}^{}u_{n}$ et $\sum_{}^{}v_{n}$ deux séries à termes
positifs telles que $u_{n}\sim v_{n}$ alors :

+ i.  Les séries $\sum_{}^{}u_{n}$ et $\sum_{}^{}v_{n}$ sont de même
    nature

+ ii. En cas de convergence, les restes sont équivalents

+ iii. En cas de divergence, les sommes partielles sont équivalentes

## Démonstration :

Par hypothèse, $u_{n}\sim v_{n}$ et
$\forall n,\ u_{n} \geq 0,v_{n} \geq 0$

$$u_{n}\sim v_{n} \Rightarrow \lim_{n \rightarrow + \infty}\frac{u_{n}}{v_{n}} = 1$$

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall\ }n \geq n_{0} \Rightarrow \left \vert \frac{u_{n}}{v_{n}} - 1 \right \vert \leq \varepsilon$$

$$v_{n}(1 - \varepsilon) \leq u_{n} \leq v_{n}(1 + \varepsilon)$$

Si $\sum_{}^{}v_{n}$ converge, alors
$\sum_{}^{}{(1 + \varepsilon)v_{n}}$ converge, alors d'après le théorème
de comparaison par inégalité, $\sum_{}^{}u_{n}$ converge.

Si $\sum_{}^{}v_{n}$ diverge, alors $\sum_{}^{}{(1 - \varepsilon)v_{n}}$
diverge, et d'après le théorème de comparaison par inégalités,
$\sum_{}^{}u_{n}$ diverge.

## Exemple :

Etudier les séries suivantes :

$$S_{n} = \sum_{}^{}\frac{e^{\frac{1}{\sqrt{n}}} - 1}{n^{2}(n - 1)}$$

$$T_{n} = \sum_{}^{}{\ln\left( 1 + \frac{1}{\sqrt{n}} \right)}$$

$$e^{\frac{1}{\sqrt{n}}} - 1\ \sim\frac{1}{\sqrt{n}}$$

$$n^{2}(n - 1)\ \sim\ n^{3}$$

$$\frac{e^{\frac{1}{\sqrt{n}}} - 1}{n^{2}(n - 1)}\ \sim\frac{1}{n^{\frac{7}{2}}}$$

$$\text{Or}\ \sum_{}^{}\frac{1}{n^{\frac{7}{2}}}\ \text{est une série de Riemann avec}\ \alpha = \frac{7}{2} > 1$$

$$\text{Donc}\ \sum_{}^{}\frac{1}{n^{\frac{7}{2}}}\ \text{converge donc}\ \left( S_{n} \right)\ \text{converge}$$

$$\ln\left( 1 + \frac{1}{\sqrt{n}} \right)\ \sim\frac{1}{\sqrt{n}}$$

$$\text{Or}\ \sum_{}^{}\frac{1}{\sqrt{n}}\ \text{est une série de Riemann divergente donc}\ \left( T_{n} \right)\ \text{diverge}$$

## Théorème : Règle de domination

Soient $\sum_{}^{}u_{n}$ et $\sum_{}^{}v_{n}$ deux séries à termes
positifs telles que $u_{n} = Ο\left( v_{n} \right)$

Si $\sum_{}^{}v_{n}$ converge alors $\sum_{}^{}u_{n}$ converge.

## Démonstration :

$u_{n} = Ο\left( v_{n} \right)$ et $\sum_{}^{}v_{n}$ converge. Montrons
que $\sum_{}^{}u_{n}$ converge.

$$u_{n} = Ο\left( v_{n} \right) \Leftrightarrow \exists n_{0}\mathbb{\in N,\ \forall}n \geq n_{0},\ \exists M \in \mathbb{R}^{+},\ u_{n} \leq Mv_{n}$$

Or $\sum_{}^{}{Mv_{n}}$

D'après le théorème de comparaison par inégalité, $\sum_{}^{}u_{n}$
converge.

## Exemple :

$$u_{n} = \frac{e^{\cos(n)}}{n^{\frac{5}{2}}}$$

$$u_{n} = Ο\left( \frac{1}{n^{\frac{5}{2}}} \right)$$

$$\text{Or}\ \sum_{}^{}\frac{1}{n^{\frac{5}{2}}}\ \ \text{converge donc}\ \sum_{}^{}u_{n}\ \text{converge}$$

## Théorème : Règle de « petit o »

Même théorème que le précédent en remplaçant $Ο$ par $ο$

## Exemple :

$$u_{n} = \frac{1}{\left( \ln n \right)^{n}} = \frac{1}{e^{n\ln\left( \ln n \right)}} = ο\left( \frac{1}{n^{2}} \right)$$

$$\text{Or}\ \sum_{}^{}\frac{1}{n^{2}}\ \text{converge donc}\ \sum_{}^{}u_{n}\ \text{converge}$$

## Remarque :

Les deux théorèmes précédents restent vrais si $\sum_{}^{}u_{n}$ est à
valeurs complexes, il suffit de remplacer $u_{n}$ par
$\left \vert u_{n} \right \vert$

## Corollaire : Règle de « $n^{\alpha}$ » ou Règle de Riemann

Soient $\sum_{}^{}u_{n}$ une série à termes positifs.

Si $\lim_{n \rightarrow + \infty}{n^{\alpha}u_{n}} = 0$ et $\alpha > 1$
alors $\sum_{}^{}u_{n}$ converge.

Si $\lim_{n \rightarrow + \infty}{n^{\alpha}u_{n}} = + \infty$ et
$\alpha \leq 1$ alors $\sum_{}^{}u_{n}$ diverge.

## Démonstration :

+ i.  On a
    $\lim_{n \rightarrow + \infty}{n^{\alpha}u_{n}} = 0 \Leftrightarrow u_{n} = ο\left( \frac{1}{n^{\alpha}} \right)$
    or $\sum_{}^{}\frac{1}{n^{\alpha}}$ converge donc $\sum_{}^{}u_{n}$
    converge.

+ ii. $\lim_{n \rightarrow + \infty}{n^{\alpha}u_{n}} = + \infty \Leftrightarrow \exists n_{0}\mathbb{\in N,\forall\ }n \geq n_{0},\ n^{\alpha}u_{n} \geq 1$

$$\forall n \geq n_{0},\ u_{n} \geq \frac{1}{n^{\alpha}}\ \text{or}\ \alpha \leq 1\ \text{alors}\ \sum_{}^{}\frac{1}{n^{\alpha}}\ \text{diverge donc, par inégalité,}\sum_{}^{}u_{n}\ \text{diverge}$$

# 5.  Règle d'Alembert et Règle de Cauchy

## Théorème : Règle d'Alembert

Soit $\left( u_{n} \right)$ une suite d'éléments de $\mathbb{K}$
($\mathbb{R}$ ou $\mathbb{C}$). On suppose que $u_{n} \neq 0$ à partir
d'un certain rang et
$\lim_{n \rightarrow + \infty}\left \vert \frac{u_{n + 1}}{u_{n}} \right \vert = l \in \overline{\mathbb{R}_{+}}$

+ i.  Si $l < 1$, alors $\sum_{}^{}\left \vert u_{n} \right \vert$ converge, donc
    $\sum_{}^{}u_{n}$ converge.

+ ii. Si $l > 1$, alors $\sum_{}^{}u_{n}$ diverge grossièrement.

## Attention : $l = 1$ est le cas douteux de la règle
d'Alembert. On ne peut pas conclure.

## Exemple :

Si on applique la règle d'Alembert à la série de Riemann on trouve le
cas douteux.

$$\left \vert \frac{u_{n + 1}}{u_{n}} \right \vert = \frac{u_{n + 1}}{u_{n}} = \left( \frac{n}{n + 1} \right)^{\alpha} \rightarrow 1$$

## Démonstration :

+ i\.

$$\text{On suppose que }\lim_{n \rightarrow + \infty}\left \vert \frac{u_{n + 1}}{u_{n}} \right \vert = l < 1$$

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall\ }n \geq n_{0},\ \left \vert \frac{u_{n + 1}}{u_{n}} \right \vert < l + \varepsilon = \frac{(l + \varepsilon)^{n + 1}}{(l + \varepsilon)^{n}}$$

Soit $\varepsilon = \frac{1 - l}{2}$

$$\frac{\left \vert u_{n + 1} \right \vert}{(l + \varepsilon)^{n + 1}} < \frac{\left \vert u_{n} \right \vert}{(l + \varepsilon)^{n}} \Rightarrow \left( \frac{\left \vert u_{n} \right \vert}{(l + \varepsilon)^{n}} \right)\ \text{est décroissante et minorée par}\ 0$$

$$\left( \frac{\left \vert u_{n} \right \vert}{(l + \varepsilon)^{n}} \right)\ \text{est convergente donc bornée}$$

$$\left \vert u_{n} \right \vert = Ο\left( (l + \varepsilon)^{n} \right)$$

$$\text{Or}\ \sum_{}^{}(l + \varepsilon)^{n}\ \text{converge car}\ 0 < l + \varepsilon < 1$$

$$\sum_{}^{}\left \vert u_{n} \right \vert\ \text{converge donc}\ \sum_{}^{}u_{n}\ \text{converge absolument}$$

+ ii\.

$$\text{On suppose que }\lim_{n \rightarrow + \infty}\left \vert \frac{u_{n + 1}}{u_{n}} \right \vert = l > 1$$

$$\exists n_{0}\mathbb{\in N,\forall\ }n \geq n_{0},\ \left \vert \frac{u_{n + 1}}{u_{n}} \right \vert \geq l - \varepsilon > 1$$

$\left( \left \vert u_{n} \right \vert \right)$ est croissante et strictement
positive donc $\left \vert u_{n} \right \vert$ ne tend pas vers 0.

$$\sum_{}^{}u_{n}\ \text{diverge grossièrement}$$

## Exemple :

$$\sum_{}^{}\frac{n^{2}}{3^{n}}\ \text{converge}$$

$$\sum_{}^{}\frac{z^{n}}{n!}\ \text{converge}$$

En effet,

$$u_{n} ≔ \frac{n^{2}}{3^{n}},\ \left \vert \frac{u_{n + 1}}{u_{n}} \right \vert = \frac{u_{n + 1}}{u_{n}} = \left( \frac{n + 1}{n} \right)^{2} \times \frac{1}{3} \rightarrow \frac{1}{3} < 1$$

Converge d'après la règle d'Alembert

$$u_{n} ≔ \frac{z^{n}}{n!}$$

$$\left \vert \frac{u_{n + 1}}{u_{n}} \right \vert = \frac{\left \vert z^{n + 1} \right \vert}{\left \vert z_{n} \right \vert} \times \frac{n!}{(n + 1)!} = \frac{ \vert z \vert }{n + 1} \rightarrow 0$$

Converge d'après la règle d'Alembert.

## Note :

$$\sum_{n \geq 0}^{}\frac{z^{n}}{n!} = e^{z}$$

Appliquée aux factorielles, exponentielles et puissance.

## Théorème : Règle de Cauchy

Soit $\left( u_{n} \right)$ une suite d'éléments de $\mathbb{K}$.

Supposons que
$\lim_{n \rightarrow + \infty}\sqrt[n]{\left \vert u_{n} \right \vert} = l$

+ i.  Si $l < 1$ alors $\sum_{}^{}u_{n}$ converge absolument

+ ii. Si $l > 1$ alors $\sum_{}^{}u_{n}$ diverge grossièrement

## Démonstration :

On suppose que
$\lim_{n \rightarrow + \infty}\sqrt[n]{\left \vert u_{n} \right \vert} = l < 1$

$$\exists a \in \mathbb{R}_{+},\ l < a < 1$$

$$\Rightarrow \sqrt[n]{\left \vert u_{n} \right \vert} \leq a$$

$$\Rightarrow \left \vert u_{n} \right \vert \leq a^{n}$$

Or $\sum_{}^{}a^{n}$ converge donc $\sum_{}^{}u_{n}$ converge absolument

## Exemple :

$$\sum_{}^{}\frac{1}{\left( \ln n \right)^{n}}$$

On applique la règle de Cauchy.

$$\sqrt[n]{\left \vert u_{n} \right \vert} = \sqrt[n]{u_{n}} = \frac{1}{\ln(n)} \rightarrow 0 < 1$$

$\sum_{}^{}u_{n}$ converge absolument.

## Exemple :

$$\sum_{n \geq 0}^{}\left( \frac{n}{n + 1} \right)^{n^{2}}$$

On applique la règle de Cauchy

$$\sqrt[n]{u_{n}} = \left( \frac{n}{n + 1} \right)^{n} = \frac{1}{\left( 1 + \frac{1}{n} \right)^{n}} \rightarrow \frac{1}{e} < 1$$

$\sum_{}^{}u_{n}$ converge absolument.

## Exemple :

$$\sum_{}^{}\frac{n^{\ln n}}{\left( \ln n \right)^{n}}$$

On applique la règle de Cauchy

$$\sqrt[n]{\frac{n^{\ln n}}{\left( \ln n \right)^{n}}} = \frac{n^{\frac{\ln n}{n}}}{\ln n} = \frac{e^{\frac{\ln(n)^{2}}{n}}}{\ln n} \rightarrow 0$$

$\sum_{}^{}u_{n}$ converge absolument.

## Remarque :

Dans le cas douteux $(l = 1)$ si on a testé avec règle d'Alembert, pas
la peine de tester la règle de Cauchy.


# 6.  **Séries alternées**

## **Définition : Série alternée**

On appelle série alternée toute série de la forme

$$\sum_{}^{}{( - 1)^{n}a_{n}}\ \text{avec}\ \left( a_{n} \right)\ \text{suite réelle de signe constant}$$

## **Exemples :**

$$\sum_{}^{}\frac{( - 1)^{n}}{n};\sum_{}^{}\frac{( - 1)^{n}e^{- n}}{n^{2} + 2}$$

## **Théorème : Critère spécial des séries alternées (CSSA) ou Critère de Leibniz**

Soit $\left( a_{n} \right)$ une suite à termes positifs décroissante et
de limite nulle.

Alors,

$$\sum_{}^{}{( - 1)^{n}a_{n}}\ \text{converge}$$

De plus,

Sa somme $S$ vérifie $S_{2n + 1} \leq S \leq S_{2n}$

Son reste $R_{n}$ vérifie $\left\vert  R_{n} \right\vert  \leq a_{n + 1}$

## **Démonstration :**

Pour montrer que $\sum_{}^{}{( - 1)^{n}a_{n}}$ converge, il suffit de
montrer que $\left( S_{2n + 1} \right)$ et $\left( S_{2n} \right)$ sont
adjacentes.

$$S_{2n + 3} - S_{2n + 1} = a_{2n + 2} - a_{2n + 3} \geq 0$$

Alors $\left( S_{2n + 1} \right)$ est croissante.

$$S_{2n + 2} - S_{2n} = a_{2n + 2} - a_{2n + 1} \leq 0$$

Alors $\left( S_{2n} \right)$ est décroissante.

$$\lim_{n \rightarrow + \infty}{s_{2n + 1} - S_{2n}} = \lim_{n \rightarrow + \infty}\left( - a_{2n + 1} \right) = 0$$

Donc $\left( S_{2n + 1} \right)$ et $\left( S_{2n} \right)$ sont
adjacentes, elles convergent vers la même limite $S$

$$S_{2n + 1} \leq S \leq S_{2n}$$

D'après le théorème des suites extraites, $\left( S_{n} \right)$
converge.

$$\left\vert  R_{2n} \right\vert  = \left\vert  S - S_{2n} \right\vert  \leq \left\lbrack S_{2n - 1} - S_{2n} \right\vert  = a_{2n + 1}$$

$$\left\vert  R_{2n + 1} \right\vert  = \left\vert  S - S_{2n + 1} \right\vert  \leq \left\vert  S_{2n + 2} - S_{2n + 1} \right\vert  = a_{2n + 2}$$

## **Définition-Théorème : Série de Riemann alternée**

$$\text{La série alternée}\ \sum_{}^{}\frac{( - 1)^{n}}{n^{\alpha}}\ \text{est une série de Riemann alternée}$$

Elle converge si et seulement si $\alpha > 0$

## **Démonstration :**

Si $\alpha \leq 0$, la série diverge grossièrement.

Si $\alpha > 0$,

$$\sum_{}^{}\frac{( - 1)^{n}}{n^{\alpha}}$$

Est une série alternée avec $a_{n} = \frac{1}{n^{\alpha}}$

Or $\left( a_{n} \right) \rightarrow 0\ \text{car}\ \alpha > 0$

$\left( a_{n} \right)$ est décroissante car
$\left( n^{\alpha} \right)_{n}$ est croissante.

D'après le CSSA,

$$\sum_{}^{}\frac{( - 1)^{n}}{n^{\alpha}}\ \text{converge}$$

## **Attention :**

$$\sum_{}^{}\frac{( - 1)^{n}}{n^{\alpha}}\ \text{est semi-convergente si}\ \alpha \in \rbrack 0;1\rbrack$$

## **Remarque :**

Généralement, il ne faut pas appliquer le CSSA directement quand on
étudie une série alternée.

En effet, l'hypothèse de décroissance de $\left( a_{n} \right)$ peut
être difficile à vérifier, voire fausse.

## **Exemple :**

$$\sum_{}^{}\frac{( - 1)^{n}}{n^{\frac{3}{4}} + n^{\frac{1}{4}}\sin\left( \pi^{n} \right)}$$

La monotonie de la suite
$a_{n} = \frac{1}{n^{\frac{3}{4}} + n^{\frac{1}{4}}\sin\left( \pi^{n} \right)}$
est difficile à étudier donc le CSSA ne nous sera donc pas utile à
appliquer.

Dans ce cas, un DL au terme général.

$$u_{n} = \frac{( - 1)^{n}}{n^{\frac{3}{4}} + n^{\frac{1}{4}}\sin\left( \pi^{n} \right)}$$

$$u_{n} = \frac{( - 1)^{n}}{n^{\frac{3}{4}}}\left( \frac{1}{1 + \frac{\sin\left( \pi^{n} \right)}{\sqrt{n}}} \right)$$

$$u_{n} = \frac{( - 1)^{n}}{n^{\frac{3}{4}}}\left( 1 + Ο\left( \frac{1}{\sqrt{n}} \right) \right)$$

$$u_{n} = \frac{( - 1)^{n}}{n^{\frac{3}{4}}} + Ο\left( \frac{1}{n^{\frac{5}{4}}} \right)$$

$$u_{n} = b_{n} + c_{n}$$

$$\sum_{}^{}b_{n}\ \text{converge car c'est une série de Riemann alternée avec}\ \alpha = \frac{3}{4} > 0$$

$$\sum_{}^{}{Ο\left( \frac{1}{n^{\frac{5}{4}}} \right)}\ \text{converge car}\ \sum_{}^{}\frac{1}{n^{\frac{5}{4}}}\ \text{converge car série de Riemann avec}\ \alpha = \frac{5}{4} > 1$$

$$\sum_{}^{}\frac{( - 1)^{n}}{n^{\frac{3}{4}} + n^{\frac{1}{4}}\sin\left( \pi^{n} \right)}\ \text{converge car}\ \sum_{}^{}b_{n}\ \text{et}\ \sum_{}^{}c_{n}\ \text{convergent}$$

## **Exemple :**

$$\sum_{}^{}u_{n}$$

$$u_{n} = \frac{( - 1)^{n}}{\sqrt{n} + ( - 1)^{n}}$$

$$u_{n} = \frac{( - 1)^{n}}{\sqrt{n}}\left( \frac{1}{1 + \frac{( - 1)^{n}}{\sqrt{n}}} \right)$$

$$u_{n} = \frac{( - 1)^{n}}{\sqrt{n}}\left( 1 - \frac{1}{\sqrt{n}} + Ο\left( \frac{1}{n} \right) \right)$$

$$u_{n} = \frac{( - 1)^{n}}{\sqrt{n}} - \frac{1}{n} + Ο\left( \frac{1}{n^{\frac{3}{2}}} \right)$$

$$u_{n} = b_{n} + c_{n} + d_{n}$$

$$\sum_{}^{}b_{n}\ \text{converge car c'est une série de Riemann alternée avec}\ \alpha = \frac{1}{2} > 0$$

$$\sum_{}^{}c_{n}\ \text{diverge car c'est une série de Riemann avec}\ \alpha = 1$$

$$\sum_{}^{}{Ο\left( \frac{1}{n^{\frac{3}{2}}} \right)}\ \text{converge car}\ \sum_{}^{}\frac{1}{n^{\frac{3}{2}}}\ \text{converge car série de Riemann avec}\ \alpha = \frac{3}{2} > 1$$

$$\sum_{}^{}u_{n}\ \text{diverge}$$

## **Attention :**

Dans le théorème de comparaison par équivalence, on a précisé que
$\left( u_{n} \right)$ et $\left( v_{n} \right)$ sont à termes positifs
(signe constant).

Dans le cas des séries à termes quelconques, le critère d'équivalence
est faux.

Voici un contre-exemple.

# 7.  **Produit de Cauchy**

## **Définition :**

$$\sum_{i \geq 0}^{}a_{i},\sum_{i \geq 0}^{}b_{i}\ \text{deux séries}$$

On appelle produit de Cauchy la série :

$$\sum_{k \geq 0}^{}C_{k},\ \text{où}\ C_{k} = \sum_{i = 0}^{k}{a_{i}b_{k - i}}$$

## **Remarque :**

Une autre façon d'écrire le coefficient $C_{k}$ est

$$C_{k} = \sum_{i + j = k}^{}{a_{i}b_{j}}$$

## **Théorème :**

Si $\sum_{}^{}a_{i}$ et $\sum_{}^{}b_{i}$ sont absolument convergentes,
alors le produit de Cauchy est absolument convergent.

On a :

$$\sum_{k \geq 0}^{}C_{k} = \left( \sum_{i \geq 0}^{}a_{i} \right)\left( \sum_{i \geq 0}^{}b_{i} \right)$$

## **Démonstration :** Voir Teams

## **Exemple :**

$$e^{a + b} = e^{a}e^{b}$$

En effet,

$$e^{a} = \sum_{n \geq 0}^{}\frac{a^{n}}{n!},\ e^{b} = \sum_{n \geq 0}^{}\frac{b^{n}}{n!}$$

$$e^{a}e^{b} = \sum_{n \geq 0}^{}\frac{a^{n}}{n!}\sum_{n \geq 0}^{}\frac{b^{n}}{n!}$$

Or $\sum_{}^{}\frac{a^{n}}{n!},\sum_{}^{}\frac{b^{n}}{n!}$ Sont
absolument convergentes.

D'après le théorème :

$$e^{a}e^{b} = \sum_{n \geq 0}^{}\frac{a^{n}}{n!}\sum_{n \geq 0}^{}\frac{b^{n}}{n!} = \sum_{k \geq 0}^{}\left( \sum_{n = 0}^{k}{a_{n}b_{k - n}} \right) = \sum_{k \geq 0}^{}\left( \sum_{n = 0}^{k}\frac{a^{n}}{n!} \times \frac{b^{k - n}}{(k - n)!} \right) = \sum_{n \geq 0}^{}\left( \sum_{k = 0}^{n}\frac{a^{k}}{k!} \times \frac{b^{n - k}}{(n - k)!} \right) = \sum_{n \geq 0}^{}\left( \sum_{k = 0}^{n}\frac{a^{k}}{k!} \times \frac{b^{n - k}}{(n - k)!} \times \frac{n!}{n!} \right) = \sum_{n \geq 0}^{}\left( \frac{1}{n!}\sum_{k = 0}^{n}{\left( \begin{array}{r}
n \\
k
\end{array} \right)a^{k}b^{n - k}} \right) = \sum_{n \geq 0}^{}\frac{(a + b)^{n}}{n!}$$

## **Attention :**

Si $\sum_{}^{}a_{n}$ et $\sum_{}^{}b_{n}$ ne sont pas absolument
convergentes mais seulement convergentes alors la série produit de
Cauchy peut être divergente.

## **Contre-exemple :**

$$a_{i} = b_{i} = \frac{( - 1)^{i}}{\sqrt{1 + i}}$$

$$C_{n} = \sum_{k = 0}^{n}{a_{n}b_{n - k}} = \sum_{k = 0}^{n}\frac{1}{\sqrt{(1 + k)(1 + n - k)}}$$

$$(1 + k)(1 + n - k) = 1 + n - k + k + kn - k^{2}$$

Or
$(1 + x)(1 + n - x) = 1 + n - x + x + nx - x^{2} = - x^{2} + nx + (n + 1)$

Rappel : Soit $f(x) = ax^{2} + bx + c$

Si $a < 0$, alors
$\forall x\mathbb{\in R,\ }f(x) < = f\left( - \frac{b}{2a} \right)$

$$(1 + x)(1 + n - x) \leq - \left( \frac{n}{2} \right)^{2} + \frac{n^{2}}{2} + n + 1 = \frac{n^{2}}{4} + n + 1 = \left( \frac{n}{2} + 1 \right)^{2}$$

$$(1 + x)(1 + n - x) \leq \frac{1}{4}(n + 2)^{2}$$

$$\sqrt{(1 + x)(1 + n - x)} \leq \frac{1}{2}(n + 2)$$

$$\frac{1}{\sqrt{(1 + x)(1 + n - x)}} \geq \frac{2}{n + 2}$$

$$C_{n} \geq \sum_{k = 1}^{n}\frac{2}{n + 2}$$

$$C_{n} \geq \frac{2(n + 1)}{n + 2} \rightarrow_{+ \infty}2$$

$$\sum_{}^{}C_{n}\ \text{diverge grossièrement}$$

# 8.  **Sommation d'Abel**

## **Théorème : « Critère d'Abel » ou « Sommation d'Abel »**

Soient $\left( a_{n} \right)$ et $\left( b_{n} \right)$ deux suites
telles que

1.  $\left( a_{n} \right)$ et décroissante et tend vers 0

2.  La somme partielle $\sum_{}^{}b_{k}$ est bornée

Alors $\sum_{}^{}{a_{n}b_{n}}$ converge.

## **Remarque :**

Le critère spécial des séries alternées est un cas particulier de la
sommation d'Abel.

En effet, si $b_{n} = ( - 1)^{n}$, alors
$\left\vert  \sum_{k = 0}^{n}b_{k} \right\vert  \leq 1$

Si $\left( a_{n} \right)$ est décroissante et tend vers 0, alors
$\sum_{}^{}{a_{n}b_{n}}$ converge.

## **Application :**

Séries de Fourier.

$$\sum_{}^{}{a_{n}e^{in\theta}\ },\sum_{}^{}{a_{n}\cos(n\theta)},\sum_{}^{}{a_{n}\sin(n\theta)}\ \text{sont des séries de Fourier}$$

Si $\left( a_{n} \right)$ est décroissante et tend vers 0 alors les
séries de Fourier convergent.

## **Exemple :**

$$\sum_{n \geq 0}^{}\frac{\sin(n\theta)}{\sqrt{n + 1}}\ \text{converge}\ \forall\theta\mathbb{\in R}$$

En effet, on applique le théorème « Sommation d'Abel »

$$a_{n} ≔ \frac{1}{\sqrt{n + 1}}\ \text{est décroissante et tend vers}\ 0$$

Reste à montrer que $\sum_{k = 0}^{n}b_{k}$ est bornée avec
$b_{k} = \sin(k\theta)$

$$S_{n} ≔ \sum_{k = 0}^{n}{\sin(k\theta)} = Im\left( \sum_{k = 0}^{n}e^{ik\theta} \right)$$

Si $\theta \neq k\pi$

$$\sum_{k = 0}^{n}e^{ik\theta} = \sum_{k = 0}^{n}\left( e^{i\theta} \right)^{k} = \frac{1 - e^{i\theta(n + 1)}}{1 - e^{i\theta}} = \frac{e^{i\theta\left( \frac{n + 1}{2} \right)}}{e^{\frac{i\theta}{2}}} \times \frac{e^{- \frac{i\theta(n + 1)}{2}} - e^{\frac{i\theta(n + 1)}{2}}}{e^{- \frac{i\theta}{2}} - e^{\frac{i\theta}{2}}} = e^{\frac{in\theta}{2}}\frac{\sin\left( \frac{(n + 1)\theta}{2} \right)}{\sin\left( \frac{\theta}{2} \right)}$$

$$S_{n} = \sin\left( \frac{n\theta}{2} \right) \times \frac{\sin\left( \frac{(n + 1)\theta}{2} \right)}{\sin\left( \frac{\theta}{2} \right)}$$

$$\left\vert  S_{n} \right\vert  \leq \frac{1}{\sin\left( \frac{\theta}{2} \right)} \Rightarrow \left( S_{n} \right)\ \text{est bornée}$$

Si $\theta = k\pi,\ S_{n}\ \text{est nulle donc bornée}$

$$\left( S_{n} \right)\ \text{est bornée}\ \forall\theta$$

$$\sum_{}^{}\frac{\sin(n\theta)}{\sqrt{n + 1}}\ \text{cv}$$

## **Chapitre 2 : Suites de fonctions**

Dans ce chapitre, les fonctions étudiées seront définies sur un
intervalle $I$ de $\mathbb{R}$ et à valeurs dans $\mathbb{R}$ ou
$\mathbb{C}$.

I.  **Mode de convergence**

On considère une suite de fonctions $\left( f_{n} \right)$ définie sur
$I$ et à valeurs dans $\mathbb{K}$ ($\mathbb{R}$ ou $\mathbb{C}$).

1.  **Convergence simple**

## **Définition :**

On dit que la suite $\left( f_{n} \right)$ converge simplement vers la
fonction $f$ sur $I$, si

$$\forall x \in I,f_{n}(x) \rightarrow_{n \rightarrow + \infty}f(x)$$

Autrement dit,

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}n \geq n_{0},\left\vert  f_{n}(x) - f(x) \right\vert  \leq \varepsilon$$

On note :

$$f_{n} \rightarrow_{n \rightarrow + \infty}^{cs}f$$

## **Attention :**

Dans l'expression ci-dessus, le rang $n_{0}$ dépend de $\varepsilon$ et
$x$.

## **Remarque :**

En pratique, prouver la convergence simple d'une suite de fonctions
revient donc à montrer la convergence de $\left( f_{n}(x) \right)_{n}$
avec $x \in I$ fixé.

On parle donc d'une convergence « ponctuelle ».

La limite est unique $\forall x \in I$.

## **Exemple :**

### 1\.

Soit
$f_{n}\ :\lbrack 0\ ;1\rbrack\mathbb{\rightarrow R,\ }x \rightarrow x^{n}$

$$f_{n} \rightarrow f,\ f(x) = \left\{ \begin{array}{r}
1\ \text{si}\ x = 1 \\
0\ \text{si}\ x \in \lbrack 0;1\lbrack
\end{array} \right\}$$

### 2\.

$$f_{n}:\mathbb{R}^{+}\mathbb{\rightarrow R}$$

$$x \rightarrow \frac{nx}{nx + 1}$$

$$f_{n} \rightarrow f,\ f(x) = \left\{ \begin{array}{r}
1\ \text{si}\ x \in \mathbb{R}_{+}^{*} \\
0\ \text{si}\ x = 0
\end{array} \right\}$$

### 3\.

$$f_{n}(x) = \sqrt{x^{2} + \frac{1}{n}},\ x\mathbb{\in R}$$

Soit $x\mathbb{\in R,\ }f_{n}(x) \rightarrow \vert x\vert $

$$f_{n} \rightarrow_{cs}f,\ \text{avec}\ f(x) = \vert x\vert $$

### 4\.

$$f_{n}:\lbrack 0;1\rbrack\mathbb{\rightarrow R}$$

$$ x \rightarrow \left\{ \begin{array}{r} 1 - nx\ \text{si}\ x \in \left\lbrack 0;\frac{1}{n} \right\rbrack \\ 0\ \text{si}\ x \in \left\lbrack \frac{1}{n};1 \right\rbrack \end{array} \right. $$

Si $x = 0$,

$$f_{n}(x) = 1$$

Si $x \in \rbrack 0\ ;1\rbrack\ $

$$\exists n_{0}\mathbb{\in N,\forall\ }n \geq n_{0},x > \frac{1}{n_{0}} \geq \frac{1}{n},\ f_{n}(x) = 0$$

$$ f_{n} \rightarrow_{cs}f,\ \text{avec}\ f(x) = \left\{ \begin{array}{r} 0\ \text{si}\ x \in \rbrack 0;1\rbrack\  \\ 1\ \text{si}\ x = 0 \end{array} \right. $$

### 5\.

$$f_{n}:\lbrack 0;1\rbrack\mathbb{\rightarrow R}$$

$$x \rightarrow \frac{n}{nx + 1}$$

Soit $x \in \lbrack 0\ ;1\rbrack$

Si $x \neq 0$

$$f_{n}(x)\ \sim\frac{n}{nx} = \frac{1}{x}$$

Si $x = 0$,

$$f_{n}(0) = n \rightarrow + \infty$$

$$\left( f_{n} \right)_{n}\ \text{ne converge pas simplement sur}\ \lbrack 0;1\rbrack$$

## **Proposition :**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$ qui converge simplement sur $I$.

Alors, pour tout sous-ensemble $I^{'} \subset I$, la suite converge
simplement.

## **Remarque :** La réciproque est fausse

## **Définition :** Domaine de convergence

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$. On appelle **domaine de convergence** de
$\left( f_{n} \right)$ l'ensemble des $x \in I$ pour lesquels la suite
numérique $\left( f_{n}(x) \right)$ converge.

## **Exemples :**

### 1\.
Le domaine de convergence de $f_{n}(x) = e^{x - \frac{1}{n}}$ est
$\mathbb{R}$

### 2\.

Le domaine de convergence de la suite de fonctions $f_{n}(x) = x^{n}$
est $\rbrack - 1;1\rbrack$

### 3\.

Le domaine de convergence de la suite de fonctions $f_{n}(x) = nx$ est
$ \{ 0 \} $

## **Proposition :**

La convergence simple est stable par :

-   Combinaisons linéaires : si $\left( f_{n} \right)$ et
    $\left( g_{n} \right)$ convergent simplement sur $I$ vers $f$ et $g$
    et soit $\lambda\mathbb{\in R}$ alors la suite de fonctions
    $\left( f_{n} + \lambda g_{n} \right)_{n}$ converge simplement sur
    $I$ vers $f + \lambda g$

-   Multiplication interne : si $\left( f_{n} \right)$ et
    $\left( g_{n} \right)$ convergent simplement sur $I$ vers $f$ et $g$
    alors la suite de fonctions $\left( f_{n}g_{n} \right)$ converge
    simplement sur $I$ vers $fg$

# 2.  **Convergence uniforme**

## **Remarque :**

Dans le mode de convergence simple, le rang $n_{0}$ dépend de
$\varepsilon$ et $x$. En exigeant que $n_{0}$ soit indépendant de $x$,
on obtient un mode de convergence plus restrictif appelé convergence
uniforme.

## **Définition :** Convergence uniforme

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$.

$\left( f_{n} \right)$ converge uniformément sur $I$ si
$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall\ }n \geq n_{0},\forall x \in I,\left\vert  f_{n}(x) - f(x) \right\vert  < \varepsilon$,
on note

$f_{n} \rightarrow_{cu}f$ sur $I$.

## **Remarques :**

-   La convergence uniforme se traduit géométriquement par l'existence
    d'un certain rang $n_{0}$ à partir duquel $f_{n}$ est comprise entre
    $f - \varepsilon$ et $f + \varepsilon$.

-   Le mode de convergence dépend essentiellement de l'intervalle
    considéré et c'est pour cela dire « $\left( f_{n} \right)$ converge
    uniformément » est imprécis.

## **Proposition :**

Si $\left( f_{n} \right)$ converge uniformément sur $I$ vers $f$ alors
elle converge simplement sur $I$ vers $f$.

## **Remarque :** La réciproque est fausse (nous verrons un
exemple plus tard).

3.  **Critère de convergence uniforme**

De la définition de la convergence uniforme, on déduit immédiatement le
critère de convergence uniforme.

## **Proposition :**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$ et $f$ une fonction de $I$ dans $\mathbb{K}$.

Pour chaque $n$, on note
$\varphi_{n} = \sup_{x \in I}\left\vert  f_{n}(x) - f(x) \right\vert  = \left\\vert  f_{n} - f \right\\vert _{\infty}$

Pour que la suite $\left( f_{n} \right)$ converge uniformément vers $f$
sur $I$, il faut et il suffit que la suite $\left( \varphi_{n} \right)$
converge vers 0.

Autrement dit,

$$f_{n} \rightarrow_{cu}f\ \text{sur}\ I \Leftrightarrow \varphi_{n} = \left\\vert  f_{n} - f \right\\vert _{\infty} \rightarrow_{n \rightarrow + \infty}0$$

## **Démonstration :**

$$\forall x \in I,\ \left\vert  f_{n}(x) - f(x) \right\vert  \leq \varepsilon \Leftrightarrow \varphi_{n} \leq \varepsilon$$

## **Remarque :**

Ce critère est intéressant lorsqu'on peut calculer explicitement
$\varphi_{n}$.

En effet, on obtient la valeur de $\varphi_{n}$ en étudiant les
variations de la fonction $\left\vert  f_{n}(x) - f(x) \right\vert $

## **Exemple :**

Etudier la convergence uniforme sur $\lbrack 0;1\rbrack$ de la suite de
fonctions définie par

$$f_{n}(x) = \left\{ \begin{array}{r}
x^{n}\ln(x)\ \text{si}\ x \in \rbrack 0;1\rbrack \\
0\ \text{si}\ x = 0
\end{array} \right\}$$

Etudions la convergence simple. Soit $x \in \rbrack 0;1\lbrack$.

$$f_{n}(x) = x^{n}\ln(x) \rightarrow 0$$

Si $x = 1,\ f_{n}(x) = 0$

Si $x = 0$, $f_{n}(x) = 0$

$$f_{n} \rightarrow_{cs}f\ \text{avec}\ f = 0\ \text{sur}\ \lbrack 0;1\rbrack$$

Etudions la convergence uniforme sur $\lbrack 0\ ;1\rbrack$

Soit $x \in \rbrack 0;1\rbrack,n\mathbb{\in N}$

On pose
$g_{n}(x) = \left\vert  f_{n}(x) - f(x) \right\vert  = - f_{n}(x) = - x^{n}\ln(x)$

$g_{n}$ est dérivable sur $\rbrack 0\ ;1\rbrack$

$$\forall x \in \lbrack 0;1\rbrack,\ g_{n}^{'}(x) = - \left( nx^{n - 1}\ln(x) + x^{n - 1} \right) = - x^{n - 1}\left( n\ln(x) + 1 \right)$$

$g_{n}^{'}(x)$ s'annule en $x = e^{- \frac{1}{n}}$. Il s'agit d'un
maximum.

$$\varphi_{n} = g\left( e^{- \frac{1}{n}} \right) = \frac{1}{ne} \rightarrow 0$$

Ainsi, $\left( f_{n} \right)$ converge uniformément vers $0$ sur
$\rbrack 0;1\rbrack$ or $f_{n}(0) = 0$

Donc
$\left( f_{n} \right) \rightarrow_{cu}0\ \text{sur}\ \lbrack 0\ ;1\rbrack$

## **Corollaire :**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$ et $f$ une fonction de $I$ dans $\mathbb{K}$. S'il existe
une suite $\left( u_{n} \right)$ telle que
$\forall n\mathbb{\in N,\forall}x \in I,\ \left\vert  f_{n}(x) - f(x) \right\vert  \leq u_{n}\ \text{ET}\lim_{n \rightarrow + \infty}u_{n} = 0$

Alors $f_{n} \rightarrow_{cu}f$ sur $I$.

## **Exemple :**

Etudier la convergence uniforme de la suite de fonctions
$\left( f_{n} \right)$ définie par

$$f_{n}(x) = \sin\left( x + \frac{1}{n} \right)\ \forall x\mathbb{\in R}$$

Etude de la convergence simple :

Soit
$x\mathbb{\in R,}f_{n} \rightarrow_{cs}\sin\ \text{sur}\mathbb{\ R}$

Etude de la convergence uniforme :

Soit $x\mathbb{\in R,\ }n \in \mathbb{N}^{*}$

$$\left\vert  \sin\left( x + \frac{1}{n} \right) - \sin(x) \right\vert  = \left\vert  \cos\left( x + \frac{1}{2n} \right)\sin\left( \frac{1}{2n} \right) \right\vert  \leq \left\vert  \sin\left( \frac{1}{2n} \right) \right\vert  \rightarrow 0$$

$f_{n} \rightarrow_{cu}f$ sur $\mathbb{R}$

## **Remarque :**

Pour que $\left( f_{n} \right)$ ne converge pas uniformément vers $f$
sur $I$, il suffit qu'il existe une suite $\left( x_{n} \right)$ de
points de $I$ telle que
$\left( f_{n}\left( x_{n} \right) - f\left( x_{n} \right) \right)$ ne
tend pas vers 0.

## **Exemple :**

$$f_{n}(x) ≔ \frac{\sin(nx)}{1 + n^{2}x^{2}},\ x\mathbb{\in R}$$

Soit $x\mathbb{\in R}$.

$$f_{n}(x) \rightarrow_{n \rightarrow + \infty}0$$

$$\text{car}\ \left\vert  \frac{\sin(nx)}{1 + n^{2}x^{2}} \right\vert  \leq \frac{1}{1 + n^{2}x^{2}} \rightarrow 0$$

$$f_{n} \rightarrow_{cs}0$$

Soit $x_{0} = \frac{1}{n}$

$$\left\vert  f_{n}\left( x_{0} \right) - f\left( x_{0} \right) \right\vert  = \frac{\sin(1)}{2} \neq 0$$

$\Rightarrow \left( f_{n} \right)$ ne converge pas uniformément vers $f$
sur $\mathbb{R}$.

## **Définition : « Convergence localement uniforme »**

Soit $I$ un intervalle de $\mathbb{R}$, $\left( f_{n} \right)$ une suite
de fonctions de $I$ dans $\mathbb{K}$.

On dit que la suite $\left( f_{n} \right)$ converge localement
uniformément sur $I$ si la suite $\left( f_{n} \right)$ converge
uniformément sur tout sous-intervalle fermé inclus dans $I$.

## **Proposition :**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$. Si $\left( f_{n} \right)$ converge uniformément sur $I$
alors elle converge localement uniformément sur $I$.

## **Remarque :**

La réciproque est fausse.

Contre-exemple :

$$f_{n}(x) = x^{n},\ x \in \lbrack 0;1\lbrack$$

$$f_{n} \rightarrow_{cs}0$$

$$\sup_{x \in \lbrack 0;1\lbrack}\left\vert  f_{n}(x) - f(x) \right\vert  = \sup_{x \in \lbrack 0;1\lbrack}\left\vert  f_{n}(x) \right\vert  = f_{n}(1) = 1 \neq 0$$

$\left( f_{n} \right)$ ne converge pas uniformément sur
$\lbrack 0;1\lbrack$

Par contre, $\left( f_{n} \right)$ converge localement uniformément sur
$\lbrack 0\ ;1\lbrack$

En effet, soit $a,\ 0 < a < 1$

$$\sup_{x \in \lbrack 0;a\rbrack}\left\vert  f_{n}(x) - f(x) \right\vert  = \sup_{x \in \lbrack 0;a\rbrack}\left\vert  f_{n}(x) \right\vert  = f_{n}(a) = a^{n} \rightarrow 0$$

$$f_{n} \rightarrow_{cu}f\ \text{sur}\ \lbrack 0;a\rbrack$$

## **Remarque :**

La définition de convergence uniforme suppose de connaitre la fonction
limite $f$ de la suite $\left( f_{n} \right)$. Lorsqu'on ne connait pas
$f$, on peut utiliser le critère important suivant :

## **Théorème : « Critère de Cauchy uniforme »**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$. La suite $\left( f_{n} \right)$ converge uniformément sur
$I$ si et seulement si

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall\ }p,q \geq n_{0},\forall x \in I,\left\vert  f_{p}(x) - f_{q}(x) \right\vert  \leq \varepsilon$$

# II. **Théorèmes d'interversion**

<!-- -->

# 1.  **Interversion limite-limite**

Le théorème suivant est fondamental.

## **Théorème : Continuité de la limite uniforme**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$. Soit $a \in I$.

Si $f_{n} \rightarrow_{cu}f$ sur $I$ et $f_{n}$ est continue en $a$,
alors $f$ est continue en $a$.

## **Démonstration : En exercice**

$$f_{n} \rightarrow_{cu}f:\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}n \geq n_{0},\forall x \in I,\ \left\vert  f_{n}(x) - f(x) \right\vert  < \varepsilon$$

$$f_{n}\ \text{continue en}\ a:\forall\varepsilon > 0,\exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f_{n}(x) - f_{n}(a) \right\vert  < \varepsilon$$

$$\text{Montrer que}:\ \forall\varepsilon > 0,\exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f(x) - f(a) \right\vert  < \varepsilon$$

Soit $\varepsilon > 0\ $:

$$\left\vert  f(x) - f(a) \right\vert  = \left\vert  f(x) - f_{n}(x) + f_{n}(x) - f_{n}(a) + f_{n}(a) - f(a) \right\vert  \leq \left\vert  f(x) - f_{n}(x) \right\vert  + \left\vert  f_{n}(x) - f_{n}(a) \right\vert  + \left\vert  f_{n}(a) - f(a) \right\vert $$

$$f_{n} \rightarrow_{cu}f\ \text{donc}\ \exists n_{0}\mathbb{\in N,\ \forall}n \geq n_{0},\forall x \in I,\ \left\vert  f_{n}(x) - f(x) \right\vert  \leq \frac{\varepsilon}{3}\ \text{d'où}\ \left\vert  f_{n}(a) - f(a) \right\vert  \leq \frac{\varepsilon}{3}\ \text{aussi}$$

$$f_{n}\ \text{continue en}\ a\ \text{donc}\ \exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f_{n}(x) - f_{n}(a) \right\vert  \leq \frac{\varepsilon}{3}$$

$$\forall\varepsilon > 0,\exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f(x) - f(a) \right\vert  \leq \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$$

## **Exemple :**

$$f_{n}(x) ≔ e^{- nx},x \in \mathbb{R}^{+}$$

$$f_{n} \rightarrow_{cs}f,\ f(x) = \left\{ \begin{array}{r}
0\ \text{si}\ x > 0 \\
1\ \text{si}\ x = 0
\end{array} \right\}$$

$f_{n}$ est continue sur $\mathbb{R}^{+}$, en particulier en 0, or $f$
n'est pas continue en 0, alors $f_{n}$ ne converge pas uniformément vers
$f$ sur $\mathbb{R}^{+}$

## **Théorème : Théorème d'interversion limite-limite**

Soit $a \in \overline{I}$, $\left( f_{n} \right)$ une suite de fonctions
de $I$ dans $\mathbb{K}$ et $f$ une fonction de $I$ dans $\mathbb{K}$.

Si

-   $\forall n\mathbb{\in N,}f_{n}$ admet une limite en $a$,
    $\lim_{x \rightarrow a}{f_{n}(x)} = l_{n}\mathbb{\in K}$

-   La suite $\left( f_{n} \right)$ converge uniformément sur $I$ vers
    $f$

Alors $f$ admet une limite en $a$ et

$$\lim_{n \rightarrow + \infty}\left( \lim_{x \rightarrow a}{f_{n}(x)} \right) = \lim_{x \rightarrow a}\left( \lim_{n \rightarrow + \infty}{f_{n}(x)} \right)$$

$$\lim_{n \rightarrow + \infty}l_{n} = \lim_{x \rightarrow a}{f(x)}$$

## **Démonstration :**

On commence par montrer que $\left( l_{n} \right)$ converge en utilisant
le critère de Cauchy.

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}p,q\mathbb{\in N,}p,q \geq n_{0} \Rightarrow \left\vert  f_{p}(x) - f_{q}(x) \right\vert  \leq \varepsilon$$

$$\Rightarrow \forall p,q\mathbb{\in N,\ }p,q \geq n_{0},\lim_{x \rightarrow a}\left\vert  f_{p}(x) - f_{q}(x) \right\vert  \leq \varepsilon$$

$$\Rightarrow \forall p,q\mathbb{\in N,}p,q \geq n_{0},\ \left\vert  l_{p} - l_{q} \right\vert  \leq \varepsilon$$

Donc $\left( l_{n} \right)$ vérifie le critère de Cauchy, donc
$\left( l_{n} \right)$ converge vers une limite finie notée $l$.

Montrons que $\lim_{x \rightarrow a}{f(x)} = l$

Montrons que, $\forall\varepsilon > 0$,
$\exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f(x) - l \right\vert  \leq \varepsilon$

Soit $\varepsilon > 0$

$$\left\vert  f(x) - l \right\vert  = \left\vert  f(x) - f_{n}(x) + f_{n}(x) - l_{n} + l_{n} - l \right\vert $$

$$\left\vert  f(x) - l \right\vert  \leq \left\vert  f_{n}(x) - f(x) \right\vert  + \left\vert  f_{n}(x) - l_{n} \right\vert  + \left\vert  l_{n} - l \right\vert $$

$$\exists n_{0}\mathbb{\in N,\forall}n \geq n_{0},\left\vert  f_{n}(x) - f(x) \right\vert  < \frac{\varepsilon}{3}\ \text{car}\ f_{n} \rightarrow_{cu}f$$

$$\exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f_{n}(x) - l_{n} \right\vert  < \frac{\varepsilon}{3}\ \text{car}\lim_{x \rightarrow a}{f_{n}(x)} = l_{n}$$

$$\exists n_{1}\mathbb{\geq N,\forall}n \geq n_{1},\left\vert  l_{n} - l \right\vert  < \frac{\varepsilon}{3}\ \text{car}\ l_{n} \rightarrow_{n \rightarrow + \infty}l$$

$$\Rightarrow \exists\eta > 0,\vert x - a\vert  < \eta \Rightarrow \left\vert  f(x) - l \right\vert  < \varepsilon$$

$$\Rightarrow \lim_{x \rightarrow a}{f(x)} = l$$

$$\Rightarrow \lim_{x \rightarrow a}{\lim_{n \rightarrow + \infty}{f_{n}(x)}} = \lim_{n \rightarrow + \infty}l_{n} = \lim_{n \rightarrow + \infty}{\lim_{x \rightarrow a}{f_{n}(x)}}$$

# 2.  **Interversion limite-intégrale**

## **Théorème :**

Soient $a,b\mathbb{\in R,\ }a < b$. Soit $\left( f_{n} \right)$ une
suite de fonctions de $\lbrack a,b\rbrack$ dans $\mathbb{K}$.

Si :

-   $\forall n\mathbb{\in N,}$ $f_{n}$ est continue sur
    $\lbrack a,b\rbrack$

-   $\left( f_{n} \right)$ converge uniformément vers $f$ sur
    $\lbrack a,b\rbrack$

Alors $f$ est continue sur $\lbrack a,b\rbrack$ et

$$\lim_{n \rightarrow + \infty}{\int_{a}^{b}{f_{n}(x)dx}} = \int_{a}^{b}{\lim_{n \rightarrow + \infty}{f_{n}(x)}dx} = \int_{a}^{b}{f(x)dx}$$

## **Démonstration : En exercice**

$f$ est continue sur $\lbrack a,b\rbrack$ (voir théorème de continuité
de la limite uniforme).

Donc $f_{n} - f$ est continue sur $\lbrack a,b\rbrack$ donc bornée sur
$\lbrack a,b\rbrack$.

$$\left\vert  \int_{a}^{b}{f_{n}(x)dx} - \int_{a}^{b}{f(x)dx} \right\vert  = \left\vert  \int_{a}^{b}{\left( f_{n}(x) - f(x) \right)dx} \right\vert  \leq \int_{a}^{b}{\left\vert  f_{n}(x) - f(x) \right\vert dx} \leq \int_{a}^{b}{\sup_{x \in \lbrack a,b\rbrack}\left\vert  f_{n}(x) - f(x) \right\vert dx} = (b - a)\sup_{x \in \lbrack a,b\rbrack}\left\vert  f_{n}(x) - f(x) \right\vert $$

$$\text{Or}\lim_{n \rightarrow + \infty}{\sup_{x \in \lbrack a,b\rbrack}\left\vert  f_{n}(x) - f(x) \right\vert } = 0\ \text{car}\ f_{n} \rightarrow_{cu}f$$

CQFD

## **Exemple :**

$$\lim_{n \rightarrow + \infty}{\int_{0}^{1}{\frac{ne^{x}}{n + x}dx}}$$

$$f_{n}(x) ≔ \frac{ne^{x}}{n + x}\ \text{continue  sur}\ \lbrack 0;1\rbrack$$

Pour $x \in \lbrack 0\ ;1\rbrack$

$$\frac{ne^{x}}{n + x}\ \sim\frac{ne^{x}}{n} = e^{x}$$

$$f_{n} \rightarrow_{cs}f,\ f(x) = e^{x}$$

Etude de la convergence uniforme :

Soit $x \in \lbrack 0\ ;1\rbrack,n\mathbb{\in N}$

$$g_{n}(x) = \left\vert  f_{n}(x) - f(x) \right\vert  = \left\vert  \frac{ne^{x}}{n + x} - e^{x} \right\vert  = \frac{xe^{x}}{n + x} \leq \frac{e}{n} \rightarrow_{n \rightarrow + \infty}0$$

$f_{n} \rightarrow_{cu}f$ sur $\lbrack 0\ ;1\rbrack$

On peut appliquer le théorème d'interversion limite-intégrale.

$$\lim_{n \rightarrow + \infty}{\int_{0}^{1}{\frac{ne^{x}}{n + x}dx}} = \int_{0}^{1}{\lim_{n \rightarrow + \infty}{\frac{ne^{x}}{n + x}dx}} = \int_{0}^{1}{e^{x}dx} = e - 1$$

# 3.  **Interversion limite-dérivée**

## **Théorème :**

Soient $a,b\mathbb{\in R,\ }a < b,$ et $\left( f_{n} \right)$ une suite
de fonctions de $\lbrack a,b\rbrack$ dans $\mathbb{K}$ et $g$ une
fonction de $\lbrack a,b\rbrack$ dans $\mathbb{K}$.

Si :

-   $\forall n\mathbb{\in N}$, $f_{n}$ est de classe $C^{1}$ sur
    $\lbrack a,b\rbrack$

-   La suite $\left( f_{n}^{'} \right)$ converge uniformément vers $g$
    sur $\lbrack a,b\rbrack$

-   $\exists x_{0} \in \lbrack a,b\rbrack,\ \left( f_{n}\left( x_{0} \right) \right)$
    converge.

Alors :

-   La suite $\left( f_{n} \right)$ converge uniformément sur
    $\lbrack a,b\rbrack$ vers une limite $f$

-   $f$ est de classe $C^{1}$ sur $\lbrack a,b\rbrack$

-   $\forall x \in \lbrack a,b\rbrack,f^{'}(x) = g(x)$

$$\left\lbrack \lim_{n \rightarrow + \infty}{f_{n}^{'}(x)} = \left( \lim_{n \rightarrow + \infty}{f(x)} \right)^{'} \right\rbrack$$

Si la convergence de $\left( f_{n}^{'} \right)$ est locale, alors la
convergence de $\left( f_{n} \right)$ est locale.

# **Chapitre 3 : Séries de fonctions**

$$\sum_{n \geq 0}^{}{f_{n}(x)}$$

# I.  **Introduction**

Comme pour les séries numériques, on peut, à partir d'une série de
fonctions $\left( f_{n} \right)$ construire une suite
$\left( S_{n} \right)$ où

$$S_{n} = f_{0} + f_{1} + \ldots + f_{n}$$

On obtient alors ce qu'on appelle série de fonctions, notée
$\sum_{}^{}f_{n}$, et

$$S_{n} = \sum_{k = 0}^{n}f_{k}\ \text{sa somme partielle}$$

Les séries de fonctions jouent un rôle considérable en analyse.

Exemple : résolution d'équations différentielles, calculs numériques,
traitement de signal, physique quantique, économie et finances, etc...

Pour les séries de fonctions, on dispose d'un nouveau mode de
convergence, dit « convergence normale », qui n'est en fait qu'une
condition suffisante très utile pour établir la convergence uniforme.

Dans ce chapitre, on garde les mêmes notations que dans le chapitre
précédent.

# II. **Modes de convergence**

<!-- -->

# 1.  **Convergence simple**

## **Définition :**

Une série de fonctions $\sum_{}^{}f_{n}$ converge simplement sur $I$ si
la suite des sommes partielles $\left( S_{n} \right)$ converge
simplement sur $I$.

Dans ce cas, la fonction limite $S$ de $\left( S_{n} \right)$ s'appelle
la fonction somme de la série $\sum_{}^{}f_{n}$ et notée :

$$S = \sum_{n = 0}^{+ \infty}f_{n}$$

## **Remarque :**

Si la série de fonctions $\sum_{}^{}f_{n}$ converge simplement sur $I$,
alors $\forall x \in I$ fixé, la série numérique
$\sum_{n \geq 0}^{}{f_{n}(x)}$ converge et

$$\forall x \in I,S(x) = \left( \sum_{n = 0}^{+ \infty}f_{n} \right)(x) = \sum_{n = 0}^{+ \infty}{f_{n}(x)}$$

## **Exemple :**

On considère la série de fonctions $\sum_{}^{}\frac{x^{n}}{n!}$ définie
sur $\mathbb{R}$.

Soit $x\mathbb{\in R}$ fixé, on étudie la série numérique
$\sum_{}^{}\frac{x^{n}}{n\ !} = \sum_{}^{}u_{n}$

On applique la règle d'Alembert.

$$\forall n\mathbb{\in N,\ }\left\vert  \frac{u_{n + 1}}{u_{n}} \right\vert  = \frac{\vert x\vert }{n + 1} \rightarrow_{n \rightarrow + \infty}0 < 1$$

$$\sum_{}^{}u_{n}\ \text{converge}$$

$$\sum_{}^{}f_{n}\ \text{converge simplement sur}\mathbb{\ R}$$

On considère la série de fonctions $\sum_{}^{}f_{n}$ sur
$\mathbb{R}^{+}$ avec $f_{n}(x) = xe^{- nx}$

Soit $x \in \mathbb{R}^{+}$ fixé.

On étudie la convergence de la série numérique $\sum_{}^{}u_{n}$,
$u_{n} = xe^{- nx}$

On applique la règle de $n^{\alpha}$

$$\lim_{n \rightarrow + \infty}{n^{2}u_{n}} = \lim_{n \rightarrow + \infty}{n^{2}xe^{- nx}} = 0\ \text{(croissance comparée)}$$

$$\Rightarrow \sum_{}^{}u_{n}\ \text{converge} \Rightarrow \sum_{}^{}f_{n}\ \text{cs}$$

## **Définition : « Domaine de convergence »**

On appelle domaine de convergence de la série de fonctions
$\sum_{}^{}f_{n}$ l'ensemble des $x$ de $I$ tels que
$\sum_{}^{}{f_{n}(x)}$ converge.

## **Exemple :**

Déterminer le domaine de convergence des séries suivantes :

$$\sum_{}^{}\frac{1}{n^{x}}$$

Série de Riemann, converge si et seulement si $x > 1$

Domaine de convergence : $\rbrack 1; + \infty\lbrack$

$$\sum_{}^{}\frac{( - 1)^{n}}{n^{x}}$$

Série de Riemann alternée, converge si et seulement si $x > 0$

Domaine de convergence : $\rbrack 0; + \infty\lbrack$

## **Proposition :**

Si $\sum_{}^{}f_{n}$ converge simplement sur $I$ alors elle converge
simplement sur tout sous-ensemble de $I$.

[Définition :**

Si la série $\sum_{}^{}f_{n}$ converge alors on peut définir le reste
d'ordre $n$

$$R_{n} = \sum_{k = n + 1}^{+ \infty}f_{k}$$

Dans ce cas,

$$\forall x \in I,\ S(x) = S_{n}(x) + R_{n}(x)$$

## **Exemple :**

$$\sum_{n \geq 0}^{}{xe^{- nx}}$$

On a montré que cette série converge simplement sur $\mathbb{R}^{+}$.

$$S_{n} = x\sum_{k = 0}^{n}e^{- kx} = x\sum_{k = 0}^{n}\left( e^{- x} \right)^{k} = \frac{x\left( 1 - e^{- x(n + 1)} \right)}{1 - e^{- x}}$$

$$\lim_{n \rightarrow + \infty}S_{n} = \frac{x}{1 - e^{- x}}$$

$$\Rightarrow R_{n} = S - S_{n} = \frac{x}{1 - e^{- x}} - x\frac{1 - e^{- x(n + 1)}}{1 - e^{- x}}$$

$$R_{n} = x\frac{e^{- (n + 1)x}}{1 - e^{- x}}$$

## **Proposition : « Condition nécessaire »**

Si $\sum_{}^{}f_{n}$ converge simplement alors $\left( f_{n} \right)$ et
$\left( R_{n} \right)$ convergent simplement vers la fonction nulle.

### **Démo :**

$$f_{n} = S_{n + 1} - S_{n} \rightarrow_{+ \infty}S - S = 0$$

$$R_{n} = S - S_{n} \rightarrow_{+ \infty}S - S = 0$$

# 2.  Convergence absolue**

Une série de fonction $\sum_{}^{}f_{n}$ converge absolument sur $I$ si

$$\forall x \in I,\ \sum_{}^{}\left\vert f_{n}(x) \right\vert\ \text{converge}$$

### **Exemple :**

$$ \sum_{}^{}\frac{( - 1)^{n}}{n^{x}}\ \text{converge absolument sur}\ \rbrack 1; + \infty \left \lbrack \ \text{mais converge simplement sur}\  \right \rbrack 0; + \infty\lbrack $$

## **Proposition :**

Si $\sum_{}^{}f_{n}$ converge absolument sur $I$ alors elle converge
simplement sur $I$.

### **Remarque :** La réciproque est fausse.

# **3.  Convergence normale**

## **Définition :**

On dit que la série $\sum_{}^{}f_{n}$ converge normalement sur $I$ si

$$\text{i.}\ \exists n_{0}\mathbb{\in N,\forall}n \geq n_{0},\ f_{n}\ \text{est bornée sur}\ I$$

$$\text{ii.}\ \text{La série numérique}\ \sum_{n \geq 0}^{}\left\vert f_{n} \right\vert_{\infty}\ \text{converge}$$

Avec
$\left\vert f_{n} \right\vert_{\infty} = \sup_{x \in I}\left\vert f_{n}(x) \right\vert$

## **Proposition :**

Si $\sum_{}^{}f_{n}$ converge normalement sur $I$ alors elle converge
normalement sur tout sous-ensemble de $I$.

## **Proposition :**

Soit $\left( f_{n} \right)$ une suite de fonction de $I$ dans
$\mathbb{K}$ et $\left( u_{n} \right)$ une suite numérique à termes
positifs.

Si
$\forall n\mathbb{\in N,\forall}x \in I,\left\vert f_{n}(x) \right\vert \leq \sup_{x \in I}\left\vert f_{n}(x) \right\vert \leq u_{n}\ \text{et}\ \sum_{}^{}u_{n}\ \text{converge}$
alors $\sum_{}^{}f_{n}$ converge normalement.

### **Démonstration :**

On remarque que
$\forall n\mathbb{\in N,\forall}x \in I,\ \left\vert f_{n}(x) \right\vert \leq u_{n}$
alors $\left\vert f_{n} \right\vert_{\infty} \leq u_{n}$

D'après le théorème de comparaison par inégalité des séries numériques,

$$\sum_{}^{}\left\vert f_{n} \right\vert_{\infty}\ \text{converge}$$

### **Exemple :**

$$\sum_{}^{}{xe^{- nx}}\ \text{converge normalement sur}\ \lbrack a,b\rbrack,\ 0 < a < b$$

En effet,
$\forall x \in \lbrack a,b\rbrack,\left\vert xe^{- nx} \right\vert \leq be^{- na}$

Or $\sum_{}^{}{be^{- na}}$ converge

Donc
$\sum_{}^{}{xe^{- nx}}\ \text{converge normalement sur}\ \lbrack a,b\rbrack$

### **Exemple :**

$$\sum_{n \geq 0}^{}\frac{\sin(nx)}{n^{2}}\ \text{converge normalement sur}\mathbb{\ R}$$

$$\text{En effet},\ \left\vert \frac{\sin(nx)}{n^{2}} \right\vert \leq \frac{1}{n^{2}}$$

$$\text{Or}\ \sum_{}^{}\frac{1}{n^{2}}\ \text{converge car série de Riemann}$$

Donc $\sum_{n \geq 0}^{}\frac{\sin(nx)}{n^{2}}$ converge normalement.

# **4.  Convergence uniforme**

## **Définition :**

Une série de fonctions $\sum_{}^{}f_{n}$ converge uniformément sur $I$
si sa somme partielle $\left( S_{n} \right)$ converge uniformément sur
$I$. Si on note $S$ la somme de la série :

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}n\mathbb{\in N,\forall}x \in I,\left\vert S_{n}(x) - S(x) \right\vert \leq \varepsilon$$

## **Proposition :**

Si $\sum_{}^{}f_{n}$ converge uniformément sur $I$ alors elle converge
simplement sur $I$.

## **Proposition : « Condition nécessaire et suffisante de convergence uniforme »**

$$\sum_{}^{}f_{n} \text{ converge uniformément sur } I \Longleftrightarrow  \left\{ \begin{array}{r}
\sum_{}^{}f_{n}\ \text{converge simplement sur } I \\
R_{n} \rightarrow_{cu}0\ \text{sur } I
\end{array} \right. $$

### **Démonstration :**

Si $\sum_{}^{}f_{n}$ converge uniformément sur $I$, alors
$R_{n} = S - S_{n}$ converge uniformément vers 0 sur $I$.

Réciproquement, si $\sum_{}^{}f_{n}$ converge simplement sur $I$ vers
$S$ et $\left( R_{n} \right)$ converge uniformément vers 0.

Alors $S_{n} = S - R_{n}$ converge uniformément vers $S$ sur $I$.

### **Exemple :**

$$\sum_{}^{}{xe^{- nx}}\ \text{ne converge pas uniformément sur}\ \mathbb{R}_{+}$$

En effet,

$$R_{n}(x) = x\frac{e^{- (n + 1)x}}{1 - e^{- x}}$$

Pour $x_{0} = \frac{1}{n + 1}$,

$$R_{n}\left( x_{0} \right) = \frac{1}{n + 1}\frac{e^{- 1}}{1 - e^{- \frac{1}{(n + 1)}}} \rightarrow e^{- 1} \neq 0$$

Donc $\left( R_{n} \right)$ ne converge pas uniformément vers 0 sur
$\mathbb{R}_{+}$

Donc la série ne converge pas uniformément sur $\mathbb{R}_{+}$

### **Exemple 2 :**

On considère la série de fonctions :

$$\sum_{n \geq 0}^{}\frac{( - 1)^{n}}{x + n}\ \text{sur}\ \mathbb{R}_{+}$$

Cette série est sous la forme $\sum_{}^{}{( - 1)^{n}a_{n}}$ avec
$a_{n} = \frac{1}{x + n} \geq 0$

$\left( a_{n} \right)$ est décroissante et tend vers 0. D'après le CSSA,
$\sum_{}^{}{( - 1)^{n}a_{n}}$ converge.

$$\sum_{n \geq 0}^{}\frac{( - 1)^{n}}{x + n}\ \text{converge simplement}$$

Aussi,

$$\left\vert R_{n} \right\vert \leq a_{n + 1} \leq \frac{1}{x + n + 1} \leq \frac{1}{n + 1} \rightarrow 0$$

$\Rightarrow \left\vert R_{n} \right\vert$ converge uniformément vers 0 sur
$\mathbb{R}_{+}$

## **Proposition : « Condition nécessaire de convergence uniforme »**

Si $\sum_{}^{}f_{n}$ converge uniformément sur $I$ alors
$\left( f_{n} \right)$ converge uniformément sur $I$ vers la fonction
nulle.

### **Attention :** Cette condition n'est pas suffisante, la réciproque est fausse.

### **Exemple :**

$$\sum_{}^{}\frac{1}{n^{x}};\ \text{on a}\ \left( \frac{1}{n^{x}} \right)\ \text{converge uniformément sur}\ \rbrack 1; + \infty\lbrack\ \text{mais}\ \sum_{}^{}\frac{1}{n^{x}}\ \text{ne converge pas uniformément sur}$$

$$\rbrack 1; + \infty\lbrack $$

## **Proposition :**

Si $\sum_{}^{}f_{n}$ converge uniformément sur $I$ alors elle converge
uniformément sur tout sous-ensemble de $I$.

## **Théorème : « Critère uniforme de Cauchy »**

La série de fonctions $\sum_{}^{}f_{n}$ converge uniformément sur $I$ si
et seulement si,

$$\forall\varepsilon > 0,\exists n_{0}\mathbb{\in N,\forall}p,q \geq n_{0},\forall x \in I,\ \left\vert \sum_{k = p + 1}^{q}{f_{k}(x)} \right\vert \leq \varepsilon$$

### **Démonstration :** C'est le critère de Cauchy appliqué à $\left( S_{n} \right)$

## **Théorème :**

Toute suite qui converge normalement converge absolument et
uniformément.

### **Démonstration :**

Par hypothèse, on suppose que $\sum_{}^{}f_{n}$ converge normalement.

$\exists\left( \alpha_{n} \right)$ une suite positive telle que
$\forall x \in I,\ \forall n\mathbb{\in N,\ }\left\vert f_{n}(x) \right\vert \leq \alpha_{n}$
et $\sum_{}^{}\alpha_{n}$ converge.

Donc la convergence est absolue.

$$\forall p,q\mathbb{\in N,\forall}x \in I,\ \left\vert f_{p + 1}(x) + \ldots + f_{q}(x) \right\vert \leq \alpha_{p + 1} + \ldots + \alpha_{q}$$

Donc le critère de Cauchy est vérifié, d'où la convergence uniforme sur
$I$.

# **III. Théorèmes d'interversion**


## **1.  Théorème d'interversion somme-limite**

Soit $a \in I$, $\sum_{}^{}f_{n}$ une série de fonctions de $I$ dans
$\mathbb{K}$. On suppose que :

- a.  $\forall n\mathbb{\in N}$, $f_{n}$ admet une limite en $a$ notée
    $l_{n}$

- b.  La série $\sum_{}^{}f_{n}$ converge uniformément sur $I$

Alors :

- a.  $\sum_{}^{}l_{n}$ converge dans $\mathbb{K}$

- b.  La fonction somme $S$ admet une limite en $a$ et

$$\lim_{x \rightarrow a}S_{n} = \sum_{n = 0}^{+ \infty}l_{n}$$

### **Démonstration :**

Il suffit d'appliquer le théorème d'interversion limite-limite du
chapitre 2 à la suite des sommes partielles $\left( S_{n} \right)$

### **Théorème : Convergence et continuité**

Soit $a \in I$, $\left( f_{n} \right)$ une suite de fonctions de $I$
dans $\mathbb{K}$.

On suppose que :

- a.  $\forall n\mathbb{\in N,\ }f_{n}$ est continue en $a$

- b.  $\sum_{}^{}f_{n}$ converge uniformément sur $I$

Alors la fonction somme $S$ de la série $\sum_{}^{}f_{n}$ est continue
en $a$.

### **Corollaire :**

Soit $\left( f_{n} \right)$ une suite de fonctions de $I$ dans
$\mathbb{K}$.

On suppose que :

- a.  $\forall n\mathbb{\in N}$, $f_{n}$ est continue sur $I$

- b.  $\sum_{}^{}f_{n}$ converge uniformément sur $I$ (ou localement
    uniformément)

Alors la fonction somme $S$ est continue sur $I$.

### **Exercice :**

$$\text{Soit}\ S(x) = \sum_{n = 0}^{+ \infty}\frac{e^{- n\vert x\vert}}{n^{2}}$$

Montrer que $S$ est continue sur $\mathbb{R}$.

$$\left \vert f_{n}(x) \right \vert = \frac{e^{- n\vert x\vert}}{n^{2}} \leq \frac{1}{n^{2}}\forall n,x$$

$$\sum_{}^{}\frac{1}{n^{2}}\ \text{converge donc}\ \sum_{}^{}f_{n}\ \text{converge normalement donc uniformément}$$

Aussi, $f_{n}$ est continue sur $\mathbb{R}$.

Donc $S$ est continue sur $\mathbb{R}$.

$$\lim_{x \rightarrow 0}{S(x)} = \ ?$$

On applique le théorème d'interversion limite-somme. Les hypothèses sont
vérifiées.

$$\lim_{x \rightarrow 0}{S(x)} = \sum_{}^{}\frac{1}{n^{2}} = \frac{\pi^{2}}{6}$$

## **2.  Théorème d'interversion limite-intégrale**

Soient deux points $a,b\mathbb{\in R}$, $a < b$ et
$\left( f_{n} \right)$ une suite de fonctions de $\lbrack a,b\rbrack$
dans $\mathbb{K}$.

On suppose que :

- a.  $\forall n\mathbb{\in N}$, $f_{n}$ est continue sur
    $\lbrack a,b\rbrack$ (ou continue par morceaux)

- b.  $\sum_{}^{}f_{n}$ converge uniformément sur $\lbrack a,b\rbrack$

Alors la fonction $S$ est continue sur $\lbrack a,b\rbrack$ et la série
numérique

$$\sum_{}^{}{\int_{a}^{b}{f_{n}(x)dx}}\ \text{converge et on a}$$

$$\sum_{n = 0}^{+ \infty}{\int_{a}^{b}{f_{n}(x)dx}} = \int_{a}^{b}{S(x)dx}$$

### **Démonstration :**

Il suffit d'appliquer le théorème d'interversion limite-intégrale du
chapitre 2 à la suite des sommes partielles $\left( S_{n} \right)$.

### **Exercice :**

Soit

$$f_{n}(x) = \left\{ \begin{array}{r}
0\ \text{si}\ x = 0 \\
\frac{x^{n}\ln(x)}{n}\ \text{si}\ x \in \rbrack 0;1\rbrack
\end{array} \right\}$$

Montrer que :

$$\int_{0}^{1}{\sum_{n = 1}^{+ \infty}{f_{n}(x)}dx} = \sum_{n = 1}^{+ \infty}\frac{1}{n(n + 1)^{2}}$$

$\forall n\mathbb{\in N,\ }f_{n}$ est continue sur $\lbrack 0;1\rbrack$,
reste à montrer que la série de fonctions converge uniformément.

Soit $x \in \rbrack 0;1\rbrack$.

$$\left\vert f_{n}(x) \right\vert = - f_{n}(x)$$

$$\left\vert f_{n}(x) \right\vert^{'} = - \frac{1}{n}\left( nx^{n - 1}\ln(x) + x^{n - 1} \right) = - x^{n + 1}\left( 1 + \frac{\ln(x)}{n} \right)$$

Atteint un minimum pour $e^{- \frac{1}{n}}$

$$\left\vert f_{n}\left( e^{- \frac{1}{n}} \right) \right\vert = \frac{1}{en^{2}}$$

$$\sum_{}^{}\frac{1}{en^{2}}\ \text{converge donc}\ \sum_{}^{}f_{n}\ \text{converge normalement donc uniformément sur}\ \lbrack 0;1\rbrack$$

On peut donc appliquer le théorème d'interversion limite-intégrale.

$$\int_{0}^{1}{\sum_{x = 1}^{+ \infty}{f_{n}(x)dx}} = \sum_{n = 1}^{+ \infty}{\int_{0}^{1}{f_{n}(x)dx}}$$

$$\int_{0}^{1}{f_{n}(x)dx} = \frac{1}{n}\int_{0}^{1}{x^{n}\ln(x)dx} $$

$$= \frac{1}{n}\left( \frac{1}{n + 1}\left\lbrack x^{n + 1}\ln(x) \right\rbrack_{0}^{1} - \frac{1}{n + 1}\int_{0}^{1}x^{n} \right)$$

$$= - \frac{1}{n(n + 1)^{2}}\left\lbrack x^{n + 1} \right\rbrack_{0}^{1} = - \frac{1}{n(n + 1)^{2}}$$

## **3.  Théorème d'interversion limite-dérivée**

Soient $a,b\mathbb{\in R}$, $a < b$ et $\left( f_{n} \right)$ une suite
de fonctions de $\lbrack a,b\rbrack$ dans $\mathbb{K}$.

On suppose que :

- a.  $\forall n\mathbb{\in N,\ }f_{n}$ est $C^{1}$ sur
    $\lbrack a,b\rbrack$

- b.  $\sum_{}^{}f_{n}^{'}$ converge uniformément vers $T$ sur
    $\lbrack a,b\rbrack$

- c.  $\exists x_{0} \in \lbrack a,b\rbrack$ tel que la suite numérique
    $\sum_{}^{}f_{n}$ converge

Alors :

- a.  $\sum_{}^{}f_{n}$ converge uniformément sur $\lbrack a,b\rbrack$
    vers $S$

- b.  $S$ est $C^{1}$ sur $\lbrack a,b\rbrack$

- c.  $S^{'} = T$

### **Démonstration :**

Il suffit d'appliquer le théorème d'interversion limite-dérivée à la
suite des sommes partielles $\left( S_{n} \right)$.

# **Chapitre 4 : Séries entières**

## **Notation :**

$D(0,R)$ le disque complexe ouvert de centre 0 et de rayon $R$

$\overline{D}(0,R)$ le disque fermé de centre $0$ et de rayon $R$

## **I.  Généralités**

### **Définition :**

Soit $\left( a_{n} \right)$ une suite numérique dans $\mathbb{K}$.

On appelle série entière de coefficient $a_{n}$ la série de fonctions du
type

$$\sum_{}^{}{a_{n}z^{n}}\ \text{où}\ z\mathbb{\in C}$$

### **Exemple :**

$$\text{Série géométrique :}\ \sum_{n \geq 0}^{}z^{n}\ \text{avec}\ a_{n} = 1$$

$$\text{Série exponentielle :}\sum_{}^{}\frac{z^{n}}{n!}\ \text{avec}\ a_{n} = \frac{1}{n!}$$

### **Lemme d'Abel :**

$$\text{Soit}\ \sum_{}^{}{a_{n}z^{n}}\ \text{une série entière},\ z_{0}\mathbb{\in C}$$

$$\text{Si}\ \left( a_{n}z_{0}^{n} \right)\ \text{est bornée alors}\ \forall z\mathbb{\in C,\ }\text{si}\ \vert z\vert < \left\vert z_{0} \right\vert\ \text{alors}\ \sum_{}^{}{a_{n}z^{n}}\ \text{converge absolument}$$

### **Démonstration :**

$$\exists M > 0,\ \forall n\mathbb{\in N,\ }\left\vert a_{n}z_{0}^{n} \right\vert \leq M$$

$$\left\vert a_{n}z^{n} \right\vert = \left\vert a^{n}z_{0}^{n} \right\vert \times \frac{\left\vert z^{n} \right\vert}{\left\vert z_{0}^{n} \right\vert} \leq M\left\vert \frac{z}{z_{0}} \right\vert^{n}$$

$$\text{Or}\ \left( \left\vert \frac{z}{z_{0}} \right\vert^{n} \right)\ \text{est une suité géométrique de raison}\ \left\vert \frac{z}{z_{0}} \right\vert < 1\ \text{d'où convergence}$$

### **Définition-Théorème : « Rayon de convergence »**

$$\text{Pour toute série entière}\ \sum_{}^{}{a_{n}z^{n}},\ \text{il existe un unique}\ R \in \mathbb{R}_{+} \cup \left\{ + \infty \right\}$$

$$\forall z\mathbb{\in C,\ }\left\{ \begin{array}{r}
\vert z\vert < R \Rightarrow \sum_{}^{}{a_{n}z^{n}}\ \text{converge absolument} \\
\vert z\vert > R\  \Rightarrow \sum_{}^{}{a_{n}z^{n}}\ \text{diverge grossièrement}
\end{array} \right. $$

$$R = \sup\left\{ r \geq 0,\ \left( \left\vert a_{n} \right\vert r^{n} \right) \text{ bornée} \right\}$$

$R$ est appelé rayon de convergence de $\sum_{}^{}{a_{n}z^{n}}$

On appelle disque de convergence de $\sum_{}^{}{a_{n}z^{n}}$ le disque
$D(0,R)$

On appelle intervalle de convergence de $\sum_{}^{}{a_{n}z^{n}}$
l'intervalle $\rbrack - R\ ;R\lbrack$

### **Attention :**

Pour $\vert z\vert = R$, $\sum_{}^{}{a_{n}z^{n}}$ parfois converge, parfois
diverge.

### **Remarque :**

Le domaine de convergence de la série entière est le disque de
convergence ou l'intervalle de convergence. Si $R = 0$ alors le domaine
de convergence est $ \{ 0 \} $. Si $R = + \infty$ alors le
domaine de convergence est $\mathbb{R}$.

### **Exemple :**

$$e^{x} = \sum_{n \geq 0}^{}\frac{x^{n}}{n!},\ R = + \infty$$

$$\sum_{}^{}x^{n},\ R = 1$$

### **Corollaire : « Contraposée de la définition du rayon de convergence »**

$$\text{Soit}\ \sum_{}^{}{a_{n}z^{n}} \text{ une série entière de rayon de convergence } R$$

$$\text{Alors } \forall z\mathbb{\in C,\ }\left\{ \begin{array}{r}
\sum_{}^{}{a_{n}z^{n}} \text{ converge} \Rightarrow \vert z\vert \leq R \\
\sum_{}^{}{a_{n}z^{n}} \text{ diverge} \Rightarrow \vert z\vert \geq R
\end{array} \right. $$

## **II. Méthode d'évaluation du rayon de convergence**


### **1.  Règle de calcul**

### **Théorème :**

$$\text{Soit}\ \sum_{}^{}{a_{n}z^{n}}\ \text{une série entière de rayon de convergence}\ R$$

-   **Règle d'Alembert :**

$$\exists n_{0}\mathbb{\in N,\ \forall}n \geq n_{0},\ a_{n} \neq 0$$

$$\lim_{n \rightarrow + \infty}\left\vert \frac{a_{n + 1}}{a_{n}} \right\vert = l \in \lbrack 0; + \infty\rbrack$$

$$\text{Alors}\ R = \frac{1}{l}$$

-   **Règle de Cauchy :**

$$\lim_{n \rightarrow + \infty}\left\vert a^{n} \right\vert^{\frac{1}{n}} = l$$

$$\text{Alors}\ R = \frac{1}{l}$$

$$R = 0\ \text{si}\ l = + \infty\ \text{et}\ R = + \infty\ \text{si}\ l = 0$$

### **Exercice :**

Déterminer le rayon de convergence des séries entières suivantes

- 1\.

$$\sum_{}^{}\frac{z^{n}}{n^{n}}$$

$$a_{n} = \frac{1}{n^{n}},\ \left\vert a_{n} \right\vert^{\frac{1}{n}} = \frac{1}{n} \rightarrow 0$$

$$R = + \infty$$

- 2\.

$$\sum_{}^{}{\frac{n!}{n^{2} + 1}z^{n}}$$

$$a_{n} = \frac{n!}{n^{2} + 1}$$

$$\left\vert \frac{a_{n + 1}}{a_{n}} \right\vert = \frac{(n + 1)\left( n^{2} + 1 \right)}{n^{2} + 2n + 2} \rightarrow + \infty$$

$$R = 0$$

- 3\.

$$\sum_{}^{}{\frac{\sqrt{n}}{( - 2)^{n}}z^{n}}$$

$$\left\vert \frac{a_{n + 1}}{a_{n}} \right\vert = \frac{\sqrt{n + 1}}{\sqrt{n}} \times \frac{1}{2} \rightarrow \frac{1}{2}$$

- 4\.

$$\sum_{}^{}{\frac{3^{n}}{\ln(n)}z^{2n + 1}}$$

$$\text{Posons}\ u_{n} = \frac{z^{n}}{\ln(n)}z^{2n + 1}$$

Etudions la convergence absolue de la série numérique $\sum_{}^{}u_{n}$

$$\left\vert \frac{u_{n + 1}}{u_{n}} \right\vert = \frac{3\ln(n)}{\ln(n + 1)}\vert z\vert^{2} \rightarrow_{n \rightarrow + \infty}3\vert z\vert^{2}$$

$$\text{Si}\ \vert z\vert < \frac{1}{\sqrt{3}}\ \text{alors}\ \sum_{}^{}u_{n}\ \text{converge absolument}$$

$$\text{Si}\ \vert z\vert > \frac{1}{\sqrt{3}}\ \text{alors}\ \sum_{}^{}u_{n}\ \text{diverge}$$

$$R = \frac{1}{\sqrt{3}}$$

- 5\.

$$\sum_{}^{}{\frac{1}{8^{n + 1}}z^{3n}}$$

$$\text{Posons}\ u_{n} = \frac{1}{8^{n + 1}}z^{3n}$$

$$\left\vert \frac{u_{n + 1}}{u_{n}} \right\vert = \frac{1}{8}\vert z\vert^{3}$$

$$\text{Si}\ \vert z\vert < 2\ \text{alors}\ \sum_{}^{}u_{n}\ \text{converge absolument}$$

$$\text{Si}\ \vert z\vert > 2\ \text{alors}\ \sum_{}^{}u_{n}\ \text{diverge}$$

$$R = 2$$

### **2.  Théorèmes de comparaison**

### **Théorème :**

$$\text{Soient}\ \sum_{}^{}{a_{n}z^{n}}\ \text{et}\ \sum_{}^{}{b_{n}z^{n}}\ \text{deux séries entières de rayons de convergence respectifs}\ R_{a}\ \text{et}\ R_{b}$$

i.  $\left\vert a_{n} \right\vert \leq \left\vert b_{n} \right\vert \Rightarrow R_{a} \geq R_{b}$

ii. $a_{n} = Ο\left( b_{n} \right)\ \text{ou}\ a_{n} = o\left( b_{n} \right) \Rightarrow R_{a} \geq R_{b}$

iii. $\left\vert a_{n} \right\vert\ \sim\ \left\vert b_{n} \right\vert \Rightarrow R_{a} = R_{b}$

### **Exemple :**

$$\sum_{}^{}{\ln\left( 1 + \frac{1}{n} \right)z^{n}}$$

$$\ln\left( 1 + \frac{1}{n} \right)\ \sim\frac{1}{n}\ \text{or}\ \sum_{}^{}\frac{z^{n}}{n}\ \text{est de rayon de convergence}\ R = 1\ \text{alors le rayon de convergence de}\ \sum_{}^{}{\ln\left( 1 + \frac{1}{n} \right)z^{n}}\ \text{est}\ R = 1$$

### **3.  Opérations sur les suites**

### **Théorème :**

$$\text{Soient}\ \sum_{}^{}{a_{n}z^{n}}\ \text{et}\ \sum_{}^{}{b_{n}z^{n}}\ \text{deux séries entières de rayon de convergence}\ R_{a}\ \text{et}\ R_{b}\ \text{et de somme}\ S_{a}\ \text{et}\ S_{b}$$

$$\forall\lambda\mathbb{\in C,}\sum_{}^{}{\lambda a_{n}z^{n}}\ \text{a pour rayon de convergence}\ R_{a}\ \text{et pour tout}\ z \in D\left( 0,R_{a} \right),\ S_{\lambda a}(z) = \lambda S_{a}(z)$$

$$\text{Si}\ R_{a} \neq R_{b},\ \text{alors}\ \sum_{}^{}{\left( a_{n} + b_{n} \right)z^{n}}\ \text{a pour rayon de convergence}\ R = \min\left( R_{a},R_{b} \right)\ \text{et}\ \forall z \in D(0,R),\ S_{a + b}(z) = S_{a}(z) + S_{b}(z)$$

$$\text{Si}\ R_{a} = R_{b}\ \text{alors}\ R \geq R_{a}$$

## **III. Convergence et régularité**


### **1.  Convergence**

### **Théorème :**

Toute série entière converge localement normalement sur son disque de
convergence. (Elle converge normalement sur tout compact de $D(0,R)$).

### **2.  Régularité**

<!-- -->

**a.  Continuité**

$$\text{Le somme d'une série entière}\ \sum_{}^{}{a_{n}z^{n}}\ \text{est continue sur son disque (ouvert) de convergence.}$$

**Proposition :**

$$\text{Soit } \sum_{}^{}{a_{n}z^{n}}\ \text{de rayon de convergence } R$$

$$\text{Si } \sum_{}^{}{a_{n}R^{n}} \text{ converge absolument alors la somme de}\sum_{}^{}{a_{n}z^{n}} \text{ est continue sur } \overline{D}(0,R) \text{ et } $$

$$\sum_{}^{}{a_{n}z^{n}} \text{ converge normalement sur } \overline{D}(0,R) $$

$$\text{Si } \sum_{}^{}{a_{n}R^{n}} \text{ converge alors } S \text{ est continue sur } \lbrack 0;R\rbrack$$

$$\text{Si } \sum_{}^{}{a_{n}( - R)^{n}} \text{ converge alors } S \text{ est continue sur } \lbrack - R;0\rbrack$$

**b.  Dérivabilité**

$$\text{Soit}\ \sum_{}^{}{a_{n}z^{n}}\ \text{une série entière de rayon de convergence}\ R \neq 0\ \text{et de somme}\ S\ \text{alors}\ S\ \text{est}\ C^{\infty}\ \text{sur}\ \rbrack - R;R\lbrack$$

$$\text{et}\ \forall p\mathbb{\in N,\forall\ }x \in \rbrack - R,R\lbrack,\ S^{(p)}(x) = \sum_{(n = p)}^{+ \infty}{\frac{n!}{(n - p)!}a_{n}x^{n - p}} = \sum_{n = 0}^{+ \infty}{\frac{(n + p)!}{n!}a_{n + p}x^{n}}$$

### **Corollaire :**

$$\text{Soit}\ \sum_{}^{}{a_{n}z^{n}}\ \text{une série entière de rayon de convergence non nul et de somme}\ S$$

$$\text{Alors}\ \forall p\mathbb{\in N,\ }a_{p} = \frac{S^{(p)}(0)}{p!}$$

### **Exemple :**

$$\forall x \in \rbrack - 1;1\lbrack,\ S(x) = \sum_{n = 0}^{+ \infty}x^{n} = \frac{1}{1 - x}$$

$$\frac{1}{(1 - x)^{2}} = S^{'}(x) = \sum_{n = 0}^{+ \infty}\frac{(n + 1)!}{n!},\ \ x^{n} = \sum_{n \geq 0}^{}{(n + 1)x^{n}}$$

## **IV. Développement en série entière**

### **Proposition :**

$$\text{Soient}\ \sum_{}^{}{a_{n}z^{n}}\ \text{et}\ \sum_{}^{}{b_{n}z^{n}}\ \text{deux séries entières de rayons de convergence}\ R_{a}\ \text{et}\ R_{b}\ \text{et de somme}\ S_{a}\ \text{et}\ S_{b}$$

$\text{Pour}\ R = \min\left( R_{a},R_{b} \right)$,

$$\text{Si}\ \forall x \in D(0,R),\ S_{a} = S_{b}\ \text{alors}\ \forall n\mathbb{\in N,\ }a_{n} = b_{n}$$

### **Proposition :**

$$\text{Soit}\ \sum_{}^{}{a_{n}z^{n}}\ \text{une série entière de rayon de convergence}\ R\ \text{et de somme}\ S$$

$$\text{Alors}\ \forall x \in \rbrack - R;R\lbrack,\ S(x) = \sum_{n = 0}^{+ \infty}{\frac{S^{(n)}(0)}{n!}x^{n}}$$

### **Définition :**

Soit $I$ un intervalle de $\mathbb{R}$, avec $ 0 \in \mathring{I} $, $f$
une fonction de $I$ dans $\mathbb{K}$, la fonction $f$ est dite
développable en série entière en 0 s'il existe une série entière
$\sum_{}^{}{a_{n}z^{n}}$ de rayon de convergence $R \neq 0$ telle que
$\forall x \in I \cap \rbrack - R,R\lbrack,\ f(x) = \sum_{n = 0}^{+ \infty}{a_{n}x^{n}}$

De même $f$ est développable en série entière en $x_{0}$ alors
$\forall x \in I \cap \ \rbrack x\_ 0 - R,x\_ 0 + R\lbrack,\ f(x) = \sum_{n = 0}^{+ \infty}{a_{n}\left( x - x_{0} \right)^{n}}$

### **Théorème :**


$$\text{Soit}\ I\ \text{un intervalle de}\mathbb{\ R,\ }0 \in \mathring{I},\ \text{si}\ f\ \text{est développable en série entière en}\ 0\ \text{de coefficient}\ a_{n}\ \text{alors}$$

$$f\ \text{est}\ C^{\infty}\ \text{sur}\ I \cap \rbrack - R,R\lbrack$$

$$\forall n\mathbb{\in N,\ }a_{n} = \frac{f^{(n)}(0)}{n!}$$

### **Remarques :**

Si $f$ est paire alors $a_{2p + 1} = 0$

Si $f$ est impaire alors $a_{2p} = 0$

### **Exemple :**

Développement en série entière de $x \rightarrow \cos(x)$ en 0

$$\cos^{(n)}x = \cos\left( x + \frac{n\pi}{2} \right)$$

$$\cos^{(n)}0 = \cos\left( \frac{n\pi}{2} \right) = \left\{ \begin{array}{r}
( - 1)^{\frac{n}{2}}\ \text{si}\ n\ \text{pair} \\
0\ \text{si}\ n\text{ impair}
\end{array} \right. $$

$$\cos(x) = \sum_{n = 0}^{+ \infty}{\frac{\cos^{(n)}(x)}{n!}x^{n}} = \sum_{p = 0}^{+ \infty}{\frac{( - 1)^{p}}{(2p)!}x^{2p}}$$