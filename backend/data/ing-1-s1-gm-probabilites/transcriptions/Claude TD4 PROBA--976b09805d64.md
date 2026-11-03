# Claude TD4 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1nwIiDVam-HqtbT8e7-mXK_7IzIy83jZi) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                     CYTech 2025-2026
                                   ING1 - GM : Probabilités
                                                TD 4


Exercice 1 Soient X et Y deux v.a.r. indépendantes de loi P (X = 1) = P (Y = 1) = 21 et
P (X = −1) = P (Y = −1) = 12.
   SoitZ = XY   . Montrer queX, Y, Z    sont indépendantes deux à deux, mais qu'elles ne sont
pas indépendantes.
Correction :
  Loi de Z = XY :
   Calculons les valeurs possibles de Z :
                     P (Z = 1)= P (X = 1, Y = 1) + P (X = −1, Y = −1)
                                1 1 1 1        1
                              = · + · =
                                2 2 2 2        2

                    P (Z = −1)= P (X = 1, Y = −1) + P (X = −1, Y = 1)
                                1 1 1 1        1
                              = · + · =
                                2 2 2 2        2
   Donc Z a la même loi que X et Y .
   Indépendance deux à deux :
    X et Y sont indépendantes : donné dans l'énoncé.
    X et Z sont indépendantes :
                                                                              1
                 P (X = 1, Z = 1)= P (X = 1, XY = 1) = P (X = 1, Y = 1) =
                                                                              4
                                     1 1  1
              P (X = 1)P (Z = 1)=     · =
                                     2 2  4
De même, on vérie pour toutes les combinaisons. Donc X et Z sont indépendantes.
    Y et Z sont indépendantes : par symétrie avec X et Z .
   X, Y, Z ne sont pas mutuellement indépendantes :
   Pour l'indépendance mutuelle, il faudrait :
           P (X = x, Y = y, Z = z) = P (X = x)P (Y = y)P (Z = z) pour tous x, y, z

   Or, considérons X = 1, Y = 1, Z = −1 :
                 P (X = 1, Y = 1, Z = −1) = P (X = 1, Y = 1, XY = −1) = 0

(car si X = 1 et Y = 1, alors Z = XY = 1 ̸= −1)
    Mais :                                             1 1 1 1
                      P (X = 1)P (Y = 1)P (Z = −1) =    · · = ̸= 0
                                                       2 2 2 8
   Donc X, Y, Z ne sont pas mutuellement indépendantes.
Exercice 2 Soit X une v.a.r. t.q. FX (x) ∈ {0, 1}. Montrer que X est constante p.s.
   Indication : Utiliser x := inf{c ∈ R, F (c) = 1}.
                         0                  X


                                               1
~~~

## Page 2

~~~text
Correction :
   Soit x = inf{c ∈ R : F (c) = 1}.
   Cas 1 : Si cet ensemble est vide, alors F (x) = 0 pour tout x ∈ R.
         0                         X


   Mais lim F (x) = 1, contradiction. Donc l'ensemble n'est pas vide.
                                                             X
             x→+∞          X
   Montrons que P (X = x ) = 1 :
    Pour x < x : par dénition de inf , F (x) = 0 (sinon x ne serait pas l'inmum).
                                       0


   Donc P (X < x ) = lim F (x) = 0.
                   0                                     X                       0


    Pour x ≥ x : soit (x ) une suite décroissante vers x avec F (x ) = 1.
                       0           x→x−
                                      0
                                               X


   Par continuité à droite de F :
                   0               n                                         0       X   n
                                           X

                                               FX (x0 ) = lim FX (xn ) = 1
                                                             n→∞

   Donc : P (X ≤ x ) = F (x ) = 1 et P (X < x ) = 0.
   Par conséquent :
                               0       X   0                         0



                               P (X = x0 ) = P (X ≤ x0 ) − P (X < x0 ) = 1 − 0 = 1

   Ainsi, X = x p.s.
                   0




Exercice 3 Soient X et Y deux variables aléatoires indépendantes dénies sur (Ω, A, P ) un
espace de probabilité. On suppose que X + Y est constante p.s.
   Montrer que X et Y sont constantes p.s.
Correction :
   Soit c ∈ R tel que X + Y = c p.s.
   Alors Y = c − X p.s.
   Calcul de la variance :
                                  Var(X + Y )= Var(c) = 0
   D'autre part, comme X et Y sont indépendantes :
                             Var(X + Y )= Var(X) + Var(Y )
   Donc :
                                   Var(X) + Var(Y ) = 0
   Comme les variances sont positives :
                                 Var(X) = 0 et Var(Y ) = 0
   Or, Var(X) = 0 ⇔ X est constante p.s.
   Donc X et Y sont constantes p.s.
Exercice 4 Soit (Xn )n≥1 une suite de v.a.r. i.i.d. t.q. X1 ∼ Bernoulli(p) où p ∈]0, 1[ : P (Xn =
1) = pet P (X = 0) = 1 − p =: q pour tout n ∈ N .
               n
                                                                     ∗

  1. Montrer qu'il y a presque sûrement une innité de n tels que X = 1.                 n
  2. Pour n ∈ N , on dénit l'événement A = {X = X = · · · = X = 1}. Montrer que
                   ∗

     p.s. il n'y a qu'un nombre ni de A qui sont réalisés.
                                                         n               n   n+1             2n−1
                                                     n




                                                                 2
~~~

## Page 3

~~~text
Correction :
  1. Innité de succès p.s. :
   Soit B = {X = 1}. On veut montrer que P (lim sup B ) = 1.
   Par le lemme de Borel-Cantelli 2 :
             n       n                                                        n


   Les  (B ) sont indépendants (car les X le sont)
                 n                                         n
    P  ∞
            P (B ) =
                     P
                     n    p = +∞ (car p > 0)
                                 ∞

   Donc P (lim sup B ) = 1, ce qui signie qu'il y a p.s. une innité de n tels que X = 1.
        n=1                      n=1
                             n                                                                       n
   2. Nombre ni de séquences :
   On a A = {X = X = · · · = X = 1}.
   Le nombre de termes dans cette séquence est 2n − 1 − n + 1 = n.
             n           n       n+1              2n−1


   Donc :
                                                       P (An ) = pn
   Calculons :                           ∞                 ∞
                                         X                 X             p
                                               P (An ) =         pn =       <∞
                                                                        1−p
                                         n=1               n=1

(car p < 1)
    Par le lemme de Borel-Cantelli 1 :
                                                  P (lim sup An ) = 0

   Cela signie que p.s., seul un nombre ni de A se réalisent.    n




Exercice 5 Soit X une v.a.r. de loi N (0, 1), et Y = X 2 .
  1. Utiliser le théorème du cours pour montrer que Y admet une densité f et donner une
     expression de f .
                                                                                               Y
                             Y
  2. En partant du calcul de la fonction de répartition de Y , F , trouver le même résultat.
                                                                                   Y


Correction :
  1. Méthode par changement de variable :
   Soit g(x) = x . On a Y = g(X).
                     2

   Sur I = [0, +∞[, g est strictement croissante avec g (y) = √y et√ (g ) (y) = .
         1
                                                                         −1            −1 ′           1
                                                                                                      √

   Sur I =] − ∞, 0], g est strictement décroissante avec g (y) = − y et (g ) (y) = − .
                                                                                                     2 y
                                                                              −1              −1 ′          1
                                                                                                            √

   Par le théorème de changement de variable :
         2                                                                                                 2 y



                                              √  1         √         1
                                  fY (y)= fX ( y)√ + fX (− y) − √
                                                2 y                 2 y
                                         1      √          √
                                       = √ [fX ( y) + fX (− y)] 1]0,+∞[ (y)
                                        2 y

   Comme f (x) = X
                                   2
                             √1 e−x /2
                              2π
                                         est paire :
                                                 1      √
                                       fY (y)= √ · 2fX ( y)1]0,+∞[ (y)
                                               2 y
                                                1   1
                                             = √ · √ e−y/2 1]0,+∞[ (y)
                                                 y  2π
                                                 1 −1/2 −y/2
                                             =√ y      e     1]0,+∞[ (y)
                                                 2π


                                                               3
~~~

## Page 4

~~~text
   C'est la loi χ = γ(1/2, 1/2).
                2
                1
   2. Méthode par fonction de répartition :
   Pour y ≥ 0 :
                                     FY (y)= P (Y ≤ y) = P (X 2 ≤ y)
                                                 √          √
                                           = P (− y ≤ X ≤ y)
                                                 √           √
                                           = FX ( y) − FX (− y)

   En dérivant par rapport à y :
                                                                         
                                            √          1       √       1
                      fY (y)= FY′ (y) = fX ( y) ·     √ − fX (− y) · − √
                                                     2 y              2 y
                                  1       √              √
                                = √ [fX ( y) + fX (− y)]
                                 2 y
                                   1
                                =√     e−y/2 1]0,+∞[ (y)
                                   2πy

   On retrouve le même résultat.
Exercice 6 Soit X une v.a.r. t.q. X ∼ U ([−1, 1]).
  1. Trouver une densité de la v.a.r. Y := X que l'on note par f , pour k ∈ N , lorsque k est
                                                    k                             ∗

     impair.
                                                                            Y


  2. Lorsque k est pair, donner l'expression de f (y) pour tout y ∈ R.
                                                            Y


Correction :
   On a f (x) = 1 (x).
          X
                     1
                     2 [−1,1]
   1. Cas k impair :
   Soit g(x) = x . Pour k impair, g est strictement croissante sur R.
                 k

   Sur [−1, 1], g : [−1, 1] → [−1, 1] bijectivement.
   On a g (y) = y et (g ) (y) = y .
          −1          1/k         −1 ′       1 (1/k)−1

   Par changement de variable :              k



                                                        1 (1/k)−1
                                  fY (y)= fX (y 1/k )     y       1[−1,1] (y)
                                                        k
                                           1 1 (1/k)−1
                                         =   · |y|      1[−1,1] (y)
                                           2 k
                                            1 (1−k)/k
                                         =    |y|     1[−1,1] (y)
                                           2k
   2. Cas k pair :
   Pour k pair, g(x) = x n'est pas monotone sur [−1, 1].
                            k

   Décomposons : sur [−1, 0], g est décroissante; sur [0, 1], g est croissante.
   Pour y ∈ [0, 1] :
                                   FY (y)= P (X k ≤ y) = P (|X| ≤ y 1/k )
                                         = P (−y 1/k ≤ X ≤ y 1/k )
                                           Z y1/k
                                                   1
                                         =           dx = y 1/k
                                            −y 1/k 2




                                                        4
~~~

## Page 5

~~~text
   En dérivant :                        1 (1/k)−1             1
                           fY (y) =       y       1[0,1] (y) = y (1−k)/k 1[0,1] (y)
                                        k                     k
   Pour y < 0 : f (y) = 0 (car         Y =X ≥0k            toujours).
   Pour y > 1 : f (y) = 0 (car                    ).
                   Y
                   Y                   Y ∈ [0, 1]


Exercice 7 Soit X une variable aléatoire à valeurs dans ]a, b[ et admettant une espérance E[X].
Soit g :]a, b[→ R une fonction convexe avec g ∈ C (]a, b[; R).   2

    Montrer que E[g(X)] ≥ g(E[X]).
Correction (Inégalité de Jensen) :
   Soit m = E[X] ∈]a, b[.
   Méthode 1 (via la convexité) :
   Comme g est convexe, pour tout x ∈]a, b[ :
                                         g(x) ≥ g(m) + g ′ (m)(x − m)

   En prenant l'espérance :
                                     E[g(X)]≥ E[g(m) + g ′ (m)(X − m)]
                                            = g(m) + g ′ (m)E[X − m]
                                            = g(m) + g ′ (m) · 0 = g(E[X])

   Méthode 2 (via Taylor-Lagrange) :
   Par Taylor-Lagrange à l'ordre 2, pour tout x ∈]a, b[ :
                                                                        g ′′ (ξ)
                            g(x) = g(m) + g ′ (m)(x − m) +                       (x − m)2
                                                                            2
où ξ est entre m et x.
   Comme g est convexe, g ≥ 0. En prenant l'espérance :
                                ′′

                                                           ′′              
                                              ′             g (ξ)         2
                       E[g(X)]= g(m) + g (m)E[X − m] + E          (X − m)
                                                               2
                                              ′′            
                                              g (ξ)        2
                              = g(m) + 0 + E        (X − m)
                                                 2
                              ≥ g(m) = g(E[X])



Exercice 8 Soient X une variable aléatoire de loi normale standard et Z une variable aléatoire
indépendante de X t.q. P (Z = −1) = = P (Z = 1).
                                              1

   1. Montrer que X et −X suivent la même loi.
                                              2


   2. Montrer que Y := ZX est une v.a.r. qui suit la gaussienne standard.
Correction :
  1. X et −X ont la même loi :
   La densité de X est f (x) =                 2
                                         √1 e−x /2     .
   Pour −X :
                            X             2π


                                           1      2      1   2
                       f−X (y)= fX (−y) = √ e−(−y) /2 = √ e−y /2 = fX (y)
                                           2π            2π

                                                             5
~~~

## Page 6

~~~text
   Donc X et −X ont la même loi.
   2. Y = ZX ∼ N (0, 1) :
   Méthode par fonction caractéristique :
   Calculons φ (t) = E[e ] = E[e
                          itY                    .
                                            itZX ]

   Par indépendance de X et Z :
               Y



                         φY (t)= EZ [EX [eitZX |Z]]
                                    = EZ [φX (tZ)]
                                    = P (Z = 1)φX (t) + P (Z = −1)φX (−t)
                                      1         1
                                    = φX (t) + φX (−t)
                                      2         2

   Or, pour X ∼ N (0, 1) : φ (t) = e         −t2 /2   .
   Donc :
                                X


                                        1 2      1        2
                                φY (t)= e−t /2 + e−(−t) /2
                                        2        2
                                        1 −t2 /2 1 −t2 /2       2
                                      = e       + e        = e−t /2
                                        2        2
                                      = φX (t)

   Par unicité de la fonction caractéristique, Y ∼ N (0, 1).
Exercice 9 Soit X ∼ N (0, 1). Déterminer les lois des v.a. Y , Z et W dénies par W = X 2 ,
Y = eX   et Z = σX + µ, où σ ∈ R et µ ∈ R.
                                        ∗


Correction :
  1. W = X 2 :
   D'après l'exercice 5, W ∼ χ = γ(1/2, 1/2) avec densité :
                                    2
                                    1

                                                           1
                                    fW (w) = √                e−w/2 1]0,+∞[ (w)
                                                          2πw

   2. Y = eX (loi log-normale) :
   Pour y > 0 :
                                    FY (y)= P (eX ≤ y) = P (X ≤ ln y)
                                            = FX (ln y) = Φ(ln y)

   En dérivant :
                                                              1
                                fY (y)= fX (ln y) ·
                                                              y
                                               1        2    1
                                            = √ e−(ln y) /2 · 1]0,+∞[ (y)
                                               2π            y
                                                1         2
                                            = √ e−(ln y) /2 1]0,+∞[ (y)
                                              y 2π
   3. Z = σX + µ :
   Transformation ane d'une gaussienne :
                                                 Z ∼ N (µ, σ 2 )


                                                             6
~~~

## Page 7

~~~text
   avec densité :                             1       2    2
                                    fZ (z) = √ e−(z−µ) /(2σ )
                                            σ 2π



Exercice 10 Une digue est haute de 4,5 mètres. On suppose que l'amplitude (en mètres) d'une
vague est une variable aléatoire de loi uniforme sur [1, 5].
   1. Quelle est la probabilité qu'une vague dépasse la digue?
   2. On observe trois vagues et l'on suppose que les amplitudes X , X , X sont indépendantes
      et identiquement distribuées. Quelle est la probabilité que de l'eau franchisse la digue?
                                                                      1   2     3


   3. Quelle devrait être la hauteur de la digue pour que cette probabilité soit de 10%?
   4. Un repère enregistre l'amplitude maximale Y de trois vagues. Quelle est son espérance?
Correction :
   Soit X ∼ U ([1, 5]), donc f (x) = 1
                              X
                                        1
                                        4 [1,5] (x)   .
   1. Probabilité qu'une vague dépasse 4,5 m :
                                                  5 − 4.5   0.5   1
                                  P (X > 4.5) =           =     =
                                                   5−1       4    8
   2. Probabilité que l'eau franchisse la digue :
   Il faut qu'au moins une des trois vagues dépasse 4,5 m :
               P (max(X1 , X2 , X3 ) > 4.5)= 1 − P (max(X1 , X2 , X3 ) ≤ 4.5)
                                            = 1 − P (X1 ≤ 4.5, X2 ≤ 4.5, X3 ≤ 4.5)
                                            = 1 − P (X1 ≤ 4.5)3
                                                    4.5 − 1 3
                                                          
                                            =1−
                                                     5−1
                                                   3           3
                                                    3.5           7
                                            =1−            =1−
                                                     4            8
                                                  343    169
                                            =1−        =     ≈ 0.33
                                                  512    512
   3. Hauteur pour probabilité de 10% :
   Soit h la hauteur recherchée. On veut :
                                   P (max(X1 , X2 , X3 ) > h) = 0.1

   Donc :
                                            h−1 3
                                                 
                                        1−          = 0.1
                                              4
                                           h−1 3
                                               
                                                   = 0.9
                                            4
                                      h−1
                                             = 0.91/3 ≈ 0.9654
                                        4
                                  h = 1 + 4 × 0.9654 ≈ 4.86  mètres
   4. Espérance du maximum :



                                                      7
~~~

## Page 8

~~~text
Soit Y = max(X , X , X ). Sa fonction de répartition est :
                   1     2   3
                                                                            3
                                                              3        y−1
                   FY (y) = P (Y ≤ y) = P (X1 ≤ y) =                              1[1,5] (y)
                                                                        4

La densité est :
                                              2
                                                                  3(y − 1)2
                                    
                                        y−1         1
                       fY (y) = 3                  · 1[1,5] (y) =           1[1,5] (y)
                                         4          4                64

L'espérance :
                                 Z 5
                                      3(y − 1)2
                        E[Y ]=     y·             dy
                                1          64
                                  Z 5
                               3
                             =        y(y − 1)2 dy
                               64 1
                                  Z 5
                               3
                             =        (y 3 − 2y 2 + y)dy
                               64 1
                                                     5
                               3 y 4 2y 3 y 2
                                  
                             =         −       +
                               64 4         3      2 1
                                                              
                               3      625 250 25            1 2 1
                             =             −       +     −   − +
                               64      4       3      2     4 3 2
                               3 64
                             =    ·    ·4=4
                               64 3
Donc E[Y ] = 4 mètres.
Exercices 11-15 : Voir page suivante




                                                        8
~~~

## Page 9

~~~text
Exercice 11 (Loi γ (gamma), β (beta) et χ2 (khi-deux)).
   Cet exercice est très long. Voici les grandes étapes :
   1.a) fXa,b est une densité :
                             Z +∞
                                           ba a−1 −bx    ba   Γ(a)
                                               x e dx =     ·      =1
                                 0        Γ(a)          Γ(a) ba
   1.b) Espérance et variance :
                                      E[Xa,b ] =
                                                        a
                                                        b
                                                          ,    Var(X ) = ba  a,b      2

   1.c) Fonction caractéristique :
                                                                   it −a
                                                                    
                                            φXa,b (t) =         1−
                                                                   b
   2.a) Somme de Gamma :
   Si X ∼ γ(a , b) et X ∼ γ(a , b) indépendantes :
        1         1      2            2

                                            X1 + X2 ∼ γ(a1 + a2 , b)

   3.a) Y 2 et valeur de Γ(1/2) :
   Si Y ∼ N (0, 1), √alors Y ∼ γ(1/2, 1/2) (cf. exercice 5).
                             2

   Donc Γ(1/2) = π.
   3.b) Somme de carrés dePgaussiennes :
   Si X ∼ N (0, 1) i.i.d., alors X ∼ χ = γ(n/2, 1/2).
        i
                                          n
                                          i=1
                                                 2
                                                 i
                                                          2
                                                          n



Exercice 13 Soient X ∼ N (0, 1), Y ∼ Poisson(λ) et Z ∼ U ([−a, a]), a ∈ R∗ .
   Calculer φ (t) pour A ∈ {X, Y, Z}.
              A


Correction :
  Pour X ∼ N (0, 1) :
                                                                         2
                                                     φX (t) = e−t /2
   Pour Y ∼ Poisson(λ) :
                                                                   ∞
                                                        itY
                                                                   X               λk e−λ
                                     φY (t)= E[e              ]=         eitk ·
                                                                                     k!
                                                                   k=0
                                                        ∞
                                                        X (λeit )k
                                                = e−λ
                                                                   k!
                                                        k=0
                                                     −λ   λeit                it
                                                =e      ·e         = eλ(e −1)

   Pour Z ∼ U ([−a, a]) :
                                                                   Z a
                                                       itZ            1
                                     φZ (t)= E[e ] =          eitx · dx
                                                           −a        2a
                                                  itx a
                                              1 e
                                           =
                                             2a it −a
                                               1
                                           =      (eita − e−ita )
                                             2ait
                                               1                    sin(at)
                                           =       · 2i sin(at) =
                                             2ait                      at

                                                               9
~~~

## Page 10

~~~text
Exercice 15 Soient n variables aléatoires indépendanteshX1 , X2 , . . . ,iXn ayant chacune un mo-
ment d'ordre 3 ni, et de moyenne nulle. Montrer que E (P                         n
                                                                                  i=1 Xi )
                                                                                           3
                                                                                               =
                                                                                                   Pn      3 .
                                                                                                    i=1 E[Xi ]


Correction : P
   Posons S = X . On veut calculer E[S ].
                        n
                        i=1   i
                                                            3

   Méthode par fonction caractéristique :
   On sait que :                          1                           (k)
                                                E[S k ] =            φS (0)
                                                                ik
   Comme les X sont indépendantes :
                    i

                                                            n
                                                            Y
                                                φS (t) =             φXi (t)
                                                            i=1

   En prenant le logarithme :                               n
                                                            X
                                              ln φS (t) =            ln φXi (t)
                                                            i=1

   Développement de Taylor :
                                                        t2            t3
                              ln φXi (t) = itE[Xi ] −      E[Xi2 ] − i E[Xi3 ] + o(t3 )
                                                        2             6
   Comme E[X ] = 0 :
                i

                                                   t2            t3
                                  ln φXi (t) = −      E[Xi2 ] − i E[Xi3 ] + o(t3 )
                                                   2             6
   Donc :                                        n                          n
                                              t2 X             t3 X
                              ln φS (t) = −        E[Xi2 ] − i      E[Xi3 ] + o(t3 )
                                              2                6
                                                i=1                         i=1

   En dérivant trois fois et évaluant en t = 0 :
                                                            n
                                                            X
                                                E[S 3 ] =            E[Xi3 ]
                                                            i=1




                                                            10
~~~
