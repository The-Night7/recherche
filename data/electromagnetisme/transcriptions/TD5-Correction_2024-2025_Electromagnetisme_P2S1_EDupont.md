---
source: "PREING2-S1/Electromagnetisme/TD5-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf"
pages: 3
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des trois pages ; équations et applications numériques vérifiées ; constantes d’intégration clarifiées
---

# TD 5 — Force de Lorentz — correction 2024–2025

## Page 1 — Exercice 2 : force de Lorentz

Un proton ($q=1{,}60\times10^{-19}\ \mathrm C$, $m=1{,}67\times10^{-27}\ \mathrm{kg}$) se trouve dans un champ magnétique uniforme d’intensité $B=0{,}5\ \mathrm T$. On appelle $x$ l’axe qui pointe dans la direction de ce champ.

À $t=0$, le proton est au point $(0,0,0)$, avec

$$
v_x(0)=1{,}5\times10^5\ \mathrm{m\,s^{-1}},\qquad
v_y(0)=0,\qquad
v_z(0)=2{,}0\times10^5\ \mathrm{m\,s^{-1}}.
$$

1. À l’aide de la deuxième loi de Newton, écrire les équations différentielles du premier ordre pour $v_x$, $v_y$ et $v_z$ à $t\geq0$. On note $\vec\Omega=-\dfrac qm\vec B$.
2. Établir les deux équations différentielles du second ordre pour $v_y$ et $v_z$.

**Annotations.** En notant $\Omega=\|\vec\Omega\|=qB/m$,

$$
\begin{cases}
\ddot v_y+\Omega^2v_y=0,\\
\ddot v_z+\Omega^2v_z=0,
\end{cases}
\qquad
\begin{cases}
v_x=v_x^0,\\
v_y=v_z^0\sin\Omega t,\\
v_z=v_z^0\cos\Omega t.
\end{cases}
$$

3. Montrer que la trajectoire du proton est une hélice d’axe la droite parallèle à $x$ d’équations $z=0$, $y=R$, de rayon $R=v_z(0)/\Omega$ et de pas $v_x(0)\,2\pi/\Omega$.

**Recherche de $x(t)$, $y(t)$, $z(t)$.**

$$
v_x=v_x^0=\frac{\mathrm dx}{\mathrm dt}
\quad\Longrightarrow\quad
\int_{x(0)}^{x(t)}\mathrm dx=\int_0^t v_x^0\,\mathrm dt.
$$

La vitesse $v_x^0$ est constante, donc

$$
x(t)-x(0)=v_x^0(t-0),\qquad
\boxed{x(t)=v_x^0t},
$$

puisque $\overrightarrow{OM}(0)=\vec0$.

Les autres composantes s’intègrent en

$$
y(t)=-\frac{v_z^0}\Omega\cos\Omega t+C_y,\qquad
z(t)=\frac{v_z^0}\Omega\sin\Omega t+C_z.
$$

La condition $y(0)=0$ impose $C_y=v_z^0/\Omega=R$ ; $z(0)=0$ impose $C_z=0$.

> Le manuscrit note d’abord les constantes d’intégration « $y(0)$ » et « $z(0)$ ». Ce sont des constantes à déterminer ; $C_y$ n’est pas la position initiale $y(0)$.

## Page 2 — Hélice et spectromètre de masse

Suite de l’exercice 2 :

$$
\boxed{\begin{aligned}
x(t)&=v_x^0t,\\
y(t)&=R(1-\cos\Omega t),\\
z(t)&=R\sin\Omega t.
\end{aligned}}
$$

Le mouvement selon $x$ est rectiligne. La projection dans $(Oyz)$ est circulaire, de centre $(R,0)$ et de rayon $R$. Le cercle est repéré aux instants $0$, $\pi/(2\Omega)$, $\pi/\Omega$, $3\pi/(2\Omega)$, $2\pi/\Omega$. Le schéma suivant représente l’hélice et son axe parallèle au champ $\vec B$.

Le pas vaut

$$x\left(\frac{2\pi}\Omega\right)=v_x^0\frac{2\pi}\Omega.$$

Le bas du schéma rappelle les équations du premier ordre :

$$
\begin{cases}
\dot v_x=0,\\
\dot v_y=(q/m)v_zB,\\
\dot v_z=-(q/m)v_yB,
\end{cases}
\qquad\vec a=\frac qm\vec v\wedge\vec B.
$$

### Exercice 3 — Spectromètre de masse

On envoie un atome de krypton ionisé une fois avec une vitesse de $40\,000\ \mathrm{m\,s^{-1}}$ dans un spectromètre de masse où règne un champ magnétique uniforme et constant de $0{,}6\ \mathrm T$. L’atome frappe la plaque à une distance de $11{,}044\ \mathrm{cm}$ du point d’entrée.

1. Quelle est la masse de l’atome ?
2. De quel isotope de l’atome pourrait-il s’agir ?

**Figure.** La trajectoire photographiée est un demi-cercle dans $(Oyz)$, d’un point d’entrée en $O$ jusqu’à un point d’impact à la distance $d=2R$. Le champ sort du plan.

$$
R=\frac{v_z(0)}\Omega,\qquad\Omega=\frac{|q|B}{m}.
$$

Donc

$$
d=\frac{2vm}{|q|B}
\quad\Longrightarrow\quad
m=\frac d2\frac{|q|B}{v}.
$$

Application numérique :

$$
m=\frac{11{,}044\times10^{-2}}2
\frac{1{,}602\times10^{-19}\times0{,}6}{40\,000}
=1{,}327\times10^{-25}\ \mathrm{kg}.
$$

> Erreur numérique du manuscrit : le résultat est écrit $1{,}327\times10^{-15}\ \mathrm{kg}$ sur la page. Le calcul avec les données indiquées donne $1{,}327\times10^{-25}\ \mathrm{kg}$, valeur reproduite ci-dessus.

L’isotope proposé est le **krypton 80**.

## Page 3 — Exercice 4 : champs électrique et magnétique

Une particule de masse $m$ et de charge $q$ entre avec une vitesse $\vec v_0=v_0\vec u_x$ dans une zone où existent un champ électrique $\vec E=E_0\vec u_y$ et un champ magnétique $\vec B=B_0\vec u_z$, uniformes et stationnaires.

1. À quelle condition le vecteur vitesse de la particule reste-t-il inchangé ?
2. Expliquer comment ce dispositif peut être adapté en sélecteur de vitesse.

### 1. Vitesse inchangée

La deuxième loi de Newton donne

$$
m\frac{\mathrm d\vec v}{\mathrm dt}=q(\vec E+\vec v\wedge\vec B).
$$

En composantes,

$$
\frac mq
\begin{pmatrix}\dot v_x\\\dot v_y\\\dot v_z\end{pmatrix}
=
\begin{pmatrix}0\\E_0\\0\end{pmatrix}
+
\begin{pmatrix}v_x\\v_y\\v_z\end{pmatrix}
\wedge
\begin{pmatrix}0\\0\\B_0\end{pmatrix}
=
\begin{pmatrix}v_yB_0\\E_0-v_xB_0\\0\end{pmatrix}.
$$

Avec $\vec v(0)=(v_0,0,0)$,

$$
\begin{cases}
\dot v_x=(qB_0/m)v_y,\\
\dot v_y=(q/m)(E_0-v_xB_0),\\
\dot v_z=0.
\end{cases}
$$

La vitesse reste inchangée si, pour tout $t$,

$$
\dot v_x=\dot v_y=0,
\qquad v_y=0,\qquad E_0-v_xB_0=0,
\qquad v_z=v_z(0)=0.
$$

Ainsi

$$
\vec v=\begin{pmatrix}v_x=E_0/B_0=v_x(0)=v_0\\0\\0\end{pmatrix},
\qquad\boxed{v_0=\frac{E_0}{B_0}}.
$$

### 2. Sélecteur de vitesse

Le dessin représente $\vec E$ suivant $+Oy$, $\vec B$ sortant du plan, et une trajectoire rectiligne suivant $+Ox$ entre deux limites verticales. D’autres trajectoires sont déviées. On sélectionne les trajectoires rectilignes telles que $v_0=E_0/B_0$.
