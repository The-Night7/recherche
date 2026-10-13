---
source: "PREING2-S2/Integration-proba-DS/DS1-2024-2025-V1-Correction_Integration-proba-DS_P2S2_DMaths.pdf"
pages: 3
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Intégration et probabilités — Contrôle continu 1 — Corrigé

CY Tech — 2024/2025 — Semestre 2, PréIng 2 — Mercredi 5 mars. Durée : 60 minutes.

Les documents et les supports électroniques sont interdits. L’épreuve est composée d’exercices indépendants. Le barème est indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte dans la notation.

## Exercice 1 — Intégration par parties (4 points)

1. Soient $f$ et $g$ deux fonctions définies sur $]0,+\infty[$. Énoncer le théorème d’intégration par parties sur cet intervalle en rappelant les hypothèses.
2. Après avoir montré que l’intégrale suivante converge, calculer

$$
I=\int_1^{+\infty}\frac{\ln t}{t^2}\,dt.
$$

### Réponse 1 — Théorème

Si $f$ et $g$ sont de classe $C^1$ sur $]0,+\infty[$ et si leur produit admet des limites finies aux deux bornes,

$$
\lim_{t\to0^+}f(t)g(t)=\ell\in\mathbb R,
\qquad
\lim_{t\to+\infty}f(t)g(t)=\ell'\in\mathbb R,
$$

alors les intégrales $\int_0^{+\infty}f'g$ et $\int_0^{+\infty}fg'$ ont la même nature. Si elles convergent,

$$
\int_0^{+\infty}f(t)g'(t)\,dt
=\bigl[f(t)g(t)\bigr]_0^{+\infty}
-\int_0^{+\infty}f'(t)g(t)\,dt.
$$

> **Coquilles de la source, page 1.** Le signe $=$ manque devant $\ell'$. Dans la formule d’intégration par parties imprimée, la dernière intégrale contient $fg'$ au lieu de $f'g$. Ces deux coquilles sont rectifiées ci-dessus.

### Réponse 2 — Calcul de l’intégrale

On pose $f(t)=\ln t$ et $g(t)=-1/t$. Ces fonctions sont de classe $C^1$ sur $]0,+\infty[$, et

$$
\lim_{t\to1}f(t)g(t)=\lim_{t\to1}\frac{-\ln t}{t}=
\frac{-\ln1}{1}=0,
\qquad
\lim_{t\to+\infty}\frac{-\ln t}{t}=0
$$

car $\ln t=o(t)$ en $+\infty$.

Le théorème d’intégration par parties montre que $I$ a la même nature que

$$
\int_1^{+\infty}f'(t)g(t)\,dt
=\int_1^{+\infty}\frac{-1}{t^2}\,dt.
$$

Cette intégrale converge : c’est une intégrale de Riemann à l’infini, d’exposant $\alpha=2>1$. Donc $I$ converge et

$$
\begin{aligned}
I&=\left[\frac{-\ln t}{t}\right]_1^{+\infty}
-\int_1^{+\infty}\frac{-1}{t^2}\,dt\\
&=0-0-\left[\frac1t\right]_1^{+\infty}
=-0+1=1.
\end{aligned}
$$

## Exercice 2 — Nature d’une intégrale (5 points)

Déterminer la nature de

$$
I=\int_1^{+\infty}\bigl(\ln(t-1)-\ln t\bigr)\,dt.
$$

### Réponse

On pose $f(t)=\ln(t-1)-\ln t$. La fonction $f$ est continue sur $]1,+\infty[$, comme somme de logarithmes continus sur cet intervalle. Il faut étudier la convergence au voisinage de $1$ et de $+\infty$. On sépare les deux problèmes :

$$
I=\int_1^2f(t)\,dt+\int_2^{+\infty}f(t)\,dt.
$$

On commence par le voisinage de l’infini. Le développement limité de $u\mapsto\ln(1+u)$ en zéro donne

$$
f(t)=\ln\left(\frac{t-1}{t}\right)
=\ln\left(1-\frac1t\right)
\underset{t\to+\infty}{\sim}-\frac1t.
$$

La fonction $t\mapsto-1/t$ est continue, non nulle et de signe constant négatif sur $[2,+\infty[$. Le théorème d’équivalence pour les intégrales généralisées montre que $\int_2^{+\infty}f(t)\,dt$ et $\int_2^{+\infty}-1/t\,dt$ ont la même nature. La seconde est une intégrale de Riemann divergente, d’exposant $\alpha=1\leq1$. La première diverge donc aussi. Par définition des intégrales généralisées, **$I$ diverge**.

## Exercice 3 — Changement de variable (4 points)

Déterminer la nature de l’intégrale suivante et, si elle converge, calculer sa valeur :

$$
J=\int_0^{+\infty}\frac{e^{-\sqrt t}}{\sqrt t}\,dt.
$$

### Réponse

On pose $u=\sqrt t$. La fonction $t\mapsto\sqrt t$ est de classe $C^1$, strictement croissante, et envoie $]0,+\infty[$ bijectivement sur lui-même. Par changement de variable, $J$ a la même nature que

$$
\int_0^{+\infty}\frac{e^{-u}}u\,2u\,du
=2\int_0^{+\infty}e^{-u}\,du.
$$

Cette intégrale de référence converge, donc $J$ converge. De plus,

$$
J=2\int_0^{+\infty}e^{-u}\,du
=2\bigl[-e^{-u}\bigr]_0^{+\infty}
=2(-0+1)=2.
$$

## Exercice 4 — Convergence dominée (7 points)

On considère la suite de fonctions $(f_n)_{n\in\mathbb N}$ définies sur $[-\pi/4,\pi/4]$ par

$$
f_n(t)=\frac1{1+(1+\sin t)^n}.
$$

1. Selon la valeur de $t\in[-\pi/4,\pi/4]$, déterminer $\lim_{n\to+\infty}(1+\sin t)^n$.
2. Calculer, si elle existe, la limite

$$
\lim_{n\to+\infty}\int_{-\pi/4}^{\pi/4}f_n(t)\,dt.
$$

### Réponse 1 — Limite de la puissance

La limite dépend du signe de $\sin t$. On distingue trois cas :

- Si $t\in[-\pi/4,0[$, alors $-1<\sin t<0$, donc $|1+\sin t|<1$ et $(1+\sin t)^n\to0$.
- Si $t=0$, alors $\sin t=0$, donc $1+\sin t=1$ et $(1+\sin t)^n\to1$.
- Si $t\in]0,\pi/4]$, alors $0<\sin t<1$, donc $1+\sin t>1$ et $(1+\sin t)^n\to+\infty$.

### Réponse 2 — Limite des intégrales

On applique le théorème de convergence dominée sur $I=[-\pi/4,\pi/4]$.

Pour tout $n\in\mathbb N$, $f_n$ est continue sur $I$ comme quotient de fonctions continues à dénominateur non nul, puisque $1+\sin t\geq0$ sur $I$.

La question précédente montre la convergence simple de $(f_n)$ vers

$$
f(t)=\begin{cases}
1&\text{si }t\in[-\pi/4,0[,\\
\frac12&\text{si }t=0,\\
0&\text{si }t\in]0,\pi/4].
\end{cases}
$$

La limite simple $f$ est continue par morceaux sur $I$.

Pour tout $t\in I$, $1+\sin t\geq0$ et $0\leq f_n(t)\leq1$. On pose $\varphi(t)=1$ : cette fonction est continue et intégrable sur $I$, puisqu’elle est constante sur un intervalle borné. On a donc, pour tout $t\in I$ et tout $n\in\mathbb N$, $|f_n(t)|\leq\varphi(t)$.

Le théorème de convergence dominée assure que $f$ est intégrable et que

$$
\lim_{n\to+\infty}\int_I f_n(t)\,dt
=\int_I f(t)\,dt
=\int_{-\pi/4}^0 1\,dt+\int_0^{\pi/4}0\,dt
=\frac\pi4.
$$

**Remarque de la source.** Le théorème de convergence dominée a été énoncé dans le cours avec l’hypothèse de continuité de la limite simple $f$ sur $I$. Il a néanmoins été mentionné que les résultats de ce chapitre s’étendent aux fonctions continues par morceaux. Pour cet exercice, on aurait aussi pu séparer $I$ en $[-\pi/4,0[$ et $]0,\pi/4]$, appliquer le théorème sur chaque morceau avec une limite simple continue, puis retrouver le résultat par la relation de Chasles.
