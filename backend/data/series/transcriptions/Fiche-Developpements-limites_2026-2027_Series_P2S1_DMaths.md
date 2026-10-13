---
source: "PREING2-S1/Series/2627/Développements limités usuels .pdf"
pages: 2
annee: 2026-2027
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — Développements limités usuels (2026–2027)

CY Tech — PréIng 2, semestre 1.

## Formule de Taylor (page 1)

Les développements limités peuvent toujours être retrouvés par la formule de Taylor : pour toute fonction $f\in C^\infty(V(a))$, où $V(a)$ est un voisinage de $a\in\mathbb R$,

$$f(x)=f(a)+(x-a)f'(a)+\frac{(x-a)^2}{2}f''(a)+\cdots+\frac{(x-a)^n}{n!}f^{(n)}(a)+o((x-a)^n).$$

La majorité des développements usuels en zéro se retrouve à partir de trois développements canoniques. Cela évite de calculer les dérivées de $f$ et de les évaluer en $a$.

## Développement 1 — Somme de suite géométrique (page 1)

Pour $u$ proche de zéro :

$$\frac1{1-u}=1+u+u^2+\cdots+u^n+o(u^n).$$

Par changement de variable ou primitive, on en déduit les développements suivants en zéro, qui peuvent être prolongés à des ordres plus élevés :

- Avec $u=-x$ : $\displaystyle\frac1{1+x}=1-x+x^2-x^3+o(x^3)$.
- Par primitive du précédent et $\ln1=0$ : $\displaystyle\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3)$.
- Par changement de variable ou primitive : $\displaystyle\ln(1-x)=-x-\frac{x^2}{2}-\frac{x^3}{3}+o(x^3)$.
- Avec $u=-x^2$ : $\displaystyle\frac1{1+x^2}=1-x^2+x^4+o(x^4)$.
- Par primitive du précédent, puisque $\arctan'(x)=1/(1+x^2)$ et $\arctan0=0$ :
  $$\arctan x=x-\frac{x^3}{3}+\frac{x^5}{5}+o(x^5).$$

## Développement 2 — Exponentielle (pages 1–2)

On part de la définition de l’exponentielle, pour tout $u\in\mathbb R$ :

$$e^u=\sum_{k=0}^{+\infty}\frac{u^k}{k!}=1+u+\frac{u^2}{2}+\frac{u^3}{3!}+\cdots+\frac{u^n}{n!}+o(u^n)\quad(u\to0).$$

L’indice muet de la somme infinie est ici noté $k$ pour le distinguer de l’ordre $n$ du développement.

On en déduit :

- La partie paire de l’exponentielle, $\operatorname{ch}x=(e^x+e^{-x})/2$ :
  $$\operatorname{ch}x=1+\frac{x^2}{2}+\frac{x^4}{4!}+o(x^4).$$
- La partie impaire, $\operatorname{sh}x=(e^x-e^{-x})/2$ :
  $$\operatorname{sh}x=x+\frac{x^3}{3!}+\frac{x^5}{5!}+o(x^5).$$
- Avec $u=ix$, la partie réelle de $e^{ix}$ :
  $$\cos x=1-\frac{x^2}{2}+\frac{x^4}{4!}+o(x^4).$$
- Avec $u=ix$, la partie imaginaire de $e^{ix}$ :
  $$\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}+o(x^5).$$

Pour $\tan x=\sin x/\cos x$, on emploie ces développements et celui de $1/(1-u)$ avec $u=x^2/2+o(x^2)$ :

$$\begin{aligned}
\tan x&=\frac{x-x^3/3!+o(x^3)}{1-x^2/2+o(x^2)}\\
&=\left(x-\frac{x^3}{3!}+o(x^3)\right)\left(1+\frac{x^2}{2}+o(x^2)\right)\\
&=x+\frac{x^3}{3}+o(x^3).
\end{aligned}$$

De même, pour $\tanh x=\operatorname{sh}x/\operatorname{ch}x$ :

$$\begin{aligned}
\tanh x&=\frac{x+x^3/3!+o(x^3)}{1+x^2/2+o(x^2)}\\
&=\left(x+\frac{x^3}{3!}+o(x^3)\right)\left(1-\frac{x^2}{2}+o(x^2)\right)\\
&=x-\frac{x^3}{3}+o(x^3).
\end{aligned}$$

Pour obtenir les termes suivants de $\tan$ et $\tanh$, la formule de Taylor est tout aussi efficace que cette approche par les sinus et cosinus.

## Développement 3 — Puissance par le binôme de Newton (page 2)

La généralisation du binôme de Newton donne, pour tout $\alpha\in\mathbb R$ et $u\to0$ :

$$(1+u)^\alpha=1+\alpha u+\frac{\alpha(\alpha-1)}2u^2+\cdots+\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}u^n+o(u^n).$$

En particulier :

- $\alpha=1/2$, $u=x$ : $\displaystyle\sqrt{1+x}=1+\frac x2-\frac{x^2}{8}+o(x^2)$.
- $\alpha=1/2$, $u=-x$ : $\displaystyle\sqrt{1-x}=1-\frac x2-\frac{x^2}{8}+o(x^2)$.
- $\alpha=-1/2$, $u=x$ : $\displaystyle\frac1{\sqrt{1+x}}=1-\frac x2+\frac{3x^2}{8}+o(x^2)$.
- $\alpha=-1/2$, $u=-x^2$ : $\displaystyle\frac1{\sqrt{1-x^2}}=1+\frac{x^2}{2}+\frac{3x^4}{8}+o(x^4)$.

> **Coquille du PDF :** la dernière indication imprime $u=x^2$ ; le changement de variable qui donne la formule affichée est $u=-x^2$.

Enfin, en prenant des primitives des développements des dérivées :

$$\arcsin x=x+\frac{x^3}{6}+\frac{3x^5}{40}+o(x^5),$$

car $\arcsin'(x)=1/\sqrt{1-x^2}$ et $\arcsin0=0$ ;

$$\arccos x=\frac\pi2-x-\frac{x^3}{6}-\frac{3x^5}{40}+o(x^5),$$

car $\arccos'(x)=-1/\sqrt{1-x^2}$ et $\arccos0=\pi/2$.
