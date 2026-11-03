# ALGEBRE TD2 correction.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14RX7RvoPV7wJDlnmbOus-RwTMwWHY1Ag) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Correction TD2 - Recherche des zéros d’une fonction
Exercice 8 : Méthode du point fixe
Énoncé : On cherche à résoudre l’équation du second degré x2 − 2x − 3 = 0 par une
méthode de point fixe.


Rappel de Cours : La méthode du point fixe
    Pour résoudre une équation f (x) = 0, on la transforme en une équation équivalente de
la forme x = g(x). Un nombre α tel que α = g(α) est appelé un point fixe de la fonction
g.
    L’algorithme du point fixe génère une suite (xn ) à partir d’une valeur initiale x0 par
la relation de récurrence :
                                      xn+1 = g(xn )
Théorème de convergence : Soit α un point fixe de g. Si la fonction g est continûment
dérivable et s’il existe un intervalle I = [α − δ, α + δ] tel que :
    1. Pour tout x ∈ I, g(x) ∈ I (stabilité de l’intervalle).
    2. Il existe une constante k < 1 telle que pour tout x ∈ I, |g ′ (x)| ≤ k.
Alors, pour tout x0 ∈ I, la suite (xn ) converge vers α.
    En pratique, si |g ′ (α)| < 1, le point fixe est dit attractif et la méthode convergera
si x0 est choisi suffisamment proche de α. Si |g ′ (α)| > 1, le point fixe est répulsif et la
méthode divergera.


Solution de l’Exercice 8
    1. Déterminer les solutions exactes.
       On résout l’équation x2 − 2x − 3 = 0. Le discriminant est ∆ = (−2)2 − 4(1)(−3) =
       4 + 12 = 16 = 42 . Les solutions (qui seront nos points fixes) sont :
                                               √
                                     −(−2) − 16         2−4
                                x1 =                =            = −1
                                          2(1)             2
                                                √
                                      −(−2) + 16         2+4
                                 x2 =                =           =3
                                           2(1)              2
       Les solutions exactes sont donc α1 = −1 et α2 = 3.
    2. Appliquer l’algorithme de point fixe.
       On part de x0 = 4 pour les trois fonctions g1 , g2 , g3 .
                         √
       — Pour g1 (x) = 2x + 3 :
                       x0 = 4
                                       p         √
                       x1 = g1 (4) =   2(4) + 3 = 11 ≈ 3.3166
                                          p               √
                       x2 = g1 (3.3166) = 2(3.3166) + 3 = 9.6332 ≈ 3.1037
                                          p               √
                       x3 = g1 (3.1037) = 2(3.1037) + 3 = 9.2074 ≈ 3.0344
                                          p               √
                       x4 = g1 (3.0344) = 2(3.0344) + 3 = 9.0688 ≈ 3.0114

                                             1
~~~

## Page 2

~~~text
                    3
   — Pour g2 (x) = x−2 :
                   x0 = 4
                                   3
                   x1 = g2 (4) =        = 1.5
                                 4−2
                                      3          3
                   x2 = g2 (1.5) =         =        = −6
                                   1.5 − 2     −0.5
                                      3         3
                   x3 = g2 (−6) =          =       = −0.375
                                   −6 − 2      −8
                                             3           3
                   x4 = g2 (−0.375) =               =        ≈ −1.2631
                                        −0.375 − 2    −2.375
                      2
   — Pour g3 (x) = x 2−3 :
                          x0 = 4
                                     42 − 3     13
                          x1 = g3 (4) =       =     = 6.5
                                        2        2
                                       6.52 − 3     42.25 − 3
                       x2 = g3 (6.5) =           =              = 19.625
                                            2           2
                                            19.6252 − 3
                       x3 = g3 (19.625) =               ≈ 191.57
                                                 2
3. Constat sur la convergence.
   — La suite générée par g1 (x) semble converger lentement vers la racine α2 = 3.
   — La suite générée par g2 (x) oscille et semble converger, beaucoup plus lentement,
      vers la racine α1 = −1.
   — La suite générée par g3 (x) diverge très rapidement vers +∞.
4. Explication des résultats.
   On étudie la dérivée de chaque fonction au voisinage des points fixes α1 = −1 et
   α2 = 3.
   — Pour g1 (x) = (2x + 3)1/2 , la dérivée est g1′ (x) = 21 (2x + 3)−1/2 × 2 = √2x+3
                                                                                  1
                                                                                      .
                           ′
      — En α1 = −1 : g1 (−1) = √          1           1
                                                 = 1 = 1. La convergence n’est pas
                                                     √
                                             2(−1)+3
                     ′
        garantie (|g (α)| doit être strict. inférieur à 1).
      — En α2 = 3 : g1′ (3) = √ 1      = √19 = 13 . Comme |g1′ (3)| = 1/3 < 1, le point
                                    2(3)+3
        fixe 3 est attractif. Cela explique la convergence observée.
                                                                         −3
   — Pour g2 (x) = 3(x − 2)−1 , la dérivée est g2′ (x) = −3(x − 2)−2 = (x−2)2.
                         ′           −3         −3      1        ′
     — En α1 = −1 : g2 (−1) = (−1−2)2 = 9 = − 3 . Comme |g2 (−1)| = 1/3 < 1, le
        point fixe -1 est attractif. Cela explique pourquoi la suite semble converger
        vers -1.
                                −3      −3
     — En α2 = 3 : g2′ (3) = (3−2)                           ′
                                   2 = 1 = −3. Comme |g2 (3)| = 3 > 1, le point fixe

        3 est répulsif. La méthode ne peut pas converger vers 3 pour g2 .
                     2
   — Pour g3 (x) = x 2−3 , la dérivée est g3′ (x) = 2x2
                                                        = x.
                         ′                          ′
     — En α1 = −1 : g3 (−1) = −1. Comme |g3 (−1)| = 1, la convergence n’est pas
        garantie.
     — En α2 = 3 : g3′ (3) = 3. Comme |g3′ (3)| = 3 > 1, le point fixe 3 est répulsif.
        Cela explique la divergence rapide observée à partir de x0 = 4, qui est proche
        de 3.




                                              2
~~~

## Page 3

~~~text
Exercice 9 : Points fixes attractifs
Énoncé : Soit λ ∈ R. On pose g(x) = λx(1 − x).


Rappel de Cours : Convergence quadratique
   L’ordre de convergence d’une méthode de point fixe est (au moins) quadratique si,
en plus des conditions de convergence, on a g′ (α) = 0 au point fixe α. Une convergence
quadratique est extrêmement rapide.


Solution de l’Exercice 9
   1. Déterminer les points fixes de g.
      Les points fixes α sont les solutions de l’équation g(x) = x.
                                         λx(1 − x) = x
                                        λx − λx2 − x = 0
                                       x(λ − 1 − λx) = 0
      On obtient deux solutions :
      — Soit x = 0. C’est le premier point fixe, α1 = 0.
      — Soit λ − 1 − λx = 0 =⇒ λx = λ − 1 =⇒ x = λ−1     λ
                                                           = 1 − λ1 (si λ ̸= 0). C’est le
                                     1
         second point fixe, α2 = 1 − λ .
   2. Déterminer les valeurs de λ pour un point fixe attractif.
      On calcule d’abord la dérivée de g(x) = λx − λx2 .
                                        g ′ (x) = λ − 2λx
      Un point fixe α est attractif si |g ′ (α)| < 1.
      — Pour le point fixe α1 = 0 : La condition est |g ′ (0)| < 1.
                                    |λ − 2λ(0)| < 1 =⇒ |λ| < 1
        Le point fixe 0 est attractif pour λ ∈] − 1, 1[.
      — Pour le point fixe α2 = 1 − λ1 : La condition est |g ′ (1 − λ1 )| < 1.
                                                     
                                                    1
                                       λ − 2λ 1 −        <1
                                                   λ
                                         |λ − 2(λ − 1)| < 1
                                          |λ − 2λ + 2| < 1
                                             |2 − λ| < 1
          Cette inégalité est équivalente à −1 < 2 − λ < 1.
                                       −1 − 2 < −λ < 1 − 2
                                           −3 < −λ < −1
          En multipliant par -1 (et en inversant les inégalités) :
                                             1<λ<3
          Le point fixe 1 − 1/λ est attractif pour λ ∈]1, 3[.

                                             3
~~~

## Page 4

~~~text
    3. Déterminer les valeurs de λ pour une convergence quadratique.
       La convergence est (au moins) quadratique si g ′ (α) = 0.
       — Pour le point fixe α1 = 0 : On cherche λ tel que g ′ (0) = 0.

                                       λ − 2λ(0) = 0 =⇒ λ = 0

         Pour λ = 0, la convergence vers 0 est quadratique (la fonction est g(x) = 0,
         donc on atteint 0 en une itération).
       — Pour le point fixe α2 = 1 − λ1 : On cherche λ tel que g ′ (1 − λ1 ) = 0.

                                         2 − λ = 0 =⇒ λ = 2

           Pour λ = 2, la convergence vers α2 = 1 − 1/2 = 1/2 est quadratique.

Exercice 10 : Vitesse de convergence de la méthode de Newton
                                                                √
Énoncé : On considère six fonctions ayant toutes α =                2 pour zéro. On étudie la
convergence de la méthode de Newton pour chacune.


Rappel de Cours : Méthode de Newton et Vitesse de Convergence
   La méthode de Newton est un algorithme itératif pour trouver une approximation
d’un zéro (ou racine) d’une fonction f . La suite (xn ) est définie par :

                                                   f (xn )
                                     xn+1 = xn −
                                                   f ′ (xn )

La vitesse de convergence de cette méthode dépend des propriétés de la fonction f au
voisinage de la racine α.
    — Convergence quadratique (ordre 2) : Si la racine α est simple, c’est-à-dire si
       f (α) = 0 et f ′ (α) ̸= 0, alors la convergence est quadratique. C’est le cas le plus
       courant et le plus souhaitable, car le nombre de chiffres significatifs corrects double
       à chaque itération.
    — Convergence linéaire (ordre 1) : Si la racine α est multiple, c’est-à-dire si
       f (α) = 0 et f ′ (α) = 0, la convergence est seulement linéaire et donc beaucoup plus
       lente. En pratique, si f ′ (xn ) est proche de zéro, l’algorithme peut devenir instable.
    — Convergence d’ordre supérieur : Si f ′ (α) ̸= 0 et que des dérivées d’ordre
       supérieur s’annulent (f ′′ (α) = 0, etc.), la convergence peut être encore plus rapide
       (cubique, etc.).


Solution de l’Exercice 10
                                        √
    1. Tableau des dérivées en x = 2.
       On calcule
              √ les dérivées première et seconde pour chaque fonction et on les évalue
       en α = 2.
       — f (x) = x2 − √
                      2 =⇒ √ f ′ (x) = 2x =⇒ f ′′ (x) = 2√
       — g(x) = x2 − √  3x + 6 − 2 =⇒    √ g ′ (x) = 2x − 3 =⇒ √
                                                               g ′′ (x) = 2
       — h(x) = x2 − 2 2x + 2 = (x − 2)2 =⇒ h′ (x) = 2(x − 2) =⇒ h′′ (x) = 2

                                              4
~~~

## Page 5

~~~text
                     √           √                          √
    — i(x) = (x − 2)4 + 12 (x − 2) =⇒ i′ (x) = 4(x − 2)3 + 21 =⇒ i′′ (x) =
             √
      12(x − 2)2 √                                   √             √
    — j(x) =√ 18 (e4(x− 2) − 1) =⇒ j ′ (x) = 84 e4(x− 2) = 12 e4(x− 2) =⇒ j ′′ (x) =
      2e4(x− 2)       √
    — k(x) = 12 (x − 2) =⇒ k ′ (x) = 12 =⇒ k ′′ (x) = 0


                                              f        g            h          i            j   k
                             √                √      √   √                     1            1   1
           Dérivée en x =        2           2 2    2 2− 3          0          2            2   2
                                     √
      Dérivée seconde en x =             2    2         2           2          0            2   0

2-5. Analyse du comportement des suites.                            √
     — Fonctions f et g : Les deux ont une dérivée non nulle en 2, donc la conver-
       gence est quadratique. Graphiquement, la méthode de Newton consiste à tracer
       la tangente à la courbe en xn et à trouver son intersection avec l’axe des abs-
       cisses pour obtenir xn+1√ .
                              ′
     — Fonction h : On a h ( 2) = 0. La racine est double. La méthode de Newton
       va donc converger très lentement (linéairement). De plus, si on s’approche de
       la racine, la tangente devient presque horizontale, et son intersection avec l’axe
       des abscisses est très éloignée, ce qui rend la méthode instable.
     — Fonctions i et j : Les deux ont une dérivée non nulle, la convergence est donc
       au moins quadratique.
     — Fonction k : La fonction k(x) est une droite. La méthode de Newton, qui
       approxime la fonction par sa tangente, est exacte pour une fonction linéaire.
       La racine est donc trouvée en une seule itération, quelle que soit la valeur
       de départ x0 .
 6. Classement de f et g selon la vitesse de convergence.
    Les deux convergent quadratiquement. La vitesse de convergence est liée à la
                  f ′′ (α)
    constante C = 2f ′ (α) . Plus C est petite, plus la convergence est rapide.

                           2√
    — Pour f : Cf =     2(2 2)
                                 = 2√1 2 ≈ 0.354.
                           2 √           1
    — Pour g : Cg = 2(2√2−     3)
                                  = 2.828−1.732 ≈ 0.912.
    Comme Cf < Cg , la suite générée par la fonction f converge plus vite que celle
    générée par la fonction g.
 7. Classement de i, j et k selon la vitesse de convergence.
    — k : Convergence
                   √      en 1 seule√ itération (la plus rapide).
                ′               ′′
    — i : On a i ( 2) ̸= 0 et i ( 2) = 0. La convergence est d’ordre supérieur à 2 (au
       moins cubique),
                    √ donc très √     rapide.
    — j : On a j ′ ( 2) ̸= 0 et j ′′ ( 2) ̸= 0. La convergence est quadratique.
    Le classement par vitesse de convergence décroissante est : k > i > j.
 8. Pourquoi les fonctions g, h, i, j, k ne sont   √ pas adaptées ?
    Le but est de calculer une approximation de 2. √
    — Les fonctions h, i, j, k contiennent explicitement
                                                √        2 dans leur définition. On ne
       peut donc pas les utiliser pour trouver 2, puisqu’il faudrait déjà connaître sa
       valeur pour évaluer la fonction.



                                             5
~~~

## Page 6

~~~text
                                             √     √
       — √ La fonction g contient les termes 3 et 6. Utiliser une méthode pour calculer
             2 qui requiert de connaître au préalable d’autres racines carrées n’est pas
           logique.
       La fonction f (x) = x2 − 2 est la plus naturelle et la plus simple pour ce problème,
       car elle ne dépend que d’opérations arithmétiques de base.




Exercice 11 : Profil d’aile d’avion NACA
                                                               √
Énoncé : Déterminer la valeur de x où l’épaisseur t(x) = T (3.7 x − 3.4x − 0.3x4 ) est
maximale, en utilisant la méthode de Newton.

Rappel de Cours : Optimisation par la méthode de Newton
   Pour trouver un extremum (maximum ou minimum) d’une fonction t(x), on cherche les
points où sa dérivée s’annule, c’est-à-dire les racines de t′ (x) = 0. On peut donc appliquer
la méthode de Newton à la fonction f (x) = t′ (x). La relation de récurrence devient :

                                                t′ (xn )
                                    xn+1 = xn − ′′
                                               t (xn )



Solution de l’Exercice 11
    1. Justification de l’approche.
       Trouver le x qui maximise t(x) revient à trouver le zéro de la dérivée t′ (x). Nous
       allons donc appliquer la méthode de Newton à la fonction f (x) = t′ (x).
    2. Calcul des dérivées.         √
       La fonction est t(x) = T (3.7 x − 3.4x − 0.3x4 ). La constante T n’influe pas sur la
       position du maximum, nous pouvons donc travailler avec u(x) = t(x)/T .

                                  u(x) = 3.7x1/2 − 3.4x − 0.3x4

       Nous appliquons Newton à la dérivée première :

                             f (x) = u′ (x) = 1.85x−1/2 − 3.4 − 1.2x3

       Nous avons besoin de la dérivée de cette fonction, qui est la dérivée seconde de
       u(x) :
                            f ′ (x) = u′′ (x) = −0.925x−3/2 − 3.6x2
    3. Itérations de la méthode de Newton.
       La formule est xn+1 = xn − ff′(x n)
                                     (xn )
                                           . D’après la forme du profil, le maximum se situe
       vers x ≈ 0.3. Choisissons comme point de départ x0 = 0.3.
       — Itération 0 : x0 = 0.3




                                             6
~~~

## Page 7

~~~text
      — Itération 1 :

           f (x0 ) = 1.85(0.3)−0.5 − 3.4 − 1.2(0.3)3
                   = 1.85(1.8257) − 3.4 − 1.2(0.027) = 3.3776 − 3.4 − 0.0324 = −0.0548
           f (x0 ) = −0.925(0.3)−1.5 − 3.6(0.3)2
            ′

                   = −0.925(3.3437) − 3.6(0.09) = −3.0929 − 0.324 = −3.4169

                                      −0.0548
                         x1 = 0.3 −           = 0.3 − 0.01604 = 0.28396
                                      −3.4169
      — Itération 2 :

           f (x1 ) = 1.85(0.28396)−0.5 − 3.4 − 1.2(0.28396)3
                   = 1.85(1.8744) − 3.4 − 1.2(0.0229) = 3.4676 − 3.4 − 0.0275 = 0.0401
           f (x1 ) = −0.925(0.28396)−1.5 − 3.6(0.28396)2
            ′

                   = −0.925(3.5117) − 3.6(0.0806) = −3.2483 − 0.2902 = −3.5385

                                      0.0401
                     x2 = 0.28396 −           = 0.28396 + 0.01133 = 0.29529
                                      −3.5385
          Après seulement deux itérations, on obtient une très bonne approximation de
      la position du maximum de l’épaisseur. La valeur de x où l’épaisseur est maximale
      est d’environ 0.295.
   [12pt, a4paper]article
   a4paper, margin=2.5cm


Exercice 12 : Intersection d’un cercle et d’une ellipse
Rappel de cours : Méthode de Newton pour un système Pour résoudre un
système d’équations non linéaires de la forme F(X) = 0, où X = (x1 , . . . , xn )T est un
vecteur et F est une fonction vectorielle, la méthode de Newton se généralise. La suite
des itérés est donnée par :

                             Xk+1 = Xk − [J(Xk )]−1 F(Xk )

où J(Xk ) est la matrice Jacobienne de F évaluée au point Xk . C’est la matrice des
dérivées partielles.



Énoncé : Déterminer les points d’intersection d’un cercle et d’une ellipse situés dans le
premier cadran.          (
                          f1 (x, y) = x2 + y 2 − 2 = 0
                          f2 (x, y) = x2 + 16y 2 − 4 = 0
   1. Mise en place de la méthode.
                                                                     2             
                                 x                                      x + y2 − 2
      On définit le vecteur X =     et la fonction vectorielle F(X) =                  .
                                 y                                     x2 + 16y 2 − 4



                                            7
~~~

## Page 8

~~~text
         La matrice Jacobienne J(X) est :
                                                     !
                                         ∂f1   ∂f1                
                                         ∂x    ∂y           2x 2y
                             J(x, y) =   ∂f2   ∂f2       =
                                         ∂x    ∂y
                                                            2x 32y

         On a besoin de l’inverse de la Jacobienne, [J(x, y)]−1 . Le déterminant est
      det(J) = (2x)(32y) − (2y)(2x) = 64xy − 4xy = 60xy.
                                                         
                                      −1    1    32y −2y
                             [J(x, y)] =
                                          60xy −2x 2x
      La formule itérative est donc :
                                                     2              
                  xk+1        xk        1      32yk −2yk    xk + yk2 − 2
                         =        −
                  yk+1        yk      60xk yk −2xk 2xk     x2k + 16yk2 − 4

   2. Solution exacte.
      Soustrayons la première équation à la seconde : (x2 + 16y 2 − 4) − (x2 + y 2 − 2) =
                                            2
      0 =⇒ 15y 2 − 2 = 0 =⇒ y 2 = 15          . Comme on est dans le premier cadran,
                           q
                             2
      y > 0, donc y =        15
                                ≈ 0.3651. En remplaçant dans la première équation :
                                                                      q
            2                          2
      x2 + 15 − 2 = 0 =⇒ x2 = 2 − 15     = 2815
                                                . Puisque x > 0, x =    28
                                                                        15
                                                                           ≈ 1.3660. La
                           p      p
      solution exacte est ( 28/15, 2/15).
   3. Itérations de Newton.                                                            
                                                                                      1
      Choisissons un point de départ dans le premier cadran, par exemple X0 =             .
                                                                                     0.5
         Itération0 : X0 = (1, 0.5)T.         
                     12 + 0.52 − 2         −0.75
      — F(X0 ) =                       =          .
                   12 + 16(0.5) 2
                               −4           1                   
                −1      1      32(0.5) −2(0.5)       1    16 −1
      — [J(X0 )] = 60(1)(0.5)                     = 30               .
                                −2(1)
                                        2(1)
                                                    −2       2               
                     −1          1   16 −1      −0.75        1     −13     0.4333
      — ∆X0 = −[J0 ] F0 = − 30                          = − 30          =           .
                                   −2 2       1                3.5    −0.1167
                           1 + 0.4333       1.4333
      X1 = X0 + ∆X0 =                    =           .
                          0.5 − 0.1167      0.3833
         Itération1 : X1 = (1.4333, 0.3833)T .           
                    (1.4333)2 + (0.3833)2 − 2         0.2012
      — F(X1 ) =                                 =             .
                   (1.4333)2 + 16(0.3833)2 − 4        0.4024                     
                                                                            1.3683
      — Le calcul complet est omis pour la brièveté, mais on trouve X2 ≈            .
                                                                            0.3654
      On constate une convergence très rapide vers la solution exacte (≈ 1.3660, ≈
      0.3651).


Exercice 13 : Intersection d’un cercle et d’une exponentielle
Énoncé : Résoudre le système d’équations :
                          (
                           f1 (x, y) = x2 + y 2 − 4 = 0
                           f2 (x, y) = ex + y − 1 = 0

                                           8
~~~

## Page 9

~~~text
Les solutions exactes sont (≈ 1.8, −1) et (≈ −1.9, 2). (Correction : les solutions données
dans l’énoncé original (1,-2) et (-2,1) sont incorrectes pour ce système.) On va converger
vers la seconde.
    1. Miseenplace de laméthode. 
            x               x2 + y 2 − 4
       X=      et F(X) =                 .
            y               ex + y − 1
         La matrice Jacobienne J(X) est :
                                                              
                                                         2x 2y
                                              J(x, y) =
                                                          ex 1

           Le déterminant est det(J) = 2x − 2yex .
                                                                           
                                              −1         1        1 −2y
                                  [J(x, y)]        =
                                                     2x − 2yex   −ex 2x

    2. Itérations de Newton.
       Pour converger vers la solution proche
                                                     de (−1.9, 2), choisissons un point de départ
                                        −2
       proche, par exemple X0 =                .
                                          2
                                            T
          Itération0 : X0 = (−2, 2)      .                                
                             2     2
                       (−2) + 2 − 4                   4                   4
       — F(X0 ) =          −2                =             −2    ≈               .
                        e    +  2
                                 − 1            1 +
                                                        e             1.1353
                       −4 4              −4       4
       — J(X0 ) = −2              ≈                   .
                      e       1       0.1353 1
       — det(J0 ) ≈ −4 −     4(0.1353) = −4.5412.
                                                
              −1       1           1        −4
       — [J0 ] ≈ −4.5412                          .
                               −0.1353 −4                                                         
                         −1              1           1          −4           4            1     −0.5412
       — ∆X0 = −[J0 ] F0 ≈ − −4.5412                                                 = 4.5412            ≈
                                               −0.1353 −4              1.1353                 −4.9812
            −0.119
                     .
            −1.097                                              
                                −2 − 0.119             −2.119
       X1 = X0 + ∆X0 ≈                           =                   .
                                 2 − 1.097               0.903
          Note : Le point de départ était trop éloigné, ce qui a causé un grand saut. Un
       meilleur point de départ, comme (−1.8, 1.8), aurait donné une meilleure conver-
       gence.                                                                    
                                                                            −1.9
          Choisissons un meilleur point de départ, X0 =                             . Itération 0 (bis) :
                                                                             2.0
                         T
       X0 = (−1.9, 2.0)
                     . 2                                  
                       (−1.9) + 22 − 4               3.61
       — F(X0 ) =          −1.9                =               .
                        e      +  2 − 1          1.149     
                       (−1.9)2 + 22 − 4             −0.39
       — F(X0 ) =          −1.9                =                 .
                     e         +2 −1             1.149
                      −3.8 4             −3.8 4
       — J(X0 ) =                   ≈                  .
                      e−1.9 1           0.149 1
       — det(J0 ) ≈ −3.8 − 4(0.149) = −4.396.


                                                      9
~~~

## Page 10

~~~text
                                                                         
                 −1            1        1    −4       −0.39        1    −4.986
— ∆X0 = −[J0 ]        F0 ≈ − −4.396                            ≈ 4.396          ≈
                                    −0.149 −3.8      1.149            −4.308
      −1.134
              .
      −0.98
                                 
        −1.9 − 1.134        −3.034
X1 ≈                   =              .
          2 − 0.98            1.02
    On observe que la méthode est très sensible au point de départ. La convergence
n’est garantie que si X0 est suffisamment proche de la racine.




                                          10
~~~
