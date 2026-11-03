---
source: "PREING2-S2/Ondes-CC/CC1-2024-2025-Correction_Ondes-CC_P2S2_DPhysique.pdf"
pages: 10
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle des dix pages ; énoncés, cases noircies, corrigés manuscrits et graphique vérifiés
---

# Ondes — PI2-MI — CC1 2024–2025 — Sujet et corrigé

## Consignes (page 1)

Durée : **1 h 30** (2 h en cas de tiers-temps). Documents et objets électroniques interdits.

Seules doivent être rendues la feuille de réponses au QCM et, le cas échéant, les feuilles de réponses aux questions ouvertes, signalées par ♣. Noircir complètement la case correspondant à la réponse choisie. Chaque question ne comporte qu’une réponse correcte. Il n’y a pas de point négatif pour une réponse incorrecte.

Le document comporte 10 pages et 17 questions. Le barème est indicatif et susceptible d’être modifié. L’en-tête porte la mention « Catalogue ».

> Les réponses correctes du QCM sont les cases noircies de la source. Dans cette version catalogue, elles correspondent toutes à A. Les réponses manuscrites des pages 7 à 9 sont transcrites après les questions auxquelles elles se rapportent.

## Approximation harmonique — 8 points (page 2)

### Question 1 [PbAHQ0] ♣ — 2,5 points

Soit une énergie potentielle $E_p(r)$ présentant une position d’équilibre stable en $r_{\mathrm{eq}}$. Montrer qu’au voisinage de $r_{\mathrm{eq}}$, cette énergie peut être approximée par une énergie potentielle de rappel élastique de position d’équilibre $r_{\mathrm{eq}}$ et de constante de raideur $k$.

**Corrigé manuscrit, page 7.** Développement limité d’ordre 2 en $(r-r_{\mathrm{eq}})$ au voisinage de $r_{\mathrm{eq}}$ :

$$
E_p(r)\simeq E_p(r_{\mathrm{eq}})
+\left.\frac{dE_p}{dr}\right|_{r_{\mathrm{eq}}}(r-r_{\mathrm{eq}})
+\frac12\left.\frac{d^2E_p}{dr^2}\right|_{r_{\mathrm{eq}}}(r-r_{\mathrm{eq}})^2.
$$

La dérivée première est nulle en un extremum ; la dérivée seconde est positive en un minimum non dégénéré. On identifie donc un rappel élastique de paramètres $(k,r_{\mathrm{eq}})$ :

$$
E_p(r)\simeq E_p(r_{\mathrm{eq}})+\frac12k(r-r_{\mathrm{eq}})^2,
\qquad k>0.
$$

> Le manuscrit emploie le signe $=$ pour ce développement limité ; le signe $\simeq$ explicite ici l’approximation au second ordre. La stabilité seule permet aussi des minima dégénérés ; l’approximation harmonique avec $k>0$ suppose une courbure strictement positive.

### Question 2 [PbAHQ1] — 0,5 point

Par identification, $k$ est égale à :

| Réponse | Expression |
| --- | --- |
| **A — correcte** | $+\left.\dfrac{d^2E_p}{dr^2}\right|_{r_{\mathrm{eq}}}$ |
| B | $-\left.\dfrac{d^2E_p}{dr^2}\right|_{r_{\mathrm{eq}}}$ |
| C | $+\left.\dfrac{dE_p}{dr}\right|_{r_{\mathrm{eq}}}$ |
| D | $-\left.\dfrac{dE_p}{dr}\right|_{r_{\mathrm{eq}}}$ |

### Potentiel de Morse — données des questions 3 à 6

On peut décrire la vibration d’une molécule diatomique à l’aide d’une énergie potentielle de Morse entre les deux atomes :

$$
E_p(r)=E_p(R)+D\{1-\exp[-a(r-R)]\}^2,
$$

où $r$ est la distance entre atomes et $D,a,R$ des constantes positives.

### Question 3 [PbAHQ2] — 1 point

Les dimensions physiques de $D$ et $a$ sont :

| Réponse | Dimensions |
| --- | --- |
| **A — correcte** | $[D]=\mathrm{ML^2T^{-2}}$ et $[a]=\mathrm{L^{-1}}$ |
| B | $[D]=[a]=\mathrm L$ |
| C | $[D]=\mathrm{MLT^{-2}}$ et $[a]=\mathrm L$ |
| D | $[D]=\mathrm{MLT^{-2}}$ et $[a]=\mathrm{L^{-1}}$ |
| E | Aucune des réponses précédentes n’est correcte. |

### Question 4 [PbAHQ3] — 1 point

La distance d’équilibre $r_{\mathrm{eq}}$ entre les atomes est égale à :

| Réponse | Valeur |
| --- | --- |
| **A — correcte** | $R$ |
| B | $2R$ |
| C | $R/2$ |
| D | $R/a$ |
| E | Aucune des réponses précédentes n’est correcte. |

### Question 5 [PbAHQ4] — 1,5 point

Dans le cadre de l’approximation harmonique, $k$ est égale à :

| Réponse | Valeur |
| --- | --- |
| **A — correcte** | $2a^2D$ |
| B | $a^2D$ |
| C | $2aD$ |
| D | $\sqrt2\,a^2D$ |
| E | Aucune des réponses précédentes n’est correcte. |

### Question 6 [PbAHQ5] ♣ — 1,5 point

Représenter qualitativement $E_p(r)$ en prenant $E_p(R)=0$. Faire apparaître $r_{\mathrm{eq}}$, ainsi que les valeurs de $E_p$ en $r_{\mathrm{eq}}$ et aux valeurs extrêmes de $r$.

**Graphique corrigé, page 7.** L’axe horizontal représente $r\ge0$ et l’axe vertical $E_p$. La courbe part de $D[1-\exp(aR)]^2$ en $r=0$, décroît jusqu’à son minimum nul en $r_{\mathrm{eq}}=R$, puis croît et tend vers l’asymptote horizontale $E_p=D$, représentée en pointillés. Les trois valeurs indiquées sont donc

$$
E_p(0)=D(1-e^{aR})^2,\qquad E_p(R)=0,\qquad
\lim_{r\to+\infty}E_p(r)=D.
$$

## Oscillateur harmonique — 6 points (page 3)

Dans le référentiel terrestre, approximé galiléen, un ressort idéal horizontal de raideur $k$ et de longueur à vide $\ell_0$ relie un bloc $M$ de masse $m$ à un point fixe $H$. Le bloc glisse sans frottement sur le plan horizontal et sa position est repérée par $x(t)$. Sa position pour le ressort à vide est notée $x_0$.

### Question 7 [PbOHQ0] — 1 point

La force $\vec F$ du ressort sur $M$ est égale à :

| Réponse | Force |
| --- | --- |
| **A — correcte** | $-k(x-x_0)\vec u_x$ |
| B | $+k(x-x_0)\vec u_x$ |
| C | $-k(x-x_H)\vec u_x$ |
| D | $+k(x-x_H)\vec u_x$ |
| E | Aucune des réponses précédentes n’est correcte. |

### Question 8 [PbOHQ1] ♣ — 1,5 point

Montrer que l’équation du mouvement sur l’axe horizontal peut se mettre sous la forme

$$\ddot X(t)+\omega_0^2X(t)=0,$$

où $X$ et $\omega_0$ sont à exprimer en fonction des paramètres de l’énoncé.

**Corrigé manuscrit, page 8.** Le schéma représente le ressort fixé en $H$, le bloc $M$, l’axe $x$ orienté à droite, la position $x(t)$ et la position à vide $x_0=x_{\mathrm{eq}}$. Dans le référentiel terrestre galiléen, le principe fondamental de la dynamique projeté sur $\vec u_x$ donne

$$
m\ddot x(t)=-k[x(t)-x_0]=-k[x(t)-x_{\mathrm{eq}}].
$$

D’où l’équation demandée, avec

$$
\boxed{X(t)=x(t)-x_0=x(t)-x_{\mathrm{eq}}},\qquad
\boxed{\omega_0^2=\frac{k}{m}}.
$$

### Question 9 [PbOHQ2] — 1 point

La solution générale peut se mettre sous la forme $X(t)=$

| Réponse | Expression |
| --- | --- |
| **A — correcte** | $\alpha_c\cos(\omega_0t)+\alpha_s\sin(\omega_0t)$, où $\alpha_c,\alpha_s$ sont des constantes réelles. |
| B | $\alpha_+e^{+\omega_0t}+\alpha_-e^{-\omega_0t}$, où $\alpha_+,\alpha_-$ sont des constantes réelles. |
| C | $e^{-t/\tau}[\alpha_c\cos(\omega_0t)+\alpha_s\sin(\omega_0t)]$, où $\tau,\alpha_c,\alpha_s$ sont des constantes réelles. |
| D | $e^{-t/\tau}(\alpha_0+\alpha_1t)$, où la source indique « $\tau,\alpha_1,\alpha_2$ constantes réelles ». |
| E | Aucune des réponses précédentes n’est correcte. |

> Le décalage des indices $\alpha_0,\alpha_1$ / $\alpha_1,\alpha_2$ dans D figure dans la source.

### Question 10 [PbOHQ3] ♣ — 1,5 point

Si $X(0)=\beta$ et $\dot X(0)=0$, déterminer $X(t)$.

**Corrigé manuscrit, page 8.**

$$
\begin{cases}
X(t)=\alpha_c\cos(\omega_0t)+\alpha_s\sin(\omega_0t),\\
\dot X(t)=\omega_0[-\alpha_c\sin(\omega_0t)+\alpha_s\cos(\omega_0t)].
\end{cases}
$$

Les conditions initiales donnent

$$X(0)=\beta=\alpha_c,\qquad \dot X(0)=0=\omega_0\alpha_s
\quad\Longrightarrow\quad \alpha_s=0.$$

Le manuscrit s’arrête à ces constantes ; leur substitution donne $X(t)=\beta\cos(\omega_0t)$.

### Question 11 [PbOHQ4] — 1 point

De façon générale, la période $T_0$ d’un oscillateur harmonique :

- **A — correcte :** ne dépend que des paramètres du système et pas de son état à un instant donné.
- B : ne dépend que de l’état du système à un instant donné et pas de ses paramètres.
- C : dépend des paramètres du système et de son état à un instant donné.
- D : ne dépend ni des paramètres du système ni de son état à un instant donné.

## Oscillateur amorti — 8 points (page 4)

On ajoute une force de frottement fluide $\vec f=-\mu\vec v$ due à l’air, avec un coefficient positif et $\vec v$ la vitesse du bloc par rapport à l’air. L’équation devient

$$\ddot X(t)+\Gamma\dot X(t)+\omega_0^2X(t)=0.$$

> Le texte source appelle le coefficient positif « $\alpha$ », alors que la formule et les réponses utilisent $\mu$.

### Question 12 [PbOAQ0] — 1 point

Le paramètre $\Gamma$ est égal à : **A — correcte :** $+\mu/m$ ; B : $-\mu/m$ ; C : $+k/m$ ; D : $-k/m$.

### Question 13 [PbOAQ1] — 1 point

Au cours du temps, l’amplitude du mouvement d’un oscillateur amorti non forcé ne peut que : **A — correcte :** diminuer ; B : augmenter ; C : rester constante.

On cherche la solution générale avec l’ansatz complexe $\widetilde X(t)=\widetilde\alpha\exp(rt)$, où $\widetilde\alpha,r$ sont des constantes complexes.

### Question 14 [PbOAQ2] ♣ — 1,5 point

Déterminer l’équation caractéristique dont $r$ est solution.

**Corrigé manuscrit, page 9.**

$$
\dot{\widetilde X}(t)=r\widetilde X(t),\qquad
\ddot{\widetilde X}(t)=r^2\widetilde X(t).
$$

En substituant dans l’équation du mouvement,

$$
(r^2+\Gamma r+\omega_0^2)\widetilde X(t)=0\qquad\forall t.
$$

Soit $\widetilde X(t)=0$ pour tout $t$ (pas d’oscillation, solution non gardée ici), soit

$$\boxed{r^2+\Gamma r+\omega_0^2=0}.\tag{1}$$

### Question 15 [PbOAQ3] ♣ — 2,5 points

En déduire qu’il existe trois régimes possibles en fonction d’une condition sur $\omega_0$ à exprimer. Il n’est pas nécessaire d’écrire $X(t)$ pour chaque régime.

**Corrigé manuscrit, page 9.** Les solutions de (1) sont

$$
r_\pm=-\frac\Gamma2\pm\left[\left(\frac\Gamma2\right)^2-\omega_0^2\right]^{1/2},
\qquad \Gamma,\omega_0\ge0.
$$

| Signe de $(\Gamma/2)^2-\omega_0^2$ | Condition | Régime |
| --- | --- | --- |
| $>0$ | $\Gamma/2>\omega_0$ | Sur-amorti ou apériodique |
| $=0$ | $\Gamma/2=\omega_0$ | Critique |
| $<0$ | $\Gamma/2<\omega_0$ | Sous-amorti ou pseudo-périodique |

### Question 16 [PbOAQ4] — 1 point

Dans le régime sur-amorti, la solution générale $X(t)=\operatorname{Re}[\widetilde X(t)]$ est une somme :

- **A — correcte :** d’exponentielles décroissantes.
- B : d’une exponentielle croissante et d’une exponentielle décroissante.
- C : d’exponentielles croissantes.
- D : de fonctions trigonométriques.
- E : aucune des réponses précédentes n’est correcte.

### Question 17 [PbOAQ5] — 1 point

Dans le régime sous-amorti, on ajoute une force extérieure périodique de pulsation $w_d$. À la résonance, l’amplitude des oscillations en fonction de $w_d$ est : **A — correcte :** maximale ; B : minimale ; C : nulle ; D : aucune des réponses précédentes n’est correcte.

## Feuilles de réponses et barème (pages 5 à 10)

La page 5 comporte les champs Nom, Prénom et Groupe, puis huit colonnes de chiffres de 0 à 9 pour coder le numéro étudiant, à remplir de gauche à droite en coloriant complètement les cases.

La page 6 noircit la réponse A aux questions **2, 3, 4, 5, 7, 9, 11, 12, 13, 16 et 17**. Les autres questions sont ouvertes.

Les pages 7 à 9 comportent les corrigés manuscrits transcrits ci-dessus et les subdivisions de barème réservées à l’enseignant :

| Question | Intitulé de la case | Subdivisions en points |
| --- | --- | --- |
| 1 | Approximation harmonique | 0,5 ; 1 ; 1 |
| 6 | Graphique $E_p(r)$ | 0,25 ; 0,25 ; 0,5 ; 0,5 |
| 8 | Équation de l’oscillateur harmonique | 0,5 ; 1 |
| 10 | $X(t)$ particulière | 0,5 ; 1 |
| 14 | Équation caractéristique de l’oscillateur amorti | 0,5 ; 1 |
| 15 | Trois régimes | 0,5 ; 1 ; 1 |

La page 10 est un espace de rédaction supplémentaire vide, avec la consigne d’indiquer le numéro de la question traitée.
