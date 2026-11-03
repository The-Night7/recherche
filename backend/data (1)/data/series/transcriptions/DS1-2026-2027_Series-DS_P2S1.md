# Séries — Devoir Surveillé 1

**CY Tech — 2026/2027 — Semestre 1 — PréIng 2**
Jeudi 15 octobre 2026 — Durée : 90 min

## Consignes

- Les documents et les supports électroniques sont interdits.
- L'épreuve est composée d'exercices indépendants.
- Le barème est à titre indicatif.
- La qualité de la rédaction et la rigueur des justifications seront prises en compte dans la notation.

---

## Exercice 1 (4 pts)

Justifier, à l'aide d'une démonstration ou d'un contre-exemple, que les affirmations suivantes sont vraies ou fausses. On considère $\sum u_n$ et $\sum v_n$ deux séries à termes positifs.

1. Si $u_n = o(v_n)$ et $\sum v_n$ diverge alors la série $\sum u_n$ diverge.
2. Si $u_n = o(v_n)$ et $\sum v_n$ converge alors la série $\sum u_n$ converge.
3. Si $u_n = o(v_n)$ et $\sum u_n$ converge alors la série $\sum v_n$ converge.

---

## Exercice 2 (6 pts)

Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\ge 1} \frac{\ln(n)}{n^{5/4}}$

2. $\displaystyle\sum_{n\ge 1} \ln\!\left(\cos\!\left(\frac{1}{\sqrt{n}}\right)\right)$

3. $\displaystyle\sum_{n\ge 1} (-1)^n \left(\sqrt{n+1} - \sqrt{n}\right)$

4. $\displaystyle\sum_{n\ge 1} \frac{1 + (-1)^n \sqrt{n}}{1 + n}$

---

## Exercice 3 (6 pts)

On considère la série de terme général

$$u_n = \frac{2^n\, n(n-1) + 3^n}{3^n\, n(n-1)}.$$

1. Montrer que la série $\displaystyle\sum_{n\ge 2} u_n$ converge.

2. Soit $S_n = \displaystyle\sum_{k=2}^{n} u_k$ la somme partielle de la série $\displaystyle\sum_{n=2}^{+\infty} u_n$. Montrer qu'on peut écrire $(S_n)$ sous la forme
$$S_n = T_n + W_n$$
où $(T_n)$ est la somme partielle d'une série géométrique dont on précisera la raison et $(W_n)$ la somme partielle d'une série télescopique.

3. En déduire la valeur de $S = \displaystyle\sum_{n=2}^{+\infty} u_n$.

---

## Exercice 4 (6 pts)

On considère la série
$$\sum_{n\ge 3} \frac{\ln n}{n}.$$

1. Montrer que, $\forall n \ge 3$,
$$\sum_{k=3}^{n} \frac{\ln k}{k} \;\ge\; \int_{3}^{n+1} \frac{\ln x}{x}\,\mathrm{d}x.$$

2. Calculer l'intégrale
$$\int_{3}^{n+1} \frac{\ln x}{x}\,\mathrm{d}x.$$

3. En déduire que
$$\sum_{k=3}^{n} \frac{\ln k}{k} \;\ge\; \frac{1}{2}\left(\ln^2(n+1) - \ln^2(3)\right).$$

4. En déduire la nature de la série $\displaystyle\sum_{n\ge 3} \frac{\ln n}{n}$.
