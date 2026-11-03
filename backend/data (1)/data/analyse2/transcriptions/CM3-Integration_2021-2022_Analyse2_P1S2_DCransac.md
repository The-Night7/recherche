# CM3-Integration_2021-2022_Analyse2_P1S2_DCransac.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1rL0dutoG2so2F_2-MRJnSwij7echGhSX) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




                                       Intégration
1   Intégrale d'une fonction en escalier
2   Intégrale d'une fonction continue (par morceaux)
3   Calcul Intégral
     Primitives     Z v (x)
     Étude de x 7→          f (t)dt
                                u(x)
      Intégration par partie
      Changement de variables
4   Recherche de primitives
      Intégration des éléments simples
      Intégration des fonctions trigonométriques
5   Approximations d'intégrales, sommes de Riemann

                                           D. Cransac     Analyse
~~~

## Page 2

~~~text
              Intégrale d'une fonction en escalier
 Intégrale d'une fonction continue (par morceaux)
                                   Calcul Intégral
                         Recherche de primitives
 Approximations d'intégrales, sommes de Riemann




Intégrale d'une fonction en escalier




                                      D. Cransac     Analyse
~~~

## Page 3

~~~text
                    Intégrale d'une fonction en escalier
       Intégrale d'une fonction continue (par morceaux)
                                         Calcul Intégral
                               Recherche de primitives
       Approximations d'intégrales, sommes de Riemann




Subdivision


  Dénition
  On appelle subdivision d'un segment [a, b] toute suite nie
  s = (x0 , x1 , . . . , xn ) de nombres réels tels que :

                                   a = x0 < x1 < · · · < xn = b.
                a                                                         b
               x0         x1 x2                  x3        x4    x5 . . . xn   x




                                            D. Cransac     Analyse
~~~

## Page 4

~~~text
                    Intégrale d'une fonction en escalier
       Intégrale d'une fonction continue (par morceaux)
                                          Calcul Intégral
                               Recherche de primitives
       Approximations d'intégrales, sommes de Riemann




Fonction en escalier
  Dénition (Fonction en escalier, subdivision adaptée)
  On dit qu'une fonction f : [a, b] −→ C est en escalier si pour une
  certaine subdivision (x0 , . . . , xn ) de [a, b], dite adaptée à f on a
            Pour tout i ∈ J0, n − 1K, f est constante sur ]xi , xi+1 [ .
                          y
                                     y1


                                                                 y4
                                             y2
                                                                                         x
                              a = x0 x1 x2                  x3        x4    x5 . . . xn = b

                                                       y3
                                                                           y5

                                             D. Cransac      Analyse
~~~

## Page 5

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Notation Au besoin on utilisera la notation

                   E[a;b] = {φ : [a; b] → R en escalier sur [a; b] }

Théorème (Propriétés élémentaires des fonctions en escalier)
Soient f : [a, b] −→ C et g : [a, b] −→ C en escalier.
     Lorsqu'on ajoute un nombre ni de points à une subdivision de [a, b]
     adaptée à f , le résultat est encore une subdivision de [a, b] adaptée à
     f.
     A fortiori, la réunion d'une subdivision de [a, b] adaptée à f et d'une
     subdivision de [a, b] adaptée à g est une subdivision de [a, b]
     adaptée à f ET à g .
     Pour tous λ, µ ∈ C, λf + µg est une fonction en escalier sur [a, b],
     de même que |f |, Re(f ), Im(f ) et fg .


                                          D. Cransac     Analyse
~~~

## Page 6

~~~text
                    Intégrale d'une fonction en escalier
       Intégrale d'une fonction continue (par morceaux)
                                         Calcul Intégral
                               Recherche de primitives
       Approximations d'intégrales, sommes de Riemann




Théorème (Intégrale d'une fonction en escalier)
Soit f : [a, b] −→ en escalier.
Soit en outre (x0 , . . . , xn ) une subdivision de [a, b] adaptée à f .
Si pour tout i ∈ [0, n − 1], on note yi la valeur de f sur ]xi , xi+1 [, alors le
                              n−1
nombre complexe :                   yi (xi+1 − xi ) ne dépend pas de la subdivision
                              X

                              i=0
(x0 , . . . , xn ) choisie.
                                       y1


                                                                      y4
                                               y2


                                  x0        x1 x2                x3        x4    x5

                                                           y3
                                                                                y5

                                            D. Cransac          Analyse
~~~

## Page 7

~~~text
                   Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                              Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Dénition
La valeur du théorème précédent est appelée intégrale de f sur [a, b],
          Z               Z                          Z b
notée :            f ou             f (t)dt ou                 f (t)dt .
           [a,b]            [a,b]                         a

                                      y1


                                                                      y4
                                              y2


                                 x0        x1 x2                 x3        x4    x5

                                                          y3
                                                                                y5




                                           D. Cransac           Analyse
~~~

## Page 8

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                               Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Théorème (Propriétés de l'intégrale d'une fonction en escalier)
Soient f : [a, b] −→ C et g : [a, b] −→ C en escalier.
 1
     Linéarité : ZPour tous           Z        Z
     λ, µ ∈ C :       (λf + µg ) = λ     f +µ        g.
                       [a,b]                             [a,b]                   [a,b]
                                           Z                Z
 2
     Inégalité triangulaire :                        f ⩽                 |f |.
                                             [a,b]               [a,b]
 3
     Relation deZChasles :ZPour toutZ
     c ∈ [a, b] :               f =              f +             f.
                        [a,b]            [a,c]           [c,b]
 4
     Lien avec Zles parties réelles
     Z                           Z et imaginaires :
          f =        Re(f ) + i      Im(f ).
      [a,b]           [a,b]                      [a,b]




                                           D. Cransac       Analyse
~~~

## Page 9

~~~text
                       Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                              Calcul Intégral
                                  Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Démonstration.
Donnons-nous λ, µ ∈ C, c ∈ [a, b] et une subdivision (x0 , . . . , xn ) de [a, b]
adaptée à f ET à g - mais donc aussi à λf + µg , |f |, Re(f ) et Im(f ).
                                                         Valeur de λf +µg
                                        n−1
      Z                                           z          }|
                                                                        {
                                        X                      xi + xi+1
  1
             (λf + µg ) =                         (λf + µg )               (xi+1 − xi )
       [a,b]                            i=0
                                                                          2
           n−1                                                   n−1            
           X                xi + xi+1                              X     xi + xi+1
      =λ           f                              (xi+1 − xi ) + µ    g              (xi+1 − xi )
                                  2                                             2
            Zi=0                  Z                                       i=0

      =λ                f +µ                  g
              [a,b]                   [a,b]




                                                   D. Cransac   Analyse
~~~

## Page 10

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                               Calcul Intégral
                               Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Démonstration.

  2   D'après l'inégalité triangulaire sur C :
                               Z                        n−1 
                                                        X     xi + xi+1 
                                           f =             f              (xi+1 − xi )
                                   [a,b]                i=0
                                                                         2
                               n−1              x + x                                 Z
                                                            i+1
                                                                  
                                                    i
                               X
                           ⩽               f                          (xi+1 − xi ) =               |f |.
                               i=0
                                                        2                                  [a,b]




                                                  D. Cransac          Analyse
~~~

## Page 11

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                          Calcul Intégral
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Démonstration.

  3   Quitte à ajouter le point c à la subdivision (x0 , . . . , xn ), on peut supposer
      que : xk = c pour un certain k ∈ [0, n].
      La fonction f[a,c] est alors en escalier sur [a, c] de subdivision adaptée
      (x0 , . . . , xk ), et la fonction f[c,b] l'est sur [c, b] de subdivision adaptée
      (xk , . . . , xn ).
      Enn :                    Z         n−1    X  xi + xi+1 
                                          f =     f              (xi+1 − xi )
                                  [a,b]          i=0
                                                                  2
                 k−1                             n−1 
                 X     xi + xi+1                 X     xi + xi+1 
             =      f              (xi+1 − xi ) +    f              (xi+1 − xi )
                  i=0
                                  2                                   i=k
                                                                                   2
                                                      Z               Z
                                                  =             f +            f
                                                        [a,c]          [c,b]




                                             D. Cransac         Analyse
~~~

## Page 12

~~~text
                     Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                             Calcul Intégral
                                   Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Démonstration.

  4   Cela découle de la linéarité de l'intégrale pour λ = 1 et µ = i .
      On peut aussi le démontrer directement :
      Z              n−1 
                     X     xi + xi+1 
               f =      f              (xi+1 − xi )
       [a,b]         i=0
                                         2
          n−1              x + x                                           n−1              x + x
                                         i+1                                                             i+1
                                                                                                              
                               i                                                                 i
          X                                                                 X
      =         Re(f )                             (xi+1 − xi ) + i                Im(f )                          (xi+1 − xi )
          i=0
                                     2                                      i=0
                                                                                                     2
                                                   Z                        Z
                                             =                 Re(f ) + i               Im(f )
                                                       [a,b]                    [a,b]




                                                 D. Cransac          Analyse
~~~

## Page 13

~~~text
               Intégrale d'une fonction en escalier
  Intégrale d'une fonction continue (par morceaux)
                                    Calcul Intégral
                          Recherche de primitives
  Approximations d'intégrales, sommes de Riemann




Intégrale d'une fonction continue
(par morceaux)




                                       D. Cransac     Analyse
~~~

## Page 14

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Théorème
Soient f : [a, b] → R continue sur [a, b] et ε > 0.
Alors il existe θ : [a, b] → R en escalier telle que
                                ∀x ∈ [a, b], |f (x) − θ(x)| ⩽ 

Démonstration.
Admis.

                                                                    = 0.2




                                          D. Cransac     Analyse
~~~

## Page 15

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Proposition
Soit f : [a, b] → R continue sur [a, b].
Pour tout ε > 0, il existe deux fonctions ϕ, ψ ∈ E([a, b], R) telles que :
                            ϕ⩽f ⩽ψ                 et    0 ⩽ ψ − ϕ ⩽ ε.


                                                                    = 0.2




                                          D. Cransac     Analyse
~~~

## Page 16

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
    Approximations d'intégrales, sommes de Riemann




                                                                    = 0.2




Démonstration.
D'après le théorème précédent, on a θ en escaliers telle que
                                                         
∀x ∈ [a, b], |f (x) − θ(x)| ⩽ . θ(x) − ⩽ f (x) ⩽ θ(x) + . On pose
                              2        2             
                                                           2
alors les fonctions en escalier ϕ = θ − et ψ = θ + pour obtenir le
                                        2            2
résultat.
                                          D. Cransac     Analyse
~~~

## Page 17

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann



On suppose à présent que f : [a, b] → R est une fonction bornée
quelconque.
Théorème
Si f : [a, b] → R est continue, alors :
                        (Z                                             )
                                 b
  1
      A−
       [a,b] (f ) =                  φ(x)dx | φ en escalier et φ ⩽ f       admet une borne
                             a
      supérieure,
                        (Z                                             )
                                 b
  2
      A+
       [a,b] (f ) =                  ψ(x)dx | ψ en escalier et f ⩽ ψ       admet une
                             a
      borne inférieure, et ces deux bornes sont égales.
Notation Au besoin on utilisera les notations
                −
               E[a;b] (f ) = {φ en escalier sur [a; b] telle que φ ⩽ f }

               +
              E[a;b] (f ) = {ψ en escalier sur [a; b] telle que f ⩽ ψ}
                                           D. Cransac     Analyse
~~~

## Page 18

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Démonstration.
La fonction f étant continue sur le segment [a, b], elle est bornée sur
[a, b].
Posons m = inf f (x) et M = sup f (x).
                 x∈[a,b]                          x∈[a,b]

    A−       est non vide puisqu'il contient la fonction constante m.
     [a,b] (f )
    Ainsi  A−     est une partie non vide de R.
             [a,b] (f )
    De plus pour tout ϕ ∈ A− [a,b] (f ), on a ϕ ⩽ f ⩽ M .
    Donc :            Z            Z
                                             ϕ⩽                  M = M(b − a).
                                     [a,b]               [a,b]

    L'ensemble A− [a,b] (f ) est donc une partie non vide de R et majorée
    (par M(b − a) ). Il possède donc une borne supérieure que l'on note
    α.
    De même, A+[a,b] (f ) est une partie non vide de R et minorée par
    m(b − a). Il possède donc une borne inférieure que l'on note β .

                                          D. Cransac             Analyse
~~~

## Page 19

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Démonstration.
   Supposons β < α.
   Alors, comme α estZ la borne sup de A− , il existe φ en escalier tel
   que φ ⩽ f et β <        ϕ < α.
                                    [a,b]
    Alors pour toute fonction ψ en escalier tel que f ⩽ ψ , on a
                                                    ϕ⩽f ⩽ψ

    donc                                       Z              Z
                                                         ϕ⩽           ψ
                                                 [a,b]        [a,b]
             Z                                                            Z
    Donc                ϕ ⩽ β Ce qui est contradictoire avec β <                  ϕ. Donc
                [a,b]                                                     [a,b]
    α⩽β



                                            D. Cransac    Analyse
~~~

## Page 20

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Autre démonstration
Démonstration.
   Puisque pour tout ϕ en escalier
                                 Z telle queZ ϕ ⩽ f et ψ en escalier telle
   que f ⩽ ψ , on a ϕ ⩽ ψ , on a       ϕ⩽        ψ.
             Z                                           [a,b]        [a,b]

    Ainsi       ψ est un majorant de A (f ), la borne supérieure α de
                                                                 −
               [a,b]                 Z
    A− (f ) est donc plus petite que    ψ.
                                                            [a,b]
    On obtient :
                                                                              Z
        Pour toute fonction en escalier ψ telle que f ⩽ ψ, α ⩽                        ψ
                                                                              [a,b]


    De même, α est un minorant de A+[a,b] (f ), et β est le plus grand des
    minorants de cette partie. Donc α ⩽ β .

                                          D. Cransac        Analyse
~~~

## Page 21

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Démonstration.
   Soit  > 0.
   On sait qu'il existe ϕ ∈ E[a;b]
                             −
                                   (f ) et ψ ∈ E[a;b]
                                                −
                                                      (f ) telles que
   φ ⩽ f ⩽ ψ telles que pour tout x ∈ [a, b], ψ(x) − ϕ(x) ⩽ .
   On a alors :         Z            Z
                                               ψ−                ϕ ⩽ (b − a)
                                       [a,b]             [a,b]

     Or par dénition de α et β , on a :
                                      Z                               Z
                                                 ϕ⩽α⩽β⩽                            ψ
                                         [a,b]                             [a,b]

     D'où pour tout ε > 0,
     on a                  Z                                      Z
                 0⩽β−α⩽                                    ψ−              ϕ ⩽ (b − a)
                                                   [a,b]           [a,b]

     Finalement, on a bien α = β .

                                          D. Cransac        Analyse
~~~

## Page 22

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Dénition
Soit f : [a, b] → R une fonction continue.               Z
On appelle intégrale de f sur [a, b] le nombre réel noté                                       f déni par :
                                                                                       [a,b]

 Z                    (Z                                  )           (Z                                )
                                            −                                             +
           f = sup                 ϕ | ϕ ∈ E[a,b] (f )        = inf              ψ | ψ ∈ E[a,b] (f )
   [a,b]                   [a,b]                                         [a,b]


Proposition (Linéarité)
Soient f , g : [a, b] → R continues et (λ, µ) ∈ R2 .
                          Z                               Z              Z
                                    (λf + µg ) = λ                f +µ             g
                            [a,b]                         [a,b]            [a,b]




                                           D. Cransac     Analyse
~~~

## Page 23

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                           Calcul Intégral
                              Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Proposition (Lemme)
Soit ε > 0.
Si f : [a, b] → R continue et θ ∈ E[a,b] telles que |f − θ| ⩽ ε, alors
                                   Z                         Z
                                                 f −                     θ ⩽ (b − a)ε
                                         [a,b]               [a,b]


Démonstration.

On a θ − ε ⩽ f ⩽ θ + ε, d'où (par dénition de l'intégrale) :
                             Z                                   Z                   Z
                                         (θ − ε) ⩽                           f ⩽               (θ + ε)
                                 [a,b]                               [a,b]             [a,b]

Par linéarité de l'intégrale des fonctions en escalier :
                             Z                   Z                       Z
                                         f −                 θ ⩽                     ε ⩽ (b − a)ε.
                               [a,b]                 [a,b]                   [a,b]



                                                 D. Cransac                  Analyse
~~~

## Page 24

~~~text
                     Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                          Calcul Intégral
                                Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Démonstration.
On dénit
    θ1 tel que |f − θ1 | < 
    θ2 tel que |g − θ2 | < 
    h = λf + µg
    θ = λθ1 + µθ2
        Z         Z                                  Z
    I =      θ=λ                          θ1 + µ                θ2 (par linéarité pour les fonctions
             [a,b]                [a,b]                [a,b]
    en escalier).
On a :
                 |h − θ| ⩽ |λ(f − θ1 ) + µ(g − θ2 | ⩽ (|λ| + |µ|)ε
Par le lemme :
            Z                             Z                 Z
                       h−I ⩽                       h−               θ ⩽ (b − a)(|λ| + |µ|)ε
               [a,b]                       [a,b]            [a,b]


                                              D. Cransac        Analyse
~~~

## Page 25

~~~text
                  Intégrale d'une fonction en escalier
    Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                             Recherche de primitives
    Approximations d'intégrales, sommes de Riemann




Démonstration.
On a : Z       Z
     λ            f +µ                 g −I
          [a,b]              [a,b]
         Z                 Z                    Z                   Z
⩽    λ            f +µ                 g −λ               θ1 − µ                θ2
          [a,b]              [a,b]                [a,b]                 [a,b]
             Z             Z                !             Z              Z             !
⩽    λ               f −               θ1       +µ                g−              θ2
             [a,b]             [a,b]                      [a,b]           [a,b]

⩽ |λ|(b − a)ε + |µ|(b − a)ε

⩽ (b − a)(|λ| + |µ|)ε



                                            D. Cransac        Analyse
~~~

## Page 26

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                         Calcul Intégral
                                 Recherche de primitives
    Approximations d'intégrales, sommes de Riemann




Démonstration.
Finalement on obtient :
                    Z                                      Z                    Z                !
          ∆=                    (λf + µg ) −           λ           f +µ                      g
                      [a,b]                                [a,b]                     [a,b]
                    Z                                                    Z                       Z               !
              =                 (λf + µg ) − I +               I −λ                  f −µ                    g
                      [a,b]                                                  [a,b]                   [a,b]
                    Z                                                    Z                       Z               !
              =                 (λf + µg ) − I + I − λ                               f −µ                    g
                        [a,b]                                            [a,b]                       [a,b]

              ⩽ 2(b − a)(|λ| + |µ|)ε.

Comme c'est vrai quelque soit ε > 0, on en déduit ∆ = 0, et donc la
linéarité de l'intégrale.


                                             D. Cransac        Analyse
~~~

## Page 27

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                               Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Proposition (Relation de Chasles)
Soient f : [a, b] → R continues et c ∈ [a, b].
                                   Z                 Z                  Z
                                               f =                f +               f.
                                      [a,b]           [a,c]                 [c,b]


Démonstration.
Soit ϕ ∈ E[a,b]
          −
                (f ).
On a alors :
                                       −
                             ϕ[a,c] ∈ E[a,c] (f ) et ϕ[c,b] ∈ E[c,b]
                                                               −
                                                                     (f ).
Par dénition de l'intégrale, on obtient :
                   Z                Z                Z                      Z              Z
                             ϕ=                ϕ+                 ϕ⩽                 f +           f
                     [a,b]             [a,c]              [c,b]              [a,c]         [c,b]




                                           D. Cransac             Analyse
~~~

## Page 28

~~~text
                     Intégrale d'une fonction en escalier
        Intégrale d'une fonction continue (par morceaux)
                                            Calcul Intégral
                                  Recherche de primitives
        Approximations d'intégrales, sommes de Riemann




Démonstration.
        Z               Z
Ainsi             f +             f est un majorant de A−
                                                        [a,b] (f ).
          [a,c]           [c,b]
Par dénition de la borne supérieure :
                                       Z                 Z                  Z
                                                   f ⩽                f +               f
                                         [a,b]                [a,q]             [c,b]

En appliquant (linéarité) ce résultat à −f , on en déduit l'inégalité
inverse, et donc :      Z          Z         Z
                                                   f =                f +               f
                                           [a,b]              [a,c]             [c,b]




                                               D. Cransac             Analyse
~~~

## Page 29

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                               Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Notation.
Soient a et b deux réels quelconques (en particulier on ne suppose plus
nécessairement a < b).
Soit f une fonction
                  Z bcontinue entre a et b .
On dénit le réel     f (x)dx par :
                           a
                  Z b                     Z
     si a < b,           f (x)dx =                   f (x)dx ;
                     a                       [a,b]
                  Z b
     si a = b,           f (x)dx = 0 ;
                     a
                  Z b                         Z
     si b < a,           f (x)dx = −                     f (x)dx .
                     a                          [b,a]
La relation de Chasles et la linéarité sont alors vraies pour a, b, c
quelconques.

                                           D. Cransac       Analyse
~~~

## Page 30

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                          Calcul Intégral
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Proposition
Soient f , g : I → R continues sur un intervalle I et a, b ∈ I .
                                   Z b
  1
      f ⩾ 0 et a ⩽ b ⇒                      f (x)dx ⩾ 0                      (positivité de l'intégrale)
                                     a
                                   Z b                          Z b
  2
      f ⩽ g et a ⩽ b ⇒                      f (x)dx ⩽                 g (x)dx (passage aux inégalités)
                                      a                          a
                     Z b                        Z b
  3
      a⩽b⇒                  f (x)dx ⩽                  |f (x)|dx (inégalité de la norme)
                       a                          a
  4
      Si a ⩽ b et m ⩽ f ⩽ M entre a et b, alors
                                                      Z b
                               m(b − a) ⩽                       f (x)dx ⩽ M(b − a)
                                                            a
      .
Attention Bien vérier a < b.
                                             D. Cransac          Analyse
~~~

## Page 31

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                        Calcul Intégral
                               Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Démonstration.
  1
   Puisque f ⩾ 0, alors ϕ = 0 est une fonction en escalier sur [a, b]
   telle que ϕ ⩽ f .
   Par dénition de l'intégrale de f sur [a, b], on en déduit que
                                    Z b                    Z b
                                           f (x)dx ⩾               ϕ(x)dx = 0.
                                      a                        a

  2
      On applique le point précédent à la fonction h = g − f ⩾ 0 :
                         Z b                              Z b               Z b
                               h(x)dx ⩾ 0 ⇒                     g (x)dx ⩾         f (x)dx
                           a                               a                 a

      par linéarité de l'intégrale.



                                           D. Cransac          Analyse
~~~

## Page 32

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                            Calcul Intégral
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Démonstration.
  3
   On a pour tout x ∈ [a, b], −|f (x)| ⩽ f (x) ⩽ |f (x)|. D'où par
   croissance de l'intégrale :
                             Z b                              Z b                    Z b
                         −         |f (x)|dx ⩽                      f (x)dx ⩽              |f (x)|dx
                               a                               a                       a

                                   Z b                             Z b
      Ainsi, on obtient                      f (x)dx ⩽                       |f (x)|dx .
                                     a                              a
  4
      Il sut de prendre l'intégrale dans les inégalités m ⩽ f ⩽ M .

Remarque. La majoration suivante, vraie également si b < a, peut être
utile :            Z                Z   b                                b
                                            f (x)dx ≤                        |f (x)| dx
                                    a                                a


                                               D. Cransac           Analyse
~~~

## Page 33

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Dénition
La valeur moyenne d'une fonction f : [a, b] → R continue est :
                                                         1
                                                             Z
                                          µ=                             f
                                                  b−a            [a,b]

Remarque. La valeur moyenne est la constante µ qui vérie
                                           Z                 Z
                                                     f =               µ
                                             [a,b]            [a,b]




                                          D. Cransac         Analyse
~~~

## Page 34

~~~text
                    Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                         Calcul Intégral
                               Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Proposition
Soit f : [a, b] → R une fonction continue sur [a, b] et positive alors
                Z
                          f = 0 si et seulement si f est nulle sur [a, b].
                  [a,b]

Démonstration.

⇐ Si f est nulle, son intégrale est nulle.
⇒ Par contraposition, supposons que f n'est pas nulle sur [a, b] : ∃c ∈ [a, b] tel que
f (c) > 0.
                                                         f (c)
D'après la dénition de la continuité de f en c avec ε =       :
                                                                           2
                ∃a ⩽ α < β ⩽ b, ∀x ∈ [a, b], x ∈ [α, β] ⇒ |f (x) − f (c)| ⩽ ε
                                                      `(c)
Ainsi pour tout x ∈ [α, β], on a f (x) ⩽    .
                                          2
En prenant l'intégrale, on en déduit donc que :
                    Z b                  Z β                 Z β
                          f (x)dx ⩾            f (x)dx ⩾           εdx = (β − α)ε > 0.
                      a                   α                   α


                                            D. Cransac       Analyse
~~~

## Page 35

~~~text
                     Intégrale d'une fonction en escalier
       Intégrale d'une fonction continue (par morceaux)
                                          Calcul Intégral
                                Recherche de primitives
       Approximations d'intégrales, sommes de Riemann




Remarque. Si f n'est pas supposée continue, le résultat est faux : par
exemple f (x) = 0 sur ]0, 1[ et f (0) = f (1) = 1 est positive, non nulle
    Z        1
mais             f = 0.
         0




                                             D. Cransac     Analyse
~~~

## Page 36

~~~text
             Intégrale d'une fonction en escalier
                                                    Primitives        Z v (x)
Intégrale d'une fonction continue (par morceaux)
                                                    Étude de x   7→             f (t)dt
                                  Calcul Intégral
                                                                     u(x)
                                                    Intégration par partie
                        Recherche de primitives
                                                    Changement de variables
Approximations d'intégrales, sommes de Riemann




                           Calcul intégral




                                     D. Cransac     Analyse
~~~

## Page 37

~~~text
                  Intégrale d'une fonction en escalier
                                                         Primitives        Z v (x)
     Intégrale d'une fonction continue (par morceaux)
                                                         Étude de x   7→             f (t)dt
                                       Calcul Intégral
                                                                          u(x)
                                                         Intégration par partie
                             Recherche de primitives
                                                         Changement de variables
     Approximations d'intégrales, sommes de Riemann




Dénition
Soient I un intervalle et f : I 7→ K une fonction continue.
On appelle primitive de f sur I toute fonction F de classe C 1 sur I dont
la dérivée est f .

Proposition (Lien entre deux primitives d'une même fonction)
Deux primitives d'une même fonction sur un intervalle dièrent d'une
constante c'est à dire :
Si F1 et F2 sont des primitives de f alors

                                      ∃C ∈ K, F1 − F2 = C

Démonstration.
Si F1 et F2 sont deux primitives de la fonction F sur I , alors
(F1 − F2 ) = F10 − F20 = f − f = 0 donc la fonction F1 − F2 est constante
          0

sur I .
                                          D. Cransac     Analyse
~~~

## Page 38

~~~text
                   Intégrale d'une fonction en escalier
                                                          Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                          Étude de x   7→             f (t)dt
                                        Calcul Intégral
                                                                           u(x)
                                                          Intégration par partie
                              Recherche de primitives
                                                          Changement de variables
      Approximations d'intégrales, sommes de Riemann




Proposition (Théorème fondamental de l'analyse)
Soient I un intervalle de R, f : I → K une fonction continue, et a ∈ I .
                                I        → K
      La fonction F :                                  est l'unique primitive de f
                                           Z x
  1

                                x      7 →     f (t)dt
                                                 a
      s'annulant en a.
  2
      Pour toute primitive F : I → K de f , on a
                                        Z x
                                              f (t)dt = F (x) − F (a)
                                          a




                                           D. Cransac     Analyse
~~~

## Page 39

~~~text
                   Intégrale d'une fonction en escalier
                                                              Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                              Étude de x   7→             f (t)dt
                                        Calcul Intégral
                                                                               u(x)
                                                              Intégration par partie
                              Recherche de primitives
                                                              Changement de variables
      Approximations d'intégrales, sommes de Riemann




Démonstration.
  1
   La fonction F est dénie pour tout x ∈ I car f est continue sur [a, x]
   ou [x, a] (selon que x ⩾ a ou x ⩽ a).
   Soit x0 ∈ I , montrons que F est dérivable en x0 et que
   F 0 (x0 ) = f (x0 ).
   On a pour tout x ∈ I :
                                                1
                                                                           Z x
                  F (x) − F (x0 )
                                  − f (x0 ) =                                        f (t)dt − f (x0 )
                      x − x0                  x − x0
                                                                           Z 0x
                                                                            x
                                                                   1
                                                          =                          f (t) − f (x0 ) dt
                                                              x − x0            x0

      D'où avec l'inégalité de la moyenne (on vérie que cette inégalité est
      aussi vraie si x < x0 ) :
                                               1
                                                                           Z x
                 F (x) − F (x0 )
                                 − f (x0 ) =                                         |f (t) − f (x0 )| dt
                     x − x0                  x − x0                             x0

                                               A suivre
                                           D. Cransac         Analyse
~~~

## Page 40

~~~text
                   Intégrale d'une fonction en escalier
                                                          Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                          Étude de x   7→             f (t)dt
                                        Calcul Intégral
                                                                           u(x)
                                                          Intégration par partie
                              Recherche de primitives
                                                          Changement de variables
      Approximations d'intégrales, sommes de Riemann




Démonstration.
  1
   (suite) Or f est continue en x0 , donc :
             ∀ε > 0, ∃α > 0, ∀t ∈ I , |t − x0 | ⩽ α ⇒ |f (t) − f (x0 )| ⩽ ε.

      Alors pour tout x ∈ I , |x − x0 | ⩽ α, on a pour tout
      t ∈ [x0 , x] , |f (t) − f (x0 )| ⩽ ε et en reportant :

                                                      1
                                                          Z x
                      F (x) − F (x0 )
                                       − f (x0 ) =            εdt ⩽ ε.
                          x − x0                   x − x0 x0

                                                0   F (x) − F (x )
      Ainsi on a montré que lim                    = f (x0 ). Donc F est
                               x→x0     x − x0
      dérivable en x0 et F (x0 ) = f (x0 ). Puisque c'est vrai pour tout
                            0

      x0 ∈ I et que f est continue, on en déduit nalement que F est de
      classe C 1 et que F 0 = f .
                                  A suivre

                                           D. Cransac     Analyse
~~~

## Page 41

~~~text
                   Intégrale d'une fonction en escalier
                                                              Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                              Étude de x   7→             f (t)dt
                                        Calcul Intégral
                                                                               u(x)
                                                              Intégration par partie
                              Recherche de primitives
                                                              Changement de variables
      Approximations d'intégrales, sommes de Riemann




Démonstration.
  1
   (suite)
   Reste à montrer que F est l'unique primitive de f qui s'annule en a.
   Si G satisfait aussi ces propriétés, alors on a vu qu'il existe C ∈ K
   tel que F = G + C .
   En évaluant en x = a, on obtient C = 0, et donc F = G .
  2
   Soit h : x 7→ F (x) − F (a). Alors h est dérivable sur I comme
   combinaison linéaire de fonctions qui le sont, et pour
   x ∈ I , h0 (x) = F 0 (x) = f (x). De plus h(a) = 0, donc h est une
   primitive de f s'annulant en aZ. D'après l'unicité du point précédent,
                                       x
   on a pour tout x ∈ I , h(x) =         f (t)dt . D'où le résultat.
                                                          a




                                           D. Cransac         Analyse
~~~

## Page 42

~~~text
                  Intégrale d'une fonction en escalier
                                                         Primitives        Z v (x)
     Intégrale d'une fonction continue (par morceaux)
                                                         Étude de x   7→             f (t)dt
                                       Calcul Intégral
                                                                          u(x)
                                                         Intégration par partie
                             Recherche de primitives
                                                         Changement de variables
    Approximations d'intégrales, sommes de Riemann




Notations.             Z
    Le symbole f (x)dx (introduit par Leibniz) désigne une primitive
    quelconque de f . Elle est donc dénie à une constante additive près.
                                Z x
    La fonction x 7→                  f (t) dt est la primitive de f s'annulant en a.
                                  a




                                          D. Cransac     Analyse
~~~

## Page 43

~~~text
                    Intégrale d'une fonction en escalier
                                                           Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                           Étude de x   7→             f (t)dt
                                         Calcul Intégral
                                                                            u(x)
                                                           Intégration par partie
                               Recherche de primitives
                                                           Changement de variables
      Approximations d'intégrales, sommes de Riemann




Proposition
Soient I , J deux intervalles de R, u, v : I → R de classe C 1 telles que
u(I ), v (I ) ⊂ J et f : J → K continue. Alors la fonction
           Z v (x)
g : x 7→             f (t)dt est dénie sur I , de classe C 1 et
             u(x)

                    ∀x ∈ I , g 0 (x) = f (v (x))v 0 (x) − f (u(x))u 0 (x).

Démonstration.

Pour tout x ∈ I , on a u(x), v (x) ∈ J et J est un intervalle. Donc [u(x), v (x)] ⊂ J et
g (x) existe pour tout x ∈ I .
La fonction f : J → K étant continue sur J , elle admet une primitive F de classe C 1
sur J . On a alors pour tout x ∈ I ,
                                       g (x) = F (v (x)) − F (u(x))
La fonction g est donc de classe C 1 en tant que diérence et composées de fonctions
de classe C 1 , et pour tout x ∈ I , on a :
                                g 0 (x) = v 0 (x)f (v (x)) − u 0 (x)f (u(x))

                                            D. Cransac     Analyse
~~~

## Page 44

~~~text
                  Intégrale d'une fonction en escalier
                                                            Primitives        Z v (x)
     Intégrale d'une fonction continue (par morceaux)
                                                            Étude de x   7→             f (t)dt
                                          Calcul Intégral
                                                                             u(x)
                                                            Intégration par partie
                                 Recherche de primitives
                                                            Changement de variables
     Approximations d'intégrales, sommes de Riemann




Proposition (Intégration par parties)
Soient f et g sont deux fonctions de classe C 1 sur [a, b] à valeur dans K.
                 Z b                                                     Z b
                           0
                       f       (t)g (t)dt = [f (t)g (t)]ba −                    f (t)g 0 (t)dt
                   a                                                      a


Démonstration.
On a
   Z b                            Z b                         Z b
         f 0 (t)g (t)dt +                 f (t)g 0 (t)dt =            (f 0 (t)g (t) + f (t)g 0 (t)) dt
    a                                a                          a
                                         Z b
                                  =            (fg )0 (t)dt = [f (t)g (t)]ba
                                          a
                       1
puisque fg est C comme produit de fonctions qui le sont.

                                               D. Cransac   Analyse
~~~

## Page 45

~~~text
                  Intégrale d'une fonction en escalier
                                                         Primitives        Z v (x)
     Intégrale d'une fonction continue (par morceaux)
                                                         Étude de x   7→             f (t)dt
                                       Calcul Intégral
                                                                          u(x)
                                                         Intégration par partie
                             Recherche de primitives
                                                         Changement de variables
     Approximations d'intégrales, sommes de Riemann




Démonstration.
(suite) On a
   Z b                         Z b                         Z b
         f 0 (t)g (t)dt +              f (t)g 0 (t)dt =            (f 0 (t)g (t) + f (t)g 0 (t)) dt
    a                             a                          a
                                      Z b
                               =            (fg )0 (t)dt = [f (t)g (t)]ba
                                       a

puisque fg est C 1 comme produit de fonctions qui le sont.




                                            D. Cransac   Analyse
~~~

## Page 46

~~~text
                    Intégrale d'une fonction en escalier
                                                                  Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                                  Étude de x   7→             f (t)dt
                                         Calcul Intégral
                                                                                   u(x)
                                                                  Intégration par partie
                               Recherche de primitives
                                                                  Changement de variables
     Approximations d'intégrales, sommes de Riemann




Proposition (Changement de variable)
Soient I un intervalle de R et f : I → K une fonction continue sur I .
Soient ϕ : [a, b] → I une fonction de classe C 1 sur [a, b]. Alors
                             Z ϕ(b)                        Z b
                                       f (x)dx =                  f (ϕ(t))ϕ0 (t)dt.
                              ϕ(a)                           a

On dit qu'on a eectué le changement de variables x = ϕ(t).

Démonstration.

Si F est une primitive de f , alors F ◦ ϕ est une primitive de f ◦ ϕ × ϕ0 et on a :
                    Z ϕ(b)
                              f (x)dx = [F (x)]ϕ(a) = F (ϕ(b)) − F (ϕ(a)).
                                                           ϕ(b)

                      ϕ(a)
              Z b
                    f ◦ ϕ(t)ϕ0 (t)dt = [F ◦ ϕ(t)]ba = F (ϕ(b)) − F (ϕ(a)).
                a




                                            D. Cransac            Analyse
~~~

## Page 47

~~~text
                    Intégrale d'une fonction en escalier
                                                            Primitives        Z v (x)
      Intégrale d'une fonction continue (par morceaux)
                                                            Étude de x   7→             f (t)dt
                                         Calcul Intégral
                                                                             u(x)
                                                            Intégration par partie
                               Recherche de primitives
                                                            Changement de variables
      Approximations d'intégrales, sommes de Riemann



En pratique, il faut modier trois éléments
    la variable x = φ(t),
    l'élément diérentiel dx = φ0 (t)dt ,
    les bornes de l'intégrale : si t varie entre a et b, x = φ(t) doit varier
    entre φ(a) et φ(b).
Proposition
Soit f : R → K une fonction continue.
  1
     si f est périodique de période T , alors pour tous a, b ∈ R :
              Z b                    Z b+T                  Z a+T                            Z b+T
                     f (t)dt =                   f (t)dt,                f (t)dt =                          f (t)dt
                a                       a+T                  a                                    b

  2
      si f est une fonction
                       Z a paire, alors pour tout a ∈ R :
      Z  a
           f (t)dt = 2    f (t)dt .
       −a                        0
                                                                                                      Z a
  3
      si f est une fonction impaire, alors pour tout a ∈ R :                                                f (t)dt = 0.
                                                                                                       −a

                                            D. Cransac      Analyse
~~~

## Page 48

~~~text
             Intégrale d'une fonction en escalier
Intégrale d'une fonction continue (par morceaux)
                                                    Intégration des éléments simples
                                  Calcul Intégral
                                                    Intégration des fonctions trigonométriques
                        Recherche de primitives
Approximations d'intégrales, sommes de Riemann




            Recherche de primitives




                                     D. Cransac     Analyse
~~~

## Page 49

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                                         Intégration des éléments simples
                                       Calcul Intégral
                                                         Intégration des fonctions trigonométriques
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Rappelons au cas où que nous savons primitiver aisément un certain
nombre de fonctions classiques :
     les fonctions de la forme x 7−→ eax cos(bx) ou x 7−→ eax sin(bx) avec
     a, b ∈ R∗ grâce à l'exponentielle complexe,
     les fonctions de la forme x 7−→ sinm x cosn x avec m, n ∈ N par
     linéarisation,
     les fonctions rationnelles par décomposition en éléments simples.
Les tableaux ci-dessous donnent enn la liste des quelques primitives qu'il
faut connaitre à tout prix.
                                       Fonction           Primitive
                                          ex                 ex
                                           ln x           x ln x − x
                                             1
                                                              ln |x|
                                             x
                                                             x α+1
                                    x α (α 6= −1)
                                                             α+1

                                          D. Cransac     Analyse
~~~

## Page 50

~~~text
                      Intégrale d'une fonction en escalier
         Intégrale d'une fonction continue (par morceaux)
                                                             Intégration des éléments simples
                                           Calcul Intégral
                                                             Intégration des fonctions trigonométriques
                                 Recherche de primitives
         Approximations d'intégrales, sommes de Riemann




Intégration des éléments simples
         P(x)
  Soit        une fraction rationnelle, où P(x), Q(x) sont des polynômes à
         Q(x)
  coecients réels.
                    P(x)
  Alors la fraction      s'écrit comme somme d'un polynôme E (x) ∈ R[x]
                            Q(x)
  (la partie entière) et d'éléments simples d'une des formes suivantes :
                      γ                               αx + β
                                     ou                                 avec b2 − 4ac < 0
                                               (ax 2 + bx + c)
                             k                                k
                (x − x0 )

  où α, β, γ, a, b, c ∈ R et k ∈ N\{0}.
    1
      Intégration du polynôme E (x). On sait faire.
                                             γ
    2
         Intégration de l'élément simple           x
                                         (x − x0 )
                                              ax + β
    3
         Intégration de l'élément simple    2         x.
                                         (ax + bx + c)
                                              D. Cransac     Analyse
~~~

## Page 51

~~~text
                     Intégrale d'une fonction en escalier
        Intégrale d'une fonction continue (par morceaux)
                                                              Intégration des éléments simples
                                          Calcul Intégral
                                                              Intégration des fonctions trigonométriques
                                Recherche de primitives
        Approximations d'intégrales, sommes de Riemann




Intégration des éléments simples


                                                                γ
    2
        Intégration de l'élément simple                               x.
                                                            (x − x0 )
                                     Z
                                          γdx
           1   Si k = 1 alors            x − x0
                                                = γ ln |x − x0 | + c0 (sur ] − ∞, x0 [ ou
               ]x0 , +∞[ ).
           2   Si
               Z k ⩾ 2 alors        Z
                     γdx                             γ
                              = γ (x − x0 )−k dx =        (x − x0 )−k+1 + c0 (sur
                  (x − x0 ) k                      −k + 1
               ] − ∞, x0 [ ou ]x0 , +∞[).




                                             D. Cransac       Analyse
~~~

## Page 52

~~~text
                      Intégrale d'une fonction en escalier
        Intégrale d'une fonction continue (par morceaux)
                                                                Intégration des éléments simples
                                           Calcul Intégral
                                                                Intégration des fonctions trigonométriques
                                 Recherche de primitives
        Approximations d'intégrales, sommes de Riemann




Intégration des éléments simples
    3   Intégration de l'élément simple (ax 2 ax +β
                                              + bx + c)x
                                                         . On écrit cette fraction
        sous la forme
                     αx + β
                                  =γ
                                          2ax + b     +δ
                                                                   1
                   (ax 2 + bx + c)k                  (ax 2 + bx + c)k                 (ax 2 + bx + c)k


         a)
              Pour le terme                 2ax + b
                                      (ax 2 + bx + c)k
                                                             2ax + bu 0 (x)
                                                   Z                              Z
                  1   Si k = 1, calcul de                                 dx =
                                                                            dx =
                                             ax 2 + bx + c          u(x)
                                            2
                      ln |u(x)| + c0 = ln ax + bx + c + c0 .
                                                  2ax + b
                                          Z                         Z 0
                                                                         u (x)
                  2   Si k ⩾ 2, calcul de                   2 dx =             dx =
                                             (ax 2 + bx + c)             u(x)k
                          1                         1                      −k+1
                               u(x)−k+1 + c0 =            ax 2 + bx + c         + c0 .
                                                                          
                       −k + 1                    −k + 1


                                              D. Cransac        Analyse
~~~

## Page 53

~~~text
                     Intégrale d'une fonction en escalier
        Intégrale d'une fonction continue (par morceaux)
                                                              Intégration des éléments simples
                                          Calcul Intégral
                                                              Intégration des fonctions trigonométriques
                                Recherche de primitives
        Approximations d'intégrales, sommes de Riemann




Intégration des éléments simples

   b)
        Pour le terme                   1
                             (ax 2 + bx + c)k

               Si k = 1, calcul de ax 2 +1bx + c dx . Par un changement de
                                            Z
           1



               variable
               Z        u = px + q on se ramène à calculer une primitive du type
                    du
                          = arctan u + c0 .
                  u2 + 1                    Z
           2   Si k ⩾ 2, calcul de            dx . On eectue le changement de
                                              (ax 2 +bx+c)k           Z
                                                                               du
               variable u = px + q pour se ramener au calcul de Ik =                  .
                                                                           (u 2 + 1)2
               Une intégration par parties permet de passer de Ik à Ik−1 .



                                             D. Cransac       Analyse
~~~

## Page 54

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                                         Intégration des éléments simples
                                       Calcul Intégral
                                                         Intégration des fonctions trigonométriques
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann



                                                                                      1
                                                          Z
                                                                  du
Exemple Calculons I2 . Partant de I1 =                                  on pose f = 2    et
                                                               u 2Z + 1            u  +1
                                                                                 Z             0
g 0 = 1. La formule d'intégration par parties                         fg 0 = [fg ] −               f 0 g donne
                       2u
(avec f 0 = −          2 et g = u )
             (u 2 + 1)

                                    2u 2 du                        u +1−1
     Z                      Z                                Z 2
          du           u                             u
I1 =           =             +                =             +  2            2 du
        u2 + 1      u2 + 1        (u 2 + 1)
                                            2      u2 + 1          (u 2 + 1)
                 Z              Z                         
         u               du               du            u
   = 2         +2             −2               2 = u 2 + 1 + 2I1 − 2I2
       u +1            u2 + 1         (u 2 + 1)

                 1    1 u
On en déduit I2 = I1 + 2    + c0 . Mais comme I1 = arctan u alors
                 2    2u +1
                                                    1                 1
                         Z
                                    du                                       u
                 I2 =                  2 = 2 arctan u + 2 u 2 + 1 + c0
                              (u 2 + 1)

                                          D. Cransac     Analyse
~~~

## Page 55

~~~text
                     Intégrale d'une fonction en escalier
       Intégrale d'une fonction continue (par morceaux)
                                                            Intégration des éléments simples
                                          Calcul Intégral
                                                            Intégration des fonctions trigonométriques
                                Recherche de primitives
       Approximations d'intégrales, sommes de Riemann




Intégration des fonctions trigonométriques

                                                                            Z
  On peut aussi calculer les primitives de la forme                              P(cos x, sin x)dx ou
                 Z
                       P(cos x, sin x)
  de la forme                          dx quand P et Q sont des polynômes, en se
                       Q(cos x, sin x)
  ramenant à intégrer une fraction rationnelle. Il existe deux méthodes :
      les règles de Bioche sont assez ecaces mais ne fonctionnent pas
      toujours ;
                                         x
      le changement de variable t = tan fonctionne tout le temps mais
                                         2
      conduit à davantage de calculs.




                                             D. Cransac     Analyse
~~~

## Page 56

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                                          Intégration des éléments simples
                                        Calcul Intégral
                                                          Intégration des fonctions trigonométriques
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Intégration des fonctions trigonométriques

  Les règles de Bioche.
  On note ω(x) = f (x)dx . On a alors ω(−x) = f (−x)d(−x) = −f (−x)dx
  et ω(π − x) = f (π − x)d(π − x) = −f (π − x)dx.
       Si ω(−x) = ω(x) alors on eectue le changement de variable
       u = cos x .
       Si ω(π − x) = ω(x) alors on eectue le changement de variable
       u = sin x .
       Si ω(π + x) = ω(x) alors on eectue le changement de variable
       u = tan x .




                                           D. Cransac     Analyse
~~~

## Page 57

~~~text
                   Intégrale d'une fonction en escalier
      Intégrale d'une fonction continue (par morceaux)
                                                              Intégration des éléments simples
                                        Calcul Intégral
                                                              Intégration des fonctions trigonométriques
                              Recherche de primitives
      Approximations d'intégrales, sommes de Riemann




Exemple
                              Z
                                     cos xdx                                     cos xdx
Calcul de la primitive             2 − cos2 x On note ω(x) = 2 − cos2 x .
                         − x)d(π − x)
Comme ω(π − x) = cos(n                     (− cos x)(−dx)
                     2 − cos2 (π − x) = 2 − cos2 x = ω(x) alors le
changement de variable qui convient est u = sin x pour lequel du = cos xdx .
Ainsi :
Z                     Z                                   Z
     cos xdx                  cos xdx                            du
    2 − cos2 x =
                                           =
                           2 − 1 − sin2 x                     1 + u 2 = [arctan u] = arctan(sin x)+c.
Le changement de variable t = tan x2 . Les formules de la  tangente de l'arc
moitié " permettent d'exprimer sinus, cosinus et tangente en fonction de tan
                 Avec t = tan x2 on a
x            1 − t 2 sin x = 2t                   2t
2 .  cos x =
             1 + t2          1 + t 2 tan x = 1 − t 2
                    et dx = 1 2+dtt 2 .

                                           D. Cransac         Analyse
~~~

## Page 58

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                                          Intégration des éléments simples
                                       Calcul Intégral
                                                          Intégration des fonctions trigonométriques
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Exemple                      Z 0
                                              dx
Calcul de l'intégrale                .
                      −π/2 1 − sin x                       h π i
                                    x
Le changement de variable t = tan dénit une bijection de − , 0
                         π
                                     2                         2
vers [−1, 0] (pour x = − , t = −1 et pour x = 0, t = 0 ). De plus on a
                         2
          2t             2dt
sin x =         et dx =        .
        1 + t2          1 + t2
    Z 0                       Z 0     2dt                     Z 0
           dx                        1+t 2                                dt
                  =                                      =2
      π 1 − sin x
                                                               −1 1 + t − 2t
                                          2t
                                −1 1 − 1+t 2
                                                                       2
     −2

                                                1 0
                                Z 0
                                                             1
                                                            
                                   dt
                          =2             =2            =2 1−     =1
                             −1 (1 − t)       1 − t −1       2
                                       2




                                          D. Cransac      Analyse
~~~

## Page 59

~~~text
             Intégrale d'une fonction en escalier
Intégrale d'une fonction continue (par morceaux)
                                  Calcul Intégral
                        Recherche de primitives
Approximations d'intégrales, sommes de Riemann




            Recherche de primitives




                                     D. Cransac     Analyse
~~~

## Page 60

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
    Approximations d'intégrales, sommes de Riemann




Dénition
Soit f : [a, b] → R une fonction continue et n ∈ N∗ . On appelle somme
de Riemann d'ordre n associée à f la somme :
                                                    n−1
                                         b−a X          b−a
                               Rn =            f (a + k     )
                                          n       | {z n }
                                                    k=0
                                                                    =ak




                                          D. Cransac      Analyse
~~~

## Page 61

~~~text
                        Intégrale d'une fonction en escalier
       Intégrale d'une fonction continue (par morceaux)
                                             Calcul Intégral
                                   Recherche de primitives
       Approximations d'intégrales, sommes de Riemann




Démonstration.

On fait la preuve dans le cas où f est lipschitzienne (ce qui est en particulier le
cas si f est de classe C 1 sur[a, b] . Notons K la constante de lipschitz associée
                        Z b                                n−1 Z ak+1                          n−1
                                                                                        b−a X
à f sur [a, b].
                                                           X
                              f (x)dx − Rn =                                f (x)dx −         f (ak )
                                                                                         n
                          a                                k=0    ak                           k=0
    n−1 Z ak+1                                        n−1 Z ak+1
                                                                                               par inégalité
    X                                                 X
=                     f (x) − f (ak ) dx ⩽                                f (x) − f (ak ) dx
    k=0       ak                                      k=0        ak
                       n−1 Z ak+1                                          n−1 Z ak+1
triangulaire ⩽                                                                          K |x − ak | dx car f est
                       X                                                   X
                                       |f (x) − f (ak )| dx ⩽
                        k=0 ak                                             k=0   ak
                          n−1 Z ak+1
lipschitzienne ⩽                           K (ak+1 − ak ) dx car f est lipschitzienne
                          X

                          k=0     ak
     n−1                                  n−1
                                              (b − a)2                    (b − a)2
              (ak+1 − ak )2 = K                                                    Comme enn lim
     X                                    X
⩽K                                                               =K
                                                      n2                     n
     k=0                                  k=0
  (b − a)2
K          = 0, on obtient par théorème d'encadrement lim
     n
     Z        b
Rn =              f (x)dx .
          a
                                                D. Cransac            Analyse
~~~

## Page 62

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann




Remarque :
   On reconnait la méthode des rectangles. En particulier, ce résultat
   signie qu'une somme de Riemann constitue une bonne
   approximation de l'intégrale pourvu que le pas soit petit.
                                                                   n          
                                                         b−a               b−a
    On a le même résultat avec                                                   .
                                                                   X
                                                   Rn0 =             f a+k
                                                            n               n
                                                                   k=1




                                          D. Cransac     Analyse
~~~

## Page 63

~~~text
                  Intégrale d'une fonction en escalier
     Intégrale d'une fonction continue (par morceaux)
                                       Calcul Intégral
                             Recherche de primitives
     Approximations d'intégrales, sommes de Riemann



Remarque. Méthode des trapèzes. La vitesse de convergence de la
                                          1
somme de Riemann vers l'intégrale est en . On peut améliorer la
                                          n
précision en utilisant
                    Z la méthode des trapèzes.
On approche alors        f par
                             [a,b]

                                                    n−1
                                    b − a X f (ak ) + f (ak+1 )
                          Tn (f ) =
                                      n              2
                                                    k=0

                                      1
On obtient alors une approximation en 2 : Si f est de classe C 2 sur
                                     n
[a, b], on peut montrer que

                                                                    (b − a)3
                           Z b
                                  f (x)dx − Tn (f ) ⩽ M2
                              a                                       12n2

où M2 = sup |f 00 (x)|.
           x∈[a,b]
                                          D. Cransac      Analyse
~~~
