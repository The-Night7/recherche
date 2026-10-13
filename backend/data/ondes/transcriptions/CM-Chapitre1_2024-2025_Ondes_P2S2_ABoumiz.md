---
source: "PREING2-S2/Ondes/CM-Chapitre1_2024-2025_Ondes_P2S2_ABoumiz.pdf"
pages: 13
transcription: manuelle
transcription_date: 2026-10-04
verification: lecture visuelle de toutes les pages ; formules et schémas vérifiés ; erreurs originales annotées
---

# Chapitre 1 — Oscillateurs harmoniques

## Oscillateur harmonique non amorti (pages 1 à 3)

On appelle oscillateur harmonique non amorti tout système physique décrit par une fonction $\psi(t)$ qui vérifie l’équation différentielle :

$$
\frac{d^2\psi(t)}{dt^2}+\omega_0^2\psi(t)=\omega_0^2\psi_0.
$$

$\psi(t)$ est une fonction caractéristique du système physique étudié : charge électrique, tension électrique, intensité de courant électrique ou élongation d’un système masse-ressort. $\omega_0$ est la pulsation propre de l’oscillateur harmonique.

Dans le cas d’une corde vibrante ou d’un système masse-ressort, la source appelle $\psi(t)$ « l’amplitude des vibrations » et $\psi_m$ sa valeur maximale. $\phi$ est la phase à l’origine des temps ; $\omega_0=2\pi f_0$, où $f_0$ est la fréquence propre de l’oscillateur.

La solution de l’équation différentielle précédente est de la forme :

$$
\psi(t)=\psi_0+\psi_m\cos(\omega_0t+\phi).
$$

$\psi_m$ et $\phi$ sont des constantes déterminées par les conditions initiales. $\psi(t)=\psi_0$ correspond à une position d’équilibre de l’oscillateur harmonique.

> Précision de transcription : $\psi(t)$ est ici la grandeur instantanée ; $\psi_m$ est l’amplitude de son écart à l’équilibre. Si $\psi_0\ne0$, la valeur maximale de $\psi(t)$ est $\psi_0+|\psi_m|$.

## Section I.1 — Un exemple simple (pages 4 et 5)

Soit un bloc de masse $M$ posé sur un plan horizontal, libre de se déplacer sans frottement, attaché à un ressort idéal sans masse, lui-même accroché à un mur. C’est un exemple de système à un seul degré de liberté.

**Schéma de la page 4 :** mur vertical à gauche, ressort horizontal, bloc à droite posé sur le plan.

Un ressort idéal obéit à la loi de Hooke. Son énergie potentielle est :

$$
E_P=\frac12k(L-L_0)^2=\frac12kx^2,\qquad x=L-L_0.
$$

$k$ est la constante de rappel ou de raideur du ressort ; $L_0$ est sa longueur à vide.

## Force de rappel et équation du mouvement (page 6)

$$
\vec F=-\frac{\partial E_P}{\partial x}\vec u_x,
\qquad E_P=\frac12kx^2,
$$

d’où :

$$
\vec F=\frac{\partial}{\partial x}\left(-\frac12kx^2\right)\vec u_x
=-kx\vec u_x.
$$

La deuxième loi de Newton s’écrit $\vec F=m\vec a$, soit $-kx\vec u_x=m\ddot x\vec u_x$. On obtient :

$$
\ddot x+\omega^2x(t)=0,
\qquad
\frac{d^2x(t)}{dt^2}+\omega^2x(t)=0,
\qquad
\left(\frac{d^2}{dt^2}+\omega^2\right)x(t)=0.
$$

La solution est $x(t)=A\cos(\omega t)+B\sin(\omega t)$, où $A$ et $B$ se déterminent à partir des conditions initiales :

$$
\begin{cases}
x(0)=A\cos(0)+B\sin(0),\\
\dot x(0)=-A\omega\sin(0)+B\omega\cos(0),
\end{cases}
\qquad
\begin{cases}A=x(0),\\ B=\dot x(0)/\omega.\end{cases}
$$

> La source passe de $M$ à $m$ pour la même masse. L’identification donne $\omega^2=k/m$.

## Exemple, période et fréquence (page 7)

Prenons $x(0)=1\,\mathrm m$ et $\dot x(0)=0\,\mathrm{m/s}$ :

$$
\begin{cases}
x(t)=A\cos(\omega t),\quad A=1\,\mathrm m,\\
\dot x(t)=-A\omega\sin(\omega t).
\end{cases}
$$

Comme $\cos(x)=\cos(x+2\pi)$ et $\sin(x)=\sin(x+2\pi)$ :

$$
x\left(t+\frac{2\pi}{\omega}\right)=x(t),
\qquad
\dot x\left(t+\frac{2\pi}{\omega}\right)=\dot x(t).
$$

Après un temps $T=2\pi/\omega$, le système revient à sa position initiale. $T$ est la période des oscillations et $\nu=1/T$ leur fréquence.

## Sens du terme « harmonique simple » (page 8)

**Harmonique :** les solutions sont des sommes de fonctions trigonométriques. **Simple :** tous les termes de la solution ont la même fréquence.

L’équation différentielle du mouvement de la masse $M$ décrit un grand nombre de systèmes physiques. Qu’ont-ils en commun ? Pourquoi les systèmes harmoniques sont-ils très répandus ?

## Propriétés (page 9)

a) Conservation de l’énergie :

$$
\frac{\partial E}{\partial t}=0,
\qquad E=\frac12M\dot x^2+\frac12kx^2.
$$

b) Les équations du mouvement sont linéaires :

$$
\ddot x_1+\omega^2x_1=0,\quad\ddot x_2+\omega^2x_2=0
\quad\Longrightarrow\quad
\frac{d^2}{dt^2}(x_1+x_2)+\omega^2(x_1+x_2)=0.
$$

Le cours indique que, si un système satisfait a) et b), on pourra le réduire à un ensemble d’oscillateurs harmoniques simples et à l’oscillateur hyperbolique $\ddot x-\omega^2x(t)=0$.

> La conservation de l’énergie le long du mouvement se note plus précisément $dE/dt=0$. L’affirmation de réduction suppose le cadre des systèmes mécaniques linéaires conservatifs étudiés ensuite ; elle ne constitue pas un théorème pour toute équation linéaire.

## Section I.2 — Linéarité et superposition (pages 10 et 11)

Une équation est dite linéaire dans la présentation du cours si, pour toutes solutions $f$ et $g$, $\alpha f+\beta g$ est aussi solution, pour toutes constantes $\alpha$ et $\beta$.

Une équation différentielle ordinaire est présentée sous la forme :

$$
S(t)+\alpha_0f(t)+\alpha_1\dot f(t)+\alpha_2\ddot f(t)+\cdots=0.\tag{**}
$$

Elle est homogène si $S(t)=0$, sinon inhomogène. Dans le cas homogène, ses solutions forment un espace vectoriel. On cherche une base $\{f_i\}_{i=1,2,\ldots}$ telle que toute solution s’écrive :

$$
\sum_{i=1}^n\gamma_i f_i,
\qquad \frac{\partial\gamma_i}{\partial t}=0.
$$

On propose $f(t)=e^{kt}$. Rappel de la source : $e^k=\sum_{n=0}^{\infty}k^n/n!$, et $S(t)=0$.

> Le principe de superposition énoncé ici s’applique à l’équation **homogène**. La méthode exponentielle suivante suppose les coefficients $\alpha_i$ constants.

## Équation caractéristique (page 12)

$$
\alpha_0e^{kt}+\alpha_1ke^{kt}+\alpha_2k^2e^{kt}+\alpha_3k^3e^{kt}+\cdots=0,
$$

d’où le polynôme de degré $n$ en $k$ :

$$
\alpha_0+\alpha_1k+\alpha_2k^2+\alpha_3k^3+\cdots=0.
$$

Pour l’oscillateur harmonique simple, $\alpha_0=\omega^2$, $\alpha_1=0$, $\alpha_2=1$ (degré 2) :

$$
\ddot f+\omega^2f=0
\quad\Longrightarrow\quad r^2+\omega^2=0
\quad\Longrightarrow\quad r=\pm i\omega.
$$

Les solutions sont de la forme $f(t)=Ae^{i\omega t}+Be^{-i\omega t}$.

## Rappel — Nombres complexes (page 13)

$$
Z=a+ib,\qquad\overline Z=a-ib,
\qquad e^{i\theta}=\cos\theta+i\sin\theta.
$$

La formule d’Euler se retrouve par le développement :

$$
\begin{aligned}
e^{i\theta}
&=1+i\theta+\frac{i^2\theta^2}{2!}+\frac{i^3\theta^3}{3!}+\cdots\\
&=\left(1-\frac{\theta^2}{2!}+\frac{\theta^4}{4!}-\frac{\theta^6}{6!}+\cdots\right)
+i\left(\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\cdots\right)\\
&=\cos\theta+i\sin\theta.
\end{aligned}
$$

$$
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}2,
\qquad\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.
$$

> Coquille de la source : le terme $\theta^5/5!$ apparaît sans son signe $+$ dans la parenthèse imaginaire ; le signe est rétabli ci-dessus.
