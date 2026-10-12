---
source: "PREING2-S1/Series/2627/Annales-20261012/2024-2025/CC3_Séries_2425.pdf"
pages: 2
annee: 2024-2025
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — Examen (2024–2025)

CY Tech — PréIng 2, semestre 1 — lundi 13 janvier 2025.

**Consignes (page 1).** Durée : 120 minutes. Inscrire nom, prénom, numéro de groupe et nombre de pages sur la copie. Documents et supports électroniques interdits. Exercices indépendants. Barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 (4 points, page 1)

On considère $(f_n)$ une suite de fonctions de $I\subset\mathbb R$ dans $\mathbb R$, $(a_n)$ une suite numérique et $R\ge0$.

1. Définir : « $(f_n)$ converge simplement sur $I$ vers $f$ ».
2. Définir : « $(f_n)$ converge uniformément sur $I$ vers $f$ ».
3. Définir : « $\sum_{n\in\mathbb N}f_n$ converge simplement sur $I$ vers $S$ ».
4. Définir : « $\sum_{n\in\mathbb N}f_n$ converge normalement sur $I$ vers $S$ ».
5. À quelles conditions peut-on affirmer que $S=\sum_{n=0}^{+\infty}f_n$ est de classe $C^1$ sur $I$ ?
6. Définir : « le rayon de convergence de la série entière $\sum a_nx^n$ est $R$ ».

## Exercice 2 (6 points, page 1)

On considère la série entière

$$\sum_{n\ge1}\ln\left(1-\frac1{(n+2)^2}\right)x^n.$$

1. Déterminer son rayon de convergence $R$.
2. On fixe $x=1$. Justifier que $\displaystyle\sum_{n\ge1}\ln\left(1-\frac1{(n+2)^2}\right)$ converge.
3. Toujours pour $x=1$, calculer la somme de cette série numérique.

## Exercice 3 (10 points et 2 points bonus, page 2)

Pour tout $n\ge2$ et $x\in\mathbb R_+$, on définit $\displaystyle f_n(x)=\frac{xe^{-nx}}{\ln n}$.

### Question 1

On introduit $u_n=1/(n\ln n)$ pour $n\ge2$ et $g(x)=\ln(\ln x)$ sur $]1,+\infty[$.

(a) Calculer $g'$ sur $]1,+\infty[$.

(b) Montrer que
$$\forall n\ge2,\qquad\sum_{k=2}^nu_k\ge\ln(\ln(n+1))-\ln(\ln2).$$

(c) En déduire la nature de $\sum_{n\ge2}u_n$.

### Question 2

Montrer que $\sum_{n\ge2}f_n$ converge simplement sur $\mathbb R_+$. On note $S$ sa somme.

### Question 3

(a) Pour $n\ge2$, calculer $\|f_n\|_\infty$ sur $\mathbb R_+$.

(b) Montrer que la suite $(f_n)$ converge uniformément vers zéro sur $\mathbb R_+$.

(c) Montrer que $\sum_{n\ge2}f_n$ ne converge pas normalement sur $\mathbb R_+$.

(d) Montrer qu’elle converge normalement sur tout intervalle $[a,+\infty[$ avec $a>0$.

### Question 4

On définit le reste $\displaystyle R_n(x)=\sum_{k=n+1}^{+\infty}f_k(x)$.

> Le PDF écrit $f_n$ sous cette somme indexée par $k$ ; l’indice est corrigé en $f_k$.

(a) Montrer que, pour $x>0$ et $n\ge2$,
$$R_n(x)\le\frac1{\ln(n+1)}\frac{xe^{-(n+1)x}}{1-e^{-x}}.$$

(b) On introduit $\displaystyle h(x)=\frac x{e^x-1}$ sur $\mathbb R_+^*$. Vérifier que, pour tout $x>0$,
$$\frac{xe^{-(n+1)x}}{1-e^{-x}}\le h(x).$$

(c) Montrer que $h$ est bornée sur $\mathbb R_+^*$.

(d) Que peut-on en déduire pour la convergence uniforme de $\sum_{n\ge2}f_n$ ?

### Question 5 et bonus

Montrer que $S$ est continue sur $\mathbb R_+$.

**Bonus.** Montrer que
$$\lim_{t\to+\infty}\int_0^t\sum_{n=2}^{+\infty}f_n(x)\,dx=\sum_{n=2}^{+\infty}\frac1{n^2\ln n}.$$
