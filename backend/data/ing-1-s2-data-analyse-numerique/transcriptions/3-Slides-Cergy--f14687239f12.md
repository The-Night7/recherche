# 3-Slides-Cergy.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1NriV93uaXMpYX4NLNoz13G1RikIfQbyA) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Chap 3: Interpolation
    polynomiale


Laboratoire AGM: Analyse, Modélisation et Géométrie
~~~

## Page 2

~~~text
Interpolation Polynômiale

  Soit I un intervalle de IR, (x0 , · · · · · · , xn ) ∈ I n , n + 1 points distincts, on
  veut déterminer un polynôme P ∈ IRn [X ] tel que P(xi ) = f (xi ) ∀i


  Theorem
                     ∃!P ∈ IRn [X ], ∀0 ≤ i ≤ n, P(xi ) = f (xi ).


  Démonstration.
  On considère
                                              → IR n+1
                                 φ : IRn [X ] −
  ,
                              P→
                               − (P(x0 ), · · · , P(xn )).
  On montre que φ est linéaire et Ker φ = {0}.                                         ■


                                                                                                     2
                                                                                            2 / 12
~~~

## Page 3

~~~text
Méthode directe


                   Pn
 On écrit P(x) = i=0 ai x i et les coefficients (ai ) sont solution du
 système linéaire de Vandermonde : Soit

                 1 x0 x02 · · · x0n
                                                            
                                               a0        f (x0 )
               1 x1 x12 · · · x1n   a1  f (x1 )
              . . . . . . . . . . . . . . . . . . =  . . . 
                                                            

                 1 xn xn2 · · · xnn            an        f (xn )

 Les points sont distincts donc la matrice est inversible.




                                                                                  3
                                                                         3 / 12
~~~

## Page 4

~~~text
Méthode de Lagrange

 On utilise la base de Lagrange de IRn [X ] définie par

                   Li (xj ) = δi,j ∀ 0 ≤ i ≤ n, ∀ 0 ≤ j ≤ n.

 On a
                                                (x − xj )
                          Li (x) = Πnj=0,j̸=i
                                                (xj − xi )
 On montre facilement que (Li )ni=0 est une famille libre et génératice de
 IRn [X ].
 Le polynôme d’interpolation est alors
                                      n
                                      X
                           Pn (x) =         f (xi )Li (x).
                                      i=0




                                                                                      4
                                                                             4 / 12
~~~

## Page 5

~~~text
Méthode de Newton


 Definition
 On définit les divisions divisées par recurrence

                                           f [xi ] = f (xi )

                                       f [x1 , x2 , · · · , xN ] − f [x0 , x1 , · · · , xN−1 ]
         f [x0 , x1 , · · · , xN ] =
                                                              xN − x 0

 On a
                                   N
                                   X
                       P(x) =             f [x0 , · · · , xk ]Πk−1
                                                               j=0 (x − xj )
                                   k=0




                                                                                                          5
                                                                                                 5 / 12
~~~

## Page 6

~~~text
Exemple de calcul avec les 3
méthodes du polynome d’interpolation
  On prend f (x) = e x , x0 = −1, x1 = 0 et x2 = 1. Pour la méthode
  directe, on a                         −1 
                         1 −1 −1         a0       e
                      1 0        0  a1  =  1 
                         1 1      1      a2         e
  On a
                       P(x) = 1 + sh(e)X + (−1 + ch(e))X 2 .
  On calcule la base de Lagrange : L0 (−1) = 1, L0 (0) = 0 et L0 (1) = 0
  d’ou L0 (X ) = CX (X − 1) et avec la premiere condition on a C = 1/2
  d’ou L0 (X ) = X /2 ∗ (X − 1). De même, L1 (X ) = 1 − X 2 et
  L2 (X ) = X /2 ∗ (X + 1). Ainsi
  P(X ) = e −1 X /2 ∗ (X − 1) + 1 − X 2 + eX /2 ∗ (X + 1)
  Pour la dernière méthode, on calcule f [x0 , x1 ] = f [xx11]−f
                                                              −x0
                                                                 [x0 ]
                                                                       = 1 − e −1 ,
  f [x1 , x2 ] = f [xx22]−f
                         −x1
                            [x1 ]
                                  = e − 1 et f [x0 , x1 , x2 ] = ch(e) − 1.
                                                                                               6
                                                                                      6 / 12
~~~

## Page 7

~~~text
Estimation de l’erreur
d’interpolation
  On a si f très régulière : ∃ζ ∈ I tel que ∀x ∈ I

                                           |f (N+1) (ζ)| N
             |EN (x)| = |f (x) − P(x)| ≤                Π (x − xi )|
                                             (N + 1)! i=0

  demonstration : Soit x ∈ I , different des xi et on définit
                                                      EN (x)
                  G (t) = EN (t) − ΠN
                                    i=0 (t − xi )    N (x − x
                                                                .
                                                    πi=0      i

  On voit que G s’annule en xi pour i = 0, .., N et en x. Donc G s’annule
  au moins N + 2 fois. En utilsant le théorème de Rolle, on peut dire que
  G ′ s’annule N + 1 fois. En reiterant on a l’existence ζ ∈ I tel que
  G N+1 (ζ) = 0. Il reste a calculer

                                                         EN (x)
               G (N+1) (t) = f (N+1) (t) − (N + 1)!                  .
                                                      ΠN
                                                       i=0 (x − xi )
                                                                                     7
                                                                            7 / 12
~~~

## Page 8

~~~text
Méthode d’Hermite



 On veut déterminer P tel que P(xi ) = f (xi ) et P ′ (xi ) = f ′ (xi ) pour tout
 i. On a
                               XN X  1
                       P(x) =           f (k) Li,k (x)
                                    i=0 k=0
 avec
                dp
                     Li,k (xj ) = 1 si i = j et k = p et 0 sinon.
                dx p




                                                                                             8
                                                                                    8 / 12
~~~

## Page 9

~~~text
Exemple de Calcul d’erreur avec
Hermite

  Exercice (corrigé en TD) :
  On cherche P tel que P(0) = f (0), P(1) = f (1), P ′ (0) = f ′ (0) et
  P ′ (1) = f ′ (1). Soit 0 < h < 1, on définit R(x) = f (x) − P(x),
  Π(x) = x 2 (x − 1)2 et F (x) = R(x)π(h) − R(h)π(x).
    1   Montrer l’existence et l’unicité de P.
    2   Déterminer les racines de R et Π.
    3   Montrer qu’il existe ζ tel que F (4) (ζ) = 0.
                              1 (4)
    4   En deduire que R(h) = 4! f (ζ)π(h).
    5   Montrer que
                                                1
                            |f (x) − P(x)| ≤       ||f (4) ||∞ .
                                               380


                                                                                   9
                                                                          9 / 12
~~~

## Page 10

~~~text
Méthode des splines cubiques
  Soient f une fonction régulière donnée, on cherche s3 ∈ IR3 [X ] telle que
  s(xi ) = f (xi ) ∀i = 1, · · · , N + 1 et s3 a une dérivée seconde continue. On
                                (2)
  note s3 (xi ) = fi , Mi = s3 (xi ). Notons par s3,i−1 (x) = s3 (x) pour tout
                                    (2)
  x ∈ [xi−1 , xi ]. On sait que s3,i−1 est linéaire

                       (2)                 xi − x      x − xi−1
                      s3,i−1 (x) = Mi−1           + Mi
                                              hi          hi
  avec hi = xi − xi−1 . En intégrant deux fois, on a
                           (xi − x)3      (x − xi−1] )3
       s3,i−1 (x) = Mi−1             + Mi               + Ci−1 (x − xi ) + C̃i−1 .
                               6hi            6hi
  En utilisant les égalités s3,i−1 (xi ) = fi et s3,i−1 (xi−1 ) = fi−1 , on a
                                                   h2
                                C̃i−1 = fi−1 − Mi−1 i
                                                    6
  et
                                  fi − fi−1  hi
                       Ci−1 =               − (Mi − Mi−1 ).
                                      hi     6
                                                                                               10
                                                                                     10 / 12
~~~

## Page 11

~~~text
Méthode des splines cubiques
  On a ∀i = 1, · · · , N, ∀x ∈ [xi−1 − xi ]
                                      (xi − x)3      (x − xi−1 )3
                    s3,i−1 = Mi−1               + Mi
                                          6hi            6hi
             fi − fi−1  hi                                      h2
         +(            − (Mi − Mi−1 ))(x − xi−1 ) + fi−1 − Mi−1 i .
                 hi     6                                        6
  Imposons que la dérivée première de s3 est continue aux points xi . On
  doit écrire
            s3′ (xi+ ) = s3,i
                          ′
                              (xi ) = s3′ (xi− ) = s3,i−1
                                                    ′
                                                          (xi ) ∀i = 1, N − 1.
                            ′
  Ainsi ayant déjà calculé s3,i−1 , on a
                                     hi       hi    fi − fi−1
                      s3′ (xi− ) =      Mi−1 + Mi +
                                     6        3        hi .
  De même, en calculant s3,i , on a
                                   hi+1      hi+1        fi+1 − fi
                  s3′ (xi+ ) = −        Mi −      Mi+1 +           .
                                    3         6            hi+1
                                                                                           11
                                                                                 11 / 12
~~~

## Page 12

~~~text
On a N − 1 équations appelées équations des moments
               µi Mi−1 + 2Mi + λi Mi+1 = di ∀i = 1, N − 1
avec
                               hi                hi+1
                      µi =              λi =
                           hi + hi+1          hi + hi+1
                           6        fi+1 − fi    fi − fi−1
                 di =             (           −            ).
                       hi + hi+1 hi+1                hi
On a N + 1 inconnues Mi par contre on a N − 1 équations, donc on va
rajouter par exemple deux équations qui seront des splines dites
naturelles M0 = MN = 0
Exemple : x0 = 0, x1 = 1, x2 = 2 et f (x0 ) = 0, f (x1 ) = 1 et f (x2 ) = 0.
On a une seule équation des moments
                         M0 + 4M1 + M1 = −12.
On trouve comme spline cubique
                                 1     3
                     s3,0 (x) = − x 3 + x 2 ∀x ∈ [0, 1],
                                 2     2
                             1          3
              s3,1 (x) = − (2 − x)3 + (2 − x) ∀x ∈ [1, 2].
                             2          2
                                                                                         12
                                                                               12 / 12
~~~
