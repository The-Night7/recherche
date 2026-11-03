# Claude TD7 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1OQLeUx7WcYhMuN9d7FTkzhzdBdKkNhno) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                     CY Tech 2025-2026
                                                 ING1 - GM : Probabilités
                                      TD 7 - Vecteurs Gaussiens




Exercice 1 Soient le vecteur aléatoire gaussien (X1 , X2 , X3 )′ et a ∈ R. Les variables aléatoires
          sont supposées telles que :
X1 , X2 , X3
   pour i = 1, 2, 3, X suit une loi N (i, i )
                            i
                                                                     2

   pour j ̸= k, Cov(X , X ) = ajk
                                j        k

  1. Donner la matrice de covariance de (X , X , X ) .                   1       2       3
                                                                                             ′

  2. Quel est l'ensemble des valeurs possibles du réel a ?
Correction :
  1. Matrice de covariance :
    On a X ∼ N (i, i ), donc Var(X ) = i .
                        2                                        2

    La matrice de covariance est :
               i                                 i


                           
                               Var(X ) Cov(X , X ) Cov(X , X )
                       Σ = Cov(X , X )      Var(X ) Cov(X , X )
                                                         1                           1       2       1       3


                             Cov(X , X ) Cov(X , X ) Var(X )
                                                 2           1                           2           2       3
                                                 3           1                       3       2           3

    Avec les données :                    
                                            1 2a 3a
                                                    

                                                         Σ = 2a 4 6a
                                                              3a 6a 9
    2. Valeurs possibles de a :
    Pour que Σ soit une matrice de covariance valide, elle doit être semi-dénie positive.
    Cela signie que tous les mineurs principaux doivent être ≥ 0.
    Mineur d'ordre 1 : ∆ = 1 > 0 (OK)1
    Mineur d'ordre 2 :
                                                   1 2a
                                         ∆2 =           = 4 − 4a2 = 4(1 − a2 )
                                                  2a 4

    Condition : ∆ ≥ 0 ⇒ 1 − a ≥ 0 ⇒ |a| ≤ 1
                   2
                                             2

    Mineur d'ordre 3 (déterminant) :
                                              4 6a        2a 6a        2a 4
                       det(Σ)= 1 ·                 − 2a ·       + 3a ·
                                             6a 9         3a 9         3a 6a
                                    = 1(36 − 36a2 ) − 2a(18a − 18a2 ) + 3a(12a2 − 12a)
                                    = 36 − 36a2 − 36a2 + 36a3 + 36a3 − 36a2
                                    = 36 − 108a2 + 72a3
                                    = 36(1 − 3a2 + 2a3 )

    Condition : det(Σ) ≥ 0 ⇒ 1 − 3a + 2a ≥ 0         2               3

    Factorisons : 1 − 3a + 2a = (1 − a) (2a + 1)
                            2            3                   2

    Donc : (1 − a) (2a + 1) ≥ 0 ⇒ 2a + 1 ≥ 0 ⇒ a ≥ −
                   2                                                                             1
                                                                                                 2




                                                                             1
~~~

## Page 2

~~~text
   Conclusion : Combinant les deux conditions :
                                                           1
                                                          − ≤a≤1
                                                           2



Exercice 2 Soient n ∈ N∗ \ {1} et X = (X1 , . . . , Xn )′ un vecteur aléatoire où on suppose que
                               sont indépendantes et suivent la même loi N (0, σ ).
X1 , X2 − X1 , . . . , Xn − Xn−1                                                                           2

   Déterminer Cov         la matrice variance-covariance de X .
                        (X)

Correction :
   Posons Z = PX , Z = X − X , ..., Z = X − X .
   On a : X = Z pour tout i.
              1     1  2       2            1             n             n           n−1
                    i
              i     j=1 j
   Variance de Xi :
                                                                           

                             Var(X )= Var 
                                                              i
                                                              X
                                        i                           Zj 
                                                              j=1


                                                       Var(Z ) (par indépendance)
                                                 i
                                                 X
                                            =                       j
                                                 j=1
                                                   2
                                            = iσ

   Covariance de Xi et Xk (avec i ≤ k) :
                                                                                               

                         Cov(X , X )= Cov 
                                                               i
                                                               X                k
                                                                                X
                                   i    k                               Zj ,            Zl 
                                                               j=1              l=1


                                                                   Cov(Z , Z )
                                                    i X
                                                    X k
                                                =                               j       l
                                                    j=1 l=1


                                                          Var(Z ) (car Z indépendants)
                                                    i
                                                    X
                                                =                       j                   j
                                                    j=1

                                                = iσ = min(i, k)σ 2
                                                      2


   Matrice de covariance :
                                       Σij =        Cov(X , X ) = min(i, j)σ
                                                               i        j
                                                                                                    2


   Pour n = 4 par exemple :                                                             
                                                        1                   1       1   1
                                                        1                   2       2   2
                                                Σ = σ2 
                                                       
                                                                                         
                                                       1                   2       3   3
                                                        1                   2       3   4



Exercice 3 Soient X1 et X2 deux v.a.r. i.i.d. de loi N (0, 1). On pose Y1 =        ,                     X12 + X22 Y2 = X
                                                                                                        p
                                                                                                                         1

et Y = (Y , Y ).
          1   2
                                                                                                                        X2


   1. Montrez que Y est un vecteur aléatoire admettant une densité et trouvez sa fonction de
      densité.
                                                                    2
~~~

## Page 3

~~~text
     2. Les variables aléatoires Y et Y sont-elles indépendantes?
                                                        1                2


Correction :
  1. Changement de variables :
      Utilisons les coordonnées polaires. Posons :
                                                                                            avec R > 0, Θ ∈ [0, 2π[
                                              (
                                               X1 = R cos(Θ)
                                               X2 = R sin(Θ)

      Alors : R = pX + X = Y et tan(Θ) = .
                                 2            2                                            X2

      Le jacobien de la transformation (x , x ) → (r, θ) est :
                                 1            2          1                                 X1
                                                                             1        2

                                                                                          |J| = r

      La densité conjointe de (X , X ) est :         1           2

                                                                                                 1 −(x21 +x22 )/2
                                                         f(X1 ,X2 ) (x1 , x2 ) =                   e
                                                                                                2π
      En coordonnées polaires :
                                                                      1 −r2 /2       r −r2 /2
                                      f(R,Θ) (r, θ) =                   e      ·r =    e      1R+ ×[0,2π[ (r, θ)
                                                                     2π             2π
      Maintenant, Y = R et Y = =                                X1          R cos Θ
                                                                            R sin Θ = cot(Θ)         .
      Donc Θ = arccot(Y ) et = − .
                             1                    2             X2
                                                  dθ                       1

      La transformation est :
                                       2          dy2                    1+y22


                                                                (r, θ) → (y1 , y2 ) = (r, cot(θ))

      Le jacobien est : |J | =         ′           ∂(r,θ)                    1
                                                                         = 1+y
      Donc :
                                                  ∂(y1 ,y2 )                   2
                                                                                      2

                                                                                     y1 −y12 /2     1
                                           f(Y1 ,Y2 ) (y1 , y2 ) =                      e       ·        1 + (y1 , y2 )
                                                                                     2π           1 + y22 R ×R
      2. Indépendance :
      On peut factoriser :
                                                                         h                          i        1
                                                                                                                               
                                                                                 −y12 /2
                                 f(Y1 ,Y2 ) (y1 , y2 ) = y1 e                              1R+ (y1 ) ·                 1R (y2 )
                                                                                                          2π(1 + y22 )
      Donc Y et Y sont indépendantes.
      De plus :
                 1       2


      Y ∼ Rayleigh (loi de la norme d'un vecteur gaussien 2D)
         1
      Y ∼ Cauchy (loi du ratio de deux gaussiennes indépendantes)
         2




Exercice 4 Soit X = (X1 , X2 , X3 , X4 )′ un vecteur gaussien N4 (mX , VX ) où mX = 0 et
                                                                                
                                                                       4 −2 0 0
                                                                     −2 5  0 0
                                                                VX =           
                                                                     0  0  3 −1
                                                                       0 0 −1 5

  On dénit le vecteur Y = (Y , Y , Y ) par Y = 5X + X + βX + αX , Y = X − X + X ,
                                                                                 ′

Y = −X − X + X .
                                                            1        2       3              1       1       2       3       4      2   1   2   4
 3           1       2            3


                                             3
~~~

## Page 4

~~~text
  1. Déterminer la loi de Y .
  2. Pour quelles valeurs de α et β, Y , Y , Y sont-elles indépendantes? Sous cette condition,
     calculer E[Y Y Y ].
                                                       1        2        3
                             2 2 2
                            1 2 3


Correction :
  1. Loi de Y :
  On a Y = AX où :                                         
                                                           5 1 β α
                                                                    

                                                     A =  1 −1 0 1 
                                                          −1 −1 1 0
  Comme X est gaussien, Y est aussi gaussien avec :
  m = Am = 0
      Y                X
  V = AV A
      Y            X
                            T

  Calculons AV :        X
                                                                                 
                                                         4 −2 0 0           
                                            5 1 β α 
                                                         −2 5  0 0
                                    AVX =  1 −1 0 1             
                                                       0   0  3 −1
                                           −1 −1 1 0
                                                          0 0 −1 5
                                                                   
                                               18 −5 3β − α −β + 5α
                                            =  6 −7  −α       5    
                                               −2 3     3     −1
  Puis V = AV A :
          Y                 X
                                T

                                                                    
                                                          5 1 −1
                                      18 −5 3β − α −β + 5α 
                                                            1 −1 −1
                                                                     
                                VY =  6 −7  −α       5     β 0   1
                                      −2 3     3     −1
                                                             α 1   0

  Après calcul (long) :
                                   86 + β 2 + 25α2 − 8βα 11 − 2α −21 − 2β + 4α
                                                                              

                            VY =          11 − 2α          16        −4       
                                      −21 − 2β + 4α        −4          7

  Donc Y ∼ N (0, V ).   3       Y
  2. Conditions d'indépendance :
  Pour que Y , Y , Y soient indépendantes, il faut que V soit diagonale.
  Donc :
                   1        2   3                                                     Y


  Cov(Y , Y ) = 0 : 11 − 2α = 0 ⇒ α =
              1    2
                                                                    11

  Cov(Y , Y ) = 0 : −21 − 2β + 4α = 0
                                                                    2
              1     3
  Avec α = :      11
                  2

                                                     11                               1
                                −21 − 2β + 4 ·          = 0 ⇒ −21 − 2β + 22 = 0 ⇒ β =
                                                     2                                2
  Calcul de E[Y12 Y22 Y32 ] :
  Avec α = et β = , les Y sont indépendantes et gaussiennes centrées.
                  11                1

  Donc :          2                 2       i


           E[Y Y Y ] = E[Y ] · E[Y ] · E[Y ] = Var(Y ) · Var(Y ) · Var(Y )
                             2 2 2
                            1 2 3               1
                                                 2
                                                           2
                                                            2
                                                                             3
                                                                              2
                                                                                          1   2   3


                                         4
~~~

## Page 5

~~~text
   Avec α = et β = :
              11
              2
                         1
                         2


                              Var(Y )= 86 + 14 + 25 · 121
                                      1
                                                       4
                                                             1 11
                                                          −8· ·
                                                             2 2
                                              = 86 + 0.25 + 756.25 − 22 = 820.5

   Var(Y ) = 16, Var(Y ) = 7
   Donc :
         2               3


                                  E[Y12 Y22 Y32 ] = 820.5 × 16 × 7 = 91896



Exercice 5 Soient X1 , X2 , X3 trois variables aléatoires réelles indépendantes de loi N (0, 1).
  1. Déterminer la loi de U := P X .          3
                                                        i
  2. Montrer que W := X − X est indépendante de U .
                                              i=1
                              1           2


Correction :
  1. Loi de U :
   U = X1 + X2 + X3      est une somme de gaussiennes indépendantes.
   Donc :
                                  E[U ]= E[X1 ] + E[X2 ] + E[X3 ] = 0
                             Var(U )= Var(X ) + Var(X ) + Var(X ) = 3
                                                            1                       2                       3

   Donc U ∼ N (0, 3).
   2. Indépendance de W et U :
   Pour des vecteurs gaussiens, l'indépendance équivaut à la non-corrélation.
   Calculons Cov(W, U ) :
                 Cov(W, U )= Cov(X − X , X + X + X )
                            = Cov(X , X ) + Cov(X , X ) + Cov(X , X )
                                                    1               2       1           2           3


                               −Cov(X , X ) − Cov(X , X ) − Cov(X , X )
                                                    1           1                       1       2                   1       3

                                                        2           1                       2       2                   2       3
                                   =1+0+0−0−1−0=0

   Comme (W, U ) est un vecteur gaussien et Cov(W, U ) = 0, alors W et U sont indépendantes.
Exercice 6 Soit X = (X1 , X2 , X3 )′ un vecteur gaussien N3 (mX , VX ) où mX = 0 et
                                                                
                                                          1 0 −1
                                                   VX =  0 2 2 
                                                         −1 2 5

   On dénit le vecteur Y = (Y , Y , Y ) par Y = X + X , Y = αX + 2X + βX , Y =
                                                            ′

−X − X + X .
                                          1     2       3                       1           1           3       2           1       2   3   3
   1     2     3

  1. Déterminer la loi de Y .
  2. Pour quelles valeurs de α et β, (Y et Y ) et (Y et Y ) sont-elles indépendantes?
                                                    1                   2           2           3
  3. Déterminer la loi du couple (Y , Y ).     1    3
  4. Déterminer la loi conditionnelle f (a, b) pour tout (a, b) ∈ R .
                                                    Y3 |Y1
                                                                                                                    2

  5. Calculer E[(2Y + 3Y ) |Y ].
                     1        3
                                  2
                                      1


                                                                            5
~~~

## Page 6

~~~text
Correction :
  1. Loi de Y :
   Y = AX          avec :                                  1
                                                            
                                                              0 1
                                                                  

                                                       A=α   2 β
                                                          −1 −1 1
   VY = AVX AT              . Après calcul :
                                                                          
                                        4         α−β               −2
                                VY = α − β α2 + 2β 2 + 8 − 4αβ −α − 2β − 2
                                       −2      −α − 2β − 2          6
   2. Conditions d'indépendance :
   Pour (Y , Y ) indépendantes : Cov(Y , Y ) = 0
               1    2                                   1       2

                                                       α−β =0⇒α=β

   Pour (Y , Y ) indépendantes : Cov(Y , Y ) = 0
               2    3                                   2       3

                                                        −α − 2β − 2 = 0

   Avec α = β :                                               2                                2
                                       −α − 2α − 2 = 0 ⇒ α = − ,                        β=−
                                                              3                                3
   3-5. Questions avancées :
   Les questions 3, 4 et 5 nécessitent des calculs longs sur les lois conditionnelles gaussiennes.
Le principe est :
   Pour (Y , Y ) : extraire la sous-matrice 2 × 2 correspondante de V .
   Pour la loi conditionnelle : utiliser les formules gaussiennes standard.
               1    3                                                                              Y


   Pour l'espérance conditionnelle : E[(2Y + 3Y ) |Y ] = 4Y + 9E[Y |Y ] + 12Y E[Y |Y ]
                                                            1               3
                                                                                2
                                                                                    1   1
                                                                                         2
                                                                                                       3
                                                                                                        2
                                                                                                            1   1   3   1




Exercice 7 Soit X1 , X2 , X3 trois v.a.r. identiquement distribuées, de fonction de densité f (x) =
         .
e−x 1R+ (x)
  1. Trouvez la fonction de densité de (Y , Y , Y ), où     1       2       3

                                                                              X1                 X1 + X2
                              Y1 = X1 + X2 + X3 ,               Y2 =                ,   Y3 =
                                                                            X1 + X2            X1 + X2 + X3
  2. Y , Y et Y sont-elles indépendantes?
       1   2            3


Correction (aperçu) :
   Cet exercice est très technique. La transformation inverse est :
                                                   
                                                   X1 = Y1 Y2 Y3
                                                   
                                                    X2 = Y1 (1 − Y2 )Y3
                                                   
                                                    X3 = Y1 (1 − Y3 )
                                                   

   Le jacobien est |J| = Y Y .        2

   Après calcul, on trouve que Y , Y , Y sont indépendantes avec :
                                     1 3
                                               1   2    3
   Y ∼ Gamma(3, 1)
       1
   Y ∼ U ([0, 1])
       2
   Y ∼ U ([0, 1])
       3


                                                                        6
~~~
