# Claude TD3 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14TcMOxB1Vq1FFhWzkk8JHqo5UFXpac5j) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                      CYTech 2025-2026
                                   ING1 - GM : Probabilités

                                             TD 3


Exercice 1 Soit X ∈ L1 (Ω, A, P ) et (An )n∈N ∈ AN telle que limn→∞ P (An ) = 0.
   Montrer que limn→∞ E[X1An ] = 0.

Correction :
   On a X ∈ L1 (Ω, A, P ), donc E[|X|] < ∞.
   Pour tout n ∈ N, on a :
                                     |E[X1An ]| ≤ E[|X|1An ]
   Décomposons : pour M > 0, posons B = {|X| ≤ M } et B c = {|X| > M }. Alors :
                           E[|X|1An ]= E[|X|1An ∩B ] + E[|X|1An ∩B c ]
                                      ≤ M · P (An ) + E[|X|1B c ]

   Pour tout ε > 0, choisissons M assez grand tel que E[|X|1B c ] < ε/2 (possible car X ∈ L1 ).
   Avec ce M xé, comme P (An ) → 0, il existe N tel que pour n ≥ N :
                                        M · P (An ) < ε/2

   Donc pour n ≥ N :
                            |E[X1An ]| ≤ E[|X|1An ] < ε/2 + ε/2 = ε
   Ceci prouve que limn→∞ E[X1An ] = 0.


Exercice 2 Soit (Ω, A, P ) un espace de probabilité et X une v.a. réelle telle que X ≥ 0 p.s. et
E[X] = 1. Dénissons Q : A → R par Q(A) = E[X1A ].
  1. Montrer que Q est une mesure probabilité sur (Ω, A).
  2. Montrer que P (A) = 0 ⇒ Q(A) = 0.
  3. Montrer que l'autre sens de l'implication est fausse, en utilisant P dénie via la distribution
     uniforme sur [0, 1] et X dénie par X(x) = 21[0,1/2] (x) pour tout x ∈ R et A =]1/2, 1].
  4. En notant EQ l'espérance par rapport à Q, montrer que EQ [Y ] = EP [XY ] pour toute v.a.
     Y ≥ 0 p.s. ou bornée.
   Pour les trois questions suivantes supposons que X > 0 p.s.
  5. Montrer que X1 est intégrable pour Q.
  6. Soit R : A → R dénie par R(A) = EQ X1 1A . Montrer que R est exactement la probabilité
                                             

     P.
  7. Montrer que Q(A) = 0 ⇒ P (A) = 0.

Correction :
  1. Q est une mesure de probabilité :
    Q(∅) = E[X1∅ ] = E[0] = 0




                                                1
~~~

## Page 2

~~~text
    Pour (An ) disjoints :
                                 !                "         #
                       [              h       i      X
                   Q        An     = E X1Sn An = E X   1A n
                        n                                         n
                                          "          #
                                           X                 X                  X
                                     =E        X1An =            E[X1An ] =          Q(An )
                                           n                 n                   n

par convergence monotone (car X ≥ 0).
    Q(Ω) = E[X1Ω ] = E[X] = 1
   Donc Q est une mesure de probabilité.
   2. P (A) = 0 ⇒ Q(A) = 0 :
   Si P (A) = 0, alors 1A = 0 p.s., donc X1A = 0 p.s.
   Par conséquent : Q(A) = E[X1A ] = 0.
   3. La réciproque est fausse :
   On a Ω = [0, 1], P est la loi uniforme, et X(x) = 21[0,1/2] (x).
   Vérions : E[X] = 01 X(x)dx = 01/2 2dx = 1 (ok)
                      R               R

   Pour A =]1/2, 1] :
                                                   Z 1                Z 1
                        Q(A) = E[X1A ] =                  X(x)dx =           0 dx = 0
                                                    1/2                1/2

   Mais P (A) = P (]1/2, 1]) = 1/2 ̸= 0.
   Donc Q(A) = 0 n'implique pas P (A) = 0.
   4. Relation entre EQ et EP :
   Pour Y ≥ 0 ou bornée, par dénition de l'espérance sous Q :
                                          Z
                              EQ [Y ]=         Y (ω)dQ(ω)
                                          ZΩ
                                      =        Y (ω)X(ω)dP (ω) = EP [XY ]
                                           Ω

   5. X1 est Q-intégrable :
   Supposons X > 0 p.s. On doit montrer EQ X1 < ∞.
                                           

   Par la question 4 :                    
                                     1          1
                              EQ       = EP X ·   = EP [1] = 1 < ∞
                                     X          X
   Donc X1 est Q-intégrable.
   6. R = P :
   Pour tout A ∈ A :
                                                             
                                              1             1
                                 R(A)= EQ        1A = EP X · 1A
                                              X             X
                                       = EP [1A ] = P (A)

   Donc R = P .
   7. Q(A) = 0 ⇒ P (A) = 0 :
   Si Q(A) = 0, alors E[X1A ] = 0.
   Comme X > 0 p.s. et X1A ≥ 0, on a nécessairement X1A = 0 p.s.
   Donc 1A = 0 p.s. (car X > 0 p.s.), d'où P (A) = 0.


Exercice 3 Soit X une variable aléatoire de densité de Cauchy, i.e. fX (x) = π1 1+x
                                                                                  1
                                                                                    2 pour tout
x ∈ R.

                                                         2
~~~

## Page 3

~~~text
   Montrer que X n'admet pas d'espérance.

Correction :
   Pour que X admette une espérance, il faut que E[|X|] < ∞, c'est-à-dire :
                                            Z
                                                  |x|fX (x)dx < ∞
                                             R

   Calculons :
                               Z                         Z
                                                                  1 1
                                    |x|fX (x)dx=            |x| ·          dx
                                R                         R       π 1 + x2
                                                           Z +∞
                                                         2            x
                                                       =                  dx
                                                         π 0       1 + x2

   Posons u = 1 + x2 , donc du = 2x dx :
                              Z +∞
                                                   1 +∞ 1
                                                     Z
                                          x
                                               dx=          du
                               0        1 + x2     2 1    u
                                                   1
                                                 = [ln(u)]+∞
                                                          1   = +∞
                                                   2
   Donc E[|X|] = +∞, et X n'admet pas d'espérance.


Exercice 4 Montrer que E[XY ] = E[X]E[Y ] n'implique pas que X et Y sont indépendants.
   Aide : utiliser X ∼ U ([−1, 1]) et Y = X 2 .

Correction :
   Prenons X ∼ U ([−1, 1]) et Y = X 2 .
   Calcul de E[X] :
                                            Z 1            1
                                                   1     1 x2
                              E[X] =            x · dx =        =0
                                             −1    2     2 2 −1
   Calcul de E[XY ] = E[X 3 ] :
                                            Z 1    1
                                    3      1     1 x4
                                                   3
                             E[X ] =    x · dx =        =0
                                     −1    2     2 4 −1

   Calcul de E[Y ] :
                                                  Z 1 1
                                        2     1     1 x3 2  1
                        E[Y ] = E[X ] =    x · dx =       =
                                        −1    2     2 3 −1 3

   On a donc :
                                                              1
                                   E[XY ] = 0 = 0 ·             = E[X]E[Y ]
                                                              3
   Mais X et Y ne sont pas indépendantes :
   En eet, si X et Y étaient indépendantes, alors pour tout a, b :
                            P (X ≤ a, Y ≤ b) = P (X ≤ a)P (Y ≤ b)

   Or, Y = X 2 , donc P (Y ≤ 0) = 0 car Y ≥ 0 toujours.
   Mais P (X ≤ 0, Y ≤ 0) = P (X ≤ 0, X 2 ≤ 0) = P (X = 0) = 0.
   Si X et Y étaient indépendantes : P (X ≤ 0, Y ≤ 0) = P (X ≤ 0) · P (Y ≤ 0) = 12 · 0 = 0 (ok)

                                                          3
~~~

## Page 4

~~~text
   Mais considérons P (X > 0, Y ≤ 1/4). On a Y ≤ 1/4 ⇔ X 2 ≤ 1/4 ⇔ |X| ≤ 1/2.
   Donc P (X > 0, Y ≤ 1/4) = P (0 < X ≤ 1/2) = 41 .
   Si indépendance : P (X > 0, Y ≤ 1/4) = P (X > 0) · P (Y ≤ 1/4) = 12 · P (X 2 ≤ 1/4).
   Or P (X 2 ≤ 1/4) = P (−1/2 ≤ X ≤ 1/2) = 12 .
   Donc si indépendance : P (X > 0, Y ≤ 1/4) = 12 · 12 = 14 (ok)
   En fait, la non-indépendance est plus claire en remarquant que Y est complètement détermi-
née par X : si on connaît X , on connaît Y . Donc X et Y ne peuvent pas être indépendantes.


Exercice 5 Soient X et Y deux v.a. indépendantes à valeurs dans N∗ , avec P (X = i) = P (Y =
i) = 2−i .
    Trouver les probabilités des événements suivants :
    a) P (min(X, Y ) ≤ i)
    b) P (X = Y )
    c) P (Y > X)
    d) P (X divise Y )
    e) P (X ≥ kY ) pour k ∈ N∗ donné.

Correction :
    On a P (X = i) = P (Y = i) = 2−i pour i ∈ N∗ .
    a) P (min(X, Y ) ≤ i) :
    Par complémentaire :
                P (min(X, Y ) ≤ i)= 1 − P (min(X, Y ) > i)
                                     = 1 − P (X > i, Y > i)
                                     = 1 − P (X > i)P (Y > i) (par indépendance)

    Calculons P (X > i) :
                                   ∞                       ∞
                                   X                       X                        1/2
                     P (X > i) =           2−j = 2−i             2−k = 2−i ·              = 2−i
                                                                                  1 − 1/2
                                   j=i+1                   k=1

    Donc :
                            P (min(X, Y ) ≤ i) = 1 − 2−i · 2−i = 1 − 2−2i
    b) P (X = Y ) :
                                                 ∞
                                                 X
                               P (X = Y )=             P (X = i, Y = i)
                                                 i=1
                                                 X∞
                                             =         P (X = i)P (Y = i)
                                                 i=1
                                                 X∞                       ∞
                                                                          X
                                                        −i       −i
                                             =         2       ·2     =         2−2i
                                                 i=1                      i=1
                                               ∞
                                               X                        1/4     1
                                             =   (1/4)i =                     =
                                                                      1 − 1/4   3
                                                 i=1

    c) P (Y > X) :
    Par symétrie (car X et Y ont la même loi) :
                                       P (Y > X) = P (X > Y )


                                                           4
~~~

## Page 5

~~~text
   Or P (X > Y ) + P (X = Y ) + P (X < Y ) = 1, donc :
                                                               1
                                     2P (Y > X) +                =1
                                                               3
                                                                1
                                        P (Y > X) =
                                                                3
   d) P (X divise Y ) :
                                       ∞ X
                                       X ∞
                           P (X|Y )=              P (X = i, Y = ij)
                                       i=1 j=1
                                       X∞ X ∞
                                   =              2−i · 2−ij
                                       i=1 j=1
                                       X∞      ∞
                                               X
                                            −i   −ij
                                   =         2             2
                                       i=1        j=1
                                        ∞
                                       X                 2−i
                                   =         2−i ·
                                                       1 − 2−i
                                       i=1
                                        ∞                      ∞
                                       X      2−2i    X      1
                                   =             −i
                                                    =
                                             1−2        4 (1 − 2−i )
                                                         i
                                       i=1                     i=1

   Cette somme nécessite un calcul numérique. On peut aussi écrire :
                                               ∞
                                               X  2−i
                                             =
                                                 2i − 1
                                                 i=1

   e) P (X ≥ kY ) pour k ∈ N∗ :




Exercice 6 Montrer que min(X, Y ) suit une loi géométrique lorsqu'on suppose que X et Y sont
indépendantes et suivent une loi géométrique de paramètres respectifs λ et µ.

Correction :
   Rappel : Si X ∼ Géom(λ), alors P (X = k) = λ(1 − λ)k pour k ∈ N.
   Calculons P (min(X, Y ) = k) :
                P (min(X, Y ) = k)= P (X = k, Y > k) + P (X > k, Y = k)
                                  = P (X = k)P (Y > k) + P (X > k)P (Y = k)

   On a :
                                    P (X = k) = λ(1 − λ)k
                                         ∞
                                         X
                          P (X > k) =             λ(1 − λ)j = (1 − λ)k+1
                                        j=k+1

   De même pour Y :
                       P (Y = k) = µ(1 − µ)k ,             P (Y > k) = (1 − µ)k+1




                                                       5
~~~

## Page 6

~~~text
Donc :
            P (min(X, Y ) = k)= λ(1 − λ)k (1 − µ)k+1 + (1 − λ)k+1 µ(1 − µ)k
                              = (1 − λ)k (1 − µ)k [λ(1 − µ) + µ(1 − λ)]
                              = [(1 − λ)(1 − µ)]k [λ + µ − 2λµ]
                              = (λ + µ − λµ)[1 − (λ + µ − λµ)]k

Posons p = λ + µ − λµ = 1 − (1 − λ)(1 − µ). Alors :
                            P (min(X, Y ) = k) = p(1 − p)k

Donc min(X, Y ) ∼ Géom(λ + µ − λµ).



                                                                              1/1




                                           6
~~~
