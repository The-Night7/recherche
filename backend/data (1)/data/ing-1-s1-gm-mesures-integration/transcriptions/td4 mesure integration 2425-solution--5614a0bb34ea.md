# td4 mesure integration 2425-solution.pdf

[Ouvrir l’original](https://drive.google.com/open?id=15fDaziwIkIFQWEXrzl9XKGhLL9YU57PN) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                           TD4 – Mesure et Intégration
                     Ingénieur 1 – Génie Mathématique – 2025/2026



      Avant-propos

                      Ce corrigé détaillé est dédié à l’ensemble de la promotion.
          Une pensée particulière accompagne ceux qui, tout au long du semestre, ont préféré
      l’observation extérieure et distante à la présence en cours. Puisse ce document combler le
                                   fossé qu’ils ont eux-mêmes creusé.




Exercice 1
Soient (Ω, T , µ) et (R+ , B(R+ ), λ) deux espaces mesurés, où µ est une mesure finie sur Ω et λ la mesure
de Lebesgue   sur R+ . On considère l’application mesurable f : (Ω, T , µ) → (R+ , B(R+ ), λ). On suppose
que Ω f 2 dµ < +∞. Soient A1 = {x ∈ Ω | 0 ≤ f (x) ≤ 1} et A2 = {x ∈ Ω | f (x) > 1}.
    R

1. Montrer que RA1 et A2 sont deux ensembles mesurables, A1 ∈ T et A2 ∈ T .
2. Montrer que A1 f dµ < +∞.
                 R
3. Montrer que A2 f dµ < +∞.
4. Que peut-on déduire sur l’intégrabilité de f sur Ω ? Justifier.


Corrigé de l’Exercice 1
  1. Mesurabilité de A1 et A2 :

     Pour A1 : L’application f est mesurable de (Ω, T ) dans (R+ , B(R+ )). Par définition, A1 =
     {x ∈ Ω | f (x) ∈ [0, 1]} = f −1 ([0, 1]).
       — L’intervalle [0, 1] est un fermé de R+ , c’est donc un ensemble borélien : [0, 1] ∈ B(R+ ).
       — Par définition de la mesurabilité de f , l’image réciproque d’un borélien appartient à la tribu
         de départ.
     ⇒ On en déduit que A1 ∈ T .

     Pour A2 : La fonction f prend ses valeurs dans R+ . Par conséquent, pour tout x ∈ Ω, nous
     avons l’alternative suivante :
       — Soit 0 ≤ f (x) ≤ 1, ce qui correspond à x ∈ A1 .
       — Soit f (x) > 1, ce qui correspond à x ∈ A2 .
     Puisque f (x) ne peut pas être strictement négatif, ces deux cas couvrent l’intégralité de l’espace
     Ω et sont disjoints. Ainsi, A2 est exactement le complémentaire de A1 :

                                              A2 = Ω \ A1 = Ac1 .

     Justification : T est une tribu, elle est donc stable par passage au complémentaire. Puisque
     nous avons montré que A1 ∈ T , il en résulte immédiatement que Ac1 ∈ T . ⇒ Donc A2 ∈ T .




                                                    1
~~~

## Page 2

~~~text
2. Intégrabilité de f sur A1 :
   Sur l’ensemble A1 , on a par définition l’encadrement 0 ≤ f (x) ≤ 1. La fonction f est donc bornée
   sur cet ensemble. En intégrant cette inégalité sur A1 par rapport à la mesure µ :
                                      Z           Z
                                          f dµ ≤     1 dµ = µ(A1 ).
                                        A1                 A1

   Argument clé : Par monotonie de la mesure, µ(A1 ) ≤ µ(Ω). Or, l’énoncé précise que µ est une
   mesure finie, donc µ(Ω) < +∞.
                                   Z
                                       f dµ ≤ µ(Ω) < +∞.
                                               A1
              R
   ⇒ Ainsi,    A1 f dµ < +∞.
3. Intégrabilité de f sur A2 :
   Sur l’ensemble A2 , on a f (x) > 1. En multipliant par f (x) (qui est positif), on obtient l’inégalité :

                                    f (x) < (f (x))2        pour tout x ∈ A2 .

   Par monotonie de l’intégrale :              Z                Z
                                                     f dµ ≤             f 2 dµ.
                                                A2              A2

   De plus, l’intégrale sur une partie est inférieure à l’intégrale sur le tout (car f 2 ≥ 0) :
                                          Z             Z
                                                2
                                               f dµ ≤       f 2 dµ.
                                                A2                  Ω

                              2                                                            2 dµ < +∞. ⇒
                                                                                  R
               R suppose que f est intégrable sur Ω, c’est-à-dire
   Hypothèse : On                                                                     Ωf                  Par
   comparaison, A2 f dµ < +∞.
4. Intégrabilité de f sur Ω :
   Les ensembles A1 et A2 forment une partition de Ω (comme vu à la question 1). Par additivité
   de l’intégrale par rapport au domaine :
                                    Z        Z         Z
                                      f dµ =    f dµ +   f dµ.
                                       Ω               A1                  A2

   Nous avons montré que les deux termes de droite sont finis. De plus, comme f ≥ 0, on a |f | = f .
                                    Z           Z
                                      |f | dµ =    f dµ < +∞.
                                           Ω                Ω

   ⇒ On en déduit que f est intégrable sur Ω (c’est-à-dire f ∈ L1 (µ)).




                                                       2
~~~

## Page 3

~~~text
Corrigé de l’Exercice 2
Soit (fn )n∈N∗ la suite de fonctions définie sur R par :

                                                      xn
                                        fn (x) =           1R (x).
                                                   1 + xn+2 +
  1. Limite simple de la suite (fn ) :
     Soit x ∈ R+ fixé. Étudions la limite de la suite numérique (fn (x))n≥1 :
       — Cas 0 ≤ x < 1 : On a limn→+∞ xn = 0 et limn→+∞ xn+2 = 0.
                                                                0
                                                lim fn (x) =       = 0.
                                              n→+∞             1+0
                                                           n
       — Cas x = 1 : Pour tout n ∈ N∗ , fn (1) = 1+11 n+2 = 12 .

                                                                 1
                                                     lim fn (1) = .
                                                   n→+∞          2

       — Cas x > 1 : On factorise par le terme prépondérant xn+2 au dénominateur :
                                                      xn               1    1
                                   fn (x) =                        =      ·    1 .
                                              xn+2 (x−(n+2) + 1)        2
                                                                       x 1 + xn+2

                                       1
           Comme x > 1, on a limn→+∞ xn+2 = 0. Par opérations sur les limites :

                                                                   1
                                                    lim fn (x) =      .
                                                   n→+∞            x2

      ⇒ La suite (fn ) converge simplement sur R+ vers la fonction f définie par :
                                          
                                          0
                                                si 0 ≤ x < 1
                                   f (x) = 1/2   si x = 1
                                          
                                              2
                                           1/x si x > 1

      Remarque importante : L’ensemble {1} étant de mesure nulle pour la mesure de Lebesgue, on a
      l’égalité presque partout :
                                             1
                                     f (x) = 2 1]1,+∞[ (x) λ-p.p.
                                             x
  2. Calcul de la limite de l’intégrale In :
     Nous allons appliquer le Théorème de Convergence Dominée (TCD). Vérifions les hypo-
     thèses :
                                                                              Nn (x)
       — Mesurabilité : Soit n ∈ N∗ . La fonction fn est définie par fn (x) = Dn (x)
                                                                                     · 1R+ (x).
            — Les fonctions Nn : x 7→ xn et Dn : x 7→ 1 + xn+2 sont des fonctions polynomiales, elles
              sont donc continues sur R.
            — Vérification du domaine : Pour tout x ∈ R+ , on a xn+2 ≥ 0, donc le dénominateur
              vérifie Dn (x) ≥ 1 > 0. Il ne s’annule jamais sur le domaine d’étude.
                                                      xn
            — Par conséquent, la fonction x 7→ 1+x     n+2 est continue sur R+ (comme quotient de
              fonctions continues dont le dénominateur ne s’annule pas).
            — Or, toute fonction continue définie sur un borélien (ici R+ ) est mesurable par rapport à
              la tribu borélienne. L’indicatrice 1R+ étant également mesurable (car R+ est un fermé
              de R donc élément de B(R)), fn est mesurable par produit.


                                                      3
~~~

## Page 4

~~~text
 — Convergence simple : Comme montré à la question 1, la suite (fn ) converge simplement
   vers f sur R+ .
 — Hypothèse de domination : Cherchons une fonction g ∈ L1 (R+ ) (indépendante de n)
   telle que ∀n ∈ N∗ , ∀x ∈ R+ , |fn (x)| ≤ g(x).
      — Si x ∈ [0, 1] : On a 1 + xn+2 ≥ 1, donc :
                                                              xn
                                          |fn (x)| =                ≤ xn ≤ 1.
                                                           1 + xn+2
      — Si x > 1 : On a 1 + xn+2 ≥ xn+2 , donc :
                                                            xn       xn     1
                                     |fn (x)| =               n+2
                                                                  ≤   n+2
                                                                          = 2.
                                                          1+x       x      x
     Définissons la fonction dominante g par :
                                                                1
                                    g(x) = 1[0,1] (x) +           1       (x).
                                                                x2 ]1,+∞[
     Intégrabilité de g :
     Par additivité de l’intégrale de Lebesgue sur les parties disjointes [0, 1] et ]1, +∞[, dont la
     réunion est R+ , on a
                           Z          Z                         Z
                                                                        1
                               g dλ =        1[0,1] (x) dλ(x) +           2
                                                                            dλ(x).
                            R+         [0,1]                     ]1,+∞[ x

      — Sur [0, 1], la fonction 1[0,1] est l’indicatrice d’un intervalle borné de mesure de Lebesgue
        λ([0, 1]) = 1, donc               Z
                                                      1 dλ(x) = λ([0, 1]) = 1.
                                              [0,1]

      — Sur ]1, +∞[, la fonction x 7→ x12 est continue (donc mesurable) et positive. L’intégrale de
        Lebesgue d’une fonction continue et positive sur un intervalle coïncide avec l’intégrale
        de Riemann impropre. On peut donc écrire
                                                                  1 +∞
                            Z                    Z +∞              
                                     1                  1
                                      2
                                        dλ(x) =            dx = −         = 1.
                              ]1,+∞[ x             1    x2        x 1

     Finalement,                      Z
                                              g dλ = 1 + 1 = 2 < +∞,
                                         R+

     ce qui montre que g ∈ L1 (R+ , λ).
⇒ Toutes les hypothèses du TCD sont réunies. On peut donc intervertir la limite et
l’intégrale :                Z          Z
                                   lim          fn (x) dx =          f (x) dx.
                                 n→+∞ R                          R
Calculons l’intégrale de la limite :
                         Z             Z 1        Z                      Z +∞
                                                                1                1
                            f (x) dx =     0 dx +                 dx +              dx.
                          R               0                 {1} 2         1      x2
L’intégrale sur [0, 1[ est nulle, et l’intégrale sur le singleton {1} est nulle (mesure de Lebesgue).
Il reste :
                                                          1 +∞
                                     Z +∞                 
                                             1
                                                dx =    −       = 1.
                                       1    x2            x 1
⇒ Finalement, limn→+∞ In = 1.


                                                      4
~~~

## Page 5

~~~text
Exercice 3
On considère la suite de fonctions (fn )n∈N∗ définie par :
                                     x      n
                        fn (x) = sin                 IR∗ (x) ∀x ∈ R, ∀n ∈ N∗ .
                                       n x(1 + x2 )

1. Mesurabilité de fn
Soit n ∈ N∗ fixé. La fonction fn peut s’écrire comme le produit de deux fonctions :

                                                                            n sin(x/n)
                         fn (x) = φn (x) × 1R∗ (x) avec φn (x) =                       .
                                                                            x(1 + x2 )

  — Étude de la fonction φn :
       — Le numérateur x 7→ n sin(x/n) est continu sur R (composée de fonctions continues).
       — Le dénominateur x 7→ x(1 + x2 ) est polynomial, donc continu sur R. Il ne s’annule que pour
         x = 0 (car 1 + x2 ≥ 1 > 0).
       — Par quotient de fonctions continues, φn est continue sur l’ouvert R∗ = R \ {0}.
       — Toute fonction continue sur un ouvert de R est mesurable par rapport à la tribu borélienne.
  — Étude de l’indicatrice : L’ensemble R∗ est un ouvert, c’est donc un borélien. Sa fonction
    indicatrice 1R∗ est donc mesurable.
⇒ La fonction fn est mesurable sur R comme produit de deux fonctions mesurables.

2. Limite simple de (fn )n∈N∗
Soit x ∈ R. Étudions la limite de la suite numérique (fn (x))n≥1 .
  — Cas x = 0 : Par définition de la fonction indicatrice 1R∗ , pour tout n ∈ N∗ , on a fn (0) = 0.
    Donc limn→+∞ fn (0) = 0.
  — Cas x ̸= 0 : On a 1R∗ (x) = 1. L’expression devient :
                                                          n          x
                                           fn (x) =              sin     .
                                                      x(1 + x2 )      n

     Analyse asymptotique : Lorsque n → +∞, le terme un = nx tend vers 0. On utilise l’équivalent
     usuel au voisinage de 0 : sin(u) ∼ u.
                                                    n        x      1
                                  fn (x)     ∼             ·     =        .
                                           n→+∞ x(1 + x2 )    n    1 + x2
                                        1
     Par conséquent, limn→+∞ fn (x) = 1+x 2.

⇒ La suite (fn ) converge simplement sur R vers la fonction f définie par :
                                                     (
                                                         1
                                      1                1+x2
                                                            si x ̸= 0
                           f (x) =        1 R∗ (x) =
                                   1 + x2             0     si x = 0

Remarque importante (Égalité presque partout) : En théorie de l’intégration de Lebesgue, les
ensembles de mesure nulle sont négligeables. L’ensemble des points où x 7→ f (x) diffère de la fonction
                        1
continue x 7→ g(x) = 1+x  2 est le singleton {0}. Or, pour la mesure de Lebesgue, λ({0}) = 0. On a
donc l’égalité fondamentale pour la suite de l’exercice :
                                                  1
                                     f (x) =                λ-p.p. sur R.
                                               1 + x2

                                                        5
~~~

## Page 6

~~~text
3. Calcul de la limite de l’intégrale
Nous appliquons le Théorème de Convergence Dominée (TCD). Vérifions les hypothèses :
  — Convergence simple : Comme établi à la question précédente, la suite (fn ) converge simplement
                                                                        1
    (et presque partout) sur R vers la fonction f définie par f (x) = 1+x 2.

  — Hypothèse de domination : Nous cherchons un majorant intégrable indépendant de n. Pour
    tout n ∈ N∗ et tout x ∈ R∗ , on utilise l’inégalité usuelle | sin(u)| ≤ |u|. En posant u = nx :

                                          n         x        n       x      1
                         |fn (x)| =          2
                                                sin     ≤          2
                                                                     ·   =        .
                                      x(1 + x )      n    |x|(1 + x ) n    1 + x2
                                                                                                    1
      Cette inégalité reste vraie pour x = 0 (où fn (0) = 0). Posons la fonction dominante g(x) = 1+x 2.

  — Intégrabilité de g (Justification du passage Lebesgue → Riemann) : La fonction g : x 7→
      1
    1+x2
         est continue sur R.
       — Elle est donc mesurable (tribu borélienne).
       — Comme elle est positive, son intégrale de Lebesgue sur R est égale à son intégrale de
         Riemann impropre.
      On peut donc calculer son intégrale à l’aide d’une primitive :
           Z                Z +∞
                                     1                            +∞   π  π
               g(x) dλ(x) =             2
                                          dx  =   lim  [arctan(x)]−∞ =   − −   = π < +∞.
             R                −∞ 1 + x          A→+∞                   2     2

      La fonction dominante g est donc bien intégrable sur R.
⇒ Les hypothèses du TCD sont vérifiées. On peut donc intervertir la limite et l’intégrale :
                    Z                Z                      Z
                                                                1
                lim   fn (x) dλ(x) =     lim fn (x) dλ(x) =        2
                                                                     dλ(x).
              n→+∞ R                  R n→+∞                 R 1+x

Le calcul de cette dernière intégrale a été effectué lors de la vérification de la domination.

                                               lim In = π.
                                              n→+∞




                                                     6
~~~

## Page 7

~~~text
Corrigé de l’Exercice 4 : Mesure définie par une densité
Soient (Ω, T , µ) un espace mesuré et f une fonction mesurable positive (la densité). On définit :
                                       Z         Z
                               ν(A) =     f dµ =    1A f dµ ∀A ∈ T .
                                                A                      Ω

  1. Montrons que ν est une mesure sur (Ω, T ) :
     La fonction f est positive et µ est une mesure positive, donc ν est à valeurs dans [0, +∞].
       — Mesure de l’ensemble vide :
                                                           Z
                                               ν(∅) =             f dµ = 0 (car µ(∅) = 0).
                                                              ∅

       — σ-additivité : SoitS(An )n∈N une suite d’ensembles mesurables de T , deux à deux dis-
         joints. Posons B = n∈N An . La fonction indicatrice de l’union disjointe est la somme des
         indicatrices :
                                                   +∞
                                                   X
                                             1B =      1A n .
                                                                               n=0

          Par définition de ν :
                                                                                         +∞
                                                       Z                        Z                       !
                                                                                         X
                                          ν(B) =              1B f dµ =                        1A n f       dµ.
                                                         Ω                       Ω       n=0

          Les fonctions un = 1An f , n ∈ N, sont mesurables (produit de mesurables) et positives
          (car f ≥ 0). D’après le Théorème de Convergence Monotone (forme série) :
                                           +∞           +∞ Z
                                       Z         !
                                           X           X
                                               un dµ =        un dµ.
                                                   Ω     n=0                         n=0 Ω

          Ce qui donne exactement :
                                                                       +∞ Z                     +∞
                                                            !
                                                [                      X                        X
                                           ν           An         =                  f dµ =           ν(An ).
                                               n∈N                     n=0 An                   n=0


     ⇒ ν est bien une mesure sur (Ω, T ).
  2. Cas où g est mesurable positive :
                                  R        R
     Nous allons prouver l’égalité Ω g dν = Ω gf dµ par la méthode standard (approximation par
     fonctions étagées).

     Étape 1 : g est une fonction indicatrice Soit g = 1A avec A ∈ T .
                          Z                  Z          Z
                            g dν = ν(A) et     gf dµ =    f dµ = ν(A).
                                     Ω                                     Ω              A

     L’égalité est vraie.

                                                                                                Pn
     Étape 2 : g est une fonction étagée positive Soit g =                                         i=1 ai 1Ai avec ai ≥ 0 et Ai ∈ T .
     Par linéarité de l’intégrale (pour ν et µ) :
                               n                   n                                     n
                Z                                             Z                  Z                       !            Z
                               X                   X                                     X
                      g dν =         ai ν(Ai ) =         ai            f dµ =                   ai 1Ai       f dµ =       gf dµ.
                  Ω            i=1                 i=1            Ai                 Ω    i=1                         Ω



                                                                       7
~~~

## Page 8

~~~text
  Étape 3 : g est une fonction mesurable positive quelconque Il existe une suite croissante
  de fonctions étagées positives (gn )n telle que gn ↗ g. Alors la suite (gn f )n est aussi une suite
  croissante de fonctions mesurables positives convergeant vers gf (car f ≥ 0). En appliquant le
  Théorème de Convergence Monotone (Beppo-Levi) deux fois :
                       Z                Z              Z            Z
                          g dν = lim       gn dν = lim    gn f dµ =     gf dµ.
                         Ω            n→∞ Ω                  n→∞ Ω                        Ω

  ⇒ L’égalité est démontrée pour toute fonction mesurable positive.
3. Cas où g est mesurable de signe quelconque :
   On décompose g en sa partie positive et sa partie négative : g = g + − g − , avec g + = max(g, 0)
   et g − = max(−g, 0). Remarquons que (gf )+ = g + f et (gf )− = g − f car f ≥ 0.
   (a) Intégrabilité :
                                                             Z                        Z
                          g est ν-intégrable ⇐⇒                  +
                                                                 g dν < ∞ et              g − dν < ∞.

        D’après le résultat de la question 2 (appliqué à g + et g − ) :
                                         Z                  Z
                                   ⇐⇒       g + f dµ < ∞ et    g − f dµ < ∞

                                                ⇐⇒ gf est µ-intégrable.

   (b) Formule de transfert : Si g est intégrable, on a par linéarité :
                                   Z         Z           Z
                                      g dν =      +
                                                g dν −      g − dν
                                            Ω                Ω                Ω
                             Z              Z                    Z                            Z
                                  +                 −                     +       −
                         =       g f dµ −           g f dµ =          (g − g )f dµ =              gf dµ.
                             Ω                  Ω                 Ω                           Ω

  ⇒ Pour toute fonction g ∈ L1 (ν), on a
                                                        R             R
                                                            g dν =        gf dµ.




                                                        8
~~~

## Page 9

~~~text
Corrigé de l’Exercice 5 : Densité de probabilité

                                             R B(R), λ) où λ est la mesure de Lebesgue. Soit f : R →
Contexte : On travaille sur l’espace mesuré (R,
R+ une fonction mesurable positive vérifiant R f dλ = 1.
On considère la mesure à densité ν définie par f par rapport à λ.
  1. Statut de mesure : D’après le résultat de l’Exercice 4 (Question 1), comme f est mesurable
     positive et λ est une mesure, l’application ν définie par :
                                                              Z
                                       ∀A ∈ B(R), ν(A) =         f dλ
                                                                   A

     est bien une mesure sur (R, B(R)).
  2. Vérification de la condition de probabilité : Une mesure est une probabilité si et seulement
     si la mesure de l’espace total vaut 1. Nous devons calculer ν(R).
     Utilisons la formule de transfert (Exercice 4, Question 2) :
                                                        Z          Z
                                ∀g mesurable positive,     g dν =     gf dµ.
                                                              Ω           Ω

     Appliquons ceci avec :
       — L’espace Ω = R et la mesure de référence µ = λ.
       — La fonction test g = 1R (la fonction constante égale à 1). Elle est mesurable (indicatrice
         d’un borélien) et positive.
     On obtient :                        Z              Z                 Z
                                ν(R) =        1R dν =       1R · f dλ =       f dλ.
                                          R             R                 R
                                         R +∞
     Hypothèse : L’énoncé précise que −∞ f (x) dx = 1. (Note : Pour une fonction positive, l’inté-
     grale de Lebesgue coïncide avec cette notation).

                                                  ν(R) = 1.

     ⇒ La mesure ν est une mesure sur R de masse totale 1. C’est donc une mesure de
     probabilité.




                                                   9
~~~

## Page 10

~~~text
Corrigé de l’Exercice 6 : Mesure image
Cadre :
 — (Ω, F, µ) un espace mesuré.
 — (Ω′ , A) un espace mesurable.
 — T : (Ω, F) → (Ω′ , A) une application mesurable.
 — On définit µT sur A par : ∀B ∈ A, µT (B) = µ(T −1 (B)).
  1. Montrons que µT définit une mesure sur (Ω′ , A) :
      — Non-négativité : Pour tout B ∈ A, T −1 (B) ∈ F (car T est mesurable). Donc µT (B) =
        µ(T −1 (B)) ∈ [0, +∞] car µ est une mesure positive.
      — Mesure de l’ensemble vide : On sait que T −1 (∅) = ∅.
                                          µT (∅) = µ(T −1 (∅)) = µ(∅) = 0.

      — σ-additivité : Soit (Bn )n∈N une suite d’ensembles de A, deux à deux disjoints. Posons
        An = T −1 (Bn ).
         — Propriété de l’image réciproque : Si les Bn sont disjoints, alors les An le sont aussi.
            En effet, si x ∈ Ai ∩ Aj , alors T (x) ∈ Bi ∩ Bj = ∅, ce qui est impossible.
         — On a aussi T −1 ( n Bn ) = n T −1 (Bn ) = n An .
                             S           S               S

        Par σ-additivité de la mesure µ :
                               +∞               +∞
                                       !              ! +∞               +∞
                               [                [          X             X
                          µT       Bn = µ           An =       µ(An ) =      µT (Bn ).
                                   n=0              n=0         n=0          n=0

     ⇒ µT est bien une mesure sur (Ω′ , A).
  2. Formule de transfert :
     Nous allons prouver l’équivalence et l’égalité par la méthode de la "Machine Standard".

     Étape 1 : g est une fonction indicatrice Soit g = 1B avec B ∈ A. On a g◦T (x) = 1B (T (x)).
     Or 1B (T (x)) = 1 ⇐⇒ T (x) ∈ B ⇐⇒ x ∈ T −1 (B). Donc g ◦ T = 1T −1 (B) .
                     Z                                 Z                Z
                        g dµT = µT (B) = µ(T −1 (B)) =   1T −1 (B) dµ =   g ◦ T dµ.
                         Ω′                                  Ω                   Ω

     L’égalité est vraie.

     Étape 2 : g est une fonction étagée positive Soit g = ni=1 ai 1Bi avec ai ≥ 0 et Bi ∈ A.
                                                             P
     Par linéarité de l’intégrale :
                    n                  n                     n
     Z                    Z                 Z              Z                !     Z
                   X                   X                     X
         g dµT =       ai    1Bi dµT =   ai   1Bi ◦ T dµ =     ai (1Bi ◦ T ) dµ =   g ◦ T dµ.
       Ω′          i=1        Ω′         i=1    Ω                 Ω   i=1                      Ω


     Étape 3 : g est une fonction mesurable positive Il existe une suite croissante de fonctions
     étagées positives (gn )n telle que gn ↗ g. Alors la suite (gn ◦ T )n est aussi une suite croissante de
     fonctions mesurables positives convergeant vers g ◦ T . En appliquant le Théorème de Conver-
     gence Monotone deux fois :
                        Z                 Z                Z                Z
                            g dµT = lim     gn dµT = lim gn ◦ T dµ =           g ◦ T dµ.
                              Ω′          Ω′                Ω                Ω

     ⇒
     R L’égalité est Rvraie pour toute fonction positive (dans [0, +∞]). Par conséquent,
      gdµT < ∞ ⇐⇒ g ◦ T dµ < ∞.

                                                     10
~~~

## Page 11

~~~text
Étape 4 : g est une fonction mesurable de signe quelconque On décompose g = g + −g − .
On a (g ◦ T )+ = g + ◦ T et (g ◦ T )− = g − ◦ T .
                                           Z              Z
                             1
                       g ∈ L (µT ) ⇐⇒          +
                                             g dµT < ∞ et   g − dµT < ∞
                      Z                     Z
                ⇐⇒         +
                          g ◦ T dµ < ∞ et       g − ◦ T dµ < ∞ (d’après l’étape 3)

                                       ⇐⇒ g ◦ T ∈ L1 (µ).
Si cette condition est vérifiée, on soustrait les égalités pour g + et g − pour obtenir le résultat
final.
⇒ g ∈ L1 (µT ) ⇐⇒ g ◦ T ∈ L1 (µ) et Ω′ g dµT = Ω g ◦ T dµ.
                                        R            R




                                             11
~~~

## Page 12

~~~text
Corrigé de l’Exercice 7 : Mesure finie
Données : Soit f une fonction mesurable strictement positive sur (Ω, T , µ). On suppose que f ∈ L1 (µ)
et f1 ∈ L1 (µ).

Méthode 1 : Utilisation de l’inégalité arithmético-géométrique
  — Inégalité ponctuelle (presque partout) : Hypothèse : La fonction f est strictement positive
                                         1
    µ-presque partout. Ainsi, f (x) et f (x)  sont définis et strictement positifs pour µ-presque tout
    x ∈ Ω.
                                                           √
    D’après l’Inégalité Arithmético-Géométrique ( ab ≤ a+b           2 ), on a µ-p.p. :
                                  s                                    
                                               1     1              1
                                     f (x) ·       ≤     f (x) +          .
                                             f (x)   2            f (x)

                       1
     Puisque f (x) · f (x) = 1, cela se simplifie en :

                                                 1        1 1
                                              1 ≤ f (x) +                      (µ-p.p.).
                                                 2        2 f (x)

  — Intégration : L’inégalité étant vraie presque partout entre fonctions mesurables positives, on
    peut l’intégrer sur Ω par rapport à µ :
                                   Z             Z            Z
                                               1            1    1
                                       1 dµ ≤        f dµ +         dµ.
                                     Ω         2 Ω          2 Ωf

  — Vérification des hypothèses : Hypothèse : On sait que Ω f < ∞ et Ω f1 < ∞. Le membre
                                                                   R       R

    de droite est donc une somme de nombres finis.
                     R
  — Résultat : Or, Ω 1 dµ = µ(Ω).
                                                             
                                            1             1
                                   µ(Ω) ≤       ∥f ∥1 +         < +∞.
                                            2             f 1

⇒ La mesure de l’espace total µ(Ω) est finie.

Méthode 2 : Utilisation de l’inégalité de Cauchy-Schwarz
                                                                                         R
  — Astuce de décomposition : On cherche à majorer µ(Ω) =                                  Ω 1 dµ. Comme f > 0 µ-p.p., on
    peut écrire pour µ-presque tout x :
                                                          p          1
                                                   1=      f (x) × p      .
                                                                    f (x)
                  √
     Posons u =       f et v = √1f . Ces fonctions sont définies µ-p.p.
  — Appartenance aux espaces L2 : Avant d’appliquer Cauchy-Schwarz, vérifions que u, v ∈ L2 (µ).
                            Z            Z p            Z
                                   2             2
                               |u| dµ = ( f ) dµ =         f dµ.
                                          Ω                    Ω                     Ω

     Or, par hypothèse, f ∈ L1 (µ), donc                  f < ∞, ce qui implique u ∈ L2 (µ).
                                                      R

     De même :                 Z                          Z             2          Z
                                               2                    1                  1
                                          |v| dµ =                 √          dµ =       dµ.
                                      Ω                    Ω         f               Ω f
     Par hypothèse, f1 ∈ L1 (µ), donc
                                                R 1                            2
                                                   f < ∞, ce qui implique v ∈ L (µ).


                                                               12
~~~

## Page 13

~~~text
 — Application du théorème : On applique l’Inégalité de Cauchy-Schwarz (∥uv∥1 ≤ ∥u∥2 ∥v∥2 ) :
                          Z p            Z       1/2 Z       1/2
                                 1                           1
                              f·√     dµ ≤     f dµ     ·      dµ      .
                           Ω      f          Ω             Ω f

                                                         s
                                              p              1
                                        µ(Ω) ≤ ∥f ∥1 ·               .
                                                             f   1

    Le produit de deux nombres réels finis est fini.
⇒ On retrouve que µ(Ω) < +∞.




                                                 13
~~~

## Page 14

~~~text
Corrigé de l’Exercice 8 : Généralisation de Hölder
Données : Soit (Ω, F, µ) un espace mesuré. Soient p, q, r trois réels strictement positifs vérifiant la
relation :
                                          1 1      1
                                            + = .
                                          p q      r
On suppose que f ∈ Lp (Ω) et g ∈ Lq (Ω).
  1. Exposants conjugués :
     On pose α = pr et β = qr . Partons de la relation donnée :

                                                        1 1 1
                                                         + = .
                                                        p q r

     En multipliant cette égalité par r (qui est non nul), on obtient :
                                          r r       1  1
                                           + = 1 ⇐⇒   + = 1.
                                          p q       α β

     ⇒ Les réels α et β sont strictement supérieurs à 1 (car r < p et r < q) et vérifient la
     relation de conjugaison. Ce sont des exposants conjugués.
  2. Démonstration de l’inégalité :
     Nous cherchons à majorer la norme ∥f g∥r . Par définition :
                                      Z                     Z
                                  r                 r
                             ∥f g∥r =   |f (x)g(x)| dµ =       |f |r · |g|r dµ.
                                            Ω                          Ω

     Posons les fonctions auxiliaires F = |f |r et G = |g|r .
       — Vérification des hypothèses :
           — Hypothèse : f ∈ Lp (Ω). Calculons la norme α de F :
                            Z            Z               Z
                                  α             r p/r
                              |F | dµ = (|f | ) dµ =        |f |p dµ = ∥f ∥pp < +∞.
                                 Ω                  Ω                   Ω

                                                                     p/α
             Donc F ∈ Lα (Ω) et ∥F ∥α = (∥f ∥pp )1/α = ∥f ∥p = ∥f ∥rp .
           — Hypothèse : g ∈ Lq (Ω). De même, calculons la norme β de G :
                            Z            Z                  Z
                               |G|β dµ = (|g|r )q/r dµ =      |g|q dµ = ∥g∥qq < +∞.
                                 Ω                  Ω                   Ω

               Donc G ∈ Lβ (Ω) et ∥G∥β = ∥g∥rq .
       — Application du théorème : Puisque F ∈ Lα et G ∈ Lβ avec α, β conjugués, nous pouvons
         appliquer l’Inégalité de Hölder classique :
                                       Z
                                          |F G| dµ ≤ ∥F ∥α ∥G∥β .
                                                Ω

          En remplaçant par les expressions en fonction de f et g :
                                         Z
                                            |f |r |g|r dµ ≤ ∥f ∥rp · ∥g∥rq .
                                                Ω

          Soit :
                                                    ∥f g∥rr ≤ (∥f ∥p ∥g∥q )r .


                                                         14
~~~

## Page 15

~~~text
  La fonction x 7→ x1/r étant croissante sur R+ , on prend la racine r-ième de l’inégalité : ⇒
  ∥f g∥r ≤ ∥f ∥p ∥g∥q .
3. Intégrabilité :
    — La fonction f g est mesurable comme produit de fonctions mesurables.
    — D’après l’inégalité démontrée à la question 2 :

                                          ∥f g∥r ≤ ∥f ∥p × ∥g∥q .
                                                   | {z } |{z}
                                                     <∞    <∞

       Le majorant est fini car f ∈ Lp et g ∈ Lq .
  ⇒ On a donc ∥f g∥r < +∞, ce qui signifie que f g ∈ Lr (Ω).




                                              15
~~~

## Page 16

~~~text
Corrigé de l’Exercice 9 : Inclusions et produits dans les espaces Lp
 1. Étude du produit f ∈ L1 et g ∈ L∞
     — Mesurabilité : Les fonctions f et g sont mesurables sur (Ω, F). Le produit de deux fonctions
       mesurables est mesurable. Donc f g est mesurable.
     — Majoration (Inégalité de Hölder cas limite) : Par définition de l’espace L∞ , il existe
       une constante C = ∥g∥∞ telle que :
                                          |g(x)| ≤ ∥g∥∞          µ-presque partout.
         En multipliant cette inégalité par |f (x)| (qui est positif), on obtient :
                                           |f (x)g(x)| ≤ ∥g∥∞ |f (x)| µ-p.p.

     — Intégrabilité : Intégrons cette inégalité sur Ω (possible par positivité et mesurabilité) :
                             Z             Z                      Z
                                |f g| dµ ≤    ∥g∥∞ |f | dµ = ∥g∥∞    |f | dµ.
                                  Ω                   Ω                           Ω

         Hypothèse : Comme f ∈ L1 , on a ∥f ∥1 < ∞. De plus ∥g∥∞ < ∞. Le membre de droite
         est donc fini.
    ⇒ La fonction f g est intégrable (i.e., f g ∈ L1 ) et ∥f g∥1 ≤ ∥f ∥1 ∥g∥∞ .
 2. Inclusions des espaces Lp (Mesure finie)
    Hypothèse fondamentale : On suppose que µ(Ω) < +∞. Soient 1 ≤ p1 ≤ p2 ≤ +∞.

    A. Inclusion L∞ ⊂ Lp2 Soit f ∈ L∞ (Ω).
     — On a |f (x)| ≤ ∥f ∥∞ µ-p.p.
     — En élevant à la puissance p2 (fonction croissante sur R+ ) :
                                                 |f (x)|p2 ≤ ∥f ∥p∞2     µ-p.p.

     — En intégrant sur Ω :
                                  Z                   Z
                                            p2
                                          |f | dµ ≤           ∥f ∥p∞2 dµ = ∥f ∥p∞2 × µ(Ω).
                                      Ω                   Ω

       Comme µ(Ω) < ∞, l’intégrale est finie.
    ⇒ Donc f ∈ Lp2 , ce qui prouve L∞ ⊂ Lp2 .

    B. Inclusion Lp2 ⊂ Lp1 Soit f ∈ Lp2 (Ω). Nous voulons montrer que Ω |f |p1 < ∞.
                                                                            R

    Méthode : Découpage de l’espace (plus rigoureux que la majoration +1). Considérons les ensembles
    A = {x : |f (x)| ≤ 1} et B = {x : |f (x)| > 1}.
                                 Z              Z             Z
                                        p1              p1
                                    |f | dµ =       |f | dµ +   |f |p1 dµ.
                                   Ω                      A               B
     — Sur A : On a |f | ≤ 1. Comme p1 ≥ 1, on a |f |p1 ≤ 1.
                               Z           Z
                                     p1
                                 |f | dµ ≤   1 dµ = µ(A) ≤ µ(Ω) < ∞.
                                   A                      A

     — Sur B : On a |f | > 1. Comme p1 ≤ p2 , la fonction t 7→ tp1 croît moins vite que tp2 pour
       t > 1. On a donc |f |p1 ≤ |f |p2 .
                          Z               Z             Z
                              |f |p1 dµ ≤   |f |p2 dµ ≤   |f |p2 dµ = ∥f ∥pp22 < ∞.
                              B                   B                  Ω

    La somme de deux quantités finies est finie. ⇒ Donc f ∈ Lp1 , ce qui prouve Lp2 ⊂ Lp1 .

                                                          16
~~~

## Page 17

~~~text
C. Inclusion Lp1 ⊂ L1 C’est un cas particulier du point précédent avec l’exposant 1 à la place
de p1 et p1 à la place de p2 (puisque 1 ≤ p1 ). ⇒ Donc Lp1 ⊂ L1 .

Synthèse : En chainant les résultats, on obtient la chaîne d’inclusions pour une mesure finie :

                                    L∞ ⊂ Lp2 ⊂ Lp1 ⊂ L1




                                            17
~~~
