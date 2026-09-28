---
source: PREING2-S2/Ondes/TD1-EX2-Correction_2024-2025_Ondes_P2S2_FPiguet.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Ondes — TD1, exercice 2 : circuit LC

## Page 1 — Circuit et approximation des régimes quasi stationnaires

Le schéma présente une bobine d’inductance $L>0$ et un condensateur de capacité $C>0$ en série dans une boucle fermée. Les armatures du condensateur portent $q_1=q(t)$ et $q_2=-q(t)$. Les flèches $u_L$ et $u_C$ sont orientées vers la gauche sur la branche du haut ; le courant est orienté vers la droite sur la branche du bas.

Avec les conventions du schéma :

$$u_C(t)=V_1-V_2=\frac{q_1(t)}C=\frac{q(t)}C,$$

$$u_L(t)=L\frac{di}{dt}(t)=L\frac{d^2q_1}{dt^2}(t).$$

### ARQS

- $i=i(t)$ est uniforme dans le circuit à chaque instant. Il n’y a pas d’accumulation locale de charge, sauf sur les surfaces du condensateur.
- Le flux du champ magnétique à travers le solénoïde est proportionnel à $i$ à chaque instant ; par Maxwell–Faraday, $u_L$ est proportionnel à $di/dt$.
- La source néglige l’auto-induction de la boucle hors de la bobine et écrit, à l’échelle du circuit, $\operatorname{rot}\vec E=-\partial_t\vec B=\vec0$, puis $\vec E=-\operatorname{grad}V-\partial_t\vec A$, avec le dernier terme indiqué nul.
- Les fils sont des conducteurs parfaits ; le potentiel est uniforme dans chaque fil.

> L’hypothèse sur l’induction des fils est une approximation de circuit. Elle ne supprime pas la tension inductive $L\,di/dt$ de la bobine, déjà prise en compte comme dipôle.

### 1. Analyse dimensionnelle

$$[C]=\frac{[q]}{[u]},\qquad [L]=\mathsf T^2\frac{[u]}{[q]}.$$

Donc

$$[(LC)^{-1/2}]=\mathsf T^{-1}=[\omega].$$

La pulsation est proportionnelle à $1/\sqrt{LC}$, à un facteur sans dimension près.

### 2. Équation différentielle

La circulation sur un chemin fermé donne, avec les conventions choisies,

$$u_L+u_C=0.$$

Ainsi,

$$L\frac{d^2q}{dt^2}+\frac qC=0
\quad\Longleftrightarrow\quad
\frac{d^2q}{dt^2}+\frac1{LC}q=0.\tag{1}$$

En dérivant et avec $i=dq/dt$ :

$$\frac{d^2i}{dt^2}+\frac1{LC}i=0.\tag{2}$$

C’est un oscillateur harmonique simple de pulsation

$$\omega_0=\frac1{\sqrt{LC}}=\frac{2\pi}{T_0}=2\pi f_0.$$

### Analogie mécanique–électrique

| Oscillateur mécanique | Oscillateur électrique |
| --- | --- |
| Position, écart à l’équilibre, ou vitesse | Charge, écart à l’équilibre, ou courant |
| Raideur $k$ | Inverse de la capacité $1/C$ |
| Masse $m$ | Inductance $L$ |
| $\omega_0=\sqrt{k/m}$ | $\omega_0=\sqrt{1/(LC)}$ |

## Page 2 — Énergies et solution

### 3. Énergie du condensateur

$$dE_C=u_C\,dq=\frac qC\,dq
=d\left(\frac{q^2}{2C}+\text{constante}\right),$$

d’où

$$E_C=\frac{q^2}{2C}+\text{constante}.$$

C’est l’analogue de l’énergie potentielle élastique.

### Énergie de la bobine

$$\begin{aligned}
dE_L&=u_L\,dq=L\,i\,dt\,\frac{di}{dt}
=Li\,di\\
&=d\left(\frac L2i^2+\text{constante}\right)
=d\left[\frac L2\left(\frac{dq}{dt}\right)^2+\text{constante}\right].
\end{aligned}$$

Donc

$$E_L=\frac L2\left(\frac{dq}{dt}\right)^2+\text{constante},$$

analogue de l’énergie cinétique.

### Conservation de l’énergie

En l’absence de dissipation,

$$E_{\mathrm{tot}}=E_C+E_L=\text{constante},$$

$$dE_{\mathrm{tot}}=dE_C+dE_L=dq\,(u_C+u_L)=0.$$

On retrouve les équations (1) et (2) et la pulsation $\omega_0$ : l’énergie passe du condensateur à la bobine et réciproquement.

### Solution analogue à celle de l’oscillateur mécanique

$$q(t)=q_c\cos\bigl(\omega_0(t-t_0)\bigr)+q_s\sin\bigl(\omega_0(t-t_0)\bigr),$$

$$i(t)=\frac{dq}{dt}
=\omega_0\left[-q_c\sin\bigl(\omega_0(t-t_0)\bigr)+q_s\cos\bigl(\omega_0(t-t_0)\bigr)\right].$$

Avec $q(t_0)=q_0=q_c$ et $q'(t_0)=0=\omega_0q_s$,

$$q(t)=q_0\cos\bigl(\omega_0(t-t_0)\bigr).$$

Alors

$$E_L(t)=\frac12L\omega_0^2q_0^2\sin^2\bigl(\omega_0(t-t_0)\bigr)+\text{constante},$$

$$E_C(t)=\frac1{2C}q_0^2\cos^2\bigl(\omega_0(t-t_0)\bigr)+\text{constante},$$

avec $L\omega_0^2=1/C$.

La moyenne sur une demi-période, donc a fortiori sur une période, donne, en prenant les constantes d’énergie nulles,

$$\langle E_L\rangle=\langle E_C\rangle
=\frac{q_0^2}{4C}=\frac14L\omega_0^2q_0^2=\frac{E_{\mathrm{tot}}}{2}.$$

Il y a équipartition de l’énergie en moyenne entre $E_L$ et $E_C$, comme pour l’oscillateur mécanique.
