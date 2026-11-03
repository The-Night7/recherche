# Corrigé Rattrapage Optim détreministe 02-24.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1mv0IGJMKClPRMtLfnhFSy-rQGJ0Mxumd) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
   Corrigé rattrapage Optimisation déterministe 02-24




1) ‖∇f + d‖ ⩽ ‖∇f‖    ⟺ ‖∇f + d‖ 2 ⩽ ‖∇f‖ 2 ⟺ ‖∇f + d‖ 2 - ‖∇f‖ 2 ⩽ 0 .
  Or ‖∇f + d‖ 2 = ‖∇f‖ 2 + ‖d‖ 2 + 2 < ∇f, d > .
  On a donc ‖∇f + d‖ 2 - ‖∇f‖ 2 = ‖d‖ 2 + 2 < ∇f, d > ⩽ 0
                                                    ‖d‖ 2
                             ⟺ < ∇f, d > ⩽ -              <0
                                                     2
  On en conclut que d est bien une direction de descente.




2) f étént de classe C 1 , on peut faire son développement limité à l'ordre 1 au voisinage
   de x qui donne :
                          f(x + h) = f(x) + ∇f(x) T h + o(‖h‖)
     a) Si on prend h = 𝜃d, avec d vecteur constant, cela donne :
             f(x + 𝜃d) = f(x) + ∇f(x) T (𝜃d) + o(‖𝜃d‖) = f(x) + 𝜃∇f(x) T d + o(𝜃)
        On en déduit :
                     f(x + 𝜃d) - f(x)                    o(𝜃)
                                         = ∇f(x) T d +          = ∇f(x) T d + o(1)
                             𝜃                            𝜃
        Et par passage à la limite,
                                       f(x + 𝜃d) - f(x)
                                 lim                      = ∇f(x) T d.
                                 𝜃→0          𝜃
~~~

## Page 2

~~~text
    b) x * minimum local ⟺ ∃r > 0, ∀x ∈ U, x ∈ B x * , r ⟹ f(x) ⩾ f x * .
       où B x * , r désigne la boule ouverte de centre x * et de rayon r.
       Soit x ∈ U, comme U est convexe, ∀𝜃 ∈ [0, 1], y = 𝜃x + (1 - 𝜃)x * ∈ U.
       Remarquons que y = x * + 𝜃 x - x * et notons d = x - x * . Ce qui nous permet
       d'écrire : y = x * + 𝜃d.
                                                             r
       Pour 𝜃 suffisamment petit, plus précisèment 𝜃 <           = 𝜖, on aura y ∈ B x * , r .
                                                        ‖d‖
                                                 *
       Par conséquent : ∀𝜃 < 𝜖, f(y) ⩾ f x           ⟺ f x * + 𝜃d - f x *        ⩾0
                   f x * + 𝜃d - f x *
       Ainsi :                          ⩾ 0 et par passage à la limite lorsque 𝜃 → 0, on
                           𝜃
       obtient :
                                        T             T
                                ∇f x * d = ∇f x * x - x * ⩾ 0.
    c) Nous savons que lorsque f est convexe et différentiable, nous avons :
                 ∀x, y ∈ U f(y) ⩾ f(x) + < ∇f(x), y - x >
    Si maintenant, x * vérifie la condition nécessaire de 1er ordre, à savoir :
                       ∀x ∈ U, < ∇f x * , x - x * > ⩾ 0.
    La caractérisation de la convexité appliquée avec x = x * donne alors :
                ∀y ∈ U    f(y) ⩾ f x * + < ∇f x * , y - x * > ⩾ f x *
    Donc f x * est un minimum global de f sur U.




            1             1                     1                        1
1) f(x) =     ‖Ax - b‖ 2 = (Ax - b) T (Ax - b) = x T A T Ax - x T A T b + b T b
            2             2                     2                        2
~~~

## Page 3

~~~text
                                                 ∇f(x) = A T Ax - A T b
   On en déduit immédiatement que :                                     .
                                                 H f (x) = A T A
2) H f = A T A est symétrique et définie positive car A est inversible.
   Par conséquent, f est strictement convexe.
3) Le minimum est atteint au seul point critique :
                                           -1                   -1
                           x* = ATA             A T b = A -1 A T A T b = A -1 b.
                               -1                                      -1
4) x (1) = x (0) - H f x (0)        ∇f x (0)     = x (0) - H f x (0)        A T Ax (0) - A T b
                           -1                                               -1                   -1
   x (1) = x (0) - A T A        A T Ax (0) - A T b = x (0) - A -1 A T A T Ax (0) + A -1 A T A T b
                              x (1) = x (0) - x (0) + A -1 b = x * .
5) Les directions de descente étant A-conjuguées 2 à 2, la convergence peut se faire en
   moins de n itérations.




            1                                               -6        4 1
1) J(X) =       X T AX + b T X + c avec c = 0, b =             et A =     .
            2                                               -1        1 2
2) ∇J(X) = AX + b        et H J (X) = A.
3) A est symétrique et définie positive car ses valeurs propres sont > 0 (leur
   somme = tr(A) = 6, leur produit = det(A) = 7). Donc J est strictement convexe.
4) Le point minimisant J est l'unique point critique :
                                                1 2 -1         -6   -11 / 7
                        X * = - A -1 b =                          =         .
                                                7 -1 4         -1    2/7
~~~

## Page 4

~~~text
                                                      6
1) d (0) = - ∇J X (0) = - b =                           .
                                                      1
                ‖∇J X (0) ‖ 2                 ‖d (0) ‖ 2             37
      (0)
  𝜌         =       (0)T        (0)
                                      =       (0)T        (0)
                                                                 =
                d          Ad             d          Ad              158
                                                                      111
                                              37 6                       79 .
  X (1) = X (0) + 𝜌 (0) d (0) =                     =
                                              158 1                      37
                                                                         158
                                                -23
2) ∇J(X (1) = AX (1) + b =                      158
                                                69
                                                 79
                                                     2               2
                                              -23               69
                ‖∇J X (1) ‖ 2                 158
                                                         +      79
      (1)                                                                      529
  𝛽         =                         =                                  =           .
                ‖∇J X (0) ‖ 2                         37                     24964
                                                                23                       1702
  d (1) = - ∇J X (1) + 𝛽 (1) d (0) =                            158 + 529 6 =   6241 .
                                                                -69  24964 1    21275
                                                                              -
                                                                79              24964
~~~
