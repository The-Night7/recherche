# correction_TD1_estimation.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1oHR5gVqzgQwmYY-QhyWG4fUKVhfsC1jB) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                        TD1 - Estimateurs
                      Correction Détaillée

            Statistiques Inférentielles - 1ère année Ingénieurs




Rappels de Cours

 Rappel de cours
 Dénitions fondamentales
    Échantillon : Suite de variables aléatoires (X1 , X2 , . . . , Xn ) indépendantes
     et identiquement distribuées (i.i.d.) de même loi que X .
    Estimateur : Une statistique Tn = g(X1 , . . . , Xn ) utilisée pour approcher un
     paramètre inconnu θ.
    Biais : b(Tn ) = E(Tn ) − θ

         Si E(Tn ) = θ, l'estimateur est sans biais
         Si limn→∞ b(Tn ) = 0, l'estimateur est asymptotiquement sans biais
    Risque quadratique : R(Tn ) = E[(Tn − θ)2 ] = Var(Tn ) + b(Tn )2

    Convergence en probabilité : Tn →
                                     − θ si ∀ε > 0, limn→∞ P(|Tn −θ| > ε) = 0
                                               P


                                                            L2
    Convergence en moyenne quadratique : Tn −→ θ si limn→∞ E[(Tn −
     θ)2 ] = 0
                                   √
    Loi asymptotique : Si
                                                   L
                                                 → N (0, σ 2 ), on dit que Tn suit
                                       n(Tn − θ) −
     asymptotiquement N (θ, σn )
                              2




                                           1
~~~

## Page 2

~~~text
CY Tech - ING1-GM                                                   Statistiques Inférentielles


  Rappel de cours
  Estimateur du Maximum de Vraisemblance (EMV)
  La fonction de vraisemblance pour un échantillon (x1 , . . . , xn ) est :
                                              n
                                              Y
                                     L(θ) =         f (xi ; θ)
                                              i=1


  L'EMV θ̂ maximise L(θ) (ou ln L(θ)) :
                                      ∂ ln L(θ)
                                                     =0
                                          ∂θ    θ=θ̂

  Propriétés :
      L'EMV est asymptotiquement sans biais

      L'EMV est convergent

      L'EMV est asymptotiquement ecace (atteint la borne de Cramér-Rao)

  Rappel de cours
  Lois usuelles

      Loi exponentielle E(λ) :

            Densité : f (x) = λe−λx pour x ≥ 0
            E(X) = λ1 , Var(X) = λ12
      Loi de Poisson P(λ) :

            P(X = k) = λ k!e pour k ∈ N
                            k −λ



            E(X) = Var(X) = λ
      Loi binomiale B(n, p) :

          P(X = k) = nk pk (1 − p)n−k
                        

            E(X) = np, Var(X) = np(1 − p)




                                              2
~~~

## Page 3

~~~text
CY Tech - ING1-GM                                              Statistiques Inférentielles

1     Exercice 1 - Temps d'attente au RU

Données
Échantillon de 30 observations : x̄30 = 9 min, s30 = 6.3 min

Question 1 : Quelle loi suit X ?
    Méthode
    Le temps d'attente avant un événement suit généralement une loi exponentielle.

    Le temps d'attente X suit une loi exponentielle de paramètre λ > 0 : X ∼ E(λ).
    Justication :
     La loi exponentielle modélise les durées d'attente

     C'est une loi à mémoire nulle, adaptée aux processus aléatoires

     Le temps d'attente est une variable continue positive

Question 2 : Détermination du paramètre
Pour une loi exponentielle E(λ) :
                                                         1
                                           E(X) =
                                                         λ
    L'estimateur naturel de λ par la méthode des moments est :
                                                     1
                                            λ̂ =
                                                    X̄n
    Avec notre échantillon :
                                    1
                                      ≈ 0.111 min−1
                                    λ̂ =
                                    9
    Vérication : C'est aussi l'EMV de λ pour la loi exponentielle.

Question 3 : Probabilité d'attendre plus de 15 min
Pour X ∼ E(λ) :
                                      P(X > t) = e−λt
    Avec λ̂ = 91 et t = 15 min :
                                           15        5
                        P(X > 15) = e− 9 = e− 3 = e−1.667 ≈ 0.189

   Réponse : La probabilité qu'un étudiant attende plus de 15 minutes est d'environ
18.9%.




                                                3
~~~

## Page 4

~~~text
CY Tech - ING1-GM                                                       Statistiques Inférentielles

2     Exercice 2 - Densité paramétrique

Données                                   (
                                              4x3
                                               θ4
                                                        si x ∈ [0, θ]
                                f (x) =
                                           0            sinon
    Estimateur : Tn = an (X1 + X2 + · · · + Xn )

Question 1 : Calcul de E(X) et Var(X)
Espérance :
                                               Z θ
                                                4x3
                                  E(X) =     x · 4 dx
                                          0      θ
                                            Z θ
                                         4
                                       = 4      x4 dx
                                         θ 0
                                             θ
                                         4 x5
                                       = 4
                                         θ    5 0
                                         4 θ5
                                       = 4·
                                         θ    5
                                         4θ
                                       =
                                          5
    Variance : On calcule d'abord E(X 2 ) :
                                               Z θ
                                      2             4x3
                                 E(X ) =        x2 · 4 dx
                                             0       θ
                                               Z θ
                                            4
                                          = 4      x5 dx
                                            θ 0
                                                θ
                                            4 x6
                                          = 4
                                            θ    6 0
                                            4 θ6
                                          = 4·
                                            θ    6
                                            2θ2
                                          =
                                             3
    Donc :

                               Var(X) = E(X 2 ) − [E(X)]2
                                                    2
                                            2θ2       4θ
                                          =      −
                                             3        5
                                               2
                                            2θ      16θ2
                                          =      −
                                             3      25 
                                                 50 −  48
                                          = θ2
                                                    75
                                               2
                                            2θ
                                          =
                                             75

                                                    4
~~~

## Page 5

~~~text
CY Tech - ING1-GM                                                       Statistiques Inférentielles

Question 2 : Calcul de a et du risque quadratique
                                 n

Calcul de an pour que Tn soit sans biais :
  Par linéarité de l'espérance :
                                    n
                                    X                           4θ   4nan θ
                      E(Tn ) = an          E(Xi ) = an · n ·       =
                                     i=1
                                                                5      5

   Pour que Tn soit sans biais : E(Tn ) = θ
                                4nan θ              5
                                       = θ =⇒ an =
                                  5                4n
   Risque quadratique :
   Puisque Tn est sans biais : R(Tn ) = Var(Tn )
   Par indépendance des Xi :
                                                   n
                               Var                         Var(Xi )
                                                   X
                                     (Tn ) = a2n
                                                     i=1
                                                        2θ2
                                            = a2n · n ·
                                                        75
                                               2
                                                  5           2θ2
                                            =            ·n·
                                                 4n            75
                                                              2
                                                25         2θ
                                            =       2
                                                      ·n·
                                              16n           75
                                              25 · 2θ2
                                            =
                                              16n · 75
                                               50θ2
                                            =
                                              1200n
                                               θ2
                                            =
                                              24n
                         θ2
   Réponse : R(Tn ) =
                      24n
   Remarque : Le risque tend vers 0 quand n → ∞, donc Tn est convergent en moyenne
quadratique.




                                                 5
~~~

## Page 6

~~~text
CY Tech - ING1-GM                                                        Statistiques Inférentielles

3    Exercice 3 - Densité triangulaire

Données                             (
                                        2
                                            1 − xθ       si x ∈ [0, θ]
                                                     
                                        θ
                          f (x) =
                                     0                   sinon

Question 1 : Calcul de E(X) et Var(X)
Espérance :
                                        Z θ
                                              2       x
                           E(X) =         x·      1−      dx
                                       0      θ        θ
                                      2 θ           x2
                                        Z             
                                    =         x−         dx
                                      θ 0            θ
                                                    θ
                                      2 x2 x3
                                        
                                    =        −
                                      θ 2        3θ 0
                                         2
                                                 θ3
                                                    
                                      2 θ
                                    =         −
                                      θ 2        3θ
                                         2
                                                 θ2
                                                    
                                      2 θ
                                    =         −
                                      θ 2         3
                                      2 3θ − 2θ2
                                            2
                                    = ·
                                      θ        6
                                      2 θ2
                                    = ·
                                      θ 6
                                      θ
                                    =
                                      3
    Calcul de E(X 2 ) :
                                        Z θ
                               2           2  2    x
                          E(X ) =     x ·       1−     dx
                                   0       θ        θ
                                  2 θ            x3
                                    Z              
                                            2
                                =         x −         dx
                                  θ 0             θ
                                                θ
                                  2 x3 x4
                                    
                                =        −
                                  θ 3        4θ 0
                                     3
                                             θ4
                                                 
                                  2 θ
                                =         −
                                  θ 3        4θ
                                     3
                                             θ3
                                                
                                  2 θ
                                =         −
                                  θ 3         4
                                  2 4θ − 3θ3
                                        3
                                = ·
                                  θ       12
                                  2θ3
                                =
                                  12θ
                                  θ2
                                =
                                  6

                                               6
~~~

## Page 7

~~~text
CY Tech - ING1-GM                                                   Statistiques Inférentielles

   Variance :
                                Var(X) = E(X 2 ) − [E(X)]2
                                                  2
                                           θ2       θ
                                         =     −
                                            6       3
                                             2     2
                                           θ     θ
                                         =     −
                                            6 9 
                                                3−2
                                         = θ2
                                                 18
                                             2
                                           θ
                                         =
                                           18

Question 2 : Étude de l'estimateur T = X̄               n      n

(a) Biais et correction
Calcul du biais :
                                                              θ       2θ
                     b(Tn ) = E(Tn ) − θ = E(X̄n ) − θ =        −θ =−
                                                              3       3
   L'estimateur est biaisé.
   Élimination du biais :
   On cherche Tn∗ tel que E(Tn∗ ) = θ.
   Posons Tn∗ = c · X̄n :
                                                             θ
                               E(Tn∗ ) = c · E(X̄n ) = c ·     =θ
                                                             3
   Donc c = 3, et l'estimateur sans biais est :

                                          Tn∗ = 3X̄n

(b) Convergence en probabilité
On applique la loi faible des grands nombres à Tn∗ :
   Puisque les Xi sont i.i.d. avec E(Xi ) = 3θ :

                                                P   θ
                                           X̄n →
                                               −
                                                    3
   Par continuité de la convergence en probabilité :
                                                        θ
                                   Tn∗ = 3X̄n →
                                                P
                                              − 3·        =θ
                                                        3
   Conclusion : Tn∗ converge en probabilité vers θ.

(c) Risque quadratique et convergence en moyenne quadratique
Puisque Tn∗ est sans biais :

                       R(Tn∗ ) = Var(Tn∗ ) = Var(3X̄n ) = 9 · Var(X̄n )


                                               7
~~~

## Page 8

~~~text
CY Tech - ING1-GM                                                          Statistiques Inférentielles

   Or :
                                              Var(X)        θ2 /18    θ2
                                Var(X̄n ) =             =          =
                                                n              n     18n
   Donc :
                                                         θ2   θ2
                                      R(Tn∗ ) = 9 ·         =
                                                        18n   2n
   Convergence en moyenne quadratique :
                                                            θ2
                                     lim R(Tn∗ ) = lim         =0
                                    n→∞                 n→∞ 2n

            L2
   Donc Tn∗ −→ θ : l'estimateur converge en moyenne quadratique.

(d) Loi asymptotique
On applique le théorème central limite :
                       √                                      θ2
                                                              
                                   θ L
                           n X̄n −     → N (0, Var(X)) = N 0,
                                       −
                                   3                          18
   Pour Tn∗ = 3X̄n :
                       √                  √              √
                                                                   
                                                                  θ
                           n(Tn∗ − θ) =
                                                     
                                           n 3X̄n − θ = 3 n X̄n −
                                                                  3

   Donc :
                           √                            θ2          θ2
                                                                    
                                          L
                               n(Tn∗ − θ) −
                                          →N     0, 9 ·      = N 0,
                                                        18          2
   Conclusion : Asymptotiquement :

                                                        θ2
                                                          
                                          Tn∗ ∼ N    θ,
                                                        2n




                                                    8
~~~

## Page 9

~~~text
CY Tech - ING1-GM                                                             Statistiques Inférentielles

4       Exercice 4 - Proportion de malades

Données
       Médecin 1 : n1 = 40 personnes, proportion X1

       Médecin 2 : n2 = 60 personnes, proportion X2

       Échantillons indépendants

Question 1 : X et X sont-ils sans biais et indépendants ?
                        1       2

Modélisation :
  Si Yi est le nombre de personnes atteintes dans l'échantillon i :

                                               Yi ∼ B(ni , p)

      La proportion est : Xi = nYii
      Espérance :                                  
                                               Yi           1           ni p
                            E(Xi ) = E                  =      E(Yi ) =      =p
                                               ni           ni          ni
    Conclusion 1 : X1 et X2 sont sans biais.
    Indépendance :
    Les échantillons sont prélevés de manière indépendante, donc Y1 et Y2 sont indépendantes,
et par conséquent X1 et X2 le sont aussi.
    Conclusion 2 : X1 et X2 sont indépendantes.

Question 2 : Biais des estimateurs T et T                      3       4

(a)   T3 = X1 +X
              2
                2
                    :
                                             1
                                      E(T3 ) = [E(X1 ) + E(X2 )]
                                             2
                                             1
                                            = (p + p)
                                             2
                                            =p

      Conclusion : T3 est sans biais.
      (b) T4 = 2X1 +3X
                   5
                      2
                        :
                                            1
                                    E(T4 ) =  [2E(X1 ) + 3E(X2 )]
                                            5
                                            1
                                           = (2p + 3p)
                                            5
                                           =p

      Conclusion : T4 est sans biais.




                                                        9
~~~

## Page 10

~~~text
CY Tech - ING1-GM                                                    Statistiques Inférentielles

Question 3 : Comparaison des risques quadratiques
Pour un estimateur sans biais : R(T ) = Var(T )
   Calcul des variances :
   Pour Xi = nYii avec Yi ∼ B(ni , p) :

                                   Var(Yi )       ni p(1 − p)   p(1 − p)
                      Var(Xi ) =              =               =
                                       n2i              2
                                                       ni          ni

   Donc :
                                               p(1 − p)
                                    Var(X1 ) =
                                                  40
                                               p(1 − p)
                                    Var(X2 ) =
                                                  60
   (a) T1 = X1 :
                                                        p(1 − p)
                             R(T1 ) = Var(X1 ) =
                                                           40
   (b) T2 = X2 :
                                                        p(1 − p)
                             R(T2 ) = Var(X2 ) =
                                                           60
   (c) T3 = X1 +X
               2
                 2
                   :
   Par indépendance :
                                                           
                                                 X1 + X 2
                           R(T3 ) = Var
                                                    2
                                     1
                                   =   [Var(X1 ) + Var(X2 )]
                                     4                      
                                     1 p(1 − p) p(1 − p)
                                   =              +
                                     4     40          60
                                                    
                                     p(1 − p) 3 + 2
                                   =
                                         4       120
                                     p(1 − p) 5
                                   =          ·
                                         4      120
                                     p(1 − p)
                                   =
                                        96




                                                 10
~~~

## Page 11

~~~text
CY Tech - ING1-GM                                                  Statistiques Inférentielles

  (d) T4 = 2X1 +3X
               5
                  2
                    :
                                                        
                                             2X1 + 3X2
                          R(T4 ) = Var
                                                 5
                                   1
                                 =     [4Var(X1 ) + 9Var(X2 )]
                                   25                         
                                   1 4p(1 − p) 9p(1 − p)
                                 =                 +
                                   25       40           60
                                                      
                                   p(1 − p) 1        3
                                 =                +
                                      25       10 20
                                   p(1 − p) 2 + 3
                                 =           ·
                                      25        20
                                   p(1 − p) 5
                                 =           ·
                                      25       20
                                   p(1 − p)
                                 =
                                      100
  Comparaison :
                                    p(1 − p)
                           R(T1 ) =          ≈ 0.025 p(1 − p)
                                       40
                                    p(1 − p)
                           R(T2 ) =          ≈ 0.0167 p(1 − p)
                                       60
                                    p(1 − p)
                           R(T3 ) =          ≈ 0.0104 p(1 − p)
                                       96
                                    p(1 − p)
                           R(T4 ) =          = 0.01 p(1 − p)
                                      100
   Conclusion : L'estimateur T4 a le plus faible risque quadratique.
   Remarque importante : T4 correspond à l'estimateur optimal qui pondère les
proportions par les tailles d'échantillons :
                         n1 X1 + n2 X2   40X1 + 60X2   2X1 + 3X2
                 T4 =                  =             =
                            n1 + n2          100           5

Question 4 : Meilleure estimation
Données observées :
   Médecin 1 : 25 personnes atteintes sur 40 ⇒ x1 = 25
                                                     40
                                                        = 0.625

   Médecin 2 : 38 personnes atteintes sur 60 ⇒ x2 = 60
                                                     38
                                                        ≈ 0.633

  Avec l'estimateur optimal T4 :
                        2 · 0.625 + 3 · 0.633   1.25 + 1.9   3.15
                t4 =                          =            =      = 0.63
                                  5                  5         5
  Ou directement :
                                      25 + 38    63
                               t4 =           =     = 0.63
                                      40 + 60   100
  Réponse : La meilleure estimation de la proportion est 63%.

                                               11
~~~

## Page 12

~~~text
CY Tech - ING1-GM                                                 Statistiques Inférentielles

5     Exercice 5 - Loi normale avec variance particulière

Données
                              Xi ∼ N (θ, θ(1 − θ)),   θ ∈]0, 1[
    Estimateurs :
                                             n
                                         1X
                                    T1 =       Xi = X̄n
                                         n i=1
                                             n
                                         1X 2
                                    T2 =      X
                                         n i=1 i

Question 1 : Biais des estimateurs
Étude de T1 :
                                E(T1 ) = E(X̄n ) = E(X) = θ
    Conclusion : T1 est sans biais pour θ.
    Étude de T2 :
    On sait que pour une variable aléatoire X : E(X 2 ) = Var(X) + [E(X)]2
    Donc :
                         E(Xi2 ) = θ(1 − θ) + θ2 = θ − θ2 + θ2 = θ
    Par conséquent :
                                              n
                                          1X
                                 E(T2 ) =       E(Xi2 ) = θ
                                          n i=1
    Conclusion : T2 est aussi sans biais pour θ.
    Remarque : C'est une situation particulière où la variance dépend de la moyenne de
façon spécique.

Question 2 : Convergence des estimateurs
Pour T1 :
  Par la loi faible des grands nombres :
                                             P
                                   T1 = X̄n →
                                            − E(X) = θ

    Conclusion : T1 est convergent.
    Pour T2 :
    Les Xi2 sont i.i.d. avec E(Xi2 ) = θ. Par la loi faible des grands nombres :
                                        n
                                      1X 2 P
                               T2 =        X →− E(X 2 ) = θ
                                      n i=1 i

    Conclusion : T2 est convergent.




                                             12
~~~

## Page 13

~~~text
CY Tech - ING1-GM                                                      Statistiques Inférentielles

Question 3 : Comparaison des estimateurs
On compare les risques quadratiques. Puisque les deux estimateurs sont sans biais :

                                       R(Ti ) = Var(Ti )

   Variance de T1 :
                                                    Var(X)       θ(1 − θ)
                        Var(T1 ) = Var(X̄n ) =               =
                                                      n             n
   Variance de T2 :
   On utilise la formule donnée : Var(Xi2 ) = 2θ2 (1 − θ2 )
                                   n
                                          !           n
                               1X 2             1 X              2θ2 (1 − θ2 )
              Var(T2 ) = Var        X         = 2    Var(Xi2 ) =
                               n i=1 i         n i=1                   n
   Comparaison :
   On doit comparer θ(1 − θ) et 2θ2 (1 − θ2 ).
                 Var(T2 ) = 2θ2 (1−θ2 )
   Posons h(θ) = Var (T1 )   θ(1−θ)
   Simplions :
                                         2θ2 (1 − θ)(1 + θ)
                                 h(θ) =
                                              θ(1 − θ)
                                       = 2θ(1 + θ)
                                       = 2θ + 2θ2

   Pour θ ∈]0, 1[ :
    Si θ = 0.5 : h(0.5) = 1 + 0.5 = 1.5 > 1

    En général : h(θ) = 2θ(1 + θ) > 2θ > 0

   Étudions quand h(θ) > 1 :

                           2θ + 2θ2 > 1 ⇐⇒ 2θ2 + 2θ − 1 > 0

   Le discriminant : √
                     ∆=4+8√      = 12    √
   Racines : θ = 4 = 4 √ = −1±2 3
                 −2± 12     −2±2 3

   La racine positive : θ0 = −1+2 3 ≈ −1+1.732
                                         2
                                               ≈ 0.366
   Conclusion :
    Si θ < 0.366 : Var(T2 ) < Var(T1 ) donc T2 est meilleur

    Si θ > 0.366 : Var(T1 ) < Var(T2 ) donc T1 est meilleur

   En pratique, pour la plupart des valeurs de θ dans ]0, 1[, T1 = X̄n est le meilleur
estimateur car plus simple et souvent plus ecace.




                                               13
~~~

## Page 14

~~~text
CY Tech - ING1-GM                                                                  Statistiques Inférentielles

6     Exercice 6 - EMV d'une proportion

Contexte
On observe n épreuves de Bernoulli indépendantes : X1 , . . . , Xn ∼ B(p)

Fonction de vraisemblance
La loi de probabilité de Xi est :
                              P(Xi = k) = pk (1 − p)1−k ,          k ∈ {0, 1}

    La vraisemblance pour l'échantillon (x1 , . . . , xn ) :
                                  n
                                  Y                           P                    P
                        L(p) =          pxi (1 − p)1−xi = p       xi
                                                                       (1 − p)n−       xi

                                  i=1

    Posons s =               (nombre de succès) :
                 Pn
                    i=1 xi

                                         L(p) = ps (1 − p)n−s

Log-vraisemblance
                                ln L(p) = s ln p + (n − s) ln(1 − p)

Maximisation
Dérivée par rapport à p :
                                          d ln L  s n−s
                                                 = −
                                            dp    p 1−p
    Condition du premier ordre :
                                               s n−s
                                                −    =0
                                               p 1−p
                                        s(1 − p) − (n − s)p
                                                            =0
                                             p(1 − p)

                                         s − sp − np + sp = 0

                                                  s = np
    Donc :
                                                      n
                                               s   1X
                                        p̂ =     =       xi = x̄n
                                               n   n i=1

    Vérication de la condition du second ordre :
                                   d2 ln L    s    n−s
                                        2
                                           =− 2 −          <0
                                    dp       p    (1 − p)2
    C'est bien un maximum.
    Conclusion : La fréquence empirique X̄n est l'EMV de p.

                                                    14
~~~

## Page 15

~~~text
CY Tech - ING1-GM                                                      Statistiques Inférentielles

Ecacité
Rappel : Un estimateur est ecace s'il atteint la borne de Cramér-Rao :
                                                      1
                                        Var(θ̂) ≥
                                                    nI(θ)

   où I(θ) est l'information de Fisher.
   Information de Fisher pour la loi de Bernoulli :
                                            2            
                                            d ln f (X; p)
                                 I(p) = −E
                                                dp2

   Pour une observation :

                            ln f (x; p) = x ln p + (1 − x) ln(1 − p)

                                       d ln f  x 1−x
                                              = −
                                         dp    p 1−p
                              d2 ln f      x       1−x
                                   2
                                      =− 2 −
                               dp          p      (1 − p)2
                                               
                               X       1−X           E(X) 1 − E(X)
                   I(p) = −E − 2 −            2
                                                  =        +
                               p      (1 − p)         p2     (1 − p)2
   Avec E(X) = p :
                        p      1−p      1  1    1−p+p          1
               I(p) =     2
                            +        2
                                       = +    =          =
                        p     (1 − p)   p 1−p   p(1 − p)   p(1 − p)

   Borne de Cramér-Rao pour n observations :
                                               1     p(1 − p)
                                 Var(p̂) ≥         =
                                             nI(p)      n

   Variance de p̂ = X̄n :
                                                 Var(X)         p(1 − p)
                         Var(p̂) = Var(X̄n ) =              =
                                                     n             n
  Conclusion : L'estimateur p̂ atteint exactement la borne de Cramér-Rao, donc il est
ecace.
  Résumé :
    La fréquence est l'EMV de la proportion

    Elle est sans biais : E(p̂) = p

    Elle est ecace : elle atteint la borne de Cramér-Rao

    Elle est convergente : p̂ →
                                P
                               − p



                                               15
~~~

## Page 16

~~~text
CY Tech - ING1-GM                                                                    Statistiques Inférentielles

7     Exercice 7 - EMV pour un échantillon gaussien

Contexte
Échantillon (X1 , . . . , Xn ) avec Xi ∼ N (µ, σ 2 ) i.i.d.
   Paramètres à estimer : θ = (µ, σ 2 )

Fonction de vraisemblance
Densité d'une observation :
                                                          (x − µ)2
                                                                                    
                                        2           1
                             f (x; µ, σ ) = √       exp −
                                              2πσ 2         2σ 2

    Vraisemblance :                         n
                                                        (xi − µ)2
                                                                 
                                   2
                                            Y          1
                            L(µ, σ ) =     √      exp −
                                       i=1  2πσ 2          2σ 2
                                                                            n
                                                                                         !
                                         1              1 X
                        L(µ, σ 2 ) =             exp −          (xi − µ)2
                                     (2πσ 2 )n/2       2σ 2 i=1

Log-vraisemblance
                                                                                 n
                                     n        n           1 X
                    ln L(µ, σ 2 ) = − ln(2π) − ln(σ 2 ) − 2     (xi − µ)2
                                     2        2          2σ i=1

Maximisation par rapport à µ
                                     n                   n
                     ∂ ln L    1    X                  1 X
                            =− 2 ·2     (xi − µ)(−1) = 2    (xi − µ)
                      ∂µ      2σ    i=1
                                                      σ i=1
    Condition du premier ordre :
                                n
                                X                                  n
                                                                   X
                                      (xi − µ) = 0 =⇒                      xi = nµ
                                i=1                                i=1

    Donc :
                                                           n
                                                   1X
                                            µ̂ =         xi = x̄n
                                                   n i=1


Maximisation par rapport à σ                       2

                                                                       n
                              ∂ ln L      n     1 X
                                     = −     +             (xi − µ)2
                               ∂σ 2      2σ 2 2(σ 2 )2 i=1
    Condition du premier ordre (en remplaçant µ par µ̂) :
                                                               n
                                  n    1 X
                                − 2+              (xi − x̄n )2 = 0
                                 2σ  2(σ 2 )2 i=1


                                                           16
~~~

## Page 17

~~~text
CY Tech - ING1-GM                                                         Statistiques Inférentielles


                                          n
                                   1 X                     2   n
                                             (x i − x̄ n )   =
                                 (σ 2 )2 i=1                   σ2
                                      n
                                      X
                                        (xi − x̄n )2 = nσ 2
                                      i=1

   Donc :
                                             n
                                  2   1X
                                 σ̂ =       (xi − x̄n )2 = s2n
                                      n i=1

  Remarque importante : On utilise le diviseur n et non n − 1 pour l'EMV (variance
empirique biaisée).

Propriétés des EMV
1. Pour µ̂ = X̄n :
   Biais :
                                       E(µ̂) = E(X̄n ) = µ
   µ̂ est sans biais.
   Variance :
                                                                σ2
                                  Var(µ̂) = Var(X̄n ) =
                                                                n
   Information de Fisher :
   Pour la moyenne d'une loi normale avec variance connue :
                                                       n
                                            I(µ) =
                                                       σ2
   Borne de Cramér-Rao :
                                                   1     σ2
                                      Var(µ̂) ≥        =
                                                  I(µ)   n

   L'égalité est atteinte : µ̂ est ecace.
   2. Pour σ̂ 2 = Sn2 :
   Biais :
   On sait que :                 "                     #
                                 n
                                 X
                                                   2
                             E         (Xi − X̄n )         = (n − 1)σ 2
                                 i=1

   Donc :                            " n              #
                                  1   X                  n−1 2
                        E(σ̂ 2 ) = E      (Xi − X̄n )2 =    σ
                                  n   i=1
                                                          n
   Le biais est :
                                            n−1 2         σ2
                              b(σ̂ 2 ) =       σ − σ2 = −
                                             n            n
   σ̂ 2 est biaisé mais asymptotiquement sans biais (biais → 0 quand n → ∞).



                                                 17
~~~

## Page 18

~~~text
CY Tech - ING1-GM                                                     Statistiques Inférentielles

  Version sans biais :
                                         n
                                    1 X                     n
                         σ̃ 2 =             (Xi − X̄n )2 =     σ̂ 2
                                  n − 1 i=1                n−1

  est sans biais mais n'est pas l'EMV.
  Ecacité :
  L'information de Fisher pour σ 2 dans une loi normale est :
                                                        n
                                         I(σ 2 ) =
                                                       2σ 4
  Borne de Cramér-Rao :
                                                     1       2σ 4
                                   Var(σ̂ 2 ) ≥            =
                                                   I(σ 2 )    n

  On peut montrer que :
                                                   2(n − 1)σ 4
                                    Var(σ̂ 2 ) =
                                                       n2
  Pour n grand :
                                                        2σ 4
                                        Var(σ̂ 2 ) ≈
                                                         n
  L'estimateur est asymptotiquement ecace.

Résumé
    Paramètre                EMV                                    Propriétés
        µ                   µ̂ =PX̄n                      Sans biais, ecace, convergent
        σ2                     1
                   σ̂ = Sn = n (Xi − X̄n )2
                     2   2
                                                        Biaisé, asympt. ecace, convergent




                                                  18
~~~

## Page 19

~~~text
CY Tech - ING1-GM                                                                  Statistiques Inférentielles


8    Exercice 8 - Nombre de bactéries (Loi de Poisson)

Contexte
On prélève n tubes de 1 ml d'eau, observant x1 , . . . , xn bactéries par tube.
   Le nombre de bactéries par tube suit une loi de Poisson : Xi ∼ P(θ)

Question 1 : EMV de θ
Fonction de vraisemblance :
  Pour la loi de Poisson :
                                                 θk e−θ
                                      P(X = k) =
                                                   k!
    La vraisemblance :                  n                         P
                                        Y θxi e−θ               θ xi e−nθ
                               L(θ) =                         = Qn
                                        i=1
                                                  xi !            i=1 xi !

    Log-vraisemblance :
                                      n
                                                 !                    n
                                      X                               X
                         ln L(θ) =          xi       ln θ − nθ −             ln(xi !)
                                      i=1                              i=1

    Maximisation :                                 Pn
                                     d ln L              i=1 xi
                                            =                     −n
                                       dθ                 θ
    Condition du premier ordre :
                                        Pn
                                            i=1 xi
                                                         −n=0
                                            θ
                                            n
                                            X
                                                  xi = nθ
                                            i=1

    Donc :
                                                     n
                                           1X
                                      θ̂ =       xi = x̄n
                                           n i=1

    Vérication de la condition du second ordre :
                                                         Pn
                                   d2 ln L                i=1 xi
                                           =−                    <0
                                    dθ2                    θ2
    C'est bien un maximum.
    Conclusion : L'EMV du nombre moyen de bactéries est la moyenne empirique
θ̂ = X̄n .




                                                     19
~~~

## Page 20

~~~text
CY Tech - ING1-GM                                                     Statistiques Inférentielles

Question 2 : Propriétés de l'EMV
1. Biais :
   Pour la loi de Poisson : E(Xi ) = θ
   Donc :                                           n
                                              1X
                            E(θ̂) = E(X̄n ) =       E(Xi ) = θ
                                              n i=1

   θ̂ est sans biais.
   2. Variance :
   Pour la loi de Poisson : Var(Xi ) = θ
                                                    Var(X)        θ
                            Var(θ̂) = Var(X̄n ) =            =
                                                        n         n
   3. Convergence :
   Par la loi faible des grands nombres :
                                            P
                                   θ̂ = X̄n →
                                            − E(X) = θ

   θ̂ est convergent.
   4. Ecacité :
   Information de Fisher pour la loi de Poisson :

                              ln f (x; θ) = x ln θ − θ − ln(x!)

                                      d ln f  x
                                             = −1
                                        dθ    θ
                                     d2 ln f     x
                                          2
                                              =− 2
                                      dθ         θ
                                           
                                        X      E(X)   θ   1
                           I(θ) = −E − 2 =        2
                                                    = 2 =
                                        θ       θ    θ    θ
   Pour n observations :                            n
                                         In (θ) =
                                                    θ
   Borne de Cramér-Rao :
                                                  1      θ
                                   Var(θ̂) ≥           =
                                                In (θ)   n

   On a exactement : Var(θ̂) = nθ
   θ̂ atteint la borne de Cramér-Rao, donc il est ecace.
   5. Loi asymptotique :
   Par le théorème central limite :
                                  √          L
                                   n(θ̂ − θ) −
                                             → N (0, θ)

   Asymptotiquement :                            
                                                θ
                                      θ̂ ∼ N θ,
                                                n

                                             20
~~~

## Page 21

~~~text
CY Tech - ING1-GM                                              Statistiques Inférentielles

Résumé des propriétés
L'estimateur θ̂ = X̄n pour la loi de Poisson est :
    Sans biais : E(θ̂) = θ

    Convergent : θ̂ →
                        P
                     − θ

    Ecace : atteint la borne de Cramér-Rao

    Asymptotiquement normal : θ̂ ∼ N (θ, nθ ) pour n grand

    EMV : c'est l'estimateur du maximum de vraisemblance

   C'est l'estimateur optimal pour θ dans le modèle de Poisson.




                             Fin de la correction du TD1
            Pour toute question ou précision complémentaire, n'hésitez pas !




                                            21
~~~
