---
source: TD0_2022-2023_Series_P2S1_DMaths.pdf, pages 1 et 2 (énoncés seuls ; le corrigé est transcrit dans TD0-Correction_2022-2023_Series_P2S1_Inconnu)
transcription: manuelle
---

# Séries — TD0 : comparaison locale des fonctions réelles (2022/2023)

## Exercice 1 : Convergence de suites

Étudier la convergence des suites numériques suivantes, de terme général $u_n$ :

1. $u_n = \sqrt{n+1} - \sqrt{n}$
2. $u_n = \left(1 + \dfrac{1}{n}\right)^n$
3. $u_n = \sqrt{n}\, e^{-\sqrt{\ln(n)}}$
4. $u_n = \dfrac{\sin(n^2)}{n}$
5. $u_n = \dfrac{a^n - b^n}{a^n + b^n}$, $(a, b) \in (\mathbb{R}_+^*)^2$

## Exercice 2 : Équivalents de suites

Donner des équivalents simples lorsque $n$ tend vers $+\infty$ pour les suites numériques suivantes, de terme général $u_n$ :

1. $u_n = \left(\ln(1 + e^{-n^2})\right)^{\frac{1}{n}}$
2. $u_n = \left(\dfrac{e^n}{1 + e^{-n}}\right)^n$

## Exercice 3 : Équivalents de fonctions en +∞

Déterminer un équivalent au voisinage de $+\infty$ des fonctions suivantes :

1. $f_1(x) = \sqrt{x^3 + x^{5/2}} - x^{3/2}$
2. $f_2(x) = \dfrac{\sqrt{x^4 + 1} - \sqrt{x^4 - 1}}{\sqrt{x^2 + 1} - \sqrt{x^2 - 1}}$
3. $f_3(x) = \dfrac{e^{1/x} - \cos\frac{1}{x}}{1 - \sqrt{1 - \frac{1}{x^2}}}$
4. $f_4(x) = \dfrac{1}{\sqrt{x}} - \sqrt{x}\,\sin\dfrac{1}{x}$
5. $f_5(x) = e^{1/x} - e^{1/(x+1)}$

## Exercice 4 : Une limite par le logarithme

Soit $f(x) = \left[\dfrac{\ln(1 + x)}{\ln(x)}\right]^{x \ln(x)}$.

1. Déterminer un équivalent de $\ln(f(x))$ en $+\infty$.
2. En déduire $\displaystyle\lim_{x \to +\infty} f(x)$.

## Exercice 5 : Calculs de limites

Calculer les limites suivantes :

1. $\displaystyle\lim_{x \to 0} \frac{4\sin^3(x) + x - 4(\cos x - 1)}{3x^2 + e^x - 1}$
2. $\displaystyle\lim_{x \to 0} \frac{(1 - e^x)\sin x}{e^x - \operatorname{ch} x}$
3. $\displaystyle\lim_{x \to 1} \frac{x^x - 1}{1 - x + \ln(1 + x)}$
4. $\displaystyle\lim_{x \to +\infty} \sqrt{x + \sqrt{x}} - \sqrt{x}$
5. $\displaystyle\lim_{x \to +\infty} \frac{(x^x)^x}{x^{(x^x)}}$
6. $\displaystyle\lim_{x \to +\infty} \left(\cos\left(\frac{1}{x}\right)\right)^{x^2}$
7. $\displaystyle\lim_{x \to 1} \frac{\sqrt[3]{2x - x^3} - \sqrt{x}}{1 - x^{3/4}}$
8. $\displaystyle\lim_{x \to 0} \left(\frac{x}{\sin x}\right)^{\frac{\sin x}{x - \sin x}}$
9. $\displaystyle\lim_{x \to 0} \left(\frac{a^x + b^x}{2}\right)^{\frac{1}{x}}$
10. $\displaystyle\lim_{x \to 0} \frac{(1 - \cos x)(1 + 2x)}{x^2 - x^4}$
11. $\displaystyle\lim_{x \to +\infty} \sqrt{4x + 1}\,\ln\left(1 - \frac{\sqrt{x + 1}}{x + 2}\right)$
12. $\displaystyle\lim_{x \to 0} x(3 + x)\frac{\sqrt{3 + x}}{\sqrt{x}\sin(\sqrt{x})}$
13. $\displaystyle\lim_{x \to 0} \exp\left(\frac{1}{x^2}\right) - \exp\left(\frac{1}{(x + 1)^2}\right)$

## Exercice 6 : Comparaison de fonctions

Comparer les fonctions suivantes au voisinage des points indiqués :

1. $\cos(x) - 1$ et $\sin(x)$ au voisinage de $0$
2. $x \ln x$ et $\ln(1 + 2x)$ au voisinage de $0$
3. $x^{\ln(x)}$ et $(\ln x)^x$ au voisinage de $+\infty$
4. $x \ln(x)$ et $\sqrt{x^2 + 3x}\,\ln(x^2)\sin(x)$ au voisinage de $+\infty$

## Exercice 7 : Négligeabilité et exponentielle

Soit $f, g : \mathbb{R} \to \mathbb{R}$. On suppose que $\displaystyle\lim_{x \to +\infty} f(x) = +\infty$.

1. On suppose que $g \underset{+\infty}{=} o(f)$. Montrer que $\exp(g) \underset{+\infty}{=} o(\exp(f))$.
2. Montrer que la réciproque est fausse.
3. Application : comparer $f(x) = (\ln(\ln x))^{x^{\ln x}}$ et $g(x) = (\ln x)^{x^{\ln(\ln(x))}}$ au voisinage de $+\infty$.
