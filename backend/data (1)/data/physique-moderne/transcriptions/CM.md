---
source: PREING2-S2/Physique-moderne/CM.docx
transcription: manuelle
format_source: docx
verification: lecture intégrale du texte et des tableaux Word
---

# CM Introduction Physique Moderne

Auteur : Mathis S.
Enseignant : P. Akridas
Date : 1er Février 2024
Catégorie : PREING2 S2, Physique-moderne

La physique quantique permet d'expliquer divers phénomènes fondamentaux et technologiques tels que le rayonnement des corps noirs selon la température, l'expérience de pensée du Chat de Schrödinger, et le fonctionnement des semi-conducteurs.

## Chapitre 1 : Quanta de lumière

### I. Description ondulatoire de la lumière

#### a. Diffraction et interférences

On considère un faisceau de rayons parallèles entre eux et perpendiculaires à la surface. Soit $\lambda$ la longueur d'onde, $S$ la source de lumière à l'infini, et $a$ la taille de l'ouverture.

Cas n°1 : $\lambda \ll a$
On observe une tache lumineuse correspondant à la taille de l'ouverture.

Cas n°2 : $\lambda \sim a$
La lumière s'étale au-delà de la forme géométrique de l'ouverture (diffraction).

#### b. Équations de Maxwell dans le vide

Les équations fondamentales régissant le champ électromagnétique sont les suivantes :

$$div \overrightarrow{E} = 0, \quad div \overrightarrow{B} = 0$$

$$\overrightarrow{rot} \overrightarrow{B} = \varepsilon_{0}\mu_{0}\frac{\partial\overrightarrow{E}}{\partial t}, \quad \overrightarrow{rot} \overrightarrow{E} = - \frac{\partial\overrightarrow{B}}{\partial t}$$

En supposant que $\overrightarrow{E}$ et $\overrightarrow{B}$ dépendent de $x$ et $t$, on aboutit à l'équation d'onde :

$$\frac{\partial^{2}E_{y}}{\partial t^{2}} - c^{2}\frac{\partial^{2}E_{y}}{\partial x^{2}} = 0 \quad \text{où } c^{2} = \frac{1}{\varepsilon_{0}\mu_{0}}$$

Les solutions sont de la forme $E_{y}(x,t) = E_{0}\cos(\omega t - kx)$, où $\omega = 2\pi\nu$ (pulsation) et $k = \frac{2\pi}{\lambda}$ (nombre d'onde).

### II. Insuffisance du modèle ondulatoire

#### a. Effet photoélectrique

Lorsqu'un métal est éclairé par une lumière monochromatique, on observe qu'au-dessus d'une fréquence seuil $\nu_{s}$, la lumière arrache des électrons, générant un courant électrique.

Observations clés :

L'énergie des électrons arrachés est indépendante de l'intensité $I$ de la source.

Le courant $i$ est proportionnel à l'intensité $I$.

L'énergie cinétique des électrons est proportionnelle à la fréquence $\nu$.

#### b. Nouvelle interprétation (Planck-Einstein)

L'énergie de la lumière est quantifiée : $E = h\nu$.
Le bilan d'énergie s'écrit :

$$E_{\text{photon}} = W + \frac{1}{2}mv^{2}$$

Où $W$ est le travail d'extraction du métal. Si $\nu = \nu_{s}$, alors $W = h\nu_{s}$.

### III. La lumière : onde ou particule ?

#### a. Interféromètre de Mach-Zehnder

L'analyse montre que si le chemin d'un photon n'est pas connu, on observe des interférences (aspect ondulatoire). Si le chemin est connu, les interférences disparaissent (aspect corpusculaire).

Conclusion : Le photon est un quanton, un objet physique possédant des propriétés ondulatoires ou corpusculaires selon l'expérience.

## Chapitre 2 : Ondes de matière

### I. Hypothèse de Louis de Broglie

De Broglie associe une onde à toute particule de masse $m$ :
$$\lambda_{dB} = \frac{h}{mv}$$

### II. Postulats de la mécanique quantique

Premier postulat : L'état d'un système est défini par sa fonction d'onde $\psi(\overrightarrow{r},t)$.

Deuxième postulat : La probabilité de présence d'une particule est donnée par $|\psi(\overrightarrow{r},t)|^{2}$.


### III. Relation d'indétermination d'Heisenberg

Il existe une limite fondamentale à la précision avec laquelle on peut connaître simultanément certaines propriétés :

$$\Delta x \Delta p \geq \frac{\hbar}{2}$$

$$\Delta E \Delta t \geq \frac{\hbar}{2}$$

## Chapitre 3 : Équation de Schrödinger

### I. Équation générale

Pour une particule de masse $m$ dans un potentiel $V(\overrightarrow{r},t)$ :

$$i\hbar\frac{\partial\psi}{\partial t}(\overrightarrow{r},t) = - \frac{\hbar^{2}}{2m}\Delta\psi(\overrightarrow{r},t) + V(\overrightarrow{r},t)\psi(\overrightarrow{r},t)$$

### II. États stationnaires

Un état est stationnaire si son énergie est constante. La fonction d'onde se sépare en une partie spatiale et une partie temporelle :
$$\psi(x,t) = \phi(x)e^{- \frac{iEt}{\hbar}}$$

L'équation de Schrödinger indépendante du temps devient :
$$- \frac{\hbar^{2}}{2m}\frac{d^{2}\phi}{dx^{2}} + V(x)\phi(x) = E\phi(x)$$

### III. Puits de potentiel infini

Pour une particule confinée entre $0$ et $L$ où $V(x)=0$ :

Fonctions d'onde : $\phi_{n}(x) = \sqrt{\frac{2}{L}}\sin\left( \frac{n\pi x}{L} \right)$

Énergies quantifiées : $E_{n} = \frac{n^{2}h^{2}}{8mL^{2}}$

### IV. Effet tunnel

Quantiquement, une particule d'énergie $E < V_{0}$ a une probabilité non nulle de traverser une barrière de potentiel. Ce phénomène explique notamment la radioactivité $\alpha$.

## Notes de transcription et précisions

Les équations ont été séparées en blocs LaTeX ; le fragment de tableau isolé `|---|` a été retiré. La notation $\hslash$ a été normalisée en $\hbar$.

- Le texte qualifie l’énergie cinétique photoélectrique de « proportionnelle » à la fréquence. Le bilan donné dans le document précise $E_{c,\max}=h\nu-W$ : c’est une relation affine au-dessus du seuil, pour le maximum de l’énergie cinétique.
- $|\psi(\vec r,t)|^2$ est une **densité** de probabilité de présence ; la probabilité dans un domaine s’obtient par intégration.
- La formule $\lambda=h/(mv)$ utilise l’impulsion non relativiste $p=mv$.
- Une énergie moyenne constante ne suffit pas à définir un état stationnaire. La séparation $\psi(x,t)=\phi(x)e^{-iEt/\hbar}$ présentée ici concerne un état propre d’un Hamiltonien indépendant du temps.
- La relation énergie–temps reproduite dans le document nécessite de préciser ce que représente $\Delta t$ ; elle ne s’interprète pas directement comme la relation position–impulsion.
