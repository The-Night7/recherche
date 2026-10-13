---
source: PREING2-S2/Algebre-lineaire/TD3-EX9-Q3-Correction_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf
pages: 1
transcription: manuelle
---

# Algèbre linéaire — TD3, exercice 9, question 3 (corrigé)

## Exercice 9 : Matrice d'une forme bilinéaire dans une base orthogonale

**Question 3.** Notons $P$ la matrice de passage de $B$ à $B'$ :

$$P=\begin{pmatrix}1&2&-3\\0&1&2\\0&0&1\end{pmatrix}.$$

La matrice $A'$ de la forme bilinéaire $f$ dans la base $B'$ est donnée par

$$\begin{aligned}
A'&=P^{\mathsf T}AP\\
&=\begin{pmatrix}1&0&0\\2&1&0\\-3&2&1\end{pmatrix}
\begin{pmatrix}1&0&0\\-2&2&0\\7&-4&-1\end{pmatrix}\\
&=\begin{pmatrix}1&0&0\\0&2&0\\0&0&-1\end{pmatrix}.
\end{aligned}$$

La base $B'$ est orthogonale pour $f$.

Soient $x,y\in\mathbb R^3$ et leurs colonnes de coordonnées dans $B'$ :

$$X'=\begin{pmatrix}x'_1\\x'_2\\x'_3\end{pmatrix},\qquad
Y'=\begin{pmatrix}y'_1\\y'_2\\y'_3\end{pmatrix}.$$

On a

$$\begin{aligned}
f(x,y)&=(X')^{\mathsf T}A'Y'\\
&=\begin{pmatrix}x'_1&x'_2&x'_3\end{pmatrix}
\begin{pmatrix}y'_1\\2y'_2\\-y'_3\end{pmatrix}\\
&=x'_1y'_1+2x'_2y'_2-x'_3y'_3.
\end{aligned}$$

> Le PDF contient une seule page, annotée « Ex. 9 (2/3) ». Cette transcription couvre cette page ; les autres questions ne figurent pas dans ce fichier.
