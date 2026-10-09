# Fiche 6 : Calculer une somme

CC1 Séries, jeudi 15 octobre 2026.

## Les méthodes

- **Télescopage.** Si $u_n=a_n-a_{n+1}$, alors $\sum_{n=1}^{N}u_n=a_1-a_{N+1}$. La série converge $\iff(a_n)$ converge.
- **Fraction rationnelle.** Décompose en éléments simples, puis regroupe en différences. Exemple : $\dfrac1{n(n+1)}=\dfrac1n-\dfrac1{n+1}$, somme égale à $1$.
- **Logarithme.** Transforme le quotient en différences de $\ln$, puis télescope.
- **Polynôme sur $n!$.** Écris le polynôme dans la base $1,\ n,\ n(n-1),\dots$ puis simplifie : $\dfrac{n(n-1)}{n!}=\dfrac1{(n-2)!}$. Chaque morceau vaut $e$.
- **Géométrique.** Sors les constantes : $\sum_{n\ge0}\dfrac{2^n}{3^{n-2}}=9\sum_{n\ge0}\left(\dfrac23\right)^n=27$.

## Sommes à connaître

$$\sum_{n\ge1}\frac{1}{n(n+1)}=1,\qquad\sum_{n\ge0}\frac{1}{n!}=e,\qquad\sum_{n\ge0}\frac{(-1)^n}{n+1}=\ln2,\qquad\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}6$$

## Trois exemples complets

**1. Fraction rationnelle.** $u_n=\dfrac{1}{n(n+1)(n+2)}=\dfrac12\left(\dfrac1n-\dfrac1{n+1}\right)+\dfrac12\left(\dfrac1{n+2}-\dfrac1{n+1}\right)$. Alors

$$\sum_{k=1}^nu_k=\frac12\left(1-\frac1{n+1}\right)+\frac12\left(\frac1{n+2}-\frac12\right)\xrightarrow[n\to+\infty]{}\frac12-\frac14=\frac14$$

**2. Polynôme sur $n!$.** On écrit $n^2-2=n(n-1)+n-2$, donc

$$\sum_{n\ge0}\frac{n^2-2}{n!}=\sum_{n\ge2}\frac1{(n-2)!}+\sum_{n\ge1}\frac1{(n-1)!}-2\sum_{n\ge0}\frac1{n!}=e+e-2e=0$$

**3. Logarithme.** $u_n=\ln(n)-2\ln(n+1)+\ln(n+2)=\big(\ln n-\ln(n+1)\big)+\big(\ln(n+2)-\ln(n+1)\big)$. Alors

$$S_N=-\ln2+\ln\!\left(\frac{N+2}{N+1}\right)\xrightarrow[N\to+\infty]{}-\ln2$$

La série converge si et seulement si $\alpha=\beta=0$ dans le développement $u_n=\alpha\ln n+\frac\beta n+O\!\left(\frac1{n^2}\right)$, c'est-à-dire pour les coefficients $(1,-2,1)$.

## Valeur de $\ln 2$ (TD1, exercice 11)

$\displaystyle\sum_{k=0}^n\frac{(-1)^k}{k+1}=\int_0^1\frac{dt}{1+t}-(-1)^{n+1}\int_0^1\frac{t^{n+1}}{1+t}\,dt$ avec $0\le\displaystyle\int_0^1\frac{t^{n+1}}{1+t}\,dt\le\frac1{n+2}$. Donc la somme vaut $\ln2$, avec une erreur d'au plus $\frac1{n+2}$.

## Piège

On ne coupe une somme infinie en deux que si chaque morceau converge. Pour un télescopage, travaille sur la somme partielle $S_N$ et passe à la limite à la fin.
