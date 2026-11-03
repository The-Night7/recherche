# CH-4.Tests de comparaison.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1coU3f60oj9cJ6kZdMVuXO1wT1QL5iNJt) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Ingénieurs 1ère année : Parcours Mathématiques appliquées

               Statistiques inférentielles




         CM 4 : Tests de comparaison d’échantillons



               Nisrine FORTIN-CAMDAVANT
~~~

## Page 2

~~~text
1   Test de comparaison de deux échantillons
      Test de Student – Test d’égalité de moyennes
        Test de comparaison de moyennes sur échantillons appariés
        Test de comparaison de deux espérances sur échantillons indépendants
      Test de Fisher – Test de comparaison de deux variances



2   Test de comparaison de plusieurs échantillons
~~~

## Page 3

~~~text
Motivations.
     Dans le CM3, on a effectué des tests à partir d’un seul échantillon.
     On a comparé l’espérance, la variance ou la proportion d’un
     caractère d’une population à une valeur de référence.


     On souhaite à présent effectuer des tests de comparaison de deux
     populations différentes selon un critère quantitatif particulier à partir
     de deux échantillons extraits de ces deux populations. Par exemple :
          Comparer le salaire moyen des femmes cadres et celui des hommes cadres.
          Comparer les performances de deux machines au vu de la proportion de
          pièces défectueuses qu’elles produisent.
          Comparer l’efficacité d’un traitement en comparant des mesures effectuées
          avant traitement à des mesures faites après traitement.



   Les échantillons ont-ils été prélevés dans la même population ?

                              ou encore :
 La différence entre les échantillons est-elle dû au hasard ou est-elle
                             significative ?
~~~

## Page 4

~~~text
        Test de comparaison de deux échantillons

En pratique, on se contente de comparer les échantillons au travers des valeurs
remarquables telles que la moyenne, variance, . . ..



    2 échantillons
     On considère deux échantillons indépendants ou appariés :

                        X1 , X2 , . . . , Xn1 et Y1 , Y2 , . . . , Yn2

     représentant les variables aléatoires X et Y.
          E(X) = µ1 et Var(X) = σ12 .
          E(Y) = µ2 et Var(Y) = σ22 .
     Nous calculons les moyennes empiriques X et Y ainsi que les variances
     empiriques corrigées S∗2    ∗2
                           1 et S2 .



Nous nous demandons : est-ce que ces deux échantillons sont issus de la même
population ? ont-ils les mêmes caractéristiques ?
~~~

## Page 5

~~~text
Test de Student – Test d’égalité de moyennes




    Test de Student – Test d’égalité de moyennes
     Le test de Student consiste à faire la différence entre les deux moyennes (propor-
     tions) et de tester si la différence est nulle.
                                 ⎧ H     ∶    µ1   =   µ2
                                 ⎪ 0
                                 ⎪
                                 ⎪
                                 ⎨
                                 ⎪
                                 ⎪
                                 ⎩ H1
                                 ⎪       ∶    µ1   ≠   µ2

     Autrement dit,

                                 ⎧ H      ∶   µ1 − µ2 = 0
                                 ⎪ 0
                                 ⎪
                                 ⎪
                                 ⎨
                                 ⎪
                                 ⎪
                                 ⎩ H1
                                 ⎪        ∶   µ1 − µ2 ≠ 0
~~~

## Page 6

~~~text
  Test de comparaison de deux échantillons                         Test de comparaison de plusieurs échantillons




               Échantillons appariés.
                On parle de données appariées lorsque les deux échantillons considérés sont
                formés des individus,
                       pour lesquels on a fait deux mesures d’une même quantité,
                       généralement avec écart temporel et/ou après l’occurrence d’un
                       événement.


                On dispose donc de deux séries de données, de même taille X1 , . . . , Xn et
                Y1 , . . . , Yn , où Xj et Yj ont toutes deux été mesurées sur le j-ième membre
                de l’échantillon.




6/44
~~~

## Page 7

~~~text
  Test de comparaison de deux échantillons                                 Test de comparaison de plusieurs échantillons



  Exemple introductif 1.


         Chez un échantillon de 30 sujets extrait d’une population, on mesure le rythme
         cardiaque (exprimé en pulsations par minute), noté X avant, et Y après
         administration d’un médicament, car on se demande si l’absorption de ce
         médicament a un effet sur le rythme cardiaque. On considère donc ici deux
         échantillons appariés (ou dépendants) (X1 , . . . , X30 ) et (Y1 , . . . , Y30 ) On
         obtient les résultats suivants :

           Patient     1       2      3      4    5    6     7    8   9        10     11     12     13      14     15
              x        80     80      82     75   80   74   80   72   91       88     70     65     83      74     81
              y        85     84      87     81   79   85   87   78   96       80     82     73     89      85     86
           Patient     16     17      18     19   20   21   22   23   24       25     26     27     28      29     30
              x        68     69      71     70   73   78   75   76   78       77     75     72     71      75     78
              y        72     74      77     75   81   70   77   76   82       83     80     80     81      76     77



             L’absorption du médicament affecte-t-elle le rythme cardiaque de manière
                                         significative ?



7/44
~~~

## Page 8

~~~text
  Test de comparaison de deux échantillons                             Test de comparaison de plusieurs échantillons




          Modélisation.
                  X1 , . . . , Xn i.i.d distribuées selon une loi d’espérance µ1 ,
                 Y1 , . . . , Yn i.i.d distribuées selon une loi éventuellement différente
                 d’espérance µ2 .
           Ici, on ne pourra supposer que les Xj sont indépendantes des Yj (même sujet,
           j, qui influe à la fois sur Xj et Yj ).


          Cadre et tests.
           On s’intéressera plutôt aux différences : Dj = Xj − Yj .
              1   Les variables aléatoires D1 , . . . , Dn sont i.i.d. selon une loi d’espérance
                  µ = µ1 − µ2 .
              2   Il s’agit alors de tester : H0 ∶ µ = 0 contre :
                         H1 ∶ µ ≠ 0, ou
                         H1 ∶ µ > 0, ou encore
                         H1 ∶ µ < 0.


8/44
~~~

## Page 9

~~~text
  Test de comparaison de deux échantillons                      Test de comparaison de plusieurs échantillons




         Test de comparaison de moyennes sur échantillons appariés
                Dans le cas des échantillons appariés on applique les techniques du
                chapitre précédent CM3.
                                            1 n
                La statistique de test : D = ∑ Dj .
                                            n j=1
                                                            1 n
                La variance empirique corrigée est S∗2
                                                    D =
                                                                          2
                                                                ∑ (Dj − D) .
                                                          n − 1 j=1




9/44
~~~

## Page 10

~~~text
  Test de comparaison de deux échantillons                                 Test de comparaison de plusieurs échantillons




               Échantillons indépendants.
                On dispose de mesures d’une même grandeur (salaire, taille, etc.) sur deux
                échantillons extraits indépendamment de deux populations différentes :
                    1   Population
                        :::::::::::
                                   1 : Le caractère est noté par X.
                        Soit x1 , . . . , xn1 les réalisations d’un échantillon de v.a. X1 , . . . , Xn1
                        de taille n1 , extrait de cette population et tels que

                                              E(Xi ) = µ1     et   Var(Xi ) = σ12 .

                    2   Population
                        :::::::::::
                                   2 : Le caractère est noté par Y.
                        Soit y1 , . . . , yn2 les réalisations d’un échantillon de v.a. Y1 , . . . , Yn2
                        de taille n2 , extrait de cette population et tels que

                                              E(Yj ) = µ2     et   Var(Yj ) = σ22 .



                Les variables Xi et Yj sont supposées indépendantes (mesures réalisées sur
                des individus nécessairement différents).

10/44
~~~

## Page 11

~~~text
  Test de comparaison de deux échantillons                       Test de comparaison de plusieurs échantillons



  Exemple introductif 2.




         Des essais cliniques sont menés auprès de 137 patients atteints d’une maladie
         pulmonaire sans gravité afin de tester l’efficacité d’un traitement. Le protocole
         est le suivant :
                Des exercices respiratoires sont prescrits à 67 patients choisis au hasard
                ainsi qu’un placebo (groupe témoin (A)).
                Les mêmes exercices respiratoires sont prescrits aux 70 autres patients
                ainsi que le traitement (groupe traité (B)).
                Au bout de trois mois, l’amélioration de la capacité pulmonaire de chaque
                patient est mesurée. L’amélioration est mesurée sur une échelle de 0 (pas
                d’amélioration) à 10 (récupération totale).




11/44
~~~

## Page 12

~~~text
  Test de comparaison de deux échantillons                            Test de comparaison de plusieurs échantillons



  Exemple introductif 2.




                               Amélioration   Groupe témoin (A)   Groupe traité (B)
                                    0                   2                  0
                                    1                   8                  0
                                    2                   4                  3
                                    3                   7                  0
                                    4                  14                 10
                                    5                   9                 14
                                    6                   5                 13
                                    7                   4                 17
                                    8                   7                 10
                                    9                   2                  3
                                   10                   5                  0
                                Ensemble            n1 = 67            n2 = 70
                                                  x = 4.776          y = 5. 671
                                                  s21 = 7.479        s22 = 2.601




12/44
~~~

## Page 13

~~~text
  Test de comparaison de deux échantillons                         Test de comparaison de plusieurs échantillons



  Exemple introductif 2.


            ∎ L’amélioration moyenne du groupe traité est supérieure de 0,9 points à
                celle du groupe témoin.
            ∎ Le problème est de savoir si cette différence moyenne d’amélioration
              entre les deux échantillons doit être attribuée aux bienfaits du
              traitement ou aux fluctuations d’échantillonnage (le même protocole sur
              d’autres individus n’aurait sans doute pas donné les mêmes résultats).
            ∎ Autrement dit, la différence observée entre les deux moyennes empiriques
              est-elle statistiquement significative ?


               Le caractère étudié est l’amélioration :
                       Soit X la v.a. qui associe à la personne choisie son amélioration sans
                       traitement. L’espérance µ1 et l’écart-type σ1 de X sont inconnus.
                       Soit Y la v.a. qui associe à la personne choisie son amélioration après
                       traitement. L’espérance µ2 et l’écart-type σ2 de Y sont inconnus.


         Il s’agit de construire un test de comparaison des deux espérances µ1 et µ2 .

13/44
~~~

## Page 14

~~~text
  Test de comparaison de deux échantillons                              Test de comparaison de plusieurs échantillons



  Exemple introductif 2.




         Les hypothèses de test
            1   Le laboratoire qui veut mettre sur le marché le traitement tient à
                l’hypothèse selon laquelle son médicament (groupe B) est plus efficace
                qu’un placebo (groupe A). L’intérêt du laboratoire est de contrôler l’erreur
                qui consiste à décider à tort que le placebo est plus efficace que le
                médicament et donc ainsi de poser le test sous la forme :

                                             H0 ∶ µ1 = µ2 contre H1 ∶ µ1 > µ2 .
            2   En revanche, l’agence de sécurité sanitaire qui délivre l’autorisation de
                mise sur le marché du traitement, veut contrôler la probabilité de décider
                à tort que le médicament est plus efficace que le placebo. Cette agence
                pose le test sous la forme :

                                             H0 ∶ µ1 = µ2 contre H1 ∶ µ1 < µ2 .




14/44
~~~

## Page 15

~~~text
  Test de comparaison de deux échantillons                         Test de comparaison de plusieurs échantillons




            Problème posé.
        ◇
        ◇   A l’aide des deux échantillons on veut comparer ces deux populations. Celà revient
        ◇
        ◇   à comparer les paramètres des lois de probabilités des Xi et Yj . Pour un test de
        ◇
        ◇
        ◇
            comparaison sur les espérances, on se demande si l’espérance de la grandeur
        ◇
        ◇   considérée est la même dans les deux populations. On veut donc tester
        ◇
        ◇
        ◇
        ◇                                     H 0 ∶ µ1 = µ2 ,
        ◇
        ◇
        ◇
        ◇
        ◇
        ◇
        ◇
        ◇
               ♠ contre l’alternative bilatérale H0 ∶ µ1 ≠ µ2 ,
        ◇
        ◇
        ◇
               ♠ ou contre l’alternative unilatérale H0 ∶ µ1 < µ2 „
        ◇
        ◇      ♠ ou contre l’autre l’alternative unilatérale H0 ∶ µ1 > µ2 ,


            Piste de tests.
        ◇
        ◇
        ◇
                 Il est naturel de fonder les tests de H0 sur l’écart D = Xn1 − Yn2 entre les
        ◇
        ◇        moyennes observées des deux échantillons.
        ◇
        ◇
        ◇
        ◇
                 Sous l’hypothèse H0 , la différence observée Xn1 − Yn2 doit avoir une
        ◇
        ◇
                 espérance nulle puisque E (Xn1 ) − E (Yn2 ) = µ1 − µ2 = 0.
        ◇
        ◇        Il faut donc connaître la loi de Xn1 − Yn2 sous H0 .
15/44
~~~

## Page 16

~~~text
  Test de comparaison de deux échantillons                        Test de comparaison de plusieurs échantillons




         Statistique de test.
         La différence D = Xn1 − Yn2 est un estimateur naturel de µ1 − µ2 . C’est notre
         variable de décision .


            1   E(D) = E (Xn1 − Yn2 ) = µ1 − µ2 . C’est un estimateur sans biais.
            2   Par indépendance des deux échantillons,

                                                                                 σX2 σY2
                        Var(D) = Var (Xn1 − Yn2 ) = Var (Xn1 ) + Var (Yn2 ) =       +    .
                                                                                 n1   n2

         On va distinguer deux cas :
                Cas des grands échantillons de loi quelconque (avec variances connues,
                avec variances inconnues, avec variances connues et égales).
                Cas des petits échantillons gaussiens.




16/44
~~~

## Page 17

~~~text
Test de comparaison de deux espérances de deux échantillons
               indépendants de grande taille


Si les deux échantillons sont de grandes tailles : n1 > 30 et n2 > 30.
  ⊠ Pour un échantillon assez grand, on approche la loi de variable de décision
                                                     σ2 σ2
    grâce au T.C.L. par une loi normale N (µ1 − µ2 , 1 + 2 ).
                                                     n1 n2
  ⊠ On distinguera 3 cas :
       1   Cas où les variances σ12 et σ22 sont connues.
       2   Cas où les variances σ12 et σ22 sont inconnues.
       3   Cas où les variances σ12 et σ22 sont inconnues mais égales.



Dans chacun des cas, on précisera la règle de décision selon les hypothèses,
hypothèse nulle H0 ∶ µ1 = µ2
     contre H1 ∶ µ1 ≠ µ2 .
     ou contre H1 ∶ µ1 > µ2 .
     ou contre H1 ∶ µ1 < µ2 .
~~~

## Page 18

~~~text
Test de comparaison de deux espérances de deux échantillons
               indépendants de grande taille


           1. Cas où les variances σ12 et σ22 sont connues.
~~~

## Page 19

~~~text
                       Test de H0 ∶ µ1 = µ2 contre H1 ∶ µ1 ≠ µ2




    Construction de test d’égalité des moyennes – Cas où σ12 et σ22 sont connues.
◇
◇
◇
      1   La variable de décision : On considère D = Xn1 − Yn2 comme statistique de
◇
          :::::::::::::::::::
◇
◇
          test.
◇
◇         La loi asymptotique de D est la loi normale. On utilisera la variable pivotale
◇
◇                               D
◇
◇
          et sous H0 , Z = √             de loi N (0, 1).
◇                             σ1 σ22
                                2
◇
◇
                                  +
◇
◇
                              n1 n2
◇
◇
      2   Allure de la région critique : Pus la différence est loin de 0 et moins il y a
◇
          ::::::::::::::::::::::
◇
◇
          de chance que l’hypothèse H0 soit vraie, donc la région critique est de la
◇         forme W = {∣D∣ > C }. (C>0)
~~~

## Page 20

~~~text
                      Test de H0 ∶ µ1 = µ2 contre H1 ∶ µ1 ≠ µ2




    Construction de test d’égalité des moyennes – Cas où σ12 et σ22 sont connues.
◇
◇
      3   La région critique : W = {∣D∣ > C }. Sous l’hypothèse H0 et avec un risque
◇
          :::::::::::::::
◇
◇
          de première espèce α, on détermine le seuil C :
◇
◇
           P (W ∣ H0 est vraie) = α ⇐⇒ P (∣D∣ > C ) = α
◇
◇
◇
◇
◇
                                              ⎛                    ⎞
◇
◇
                                              ⎜   ∣D∣        C     ⎟
◇
                                              ⎜                    ⎟=α
◇
                                      ⇐⇒     P⎜√         >√        ⎟
◇
                                                   2   2     2   2
                                              ⎜  σ1 σ2      σ1 σ2 ⎟
◇
◇
                                              ⎝      +         +   ⎠
◇
                                                 n1 n2      n1 n2
◇
◇
◇
◇                                            P (∣Z∣ > ℓ) = α
◇
                                      ⇐⇒
◇
◇
◇
◇                                            P (Z ≤ ℓ) = 1 −
                                                                α
◇
                                      ⇐⇒
                                                                2
◇
◇
◇
◇
                                                            α
◇                                     ⇐⇒     FZ (ℓ) = 1 −
                                                            2
~~~

## Page 21

~~~text
                           Test de H0 ∶ µ1 = µ2 contre H1 ∶ µ1 ≠ µ2




    Construction de test d’égalité des moyennes – Cas où σ12 et σ22 sont connues.
◇
◇                      C
◇
◇
          où ℓ = √              . Par lecture sur la table de la loi normale centrée
◇
◇
                     σ12σ2
                       + 2
◇
◇
                     n1 n2
◇
                                                                           √
◇
◇
                                                     α                         σ12 σ22
◇
          réduite, on déduit le quantile d’ordre 1 −   , ℓ puis C = ℓ ×           +    .
◇
◇
                                                     2                         n1 n2
◇
◇     4   La règle de décision :
◇
◇
          :::::::::::::::::

◇
◇
               Si ∣D∣ < C , on valide (H0 ), les moyennes sont égales.
◇              Si ∣D∣ > C , on valide (H1 ), les moyennes sont différentes.
~~~

## Page 22

~~~text
                    Test de H0 ∶ µ1 = µ2 contre H1 ∶ µ1 < µ2



  Construction de test d’égalité des moyennes – Cas où σ12 et σ22 sont connues.
◇
◇ Les premières étapes sont les mêmes. L’allure de la région critique change.
◇
◇
◇
◇
    1 l’allure de la région critique est de la forme W = {D < C }. (C<0)

◇
◇
◇
    2 Le seuil C est déterminé de la façon suivante :

◇
◇
◇
◇
   P (W ∣ H0 est vraie) = α ⇐⇒ P (D < C ) = α ⇐⇒ P (Z < ℓ) = α ⇐⇒ FZ (ℓ) = α
◇
◇
◇
◇
◇
                    C
◇
◇
       où ℓ = √
                  σ1 σ22
                   2
                           . Par lecture sur la table de la loi normale centrée
◇
◇
◇
                      +
◇
                  n1 n2
◇
                                                                    √
◇
◇      réduite, on déduit  le quantile  d’ordre α , ℓ puis C    ℓ
                                                                      σ12 σ22
                                                                              .
◇
                                                              =   ×       +
◇
                                                                      n1 n2
◇
◇
◇
    3 La règle de décision : Sous H , Z a tendance a prendre des valeurs plus
       :::::::::::::::::               1
◇
◇      petites.
◇
◇
◇
◇
             Si D > C , on valide (H0 ), les moyennes sont égales.
◇            Si D < C , on valide (H1 ), les moyennes sont différentes.
~~~

## Page 23

~~~text
                     Test de H0 ∶ µ1 = µ2 contre H1 ∶ µ1 > µ2


  Construction de test d’égalité des moyennes – Cas où σ12 et σ22 sont connues.
◇
◇ Les premières étapes sont les mêmes. L’allure de la région critique change.
◇
◇
◇
◇
     1 l’allure de la région critique est de la forme W = {D > C }. (C>0)

◇
◇
◇
     2 Le seuil C est déterminé de la façon suivante :

◇
◇
◇
◇
  P (W ∣ H0 est vraie) = α ⇐⇒ P (D > C ) = α ⇐⇒ P (Z > ℓ) = α ⇐⇒ FZ (ℓ) = 1−α
◇
◇
◇
◇
◇
                     C
◇
◇
       où ℓ = √
                   σ1 σ22
                    2
                            . Par lecture sur la table de la loi normale centrée
◇
◇
◇
                       +
◇
                   n1 n2
◇
                                                                         √
◇
◇      réduite,  on déduit  le quantile  d’ordre 1   α , ℓ puis  C   ℓ
                                                                           σ12 σ22
                                                                                   .
◇
                                                   −               =   ×      +
◇
                                                                           n1 n2
◇
◇
◇
     3 La règle de décision : Sous H , Z a tendance a prendre des valeurs plus
       :::::::::::::::::                1
◇
◇      grandes.
◇
◇
◇
◇
              Si D < C , on valide (H0 ), les moyennes sont égales.
◇             Si D > C , on valide (H1 ), les moyennes sont différentes.
~~~

## Page 24

~~~text
Test de comparaison de deux espérances de deux échantillons
               indépendants de grande taille


          2. Cas où les variances σ12 et σ22 sont inconnues.
~~~

## Page 25

~~~text
    Construction de test d’égalité des moyennes – Cas où σ12 et σ22 sont inconnues.
◇
◇     ⊠ La variable de décision : On considère D = Xn1 − Yn2 comme statistique de
◇
◇
        :::::::::::::::::::

◇
        test.
◇
◇                                                               σ2 σ2
◇
◇
      ⊠ La loi asymptotique de D est la loi normale de variance 1 + 2 .
◇
◇
                                                                n1 n2
◇
◇     ⊠ Comme σ12 et σ22 sont inconnues, on les remplace respectivement par leur
◇
◇       estimation s∗2    ∗2
                    1 et s2 .
◇
◇
◇
◇
      ⊠ Pour un échantillon assez grand, on approche la loi de variable de décision
◇
◇                                                        s∗2 s∗2
◇
◇
        grâce au T.C.L. par une loi normale N (µ1 − µ2 , 1 + 2 ).
◇
                                                         n1    n2
◇
◇
◇
      ⊠ On transforme la variable de décision en une variable de décision pivotale.
◇
◇                                              D         Xn − Yn2
◇
◇
        Sous l’hypothèse nulle H0 , Zn = √
                                             ∗2    ∗2
                                                      =√ 1            est
◇                                           s1   s         s∗2   s∗2
◇                                               + 2         1
                                                               + 2
◇
◇                                           n1    n2       n1     n2
◇       approximativement de loi normale centrée réduite N (0, 1).


    Pour les différents tests, on procède de la même façon que dans le cas précédent.
~~~

## Page 26

~~~text
Test de comparaison de deux espérances de deux échantillons
               indépendants de grande taille


      3. Cas où les variances σ12 et σ22 sont inconnues mais égales.
~~~

## Page 27

~~~text
    Construction de test d’égalité des moyennes – Cas où σ12 = σ22 et inconnues.
◇
◇     ⊠ Comme les variances sont inconnues mais égales σ12 = σ22 , on estime la valeur
◇
◇                                             (n1 − 1)s∗2            ∗2
◇
◇       commune σ 2 par la statistique : S2 =          1 + (n2 − 1)s2
                                                                        .
◇
◇
                                                     n1 + n2 − 2
◇
◇       S2 est un estimateur sans biais de σ 2 .
◇
◇
◇
◇
                              σ2 σ2 σ2 σ2
      ⊠ On estime la variance 1 + 2 =
                                                         1  1
                                                  = σ 2 ( + ) de la variable de
◇
                                              +
◇
                              n1 n2 n1 n2                n1 n2
◇
◇
        test D par :
◇
◇
                                             1   1
                                        S2 ( + ) .
◇
◇                                           n1 n2
◇
◇
◇
◇
      ⊠ Pour un échantillon assez grand, on approche la loi de variable de décision
◇
◇
                                                              1
        grâce au T.C.L. par une loi normale N (µ1 − µ2 , S2 ( + )).
                                                                   1
◇
◇
                                                              n1 n2
◇
◇     ⊠ On transforme la variable de décision en une variable de décision pivotale.
◇
◇
◇
                                              D           Xn − Yn2
◇
◇
        Sous l’hypothèse nulle H0 , Zn = √           = √1             est
◇
                                              1   1          1    1
◇
◇
                                        S       +
                                             n1 n2
                                                        S       +
                                                             n1 n2
◇
◇       approximativement de loi normale centrée réduite N (0, 1).


    Pour les différents tests, on procède de la même façon que dans le cas précédent.
~~~

## Page 28

~~~text
Test de comparaison de deux espérances de deux échantillons
               indépendants de petite taille


On s’intéresse dans cette partie aux échantillons gaussiens. On traitera les cas :
  1   Cas où les variances sont connues.
  2   Cas où les variances σ12 et σ22 sont inconnues mais égales.
~~~

## Page 29

~~~text
  Test de comparaison de deux échantillons                                Test de comparaison de plusieurs échantillons




         Si les deux échantillons sont de petites tailles et suivent la loi normale

                                        X ∼ N (µ1 , σ12 ) , Y ∼ N (µ2 , σ22 ) .


            ⊠ La variable de décision D = Xn1 − Yn2 est un estimateur naturel de µ1 − µ2 .
            ⊠ La loi exacte de l’estimateur D est la loi normale, de paramètres (par
              indépendance) :
                                                      σ2 σ2
                                        N (µ1 − µ2 , 1 + 2 ) .
                                                      n1 n2
                                                               σ12 σ22
            ⊠ Sous l’hypothèse nulle H0 , D ∼ N (0,               +    ).
                                                               n1 n2




29/44
~~~

## Page 30

~~~text
  Test de comparaison de deux échantillons                       Test de comparaison de plusieurs échantillons




          Construction de test d’égalité des moyennes – Cas petits échantillons gaussiens
          de variances connues.
        ◇
        ◇
        ◇
             1 La variable de décision : On considère D = X
               :::::::::::::::::::                            n1 − Yn2 comme statistique de
        ◇
        ◇      test.
        ◇
        ◇                                                              D
        ◇
        ◇
               On utilisera la variable pivotale et sous H0 , Z = √          de loi normale
        ◇                                                            σ1 σ22
                                                                       2
        ◇
        ◇                                                                +
        ◇
        ◇
                                                                     n1 n2
        ◇
        ◇
               centrée réduite.
        ◇
        ◇    2   Allure de la région critique :
        ◇
        ◇
                 ::::::::::::::::::::::

        ◇
        ◇
                       la région critique est de la forme W = {∣D∣ > C } (C>0) si
        ◇
        ◇                               H0 ∶ µ1 = µ2 contre H1 ∶ µ1 ≠ µ2 .
        ◇
        ◇
        ◇
        ◇
                       la région critique est de la forme W = {D > C } (C>0) si
        ◇
        ◇                               H0 ∶ µ1 = µ2 contre H1 ∶ µ1 > µ2 .
        ◇
        ◇
        ◇
                       la région critique est de la forme W = {D < C } (C<0) si
        ◇
        ◇                               H0 ∶ µ1 = µ2 contre H1 ∶ µ1 < µ2 .
        ◇
        ◇
        ◇
        ◇
                 On procède de la même façon que les cas précédents où la loi pivotale est
        ◇        normale centrée réduite.

30/44
~~~

## Page 31

~~~text
  Test de comparaison de deux échantillons                       Test de comparaison de plusieurs échantillons




          Construction de test d’égalité des moyennes – Cas petits échantillons gaussiens
          de variances σ12 = σ22 et inconnues.
        ◇
        ◇
        ◇
             1 La variable de décision : On considère D = X
                                                            n1 − Yn2 comme statistique de
        ◇
               :::::::::::::::::::
        ◇
        ◇
               test.
        ◇
        ◇
                     D
        ◇
            ↝ √              ∼ N (0; 1). Comme les variances sont inconnues et sont égales,
        ◇
        ◇
                   σ1 σ22
                     2

        ◇
        ◇
                       +
                   n1 n2
        ◇
        ◇      on remplace la variance de D par son estimateur S2 .
        ◇
        ◇
        ◇
        ◇
             ↝ Comme les échantillons sont petits, la variable pivotale et sous H0 ,
        ◇
        ◇
                       D
        ◇
        ◇
               Z= √           suit la loi de student à n1 + n2 − 2 d.d.l.
        ◇
                      1     1
        ◇
        ◇
                  S      +
                      n1 n2
        ◇
        ◇
        ◇
        ◇
             2   Allure de la région critique :
                 ::::::::::::::::::::::
        ◇
        ◇
        ◇
                       la région critique est de la forme W = {∣D∣ > C } (C>0) si
        ◇
        ◇                               H0 ∶ µ1 = µ2 contre H1 ∶ µ1 ≠ µ2 .
        ◇
        ◇
        ◇
        ◇
                       la région critique est de la forme W = {D > C } (C>0) si
        ◇
        ◇                               H0 ∶ µ1 = µ2 contre H1 ∶ µ1 > µ2 .
        ◇
        ◇
        ◇
                       la région critique est de la forme W = {D < C } (C<0) si
        ◇
        ◇                               H0 ∶ µ1 = µ2 contre H1 ∶ µ1 < µ2 .
31/44
~~~

## Page 32

~~~text
  Cas : H0 ∶ µ1 = µ2 contre H1 ∶ µ1 ≠ µ2 .
◇
◇
     3 La région critique : W = {∣D∣ > C }. Sous l’hypothèse H0 et avec un risque
◇
◇
       :::::::::::::::
       de première espèce α, on détermine le seuil C>0 :
◇
◇
◇
        P (W ∣ H0 est vraie) = α ⇐⇒ P (∣D∣ > C ) = α
◇
◇
◇
◇
◇
                                             ⎛                             ⎞
◇
◇
                                             ⎜                      C      ⎟
◇
                                             ⎜      ∣D∣                    ⎟=α
◇
                                    ⇐⇒ P ⎜ √                  > √          ⎟
◇                                                   1     1         1    1
                                             ⎜                             ⎟
◇
◇
                                             ⎝ S       +       S      +
                                                                   n1 n2 ⎠
◇
                                                    n1 n2
◇
◇
◇
◇                                   ⇐⇒ P (∣Z∣ > ℓ) = α
◇
◇
◇
◇                                                           α
◇
◇
                                    ⇐⇒ P (Z ≤ ℓ) = 1 −
◇
                                                            2
◇
◇
◇
◇                                   ⇐⇒ FZ (ℓ) = 1 −
                                                        α
◇
◇
                                                        2
◇
◇ où ℓ = √
                C
                       . Par lecture sur la table de la loi de Student, on déduit ℓ
◇
◇              1     1
◇
◇
         S        +
◇
               n1 n2
◇
◇                 student d’ordre 1 − α2 et de d.d.d égal à n1 + n2 − 2 puis C =
◇
  le quantile de
◇
◇
       √
◇
◇ ℓ×S
          1     1
              + .
◇         n1 n2
~~~

## Page 33

~~~text
  Test de comparaison de deux échantillons                         Test de comparaison de plusieurs échantillons




          Cas petits échantillons gaussiens de même variance. Construction de test d’éga-
          lité des moyennes
        ◇
        ◇
              4 La règle de décision :

        ◇
        ◇
                :::::::::::::::::

        ◇
        ◇
                       Si ∣D∣ < C , on valide (H0 ), les moyennes sont égales.
        ◇              Si ∣D∣ > C , on valide (H1 ), les moyennes sont différentes.




33/44
~~~

## Page 34

~~~text
  Cas : H0 ∶ µ1 = µ2 contre H1 ∶ µ1 > µ2 .
◇
◇   3  La région critique : W = {D > C }. Sous l’hypothèse H0 et avec un risque
◇
◇
       :::::::::::::::

◇
       de première espèce α, on détermine le seuil C>0 :
◇
◇
◇
◇
◇
◇ P (W ∣ H0 est vraie) = α ⇔ P (D > C ) = α ⇔ P (Z ≤ ℓ) = 1 − α ⇔ FZ (ℓ) = 1 − α
◇
◇
◇
◇
◇
  Par lecture sur la table de la loi de Student, on déduit ℓ le quantile de student
◇
◇ d’ordre 1 − α et de d.d.l égal à n1 + n2 − 2.


  Cas : H0 ∶ µ1 = µ2 contre H1 ∶ µ1 < µ2 .
◇
◇      La région critique : W = {D < C }. Sous l’hypothèse H0 et avec un risque
◇
    3
       :::::::::::::::
◇
◇
       de première espèce α, on détermine le seuil C<0 :
◇
◇
◇
◇
◇
◇     P (W ∣ H0 est vraie) = α ⇔ P (D < C ) = α ⇔ P (Z ≤ ℓ) = α ⇔ FZ (ℓ) = α
◇
◇
◇
◇
◇
  Par lecture sur la table de la loi de Student, on déduit ℓ le quantile de student
◇
◇ d’ordre α et de d.d.l égal à n1 + n2 − 2.
~~~

## Page 35

~~~text
           Test de comparaison de deux variances

Le test de Fisher ne fonctionne que si le caractère est distribué dans les deux
populations suivant une loi normale.



     2 échantillons gaussiens

     On considère deux échantillons indépendants et gaussiens :

                         X1 , X2 , . . . , Xn1 et Y1 , Y2 , . . . , Yn2

     représentant les variables aléatoires X ∼ N (µ1 , σ12 ) et Y ∼ N (µ2 , σ22 ).
          E(X) = µ1 et Var(X) = σ12 .
          E(Y) = µ2 et Var(Y) = σ22 .
     Les variances empiriques corrigées

                   1 n1                                        1 n2
          S∗2                                       S∗2
                                     2                                           2
           1 =          ∑ (Xi − Xn1 )          et    2 =            ∑ (Yi − Yn2 )
                 n1 − 1 i=1                                  n2 − 1 i=1

     sont des estimateurs sans biais respectivement des variances σ12 et σ22
~~~

## Page 36

~~~text
Test de Fisher – Test d’égalité de variances
Dans le cas gaussien, le test de Fisher consiste à faire la rapport entre les deux
variances et de tester si le rapport est égal à 1.
                            ⎧ H       ∶       σ1    =   σ2
                            ⎪ 0
                            ⎪
                            ⎪
                            ⎨
                            ⎪
                            ⎪
                            ⎩ H1
                            ⎪         ∶       σ1    ≠   σ2

Autrement dit,

                               ⎧                   σ1
                               ⎪
                               ⎪ H0       ∶           =1
                               ⎪
                               ⎪
                               ⎪                   σ2
                               ⎨
                               ⎪
                               ⎪
                               ⎪                   σ1
                               ⎪ H        ∶           ≠1
                               ⎩ 1
                               ⎪
                                                   σ2


La statistique de test
                                              S∗2
                                               1
Le test va être fondé sur le rapport K =          que l’on comparera à la valeur de
                                              S∗2
                                               2
référence 1.
~~~

## Page 37

~~~text
  Test de comparaison de deux échantillons                        Test de comparaison de plusieurs échantillons



  La loi de la statistique de test




        Loi de Fisher
         Soient X et Y deux v.a. indépendantes telles que X ∼ χ2d1 et Y ∼ χ2d2 . Alors la v.a.

                                             X/d1
                                                  ∼ F(d1 , d2 )
                                             Y/d2

         F(d1 , d2 ) étant la loi de de Fisher à d1 et d2 degrés de liberté.


         La loi de Fisher est une loi non symétrique et une v.a. de Fisher ne prend que
         des valeurs positives




37/44
~~~

## Page 38

~~~text
  Test de comparaison de deux échantillons                                Test de comparaison de plusieurs échantillons



  La loi de la statistique de test


        La loi de la statistique de test K.
         Comme les échantillons sont gaussiens alors :

                                  (n1 − 1)S∗2              (n2 − 1)S∗2
                                        2
                                           1
                                              ∼ χ2n1 −1 et          2
                                                                       ∼ χ2n2 −1
                                      σ1                       σ22

         Les échantillons sont indépendants donc

                                       (n1 − 1)S∗2
                                                1
                                   (               ) /(n1 − 1)
                                           σ12
                                                                 ∼ F(n1 − 1, n2 − 1)
                                       (n2 − 1)S∗2
                                                2
                                   (               ) /(n2 − 1)
                                           σ22

         Sous l’hypothèse H0 , σ12 = σ22 , donc, sous H0 , la variable

                                               S∗2
                                                1
                                                   ∼ F(n1 − 1, n2 − 1).
                                               S∗2
                                                2

         Donc, sous H0 , K ∼ F(n1 − 1, n2 − 1).
38/44
~~~

## Page 39

~~~text
  Test de comparaison de deux échantillons                          Test de comparaison de plusieurs échantillons



  Règle de décision




        Région critique.
            ↝ Le test d’hypothèses H0 ∶ σ12 = σ22 contre H1 ∶ σ12 ≠ σ22 .
            ↝ La région critique est sous la forme W = {K < C1 ou K > C2 } où C1 < 1 et
              C2 > 1.
            ↝ Sous l’hypothèse H0 et avec un risque de premier espèce α, on détermine
              les seuils C1 et C2 .
                P (W ∣ H0 est vraie) = α ⇐⇒ P (K < C1 ou K > C2 ) = α

                                                  ⇐⇒   P (K < C1 ) + P (K > C2 ) = α
                Sous H0 , K ∼ F(n1 − 1, n2 − 1), on choisit C1 et C2 tels que
                          X
                          X                      α X
                                                   X         X
                                                             X                        α   X
                                                                                          X
                          X
                          X P (K < C1 )      =     X
                                                   X         X
                                                             X P (K < C1 )      =         X
                                                                                          X
                          X
                          X
                          X
                          X                      2 X
                                                   X
                                                   X
                                                   X
                                                             X
                                                             X
                                                             X                        2   X
                                                                                          X
                                                                                          X
                          X
                          X
                          X                        X
                                                   X   Soit, X
                                                             X
                                                             X                            X
                                                                                          X
                                                                                          X
                          X
                          X
                          X                      α X
                                                   X
                                                   X
                                                   X
                                                             X
                                                             X
                                                             X
                                                             X                          α X
                                                                                          X
                                                                                          X
                                                                                          X
                          X
                          X P (K > C2 )      =     X
                                                   X         X
                                                             X P (K ≤ C2 )      =    1−   X
                                                                                          X
                          X
                          X                      2 X
                                                   X         X
                                                             X                          2 X
                                                                                          X


39/44
~~~

## Page 40

~~~text
      Test de comparaison de plusieurs échantillons

On se propose de comparer plusieurs échantillons à travers une égalité des
espérances et les différentes mesures de la variance nous permettront
d’effectuer ces tests.


Plusieurs échantillons
On considère k ≥ 3 échantillons indépendants :
      (1)   (1)                    (2)    (2)                         (k)   (k)
   (X1 , X2 , . . . , X(1)                        (2)                                    (k)
                       n1 ) , (X1 , X2 , . . . , Xn2 ) , . . . . . . (X1 , X2 , . . . , Xnk )


représentant les variables aléatoires X(1) , X(2) ,. . ., X(k) .
     Hypothèses à tester :

                H0   ∶   Les k échantillons sont issus de la même population
            {
                H1   ∶   Il y a au moins un échantillon différent des autres

     Dans le cas où les échantillons sont gaussiens de même variance, nous
     utiliserons le test d’analyse de variance ANOVA.
~~~

## Page 41

~~~text
  Test de comparaison de deux échantillons                                    Test de comparaison de plusieurs échantillons



  Principe de l’ANOVA




                On a k échantillons de taille n1 ; n2 ; . . . ; nk .

                                                 (j)   (j)        (j)
                Le j-ème échantillon (X1 , X2 , . . . , Xnj ) est associé à la v.a. X(j) .
                Les échantillons sont gaussiens, indépendants et de même variance :

                                      X(j) ∼ N (µj , σ 2 ) , pour tout j = 1, . . . , k.

                On va donc tester :
                                                  H0    ∶    µ1 = µ2 = . . . = µk
                                             {
                                                  H1    ∶    ∃(i, j) µi ≠ µj

                Ce sont les différentes mesures de variance qui vont nous permettre de
                décider.




41/44
~~~

## Page 42

~~~text
  Test de comparaison de deux échantillons                  Test de comparaison de plusieurs échantillons



  Quelques définitions



                                              Variance empirique d’un échantillon


                                                             1 nj            2
                                                  V (j) =       ∑ (Xi − X )
                                                                    (j)  (j)
         Moyenne empirique d’un échantillon
                                                             nj i=1
                                  1 nj (j)
                              =      ∑X
                        (j)
                      X
                                  nj i=1 i
                                              Variance intra-classes
                                                                      k  nj (j)
         Moyenne de l’échantillon                      Vintra = ∑          V
                                                                     j=1 n
                              1 k nj (j)
                      X=        ∑∑X
                              n j=1 i=1 i
                                              Variance inter-classes
         où n = n1 + ⋯ + nk
                                                                k             2
                                                                   nj
                                                   Vinter = ∑         (X − X)
                                                                        (j)

                                                               j=1 n



42/44
~~~

## Page 43

~~~text
  Test de comparaison de deux échantillons                          Test de comparaison de plusieurs échantillons



  Résultat principal




        Plusieurs échantillons
            ∎ La variance totale est égale à la somme des variances inter classes et intra
                classes :
                                           Vtot = Vintra + Vinter
                                                 Viner
            ∎ La variable de décision est : D = − 1
                                                 k
                                                 Vintra
                                                 n−1
            ∎ Sous l’hypothèse H0 , d’égalité des moyennes, D suit la loi de Fisher à
              (k − 1) et (n − 1) degrés de liberté.

                                             D ∼ F (k − 1, n − 1)




43/44
~~~

## Page 44

~~~text
  Test de comparaison de deux échantillons                       Test de comparaison de plusieurs échantillons




        Test ANOVA
            1   La région critique est de la forme : W = {D > C } où C > 0 et C = fractile
                ::::::::::::::
                d’ordre 1 − α pour la loi F (k − 1, n − 1).
            2   La règle de décision est donc :
                :::::::::::::::
                     Si D < C , on valide H0 , les moyennes sont égales. Les échantillons
                     sont issus de la même population.
                     Si D > C , on valide H1 . Il y a au moins un échantillon différent des
                     autres.




44/44
~~~
