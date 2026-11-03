# correction_examen_data_exploration2024-2025.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1rDoiNWDN2cmYblkcFlTp17BBIUdOFgvp) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                               Correction Complète
                          Examen Data Exploration
                       ING1 Mathématiques Appliquées
                                 CY Tech - 17 décembre 2024




Introduction
Ce document présente une correction détaillée de l'examen de Data Exploration portant sur
l'analyse du jeu de données Avocado Prices. Chaque section inclut des rappels de cours suivis
des solutions complètes.

Contents
1 Partie A - Statistiques univariées                                                             2
  1.1 Question 1 : Quartiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   2
  1.2 Question 2 : Étendue et écart interquartile . . . . . . . . . . . . . . . . . . . . . .    3
  1.3 Question 3 : Moustaches du boxplot . . . . . . . . . . . . . . . . . . . . . . . . .       3
  1.4 Question 4 : Valeurs atypiques . . . . . . . . . . . . . . . . . . . . . . . . . . . .     4
  1.5 Question 5 : Comparaison moyenne/médiane . . . . . . . . . . . . . . . . . . . .           4
2 Partie B - Statistiques Bivariées                                                               6
  2.1 B-1 : Analyse Quantitative Ö Quantitative . . . . . . . . . . . . . . . . . . . . .         6
      2.1.1 Question 1 : Coecient de corrélation linéaire . . . . . . . . . . . . . . . .        6
      2.1.2 Question 2 : Équation de la droite de régression . . . . . . . . . . . . . . .        7
      2.1.3 Question 3 : Prédiction et erreur . . . . . . . . . . . . . . . . . . . . . . .       8
      2.1.4 Question 4 : Coecient de détermination . . . . . . . . . . . . . . . . . .           9
      2.1.5 Question 5 : Valeurs atypiques (résidus) . . . . . . . . . . . . . . . . . . .        9
      2.1.6 Question 6 : Qualité du modèle . . . . . . . . . . . . . . . . . . . . . . . .       10
  2.2 B-2 : Analyse Quantitative Ö Qualitative . . . . . . . . . . . . . . . . . . . . . .       11
      2.2.1 Question 1 : Diérence de prix entre régions . . . . . . . . . . . . . . . . .       11
      2.2.2 Question 2 : Variances . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     12
      2.2.3 Question 3 : Rapport de corrélation . . . . . . . . . . . . . . . . . . . . .        13
  2.3 B-3 : Analyse Qualitative Ö Qualitative . . . . . . . . . . . . . . . . . . . . . . .      15
      2.3.1 Question 1 : Eectifs marginaux . . . . . . . . . . . . . . . . . . . . . . .        15
      2.3.2 Question 2 : Fréquences . . . . . . . . . . . . . . . . . . . . . . . . . . . .      16
      2.3.3 Question 3 : Prol moyen ligne . . . . . . . . . . . . . . . . . . . . . . . .       16
      2.3.4 Question 4 : Étude des prols lignes . . . . . . . . . . . . . . . . . . . . .       17
      2.3.5 Question 5 : Test du χ2 . . . . . . . . . . . . . . . . . . . . . . . . . . . .      19
3 Partie C - Analyse en Composantes Principales (ACP)                                        21
  3.1 Question 1 : Nombre et dimension des points . . . . . . . . . . . . . . . . . . . . 21
  3.2 Question 2 : Quantité d'information . . . . . . . . . . . . . . . . . . . . . . . . . 22
  3.3 Question 3 : Valeurs propres manquantes . . . . . . . . . . . . . . . . . . . . . . 23
  3.4 Question 4 : Inertie des deux premières composantes . . . . . . . . . . . . . . . . 24
  3.5 Question 5 : Poids des variables et observations . . . . . . . . . . . . . . . . . . . 25

                                                 1
~~~

## Page 2

~~~text
Correction - Data Exploration                                               ING1-GM - CY Tech


   3.6 Question 6 : Qualité de représentation en 2D . . . . . . . . . . . . . . . . . . . .     26
   3.7 Question 7 : Interprétation des liaisons entre variables . . . . . . . . . . . . . . .   28
   3.8 Question 8 : Calcul des composantes principales . . . . . . . . . . . . . . . . . . .    30




                                                2
~~~

## Page 3

~~~text
Correction - Data Exploration                                              ING1-GM - CY Tech


1     Partie A - Statistiques univariées

Données

Variable étudiée : Price (prix moyen d'un kg d'avocat en dollars)
   Résumé statistique :
     Min = 2.600

     Q1 (1st Qu.) = 3.930

     Médiane = 4.580

     Moyenne = 4.723

     Q3 (3rd Qu.) = 5.200

     Max = 7.760

1.1    Question 1 : Quartiles

    Rappel de cours
    Les quartiles divisent une série ordonnée en quatre parties égales :
        Q1 (premier quartile) : 25% des valeurs sont inférieures à Q1

        Q2 (médiane) : 50% des valeurs sont inférieures à Q2

        Q3 (troisième quartile) : 75% des valeurs sont inférieures à Q3

    Solution
    Identication :
        Q1 = 3.930 dollars

        Q2 (Médiane) = 4.580 dollars

        Q3 = 5.200 dollars

    Interprétation :
        25% des avocats ont un prix inférieur à 3.93 $/kg

        50% des avocats ont un prix inférieur à 4.58 $/kg (médiane)

        75% des avocats ont un prix inférieur à 5.20 $/kg

        Inversement, 25% des avocats sont vendus à plus de 5.20 $/kg




                                                3
~~~

## Page 4

~~~text
Correction - Data Exploration                                              ING1-GM - CY Tech


1.2   Question 2 : Étendue et écart interquartile

   Rappel de cours
   Mesures de dispersion :
       Étendue : E = xmax − xmin

       Écart interquartile (IQR) : IQR = Q3 − Q1

   L'IQR est plus robuste que l'étendue car il n'est pas aecté par les valeurs extrêmes.

   Solution
   Étendue :
                       E = xmax − xmin = 7.760 − 2.600 = 5.160 dollars
   Écart interquartile :
                       IQR = Q3 − Q1 = 5.200 − 3.930 = 1.270 dollars

   Interprétation :
       L'étendue de 5.16$ indique une forte variabilité des prix

       L'IQR de 1.27$ montre que 50% des prix centraux sont concentrés sur un intervalle
        de 1.27$

1.3   Question 3 : Moustaches du boxplot

   Rappel de cours
   Les moustaches (whiskers) du boxplot délimitent les valeurs non atypiques :
       Moustache inférieure : m = max(xmin , Q1 − 1.5 × IQR)

       Moustache supérieure : M = min(xmax , Q3 + 1.5 × IQR)

   Solution
   Calcul de la moustache inférieure m :
                Q1 − 1.5 × IQR = 3.930 − 1.5 × 1.270 = 3.930 − 1.905 = 2.025


                                m = max(2.600, 2.025) = 2.600
   La moustache inférieure est donc m = 2.600 dollars (= xmin ).
   Calcul de la moustache supérieure M :
                Q3 + 1.5 × IQR = 5.200 + 1.5 × 1.270 = 5.200 + 1.905 = 7.105


                                M = min(7.760, 7.105) = 7.105
   La moustache supérieure est donc M = 7.105 dollars.



                                               4
~~~

## Page 5

~~~text
Correction - Data Exploration                                                ING1-GM - CY Tech


1.4   Question 4 : Valeurs atypiques

   Rappel de cours
   Les valeurs atypiques (outliers) sont les observations situées en dehors de l'intervalle
   [m, M ] :

       Valeurs atypiques inférieures : x < m = Q1 − 1.5 × IQR

       Valeurs atypiques supérieures : x > M = Q3 + 1.5 × IQR

   Solution
   Intervalle des valeurs non atypiques : [m, M ] = [2.600, 7.105]
   Analyse :
       Valeurs atypiques inférieures : aucune (car xmin = 2.600 = m)

       Valeurs atypiques supérieures : toutes les valeurs > 7.105 dollars

   Comme xmax = 7.760 > 7.105, il existe au moins une valeur atypique supérieure.
   Conclusion : Oui, il y a des valeurs atypiques dans cette distribution. Ces valeurs
   correspondent à des avocats vendus à un prix exceptionnellement élevé (supérieur à
   7.10$/kg).

1.5   Question 5 : Comparaison moyenne/médiane


   Rappel de cours
   La comparaison entre la moyenne et la médiane renseigne sur la symétrie de la
   distribution :
       x̄ ≈ Médiane : distribution symétrique

       x̄ > Médiane : distribution asymétrique à droite (queue à droite)

       x̄ < Médiane : distribution asymétrique à gauche (queue à gauche)

   La médiane est plus robuste aux valeurs extrêmes que la moyenne.




                                              5
~~~

## Page 6

~~~text
Correction - Data Exploration                                                ING1-GM - CY Tech


   Solution
   Valeurs :
       Moyenne = 4.723 dollars

       Médiane = 4.580 dollars

   Comparaison :
                                  x̄ = 4.723 > 4.580 = Médiane
   Diérence : 4.723 − 4.580 = 0.143 dollars
   Interprétation :
   La moyenne est supérieure à la médiane, ce qui indique une asymétrie positive
   (distribution étalée vers la droite). Cela conrme la présence de valeurs élevées (atypiques)
   qui tirent la moyenne vers le haut.
   La présence de prix élevés (comme 7.76$) augmente la moyenne mais n'aecte pas la
   médiane, qui reste centrée sur la valeur typique de 4.58$.




                                                6
~~~

## Page 7

~~~text
Correction - Data Exploration                                         ING1-GM - CY Tech


2     Partie B - Statistiques Bivariées

2.1    B-1 : Analyse Quantitative           Ö    Quantitative

Données
Variables : X = Price et Y = Volume
   Statistiques :
     X̄ = 4.723, Ȳ = 522.7787

     s2X = 1.151, s2Y = 423428

     Cov(X, Y ) = 324.6

2.1.1 Question 1 : Coecient de corrélation linéaire
    Rappel de cours
    Le coecient de corrélation linéaire de Pearson mesure l'intensité de la liaison
    linéaire entre deux variables :
                                        Cov(X, Y )      Cov(X, Y )
                                   r=                  =q
                                         sX × sY          s2X × s2Y
    Propriétés :
        −1 ≤ r ≤ 1

        |r| ≈ 1 : forte corrélation linéaire

        |r| ≈ 0 : faible corrélation linéaire

        r > 0 : corrélation positive

        r < 0 : corrélation négative




                                                   7
~~~

## Page 8

~~~text
Correction - Data Exploration                                               ING1-GM - CY Tech


   Solution
   Calcul :
                                             √
                                      sX =       1.151 = 1.0728

                                           √
                                    sY =       423428 = 650.713

                                      324.6          324.6
                            r=                    =         = 0.465
                                 1.0728 × 650.713   698.089
   Interprétation :
   r = 0.465 indique une corrélation linéaire positive modérée entre le prix et le volume
   de vente des avocats.
   Plus précisément :
       Lorsque le prix augmente, le volume tend à augmenter également

       La liaison n'est pas très forte (46.5% d'intensité)

       Ce résultat peut sembler contre-intuitif économiquement (loi de la demande), mais
          peut s'expliquer par des facteurs confondants (qualité, saison, région)


2.1.2 Question 2 : Équation de la droite de régression
   Rappel de cours
   La droite de régression de Y en fonction de X a pour équation :

                                             Ŷ = aX + b
   où :
       a = Covs(X,Y
                 2
                     )
                       (pente)
                  X


       b = Ȳ − aX̄ (ordonnée à l'origine)

   Cette droite minimise la somme des carrés des résidus (méthode des moindres carrés).




                                                   8
~~~

## Page 9

~~~text
Correction - Data Exploration                                             ING1-GM - CY Tech


   Solution
   Calcul de la pente a :
                                     Cov(X, Y )       324.6
                                a=                =         = 282.015
                                        s2X           1.151
   Calcul de l'ordonnée à l'origine b :

        b = Ȳ − aX̄ = 522.7787 − 282.015 × 4.723 = 522.7787 − 1331.877 = −809.098
   Équation de la droite de régression :

                                     Ŷ = 282.015X − 809.098
   Interprétation :
       La pente a = 282.015 : une augmentation de 1$ du prix est associée à une
        augmentation de 282 tonnes du volume vendu
       L'ordonnée b = −809.098 n'a pas de sens physique (volume négatif pour prix nul)


2.1.3 Question 3 : Prédiction et erreur
   Solution
   a) Valeur estimée pour X = 3.92 :

              Ŷ = 282.015 × 3.92 − 809.098 = 1105.499 − 809.098 = 296.401 tonnes
   b) Erreur d'estimation (résidu) :

                    e = Yobservé − Ŷ = 27.357 − 296.401 = −269.044 tonnes
   Interprétation :
   L'erreur est de −269 tonnes, ce qui signie que le modèle surestime largement le volume
   de vente pour ce prix. Le volume observé (27.36 tonnes) est beaucoup plus faible que prévu
   (296.4 tonnes).
   Cette erreur importante suggère que le modèle linéaire simple ne capture pas bien la
   relation entre prix et volume.




                                                  9
~~~

## Page 10

~~~text
Correction - Data Exploration                                                 ING1-GM - CY Tech


2.1.4 Question 4 : Coecient de détermination
   Rappel de cours
   Le coecient de détermination R2 mesure la qualité de l'ajustement :
                                                   Cov(X, Y )
                                                               2
                                     2    2
                                   R =r =
                                                      sX × sY
   Interprétation :
       0 ≤ R2 ≤ 1

       R2 = proportion de variance de Y expliquée par X

       R2 = 1 : ajustement parfait

       R2 = 0 : X n'explique rien de Y

   Solution
   Calcul :

                                  R2 = r2 = (0.465)2 = 0.216
   Interprétation :
   R2 = 0.216 = 21.6%
   Le prix explique seulement 21.6% de la variabilité du volume de vente des avocats.
   Autrement dit :
       21.6% de la variance du volume est expliquée par le modèle linéaire avec le prix

       78.4% de la variance reste inexpliquée

   Ce faible R2 conrme que le modèle linéaire simple prix-volume est peu performant.

2.1.5 Question 5 : Valeurs atypiques (résidus)
   Rappel de cours
   Les résidus standardisés (ou centrés-réduits) permettent d'identier les valeurs
   atypiques :
                                                      ei
                                              ri∗ =
                                                      se
   où ei = Yi − Ŷi et se est l'écart-type des résidus.
   Règle : Un résidu est considéré atypique si |ri∗ | > 2 (ou parfois > 3).




                                                10
~~~

## Page 11

~~~text
Correction - Data Exploration                                                ING1-GM - CY Tech


   Solution
   Résumé des résidus standardisés :
       Min = -1.352

       Q1 = -0.883

       Médiane = -0.385

       Moyenne = 0.001

       Q3 = 0.965

       Max = 2.573

   Analyse :
   La valeur maximale est 2.573 > 2, donc oui, il existe au moins une valeur atypique.
   Cette observation a un résidu standardisé de 2.573, ce qui signie que l'erreur de prédiction
   pour cette observation est 2.57 fois plus grande que l'erreur typique.
   Remarque : La médiane négative (-0.385) suggère que le modèle surestime souvent les
   volumes.

2.1.6 Question 6 : Qualité du modèle
   Solution
   Évaluation du modèle :
   Ce modèle est de qualité médiocre pour plusieurs raisons :

     1. Faible R2 : Seulement 21.6% de variance expliquée
     2. Corrélation modérée : r = 0.465, pas très forte
     3. Erreurs importantes : L'exemple montre une erreur de 269 tonnes
     4. Valeurs atypiques : Présence de résidus > 2 écarts-types

   Améliorations possibles :

       Modèle multivarié : Inclure d'autres variables explicatives (Type, Region, Year,
         Total.Bags)
       Transformation : Tester une transformation logarithmique si la relation n'est pas
         linéaire
       Segmentation : Créer des modèles séparés par région ou par type d'avocat

       Variables d'interaction : Tester les interactions PrixÖRegion ou PrixÖType

       Modèle polynomial : Tester une régression polynomiale (degré 2 ou 3)

   La relation entre prix et volume est probablement plus complexe qu'une simple relation
   linéaire, d'où la nécessité d'approches plus sophistiquées.




                                                11
~~~

## Page 12

~~~text
Correction - Data Exploration                                           ING1-GM - CY Tech


2.2   B-2 : Analyse Quantitative       Ö   Qualitative

Données
Variable quantitative : Price
   Variable qualitative : Region (Center, North, South, West)
   Table ANOVA :
                        Source  Df Sum Sq Mean Sq F value
                        Region   3   2.383  0.79423 0.685
                        Résidus 126 146.101 1.15953
   p-value = 0.5628

2.2.1 Question 1 : Diérence de prix entre régions
   Rappel de cours
   Le boxplot permet de comparer visuellement les distributions de plusieurs groupes :
       Comparaison des médianes

       Comparaison des dispersions (IQR)

       Détection de chevauchements

   Le test ANOVA teste l'hypothèse :
       H0 : Les moyennes sont égales pour tous les groupes

       H1 : Au moins une moyenne dière




                                             12
~~~

## Page 13

~~~text
Correction - Data Exploration                                             ING1-GM - CY Tech


   Solution
   Analyse du boxplot :
   D'après le graphique :
       Center : Médiane ≈ 4.8, IQR modéré, symétrique

       North : Médiane ≈ 4.9, IQR petit, symétrique

       South : Médiane ≈ 4.5, IQR important, asymétrique (valeurs élevées)

       West : Médiane ≈ 4.4, IQR très important, large dispersion, valeur atypique haute

   Observations visuelles :
       Les médianes sont relativement proches (entre 4.4 et 4.9)

       Fort chevauchement des boîtes et des moustaches

       Diérences visuelles limitées

   Test statistique :
   ANOVA : F = 0.685 avec p-value = 0.5628
   Comme p-value = 0.5628 > 0.05, on ne rejette pas H0 .
   Conclusion :
   Non, il n'y a pas de diérence signicative de prix des avocats entre les régions au
   seuil de 5%. Les variations observées sur le boxplot peuvent être attribuées au hasard de
   l'échantillonnage.

2.2.2 Question 2 : Variances
   Rappel de cours
   Dans l'ANOVA à un facteur, la variance totale se décompose :

              Variance totale = Variance inter-groupes + Variance intra-groupes

       Variance inter-groupes : variabilité entre les moyennes des groupes
                                                     SCEinter
                                         s2inter =
                                                      k−1

       Variance intra-groupes : variabilité à l'intérieur des groupes
                                                     SCEintra
                                         s2intra =
                                                      n−k

       Variance totale :
                                                     SCEtot
                                           s2tot =
                                                      n−1
   où k = nombre de groupes, n = eectif total.




                                              13
~~~

## Page 14

~~~text
Correction - Data Exploration                                           ING1-GM - CY Tech


   Solution
   Données de la table ANOVA :
       k = 4 groupes (régions)

       n = 130 observations (Df total = 3 + 126 = 129, donc n = 130)

       SCEinter = 2.383

       SCEintra = 146.101

   Variance inter-groupes :
                                            SCEinter   2.383
                                s2inter =            =       = 0.794
                                             k−1         3
   C'est la valeur "Mean Sq" pour Region.
   Variance intra-groupes :
                                          SCEintra   146.101
                             s2intra =             =         = 1.160
                                           n−k         126
   C'est la valeur "Mean Sq" pour Residuals.
   Variance totale :

                 SCEtot = SCEinter + SCEintra = 2.383 + 146.101 = 148.484

                                          SCEtot   148.484
                                s2tot =          =         = 1.151
                                           n−1       129
   Résumé :
       Variance inter-groupes = 0.794

       Variance intra-groupes = 1.160

       Variance totale = 1.151


2.2.3 Question 3 : Rapport de corrélation
   Rappel de cours
   Le rapport de corrélation η 2 (êta carré) mesure la proportion de variance expliquée
   par le facteur :
                                     SCEinter   Variance expliquée
                             η2 =             =
                                     SCEtot      Variance totale
   Interprétation :
       0 ≤ η2 ≤ 1

       η 2 proche de 0 : le facteur explique peu la variable

       η 2 proche de 1 : le facteur explique bien la variable

   Le rapport de corrélation est l'équivalent du R2 pour une relation Quantitative Ö
   Qualitative.


                                                   14
~~~

## Page 15

~~~text
Correction - Data Exploration                                           ING1-GM - CY Tech


   Solution
   Calcul :
                                     SCEinter    2.383
                              η2 =            =         = 0.0160
                                     SCEtot     148.484
   Interprétation :
   η 2 = 0.0160 = 1.6%
   La région géographique explique seulement 1.6% de la variabilité du prix des avocats.
   Autrement dit :
       La région a un eet négligeable sur le prix

       98.4% de la variance du prix est due à d'autres facteurs

       Il y a très peu de diérence de prix entre les régions

   Ce très faible rapport de corrélation conrme les conclusions de l'ANOVA : la région ne
   permet pas d'expliquer les variations de prix des avocats.




                                               15
~~~

## Page 16

~~~text
Correction - Data Exploration                                          ING1-GM - CY Tech


2.3   B-3 : Analyse Qualitative        Ö   Qualitative

Données
Table de contingence (Type Ö Region) :
                                        Center North South West
                        Conventional      8     20    22    34
                        Organic           4      4     7    31

2.3.1 Question 1 : Eectifs marginaux
   Rappel de cours
   Les eectifs marginaux sont les totaux par ligne et par colonne :
       Eectifs marginaux lignes : ni· =
                                              P
                                                   j nij

       Eectifs marginaux colonnes : n·j =
                                                    P
                                                       i nij

       Eectif total : n = i j nij
                           P P


   Solution
   Calcul des eectifs marginaux :
   Par ligne (Type) :
       Conventional : n1· = 8 + 20 + 22 + 34 = 84

       Organic : n2· = 4 + 4 + 7 + 31 = 46

   Par colonne (Region) :
       Center : n·1 = 8 + 4 = 12

       North : n·2 = 20 + 4 = 24

       South : n·3 = 22 + 7 = 29

       West : n·4 = 34 + 31 = 65

   Eectif total :
                                       n = 84 + 46 = 130
   Table complète avec marges :
                                    Center North South West Total
                     Conventional     8     20    22    34   84
                     Organic          4      4     7    31   46
                     Total            12    24    29    65   130




                                              16
~~~

## Page 17

~~~text
Correction - Data Exploration                                                 ING1-GM - CY Tech


2.3.2 Question 2 : Fréquences
   Rappel de cours
   Dans une table de contingence :
       Fréquence conjointe : fij = nij
                                           n


       Fréquence marginale colonne : f·j = n·j
                                                       n


       Fréquence conditionnelle : fi|j = nij (fréquence de la ligne i sachant la colonne
                                                  n
                                           ·j
        j)

   Solution
   Calcul de f12 (fréquence conjointe) :
   f12 = fréquence de (Conventional, North)
                                         n12   20
                                f12 =        =     = 0.154 = 15.4%
                                          n    130
   Interprétation : 15.4% des avocats sont conventionnels et vendus dans le Nord.
   Calcul de f·1 (fréquence marginale) :
   f·1 = fréquence marginale de Center
                                         n·1   12
                                f·1 =        =     = 0.092 = 9.2%
                                          n    130
   Interprétation : 9.2% des avocats sont vendus dans la région Center.
   Calcul de f2|1 (fréquence conditionnelle) :
   f2|1 = fréquence d'Organic sachant Center
                                         n21   4
                                f2|1 =       =    = 0.333 = 33.3%
                                         n·1   12
   Interprétation : Parmi les avocats vendus dans le Center, 33.3% sont biologiques
   (organic).

2.3.3 Question 3 : Prol moyen ligne
   Rappel de cours
   Le prol moyen ligne (ou prol marginal ligne) représente la distribution des colonnes
   dans l'ensemble de l'échantillon :

                             Prol moyen ligne = (f·1 , f·2 , . . . , f·J )
   où f·j = nn·j .
   C'est la distribution de référence pour comparer les prols lignes.




                                                  17
~~~

## Page 18

~~~text
Correction - Data Exploration                                                    ING1-GM - CY Tech


   Solution
   Calcul du prol moyen ligne :
                                             12
                                     f·1 =       = 0.092 = 9.2%
                                             130
                                              24
                                    f·2 =        = 0.185 = 18.5%
                                             130
                                              29
                                    f·3 =        = 0.223 = 22.3%
                                             130
                                              65
                                    f·4 =        = 0.500 = 50.0%
                                             130
   Prol moyen ligne :

                                     (0.092, 0.185, 0.223, 0.500)
   ou en pourcentages : (9.2%, 18.5%, 22.3%, 50.0%)
   Interprétation :
   Dans l'ensemble de l'échantillon, la distribution des régions est :
       9.2% Center

       18.5% North

       22.3% South

       50% West (région la plus représentée)


2.3.4 Question 4 : Étude des prols lignes
   Rappel de cours
   Les prols lignes représentent la distribution conditionnelle des colonnes pour chaque
   ligne :

                                Prol ligne i = fi|1 , fi|2 , . . . , fi|J
                                                                             

   où fi|j = nniji· .
   Indépendance : Les deux variables sont indépendantes si tous les prols lignes sont
   égaux au prol moyen ligne.




                                                    18
~~~

## Page 19

~~~text
Correction - Data Exploration                                         ING1-GM - CY Tech


   Solution
   a) Tableau des prols lignes :
   Pour chaque type, on calcule la proportion de chaque région :
   Ligne Conventional :
       Center : 84
                 8
                    = 0.095 = 9.5%

       North : 20
                84 = 0.238 = 23.8%

       South : 22
                84 = 0.262 = 26.2%

       West : 84
               34
                  = 0.405 = 40.5%

   Ligne Organic :
       Center : 46
                 4
                    = 0.087 = 8.7%

       North : 46
                4
                   = 0.087 = 8.7%

       South : 46
                7
                   = 0.152 = 15.2%

       West : 46
               31
                  = 0.674 = 67.4%

   Table des prols lignes :
                                    Center North South West Total
                    Conventional    0.095 0.238 0.262 0.405 1.000
                    Organic         0.087 0.087 0.152 0.674 1.000
                    Prol moyen     0.092 0.185 0.223 0.500 1.000
   b) Comparaison avec le prol moyen :

                                  Center North South West
                     Conventional 9.5% 23.8% 26.2% 40.5%
                     Organic       8.7%  8.7% 15.2% 67.4%
                     Prol moyen 9.2% 18.5% 22.3% 50.0%
                     Écart Conv. +0.3% +5.3% +3.9% -9.5%
                     Écart Org.   -0.5% -9.8% -7.1% +17.4%
   Observations :

       Center : Prols similaires au prol moyen (≈ 9% pour tous)

       North :

            Conventional : 23.8% (surreprésentation)
            Organic : 8.7% (sous-représentation)
            Écart important au prol moyen (18.5%)
       South :

            Conventional : 26.2% (légère surreprésentation)
            Organic : 15.2% (sous-représentation)
       West :

            Conventional : 40.5% (sous-représentation par rapport à 50%)
            Organic : 67.4% (forte surreprésentation)
                                             19
            Écarts importants au prol moyen

   c) Conclusion sur le lien :
~~~

## Page 20

~~~text
Correction - Data Exploration                                      ING1-GM - CY Tech


2.3.5 Question 5 : Test du χ2
   Rappel de cours
   Le test du χ2 d'indépendance teste :
       H0 : Les deux variables sont indépendantes

       H1 : Les deux variables sont liées

   Statistique de test :
                                             X (nij − nth
                                                       ij )
                                                           2
                                       2
                                      χ =
                                             i,j
                                                        nth
                                                         ij

   où nth
       ij =
            ni· ×n·j
                n    (eectif théorique sous H0 ).
   Règle de décision :
   On rejette H0 si χ2obs > χ2α (ddl) avec ddl = (I − 1)(J − 1).
   Conditions d'application :
       Tous les eectifs théoriques ≥ 5

       Si non respecté, le test n'est pas able




                                                   20
~~~

## Page 21

~~~text
Correction - Data Exploration                                         ING1-GM - CY Tech


   Solution
   a) Nom du test :
   Le test à eectuer est le test du χ2 d'indépendance (ou test du khi-deux).
   b) Tableau des eectifs théoriques :
   Sous l'hypothèse d'indépendance :

                                         nth
                                                 ni· × n·j
                                          ij =
                                                     n
   Calculs :

       nth  84×12  1008
         11 = 130 = 130 = 7.75

       nth  84×24  2016
         12 = 130 = 130 = 15.51

       nth  84×29  2436
         13 = 130 = 130 = 18.74

       nth  84×65  5460
         14 = 130 = 130 = 42.00

       nth  46×12  552
         21 = 130 = 130 = 4.25

       nth  46×24  1104
         22 = 130 = 130 = 8.49

       nth  46×29  1334
         23 = 130 = 130 = 10.26

       nth  46×65  2990
         24 = 130 = 130 = 23.00

   Table des eectifs théoriques :
                                         Center North South West
                        Conventional      7.75  15.51 18.74 42.00
                        Organic           4.25   8.49 10.26 23.00
   c) Test d'indépendance :
   Données :
       Distance du χ2 observée : χ2obs = 9.6106

       Degrés de liberté : ddl = (2 − 1) × (4 − 1) = 3

       Valeur critique au seuil 5% : χ20.05 (3) = 7.82

   Décision :

                                χ2obs = 9.6106 > 7.82 = χ20.05 (3)
   On rejette H0 au seuil de 5%.
   Conclusion :
   Les variables Type et Region sont signicativement liées. Il existe une dépendance
   statistique entre le type d'avocat (conventional/organic) et la région de vente.
   Plus précisément :
       Les avocats biologiques sont sur-représentés dans l'Ouest

       Les avocats conventionnels sont mieux répartis géographiquement

   d) Fiabilité du test :
   Vérication des conditions d'application :
   Tous les eectifs théoriques sont ≥ 5 :
       Le plus petit eectif théorique est 4.2521

       4.25 < 5 : condition non respectée !
~~~

## Page 22

~~~text
Correction - Data Exploration                                              ING1-GM - CY Tech


3     Partie C - Analyse en Composantes Principales (ACP)
Données
ACP normalisée sur 7 variables quantitatives :
     Price, Volume, Hass, Fuerte, Bacon, Total.Bags, Year

    Table des valeurs propres :
                                   Valeur propre % variance % cumulé
                         Comp 1        4.367       62.38      62.38
                         Comp 2        1.492       21.32      83.70
                         Comp 3         ???        10.35     94.06
                         Comp 4         ???         3.68     97.74
                         Comp 5        0.119        1.70      99.44
                         Comp 6        0.039        0.56     100.00
                         Comp 7         ≈0          ≈0       100.00
3.1    Question 1 : Nombre et dimension des points

    Rappel de cours
    Dans une ACP :
        Chaque observation (individu) est représentée par un point

        Ces points sont initialement dans Rp où p = nombre de variables

        L'ACP projette ces points dans un espace de dimension réduite (les composantes
         principales)

    Solution
    Nombre de points :
    Le jeu de données contient 130 observations (jours de vente), donc il y a 130 points dans
    le nuage.
    Dimension de l'espace :
    Les points sont représentés en dimension p = 7 (le nombre de variables quantitatives).
    Espace initial : R7
    Chaque point (jour de vente) est caractérisé par 7 coordonnées : (Price, Volume, Hass,
    Fuerte, Bacon, Total.Bags, Year).




                                                 22
~~~

## Page 23

~~~text
Correction - Data Exploration                                               ING1-GM - CY Tech


3.2   Question 2 : Quantité d'information

   Rappel de cours
   La quantité d'information (ou inertie totale) dans une ACP normalisée mesure la
   variabilité totale du nuage de points.
   Dénition :
   L'inertie totale est la somme des variances des variables centrées-réduites :
                                          p                    p
                                                Var(Zj ) =
                                          X                    X
                                 Itot =                              1=p
                                          j=1                  j=1

   où Zj sont les variables normalisées.
   Calcul pratique :
   L'inertie totale = trace de la matrice de corrélation = somme des valeurs propres.
                                                   p
                                                   X
                                          Itot =         λk = p
                                                   k=1

   Dans une ACP normalisée, l'inertie totale est toujours égale au nombre de variables.

   Solution
   Dénition :
   La quantité d'information contenue dans le nuage de points est mesurée par l'inertie
   totale (ou variance totale).
   Matrice utilisée :
   L'inertie est calculée à partir de la matrice de corrélation R des variables.
   Dans une ACP normalisée :
       On part de la matrice de corrélation (et non de covariance)

       Les variables sont centrées-réduites

       Chaque variable a une variance de 1

   Calcul :
                                                         p
                                Itot = trace(R) =
                                                         X
                                                               λk = p = 7
                                                         k=1

   Où λk sont les valeurs propres de la matrice de corrélation.
   Interprétation :
   Dans une ACP normalisée, l'inertie totale vaut toujours le nombre de variables (ici 7), car
   chaque variable normalisée contribue pour 1 à l'inertie totale.




                                                   23
~~~

## Page 24

~~~text
Correction - Data Exploration                                       ING1-GM - CY Tech


3.3   Question 3 : Valeurs propres manquantes

   Rappel de cours
   Dans une ACP, les valeurs propres satisfont :
                                      p
                                      X
                                             λk = Itot = p
                                       k=1

   Le pourcentage de variance expliquée par la composante k est :
                                    λk           λk
                                         × 100 =    × 100
                                    Itot         p
   En ACP normalisée : λpk × 100




                                                24
~~~

## Page 25

~~~text
Correction - Data Exploration                                              ING1-GM - CY Tech


   Solution
   Méthode 1 : À partir des pourcentages de variance
   Composante 3 :
   Le pourcentage de variance est 10.35%
                                            10.35
                                     λ3 =         × 7 = 0.7245
                                             100
   Composante 4 :
   Le pourcentage de variance est 3.68%
                                            3.68
                                     λ4 =        × 7 = 0.2576
                                            100
   Méthode 2 : Vérication par la somme
                                             7
                                             X
                                                    λk = 7
                                             k=1

                       4.367 + 1.492 + λ3 + λ4 + 0.119 + 0.039 + 0 = 7


                                 λ3 + λ4 = 7 − 6.017 = 0.983
   Avec λ3 = 0.725 et λ4 = 0.258 :

                                      0.725 + 0.258 = 0.983
   Valeurs propres manquantes :
                                     λ3 = 0.725 et λ4 = 0.258

   Table complète :
                                 Valeur propre % variance % cumulé
                      Comp 1         4.367       62.38      62.38
                      Comp 2         1.492       21.32      83.70
                      Comp 3         0.725       10.35     94.06
                      Comp 4         0.258        3.68      97.74
                      Comp 5         0.119        1.70      99.44
                      Comp 6         0.039        0.56     100.00
                      Comp 7          ≈0          ≈0       100.00


3.4   Question 4 : Inertie des deux premières composantes

   Rappel de cours
   Le pourcentage d'inertie cumulée des k premières composantes mesure la qualité de
   représentation dans l'espace réduit à k dimensions :
                                            Pk
                                             i=1 λi
                                                         × 100
                                             Itot
   C'est la proportion de variance totale expliquée par les k premiers axes.



                                                    25
~~~

## Page 26

~~~text
Correction - Data Exploration                                           ING1-GM - CY Tech


   Solution
   Lecture directe :
   D'après le tableau, le pourcentage cumulé pour les deux premières composantes est :

                                           83.70%
   Vérication par calcul :
                λ1 + λ2         4.367 + 1.492         5.859
                        × 100 =               × 100 =       × 100 = 83.70%
                   7                  7                 7
   Interprétation :
   Les deux premières composantes principales contiennent 83.7% de l'information totale.
   Cela signie :
       Une représentation en 2D capture plus de 83% de la variabilité totale

       On perd seulement 16.3% d'information en passant de 7 à 2 dimensions

       C'est un très bon taux de compression

       Le plan factoriel (C1, C2) est susant pour une analyse pertinente

   Règle pratique : Un taux > 70-80% est généralement considéré comme satisfaisant pour
   une ACP.

3.5   Question 5 : Poids des variables et observations

   Rappel de cours
   Dans une ACP normalisée :
   Poids des variables :
   Chaque variable j a un poids :
                                                   1
                                           wj =
                                                   p
   où p = nombre de variables.
   Poids des observations :
   Chaque observation i a un poids :
                                                   1
                                           wi =
                                                   n
   où n = nombre d'observations.
   Ces poids sont uniformes car on utilise la métrique standard.




                                              26
~~~

## Page 27

~~~text
Correction - Data Exploration                                                      ING1-GM - CY Tech


   Solution
   Poids de chaque variable :
   Dans une ACP normalisée, toutes les variables ont le même poids :
                                          1  1
                                  wj =      = ≈ 0.143 = 14.3%
                                          p  7
   Chaque variable contribue également à l'analyse.
   Poids de chaque observation :
   Toutes les observations ont le même poids :
                                       1    1
                                wi =     =     ≈ 0.0077 = 0.77%
                                       n   130
   Justication :
   L'ACP normalisée utilise des poids uniformes pour :
       Traiter toutes les variables de façon équitable (d'où la normalisation)

       Donner la même importance à chaque observation

       Éviter qu'une variable ou observation domine l'analyse


3.6   Question 6 : Qualité de représentation en 2D

   Rappel de cours
   La qualité de représentation d'une variable en dimension k est mesurée par le cos2
   (cosinus carré) :
                                               cor2 (xj , Ck )
                           cos2 (xj , Ck ) =                   = cor2 (xj , Ck )
                                                 Var(xj )
   En dimension 2, la qualité totale est :

                            cos2total (xj ) = cos2 (xj , C1 ) + cos2 (xj , C2 )
   Interprétation :
       cos2 proche de 1 : variable bien représentée

       cos2 proche de 0 : variable mal représentée

       Seuil pratique : cos2 ≥ 0.5 ou 0.7




                                                    27
~~~

## Page 28

~~~text
Correction - Data Exploration                                          ING1-GM - CY Tech


   Solution
   Calcul des qualités de représentation en 2D :
   On additionne les cos2 des dimensions 1 et 2 :
                       Variable   Dim.1 Dim.2 Total (Dim.1+2)
                       Price      0.287 0.098      0.385
                       Volume     0.935 0.041      0.976
                       Hass       0.804 0.089      0.893
                       Fuerte     0.844 0.085      0.929
                       Bacon      0.689 0.234      0.923
                       Total.Bags 0.574 0.310      0.884
                       Year       0.233 0.635      0.868
   Analyse :
   Variables bien représentées (cos2 > 0.85) :
       Volume : 97.6% (excellente représentation, presque entièrement sur C1)

       Hass : 89.3% (très bonne représentation)

       Fuerte : 92.9% (très bonne représentation)

       Bacon : 92.3% (très bonne représentation)

       Total.Bags : 88.4% (très bonne représentation)

       Year : 86.8% (bonne représentation, surtout sur C2)

   Variable mal représentée :
       Price : 38.5% seulement

       Seulement 38.5% de sa variance est expliquée par le plan (C1, C2)

       61.5% de son information se trouve sur les autres axes

   Conclusion :
   Non, toutes les variables ne sont pas bien représentées en dimension 2.
   La variable Price est mal représentée dans le plan factoriel (C1, C2). Pour bien
   comprendre le comportement du prix, il faudrait examiner les composantes suivantes
   (notamment C3 où cos2 = 0.607, cf. tableau).
   Les 6 autres variables sont excellemment représentées (> 85%).




                                             28
~~~

## Page 29

~~~text
Correction - Data Exploration                                    ING1-GM - CY Tech


3.7   Question 7 : Interprétation des liaisons entre variables

   Rappel de cours
   Sur le cercle des corrélations :
   Proximité angulaire :
       Angle ≈ 0 : corrélation positive forte

       Angle ≈ 90 : variables indépendantes

       Angle ≈ 180 : corrélation négative forte

   Distance au centre :
       Proche du cercle : bien représentée

       Proche du centre : mal représentée

   Position sur les axes :
       Variables alignées avec C1 : fortement corrélées à C1

       Variables alignées avec C2 : fortement corrélées à C2




                                                 29
~~~

## Page 30

~~~text
Correction - Data Exploration                                              ING1-GM - CY Tech


   Solution
   Analyse du graphique PCA :
   Axe 1 (62.38% de variance) - "Volume de vente" :
   Variables fortement corrélées positivement (à droite, angle faible) :
       Volume, Hass, Fuerte, Bacon, Total.Bags

       Ces 5 variables forment un groupe compact

       Elles sont très corrélées entre elles

   Interprétation C1 : Cet axe représente le volume global de vente. Les avocats avec un
   fort volume total ont également de forts volumes pour chaque variété et beaucoup de sacs
   vendus.
   Variable négativement corrélée (à gauche) :
       Price : opposé aux variables de volume

   Observation : Prix et volume sont négativement corrélés sur C1 (angle ≈ 180),
   contrairement à ce que suggérait la corrélation brute (0.465). Cela indique une relation
   plus complexe.
   Axe 2 (21.32% de variance) - "Dimension temporelle" :
   Variable dominante :
       Year : seule variable fortement corrélée à C2 (en haut)

   Interprétation C2 : Cet axe capture l'évolution temporelle (année de vente).
   Variable secondaire :
       Total.Bags : corrélation modérée avec C2

   Groupes de variables identiés :

     1. Groupe "Volume" : Volume, Hass, Fuerte, Bacon
            Forte inter-corrélation
            Représentent diérentes facettes du volume total
            Les volumes des diérentes variétés évoluent ensemble

     2. Total.Bags :
            Corrélé au groupe Volume (angle ≈ 30)
            Mais aussi légèrement corrélé à Year (composante sur C2)
            Variable "pont" entre volume et année

     3. Price :
            Relativement indépendant des autres (proche du centre)
            Légère corrélation négative avec le volume
            Mal représenté dans ce plan

     4. Year :
            Orthogonal au groupe Volume (angle ≈ 90)
            Indépendant des volumes des variétés
            Capture la dimension temporelle
                                                30
   Conclusions principales :

       Les diérentes variétés (Hass, Fuerte, Bacon) sont fortement corrélées : quand on
~~~

## Page 31

~~~text
Correction - Data Exploration                                               ING1-GM - CY Tech


3.8   Question 8 : Calcul des composantes principales

   Rappel de cours
   Les composantes principales sont calculées comme suit :
   Principe :
      1. Normalisation : Centrer-réduire les variables
                                                    Xj − X̄j
                                            Zj =
                                                       sj

      2. Matrice de corrélation : Calculer R = Cor(Z)
      3. Diagonalisation : Trouver les valeurs propres λk et vecteurs propres uk de R
      4. Composantes principales : Les nouvelles coordonnées sont
                                                        p
                                                        X
                                       Ck = Z · uk =          zj ujk
                                                        j=1


   Propriétés des composantes :
       C1 maximise la variance projetée (= λ1 )

       Ck maximise la variance sous contrainte d'orthogonalité avec C1 , . . . , Ck−1

       Les Ck sont orthogonales (non corrélées)

       Var(Ck ) = λk

   Interprétation géométrique :
   Les composantes principales sont les axes d'inertie maximale du nuage de points. C1 est
   la direction de plus grande variance, C2 la direction orthogonale de deuxième plus grande
   variance, etc.




                                               31
~~~

## Page 32

~~~text
Correction - Data Exploration                                                     ING1-GM - CY Tech


   Solution
   Processus de calcul (sans calculs explicites) :
   Étape 1 : Normalisation des données
   On transforme chaque variable en variable centrée-réduite :
                                                   Xj − X̄j
                                            Zj =
                                                      sj

       Chaque variable a maintenant une moyenne de 0 et un écart-type de 1

       Cela permet de traiter toutes les variables équitablement

       Nécessaire car Price (en $) et Volume (en tonnes) n'ont pas les mêmes unités

   Étape 2 : Calcul de la matrice de corrélation
   On calcule la matrice de corrélation R des variables normalisées :
                                                    1 T
                                             R=       Z Z
                                                    n
   Cette matrice 7 × 7 contient les corrélations entre toutes les paires de variables.
   Étape 3 : Diagonalisation de la matrice de corrélation
   On résout le problème aux valeurs propres :
                                           R · uk = λk · uk

   Cela donne :
       7 valeurs propres λ1 ≥ λ2 ≥ · · · ≥ λ7 ≥ 0

       7 vecteurs propres orthonormés u1 , u2 , . . . , u7

   Étape 4 : Construction des composantes principales
   Pour chaque observation i et chaque composante k :
                                                  7
                                                  X
                                          Cik =          zij · ujk
                                                   j=1

   C'est la projection de l'observation i sur le vecteur propre uk .
   Propriétés des axes obtenus :
   Composante principale 1 (C1 ) :
       Direction de variance maximale

       Combine les 7 variables selon les poids u1 = (u11 , u21 , . . . , u71 )

       Variance de C1 = λ1 = 4.367

       Explique 62.38% de la variance totale

   Composante principale 2 (C2 ) :
       Direction de variance maximale orthogonale à C1

       Combine les 7 variables selon les poids u2

       Variance de C2 = λ2 = 1.492

       Explique 21.32% de la variance totale

       C1 et C2 sont non corrélées                 32

   Interprétation géométrique :
~~~

## Page 33

~~~text
Correction - Data Exploration                                               ING1-GM - CY Tech


Conclusion générale

Synthèse de l'analyse

L'analyse complète du jeu de données Avocado Prices a révélé plusieurs résultats importants :
   Statistiques univariées :
    Le prix moyen des avocats est de 4.72$, avec une distribution asymétrique vers la droite

    Présence de prix exceptionnellement élevés (> 7.10$)

   Analyses bivariées :
    La relation linéaire simple entre prix et volume est faible (R2 = 21.6%)

    Pas de diérence signicative de prix entre les régions géographiques

    Lien signicatif entre le type d'avocat et la région : les avocats biologiques sont concentrés
     dans l'Ouest
   ACP :
    La structure des données est bien capturée en 2 dimensions (83.7% de variance)

    Premier axe : opposition entre prix et volumes de vente

    Deuxième axe : dimension temporelle

    Les volumes des diérentes variétés sont fortement inter-corrélés

   Limites et perspectives :
    Le modèle linéaire simple prix-volume est insusant

    Une modélisation multivariée serait nécessaire

    L'analyse pourrait être approfondie en segmentant par type et région




                                                33
~~~
