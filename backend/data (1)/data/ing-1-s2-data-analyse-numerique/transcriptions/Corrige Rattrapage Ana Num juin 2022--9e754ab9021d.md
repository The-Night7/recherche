# Corrige Rattrapage Ana Num juin 2022.pdf

[Ouvrir l’original](https://drive.google.com/open?id=177PevNzyUVo0zTu2haVp2yE4QhtRtRMG) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
         Corrige Rattrapage Ana Num juin 2022




1.      f'(x) = e x - 4 est strictement négative sur ]0, 1[. f est donc strictement
     décroissante.
              f(0) = 1 > 0 et f(1) = e - 4 < 0 ⟹ ∃!𝛼 ∈ ]0, 1[, f(𝛼) = 0 .
                           1
2.    Si on pose g(x) = e x , on a :           g(x) = x ⟺ f(x) = 0 .
                           4
   𝛼 est donc l'unique point fixe de g dans I = ]0, 1[ .
   La suite récurrente x n , associée à g devrait, en cas de convergence, tendre vers 𝛼.
                             1                       1 e
                  g'(x) = e x est comprise entre et           ⟹ |g'(𝛼)| < 1.
                             4                       4 4
   𝛼 est donc un point fixe attractif. La suite est donc convergente.
3.     La formule de récurrence de la méthode de Newton est la suivante :
                                             f(xn )            e xn - 4xn
                             xn+1 = xn -              = xn -                .
                                           f'(xn )              e xn - 4
                                                                                       1
                                                                                           4
                                              1  1                              1     e3 - 3
                  x0 = 0 ⟹        x1 = 0 -      = ⟹                 x2 =          -
                                             1-4 3                              3      1
                                                                                      e3 - 4
~~~

## Page 2

~~~text
1. Si x = 0, on a évidemment Ax = 0 et par conséquent : ‖Ax‖ ⩽ ‖|A‖| × ‖x‖ .
                               ‖Ax‖
  Par définition, ‖|A‖| = sup       . Par conséquent :
                           x≠0 ‖x‖

                         ‖Ax‖
                              ⩽ ‖|A‖| ⟹ ‖Ax‖ ⩽ ‖|A‖| × ‖x‖.
                          ‖x‖

  On en déduit, pour 2 matrices carrées A et B :
                      ‖ABx‖ ⩽ ‖|A‖| × ‖Bx‖ ⩽ ‖|A‖| × ‖|B‖| × ‖x‖
                                ‖ABx‖
  Ce qui implique, pour x ≠ 0 :         ⩽ ‖|A‖| × ‖|B‖| .
                                 ‖x‖

  Par passage au sup, on obtient l'inégalité souhaitée.
2. Rappelons que 𝜅(A) = ‖|A‖| × ‖|A -1 ‖| et montrons le résultat par récurrence.
   Initialisation : Pour k = 0, on a :
                                𝜅(A) 0 = 1 = 𝜅(In ) = 𝜅 A 0 .
  Hérédité : Supposons, pour un k fixé, 𝜅 A k ⩽ 𝜅(A) k .
  Tout d'abord, on a :
                                             -1                               -1
         𝜅 A k+1 = ‖|A k+1 ‖| × ‖| A k+1          ‖| = ‖|A k × A‖| × ‖| A k        × A -1 ‖|
  Ensuite, d'après la question précédente, on peut écrire :
                                        -1
          𝜅 A k+1 ⩽ ‖|A k ‖| × ‖| A k        ‖| × ‖|A‖| × ‖|A -1 ‖| = 𝜅 A k × 𝜅(A)
  On a donc bien :
                                    𝜅 A k+1 ⩽ 𝜅(A) k+1 .
~~~

## Page 3

~~~text
3. Rappelons que les normes 1 et infinie d'une matrice sont définies par :
                                       n                                         n
                     ‖|A‖|1 = max ∑ |aij |          et     ‖|A‖|∞ = max ∑ |aij |
                              j=1,..,n i=1                              i=1,..,n j=1

                                    2 1                     1 / 2 -1 / 2
                            A=                 ⟹ A -1 =
                                    0 1                      0      1
  On en déduit immédiatement :
  ‖|A‖|1 = 2,         ‖|A‖|∞ = 3,          ‖|A -1 ‖|1 = 3 / 2 et ‖|A‖|∞ = 1.
  Et finalement :
                                  𝜅1 (A) = 3         et   𝜅2 (A) = 3.




1.
• Méthode directe = méthode donnant la solution exacte en un nombre fini d'étapes de
   calcul.
   Exemple : factorisation LU (pivot de Gauss).
• Méthode itérative = méthode basée sur la construction d'une suite convergeant vers
   la solution.
   Exemple : Jacobi, Gauss-Seidel.
2. En notant D la partie diagonale de A, on a : J = D -1 (D - A)
                -1
     2 0             0 -1         1/2 0             0 -1            0    -1 / 2
  J=                 ×        =                ×            =                    .
     0 4            -1 0           0 1/4           -1 0          -1 / 4    0
                                  1                                        1
  Les valeurs propres de J sont ±     . Donc le rayon spectral est 𝜌(J) =       < 1.
                                    8                                        8
  La méthode de Jacobi est donc convergente.
3. La formule de récurrence est : x n+1 = Jx n + D -1 b .
~~~

## Page 4

~~~text
              1                  1/2                    1/8
       x0 =         ⟹ x1 =                ⟹ x2 =
              0                  3/4                    7/8
    4. En notant T la partie triangulaire inférieure de A, on a : G = T -1 (T - A)
                    -1
          2 0             0 -1        1/2    0        0 -1         0 -1 / 2
       G=                ×       =                ×          =              .
          1 4             0 0        -1 / 8 1 / 4     0 0          0 1/8
                                    1                                       1
       Les valeurs propres de G sont et 0. Donc le rayon spectral est 𝜌(J) = < 1 .
                                    8                                       8
       La méthode est donc convergente.
       La formule de récurrence est : x n+1 = Gx n + T -1 b .
              1                  1/2                      1 / 16
       x0 =         ⟹ x1 =                ⟹ x2 =
              0                  7/8                     63 / 64




Les disques lignes de Gershgorin sont :
                              D1l = { z, |z - 10| ⩽ 2 } = D(10, 2)
                                D2l = { z, |z - 8| ⩽ 7 } = D(8, 7)
                              D1l = { z, |z - 5| ⩽ 12 } = D(5, 12)
                             D1l = { z, |z - 0| ⩽ 1 / 2 } = D(1, 1 / 2)
Les disques colonnes de Gershgorin sont :
                              D1l = { z, |z - 10| ⩽ 2 } = D(10, 2)
                               D2l = { z, |z - 8| ⩽ 7 } = D(8, 7)
                              D1l = { z, |z - 5| ⩽ 12 } = D(5, 12)
                             D1l = { z, |z - 0| ⩽ 1 / 2 } = D(1, 1 / 2)
La matrice étant à coefficients réels, elle possède soit des valeurs propres réelles, soit des
paires de valeurs propres complexes conjuguées qui se trouvent dans le même disque par
symétrie.
Le disque D(1, 1 / 2) est disjoint des 3 autres. Il contient donc une unique valeur propre.
Celle-ci est forcément réelle.
~~~

## Page 5

~~~text
La réunion des 3 autres disques contient 3 valeurs propres dont une (au minimum) est réelle.
Il y a donc au minimum 2 valeurs propres réelles, et par conséquent au maximum deux
valeurs propres non réelles.




           0 1
                                    1 0
    1. A = 0 2        ⟹ ATA =           . Les valeurs propres sont évidemment 1 et 5.
                                    0 5
           1 0
       Les valeurs singulières de A sont donc :   5 et 1.
    2. On a évidemment :
                                              5 0
                                          𝛴=    1 0
                                                0 0
                                         0    1       0 1
      Les vecteurs propres de A T A sont   et     ⟹V=
                                         1    0       1 0
               1 2 0
          T
      AA = 2 4 0 a comme valeurs propres :
               0 0 1
                                   1
      𝜆1 = 5 associée au vecteur 2 ,
                                   0
~~~

## Page 6

~~~text
                             0
  𝜆2 = 1 associée au vecteur 0
                             1
                                  2
  et 𝜆 3 = 0 associée au vecteur -1 .
                                  0
  La matrice candidate pour U est donc :
          1/ 5 0 2/ 5                 1        0     2
                                  1
  U = 2 / 5 0 -1 / 5 =                2        0    -1 .
            0    1      0           5 0            5 0
  On vérifie que l'on a bien :
                                       A = U 𝛴 VT .
3. Pour calculer le pseudo-inverse de A, on a besoin de celui de 𝛴.
                         1                                       0     1 0
                              0  0
                𝛴† =                  ⟹ A† = V 𝛴† UT =           1
                           5                                           0 0
                         0       1 0                               5
4. La meilleure solution du système Ax = b, qui n'a pas de solution exacte, est celle du
  problème aux moindres carrés : min ‖Ax - b‖ 2 .
                                         x
  Cette solution est donnée par :
                                                         1
                                       x = A†b =
                                                    1/       5
~~~
