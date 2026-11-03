# Fiche 4 : Règles de d'Alembert et de Cauchy

CC1 Séries, jeudi 15 octobre 2026.

| Règle | Quantité | Quand l'utiliser |
|---|---|---|
| D'Alembert | $\left\vert\frac{u_{n+1}}{u_n}\right\vert\to \ell$ | factorielles, $a^n$, produits |
| Cauchy | $\sqrt[n]{\vert u_n\vert}\to \ell$ | puissances $n$-ièmes : $(\dots)^n$, $(\dots)^{n^2}$ |

## Énoncé

On suppose $u_n\ne0$ à partir d'un certain rang pour d'Alembert.

- $\ell<1$ : $\sum u_n$ converge absolument.
- $\ell>1$ : $\sum u_n$ diverge grossièrement.
- $\ell=1$ : **cas douteux**, on ne conclut pas.

## Remarques

- Si d'Alembert donne $\ell=1$, inutile d'essayer Cauchy : il donnera aussi $1$. Change d'outil.
- Sur une série de Riemann, les deux règles donnent $\ell=1$. Elles ne servent à rien pour les fractions rationnelles.
- Limite utile : $\left(1+\frac{x}{n}\right)^n\to e^x$.

## Démonstration de d'Alembert (cas $\ell<1$)

Soit $\varepsilon=\frac{1-\ell}{2}$. À partir d'un rang $n_0$, $\left|\frac{u_{n+1}}{u_n}\right|<\ell+\varepsilon<1$. La suite $\left(\frac{|u_n|}{(\ell+\varepsilon)^n}\right)$ est décroissante et minorée par $0$, donc bornée. Ainsi $|u_n|=O\!\left((\ell+\varepsilon)^n\right)$, et $\sum(\ell+\varepsilon)^n$ converge. Par domination, $\sum|u_n|$ converge.

## Exemples

- $\dfrac{n^2}{3^n}$ : $\dfrac{u_{n+1}}{u_n}=\left(\dfrac{n+1}{n}\right)^2\dfrac13\to\dfrac13<1$, converge.
- $\dfrac{z^n}{n!}$ : $\dfrac{|u_{n+1}|}{|u_n|}=\dfrac{|z|}{n+1}\to0$, converge pour tout $z$.
- $\dfrac{n^{10000}}{n!}$ : $\dfrac{u_{n+1}}{u_n}=\left(\dfrac{n+1}{n}\right)^{10000}\dfrac1{n+1}\to0$, converge.
- $\left(\dfrac{n}{n+1}\right)^{n^2}$ : Cauchy, $\sqrt[n]{u_n}=\dfrac{1}{(1+1/n)^n}\to\dfrac1e<1$, converge.
- $\dfrac{1}{(\ln n)^n}$ : Cauchy, $\sqrt[n]{u_n}=\dfrac1{\ln n}\to0<1$, converge.
- $\left(1-\dfrac1n\right)^{n^2}$ : $\sqrt[n]{u_n}\to\dfrac1e<1$, converge. Pour $\left(1+\dfrac1n\right)^{n^2}$, la limite vaut $e>1$ : diverge.
- $\dfrac{n^{\ln n}}{(\ln n)^n}$ : $\sqrt[n]{u_n}=\dfrac{e^{(\ln n)^2/n}}{\ln n}\to0$, converge.

## Piège

Le cas $\ell=1$ ne se conclut pas. Si la règle donne $1$, repasse par un équivalent ou une comparaison.
