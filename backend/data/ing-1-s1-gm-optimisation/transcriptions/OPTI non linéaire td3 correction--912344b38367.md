# OPTI non linéaire td3 correction.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1RIoqP73CTAEz6ip6fw-_dpsY8VQ9RtZK) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
       Correction Complète TD3
       Optimisation avec contraintes d’égalité et d’inégalité


                  CY Tech - 1ère année Ingénieurs
                         Année 2024-2025


Table des matières




                                 1
~~~

## Page 2

~~~text
Optimisation Non Linéaire - TD3                             Génie Mathématique - ING1


1     Exercice 1 : Géométrie différentielle et optimisa-
      tion

       Rappel de Cours
    Plan tangent à une surface :
       Pour une surface S définie par F (x, y, z) = 0, le plan tangent en un point
    P0 = (x0 , y0 , z0 ) est donné par :

                                   ∇F (P0 ) · (P − P0 ) = 0

       Pour une courbe paramétrée γ(t) passant par P0 (avec γ(t0 ) = P0 ), le vecteur
    tangent est γ ′ (t0 ).
       Le plan tangent est engendré par tous les vecteurs tangents aux courbes passant
    par P0 .


    Données :
    — S = {(x, y, z) ∈ R3 : x2 + y 2 + z 2 = 1} (sphère unité)
    — H = {(x, y, z) ∈ R3 : x2 + y 2 + z 2 = 1 et x + y = 0} (grand cercle)
    — γ1 (t) = (sin(t), 0, cos(t)) pour t ∈ (− π2 , π2 )
    — γ2 (t) = (0, sin(t), cos(t)) pour t ∈ (− π2 , π2 )
    — N = (0, 0, 1) (pôle Nord)

Question 1 : Représentations graphiques
    Les courbes γ1 et γ2 sont deux demi-grands cercles sur la sphère :
    — γ1 : méridien dans le plan (x, z) (avec y = 0)
    — γ2 : méridien dans le plan (y, z) (avec x = 0)
    Les deux courbes passent par le point N = (0, 0, 1) (obtenu pour t = 0).

Question 2 : Plan tangent à S au point N
Méthode 1 : Par les courbes paramétrées Calculons les vecteurs tangents :

                     γ1′ (t) = (cos(t), 0, − sin(t)) =⇒ γ1′ (0) = (1, 0, 0)

                     γ2′ (t) = (0, cos(t), − sin(t)) =⇒ γ2′ (0) = (0, 1, 0)
    Les deux vecteurs tangents sont (1, 0, 0) et (0, 1, 0). Ils sont linéairement indépendants
et orthogonaux.
    Le plan tangent en N est engendré par ces deux vecteurs :

                  TN (S) = Vect{(1, 0, 0), (0, 1, 0)} = {(x, y, 0) : x, y ∈ R}

    C’est le plan horizontal z = 1 (décalé au point N ), ou en coordonnées relatives : z = 0.




                                               2
~~~

## Page 3

~~~text
Optimisation Non Linéaire - TD3                               Génie Mathématique - ING1


Méthode 2 : Par l’équation cartésienne Posons F (x, y, z) = x2 + y 2 + z 2 − 1. Alors :

                    ∇F (x, y, z) = (2x, 2y, 2z) =⇒ ∇F (N ) = (0, 0, 2)

   L’équation du plan tangent en N = (0, 0, 1) est :
                                  
                             x−0
                 ∇F (N ) · y − 0 = 0 ⇐⇒ 2(z − 1) = 0 ⇐⇒ z = 1
                                

                             z−1

   Ou en coordonnées relatives à N : z = 0 (plan horizontal).

Question 3 : Représentation de H
   H est l’intersection de la sphère S et du plan x + y = 0 (soit y = −x).
   C’est un grand cercle de la sphère. En substituant y = −x dans l’équation de la
sphère :
                         x2 + (−x)2 + z 2 = 1 ⇐⇒ 2x2 + z 2 = 1
   C’est une ellipse de demi-axes √12 (en x) et 1 (en z), située dans le plan y = −x.


Question 4 : Espace tangent à H au point N
Méthode 1 : Par une courbe paramétrée Cherchons une courbe dans H passant
par N .
   Paramétrisation de H : avec y = −x et 2x2 + z 2 = 1, posons x = √12 sin(t), z = cos(t) :
                                                                     !
                                   1            1
                         γ(t) =    √ sin(t), − √ sin(t), cos(t)
                                    2            2

   Pour t = 0 : γ(0) = (0, 0, 1) = N
   Vecteur tangent :
                                                                       !
                         ′        1           1
                        γ (t) =   √ cos(t), − √ cos(t), − sin(t)
                                   2           2
                                                             !
                                               1   1
                                  γ ′ (0) =   √ , −√ , 0
                                                2   2
   L’espace tangent à H en N est la droite engendrée par ce vecteur :
                                  (                   !)
                                        1   1
                  TN (H) = Vect        √ , −√ , 0          = Vect{(1, −1, 0)}
                                         2   2

Méthode 2 : Par les équations cartésiennes H est définie par deux contraintes :

                             h1 (x, y, z) = x2 + y 2 + z 2 − 1 = 0
                             h2 (x, y, z) = x + y = 0

   Gradients :
                        ∇h1 (N ) = (0, 0, 2),       ∇h2 (N ) = (1, 1, 0)

                                                3
~~~

## Page 4

~~~text
Optimisation Non Linéaire - TD3                                 Génie Mathématique - ING1


   L’espace tangent est le noyau de la matrice Jacobienne :
                                                            !
                                               0 0 2
                                      ∇h(N ) =
                                               1 1 0

   On cherche v = (v1 , v2 , v3 ) tel que :
                                                     
                             2v
                                   3 = 0                   3 = 0
                                                      v
                                                ⇐⇒
                             v1 + v2 = 0             v2 = −v1


   Donc : v = v1 (1, −1, 0).

                                   TN (H) = Vect{(1, −1, 0)}


Question 5 : Optima de h(x, y, z) = z sur H

      Méthode
  On minimise/maximise z sous les contraintes x2 + y 2 + z 2 = 1 et x + y = 0.


Lagrangien :

                  L(x, y, z, λ1 , λ2 ) = z + λ1 (x2 + y 2 + z 2 − 1) + λ2 (x + y)

Conditions de stationnarité :
                                      ∂L
                                         = 2λ1 x + λ2 = 0                             (1)
                                      ∂x
                                      ∂L
                                         = 2λ1 y + λ2 = 0                             (2)
                                      ∂y
                                      ∂L
                                         = 1 + 2λ1 z = 0                              (3)
                                      ∂z
   De (1) et (2) : 2λ1 x = 2λ1 y =⇒ x = y (si λ1 ̸= 0).
   Mais la contrainte impose x + y = 0, donc x = y =⇒ 2x = 0 =⇒ x = 0.
   Donc : x = y = 0.
   De la contrainte sphérique : 0 + 0 + z 2 = 1 =⇒ z = ±1.
                    1
   De (3) : λ1 = − 2z .
   Points critiques :
   — (0, 0, 1) : z = 1 (maximum)
   — (0, 0, −1) : z = −1 (minimum)

      Résultat

                                Maximum : (0, 0, 1) avec h = 1

                               Minimum : (0, 0, −1) avec h = −1



                                                4
~~~

## Page 5

~~~text
Optimisation Non Linéaire - TD3                            Génie Mathématique - ING1


Question 6 : Optima de g(x, y, z) = z 2 sur S
Lagrangien :
                          L(x, y, z, λ) = z 2 + λ(x2 + y 2 + z 2 − 1)

Conditions :
                                    ∂L
                                       = 2λx = 0
                                    ∂x
                                    ∂L
                                       = 2λy = 0
                                    ∂y
                                    ∂L
                                       = 2z + 2λz = 0
                                    ∂z
   Cas 1 : λ = 0 =⇒ de la 3ème équation : z = 0.
   De la contrainte : x2 + y 2 = 1.
   Points : cercle équatorial {(x, y, 0) : x2 + y 2 = 1} avec g = 0.
   Cas 2 : λ ̸= 0 =⇒ x = y = 0 et 2z(1 + λ) = 0.
   Si z ̸= 0 : λ = −1 et z 2 = 1 =⇒ z = ±1.
   Points : (0, 0, 1) et (0, 0, −1) avec g = 1.

      Résultat

                   Minimum : cercle équatorial (x, y, 0) avec gmin = 0

                        Maximum : pôles (0, 0, ±1) avec gmax = 1




                                              5
~~~

## Page 6

~~~text
Optimisation Non Linéaire - TD3                            Génie Mathématique - ING1


2     Exercice 2 : Projection sur un hyperplan
   Énoncé : Calculer la distance d’un point x0 ∈ Rn au plan défini par Ax = b, où
A ∈ Mp×n (R) et Rang(A) = p.

       Méthode
    On minimise la distance au carré : min 12 ∥x − x0 ∥2 sous Ax = b.


Lagrangien :
                                1
                       L(x, λ) = (x − x0 )T (x − x0 ) + λT (Ax − b)
                                2

Condition de stationnarité :

                      ∇x L = x − x0 + AT λ = 0 =⇒ x = x0 − AT λ

Injection dans la contrainte :

                  Ax = b =⇒ A(x0 − AT λ) = b =⇒ Ax0 − AAT λ = b

    Comme Rang(A) = p, la matrice AAT ∈ Mp×p (R) est inversible :

                                    λ = (AAT )−1 (Ax0 − b)

Projection orthogonale :

                             x∗ = x0 − AT (AAT )−1 (Ax0 − b)

Distance au plan :

                    d(x0 , Plan) = ∥x∗ − x0 ∥ = AT (AAT )−1 (Ax0 − b)
                                    q
                                =       (Ax0 − b)T (AAT )−1 (Ax0 − b)


3     Exercice 3 : Condition nécessaire du second ordre
    Théorème : Voir Exercice 3 de la correction TD3-bis (identique).
    La démonstration repose sur :
    1. L’unicité de λ découle de la régularité du point (indépendance linéaire des gra-
       dients).
    2. La positivité de la forme quadratique provient de l’analyse des variations secondes
       le long des courbes admissibles.




                                               6
~~~

## Page 7

~~~text
Optimisation Non Linéaire - TD3                             Génie Mathématique - ING1


4     Exercice 4 : Méthodes de substitution et Lagrange
Problème (P1)
    Énoncé :
           
           
           
           
           
             Optimiser
                  
                       f (x1 , x2 , x3 , x4 ) = 2x1 − 2x21 − 5x22 − x23 + 4x3 + 4x4
                  x − 2x = 2
                    4      2
           
            sous
           
                 x3 − x1 = 1


    Solution : Voir correction TD3-bis (identique).

                                  2 4 5 18
                                                  
                                  ∗
                              x =  , , ,               (maximum)
                                  3 5 3 5

Problème (P2) - renommé (P1) dans l’énoncé
    Énoncé :
        
        Optimiser
        
        
              
                    f (x1 , x2 , x3 , x4 ) = −x21 − x22 − x23 + 4x1 + 6x2 + 4x3 + 2x4
               x − 2x = 0
                  4     2
        
         sous
        
               x3 − x1 = 1


    Solution : Voir correction TD3-bis.

                                 3     5                         65
                                              
                              ∗
                             x =   , 5, , 10       avec fmax =
                                 2     2                          2




                                               7
~~~

## Page 8

~~~text
Optimisation Non Linéaire - TD3                              Génie Mathématique - ING1


5     Exercice 5 : Optimisation avec contraintes d’inéga-
      lité
    Énoncé :       
                   Minimiser
                   
                   
                        
                               f (x1 , x2 , x3 ) = x21 − x22 + x23 − 2x1 x2
                         g (x) = x2 + x2 + x2 − 1 ≤ 0
                           1           1      2     3
                   sous
                   
                   
                        g2 (x) = x1 + x2 − 1 ≤ 0


Question 1 : Lagrangien


        L(x, µ) = x21 − x22 + x23 − 2x1 x2 + µ1 (x21 + x22 + x23 − 1) + µ2 (x1 + x2 − 1)


Question 2 : Points réguliers
Point P1 = (0, 0, 0) Vérification de l’admissibilité :

                       g1 (P1 ) = 0 + 0 + 0 − 1 = −1 < 0 (inactive)
                       g2 (P1 ) = 0 + 0 − 1 = −1 < 0 (inactive)

    Aucune contrainte active =⇒ P1 est régulier.
    Le plan tangent est tout R3 (aucune restriction).

Point P2 = (0, 1, 0) Vérification :

                           g1 (P2 ) = 0 + 1 + 0 − 1 = 0 (active)
                           g2 (P2 ) = 0 + 1 − 1 = 0 (active)

    Gradients :
                    ∇g1 (x) = (2x1 , 2x2 , 2x3 ) =⇒ ∇g1 (P2 ) = (0, 2, 0)
                        ∇g2 (x) = (1, 1, 0) =⇒ ∇g2 (P2 ) = (1, 1, 0)
    Ces deux vecteurs sont linéairement indépendants =⇒ P2 est régulier.
    Plan tangent : T (P2 ) = {v : ∇g1 (P2 ) · v ≤ 0 et ∇g2 (P2 ) · v ≤ 0}

        T (P2 ) = {(v1 , v2 , v3 ) : 2v2 ≤ 0 et v1 + v2 ≤ 0} = {v : v2 ≤ 0 et v1 ≤ −v2 }


Question 3 : Conditions de KKT

       Rappel de Cours
    Conditions de Karush-Kuhn-Tucker :
       1. Stationnarité : ∇f (x) +        i µi ∇gi (x) = 0
                                       P

       2. Admissibilité primale : gi (x) ≤ 0 pour tout i
       3. Admissibilité duale : µi ≥ 0 pour tout i


                                               8
~~~

## Page 9

~~~text
Optimisation Non Linéaire - TD3                           Génie Mathématique - ING1


       4. Écart complémentaire : µi gi (x) = 0 pour tout i


   Pour notre problème :
                          ∇f (x) = (2x1 − 2x2 , −2x1 − 2x2 , 2x3 )
   Système KKT :
                               2x1 − 2x2 + 2µ1 x1 + µ2 = 0                                 (1)
                              −2x1 − 2x2 + 2µ1 x2 + µ2 = 0                                 (2)
                                           2x3 + 2µ1 x3 = 0                                (3)
                                 µ1 (x1 + x22 + x23 − 1) = 0
                                      2
                                                                                           (4)
                                       µ2 (x1 + x2 − 1) = 0                                (5)
                                           x21 + x22 + x23 ≤ 1                             (6)
                                                 x1 + x2 ≤ 1                               (7)
                                                   µ1 , µ2 ≥ 0                             (8)

Question 4 : Tous les points KKT

      Méthode
   On examine tous les cas selon les contraintes actives : (I,I), (I,A), (A,I), (A,A) où
   I=inactive, A=active.


Cas 1 : µ1 = 0, µ2 = 0 (aucune contrainte active) Système :
                              2x1 − 2x2 = 0 =⇒ x1 = x2
                             −2x1 − 2x2 = 0 =⇒ x1 = −x2
                                    2x3 = 0 =⇒ x3 = 0
   De x1 = x2 et x1 = −x2 : x1 = 0. Donc (0, 0, 0).
   Vérification des contraintes :
   — g1 = −1 < 0
   — g2 = −1 < 0
   Point candidat : (0, 0, 0)

Cas 2 : µ1 = 0, µ2 > 0 (seule g2 active) De (5) : x1 + x2 = 1.
  Système :
                             2x1 − 2x2 + µ2 = 0
                            −2x1 − 2x2 + µ2 = 0
                                        2x3 = 0 =⇒ x3 = 0
   Soustraction des deux premières : 4x1 = 0 =⇒ x1 = 0.
   Donc x2 = 1 et µ2 = −2x1 + 2x2 = 2 > 0
   Vérification g1 = 0 + 1 + 0 − 1 = 0 : la contrainte g1 est aussi active ! Contradiction
avec µ1 = 0.
   Ce cas ne donne pas de solution valide.

                                             9
~~~

## Page 10

~~~text
Optimisation Non Linéaire - TD3                            Génie Mathématique - ING1


Cas 3 : µ1 > 0, µ2 = 0 (seule g1 active) De (4) : x21 + x22 + x23 = 1.
  De (3) : 2x3 (1 + µ1 ) = 0 =⇒ x3 = 0 (car µ1 > 0).
  Donc x21 + x22 = 1.
  Système :

                                  2x1 (1 + µ1 ) − 2x2 = 0                        (a)
                                 −2x1 + 2x2 (1 − µ1 ) = 0                        (b)

   De (a) : x2 = x1 (1 + µ1 )
   De (b) : x1 = x2 (1 − µ1 )
   Substitution : x2 = x2 (1 − µ1 )(1 + µ1 ) = x2 (1 − µ21 )
   Si x2 ̸= 0 : 1 = 1 − µ21 =⇒ µ1 = 0. Contradiction.
   Donc x2 = 0 =⇒ x1 = 0. Mais alors x23 = 1, et de (7) : 0 ≤ 1
   Points : (0, 0, ±1).
   De (a) avec x2 = 0 : toujours vérifié.
   Calcul de µ1 : on utilise (a) ou (b) qui sont automatiquement vérifiées.
   En fait, pour x1 = x2 = 0, les équations (1) et (2) deviennent :

                                 µ2 = 0 (déjà supposé)
                                 µ2 = 0

   µ1 peut être quelconque > 0. Vérifions avec une valeur : prenons µ1 = 1.
   Points candidats : (0, 0, 1) et (0, 0, −1) avec µ1 > 0 arbitraire.

Cas 4 : µ1 > 0, µ2 > 0 (les deux contraintes actives)

                                     x21 + x22 + x23 = 1
                                           x1 + x2 = 1

   De (3) : x3 = 0 (car µ1 > 0).
   Donc : x21 + x22 = 1 et x1 + x2 = 1.
   De x2 = 1 − x1 : x21 + (1 − x1 )2 = 1

               2x21 − 2x1 + 1 = 1 =⇒ 2x21 − 2x1 = 0 =⇒ x1 (x1 − 1) = 0

   Solutions : x1 = 0 ou x1 = 1.
   — x1 = 0 =⇒ x2 = 1 : point (0, 1, 0)
   — x1 = 1 =⇒ x2 = 0 : point (1, 0, 0)
   Calculons les multiplicateurs pour (0, 1, 0) :
   De (1) : −2 + µ2 = 0 =⇒ µ2 = 2
   De (2) : −2 + 2µ1 + µ2 = 0 =⇒ µ1 = 2−µ     2
                                                2
                                                  =0
   Contradiction : µ1 > 0 requis. (0, 1, 0) ne satisfait pas KKT dans ce cas.
   Pour (1, 0, 0) :
   De (1) : 2 + 2µ1 + µ2 = 0 =⇒ µ2 = −2 − 2µ1 < 0
   Contradiction avec µ2 ≥ 0. (1, 0, 0) ne satisfait pas non plus.
   Conclusion du Cas 4 : Aucun point valide.




                                             10
~~~

## Page 11

~~~text
Optimisation Non Linéaire - TD3                          Génie Mathématique - ING1


Question 5 : Résolution du problème
   Points candidats KKT :
   — P1 = (0, 0, 0)
   — P2 = (0, 0, 1)
   — P3 = (0, 0, −1)
   Calculons f en ces points :

                                 f (P1 ) = 0
                                 f (P2 ) = 0 − 0 + 1 − 0 = 1
                                 f (P3 ) = 0 − 0 + 1 − 0 = 1


      Résultat

                       Minimum global : (0, 0, 0) avec fmin = 0


   Note : On peut vérifier la condition du second ordre pour confirmer.




                                             11
~~~

## Page 12

~~~text
Optimisation Non Linéaire - TD3                        Génie Mathématique - ING1


6     Exercice 6 : Application des conditions KKT
    Énoncé : Identique à l’Exercice 7 du TD3-bis.
    Solution complète : Voir correction TD3-bis, Exercice 7.

       Résultat
    Le point y = (−1, −1) satisfait les conditions KKT avec µ1 = 0, µ2 = 8.
       La condition suffisante du second ordre est vérifiée.

                        y = (−1, −1) est un minimum local strict




                                           12
~~~

## Page 13

~~~text
Optimisation Non Linéaire - TD3                             Génie Mathématique - ING1


A      Récapitulatif des formules essentielles
Géométrie différentielle
    — Surface implicite : S = {P : F (P ) = 0}
    — Plan tangent : ∇F (P0 ) · (P − P0 ) = 0
    — Courbe paramétrée : Vecteur tangent = γ ′ (t0 )
    — Intersection de surfaces : T (P0 ) = Ker(∇h(P0 ))

Optimisation avec égalités
    — Lagrangien : L(x, λ) = f (x) + λT h(x)
    — CN1 : ∇x L = 0 et h(x) = 0
    — Cône tangent : T (x∗ ) = {y : ∇h(x∗ )T y = 0}
    — CS2 : y T ∇2xx Ly > 0 pour tout y ∈ T (x∗ ), y ̸= 0

Optimisation avec inégalités (KKT)
    — Lagrangien : L(x, µ) = f (x) + i µi gi (x)
                                         P

    — Stationnarité : ∇f (x) + i µi ∇gi (x) = 0
                                 P

    — Admissibilité : gi (x) ≤ 0 et µi ≥ 0
    — Écart complémentaire : µi gi (x) = 0
    — Cône tangent : T (x∗ ) = {y : ∇gi (x∗ )T y ≤ 0 si gi (x∗ ) = 0}
    — CS2 : y T ∇2xx Ly > 0 pour tout y ∈ T (x∗ ), y ̸= 0


B      Méthodologie générale
    1. Identifier le type de problème : sans contraintes, égalités, inégalités
    2. Écrire le Lagrangien avec les bons multiplicateurs
    3. Cas avec inégalités : explorer tous les cas selon les contraintes actives
    4. Résoudre le système de conditions nécessaires
    5. Vérifier l’admissibilité de chaque candidat
    6. Comparer les valeurs pour identifier l’optimum global
    7. Vérifier CS2 si demandé (nature locale)




       Attention
    Pièges classiques :
       — Oublier de vérifier l’admissibilité (contraintes satisfaites)
       — Ne pas explorer tous les cas de contraintes actives/inactives
       — Confondre gradient et Hessienne
       — Oublier les conditions µi ≥ 0 et µi gi (x) = 0



                                             13
~~~
