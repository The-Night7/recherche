---
source: "PREING2-S2/Ondes-CC/CC2-2023-2024-Correction_Ondes-CC_P2S2_FPiguet.pdf"
pages: 4
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle des trois pages manuscrites et de la quatrième page d’erratum ; matrices, développements et conditions initiales vérifiés
---

# Ondes — CC2 du 25 avril 2024 — Corrigé et erratum

> Le fichier comprend trois pages de corrigé et une page supplémentaire intitulée « Erreur dans la correction ». L’énoncé n’est pas fourni. L’erratum porte sur la répartition du barème de la question II.2 ; il est intégré ci-dessous.

## Problème I — Chaîne de masses et équation d’onde (8 points ; page 1)

On note $n$ l’indice d’une masse, $m$ sa masse, $K$ la raideur et $a_0$ le pas de la chaîne.

### 1. Forces et deuxième loi de Newton [3 pt]

Les forces sont

$$
f_{n+1\to n}=-K(x_n-x_{n+1}),\qquad
f_{n-1\to n}=-K(x_n-x_{n-1}).
$$

Le barème attribue un point à chacune. La deuxième loi de Newton, pour un point supplémentaire, donne

$$
m\ddot x_n=-K(x_n-x_{n+1})-K(x_n-x_{n-1}),
$$

puis

$$
\ddot x_n+\omega^2(2x_n-x_{n-1}-x_{n+1})=0,
\qquad\omega^2=\frac Km.
$$

> La source écrit $\omega=K/m$ à côté de l’équation ; c’est $\omega^2=K/m$, comme l’imposent la ligne précédente et les dimensions.

### 2. Approximation continue [3 pt]

En posant $x_n(t)=f(na_0,t)$, les développements à l’ordre deux sont

$$
\begin{aligned}
x_{n+1}(t)&=f((n+1)a_0,t)\\
&\simeq f(na_0,t)+a_0\left.\frac{\partial f}{\partial x}\right|_{x=na_0}
+\frac{a_0^2}2\left.\frac{\partial^2f}{\partial x^2}\right|_{x=na_0},
\end{aligned}
$$

$$
\begin{aligned}
x_{n-1}(t)&=f((n-1)a_0,t)\\
&\simeq f(na_0,t)-a_0\left.\frac{\partial f}{\partial x}\right|_{x=na_0}
+\frac{a_0^2}2\left.\frac{\partial^2f}{\partial x^2}\right|_{x=na_0}.
\end{aligned}
$$

Le barème donne un point à chaque développement. Leur substitution dans l’équation discrète annule les termes constants et les dérivées premières :

$$
\frac{\partial^2 f}{\partial t^2}(na_0,t)
-\omega^2a_0^2\frac{\partial^2f}{\partial x^2}(na_0,t)=0.
$$

On obtient l’équation d’onde, pour le dernier point :

$$
\frac{\partial^2 f}{\partial t^2}(x,t)
-\omega^2a_0^2\frac{\partial^2f}{\partial x^2}(x,t)=0,
$$

ou

$$
\frac{\partial^2f}{\partial x^2}
-\frac1{\omega^2a_0^2}\frac{\partial^2f}{\partial t^2}=0.
$$

### 3. Vitesse [2 pt]

Par identification, $1/(a_0^2\omega^2)=1/c^2$, donc $c=a_0\omega$. $c$ est la vitesse de phase.

> Le manuscrit ajoute « $a_0=1/k$ où $k$ est le nombre d’onde ». Cette identification n’est pas déduite du développement : $a_0$ désigne le pas fixe du réseau, alors que le nombre d’onde d’une perturbation peut varier. Elle n’est pas nécessaire pour obtenir $c=a_0\omega$.

## Problème II — Deux masses couplées (12 points ; pages 2 et 3)

### 1. Forces [2 pt]

Le schéma représente, de gauche à droite, un support fixe, la masse $m_1$, puis la masse $m_2$, reliés successivement par des ressorts. Les déplacements $x_1,x_2$ sont orientés vers la droite.

$$
\vec F_1=-Kx_1\vec u_x-K(x_1-x_2)\vec u_x,
\qquad\vec F_2=-K(x_2-x_1)\vec u_x.
$$

Un point est attribué à chaque force.

### 2. Équations et matrice [2 pt, erratum page 4]

Avec $\omega_1^2=K/m_1$ et $\omega_2^2=K/m_2$,

$$
\begin{cases}
\ddot x_1=\omega_1^2(x_2-2x_1),\\
\ddot x_2=\omega_2^2(x_1-x_2).
\end{cases}
$$

D’où

$$
\begin{pmatrix}\ddot x_1\\\ddot x_2\end{pmatrix}
+W\begin{pmatrix}x_1\\x_2\end{pmatrix}=\vec0,
\qquad
W=\begin{pmatrix}2\omega_1^2&-\omega_1^2\\-\omega_2^2&\omega_2^2\end{pmatrix}.
$$

**Erratum intégré.** La page 2 donnait un point pour chacune des deux équations et un point pour la matrice, malgré un total annoncé de deux. La page 4 remplace les deux premiers « 1 pt » par « 0,5 pt » ; la matrice reste notée sur un point.

### 3. Valeurs propres et pulsations propres [2 pt]

La suite se place dans le cas $\omega_1=\omega_2=\omega$. Les valeurs propres sont notées $\lambda^2$ :

$$
\det\begin{pmatrix}2\omega^2-\lambda^2&-\omega^2\\-\omega^2&\omega^2-\lambda^2\end{pmatrix}=0.
$$

Donc

$$
(2\omega^2-\lambda^2)(\omega^2-\lambda^2)-\omega^4=0,
\qquad\lambda^4-3\omega^2\lambda^2+\omega^4=0.
$$

En résolvant le trinôme en $\lambda^2$,

$$
\lambda_\pm^2=\frac{3\omega^2\pm\sqrt{9\omega^4-4\omega^4}}2
=\omega^2\frac{3\pm\sqrt5}2.
$$

Les pulsations propres sont

$$
\omega_\pm=\lambda_\pm=\omega\sqrt{\frac{3\pm\sqrt5}2}.
$$

### 4. Vecteurs propres [2 pt]

Pour $\vec V_\pm=(a_\pm,b_\pm)^{\mathsf T}$,

$$
\begin{cases}
(2\omega^2-\lambda_\pm^2)a_\pm=\omega^2b_\pm,\\
-\omega^2a_\pm=(\lambda_\pm^2-\omega^2)b_\pm.
\end{cases}
$$

En additionnant,

$$
(\omega^2-\lambda_\pm^2)a_\pm=\lambda_\pm^2b_\pm.
$$

On peut choisir

$$
\vec V_+=\begin{pmatrix}\lambda_+^2\\\omega^2-\lambda_+^2\end{pmatrix},
\qquad
\vec V_-=\begin{pmatrix}\lambda_-^2\\\omega^2-\lambda_-^2\end{pmatrix},
\qquad\lambda_\pm^2=\omega_\pm^2.
$$

Un point est attribué à chaque vecteur.

> Dans la matrice manuscrite de cette question, le signe moins devant l’élément supérieur droit est omis. Les deux équations développées, la matrice $W$ de II.2 et les vecteurs finaux sont cohérents avec $-\omega^2$.

### 5. Modes propres [2 pt]

Les modes sont

$$
\vec x_\pm(t)=e^{i\omega_\pm t}\vec V_\pm
$$

et leurs conjugués complexes.

### 6. Conditions initiales et solution [2 pt]

La solution générale est

$$
\vec x(t)=a\vec x_+(t)+b\vec x_+^*(t)
+c\vec x_-(t)+d\vec x_-^*(t).
$$

La condition $\vec x(0)=\vec0$ impose

$$
(a+b)\vec V_++(c+d)\vec V_-=\vec0,
\qquad a=-b,\quad c=-d.
$$

La condition sur la vitesse est

$$
\dot{\vec x}(0)=
(i\lambda_+a-i\lambda_+b)\vec V_+
+(i\lambda_-c-i\lambda_-d)\vec V_-
=\begin{pmatrix}0\\-v_0\end{pmatrix}.
$$

Le corrigé donne

$$
a=\frac{iv_0(\omega^2-\lambda_+^2)}
{2\lambda_+[\lambda_+^4+(\omega^2-\lambda_+^2)^2]},
$$

$$
c=\frac{iv_0(\omega^2-\lambda_-^2)}
{2\lambda_-[\lambda_-^4+(\omega^2-\lambda_-^2)^2]}.
$$

Finalement,

$$
\vec x(t)=2ia\sin(\lambda_+t)\vec V_+
+2ic\sin(\lambda_-t)\vec V_-.
$$
