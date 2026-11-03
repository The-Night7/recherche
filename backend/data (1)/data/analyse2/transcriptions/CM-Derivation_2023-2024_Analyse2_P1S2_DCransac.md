---
source: "PREING2-S1/Series/CM-Derivation_2024-2025_Series_P2S1_DCransac.pdf"
pages: 109
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Dérivabilité — D. Cransac

## Page 1

Dérivabilité — D. Cransac, Analyse.

Plan :

1. Nombre dérivé, fonction dérivée, opérations : définitions ; opérations sur la dérivabilité ; dérivabilité de la fonction réciproque ; dérivées usuelles.
2. Dérivées successives, fonctions de classe $C^n$ : définitions ; formule de Leibniz.
3. Propriétés des fonctions dérivables : extremum local ; théorème de Rolle ; théorème des accroissements finis ; sens de variation et dérivabilité ; règle de l’Hospital.
4. Applications : dérivabilité de la fonction racine carrée ; réciproque de la fonction tangente ; détermination des dérivées de sinus et cosinus.

Les bandeaux de navigation et le pied de page « D. Cransac — Analyse » sont répétés dans le PDF. Les étapes successives d’affichage sont repérées page par page.

## Page 2

## Définition — dérivabilité en un point ou sur une partie de $\mathbb R$

Soit $f:D\to\mathbb C$ une fonction. Soit $a\in D$. On dit que $f$ est dérivable en $a$ si, lorsque $x$ tend vers $a$,

$$\frac{f(x)-f(a)}{x-a}$$

**admet une limite qui est finie**. Cette limite est appelée le nombre dérivé de $f$ en $a$, noté $f'(a)$.

$f$ est dérivable sur $D$ si elle est dérivable en tout point de $D$. La fonction $x\mapsto f'(x)$ est alors appelée la dérivée de $f$.

Remarques :

- On note $\mathcal D(D,\mathbb K)$ l’ensemble des fonctions dérivables sur $D$ à valeurs dans $\mathbb K$.
- Dans la notation $f'$, la variable $x$ est implicite. Pour éviter les ambiguïtés, notamment avec plusieurs variables, on peut noter le nombre dérivé $\frac{df}{dx}(a)$ et remplacer $x$ par un autre symbole.

## Page 3

## Définition — tangente

Soient $f:D\to\mathbb R$ et $a\in D$.

- Si $f$ est dérivable en $a$, la droite $y=f(a)+f'(a)(x-a)$ est appelée la tangente de $f$ en $a$.
- Si $\lim_{x\to a}(f(x)-f(a))/(x-a)=\pm\infty$, la droite $x=a$ est appelée la tangente de $f$ en $a$.

## Page 4

**Attention.** Ne pas confondre deux domaines mathématiques séparés :

- Analyse : fonction, réel, limite, taux de variation, dérivabilité.
- Géométrie : représentation graphique, point, coefficient directeur, tangente, asymptote.

## Page 5

**Attention.** Bien distinguer dérivabilité et existence d’une tangente à la courbe représentative.

Le taux $\frac{f(x)-f(a)}{x-a}$ admet en $a$…

| Analyse : limite du taux | Géométrie | Analyse : fonction |
| --- | --- | --- |
| Une limite finie | Tangente | Dérivable |
| Une limite infinie | Tangente verticale | Non dérivable |
| Pas de limite | Pas de tangente | Non dérivable |

## Page 6

## Définition — dérivabilité à gauche / à droite, demi-tangente

Soient $f:D\to\mathbb C$ et $a\in D$, au voisinage duquel $f$ est définie à gauche et à droite.

- $f$ est dérivable à gauche en $a$ si sa restriction à $D\cap]-\infty,a]$ est dérivable en $a$, c’est-à-dire si $\lim_{x\to a^-}(f(x)-f(a))/(x-a)$ existe et est finie. Cette limite est le nombre dérivé à gauche $f'_g(a)$.
- $f$ est dérivable à droite en $a$ si sa restriction à $D\cap[a,+\infty[$ est dérivable en $a$, c’est-à-dire si $\lim_{x\to a^+}(f(x)-f(a))/(x-a)$ existe et est finie. Cette limite est le nombre dérivé à droite $f'_d(a)$.

## Page 7

## Théorème — caractérisation par les dérivées à gauche et à droite

Soient $f:D\to\mathbb C$ et $a\in D$, au voisinage duquel $f$ est définie à gauche et à droite. $f$ est dérivable en $a$ si et seulement si elle est dérivable à gauche et à droite en $a$, avec $f'_g(a)=f'_d(a)$.

La valeur absolue est dérivable à gauche et à droite en $0$, mais pas en $0$, car $f'_g(0)=-1$ et $f'_d(0)=1$.

**Figure :** courbe en V de $x\mapsto|x|$, avec les deux demi-tangentes en $0$ de pentes $-1$ et $1$.

**Note de transcription :** la dernière inégalité de la phrase imprimée répète $f'_g(0)$ dans les deux membres ; elle doit comparer $f'_g(0)$ et $f'_d(0)$.

## Page 8

## Démonstration

$f$ est dérivable en $a$ si et seulement si $\lim_{x\to a}(f(x)-f(a))/(x-a)$ existe et est finie. Cela équivaut à l’existence de deux limites finies et égales à gauche et à droite :

$$\lim_{x\to a^-}\frac{f(x)-f(a)}{x-a}=\lim_{x\to a^+}\frac{f(x)-f(a)}{x-a}.$$

C’est exactement la dérivabilité à gauche et à droite avec $f'_g(a)=f'_d(a)$.

## Page 9

## Théorème — la dérivabilité implique la continuité

Soient $f:D\to\mathbb R$ et $a\in D$. Si $f$ est dérivable en $a$, alors $f$ est continue en $a$.

**Attention : la réciproque est fausse.** La valeur absolue n’est pas dérivable en $0$. Il existe même des fonctions continues sur tout $\mathbb R$ et dérivables en aucun point.

## Page 10

## Théorème — la dérivabilité implique la continuité

Soient $f:D\to\mathbb R$ et $a\in D$. Si $f$ est dérivable en $a$, alors $f$ est continue en $a$.

**Attention : la réciproque est fausse.** La valeur absolue n’est pas dérivable en $0$. Il existe même des fonctions continues sur tout $\mathbb R$ et dérivables en aucun point.

**Remarque du cours.** « Cette propriété n’a aucun intérêt pratique : on ne peut pas s’intéresser à la dérivabilité si on n’a pas vérifié que la fonction est continue. » Exemple donné : une fonction polynôme n’est pas « continue parce qu’elle est dérivable », mais « est continue et de plus dérivable ».

Ce commentaire exprime l’ordre de présentation choisi dans le cours ; l’implication du théorème reste mathématiquement utilisable.

## Page 11

## Théorème — opérations sur la dérivabilité

Soient $f,g:D\to\mathbb C$ et $a\in D$. On suppose $f$ et $g$ dérivables en $a$.

**1. Combinaison linéaire.** Pour tous $\lambda,\mu\in\mathbb C$, $\lambda f+\mu g$ est dérivable en $a$ et

$$(\lambda f+\mu g)'(a)=\lambda f'(a)+\mu g'(a).$$

## Page 12

## Théorème — opérations sur la dérivabilité

Soient $f,g:D\to\mathbb C$ et $a\in D$. On suppose $f$ et $g$ dérivables en $a$.

**1. Combinaison linéaire.** Pour tous $\lambda,\mu\in\mathbb C$, $\lambda f+\mu g$ est dérivable en $a$ et

$$(\lambda f+\mu g)'(a)=\lambda f'(a)+\mu g'(a).$$

**2. Produit.** $fg$ est dérivable en $a$ et $(fg)'(a)=f'(a)g(a)+f(a)g'(a)$.

La page imprime $(fg')'(a)$ au lieu de $(fg)'(a)$ ; la formule est corrigée dès la page suivante.

## Page 13

## Théorème — opérations sur la dérivabilité

Soient $f,g:D\to\mathbb C$ et $a\in D$. On suppose $f$ et $g$ dérivables en $a$.

**1. Combinaison linéaire.** Pour tous $\lambda,\mu\in\mathbb C$, $\lambda f+\mu g$ est dérivable en $a$ et

$$(\lambda f+\mu g)'(a)=\lambda f'(a)+\mu g'(a).$$

**2. Produit.** $fg$ est dérivable en $a$ et $(fg)'(a)=f'(a)g(a)+f(a)g'(a)$.

**3. Quotient.** Si $g(a)\ne0$, $f/g$ est dérivable en $a$ et

$$\left(\frac fg\right)'(a)=\frac{f'(a)g(a)-f(a)g'(a)}{g(a)^2}.$$

## Page 14

## Démonstration des opérations

Pour les assertions 2 et 3, remarquons que $\lim_{x\to a}g(x)=g(a)$ : la dérivabilité de $g$ en $a$ implique sa continuité.

$$\frac{(\lambda f+\mu g)(x)-(\lambda f+\mu g)(a)}{x-a}
=\lambda\frac{f(x)-f(a)}{x-a}+\mu\frac{g(x)-g(a)}{x-a}
\longrightarrow\lambda f'(a)+\mu g'(a).$$

$$\frac{(fg)(x)-(fg)(a)}{x-a}
=\frac{f(x)-f(a)}{x-a}g(x)+f(a)\frac{g(x)-g(a)}{x-a}
\longrightarrow f'(a)g(a)+f(a)g'(a).$$

Supposons $g(a)\ne0$. Comme $g$ est continue, elle est non nulle sur un intervalle ouvert $I$ contenant $a$. Pour $x\in I\setminus\{a\}$,

$$\frac{(1/g)(x)-(1/g)(a)}{x-a}
=-\frac1{g(x)g(a)}\frac{g(x)-g(a)}{x-a}\longrightarrow-\frac{g'(a)}{g(a)^2}.$$

## Page 15

## Théorème — composition

Soient $f:D\to E$, $g:E\to\mathbb C$ et $a\in D$. On suppose $f$ dérivable en $a$ et $g$ dérivable en $f(a)$. Alors $g\circ f$ est dérivable en $a$ et

$$(g\circ f)'(a)=f'(a)g'(f(a)).$$

## Page 16

## Démonstration

Pour tout $y\in E$, posons

$$\tau(y)=\begin{cases}\dfrac{g(y)-g(f(a))}{y-f(a)}&y\ne f(a),\\g'(f(a))&y=f(a).\end{cases}$$

Par dérivabilité de $g$ en $f(a)$, $\lim_{y\to f(a)}\tau(y)=g'(f(a))$. Pour tout $x\in D$,

$$\tau(f(x))(f(x)-f(a))=g\circ f(x)-g\circ f(a),$$

y compris pour $x=a$. De plus, $\lim_{x\to a}f(x)=f(a)$. Donc

$$\frac{g\circ f(x)-g\circ f(a)}{x-a}=\frac{f(x)-f(a)}{x-a}\tau(f(x))\longrightarrow f'(a)g'(f(a)).$$

**Note de transcription :** le PDF indique $x\in E$ dans l’identité ; le domaine correct de $x$ est $D$.

## Page 17

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

## Page 18

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

## Page 19

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

Nouvelle égalité : $\{M(f^{-1}(y),y):y\in E\}$.

## Page 20

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

Nouvelle égalité : $\{M(f^{-1}(y),y):y\in E\}$.

En renommant la variable : $\{M(f^{-1}(x),x):x\in E\}$.

## Page 21

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

Nouvelle égalité : $\{M(f^{-1}(y),y):y\in E\}$.

En renommant la variable : $\{M(f^{-1}(x),x):x\in E\}$.

## Page 22

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

Nouvelle égalité : $\{M(f^{-1}(y),y):y\in E\}$.

En renommant la variable : $\{M(f^{-1}(x),x):x\in E\}$.

## Page 23

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

Nouvelle égalité : $\{M(f^{-1}(y),y):y\in E\}$.

En renommant la variable : $\{M(f^{-1}(x),x):x\in E\}$.

Cet ensemble est le symétrique, par rapport à l’axe $y=x$, de l’ensemble $\{M(x,f^{-1}(x)):x\in E\}$.

## Page 24

## Définition — fonction réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$. On appelle fonction réciproque de $f$ la fonction $f^{-1}$ telle que, pour tout $x\in I$,

$$y=f(x)\quad\Longleftrightarrow\quad x=f^{-1}(y).$$

La représentation graphique de $f$ est l’ensemble

$$\{M(x,y):y=f(x),\ x\in D\}=\{M(x,f(x)):x\in D\}.$$

Le PDF passe aux noms $D,E$ pour les ensembles de départ et d’arrivée. **Figure :** une courbe rouge croissante de forme cubique, passant par l’origine et le point $(1,1)$.

Ajout à la représentation graphique : cet ensemble est aussi $\{M(x,y):f^{-1}(y)=x,\ y\in E\}$. La figure reste identique.

Nouvelle égalité : $\{M(f^{-1}(y),y):y\in E\}$.

En renommant la variable : $\{M(f^{-1}(x),x):x\in E\}$.

Cet ensemble est le symétrique, par rapport à l’axe $y=x$, de l’ensemble $\{M(x,f^{-1}(x)):x\in E\}$.

**Ajout à la figure :** la courbe de la réciproque est tracée en rouge plein, symétrique de la courbe cubique pointillée ; elle possède une tangente verticale à l’origine.

## Page 25

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Première étape d’affichage : seule cette hypothèse est visible.

## Page 26

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors… [suite de l’énoncé non encore affichée].

## Page 27

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors $f^{-1}$ est dérivable sur $J$.

## Page 28

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors $f^{-1}$ est dérivable sur $J$.

De plus, $(f^{-1})'=1/(f'\circ f^{-1})$.

## Page 29

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors $f^{-1}$ est dérivable sur $J$.

De plus, $(f^{-1})'=1/(f'\circ f^{-1})$.

**Attention :** l’hypothèse selon laquelle $f'$ ne s’annule pas est essentielle !

Deux repères encore vides sont placés sous l’énoncé.

## Page 30

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors $f^{-1}$ est dérivable sur $J$.

De plus, $(f^{-1})'=1/(f'\circ f^{-1})$.

**Attention :** l’hypothèse selon laquelle $f'$ ne s’annule pas est essentielle !

**Figure :** le repère de gauche montre une courbe cubique rouge avec une tangente horizontale à l’origine ; le repère de droite est encore vide.

## Page 31

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors $f^{-1}$ est dérivable sur $J$.

De plus, $(f^{-1})'=1/(f'\circ f^{-1})$.

**Attention :** l’hypothèse selon laquelle $f'$ ne s’annule pas est essentielle !

**Figures :** à gauche, courbe cubique et tangente horizontale à l’origine ; à droite, courbe réciproque et tangente verticale à l’origine. La réciproque n’est pas dérivable à cet endroit.

## Page 32

## Théorème — dérivabilité d’une réciproque

Soit $I$ un intervalle et $f\in\mathcal D(I,\mathbb R)$ bijective de $I$ sur $J=f(I)$.

Si $f'$ **ne s’annule pas sur $I$**, alors $f^{-1}$ est dérivable sur $J$.

De plus, $(f^{-1})'=1/(f'\circ f^{-1})$.

**Attention :** l’hypothèse selon laquelle $f'$ ne s’annule pas est essentielle !

**Figures :** à gauche, courbe cubique et tangente horizontale à l’origine ; à droite, courbe réciproque et tangente verticale à l’origine. La réciproque n’est pas dérivable à cet endroit.

La courbe cubique est ajoutée en pointillés dans le repère de droite, pour montrer la symétrie des courbes réciproques.

## Page 33

## Démonstration

Soit $b\in J$ et $a=f^{-1}(b)$. Comme $f$ est dérivable en $a$,

$$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=f'(a).$$

Après passage à l’inverse, autorisé puisque $f'(a)\ne0$,

$$\lim_{x\to a}\frac{x-a}{f(x)-f(a)}=\frac1{f'(a)}.$$

## Page 34

## Démonstration

Soit $b\in J$ et $a=f^{-1}(b)$. Comme $f$ est dérivable en $a$,

$$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=f'(a).$$

Après passage à l’inverse, autorisé puisque $f'(a)\ne0$,

$$\lim_{x\to a}\frac{x-a}{f(x)-f(a)}=\frac1{f'(a)}.$$

Comme $f$ est continue et bijective sur un intervalle, $f^{-1}$ est continue en $b$ : $\lim_{y\to b}f^{-1}(y)=f^{-1}(b)=a$.

## Page 35

## Démonstration

Soit $b\in J$ et $a=f^{-1}(b)$. Comme $f$ est dérivable en $a$,

$$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=f'(a).$$

Après passage à l’inverse, autorisé puisque $f'(a)\ne0$,

$$\lim_{x\to a}\frac{x-a}{f(x)-f(a)}=\frac1{f'(a)}.$$

Comme $f$ est continue et bijective sur un intervalle, $f^{-1}$ est continue en $b$ : $\lim_{y\to b}f^{-1}(y)=f^{-1}(b)=a$.

On peut donc remplacer $x$ par $f^{-1}(y)$ et $a$ par $f^{-1}(b)$. Par composition,

$$\begin{aligned}\lim_{y\to b}\frac{f^{-1}(y)-f^{-1}(b)}{y-b}
&=\lim_{y\to b}\frac{f^{-1}(y)-f^{-1}(b)}{f(f^{-1}(y))-f(f^{-1}(b))}\\
&=\frac1{f'(f^{-1}(b))}.
\end{aligned}$$

## Page 36

## Remarque sur la démonstration de la composition

On pourrait penser à écrire le taux de variation ainsi :

$$\frac{g(f(x))-g(f(a))}{x-a}
=\frac{g(f(x))-g(f(a))}{f(x)-f(a)}\frac{f(x)-f(a)}{x-a}.$$

## Page 37

## Remarque sur la démonstration de la composition

On pourrait penser à écrire le taux de variation ainsi :

$$\frac{g(f(x))-g(f(a))}{x-a}
=\frac{g(f(x))-g(f(a))}{f(x)-f(a)}\frac{f(x)-f(a)}{x-a}.$$

Mais on divise alors par $f(x)-f(a)$, qui pourrait être nul : cela pose un problème et explique l’introduction de la fonction $\tau$.

## Page 38

## Principales formules à connaître

$x$ est une variable ; $u$ représente une fonction $x\mapsto u(x)$. Les formules s’appliquent sur les domaines où les expressions et leurs dérivées sont définies.

| Fonction | Dérivée | Composée | Dérivée de la composée |
| --- | --- | --- | --- |
| $x^n$, $n\in\mathbb Z$ | $nx^{n-1}$ | $u^n$ | $nu'u^{n-1}$ |
| $1/x$ | $-1/x^2$ | $1/u$ | $-u'/u^2$ |
| $\sqrt x$ | $1/(2\sqrt x)$ | $\sqrt u$ | $u'/(2\sqrt u)$ |
| $x^\alpha$, $\alpha\in\mathbb R$ | $\alpha x^{\alpha-1}$ | $u^\alpha$ | $\alpha u'u^{\alpha-1}$ |
| $e^x$ | $e^x$ | $e^u$ | $u'e^u$ |
| $\ln x$ | $1/x$ | $\ln u$ | $u'/u$ |
| $\cos x$ | $-\sin x$ | $\cos u$ | $-u'\sin u$ |
| $\sin x$ | $\cos x$ | $\sin u$ | $u'\cos u$ |
| $\tan x$ | $1+\tan^2x=1/\cos^2x$ | $\tan u$ | $u'(1+\tan^2u)=u'/\cos^2u$ |

## Page 39

## Définition — dérivées successives

Soit $f:D\to\mathbb C$. On pose $f^{(0)}=f$. Pour $k\in\mathbb N$, $P_k$ signifie : « $f^{(k)}$ est définie et dérivable sur $D$ ». Lorsque les dérivées nécessaires existent, on définit $f^{(n+1)}=(f^{(n)})'$ sur $D$.

$f^{(k)}$ est appelée dérivée $k$-ième de $f$. On dit que $f$ est $k$ fois dérivable sur $D$.

Remarques :

1. On note généralement $f,f^{\prime},f^{\prime\prime},f^{\prime\prime\prime}$ plutôt que $f^{(0)},f^{(1)},f^{(2)},f^{(3)}$.
2. On peut noter la dérivée $k$-ième $d^kf/dx^k$.

**Notes de transcription :** pour définir $f^{(n+1)}$, le PDF demande $P_k$ pour $k<n$ ; il faut aussi la dérivabilité de $f^{(n)}$, donc $P_n$. La seconde remarque parle de dérivée « $n$-ième » mais affiche l’indice $k$ ; les indices sont harmonisés.

## Page 40

## Définition — fonction de classe $C^k$

Soit $f:D\to\mathbb C$.

- Pour $k\in\mathbb N$, $f$ est de classe $C^k$ sur $D$ si elle est $k$ fois dérivable et si $f^{(k)}$ est continue sur $D$. On note $C^k(D,\mathbb K)$ l’ensemble de ces fonctions à valeurs dans $\mathbb K$.
- $f$ est de classe $C^\infty$ sur $D$ si elle est dérivable autant de fois qu’on le veut.
- On note $C^\infty(D,\mathbb K)$ l’ensemble de ces fonctions.

**Attention :** être $C^1$ signifie « dérivable à dérivée continue », et pas seulement « dérivable et continue ».

## Page 41

## Schéma d’implications

Classe $C^\infty$ ⇒ … ⇒ classe $C^2$ ⇒ dérivabilité deux fois ⇒ classe $C^1$ ⇒ dérivabilité ⇒ continuité = classe $C^0$.

## Page 42

## Proposition

Soient $n\in\mathbb N$, $f,g\in C^n(I,\mathbb R)$ et $\lambda,\mu\in\mathbb R$. Alors $\lambda f+\mu g\in C^n(I,\mathbb R)$ et

$$(\lambda f+\mu g)^{(n)}=\lambda f^{(n)}+\mu g^{(n)}.$$

On dit que l’ensemble des fonctions de classe $C^n$ est un $\mathbb R$-espace vectoriel.

## Page 43

## Démonstration

Montrons par récurrence $\mathcal P(n)$ : si $f,g$ sont $C^n$, alors $\lambda f+\mu g$ est $C^n$ et $(\lambda f+\mu g)^{(n)}=\lambda f^{(n)}+\mu g^{(n)}$.

Pour $n=0$, $\mathcal P(0)$ a été vue au chapitre précédent.

Supposons $\mathcal P(n)$ vraie et $f,g$ de classe $C^{n+1}$. Elles sont $C^n$ ; l’hypothèse de récurrence donne donc $\lambda f+\mu g\in C^n$ et la formule à l’ordre $n$. Puisque $f^{(n)}$ et $g^{(n)}$ sont $C^1$, cette combinaison est dérivable, de dérivée continue

$$(\lambda f+\mu g)^{(n+1)}=\lambda f^{(n+1)}+\mu g^{(n+1)}.$$

Ainsi $\lambda f+\mu g$ est $C^{n+1}$ et $\mathcal P(n+1)$ est vraie. Conclusion : $\mathcal P(n)$ est vraie pour tout $n\in\mathbb N$.

Le PDF rattache la dérivabilité de la combinaison linéaire à $\mathcal P(0)$ ; elle vient du théorème de dérivation de la page 11, tandis que $\mathcal P(0)$ porte sur la continuité.

## Page 44

## Formule de Leibniz

Soient $n\in\mathbb N$ et $f,g:I\to\mathbb R$ de classe $C^n$. Alors $fg$ est de classe $C^n$ sur $I$ et

$$(fg)^{(n)}=\sum_{k=0}^n\binom nk f^{(k)}g^{(n-k)}.$$

## Page 45

## Démonstration — initialisation

On montre par récurrence la propriété $\mathcal P(n)$ : si $f,g$ sont $C^n$ sur $I$, alors $fg$ est $C^n$ et vérifie la formule de Leibniz.

Si $f,g$ sont continues, $fg$ est continue et

$$\sum_{k=0}^0\binom0k f^{(k)}g^{(0-k)}=\binom00 f^{(0)}g^{(0)}=fg=(fg)^{(0)}.$$

Donc $\mathcal P(0)$ est vraie. Au rang $k$, l’hypothèse est : pour tous $f,g\in C^k(D,\mathbb C)$, $fg\in C^k(D,\mathbb C)$ et

$$(fg)^{(k)}=\sum_{p=0}^k\binom kp f^{(p)}g^{(k-p)}.$$

La preuve passe aux fonctions complexes et au nom $D$ pour le domaine ; le raisonnement est le même. L’exposant $(n)$ de dérivation est imprimé sans parenthèses dans la première formule du PDF.

## Page 46

## Démonstration — hérédité, régularité

Soit $k\in\mathbb N$ et supposons $\mathcal P(k)$ vraie. Soient $f,g\in C^{k+1}(D,\mathbb C)$.

Elles sont $C^1$, donc $fg\in C^1$ et $(fg)'=f'g+fg'$. Par l’hypothèse de récurrence, $f'g$ et $fg'$ sont $C^k$. Ainsi $(fg)'\in C^k$, c’est-à-dire $fg\in C^{k+1}$.

## Page 47

## Démonstration — hérédité, formule

$$\begin{aligned}(fg)^{(k+1)}
&=((fg)')^{(k)}=(f'g)^{(k)}+(fg')^{(k)}\\
&=\sum_{p=0}^k\binom kp(f')^{(p)}g^{(k-p)}+\sum_{p=0}^k\binom kp f^{(p)}(g')^{(k-p)}\\
&=\sum_{p=0}^k\binom kp f^{(p+1)}g^{(k-p)}+\sum_{p=0}^k\binom kp f^{(p)}g^{(k-p+1)}\\
&=\sum_{p=1}^{k+1}\binom k{p-1}f^{(p)}g^{(k-p+1)}+\sum_{p=0}^k\binom kp f^{(p)}g^{(k-p+1)}\\
&=\underbrace{f^{(0)}g^{(k+1)}}_{p=0}+\sum_{p=1}^k\binom{k+1}p f^{(p)}g^{(k+1-p)}+\underbrace{f^{(k+1)}g^{(0)}}_{p=k+1}\\
&=\sum_{p=0}^{k+1}\binom{k+1}p f^{(p)}g^{(k+1-p)}.
\end{aligned}$$

Le passage aux deux premières sommes utilise l’hypothèse de récurrence (« HDR » dans le PDF).

## Page 48

## Propositions

1. Soient $f,g:I\to\mathbb R$ de classe $C^n$. Si $g$ ne s’annule pas, alors $f/g$ est $C^n$ sur $I$.
2. Soient $f:I\to\mathbb R$ et $g:J\to\mathbb R$ de classe $C^n$ sur leurs intervalles respectifs, avec $f(I)\subset J$. Alors $g\circ f$ est $C^n$ sur $I$.
3. Soit $f:I\to J$ bijective, $C^n$ sur $I$, avec $f'$ ne s’annulant pas. Alors $f^{-1}$ est $C^n$ sur $J$.

Dans 2, le PDF écrit « deux fonctions $C^n$ sur $I$ » alors que $g$ est définie sur $J$ ; les domaines sont explicités ci-dessus.

## Page 49

## Définition — maximum local

Soit $f:I\to\mathbb R$. $f$ admet un maximum local en $a$ s’il existe $\eta>0$ tel que sa restriction à $I\cap[a-\eta,a+\eta]$ admette un maximum en $a$, c’est-à-dire

$$\forall x\in I\cap[a-\eta,a+\eta],\quad f(x)\le f(a).$$

**Figure :** une courbe possède un minimum global, un maximum, un point d’inflexion à tangente horizontale, puis un minimum local plus haut que le minimum global. Les tangentes horizontales sont marquées.

## Page 50

## Définition — maximum local

Soit $f:I\to\mathbb R$. $f$ admet un maximum local en $a$ s’il existe $\eta>0$ tel que sa restriction à $I\cap[a-\eta,a+\eta]$ admette un maximum en $a$, c’est-à-dire

$$\forall x\in I\cap[a-\eta,a+\eta],\quad f(x)\le f(a).$$

$f$ admet un minimum local en $a$ s’il existe $\eta>0$ tel que sa restriction à $I\cap[a-\eta,a+\eta]$ admette un minimum en $a$, soit $f(a)\le f(x)$ pour tout $x$ de cet ensemble.

$f$ admet un extremum local en $a$ si elle y admet un maximum ou un minimum local.

## Page 51

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

Le cadre « Démonstration » est encore vide.

## Page 52

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

## Page 53

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

**Figure :** maximum en $a$ d’une courbe sur $[c,d]$ ; les verticales en $a\pm\eta$ et $a\pm\delta$ montrent le voisinage intérieur retenu, avec une tangente horizontale en $a$.

## Page 54

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

Le cadre « Démonstration » est encore vide.

## Page 55

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

## Page 56

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

Pour tout $x\in[a-\delta,a[$, $\frac{f(x)-f(a)}{x-a}\ge0$, car $f(x)-f(a)\le0$ et $x-a<0$.

## Page 57

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

Pour tout $x\in[a-\delta,a[$, $\frac{f(x)-f(a)}{x-a}\ge0$, car $f(x)-f(a)\le0$ et $x-a<0$. On passe à la limite quand $x\to a^-$… [conclusion à la page suivante].

## Page 58

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

Pour tout $x\in[a-\delta,a[$, $\frac{f(x)-f(a)}{x-a}\ge0$, car $f(x)-f(a)\le0$ et $x-a<0$. En passant à la limite quand $x\to a^-$, puisque $f$ est dérivable en $a$, on obtient $f'(a)=f'_g(a)\ge0$.

## Page 59

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

Pour tout $x\in[a-\delta,a[$, $\frac{f(x)-f(a)}{x-a}\ge0$, car $f(x)-f(a)\le0$ et $x-a<0$. En passant à la limite quand $x\to a^-$, puisque $f$ est dérivable en $a$, on obtient $f'(a)=f'_g(a)\ge0$.

De même, pour $x\in]a,a+\delta]$, $\frac{f(x)-f(a)}{x-a}\le0$, car $f(x)-f(a)\le0$ et $x-a>0$.

## Page 60

## Proposition — condition nécessaire d’extremum

Soit $f:I\to\mathbb R$ dérivable. Si $f$ admet un extremum local en un point $a$ intérieur à $I$ (c’est-à-dire $a\in I$ et $a$ n’est pas une extrémité de $I$), alors $f'(a)=0$.

**Démonstration.** Quitte à remplacer $f$ par $-f$, supposons que $f$ admet en $a$ un maximum local.

Il existe $\eta>0$ tel que, pour tout $x\in[a-\eta,a+\eta]\cap I$, $f(x)\le f(a)$. Comme $a$ n’est pas une extrémité de $I$, il existe $\nu>0$ tel que $[a-\nu,a+\nu]\subset I$.

Posons $\delta=\min(\eta,\nu)>0$. Pour tout $x\in[a-\delta,a+\delta]$, $f(x)\le f(a)$.

Pour tout $x\in[a-\delta,a[$, $\frac{f(x)-f(a)}{x-a}\ge0$, car $f(x)-f(a)\le0$ et $x-a<0$. En passant à la limite quand $x\to a^-$, puisque $f$ est dérivable en $a$, on obtient $f'(a)=f'_g(a)\ge0$.

De même, pour $x\in]a,a+\delta]$, $\frac{f(x)-f(a)}{x-a}\le0$, car $f(x)-f(a)\le0$ et $x-a>0$. En passant à la limite quand $x\to a^+$, on obtient $f'(a)=f'_d(a)\le0$. Ainsi $f'(a)=0$.

## Page 61

## Remarques

- $f'(a)=0$ n’implique pas un extremum local en $a$. Exemple : $f(x)=x^3$ satisfait $f'(0)=0$ sans extremum local en $0$.
- L’hypothèse « $a$ intérieur à $I$ » est essentielle : l’identité sur $[0,1]$ a son minimum en $0$, son maximum en $1$, mais $f'(0)=f'(1)=1\ne0$.
- Pour déterminer les extrema d’une fonction dérivable, résoudre $f'(x)=0$ aux points intérieurs et vérifier si les points obtenus sont des extrema locaux, par exemple avec un tableau de variations. Étudier aussi les extrémités de $I$ lorsqu’elles appartiennent à $I$.

**Note de transcription :** l’exemple de l’identité est imprimé $x\in[0,1]\mapsto[0,1]$ ; son expression attendue est $x\mapsto x$.

## Page 62

## Théorème de Rolle

Soit $f:[a,b]\to\mathbb R$, continue sur $[a,b]$, dérivable sur $]a,b[$, telle que $f(a)=f(b)$. Il existe $c\in]a,b[$ tel que $f'(c)=0$.

## Page 63

## Remarque — chaque hypothèse a son importance

Quatre figures :

1. **Hypothèses vérifiées :** courbe lisse avec $f(a)=f(b)$, un minimum et un maximum intérieurs à tangentes horizontales.
2. **Pas de dérivabilité en un point :** $f(a)=f(b)$, mais le sommet de la courbe est anguleux ; aucune tangente horizontale n’est représentée.
3. **Pas de continuité sur $[a,b]$ :** $f(a)=f(b)$, mais le point isolé en $a$ est au-dessous de la limite à droite ; la courbe décroît jusqu’à $b$.
4. **$f(a)\ne f(b)$ :** courbe croissante dont les deux valeurs aux extrémités diffèrent.

## Page 64

## Démonstration de Rolle

Comme $f$ est continue sur le segment $[a,b]$, elle est bornée et atteint son minimum $m$ et son maximum $M$.

- Si $f(a)=f(b)\ne M$, le maximum est atteint en un $c\in]a,b[$. Ce point n’est pas une borne du segment, donc $f'(c)=0$ par la condition nécessaire d’extremum.
- Si $f(a)=f(b)\ne m$, même raisonnement avec le minimum.
- Si $f(a)=f(b)=m=M$, $f$ est constante, de valeur $M=m$ sur tout $[a,b]$, donc sa dérivée est nulle, en particulier sur $]a,b[$.

## Page 65

## Théorème des accroissements finis

Soit $f:[a,b]\to\mathbb R$ continue sur $[a,b]$ et dérivable sur $]a,b[$. Il existe $c\in]a,b[$ tel que

$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad\text{ou encore}\qquad f(b)-f(a)=f'(c)(b-a).$$

Ce théorème généralise celui de Rolle.

**Des informations sur $f'$ donnent des informations sur $f$.** Il est très utile pour transformer une majoration ou minoration de $f'$ en une majoration ou minoration sur $f$.

## Page 66

## Démonstration

Posons $\phi(x)=f(x)-\frac{f(b)-f(a)}{b-a}(x-a)-f(a)$.

$\phi$ est la somme de $f$ et d’une fonction affine ; elle est continue sur $[a,b]$ et dérivable sur $]a,b[$. On a $\phi(a)=\phi(b)=0$. On peut donc lui appliquer Rolle : il existe $c\in]a,b[$ tel que $\phi'(c)=0$.

Ainsi $f'(c)+\frac{f(a)-f(b)}{b-a}=0$, soit $f'(c)=\frac{f(b)-f(a)}{b-a}$.

**Coquilles de la source :** le texte dit « fonction linéaire » au lieu d’affine. Les calculs imprimés de $\phi(a)$ et $\phi(b)$ omettent le terme $-f(a)$ de la définition et donnent tous deux $f(a)$ ; l’égalité des deux valeurs reste vraie, mais avec la définition écrite elles valent $0$. La dernière ligne écrit $f'(x)$ au lieu de $f'(c)$.

## Page 67

## Théorème — sens de variation et dérivabilité

Soit $f:I\to\mathbb R$ dérivable sur un intervalle $I$.

- $f$ est constante sur $I$ si et seulement si $f'$ est nulle sur $I$.
- $f$ est croissante (respectivement décroissante) sur $I$ si et seulement si $f'$ est positive (respectivement négative) sur $I$, au sens large.

## Page 68

## Démonstration

Le cadre de démonstration est vide à cette étape d’affichage.

## Page 69

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

## Page 70

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$.

## Page 71

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

## Page 72

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

Pour la monotonie, traitons le cas croissant ; le cas décroissant s’en déduit en remplaçant $f$ par $-f$.

## Page 73

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

Pour la monotonie, traitons le cas croissant ; le cas décroissant s’en déduit en remplaçant $f$ par $-f$.

Sens direct : soit $a\in I$. Pour tout $x\in I\setminus\{a\}$, $\frac{f(x)-f(a)}{x-a}\ge0$.

## Page 74

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

Pour la monotonie, traitons le cas croissant ; le cas décroissant s’en déduit en remplaçant $f$ par $-f$.

Sens direct : soit $a\in I$. Pour tout $x\in I\setminus\{a\}$, $\frac{f(x)-f(a)}{x-a}\ge0$. En faisant tendre $x$ vers $a$, le passage à la limite dans les inégalités donne $f'(a)\ge0$ pour tout $a\in I$.

## Page 75

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

Pour la monotonie, traitons le cas croissant ; le cas décroissant s’en déduit en remplaçant $f$ par $-f$.

Sens direct : soit $a\in I$. Pour tout $x\in I\setminus\{a\}$, $\frac{f(x)-f(a)}{x-a}\ge0$. En faisant tendre $x$ vers $a$, le passage à la limite dans les inégalités donne $f'(a)\ge0$ pour tout $a\in I$.

Réciproquement, supposons $f'$ à valeurs positives. Soit $(x,y)\in I^2$ avec $x<y$.

## Page 76

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

Pour la monotonie, traitons le cas croissant ; le cas décroissant s’en déduit en remplaçant $f$ par $-f$.

Sens direct : soit $a\in I$. Pour tout $x\in I\setminus\{a\}$, $\frac{f(x)-f(a)}{x-a}\ge0$. En faisant tendre $x$ vers $a$, le passage à la limite dans les inégalités donne $f'(a)\ge0$ pour tout $a\in I$.

Réciproquement, supposons $f'$ à valeurs positives. Soit $(x,y)\in I^2$ avec $x<y$. Par les accroissements finis, il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)\ge0$, car $f'(c)\ge0$ et $y-x>0$.

## Page 77

## Démonstration

Sens direct de « constante ⇒ dérivée nulle » : immédiat.

Réciproquement, supposons $f'=0$ sur $I$ et soient $x,y\in I$ avec $x<y$. Par le théorème des accroissements finis entre $x$ et $y$ ($f$ est continue sur $[x,y]$ et dérivable sur $]x,y[$ car dérivable sur $I$), il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)=0$. Donc $f(x)=f(y)$.

Pour la monotonie, traitons le cas croissant ; le cas décroissant s’en déduit en remplaçant $f$ par $-f$.

Sens direct : soit $a\in I$. Pour tout $x\in I\setminus\{a\}$, $\frac{f(x)-f(a)}{x-a}\ge0$. En faisant tendre $x$ vers $a$, le passage à la limite dans les inégalités donne $f'(a)\ge0$ pour tout $a\in I$.

Réciproquement, supposons $f'$ à valeurs positives. Soit $(x,y)\in I^2$ avec $x<y$. Par les accroissements finis, il existe $c\in]x,y[$ tel que $f(y)-f(x)=f'(c)(y-x)\ge0$, car $f'(c)\ge0$ et $y-x>0$. Ainsi $f(y)\ge f(x)$ et $f$ est croissante.

## Page 78

## Théorème — stricte monotonie

Soit $f:I\to\mathbb R$ dérivable sur un intervalle $I$. Si $f'$ est strictement positive (respectivement strictement négative), sauf éventuellement en un nombre fini de points de $I$ où elle s’annule, alors $f$ est strictement croissante (respectivement strictement décroissante).

## Page 79

## Théorème — stricte monotonie

Soit $f:I\to\mathbb R$ dérivable sur un intervalle $I$. Si $f'$ est strictement positive (respectivement strictement négative), sauf éventuellement en un nombre fini de points de $I$ où elle s’annule, alors $f$ est strictement croissante (respectivement strictement décroissante).

**Démonstration.** Par l’absurde, si $f$ n’est pas strictement croissante, il existe $c<d$ dans $I$ tels que $f(c)=f(d)$.

## Page 80

## Théorème — stricte monotonie

Soit $f:I\to\mathbb R$ dérivable sur un intervalle $I$. Si $f'$ est strictement positive (respectivement strictement négative), sauf éventuellement en un nombre fini de points de $I$ où elle s’annule, alors $f$ est strictement croissante (respectivement strictement décroissante).

**Démonstration.** Par l’absurde, si $f$ n’est pas strictement croissante, il existe $c<d$ dans $I$ tels que $f(c)=f(d)$. Comme $f$ est croissante, sa restriction à $[c,d]$ est constante…

## Page 81

## Théorème — stricte monotonie

Soit $f:I\to\mathbb R$ dérivable sur un intervalle $I$. Si $f'$ est strictement positive (respectivement strictement négative), sauf éventuellement en un nombre fini de points de $I$ où elle s’annule, alors $f$ est strictement croissante (respectivement strictement décroissante).

**Démonstration.** Par l’absurde, si $f$ n’est pas strictement croissante, il existe $c<d$ dans $I$ tels que $f(c)=f(d)$. Comme $f$ est croissante, sa restriction à $[c,d]$ est constante, donc $f'$ est nulle sur le segment $[c,d]$.

## Page 82

## Théorème — stricte monotonie

Soit $f:I\to\mathbb R$ dérivable sur un intervalle $I$. Si $f'$ est strictement positive (respectivement strictement négative), sauf éventuellement en un nombre fini de points de $I$ où elle s’annule, alors $f$ est strictement croissante (respectivement strictement décroissante).

**Démonstration.** Par l’absurde, si $f$ n’est pas strictement croissante, il existe $c<d$ dans $I$ tels que $f(c)=f(d)$. Comme $f$ est croissante, sa restriction à $[c,d]$ est constante, donc $f'$ est nulle sur le segment $[c,d]$. Cela contredit l’hypothèse de départ ; donc $f$ est strictement croissante.

## Page 83

## Fonctions lipschitziennes — rappel

Soit $f:I\to\mathbb R$ et $k\ge0$. On dit que $f$ est $k$-lipschitzienne (ou lipschitzienne de rapport $k$) sur $I$ si

$$\forall(x,y)\in I^2,\quad|f(x)-f(y)|\le k|x-y|.$$

## Page 84

## Fonctions lipschitziennes — rappel

Soit $f:I\to\mathbb R$ et $k\ge0$. On dit que $f$ est $k$-lipschitzienne (ou lipschitzienne de rapport $k$) sur $I$ si

$$\forall(x,y)\in I^2,\quad|f(x)-f(y)|\le k|x-y|.$$

**Théorème.** Soit $f:I\to\mathbb R$ dérivable sur $I$. Si $f'$ est bornée en valeur absolue par $M\ge0$, alors $f$ est $M$-lipschitzienne sur $I$.

## Page 85

## Fonctions lipschitziennes — rappel

Soit $f:I\to\mathbb R$ et $k\ge0$. On dit que $f$ est $k$-lipschitzienne (ou lipschitzienne de rapport $k$) sur $I$ si

$$\forall(x,y)\in I^2,\quad|f(x)-f(y)|\le k|x-y|.$$

**Théorème.** Soit $f:I\to\mathbb R$ dérivable sur $I$. Si $f'$ est bornée en valeur absolue par $M\ge0$, alors $f$ est $M$-lipschitzienne sur $I$.

**Démonstration.** Appliquer l’inégalité des accroissements finis sur tout segment $[x,y]$ : $|f(x)-f(y)|\le M|x-y|$.

## Page 86

## Règle de l’Hospital — théorème

Soient $f,g:I\to\mathbb R$ deux fonctions dérivables et $x_0\in I$. On suppose $f(x_0)=g(x_0)=0$.

Première étape d’affichage des hypothèses.

## Page 87

## Règle de l’Hospital — théorème

Soient $f,g:I\to\mathbb R$ deux fonctions dérivables et $x_0\in I$. On suppose $f(x_0)=g(x_0)=0$.

On suppose aussi $g'(x)\ne0$ pour tout $x\in I\setminus\{x_0\}$.

## Page 88

## Règle de l’Hospital — théorème

Soient $f,g:I\to\mathbb R$ deux fonctions dérivables et $x_0\in I$. On suppose $f(x_0)=g(x_0)=0$.

On suppose aussi $g'(x)\ne0$ pour tout $x\in I\setminus\{x_0\}$.

Si $\lim_{x\to x_0}f'(x)/g'(x)=\ell\in\mathbb R$, alors $\lim_{x\to x_0}f(x)/g(x)=\ell$.

## Page 89

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

## Page 90

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$.

## Page 91

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$.

## Page 92

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

## Page 93

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$.

## Page 94

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$. Or $h'(x)=g(a)f'(x)-f(a)g'(x)$.

## Page 95

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$. Or $h'(x)=g(a)f'(x)-f(a)g'(x)$. Donc $g(a)f'(c_a)-f(a)g'(c_a)=0$.

## Page 96

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$. Or $h'(x)=g(a)f'(x)-f(a)g'(x)$. Donc $g(a)f'(c_a)-f(a)g'(c_a)=0$.

Comme $g'$ ne s’annule pas sur $I\setminus\{x_0\}$, cela conduit à… [quotient affiché page suivante].

## Page 97

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$. Or $h'(x)=g(a)f'(x)-f(a)g'(x)$. Donc $g(a)f'(c_a)-f(a)g'(c_a)=0$.

Comme $g'$ ne s’annule pas sur $I\setminus\{x_0\}$, cela conduit à $f(a)/g(a)=f'(c_a)/g'(c_a)$.

**Précision de transcription :** $g(a)\ne0$ découle également de Rolle, puisque $g(x_0)=0$ et $g'$ ne s’annule pas entre $a$ et $x_0$.

## Page 98

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$. Or $h'(x)=g(a)f'(x)-f(a)g'(x)$. Donc $g(a)f'(c_a)-f(a)g'(c_a)=0$.

Comme $g'$ ne s’annule pas sur $I\setminus\{x_0\}$, cela conduit à $f(a)/g(a)=f'(c_a)/g'(c_a)$.

**Précision de transcription :** $g(a)\ne0$ découle également de Rolle, puisque $g(x_0)=0$ et $g'$ ne s’annule pas entre $a$ et $x_0$.

Comme $a<c_a<x_0$, lorsque $a\to x_0$, on obtient $c_a\to x_0$.

## Page 99

## Démonstration de la règle de l’Hospital

Fixons $a\in I\setminus\{x_0\}$, avec par exemple $a<x_0$. Soit $h:I\to\mathbb R$ définie par $h(x)=g(a)f(x)-f(a)g(x)$.

$h$ est continue sur $[a,x_0]\subset I$. Elle est dérivable sur $]a,x_0[$. De plus, $h(x_0)=h(a)=0$.

Par Rolle, il existe $c_a\in]a,x_0[$ tel que $h'(c_a)=0$. Or $h'(x)=g(a)f'(x)-f(a)g'(x)$. Donc $g(a)f'(c_a)-f(a)g'(c_a)=0$.

Comme $g'$ ne s’annule pas sur $I\setminus\{x_0\}$, cela conduit à $f(a)/g(a)=f'(c_a)/g'(c_a)$.

**Précision de transcription :** $g(a)\ne0$ découle également de Rolle, puisque $g(x_0)=0$ et $g'$ ne s’annule pas entre $a$ et $x_0$.

Comme $a<c_a<x_0$, lorsque $a\to x_0$, on obtient $c_a\to x_0$.

Cela implique

$$\lim_{a\to x_0}\frac{f(a)}{g(a)}=\lim_{a\to x_0}\frac{f'(c_a)}{g'(c_a)}=\lim_{c_a\to x_0}\frac{f'(c_a)}{g'(c_a)}=\ell.$$

## Page 100

## Exercice — dérivabilité de $x\mapsto\sqrt x$

En $0$ :

$$\frac{\sqrt x-\sqrt0}{x-0}=\frac{\sqrt x}x=\frac1{\sqrt x}\xrightarrow[x\to0^+]{}+\infty.$$

La limite est infinie : la fonction n’est pas dérivable en $0$, mais sa courbe admet une tangente verticale.

En $a>0$, le taux de variation vaut

$$\frac{\sqrt x-\sqrt a}{x-a}
=\frac{\sqrt x-\sqrt a}{x-a}\frac{\sqrt x+\sqrt a}{\sqrt x+\sqrt a}
=\frac{x-a}{(x-a)(\sqrt x+\sqrt a)}=\frac1{\sqrt x+\sqrt a}.$$

Donc $\lim_{x\to a}\frac{\sqrt x-\sqrt a}{x-a}=1/(2\sqrt a)$ : la fonction est dérivable en $a$.

**Note de transcription :** la phrase suivant le calcul imprime $1/\sqrt{2a}$ ; la dérivée correcte, obtenue juste au-dessus, est $1/(2\sqrt a)$.

La fin de la diapositive répète le cas $a=0$, sa limite infinie, l’absence de dérivabilité et l’existence de la tangente verticale.

## Page 101

## Étude de la tangente et de sa réciproque

On définit la tangente sur $I=]-\pi/2,\pi/2[$ à valeurs dans $\mathbb R$ par $f(x)=\tan x=\sin x/\cos x$.

## Page 102

## Étude de la tangente et de sa réciproque

On définit la tangente sur $I=]-\pi/2,\pi/2[$ à valeurs dans $\mathbb R$ par $f(x)=\tan x=\sin x/\cos x$.

$f$ est dérivable sur $I$ et

$$f'(x)=\frac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\frac1{\cos^2x}=1+\tan^2x.$$

**Coquille de la source :** le second produit du numérateur est écrit $(-\sin x)\cos x$ ; il doit être $(-\sin x)\sin x$.

## Page 103

## Étude de la tangente et de sa réciproque

On définit la tangente sur $I=]-\pi/2,\pi/2[$ à valeurs dans $\mathbb R$ par $f(x)=\tan x=\sin x/\cos x$.

$f$ est dérivable sur $I$ et

$$f'(x)=\frac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\frac1{\cos^2x}=1+\tan^2x.$$

**Coquille de la source :** le second produit du numérateur est écrit $(-\sin x)\cos x$ ; il doit être $(-\sin x)\sin x$.

Pour $x\in I$, $\cos x\ge0$ ; $\lim_{x\to(\pi/2)^-}\tan x=+\infty$ et $\lim_{x\to(-\pi/2)^+}\tan x=-\infty$. Les limites se prennent dans $I$.

## Page 104

## Étude de la tangente et de sa réciproque

On définit la tangente sur $I=]-\pi/2,\pi/2[$ à valeurs dans $\mathbb R$ par $f(x)=\tan x=\sin x/\cos x$.

$f$ est dérivable sur $I$ et

$$f'(x)=\frac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\frac1{\cos^2x}=1+\tan^2x.$$

**Coquille de la source :** le second produit du numérateur est écrit $(-\sin x)\cos x$ ; il doit être $(-\sin x)\sin x$.

Pour $x\in I$, $\cos x\ge0$ ; $\lim_{x\to(\pi/2)^-}\tan x=+\infty$ et $\lim_{x\to(-\pi/2)^+}\tan x=-\infty$. Les limites se prennent dans $I$.

Comme $f'(x)>0$ sur $I$, $f$ est strictement croissante. Elle est aussi continue et réalise donc une bijection de $I$ sur $\mathbb R$.

## Page 105

## Étude de la tangente et de sa réciproque

On définit la tangente sur $I=]-\pi/2,\pi/2[$ à valeurs dans $\mathbb R$ par $f(x)=\tan x=\sin x/\cos x$.

$f$ est dérivable sur $I$ et

$$f'(x)=\frac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\frac1{\cos^2x}=1+\tan^2x.$$

**Coquille de la source :** le second produit du numérateur est écrit $(-\sin x)\cos x$ ; il doit être $(-\sin x)\sin x$.

Pour $x\in I$, $\cos x\ge0$ ; $\lim_{x\to(\pi/2)^-}\tan x=+\infty$ et $\lim_{x\to(-\pi/2)^+}\tan x=-\infty$. Les limites se prennent dans $I$.

Comme $f'(x)>0$ sur $I$, $f$ est strictement croissante. Elle est aussi continue et réalise donc une bijection de $I$ sur $\mathbb R$.

La dérivée ne s’annule pas : $\arctan=\tan^{-1}$, notée « atan » dans le PDF, est donc dérivable sur $\mathbb R$ et

$$\arctan'(x)=\frac1{f'(\arctan x)}=\frac1{1+\tan^2(\arctan x)}=\frac1{1+x^2}.$$

## Page 106

## Dérivées de cosinus et sinus

On admet, par démonstration géométrique, que

$$\forall x\in[0,\pi/2[,\quad\sin x\le x\le\frac{\sin x}{\cos x}.$$

Alors $x\cos x\le\sin x$ et… [suite de l’affichage page suivante].

## Page 107

## Dérivées de cosinus et sinus

On admet, par démonstration géométrique, que

$$\forall x\in[0,\pi/2[,\quad\sin x\le x\le\frac{\sin x}{\cos x}.$$

Alors $x\cos x\le\sin x\le x$. Pour $x>0$, il vient $\cos x\le\sin x/x\le1$. Comme $\lim_{x\to0}\cos x=1$, le théorème des gendarmes donne $\lim_{x\to0^+}\sin x/x=1$.

La fonction $x\mapsto\sin x/x$ étant paire, la limite à gauche est la même :

$$\lim_{x\to0}\frac{\sin x}x=1.$$

## Page 108

## Dérivée de cosinus en $0$

$$\frac{\cos x-1}x=\frac{-2\sin^2(x/2)}{2(x/2)}=-\frac{\sin^2(x/2)}{x/2}\longrightarrow0.$$

On utilise la composition avec $x/2\to0$ et $\sin t/t\to1$.

**Erreur de la source :** la diapositive affiche une limite $-1$ ; la limite vaut $0$, valeur effectivement utilisée dans la suite du calcul.

## Dérivée de cosinus en un réel $a$

$$\begin{aligned}\frac{\cos(a+h)-\cos a}h
&=\frac{\cos a\cos h-\sin a\sin h-\cos a}h\\
&=\cos a\frac{\cos h-1}h-\sin a\frac{\sin h}h.
\end{aligned}$$

Donc

$$\lim_{h\to0}\frac{\cos(a+h)-\cos a}h=\cos a\times0-\sin a\times1=-\sin a.$$

**Notes de transcription :** le sous-titre imprimé dit « dérivée de sin » mais les formules portent sur cosinus. La limite finale indique $x\to0$ au lieu de $h\to0$.

## Page 109

## Dérivée de sinus en un réel $a$

$$\begin{aligned}\frac{\sin(a+h)-\sin a}h
&=\frac{\sin a\cos h+\cos a\sin h-\sin a}h\\
&=\sin a\frac{\cos h-1}h+\cos a\frac{\sin h}h.
\end{aligned}$$

Donc

$$\lim_{h\to0}\frac{\sin(a+h)-\sin a}h=\sin a\times0+\cos a\times1=\cos a.$$

**Théorème.** On a bien montré que la dérivée de sinus est cosinus, et que la dérivée de cosinus est $-\sin$.

**Notes de transcription :** le titre du PDF annonce « dérivée de cos » alors que le calcul porte sur sinus. La variable de la limite est encore imprimée $x$ au lieu de $h$.
