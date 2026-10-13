# Analyse 1 — DS3 2023–2024, sujet (examen)

> Source : `PREING1-S1/Analyse1-DS/DS3-2023-2024_Analyse1-DS_P1S1_DMaths.pdf`, 2 pages (scans d’un sujet imprimé froissé).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. L’en-tête porte « Examen Analyse I ». Le barème indiqué totalise 28 points (10 + 6 + 6 + 6). La source note la même fonction $\phi$ puis $\varphi$ dans l’exercice 4 ; la notation est conservée.

**Préing 1 — Examen Analyse I**

| Date | Durée | Nombre de pages |
| --- | --- | --- |
| 24 janvier 2024 | 2 h 00 | 2 |

L’usage de tout appareil électronique est interdit.

**Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.** *Le sujet comporte 4 exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.*

## Exercice 1 (10 points)

Déterminer, si elle existe, la limite de chacune des fonctions suivantes. Sinon, justifier pourquoi il n’y a pas de limite. :

1. $\displaystyle\lim_{x\to+\infty}\frac{4x^2+7\ln(x)}{3x+2e^x}$.
2. $\displaystyle\lim_{x\to0}x\cdot E\left(\frac1x\right)$.
3. $\displaystyle\lim_{x\to1}\frac{(x-1)^2+2|x-1|}{x-1}$.
4. $\displaystyle\lim_{x\to0}\frac{(e^x-1)}{x}$.
5. $\displaystyle\lim_{x\to+\infty}\sqrt{x^2+\sqrt{x^4+5}}-x$.

## Exercice 2 (6 points)

1. Donner la définition exacte, avec les quantificateurs, des propositions suivantes :
   1. a) $\displaystyle\lim_{x\to a}f(x)=\ell$, où $a$ et $\ell$ sont deux nombres réels.
   2. b) $\displaystyle\lim_{x\to+\infty}f(x)=\ell$, où $\ell$ est un nombre réel.
2. Utiliser la définition exacte (avec les quantificateurs) pour prouver que :
   $$\lim_{x\to0}x^2\cos\left(\frac1x\right)=0.$$
3. Utiliser la définition exacte (avec les quantificateurs) pour prouver que :
   $$\lim_{x\to1}\frac{4}{5(x-1)^2}=+\infty.$$

## Exercice 3 (6 points)

**Choisir deux des trois questions suivants.**

1. Soit $f$ la fonction définie sur $[-2,+\infty[\setminus\{7\}$ par
   $$f(x)=\frac{\sqrt{x+2}-3}{x-7}.$$
   1. (a) Étudier la continuité de $f$ sur $[-2,+\infty[\setminus\{7\}$.
   2. (b) Démontrer qu’on peut prolonger $f$ par continuité en $7$. Préciser la valeur prise en $7$ par ce prolongement.
2. Soit $f:\mathbb R\longrightarrow\mathbb R$ définie par
   $$f(x)=E(x)+(x-E(x))^2.$$
   Étudier la continuité de $f$ sur $\mathbb R$.
3. On considère la fonction $f$ définie sur $\mathbb R$ par :
   $$f(x)=\begin{cases}\dfrac{\sin(ax)}{x} & \text{si } x<0\\[4pt] \dfrac1x-\dfrac1{x(x+1)} & \text{si } x>0\end{cases}$$
   où $a\in\mathbb R^*$.
   1. (a) Montrer que $f$ est continue sur $\mathbb R\setminus\{0\}$.
   2. (b) Quelle valeur doit-on donner à $a$ pour que $f$ soit prolongeable par continuité en $0$. Justifier votre réponse.

> Note : la question 1 ne porte pas de numéro visible sur le scan (pli du papier) ; la numérotation 1 est déduite des questions 2 et 3.

## Exercice 4 (6 points)

1. Énoncer le **Théorème des valeurs intermédiaires**.
2. Soit $f:[a,b]\longrightarrow\mathbb R$ une fonction continue telle que
   $$f([a,b])\subset[a,b].$$
   Montrer qu’il existe $c\in[a,b]$ tel que
   $$f(c)=c.$$
3. Soient $f,g:I\longrightarrow\mathbb R$ deux fonctions continues sur un intervalle $I$ de $\mathbb R$ telles que
   $$\forall x\in I,\ |f(x)|=|g(x)|\neq0.$$
   1. (a) Montrer que la fonction $\phi:I\longrightarrow\mathbb R$ définie par $\varphi(x)=\dfrac{f(x)}{g(x)}$ est continue sur $I$.
   2. (b) À l’aide de la fonction $\phi$ en déduire que $f=g$ ou $f=-g$.
