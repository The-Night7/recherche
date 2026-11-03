# Analyse 1 — DS1 2024–2025, corrigé manuscrit (version 3)

> Source : `PREING1-S1/Analyse1-DS/DS1-2024-2025-V3-Correction_Analyse1-DS_P1S1_PAfsharijoo.pdf`, 3 pages. Année et attribution issues du nom du fichier ; pas de date complète sur les pages.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules, tableaux de signes et représentation des intervalles restitués. Les annotations rouges modifient certains résultats et portent un barème parfois raturé ; les corrections mathématiques lisibles sont prises en compte et signalées. Les énoncés complets ne figurent pas dans la source.

## Exercice 1 — Équations trigonométriques (page 1)

### 1. $\sin(2x)=1/2$

$$
\begin{aligned}
\sin(2x)=\frac12=\sin\frac\pi6
&\Longleftrightarrow 2x=\frac\pi6+2k\pi\text{ ou }2x=\frac{5\pi}6+2k\pi\\
&\Longleftrightarrow x=\frac\pi{12}+k\pi\text{ ou }x=\frac{5\pi}{12}+k\pi,\qquad k\in\mathbb Z.
\end{aligned}
$$

L’ensemble des solutions est $S=\{\pi/12+k\pi,\ 5\pi/12+k\pi\mid k\in\mathbb Z\}$. Sur $[0,2\pi]$ :

$$S\cap[0,2\pi]=\left\{\frac\pi{12},\frac{13\pi}{12},\frac{5\pi}{12},\frac{17\pi}{12}\right\}.$$

### 2. Équation en $\cos x$

Posons $X=\cos x$. L’équation devient $2X^2-3X+1=0$. Son discriminant est $\Delta=9-4\times2\times1=1$, d’où :

$$X_1=\frac{3-1}4=\frac12,\qquad X_2=\frac{3+1}4=1.$$

Or :

$$\cos x=\frac12=\cos\frac\pi3\Longleftrightarrow x=\pm\frac\pi3+2k\pi,$$

$$\cos x=1\Longleftrightarrow x=2k\pi,\qquad k\in\mathbb Z.$$

Donc $S=\{\pm\pi/3+2k\pi,\ 2k\pi\mid k\in\mathbb Z\}$. Sur $[0,2\pi]$, les solutions sont $0,2\pi,\pi/3,5\pi/3$.

## Exercice 2 — Écritures décimales périodiques (page 1)

### 1. $a=2,0\overline{63}$

$$10a=20,\overline{63},\qquad1000a=2063,\overline{63}.$$

Par soustraction, $990a=2043$, donc $a=2043/990$.

### 2. $b=3,\overline{54}$

$$100b=354,\overline{54},\qquad99b=351,\qquad b=\frac{351}{99}.$$

**Note sur la source.** Le résultat bleu $354$ dans les deux dernières expressions est corrigé en rouge en $351$. La soustraction $100b-b$ confirme cette correction.

## Exercice 3 — Inéquation avec racine carrée (page 1)

Le manuscrit commence par imposer $x\in]-2,+\infty[$, puis étudie $\sqrt{x+2}\geq x-1$.

- Si $x-1<0$, la condition est satisfaite ; la source donne $S_1=]-2,1[$.
- Si $x\geq1$, les deux membres sont positifs ou nuls et :

$$\sqrt{x+2}\geq x-1\Longleftrightarrow x+2\geq x^2-2x+1\Longleftrightarrow x^2-3x-1\leq0.$$

$\Delta=9-4\times1\times(-1)=13$, avec $x_1=(3-\sqrt{13})/2$ et $x_2=(3+\sqrt{13})/2$.

| $x$ | $]-\infty,x_1[$ | $x_1$ | $]x_1,x_2[$ | $x_2$ | $]x_2,+\infty[$ |
| --- | --- | --- | --- | --- | --- |
| $x^2-3x-1$ | $+$ | $0$ | $-$ | $0$ | $+$ |

Ainsi $S_2=[1,+\infty[\cap[x_1,x_2]=[1,x_2]$. La conclusion du manuscrit est :

$$S=\left]-2,\frac{3+\sqrt{13}}2\right].$$

**Note sur la source.** Si l’inéquation à résoudre est uniquement $\sqrt{x+2}\geq x-1$, sans autre restriction provenant de l’énoncé absent, $x=-2$ est aussi admissible et solution. L’intervalle serait alors fermé en $-2$. Le corrigé exclut ce point dès sa première ligne.

## Exercice 4 — Somme binomiale et produit (page 2)

### 1. Somme

Le calcul demandé est :

$$2\sum_{k=0}^n k\binom nk+\sum_{k=0}^n\binom nk=n2^n+2^n=(n+1)2^n.$$

Pour justifier, on calcule :

$$
\begin{aligned}
\sum_{k=0}^n k\binom nk
&=\sum_{k=1}^n\frac{n!}{(n-k)!k!}\,k\\
&=n\sum_{k=1}^n\frac{(n-1)!}{(n-k)!(k-1)!}\\
&=n\sum_{k=1}^n\binom{n-1}{k-1}\\
&=n\sum_{\ell=0}^{n-1}\binom{n-1}\ell=n2^{n-1}.
\end{aligned}
$$

On utilise également $\sum_{k=0}^n\binom nk=2^n$. Les annotations attribuent 2 points au premier calcul et 1 point à la seconde identité.

### 2. Produit

$$
\begin{aligned}
\prod_{k=1}^n\left(1+\frac{k}{k+2}\right)
&=\prod_{k=1}^n\frac{2k+2}{k+2}\\
&=\frac{2^n\prod_{k=1}^n(k+1)}{\prod_{k=1}^n(k+2)}\\
&=\frac{2^n\prod_{\ell=2}^{n+1}\ell}{\prod_{\ell=3}^{n+2}\ell}\\
&=\frac{2^n\times2}{n+2}=\boxed{\frac{2^{n+1}}{n+2}}.
\end{aligned}
$$

Les deux étapes de transformation et de simplification sont chacune annotées 1 point.

## Exercice 5 — Bornes d’ensembles (pages 2–3)

### 1. Ensemble $A$

La première condition étudiée est :

$$\frac{x^2+3x+8}{x+1}-6=\frac{x^2+3x+8-6x-6}{x+1}=\frac{x^2-3x+2}{x+1}>0.$$

Le numérateur a discriminant 1 et racines $(3-1)/2=1$, $(3+1)/2=2$.

| $x$ | $]-\infty,-1[$ | $-1$ | $]-1,1[$ | $1$ | $]1,2[$ | $2$ | $]2,+\infty[$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $x^2-3x+2$ | $+$ | $+$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| $x+1$ | $-$ | $0$ | $+$ | $+$ | $+$ | $+$ | $+$ |
| $(x^2-3x+2)/(x+1)$ | $-$ | non défini | $+$ | $0$ | $-$ | $0$ | $+$ |

Donc $S_1=]-1,1[\cup]2,+\infty[$.

La seconde condition donne :

$$|x+1|\leq4\Longleftrightarrow-4\leq x+1\leq4\Longleftrightarrow-5\leq x\leq3.$$

Donc $S_2=[-5,3]$ et :

$$\boxed{A=S_1\cap S_2=]-1,1[\cup]2,3].}$$

Le schéma place $S_2$ comme un segment fermé de $-5$ à 3, et $S_1$ comme un intervalle ouvert de $-1$ à 1 puis une demi-droite ouverte à partir de 2. Leur intersection conserve les points strictement entre $-1$ et 1 et ceux strictement au-dessus de 2 jusqu’à 3 inclus.

- Les majorants de $A$ sont les réels de $[3,+\infty[$.
- Les minorants de $A$ sont les réels de $]-\infty,-1]$.
- $\sup A=3=\max A$.
- $\inf A=-1$ ; $A$ n’a pas de minimum puisque $-1\notin A$.

### 2. Ensemble $B=\{m/(n+m)\mid m,n\in\mathbb N^*\}$

Pour tous $m,n\in\mathbb N^*$, $m/(n+m)>0$. Ainsi 0 est un minorant et $0\leq\inf B$. Pour $m$ fixé :

$$\inf B\leq\frac m{n+m}\quad\Longrightarrow\quad\inf B\leq\lim_{n\to+\infty}\frac m{n+m}=0.$$

Donc $\boxed{\inf B=0}$.

Comme $m<n+m$, on a $m/(n+m)<1$. Ainsi 1 est un majorant et $\sup B\leq1$. Pour $n$ fixé :

$$\frac m{n+m}\leq\sup B\quad\Longrightarrow\quad1=\lim_{m\to+\infty}\frac m{n+m}\leq\sup B.$$

Donc $\boxed{\sup B=1}$.

Les majorants de $B$ sont les réels de $[1,+\infty[$ ; ses minorants sont ceux de $]-\infty,0]$. Comme $m/(n+m)$ n’est jamais égal à 0 ni à 1 pour $m,n\in\mathbb N^*$, $B$ n’a ni minimum ni maximum.
