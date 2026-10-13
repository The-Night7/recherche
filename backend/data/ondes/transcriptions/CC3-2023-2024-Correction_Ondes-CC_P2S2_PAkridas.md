---
source: "PREING2-S2/Ondes-CC/CC3-2023-2024-Correction_Ondes-CC_P2S2_PAkridas.pdf"
pages: 3
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale du manuscrit ; contrôle des dimensions, des modes propres et des relations de dispersion
---

# Ondes — CC3 2023–2024 — Corrigé

> Le PDF contient le corrigé seul. Les numéros de réponse sont conservés. Les abréviations d’analyse vectorielle sont développées sans modifier les équations.

## Exercice 1 — Onde électromagnétique (page 1)

**1. Maxwell–Thomson.**

$$
\operatorname{div}\vec B=0.
$$

**2. Dimensions.** La force de Lorentz est

$$
\vec F=q(\vec E+\vec v\wedge\vec B).
$$

D’où

$$
[\vec E]=\frac{MLT^{-2}}{IT}=MLI^{-1}T^{-3},
\qquad
[\vec B]=\frac{MLT^{-2}}{IT\cdot LT^{-1}}=MI^{-1}T^{-2}.
$$

Avec Maxwell–Gauss, $\operatorname{div}\vec E=\rho/\varepsilon_0$ :

$$
[\varepsilon_0]
=\frac{ITL^{-3}}{MLI^{-1}T^{-3}L^{-1}}
=T^4I^2M^{-1}L^{-3}.
$$

Unité SI : $\mathrm{s^4\,A^2\,kg^{-1}\,m^{-3}}$.

La relation de Maxwell–Ampère utilisée ici pour l’analyse dimensionnelle est $\operatorname{rot}\vec B=\mu_0\vec j+\cdots$. Alors

$$
[\mu_0]=\frac{MI^{-1}T^{-2}L^{-1}}{IL^{-2}}
=MLI^{-2}T^{-2},
$$

soit $\mathrm{kg\,m\,A^{-2}\,s^{-2}}$.

### 3. Équations de propagation

**3.a)** En prenant le rotationnel de Maxwell–Faraday,

$$
\operatorname{rot}(\operatorname{rot}\vec E)
=-\operatorname{rot}(\partial_t\vec B)
=-\partial_t(\operatorname{rot}\vec B).
$$

L’identité vectorielle donne

$$
\operatorname{rot}(\operatorname{rot}\vec E)
=\operatorname{grad}(\operatorname{div}\vec E)-\Delta\vec E.
$$

Dans le vide, $\rho=0$ donc $\operatorname{div}\vec E=0$. Avec $\vec j=\vec0$, Maxwell–Ampère donne pour l’autre membre $-\mu_0\varepsilon_0\partial_t^2\vec E$. Finalement,

$$
(\mu_0\varepsilon_0\partial_t^2-\Delta)\vec E=\vec0.
$$

**3.b)** De même,

$$
\begin{aligned}
\operatorname{rot}(\operatorname{rot}\vec B)
&=\mu_0\varepsilon_0\operatorname{rot}(\partial_t\vec E)\\
&=\mu_0\varepsilon_0\partial_t(\operatorname{rot}\vec E)
=-\mu_0\varepsilon_0\partial_t^2\vec B.
\end{aligned}
$$

Comme $\operatorname{div}\vec B=0$,

$$
(\mu_0\varepsilon_0\partial_t^2-\Delta)\vec B=\vec0.
$$

**3.c)** Les dimensions de ces équations donnent

$$
[\mu_0\varepsilon_0]^{-1}
=\frac{[\partial_t^2]}{[\Delta]}
=(LT^{-1})^2=[c]^2,
$$

avec $c$ la vitesse de phase de l’onde électromagnétique. Numériquement, avec les approximations du manuscrit,

$$
c=(\mu_0\varepsilon_0)^{-1/2}
\simeq(10^{-6}\times9\times10^{-12})^{-1/2}\ \mathrm{m\,s^{-1}}
=\frac13\times10^9\ \mathrm{m\,s^{-1}}
\simeq3\times10^8\ \mathrm{m\,s^{-1}}.
$$

### 4. Onde plane

$$
\vec E(x,t)=\vec u_y E_0\cos(\omega t-kx),
\qquad\vec B(x,t)=\vec u_z B_0\cos(\omega t-kx).
$$

**4.a)** À phase constante, $d\varphi=0=\omega\,dt-k\,dx$, donc

$$
v_\varphi=\frac{dx}{dt}=\frac\omega k>0.
$$

La propagation se fait dans la direction $x$, vers les $x$ croissants.

**4.b)** Polarisation : $\vec E$ selon $y$ et $\vec B$ selon $z$.

## Exercice 2 — Onde mécanique (pages 2 et 3)

L’équation de départ est

$$
\left(\frac1{c^2}\partial_t^2-\partial_x^2\right)\Psi(x,t)=0,
\qquad\forall x,t.\tag{1}
$$

### 1. Ondes propres et dispersion

**1.a)** L’équation est linéaire ; on peut la résoudre dans $\mathbb C$ puis prendre la partie réelle. On cherche

$$
\widetilde\Psi(x,t)=\widetilde\Psi_0e^{i(\omega t-kx)}.
$$

Alors $\partial_t^2\widetilde\Psi=-\omega^2\widetilde\Psi$ et $\partial_x^2\widetilde\Psi=-k^2\widetilde\Psi$. L’équation devient

$$
\left(-\frac{\omega^2}{c^2}+k^2\right)\widetilde\Psi=0.
$$

La solution nulle, sans onde, est écartée. Il reste $\omega^2=(ck)^2$, soit

$$
\omega_\pm=\pm\omega=\pm ck,\qquad\omega,k\in\mathbb R_{+}^{*}.\tag{2}
$$

**1.b)**

$$
v_{\varphi,\pm}=\frac{\omega_\pm}{k}
=\frac{d\omega_\pm}{dk}=v_{g,\pm}=\pm c.
$$

Le milieu est non dispersif.

**1.c)** La combinaison linéaire des ondes propres s’écrit

$$
\begin{aligned}
\widetilde\Psi(x,t)=
&\widetilde A_{++}e^{i(\omega t+kx)}
+\widetilde A_{+-}e^{i(\omega t-kx)}\\
&+\widetilde A_{-+}e^{-i(\omega t+kx)}
+\widetilde A_{--}e^{-i(\omega t-kx)},
\end{aligned}
$$

avec les quatre coefficients dans $\mathbb C$.

### 2. Conditions aux bords

**2.a)** En zéro,

$$
0=\widetilde\Psi(0,t)
=(\widetilde A_{++}+\widetilde A_{+-})e^{i\omega t}
+(\widetilde A_{-+}+\widetilde A_{--})e^{-i\omega t}.
$$

Après multiplication par $e^{i\omega t}$,

$$
(\widetilde A_{++}+\widetilde A_{+-})e^{2i\omega t}
+(\widetilde A_{-+}+\widetilde A_{--})=0.
$$

Si $\omega=0$, il n’y a pas d’oscillation temporelle ; ce cas est écarté. Sinon le terme dépendant du temps et le terme constant doivent s’annuler séparément :

$$
\widetilde A_{++}+\widetilde A_{+-}=0,
\qquad\widetilde A_{-+}+\widetilde A_{--}=0.
$$

D’où

$$
\begin{aligned}
\widetilde\Psi(x,t)
&=(\widetilde A_{++}e^{i\omega t}+\widetilde A_{--}e^{-i\omega t})
(e^{ikx}-e^{-ikx})\\
&=(\widetilde B_+e^{i\omega t}+\widetilde B_-e^{-i\omega t})\sin(kx),
\end{aligned}
$$

avec $\widetilde B_+=2i\widetilde A_{++}$ et $\widetilde B_-=2i\widetilde A_{--}$. La partie réelle est

$$
\Psi(x,t)=[\alpha\cos(\omega t)+\beta\sin(\omega t)]\sin(kx),\tag{3}
$$

avec

$$
\alpha=\operatorname{Re}(\widetilde B_++\widetilde B_-),
\qquad\beta=\operatorname{Im}(-\widetilde B_++\widetilde B_-).
$$

Le découplage entre le facteur temporel et le facteur spatial caractérise une onde stationnaire.

Le manuscrit précise que la condition physique est $\Psi(0,t)=0$, pas nécessairement $\widetilde\Psi(0,t)=0$, mais que cela ne change pas le résultat ici.

**2.b)** Au second bord,

$$
0=\Psi(L,t)=[\alpha\cos(\omega t)+\beta\sin(\omega t)]\sin(kL).
$$

Le cas $\alpha=\beta=0$, sans onde, est écarté. Il faut donc

$$
\sin(kL)=0,\qquad k_m=\frac{m\pi}{L},\quad m\in\mathbb N^*.\tag{4}
$$

Les nombres d’onde sont quantifiés.

**2.c)** En combinant (4) et (2), les pulsations sont quantifiées :

$$
\omega_m=ck_m=\frac{cm\pi}{L}.
$$

> Le dernier quotient du manuscrit omet le facteur $c$. Celui-ci est rétabli conformément à l’égalité $\omega_m=ck_m$ qui précède et aux dimensions physiques.

Le cas $m=0$ donnerait $k_0=\omega_0=0$, donc aucune onde ; il est écarté.

**2.d)** La combinaison des modes propres est

$$
\Psi(x,t)=\sum_{m=1}^{+\infty}
[\alpha_m\cos(\omega_mt)+\beta_m\sin(\omega_mt)]\sin(k_mx).
$$

### 3. Équation avec un terme spatial d’ordre quatre

On considère maintenant

$$
\left(\frac1{c^2}\partial_t^2-\partial_x^2-\gamma\partial_x^4\right)
\Psi(x,t)=0,\qquad\gamma>0.\tag{5}
$$

**3.a)** Avec le même essai que précédemment, $\partial_x^4\widetilde\Psi=k^4\widetilde\Psi$. Alors

$$
\left(-\frac{\omega^2}{c^2}+k^2-\gamma k^4\right)\widetilde\Psi=0,
\qquad\omega^2=(ck)^2(1-\gamma k^2).
$$

La relation de dispersion est

$$
\omega_\pm=\pm ck\sqrt{1-\gamma k^2}.\tag{6}
$$

**3.b)**

$$
v_{\varphi,\pm}=\frac{\omega_\pm}{k}
=\pm c\sqrt{1-\gamma k^2},
$$

$$
v_{g,\pm}=\frac{d\omega_\pm}{dk}
=v_{\varphi,\pm}\mp\frac{\gamma ck^2}{\sqrt{1-\gamma k^2}}
=v_{\varphi,\pm}-\frac{\gamma(ck)^2}{v_{\varphi,\pm}}.
$$

Les vitesses de phase et de groupe diffèrent : le milieu est dispersif. Ces formules de vitesse s’entendent lorsque $1-\gamma k^2>0$.

**3.c)** Pour une pulsation réelle, il faut $\omega^2\ge0$ ; sinon une exponentielle réelle apparaît dans $\Psi$.

**3.d)** Comme $(ck)^2>0$,

$$
1-\gamma k^2\ge0,
\qquad k=\frac{2\pi}{\lambda}\le\gamma^{-1/2},
\qquad\lambda\ge2\pi\sqrt\gamma=\lambda_c.
$$

Puisque les conditions aux bords imposent également $k=k_m=m\pi/L$, avec $m\in\mathbb N^*$, les nombres d’onde et les pulsations des modes non atténués sont bornés.
