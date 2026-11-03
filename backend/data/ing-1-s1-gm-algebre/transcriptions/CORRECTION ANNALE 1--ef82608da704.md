# CORRECTION ANNALE 1.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Vw-mVOotb4oJoUxgnnNjgDRoR5EMpyk6) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
          Corrigé Annale 1 - Algèbre Linéaire Appliquée
                             ING1 Mathématiques - CY Tech




Exercice 1 : Normes vectorielles et matricielles (5 points)
Soit le vecteur x = (2, −1, 3, −4)T ∈ R4 .

1. Calcul des normes de x (1,5 point)

                ∥x∥1 = |2| + | − 1| + |3| + | − 4| = 2 + 1 + 3 + 4 = 10
                       p                                √               √
                ∥x∥2 = 22 + (−1)2 + 32 + (−4)2 = 4 + 1 + 9 + 16 = 30 ≈ 5, 477
               ∥x∥∞ = max(|2|, | − 1|, |3|, | − 4|) = 4

2.a. Calcul des normes de A (1,5 point)
                 
           1 −2 3
Pour A =  2  0 −1 :
          −1 4  2
   Norme 1 (maximum des sommes colonnes) :
    Colonne 1 : |1| + |2| + | − 1| = 4

    Colonne 2 : | − 2| + |0| + |4| = 6

    Colonne 3 : |3| + | − 1| + |2| = 6

                                              ∥A∥1 = max(4, 6, 6) = 6
   Norme innie (maximum des sommes lignes) :
    Ligne 1 : |1| + | − 2| + |3| = 6

    Ligne 2 : |2| + |0| + | − 1| = 3

    Ligne 3 : | − 1| + |4| + |2| = 7

                                             ∥A∥∞ = max(6, 3, 7) = 7
   Norme de Frobenius :
                  sX
                                    √                                          √         √
         ∥A∥F =            a2ij =       1 + 4 + 9 + 4 + 0 + 1 + 1 + 16 + 4 =       40 = 2 10 ≈ 6, 325
                     i,j




                                                         1
~~~

## Page 2

~~~text
2.b. Vérication ∥A∥1 = ∥AT ∥∞ (1 point)
                                                          
                                                    1  2 −1
                                              AT = −2 0 4
                                                    3 −1 2
   Sommes lignes de AT :
    Ligne 1 : |1| + |2| + | − 1| = 4

    Ligne 2 : | − 2| + |0| + |4| = 6

    Ligne 3 : |3| + | − 1| + |2| = 6


                                 ∥AT ∥∞ = max(4, 6, 6) = 6 = ∥A∥1              ✓
   La propriété est bien vériée.

2.c. Vérication inégalité (1 point)
Pour x = (1, 1, 1)T :                             
                                         1 −2 3     1   2
                                  Ax =  2  0 −1  1 = 1
                                                      
                                         −1 4 2     1   5

                                        ∥Ax∥∞ = max(|2|, |1|, |5|) = 5
                                          ∥A∥∞ · ∥x∥∞ = 7 × 1 = 7
   On a bien : 5 ≤ 7 ✓

Exercice 2 : Méthode du point xe (5 points)
Équation : x3 − 2x − 5 = 0 sur [2, 3]

1. Existence et unicité (0,5 point)
Soit f (x) = x3 − 2x − 5.
    Existence : f continue sur [2, 3] et :
    f (2) = 8 − 4 − 5 = −1 < 0

    f (3) = 27 − 6 − 5 = 16 > 0

Par le théorème des valeurs intermédiaires, ∃x∗ ∈ [2, 3] tel que f (x∗ ) = 0.
   Unicité : f ′ (x) = 3x2 − 2 > 0 pour x ∈ [2, 3] donc f strictement croissante ⇒ solution unique.

2.a. Étude des dérivées (1,5 point)
               √
Pour g1 (x) = 3 2x + 5 :
                                        1                        2
                               g1′ (x) = (2x + 5)−2/3 · 2 =
                                        3                   3(2x + 5)2/3
   Pour x ∈ [2, 3] : 2x + 5 ∈ [9, 11]
                                                                
                                                  2         2
                              g1′ (x) ∈                ,           ≈ [0, 141; 0, 165]
                                              3 · 112/3 3 · 92/3

   Donc |g1′ (x)| < 1 sur [2, 3] ⇒ Convergence garantie


                                                           2
~~~

## Page 3

~~~text
   Pour g2 (x) = x 2−5 :
                    3


                                                                      3x2
                                                          g2′ (x) =
                                                                       2
   Pour x ∈ [2, 3] : g2′ (x) ∈ [6, 13, 5]
   Donc |g2′ (x)| >q1 sur [2, 3] ⇒ Pas de convergence
   Pour g3 (x) =        x3 −5
                          2     :
                                                         1      3x2    3x2
                                             g3′ (x) = q      ·     = q
                                                           3
                                                      2 x 2−5    2       3
                                                                     4 x 2−5

   Pour x = 2, 5 : g3′ (2, 5) =       3·6,25
                                      q          18,75
                                              ≈ 4·2,304 ≈ 2, 04 > 1
                                     4 10,625
                                           2
   Donc |g3′ (x)| > 1 ⇒ Pas de convergence

2.b. Conclusion (1 point)
Seule la fonction g1 permet la convergence de la méthode du point xe.

2.c. Deux itérations avec g1 (1 point)
Avec x0 = 2, 5 :
                                                     p               √
                                                                     3
                                    x1 = g1 (2, 5) = 3 2 · 2, 5 + 5 = 10 ≈ 2, 154

                                               p                  p
                            x2 = g1 (2, 154) = 3 2 · 2, 154 + 5 = 3 9, 308 ≈ 2, 104

2.d. Vitesse de convergence (1 point)
On a calculé que g1′ (x∗ ) ̸= 0 (environ 0,15 près de la solution).
   Donc la convergence est linéaire avec taux de convergence ≈ |g1′ (x∗ )| ≈ 0, 15.

Exercice 3 : Conditionnement (4 points)
             
    4 1
A=
    1 3
         , b = 54

1. Calcul de A−1 (1 point)
                                                det(A) = 4 · 3 − 1 · 1 = 11

                                                                        
                                        −1     1        3 −1     3/11 −1/11
                                    A        =                =
                                               11       −1 4    −1/11 4/11

2. Conditionnement (1 point)
                                ∥A∥∞ = max(|4| + |1|, |1| + |3|) = max(5, 4) = 5

                                     1                                     1             5
                   ∥A−1 ∥∞ =            max(|3| + | − 1|, | − 1| + |4|) =    max(4, 5) =
                                     11                                   11             11

                                                                5   25
                                              κ∞ (A) = 5 ×        =    ≈ 2, 27
                                                               11   11
   Le système est bien conditionné (κ proche de 1).


                                                                3
~~~

## Page 4

~~~text
3. Nouvelle solution avec perturbation (1 point)
             
             5, 1
Avec b′ =         :
             3, 9
                                                                                 
                       ′       −1 ′      3/11 −1/11    5, 1         (15, 3 − 3, 9)/11
                      x =A       b =                          =
                                        −1/11 4/11     3, 9       (−5, 1 + 15, 6)/11
                                                                
                                           ′  11, 4/11      1, 0364
                                         x =           =
                                              10, 5/11      0, 9545
   Erreur relative :
                           ∥x′ − x∥∞   max(|0, 0364|, |0, 0455|)
                                     =                           = 0, 0455 ≈ 4, 55%
                             ∥x∥∞                 1

4. Borne théorique (1 point)
Perturbation relative sur b :
                             ∥b′ − b∥∞   max(|0, 1|, | − 0, 1|)   0, 1
                                       =                        =      = 0, 02 = 2%
                               ∥b∥∞               5                5

   Borne théorique :
                           ∥∆x∥∞            ∥∆b∥∞   25
                                 ≤ κ∞ (A) ·       =    × 0, 02 ≈ 0, 0455 = 4, 55%
                            ∥x∥∞             ∥b∥∞   11

   L'erreur réelle (4,55%) est exactement égale à la borne théorique, ce qui conrme l'analyse.

Exercice 4 : Factorisation LU (6 points)
                 
      2 1 1        4
A =  4 1 0, b = 5
     −2 2 1        1

1. Existence factorisation LU (1 point)
Calcul des mineurs principaux :
    M1 = a11 = 2 ̸= 0 ✓
                   
               2 1
    M2 = det          = 2 − 4 = −2 ̸= 0 ✓
               4 1

    M3 = det(A) = 2(1 − 0) − 1(4 − 0) + 1(8 + 2) = 2 − 4 + 10 = 8 ̸= 0 ✓

   Tous les mineurs principaux sont non nuls ⇒ A admet une factorisation LU.

2. Factorisation A = LU (3 points)
Initialisation :                                                        
                                           2 1 1                 1   0   0
                                      U = 0 · ·  ,    L = l21     1   0
                                           0 · ·             l31 l32     1
   Étape 1 : Première colonne de L
                                                      a21  4
                                              l21 =       = =2
                                                      u11  2


                                                       4
~~~

## Page 5

~~~text
                                                 a31   −2
                                         l31 =       =    = −1
                                                 u11    2
  Étape 2 : Deuxième ligne de U
                                 u22 = a22 − l21 u12 = 1 − 2 · 1 = −1
                                 u23 = a23 − l21 u13 = 0 − 2 · 1 = −2
  Étape 3 : Deuxième colonne de L
                                 a32 − l31 u12   2 − (−1) · 1   3
                         l32 =                 =              =    = −3
                                     u22             −1         −1
  Étape 4 : Troisième ligne de U
           u33 = a33 − l31 u13 − l32 u23 = 1 − (−1) · 1 − (−3) · (−2) = 1 + 1 − 6 = −4
  Résultat :                                                     
                              1 0 0                          2 1  1
                          L= 2 1 0 ,                  U = 0 −1 −2
                             −1 −3 1                         0 0 −4

3. Résolution Ly = b (1 point)
                                                
                                       1  0 0     y1    4
                                     2   1 0   y2 = 5
                                                      
                                      −1 −3 1     y3    1
  Descente :
                          y1 = 4
                          y2 = 5 − 2y1 = 5 − 8 = −3
                          y3 = 1 − (−1)y1 − (−3)y2 = 1 + 4 − 9 = −4

                                                       
                                                      4
                                                 y = −3
                                                      −4

4. Résolution U x = y (1 point)
                                            
                                   2 1  1    x1      4
                                  0 −1 −2 x2  = −3
                                   0 0 −4    x3      −4
  Remontée :
                                      −4
                                 x3 =    =1
                                      −4
                                      −3 − (−2) · 1   −3 + 2
                                 x2 =               =        =1
                                          −1            −1
                                      4−1·1−1·1        2
                                 x1 =                = =1
                                            2          2
                                                     
                                                      1
                                                 x = 1
                                                    
                                                      1

                            Fin du corrigé - Note totale : /20

                                                    5
~~~
