# 2122-MI2-TraitementSignal-ExamCorr.pdf

[Ouvrir l’original](https://drive.google.com/open?id=104oKijAZ5LO9_7uic8mKVpyBcvwqDhyr) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                           CYTECH         EXAMEN CORRECTION

                                                  Filière : ING2 MI
                                                  Matière : Traitement du Signal
                                                  Date : Avril 2022     Durée : 2h
  Département de Mathématiques                    Responsables : BARRAU Nelly ; DESPLAT Lucie
  Année universitaire 2021-2022

Exercice 1 [2 points] VRAI ou FAUX ?
Réponse exacte (+0.25pt), Pas de réponse (0pt), Réponse fausse (-0.25pt).
Aucune justification n’est demandé en cas de réponse VRAI.
Une justification doit être apportée en cas de réponse FAUX.
  1. Le bruit d’une image désigne les pixels de l’image dont l’intensité est très différente de celles des pixels
     voisins.
  2. Le filtre Laplacien ne possède pas un masque de convolution.
  3. Pour numériser une image analogique, une seule opération est nécessaire : l’échantillonnage.


Exercice 2 [2 points]
Considérons les deux images et les deux histogrammes suivants :




Associer chaque image à son histogramme en justifiant soigneusement vos réponses.


Exercice 3 [4 points] Distributions
Considérons les deux applications suivantes
                  f : R −→ R                                               g : R −→ R
                                                   1    si x ≥ 0
                       x 7−→ signe(x) =                                         x 7−→ |x|
                                                  −1    si x ≤ 0
  1. Justifier que f et g définissent des distributions de D0 (R).
     f et g sont localement intégrables : elles définissent donc bien des distributions.
  2. Déterminer f 0 et g 0 au sens des distributions.
     Soit ϕ ∈ D(R)
     — On a pour f 0 :
                                                     Z 0           Z +∞
                                0               0         0
                              hf , ϕi = −hf, ϕ i =       ϕ (x)dx −      ϕ0 (x)dx = 2ϕ(0)
                                                     −∞               0


                                                       1
~~~

## Page 2

~~~text
        Ainsi f 0 = 2δ0
      — On a pour g 0 :                                       Z 0                 Z +∞
                                     0                    0           0
                                   hg , ϕi = −hg, ϕ i =             xϕ (x)dx −           xϕ0 (x)dx
                                                               −∞                  0
         On effectue une intégration par partie pour chacune des deux intégrales
                         Z +∞                              Z +∞                Z +∞
                                   0                 +∞
                               xϕ (x)dx = [xϕ(x)]0 −              ϕ(x)dx = −        ϕ(x)dx
                              0                                      0                     0

         De même :                               Z 0                      Z 0
                                                          xϕ0 (x)dx = −         ϕ(x)dx
                                                     −∞                    −∞
         Il vient alors
                            Z 0                 Z +∞                Z +∞                       Z +∞
            hg 0 , ϕi = −         ϕ(x)dx +             ϕ(x)dx =            1[0;+∞[ ϕ(x)dx +           −1]−∞;0] ϕ(x)dx
                             −∞                  0                  −∞                         −∞

         Ainsi g 0 = 1[0;+∞[−1]−∞;0]


Exercice 4 [4 points] Convolution
Soit a ≥ 1 et considérons les deux applications suivantes

                                         f = 1[−1;1]          et          g = 1[−a;a]

  1. Justifier que le produit de convolution f ? g a un sens.
     f et g sont toutes deux des fonctions L2 (R) : nous pouvons donc calculer leur produit de convolution.
  2. Calculer f ? g.
     On a                                 Z                         Z 1                  Z 1−x
                          (f ? g)(x) =         f (y)g(x − y)dy =          g(x − y)dy =           g(u)du
                                           R                         −1                   −1−x
      Nous pouvons donc déjà en conclure que
      — si −1 − x ≥ a (ie x ≤ −a − 1) alors (f ? g)(x) = 0
      — si si 1 − x ≤ −a (ie x ≥ a + 1) alors (f ? g)(x) = 0
      Considérons à présent x ∈ [−a − 1; a + 1]. Alors
                         Z 1−x            Z min(1+x;a)
           (f ? g)(x) =         g(u)du =                 du = 2 + min(x; a − 1) + min(−x, a − 1)
                              −1−x                   max(−1+x;−a)

      On remarque que f ∗ g est paire. (Rmq. : On montre que si f et g sont paires alors f ∗ g est paire).
      Prenons alors x positif. On a alors pour x ∈ [0, a + 1]
                                               (
                                                 2            si x ∈ [0, a − 1]
                                 (f ∗ g)(x) =                                     .
                                                 1 + a − x si x ∈ [a − 1, a + 1]

      Finalement, on obtient
                                              
                                              
                                              0         si x ≤ −a − 1
                                              
                                              1 + a + x si x ∈ [−a − 1, −a + 1]
                                              
                                              
                                              
                                  (f ∗ g)(x) = 2         si x ∈ [−a + 1, a − 1] .
                                              
                                               1 + a − x si x ∈ [a − 1, a + 1]
                                              
                                              
                                              
                                              
                                              
                                               0         si x ≥ a + 1
                                              




                                                               2
~~~

## Page 3

~~~text
Exercice 5 [5 points] Convolution discrète
On souhaite réaliser la convolution 2D discrète de A par la distribution résumée par une matrice de convolution
M (de taille 3). La matrice A considérée est la suivante
                                                                
                                                      2 2 2
                                              A =  4 6 8
                                                     −1 0 1
  1. Donner la matrice de convolution M correspondant à l’élément neutre du produit de convolution.
     L’élément neutre du produit de convolution est
                                                             
                                                     0 0 0
                                               M = 0 1 0
                                                     0 0 0
  2. Prenons                                                  
                                                      1 1 1
                                               M = 1 1 1
                                                      1 1 1
      Donner B la convolution discrète de A par M (vos étapes de calculs doivent être visibles et justifiées)
      On cherche B ∈ M3 (R) telle que B = A ? M et
                                                              
                                                      a b c
                                               B = d e f 
                                                      g h i
      Considérons d’abord A0 correspondant à A que l’on entoure de 0 :
                                                                  
                                                 0 0 0 0 0
                                               0 2 2 2 0
                                            0
                                                                  
                                         A =   0    4    6  8   0
                                                                   
                                               0 −1 0 1 0
                                                 0 0 0 0 0
      — Pour déterminer a, posons                              
                                                         0 0 0
                                                 Aa = 0 2 2
                                                         0 4 6
         et effectuons le produit terme à terme de Aa avec M : on obtient Aa . a correspond à la somme de
         tous les éléments de Aa : autrement dit
                                                a = 2 + 2 + 4 + 6 = 14
      — Pour déterminer b, posons                              
                                                          0 0 0
                                                   Ab =  2 2 2 
                                                          4 6 8
         et effectuons le produit terme à terme de Ab avec M : on obtient Ab . b correspond à la somme de tous
         les éléments de Ab : autrement dit
                                            b = 2 + 2 + 2 + 4 + 6 + 8 = 24
      — Pour déterminer c, posons                                 
                                                           0 0 0
                                                   Ac = 2 2 0
                                                           6 8 0
         et effectuons le produit terme à terme de Ac avec M : on obtient Ac . c correspond à la somme de tous
         les éléments de Ac : autrement dit
                                                c = 2 + 2 + 6 + 8 = 18


                                                       3
~~~

## Page 4

~~~text
      En réitérant le processus, on obtient finalement
                                                               
                                                       14 24 18
                                                  B = 13 24 19
                                                       9 18 15



Exercice 6 [8 points]
On considère le circuit électrique correspondant au schéma suivant :




  On crée entre les bornes a et b une différence de potentiel E(t) dépendant du temps. Soit alors S(t) la
différence de potentiel entre les bornes c et d à l’instant t.
  On suppose E(t) et S(t) nulles pour t < 0. On note I(t) l’intensité du courant de b vers a à l’instant t.
  La résistance R et l’inductance L sont des constantes connues. On rappelle que l’on a les relations

                                      E − S = RI            et   S = L I 0.

  1. Montrer que l’on a
                                                         R
                                                    S0 +   S = E0                                         (1)
                                                         L
      On considère dans la suite, le circuit électrique comme un filtre qui à un signal d’entrée E associe un
      signal de sortie S.
      On a S = E − RI. En dérivant, on obtient S 0 = E 0 − RI 0 = E 0 − R            0   R
                                                                          L S d’où S + L S = E .
                                                                                                 0

  2. Soit T une distribution de D0 (R) et f ∈ C ∞ (R). Rappeler la définition du produit f × T.
     Vérifier que si f (0) = 1 alors f × δ0 = δ0 .
     Pour toute fonction f ∈ C ∞ (R),la distribution f × T est définie par : ∀ϕ ∈ D(R),

                                          < f × T, ϕ >=< T, f × ϕ > .

      Par conséquent, si f (0) = 1, on a ∀ϕ ∈ D(R), < f × δ0 , ϕ >=< δ0 , f ϕ >= f (0) × ϕ(0) = ϕ(0) =<
      δ0 , ϕ >. Cela montre que f × δ0 = δ0 .
                                                                                   R
  3. On considère maintenant la fonction f définie sur R par f (t) = H(t)e− L t où H est la fonction de
     Heaviside.
     (a) Justifier que f définit une distribution régulière T .
         f est localement intégrable et définit donc une distribution régulière.
     (b) Montrer que (δ00 + R
                            L δ0 ) ∗ T = δ0 .
         On a
                                                  R                     R
                                         (δ00 +     δ0 ) ∗ T = δ00 ∗ T + δ0 ∗ T
                                                  L                     L
                                                                      0 R
                                                             = δ0 ∗ T + T
                                                                         L
                                                                      R
                                                             = T 0 + T.
                                                                      L


                                                        4
~~~

## Page 5

~~~text
      Or au sens des distributions, on a
                                           R                R      R        R           R    R
                           T 0 = (H(t)e− L t )0 = δ0 e− L t −        H(t)e− L t = δ0 e− L t − T.
                                                                   L                         L
      Par conséquent,
                                         R                  R    R   R          R
                                (δ00 +     δ0 ) ∗ T = δ0 e− L t − T + T = δ0 e− L t .
                                         L                       L   L
                                               R
      La fonction f définie par f (t) = e− L t est de classe C ∞ et vérifie f (0) = 1. D’après la question 2,
                                                            R
                                                   (δ00 +     δ0 ) ∗ T = δ0 .
                                                            L
  (c) Montrer que T est une solution au sens des distributions de l’équation
                                                                R
                                                     T0 +         T = H 0.
                                                                L
      (T est donc le signal de sortie correspondant au signal d’entrée égal à H. On dit que T est « la »
      réponse indicielle du circuit).
      On a vu que
                                                   R      R         R
                                       T 0 = δ0 e− L t − T = δ0 − T,
                                                          L         L
      donc
                                                       R
                                                 T 0 + T = δ0 .
                                                        L
                0
      Or on a H = δ0 . Donc T vérifie bien la relation
                                                                R
                                                     T0 +         T = H 0.
                                                                L
  (d) On veut montrer l’unicité de la réponse indicielle. On considère une solution au sens des distributions
      de l’équation
                                                       R
                                                  S0 + S = H 0.
                                                       L
      Montrer que l’on a alors
                                                     R
                                              (δ00 + δ0 ) ∗ S = δ0 .
                                                     L
      En déduire que S = T.
      On a, comme précédemment,
                          R                     R                   R         R
                 (δ00 +     δ0 ) ∗ S = δ00 ∗ S + δ0 ∗ S = δ0 ∗ S 0 + S = S 0 + S = H 0 = δ0 .
                          L                     L                   L         L
      Montrons que S = T. En convoluant par T dans la relation (δ00 + R
                                                                      L δ0 ) ∗ S = δ0 , on obtient :

                                                        R
                                           T ∗ (δ00 +     δ0 ) ∗ S = T ∗ δ0 = T.
                                                        L
      De même, en convoluant par S dans la relation (δ00 + R
                                                           L δ0 ) ∗ T = δ0 , on aboutit à :

                                                        R
                                           S ∗ (δ00 +     δ0 ) ∗ T = S ∗ δ0 = S.
                                                        L
      Comme T ∗ (δ00 + R                  0   R
                       L δ0 ) ∗ S = S ∗ (δ0 + L δ0 ) ∗ T, on en conclut que T = S.
4. On note D la réponse impulsionnelle du circuit, c’est-à-dire la réponse correspondant au signal d’entrée
   E = δ0 . D est donc solution de
                                                    R
                                             D0 + D = δ00 .
                                                    L



                                                         5
~~~

## Page 6

~~~text
  (a) Montrer que l’on a T = D ∗ H.
      Il suffit de vérifier que D ∗ H est la réponse indicielle du système. Or
                                     R                     R             R
                        (D ∗ H)0 +     (D ∗ H) = D0 ∗ H + (D ∗ H) = (D0 + D) ∗ H
                                     L                     L             L
                                               = δ00 ∗ H = H 0 .

      Dela montre que D ∗ H est bien la réponse indicielle du système et par unicité de celle-ci, on a
      D ∗ H = T.
  (b) Par dérivation de la relation T = D ∗ H, en déduire l’expression de D.
      En dérivant au sens distribution, on obtient

                                             T 0 = D ∗ H 0 = D ∗ δ0 = D.

      Donc
                                                                R         R
                                           D = T 0 = δ0 −         T = δ0 − T.
                                                                L         L
                                                                                         R
5. Déterminer la réponse du circuit pour le signal d’entrée : E(t) = H(t)(1 − e− L t ).
   En procédant comme à la question 4.(a), on a
                                R                   R               R
                  (D ∗ E)0 +      (D ∗ E) = D0 ∗ E + (D ∗ E) = (D0 + D) ∗ E = E 0 .
                                L                   L               L
   La réponse du circuit est donc D ∗ E c’est-à-dire
                      R                   R                        R      R                R
              (δ0 −     T ) ∗ H(t)(1 − e− L t ) = δ0 ∗ H(t)(1 − e− L t ) − T ∗ H(t)(1 − e− L t )
                      L                                                   L
                                                             −R       R               R
                                                = H(t)(1 − e L ) − T ∗ H(t)(1 − e− L t ).
                                                                t
                                                                      L
   Or pour tout t ≥ 0
                                                Z +∞
                                       R                           R                 R
                      T ∗ H(t)(1 − e− L t ) =            H(x)e− L x H(t − x)(1 − e− L (t−x) )dx
                                                 −∞
                                                Z t
                                                          R            R
                                            =          e− L x (1 − e− L (t−x) )dx
                                                Z0 t
                                                          R        R
                                            =          e− L x − e− L t dx
                                                 0
                                                L   R             R
                                            = − [e− L x ]t0 − te− L t
                                                R
                                              L        R            R
                                            = (1 − e− L t ) − te− L t .
                                              R
                                                                   R
   Le signal de sortie correspondant à E(t) = H(t)(1 − e− L t ) est donc
                                                           R    R
                                                S(t) = H(t) te− L t .
                                                           L




                                                                                                   Fin.




                                                          6
~~~
