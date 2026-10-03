---
source: "PREING2-S2/Ondes/Physique_des_ondes___guide_complet.png"
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale de l’infographie ; formules, tableau et schémas transcrits ; incohérences graphiques signalées
---

# Physique des ondes — Le guide de révision complet

> Transcription de l’infographie portant la signature NotebookLM. Les schémas sont décrits et les erreurs de la source sont signalées séparément.

## I. L’oscillateur harmonique — Le modèle idéal

### Équation du mouvement

$$\ddot x+\omega_0^2x=0,\qquad \omega_0=\sqrt{\frac{k}{m}}.$$

$\omega_0$ est la pulsation propre, exprimée en rad/s. Le dessin montre un ressort de raideur $k$ fixé à un mur et relié à une masse $m$ sur un plan horizontal.

### Solution et énergie

$$x(t)=A\cos(\omega_0t+\phi),$$

$$E_m=\frac12m\dot x^2+\frac12kx^2=\text{constante}.$$

### Période propre

$$T_0=\frac{2\pi}{\omega_0}.$$

Elle est indépendante des conditions initiales. Le tracé associé représente une sinusoïde d’amplitude constante.

## II. Oscillateurs amortis et forcés

### Les trois régimes d’amortissement

| Régime | Condition affichée | Tracé du déplacement en fonction du temps |
| --- | --- | --- |
| Sous-amorti | $\Gamma<\Gamma_0$ | Oscillations sous une enveloppe décroissante |
| Critique | $\Gamma=\Gamma_0$ | Retour à zéro sans oscillation |
| Sur-amorti | $\Gamma>\Gamma_0$ | Retour à zéro sans oscillation |

> Le symbole $\Gamma_0$ n’est pas défini dans l’image. Avec la convention $\ddot x+\Gamma\dot x+\omega_0^2x=0$, sa valeur critique serait $2\omega_0$. Il ne faut pas l’identifier silencieusement à $\omega_0$.

Un petit graphique supplémentaire présente un pic d’amplitude, une verticale pointillée repérée $\omega_0$, mais un axe horizontal intitulé « Temps ». Cette légende est incohérente avec le repère de pulsation.

### Le phénomène de résonance

Sous une force $F_0\cos(\omega t)$, l’amplitude est maximale près de $\omega_0$. Le graphique représente l’amplitude en fonction de la pulsation excitatrice $\omega$, avec un pic annoté « Amplitude maximale » pour $\omega\approx\omega_0$.

### Transfert d’énergie

À la résonance, la puissance moyenne absorbée est maximale. Les amplitudes sont très élevées si l’amortissement est faible.

> Les maxima de déplacement et de puissance absorbée ne sont pas exactement au même endroit en présence de frottement visqueux. L’image emploie ici une description qualitative, valable près de $\omega_0$ pour un faible amortissement.

## III. Systèmes couplés et modes normaux

### Couplage de N oscillateurs

Le schéma montre deux masses $m_1,m_2$ sur un plan horizontal, reliées par deux ressorts dessinés en série, chacun noté $k$.

Le système matriciel est

$$M\ddot x+Kx=0,$$

avec $M$ la matrice des masses et $K$ la matrice de raideur.

### Modes propres

Chaque mode correspond à une pulsation $\omega_\mu$ déterminée par les valeurs propres de $M^{-1}K$.

> Précision : pour un mode $x(t)=v e^{i\omega t}$, on obtient $M^{-1}Kv=\omega^2v$. Les valeurs propres sont donc les carrés des pulsations.

### Exemple — Mode en phase et mode en opposition

Deux dessins sont intitulés « Mode 1 (en phase) » et « Mode 2 (en opposition) ». Chacun représente deux masses $m_1,m_2$ reliées par des ressorts $k$. Dans les deux dessins, la flèche de la masse gauche pointe vers la gauche et celle de la masse droite vers la droite.

> **Incohérence du dessin :** les flèches du premier schéma indiquent elles aussi une opposition de mouvement. Un mouvement en phase aurait des déplacements simultanés de même signe ; le titre et les flèches du « Mode 1 » ne concordent pas.

## IV. L’équation d’onde de d’Alembert

Le dessin représente une déformation de corde en cours de propagation vers la droite. Sous le libellé « La Limite d’equation », l’image donne

$$\frac{\partial^2u}{\partial t^2}-c^2\frac{\partial^2u}{\partial x^2}=0,$$

où $c$ est la célérité de l’onde.

### Solutions de propagation

La solution générale est

$$u(x,t)=f(x-ct)+g(x+ct).$$

Elle est la somme d’une onde progressive vers la droite et d’une onde progressive vers la gauche.

## V. Dispersion et ondes stationnaires

### Relation de dispersion

La relation de dispersion $\omega(k)$ relie pulsation et nombre d’onde. Si $\omega/k$ n’est pas constant, le milieu est dit dispersif.

### Formation d’ondes stationnaires

Une onde stationnaire résulte de la superposition de deux ondes de même fréquence se propageant en sens inverses, par exemple après réflexion.

Le schéma représente une corde de longueur $L$ fixée à ses extrémités. Plusieurs profils superposés illustrent les oscillations. Les nœuds sont les points immobiles ; les ventres sont les points d’amplitude maximale.

### Quantification des modes

Les dessins des modes $n=1$, $n=2$ et $n=3$ sont suivis de la formule

$$\boxed{\lambda_n=\frac{2L}{n}},$$

pour une corde de longueur $L$ fixée à ses extrémités, avec des fréquences spécifiques, ou harmoniques.

> **Incohérences graphiques :** les petites flèches horizontales sous les modes sont étiquetées comme des longueurs d’onde alors qu’elles ne représentent pas de manière cohérente les valeurs $2L/n$. Sous le troisième dessin figure notamment « $\lambda_n=\lambda_3$ ». La formule encadrée donne la relation exploitable ; ces graduations ne permettent pas une lecture quantitative fiable.

## Comparaison des vitesses

| Type de vitesse | Formule | Signification physique |
| --- | --- | --- |
| Vitesse de phase $v_\varphi$ | $\omega/k$ | Vitesse de déplacement d’une phase constante, par exemple une crête |
| Vitesse de groupe $v_g$ | $d\omega/dk$ | Vitesse de l’enveloppe d’un paquet d’ondes, associée à l’énergie dans le cadre usuel |
| Célérité $c$ | $\sqrt{T/\rho}$ | Vitesse de propagation dépendant des propriétés du milieu, par exemple d’une corde |

> Dans la dernière formule, $\rho$ doit désigner la masse linéique de la corde et $T$ sa tension. L’infographie ne définit pas ces deux symboles.
