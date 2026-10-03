---
source: "PREING2-S2/Ondes/CM-Chapitre1_2024-2025_Ondes_P2S2_ABoumiz.pdf"
pages: 13
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale et comparaison avec le texte natif ; formules, schémas et erreurs de la source vérifiés
---

# Ondes — Chapitre 1 : oscillateurs harmoniques — 2024–2025

## Définition de l’oscillateur harmonique non amorti (pages 1 à 3)

On appelle oscillateur harmonique non amorti tout système physique décrit par une fonction $\psi(t)$ vérifiant

$$\frac{d^2\psi(t)}{dt^2}+\omega_0^2\psi(t)=\omega_0^2\psi_0.$$

La fonction $\psi(t)$ caractérise le système étudié : charge électrique, tension, intensité du courant ou élongation d’un système masse-ressort. $\omega_0$ est la pulsation propre de l’oscillateur.

Dans le cas d’une corde vibrante ou d’un système masse-ressort, la source appelle $\psi(t)$ « l’amplitude des vibrations » et $\psi_m$ sa valeur maximale. $\phi$ est la phase à l’origine des temps. La fréquence propre $f_0$ vérifie $\omega_0=2\pi f_0$.

La solution est de la forme

$$\psi(t)=\psi_0+\psi_m\cos(\omega_0t+\phi),$$

avec $\psi_m$ et $\phi$ constants, déterminés à partir des conditions initiales. La solution constante $\psi(t)=\psi_0$ correspond à une position d’équilibre.

> Précision de vocabulaire : $\psi(t)$ est ici l’élongation instantanée ; $\psi_m$ est l’amplitude de l’écart à l’équilibre. Si $\psi_0\ne0$ et $\psi_m\ge0$, la valeur maximale de $\psi$ vaut $\psi_0+\psi_m$.

## Section I.1 — Un exemple simple : le système masse-ressort (pages 4 à 8)

Un bloc de masse $M$ posé sur un plan horizontal se déplace sans frottement. Il est attaché à un ressort idéal sans masse accroché à un mur. Le dessin représente le mur à gauche, le ressort horizontal et le bloc à droite. C’est un système à un seul degré de liberté.

### Loi de Hooke et énergie potentielle (page 5)

Un ressort idéal obéit à la loi de Hooke. Son énergie potentielle est

$$E_P=\frac12k(L-L_0)^2=\frac12kx^2,\qquad x=L-L_0,$$

avec $k$ la constante de rappel, ou raideur, et $L_0$ la longueur à vide.

### Force et équation du mouvement (page 6)

$$\vec F=-\frac{\partial E_P}{\partial x}\vec u_x
=\frac\partial{\partial x}\left(-\frac12kx^2\right)\vec u_x
=-kx\vec u_x.$$

La deuxième loi de Newton donne $\vec F=m\vec a$, soit

$$-kx\vec u_x=m\ddot x\vec u_x,$$

puis

$$\ddot x+\omega^2x(t)=0,\qquad
\frac{d^2x(t)}{dt^2}+\omega^2x(t)=0,
\qquad\left(\frac{d^2}{dt^2}+\omega^2\right)x(t)=0.$$

> La source alterne $M$ et $m$ pour la masse. Par identification, $\omega^2=k/m$.

La solution générale est

$$x(t)=A\cos(\omega t)+B\sin(\omega t),$$

avec $A,B$ déterminés par les conditions initiales :

$$\begin{cases}
x(0)=A\cos0+B\sin0,\\
\dot x(0)=-A\omega\sin0+B\omega\cos0,
\end{cases}
\qquad
\begin{cases}A=x(0),\\B=\dot x(0)/\omega.\end{cases}$$

### Exemple et périodicité (page 7)

Pour $x(0)=1\ \mathrm m$ et $\dot x(0)=0\ \mathrm{m/s}$,

$$x(t)=A\cos(\omega t),\qquad \dot x(t)=-A\omega\sin(\omega t),\qquad A=1\ \mathrm m.$$

Les identités $\cos x=\cos(x+2\pi)$ et $\sin x=\sin(x+2\pi)$ entraînent

$$x\left(t+\frac{2\pi}{\omega}\right)=x(t),\qquad
\dot x\left(t+\frac{2\pi}{\omega}\right)=\dot x(t).$$

Après un temps $T=2\pi/\omega$, le système revient à sa position initiale. $T$ est la période des oscillations et $\nu=1/T$ leur fréquence.

### Pourquoi « harmonique simple » ? (page 8)

- **Harmonique :** les solutions sont des sommes de fonctions trigonométriques.
- **Simple :** tous les termes de la solution ont la même fréquence.

L’équation différentielle du mouvement de la masse $M$ décrit de nombreux systèmes physiques. Qu’ont-ils en commun ? Pourquoi les systèmes harmoniques sont-ils très répandus ?

## Propriétés (page 9)

**a) Conservation de l’énergie :**

$$\frac{\partial E}{\partial t}=0,\qquad
E=\frac12M\dot x^2+\frac12kx^2.$$

> Le symbole de dérivée partielle est celui de la diapositive. La conservation le long du mouvement s’écrit rigoureusement $dE/dt=0$.

**b) Linéarité des équations du mouvement :** si

$$\ddot x_1+\omega^2x_1=0,\qquad\ddot x_2+\omega^2x_2=0,$$

alors

$$\frac{d^2}{dt^2}(x_1+x_2)+\omega^2(x_1+x_2)=0.$$

Le cours indique que, pour un système satisfaisant a) et b), on peut se ramener à un ensemble d’oscillateurs harmoniques simples et à l’oscillateur hyperbolique

$$\ddot x-\omega^2x(t)=0.$$

## Section I.2 — Linéarité et superposition (pages 10 à 12)

Le cours énonce : une équation est linéaire si, pour toutes solutions $f,g$, la combinaison $\alpha f+\beta g$ est aussi solution, quelles que soient les constantes $\alpha,\beta$.

> Ce principe de superposition des solutions s’applique à une équation linéaire **homogène**. Pour une équation linéaire inhomogène, une combinaison quelconque de solutions n’a généralement pas le même second membre.

L’équation différentielle ordinaire considérée est

$$S(t)+\alpha_0f(t)+\alpha_1\dot f(t)+\alpha_2\ddot f(t)+\cdots=0.\tag{**}$$

Elle est homogène si $S(t)=0$, inhomogène sinon. Dans le cas homogène, les solutions forment un espace vectoriel. On cherche une base $(f_i)$ permettant d’écrire toute solution sous la forme

$$\sum_{i=1}^n\gamma_i f_i,\qquad \frac{\partial\gamma_i}{\partial t}=0.$$

On propose $f(t)=e^{kt}$. La diapositive rappelle $e^k=\sum_{n=0}^{\infty}k^n/n!$ et $S(t)=0$. L’équation devient

$$\alpha_0e^{kt}+\alpha_1ke^{kt}+\alpha_2k^2e^{kt}+\alpha_3k^3e^{kt}+\cdots=0,$$

d’où le polynôme d’ordre $n$ en $k$ :

$$\alpha_0+\alpha_1k+\alpha_2k^2+\alpha_3k^3+\cdots=0.$$

Pour l’oscillateur harmonique simple, $\alpha_0=\omega^2$, $\alpha_1=0$ et $\alpha_2=1$ (degré 2). Ainsi,

$$\ddot f+\omega^2f=0\quad\Longrightarrow\quad r^2+\omega^2=0
\quad\Longrightarrow\quad r=\pm i\omega,$$

et

$$f(t)=Ae^{i\omega t}+Be^{-i\omega t}.$$

> Le paramètre exponentiel, d’abord appelé $k$, est appelé $r$ dans cet exemple. La méthode par polynôme caractéristique suppose les coefficients constants ; les racines multiples nécessitent des facteurs polynomiaux en $t$, non développés dans ces diapositives.

## Rappel — Nombres complexes (page 13)

$$Z=a+ib,\qquad\overline Z=a-ib.$$

La formule d’Euler est $e^{i\theta}=\cos\theta+i\sin\theta$. Le développement donné commence par

$$e^{i\theta}=1+i\theta+\frac{i^2\theta^2}{2!}+\frac{i^3\theta^3}{3!}+\cdots.$$

En séparant parties réelle et imaginaire, on obtient

$$e^{i\theta}=\left(1-\frac{\theta^2}{2!}+\frac{\theta^4}{4!}-\frac{\theta^6}{6!}+\cdots\right)
+i\left(\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\cdots\right)
=\cos\theta+i\sin\theta.$$

> **Signe rectifié :** la ligne développée de la source imprime un signe moins devant le terme en $\theta^4/4!$. Le signe correct est plus, puisque $i^4=1$.

Finalement,

$$\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}2,
\qquad\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.$$
