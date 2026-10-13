---
source: "PREING2-S1/Electromagnetisme/CM-Chapitre4-Gauss_2023-2024_Electromagnetisme_P2S1_EDupont.pdf"
pages: 15
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des pages rendues et comparaison avec le texte natif ; formules restituées en LaTeX
---

# Électromagnétisme — Chapitre 4 : théorème de Gauss (2023-2024)

## Page 1

Électromagnétisme — Chapitre 4 — Théorème de Gauss.

Physique, 2023-2024. Présentation rédigée par Émilie Dupont (Cergy), emilie.dupont@cyu.fr, CY308. CY Tech, Cergy Paris Université.

**Schéma de couverture.** Un fil de densité linéique $\lambda$ traverse suivant son axe un cylindre de hauteur $h$ et de rayon $r$. Les bases sont $S_1$ et $S_2$, la surface latérale $S_3$. Les normales sortantes $\vec n_1$ et $\vec n_2$ sont axiales et opposées ; $\vec n_3$ est radiale. Le champ $\vec E$ est représenté radialement, notamment au point $M$ de la surface latérale.

## Page 2

### Programme d’électrostatique

1. Force entre deux charges.
2. Champ électrostatique.
3. Théorème de superposition et symétries.
4. Théorème de Gauss.
5. Potentiel électrostatique.
6. Conducteurs en équilibre électrostatique.

## Page 3

### 1.4.1. Flux du champ d’une charge à travers une surface

**Flux élémentaire.** Une surface élémentaire $dS$ est orientée par sa normale unitaire $\vec n$ :

$$d\vec S=\vec n\,dS.$$

Le flux élémentaire du champ $\vec E$ à travers $dS$ est défini par le produit scalaire

$$d\Phi=\vec E\cdot d\vec S=\vec E\cdot\vec n\,dS.$$

Unités : $dS$ en $\mathrm{m^2}$, $d\Phi$ en $\mathrm{V\,m}$ et $\vec E$ en $\mathrm{V\,m^{-1}}$.

**Figure.** La normale $d\vec S$ est perpendiculaire à la petite surface ; le vecteur champ est incliné par rapport à cette normale.

## Page 4

### Flux total à travers une surface

$$\Phi=\iint_S d\Phi
=\iint_S\vec E\cdot d\vec S
=\iint_S\vec E\cdot\vec n\,dS.$$

La figure rappelle $d\vec S=\vec n\,dS$ et l’inclinaison possible du champ par rapport à la normale.

## Page 5

### 1.4.2. Théorème de Gauss

Le flux $\Phi$ du champ $\vec E$ à travers une surface fermée $S$ est proportionnel à la charge $q_{\mathrm{int}}$ contenue dans le volume $V$ délimité par cette surface :

$$\boxed{\Phi=\oiint_S\vec E\cdot d\vec S=\frac{q_{\mathrm{int}}}{\varepsilon_0}.}$$

| Symbole | Grandeur | Unité indiquée |
| --- | --- | --- |
| $\Phi$ | Flux | $\mathrm{V\,m}$ |
| $q_{\mathrm{int}}$ | Charge intérieure | $\mathrm C$ |
| $\varepsilon_0$ | Permittivité absolue du vide | SI |

Les normales de la surface fermée sont orientées vers l’extérieur.

## Page 6

### 1.4.3. Distribution linéique uniformément chargée

La symétrie cylindrique et l’invariance par translation conduisent, en coordonnées cylindriques, à

$$\vec E(M)=E(r)\vec u_r.$$

**Schéma.** Un fil rectiligne infini de densité linéique uniforme $\lambda$ ; $M$ se trouve à distance $r$ du fil.

## Page 7

### Fil infini — application du théorème de Gauss

On choisit un cylindre fermé coaxial au fil, de rayon $r$ et de hauteur $h$. Il est constitué de la base supérieure $S_1$, de la base inférieure $S_2$ et de la surface latérale $S_3$. Les normales sortantes des bases sont opposées, la normale latérale est radiale.

Le champ est perpendiculaire aux normales des bases :

$$\Phi_1=\iint_{S_1}\vec E\cdot\vec n_1\,dS=0,
\qquad
\Phi_2=\iint_{S_2}\vec E\cdot\vec n_2\,dS=0.$$

Sur la surface latérale :

$$\Phi_3=\iint_{S_3}\vec E\cdot\vec n_3\,dS
=\iint_{S_3}E(r)\,dS
=E(r)\iint_{S_3}dS
=E(r)\,2\pi rh.$$

Ainsi,

$$\Phi=\Phi_1+\Phi_2+\Phi_3=\Phi_3
=\frac{q_{\mathrm{int}}}{\varepsilon_0}
=\frac{\lambda h}{\varepsilon_0}.$$

$$E(r)\,2\pi rh=\frac{\lambda h}{\varepsilon_0}
\quad\Longrightarrow\quad
\boxed{E(r)=\frac{\lambda}{2\pi\varepsilon_0r}.}$$

## Page 8

### Exemple du fil — espace de notes

La zone lignée est vide dans cette version.

## Page 9

### Plan infini uniformément chargé

Un plan infini $\Pi$ porte une densité surfacique uniforme $\sigma$. Les plans de symétrie imposent que le champ soit perpendiculaire à $\Pi$ :

$$\vec E=E_z(x,y,z)\vec k.$$

Les translations selon $x$ et $y$ donnent $\vec E=E_z(z)\vec k$.

On utilise un cylindre fermé traversant le plan, avec deux bases de même aire $S$, symétriques par rapport à $\Pi$. Le champ est tangent à la surface latérale, dont le flux est nul. Les normales des bases sont opposées, et

$$\vec E(-z)=-\vec E(z),\qquad \vec n_2=-\vec n_1.$$

Donc

$$\begin{aligned}
\Phi&=\iint_{S_1}\vec E\cdot\vec n_1\,dS
+\iint_{S_2}\vec E\cdot\vec n_2\,dS
+\iint_{S_3}\vec E\cdot\vec n_3\,dS\\
&=ES+ES+0=2ES,
\end{aligned}$$

et

$$\boxed{E=\frac{\sigma}{2\varepsilon_0}.}$$

> Précision de notation : le support écrit $E(z)S+E(-z)S$. Dans cette ligne, les deux termes sont les composantes suivant les normales sortantes, donc égales ; les composantes suivant le même axe $Oz$ sont, elles, opposées.

## Page 10

### Exemple du plan — espace de notes

La zone lignée est vide dans cette version.

## Page 11

### Boule uniformément chargée

Une boule de rayon $R$, de densité volumique uniforme $\rho$, est centrée en $O$. Sa symétrie sphérique impose

$$\vec E(r)=E(r)\vec u_r.$$

On choisit une sphère de Gauss de rayon $r$ centrée en $O$. Sur cette sphère :

$$\begin{aligned}
\Phi&=\oiint_{S_G}\vec E\cdot d\vec S
=\oiint_{S_G}\vec E\cdot\vec n\,dS\\
&=\oiint_{S_G}E(r)\,dS
=E(r)\oiint_{S_G}dS
=E(r)\,4\pi r^2.
\end{aligned}$$

Ainsi,

$$\Phi=\frac{q_{\mathrm{int}}}{\varepsilon_0}
=\frac{\rho V}{\varepsilon_0}
=E(r)\,4\pi r^2,$$

où $V$ désigne ici le volume chargé enfermé par la surface de Gauss.

**Figure.** Boule de rayon $R$ en rouge et sphère de Gauss de rayon $r$ en bleu, avec le point $M$ sur cette dernière et les axes $x,y,z$.

## Page 12

### Boule chargée — champ intérieur et extérieur

**Si $r>R$**, la sphère de Gauss enferme toute la charge $Q=\rho V$ :

$$\boxed{E(r)=\frac{Q}{4\pi\varepsilon_0r^2}.}$$

**Si $r<R$**, elle enferme seulement la charge du volume de rayon $r$ :

$$\boxed{E(r)=\frac{\rho r}{3\varepsilon_0}.}$$

La figure reprend les deux sphères concentriques et leurs rayons $R$ et $r$.

## Page 13

### Exemple de la boule — espace de notes

La zone lignée est vide dans cette version.

## Page 14

### Lignes de champ

Les lignes de champ produites par une charge ponctuelle placée en $O$ sont des droites passant par $O$.

**Figure.** Une sphère centrée en $O$, de rayon $r$, est traversée par des lignes de champ radiales, avec des flèches dirigées vers l’extérieur.

## Page 15

### Bibliographie

- [1] Polycopié de cours.
- [2] [CUPGE — CY : Introduction à l’électromagnétisme](https://cpinettes.u-cergy.fr/S3-Electromag.html).
- [3] Wikipédia.
- [4] [Encyclopédie Universalis](https://www.universalis.fr/encyclopedie).
- [5] David Sénéchal, [Histoire des sciences, PHQ399](https://www.physique.usherbrooke.ca/pages/node/7930), Université de Sherbrooke, Québec.
- [6] Pour la suite : [Khan Academy](https://fr.khanacademy.org/science/physics), [Unisciel](http://www.unisciel.fr/etudiants/), etc.
