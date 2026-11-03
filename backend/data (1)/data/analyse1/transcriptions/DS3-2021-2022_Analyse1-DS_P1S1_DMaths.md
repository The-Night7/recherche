# Analyse 1 — DS3 2021–2022, sujet

> Source : `PREING1-S1/Analyse1-DS/DS3-2021-2022_Analyse1-DS_P1S1_DMaths.pdf`, 2 pages (PDF natif).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale des deux pages ; formules restituées en LaTeX. L’extraction brute `DS3-2021-2022_Analyse1-DS_P1S1_DMaths.txt` n’a pas servi de référence.

**Préing 1 — Devoir Surveillé 3**

| Matière | Date | Durée | Nombre de pages |
| --- | --- | --- | --- |
| Mathématiques - Analyse | Lundi 24 janvier 2022 | 1 h 30 | 2 |

L’usage de tout appareil électronique est interdit.

***Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.*** *Le sujet comporte cinq exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.*

## Exercice 1

Calculer les limites suivantes :

1. $\displaystyle\lim_{x\to+\infty}\sqrt{x(x^2+\sqrt x)}-\sqrt{x^3}$.
2. $\displaystyle\lim_{x\to1}\frac{1-x^2}{1-x^3}$.
3. $\displaystyle\lim_{x\to0}\frac{(e^x-1)}{5x+x^2}$.
4. $\displaystyle\lim_{x\to+\infty}\frac{E(\ln(x))}{x}$.
   Où $E(\ln(x))$ désigne la partie entière de $\ln(x)$.

## Exercice 2

1. Donner la définition exacte, avec les quantificateurs, des propositions suivantes :
   1. a) $\displaystyle\lim_{x\to a}f(x)=\ell$, où $a$ et $\ell$ sont des nombres réels.
   2. b) $\displaystyle\lim_{x\to-\infty}f(x)=+\infty$.
2. Utiliser la définition exacte (avec les quantificateurs) pour prouver que :
   $$\lim_{x\to-5}\frac{x+5}{x-5}=0.$$
   On pourra supposer $x\le0$.

## Exercice 3

Soit $f$ la fonction définie sur $]0,+\infty[$ par

$$f(x)=\frac{\sqrt{5x}-x}{\sqrt{3x}+x}.$$

1. Étudier la continuité de $f$.
2. Montrer que l’on peut prolonger $f$ par continuité en $0$ par une fonction continue $\tilde f$. Déterminer $\tilde f$.

## Exercice 4

Soit $f$ la fonction définie sur $\mathbb R$ par

$$f(x)=\begin{cases}\dfrac{x^2-4x+3}{x-3} & \text{si } x>3\\[4pt] e^{ax}+ax & \text{si } x\le3\end{cases}$$

où $a\in\mathbb R$.

1. Déterminer $\displaystyle\lim_{x\to3^+}\frac{x^2-4x+3}{x-3}$.
2. Montrer que $f$ est continue sur $\mathbb R\setminus\{3\}$.
3. Montrer qu’il existe $a\in[0,1]$ tel que $f$ est continue en $x=3$.
   **Indication :** Pensez à appliquer le **TVI** à la fonction
   $$g(a)=e^{3a}+3a-2.$$

## Exercice 5

1. Soit $f$ une fonction continue sur $[0;1]$ telle que $f([0,1])\subset[0,1]$. On considère la fonction
   $$g(x)=f(x)-5x-2x^2.$$
   1. (a) Montrer que $g$ est continue sur $[0,1]$.
   2. (b) Montrer qu’il existe $c\in\left[0,\frac12\right]$ tel que
      $$f(c)=5c+2c^2.$$
2. Montrer que l’équation $x^2(\cos(x))^5+x\sin(x)+1=0$ admet au moins une solution réelle.
