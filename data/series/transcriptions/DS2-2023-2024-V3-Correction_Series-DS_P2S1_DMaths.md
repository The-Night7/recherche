---
source: PREING2-S1/Series-DS/DS2-2023-2024-V3-Correction_Series-DS_P2S1_DMaths.pdf
pages: 1-2
transcription: manuelle
---

# Séries — DS2, version 3, corrigé (2023/2024)

## Consignes

Mercredi 29 novembre 2023. Durée : 60 minutes. Documents et supports électroniques interdits. Exercices indépendants ; barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 : Propriétés de la limite simple

**Énoncé.** Soit $(f_n)$ une suite de fonctions qui converge simplement vers une fonction $f$ sur un intervalle $I$. Dire si les assertions suivantes sont vraies ou fausses :

1. Si les $f_n$ sont croissantes sur $I$, alors $f$ aussi.
2. Si les $f_n$ sont convexes sur $I$, alors $f$ aussi.
3. Si les $f_n$ sont continues sur $I$, alors $f$ aussi.

**Réponses du corrigé.** 1. Vrai. 2. Vrai. 3. Faux.

## Exercice 2 : Convergence de fonctions exponentielles avec paramètre

**Énoncé.** Soit $f_n(x)=n^\alpha x e^{-nx}$, où $\alpha\in\mathbb R$.

1. Montrer que $(f_n)$ converge simplement sur $\mathbb R_+$ vers une limite $f$ à déterminer.
2. Déterminer les $\alpha$ pour lesquels la convergence est uniforme sur $\mathbb R_+$.
3. On fixe $\alpha=1$. Montrer que la convergence est localement uniforme sur $]0,+\infty[$.

**1. Convergence simple.** $f_n(0)=0$. Pour $x>0$ fixé, l'exponentielle l'emporte sur $n^\alpha$, donc $f_n(x)\to0$. La limite simple est la fonction nulle sur $\mathbb R_+$.

**2. Convergence uniforme.** Sur $\mathbb R_+$, $|f_n(x)-0|=f_n(x)$ et

$$f_n'(x)=n^\alpha e^{-nx}-n^{\alpha+1}xe^{-nx}=n^\alpha e^{-nx}(1-nx).$$

Pour $n\ge1$, la dérivée est positive sur $[0,1/n[$, nulle en $1/n$ et négative sur $]1/n,+\infty[$. Le maximum est atteint en $x_n=1/n$ :

$$\sup_{x\in\mathbb R_+}|f_n(x)|=f_n(1/n)=n^\alpha\frac1n e^{-1}=\frac{n^{\alpha-1}}e.$$

Cette quantité tend vers zéro si et seulement si $\alpha<1$. La convergence est donc uniforme exactement pour $\alpha<1$.

**3. Convergence localement uniforme pour $\alpha=1$.** Soient $0<a<b$. Pour $x\in[a,b]$,

$$0\le f_n(x)=nxe^{-nx}\le nb e^{-na},$$

d'où $\sup_{x\in[a,b]}|f_n(x)|\le nb e^{-na}\to0$. La convergence est uniforme sur tout segment $[a,b]\subset]0,+\infty[$, donc localement uniforme sur cet intervalle.

## Exercice 3 : Inversion limite-intégrale

**Énoncé.** Sur $[0,1]$, on définit

$$f_n(x)=\frac{2^n x}{1+2^n n x^2}.$$

1. Étudier la convergence simple sur $[0,1]$.
2. Montrer que $\bigl(\ln(1+2^n n x^2)\bigr)'=2n f_n(x)$.
3. Pour $n\ge1$, calculer $I_n=\int_0^1 f_n(t)\,dt$ et montrer que $I_n\to\ln(2)/2$.
4. En déduire que la convergence n'est pas uniforme sur $[0,1]$.

**1.** $f_n(0)=0$. Pour $x\in]0,1]$ fixé,

$$f_n(x)=\frac{2^n x}{1+2^n n x^2}\sim\frac{2^n x}{2^n n x^2}=\frac1{nx}\longrightarrow0.$$

La limite simple est donc nulle sur $[0,1]$.

**2.** Avec $(\ln U)'=U'/U$,

$$\bigl(\ln(1+2^n n x^2)\bigr)'=\frac{2n2^n x}{1+2^n n x^2}=2n f_n(x).$$

**3.** Pour $n\ge1$,

$$\begin{aligned}
I_n&=\frac1{2n}\left[\ln(1+2^n n t^2)\right]_0^1\\
&=\frac1{2n}\ln(1+2^n n)\\
&=\frac{\ln2}{2}+\frac{\ln n}{2n}+\frac1{2n}\ln\left(1+\frac1{2^n n}\right).
\end{aligned}$$

Comme $\ln(n)/n\to0$ et $\ln(1+1/(2^n n))\sim1/(2^n n)\to0$, on obtient $I_n\to\ln(2)/2$.

**4.** Si les fonctions continues $f_n$ convergeaient uniformément vers zéro sur $[0,1]$, le théorème d'inversion limite-intégrale donnerait

$$\lim_{n\to\infty}\int_0^1 f_n(t)\,dt=\int_0^1\lim_{n\to\infty}f_n(t)\,dt=0,$$

en contradiction avec $\ln(2)/2\ne0$. La convergence n'est pas uniforme sur $[0,1]$.
