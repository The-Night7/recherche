# CM5-Mesures-produit_Mesures-et-integration.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1F_H50-EJRQTIJMGrPS1PZ0W4cPhpIXEL) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Ingénieurs 1ère année : Mathématiques appliquées

            Mesure et intégration




           CM5 – Mesures produit

          Nisrine FORTIN CAMDAVANT
~~~

## Page 2

~~~text
1   Produit de tribus
      Pavé mesurable
      Projection canonique et fonctions mesurables


2   Mesure produit
     Mesure σ-finie
     Mesure produit


3   Théorème de Fubini


4   Fonctions à variables séparées
~~~

## Page 3

~~~text
  Produit de tribus         Mesure produit         Théorème de Fubini   Fonctions à variables séparées



  Introduction




         (Ω1 , T1 , µ) et (Ω2 , T2 , ν) deux espaces mesurés.


                Étant donnés deux ensembles mesurables A et B respectivement dans Ω1
                et Ω2 , on a en pratique

                                       mesure (A × B) = µ(A) × ν(B).

                La théorie de la mesure nous donne ce résultat.


                Le théorème de Fubini nous permettra d’intégrer par rapport à une
                mesure produit et facilitera le calcul des intégrales multiples.




3/18
~~~

## Page 4

~~~text
  Produit de tribus         Mesure produit         Théorème de Fubini    Fonctions à variables séparées



  Pavé mesurable



          Soient (Ω1 , T1 ) et (Ω2 , T2 ) deux espaces mesurables.

          Définition
          On appelle pavé mesurable tout ensemble A1 × A2 avec Ai ∈ Ti , i ∈ {1, 2}.

          Remarque : Le complémentaire d’un pavé peut s’écrire comme une union finie
          de pavés :
                                                                                
       (Ω1 × Ω2 )\(A1 × A2 ) = (Ω1 \ A1 )×(Ω2 \ A2 ) ∪ (Ω1 \ A1 )×Ω2 ∪ Ω1 ×(Ω2 \ A2 ) .



          Proposition
          Une union finie de pavés mesurables est égale à une union finie de pavés
          mesurables disjoints.




4/18
~~~

## Page 5

~~~text
  Produit de tribus        Mesure produit           Théorème de Fubini    Fonctions à variables séparées



  Tribu produit


         On appelle tribu produit de T1 par T2 la tribu de parties de Ω1 × Ω2
         engendrée par les pavés mesurables de Ω1 × Ω2 . On la note T1 ⊗ T2 .
                                                                    
                     T1 ⊗ T2 := σ {A1 × A2 ; A1 ∈ T1 , A2 ∈ T2 }

         Remarques
         ::::::::::
                    :
             Le produit de deux tribus n’est pas commutatif. La tribu T1 ⊗ T2 n’est pas
             en général égale à T2 ⊗ T1 , tout simplement parce que le produit cartésien
             n’est pas commutatif :
                                            Ω1 × Ω2 ̸= Ω2 × Ω1 .
                Par conséquent le produit de deux mesures que nous allons définir sur
                T1 ⊗ T2 ne sera pas non plus commutatif.
                B R2 = B (R) ⊗ B (R). Par récurrence, on peut démontrer à partir du
                      

                résultat précédent que pour tout n ∈ N∗
                                        B (Rn ) = B (R) ⊗ . . . ⊗ B (R)
                                                  |        {z         }
                                                           n fois

5/18
~~~

## Page 6

~~~text
  Produit de tribus        Mesure produit             Théorème de Fubini   Fonctions à variables séparées



  Projection canonique et coupe




         Pour i = 1, 2, l’application

                                        πi   :   Ω1 × Ω2      →     Ωi
                                                 (x1 , x2 )   7 →   xi

         est appelée la projection canonique sur Ωi .

         La fonction g : Y → Ω1 × Ω2 est (F, T1 ⊗ T2 )-mesurable si et seulement si
         ∀i ∈ {1, 2}, πi ◦ g est (F, Ti )-mesurable.




6/18
~~~

## Page 7

~~~text
  Produit de tribus           Mesure produit              Théorème de Fubini     Fonctions à variables séparées



  Proposition


         Si A ∈ T1 ⊗ T2 et si x1 ∈ Ω1 , on appelle coupe de A par rapport à x1 , notée
         Ax1 , l’ensemble                                  
                                               x2 ∈ Ω2 , (x1 , x2 ) ∈ A .
                                   
         On a Ax1 = π2 A ∩ {x1 } × Ω2 .


         Soient (Ω1 , T1 ), (Ω2 , T2 ) et (Ω3 , T3 ) trois espaces mesurables.


            1   Si A ∈ T1 ⊗ T2 alors Ax1 ∈ T2 pour tout x1 ∈ Ω1 .


            2   Si f : Ω1 × Ω2 → Ω3 est (T1 ⊗ T2 , T3 )-mesurable, alors

                      ∀x2 ∈ Ω2 , x1 7→ f (x1 , x2 ) est (T1 , T3 )-mesurable.

                      ∀x1 ∈ Ω1 , x2 7→ f (x1 , x2 ) est (T2 , T3 )-mesurable.

7/18
~~~

## Page 8

~~~text
  Produit de tribus        Mesure produit       Théorème de Fubini      Fonctions à variables séparées



  Mesure σ-finie




         Définition
         Soit (Ω, T ) un espace mesurable, µ : T → [0, +∞] une mesure positive, on dit
         que µ est σ-finie, si
                                                       S
                                   n n∈N ⊂ T telle que
           1 il existe une suite (A )                    An = X ,
                                                         n∈N
            2   µ(An ) < +∞, pour tout n ∈ N.


         Remarque
           • Une mesure σ-finie peut être de masse totale infinie, par exemple la
                mesure de Lebesgue.
             • La mesure de Lebesgue sur R et la mesure de comptage sur N sont
               σ-finies.




8/18
~~~

## Page 9

~~~text
  Produit de tribus           Mesure produit       Théorème de Fubini         Fonctions à variables séparées



  Théorème et mesure produit



         Soient (Ω1 , T1 , µ1 ) et (Ω2 , T2 , µ2 ) deux espaces mesurés et µ1 et µ2 σ-finies
         alors
                il existe une mesure unique µ sur T1 ⊗ T2 telle que :

                        ∀A1 ∈ T1 , ∀A2 ∈ T2 , µ (A1 × A2 ) = µ1 (A1 ) × µ2 (A2 ) .

                µ est une mesure σ-finie
                x1 7→ µ2 (Ax1 ) est T1 -mesurable pour tout A ∈ T1 ⊗ T2
                        Z
                µ(A) =      µ2 (Ax1 ) dµ1 (x1 ).
                         Ω1


         Définition
         µ est la mesure produit de µ1 par µ2 et on la note µ1 ⊗ µ2 .




9/18
~~~

## Page 10

~~~text
  Produit de tribus          Mesure produit          Théorème de Fubini          Fonctions à variables séparées



  Remarques



            1   Si on a trois espaces mesurés (Ωi , Ti , µi ), i ∈ {1, 2, 3} avec µi σ-finies
                alors on a l’associativité du produit

                                        µ1 ⊗ µ2 ⊗ µ3 = µ1 ⊗ (µ2 ⊗ µ3 ) .

                Comme on avait (T1 ⊗ T2 ) ⊗ T3 = T1 ⊗ (T2 ⊗ T3 ), on peut donc définir la
                mesure sur T1 ⊗ T2 ⊗ T3 comme l’unique mesure µ sur ce produit de
                tribus telle que

                µ (A1 × A2 × A3 ) = µ(A1 )×µ(A2 )×µ(A3 )           avec   Ai ∈ Ti , i ∈ {1, 2, 3} .

                Idem avec n facteurs (n ∈ N∗ ) (par récurrence).
            2   La mesure de Lebesgue sur R2 est le produit des mesures de Lebesgue sur
                (R, B(R)).
                La mesure de Lebesgue sur Rn (n ∈ N∗ ) est le produit des mesures de
                Lebesgue sur chaque facteur.



10/18
~~~

## Page 11

~~~text
  Produit de tribus           Mesure produit          Théorème de Fubini         Fonctions à variables séparées



  Intégration par rapport à une mesure produit


         Soient (Ω1 , T1 , µ1 ) et (Ω2 , T2 , µ2 ) deux espaces mesurés et µ1 et µ2 σ-finies et
         µ = µ1 ⊗ µ2 .


                L’intégration d’une fonction numérique définie sur T1 ⊗ T2 par rapport à
                la mesure µ est précisée par les deux théorèmes ci-dessous.


                Le premier traite le cas d’une fonction positive, connu sous le nom du
                théorème de Fubini-Tonelli ;


                le deuxième traite le cas d’une fonction de signe quelconque, connu sous
                le nom du théorème de Fubini.


                Attention.
                 Dans la suite, on considère (Ω1 , T1 , µ1 ) et (Ω2 , T2 , µ2 ) deux espaces mesurés
                 et µ1 et µ2 σ-finies et µ = µ1 ⊗ µ2 .


11/18
~~~

## Page 12

~~~text
  Produit de tribus              Mesure produit                  Théorème de Fubini             Fonctions à variables séparées



  Théorème de Fubini-Tonelli




                Théorème de Fubini-Tonelli.
                 Si f : Ω1 × Ω2 → [0, +∞] est T1 ⊗ T2 -mesurable, alors


                      1   Les fonctions φ et ψ définies respectivement sur Ω1 et Ω2 par
                                    Z                                      Z
                          φ : x1 7→    f (x1 , x2 ) dµ2 (x2 ) et ψ : x2 7→   f (x1 , x2 ) dµ1 (x1 )
                                      Ω2                                                  Ω1

                          sont mesurables.
                      2
                           Z                      Z        Z                            
                                     fdµ   =                         f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 )
                            Ω1 ×Ω2                Ω1            Ω2

                                                  Z        Z                              
                                           =                         f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 ) .
                                                      Ω2        Ω1



12/18
~~~

## Page 13

~~~text
  Produit de tribus       Mesure produit        Théorème de Fubini       Fonctions à variables séparées



  Commentaire




         Ce théorème nous permet entre autres de calculer des intégrales multiples par
         intégrations successives dans l’ordre que l’on désire avec la seule hypothèse f
         mesurable et positive.




13/18
~~~

## Page 14

~~~text
  Produit de tribus               Mesure produit                 Théorème de Fubini           Fonctions à variables séparées




           Théorème de Fubini (1).
           Soit f : Ω1 × Ω2 → R une fonction µ-intégrable, alors
               1          • ∀x1 ∈ Ω1 p.p, la fonction x2 7→ f (x1 , x2 ) est intégrable sur Ω2 .
                          • La fonction φ définie p.p sur Ω1 par
                                                           Z
                                                 φ : x1 7→     f (x1 , x2 ) dµ2 (x2 )
                                                                      Ω2

                            est µ1 -intégrable sur Ω1 .
               2          • Pour p.p x2 ∈ Ω2 , la fonction x1 7→ f (x1 , x2 ) est intégrable sur Ω1 .
                          • La fonction ψ définie p.p sur Ω2 par
                                                           Z
                                                 ψ : x2 7→     f (x1 , x2 ) dµ1 (x1 )
                                                                      Ω1

                            est µ2 -intégrable sur Ω2 .
                      Z                    Z Z                             
               3
                                fdµ =                 f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 )
                      Ω1 ×Ω2                   Ω1        Ω2

                                             Z      Z                              
                                        =                     f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 ) .
                                               Ω2        Ω1

14/18
~~~

## Page 15

~~~text
  Produit de tribus        Mesure produit                 Théorème de Fubini          Fonctions à variables séparées




           Théorème de Fubini (2).
           Si l’une des trois intégrales suivantes
                                       Z
                              I1 =              f dµ
                                            Ω1 ×Ω2

                                        Z        Z                             
                             I2   =                       f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 )
                                            Ω1       Ω2

                                        Z        Z                             
                             I3   =                       f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 )
                                            Ω2       Ω1

           est finie alors il en est de même pour les deux autres, f est intégrable et
            Z Z                                          Z Z                       
                        f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 ) =      f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 ) .
               Ω1     Ω2                                          Ω2     Ω1




15/18
~~~

## Page 16

~~~text
  Produit de tribus          Mesure produit         Théorème de Fubini         Fonctions à variables séparées



  Mode d’emploi et mise en garde

            1   Pour prouver que f est intégrable sur T1 ⊗ T2 , on applique le théorème de
                Fubini-Tonelli à |f | qui affirme que I1 , I2 et I3 sont égales (qu’elles soient
                finies ou non), puis montrer que I2 ou I3 est finie. Souvent, l’une d’elles
                est facile à estimer.

            2   Bien distinguer le cas f mesurable positive où les trois intégrales I1 , I2 et
                I3 ont toujours un sens (valeur finie ou infinie) du cas où f est de signe
                variable pour lequel les intégrales
                              Z Z                       Z Z           
                                         fdµ2 dµ1 et                fdµ1 dµ2
                                Ω1     Ω2                     Ω2     Ω1

                peuvent ne pas exister, ou bien peuvent exister avec des valeurs finies ou
                infinies distinctes ou égales, sans que f soit intégrable. Autrement dit, si f
                est en général mesurable mais pas intégrable, les expressions
                               Z Z                       Z Z           
                                         fdµ2 dµ1 et                 fdµ1 dµ2
                                Ω1     Ω2                     Ω2     Ω1

                peuvent exister mais avoir des valeurs différentes.
16/18
~~~

## Page 17

~~~text
  Produit de tribus      Mesure produit            Théorème de Fubini             Fonctions à variables séparées



  Fonctions à variables séparées




         Si f1 et f2 sont deux fonctions mesurables positives (ou intégrables),
         définies respectivement sur Ω1 et Ω2 . On pose

                                   f (x1 , x2 ) = f1 (x1 ) × f2 (x2 ).

         Alors f est T1 ⊗ T2 -mesurable et
                     Z                      Z                      Z            
                            fd (µ1 × µ2 ) =               f1 dµ1              f2 dµ2 .
                      Ω1 ×Ω2                         Ω1                  Ω2




17/18
~~~

## Page 18

~~~text
  Produit de tribus         Mesure produit         Théorème de Fubini        Fonctions à variables séparées



  Remarques sur les hypothèses des théorèmes de Fubini-Tonelli et Fubini




         Les théorèmes de Fubini-Tonelli et Fubini cessent d’être vrais si
                on supprime l’hypothèse de σ-finitude d’une des mesures µ1 et µ2 . (Voir
                TD5.)


                dans le théorème de Fubini, si les valeurs des deux intégrales I1 et I2 sont
                distinctes, on peut déduire que la fonction f n’est pas µ1 ⊗ µ2 -intégrable
                (Voir TD5.)


                en revanche, si les valeurs des deux intégrales I1 et I2 sont égales, on ne
                peut pas déduire directement que la fonction f est µ1 ⊗ µ2 -intégrable
                (Voir TD5.)




18/18
~~~
