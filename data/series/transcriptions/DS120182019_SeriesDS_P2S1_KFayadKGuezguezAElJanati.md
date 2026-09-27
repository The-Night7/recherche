---
source: DS1-2018-2019_Series-DS_P2S1_KFayad-KGuezguez-AElJanati.pdf, pages 1 et 2 (corrigé dans DS120182019Correction_SeriesDS_P2S1_DMaths)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (octobre 2018)

Devoir du vendredi 12 octobre 2018 (A. El Janati, K. Fayad, K. Guezguez). Durée 2 heures, appareils électroniques et documents interdits.

## Exercice 1 : Vrai ou faux sur les séries à termes positifs

**Énoncé.** (4 points) Soit $\sum_{n\geq 0} u_n$ une série à termes réels positifs. Répondre par VRAI ou FAUX **en justifiant**.

1. Si la suite $(u_n)_{n\geq 0}$ tend vers $0$, alors la série $\sum_{n\geq 0} u_n$ converge.
2. Si la série $\sum_{n\geq 0} u_n$ diverge, alors la suite $(u_n)_{n\geq 0}$ ne tend pas vers $0$.
3. Si la série $\sum_{n\geq 0} u_n$ diverge, alors la série $\sum_{n\geq 0} u_n^2$ diverge.
4. Si la série $\sum_{n\geq 0} u_n$ converge, alors la série $\sum_{n\geq 0} u_n^2$ converge.

## Exercice 2 : Nature de trois séries

**Énoncé.** (5 points) Étudier la nature des séries numériques de terme général :

1. $u_n = \cos\left(\dfrac{1}{n^2}\right)$, $n \geq 1$.
2. $v_n = \left(\dfrac{2n+1}{2n+5}\right)^{n^2}$, $n \geq 0$.
3. $w_n = \dfrac{(n!)^3}{(3n)!}\,3^n$, $n \geq 0$.

## Exercice 3 : Somme de la série de terme (n+1)/3ⁿ

**Énoncé.** (3 points) Pour $n \in \mathbb{N}$, on pose
$$u_n = \frac{n+1}{3^n}$$

1. Montrer que la série $\sum_{n\geq 0} u_n$ converge. On note $S$ sa somme.
2. Calculer $S$. *Indication :* on pourra trouver un réel $\alpha$ tel que $\frac{1}{3}S = S - \alpha$.

## Exercice 4 : Série définie par une récurrence

**Énoncé.** (8 points) On considère la suite réelle $(u_n)_{n\geq 0}$ définie par la donnée de $u_0 > 0$ et la relation :
$$\forall n \geq 0, \quad u_{n+1} = \frac{n+1}{n+3}\,u_n$$

1. Le but de cette question est d'étudier la nature de la série $\sum_{n\geq 0} u_n$. Pour $n > 0$, on pose
$$v_n = \ln(n^2 u_n) \quad\text{et}\quad w_n = v_{n+1} - v_n$$
    a) Donner le développement limité à l'ordre 2 de $w_n$ et en déduire la nature de la série $\sum_{n>0} w_n$.
    b) Que peut-on dire de la suite $(v_n)_{n>0}$ ? Justifier.
    c) En déduire qu'il existe un réel $L > 0$ (que l'on ne cherchera pas à déterminer) tel que $u_n \underset{+\infty}{\sim} \frac{L}{n^2}$, et conclure.
2. Le but de cette question est de calculer la somme de la série $\sum_{n\geq 0} u_n$.
    a) Déterminer $\lim_{n\to+\infty} n u_n$.
    b) Pour $n \geq 0$, on pose $z_n = (n+1)u_{n+1} - n u_n$. Calculer $\lim_{N\to+\infty} \sum_{n=0}^{N} z_n$.
    c) En utilisant la question précédente et la relation de récurrence vérifiée par la suite $(u_n)_{n\geq 0}$, calculer $\sum_{n=0}^{+\infty} u_n$ en fonction de $u_0$.
