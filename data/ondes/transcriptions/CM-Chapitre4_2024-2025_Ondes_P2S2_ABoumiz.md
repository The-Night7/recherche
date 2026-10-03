---
source: "PREING2-S2/Ondes/CM-Chapitre4_2024-2025_Ondes_P2S2_ABoumiz.pdf"
pages: 29
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle des vingt-neuf pages ; équations, récurrence, schémas et conditions aux limites vérifiés
---

# Ondes — Chapitre 4 — 2024–2025

## 4.1. Chaîne de N oscillateurs (pages 1 à 14)

### Modèle et équations du mouvement (pages 1 à 5)

Une chaîne comporte $N$ petits blocs identiques, de masse $M$, espacés de $L_0$ et alignés suivant $(Ox)$. Une petite perturbation de l’équilibre se déplace de proche en proche et provoque un petit déplacement de chaque bloc.

Les interactions d’un bloc sont limitées à ses deux voisins immédiats, $n-1$ et $n+1$. Elles sont du même type que la tension d’un ressort de constante de raideur $k$, notée ensuite $K_0$. $X_n(t)$ désigne le déplacement de la masse $n$ par rapport à sa position d’équilibre, pour $1\leq n\leq N$.

**Schéma, page 2 :** une chaîne de masses $1,2,3,\ldots,n-1,n,n+1,\ldots,N-1,N$ reliées par des ressorts $K_0$ ; les deux ressorts extrêmes sont attachés à des parois fixes.

Les projections des forces de rappel sur le bloc $n$ sont

$$f_{n+1\to n}=-K_0(X_n-X_{n+1}),\qquad f_{n-1\to n}=-K_0(X_n-X_{n-1}).$$

La deuxième loi de Newton donne

$$\begin{aligned}
M\ddot X_n&=f_{n-1\to n}+f_{n+1\to n}\\
&=K_0(X_{n+1}-X_n)-K_0(X_n-X_{n-1}),\\
\ddot X_n+\frac{K_0}{M}(2X_n-X_{n-1}-X_{n+1})&=0.
\end{aligned}$$

En posant $\omega^2=K_0/M$,

$$\ddot X_n+2\omega^2X_n-\omega^2(X_{n-1}+X_{n+1})=0.$$

Les termes en $X_n$ s’additionnent et ne s’éliminent pas. Le mouvement dépend des deux voisins : une onde mécanique se propage le long de la chaîne.

> La source alterne $M$ et $m$, puis $\omega$ et $\omega_0$. Elle appelle $\omega_0$ « pulsation propre de chacun des blocs ». La définition utilisée dans les calculs est $\omega=\sqrt{K_0/M}$ ; un bloc intérieur dont les deux voisins seraient immobilisés aurait une pulsation $\sqrt{2K_0/M}$.

Pour les extrémités fixes, $X_0=X_{N+1}=0$, d’où

$$\begin{cases}
\ddot X_1+2\omega^2X_1-\omega^2(X_0+X_2)=0,\\
\ddot X_N+2\omega^2X_N-\omega^2(X_{N-1}+X_{N+1})=0.
\end{cases}$$

> Corrections d’indices de la page 5 : la première ligne imprimée contient $X_0+X_1$ au lieu de $X_0+X_2$ ; la dernière emploie $X_{n+1}$ au lieu de $X_{N+1}$.

### Limite continue et équation d’onde (pages 6 et 7)

On considère $N$ grand et $L_0$ petit. On introduit une fonction $F(X,t)$ telle que $F(nL_0,t)=X_n(t)$. Son développement donne

$$\begin{aligned}
X_{n\pm1}(t)&=F((n\pm1)L_0,t)\\
&\simeq F(nL_0,t)\pm L_0\left.\frac{\partial F}{\partial X}\right|_{X=nL_0}
+\frac{L_0^2}{2}\left.\frac{\partial^2F}{\partial X^2}\right|_{X=nL_0}.
\end{aligned}$$

> La source imprime un second $\pm$ devant le terme d’ordre 2. Ce terme est positif dans les deux développements.

Ainsi

$$2X_n-X_{n-1}-X_{n+1}\simeq-L_0^2\left.\frac{\partial^2F}{\partial X^2}\right|_{X=nL_0},$$

puis, à la limite continue,

$$\frac{\partial^2F(nL_0,t)}{\partial t^2}-\omega^2L_0^2\left.\frac{\partial^2F}{\partial X^2}\right|_{X=nL_0}=0.$$

La diapositive pose $k^2=1/L_0^2$ et écrit

$$\frac1{\omega^2}\frac{\partial^2F}{\partial t^2}-\frac1{k^2}\frac{\partial^2F}{\partial X^2}=0.\tag{*}$$

En définissant $k^2/\omega^2=1/c^2$, on obtient

$$\boxed{\frac{\partial^2F}{\partial X^2}-\frac1{c^2}\frac{\partial^2F}{\partial t^2}=0},\qquad c=\omega L_0=L_0\sqrt{\frac{K_0}{M}}.$$

> La page 7 appelle $k=1/L_0$ « nombre d’onde », en $\mathrm{cm}^{-1}$. Ici il s’agit de l’inverse du pas de la chaîne, et $\omega$ reste la fréquence caractéristique du ressort. Dans la section 4.2, les mêmes lettres désignent le nombre d’onde et la pulsation variables d’un mode. Ces deux usages doivent être distingués.

### Solution par fonctions progressives (pages 8 à 10)

Soit $G(z)$ une fonction d’une variable et $\phi(x,t)$ une fonction de deux variables. En notant $G'$ et $G''$ les dérivées par rapport à $z$ — représentées par des points dans la source —, la règle de chaîne donne

$$\begin{aligned}
\partial_tG(\phi)&=G'(\phi)\,\partial_t\phi,\\
\partial_t^2G(\phi)&=G''(\phi)(\partial_t\phi)^2+G'(\phi)\partial_t^2\phi,\\
\partial_X^2G(\phi)&=G''(\phi)(\partial_X\phi)^2+G'(\phi)\partial_X^2\phi.
\end{aligned}$$

Dans l’équation $(*)$,

$$\begin{aligned}
\frac1{\omega^2}\partial_t^2G(\phi)-\frac1{k^2}\partial_X^2G(\phi)
&=\frac1{\omega^2}\bigl[G''(\phi)(\partial_t\phi)^2+G'(\phi)\partial_t^2\phi\bigr]\\
&\quad-\frac1{k^2}\bigl[G''(\phi)(\partial_X\phi)^2+G'(\phi)\partial_X^2\phi\bigr]\\
&=G''(\phi)\left[\frac{(\partial_t\phi)^2}{\omega^2}-\frac{(\partial_X\phi)^2}{k^2}\right]
+G'(\phi)\left[\frac{\partial_t^2\phi}{\omega^2}-\frac{\partial_X^2\phi}{k^2}\right].
\end{aligned}$$

Si $\phi(x,t)=\omega t\pm kX$, les deux premiers rapports sont égaux à $1$ et $\partial_t^2\phi=\partial_X^2\phi=0$. La solution générale est donc

$$F(X,t)=G_+(\omega t+kX)+G_-(\omega t-kX),$$

où $G_+$ et $G_-$ sont deux fonctions $C^2$ arbitraires.

> Le « rappel » de la page 10 affirme qu’une équation différentielle d’ordre $n$ a $n$ fonctions arbitraires dans sa solution. Ce n’est pas une règle générale : pour une équation différentielle ordinaire d’ordre $n$, il s’agit normalement de $n$ constantes. Les deux fonctions arbitraires interviennent ici dans l’équation aux dérivées partielles d’onde.

### Modes de la chaîne discrète (pages 10 à 13)

On revient au système discret et on pose $X_n=A_ne^{i\lambda t}$. Alors

$$-\lambda^2A_n+2\omega^2A_n-\omega^2(A_{n-1}+A_{n+1})=0,$$

soit

$$A_{n+1}=2\beta A_n-A_{n-1},\qquad\beta=1-\frac{\lambda^2}{2\omega^2},\qquad A_2=2\beta A_1.$$

Les conditions de fixation sont $A_0=A_{N+1}=0$. En posant $\beta=\cos\theta$, la solution de la récurrence est

$$A_n=\frac{\sin(n\theta)}{\sin\theta}A_1.$$

**Preuve par récurrence.** On pose $\beta=(q+q^{-1})/2$. Pour $n=1$,

$$A_1=\frac{q-q^{-1}}{q-q^{-1}}A_1.$$

Pour $n=2$, $A_2=(q+q^{-1})A_1$ et

$$\frac{q^2-q^{-2}}{q-q^{-1}}=\frac{(q+q^{-1})(q-q^{-1})}{q-q^{-1}}=q+q^{-1}.$$

En supposant le résultat vrai aux rangs $n$ et $n-1$,

$$\begin{aligned}
A_{n+1}&=\left[(q+q^{-1})\frac{q^n-q^{-n}}{q-q^{-1}}-\frac{q^{n-1}-q^{1-n}}{q-q^{-1}}\right]A_1,\\
\frac{A_{n+1}}{A_1}&=\frac{q^{n+1}-q^{-n-1}}{q-q^{-1}}=\frac{\sin((n+1)\theta)}{\sin\theta},\qquad q=e^{i\theta}.
\end{aligned}$$

> La dernière égalité de la page 12 imprime $\sin(n\theta)$ au lieu de $\sin((n+1)\theta)$.

On en déduit

$$X_n=\frac{\sin(n\theta)}{\sin\theta}A_1e^{i\lambda t},\qquad
X_{N+1}=0\Longrightarrow\sin((N+1)\theta)=0\Longrightarrow\theta_k=\frac{k\pi}{N+1}.$$

Puis

$$1-\frac{\lambda_k^2}{2\omega^2}=\cos\theta_k=1-2\sin^2\frac{\theta_k}{2},\qquad
\boxed{\lambda_k=2\omega\sin\frac{k\pi}{2(N+1)}}.$$

À un facteur d’amplitude près, les modes propres sont

$$X_n^{(k)}(t)=\frac{\sin(n\theta_k)}{\sin\theta_k}e^{i\lambda_kt},\qquad k=1,\ldots,N.$$

> La page 13 indique $k=1,\ldots,N+1$. Il existe $N$ modes indépendants pour ces $N$ masses. Le rang $N+1$, qui donnerait $\theta=\pi$, ne fournit pas un mode supplémentaire et rend cette expression singulière.

### Modes de la limite continue (page 14)

En absorbant la normalisation dans l’amplitude et en posant $L=L_0(N+1)$,

$$F_k(nL_0,t)=\sin\left(\frac{knL_0\pi}{L_0(N+1)}\right)e^{i\lambda_kt}.$$

Pour les modes de grande longueur d’onde,

$$\lambda_k=2\omega\sin\frac{k\pi}{2(N+1)}\simeq\frac{k\omega\pi}{N+1}.$$

> La source justifie l’approximation par $N+1$ grand. Il faut plus précisément $k\ll N+1$.

Avec $c=\omega L_0$,

$$\begin{aligned}
F_k(nL_0,t)&=\sin\frac{knL_0\pi}{L}\,e^{ikt\omega L_0\pi/[L_0(N+1)]}\\
&=\sin\frac{knL_0\pi}{L}\,e^{ictk\pi/L},\\
F_k(x,t)&=\sin\frac{k\pi x}{L}\,e^{ictk\pi/L}.
\end{aligned}$$

La superposition des modes dans le modèle continu donne

$$F(x,t)=\sum_{k=1}^{\infty}\sin\frac{k\pi x}{L}\left(A_ke^{ictk\pi/L}+B_ke^{-ictk\pi/L}\right).$$

## 4.2. Vitesses de groupe et de phase (pages 15 à 18)

L’équation d’onde et sa relation de dispersion sont

$$\frac1{c^2}\partial_t^2F-\partial_x^2F=0,\qquad
\frac{\omega^2}{c^2}-k^2=0\Longleftrightarrow\omega^2=k^2c^2.$$

Les modes s’écrivent $\phi_{j,k}^{\pm}(x,t)=e^{\pm i(\omega_j(k)t-kx)}$. La périodicité se traduit par

$$\phi(x,t)=\phi(x+\lambda,t)=\phi(x,t+\tau),\qquad\lambda=\frac{2\pi}{k},$$

où $\lambda$ est la longueur d’onde et $\tau$ la période temporelle. La source alterne $k$ et $K$ pour le nombre d’onde.

### Vitesse de phase (page 16)

$$\phi(x+\Delta x,t+\Delta t)=e^{\pm i(\omega_jt-kx)}e^{\pm i(\omega_j\Delta t-k\Delta x)}.$$

Pour suivre une phase constante, $\omega_j\Delta t-k\Delta x=0$, donc

$$v_\varphi=\frac{\Delta x}{\Delta t}=\frac{\omega_j(k)}{k}.$$

### Vitesse de groupe (pages 16 et 17)

La vitesse de groupe est $v_g=d\omega_j/dk$. Pour une petite variation $\Delta k$,

$$\begin{aligned}
\phi_{j,k+\Delta k}^{\pm}(x,t)&=e^{\pm i[\omega_j(k+\Delta k)t-(k+\Delta k)x]}\\
&\simeq e^{\pm i(\omega_j(k)t-kx)}e^{\pm i\Delta k[(d\omega_j/dk)t-x]}.
\end{aligned}$$

Le dernier facteur se déplace à la vitesse $d\omega_j/dk$.

Pour $\phi_1=\cos(\omega_1t-k_1x)$ et $\phi_2=\cos(\omega_2t-k_2x)$, avec $\omega_i=\omega(k_i)$,

$$\phi_1+\phi_2=2\cos\left(\frac{\omega_1+\omega_2}{2}t-\frac{k_1+k_2}{2}x\right)
\cos\left(\frac{\omega_1-\omega_2}{2}t-\frac{k_1-k_2}{2}x\right).$$

Le premier facteur oscille à la vitesse $(\omega_1+\omega_2)/(k_1+k_2)$. L’enveloppe, donnée par le second, se déplace à la vitesse $(\omega_1-\omega_2)/(k_1-k_2)$.

**Figure, page 18 :** un paquet d’ondes comporte des oscillations rapides bleues sous une enveloppe rouge en pointillés. Une flèche bleue vers la droite porte la vitesse $c$ et une flèche rouge la vitesse $V_g$ de l’enveloppe.

## 4.2.1. Conditions aux limites (pages 19 à 22)

Une équation différentielle doit être accompagnée de conditions aux limites pour définir le problème. Sur $[a,b]$, on distingue :

- **Dirichlet :** $F(a,t)=\alpha$ et $F(b,t)=\beta$.
- **Neumann :** $\partial_xF(a,t)=\alpha$ et $\partial_xF(b,t)=\beta$.
- **Mixtes :** une combinaison des deux types.

Si $F_1$ satisfait les valeurs $\alpha,\beta$ aux extrémités et si $F_2$ satisfait des conditions homogènes, leur somme conserve les valeurs $\alpha,\beta$. Pour la superposition des équations, on considère ici une équation linéaire homogène ; avec un second membre, $F_2$ doit résoudre l’équation homogène associée.

### Dirichlet homogène : détermination des nombres d’onde (pages 20 et 21)

On commence par $\alpha=\beta=0$. La combinaison des branches est

$$\phi_k(x,t)=\sum_{j=1}^{N}\left[r_je^{i(\omega_jt-kx)}+s_je^{-i(\omega_jt-kx)}\right].$$

> Les indices $r_n,s_n$ imprimés dans la source sont harmonisés ici avec l’indice de sommation $j$. Le $N$ de cette expression compte les branches et ne désigne plus les masses de la section 4.1.

La condition en $a$ donne

$$\phi_k(a,t)=e^{-ika}\sum_jr_je^{i\omega_jt}+e^{ika}\sum_js_je^{-i\omega_jt}=0.$$

Pour l’équation d’onde, les deux branches sont $\omega_1=-\omega_2=\omega(k)$, donc $N=2$. Ainsi

$$\phi_k(a,t)=e^{i\omega t}(r_1e^{-ika}+s_2e^{ika})+e^{-i\omega t}(r_2e^{-ika}+s_1e^{ika})=0$$

si et seulement si

$$r_1=-s_2e^{2ika},\qquad r_2=-s_1e^{2ika}.$$

De même, la condition en $b$ impose $r_1=-s_2e^{2ikb}$ et $r_2=-s_1e^{2ikb}$. Une solution non nulle exige

$$e^{2ik(b-a)}=1\Longrightarrow k_n=\frac{n\pi}{b-a},\qquad n\in\mathbb Z.$$

Les modes et leur superposition s’écrivent alors

$$\phi_n(x,t)=\sin\frac{n\pi(x-a)}{b-a}\left(A_ne^{i\omega_nt}+B_ne^{-i\omega_nt}\right),\qquad
\omega_n=\omega\left(\frac{n\pi}{b-a}\right),$$

$$F(x,t)=\sum_{n=1}^{\infty}\sin\frac{n\pi(x-a)}{b-a}\left(A_ne^{i\omega_nt}+B_ne^{-i\omega_nt}\right),\qquad F(a,t)=F(b,t)=0.$$

Pour des valeurs imposées $F(a,t)=\alpha(t)$ et $F(b,t)=\beta(t)$, il faut ajouter une solution particulière appropriée, dont la recherche dépend de l’équation étudiée.

### Neumann homogène : erreur de la page 22

La page 22 répète la série en sinus précédente en lui associant $\partial_xF(a,t)=\partial_xF(b,t)=0$. Cette série ne vérifie pas en général ces conditions : il faut des cosinus, comme l’indique ensuite la page 27, et traiter le mode constant séparément.

## Conditions initiales et calcul des coefficients (pages 23 à 28)

### Dirichlet : développement en sinus (pages 23 à 26)

On impose

$$F(x,0)=f(x),\qquad\partial_tF(x,0)=g(x).$$

En utilisant la série en sinus, on obtient

$$\sum_{n=1}^{\infty}\sin\frac{n\pi(x-a)}{b-a}(A_n+B_n)=f(x),\tag{1}$$

$$\sum_{n=1}^{\infty}\sin\frac{n\pi(x-a)}{b-a}\,i\omega_n(A_n-B_n)=g(x).\tag{2}$$

On multiplie (1) par $\sin(m\pi(x-a)/(b-a))$ et on intègre de $a$ à $b$ :

$$\sum_{n=1}^{\infty}(A_n+B_n)\int_a^b\sin\frac{n\pi(x-a)}{b-a}\sin\frac{m\pi(x-a)}{b-a}\,dx
=\int_a^bf(x)\sin\frac{m\pi(x-a)}{b-a}\,dx.$$

L’orthogonalité donne, pour $m,n\geq1$,

$$\int_a^b\sin\frac{n\pi(x-a)}{b-a}\sin\frac{m\pi(x-a)}{b-a}\,dx=\frac{b-a}{2}\delta_{nm},\qquad
\delta_{nm}=\begin{cases}1&n=m,\\0&n\ne m.\end{cases}$$

Ainsi

$$\sum_{n=1}^{\infty}\frac{b-a}{2}\delta_{nm}(A_n+B_n)=\int_a^bf(x)\sin\frac{m\pi(x-a)}{b-a}\,dx,$$

et

$$A_n+B_n=\frac2{b-a}\int_a^bf(x)\sin\frac{n\pi(x-a)}{b-a}\,dx.$$

La même projection appliquée à (2) donne

$$\sum_{n=1}^{\infty}i\omega_n(A_n-B_n)\int_a^b\sin\frac{n\pi(x-a)}{b-a}\sin\frac{m\pi(x-a)}{b-a}\,dx
=\int_a^bg(x)\sin\frac{m\pi(x-a)}{b-a}\,dx,$$

donc

$$\frac{b-a}{2}i\omega_m(A_m-B_m)=\int_a^bg(x)\sin\frac{m\pi(x-a)}{b-a}\,dx.$$

### Neumann : développement en cosinus (pages 27 et 28)

La source propose

$$F(x,t)=\sum_{n=0}^{\infty}\cos\frac{n\pi(x-a)}{b-a}\left(A_ne^{i\omega_nt}+B_ne^{-i\omega_nt}\right),$$

avec les mêmes conditions initiales $f,g$. Elle utilise

$$\int_a^b\cos\frac{n\pi(x-a)}{b-a}\cos\frac{m\pi(x-a)}{b-a}\,dx=\frac{b-a}{2}\delta_{nm}$$

puis en déduit

$$A_n+B_n=\frac2{b-a}\int_a^bf(x)\cos\frac{n\pi(x-a)}{b-a}\,dx,$$

$$A_n-B_n=\frac2{(b-a)i\omega_n}\int_a^bg(x)\cos\frac{n\pi(x-a)}{b-a}\,dx.$$

> **Mode nul omis dans le traitement de la source :** ces trois dernières formules s’appliquent aux indices strictement positifs. Pour $m=n=0$, l’intégrale vaut $b-a$. Pour l’équation d’onde, $\omega_0=0$ et il est impossible de diviser par $\omega_0$ ; le mode uniforme est affine en temps. La forme complète, explicitée ici, est

$$F(x,t)=a_0+b_0t+\sum_{n=1}^{\infty}\cos\frac{n\pi(x-a)}{b-a}\left(A_ne^{i\omega_nt}+B_ne^{-i\omega_nt}\right),$$

$$a_0=\frac1{b-a}\int_a^bf(x)\,dx,\qquad b_0=\frac1{b-a}\int_a^bg(x)\,dx.$$

## Exemple : corde pincée (page 29)

On considère l’équation d’onde avec extrémités fixes,

$$\frac1{c^2}\partial_t^2F-\partial_x^2F=0,\qquad F(0,t)=F(L,t)=0,$$

et les conditions initiales

$$F(x,0)=\begin{cases}x&x<L/2,\\L-x&x\geq L/2,\end{cases}\qquad\partial_tF(x,0)=0.$$

**Figure :** le profil initial est triangulaire, nul en $0$ et $L$, avec un sommet en $L/2$ étiqueté $A$.

> La diapositive appelle aussi « conditions initiales » les valeurs aux extrémités, qui sont des conditions aux limites. La formule du profil donne une hauteur $L/2$ ; pour une hauteur arbitraire $A$, il faudrait multiplier ce profil par $2A/L$. L’exemple est seulement posé, sans résolution dans ce fichier.
