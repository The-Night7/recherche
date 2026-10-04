---
source: "PREING2-S2/Ondes/Physique_des_ondes___guide_complet.png"
transcription: manuelle
transcription_date: 2026-10-04
verification: lecture visuelle de toute l’infographie ; équations, tableau, légendes et schémas transcrits ; incohérences annotées
---

# Physique des ondes — Le guide de révision complet

## I — L’oscillateur harmonique : le modèle idéal

**Équation du mouvement :**

$$
\ddot x+\omega_0^2x=0,
\qquad \omega_0=\sqrt{k/m}.
$$

$\omega_0$ : pulsation propre, en rad/s. Le schéma représente une masse $m$ sur un plan horizontal, reliée à un mur par un ressort de raideur $k$.

**Solution et énergie :**

$$
x(t)=A\cos(\omega_0t+\phi),
\qquad E_m=\frac12m\dot x^2+\frac12kx^2=\text{constante}.
$$

**Période propre :** $T_0=2\pi/\omega_0$, indépendante des conditions initiales. Le graphique montre une oscillation sinusoïdale d’amplitude constante.

## II — Oscillateurs amortis et forcés

### Les trois régimes d’amortissement

| Régime | Condition portée sur l’image | Allure du graphique |
| --- | --- | --- |
| Sous-amorti | $\Gamma<\Gamma_0$ | Oscillations autour de zéro, enveloppe décroissante. |
| Critique | $\Gamma=\Gamma_0$ | Retour vers zéro sans oscillation. |
| Sur-amorti | $\Gamma>\Gamma_0$ | Retour vers zéro sans oscillation. |

Les axes sont légendés « Déplacement » et « Temps ». Un autre petit graphique en cloche porte « Amplitude » en ordonnée et « Temps » en abscisse, avec $\omega_0$ marqué sous le maximum.

> Cette dernière abscisse est incohérente : le repère $\omega_0$ désigne une pulsation, pas un temps. Le symbole $\Gamma_0$ du seuil critique n’est pas défini dans l’image.

### Le phénomène de résonance

Sous une force $F_0\cos(\omega t)$, l’amplitude est maximale près de $\omega_0$. Le graphique porte « Amplitude » en ordonnée, « Pulsation excitatrice ($\omega$) » en abscisse, « Amplitude maximale » au sommet et $\omega\simeq\omega_0$ sous celui-ci.

**Transfert d’énergie :** à la résonance, la puissance moyenne absorbée est maximale. Les amplitudes sont très élevées si l’amortissement est faible.

## III — Systèmes couplés et modes normaux

### Couplage de $N$ oscillateurs

Le dessin montre deux masses $m_1$ et $m_2$, deux ressorts notés $k$ entre elles, sur un support horizontal.

**Système matriciel :**

$$
M\ddot x+Kx=\vec0,
$$

où $M$ est la matrice des masses et $K$ la matrice de raideur.

**Modes propres :** chaque mode correspond à une pulsation $\omega_n$ déterminée par les valeurs propres de $M^{-1}K$.

> Plus précisément, les valeurs propres sont les $\omega_n^2$ pour les modes oscillants stables.

### Exemple — Mode en phase et mode en opposition

Le premier dessin est intitulé « Mode 1 (en phase) » ; le deuxième, « Mode 2 (en opposition) ». Tous deux montrent $m_1$ à gauche et $m_2$ à droite, reliées par des ressorts notés $k$, avec une flèche vers la gauche sur $m_1$ et une flèche vers la droite sur $m_2$.

> Incohérence graphique de la source : les flèches sont opposées dans les **deux** dessins. Un mouvement en phase devrait montrer les deux déplacements dans le même sens.

## IV — L’équation d’onde de d’Alembert

L’image comporte les titres « Équation de d’Alembert » puis « La limite d’équation » et la formule :

$$
\frac{\partial^2u}{\partial t^2}-c^2\frac{\partial^2u}{\partial x^2}=0,
$$

où $c$ est la célérité de l’onde. Le schéma représente une déformation de corde, avec une bosse et un creux, se propageant vers la droite.

**Solutions de propagation — solution générale :**

$$
u(x,t)=f(x-ct)+g(x+ct).
$$

Somme d’une onde progressive vers la droite et d’une onde progressive vers la gauche.

## V — Dispersion et ondes stationnaires

### Relation de dispersion

$\omega(k)$ relie la pulsation au nombre d’onde. Si $\omega/k$ n’est pas constant, le milieu est dit dispersif.

### Formation d’ondes stationnaires

Superposition de deux ondes de même fréquence en sens inverses, par exemple par réflexion. Les dessins représentent une corde de longueur $L$ entre deux parois fixes, avec plusieurs profils d’oscillation. Les points immobiles sont légendés « Nœuds » ; les zones d’oscillation maximale, « Ventres ».

### Quantification des modes

Trois dessins portent $n=1$, $n=2$ et $n=3$. Les deux premiers montrent chacun un fuseau ; le troisième montre deux fuseaux. Sous les dessins figurent les inscriptions $\lambda_n$, $\lambda_2$ et « $\lambda_n=\lambda_3$ ».

Sur une corde de longueur $L$ fixée :

$$
\lambda_n=\frac{2L}{n}.
$$

Ce sont les fréquences spécifiques, ou harmoniques.

> Les dessins et annotations de longueur ne correspondent pas correctement aux modes annoncés : le mode $n$ d’une corde fixée aux deux extrémités comporte $n$ fuseaux, chacun de longueur $\lambda_n/2$.

## Comparaison des vitesses

| Type de vitesse | Formule | Signification physique |
| --- | --- | --- |
| Vitesse de phase ($v_\theta$ sur l’image) | $\omega/k$ | Vitesse de déplacement d’une phase constante (crête). |
| Vitesse de groupe ($v_g$) | $d\omega/dk$ | Vitesse de l’enveloppe d’un paquet d’ondes (énergie). |
| Célérité ($c$) | $\sqrt{T/\rho}$ | Vitesse de propagation dépendante des propriétés du milieu, par exemple une corde. |

> Dans la formule de la corde, $T$ est la tension et $\rho$ doit désigner la **masse linéique**. Ces deux symboles ne sont pas définis dans le tableau original. L’assimilation de la vitesse de groupe à une vitesse de transport d’énergie suppose un contexte où cette interprétation est applicable.

L’infographie porte la signature « NotebookLM » en bas à droite.
