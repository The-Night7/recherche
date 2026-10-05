---
source: "PREING2-S1/Series-DS/DS3-2023-2024-Ratrapage-Correction_Series-DS_P2S1__RayaneM.pdf"
pages: 8
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des huit pages ; normes uniformes, séries alternées, somme complexe et quotients factoriels vérifiés ; coquilles du manuscrit signalées
---

# Séries — DS 3, rattrapage 2023–2024 — corrigé manuscrit

> Le support est constitué de huit pages photographiées, parfois assemblées et rognées. Les calculs lisibles sont transcrits ; les erreurs d’indice, de signe et de justification sont signalées. Les énoncés complets ne figurent pas dans ce corrigé.

## Page 1 — Exercice 1 : convergence de $f_n(x)=-x^n\ln x$

### a. Convergence simple sur $]0,1]$

Pour $x=1$, $f_n(x)=0$. Pour $0<x<1$,

$$f_n(x)=-x^n\ln x\longrightarrow0,$$

car $x^n\to0$. Ainsi $f_n$ converge simplement vers $f=0$ sur $]0,1]$.

### b. Convergence uniforme

On pose

$$g_n(x)=|f_n(x)-f(x)|=-x^n\ln x.$$

La dérivée vaut

$$g_n'(x)=-nx^{n-1}\ln x-x^{n-1}
=nx^{n-1}\left(\ln\frac1x-\frac1n\right).$$

Le tableau de variations donne une croissance sur $]0,e^{-1/n}]$, puis une décroissance sur $[e^{-1/n},1]$. Le maximum vaut

$$\sup_{x\in]0,1]}g_n(x)=g_n(e^{-1/n})
=-e^{-1}\ln(e^{-1/n})=\frac{e^{-1}}n\longrightarrow0.$$

> Dans la dernière ligne manuscrite, le signe moins devant le logarithme est omis ; la valeur positive $e^{-1}/n$ qui suit est correcte.

## Page 2 — Dérivées et début de l’exercice 2

Ainsi $f_n$ converge uniformément vers $0$ sur $]0,1]$.

### Étude de la suite des dérivées

Cette partie est de nouveau numérotée « b) » dans la source. On y réutilise le nom $g_n$ pour

$$g_n(x)=f_n'(x)=-x^{n-1}(n\ln x+1).$$

Si $x=1$, $g_n(1)=-1$. Si $0<x<1$,

$$g_n(x)=nx^{n-1}\left(\ln\frac1x-\frac1n\right)\longrightarrow0$$

par croissance comparée de l’exponentielle et de $n$. Donc

$$g_n\longrightarrow g\text{ simplement},\qquad
g(x)=\begin{cases}0,&0<x<1,\\-1,&x=1.\end{cases}$$

Chaque $g_n$ est continue en $1$, mais $g$ ne l’est pas. La convergence n’est pas uniforme sur $]0,1]$.

### Exercice 2 — Série de fonctions

Les calculs utilisent

$$f_n(x)=\frac{x^3}{1+n^\alpha x^4},\qquad x\in\mathbb R.$$

1. Pour $x\ne0$ fixé :

- Si $\alpha<0$, $f_n(x)\to x^3\ne0$, donc la série diverge.
- Si $\alpha=0$, $f_n(x)=x^3/(1+x^4)\ne0$, donc la série diverge.

> Au point $x=0$, tous les termes sont nuls, quelle que soit $\alpha$ ; cette exception n’est pas mentionnée dans ces deux lignes de la source.

## Page 3 — Convergence simple et étude de la norme

Si $\alpha>0$, pour $x\ne0$ fixé,

$$f_n(x)\sim\frac{x^3}{n^\alpha x^4}=\frac1{x n^\alpha}.$$

- Si $\alpha>1$, la série converge, par comparaison à une série de Riemann.
- Si $0<\alpha\leq1$, elle diverge.

La série converge donc simplement sur tout $\mathbb R$ si et seulement si $\alpha>1$.

### 2 a. Convergence normale

On pose

$$g_n(x)=|f_n(x)|=\frac{|x|^3}{1+n^\alpha x^4}.$$

La fonction est paire ; on se restreint à $x\geq0$. Pour $x>0$,

$$
g_n'(x)=\frac{3x^2(1+n^\alpha x^4)-4n^\alpha x^6}{(1+n^\alpha x^4)^2}
=\frac{3x^2-n^\alpha x^6}{(1+n^\alpha x^4)^2}
=x^2\frac{3-n^\alpha x^4}{(1+n^\alpha x^4)^2}.
$$

Le tableau donne une croissance jusqu’à

$$x_n=\sqrt[4]{\frac3{n^\alpha}},$$

puis une décroissance vers zéro.

## Page 4 — Convergence normale et continuité de la somme

$$\|f_n\|_\infty=g_n(x_n)
=\frac{(3/n^\alpha)^{3/4}}{1+3}
=\frac{3^{3/4}}4\frac1{n^{3\alpha/4}}.$$

Par le critère des séries de Riemann,

$$\sum\|f_n\|_\infty\text{ converge}
\Longleftrightarrow\frac{3\alpha}4>1
\Longleftrightarrow\alpha>\frac43.$$

On note $\alpha_0=4/3$. La série converge normalement sur $\mathbb R$ si et seulement si $\alpha>\alpha_0$.

### 2 b. Continuité pour $\alpha>\alpha_0$

La convergence normale entraîne la convergence uniforme. Chaque $f_n$ est continue sur $\mathbb R$, puisque $1+n^\alpha x^4>0$. La somme $S_\alpha$ est donc continue sur $\mathbb R$.

> Le manuscrit invoque ici le « théorème d’interversion somme-intégrale ». Pour cette conclusion de continuité, il s’agit du théorème de continuité d’une somme uniformément convergente de fonctions continues.

### 3 a. Convergence loin de zéro

Soient $\alpha>1$ et $a>0$. Sur $D_a=]-\infty,-a]\cup[a,+\infty[$,

$$|f_n(x)|=\frac{|x|^3}{1+n^\alpha x^4}
\leq\frac{|x|^3}{n^\alpha|x|^4}
=\frac1{|x|n^\alpha}\leq\frac1{a n^\alpha}.$$

La majorante est sommable ; la série converge normalement sur $D_a$.

### 3 b

Comme cela vaut pour tout $a>0$, la série converge normalement localement sur $\mathbb R^*$, pour $\alpha>1$.

## Page 5 — Série alternée associée

La continuité de chaque $f_n$ et la convergence uniforme locale donnent la continuité de $S_\alpha$ sur $\mathbb R^*$ pour $\alpha>1$.

> La source emploie de nouveau le nom « interversion somme-intégrale » ; le résultat utilisé est celui sur la continuité de la somme.

### 4 a. Convergence simple alternée

On considère $g_n(x)=(-1)^nf_n(x)$, avec $\alpha>0$. Pour $x$ fixé, on pose

$$a_n=\frac{|x|^3}{1+n^\alpha x^4}.$$

$$
a_{n+1}-a_n
=|x|^3\left[\frac1{1+(n+1)^\alpha x^4}-\frac1{1+n^\alpha x^4}\right]
=\frac{|x|^7[n^\alpha-(n+1)^\alpha]}
{[1+(n+1)^\alpha x^4][1+n^\alpha x^4]}\leq0.
$$

La suite $(a_n)$ est décroissante et tend vers zéro : elle est nulle si $x=0$ et, si $x\ne0$, $a_n\sim1/(|x|n^\alpha)$. Le critère spécial des séries alternées donne la convergence de

$$\sum_{n\geq1}(-1)^n\frac{|x|^3}{1+n^\alpha x^4},$$

puis de

$$\sum_{n\geq1}(-1)^n\frac{x^3}{1+n^\alpha x^4}.$$

### 4 b. Reste

Le critère donne, pour $x\ne0$,

$$|R_n(x)|\leq a_{n+1}
=\frac{|x|^3}{1+(n+1)^\alpha x^4}
\leq\frac1{|x|(n+1)^\alpha}.$$

La page s’arrête à cette majoration.

## Page 6 — Exercice 3 : série trigonométrique

Les calculs portent sur

$$f_n(x)=\frac{\sin(nx)}{2^n},\qquad n\geq0,\quad x\in\mathbb R.$$

### 1. Convergence normale

$$|f_n(x)|\leq\left(\frac12\right)^n.$$

La majorante géométrique est sommable, donc $\sum f_n$ converge normalement sur $\mathbb R$.

### 2. Dérivation terme à terme

Chaque $f_n$ est de classe $C^1$. Au point $x_0=0$, la série converge, car $f_n(0)=0$.

$$|f_n'(x)|=\frac n{2^n}|\cos(nx)|\leq\frac n{2^n}.$$

Par croissance comparée, $n^2(n/2^n)\to0$, donc $\sum n/2^n$ converge. La série des dérivées converge normalement, donc uniformément, sur $\mathbb R$. Le théorème de dérivation d’une série de fonctions donne $S\in C^1(\mathbb R)$.

### 3. Calcul de la somme

Pour $x\in\mathbb R$,

$$S_n(x)=\sum_{k=0}^n\frac{\sin(kx)}{2^k}
=\sum_{k=0}^n\frac{\operatorname{Im}(e^{ikx})}{2^k}.$$

## Page 7 — Somme géométrique complexe

$$
S_n(x)=\operatorname{Im}\left[\sum_{k=0}^n\left(\frac{e^{ix}}2\right)^k\right]
=\operatorname{Im}\left[\frac{1-(e^{ix}/2)^{n+1}}{1-e^{ix}/2}\right]
=\frac1{2^n}\operatorname{Im}\left[\frac{2^{n+1}-e^{i(n+1)x}}{2-e^{ix}}\right].
$$

On développe les exponentielles et on multiplie par le conjugué du dénominateur :

$$
S_n(x)=\frac1{2^n}\operatorname{Im}\left[
\frac{[2^{n+1}-\cos((n+1)x)-i\sin((n+1)x)]
[2-\cos x+i\sin x]}
{(2-\cos x)^2+\sin^2x}\right].
$$

Le dénominateur vaut $5-4\cos x$. Les termes imaginaires du développement sont

$$
-2\sin((n+1)x)+\cos x\sin((n+1)x)
+2^{n+1}\sin x-\sin x\cos((n+1)x).
$$

Donc

$$
S_n(x)=\frac{-2\sin((n+1)x)+\cos x\sin((n+1)x)
+2^{n+1}\sin x-\sin x\cos((n+1)x)}{2^n(5-4\cos x)}.
$$

En passant à la limite,

$$\boxed{S(x)=\frac{2\sin x}{5-4\cos x}}.$$

> Une ligne intermédiaire de la photographie laisse un signe de sommation devant la formule de la somme géométrique déjà calculée. Ce signe est superflu ; l’expression est la partie imaginaire du quotient unique ci-dessus.

## Page 8 — Exercice 4 : rayons de convergence

### 1. Coefficients factoriels

$$a_n=\frac{n!}{2^{2n}\sqrt{(2n)!}}.$$

Alors

$$
\left|\frac{a_{n+1}}{a_n}\right|
=\frac{n+1}{2^2\sqrt{(2n+1)(2n+2)}}
=\frac18\frac{1+1/n}{\sqrt{(1+1/(2n))(1+1/n)}}
\longrightarrow\frac18.
$$

Donc $\boxed{R=8}$.

### 2. Coefficients exponentiels

$$a_n=e^{1/n}-1.$$

Comme $e^u-1\sim u$ en zéro,

$$\left|\frac{a_{n+1}}{a_n}\right|
=\frac{e^{1/(n+1)}-1}{e^{1/n}-1}
\sim\frac{1/(n+1)}{1/n}\longrightarrow1.$$

Donc $\boxed{R=1}$.

### 3. Produit d’entiers impairs

Le manuscrit écrit

$$a_n=\frac{(-1)^n}{1\times3\times\cdots\times(2n-1)}.$$

Le quotient absolu est obtenu en annulant les facteurs communs. La dernière ligne de la photographie porte une étiquette ajoutée « $2n(2n+1)$ » au dénominateur et conclut que la limite est nulle, donc $R=+\infty$.

> **Correction du quotient :** pour les coefficients écrits ci-dessus, le seul facteur nouveau est $2n+1$. Ainsi $|a_{n+1}/a_n|=1/(2n+1)\to0$. Le facteur $2n$ de l’étiquette est en trop ; le rayon annoncé, $\boxed{R=+\infty}$, reste correct.
