---
source: DS120232024V1_SeriesDS_P2S1_DMaths.pdf (scan)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (2023/2024, mardi 24 octobre)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1

Soit $q \in \mathbb{R}$, à quelle condition sur $q$ la série $\sum_{n\geq 0} q^n$ converge-t-elle ? Le démontrer, et calculer sa valeur.

## Exercice 2

L'objectif de cet exercice est de calculer
$$S = \sum_{k=1}^{+\infty} \frac{2k^2-1}{k^2(k+1)^2}$$

1. Montrer que l'égalité ci-dessus définit bien un réel $S \in \mathbb{R}$.
2. Montrer que $\dfrac{2k^2-1}{k^2(k+1)^2} = \dfrac{2k-1}{k^2} - \dfrac{2k+1}{(k+1)^2}$.
3. En déduire la valeur de $S \in \mathbb{R}$.

## Exercice 3

Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\geq 1} n\ln\left(1+\frac{1}{n}\right) - \cos\left(\frac{1}{\sqrt{n}}\right)$
2. $\displaystyle\sum_{n\geq 1} \ln\left(1+\frac{(-1)^n}{2n+1}\right)$
3. $\displaystyle\sum_{n\geq 1} \left(\cos\left(\frac{1}{n}\right)\right)^{n^3}$
4. $\displaystyle\sum_{n\geq 0} \left(\frac{4n+1}{3n+2}\right)^n$

## Exercice 4

Le but de cet exercice est de montrer $\ln(n!) \sim n\ln(n)$. Pour tout $k, n \in \mathbb{N}^*$, on pose $u_k := \ln(k)$ et $S_n := \sum_{k=1}^{n} u_k$.

1. Montrer que : $\forall n \in \mathbb{N}^*,\ \int_1^n \ln(t)\,dt \leq S_n \leq \int_1^{n+1} \ln(t)\,dt$.
2. En déduire : $n\ln(n) \leq S_n \leq (n+1)\ln(n+1)$ (on pourra effectuer une intégration par parties pour calculer les intégrales).
3. Montrer que $S_n = \ln(n!)$ et en déduire $\ln(n!) \sim n\ln(n)$.
