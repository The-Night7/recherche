---
source: "PREING2-S2/Ondes-CC/CC1-2023-2024-Correction_Ondes-CC_P2S2_FPiguet.pdf"
pages: 3
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale du corrigé manuscrit ; équations, schémas et conditions initiales vérifiés
---

# Ondes — CC1 2023–2024 — Corrigé

> Le fichier contient le corrigé seul. Les numéros des réponses sont conservés ; les questions absentes ne sont pas reconstituées. Les dessins sont décrits avec leurs axes et leurs grandeurs.

## Exercice 1 — Oscillateur harmonique (page 1)

**1 et 2.** Pour un oscillateur harmonique, l’énergie mécanique $E_m$ est constante et l’énergie potentielle $E_p$ est proportionnelle à $X^2$.

**3.** Le schéma représente une masse $M$ attachée à un ressort horizontal fixé en $H$. L’axe $x$ est dirigé vers la droite ; $x_0=x_{\mathrm{eq}}$ indique ici la position d’équilibre et $x(t)$ la position instantanée de la masse.

Dans un référentiel galiléen, le principe fondamental de la dynamique appliqué à $M$, projeté sur l’axe $x$, donne

$$
m\ddot x=-k(x-x_0)=-k(x-x_{\mathrm{eq}}).
$$

En posant $X=x-x_{\mathrm{eq}}$, on obtient

$$
\ddot X+\frac kmX=0.
$$

Avec $X=A\cos(\omega_0t)$, on a $\ddot X=-\omega_0^2X$ et

$$
\left(-\omega_0^2+\frac km\right)X=0\qquad\forall t.
$$

Soit $X(t)=0$ pour tout $t$, cas sans oscillation écarté dans le corrigé, soit

$$
\omega_0=\sqrt{\frac km}.
$$

Comme $[\omega_0t]=1$, $[\omega_0]=T^{-1}$.

**4.** L’ajout d’une force de frottement fluide amortit le mouvement et dissipe de l’énergie vers le milieu extérieur :

$$
X(t)\xrightarrow[t\to+\infty]{}X_{\mathrm{eq}}=0.
$$

**5.** On ajoute une force extérieure périodique de pulsation $\omega_{\mathrm{ext}}$, dans la direction du mouvement. La résonance d’amplitude correspond à l’obtention d’une amplitude maximale de $X$ pour une certaine valeur de $\omega_{\mathrm{ext}}$.

## Exercice 2 — Oscillateur vertical dans un fluide (pages 2 et 3)

Le dessin montre une masse $M$ suspendue à un ressort fixé en $H$, immergée dans un liquide. L’axe $z$ et le vecteur $\vec g$ sont dirigés vers le bas.

### 1. Forces sur $M$

En notant $g=\|\vec g\|$,

$$
\begin{aligned}
\text{Pesanteur : }&\vec P=m\vec g=mg\vec u_z,\\
\text{Poussée d’Archimède : }&\vec\Pi=-\rho V\vec g=-\rho Vg\vec u_z,\\
\text{Rappel élastique : }&\vec F=-k(\ell-\ell_0)\vec u_{HM}=-k(z-z_0)\vec u_z,\\
\text{Frottement fluide : }&\vec f=-\mu\vec v=-\mu\dot z\vec u_z.
\end{aligned}
$$

### 2. Équation du mouvement

Le référentiel terrestre est supposé galiléen. La projection du principe fondamental sur $\vec u_z$ donne

$$
m\ddot z=-\mu\dot z-k(z-z_0)+(m-\rho V)g,
$$

soit

$$
\ddot z+\frac\mu m\dot z+\frac km(z-z_0)
-\left(1-\frac{\rho V}{m}\right)g=0.\tag{1}
$$

Le corrigé pose

$$
\Gamma=\frac\mu m,\qquad\omega_0^2=\frac km,
\qquad m'=1-\frac{\rho V}{m}.
$$

Il précise que $[m']=1$ : malgré la lettre employée, $m'$ n’a pas la dimension d’une masse.

### 3. Équilibre et absence d’amortissement

À l’équilibre, la position est constante. L’équation (1) donne

$$
\omega_0^2(z_{\mathrm{eq}}-z_0)=m'g.\tag{1-éq}
$$

Le manuscrit indique également : oscillateur non amorti si $\Gamma=0$.

### 4. Écart à l’équilibre

En injectant (1-éq) dans (1), avec $Z=z-z_{\mathrm{eq}}$,

$$
\ddot Z+\Gamma\dot Z+\omega_0^2Z=0.\tag{2}
$$

### 5. Résolution

**5.a)** On cherche une solution complexe $\widetilde Z(t)=Ae^{rt}$, avec $A,r\in\mathbb C$. Alors

$$
\dot{\widetilde Z}=r\widetilde Z,
\qquad\ddot{\widetilde Z}=r^2\widetilde Z.
$$

L’équation (2) impose $(r^2+\Gamma r+\omega_0^2)\widetilde Z=0$. En écartant la solution identiquement nulle, on obtient

$$
r^2+\Gamma r+\omega_0^2=0.\tag{3}
$$

Les racines sont

$$
r_\pm=-\frac\Gamma2\pm\sqrt\Delta,
\qquad\Delta=\left(\frac\Gamma2\right)^2-\omega_0^2.
$$

Il existe trois régimes, selon que $\Delta$ est positif, nul ou négatif.

**6. Régime pseudo-périodique.** $\Delta<0$, soit $0<\Gamma/2<\omega_0$ dans le cas amorti.

**6.a)**

$$
r_\pm=-\frac\Gamma2\pm i\sqrt{-\Delta}
=-\frac\Gamma2\pm i\omega,
\qquad\omega=\sqrt{\omega_0^2-\left(\frac\Gamma2\right)^2}<\omega_0.
$$

On écrit

$$
\widetilde Z(t)=e^{-\Gamma t/2}
\left(A_+e^{i\omega t}+A_-e^{-i\omega t}\right),
\quad A_\pm=a_\pm+ib_\pm,\quad a_\pm,b_\pm\in\mathbb R.
$$

En développant les exponentielles,

$$
\begin{aligned}
\widetilde Z(t)=e^{-\Gamma t/2}\bigl\{
&(a_++ib_+)[\cos(\omega t)+i\sin(\omega t)]\\
+&(a_-+ib_-)[\cos(\omega t)-i\sin(\omega t)]\bigr\}.
\end{aligned}
$$

Sa partie réelle contient $(a_++a_-)\cos(\omega t)+(-b_++b_-)\sin(\omega t)$. En posant $A_c=a_++a_-$ et $A_s=-b_++b_-$,

$$
Z(t)=\operatorname{Re}\widetilde Z(t)
=e^{-\Gamma t/2}[A_c\cos(\omega t)+A_s\sin(\omega t)].
$$

Le corrigé distingue l’enveloppe exponentielle décroissante et le facteur harmonique.

**6.b)** Le graphe représente $Z(t)$ en fonction de $t$ : une sinusoïde amortie autour de zéro, comprise entre deux enveloppes exponentielles symétriques qui tendent vers zéro.

**6.c)** La pseudo-pulsation et la pseudo-période vérifient

$$
\omega=\sqrt{\omega_0^2-(\Gamma/2)^2}=\frac{2\pi}{T}.
$$

**6.d)** En dérivant,

$$
\dot Z(t)=e^{-\Gamma t/2}\left\{
-\frac\Gamma2[A_c\cos(\omega t)+A_s\sin(\omega t)]
+\omega[-A_c\sin(\omega t)+A_s\cos(\omega t)]\right\}.
$$

Les conditions initiales donnent

$$
Z(0)=0=A_c,\qquad\dot Z(0)=v_0=\omega A_s.
$$

Donc

$$
Z(t)=\frac{v_0}{\omega}e^{-\Gamma t/2}\sin(\omega t).
$$
