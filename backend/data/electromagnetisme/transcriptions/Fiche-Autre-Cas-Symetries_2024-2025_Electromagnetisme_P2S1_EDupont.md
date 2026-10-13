---
source: "PREING2-S1/Electromagnetisme/Fiche-Autre-Cas-Symetries_2024-2025_Electromagnetisme_P2S1_EDupont.pdf"
pages: 3
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des trois pages manuscrites ; formules en LaTeX ; portée des conclusions de symétrie explicitée dans des notes distinctes
---

# Autres cas de symétrie — distributions de charges

## Page 1 — Rappels, cerceau et sphère uniforme

### Plans de symétrie et d’antisymétrie

Les deux petits schémas en haut de page représentent des distributions de charges de part et d’autre d’un plan.

- **Plan $\Pi$ de symétrie passant par $M$ :** $\vec E(M)\in\Pi$. Deux plans de symétrie passant par le point déterminent une direction commune de $\vec E$.
- **Plan $\Pi'$ d’antisymétrie :** $\vec E$ est dirigé suivant la normale à $\Pi'$ pour un point de ce plan.

Dans le premier schéma, les charges de part et d’autre du plan sont images par réflexion et gardent leur signe. Dans le second, les densités sont opposées, $\rho(\vec r)$ et $-\rho(\vec r)$.

### Cerceau chargé

**Énoncé.** Quelles sont les symétries de la distribution ci-contre ?

Le cerceau, centré en $O$, est dans le plan $(Oxy)$. Sa moitié droite porte une densité linéique $+\lambda$, sa moitié gauche une densité $-\lambda$. L’axe $Oz$ est perpendiculaire au plan du cerceau.

**Annotations — coordonnées cartésiennes.**

Plans de symétrie :

$$
P_1=(O,\vec e_x,\vec e_z),\qquad
P_2=(O,\vec e_x,\vec e_y).
$$

Donc $\vec E\in P_1$ et $\vec E\in P_2$ : $\vec E$ est suivant $\vec e_x$.

Plan d’antisymétrie :

$$
P'=(O,\vec e_y,\vec e_z).
$$

Donc $\vec E\perp P'$ : $\vec E$ est suivant $\vec e_x$.

> Portée des annotations : la conclusion obtenue simultanément avec les trois plans s’applique au centre $O$, représenté sur le dessin. La symétrie ne donne pas cette même direction en un point arbitraire de l’espace.

### Sphère uniformément chargée en surface

**Énoncé.** Soit une sphère de rayon $a$, de centre $O$, portant une répartition surfacique uniforme de charges $\sigma$. Quelles symétries peut-on attribuer à cette distribution de charges ?

0. $\vec E$ est défini et continu partout sauf lors de la traversée de la surface chargée.
1. Coordonnées sphériques : $(O,\vec e_r,\vec e_\theta,\vec e_\varphi)$ ; initialement $\vec E(r,\theta,\varphi)$.
2. **Invariances.** La distribution de charges est invariante par rotation de $\theta$ ou $\varphi$ (la note indique une rotation autour de l’axe $Oy$ ou $Oz$). Les dépendances angulaires sont barrées dans $\vec E(r,\theta,\varphi)$ : la composante radiale ne dépend que de $r$.
3. **Symétries.** Deux plans de symétrie passant par $M$ :

$$
P_1=(M,\vec e_r,\vec e_\varphi),\qquad
P_2=(M,\vec e_r,\vec e_\theta).
$$

Leur direction commune est $\vec e_r$. Comme $\vec E\in P_1$ et $\vec E\in P_2$,

$$
\boxed{\vec E(M)=E(r)\vec e_r},\qquad
\vec e_r=\frac{\overrightarrow{OM}}{\|\overrightarrow{OM}\|}
=\frac{\overrightarrow{OM}}r.
$$

La note de marge définit

$$
\sigma=\frac{\mathrm dq}{\mathrm dS},\qquad [\sigma]=\mathrm{C\,m^{-2}}.
$$

Un petit graphe oppose une densité uniforme $\sigma=\sigma_0$, constante, à une densité non uniforme. Remarque manuscrite : de très loin, une sphère chargée ressemble à une charge ponctuelle. Le dessin montre les directions radiales du champ autour d’une charge positive et la base sphérique au point $M$.

## Page 2 — Cylindre évidé et cube

### Cylindre

**Énoncé.** Un cylindre infini d’axe $(Oz)$, comportant une partie cylindrique évidée d’axe $(O'z)$, porte une charge volumique $\rho$ uniforme. Quelles symétries peut-on attribuer à cette distribution de charges ?

Le dessin place $O'$ sur l’axe $Ox$, à droite de $O$. La cavité est parallèle à $Oz$ et décentrée. Un point $M$, une base cylindrique et un angle $\theta$ sont ajoutés à la main.

**Superposition notée dans la marge :**

$$
\vec E=\vec E_{\text{sans trou}}+\vec E_{\text{cylindre du trou, densité }-\rho}.
$$

Deux plans de symétrie sont indiqués :

$$
P_1=(O,\vec u_x,\vec u_y)
\quad\text{(plan perpendiculaire à }Oz\text{)},
\qquad
P_2=(O,\vec u_x,\vec u_z).
$$

La conclusion manuscrite est

$$
\vec E\in P_1\cap P_2\quad\Longrightarrow\quad\vec E=E\vec u_x.
$$

> Précision de lecture : l’appartenance du champ à un plan de symétrie s’utilise en un point de ce plan. La conclusion écrite découle donc de ces deux plans à leur intersection ; elle ne démontre pas à elle seule une direction uniforme du champ dans tout l’espace. La superposition est indiquée, mais aucun calcul des champs cylindriques n’est développé sur la page.

### Cube

**Énoncé.** Soit un cube de centre $O$ avec deux faces chargées : $(+\sigma)$ sur $A'B'C'D'$ et $(-\sigma)$ sur $ABCD$. Quelles sont les symétries de cette distribution ?

Le dessin représente deux faces parallèles au plan $(Oyz)$, la face négative à gauche et la face positive à droite de $O$, suivant $Ox$.

Plan d’antisymétrie :

$$
\Pi'=(O,\vec e_z,\vec e_y).
$$

L’annotation en déduit

$$
\vec E\perp\Pi'\quad\Longrightarrow\quad\vec E=E\vec e_x.
$$

Plans de symétrie recensés :

$$
\begin{aligned}
P_1&=(O,\vec e_x,\vec e_z),\\
P_2&=(O,\vec e_x,\vec e_y),\\
P_3&=AA'C'C,\\
P_4&=BB'D'D.
\end{aligned}
$$

Les deux derniers sont les plans diagonaux du cube passant par $Ox$.

> La conclusion issue du plan d’antisymétrie s’applique aux points de ce plan, en particulier au centre $O$.

## Page 3 — Sphère à densité $\sigma_0\cos\theta$

**Énoncé.** Soit une sphère de rayon $a$, de centre $O$, portant une répartition surfacique de charges, en coordonnées sphériques,

$$
\sigma=\sigma_0\cos\theta.
$$

Le centre de la sphère est en $O$. Quelles symétries peut-on attribuer à cette distribution de charges ?

> Dans l’énoncé, le mot « uniforme » a été barré à la main.

**Annotations.**

$$
\sigma=\frac{\mathrm dq}{\mathrm dS}=\sigma_0\cos\theta,
\qquad [\sigma]=\mathrm{C\,m^{-2}}.
$$

Coordonnées sphériques : $(O,\vec u_r,\vec u_\theta,\vec u_\varphi)$.

Le dessin montre $\theta$ mesuré depuis $Oz$, le rayon $a$, et un plan équatorial $P'$. L’hémisphère supérieur porte des charges positives, l’inférieur des charges négatives. Le graphe $\sigma(\theta)$ part de $\sigma_0$ pour $\theta=0$, passe par zéro pour $\theta=\pi/2$ et atteint $-\sigma_0$ pour $\theta=\pi$.

La charge totale est écrite sous forme d’intégrale :

$$
Q=\iint_S\sigma\,\mathrm dS
=\int_{\theta=0}^{\pi}\int_{\varphi=0}^{2\pi}
\sigma\,\mathrm d\ell_\theta\,\mathrm d\ell_\varphi
=\int_0^\pi\int_0^{2\pi}
\sigma_0\cos\theta\,(r\,\mathrm d\theta)
(r\sin\theta\,\mathrm d\varphi).
$$

Les deux facteurs $r$ sont entourés en bleu dans la source ; sur la surface sphérique, $r=a$. Le calcul n’est pas poursuivi dans le document.

**Antisymétrie :** plan équatorial $\theta=\pi/2$.

**Symétrie :** tous les plans contenant l’axe $(Oz)$.
