# CLAUDE TD4 MESURE.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1f0uT6vtNCnZn6Z2_1ZXV1qiAdIdKWD8s) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                           CY-Tech - Département Mathématiques
                           1ère année Ingénieurs - Génie Mathématique
                                           Mesure & intégration




                   TD4  Intégration de fonctions mesurables


Fonction réelle intégrable  Rappel 1.
Une fonction f de Ω dans R est dite µ-intégrable si f est (T , B(R))-mesurable et
                           Z                      Z
                              f + dµ < +∞ et         f − dµ < +∞.



EXERCICE 1 Soient (Ω, T , µ) et (R+ , B(R+ ), λ) deux espaces mesurés où µ est une mesure
nie sur Ω et λ la mesure de Lebesgue sur R+ . On considère l'application mesurable

                                       f : (Ω, T , µ) → (R+ , B(R+ ), λ).

On suppose que Ω f 2 dµ < +∞.
               R

   Soient A1 = {x ∈ Ω, 0 ≤ f (x) ≤ 1} et A2 = {x ∈ Ω, f (x) > 1}.
  1. Montrer que A1 et A2 sont deux ensembles mesurables, A1 ∈ T et A2 ∈ T .
  2. Montrer que A1 f dµ < +∞.
                 R

  3. Montrer que A2 f dµ < +∞.
                 R

  4. Que peut-on déduire sur l'intégrabilité de f sur Ω ? Justier.

Correction :
  1. Mesurabilité de A1 et A2 : Puisque f est mesurable, on a :

                            A1 = {x ∈ Ω : 0 ≤ f (x) ≤ 1} = f −1 ([0, 1])
                            A2 = {x ∈ Ω : f (x) > 1} = f −1 (]1, +∞[)

Les ensembles [0, 1] et ]1, +∞[ sont des boréliens de R+ , donc par mesurabilité de f , on a
A1 , A2 ∈ T .
     2. Intégrale sur A1 : Sur A1 , on a 0 ≤ f ≤ 1, donc :
                          Z           Z
                              f dµ ≤      1 dµ = µ(A1 ) ≤ µ(Ω) < +∞
                             A1              A1

car µ est une mesure nie. Donc A1 f dµ < +∞.
                                       R

    3. Intégrale sur A2 : Sur A2 , on a f > 1, donc f 2 > f . Par inégalité de Cauchy-Schwarz
(ou simplement par monotonie) :
                            Z          Z          Z
                                           2
                               f dµ ≤     f dµ ≤     f 2 dµ < +∞
                                  A2              A2         Ω

Donc       A2 f dµ < +∞.
       R



                                                       1
~~~

## Page 2

~~~text
   4. Intégrabilité de f : On a Ω = A1 ∪ A2 avec A1 ∩ A2 = ∅. Par additivité de l'intégrale :
                            Z         Z         Z
                               f dµ =    f dµ +   f dµ < +∞
                               Ω          A1           A2

De plus, f ≥ 0, donc f est µ-intégrable sur Ω.




Théorème de la convergence dominée  Rappel 2.
Soient (fn )n∈N une suite de fonctions de L(Ω, T ) et g ∈ L1 (Ω, T , µ). On suppose que
   (fn )n∈N converge vers f µ-p.p
   Pour tout n ∈ N, |fn | ≤ g .
Alors                              (
                                    f ∈ L1 (Ω, T , µ)
                                              R       R
                                    limn→+∞ fn dµ = f dµ



EXERCICE 2 Soit (fn )n∈N une suite de fonctions dénie, pour tout entier n, par
                                                        xn
                              ∀x ∈ R,    fn (x) =            1 + (x).
                                                     1 + xn+2 R
  1. Déterminer la limite simple de la suite (fn )n∈N .
  2. Pour tout entier n, on considère l'intégrale In =      R fn (x)dx. Calculer la limite limn→+∞ In .
                                                          R


Correction :
  1. Limite simple : Pour x ∈ R+ , étudions le comportement de fn (x) :
                                                                n
   Si 0 ≤ x < 1 : xn → 0 et xn+2 → 0, donc fn (x) = 1+x
                                                       x        0
                                                         n+2 → 1+0 = 0

   Si x = 1 : fn (1) = 1+1
                         1
                            = 21 pour tout n
                                                                    n
   Si x > 1 : xn → +∞ et xn+2 → +∞, donc fn (x) = 1+x
                                                     x          1        1    1
                                                       n+2 = x−n +x2 → 0+x2 = x2

Donc :                                               
                                                     0
                                                             si 0 ≤ x < 1
                           f (x) = lim fn (x) = 12            si x = 1
                                  n→+∞
                                                              si x > 1
                                               
                                               1
                                                 x2

    2. Calcul de limn→+∞ In : On veut appliquer le théorème de convergence dominée. Il faut
trouver une fonction dominante g .
                                   xn
    Pour 0 ≤ x < 1 : fn (x) = 1+x            n
                                    n+2 ≤ x ≤ 1
                             xn
    Pour x ≥ 1 : fn (x) = 1+x n+2 = x−n +x2 ≤ x2 car x
                                          1        1      −n ≥ 0

    Donc |fn (x)| ≤ g(x) = 1[0,1] (x) + x12 1]1,+∞[ (x).
    Vérions que g est intégrable :
                                                             1 +∞
             Z            Z 1          Z +∞                   
                                                1
                g(x)dx =      1 dx +              dx = 1 + −      = 1 + 1 = 2 < +∞
              R            0            1      x2            x 1

   Par le théorème de convergence dominée :
                                  Z            Z 1        Z +∞
                                                               1
                        lim In =     f (x)dx =     0 dx +       2
                                                                  dx
                       n→+∞        R            0          1   x
                                =0+1=1


                                                 2
~~~

## Page 3

~~~text
EXERCICE 3 Soit (fn )n∈N∗ une suite de fonctions dénie, pour n ∈ N∗ par
                                                       x    n
                          ∀x ∈ R,       fn (x) = sin                 1R∗ (x).
                                                        n x(1 + x2 )
  1. Montrer que ∀n ∈ N, fn est mesurable.
  2. Calculer limn→+∞ fn .
  3. Calculer, en justiant, limn→+∞ R fn (x)dλ(x).
                                    R


Correction :
  1. Mesurabilité : fn est le produit et la composition de fonctions mesurables (continues),
donc fn est mesurable pour tout n ∈ N∗ .
    2. Limite simple : Pour x ̸= 0, on a nx → 0 quand n → +∞. En utilisant le développement
limité sin(u) ∼ u quand u → 0 :
                                  x      n      x      n         1
                     fn (x) = sin            2
                                                ∼ ·        2
                                                              =
                                   n x(1 + x )    n x(1 + x )   1 + x2

Donc limn→+∞ fn (x) = 1+x 1
                            2 pour x ̸= 0.

    Pour x = 0, fn (0) = 0 pour tout n, donc la limite est aussi 0 (qui coïncide avec 1+0
                                                                                       1
                                                                                         2 = 1 si
on prolonge par continuité, mais la fonction vaut 0 en 0).
    3. Calcul de la limite de l'intégrale : On cherche une fonction dominante. On a | sin(u)| ≤
|u| pour tout u, donc :
                                   x        n         |x|     n            1
                  |fn (x)| = sin                      ≤     ·           =
                                    n    |x|(1 + x2 )    n |x|(1 + x2 )   1 + x2

La fonction g(x) = 1+x
                     1
                       2 est intégrable sur R :

                   Z
                          1                     +∞   π  π
                             2
                               dx = [arctan(x)] −∞ =   − −   = π < +∞
                     R 1+x                           2     2

   Par le théorème de convergence dominée :
                                Z                Z
                                                                1
                           lim     fn (x)dλ(x) =                   2
                                                                     dx = π
                             n→+∞ R                          R 1+x




EXERCICE 4 (Mesure dénie par une densité) Soient (Ω, T , µ) un espace mesuré et f une
fonction positive et (Ω, T )-mesurable. On considère la fonction d'ensembles ν dénie par
                                                Z         Z
                              ∀A ∈ T , ν(A) =      f dµ =     1A f dµ.
                                                       A          Ω

  1. Montrer que ν dénit une mesure sur (Ω, T ). La fonction f s'appelle la densité de ν par
     rapport à µ.
  2. Soit g : (Ω, T ) → (R, B(R)) une fonction mesurable et positive.
      (a) Montrer que Ω gdν = Ω f gdµ.
                         R        R

      (b) En déduire que g est ν -intégrable si et seulement si gf est µ-intégrable.

                                                   3
~~~

## Page 4

~~~text
   3. Soit g : (Ω, T ) → (R, B(R)) une fonction mesurable de signe quelconque.
       (a) g est ν -intégrable si et seulement si gf est µ-intégrable.
       (b) Montrer que Ω gdν = Ω f gdµ.
                          R         R


Correction :
  1. ν est une mesure R : Il fautR vérier les Rdeux propriétés :
   ν(∅) = 0 : ν(∅) = ∅ f dµ = Ω 1∅ f dµ = Ω 0 dµ = 0.
   σ -additivité : Soit (An ) une suite d'ensembles disjoints de T . Alors :
                                         !       Z                                     Z                       !
                                [                                                                X
                        ν           An       =            1S   n An
                                                                      f dµ =                           1An         f dµ
                                n                     Ω                                    Ω      n
                                                 Z X
                                             =                  1An f dµ
                                                      Ω n

Par le théorème de convergence monotone (série de fonctions positives) :
                                 XZ                X
                               =       1An f dµ =      ν(An )
                                                 n        Ω                            n

Donc ν est une mesure.
   2. Fonctions positives :
   (a) Montrons d'abord le résultat pour les fonctions étagées. Soit g = mi=1 ai 1Bi avec ai ≥ 0 :
                                                                        P

                        Z                m
                                         X                            m
                                                                      X            Z
                                gdν =            ai ν(Bi ) =                  ai               f dµ
                            Ω            i=1                          i=1              Bi
                                          m                                                    m
                                                      Z                        Z                               !
                                         X                                                     X
                                    =            ai           1Bi f dµ =                              ai 1Bi       f dµ
                                                          Ω                        Ω
                                      Zi=1                                                     i=1

                                    =     gf dµ
                                          Ω


   Pour g mesurable positive quelconque, il existe une suite croissante (gn ) de fonctions étagées
positives qui converge vers g . Par convergence monotone appliquée deux fois :
                        Z              Z           Z            Z
                           gdν = lim gn dν = lim gn f dµ =          gf dµ
                            Ω                n       Ω                    n        Ω                      Ω


    (b) g est ν -intégrable si et seulement si Ω gdν < +∞, c'est-à-dire Ω gf dµ < +∞, ce qui
                                                  R                          R

signie que gf est µ-intégrable.
    3. Fonctions de signe quelconque :
    (a) On a g = g + − g − avec g + , g − ≥ 0. Alors g est ν -intégrable si et seulement si g + et g −
sont ν -intégrables, ce qui équivaut (par la question 2b) à g + f et g − f sont µ-intégrables, soit
(gf )+ = g + f et (gf )− = g − f sont µ-intégrables, ce qui signie que gf est µ-intégrable.
    (b) Si g est ν -intégrable, par linéarité et la question 2a :
                                Z         Z            Z
                                   gdν =      g + dν −     g − dν
                                 Ω        ZΩ            ΩZ
                                        =       +
                                              g f dµ −       g − f dµ
                                          ZΩ              Ω        Z
                                                +     −
                                        = (g − g )f dµ =              gf dµ
                                                          Ω                                      Ω


                                                                      4
~~~

## Page 5

~~~text
EXERCICE 5 Montrer que toute mesure sur R de densité f vériant −∞
                                                                +∞
                                                                   f (x)dx = 1 est une
                                                                                    R

mesure de probabilité.

Correction :
   Soit ν la mesure de densité f par rapport à la mesure de Lebesgue λ : ν(A) =         A f dλ pour
                                                                                        R

tout A borélien.
   Pour que ν soit une mesure de probabilité, il faut vérier que ν(R) = 1.
   Or, par dénition :               Z          Z             +∞
                                   ν(R) =         f dλ =            f (x)dx = 1
                                              R               −∞

   Donc ν est bien une mesure de probabilité.


EXERCICE 6 Soient (Ω, T , µ) un espace mesuré, (Ω′ , A) un espace mesurable, et T : (Ω, T ) →
(Ω′ , A) une application mesurable. On considère la fonction d'ensembles µT dénie par :

                          ∀B ∈ A,        µT (B) = µ(T −1 (B)) = µ ◦ T −1 (B).

   1. Montrer que µT dénit une mesure sur (Ω′ , A). µT s'appelle mesure image de µ par T .
   2. Soit g : (Ω′ , A) → (R, B(R)) une fonction mesurable. Montrer que g est µT -intégrable si et
      seulement si l'application mesurable g ◦ T est µ-intégrable et que
                                         Z          Z
                                            gdµT =     g ◦ T dµ.
                                              Ω′               Ω



Correction :
  1. µT est une mesure :
   µT (∅) = 0 : µT (∅) = µ(T −1 (∅)) = µ(∅) = 0.
   σ -additivité : Soit (Bn ) une suite d'ensembles disjoints de A. Les ensembles T −1 (Bn )
sont disjoints dans T (car si x ∈ T −1 (Bi ) ∩ T −1 (Bj ) avec i ̸= j , alors T (x) ∈ Bi ∩ Bj = ∅,
contradiction).
   Donc :
                               !                     !!                       !
                        [                     [                 [
                    µT     Bn = µ T −1            Bn      =µ       T −1 (Bn )
                           n                             n                   n
                                         X                          X
                                                    −1
                                     =        µ(T        (Bn )) =        µT (Bn )
                                          n                          n

par σ -additivité de µ.
   2. Formule de changement de variable :
   Montrons d'abord le résultat pour les fonctions indicatrices. Soit B ∈ A :
                             Z
                                 1B dµT = µT (B) = µ(T −1 (B))
                                    Ω′

Or, (1B ◦ T )(x) = 1B (T (x)) = 1T −1 (B) (x), donc :
                           Z                 Z
                              1B ◦ T dµ =       1T −1 (B) dµ = µ(T −1 (B))
                               Ω                   Ω


                                                          5
~~~

## Page 6

~~~text
Donc l'égalité est vraie pour les fonctions indicatrices.
   Par linéarité, elle est vraie pour les fonctions étagées positives.
   Pour g mesurable positive, il existe une suite croissante (gn ) de fonctions étagées positives
convergeant vers g . Alors (gn ◦ T ) converge vers g ◦ T . Par convergence monotone :
                    Z                Z                Z              Z
                        gdµT = lim      gn dµT = lim gn ◦ T dµ =        g ◦ T dµ
                      Ω′               n       Ω′                      n   Ω              Ω


   Pour g de signe quelconque, on écrit g = g + − g − et on applique la linéarité.
   L'équivalence d'intégrabilité découle de l'égalité des intégrales appliquée à |g| :
                           Z             Z                Z
                                |g|dµT =     |g ◦ T |dµ =    |g| ◦ T dµ
                                  Ω′                   Ω                        Ω

Donc g est µT -intégrable si et seulement si g ◦ T est µ-intégrable.




Espace Lp  Rappel 4.
Soit p ∈ [1, +∞[. On dit que f est de puissance p-ième-intégrable, et on note f ∈ Lp (Ω, T , µ), si
f est mesurable et |f |p est µ-intégrable.
                                                          Z
                     f ∈ Lp (Ω, T , µ) ⇐⇒ f ∈ L(Ω, T ) et    |f |p dµ < +∞.
                                                                                    Ω
                                                    1/p
Si f ∈ Lp (Ω, T , µ), Np (f ) =          p                 .
                                  R
                                   Ω |f | dµ



EXERCICE 7 Soit f une fonction réelle strictement positive. On suppose que f ∈ L1 (Ω, T , µ)
et f1 ∈ L1 (Ω, T , µ). Montrer que Ω est ni.

Correction :
   Posons A1 = {x ∈ Ω : f (x) ≤ 1} et A2 = {x ∈ Ω : f (x) > 1}.
   Sur A1 , on a f ≤ 1, donc f1 ≥ 1. Donc :
                                  Z          Z          Z
                                                 1         1
                         µ(A1 ) =     1 dµ ≤       dµ ≤      dµ < +∞
                                   A1         A1 f       Ω f

   Sur A2 , on a f > 1, donc :
                                           Z                   Z                Z
                           µ(A2 ) =                 1 dµ <             f dµ ≤       f dµ < +∞
                                           A2                  A2               Ω


   Par conséquent :
                                       µ(Ω) = µ(A1 ) + µ(A2 ) < +∞
Donc Ω est de mesure nie.


EXERCICE 8 Soit (Ω, T , µ) un espace mesuré. On considère trois réels non nuls et positifs p, q
et r tels que
                                                       1 1 1
                                                        + = .
                                                       p q r
On suppose que f ∈ Lp (Ω, T , µ) et que g ∈ Lq (Ω, T , µ).

                                                                   6
~~~

## Page 7

~~~text
   1. Montrer que Nr (f g) ≤ Np (f )Nq (g).
   2. Montrer que la fonction f g est r-intégrable.

Correction :
  1. Inégalité de norme : De p1 + 1q = 1r , on déduit pr + qr = 1.
   Posons p′ = pr > 1 et q ′ = qr > 1 (car r < p et r < q ). On a p1′ + q1′ = pr + qr = 1, donc p′ et q ′
sont conjugués.
   Par l'inégalité de Hölder appliquée à |f |r et |g|r avec les exposants p′ et q ′ :
                      Z              Z              1/p′ Z             1/q′
                              r                r p′                r q′
                         |f g| dµ ≤       (|f | ) dµ           (|g| ) dµ
                         Ω                 Ω                               Ω
                                         Z                  1/p′ Z                      1/q′
                                                  rp′                          rq ′
                                    =          |f |     dµ                 |g|        dµ
                                           Ω                           Ω
                                         Z              r/p Z                 r/q
                                                  p                        q
                                    =          |f | dµ                 |g| dµ
                                           Ω                       Ω

car rp′ = r · pr = p et rq ′ = q .
    En prenant la racine r-ième :
                      Z              1/r Z         1/p Z        1/q
                                  r               p              q
          Nr (f g) =         |f g| dµ     ≤   |f | dµ         |g| dµ      = Np (f )Nq (g)
                         Ω                        Ω                        Ω


    2. f g est r-intégrable : Puisque f ∈ Lp et g ∈ Lq , on a Np (f ) < +∞ et Nq (g) < +∞. Par
la question 1 :
                                 Nr (f g) ≤ Np (f )Nq (g) < +∞
Donc Ω |f g|r dµ < +∞, ce qui signie que f g ∈ Lr (Ω, T , µ).
       R




Fonction essentiellement bornée  Rappel 5.
Une fonction f de L(Ω, T ) est dite essentiellement bornée s'il existe r ≥ 0 tel que |f | ≤ r µ-p.p.
On note L∞ (Ω, T , µ) l'ensemble des fonctions essentiellement bornées de L(Ω, T ).

                    L∞ (Ω, T , µ) = {f ∈ L(Ω, T ), ∃r ≥ 0 tel que |f | ≤ r µ-p.p.}

et N∞ (f ) = inf{r ≥ 0 : |f | ≤ r µ-p.p.}.


EXERCICE 9
   1. Soit f ∈ L1 et g ∈ L∞ . Montrer que f g est µ-intégrable et que

                                         N1 (f × g) ≤ N1 (f ) × N∞ (g).

   2. Supposons que µ(Ω) < +∞ et 1 ≤ p1 ≤ p2 ≤ +∞. Montrer que L∞ ⊂ Lp2 ⊂ Lp1 ⊂ L1 .

Correction :
  1. Produit f g : Puisque g ∈ L∞ , il existe M ≥ 0 tel que |g| ≤ M µ-p.p. On peut prendre
M = N∞ (g).
  Alors |f g| ≤ |f | · M = M |f | µ-p.p. Donc :
                 Z                Z
                      |f g|dµ ≤ M    |f |dµ = M · N1 (f ) = N∞ (g) · N1 (f ) < +∞
                    Ω                Ω


                                                         7
~~~

## Page 8

~~~text
car f ∈ L1 . Donc f g ∈ L1 et N1 (f g) ≤ N1 (f ) · N∞ (g).
    2. Inclusions des espaces Lp : On suppose µ(Ω) < +∞.
     L∞ ⊂ Lp2 : Soit f ∈ L∞ . Alors |f | ≤ N∞ (f ) µ-p.p., donc |f |p2 ≤ [N∞ (f )]p2 µ-p.p.
                              Z
                                  |f |p2 dµ ≤ [N∞ (f )]p2 µ(Ω) < +∞
                                Ω

Donc f ∈ Lp2 .
    Lp2 ⊂ Lp1 : Soit f ∈ Lp2 . Posons A = {x : |f (x)| ≤ 1} et B = {x : |f (x)| > 1}.
   Sur A : |f |p1 ≤ |f |p2 (car p1 ≤ p2 et |f | ≤ 1)
   Sur B : |f |p1 ≤ |f |p2 (car p1 ≤ p2 et |f | > 1)
   Donc |f |p1 ≤ |f |p2 partout, et :
                                   Z              Z
                                      |f |p1 dµ ≤    |f |p2 dµ < +∞
                                    Ω            Ω

Donc f ∈ Lp1 .
    Lp1 ⊂ L1 : Cas particulier de l'inclusion précédente avec p2 = p1 et p′1 = 1.



              ING1 GM  TD4                                                                    3/3




                                                 8
~~~
