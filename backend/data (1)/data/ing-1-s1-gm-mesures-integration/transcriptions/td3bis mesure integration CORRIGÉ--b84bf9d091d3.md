# td3bis mesure integration CORRIGÉ.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1h7ojyIMGnsx2wGaVlxm37AfzIPm1JiVk) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Exercice 1
Soit (E, A, µ) un espace mesuré et f : E → R une fonction mesurable. On suppose que f est intégrable sur E.         S∞
    Définition : Un ensemble A ∈ A est dit σ-fini s’il existe une suite (An )n≥1 d’ensembles mesurables tels que A = n=1 An
et µ(An ) < ∞ pour tout n ≥ 1.
    Le but de cet exercice est de démontrer que l’ensemble A = {x ∈ E : f (x) ̸= 0} est σ-fini.

  1. Pour tout entier naturel n ≥ 1, on définit l’ensemble
                                                                                                 1
                                                          An = {x ∈ E : |f (x)| ≥                  }.
                                                                                                 n
     Montrer que pour tout n ≥ 1, An ∈ A.
                     S∞
  2. Montrer que A = n=1 An .

  3. Montrer que pour tout n ≥ 1,                                               Z
                                                                 1
                                                                   µ(An ) ≤             |f | dµ.
                                                                 n              An

  4. En déduire que pour tout n ≥ 1, µ(An ) < ∞.

  5. Conclure que l’ensemble A est σ-fini.


Corrigé
  1. Pour tout n ≥ 1, la fonction x 7→ |f (x)| est mesurable car f est mesurable. L’ensemble An est l’image réciproque de
     l’intervalle fermé [ n1 , +∞[ par cette fonction. Comme l’intervalle [ n1 , +∞[ est un borélien et que l’image réciproque d’un
     borélien par une fonction mesurable est un ensemble mesurable, on a bien An ∈ A.
                                          implique |f (x)| > 0. Il existe donc un entier n ≥ 1 tel que |f (x)| ≥ n1 , c’est-à-dire
  2. Soit x ∈ A. Alors f (x) ̸= 0, ce qui S
                                            ∞
     x ∈ An . On a donc montré que A ⊂ n=1 An .
                              S∞                                                                                     1
     Réciproquement, si x ∈ n=1 An , alorsS∞il existe un entier n ≥ 1 tel que x ∈ An , ce qui signifie que |f (x)| ≥ n > 0. Donc
     f (x) ̸= 0 et x ∈ A. On a montré que n=1 An ⊂ A.
                                     S∞
     Par double inclusion, on a A = n=1 An .
  3. Pour tout n ≥ 1, la fonction indicatrice 1An est mesurable et positive. De plus, pour tout x ∈ An , on a |f (x)| ≥ n1 , donc
     1
     n 1An (x) ≤ |f (x)|1An (x). Par monotonie de l’intégrale, on a :
                                                             Z                  Z
                                                         1
                                                                  1An dµ ≤              |f |1An dµ.
                                                         n   E                      E

     Ce qui donne :
                                                                                Z
                                                                 1
                                                                   µ(An ) ≤             |f | dµ.
                                                                 n              An

  4. En utilisant l’inégalité de la question 3 et la croissance de l’intégrale, on a pour tout n ≥ 1 :
                                                                     Z                     Z
                                                       1
                                                         µ(An ) ≤           |f | dµ ≤            |f | dµ.
                                                       n               An                    E
                                           R
     Comme f est intégrable sur E, on a        E
                                                   |f | dµ < ∞. Donc, pour tout n ≥ 1,
                                                                            Z
                                                           µ(An ) ≤ n           |f | dµ < ∞.
                                                                            E
                          S∞
  5. On a montré que A = n=1 An (question 2) et que pour tout n ≥ 1, µ(An ) < ∞ (question 4). Donc A est une union
     dénombrable d’ensembles de mesure finie, ce qui signifie que A est σ-fini.
~~~

## Page 2

~~~text
Exercice 2
Soit f une fonction mesurable au sens de Lebesgue, à valeurs réelles, définie sur [0, +∞[, telle que :
   1. f est intégrable au sens de Lebesgue sur tout sous-intervalle fini de [0, +∞[.
   2. limx→+∞ f (x) = c ∈ R.
   Le but de cet exercice est de démontrer que
                                                            Z
                                                          1
                                                     lim          f dµL = c.
                                                   a→+∞ a [0,a]

   où µL désigne la mesure de Lebesgue.

  1. En utilisant l’hypothèse 2, montrer que :

                                                    ∀ε > 0, ∃N ∈ R, ∀x > N, |f (x) − c| < ε.

  2. Pour a > N , montrer que
                                                            Z                               Z
                                                        1                      1
                                                                   f dµL − c ≤                       |f − c| dµL .
                                                        a    [0,a]             a             [0,a]


  3. En déduire que pour a > N ,
                                        Z                                 Z                              Z                      !
                                    1                     1
                                              f dµL − c ≤                              |f − c| dµL +              |f − c| dµL       .
                                    a   [0,a]             a                   [0,N ]                      [N,a]


  4. Montrer que
                                                                                  (a − N )
                                                                        lim                ε = ε.
                                                                        a→+∞         a
                                                    R
  5. En utilisant l’hypothèse 1, montrer que            [0,N ]
                                                                 |f − c| dµL est finie.

  6. Montrer que                                                          Z
                                                                      1
                                                                  lim                  |f − c| dµL = 0.
                                                                 a→+∞ a       [0,N ]

  7. Conclure que
                                                                              Z
                                                                      1
                                                                  lim                  f dµL − c = 0.
                                                                 a→+∞ a        [0,a]


  8. En déduire que                                                               Z
                                                                         1
                                                                     lim                   f dµL = c.
                                                                    a→+∞ a         [0,a]


Corrigé
  1. L’hypothèse 2 signifie que f (x) tend vers c lorsque x tend vers l’infini. Par définition de la limite, cela se traduit par : pour
     tout ε > 0, il existe un réel N tel que pour tout x > N , on a |f (x) − c| < ε.
  2. Pour a > N , on a :


                                                Z                                     Z          Z
                                            1                     1                            1
                                                      f dµL − c =                     f dµL −          c dµL
                                            a   [0,a]             a             [0,a]          a [0,a]
                                                                               Z
                                                                             1
                                                                          =           (f − c) dµL
                                                                             a [0,a]
                                                                              Z
                                                                            1
                                                                          ≤         |f − c| dµL
                                                                            a [0,a]
~~~

## Page 3

~~~text
3. En utilisant la relation de Chasles pour l’intégrale, on a :
                                                 Z                       Z                                Z
                                                         |f − c| dµL =                |f − c| dµL +                  |f − c| dµL .
                                                 [0,a]                       [0,N ]                          [N,a]

   En combinant avec l’inégalité de la question 2, on obtient :

                                             Z                                Z                               Z                          !
                                         1                     1
                                                   f dµL − c ≤                               |f − c| dµL +               |f − c| dµL         .
                                         a   [0,a]             a                 [0,N ]                        [N,a]

4. On a :
                                                                                       
                                                              (a − N )                N        Nε
                                                                       ε=          1−     ε=ε−    .
                                                                 a                    a        a

   Comme N et ε sont des constantes, on a lima→+∞ Naε = 0. Donc :

                                                                                     (a − N )
                                                                         lim                  ε = ε.
                                                                       a→+∞             a
5. L’hypothèse 1 stipule que f est intégrable sur tout sous-intervalle fini de [0, +∞[. En particulier, f est intégrable sur [0, N ].
   Comme
   R           c est une constante, la fonction (f − c) est également intégrable sur [0, N ]. Donc, par définition de l’intégrabilité,
     [0,N ]
            |f − c| dµL est finie.

6. On a :
                                                                         Z
                                                                   1                                       1
                                                                0≤                    |f − c| dµL ≤          M,
                                                                   a      [0,N ]                           a
            R
   où M =       [0,N ]
                         |f − c| dµL est une constante finie (d’après la question 5).
   Comme lima→+∞ a1 M = 0, on a, par le théorème des gendarmes :
                                                                              Z
                                                                     1
                                                                 lim                         |f − c| dµL = 0.
                                                                a→+∞ a            [0,N ]

7. En utilisant les questions 1, 3, 4 et 6, on obtient :

                                        Z                                                Z                           Z                           !
                                    1                           1
                                lim             f dµL − c ≤ lim                                     |f − c| dµL +              |f − c| dµL
                               a→+∞ a     [0,a]            a→+∞ a                          [0,N ]                      [N,a]
                                                                                     Z                                         Z
                                                                       1                                               1
                                                                ≤ lim                            |f − c| dµL + lim                       |f − c| dµL
                                                                  a→+∞ a              [0,N ]                      a→+∞ a         [N,a]
                                                                                         (a − N )
                                                                ≤ 0 + lim                         ε
                                                                         a→+∞               a
                                                                = ε.

   Comme ε > 0 est arbitraire, on a :

                                                                                 Z
                                                                     1
                                                                  lim                        f dµL − c = 0.
                                                                a→+∞ a             [0,a]

8. La limite de la valeur absolue de l’expression est nulle, donc la limite de l’expression elle-même est également nulle :

                                                                                 Z                       !
                                                                             1
                                                                 lim                         f dµL − c       = 0.
                                                               a→+∞          a     [0,a]

   Ce qui donne finalement :
                                                                                     Z
                                                                        1
                                                                       lim                       f dµL = c.
                                                                   a→+∞ a                [0,a]
~~~

## Page 4

~~~text
Exercice 3
Soit (X, A, µ) un espace mesuré. Soit f une fonction mesurable à valeurs réelles étendues, intégrable sur X. Pour tout n ∈ N,
on définit l’ensemble En = {x ∈ X : |f (x)| ≥ n}.
   Le but de cet exercice est de démontrer que limn→∞ µ(En ) = 0.

  1. Montrer que X = E0 .
  2. Pour tout n ∈ N, exprimer l’ensemble En \ En+1 en fonction de f .
  3. Montrer que la famille d’ensembles {En \ En+1 : n ∈ N} est constituée d’ensembles mesurables deux à deux disjoints.

  4. Montrer que
                                                                ∞
                                                                [
                                                                    (En \ En+1 ) = X.
                                                                n=0

  5. En utilisant l’intégrabilité de f , montrer que
                                              Z               ∞ Z
                                                              X                              ∞
                                                                                             X
                                      ∞>          |f | dµ =                      |f | dµ ≥         nµ(En \ En+1 ).
                                              X               n=0     En \En+1               n=0


  6. Montrer que
                                              ∞
                                              X                             ∞
                                                                            X
                                                    nµ(En \ En+1 ) =              n[µ(En ) − µ(En+1 )].
                                              n=0                           n=0

  7. En développant la somme précédente, montrer que
                                                       ∞
                                                       X                             ∞
                                                                                     X
                                                              nµ(En \ En+1 ) =               µ(En ).
                                                       n=0                           n=1


  8. Conclure que limn→∞ µ(En ) = 0.


Corrigé
  1. Par définition, E0 = {x ∈ X : |f (x)| ≥ 0} = X car la valeur absolue est toujours positive.
  2. Pour tout n ∈ N, on a :
                                                  En \ En+1 = {x ∈ X : n ≤ |f (x)| < n + 1}.

  3. Pour tout n ∈ N, l’ensemble En \ En+1 est mesurable car c’est la différence de deux ensembles mesurables. De plus, si
     n ̸= m, les ensembles En \ En+1 et Em \ Em+1 sont disjoints car les intervalles [n, n + 1[ et [m, m + 1[ sont disjoints.

  4. Soit x ∈ X. Si f (x) = 0, alors x ∈ ES    0 \ E1 . Sinon, il existe un unique entier n ≥ 0Stel que n ≤ |f (x)| < n + 1, et donc
                                                 ∞                                               ∞
     x ∈ En \ En+1 . Dans tous les cas, x ∈ n=0 (En \ En+1 ). On a donc montré que X ⊂ n=0 (En \ En+1 ). L’inclusion inverse
     est évidente.
                                    R                                                  S∞
  5. Par l’intégrabilité de f , on a X |f | dµ < ∞. D’après la question 4, on a X = n=0 (En \ En+1 ), et les ensembles En \ En+1
     sont mesurables et deux à deux disjoints (question 3). Par le théorème de convergence monotone pour les séries d’intégrales,
     on a :
                                                       Z                  ∞ Z
                                                                          X
                                                              |f | dµ =                      |f | dµ.
                                                        X                 n=0    En \En+1


     De plus, pour tout n ∈ N et tout x ∈ En \ En+1 , on a |f (x)| ≥ n. Donc :
                                          Z                           Z
                                                       |f | dµ ≥                  n dµ = nµ(En \ En+1 ).
                                           En \En+1                    En \En+1

     On obtient donc l’inégalité souhaitée.
  6. Pour tout n ∈ N, on a En+1 ⊂ En , donc µ(En \ En+1 ) = µ(En ) − µ(En+1 ).
~~~

## Page 5

~~~text
  7. En développant la somme et en regroupant les termes, on obtient :


                        ∞
                        X
                              n[µ(En ) − µ(En+1 )] = µ(E0 ) − µ(E1 ) + 2[µ(E1 ) − µ(E2 )] + 3[µ(E2 ) − µ(E3 )] + · · ·
                        n=0
                                                   = µ(E1 ) + µ(E2 ) + µ(E3 ) + · · ·
                                                     X∞
                                                   =    µ(En ).
                                                        n=1

                                              P∞
  8. D’après les questions 5 et 7, la série    n=1 µ(En ) est convergente. Par conséquent, son terme général tend vers 0, c’est-à-dire
     limn→∞ µ(En ) = 0.


Exercice 4
Soit (X, A, µ) un espace mesuré. Soit f une fonction mesurable à valeurs réelles étendues, intégrable sur X.

  1. Montrer que pour tout ε > 0, il existe δ > 0 tel que pour tout A ∈ A avec µ(A) < δ, on a :
                                                            Z
                                                               f dµ < ε.
                                                                            A

     Indication : On pourra introduire la suite de fonctions (fn )n∈N définie par :
                                                                  (
                                                                   f (x) si f (x) ≤ n
                                                         fn (x) =
                                                                   n     sinon

     et utiliser le théorème de convergence monotone.

  2. Soit (En )n∈N une suite d’ensembles mesurables tels que limn→∞ µ(En ) = 0. Montrer que
                                                              Z
                                                         lim     f dµ = 0.
                                                                      n→∞       En


Corrigé
  1. Pour tout n ∈ N, on définit la fonction fn comme dans l’indication.
     a) Montrer que la suite (fn )n∈N est croissante et converge simplement vers f .
     b) Montrer que chaque fonction fn est bornée et mesurable.
     c) En utilisant le théorème de convergence monotone, montrer qu’il existe N ∈ N tel que :
                                                              Z                  Z
                                                                                                  ε
                                                                      fN dµ −            f dµ <     .
                                                              X                      X            2
                     ε
     d) On pose δ = 2N . Soit A ∈ A tel que µ(A) < δ. Montrer que :

                                                   Z                   Z                          Z
                                                        f dµ ≤              (f − fN ) dµ +                fN dµ
                                                    A                   A                             A
                                                                       Z                          Z
                                                                  ≤         (f − fN ) dµ +              |fN | dµ
                                                                        X                         A
                                                                    ε
                                                                  <    + N µ(A)
                                                                    2
                                                                    ε         ε
                                                                  < +N ·
                                                                    2        2N
                                                                  = ε.
~~~

## Page 6

~~~text
                                                                                                    R
2. Soit ε > 0. D’après la question 1, il existe δ > 0 tel que pour tout A ∈ A avec µ(A) < δ, on a       A
                                                                                                            f dµ < ε.
  Comme limn→∞ µ(En ) = 0, il existe n0 ∈ N tel que pour tout n ≥ n0 , on a µ(En ) < δ. Donc, pour tout n ≥ n0 , on a :
                                                         Z
                                                               f dµ < ε.
                                                          En
                        R
  Ceci montre que limn→∞ En f dµ = 0.
~~~
