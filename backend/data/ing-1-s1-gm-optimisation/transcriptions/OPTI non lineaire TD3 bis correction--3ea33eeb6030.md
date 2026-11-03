# OPTI non lineaire TD3 bis correction.pdf

[Ouvrir l’original](https://drive.google.com/open?id=11V4w9mgsaZjK3TchYAOd6Yk9RO4dHkS1) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
       Correction Complète TD3
       Optimisation avec contraintes d’égalité et d’inégalité


                  CY Tech - 1ère année Ingénieurs
                         Année 2024-2025


Table des matières




                                 1
~~~

## Page 2

~~~text
Optimisation Non Linéaire - TD3                                 Génie Mathématique - ING1


1     Optimisation sans contraintes

       Rappel de Cours
    1. Existence (Coercivité) : Une fonction continue f : Rn → R est dite coercive
    si
                                 lim f (x) = +∞.
                                      ∥x∥→+∞

    Toute fonction continue et coercive sur Rn admet au moins un minimum global.
       2. Condition Nécessaire d’ordre 1 (CN1) : Si x∗ est un extremum local
    de f et si f est différentiable en x∗ , alors

                         ∇f (x∗ ) = 0 (x∗ est un point critique).

       3. Condition Suffisante d’ordre 2 (CS2) : Si ∇f (x∗ ) = 0 et la matrice
    Hessienne ∇2 f (x∗ ) est :
       — définie positive (toutes valeurs propres > 0) : x∗ est un minimum local
           strict,
       — définie négative (toutes valeurs propres < 0) : x∗ est un maximum local
           strict,
       — indéfinie : x∗ est un point selle.
       4. Convexité stricte : Si ∇2 f (x) est définie positive pour tout x ∈ Rn , alors
    f est strictement convexe et admet au plus un minimum global.


Exercice 1 : Étude complète d’une fonction quadratique
    Énoncé : Soit f (x, y) = x2 + y 2 − 2x + y.

1. Existence d’une solution

       Méthode
    Pour montrer l’existence, on montre que f est coercive en mettant sous forme
    canonique.


    Complétons les carrés :

                     f (x, y) = (x2 − 2x) + (y 2 + y)
                                                              1 1
                                                                       
                                  2                         2
                              = (x − 2x + 1 − 1) + y + y + −
                                                              4 4
                                                       2
                                                     1      1
                                              
                              = (x − 1)2 − 1 + y +        −
                                                     2      4
                                                  2
                                                1       5
                                           
                              = (x − 1)2 + y +       −
                                                2       4
    Cette forme canonique montre clairement que :

                                      lim      f (x, y) = +∞.
                                 ∥(x,y)∥→+∞


                                                2
~~~

## Page 3

~~~text
Optimisation Non Linéaire - TD3                                     Génie Mathématique - ING1


   Conclusion : La fonction f est continue et coercive sur R2 , donc elle admet au
moins un minimum global.

2. Unicité de la solution

      Méthode
   Pour l’unicité, on étudie la Hessienne de f pour déterminer si f est strictement
   convexe.

   Calculons le gradient et la Hessienne :
                                             ∂f
                                                     !               !
                                             ∂x            2x − 2
                             ∇f (x, y) =     ∂f          =
                                             ∂y
                                                           2y + 1
                                                              
                                        ∂2f               ∂2f              !
                          2                  2                       2 0
                         ∇ f (x, y) =  ∂∂x2 f           ∂x∂y 
                                                          ∂2f   =
                                       ∂y∂x               ∂y 2
                                                                     0 2
   Cette matrice est diagonale avec valeurs propres λ1 = λ2 = 2 > 0.
   La Hessienne est donc définie positive pour tout (x, y) ∈ R2 .
   Conclusion : La fonction f est strictement convexe, donc le minimum global est
unique.

3. Points critiques et leur nature Résolvons ∇f (x, y) = 0 :
                                                          
                           2x − 2 = 0                     x = 1
                                                           
                                                 ⇐⇒               1
                           2y + 1 = 0                     y = −
                                                           
                                                                     2

                                      1
                                       
   Le point critique est : x∗ = 1, −      .
                                      2
   D’après l’étude de la Hessienne (définie positive), ce point est un minimum local
strict.
   Puisque f est coercive et strictement convexe, c’est aussi le minimum global unique.
   La valeur minimale est :
                                               1    5
                                                          
                                    ∗
                               f (x ) = f 1, −   =−
                                               2    4

                                                                                    1                    5
                                                                                       
   Réponse finale : Le minimum global unique est atteint en                    1, −         avec fmin = − .
                                                                                    2                    4




                                                 3
~~~

## Page 4

~~~text
Optimisation Non Linéaire - TD3                               Génie Mathématique - ING1


2     Optimisation avec contraintes d’égalité

       Rappel de Cours
    Problème général : Minimiser f (x) sous h(x) = 0 où h : Rn → Rp .
      1. Lagrangien :
                            L(x, λ) = f (x) + λT h(x)
    où λ ∈ Rp est le vecteur des multiplicateurs de Lagrange.
        2. Conditions Nécessaires du Premier Ordre (Théorème de Lagrange) :
    Si x∗ est un minimum local régulier (point qualifié), il existe λ∗ ∈ Rp tel que :
                            
                            ∇ L(x∗ , λ∗ ) = 0        (stationnarité)
                                x
                                    ∗
                            h(x ) = 0                (admissibilité)

       3. Cône Tangent : Le cône tangent à l’ensemble {x : h(x) = 0} en x∗ est :

                    T (x∗ ) = {y ∈ Rn : ∇h(x∗ )T y = 0} = Ker(∇h(x∗ ))

       4. Condition Suffisante du Second Ordre : Si de plus la Hessienne du
    Lagrangien restreinte au cône tangent est définie positive :

                       ∀y ∈ T (x∗ ), y ̸= 0 =⇒ y T ∇2xx L(x∗ , λ∗ )y > 0

    alors x∗ est un minimum local strict.


Exercice 2 : Projection sur un hyperplan
   Énoncé : Calculer la distance d’un point x0 ∈ Rn au plan défini par Ax = b, où
A ∈ Mp×n (R) et Rang(A) = p.

       Méthode
    On minimise la distance au carré (pour simplifier) : min 12 ∥x − x0 ∥2 sous Ax = b.


Résolution par Lagrange Le Lagrangien est :
                                1
                       L(x, λ) = (x − x0 )T (x − x0 ) + λT (Ax − b)
                                2
    Condition de stationnarité :
                      ∇x L = x − x0 + AT λ = 0 =⇒ x = x0 − AT λ
    Injection dans la contrainte :
                  Ax = b =⇒ A(x0 − AT λ) = b =⇒ Ax0 − AAT λ = b
    Comme Rang(A) = p, la matrice AAT ∈ Mp×p (R) est inversible :
                                        λ = (AAT )−1 (Ax0 − b)

                                                  4
~~~

## Page 5

~~~text
Optimisation Non Linéaire - TD3                                 Génie Mathématique - ING1


   Solution (projection orthogonale) :

                               x∗ = x0 − AT (AAT )−1 (Ax0 − b)

   Distance au plan :

                   d(x0 , Plan) = ∥x∗ − x0 ∥ =          AT (AAT )−1 (Ax0 − b)


Exercice 3 : Condition nécessaire d’optimalité du second ordre
    Énoncé : Soit x̂ un point régulier solution du problème (PCE ). Montrer qu’il existe
un unique vecteur λ ∈ Rp vérifiant ∇x L(x̂, λ) = 0, et que pour tout y ∈ T (x̂), y ̸= 0, on
a y T ∇2xx L(x̂, λ)y ≥ 0.

      Rappel de Cours
   Théorème (CN du second ordre) :
      Soit x̂ un minimum local du problème sous contraintes d’égalité, et supposons
   que x̂ est régulier (les gradients ∇hi (x̂) sont linéairement indépendants).
      Alors il existe un unique λ̂ ∈ Rp tel que :
       1. ∇x L(x̂, λ̂) = 0
       2. Pour tout y ∈ T (x̂) = Ker(∇h(x̂)) avec y ̸= 0 :

                                          y T ∇2xx L(x̂, λ̂)y ≥ 0


   Démonstration (esquisse) :

Unicité de λ : La condition de stationnarité s’écrit :
                                              p
                                              X
                                  ∇f (x̂) +         λi ∇hi (x̂) = 0
                                              i=1

    Ceci est un système linéaire en λ. Puisque x̂ est régulier, les vecteurs ∇hi (x̂) sont
linéairement indépendants, donc le système admet une solution unique.

Positivité de la forme quadratique : Pour tout y ∈ T (x̂), considérons une courbe
admissible γ(t) telle que γ(0) = x̂ et γ ′ (0) = y.
   La fonction φ(t) = f (γ(t)) admet un minimum local en t = 0, donc φ′′ (0) ≥ 0.
   Or, par dérivation de la contrainte :

                             φ′′ (0) = y T ∇2 f (x̂)y + termes en ∇h

   En utilisant le Lagrangien et le fait que y ∈ T (x̂), on obtient :

                                 φ′′ (0) = y T ∇2xx L(x̂, λ̂)y ≥ 0




                                                    5
~~~

## Page 6

~~~text
Optimisation Non Linéaire - TD3                            Génie Mathématique - ING1


Exercice 4 : Résolution par substitution et Lagrange
Problème (P1)
   Énoncé :
          
          
          
          
          
            Optimiser
                 
                      f (x1 , x2 , x3 , x4 ) = 2x1 − 2x21 − 5x22 − x23 + 4x3 + 4x4
                 x − 2x = 2
                   4      2
          
           sous
          
                x3 − x1 = 1


Méthode 1 : Substitution Des contraintes, on tire : x4 = 2x2 + 2 et x3 = x1 + 1.
  Substituons dans f :

           f (x1 , x2 ) = 2x1 − 2x21 − 5x22 − (x1 + 1)2 + 4(x1 + 1) + 4(2x2 + 2)
                        = 2x1 − 2x21 − 5x22 − x21 − 2x1 − 1 + 4x1 + 4 + 8x2 + 8
                        = −3x21 + 4x1 − 5x22 + 8x2 + 11

   Cherchons les points critiques :
                                                          
                                              x = 2
                                            !
                             −6x1 + 4            1   3
                        ∇f =           = 0 =⇒
                             −10x2 + 8         x2 = 4
                                                                  5


   D’où : x3 = x1 + 1 = 53 et x4 = 2x2 + 2 = 18
                                             5
                                                .
   Hessienne :                                    !
                                    2      −6 0
                                  ∇f=
                                            0 −10
   Cette matrice est définie négative, donc il s’agit d’un maximum.
                       2 4 5 18
                                
   Solution : x∗ =      , , ,       est le maximum global.
                       3 5 3 5

Méthode 2 : Multiplicateurs de Lagrange Lagrangien :

   L(x, λ) = 2x1 − 2x21 − 5x22 − x23 + 4x3 + 4x4 + λ1 (x4 − 2x2 − 2) + λ2 (x3 − x1 − 1)

   Conditions de stationnarité :
                                 ∂L
                                     = 2 − 4x1 − λ2 = 0                                   (1)
                                 ∂x1
                                 ∂L
                                     = −10x2 − 2λ1 = 0                                    (2)
                                 ∂x2
                                 ∂L
                                     = −2x3 + 4 + λ2 = 0                                  (3)
                                 ∂x3
                                 ∂L
                                     = 4 + λ1 = 0                                         (4)
                                 ∂x4
   De (4) : λ1 = −4
   De (2) : −10x2 + 8 = 0 =⇒ x2 = 54
   De (3) : λ2 = 2x3 − 4
   De (1) : 2 − 4x1 − (2x3 − 4) = 0 =⇒ 6 − 4x1 − 2x3 = 0

                                                6
~~~

## Page 7

~~~text
Optimisation Non Linéaire - TD3                             Génie Mathématique - ING1


   Avec x3 = x1 + 1 : 6 − 4x1 − 2(x1 + 1) = 0 =⇒ 4 − 6x1 = 0 =⇒ x1 = 23
   Donc : x3 = 53 , x4 = 18
                         5
                            , λ2 = 2 · 53 − 4 = −2
                                                 3
                                                   .
   Vérification du second ordre :

                                         −4 0   0 0
                                                              
                                         0 −10 0 0
                               ∇2xx L = 
                                                   
                                         0  0 −2 0
                                                    

                                          0  0  0 0
   Matrice Jacobienne des contraintes :
                                                           !
                                       0 −2 0 1
                                  ∇h =
                                       −1 0 1 0
    Le cône tangent T (x∗ ) est de dimension 2. Sur ce sous-espace, la Hessienne restreinte
est définie négative, confirmant que x∗ est un maximum local strict.

Problème (P2)
   Énoncé :
        
        
        
        
        
          Optimiser
               
                    f (x1 , x2 , x3 , x4 ) = −x21 − x22 − x23 + 4x1 + 6x2 + 4x3 + 2x4
               x − 2x = 0
                  4     2
        
         sous
        
               x3 − x1 = 1


Méthode 1 : Substitution Des contraintes : x4 = 2x2 et x3 = x1 + 1.
  Substituons :
           f (x1 , x2 ) = −x21 − x22 − (x1 + 1)2 + 4x1 + 6x2 + 4(x1 + 1) + 2(2x2 )
                        = −x21 − x22 − x21 − 2x1 − 1 + 4x1 + 6x2 + 4x1 + 4 + 4x2
                        = −2x21 + 6x1 − x22 + 10x2 + 3
   Points critiques :
                                                          
                                               x = 3
                                              !
                              −4x1 + 6            1   2
                         ∇f =           = 0 =⇒
                              −2x2 + 10         x2 = 5

   D’où : x3 = x1 + 1 = 52 et x4 = 2x2 = 10.
   Hessienne :                                   !
                                            −4 0
                                   ∇2 f =
                                             0 −2
   Définie négative =⇒ maximum.
                       3     5
                                 
                 ∗
   Solution : x =        , 5, , 10 est le maximum global.
                       2     2
   Valeur optimale :
                                            9      3
                           f (x∗ ) = −2 ·     + 6 · − 25 + 50 + 3
                                            4      2
                                      9
                                  = − + 9 − 25 + 50 + 3
                                      2
                                    65
                                  =
                                     2

                                                  7
~~~

## Page 8

~~~text
Optimisation Non Linéaire - TD3                                     Génie Mathématique - ING1


Méthode 2 : Lagrange Lagrangien :

     L = −x21 − x22 − x23 + 4x1 + 6x2 + 4x3 + 2x4 + λ1 (x4 − 2x2 ) + λ2 (x3 − x1 − 1)

   Conditions :
                                  ∂L
                                      = −2x1 + 4 − λ2 = 0
                                  ∂x1
                                  ∂L
                                      = −2x2 + 6 − 2λ1 = 0
                                  ∂x2
                                  ∂L
                                      = −2x3 + 4 + λ2 = 0
                                  ∂x3
                                  ∂L
                                      = 2 + λ1 = 0
                                  ∂x4
   De la dernière : λ1 = −2
   De la deuxième : −2x2 + 6 + 4 = 0 =⇒ x2 = 5
   De la troisième : λ2 = 2x3 − 4
   De la première : −2x1 + 4 − (2x3 − 4) = 0 =⇒ −2x1 − 2x3 + 8 = 0
   Avec x3 = x1 + 1 : −2x1 − 2(x1 + 1) + 8 = 0 =⇒ −4x1 + 6 = 0 =⇒ x1 = 32
   On retrouve la même solution.

Exercice 5 : Intersection de cylindres
   Énoncé : Résoudre dans R3 :

                                            min           (x + z)
                                    x2 +y 2 =1, y 2 +z 2 =4


Résolution par Lagrange Lagrangien :

                  L(x, y, z, λ, µ) = x + z + λ(x2 + y 2 − 1) + µ(y 2 + z 2 − 4)

   Conditions de stationnarité :
                                     ∂L
                                        = 1 + 2λx = 0                                     (1)
                                     ∂x
                                     ∂L
                                        = 2λy + 2µy = 0                                   (2)
                                     ∂y
                                     ∂L
                                        = 1 + 2µz = 0                                     (3)
                                     ∂z
   De (2) : 2y(λ + µ) = 0 =⇒ y = 0 ou λ = −µ

Cas 1 : λ = −µ De (1) et (3) : 1 + 2λx = 0 et 1 − 2λz = 0
  Donc : 2λx = −1 et 2λz = 1 =⇒ x = −z
  Avec les contraintes :
  — x2 + y 2 = 1
  — y2 + z2 = 4
  Si x = −z : x2 + y 2 = 1 et y 2 + x2 = 4
  Contradiction : 1 = 4. Ce cas est impossible.

                                                    8
~~~

## Page 9

~~~text
Optimisation Non Linéaire - TD3                                 Génie Mathématique - ING1


Cas 2 : y = 0 Les contraintes deviennent :
  — x2 = 1 =⇒ x = ±1
  — z 2 = 4 =⇒ z = ±2
  On cherche à minimiser x + z, donc on prend les valeurs négatives :
                                x = −1,        y = 0,       z = −2

   Valeur optimale : x + z = −1 + (−2) = −3
   Vérification : Les autres combinaisons donnent :
   — (1, 0, 2) : x + z = 3
   — (1, 0, −2) : x + z = −1
   — (−1, 0, 2) : x + z = 1
   Le minimum est bien −3.

Exercice 6 : Optimisation avec contraintes quadratiques
Problème (P1)
   Énoncé :            
                       Optimiser f (x , x , x ) = x              2     2
                                          1     2       3    1 + x2 + x 3
                       sous x1 + x2 = 1
                                      2


Méthode de substitution De la contrainte : x1 = 1 − x22
  Substituons dans f :
                         F (x2 , x3 ) = (1 − x22 ) + x22 + x23 = 1 + x23
   Cette fonction ne dépend plus de x2 ! Elle est minimale pour x3 = 0.
   Solution : Pour tout x2 ∈ R, le point (1 − x22 , x2 , 0) est un minimum avec :

                                              fmin = 1

   L’ensemble des minima est : {(1 − x22 , x2 , 0) : x2 ∈ R}

Vérification par Lagrange Lagrangien :
                            L = x1 + x22 + x23 + λ(x1 + x22 − 1)
   Conditions :
              1 + λ = 0 =⇒ λ = −1
         2x2 + 2λx2 = 0 =⇒ 2x2 (1 + λ) = 0 =⇒ x2 · 0 = 0 (toujours vrai)
                2x3 = 0 =⇒ x3 = 0
   Avec x3 = 0 et la contrainte x1 + x22 = 1, on retrouve la même famille de solutions.

Problème (P2)
   Énoncé :            
                       Optimiser f (x , x , x ) = x              2    2
                                          1    2        3   1 + 2x2 + x3
                       sous x1 − x2 = 1
                                      2


                                                    9
~~~

## Page 10

~~~text
Optimisation Non Linéaire - TD3                                 Génie Mathématique - ING1


Méthode de substitution De la contrainte : x1 = 1 + x22
  Substituons :

                        F (x2 , x3 ) = (1 + x22 ) + 2x22 + x23 = 1 + 3x22 + x23

   Points critiques :                     !
                                  6x2
                             ∇F =     = 0 =⇒ x2 = 0, x3 = 0
                                  2x3
   D’où x1 = 1 + 0 = 1.
   Hessienne :                                            !
                                              26 0
                                          ∇F =
                                               0 2
   Définie positive =⇒ minimum.
   Solution : x∗ = (1, 0, 0) avec fmin = 1

Vérification par Lagrange Lagrangien :

                              L = x1 + 2x22 + x23 + λ(x1 − x22 − 1)

   Conditions :

                         1 + λ = 0 =⇒ λ = −1
                    4x2 − 2λx2 = 0 =⇒ 4x2 + 2x2 = 0 =⇒ x2 = 0
                           2x3 = 0 =⇒ x3 = 0

   Avec x2 = x3 = 0 et la contrainte : x1 = 1.
   On retrouve la même solution unique.




                                                  10
~~~

## Page 11

~~~text
Optimisation Non Linéaire - TD3                                Génie Mathématique - ING1


3     Optimisation avec contraintes d’inégalité (KKT)

       Rappel de Cours
    Problème général : Minimiser f (x) sous gj (x) ≤ 0 pour j = 1, . . . , m.
      1. Ensemble admissible :

                           K = {x ∈ Rn : gj (x) ≤ 0, j = 1, . . . , m}

        2. Contraintes actives : En un point x∗ , la contrainte gj est dite active si
    gj (x∗ ) = 0.
        3. Qualification des contraintes (LICQ) : Un point x∗ est dit qualifié (ou
    régulier) si les gradients des contraintes actives sont linéairement indépendants.
        4. Conditions de Karush-Kuhn-Tucker (KKT) - Conditions Néces-
    saires :
        Si x∗ est solution et qualifié, il existe µ = (µ1 , . . . , µm ) ∈ Rm tel que :
                                          Pm
       1. Stationnarité : ∇f (x∗ ) +                        ∗
                                               j=1 µj ∇gj (x ) = 0
                                                ∗
       2. Admissibilité primale : gj (x ) ≤ 0 pour tout j
       3. Admissibilité duale : µj ≥ 0 pour tout j
       4. Écart complémentaire : µj gj (x∗ ) = 0 pour tout j
       5. Cône tangent :
                     n                                                           o
            T (x∗ ) = y ∈ Rn : ∇gj (x∗ )T y ≤ 0 pour toute contrainte active j

       6. Condition Suffisante du Second Ordre : Si de plus :

                         ∀y ∈ T (x∗ ), y ̸= 0 =⇒ y T ∇2xx L(x∗ , µ∗ )y > 0

    alors x∗ est un minimum local strict.


Exercice 7 : Application complète des conditions KKT
    Énoncé :         
                     
                     Minimiser   f (x) = x31 + 2x1 x2 + 15x1 + 10x2
                     
                                                  √
                           g (x) = −x + x − 2 ≤ 0
                              1           1     2
                     sous 
                     
                             g2 (x) = x2 − x2 − 2 ≤ 0
                     
                     
                                           1

    On considère le point y = (−1, −1).

1. Admissibilité et qualification Vérification de l’admissibilité :
                                         √       √
                g1 (y) = −(−1) + (−1) − 2 = − 2 < 0 (inactive)
                g2 (y) = (−1)2 − (−1) − 2 = 1 + 1 − 2 = 0 (active)
    Le point y ∈ K (ensemble admissible).
    Qualification (LICQ) : Seule g2 est active. Son gradient est :
                                          !                          !
                                   2x1                      −2
                         ∇g2 (x) =             =⇒ ∇g2 (y) =    ̸ 0
                                                                =
                                   −1                       −1

                                                  11
~~~

## Page 12

~~~text
Optimisation Non Linéaire - TD3                                  Génie Mathématique - ING1


   Un seul vecteur non nul est toujours linéairement indépendant. =⇒ y est qualifié.

2. Cône tangent en y       Le cône tangent est :
                                         n                             o
                               T (y) = v ∈ R2 : ∇g2 (y)T v ≤ 0

                                                           !
                               T
                                                        v1
                      ∇g2 (y) v = −2 −1                      = −2v1 − v2 ≤ 0
                                                          v2

                T (y) = {v = (v1 , v2 ) : −2v1 − v2 ≤ 0} = {v : v2 ≥ −2v1 }
   Géométriquement, c’est un demi-plan.

3. Conditions de KKT Rappel : Le Lagrangien est :

                            L(x, µ) = f (x) + µ1 g1 (x) + µ2 g2 (x)

   Conditions à vérifier :
   1. ∇x L(y, µ) = 0 (stationnarité)
   2. µ1 , µ2 ≥ 0 (positivité)
   3. µ1 g1 (y) = 0 et µ2 g2 (y) = 0 (écart complémentaire)
   Écart complémentaire :
   — g1 (y) < 0 =⇒ µ1 = 0
   — g2 (y) = 0 =⇒ µ2 quelconque
   Stationnarité :
                       ∇f (y) + µ1 ∇g1 (y) + µ2 ∇g2 (y) = 0
   Calculons les gradients :
                                             !                                 !   !
                    3x21 + 2x2 + 15                          3 − 2 + 15   16
           ∇f (x) =                              =⇒ ∇f (y) =            =
                        2x1 + 10                              −2 + 10     8
                                                 !                         !
                                     −1                             −2
                           ∇g1 (x) =    ,                 ∇g2 (y) =
                                      1                             −1
   Avec µ1 = 0 :                             !              !
                                         16      −2
                                            + µ2    =0
                                          8      −1
   Système :                     
                                 16 − 2µ
                                             2 = 0
                                 8 − µ2 = 0
                                                           =⇒ µ2 = 8

   Les deux équations donnent µ2 = 8 ≥ 0.
   Conclusion : y satisfait les conditions KKT avec µ1 = 0, µ2 = 8.




                                                     12
~~~

## Page 13

~~~text
Optimisation Non Linéaire - TD3                                             Génie Mathématique - ING1


4. Condition suffisante du second ordre Hessienne du Lagrangien :

                                     ∇2xx L = ∇2 f (y) + µ2 ∇2 g2 (y)

   Calculons :                                       !                                   !
                        2        6x1 2                              2 −6 2
                       ∇ f (x) =                         =⇒ ∇ f (y) =
                                  2 0                                 2 0
                                                                        !
                                             2       2 0
                                          ∇ g2 (x) =
                                                     0 0
                                                         !                  !            !
                                             −6 2    2 0   10 2
                    ∇2xx L(y, µ) =                +8     =
                                              2 0    0 0   2 0
   Vérification sur le cône tangent :
   Un vecteur v ∈ T (y) vérifie ∇g2 (y)T v ≤ 0, soit −2v1 − v2 ≤ 0.
   Pour la condition du second ordre stricte, on considère les vecteurs tangents à la
contrainte active :

                  ∇g2 (y)T v = 0 =⇒ −2v1 − v2 = 0 =⇒ v2 = −2v1

   Prenons v = (1, −2)T (direction tangente) :
                                                                            !        !
                                T
                                                                10 2           1
                            v       ∇2xx Lv =        1 −2
                                                                  2 0           −2
                                             !                          !
                                   10 − 4       6
                 = 1 −2                     = 1 −2    =6−4=2>0
                                     2−0            2
   Conclusion : La condition suffisante du second ordre est vérifiée.

                       y = (−1, −1) est un minimum local strict


Exercice 8 : Contraintes mixtes (égalité + inégalité)
   Énoncé :
                 
                 
                 
                 
                 
                   Minimiser
                        
                             f (x, y, z) = x + 2y + 3z
                        x2 + y 2 + z 2 = 1 (contrainte d’égalité)
                 
                  sous 
                 
                         x+y+z ≤0            (contrainte d’inégalité)

Approche géométrique La fonction objectif f (x, y, z) = x + 2y + 3z = u · x avec
u = (1, 2, 3) est une forme linéaire.
   Sur la sphère unité ∥x∥ = 1, le minimum de u · x est atteint en :
                                                               u
                                                 x=−
                                                              ∥u∥

   Calculons :                               √                              √
                                     ∥u∥ =       12 + 22 + 32 =              14


                                                         13
~~~

## Page 14

~~~text
Optimisation Non Linéaire - TD3                           Génie Mathématique - ING1


                                                                 !
                             (1, 2, 3)     1    2    3
                         P =− √        = −√ , −√ , −√
                                 14        14   14    14
   Vérification de la contrainte d’inégalité :
                                    1   2   3     6
                  xP + yP + zP = − √ − √ − √ = − √ < 0 ✓
                                    14  14  14    14
   La contrainte est satisfaite ! La contrainte d’inégalité est donc inactive.
   Valeur optimale :
                                                                  √
                                                    !
                                             ∥u∥
                    f (P ) = u · P = ∥u∥ · −            = −∥u∥ = − 14
                                             ∥u∥

   Solution :                                                !
                                ∗    1    2    3
                               x = −√ , −√ , −√
                                     14   14   14
                                            √
                                    fmin = − 14 ≈ −3.742

Vérification par Lagrange Puisque la contrainte d’inégalité est inactive, on peut igno-
rer µ et résoudre uniquement avec la contrainte d’égalité :
    Lagrangien : L = x + 2y + 3z + λ(x2 + y 2 + z 2 − 1)
    Conditions :
                                                      1
                                1 + 2λx = 0 =⇒ x = −
                                                     2λ
                                                     1
                                2 + 2λy = 0 =⇒ y = −
                                                     λ
                                                      3
                                3 + 2λz = 0 =⇒ z = −
                                                     2λ
   Contrainte :
                                                   1   1   9
                         x2 + y 2 + z 2 = 1 =⇒       +   +   =1
                                                  4λ2 λ2 4λ2
                       1+4+9        14              14   7
                           2
                             = 1 =⇒   2
                                        = 1 =⇒ λ2 =    =
                         4λ         4λ               4   2
                   q
                       7
   Prenant λ = −       2
                         (négatif pour avoir un minimum) :
                                        1    1     1
                                x=−       = q    =√
                                       2λ  2 7/2   14
                                                                     q
                                                                         7
   Mais cela donne le maximum ! Pour le minimum, on prend λ =            2
                                                                           :
                        1       1                      2           3
                   x=− q    = −√ ,               y = −√ ,    z = −√
                      2 7/2     14                     14           14
   On retrouve bien notre solution.




                                             14
~~~

## Page 15

~~~text
Optimisation Non Linéaire - TD3                           Génie Mathématique - ING1


      Attention
  Remarque importante :
     Si la contrainte d’inégalité était active (i.e., si P ne la satisfaisait pas), il fau-
  drait résoudre le problème complet avec les conditions KKT en considérant le sous-
  ensemble défini par x + y + z = 0 ET x2 + y 2 + z 2 = 1.
     Dans ce cas, on chercherait le minimum sur le cercle d’intersection entre la
  sphère et le plan.




                                             15
~~~

## Page 16

~~~text
Optimisation Non Linéaire - TD3                            Génie Mathématique - ING1


A      Récapitulatif des méthodes

        Type             Méthode
        Sans contraintes CN1 : ∇f = 0
                         CS2 : Hessienne définie positive
        Égalités         Lagrange : ∇x L = 0 et h(x) = 0
                         Ou substitution si possible
        Inégalités       KKT : Stationnarité + Admissibilité + Écart complé-
                         mentaire
                         CS2 : Hessienne positive sur cône tangent

                    Table 1 – Synthèse des méthodes d’optimisation



B      Formules essentielles
Optimisation sans contraintes
    — Coercivité : lim∥x∥→∞ f (x) = +∞
                             ∗
    — Point critique : ∇f (x
                           )2 = 0
    — Hessienne : ∇2 f = ∂x∂i ∂x
                               f
                                 j




Contraintes d’égalité
    — Lagrangien : L(x, λ) = f (x) + λT h(x)
    — Conditions : ∇x L = 0 et h(x) = 0
    — Cône tangent : T (x∗ ) = Ker(∇h(x∗ ))

Contraintes d’inégalité (KKT)
    — Lagrangien : L(x, µ) = f (x) + µj gj (x)
                                        P

    — Stationnarité : ∇f + µj ∇gj = 0
                            P

    — Positivité : µj ≥ 0
    — Écart complémentaire : µj gj (x) = 0
    — Cône tangent : T (x∗ ) = {y : ∇gj (x∗ )T y ≤ 0 si gj (x∗ ) = 0}




                                              16
~~~
