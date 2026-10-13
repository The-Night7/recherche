---
source: "PREING2-S1/Series/2627/Annales-20261012/2024-2025/CC1_SujetC_2425.pdf"
pages: 1
annee: 2024-2025
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — DS1, sujet C (2024–2025)

CY Tech — PréIng 2, semestre 1 — mercredi 16 octobre. Page 1.

**Consignes.** Durée : 60 minutes. Documents et supports électroniques interdits. Exercices indépendants. Barème indicatif, sur 18 points, complété par 2 points de QCM en cours magistral. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 (3 points)

Soient $\sum u_n$ et $\sum v_n$ deux séries à termes positifs.

1. On suppose qu’il existe $\alpha>1$ tel que $\displaystyle\lim_{n\to+\infty}n^\alpha u_n=0$. Montrer que $\sum u_n$ converge.
2. On suppose qu’il existe $\alpha\le1$ tel que $\displaystyle\lim_{n\to+\infty}n^\alpha v_n=+\infty$. Montrer que $\sum v_n$ diverge.

## Exercice 2 (5 points)

Déterminer la nature des séries :

1. $\displaystyle\sum_{n\ge1}\sin\left(\frac{(-1)^{n+1}}{\sqrt n}\right)$.
2. $\displaystyle\sum_{n\ge0}\left(\frac{4n+3}{3n+1}\right)^n$.
3. $\displaystyle\sum_{n\ge0}\left(\frac n{n+1}\right)^{n^2}$.

> La troisième expression donne $0^0$ au rang zéro, sans convention précisée. On peut commencer à $n=1$ pour étudier sa nature.

## Exercice 3 (4 points)

On considère $\displaystyle u_n=\frac{2n+2}{n^3+4n^2+n-6}$.

1. Déterminer la nature de $\displaystyle\sum_{n\ge1}u_n$.
2. Calculer $\displaystyle\sum_{n=1}^{+\infty}u_n$.

On pourra chercher $A,B,C\in\mathbb R$ tels que $\displaystyle u_n=\frac A{n-1}+\frac B{n+2}+\frac C{n+3}$.

> **Erreur de l’énoncé :** le dénominateur est $(n-1)(n+2)(n+3)$ ; le terme $u_1$ n’est pas défini. Les séries écrites dans le PDF doivent commencer au moins à $n=2$. Aucun premier indice corrigé n’est fourni par la source.

## Exercice 4 (6 points)

On considère $u_n=2ne^{-n^2}$ et ses sommes partielles $\displaystyle S_n=\sum_{k=1}^nu_k$.

1. Déterminer la nature de $\displaystyle\sum_{n\ge1}u_n$.
2. Montrer que
   $$\forall n\in\mathbb N^*,\qquad\int_1^{n+1}2te^{-t^2}\,dt\le S_n\le\int_0^n2te^{-t^2}\,dt.$$
3. En déduire que $\displaystyle\frac1e\le\sum_{n=1}^{+\infty}u_n\le1$.

> **Coquilles et erreur de la source :** le PDF écrit $\sum_{n=1}^n u_k$ ; l’indice est rétabli en $k$. La majoration de la question 2 est fausse pour $n=1$ : $S_1=2/e>1-1/e=\int_0^1 2te^{-t^2}\,dt$. L’énoncé est conservé ; la conclusion finale nécessite donc une justification distincte de cet encadrement tel qu’il est formulé.
