# CM2 -- Conditions d_optimalité.pdf

[Ouvrir l’original](https://drive.google.com/open?id=169VXAbCOUNBWf2JszTOBWJwwuZScatl3) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 3, 6.

## Page 1

~~~text
Ingénieurs 2ème année : Mathématiques et Informatique

   Méthodes itératives d’optimisation déterministe




           CM2 – Conditions d’optimalité
             Nisrine FORTIN CAMDAVANT
~~~

## Page 2

~~~text
1   Introduction et généralités


2   Théorèmes généraux d’existence


3   Unicité


4   Conditions nécessaires et suffisantes d’optimalité dans le cas sans
    contraintes
~~~

## Page 3

![Fac-similé de la page 3](../facsimiles/7dc572882d4ce22f5114081b.jpg)

~~~text
Introduction
~~~



## Page 4

~~~text
On peut scinder les conditions d’optimalité en deux catégories :

     Les conditions nécessaires : des propriétés, équations ou inéquations que
     vérifient les solutions du problème (P) ;


     Les conditions suffisantes : des propriétés qui assurent à un point d’être
     solution du problème (P).


Ces résultats ne peuvent pas toujours être appliqués directement pour résoudre
le problème (P),

 ↝ ils permettront en revanche de vérifier l’optimalité éventuelle d’un point x ∈ K,
  ↝ de calculer analytiquement des solutions du problème (P) ou
  ↝ de définir des tests d’arrêts des itérations dans des algorithmes de résolution.
~~~

## Page 5

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




                Articulation du cours
                 On considère le problème d’optimisation

                                                       (PC) ∶ min f (x),
                                                                   x∈K

                 où K est l’ ensemble des contraintes considéré non vide.


                    ↝ On présentera deux résultats très généraux d’existence d’une
                      solution au problème (PC).


                    ↝ L’unicité sera vue dans le cadre de convexité.


                    ↝ On abordera les conditions nécessaire d’optimalité en l’absence
                      des contraintes.



5/22
~~~

## Page 6

![Fac-similé de la page 6](../facsimiles/bf45d55fc3e3d376ac2422b3.jpg)

~~~text
Théorèmes généraux d’existence
~~~

**Lecture OCR à contrôler**

~~~text
Théorémes généraux d'existence
~~~

## Page 7

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




              Cas où l’ensemble des contraintes est un compact de Rn

         Une partie K ⊂ Rn est dite un compact de Rn si K est un fermé de Rn et borné.
         Le résultat suivant sera admis.



                Théorème 1. Cas K compact
           Soit K un compact de Rn . Si f ∶ K → R est continue alors le problème (PC)
           admet une solution optimale x̂ ∈ K au sens de la définition suivante :

                                                   f (x̂) ≤ f (x), ∀x ∈ K.




7/22
~~~

## Page 8

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



                            Cas où l’ensemble des contraintes K = Rn


                Théorème 2. Cas K = Rn
           Soit f ∶ Rn → R une fonction continue. Si

                                                        lim f (x) = +∞
                                                     ∥x∥→+∞


           alors le problème (PSC) admet une solution optimale.

         Démonstration. Admise
         ::::::::::::




8/22
~~~

## Page 9

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



                   Cas où l’ensemble des contraintes K est un convexe


                Théorème 3. Condition nécessaire du premier ordre et convexité
           Soit f ∶ Rn → R une application différentiable et K un sous-ensemble convexe
           de Rn . Si x ∗ un minimum local du problème (P) alors

                                             ∀x ∈ K, ⟨∇f (x ∗ ), x − x ∗ ⟩ ≥ 0.                                       (1)

         Démonstration.
         ::::::::::::




9/22
~~~

## Page 10

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



                   Cas où l’ensemble des contraintes K est un convexe


                Théorème 4. Condition suffisante du premier ordre et convexité
           Soit f ∶ Rn → R une application différentiable et convexe sur le convexe K,
           alors la condition (1) est suffisante pour que x ∗ soit un minimum global de f
           sur K.

         Démonstration.
         ::::::::::::




10/22
~~~

## Page 11

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



  Interprétation géométrique




         La condition ⟨∇f (x ∗ ), x − x ∗ ⟩ ≥ 0 s’interprète en disant que l’angle entre le
                                                                          π π
         vecteur ∇f (x ∗ ) et le vecteur x − x ∗ est dans l’intervalle [− ; ].
                                                                          2 2




11/22
~~~

## Page 12

~~~text
                            Unicité

L’unicité de la solution optimale résulte en général de propriétés de convexité
du critère f et l’ensemble des contraintes K.
~~~

## Page 13

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




                Théorème 5. Stricte convexité et unicité
           Soit f ∶ K → R une fonction strictement convexe sur le convexe K ⊂ Rn . Le
           minimum de f sur K, s’il existe, est unique.
         Démonstration.
         ::::::::::




13/22
~~~

## Page 14

~~~text
Conditions nécessaires et suffisantes d’optimalité
                      Cas sans contraintes


 On se place dans le cas où K = Rn . On considère le problème d’optimisation
 sans contraintes
                                     ⎧
                                     ⎪ min f (x)
                                     ⎪
                                     ⎪
                           (PSC) ⎨
                                     ⎪
                                     ⎪       n
                                     ⎩ x ∈R
                                     ⎪
~~~

## Page 15

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




         Définition 1. Point critique
         Soit f ∶ Rn → R une fonction différentiable sur Rn . Un point x ∗ de Rn vérifiant
         ∇f (x ∗ ) = 0 est appelé point critique.

         Exemples :
            1    Déterminer les points critiques de f, f (x, y ) = x 3 + y 3 − 3x − 3a2 y (a est un paramètre). f
                 est différentiable et le gradient de f vaut :

                                             →T
                                             Ð      ∂f ∂f        2       2    2
                                             ∇ f =(   ,   ) = (3x − 3, 3y − 3a )
                                                    ∂x ∂y

                            →T
                            Ð
                 L’équation ∇ f = 02 possède alors quatre solutions :

                                                 (1, a); (1, −a), (−1, a) et (−1, −a)

                 Quatre points stationnaires !
                                                                                →T
                                                                                Ð
             2   Soit f telle que f (x, y ) = x + y 2 . f est différentiable et ∇ f (x, y ) = (1, 2y ).
                 →T
                 Ð
                 ∇ f = 02 n’admet pas de solutions donc f ne possède pas de points critiques.




15/22
~~~

## Page 16

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




                Théorème 6.
           Soit f ∶ Rn → R une fonction différentiable et x̂ ∈ Rn vérifiant

                                                f (x̂) ≤ f (x), ∀x ∈ Rn

           alors on a nécessairement ∇f (x̂) = 0.

         Démonstration.
         ::::::::::




16/22
~~~

## Page 17

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa


         La condition ∇T f (x̂) = 0 devient suffisante dans le cas où la fonction f est
         convexe.

                Théorème 7. Condition nécessaire et suffisante
           Soit f ∶ Rn → R une fonction différentiable et convexe. Si x̂ est un point
           critique de f , alors on a

                                                ∀x ∈ Rn , f (x̂) ≤ f (x).
         Démonstration.
         ::::::::::




17/22
~~~

## Page 18

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




         Lorsque la fonction f n’est pas convexe, on ne peut donner qu’une condition
         nécessaire et suffisante d’optimalité locale.

         Définition 2. Minimum local
         On appellera x ∗ minimum local de f , s’il existe δ > 0 tel que pour tout x ∈ Rn ,

                                           ∥x − x ∗ ∥ ≤ δ Ô⇒ f (x ∗ ) ≤ f (x).



                Théorème 8.
           Soit f ∶ Rn → R une fonction deux fois différentiable au voisinage de x ∗ . Si

                                           ∇f (x ∗ ) = 0Rn et Hf (x ∗ ) > 0

           alors x ∗ est un minimum local local de f .




18/22
~~~

## Page 19

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa




                    Optimisation sans contraintes : en pratique
         Soit f une fonction définie sur un ouvert S ⊂ Rn et deux fois différentiable et
         soit Hf le hessien de f . Soit x ∗ un point critique de f alors :

            1   Si la matrice Hf est définie positive alors f est localement convexe en x ∗
                et x ∗ est un minimum local pour f .


            2   Si la matrice Hf est définie négative alors f est localement concave en x ∗
                et x ∗ est un maximum local pour f .


            3   Si Hf est non définie alors x ∗ est un point selle.


            4   Si Hf est semi-définie positive (ou négative) on n’a pas de conclusion, et
                une étude plus fine doit être réalisée.




19/22
~~~

## Page 20

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



  Optimisation sans contraintes



         Exemple
         Déterminer les valeurs optimales de

                                             f (x, y ) = x 3 + y 3 − 3x − 3a2 y

         (discussion selon le paramètre a).

                Le gradient de f vaut :

                                         →T
                                         Ð     ∂f ∂f
                                         ∇ f =( ,    ) = (3x 2 − 3, 3y 2 − 3a2 )
                                               ∂x ∂y
                             →T
                             Ð
                La condition ∇ f = 0 impose a2 ≥ 0, soit a ∈ R.
                L’équation possède alors quatre solutions :

                                             (1, a); (1, −a), (−1, a) et (−1, −a)

                Quatre points stationnaires !

20/22
~~~

## Page 21

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



  Optimisation sans contraintes




                La matrice hessienne de f est

                                               ⎛        ∂2f              ∂2f ⎞
                                               ⎜        ∂x 2            ∂y ∂x ⎟   6x               0
                                  2            ⎜                              ⎟
                                 ∇ f (x, y ) = ⎜                              ⎟=(                    )
                                               ⎜          2               2   ⎟    0              6y
                                               ⎜        ∂ f              ∂ f ⎟
                                               ⎝                              ⎠
                                                       ∂x∂y              ∂y 2
                Pour que la forme quadratique soit définie, il faut que xy ≥ 0.
                Bilan : un minimum, un maximum et deux “points selles”.




21/22
~~~

## Page 22

~~~text
  Introduction et généralités Théorèmes généraux d’existence Unicité Conditions nécessaires et suffisantes d’optimalité dans le cas sa



         Bibliographie :
                Méthodes numériques et optimisation, Jean Pierre Corriou, LAVOISIER
                2010
                Linear and Nonlinear Programming, David G.LUENBERGER, Second
                Edition Springer 2005
                Introduction à l’optimisation, Jean Christophe Culioli, ellipses,1994.
                Introduction à l’analyse numérique matricielle et à l’optimisation PG.
                CIARLET MASSON 1990
                Inverse Problem Theory and Methods for Model Parameter Estimation
                Albert Tarantola SIAM 2005.
                Convexité et optimisation Guy Cohen Ecole Nationale des Ponts et
                Chaussées et INRIA 2000.
                Optimisation sans contraintes M. Bergounioux http ://www.univ-
                orleans.fr/mapmo/membres/maitine/MASTER2/FAP/optimFAP.pdf
                Introduction à l’analyse numérique
                http ://www.math.uvsq.fr/jaisson/ENSAE cours45.pdf
                Algorithmes d’optimisation non-linéaire sans contrainte
                http ://www.math.u-bordeaux1.fr/ bergmann/PDF/These/annexeC.pdf

22/22
~~~
