---
source: "PREING2-S2/Ondes-CC/CC3-2021-2022-Correction_Ondes-CC_P2S2.pdf"
pages: 5
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle des cinq pages manuscrites ; équations de dispersion, séparation des variables et intégration par parties vérifiées ; bord rogné signalé
---

# Ondes — CC3 2021–2022 — Corrigé

> Le document contient les réponses seules, sans énoncé. La notation temporelle manuscrite est rendue par $t$. Les erreurs de calcul de la source sont conservées puis signalées.

## Question 1 — Solution générale [2 pt ; page 1]

$$
F(x,t)=G_+(ct+x)+G_-(ct-x),
$$

avec $G_+$ et $G_-$ des fonctions arbitraires.

## Question 2 — Dispersion [3 pt ; page 1]

On pose

$$
F(x,t)=e^{i(\omega t-kx)}.
$$

La substitution dans l’équation de l’énoncé, non reproduite dans ce fichier, donne

$$
-\frac{\omega^2}{c^2}+k^2+m^2c^2=0.
$$

La relation de dispersion est donc

$$
\omega^2=c^2(k^2+m^2c^2).
$$

Le corrigé retient la branche positive pour écrire la vitesse de phase

$$
v_\varphi=\frac\omega k=c\sqrt{1+\frac{m^2c^2}{k^2}},
$$

et la vitesse de groupe

$$
v_g=\frac{d\omega}{dk}
=\frac{ck}{\sqrt{k^2+m^2c^2}}
=\frac{c^2}{v_\varphi}.
$$

## Question 3 — Séparation des variables [3 pt ; page 2]

On pose $F(x,y,t)=A(x)B(y)C(t)$. L’équation devient

$$
\frac1{\alpha^2}ABC''-A''BC-AB''C=0,
$$

puis, là où les divisions sont définies,

$$
\frac1{\alpha^2}\frac{C''}{C}-\frac{A''}{A}-\frac{B''}{B}=0.
$$

Les trois termes dépendent respectivement de $t$, de $x$ et de $y$ ; chacun doit être constant. Le corrigé choisit

$$
C''=-\omega^2C,\qquad A''=-k_x^2A,\qquad B''=-k_y^2B,
$$

avec

$$
\omega^2=\alpha^2(k_x^2+k_y^2).
$$

## Question longue — Corde et modes propres (pages 3 à 5)

### a) Onde plane et vitesse de phase [2 pt]

En posant $F(x,t)=e^{i(\omega t-kx)}$, on obtient

$$
\frac\mu{T_0}\omega^2-k^2=0,
\qquad\omega^2=\frac{T_0}{\mu}k^2.
$$

La vitesse de phase est

$$
v_\varphi=\frac\omega k=\sqrt{\frac{T_0}{\mu}}.
$$

### b) Conditions aux bords et modes [4 pt]

On cherche

$$
F(x,t)=e^{i\omega t}[A\cos(kx)+B\sin(kx)].
$$

Les dérivées vérifient

$$
\frac{\partial^2F}{\partial t^2}=-\omega^2F,
\qquad\frac{\partial^2F}{\partial x^2}=-k^2F.
$$

C’est donc une solution si $\omega^2=(T_0/\mu)k^2$. Les conditions sont

$$
F(0,t)=F(L,t)=0.
$$

La première donne $A=0$ ; la seconde donne $B\sin(kL)=0$. Pour un mode non nul,

$$
k=\frac{n\pi}{L},\qquad n=1,2,\ldots.
$$

La solution réelle s’écrit

$$
F(x,t)=\sum_{n=1}^{\infty}
[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)]
\sin\left(\frac{n\pi x}{L}\right),
$$

avec

$$
n\omega_0=\sqrt{\frac{T_0}{\mu}}\frac{n\pi}{L},
\qquad\omega_0=\sqrt{\frac{T_0}{\mu}}\frac\pi L.
$$

> Le bas de la page 3 est rogné dans le scan : une partie des dénominateurs de cette dernière ligne n’est plus visible. Ils sont restitués à partir des deux relations entièrement lisibles qui précèdent, $\omega^2=(T_0/\mu)k^2$ et $k=n\pi/L$.

### c) Coefficients à partir des conditions initiales [3 pt ; page 4]

À $t=0$,

$$
F(x,0)=\sum_{n=1}^{\infty}a_n\sin\left(\frac{n\pi x}{L}\right),
$$

d’où

$$
a_n=\frac2L\int_0^L\sin\left(\frac{n\pi x}{L}\right)F(x,0)\,dx.
$$

De même,

$$
\left.\frac{\partial F}{\partial t}(x,t)\right|_{t=0}
=\sum_{n=1}^{\infty}b_n\omega_0n\sin\left(\frac{n\pi x}{L}\right),
$$

et

$$
b_n=\frac2{nL\omega_0}\int_0^L
\sin\left(\frac{n\pi x}{L}\right)
\left.\frac{\partial F}{\partial t}(x,t)\right|_{t=0}\,dx.
$$

### d) Application [3 pt ; pages 4 et 5]

La vitesse initiale est nulle, donc $b_n=0$. Pour le profil initial utilisé dans le corrigé,

$$
a_n=\frac2L\int_0^{L/2}x\sin\left(\frac{n\pi x}{L}\right)dx.
$$

L’intégration par parties est écrite

$$
a_n=\frac2L\left\{
\left[-\frac L{n\pi}x\cos\left(\frac{n\pi x}{L}\right)\right]_0^{L/2}
+\frac L{n\pi}\int_0^{L/2}\cos\left(\frac{n\pi x}{L}\right)dx
\right\}.
$$

La page 5 donne ensuite

$$
a_n=-\frac L{n\pi}\cos\left(\frac{n\pi}2\right)
+\frac{L^2}{n^2\pi^2}\left[\sin\left(\frac{n\pi x}{L}\right)\right]_0^{L/2},
$$

puis le résultat encadré

$$
a_n=-\frac L{n\pi}\cos\left(\frac{n\pi}2\right)
+\frac{L^2}{n^2\pi^2}\sin\left(\frac{n\pi}2\right).
\tag{résultat source}
$$

> **Erreur de facteur dans la source.** Le facteur extérieur $2/L$ a été oublié dans le second terme après intégration. À partir de l’intégrale affichée, le résultat est
>
> $$
> a_n=-\frac L{n\pi}\cos\left(\frac{n\pi}2\right)
> +\frac{2L}{n^2\pi^2}\sin\left(\frac{n\pi}2\right).
> $$
