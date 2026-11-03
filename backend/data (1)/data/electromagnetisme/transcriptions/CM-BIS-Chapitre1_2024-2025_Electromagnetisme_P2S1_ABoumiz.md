---
source: "PREING2-S1/Electromagnetisme/CM-BIS-Chapitre1_2024-2025_Electromagnetisme_P2S1_ABoumiz.pdf"
pages: 35
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Chapitre 1 bis — Magnétostatique — Abdelaziz Boumiz (2024–2025)

## Page 1

Chapitre 1 bis — Magnétostatique. CY Tech. Support classé sous Abdelaziz Boumiz dans le nom du fichier.

## Page 2

### I. Symétries des distributions de courants — 1. Symétrie plane

Deux boucles symétriques par rapport au plan $(x,y)$, d'axe commun $(Oz)$, portent des courants images l'un de l'autre : $\vec j'(M')=S(\vec j(M))$. Les flèches tangentes aux boucles et les vecteurs $\vec j,\vec j'$ illustrent le plan de symétrie.

## Page 3

### 2. Antisymétrie plane

Une boucle centrée en $O$ est partagée par un plan passant par son diamètre : les courants aux points images sont opposés aux images géométriques,

$$\vec j'(M')=-S(\vec j(M)).$$

La figure indique le plan d'antisymétrie et les vecteurs tangents de part et d'autre.

## Page 4

### 3. Invariance par translation

Cylindre parcouru par un courant axial. Invariance suivant $(Oz)$ : $\vec j(x,y,z)=\vec j(x,y)$.

## Page 5

### 4. Invariance par rotation autour de $(Oz)$

Dans l'exemple du cylindre à courant axial : $\vec j(r,\theta,z)=j(r)\vec e_z$. La figure montre le courant parallèle à l'axe.

## Page 6

### II. Loi de Biot et Savart — 1. Vecteur élément de courant

Pour un circuit filiforme, $d\vec C=I\,d\vec\ell$. Le dessin oriente $\vec j$ et $d\vec\ell$ le long du fil, dans le sens du courant.

## Page 7

### 2. Loi de Biot et Savart

Fil parcouru par $I$, élément $d\vec C=I\,d\vec\ell$ en $P$, point $M$ à distance $r$ :

$$d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec\ell\wedge\vec u}{r^2}.$$

$\vec u$ est orienté de $P$ vers $M$ ; le dessin montre le fil courbe et la direction de $d\vec\ell$.

## Page 8

### Cas d'une distribution surfacique de courant

La page ne contient que ce titre ; aucune formule n'y est renseignée.

## Page 9

Champ total :

$$\vec B(M)=\frac{\mu_0}{4\pi}\int\frac{I\,d\vec\ell\wedge\vec u}{r^2}.$$

Unité de $B$ : tesla (T).

## Page 10

### III. Propriétés de symétrie du champ magnétostatique — 1. Symétrie plane

Le champ magnétostatique est perpendiculaire au plan de symétrie de la distribution de courant en chacun des points de ce plan.

## Page 11

### 2. Antisymétrie plane

Le champ magnétostatique est contenu dans le plan d'antisymétrie des courants en chacun des points de ce plan.

## Page 12

### IV. Calcul du champ magnétique — 1. Spire circulaire

Une spire de rayon $R$ est parcourue par $I$.

1. Établir l'orientation du champ en tout point de son axe à partir des symétries.
2. Exprimer ce champ à partir de la loi de Biot et Savart.

Aucune correction de ces deux questions ne figure sur cette page.

## Page 13

### 2. Champ créé par un segment

Segment $AB$, longueur $L$, courant $I$ : établir le champ en $M$ à distance $d$ du fil (notée $a$ sur les figures).

$$d\ell=dz,\qquad d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec\ell\wedge\vec u}{r^2}.$$

Le fil est vertical, le courant de $A$ vers $B$, $P$ est le point source. $r=PM$, $\vec u$ va de $P$ à $M$ ; le champ entre dans la feuille.

## Page 14

$$dB=\frac{\mu_0}{4\pi}\frac{I\,d\ell\sin\alpha}{r^2}.$$

Schéma : $\alpha$ angle entre le fil et $PM$ ; $\theta$ repère $P$ depuis $M$, relativement à la perpendiculaire au fil de longueur $a$. Les extrémités $A,B$ correspondent aux angles $\theta_1,\theta_2$.

## Page 15

$$\tan\theta=\frac za\quad\Longrightarrow\quad dz=\frac{a\,d\theta}{\cos^2\theta},\qquad
 dB=\frac{\mu_0I}{4\pi a}\cos\theta\,d\theta.$$

## Page 16

$$B=\frac{\mu_0I}{4\pi a}\int_{\theta_1}^{\theta_2}\cos\theta\,d\theta=\frac{\mu_0I}{4\pi a}(\sin\theta_2-\sin\theta_1).$$

## Page 17

Pour un fil rectiligne infiniment long : $\theta_1=-\pi/2$ et $\theta_2=\pi/2$.

## Page 18

### V. Théorème d'Ampère — 1. Énoncé

La circulation du champ magnétique le long d'un contour fermé est égale à la somme algébrique des courants enlacés multipliée par $\mu_0$ :

$$\oint_C\vec B\cdot d\vec\ell=\mu_0\sum I_{\rm enlacés}.$$

## Page 19

### 2. Champ créé par un fil infini

Fil rectiligne de longueur infinie, parcouru par un courant constant $I$, axe $(Oz)$. Contour d'Ampère : cercle de rayon $r$ centré en $O$, passant par $M$. $\vec B$ appartient au plan d'antisymétrie et est perpendiculaire au plan de symétrie.

## Page 20

Tout plan perpendiculaire au fil est un plan d'antisymétrie. Tout plan contenant le fil est un plan de symétrie. Le champ est tangentiel :

$$\vec B=B(r)\vec e_\theta.$$

## Page 21

$$\oint_C\vec B\cdot d\vec\ell=\mu_0I=B\oint_Cd\ell=B,2\pi r.$$

Donc $B(r)=\mu_0I/(2\pi r)$ et

$$\vec B(r)=\frac{\mu_0I}{2\pi r}\vec e_\theta.$$

## Page 22

### 3. Application 1 — sphère en rotation

Une sphère creuse de rayon $a$, chargée avec une densité surfacique uniforme $\sigma$, tourne autour d'un diamètre à vitesse angulaire $\omega$. Exprimer le champ magnétique au centre de la sphère.

## Page 23

### Correction — géométrie

La sphère de centre $O$ tourne autour de $(Oz)$. Une bande élémentaire à l'angle polaire $\theta$ forme une spire de rayon $r$, de largeur méridienne $dy$. Le schéma repère $r$, $dy$, $\theta$ et le sens de $\omega$.

## Page 24

Le champ sur l'axe d'une spire de rayon $r$ parcourue par $i$ est

$$b=\frac{\mu_0i}{2r}\sin^3\theta.$$

La vitesse des charges est $v=r\omega$ ; leur déplacement pendant $dt$ est $d\ell=r\omega\,dt$.

## Page 25

Charge élémentaire : $dq=r\omega\sigma\,dy\,dt$. Courant de la bande : $dI=dq/dt=r\omega\sigma\,dy$.

$$dB=\frac{\mu_0dI}{2r}\sin^3\theta=\frac{\mu_0\omega r\sigma\,dy}{2r}\sin^3\theta.$$

## Page 26

Avec $dy=a\,d\theta$ :

$$dB=\frac{\mu_0\omega a\sigma}{2}\sin^3\theta\,d\theta,\qquad
B=\frac{\mu_0\omega a\sigma}{2}\int_0^\pi\sin^3\theta\,d\theta.$$

## Page 27

Le support imprime

$$\int_0^\pi\sin^3\theta\,d\theta=\frac34\cos\theta-\frac1{12}\cos(3\theta),$$

puis donne le résultat :

$$B=\frac{2\mu_0\omega a\sigma}{3}.$$

> La première ligne confond intégrale définie et primitive, avec des signes inversés. Une primitive correcte est $-3\cos\theta/4+\cos(3\theta)/12$ ; l'intégrale entre $0$ et $\pi$ vaut $4/3$, ce qui confirme le résultat final.

## Page 28

### 4. Application 2 — champ créé par un électron

Exprimer le champ magnétique créé par un électron décrivant un cercle de rayon $a$ autour d'un proton, au point où se trouve le proton.

## Page 29

Le dessin montre l'électron sur le cercle de centre $O$, sa vitesse tangentielle $\vec V$ et le rayon $a$.

Élément de courant :

$$i\,d\vec\ell=\frac{dq}{dt}d\vec\ell=dq\,\vec V=-e\vec V.$$

## Page 30

$$\vec B=-\frac{\mu_0}{4\pi}e\vec V\wedge\frac{\vec u}{r^2},\qquad r=a.$$

Mouvement circulaire : accélération $\gamma=V^2/a$. Relation fondamentale de la dynamique :

$$\frac{mV^2}{a}=\frac1{4\pi\varepsilon_0}\frac{e^2}{a^2}.$$

## Page 31

$$V^2=\frac1{4\pi\varepsilon_0m}\frac{e^2}{a},$$

$$B^2=\left(\frac{\mu_0}{4\pi}\right)^2e^2\left(\frac{e^2}{4\pi\varepsilon_0am}\right)\frac1{a^4},$$

$$B=\left(\frac{\mu_0}{4\pi}\right)^{3/2}\frac{e^2c}{\sqrt{ma^5}}.$$

La dernière ligne emploie $c$ (noté C dans le support), vitesse de la lumière, avec $\varepsilon_0\mu_0c^2=1$.

## Page 32

### 5. Application 3 — bobines de Helmholtz

Deux bobines plates de $N$ spires, rayon $R$, courant $I$, ont leurs centres distants de $R$. Le sens du courant est tel que leurs champs s'ajoutent entre les bobines.

1. Exprimer le champ au milieu $O$ de leurs centres.
2. Exprimer le champ en un point $M$ voisin de $O$.

## Page 33

Schéma : bobines coaxiales (1) et (2), centres $O_1,O_2$, séparation $R$, milieu $O$. Les courants $I_1,I_2$ sont orientés pour que les champs s'ajoutent.

## Page 34

Bobine de très faible largeur : les champs de ses $N$ spires s'ajoutent. Pour une spire sur son axe :

$$b=\frac{\mu_0I}{2R}\sin^3\theta.$$

Champ total au milieu $O$ des deux bobines :

$$B=2\frac{\mu_0NI}{2R}\sin^3\theta.$$

Le calcul s'arrête à cette expression. La deuxième question, au voisinage de $O$, n'est pas développée dans ce PDF.

## Page 35

Page blanche, portant uniquement le numéro 35.
