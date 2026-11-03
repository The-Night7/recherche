---
source: "PREING2-S1/Electromagnetisme/TD7-Correction_2024-2025_Electromagnetisme_P2S1_EDupont.pdf"
pages: 11
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des onze pages ; dérivations en coordonnées cylindriques et sphériques vérifiées ; erreurs de champ extérieur et de bilan énergétique explicitement signalées
---

# TD 7 — Équations de Maxwell — correction 2024–2025

## Page 1

### Conséquences des équations de Maxwell — Exercice 1 : équations de Poisson

Établir les équations de Poisson vues en cours :

$$\Delta V+\frac\rho{\varepsilon_0}=0,\qquad
\Delta\vec A+\mu_0\vec j=\vec0.$$

Rappels :

$$\Delta V=\operatorname{div}(\operatorname{grad}V),\qquad
\Delta\vec A=\begin{pmatrix}\Delta A_x\\\Delta A_y\\\Delta A_z\end{pmatrix}.$$

Les quatre équations de Maxwell sont rappelées :

$$\operatorname{div}\vec E=\frac\rho{\varepsilon_0}\tag{1}$$

$$\operatorname{div}\vec B=0\tag{2}$$

$$\operatorname{rot}\vec E=-\frac{\partial\vec B}{\partial t}\tag{3}$$

$$\operatorname{rot}\vec B=\mu_0\vec j+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}.\tag{4}$$

Elles couplent les champs $\vec E$ et $\vec B$. La densité de charge est une source du champ électrique ; le courant intervient dans les sources du champ magnétique.

En électrostatique, $\vec E=-\operatorname{grad}V$. L’équation (1) devient

$$\operatorname{div}\vec E
=\operatorname{div}(-\operatorname{grad}V)
=-\operatorname{div}(\operatorname{grad}V)
=-\Delta V=\frac\rho{\varepsilon_0}.$$

La page renvoie au résumé d’analyse vectorielle reproduit ensuite.

## Page 2

### Identités de calcul vectoriel

$$\begin{aligned}
\operatorname{rot}(\operatorname{grad}V)&=\vec0,\\
\operatorname{div}(\operatorname{rot}\vec A)&=0,\\
\operatorname{div}(\operatorname{grad}V)&=\Delta V,\\
\operatorname{rot}(\operatorname{rot}\vec A)&=
\operatorname{grad}(\operatorname{div}\vec A)-\Delta\vec A,\\
\operatorname{grad}(V_1V_2)&=V_1\operatorname{grad}V_2+V_2\operatorname{grad}V_1,\\
\operatorname{rot}(V\vec A)&=V\operatorname{rot}\vec A+\operatorname{grad}V\wedge\vec A,\\
\operatorname{div}(V\vec A)&=V\operatorname{div}\vec A+\operatorname{grad}V\cdot\vec A,\\
\operatorname{div}(\vec A_1\wedge\vec A_2)&=
\vec A_2\cdot\operatorname{rot}\vec A_1-\vec A_1\cdot\operatorname{rot}\vec A_2.
\end{aligned}$$

La première équation de Poisson est donc

$$\boxed{\Delta V+\frac\rho{\varepsilon_0}=0}.$$

On introduit le potentiel vecteur par $\vec B=\operatorname{rot}\vec A$. Maxwell-Ampère donne

$$\operatorname{rot}\vec B=\mu_0\left(\vec j+\varepsilon_0\frac{\partial\vec E}{\partial t}\right).$$

En statique, $\partial\vec E/\partial t=\vec0$. Ainsi

$$\operatorname{rot}(\operatorname{rot}\vec A)
=\operatorname{grad}(\operatorname{div}\vec A)-\Delta\vec A
=\mu_0\vec j.$$

Avec la jauge de Coulomb,

$$\operatorname{div}\vec A=0,$$

on obtient

$$\boxed{\Delta\vec A+\mu_0\vec j=\vec0}.$$

### Exercice 2 — Cylindre parcouru par un courant

En utilisant les équations locales de Maxwell, déterminer le champ magnétique créé par un cylindre plein, infiniment long, de rayon $R$, parcouru par un courant uniforme $I$ suivant sa longueur.

Le dessin oriente le cylindre selon $Oz$, avec le courant vers le haut. On choisit les coordonnées cylindriques $(O,\vec u_r,\vec u_\theta,\vec u_z)$. Le courant est constant ; le calcul est placé dans le régime statique ou dans l’ARQS pour Maxwell-Ampère. Sur une section droite $S=\pi R^2$,

$$I=\iint_S\vec j\cdot\mathrm d\vec S=\Phi(\vec j).$$

## Page 3

### Courant uniforme, invariances et équation locale

Le courant est uniformément réparti :

$$I=jS=j\pi R^2,\qquad
\vec j=\frac I{\pi R^2}\vec u_z.$$

La densité $\vec j$ est indépendante de $r$, $\theta$ et $z$ à l’intérieur.

1. **Invariances.** Le cylindre infini donne l’indépendance en $z$ ; l’invariance par rotation donne l’indépendance en $\theta$.

Le manuscrit rappelle

$$\operatorname{rot}\vec B=\underbrace{\mu_0\vec j}_{\text{source 1}}
+\underbrace{\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}}_{\text{source 2}}.$$

Il indique que, pour certaines échelles de temps, la source 2 est négligeable devant la source 1, et rappelle $\mu_0\varepsilon_0c^2=1$. L’équation de Faraday conserve le terme $-\partial\vec B/\partial t$ dans l’ARQS ; dans le cas stationnaire de cet exercice, ce terme est nul.

> Erreur dans le rapport manuscrit : la ligne étiquetée « source 2 / source 1 » écrit $\|\vec j\|/(\varepsilon_0\|\partial\vec E/\partial t\|)\ll1$. Le rapport correspondant au texte est l’inverse : $\varepsilon_0\|\partial\vec E/\partial t\|/\|\vec j\|\ll1$.

2. **Symétries.** $\Pi^*=(M,\vec u_r,\vec u_\theta)$ est un plan d’antisymétrie des courants ; $\Pi=(M,\vec u_r,\vec u_z)$ est un plan de symétrie. Donc $\vec B\in\Pi^*$ et $\vec B\perp\Pi$, d’où

$$\vec B=B(r)\vec u_\theta.$$

3. **Équation locale de Maxwell-Ampère.**

$$\operatorname{rot}\vec B=\mu_0\vec j.$$

Pour mémoire, le rotationnel d’un champ en coordonnées cylindriques est

$$
\operatorname{rot}\vec A=
\left(\frac1r\frac{\partial A_z}{\partial\theta}-\frac{\partial A_\theta}{\partial z}\right)\vec u_r
+\left(\frac{\partial A_r}{\partial z}-\frac{\partial A_z}{\partial r}\right)\vec u_\theta
+\frac1r\left(\frac{\partial(rA_\theta)}{\partial r}-\frac{\partial A_r}{\partial\theta}\right)\vec u_z.
$$

Ici, $B_r=B_z=0$ et les dérivées en $\theta$ et $z$ s’annulent. Pour $r\leq R$,

$$\operatorname{rot}\vec B=\frac1r\frac{\mathrm d}{\mathrm dr}(rB(r))\vec u_z
=\frac{\mu_0I}{\pi R^2}\vec u_z,$$

soit

$$\frac{\mathrm d}{\mathrm dr}(rB(r))=\frac{\mu_0I}{\pi R^2}r.$$

## Page 4

### Champ à l’intérieur et à l’extérieur du cylindre

L’intégration donne

$$rB(r)=\frac{\mu_0I}{2\pi R^2}r^2+A,\qquad
B(r)=\frac{\mu_0I}{2\pi R^2}r+\frac Ar.$$

Un champ divergent en $r=0$ est exclu pour cette distribution volumique ; $A=0$. Donc

$$\boxed{\vec B(r\leq R)=\frac{\mu_0I}{2\pi R^2}r\vec u_\theta}.$$

À l’extérieur, il n’y a pas de courant :

$$\operatorname{rot}\vec B=\vec0
\quad\Longrightarrow\quad
\frac1r\frac{\mathrm d}{\mathrm dr}(rB(r))=0.$$

Ainsi $rB(r)=A'$ et $B(r)=A'/r$. Le champ est continu en $r=R$, car le courant est volumique :

$$\frac{\mu_0I}{2\pi R}=\frac{A'}R
\quad\Longrightarrow\quad A'=\frac{\mu_0I}{2\pi}.$$

Donc

$$\boxed{\vec B(r\geq R)=\frac{\mu_0I}{2\pi r}\vec u_\theta}.$$

### Exercice 3 — Champ électrique

Dans le demi-espace vide $x>0$, il règne un champ électrique

$$\vec E(\vec r,t)=E_0\cos(\omega t-kz)\vec e_x,$$

en coordonnées cartésiennes, avec $\omega$ et $k$ deux constantes positives.

1. Calculer $\operatorname{div}\vec E$ et justifier le résultat.

$$\operatorname{div}\vec E=\vec\nabla\cdot\vec E
=\frac{\partial E(z,t)}{\partial x}=0.$$

C’est cohérent avec le vide sans charges : $\rho=0$.

2. Calculer $\operatorname{rot}\vec E$ et donner l’équation de Maxwell où cette quantité intervient.

$$\operatorname{rot}\vec E=\vec\nabla\wedge\vec E
=\begin{pmatrix}0\\\partial E(z,t)/\partial z\\-\partial E(z,t)/\partial y\end{pmatrix}
=\begin{pmatrix}0\\\partial E(z,t)/\partial z\\0\end{pmatrix}.$$

## Page 5

### Champ magnétique de l’onde

$$\operatorname{rot}\vec E
=kE_0\sin(\omega t-kz)\vec e_y.$$

3. Déterminer $\vec B(\vec r,t)$ en supposant qu’il n’a pas de terme constant.

L’équation de Maxwell-Faraday est

$$\operatorname{rot}\vec E=-\frac{\partial\vec B}{\partial t}.$$

Donc

$$\dot B_x=0,\qquad
\dot B_y=-kE_0\sin(\omega t-kz),\qquad
\dot B_z=0.$$

L’intégration temporelle est notée dans le manuscrit

$$B_x=A,\qquad B_y=\frac{kE_0}\omega\cos(\omega t-kz)+B,\qquad B_z=C.$$

Sans contribution indépendante du temps,

$$\boxed{\vec B=\frac{kE_0}\omega\cos(\omega t-kz)\vec e_y},\qquad
\boxed{\vec E=E_0\cos(\omega t-kz)\vec e_x}.$$

À $t$ fixé, le dessin représente les deux champs sinusoïdaux transversaux. Ils sont en phase, et

$$\frac{B_0}{E_0}=\frac k\omega>0,\qquad
\vec e_x\wedge\vec e_y=\vec e_z.$$

Le vecteur d’onde est $\vec k=k\vec e_z$, et

$$\vec E\wedge\vec B=\frac k\omega E_0^2\cos^2(\omega t-kz)\vec e_z.$$

Une note indique la vitesse de la lumière dans le vide, $v=c$.

4. Vérifier la divergence du champ magnétique.

$$\operatorname{div}\vec B
=\frac{\partial B_x}{\partial x}+\frac{\partial B_y}{\partial y}+\frac{\partial B_z}{\partial z}
=\frac{\partial B_y(z,t)}{\partial y}=0,$$

conformément à Maxwell-flux.

## Page 6

### Relation entre $\omega$ et $k$

5. Déterminer la relation entre $\omega$ et $k$ à l’aide d’une autre équation de Maxwell dans le vide.

Avec $\vec j=\vec0$, Maxwell-Ampère donne

$$\operatorname{rot}\vec B=\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}.$$

Comme $\vec B=B(z,t)\vec e_y$,

$$\operatorname{rot}\vec B
=\begin{pmatrix}-\partial B/\partial z\\0\\\partial B/\partial x\end{pmatrix}
=\begin{pmatrix}-\partial B/\partial z\\0\\0\end{pmatrix}.$$

Ainsi

$$-\frac{\partial B}{\partial z}=\mu_0\varepsilon_0\frac{\partial E}{\partial t}.$$

En remplaçant les champs,

$$
-\frac{k^2E_0}\omega\sin(\omega t-kz)
=-\mu_0\varepsilon_0\omega E_0\sin(\omega t-kz).
$$

On en déduit

$$\frac{k^2}\omega=\mu_0\varepsilon_0\omega,\qquad
k^2=\frac{\omega^2}{c^2}.$$

Puisque $k$ et $\omega$ sont positifs,

$$\boxed{k=\frac\omega c},\qquad\vec k=k\vec e_z.$$

La phase est sans dimension : $[kz]=[\omega t]=1$. Donc

$$[k]=L^{-1},\qquad k=\frac{2\pi}\lambda,$$

avec $\lambda$ la période spatiale ou longueur d’onde, et

$$[\omega]=T^{-1},\qquad\omega=\frac{2\pi}T,$$

avec $T$ la période temporelle.

La page annonce ensuite « Applications des équations de Maxwell ».

## Page 7

### Exercice 4 — Équation de Maxwell-Gauss

Une sphère creuse de rayon interne $R/2$ et de rayon externe $R$ porte une charge volumique de densité $\rho(r)$, de charge totale $Q$. Pour $R/2\leq r\leq R$, le champ électrostatique est

$$\vec E=k(\alpha r-R)\vec u_r,$$

où $\vec u_r$ est le vecteur unitaire radial en coordonnées sphériques. Le milieu est assimilable au vide.

1. Exprimer $\vec E(0)$.

La distribution est volumique : le champ est défini et continu. La distribution possède la symétrie sphérique ; elle ne varie pas lorsque $\theta$ ou $\varphi$ varie. La charge totale est $Q=\iiint\rho(r)\,\mathrm dV$.

Au centre, trois plans de symétrie indépendants imposent que $\vec E(0)$ appartienne à leur intersection. Donc

$$\boxed{\vec E(0)=\vec0}.$$

2. Établir $\vec E(r)$ pour $0\leq r\leq R/2$ à partir des équations locales de Maxwell ; en déduire $\alpha$.

Dans la cavité, $\rho=0$, donc $\operatorname{div}\vec E=0$. Les plans passant par $O$ et $M$ sont des plans de symétrie, donc $\vec E=E(r)\vec u_r$.

La divergence sphérique vaut

$$
\operatorname{div}\vec E
=\frac1{r^2}\frac{\partial(r^2E_r)}{\partial r}
+\frac1{r\sin\theta}\frac{\partial(\sin\theta E_\theta)}{\partial\theta}
+\frac1{r\sin\theta}\frac{\partial E_\varphi}{\partial\varphi}.
$$

Ici $E_\theta=E_\varphi=0$, d’où

$$\frac1{r^2}\frac{\mathrm d}{\mathrm dr}(r^2E(r))=0.$$

> Le manuscrit conclut directement « $E(r)=K$ ». L’intégration correcte est $r^2E(r)=K$, soit $E(r)=K/r^2$. La régularité au centre impose $K=0$, ce qui conserve le résultat final du corrigé.

$$\boxed{\vec E(r\leq R/2)=\vec0}.$$

Par continuité en $R/2$,

$$0=k\left(\alpha\frac R2-R\right),$$

d’où $\boxed{\alpha=2}$ pour le cas chargé non trivial.

## Page 8

### Densité de charge et constante $k$

3. Établir $\rho(r)$, calculer la charge totale et en déduire $k$.

Dans la couche chargée,

$$\operatorname{div}\vec E
=\frac1{r^2}\frac{\mathrm d}{\mathrm dr}\left[k(\alpha r^3-Rr^2)\right]
=\frac{\rho(r)}{\varepsilon_0}.$$

Donc, avec $\alpha=2$,

$$\boxed{\rho(r)=k\varepsilon_0\left(3\alpha-\frac{2R}r\right)
=2k\varepsilon_0\left(3-\frac Rr\right)}.$$

La charge est nulle dans la cavité. L’intégrale volumique donne

$$
Q=\int_{R/2}^R\rho(r)r^2\,\mathrm dr
\int_0^\pi\sin\theta\,\mathrm d\theta
\int_0^{2\pi}\mathrm d\varphi.
$$

Les intégrales angulaires valent $2$ et $2\pi$. Ainsi

$$
Q=8\pi k\varepsilon_0\int_{R/2}^R\left(3-\frac Rr\right)r^2\,\mathrm dr
=8\pi k\varepsilon_0\left[r^3-\frac{Rr^2}2\right]_{R/2}^R
=4\pi k\varepsilon_0R^3.
$$

D’où

$$\boxed{k=\frac Q{4\pi\varepsilon_0R^3}}.$$

4. À l’extérieur, les résultats sont-ils compatibles avec le théorème de Gauss ?

On a déjà

$$\vec E=\vec0\quad(r\leq R/2),\qquad
\vec E=\frac Q{4\pi\varepsilon_0R^3}(2r-R)\vec u_r
\quad(R/2\leq r\leq R).$$

À l’extérieur, $\operatorname{div}\vec E=0$ implique $r^2E(r)=K'$. La continuité en $R$ impose

$$\frac{K'}{R^2}=\frac Q{4\pi\varepsilon_0R^2},
\qquad K'=\frac Q{4\pi\varepsilon_0}.$$

## Page 9

### Vérification par Gauss

$$\vec E(r\geq R)=\frac Q{4\pi\varepsilon_0r^2}\vec u_r.$$

Pour une sphère $S$ de rayon $r\geq R$,

$$\oiint_S\vec E\cdot\mathrm d\vec S=\frac Q{\varepsilon_0}.$$

Le champ est radial et sa norme est constante sur $S$, donc

$$\Phi(\vec E)=E(r)\iint_S\mathrm dS=4\pi r^2E(r).$$

La surface se calcule par

$$\iint_S\mathrm dS=r^2\int_0^\pi\sin\theta\,\mathrm d\theta
\int_0^{2\pi}\mathrm d\varphi=4\pi r^2.$$

On retrouve donc $\vec E=Q\vec u_r/(4\pi\varepsilon_0r^2)$.

### Exercice 5 — Cylindre conducteur

Soit un cylindre conducteur de conductivité $\sigma$, de longueur $h$ considérée comme infinie, parcouru par un courant stationnaire uniformément réparti, dans la direction de son axe, d’intensité $I$. Le dessin précise le rayon $R$ et l’axe $Oz$.

1. Déterminer le champ électromagnétique en tout point de l’espace.

En reprenant l’exercice 2,

$$\vec B(r\leq R)=\frac{\mu_0jr}{2}\vec u_\theta
=\frac{\mu_0I}{2\pi R^2}r\vec u_\theta,$$

$$\vec B(r\geq R)=\frac{\mu_0jR^2}{2r}\vec u_\theta
=\frac{\mu_0I}{2\pi r}\vec u_\theta.$$

Dans le conducteur, la loi d’Ohm locale donne

$$\vec j=\frac I{\pi R^2}\vec u_z=\sigma\vec E,
\qquad\boxed{\vec E(r<R)=\frac I{\pi R^2\sigma}\vec u_z}.$$

Le manuscrit affirme aussi $\vec E(r\geq R)=\vec0$ au motif que $\vec j=\vec0$ à l’extérieur. Il ajoute : « $\vec B$ et $\vec E$ sont liés par les équations de Maxwell “sauf” en statique ».

> **Erreur du support :** l’absence de courant dans le vide extérieur ne permet pas d’y conclure que $\vec E=\vec0$ ; la loi d’Ohm du conducteur ne s’y applique pas. En régime stationnaire, la composante tangentielle du champ électrique est continue à la surface : juste à l’extérieur, elle doit correspondre au champ axial non nul intérieur. Les équations statiques pour $\vec E$ et $\vec B$ peuvent être résolues séparément lorsque leurs sources sont données ; cela ne dispense pas de respecter les conditions aux limites.

## Page 10

### Vecteur et flux de Poynting

2. En déduire le vecteur de Poynting en tout point et son flux à travers la surface cylindrique du conducteur. Commenter.

$$\vec\Pi=\frac{\vec E\wedge\vec B}{\mu_0}.$$

Le dessin rappelle les directions des trois vecteurs. À l’intérieur,

$$
\vec\Pi(r<R)=\frac1{\mu_0}
\left(\frac I{\pi R^2\sigma}\vec u_z\right)
\wedge
\left(\frac{\mu_0I}{2\pi R^2}r\vec u_\theta\right)
=-\frac{I^2}{(\pi R^2)^2\sigma}\frac r2\vec u_r,
$$

car $\vec u_z\wedge\vec u_\theta=-\vec u_r$.

La source conclut ensuite que $\vec\Pi(r\geq R)=\vec0$ à partir de son affirmation $\vec E=\vec0$ à l’extérieur.

> Cette conclusion extérieure reprend l’erreur signalée page 9. Le flux à la surface peut toutefois être calculé avec la limite intérieure du champ et la continuité des composantes tangentielles.

Pour la surface latérale orientée vers l’extérieur,

$$\mathrm d\vec S=r\,\mathrm d\theta\,\mathrm dz\vec u_r.$$

À rayon $r$ fixé et sur une longueur $h$,

$$
\Phi(\vec\Pi)=\iint_S\vec\Pi\cdot\mathrm d\vec S
=\int_{-h/2}^{h/2}\mathrm dz\int_0^{2\pi}\mathrm d\theta\,
 r\left(-\frac{I^2}{(\pi R^2)^2\sigma}\frac r2\right).
$$

Les facteurs sont indépendants de $z$ et $\theta$. À la surface $r=R$,

$$
\Phi(\vec\Pi)
=-\frac{I^2}{(\pi R^2)^2\sigma}\frac{R^2}2\times h\times2\pi
=\boxed{-\frac h{\sigma\pi R^2}I^2}.
$$

$h$ représente ici la longueur du tronçon considéré, dans le modèle où les effets de bord sont négligés.

## Page 11

### Interprétation énergétique

Rappel dessiné pour une résistance : $U=\mathcal RI$, et la puissance vaut

$$\mathcal P=UI=\mathcal RI^2.$$

Le manuscrit décrit $\Phi(\vec\Pi)$ comme la « puissance cédée par le conducteur à l’extérieur sous forme de puissance thermique », en indiquant son signe négatif. Le dessin montre les vecteurs de Poynting dirigés vers le conducteur, et $\mathrm d\vec S$ orienté vers l’extérieur.

> **Correction de l’interprétation :** avec cette normale sortante, le flux négatif représente une puissance électromagnétique **entrant** dans le conducteur. Elle est dissipée par effet Joule. En notant $\mathcal R=h/(\sigma\pi R^2)$ la résistance du tronçon, $-\Phi(\vec\Pi)=\mathcal RI^2$ est la puissance reçue et dissipée. Le vecteur de Poynting ne décrit pas ici un flux de chaleur sortant.

La suite de la page est blanche.
