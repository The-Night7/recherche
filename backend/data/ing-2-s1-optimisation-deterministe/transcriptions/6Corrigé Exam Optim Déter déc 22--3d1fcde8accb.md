# 6Corrigé Exam Optim Déter déc 22.pdf

[Ouvrir l’original](https://drive.google.com/open?id=19UNDbKC5YXxYvMESU2zOqyyiGP6lhH1x) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                  Corrigé Exam Optim Déter déc 22
Exercice 1
 1. On sait que lorsque f est différentiable et convexe, on a :
                      ∀(x, y) ∈ R n ,   f(y) ⩾ f(x) + < ∇f(x) , y - x >
    En remplaçant x par x * et y par n'impoirte quel élément x de H, on obtient :

                 ∀x ∈ H,      f(x) ⩾ f x * + < ∇f x * , x - x * > ⩾ f x * .
    Donc x * est un minimum global de (PC).
                                               1 1 -1        1
 2. a) H =     x ∈ R 3 , Ax = b avec A =              et b =   .
                                               2 -1 0        3
     b) Si x 1 et x 2 ∈ H, alors
    ∀𝜆 ∈ [0, 1], A(𝜆x 1 + (1 - 𝜆)x 2 ) = 𝜆Ax 1 + (1 - 𝜆)Ax 2 = b.
        Donc 𝜆x 1 + (1 - 𝜆)x 2 ∈ H.

     c) On a bien Ax * = b, donc x * est admissible.
                                                  18
                     2x 1                         7
                                                   6
     d) On a ∇f(x) = 2x 2          ⟹ ∇f x *    = -   , et
                     2x 3                          7
                                                   2
                                                 -
                                                   7
                    x1 + x2 - x3 = 1
    x∈H ⟹                            .
                    2x 1 - x 2   =3
       On en déduit :
                                          18          9       6          3       2          1
               < ∇f x * , x - x * > =          x1 -       -       x2 +       -       x3 +
                                           7         7   7       7     7         7
                 2                      26 2                                    26
              = (9x 1 - 3x 2 - x 3 ) -      = (x 1 + x 2 - x3 + 8x 1 - 4x 2 ) -
                 7                       7     7                                7
                2                                    26 2                 26
              = (x 1 + x 2 - x 3 + 4(2x 1 - x 2 )) -    = (1 + 4 × 3) -        = 0.
                7                                     7   7                7
       Donc d'après la question 1), x * est bien un optimum global de (P).

    e) ∇f x * est non nul alors que x * est un optimum global. Ceci est dû au fait qu'il
    s'agit d'un problème d'optimisation sous contraintes.
~~~

## Page 2

~~~text
Exercice 2
 1) f est strictement convexe puisque sa hessienne est A qui est définie positive.
    ∇f(x) = Ax + b et A inversible puisque
    définie ⟹ ∃!x * , Ax * = - b ⟹ ∇f x * = 0.

    Conclusion : x * est l'unique optimum global.

 2) (a) dk et dk-1 sont A-conjugués si < dk , Adk-1 > = 0. On a alors :
   0 =< -∇f(x k ) + 𝛽 k d k-1 , Ad k-1 > = - < ∇f(x k ), Ad k-1 > + 𝛽 k < d k-1 , Adk-1 >
                                          < ∇f(x k ), Ad k-1 >
                                 ⟺ 𝛽k =                        .
                                           < d k-1 , Adk-1 >
    (b) On sait que l'optimum de la fonction g(t) = f(x k + td k ) a lieu pour t = 𝜌 tel que :

                < ∇f(x k + 𝜌dk ), d k > = 0 ⟺< A(x k + 𝜌d k ) + b, d k > = 0
           ⟺< Ax k + b + 𝜌Ad k , d k > = 0 ⟺< ∇f(x k ) + 𝜌Ad k , d k > = 0
                                                             ∇f(x k ), d k >
           ⟺< ∇f(x k ), d k > + 𝜌 < Ad k , d k > = 0 ⟺ 𝜌 = -
                                                              < Ad k , d k >

 3) (a) On vérfie immédiatement que AX * + b = 0.
                0
    (b) X 0 =     .
                1
                                                   -1
       i. d 0 = - ∇f(X 0 ) = - AX 0 - b =
                                                   1
                                                                 -1
                     <∇f(X 0 ),d0 >     1                1       2
       ii. 𝜌 0 = -                    = 2 ⟹ X1 = X0 + 2 d0 =             .
                      <Ad 0 ,d0 >                                3
                                                                 2
                                                    1
                                                    2                <∇f(X 1 ),d1 >     1
       iii. d 1 = - ∇f(X 1 ) = - AX 1 - b =             et 𝜌 1 = -                    = 2.
                                                    1                 <Ad 1 ,d1 >

                                                    2
                                              -1
         Et donc : X 2 = X 1 + 𝜌 1 d 1 =       4    .
                                               7
                                               4
~~~

## Page 3

~~~text
                  0
    (c) X 0 =       . Méthode du gradient conjugué. La 1ère itération est la même que
                  1
                                                                -1
                                                                   1         2
    celle du gradient à pas optimal avec : X 1 = X 0 + d 0 =
                                                                   2         3
                                                                             2
                                                                                            1
                  < ∇f(X 1 ), Ad 0 >             1                                          4 .
       i. 𝛽 1 =                             =        et donc d 1 = - ∇f(X 1 ) + 𝛽 1 d 0 =
                     < d 0 , Ad 0 >              4                                          3
                                                                                            4
                                                 1    1
                                            < 2 , 4 >
                                              1   3
                     <∇f(X 1 ),d1 >              2    4       2
       ii. 𝜌 1 = -                    = -                  =3 .
                      <Ad 1 ,d1 >                3    1
                                            < 4 , 4 >
                                              3   3
                                                 4    4
                                      -1
                          2
       iii. X 2 = X 1 + d 1 =
                          3            3        = X*.
                                       2
    (d) La méthode du gradient conjugué à pas optimal converge vars la solution exacte
    en 2 itérations comme prévu en dimension 2 pour une fonction quadratique. La
    méthode du gradient à pas optimal semble également se rapprocher au fur et à
    mesure de la solution.




Exercice 3
 1) (a) d direction de descente en x ⟺< ∇f(x), d > ⩽ 0.
                                            1
    (b) Si f(x) = c + < B, x > +                < Ax, x > , alors ∇f(x) = Ax + b et H f (x) = A.
                                            2
    Par suite : d (0) = - A -1 AX (0) + b = - X (0) - A -1 b
    et donc : X (1) = X (0) + d (0) = - A -1 b = X * .
    (c) Il faut que la fonction soit 2 fois différentiable, calculer la matrice hessienne et
    l'inverser ou au minimum résoudre un système linéaire la concernant.
 2) f(x, y) = x 4 + 2y 4 + z 4 - 2x + y - z.
~~~

## Page 4

~~~text
                                                    1
                                              x=
            4x 3 - 2 0                             ∛2
                                                   -1
(a) ∇f(X) = 8y + 1 = 0 ⟺
               3
                                              y=        .
                                                   2
            4z 3 - 1 0
                                                   1
                                              z=
                                                   ∛4
              1
              ∛2
              -1
Donc X * =         unique point critique
              2
              1
              ∛4
               12x 2 0   0
                       2      (k)                           (k)
(b) H f (X) =    0 24y   0 . d existe à condition que H f X     soit
                           2
                 0   0 12z
inversible.
                                                    x
Il faut donc que les 3 coordonnées de X (k) =       y soient non nulles. Et dans ce cas :
                                                    z
                                                             4x 3 - 2
                                                                 12x 2
                                         -1                     8y 3 + 1
                   d (k) = - H f X (k)        ∇f X (k) = -                 .
                                                                 24y 2
                                                                4z 3 - 1
                                                                 12z 2
                                                    2           -1

                 1                          12                  6
                                            9                   -3
(c) Avec X (0) = 1 , on obtient : d (0) = -                 =        . Et par suite :
                 1                          24                  8
                                            3                   -1
                                                   12           4
                                                            5
                                                            6
                                                            5
                              X (1) = X (0) + d (0) =
                                                            8
                                                            3
                                                            4
~~~
