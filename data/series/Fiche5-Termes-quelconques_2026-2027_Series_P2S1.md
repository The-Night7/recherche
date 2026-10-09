# Fiche 5 : Séries à termes quelconques

CC1 Séries, jeudi 15 octobre 2026.

## Les réflexes, dans l'ordre

1. **Convergence absolue d'abord.** Teste $\sum|u_n|$ avec les outils de la fiche 3. Exemple : $\left|\dfrac{\cos n}{n^3+n}\right|\le\dfrac1{n^3}$, donc la série converge absolument.
2. **CSSA** (critère spécial des séries alternées), si la décroissance est évidente.
3. **Développement limité du terme général**, si la décroissance est fausse ou pénible à vérifier, puis étude de chaque morceau.

## Critère spécial des séries alternées (Leibniz)

Soit $(a_n)$ une suite positive, **décroissante**, de limite nulle. Alors $\sum(-1)^na_n$ converge. De plus :

- sa somme vérifie $S_{2n+1}\le S\le S_{2n}$ ;
- son reste vérifie $|R_n|\le a_{n+1}$.

Valeur approchée de $S$ à $10^{-3}$ près : cherche $n$ tel que $a_{n+1}\le10^{-3}$.

Démonstration : $(S_{2n})$ et $(S_{2n+1})$ sont adjacentes, car $S_{2n+2}-S_{2n}=a_{2n+2}-a_{2n+1}\le0$, $S_{2n+3}-S_{2n+1}=a_{2n+2}-a_{2n+3}\ge0$ et $S_{2n+1}-S_{2n}=-a_{2n+1}\to0$.

## Série de Riemann alternée

$\sum\dfrac{(-1)^n}{n^\alpha}$ converge $\iff\alpha>0$. Elle converge absolument pour $\alpha>1$ et elle est semi-convergente pour $0<\alpha\le1$.

## Exemple à savoir refaire

$$\frac{(-1)^n}{\sqrt n+(-1)^n}=\frac{(-1)^n}{\sqrt n}\cdot\frac{1}{1+\frac{(-1)^n}{\sqrt n}}=\underbrace{\frac{(-1)^n}{\sqrt n}}_{\text{converge (alternée)}}-\underbrace{\frac1n}_{\text{diverge}}+\underbrace{O\!\left(\frac{1}{n^{3/2}}\right)}_{\text{converge absolument}}$$

Convergente + divergente + convergente : la série **diverge**. Pourtant son terme général est équivalent à $\frac{(-1)^n}{\sqrt n}$, qui donne une série convergente.

Autre exemple : $\dfrac{(-1)^n}{n+(-1)^n}=\dfrac{(-1)^n}{n}-\dfrac1{n^2}+O\!\left(\dfrac1{n^3}\right)$, trois séries convergentes, donc la série converge. Elle est semi-convergente.

Troisième exemple (TD1, exercice 8) : $\ln\!\left(1+\dfrac{(-1)^n}{\sqrt n}\right)=\dfrac{(-1)^n}{\sqrt n}-\dfrac1{2n}+O\!\left(\dfrac1{n^{3/2}}\right)$, donc la série diverge.

## Piège

Le critère d'équivalence est faux pour les séries dont le terme change de signe. Pousse le développement jusqu'à un reste en $O$ d'une série absolument convergente.

Le CSSA ne s'applique pas directement quand $(a_n)$ n'est pas clairement décroissante, par exemple $a_n=\dfrac1{n^{3/4}+n^{1/4}\sin(\pi^n)}$.

## À connaître si vu en CM

**Sommation d'Abel.** Si $(a_n)$ est décroissante de limite nulle et si les sommes partielles de $\sum b_n$ sont bornées, alors $\sum a_nb_n$ converge. Le CSSA est le cas $b_n=(-1)^n$. Application : $\sum\dfrac{\sin(n\theta)}{\sqrt{n+1}}$ converge pour tout $\theta$, avec $\left|\sum_{k=0}^n\sin(k\theta)\right|\le\dfrac1{|\sin(\theta/2)|}$ pour $\theta\notin\pi\mathbb{Z}$.

**Produit de Cauchy.** On pose $c_n=\sum_{k=0}^na_kb_{n-k}$. Si $\sum a_n$ et $\sum b_n$ convergent **absolument**, alors $\sum c_n$ converge absolument et

$$\sum_{n\ge0}c_n=\left(\sum_{n\ge0}a_n\right)\left(\sum_{n\ge0}b_n\right)$$

Exemple : $e^{a}e^{b}=e^{a+b}$. Si les séries convergent seulement, le produit peut diverger : contre-exemple $a_i=b_i=\dfrac{(-1)^i}{\sqrt{1+i}}$.
