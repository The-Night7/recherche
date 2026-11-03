# Corrigé exam analyse numérique 22.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1H-G1qSWde75mnLCyPEHlXZpsKJqdTGpz) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
           Corrigé exam analyse numérique 2022
1. Exercice 1
On souhaite approcher le zéro positif de la fonction définie par : f(x) = 2x 2 - 2x - 1.
                                       1+ 3
On sait que la valeur exacte est 𝛼 =        ≃ 1, 366.
                                         2


    1. Dans un premier temps, on envisage d'utiliser la méthode du point fixe en utilisant la
       fonction définie par g(x) = 2x 2 - x - 1.
       Expliquer le lien entre f, g et 𝛼 et donner la formule de récurrence de cette méthode.
                  f(x) = 0 ⟺ g(x) = x. Les zéros de f sont les points fixes de g.
       𝛼 est donc l'unique point fixe positif de g. La suite récurrente censée converger vers 𝛼
                            x0                     x0
       est définie par :                    ⟺
                            x n+1 = g(x n )        x n+1 = 2x n2 - x n - 1
    2. Justifier que 𝛼 est un point fixe répulsif et conclure quant à la convergence de cette
       méthode.
                                                      1+ 3
                               g'(𝛼) = 4𝛼 - 1 = 4       2
                                                           -1 = 1+2                  3.
       On a bien |g'(𝛼)| > 1, par conséquent 𝛼 est un point fixe répulsif.
       La suite récurrente x n ne convergera pas (sauf si x 0 = 𝛼).
    3. On souhaite maintenant approcher 𝛼 par la méthode de Newton.
       Donner la formule de récurrence associée.
                                                                                                   f(x n )
       La formule de récurrence de la méthode de Newton est : x n+1 = x n -                                   .
                                                                                                   f'(x n )
                                       2x n2 - 2x n - 1
       Ce qui donne : x n+1 = x n -                       .
                                          4x n - 2
    4. En partant de x 0 = 1, calculer les 2 premiers itérés x 1 et x 2 .
                                                2x 02 - 2x 0 - 1                -1           3
                    x0 = 1 ⟹ x1 = x0 -                              = 1-             =           = 1, 5
                                                     4x 0 - 2                   2            2
                                                                            1
                        3                    2x 12 - 2x 1 - 1       3       2        3       1
                 x1 =       ⟹ x2 = x1 -                         =       -       =        -       = 1, 375
                        2                       4x 1 - 2            2       4        2       8


2. Exercice 2
                                 2 0 1
On considère la matrice A =      4 -1 3 et on s'intéresse au système linéaire Ax = b où
                                 -2 -1 3
~~~

## Page 2

~~~text
                      5
b est donné par : b = 8 .
                      -4

   1. Justifier que A possède une factorisation L U.
      Est-elle unique ?
      Les déterminants des 2 sous-matrices principales sont non nuls, donc A possède une
      factorisation L U.
                            -1 3    4 -1
      De plus, det(A) = 2        +1                 = - 2 ≠ 0, donc cette factorisation est
                            -1 3    -2 -1
      unique.
   2. Déterminer les 2 matrices L et U de cette factorisation.
                                                                         2 0 1
                                            L 2 ← L 2 - 2L 1
      La matrice U s'obtient en 2 étapes :                   qui donne : 0 -1 1 ,
                                            L3 ← L3 + L1
                                                                         0 -1 4
                                             2 0 1
       puis L 3 ← L 3 - L 2 qui donne : U = 0 -1 1 .
                                             0 0 3
                        1 0 0
      La matrice L = a 1 0 peut être obtenue par identification grâce à L U = A.
                        b c 1
                                                     2a = 4
                            2 0         1            a+1 = 3             a=2
                 L U = 2a -1 a + 1             ⟹ 2b = -2            ⟺ b = -1
                           2b -c b + c + 3           -c = -1             c=1
                                                     b+c+3 = 3
                   1 0 0
      Donc L = 2 1 0
                  -1 1 1
   3. Utiliser cette factorisation pour résoudre le système.
      La résolution revient à résoudre 2 systèmes triangulaires :
                                                Ly = b
                                     Ax = b ⟺
                                                Ux = y
                                                    5
                                     Ly = b ⟹ y = -2
                                                    3
                                                    2
                                     Ux = y ⟹ x = 3
                                                    -1
~~~

## Page 3

~~~text
3. Exercice 3
On rappelle que la norme matricielle subordonnée à la norme 2 est calculée de la manière

suivante : ‖|A‖| 2 =        𝜌 AA * =        𝜌 A * A = plus grande valeur singulière de A.

    1. Montrer que si Q est une matrice réelle orthogonale (i.e. Q -1 = Q T ), alors
       ‖|Q‖| 2 = 1.
                ‖|Q‖| 2 = 𝜌 QQ * = 𝜌 QQ T = 𝜌 QQ -1 = 𝜌(I n ) = 1
    2. En déduire que si A est une matrice réelle inversible, qui s'écrit sous la forme
       A = QR, avec Q orthogonale, alors les conditionnements pour la norme 2 vérifient :
                                     Cond 2 (A) = Cond 2 (R)
          A A = A A = (QR) QR = R T Q T QR = R T Q -1 QR = R T I n R = R T R = R * R
           *       T            T


      Donc : ‖|A‖| 2 =          𝜌 A*A =         𝜌 R * R = ‖|R‖|2
      De même, puisque : A -1 = (QR) -1 = R -1 Q -1 = R -1 Q T , on peut écrire :
                      T                         T                       T                 T                   *
         A -1 A -1        = R -1 Q T R -1 Q T       = R -1 Q T Q R -1       = R -1 R -1       = R -1 R -1
      Donc :
                                        *                         T                           *
       ‖|A -1 ‖|2 =       𝜌 A -1 A -1       =       𝜌 A -1 A -1       =      𝜌 R -1 R -1          = ‖|R -1 ‖| 2 .
      Finalement, on a bien :
                      Cond 2 (A) = ‖|A‖|2 ‖|A -1 ‖| 2 = ‖|R‖|2 ‖|R -1 ‖| 2 = Cond 2 (R)
4. Exercice 4
La résolution d'un problème d'interpolation nous a ramené au système linéaire Ax = b avec :
                                      1 0 1                    1
                                      1 0 0                    1
                                   A=                   et b =    .
                                      0 1 0                    1
                                      0 1 1                    -1

    1. Ce système n'ayant pas de solution, quel est le problème des moindres carrés par
       lequel il est remplacé ?
       Le système est surdéterminé, il est remplacé par la recherche de :
                                            x = arg min ‖Ax - b‖ 22
    2. La solution du problème aux moindres carrés précédent fait appel à la décomposition
       en valeurs singulières :
                                                    A = U 𝛴 VT
      où 𝛴 est une matrice diagonale de même dimension que A et dont les coefs
      diagonaux sont les valeurs singulières de A par ordre décroissant.
~~~

## Page 4

~~~text
  Le pseudo-inverse A † de A s'obtient facilement à partir de cette décomposition.

  Donner l'expression de de A † en fonction de U, V et de 𝛴 † dont vous expliciterez les
  composantes.
  Le pseudo-inverse A † est donné par : A † = V 𝛴 † U T ,
   avec 𝛴 † matrice de taille 3 × 4 diagonale, dont les coefs diagonaux sont les inverses
   de ceux de 𝛴.
3. Calculer la solution de ce problème des moindres carrés à partir de la donnée de :
                                         1    3    1     -1
                                         4    4    4         4
                                         -1   1    3         1
                                 A† =
                                         4    4 4            4
                                         1    -1 -1          1
                                         2    2 2            2
                                    1    3    1 -1
                                   4     4    4    4         1
                                                                  3/2
                                   -1    1    3    1         1
                     x = A†b =                                  = 1/2
                                    4   4 4        4         1
                                                                  -1
                                    1   -1 -1      1         -1
                                   2 2 2 2
4. Question bonus : Justifier que A est de rang maximal et en déduire une expression
   de son pseudo-inverse A † en fonction de A et A T .
   On a bien rang(A) = 3. On peut le voir en remarquant que la matrice obtenue en
  éliminant la 1ère ligne est inversible, ou en montrant que les 3 colonnes sont
  indépndantes.
  Par conséquent, le peudo-inverse peut être obtenu par la formule :
                                                   -1
                                     A† = ATA           AT
~~~
