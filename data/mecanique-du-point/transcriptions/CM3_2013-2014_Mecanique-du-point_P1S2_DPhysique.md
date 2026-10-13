# Mécanique du point — Résumé 3 : cinématique

> Source : `PREING1-S2/Mecanique-du-point/CM3_2013-2014_Mecanique-du-point_P1S2_DPhysique.pdf`, 2 pages, numérotées 4–5 dans le cours.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif, restitution des formules et description du schéma. Les précisions ajoutées sont distinguées du texte du cours.

## Position, déplacement, vitesse et accélération (page 1)

La cinématique étudie le mouvement d’un corps indépendamment de ses causes.

Vecteur position : $\vec r(t)=\overrightarrow{OM}(t)$.

Vecteur déplacement pendant $\Delta t$ :

$$\Delta\overrightarrow{OM}=\overrightarrow{OM}(t+\Delta t)-\overrightarrow{OM}(t).$$

Vitesse moyenne et vitesse instantanée :

$$\vec v_{\mathrm{moy}}(t)=\frac{\Delta\overrightarrow{OM}}{\Delta t},\qquad\vec v(t)=\frac{d\overrightarrow{OM}(t)}{dt}.$$

Le vecteur vitesse est tangent à la trajectoire et dirigé dans le sens du déplacement.

Accélération moyenne et accélération instantanée :

$$\vec a_{\mathrm{moy}}(t)=\frac{\Delta\vec v(t)}{\Delta t},\qquad\vec a(t)=\frac{d\vec v(t)}{dt}=\frac{d^2\overrightarrow{OM}(t)}{dt^2}.$$

## Coordonnées cartésiennes (page 1)

$$\overrightarrow{OM}(t)=x(t)\vec u_x+y(t)\vec u_y+z(t)\vec u_z.$$

$$\vec v(t)=\frac{dx}{dt}\vec u_x+\frac{dy}{dt}\vec u_y+\frac{dz}{dt}\vec u_z=\dot x\vec u_x+\dot y\vec u_y+\dot z\vec u_z.$$

$$\vec a(t)=\frac{d^2x}{dt^2}\vec u_x+\frac{d^2y}{dt^2}\vec u_y+\frac{d^2z}{dt^2}\vec u_z=\ddot x\vec u_x+\ddot y\vec u_y+\ddot z\vec u_z.$$

## Observation d’un mouvement (page 1)

Les équations horaires donnent $x(t),y(t),z(t)$. La trajectoire est l’ensemble des positions successives du point $M$ ; on l’obtient en éliminant $t$. Le document indique une écriture $f(x,y,z)=0$.

**Précision.** Pour une courbe dans l’espace, il peut être nécessaire de donner plusieurs relations cartésiennes : une seule équation régulière décrit généralement une surface.

Le mouvement, donc $\overrightarrow{OM}(t)$, $\vec v(t)$ et $\vec a(t)$, dépend du référentiel d’observation.

## Mouvements particuliers (pages 1–2)

- Mouvement uniforme si et seulement si $\|\vec v(t)\|$ est constante.
- Mouvement accéléré si la norme de la vitesse croît avec $t$.
- Mouvement freiné si la norme de la vitesse décroît avec $t$.
- Mouvement rectiligne uniforme si $\vec v(t)$ est un vecteur constant.
- Mouvement uniformément accéléré, au sens employé ici, si $\vec a(t)$ est un vecteur constant non nul.

Un mouvement à accélération constante n’est pas forcément rectiligne : si la vitesse initiale n’est pas alignée avec l’accélération, la trajectoire est une parabole.

## Chute libre (page 2)

La chute libre est le mouvement d’une masse $m$ soumise uniquement à son poids $m\vec g$. Dans le champ constant considéré :

$$\vec a(t)=\vec g=\text{vecteur constant}.$$

Au sommet d’un tir parabolique, seule la composante verticale de la vitesse est nulle ; la vitesse totale n’est pas nulle. Juste avant de toucher le sol, la vitesse d’un corps en chute libre n’est pas nulle ; le document la décrit comme maximale.

**Précisions.** La remarque sur le sommet concerne un tir avec composante horizontale non nulle. La vitesse maximale à l’arrivée suppose que le sol est le point le plus bas de la portion de trajectoire étudiée.

## Mouvement circulaire uniforme (page 2)

La position sur le cercle est repérée par $\theta(t)$. La vitesse angulaire est :

$$\omega(t)=\frac{d\theta(t)}{dt}=\dot\theta(t).$$

Le mouvement circulaire est uniforme lorsque $\omega$ est constante. Dans la base polaire $\{\vec u_r,\vec u_\theta\}$ :

$$\overrightarrow{OM}=R\vec u_r,\qquad\vec v=R\omega\vec u_\theta,\qquad\vec a=-R\omega^2\vec u_r=-\frac{v^2}{R}\vec u_r.$$

Le schéma représente un cercle de centre $O$, le rayon faisant l’angle $\theta(t)$ avec l’horizontale, $\vec u_r$ vers l’extérieur, $\vec u_\theta$ et $\vec v$ tangents dans le sens de rotation, et $\vec a$ dirigé vers $O$.

L’accélération est centripète. Bien que la norme de la vitesse soit constante, le vecteur vitesse varie : l’accélération n’est pas nulle.

## Mouvement relatif : translation rectiligne uniforme (page 2)

Un référentiel est un repère muni d’une horloge. $\mathcal R'$ est en translation rectiligne uniforme dans $\mathcal R$ lorsque ses vecteurs de base gardent des directions fixes par rapport à ceux de $\mathcal R$ et que son origine $O'$ se déplace à vitesse vectorielle constante $\vec v$ dans $\mathcal R$.

Si $\mathcal R$ est galiléen et $\mathcal R'$ en translation rectiligne uniforme à vitesse $\vec v$, alors :

$$\overrightarrow{OM}=\overrightarrow{OO'}+\overrightarrow{O'M},$$

$$\vec v_{\mathcal R}(M)=\vec v+\vec v_{\mathcal R'}(M),\qquad\vec a_{\mathcal R}(M)=\vec a_{\mathcal R'}(M).$$
