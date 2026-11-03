---
source: PREING2-S2/Algebre-lineaire/TD2-EX3-Correction_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Algèbre linéaire — TD2, exercice 3 : système différentiel

## Page 1 — Mise sous forme matricielle et réduction

$$(S)\quad\begin{cases}x'=y+z,\\y'=x,\\z'=x+y+z.\end{cases}
\qquad\Longleftrightarrow\qquad X'(t)=AX(t),$$

avec

$$X(t)=\begin{pmatrix}x(t)\\y(t)\\z(t)\end{pmatrix},\qquad
A=\begin{pmatrix}0&1&1\\1&0&0\\1&1&1\end{pmatrix}.$$

$(S)$ est un système différentiel linéaire à coefficients constants, sans second membre.

### Polynôme caractéristique

$$\begin{aligned}
P_A(\lambda)&=\det(A-\lambda I_3)
=\begin{vmatrix}-\lambda&1&1\\1&-\lambda&0\\1&1&1-\lambda\end{vmatrix}\\
&=\begin{vmatrix}-\lambda&1&1\\1&-\lambda&0\\2-\lambda&2-\lambda&2-\lambda\end{vmatrix}
&&\left(L_3\leftarrow L_3+L_1+L_2\right)\\
&=\begin{vmatrix}-1-\lambda&0&1\\1&-\lambda&0\\0&0&2-\lambda\end{vmatrix}
&&\left(C_1\leftarrow C_1-C_3,\ C_2\leftarrow C_2-C_3\right)\\
&=(2-\lambda)\lambda(1+\lambda).
\end{aligned}$$

$$\operatorname{Sp}(A)=\{-1,0,2\},\qquad m_{-1}=m_0=m_2=1.$$

$A$ est diagonalisable dans $\mathcal M_3(\mathbb R)$.

### Espace propre pour $-1$

$$X=\begin{pmatrix}x\\y\\z\end{pmatrix}\in E_{-1}=\ker(A+I_3)
\iff\begin{cases}x+y+z=0,\\x+y=0,\\x+y+2z=0\end{cases}
\iff\begin{cases}z=0,\\x=-y.\end{cases}$$

L’opération $L_3\leftarrow L_3-2L_1$ donne la troisième équation $-x-y=0$, redondante. Ainsi,

$$X=x\begin{pmatrix}1\\-1\\0\end{pmatrix},\qquad
E_{-1}=\operatorname{Vect}\left\{\begin{pmatrix}1\\-1\\0\end{pmatrix}\right\}.$$

### Espace propre pour $0$

$$X\in E_0=\ker A
\iff\begin{cases}y+z=0,\\x=0,\\x+y+z=0\end{cases}
\iff\begin{cases}x=0,\\y=-z.\end{cases}$$

$$E_0=\operatorname{Vect}\left\{\begin{pmatrix}0\\1\\-1\end{pmatrix}\right\}.$$

### Espace propre pour $2$

$$X\in E_2=\ker(A-2I_3)
\iff\begin{cases}-2x+y+z=0,\\x-2y=0,\\x+y-z=0\end{cases}
\iff\begin{cases}z=3y,\\x=2y.\end{cases}$$

L’addition $L_3\leftarrow L_3+L_1$ donne $-x+2y=0$, redondante. Ainsi,

$$E_2=\operatorname{Vect}\left\{\begin{pmatrix}2\\1\\3\end{pmatrix}\right\}.$$

## Page 2 — Résolution par changement de variables

On résume la réduction par $A=PDP^{-1}$, avec

$$D=\begin{pmatrix}-1&0&0\\0&0&0\\0&0&2\end{pmatrix},\qquad
P=\begin{pmatrix}1&0&2\\-1&1&1\\0&-1&3\end{pmatrix}
=\begin{pmatrix}V_1&V_2&V_3\end{pmatrix}.$$

En posant $Y(t)=P^{-1}X(t)$,

$$X'(t)=AX(t)\iff Y'(t)=DY(t)
\iff Y(t)=\begin{pmatrix}c_1e^{-t}\\c_2\\c_3e^{2t}\end{pmatrix},\qquad c_1,c_2,c_3\in\mathbb R.$$

La solution générale est $X(t)=PY(t)$, c’est-à-dire

$$\boxed{X(t)=c_1e^{-t}\begin{pmatrix}1\\-1\\0\end{pmatrix}
+c_2\begin{pmatrix}0\\1\\-1\end{pmatrix}
+c_3e^{2t}\begin{pmatrix}2\\1\\3\end{pmatrix},\qquad c_1,c_2,c_3\in\mathbb R.}$$
