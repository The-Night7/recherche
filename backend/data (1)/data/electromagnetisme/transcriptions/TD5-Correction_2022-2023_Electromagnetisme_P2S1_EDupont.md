---
source: "PREING2-S1/Electromagnetisme/TD5-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf"
pages: 5
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des cinq pages ; calculs, signes du produit vectoriel et unités vérifiés ; erreurs du support signalées
---

# TD 5 — Force de Lorentz — correction 2022–2023

## Page 1 — Force magnétique sur une charge en mouvement

### Rappel

$$\vec f=q\vec v\wedge\vec B.$$

- $\vec f$ : force de Lorentz, en newtons (N).
- $q$ : charge, en coulombs (C).
- $\vec B$ : champ magnétique, en teslas (T).
- $\vec v$ : vitesse, en $\mathrm{m\,s^{-1}}$.

Le dessin de la main illustre la direction du produit vectoriel pour une charge positive.

### Exercice 1 a

Un proton se déplace vers la droite à $3\,000\ \mathrm{m\,s^{-1}}$ dans un champ de $10\ \mathrm G$ orienté dans la direction indiquée sur la figure. Quelle est la force sur ce proton ?

**Figure.** La vitesse est portée par $+Ox$. Le champ est dans $(Oxy)$, à $70^\circ$ de $+Ox$, vers les $y$ positifs. La force sort du plan de la figure, suivant $+Oz$.

Pour le proton,

$$q=|e|=1{,}602\times10^{-19}\ \mathrm C.$$

La force vaut $\vec F=q\vec v\wedge\vec B$, de norme

$$
\|\vec F\|=|q|\,\|\vec v\|\,\|\vec B\|
\left|\sin\widehat{(\vec v,\vec B)}\right|.
$$

Application numérique :

$$
F=1{,}602\times10^{-19}\times3\,000\times(10\times10^{-4})
\sin70^\circ
=4{,}516\times10^{-19}\ \mathrm N.
$$

Composantes :

$$
\vec F=q
\begin{pmatrix}v\\0\\0\end{pmatrix}
\wedge
\begin{pmatrix}B\cos70^\circ\\B\sin70^\circ\\0\end{pmatrix}
=
\begin{pmatrix}0\\0\\qvB\sin70^\circ\end{pmatrix}.
$$

> La marge indique correctement $1\ \mathrm T=10^4\ \mathrm G$, puis écrit $1\ \mathrm G=10^4\ \mathrm T$ sans le signe moins. Il faut lire $1\ \mathrm G=10^{-4}\ \mathrm T$, comme dans l’application numérique.

## Page 2 — Champ inconnu et spectromètre

En haut de page, l’annotation oppose « Lorentz : seulement $\vec B$ », avec $q\vec v\wedge\vec B$, à « Laplace : $\vec E$ et $\vec B$ », avec $q(\vec v\wedge\vec B+\vec E)$.

> Correction terminologique : la force $q(\vec E+\vec v\wedge\vec B)$ est la force de Lorentz complète. La force de Laplace désigne la force magnétique exercée sur un conducteur parcouru par un courant.

### Exercice 1 b

Une charge de $1\ \mu\mathrm C$ se déplace dans une région où le champ magnétique est uniforme. Elle ne subit pas de force quand elle se dirige avec une vitesse de $5\ \mathrm{m\,s^{-1}}$ dans la direction des $x$ positifs. Elle subit cependant une force de $10^{-7}\ \mathrm N$ dans la direction des $z$ positifs quand sa vitesse est

$$\vec v=(3\vec i+4\vec j)\ \mathrm{m\,s^{-1}}.$$

Quel est le champ magnétique ?

Données : $q=10^{-6}\ \mathrm C$. Pour $\vec v=v_x\vec i$, $v_x=5\ \mathrm{m\,s^{-1}}$, la force est nulle. Donc

$$
\vec v\wedge\vec B=\vec0
\quad\Longrightarrow\quad\vec v\parallel\vec B,
\qquad\vec B=B_x\vec i.
$$

Pour la seconde vitesse,

$$
\vec F=q
\begin{pmatrix}3\\4\\0\end{pmatrix}
\wedge
\begin{pmatrix}B_x\\0\\0\end{pmatrix}
=q\begin{pmatrix}0\\0\\-4B_x\end{pmatrix}
=-4qB_x\vec k.
$$

Ainsi

$$
B_x=\frac{F_z}{-4q}
=-\frac{10^{-7}}{4\times10^{-6}}
=-0{,}25\times10^{-1}\ \mathrm T
=-0{,}025\ \mathrm T.
$$

Résultat encadré : $\boxed{\vec B=-0{,}025\vec i\ \mathrm T}$.

### Exercice 2 — Spectromètre de masse

On envoie un atome de krypton ionisé une fois avec une vitesse de $40\,000\ \mathrm{m\,s^{-1}}$ dans un spectromètre de masse où il y a un champ magnétique de $0{,}6\ \mathrm T$. L’atome frappe la plaque à une distance de $11{,}044\ \mathrm{cm}$ du point d’entrée.

1. Quelle est la masse de l’atome ?
2. De quel isotope de l’atome pourrait-il s’agir ?

Données :

$$
|q|=e=1{,}602\times10^{-19}\ \mathrm C,\quad
B=0{,}6\ \mathrm T,\quad v=4\times10^4\ \mathrm{m\,s^{-1}},\quad
2R=11{,}044\ \mathrm{cm}.
$$

**Figure.** L’ion $\mathrm{Kr}^+$ décrit un demi-cercle de rayon $R$ ; le champ sort du plan. La vitesse est tangentielle. Le vecteur $\vec u_r$ est radial vers l’extérieur et l’accélération est centripète.

$$
\vec F=m\vec a=q\vec v\wedge\vec B.
$$

En coordonnées polaires, pour $R$ constant,

$$
\vec a(t)=-R\dot\theta^2\vec u_r+R\ddot\theta\vec u_\theta
=-\frac{v^2}{R}\vec u_r+R\ddot\theta\vec u_\theta,
\qquad\vec v=R\dot\theta\vec u_\theta.
$$

## Page 3 — Masse du krypton et mouvement du proton

Suite du calcul du spectromètre :

$$
qR\dot\theta\vec u_\theta\wedge B\vec u_z
=qR\dot\theta B\vec u_r
=m\left(-\frac{v^2}{R}\vec u_r+R\ddot\theta\vec u_\theta\right).
$$

En norme,

$$
|q|\,|v|B=\frac{mv^2}{R}
\quad\Longrightarrow\quad
|q|RB=m|v|.
$$

Donc

$$
m=\frac{|q|RB}{v}
=\frac{1{,}602\times10^{-19}\times
\left(\frac12\times11{,}044\times10^{-2}\right)\times0{,}6}
{4\times10^4}
=1{,}327\times10^{-25}\ \mathrm{kg}.
$$

La note donne $m=79{,}62\ \mathrm u$ et $N_A=6\times10^{23}\ \mathrm{mol^{-1}}$.

**Réponse b :** isotope 80 du krypton.

### Exercice 3 — Force de Lorentz

Un proton de charge $q=1{,}60\times10^{-19}\ \mathrm C$ et de masse $m=1{,}67\times10^{-27}\ \mathrm{kg}$ se trouve dans un champ magnétique uniforme d’intensité $B=0{,}5\ \mathrm T$. On appelle $x$ l’axe qui pointe dans la direction de ce champ.

À $t=0$, le proton se trouve en $(0,0,0)$ et sa vitesse vérifie

$$
v_x(0)=1{,}5\times10^5\ \mathrm{m\,s^{-1}},\quad
v_y(0)=0,\quad
v_z(0)=2{,}0\times10^5\ \mathrm{m\,s^{-1}}.
$$

> Les signes moins des exposants de $q$ et $m$ sont absents dans l’énoncé imprimé de cette version. Les valeurs physiques du proton sont explicitées ci-dessus.

Notations :

$$
\vec B=B\vec e_x,\quad
\vec v(0)=v_x^0\vec e_x+v_z^0\vec e_z,\quad
\overrightarrow{OM}(0)=\vec0,
$$

avec $v_x^0=v_x(0)$ et $v_z^0=v_z(0)$.

#### a. Deuxième loi de Newton à $t=0$

$$
m\vec a=q
\begin{pmatrix}v_x^0\\0\\v_z^0\end{pmatrix}
\wedge
\begin{pmatrix}B\\0\\0\end{pmatrix}
=q\begin{pmatrix}0\\v_z^0B\\0\end{pmatrix}.
$$

D’où

$$
\vec a(0)=\frac{qv_z^0B}{m}\vec e_y\ne\vec0,
\qquad\dot v_x(0)=0,\quad
\dot v_y(0)=\frac{qv_z^0B}{m},\quad\dot v_z(0)=0.
$$

À $t>0$, le proton a désormais une vitesse à trois composantes non nulles, tandis que $\vec B$ reste uniforme, constant et orienté suivant $x$.

#### b. Équations différentielles du premier ordre

$$
m\vec a=q
\begin{pmatrix}v_x\\v_y\\v_z\end{pmatrix}
\wedge
\begin{pmatrix}B\\0\\0\end{pmatrix}
=q\begin{pmatrix}0\\v_zB\\-v_yB\end{pmatrix}.
$$

## Page 4 — Résolution des équations

$$
\boxed{\dot v_x=0}\tag{1}
$$

$$
\boxed{\dot v_y=\frac{qB}{m}v_z}\tag{2}
$$

$$
\boxed{\dot v_z=-\frac{qB}{m}v_y}\tag{3}
$$

#### c. Équations du second ordre

On note $\vec\Omega=-\dfrac qm\vec B$ et

$$
\Omega=\|\vec\Omega\|=\frac{qB}{m},\qquad
\Omega^2=\vec\Omega\cdot\vec\Omega=\left(\frac{qB}{m}\right)^2.
$$

D’après (1), $v_x(t)=v_x^0$ est constant, donc

$$x(t)=v_x^0t+x(0)=v_x^0t.$$

En dérivant (2) et en utilisant (3),

$$
\ddot v_y=\frac{qB}{m}\dot v_z
=\frac{qB}{m}\left(-\frac{qB}{m}v_y\right)
=-\Omega^2v_y.
$$

De même, $\ddot v_z=-\Omega^2v_z$. Pour l’équation générique

$$\ddot v+\Omega^2v=0,$$

l’équation caractéristique est $r^2+\Omega^2=0$ et

$$
v(t)=A\cos\Omega t+B\sin\Omega t,
\qquad A=v(0),\quad B=\frac{\dot v(0)}\Omega.
$$

Pour $v_y$ : $v_y(0)=0$ et $\dot v_y(0)=\Omega v_z^0$, donc

$$\boxed{v_y(t)=v_z^0\sin\Omega t}.$$

Pour $v_z$ : $v_z(0)=v_z^0$ et $\dot v_z(0)=-\Omega v_y(0)=0$, donc

$$\boxed{v_z(t)=v_z^0\cos\Omega t}.$$

#### d. Nature de la trajectoire

Montrer que la trajectoire est une hélice d’axe la droite parallèle à $x$ d’équations $z=0$, $y=R$, de rayon $R=v_z(0)/\Omega$ et de pas $v_x(0)\,2\pi/\Omega$.

Le mouvement selon $x$ est rectiligne : $x(t)=v_x^0t$.

## Page 5 — Hélice

L’intégration des deux autres composantes donne

$$
y(t)=-\frac{v_z^0}\Omega\cos\Omega t+C_y,
\qquad z(t)=\frac{v_z^0}\Omega\sin\Omega t+C_z.
$$

À $t=0$, $y=z=0$. En posant $R=v_z^0/\Omega$,

$$
\boxed{y(t)=R(1-\cos\Omega t)},\qquad
\boxed{z(t)=R\sin\Omega t}.
$$

Dans le plan $(Oyz)$, la projection est un cercle de centre $(R,0)$ et de rayon $R$. Le dessin repère :

- $t=0$ et $t=2\pi/\Omega$ : $(y,z)=(0,0)$ ;
- $t=\pi/(2\Omega)$ : $(R,R)$ ;
- $t=\pi/\Omega$ : $(2R,0)$ ;
- $t=3\pi/(2\Omega)$ : $(R,-R)$.

La trajectoire est une **hélice** d’axe la droite parallèle à $x$ d’équations $y=R$, $z=0$, de rayon $R=v_z^0/\Omega$, de pas

$$
x\left(\frac{2\pi}\Omega\right)-x(0)
=v_x^0\frac{2\pi}\Omega.
$$
