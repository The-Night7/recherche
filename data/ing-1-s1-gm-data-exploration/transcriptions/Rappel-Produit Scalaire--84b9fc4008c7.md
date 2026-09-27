---
source: ING 1/S1 GM /DATA EXPLORATION/Chapitre 2 - Quantitative x Quantitative/Rappel-Produit Scalaire.pdf
pages: 1-2
transcription: manuelle
---

# Data exploration — Rappel sur le produit scalaire

## Norme et produit scalaire dans le plan

Soient $u=(x,y)$ et $v=(x',y')$. On a

$$\|u\|=\sqrt{x^2+y^2},\qquad\|u\|^2=x^2+y^2,$$

$$\langle u,v\rangle=xx'+yy'.$$

Pour deux vecteurs non nuls, si $\theta$ est l'angle entre eux,

$$\langle u,v\rangle=\|u\|\,\|v\|\cos\theta,\qquad
\cos\theta=\frac{\langle u,v\rangle}{\|u\|\,\|v\|}.$$

> **Précision :** la norme de $u$ est la distance de l'origine au point de coordonnées $(x,y)$ ; la mention manuscrite « distance euclidienne entre $x$ et $y$ » est imprécise.

## Interprétation de l'angle et corrélation

- Si $\cos\theta=0$, les vecteurs sont orthogonaux ; le dessin représente un angle droit.
- Si $\cos\theta=1$, l'angle est nul ; si $\cos\theta=-1$, il est plat.
- Si $0<\cos\theta<1$, l'angle est aigu.
- Si $-1<\cos\theta<0$, l'angle est obtus.

> Les cas limites $\cos\theta=\pm1$ sont séparés pour préciser les inégalités de la fiche.

Dans le vocabulaire statistique de la fiche, $X$ et $Y$ sont non corrélées si $r_{xy}=0$, et parfaitement corrélées si $r_{xy}=\pm1$.

## Symétrie et bilinéarité

$$\langle X,Y\rangle=\langle Y,X\rangle,$$

$$\langle X,Y+Y'\rangle=\langle X,Y\rangle+\langle X,Y'\rangle,$$

$$\langle X+X',Y\rangle=\langle X,Y\rangle+\langle X',Y\rangle.$$

Pour $\lambda\in\mathbb R$,

$$\langle X,\lambda Y\rangle=\lambda\langle X,Y\rangle,\qquad
\langle\lambda X,Y\rangle=\lambda\langle X,Y\rangle.$$

En réunissant ces propriétés,

$$\begin{aligned}
\langle X,\lambda Y+\lambda'Y'\rangle
&=\langle X,\lambda Y\rangle+\langle X,\lambda'Y'\rangle\\
&=\lambda\langle X,Y\rangle+\lambda'\langle X,Y'\rangle.
\end{aligned}$$
