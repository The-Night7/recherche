# ALGEBRE LINEAIRE CORRIGÉ TD2.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1QOorU56s9qpVyArW-X8o5MU1U5YYYhFz) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Algèbre Linéaire Appliquée
     Corrigé du TD2
   CY Tech - ING1 Mathématiques

          12 octobre 2025




                1
~~~

## Page 2

~~~text
Exercice 8 : Méthode du point fixe pour une équation du second
degré
   Question : On cherche à résoudre l’équation x2 − 2x − 3 = 0 par une méthode de point fixe.

1. Déterminer les solutions exactes.
  Solution Détaillée

  C’est une équation du second degré. On calcule le discriminant ∆ = b2 − 4ac.

                         ∆ = (−2)2 − 4(1)(−3) = 4 + 12 = 16 = 42

  Les solutions sont donc :                   √
                                        −b ± ∆    2±4
                                x1,2 =          =
                                            2a     2
  Ce qui nous donne deux racines distinctes :
     — x1 = 2−42 = −1
              2+4
     — x2 = 2 = 3


2. Appliquer l’algorithme de point fixe pour g1 , g2 , g3 en partant de x0 = 4.
                                       Rappel du Cours
  La méthode du point fixe consiste à transformer une équation f (x) = 0 en une forme
  équivalente x = g(x). On construit ensuite une suite (xk )k par la relation de récurrence
  xk+1 = g(xk ).
  La convergence de la méthode est assurée localement si la fonction g est contractante,
  c’est-à-dire si |g ′ (r)| < 1 au voisinage de la racine r.

  Solution Détaillée
  On part de x0 = 4 et √
                       on calcule les premiers termes pour chaque fonction.
     — Pour g1 (x) = 2x + 3 :
                                    p            √
                     x1 = g1 (4) = 2(4) + 3 = 11 ≈ 3.3166
                                         p                 √
                     x2 = g1 (3.3166) = 2(3.3166) + 3 = 9.6332 ≈ 3.1037
                                         p                 √
                     x3 = g1 (3.1037) = 2(3.1037) + 3 = 9.2074 ≈ 3.0344
                        ..
                         .
                       3
      — Pour g2 (x) = x−2 :

                                       3
                       x1 = g2 (4) =        = 1.5
                                     4−2
                                          3         3
                       x2 = g2 (1.5) =         =        = −6
                                       1.5 − 2     −0.5
                                          3
                       x3 = g2 (−6) =          = −0.375
                                       −6 − 2
                                                 3           3
                       x4 = g2 (−0.375) =               =        ≈ −1.2631
                                            −0.375 − 2    −2.375
                         ..
                          .


                                              2
~~~

## Page 3

~~~text
                          2
     — Pour g3 (x) = x 2−3 :

                                            42 − 3    13
                              x1 = g3 (4) =         =     = 6.5
                                               2       2
                                              6.52 − 3    42.25 − 3
                              x2 = g3 (6.5) =          =            = 19.625
                                                 2            2
                                                  19.6252 − 3
                              x3 = g3 (19.625) =              ≈ 191.07
                                                       2
                                ..
                                 .


3. Dans quels cas converge-t-on apparemment, et vers quelle racine ?
  Conclusion
     — La suite générée par g1 semble converger vers la racine x2 = 3.
     — La suite générée par g2 semble converger (en oscillant) vers la racine x1 = −1.
     — La suite générée par g3 diverge très rapidement.


4. Expliquer les résultats que vous constatez.
  Solution Détaillée
  Pour expliquer la convergence, nous devons étudier la condition |g ′ (r)| < 1 pour chaque
  fonction au voisinage des racines r = −1 et r = 3.
  Calculons d’abord les dérivées :
     — g1′ (x) = 2√2x+3
                     2        1
                         = √2x+3
                   −3
     — g2′ (x) = (x−2)2

     — g3′ (x) = x
  Évaluons maintenant ces dérivées aux points fixes (les racines) :

               Dérivée              Valeur en r1 = −1               Valeur en r2 = 3
                g1′ (x)             |g1′ (−1)| = | √11 | = 1    |g1′ (3)| = | √19 | = 13 < 1
                                                −3                             −3
                g2′ (x)       |g2′ (−1)| = | (−3)         1
                                                   2| = 3 < 1   |g2′ (3)| = | (1)2| = 3 > 1

                g3′ (x)            |g3′ (−1)| = | − 1| = 1           ′
                                                                  |g3 (3)| = |3| = 3 > 1

  Analyse des résultats :
    — Pour g1 : La condition de convergence est strictement vérifiée pour r2 = 3
       (|g1′ (3)| = 1/3 < 1). La méthode converge donc vers 3. Pour r1 = −1, |g1′ (−1)| = 1,
       la convergence n’est pas garantie et est généralement très lente (convergence sous-
       linéaire).
    — Pour g2 : La condition de convergence est strictement vérifiée pour r1 = −1
       (|g2′ (−1)| = 1/3 < 1). La méthode converge donc vers -1. Pour r2 = 3, |g2′ (3)| =
       3 > 1, le point fixe est répulsif, la méthode diverge de ce point.
    — Pour g3 : Pour r2 = 3, on a |g3′ (3)| = 3 > 1, donc le point est répulsif. Comme
       notre point de départ x0 = 4 est proche de 3, la suite s’éloigne rapidement de cette
       racine. Pour r1 = −1, |g3′ (−1)| = 1, la convergence n’est pas garantie.




                                                     3
~~~

## Page 4

~~~text
Exercice 9 : Étude d’une famille de fonctions pour le point fixe
   Question : Soit λ ∈ R. On pose g(x) = λx(1 − x).
   Modifions la condition de λ en λ ∈ R∗ car autrement il est inutile d’étudier la
fonction g nulle.

1. Déterminer les points fixes de la fonction g.
                                       Rappel du Cours
  Par définition un point fixe d’une fonction g est une valeur r qui reste invariante par cette
  fonction, c’est-à-dire une solution de l’équation g(r) = r.

  Solution Détaillée
  On résout l’équation g(x) = x pour trouver les points fixes :

                                            λx(1 − x) = x
                                             λx − λx2 = x
                                         λx − λx2 − x = 0
                                         x(λ − λx − 1) = 0

  Cette équation produit deux solutions :
     — Soit x = 0. C’est notre premier point fixe et on va le symboliser par, r1 (λ) = 0.
     — Soit λ − λx − 1 = 0. En isolant x, on trouve λx = λ − 1. Si λ ̸= 0, on obtient le
         second point fixe et on va le symboliser par, r2 (λ) = λ−1
                                                                 λ .


  Conclusion
  La fonction g admet deux points fixes :
     — r1 (λ) = 0.
     — r2 (λ) = 1 − λ1 .


2. Déterminer pour chaque point fixe, les valeurs de λ pour lesquelles ce point
fixe est attractif.
                                       Rappel du Cours
  Un point fixe r, dans notre exercice noté par ri (λ) pour tout i ∈ {1, 2}, est dit attractif si
  la méthode du point fixe converge localement vers lui. Une condition suffisante pour cela
  est que la fonction g soit contractante au voisinage de r, ce qui se traduit par l’inégalité :

                                            |g ′ (r)| < 1

  Attention, ceci est une condition suffisante, il se peut qu’on ait un autre en-
  semble de fonctions g vérifiant une autre hypothèse que |g ′ (r)| < 1 au voisinage
  de r afin que la méthode du point fixe converge localement vers r..

  Solution Détaillée
  D’abord, calculons la dérivée de g :

                                  g ′ (x) = λ − 2λx = λ(1 − 2x)


                                                 4
~~~

## Page 5

~~~text
  Cas du point fixe r1 (λ) :
    — On évalue la dérivée en r1 (λ) : g ′ (0) = λ(1 − 2(0)) = λ.
    — On applique la condition de convergence : |g ′ (0)| < 1 =⇒ |λ| < 1.
    — Le point fixe r1 (λ) est donc attractif si et seulement si λ ∈] − 1, 1[.
  Cas du point fixe r2 (λ) :
    — On évalue la dérivée en r2 (λ) :
                                                           
             ′ λ−1                 λ−1             λ − 2(λ − 1)
           g            =λ 1−2               =λ                   = λ − 2λ + 2 = 2 − λ
                 λ                   λ                   λ

     — On applique la condition de convergence : |g ′ (r2 (λ))| < 1 =⇒ |2 − λ| < 1.
     — On résout l’inégalité :

                                              −1 < 2 − λ < 1
                                           −1 − 2 < −λ < 1 − 2
                                              −3 < −λ < −1
                                                1<λ<3

     — Le point fixe r2 (λ) est donc attractif si et seulement si λ ∈]1, 3[.


3. Déterminer la valeur de λ pour laquelle la convergence sera quadratique.

Lien entre le Développement de Taylor et la Convergence Quadra-
tique
                                       Rappel du Cours
  Pour une méthode de point fixe xk+1 = g(xk ) qui converge vers une racine r, on définit
  l’erreur à l’itération k par ek = xk − r.
  L’erreur à l’itération suivante est donc :

                                ek+1 = xk+1 − r = g(xk ) − g(r)

  Puisque xk = r + ek , on peut écrire :

                                     ek+1 = g(r + ek ) − g(r)

  Cette relation est la base de l’analyse de convergence.
  1. Application du Développement de Taylor
  On effectue un développement de Taylor de la fonction g(r + ek ) au voisinage de r. En
  supposant g suffisamment dérivable, on a :
                                                       g ′′ (r) 2 g ′′′ (r) 3
                     g(r + ek ) = g(r) + g ′ (r)ek +           e +         e + ...
                                                          2! k        3! k
  En substituant cette expansion dans l’équation de l’erreur ek+1 = g(r + ek ) − g(r), on
  obtient :
                                               g ′′ (r) 2
                                                               
                                      ′
                      ek+1 = g(r) + g (r)ek +          e + . . . − g(r)
                                                   2 k
  Ce qui se simplifie en :
                                          g ′′ (r) 2
                               ek+1 = g ′ (r)ek + e + O(e3k )
                                              2 k
  2. Application des conditions spécifiques


                                                 5
~~~

## Page 6

~~~text
Maintenant, appliquons les conditions (c’est une hypothèse sur g que nous écrivons)
g′ (r) = 0 et g′′ (r) ̸= 0.
     — Comme g ′ (r) = 0, le premier terme du développement (g ′ (r)ek ) s’annule.
     — Le terme dominant qui reste est celui en e2k .
L’expression de l’erreur devient alors, en négligeant les termes d’ordre supérieur à 2 :

                                                g ′′ (r) 2
                                       ek+1 ≈           e
                                                    2 k
                              ′′
L’expression finale ek+1 ≈ g 2(r) e2k correspond exactement à la forme générale de la conver-
gence quadratique ek+1 ≈ C · e2k (c’est ça la définition).
                                                                         g ′′ (r)
On identifie même la constante de convergence asymptotique : C =             2    .
C’est donc bien le développement de Taylor qui prouve que la condition g ′ (r) = 0 (avec
g ′′ (r) ̸= 0) est une condition suffisante pour garantir une convergence d’ordre 2 (quadra-
tique) pour une méthode de point fixe.

Solution Détaillée
Nous avons les dérivées de g :
    — g ′ (x) = λ(1 − 2x)
    — g ′′ (x) = −2λ
Nous appliquons les conditions de convergence quadratique à nos deux points fixes :
r1 (λ) = 0 et r2 (λ) = 1 − λ1 .

Analyse pour le point fixe r1 (λ) = 0 :
    1. Condition g ′ (r1 ) = 0 :
                                      g ′ (0) = λ(1 − 2(0)) = λ
       Pour que cette dérivée soit nulle, il faut que λ = 0.
    2. Condition g ′′ (r1 ) ̸= 0 :
                                          g ′′ (0) = −2λ ̸= 0

       Rappel : on avait dès le départ λ ̸= 0.
Conclusion pour r1 : La convergence quadratique n’est pas atteinte au sens strict. Le
cas λ = 0 est un cas dégénéré où la fonction g devient identiquement nulle et on avait dès
le départ exclu ce cas qui n’est pas du tout intéressant, et la suite atteint r1 = 0 en une
seule étape de manière triviale.

Analyse pour le point fixe r2 (λ) = 1 − λ1 :
    1. Condition g ′ (r2 ) = 0 : Nous avons déjà calculé g ′ (r2 ) = 2 − λ.

                                       2 − λ = 0 =⇒ λ = 2

    2. Condition g ′′ (r2 ) ̸= 0 : La dérivée seconde g ′′ (x) = −2λ est une constante (elle
       ne dépend pas de x). Pour λ = 2, on a :

                                       g ′′ (r2 ) = −2(2) = −4

       Puisque −4 ̸= 0, la deuxième condition est bien remplie.




                                                6
~~~

## Page 7

~~~text
Conclusion
La convergence de la méthode du point fixe est quadratique pour le point fixe r2 (λ) si
et seulement si λ = 2.
Dans ce cas, le point fixe est r2 (2) = 1 − 21 = 12 .




                                          7
~~~

## Page 8

~~~text
Exercice 10 : Vitesse de convergence de la méthode de Newton
                                                                  √
   Question : On considère six fonctions ayant toutes α =             2 pour zéro et on analyse la
convergence de la méthode de Newton à partir de x0 = 1.
                                                       √
1. Compléter le tableau des dérivées en x =             2.
  Solution Détaillée
  Pour chaque fonction, nous
                          √   devons calculer la dérivée première f ′ (x) et seconde f ′′ (x),
  puis les évaluer en x = 2.
     — f (x) = x2 − √ 2 =⇒ f√′ (x) = 2x, f ′′ (x) = 2       √
     — g(x) = x − 3x + (√ 6 − 2) =⇒ g ′ (x) = 2x − 3, g ′′ (x) = 2
                   2

     — h(x) = x2 −√   2x + (2 2 − 2)
                                   √  =⇒ h′ (x) = 2x − 2, h√′′ (x) = 2               √
     — i(x) = (x − 2)4 + 12 (x − 2) =⇒ i′ (x) = 4(x − 2)3 + 12 , i′′ (x) = 12(x − 2)2
                        √                             √                     √
     — j(x) = 18 (e4(x− 2) − 1) =⇒ j ′ (x) = 12 e4(x− 2) , j ′′ (x) = 2e4(x− 2)
                        √
     — k(x) = 21 (x − 2) =⇒ k ′ (x) = 12 , k ′′ (x) = 0
                       √
  En évaluant en x = 2, on obtient le tableau suivant :

                              √           f
                                          √      √ g √        √h          i   j   k
                                                                          1   1   1
              Dérivée 1ère en √2         2 2    2 2− 3       2 2−2        2   2   2
              Dérivée 2nde en 2           2        2           2          0   2   0


2. Tracer sur la figure (2.5) les quatre premiers termes des suites associées.
                                      Rappel du Cours
  Interprétation géométrique de la méthode de Newton : La méthode de Newton
  consiste à construire une suite d’approximations de la racine d’une fonction f . Pour passer
  d’un point xn au suivant xn+1 :
      1. On se place au point (xn , f (xn )) sur la courbe de la fonction.
      2. On trace la tangente à la courbe en ce point.
      3. Le nouveau point, xn+1 , est l’abscisse de l’intersection de cette tangente avec
         l’axe des abscisses (y = 0).

  Solution Détaillée
  D’abord, calculons les valeurs des quatre premiers termes pour chaque suite, en partant
  de x0 = 1.
  Pour la suite xfn (fonction f (x) = x2 − 2) :
     — xf0 = 1
     — xf1 = 1.5
     — xf2 = 1.41666...
     — xf3 = 1.414215...                    √      √
  Pour la suite xgn (fonction g(x) = x2 − 3x + 6 − 2) :
     — xg0 = 1
     — xg1 ≈ 2.056
     — xg2 ≈ 1.588
     — xg3 ≈ 1.435
  Construction graphique sur la Figure 2.5 :



                                                8
~~~

## Page 9

~~~text
      1. Pour xf1 :
         — Placez le point (x0 , f (x0 )) = (1, −1) sur la courbe noire de f .
         — Tracez la tangente à la courbe en ce point.
         — L’abscisse où cette tangente coupe l’axe des y = 0 est xf1 = 1.5.
      2. Pour xf2 :
         — Placez le point (x1 , f (x1 )) = (1.5, 0.25) sur la courbe de f .
         — Tracez la tangente en ce nouveau point.
         — L’intersection de cette tangente avec l’axe des abscisses vous donnera xf2 ≈
           1.417.
      3. Répétez
           √     le processus pour xf3 . Vous verrez que les points se rapprochent très vite
         de 2.
      4. Faites de même pour la fonction g (courbe rouge), en partant du même point
         x0 = 1. Vous observerez que la convergence est visiblement plus lente, comme
         discuté dans la question 6.

  Conclusion
  Le tracé des tangentes successives et de leurs intersections avec l’axe des abscisses permet
  de visualiser la convergence des suites de Newton. On constate graphiquement
                                                                            √            que la
  suite associée à la fonction f (courbe noire) s’approche de la racine 2 beaucoup plus
  rapidement que celle associée à la fonction g (courbe rouge).


3. Que se passe-t-il pour la fonction h ?
  Solution Détaillée

  La méthode de Newton est définie par la suite xn+1 = xn − hh(x  n)
                                                              ′ (x ) . Le point de départ est
                                                                  n
  x0 = 1.
  Calculons la dérivée de h en ce point : h′ (x) = 2x − 2.

                                     h′ (1) = 2(1) − 2 = 0

  La dérivée est nulle en x0 = 1. L’expression de x1 nécessiterait une division par zéro, ce
  qui est impossible.
  Interprétation géométrique : La tangente à la courbe de h au point d’abscisse x0 = 1
  est horizontale. Elle ne coupe donc jamais l’axe des abscisses pour fournir une nouvelle
  approximation. La méthode de Newton échoue dès la première itération.




                                               9
~~~

## Page 10

~~~text
5. Que se passe-t-il pour la fonction k ?
  Solution Détaillée
                            √
  La fonction k(x) = 12 (x − 2) est une fonction affine (une droite). La méthode de Newton
  consiste à approcher la fonction par sa tangente. Or, pour une droite, la tangente en
  n’importe quel point est la droite elle-même.
  Ainsi, dès la première itération, l’intersection de la tangente avec l’axe des abscisses est
  exactement la racine de la fonction.
                                             1
                                                    √
                              k(x0 )         2 (1 − 2)
                                                                   √      √
                   x1 = x0 − ′       =1−          1     = 1 − (1 − 2) = 2
                             k (x0 )              2

  La méthode converge en une seule itération.


6. Classer les fonctions f et g selon la vitesse de convergence.
  Conclusion
  La méthode de Newton appliquée à f converge plus vite que pour g.

  Solution Détaillée
  Explication : L’erreur de la méthode de Newton pour une racine simple α vérifie ap-
                          f ′′ (α) 2
  proximativement en+1 ≈ 2f  ′ (α) en . Pour une convergence rapide, il est préférable que le

                f ′′ (α)
  facteur           soit petit.
                2f ′ (α)
          √             √
  Ici, f ′′ (2) = g ′′ ( 2) = 2. La vitesse de convergence dépend donc de la valeur de la
  dérivée première
              √       au√voisinage de la racine.
      — |f ′ (√ 2)| = 2√ 2 ≈ √  2.83
      — |g ′ ( 2)| = 2 2 − 3 ≈ 2.83 − 1.73 = 1.10
                √                                f ′′
  Puisque |f ′ ( 2)| est plus grand, le facteur 2f  ′ est plus petit pour f . Géométriquement,
  une pente plus forte au niveau de la racine signifie que la tangente coupe l’axe des x plus
  près de la racine, accélérant la convergence.


7. Classer les fonctions i, j et k selon la vitesse de convergence.
  Conclusion
  L’ordre de convergence, du plus rapide au plus lent, est : k > i > j.

  Solution Détaillée
                                                                         √
  Explication : Les trois fonctions ont la même dérivée première en 2 (1/2). La différence
  de vitesse vient donc des dérivées d’ordre supérieur.
     — Fonction k : La convergence est exacte en une étape (voir question 5). C’est le
         cas le plus rapide possible.
                                  √   Cela est dû au√fait que k ′′ (x) = 0 pour tout x.
     — Fonction i : On a i′ ( 2) = 1/2 et i′′ ( 2) = 0. Le fait que la dérivée seconde
         s’annule à la racine implique une convergence d’ordre supérieur à 2 (en l’occurrence,
         d’ordre 3), ce qui est extrêmement
                                  √           rapide. √
     — Fonction j : On a j ( 2) = 1/2 mais j ′′ ( 2) = 2 ̸= 0. La convergence est donc
                                ′

         quadratique standard.



                                              10
~~~

## Page 11

~~~text
  Ainsi, la convergence "instantanée" de k est plus rapide que la convergence cubique de i,
  qui est elle-même plus rapide que la convergence quadratique de j.


8. Expliquer pourquoi les fonctions
                                √ g, h, i, j, k ne sont pas très adaptées pour
calculer des approximations de 2.
  Solution Détaillée
  Le but est de calculer une approximation d’un nombre que l’on ne connaît pas. Or, pour
                     √ g(x),
  évaluer les fonctions  √ h(x),√ i(x), j(x) et k(x) (ou leurs dérivées), il est nécessaire d’uti-
  liser la valeur de 2, 3 ou 6 dans les √    calculs. √                                      √
  Par   exemple,  pour calculer g(1) = 1 2 −   3(1) +    ( 6 − 2), il   faut déjà connaître    3 et
  √
     6. C’est un raisonnement circulaire : on ne peut pas utiliser la valeur que l’on cherche à
  calculer dans le processus de calcul lui-même.
  Seule la fonction f (x) = x2 − 2 et ses dérivées (f ′ (x) = 2x, f ′′ (x) = 2) n’utilisent que des
  opérations et des nombres rationnels. Elle est donc la seule fonction√de la liste qui soit
  réellement utilisable en pratique pour trouver une approximation de 2.




                                                 11
~~~

## Page 12

~~~text
Exercice 11 : Épaisseur maximale d’un profil d’aile NACA
    Question : Déterminer la valeur de x où l’épaisseur du profil d’aile est maximale en utilisant
la méthode de Newton.

                                        Rappel du Cours
   Justification de l’approche : Pour trouver la valeur de x qui maximise une fonction
   différentiable t(x), il faut trouver les points où sa dérivée première s’annule. Nous cherchons
   donc à résoudre l’équation :
                                                t′ (x) = 0
   Il s’agit d’un problème de recherche de zéro, pour lequel la méthode de Newton est
   parfaitement adaptée.
   La formule itérative de Newton est xk+1 = xk − ff′(x  k)
                                                       (xk ) .
   Dans notre cas, la fonction dont on cherche le zéro est f (x) = t′ (x). La formule devient
   donc :
                                                   t′ (xk )
                                     xk+1 = xk − ′′
                                                  t (xk )

   Solution Détaillée
   1. Calcul des dérivées
   La fonction de demi-épaisseur est donnée par t(x) = T · (3.7x1/2 − 3.4x − 0.3x4 ). On peut
   ignorer la constante multiplicative T pour la recherche du zéro de la dérivée.
      — Dérivée première :
                                                                 
                                                  3.7
                                    t′ (x) = T    √ − 3.4 − 1.2x3
                                                 2 x
       — Dérivée seconde :
                                                                     
                         ′′        3.7 −3/2       2      0.925        2
                        t (x) = T − x       − 3.6x = T −   √   − 3.6x
                                    4                    x x
   2. Application de la méthode de Newton
   Le corrigé suggère de partir du point initial x0 = 0.3.
   Première itération : On calcule t′ (0.3) et t′′ (0.3) (en omettant T ) :
                          1.85
             t′ (0.3)/T = √     − 3.4 − 1.2(0.3)3 ≈ 3.3779 − 3.4 − 0.0324 = −0.0545
                            0.3
                              0.925
            t′′ (0.3)/T = −      √    − 3.6(0.3)2 ≈ −5.6293 − 0.324 = −5.9533
                            (0.3) 0.3
   On peut maintenant calculer x1 :
                           t′ (x0 )         −0.0545
                 x1 = x0 − ′′       = 0.3 −         ≈ 0.3 − 0.00915 = 0.29085
                          t (x0 )           −5.9533
   Deuxième itération : On repart de x1 ≈ 0.29085.
                         1.85
     t′ (0.29085)/T = √          − 3.4 − 1.2(0.29085)3 ≈ 3.4305 − 3.4 − 0.0295 ≈ 0.001
                        0.29085
                               0.925
    t′′ (0.29085)/T = −           √         − 3.6(0.29085)2 ≈ −5.8847 − 0.3046 ≈ −6.1893
                        (0.29085) 0.29085
   On calcule x2 :
                      t′ (x1 )              0.001
            x2 = x1 − ′′       ≈ 0.29085 −         ≈ 0.29085 + 0.00016 = 0.29101
                     t (x1 )               −6.1893


                                                 12
~~~

## Page 13

~~~text
Conclusion
Après deux itérations, on obtient une excellente approximation de la solution. La suite
des itérés converge très rapidement :
    — x0 = 0.3
    — x1 ≈ 0.29085
    — x2 ≈ 0.29101
La valeur exacte est proche de 0.29098. On observe bien la convergence quadratique ca-
ractéristique de la méthode de Newton. L’épaisseur maximale de l’aile se trouve donc à
environ 29.1% de la corde à partir du bord d’attaque.




                                          13
~~~

## Page 14

~~~text
Exercice 12 : Intersection d’un cercle et d’une ellipse
   Question : Déterminer les points d’intersection d’un cercle avec une ellipse situés dans le
premier cadran, par la méthode de Newton vectorielle.

1. Formulation du problème
   Solution Détaillée
   On cherche à résoudre le système d’équations non linéaires suivant :
                      (                         (
                        x2 + y 2 = 2              x2 + y 2 − 2 = 0
                                          ⇐⇒
                        x2 + (4y)2 = 4            x2 + 16y 2 − 4 = 0

   Ce problème revient à trouver les zéros de la fonction F : R2 → R2 définie par :
                                                  2
                                                       x + y2 − 2
                                                                   
                                       f1 (x, y)
                          F (x, y) =             =
                                       f2 (x, y)     x2 + 16y 2 − 4
                                         
                                         x
   On note le vecteur des inconnues X =    . Le problème est donc de trouver X tel que
                                         y
   F (X) = 0.


2. Solution Analytique (pour comparaison)
   Solution Détaillée
   On peut résoudre ce système directement pour trouver la solution exacte et évaluer la
   précision de la méthode numérique. En soustrayant la première équation à la seconde, on
   obtient :

                             (x2 + 16y 2 − 4) − (x2 + y 2 − 2) = 0
                                                    15y 2 − 2 = 0
                                                                 2
                                                           y2 =
                                                                15
                                                                             q
                                                                                 2
   Comme on cherche une solution dans le premier cadran (y ≥ 0), on a y =        15 .
   On remplace y 2 dans la première équation pour trouver x :
                              2                   2     30 − 2     28
                        x2 +    = 2 =⇒ x2 = 2 −       =          =
                             15                   15      15       15
                                                          q
   Comme on est dans le premier cadran (x ≥ 0), on a x = 28 15 .
                                    p                    
                                      28/15         1.36626
   La solution exacte est donc X ∗ = p        ≈               .
                                       2/15        0.365148




                                               14
~~~

## Page 15

~~~text
3. Méthode de Newton Vectorielle
                                     Rappel du Cours
  Le principe de la méthode de Newton dans le cas vectoriel est décrit à la section 2.2.2
  (page 37) du cours. À partir d’un point initial Xk , on trouve le point suivant Xk+1 en
  deux étapes :
      1. Résoudre le système linéaire : JF (Xk ) · Yk = −F (Xk ), où Yk est le vecteur de
         correction.
      2. Mettre à jour la solution : Xk+1 = Xk + Yk .
  JF (X) est la matrice Jacobienne de la fonction F au point X.

  Solution Détaillée

  Étape 1 : Calculer la matrice
                               2 Jacobienne
                                x + y2 − 2
                                              
  La Jacobienne de F (x, y) =                   est :
                               x2 + 16y 2 − 4
                                                    !
                                        ∂f1   ∂f1                
                                        ∂x    ∂y           2x 2y
                            JF (X) =    ∂f2   ∂f2       =
                                        ∂x    ∂y
                                                           2x 32y

  Étape 2 : Appliquer une itération manuellement                                      
                                                                                      1.3
  Le fichier Python ‘TD2-Exo12.py‘ fourni avec le TD utilise le point de départ X0 =      .
                                                                                      0.3
  Effectuons la première itération.
      — Calcul de F (X0 ) :

                              (1.3)2 + (0.3)2 − 2
                                                                              
                                                      1.69 + 0.09 − 2        −0.22
                 F (X0 ) =                          =                     =
                             (1.3)2 + 16(0.3)2 − 4    1.69 + 1.44 − 4        −0.87

     — Calcul de JF (X0 ) :
                                                               
                                        2(1.3) 2(0.3)     2.6 0.6
                            JF (X0 ) =                  =
                                        2(1.3) 32(0.3)    2.6 9.6

     — Résolution du système JF (X0 ) · Y0 = −F (X0 ) :
                                                       
                          2.6 0.6             −0.22     0.22
                                    Y =−              =
                          2.6 9.6 0           −0.87     0.87

       En soustrayant la première ligne de la seconde, on a (9.6 − 0.6)∆y0 = 0.87 −
       0.22 =⇒ 9∆y0 = 0.65, soit ∆y0 ≈ 0.07222. En réinjectant dans la première ligne :
       2.6∆x0 + 0.6(0.07222) = 0.22 =⇒ 2.6∆x0 ≈ 0.17667, soit ∆x0 ≈ 0.06795. Le
                                    0.06795
       vecteur correction est Y0 ≈           .
                                    0.07222
     — Mise à jour de la solution :
                                                                
                                         1.3     0.06795     1.36795
                       X1 = X0 + Y0 =          +          =
                                         0.3     0.07222     0.37222

  Après une seule itération, on est déjà très proche de la solution exacte X ∗ ≈
  (1.36626, 0.365148).




                                              15
~~~

## Page 16

~~~text
Conclusion
La méthode de Newton vectorielle converge très rapidement. Le fichier ‘TD2-Exo12.py‘
montre que la solution est trouvée avec une précision
                                                       de 10−4en seulement 3 itérations.
                                                   1.36626004
    — Solution numérique finale : Xf inal =
                                                   0.36514837
                                                   
                                         1.36626010
    — Solution analytique : X ∗ =
                                         0.36514837
L’écart (norme euclidienne) entre la solution numérique et la solution exacte est infime,
de l’ordre de 6 × 10−8 , ce qui démontre la grande efficacité de la méthode lorsque le point
de départ est bien choisi.




                                            16
~~~

## Page 17

~~~text
Exercice 13 : Résolution d’un système non linéaire
                                                                (
                                                                 x2 + y 2 = 4
   Question : On recherche les solutions du système d’équations                        par la mé-
                                                                 ex + y = 1
                                                      −4
thode de Newton vectorielle, avec une précision ϵ = 10 .

1. Formulation du problème et note sur les solutions
   Solution Détaillée

   On cherche les zéros de la fonction F : R2 → R2 définie par :
                                                    2
                                                     x + y2 − 4
                                                                
                                         f1 (x, y)
                            F (x, y) =             =
                                         f2 (x, y)    ex + y − 1

   Note importante

   L’énoncé du TD mentionne que les solutions exactes sont (1, −2) et (−2, 1). Ceci est une
   erreur. En effet, aucun de ces couples ne vérifie la première équation (12 + (−2)2 = 5 ̸= 4
   et (−2)2 + 12 = 5 ̸= 4). Le but de l’exercice est justement de trouver les vraies solutions
   par une méthode numérique.


2. Méthode de Newton Vectorielle
                                      Rappel du Cours
   L’algorithme de Newton pour un système F (X) = 0 est une méthode itérative (Support
   de cours, section 2.2.2, page 37). À chaque étape, on met à jour l’approximation Xk
   en calculant Xk+1 = Xk + Yk , où le vecteur de correction Yk est la solution du système
   linéaire :
                                  JF (Xk ) · Yk = −F (Xk )
   JF (X) est la matrice Jacobienne de F .

   Solution Détaillée

   Étape 1 : Calculer la matrice
                                2 Jacobienne
                                x + y2 − 4
                                           
   La Jacobienne de F (x, y) =               est :
                                ex + y − 1
                                                 !
                                          ∂f1   ∂f1           
                                          ∂x    ∂y       2x 2y
                              JF (X) =    ∂f2   ∂f2   =
                                          ∂x    ∂y
                                                          ex 1

   Étape 2 : Choix des points de départ
   Graphiquement, on voit que les courbes du cercle x2 +y 2 = 4 et de l’exponentielle y = 1−ex
   se croisent en deux points :                                                             
                                                                                         −1.8
       — Une solution avec x < 0 et y > 0. Un point de départ judicieux serait X0 =           .
                                                                                         0.8
                                                                                            
                                                                                         1.9
       — Une solution avec x > 0 et y < 0. Un point de départ judicieux serait X0 =           .
                                                                                         −0.6
   Étape 3 : Application
                          d’une itération (pour la 1ère solution)
                       −1.8
   Partons de X0 =           .
                       0.8


                                                17
~~~

## Page 18

~~~text
   — Calcul de F (X0 ) :

                     (−1.8)2 + (0.8)2 − 4
                                                                    
                                              3.24 + 0.64 − 4      −0.12
          F (X0 ) =                        =                   =
                         e−1.8 + 0.8 − 1     0.1653 + 0.8 − 1     −0.0347

   — Calcul de JF (X0 ) :
                                                               
                                     2(−1.8) 2(0.8)      −3.6 1.6
                         JF (X0 ) =                  =
                                      e−1.8    1        0.1653 1

   — Résolution du système JF (X0 ) · Y0 = −F (X0 ) :
                                                     
                             −3.6 1.6              0.12
                                           Y0 =
                            0.1653 1             0.0347
                                                                                   
                                                                            −0.0167
     La résolution de ce système 2 × 2 donne le vecteur de correction Y0 ≈           .
                                                                             0.0375
   — Mise à jour de la solution :
                                                                   
                                      −1.8       −0.0167       −1.8167
                   X1 = X0 + Y0 =           +              =
                                       0.8        0.0375        0.8375

On continuerait ce processus jusqu’à ce que la norme du vecteur de correction Yk soit
inférieure à ϵ = 10−4 .

Conclusion
En poursuivant les itérations (par exemple avec un script Python), on trouve les deux
solutions avec la précision requise :          
                                           −1.8
    — Solution 1 : En partant de X0 =            , la méthode converge en 3 itérations
                                            0.8
       vers :                                        
                                       ∗    −1.817256
                                      X1 ≈
                                             0.838183
                                               
                                            1.9
    — Solution 2 : En partant de X0 =            , la méthode converge en 3 itérations
                                           −0.6
       vers :                                        
                                       ∗     1.957584
                                      X2 ≈
                                            −0.370817
Le critère d’arrêt est atteint car la norme de la correction à la 3ème itération est inférieure
à 10−4 . L’écart à la "vraie" solution est donc maîtrisé par la précision demandée.




                                              18
~~~
