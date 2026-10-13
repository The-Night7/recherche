---
source: PREING2-S2/Algebre-lineaire/TD2-EX4-FIN-Correction_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf
pages: 1
transcription: manuelle
---

# Algèbre linéaire — TD2, fin de l'exercice 4 (corrigé)

## Exercice 4 : Résolution du système différentiel

On a $A=PTP^{-1}$, avec

$$T=\begin{pmatrix}-1&0&0\\0&0&1\\0&0&0\end{pmatrix},\qquad
P=\begin{pmatrix}-1&1&0\\1&2&1\\2&0&1\end{pmatrix}.$$

Posons $Y(t)=P^{-1}X(t)$, soit $X(t)=PY(t)$. Alors

$$X'(t)=AX(t)\iff Y'(t)=TY(t)
\iff\begin{cases}
y'_1(t)=-y_1(t),\\
y'_2(t)=y_3(t),\\
y'_3(t)=0.
\end{cases}$$

On résout de bas en haut :

$$y_3(t)=c_3,\qquad y_2(t)=c_3t+c_2,\qquad y_1(t)=c_1e^{-t},
\qquad c_1,c_2,c_3\in\mathbb R.$$

En notant $V_1,V_2,V_3$ les colonnes de $P$,

$$X(t)=y_1(t)V_1+y_2(t)V_2+y_3(t)V_3.$$

Finalement,

$$X(t)=c_1e^{-t}\begin{pmatrix}-1\\1\\2\end{pmatrix}
+(c_2+c_3t)\begin{pmatrix}1\\2\\0\end{pmatrix}
+c_3\begin{pmatrix}0\\1\\1\end{pmatrix},\qquad c_1,c_2,c_3\in\mathbb R.$$

> Le fichier source contient uniquement la dernière page, annotée « Ex. 4 (3/3) ». La réduction de $A$ qui précède cette résolution n'y figure pas.
