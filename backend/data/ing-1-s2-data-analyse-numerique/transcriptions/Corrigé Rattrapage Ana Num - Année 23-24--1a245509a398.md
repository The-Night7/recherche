# Corrigé Rattrapage Ana Num - Année 23-24.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1TJMiShgOgwsK_i1E76_ET7w0IYu86RUB) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                            Corrigé Analyse Numérique
                             Session 2 - Année 23-24
1. Exercice 1 :




                      f(x n )
   1) x n+1 = x n -              .
                      f'(x n )




                                     f(x n ) - f(x n-1 )
   2) On remplace f'(x n ) par                               , et on obtient :
                                     x n - x n-1
                                 f(x n )         x n (f(x n ) - f(x n-1 )) - f(x n )(x n - x n-1 )
               x n+1 = x n -                   =
                             f(x n )-f(x n-1 )                  f(x n ) - f(x n-1 )
                                      x n -x n-1
                                                       x n-1 f(x n ) - x n f(x n-1 )
                                         x n+1 =                                       .
                                                           f(x n ) - f(x n-1 )
     Il s'agit de la méthode de la sécante.




   3) La méthode du point fixe est en général d'ordre 1, celle de Newton d'ordre 2
      (quadratique).
      Par conséquent, la méthode de la sécante sera plus rapide que celle du point fixe et
      moins rapide que celle de Newton, dans le cas général.




   4) f(0) = - 1 et f(1) = 1, donc :
                                             x 0 f( x 1 ) - x 1 f ( x 0 )       0+1 1
                                     x2 =                                   =      = .
                                                   f(x 1 ) - f(x 0 )            1+1 2
~~~

## Page 2

~~~text
                 1       3
     f(x 2 ) = f 2 = - 8 , donc :
                                                                        3   3
                                    x 1 f( x 2 ) - x 2 f ( x 1 )       -8 + 8
                             x3 =                                  =            = 0.
                                       f(x 2 ) - f(x 1 )                3
                                                                       -8 - 1
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

2. Exercice 2 :




   1) A est symétrique, donc diagonlisable avec valeurs propres réelles. En raisonnant sur
      les disques de Gershgorin, par exemple, on voit que ses valeurs propres se trouvent
      dans le disque ouvert de centre 2 et de rayon 2. Par conséquent, elles sont
      strictement positives.
      A est symétrique définie positive, donc possède une factorisation de Cholesky.
                                                    2 -1
   2) Les 2 sous-matrices principales (2) et             sont inversibles, donc A possède
                                                    -1 2
     une factorisation LU.



                                                                                       1 0 0
   3) On commence par annuler les coefs de la 1ère colonne, en multipliant par L 1 = 1 / 2 1 0
                                                                                       0 0 1
              2 -1 0                                                               1 0 0
   L 1 A = 0 3 / 2 -1 . On passe à la 2ème colonne, en multipliant par : L 2 = 0 1 0
              0 -1 2                                                               0 2/3 1
                2 -1      0
   L 2 L 1 A = 0 3 / 2 -1 = U.
                0 0 4/3
                                                   1     0 0
   Pour déterminer L, il faut inverser L 2 L 1 = 1 / 2 1 0 .
                                                 1/3 2/3 1
                                            1     0    0
                                  -1
   On obtient alors L = (L 2 L 1 ) = -1 / 2       1    0 .
                                            0   -2 / 3 1
~~~

## Page 3

~~~text
   4) On cherche à écrire A = LU = L D DL T = LDL T .
      L a des coefs diagonaux égaux à 1, donc les coefs de D sont les coefs diagonaux de
      U.
     On vérifie, que l'on a bien : A = LDL T , avec :
                              1      0    0          2 0     0
                        L = -1 / 2   1    0 , et D = 0 3 / 2 0 .
                              0    -2 / 3 1          0 0 4/3
                                     2      0      0
     On en déduit :     D=       0         3/2     0       .

                                 0          0      4/3




   5) Etant donné que     D est diagonale, elle est égale à sa transposée, on peut donc
      écrire :
                                                               T                T
                      A=L D              DL T = L D        D LT = L      D L   D .
     Il suffit alors de poser S = L       D pour obtenir la décomposition de Cholesky
     recherchée.
                                                       2           0     0
                           S=L D= -                2/2             3/2   0
                                                   0       -       2/3   4/3
                             T
     Et on a bien : A = SS .

≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

3. Exercice 3 :
~~~

## Page 4

~~~text
                                                 x+z = 2                 z = 2-x
1) On doit résoudre le système linéaire                             ⟺              .
                                                 -x + y = 3              y = 3+x
                                                        x
  L'ensemble des solutions est donc S =                3+x , x ∈ R .
                                                       2-x
2) On cherche, parmi ces solutions, celle qui a la plus petite norme eucildienne. Cela
   revient à minimiser le carré de cette norme, donc à minimiser :
                 x 2 + (3 + x) 2 + (2 - x) 2 = 3x 2 + 2x + 13 = ax 2 + bx + c.
                                                  -b -1
  On sait que le minimum est atteint pour x =         =     .
                                                   2a    3
                                              -1 / 3
  La solution recherchée est donc : x 0 = 8 / 3 .
                                               7/3




               2 -1
3) AA T =           .
               -1 2
                                                                          1     1
  Elle a pour valeurs propres 3 et 1, et pour vecteurs propres               et   . En
                                                                          -1    1
                                      1       1 1
  normalisant, on obtient : U =                    .
                                          2   -1 1
  Les valeurs singulières sont 𝜎 1 =           3 et 𝜎 2 = 1, et par suite :

                                      𝛴=          3 0 0
                                                 0 1 0
  On va utiliser les valeurs singulières pour déterminer la matrice V.

         1                     1 -1                            2
               T       1              1       1        1
  v1 =        A u1 =           0 1               =             -1
         𝜎1                3              2   -1           6
                               1 0                             1
~~~

## Page 5

~~~text
           1                     1 -1                                       0
                    T        1             1       1                1
  v2 =          A       u2 = 1   0 1                 =                      1 .
           𝜎2                                  2   1                    2
                                 1 0                                        1
                                                                2 -1 1
                                                                                                T
  Le 3ème vecteur doit être recherché dans le noyau de A A = -1 1 0 .
                                                                1 0 1
                             2x - y + z = 0
                                                   y =x
                             -x + y     =0 ⟺               .
                                                   z = -x
                             x+z        =0
                           1                                         1
                                                                 1
  On peut donc prendre 1 et le normaliser, ce qui donne : v 3 =      1 .
                                                                   3
                          -1                                         -1
  Finalement :
                                                               2        0         2
                                                   1
                                          V=                   -1           3     2 .
                                                       6
                                                               1            3 -   2




               1/     3 0
4) 𝛴 † =            0   1 , et
                    0   0
                                     2     0                   2    1/        3 0
    †           †        T   1                                                          1       1 -1
  A = V𝛴 U =                         -1        3               2            0   1                    .
                                 6                                                          2   1 1
                                     1         3 -             2            0   0
  On obtient bien :
                                                       1 / 3 -1 / 3
                                                           †
                                                   A = 1/3 2/3 .
                                                       2/3 1/3




5) Le vecteur x 0 peut être obtenu directement grâce à A † , par :
~~~

## Page 6

~~~text
                                    1 / 3 -1 / 3                -1 / 3
                                 †                      2
                         x0 = A b = 1 / 3 2 / 3           =     8/3 .
                                                        3
                                    2/3 1/3                     7/3
 ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

4. Exercice 4 :




   1) A est inversible, donc le système linéaire Ax = b possède une unique solution.
   2) La formule de récurrence de Gauss-Seidel est donnée par :
                              x n+1 = (D - E) -1 Fx n + (D - E) -1 b
     où D, -E et -F représentent, respectivement, les parties diagonales, triangulaire
     inférieure et supérieure de A.
                               1 0 0                         1   0 0
                                                          -1
     Dans notre cas : D - E = 2 2 0 , et par suite (D - E) = -1 1 / 2 0 .
                               3 0 1                         -3 0 1
                                     1    0 0 0 -1 -3          0 -1 -3
                               -1
     On en déduit : B = (D - E) F = -1 1 / 2 0 0 0 -2 = 0 1 2 .
                                     -3 0 1 0 0 0              0 3 9
                            1     0 0 0        0
                     -1
     Et C = (D - E) b = -1 1 / 2 0 4 = 2 .
                            -3 0 1 5           5
~~~

## Page 7

~~~text
                     0                         0
3) A partir de x 0 = 0 , on obtient x 1 = C = 2 , et ensuite :
                     0                         5
                                                  -17
                                 x 2 = Bx1 + C = 14 .
                                                   56
4) La convergence de la méthode dépend du rayon spectral de B. Calculons son
   polynôme caractéristique :
                  -x -1  -3
      𝜒 B (x) =   0 1-x 2           = - x((1 - x)(9 - x) - 6) = - x x 2 - 10x + 3
                  0   3 9-x
  Les valeurs propres de B sont donc 0, 5 -    22 et 5 +   22.
                  𝜌(B) = 5 +   22 > 1    ⟹ la méthode est divergente.
~~~
