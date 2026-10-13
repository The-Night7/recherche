# Fiche 3 : Séries à termes positifs

CC1 Séries, jeudi 15 octobre 2026. Valable dès que $u_n$ garde un signe constant à partir d'un certain rang. Écris toujours « série à termes positifs » avant d'utiliser un de ces outils.

## Les six outils

1. **Sommes partielles.** À termes positifs, $\sum u_n$ converge $\iff (S_n)$ est majorée. En cas de divergence, $S_n\to+\infty$.
2. **Inégalité.** Soit $0\le u_n\le v_n$. Si $\sum v_n$ converge, alors $\sum u_n$ converge. Si $\sum u_n$ diverge, alors $\sum v_n$ diverge.
3. **Équivalent.** Si $u_n\sim v_n$, les deux séries ont même nature. En cas de convergence, les restes sont équivalents. En cas de divergence, les sommes partielles sont équivalentes. C'est l'outil le plus rentable.
4. **Domination.** Si $u_n=O(v_n)$ ou $u_n=o(v_n)$ et $\sum v_n$ converge, alors $\sum u_n$ converge.
5. **Règle $n^\alpha$.** Si $n^\alpha u_n\to0$ avec $\alpha>1$, la série converge. Si $n^\alpha u_n\to+\infty$ avec $\alpha\le1$, la série diverge.
6. **Série-intégrale.** Soit $f$ positive et décroissante. Alors $\sum f(n)$ et $\int^{+\infty}f$ ont même nature.

## Exemples types

- $\dfrac{e^{1/\sqrt n}-1}{n^2(n-1)}\sim\dfrac{1}{n^{7/2}}$, Riemann $\alpha=\frac72>1$ : converge.
- $\ln\!\left(1+\dfrac{1}{\sqrt n}\right)\sim\dfrac{1}{\sqrt n}$, Riemann $\alpha=\frac12\le1$ : diverge.
- $\dfrac{\ln n}{n^{3/2}}$ : $n^{5/4}u_n=\dfrac{\ln n}{n^{1/4}}\to0$, avec $\alpha=\frac54>1$ : converge.
- $\dfrac{1}{n^3\left(2+\sin\sqrt{n^3+n^2+5}\right)}\le\dfrac1{n^3}$ : converge par inégalité.
- $\dfrac{\exp\left(\cos\left(\frac{n!}{\sqrt{n^2+1}}\right)\right)}{\sqrt n}\ge\dfrac{1}{e\sqrt n}$ : diverge par inégalité.

## Piège

On ne somme pas des équivalents et on ne les compose pas à gauche : pas d'équivalent dans un $\ln$ ou dans une exponentielle. Dans le doute, passe par un développement limité.

Le critère d'équivalence est faux pour les séries dont le terme change de signe (voir fiche 5).

## Termes de signe constant mais négatifs

Tout s'adapte en remplaçant « croissant » par « décroissant » et « majoré » par « minoré ». On peut aussi passer à $-u_n$.
