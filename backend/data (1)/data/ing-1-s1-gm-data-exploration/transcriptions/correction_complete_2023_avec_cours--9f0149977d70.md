# correction_complete_2023_avec_cours.pdf

[Ouvrir l’original](https://drive.google.com/open?id=10RKbx7gSr0mKuSzVWDOEoliB3-M-ieow) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                       Correction Complète avec Cours
                                Examen Data Exploration

                                        ING1 GM-MIM

                                               CY Tech

                                           22 décembre 2023


                                                Abstract
         Ce document présente une correction détaillée de l'examen de Data Exploration portant

     sur l'analyse du jeu de données  Airbnb New York 2019 (Exercice 1) et des données climatiques
     françaises   Climfrance (Exercice 2). Chaque question est accompagnée d'un rappel de cours
     complet suivi de la solution détaillée.




Contents
1 Exercice 1 - Analyse des données Airbnb New York                                                   2
  1.1 Questions 1-2 : Présentation générale des données . . . . . . . . . . . . . . . . . . .        2
2 Analyse Univariée : Variable Prix                                                                   4
  2.1 Question 3 : Quartiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      4
  2.2 Question 4 : Écart interquartile et Étendue . . . . . . . . . . . . . . . . . . . . . .         6
  2.3 Question 5 : Comparaison Moyenne / Médiane . . . . . . . . . . . . . . . . . . . .              8
  2.4 Question 6 : Classication des indicateurs . . . . . . . . . . . . . . . . . . . . . . .       10
  2.5 Question 7 : Boxplot (Boîte à moustaches) . . . . . . . . . . . . . . . . . . . . . . .        12
      2.5.1 Question 7a : Extrémités des moustaches . . . . . . . . . . . . . . . . . . .            12
      2.5.2 Question 7b : Valeurs aberrantes . . . . . . . . . . . . . . . . . . . . . . . .         14
3 Analyse Bivariée : Prix Ö Neighbourhood (ANOVA)                                                    16
  3.1 Question 8 : Variances inter-groupes et intra-groupes . . . . . . . . . . . . . . . . .        18
  3.2 Question 9 : Rapport de corrélation . . . . . . . . . . . . . . . . . . . . . . . . . .        20




                                                    1
~~~

## Page 2

~~~text
Correction avec cours - Data Exploration 2023-2024                                ING1-GM/MIM


1    Exercice 1 - Analyse des données Airbnb New York

Contexte du jeu de données
Le jeu de données comprend 500 logements Airbnb à New York (extrait de 28 590 logements) avec
les variables suivantes :
     Id : Identiant unique du logement
     Neighbourhood : Arrondissement (Bronx, Brooklyn, Manhattan, Queens, Staten Island)
     Latitude, Longitude : Coordonnées GPS
     Room type : Type de chambre (Entire home/apt, Private room, Shared room)
     Price$ : Prix par nuit en dollars
     Minimum night : Nombre minimum de nuits
     Number of reviews : Nombre d'avis
     Availability : Disponibilité (jours/an)
1.1 Questions 1-2 : Présentation générale des données
    RAPPEL DE COURS
    Types de variables en statistique :
    1. Variables qualitatives (catégorielles) :
        Nominales : Pas d'ordre naturel (couleur, région, type)
        Ordinales : Ordre naturel (niveau d'études, satisfaction)
    2. Variables quantitatives (numériques) :
        Discrètes : Valeurs entières dénombrables (nombre d'enfants, eectifs)
        Continues : Valeurs réelles dans un intervalle (taille, prix, température)
    Représentations graphiques selon le type :
        Qualitative : Diagramme en barres, diagramme circulaire (camembert)
        Quantitative : Histogramme, boxplot, polygone des fréquences
        Deux variables : Nuage de points, tableau de contingence
    Population vs Échantillon :
        Population : Ensemble complet des individus étudiés
        Échantillon : Sous-ensemble de la population (taille n)




                                                 2
~~~

## Page 3

~~~text
Correction avec cours - Data Exploration 2023-2024                          ING1-GM/MIM


   SOLUTION
   Question 1 : Variables étudiées

          Variable             Type               Représentation graphique
          Id                   Quantitative discrète
                                                  Aucune (identiant)
          Neighbourhood        Qualitative nominale
                                                  Diagramme      en     barres,
                                                  Camembert
          Latitude          Quantitative continue Carte, Nuage de points
          Longitude         Quantitative continue Carte, Nuage de points
          Room type         Qualitative nominale Diagramme       en     barres,
                                                  Camembert
          Price$            Quantitative continue Histogramme, Boxplot
          Minimum night     Quantitative discrète Histogramme, Diagramme en
                                                  barres
          Number of reviews Quantitative discrète Histogramme, Boxplot
          Availability      Quantitative discrète Histogramme
   Question 2 : Population et échantillon

       Population étudiée : Tous les logements Airbnb disponibles à New York en 2019
        Total : environ 28 590 logements
       Taille de l'échantillon : n = 500 logements (les 500 premiers)
       Type d'échantillonnage : Non aléatoire (500 premiers)  biais potentiel




                                              3
~~~

## Page 4

~~~text
Correction avec cours - Data Exploration 2023-2024                          ING1-GM/MIM


2    Analyse Univariée : Variable Prix

Données fournies
Variable : Price (prix par nuit en dollars)
   Résumé statistique :
     Minimum = 33$
     Q1 (25%) = 85$
     Médiane Q2 (50%) = 125$
     Q3 (75%) = 186$
     Maximum = 2000$
     Moyenne = 152.3$
2.1 Question 3 : Quartiles
    RAPPEL DE COURS
    Les quartiles divisent une série ordonnée en quatre parties égales :
    Dénitions :
        Q1 (premier quartile) : 25% des valeurs sont ≤ Q          1

        Q2 (médiane) : 50% des valeurs sont ≤ Q        2

        Q3 (troisième quartile) : 75% des valeurs sont ≤ Q            3

    Calcul (méthode simpliée) :
    Pour une série de n valeurs ordonnées x1 ≤ x2 ≤ · · · ≤ xn :
        Position de Q1 :   n+1
                             4

        Position de Q2 :   n+1
                             2

        Position de Q3 :   3(n+1)
                               4

    Si la position n'est pas entière, on interpole linéairement.
    Propriétés :
        50% des valeurs sont dans l'intervalle [Q , Q ]
                                                    1   3

        Les quartiles sont robustes (peu sensibles aux valeurs extrêmes)
        Q2 = médiane (indicateur de tendance centrale robuste)




                                                   4
~~~

## Page 5

~~~text
Correction avec cours - Data Exploration 2023-2024                                  ING1-GM/MIM


   SOLUTION
   Identication des quartiles :

       Q1 = 85 dollars
       Q2 = 125 dollars (médiane)
       Q3 = 186 dollars
   Interprétation détaillée :
   Q1 = 85$ :
       25% des logements Airbnb coûtent moins de 85$ par nuit
       75% des logements coûtent plus de 85$ par nuit
       C'est le prix du "premier quart" des logements les moins chers
   Q2 = 125$ (médiane) :
       50% des logements coûtent moins de 125$ par nuit
       50% des logements coûtent plus de 125$ par nuit
       C'est le prix typique/médian d'un logement Airbnb à New York
       La moitié des logements sont en dessous, l'autre moitié au-dessus
   Q3 = 186$ :
       75% des logements coûtent moins de 186$ par nuit
       25% des logements coûtent plus de 186$ par nuit
       Les logements à plus de 186$ constituent le "quart supérieur"
   Synthèse :
   L'intervalle interquartile [85, 186] contient 50% des prix centraux. Cela signie que la moitié
   des logements se situent dans cette fourchette de prix, qui représente une gamme de logements
   "moyens" à New York.




                                                 5
~~~

## Page 6

~~~text
Correction avec cours - Data Exploration 2023-2024                                ING1-GM/MIM


2.2 Question 4 : Écart interquartile et Étendue
   RAPPEL DE COURS
   Mesures de dispersion :
   Les mesures de dispersion quantient l'étalement/la variabilité des données.
   1. Écart interquartile (IQR = Interquartile Range) :
       FORMULES CLÉS

                                        IQR = Q3 − Q1

   Propriétés :
       Mesure la dispersion des 50% de valeurs centrales
       Robuste aux valeurs extrêmes (outliers)
       Utilisé pour détecter les valeurs aberrantes
   2. Étendue (Range) :
       FORMULES CLÉS

                                        E = xmax − xmin

   Propriétés :
       Mesure la dispersion totale des données
       Non robuste (très sensible aux valeurs extrêmes)
       Simple mais peu informatif si outliers présents
   3. Autres mesures de dispersion :
       Variance : s = P (x − x̄)
                      2   1
                          n
                              n
                              i=1   i
                                         2


       Écart-type : s = √s   2


       Coecient de variation : CV = (dispersion relative)
                                             s
                                             x̄




                                                  6
~~~

## Page 7

~~~text
Correction avec cours - Data Exploration 2023-2024                                 ING1-GM/MIM


   SOLUTION
   Calcul de l'écart interquartile :

                            IQR = Q3 − Q1 = 186 − 85 = 101 dollars
   Interprétation :
   L'écart interquartile de 101$ signie que :
       Les 50% de prix centraux sont répartis sur un intervalle de 101$
       C'est la "largeur" de la boîte dans un boxplot
       Cette dispersion est modérée : l'intervalle [85, 186] est relativement concentré
   Calcul de l'étendue :

                          E = xmax − xmin = 2000 − 33 = 1967 dollars
   Interprétation :
   L'étendue de 1967$ signie que :
       L'écart entre le logement le moins cher (33$) et le plus cher (2000$) est énorme
       Cette valeur est très supérieure à l'IQR (1967 vs 101)
       Cela indique la présence de valeurs extrêmes (logements de luxe)
   Comparaison IQR vs Étendue :
   Le rapport IQR
               E
                    101 ≈ 19.5 est très élevé, conrmant :
                  = 1967

       Une forte asymétrie dans la distribution
       La présence de prix exceptionnellement élevés
       L'IQR est plus représentatif de la dispersion "typique"




                                                 7
~~~

## Page 8

~~~text
Correction avec cours - Data Exploration 2023-2024                           ING1-GM/MIM


2.3 Question 5 : Comparaison Moyenne / Médiane
   RAPPEL DE COURS
   Indicateurs de tendance centrale :
   1. Moyenne arithmétique :
       FORMULES CLÉS
                                                    n
                                                1X
                                         x̄ =      xi
                                                n
                                                    i=1


   Propriétés :
       Prend en compte toutes les valeurs
       Sensible aux valeurs extrêmes
       "Centre de gravité" des données
   2. Médiane :
       FORMULES CLÉS

                                                          si n impair
                                      (
                                       x(n+1)/2
                               Me =     xn/2 +xn/2+1
                                              2           si n pair

   Propriétés :
       Valeur centrale qui partage en deux groupes égaux
       Robuste aux valeurs extrêmes
       Plus représentative si distribution asymétrique
   Comparaison Moyenne/Médiane et forme de la distribution :

                       Relation Distribution                     Asymétrie
                       x̄ = M e Symétrique                       Aucune
                       x̄ > M e Asymétrique à droite             Positive
                       x̄ < M e Asymétrique à gauche             Négative

   Asymétrie à droite (positive) :
       Queue de distribution étalée vers les valeurs élevées
       Valeurs extrêmes élevées tirent la moyenne vers le haut
       Typique des distributions de revenus, prix immobiliers




                                                8
~~~

## Page 9

~~~text
Correction avec cours - Data Exploration 2023-2024                              ING1-GM/MIM


   SOLUTION
   Données :
       Moyenne : x̄ = 152.3 dollars
       Médiane : M e = 125 dollars
       Diérence : x̄ − M e = 152.3 − 125 = 27.3 dollars
   Comparaison :

                                    x̄ = 152.3 > 125 = M e
   La moyenne est supérieure à la médiane.
   Interprétation de la diérence :
   Cette situation (x̄ > M e) indique une distribution asymétrique à droite (asymétrie
   positive).
   Explications :

     1. Présence de valeurs élevées :
            Le maximum est de 2000$, très éloigné de la médiane
            Ces prix exceptionnels (logements de luxe) augmentent la moyenne
            La médiane reste insensible à ces valeurs extrêmes
     2. Distribution "tirée vers le haut" :
            Queue de distribution étalée vers les prix élevés
            Plus de logements au-dessus de la moyenne qu'en dessous
            Quelques logements très chers déséquilibrent la moyenne
     3. Représentativité :
            La médiane (125$) est plus représentative du prix "typique"
            La moyenne (152$) est "tirée" par les logements de luxe
            50% des logements coûtent moins de 125$
            Mais la moyenne est à 152$ à cause de quelques prix très élevés
   Contexte économique :
   C'est typique du marché immobilier :
       Majorité de logements "standards" (autour de 125$)
       Minorité de logements premium/luxe (plusieurs centaines ou milliers de $)
       Les penthouses, appartements de standing, maisons entières à Manhattan créent cette
        asymétrie
   Conclusion :
   Pour décrire le prix "typique" d'un logement Airbnb à New York, il vaut mieux utiliser la
   médiane (125$) plutôt que la moyenne (152$), car elle n'est pas inuencée par les quelques
   logements exceptionnellement chers.




                                               9
~~~

## Page 10

~~~text
Correction avec cours - Data Exploration 2023-2024                           ING1-GM/MIM


2.4 Question 6 : Classication des indicateurs
   RAPPEL DE COURS
   Classication des indicateurs statistiques :
   1. Indicateurs de position (ou de tendance centrale) :
   Répondent à la question : "Où se situent les données ?"

       Moyenne x̄ : Centre de gravité
       Médiane M e : Valeur centrale
       Mode M o : Valeur la plus fréquente
       Quartiles Q , Q , Q : Positions à 25%, 50%, 75%
                        1   2     3

       Déciles, percentiles : Positions à 10%, 1%, etc.
       Minimum, Maximum : Valeurs extrêmes
   2. Indicateurs de dispersion :
   Répondent à la question : "Comment les données sont-elles dispersées ?"

       Étendue E = x − x   max       min

       Écart interquartile IQR = Q − Q     3   1

       Variance s  2


       Écart-type s
       Coecient de variation CV = s/x̄
   3. Indicateurs de forme :

       Coecient d'asymétrie (skewness) : mesure l'asymétrie
       Coecient d'aplatissement (kurtosis) : mesure le "pic" de la distribution




                                                    10
~~~

## Page 11

~~~text
Correction avec cours - Data Exploration 2023-2024                  ING1-GM/MIM


   SOLUTION
   Classication des indicateurs calculés :
   INDICATEURS DE POSITION :

     1. Minimum = 33$
            Indique la position de la valeur la plus basse
            Le logement le moins cher coûte 33$/nuit
     2. Q1 = 85$
            Indique la position du premier quartile
            25% des données sont en dessous de cette valeur
     3. Médiane (Q2) = 125$
            Indique la position centrale
            50% des données sont de chaque côté
     4. Moyenne = 152.3$
            Indique le "centre de gravité" des données
            Point d'équilibre si on pondère toutes les valeurs
     5. Q3 = 186$
            Indique la position du troisième quartile
            75% des données sont en dessous
     6. Maximum = 2000$
            Indique la position de la valeur la plus élevée
            Le logement le plus cher coûte 2000$/nuit
   INDICATEURS DE DISPERSION :

     1. Étendue = 1967$
            Mesure la dispersion totale des prix
            Écart entre le moins cher et le plus cher
            Indique une très forte variabilité
     2. Écart interquartile (IQR) = 101$
            Mesure la dispersion des 50% centraux
            Largeur de l'intervalle contenant la moitié des prix
            Plus robuste que l'étendue
   Résumé du tableau :
                               Indicateur Valeur   Type
                               Minimum      33$   Position
                               Q1           85$   Position
                               Médiane     125$   Position
                               Moyenne    152.3$  Position
                               Q3          186$   Position
                               Maximum      11
                                           2000$  Position
                               Étendue     1967$ Dispersion
                               IQR         101$  Dispersion
~~~

## Page 12

~~~text
Correction avec cours - Data Exploration 2023-2024                                ING1-GM/MIM


2.5 Question 7 : Boxplot (Boîte à moustaches)
2.5.1 Question 7a : Extrémités des moustaches
   RAPPEL DE COURS
   Le boxplot (boîte à moustaches) :
   Le boxplot est une représentation graphique qui résume 5 indicateurs :
       Le minimum (ou la moustache inférieure)
       Q1, Q2 (médiane), Q3 (la "boîte")
       Le maximum (ou la moustache supérieure)
   Calcul des moustaches :
   Les moustaches délimitent les valeurs non aberrantes :
       FORMULES CLÉS
      Moustache inférieure :
                                m = max(xmin , Q1 − 1.5 × IQR)

      Moustache supérieure :

                                M = min(xmax , Q3 + 1.5 × IQR)

   Règle de Tukey (coecient 1.5) :
   Le coecient 1.5 est une convention (John Tukey) qui dénit une zone "normale" :
       Zone normale : [Q − 1.5 × IQR, Q + 1.5 × IQR]
                           1                3

       Au-delà : valeurs considérées comme aberrantes (outliers)
   Interprétation :
       Si x ≥ Q − 1.5 × IQR : moustache va jusqu'au minimum
            min       1

       Sinon : moustache s'arrête à Q − 1.5 × IQR et les valeurs plus petites sont des outliers
                                       1

       Même logique pour la moustache supérieure




                                                12
~~~

## Page 13

~~~text
Correction avec cours - Data Exploration 2023-2024                             ING1-GM/MIM


   SOLUTION
   Données :
       Q = 85$
          1

       Q = 186$
          3

       IQR = 101$
       x = 33$
          min

       x = 2000$
          max

   Calcul de la moustache inférieure m :
   Étape 1 : Calculer Q1 − 1.5 × IQR

                     Q1 − 1.5 × IQR = 85 − 1.5 × 101 = 85 − 151.5 = −66.5
   Étape 2 : Prendre le maximum entre cette valeur et xmin

                      m = max(xmin , −66.5) = max(33, −66.5) = 33 dollars
   Interprétation :
   La moustache inférieure est à 33$, c'est-à-dire exactement le minimum.
   Cela signie qu'il n'y a pas de valeurs aberrantes inférieures car :
                              xmin = 33 > −66.5 = Q1 − 1.5 × IQR

   Tous les prix, même le plus bas (33$), restent dans la zone "normale".
   Calcul de la moustache supérieure M :
   Étape 1 : Calculer Q3 + 1.5 × IQR

                    Q3 + 1.5 × IQR = 186 + 1.5 × 101 = 186 + 151.5 = 337.5
   Étape 2 : Prendre le minimum entre cette valeur et xmax

                    M = min(xmax , 337.5) = min(2000, 337.5) = 337.5 dollars
   Interprétation :
   La moustache supérieure s'arrête à 337.5$, bien avant le maximum (2000$).
   Cela signie qu'il existe des valeurs aberrantes supérieures car :
                             xmax = 2000 > 337.5 = Q3 + 1.5 × IQR

   Toutes les valeurs au-dessus de 337.5$ sont considérées comme aberrantes.
   Résumé des moustaches :
                                     Moustache       Valeur
                                     Inférieure (m)   33$
                                     Supérieure (M ) 337.5$

   L'intervalle des valeurs non aberrantes est donc [33, 337.5] dollars.




                                                 13
~~~

## Page 14

~~~text
Correction avec cours - Data Exploration 2023-2024                              ING1-GM/MIM


2.5.2 Question 7b : Valeurs aberrantes
   RAPPEL DE COURS
   Valeurs aberrantes (outliers) :
   Une valeur est considérée comme aberrante si elle se situe en dehors de l'intervalle déni
   par les moustaches.
       FORMULES CLÉS
      Valeurs aberrantes inférieures :
                                     x < Q1 − 1.5 × IQR

      Valeurs aberrantes supérieures :
                                     x > Q3 + 1.5 × IQR

   Sur le boxplot :
       Les valeurs aberrantes sont représentées par des points isolés
       Au-delà des moustaches
       Peuvent être à droite ou à gauche de la boîte
   Causes possibles des outliers :
       Erreur de mesure : Saisie incorrecte, dysfonctionnement d'appareil
       Valeurs réelles exceptionnelles : Cas rares mais légitimes
       Population diérente : Individu d'une autre population
   Traitement des outliers :
       Conserver : Si valeurs réelles et pertinentes pour l'analyse
       Analyser séparément : Étudier ces cas particuliers
       Supprimer : Uniquement si erreur avérée ou hors contexte
       Utiliser des méthodes robustes : Médiane plutôt que moyenne




                                              14
~~~

## Page 15

~~~text
Correction avec cours - Data Exploration 2023-2024                               ING1-GM/MIM


   SOLUTION
   Critère de détection :
   Une valeur est aberrante si elle est en dehors de l'intervalle [m, M ] = [33, 337.5].
   Analyse des valeurs aberrantes inférieures :
   Seuil inférieur : Q1 − 1.5 × IQR = −66.5$
   Valeurs à tester : x < −66.5 ?
   Comme tous les prix sont positifs et xmin = 33 > −66.5, il n'y a aucune valeur aberrante
   inférieure.
   Analyse des valeurs aberrantes supérieures :
   Seuil supérieur : Q3 + 1.5 × IQR = 337.5$
   Valeurs à tester : x > 337.5 ?
   Observation :
       Le maximum est x = 2000$
                           max

       2000 > 337.5 : c'est une valeur aberrante
       Sur le boxplot fourni, on observe plusieurs points au-dessus de la moustache supérieure
   Conclusion :
   Oui, il existe des valeurs aberrantes, toutes supérieures.
   Identication sur le graphique :
   D'après le boxplot de l'énoncé, on observe :
       Plusieurs points isolés au-dessus de la moustache supérieure
       Ces points se situent entre environ 400$ et 2000$
       Le point le plus élevé (vers 2000$) est très éloigné de la boîte
       On observe aussi des points vers 500$, 800$, 1000$
   Interprétation contextuelle :
   Ces valeurs aberrantes correspondent à des logements exceptionnellement chers :
       Penthouses de luxe à Manhattan
       Appartements entiers haut de gamme
       Maisons avec vue exceptionnelle
       Logements avec équipements premium
       Emplacements ultra-privilégiés (Central Park, Times Square)
   Faut-il les supprimer ?
   Non, ces valeurs ne doivent pas être supprimées car :
     1. Ce sont des valeurs réelles et vériables
     2. Elles représentent un segment légitime du marché Airbnb (luxe)
     3. Elles expliquent pourquoi la moyenne (152$) est supérieure à la médiane (125$)
     4. Supprimer ces valeurs fausserait l'analyse du marché complet
   Cependant, pour certaines analyses, on pourrait :
       Utiliser la médiane plutôt que la moyenne (plus robuste)
       Faire une analyse séparée du segment luxe
                                              15
       Créer des catégories de prix (économique, moyen, premium, luxe)
~~~

## Page 16

~~~text
Correction avec cours - Data Exploration 2023-2024                           ING1-GM/MIM


3    Analyse Bivariée : Prix             Ö Neighbourhood (ANOVA)
Contexte
On étudie le lien entre :
     Variable quantitative : Price (prix par nuit)
     Variable qualitative : Neighbourhood (5 arrondissements de New York)
    Question : Le prix varie-t-il selon l'arrondissement ?

Résultats ANOVA fournis
Analysis of Variance Table
Response: price
                        Df Sum Sq Mean Sq F value Pr(>F)
as.factor(neighbourhood) 68 1253070 18428 1.1695 0.1819
Residuals               431 6791083 15757




                                                 16
~~~

## Page 17

~~~text
Correction avec cours - Data Exploration 2023-2024   ING1-GM/MIM




                                              17
~~~

## Page 18

~~~text
Correction avec cours - Data Exploration 2023-2024                         ING1-GM/MIM


3.1 Question 8 : Variances inter-groupes et intra-groupes
   RAPPEL DE COURS
   Analyse de la Variance (ANOVA) à un facteur :
   L'ANOVA teste l'égalité des moyennes de plusieurs groupes.
   Principe de décomposition de la variance :
   La variance totale se décompose en deux parties :
       FORMULES CLÉS

                                 SCEtot = SCEinter + SCEintra
      Où :
           SCE : Somme des Carrés des Écarts totale
                 tot

           SCE : Variation ENTRE les groupes (expliquée par le facteur)
                 inter

           SCE : Variation À L'INTÉRIEUR des groupes (résiduelle)
                 intra


   Formules détaillées :
   1. SCE inter-groupes (Between groups) :
                                                   k
                                                   X
                                   SCEinter =            ni (x̄i − x̄)2
                                                   i=1

       k = nombre de groupes
       n = eectif du groupe i
          i

       x̄ = moyenne du groupe i
          i

       x̄ = moyenne générale
   2. SCE intra-groupes (Within groups) :
                                              ni
                                            k X
                                            X
                                 SCEintra =      (xij − x̄i )2
                                              i=1 j=1

   3. Variances (Mean Squares) :
       FORMULES CLÉS
                                                   SCEinter
                                       s2inter =
                                                    k−1
      (variance inter-groupes)

                                                   SCEintra
                                      s2intra =
                                                    n−k
      (variance intra-groupes)

                                                   SCEtot
                                         s2tot =
                                                    n−1
      (variance totale)

   Où :                                            18
       k = nombre de groupes
~~~

## Page 19

~~~text
Correction avec cours - Data Exploration 2023-2024                              ING1-GM/MIM


   SOLUTION
   Lecture du tableau ANOVA :
                         Source        Df Sum Sq Mean Sq
                         Neighbourhood 68 1253070  18428
                         Residuals     431 6791083 15757
   Identication des valeurs :

       k − 1 = 68 donc k = 69 groupes (nombre d'arrondissements distincts)
       n − k = 431 donc n = 431 + 69 = 500 observations
       SCE = 1253070
             inter

       SCE = 6791083
             intra

   Variance inter-groupes :
                                         SCEinter   1253070
                             s2inter =            =         = 18428
                                          k−1          68
   C'est la valeur "Mean Sq" pour Neighbourhood dans le tableau.
   Interprétation : Cette variance mesure la variabilité des prix entre les diérents
   arrondissements. C'est la partie de la variance "expliquée" par le facteur Neighbourhood.
   Variance intra-groupes :
                                         SCEintra   6791083
                             s2intra =            =         = 15757
                                          n−k         431
   C'est la valeur "Mean Sq" pour Residuals dans le tableau.
   Interprétation : Cette variance mesure la variabilité des prix à l'intérieur de chaque
   arrondissement. C'est la partie "résiduelle" ou "inexpliquée" par le facteur.
   Variation totale (SCE totale) :

                                 SCEtot = SCEinter + SCEintra
                            SCEtot = 1253070 + 6791083 = 8044153
   Variance totale :
                                       SCEtot   8044153
                             s2tot =          =         = 16121.35
                                        n−1       499
   Résumé des résultats :
                               Indicateur             Valeur
                               Variance inter-groupes  18428
                               Variance intra-groupes  15757
                               Variation totale (SCE) 8044153
                               Variance totale        16121.35
   Observation importante :
   Les deux variances sont du même ordre de grandeur :
                                         s2inter   18428
                                          2      =       = 1.17
                                         sintra    15757

   Ce rapport est la statistique F = 1.1695 (légèrement diérent à cause des arrondis). Un
   ratio proche de 1 suggère que la variance entre les groupes n'est pas beaucoup plus grande
   que la variance à l'intérieur des groupes, ce qui
                                                  19 indique un faible eet du facteur.
~~~

## Page 20

~~~text
Correction avec cours - Data Exploration 2023-2024                              ING1-GM/MIM


3.2 Question 9 : Rapport de corrélation
   RAPPEL DE COURS
   Le rapport de corrélation η 2 (êta carré) :
   Le rapport de corrélation mesure la proportion de variance expliquée par le facteur
   qualitatif.
       FORMULES CLÉS
                                     SCEinter   V ariance explique
                              η2 =            =
                                      SCEtot     V ariance totale

   Propriétés :
       0≤η ≤12


       η = 0 : Le facteur n'explique rien de la variable
         2


       η = 1 : Le facteur explique totalement la variable
         2


   Interprétation des valeurs :
       η < 0.01 : Eet négligeable
         2


       0.01 ≤ η < 0.06 : Eet faible
                  2


       0.06 ≤ η < 0.14 : Eet moyen
                  2


       η ≥ 0.14 : Eet fort
         2


   Relation avec l'ANOVA :
                                                SCEinter
                                     η2 =
                                            SCEinter + SCEintra
   Le rapport de corrélation est l'équivalent du R2 (coecient de détermination) pour une
                        Ö
   relation Quantitative Qualitative.
   Diérence avec la corrélation linéaire :
   Le rapport de corrélation η 2 peut détecter des relations non linéaires, contrairement à r2
   qui ne mesure que les relations linéaires.




                                                  20
~~~

## Page 21

~~~text
Correction avec cours - Data Exploration 2023-2024                                ING1-GM/MIM


   SOLUTION
   Calcul du rapport de corrélation :
                                     SCEinter   1253070
                              η2 =            =         = 0.1558
                                      SCEtot    8044153
   En pourcentage : η 2 = 15.58%
   Interprétation :
   Le rapport de corrélation de 0.156 (ou 15.6%) signie que :

     1. Part expliquée :
            L'arrondissement explique 15.6% de la variabilité du prix
            Si on connaît l'arrondissement, on réduit l'incertitude sur le prix de 15.6%
     2. Part non expliquée :
            1 − η = 1 − 0.156 = 0.844 = 84.4%
                  2

            84.4% de la variance du prix est due à d'autres facteurs :
                Type de logement (Entire home vs Private room)
                Taille du logement
                Équipements (WiFi, cuisine, piscine)
                Proximité des attractions touristiques
                Qualité du logement (notes, avis)
                Saison, disponibilité
     3. Force de l'eet :
            η = 0.156 > 0.14 : c'est un eet fort selon les seuils standards
              2

            L'arrondissement a un impact modéré à fort sur le prix
   Cohérence avec le test F :
   Le test F donne :
       F = 1.1695
       p-value = 0.1819 > 0.05
   On ne rejette pas H0 au seuil 5% : les diérences de moyennes entre arrondissements ne
   sont pas statistiquement signicatives.
   Apparent paradoxe :
   Comment η 2 = 15.6% (eet modéré) peut-il coexister avec un test non signicatif ?
   Explications :

     1. Nombre de groupes : Avec 69 arrondissements, les degrés de liberté sont importants,
        ce qui réduit la puissance du test
     2. Variance intra-groupes élevée : s2intra = 15757 est très proche de s2inter = 18428
     3. Eectifs déséquilibrés :         Certains arrondissements ont peut-être très peu
        d'observations
     4. Distinction eet pratique vs signicativité statistique :
            η = 15.6% indique un eet pratique réel mais modéré
              2

            Le test F non signicatif indique qu'avec cet échantillon, on ne peut pas armer
             avec certitude que cet eet existe dans la population
                                                21
   Conclusion pratique :
   Bien que le test ne soit pas signicatif au seuil 5%, le rapport de corrélation suggère que
~~~
