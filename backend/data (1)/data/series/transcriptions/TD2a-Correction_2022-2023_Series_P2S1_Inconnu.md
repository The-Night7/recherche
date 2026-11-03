---
source: "PREING2-S1/Series/TD2a-Correction_2022-2023_Series_P2S1_Inconnu.pdf"
pages: 79
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 79 pages manuscrites ; calculs et annotations transcrits, incohérences et lectures incertaines signalées
---

# Séries — TD2A : suites de fonctions — Corrigé manuscrit (2022–2023)

## Page 1

### TD2A — Suites de fonctions

#### Exercice 1 — 1

$f_n:[0,1]\to\mathbb R$, $f_n(x)=x/(1+nx)$.

**Convergence simple.** En $x=0$, $f_n(0)=0\to0$. Pour $x\ne0$, $f_n(x)\sim x/(nx)=1/n\to0$. Ainsi $f_n$ converge simplement sur $[0,1]$ vers $f=0$.

**Convergence uniforme.** $g_n(x)=|f_n(x)-f(x)|=x/(1+nx)$. Pour $x>0$, $1+nx\ge nx$, donc $g_n(x)\le1/n$ ; cette borne vaut aussi en zéro. Elle est indépendante de $x$ et tend vers zéro : $f_n\to0$ uniformément sur $[0,1]$.

## Page 2

#### Exercice 1 — 2

$f_n:\mathbb R\to\mathbb R$, $f_n(x)=nx/(1+n^2x^2)$.

**Convergence simple.** En zéro, $f_n(0)=0$. Pour $x\ne0$, $f_n(x)\sim nx/(n^2x^2)=1/(nx)\to0$. La limite simple sur $\mathbb R$ est $f=0$.

**Convergence uniforme.** Pour $n\ge1$, prendre $x_n=1/n$ :
$$|f_n(x_n)-f(x_n)|=\frac12.$$
Donc $\sup_{x\in\mathbb R}|f_n(x)-f(x)|\ge1/2$ ; cette quantité ne tend pas vers zéro.

## Page 3

**Exercice 1, 2 (suite).** La convergence n’est pas uniforme sur $\mathbb R$.

Étudier maintenant la convergence uniforme sur $[a,+\infty[$, $a>0$. Comme
$$f_n(-x)=\frac{-nx}{1+n^2x^2}=-f_n(x),$$
la fonction est impaire ; l’étude sur $]-\infty,-a]$ en découlera.

Sur $[a,+\infty[$, $f_n$ est positive, donc $|f_n-f|=f_n$. Sa dérivée est
$$f_n'(x)=\frac{n(1+n^2x^2)-nx(2n^2x)}{(1+n^2x^2)^2}=\frac{n(1-n^2x^2)}{(1+n^2x^2)^2}.$$

## Page 4

**Exercice 1, 2 (fin).** La dérivée s’annule en $x=\pm1/n$. Le tableau de variations sur $\mathbb R$ indique : décroissance jusqu’à $-1/n$, croissance entre $-1/n$ et $1/n$, puis décroissance. Les extrema sont $f_n(-1/n)=-1/2$ et $f_n(1/n)=1/2$ ; les limites en $\pm\infty$ sont nulles.

Pour $n$ assez grand, $1/n<a$. Sur $[a,+\infty[$, $f_n$ est alors décroissante, et
$$\sup_{x\ge a}|f_n(x)-f(x)|=f_n(a)=\frac{na}{1+n^2a^2}\sim\frac1{na}\to0.$$
La convergence est uniforme sur $[a,+\infty[$. Par imparité,
$$\sup_{x\le-a}|f_n(x)-f(x)|=|f_n(-a)|=\frac{na}{1+n^2a^2}\to0.$$
Elle est aussi uniforme sur $]-\infty,-a]$.

## Page 5

#### Exercice 1 — 3

$f_n:\mathbb R_+\to\mathbb R$, $f_n(x)=(x^n-1)/(x^n+1)$.

**Convergence simple.**

- Si $0\le x<1$, $x^n\to0$, donc $f_n(x)\to-1$.
- Si $x=1$, $f_n(1)=0$.
- Si $x>1$, $x^n\to+\infty$ et $f_n(x)\sim x^n/x^n=1$.

La limite simple est
$$f(x)=\begin{cases}-1&0\le x<1,\\0&x=1,\\1&x>1.\end{cases}$$
Les annotations commencent le rappel : une limite uniforme de fonctions continues est continue.

## Page 6

**Exercice 1, 3 (fin).** Les $f_n$ sont continues sur $\mathbb R_+$, mais la limite simple $f$ est discontinue en $1$ : ses limites à gauche et à droite sont différentes, et différentes de $f(1)$. La convergence n’est donc pas uniforme sur $\mathbb R_+$.

Le rappel logique annoté est : continuité des $f_n$ et convergence uniforme impliquent la continuité de $f$ ; la contraposée permet ici d’exclure la convergence uniforme.

#### Exercice 1 — 5 (traité avant la question 4)

Pour $n\ge1$, $f_n:[0,1]\to\mathbb R$, $f_n(x)=(ne^{-x}+x^2)/(n+x)$.

Pour tout $x\in[0,1]$, $f_n(x)\sim ne^{-x}/n=e^{-x}$ ; la limite simple est donc $f(x)=e^{-x}$.

## Page 7

**Exercice 1, 5 (suite).** $f_n\to f:x\mapsto e^{-x}$ simplement sur $[0,1]$.

Pour la convergence uniforme,
$$|f_n(x)-f(x)|=\left|\frac{ne^{-x}+x^2}{n+x}-e^{-x}\right|=\left|\frac{x(x-e^{-x})}{n+x}\right|.$$
Poser $g_n(x)=[x^2-xe^{-x}]/(n+x)$ et chercher une borne de $\sup_{[0,1]}|g_n|$.

**Note de transcription :** la dernière fraction de la ligne manuscrite perd les barres de valeur absolue ; $g_n$ peut être négative, et c’est bien $|g_n|$ qui mesure l’erreur.

## Page 8

**Exercice 1, 5 (fin).** Pour $x\in[0,1]$, $n\le n+x\le n+1$, donc $1/(n+1)\le1/(n+x)\le1/n$. Par ailleurs, $0\le x^2\le1$ et $e^{-1}\le e^{-x}\le1$, d’où $-1\le-xe^{-x}\le0$. Ainsi
$$-1\le x^2-xe^{-x}\le1,$$
$$-\frac1n\le-\frac1{n+x}\le g_n(x)\le\frac1{n+x}\le\frac1n.$$
Donc $|g_n(x)|\le1/n$ pour tout $x\in[0,1]$ ; comme $1/n\to0$, $f_n\to e^{-x}$ uniformément sur $[0,1]$.

## Page 9

#### Exercice 1 — 1, seconde méthode

$f_n(x)=x/(1+nx)$ sur $[0,1]$. Le même raisonnement en $x=0$ et $x\ne0$ donne la limite simple nulle.

Pour la convergence uniforme,
$$|f_n(x)-0|=f_n(x),\qquad f_n'(x)=\frac{1+nx-nx}{(1+nx)^2}=\frac1{(1+nx)^2}>0.$$
Le tableau montre une croissance de $f_n(0)=0$ à $f_n(1)=1/(1+n)$. Donc
$$\sup_{x\in[0,1]}|f_n(x)|=\frac1{n+1}\to0.$$
La convergence vers zéro est uniforme.

## Page 10

#### Exercice 1 — 4

$f_n:[0,1]\to\mathbb R$, $f_n(x)=(1-x^n)/(1+x^{2n})$.

**Convergence simple.** En $x=1$, $f_n(1)=0$. Pour $0\le x<1$, $x^n\to0$ et $x^{2n}\to0$, donc $f_n(x)\to1$. Ainsi
$$f(x)=\begin{cases}1&0\le x<1,\\0&x=1.\end{cases}$$
Pour chaque $n$, $f_n$ est continue en $1$. La limite simple $f$ ne l’est pas.

## Page 11

**Exercice 1, 4 (suite).** Comme $f(1)=0$ mais $\lim_{x\to1^-}f(x)=1$, le théorème de continuité de la limite uniforme exclut la convergence uniforme sur $[0,1]$.

Pour $a\in]0,1[$, étudier la convergence sur $[0,a]$, où la limite vaut $1$. On a
$$|f_n(x)-1|=\left|\frac{1-x^n}{1+x^{2n}}-1\right|=\frac{x^n(1+x^n)}{1+x^{2n}}.$$
Comme $x^n\le a^n$, $1+x^n\le2$ et $1+x^{2n}\ge1$,
$$|f_n(x)-1|\le2a^n.$$
Cette borne tend vers zéro, puisque $0<a<1$.

## Page 12

**Exercice 1, 4 (fin).** $\sup_{x\in[0,a]}|f_n(x)-f(x)|\to0$ : convergence uniforme sur tout $[0,a]$ avec $a<1$.

#### Exercice 1 — 6

$f_n:\mathbb R_+\to\mathbb R$, $f_n(x)=e^{-nx}\sin(nx)$.

**Convergence simple.** Pour $x>0$, $|f_n(x)|\le e^{-nx}\to0$. En $x=0$, $f_n(0)=0$. Donc $f_n\to0$ simplement sur $\mathbb R_+$.

**Convergence uniforme.** Prendre $x_n=1/n$ :
$$|f_n(x_n)|=e^{-1}\sin1=\frac{\sin1}e>0.$$
Le supremum de l’erreur est au moins cette constante, donc ne tend pas vers zéro. La convergence n’est pas uniforme sur $\mathbb R_+$.

La distinction $x>0$ et $x=0$ précise la majoration manuscrite, dont le membre droit ne tend pas vers zéro en $x=0$.

## Page 13

**Exercice 1, 6 (conclusion).** La norme uniforme de $f_n-f$ ne tend pas vers zéro : absence de convergence uniforme sur $\mathbb R_+$.

#### Exercice 1 — 7

$f_n:[0,1]\to\mathbb R$, $f_n(x)=e^{-nx^2}\sin(nx^2)$.

Pour $x>0$, $|f_n(x)|\le e^{-nx^2}\to0$ ; en zéro, $f_n(0)=0$. La limite simple est $f=0$.

Prendre $x_n=1/\sqrt n\in[0,1]$. Alors
$$|f_n(x_n)|=e^{-1}\sin1>0,$$
donc $\|f_n-f\|_\infty\ge e^{-1}\sin1$ ne tend pas vers zéro.

## Page 14

**Exercice 1, 7 (suite).** La convergence n’est pas uniforme sur $[0,1]$.

Pour $a\in]0,1[$ et $x\in[a,1]$, $|\sin(nx^2)|\le1$ et $e^{-nx^2}\le e^{-na^2}$. Donc
$$\sup_{x\in[a,1]}|f_n(x)-f(x)|\le e^{-na^2}\to0.$$
La convergence est uniforme sur $[a,1]$.

**Note de transcription :** cette page écrit $\sin(nx)$ dans plusieurs lignes, tandis que la fonction définie à la page précédente contient $\sin(nx^2)$. La majoration par $1$ est valable dans les deux cas ; la notation de la définition est conservée ici.

## Page 15

#### Exercice 1 — 8

$f_n:[0,\pi/2]\to\mathbb R$, $f_n(x)=\sin^n x$.

**Convergence simple.** En $x=\pi/2$, $f_n(x)=1$. Pour $0\le x<\pi/2$, $0\le\sin x<1$, donc $(\sin x)^n\to0$. La limite simple est
$$f(x)=\begin{cases}0&0\le x<\pi/2,\\1&x=\pi/2.\end{cases}$$
Pour la convergence uniforme, noter que chaque $f_n$ est continue en $\pi/2$.

## Page 16

**Exercice 1, 8 (suite).** La limite $f$ n’est pas continue en $\pi/2$, puisque $f(\pi/2)=1$ mais sa limite à gauche vaut zéro. Le théorème de continuité d’une limite uniforme exclut donc la convergence uniforme sur $[0,\pi/2]$.

Pour $a\in]0,\pi/2[$, étudier la convergence sur $[0,a]$. La limite y est nulle et
$$|f_n(x)-f(x)|=(\sin x)^n.$$
Le sinus est croissant sur $[0,\pi/2]$ ; pour $x\in[0,a]$, $0\le\sin x\le\sin a$.

**Note de transcription :** la première phrase de la page affirme par erreur une convergence « uniformément » sur l’intervalle complet ; le raisonnement qui suit la réfute. Il s’agit à cet endroit de la convergence simple déjà établie.

## Page 17

**Exercice 1, 8 (fin).** Pour $x\in[0,a]$,
$$0\le(\sin x)^n\le(\sin a)^n,$$
$$\|f_n-f\|_{\infty,[0,a]}\le(\sin a)^n\to0,$$
car $0<\sin a<1$. Donc $f_n\to f$ uniformément sur $[0,a]$.

## Page 18

#### Exercice 1 — 9, première rédaction

Pour $n\ge1$, $f_n:\mathbb R_+\to\mathbb R$,
$$f_n(x)=\sin\sqrt{x+4\pi^2n^2}-\frac{x}{4\pi n}.$$
Pour $x$ fixé,
$$\sqrt{x+4\pi^2n^2}=2\pi n\sqrt{1+\frac{x}{4\pi^2n^2}}=2\pi n+\frac{x}{4\pi n}+o(n^{-1}).$$
Par périodicité du sinus,
$$f_n(x)=\sin\left(\frac{x}{4\pi n}+o(n^{-1})\right)-\frac{x}{4\pi n}\to0.$$
Ainsi la limite simple sur $\mathbb R_+$ est nulle.

**Note de transcription :** le manuscrit poursuit avec un terme $-x^3/(384\pi^3n^3)$ en négligeant la contribution de la racine à l’ordre 3. Le développement à cet ordre serait
$$f_n(x)=-\left(\frac{x^2}{64\pi^3}+\frac{x^3}{384\pi^3}\right)n^{-3}+o(n^{-3}).$$
Le développement à l’ordre 1 suffit à la limite demandée ; la conclusion de convergence simple est correcte.

## Page 19

**Exercice 1, 9 — étude uniforme, première rédaction.** La page essaie le choix $x_n=4\pi^2n^2$ et écrit $f_n(x_n)=-\pi n$, en remplaçant le signe $+$ sous la racine par un signe $-$. Elle en déduit un supremum au moins égal à $\pi n$ et l’absence de convergence uniforme.

**Correction de la substitution.** Pour la fonction définie page 18 avec le signe $+$,
$$f_n(4\pi^2n^2)=\sin(2\sqrt2\pi n)-\pi n,$$
donc
$$\sup_{x\ge0}|f_n(x)|\ge\pi n-1\to+\infty.$$
La conclusion demeure : **pas de convergence uniforme sur $\mathbb R_+$**. En fait, pour chaque $n$ fixé, $f_n(x)$ est non bornée quand $x\to+\infty$, puisque le sinus est borné et $-x/(4\pi n)\to-\infty$ ; le supremum est $+\infty$. La notation de norme du manuscrit doit être comprise ici comme supremum étendu.

## Page 20

#### Exercice 1 — 9, seconde rédaction

Le manuscrit reprend la même fonction
$$f_n(x)=\sin\sqrt{x+4\pi^2n^2}-\frac{x}{4\pi n},\qquad n\ge1.$$
Il factorise $4\pi^2n^2$ sous la racine et utilise
$$\sqrt{1+\frac{x}{4\pi^2n^2}}=1+\frac{x}{8\pi^2n^2}+o(n^{-2}).$$
Après multiplication par $2\pi n$ et périodicité,
$$f_n(x)=\sin\left(\frac{x}{4\pi n}+o(n^{-1})\right)-\frac{x}{4\pi n}\to0.$$
La limite simple est donc nulle sur $\mathbb R_+$.

La page affiche ensuite $-x^3/(384\pi^3n^3)+o(n^{-3})$ ; comme signalé page 18, cette précision oublie le terme $-x^2/(64\pi^3n^3)$ venant du développement de la racine. Cela ne change pas la limite.

## Page 21

**Exercice 1, 9 — étude uniforme, seconde rédaction.** La même substitution $x_n=4\pi^2n^2$ est reprise, avec à nouveau un signe $-$ sous la racine et la valeur annoncée $-\pi n$. Pour la définition avec $+$, la borne correcte est $|f_n(x_n)|\ge\pi n-1$ (page 19). L’absence de convergence uniforme sur $\mathbb R_+$ est confirmée.

#### Exercice 1 — 10

Pour $\alpha\in\mathbb R$ et $n\ge1$,
$$f_n:\mathbb R_+\to\mathbb R,\qquad f_n(x)=n^\alpha xe^{-nx}.$$

## Page 22

**Exercice 1, 10 (suite).**
$$f_n(x)=xe^{-nx+\alpha\ln n}.$$
Pour $x>0$ fixé, cette expression tend vers zéro par croissance comparée ; en zéro, $f_n(0)=0$. La convergence simple sur $\mathbb R_+$ est donc vers $f=0$.

Pour la convergence uniforme, $g_n(x)=|f_n(x)|=n^\alpha xe^{-nx}$ et
$$g_n'(x)=n^\alpha(1-nx)e^{-nx}.$$
La dérivée s’annule en $1/n$, est positive avant, négative après. Le tableau montre une croissance de zéro à $g_n(1/n)$, puis une décroissance vers zéro. Donc
$$\sup_{x\ge0}|f_n(x)|=g_n(1/n).$$

## Page 23

**Exercice 1, 10 (fin).**
$$g_n(1/n)=n^{\alpha-1}e^{-1}.$$
Si $\alpha=1$, le supremum vaut $e^{-1}$ : pas de convergence uniforme. Si $\alpha>1$, il tend vers $+\infty$ : pas de convergence uniforme. Si $\alpha<1$, il tend vers zéro : convergence uniforme vers zéro sur $\mathbb R_+$.

#### Exercice 2

Pour $k\in\mathbb N$ et $n\ge1$,
$$f_n:\mathbb R\to\mathbb R,\qquad f_n(x)=\frac{x^k}{x^2+n}.$$
Pour tout réel $x$ fixé, $f_n(x)\to0$.

## Page 24

**Exercice 2 — convergence uniforme.** La limite simple sur $\mathbb R$ est $f=0$. Pour les variations,
$$f_n'(x)=\frac{kx^{k-1}(x^2+n)-2x^{k+1}}{(x^2+n)^2}=\frac{x^{k-1}[(k-2)x^2+kn]}{(x^2+n)^2}.$$
Pour $k\ne2$, les racines non nulles éventuelles vérifient $x^2=kn/(2-k)$. L’écriture factorisée en $x^{k-1}$ est utilisée pour $k\ge1$, le cas $k=0$ étant traité séparément.

**Premier cas : $k=0$.** $f_n(x)=1/(x^2+n)$, et $|f_n(x)|\le1/n$ pour tout $x$. Donc $\|f_n\|_\infty\le1/n\to0$ : convergence uniforme sur $\mathbb R$.

## Page 25

**Exercice 2 — $k=1$.**
$$f_n(x)=\frac{x}{x^2+n},\qquad f_n'(x)=\frac{n-x^2}{(x^2+n)^2}.$$
La dérivée s’annule en $\pm\sqrt n$. La fonction décroît de $0$ à $-1/(2\sqrt n)$ sur $]-\infty,-\sqrt n]$, croît jusqu’à $1/(2\sqrt n)$ sur $[-\sqrt n,\sqrt n]$, puis décroît vers zéro. Ainsi
$$\|f_n\|_\infty=\frac1{2\sqrt n}\to0.$$
Il y a convergence uniforme sur $\mathbb R$.

**$k=2$.**
$$f_n(x)=\frac{x^2}{x^2+n},\qquad f_n'(x)=\frac{2nx}{(x^2+n)^2}.$$
La fonction, paire, décroît de la limite $1$ à $0$ sur $]-\infty,0]$, puis croît vers $1$. Son supremum vaut $1$ : pas de convergence uniforme sur $\mathbb R$. On peut aussi choisir $x_n=n$ :
$$f_n(n)=\frac{n^2}{n+n^2}=\frac1{1+1/n}\to1.$$

**Note de transcription :** certains radicaux dans le premier tableau et l’évaluation de l’extremum sont mal placés. Les points critiques sont $\pm\sqrt n$, et leur image vaut $\pm1/(2\sqrt n)$, conformément à la norme finale.

## Page 26

**Exercice 2 — $k>2$.** Première méthode :
$$\|f_n\|_\infty\ge |f_n(n)|=\frac{n^k}{n+n^2}\sim n^{k-2}\to+\infty.$$
Il n’y a donc pas de convergence uniforme sur $\mathbb R$.

Deuxième méthode :
$$f_n'(x)=\frac{x^{k-1}[(k-2)x^2+kn]}{(x^2+n)^2}.$$
Pour $k>2$, le facteur entre crochets est strictement positif. Si $k$ est pair, la dérivée a le signe de $x$ : la fonction décroît de $+\infty$ à zéro, puis croît vers $+\infty$. Si $k$ est impair, la dérivée est positive hors zéro : la fonction croît de $-\infty$ à $+\infty$. Dans les deux cas, $\sup_{x\in\mathbb R}|f_n(x)|=+\infty$ pour chaque $n$ ; la notation de norme est donc un supremum étendu.

## Page 27

**Exercice 2 — bilan sur $\mathbb R$.**

| $k$ | $\sup_{\mathbb R}|f_n|$ | Convergence uniforme vers zéro |
|---|---|---|
| $0$ | $1/n$ | Oui |
| $1$ | $1/(2\sqrt n)$ | Oui |
| $2$ | $1$ | Non |
| $>2$ | $+\infty$ | Non |

**2. Sur $[a,b]$, avec $a<b$ réels.** Pour $k=0$ ou $k=1$, la convergence uniforme sur $\mathbb R$ implique celle sur tout segment $[a,b]$. Pour $k=2$, on reprend le tableau : décroissance jusqu’à zéro puis croissance, avec limites $1$ aux deux infinis. Il faut distinguer la position du segment par rapport à zéro.

## Page 28

**Exercice 2 — $k=2$ sur un segment.** Les graphiques placent successivement le segment à droite de zéro, de part et d’autre de zéro, puis à gauche.

- Si $0\le a<b$, la fonction est positive et croissante :
$$\sup_{x\in[a,b]}|f_n(x)|=f_n(b)=\frac{b^2}{b^2+n}\to0.$$
- Si $a<0<b$, le maximum est atteint à l’une des extrémités :
$$\sup_{x\in[a,b]}|f_n(x)|=\max\left(\frac{a^2}{a^2+n},\frac{b^2}{b^2+n}\right)\to0.$$
- Si $a<b\le0$, la fonction est positive et décroissante :
$$\sup_{x\in[a,b]}|f_n(x)|=f_n(a)=\frac{a^2}{a^2+n}\to0.$$

Dans tous les cas, convergence uniforme sur $[a,b]$.

## Page 29

**Exercice 2 — $k>2$ pair sur un segment.** La fonction est positive, décroissante sur $\mathbb R_-$, croissante sur $\mathbb R_+$. Les trois schémas conduisent à
$$\sup_{[a,b]}|f_n|=\begin{cases}f_n(a),&a<b\le0,\\\max(f_n(a),f_n(b)),&a<0<b,\\f_n(b),&0\le a<b.\end{cases}$$
Pour chaque extrémité fixe, $f_n(a)\to0$ et $f_n(b)\to0$. Le supremum tend donc vers zéro dans les trois cas : convergence uniforme sur tout segment.

## Page 30

**Exercice 2 — $k>2$ impair sur un segment.** La fonction est croissante, négative pour $x<0$ et positive pour $x>0$. Les trois schémas donnent
$$\sup_{[a,b]}|f_n|=\begin{cases}|f_n(a)|,&a<b\le0,\\\max(|f_n(a)|,|f_n(b)|),&a<0<b,\\|f_n(b)|,&0\le a<b.\end{cases}$$
Les valeurs aux extrémités tendent vers zéro. Il y a donc, ici encore, convergence uniforme sur tout segment $[a,b]$.

## Page 31

**Exercice 2 — conclusion.** Pour tout $k\in\mathbb N$, la suite $x\mapsto x^k/(x^2+n)$ converge uniformément vers zéro sur chaque segment de $\mathbb R$, et par restriction sur toute partie bornée de $\mathbb R$.

#### Exercice 4

Pour $n\ge1$,
$$f_n:[-1,1]\to\mathbb R,\qquad f_n(x)=\frac{x}{1+n^2x^2}.$$
**1. Convergence simple.** Pour $x=0$, $f_n(0)=0$, donc la limite est nulle. Le cas $x\ne0$ se poursuit page suivante.

## Page 32

**Exercice 4 — 1, suite.** Pour $x\ne0$ fixé,
$$f_n(x)\sim\frac1{n^2x}\to0.$$
La limite simple est $f=0$ sur $[-1,1]$. Pour la convergence uniforme,
$$f_n'(x)=\frac{1-n^2x^2}{(1+n^2x^2)^2}.$$
Les points critiques sont $\pm1/n$. Le tableau donne les valeurs
$$f_n(-1)=-\frac1{1+n^2},\quad f_n(-1/n)=-\frac1{2n},\quad f_n(1/n)=\frac1{2n},\quad f_n(1)=\frac1{1+n^2}.$$
La fonction décroît jusqu’à $-1/n$, croît jusqu’à $1/n$, puis décroît. Donc
$$\|f_n\|_{\infty,[-1,1]}=\frac1{2n}\to0.$$

## Page 33

**Exercice 4 — 1, conclusion.** La suite $(f_n)$ converge uniformément vers zéro sur $[-1,1]$.

**2. Suite des dérivées.**
$$f_n'(x)=\frac{1-n^2x^2}{(1+n^2x^2)^2}.$$
En zéro, $f_n'(0)=1$. Pour $x\ne0$ fixé, $f_n'(x)\sim-1/(n^2x^2)\to0$. La limite simple est donc
$$h(x)=\begin{cases}1,&x=0,\\0,&x\ne0.\end{cases}$$
Chaque dérivée $f_n'$ est continue, tandis que $h$ est discontinue en zéro. Il ne peut donc pas y avoir convergence uniforme des dérivées sur $[-1,1]$.

## Page 34

**Exercice 4 — 3.** On pose
$$g_n(x)=\frac{\ln(1+n^2x^2)}{2n^2},\qquad x\in[-1,1],\quad n\ge1.$$
Alors
$$g_n'(x)=\frac{2n^2x}{2n^2(1+n^2x^2)}=f_n(x).$$
Pour $x=0$, $g_n(0)=0$. Pour $x\ne0$ fixé, le logarithme croît moins vite que $n^2$, donc $g_n(x)\to0$. Plus précisément,
$$g_n(x)=\frac{2\ln n+\ln(x^2+n^{-2})}{2n^2}\to0.$$
La limite simple est nulle sur $[-1,1]$.

**Note de transcription :** une ligne intermédiaire manuscrite omet le facteur $2$ du dénominateur ; la définition de $g_n$ ci-dessus et sa dérivée le conservent.

## Page 35

**Exercice 4 — 3, convergence uniforme.** La dérivée $g_n'=f_n$ a le signe de $x$. La fonction $g_n$, paire et positive, décroît sur $[-1,0]$ de $\ln(1+n^2)/(2n^2)$ à zéro, puis croît vers cette même valeur sur $[0,1]$. Ainsi
$$\|g_n\|_{\infty,[-1,1]}=\frac{\ln(1+n^2)}{2n^2}\to0.$$
La convergence de $(g_n)$ vers zéro est uniforme sur $[-1,1]$.

## Page 36

**Exercice 4 — 3, autre méthode.** On utilise le théorème de convergence des suites de fonctions dérivables :

- chaque $g_n$ est de classe $C^1$ sur $[-1,1]$ ;
- $g_n'=f_n$ converge uniformément vers zéro, d’après la question 1 ;
- $(g_n)$ converge simplement vers zéro (en particulier, $g_n(0)=0$).

Le théorème donne la convergence uniforme de $(g_n)$ vers $g=0$ sur $[-1,1]$ et la dérivation de la limite :
$$g'=\lim_{n\to\infty}g_n'=\lim_{n\to\infty}f_n=0.$$

## Page 37

#### Exercice 5

Pour $n\ge1$, on définit sur $[0,1]$
$$f_n(x)=\begin{cases}n^2x(1-nx),&0\le x\le1/n,\\0,&\text{sinon}.\end{cases}$$
**1. Convergence simple.** En zéro, $f_n(0)=0$. Pour tout $x>0$ fixé, comme $1/n\to0$, on a $x>1/n$ à partir d’un certain rang ; alors $f_n(x)=0$. Donc $(f_n)$ converge simplement vers la fonction nulle sur $[0,1]$.

**Précision de lecture :** la distinction manuscrite entre $x\in[0,1/n]$ et $x\notin[0,1/n]$ dépend de $n$ ; l’argument à $x$ fixé est celui explicité ci-dessus.

## Page 38

**Exercice 5 — 2. Intégrale.**
$$\int_0^1f_n(t)\,dt=\int_0^{1/n}n^2t(1-nt)\,dt+\int_{1/n}^1 0\,dt.$$
Donc
$$\int_0^1f_n(t)\,dt=\left[\frac{n^2t^2}{2}-\frac{n^3t^3}{3}\right]_0^{1/n}=\frac12-\frac13=\frac16.$$
Par conséquent,
$$\lim_{n\to\infty}\int_0^1f_n(t)\,dt=\frac16.$$

## Page 39

**Exercice 5 — 2, conclusion.** Puisque la limite simple est nulle,
$$\int_0^1\lim_{n\to\infty}f_n(t)\,dt=0\ne\frac16=\lim_{n\to\infty}\int_0^1f_n(t)\,dt.$$
Or chaque $f_n$ est continue sur $[0,1]$, y compris au raccord $1/n$. Si la convergence était uniforme, le théorème d’interversion limite–intégrale imposerait l’égalité. Ainsi $(f_n)$ **ne converge pas uniformément** sur $[0,1]$.

## Page 40

**Exercice 5 — 3.** Soit $a\in]0,1[$. Comme $a>0$, il existe un entier $N$ tel que
$$a>\frac1N\ge\frac1n\quad\text{pour tout }n\ge N.$$
Le schéma place $1/n$ à gauche de $a$ sur $[0,1]$. Pour $x\in[a,1]$ et $n\ge N$, $f_n(x)=0$. Ainsi
$$\sup_{x\in[a,1]}|f_n(x)-0|=0\quad(n\ge N).$$
La convergence est uniforme sur tout $[a,1]$, $a>0$.

## Page 41

#### Exercice 6 — 1

Calculer
$$\lim_{n\to\infty}\int_0^1\frac{ne^x}{n+x}\,dx.$$
On pose $f_n(x)=ne^x/(n+x)$ sur $[0,1]$, pour $n\ge1$. Chaque $f_n$ est continue sur ce segment. Pour $x$ fixé,
$$f_n(x)\sim\frac{ne^x}{n}=e^x.$$
La limite simple est donc $f:x\mapsto e^x$. On étudie ensuite la convergence uniforme pour intervertir limite et intégrale.

## Page 42

**Exercice 6 — 1, majoration uniforme.** Pour $x\in[0,1]$,
$$|f_n(x)-f(x)|=\left|\frac{ne^x}{n+x}-e^x\right|=\frac{xe^x}{n+x}.$$
Comme $xe^x\le e$ et $n+x\ge n$,
$$|f_n(x)-f(x)|\le\frac en,$$
indépendamment de $x$. Cette borne tend vers zéro.

## Page 43

**Exercice 6 — 1, conclusion.**
$$\|f_n-f\|_{\infty,[0,1]}\le\frac en\to0.$$
Les fonctions sont continues et convergent uniformément ; le théorème d’interversion donne
$$\lim_{n\to\infty}\int_0^1\frac{ne^x}{n+x}\,dx=\int_0^1e^x\,dx=e-1.$$

## Page 44

#### Exercice 6 — 2

On pose
$$f_n:[0,1]\to\mathbb R,\qquad f_n(x)=\frac{x^5}{(1+x^2)^n}.$$
Chaque $f_n$ est continue sur $[0,1]$. Pour $x=0$, $f_n(0)=0$. Pour $x\in]0,1]$, $1+x^2>1$ et la suite géométrique $(1+x^2)^n$ tend vers $+\infty$ ; donc $f_n(x)\to0$. La convergence simple est vers $f=0$.

## Page 45

**Exercice 6 — 2, convergence uniforme.** La fonction $f_n$ est positive et
$$f_n'(x)=\frac{5x^4(1+x^2)^n-2nx^6(1+x^2)^{n-1}}{(1+x^2)^{2n}}=\frac{x^4[5-(2n-5)x^2]}{(1+x^2)^{n+1}}.$$
Pour $n\ge5$, le point critique positif
$$x_n=\sqrt{\frac5{2n-5}}$$
appartient à $[0,1]$. Le tableau montre une croissance de $f_n(0)=0$ jusqu’à $f_n(x_n)$, puis une décroissance jusqu’à $f_n(1)=2^{-n}$. Ainsi le supremum est $f_n(x_n)$.

La condition $n\ge3$ écrite près de la racine assure seulement $2n-5>0$ ; la condition $n\ge5$ indiquée près du tableau assure aussi $x_n\le1$.

## Page 46

**Exercice 6 — 2, valeur du maximum.**
$$f_n(x_n)=\frac{\left(5/(2n-5)\right)^{5/2}}{\left(1+5/(2n-5)\right)^n}=\left(\frac5{2n-5}\right)^{5/2}\exp\left[-n\ln\left(1+\frac5{2n-5}\right)\right].$$
Or
$$-n\ln\left(1+\frac5{2n-5}\right)=-n\left(\frac5{2n-5}+o(n^{-1})\right)\to-\frac52.$$
Le facteur exponentiel tend vers $e^{-5/2}$ et le premier facteur vers zéro. Donc
$$\|f_n\|_{\infty,[0,1]}=f_n(x_n)\to0.$$

## Page 47

**Exercice 6 — 2, intégrale.** La suite converge uniformément vers zéro sur $[0,1]$. Par continuité et interversion,
$$\lim_{n\to\infty}\int_0^1\frac{x^5}{(1+x^2)^n}\,dx=\int_0^1 0\,dx=0.$$

**Remarque.** Sans étudier les variations, on peut montrer directement la convergence localement uniforme sur $]0,1]$. Soit $a\in]0,1[$ et $x\in[a,1]$ ; la majoration se poursuit page suivante.

## Page 48

**Exercice 6 — 2, remarque, suite.** Pour $x\in[a,1]$,
$$0\le f_n(x)=\frac{x^5}{(1+x^2)^n}\le\frac1{(1+a^2)^n}\to0.$$
La borne ne dépend pas de $x$ ; ainsi
$$\|f_n\|_{\infty,[a,1]}\le(1+a^2)^{-n}\to0.$$
Il y a convergence uniforme sur chaque $[a,1]$, $a>0$, donc convergence localement uniforme sur $]0,1]$. Cette remarque concerne cet intervalle ; la preuve sur $[0,1]$ a été donnée pages 45–46.

## Page 49

#### Exercice 7

Pour $n\ge1$,
$$f_n:[0,1]\to\mathbb R,\qquad f_n(x)=\frac{ne^{-x}+x^2}{n+x}.$$
**1.** Pour $x$ fixé, $f_n(x)\sim ne^{-x}/n=e^{-x}$. La limite simple est $f(x)=e^{-x}$. Pour l’étude uniforme,
$$|f_n(x)-f(x)|=\left|\frac{ne^{-x}+x^2-ne^{-x}-xe^{-x}}{n+x}\right|=\frac{|x(x-e^{-x})|}{n+x}.$$

## Page 50

**Exercice 7 — 1, suite.** Sur $[0,1]$, $0\le x^2\le1$ et $0\le xe^{-x}\le1$, donc $|x^2-xe^{-x}|\le1$. De plus, $n+x\ge n$. Ainsi
$$|f_n(x)-f(x)|\le\frac1n,\qquad\|f_n-f\|_{\infty,[0,1]}\le\frac1n\to0.$$
La convergence est uniforme.

**2.** Chaque $f_n$ est continue sur $[0,1]$ et la convergence y est uniforme : les hypothèses du théorème d’interversion limite–intégrale sont réunies.

**Précision :** les annotations de la page indiquent $x^2\le1$ et $-xe^{-x}\le0$ ; pour majorer la valeur absolue, il faut également la borne inférieure $x^2-xe^{-x}\ge-1$, utilisée ci-dessus.

## Page 51

**Exercice 7 — 2, conclusion.** Pour $u_n=\int_0^1f_n(x)\,dx$,
$$\lim_{n\to\infty}u_n=\int_0^1\lim_{n\to\infty}f_n(x)\,dx=\int_0^1e^{-x}\,dx=[-e^{-x}]_0^1=1-e^{-1}.$$
La suite $(u_n)$ converge donc vers $1-e^{-1}$.

## Page 52

#### Exercice 8

On considère
$$f_n:[0,1]\to\mathbb R,\qquad f_n(x)=\frac{n(x^3+x)e^{-x}}{nx+1}.$$
**1. Convergence simple.** En zéro, $f_n(0)=0$. Pour $x\in]0,1]$ fixé,
$$f_n(x)\sim\frac{n(x^3+x)e^{-x}}{nx}=(x^2+1)e^{-x}.$$
La limite est
$$f(x)=\begin{cases}0,&x=0,\\(x^2+1)e^{-x},&x\in]0,1].\end{cases}$$
Remarque : $\lim_{x\to0^+}f(x)=1\ne f(0)$ ; $f$ est discontinue en zéro.

## Page 53

**Exercice 8 — 2.** Soit $\alpha\in]0,1[$. Sur $[\alpha,1]$,
$$|f_n(x)-f(x)|=\left|\frac{n(x^3+x)e^{-x}}{nx+1}-(x^2+1)e^{-x}\right|=\frac{(x^2+1)e^{-x}}{nx+1}.$$
En effet, les termes contenant $n(x^3+x)$ se simplifient. Pour $x\in[\alpha,1]$, on a $x^2+1\le2$, $e^{-x}\le e^{-\alpha}$ et $nx+1\ge n\alpha+1$.

## Page 54

**Exercice 8 — 2, suite.** La majoration indépendante de $x$ est
$$|f_n(x)-f(x)|\le\frac{2e^{-\alpha}}{n\alpha+1}.$$
D’où
$$\|f_n-f\|_{\infty,[\alpha,1]}\le\frac{2e^{-\alpha}}{n\alpha+1}\to0.$$
La suite converge uniformément vers $f$ sur chaque $[\alpha,1]$, $\alpha>0$, donc localement uniformément sur $]0,1]$.

## Page 55

**Exercice 8 — absence de convergence uniforme sur $[0,1]$.** Chaque $f_n$ est continue en zéro et la suite converge simplement vers $f$. Mais $f$ n’est pas continue en zéro. D’après le théorème de continuité de la limite uniforme, la convergence ne peut pas être uniforme sur $[0,1]$.

## Page 56

**Exercice 8 — reprise des résultats.** La page rappelle la famille
$$f_n(x)=\frac{n(x^3+x)e^{-x}}{nx+1}$$
et sa limite simple, nulle en zéro et égale à $(x^2+1)e^{-x}$ ailleurs. Elle reprend la convergence uniforme sur $[\alpha,1]$, pour tout $\alpha\in]0,1[$, avec la borne légèrement moins précise
$$\sup_{x\in[\alpha,1]}|f_n(x)-f(x)|\le\frac{2e^{-\alpha}}{n\alpha}\to0.$$
La discontinuité de $f$ en zéro, opposée à la continuité de chaque $f_n$, exclut la convergence uniforme sur $[0,1]$.

## Page 57

**Exercice 8 — 3. Borne globale.** Pour $x\in]0,1]$,
$$|f_n(x)-f(x)|=\frac{(x^2+1)e^{-x}}{nx+1}\le2,$$
car $x^2+1\le2$, $e^{-x}\le1$ et $nx+1\ge1$. En zéro, $f_n(0)=f(0)=0$, donc la même borne vaut. Ainsi
$$|f_n(x)-f(x)|\le2\quad\text{pour tout }x\in[0,1]\text{ et tout }n.$$
**4.** Étudier la convergence de la suite $\left(\int_0^1f_n(x)\,dx\right)_n$ et calculer sa limite.

## Page 58

**Exercice 8 — 4.** On note
$$u_n=\int_0^1f_n(t)\,dt.$$
Pour $\alpha\in]0,1[$, on introduit
$$u_n^\alpha=\int_\alpha^1f_n(t)\,dt.$$
Sur $[\alpha,1]$, chaque $f_n$ est continue et $(f_n)$ converge uniformément vers $f$. On peut donc appliquer l’interversion limite–intégrale sur ce segment.

## Page 59

**Exercice 8 — 4, suite.** Pour tout $\alpha\in]0,1[$ fixé,
$$u_n^\alpha\longrightarrow\int_\alpha^1 f(t)\,dt.$$
Il reste à démontrer
$$u_n\longrightarrow\int_0^1f(t)\,dt,$$
ce qui équivaut à
$$\int_0^1(f_n(t)-f(t))\,dt\longrightarrow0.$$
La page prépare une coupure de l’intégrale en $[0,\alpha]$ et $[\alpha,1]$.

## Page 60

**Exercice 8 — 4, contrôle près de zéro.** En découpant puis en utilisant la borne de la question 3,
$$\left|\int_0^1(f_n-f)\,dt\right|\le\int_0^\alpha|f_n-f|\,dt+\left|\int_\alpha^1(f_n-f)\,dt\right|\le2\alpha+\left|\int_\alpha^1(f_n-f)\,dt\right|.$$
Le second terme tend vers zéro pour $\alpha$ fixé. Ainsi
$$\limsup_{n\to\infty}\left|\int_0^1(f_n-f)\,dt\right|\le2\alpha.$$
Comme cette borne vaut pour tout $\alpha>0$, on fait tendre $\alpha$ vers zéro, et l’intégrale de la différence tend vers zéro. Donc
$$\lim_{n\to\infty}\int_0^1f_n(t)\,dt=\int_0^1f(t)\,dt.$$

**Note de transcription :** le manuscrit écrit directement une limite avant d’en établir l’existence ; l’emploi de la limite supérieure rend cette étape rigoureuse. Une ligne comporte également un signe $+$ entre $f_n$ et $f$ ; il s’agit bien de leur différence dans ce raisonnement.

## Page 61

**Exercice 8 — calcul de la limite.** La valeur isolée de $f(0)$ ne modifie pas l’intégrale. En intégrant par parties avec $u(t)=t^2+1$ et $v'(t)=e^{-t}$,
$$I=\int_0^1(t^2+1)e^{-t}\,dt=[-(t^2+1)e^{-t}]_0^1+2\int_0^1te^{-t}\,dt.$$
Une seconde intégration par parties donne
$$\int_0^1te^{-t}\,dt=[-te^{-t}]_0^1+\int_0^1e^{-t}\,dt=-e^{-1}+1-e^{-1}.$$
Ainsi
$$I=-2e^{-1}+1+2(1-2e^{-1})=3-6e^{-1}.$$
La limite de $u_n$ vaut donc $3-6/e$.

## Page 62

#### Exercice 9 — composition

On suppose $(f_n)$ uniformément convergente vers $f$ sur $\mathbb R$ et $\varphi:\mathbb R\to\mathbb R$ continue.

**1.** Montrer que $f_n\circ\varphi$ converge uniformément vers $f\circ\varphi$. On a
$$\sup_{x\in\mathbb R}|f_n(\varphi(x))-f(\varphi(x))|=\sup_{y\in\varphi(\mathbb R)}|f_n(y)-f(y)|\le\sup_{y\in\mathbb R}|f_n(y)-f(y)|\to0.$$
D’où la convergence uniforme demandée. La continuité de $\varphi$ n’est pas nécessaire pour cette première propriété.

**Note de transcription :** le manuscrit remplace directement le supremum sur les valeurs $\varphi(x)$ par celui sur tout $\mathbb R$ avec une égalité. Sans surjectivité de $\varphi$, il faut l’inégalité ci-dessus.

## Page 63

**Exercice 9 — 2.** Soit $\psi:\mathbb R\to\mathbb R$ uniformément continue. Montrer que $\psi\circ f_n$ converge uniformément vers $\psi\circ f$.

Le manuscrit utilise le critère de Cauchy uniforme. Fixons $\varepsilon>0$. Par continuité uniforme de $\psi$, il existe $\eta>0$ tel que
$$|u-v|<\eta\implies|\psi(u)-\psi(v)|<\varepsilon.$$
Comme $(f_n)$ converge uniformément, elle est uniformément de Cauchy : il existe $N$ tel que pour tous $p,q\ge N$ et tout $x\in\mathbb R$,
$$|f_p(x)-f_q(x)|<\eta.$$
Donc $|\psi(f_p(x))-\psi(f_q(x))|<\varepsilon$, uniformément en $x$.

**Note de transcription :** la page emploie $\varepsilon$ à la fois comme seuil sur l’entrée et sur la sortie de $\psi$ ; les deux seuils sont distingués ici par $\eta$ et $\varepsilon$.

## Page 64

**Exercice 9 — 2, conclusion.** La suite $(\psi\circ f_n)$ satisfait le critère de Cauchy uniforme, donc converge uniformément. Sa limite simple est $\psi\circ f$ par continuité de $\psi$ ; c’est donc aussi sa limite uniforme.

**Rappel.** Une fonction $g$ est uniformément continue sur un intervalle $I$ lorsque
$$\forall\varepsilon>0,\ \exists\eta>0,\ \forall x,y\in I,\quad |x-y|<\eta\implies|g(x)-g(y)|<\varepsilon.$$
**3.** On considère $\psi(x)=x^2$ sur $\mathbb R$. Cette fonction n’est pas uniformément continue.

## Page 65

**Exercice 9 — 3, non-uniforme continuité du carré.** Supposons par l’absurde que $\psi(x)=x^2$ soit uniformément continue. Pour $\varepsilon=1$, il existerait $\eta>0$ tel que $|x-y|<\eta$ implique $|x^2-y^2|<1$. Choisissons
$$x=\frac\eta2+\frac1\eta,\qquad y=\frac1\eta.$$
Alors $|x-y|=\eta/2<\eta$, mais
$$|x^2-y^2|=1+\frac{\eta^2}{4}>1,$$
contradiction. La fonction carré n’est donc pas uniformément continue sur $\mathbb R$.

**Note de transcription :** le dernier terme est écrit $\eta^2/2$ dans le manuscrit ; le développement du carré donne $\eta^2/4$, sans changer la contradiction.

## Page 66

**Exercice 9 — 3, exemple de suite.** Posons $f_n(x)=x+1/n$ pour $n\ge1$. Pour chaque réel $x$, $f_n(x)\to x$. De plus,
$$\sup_{x\in\mathbb R}|f_n(x)-x|=\frac1n\to0.$$
La convergence de $(f_n)$ vers $f=\operatorname{id}_{\mathbb R}$ est uniforme. On examine si la composition à gauche par $\psi(x)=x^2$ conserve cette propriété.

## Page 67

**Exercice 9 — 3, compositions.**
$$\psi\circ f_n(x)=(x+1/n)^2\longrightarrow x^2=\psi\circ f(x)$$
pour tout $x$ fixé : convergence simple. Mais en choisissant $x_n=n$,
$$\psi(f_n(x_n))-\psi(f(x_n))=\frac{2x_n}{n}+\frac1{n^2}=2+\frac1{n^2}\to2\ne0.$$

## Page 68

**Exercice 9 — 3, défaut d’uniformité.**
$$\sup_{x\in\mathbb R}|\psi(f_n(x))-\psi(f(x))|\ge\left|\psi(f_n(n))-\psi(f(n))\right|\ge2.$$
Ce supremum ne tend pas vers zéro, donc la convergence des compositions n’est pas uniforme sur $\mathbb R$.

La conclusion manuscrite commence : « La continuité uniforme de $\psi$ est une condition nécessaire pour que… », et se poursuit page suivante. Ce contre-exemple montre que la simple continuité de $\psi$ ne suffit pas à garantir la propriété pour toutes les suites considérées. Il ne prouve pas une nécessité pour une suite particulière : par exemple, une suite constante $f_n=f$ conserve la convergence uniforme pour toute $\psi$.

## Page 69

**Exercice 9 — fin.** La phrase de la page précédente se termine par « $(\psi\circ f_n)$ converge uniformément sur $\mathbb R$ vers $(\psi\circ f)$ ». Sa portée doit être comprise avec la réserve donnée page 68.

#### Exercice 10

Soit $\psi:\mathbb R\to\mathbb R$ continue. On pose
$$f_n(x)=x+1/n,\qquad g_n=\psi\circ f_n.$$
D’après l’exercice 9, $(f_n)$ converge uniformément vers $f=\operatorname{id}_{\mathbb R}$.

**1.** Montrer que $(g_n)$ converge simplement vers $\psi$.

## Page 70

**Exercice 10 — 1.** Pour tout $x\in\mathbb R$, $x+1/n\to x$. Par continuité de $\psi$,
$$g_n(x)=\psi(x+1/n)\longrightarrow\psi(x).$$
Donc $(g_n)$ converge simplement vers $\psi$ sur $\mathbb R$.

**2.** Cette convergence n’est pas nécessairement uniforme. L’exercice 9 fournit le contre-exemple de $\psi(x)=x^2$, développé page suivante. La continuité uniforme de $\psi$ est une hypothèse suffisante pour appliquer le résultat de composition ; la formulation « il faut » dans le manuscrit n’établit pas une caractérisation.

## Page 71

**Exercice 10 — 2, contre-exemple.** Pour $\psi(x)=x^2$, les fonctions $\psi(x+1/n)$ ne convergent pas uniformément vers $\psi(x)$ sur $\mathbb R$, d’après le calcul de l’exercice 9.

**3.** Montrer la convergence uniforme sur chaque segment $[a,b]$, $a<b$. La continuité de $\psi$ entraîne sa continuité uniforme sur tout segment compact. Pour tenir compte des arguments décalés, on utilise le segment $[a,b+1]$, qui contient $x$ et $x+1/n$ pour $x\in[a,b]$, $n\ge1$. Comme leur distance est $1/n$, la continuité uniforme donne
$$\sup_{x\in[a,b]}|\psi(x+1/n)-\psi(x)|\to0.$$
Ainsi $(g_n)$ converge localement uniformément vers $\psi$ sur $\mathbb R$.

**Note de transcription :** le manuscrit invoque seulement la continuité uniforme sur $[a,b]$ ; le segment élargi est nécessaire pour inclure aussi $x+1/n$.

## Page 72

#### Exercice 3 — repris en fin de document

Le manuscrit donne une fonction par morceaux sur les intervalles
$$]-\infty,0],\quad[0,1/n],\quad[1/n,2/n],\quad[2/n,+\infty[.$$
Les expressions inscrites sont respectivement $0$, $nx^2$, une expression lue $(1-n^2)x^2+2n-1/n$ **[lecture incertaine du terme après le carré]**, et $1/n$.

**Réserve sur la source :** cette définition est incohérente avec les calculs des pages 73–74, qui utilisent $n^2x$ sur $[0,1/n]$. Les expressions des morceaux ne se raccordent pas telles qu’elles sont écrites. La transcription conserve cette divergence plutôt que de reconstruire silencieusement un énoncé.

**1.** La page cherche la limite simple nulle. Pour $x\le0$, la valeur est nulle. Elle remarque aussi que les deux intervalles intermédiaires se resserrent vers zéro.

**Précision du raisonnement :** pour un $x>0$ fixé, on a $x\ge2/n$ à partir d’un certain rang ; c’est donc le dernier morceau, $f_n(x)=1/n$, qui donne la limite, indépendamment des formules intermédiaires. On ne peut pas simplement remplacer un argument dépendant de $n$ par zéro en gardant $f_n$.

## Page 73

**Exercice 3 — 1, fin.** Pour $x>0$ fixé et $n$ assez grand, $f_n(x)=1/n\to0$. Avec le cas $x\le0$, la limite simple est la fonction nulle $f=0$.

**2. Composition.** Si $x\le0$, $f_n(f_n(x))=f_n(0)=0$. Sur $[0,1/n]$, la page utilise maintenant
$$f_n(x)=n^2x,$$
contrairement à $nx^2$ inscrit dans la définition page 72. Elle choisit $x_n=1/n^4$, puis calcule
$$f_n(x_n)=n^2\frac1{n^4}=\frac1{n^2}\in[0,1/n].$$
Le calcul de la seconde composition se poursuit page suivante. Le point noté $x_0$ dans le manuscrit dépend de $n$ ; on le note ici $x_n$.

## Page 74

**Exercice 3 — 2, suite de l’argument manuscrit.** Avec la formule $n^2x$ employée page 73,
$$f_n(f_n(x_n))=n^2\frac1{n^2}=1,$$
tandis que $f(f(x_n))=0$. La page en déduit que $(f_n\circ f_n)$ ne converge pas simplement vers $f\circ f$.

**Note de transcription :** le choix $x_n=1/n^4$ dépend de $n$ ; ce calcul prouve un défaut de convergence **uniforme**, mais ne suffit pas à réfuter la convergence simple. En outre, il utilise la formule $n^2x$, incompatible avec la définition page 72. La conclusion de convergence simple ne peut donc pas être validée par cette démonstration telle qu’écrite.

**Remarque manuscrite.** Avec $x_n=1/n^2$ et toujours la formule $n^2x$,
$$f_n(x_n)=1,\qquad\sup_x|f_n(x)-0|\ge1,$$
ce qui exclurait la convergence uniforme de $(f_n)$. La page commence ensuite une remarque générale sur la composition de suites simplement convergentes.

## Page 75

**Exercice 3 — remarque.** La convergence simple de $(f_n)$ vers $f$ sur un intervalle $I$ ne permet pas, à elle seule, de conclure à la convergence simple de $(f_n\circ f_n)$ vers $f\circ f$ ; l’implication est barrée sur la page.

**2, résultat sous hypothèses renforcées.** Si chaque $f_n$ est continue et si $(f_n)$ converge uniformément vers $f$, alors $f$ est continue. Sur $\mathbb R$ (ou pour des applications d’un intervalle $I$ dans lui-même), on veut montrer la convergence simple de $(f_n\circ f_n)$ vers $f\circ f$.

Pour $x$ fixé, on décompose
$$f_n(f_n(x))-f(f(x))=\underbrace{f_n(f_n(x))-f(f_n(x))}_{(1)}+\underbrace{f(f_n(x))-f(f(x))}_{(2)}.$$
On va montrer séparément que les deux termes tendent vers zéro.

## Page 76

**Exercice 3 — convergence du terme (2).** La convergence uniforme entraîne la convergence simple, donc $f_n(x)\to f(x)$ pour $x$ fixé. La fonction $f$ est continue, comme limite uniforme de fonctions continues. Par composition,
$$f(f_n(x))\to f(f(x)),$$
d’où
$$f(f_n(x))-f(f(x))\to0.$$
Cela établit le résultat (2). Pour le terme (1), la page rappelle la convergence uniforme de $f_n$ vers $f$.

## Page 77

**Exercice 3 — convergence du terme (1).** La convergence uniforme donne
$$\sup_{y\in\mathbb R}|f_n(y)-f(y)|\to0.$$
Comme $f_n(x)\in\mathbb R$,
$$|f_n(f_n(x))-f(f_n(x))|\le\sup_{y\in\mathbb R}|f_n(y)-f(y)|\to0.$$
En ajoutant les deux termes des pages 75–76,
$$f_n(f_n(x))-f(f(x))\to0.$$
Ainsi $(f_n\circ f_n)$ converge simplement vers $f\circ f$ sur $\mathbb R$.

## Page 78

**Exercice 3 — 3. La convergence des compositions n’est pas forcément uniforme.** Prenons
$$f_n(x)=x^2+\frac1n,\qquad f(x)=x^2.$$
Pour chaque $x$, $f_n(x)\to f(x)$, et
$$\|f_n-f\|_{\infty,\mathbb R}=\frac1n\to0.$$
La convergence est donc uniforme. Mais
$$f_n(f_n(x))=\left(x^2+\frac1n\right)^2+\frac1n=x^4+\frac{2x^2}{n}+\frac1{n^2}+\frac1n,$$
alors que $f(f(x))=x^4$. La différence vaut $2x^2/n+1/n^2+1/n$.

## Page 79

**Exercice 3 — 3, conclusion.** En choisissant $x_n=\sqrt n$,
$$f_n(f_n(x_n))-f(f(x_n))=2+\frac1{n^2}+\frac1n\to2.$$
Donc
$$\|f_n\circ f_n-f\circ f\|_{\infty,\mathbb R}\ge2+\frac1{n^2}+\frac1n,$$
et ce supremum ne tend pas vers zéro. Les compositions ne convergent pas uniformément vers $f\circ f$ sur $\mathbb R$. Pour chaque $n$, le supremum est même infini, car la différence contient $2x^2/n$.
