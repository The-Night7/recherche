# Corrigé Analyse Numérique mai 2024.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1rKTvzhQRehj_Yi7OYpIBk4IhckXx23ka) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                   Corrigé Analyse Numérique mai 2024
1. Exercice 1




1. f'(x) = 3x 2 + 1 > 0 ⟹ f strictement croissante. f(0) = - 1 < 0, f(1) = 1 > 0.
Donc f possède une racine unique 𝛼 ∈ ]0, 1[.




2. g est continue et est à valeurs dans ]0, 1], donc si (x n ) n converge, ce sera vers un point
fixe de g dans ]0, 1].
                      1
Or g(x) = x ⟺               = x ⟺ f(x) = 0. 𝛼 est donc l'unique point fixe de g dans ]0, 1].
                   1 + x2
Conclusion : lim x n = 𝛼.
La construction de cette suite est une application de la méthode du point fixe pour déterminer
un zéro de f.




3. En appliquant l'inégalité des accroissements finis à g entre x n et 𝛼, on obtient :
                                   |g(x n ) - g(𝛼)| ⩽ C|x n - 𝛼|
g(x n ) = x n+1 et g(𝛼) = 𝛼, d'où le 1er résultat. Le 2ème s'obtient par récurrence :
     • |x 0 - 𝛼| ⩽ 1 = C 0 .
     • Si on suppose |x n - 𝛼| ⩽ C n pour un n fixé, alors :
                                     |x n+1 - 𝛼| ⩽ C|x n - 𝛼| ⩽ C n+1 .




4. |x 10 - 𝛼| ⩽ C 10 ≃ 0.01336 et            |x 11 - 𝛼| ⩽ C 11 ≃ 0.00858 < 0.01
On est donc sûr qu'à partir de la 11ème itération, x n donne une valeur approchée à moins de
~~~

## Page 2

~~~text
10 -2 près.




5. La formule de récurrence de la méthode de Newton est :
                                            f(z n )        z n3 + z n - 1
                            z n+1 = z n -    = zn -
                                    f'(z n )        3z n2 + 1
                                   -1                       1+1-1 3
                 z0 = 0 ⟹ z1 = 0 -     = 1 ⟹ z2 = 1 -             = .
                                   1                          3+1  4




6. La méthode de Newton est quadratique signifie que :
                                    |z n+1 - 𝛼| ⩽ K|z n - 𝛼| 2 .
Une récurrence immédiate permet d'en déduire :
                                                               n
                                    |z n - 𝛼| ⩽ K n |z 0 - 𝛼| 2 .
La convergence va être beaucoup plus rapide, mais l'effet quadratique dépendra de la
position de z 0 et de la valeur de K.
Toutefois, pour n = 10, on a 2 10 = 1024 et 𝛼 n'est pas trop proche de 0 ni de 1, donc
                                                                            10
|z 0 - 𝛼| ne sera pas trop proche de 1. Et par conséquent |z 0 - 𝛼| 2 sera beaucoup
beaucoup plus petit que 10 -2 .
On peut donc prévoir que la précision souhaitée sera atteinte beaucoup plus rapidement
avec la méthode de Newton à moins que K soit très grand.
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

2. Exercice 2




              10 6 0
1. M -1 =            et donc 𝜅 1 (M) = 𝜅 2 (M) = 𝜅 ∞ (M) = 1 × 10 6 = 10 6 .
               0 1
~~~

## Page 3

~~~text
                                             1          2
2. On trouve très facilement x 1 =             et x 2 =   .
                                             1          1




        1              ‖𝛿x‖         1             ‖𝛿b‖             10 -6
3. 𝛿x =           ⟹             =        , et            =                   ≃ 10 -6 .
        0              ‖x 1 ‖                      ‖b‖
                                        2                       1 + 10 -12
                                        ‖𝛿x‖                 ‖𝛿b‖
On sait que l'on devrait avoir :                 ⩽ 𝜅2 (M)          et on vérifie bien que :
                                        ‖x 1 ‖               ‖b‖
 1
         ⩽ 10 6 × 10 -6 = 1.
     2


≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

3. Exercice 3




                                                         1 0
1. La 2ème sous-matrice principale de A,                     , n'est pas inversible, donc A ne possède
                                                         2 0
pas de factorisation LU.
Il suffit de permuter les lignes 1 et 3, ou bien les lignes 2 et 3 pour obtenir une matrice
possédant une factorisation LU.
                         0 0 1                                1 0 0
On peut donc prendre P = 0 1 0                    ou bien P = 0 0 1 .
                         1 0 0                                0 1 0
~~~

## Page 4

~~~text
                                    0 0 1                     3 3 1
2. Prenons la première solution P = 0 1 0 , on a alors : PA = 2 0 2 dont on va
                                    1 0 0                     1 0 1
faire la factorisation LU.
                                                                                  1    0 0
On commence par annuler les coefs de la 1ère colonne, en multipliant par L 1 = -2 / 3 1 0
                                                                                -1 / 3 0 1
           3 3    1                                                           1     0   0
L 1 A = 0 -2 4 / 3 . On passe à la 2ème colonne, en multipliant par : L 2 = 0       1   0
           0 -1 2 / 3                                                         0 -1 / 2 1
             3 3     1
L 2 L 1 A = 0 -2 4 / 3 = U.
             0 0     0
                                                1      0    0
Pour déterminer L, il faut inverser L 2 L 1 = -2 / 3   1    0 .
                                                0    -1 / 2 1
                                        1    0 0
                               -1
On obtient alors L = (L 2 L 1 ) = 2 / 3 1 0 . Et on peut conclure que : PA = LU.
                                     1/3 1/2 1




                                      2
3. On voit immédiatement que C 1 =        C 2 + C 3 et donc Im(A) = Vect{ C 2 , C 3 }. On peut
                                      3
                                            1                 1
ensuite pour simplifier remplacer C 2 par C 2 et C 3 par C 3 - C 2 , ce qui nou donne :
                                        3                     3
                                                   0     1
                                 Im(A) = Vect 0 , 2 .
                                                   1     0
b ∉ Im(A), donc le système Ax = b n'a pas de solution.



                                0      1       y
4. On peut déjà écrire : b' = x 0 + y 2 = 2y , et b' est le projeté orthogonal de b sur
                                1      0       x
Im(A). Donc b' - b est orthogonal à Im(A) et donc aux deux vecteurs qui l'engendrent.
~~~

## Page 5

~~~text
         y-2
                                       x-1 = 0                       x=1
b' - b = 2y et l'orthogonalité donne :                     ⟺                 .
                                       (y - 2) + 2(2y) = 0           y = 2/5
         x-1
          2/5
Donc b' = 4 / 5 .
           1



5. Ax = b' ⟺ PAx = Pb' ⟺ LUx = Pb'.
On va donc d'abord résoudre : Ly = Pb' et ensuite Ux = y.
                  1                                     1
Ly = Pb' = 4 / 5 donne comme solution y = 2 / 15 .
                2/5                                     0
                                            -z + 2 / 5
Ux = y donne comme solution : x = (2 / 3)z - 1 / 15 avec z quelconque.
                                                 z
                                                               2/5
En particulier, si on prend z = 0, on obtient la solution x = -1 / 15
                                                                0

≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

4. Exercice 4




            5 2
1. A T A =        a pour polynôme caractéristque x 2 - 13x + 36 et donc comme valeurs
            2 8
propres 𝜆 1 = 9 et 𝜆 2 = 4. Les valeurs singulières de A sont donc 𝜎 1 = 3 et 𝜎 2 = 2.
                                                    5x + 2y = 9x
La recherche de vecteurs propres de A T A donne                   ⟺ y = 2x.
                                                    2x + 8y = 9y
                             1 1
On peut donc prendre v 1 =          pour 𝜆 1 = 9.
                              5 2
  5x + 2y = 4x                                                1 -2
                ⟺ x = - 2y. On peut donc prendre v 2 =                 pour 𝜆 2 = 4.
  2x + 8y = 4y                                                 5 1
~~~

## Page 6

~~~text
                                      1   1 -2
La matrice V est donc connue : V =                .
                                       5 2 1
Pour déterminer U, on va d'abord calculer u 1 et u 2 à partir de v 1 et v 2 . On obtient :

                                         1                5
                                                      1
                                  u 1 = Av 1 =            2
                                        𝜎1          3 5
                                                          4
                                        1                 0
                                                     1
                                  u 2 = Av 2 =           -2
                                        𝜎2             5
                                                          1
On doit ensuite compléter par un vecteur unitaire du noyau de AA T ou bien, ce qui revient
                                                                                     -2
                                                                                  1
au même, un vecteur orthogonal à u 1 et u 2 . On obtient par exemple : u 3 =          1 .
                                                                                  3
                                                                                      2
                                                      5 0 -2         5
                                              1
La matrice U est donc donnée par : U =                2 -6       5       .
                                          3       5
                                            4 3              2   5
                                         3 0
La dernière matrice est finalement : 𝛴 = 0 2 .
                                         0 0




                                                                             1/3 0 0
2. On sait que A = U𝛴V T et que A † = V𝛴 † U T avec 𝛴 † =                             .
                                                                              0 1/2 0
                                          1 1 4 -1
Le calcul donne bien : A † = V𝛴 † U T =                .
                                          9 2 -1 5 / 2




3. Le système Ax = b a pour solution :

                                1 1 4 -1                     3
                                †                                1
                         x=A b=                              2 =   .
                                9 2 -1 5 / 2                     1
                                                             2
~~~

## Page 7

~~~text
                               𝛼 + 2𝛽   =1          1
                                                𝛼
4. On cherche 𝛼, 𝛽 solution de 2𝛼 + 0.𝛽 = 1 ⟺ A   = 1 .
                                                𝛽
                               0.𝛼 + 2𝛽 = 1         1
La solution est donc :
                               1  1 1 4 -1                 1   1 4
                         𝛼   †
                           =A 1 =                          1 =
                         𝛽        9 2 -1 5 / 2                 9 7/2
                               1                           1
                                        4
                                    𝛼=
                                        9 .
                                         7
                                    𝛽=
                                        18

≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

5. Exercice 5




1. En notant D la partie diagonale de A, on peut écrire la formule de récurrence de Jacobi
sous la forme :
                  x n+1 = D -1 ((D - A)x n + b) = D -1 (D - A)x n + D -1 b
                                     x n+1 = Bxn + C
                           1 0 0 0 0 -2 0 0                   0 -1 0 0
                         1 0 1 0 0       2 0 2 0           1 1 0 1 0
avec B = D -1 (D - A) =                                  =
                         4 0 0 1 0       0 0 0 2           2 0 0 0 1
                           0 0 0 1 0 0 -2 0                   0 0 -1 0

             1 0 0 0      1        1
         1   0 1 0 0      2  1     2
et C =                      =4       .
         4   0 0 1 0      3        3
             0 0 0 1      4        4




2. La matrice A n'étant pas symétrique, il faut calculer le rayon spectral de B, en
~~~

## Page 8

~~~text
commençant par calculer son polynôme caractéristique.
                           1
                    -x -       0       0
                           2
                     1         1                        1     1                    2
                          -x           0           -x      -x
        𝜒 B (x) =    2         2            = x2      2 +1    2       = x2 +
                                                                               1
                                       1            1    4  1                  4
                     0    0    -x                  - -x    - -x
                                       2            2       2
                                   1
                     0    0    -       -x
                                   2
                     i i                                       1
Donc Spec(B) =      - , . Et son rayon spectral est donc 𝜌(B) = < 1.
                     2 2                                       2
La métode de Jacobi est donc convergente.




3. On sait que : x n+1 = Bx n + C. On en déduit :
                                0 -1 0 0            0       1    -1
                              1 1 0 1 0             1  1    2  1 4
                         x1 =                         +4      =4
                              2 0 0 0 1             1       3    3
                                0 0 -1 0            0       4    2

                                0 -1 0 0           -1       1    -2
                              1 1 0 1 0            4   1    2  1 6
                         x2 =                         +4      =8
                              8 0 0 0 1            3        3    8
                                0 0 -1 0           2        4    5
~~~
