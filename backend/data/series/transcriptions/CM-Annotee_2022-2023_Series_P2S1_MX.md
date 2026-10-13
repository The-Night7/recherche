---
source: "PREING2-S1/Series/CM-Annotee_2022-2023_Series_P2S1_MX.pdf"
pages: 42
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des 42 pages manuscrites ; formules, démonstrations, schémas et erreurs de la source explicités
---

# Séries — cours annoté 2022–2023

## Page 1

Série — CM 2022–2023.

Notes manuscrites. Les abréviations « CV », « DV », « SSI » et « tq » sont développées en « converge », « diverge », « si et seulement si » et « tel que ». Les erreurs des notes sont conservées ou corrigées avec une mention explicite.

## Page 2

## Série à terme quelconque

**Théorème.** Une série $\sum u_n$ est convergente si et seulement si la suite des sommes partielles est une suite de Cauchy, c’est-à-dire

$$\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall p\ge N,\ \forall q\ge N,\ |S_p-S_q|<\varepsilon,$$

avec $S_p=\sum_{k=0}^p u_k$ et $S_q=\sum_{k=0}^q u_k$.

Ce qui peut s’écrire :

$$\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall q\ge p\ge N,\ \left|\sum_{k=p+1}^q u_k\right|<\varepsilon.$$

**Note de transcription :** la seconde ligne du manuscrit indique seulement $p\ge N$, $q\ge N$ ; l’ordre $q\ge p$ est explicité pour la somme écrite.

**Corollaire.** Soit $\sum u_n$ une série numérique. S’il existe deux suites $(p_n)_n$ et $(q_n)_n$ telles que :

1. pour tout $n\in\mathbb N$, $p_n\le q_n$ ;
2. $\lim p_n=\lim q_n=+\infty$ ;
3. la suite $\left(\sum_{k=p_n}^{q_n}u_k\right)_n$ ne converge pas vers $0$ ;

alors $\sum_{n\in\mathbb N}u_n$ diverge.

## Page 3

## Exemple — technique à appliquer dans tous les exercices

$p_n=n+1$, $q_n=2n$. On a $\lim p_n=\lim q_n=+\infty$ et $n+1\le2n$ (pour $n\ge1$).

Pour montrer que $\left(\sum_{k=n+1}^{2n}u_k\right)_n$ ne tend pas vers $0$ : « idée : trouver un minorant strictement supérieur à $0$ ».

Encadrer $h(n)\le u_k\le g(n)$ : « il faut encadrer — théorème des gendarmes ».

$$\sum_{k=n+1}^{2n}h(n)\le\sum_{k=n+1}^{2n}u_k
\quad\Longrightarrow\quad nh(n)\le\sum_{k=n+1}^{2n}u_k.$$

La page ne donne pas de terme général particulier. Pour conclure par cette minoration, le minorant doit rester à distance de zéro quand $n\to\infty$.

## Page 4

## Séries alternées — règle d’Abel

Soient $(a_n)_n$ et $(b_n)_n$ deux suites numériques telles que :

- $(a_n)_n$ est à termes positifs, décroissante et tend vers $0$ ;
- la suite $\left(\sum_{k=0}^n b_k\right)_n$ est bornée.

Alors $\sum_{n\in\mathbb N}a_nb_n$ converge.

**Exemple.** Étudier la convergence de $\sum_{n\ge1}\cos(n)/n$ et de $\sum_{n\ge1}\cos(n)/n^2$.

Annotation : « mettre à termes positifs ».

$$0\le\left|\frac{\cos n}{n^2}\right|\le\frac1{n^2}.$$

La série $\sum1/n^2$ converge : Riemann, $\alpha=2>1$.

## Page 5

Par le théorème de majoration des séries à termes positifs, $\sum_{n\ge1}|\cos(n)/n^2|$ converge. Cela signifie que $\sum_{n\ge1}\cos(n)/n^2$ converge absolument, donc converge.

**Note de transcription :** les notes dessinent une double flèche entre convergence absolue et convergence ; seule l’implication de la première vers la seconde est valable en général.

On applique la règle d’Abel à $\sum_{n\ge1}\cos(n)/n$ :

$$a_n=\frac1n\quad(n\ge1),\qquad b_n=\cos n.$$

La suite $(1/n)_n$ est décroissante et tend vers $0$. Il reste à borner $\left|\sum_{k=0}^n\cos k\right|$ (point d’interrogation dans les notes).

## Page 6

$$\cos n=\operatorname{Re}(e^{in}),$$

$$\sum_{k=0}^n\cos k=\operatorname{Re}\left(\sum_{k=0}^n e^{ik}\right)
=\operatorname{Re}\left(\sum_{k=0}^n(e^i)^k\right)
=\operatorname{Re}\left(\frac{1-e^{i(n+1)}}{1-e^i}\right).$$

$$\left|\frac{1-e^{i(n+1)}}{1-e^i}\right|
\le\frac{1+|e^{i(n+1)}|}{|1-e^i|}=\frac{1+1}{|1-e^i|}.$$

Calcul du dénominateur, par factorisation de $e^{ia}-e^{ib}$ :

$$e^{ia}-e^{ib}=e^{i(a+b)/2}\left(e^{i(a-b)/2}-e^{-i(a-b)/2}\right)
=2i\sin\left(\frac{a-b}2\right)e^{i(a+b)/2}.$$

Rappel entouré : $e^{i\alpha}-e^{-i\alpha}=2i\sin\alpha$.

Avec $a=0$, $b=1$, on obtient $|1-e^i|=|2i\sin(-1/2)e^{i/2}|=2\sin(1/2)$. Donc le majorant est $2/[2\sin(1/2)]=1/\sin(1/2)$ : la suite est bornée.

**Note de transcription :** le manuscrit passe de $1-e^i$ à son module au milieu du calcul sans modifier le membre de gauche ; la distinction est explicitée ici.

## Page 7

D’où

$$\left|\frac{1-e^{i(n+1)}}{1-e^i}\right|\le\frac2{2\sin(1/2)}=\frac1{\sin(1/2)},$$

$$\left|\sum_{k=0}^n\cos k\right|=\left|\operatorname{Re}\left(\sum_{k=0}^n e^{ik}\right)\right|\le\frac1{\sin(1/2)}.$$

La suite $\left(\sum_{k=0}^n b_k\right)_n$ est bornée. Par la règle d’Abel, $\sum_{n\ge1}\cos(n)/n$ converge.

**Définition.** Une série numérique réelle $\sum_{n\in\mathbb N}u_n$ est dite alternée si et seulement si

$$\forall n\in\mathbb N,\ u_n=(-1)^n|u_n|,$$

ou $\forall n\in\mathbb N,\ u_n=-(-1)^n|u_n|$.

## Page 8

## Remarques

1. Les notes écrivent : « $\sum u_n$ est une série alternée si et seulement si $u_nu_{n+1}\le0$ ».
2. Elles écrivent aussi : « $u_n=(-1)^na_n$, avec $(a_n)_n$ une suite à termes constants ».

**Notes de transcription :** dans 2, lire « de signe constant », comme le confirme la page 10. Dans 1, l’équivalence avec la définition de la page 7 suppose de traiter les termes nuls : la seule condition $u_nu_{n+1}\le0$ ne fixe pas la parité du signe lorsqu’il y a des zéros intercalés.

**Exemples :**

1. $\sum (-1)^n/n$.
2. $\sum\cos(n\pi)/(n\sqrt n)$, avec $\cos(n\pi)=(-1)^n$ entouré.
3. $\sum\sin(n\pi/2)/\ln n$.

$$\sin\left(\frac{n\pi}2\right)=\begin{cases}0&\text{si }n=2k,\\(-1)^k&\text{si }n=2k+1.\end{cases}$$

Le PDF indique $n\in\mathbb N$ sous les trois sommes ; les dénominateurs imposent $n\ge1$ pour 1 et 2, $n\ge2$ pour 3. Le troisième exemple alterne après suppression des termes nuls, et ne satisfait pas directement la définition par parité de la page 7.

## Page 9

## Théorème spécial des séries alternées (« TSCSA »)

Soit $\sum u_n$ une série alternée telle que $(|u_n|)_n$ soit décroissante et tende vers $0$. Alors $\sum u_n$ converge. De plus, pour tout $n\ge n_0$, le reste $R_n$ est du signe de $u_{n+1}$ et

$$|R_n|=\left|\sum_{k=n+1}^{+\infty}u_k\right|\le|u_{n+1}|.$$

## Exercice — énoncé manuscrit

On considère $(u_n)_n$ et $(v_n)_n$ définies, pour tout $n\in\mathbb N^*$, par les deux lignes suivantes présentes dans les notes :

$$u_n=\frac12\frac{(-1)^{n+1}}n,\qquad v_n=\ln\left(\cos\left(\frac{(-1)^{n/2}}{\sqrt n}\right)\right),$$

puis

$$u_n=\frac{(-1)^{n+1}}n,\qquad v_n=\ln\left(1+\sin\left(\frac{(-1)^n}{\sqrt n}\right)\right).$$

1. Montrer que $u_n\sim v_n$.
2. Étudier la convergence de $\sum u_n$ et $\sum v_n$.
3. Que peut-on conclure ?

**Incohérence de la source :** ces deux lignes ne définissent pas les mêmes suites ; $(-1)^{n/2}$ n’est pas réel pour tout entier $n$. La correction suivante utilise en réalité $u_n=(-1)^n/\sqrt n$ et le second $v_n$. Les expressions d’origine sont conservées ci-dessus.

## Page 10

## Correction telle que développée dans les notes

**1.**

$$\ln\left(1+\sin\frac{(-1)^n}{\sqrt n}\right)
\underset{+\infty}\sim\sin\frac{(-1)^n}{\sqrt n}
\underset{+\infty}\sim\frac{(-1)^n}{\sqrt n}.$$

Les annotations entourent d’abord $X=\sin((-1)^n/\sqrt n)\to0$, puis $Y=(-1)^n/\sqrt n\to0$.

**2.** $u_n=(-1)^n/\sqrt n=(-1)^na_n$, avec $a_n=1/\sqrt n$ de signe constant : $\sum u_n$ est alternée. La suite $(1/\sqrt n)$ est décroissante ; d’après le TSCSA, $\sum_{n\ge1}u_n$ converge (sa limite nulle est également nécessaire).

**Attention, en rouge :** $u_n\sim v_n$, mais les suites ne sont pas de signe constant. On ne peut pas appliquer le théorème des équivalents des séries à termes de signe constant.

## Page 11

On pose $v_n=\ln(1+\sin((-1)^n/\sqrt n))$.

$$v_n=\ln\left(1+\frac{(-1)^n}{\sqrt n}-\frac16\frac{(-1)^n}{n^{3/2}}+o\left(\frac{(-1)^n}{n^{3/2}}\right)\right).$$

La page contient ensuite l’essai de calcul suivant :

$$\ln(1+X)=X-\frac{X^3}3+o(X^3),$$

puis $\sin((-1)^n/\sqrt n)-\frac13(\sin((-1)^n/\sqrt n))^3+o((\sin((-1)^n/\sqrt n))^3)$.

**Erreur de la source :** ce développement de $\ln(1+X)$ est faux. La page 12 reprend le calcul avec $X-X^2/2+X^3/3+o(X^3)$.

**Attention, en rouge :** si $(u_n)$ et $(v_n)$ ne gardent pas un signe constant, $u_n=o(v_n)$ et la convergence de $\sum v_n$ n’impliquent pas la convergence de $\sum u_n$ (flèche barrée dans les notes).

## Page 12

Avertissement en rouge : pour une série de termes $o(v_n)$, utiliser une convergence absolue ; exemple de référence, les séries de Riemann d’exposant $\alpha>1$.

$$v_n=\ln\left(1+\sin\frac{(-1)^n}{\sqrt n}\right)=\ln(1+X)
=X-\frac{X^2}2+\frac{X^3}3+o(X^3),$$

avec

$$X=\sin\frac{(-1)^n}{\sqrt n}
=\frac{(-1)^n}{\sqrt n}-\frac16\frac{(-1)^n}{n^{3/2}}+o\left(\frac{(-1)^n}{n^{3/2}}\right).$$

Ainsi

$$\begin{aligned}v_n&=\frac{(-1)^n}{\sqrt n}-\frac16\frac{(-1)^n}{n^{3/2}}-\frac1{2n}+\frac13\frac{(-1)^n}{n^{3/2}}+o\left(\frac{(-1)^n}{n^{3/2}}\right)\\
&=\underbrace{\frac{(-1)^n}{\sqrt n}}_{a_n}\underbrace{-\frac1{2n}}_{b_n}+\underbrace{\frac16\frac{(-1)^n}{n^{3/2}}}_{c_n}+\underbrace{o\left(\frac{(-1)^n}{n^{3/2}}\right)}_{d_n}.
\end{aligned}$$

## Page 13

$\sum a_n$ converge (série alternée, TSCSA). $\sum b_n$ diverge (Riemann, $\alpha=1$). $\sum c_n$ converge absolument, et aussi par le TSCSA. $\sum d_n$ converge absolument.

Donc $\sum v_n$ diverge.

**Note de transcription :** la conclusion manuscrite écrit $\sum u_n$ ; il faut lire $\sum v_n$, puisque les quatre termes de la page 12 décomposent $v_n$.

**3.** On a deux suites équivalentes $(u_n)_n$ et $(v_n)_n$, mais $\sum u_n$ et $\sum v_n$ n’ont pas la même nature, car ce ne sont pas des séries à termes de signe constant.

## Somme de produits

**Théorème.** Si $\sum_{n\ge0}a_n$ et $\sum_{n\ge0}b_n$ sont absolument convergentes, alors la série $\sum_{n\ge0}c_n$, avec

$$c_n=\sum_{j=0}^n a_jb_{n-j},$$

converge absolument et

$$\sum_{n=0}^{+\infty}c_n=\left(\sum_{n=0}^{+\infty}a_n\right)\left(\sum_{n=0}^{+\infty}b_n\right).$$

Les bornes des sommes imbriquées sont confuses dans la première ligne manuscrite ; la définition de $c_n$ est explicitée ici.

## Page 14

## Chapitre — suites et séries de fonctions

### I. Suites de fonctions — 1. Convergence simple et convergence uniforme

**Définition.** Soit $A\subseteq\mathbb R$ et $f,f_n:A\to\mathbb R$, pour tout $n\in\mathbb N$.

1. La suite de fonctions $(f_n)$ converge simplement vers $f$ sur $A$ si, pour tout $x\in A$, la suite numérique $(f_n(x))_n$ converge vers $f(x)$. Notation : $f_n\xrightarrow[A]{\mathrm{CVS}}f$.
2. La suite $(f_n)_n$ converge simplement sur $A$ s’il existe $f:A\to\mathbb R$ telle que $f_n\to f$ simplement.

Quantification :

$$f_n\xrightarrow[A]{\mathrm{CVS}}f\quad\Longleftrightarrow\quad
\forall\varepsilon>0,\ \forall x\in A,\ \exists n_0=n_0(x)\in\mathbb N,\ \forall n\ge n_0,\ |f_n(x)-f(x)|<\varepsilon.$$

Le rang dépend aussi de $\varepsilon$, laissé implicite dans les notes.

**Exemple 1.** Pour tout $n\in\mathbb N$, $f_n:[0,1]\to\mathbb R$, $x\mapsto x^n-x$.

## Page 15

Étudions la convergence simple de $(f_n)_n$.

- Pour $x=1$, $f_n(1)=1^n-1=0\to0$.
- Pour $x\in[0,1[$, $f_n(x)=x^n-x\to-x$.

Conclusion : $f_n\xrightarrow[[0,1]]{\mathrm{CVS}}f$, où

$$f(x)=\begin{cases}0&x=1,\\-x&x\in[0,1[.\end{cases}$$

L’extrémité de la seconde branche est écrite fermée dans le manuscrit ; elle est rétablie ouverte.

**Exemple 2.** $g_n:\mathbb R_+\to\mathbb R$, $g_n(x)=x^n/(1+x)$.

- Si $x=1$, $g_n(1)=1/2$.
- Si $x\in[0,1[$, $g_n(x)\to0$.
- Si $x>1$, $x^n\to+\infty\notin\mathbb R$.

Conclusion : $(g_n)$ ne converge pas simplement sur $\mathbb R_+$. Sur $[0,1]$, elle converge simplement vers la fonction valant $0$ sur $[0,1[$ et $1/2$ en $1$.

Les notes réemploient $f_n,f$ dans cette conclusion ; les noms $g_n$ sont conservés ici pour éviter la confusion avec l’exemple 1.

## Page 16

## Rappel

$$\|f\|_\infty=\sup_x|f(x)|\in\overline{\mathbb R}_+=\mathbb R_+\cup\{+\infty\}.$$

$$\big|\|f\|_\infty-\|g\|_\infty\big|\le\|f+g\|_\infty\le\|f\|_\infty+\|g\|_\infty.$$

La première inégalité suppose des normes finies pour que leur différence soit définie.

**Définition.** Soit $A\subseteq\mathbb R$ et $f,f_n:A\to\mathbb R$. Posons

$$b_n=\|f_n-f\|_\infty=\sup_{x\in A}|f_n(x)-f(x)|.$$

1. $(f_n)_n$ converge uniformément vers $f$ sur $A$ si $\lim_{n\to\infty}b_n=0$, c’est-à-dire $\lim_{n\to\infty}\|f_n-f\|_\infty=0$. Notation : $f_n\xrightarrow[A]{\mathrm{CVU}}f$.
2. $(f_n)_n$ converge uniformément sur $A$ s’il existe une fonction $f$ définie sur $A$ telle que $f_n\xrightarrow[A]{\mathrm{CVU}}f$.

## Page 17

## Quantification

$$f_n\xrightarrow[A]{\mathrm{CVU}}f\quad\Longleftrightarrow\quad
\forall\varepsilon>0,\ \exists n_0\in\mathbb N,\ \forall x\in A,\ \forall n\ge n_0,\ |f_n(x)-f(x)|<\varepsilon.$$

Remarque : $n_0$ ne dépend pas de $x$.

**Figure :** dans un repère d’abscisse $I$, la courbe de $f_n$ (rouge) reste dans le tube délimité par $f+\varepsilon$ (noir) et $f-\varepsilon$ (bleu), autour de $f$ (vert).

Pour $f,f_n:I\to\mathbb R$, $f_n\xrightarrow[I]{\mathrm{CVU}}f$ veut dire que, pour tout $n\ge n_0$, le graphique de $f_n$ se trouve dans ce tube.

**Proposition.** La convergence uniforme implique la convergence simple :

$$f_n\xrightarrow[A]{\mathrm{CVU}}f\quad\Longrightarrow\quad f_n\xrightarrow[A]{\mathrm{CVS}}f.$$

Attention : la réciproque n’est pas toujours vraie.

## Page 18

## Preuve

On a $\|f_n-f\|_\infty\to0$, c’est-à-dire $\sup_{x\in A}|f_n(x)-f(x)|\to0$. Donc, pour tout $x\in A$, $|f_n(x)-f(x)|\to0$, car

$$0\le|f_n(x)-f(x)|\le\sup_{t\in A}|f_n(t)-f(t)|.$$

Encadré rouge : « Étudier le sup, c’est étudier la convergence uniforme ».

Remarque manuscrite inachevée : « si $(f_n)_n$ ne converge pas simplement alors $(f_n)_n$… » [la conclusion attendue est : ne converge pas uniformément].

**Exemple.** $f_n:[0,1]\to\mathbb R$, $f_n(x)=x^n$. Si $|x|<1$, $x^n\to0$, donc

$$f_n\xrightarrow[[0,1]]{\mathrm{CVS}}f,\qquad f(x)=\begin{cases}0&x\in[0,1[,\\1&x=1.\end{cases}$$

Étudions la convergence uniforme vers $f$ sur $[0,1]$. Posons $h_n=f_n-f$ :

$$h_n(x)=\begin{cases}x^n-0=x^n&x\in[0,1[,\\1-1=0&x=1.\end{cases}$$

## Page 19

## Méthode 1

Choisissons $x_n=1-1/n$ (noté $x_0$ dans les notes, bien qu’il dépende de $n$).

$$(f_n-f)(x_n)=x_n^n=\left(1-\frac1n\right)^n=e^{n\ln(1-1/n)}\longrightarrow e^{-1}\ne0.$$

Puisque $\|f_n-f\|_\infty\ge|f_n(x_n)-f(x_n)|$, on a $\liminf\|f_n-f\|_\infty\ge e^{-1}$. Donc $\|f_n-f\|_\infty$ ne tend pas vers $0$ et la convergence n’est pas uniforme.

**Notes de transcription :** le manuscrit écrit une limite au lieu d’une limite inférieure avant d’en établir l’existence. L’annotation rouge dit que le problème se situe près de $1$, d’où le choix $1-1/n$. Le point $1$ appartient bien au domaine, mais la formule $h_n(x)=x^n$ ne vaut que pour $x<1$.

## Méthode 2

Pour $x\in[0,1[$, $h_n(x)=x^n$ et $h_n'(x)=nx^{n-1}\ge0$.

**Tableau de variations :** $h_n$ croît de $0$ vers $1$ lorsque $x$ va de $0$ à $1$ par valeurs inférieures. Ainsi $\|h_n\|_\infty=1\not\to0$ : pas de convergence uniforme sur $[0,1]$.

## Page 20

Comme $h_n(1)=0$, $\sup_{x\in[0,1[}|h_n(x)|=\sup_{x\in[0,1]}|h_n(x)|$.

Montrer que $(f_n)$ converge uniformément vers $f$ sur $[0,a]$ pour tout $a\in[0,1[$ :

$$\sup_{x\in[0,a]}|f_n(x)-f(x)|=\sup_{x\in[0,a]}|h_n(x)|=h_n(a)=a^n\to0.$$

D’où $f_n\xrightarrow[[0,a]]{\mathrm{CVU}}f$.

**Définition.** Si $(f_n)$ converge uniformément sur tout $[0,a]$, pour $a\in[0,1[$ (respectivement $a\in[0,+\infty[$), on dit qu’elle converge localement uniformément sur $[0,1[$ (respectivement $[0,+\infty[$).

**Théorème — critère de Cauchy pour la convergence uniforme.** Une suite $(f_n)_n$ de fonctions de $A$ dans $\mathbb R$ converge uniformément sur $A$ si et seulement si

$$\forall\varepsilon>0,\ \exists n_0\in\mathbb N,\ \forall x\in A,\ \forall n,m\ge n_0,\ |f_n(x)-f_m(x)|<\varepsilon.$$

Notation : $\|f_n-f_m\|_\infty\to0$ lorsque $n,m\to+\infty$. Le manuscrit n’indique que $n\to+\infty$ sous cette dernière flèche ; les deux indices doivent tendre vers l’infini.

## Page 21

## Étude de la convergence uniforme de $(f_n)$ sur $I$

**1. Étudier la convergence simple sur $I$.**

- Si $(f_n)$ ne converge pas simplement, alors elle ne converge pas uniformément.
- S’il existe $f:I\to\mathbb R$ telle que $f_n\xrightarrow[I]{\mathrm{CVS}}f$, poursuivre l’étude.

**Pour montrer la non-convergence uniforme vers $f$**, le schéma propose trois voies :

- choisir une suite de points $x_n\in I$ telle que $|f_n(x_n)-f(x_n)|$ ne tende pas vers $0$ (notée $x_0$ dans les notes, avec « choisir une suite ») ;
- si chaque $f_n$ est continue sur $I$ et si $f$ ne l’est pas, conclure à l’absence de convergence uniforme ;
- étudier $h_n=|f_n-f|$ et chercher $\sup_{x\in I}|h_n(x)|$.

**Pour montrer la convergence uniforme**, étudier $h_n=|f_n-f|$ et montrer que $\sup_{x\in I}|h_n(x)|\to0$.

Les flèches de non-convergence du manuscrit sont retranscrites en toutes lettres.

## Page 22

## Proposition

Soient $f_n,g_n:I\to\mathbb R$. Si $(f_n)$ et $(g_n)$ convergent uniformément sur $I$, alors $(f_n+g_n)$ converge uniformément sur $I$.

**Preuve.** Soient $f$ et $g$ leurs limites respectives. On veut montrer $\|(f_n+g_n)-(f+g)\|_\infty\to0$. Or

$$\|f_n+g_n-f-g\|_\infty\le\|f_n-f\|_\infty+\|g_n-g\|_\infty\to0+0.$$

D’où le résultat.

**Exemple.** $f_n(x)=x+1/n$, $x\in\mathbb R$, $n\in\mathbb N^*$. Étudions la convergence uniforme de $(f_n)$, puis de $(f_n^2)=(f_n\times f_n)$, puis de $(f_n/n)$.

Convergence simple : pour $x\in\mathbb R$ fixé, $\lim f_n(x)=x$. Donc $f_n\xrightarrow[\mathbb R]{\mathrm{CVS}}f$, avec $f(x)=x$.

## Page 23

## a. Convergence uniforme de $(f_n)$

$$|f_n(x)-f(x)|=\left|x+\frac1n-x\right|=\frac1n,$$

indépendamment de $x$. Donc $\sup_{x\in\mathbb R}|f_n(x)-f(x)|=1/n\to0$ : $f_n\xrightarrow[\mathbb R]{\mathrm{CVU}}f$.

## b. Étude de $(f_n^2)$ sur $\mathbb R$

Pour tout $x\in\mathbb R$,

$$f_n^2(x)=\left(x+\frac1n\right)^2=x^2+\frac{2x}n+\frac1{n^2}\longrightarrow x^2.$$

Ainsi $f_n^2\xrightarrow[\mathbb R]{\mathrm{CVS}}f^2$, où $f^2(x)=x^2=(f(x))^2$.

Pour la convergence uniforme :

$$|f_n^2(x)-f^2(x)|=\left|x^2+\frac{2x}n+\frac1{n^2}-x^2\right|=\left|\frac{2x}n+\frac1{n^2}\right|.$$

## Page 24

Pour $x_n=n$ (noté $x_0$ dans les notes),

$$|f_n^2(x_n)-f^2(x_n)|=\left|2+\frac1{n^2}\right|\longrightarrow2\ne0.$$

Donc $\|f_n^2-f^2\|_\infty$ ne tend pas vers $0$ : $(f_n^2)$ ne converge pas uniformément vers $f^2$ sur $\mathbb R$.

## c. Étude de $g_n=f_n/n$

Convergence simple sur $\mathbb R$ : pour $x\in\mathbb R$,

$$g_n(x)=\frac1n\left(x+\frac1n\right)=\frac xn+\frac1{n^2}.$$

- Pour $x=0$, $g_n(0)=1/n^2\to0$.
- Pour $x\ne0$, $g_n(x)\sim x/n$, donc $\lim g_n(x)=0$.

Ainsi $g_n\xrightarrow[\mathbb R]{\mathrm{CVS}}g=0$.

**Note de transcription :** le manuscrit écrit $g_n(0)=0$ ; la valeur exacte est $1/n^2$, sans changement de limite.

## Page 25

## Convergence uniforme de $(g_n)$ sur $\mathbb R$

Avec $g_n(x)=x/n+1/n^2$ et $g=0$, $|g_n(x)-g(x)|=|x/n+1/n^2|$. Pour $x_n=n$, $|g_n(x_n)-g(x_n)|=1+1/n^2\to1\ne0$. Donc $(g_n)=(f_n/n)$ ne converge pas uniformément vers $0$ sur $\mathbb R$.

**Note de transcription :** cette page remplace par erreur $1/n^2$ par $1/n$ et note « $x_0=x$ » au lieu du choix dépendant de $n$ utilisé dans le calcul ; les expressions cohérentes avec la page 24 sont rétablies.

Remarque : $g_n(x)=f_n(x)h_n(x)$ avec $h_n(x)=1/n$. La suite $(h_n)$ converge uniformément vers $h=0$ sur $\mathbb R$.

On a $f_n\xrightarrow[\mathbb R]{\mathrm{CVU}}f$, mais $f_n\times f_n$ ne converge pas uniformément vers $f\times f$. De même, les convergences uniformes de $(f_n)$ et $(h_n)$ impliquent seulement, sans hypothèses supplémentaires, la convergence simple de $(h_nf_n)$ vers $hf$, pas sa convergence uniforme.

## Page 26

## Proposition — continuité

Soit $I\subseteq\mathbb R$, $a\in I$ et $f_n:I\to\mathbb R$ continue en $a$, pour tout $n$. Supposons $f_n\xrightarrow[I]{\mathrm{CVU}}f$. Alors $f$ est continue en $a$.

**Corollaire.** Une limite uniforme d’une suite de fonctions continues sur $I$ est continue sur $I$.

Remarque : ce résultat est utile pour montrer la non-convergence uniforme lorsque la fonction limite n’est pas continue.

**Proposition.** Soit $(f_n)$ une suite de fonctions continues convergeant uniformément sur $I$ vers $f$. Pour toute suite $(x_n)$ de points de $I$ convergeant vers $x\in I$,

$$\lim_{n\to\infty}f_n(x_n)=f(x).$$

**Début de preuve manuscrite.** Montrer que $|f_n(x_n)-f(x)|\to0$ :

$$|f_n(x_n)-f(x)|=|f_n(x_n)-f_n(x)+f_n(x)-f(x)|.$$

Annotation : « on va utiliser l’inégalité triangulaire ».

## Page 27

## Suite de la preuve manuscrite

$$\begin{aligned}|f_n(x_n)-f(x)|
&\le|f_n(x_n)-f_n(x)|+|f_n(x)-f(x)|\\
&\le|f_n(x_n)-f_n(x)|+\|f_n-f\|_\infty.
\end{aligned}$$

Les notes invoquent $x_n\to x$ et la continuité de $f_n$ pour affirmer $|f_n(x_n)-f_n(x)|\to0$.

**Lacune de la preuve :** la seule continuité de chaque $f_n$ ne suffit pas à cette étape, car $n$ varie. Une justification directe utilise la continuité de $f$, établie par le corollaire précédent :

$$|f_n(x_n)-f(x)|\le\|f_n-f\|_\infty+|f(x_n)-f(x)|\to0.$$

Remarque manuscrite : « la convergence uniforme est une condition nécessaire dans la proposition ». L’exemple montre qu’on ne peut pas simplement supprimer cette hypothèse du théorème, sans affirmer sa nécessité pour chaque suite particulière.

**Exemple.** $f_n(x)=x^n$ sur $[0,1]$. La limite simple $f$ vaut $1$ en $1$, $0$ sur $[0,1[$. La convergence n’est pas uniforme. Prenons $x_n=1-1/n\to1$.

## Page 28

On a $f(1)=1$, mais

$$\lim_{n\to\infty}f_n(x_n)=\lim_{n\to\infty}\left(1-\frac1n\right)^n=e^{-1}.$$

Ainsi $f(1)\ne\lim f_n(x_n)$.

## Interversion des limites

Dans cet exemple sans convergence uniforme,

$$\lim_{x\to1^-}\lim_{n\to\infty}f_n(x)\ne\lim_{n\to\infty}\lim_{x\to1^-}f_n(x).$$

**Théorème.** Soit $I\subseteq\mathbb R$, $a\in\overline I$ et $f_n:I\to\mathbb R$. Supposons que $(f_n)$ converge uniformément sur $I$ vers $f$ et que, pour tout $n$, la limite $\ell_n=\lim_{x\to a}f_n(x)$ existe. Alors

$$\lim_{x\to a}\lim_{n\to\infty}f_n(x)=\lim_{n\to\infty}\lim_{x\to a}f_n(x).$$

Encadré : « Important ». Les limites en $a$ sont prises suivant $I$ ; l’indice intérieur du premier membre, noté par erreur $x\to\infty$ dans les notes, est rétabli en $n\to\infty$.

## Page 29

## Intégrales et convergence uniforme

**Théorème — valable pour un intervalle borné.** Soit $a<b$. Si une suite $(f_n)$ de fonctions intégrables sur $[a,b]$ converge uniformément vers $f$, alors $f$ est intégrable et

$$\lim_{n\to\infty}\int_a^b f_n(x)\,dx=\int_a^b\lim_{n\to\infty}f_n(x)\,dx.$$

Le domaine est noté $[0,a]$ dans la phrase manuscrite, alors que la formule porte sur $[a,b]$ ; cette incohérence est corrigée ci-dessus.

**Point 2 du manuscrit :** il existe des suites de fonctions intégrables $(f_n)$ convergeant simplement vers une fonction « non intégrable », suivies de la formule

$$\lim_{n\to\infty}\int_a^b f_n(x)\,dx\ne\int_a^b\lim_{n\to\infty}f_n(x)\,dx.$$

**Note de transcription :** si la limite n’est pas intégrable, le second membre n’est pas défini dans ce cadre. La convergence simple peut aussi échouer à permettre l’interversion avec une limite intégrable, comme dans l’exemple de la page suivante.

Les emplacements « Preuve : 1/ » et « 2/ » sont laissés vides. Indication manuscrite : « Regarder cours Teams enregistré ».

## Page 30

## 3. Exercice

$$f_n(x)=\begin{cases}
4n^2x&0\le x\le(2n)^{-1}=1/(2n),\\
4n(1-nx)&1/(2n)\le x\le1/n,\\
0&x>n^{-1}=1/n.
\end{cases}$$

Aucune question ni correction n’est ajoutée sur cette page.

**Corollaire :** « Soient $a,b\in\mathbb R$, $a<b$… » [énoncé interrompu ; le reste de la page est vide].

## Page 31

## Théorème — dérivation d’une limite

Soit $I\subseteq\mathbb R$ un intervalle et $f_n\in C^1(I)$. Supposons que :

1. $(f_n)$ converge simplement sur $I$ vers $f$ ;
2. $(f_n')$ converge uniformément sur $I$ vers $g$.

Alors $f\in C^1(I)$ et $f'=g$, c’est-à-dire

$$\left(\lim_{n\to\infty}f_n(x)\right)'=\lim_{n\to\infty}f_n'(x).$$

## Exemple — énoncé du manuscrit

$$f_n(x)=n^2\left(\frac{x^{n+1}}{n+1}-\frac{x^{n+2}}{n+2}\right),\qquad0\le x\le1.$$

1. Étudier la convergence simple et uniforme de $(f_n)$ sur $[0,1]$.
2. Montrer que $(f_n')$ converge uniformément sur $[0,1]$.
3. Montrer que $f=\lim f_n$ est dérivable sur $[0,1]$.

**Erreur de l’énoncé :** avec le coefficient $n^2$ effectivement écrit, la limite simple vaut $0$ sur $[0,1[$ et $1$ en $1$ ; elle n’est pas continue. De plus, $f_n'(x)=n^2x^n(1-x)$ ne converge pas uniformément vers $0$ (en $x=n/(n+1)$, sa valeur est équivalente à $n/e$). Les demandes 2 et 3 sont donc fausses pour cette formule. Aucune correction n’est fournie dans les notes.

## Page 32

## Séries de fonctions

### II. Continuité en un point d’une série uniformément convergente

**1. Continuité — théorème 1.** Soit $\sum f_n$ une série de fonctions uniformément convergente sur $A$. Si chaque $f_n$ est continue en $x_0\in A$ (respectivement sur $A$), alors sa somme $S$ est continue en $x_0$ (respectivement sur $A$).

Preuve : voir le théorème sur les suites de fonctions et considérer les sommes partielles $S_n=f_0+\cdots+f_n$, dont la suite converge uniformément. On a

$$\lim_{x\to x_0}\sum_{n=0}^{+\infty}f_n(x)
=\sum_{n=0}^{+\infty}\lim_{x\to x_0}f_n(x)
=\sum_{n=0}^{+\infty}f_n(x_0).$$

Annotation rouge inachevée : « Intervertir ⇒ continuité uniforme et… ». L’hypothèse du théorème est la convergence uniforme de la série et la continuité de ses termes.

**2. Limite en un point — théorème 2.** Soit $\sum f_n$ uniformément convergente sur $A$. Si $\ell_n=\lim_{x\to x_0}f_n(x)$ existe pour tout $n$, alors $\sum\ell_n$ converge et

$$\lim_{x\to x_0}\sum_{n=0}^{+\infty}f_n(x)
=\sum_{n=0}^{+\infty}\lim_{x\to x_0}f_n(x)
=\sum_{n=0}^{+\infty}\ell_n.$$

Annotation : $\ell$ est indexé par $n$.

### III. Intégration terme à terme d’une série de fonctions

Soit $\sum f_n$ une série de fonctions continues sur $[a,b]$. Si elle converge uniformément sur $[a,b]$, alors $\sum\int_a^b f_n(x)\,dx$ converge et

$$\sum_{n=0}^{+\infty}\int_a^b f_n(x)\,dx=\int_a^b\sum_{n=0}^{+\infty}f_n(x)\,dx.$$

## Page 33

Preuve : voir le théorème d’intégration de la limite uniforme des suites de fonctions.

## Exemple d’application

Soit $\sum f_n$, où $f_n(x)=(-1)^nx^n$.

**Convergence simple.** Pour $x$ fixé, $\sum f_n(x)=\sum(-x)^n$ est géométrique et converge si $|x|<1$, c’est-à-dire $-1<x<1$. La série converge simplement sur $]-1,1[$ vers $S(x)=1/(1+x)$.

**Convergence normale.** On étudie $\sum\|f_n\|_\infty$. Or $\|f_n\|_\infty=\sup_{x\in]-1,1[}|x|^n=1$. Donc la série ne converge pas normalement sur $]-1,1[$.

**Convergence uniforme.** La série converge uniformément sur $A$ si et seulement si $\sup_{x\in A}|R_n(x)|\to0$.

Annotation : « série alternée, c’est bien pour [la] convergence uniforme car on peut majorer ».

$$\begin{aligned}R_n(x)&=\sum_{k=1}^{+\infty}f_{n+k}(x)
=\sum_{k=1}^{+\infty}(-1)^{n+k}x^{n+k}\\
&=(-x)^n\sum_{k=1}^{+\infty}(-x)^k
=(-x)^n\frac{-x}{1+x}=\frac{(-x)^{n+1}}{1+x}.
\end{aligned}$$

Pour $x\in]-1,1[$,

$$\sup_{x\in]-1,1[}|R_n(x)|=\sup_{x\in]-1,1[}\frac{|x|^{n+1}}{1+x}=+\infty.$$

Donc $\sum f_n$ ne converge pas uniformément sur $]-1,1[$. Soit maintenant $[a,b]\subset]-1,1[$.

## Page 34

Pour $x\in[a,b]$,

$$\frac{|x|^{n+1}}{1+x}\le\frac{|x|^{n+1}}{1+a}
\le\frac{\max(|a|^{n+1},|b|^{n+1})}{1+a}\longrightarrow0.$$

Donc $\sum f_n$ converge uniformément sur tout segment $[a,b]\subset]-1,1[$.

Appliquons le théorème d’intégration terme à terme. Choisissons $[a,b]=[0,t]$, avec $0<t<1$ :

$$\begin{aligned}\sum_{n=0}^{+\infty}\int_0^t f_n(x)\,dx
&=\int_0^t\sum_{n=0}^{+\infty}f_n(x)\,dx\\
&=\int_0^t\frac1{1+x}\,dx=[\ln(1+x)]_0^t=\ln(1+t).
\end{aligned}$$

D’autre part,

$$\sum_{n=0}^{+\infty}\int_0^t(-1)^nx^n\,dx
=\sum_{n=0}^{+\infty}(-1)^n\left[\frac{x^{n+1}}{n+1}\right]_0^t
=\sum_{n=0}^{+\infty}\frac{(-1)^nt^{n+1}}{n+1}.$$

Ainsi

$$\sum_{n=1}^{+\infty}\frac{(-1)^{n-1}t^n}{n}=\ln(1+t)\qquad(t\in]0,1[).$$

On peut aussi obtenir cette formule pour $t\in]-1,1[$.

**Note de transcription :** une ligne intermédiaire des notes omet l’exposant $n+1$ de $t$, puis le rétablit à la ligne suivante.

## Page 35

## IV. Dérivation terme à terme

Soit $\sum f_n$ une série de fonctions de classe $C^1$ sur un intervalle $I\subseteq\mathbb R$. Si :

1. il existe au moins un $x_0\in I$ tel que $\sum f_n(x_0)$ converge vers une constante réelle $\ell$ ;
2. la série des dérivées $\sum f_n'$ converge uniformément sur tout intervalle fermé borné $[a,b]\subset I$ vers une fonction $G$ ;

alors :

- $\sum f_n$ converge uniformément sur tout $[a,b]\subset I$ vers $S(x)=\ell+\int_{x_0}^xG(t)\,dt$ ;
- $S=\sum_{n=0}^{+\infty}f_n$ est de classe $C^1$ sur $I$ et

$$S'(x)=\left(\sum_{n=0}^{+\infty}f_n(x)\right)'=\sum_{n=0}^{+\infty}f_n'(x).$$

**Note de transcription :** l’hypothèse 2 du manuscrit écrit $\sum f_n$ sans prime ; la série visée est celle des dérivées, conformément au titre et à la conclusion.

## Page 36

## Série entière — I. Définition

Une série entière complexe (respectivement réelle) est une série de fonctions $\sum f_n$ pour laquelle il existe une suite complexe (respectivement réelle) $(a_n)_{n\in\mathbb N}$ telle que $f_n:\mathbb C\to\mathbb C$, $z\mapsto a_nz^n$ (respectivement $f_n:\mathbb R\to\mathbb R$, $x\mapsto a_nx^n$).

Une telle série est notée $\sum a_nz^n$ (respectivement $\sum a_nx^n$).

### II. Rayon et domaine de convergence

Pour une série entière complexe ou réelle, l’ensemble

$$I=\left\{r\in\mathbb R_+:\sum|a_n|r^n\text{ converge}\right\}$$

est un intervalle de $\mathbb R_+$ contenant $0$. Sa borne supérieure est appelée rayon de convergence de $\sum a_nz^n$.

**Définition du domaine de convergence, dans les notes.** Pour un rayon $r$ :

- dans le cas complexe, $D_r=\{z\in\mathbb C:|z|<r\}$ ;
- dans le cas réel, $D_r=]-r,r[$.

**Précision de transcription :** il s’agit ici du disque ou de l’intervalle ouvert de convergence ; des points de la frontière peuvent aussi appartenir à l’ensemble complet de convergence. Le rayon peut valoir $+\infty$. Pour un rayon nul, la série reste définie en $0$.

**Exemple.** Considérons $a_n=n^n$, donc la série entière $\sum n^nz^n$. Pour chercher le rayon, on cherche l’ensemble… [suite page suivante].

## Page 37

## 1. Suite de l’exemple $a_n=n^n$

On étudie la série numérique positive $\sum n^nr^n$ et les valeurs de $r$ pour lesquelles elle converge.

$$\sqrt[n]{n^nr^n}=nr\longrightarrow\begin{cases}+\infty&r>0,\\0&r=0.\end{cases}$$

Donc $I=\{0\}$ et le rayon de convergence vaut $0$. Les notes écrivent $D_r=\varnothing$ pour le disque ouvert de rayon nul ; l’ensemble réel de convergence de la série est cependant $\{0\}$.

## 2. Exemple $a_n=1/n!$

On étudie $\sum|a_n|r^n=\sum r^n/n!$, série à termes positifs. Pour $r>0$, par d’Alembert,

$$\frac{r^{n+1}}{(n+1)!}\frac{n!}{r^n}=\frac r{n+1}\to0.$$

Donc $I=[0,+\infty[$ et le rayon vaut $+\infty$. Le domaine de convergence est $\mathbb C$ dans le cas complexe et $]-\infty,+\infty[=\mathbb R$ dans le cas réel.

## Page 38

Une série entière s’écrit $\sum a_nx^n$ ou $\sum a_nz^n$. On a défini

$$I=\left\{r\in\mathbb R_+:\sum|a_n|r^n\text{ converge}\right\}.$$

La borne supérieure de $I$ est le rayon de convergence $R\in\mathbb R_+\cup\{+\infty\}$ : $0$ et $+\infty$ sont possibles.

- Pour une série entière réelle, l’intervalle ouvert de convergence est $]-R,R[$.
- Pour une série entière complexe, le disque ouvert de convergence est $D=\{z\in\mathbb C:|z|<R\}$, boule ouverte de centre $0$ et de rayon $R$.

**Figure :** disque hachuré centré à l’origine dans le plan complexe, avec un rayon indiqué.

**Exemple 1.** $a_n=1$, donc $\sum z^n$. Cherchons $r\in\mathbb R_+$ tel que $\sum r^n$ converge. C’est une série géométrique convergente pour $|r|<1$, donc, puisque $r\ge0$, $r\in[0,1[$. Ainsi $I=[0,1[$.

## Page 39

Le rayon de convergence de $\sum z^n$ vaut $R=1$.

- Dans le cas réel, l’intervalle de convergence est $]-1,1[$.
- Dans le cas complexe, le domaine est la boule ouverte unité.

## Lemme d’Abel

Soit $\sum a_nz^n$ une série entière complexe. S’il existe $z_0\in\mathbb C\setminus\{0\}$ tel que $(a_nz_0^n)_n$ soit bornée, alors, pour tout $z\in\mathbb C$ tel que $|z|<|z_0|$, $\sum a_nz^n$ converge absolument. De plus, elle converge normalement sur tout disque fermé de centre $0$ et de rayon $r<|z_0|$.

**Remarque.** À toute série entière complexe est associé un unique $\alpha\in\overline{\mathbb R}_+$ tel que :

- pour $|z|<\alpha$, la série converge absolument ;
- pour $|z|>\alpha$, la série diverge.

Le réel étendu $\alpha$, aussi noté $R$, est le rayon de convergence.

**Note de transcription :** les notes emploient « absolument divergente » à l’extérieur ; la conclusion usuelle est la divergence, le terme général ne tendant pas vers zéro.

**Figures :** un disque de rayon $\alpha$ : convergence absolue à l’intérieur, convergence normale sur les disques fermés de rayon strictement inférieur, divergence à l’extérieur. La frontière rouge est nommée « cercle d’incertitude » : « si on est à la frontière, ça dépend (convergence ou divergence) ». Sur l’axe réel, l’intervalle $]-\alpha,\alpha[$ est marqué convergent absolument, les deux régions extérieures divergentes.

## Page 40

## Détermination pratique du rayon — règles de Cauchy ou de d’Alembert

**Théorème.** Soit $\sum a_nz^n$ une série entière complexe. Si $\lim\sqrt[n]{|a_n|}=\ell\in\overline{\mathbb R}_+$, ou bien si $\lim|a_{n+1}/a_n|=\ell\in\overline{\mathbb R}_+$, alors le rayon vaut $R=1/\ell$.

Le quotient suppose $a_n\ne0$ à partir d’un certain rang ; on adopte $1/0=+\infty$ et $1/(+\infty)=0$.

**Exemples.** Déterminer le rayon pour :

1. $a_n=((n-1)/n)^{n^2}$ ;
2. $a_n=n!/(2^{2n}\sqrt{(2n)!})$.

**1.**

$$\begin{aligned}\sqrt[n]{|a_n|}&=\left[\left(\frac{n-1}n\right)^{n^2}\right]^{1/n}
=\left(1-\frac1n\right)^n\\
&=e^{n\ln(1-1/n)}=e^{n(-1/n+o(1/n))}=e^{-1+o(1)}\to e^{-1}.
\end{aligned}$$

Donc $R=1/e^{-1}=e$. Annotation : « $1^\infty$ : forme indéterminée ».

**2.**

$$\begin{aligned}\left|\frac{a_{n+1}}{a_n}\right|
&=\frac{(n+1)!}{2^{2n+2}\sqrt{(2n+2)!}}\frac{2^{2n}\sqrt{(2n)!}}{n!}\\
&=\frac{n+1}{4}\sqrt{\frac{(2n)!}{(2n+2)!}}
=\frac{n+1}{4\sqrt{(2n+2)(2n+1)}}\\
&\sim\frac n{4\sqrt{2n\cdot2n}}=\frac n{4\sqrt{4n^2}}=\frac18.
\end{aligned}$$

Donc $R=8$.

**Note de transcription :** le premier dénominateur du quotient manuscrit porte $2^{n+2}$ ; il est rétabli en $2^{2n+2}$, conforme à $a_n$ et aux lignes suivantes.

## Page 41

## Utilisation d’un équivalent

**Théorème.** Soient $\sum a_nz^n$ et $\sum b_nz^n$ de rayons respectifs $R_a,R_b$. Si $|a_n|\sim|b_n|$, alors $R_a=R_b$.

**Exemple.** $a_n=(1+1/n)^n-e$.

$$\begin{aligned}a_n
&=e^{n\ln(1+1/n)}-e\\
&=e^{n(1/n-1/(2n^2)+o(1/n^2))}-e\\
&=e^{1-1/(2n)+o(1/n)}-e\\
&=e\,e^{-1/(2n)+o(1/n)}-e\\
&=e\left[1-\frac1{2n}+o\left(\frac1n\right)\right]-e\\
&=-\frac e{2n}+o\left(\frac1n\right).
\end{aligned}$$

Ainsi $a_n\sim-e/(2n)=b_n$. On cherche le rayon de $\sum b_nz^n$ :

$$\left|\frac{b_{n+1}}{b_n}\right|=\frac n{n+1}\to1.$$

Donc $R_b=1$, puis $R_a=1$.

**Remarque.** Si $|a_n|\le|b_n|$, alors $R_a\ge R_b$.

**Preuve.** Pour $z\in\mathbb C$ tel que $|z|<R_b$, $\sum b_nz^n$ converge absolument. Par comparaison, $\sum a_nz^n$ converge absolument. On en déduit $R_a\ge R_b$.

**Note de transcription :** les notes concluent intermédiairement $|z|<R_a$ à partir d’une convergence absolue ponctuelle ; on peut seulement conclure $|z|\le R_a$ à ce stade, ce qui suffit, pour tout $|z|<R_b$, à la conclusion. Le petit schéma d’axe barre le cas où $R_a<R_b$ en choisissant un $|z|$ entre les deux rayons.

## Page 42

## Exemple — rayon de convergence de $\sum\sin(n)z^n$

On pose $a_n=\sin n$ (le nom $a_n$ est écrit sous le numérateur dans le titre). On a $|a_n|=|\sin n|\le1=b_n$.

Soit $R$ le rayon de $\sum\sin(n)z^n$ et $R'$ celui de $\sum z^n$. On sait que $R'=1$, donc $R\ge1$.

Pour $z=1$, $\sum\sin n$ diverge ; donc $R\le1$. Finalement, $R=1$.

Fin des notes manuscrites.
