# Fiche 7 : Équivalents et développements limités

CC1 Séries, jeudi 15 octobre 2026. Les formules ci-dessous sont pour $u\to0$. En pratique $u=\frac1n$, $\frac1{\sqrt n}$ ou $\frac{(-1)^n}{\sqrt n}$.

| Fonction | Équivalent | Développement |
|---|---|---|
| $\ln(1+u)$ | $u$ | $u-\frac{u^2}{2}+\frac{u^3}{3}+o(u^3)$ |
| $e^u-1$ | $u$ | $u+\frac{u^2}{2}+o(u^2)$ |
| $\sin u$ | $u$ | $u-\frac{u^3}{6}+o(u^3)$ |
| $1-\cos u$ | $\frac{u^2}{2}$ | $\frac{u^2}{2}-\frac{u^4}{24}+o(u^4)$ |
| $(1+u)^\alpha-1$ | $\alpha u$ | $\alpha u+\frac{\alpha(\alpha-1)}{2}u^2+o(u^2)$ |
| $\frac{1}{1+u}$ | $1$ | $1-u+u^2+o(u^2)$ |
| $\tan u$ | $u$ | $u+\frac{u^3}{3}+o(u^3)$ |

## Rappels sur les relations de comparaison

- $f\sim g\iff\lim\frac fg=1\iff f=g+o(g)$. C'est une relation d'équivalence.
- $f=o(g)\iff\lim\frac fg=0$. $f=O(g)\iff\frac fg$ est bornée.
- Autorisé sur les équivalents : produit, quotient, puissance fixe, composition à droite.
- **Interdit** : somme d'équivalents, composition à gauche.

## Croissances comparées

Pour $\alpha,\beta>0$ et $a>1$ :

$$(\ln n)^\beta\ll n^\alpha\ll a^n\ll n!\ll n^n$$

## Forme $a_n^{\,b_n}$

Passe toujours par $\exp(b_n\ln a_n)$.

- Exemple : $\left(n\sin\frac1n\right)^{n^a}$. On a $n\sin\frac1n=1-\frac1{6n^2}+o\!\left(\frac1{n^2}\right)$, donc $\ln u_n=-\frac16n^{a-2}+o(n^{a-2})$.
  - Si $a<2$, $u_n\to1\ne0$ et la série diverge grossièrement.
  - Si $a>2$, $n^2u_n\to0$ et la série converge (règle $n^\alpha$ avec $\alpha=2$).
- Exemple : $\left(\cos\frac1n\right)^{n^2}$, $n^2\ln\cos\frac1n\sim-\frac12$, donc $u_n\to e^{-1/2}\ne0$ et la série diverge grossièrement.

## Technique : mettre le terme dominant en facteur

- $\dfrac1{\sqrt{n^2-1}}-\dfrac1{\sqrt{n^2+1}}=\dfrac1n\left[\left(1-\dfrac1{n^2}\right)^{-1/2}-\left(1+\dfrac1{n^2}\right)^{-1/2}\right]\sim\dfrac1{n^3}$, la série converge.
- $1-\cos\frac1n\sim\frac1{2n^2}$ et $e^{1/n}-1\sim\frac1n$, donc $\dfrac{1-\cos(1/n)}{e^{1/n}-1}\sim\dfrac1{2n}$, la série diverge.
- $\ln\!\left(\dfrac{(n+1)^2}{n(n+2)}\right)=\ln\!\left(1+\dfrac1{n(n+2)}\right)\sim\dfrac1{n^2}$, la série converge.

## Piège

Dans un $\ln$ ou une exponentielle, on ne remplace pas par un équivalent. Écris un développement limité avec son reste, par exemple $\ln\!\left(1+\frac{1}{\sqrt n}\right)=\frac1{\sqrt n}-\frac1{2n}+o\!\left(\frac1n\right)$.
