# CM2-Groupes_2021-2022_Algebre2_P1S2_DCransac.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Z6ZtCMtsJLPIlRfPpBMahaTByGoyoBxw) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                  Lois de composition internes
                                                  Structure de groupe
                                    Groupe
                                                  Sous-groupes
                                                  Morphismes de groupes




       Dans tout ce chapitre, E est un ensemble.
       Dénition
       On appelle loi de composition interne sur E (lci) toute application de
       E × E dans E .
       Exemple
             R2
         
                     →     R
       p:
            (x, y ) 7→   x +y

       Dénition
       On appelle magma tout couple constitué d'un ensemble et d'une lci.

       Example
            (R, +) est un magma.
            (Z, −) est un magma.
            (N, −) n'est pas un magma : en eet 3 − 4 ∈
                                                      /N

1/45                                 D. Cransac       Analyse
~~~

## Page 2

~~~text
                                                      Lois de composition internes
                                                      Structure de groupe
                                         Groupe
                                                      Sous-groupes
                                                      Morphismes de groupes




       Dans toute la suite, ⋆ est une lci sur E .
       Dénition
       Soit (E , ⋆) un magma.
            On dit que E est associatif si pour tout x, y , z ∈ E , on a :

                                     x ⋆ (y ⋆ z) = (x ⋆ y ) ⋆ z

            L'élément x ⋆ (y ⋆ z) = (x ⋆ y ) ⋆ z est alors noté x ⋆ y ⋆ z .
            On dit que E est commutatif si pour tout x, y ∈ E , on a :

                                            x ⋆y =y ⋆x

            Soit ∗ une seconde lci sur E .
            On dit que dans E ⋆ est distributive par rapport à ∗ si pour tout
            x, y , z ∈ E , on a :
                 x ⋆ (y ∗ z) = (x ⋆ y ) ∗ (x ⋆ z)
                 (y ∗ z) ⋆ x = (y ⋆ x) ∗ (z ⋆ x).

2/45                                     D. Cransac       Analyse
~~~

## Page 3

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                      Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




       Remarque
       On dit que dans (E , ⋆) est distributive à gauche par rapport à ∗ si pour
       tout x, y , z ∈ E , on a :
                             x ⋆ (y ∗ z) = (x ⋆ y ) ∗ (x ⋆ z)

       De même, on a la notion de distributivité à droite.




3/45                                  D. Cransac       Analyse
~~~

## Page 4

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                      Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




       Example
        1   C, R, Q, Z, N avec + ou × sont associatifs, mais pas (Z, −) car
            1 − (2 − 3) ̸= (1 − 2) − 3.
        2   C, R, Q, Z, N avec + ou × sont commutatifs, mais pas (Z, −), ni
            (F (R, R), ◦).
        3   Sur C, R, Q, Z, N la loi de composition interne × est distributive par
            rapport à +.
        4   P(E ), ∩ et ∪ sont distributives l'une par rapport à l'autre.




4/45                                  D. Cransac       Analyse
~~~

## Page 5

~~~text
                                                  Lois de composition internes
                                                  Structure de groupe
                                    Groupe
                                                  Sous-groupes
                                                  Morphismes de groupes




       Dénition (Elément neutre)
       Soit e ∈ E .
       On dit que e est un élément neutre à gauche (resp. à droite) pour ⋆ si
       pour tout x ∈ E on a
                                      e ⋆x =x
       On dit que e est un élément neutre à droite (resp. à droite) pour ⋆ si
       pour tout x ∈ E on a
                                      x ⋆e =x
       On dit que e est un élément neutre pour ⋆ si c'est un élément neutre à
       gauche et à droite, i.e.

                              ∀x ∈ E , e ⋆ x = x ⋆ e = x




5/45                                 D. Cransac       Analyse
~~~

## Page 6

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                     Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




       Dénition (Elément inversible)
       Soit e un neutre pour ⋆ et soit x ∈ E .
            On dit que x est inversible à gauche s'il existe un élément y ∈ E
            tel que
                                           y ⋆x =e
           Un tel élément y s'appelle UN inverse à gauche x .
           On dit que x est inversible à droite s'il existe un élément y ∈ E tel
           que
                                           x ⋆y =e
           Un tel élément y s'appelle UN inverse à droite x .
           On dit que x est inversible s'il est inversible à gauche et à droite,
           i.e. il existe y ∈ E tel que

                                     y ⋆x =x ⋆y =e

           Dans ce cas y est UN inverse de x.

6/45                                  D. Cransac       Analyse
~~~

## Page 7

~~~text
                                                        Lois de composition internes
                                                        Structure de groupe
                                           Groupe
                                                        Sous-groupes
                                                        Morphismes de groupes




       Example
            0 est un élément neutre pour + dans R, C, Q, Z, N.
            1 est un élément neutre pour × dans R, C, Q.
            IdE est un élément neutre pour ◦ (composition) dans F (E , E ) et les
            bijections sont tous les éléments inversibles de cet ensemble.
       Remarque
        1   Être inversible seulement à gauche ou à droite ne sut pas pour être
            inversible tout court.       
                                              N →
                                                               (n
                                                                             N
            Soit f :             →                                         Si n pair
                                     2n et g : 
                           N         N
                           n   7 →              n 7→  2
                                                       0 Si n impair
            On a g ◦ f = Id pour tout h ∈ F (N, N), f ◦ h ̸= Id car 3 par
            exemple n'a pas d'antécédent par f ◦ h donc f ◦ h n'est pas l'identité.
        2   Un neutre est toujours inversible et est son propre inverse.
            En eet, par dénition du neutre, e ⋆ e = e ⋆ e = e
7/45                                       D. Cransac       Analyse
~~~

## Page 8

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




       Proposition
       Si ⋆ admet un neutre, alors ce neutre est unique.

       Démonstration.
       Soient e et e ′ deux neutres.
       Alors e ⋆ e ′ = e car e ′ est une neutre
       et e ⋆ e ′ = e ′ car e est un neutre.
       donc e = e ′ .




8/45                                    D. Cransac       Analyse
~~~

## Page 9

~~~text
                                                      Lois de composition internes
                                                      Structure de groupe
                                        Groupe
                                                      Sous-groupes
                                                      Morphismes de groupes




       Proposition
       On suppose la loi ⋆ associative, et admettant un neutre e .
       Si un élément est inversible, alors il a un seul inverse.

       Démonstration.
       Soient y et y ′ deux inverses de x ∈ E .
       Alors y ⋆ x = e et x ⋆ y ′ = e .
       Donc y ⋆ (x ⋆ y ′ ) = y ⋆ e = y et (y ⋆ x) ⋆ y ′ = e ⋆ y ′ = y ′ , d'où
       y = y ′.




9/45                                     D. Cransac       Analyse
~~~

## Page 10

~~~text
                                                        Lois de composition internes
                                                        Structure de groupe
                                          Groupe
                                                        Sous-groupes
                                                        Morphismes de groupes




        Remarque
        On utilise souvent les notations additives et multiplicatives.
          1 En notation additive, ⋆ est notée +
                  x + x + · · · + x (n−fois) se note nx .
                  Si x est inversible, son inverse se note −x . On l'appelle alors

                  l'opposé de x .

                  On notera le neutre d'une telle structure 0 ou 0E .

          2   En notation multiplicative, ⋆ est en général notée par × (et ce
              symbole est même souvent omis)
                  x × x × · · · × x (n−fois) se note x n
                                                             −1
                  Si x est inversible, son inverse se note x    . On l'appelle alors

                  l'inverse de x .

                  On notera le neutre d'une telle structure 1 ou 1E .




10/45                                      D. Cransac        Analyse
~~~

## Page 11

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Pour éviter toute erreur, on essaiera au maximum de n'utiliser la notation
        additive que pour des lois qui ont les mêmes propriétés que la loi + sur
        R.
        La notation + est en général réservée à des lci commutatives et pour
        lesquelles les éléments sont tous inversibles.
        Par exemple, noter + une lci non commutative peut-être déroutant, ainsi
        que pour une lci pour laquelle tous les éléments ne sont pas inversibles.




11/45                                  D. Cransac        Analyse
~~~

## Page 12

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                      Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        La notation multiplicative est la plus couramment utilisée pour des lois
        associatives
        Par exemple il est fréquent d'utiliser × même pour une lci non
        commutative et pour laquelle les éléments ne sont pas tous inversibles.
        Attention
        En général on aura xy ̸= yx , et x −1 n'existera pas forcément !
        Dans toute la suite, on adoptera la notation multiplicative, et on suppose
        que E a un neutre noté 1.




12/45                                   D. Cransac        Analyse
~~~

## Page 13

~~~text
                                                        Lois de composition internes
                                                        Structure de groupe
                                          Groupe
                                                        Sous-groupes
                                                        Morphismes de groupes




        Proposition
        On suppose la loi ⋆ associative. Soient x, y , z ∈ E .
          1 Simplication par un inversible : si x est inversible, alors

                                       x ⋆y =x ⋆z ⇔y =z

          2   Inverse d'un produit : si x et y sont inversibles alors x ⋆ y l'est aussi
              et
                                       (x ⋆ y )−1 = y −1 ⋆ x −1
          3   Puissances négatives  : si x est inversible, on pose pour n ∈ N∗ ,
               −n      −1 n
                            . Alors x −n = (x n )−1 .
                          
              x = x
          4   Inverse d'un inverse : si x est inversible, x −1 l'est aussi et
                 −1 −1
                        = x.
                   
               x

        Attention : l'inverse de x ⋆ y n'a aucune raison d'être x −1 ⋆ y −1 .

13/45                                      D. Cransac        Analyse
~~~

## Page 14

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        Démonstration.
           On a xy = xz ⇔ x −1 xy = x −1 xz ⇔ ey = ez ⇔ y = z
           (xy )(y −1 x −1 ) = x(yy −1 )x −1 = xex −1 = xx −1 = e et de même
           (y −1 x −1 )(xy ) = y −1 (x −1 x)y = y −1 ey = y −1 xx −1 = e Donc
           y −1 x −1 est bien l'inverse à gauche et à droite de xy ..
           Par récurrence.
           Initialisation : Vrai si n = 0.
           Hérédité : Soit n ∈ N, si on suppose vraie pour vrai pour n, alors
           x n+1 ⋆ x −n−1 = x n ⋆ x ⋆ x −1 ⋆ x −n = x n ⋆ e ⋆ x −n = x n ⋆ x −n = e .
           Vrai par unicité de l'inverse.




14/45                                   D. Cransac        Analyse
~~~

## Page 15

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Dénition
        Soit (E , ⋆) un magma et F une partie de E .
        On dit que F est une partie stable (de E par ⋆ ) si pour tous
        x, y ∈ F , x ⋆ y ∈ F .

        Example
        {−1, 1} est une partie stable de (R, ×), mais pas {−2, 2}.




15/45                                  D. Cransac        Analyse
~~~

## Page 16

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                      Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        Dénition
        On appelle groupe tout magma associatif, ayant un neutre, et dont tout
        élément est inversible.
        Si un groupe est commutatif (ce qui signie en fait que sa loi est
        commutative), il est dit abélien.
        Par défaut on utilise la notation multiplicative pour un groupe, sauf pour
        les groupes abéliens pour lesquels on utilise la notation additive.




16/45                                   D. Cransac        Analyse
~~~

## Page 17

~~~text
                                                             Lois de composition internes
                                                             Structure de groupe
                                              Groupe
                                                             Sous-groupes
                                                             Morphismes de groupes




        Example
         1   C, R, Q, Z sont des groupes avec la loi +, mais pas avec la loi ×.
         2   Pour n ∈ N∗ , pour E = Cn , E = Rn , E = Qn ou E = Zn .
             On dénit l'addition + par
              (x1 , x2 , . . . , xn ) + (y1 , y2 , . . . , yn ) = (x1 + y1 , x2 + y2 , . . . , xn + yn )

             alors (E , +) sont des groupes avec la loi +.
         3   C∗ , R∗ , Q∗ , sont des groupes avec la loi ×.
         4   (N, +) n'est pas un groupe..
             En eet 3 n'admet pas d'opposé dans N
         5   (N, ×) n'est pas un groupe.
             En eet 3 n'admet pas d'inverse dans N


17/45                                           D. Cransac        Analyse
~~~

## Page 18

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        Dénition
        Soit X un ensemble non vide.

        On appelle groupe des permutations de X l'ensemble des bijections de
        X dans X muni de la loi de composition ◦.

        On le note SX .




18/45                                   D. Cransac        Analyse
~~~

## Page 19

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                      Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes


        Dans toute la suite, (G , ⋆) est un groupe de neutre e . On adopte la
        notation multiplicative.
        Dénition
        On appelle sous-groupe de (G , ⋆) tout ensemble H vériant les
        propriétés suivantes :
          1  H⊂G;
          2  e ∈H;
          3  Stabilité par produit : ∀x, y ∈ H, x ⋆ y ∈ H ;
          4  Stabilité par passage à l'inverse : ∀x ∈ H , on a x −1 ∈ H .

        Example
        Sont des sous-groupes :
          1 {e} et G dans (G , ⋆).
          2 U (ensemble des complexes de module 1) dans (C∗ , ×).
          3 nZ dans (Z, +).
          4 H = {f ∈ SR | f (0) = 0} dans (SR , ◦).
19/45                                   D. Cransac        Analyse
~~~

## Page 20

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                     Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




        Proposition
        Un ensemble H est un sous groupe de (G , ⋆) si et seulement si H est un
        sous-ensemble non vide de G et pour tout (x, y ) ∈ H 2 , on a

                                     x −1 ⋆ y ∈ H

        Démonstration.
        Montrons l'implication et sa réciproque :
          1"⇒" Supposons que H est un sous-groupe de G .Alors H contient e
           et n'est donc pas vide.
           De plus, soit (x, y ) ∈ H .
           H étant stable par passage à l'inverse,
           on a alors x −1 ∈ H et par stabilité par produit, on a donc
           x −1 ⋆ y ∈ H .



20/45                                 D. Cransac        Analyse
~~~

## Page 21

~~~text
                                                          Lois de composition internes
                                                          Structure de groupe
                                           Groupe
                                                          Sous-groupes
                                                          Morphismes de groupes




        Démonstration.
          2   "⇐" Réciproquement, supposons que H est non vide et que pour
              tout (x, y ) ∈ H 2 , on a x −1 ⋆ y ∈ H .
              Montrons que H possède les trois propriétés énumérées dans sa
              dénition :
                1   H étant non vide, il possède au moins un élément x0 . On a alors
                    e = x0−1 ⋆ x0 ∈ H .
                                                        2         −1
                2   Soit x ∈ H . On a alors (x, e) ∈ H , donc x      ⋆ e = x −1 ∈ H .
                                                                            −1
                3   Soit (x, y ) ∈ H . D'après ce qui précède, on a alors x    ∈ H , donc
                      −1          2                   −1 −1
                    (x , y ) ∈ H , donc x ⋆ y = x            ⋆ y ∈ H.


        Remarque
        On a aussi la propriété équivalente en remplaçant ci-dessus la condition
        x −1 ⋆ y ∈ H par x ⋆ y −1 ∈ H .


21/45                                        D. Cransac        Analyse
~~~

## Page 22

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        Dénition
        Soit (G , ⋆) un groupe et H , un sous-groupe de (G , ⋆).
        On peut dénir sur H une loi appellée loi induite △ telle que

                                ∀(x, y ) ∈ H, x△y = x ⋆ y

        Remarque
        Par la suite, par soucis de simplication on notera la loi sur H : △ avec le
        même symbole que la lci sur G : ⋆
        Theorem
        Un sous-groupe muni de la loi induite du groupe est lui-même un
        groupe.




22/45                                   D. Cransac        Analyse
~~~

## Page 23

~~~text
                                                       Lois de composition internes
                                                       Structure de groupe
                                        Groupe
                                                       Sous-groupes
                                                       Morphismes de groupes




        Démonstration.
        Soit (G , ⋆) un groupe de neutre e et H un sous-groupe de G .
          1  Montrons qu'on peut restreindre ⋆ : G × G → G au départ à H × H
             et à l'arrivée à H .
             On a H × H ⊂ G × G , donc la restriction au départ est légitime,
             pour eectuer la restriction à l'arrivée, il sut de montrer que pour
             tout (x, y ) ∈ H 2 , on a x ⋆ y ∈ H , c'est-à-dire que H est stable par ⋆.
             Or H est un sous-groupe de G : la dénition d'un sous-groupe
             assure cette stabilité.




23/45                                     D. Cransac        Analyse
~~~

## Page 24

~~~text
                                                        Lois de composition internes
                                                        Structure de groupe
                                        Groupe
                                                        Sous-groupes
                                                        Morphismes de groupes




        Démonstration.
         2   H muni de la loi induite par ⋆ est un magma associatif.
             En eet (G , ⋆) est un magma associatif, on a donc
                          ∀(x, y , z) ∈ G 3        (x ⋆ y ) ⋆ z = x ⋆ (y ⋆ z)

             Or H ⊂ G donc
                          ∀(x, y , z) ∈ H 3        (x ⋆ y ) ⋆ z = x ⋆ (y ⋆ z)

             Donc la restriction de ⋆ à H est associative, d'où le résultat.
         3   e est neutre pour la loi induite par ⋆ sur H . En eet, e est le neutre
             de ⋆, donc
                                  ∀x ∈ G          e ⋆x =x ⋆e =x
             D'où le résultat.


24/45                                      D. Cransac        Analyse
~~~

## Page 25

~~~text
                                                      Lois de composition internes
                                                      Structure de groupe
                                        Groupe
                                                      Sous-groupes
                                                      Morphismes de groupes




        Démonstration.
         4   Tout élément de H admet un inverse pour la loi induite par ⋆.
             En eet tout élément x de H admet un inverse x −1 dans G pour la
             loi ⋆ et par stabilité de l'inverse sur le sous-groupe H , on a x −1 ∈ H .
             Donc tout élément de H admet un inverse dans H pour la loi induite
             par ⋆.
         5   On déduit des points précédents que H muni de la loi induite par ⋆
             est un groupe.




25/45                                    D. Cransac        Analyse
~~~

## Page 26

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        Remarque
        La réciproque de ce théorème est également vraie (bien que moins
        utilisée) : si H est un sous-ensemble de G tel que, muni de la loi induite
        par celle de G , H soit un groupe, alors H est un sous-groupe de G .
        Example
        Si n ∈ N∗ , Un est un sous-groupe de (U, ×), donc (Un , ×) est un groupe.




26/45                                   D. Cransac        Analyse
~~~

## Page 27

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Remarque
        Il est plus facile de montrer qu'un ensemble est un sous-groupe que de
        montrer que c'est un groupe (pas besoin de redémontrer l'associativité,
        etc.).
        Par exemple (U, ×) est un groupe, vu comme sous-groupe de (C∗ , ×).
        À chaque fois que l'on essaiera de montrer qu'un ensemble est muni
        d'une structure de groupe, on tentera de le voir comme un sous-groupe
        d'un groupe bien connu.




27/45                                  D. Cransac        Analyse
~~~

## Page 28

~~~text
                             Lois de composition internes
                             Structure de groupe
               Groupe
                             Sous-groupes
                             Morphismes de groupes




        Morphismes de groupes



28/45           D. Cransac        Analyse
~~~

## Page 29

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes




        Dénition
        Soient (G , ⋆) et (G ′ , ∗) deux groupes et φ : G → G ′ .
          1  On dit que φ est un morphisme du groupe (G , ⋆) dans le groupe
             (G ′ , ∗), si

                         ∀x, y ∈ G ,            φ(x ⋆ y ) = φ(x) ∗ φ(y ).

          2   Tout morphisme d'un groupe dans lui-même est appelé
              endomorphisme.
          3   Tout morphisme de G dans G ′ qui est une bijection est appelé
              isomorphisme de G sur G ′ .
              Dans ce cas on dit que G et G ′ sont isomorphes.
              Un morphisme qui est à la fois un isomorphisme et un
              endomorphisme est appelé automorphisme.



29/45                                   D. Cransac        Analyse
~~~

## Page 30

~~~text
                                                       Lois de composition internes
                                                       Structure de groupe
                                         Groupe
                                                       Sous-groupes
                                                       Morphismes de groupes




        Example
             
                 (Z, +) →     (Z, +)
                                2x
         1
                   x    7→
             est un morphisme, mais pas un isomorphisme.
                 (C∗ , ×) → (R∗ , ×)
             
         2
                    z     7→  |z|
                                     est un morphisme, mais pas un
             isomorphisme.
                            → (C∗ , ×)
             
         3
                 (R, +)
                   x      7 →   e ix
             est un morphisme, mais pas un isomorphisme.
                            → (R∗+ , ×)
             
                 (R, +)
         4
                   x      7 →    ex
                                        est un isomorphisme de réciproque ln, qui
             est aussi un isomorphisme.


30/45                                     D. Cransac        Analyse
~~~

## Page 31

~~~text
                                                             Lois de composition internes
                                                             Structure de groupe
                                               Groupe
                                                             Sous-groupes
                                                             Morphismes de groupes




        Example
        Etudions les applications suivantes
          1 Si n ∈ N∗ ,
                                      φn   :∗
                                                 (C , ×) → (C∗ , ×)
                                                   z     7→  zn
          2   Si n ∈ N∗ et a1 , . . . , an ∈ Kn , l'application
                            φn    :      (Kn , +)          →       (K, +)
                                       (x1 , . . . , xn ) 7→ a1 x1 + · · · + an xn




31/45                                           D. Cransac        Analyse
~~~

## Page 32

~~~text
                                                        Lois de composition internes
                                                        Structure de groupe
                                         Groupe
                                                        Sous-groupes
                                                        Morphismes de groupes




        Dans toute la suite, (G , ⋆) et (G ′ , ∗) sont deux groupes de neutres e et e ′ ,
        on adopte une notation multiplicative, et φ : G → G ′ est un morphisme.
        Theorem
        Soit φ un morphisme de G sur G ′ , on a, e et e ′ désignant les neutres de
        G et G ′ :
          1   φ(e) = e ′
                                           −1
          2   ∀x ∈ G , φ(x −1 ) = (φ(x))        .

        Démonstration.
          1   On a φ(e) ∗ φ(e) = φ(e ⋆ e) = φ(e) = φ(e) ∗ e ′ , donc en simpliant
              par φ(e), on en déduit φ(e) = e ′ .
          2   Soit x ∈ G . Alors φ(x −1 ) ∗ φ(x) = φ(x −1 ⋆ x) = φ(e) = e .



32/45                                      D. Cransac        Analyse
~~~

## Page 33

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes



        Corollary
        Sous les mêmes hypothèses, on a
                                                                              k
                        ∀x ∈ G       ∀k ∈ Z            φ(x k ) = φ(x) .

        Démonstration.
            On démontre par récurrence :
            Soit x ∈ G .
            Initialisation : D'après le théorème précédent, on a
                                                                          0
                                 φ(x 0 ) = φ(e) = e ′ = φ(x) .

            Hérédité : Soit n ∈ N, on suppose φ(x n ) = φ(x)n .
            On a alors φ(x n+1 ) = φ(x n x) = φ(x n )φ(x) = φ(x)n φ(x) = φ(x)n+1
            D'après le théorème précédent, pour tout n ∈ N,
                                                               −1
                                     φ(x −n ) = φ(x n )

            d'où φ(x −n ) = φ(x)−n . On en déduit le résultat.
33/45                                  D. Cransac        Analyse
~~~

## Page 34

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Example
         1   C∗ → R∗ , z 7→ |z| est un morphisme de (C∗ , ×) dans (R∗ , ×), donc
             pour tout z ∈ C∗ , on a
                                               1         1
                                                   =
                                           z           |z |
         2   exp est un morphisme de (C, +) dans (C∗ , ×), donc pour tout
                              1
             z ∈ C, e −z = z .
                             e
         3   ln est un morphisme
                                de (R+ , ×) dans (R, +), donc pour tout
                                       ∗

                                1
             x ∈ R∗+ , on a ln     = − ln(x).
                               x




34/45                                  D. Cransac        Analyse
~~~

## Page 35

~~~text
                                                       Lois de composition internes
                                                       Structure de groupe
                                         Groupe
                                                       Sous-groupes
                                                       Morphismes de groupes



        Theorem
         1   La composée de deux morphismes de groupes est un morphisme de
             groupe.
             Plus précisément, soit (G1 , ⋆1 ), (G2 , ⋆2 ) et (G3 , ⋆3 ) trois groupes, φ
             un morphisme de G1 dans G2 et φ un morphisme de G2 dans G3 .
             Alors ψ ◦ φ est un morphisme de G1 dans G3 .
         2   La fonction réciproque d'un isomorphisme (en tant qu'application
             bijective) est un isomorphisme.
             Plus précisément, soit (G1 , ⋆1 ) et (G2 , ⋆2 ) deux groupes et φ un
             isomorphisme de G1 sur G2 . Alors φ−1 est un isomorphisme de G2
             sur G1 .

        Démonstration.
             Pour tout (x, y ) ∈ G12 , (ψ ◦ φ)(xy ) = ψ(φ(xy )) = ψ(φ(x)φ(y )) =
             ψ(φ(x))ψ(φ(y )) = (ψ ◦ φ)(x)(ψ ◦ φ)(y )
             Pour tout (x, y ) ∈ G22 ,
             φ(φ−1 (x)φ−1 (y )) = φ(φ−1 (x))φ(φ−1 (y )) = xy = φ(φ−1 (xy )).
             On a donc en appliquant φ−1 , φ−1 (x)φ−1 (y ) = φ−1 (xy )
35/45                                     D. Cransac        Analyse
~~~

## Page 36

~~~text
                                                       Lois de composition internes
                                                       Structure de groupe
                                        Groupe
                                                       Sous-groupes
                                                       Morphismes de groupes



        Theorem
        L'image d'un sous-groupe par un morphisme de groupes est un
        sous-groupe.

        Démonstration.
        Soient (G , ⋆) et (G ′ , ∗) deux groupes de neutres respectifs e et e ′ , et
        φ : G → G ′ un morphisme de groupes. Soit H un sous-groupe de G .
        Montrons que φ(H) est un sous-groupe de G ′ .
          1  On a évidemment φ(H) ∈ G ′ et de plus e ∈ H et e ′ = φ(e) ∈ φ(H).
          2  Soit x ′ , y ′ ∈ φ(H). Alors x ′ possède un antécédent x ∈ H et y ′ un
             antécédent y ∈ H par φ. On a alors successivement
                  x ′ ∗ y ′−1   = φ(x) ∗ φ(y )−1               par dénition dex et y
                                = φ(x) ∗ φ(y −1 )              car φ est un morphisme
                                = φ(x ⋆ y −1 )             car φ est un morphisme
              Donc x ′ ∗ y ′−1 ∈ φ(H) et nalement φ(H) est donc un sous-groupe
              de G ′ .
36/45                                     D. Cransac        Analyse
~~~

## Page 37

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                     Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




        Theorem
        L'image réciproque d'un sous-groupe par un morphisme est un
        sous-groupe.

        Démonstration.
        Gardons les même notations que dans le premier point, et notons H ′ un
        sous-groupe de G ′ .
          1  On a évidemment φ−1 (H ′ ) ⊂ G et de plus e ′ ∈ H ′ et
             e′ = φ(e) ∈ H ′ donc e ∈ φ−1 (H ′ ).
          2  Soit x, y ∈ φ−1 (H ′ ).
             Alors φ(x), φ(y ) ∈ H ′
             donc φ(x ⋆ y −1 ) = φ(x) ∗ (φ(y ))−1 ∈ H ′
             donc x ⋆ y −1 ∈ φ−1 (H ′ ).
             φ−1 (H) est donc un sous-groupe de G .



37/45                                 D. Cransac        Analyse
~~~

## Page 38

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                     Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




        Remarque
        Lorsque l'on veut montrer qu'un ensemble est muni d'une structure de
        groupe, on commence toujours par essayer de l'identier comme image
        réciproque (ou directe) d'un sous-groupe d'un groupe bien connu par un
        morphisme.




38/45                                 D. Cransac        Analyse
~~~

## Page 39

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Dénition
        Soit φ : G → G ′ un morphisme de groupe.
          1  On appelle noyau de φ, noté Ker φ, l'image réciproque de {e ′ } par
             φ, autrement dit l'ensemble des antécédents de e ′ par φ

                                Ker φ = {x ∈ G | φ(x) = e ′ }.

          2   On appelle image de φ notée Imφ, l'image directe de G par φ.
              Autrement dit
                                   Imφ = {φ(x) | x ∈ G }.




39/45                                  D. Cransac        Analyse
~~~

## Page 40

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                      Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Theorem
        Les noyaux et les images sont des sous-groupes respectivement de G et
        G ′.

        Démonstration.
            {e ′ } est un sous-groupe de G ′ et Ker φ est donc l'image réciproque
            d'un sous-groupe donc un sous-groupe.
            G est un sous-groupe de G donc son image par le morphisme φ est
            un sous-groupe de G ′ .




40/45                                  D. Cransac        Analyse
~~~

## Page 41

~~~text
                                                    Lois de composition internes
                                                    Structure de groupe
                                     Groupe
                                                    Sous-groupes
                                                    Morphismes de groupes




        Démonstration directe.
        Montrons que Ker φ est un sous-groupe de G :
         1 On a Ker φ ⊂ G et de plus φ(e) = e ′ donc Ker φ est un
           sous-ensemble non vide de G .
         2 Soit x, y ∈ Ker φ. Alors on a successivement
                                                                          −1
                              φ(x ⋆ y −1 ) = φ(x) ∗ φ(y )
                                              = e ′ ∗ e ′−1
                                              = e′

             Donc x ⋆ y −1 ∈ Ker φ.Donc Ker φ est un sous-groupe de G .




41/45                                  D. Cransac        Analyse
~~~

## Page 42

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                     Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




        Remarque
        Lorsque l'on veut montrer qu'un ensemble est muni d'une structure de
        groupe, on commence toujours par essayer de l'identier comme noyau
        ou image d'un morphisme.
        Example
        U est le noyau du morphisme  module , de (C∗ , ×) dans (R∗ , ×).




42/45                                 D. Cransac        Analyse
~~~

## Page 43

~~~text
                                                      Lois de composition internes
                                                      Structure de groupe
                                       Groupe
                                                      Sous-groupes
                                                      Morphismes de groupes




        Theorem
        φ surjectif si et seulement si Imφ = G ′ .

        Démonstration.
        Dénition !




43/45                                    D. Cransac        Analyse
~~~

## Page 44

~~~text
                                                     Lois de composition internes
                                                     Structure de groupe
                                       Groupe
                                                     Sous-groupes
                                                     Morphismes de groupes



        Theorem
        φ injectif si et seulement si Ker φ = {e}.

        Démonstration.
        On montre l'implication et sa réciproque :
        "⇒" Supposons φ injectif. On sait que φ(e) = e ′ . Donc e est un
        antécédent de e ′ et comme φ est injective, c'est le seul. Donc
        Ker φ = {e}.
        "⇐" Réciproquement, supposons Ker φ = {e} et montrons que φ est
        injectif.
        Soit (x, y ) ∈ G 2 vériant φ(x) = φ(y ). Alors on a successivement
                φ(x ⋆ y −1 ) =    φ(x) ∗ φ(y )
                                                 −1
                                                        car φ est un morphisme
                                                 −1
                              =   φ(x) ∗ φ(x)
                              =   e′

        Donc x ⋆ y −1 ∈ Ker φ, donc x ⋆ y −1 = e , donc x = y .
44/45                                   D. Cransac        Analyse
~~~

## Page 45

~~~text
                                                   Lois de composition internes
                                                   Structure de groupe
                                    Groupe
                                                   Sous-groupes
                                                   Morphismes de groupes




        Remarque
        Pour montrer qu'un morphisme est injectif, on utilisera TOUJOURS le
        noyau et JAMAIS (ou presque) la méthode classique pour des fonctions
        quelconques : c'est beaucoup plus rapide !




45/45                                 D. Cransac        Analyse
~~~
