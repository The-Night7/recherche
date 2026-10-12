---
source: "PREING2-S1/Series/2627/Annales-20261012/2025-2026/CC3_Séries_2526_corrigé.pdf"
pages: 7
annee: 2025-2026
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — Contrôle continu 3, corrigé (2025–2026)

CY Tech — PréIng 2, semestre 1 — lundi 12 janvier 2026.

**Consignes (page 1).** Durée : 120 minutes. Documents et supports électroniques interdits. Quatre exercices indépendants. Le corrigé comporte sept pages ; la mention « 2 pages » des consignes concerne le sujet seul. Barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 — Séries numériques (3 points, pages 1–2)

On considère $\displaystyle\sum_{n\ge0}u_n$, avec $u_n=(-1)^n(\sqrt{n^2+1}-n)$.

1. Montrer que $\sum_{n\ge0}u_n$ converge.
2. Donner un équivalent $w_n$ de $u_n$ lorsque $n\to+\infty$.
3. Déterminer la nature de $\sum_{n\ge0}w_n$ et commenter.
4. La série $\sum_{n\ge0}u_n$ est-elle absolument convergente ?

### Réponse (pages 1–2)

1. On applique le théorème spécial des séries alternées :

- Pour $n\ge0$, $\sqrt{n^2+1}\ge\sqrt{n^2}=n$, donc $u_n=(-1)^n|u_n|$.
- Posons $g(x)=\sqrt{x^2+1}-x$ sur $\mathbb R_+$. La fonction est $C^1$ et
  $$g'(x)=\frac x{\sqrt{x^2+1}}-1\le0.$$
  Elle décroît, donc $(|u_n|)=(g(n))$ décroît aussi.
- Pour $n\to+\infty$,
  $$|u_n|=n\left(\sqrt{1+\frac1{n^2}}-1\right)
  =n\left(1+\frac1{2n^2}+o\left(\frac1{n^2}\right)-1\right)\sim\frac1{2n}\longrightarrow0.$$

La série converge par le TSSA.

**Solution alternative donnée par le corrigé :** la quantité conjuguée donne
$$|u_n|=\frac{(\sqrt{n^2+1})^2-n^2}{\sqrt{n^2+1}+n}=\frac1{\sqrt{n^2+1}+n}.$$
Cette expression permet également d’étudier la décroissance et la limite nulle.

2. On obtient $\displaystyle u_n\sim w_n=\frac{(-1)^n}{2n}$.

3. La série $\sum_{n\ge1}w_n$ est un multiple de la série harmonique alternée, donc converge.

**Commentaire du corrigé :** $u_n\sim w_n$ et les deux séries ont ici la même nature, mais on ne peut pas invoquer le théorème d’équivalence, car leurs termes ne gardent pas un signe constant à partir d’un certain rang.

4. On a $|u_n|\sim1/(2n)$. Les termes sont positifs et $\sum1/(2n)$ diverge comme la série harmonique. Le théorème d’équivalence donne la divergence de $\sum|u_n|$. La série $\sum u_n$ ne converge pas absolument.

> **Coquilles corrigées :** la page 1 imprime $n\sqrt{1+1/n^2}-1$ au lieu de $n(\sqrt{1+1/n^2}-1)$. La page 2 annonce un exposant de Riemann $\alpha=1/2$ alors que $w_n=(-1)^n/(2n)$ correspond à $\alpha=1$. Enfin, $w_0$ n’est pas défini par cette formule : on commence sa série à $n=1$, ou on choisit arbitrairement un terme initial fini.

## Exercice 2 — Séries entières (6 points, pages 2–4)

On considère $\displaystyle\sum_{n\ge0}\frac{n^2+1}{n!}x^n$.

1. Déterminer son rayon de convergence $R$.
2. On note $S(x)$ sa somme sur $]-R,R[$.
   (a) Montrer que $\displaystyle S(x)=(x^2+x+1)e^x$ pour tout $x\in]-R,R[$. **Indication :** $n^2+1=n(n-1)+n+1$.
   (b) Calculer $\displaystyle\sum_{n\ge0}\frac{(-1)^n(n^2+1)}{2^nn!}$.
3. Soit $f(x)=(x^2+3x+2)e^x$.
   (a) Vérifier que $S'(x)=f(x)$.
   (b) En déduire un développement en série entière en zéro de $f$.

### Réponse (pages 3–4)

1. Posons $a_n=(n^2+1)/n!$. Les coefficients sont non nuls et
$$\frac{a_{n+1}}{a_n}=\frac{(n+1)^2+1}{(n+1)!}\frac{n!}{n^2+1}
=\frac1{n+1}\frac{(n+1)^2+1}{n^2+1}\longrightarrow0.$$
La règle de d’Alembert donne $R=+\infty$.

> La dernière expression sous la limite dans le PDF remplace le quotient de polynômes par $(n^2+1)/n^2$. Ces expressions ont la même limite ; l’égalité exacte du quotient est rétablie ci-dessus.

2. (a) Pour $n\ge2$,
$$\frac{n^2+1}{n!}=\frac{n(n-1)+n+1}{n!}=\frac1{(n-2)!}+\frac1{(n-1)!}+\frac1{n!}.$$
Les séries obtenues convergent pour tout réel $x$. On écrit
$$\sum_{n=2}^{+\infty}\frac{n^2+1}{n!}x^n
=\sum_{n=2}^{+\infty}\frac{x^n}{(n-2)!}+\sum_{n=2}^{+\infty}\frac{x^n}{(n-1)!}+\sum_{n=2}^{+\infty}\frac{x^n}{n!}.$$
En ajoutant les termes de rang zéro et un,
$$\begin{aligned}
S(x)&=1+2x+\sum_{n=2}^{+\infty}\frac{n^2+1}{n!}x^n\\
&=\sum_{n=2}^{+\infty}\frac{x^n}{(n-2)!}
+\left(x+\sum_{n=2}^{+\infty}\frac{x^n}{(n-1)!}\right)
+\left(1+x+\sum_{n=2}^{+\infty}\frac{x^n}{n!}\right)\\
&=\sum_{n=2}^{+\infty}\frac{x^n}{(n-2)!}+\sum_{n=1}^{+\infty}\frac{x^n}{(n-1)!}+\sum_{n=0}^{+\infty}\frac{x^n}{n!}\\
&=\sum_{n=0}^{+\infty}\frac{x^{n+2}}{n!}+\sum_{n=0}^{+\infty}\frac{x^{n+1}}{n!}+\sum_{n=0}^{+\infty}\frac{x^n}{n!}\\
&=x^2e^x+xe^x+e^x=(x^2+x+1)e^x.
\end{aligned}$$

(b) On reconnaît $x=-1/2\in\mathbb R=]-R,R[$ :
$$\sum_{n=0}^{+\infty}\frac{(-1)^n(n^2+1)}{2^nn!}=S(-1/2)
=\left(\frac14-\frac12+1\right)e^{-1/2}=\frac34e^{-1/2}.$$

3. (a) La fonction $S$ est $C^1$ sur $\mathbb R$ et
$$S'(x)=(2x+1)e^x+(x^2+x+1)e^x=(x^2+3x+2)e^x=f(x).$$

(b) On peut dériver terme à terme une série entière à l’intérieur de son disque de convergence. Pour tout $x\in\mathbb R$,
$$f(x)=\sum_{n=1}^{+\infty}na_nx^{n-1}
=\sum_{n=1}^{+\infty}\frac{n^2+1}{(n-1)!}x^{n-1}
=\sum_{n=0}^{+\infty}\frac{(n+1)^2+1}{n!}x^n.$$
Le développement cherché est donc $\sum b_nx^n$ avec $\displaystyle b_n=\frac{(n+1)^2+1}{n!}$.

## Exercice 3 — Suites et séries de fonctions (10 points, pages 4–6)

Pour tout $n\ge2$, on définit $f_n:\mathbb R_+\to\mathbb R_+$ par

$$f_n(x)=\frac{(1+x)e^{-x/n^2}}{n(n^2-1)}.$$

### Question 1 — Étude de la suite

(a) Déterminer le domaine de convergence de $(f_n)_{n\ge2}$.

(b) Étudier la convergence uniforme de cette suite sur son domaine de convergence.

### Question 2 — Étude de la série

(a) Déterminer le domaine de convergence de $\sum_{n\ge2}f_n$. On note $S$ sa somme.

(b) Calculer $S(0)$.

(c) Étudier la convergence normale de $\sum_{n\ge2}f_n$ sur $\mathbb R_+$.

(d) Montrer que cette série converge normalement sur tout $[0,A]$ avec $A>0$.

### Question 3 — Intégrales

Pour $n\ge2$, on note $\displaystyle I_n=\int_0^1f_n(x)\,dx$.

(a) Montrer que
$$I_n=\frac n{n^2-1}\left(n^2+1-e^{-1/n^2}(n^2+2)\right).$$

(b) Étudier la nature de $\sum_{n\ge2}I_n$.

(c) Justifier que cette nature est cohérente avec l’étude de $\sum_{n\ge2}f_n$ réalisée précédemment.

### Réponse à la question 1 (pages 4–5)

(a) En zéro, $f_n(0)=1/[n(n^2-1)]\to0$. Pour $x>0$ fixé, $e^{-x/n^2}\to1$ et $f_n(x)\to0$. Le domaine de convergence est $\mathbb R_+$ et la limite simple est nulle.

> À $x=0$, le corrigé conserve par inadvertance un facteur $1+x$ dans le calcul ; il vaut $1$.

(b) Pour $n\ge2$, $f_n$ est $C^1$ et
$$f_n'(x)=\frac{e^{-x/n^2}+(1+x)(-1/n^2)e^{-x/n^2}}{n(n^2-1)}
=\left(1-\frac{1+x}{n^2}\right)\frac{e^{-x/n^2}}{n(n^2-1)}.$$
Le seul point critique est $x=n^2-1$. Les variations sont :

| Position | $x=0$ | $0<x<n^2-1$ | $x=n^2-1$ | $x>n^2-1$ | $x\to+\infty$ |
| --- | --- | --- | --- | --- | --- |
| Signe de $f_n'$ | $+$ | $+$ | $0$ | $-$ | |
| $f_n$ | $\frac1{n(n^2-1)}$ | croît | $\frac{n^2e^{-1+1/n^2}}{n(n^2-1)}$ | décroît | $0$ |

Comme $1\le n^2e^{-1}$ pour $n\ge2$, le maximum est celui du point critique et
$$\sup_{x\in\mathbb R_+}|f_n(x)|=\frac{n^2e^{-1+1/n^2}}{n(n^2-1)}\longrightarrow0.$$
La suite converge uniformément vers zéro sur $\mathbb R_+$.

> **Coquille du tableau source :** le maximum y omet le facteur $e^{1/n^2}$ ; la formule juste figure dans le texte sous le tableau et est reprise ici.

### Réponse à la question 2 (pages 5–6)

(a) Pour $x\ge0$ fixé, $f_n(x)\sim(1+x)/n^3$. Les termes sont positifs et la série de Riemann d’exposant $3$ converge. Le domaine de convergence simple de la série est $\mathbb R_+$.

(b) On calcule
$$S(0)=\sum_{n=2}^{+\infty}\frac1{n(n^2-1)}.$$
La décomposition en éléments simples est
$$\frac1{n(n^2-1)}=\frac{1/2}{n-1}-\frac1n+\frac{1/2}{n+1}.$$
Par télescopage,
$$\begin{aligned}
\sum_{k=2}^n\frac1{k(k^2-1)}
&=\frac12\sum_{k=2}^n\frac1{k-1}-\sum_{k=2}^n\frac1k+\frac12\sum_{k=2}^n\frac1{k+1}\\
&=\frac12\sum_{k=1}^{n-1}\frac1k-\sum_{k=2}^n\frac1k+\frac12\sum_{k=3}^{n+1}\frac1k\\
&=\frac12\left(1+\frac12\right)-\left(\frac12+\frac1n\right)+\frac12\left(\frac1n+\frac1{n+1}\right)\\
&=\frac14+O(1/n).
\end{aligned}$$
Donc $\boxed{S(0)=1/4}$.

> La première somme du corrigé est indexée par $k$ mais contient $1/[n(n^2-1)]$ ; le terme est corrigé en $1/[k(k^2-1)]$. La séparation des bornes ci-dessus est faite pour $n$ assez grand.

(c) D’après la question 1(b),
$$\|f_n\|_{\infty,\mathbb R_+}=\frac{n^2e^{-1+1/n^2}}{n(n^2-1)}\sim\frac{e^{-1}}n.$$
La série des normes diverge par comparaison à la série harmonique : il n’y a pas convergence normale sur $\mathbb R_+$.

(d) Fixons $A>0$. Pour $n$ assez grand, $n^2-1>A$, donc $f_n$ croît sur $[0,A]$ et
$$\|f_n\|_{\infty,[0,A]}=f_n(A)=\frac{(1+A)e^{-A/n^2}}{n(n^2-1)}\sim\frac{1+A}{n^3}.$$
La série des normes converge, par comparaison à une série de Riemann d’exposant $3$. La série converge normalement sur $[0,A]$.

### Réponse à la question 3 (page 6)

(a) L’intégration par parties donne
$$\begin{aligned}
I_n&=\frac1{n(n^2-1)}\int_0^1(1+x)e^{-x/n^2}\,dx\\
&=\frac1{n(n^2-1)}\left(\left[(1+x)\frac{e^{-x/n^2}}{-1/n^2}\right]_0^1-\int_0^1\frac{e^{-x/n^2}}{-1/n^2}\,dx\right)\\
&=\frac1{n(n^2-1)}\left(n^2-2n^2e^{-1/n^2}+n^2\left[\frac{e^{-x/n^2}}{-1/n^2}\right]_0^1\right)\\
&=\frac1{n(n^2-1)}\left(n^2-2n^2e^{-1/n^2}+n^4(1-e^{-1/n^2})\right)\\
&=\frac{n^2}{n(n^2-1)}\left(1-2e^{-1/n^2}+n^2-n^2e^{-1/n^2}\right)\\
&=\frac n{n^2-1}\left(1+n^2-e^{-1/n^2}(2+n^2)\right).
\end{aligned}$$

(b) En développant l’exponentielle,
$$\begin{aligned}
I_n&=\frac n{n^2-1}\left[n^2+1-\left(1-\frac1{n^2}+\frac1{2n^4}+o(n^{-4})\right)(n^2+2)\right]\\
&=\frac n{n^2-1}\left[n^2+1-\left(n^2+1-\frac3{2n^2}+o(n^{-2})\right)\right]\\
&\sim\frac1n\frac3{2n^2}=\frac3{2n^3}.
\end{aligned}$$
Les $I_n$ sont positifs ; la série de Riemann d’exposant $3$ converge. Donc $\sum_{n\ge2}I_n$ converge.

(c) La question 2(d), appliquée à $A=1$, donne la convergence normale, donc uniforme, de $\sum f_n$ sur $[0,1]$. Chaque $f_n$ y est continue. Le théorème d’interversion somme-intégrale assure alors la convergence de $\sum_{n\ge2}\int_0^1f_n(x)\,dx$, conformément à la question précédente.

> La réponse source numérote ces trois dernières étapes « 3, 4, 5 » au lieu de 3(a), 3(b), 3(c), et écrit parfois $n\in\mathbb N$ sous les sommes. Toutes les fonctions de cet exercice sont définies pour $n\ge2$.

## Exercice 4 — Séries de fonctions (3 points, page 7)

Soit $\displaystyle\sum_{n\ge1}\frac{(-1)^n\cos(nx)}{n^2}$.

1. Montrer qu’elle converge normalement sur $\mathbb R$. Notons $S$ sa somme.
2. La fonction $S$ est-elle continue sur $\mathbb R$ ?
3. On admet, selon le PDF, que
   $$\forall x\in\mathbb R,\qquad S(x)=\frac14\left(x^2-\frac{\pi^2}{3}\right).$$
   En déduire que $\displaystyle\sum_{n=1}^{+\infty}\frac1{n^2}=\frac{\pi^2}{6}$.

> **Erreur de domaine dans la source :** la formule polynomiale est valable sur $[-\pi,\pi]$, puis prolongée par périodicité de période $2\pi$. Elle ne vaut pas pour tout réel : la série définit une fonction périodique. La valeur $x=\pi$ nécessaire à la question est bien dans l’intervalle de validité.

### Réponse (page 7)

1. Posons $f_n(x)=(-1)^n\cos(nx)/n^2$. Le cosinus est borné entre $-1$ et $1$, donc
$$\|f_n\|_{\infty,\mathbb R}\le\frac1{n^2}.$$
La série de Riemann d’exposant $2$ converge. Par majoration, $\sum\|f_n\|_\infty$ converge : la série de fonctions converge normalement sur $\mathbb R$.

2. Chaque $f_n$ est continue. La convergence normale implique la convergence uniforme sur $\mathbb R$ ; le théorème d’interversion somme-limite donne la continuité de $S$ sur $\mathbb R$.

3. En $x=\pi$, $\cos(n\pi)=(-1)^n$, d’où
$$S(\pi)=\sum_{n=1}^{+\infty}\frac{(-1)^n\cos(n\pi)}{n^2}=\sum_{n=1}^{+\infty}\frac1{n^2}.$$
En utilisant la valeur admise en $\pi$,
$$\sum_{n=1}^{+\infty}\frac1{n^2}=\frac14\left(\pi^2-\frac{\pi^2}3\right)=\frac14\frac{2\pi^2}3=\frac{\pi^2}6.$$
La réserve sur le domaine de la formule admise s’applique aussi au corrigé, qui répète « pour tout $x\in\mathbb R$ ».
