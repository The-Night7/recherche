---
source: "PREING1-S2/Analyse2/Fiche-Analyse-Asymptotique_2024-2025_Analyse2_P1S2_DMaths.pdf"
pages: 1
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Formulaire d’analyse asymptotique

## Relations d’équivalence usuelles au voisinage de 0

$$\sin x\underset{x\to0}{\sim}x,\qquad
1-\cos x\underset{x\to0}{\sim}\frac{x^2}{2},\qquad
\tan x\underset{x\to0}{\sim}x,$$

$$\ln(1+x)\underset{x\to0}{\sim}x,\qquad
e^x-1\underset{x\to0}{\sim}x,\qquad
(1+x)^\alpha-1\underset{x\to0}{\sim}\alpha x.$$

On peut remplacer $x$ par une suite $u_n$ qui tend vers $0$ pour obtenir des relations d’équivalence usuelles entre suites.

> Précision de transcription : la dernière équivalence suppose $\alpha\ne0$ ; pour $\alpha=0$, les deux expressions sont identiquement nulles. Cette condition n’est pas indiquée dans le formulaire.

## Développements limités usuels

Tous les petits $o$ ci-dessous sont pris lorsque $x\to0$. Le tableau source porte l’en-tête « À l’ordre $n$ » ; pour le cosinus et le sinus, les puissances maximales indiquées sont respectivement $2n$ et $2n+1$.

| Fonction | Développement général | Premiers termes |
| --- | --- | --- |
| $\cos x$ | $\displaystyle\sum_{k=0}^{n}(-1)^k\frac{x^{2k}}{(2k)!}+o(x^{2n+1})$ | $1-\frac{x^2}{2}+\frac{x^4}{24}+o(x^5)$ |
| $\sin x$ | $\displaystyle\sum_{k=0}^{n}(-1)^k\frac{x^{2k+1}}{(2k+1)!}+o(x^{2n+2})$ | $x-\frac{x^3}{6}+\frac{x^5}{120}+o(x^6)$ |
| $e^x$ | $\displaystyle\sum_{k=0}^{n}\frac{x^k}{k!}+o(x^n)$ | $1+x+\frac{x^2}{2}+\frac{x^3}{6}+o(x^3)$ |
| $\ln(1+x)$ | $\displaystyle\sum_{k=1}^{n}(-1)^{k+1}\frac{x^k}{k}+o(x^n)$ | $x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3)$ |
| $\frac1{1+x}$ | $\displaystyle\sum_{k=0}^{n}(-1)^kx^k+o(x^n)$ | $1-x+x^2-x^3+o(x^3)$ |
| $\frac1{1-x}$ | $\displaystyle\sum_{k=0}^{n}x^k+o(x^n)$ | $1+x+x^2+x^3+o(x^3)$ |

$$\begin{aligned}
(1+x)^\alpha={}&1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2+\cdots\\
&+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n+o(x^n).
\end{aligned}$$

$$\sqrt{1+x}=1+\frac{x}{2}-\frac{x^2}{8}+\frac{x^3}{16}+o(x^3),$$

$$\frac1{\sqrt{1+x}}=1-\frac{x}{2}+\frac{3x^2}{8}-\frac{5x^3}{16}+o(x^3).$$
