# Claude TD6 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Vt7whVvkVbipgHh0XCTPdQCLyiNNyFhh) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                          CY Tech 2025-2026
                                        ING1 - GM : Probabilités

                                 TD 6 - Vecteurs Aléatoires




Exercice 1 Considérons un vecteur aléatoire (Z1 , Z2 ) =: Z tel que Z1 (Ω) = Z2 (Ω) = {0, 1} et
                           P (Z = (0, 0)) = (1 − p)2 ,    P (Z = (1, 1)) = p2

et
                                 P (Z = (0, 1)) = P (Z = (1, 0)) = p(1 − p)
où p ∈]0, 1[. Montrer que Z1 et Z2 sont indépendantes.

Correction :
  Lois marginales :
     Pour Z1 :
                       P (Z1 = 0)= P (Z = (0, 0)) + P (Z = (0, 1))
                                     = (1 − p)2 + p(1 − p) = (1 − p)[(1 − p) + p]
                                     =1−p


                             P (Z1 = 1)= P (Z = (1, 0)) + P (Z = (1, 1))
                                          = p(1 − p) + p2 = p[(1 − p) + p]
                                          =p

     Donc Z1 ∼ Bernoulli(p).
     Par symétrie, Z2 ∼ Bernoulli(p) également.
     Vérication de l'indépendance :
     Pour montrer l'indépendance, il faut vérier que pour tous i, j ∈ {0, 1} :
                                 P (Z1 = i, Z2 = j) = P (Z1 = i)P (Z2 = j)

     Cas 1 : (i, j) = (0, 0) :
                             P (Z1 = 0, Z2 = 0)= (1 − p)2
                          P (Z1 = 0)P (Z2 = 0)= (1 − p)(1 − p) = (1 − p)2

OK
     Cas 2 : (i, j) = (0, 1) :
                                  P (Z1 = 0, Z2 = 1)= p(1 − p)
                             P (Z1 = 0)P (Z2 = 1)= (1 − p) · p = p(1 − p)

OK
     Cas 3 : (i, j) = (1, 0) :
                                  P (Z1 = 1, Z2 = 0)= p(1 − p)
                             P (Z1 = 1)P (Z2 = 0)= p · (1 − p) = p(1 − p)

OK

                                                     1
~~~

## Page 2

~~~text
     Cas 4 : (i, j) = (1, 1) :
                                       P (Z1 = 1, Z2 = 1)= p2
                                    P (Z1 = 1)P (Z2 = 1)= p · p = p2

OK
     Donc Z1 et Z2 sont indépendantes.


Exercice 2 Soient X et Y deux v.a. t.q. (X, Y ) admette une fonction de densité conjointe f(X,Y )
dénie par
                                 f(X,Y ) (x, y) = c(2x + y)1]2,6[×]0,5[ (x, y)
  1. Que vaut c ?
  2. Trouvez les fonctions de répartitions marginales FX et FY .
  3. Trouver les fonctions de densités marginales fX et fY .
  4. Calculer P (X > 3, Y > 2), P (X > 3) et P (X + Y < 4).
  5. Soient x > 6 et y ∈]0, 5[, calculer F(X,Y ) (x, y) et f(X,Y ) (x, y). En déduire que X et Y ne
     sont pas indépendantes.

Correction :
  1. Calcul de c :
     Pour que f(X,Y ) soit une densité, il faut :
                                         Z
                                               f(X,Y ) (x, y)dxdy = 1
                                          R2


                          Z 6Z 5                           Z 6    5
                                                                y2
                                   c(2x + y)dydx= c       2xy +       dx
                           2     0                    2         2 0
                                                    Z 6           
                                                                25
                                                =c        10x +       dx
                                                      2          2
                                                            25x 6
                                                               
                                                        2
                                                = c 5x +
                                                              2 2
                                                    = c [(180 + 75) − (20 + 25)]
                                                    = c · 210 = 1

     Donc c = 210
               1
                  .
     2. Fonctions de répartition marginales :




                                                       2
~~~

## Page 3

~~~text
Pour x ∈]2, 6[ :
                                   Z x Z +∞
                      FX (x)=                    f(X,Y ) (s, t)dtds
                                    −∞ −∞
                                   Z xZ 5
                                           1
                               =             (2s + t)dtds
                                  2   0 210
                                     Z x            
                                  1               25
                               =            10s +      ds
                                 210 2             2
                                              25s x
                                                
                                  1      2
                               =       5s +
                                 210           2 2
                                                          
                                  1      2    25x
                               =       5x +       − 20 − 25
                                 210           2
                                 5x2 + 12.5x − 45
                               =
                                        210
Pour y ∈]0, 5[ :
                                   Z 6Z y
                                          1
                       FY (y)=              (2x + t)dtdx
                                  2   0 210
                                     Z 6            y
                                  1               t2
                               =          2xt +         dx
                                 210 2            2 0
                                     Z 6
                                                   y2
                                                      
                                  1
                               =           2xy +         dx
                                 210 2              2
                                                  6
                                             xy 2
                                     
                                  1     2
                               =       x y+
                                 210          2 2
                                  1 
                                      36y + 3y 2 − 4y − y 2
                                                            
                               =
                                 210
                                 32y + 2y 2   16y + y 2
                               =            =
                                    210            105
3. Densités marginales :
Pour x ∈]2, 6[ :
                                       Z 5
                                            1
                             fX (x)=           (2x + y)dy
                                        0 210
                                                         5
                                                     y2
                                           
                                        1
                                     =       2xy +
                                       210           2 0
                                                        
                                        1            25
                                     =       10x +
                                       210            2
                                       20x + 25
                                     =           1]2,6[ (x)
                                          420
Pour y ∈]0, 5[ :
                                     Z 6
                                        1
                           fY (y)=         (2x + y)dx
                                   2  210
                                   1  2        6
                                =       x + xy 2
                                  210
                                   1
                                =      [36 + 6y − 4 − 2y]
                                  210
                                  32 + 4y      8+y
                                =           =       1 (y)
                                     210       52.5 ]0,5[

                                             3
~~~

## Page 4

~~~text
   4. Calculs de probabilités :
    P (X > 3, Y > 2) :
                                         Z 6Z 5
                                                   1
                     P (X > 3, Y > 2)=                (2x + y)dydx
                                          3   2 210
                                              Z 6           5
                                          1               y2
                                       =            2xy +       dx
                                         210 3             2 2
                                              Z 6
                                          1
                                       =          [(10x + 12.5) − (4x + 2)] dx
                                         210 3
                                              Z 6
                                          1
                                       =          (6x + 10.5)dx
                                         210 3
                                          1  2            6
                                       =       3x + 10.5x 3
                                         210
                                          1
                                       =     [(108 + 63) − (27 + 31.5)]
                                         210
                                         112.5     15
                                       =        =
                                          210      28
    P (X > 3) :

                           P (X > 3)= 1 − FX (3)
                                          5(9) + 12.5(3) − 45
                                    =1−
                                                  210
                                          45 + 37.5 − 45      37.5
                                    =1−                  =1−
                                                210           210
                                      172.5    23
                                    =       =
                                       210     28
     P (X + Y < 4) :
    Le domaine {(x, y) : x + y < 4, x ∈]2, 6[, y ∈]0, 5[} est : {(x, y) : 2 < x < 4 − y, 0 < y < 2}
(car si x ≥ 2 et x + y < 4, alors y < 2)

                                    Z 2 Z 4−y
                                              1
                   P (X + Y < 4)=               (2x + y)dxdy
                                   0   2    210
                                      Z 2
                                   1       2      4−y
                                =          x + xy 2 dy
                                  210 0
                                      Z 2
                                   1
                                           (4 − y)2 + y(4 − y) − 4 − 2y dy
                                                                        
                                =
                                  210 0
                                      Z 2
                                   1
                                           16 − 8y + y 2 + 4y − y 2 − 4 − 2y dy
                                                                           
                                =
                                  210 0
                                      Z 2
                                   1
                                =         (12 − 6y)dy
                                  210 0
                                   1            2
                                =      12y − 3y 2 0
                                  210
                                   1                12     2
                                =     (24 − 12) =       =
                                  210              210    35
   5. Non-indépendance :
   Pour x > 6 et y ∈]0, 5[ :
                                                            16y + y 2
                                F(X,Y ) (x, y) = FY (y) =
                                                              105

                                                  4
~~~

## Page 5

~~~text
                                                   f(X,Y ) (x, y) = 0
   Si X et Y étaient indépendantes, on aurait :
                            f(X,Y ) (x, y) = fX (x)fY (y) pour tout (x, y)
   Or, le support de f(X,Y ) est ]2, 6[×]0, 5[, qui n'est PAS un produit cartésien de la forme A × B
avec A = support de fX et B = support de fY .
   Donc X et Y ne sont PAS indépendantes.


Exercice 3 Soient X et Y deux v.a. i.i.d. de loi N (µ, σ2 ) où µ = 0 et σ2 = 1. Calculer f(U,V ) (u, v)
où (U, V ) = (X + Y, X − Y ).

Correction :
  Transformation :                  (                         (
                                     U =X +Y                   X = U +V
                                                                     2
                                                            ⇔
                                     V =X −Y                   Y = U −V
                                                                     2
   Jacobien :                       ∂x       ∂x
                                    ∂u       ∂v       1/2 1/2    1 1   1
                          J=        ∂y       ∂y   =            =− − =−
                                    ∂u       ∂v
                                                      1/2 −1/2   4 4   2
   Donc |J| = 12 .
   Densité conjointe de (X, Y ) :
   Comme X et Y sont indépendantes et X, Y ∼ N (0, 1) :
                                f(X,Y ) (x, y)= fX (x)fY (y)
                                                  1      2      1  2
                                              = √ e−x /2 · √ e−y /2
                                                  2π            2π
                                                 1 −(x2 +y2 )/2
                                              =    e
                                                2π
   Densité de (U, V ) :
                                                       
                                             u+v u−v
                     f(U,V ) (u, v)= f(X,Y )      ,       · |J|
                                              2      2
                                                 "                   #!
                                                    u+v 2         u−v 2
                                                               
                                      1        1                            1
                                   =    exp −                +            ·
                                     2π        2      2            2        2

   Calculons l'exposant :
                               2                  2
                                                          (u + v)2 + (u − v)2
                                        
                         u+v                 u−v
                                    +                   =
                          2                   2                    4
                                                          u + 2uv + v 2 + u2 − 2uv + v 2
                                                           2
                                                        =
                                                                         4
                                                          2u2 + 2v 2   u2 + v 2
                                                        =            =
                                                              4            2
   Donc :
                                                     1 −(u2 +v2 )/4 1
                               f(U,V ) (u, v)=         e            ·
                                                    2π                2
                                                     1 −(u2 +v2 )/4
                                                  =    e
                                                    4π
                                                      1      2         1 2
                                                  = √ e−u /4 · √ e−v /4
                                                    2 2π            2 2π

                                                            5
~~~

## Page 6

~~~text
   Ceci montre que U et V sont indépendantes avec :

                                           U ∼ N (0, 2),           V ∼ N (0, 2)



Exercice 4 Soit (X, Y, Z) un vecteur aléatoire de dimension 3 admettant une densité f(X,Y,Z)
dénie par :                                             Q
                                                  1−         w∈{x,y,z} sin(w)
                        f(X,Y,Z) (x, y, z) =                                  1[0,2π[3 (x, y, z)
                                                               8π 3
   Montrer que X, Y, Z sont 2 à 2 indépendants mais pas indépendants.

Correction :
  Densités marginales :
   Calculons la densité de X :
                                        Z 2π Z 2π
                                            1 − sin(x) sin(y) sin(z)
                          fX (x)=                                     dydz
                                     0  0              8π 3
                                       Z 2π Z 2π
                                     1
                                   = 3           [1 − sin(x) sin(y) sin(z)]dydz
                                    8π 0     0

   Or          sin(y)dy = 0 et          1dy = 2π , donc :
        R 2π                     R 2π
          0                       0

                                                 1
                                        fX (x)=      [2π · 2π − sin(x) · 0]
                                                8π 3
                                                4π 2      1
                                               = 3 =        1     (x)
                                                8π      2π [0,2π[
   Par symétrie : fY (y) = fZ (z) = 2π
                                     1
                                       1[0,2π[ .
   Densité conjointe de (X, Y ) :
                                                  Z 2π
                                                          1 − sin(x) sin(y) sin(z)
                             f(X,Y ) (x, y)=                                       dz
                                                    0              8π 3
                                                1
                                              =     [2π − sin(x) sin(y) · 0]
                                               8π 3
                                                1
                                              = 2 1[0,2π[2 (x, y)
                                               4π
   Vérication de l'indépendance 2 à 2 :
                                                     1   1   1
                                 fX (x)fY (y)=         ·   = 2 = f(X,Y ) (x, y)
                                                    2π 2π   4π
   Donc X et Y sont indépendantes. Par symétrie, toutes les paires sont indépendantes.
   Non-indépendance mutuelle :
   Si X, Y, Z étaient mutuellement indépendantes :
                                                                                     1
                                 f(X,Y,Z) (x, y, z) = fX (x)fY (y)fZ (z) =
                                                                                    8π 3
   Or :
                                                        1 − sin(x) sin(y) sin(z)    1
                           f(X,Y,Z) (x, y, z) =                      3
                                                                                 ̸= 3
                                                                 8π                8π
(sauf si sin(x) sin(y) sin(z) = 0)
    Donc X, Y, Z ne sont PAS mutuellement indépendantes.

                                                               6
~~~

## Page 7

~~~text
Exercice 5 Soient X et Y deux variables aléatoires réelles indépendantes avec X de loi normale
centrée réduite et Y de loi Gamma
                             √
                                   de paramètre α = n/2 et β = 1/2 avec n ∈ N∗ .
   Quelle est la loi de Z = √nXY
                                 ?

Correction :
   On a X ∼ N (0, 1)√ et Y ∼ γ(n/2, 1/2) = χ2n .
   La variable Z = √nXY
                         suit la loi de Student à n degrés de liberté, notée tn .
   Démonstration :
   La densité de la loi de Student à n degrés de liberté est :
                                                          − n+1
                                          Γ n+1
                                                 
                                              2        z2     2
                                fZ (z) = √      n
                                                   1+
                                           nπΓ 2       n

    Cette loi joue un rôle fondamental en statistique pour les tests d'hypothèses lorsque la variance
est inconnue.




                                                 7
~~~
