# Corrige-Examen-Ana-Num05-23.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Ro-lgHVrubJr-18YgNjnEILc8CJ4gE_O) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                 Examen d'analyse numérique
                                          mai 2023
Exercice 1

  On souhaite résoudre numériquement l'équation :
                                    -ln(x) = x ⟺ ln(x) + x = 0 .
  1. Montrer que cette équation possède une unique solution 𝛼 ∈ ]0, 1[.
     On pose f(x) = ln(x) + x définie sur ]0, + ∞[.
                 1
     f'(x) = 1 + > 0, donc f est strictement croissante. lim f(x) = - ∞ et f(1) = 1.
                 x                                       x → 0+
     Conclusion : ∃!𝛼 ∈ ]0, 1[, f(𝛼) = 0.
  2. On décide d'essayer d'abord la méthode du point fixe.
     (a) Quelle est la formule de récurrence permettant de construire la suite correspondante ?
     Le réel 𝛼 recherché est le point fixe de la fonction g(x) = - ln(x). Il est donc limite possible
     d'une suite définie par : x k+1 = g(x k ) = - ln(x k ).
     (b) Justifier, en étudiant la nature du point fixe, pourquoi cette méthode ne marche pas.
                                    1
    𝛼 ∈ ]0, 1[ ⟹ |g'(𝛼)| =               > 1 ⟹ 𝛼 est un poit fixe répulsif.
                                    𝛼
     La méthode du point fixe ne convergera pas.
  3. On pense ensuite à la méthode de Newton.
     (a) Donner la formule de récurrence détaillée permettant de construire la suite correspondant à
     l'application de la méthode de Newton à f(x) = ln(x) + x.
                    f(x k )             ln(x k ) + x k             x k ln(xk ) + x k2       x k (1 - ln xk )
    x k+1 = x k -              = xk -                    = xk -                         =                      .
                    f'(x k )                     1                       1 + xk                 1 + xk
                                           1+ x
                                                  k

    (b) Calculer les 2 premiers termes x 1 , x 2 obtenus en partant de x 0 = 1.
                                                             x 0 (1 - ln x 0 )
                                                                        1
                                                      x1 =           = .
                                                           1 + x0       2
                                               x 1 (1 - ln x 1 ) 1 + ln 2
                                          x2 =                  =         ≃ 0.56
                                                    1 + x1          3

Exercice 2

  Soit A ∈ M n (R) une matrice inversible qui possède une factorisation LU avec L matrice
  triangulaire inférieure à coefficients diagonaux tous égaux à 1 et U triangulaire supérieure.
  1. On veut montrer que cette factorisation est unique. Supposons donc l'existence de 2
      factorisations de ce type : A = L 1 U 1 = L 2 U 2 .
    (a) En raisonnant sur les produits de matrices triangulaires, montrer que L 1 L 2-1 = I n .
    L 1 et L 2 sont inversibles car triangulaires à coefs diagonaux égaux à 1. Par conséqeunt U 1 et U 2
    sont inversibles également (U 1 = L 1-1 A).
                                           L 1 U 1 = L 2 U 2 ⟹ L 1 L 2-1 = U 2 U 1-1
    L 1 et L 2-1 sont des matrices triangulaires inférieures, leur produit l'est également.
    U 2 et U 1-1 sont des matrices triangulaires supérieures, leur produit de même.
~~~

## Page 2

~~~text
    L'égalité L 1 L 2-1 = U 2 U 1-1 implique que ces 2 produits forment une matrice diagonale.
    Avec des 1 sur la diagonale. Conclusion : L 1 L 2-1 = I n .
    (b) En déduire que L 1 = L 2 et U 1 = U 2 et conclure.
                             L 1 L 2-1 = I n = U 2 U 1-1 ⟹ L 1 = L2 et U 1 = U 2 .
                                       4 2 0
  2. On considère la matrice A = 2 5 2 .
                                       0 2 5
     (a) Justifier que A possède une factoristion LU et qu'elle est unique.
                                                4 2
     Les 2 sous-matrices principales (4) et             de A sont inversibles, donc A possède une
                                                2 5
     factorisation LU. De plus A est ele même inversible ; cette décomposition est donc unique.
     (b) Déterminer les matrices L et U de cette factorisation.
     A partir de A, on obtient U par les transformations habituelles du pivot de Gauss :
                                              1                       1
                                     L2 ← L2 - L1            L3 ← L3 - L2
                           4 2 0              2     4 2 0             2     4 2 0
                           2 5 2         ⟹          0 4 2         ⟹         0 4 2 =U
                           0 2 5                    0 2 5                   0 0 4
                                                        1 0 0
    On obtient ensuite L par identification grâce à L = a 1 0 et LU = A.
                                                        b c 1
                                     1 0 0
                                     1
                                         1 0
    Ce qui donne finalement L = 2              .
                                         1
                                     0      1
                                         2
                                                                             0
  3. Utiliser ces 2 matrices L et U pour résoudre le système Ax = b avec b = 0 en expliquant
                                                                             16
    les différentes étapes.
                            Ax = b ⟺ LUx = b ⟺ Ly = b avec y = Ux.
                                                         0
    On commence par résoudre Ly = b, qui donne y = 0 .
                                                         16
                                                            1
    Ensuite, on résout : Ux = y, qui donne facilement x = -2 .
                                                            4


Exercice 3

  Pour résoudre le système linéaire Ax = b, où A est une matrice carrée d’ordre n, on considère la
  méthode suivante, dite méthode de Richardson :
  Soit r > 0 et x 0 ∈ R n , on définit la suite x k ∈ R n par la formule de récurrence :
                                           x k+1 = x k - r(Ax k - b)

  1. Montrer que cette méthode est du type Mx k+1 = Nx k + b issue d'une écriture A = M - N.
     Préciser ce que sont les matrices M et N.
~~~

## Page 3

~~~text
    On peut réécrire la relation de récurrence :
                                                  1               1
            x k+1 = (I n - rA)xk + rb ⟺ r I n x k+1 =               I - A xk + b
                                                                  r n
                                                                                   ⟺ Mx k+1 = Nx k + b
                1            1
    avec M = I n et N = I n - A. On vérifie que l'on a bien A = M - N.
                r            r
  2. Montrer que la matrice de récurrence B telle que : x k+1 = Bx k + c, où c est un vecteur constant,
     est définie par : B = I n - rA, où I n désigne la matrice identité.
                                                                      B = I n - rA
    On a bien : x k+1 = (I n - rA)x k + rb = Bx k + c avec                         .
                                                                      c = rb
  3. On suppose A symétrique définie positive.
     (a) Exprimer les valeurs propres de B en fonction de des valeurs propres 𝜆 i de A.
                    x vecteur propre de A pour 𝜆 ⟺ Ax = 𝜆x ⟺ (I n - rA)x = (1 - r𝜆)x
     Donc, les valeurs propres de B = I n - rA sont les (1 - r𝜆 i ) où les 𝜆 i sont les valeurs propres de
     A.
     (b) Justifier que le rayon spectral de B est : 𝜌(B) = max(|1 - 2𝜆 min |, |1 - 2𝜆 max |), et en déduire
     un critère de convergence de cette méthode.
     Il y avait une erreur dans l'énoncé. La bonne expression est :
                                     𝜌(B) = max(|1 - r𝜆 min |, |1 - r𝜆max |).
     On a bien évidemment, pour tout i :      1 - r𝜆max ⩽ 1 - r𝜆 i ⩽ 1 - r𝜆 min .
     On en déduit, par application de la valeur absolue :
                                     |1 - r𝜆 i | ⩽ max(|1 - r𝜆 min |, |1 - r𝜆max |)
    D'où le résultat :
                           𝜌(B) = max |1 - r𝜆 i | = max(|1 - r𝜆 min |, |1 - r𝜆max |)
                                         i



Exercice 4

                                                                                         1 1
  Afin d'effectuer la décomposition en valeurs singulières de la matrice A =             2 1 , on a calculé
                                                                                         -1 1
  les valeurs propres de A T A et obtenu : 𝜆 1 = 7 et 𝜆 2 = 2.


                                             2               1
  1. Vérifier que les vecteurs v 1 =             et v 2 =           sont propres associés à ces valeurs propres.
                                             1               -2
               6 2                                          14                          2
    ATA =          , et on a bien : A T Av 1 =                    = 7v 1 , A T Av 2 =        = 2v 2 .
               2 3                                          7                           -4
  2. Sans les calculer, indiquer, en justifiant, quelles sont les valeurs propres de AA T .
                                    2 3 0
                                 T
    A est de rang 2, donc AA = 3 5 -1 est de rang 2.
                                    0 -1 2
                            T     T
    De plus les matrices AA et A A possèdent les mêmes valeurs peopres non nulles. Par
    conséquent, les valeurs propres de AA T sont : 7, 2 et 0.
~~~

## Page 4

~~~text
                                                 3                      1                    -3
3. Vérifier que les vecteurs u 1 =               5    , u2 =            0       et u 3 =     2     sont propres associés à ces
                                                 -1                     3                    1
  valeurs propres.
   On vérifie facilement que : AA T u 1 = 7u 1 , AA T u 2 = 2u 2 et AA T u 3 = 0.
4. Expliquer comment obtenir les matrices orthogonales U et V de la décomposition en valeurs
   singulières de A à partir de ces vecteurs.
   La matrice U est obtenue en normalisant les vecteurs u 1 , u 2 , u 3 mais à un signe près.
   De même, la matrice V est obtenue en normalisant les vecteurs v 1 , v 2 toujours à un signe près.
   Le choix des signes se fait grâce à l'égalité : A = U𝛴V T ⟺ AV = U𝛴.
5. Calculer la matrice 𝛴 de cette décomposition.

                                                                            7     0
                                                       𝛴=               0             2
                                                                        0         0
6. Expliquer comment utiliser cette décomposition pour résoudre le système linéaire Ax = b avec
         2
  b=     2 .
         0
  Le système Ax = b n'a pas de solution exacte, il est remplacé par le pb. aux moindres carrés :
       x = arg min ‖Ax - b‖22 .
                  x
  La solution est donnée par : x = A † b où A † est le pseudo-inverse de A donné par la formule :
                                                              A † = V𝛴 † U T
                      1
                               0        0
                          7
  avec 𝛴 † =                                 .
                               1
                      0                 0
                                   2
  Complément :
  Le calcul exact des matrices U et V donne :
            3             1        -3
             35           10            14            2         -1
            5                          2                  5         5                         1 1 4 -5
  U=                      0                  , V=                               ⟹ A† =
            35                          14            1         2                             14 4 2 8
           -1             3            1                  5         5
            35            10           14
                                                                                      -1          1 1 4 -5
  Résultat que l'on peut retrouver grâce à : A † = A T A                                   AT =            .
                                                                                                  14 4 2 8
                                                                                                     5
                                                                                   1 10             7 .
  La solution du système linéaire est donc : x = A † b =                                 =
                                                                                   14 12            6
                                                                                                    7
~~~
