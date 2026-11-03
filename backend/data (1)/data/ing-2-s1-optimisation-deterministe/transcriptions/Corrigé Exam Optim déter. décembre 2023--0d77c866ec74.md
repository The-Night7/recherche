# Corrigé Exam Optim déter. décembre 2023.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1wiiZrLi-okABz3aUNmPccGiYdeelLg82) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
      Corrigé Exam Optim déter. décembre 2023




≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
Réponses :
   1) A'A = A T A est symétrique, et ses valeurs propres sont positives ou nulles.
      En effet, si 𝜆 est une valeur propre de A'A, il existe x ≠ 0, tel que A'Ax = 𝜆x.
     On a alors : 𝜆‖x‖ 2 =< 𝜆x, x > =< A'Ax, x > =< Ax, Ax > = ‖Ax‖ 2 ⩾ 0.
     Si on lui ajoute 𝜆I p , avec 𝜆 > 0, la matrice A'A + 𝜆I p ne possède que des valeurs
     propres strictement positives. (Rappel : non inversible ⟺ admet 0 comme valeur
     propre).
     Cette matrice A'A + 𝜆I p est donc bien inversible.
   2) Sachant que ‖x‖ 2 = x'x = x'I p x, on peut écrire :
           f(x) = (b - Ax)'(b - Ax) + 𝜆x'I p x = b'b + x'A'Ax - x'A'b - b'Ax + 𝜆x'I p x
                              f(x) = ‖b‖ 2 - 2x'A'b + x'(A'A + 𝜆Ip )x
      (Remarque : x'A'b =< x, A'b > =< A'b, x > = (A'b)'x = b'Ax)

                                                      1             c = ‖b‖ 2
      Donc f(x) s'écrit bien sous la forme : c + x'd + x'Bx avec d = -2A'b
                                                      2
                                                                    B = 2(A'A + 𝜆I p )
      c est une constante, d = A'b est un vecteur constant et B = 2(A'A + 𝜆I p ) est une
      matrice symétrique. f est donc bien une fonction quadratique.
   3) ∇f(x) = Bx + d = 2(A'A + 𝜆I p )x - 2A'b.
   4) On sait que A'A + 𝜆I p est symétrique et on a montré que ses valeurs propres étaient
     strictement positives. Par conséquent elle est définie positive.
~~~

## Page 2

~~~text
   5) On s'intéresse à : (P) min f(x).
                                   x∈R p
         a) La matrice hessienne de f est B = 2(A'A + 𝜆I p ) définie positive, donc f est
            strictement convexe. De plus le gradient s'annule bien en un seul point x * .
            Conclusion : (P) possède une unique solution.
         b) x * est solution de ∇f x * = 0        ⟹ 2(A'A + 𝜆Ip )x * - 2A'b = 0
                                           ⟹ x * = (A'A + 𝜆I p ) -1 A'b
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡




≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
Réponses :
                                                                    1
   1) f(x) = 30 + x 1 - x 2 + x 12 + 2x 22 + x 1 x 2   =   c + b'x + x'Ax
                                                                    2
              c=   30
                      1
             b=
      avec           -1 et B est bien symétrique. Donc f est bien quadratique.
                     2 1
             A=
                     1 4
   2) La matrice hessienne de f est A qui est symétrique définie positive (tr(A) > 0 et
      det(A) = 7 > 0). Donc f est strictement convexe.
~~~

## Page 3

~~~text
                                                                                             -5
                                                                         1 4 -1       1      7
   3) ∇f x * = 0 ⟺ Ax * + b = 0 ⟺ x * = - A -1 b = -                                     =        .
                                                                         7 -1 2       -1     3
                                                                                             7
                                          *
      La convexité stricte garantit que x est l'unique solution.
   4) Méthode de descente :
        a) d direction de descente à partir de x ⟺ < d, ∇f(x) > ⩽ 0.
        b) Définissons la fonction g(t) = f(x + td). Sa dérivée est donnée par :
                     g'(t) =< d, ∇f(x + td) > = d T (A(x + td) + b)
                             g'(t) = d T Ax + t d T Ad + d T b
                              g'(t) = d T (Ax + b) + t d T Ad
        Cette dérivée s'annule pour la valeur :
                                    d T (Ax + b)             d T ∇f(x)
                             t=-                       = -
                                         d T Ad               d T Ad
                *      d T ∇f(x)         d T (Ax + b)
        Donc 𝜌 = -                 = -                  .
                        d T Ad                d T Ad

        c) Dans le cas de la méthode du gradient, on choisit d = -∇f(x) = - (Ax + b).
                                                        *         d T ∇f(x)   ‖d‖ 2
          L'expression du pas optimal devient : 𝜌 = -         = T .
                                                    d T Ad       d Ad
                         1                         -3             9   1
              i) X 0 =       ⟹ d 0 = - (AX0 + b) =      et 𝜌 0 =    = .
                         0                         0             18 2
                                              -1
                 D'où : X 1 = X 0 + 𝜌 0 d 0 = 2 .
                                              0
                                                              9
                                              0                 1
                                                              4
              ii) d 1 = - (AX 1 + b) =        3   et 𝜌 1 =     = .
                                                              9 4
                                              2
                                                  -1
                D'où : X 2 = X 1 + 𝜌 1 d 1 =      2     .
                                                  3
                                                  8
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
~~~

## Page 4

~~~text
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
Réponses :
   1) On sait que lorsque f est convexe et différentiable, nous avons :
                        ∀x, y ∈ H      f(y) ⩾ f(x) + < ∇f(x), y - x >
   Si maintenant, x * vérifie la condition :
                             ∀x ∈ H, < ∇f x * , x - x * > ⩾ 0.
   La caractérisation de la convexité appliquée avec x = x * donne alors :
                 ∀y ∈ H      f(y) ⩾ f x * + < ∇f x * , y - x * > ⩾ f x *
   Donc f x * est un minimum global de f sur H.
   2) On cherche à résoudre (P).
        a) Soient x = (x 1 , x 2 )' et y = (y 1 , y 2 )' deux éléments de H et t ∈ [0, 1].
                            x1 + x2 ⩽ 4               y1 + y2 ⩽ 4
           On sait que :                   et
                            x 1 + 3x 2 ⩽ 9            y 1 + 3y 2 ⩽ 9
           On en déduit immédiatement que :
                    (tx 1 + (1 - t)y 1 + (tx 2 + (1 - t)y 2 ) ⩽ 4t + 4(1 - t) = 4
                    (tx 1 + (1 - t)y 1 + 3(tx 2 + (1 - t)y 2 ) ⩽ 9t + 9(1 - t) = 9
           Par conséquent le point tx + (1 - t)y appartient également à H.
           OU BIEN : Tout demi-plan est convexe, et H est l'intersection de 2 demi-plans.
           Donc H est convexe.
~~~

## Page 5

~~~text
b) Les coordonnées de x * vérifient les inéquations définissant H, donc x * ∈ H.
              2(x 1 - 4)                          -4
c) ∇f(x) =                   ⟹ ∇f x * =              .
              2(x 2 - 4)                          -4
                                     x1 + x2      ⩽4                   x1 - 2
  Si x = (x 1 , x 2 )' ∈ H, on a :                     et   x - x* =          .
                                     x 1 + 3x 2   ⩽9                   x2 - 2
  Donc : < ∇f x * , x - x * > = - 4(x 1 - 2) - 4(x 2 - 2) = 16 - 4(x 1 + x 2 )
                      < ∇f x * , x - x * > = - 4(x 1 + x 2 - 4) ⩾ 0.
  Donc x * vérifie la condition de la question 1, et par suite c'est un minimum global
  de de (P).
            -4       0
d) ∇f x * =      ≠      , mais cela n'a rien de surprenant. Il s'agit d'un
            -4       0
  minimum dans H qui n'est pas du tout ouvert (en fait fermé). La condition de
  nullité du gradient n'a donc pas lieu d'être ici.
~~~
