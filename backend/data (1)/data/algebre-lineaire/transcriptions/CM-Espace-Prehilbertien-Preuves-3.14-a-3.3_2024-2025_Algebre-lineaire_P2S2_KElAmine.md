---
source: "PREING2-S2/Algebre-lineaire/CM-Espace-Prehilbertien-Preuves-3.14-a-3.3_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf"
pages: 1
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Espaces préhilbertiens — Preuves et début du procédé de Gram–Schmidt

K. El Amine — Page imprimée 10. Cette page commence au milieu d’une preuve et se termine au début de l’énoncé du théorème 3.17.

## Fin de la preuve de liberté d’une famille orthogonale de vecteurs non nuls

Soit $J$ une partie finie de $I$. Si $\sum_{j\in J}\alpha_jx_j=0$, alors, pour tout $k\in J$,

$$\begin{aligned}
0&=\left\langle\sum_{j\in J}\alpha_jx_j,x_k\right\rangle
=\sum_{j\in J}\alpha_j\langle x_j,x_k\rangle\\
&=\alpha_k\langle x_k,x_k\rangle=\alpha_k\|x_k\|^2.
\end{aligned}$$

D’où $\alpha_k=0$, car $\|x_k\|\ne0$. L’annotation manuscrite au-dessus du premier zéro rappelle $\langle0,x_k\rangle$.

**Remarque.** En conséquence, toute famille orthonormale $\{x_i\}_{i\in I}$ de vecteurs de $E$ est libre.

## Théorème 3.15 — Formule de Pythagore

Soit $(E,\langle\cdot,\cdot\rangle)$ un espace préhilbertien réel. Pour tous $x,y\in E$,

$$x\perp y\iff\|x+y\|^2=\|x\|^2+\|y\|^2.$$

**Preuve.**

$$\begin{aligned}
x\perp y&\iff\langle x,y\rangle=0\\
&\iff\|x\|^2+\|y\|^2+2\langle x,y\rangle=\|x\|^2+\|y\|^2\\
&\iff\|x+y\|^2=\|x\|^2+\|y\|^2.
\end{aligned}$$

## Proposition 3.16 — Famille orthogonale finie

Soit $(E,\langle\cdot,\cdot\rangle)$ un espace préhilbertien réel et $\{x_i\}_{1\le i\le p}$ une famille finie d’éléments de $E$ :

$$\{x_i\}_{1\le i\le p}\text{ est orthogonale}
\implies\left\|\sum_{i=1}^p x_i\right\|^2=\sum_{i=1}^p\|x_i\|^2.$$

La réciproque est fausse pour $p\ge3$.

**Preuve.** Par récurrence ou directement :

$$\begin{aligned}
\left\|\sum_{i=1}^p x_i\right\|^2
&=\left\langle\sum_{i=1}^p x_i,\sum_{i=1}^p x_i\right\rangle
=\left\langle\sum_{i=1}^p x_i,\sum_{j=1}^p x_j\right\rangle\\
&=\sum_{i=1}^p\sum_{j=1}^p\langle x_i,x_j\rangle
=\sum_{i=1}^p\langle x_i,x_i\rangle
=\sum_{i=1}^p\|x_i\|^2,
\end{aligned}$$

car $\langle x_i,x_j\rangle=0$ si $i\ne j$.

Montrons par un contre-exemple que la réciproque est fausse si $p\ge3$. Dans l’espace euclidien usuel $\mathbb R^2$, soient $x_1=(1,0)$, $x_2=(0,1)$ et $x_3=(1,-1)$. On a

$$\|x_1+x_2+x_3\|^2=\|(1,0)+(0,1)+(1,-1)\|^2=\|(2,0)\|^2=4,$$

$$\|x_1\|^2+\|x_2\|^2+\|x_3\|^2
=\|(1,0)\|^2+\|(0,1)\|^2+\|(1,-1)\|^2=1+1+2=4.$$

Les quantités sont égales, mais les vecteurs ne sont pas deux à deux orthogonaux : $\langle x_1,x_3\rangle=1\ne0$.

## 3.3. Procédé d’orthogonalisation de Gram–Schmidt

Dans tout $\mathbb R$-espace vectoriel $E$ de dimension finie et pour toute forme bilinéaire symétrique $\varphi$ sur $E$, il existe une base $\varphi$-orthogonale. Le théorème du chapitre « Forme bilinéaire » établit l’existence d’une telle base mais ne fournit pas le moyen de la construire. La méthode d’orthogonalisation de Gram–Schmidt permet, à l’aide du produit scalaire, de construire des bases orthogonales à partir d’une base quelconque de $E$.

### Théorème 3.17 — Orthogonalisation de Gram–Schmidt

Soit $(E,\langle\cdot,\cdot\rangle)$ un espace préhilbertien réel et $\{v_1,\ldots,v_p\}$ une famille libre de $E$. La famille $\{q_1,\ldots,q_p\}$ est définie par récurrence par

$$q_1=v_1,\qquad
\forall k\in\{2,\ldots,p\},\quad
q_k=v_k-\sum_{i=1}^{k-1}\frac{\langle v_k,q_i\rangle}{\|q_i\|^2}q_i.$$

La page se termine sur « Vérifie : ». La suite de l’énoncé n’est pas contenue dans ce fichier d’une page.
