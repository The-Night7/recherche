---
source: "PREING2-S1/Series/2627/Annales-20261012/2025-2026/CC1_Series_2526_corrigé.pdf"
pages: 4
annee: 2025-2026
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — Contrôle continu 1, corrigé (2025–2026)

CY Tech — PréIng 2, semestre 1 — jeudi 16 octobre. Pages 1 à 4. Les réponses ci-dessous proviennent du corrigé fourni.

**Consignes.** Durée : 90 minutes. Documents et supports électroniques interdits. Exercices indépendants. Barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 (3 points)

1. Donner la définition de série alternée.
2. (a) Énoncer la règle de d’Alembert pour les séries numériques à termes quelconques.
   (b) Étudier la nature de $\displaystyle\sum_{n\ge1}\frac{(-2)^n}{n(n+1)}$.

### Réponse (page 1)

1. Une série $\sum_{n\in\mathbb N}u_n$ est alternée s’il existe $n_0$ tel que, pour tout $n\ge n_0$, $u_n=(-1)^n|u_n|$, ou bien $u_n=(-1)^{n+1}|u_n|$.

2. (a) Soit $\sum u_n$ avec $u_n\ne0$ à partir d’un certain rang. Pour $\ell=\lim_{n\to\infty}|u_{n+1}/u_n|$ :

- Si $\ell<1$, la série converge.
- Si $\ell>1$ ou $\ell=+\infty$, elle diverge.
- Si $\ell=1$, on ne peut pas conclure par cette règle.

(b) Pour tout $n\ge1$, $u_n\ne0$ et
$$\left|\frac{u_{n+1}}{u_n}\right|=\frac{2^{n+1}}{(n+1)(n+2)}\frac{n(n+1)}{2^n}=\frac{2n}{n+2}\longrightarrow2>1.$$
La série diverge.

## Exercice 2 (8 points)

Étudier la nature des séries numériques suivantes :

1. $\displaystyle\sum_{n\ge1}\frac{n^2-1}{(n+1)^2\sqrt n}$.
2. $\displaystyle\sum_{n\ge1}\frac{n^{\sqrt n}}{(\sqrt n)^n}$.
3. $\displaystyle\sum_{n\ge1}\frac{\ln n}{n^2+n}$.
4. $\displaystyle\sum_{n\ge1}(-1)^n\ln\left(1+\frac1n\right)$.

### Réponse (page 2)

1. Par équivalence,
$$u_n=\frac{n^2-1}{(n+1)^2\sqrt n}\sim\frac{n^2}{n^2\sqrt n}=\frac1{\sqrt n}.$$
Le terme de comparaison est positif. La série de Riemann d’exposant $\alpha=1/2<1$ diverge ; il en est de même de $\sum u_n$.

2. On applique la règle de Cauchy :
$$\sqrt[n]{|u_n|}=\frac{n^{1/\sqrt n}}{\sqrt n}=\frac{e^{\ln n/\sqrt n}}{\sqrt n}\longrightarrow0<1,$$
car $e^{\ln n/\sqrt n}\to e^0=1$. La série converge.

3. Le lemme de Riemann avec $\alpha=3/2>1$ donne
$$n^{3/2}u_n=\frac{n^{3/2}\ln n}{n^2+n}\sim\frac{\ln n}{\sqrt n}\longrightarrow0.$$
La série converge. On pouvait aussi raisonner par équivalence en reconnaissant une série de Bertrand.

4. Puisque $\ln(1+1/n)\ge0$, on a $u_n=(-1)^n|u_n|$. La suite des valeurs absolues est décroissante : $1+1/n$ décroît et la fonction logarithme est croissante. De plus, $|u_n|\to\ln1=0$. Le théorème spécial des séries alternées donne la convergence.

> **Précision rédactionnelle :** la source invoque la « suite $(\ln n)$ croissante » dans la composition ; c’est la croissance de la fonction $\ln$ qui est utilisée.

## Exercice 3 (4 points)

On considère $\sum_{n\ge2}u_n$, où $\displaystyle u_n=\frac{3n}{(n^2-1)(n+2)}$ pour $n\ge2$.

1. Montrer que cette série converge.
2. Calculer sa somme.

### Réponse (page 3)

1. On a
$$u_n=\frac{3n}{(n^2-1)(n+2)}\sim\frac3{n^2}.$$
Les termes sont positifs et la série de Riemann d’exposant $2>1$ converge. Le théorème d’équivalence donne donc la convergence de $\sum_{n\ge2}u_n$.

2. Pour tout $k\ge2$, la décomposition en éléments simples est
$$u_k=\frac{1/2}{k-1}+\frac{3/2}{k+1}-\frac2{k+2}.$$
On somme et on change les indices pour faire apparaître le télescopage :
$$\begin{aligned}
\sum_{k=2}^n u_k
&=\frac12\sum_{k=2}^n\frac1{k-1}+\frac32\sum_{k=2}^n\frac1{k+1}-2\sum_{k=2}^n\frac1{k+2}\\
&=\frac12\sum_{k=1}^{n-1}\frac1k+\frac32\sum_{k=3}^{n+1}\frac1k-2\sum_{k=4}^{n+2}\frac1k\\
&=\frac12\left(1+\frac12+\frac13\right)+\frac32\left(\frac13+\frac1n+\frac1{n+1}\right)
-2\left(\frac1n+\frac1{n+1}+\frac1{n+2}\right)
+\left(\frac12+\frac32-2\right)\sum_{k=4}^{n-1}\frac1k\\
&=\frac{17}{12}+O\left(\frac1n\right).
\end{aligned}$$
En passant à la limite :
$$\boxed{\sum_{n=2}^{+\infty}u_n=\frac{17}{12}.}$$

> **Coquille corrigée :** la première ligne du PDF imprime $1/(n+2)$ dans la dernière somme ; il faut $1/(k+2)$. La séparation des bornes intermédiaires est comprise pour $n$ assez grand.

## Exercice 4 (5 points)

On considère $\sum_{n\ge1}u_n$, où $\displaystyle u_n=\frac2{n^3+n}$ pour $n\ge1$.

1. Déterminer sa nature.
2. Montrer que, pour tout $n\ge2$,
   $$\int_2^{n+1}\frac2{x+x^3}\,dx\le\sum_{k=2}^nu_k\le\int_1^n\frac2{x+x^3}\,dx.$$
3. Calculer la dérivée sur $\mathbb R_+^*$ de $\displaystyle F(x)=\ln\left(1+\frac1{x^2}\right)$.
4. En déduire l’encadrement
   $$\ln\frac54\le\sum_{n=2}^{+\infty}u_n\le\ln2.$$

### Réponse (page 4)

1. On a $u_n=2/(n^3+n)\sim2/n^3$. Les termes sont positifs et la série de Riemann d’exposant $3>1$ converge. La série converge donc, qu’on la fasse commencer à $n=1$ ou $n=2$.

2. Posons $f(x)=2/(x^3+x)$. Sur $\mathbb R_+^*$, $x\mapsto x^3+x$ est croissante et son inverse multiplicatif est décroissant. On peut aussi calculer
$$f'(x)=-\frac{2(3x^2+1)}{(x^3+x)^2}\le0.$$
Pour $k\ge2$ : $u_k=f(k)\le f(x)$ sur $[k-1,k]$ et $f(x)\le f(k)=u_k$ sur $[k,k+1]$. En intégrant,
$$\int_k^{k+1}f(x)\,dx\le u_k\le\int_{k-1}^kf(x)\,dx.$$
En sommant et par Chasles,
$$\sum_{k=2}^n\int_k^{k+1}f=\int_2^{n+1}f\le\sum_{k=2}^nu_k\le\sum_{k=2}^n\int_{k-1}^kf=\int_1^nf.$$

> **Correction de domaine :** le PDF dit « décroissante sur $\mathbb R$ » et « dérivable sur $\mathbb R$ ». La fonction n’est pas définie en zéro ; seul $\mathbb R_+^*$ est nécessaire ici.

3. Pour $x>0$,
$$F'(x)=-\frac2{x^3}\frac1{1+1/x^2}=-\frac2{x^3+x}=-f(x).$$

4. On obtient, pour $n\ge2$,
$$\left[-\ln\left(1+\frac1{x^2}\right)\right]_2^{n+1}
\le\sum_{k=2}^nu_k\le
\left[-\ln\left(1+\frac1{x^2}\right)\right]_1^n,$$
soit
$$\ln\frac54-\ln\left(1+\frac1{(n+1)^2}\right)
\le\sum_{k=2}^nu_k\le\ln2-\ln\left(1+\frac1{n^2}\right).$$
La série étant convergente, le passage à la limite donne
$$\boxed{\ln\frac54\le\sum_{n=2}^{+\infty}u_n\le\ln2.}$$
