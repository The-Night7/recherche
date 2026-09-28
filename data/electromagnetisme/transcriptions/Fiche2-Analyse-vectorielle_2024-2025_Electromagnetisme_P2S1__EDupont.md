---
source: PREING2-S1/Electromagnetisme/Fiche2-Analyse-vectorielle_2024-2025_Electromagnetisme_P2S1__EDupont.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Électromagnétisme — Analyse vectorielle, fiche 2

## Page 1 — Gradient

$$df=\operatorname{grad}f\cdot d\vec\ell.$$

En coordonnées cartésiennes,

$$\operatorname{grad}V=\begin{pmatrix}
\dfrac{\partial V}{\partial x}\\[3pt]
\dfrac{\partial V}{\partial y}\\[3pt]
\dfrac{\partial V}{\partial z}
\end{pmatrix}.$$

La fiche introduit l’opérateur « nabla » par ses composantes cartésiennes :

$$\vec\nabla=\begin{pmatrix}
\dfrac{\partial}{\partial x}\\[3pt]
\dfrac{\partial}{\partial y}\\[3pt]
\dfrac{\partial}{\partial z}
\end{pmatrix},\qquad\operatorname{grad}V=\vec\nabla V.$$

> Le manuscrit dit « seulement en coordonnées cartésiennes ». Cette restriction concerne la forme en composantes affichée ; les expressions dans d’autres systèmes de coordonnées diffèrent.

## Page 1 — Divergence

En coordonnées cartésiennes,

$$\operatorname{div}\vec A=\frac{\partial A_x}{\partial x}+
\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}
=\vec\nabla\cdot\vec A.$$

La fiche représente ce calcul comme le produit scalaire de la colonne des opérateurs $(\partial_x,\partial_y,\partial_z)$ avec la colonne $(A_x,A_y,A_z)$.

## Page 1 — Rotationnel

En coordonnées cartésiennes,

$$\begin{aligned}
\operatorname{rot}\vec A={}&\left(\frac{\partial A_z}{\partial y}-\frac{\partial A_y}{\partial z}\right)\vec u_x\\
&+\left(\frac{\partial A_x}{\partial z}-\frac{\partial A_z}{\partial x}\right)\vec u_y\\
&+\left(\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}\right)\vec u_z
=\vec\nabla\wedge\vec A.
\end{aligned}$$

Le schéma des flèches croisées associe les composantes du produit vectoriel : $(y,z)$ pour la composante selon $x$, $(z,x)$ pour celle selon $y$, $(x,y)$ pour celle selon $z$, avec la soustraction dans chaque paire.

## Page 2 — Laplacien scalaire

$$\Delta V=\operatorname{div}(\operatorname{grad}V).$$

En coordonnées cartésiennes,

$$\Delta V=\vec\nabla\cdot(\vec\nabla V)
=\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}.$$

La fiche développe ce calcul comme le produit scalaire de $(\partial_x,\partial_y,\partial_z)$ avec $(\partial_xV,\partial_yV,\partial_zV)$.

## Page 2 — Laplacien vectoriel

En coordonnées cartésiennes,

$$\Delta\vec V=\begin{pmatrix}\Delta V_x\\\Delta V_y\\\Delta V_z\end{pmatrix}.$$
