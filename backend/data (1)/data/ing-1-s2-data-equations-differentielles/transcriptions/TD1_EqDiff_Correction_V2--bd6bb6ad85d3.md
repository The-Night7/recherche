# TD1_EqDiff_Correction_V2.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1cggLPYLi7cK26csPFUuQLj0wjg0_Xe6v) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
TD1 - Équations Diérentielles                          ING1-MF


                 CORRECTION TD1
                       Équations Diérentielles
                           ING1-MF - 2021/2022




       Document complet avec rappels de cours et exercices
                          corrigés



Contents




                                   1
~~~

## Page 2

~~~text
TD1 - Équations Diérentielles                                               ING1-MF

1     Rappels de cours

1.1 Équations diérentielles linéaires du premier ordre
    Dénition
    Une équation de la forme :
                                     y ′ + a(t)y = b(t)
    est appelée équation diérentielle linéaire du premier ordre.

    Méthode de résolution
    Stratégie de résolution en 3 étapes :
    1. Solution homogène : Résoudre y′ + a(t)y = 0
                                                              Z
                            yh (t) = Ce−A(t)
                                               où A(t) =          a(t) dt


    2. Solution particulière : Utiliser la variation de la constante
                                                   Z
                                           −A(t)
                                 yp (t) = e            b(t)eA(t) dt


    3. Solution générale : y(t) = yh (t) + yp (t)

    Rappel
    Astuce : Pour les seconds membres simples (constante, polynôme, exponentielle,
    trigonométrique), on peut chercher directement une solution particulière de même
    forme.

1.2 Équations à variables séparées
    Dénition
    Une équation de la forme :
                                      dy
                                         = f (t) · g(y)
                                      dt
    est une équation à variables séparées.




                                               2
~~~

## Page 3

~~~text
TD1 - Équations Diérentielles                                           ING1-MF

  Méthode de résolution
  Méthode :
                   dy
  1. Réécrire :        = f (t) dt
                  g(y)
                                    Z            Z
                                         dy
  2. Intégrer les deux côtés :               =       f (t) dt
                                        g(y)
  3. Résoudre pour y(t)

1.3 Équations de Bernoulli
  Dénition
  Une équation de la forme :

                              y ′ = a(t)y + b(t)y n         avec n ≥ 2

  est une équation de Bernoulli.

  Méthode de résolution
  Changement de variable :
                              z = y 1−n =⇒ z ′ = (1 − n)y −n y ′

  L'équation devient linéaire en z :
                               z ′ + (1 − n)a(t)z = (1 − n)b(t)


1.4 Analyse qualitative
  Concepts clés
  ▶ Point d'équilibre : ye tel que f (ye ) = 0

  ▶ Stabilité :

     ▶ Stable si f ′ (ye ) < 0 (convergence)
     ▶ Instable si f ′ (ye ) > 0 (divergence)

  ▶ Isocline Ik : Lieu des points où y ′ = k

  ▶ Champ de vecteurs : Représentation graphique de y ′ (t, y)




                                                     3
~~~

## Page 4

~~~text
TD1 - Équations Diérentielles                                             ING1-MF

2     Exercices corrigés

2.1 Modélisation - Résolution analytique
  Exercice 1 : Oscillateur amorti
    Contexte : Une masse m oscille avec frottement.
    Équation : mv′ = λ cos t − kv
    où λ cos t est la force d'oscillation et −kv la force de frottement.

Question 1 : Déterminer la vitesse v(t)
On réécrit l'équation sous forme standard :
                                            k    λ
                                     v′ +     v=   cos t
                                            m    m

    Étape 1 : Solution homogène
    L'équation homogène est : v ′ + mk v = 0
                            dv    k                k
                               = − dt =⇒ ln |v| = − t + C1
                            v     m                m
                                                     k
                                       vh (t) = Ce− m t




                                               4
~~~

## Page 5

~~~text
TD1 - Équations Diérentielles                                                  ING1-MF


   Étape 2 : Solution particulière
   On cherche vp (t) = A cos t + B sin t
   En dérivant : vp′ (t) = −A sin t + B cos t
   Substitution dans l'équation :
                                              k                       λ
                    −A sin t + B cos t +        (A cos t + B sin t) =   cos t
                                              m                       m
   Identication des coecients :
                                                    k    λ
                                     cos t : B +      A=
                                                   m     m
                                                      k
                                        sin t : −A + B = 0
                                                      m
   De la deuxième : A = mk B
   Substitution dans la première :
                                   k2    λ        λm
                              B+    2
                                      B=   =⇒ B = 2
                                   m     m       m + k2

                                                      λk
                                            A=
                                                 m2 + k 2

   Résultat nal
                                        k        λ
                           v(t) = Ce− m t +            (k cos t + m sin t)
                                              m2 + k 2
   Interprétation physique :
   ▶ Le terme Ce− m t représente le régime transitoire (disparaît avec le temps)
                       k




   ▶ Le terme trigonométrique est le régime permanent (oscillation forcée)


Question 2 : Masse variable m(t) = m0 (1 − t)
L'équation devient :
                                   m0 (1 − t)v ′ = λ cos t − kv

                                            k          λ cos t
                                 v′ +              v=
                                        m0 (1 − t)    m0 (1 − t)




                                                  5
~~~

## Page 6

~~~text
TD1 - Équations Diérentielles                                            ING1-MF


  Solution homogène :
                                     dv        k
                                        =−            dt
                                      v    m0 (1 − t)
                                            k
                               ln |v| =        ln |1 − t| + cte
                                            m0

                                  vh (t) = C(1 − t)k/m0

  Résultat nal
  Pour la solution complète, on utilise la variation de la constante :
                                                  Z                  
                                     k/m0       λ        cos t
                    v(t) = (1 − t)           C+                     dt
                                                m0   (1 − t)k/m0 +1




                                                6
~~~

## Page 7

~~~text
TD1 - Équations Diérentielles                                        ING1-MF

   Exercice 2 : Loi de refroidissement de Newton
   Principe : Le taux de refroidissement est proportionnel à la diérence de
   température.

Question 1 : Équation diérentielle
Si T (t) est la température du corps et Tair celle de l'air :
   Résultat nal
                                     dT
                                        = −k(T − Tair )
                                     dt
   où k > 0 est le coecient de transfert thermique.

Question 2 : Calcul du temps de refroidissement
Données : Tair = 20C, T (0) = 100C, T (20) = 60C
  Cherché : Temps pour atteindre 30C
   Résolution :
                                      T ′ = −k(T − 20)
   C'est une équation à variables séparées :
                                         dT
                                              = −k dt
                                       T − 20

                                   ln |T − 20| = −kt + C1

                                     T (t) = 20 + Ce−kt


   Détermination de k :
   Conditions : T (0) = 100 =⇒ C = 80
   Donc : T (t) = 20 + 80e−kt
   De T (20) = 60 :
                                    60 = 20 + 80e−20k
                                                1
                                        e−20k =
                                                2
                                     ln 2
                                  k=      ≈ 0.0347 min−1
                                      20




                                               7
~~~

## Page 8

~~~text
TD1 - Équations Diérentielles                                             ING1-MF

  Calcul nal
  Pour T = 30C :
                                     30 = 20 + 80e−kt
                                                1
                                         e−kt =
                                                8
                                ln 8     3 ln 2
                             t=       =         = 60 minutes
                                 k      ln 2/20

  Résultat nal
                         Il faut 60 minutes pour atteindre 30°C
  Vérication : Le temps double à chaque fois que la diérence de température est
  divisée par 2 (propriété des exponentielles).
  ▶ 100 → 60 : ∆T = 80 → 40 en 20 min

  ▶ 60 → 40 : ∆T = 40 → 20 en 20 min

  ▶ 40 → 30 : ∆T = 20 → 10 en 20 min

  Total : 60 minutes

Question 3 : Température de l'air sinusoïdale
                                                         2πt
                                Tair (t) = −5 + 35 cos
                                                         365
  L'équation devient :
                                                                     2π
                       T ′ + kT = k (−5 + 35 cos ωt)     avec ω =
                                                                     365

  On cherche Tp (t) = A + B cos ωt + D sin ωt
  Après calculs d'identication :
                                           35k 2                35kω
                         A = −5,     B=           ,    D=
                                          ω2 + k2              ω2 + k2

  Résultat nal
                                          35k 2            35kω
                   T (t) = Ce−kt − 5 +           cos ωt +         sin ωt
                                         ω2 + k2          ω2 + k2
                            35ω 2
  Avec T (0) = 30 : C =
                           ω2 + k2




                                             8
~~~

## Page 9

~~~text
TD1 - Équations Diérentielles                                            ING1-MF

Question 4 : Variation brusque
Pour Tair (t) = 25 − 25t2 , on cherche Tp = A + Bt + Ct2 et on trouve :
   Résultat nal
                                                 50 50
                          T (t) = Ce−kt + 25 −      + t − 25t2
                                                 k2  k




                                            9
~~~

## Page 10

~~~text
TD1 - Équations Diérentielles                                             ING1-MF


  Exercice 3 : Équation logistique (Modèle de populations)
  Équation : x′ = ax − bx2 = ax 1 − ab x
                                           

  Contexte : Croissance d'une population de lapins avec ressources limitées.

Question 1 : Interprétation des constantes
  ▶ a > 0 : Taux de croissance naturel (natalité - mortalité)

  ▶ b > 0 : Facteur de compétition (eet de surpopulation)

  ▶ K = ab : Capacité de charge (population maximale soutenable)


Question 2 : Résolution par variables séparées
                                        dx
                                               = dt
                                     x(a − bx)

  Décomposition en éléments simples :
                                                  
                                1       1 1      b
                                      =       +
                            x(a − bx)   a x a − bx
                              Z                Z
                            1      dx    b dx
                                      +         = dt
                            a      x    a − bx
                            1
                              [ln |x| − ln |a − bx|] = t + C1
                            a
                                       x
                                ln          = at + C2
                                     a − bx


                                       x
                                            = Ceat
                                     a − bx

                                 x = aCeat − bxCeat

                                x(1 + bCeat ) = aCeat

                                            aCeat
                                     x=
                                          1 + bCeat




                                           10
~~~

## Page 11

~~~text
TD1 - Équations Diérentielles                                            ING1-MF

   Résultat nal
                                                   a
                                      x(t) =
                                               b + Ke−at
   Avec condition initiale x(0) = x0 :
                                                 x0 · ab
                                   x(t) =
                                            x0 + ab − x0 e−at
                                                         

   Forme courante :
                                         Kx0                          a
                          x(t) =                         avec K =
                                   x0 + (K − x0 )e−at                 b


Question 3 : Résolution par la méthode de Bernoulli
L'équation x′ = ax − bx2 est de Bernoulli avec n = 2.

   Changement de variable : z = x−1
                                        1              z′
                                      x= ,       x′ = − 2
                                        z              z
   L'équation devient :
                                         z′  a  b
                                        − 2 = − 2
                                         z   z z
   En multipliant par −z 2 :
                                         z ′ = −az + b

                            z ′ + az = b      (Équation linéaire !)

   Solution :
   Solution homogène : zh = Ce−at
   Solution particulière : zp = ab
                                                         b
                                       z(t) = Ce−at +
                                                         a
   Retour à x :
                                    1        1             a
                          x(t) =        =            =
                                   z(t)   Ce−at + ab   aCe−at + b




                                               11
~~~

## Page 12

~~~text
TD1 - Équations Diérentielles                                               ING1-MF

  Résultat nal
                                                   a
                                      x(t) =
                                               b + Ke−at
  On retrouve le même résultat !

Question 4 : Comportement asymptotique
  Pour x0 > 0 :
                                                    a a
                            lim x(t) = lim              =K =
                            t→∞        t→∞ b + Ke−at  b
  Conclusion : Quelle que soit la population initiale x0 > 0, la population converge
  vers la capacité de charge K = ab .

                    x(t)

                             x0 > K
                                                               K = ab

                           x0 ≈ K



                           x0 < K
                                                               t


Question 5 : Points d'équilibre et stabilité
  Points d'équilibre : x′ = 0
                                            b
                                      ax(1 − x) = 0
                                            a
                                                        a
                                  x1 = 0 et x2 =          =K
                                                        b


  Analyse de stabilité :
  Posons f (x) = ax − bx2 , alors f ′ (x) = a − 2bx

  ▶ En x1 = 0 : f ′ (0) = a > 0 =⇒ INSTABLE

  ▶ En x2 = ab : f ′ ab = a − 2a = −a < 0 =⇒ STABLE
                       



                                               12
~~~

## Page 13

~~~text
TD1 - Équations Diérentielles                                               ING1-MF

  Résultat nal
  Interprétation biologique :
  ▶ x = 0 instable : Si on introduit quelques lapins, la population croît

  ▶ x = K stable : Toute population positive converge vers la capacité de charge

  Diagramme de phase :
                x′




                                                                    x
              x1 = 0                                   x2 = K


                         x′ > 0 (croissance)         x′ < 0 (décroissance)




                                           13
~~~

## Page 14

~~~text
TD1 - Équations Diérentielles                                                   ING1-MF

   Exercice 4 : Datation au carbone 14
   Principe : Le C14 radioactif se désintègre après la mort d'un organisme.
   Loi : Perte de 8000
                    1
                       de la masse par an.


Question 1 : Équation diérentielle
Si p(t) est la proportion de C14 :
   Résultat nal
                                     dp     1
                                        =−      p = −λp
                                     dt    8000
   où λ = 8000
           1
               ≈ 1.25 × 10−4 an−1

   Solution :
                                       p(t) = p0 e−t/8000

Question 2 : Allure des solutions
                 p(t)
                  p0 élevé
                 p0 moyen
                 p0 faible

                                                            p0 /2



                                                                    t (années)


   Propriété : Temps de demi-vie t1/2 = 8000 ln 2 ≈ 5544 ans




                                              14
~~~

## Page 15

~~~text
TD1 - Équations Diérentielles                                           ING1-MF

Applications
  Application 1 : Homme de Néanderthal
  Données : p(t) = 0.0624 p0 (soit 6.24% restant)
  Calcul :
                                   0.0624 = e−t/8000
                                                   t
                                 ln(0.0624) = −
                                                8000
                   t = −8000 ln(0.0624) = 8000 × 2.774 ≈ 22192 ans


               L'homme de Néanderthal a vécu il y a environ 22 200 ans


  Application 2 : Homme de Cro-Magnon
  Estimation : Vivait entre 30 000 et 20 000 ans avant J.C.
  Calculs :
  Pour t = 20000 ans :
                     p = p0 e−20000/8000 = p0 e−2.5 ≈ 0.082 p0 = 8.2%

  Pour t = 30000 ans :
                    p = p0 e−30000/8000 = p0 e−3.75 ≈ 0.024 p0 = 2.4%


                  Le rapport C14 devrait se situer entre 2.4% et 8.2%




                                           15
~~~

## Page 16

~~~text
TD1 - Équations Diérentielles                                             ING1-MF


  Exercice 5 : Évaporation d'une goutte sphérique
  Problème : Une goutte d'eau s'évapore avec un débit proportionnel à sa surface.
   Données géométriques :
▶ Volume : V = 43 πr3

▶ Surface : S = 4πr2

  Modélisation :
  Le débit d'évaporation est :
                                 dV
                                    = −kS = −k · 4πr2
                                 dt
  Or :                                              
                                dV   d        4 3                 dr
                                   =            πr       = 4πr2
                                dt   dt       3                   dt
  Donc :
                                          dr
                                   4πr2      = −k · 4πr2
                                          dt
                                          dr
                                             = −k
                                          dt

  Intégration :
                                      r(t) = r0 − kt
  où r0 est le rayon initial.

  Résultat nal
                                          4
                                   V (t) = π(r0 − kt)3
                                          3
  Remarque : La goutte disparaît complètement au temps t∗ = rk         0




  Exercice 6 : Nutriments dans une cellule
  Modèle : Entrée constante, sortie proportionnelle à la concentration.
                                     dN
                                         = R − KN
                                      dt




                                               16
~~~

## Page 17

~~~text
TD1 - Équations Diérentielles                                           ING1-MF


  Résolution :
  C'est une équation linéaire : N ′ + KN = R
  Solution homogène : Nh = Ce−Kt
  Solution particulière : Np = KR (constante)

  Résultat nal
                                                        R
                                  N (t) = Ce−Kt +
                                                        K
  Avec N (0) = N0 : C = N0 − KR
                                          
                                         R          R
                            N (t) = N0 −     e−Kt +
                                         K          K


  Analyse d'équilibre :
                                  R
  Il existe un équilibre : Ne =
                                  K
                                                    R
                                      lim N (t) =
                                      t→∞           K
  L'équilibre est stable : toute condition initiale converge vers Ne .




                                            17
~~~

## Page 18

~~~text
TD1 - Équations Diérentielles                                   ING1-MF


   Exercice 7 : Équations diverses
   Résolution de 4 équations diérentielles variées.


a) (1 + x2 )dy −
                   p
                    1 − y 2 dx = 0

                                         dy        dx
                                       p       =
                                        1 − y2   1 + x2
                                     Z           Z
                                         dy           dx
                                       p       =
                                        1−y  2      1 + x2

                                   arcsin(y) = arctan(x) + C

   Résultat nal
                                     y = sin(arctan(x) + C)


b) x2 dy + (y − a)dx = 0
                                           dy   dx
                                              =− 2
                                          y−a   x
                                                      1
                                       ln |y − a| =     + C1
                                                      x

   Résultat nal
                                         y = a + Ke1/x


c) (1 − x2 )y′ − xy(1 + ay) = 0

                                           y′        x
                                                 =
                                       y(1 + ay)   1 − x2
                          1        1    a
   Décomposition :              = −
                      y(1 + ay)    y 1 + ay
                                          
                                  1    a           x dx
                                     −       dy =
                                  y 1 + ay        1 − x2
                                      y      1
                              ln          = − ln |1 − x2 | + C
                                   1 + ay    2




                                               18
~~~

## Page 19

~~~text
TD1 - Équations Diérentielles                                        ING1-MF

   Résultat nal
                                               K
                                   y=√
                                           1 − x2 − Ka


d) y − y′ cos(x) = y2 cos(x)(1 − sin(x))
                                      y
                                y′ =      − y 2 (1 − sin x)
                                    cos x
   C'est une équation de Bernoulli (n = 2).
   Changement : z = y −1
                                           z
                                  z′ +         = 1 − sin x
                                         cos x
   Solution nécessitant la variation de la constante (calcul long).




                                             19
~~~

## Page 20

~~~text
TD1 - Équations Diérentielles                                   ING1-MF

3     Résolution graphique

    Exercice 8 : Champ de vecteurs
    Dessiner le champ de vecteurs et tracer les solutions.

1. x′ = −t + 1
    Analyse :
    ▶ Le champ ne dépend que de t (pas de x)

    ▶ x′ > 0 pour t < 1 (croissance)

    ▶ x′ = 0 pour t = 1 (isocline verticale)

    ▶ x′ < 0 pour t > 1 (décroissance)

    Résultat nal
    Solution générale :
                                               t2
                                    x(t) = −      +t+C
                                               2
    Ce sont des paraboles avec un maximum en t = 1.

                             x




                                                             t
                                         t=1




                                               20
~~~

## Page 21

~~~text
TD1 - Équations Diérentielles                                    ING1-MF

2. x′ = −x/2
  Analyse :
  ▶ Le champ ne dépend que de x (autonome)

  ▶ x′ < 0 pour x > 0 (décroissance)

  ▶ x′ = 0 pour x = 0 (équilibre stable)

  ▶ x′ > 0 pour x < 0 (croissance vers 0)

  Résultat nal
  Solution générale :
                                    x(t) = Ce−t/2
  Toutes les solutions convergent exponentiellement vers 0.

                        x




                                                         x t= 0




                                            21
~~~

## Page 22

~~~text
TD1 - Équations Diérentielles                                                      ING1-MF

  Exercice 9 : Association graphiques - équations
  Pour chaque dessin, trouver l'isocline I0 , les points singuliers, et associer l'équation.


Équations à associer
                               x′ = 2, x′ = x − t, x′ = x
                                     x                 t
                               x′ = , x′ = t, x′ = −
                                     t                 x


Analyse des équations
  1) x′ = 2
  ▶ Isocline I0 : Aucune (jamais x′ = 0)

  ▶ Pente : Constante partout = 2

  ▶ Solutions : Droites x = 2t + C

  ▶ Caractéristique : Vecteurs tous horizontaux et parallèles

                                  Correspond au dessin 1

  2) x′ = x − t
  ▶ Isocline I0 : x = t (droite à 45°)

  ▶ Comportement :

     ▶ Au-dessus de x = t : x′ > 0 (croissance)
     ▶ En-dessous : x′ < 0 (décroissance)

  ▶ Caractéristique : Vecteurs horizontaux sur x = t

                                  Correspond au dessin 2




                                             22
~~~

## Page 23

~~~text
TD1 - Équations Diérentielles                               ING1-MF

  3) x′ = x
  ▶ Isocline I0 : x = 0 (axe horizontal)

  ▶ Comportement :

     ▶ x > 0 : x′ > 0 (croissance exponentielle)
     ▶ x < 0 : x′ < 0 (décroissance exponentielle)

  ▶ Solutions : x = Cet

  ▶ Caractéristique : Divergence/convergence exponentielle

                               Correspond au dessin 4

  4) x′ = xt
  ▶ Isocline I0 : x = 0 ou t → ∞

  ▶ Singularité : t = 0 (pente non dénie)

  ▶ Solutions : x = Ct (droites par l'origine)

  ▶ Caractéristique : Champ radial depuis l'origine

                               Correspond au dessin 3

  5) x′ = t
  ▶ Isocline I0 : t = 0 (axe vertical)

  ▶ Comportement :

     ▶ t > 0 : x′ > 0 (croissance)
     ▶ t < 0 : x′ < 0 (décroissance)

  ▶ Solutions : x = t2 + C (paraboles)
                       2




  ▶ Caractéristique : Symétrique par rapport à t = 0

                               Correspond au dessin 5




                                           23
~~~

## Page 24

~~~text
TD1 - Équations Diérentielles                              ING1-MF

  6) x′ = − xt
  ▶ Isocline I0 : t = 0 (axe vertical)

  ▶ Singularité : x = 0 (pente non dénie)

  ▶ Équation intégrable : x dx = −t dt

  ▶ Solutions : x2 + t2 = K (cercles centrés à l'origine)

  ▶ Caractéristique : Trajectoires circulaires fermées

                               Correspond au dessin 6


Tableau récapitulatif
                 maincolor!20 Dessin Équation
                          1            x′ = 2
                          2          x′ = x − t
                          3            x′ = xt
                          4            x′ = x
                          5            x′ = t
                          6           x′ = − xt




                                         24
~~~

## Page 25

~~~text
TD1 - Équations Diérentielles                                               ING1-MF

4    Synthèse et conseils

    Points clés à retenir

         1. Équations linéaires
            Toujours résoudre l'homogène d'abord, puis chercher une solution
            particulière
         2. Variables séparées
            Méthode simple et directe quand y ′ = f (t) · g(y)
         3. Bernoulli
            Le changement z = y 1−n transforme en équation linéaire
         4. Analyse qualitative
            Les isoclines et points d'équilibre donnent beaucoup d'informations sans
            calcul
         5. Modélisation
            Vérier l'homogénéité des unités et l'interprétation physique



    Conseils pour l'examen

         ✓ Identier le type d'équation avant de commencer

         ✓ Vérier la solution en la substituant dans l'équation

         ✓ Pour les applications, toujours donner les unités

         ✓ Faire des schémas pour les problèmes graphiques

         ✓ Ne pas oublier la constante d'intégration !

         ✓ Interpréter physiquement les résultats




                                         25
~~~

## Page 26

~~~text
TD1 - Équations Diérentielles                                                 ING1-MF


  Formules essentielles

  Équation linéaire :                       Variables séparées :
                                                          dy
                 y ′ + ay = b                                 = f (t) dt
                                                         g(y)
                y = Ce−at + yp
                                                       Z        Z
                                                          dy
                                                              = f (t) dt
                                                         g(y)
  Bernoulli :                               Décroissance exponentielle :
                y ′ = ay + by n                             y ′ = −ky
                  z = y 1−n
                                                            y = y0 e−kt




                  Bon courage pour vos révisions !

           N'hésitez pas à refaire les exercices sans regarder la correction




                                          26
~~~
