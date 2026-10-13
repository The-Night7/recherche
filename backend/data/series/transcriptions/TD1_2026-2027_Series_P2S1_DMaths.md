---
source: "PREING2-S1/Series/2627/Séries_TD1_2627.pdf"
pages: 3
annee: 2026-2027
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — TD1 : séries numériques (2026–2027)

CY Tech — PréIng 2, semestre 1. Énoncés des trois pages du PDF.

## Partie I — Séries numériques à termes positifs (page 1)

### Exercice 1

Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\ge1}\cos\frac1{n^2}$.
2. $\displaystyle\sum_{n\ge0}\frac{(-1)^n n}{n+1}$.
3. $\displaystyle\sum_{n\ge1}\left(1+\frac1n\right)^n$.
4. $\displaystyle\sum_{n\ge1}\left(\cos\frac1n\right)^{n^2}$.

> La deuxième série est alternée, malgré le titre de cette partie ; elle est reproduite à sa place dans le document.

### Exercice 2

Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\ge1}\frac{n^2+1}{n^2}$.
2. $\displaystyle\sum_{n\ge1}\frac2{\sqrt n}$.
3. $\displaystyle\sum_{n\in\mathbb N}\frac{(2n+1)^4}{(7n^2+1)^3}$.
4. $\displaystyle\sum_{n\ge1}\left(ne^{1/n}-n\right)$.
5. $\displaystyle\sum_{n\ge2}\frac1{(\ln n)^n}$.
6. $\displaystyle\sum_{n\in\mathbb N}\ln(1+e^{-n})$.

### Exercice 3

Soit $(u_n)$ une suite de réels positifs et $v_n=\dfrac{u_n}{1+u_n}$. Montrer que $\sum_{n\in\mathbb N}u_n$ et $\sum_{n\in\mathbb N}v_n$ sont de même nature.

### Exercice 4

Étudier la nature et, le cas échéant, calculer la somme des séries de terme général :

1. $\displaystyle u_n=\frac1{n(n+1)}$.
2. $\displaystyle u_n=\frac1{n(n+1)(n+2)}$.
3. $\displaystyle u_n=\frac{2n-1}{n(n^2-4)}$.
4. $\displaystyle u_n=\ln\left(1-\frac1{(n+2)^2}\right)$.

> **Précision sur la source :** aucun rang initial n’est indiqué dans cet exercice. Il faut exclure les indices où le terme n’est pas défini ; le choix du premier terme influe sur la somme.

### Exercice 5 — Séries de Bertrand

1. Montrer que
   $$\forall n\ge2,\qquad\sum_{k=2}^n\frac1{k\ln k}\ge\ln(\ln(n+1))-\ln(\ln2).$$
2. En déduire la nature de $\displaystyle\sum_{n\ge2}\frac1{n\ln n}$.
3. Montrer que
   $$\forall n\ge3,\qquad\sum_{k=3}^n\frac1{k\ln^2k}\le\frac1{\ln2}.$$
4. En déduire la nature de $\displaystyle\sum_{n\ge2}\frac1{n\ln^2n}$.

## Exercices supplémentaires (page 2)

### Exercice 6

Étudier la nature de la série de terme général :

1. $\displaystyle u_n=\frac{n+1}{n^3-7}$.
2. $\displaystyle u_n=\frac{n+1}{n^2-7}$.
3. $\displaystyle u_n=\frac{n+1}{n-7}$.
4. $\displaystyle u_n=\sin\left(\frac1{n^2}\right)$.
5. $\displaystyle u_n=\frac1{n^{1+1/\sqrt n}}$.
6. $\displaystyle u_n=\frac1{\ln(n^2+2)}$.
7. $\displaystyle u_n=\frac{\ln n}{n^{3/2}}$.
8. $\displaystyle u_n=\frac n{2^n}$.
9. $\displaystyle u_n=\frac{n^n}{2^n}$.
10. $\displaystyle u_n=\frac{2^n+3^n}{n^2+\ln n+5^n}$.
11. $\displaystyle u_n=\frac1{n!}$.
12. $\displaystyle u_n=\frac{n^{10000}}{n!}$.
13. $\displaystyle u_n=\left(\sin\frac1n\right)^n$.
14. $\displaystyle u_n=\left(1-\frac1n\right)^{n^2}$.
15. $\displaystyle u_n=\left(1+\frac1n\right)^{n^2}$.

> Les rangs initiaux ne sont pas précisés ; notamment, le terme de la question 3 est indéfini pour $n=7$. L’étude de nature se fait à partir d’un rang où les termes sont définis.

### Exercice 7

Étudier la nature de la série de terme général

$$u_n=\left(\sqrt{n^2+an+2}-\sqrt{n^2+bn+1}\right)^n,\qquad(a,b)\in\mathbb R^2,\quad a\ge b.$$

## Partie II — Séries numériques à termes quelconques (page 3)

### Exercice 8

Considérons les séries

$$\sum_{n\ge1}\frac{(-1)^n}{\sqrt n}\qquad\text{et}\qquad\sum_{n\ge1}\ln\left(1+\frac{(-1)^n}{\sqrt n}\right).$$

Montrer que les termes généraux sont équivalents, mais que les séries n’ont pas la même nature.

> **Coquille de la source :** le logarithme n’est pas défini pour $n=1$. La seconde série doit commencer à $n=2$ pour être une série réelle bien définie.

### Exercice 9

Étudier les séries :

1. $\displaystyle\sum_{n\ge1}\left(\sqrt{1+\frac{(-1)^n}{\sqrt n}}-1\right)$.
2. $\displaystyle\sum_{n\ge1}(-1)^n\sqrt n\sin\frac1n$.
3. $\displaystyle\sum_{n\ge2}\frac{(-1)^n}{n+(-1)^n}$.

### Exercice 10

Étudier la convergence de la série numérique de terme général :

1. $\displaystyle u_n=(-1)^n\frac{n^3}{n!}$.
2. $\displaystyle u_n=\frac{a^n}{n!}$, $a\in\mathbb C$.
3. $\displaystyle u_n=na^{n-1}$, $a\in\mathbb C$.
4. $\displaystyle u_n=\sin\left(\frac{n^2+1}{n}\pi\right)$.
5. $\displaystyle u_n=(-1)^n\left(\sqrt{n+1}-\sqrt n\right)$.
6. $\displaystyle u_n=n\ln\left(1+\frac1n\right)-\cos\left(\frac1{\sqrt n}\right)$.

### Exercice 11

On considère la série $\displaystyle\sum_{n\ge0}\frac{(-1)^n}{n+1}$.

1. Montrer qu’elle converge.
2. Montrer que, pour tout $n\in\mathbb N$,
   $$\sum_{k=0}^n\frac{(-1)^k}{k+1}=\int_0^1\frac{dt}{1+t}-(-1)^{n+1}\int_0^1\frac{t^{n+1}}{1+t}\,dt.$$
3. Montrer que
   $$\forall n\in\mathbb N,\qquad0\le\int_0^1\frac{t^{n+1}}{1+t}\,dt\le\frac1{n+2}.$$
4. En déduire que $\displaystyle\sum_{n=0}^{+\infty}\frac{(-1)^n}{n+1}=\ln2$.
5. Donner une valeur approchée de $\ln2$ à la précision $10^{-3}$.

### Exercice 12

Montrer la convergence et calculer les sommes des séries de terme général :

1. $\displaystyle u_n=\sum_{k=0}^n\frac1{(n-k)!k!}$.
2. $\displaystyle u_n=\sum_{k=0}^n\frac{(-1)^{n-k}}{k!2^{n-k}}$.
