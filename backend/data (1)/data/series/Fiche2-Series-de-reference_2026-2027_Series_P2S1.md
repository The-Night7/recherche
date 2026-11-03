# Fiche 2 : Séries de référence

CC1 Séries, jeudi 15 octobre 2026.

| Série | Nature | À retenir |
|---|---|---|
| Géométrique $\sum z^n$ | converge $\iff \lvert z\rvert<1$ | $\sum_{n\ge0}z^n=\frac{1}{1-z}$ et $\sum_{n\ge N}z^n=\frac{z^N}{1-z}$ |
| Riemann $\sum \frac{1}{n^\alpha}$ | converge $\iff \alpha>1$ | $\sum\frac{1}{n^2}=\frac{\pi^2}{6}$ ; harmonique $\sum\frac1n$ diverge |
| Riemann alternée $\sum \frac{(-1)^n}{n^\alpha}$ | converge $\iff \alpha>0$ | semi-convergente pour $0<\alpha\le1$ |
| Exponentielle $\sum \frac{z^n}{n!}$ | converge pour tout $z$ | somme $e^z$ |
| Bertrand $\sum \frac{1}{n\ln n}$ | diverge | comparaison série-intégrale, primitive $\ln(\ln t)$ |
| Bertrand $\sum \frac{1}{n\ln^2 n}$ | converge | primitive $-\frac{1}{\ln t}$ |

## Série harmonique

$$\sum_{k=1}^{n}\frac1k=\ln n+\gamma+o(1),\qquad\text{donc}\qquad\sum_{k=1}^n\frac1k\sim\ln n$$

La constante d'Euler $\gamma$ est la limite commune des suites adjacentes $\sum_{k=1}^n\frac1k-\ln(n+1)$ et $\sum_{k=1}^n\frac1k-\ln n$.

## Série de Riemann : démonstration

Pour $\alpha\le0$, le terme ne tend pas vers $0$ : divergence grossière. Pour $\alpha>0$, la fonction $t\mapsto\frac1{t^\alpha}$ est décroissante, donc pour tout $k\ge1$

$$\frac{1}{(k+1)^\alpha}\le\int_k^{k+1}\frac{dt}{t^\alpha}\le\frac{1}{k^\alpha}$$

- $\alpha\le1$ : $\sum_{k=1}^n\frac1{k^\alpha}\ge\int_1^{n+1}\frac{dt}{t^\alpha}\to+\infty$, la série diverge.
- $\alpha>1$ : $S_n\le1+\int_1^n\frac{dt}{t^\alpha}\le1+\frac1{\alpha-1}$. La suite $(S_n)$ est croissante et majorée, donc elle converge.

## Comparaison série-intégrale

Soit $f$ positive et décroissante sur $[a,+\infty[$. Alors $\sum f(n)$ et $\int_a^{+\infty}f(t)\,dt$ ont même nature. Encadrement de base :

$$f(k+1)\le\int_k^{k+1}f(t)\,dt\le f(k)$$

## Piège

Bertrand n'est pas un résultat à citer : il se redémontre à chaque fois par comparaison série-intégrale (TD1, exercice 5).

- Divergence de $\sum\frac1{n\ln n}$ : $\sum_{k=2}^n\frac1{k\ln k}\ge\int_2^{n+1}\frac{dt}{t\ln t}=\ln(\ln(n+1))-\ln(\ln2)\to+\infty$.
- Convergence de $\sum\frac1{n\ln^2n}$ : $\sum_{k=3}^n\frac1{k\ln^2k}\le\int_2^n\frac{dt}{t\ln^2t}\le\frac1{\ln2}$.
