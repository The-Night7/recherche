---
source: "PREING2-S1/Series/2627/Annales-20261012/2025-2026/CC3_Séries_2526.pdf"
pages: 2
annee: 2025-2026
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — Contrôle continu 3 (2025–2026)

CY Tech — PréIng 2, semestre 1 — lundi 12 janvier 2026.

**Consignes (page 1).** Durée : 120 minutes. Documents et supports électroniques interdits. Quatre exercices indépendants, sur deux pages. Barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 — Séries numériques (3 points, page 1)

On considère $\displaystyle\sum_{n\ge0}u_n$, avec $u_n=(-1)^n(\sqrt{n^2+1}-n)$.

1. Montrer que $\sum_{n\ge0}u_n$ converge.
2. Donner un équivalent $w_n$ de $u_n$ lorsque $n\to+\infty$.
3. Déterminer la nature de $\sum_{n\ge0}w_n$ et commenter.
4. La série $\sum_{n\ge0}u_n$ est-elle absolument convergente ?

## Exercice 2 — Séries entières (6 points, page 1)

On considère $\displaystyle\sum_{n\ge0}\frac{n^2+1}{n!}x^n$.

1. Déterminer son rayon de convergence $R$.
2. On note $S(x)$ sa somme sur $]-R,R[$.
   (a) Montrer que $\displaystyle S(x)=(x^2+x+1)e^x$ pour tout $x\in]-R,R[$. **Indication :** $n^2+1=n(n-1)+n+1$.
   (b) Calculer $\displaystyle\sum_{n\ge0}\frac{(-1)^n(n^2+1)}{2^nn!}$.
3. Soit $f(x)=(x^2+3x+2)e^x$.
   (a) Vérifier que $S'(x)=f(x)$.
   (b) En déduire un développement en série entière en zéro de $f$.

## Exercice 3 — Suites et séries de fonctions (10 points, page 2)

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

## Exercice 4 — Séries de fonctions (3 points, page 2)

Soit $\displaystyle\sum_{n\ge1}\frac{(-1)^n\cos(nx)}{n^2}$.

1. Montrer qu’elle converge normalement sur $\mathbb R$. Notons $S$ sa somme.
2. La fonction $S$ est-elle continue sur $\mathbb R$ ?
3. On admet, selon le PDF, que
   $$\forall x\in\mathbb R,\qquad S(x)=\frac14\left(x^2-\frac{\pi^2}{3}\right).$$
   En déduire que $\displaystyle\sum_{n=1}^{+\infty}\frac1{n^2}=\frac{\pi^2}{6}$.

> **Erreur de domaine dans la source :** la formule polynomiale est valable sur $[-\pi,\pi]$, puis prolongée par périodicité de période $2\pi$. Elle ne vaut pas pour tout réel : la série définit une fonction périodique. La valeur $x=\pi$ nécessaire à la question est bien dans l’intervalle de validité.
