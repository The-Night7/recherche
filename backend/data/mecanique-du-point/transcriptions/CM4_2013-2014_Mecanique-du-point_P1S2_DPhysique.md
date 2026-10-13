# Mécanique du point — Résumé 4 : dynamique

> Source : `PREING1-S2/Mecanique-du-point/CM4_2013-2014_Mecanique-du-point_P1S2_DPhysique.pdf`, 3 pages, numérotées 6–8 dans le cours.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif, restitution des formules et description des schémas. Les précisions ou erreurs de source sont signalées séparément.

La dynamique étudie le mouvement d’un corps en relation avec ses causes : les forces.

## Lois de Newton (page 1)

1. **Première loi.** Un point matériel soumis à aucune force a une vitesse vectorielle constante : il est au repos ou en mouvement rectiligne uniforme.
2. **Deuxième loi.** $\sum\vec F=m\vec a$, où $\sum\vec F$ est la résultante des forces agissant sur la masse $m$.
3. **Troisième loi.** $\vec F_{1\to2}=-\vec F_{2\to1}$. La première force est exercée par le corps 1 sur le corps 2, la seconde par 2 sur 1. Le document les décrit comme colinéaires à la droite reliant les deux corps ; elles forment un couple action–réaction.

Ces lois sont présentées comme des postulats confirmés par l’expérience pour les corps macroscopiques usuels. Les deux forces d’action–réaction s’exercent sur deux corps distincts : la réaction normale $\vec N$ d’un support et le poids $m\vec g$, appliqués au même corps, ne forment pas un tel couple.

Avant d’appliquer ces lois, préciser le système et dessiner le bilan des forces qui s’exercent sur lui.

## Définitions et référentiels (page 1)

Un corps est au repos, ou à l’équilibre dans le vocabulaire du document, lorsque $\overrightarrow{OM}(t)$ est constant ; alors $\sum\vec F=\vec0$.

La source appelle « isolé » un système pour lequel $\sum\vec F=\vec0$. Il peut être en mouvement rectiligne uniforme et n’est donc pas nécessairement au repos. **Précision terminologique :** des forces extérieures qui se compensent correspondent à un système pseudo-isolé ; un système isolé ne subit aucune force extérieure.

Un référentiel est un repère muni d’une horloge. Un référentiel galiléen, ou inertiel, est un référentiel dans lequel les lois de Newton s’appliquent. Tout référentiel en translation rectiligne uniforme par rapport à un référentiel galiléen est galiléen.

Le référentiel terrestre peut être considéré comme galiléen pour la plupart des expériences de laboratoire envisagées dans le cours. Les référentiels non galiléens sont annoncés pour le deuxième semestre.

## Attraction gravitationnelle (page 2)

La force exercée par la masse $m_1$ sur la masse $m_2$ est :

$$\vec F_{1\to2}=-G\frac{m_1m_2}{r^2}\vec u_{1\to2}.$$

$G=6,67\times10^{-11}$ en unités SI est la valeur de la constante de gravitation donnée dans le document ; $r$ sépare les deux masses et $\vec u_{1\to2}$ est unitaire, dirigé de $m_1$ vers $m_2$. La force est attractive. Le schéma montre les deux masses sur une droite, le vecteur unitaire de 1 vers 2 et la force appliquée en 2 vers 1.

## Poids (page 2)

Une masse $m$ proche de la Terre est soumise à son poids $\vec P=m\vec g$. En première approximation, il correspond à l’attraction gravitationnelle terrestre près du sol :

$$g\simeq G\frac{M_T}{R_T^2}\simeq9,8\ \mathrm{m\,s^{-2}}.$$

$g$ est l’accélération de pesanteur terrestre.

## Tension d’une corde (page 2)

Une corde tendue exerce sur ses extrémités une force de rappel $\vec T$ colinéaire à la corde : la tension.

- Une corde idéale est inextensible et de masse négligeable.
- Une poulie idéale est de masse négligeable et tourne sans frottement.
- Pour une corde idéale passant éventuellement sur une poulie idéale, $\|\vec T_1\|=\|\vec T_2\|$.

Le cours avertit que les vecteurs ne sont pas nécessairement opposés lorsqu’une poulie change la direction de la corde : l’égalité des modules ne permet pas d’écrire en général $\vec T_1=-\vec T_2$.

## Contact solide–solide : lois de Coulomb (pages 2–3)

La force du support se décompose en :

$$\vec F_{\mathrm{support}}=\vec N+\vec f,$$

où $\vec N$ est perpendiculaire au support et $\vec f$, force de frottement, lui est parallèle. Le schéma sur un plan incliné représente ces deux composantes et leur somme par un parallélogramme.

Le document repère la rupture du contact par $\vec N=\vec0$ ; c’est la condition limite d’annulation de la réaction normale.

### Frottement statique

En l’absence de glissement, le frottement est statique, noté $\vec f_s$. La condition de non-glissement est :

$$\|\vec f_s\|\leq\mu_s\|\vec N\|,$$

où $\mu_s$ est le coefficient de frottement statique. La direction de $\vec f_s$ n’est pas connue a priori ; elle appartient au plan tangent au contact. Le cours indique qu’on la détermine par $\sum\vec F=\vec0$.

**Précision.** Cette dernière équation correspond à un équilibre ou à une accélération nulle. Dans un mouvement sans glissement mais accéléré, il faut utiliser $\sum\vec F=m\vec a$.

### Frottement dynamique

En cas de glissement, le frottement dynamique $\vec f_d$ vérifie :

$$\|\vec f_d\|=\mu_d\|\vec N\|.$$

Il s’oppose au glissement du corps sur le support. Le coefficient dynamique est $\mu_d$ ; la phrase explicative du PDF écrit par erreur $\mu_s$.

Les coefficients $\mu_s,\mu_d$ dépendent des matériaux en contact, sont sans dimension et vérifient en général $\mu_s>\mu_d$. Ne pas confondre l’égalité des normes avec une égalité vectorielle : $\vec f_d\neq\mu_d\vec N$, car $\vec f_d\perp\vec N$.

## Frottement fluide (page 3)

Un corps en mouvement dans un fluide subit une force opposée à sa vitesse relative au fluide $\vec v$.

- Aux faibles vitesses : $\vec f=-k\vec v$.
- Aux grandes vitesses, dans le modèle donné : $\vec f=-k'\|\vec v\|\vec v$.

$k$ et $k'$ sont les coefficients de frottement fluide. Pour une chute dans un fluide, une vitesse limite est atteinte lorsque :

$$\vec f+m\vec g+\vec P_A=\vec0,$$

où $\vec P_A$ est la poussée d’Archimède.

## Rappel élastique (page 3)

Un ressort idéal de longueur $\ell$ exerce à son extrémité la force donnée par la loi de Hooke :

$$\vec F=-k(\ell-\ell_0)\vec u.$$

$k$ est la raideur, ou constante de rappel ; $\ell_0$ la longueur à vide ; $\vec u$ un vecteur unitaire orienté du ressort vers le point considéré. Cette force s’oppose à la déformation. $\ell-\ell_0$ représente la compression ou l’étirement.

Le schéma montre un ressort fixé à gauche, comprimé ($\ell<\ell_0$), avec $\vec u$ et la force à l’extrémité droite dirigés vers la droite.
