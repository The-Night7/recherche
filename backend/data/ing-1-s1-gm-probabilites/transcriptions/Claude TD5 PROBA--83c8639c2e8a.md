# Claude TD5 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1RhJTuP4gpsDxu51t_c9Qp9QTLHOIUafo) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                      CYTech 2025-2026
                                    ING1 - GM : Probabilités

                                 TD 5 - Convergences




Exercice 1 Soit (Xn )n∈N∗ une suite de v.a.r. On suppose que chaque Xn ∼ Exp(nλ), avec λ > 0.
Montrer que la suite (Xn )n∈N∗ converge en probabilité vers 0.

Correction :
   Rappel : Si X ∼ Exp(µ), alors E[X] = µ1 et Var(X) = µ12 .
   Donc pour Xn ∼ Exp(nλ) :
                                             1                    1
                                E[Xn ] =       ,   Var(Xn ) =
                                            nλ                  (nλ)2

   Méthode 1 : Inégalité de Bienaymé-Tchebychev
   Pour tout ε > 0 :
                                                         Var(Xn )
                                   P (|Xn − 0| ≥ ε)≤
                                                            ε2
                                                            1
                                                       =
                                                         (nλ)2 ε2
                                                       n→∞
                                                       −−−→ 0

   Donc Xn −
           → 0.
              P

   Méthode 2 : Convergence en L
                                        2

   On peut aussi montrer que E[Xn2 ] → 0 :

                                E[Xn2 ]= Var(Xn ) + E[Xn ]2
                                           1        1        2
                                       =      2
                                                +      2
                                                         =
                                         (nλ)     (nλ)     (nλ)2
                                       n→∞
                                       −−−→ 0

              L2
   Donc Xn −→ 0, ce qui implique Xn −
                                    → 0.
                                            P




Exercice 2   Soit (Un )n∈N∗ une suite de v.a.r. i.i.d., de loi U ([0, 1]). Soient 0 ≤ a < b ≤ 1. On
pose, pour tout n ∈ N∗ , Xn = 1[a,b] (Un ).
  1. Déterminer la loi des variables Xn pour tout n ∈ N∗ .
  2. Montrer que X1 +X2n+···+Xn n∈N∗ converge vers b − a p.s.
                                 


Correction :
   1. Loi de Xn :
   Xn = 1[a,b] (Un ) est une variable de Bernoulli :

                               P (Xn = 1)= P (Un ∈ [a, b]) = b − a
                               P (Xn = 0)= 1 − (b − a)

   Donc Xn ∼ Bernoulli(b − a).

                                                   1
~~~

## Page 2

~~~text
   2. Convergence p.s. :
   Les (Xn ) sont i.i.d. avec E[Xn ] = b − a et Var(Xn ) = (b − a)(1 − (b − a)) < ∞.
   Par la Loi Forte des Grands Nombres :
                                     n
                                  1X     p.s.
                                     Xi −−→ E[X1 ] = b − a
                                  n
                                    i=1




Exercice 3 Pour tout n ∈ N∗ , Yn ∼ Geom(a/n), où a > 0. On pose Xn = Yn /n pour tout
n ∈ N . Montrer que (Xn )n∈N∗ converge en loi vers une variable aléatoire X qui suit une loi
     ∗

exponentielle de paramètre a.

Correction :
   Rappel : Si Y ∼ Geom(p) avec p = a/n :
                                                     a    a k
                        P (Y = k) = p(1 − p)k =         1−      ,     k∈N
                                                     n     n
   Fonction de répartition de Xn :
   Pour x ≥ 0 :
                                                                     
                                                              Yn
                             FXn (x)= P (Xn ≤ x) = P             ≤x
                                                              n
                                     = P (Yn ≤ nx)
                                         ⌊nx⌋
                                          Xa          a k
                                     =          1−
                                        n              n
                                          k=0
                                                   a ⌊nx⌋+1
                                     =1− 1−
                                                    n
   Passage à la limite :
   Quand n → ∞, ⌊nx⌋ ∼ nx, donc :
                                                       a nx
                              lim FXn (x)= lim 1 − 1 −
                                                    h na n ix
                             n→∞           n→∞

                                         = 1 − lim    1−
                                               n→∞       n
                                         = 1 − e−ax

   C'est la fonction de répartition de la loi exponentielle Exp(a).
              L
   Donc Xn −  → X où X ∼ Exp(a).


Exercice 4 Soit
            P (Xn )n∈N une suite de v.a.r. i.i.d. suivant une loi de Poisson de paramètre 1.
                       ∗

On note Sn = nk=1 Xk .
  1. Soit Yn = S√n −n
                   n
                       . Montrer que (Yn )n∈N∗ converge en loi vers une variable aléatoire dont on
     précisera la loi.
  2. Montrer que Sn suit une loi de Poisson, dont on déterminera le paramètre.
  3. En déduire que la suite de terme général un = e−n nk=0 nk! converge vers 1/2, lorsque
                                                             P       k


     n → +∞.



                                                2
~~~

## Page 3

~~~text
Correction :
   1. Convergence de Yn :
   Les (Xk ) sont i.i.d. avec Xk ∼ Poisson(1), donc :
                                   E[Xk ] = 1,          Var(Xk ) = 1
   Par le Théorème Central Limite :
                               Sn − nE[X1 ]  Sn − n L
                                            = √     −
                                                    → N (0, 1)
                                 nVar(X1 )
                               p
                                                n

             L
           → N (0, 1).
   Donc Yn −
   2. Loi de Sn :
   La somme de Poisson indépendantes est encore    une Poisson
                                                             P:
   Si Xi ∼ Poisson (λi ) indépendantes, alors   Xi ∼ Poisson( λi ).
                                              P
   Ici, Sn = nk=1 Xk avec Xk ∼ Poisson(1) :
            P

                                          Sn ∼ Poisson(n)

   3. Convergence de un :
   On a Sn ∼ Poisson(n), donc :
                                                            n
                                                            X nk
                                    P (Sn ≤ n) = e−n
                                                                  k!
                                                            k=0

   D'autre part, par la question 1 :
                                                         
                                                Sn − n
                          P (Sn ≤ n) = P         √     ≤ 0 = P (Yn ≤ 0)
                                                   n
                 L
   Comme Yn −
            → N (0, 1) :
                                                                         1
                                lim P (Yn ≤ 0) = P (Z ≤ 0) =
                                n→∞                                      2
où Z ∼ N (0, 1).
   Donc :                                         n
                                             −n
                                                  X nk n→∞ 1
                                    un = e             −−−→
                                                    k!      2
                                                  k=0




             Soit (an )n≥1 une suite de réels positifs tel que +∞
                                                               n=1 an = 2. Soit (Xn )n≥1 une suite
                                                                   P
Exercice 5
de v.a.r. indépendantes de lois exponentielles E(an ). On pose pour tout n ≥ 1 :
                                       Yn = min{X1 , . . . , Xn }

   Montrer que la suite de v.a.r. (Yn )n≥1 converge en loi vers une v.a.r. Y de loi E(2).

Correction :
   Propriété du minimum d'exponentielles indépendantes :
   Si Xi ∼ Exp(ai ) indépendantes, alors :
                                                                  n
                                                                             !
                               min{X1 , . . . , Xn } ∼ Exp
                                                                  X
                                                                        ai
                                                                  i=1


                                                    3
~~~

## Page 4

~~~text
   Démonstration :     Pour y ≥ 0 :
                             P (Yn > y)= P (min{X1 , . . . , Xn } > y)
                                         = P (X1 > y, . . . , Xn > y)
                                           Yn
                                         =    P (Xi > y)
                                              i=1
                                              n
                                              Y                    Pn
                                         =          e−ai y = e−y    i=1 ai

                                              i=1

   Donc Yn ∼ Exp ( ni=1 ai ).
                  P
   Convergence :
   Comme       n=1 an = 2, on a :
             P+∞
                                           n
                                                      n→∞
                                           X
                                                  ai −−−→ 2
                                           i=1
   Pour la fonction de répartition de Yn :
                                                            Pn
                                      FYn (y)= 1 − e−y        i=1 ai

                                                  n→∞
                                               −−−→ 1 − e−2y

   C'est la fonction de répartition de Exp(2).
             L
   Donc Yn − → Y où Y ∼ Exp(2).


Exercice 6   On travaille dans l'espace probabilisé (Ω, B(Ω), P ) où Ω = [0, 1], B(Ω) est la tribu
borélienne et P est la probabilité uniforme sur le segment [0, 1], i.e. :
                                              Z
                                    P (D) =         dx,   ∀D ∈ B(Ω)
                                               D

   Pour tout n ≥ 1, on dénit :
                          Xn : [0, 1] → R,        ω 7→ Xn (ω) = min(nω, 1)

  Montrer que la suite de v.a.r. (Xn )n≥1 converge presque sûrement vers la variable certaine
X = 1.

Correction :
   Convergence ponctuelle :
   Fixons ω ∈ [0, 1].
   Cas 1 : Si ω > 0, alors pour n > ω1 :
                                nω > 1 ⇒ Xn (ω) = min(nω, 1) = 1

   Donc limn→∞ Xn (ω) = 1.
   Cas 2 : Si ω = 0, alors :


                                Xn (0) = min(0, 1) = 0 pour tout n

   Donc limn→∞ Xn (0) = 0 ̸= 1.
   Convergence p.s. :
   L'ensemble où la convergence échoue est {0}.
   Or P ({0}) = 0 (la mesure de Lebesgue d'un singleton est nulle).

                                                      4
~~~

## Page 5

~~~text
   Donc :
                                                      p.s.
                                                   Xn −−→ 1



Exercice 7   Soit (Xn )n∈N∗ une suite de variables aléatoires réelles de lois :
                                                                      1                            1
            ∀n ∈ N∗ :      Xn (Ω) = {0, n2 },      P (Xn = 0) = 1 −     ,       P (Xn = n2 ) =
                                                                      n                            n
  1. Montrer que la suite (Xn )n∈N∗ converge en probabilité vers 0.
  2. Montrer que la suite (Xn )n∈N∗ ne converge pas en moyenne (dans L1 ) vers 0.
  3. (Xn )n∈N∗ converge-t-elle dans L2 vers 0 ?

Correction :
   1. Convergence en probabilité :
   Pour tout ε > 0 :

                                 P (|Xn − 0| ≥ ε)= P (Xn ≥ ε)
                                                                            1
                                                     = P (Xn = n2 ) =
                                                                            n
                                                      n→∞
                                                     −−−→ 0

   Donc Xn −
           → 0.
              P

   2. Non-convergence dans L
                                      1 :

   Calculons E[|Xn − 0|] = E[Xn ] :
                                                     
                                                    1          1
                                    E[Xn ]= 0 · 1 −     + n2 ·
                                                    n          n
                                          =n
                                             n→∞
                                             −−−→ +∞

   Donc Xn ne converge PAS dans L1 vers 0.
   3. Non-convergence dans L
                                      2 :

   Calculons E[Xn2 ] :
                                                     
                                                    1              1
                                   E[Xn2 ]= 0 · 1 −     + (n2 )2 ·
                                                    n              n
                                            = n3
                                            n→∞
                                            −−−→ +∞

   Donc Xn ne converge PAS dans L2 vers 0.
   Remarque importante : Cet exercice montre que :


                         Convergence en probabilité ̸⇒ Convergence dans L1



Exercice 8   Soit (Yn )n∈N∗ une suite de variables aléatoires réelles de loi :
                                                                      1                        1
             ∀n ∈ N∗ :      Yn (Ω) = {0, n},       P (Yn = 0) = 1 −     ,       P (Yn = n) =
                                                                      n                        n

                                                      5
~~~

## Page 6

~~~text
  1. Calculer limn→+∞ E[Yn ] et limn→+∞ Var(Yn ). Que peut-on en déduire ?
  2. La suite (Yn )n∈N∗ converge-t-elle en moyenne quadratique vers Y = 0 ?
  3. Montrer que (Yn )n∈N∗ converge en probabilité vers Y = 0.
  4. On considère une suite (Xk )k∈N∗ de v.a.r. i.i.d. de mêmePloi que Y2 . Pour k assez grand,
     par quelle loi peut-on approcher la loi de la v.a.r. Z = k1 ki=1 Xi ?

Correction :
   1. Espérance et variance :
   Espérance :
                                                 
                                                1      1
                                E[Yn ]= 0 · 1 −     +n· =1
                                                n      n
                                      n→∞
                                      −−−→ 1
   Moment d'ordre 2 :
                                                   
                                                  1         1
                               E[Yn2 ]= 0 ·    1−     + n2 · = n
                                                  n         n
   Variance :
                               Var(Yn )= E[Yn2 ] − E[Yn ]2 = n − 1
                                        n→∞
                                       −−−→ +∞
   Déduction :     Bien que l'espérance soit constante, la variance diverge, donc la distribution
s'étale de plus en plus.
   2. Convergence dans L
                              2 :

   Pour la convergence dans L2 vers 0, il faut E[Yn2 ] → 0.
                  n→∞
   Or E[Yn2 ] = n −−−→ +∞.
   Donc Yn ne converge PAS dans L2 vers 0.
   3. Convergence en probabilité :
   Pour tout ε > 0 :
                               P (|Yn − 0| ≥ ε)= P (Yn ≥ ε)
                                                                  1
                                                 = P (Yn = n) =
                                                                  n
                                                 n→∞
                                                 −−−→ 0

   Donc Yn −
           → 0.
             P

   4. Approximation de Z :
   Y2 a pour loi : P (Y2 = 0) = 1/2, P (Y2 = 2) = 1/2.
   Donc E[Y2 ] = 1 et Var(Y2 ) = E[Y22 ] − E[Y2 ]2 = 2 − 1 = 1.
   Pour (Xi ) i.i.d. de loi Y2 :
                                                   k
                                              1X
                                          Z=         Xi
                                              k
                                                  i=1

   Par la Loi des Grands Nombres : Z −
                                     → E[X1 ] = 1.
                                         P

   Par le Théorème Central Limite :
                          Z − E[X1 ]   Z −1 √           L
                                      =p     = k(Z − 1) −
                                                        → N (0, 1)
                           Var(X1 )/k
                         p
                                         1/k
   Donc pour k grand :                             
                                                  1
                                         Z ≈ N 1,
                                                  k

                                                  6
~~~
