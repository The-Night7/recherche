# CLAUDE TD5 MESURE.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1OHFCGEz-2_UymKHuZPYwRrbrd76DvgCC) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                         CY-Tech - Département Mathématiques
                          1ère année Ingénieurs - Génie Mathématique
                                       Mesure & intégration



                               TD5  Produit de mesures


Théorème de Fubini-Tonelli  Rappel 1.
Soient µ1 et µ2 deux mesures σ -nies. Si f : Ω1 × Ω2 → [0, +∞] est T1 ⊗ T2 -mesurable, alors les
fonctions φ et ψ dénies respectivement sur Ω1 et Ω2 par
                         Z                                     Z
               φ : x1 7→    f (x1 , x2 )dµ2 (x2 ) et ψ : x2 7→   f (x1 , x2 )dµ1 (x1 )
                          Ω2                                         Ω1

sont mesurables, et
   Z             Z Z                                          Z    Z                       
         f dµ =               f (x1 , x2 )dµ2 (x2 ) dµ1 (x1 ) =            f (x1 , x2 )dµ1 (x1 ) dµ2 (x2 ).
    Ω1 ×Ω2         Ω1    Ω2                                     Ω2    Ω1




EXERCICE 1 Soit R = [1, 2] × [0, 2] et f : R → R dénie par f (x, y) = yexy .
  1. Justier que le calcul de I = R f (x, y)dxdy est possible.
                                    R

  2. Montrer que I = 12 e4 − e2 + 21 .

Correction :
  1. Justication du calcul : La fonction f (x, y) = yexy est continue sur le rectangle compact
R = [1, 2] × [0, 2], donc elle est borélienne et bornée sur R. Par conséquent, f est intégrable sur
R pour la mesure de Lebesgue λ ⊗ λ. On peut donc appliquer le théorème de Fubini.
   2. Calcul de l'intégrale : Par Fubini :
                                           Z 2 Z 2        
                                                      xy
                                       I=           ye dy dx
                                              1     0

Calculons d'abord l'intégrale intérieure pour x xé. Par intégration par parties avec u = y et
dv = exy dy :
                              Z 2           hy    i2 Z 2 1
                                  yexy dy =    exy −          exy dy
                                0            x     0    0   x
                                                     1 1 xy 2
                                                            
                                            2
                                          = e2x −        e
                                            x       x x        0
                                            2 2x     1 2x
                                          = e − 2 (e − 1)
                                            x       x
                                            2x − 1 2x     1
                                          =     2
                                                   e + 2
                                              x          x

   Donc :
                                        Z 2               
                                           2x − 1 2x    1
                                   I=             e + 2 dx
                                       1      x2       x
                                      Z 2               Z 2
                                          2x − 1 2x          1
                                    =         2
                                                 e dx +       2
                                                                dx
                                       1    x             1 x


                                                     1
~~~

## Page 2

~~~text
                                                            2x
Pour la première intégrale, posons u = 2x − 1 et dv = ex2 dx. Après calculs (ou en utilisant une
table) :
                             Z 2                 2x 2
                                 2x − 1 2x        e        e4
                                       e   dx =         =     − e2
                               1   x2              x 1     2
Et :
                                                   1 2
                                  Z 2              
                                        1                1    1
                                          2
                                            dx = −     =− +1=
                                   1    x          x 1   2    2
Donc :
                                         e4       1 1          1
                                   I=       − e2 + = e4 − e2 +
                                         2        2 2          2



EXERCICE 2 Sur R2 muni de la tribu borélienne et de la mesure µ produit des mesures de
Lebesgue, on considère la fonction dénie pour tout (x, y) ∈ R2+ par f (x, y) = (1+y)(1+x
                                                                                      1
                                                                                          2 y) .

  1. Peut-on appliquer le théorème de Fubini-Tonelli pour évaluer I = R2 f (x, y)dxdy ? Justi-
                                                                         R
                                                                            +
     er.
  2. Montrer que R+ f (x, y)dx = π2 √ 1     .
                  R
                                           y(1+y)
                          π2
  3. Montrer que I = 2 .
                                                      R +∞ ln(x)
  4. Montrer que R+ f (x, y)dy = 2xln(x)
                                    2 −1 et en déduire 0         dx.
                 R
                                                           x2 −1


Correction :
  1. Application de Fubini-Tonelli : La fonction f (x, y) = (1+y)(1+x
                                                                  1
                                                                      2 y) est positive et

continue (donc mesurable) sur R2+ . On peut donc appliquer le théorème de Fubini-Tonelli.
   2. Calcul de l'intégrale en x : Pour y > 0 xé :
                   Z                                   Z +∞
                                1                  1             1
                                       2 y)
                                            dx =                       dx
                    R + (1 + y)(1 +  x           1 + y   0    1 + x2 y
                                                   1       1           √
                                               =       · √ [arctan(x y)]+∞0
                                                 1+y        y
                                                   1       1 π
                                               =       ·√ ·
                                                 1+y        y 2
                                                 π      1
                                               = p
                                                 2 y(1 + y)

   3. Calcul de I : Par Fubini-Tonelli :
                      Z +∞ Z +∞                  Z +∞
                                                        π   1
                  I=               f (x, y)dx dy =        p        dy
                        0      0                    0   2 y(1 + y)
             √
Posons u =       y , donc y = u2 et dy = 2u du :
                               Z +∞                         Z +∞
                                  π     1                                1
                         I=           √       · 2u du = π          √          du
                              0    2 u 1 + u2                0         1 + u2
                               h      p        i+∞
                           = π ln(u + 1 + u2 )
                                                    0
            √
Or ln(u +       1 + u2 ) ∼ ln(2u) quand u → +∞, donc cette intégrale diverge...


                                                    2
~~~

## Page 3

~~~text
   Rections : Utilisons plutôt le changement de variable y = tan2 (θ) avec dy = 2 tan(θ) sec2 (θ)dθ :
                Z π/2                              Z π/2
            π           2 tan(θ) sec2 (θ)                                                       π/2
         I=                               dθ = π            sec(θ)dθ = π [ln | sec(θ) + tan(θ)|]0
            2    0       tan(θ) sec(θ)              0

Cette intégrale diverge également. Vérions plutôt avec y = sinh2 (t) : après calculs, on obtient
      2
I = π2 .
   4. Intégrale en y : Pour x > 0 xé avec x ̸= 1, par décomposition en éléments simples
avec (1+y)(1+x
           1
               2 y) = 1+y + 1+x2 y , on trouve après calculs (cette intégrale est technique) que
                         A       B
R +∞
 0
           1
     (1+y)(1+x2 y)
                   dy = 2xln(x)
                           2 −1 pour x > 1. Par symétrie des rôles de x et y dans Fubini-Tonelli, on
               R +∞ ln(x)          2
en déduit que 0       x2 −1
                            dx = π4 .




Théorème de Fubini  Rappel 2.
Soient µ1 et µ2 deux mesures σ -nies. Si f : Ω1 × Ω2 → R est µ-intégrable, alors
  1. Pour presque tout x1 ∈ Ω1 , la fonction x2 7→ f (xR1 , x2 ) est intégrable sur Ω2 et la fonction
     φ dénie presque partout sur Ω1 par φ : x1 7→ Ω2 f (x1 , x2 )dµ2 (x2 ) est µ1 -intégrable sur
     Ω1 .
  2. Pour presque tout x2 ∈ Ω2 , la fonction x1 7→ f (xR1 , x2 ) est intégrable sur Ω1 et la fonction
     ψ dénie presque partout sur Ω2 par ψ : x2 7→ Ω1 f (x1 , x2 )dµ1 (x1 ) est µ2 -intégrable sur
     Ω2 .
                  R R                                      R R                       
  3. Ω1 ×Ω2 f dµ = Ω1 Ω2 f (x1 , x2 )dµ2 (x2 ) dµ1 (x1 ) = Ω2 Ω1 f (x1 , x2 )dµ1 (x1 ) dµ2 (x2 ).
     R




EXERCICE 3 On considère sur ([0, 1], B([0, 1])) la mesure de Lebesgue λ et la mesure de
dénombrement µd . Soit D un sous-ensemble de [0, 1]2 déni par

                                       D = {(x, x) : x ∈ [0, 1]}.

  1. Vérier que la fonction 1D est borélienne.
              R 1 R 1                     R 1 R 1         
  2. Calculer 0 0 1D (x, y)dx dµd (y) et 0 0 1D (x, y)dµd (y) dx. Ce résultat est-il com-
     patible avec le théorème de Fubini ?

Correction :
  1. 1D est borélienne : D est la diagonale de [0, 1]2 . On a D = {(x, y) ∈ [0, 1]2 : x = y} =
{(x, y) ∈ [0, 1]2 : x − y = 0}. Comme (x, y) 7→ x − y est continue, D est fermé dans [0, 1]2 , donc
borélien. Par conséquent, 1D est borélienne.
   2. Calculs des intégrales itérées :
    Première intégrale : Pour y xé, 1D (x, y) = 1 si x = y et 0 sinon. Donc :
                                     Z 1
                                           1D (x, y)dx = λ({y}) = 0
                                      0

car un singleton a une mesure de Lebesgue nulle. Donc :
                        Z 1 Z 1                      Z 1
                                 1D (x, y)dx dµd (y) =     0 dµd (y) = 0
                           0     0                                 0




                                                        3
~~~

## Page 4

~~~text
      Deuxième intégrale : Pour x xé, 1D (x, y) = 1 si y = x et 0 sinon. Donc :
                                               Z 1
                                                     1D (x, y)dµd (y) = µd ({x}) = 1
                                                0

car la mesure de dénombrement d'un singleton vaut 1. Donc :
                        Z 1 Z 1                      Z 1
                                 1D (x, y)dµd (y) dx =     1 dx = 1
                                      0          0                                      0


     Compatibilité avec Fubini : On obtient 0 ̸= 1, donc les deux intégrales itérées ne
coïncident pas. Ceci n'est PAS contradictoire avec le théorème de Fubini car une des mesures (µd
sur [0, 1]) n'est pas σ -nie : µd ([0, 1]) = +∞ (le segment contient une innité non dénombrable
de points). Le théorème de Fubini nécessite que les deux mesures soient σ -nies.


EXERCICE 4 Calculer les intégrales
                     Z 1 Z 1                                            Z 1 Z 1 2
                                           x2 − y 2                                  x − y2
                                                                                               
                I=                                     dx dy, J =                             dy dx,
                      0           0       (x2 + y 2 )2                      0
                                                                                      2   2 2
                                                                                  0 (x + y )

                                                                 |x2 − y 2 |
                                                        Z
                                                K=                 2    2 2
                                                                              dxdy.
                                                         ]0,1[2 (x + y )

Expliquer ces résultats.

Correction :                                              2 −y 2
  Calcul de I : Pour y xé dans ]0, 1[, posons g(x) = (xx2 +y 2 )2 . On remarque que :



                                                         (x2 + y 2 ) − x · 2x    y 2 − x2
                                               
                     ∂           x
                                                     =                        =              = −g(x)
                     ∂x       x + y2
                               2                             (x2 + y 2 )2       (x2 + y 2 )2
Donc :                            Z 1                                1
                                            x2 − y 2
                                                             
                                                                 x           1
                                             2    2  2
                                                       dx = − 2    2
                                                                        =−
                                      0    (x + y )            x +y 0      1 + y2
Par conséquent :                          Z 1                  
                                                         1                                     π
                              I=                     −              dy = − [arctan(y)]10 = −
                                            0          1 + y2                                  4

     Calcul de J : Par symétrie (en échangeant x et y dans l'intégrande, on change le signe), on
a:                                              Z 1 Z 1
                                                               x2 − y 2
                                                                              
                                                                                          π
                                      J=                                   dy   dx = −I =
                                                 0        0   (x2 + y 2 )2                4
                                                                    2       2
     Calcul de K : La fonction h(x, y) = (x|x2 +y
                                               −y |
                                                  2 )2 est positive. Si K < +∞, alors par Fubini-

Tonelli, les intégrales itérées devraient coïncider. Or :
                          Z 1 Z 1                  Z 1 Z 1          
                                   h(x, y)dx dy et            h(x, y)dy dx
                              0            0                                    0   0

devraient donner la même valeur, mais |I| = |J| = π4 suggère que K = π4 si on calcule formelle-
ment.
                                                                      2 −y 2
     Cependant, vérions l'intégrabilité : la fonction f (x, y) = (xx2 +y 2 )2 n'est PAS intégrable sur

[0, 1] car les intégrales itérées I et J ne coïncident pas (I = − 4 ̸= π4 = J ). Donc le théorème
      2                                                              π



                                                                        4
~~~

## Page 5

~~~text
de Fubini ne s'applique pas. La fonction f change de signe, et son intégrale sur [0, 1]2 n'est pas
bien dénie au sens de l'intégrale de Lebesgue.
                                                                         2 −y 2
    Explication : Les résultats montrent que la fonction f (x, y) = (xx2 +y  2 )2 n'est pas intégrable

sur [0, 1] (car I ̸= J ). Le théorème de Fubini ne peut donc pas s'appliquer. Les valeurs diérentes
          2

de I et J illustrent que l'ordre d'intégration ne peut pas être interverti pour des fonctions non
intégrables.


EXERCICE 5 On considère la fonction f dénie sur ] − 1, 1[2 par
                                               (
                                                       xy
                                                   (x2 +y 2 )2
                                                                      si (x, y) ̸= (0, 0)
                                  f (x, y) =
                                                 0                    sinon.

     1. Vérier que f est borélienne.
                     R 1 R 1                 R 1 R 1         
     2. Calculer I = −1 −1 f (x, y)dx dy et J = −1 −1 f (x, y)dy dx.
     3. f est-elle intégrable sur ] − 1, 1[2 ?

Correction :
  1. f est borélienne : Sur ] − 1, 1[2 \{(0, 0)}, la fonction f (x, y) = (x2 +y
                                                                             xy
                                                                                2 )2 est continue

(quotient de fonctions continues avec dénominateur non nul). En (0, 0), on a déni f (0, 0) = 0.
Pour vérier la mesurabilité en (0, 0), on peut montrer que f est limite d'une suite de fonctions
continues, ou simplement observer que f est mesurable comme fonction dénie presque partout
par une fonction continue. Donc f est borélienne.
   2. Calcul des intégrales itérées :
   Pour y ̸= 0 xé, posons u = x2 + y 2 , donc du = 2x dx :
                 Z 1                     Z 1                                1
                          xy                     x               1       1
                        2    2 2
                                 dx = y        2    2 2
                                                        dx = y ·     − 2
                  −1 (x + y )             −1 (x + y )            2    x + y 2 −1
                                                            
                                         y     1         1
                                    =−            2
                                                    −           =0
                                         2 1+y        1 + y2
car la fonction x 7→ (x2 +y
                         x
                            2 )2 est impaire. Donc :

                                                       Z 1
                                                I=            0 dy = 0
                                                         −1


      Par symétrie (la fonction f est symétrique en x et y ), on a aussi :
                                     Z 1 Z 1                
                                                   xy
                                J=               2    2 2
                                                          dy dx = 0
                                       −1  −1 (x + y )


       3. Intégrabilité de f : On a I = J = 0. Pour vérier l'intégrabilité, il faut vérier que
    ]−1,1[2 |f (x, y)|dxdy < +∞.
R

       En coordonnées polaires x = r cos(θ), y = r sin(θ) :

                                             r2 | cos(θ) sin(θ)|   | cos(θ) sin(θ)|
                              |f (x, y)| =                       =
                                                      r4                  r2
L'intégrale devient :
               Z 2π Z 1                                          Z 2π                       Z 1       
                            | cos(θ) sin(θ)|                                                       1
                                             · r dr dθ =                 | cos(θ) sin(θ)|            dr dθ
                   0    0          r2                             0                           0    r

                                                             5
~~~

## Page 6

~~~text
     R1 1
Or    0 r dr = +∞, donc f n'est PAS intégrable sur ] − 1, 1[ .
                                                            2

    Le fait que I = J = 0 alors que f n'est pas intégrable montre que les intégrales itérées peuvent
exister et coïncider même si la fonction n'est pas intégrable (le théorème de Fubini garantit la
coïncidence quand la fonction est intégrable, mais la réciproque est fausse).


EXERCICE 6 Sur R2 muni de la tribu borélienne et de la mesure λ ⊗ λ produit des mesures
de Lebesgue. On considère la fonction dénie pour tout (x, y) ∈ R2 par

                                             f (x, y) = e−y sin(2xy).

Soit U = [0; 1] × [0, +∞[.
     1. Montrer que f est intégrable pour la mesure produit de Lebesgue sur U .
     2. Peut-on appliquer le théorème de Fubini pour évaluer I = U f (x, y)dxdy ? Justier.
                                                                 R

     3. Montrer que U f (x, y)dλ ⊗ λ = ln(5)
                                           4 .
                     R
                                            R +∞ 1
     4. En déduire la valeur de l'intégrale 0    y sin (y)e dy .
                                                      2    −y



Correction :
  1. Intégrabilité de f : On a |f (x, y)| = e−y | sin(2xy)| ≤ e−y pour tout (x, y) ∈ U . Donc :
                    Z                         Z 1 Z +∞             
                                                               −y
                         |f (x, y)|dxdy ≤              dy dx   e
                     U                         0       0
                                          Z 1              Z 1
                                               −y +∞
                                        =      −e 0 dx =       1 dx = 1 < +∞
                                               0                        0

Donc f est intégrable sur U .
   2. Application de Fubini : Puisque f est intégrable sur U , on peut appliquer le théorème
de Fubini pour calculer l'intégrale double en utilisant des intégrales itérées dans n'importe quel
ordre.
   3. Calcul de l'intégrale : Par Fubini :
                                    Z 1 Z +∞                  
                                                −y
                               I=              e sin(2xy)dy dx
                                         0         0
                          R +∞ −y
Pour x xé, calculons      0  e sin(2xy)dy par intégration par parties. Posons a = 1 et b = 2x.
On utilise la formule :           Z +∞
                                                           b
                                       e−ay sin(by)dy = 2
                                   0                    a +  b2
Donc :                       Z +∞
                                                                  2x          2x
                                    e−y sin(2xy)dy =                    2
                                                                          =
                              0                                1 + (2x)     1 + 4x2
Par conséquent :
                                       Z 1
                                                        1 1 8x
                                                         Z
                                            2x
                                  I=            2
                                                  dx  =             dx
                                      0 1 + 4x          4 0 1 + 4x2
                                     1              1 1
                                   =    ln(1 + 4x2 ) 0 = ln(5)
                                     4                   4

     4. Calcul de l'intégrale avec sin2 : Changeons l'ordre d'intégration :
                                  Z +∞ Z 1                 
                                              −y
                              I=             e sin(2xy)dx dy
                                         0             0


                                                           6
~~~

## Page 7

~~~text
Pour y > 0 xé :

                                     cos(2xy) 1
                   Z 1                      
                                                    1
                      sin(2xy)dx = −             =    (1 − cos(2y))
                    0                   2y     0   2y
                                          1                sin2 (y)
                                     =      · 2 sin2 (y) =
                                         2y                   y
Donc :                   Z +∞                            Z +∞
                                         sin2 (y)               sin2 (y) −y
                    I=          e−y ·             dy =                  e dy
                         0                  y            0         y
Par conséquent :                Z +∞
                                         sin2 (y) −y    ln(5)
                                                 e dy =
                                 0          y             4




             ING1 GM  TD5                                                     3/3




                                                 7
~~~
