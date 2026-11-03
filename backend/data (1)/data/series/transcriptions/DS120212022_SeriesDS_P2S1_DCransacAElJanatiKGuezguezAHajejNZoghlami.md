---
source: DS1-2021-2022_Series-DS_P2S1_DCransac-AElJanati-KGuezguez-AHajej-NZoghlami.pdf, page 1 (corrigé dans DS120212022Correction_SeriesDS_P2S1_DCransacAElJanatiKGuezguezAHajejNZoghlami)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (novembre 2021)

Devoir du vendredi 12 novembre 2021 (D. Cransac, A. El Janati, K. Guezguez, A. Hajej, N. Zoghlami). Durée 1 h 30, appareils électroniques et documents interdits.

## Exercice 1 : Nature de cinq séries

**Énoncé.** (8 points)

A) Déterminer la nature de convergence des séries de terme général :
$$u_n = \left(\frac{1}{3}\right)^{\sqrt{n}}\ ; \qquad v_n = 2\ln(n^3+1) - \ln(n^2+1)$$

B) Déterminer la nature de convergence des séries de terme général :
$$a_n = (-1)^n\sin\left(\frac{1}{n}\right)\ ; \qquad b_n = \left(1 + \frac{1}{n^3}\right)^n - 1\ ; \qquad c_n = \ln n \times b_n$$

## Exercice 2 : Deux calculs de sommes

**Énoncé.** (5,5 points)

1. 
    a) Montrer que, pour tout entier naturel $k$, $k^3 = k + 3k(k-1) + k(k-1)(k-2)$.
    b) Montrer que la série $\sum_{k\geq 0} \frac{k^3}{k!}$ est convergente et déterminer sa somme.
2. Montrer que la série $\sum_{n\geq 2} u_n$ où $u_n = \dfrac{1}{\sqrt{n-1}} - \dfrac{2}{\sqrt{n}} + \dfrac{1}{\sqrt{n+1}}$ est convergente et déterminer sa somme.

> **Erreur corrigée :** le sujet imprimé écrit $u_n = \frac{1}{\sqrt{n-1}} - \frac{2}{n} + \frac{1}{\sqrt{n+1}}$ ; avec $\frac{2}{n}$ la série diverge ($u_n \sim \frac{2}{\sqrt n}$). Le corrigé utilise $\frac{2}{\sqrt n}$, qui est la version voulue.

## Exercice 3 : Suite récurrente uₙ₊₁ = uₙ − uₙ²

**Énoncé.** (6,5 points) Soit $a \in \,]0, 1[$ et $(u_n)_{n\in\mathbb{N}}$ la suite définie par :
$$\begin{cases} \forall n \in \mathbb{N},\ u_{n+1} = u_n - u_n^2 \\ u_0 = a \end{cases}$$

1. Montrer que : $\forall n \in \mathbb{N}$, $u_n \in \,]0, 1[$.
2. Montrer que la suite $(u_n)_{n\in\mathbb{N}}$ est convergente. Quelle est sa limite ?
3. Montrer que la série $\sum_{n\geq 0} u_n^2$ est convergente et déterminer sa somme.
4. Montrer que la série $\sum_{n\geq 0}\ln\left(\frac{u_{n+1}}{u_n}\right)$ est divergente (on pourra utiliser la définition).
5. Quelle est la nature de la série $\sum_{n\geq 0} u_n$ ?
