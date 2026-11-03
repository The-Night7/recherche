---
source: ING 1/S1 GM /DATA EXPLORATION/Chapitre 1 - Analyse Univariée/Calcule de Mediane.pdf
pages: 3
transcription: manuelle
verification: lecture intégrale de la source
---

# Calcul de médiane et écarts absolus

## Page 1 — Écarts moyen et médian

**Écart moyen (absolu).** Moyenne des valeurs absolues des différences entre les observations et leur moyenne $\bar x$ :

$$e_m^*=\frac1n\sum_{i=1}^n|x_i-\bar x|.$$

**Écart médian (absolu), selon la terminologie de la fiche.** Moyenne des valeurs absolues des différences entre les observations et leur médiane $M_e$ :

$$e_m=\frac1n\sum_{i=1}^n|x_i-M_e|.$$

L’interprétation de ces deux écarts est simple : les observations se situent en moyenne à $e_m^*$ unités de $\bar x$, respectivement à $e_m$ unités de $M_e$.

### Exemple

Série statistique : $\{1,2,3,4,5,10,11,12,15\}$ ; $n=9$.

$$\bar x=\frac{1+2+3+4+5+10+11+12+15}{9}=7.$$

La médiane est la cinquième observation de la série ordonnée :

$$M_e=x_{(n+1)/2}=x_5=5.$$

$$e_m^*=\frac{|1-7|+|2-7|+\cdots+|15-7|}{9}
=\frac{40}{9}\simeq4{,}44.$$

## Page 2 — Écart à la médiane et écart interquartile

$$e_m=\frac{|1-5|+|2-5|+\cdots+|15-5|}{9}
=\frac{38}{9}\simeq4{,}22.$$

Les observations de la série se trouvent donc, en moyenne, à 4,44 unités de leur moyenne $\bar x$ et à 4,22 unités de leur médiane $M_e$.

**Écart interquartile :** $Q_3-Q_1$, indicateur de dispersion. L’intervalle entre ces deux quartiles contient la moitié centrale des valeurs de la série. Plus cet écart est petit, plus les valeurs centrales de la série se concentrent autour de la médiane.

### Calcul de la médiane

Il faut d’abord ranger les observations par ordre croissant.

Pour un effectif total pair, la médiane usuelle est :

$$M_e=\frac{x_{n/2}+x_{n/2+1}}2.$$

Pour un effectif total impair :

$$M_e=x_{(n+1)/2}.$$

## Page 3 — Deux exemples

### Exemple 1 — Effectif pair

Observations : $1,10,4,3,7,6,5,8,2,1,0,9$.

Après rangement : $0,1,1,2,3,4,5,6,7,8,9,10$.

$n=12$ ; les deux valeurs centrales sont $x_6=4$ et $x_7=5$.

$$M_e=\frac{4+5}{2}=4{,}5.$$

Dans cet exemple, 50 % des observations sont inférieures à 4,5 et 50 % sont supérieures à 4,5.

### Exemple 2 — Effectif impair

Observations : $2,1,5,3,6,7,8,10,9,11,2$.

$n=11$ ; la médiane est la sixième observation :

$$x_{(n+1)/2}=x_{12/2}=x_6.$$

Après rangement : $1,2,2,3,5,6,7,8,9,10,11$.

$$\boxed{M_e=6.}$$

## Rectifications et conventions de transcription

- La fiche appelle « écart médian » la **moyenne** des écarts absolus à la médiane. La formule a été conservée : elle ne doit pas être confondue avec la médiane des écarts absolus, souvent appelée MAD.
- Les deux calculs numériques développés comportent dans la source un symbole $\sum$ superflu devant une somme déjà écrite ; il est supprimé ici. La valeur exacte de chaque résultat a été ajoutée pour rendre l’arrondi vérifiable.
- Page 2, le résultat relatif à la médiane est de nouveau nommé $e_m^*$ ; la notation $e_m$ de sa définition est rétablie.
- Page 2, la formule pour un effectif pair omet la division par 2 ; l’exemple de la page 3 la comporte bien. La formule générale est rectifiée ici.
- « Rang » est employé dans le manuscrit devant une valeur $x_k$ : le rang est $k$, la valeur est $x_k$.
- La dernière phrase de l’exemple 1 porte « 50 % sup à 50 % » ; le second seuil est rectifié en 4,5, conformément au calcul.
- L’exemple 2 porte « $n=11$, paire » ; 11 est impair. Les calculs de cet exemple utilisent bien le cas impair.
