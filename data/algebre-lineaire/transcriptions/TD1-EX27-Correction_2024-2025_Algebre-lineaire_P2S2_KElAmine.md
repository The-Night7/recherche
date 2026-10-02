---
source: "PREING2-S2/Algebre-lineaire/TD1-EX27-Correction_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf"
pages: 3
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Correction d’un exercice sur une suite vectorielle affine

> **Repère de la source :** les trois pages manuscrites portent « Ex. 26 » (1/3, 2/3 et 3/3), alors que le nom du fichier annonce « EX27 ». Ce décalage de numérotation est conservé et signalé ici.

## Page 1 — Point fixe et changement de variable

On considère

$$
X_{n+1}=AX_n+B,\qquad
A=\begin{pmatrix}\frac12&\frac14\\\frac14&\frac12\end{pmatrix},\qquad
B=\begin{pmatrix}\frac14\\\frac14\end{pmatrix},
$$

avec $X_n=\begin{pmatrix}x_n\\y_n\end{pmatrix}$ et $X_0=\begin{pmatrix}x_0\\y_0\end{pmatrix}$ donné.

### 1. Inversibilité de $I_2-A$

$$
I_2-A=\begin{pmatrix}\frac12&-\frac14\\-\frac14&\frac12\end{pmatrix},
\qquad \det(I_2-A)=\frac14-\frac1{16}=\frac3{16}\ne0.
$$

Donc $I_2-A$ est inversible, et

$$
(I_2-A)^{-1}
=\frac{16}{3}\begin{pmatrix}\frac12&\frac14\\\frac14&\frac12\end{pmatrix}
=\begin{pmatrix}\frac83&\frac43\\\frac43&\frac83\end{pmatrix}
=\frac43\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

### 2. Résolution de $X=AX+B$

$$
X=AX+B\iff(I_2-A)X=B\iff X=(I_2-A)^{-1}B.
$$

Ainsi,

$$
X=\frac43\begin{pmatrix}2&1\\1&2\end{pmatrix}
\begin{pmatrix}\frac14\\\frac14\end{pmatrix}
=\frac43\begin{pmatrix}\frac34\\\frac34\end{pmatrix}
=\begin{pmatrix}1\\1\end{pmatrix}.
$$

### 3.a. Suite translatée

Posons $U_n=X_n-X$. En soustrayant $X=AX+B$ de $X_{n+1}=AX_n+B$, on obtient

$$
X_{n+1}-X=A(X_n-X),\qquad U_{n+1}=AU_n.
$$

## Page 2 — Puissances et sous-espaces propres

### 3.b. Expression de $U_n$

Pour $n\ge1$,

$$
U_n=AU_{n-1}=AAU_{n-2}=A^2U_{n-2}=\cdots=A^nU_0.
$$

Finalement, pour tout $n\in\mathbb N$, $U_n=A^nU_0$.

### 3.c. Diagonalisation de $A$

Le polynôme caractéristique est

$$
\begin{aligned}
p_A(\lambda)&=\det(A-\lambda I_2)\\
&=\left(\frac12-\lambda\right)^2-\left(\frac14\right)^2\\
&=\left(\frac12-\lambda-\frac14\right)\left(\frac12-\lambda+\frac14\right)\\
&=\left(\frac14-\lambda\right)\left(\frac34-\lambda\right).
\end{aligned}
$$

Donc $\operatorname{Sp}(A)=\{\frac14,\frac34\}$. La matrice $A$, d’ordre 2, possède deux valeurs propres distinctes : elle est diagonalisable.

Pour $\lambda=\frac14$,

$$
\begin{aligned}
X=\begin{pmatrix}x\\y\end{pmatrix}\in E_{1/4}
&\iff\left(A-\frac14I_2\right)X=0\\
&\iff\begin{pmatrix}\frac14&\frac14\\\frac14&\frac14\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=0\\
&\iff\frac14(x+y)=0\iff x=-y.
\end{aligned}
$$

Ainsi,

$$
E_{1/4}=\operatorname{Vect}\left(\begin{pmatrix}-1\\1\end{pmatrix}\right).
$$

> **Erreur de signe dans la source :** la ligne intermédiaire écrit $\begin{pmatrix}-y\\y\end{pmatrix}=y\begin{pmatrix}1\\-1\end{pmatrix}$. Il faut lire $y\begin{pmatrix}-1\\1\end{pmatrix}$, ou $-y\begin{pmatrix}1\\-1\end{pmatrix}$. Le sous-espace propre final est correct ; les deux générateurs opposés conviennent.

Pour $\lambda=\frac34$,

$$
\begin{aligned}
X=\begin{pmatrix}x\\y\end{pmatrix}\in E_{3/4}
&\iff\left(A-\frac34I_2\right)X=0\\
&\iff\begin{pmatrix}-\frac14&\frac14\\\frac14&-\frac14\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=0\\
&\iff-\frac14(x-y)=0\iff x=y.
\end{aligned}
$$

Donc $X=y\begin{pmatrix}1\\1\end{pmatrix}$ et

$$
E_{3/4}=\operatorname{Vect}\left(\begin{pmatrix}1\\1\end{pmatrix}\right).
$$

## Page 3 — Calcul de $A^n$ et limite

On choisit

$$
P=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad
D=\begin{pmatrix}\frac14&0\\0&\frac34\end{pmatrix},\qquad
P^{-1}=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
$$

Alors $A=PDP^{-1}$, d’où

$$
\begin{aligned}
A^n&=PD^nP^{-1}\\
&=\frac12\begin{pmatrix}(1/4)^n&(3/4)^n\\-(1/4)^n&(3/4)^n\end{pmatrix}\begin{pmatrix}1&-1\\1&1\end{pmatrix}\\
&=\frac12\left(\frac34\right)^n\begin{pmatrix}3^{-n}&1\\-3^{-n}&1\end{pmatrix}\begin{pmatrix}1&-1\\1&1\end{pmatrix}\\
&=\frac12\left(\frac34\right)^n\begin{pmatrix}3^{-n}+1&1-3^{-n}\\1-3^{-n}&3^{-n}+1\end{pmatrix}.
\end{aligned}
$$

### 3.d. Coordonnées de $U_n$

En écrivant $U_n=\begin{pmatrix}u_n\\v_n\end{pmatrix}$ et $U_0=\begin{pmatrix}u_0\\v_0\end{pmatrix}$, l’égalité $U_n=A^nU_0$ donne

$$
\begin{cases}
u_n=\dfrac12\left(\dfrac34\right)^n\left[(3^{-n}+1)u_0+(1-3^{-n})v_0\right],\\[4pt]
v_n=\dfrac12\left(\dfrac34\right)^n\left[(1-3^{-n})u_0+(1+3^{-n})v_0\right].
\end{cases}
$$

### 4. Limite

Les deux coordonnées $u_n$ et $v_n$ tendent vers 0. Ainsi,

$$
U_n\longrightarrow\begin{pmatrix}0\\0\end{pmatrix},\qquad
X_n-X\longrightarrow\begin{pmatrix}0\\0\end{pmatrix},\qquad
X_n\longrightarrow X=\begin{pmatrix}1\\1\end{pmatrix}.
$$

Cette limite vaut pour tout vecteur initial $X_0$.
