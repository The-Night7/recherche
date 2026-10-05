---
source: "PREING2-S1/Electromagnetisme/CM-Chapitre3-Superposition-et-symetrie_2022-2023_Electromagnetisme_P2S1_EDupont.pdf"
pages: 11
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-05
verification: lecture visuelle intégrale des pages rendues et comparaison avec le texte natif ; formules restituées en LaTeX
---

# Électromagnétisme — Chapitre 3 : superposition et symétries, annoté

## Page 1

Électromagnétisme — Chapitre 3 — Théorème de superposition et symétries.

Physique, 2022-2023. Présentation rédigée par Émilie Dupont (Cergy), emilie.dupont@cyu.fr, CY308. CY Tech, Cergy Paris Université.

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

### 1.3.1. Invariances d’une distribution

**Invariance par translation.** Si $\rho(\vec r)$ est invariante dans toute translation parallèle à un axe $Oz$, alors $\vec E$ ne dépend pas de $z$.

**Invariance par rotation / symétrie axiale.** Si $\rho(\vec r)$ est invariante dans toute rotation autour d’un axe $Oz$, alors la distribution présente une symétrie axiale. Il convient d’utiliser les coordonnées cylindriques. Dans ce cas, les composantes de $\vec E(r,\theta,z)$ dans cette base ne dépendent pas de $\theta$.

**Symétrie cylindrique.** Si la distribution est invariante par toute translation parallèle à $Oz$ et toute rotation autour de $Oz$, elle présente une symétrie cylindrique. Dans ce cas, les composantes du champ ne dépendent que de $r$.

Extrait du cours [7].

**Annotations.** Les dépendances supprimées sont barrées : $z$ pour la translation, $\theta$ pour la rotation, $\theta$ et $z$ pour la symétrie cylindrique. Un fil illustre l’axe de translation et de rotation.

## Page 4

### 1.3.2. Direction de $\vec E$ en un point d’un plan de symétrie ou d’antisymétrie

**Plan de symétrie.** Si $\rho(\vec r)$ admet un plan de symétrie, alors, en tout point de ce plan, le champ électrostatique est contenu dans ce plan.

**Plan d’antisymétrie.** Si la réflexion par rapport à un plan transforme la distribution $\rho(\vec r)$ en $-\rho(\vec r)$, c’est-à-dire qu’à une charge positive correspond une charge négative et réciproquement, alors, en tout point de ce plan, le champ électrostatique est perpendiculaire à ce plan.

Extrait du cours [7].

**Annotations.** Deux plans de symétrie distincts contenant le point considéré permettent de déterminer la direction du champ par leur intersection. Un seul plan d’antisymétrie contenant le point suffit à imposer la direction normale au plan. Des croquis représentent le champ tangent au plan de symétrie et normal au plan d’antisymétrie.

## Page 5

### Exemple : deux charges identiques

Deux charges identiques sont placées en $A$ et $B$.

- Pas de symétrie de translation.
- Symétrie miroir par tout plan contenant la droite $(AB)$.
- Symétrie miroir par le plan médiateur du segment $[AB]$.
- Symétrie de rotation autour de $(AB)$.

**Figures.** Deux plans contenant $(AB)$ et le plan médiateur sont représentés. Des flèches de champ s’éloignent des charges positives. Une seconde figure montre les lignes de champ de deux charges positives : elles partent de chaque charge et s’écartent dans la région entre les deux charges. Référence [7].

**Annotations.** Les plans sont repérés $P$, $P_1$, $P_2$. Le champ appartient aux plans de symétrie contenant le point étudié. Le point médian $C$ entre les charges est repéré sur les lignes de champ.

> Précision de transcription : l’annotation « direction commune aux trois plans » s’applique en tenant compte de la position du point. Au milieu des deux charges identiques, les contraintes imposent $\vec E(C)=\vec 0$ ; on ne peut imposer à un point quelconque d’appartenir aux trois plans dessinés.

## Page 6

### Exemple : fil infini chargé

- Symétrie de translation le long du fil.
- Symétrie miroir par tout plan contenant le fil.
- Symétrie miroir par tout plan perpendiculaire au fil.
- Symétrie de rotation autour de l’axe du fil : symétrie axiale.

**Figures.** Le fil vertical est accompagné de deux plans qui le contiennent et d’un plan perpendiculaire. Les flèches du champ sont radiales. La vue de dessus représente le fil par un point central, entouré de flèches dirigées vers l’extérieur. Référence [7].

**Annotations.** On choisit les coordonnées cylindriques $(r,\theta,z)$. L’invariance suivant $z$ et en rotation suivant $\theta$ donne une intensité $E(r)$. Les plans contenant le fil et les plans perpendiculaires au fil permettent de préciser la direction.

## Page 7

### Direction du champ du fil — annotations manuscrites

Le champ appartient aux plans de symétrie qui contiennent $M$. Leur intersection est la direction radiale :

$$\boxed{\vec E(M)=E(r)\vec u_r.}$$

L’annotation renvoie au théorème de Gauss du chapitre 4 pour déterminer l’intensité :

$$E(r)=\frac{\lambda}{2\pi\varepsilon_0r}.$$

$\lambda$ est une densité linéique en $\mathrm{C\,m^{-1}}$ ; $r$ est la distance au fil en mètres.

**Lecture des plans.** Un plan contenant le fil et $M$, ainsi que le plan perpendiculaire au fil passant par $M$, se coupent suivant la direction $\vec u_r$. Les différents plans repérés sur le dessin illustrent ces symétries.

## Page 8

### 1.3.3. Distribution linéique uniformément chargée

Il existe une symétrie cylindrique et une invariance par translation. Le champ en $M$ s’exprime en coordonnées cylindriques :

$$\vec E(r)=E(r)\vec u_r.$$

**Schéma.** Fil rectiligne de densité $\lambda$, point $M$ situé à distance du fil. **Annotations.** Les plans repérés $P_1,P_2,P_3$ servent à retrouver la direction radiale ; les invariances éliminent les dépendances en $\theta$ et en $z$.

## Page 9

### Plan infini uniformément chargé

Un plan infini $\Pi$ porte une charge électrique uniforme $\sigma$ par unité de surface.

Le champ appartient aux plans de symétrie passant par $M$ et perpendiculaires à $\Pi$ ; il est donc perpendiculaire à $\Pi$ :

$$\vec E(M)=E_z(x,y,z)\vec k.$$

Les invariances par translation suivant $x$ et $y$ donnent

$$\vec E(M)=E_z(z)\vec k.$$

**Schéma.** Le plan $\Pi$ est horizontal, $Oz$ lui est perpendiculaire. Un cylindre fermé le traverse : $S_1$ est au-dessus, $S_2$ au-dessous, $S_3$ est la surface latérale ; les normales aux bases pointent vers l’extérieur. Le point $M$ est sur l’axe, en haut du cylindre. **Annotations.** $\sigma=dq/dS=\sigma_0$. On choisit les coordonnées cartésiennes $(O,\vec i,\vec j,\vec k)$. Les plans $(M,\vec j,\vec k)$ et $(M,\vec i,\vec k)$ sont des plans de symétrie ; leur intersection impose la direction $\vec k$.

## Page 10

### Boule uniformément chargée

La distribution présente une symétrie sphérique :

$$\vec E(r)=E(r)\vec u_r.$$

**Schéma.** Une boule de rayon $R$, centrée en $O$, est représentée en rouge ; une sphère concentrique de rayon $r$ passant par $M$ est représentée en bleu. Les axes $x,y,z$ et les rayons $R,r$ sont indiqués. **Annotations.** On choisit les coordonnées sphériques $(r,\theta,\varphi)$ et la base $(\vec u_r,\vec u_\theta,\vec u_\varphi)$. Les rotations suppriment les dépendances angulaires. Tout plan contenant $O$ et $M$ est un plan de symétrie : le champ est radial.

La remarque « $R=0$ : charge ponctuelle » rapproche ce dessin du modèle d’une charge ponctuelle. Une figure complémentaire montre des lignes de champ radiales.

## Page 11

### Bibliographie

- [1] Polycopié de cours.
- [2] [CUPGE — CY : Introduction à l’électromagnétisme](https://cpinettes.u-cergy.fr/S3-Electromag.html).
- [3] Wikipédia.
- [4] [Encyclopédie Universalis](https://www.universalis.fr/encyclopedie).
- [5] David Sénéchal, [Histoire des sciences, PHQ399](https://www.physique.usherbrooke.ca/pages/node/7930), Université de Sherbrooke, Québec.
- [6] Pour la suite : [Khan Academy](https://fr.khanacademy.org/science/physics), [Unisciel](http://www.unisciel.fr/etudiants/), etc.
- [7] Nicolas Menguy, [LP 203 — Champs électrique et magnétique](http://www-ext.impmc.upmc.fr/~menguy/Cours_LP203.html).
