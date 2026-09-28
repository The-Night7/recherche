---
source: ING 1/S1 INFO/Data-Exploration/TP5-EX4-2-Correction_Data-Exploration.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Data exploration — TP5, exercice 4, question 2.d : contribution aux axes de l’ACP

## Page 1 — Axe $C_1$

Les variables `X100`, `X400` et `X110.hurdle` contribuent le plus à la construction de l’axe $C_1$. Ces épreuves sont des épreuves de vitesse : plus le temps pris par l’athlète est faible, plus il est rapide.

Les corrélations entre $C_1$ et ces variables sont négatives. Plus les valeurs de ces variables sont élevées (athlète lent), moins l’abscisse sur $C_1$ est élevée.

En particulier, `X100` est corrélée négativement avec $C_1$ : une valeur élevée de `X100` correspond à un athlète lent, dont l’abscisse sur $C_1$ est plus faible.

### Cartographie figurant dans le document

Le schéma place $C_1$ horizontalement, orienté vers la droite, et $C_2$ verticalement, orienté vers le haut.

| Position sur le schéma | $C_1$ négatif | $C_1$ positif |
| --- | --- | --- |
| $C_2$ positif | Lent, puissant | Rapide, puissant |
| $C_2$ négatif | Lent, faible | Rapide, faible |

## Page 2 — Axe $C_2$

Les variables `Shotput` et `Discus` contribuent le plus à la construction de l’axe $C_2$. Ces variables sont corrélées positivement avec $C_2$ : plus leurs valeurs sont élevées, plus l’ordonnée de l’athlète sur $C_2$ est élevée.

`Discus` correspond au lancer de disque : plus le disque est lancé loin (athlète puissant), plus l’ordonnée sur $C_2$ est élevée.

À partir de ces analyses, on peut réaliser la cartographie présentée à la page précédente.
