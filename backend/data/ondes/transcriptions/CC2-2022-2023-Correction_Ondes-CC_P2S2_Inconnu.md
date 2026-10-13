---
source: "PREING2-S2/Ondes-CC/CC2-2022-2023-Correction_Ondes-CC_P2S2_Inconnu.pdf"
pages: 4
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale des quatre pages manuscrites ; développements de Taylor, déterminant, vecteurs propres et conditions initiales vérifiés
---

# Ondes — CC2 2022–2023 — Corrigé

Le manuscrit est titré « DS II ». Le fichier ne contient pas l’énoncé. Barème indiqué : problème I, a) 2 points, b) 3 points, c) 2 points ; problème II, a) 3 points, b) 4 points, c) 3 points, d) 3 points.

## Problème I — Chaîne de ressorts (pages 1 et 2)

Le schéma montre trois masses voisines $n-1,n,n+1$ reliées par des ressorts. Leurs déplacements $x_{n-1},x_n,x_{n+1}$ sont mesurés vers la droite, suivant $\vec u_x$. Les allongements des ressorts de gauche et de droite sont notés $\Delta_-$ et $\Delta_+$.

### a) Énergie, force et équation du mouvement

$$
E_{\mathrm{ressort\ G}}=\frac k2\Delta_-^2
=\frac k2(x_n-x_{n-1})^2,
$$

$$
E_{\mathrm{ressort\ D}}=\frac k2\Delta_+^2
=\frac k2(x_n-x_{n+1})^2.
$$

La force totale sur la masse centrale est

$$
\vec F_{\mathrm{tot}}=-k(2x_n-x_{n-1}-x_{n+1})\vec u_x.
$$

D’où

$$
M\ddot x_n=-k(2x_n-x_{n-1}-x_{n+1}),
$$

$$
\ddot x_n+\frac kM(2x_n-x_{n-1}-x_{n+1})=0.
$$

### b) Limite continue

On pose $F(na_0,t)=x_n(t)$, donc $\ddot x_n=\partial_t^2F(na_0,t)$.

Le développement écrit dans la source est

$$
F((n\pm1)a_0,t)\simeq F(na_0,t)
\pm a_0\left.\frac{\partial F}{\partial x}\right|_{x=na_0}
+a_0^2\left.\frac{\partial^2F}{\partial x^2}\right|_{x=na_0}.
$$

La ligne suivante donne

$$
2F(na_0,t)-F((n+1)a_0,t)-F((n-1)a_0,t)
=-a_0^2\left.\frac{\partial^2F}{\partial x^2}\right|_{x=na_0},
$$

puis

$$
\frac M{ka_0^2}\frac{\partial^2F}{\partial t^2}
-\frac{\partial^2F}{\partial x^2}=0,
\qquad\frac1{c^2}=\frac M{ka_0^2}.
$$

> **Notes de vérification.** Il manque le facteur $1/2$ devant le terme d’ordre deux dans le développement de Taylor imprimé. Avec ce facteur, la différence centrée et l’équation finales sont correctes. Le manuscrit écrit ensuite $c=\sqrt{ka_0/M}$ : il faut $c=a_0\sqrt{k/M}$, conformément au coefficient $1/c^2$ encadré.

### c) Relation de dispersion et vitesse de phase

On pose $F=e^{i(\omega t-\kappa x)}$, où $\kappa$ désigne ici le nombre d’onde afin de le distinguer de la raideur $k$.

$$
-\frac{\omega^2}{c^2}+\kappa^2=0,
\qquad\omega^2=c^2\kappa^2.
$$

La branche retenue dans le corrigé est $\omega=c\kappa$ ; sa vitesse de phase est

$$
v_\varphi=\frac\omega\kappa=c.
$$

## Problème II — Trois modes couplés (pages 2 à 4)

### a) Valeurs propres

$$
W=\omega^2\begin{pmatrix}
0&\cos\theta&0\\
\cos\theta&0&\sin\theta\\
0&\sin\theta&0
\end{pmatrix}.
$$

Le corrigé cherche $\lambda=\delta\omega^2$. Son calcul développe

$$
\begin{vmatrix}
-\delta&\cos\theta&0\\
\cos\theta&-\delta&\sin\theta\\
0&\sin\theta&-\delta
\end{vmatrix}
=-\delta(\delta^2-\sin^2\theta)-\cos\theta(-\delta\cos\theta)
=-\delta^3+\delta(\sin^2\theta+\cos^2\theta)
=\delta(1-\delta^2).
$$

D’où $\delta\in\{-1,0,1\}$ et

$$
\lambda_1=-\omega^2,\qquad\lambda_2=0,\qquad\lambda_3=\omega^2.
$$

> Le facteur global devant le déterminant $\det(W-\delta\omega^2I_3)$ est écrit $\omega^2$ dans le manuscrit. Il vaut $\omega^6$, puisqu’on factorise $\omega^2$ sur trois lignes ; les racines ne changent pas pour $\omega\ne0$.

### b) Vecteurs propres et équations modales

Le corrigé choisit les vecteurs, non normalisés,

$$
\vec V_1=\begin{pmatrix}\sin\theta\\0\\-\cos\theta\end{pmatrix},
\quad
\vec V_2=\begin{pmatrix}\cos\theta\\-1\\\sin\theta\end{pmatrix},
\quad
\vec V_3=\begin{pmatrix}\cos\theta\\1\\\sin\theta\end{pmatrix}.
$$

Les multiplications donnent

$$
W\vec V_1=\vec0=\lambda_2\vec V_1,
$$

$$
W\vec V_2=\omega^2\begin{pmatrix}-\cos\theta\\1\\-\sin\theta\end{pmatrix}
=\lambda_1\vec V_2,
$$

$$
W\vec V_3=\omega^2\begin{pmatrix}\cos\theta\\1\\\sin\theta\end{pmatrix}
=\lambda_3\vec V_3.
$$

> L’ordre des indices des vecteurs diffère de celui des valeurs propres : $\vec V_1$ correspond à $\lambda_2=0$, et $\vec V_2$ à $\lambda_1=-\omega^2$. Ce choix de la source est conservé.

Pour $\ddot{\vec X}+W\vec X=\vec0$, on cherche successivement $\vec X=f(t)\vec V_i$.

- **$i=1$ :** $(f\vec V_1)''+W(f\vec V_1)=f''\vec V_1=\vec0$, donc $f''=0$. Le manuscrit note ce coefficient modal $\delta_1=0$.
- **$i=2$ :** $f''\vec V_2+\lambda_1f\vec V_2=\vec0$, donc $f''+\lambda_1f=0$, avec $\delta_2=\lambda_1$ dans cette partie du manuscrit.
- **$i=3$ :** $f''\vec V_3+\lambda_3f\vec V_3=\vec0$, donc $f''+\lambda_3f=0$, avec $\delta_3=\lambda_3$.

### c) Solution générale

$$
\vec X(t)=(Ae^{\omega t}+Be^{-\omega t})\vec V_2
+(Dt+E)\vec V_1
+(Fe^{i\omega t}+Ge^{-i\omega t})\vec V_3.
$$

### d) Conditions initiales

$$
\vec X(0)=\frac{\vec V_3-\vec V_2}{2},
\qquad\dot{\vec X}(0)=\vec0.
$$

La première condition donne

$$
(A+B)\vec V_2+E\vec V_1+(F+G)\vec V_3
=\frac12(\vec V_3-\vec V_2),
$$

soit

$$
A+B=-\frac12,\qquad E=0,\qquad F+G=\frac12.
$$

La seconde donne

$$
\omega(A-B)\vec V_2+D\vec V_1+i\omega(F-G)\vec V_3=\vec0,
$$

soit $A=B$, $D=0$, $F=G$. Finalement,

$$
\vec X(t)=\frac14\left[-(e^{\omega t}+e^{-\omega t})\vec V_2
+(e^{i\omega t}+e^{-i\omega t})\vec V_3\right].
$$
