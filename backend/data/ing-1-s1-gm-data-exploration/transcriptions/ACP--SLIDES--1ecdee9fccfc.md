# ACP--SLIDES.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1rj4OOEYy9S6kQTeFI-46frcuTejop8_V) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                             CM 3 : Analyse multivariée - ACP




               Data exploration
      Analyse en Composantes Principales

Observer simultanément des individus d'une population sur p>2 variables

    Etudier le lien entre les variables
    Faire une représentation graphique d’un nuage de points à p
    dimensions
    Qualifier les observations du jeu de donnée
~~~

## Page 2

~~~text
                                                                                                                   CM 3 : Analyse multivariée - ACP


                                                                           ACP
                                        Nuage de points en dimension p
Un jeu de données est un tableau avec en ligne les observations et en colonne les variables
  , … , . On peut donc représenter chaque ligne du tableau comme un point dont les coordonnées
sont les valeurs prises par les variables.
                          p variables

                    x11         x1i     x1p
                    x21     x2i   x2p                             Sur cet exemple chaque
   n observations




                                                                  point est un pays
                             M                                    caractérisé par son
                    xk1   K xki L xkp         observation :       espérance de vie, et ses
                                                                  taux de natalité et de
                             M                                    mortalité.
                    xn1     xni   xnp
                          Variable :

Si p>3, il est impossible de visualiser le nuage de points. L’objectif de l’ACP est de trouver une
projection du nuage de points en dimension 2 ou 3 de façon à perdre le moins possible
d’information.
                                                                                                    Perte
               • Qu’est-ce que l’information?
                                                                                               d’information




                                                                                             Figure J.P. Fenelon
               • Si projection alors produit scalaire?
                                                     ,…,
                                                                                                                        2
               • Quel lien avec les variables                 ?                                                             2
                                                                                                                                                 2
~~~

## Page 3

~~~text
                                                                                        CM 3 : Analyse multivariée - ACP


                                                           ACP
                            Comment mesurer l’information?
Centre de gravité
Le centre de gravité est le point dont les coordonnées sont définies par les valeurs moyennes des
variables,
                                               = ( ,…, )
Inertie
L’information contenue dans un nuage de points correspond à l’inertie de celui-ci, c.-à-d. la somme
des distances au carré entre les observations et le centre de gravité du nuage,

                                            =          −

où . désigne la norme euclidienne. L' inetrie mesure la dispersion totale du nuage de points.
Propriétés de l’inertie
L’inertie peut s’exprimer comme la trace de la matrice de variance-covariance, c.-à-d. la somme des
variances des variables,
                                                                      ⋯
                        =        =∑              où        =     ⋮    ⋱      ⋮    .
                                                                      ⋯
La matrice de variance-covariance est symétrique définie positive.
L’inertie peut aussi s’écrire comme la somme des valeurs propres de ,
                                             =     + ⋯+
                                                                                                3
                                                                                                    3
                                                                                                                      3
~~~

## Page 4

~~~text
                                                                                                                     CM 3 : Analyse multivariée - ACP


                                                                                ACP
                                      Centrer et réduire les variables
L’analyse en composantes principales nécessite de calculer des distances entre observations,

                                                      −   #      =∑         ($ − $ % )².
Si les variables n’ont pas le même ordre de grandeur, certaines variables à valeurs faibles
« disparaitrons » de l’information au profit de celles ayant de fortes valeurs.
                                       Pop. (milliers)        Taux nat. (pour mille)   Esp. vie   Nb. enfants
                   Argentine                  41050                     16,87            75,87         2,19
                   Arménie                    3099                      15,47            74,44         1,77
                   Australie                  21731                     12,56            81,99         1,85
                   Autriche                   8407                      9,01             80,55         1,40

  distance entre                                                                                                 Les variables Taux nat., Esp.
  l’Argentine et               (41050-3099)²+(16,87-15,47)²+(75,87-74,44)²+(2,19-1,77)²=1440278405                  vie et Nb. enfants ne
     l’Arménie                                                          (41050-3099)² =1440278401               comptent pas dans le calcul de
                                                                                                                          la distance

De la même façon la quantification de l’information au travers de l’inertie, = ∑                                     , privilégie les
variables fortement dispersés.
                   Il est donc important de centrer et réduire les variables
                                            −
                                     ←            , i = 1, … , p                                                          4
                                                                                                                              4
                                                                                                                                                   4
~~~

## Page 5

~~~text
                                                                                                 CM 3 : Analyse multivariée - ACP


                                                                  ACP
                                         Quel produit scalaire?
Le produit scalaire entre deux variables      et     + est défini par,
                                                            1
                                         <    , + >=                   $ $ +,
                                                            .
d’où la norme
                                                        1
                                                 ² =               $      ²
                                                        .

Si les variables sont centrées alors <       , + >=         / 0
                                                                  et              =                                     79
D’après la formule du cosinus,                                                              78
                                                 <     , + >
                              cos 4
                                                                          / 0
                                  , +        =                     =              =   / 0
                                                            +                 +



 •|    5 6
          |=1 ⇔ les variables sont colinéaires
                     corrélées positivement si 5 6 =1
                     corrélées négativement si 5 6 =-1
 •    5 6
          = 0 ⇔ les variables sont orthogonales
             ⇔ les variables ne sont pas linéairement corrélées                                       5
                                                                                                          5
                                                                                                                               5
~~~

## Page 6

~~~text
                                                                                         CM 3 : Analyse multivariée - ACP


                                                             ACP
                                                      Principe de l’ACP
  Le principe de l’ACP est de trouver des espaces de petites dimensions sur lesquels les projections des
  observations minimisent la déformation de la réalité.

  On cherche donc un sous-espace :; de Rp de dimension q (q=2,3,..) sur lequel projeté le nuage de
  points. Les axes de ce sous-espace sont des combinaisons linéaires des axes d’origine (c.-à-d. les
  variables). Les nouveaux axes s’appellent les composantes principales.

 Principe                                                          X1      C2
 • La 1ère composante principale (C1) doit « capturer » le                                       C1
 maximum d’information
            Il reste un résidu d’information non expliquée
 • La 2ème composante principale (C2) est calculée sur ce
 résidu telle que
       Elle capture un maximum d’information
       Elle soit non corrélée linéairement à C1
        (orthogonalité)
 • Sur le même principe, calcul de C3, C4, …,Cp                                                           X2



Il s’agit d’un changement de repère pour passer du repère initial formé par les variables à un repère
orthogonale tel que les nouveaux axes sont ordonnés par quantité d’information décroissante.  6
                                                                                                                       6
                        Nb. composantes principales = Nb. variables initiales
~~~

## Page 7

~~~text
                                                                                  CM 3 : Analyse multivariée - ACP

                                                  ACP
                           Comment perdre le moins
                            d’information possible?
Soit un point du nuage et notons < sa projection orthogonale sur le sous-
espace :; .
On cherche :; tel que la distance entre :; et les individus soit minimale.

Minimiser : ∑        < −    ²                                                                      ek




D’après Pythagore,                                                                            fk
                                                                              g
                                                                         Fq
            < −      ²= = −       − < −= ²

Donc le problème revient à maximiser

                       ∑        < −= ²       car = −   ne dépend pas de :;



autrement dit maximiser l’inertie du nuage projeté. On cherche à garder un
maximum de dispersion dans la projection.
                                                                                       7
                                                                                                                7
~~~

## Page 8

~~~text
                                                                                        CM 3 : Analyse multivariée - ACP


                                                          ACP
                                       Solution du problème
Le sous-espace qui minimise l’inertie du nuage projeté est définir par :
                                         :; = vect(Q , … , Q; )
où QR est le vecteur propre unitaire de la matrice de variance-covariance       associée à la kème plus
grande valeur propre.
                          L’inertie du nuage projeté sur Q est
                          L’inertie du nuage projeté sur :; est +…+ ;
                          L’inertie totale est I= +…+ ;

Les vecteurs propres sont appelés les axes principaux
 Le premier axe principal Q est associé à la plus grande valeur propre λ1
 Le deuxième axe principal Q est associé à la deuxième valeur propre λ2
 Etc…
L’ACP est un changement de repère dans lequel les 1ers axes contiennent un maximum d’information

La projection des individus sur un axe principal est une nouvelle variable appelée composante principale
 La première composante c1 représente les coordonnées des projections des individus sur l’axe Q
 La deuxième composante c2 représente les coordonnées des projections des individus sur l’axe Q
 Etc…

                                                                                                                      8
~~~

## Page 9

~~~text
                                                                               CM 3 : Analyse multivariée - ACP


                                                      ACP
                                Combien d’axes retient-on?
Il y a deux règles pour le choix du nombre d’axes :

• garder un maximum d’information contenu dans ces axes (pourcentage cumulé d’inertie)
• couper sur le dernier grand saut d’information entre les axes (elbow rule)




                                                                                                             9
~~~

## Page 10

~~~text
                                     CM 3 : Analyse multivariée - ACP


               ACP
Exemple de la démographie mondiale



                     Pays caractérisés par 4 variables :
                     • TNAT : Taux de natalité
                     • TMORT : Taux de mortalité
                     • EV : Espérance de vie
                     • T65 : Taux >65 ans




                                                                  10
~~~

## Page 11

~~~text
                                                                                                          CM 3 : Analyse multivariée - ACP


                                                                      ACP
                                         Représentation des observations
                   eigenvalue    percentage            cumulative %                   4 variables
                                  of variance          of variance              (TNAT, TMORT, EV, T65)
                                                                                           ⇔
              comp 1   2.66302177      66.5755442         66.57554
              comp 2   1.19799267      29.9498168         96.52536
              comp 3   0.12720887      3.1802217          99.70558            4 composantes principales
              comp 4   0.01177669      0.2944172         100.00000
                                                                          (combinaisons linaires des 4 variables
                                                                                       initiales)
         3




                                                                              La 1ère composante principale contient
                                                                              66,6% de l’inertie.
         2




                                                                              La 2ème composante principale contient
                                                                              29,9% de l’inertie.
         1
Comp 2




                                                                              La représentation des pays sur le plan
                                                                              principal retranscrit 96,5% de l’information.
         0
         -1




                                                                                       Comment interpréter ce
         -2




                                                                                           graphique?
                                                                                  Comment qualifier un pays en haut à droite par
                                                                                                   exemple?
         -3




                                          Comp 1                                                                                       11
              -6         -4         -2             0           2      4
~~~

## Page 12

~~~text
                                                                                                               CM 3 : Analyse multivariée - ACP


                                                                            ACP
                                               Représentation des variables
                         $cor = coordonnée=corrélation
                         $cos2= répartition de la variable sur les 4 axes principaux
                                      La variable TNAT est représentée à 89.82% sur C1 et 1.98% sur C2 etc..
                         $contrib = contribution de la variable à la construction de l’axe
                                          La variable TMORT ne contribue pas (8%) à la construction de c1.
                            Représentation des variables

                                                                              $cor
         1.0




                            TMORT                                                        Dim.1      Dim.2      Dim.3 Dim.4
                                                                              TNAT -0.9477642 -0.1409135          ...
                                                                              TMORT -0.4674138 0.8814408
                              r(T65,c2)                    T65                EV     0.9692397 -0.1966503
         0.5




                                                                              T65    0.7790144 0.6021020

                                                                              $cos2
                                                                                        Dim.1      Dim.2
                                                                              TNAT 0.8982571 0.01985663
Comp 2
         0.0




                                                                              TMORT 0.2184757 0.77693792
                TNAT
                                                     r(T65,c1)                EV    0.9394256 0.03867136
                                                                  EV
                                                                              T65   0.6068634 0.36252677

                                                                              $contrib
         -0.5




                                                                                       Dim.1     Dim.2
                                                                              TNAT 33.73074 1.657492
                                                                              TMORT 8.20405 64.853311
                                                                              EV    35.27668 3.228013
         -1.0




                                                                              T65   22.78853 30.261184

                  -1.0       -0.5       0.0         0.5          1.0                                                                        12
                                      Comp 1
~~~

## Page 13

~~~text
                                                                                                                                             CM 3 : Analyse multivariée - ACP


                                                                                                           ACP
                                                                                Interprétation
                                         Représentation des individus                                               Représentation des variables




                                                                                                    1.0
                                                                                                                    TMORT
                       3




                                                                                                                                                      T65
                       2




                                                                                                    0.5
                       1




                                                                                   Dim 2 (29.95%)
D im 2 (2 9 .9 5 % )




                                                                                                    0.0
                       0




                                                                                                           TNAT
                                                                                                                                                            EV
                       -1




                                                                                                    -0.5
                       -2




                                                                                                    -1.0
                       -3




                            -6   -4         -2                0         2   4                                -1.0    -0.5        0.0         0.5          1.0
                                                 Dim 1 (66.58%)                                                             Dim 1 (66.58%)


                                      • TNAT et EV sont corrélés négativement
                                                 les pays avec un fort taux de natalité ont une espérance de vie courte
                                      • TMORT et T65 sont non corrélés
                                                                                                                                                                          13
~~~

## Page 14

~~~text
                                                                                       CM 3 : Analyse multivariée - ACP


                                                         ACP
                    Validité des représentations graphiques
    • La projection perd le moins d’information possible
 vérifier le % d’inertie expliquée pas l’axe
 conserver le nombre d’axes nécessaire pour avoir une inertie expliquée correcte

                      Autre utilisation de l’ACP = réduire la dimension d’un problème
        L’ACP est très souvent utilisée en amont de méthodes de machine learning pour réduire le
          nombre de variables. L’objectif n’est plus l’interprétation des données sur un graphique.

     • Les variables sont bien représentées si elles sont proches du cercle. A
     contrario celles qui sont proches de l’origine sont peu corrélées avec les axes
 pas d’interprétation possible pour ces variables
                                                                                            e1
     • Les individus sont bien représentés s’ils ne sont pas trop
     éloignés de l’axe sur lequel on les projette
                                                                                                        e2
  vérifier le cosinus entre l’individu et l’axe (proche de 1)
  valable si l’individu loin du centre de gravité                          g
                                                                                                               ck
                                                                                                                    14
~~~

## Page 15

~~~text
                                                                                                         CM 3 : Analyse multivariée - ACP


                                                                                 ACP
                                           Ajout de variable ou d’observation
                      Il est possible d’ajouter des individus ou des variables aux représentations graphiques.
                      Ceux-ci ne participent pas à la construction des axes

                                             Représentation des individus
                 3
                 2




                                                                                                   Ajout d’une variable
                                                                            EUROPE
                                                                                                         qualitative
                 1




                                                                                                une modalité = un nouveau
Dim 2 (29.95%)




                                                                             AMERNOR
                                              AFRIQUE                                            point qui est le centre de
                                                                                                    gravité des individus
                 0




                                                                   AMERSUD
                                                                  ASIE
                                                                 OCEANIE                         présentant cette modalité
                 -1
                 -2
                 -3




                      -6           -4           -2                0              2     4

                                                     Dim 1 (66.58%)                                                                   15
~~~

## Page 16

~~~text
                                                                                                              CM 3 : Analyse multivariée - ACP


                                                                                  ACP
                                               Ajout de variable ou d’observation
                                       Représentation des variables
                 1.0




                                       TMORT



                                                                      T65
                 0.5




                                                                                        Ajout des variables nombre d’enfants
                                                                                        par femme et taux de croissance.
Dim 2 (29.95%)




                                                                                        Cet ajout n’a pas modifié le calcul des
                 0.0




                        NBENF
                         TNAT
                                                                                        composantes principales. Il s’agit juste
                                                                             EV         d’une projection des variables dans le
                                                                                        cercle de corrélation.
                                 TCR
                 -0.5
                 -1.0




                          -1.0         -0.5         0.0         0.5         1.0

                                               Dim 1 (66.58%)                                                                              16
~~~

## Page 17

~~~text
                                                                                                              CM 3 : Analyse multivariée - ACP


                                                                                  ACP
                                               Ajout de variable ou d’observation
                                       Représentation des variables
                 1.0




                                       TMORT



                                                                      T65
                 0.5




                                                                                        Ajout des variables nombre d’enfants
                                                                                        par femme et taux de croissance.
Dim 2 (29.95%)




                                                                                        Cet ajout n’a pas modifié le calcul des
                 0.0




                        NBENF
                         TNAT
                                                                                        composantes principales. Il s’agit juste
                                                                             EV         d’une projection des variables dans le
                                                                                        cercle de corrélation.
                                 TCR
                 -0.5
                 -1.0




                          -1.0         -0.5         0.0         0.5         1.0

                                               Dim 1 (66.58%)                                                                              17
~~~

## Page 18

~~~text
                                                                                                                        CM 3 : Analyse multivariée - ACP


                                                                                    ACP
                                                               Alternatives à l’ACP

Analyse en composantes principales indépendants                                       L'algorithme t-SNE (t-distributed stochastic neighbor
Analyse en composantes principales par noyaux                                         embedding) est une technique de réduction de
                                                                                      dimension pour la visualisation de données . Il s'agit
                                                                                      d'une méthode non linéaire (contrairement à l’ACP)
                                                                                      permettant de représenter un ensemble de points d'un
                                                                                      espace à grande dimension dans un espace de deux
                                                                                      ou trois dimensions, les données peuvent ensuite être
                                                                                      visualisées avec un nuage de points. L'algorithme t-SNE
                                                                                      tente de trouver une configuration optimale pour
                                                                                      respecter les proximités entre points : deux points qui
                                                                                      sont proches (resp. éloignés) dans l'espace d'origine
                                                                                      devront être proches (resp. éloignés) dans l'espace de
                                                                                      faible dimension.




 https://www.commonlounge.com/discussion/9bcc188644cd4bc9b7542dab93fa8bd7/history
                                                                                                                                                     18
                                                                                                 https://openclassrooms.com/fr/courses/4379436
~~~
