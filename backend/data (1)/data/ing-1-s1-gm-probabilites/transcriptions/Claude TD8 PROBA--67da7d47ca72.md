# Claude TD8 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1PT4jLXICfNlGJ0rF1TP1mJ7w7WZvL5zl) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                    ING1 - GM : Probabilités
                                      CY Tech 2025-2026




                        TD 8 - Espérance Conditionnelle




             On lance 3 pièces de monnaies non biaisées, 10, 20 et 50 centimes d'euros. Face =
0, Pile = valeur de la pièce. X = somme totale. Z = somme des pièces de 10 et 20.
Exercice 1


    Calculer E[X|Z].
Correction :
   Espace des possibilités :
   ΩX = {F F F, F F P, F P F, F P P, P F F, P F P, P P F, P P P }
   X prend les valeurs : {0, 10, 20, 30, 50, 60, 70, 80}
   Z=  somme de 10 et 20, donc     Z ∈ {0, 10, 20, 30}
   Valeurs possibles :

   Z = 0 : pièces 10 et 20 sont Face. Alors X ∈ {0, 50}
   Z = 10 : une seule parmi 10 et 20 est Pile. Alors X ∈ {10, 20, 60, 70}
   Z = 20 : 10 est Face et 20 est Pile OU 10 est Pile et 20 est Face. Alors X ∈ {20, 70} ou
    {10, 60}
   Z = 30 : pièces 10 et 20 sont Pile. Alors X ∈ {30, 80}
              E[X|Z = z]
       Z = 0 (FF?)
   Calcul de                 :
   Cas         :



                          P (X = 0|Z = 0)= P (50 est F|Z = 0) =
                                                                   1
                                                                   2
                         P (X = 50|Z = 0)= P (50 est P|Z = 0) =
                                                                   1
                                                                   2
                                                      1       1
                                 E[X|Z = 0]= 0 ·        + 50 · = 25
                                                      2       2
   Cas Z = 10 :  (une parmi 10 et 20 est P)
   Si 10P et 20F : X ∈ {10, 60} avec proba 1/2 chacun
   Si 10F et 20P : X ∈ {20, 70} avec proba 1/2 chacun
   Mais quelle conguration sachant Z = 10 ? Par symétrie : 1/2 chacune
                                                             
                                        1 10 + 60     1 20 + 70
                           E[X|Z = 10]=             +
                                        2    2        2    2
                                        1      1
                                      = (35) + (45) = 40
                                        2      2
   Cas Z = 20 :
   Si 10P et 20F : impossible car Z = 10 ̸= 20
   Si 10F et 20P : Z = 20, donc X ∈ {20, 70}
   Ou 10P et 20P : Z = 30 ̸= 20
   En fait, Z = 20 signie exactement une des deux est Pile (avec valeur 20).
   Donc soit 10F-20P : X ∈ {20, 70}, soit 10P-20F : impossible si on veut Z = 20.
   Correction : Z = 20 peut être :
   10F, 20P : Z = 0 + 20 = 20, X ∈ {20, 70}
   10P, 20F : Z = 10 + 0 = 10 ̸= 20
                                                  1
~~~

## Page 2

~~~text
   Donc sachant Z = 20, on a 10F et 20P :
                                                        20 + 70
                                    E[X|Z = 20] =               = 45
                                                           2
   Cas Z = 30 :    (PP?)                                30 + 80
                                    E[X|Z = 30] =               = 55
                                                           2
   Conclusion :


                      E[X|Z] = 251{Z=0} + 401{Z=10} + 451{Z=20} + 551{Z=30}



              On considère l'espace de probabilité ([0, 1], B([0, 1]), λ ). Soient X et Z deux
variables aléatoires dénies par
Exercice 2                                                                   [0,1]



                   X(ω) = 2ω 2 ,     Z(ω) = 21[0,1/2[ (ω) + ω1[1/2,1] (ω),     ∀ω ∈ Ω

   Montrer que E[X|Z](ω) = 1      1                 2           .
                                  6 [0,1/2[ (ω) + 2ω 1[1/2,1] (ω)


Correction :
   Valeurs de Z :

   Sur [0, 1/2[ : Z(ω) = 2
   Sur [1/2, 1] : Z(ω) = ω
   Donc σ(Z) = {∅, [0, 1], [0, 1/2[, [1/2, 1]} (en fait plus riche sur [1/2, 1])
              E[X|Z]
       {Z = 2} c'est l'événement [0, 1/2[
   Calcul de              :
   Sur            :


                                   E[X|Z = 2]= E[X|ω ∈ [0, 1/2[]
                                               R 1/2 2
                                                      2ω dω
                                             = 0R 1/2
                                                   0    dω
                                                          1/2
                                               2 · 13 ω 3 0
                                                      
                                             =
                                                     1/2
                                                    1
                                               2 · 24      1/12   1
                                             =          =       =
                                                1/2         1/2   6

   Sur [1/2, 1] : Z(ω) = ω
   Donc sachant Z = z avec z ∈ [1/2, 1], on sait que ω = z.
   Donc :
                                 E[X|Z = z] = E[2ω 2 |ω = z] = 2z 2
   Conclusion :
                                         1
                              E[X|Z](ω) = 1[0,1/2[ (ω) + 2ω 2 1[1/2,1] (ω)
                                         6


            Soient X et Y deux v.a.r. indépendantes de loi exponentielle de paramètre 1. On
pose Z = X + Y . Déterminer la loi du couple (X, Z). En déduire la densité conditionnelle de X
Exercice 3


sachant Z et E[X|Z].
Correction :



                                                    2
~~~

## Page 3

~~~text
   Loi du couple (X, Z) :
   On a X ∼ Exp(1) et Y ∼ Exp(1) indépendantes.
   Transformation : (X, Y ) → (X, Z) avec Z = X + Y .
   Inverse : (X, Z) → (X, Z − X) = (X, Y )
   Jacobien : |J| = 1
   Densité de (X, Y ) :
                  f(X,Y ) (x, y) = e−x e−y 1R+ (x)1R+ (y) = e−(x+y) 1R+ (x)1R+ (y)
   Densité de (X, Z) : avec y = z − x
                                  f(X,Z) (x, z) = e−z 1{0≤x≤z} (x, z)
   Densité marginale de Z :
                                            Z z
                                  fZ (z)=         e−z dx = ze−z 1R+ (z)
                                             0
   C'est la loi Gamma Γ(2, 1).
   Densité conditionnelle :

                                          f(X,Z) (x, z)  e−z  1
                           fX|Z (x|z) =                 = −z = 1[0,z] (x)
                                             fZ (z)      ze   z
   C'est la loi uniforme sur [0, z] !
   Espérance conditionnelle :
                                                  Z z
                                                        1    1 z2   z
                              E[X|Z = z] =           x · dx = ·   =
                                                        z    z  2   2
   Donc :
                                                   0


                                                                 Z
                                             E[X|Z] =
                                                                 2



             Soient X une v.a.r. qui suit une loi de Poisson de paramètre λ > 0 et Y = 2⌊X/2⌋
où ⌊·⌋ désigne la partie entière. Calculer E[Y |X] et E[X|Y ].
Exercice 4




Correction :
   Calcul de E[Y |X] :
   Y = 2⌊X/2⌋    est une fonction de X , donc :
                                        E[Y |X] = Y = 2⌊X/2⌋
   Calcul de E[X|Y ] :
   Y prend les valeurs {0, 2, 4, 6, . . .} (nombres pairs).
   Sachant Y = 2k, on a ⌊X/2⌋ = k, donc 2k ≤ X < 2k + 2, c'est-à-dire X ∈ {2k, 2k + 1}.
   Calculons :
                                                           P (X = 2k)
                       P (X = 2k|Y = 2k)=
                                                   P (X = 2k) + P (X = 2k + 1)
                                                                     2k
                                                             e−λ (2k)!
                                                                  λ
                                             =          λ   2k      λ     2k+1
                                                   e−λ (2k)! + e−λ (2k+1)!
                                                      λ2k
                                                     (2k)!
                                             = λ2k       λ2k+1
                                               (2k)! + (2k+1)!
                                                        1              2k + 1
                                             =           λ
                                                                 =
                                                   1 + 2k+1          2k + 1 + λ


                                                        3
~~~

## Page 4

~~~text
     De même :                                                         λ
                                 P (X = 2k + 1|Y = 2k) =
                                                                   2k + 1 + λ
     Donc :
                                                 2k + 1                    λ
                       E[X|Y = 2k]= 2k ·                  + (2k + 1) ·
                                               2k + 1 + λ              2k + 1 + λ
                                           2k(2k + 1) + (2k + 1)λ
                                         =
                                                 2k + 1 + λ
                                           (2k + 1)(2k + λ)
                                         =
                                              2k + 1 + λ
                                                2kλ + λ − λ
                                         = 2k +
                                                 2k + 1 + λ
                                                λ(Y + 1)
                                         =Y +
                                                Y +1+λ
     Donc :
                                                               λ(Y + 1)
                                          E[X|Y ] = Y +
                                                               Y +1+λ



            Considérons l'exemple du dé où Ω = {1, 2, . . . , 6} et P ({i}) = . Soient F = {∅, Ω},
                                                                                      1

F = {∅, {1, 2, 3}, {4, 5, 6}, Ω}, F = P(Ω) et X : Ω → R t.q. X(i) = max(i − 4, 0).
Exercice 5                                                                                        1
                                                                                      6
 2                                   3

  1. Trouver σ(X). X est F -mesurable? F -mesurable? F -mesurable?
                                 3                 1                    2
  2. Calculer E[X|F ] pour tout i ∈ {1, 2, 3}.
                        i


Correction :
     1. Tribu engendrée par X :
   Valeurs de X :
   X(1) = 0, X(2) = 0, X(3) = 0, X(4) = 0
   X(5) = 1, X(6) = 2
   Donc σ(X) = {∅, {1, 2, 3, 4}, {5}, {6}, {5, 6}, . . .}
   En fait, σ(X) est la tribu la plus petite rendant X mesurable :
                σ(X) = {∅, {1, 2, 3, 4}, {5}, {6}, {5, 6}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 6}, Ω}

     Mesurabilité :

   X est F -mesurable : OUI (car F = P(Ω))
               3                              3
   X est F -mesurable : NON (car {5, 6} ∈/ F )
               1                                           1
   X est F -mesurable : NON (car {5} ∈/ F )
               2                                       2
     2. Espérances conditionnelles :
     E[X] = 61 (0 + 0 + 0 + 0 + 1 + 2) = 63 = 12
     E[X|F1 ] :
     La tribu est triviale, donc :
              F1
                                                                    1
                                            E[X|F1 ] = E[X] =
                                                                    2
     E[X|F2 ] :
     Sur           :
        {1, 2, 3} X = 0     toujours
                                             E[X|F2 ]1{1,2,3} = 0

                                                       4
~~~

## Page 5

~~~text
   Sur {4, 5, 6} : X ∈ {0, 1, 2}
                                                        0+1+2
                                   E[X|F2 ]1{4,5,6} =         =1
                                                          3
   Donc :
                                   E[X|F2 ] = 0 · 1{1,2,3} + 1 · 1{4,5,6}
   E[X|F3 ] :
                                              E[X|F3 ] = X
(car F = P(Ω) contient toute l'information)
      3




           Soient X et Y deux variables aléatoires réelles intégrables. On suppose que E[X|Y ] =
Y et E[Y |X] = X p.s.
Exercice 7



  1. Montrer que X = Y p.s.
  2. Soit Y = 0 et X une v.a. discrète à valeurs dans {−1, 1} avec P (X = −1) = P (X = 1) = . 1

     Montrer que E[X|Y ] = Y p.s. et que X ̸= Y p.s.                                          2




Correction :
   1. Montrons X = Y p.s. :
   Par la tour d'espérance :
                                       E[X]= E[E[X|Y ]] = E[Y ]

   De même :
                                          E[X 2 ]= E[E[X 2 |Y ]]

   Or, par Jensen (ou calcul direct) :
                                       E[X 2 |Y ] ≥ E[X|Y ]2 = Y 2

   Donc :
                                             E[X 2 ] ≥ E[Y 2 ]
   Par symétrie, E[Y ] ≥ E[X ], donc E[X ] = E[Y ].
                         2         2              2         2

   Maintenant :
                             0= E[(X − Y )2 ] = E[X 2 ] − 2E[XY ] + E[Y 2 ]

   Il reste à montrer que E[XY ] = E[X ].     2

   Par tour d'espérance :
                 E[XY ] = E[E[XY |X]] = E[X · E[Y |X]] = E[X · X] = E[X 2 ]

   Donc E[(X − Y ) ] = 0, d'où X = Y p.s.
                     2


   Si Y = 0 (constante), alors σ(Y ) = {∅, Ω}.
   2. Contre-exemple :


   Donc :                                                 1    1
                             E[X|Y ] = E[X] = (−1) ·        +1· =0=Y
                                                          2    2
   Mais clairement X ̸= Y p.s. car X ∈ {−1, 1} et .       Y =0
   Ceci montre que E[X|Y ] = Y seul ne sut pas à conclure       X=Y        !
                                             5
~~~

## Page 6

~~~text
             Soient X et Y deux variables aléatoires de Bernoulli indépendantes et de paramètre
        . Soit Z = 1        . Calculer E[X|Z] et E[Y |Z].
Exercice 8
p ∈]0, 1[             {X+Y =0}



             si X + Y = 0, c'est-à-dire si X = Y = 0.
Correction :
    Z=1
    Z=0      si X + Y ≥ 1.
    Probabilités :


                              P (Z = 1)= P (X = 0, Y = 0) = (1 − p)2
                              P (Z = 0)= 1 − (1 − p)2 = 2p − p2

    E[X|Z = 1] :
    SachantZ=1      , on sait que X = 0 et Y = 0. Donc :
                                             E[X|Z = 1] = 0

    E[X|Z = 0] :
   Sachant , on a X + Y ≥ 1. Les cas possibles sont :
           Z=0
   (X, Y ) = (1, 0) : prob p(1 − p)
   (X, Y ) = (0, 1) : prob (1 − p)p
   (X, Y ) = (1, 1) : prob p    2

   Probabilité conditionnelle :
                                          p(1 − p) + p2   p(1 − p + p)    p
                     P (X = 1|Z = 0) =                  =              =
                                             2p − p2        p(2 − p)     2−p
    Donc :                                                  p
                                        E[X|Z = 0] =
                                                           2−p
    Conclusion :
                                                             p
                                 E[X|Z] = 0 · 1{Z=1} +          ·1
                                                           2 − p {Z=0}
    Par symétrie : E[Y |Z] = E[X|Z].
             Soient X une variable aléatoire positive sur un espace de probabilité (Ω, F, P ) et G
une sous-tribu de F . Soit Y = E[X|G].
Exercice 9


   Montrer que {Y > 0} est le plus petit ensemble G-mesurable (aux ensembles négligeables
près) qui contient {X > 0}.
Correction :
    Étape 1 : {Y     > 0} est G -mesurable
    Puisque Y = E[X|G] est G-mesurable, l'ensemble {Y > 0} est automatiquement G-mesurable.
               {X > 0} ⊂ {Y > 0}
    Sur {X > 0}, on a X > 0. Montrons que Y > 0 p.s. sur cet ensemble.
    Étape 2 :                          (à un ensemble négligeable près)


    Supposons par l'absurde qu'il existe A ∈ G avec P (A ∩ {Y = 0} ∩ {X > 0}) > 0.
    Par dénition de l'espérance conditionnelle :
                                         Z             Z
                                              Y dP =       XdP
                                          A            A

   SurR A ∩ {Y = 0} ∩ {X > 0} :
      A∩{Y =0}Y dP = 0

                                                   6
~~~

## Page 7

~~~text
  R                XdP > 0
       A∩{Y =0}∩{X>0}
  Ceci donnerait une contradiction car R Y dP < R XdP .
  Donc {X > 0} ⊂ {Y > 0} p.s.                        A              A

             {Y > 0}
  Soit B ∈ G tel que {X > 0} ⊂ B p.s.
   Étape 3 :            est minimal


  Il faut montrer que {Y > 0} ⊂ B p.s.
  Sur B , on a X = 0 p.s. (car {X > 0} ⊂ B).
             c

  Donc pour tout A ∈ G :              Z
                                                            XdP = 0
                                                    A∩B c
   Par dénition de Y :            Z                        Z
                                               Y dP =                   XdP = 0
                                   A∩B c                        A∩B c
   Comme ceci est vrai pour tout A ∈ G, on a Y = 0 p.s. sur B .                   c

   Donc {Y > 0} ⊂ B p.s.
   Conclusion : {Y > 0} est le plus petit ensemble G -mesurable contenant {X > 0}.


             Soient X et Y deux variables aléatoires réelles dénies sur un espace de probabilité
       , telles que E[X ] et E[Y ] existent.
Exercice 10
(Ω, F, P )                2            2

   Montrer que si E[Y |G] = X et E[X ] = E[Y ] alors X = Y p.s.
                                               2             2


Correction :
   Hypothèses :

   E[Y |G] = X p.s.
   E[X ] = E[Y ]
             2     2



   Par la tour d'espérance :
   Étape 1 : Relation entre les espérances


                                       E[Y ] = E[E[Y |G]] = E[X]


   Par l'inégalité de Jensen pour l'espérance conditionnelle (avec φ(x) = x convexe) :
   Étape 2 : Utiliser l'inégalité de Jensen conditionnelle
                                                                                      2


                                       E[Y 2 |G] ≥ (E[Y |G])2 = X 2


   En prenant l'espérance des deux côtés :
   Étape 3 : Prendre l'espérance




                                           E[E[Y 2 |G]] ≥ E[X 2 ]

   Par la tour d'espérance :
                                                   E[Y 2 ] ≥ E[X 2 ]
   Mais par hypothèse, E[Y ] = E[X ].
                               2           2

   Donc on a égalité dans l'inégalité de Jensen :
                                            E[Y 2 |G] = X 2             p.s.
    L'égalité dans l'inégalité de Jensen pour une fonction strictement convexe implique que la
   Étape 4 : Égalité dans Jensen implique constance


variable est constante conditionnellement.
    Donc Y = E[Y |G] = X p.s.
   Méthode alternative :



                                                            7
~~~

## Page 8

~~~text
   On peut aussi calculer directement :
                                    E[(Y − X)2 ]= E[Y 2 ] − 2E[XY ] + E[X 2 ]
                                                        = E[Y 2 ] − E[X 2 ] − 2E[XY ] + 2E[X 2 ]
                                                        = 0 − 2E[XY ] + 2E[X 2 ]
                                                        = 2(E[X 2 ] − E[XY ])

   Calculons E[XY ] :
                                                        E[XY ]= E[E[XY |G]]
                                                                = E[X · E[Y |G]]
                                                                = E[X · X] = E[X 2 ]

   Donc :
                                           E[(Y − X)2 ] = 2(E[X 2 ] − E[X 2 ]) = 0
   Ce qui implique Y = X p.s.
Exercice (Examen 2017)      Soit
                               U = (X, Y ) un vecteur aléatoire gaussien de loi N (m, K) où
                                                                    ′
                                                                                                        2

m = (0, 0) et K =               .
                            
            ′         1 1/2

   On pose W = X et Z = 2X − Y .
                     1/2 1

  1. Trouver la loi de (W, Z) .             ′

  2. Exprimer Y en fonction de W et Z .
  3. Montrer que E[X Y |(2X − Y )] existe et calculer la.
                                     2



Correction :
   1. Loi de (W, Z) :

                                    avec A =
                                                           
                                                        1 0
   (W, Z) = A(X, Y )
                                                        2 −1
   Donc (W, Z) ∼ N (0, AKA )                    T

   Calculons :
                                2
                                                  
                             1 0    1   1/2      1 1/2
                      AK =                   =
                            2 −1    1/2 1       3/2 0
                                                   
                         T     1 1/2   1 2        1 3/2
                    AKA =                     =
                              3/2 0    0 −1      3/2 3

   Donc
                             
                         1 3/2
        (W, Z) ∼ N2 0,
                        3/2 3
   2. Expression de Y :
   W =X          et
             Z = 2X − Y                   , donc :
                                                         Y = 2X − Z = 2W − Z

   3. E[X
                2 Y |Z] :

   E[X 2 Y |Z] = E[W 2 (2W − Z)|Z] = E[2W 3 − W 2 Z|Z]
   = 2E[W 3 |Z] − ZE[W 2 |Z]
   Pour calculer, utilisons la loi conditionnelle de W sachant Z :
                                                                        (3/2)2
                                                                                                 
                                                             3/2                              Z 1
                                         W |Z ∼ N                Z, 1 −              =N        ,
                                                              3           3                   2 4

                                                                        8
~~~

## Page 9

~~~text
Donc E[W |Z] = et Var(W |Z) =
                Z                  1

Alors E[W |Z] = Var(W |Z) + E[W |Z] = +
                2                  4
          2                            2   1   Z2

Pour E[W |Z] : utiliser W = + ε où ε ∼ N (0, 1/4) indépendant de Z .
         3                  Z
                                           4   4

Après développement (long) :2



                                                  Z3 Z
                                E[X 2 Y |Z] = −     −
                                                  8   8




                                           9
~~~
