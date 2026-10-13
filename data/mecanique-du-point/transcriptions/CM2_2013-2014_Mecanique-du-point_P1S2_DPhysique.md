# Mécanique du point — Résumé 2 : rappels de mathématiques

> Source : `PREING1-S2/Mecanique-du-point/CM2_2013-2014_Mecanique-du-point_P1S2_DPhysique.pdf`, 1 page, numérotée 3 dans le cours.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif, restitution des formules et description du schéma.

## Vecteurs

Un vecteur est défini par une norme et une orientation, c’est-à-dire une direction et un sens. Un vecteur unitaire a une norme égale à 1. Un vecteur n’est pas un scalaire.

## Base cartésienne

La base cartésienne $\{\vec u_x,\vec u_y,\vec u_z\}$ est orthonormée directe. On écrit :

$$\vec V=V_x\vec u_x+V_y\vec u_y+V_z\vec u_z.$$

Les nombres $(V_x,V_y,V_z)$ sont les coordonnées de $\vec V$ dans cette base.

## Opérations sur les vecteurs

Relation de Chasles :

$$\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}.$$

Produit scalaire :

$$\vec V_1\cdot\vec V_2=\|\vec V_1\|\,\|\vec V_2\|\cos\theta,$$

où $\theta$ est l’angle non orienté entre les deux vecteurs. Dans la base cartésienne :

$$\vec V_1\cdot\vec V_2=V_{1x}V_{2x}+V_{1y}V_{2y}+V_{1z}V_{2z}.$$

Norme :

$$\|\vec V\|^2=\vec V\cdot\vec V=V_x^2+V_y^2+V_z^2.$$

## Projection d’un vecteur

Le schéma représente un axe $x$ vers la droite, un axe $y$ vers le haut et un vecteur $\vec V$ orienté vers le haut et la gauche. L’angle $\alpha$ est mesuré entre le vecteur et la verticale positive passant par son origine ; les pointillés indiquent les directions horizontale et verticale. Ainsi :

$$\vec V=-\|\vec V\|\sin\alpha\,\vec u_x+\|\vec V\|\cos\alpha\,\vec u_y.$$

## Notation différentielle

$$\frac{df}{dx}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}=f'(x).$$

Le document écrit :

$$df=f(x+dx)-f(x)=f'(x)\,dx.$$

$df$ est la différentielle de $f$, présentée comme sa variation infinitésimale correspondant à l’accroissement infinitésimal $dx$ de la variable $x$.

**Précision sur la source.** L’égalité $df=f'(x)dx$ définit la différentielle ; pour un accroissement fini $h$, on a $f(x+h)-f(x)=f'(x)h+o(h)$ en général. L’égalité de la source avec la variation de $f$ est une écriture infinitésimale informelle.

La dérivée seconde s’écrit :

$$f''(x)=\frac d{dx}\left(\frac{df}{dx}\right)=\frac{d^2f}{dx^2},$$

et de même pour les ordres suivants. $df$ et $dx$ ont respectivement les dimensions de $f$ et $x$. De plus, $[d^2f]=[f]$ et $[dx^2]=[x]^2$.
