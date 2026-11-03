# Mécanique du point — Résumé 1 : analyse dimensionnelle

> Source : `PREING1-S2/Mecanique-du-point/CM1_2013-2014_Mecanique-du-point_P1S2_DPhysique.pdf`, 2 pages. Université de Cergy-Pontoise, Introduction à la mécanique du point, S1-MPI 2013–2014 ; classement P1S2 conservé selon le dépôt.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale et comparaison au texte natif ; tableaux, formules et notes de bas de page restitués. Les définitions des étalons sont celles du document de 2013–2014, sans actualisation.

## Le système international (page 1)

Le système international est basé sur sept grandeurs fondamentales auxquelles sont associées une dimension et une unité :

| Grandeur | Dimension | Unité SI | Symbole SI |
| --- | --- | --- | --- |
| Longueur | $L$ | mètre | m |
| Masse | $M$ | kilogramme | kg |
| Temps | $T$ | seconde | s |
| Intensité électrique | $I$ | ampère | A |
| Température | $\theta$ | kelvin | K |
| Quantité de matière | $N$ | mole | mol |
| Intensité lumineuse | $J$ | candela | cd |

L’intensité lumineuse porte la note « pas à connaître » dans ce cours.

En mécanique, toutes les grandeurs peuvent s’écrire en fonction de $M,L,T$. La dimension d’une grandeur $G$ est notée $[G]$. La dimension d’une température est ici $\theta$, et non $T$, réservé au temps.

## Règles de l’analyse dimensionnelle (page 1)

$$[G_1G_2]=[G_1][G_2],\qquad\left[\frac{G_1}{G_2}\right]=\frac{[G_1]}{[G_2]},\qquad\left[\frac{d^nG}{dX^n}\right]=\frac{[G]}{[X]^n}.$$

Les membres des opérateurs $=,>,<,+,-$ doivent avoir la même dimension. Le texte indique que les constantes, les angles, les fonctions exp, ln et trigonométriques, ainsi que leurs arguments, sont sans dimension, c’est-à-dire de dimension 1.

**Précision sur la source.** L’affirmation sur les « constantes » concerne les constantes numériques sans unité ; une constante physique peut avoir une dimension.

On ne peut additionner ni soustraire des dimensions : le document barre l’expression $[l]+[d]$.

## Homogénéité (page 1)

Vérifier l’homogénéité d’une équation consiste à vérifier que ses membres ont la même dimension. Il faut contrôler l’homogénéité des équations : une équation non homogène est fausse.

## Les « pseudo-unités » du SI (page 2)

Le radian et le stéradian sont présentés comme des « pseudo-unités » : des unités associées à des grandeurs sans dimension. Le stéradian porte la note « pas à connaître ». Un angle est donc une grandeur sans dimension qui possède une unité.

## Unités dérivées du SI (page 2)

Les unités dérivées s’expriment à partir des sept unités fondamentales. Unités à connaître en mécanique :

| Grandeur | Unité SI | Symbole SI |
| --- | --- | --- |
| Force | newton | N |
| Énergie | joule | J |
| Puissance | watt | W |
| Pression | pascal | Pa |
| Fréquence | hertz | Hz |

Le document rappelle qu’une valeur numérique doit être accompagnée de son unité.

## Préfixes du système international (page 2)

| Facteur | Préfixe | Symbole | Facteur | Préfixe | Symbole |
| --- | --- | --- | --- | --- | --- |
| $10$ | déca | da | $10^{-1}$ | déci | d |
| $10^2$ | hecto | h | $10^{-2}$ | centi | c |
| $10^3$ | kilo | k | $10^{-3}$ | milli | m |
| $10^6$ | méga | M | $10^{-6}$ | micro | $\mu$ |
| $10^9$ | giga | G | $10^{-9}$ | nano | n |
| $10^{12}$ | téra | T | $10^{-12}$ | pico | p |
| $10^{15}$ | peta | P | $10^{-15}$ | femto | f |

Téra, pico, peta et femto portent la note « pas à connaître ». Ce tableau est celui de la source ; il n’est pas présenté comme une liste exhaustive actualisée.

## Étalons du système international, tels que décrits en 2013–2014 (page 2)

- **Mètre :** 1 m est la distance parcourue par la lumière dans le vide pendant $1/299\,792\,458$ s.
- **Seconde :** 1 s est la durée de $9\,192\,631\,770$ vibrations d’une raie de l’atome de césium 133.
- **Kilogramme :** 1 kg est décrit comme la masse d’un étalon en platine iridié déposé au BIPM à Sèvres.

Les valeurs numériques des deux premières définitions portent la note « pas à connaître ».
