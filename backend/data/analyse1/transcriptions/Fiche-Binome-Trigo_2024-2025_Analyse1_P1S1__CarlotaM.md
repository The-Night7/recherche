---
source: PREING1-S1/Analyse1/Fiche-Binome-Trigo_2024-2025_Analyse1_P1S1__CarlotaM.pdf
pages: 1-2
transcription: manuelle
---

# Analyse 1 — Binôme, trigonométrie et méthodes de calcul

## Coefficients binomiaux

Pour $n,k\in\mathbb N$ avec $0\le k\le n$,

$$\binom nk=\frac{n!}{k!(n-k)!}.$$

On pose $\binom nk=0$ pour $k>n$. En particulier,

$$\binom n0=\binom nn=1,\qquad\binom n1=n.$$

**Symétrie :** $\binom nk=\binom n{n-k}$.

Pour $1\le k\le n$, $k\binom nk=n\binom{n-1}{k-1}$.

**Relation de Pascal :**

$$\binom nk=\binom{n-1}k+\binom{n-1}{k-1}.$$

Le triangle de Pascal commence par les lignes $1$ ; $1,1$ ; $1,2,1$ ; $1,3,3,1$ ; $1,4,6,4,1$ ; $1,5,10,10,5,1$. Par exemple, $\binom51=\binom40+\binom41=1+4=5$. Les coefficients binomiaux sont des entiers.

## Formule du binôme de Newton

Pour $x,y\in\mathbb R$ et $n\in\mathbb N$,

$$ (x+y)^n=\sum_{k=0}^n\binom nk x^{n-k}y^k.$$

Par exemple, pour $n\ge1$,

$$\sum_{k=0}^n\binom nk(-1)^k=(1-1)^n=0.$$

Autre exemple indiqué sur la fiche :

$$\sum_{k=0}^n\binom nk5^k1^{n-k}=(5+1)^n=6^n.$$

> La condition $n\ge1$ est nécessaire dans l'exemple de la somme alternée ; pour $n=0$, cette somme vaut $1$.

## Cercle trigonométrique et congruence

Un point $(a,b)$ du cercle unité vérifie $a^2+b^2=1$, donc $-1\le a,b\le1$. Pour l'angle $x$, ses coordonnées sont $(\cos x,\sin x)$, et

$$-1\le\cos x\le1,\qquad-1\le\sin x\le1,\qquad\cos^2x+\sin^2x=1.$$

La congruence $x\equiv y\pmod\theta$ signifie qu'il existe $k\in\mathbb Z$ tel que $x-y=k\theta$.

> Le quantificateur est existentiel ; le « pour tout $k$ » de la fiche est rectifié.

## Périodicité, parité et égalités trigonométriques

$$\sin(x+2\pi)=\sin x,\qquad\cos(x+2\pi)=\cos x,$$

$$\sin(-x)=-\sin x,\qquad\cos(-x)=\cos x.$$

$$\sin x=\sin y\iff x\equiv y\pmod{2\pi}\text{ ou }x\equiv\pi-y\pmod{2\pi},$$

$$\cos x=\cos y\iff x\equiv y\pmod{2\pi}\text{ ou }x\equiv-y\pmod{2\pi}.$$

## Transformations des angles

$$\sin(x+\pi)=-\sin x,\qquad\cos(x+\pi)=-\cos x,$$

$$\sin(\pi-x)=\sin x,\qquad\cos(\pi-x)=-\cos x,$$

$$\sin(x+\pi/2)=\cos x,\qquad\cos(x+\pi/2)=-\sin x,$$

$$\sin(\pi/2-x)=\cos x,\qquad\cos(\pi/2-x)=\sin x.$$

Les notes de méthode en fin de fiche reprennent les décalages de $\pi$ et $\pi/2$. Pour les décalages négatifs :

$$\sin(x-\pi)=-\sin x,\quad\cos(x-\pi)=-\cos x,$$

$$\sin(x-\pi/2)=-\cos x,\quad\cos(x-\pi/2)=\sin x.$$

> **Rectifications :** la fiche écrit $\cos(\pi-x)=\sin x$ et omet un signe dans le rappel de $\sin(x-\pi/2)$. Les formules corrigées sont celles ci-dessus.

## Addition et duplication

$$\sin(x+y)=\sin x\cos y+\cos x\sin y,$$

$$\cos(x+y)=\cos x\cos y-\sin x\sin y,$$

$$\sin(x-y)=\sin x\cos y-\cos x\sin y,$$

$$\cos(x-y)=\cos x\cos y+\sin x\sin y.$$

$$\sin(2x)=2\sin x\cos x,$$

$$\cos(2x)=\cos^2x-\sin^2x=2\cos^2x-1=1-2\sin^2x.$$

## Formules de produit

$$\cos x\cos y=\frac12\bigl(\cos(x+y)+\cos(x-y)\bigr),$$

$$\sin x\sin y=\frac12\bigl(\cos(x-y)-\cos(x+y)\bigr),$$

$$\sin x\cos y=\frac12\bigl(\sin(x+y)+\sin(x-y)\bigr).$$

## Valeurs remarquables

| $x$ | $0$ | $\pi/6$ | $\pi/4$ | $\pi/3$ | $\pi/2$ |
| --- | --- | --- | --- | --- | --- |
| $\sin x$ | $0$ | $1/2$ | $1/\sqrt2$ | $\sqrt3/2$ | $1$ |
| $\cos x$ | $1$ | $\sqrt3/2$ | $1/\sqrt2$ | $1/2$ | $0$ |
| $\tan x$ | $0$ | $1/\sqrt3=\sqrt3/3$ | $1$ | $\sqrt3$ | non définie |

## Fonction tangente

Pour $x\notin\pi/2+\pi\mathbb Z$,

$$\tan x=\frac{\sin x}{\cos x}.$$

La tangente est $\pi$-périodique et impaire : $\tan(x+\pi)=\tan x$ et $\tan(-x)=-\tan x$. Pour $x,y$ dans son domaine,

$$\tan x=\tan y\iff x\equiv y\pmod\pi.$$

Lorsque les expressions sont définies et les dénominateurs non nuls,

$$\tan(x+y)=\frac{\tan x+\tan y}{1-\tan x\tan y},$$

$$\tan(x-y)=\frac{\tan x-\tan y}{1+\tan x\tan y},$$

$$\tan(2x)=\frac{2\tan x}{1-\tan^2x}.$$

## Méthode : écrire un produit avec des factorielles

Pour $n\ge2$, on veut calculer $\prod_{k=2}^n(2k+1)=5\cdot7\cdots(2n+1)$.

On sépare les facteurs pairs et impairs dans le produit des entiers de $5$ à $2n+1$ :

$$\begin{aligned}
\prod_{k=2}^n(2k+1)
&=\frac{\prod_{j=5}^{2n+1}j}{\prod_{k=3}^n(2k)}\\
&=\frac{(2n+1)!/4!}{2^{n-2}(n!/2!)}\\
&=\frac{(2n+1)!}{12\,2^{n-2}n!}
=\frac{(2n+1)!}{3\,2^n n!}.
\end{aligned}$$

## Méthode : changement d'indice et simplification

Pour $n\ge2$, en posant $k'=k+2$,

$$\prod_{k=2}^n(k+2)=\prod_{k'=4}^{n+2}k'.$$

Donc

$$\prod_{k=2}^n\frac{k}{k+2}
=\frac{\prod_{k=2}^n k}{\prod_{k=4}^{n+2}k}
=\frac{6}{(n+1)(n+2)}.$$
