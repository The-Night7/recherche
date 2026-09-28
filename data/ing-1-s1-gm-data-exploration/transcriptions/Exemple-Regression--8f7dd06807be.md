---
source: ING 1/S1 GM /DATA EXPLORATION/Chapitre 2 - Quantitative x Quantitative/Exemple-Regression.pdf
pages: 1
transcription: manuelle
---

# Data exploration — Exemple de régression taille-poids

## Données du tableau

Le document donne la taille $X$ et le poids $Y$ de dix enfants. Les unités ne sont pas précisées sur cette page.

| Enfant | Taille $X$ | Poids $Y$ | Poids prédit, tel qu'écrit | Résidu, tel qu'écrit |
| --- | --- | --- | --- | --- |
| 1 | 121 | 25 | 23,4 | 1,56 |
| 2 | 123 | 22 | 24,42 | −2,42 |
| 3 | 108 | 19 | 18,1 | 0,89 |
| 4 | 118 | 24 | 22,3 | 1,67 |
| 5 | 111 | 19 | 19,3 | −0,37 |
| 6 | 109 | 18 | 18,5 | −0,53 |
| 7 | 114 | 20 | 20,6 | −0,36 (lecture du manuscrit agrandi) |
| 8 | 103 | 15 | 16,004 | −1,004 |
| 9 | 110 | 20 | 18,96 | 1,04 |
| 10 | 115 | 21 | 21,05 | −0,05 |

La ligne imprimée « résidu centré et réduit » donne, dans l'ordre : $-1{,}23$ ; $-2{,}28$ ; $0{,}73$ ; $1{,}36$ ; $[\text{signe masqué}]\,0{,}29$ ; $-0{,}42$ ; $-0{,}5$ ; $-0{,}96$ ; $0{,}8$ ; $-0{,}04$. La deuxième valeur est surlignée. Le début de la cinquième valeur est recouvert dans le scan : son signe ne peut pas être confirmé à partir de ce fichier. Aucune valeur recalculée ne lui est substituée.

> **Incohérences de la source conservées :** les poids prédits du tableau ne correspondent pas tous à la droite affichée ci-dessous, et les arrondis des prédictions et résidus ne sont pas homogènes. Le premier résidu réduit est négatif dans la ligne imprimée alors que le résidu calculé en bas de page est positif. Ces nombres sont transcrits tels qu'ils figurent dans le document, sans les présenter comme un tableau recalculé.

## Calcul de la prédiction

La droite affichée est

$$\widehat Y=0{,}42X-27{,}38,$$

où $Y$ désigne le poids et $X$ la taille.

Pour le premier enfant,

$$\widehat y_1=0{,}42x_1-27{,}38
=0{,}42\times121-27{,}38=23{,}44.$$

$\widehat y_1=23{,}44$ est la valeur prédite ; $y_1=25$ est la valeur observée.

## Calcul du résidu

Le résidu est la différence entre la valeur observée et la valeur prédite :

$$e_i=y_i-\widehat y_i.$$

Pour le premier enfant,

$$e_1=25-23{,}44=1{,}56.$$
