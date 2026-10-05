---
source: "PREING2-S1/Electromagnetisme/TD7-Correction_2022-2023_Electromagnetisme_P2S1_EDupont.pdf"
pages: 5
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des cinq pages ; topologie des circuits décrite ; équations de nœuds et de mailles ainsi que régime transitoire vérifiés
---

# TD 7 — Électrocinétique — correction 2022–2023

## Page 1 — Exercice 1 : générateur de courant

Soit le circuit suivant, composé d’un générateur de courant $I$ et de deux résistances. Quelle est la valeur de la tension $V$ aux bornes du générateur de courant ?

**Circuit.** Un générateur impose un courant $I=1\ \mathrm{mA}$, ascendant dans la branche de gauche. Le courant traverse successivement $R_1=1\ \mathrm{k\Omega}$ en haut et $R_2=2\ \mathrm{k\Omega}$ à droite, puis retourne au générateur par la masse commune. Les tensions $V$, $V_1$ et $V_2$ sont orientées respectivement vers le haut, vers la gauche et vers le haut.

Attention aux unités :

$$I=10^{-3}\ \mathrm A,\qquad R_1=10^3\ \Omega,\qquad R_2=2\times10^3\ \Omega.$$

### Conventions

Deux types de composants sont rappelés :

- **Générateur :** tension et courant sont orientés dans le même sens (convention générateur).
- **Récepteur**, par exemple résistance ou condensateur : tension et courant sont de sens opposés (convention récepteur). Pour une résistance parcourue de $A$ vers $B$, $V_{AB}=+RI$.

L’exemple d’une pile de $5\ \mathrm V$ et d’une lampe dans une seule maille indique $U_{\text{lampe}}=U_{\text{pile}}=5\ \mathrm V$.

Le circuit de l’énoncé est redessiné avec les deux résistances en série dans une même branche. La loi des mailles donne

$$V-V_1-V_2=0\quad\Longleftrightarrow\quad V=V_1+V_2.$$

Par la loi d’Ohm,

$$V_1=R_1I,\qquad V_2=R_2I.$$

D’où

$$
\boxed{V=(R_1+R_2)I=(1+2)\times10^3\times(1\times10^{-3})=3\ \mathrm V}.
$$

$R_{\mathrm{eq}}=R_1+R_2$ est la résistance équivalente de deux résistances en série.

Note de marge : loi d’Ohm locale, $\vec j=\sigma\vec E$.

## Page 2 — Exercice 2 : résistance équivalente

Soit le réseau de résistances suivant. Calculer la valeur de la résistance équivalente $R_{AB}$ entre $A$ et $B$.

**Description du réseau.** De $A$ à un nœud $C$, une résistance de $1\ \mathrm{k\Omega}$. Entre $C$ et un nœud $E$, deux branches en parallèle : la branche supérieure comporte deux résistances de $1\ \mathrm{k\Omega}$ en série ; l’autre comporte une résistance de $2\ \mathrm{k\Omega}$. De $E$ à $B$, une résistance de $1\ \mathrm{k\Omega}$. Une branche inférieure relie directement $C$ à $B$ par deux résistances de $1\ \mathrm{k\Omega}$ en série. Les points $C$ et $D$ dessinés sur le même fil sont au même potentiel : $V_C=V_D$, le fil étant de résistance nulle.

1. Dans la branche supérieure, $1+1=2\ \mathrm{k\Omega}$.
2. Les deux résistances de $2\ \mathrm{k\Omega}$ entre $C$ et $E$ sont en parallèle. Pour deux résistances en parallèle,

$$\frac1{R_{\mathrm{eq}}}=\frac1{R_1}+\frac1{R_2}.$$

Ici, en exprimant les résistances en $\mathrm{k\Omega}$,

$$\frac1{R_{\mathrm{eq}}}=\frac12+\frac12=1,
\qquad R_{\mathrm{eq}}=1\ \mathrm{k\Omega}.$$

3. Cette résistance est en série avec celle de $1\ \mathrm{k\Omega}$ entre $E$ et $B$, soit $2\ \mathrm{k\Omega}$.
4. La branche inférieure vaut elle aussi $1+1=2\ \mathrm{k\Omega}$. Entre $C$ et $B$, on obtient donc $2\parallel2=1\ \mathrm{k\Omega}$.
5. On ajoute la résistance de $1\ \mathrm{k\Omega}$ située entre $A$ et $C$ :

$$\boxed{R_{AB}=2\ \mathrm{k\Omega}}.$$

Les dessins successifs illustrent chacune de ces réductions du même réseau.

## Page 3 — Exercice 3 : association de dipôles

Soit le montage suivant, avec

$$\eta=0{,}2\ \mathrm A,\qquad E=3\ \mathrm V,\qquad R=5\ \Omega.$$

**Circuit et conventions.** Les nœuds $D$, $C$ et $M$ sont reliés par un fil horizontal inférieur. Une source de tension entre $D$ et $E$ impose $E=V_E-V_D$. Une résistance $2R$ relie $E$ au nœud supérieur $A$ ; le courant $i$ la traverse vers $A$. Une seconde résistance $2R$ relie $A$ à $D$, parcourue par $i_2$ vers le bas. Une résistance $R$ relie $A$ à $B$, parcourue par $i_1$ vers $B$ ; la tension recherchée $u$ est orientée vers $B$, donc $u=V_B-V_A$. Entre $B$ et $C$ se trouve $3R$, parcourue par $i_3$ vers le bas. Enfin une source de courant entre $B$ et $M$ impose $\eta$ vers le bas.

Quatre inconnues : $i$, $i_1$, $i_2$, $i_3$.

### Loi des nœuds

En $A$ et $B$ :

$$i=i_1+i_2\tag{i}$$

$$i_1=\eta+i_3.\tag{ii}$$

Les nœuds $D$ et $C$ donnent les mêmes relations avec le courant de retour $i_4$ : $i_4+i_2=i$ et $i_3+\eta=i_4$.

### Loi des mailles

La résistance $R$ donne $u=-Ri_1$.

Dans la maille de gauche, en notant $F$ le point du fil supérieur relié à $A$,

$$u_{ED}+u_{FE}+u_{AF}+u_{DA}=0.$$

Avec $u_{AF}=0$, $u_{ED}=E$, $u_{FE}=-2Ri$ et $u_{DA}=-2Ri_2$,

$$E=2R(i+i_2).\tag{iii}$$

Dans la maille centrale,

$$u_{DC}+u_{AD}+u+u_{CB}=0.$$

Puisque $u_{DC}=0$,

$$
u_{AD}=u_{BC}-u,
\qquad 2Ri_2=3Ri_3-(-Ri_1),
$$

soit

$$2i_2=3i_3+i_1.\tag{iv}$$

On dispose de quatre équations couplées pour quatre inconnues.

## Page 4 — Résolution et circuit RL

### Fin de l’exercice 3

Le système est

$$
\begin{cases}
i=i_1+i_2,\\
i_1=\eta+i_3,\\
E=2R(i+i_2),\\
2i_2=3i_3+i_1.
\end{cases}
$$

En substituant $i_1=\eta+i_3$,

$$
\begin{cases}
i=(\eta+i_3)+i_2,\\
i_1=\eta+i_3,\\
i+i_2=E/(2R),\\
i_2=\frac12(3i_3+i_3+\eta).
\end{cases}
$$

Donc

$$
i_2=\frac\eta2+2i_3,\qquad
i=\frac32\eta+3i_3,\qquad
\frac E{2R}=2\eta+5i_3.
$$

Le manuscrit donne finalement

$$
\begin{aligned}
i&=\frac{3E}{10R}+\frac{3\eta}{10},\\
i_1&=\frac E{10R}+\frac35\eta,\\
i_3&=\frac E{10R}-\frac25\eta,\\
i_2&=\frac{2E}{10R}-\frac{3\eta}{10}.
\end{aligned}
$$

D’où

$$
u=-Ri_1=-\frac E{10}-\frac{3R}{5}\eta
=-\left(\frac3{10}+\frac{3\times5}{5}\times0{,}2\right)
=-(0{,}3+0{,}6)
=\boxed{-0{,}9\ \mathrm V}.
$$

**Remarque :** théorème de superposition : étudier une source à la fois et sommer.

### Exercice 4 — « Condensateur »

> Le titre imprimé est « Condensateur », mais le montage étudié comporte une résistance et une bobine : il s’agit bien d’un circuit **RL**, sans condensateur.

On considère le circuit RL série ci-dessous. La source $e(t)$, à gauche, alimente la résistance $R$ puis la bobine $L$. Le courant $i$ circule dans le sens horaire. Les tensions $u_R$ et $u_L$ sont en convention récepteur. Le graphe d’entrée représente un échelon : $e(t)=0$ avant $t=0$, puis $e(t)=E$ pour $t>0$.

1. Établir l’équation différentielle $(\mathcal E)$ vérifiée par $i$.

Loi des mailles :

$$e(t)=u_R+u_L,\qquad u_R=Ri,\qquad u_L=L\frac{\mathrm di}{\mathrm dt}.$$

Ainsi

$$
e(t)=Ri(t)+L\frac{\mathrm di}{\mathrm dt},
\qquad
\boxed{\frac{e(t)}R=i(t)+\frac LR\frac{\mathrm di}{\mathrm dt}}.
\tag{E}
$$

Le rapport $L/R$ a la dimension d’un temps ; on note $\tau=L/R$.

## Page 5 — Réponse à l’échelon

2. Pour $t>0$, on écrit $i(t)=A+Be^{-t/\tau}$, où $A$, $B$ et $\tau$ sont à déterminer. À quelles conditions, l’une portant sur $\tau$ et l’autre sur $A$, $i$ est-il solution de $(\mathcal E)$ ?

Pour $t>0$, $e(t)=E$, donc

$$i+\tau\frac{\mathrm di}{\mathrm dt}=\frac ER.$$

L’équation homogène donne

$$
i+\tau\frac{\mathrm di}{\mathrm dt}=0
\quad\Longrightarrow\quad
\frac{\mathrm di}{i}=-\frac{\mathrm dt}\tau,
\qquad\ln|i|=-\frac t\tau+k.
$$

La solution complète est $i(t)=Be^{-t/\tau}+A$, avec

$$\boxed{\tau=\frac LR},\qquad\boxed{A=\frac ER}.$$

Vérification par substitution :

$$
\frac{\mathrm di}{\mathrm dt}=-\frac B\tau e^{-t/\tau},
\qquad
A+Be^{-t/\tau}-\tau\frac B\tau e^{-t/\tau}=\frac ER.
$$

3. En tenant compte des conditions initiales, déterminer $i$, puis $u_L=f(t)$.
4. Représenter graphiquement $i=f(t)$, puis $u_L=f(t)$.

Avec $e(0^-)=0$ et $i(0)=0$,

$$0=A+B\quad\Longrightarrow\quad B=-A=-\frac ER.$$

Donc

$$\boxed{i(t)=\frac ER\left(1-e^{-Rt/L}\right)}.$$

Puis

$$
u_L(t)=L\frac{\mathrm di}{\mathrm dt}
=L\frac ER\left[-\left(-\frac RL\right)e^{-Rt/L}\right]
=\boxed{Ee^{-Rt/L}}.
$$

Les graphes montrent $i(t)$ croissant de $0$ vers l’asymptote $E/R$, tandis que $u_L(t)$ décroît de $E$ vers zéro.
