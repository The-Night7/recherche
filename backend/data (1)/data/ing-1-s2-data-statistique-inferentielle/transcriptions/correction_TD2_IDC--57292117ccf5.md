# correction_TD2_IDC.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1HuPeBGYGeO3yqA0GDAnhVp2W6jlO7OSD) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
CY Tech  ING1-GM                                                                      Statistiques Inférentielles




                         TD2  Intervalles de Conance
                                            Correction Détaillée
                            Statistiques Inférentielles  1ère année Ingénieurs


    Rappels de cours  Intervalles de conance pour une loi gaussienne
    Soit (X1 , . . . , Xn ) un échantillon i.i.d. de loi N (µ, σ 2 ). On note X n = n1          Xi la moyenne
                                                                                            P
    empirique et Sn = n−1 (Xi − X n )2 la variance empirique corrigée.
                        ∗2    1 P


                                    Xn − µ
    Cas 1 : σ 2 connue       Z=       √ ∼ N (0, 1)
                                    σ/ n
                                                                 
                                                              σ
                                       IC1−α (µ) = x̄n ± zα/2 √
                                                                n

                                       Xn − µ
    Cas 2 : σ 2 inconnue        T =         √ ∼ T (n − 1)
                                       Sn∗ / n
                                                                  s∗n
                                                                     
                                      IC1−α (µ) = x̄n ± tn−1, α/2 √
                                                                    n

                                    (n − 1)Sn∗2
    IC pour σ 2 (µ inconnue)                     ∼ χ2 (n − 1)
                                         σ2
                                             "                          #
                                               (n − 1)s∗2    (n − 1)s∗2
                                IC1−α (σ ) =
                                        2                n
                                                           ; 2       n
                                                χ2n−1, α/2  χn−1, 1−α/2

    Taille d'échantillon (pour une précision ε donnée, σ connue) :
                                                      z
                                                           α/2 σ
                                                                   2
                                                 n≥
                                                            ε



1    Exercice 1  Force de compression d'un ciment
Données : n = 9, x̄9 = 19.72 kg/cm2 , s9∗2 = 0.69, α = 10%.

Question 1 : IC pour µ et σ (σ inconnue)
                                      2     2


    Méthode
    Les deux paramètres µ et σ 2 sont inconnus. On utilise :

        la loi de Student T (n − 1) pour µ,

        la loi du χ2 (n − 1) pour σ 2 .

    Valeurs critiques pour α = 10%, n − 1 = 8 degrés de liberté :
                        t8, 0.05 = 1.860,       χ28, 0.05 = 15.507,     χ28, 0.95 = 2.733

    Intervalle de conance pour µ :
                               √                   s∗   0.831
    On calcule d'abord s∗9 =       0.69 ≈ 0.831 et √9 =       ≈ 0.277.
                                                    n     3

                                                        1
~~~

## Page 2

~~~text
CY Tech  ING1-GM                                                                     Statistiques Inférentielles




                           IC0.90 (µ) = [19.72 ± 1.860 × 0.277] = [19.72 ± 0.515]

    Résultat

                                   IC0.90 (µ) = [19.205 ; 20.235] kg/cm2

    Intervalle de conance pour σ 2 :

                      "                                #
                       (n − 1) s∗2     (n − 1) s∗2
                                                                                             
                                                             8 × 0.69 8 × 0.69      5.52   5.52
       IC0.90 (σ 2 ) =             9
                                     ;             9
                                                           =         ;          =        ;
                         χ28, 0.05       χ28, 0.95            15.507    2.733      15.507 2.733

    Résultat

                                  IC0.90 (σ 2 ) = [0.356 ; 2.020] (kg/cm2 )2


Question 2 : IC pour µ avec σ = 0.69 connue
                                          2


    Méthode
    σ 2 est maintenant supposée connue. On utilise la loi normale standard N (0, 1).

    Valeur critique : z0.05 = 1.645.
                       "                      √        #
                                                  0.69
          IC0.90 (µ) = 19.72 ± 1.645 ×                   = [19.72 ± 1.645 × 0.277] = [19.72 ± 0.456]
                                                  3

    Résultat

                                   IC0.90 (µ) = [19.264 ; 20.176] kg/cm2

    Comparaison :

                                      σ 2 inconnue (Student)         σ 2 connue (normale)
                   Demi-largeur                ± 0.515                       ± 0.456
                   Intervalle             [19.205 ; 20.235]             [19.264 ; 20.176]

    Remarque
    L'intervalle obtenu avec σ 2 connue est plus étroit (±0.456 contre ±0.515). Cela s'explique
    par le fait que connaître σ 2 réduit l'incertitude : la loi de Student possède des queues plus
    lourdes que la loi normale, ce qui élargit mécaniquement l'intervalle.


2    Exercice 2  Poids des pièces de 2¿
Données : σ = 10−1 = 0.1 g (connue), n = 100, x̄100 = 8.55 g.




                                                            2
~~~

## Page 3

~~~text
CY Tech  ING1-GM                                                                              Statistiques Inférentielles




Question 1 : IC à 99% pour µ
    Méthode
    La variance est connue, l'échantillon est grand : on utilise N (0, 1).

    Valeur critique : z0.005 = 2.576 (risque α = 1%, donc α/2 = 0.005).
                                       σ   0.1    0.1
                                       √ =√     =     = 0.01 g
                                        n   100   10

                          IC0.99 (µ) = [8.55 ± 2.576 × 0.01] = [8.55 ± 0.02576]

    Résultat

                                   IC0.99 (µ) = [8.524 ; 8.576] grammes
    Le poids moyen d'une pièce de 2¿ a 99% de chance de se trouver dans cet intervalle.


Question 2 : Taille d'échantillon pour une précision ε = 10 g                          −2


On souhaite que la demi-largeur de l'intervalle à 99% soit inférieure à ε = 0.01 g :

                          σ                     √           zα/2 σ                   z
                                                                                          α/2 σ
                                                                                                  2
                     zα/2 √ < ε        ⇐⇒           n>                    ⇐⇒    n>
                           n                                  ε                            ε

    Application numérique :
                                              2                   2
                                 2.576 × 0.1                0.2576
                        n>                          =                     = (25.76)2 = 663.6
                                    0.01                     0.01

    Résultat
    Il faut prélever au minimum n ≥ 664 pièces pour obtenir une précision inférieure à 10−2
    gramme au niveau de conance 99%.

    Remarque
    La précision demandée (10−2 g) est exactement la demi-largeur obtenue en Q1 avec n = 100.
    On constate que pour diviser celle-ci par un facteur k , il faut multiplier la taille d'échantillon
    par k 2 .


3    Exercice 3  Abonnés au journal Le Monde
Données : n = 25, x̄25 = 6.7 h/semaine, s∗25 = 5.8 h, niveau 1 − α = 95%.
    Méthode
    σ est inconnue et estimée par s∗25 . L'échantillon est de taille modérée (n = 25). On suppose
    la population gaussienne et on utilise la loi de Student T (n − 1) = T (24).

    Valeur critique : Pour α = 5% et n − 1 = 24 degrés de liberté :
                                                t24, 0.025 = 2.064


                                                             3
~~~

## Page 4

~~~text
CY Tech  ING1-GM                                                              Statistiques Inférentielles




  Calcul de la demi-largeur :
                           s∗            5.8         5.8
              t24, 0.025 × √25 = 2.064 × √ = 2.064 ×     = 2.064 × 1.16 ≈ 2.394
                             n            25          5

  Intervalle de conance :
                                     IC0.95 (µ) = [6.7 ± 2.394]

  Résultat

                          IC0.95 (µ) = [4.306 ; 9.094] heures par semaine
  Le temps moyen hebdomadaire de consultation d'internet par les abonnés au       Monde est estimé
  entre 4h18 et 9h06 avec un niveau de conance de 95%.

  Remarque
  L'intervalle est relativement large (≈ 4.8 heures d'amplitude) en raison :

      de la petite taille d'échantillon (n = 25), et

      de la grande variabilité (s∗25 = 5.8 h, soit presque autant que la moyenne).

  Un échantillon plus grand permettrait de réduire cet intervalle.




    Fin de la correction du TD2  Pour toute question ou précision complémentaire, n'hésitez pas !




                                                  4
~~~
