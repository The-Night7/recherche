---
source: "PREING2-S1/Series/TD2b-Correction_2022-2023_Series_P2S1_Inconnu.pdf"
pages: 64
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 64 pages manuscrites ; calculs, tableaux et annotations transcrits, corrections signalées
---

# Séries — TD2B : séries de fonctions — Corrigé manuscrit (2022–2023)

## Page 1

### TD2B — Séries de fonctions — Groupe 4

#### Exercice 1

Pour $n\in\mathbb N$, $f_n:\mathbb R\to\mathbb R$, $f_n(x)=xe^{-nx^2}$.

**1. Convergences simple et absolue de $\sum f_n$.** Rappel : $u_n\to0$ ne suffit pas à assurer la convergence de $\sum u_n$ ; si $u_n$ ne tend pas vers zéro, la série diverge. En $x=0$, tous les termes sont nuls, donc la série converge absolument et sa somme vaut zéro. Pour $x\ne0$, plusieurs méthodes sont proposées.

## Page 2

**Exercice 1 — 1, trois critères.** Pour $x\ne0$ fixé :

1. Par croissance comparée, $n^2|f_n(x)|=n^2|x|e^{-nx^2}\to0$. La comparaison à la série de Riemann d’exposant $2>1$ donne la convergence absolue.
2. D’Alembert :
$$\left|\frac{f_{n+1}(x)}{f_n(x)}\right|=e^{-x^2}<1.$$
La série $\sum|f_n(x)|$ converge.
3. Cauchy :
$$\sqrt[n]{|f_n(x)|}=|x|^{1/n}e^{-x^2}\to e^{-x^2}<1.$$
La série converge encore absolument.

## Page 3

**Exercice 1 — 1, conclusion et calcul direct.** La série $\sum_{n\ge0}f_n(x)$ converge absolument, donc converge, pour tout $x\in\mathbb R$. Il y a convergence simple et absolue sur $\mathbb R$.

**Autre méthode.** On pose
$$S_n(x)=\sum_{k=0}^nf_k(x)=\sum_{k=0}^nxe^{-kx^2}.$$
En zéro, $S_n(0)=0$. Pour $x\ne0$, la raison $e^{-x^2}$ est strictement inférieure à $1$, et on utilise la somme géométrique.

## Page 4

**Exercice 1 — somme.** Pour $x\ne0$,
$$S_n(x)=x\frac{1-(e^{-x^2})^{n+1}}{1-e^{-x^2}}\longrightarrow\frac{x}{1-e^{-x^2}}.$$
Donc
$$S(x)=\begin{cases}0,&x=0,\\\dfrac{x}{1-e^{-x^2}},&x\ne0.\end{cases}$$
Chaque $S_n$ est continue sur $\mathbb R$. En revanche, $1-e^{-x^2}\sim x^2$, donc $S(x)\sim1/x$ quand $x\to0$ ; $S$ n’est pas continue en zéro. L’annotation manuscrite illustre cette discontinuité par un développement limité.

## Page 5

**Exercice 1 — pas de convergence uniforme sur $\mathbb R$.** Une limite uniforme de fonctions continues étant continue, la discontinuité de $S$ exclut la convergence uniforme de $(S_n)$ sur $\mathbb R$.

**2. Convergence normale.** La série converge normalement sur un ensemble si la série des normes uniformes converge. Pour réfuter cette propriété, on peut montrer que $\sum\|f_n\|_\infty$ diverge.

Avec $x_n=1/\sqrt n$, $n\ge1$,
$$f_n(x_n)=\frac{e^{-1}}{\sqrt n}.$$
Comme $\sum1/\sqrt n$ diverge, la minoration $\|f_n\|_\infty\ge e^{-1}/\sqrt n$ empêche la convergence normale.

**Note de transcription :** le point appelé $x_0$ sur la page varie avec $n$. Ce n’est donc pas un point fixe où la série numérique divergerait ; il fournit une minoration de la norme de chaque terme.

## Page 6

**Exercice 1 — 2, suite.** Le calcul précédent prouve l’absence de convergence normale sur $\mathbb R$.

**b.** Soit $a>0$. Étudier la convergence normale sur
$$I_a=]-\infty,-a]\cup[a,+\infty[.$$
Deux voies sont rappelées : calculer les normes et montrer que leur série converge, ou majorer $|f_n(x)|$ par un terme $u_n$ indépendant de $x\in I_a$, avec $\sum u_n$ convergente. On utilise
$$f_n'(x)=(1-2nx^2)e^{-nx^2}.$$

**Précision d’indice :** on étudie ici la série à partir de $n=1$. Si l’on inclut $f_0(x)=x$, ce premier terme n’est pas borné sur $I_a$ ; la convergence normale au sens de la série de normes exige de l’écarter. Les résultats sur les restes et la convergence uniforme ne sont pas affectés par un nombre fini de termes.

## Page 7

**Exercice 1 — 2b, normes sur $I_a$.** Pour $n\ge1$, les points critiques sont $\pm1/\sqrt{2n}$. Le tableau montre une décroissance depuis la limite zéro jusqu’au minimum négatif, puis une croissance jusqu’au maximum positif, puis une décroissance vers zéro.

Pour $n$ assez grand, $1/\sqrt{2n}<a$. Les extrema sur $I_a$ sont alors aux points $\pm a$, et
$$\sup_{x\in I_a}|f_n(x)|=ae^{-na^2}.$$
La série de ces majorants converge, car $n^2ae^{-na^2}\to0$ (ou par série géométrique). Les premiers termes d’indices $n\ge1$ sont bornés et ne changent pas la convergence. Ainsi $\sum_{n\ge1}f_n$ converge normalement sur $I_a$, pour tout $a>0$.

La mention finale $a\ge0$ du manuscrit doit être $a>0$, puisque le cas $a=0$ est précisément exclu par la question précédente.

## Page 8

**Exercice 1 — 3.** La convergence normale entraîne la convergence uniforme. Donc la série converge uniformément sur $I_a$ pour tout $a>0$, et localement uniformément sur $\mathbb R^*$.

**Autre preuve de non-uniformité sur $\mathbb R$ : les restes.** Une série simplement convergente est uniformément convergente si et seulement si ses restes tendent uniformément vers zéro. Pour $x>0$,
$$R_n(x)=\sum_{k=n+1}^{\infty}f_k(x)\ge\sum_{k=n+1}^{2n}f_k(x).$$

## Page 9

**Exercice 1 — minoration du reste.** Pour $n+1\le k\le2n$ et $x>0$,
$$e^{-kx^2}\ge e^{-2nx^2},\qquad f_k(x)\ge xe^{-2nx^2}.$$
Il y a $n$ termes dans la somme, donc
$$R_n(x)\ge nxe^{-2nx^2}.$$
En choisissant $x_n=1/\sqrt n$,
$$R_n(x_n)\ge\sqrt n\,e^{-2}\to+\infty.$$

## Page 10

**Exercice 1 — conclusion.** $\|R_n\|_\infty\ge|R_n(x_n)|\to+\infty$, donc les restes ne convergent pas uniformément vers zéro. La série ne converge pas uniformément sur $\mathbb R$.

#### Exercice 2

Pour $n\in\mathbb N$,
$$f_n:\mathbb R\to\mathbb R,\qquad f_n(x)=\frac{(-1)^nx}{(1+x^2)^n}.$$
**1. Convergences simple et absolue.** Pour $x\ne0$ fixé,
$$n^2|f_n(x)|=n^2|x|\exp[-n\ln(1+x^2)]\to0.$$
En zéro, tous les termes sont nuls.

## Page 11

**Exercice 2 — 1, somme.** La comparaison de Riemann à l’exposant $2$ donne la convergence de $\sum|f_n(x)|$ pour chaque réel $x$. La convergence absolue entraîne la convergence simple.

Pour $x\ne0$, la somme géométrique de raison $-1/(1+x^2)$ donne
$$S(x)=x\frac1{1+1/(1+x^2)}=\frac{x(1+x^2)}{2+x^2}.$$
Cette expression vaut aussi zéro en $x=0$, comme la série. Les sommes partielles s’écrivent correctement
$$S_n(x)=x\sum_{k=0}^n\left(-\frac1{1+x^2}\right)^k.$$
**Note de transcription :** la puissance dans la somme manuscrite est notée $n$ au lieu de l’indice de sommation $k$.

**2.** On introduit $R_n=S-S_n$. En zéro, $R_n(0)=0$.

## Page 12

**Exercice 2 — 2, reste et majoration.** Pour $x\ne0$,
$$R_n(x)=\frac{(-1)^{n+1}x}{(1+x^2)^n(2+x^2)}.$$
La même formule vaut en zéro. Puisque $2+x^2\ge1+x^2$,
$$|R_n(x)|\le\frac{|x|}{(1+x^2)^{n+1}}.$$
Posons $g_n(x)=x/(1+x^2)^{n+1}$. Alors
$$g_n'(x)=\frac{1-(2n+1)x^2}{(1+x^2)^{n+2}}.$$
Le tableau présente des extrema aux points $\pm1/\sqrt{2n+1}$, avec limites nulles aux deux infinis. Par conséquent,
$$\|R_n\|_\infty\le\|g_n\|_\infty=\frac1{\sqrt{2n+1}}\left(1+\frac1{2n+1}\right)^{-(n+1)}.$$
**Note de transcription :** la dernière ligne de la page écrit une égalité pour $\|R_n\|_\infty$ ; le calcul porte sur la fonction majorante $g_n$, donc donne une inégalité.

## Page 13

**Exercice 2 — 2, convergence uniforme.**
$$\|g_n\|_\infty=\frac1{\sqrt{2n+1}}\exp\left[-(n+1)\ln\left(1+\frac1{2n+1}\right)\right].$$
L’exponentielle tend vers $e^{-1/2}$ et le premier facteur vers zéro. Donc $\|R_n\|_\infty\le\|g_n\|_\infty\to0$ : la série $\sum f_n$ converge uniformément sur $\mathbb R$.

**3. Convergence normale.** Pour $x>0$, $|f_n(x)|=h_n(x)=x/(1+x^2)^n$, et
$$h_n'(x)=\frac{1-(2n-1)x^2}{(1+x^2)^{n+1}}.$$
Par symétrie, on peut étudier $h_n$ sur toute la droite puis prendre la valeur absolue.

## Page 14

**Exercice 2 — 3, normes.** Pour $n\ge1$, le tableau donne des extrema aux points $\pm1/\sqrt{2n-1}$. Ainsi
$$\|f_n\|_\infty=\frac1{\sqrt{2n-1}}\left(1+\frac1{2n-1}\right)^{-n}\sim\frac{e^{-1/2}}{\sqrt{2n-1}}.$$
La série $\sum(2n-1)^{-1/2}$ diverge, donc, par équivalence de termes positifs, $\sum\|f_n\|_\infty$ diverge. Il n’y a pas de convergence normale sur $\mathbb R$, même en commençant à $n=1$.

## Page 15

**Exercice 2 — fin.** La série converge uniformément sur $\mathbb R$, mais pas normalement.

#### Exercice 3 — 1

Pour $n\ge1$,
$$f_n:\mathbb R_+\to\mathbb R,\qquad f_n(x)=\frac{x^n+(1-x)^n}{n^2}.$$
Rappels : si le terme général ne tend pas vers zéro en un point, la série y diverge. Sans convergence simple sur un ensemble, on ne peut avoir ni convergence uniforme, ni convergence absolue sur cet ensemble, ni convergence normale. On commence donc par étudier les puissances $x^n$ et $(1-x)^n$.

## Page 16

**Exercice 3 — 1, étude des puissances.** La page rappelle que $x^n\to0$ pour $|x|<1$, vaut $1$ en $x=1$, tend vers $+\infty$ pour $x>1$, et ne possède pas de limite finie pour $x\le-1$ (oscillation en $-1$). De même, $(1-x)^n\to0$ pour $0<x<2$, vaut $1$ en zéro, oscille en $2$ et ne possède pas de limite finie hors de cet intervalle.

**Premier cas : $x\in[0,1]$.**
$$|f_n(x)|\le\frac{|x|^n+|1-x|^n}{n^2}\le\frac2{n^2}.$$
La borne est indépendante de $x$.

## Page 17

**Exercice 3 — 1, sur $[0,1]$.** Comme $\sum2/n^2$ converge, la majoration précédente prouve la convergence normale sur $[0,1]$. Elle implique la convergence uniforme, simple et absolue.

**Pour $x>1$.**
$$f_n(x)=\frac{x^n}{n^2}\left[1+\left(\frac1x-1\right)^n\right].$$
On a $-1<1/x-1<0$, donc la puissance entre crochets tend vers zéro, tandis que $x^n/n^2\to+\infty$. Par conséquent $f_n(x)\to+\infty$.

## Page 18

**Exercice 3 — 1, conclusion hors de $[0,1]$.** Pour tout $x>1$, le terme général ne tend pas vers zéro ; la série diverge. Il n’y a donc sur $]1,+\infty[$ aucune des convergences simple, absolue, uniforme ou normale.

#### Exercice 3 — 2

Pour $n\ge1$,
$$f_n:\mathbb R\to\mathbb R,\qquad f_n(x)=\frac1{n^2+x^2}.$$
Pour tout $x\in\mathbb R$,
$$|f_n(x)|\le\frac1{n^2}.$$
La série de Riemann majorante converge : $\sum f_n$ converge normalement sur $\mathbb R$.

## Page 19

**Exercice 3 — 2, fin.** La convergence normale entraîne les convergences uniforme, simple et absolue sur $\mathbb R$.

#### Exercice 3 — 3

Pour $n\ge1$, $f_n(x)=(-1)^n/(n+x^2)$, $x\in\mathbb R$. Pour $x$ fixé,
$$|f_n(x)|=\frac1{n+x^2}\sim\frac1n.$$
La série harmonique diverge : il n’y a convergence absolue en aucun point, donc pas de convergence normale.

En revanche, pour $x$ fixé, la série est alternée et la suite positive $1/(n+x^2)$ tend vers zéro. Il reste à vérifier sa décroissance.

## Page 20

**Exercice 3 — 3, convergence simple et uniforme.**
$$n+1+x^2\ge n+x^2\implies\frac1{n+1+x^2}\le\frac1{n+x^2}.$$
Le critère des séries alternées donne la convergence pour tout $x\in\mathbb R$. Le domaine de convergence est donc $\mathbb R$.

Le reste vérifie
$$|R_n(x)|\le|f_{n+1}(x)|=\frac1{n+1+x^2}\le\frac1{n+1}.$$
Ainsi $\|R_n\|_\infty\to0$ et la série converge uniformément sur $\mathbb R$, malgré l’absence de convergence absolue et normale.

## Page 21

#### Exercice 3 — 7

Pour $n\ge1$,
$$f_n:\mathbb R_+^*\to\mathbb R,\qquad f_n(x)=\frac{\ln(1+nx)}{nx^n}.$$
**Pour $x>1$ fixé**, on a
$$n^2f_n(x)=n\exp[-n\ln x]\ln(1+nx)\to0.$$
La comparaison à la série de Riemann d’exposant $2$ donne la convergence de $\sum f_n(x)$. Les termes étant positifs, cette convergence est aussi absolue. La série converge simplement et absolument sur $]1,+\infty[$.

## Page 22

**Exercice 3 — 7, pour $0<x<1$.**
$$f_n(x)=\frac{e^{-n\ln x}\ln(1+nx)}n\to+\infty,$$
car $-\ln x>0$. Le terme général ne tend donc pas vers zéro et la série diverge.

**En $x=1$.**
$$f_n(1)=\frac{\ln(1+n)}n.$$
Ce cas est poursuivi page suivante.

## Page 23

**Exercice 3 — 7, en $x=1$.** On a $nf_n(1)=\ln(1+n)\to+\infty$. En particulier $f_n(1)\ge1/n$ à partir d’un certain rang ; la série positive diverge.

La série diverge donc pour tout $x\in]0,1]$. Sur cet ensemble, aucune convergence simple, absolue, uniforme ou normale n’est possible.

On étudie ensuite les convergences normale et uniforme sur le domaine $]1,+\infty[$ en examinant les variations de $f_n$.

## Page 24

**Exercice 3 — 7, variations sur $]1,+\infty[$.**
$$f_n'(x)=\frac{x-(1+nx)\ln(1+nx)}{(1+nx)x^{n+1}}=\frac{x[1-n\ln(1+nx)]-\ln(1+nx)}{(1+nx)x^{n+1}}.$$
Le manuscrit observe que le numérateur est négatif à partir d’un certain rang, donc que $f_n$ est décroissante sur $]1,+\infty[$ pour ces indices.

On peut préciser que c’est vrai pour tout $n\ge1$ : l’inégalité $\ln(1+t)>t/(1+t)$, $t>0$, donne $(1+nx)\ln(1+nx)>nx\ge x$. Le dénominateur est positif, donc $f_n'(x)<0$.

## Page 25

**Exercice 3 — 7, absence de convergence normale.** Le tableau montre une décroissance de la limite $\ln(1+n)/n$ en $1^+$ vers zéro en $+\infty$. Donc
$$\sup_{x>1}|f_n(x)|=\frac{\ln(1+n)}n.$$
La série de ces normes diverge : pas de convergence normale sur $]1,+\infty[$.

**Convergence uniforme ?** Pour $x>1$, les termes sont positifs, donc
$$R_n(x)=\sum_{k=n+1}^{\infty}f_k(x)\ge\sum_{k=n+1}^{2n}f_k(x).$$

## Page 26

**Exercice 3 — 7, minoration du reste.** Pour $n+1\le k\le2n$ et $x>1$,
$$kx^k\le2nx^{2n},\qquad\ln(1+kx)\ge\ln(1+(n+1)x).$$
Donc
$$f_k(x)\ge\frac{\ln(1+(n+1)x)}{2nx^{2n}}.$$
En sommant les $n$ termes,
$$R_n(x)\ge\frac{\ln(1+(n+1)x)}{2x^{2n}}.$$

## Page 27

**Exercice 3 — 7, choix d’un point variable.** Notons
$$h_n(x)=\frac{\ln(1+(n+1)x)}{2x^{2n}},\qquad x_n=1+\frac1{n+1}.$$
Alors
$$h_n(x_n)=\frac{\ln(n+3)}{2(1+1/(n+1))^{2n}}\sim\frac{e^{-2}}2\ln(n+3)\to+\infty.$$
Comme $\|R_n\|_\infty\ge R_n(x_n)\ge h_n(x_n)$, les restes ne tendent pas uniformément vers zéro.

## Page 28

**Exercice 3 — 7, conclusion.** La série ne converge pas uniformément sur $]1,+\infty[$.

#### Exercice 4

Soit $a>0$. Pour $n\in\mathbb N$,
$$f_n:\mathbb R_+\to\mathbb R,\qquad f_n(x)=x^ae^{-nx}.$$
**1. Convergence simple.** En zéro, tous les termes sont nuls. Pour $x>0$ fixé,
$$n^2f_n(x)=n^2x^ae^{-nx}\to0.$$
La comparaison à une série de Riemann permet de conclure.

## Page 29

**Exercice 4 — 1, conclusion.** La série converge pour tout $x\ge0$, donc son domaine de convergence est $\mathbb R_+$. Les termes étant positifs, la convergence est aussi absolue en tout point.

**2. Calcul de la somme.** Pour $x$ fixé,
$$\sum_{n=0}^{\infty}f_n(x)=\sum_{n=0}^{\infty}x^ae^{-nx}.$$
On reconnaît une série géométrique lorsque $x>0$.

## Page 30

**Exercice 4 — 2, somme géométrique.**
$$\sum_{n=0}^{\infty}f_n(x)=x^a\sum_{n=0}^{\infty}(e^{-x})^n.$$
En zéro, la somme des $f_n(0)$ vaut zéro. Pour $x>0$, $0<e^{-x}<1$, donc
$$\sum_{n=0}^{\infty}f_n(x)=\frac{x^a}{1-e^{-x}}.$$

## Page 31

**Exercice 4 — somme et question 3.**
$$S(x)=\begin{cases}0,&x=0,\\\dfrac{x^a}{1-e^{-x}},&x>0.\end{cases}$$
**3.** Montrer que la série converge normalement sur $\mathbb R_+$ si et seulement si $a>1$. On étudie les variations de $f_n$.

**Précision d’indice :** cette affirmation s’applique à $\sum_{n\ge1}f_n$. Pour la série commençant à zéro, $f_0(x)=x^a$ n’est pas bornée sur $\mathbb R_+$ ; sa norme uniforme est infinie. Le manuscrit passe de $n\ge0$ à $n\ge1$ dans le calcul de convergence normale. La somme de la série à partir de $1$ est $S(x)-x^a$ ; l’ajout du terme $f_0$ ne change pas la convergence uniforme des sommes partielles.

## Page 32

**Exercice 4 — 3, maximum.** Pour $n\ge1$ et $x>0$,
$$f_n'(x)=(a-nx)x^{a-1}e^{-nx}.$$
La fonction part de zéro, croît jusqu’à $x=a/n$, puis décroît vers zéro. Son maximum est
$$\|f_n\|_\infty=f_n(a/n)=\frac{a^a}{n^a}e^{-a}=a^ae^{-a}n^{-a}.$$

## Page 33

**Exercice 4 — 3, critère exact.** Les affirmations suivantes sont équivalentes :

- $\sum_{n\ge1}f_n$ converge normalement sur $\mathbb R_+$ ;
- $\sum_{n\ge1}\|f_n\|_\infty$ converge ;
- $\sum_{n\ge1}a^ae^{-a}n^{-a}$ converge ;
- la série de Riemann $\sum_{n\ge1}n^{-a}$ converge ;
- $a>1$.

Le facteur $a^ae^{-a}$ est une constante strictement positive.

## Page 34

**Exercice 4 — 4, convergence uniforme lorsque $a\le1$.** On examine la continuité de la somme en zéro. Comme $1-e^{-x}\sim x$ quand $x\to0^+$,
$$S(x)\sim x^{a-1}.$$
Donc
$$\lim_{x\to0^+}S(x)=\begin{cases}0,&a>1,\\1,&a=1,\\+\infty,&0<a<1.\end{cases}$$
La valeur $S(0)$ vaut zéro. La somme est continue en zéro seulement si $a>1$.

## Page 35

**Exercice 4 — 4, conclusion.** Pour $0<a\le1$, les sommes partielles sont continues en zéro et leur limite simple $S$ ne l’est pas. La convergence ne peut donc pas être uniforme sur $\mathbb R_+$.

Pour $a>1$, la convergence normale de la série à partir de l’indice $1$ implique la convergence uniforme. L’ajout éventuel de $f_0$ ne change pas ce résultat. Ainsi la convergence uniforme sur $\mathbb R_+$ a lieu exactement pour $a>1$.

## Page 36

**Exercice 4 — 5.** Soit $A>0$. Montrer la convergence uniforme sur $[A,+\infty[$. Pour $n$ assez grand, $a/n<A$ ; le tableau des variations montre alors que $f_n$ décroît sur ce demi-axe, et
$$\sup_{x\ge A}|f_n(x)|=f_n(A)=A^ae^{-nA}.$$
La série de ces majorants converge ; par exemple $n^2A^ae^{-nA}\to0$. La conclusion se poursuit page suivante.

## Page 37

**Exercice 4 — 5, conclusion.** La série $\sum_{n\ge1}f_n$ converge normalement, donc uniformément, sur chaque $[A,+\infty[$, $A>0$. Elle converge donc localement uniformément sur $\mathbb R_+^*$.

#### Exercice 3 — 5, reprise

Pour $n\ge1$, $f_n:\mathbb R\to\mathbb R$, $f_n(x)=1/n^x$. Pour $x$ fixé,
$$\sum_{n\ge1}f_n(x)=\sum_{n\ge1}\left(\frac1n\right)^x.$$
C’est une série de Riemann.

## Page 38

**Exercice 3 — 5, domaine et convergence absolue.** La série de Riemann converge si et seulement si $x>1$. Le domaine de convergence est donc $D_c=]1,+\infty[$. Les termes sont positifs : la convergence y est aussi absolue.

Pour étudier les convergences uniforme et normale sur ce domaine, on écrit
$$f_n(x)=e^{-x\ln n}.$$

## Page 39

**Exercice 3 — 5, absence de convergence normale.** Pour $n>1$,
$$f_n'(x)=-(\ln n)e^{-x\ln n}<0.$$
Le tableau va de la limite $1/n$ en $1^+$ à zéro en $+\infty$. Pour $n=1$, $f_1=1$ est constante. Dans tous les cas,
$$\sup_{x>1}|f_n(x)|=\frac1n.$$
La série de ces normes est harmonique et diverge. Il n’y a pas de convergence normale sur $]1,+\infty[$.

## Page 40

**Exercice 3 — 5, essai de minoration du reste.** Pour $x>1$,
$$R_n(x)=\sum_{k=n+1}^{\infty}k^{-x}\ge\sum_{k=n+1}^{2n}k^{-x}.$$
La page compare ensuite $\ln k$ à $\ln(n+1)$ et $\ln(2n)$, puis propose la minoration $R_n(x)\ge n(n+1)^{-x}$.

**Erreur de sens signalée :** comme $k\ge n+1$, on a $k^{-x}\le(n+1)^{-x}$, et cette expression ne fournit pas la minoration écrite. La minoration correcte issue de cette tranche serait
$$R_n(x)\ge n(2n)^{-x}.$$
Le manuscrit abandonne cette voie page suivante et passe à une comparaison intégrale.

## Page 41

**Exercice 3 — 5, comparaison intégrale.** La page signale que l’essai précédent ne donne pas le résultat recherché avec un point $x_0>1$ fixé, puis change de méthode.

Pour $x>1$, l’application $t\mapsto t^{-x}$ est décroissante sur $[1,+\infty[$. Pour $k\ge1$ et $t\in[k,k+1]$,
$$\frac1{(k+1)^x}\le\frac1{t^x}\le\frac1{k^x}.$$
En intégrant sur cet intervalle de longueur $1$,
$$\frac1{(k+1)^x}\le\int_k^{k+1}t^{-x}\,dt\le\frac1{k^x}.$$

**Précision :** pour réfuter une convergence uniforme, un point dépendant de $n$ est autorisé. La suite de la correction utilise effectivement ce procédé.

## Page 42

**Exercice 3 — 5, première somme d’inégalités.** En sommant la majoration intégrale de la page précédente pour $k=2,\ldots,N$,
$$\int_2^{N+1}t^{-x}\,dt\le\sum_{k=2}^N\frac1{k^x}.$$
En la sommant pour $k=N+1,\ldots,N'$, avec $N'>N$,
$$\int_{N+1}^{N'+1}t^{-x}\,dt\le\sum_{k=N+1}^{N'}\frac1{k^x}.$$

## Page 43

**Exercice 3 — 5, seconde somme d’inégalités.** Pour $k\ge2$ et $t\in[k-1,k]$,
$$\frac1{k^x}\le\frac1{t^x}\le\frac1{(k-1)^x},$$
donc $k^{-x}\le\int_{k-1}^kt^{-x}\,dt$. En sommant,
$$\sum_{k=2}^N\frac1{k^x}\le\int_1^Nt^{-x}\,dt,$$
et
$$\sum_{k=N+1}^{N'}\frac1{k^x}\le\int_N^{N'}t^{-x}\,dt.$$
On obtient notamment
$$\int_2^{N+1}t^{-x}\,dt\le\sum_{k=2}^N\frac1{k^x}\le\int_1^Nt^{-x}\,dt.$$

## Page 44

**Exercice 3 — 5, encadrement d’un reste fini.** Notons
$$R_{N,N'}(x)=\sum_{k=N+1}^{N'}k^{-x},\qquad R_N(x)=\lim_{N'\to\infty}R_{N,N'}(x).$$
Les inégalités précédentes donnent
$$\int_{N+1}^{N'+1}t^{-x}\,dt\le R_{N,N'}(x)\le\int_N^{N'}t^{-x}\,dt.$$
Puisque $x>1$, une primitive est $t^{1-x}/(1-x)$. Ainsi la borne inférieure vaut
$$\frac{(N'+1)^{1-x}-(N+1)^{1-x}}{1-x},$$
et la borne supérieure vaut $((N')^{1-x}-N^{1-x})/(1-x)$.

## Page 45

**Exercice 3 — 5, reste infini.** En faisant tendre $N'$ vers l’infini,
$$\frac1{(x-1)(N+1)^{x-1}}\le R_N(x)\le\frac1{(x-1)N^{x-1}}.$$
Notons $g_N$ la borne inférieure et $h_N$ la borne supérieure. Une borne uniforme de $h_N$ tendant vers zéro prouverait la convergence uniforme ; une suite de points où $g_N$ ne tend pas vers zéro la réfute.

Pour $n\ge2$, choisissons
$$x_n=1+\frac1{\ln n}.$$
Alors
$$g_n(x_n)=\ln n\,(n+1)^{-1/\ln n}.$$

## Page 46

**Exercice 3 — 5, conclusion.**
$$g_n(x_n)=\ln n\exp\left[-\frac{\ln(n+1)}{\ln n}\right]\sim e^{-1}\ln n\to+\infty.$$
Donc $\|R_n\|_\infty\ge g_n(x_n)$ ne tend pas vers zéro : la série n’est pas uniformément convergente sur $]1,+\infty[$.

#### Exercice 3 — 6

Pour $n\ge1$, $f_n(x)=(-1)^n/n^x$, $x\in\mathbb R$. Si $x\le0$, le terme général ne tend pas vers zéro, donc la série diverge. Les sommes notées à partir de $0$ dans certaines lignes du manuscrit doivent commencer à $1$, puisque $n^{-x}$ n’est pas défini uniformément en $x$ pour $n=0$.

## Page 47

**Exercice 3 — 6, domaine de convergence.** Pour $x>0$, la suite $n^{-x}$ est positive, décroissante et tend vers zéro. Le critère des séries alternées donne la convergence de $\sum_{n\ge1}(-1)^nn^{-x}$. Ainsi $D_c=]0,+\infty[$.

**Convergence absolue.** Comme $|f_n(x)|=n^{-x}$, la série des valeurs absolues converge si et seulement si $x>1$. Sur $]0,1]$, la série converge simplement mais pas absolument.

## Page 48

**Exercice 3 — 6, convergences uniforme et normale.** L’absence de convergence absolue sur $]0,1]$ exclut la convergence normale sur cet ensemble.

Pour chaque $n\ge1$,
$$\sup_{x>0}|f_n(x)|=\sup_{x>0}n^{-x}=1.$$
Le terme général ne tend donc pas uniformément vers zéro sur $]0,+\infty[$, condition nécessaire à la convergence uniforme de la série. Celle-ci n’y converge pas uniformément.

**Remarque.** Pour $\alpha>1$,
$$\sup_{x\ge\alpha}|f_n(x)|=n^{-\alpha},$$
et la série de Riemann majorante converge : il y a convergence normale et uniforme sur $[\alpha,+\infty[$. Cela établit déjà la convergence localement uniforme sur $]1,+\infty[$.

## Page 49

#### Exercice 6

Pour $n\ge0$ et $x\in\mathbb R$,
$$f_n(x)=\frac{(-1)^ne^{-nx^2}}{(n+1)^3}.$$
Pour $x$ fixé,
$$n^2|f_n(x)|=\frac{n^2}{(n+1)^3}e^{-nx^2}\to0.$$
La comparaison de Riemann donne la convergence absolue pour tout $x\in\mathbb R$, donc la convergence simple. Le domaine de convergence est $\mathbb R$. On note
$$S(x)=\sum_{n=0}^{\infty}f_n(x).$$
On veut montrer que $S$ est continue sur $\mathbb R$.

## Page 50

**Exercice 6 — continuité.** Pour tout réel $x$,
$$|f_n(x)|\le\frac1{(n+1)^3}.$$
La série majorante converge : la série de fonctions converge normalement, donc uniformément, sur $\mathbb R$. Chaque $f_n$ étant continue, sa somme $S$ est continue sur $\mathbb R$.

#### Exercice 7

Pour $n\ge0$ et $x\in\mathbb R$,
$$f_n(x)=e^{-n}\sin(n^2x).$$

## Page 51

**Exercice 7 — convergence et dérivées.** Pour tout $x\in\mathbb R$,
$$|f_n(x)|\le e^{-n}.$$
La série géométrique $\sum e^{-n}$ converge ; la série de fonctions converge normalement sur $\mathbb R$. Sa somme $S=\sum f_n$ est donc bien définie.

Pour montrer que $S$ est dérivable, on étudie la série des dérivées :
$$f_n'(x)=n^2e^{-n}\cos(n^2x),\qquad|f_n'(x)|\le n^2e^{-n}=u_n.$$
Comme $n^2u_n=n^4e^{-n}\to0$, la série $\sum u_n$ converge par comparaison à $\sum1/n^2$.

## Page 52

**Exercice 7 — dérivation terme à terme.** La série des dérivées converge normalement, donc uniformément, sur $\mathbb R$. On réunit les hypothèses : chaque $f_n$ est de classe $C^1$, la série $\sum f_n$ converge simplement et la série $\sum f_n'$ converge uniformément. Le théorème de dérivation donne $S\in C^1(\mathbb R)$ et
$$S'(x)=\sum_{n=0}^{\infty}n^2e^{-n}\cos(n^2x).$$
La convergence uniforme de la série initiale avait déjà été établie par convergence normale.

## Page 53

#### Exercice 5

Pour $x>0$ et $n\ge0$,
$$f_n(x)=\frac{(-1)^n}{n!(n+x)}.$$
Pour $x$ fixé, les valeurs absolues sont décroissantes et tendent vers zéro. Le critère des séries alternées donne la convergence ; on pose
$$S(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!(n+x)}.$$
**1.** Montrer que $S$ est de classe $C^1$ sur $\mathbb R_+^*$. Les dérivées sont
$$f_n'(x)=-\frac{(-1)^n}{n!(n+x)^2}.$$
Pour $n\ge1$ et $x>0$, $|f_n'(x)|\le1/n^2$.

**Note d’indice :** cette borne ne concerne pas $n=0$, pour lequel $f_0'(x)=-1/x^2$. On traite ce terme séparément.

## Page 54

**Exercice 5 — 1, régularité.** La série $\sum_{n\ge1}f_n'$ converge normalement sur $\mathbb R_+^*$, grâce à la borne $1/n^2$. Chaque $f_n$ est de classe $C^1$ sur cet intervalle, et la série initiale converge simplement. Sur chaque segment compact inclus dans $\mathbb R_+^*$, on peut appliquer le théorème de dérivation, y compris au terme $n=0$ traité séparément. Ainsi
$$S\in C^1(\mathbb R_+^*),\qquad S'(x)=-\sum_{n=0}^{\infty}\frac{(-1)^n}{n!(n+x)^2}.$$

**Notes sur la source :** plusieurs lignes écrivent $\mathbb R$ au lieu de $\mathbb R_+^*$ ; les fonctions ont des pôles en dehors du domaine positif. Le manuscrit applique aussi la borne $1/n^2$ à une somme partant de zéro, ce qui doit être corrigé comme ci-dessus.

**2.** On définit $g(x)=xS(x)-S(x+1)$, $x>0$.

## Page 55

**Exercice 5 — 2, dérivée de $g$.**
$$g'(x)=S(x)+xS'(x)-S'(x+1).$$
En substituant les séries,
$$g'(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\left(\frac1{n+x}-\frac{x}{(n+x)^2}+\frac1{(n+x+1)^2}\right).$$
Comme $1/(n+x)-x/(n+x)^2=n/(n+x)^2$,
$$g'(x)=\sum_{n=1}^{\infty}\frac{(-1)^n}{(n-1)!(n+x)^2}+\sum_{n=0}^{\infty}\frac{(-1)^n}{n!(n+x+1)^2}.$$
En posant $k=n-1$ dans la première somme,
$$g'(x)=\sum_{k=0}^{\infty}\frac{(-1)^{k+1}}{k!(k+x+1)^2}+\sum_{k=0}^{\infty}\frac{(-1)^k}{k!(k+x+1)^2}.$$

## Page 56

**Exercice 5 — 2, identité fonctionnelle.** Les deux séries se compensent : $g'(x)=0$. Donc $g$ est constante sur $\mathbb R_+^*$ et
$$xS(x)-S(x+1)=g(1)=S(1)-S(2).$$
**3a. Équivalent en zéro.** On réécrit
$$xS(x)=S(x+1)+S(1)-S(2).$$
Par continuité de $S$ en $1$, le membre de droite tend vers $2S(1)-S(2)$. Le manuscrit en déduit
$$S(x)\sim_{x\to0^+}\frac{2S(1)-S(2)}x.$$

**Justification du coefficient non nul :** le terme d’indice zéro de $S$ vaut $1/x$, et la somme des autres termes est bornée près de zéro par $\sum_{n\ge1}1/(n!n)$. Ainsi $xS(x)\to1$, donc $2S(1)-S(2)=1$, ce qui valide l’équivalent.

## Page 57

**Exercice 5 — 3b, équivalent à l’infini.** Le manuscrit part de
$$xS(x)-S(x+1)=C,\qquad C=S(1)-S(2),$$
puis écrit $S(x)[x-S(x+1)/S(x)]=C$ et annonce
$$S(x)\sim_{x\to+\infty}\frac C{x-1}.$$
La fin du calcul du quotient contient des simplifications insuffisamment justifiées : le terme $C/[S(x)(x-1)]$ y est notamment traité comme tendant vers zéro, ce qui n’est pas établi et serait incompatible avec l’équivalent annoncé.

**Vérification de la conclusion.** À partir de la série absolument convergente,
$$xS(x)=\sum_{n=0}^{\infty}\frac{(-1)^n}{n!}\frac{x}{n+x}.$$
Chaque facteur $x/(n+x)$ tend vers $1$ et est compris entre $0$ et $1$ ; la série majorante $\sum1/n!$ converge. Donc $xS(x)\to e^{-1}$, soit $S(x)\sim e^{-1}/x$. D’autre part, la même décomposition algébrique donne exactement $xS(x)-S(x+1)=\sum(-1)^n/n!=e^{-1}$, donc $C=e^{-1}$. L’équivalent annoncé $C/(x-1)$ est ainsi correct, puisque $x-1\sim x$.

## Page 58

#### Exercice 8

Pour $n\ge1$ et $x>1$, $f_n(x)=n^{-x}$.

**1.** Pour tout $x>1$, la série de Riemann converge. On définit
$$S(x)=\sum_{n=1}^{\infty}n^{-x}.$$
**2.** On écrit $f_n(x)=e^{-x\ln n}$. Pour $n>1$, $f_n'(x)=-(\ln n)e^{-x\ln n}<0$ : la fonction est décroissante. Pour $n=1$, elle est constante égale à $1$. Pour tout $\alpha>1$,
$$\sup_{x\ge\alpha}|f_n(x)|=n^{-\alpha}.$$

## Page 59

**Exercice 8 — 2, convergence locale et dérivées.** La série $\sum n^{-\alpha}$ converge pour $\alpha>1$, donc $\sum f_n$ converge normalement et uniformément sur chaque $[\alpha,+\infty[$. Elle converge localement uniformément sur $]1,+\infty[$.

Pour montrer que $S$ est décroissante, on veut justifier
$$S'(x)=\sum_{n=1}^{\infty}f_n'(x).$$
On étudie donc la convergence locale uniforme de la série des dérivées. Pour $n>1$,
$$f_n'(x)=-(\ln n)n^{-x},\qquad f_n''(x)=(\ln n)^2n^{-x}>0.$$
Le tableau de $f_n'$ montre une croissance de ses valeurs négatives vers zéro ; sa valeur absolue décroît.

## Page 60

**Exercice 8 — 2, majoration des dérivées.** Pour tout $\alpha>1$,
$$\sup_{x\ge\alpha}|f_n'(x)|=\frac{\ln n}{n^\alpha}.$$
La série $\sum_{n\ge1}(\ln n)n^{-\alpha}$ converge (série de Bertrand, exposant $\alpha>1$, exposant logarithmique $-1$ dans la convention du cours). Donc la série des dérivées converge normalement sur $[\alpha,+\infty[$.

## Page 61

**Exercice 8 — 2, dérivation.** Pour tout $\alpha>1$, la série des dérivées converge normalement, donc uniformément, sur $[\alpha,+\infty[$. Elle converge donc localement uniformément sur $]1,+\infty[$.

Chaque $f_n$ est de classe $C^1$ sur cet intervalle, la série $\sum f_n$ y converge simplement et la série $\sum f_n'$ y converge localement uniformément. Le théorème de dérivation donne
$$S\in C^1(]1,+\infty[),\qquad S'(x)=\sum_{n=1}^{\infty}f_n'(x).$$

## Page 62

**Exercice 8 — 2, décroissance.**
$$S'(x)=-\sum_{n=1}^{\infty}\frac{\ln n}{n^x}<0\qquad(x>1),$$
car les termes sont positifs à partir de $n=2$. Donc $S$ est strictement décroissante.

**3. Comparaison intégrale.** La page renvoie à un calcul précédent (renvoi manuscrit « page 43 »). On dispose de
$$\int_2^{N+1}t^{-x}\,dt\le\sum_{k=2}^Nk^{-x}\le\int_1^Nt^{-x}\,dt.$$
En calculant les primitives et en faisant tendre $N$ vers l’infini,
$$\frac{2^{1-x}}{x-1}\le S(x)-1\le\frac1{x-1}.$$
Donc
$$1+\frac1{(x-1)2^{x-1}}\le S(x)\le1+\frac1{x-1}.$$

## Page 63

**Exercice 8 — 4, limites.**

**a. En $+\infty$.** Les deux bornes
$$1+\frac1{(x-1)2^{x-1}}\quad\text{et}\quad1+\frac1{x-1}$$
tendent vers $1$. Par encadrement, $\lim_{x\to+\infty}S(x)=1$.

**b. En $1^+$.** La minoration
$$S(x)\ge1+\frac1{(x-1)2^{x-1}}$$
tend vers $+\infty$ quand $x\to1^+$. Donc $\lim_{x\to1^+}S(x)=+\infty$.

La page rappelle enfin que $S$ est de classe $C^1$, donc continue et dérivable sur $]1,+\infty[$.

## Page 64

**Exercice 8 — représentation finale.** On rappelle
$$S'(x)=-\sum_{n=1}^{\infty}\frac{\ln n}{n^x},\qquad x>1.$$
Le graphique représente une courbe strictement décroissante, située au-dessus de la droite horizontale $y=1$. Elle tend vers $+\infty$ au voisinage droit de l’asymptote verticale $x=1$, puis se rapproche de l’asymptote horizontale $y=1$ quand $x\to+\infty$. Les deux asymptotes sont tracées en couleur.
