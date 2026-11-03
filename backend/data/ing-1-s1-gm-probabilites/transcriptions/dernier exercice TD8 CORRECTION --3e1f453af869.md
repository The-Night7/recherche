# dernier exercice TD8 CORRECTION .pdf

[Ouvrir l’original](https://drive.google.com/open?id=1VfWEupbw6n2o1PC_HuNcWqihMp_iyfeG) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
     Correction Détaillée - Vecteurs Gaussiens et
              Espérance Conditionnelle
                                   Probabilités Avancées


Exercice 2 (Examen 2017)
Énoncé : Soit U = (X, Y )′ un vecteur aléatoire
                                                gaussien de loi N2 (m, K) où m = (0, 0)′ et la
                                 1 1/2
matrice de covariance est K =              . On pose W = X et Z = 2X − Y .
                                1/2 1




1. Trouver la loi du vecteur (W, Z)′ .
Méthode : Le vecteur (W, Z)′ est une transformation linéaire du vecteur gaussien (X, Y )′ .
Toute transformation linéaire d’un vecteur gaussien reste un vecteur gaussien. Il suffit de cal-
culer son espérance et sa matrice de covariance.                              
                                                                     W            X
    — Écriture matricielle : On cherche A déterministe telle que          =A          . Comme
                                                                      Z           Y
       W = 1 · X + 0 · Y et Z = 2 · X − 1 · Y , on a :
                                                       
                                                   1 0
                                            A=
                                                   2 −1

   — Espérance : E[(W, Z)′ ] = AE[(X, Y )′ ] = A · (0, 0)′ = (0, 0)′ . Le vecteur est centré.
   — Matrice de covariance K̄ : La formule du cours donne K̄ = AKA′ . Détaillons le
     calcul matriciel :


                                                 1 × 1 + 0 1 × 12 + 0
                                                                           
                       1 0          1 1/2                                    1 1/2
              AK =                          =                            =
                       2 −1      1/2 1           2 × 1 − 21 2 × 12 − 1      3/2 0
                                            
                                  ′     1 2
          Puis on multiplie par A =            :
                                        0 −1

                                                            1 2 − 12
                                                                          
                            ′        1 1/2    1 2                           1 3/2
                K̄ = (AK)A =                           = 3              =
                                  3/2 0       0 −1          2
                                                               3+0         3/2 3

   Conclusion
                                                                    
                    ′                                         0    1 3/2
   Le couple (W, Z) suit la loi normale bidimensionnelle N2     ,         .
                                                              0   3/2 3




                                               1
~~~

## Page 2

~~~text
2. Exprimer Y en fonction de W et Z.
   Nous avons le système :              (
                                         W =X
                                         Z = 2X − Y
De la première ligne, X = W . En remplaçant dans la seconde : Z = 2W −Y ⇐⇒ Y = 2W −Z.


                                          Y = 2W − Z


3. Montrer que E[X 2 Y |(2X − Y )] existe et la calculer.
A. Existence
   (Rappel : Pour qu’une espérance conditionnelle existe, il suffit que la variable
aléatoire soit intégrable (L1 ).) Ici, les variables sont gaussiennes. Une variable gaussienne
admet des moments de tout ordre (car sa densité décroît exponentiellement vite à l’infini).
Ainsi, E[X 4 ] < +∞ et E[Y 2 ] < +∞. Par l’inégalité de Cauchy-Schwarz :
                                 p          p         p
                   E[|X 2 Y |] ≤ E[(X 2 )2 ] E[Y 2 ] = E[X 4 ]E[Y 2 ] < +∞

La variable X 2 Y est intégrable, donc l’espérance conditionnelle existe.

B. Calcul via la méthode de la densité conditionnelle
   On cherche à calculer E = E[X 2 Y | 2X − Y ]. En utilisant les nouvelles variables W = X et
Z = 2X − Y (donc Y = 2W − Z) :

                                    E = E[W 2 (2W − Z) | Z]

Par linéarité de l’espérance conditionnelle :

                                 E = 2E[W 3 | Z] − E[W 2 Z | Z]

Puisque Z est mesurable par rapport à la tribu σ(Z) (on dit que Z est "connue" sachant Z),
on peut la sortir de l’espérance :

                                 E = 2E[W 3 | Z] − ZE[W 2 | Z]

Objectif : Il faut trouver la loi de W sachant Z (la loi conditionnelle) pour calculer ces moments
conditionnels.

Étape 1 : Inversion de la matrice de covariance K̄
                                 3 3       9 12 − 9   3
                                   × =3− =
                      det(K̄) = 1 × 3 −             = ̸= 0
                                 2 2       4    4     4
                                                          
                  −1  1   3   −3/2    4   3  −3/2       4 −2
                K̄ =                =               =
                     3/4 −3/2  1      3 −3/2  1         −2 4/3

Étape 2 : Écriture de la densité conjointe f(W,Z)
                                                        
                                   1              1  −1 w
                 f(W,Z) (w, z) = p         exp − w z K̄
                                2π det(K̄)        2      z

                                                2
~~~

## Page 3

~~~text
                                                                  
                                     1          1     2         4 2
                f(W,Z) (w, z) = p         exp − 4w − 2wz − 2zw + z
                                 2π 3/4         2               3
                                                             
                                        1         1         4
                      f(W,Z) (w, z) = √ exp − 4w2 − 4wz + z 2
                                       π 3        2         3

Étape 3 : Factorisation (La "forme canonique") Pour trouver la loi conditionnelle, on
doit faire apparaître une structure du type "carré en w" plus un "reste en z". On complète le
carré pour la variable w dans l’exponentielle :

                                  4w2 − 4wz = (2w − z)2 − z 2

Donc l’argument de l’exponentielle devient :
                            4                       4                 1
                 4w2 − 4wz + z 2 = (2w − z)2 − z 2 + z 2 = (2w − z)2 + z 2
                            3                       3                 3
                                                                  2
On veut faire apparaître la forme d’une gaussienne (w−moyenne)
                                                     variance
                                                               .

                                     2              (w − z/2)2
                                                           2
                            (2w − z) = 4(w − z/2) =
                                                       1/4
                                          1 2 z2
                                            z =
                                          3        3
   On peut donc réécrire la densité conjointe comme un produit :
                                              (w − z/2)2                     z2
                                                                             
                              1                                1
         f(W,Z) (w, z) = p            exp −                ×√        exp −
                           2π · (1/4)          2 · (1/4)      2π · 3        2·3
                         |              {z               } |           {z       }
                                         fW |Z (w,z)                      fZ (z)


   Interprétation
   Cette factorisation prouve deux choses :
       1. Z ∼ N (0, 3) (c’est la densité marginale, le terme en rouge).
       2. La loi conditionnelle de W sachant Z = z est une loi Normale :
                                                            
                                                         z 1
                                     L(W |Z = z) = N      ,
                                                         2 4

   Cela signifie que l’on peut écrire : W = Z2 + 12 X̃ avec X̃ ∼ N (0, 1) indépendante de Z.


Étape 4 : Calcul des espérances conditionnelles Utilisons la représentation W = z2 + 12 X̃
(où X̃ ∼ N (0, 1)) pour calculer les moments.
   — Calcul de E[W 2 |Z = z] :
                                "         2 #     2           
                                    z 1             z   2z   1 2
                              E       + X̃      =E     + X̃ + X̃
                                    2 2              4   4   4

      Par linéarité, et sachant que E[X̃] = 0 et E[X̃ 2 ] = 1 :
                                             z2      1 1
                                         =      + 0 + = (z 2 + 1)
                                             4       4 4
                                                       3
~~~

## Page 4

~~~text
   — Calcul de E[W 3 |Z = z] :
                                      "           3 #
                                           z 1             1 h          i
                                  E         + X̃          = E (z + X̃)3
                                           2 2             8

                                    1 h 3    2          2     3
                                                                i
                                   = E z + 3z X̃ + 3z X̃ + X̃
                                    8
      Sachant que E[X̃] = 0, E[X̃ 2 ] = 1, et E[X̃ 3 ] = 0 (car loi symétrique centrée) :
                          1                       1            z
                         = (z 3 + 0 + 3z(1) + 0) = (z 3 + 3z) = (z 2 + 3)
                          8                       8            8

Étape 5 : Conclusion finale On remplace ces résultats dans notre expression de départ :

                        E[X 2 Y | 2X − Y ] = 2E[W 3 | Z] − ZE[W 2 | Z]

En remplaçant par les variables aléatoires (on remplace petit z par grand Z) :
                                                             
                                    Z 2               1 2
                              =2      (Z + 3) − Z (Z + 1)
                                    8                 4
                                Z              Z
                              = (Z 2 + 3) − (Z 2 + 1)
                                 4             4
                                Z 2
                                    (Z + 3) − (Z 2 + 1)
                                                        
                              =
                                 4
                                Z
                              = [2]
                                 4
                                Z
                              =
                                 2
   Comme Z = 2X − Y , on obtient finalement :

   Résultat Final
                                                       2X − Y     Y
                            E[X 2 Y | 2X − Y ] =              =X−
                                                         2        2




                                                   4
~~~
