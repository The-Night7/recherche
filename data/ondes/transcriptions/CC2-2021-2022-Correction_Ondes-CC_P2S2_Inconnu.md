---
source: "PREING2-S2/Ondes-CC/CC2-2021-2022-Correction_Ondes-CC_P2S2_Inconnu.pdf"
pages: 3
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale des trois pages manuscrites ; matrices, modes propres et conditions initiales vérifiés
---

# Ondes — CC2 2021–2022 — Corrigé

> Corrigé seul : l’énoncé n’est pas contenu dans ce fichier. Les réponses et les indications de barème sont transcrites ; les indices manifestement fautifs sont signalés. On note $n$ l’indice d’une masse et $m$ sa masse.

## 1. Chaîne de masses et ressorts (page 1)

**1. [1 pt]** Force exercée sur la masse $n$ par le ressort du côté $n+1$ :

$$
f_{n+1\to n}=-k_0(x_n-x_{n+1}).
$$

**2. [1 pt]** Force du côté $n-1$ :

$$
f_{n-1\to n}=-k_0(x_n-x_{n-1}).
$$

**3. [2 pt]** Le principe fondamental de la dynamique donne

$$
m\ddot x_n=-k_0(x_n-x_{n+1})-k_0(x_n-x_{n-1}),
$$

soit, avec $\omega_0^2=k_0/m$,

$$
\ddot x_n+\omega_0^2(2x_n-x_{n-1}-x_{n+1})=0.
$$

> Le signe du premier terme de force est peu net dans la ligne manuscrite du bilan ; les deux forces précédentes et l’équation finale fixent sans ambiguïté les deux signes moins.

## 2. Deux masses et modes propres (pages 1 à 3)

### 1. Équations [2 pt]

Avec les extrémités fixes $x_0=0$ et $x_3=0$,

$$
\begin{cases}
\ddot x_1+\omega_0^2(2x_1-x_2)=0,\\
\ddot x_2+\omega_0^2(2x_2-x_1)=0.
\end{cases}
$$

### 2. Forme matricielle [2 pt]

Pour $\vec X=(x_1,x_2)^{\mathsf T}$,

$$
\frac{d^2\vec X}{dt^2}=A\vec X,
\qquad
A=\begin{pmatrix}-2\omega_0^2&\omega_0^2\\\omega_0^2&-2\omega_0^2\end{pmatrix}
=\omega_0^2\begin{pmatrix}-2&1\\1&-2\end{pmatrix}.
$$

### 3. Valeurs propres [2 pt]

On résout $A\vec X=\lambda\vec X$, donc $\det(A-\lambda I_2)=0$. Les valeurs propres sont

$$
\lambda_1=-\omega_0^2,\qquad\lambda_2=-3\omega_0^2.
$$

### 4. Vecteurs propres [2 pt]

$$
\vec V_1=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},
\qquad
\vec V_2=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.
$$

Les versions non normalisées $(1,1)^{\mathsf T}$ et $(1,-1)^{\mathsf T}$ sont également acceptées.

### 5.a. Déplacements initiaux opposés [4 pt de calcul, puis 2 pt pour les positions]

Le corrigé utilise les quatre coefficients $\alpha,\beta,\gamma,\delta$ des exponentielles modales. Les conditions $x_1(0)=a_0$, $x_2(0)=-a_0$ donnent

$$
\begin{cases}
\dfrac{\alpha+\beta+\gamma+\delta}{\sqrt2}=a_0,\quad(1)\\
\dfrac{\alpha+\beta-\gamma-\delta}{\sqrt2}=-a_0.\quad(2)
\end{cases}
$$

La somme donne $\alpha=-\beta$.

La vitesse initiale est nulle :

$$
\dot{\vec X}(0)=i\omega_0\alpha\vec V_1-i\omega_0\beta\vec V_1
+i\sqrt3\omega_0\gamma\vec V_2-i\sqrt3\omega_0\delta\vec V_2=\vec0.
$$

Après division par $i\omega_0$ et projection,

$$
\begin{cases}
\alpha-\beta+\sqrt3\gamma-\sqrt3\delta=0,\quad(3)\\
\alpha-\beta-\sqrt3\gamma+\sqrt3\delta=0.\quad(4)
\end{cases}
$$

La somme donne $\alpha=\beta$. Donc $\alpha=\beta=0$.

La différence $(1)-(2)$ donne $2(\gamma+\delta)=2a_0\sqrt2$. La différence $(3)-(4)$ donne $2\sqrt3(\gamma-\delta)=0$, d’où $\delta=\gamma$. En revenant à (1),

$$
\frac{2\delta}{\sqrt2}=a_0,
\qquad\gamma=\delta=\frac{a_0}{\sqrt2}.
$$

Par conséquent,

$$
\begin{aligned}
\vec X(t)
&=\frac{a_0}{\sqrt2}e^{i\omega_2t}\vec V_2
+\frac{a_0}{\sqrt2}e^{-i\omega_2t}\vec V_2\\
&=\frac{a_0}2(e^{i\omega_2t}+e^{-i\omega_2t})
\begin{pmatrix}1\\-1\end{pmatrix},
\qquad\omega_2=\sqrt3\omega_0.
\end{aligned}
$$

Ainsi

$$
\begin{cases}
x_1(t)=a_0\cos(\omega_2t),\\
x_2(t)=-a_0\cos(\omega_2t).
\end{cases}
$$

> La dernière ligne de la page 2 répète par erreur l’indice $1$ ; il s’agit de $x_2$, comme le montre le vecteur qui précède.

### 5.b. Déplacements initiaux égaux [4 pt de calcul, puis 2 pt pour les positions]

Cette fois, $x_1(0)=x_2(0)=a_0$ :

$$
\begin{cases}
\dfrac{\alpha+\beta+\gamma+\delta}{\sqrt2}=a_0,\quad(1)\\
\dfrac{\alpha+\beta-\gamma-\delta}{\sqrt2}=a_0.\quad(2)
\end{cases}
$$

Les deux équations de vitesse restent

$$
\begin{cases}
\alpha-\beta+\sqrt3\gamma-\sqrt3\delta=0,\quad(3)\\
\alpha-\beta-\sqrt3\gamma+\sqrt3\delta=0.\quad(4)
\end{cases}
$$

On obtient $\alpha=\beta$, tandis que $(1)-(2)$ donne $\gamma=-\delta$. Alors

$$
\frac{2\alpha}{\sqrt2}=a_0,
\qquad\alpha=\beta=\frac{a_0}{\sqrt2}.
$$

La différence $(3)-(4)$ impose $\gamma=\delta$, donc $\gamma=\delta=0$. Finalement,

$$
\vec X(t)=\left(\frac{a_0}{\sqrt2}e^{i\omega_1t}
+\frac{a_0}{\sqrt2}e^{-i\omega_1t}\right)\vec V_1
=a_0\cos(\omega_1t)\begin{pmatrix}1\\1\end{pmatrix},
$$

avec $\omega_1=\omega_0$. Les positions sont

$$
x_1(t)=a_0\cos(\omega_1t),\qquad x_2(t)=a_0\cos(\omega_1t).
$$
