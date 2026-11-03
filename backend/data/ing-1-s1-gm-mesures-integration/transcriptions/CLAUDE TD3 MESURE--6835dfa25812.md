# CLAUDE TD3 MESURE.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14DqgFCJT9b9O_fRJXm6ZxowQ37cK9E3Q) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                         CY-Tech - Département Mathématiques
                          1ère année Ingénieurs - Génie Mathématique
                                    Mesure & intégration




         TD3  Intégration de fonctions mesurables positives


Intégrale d'une fonction étagée positive  Rappel 1.
Soit φ ∈ E + (Ω, T ) et m
                        i=1 ai 1Ai sa représentation
                                                 R canonique. On appelle
                                                                       Pintégrale de φ sur Ω
                   P
par rapport à la mesure µ et on note Ω φdµ ou Ω φ(x)dµ(x), la somme m    i=1 ai µ(Ai ) :
                                       R

                                        Z               m
                                                        X
                                                φdµ =         ai µ(Ai )
                                            Ω           i=1




EXERCICE 1 Vérier que la fonction indicatrice 1R est δ0 -intégrable sur R mais n'est pas
λ-intégrable sur R.

Correction :
   La fonction indicatrice 1R est la fonction constante égale à 1 sur R.
    Pour la mesure de Dirac δ0 :
                                 Z
                                     1R dδ0 = δ0 (R) = 1 < +∞
                                    R

Donc 1R est δ0 -intégrable sur R.
    Pour la mesure de Lebesgue λ :
                                        Z
                                            1R dλ = λ(R) = +∞
                                        R

Donc 1R n'est pas λ-intégrable sur R.


EXERCICE 2 Soient Ω = N, T = P(N) et µc la mesure de comptage dénie sur (N, P(N)).
  1. Soit A ∈ P(N). Montrer que µc (A) =            n∈N 1A (n).
                                                  P

  2. Soit φ une fonction étagée positive sur (N, P(N)). Montrer que                        n∈N φ(n).
                                                                                R          P
                                                                                N φdµc =


Correction :
   1. Par dénition, la mesure de comptage µc compte le nombre d'éléments d'un ensemble :
                                                            X
                      µc (A) = Card(A) = #{n ∈ N : n ∈ A} =     1A (n)
                                                                          n∈N

En eet, 1A (n) = 1 si n ∈ A et 1A (n) = 0 si n ∈
                                                / A, donc la somme compte exactement les
éléments de A.




                                                        1
~~~

## Page 2

~~~text
                 Pm
   2. Soit φ =    i=1 ai 1Ai la représentation canonique de φ (avec ai > 0 distincts et Ai disjoints).
Alors :
                             Z                  m
                                                X                      m
                                                                       X          X
                                  φdµc =              ai µc (Ai ) =          ai          1
                              N                 i=1                    i=1        n∈Ai
                                                m X
                                                X                     m
                                                                     XX
                                           =                ai =                  ai 1Ai (n)
                                                i=1 n∈Ai             n∈N i=1
                                                X
                                           =          φ(n)
                                                n∈N




EXERCICE 3 (Additivité domaniale) Soit φ une fonction étagée positive sur un espace mesuré
(Ω, T , µ). Pour F et G deux ensembles mesurables disjoints, montrer que
                                Z           Z         Z
                                     φdµ =     φdµ +      φdµ.
                                         F ∪G              F             G


Correction P
           :
        φ= m
                                                                                 Pm
    SoitP      i=1 ai 1Ai la représentation canonique de φ. On note que φ1F =      i=1 ai 1Ai ∩F et
          m
φ1G = i=1 ai 1Ai ∩G .
    Puisque F et G sont disjoints, on a Ai ∩ F et Ai ∩ G disjoints, et Ai ∩ (F ∪ G) = (Ai ∩ F ) ∪
(Ai ∩ G).
    Donc :
                   Z              Z              Xm
                          φdµ =      φ1F ∪G dµ =    ai µ(Ai ∩ (F ∪ G))
                      F ∪G            Ω                        i=1
                                     m
                                     X
                                 =         ai µ((Ai ∩ F ) ∪ (Ai ∩ G))
                                     i=1
                                     Xm
                                 =         ai [µ(Ai ∩ F ) + µ(Ai ∩ G)] (car disjoints)
                                     i=1
                                     Xm                          m
                                                                 X
                                 =         ai µ(Ai ∩ F ) +             ai µ(Ai ∩ G)
                                     i=1                         i=1
                                     Z                Z
                                 =         φdµ +           φdµ
                                      F                G




EXERCICE 4 Soit f une fonction réelle dénie pour tout x ∈ R par
                                         f (x) = 1[1;2] (x) + 51[3;5] (x).

On note λ la mesure de Lebesgue, δ3/2 la mesure de Dirac concentrée en 32 et µd la mesure de
comptage. Calculer en justiant vos calculs les intégrales suivantes :
                             Z               Z                  Z
                        I1 =    f dλ, I2 =       f dδ3/2 , I3 =    f dµd
                                  R                        R                             R


Correction :

                                                             2
~~~

## Page 3

~~~text
     Calcul de I1 :
                                             Z                Z
                                                                                      
                                    I1 =             f dλ =           1[1;2] + 51[3;5] dλ
                                                 R            R
                                         = λ([1; 2]) + 5λ([3; 5])
                                         = (2 − 1) + 5(5 − 3)
                                         = 1 + 10 = 11


     Calcul de I2 :
                                         Z                    Z
                                                                                      
                                  I2 =           f dδ3/2 =            1[1;2] + 51[3;5] dδ3/2
                                           R                  R
                                     = δ3/2 ([1; 2]) + 5δ3/2 ([3; 5])
                                     =1+5·0=1

car 32 ∈ [1; 2] mais 32 ∈
                        / [3; 5].
     Calcul de I3 :
                                             Z                Z
                                                                                      
                                    I3 =           f dµd =            1[1;2] + 51[3;5] dµd
                                               R              R
                                      = µd ([1; 2]) + 5µd ([3; 5])

Or [1; 2] et [3; 5] contiennent chacun une innité (non dénombrable) de points, donc µd ([1; 2]) =
+∞ et µd ([3; 5]) = +∞.
Ainsi, I3 = +∞.




Théorème de convergence monotone ou de Beppo-Levi  Rappel 2.
Soit (fn )n∈N une suite croissante de fonctions de L+ (Ω, T ) qui tend µ-p.p vers une fonction f ,
alors
   1. f ∈ L+ (Ω, T ),
   2. La suite    fn dµ n∈N converge en croissant vers f dµ.
               R                                     R



EXERCICE 5 Soit l'espace mesuré (R, B(R), λ) où λ est la mesure de Lebesgue et soit
                                         fn (x) = 1 − e−n cos x 1[0,π/2] .
                                                               


Calculer limn→+∞         fn dλ.
                     R


Correction :
    Pour x ∈ [0, π/2], on a cos x ∈ [0, 1]. La suite (fn (x)) est croissante car :

                fn+1 (x) − fn (x) = e−n cos x − e−(n+1) cos x = e−n cos x (1 − e− cos x ) ≥ 0


    De plus, pour x ∈ [0, π/2] :
                                                                                   (
                                                                  −n cos x
                                                                                   1 si cos x > 0
                         lim fn (x) = lim                1−e                     =
                         n→+∞                    n→+∞                               0 si cos x = 0

                                                                  3
~~~

## Page 4

~~~text
Or cos x = 0 seulement pour x = π/2. Donc fn → 1[0,π/2) presque partout.
   Par le théorème de convergence monotone (Beppo-Levi) :
                                     Z          Z
                                 lim    fn dλ =   1[0,π/2) dλ
                                        n→+∞ R                   R
                                                           = λ([0, π/2))
                                                             π
                                                           =
                                                             2




EXERCICE 6 Soient Ω = N, T = P(N) et µ la mesure de comptage dénie sur (Ω, T ).
Pour n ∈ N, soit fn = 1{n} . Déterminer            N limn→+∞ fn dµ et limn→+∞ N fn dµ. Commenter vos
                             R                         R

résultats.

Correction :
   Calcul de limn→+∞ fn : Pour tout k ∈ N xé, fn (k) = 1{n} (k) = 0 pour n ̸= k. Donc
pour n assez grand (i.e., n > k ), on a fn (k) = 0. Ainsi :

                                    lim fn (k) = 0 pour tout k ∈ N
                                    n→+∞

Donc limn→+∞ fn = 0 (la fonction nulle).
   D'où :                      Z               Z
                                   lim fn dµ =   0 dµ = 0
                                         N n→+∞                  N

    Calcul de limn→+∞ N fn dµ : Pour chaque n :
                            R

                                Z                  Z
                                        fn dµ =         1{n} dµ = µ({n}) = 1
                                    N               N

Donc :                                         Z
                                         lim           fn dµ = lim 1 = 1
                                        n→+∞ N                  n→+∞


    Commentaire : On a         N limn→+∞ fn dµ = 0 ̸= 1 = limn→+∞ N fn dµ.
                                R                                              R

    Ceci montre qu'on ne peut pas toujours intervertir limite et intégrale. Le théorème de conver-
gence monotone ne s'applique pas ici car la suite (fn ) n'est pas croissante (les fonctions prennent
la valeur 1 en des points diérents qui se déplacent).


EXERCICE 7 Soit (fn )n≥0 une suite de fonctions mesurables positives sur (Ω, T , µ). On dénit
la fonction F pour tout x ∈ Ω par
                                                          +∞
                                                          X
                                               F (x) =          fn (x).
                                                          n=0

Montrer que la fonction F est mesurable positive et que
                                         Z               +∞ Z
                                                         X                
                                              F dµ =                 fn dµ .
                                          Ω              n=0     Ω



Correction :

                                                          4
~~~

## Page 5

~~~text
    Posons pour tout N ∈ N : SN (x) = N    n=0 fn (x).
                                         P
     F est mesurable positive : Chaque fn est mesurable positive, donc chaque SN est
mesurable positive (somme nie de fonctions mesurables positives). De plus, la suite (SN ) est
croissante et converge vers F . Par théorème, la limite d'une suite croissante de fonctions mesu-
rables positives est mesurable positive. Donc F ∈ L+ (Ω, T ).
     Calcul de l'intégrale : Par linéarité de l'intégrale pour les sommes nies :
                             Z            Z XN           N Z
                                                         X
                                 SN dµ =        fn dµ =        fn dµ
                                  Ω                 Ω n=0                n=0 Ω

   La suite (SN ) est croissante et converge vers F . Par le théorème de convergence monotone
(Beppo-Levi) :
                Z                 Z                   N Z
                                                      X             +∞ Z
                                                                    X
                   F dµ = lim        SN dµ = lim            fn dµ =       fn dµ
                     Ω        N →+∞ Ω                    N →+∞
                                                                     n=0 Ω                     n=0 Ω




EXERCICE 8 Soit (Ω, T , λ) un espace mesuré où λ est la mesure de Lebesgue.R Soit (fn )n une
suite décroissante de fonctions mesurables et positives sur Ω. On suppose que                          Ω f0 dλ < +∞.
Montrer que
   1. la suite (fn )n converge, on note f la limite de (fn )n ;
   2. f est λ-intégrable ;
   3. limn→+∞ Ω fn dλ = Ω f dλ.
                 R          R


Correction :
  1. Convergence de (fn ) : La suite (fn ) est décroissante et minorée par 0. Par le théorème
de convergence monotone pour les suites décroissantes, (fn (x)) converge pour tout x ∈ Ω vers
une limite f (x) ≥ 0. Donc la suite (fn ) converge ponctuellement vers f .
   2. f est λ-intégrable : Puisque (fn ) est décroissante, on a fn ≥ f pour tout n. En particulier,
f0 ≥ f , donc 0 ≤ f ≤ f0 . Par monotonie de l'intégrale :
                                       Z          Z
                                  0≤       f dλ ≤   f0 dλ < +∞
                                              Ω                 Ω
Donc f est λ-intégrable.
    3. Passage à la limite dans l'intégrale : Posons gn = f0 − fn . Alors (gn ) est une suite
croissante de fonctions positives (car (fn ) est décroissante) qui converge vers g = f0 − f ≥ 0.
    Par le théorème de convergence monotone appliqué à (gn ) :
                                             Z          Z
                                       lim      gn dλ =    gdλ
                                           n→+∞ Ω                        Ω
c'est-à-dire :                    Z                Z                   Z                 Z
                            lim           f0 dλ −        fn dλ       =           f0 dλ −       f dλ
                          n→+∞        Ω              Ω                       Ω             Ω

    Puisque      Ω f0 dλ < +∞, on peut simplier :
              R
                                                    Z                Z
                                            lim          fn dλ =             f dλ
                                           n→+∞ Ω                        Ω




                  ING1 GM  TD3                                                                                 2/2


                                                            5
~~~
