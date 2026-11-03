# 2-Slides.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1BDyjHFenOICjogeZCvRD0PZ__g8RfNbQ) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
   Motivations               SVD            Pseudo-inverse         Méthode des moindres carrés   Fin




                      ING1 MI/MF Semestre 2
                 ANALYSE NUMÉRIQUE EN PYTHON
                          * Chapitre 2 *

                                           Nelly BARRAU
                                         ( nelly.barrau@cyu.fr )




1/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 2

~~~text
   Motivations               SVD                Pseudo-inverse      Méthode des moindres carrés   Fin




  Planning


                    Semaine du Contenu                                         CM        TD
                         19/01           Détermination des valeurs propres     1.5h      3h
                         26/01           SVD et Moindres Carrés                1.5h
                         02/02                                                           3h
                         09/02           Interpolation                         1.5h
                         16/02           Vacances Hiver
                         23/02                                                           3h
                         02/03           Calcul Intégrale                      1.5h
                         09/03           Campagne BDE
                         16/03                                                           3h
                         23/03           Résolution numérique EDO              1.5h
                         30/03                                                           3h
                         06/04           Préparation TP/Révisions              1.5h       -
                         13/04           Vacances Avril
                         20/04           TP Noté en python                               3h
                         27/04
                         04/05           Examen                                          2h
                          ···
2/23
                         15/06
  Nelly BARRAU ( nelly.barrau@cyu.fr )   Rattrapage                                      2h
~~~

## Page 3

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin




  Décomposition en valeurs singulières et Moindres Carrés


         CM [1.5h] et TD [3h]
         1 Motivations

         2       SVD
                  Rappels
                  Forme générale et décomposition
         3   Pseudo-inverse
               Dénitions et propriétés
               SVD
         4   Méthode des moindres carrés
              Cas systèmes surdéterminés
              Cas systèmes sous-déterminés
         5   Fin

3/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 4

~~~text
   Motivations               SVD               Pseudo-inverse     Méthode des moindres carrés   Fin




         But de ce chapitre
             Résoudre des systèmes linéaires dont la matrice n'est pas
             nécessairement carrée (donc pas SL de Cramer)
             Généraliser la notion d'inverse à l'ensemble des matrices carrées (ou
             non), inversibles (ou non) : on parle de pseudo-inverse
         Soit m, n ∈ N∗ ; A ∈ Mm,n (K) et b ∈ Km : Ax = b sera de la forme
                                                        
                                      a1,1   ... a1,n    x1         b1
                                      ...        ...   ...  =  ... 
                                      am,1   ... am,n    xn        bm

         Ici, on s'intéressera aux cas où m < n (avec rg (A) = m) et m > n (avec
         rg (A) = n) et m = n (avec A non inversible), pour lesquels les systèmes
         admettent une innité de solutions.


4/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 5

~~~text
   Motivations               SVD               Pseudo-inverse        Méthode des moindres carrés   Fin

  Rappels



         Norme spectrale
         La norme spectrale de A est dénie par
                                             ∥Ax∥2  p                                   T
                         ∥|A|∥2 = sup              = ρ(A∗ A)         avec A∗ = A
                                         x̸=0 ∥x∥2


         Valeurs singulières
         Les valeurs singulières de A sont les racines carrées des valeurs propres
         non nulles de A∗ A
                                               p
                                    σi (A) =       λi     avec λi ∈ Sp(A∗ A)

         Remarque.
            Les valeurs de A∗ A et AA∗ sont toujours positives ou nulles
            Les valeurs propres non nulles de A∗ A et AA∗ sont identiques

5/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 6

~~~text
   Motivations               SVD              Pseudo-inverse         Méthode des moindres carrés      Fin

  Rappels


  Exemple 1 - Cas matrice carrée




                                                    3 0
                                                                          
         Déterminons les valeurs singulières de A =
                                                    0 −2
         On note que
                 A ∈ M2 (R) est réelle donc A = A
                 A est symétrique donc A = AT
                             T
         Ainsi A∗ = A = A = A. Il vient alors
                                                                   9 0
                                                                      
                                         A∗ A = A2 = AA∗ =
                                                                   0 4
                                                                                            √
         Donc
           √ Sp(A A) = {9; 4}. Ainsi, les valeurs singulières de A sont
                  ∗
                                                                                                9=3
         et 4 = 2

6/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 7

~~~text
   Motivations               SVD         Pseudo-inverse               Méthode des moindres carrés       Fin

  Rappels


  Exemple 2 - Cas matrice non carrée


                                                                      √
                                                              1          2 √0
                                                                                  
         Déterminons les valeurs singulières de A =
                                                              1         0    2
                                                                  1                     √1
                                                                                                   
                                                                  T
         A ∈ M2,3 (R) est réelle donc A = A et A∗ = A = AT =  2 √0 
                                                               0   2
         Alors                      √    √
                                2     2    2
                                           
                               √                          3 1
                                                             
                    A A = √2 2
                     ∗
                                          0           ∗
                                                et AA =
                                                          1 3
                                           
                                 2 0      2

                 AA∗ a pour valeurs propres 4 et 2
              A∗ A a pour valeurs propres : 4 ; 2 et 0
                                                       √
         Les valeurs singulières de A sont donc 2 et 2
7/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 8

~~~text
   Motivations               SVD               Pseudo-inverse        Méthode des moindres carrés   Fin

  Forme générale et décomposition



         Décomposition en valeurs singulières (SVD)
         Soit A ∈ Mm,n (K) de rang r . Alors ∃U ∈ Mm (K) ; ∃V ∈ Mn (K) et
         ∃B ∈ Mm,n (K) de rang r telles que
                                                                           T
                                         A = UBV ∗          avec V ∗ = V

         et B est diagonale (correspondant aux valeurs singulières de A).

         SVD de A (exemple de cours)
                                                1 1
                                                           
                                             A=     = UBV ∗
                                                2 2
         avec
                               10 0                1 1 −2                      1 1 −1
                          √                                                              
                  B=                         U=√                     V =√
                               0  0                 5 2 1                       2 1 1

8/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 9

~~~text
   Motivations               SVD           Pseudo-inverse      Méthode des moindres carrés   Fin

  Forme générale et décomposition




         Remarques pratiques.

                 Le calcul des valeurs singulières se ramène à un calcul de valeurs
                 propres
                 Les valeurs singulières de A étant les racines carrées des valeurs
                 propres non nulles de AA∗ ou A∗ A : il vaut donc mieux les
                 déterminer sur la matrice de plus petite taille (entre AA∗ ou A∗ A)
                 Si A est réelle, alors
                                    T
                       A∗ = A = AT
                       U et V sont orthogonales (ie U −1 = U T et V −1 = V T )
                 Les colonnes {u1 ; ...; um } de U sont "des" vecteurs propres unitaires
                 de AA∗
                 Les colonnes {v1 ; ...; vn } de V (donc les lignes de V T ) sont "des"
                 vecteurs propres unitaires de A∗ A



9/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 10

~~~text
   Motivations               SVD         Pseudo-inverse    Méthode des moindres carrés   Fin

  Forme générale et décomposition


  Méthodologie pratique

         Pour obtenir "la" décomposition en valeurs singulières (SVD) d'une
         matrice A ∈ Mm,n (K), il faut :
           1 Calculer AA∗ ∈ Mm (K) et A∗ A ∈ Mn (K) (ces matrices sont

             toujours symétriques)
           2 Calculer les valeurs propres (non nulles) de C , la matrice de plus

             petite taille entre AA∗ et A∗ A : {λ1 ; ...; λr }
           3 Calculer les vecteurs propres de cette matrice C et les normaliser :

             on obtient {u1 ; ...; ur } sont alors des vecteurs propres normalisés de
             C associés aux valeurs propres (non nulles) {λ1 ; ...; λr }
           4 On déduit {v1 ; ...; vr } des vecteurs propres normalisés de C ∗

             (matrice de plus grande taille entre AA∗ et A∗ A), associés aux
             mêmes valeurs propres (non nulles) {λ1 ; ...; λr }.
             On calcule également les vecteurs propres associés (normalisés) aux
             valeurs propres nulles
           5 Conclusion
10/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 11

~~~text
   Motivations               SVD                   Pseudo-inverse       Méthode des moindres carrés   Fin

  Forme générale et décomposition


  Application



         Déterminer la SVD de
                                                     √
                                            1           2 √0
                                                                   
                                         A=                   ∈ M2,3 (R)
                                            1          0    2
                                   1          √1
                                                          

         On a alors A∗ = AT =  2 √0  ∈ M3,2 (R)
                                0   2




11/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 12

~~~text
   Motivations               SVD                   Pseudo-inverse       Méthode des moindres carrés   Fin

  Forme générale et décomposition


  Application



         Déterminer la SVD de
                                                     √
                                            1           2 √0
                                                                   
                                         A=                   ∈ M2,3 (R)
                                            1          0    2
                                     1        √1
                                                          

         On a alors A∗ = AT =  2 √0  ∈ M3,2 (R)
                                0     2
           1 Calculons AA∗ ∈ M2 (K) et A∗ A ∈ M3 (K)




11/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 13

~~~text
   Motivations               SVD                       Pseudo-inverse         Méthode des moindres carrés   Fin

  Forme générale et décomposition


  Application



         Déterminer la SVD de
                                                         √
                                            1               2 √0
                                                                       
                                         A=                       ∈ M2,3 (R)
                                            1              0    2
                                     1            √1
                                                              

         On a alors A∗ = AT =  2 √0  ∈ M3,2 (R)
                                0     2
           1 Calculons AA∗ ∈ M2 (K) et A∗ A ∈ M3 (K)
                                                                                        √       √ 
                                                                                √2        2       2
                                                                               
                                             3 1
                                                 
                           AA∗ =                             et         A∗ A = √2       2       0
                                             1 3
                                                                                   2     0       2

                 Pour la suite, on travaillera avec C = AA∗

11/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 14

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C




12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 15

~~~text
   Motivations               SVD             Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C
                                            3−λ      1
                      det(C − λI2 )      =                = (3 − λ)2 − 12
                                              1    3−λ
                                         = (3 − λ − 1)(3 − λ + 1) = (2 − λ)(4 − λ)
                 Valeurs propres de AA∗ :




12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 16

~~~text
   Motivations               SVD             Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C
                                            3−λ      1
                      det(C − λI2 )      =                = (3 − λ)2 − 12
                                              1    3−λ
                                         = (3 − λ − 1)(3 − λ + 1) = (2 − λ)(4 − λ)
                 Valeurs propres de AA∗ : λ1 = 4 et λ2 = 2
                 Valeurs propres de A∗ A :




12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 17

~~~text
   Motivations               SVD             Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C
                                            3−λ      1
                      det(C − λI2 )      =                = (3 − λ)2 − 12
                                              1    3−λ
                                         = (3 − λ − 1)(3 − λ + 1) = (2 − λ)(4 − λ)
                 Valeurs propres de AA∗ : λ1 = 4 et λ2 = 2
                 Valeurs propres de A∗ A : λ1 = 4 ; λ2 = 2 et λ3 = 0
                 Valeurs singulières de A :




12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 18

~~~text
   Motivations               SVD             Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C
                                            3−λ      1
                      det(C − λI2 )      =                = (3 − λ)2 − 12
                                              1    3−λ
                                         = (3 − λ − 1)(3 − λ + 1) = (2 − λ)(4 − λ)
              Valeurs propres de AA∗ : λ1 = 4 et λ2 = 2
              Valeurs propres de A∗ A : λ1 = 4√; λ2 = 2 et λ3 =√0
              Valeurs singulières de A : σ1 = 4 = 2 et σ2 = 2
            3 Calculons les vecteurs propres associés (normalisés) de AA∗ (lien
              avec U ) :




12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 19

~~~text
   Motivations               SVD             Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C
                                            3−λ      1
                      det(C − λI2 )      =                = (3 − λ)2 − 12
                                              1    3−λ
                                         = (3 − λ − 1)(3 − λ + 1) = (2 − λ)(4 − λ)
              Valeurs propres de AA∗ : λ1 = 4 et λ2 = 2
              Valeurs propres de A∗ A : λ1 = 4√; λ2 = 2 et λ3 = √0
              Valeurs singulières de A : σ1 = 4 = 2 et σ2 = 2
            3 Calculons les vecteurs propres associés (normalisés) de AA∗ (lien
              avec U ) :
                                                       1
                                                       
                   E4 = Ker (AA∗ − 4I2 ) = Vect{u1′ =    } : en eet
                                                       1
                                               −1         1       0               1
                                                                          
                                                          x1           x1
                       (AA −4I2 )X = 02 ⇔
                             ∗
                                                               =    ⇔     ∈ Vect{   }
                                               1         −1
                                                          x2      0    x2         1
                                                             1
                                                           
                       E2 = Ker (AA∗ − 2I2 ) = Vect{u2′ =       }
                                                           −1



12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 20

~~~text
   Motivations               SVD             Pseudo-inverse     Méthode des moindres carrés   Fin

  Forme générale et décomposition

            2 Calculons les valeurs propres de C
                                            3−λ      1
                      det(C − λI2 )      =                = (3 − λ)2 − 12
                                              1    3−λ
                                         = (3 − λ − 1)(3 − λ + 1) = (2 − λ)(4 − λ)
              Valeurs propres de AA∗ : λ1 = 4 et λ2 = 2
              Valeurs propres de A∗ A : λ1 = 4√; λ2 = 2 et λ3 = √0
              Valeurs singulières de A : σ1 = 4 = 2 et σ2 = 2
            3 Calculons les vecteurs propres associés (normalisés) de AA∗ (lien
              avec U ) :
                                                       1
                                                       
                   E4 = Ker (AA∗ − 4I2 ) = Vect{u1′ =    } : en eet
                                                       1
                                                   −1     1       0               1
                                                                          
                                                          x1           x1
                       (AA −4I2 )X = 02 ⇔
                             ∗
                                                               =    ⇔     ∈ Vect{   }
                                               1         −1
                                                          x2      0    x2         1
                                                             1
                                                           
                       E2 = Ker (AA∗ − 2I2 ) = Vect{u2′ =       }
                                                           −1
                                              ′                       ′
                 Normalisation : u1 = ∥uu1′ ∥ = √12 u1′ et u2 = ∥uu2′ ∥ = √12 u2′
                                             1                        2
12/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 21

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition




13/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 22

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition



            4 Déduisons les vecteurs propres (normalisés) de C ∗ = A∗ A (lien avec
              V ), associés aux valeurs propres {λ1 ; λ2 ; λ3 }




13/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 23

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition



            4 Déduisons les vecteurs propres (normalisés) de C ∗ = A∗ A (lien avec
              V ), associés aux valeurs propres {λ1 ; λ2 ; λ3 }
                   v1 est associé à λ1 : A∗ Av1 = λ1 v1
                                                                              √ 
                                                                              1/ 2
                                                              1 ∗
                   Or on sait que AA u1 = λ1 u1 donc v1 = σ1 A u1 ie v1 =  1/2 
                                      ∗

                                                                               1/2
                   v2 est associé à λ2 : A Av2 = λ1 v2
                                          ∗

                                                                                0√
                                                                                  

                   Or on sait que AA∗ u2 = λ1 u2 donc v2 = σ12 A∗ u2 ie v2 = 1/√2
                                                                              1/ 2




13/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 24

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition



            4 Déduisons les vecteurs propres (normalisés) de C ∗ = A∗ A (lien avec
              V ), associés aux valeurs propres {λ1 ; λ2 ; λ3 }
                   v1 est associé à λ1 : A∗ Av1 = λ1 v1
                                                                              √ 
                                                                              1/ 2
                                                              1 ∗
                   Or on sait que AA u1 = λ1 u1 donc v1 = σ1 A u1 ie v1 =  1/2 
                                      ∗

                                                                               1/2
                   v2 est associé à λ2 : A Av2 = λ1 v2
                                          ∗

                                                                                0√
                                                                                  

                   Or on sait que AA∗ u2 = λ1 u2 donc v2 = σ12 A∗ u2 ie v2 = 1/√2
                                                                              1/ 2
                                                                           √ 
                                                                            1/ 2
                   v3 est associé à λ3 = 0 : E0 = Ker (A∗ A) = Vect{v3′ = −1/2}
                                                                            −1/2




13/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 25

~~~text
   Motivations               SVD         Pseudo-inverse         Méthode des moindres carrés   Fin

  Forme générale et décomposition



            4 Déduisons les vecteurs propres (normalisés) de C ∗ = A∗ A (lien avec
              V ), associés aux valeurs propres {λ1 ; λ2 ; λ3 }
                   v1 est associé à λ1 : A∗ Av1 = λ1 v1
                                                                              √ 
                                                                              1/ 2
                                                              1 ∗
                   Or on sait que AA u1 = λ1 u1 donc v1 = σ1 A u1 ie v1 =  1/2 
                                      ∗

                                                                               1/2
                   v2 est associé à λ2 : A Av2 = λ1 v2
                                          ∗

                                                                                0√
                                                                                  

                   Or on sait que AA∗ u2 = λ1 u2 donc v2 = σ12 A∗ u2 ie v2 = 1/√2
                                                                              1/ 2
                                                                           √ 
                                                                            1/ 2
                   v3 est associé à λ3 = 0 : E0 = Ker (A∗ A) = Vect{v3′ = −1/2}
                                                                            −1/2
                                                          v′
                 v1 et v2 sont déjà normalisés et v3 = ∥v3′ ∥
                                                           3




13/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 26

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Forme générale et décomposition

            5 Conclusion : A = UBV ∗ avec
                       B




14/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 27

~~~text
   Motivations               SVD         Pseudo-inverse     Méthode des moindres carrés   Fin

  Forme générale et décomposition

            5 Conclusion : A = UBV ∗ avec
                  B est de même taille de A, et sa diagonale contient les valeurs
                  singulières de A
                                        2 √0 0
                                                  
                                  B=                  ∈ M2,3 (R)
                                        0     2 0
            1    U




14/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 28

~~~text
   Motivations               SVD         Pseudo-inverse     Méthode des moindres carrés   Fin

  Forme générale et décomposition

            5 Conclusion : A = UBV ∗ avec
                  B est de même taille de A, et sa diagonale contient les valeurs
                  singulières de A
                                        2 √0 0
                                                  
                                  B=                  ∈ M2,3 (R)
                                        0     2 0
            1    U contient les vecteurs propres de AA∗ ie que les colonnes de U sont
                 les vecteurs (normalisés) u1 et u2 :
                                                 1 1 1
                                                          
                                          U=√
                                                  2 1 −1
            2    V




14/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 29

~~~text
   Motivations               SVD         Pseudo-inverse     Méthode des moindres carrés   Fin

  Forme générale et décomposition

            5 Conclusion : A = UBV ∗ avec
                  B est de même taille de A, et sa diagonale contient les valeurs
                  singulières de A
                                        2 √0 0
                                                  
                                  B=                  ∈ M2,3 (R)
                                        0     2 0
            1    U contient les vecteurs propres de AA∗ ie que les colonnes de U sont
                 les vecteurs (normalisés) u1 et u2 :
                                                 1 1 1
                                                          
                                          U=√
                                                  2 1 −1
            V contient les vecteurs propres de A∗ A ie les colonnes de V sont les
            2

            vecteurs (normalisés) v1 , v2 et v3 :
                                                                       √         √ 
                   1    0      1√                               1 1/ 2        1/ 2
                                                             
            1  √                                    T      1
        V =√    1/ 2 1 −1/ 2 donc V ∗ = V = √ 0                      1         1 
             2 1/√2 1 −1/√2                                  2 1 −1/√2 −1/√2

14/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 30

~~~text
   Motivations               SVD         Pseudo-inverse           Méthode des moindres carrés   Fin

  Dénitions et propriétés

         But Généraliser la notion d'inverse pour une matrice non inversibles (voir
         non carrée).
         Pseudo-inverse
         On appelle pseudo-inverse (ou inverse généralisée ou de Moore-Penrose)
         d'une matrice A ∈ Mm,n (K), la matrice A+ ∈ Mn,m (K) vériant

            1    AA+ est symétrique                       3   AA+ A = A
            2    A A est symétrique
                   +                                      4   A+ AA+ = A+

         Proposition
         Soit A ∈ Mm,n (K)
           1 Si m = n et A inversible, alors A+ = A−1

           2 Si m ≤ n et A de rang max (m), alors A+ = AT (AAT )−1 et

                 AA+ = Im
            3    Si m ≥ n et A de rang max (n), alors A+ = (AT A)−1 AT et
                 A+ A = In
15/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 31

~~~text
   Motivations               SVD                Pseudo-inverse       Méthode des moindres carrés   Fin

  Dénitions et propriétés


  Exemple - Déterminer la pseudo-inverse



                                            1 1 1 1
                                                                
                                         A=         ∈ M2,4 (R)
                                            5 7 7 9
         Comme m = 2 ≤ 4 = n et que rg (A) = 2 alors




16/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 32

~~~text
   Motivations               SVD                Pseudo-inverse       Méthode des moindres carrés   Fin

  Dénitions et propriétés


  Exemple - Déterminer la pseudo-inverse



                                            1 1 1 1
                                                                
                                         A=         ∈ M2,4 (R)
                                            5 7 7 9
         Comme m = 2 ≤ 4 = n et que rg (A) = 2 alors A+ = AT (AAT )−1




16/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 33

~~~text
   Motivations                SVD                      Pseudo-inverse                Méthode des moindres carrés   Fin

  Dénitions et propriétés


  Exemple - Déterminer la pseudo-inverse



                                             1 1 1 1
                                                                       
                                          A=         ∈ M2,4 (R)
                                             5 7 7 9
         Comme m = 2 ≤ 4 = n et que rg (A) = 2 alors A+ = AT (AAT )−1 avec

                        4 28                                                      102/16 −14/16
                                                                                                           
                        T                                            T −1
                   AA =                                et       (AA )           =
                        28 204                                                    −14/16  1/8

         D'où
                                                                 2          −1/4
                                                                                
                                                        1/4                  0 
                                                  A+ = 
                                                        1/4                  0 
                                                                                 

                                                        −3/2                 1/4
                                                                                       
                                      a   b                                     d    −b
         Rappel :            B=                   alors B −1 = det(B)
                                                                  1
                                      c   d                                     −c    a
16/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 34

~~~text
   Motivations               SVD                Pseudo-inverse             Méthode des moindres carrés   Fin

  SVD




         Proposition
         Soit A ∈ Mm,n (K) telle que

                                                                       01
                                                                          
                                         ∗                       D
                           A = UBV             avec B =                   ∈ Mm,n (K).
                                                                 02    03

         Alors
                                                                  −1
                                                                           02
                                                                               
                                                                  D
                      A+ = VB + U ∗            avec B + =                     ∈ Mn,m (K)
                                                                      01   03

         Exemple du cours
                                 1 1                                           1 1 −2
                                                                                            
                        A=                   alors    A+ = VB + U ∗ =
                                 2 2                                           10 1 −2


17/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 35

~~~text
   Motivations               SVD             Pseudo-inverse           Méthode des moindres carrés   Fin

  SVD


  Exemple - Déterminons la pseudo-inverse à l'aide de la SVD



                                                        √
                                               1           2 √0
                                                                 
                                            A=
                                               1          0    2
         On avait A = UBV ∗ avec
                                                                           1  0   1√
                                                                                                   
       2 √0 0                               1 1 1                     1  √
                                                           
    B=                                   U=√                      V =√   1/ 2 1 −1/ 2
       0   2 0                               2 1 −1                    2 1/√2 1 −1/√2

         Alors




18/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 36

~~~text
   Motivations               SVD             Pseudo-inverse           Méthode des moindres carrés   Fin

  SVD


  Exemple - Déterminons la pseudo-inverse à l'aide de la SVD



                                                        √
                                               1           2 √0
                                                                 
                                            A=
                                               1          0    2
         On avait A = UBV ∗ avec
                                                                           1  0   1√
                                                                                                   
       2 √0 0                               1 1 1                     1  √
                                                           
    B=                                   U=√                      V =√   1/ 2 1 −1/ 2
       0   2 0                               2 1 −1                    2 1/√2 1 −1/√2

         Alors A+ = VB + U ∗ avec




18/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 37

~~~text
   Motivations               SVD              Pseudo-inverse             Méthode des moindres carrés   Fin

  SVD


  Exemple - Déterminons la pseudo-inverse à l'aide de la SVD



                                                         √
                                                1           2 √0
                                                                    
                                             A=
                                                1          0    2
         On avait A = UBV ∗ avec
                                                                              1  0   1√
                                                                                                      
       2 √0 0                               1 1 1                        1  √
                                                            
    B=                                   U=√                         V =√   1/ 2 1 −1/ 2
       0   2 0                               2 1 −1                       2 1/√2 1 −1/√2

         Alors A+ = VB + U ∗ avec
                   1/2  0√                                                   1/4             1/4
                                                                                               
                                                                            √                √
            B + =  0 1/ 2                  U∗ = UT           et   A+ =  3 √2/8           −√ 2/8
                    0   0                                                 − 2/8             3 2/8

18/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 38

~~~text
   Motivations                 SVD         Pseudo-inverse     Méthode des moindres carrés   Fin

  Cas systèmes surdéterminés


         Soit m, n ∈ N∗ , considérons un système linéaire Ax = b avec
         A ∈ Mm,n (K) ; x ∈ Kn ; b ∈ Km ; m ̸= n et m > n (système
         surdéterminé).
         BUT
         Minimiser la norme quadratique (norme euclidienne au carré) d'une
         fonction e (fonction erreur)

         Problème aux moindres carrés
         Problème d'optimisation de la forme
                                               1
                                           minn ∥Ax − b∥22
                                           x∈K 2

         Ce problème de minimisation repose sur l'utilisation de la pseudo-inverse

                                         Ax = b ⇐⇒ x = A+ b

19/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 39

~~~text
   Motivations                 SVD           Pseudo-inverse       Méthode des moindres carrés   Fin

  Cas systèmes surdéterminés


  Exemple - Régression linéaire




         Trouver la droite d'équation ax + b = y
         passant "au mieux" par le nuage de points
         (xi ; yi )


         On cherche a, b ∈ R tel que axi + b = yi pour tout i ∈ {1; ...; n} ie

                                                        1
                                                                 
                                                x1                  y1
                                               x2      1  
                                                          a
                                                                   y2 
                                     Ux = v ⇔  .                =.
                                                                  
                                               ..         b      .. 
                                                          

                                               xn       1          yn

         La méthode des moindres carrés, appliquées à ce système surdéterminé,
         nous donne la solution x = U + v
20/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 40

~~~text
   Motivations                 SVD       Pseudo-inverse   Méthode des moindres carrés   Fin

  Cas systèmes surdéterminés


  Exemple - Interpolation parabolique




         Trouver le polynôme ax 2 + bx + c = y passant "au mieux" par le nuage
         de points (xi ; yi )
         On cherche a, b, c ∈ R tel que axi2 + bxi + c = yi pour tout i ∈ {1; ...; n}
         ie                          2
                                      x1 x1 1  
                                                            
                                                              y1
                                    x22 x2 1 a             y2 
                         Ux = v ⇔  .             b =  .. 
                                                   
                                     ..          c        .
                                      xn2 xn 1                yn
         La méthode des moindres carrés, appliquées à ce système surdéterminé,
         nous donne la solution x = U + b


21/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 41

~~~text
   Motivations               SVD         Pseudo-inverse   Méthode des moindres carrés   Fin

  Cas systèmes sous-déterminés




         Considérons un système linéaire Ax = b où A ∈ Mm,n (K) et b ∈ Km et
         traitons le cas où m < n.

         Le système est alors sous-déterminé et admet (en général) une innité de
         solutions (respectant une certaine forme, combinaison linéaire de certains
         vecteurs par ex.).
         Parmi cette innité de solutions, on peut par exemple chercher celle qui
         a la plus petite norme : le problème est alors transformé en un
         problème de minimisation pour lequel la méthode précédente (moindres
         carrés) s'applique parfaitement.

         La solution est alors donnée par x = A+ b




22/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~

## Page 42

~~~text
   Motivations               SVD         Pseudo-inverse      Méthode des moindres carrés   Fin




                                             Conclusion
         La SVD de A permet de déterminer les valeurs singulières de A et donc la
         norme spectrale de A (ainsi que son conditionnement).
         Cette décomposition permet également de déterminer la pseudo-inverse
         A+ , qui permet de résoudre des systèmes linéaires sur et sous-déterminés.


                                         Fin - Chapitre 2.

         Prochaine séance : TD (3h)
                 Télécharger la série de TD2 et préparer un maximum d'exercices
                 Travailler le cours (slides + support cours)
                 Compléter vos ches (2 feuilles RV autorisées à l'examen)


23/23
  Nelly BARRAU ( nelly.barrau@cyu.fr )
~~~
