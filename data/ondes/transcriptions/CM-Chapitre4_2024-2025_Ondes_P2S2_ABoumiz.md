---
source: "PREING2-S2/Ondes/CM-Chapitre4_2024-2025_Ondes_P2S2_ABoumiz.pdf"
pages: 29
transcription: manuelle
transcription_date: 2026-10-04
verification: lecture visuelle des vingt-neuf pages ; formules, démonstrations et schémas vérifiés ; erreurs originales annotées
---

# Chapitre 4 — Ondes

## Section 4.1 — Chaîne de $N$ oscillateurs (pages 1 et 2)

Une chaîne est constituée de $N$ petits blocs identiques, de même masse $M$, espacés de la même distance $L_0$ et alignés suivant la droite $(Ox)$. Une petite perturbation modifie l’équilibre initial ; elle se déplace de proche en proche le long de la chaîne et provoque un petit déplacement de chaque bloc.

On admet que les forces d’interaction de chaque bloc se limitent à ses deux voisins immédiats : $n-1$ et $n+1$ pour le bloc $n$. Ces interactions sont du même type que la tension d’un système masse-ressort de raideur $k$. $X_n$ désigne la position de la masse $n$ par rapport à sa position d’équilibre, pour $1\le n\le N$.

**Schéma :** chaîne de masses numérotées $1,2,3,\ldots,n-1,n,n+1,\ldots,N-1,N$, reliées par des ressorts de raideur $K_0$ ; les deux extrémités de la chaîne sont attachées à des parois fixes.

## Équation du mouvement du bloc $n$ (pages 3 et 4)

Projections des forces de rappel exercées par les voisins :

$$
f_{n+1\to n}=-K_0(X_n-X_{n+1}),
\qquad f_{n-1\to n}=-K_0(X_n-X_{n-1}).
$$

La deuxième loi de Newton donne :

$$
M\ddot X_n=f_{n-1\to n}+f_{n+1\to n}
=K_0(X_{n+1}-X_n)-K_0(X_n-X_{n-1}),
$$

$$
\ddot X_n+\frac{K_0}{M}(2X_n-X_{n-1}-X_{n+1})=0,
\qquad\omega^2=\frac{K_0}{M}.
$$

Le cours appelle $\omega_0$ la pulsation propre de chacun des $N$ blocs identiques constituant la chaîne. Les termes $X_n$ s’additionnent et ne s’éliminent pas. La solution $X_n$ dépend de $X_{n-1}$ et de $X_{n+1}$ : le mouvement de chaque bloc dépend de celui de ses voisins. La perturbation se déplace de proche en proche ; c’est une onde mécanique qui se propage le long de la chaîne.

> La source alterne $M$ et $m$, $k$ et $K_0$, puis $\omega$ et $\omega_0$. Ici $\omega=\sqrt{K_0/M}$ est le paramètre de couplage. Un bloc dont les deux voisins seraient immobilisés oscillerait à $\sqrt{2K_0/M}$.

## Équations aux extrémités (page 5)

Pour le bloc $n$ :

$$
\ddot X_n+2\omega^2X_n-\omega^2(X_{n-1}+X_{n+1})=0.
$$

La source écrit pour le premier bloc, avec $X_0=0$ :

$$
\ddot X_1+2\omega^2X_1-\omega^2(X_0+X_1)=0,
$$

et pour le dernier :

$$
\ddot X_N+2\omega^2X_N-\omega^2(X_{N-1}+X_{n+1})=0.
$$

> Coquilles d’indices : dans la première équation, le voisin est $X_2$, pas $X_1$ ; dans la dernière, lire $X_{N+1}$. Les extrémités fixées correspondent à $X_0=X_{N+1}=0$.

## Limite continue (pages 6 et 7)

On s’intéresse à $N$ grand et $L_0$ petit. Soit $F(X,t)$ telle que $F(nL_0,t)=X_n(t)$. Alors :

$$
X_{n\pm1}(t)=F((n\pm1)L_0,t)
\simeq F(nL_0,t)
\pm\left.\frac{\partial F}{\partial X}\right|_{X=nL_0}L_0
+\frac12\left.\frac{\partial^2F}{\partial X^2}\right|_{X=nL_0}L_0^2.
$$

> La source met aussi un $\pm$ devant le terme du second ordre. Ce terme est positif dans les **deux** développements ; le signe est rétabli ici.

On obtient, à cet ordre :

$$
2X_n-X_{n-1}-X_{n+1}
\simeq-\left.\frac{\partial^2F(X,t)}{\partial X^2}\right|_{X=nL_0}L_0^2,
$$

$$
\frac{\partial^2F(nL_0,t)}{\partial t^2}
-\omega^2L_0^2\left.\frac{\partial^2F(X,t)}{\partial X^2}\right|_{X=nL_0}=0.
$$

La page 7 introduit $k^2=1/L_0^2$ et écrit :

$$
\frac1{\omega^2}\frac{\partial^2F}{\partial t^2}
-\frac1{k^2}\frac{\partial^2F}{\partial X^2}=0,\tag{*}
$$

puis :

$$
\frac{\partial^2F}{\partial X^2}
-\frac{k^2}{\omega^2}\frac{\partial^2F}{\partial t^2}=0,
\qquad\frac{k^2}{\omega^2}=\frac1{c^2}.
$$

$c$ est la vitesse de phase. D’où l’équation d’onde :

$$
\frac{\partial^2F(X,t)}{\partial X^2}
-\frac1{c^2}\frac{\partial^2F(X,t)}{\partial t^2}=0.
$$

> La source appelle $k=1/L_0$ « nombre d’onde (en cm$^{-1}$) ». Ici, il s’agit de l’inverse du pas de la chaîne ; ce n’est pas le nombre d’onde libre d’un mode. La célérité obtenue est $c=\omega L_0=L_0\sqrt{K_0/M}$.

## Solution de l’équation d’onde — Règle de la chaîne (pages 8 et 9)

Soit $G(z)$ une fonction d’une variable et $\phi(x,t)$ une fonction de deux variables. Les points de la source sur $G$ désignent ses dérivées par rapport à son argument ; on les note ici $G'$ et $G''$ :

$$
\partial_tG(\phi)=G'(\phi)\partial_t\phi,
$$

$$
\partial_t^2G(\phi)=G''(\phi)(\partial_t\phi)^2+G'(\phi)\partial_t^2\phi,
\qquad
\partial_x^2G(\phi)=G''(\phi)(\partial_x\phi)^2+G'(\phi)\partial_x^2\phi.
$$

Dans (*) :

$$
\begin{aligned}
\frac1{\omega^2}\partial_t^2G(\phi)-\frac1{k^2}\partial_x^2G(\phi)
&=\frac1{\omega^2}\left[G''(\partial_t\phi)^2+G'\partial_t^2\phi\right]
-\frac1{k^2}\left[G''(\partial_x\phi)^2+G'\partial_x^2\phi\right]\\
&=G''\left[\frac{(\partial_t\phi)^2}{\omega^2}-\frac{(\partial_x\phi)^2}{k^2}\right]
+G'\left[\frac{\partial_t^2\phi}{\omega^2}-\frac{\partial_x^2\phi}{k^2}\right].
\end{aligned}
$$

Si $\phi(x,t)=\omega t\pm kx$, alors :

$$
\frac{(\partial_t\phi)^2}{\omega^2}
=\frac{(\partial_x\phi)^2}{k^2}=1,
\qquad\partial_t^2\phi=\partial_x^2\phi=0.
$$

## Solution générale et retour à la chaîne discrète (page 10)

La solution générale de l’équation d’onde est :

$$
F(X,t)=G_+(\omega t+kX)+G_-(\omega t-kX),
$$

où $G_+$ et $G_-$ sont deux fonctions $C^2$ arbitraires.

> Le « rappel » de la source affirme qu’une équation différentielle d’ordre $n$ contient $n$ fonctions arbitraires dans sa solution générale. Ce n’est pas vrai en général : une équation différentielle **ordinaire** régulière d’ordre $n$ comporte $n$ constantes ; l’équation d’onde étudiée ici est une équation aux dérivées partielles dont la solution sur la droite comporte deux fonctions.

Pour la chaîne discrète, posons $X_n=A_ne^{i\lambda t}$. L’équation devient :

$$
-\lambda^2A_n+2\omega^2A_n-\omega^2(A_{n-1}+A_{n+1})=0.
$$

## Récurrence sur les amplitudes (pages 11 et 12)

$$
A_{n+1}=2\beta A_n-A_{n-1},
\qquad\beta=1-\frac{\lambda^2}{2\omega^2},
\qquad A_2=2\beta A_1.
$$

$A_{N+1}=A_0=0$, car la chaîne est fixée aux extrémités. La solution proposée est :

$$
A_n=\frac{\sin(n\theta)}{\sin\theta}A_1,
\qquad\beta=\cos\theta.
$$

**Preuve.** Posons $\beta=(q+q^{-1})/2$. Pour $n=1$ :

$$
A_1=\frac{q-q^{-1}}{q-q^{-1}}A_1.
$$

Pour $n=2$ :

$$
A_2=(q+q^{-1})A_1,
\qquad
\frac{q^2-q^{-2}}{q-q^{-1}}
=\frac{(q+q^{-1})(q-q^{-1})}{q-q^{-1}}=q+q^{-1}.
$$

Supposons le résultat vrai pour $A_n$ et $A_{n-1}$ :

$$
A_{n+1}=\left[(q+q^{-1})\frac{q^n-q^{-n}}{q-q^{-1}}
-\frac{q^{n-1}-q^{1-n}}{q-q^{-1}}\right]A_1.
$$

Ainsi :

$$
\frac{A_{n+1}}{A_1}
=\frac{q^{n+1}-q^{-n-1}}{q-q^{-1}}
=\frac{\sin((n+1)\theta)}{\sin\theta},
$$

en prenant $q=e^{i\theta}$. Donc :

$$
X_n=\frac{\sin(n\theta)}{\sin\theta}A_1e^{i\lambda t},
\qquad X_{N+1}=0\Longrightarrow\sin((N+1)\theta)=0
\Longrightarrow\theta_k=\frac{k\pi}{N+1}.
$$

> La page 12 écrit $\sin(n\theta)$ au lieu de $\sin((n+1)\theta)$ dans le quotient donnant $A_{n+1}/A_1$ ; l’indice est corrigé ci-dessus.

## Modes et pulsations propres (page 13)

$$
1-\frac{\lambda_k^2}{2\omega^2}=\cos\theta_k,
\qquad\cos\theta_k=1-2\sin^2(\theta_k/2),
\qquad\theta_k=\frac{k\pi}{N+1}.
$$

On obtient :

$$
\lambda_k=2\omega\sin\left(\frac{k\pi}{2(N+1)}\right),
\qquad
X_n^k=\frac{\sin(n\theta_k)}{\sin\theta_k}e^{i\lambda_kt}.
$$

> La source donne $k=1,\ldots,N+1$. Les $N$ modes non nuls correspondent à **$k=1,\ldots,N$** ; $k=N+1$ donne $\theta_k=\pi$ et rend le quotient affiché indéfini.

## Modes propres à la limite continue (page 14)

En absorbant la normalisation dans l’amplitude et en posant $L=L_0(N+1)$ :

$$
F_k(nL_0,t)=\sin\left(\frac{knL_0\pi}{L_0(N+1)}\right)e^{i\lambda_kt},
$$

$$
\lambda_k=2\omega\sin\left(\frac{k\pi}{2(N+1)}\right)
\simeq\frac{k\omega\pi}{N+1}.
$$

Comme $c=\omega L_0$ :

$$
F_k(nL_0,t)=\sin\left(\frac{knL_0\pi}{L}\right)
e^{ikt\omega L_0\pi/[L_0(N+1)]}
=\sin\left(\frac{knL_0\pi}{L}\right)e^{ictk\pi/L},
$$

puis :

$$
F_k(x,t)=\sin\left(\frac{k\pi x}{L}\right)e^{ictk\pi/L},
\qquad
F(x,t)=\sum_{k=1}^{\infty}\sin\left(\frac{k\pi x}{L}\right)
\left(A_ke^{ictk\pi/L}+B_ke^{-ictk\pi/L}\right).
$$

> La linéarisation du sinus demande $k/(N+1)\ll1$ ; $N$ grand ne suffit pas pour les modes proches de l’extrémité du spectre.

## Section 4.2 — Vitesse de groupe, vitesse de phase et conditions aux limites (page 15)

L’équation d’onde $c^{-2}\partial_t^2F-\partial_x^2F=0$ conduit à la relation de dispersion :

$$
\frac{\omega^2}{c^2}-k^2=0,
\qquad\omega^2=k^2c^2.
$$

Modes propres :

$$
\phi_{j,k}^{\,\pm}(x,t)=e^{\pm i(\omega_j(k)t-kx)}.
$$

Ils sont périodiques :

$$
\phi_{j,k}^{\,\pm}(x,t)
=\phi_{j,k}^{\,\pm}(x+\lambda,t)
=\phi_{j,k}^{\,\pm}(x,t+\tau),
$$

avec $\lambda=2\pi/K$ la longueur d’onde et $\tau$ la période. La source alterne $k$ et $K$ pour le nombre d’onde.

## Vitesse de phase et vitesse de groupe (page 16)

$$
\phi_{j,k}^{\,\pm}(x+\Delta x,t+\Delta t)
=e^{\pm i(\omega_jt-Kx)}e^{\pm i(\omega_j\Delta t-K\Delta x)}.
$$

En suivant une phase constante, $\omega_j\Delta t-K\Delta x=0$, donc :

$$
\frac{\Delta x}{\Delta t}=\frac{\omega_j}{K}
=\text{vitesse de phase}.
$$

Le rapport $\omega_j/K$ a les unités d’une vitesse, comme $\partial\omega_j/\partial K$. Cette dernière est la vitesse de groupe ; que mesure-t-elle ? Pour $\Delta k$ petit :

$$
\begin{aligned}
\phi_{j,k+\Delta k}^{\,\pm}(x,t)
&=e^{\pm i[\omega_j(k+\Delta k)t-(k+\Delta k)x]}\\
&\simeq e^{\pm i[\omega_j(k)t-kx]}
e^{\pm i\Delta k[(\partial\omega_j/\partial k)t-x]}.
\end{aligned}
$$

Le dernier facteur correspond à une onde se déplaçant à la vitesse $\partial\omega_j/\partial k$.

## Deux ondes et leur enveloppe (pages 17 et 18)

Soient $\phi_1=\cos(\omega_1t-k_1x)$ et $\phi_2=\cos(\omega_2t-k_2x)$, avec $\omega_i=\omega(k_i)$ :

$$
\phi_1+\phi_2
=2\cos\left(\frac{\omega_1+\omega_2}{2}t-\frac{k_1+k_2}{2}x\right)
\cos\left(\frac{\omega_1-\omega_2}{2}t-\frac{k_1-k_2}{2}x\right).
$$

Le premier facteur correspond à une onde de vitesse $(\omega_1+\omega_2)/(k_1+k_2)$ ; le second, l’enveloppe, à une onde de vitesse $(\omega_1-\omega_2)/(k_1-k_2)$.

**Schéma de la page 18 :** oscillations rapides bleues sous une enveloppe rouge en pointillés. Une flèche bleue repérée $c$ représente le mouvement de la phase ; une flèche rouge repérée $v_g$ celui du paquet d’ondes. Les deux flèches pointent vers la droite ; la légende est « Paquet d’ondes ».

## Section 4.2.1 — Conditions aux bords ou aux limites (page 19)

Les équations différentielles doivent être accompagnées de conditions aux bords pour avoir une solution bien définie. Pour $x\in[a,b]$ :

| Type | Conditions |
| --- | --- |
| Dirichlet | $F(a,t)=\alpha$, $F(b,t)=\beta$. |
| Neumann | $\partial_xF(a,t)=\alpha$, $\partial_xF(b,t)=\beta$. |
| Mixte | Mélange des deux types. |

Si $F_1$ et $F_2$ sont des solutions de l’équation différentielle linéaire, avec :

$$
F_1(a,t)=\alpha,\quad F_1(b,t)=\beta,
\qquad F_2(a,t)=F_2(b,t)=0,
$$

alors $F_1+F_2$ satisfait les mêmes conditions aux bords que $F_1$.

> Le principe de superposition suppose ici l’équation d’onde homogène étudiée ; pour une équation avec second membre non nul, on ajoute une solution de l’équation homogène à une solution particulière.

## Conditions de Dirichlet homogènes (page 20)

Commençons par $\alpha=\beta=0$. On considère :

$$
\phi_k(x,t)=\sum_{j=1}^N\left[r_je^{i(\omega_jt-kx)}+s_je^{-i(\omega_jt-kx)}\right].
$$

On veut déterminer les coefficients $r_j,s_j$ (la source les indice $n$ dans une somme d’indice $j$ ; l’indice est harmonisé ici).

$$
\phi_k(a,t)=e^{-ika}\sum_{j=1}^Nr_je^{i\omega_jt}
+e^{ika}\sum_{j=1}^Ns_je^{-i\omega_jt}=0.
$$

Pour l’équation d’onde, $\omega_1=-\omega_2=\omega(k)$, avec $N=2$. Ainsi :

$$
\phi_k(a,t)=e^{i\omega t}(r_1e^{-ika}+s_2e^{ika})
+e^{-i\omega t}(r_2e^{-ika}+s_1e^{ika})=0,
$$

d’où :

$$
\begin{cases}r_1=-s_2e^{2ika},\\r_2=-s_1e^{2ika}.\end{cases}
$$

De même, $\phi_k(b,t)=0$ donne :

$$
\begin{cases}r_1=-s_2e^{2ikb},\\r_2=-s_1e^{2ikb}.\end{cases}
$$

## Quantification et série de Fourier (page 21)

Pour une solution non nulle :

$$
e^{2ik(b-a)}=1,
\qquad k_n=\frac{n\pi}{b-a},\quad n\in\mathbb Z.
$$

Les modes sont :

$$
\phi_n(x,t)=\sin\left(\frac{n\pi}{b-a}(x-a)\right)
\left(A_ne^{i\omega t}+B_ne^{-i\omega t}\right),
\qquad\omega=\omega\left(\frac{n\pi}{b-a}\right)=\omega(n).
$$

La solution est une série de Fourier :

$$
F(x,t)=\sum_{n=1}^{\infty}\sin\left(\frac{n\pi}{b-a}(x-a)\right)
\left(A_ne^{i\omega_nt}+B_ne^{-i\omega_nt}\right),
\qquad F(a,t)=F(b,t)=0.
$$

Il manque encore une solution particulière de l’équation avec $F(a,t)=\alpha(t)$ et $F(b,t)=\beta(t)$. Le cours remarque que de telles solutions dépendent de l’équation étudiée.

## Conditions de Neumann homogènes — Formule originale (page 22)

La page affirme que des arguments similaires donnent, pour $\partial_xF(a,t)=\partial_xF(b,t)=0$ :

$$
F(x,t)=\sum_{n=1}^{\infty}\sin\left(\frac{n\pi}{b-a}(x-a)\right)
\left(A_ne^{i\omega t}+B_ne^{-i\omega t}\right).
$$

> **Erreur de la source :** ce sont des cosinus qui conviennent aux conditions de Neumann homogènes ; le mode spatial constant doit aussi être pris en compte. La page 27 revient aux cosinus. Pour l’équation d’onde, une écriture complète est $F(x,t)=C_0+D_0t+\sum_{n\ge1}\cos[n\pi(x-a)/(b-a)](A_ne^{i\omega_nt}+B_ne^{-i\omega_nt})$.

## Section 4.2.2 — Conditions initiales (page 23)

En plus des conditions aux bords en $x$, on donne les conditions initiales en $t$ :

$$
F(x,0)=f(x),\qquad\partial_tF(x,0)=g(x).
$$

Pour la solution en sinus (Dirichlet), on cherche à résoudre :

$$
\sum_{n=1}^{\infty}\sin\left(\frac{n\pi(x-a)}{b-a}\right)(A_n+B_n)=f(x),\tag{1}
$$

$$
\sum_{n=1}^{\infty}\sin\left(\frac{n\pi(x-a)}{b-a}\right)
(i\omega_nA_n-i\omega_nB_n)=g(x).\tag{2}
$$

## Recherche des coefficients — Projection (page 24)

Multiplions (1) par $\sin[m\pi(x-a)/(b-a)]$ :

$$
\sin\left(\frac{m\pi(x-a)}{b-a}\right)
\sum_{n=1}^{\infty}\sin\left(\frac{n\pi(x-a)}{b-a}\right)(A_n+B_n)
=f(x)\sin\left(\frac{m\pi(x-a)}{b-a}\right).
$$

Intégrons entre $a$ et $b$ :

$$
\sum_{n=1}^{\infty}\int_a^b
\sin\left(\frac{n\pi(x-a)}{b-a}\right)
\sin\left(\frac{m\pi(x-a)}{b-a}\right)(A_n+B_n)\,dx
=\int_a^b\sin\left(\frac{m\pi(x-a)}{b-a}\right)f(x)\,dx.
$$

## Orthogonalité des sinus (page 25)

Pour $m,n\ge1$ :

$$
\int_a^b\sin\left(\frac{n\pi(x-a)}{b-a}\right)
\sin\left(\frac{m\pi(x-a)}{b-a}\right)\,dx
=\frac{b-a}{2}\delta_{n,m},
\qquad
\delta_{n,m}=\begin{cases}1&n=m,\\0&n\ne m.\end{cases}
$$

La projection précédente donne donc :

$$
\sum_{n=1}^{\infty}\frac{b-a}{2}\delta_{n,m}(A_n+B_n)
=\int_a^b\sin\left(\frac{m\pi(x-a)}{b-a}\right)f(x)\,dx.
$$

## Coefficients déterminés par les conditions initiales (page 26)

$$
A_n+B_n=\frac2{b-a}\int_a^b\sin\left(\frac{n\pi(x-a)}{b-a}\right)f(x)\,dx.
$$

En projetant (2) de la même manière :

$$
\sum_{n=1}^{\infty}\int_a^b
\sin\left(\frac{n\pi(x-a)}{b-a}\right)
\sin\left(\frac{m\pi(x-a)}{b-a}\right)
(i\omega_nA_n-i\omega_nB_n)\,dx
=\int_a^b\sin\left(\frac{m\pi(x-a)}{b-a}\right)g(x)\,dx,
$$

$$
\frac{b-a}{2}i\omega_m(A_m-B_m)
=\int_a^b\sin\left(\frac{m\pi(x-a)}{b-a}\right)g(x)\,dx.
$$

## Conditions initiales pour Neumann (pages 27 et 28)

La source suppose :

$$
F(x,t)=\sum_{n=0}^{\infty}\cos\left(\frac{n\pi(x-a)}{b-a}\right)
\left(A_ne^{i\omega_nt}+B_ne^{-i\omega_nt}\right),
\qquad
F(x,0)=f(x),\quad\partial_tF(x,0)=g(x).
$$

Elle utilise :

$$
\int_a^b\cos\left(\frac{n\pi(x-a)}{b-a}\right)
\cos\left(\frac{m\pi(x-a)}{b-a}\right)\,dx
=\frac{b-a}{2}\delta_{m,n},
$$

puis donne :

$$
A_n+B_n=\frac2{b-a}\int_a^b\cos\left(\frac{n\pi(x-a)}{b-a}\right)f(x)\,dx,
$$

$$
A_n-B_n=\frac2{(b-a)i\omega_n}\int_a^b\cos\left(\frac{n\pi(x-a)}{b-a}\right)g(x)\,dx.
$$

> Ces relations valent pour $n\ge1$. Pour $m=n=0$, l’intégrale d’orthogonalité vaut $b-a$, et non $(b-a)/2$. De plus, $\omega_0=0$ interdit la division par $i\omega_0$. Le mode constant spatial est $C_0+D_0t$, avec $C_0=(b-a)^{-1}\int_a^bf(x)\,dx$ et $D_0=(b-a)^{-1}\int_a^bg(x)\,dx$.

## Exemple — Corde pincée (page 29)

On veut résoudre :

$$
\frac1{c^2}\frac{\partial^2F(X,t)}{\partial t^2}
-\frac{\partial^2F(X,t)}{\partial X^2}=0,
$$

avec $F(0,t)=F(L,t)=0$ et les conditions initiales :

$$
F(x,0)=\begin{cases}
x,&0\le x<L/2,\\
L-x,&L/2\le x\le L,
\end{cases}
\qquad\frac{\partial F(x,0)}{\partial t}=0.
$$

**Schéma :** profil triangulaire nul en $0$ et $L$, sommet en $L/2$, hauteur repérée $A$ ; axes $x$ et $F(x,0)$.

> La source appelle à tort $F(0,t)=F(L,t)=0$ des conditions « initiales » : ce sont des conditions aux bords. Avec la formule affichée, la hauteur du triangle vaut $A=L/2$. Pour une hauteur indépendante $A$, il faudrait multiplier le profil par $2A/L$. Le PDF se termine avec cet énoncé et ne donne pas sa résolution.
