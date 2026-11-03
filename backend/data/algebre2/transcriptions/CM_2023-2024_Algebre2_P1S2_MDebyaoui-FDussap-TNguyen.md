# CM_2023-2024_Algebre2_P1S2_MDebyaoui-FDussap-TNguyen.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1y9BsphAZMuYE9RoX3YBLL7Mp2mAEgl85) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                  CM Algèbre 2
                                 Cycle pré-ingénieur 1


     Mohamed Ali DEBYAOUI             Florian DUSSAP     Thi Hien NGUYEN




                                      2023-2024



Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2       Pré-Ing 1 – 2023-2024   1 / 231
~~~

## Page 2

~~~text
Évaluation

Vous aurez 4 notes :
      DS1 (25 %) : 1h en TD, semaine du 04/03/2024.
      DS2 (25 %) : 1h en TD, semaine du 01/04/2024.
      Examen (40 %) : 2h, semaine du 03/06/2024.
      TD (10 %) : au cours du semestre.
On calcule une moyenne pondérée M de ces notes :

                      M = 0,25 (DS1 + DS2) + 0,4 E + 0,1 TD.

La note finale NF est le maximum entre la moyenne M et l’examen E :

                                 NF = max(M, E ).



Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2      Pré-Ing 1 – 2023-2024   2 / 231
~~~

## Page 3

~~~text
Chapitres

1   Groupes et morphismes

2   Systèmes linéaires

3   Espaces vectoriels

4   Applications linéaires

5   Matrices et inverses de matrices

6   Déterminants

7   Représentation matricielle et changements de bases

Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2       Pré-Ing 1 – 2023-2024   3 / 231
~~~

## Page 4

~~~text
                                 Groupes et morphismes




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2     Pré-Ing 1 – 2023-2024   4 / 231
~~~

## Page 5

~~~text
Contenu




1   Groupes et morphismes
      Lois de composition interne
      Groupes
      Morphismes




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2   Pré-Ing 1 – 2023-2024   5 / 231
~~~

## Page 6

~~~text
Contenu




1   Groupes et morphismes
      Lois de composition interne
      Groupes
      Morphismes




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2   Pré-Ing 1 – 2023-2024   6 / 231
~~~

## Page 7

~~~text
Lois de composition interne




Définition
Soit E un ensemble. Une loi de composition interne sur E est une
application :
                        ∗ : E × E −→        E
                             (x, y ) 7−→ x ∗ y .
On appelle magma tout couple (E , ∗) formé d’un ensemble E et d’une loi
de composition interne ∗ sur E .




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2       Pré-Ing 1 – 2023-2024   7 / 231
~~~

## Page 8

~~~text
Lois de composition interne

Questions
   1   Sur R, les opérations +, −, ×, ÷ sont-elles des lois de composition
       interne ?
   2   La soustraction est-elle une loi de composition interne sur N ? sur Z ?
       sur Q ? sur R ? sur C ?
   3   Donner une loi de composition interne sur l’ensemble F(E , E ) des
       applications d’un ensemble E dans lui-même.

Réponses
   1   Les opérations +, − et × sont des lois de compositions internes sur R,
       mais pas ÷. En revanche, ÷ est une loi de composition interne sur R∗ .
   2   La soustraction n’est pas une loi de composition interne sur N. C’est
       une loi de composition interne sur Z, Q, R et C.
   3   La composition ◦ est une loi de composition interne sur F(E , E ).

Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2          Pré-Ing 1 – 2023-2024   8 / 231
~~~

## Page 9

~~~text
Associativité et commutativité

Définition
Soit (E , ∗) un magma.
      On dit que ∗ est associative si ∀x, y , z ∈ E , (x ∗ y ) ∗ z = x ∗ (y ∗ z).
      On dit que ∗ est commutative si ∀x, y ∈ E , x ∗ y = y ∗ x.

Exemple
      Sur R, l’addition et la multiplication sont associatives et commutatives.
      Sur R, la soustraction n’est ni associative ni commutative.
      Sur F(E , E ), la composition d’applications est associative :

                      ∀f , g , h ∈ F(E , E ),   (f ◦ g ) ◦ h = f ◦ (g ◦ h),

      mais pas commutative (sauf si Card(E ) ≤ 1) :

                                  f ◦ g ̸= g ◦ f        en général.
Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2                 Pré-Ing 1 – 2023-2024   9 / 231
~~~

## Page 10

~~~text
Distributivité


Définition
Soit E un ensemble et soient ∗ et △ deux lois de composition interne sur E .
      On dit que ∗ est distributive à gauche par rapport à △ si :

                      ∀x, y , z ∈ E ,   x ∗ (y △ z) = (x ∗ y ) △ (x ∗ z).

      On dit que ∗ est distributive à droite par rapport à △ si :

                      ∀x, y , z ∈ E ,   (x △ y ) ∗ z = (x ∗ z) △ (y ∗ z).

      On dit que ∗ est distributive par rapport à △ si elle est distributive à
      gauche et à droite par rapport à △.



Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2           Pré-Ing 1 – 2023-2024   10 / 231
~~~

## Page 11

~~~text
Distributivité


Exemple
      Dans R, la multiplication est distributive par rapport à l’addition.
      Soit E un ensemble. Dans l’ensemble P(E ) des parties de E ,
      l’intersection est distributive par rapport à la réunion :
                                    (
                                      A ∩ (B ∪ C ) = (A ∩ B) ∪ (A ∩ C ),
             ∀A, B, C ∈ P(E ),
                                      (A ∪ B) ∩ C = (A ∩ C ) ∪ (B ∩ C ).

      La réunion est également distributive par rapport à l’intersection :
                                (
                                  A ∪ (B ∩ C ) = (A ∪ B) ∩ (A ∪ C ),
            ∀A, B, C ∈ P(E ),
                                  (A ∩ B) ∪ C = (A ∪ C ) ∩ (B ∪ C ).



Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2          Pré-Ing 1 – 2023-2024   11 / 231
~~~

## Page 12

~~~text
Élément neutre


Définition
Soit (E , ∗) un magma et soit e ∈ E . On dit que e est un élément neutre
pour ∗ si :
                      ∀x ∈ E , x ∗ e = e ∗ x = x.

Exemple
      Dans (N, +), l’élément neutre est 0.
      Dans (R, ×), l’élément neutre est 1.
      Dans (2Z, ×), il n’y a pas d’élément neutre.
      Dans (F(E , E ), ◦), l’élément neutre est idE .




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2        Pré-Ing 1 – 2023-2024   12 / 231
~~~

## Page 13

~~~text
Élément neutre


Proposition (unicité de l’élément neutre)
Soit (E , ∗) un magma. Si ∗ possède un élément neutre, alors il est unique.

Démonstration.
Soient e et e ′ des éléments neutres de (E , ∗). Puisque e est neutre pour ∗,
on a :
                                 e ∗ e ′ = e ′.
 Mais puisque e ′ est aussi neutre pour ∗, on a :

                                  e ∗ e ′ = e.

 Par conséquent, on a e = e ′ .


Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2         Pré-Ing 1 – 2023-2024   13 / 231
~~~

## Page 14

~~~text
Symétrique d’un élément


Définition
Soit (E , ∗) un magma possédant un élément neutre e et soit x ∈ E .
      On dit que x admet un symétrique à droite s’il existe x ′ ∈ E tel que
      x ∗ x ′ = e.
      On dit que x admet un symétrique à gauche s’il existe x ′ ∈ E tel que
      x ′ ∗ x = e.
      On dit que x est symétrisable s’il existe x ′ ∈ E qui est à la fois
      symétrique à droite et à gauche.

Vocabulaire. On emploie aussi le terme « inversible » à la place de
« symétrisable ».



Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2          Pré-Ing 1 – 2023-2024   14 / 231
~~~

## Page 15

~~~text
Symétrique d’un élément




Exemple
      Dans (R, +), le symétrique d’un nombre x est son opposé −x.
      Dans (R, ×), un nombre x est symétrisable si et seulement si x ̸= 0.
      Dans ce cas, le symétrique de x est son inverse x1 .
      Dans (F(E , E ), ◦), une application f est symétrisable si et seulement
      si f est bijective. Dans ce cas, le symétrique de f est son application
      réciproque f −1 .




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   15 / 231
~~~

## Page 16

~~~text
Symétrique d’un élément

Proposition (unicité du symétrique)
Soit (E , ∗) un magma associatif possédant un élément neutre et soit x ∈ E .
   1   Si x ′ est un symétrique à droite et si x ′′ est un symétrique à gauche
       de x, alors x ′ = x ′′ .
   2   Si x est symétrisable, alors son symétrique est unique.

Démonstration.
Soit x ∈ E et soient x ′ , x ′′ les symétriques à droite et à gauche de x,
c.-à-.d. x ∗ x ′ = e et x ′′ ∗ x = e où e est l’élément neutre de (E , ∗). Par
associativité de ∗, on a :

            x ′ = e ∗ x ′ = (x ′′ ∗ x) ∗ x ′ = x ′′ ∗ (x ∗ x ′ ) = x ′′ ∗ e = x ′′ .



Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2              Pré-Ing 1 – 2023-2024   16 / 231
~~~

## Page 17

~~~text
Symétrique d’un produit

Proposition
Soit (E , ∗) un magma associatif possédant un élément neutre. Si x, y ∈ E
sont symétrisables de symétriques x −1 et y −1 , alors x ∗ y est symétrisable
de symétrique :
                         (x ∗ y )−1 = y −1 ∗ x −1 .

Remarque. Si ∗ n’est pas commutative, l’ordre des symétriques ci-dessus
est important.
Démonstration.
Notons e l’élément neutre de (E , ∗). On a par associativité de ∗ :

 (x ∗ y ) ∗ (y −1 ∗ x −1 ) = x ∗ (y ∗ y −1 ) ∗ x −1 = x ∗ e ∗ x −1 = x ∗ x −1 = e,

donc y −1 ∗ x −1 est le symétrique à droite de x ∗ y . On procède de même
pour montrer que c’est le symétrique à gauche.

Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   17 / 231
~~~

## Page 18

~~~text
Simplification par un élément symétrisable

Proposition
Soit (E , ∗) un magma associatif possédant un élément neutre et soit
x ∈ E . Si x est symétrisable, alors :

                        ∀y , z ∈ E ,   x ∗ y = x ∗ z =⇒ y = z
                        ∀y , z ∈ E ,   y ∗ x = z ∗ x =⇒ y = z.

Attention !
Ces implications sont fausses en général
                                        si x n’est pas inversible. Par
exemple, dans le magma P(R), ∪ , on a :

                [0, 1] ∪ [0, 2] = [0, 1] ∪ [1, 2] mais [0, 2] ̸= [1, 2].

Un autre contre-exemple important est le produit matriciel, cf. chapitre 5.

Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2          Pré-Ing 1 – 2023-2024   18 / 231
~~~

## Page 19

~~~text
Itérés d’un élément


Définition
Soit (E , ∗) un magma associatif possédant un élément neutre e. Si x ∈ E
et n ∈ N, on note x n l’itéré n-ième de x qu’on définit par récurrence par :
                         (
                           x0 = e
                                 x n = x ∗ x n−1      si n ≥ 1.

Autrement dit, si n ≥ 1 alors :

                                     x n = x| ∗ ·{z
                                                  · · ∗ x} .
                                                n fois

Remarque. Pour une loi additive +, l’élément neutre se note 0E et l’itéré
n-ième de x se note nx.


Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2            Pré-Ing 1 – 2023-2024   19 / 231
~~~

## Page 20

~~~text
Itérés d’un élément


Proposition
Soit (E , ∗) un magma associative possédant un élément neutre e. Si x ∈ E
possède un symétrique x −1 , alors pour tout n ∈ N, x n est symétrisable et :
                                            n
                             (x n )−1 = x −1 .

Dans ce cas, on note x −n le symétrique de x n . On définit ainsi x k pour
tout k ∈ Z.
Remarque. Pour une loi additive +, le symétrique de x se note −x. La
proposition précédente s’écrit −(nx) = n(−x). On note −nx le symétrique
de nx, ce qui permet de définir kx pour tout k ∈ Z.



Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   20 / 231
~~~

## Page 21

~~~text
Itérés d’un élément

Exemple
On considère le magma (F(E , E ), ◦). L’itéré n-ième d’une application f est
définie par :            
                         idE              si n = 0,
                    f n = f ◦ · · · ◦ f si n ≥ 1.
                         | {z }
                                     n fois

Si f est bijective, alors on note f −n l’itéré n-ième de f −1 .

Attention !
Si f : R → R, alors f 2 peut avoir un sens différent selon le contexte :
      f 2 peut désigner l’itéré 2e de f , c’est-à-dire l’application x 7→ f (f (x)).
      f 2 peut désigner le carré de f , c’est-à-dire l’application x 7→ f (x)2 .


Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2           Pré-Ing 1 – 2023-2024   21 / 231
~~~

## Page 22

~~~text
Applications à valeurs dans un magma

Proposition
Soit E et F des ensembles non vides et soit ∗ une loi de composition
interne sur F . On définit la loi de composition interne ⊛ sur F(E , F ) par :

                         ∀x ∈ E ,   (f ⊛ g )(x) = f (x) ∗ g (x).

De plus :
   1   si ∗ est associative ou commutative, ⊛ l’est aussi.
   2   si e est l’élément neutre pour ∗, alors l’application constante égale à e
       est l’élément neutre pour ⊛.

En pratique, on note aussi ∗ la loi de F(E , F ). C’est ainsi qu’on définit la
somme et le produit de fonctions à valeurs réelles :

               (f + g )(x) = f (x) + g (x) et (fg )(x) = f (x)g (x).

Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2          Pré-Ing 1 – 2023-2024   22 / 231
~~~

## Page 23

~~~text
Contenu




1   Groupes et morphismes
      Lois de composition interne
      Groupes
      Morphismes




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2   Pré-Ing 1 – 2023-2024   23 / 231
~~~

## Page 24

~~~text
Groupes



Définition
Soit (G , ∗) un magma. On dit que (G , ∗) est un groupe si :
   1   la loi ∗ est associative ;
   2   la loi ∗ admet un élément neutre ;
   3   tout élément de G est symétrisable pour ∗.
Si de plus la loi ∗ est commutative, on dit que (G , ∗) est un groupe
commutatif (ou abélien).




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2       Pré-Ing 1 – 2023-2024   24 / 231
~~~

## Page 25

~~~text
Groupes



Exemple
      (Z, +), (Q, +), (R, +) et (C, +) sont des groupes abéliens.
      (Q∗ , ×), (R∗ , ×) et (C∗ , ×) sont des groupes abéliens.
      (N, +), (Z∗ , ×) et (R, ×) ne sont pas des groupes.
      Soit E un ensemble et soit S(E ) l’ensemble des applications bijectives
      de E dans E . Alors (S(E ), ◦) est un groupe, non abélien si E possède
      au moins trois éléments. Ce groupe est appelé groupe symétrique de
      E , ou groupe des permutations de E .




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2          Pré-Ing 1 – 2023-2024   25 / 231
~~~

## Page 26

~~~text
Groupe produit


Définition
Soient (E1 , ∗1 ), . . . , (En , ∗n ) des magmas. On définit sur E = E1 × · · · × En
une loi de composition interne ∗ appelée loi produit par :

                         ∀(x1 , . . . , xn ) ∈ E , ∀(y1 , . . . , yn ) ∈ E ,
              (x1 , . . . , xn ) ∗ (y1 , . . . , yn ) = (x1 ∗1 y1 , . . . , xn ∗n yn ).

Proposition (à faire chez vous)
Soient (G1 , ∗1 ), . . . , (Gn , ∗n ) des groupes d’éléments neutres e1 , . . . , en .
Alors G = G1 × · · · × Gn est un groupe pour la loi produit, d’élément
neutre (e1 , . . . , en ). De plus, le symétrique d’un élément (x1 , . . . , xn ) ∈ G
est l’élément (x1−1 , . . . , xn−1 ) où xi−1 est le symétrique de xi dans (Gi , ∗i ).


Debyaoui, Dussap, Nguyen (CYU)              CM Algèbre 2                Pré-Ing 1 – 2023-2024   26 / 231
~~~

## Page 27

~~~text
Sous-groupes

Définition
Soient (G , ∗) un groupe et H une partie de G . On dit que H est un
sous-groupe de G si (H, ∗) un groupe.

Exemple
Pour tout groupe G d’élément neutre e, les parties {e} et G sont des
sous-groupes de G . Un sous-groupe de G différent de {e} et G est appelé
sous-groupe propre de G .

Lemme
Soient (G , ∗) un groupe d’élément neutre e et H un sous-groupe de G .
Alors :
   1   e est l’élément neutre de (H, ∗).
   2   H est stable par passage à l’inverse : ∀h ∈ H,   h−1 ∈ H.

Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   27 / 231
~~~

## Page 28

~~~text
Sous-groupes



Démonstration.
   1   Soit H un sous-groupe de (G , ∗). Alors (H, ∗) est un groupe, notons
       eH son élément neutre. Alors on a eH ∗ eH = eH et eH ∗ e = eH , donc
       eH ∗ eH = eH ∗ e. En simplifiant à gauche par eH , on obtient eH = e.
   2   Soit h ∈ H, soit h′ ∈ H son inverse dans H et soit h−1 son inverse
       dans G . Alors on a :

            h′ = e ∗ h′ = (h−1 ∗ h) ∗ h′ = h−1 ∗ (h ∗ h′ ) = h−1 ∗ e = h−1 .

       Donc h−1 ∈ H.




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2          Pré-Ing 1 – 2023-2024   28 / 231
~~~

## Page 29

~~~text
Caractérisation des sous-groupes

Proposition
Soient (G , ∗) un groupe et H une partie de G . Alors H est un sous-groupe
de G si et seulement si :
   1   H est non vide ;
   2   H est stable par produit et passage à l’inverse :

                                 ∀x, y ∈ H,    x ∗ y −1 ∈ H.

En pratique, pour vérifier que H est non vide, on regarde si l’élément
neutre e de G appartient à H :
       si e ∈ H, alors H est non vide. Il reste à vérifier la propriété de
       stabilité pour montrer que H est un sous-groupe.
       si e ∈
            / H, alors H n’est pas un sous-groupe.


Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2             Pré-Ing 1 – 2023-2024   29 / 231
~~~

## Page 30

~~~text
Caractérisation des sous-groupes

Démonstration.
Ces conditions sont évidemment nécessaires, montrons qu’elles sont
suffisantes.
      Puisque H est non vide, soit x ∈ H. Par stabilité, on a
      e = x ∗ x −1 ∈ H. Puisque e est neutre pour ∗ dans G , il l’est aussi
      dans H.
      Si x ∈ H, alors par stabilité x −1 = e ∗ x −1 ∈ H. Donc le symétrique
      de x pour ∗ appartient à H.
      Si x, y ∈ H, alors y −1 ∈ H d’après le point précédent, donc par
      stabilité on a x ∗ y = x ∗ (y −1 )−1 ∈ H. Ainsi, H est sable par ∗.
      La loi ∗ étant associative sur G , elle l’est à fortiori sur H.
On a montré que ∗ est une loi de composition interne associative sur H,
possède un élément neutre dans H et que tout élément de H possède un
symétrique dans H. Donc H est un sous-groupe de (G , ∗).

Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2           Pré-Ing 1 – 2023-2024   30 / 231
~~~

## Page 31

~~~text
Caractérisation des sous-groupes

Exemple
      (Z, +) est un sous-groupe de (Q, +), qui est un sous-groupe de
      (R, +), qui est un sous-groupe de (C, +).
      Montrons que (U, ×) est groupe. Pour ce faire, on montre que c’est
      un sous-groupe de (C∗ , ×) :
         1   On a bien U ⊂ C∗ .
         2   U est non vide car 1 ∈ U.
         3   Pour tous z, w ∈ U, on a :

                                               |z|   1
                                    zw −1 =         = = 1,
                                               |w |  1

             donc zw −1 ∈ U.
      Pour tout n ∈ N∗ , (Un , ×) est un sous-groupe de U (le vérifier !).


Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2            Pré-Ing 1 – 2023-2024   31 / 231
~~~

## Page 32

~~~text
Contenu




1   Groupes et morphismes
      Lois de composition interne
      Groupes
      Morphismes




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2   Pré-Ing 1 – 2023-2024   32 / 231
~~~

## Page 33

~~~text
Morphismes


Définition
Soient (E , ∗) et (F , △) deux magmas et f une application de E dans F . On
dit que f est un morphisme (ou homomorphisme) de (E , ∗) dans (F , △) si :

                         ∀x, y ∈ E ,   f (x ∗ y ) = f (x) △ f (y ).

Si (E , ∗) et (F , △) sont des groupes, on dit que f est un morphisme de
groupes.

Un peu de vocabulaire :
      Un morphisme de (E , ∗) dans lui-même est appelé un endomorphisme.
      Un morphisme bijectif est appelé un isomorphisme.
      Un endomorphisme bijectif est appelé un automorphisme.


Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2             Pré-Ing 1 – 2023-2024   33 / 231
~~~

## Page 34

~~~text
Morphismes

Exemple
      Pour tout λ ∈ R, l’application linéaire :

                                        f : R −→ R
                                            x 7−→ λx,

      est un endomorphisme du groupe (R, +). Si λ ̸= 0, c’est un
      automorphisme.
      L’exponentielle est un isomorphisme de groupes de (R, +) dans
      (R∗+ , ×). En effet, pour tous x, y ∈ R, on a :

                                 exp(x + y ) = exp(x) × exp(y ),

      donc exp est un morphisme de groupe, et on sait que l’exponentielle
      est bijective de R dans R∗+ .

Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2         Pré-Ing 1 – 2023-2024   34 / 231
~~~

## Page 35

~~~text
Composition de morphismes

Proposition
La composée de deux morphismes est un morphisme.

Démonstration.
Soient (E , ∗), (F , △) et (G , ♡) des magmas, et soient f : E → F et
g : F → G des morphismes. Alors pour tous x, y ∈ E , on a :
                                                  
                   (g ◦ f )(x ∗ y ) = g f (x ∗ y )
                                                      
                                    = g f (x) △ f (y )
                                                       
                                    = g f (x) ♡ g f (y )
                                 = (g ◦ f )(x) ♡ (g ◦ f )(y ).

Par conséquent, g ◦ f est un morphisme de (E , ∗) dans (G , ♡).


Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2           Pré-Ing 1 – 2023-2024   35 / 231
~~~

## Page 36

~~~text
Application réciproque d’un isomorphisme


Proposition
L’application réciproque d’un isomorphisme est un isomorphisme.

Démonstration.
Soient (E , ∗) et (F , △) des magmas et soit f : E → F un isomorphisme.
L’application f est bijective, donc elle possède une application réciproque
f −1 : F → E également bijective. Montrons que f −1 est un morphisme.
Pour tous x, y ∈ F , on a :

          f f −1 (x) ∗ f −1 (y ) = f f −1 (x) △ f f −1 (y ) = x △ y ,
                                                         


donc f −1 (x) ∗ f −1 (y ) = f −1 (x △ y ). Par conséquent, f −1 est un
isomorphisme.


Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2           Pré-Ing 1 – 2023-2024   36 / 231
~~~

## Page 37

~~~text
Calculs avec un morphisme de groupes




Proposition
Soient (G , ∗) et (G ′ , △) deux groupes d’éléments neutres respectifs e ∈ G
et e ′ ∈ G ′ . Si f : G → G ′ est un morphisme, alors :
   1   f (e) = e ′ .
   2   ∀x ∈ G , f (x −1 ) = f (x)−1 .
   3   ∀x ∈ G , ∀n ∈ Z, f (x n ) = f (x)n .




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2   Pré-Ing 1 – 2023-2024   37 / 231
~~~

## Page 38

~~~text
Calculs avec un morphisme de groupes


Démonstration.
   1   On a e = e ∗ e, donc :

             f (e) = f (e ∗ e) =⇒ f (e) = f (e) △ f (e)
                                  =⇒ f (e) △ f (e)−1 = f (e) △ f (e) △ f (e)−1
                                  =⇒ e ′ = f (e).

   2   Soit x ∈ G , alors on a :

                          e ′ = f (e) = f (x ∗ x −1 ) = f (x) △ f (x −1 ).

       Par conséquent, f (x −1 ) est le symétrique de f (x).
   3   Par récurrence (à faire chez soi).


Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2             Pré-Ing 1 – 2023-2024   38 / 231
~~~

## Page 39

~~~text
Image directe/réciproque d’un sous-groupe




Proposition
Soient (G , ∗) et (G ′ , △) deux groupes et soit f : G → G ′ un morphisme.
   1   Si H est un sous-groupe de (G , ∗), alors f (H) est un sous-groupe de
       (G ′ , △).
   2   Si H ′ est un sous-groupe de (G ′ , △), alors f −1 (H ′ ) est un sous-groupe
       de (G , ∗).




Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2           Pré-Ing 1 – 2023-2024   39 / 231
~~~

## Page 40

~~~text
Image directe/réciproque d’un sous-groupe



Démonstration de 1.
L’ensemble f (H) est non vide car H est non vide. Soient y1 , y2 ∈ f (H),
alors il existe x1 , x2 ∈ H tels que f (x1 ) = y1 et f (x2 ) = y2 . Montrons que
y1 △ y2−1 ∈ f (H). On a :

                     y1 △ y2−1 = f (x1 ) △ f (x2 )−1 = f (x1 ∗ x2−1 ).

Or, x1 ∗ x2−1 ∈ H car H est un sous-groupe de (G , ∗), donc
y1 △ y2−1 ∈ f (H). Ainsi, on a montré que f (H) est un sous-groupe de
(G ′ , △).




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2            Pré-Ing 1 – 2023-2024   40 / 231
~~~

## Page 41

~~~text
Image directe/réciproque d’un sous-groupe



Démonstration de 2.
On a f (e) = e ′ ∈ H ′ , donc e ∈ f −1 (H ′ ). Par conséquent, f −1 (H ′ ) est non
vide. Soient x1 , x2 ∈ f −1 (H ′ ), montrons que x1 ∗ x2−1 ∈ f −1 (H ′ ). On a :

                         f (x1 ∗ x2−1 ) = f (x1 ) △ f (x2 )−1 ∈ H ′ ,

car f (x1 ) ∈ H ′ , f (x2 ) ∈ H ′ et H ′ est un sous-groupe de (G ′ , △). Par
conséquent, x1 ∗ x2−1 ∈ f −1 (H ′ ). Ainsi, on a montré que f −1 (H ′ ) est un
sous-groupe de (G , ∗).




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2              Pré-Ing 1 – 2023-2024   41 / 231
~~~

## Page 42

~~~text
Noyau et image d’un morphisme de groupes


Définition
Soient (G , ∗) et (G ′ , △) deux groupes et soit f : G → G ′ un morphisme.
On note e ′ l’élément neutre de G ′ .
      f (G ) est appelé l’image de f et on le note Im f .
      f −1 ({e ′ }) est appelé le noyau de f et on le note ker f .

Proposition
Si f : G → G ′ est un morphisme de groupe, alors ker f est un sous-groupe
de G et Im f est un sous-groupe de G ′ .

C’est la conséquence de la proposition précédente.



Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2           Pré-Ing 1 – 2023-2024   42 / 231
~~~

## Page 43

~~~text
Injectivité d’un morphisme de groupes


Lemme
Soient (G , ∗) et (G ′ , △) deux groupes et soit f : G → G ′ un morphisme.
Pour tous x, y ∈ G , on a l’équivalence :

                           f (x) = f (y ) ⇐⇒ x ∗ y −1 ∈ ker f .

Démonstration.
Soit e ′ l’élément neutre de G ′ et soient x, y ∈ G . Alors on a :

       f (x) = f (y ) ⇐⇒ f (x) △ f (y )−1 = e ′
                         ⇐⇒ f (x ∗ y −1 ) = e ′         (f est un morphisme)
                         ⇐⇒ x ∗ y −1 ∈ ker f .



Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2         Pré-Ing 1 – 2023-2024   43 / 231
~~~

## Page 44

~~~text
Injectivité d’un morphisme de groupes

Théorème
Soit (G , ∗) un groupe d’élément neutre e et soit (G ′ , △) un groupe. Alors
un morphisme f : G → G ′ est injectif si et seulement si ker f = {e}.

Démonstration.
On procède par double implication.
( =⇒ ) Supposons que f est injective. Soit x ∈ ker f , alors on a :

                                 f (x) = e ′ = f (e),

donc x = e par injectivité de f . Par conséquent, ker f = {e}.
( ⇐= ) Supposons que ker f = {e}. Soient x, y ∈ E tels que f (x) = f (y ),
alors d’après le lemme précédent, on a x ∗ y −1 ∈ ker f . Puisque ker f = {e},
alors x ∗ y −1 = e, c’est-à-dire x = y . Par conséquent, f est injective.

Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2      Pré-Ing 1 – 2023-2024   44 / 231
~~~

## Page 45

~~~text
                                 Systèmes linéaires




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2    Pré-Ing 1 – 2023-2024   45 / 231
~~~

## Page 46

~~~text
Contenu




2   Systèmes linéaires
      Définitions
      Systèmes équivalents
      Algorithme de Gauss
      Résolution d’un système linéaire




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   46 / 231
~~~

## Page 47

~~~text
Contenu




2   Systèmes linéaires
      Définitions
      Systèmes équivalents
      Algorithme de Gauss
      Résolution d’un système linéaire




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   47 / 231
~~~

## Page 48

~~~text
Système d’équations linéaires
Dans ce chapitre, K désigne l’ensemble R ou l’ensemble C, et n et p sont
des entiers naturels non nuls.
Définition
On appelle système de n équations linéaires à p inconnues x1 , . . . , xp un
système de la forme :

                   a1,1 x1 + a1,2 x2 + · · · + a1,p xp = b1
                 
                 
                 
                  a2,1 x1 + a2,2 x2 + · · · + a2,p xp = b2
                 
                 
                                                     ..
                 
                 
                                                     .
                 
                 
                   an,1 x1 + an,2 x2 + · · · + an,p xp = bn ,

où les ai,j ∈ K sont les coefficients du système et les bi ∈ K sont le second
membre. Une solution de ce système est un vecteur (s1 , . . . , sp ) ∈ Kp
vérifiant simultanément chaque équation du système. Si tous les bi sont
nuls, on dit que le système est homogène.
Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2          Pré-Ing 1 – 2023-2024   48 / 231
~~~

## Page 49

~~~text
Matrice associée à un système

Définition
Soit (S) un système linéaire :

                          a1,1 x1 + a1,2 x2 + · · · + a1,p xp = b1
                        
                        
                        
                         a2,1 x1 + a2,2 x2 + · · · + a2,p xp = b2
                        
                        
                                                            ..
                        
                        
                                                            .
                        
                        
                         an,1 x1 + an,2 x2 + · · · + an,p xp = bn .

On appelle matrice associée au système (S) le tableau de nombres :
                                              
                          a1,1 a1,2       a1,p
                        a2,1 a2,2        a2,p 
                                               .
                                              
                        
                                              
                          an,1 an,2       an,p

Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2           Pré-Ing 1 – 2023-2024   49 / 231
~~~

## Page 50

~~~text
Matrice augmentée

Définition
Soit (S) un système linéaire de matrice A et notons B le vecteur colonne
formé par le second membre :
                                                  
                       a1,1       a1,p               b1
                 A=                   ,     B =  .
                                                  
                       an,1       an,p               bn

On appelle matrice augmentée du système (S) la matrice obtenue en
juxtaposant A et B :
                                           
                         a1,1       a1,p b1
                                            .
                                           
                       
                         an,1       an,p bn


Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2        Pré-Ing 1 – 2023-2024   50 / 231
~~~

## Page 51

~~~text
Exemple
Soit le système de 5 équations à 3 inconnues :
                        
                        
                           3x1 + 2x2 + 5x3 = 7
                        
                         2x1
                        
                        
                                     + 2x3 = −4
                           −x1 + x2 − 3x3 = 2
                        
                            4x1 − 2x2       = 32
                        
                        
                        
                        
                        
                                  3x2 + 5x3 = 4.
                        

La matrice associée A et la matrice augmentée M sont :

                                           3   2    5  7
                                                      
                 3    2     5
              2
                     0     2
                                        2
                                              0    2 −4 
                                                         
         A = −1 1 −3 , M = −1 1 −3 2 
                                      
                                                         .
               4 −2 0                  4 −2 0 3/2
                 0    3     5              0   3    5  4


Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2      Pré-Ing 1 – 2023-2024   51 / 231
~~~

## Page 52

~~~text
Contenu




2   Systèmes linéaires
      Définitions
      Systèmes équivalents
      Algorithme de Gauss
      Résolution d’un système linéaire




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   52 / 231
~~~

## Page 53

~~~text
Opérations élémentaires


Définition
On appelle opération élémentaire sur les lignes d’un système (ou d’une
matrice) l’une des opérations suivantes :
   1   Li ↔ Lj : échanger les lignes Li et Lj .
   2   Li ← λLi (λ ̸= 0) : multiplication de la ligne Li par un scalaire λ ∈ K∗ .
   3   Li ← Li + λLj (i ̸= j) : ajouter λLj à la ligne Li .

Remarque. Les opérations élémentaires sont inversibles :
   1   Li ↔ Lj est son propre inverse.
   2   L’inverse de Li ← λLi est Li ← λ1 Li .
   3   L’inverse de Li ← Li + λLj est Li ← Li − λLj .



Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2             Pré-Ing 1 – 2023-2024   53 / 231
~~~

## Page 54

~~~text
Équivalence en lignes

Définition
       On dit que deux systèmes sont équivalents si on peut passer de l’un à
       l’autre par une suite finie d’opérations élémentaires sur les lignes.
       On dit que deux matrices M et M ′ sont équivalentes en lignes si on
       peut passer de l’une à l’autre par une suite finie d’opérations
       élémentaires sur les lignes. Dans ce cas, on note : M ∼ M ′ .
                                                                     L

Remarques.
   1   Si on passe d’un système (S1 ) à un système (S2 ) par une suite
       d’opérations élémentaires O1 , O2 , . . . , Om , alors on passe de (S2 ) à
       (S1 ) par la suite Om −1 , . . . , O −1 , O −1 . Ainsi, si (S ) est équivalent à
                                           2      1                 1
       (S2 ), alors (S2 ) est équivalent à (S1 ). L’équivalence en lignes est une
       relation d’équivalence.
   2   Effectuer des opérations élémentaires sur un système revient à les
       effectuer sur sa matrice augmentée.
Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2            Pré-Ing 1 – 2023-2024   54 / 231
~~~

## Page 55

~~~text
Équivalence et ensemble de solutions

Lemme
Si (S1 ) est un système linéaire et (S2 ) est le système obtenu à partir de
(S1 ) après une opération élémentaire, alors les solutions de (S1 ) sont des
solutions de (S2 ).

Démonstration.
Soit s = (s1 , . . . , sp ) une solution de (S1 ).
      Si l’opération élémentaire pour passer à (S2 ) est un échange de lignes
      ou la multiplication d’une ligne par une constante non nulle, il est
      évident que s est solution de (S2 ).
      Si l’opération élémentaire est Li ← Li + λLj , alors puisque s est
      solution de Li et de Lj , il est aussi solution de λLj et de Li + λLj ,
      donc s est solution de (S2 ).


Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2        Pré-Ing 1 – 2023-2024   55 / 231
~~~

## Page 56

~~~text
Équivalence et ensemble de solutions



Proposition
Deux systèmes équivalents ont le même ensemble de solutions.

Démonstration.
Soient (S1 ) et (S2 ) des systèmes linéaires équivalents. Puisqu’on passe de
(S1 ) à (S2 ) par des opérations élémentaires, les solutions de (S1 ) sont des
solutions de (S2 ) d’après le lemme précédent. Réciproquement, des
opérations élémentaires permettent de passer de (S2 ) à (S1 ), donc les
solutions de (S2 ) sont aussi des solutions de (S1 ). Les systèmes (S1 ) et
(S2 ) ont donc les mêmes solutions.




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   56 / 231
~~~

## Page 57

~~~text
Contenu




2   Systèmes linéaires
      Définitions
      Systèmes équivalents
      Algorithme de Gauss
      Résolution d’un système linéaire




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   57 / 231
~~~

## Page 58

~~~text
Matrice échelonnée en lignes




Définition
Une matrice est échelonnée en lignes si elle vérifie les deux propriétés
suivantes :
   1   Si une ligne est nulle, toutes les lignes suivantes le sont aussi.
   2   À partir de la 2e ligne, dans chaque ligne non nulle, le premier
       coefficient non nul (à partir de la gauche) est situé strictement à
       droite du premier coefficient non nul de la ligne précédente.




Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2          Pré-Ing 1 – 2023-2024   58 / 231
~~~

## Page 59

~~~text
Matrice échelonnée en lignes

Exemple
                                
                    1        2 3
   1   La matrice 0
                            0 0 n’est pas échelonnée en lignes.
                    2        1 3
                                     
                    1        2 3 4 5
   2   La matrice 0
                            6 7 8 9 est échelonnée en lignes.
                    0        0 0 1 2
                                     
                    1        2 3 4 5
   3   La matrice 0
                            0 4 5 6 n’est pas échelonnée en lignes.
                    0        7 8 9 1
                                     
                    1        2 0 0 3
                  0         0 4 5 6
   4   La matrice 
                  0
                                       n’est pas échelonnée en lignes.
                             0 7 8 0
                    0        0 0 0 9

Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2        Pré-Ing 1 – 2023-2024   59 / 231
~~~

## Page 60

~~~text
Pivots

Définition
Dans une matrice échelonnée en lignes, on appelle pivot le premier
coefficient non nul de chaque ligne non entièrement nulle.

Exemple
Dans la matrice échelonnée :
                                            
                           2     1    2 0  3
                         0      1    4 5  6
                                            
                         0
                                0    0 −3 7 
                                             ,
                         0      0    0 0 −2
                           0     0    0 0  0

les pivots sont dans l’ordre : 2, 1, −3, −2.


Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2    Pré-Ing 1 – 2023-2024   60 / 231
~~~

## Page 61

~~~text
Algorithme du pivot de Gauss



Proposition (admise)
Toute matrice est équivalente en lignes à une matrice échelonnée en lignes.

      La démonstration repose sur l’algorithme du pivot de Gauss, qui
      consiste à effectuer des opérations élémentaires sur les lignes d’une
      matrice pour mettre à zéro petit à petit des coefficients jusqu’à
      obtenir une matrice échelonnée équivalente.
      Le système associé à une matrice échelonnée en lignes peut ensuite
      être résolu facilement par « remontée ».




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   61 / 231
~~~

## Page 62

~~~text
Exemple

On considère le système de 3 équations à 4 inconnues :
                     
                     2x1 + 7x2 + 11x3 + 15x4 = 19
                     
                       3x1 + 5x2 + 8x3 + 11x4 = 14                             (S)
                     
                        x1 + x2 + 2x3 + 3x4 = 4.
                     

La matrice augmentée de (S) est :
                                       
                            2 7 11 15 19
                     M = 3 5 8 11 14.
                            1 1 2 3 4

On commence par échanger les lignes 1 et 3 car il est plus facile d’effectuer
les calculs avec un pivot qui vaut 1 ou −1.


Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2          Pré-Ing 1 – 2023-2024   62 / 231
~~~

## Page 63

~~~text
                                              
                                1   1 2 3 4 L1 ↔L3
                          M ∼ 3    5 8 11 14
                            L
                                2   7 11 15 19 L1 ↔L3
                                            
                               1    1 2 3 4
                            ∼ 0    2 2 2 2 L2 ←L2 −3L1
                            L
                               0    5 7 9 11 L3 ←L3 −2L1
                                            
                               1    1 2 3 4
                            ∼ 0    1 1 1 1 L2 ← 12 L2
                            L
                               0    5 7 9 11
                                           
                               1    1 2 3 4
                            ∼ 0    1 1 1 1
                            L
                               0    0 2 4 6 L3 ←L3 −5L2
                                           
                               1    1 2 3 4
                            ∼ 0
                                   1 1 1 1
                            L
                               0    0 1 2 3 L3 ← 12 L3

Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2     Pré-Ing 1 – 2023-2024   63 / 231
~~~

## Page 64

~~~text
Le système (S) est donc équivalent au système
                       
                       x1 + x2 + 2x3 + 3x4 = 4
                       
                              x2 + x3 + x4 = 1                                  (S ′ )
                       
                                    x3 + 2x4 = 3.
                       

On passe l’inconnue x4 dans le second membre et on la traite comme un
paramètre. Le système est alors triangulaire en x1 , x2 , x3 , on le résout par
« remontée » : la dernière équation donne la valeur de x3 , ce qui permet de
trouver la valeur de x2 dans la 2e équation, ce qui permet de trouver la
valeur de x1 dans la 1re équation.
                                         
       x1 + x2 + 2x3 = 4 − 3x4
                                         x1 + x2 + 2x3 = 4 − 3x4
                                          
               x2 + x3 = 1 − x4 ⇐⇒               x2            = −2 + x4
                                         
                     x3 = 3 − 2x4                          x3 = 3 − 2x4
                                         
                                          
                                          x1
                                                            =0
                                    ⇐⇒           x2          = −2 + x4
                                          
                                                         x3 = 3 − 2x4 .
                                          

Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   64 / 231
~~~

## Page 65

~~~text
Finalement, on obtient une description paramétrique des solutions du
système : on a exprimé les inconnues x1 , x2 , x3 en fonction de l’inconnue x4
qui n’est pas contrainte et peut prendre n’importe quelle valeur dans R. Les
solutions de (S) sont donc tous les vecteurs de la forme :

                                 (0, −2 + x4 , 3 − 2x4 , x4 ),

avec x4 ∈ R une variable libre. L’ensemble des solutions s’écrit :
                    
               S = (0, −2 + x4 , 3 − 2x4 , x4 ) : x4 ∈ R .


Remarque. Géométriquement, on interprète S comme la droite dans un
espace à 4 dimensions (!) passant par le point de coordonnées (0, −2, 3, 0)
et dirigée par le vecteur de coordonnées (0, 1, −2, 1).



Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2           Pré-Ing 1 – 2023-2024   65 / 231
~~~

## Page 66

~~~text
Lignes nulles d’une matrice échelonnée



Soit M la matrice augmentée échelonnées en lignes d’un système linéaire.
      Les lignes entièrement nulle de M correspondent à des équations
      « 0 = 0 ». Elles peuvent être supprimées du système sans changer les
      solutions.
      Après avoir enlever les lignes nulles, si le pivot de la dernière lignes est
      dans la dernière colonne, alors le système contient une équation de la
      forme « 0 = b » avec b ̸= 0 le pivot. Dans ce cas, le système n’a pas
      de solutions.




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   66 / 231
~~~

## Page 67

~~~text
Contenu




2   Systèmes linéaires
      Définitions
      Systèmes équivalents
      Algorithme de Gauss
      Résolution d’un système linéaire




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   67 / 231
~~~

## Page 68

~~~text
Rang d’une matrice/d’un système linéaire

Proposition (admise)
Soient M1 et M2 deux matrices échelonnées en lignes. Si M1 et M2 sont
équivalentes en lignes, alors le nombre de pivots de M1 est égal au nombre
de pivots de M2 .

Cette proposition implique que peu importe la façon d’échelonner en lignes
une matrice, le nombre de pivots est toujours le même.
Définition
      On appelle rang d’une matrice M, et on note rg(M), le nombre de
      pivots obtenus après avoir échelonné en lignes M.
      On appelle rang d’un système linéaire le rang de sa matrice associée.

Remarque. Le rang est toujours plus petit que le nombre de lignes et le
nombre de colonnes de la matrice.

Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2         Pré-Ing 1 – 2023-2024   68 / 231
~~~

## Page 69

~~~text
Inconnues principales/secondaires




Définition
Soit (S) un système linéaire à p inconnues, de rang r et dont la matrice
associée est échelonnée en lignes.
      On appelle inconnues principales les r inconnues correspondant aux
      colonnes contenant les pivots.
      On appelle inconnues secondaires les p − r inconnues restantes.




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2        Pré-Ing 1 – 2023-2024   69 / 231
~~~

## Page 70

~~~text
Système compatible/incompatible


Définition
      On dit qu’un système est incompatible s’il n’admet aucune solution.
      On dit qu’il est compatible s’il admet au moins une solution.

Exemple
Soit (Sα,β ) le système linéaire :
                           
                           
                              x1 − 3x2 + 5x3 = −4
                           
                           2x + x − 4x = −1
                           
                                1     2     3
                                                                                (Sα,β )
                           
                           
                            3x1 − 2x2 + x3 = α
                           
                           4x − 5x + 6x = β
                                 1      2           3




Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2       Pré-Ing 1 – 2023-2024     70 / 231
~~~

## Page 71

~~~text
Exemple
Sa matrice augmentée est :

                                         1 −3 5 −4
                                                  
                                        2 1 −4 −1
                                 Mα,β = 
                                        3 −2 1
                                                   .
                                                α
                                         4 −5 6 β

En appliquant l’algorithme du pivot de Gauss, on obtient la matrice
échelonnée :
                               1 −3 5         −4
                                                 

                        ′
                             0 1 −2           1 
                      Mα,β =0 0
                                                  .
                                        0 α + 5
                               0 0      0 β+9
Le système est compatible si et seulement si α = −5 et β = −9. Dans ce
cas, le système est de rang 2, les inconnues principales sont x1 , x2 et
l’inconnue secondaire est x3 .

Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2    Pré-Ing 1 – 2023-2024   71 / 231
~~~

## Page 72

~~~text
Existence et unicité des solutions en fonction du rang

Proposition
Soit un système de n équations à p inconnues, de rang r , et soit (A | B) sa
matrice augmentée.
      Si r = n, alors le système est compatible quel que soit B.
      Si r < n, toute forme échelonnée de A contient n − r lignes nulles. Le
      système est compatible ssi ces lignes sont entièrement nulles dans la
      forme échelonnée de la matrice augmentée.
Dans le cas où le système est compatible :
      Si r = p, alors le système admet une unique solution.
      Si r < p, alors le système admet une infinité de solutions dépendant
      de p − r paramètres.

Corollaire
Si r = n = p, alors quel que soit B, le système admet une unique solution.
Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2         Pré-Ing 1 – 2023-2024   72 / 231
~~~

## Page 73

~~~text
Structure de l’ensemble des solutions


Proposition (admise)
Les solutions d’un système linéaire s’obtiennent en faisant la somme d’une
solution particulière du système avec toutes les solutions du système
homogène associé.


                                                                
 solution générale            une solution         solution générale
                     =                          +
    du système          particluière du système   du sys. homogène


Remarque. L’ensemble des solutions d’un système linéaire homogène est
un espace vectoriel, voir chapitre suivant.



Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2        Pré-Ing 1 – 2023-2024   73 / 231
~~~

## Page 74

~~~text
Exemple
Soit un système linéaire à 5 inconnues, compatible et de rang 3. Supposons
qu’après résolution (et après suppression des lignes « 0 = 0 »), on obtienne
le système :               
                           x2 = 3 + 2x1 + x3
                           
                                  x4 = 2 + x1 + 2x3
                                 
                                  x5 = −2 + 2x1 − x3 .
                                 

On a 3 inconnues principales : x2 , x4 et x5 , et 2 inconnues secondaires : x1
et x3 . L’ensemble des solutions s’écrit :
       
 S = (x1 , 3 + 2x1 + x3 , x3 , 2 + x1 + 2x3 , −2 + 2x1 − x3 ) : x1 , x3 ∈ R .

Tout élément s ∈ S peut s’écrire :

s = (0, 3, 0, 2, −2) + x1 (1, 2, 0, 1, 2) + x3 (0, 1, 1, 2, −1),             avec x1 , x3 ∈ R.
    |      {z      } |                    {z                  }
      solution particulière      solution générale du sys. homogène


Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2                Pré-Ing 1 – 2023-2024   74 / 231
~~~

## Page 75

~~~text
                                 Espaces vectoriels




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2    Pré-Ing 1 – 2023-2024   75 / 231
~~~

## Page 76

~~~text
Contenu




3   Espaces vectoriels
      Espaces et sous-espaces vectoriels
      Familles de vecteurs
      Dimension d’un espace vectoriel




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2   Pré-Ing 1 – 2023-2024   76 / 231
~~~

## Page 77

~~~text
Contenu




3   Espaces vectoriels
      Espaces et sous-espaces vectoriels
      Familles de vecteurs
      Dimension d’un espace vectoriel




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2   Pré-Ing 1 – 2023-2024   77 / 231
~~~

## Page 78

~~~text
Vecteurs géométriques (rappels de lycée)
Dans le plan ou l’espace, on définit deux opérations sur les vecteurs :
   1   l’addition vectorielle ;
   2   la multiplication par un scalaire.
Pour additionner deux vecteurs de même origine, on utilise la règle du
parallélogramme.

                                   u⃗ + ⃗v
                                                                            λ⃗
                                                                             u
                 ⃗v

                                                            u⃗
                                  u⃗

         O                                              O


Debyaoui, Dussap, Nguyen (CYU)               CM Algèbre 2    Pré-Ing 1 – 2023-2024   78 / 231
~~~

## Page 79

~~~text
Vecteurs géométriques (rappels de lycée)
      Fixons un repère de l’espace. On associe à tout vecteur un triplet
      (x, y , z) de nombres réels appelés coordonnées du vecteur.

                                             z
                                                        u⃗
                                             ⃗k
                                                  ⃗ȷ         y
                                        ⃗ı
                                    x

      Si u⃗ et ⃗v ont pour coordonnées (x, y , z) et (x ′ , y ′ , z ′ ), alors u⃗ + ⃗v et
       u (où λ ∈ R) ont pour coordonnées :
      λ⃗
                       (x + x ′ , y + y ′ , z + z ′ ) et (λx, λy , λz).
      On définit ainsi deux opérations sur R3 :
          ▶   une loi de composition interne + (addition vectorielle) ;
          ▶   une loi de composition externe · (multiplication par un scalaire).
Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2            Pré-Ing 1 – 2023-2024   79 / 231
~~~

## Page 80

~~~text
L’espace Rn

Généralisons les opérations + et · précédentes à Rn et étudions leurs
propriétés algébriques.
Définition
Sur Rn , on définit une loi de composition interne + par :

                 ∀⃗x = (x1 , . . . , xn ) ∈ Rn ,   ∀⃗y = (y1 , . . . , yn ) ∈ Rn ,
                             ⃗x + ⃗y = (x1 + y1 , . . . , xn + yn ).

Proposition (à vérifier chez vous)
(Rn , +) est un groupe commutatif, d’élément neutre ⃗0 = (0, . . . , 0), et le
symétrique d’un n-uplet (x1 , . . . , xn ) est le n-uplet (−x1 , . . . , −xn ).

Remarque. On définit l’addition de la même façon sur Cn , avec les mêmes
propriétés.

Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2                Pré-Ing 1 – 2023-2024   80 / 231
~~~

## Page 81

~~~text
Définition
Sur Rn , on définit une loi de composition externe · (application de R × Rn
dans Rn ) par :

          ∀λ ∈ R,       ∀⃗x = (x1 , . . . , xn ) ∈ Rn ,   λ · ⃗x = (λx1 , . . . , λxn ).

En pratique, le symbole de la multiplication est omis : on note λ⃗x = λ · ⃗x .

Proposition (à vérifier chez vous)
La loi · de Rn vérifie :
   1   ∀⃗x ∈ Rn , 1⃗x = ⃗x .
   2   ∀λ, µ ∈ R, ∀⃗x ∈ Rn , λ(µ⃗x ) = (λµ)⃗x .
   3   ∀λ ∈ R, ∀⃗x , ⃗y ∈ Rn , λ(⃗x + ⃗y ) = λ⃗x + λ⃗y .
   4   ∀λ, µ ∈ R, ∀⃗x , (λ + µ)⃗x = λ⃗x + µ⃗x .

Remarque. On définit la multiplication par un nombre complexe de la
même façon sur Cn , avec les mêmes propriétés.
Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2               Pré-Ing 1 – 2023-2024   81 / 231
~~~

## Page 82

~~~text
D’autres exemples de « vecteurs »

On connait d’autres objets mathématiques pour lesquels des opérations
d’addition et de multiplication par un nombre sont définies et vérifient les
mêmes propriétés que dans Rn . Par exemple :
      les fonctions définies sur un même intervalle [a, b] ;
      les polynômes à coefficients réels ;
      les suites numériques réelles ;
      . . . (cherchez si vous connaissez d’autres exemples).
Les ensembles Rn , F([a, b], R), R[X ], F(N, R), etc, sont des exemples
d’espaces vectoriels (réels).
Plus généralement, on appelle espace vectoriel n’importe quel ensemble
dans lequel sont définies des lois + et · satisfaisant les mêmes propriétés
algébriques que dans Rn .


Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2          Pré-Ing 1 – 2023-2024   82 / 231
~~~

## Page 83

~~~text
Scalaires



Jusqu’à présent, on a toujours utilisé les nombres réels comme scalaires
dans le calcul vectoriel, mais rien n’empêche d’utiliser les nombres
complexes à la place.
Définition
Dans ce chapitre, K désigne soit R, soit C. Les éléments de K sont appelés
les scalaires.
Remarque. Plus généralement, dans la plupart des énoncés de ce cours, K
peut être n’importe quel corps.




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   83 / 231
~~~

## Page 84

~~~text
Espace vectoriel

Définition
On appelle K–espace vectoriel (K–e.v.) un ensemble E dont les éléments
sont appelés vecteurs, muni d’une loi de composition interne + et d’une loi
de composition externe · (application de K × E dans E ) telles que :
  1 (E , +) est un groupe commutatif. De plus :

          ▶   l’élément neutre est noté 0E et est appelé vecteur nul de E .
          ▶   le symétrique d’un vecteur u est noté −u et est appelé vecteur opposé
              de u.
   2   La loi de composition externe vérifie :
         1    ∀u ∈ E , 1 · u = u.
         2    ∀λ, µ ∈ K, ∀u ∈ E , λ · (µ · u) = (λ × µ) · u.
         3    ∀λ ∈ K, ∀u, v ∈ E , λ · (u + v ) = (λ · u) + (λ · v ).
         4    ∀λ, µ ∈ K, ∀u ∈ E , (λ + µ) · u = (λ · u) + (µ · u).
Lorsqu’il n’y a pas d’ambiguïté sur les lois utilisées, on note simplement E
l’espace vectoriel, sinon on le note (E , +, ·).

Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2             Pré-Ing 1 – 2023-2024   84 / 231
~~~

## Page 85

~~~text
Espace vectoriel
Remarque. Dans un espace vectoriel, le vecteur nul est unique et l’opposé
d’un vecteur est unique.
Proposition
Soit E un K–espace vectoriel. Pour tout u ∈ E , on a :
   1   0 · u = 0E .
   2   (−1) · u = −u.

Démonstration.
Soit u ∈ E .
   1   0 · u = (0 + 0) · u = (0 · u) + (0 · u), donc en ajoutant −(0 · u) à
       chaque membre, on obtient 0E = 0 · u.
   2   u + ((−1) · u) = (1 · u) + ((−1) · u) = (1 + (−1)) · u = 0 · u = 0E ,
       donc (−1) · u = −u par unicité du vecteur opposé de u.

Notation. À partir de maintenant, on note λu + v le vecteur (λ · u) + v .
Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2          Pré-Ing 1 – 2023-2024   85 / 231
~~~

## Page 86

~~~text
Espace vectoriel

Exemple
      R, R2 et R3 sont des R–e.v.
      Plus généralement, Kn est un K–e.v. Le vecteur nul de Kn est le
      n-uplet (0, . . . , 0).
      C est à la fois un R–e.v. et un C–e.v. Le vecteur nul de C est le
      nombre 0.
      K[X ] et K(X ) sont des K–e.v. Le vecteur nul de K[X ] et de K(X ) est
      le polynôme nul.
      Si A est un ensemble, alors F(A, K) est un K–e.v. pour les opérations
      d’addition d’applications et de multiplication d’une application par un
      scalaire. Le vecteur nul de F(A, K) est l’application nulle (application
      constante égale à 0). En particulier :
          ▶   l’ensemble des fonctions définies sur un même intervalle est un K–e.v.
          ▶   l’ensemble des suites numériques (réelles ou complexes) est un K–e.v.

Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2           Pré-Ing 1 – 2023-2024   86 / 231
~~~

## Page 87

~~~text
Espace vectoriel produit


Proposition (à vérifier chez vous)
Soient (E1 , +1 , ·1 ), . . . , (En , +n , ·n ) des K–e.v. et soit E = E1 × · · · × En .
On définit sur E :
      une loi de composition interne + par (loi produit) :

                (u1 , . . . , un ) + (v1 , . . . , vn ) = (u1 +1 v1 , . . . , un +n vn );

      une loi de composition externe · par :

                          λ · (u1 , . . . , un ) = (λ ·1 u1 , . . . , λ ·n un );

où ui , vi ∈ Ei et λ ∈ K. Alors (E , +, ·) est un K–e.v.



Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2                Pré-Ing 1 – 2023-2024   87 / 231
~~~

## Page 88

~~~text
Combinaisons linéaires

Définition
Soit E un K–espace vectoriel. On appelle famille finie de vecteurs de E tout
n-uplet (u1 , . . . , un ) ∈ E n .

Remarque. Une famille peut comporter plusieurs fois le même vecteur et
l’ordre des vecteurs dans la famille est important.
Définition
Soit E un K–espace vectoriel et soit (u1 , . . . , un ) une famille de vecteurs.
On dit que u ∈ E est une combinaison linéaire de la famille (u1 , . . . , un ) s’il
existe des scalaires λ1 , . . . , λn ∈ K tels que :
                                 n
                                 X
                           u=          λi ui = λ1 u1 + · · · + λn un .
                                 i=1

Cette écriture est appelée décomposition de u sur la famille (u1 , . . . , un ).
Debyaoui, Dussap, Nguyen (CYU)              CM Algèbre 2            Pré-Ing 1 – 2023-2024   88 / 231
~~~

## Page 89

~~~text
Combinaisons linéaires


Exemple
Dans R3 , soient u⃗1 = (1, −1, 0), u⃗2 = (3, 1, 1) et u⃗3 = (−1, −3, −1). Alors
le vecteur ⃗v = (5, 3, 2) est combinaison linéaire de (⃗ u1 , u⃗2 , u⃗3 ). En effet, on
a par exemple ⃗v = u⃗1 + u⃗2 − u⃗3 , ou encore ⃗v = −⃗  u1 + 2⃗ u2 + 0⃗    u3 .

Remarque. La décomposition d’un vecteur sur une famille n’est pas unique
en général.

Proposition (combinaison linéaire de combinaisons linéaires)
Soit E un K–espace vectoriel et soit (u1 , . . . , un ) une famille de vecteurs. Si
v1 , . . . , vp ∈ E sont des combinaisons linéaires de (u1 , . . . , un ), alors toute
combinaison linéaire de (v1 , . . . , vp ) est une combinaison linéaire de
(u1 , . . . , un ).


Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2            Pré-Ing 1 – 2023-2024   89 / 231
~~~

## Page 90

~~~text
Combinaisons linéaires

Démonstration.
Par hypothèse, il existes des scalaires λi,k ∈ K tels que :
                                                             n
                                                             X
                                 ∀i ∈ J1, pK,         vi =         λi,k uk .
                                                             k=1
            Pp
Soit u =        i=1 αi vi une combinaison linéaire de (v1 , . . . , vp ). Alors on a :

                   p          n                       p X
                                                        n
                                              !
                   X          X                       X
            u=           αi         λi,k uk       =             αi λi,k uk
                   i=1        k=1                     i=1 k=1
                     p
                   n X                        n p                                 n
                                                                       !
                   X                          X X                                 X
               =              αi λi,k uk =                   αi λi,k       uk =         βk uk ,
                   k=1 i=1                    k=1      i=1                        k=1
            Pn
où βk =        i=1 αi λi,k pour tout k ∈ J1, nK.

Debyaoui, Dussap, Nguyen (CYU)                CM Algèbre 2                     Pré-Ing 1 – 2023-2024   90 / 231
~~~

## Page 91

~~~text
Sous-espace vectoriel



Définition
Soit (E , +, ·) un K–espace vectoriel. On dit que F est un sous-espace
vectoriel (s.e.v.) de E si :
   1   F ⊂E;
   2   (F , +, ·) est un K–espace vectoriel.

Exemple
Dans un espace vectoriel E , les ensembles {0E } et E sont des s.e.v. de E .




Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2      Pré-Ing 1 – 2023-2024   91 / 231
~~~

## Page 92

~~~text
Caractérisation d’un sous-espace vectoriel

Proposition
Soit E un K–espace vectoriel. Une partie F de E est un sous-espace
vectoriel de E si et seulement si :
   1   0E ∈ F ;
   2   F est stable par combinaisons linéaires :

                             ∀u, v ∈ F , ∀λ, µ ∈ K, λu + µv ∈ F .

Remarques.
       Noter la ressemblance avec le critère pour montrer qu’un ensemble est
       un sous-groupe (cf. chapitre 1).
       Si 0E ∈/ F , alors F ne peut pas être un sous-espace vectoriel (tout
       s.e.v. de E contient nécessairement le vecteur nul).
       En général, pour montrer qu’un ensemble F est un espace vectoriel,
       on montre que c’est un s.e.v. d’un espace vectoriel E connu.
Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2        Pré-Ing 1 – 2023-2024   92 / 231
~~~

## Page 93

~~~text
Exemple
Montrons que D = (x, y ) ∈ R2 2x − y = 0 est un s.e.v. de R2 .
                

   1   (2 × 0) − 0 = 0 donc (0, 0) ∈ D.
   2   Soient u⃗ = (x, y ) ∈ D, ⃗v = (x ′ , y ′ ) ∈ D et λ, µ ∈ R, alors x, y , x ′ , y ′
       vérifient 2x − y = 0 et 2x ′ − y ′ = 0.
       Montrons que λ⃗  u + µ⃗v ∈ D. Les composantes de ce vecteur sont
        u + µ⃗v = (λx + µx ′ , λy + µy ′ ). Calculons :
       λ⃗

              2(λx + µx ′ ) − (λy + µy ′ ) = λ(2x − y ) + µ(2x ′ − y ′ ) = 0,
                                               | {z }       | {z }
                                                       =0              =0

             u + µ⃗v ∈ D.
       donc λ⃗
Par conséquent D est un s.e.v. de R2 .

Remarque. Géométriquement, D est une droite passant par l’origine du
repère. Plus généralement, toutes les droites et les plans passant par
l’origine sont des s.e.v. de R3 .

Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2              Pré-Ing 1 – 2023-2024   93 / 231
~~~

## Page 94

~~~text
Intersection de sous-espaces vectoriels
Proposition
L’intersection de deux s.e.v. d’un K–espace vectoriel E est un s.e.v. de E .

Démonstration.
Soient F et G des s.e.v. d’un K–espace vectoriel E .
   1   0E ∈ F et 0E ∈ G car F et G sont des s.e.v. de E , donc 0E ∈ F ∩ G .
   2   Soient u, v ∈ F ∩ G et λ, µ ∈ K. Montrons que λu + µv ∈ F ∩ G :
          ▶   λu + µv ∈ F par stabilité de F par combinaisons linéaires.
          ▶   λu + µv ∈ G par stabilité de G par combinaisons linéaires.
       Donc λu + µv ∈ F ∩ G .
Par conséquent, F ∩ G est un s.e.v. de E .

Proposition
Toute intersection (finie ou infinie) de s.e.v. d’un K–espace vectoriel E est
un s.e.v. de E .
Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2          Pré-Ing 1 – 2023-2024   94 / 231
~~~

## Page 95

~~~text
Sous-espace vectoriel engendré par une famille


Proposition
Soit E un K–espace vectoriel et soit (u1 , . . . , un ) une famille de vecteurs.
L’ensemble des combinaisons linéaires de cette famille est un s.e.v. de E ,
appelé sous-espace vectoriel engendré par la famille (u1 , . . . , un ). On note
cet ensemble Vect(u1 , . . . , un ).

Démonstration.
Notons F = Vect(u1 , . . . , un ).
   1   On a 0E = 0u1 + · · · + 0un donc 0E ∈ F .
   2   Si u, v ∈ F et λ, µ ∈ K, alors λu + µv ∈ F d’après une proposition
       précédente (combinaison linéaire de combinaisons linéaires).
Par conséquent, F est un s.e.v. de E .


Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2         Pré-Ing 1 – 2023-2024   95 / 231
~~~

## Page 96

~~~text
Sous-espace vectoriel engendré par une famille
Proposition
Soit E un K–espace vectoriel et soit (u1 , . . . , un ) une famille de vecteurs.
Alors Vect(u1 , . . . , un ) est le plus petit espace vectoriel (au sens de
l’inclusion) contenant les vecteurs u1 , . . . , un . On a alors :
                                                    \
                           Vect(u1 , . . . , un ) =        F.
                                              F s.e.v. de E
                                               u1 ,...,un ∈F


Démonstration.
Soit F un s.e.v. de E contenant les vecteurs u1 , . . . , un . Montrons que
Vect(u1 , . . . , un ) ⊂ F .
Soit u ∈ Vect(u1 , . . . , un ), alors il existe λ1 , . . . , λn ∈ K tels que
u = λ1 u1 + · · · + λn un . Puisque u1 , . . . , un ∈ F et que F est un s.e.v., on a
u ∈ F (stabilité par combinaisons linéaires). Par conséquent, on a montré
que Vect(u1 , . . . , un ) ⊂ F .
Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2               Pré-Ing 1 – 2023-2024   96 / 231
~~~

## Page 97

~~~text
Sous-espace vectoriel engendré par une partie

Définition
Soient E un K–espace vectoriel et A une partie de E . L’intersection de tous
les sous-espaces de E qui contiennent A est un sous-espace vectoriel de E .
On l’appelle le sous-espace vectoriel engendré par A et on le note Vect(A).

Remarque. Si A = {u1 , . . . , un }, alors Vect(A) = Vect(u1 , . . . , un ).

Proposition
Soient E un K–espace vectoriel et A une partie de E . Alors Vect(A) est le
plus petit s.e.v. de E contenant A.

Démonstration.
Par définition, Vect(A) est un s.e.v. de E . De plus, si F est un s.e.v. qui
contient A, alors Vect(A) ⊂ F puisque Vect(A) est l’intersection de F avec
d’autres sous-espaces.

Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2           Pré-Ing 1 – 2023-2024   97 / 231
~~~

## Page 98

~~~text
Sous-espace vectoriel engendré par une partie




Proposition
Soit E un K–espace vectoriel et soient A et B des parties de E . Si A ⊂ B
alors Vect(A) ⊂ Vect(B).

Démonstration.
On a A ⊂ B ⊂ Vect(B). Ainsi, Vect(B) est un espace vectoriel qui
contient A,donc Vect(A) ⊂ Vect(B).




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2        Pré-Ing 1 – 2023-2024   98 / 231
~~~

## Page 99

~~~text
Somme de sous-espaces vectoriels
Si F et G sont des s.e.v. d’un espace vectoriel E , alors F ∪ G n’est pas un
s.e.v. en général (il n’est pas stable pour l’addition).

Exemple
Dans R2 , soient F = (x, y ) ∈ R2 y = 0 et G = (x, y ) ∈ R2 x = 0 .
                                                     

Alors F et G sont des s.e.v. de R2 , mais pas F ∪ G : on a
u⃗ = (1, 0) ∈ F ∪ G et ⃗v = (0, 1) ∈ F ∪ G , mais u⃗ + ⃗v = (1, 1) ∈
                                                                   / F ∪ G.

Proposition
Soit E un K–e.v. et soient F et G des s.e.v. de E . L’ensemble :

                          F + G = {u + v : u ∈ F et v ∈ G } ,

est le plus petit s.e.v. qui contient F ∪ G . Ce sous-espace est appelé la
somme des sous-espaces F et G .

Remarque. Autrement dit, on a F + G = Vect(F ∪ G ).
Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2        Pré-Ing 1 – 2023-2024   99 / 231
~~~

## Page 100

~~~text
Démonstration.
Notons S = F + G . Montrons que S est un s.e.v. de E .
   1   On a 0E = 0E + 0E avec 0E ∈ F et 0E ∈ G , donc 0E ∈ S.
   2   Soient w , w ′ ∈ S et λ, µ ∈ K. Alors il existe u, u ′ ∈ F et v , v ′ ∈ G tels
       que w = u + v et w ′ = u ′ + v ′ . Alors :

          λw + µw ′ = λ(u + v ) + µ(u ′ + v ′ ) = λu + µu ′ + λv + µv ′ ∈ S.
                                                  | {z } | {z }
                                                        ∈F             ∈G

Ainsi, on a montré que S est un s.e.v. de E .
Montrons à présent que F + G est le plus petit s.e.v. contenant F ∪ G ,
c’est-à-dire que F + G = Vect(F ∪ G ). On procède par double inclusion :
       On a clairement F + G ⊂ Vect(F ∪ G ).
       Puisque F ⊂ F + G et G ⊂ F + G , on a F ∪ G ⊂ F + G . Ainsi,
       F + G est un espace vectoriel qui contient F ∪ G , donc
       Vect(F ∪ G ) ⊂ F + G .
Par conséquent, F + G = Vect(F ∪ G ).
Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2           Pré-Ing 1 – 2023-2024   100 / 231
~~~

## Page 101

~~~text
Sous-espaces vectoriels en somme directe

Définition
Soit E un K–e.v. et soient F et G des s.e.v. de E . On dit que F et G sont
en somme directe si tout élément de F + G se décompose de manière
unique comme somme d’un élément de F et d’un élément de G . Dans ce
cas, on note F ⊕ G la somme de F et de G .

Exemple (contre-exemple)
Dans R3 , soient F = (x, y ) ∈ R3 x = y et G = (x, y ) ∈ R3 y = z .
                                                   

Le vecteur u⃗ = (1, 3, 2) se décompose de 2 façons différentes sur F + G :

                   u⃗ = (1, 1, 0) + (0, 2, 2) = (2, 2, 1) + (−1, 1, 1).

Proposition
Soit E un K–e.v. et soient F et G des s.e.v. de E . Alors F et G sont en
somme directe si et seulement si F ∩ G = {0E }.
Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2            Pré-Ing 1 – 2023-2024   101 / 231
~~~

## Page 102

~~~text
Sous-espaces vectoriels en somme directe



On démontre la proposition par double implication.

Démonstration ( =⇒ ).
Supposons que F et G sont en somme directe. Soit u ∈ F ∩ G , alors on a
les décompositions :

                                  u + 0E = 0E + |{z}
                             u = |{z}            u .
                                      |{z} |{z}
                                 ∈F    ∈G        ∈F   ∈G

Par unicité de la décomposition, on a u = 0E . Ainsi, F ∩ G = {0E }.




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2         Pré-Ing 1 – 2023-2024   102 / 231
~~~

## Page 103

~~~text
Sous-espaces vectoriels en somme directe


Démonstration ( ⇐= ).
Supposons que F ∩ G = {0E }. Soit u ∈ F + G , montrons que la
décomposition de u comme somme de vecteurs de F et G est unique.
Soient v , v ′ ∈ F et w , w ′ ∈ G tels que u = v + w = v ′ + w ′ . Alors :

                                 v − v′ = w′ − w,
                                 | {z } | {z }
                                  ∈F             ∈G

donc v − v ′ et w ′ − w appartiennent à F ∩ G = {0E }. Par conséquent,
v − v ′ = 0E et w ′ − w = 0E , c’est-à-dire v = v ′ et w = w ′ .Ainsi, la
décomposition de u est unique.




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2      Pré-Ing 1 – 2023-2024   103 / 231
~~~

## Page 104

~~~text
Sous-espaces supplémentaires

Définition
Soit E un K–e.v. et soient F et G des s.e.v. de E . On dit que F et G sont
supplémentaires dans E si tout vecteur de E se décompose de manière
unique comme la somme d’un vecteur de F et d’un vecteur de G :

                     ∀u ∈ E ,    ∃!(v , w ) ∈ F × G ,   u = v + w.

Proposition
Soit E un K–e.v. et soient F et G des s.e.v. de E . Alors F et G sont
supplémentaires dans E si et seulement si :
   1   F +G =E;
   2   F et G sont en somme directe.
Dans ce cas, on note F ⊕ G = E .


Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2          Pré-Ing 1 – 2023-2024   104 / 231
~~~

## Page 105

~~~text
Sous-espaces supplémentaires

Démonstration.
Le point 1 est équivalent à l’existence d’une décomposition des vecteurs de
E comme somme de vecteurs de F et de G , et le point 2 est équivalent à
l’unicité d’une telle décomposition.

Exemple
Dans R3 , tout plan F passant par (0, 0, 0) et toute droite G non contenue
dans F passant par (0, 0, 0) sont supplémentaires.
                                                 G

                                                      u⃗
                                             ⃗
                                             w

                                        ⃗0
                                 F               ⃗v


Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2          Pré-Ing 1 – 2023-2024   105 / 231
~~~

## Page 106

~~~text
Contenu




3   Espaces vectoriels
      Espaces et sous-espaces vectoriels
      Familles de vecteurs
      Dimension d’un espace vectoriel




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2   Pré-Ing 1 – 2023-2024   106 / 231
~~~

## Page 107

~~~text
Familles génératrices



Définition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille de vecteurs de E . On dit
que (u1 , . . . , un ) est une famille génératrice de E (ou que u1 , . . . , un
engendrent E ) si tout vecteur de E est combinaison linéaire des vecteurs
u1 , . . . , un , c’est-à-dire si Vect(u1 , . . . , un ) = E .

Exemple
Les vecteurs (1, 0, 0), (0, 1, 0) et (0, 0, 1) engendrent R3 , de même que les
vecteurs (1, 0, 0), (1, 1, 0) et (1, 1, 1).




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   107 / 231
~~~

## Page 108

~~~text
Familles génératrices


Proposition
Soit E un K–e.v. Toute sur-famille d’une famille génératrice de E est
génératrice.

Démonstration.
Si un vecteur est combinaison linéaire d’une famille (u1 , . . . , un ), il est à
fortiori combinaison linéaire de la famille (u1 , . . . , un , un+1 , . . . , un+p ).

Proposition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille génératrice de E . Alors
(u1 , . . . , up−1 , up+1 , . . . , un ) est une famille génératrice de E si et
seulement si up ∈ Vect(u1 , . . . , up−1 , up+1 , . . . , un ).


Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2            Pré-Ing 1 – 2023-2024   108 / 231
~~~

## Page 109

~~~text
Familles génératrices


Démonstration.
On procède par double implication.

( =⇒ ) Supposons que (u1 , . . . , up−1 , up+1 , . . . , un ) est génératrice.
Puisque up ∈ E , alors up est combinaison linéaire de
(u1 , . . . , up−1 , up+1 , . . . , un ) par définition d’une famille génératrice.

( ⇐= ) Supposons que up est combinaison linéaire de
(u1 , . . . , up−1 , up+1 , . . . , un ). Les vecteurs u1 , . . . , un sont combinaisons
linéaires de (u1 , . . . , up−1 , up+1 , . . . , un ), donc toute combinaison linéaire
de (u1 , . . . , un ), c.-à-d. tout élément de E , est combinaison linéaire de
(u1 , . . . , up−1 , up+1 , . . . , un ) d’après une proposition précédente
(combinaison linéaire de combinaisons linéaires).


Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2             Pré-Ing 1 – 2023-2024   109 / 231
~~~

## Page 110

~~~text
Familles liées


Proposition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille de vecteurs de E . Les
assertions suivantes sont équivalentes :
   1   L’un des vecteurs ui est combinaison linéaire des autres.
   2   Il existe λ1 , . . . , λn ∈ K non tous nuls tels que λ1 u1 + · · · + λn un = 0E .
Dans ce cas, on dit que la famille (u1 , . . . , un ) est liée.

Remarques.
   1   Toute famille contenant le vecteur nul est liée.
   2   Une famille (u, v ) est liée si et seulement si u et v sont colinéaires.




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2            Pré-Ing 1 – 2023-2024   110 / 231
~~~

## Page 111

~~~text
Familles liées



Démonstration de (1 =⇒ 2).
Supposons que ui0 ∈ Vect({ui : i ̸= i0 }). Alors il existe des scalaires λi ∈ K
tels que :
                                    X n
                             ui0 =        λ i ui .
                                          i=1
                                          i̸=i0

Par conséquent :

     λ1 u1 + · · · + λi0 −1 ui0 −1 + (−1)ui0 + λi0 +1 ui0 +1 + · · · + λn un = 0E .




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2            Pré-Ing 1 – 2023-2024   111 / 231
~~~

## Page 112

~~~text
Familles liées



Démonstration de (2 =⇒ 1).
Supposons qu’il existe λ1 , . . . , λn ∈ K non tous nuls tels que :

                                    λ1 u1 + · · · + λn un = 0E .

Soit i0 tel que λi0 ̸= 0, alors on a :
                           n                                 n       
                           X                                 X    λi
               λi0 ui0 =           (−λi )ui ,     donc ui0 =    −       ui .
                                                                  λi0
                           i=1                                 i=1
                           i̸=i0                               i̸=i0




Debyaoui, Dussap, Nguyen (CYU)                  CM Algèbre 2           Pré-Ing 1 – 2023-2024   112 / 231
~~~

## Page 113

~~~text
Familles libres

Définition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille de vecteurs de E . On dit
que la famille est libre si elle n’est pas liée. On dit alors que les vecteurs
u1 , . . . , un sont linéairement indépendants.

Proposition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille de vecteurs de E . Les
assertions suivantes sont équivalentes :
   1   La famille (u1 , . . . , un ) est libre.
   2   Aucun vecteur de la famille n’est combinaison linéaire des autres.
   3   ∀λ1 , . . . , λn ∈ K, (λ1 u1 + · · · + λn un = 0E =⇒ λ1 = · · · = λn = 0).

Démonstration.
Prendre la négation des assertions de la proposition précédente.
Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2     Pré-Ing 1 – 2023-2024   113 / 231
~~~

## Page 114

~~~text
Familles libres

Exemple
Dans R4 , soient u⃗1 = (1, 1, 0, 2), u⃗2 = (1, 2, −2, 1) et u⃗3 = (2, 0, −1, 1).
Cherchons si (⃗u1 , u⃗2 , u⃗3 ) est libre. Soient λ1 , λ2 , λ3 ∈ R tels que :

                                 λ1 u⃗1 + λ2 u⃗2 + λ3 u⃗3 = ⃗0.

Cette égalité est équivalente au système linéaire :
                          
                           λ1 + λ2 + 2λ3 = 0
                          
                          
                           λ + 2λ
                          
                                              =0
                               1      2
                          
                          
                                − 2λ2 − λ3 = 0
                          
                          2λ + λ + λ = 0.
                                       1       2          3

En résolvant ce système (p. ex. pivot de Gauss), on trouve que l’unique
solution est λ1 = λ2 = λ3 = 0. Ainsi, la famille (⃗
                                                  u1 , u⃗2 , u⃗3 ) est libre.

Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2           Pré-Ing 1 – 2023-2024   114 / 231
~~~

## Page 115

~~~text
Familles libres




Proposition (à faire chez vous)
Toute sous-famille d’une famille libre est libre.

Proposition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille libre. Soit u ∈ E , alors la
famille (u1 , . . . , un , u) est libre si et seulement si u ∈
                                                             / Vect(u1 , . . . , un ).




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2            Pré-Ing 1 – 2023-2024   115 / 231
~~~

## Page 116

~~~text
Familles libres
Démonstration.
On procède par double implication.
      ( =⇒ ) Par contraposée, si u ∈ Vect(u1 , . . . , un ) alors la famille
      (u1 , . . . , un , u) est liée.

      ( ⇐= ) Par contraposée, supposons que (u1 , . . . , un , u) est liée. Alors
      il existe λ1 , . . . , λn , λ ∈ K non tous nuls tels que :

                                 λ1 u1 + · · · + λn un + λu = 0E .                        (∗)

      Si on avait λ = 0, alors (∗) serait une combinaison linéaire nulle de la
      famille (u1 , . . . , un ), donc par liberté de cette famille, tous les λi
      seraient nuls, contradiction. Par conséquent, λ ̸= 0 et on a :
                              n      
                              X    λi
                           u=    −      ui ∈ Vect(u1 , . . . , un ).
                                   λ
                                 i=1

Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2          Pré-Ing 1 – 2023-2024   116 / 231
~~~

## Page 117

~~~text
Bases

Définition
Soit E un K–e.v. et soit (u1 , . . . , un ) une famille de vecteurs de E . On dit
que (u1 , . . . , un ) est une base de E si c’est famille à la fois libre et
génératrice.

Exemple
   1   Dans Kn , les vecteurs :

        e⃗1 = (1, 0 . . . , 0),   e⃗2 = (0, 1, 0, . . . , 0),   ... ,      e⃗n = (0, . . . , 0, 1),

       forment une base appelée la base canonique de Kn .
   2   Dans Kn [X ], les polynômes 1, X , X 2 , . . . , X n forment une base appelée
       la base canonique de Kn [X ].
       Si a ∈ K, alors les polynômes 1, X − a, (X − a)2 , . . . , (X − a)n forment
       également une base de Kn [X ] (formule de Taylor).

Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2                 Pré-Ing 1 – 2023-2024   117 / 231
~~~

## Page 118

~~~text
Bases


Exemple
Dans R4 , soit F = (x, y , z, t) ∈ R4 2x − y + z + 3t = 0 . Alors F est
                    

un s.e.v. de R4 . Cherchons une base de F . Soit u⃗ = (x, y , z, t) ∈ R4 , on a :

                       u⃗ ∈ F ⇐⇒ 2x − y + z + 3t = 0
                                 ⇐⇒ y = 2x + z + 3t
                                 ⇐⇒ u⃗ = (x, 2x + z + 3t, z, t)
                                 ⇐⇒ u⃗ = x u⃗1 + z u⃗2 + t u⃗3 ,

avec u⃗1 = (1, 2, 0, 0), u⃗2 = (0, 1, 1, 0) et u⃗3 = (0, 3, 0, 1). Ainsi, on a
F = Vect(⃗  u1 , u⃗2 , u⃗3 ), c.-à-d. la famille (⃗
                                                  u1 , u⃗2 , u⃗3 ) est génératrice de F . On
vérifie facilement qu’elle est libre (le vérifier !), donc c’est une base de F .



Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2             Pré-Ing 1 – 2023-2024   118 / 231
~~~

## Page 119

~~~text
Coordonnées d’un vecteur dans une base




Théorème
Soit E un K–e.v. et soit (u1 , . . . , un ) une base de E . Alors tout vecteur de
E s’écrit de manière unique comme combinaison linéaire de (u1 , . . . , un ) :

            ∀u ∈ E ,      ∃!(λ1 , . . . , λn ) ∈ Kn ,     u = λ1 u1 + · · · + λn un .

Cet unique n-uplet (λ1 , . . . , λn ) ∈ Kn est appelé les coordonnées de u dans
la base (u1 , . . . , un ).




Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2               Pré-Ing 1 – 2023-2024   119 / 231
~~~

## Page 120

~~~text
Coordonnées d’un vecteur dans une base



Démonstration.
Une base est une famille génératrice, donc tout vecteur de E s’écrit comme
combinaison linéaire de (u1 , . . . , un ). Il reste à montrer l’unicité de cette
combinaison. Soit u ∈ E et soient λ1 , . . . , λn , µ1 , . . . , µn ∈ K tels que :

                    u = λ1 u1 + · · · + λn un = µ1 u1 + · · · + µn un .

Alors on a (λ1 − µ1 )u1 + · · · + (λn − µn )un = 0E . Puisque la famille
(u1 , . . . , un ) est libre, tous les coefficients de cette combinaison linéaire
sont nuls, c.-à-d. λi = µi pour tout i, d’où l’unicité.




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2            Pré-Ing 1 – 2023-2024   120 / 231
~~~

## Page 121

~~~text
Familles infinies de vecteurs


Définition
Soit E un K–e.v.
      Une famille infinie de vecteurs de E est une famille (ui )i∈I où I est un
      ensemble infini.
      On dit qu’un vecteur u ∈ E est combinaison linéaire de (ui )i∈I si u est
      combinaison linéaire d’une sous-famille finie de (ui )i∈I , c.-à-d. s’il
      existe i1 , . . . , in ∈ I tels que u est combinaison linéaire de (ui1 , . . . , uin ).

Attention !
En algèbre linéaire, on ne manipule que des sommes finies de vecteurs.




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2              Pré-Ing 1 – 2023-2024   121 / 231
~~~

## Page 122

~~~text
Familles infinies de vecteurs

Définition
Soit E un K–e.v. et soit (ui )i∈I une famille infinie de vecteurs de E .
      On dit que (ui )i∈I est une famille génératrice si tout vecteur de E est
      combinaison linéaire de (ui )i∈I , c’est-à-dire si :

                    ∀u ∈ E ,      ∃i1 , . . . , in ∈ I ,     u ∈ Vect(ui1 , . . . , uin ).

      On dit que (ui )i∈I est une famille libre si toute sous-famille finie de
      (ui )i∈I est libre, c’est-à-dire si :

                           ∀i1 , . . . , in ∈ I ,   (ui1 , . . . , uin ) est libre.

Exemple
Dans K[X ], la famille (X n )n∈N est libre et génératrice : c’est une base de
K[X ] appelée la base de canonique de K[X ].

Debyaoui, Dussap, Nguyen (CYU)                CM Algèbre 2                 Pré-Ing 1 – 2023-2024   122 / 231
~~~

## Page 123

~~~text
Contenu




3   Espaces vectoriels
      Espaces et sous-espaces vectoriels
      Familles de vecteurs
      Dimension d’un espace vectoriel




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2   Pré-Ing 1 – 2023-2024   123 / 231
~~~

## Page 124

~~~text
Espace vectoriel de dimension finie

Définition
Soit E un K–e.v. On dit que E est de dimension finie s’il existe une famille
génératrice finie de E . Sinon, on dit que E est de dimension infinie.

Lemme (admis)
Soit E un K–e.v. Si E possède une famille libre de p vecteurs et une famille
génératrice de m vecteurs, alors p ≤ m (la taille d’une famille libre est
toujours inférieure à la taille d’une famille génératrice).

Exemple
   1   Kn est dimension finie.
   2   Kn [X ] est de dimension finie.
   3   K[X ] est dimension infinie (car il possède une famille libre infinie, donc
       aucune famille génératrice ne peut être finie d’après le lemme).
Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2          Pré-Ing 1 – 2023-2024   124 / 231
~~~

## Page 125

~~~text
Existence de bases

Théorème (de la base incomplète)
Soit E un K–e.v. de dimension finie. Si (u1 , . . . , up ) est une famille libre et
si (vi )i∈I est une famille génératrice (finie ou infinie) de E , alors il existe
une base de E de la forme :

                                 (u1 , . . . , up , vi1 , . . . , vin ),

(avec n = 0 si (u1 , . . . , up ) est déjà une base de E ).

Corollaire
Soit E un K–e.v. non nul de dimension finie.
   1   Il existe une base de E .
   2   De toute famille génératrice (vi )i∈I de E , on peut extraire une base
       (vi1 , . . . , vin ).

Debyaoui, Dussap, Nguyen (CYU)               CM Algèbre 2                  Pré-Ing 1 – 2023-2024   125 / 231
~~~

## Page 126

~~~text
Existence de bases
Démonstration du théorème de la base incomplète.
On construit par récurrence une suite de familles libres par ajouts successifs
de vecteurs de la famille (vi )i∈I , en s’arrêtant quand on obtient une base.
      Posons L0 = (u1 , . . . , up ). C’est une famille libre par hypothèse.
      Soit n ∈ N. Supposons que Ln = (u1 , . . . , up , vi1 , . . . , vin ) est libre. Si
      Ln est génératrice, alors c’est une base ; le théorème est démontré.
      Sinon, il existe in+1 ∈ I tel que vin+1 ∈       / Vect(u1 , . . . , up , vi1 , . . . , vin ).
      Posons Ln+1 = (u1 , . . . , up , vi1 , . . . , vin , vin+1 ). Cette famille est libre
      d’après une proposition précédente.
Montrons qu’il existe n tel que Ln soit une base de E . Par l’absurde, si ce
n’était pas le cas, on aurait une suite (Ln )n∈N de familles libres de tailles
strictement croissantes. Or d’après le lemme précédent, la taille d’une
famille libre est toujours inférieure à la taille d’une famille génératrice de E .
Puisque E est de dimension finie, la taille des familles libres est majorée,
donc elle ne peut pas croître indéfiniment ; contradiction.
Debyaoui, Dussap, Nguyen (CYU)              CM Algèbre 2                Pré-Ing 1 – 2023-2024   126 / 231
~~~

## Page 127

~~~text
Dimension d’un espace vectoriel



Théorème
Si E est un K–e.v. non nul de dimension finie, alors toutes les bases de E
ont le même nombre de vecteurs. Ce nombre est appelé la dimension de E
et on le note dim(E ). Si E = {0E }, on convient que dim(E ) = 0.

Démonstration.
Soient B et B ′ deux bases de E , de tailles respectives n et n′ . Puisque B
est une famille libre et que B ′ est une famille génératrice, on a n ≤ n′ . En
échangeant les rôles de B et B ′ , on obtient l’inégalité contraire n′ ≤ n. Par
conséquent, n = n′ .




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2           Pré-Ing 1 – 2023-2024   127 / 231
~~~

## Page 128

~~~text
Dimension d’un espace vectoriel


Exemple
   1   dim(Kn ) = n.
   2   dim(Kn [X ]) = n + 1.
   3   dim(C) = 2 si C est vu comme un R–e.v.mais dim(C) = 1 si C est vu
       comme un C–e.v.

Proposition
Soit E un K–e.v. de dimension n et soit F une famille de p vecteurs de E .
   1   Si F est libre alors p ≤ n, avec égalité si et seulement si F est une
       base de E .
   2   Si F est génératrice alors p ≥ n, avec égalité si et seulement si F est
       une base de E .


Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2         Pré-Ing 1 – 2023-2024   128 / 231
~~~

## Page 129

~~~text
Dimension d’un sous-espace vectoriel

Proposition (admis)
Soit E un K–e.v. de dimension finie. Si F est un s.e.v. de E , alors F est de
dimension finie et dim(F ) ≤ dim(E ). De plus, dim(F ) = dim(E ) si et
seulement si F = E .

Définition
Soit E un K–e.v. de dimension n et soit F un s.e.v. de E .
      Si dim(F ) = 1, on dit que F est une droite vectorielle de E .
      Si dim(F ) = 2, on dit que F est un plan vectoriel de E .
      Si dim(F ) = n − 1, on dit que F est un hyperplan vectoriel de E .

Exemple
Dans R4 , soit F = (x, y , z, t) ∈ R4 2x − y + z + 3t = 0 . On a vu
                  

précédemment que F possède une base de 3 vecteurs, donc dim(F ) = 3.
Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   129 / 231
~~~

## Page 130

~~~text
Rang d’une famille de vecteurs




Définition
Soit E un K–e.v. et soient (u1 , . . . , un ) une famille de vecteurs. On appelle
rang de (u1 , . . . , un ), et on note rg(u1 , . . . , un ), la dimension (finie) du
s.e.v. Vect(u1 , . . . , un ).

Remarque. Le rang d’une famille est le nombre maximal de vecteurs
linéairement indépendants de cette famille.




Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2           Pré-Ing 1 – 2023-2024   130 / 231
~~~

## Page 131

~~~text
Dimension d’une somme


Théorème (formule de Grassmann)
Soient F et G des s.e.v. de dimensions finies d’un K–e.v. Alors :

                  dim(F + G ) = dim(F ) + dim(G ) − dim(F ∩ G ).

Corollaire
Soient F et G des s.e.v. de dimensions finies d’un K–e.v. Alors :

                            dim(F + G ) ≤ dim(F ) + dim(G ),

avec égalité si et seulement si F et G sont somme directe.




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2        Pré-Ing 1 – 2023-2024   131 / 231
~~~

## Page 132

~~~text
Caractérisation des supplémentaires en dimension finie




Proposition
Soit E un K–e.v. de dimension finie et soient F et G des s.e.v. de E . Les
assertions suivantes sont équivalentes :
   1   E = F ⊕ G (c.-à-d. F et G sont supplémentaires dans E ).
   2   dim(E ) = dim(F ) + dim(G ) et F ∩ G = {0E }.
   3   dim(E ) = dim(F ) + dim(G ) et E = F + G .




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2         Pré-Ing 1 – 2023-2024   132 / 231
~~~

## Page 133

~~~text
Caractérisation des supplémentaires en dimension finie


Démonstration.
On montre que 1 =⇒ 2 =⇒ 3 =⇒ 1.

(1 =⇒ 2) Si E = F ⊕ G , alors dim(E ) = dim(F ) + dim(G ) d’après la
formule de Grassmann. De plus, F et G sont en somme directe donc
F ∩ G = {0E }.

(2 =⇒ 3) Si dim(E ) = dim(F ) + dim(G ) et F ∩ G = {0E }, alors d’après
la formule de Grassmann, on a dim(E ) = dim(F + G ), donc E = F + G .

(3 =⇒ 1) Si dim(E ) = dim(F ) + dim(G ) et E = F + G , alors d’après la
formule de Grassmann, on a dim(F ∩ G ) = 0, donc F ∩ G = {0E }. Par
conséquent F et G sont en somme directe, d’où E = F ⊕ G .



Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2      Pré-Ing 1 – 2023-2024   133 / 231
~~~

## Page 134

~~~text
Existence de supplémentaires

Proposition
Soit E un K–e.v. de dimension finie et soit F un s.e.v. de E . Alors il existe
un s.e.v. G tel que F et G sont supplémentaires dans E .

Démonstration.
Posons n = dim(E ). Soit (e1 , . . . , ep ) une base de F , que l’on complète
avec des vecteurs ep+1 , . . . , en tels que (e1 , . . . , en ) soit une base de E .
Posons G = Vect(ep+1 , . . . , en ). On a donc dim(F ) = p et
dim(G ) = n − p, d’où dim(E ) = dim(F ) + dim(G ). Enfin, pour tout
vecteur u ∈ E , il existe λ1 , . . . , λn ∈ K tels que :

                 u = λ1 e1 + · · · + λp ep + λp+1 ep+1 + · · · + λn en ,
                     |        {z         } |           {z            }
                                 ∈F                      ∈G

donc E = F + G . D’après la proposition précédente, E = F ⊕ G .

Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2            Pré-Ing 1 – 2023-2024   134 / 231
~~~

## Page 135

~~~text
                                 Applications linéaires




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2      Pré-Ing 1 – 2023-2024   135 / 231
~~~

## Page 136

~~~text
Contenu




4   Applications linéaires
      Définitions et propriétés
      Applications linéaires particulières
          Formes linéaires
          Endomorphisme
          Isomorphisme
          Automorphisme
       Noyau et image d’une application linéaire
          Feuille d’exercices-Espaces vectoriels et sous-espaces vectoriels




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2              Pré-Ing 1 – 2023-2024   136 / 231
~~~

## Page 137

~~~text
Contenu




4   Applications linéaires
      Définitions et propriétés
      Applications linéaires particulières
          Formes linéaires
          Endomorphisme
          Isomorphisme
          Automorphisme
       Noyau et image d’une application linéaire
          Feuille d’exercices-Espaces vectoriels et sous-espaces vectoriels




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2              Pré-Ing 1 – 2023-2024   137 / 231
~~~

## Page 138

~~~text
Définitions


Définition
Soient (E , +, .) et (F , +, .) deux K-espaces vectoriels.
On dit que f : E → F est linéaire (ou est un morphisme d’espace vectoriel)
si :
 (1) ∀x, y ∈ E , on a f (x + y ) = f (x) + f (y ) ;
 (2) ∀λ ∈ K, ∀x ∈ E , on a f (λx) = λf (x).
On note L (E , F ) l’ensemble des applications de E dans F .

Proposition (Caractérisation usuelle des applications linéaires)
Soit f : E → F . L’application f est linéaire, si et seulement si , ∀λ, ∈ K,
∀x, y ∈ E , f (λx + y ) = λf (x) + f (y ).



Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2         Pré-Ing 1 – 2023-2024   138 / 231
~~~

## Page 139

~~~text
Exemple
Soit f : E → F définie par f : x 7→ 0F . L’application f est linéaire.

Proposition
Soient E , E1 , . . . En , (n ∈ N∗ ) des K espaces vectoriels. L’application

                            f    : E     →   E1 × · · · × En
                                   x   7 → (f1 (x), . . . , fn (x)).

f est linéaire de E dans E1 × · · · × En , si et seulement si, f1 , . . . , fn sont des
applications linéaires de respectivement de E dans E1 , . . . , de E dans En .




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2                  Pré-Ing 1 – 2023-2024   139 / 231
~~~

## Page 140

~~~text
Exemple
Montrons que f : R2 → R3 définie par f (x, y ) = (x + y , x − y , 2y ) est une
application linéaire. Soient λ, ∈ R, et a = (x, y ), b = (x ′ , y ′ ) ∈ R2 ,

      f (λa + b) = f (λx + x ′ , λy + y ′ )
                      = (λx + x ′ + λy + y ′ , λx + x ′ − λy − y ′ , 2λy + 2y ′ )
                      = λ(x + y , x − y , 2y ) + (x ′ + y ′ , x ′ − y ′ , 2y ′ )
                      = λf (a) + f (b).




Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2              Pré-Ing 1 – 2023-2024   140 / 231
~~~

## Page 141

~~~text
Proposition
Soient (E , +, .), (F , +, .), (G , +, .) des K- espaces vectoriels.
 (1) Si l’application f : E → F est linéaire alors f (0E ) = 0F ;
 (2) Si f : E → F et g : F → G sont linéaires alors g ◦ f : E → G est
     linéaire.
 (3) Si u1 , . . . , un sont des vecteurs de E alors ∀λ1 , . . . , λn ∈ K :
                                   n             n
                                           !
                                  X             X
                              f       λk uk =       λk f (uk ).
                                 k=1                  k=1




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2           Pré-Ing 1 – 2023-2024   141 / 231
~~~

## Page 142

~~~text
Contenu




4   Applications linéaires
      Définitions et propriétés
      Applications linéaires particulières
          Formes linéaires
          Endomorphisme
          Isomorphisme
          Automorphisme
       Noyau et image d’une application linéaire
          Feuille d’exercices-Espaces vectoriels et sous-espaces vectoriels




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2              Pré-Ing 1 – 2023-2024   142 / 231
~~~

## Page 143

~~~text
Formes linéaires


Définition
On appelle forme linéaire sur un K-espace vectoriel E , toute application
linéaire de E dans K. On note E ∗ , au lieu de L (E , K), l’ensemble des
formes linéaires sur E .

Exemple
Pour a1 , . . . , an ∈ K fixé, l’application f : Kn → K définie par
f : (x1 , . . . , xn ) 7→ a1 x1 + · · · + an xn est une forme linéaire sur Kn . En effet,
c’est une application de Kn vers K et c’est aussi une application linéaire car
on vérifie aisement que ∀λ, ∈ K, ∀x, y ∈ Kn , on a
f (λx + y ) = λf (x) + f (y ).




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2            Pré-Ing 1 – 2023-2024   143 / 231
~~~

## Page 144

~~~text
Endomorphisme


Définition
On appelle endomorphisme de E , toute applicatin linéaire de E dans lui
même. On note L (E ) ou End(E ), au lieu de L (E , E ), l’ensemble des
endomorphismes de E .

Exemple
L’application identité IdE : E → E est un endomorphisme de E .

Proposition
Si f et g deux endomorphismes de E , alors g ◦ f est aussi un
endomorphisme de E .



Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2        Pré-Ing 1 – 2023-2024   144 / 231
~~~

## Page 145

~~~text
Isomorphisme


Définition
On appelle isomorphisme d’un K espace vectoriel E vers un K-espace
vectoriel F toute application linéaire bijective de E vers F . On note
iso(E , F ) l’ensemble des isomorphismes de E dans F .

Exemple
L’application f : R2 → C définie par f (a, b) = a + ib est un isomorphisme
de R-espace vectoriel. En effet, cette application est R-linéaire et bijective.

Proposition
Si f : E → F et g : F → G sont des isomorphismes alors la composée
g ◦ f : E → G est un isomorphisme.


Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2          Pré-Ing 1 – 2023-2024   145 / 231
~~~

## Page 146

~~~text
Proposition
Si f : E → F est un isomorphisme alors son application réciproque
f −1 : F → E est un isomorphisme.

Exemple
L’application g : C → R2 définie par g : z 7→ (ℜ(z), ℑ(z)) est
l’isomorphisme réciproque de l’application f : (a, b) ∈ R2 7→ a + ib ∈ C.




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2          Pré-Ing 1 – 2023-2024   146 / 231
~~~

## Page 147

~~~text
Automorphisme


Définition
On appelle automorphisme de E , tout endomorphisme bijectif de E . On
note Gl(E ) l’ensemble d’automorphisme de E .

Proposition
Si f : E → E et g : E → E sont des automorphismes de E alors la
composée g ◦ f : E → E est un automorphisme.

Proposition
Si f : E → E est un automorphisme alors son application réciproque
f −1 : E → E est un automorphisme.



Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2       Pré-Ing 1 – 2023-2024   147 / 231
~~~

## Page 148

~~~text
Contenu




4   Applications linéaires
      Définitions et propriétés
      Applications linéaires particulières
          Formes linéaires
          Endomorphisme
          Isomorphisme
          Automorphisme
       Noyau et image d’une application linéaire
          Feuille d’exercices-Espaces vectoriels et sous-espaces vectoriels




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2              Pré-Ing 1 – 2023-2024   148 / 231
~~~

## Page 149

~~~text
Théorème
Soit f : E → F une application linéaire.
   1   Si V est un sous-espace vectoriel de E alors f (V ) est un sous-espace
       vectoriel de F .
   2   Si W est un sous-espace vectoriel de F alors f −1 (W ) est un
       sous-espace vectoriel de E .




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   149 / 231
~~~

## Page 150

~~~text
Noyau et image d’une application linéaire

Définition
Soit f : E → F une application linéaire.
 (1) On appelle image de f l’espace Im f = f (E ) = {f (x), x ∈ E }.
 (2) On appelle noyau de f l’espace
     ker f = f −1 ({0F }) = {x ∈ E | f (x) = 0F }.

Proposition
 (1) Im f est un sous-espace vectoriel de F .
 (2) ker f est un sous-espace vectoriel de E .

Théorème
Si f : E → F est une application linéaire alors
 (1) f est surjective, si et seulement si, Im f = F
 (2) f est injective, si et seulement si, ker f = {0E }.
Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2            Pré-Ing 1 – 2023-2024   150 / 231
~~~

## Page 151

~~~text
Remarque
 (1) Pour déterminer l’image d’une application linéaire f , on détermine les
     valeurs prises par f , i.e., les y ∈ F tels qu’il existe x ∈ E pour lequel
     y = f (x). En pratique, l’image de f est engendré par l’image d’une
     base de E . C’est-à-dire pour toute B = (u1 , . . . , un ) une base de E

                                 Im(f ) = Vect (f (u1 ), . . . , f (un ))

 (2) Pour déterminer le noyau d’une application linéaire f , on résout
     l’equation f (x) = 0F d’inconnue x ∈ E .




Debyaoui, Dussap, Nguyen (CYU)              CM Algèbre 2              Pré-Ing 1 – 2023-2024   151 / 231
~~~

## Page 152

~~~text
Rang




Définition
Soient E et F deux K-espaces vectoriels et f ∈ L (E , F ). On appelle Rang
de f la dimension du sous-espaces vectoriel Im(f ). On le note rg (f ).

Corollaire
Pour toute application linéaire f de L (E , F ). On a rg (f ) ⩽ dim(E ).




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   152 / 231
~~~

## Page 153

~~~text
Exemple
Déterminons le noyau et l’image de l’application linéaire f : R2 → R2
définie par f : (x, y ) 7→ (x − y , x + y ). On a :

                                 ker f = {(0, 0)}
      Im f = {(x, x) + (−y , y ) | x, y ∈ R} = Vect ((1, 1), (−1, 1)) = R2 .




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2          Pré-Ing 1 – 2023-2024   153 / 231
~~~

## Page 154

~~~text
Théorème du rang




Théorème (Théorème du rang)
Soient E et F deux K-espaces vectoriels et f de E dans F linéaire. On a

                                 dim(E ) = dim(ker(f )) + rg (f )




Debyaoui, Dussap, Nguyen (CYU)              CM Algèbre 2            Pré-Ing 1 – 2023-2024   154 / 231
~~~

## Page 155

~~~text
Exercice 1.
Soit E un R-espace vectoriel.
On munit le produit cartésien E × E de l’addition usuelle :
(x, y ) + (x ′ , y ′ ) = (x + x ′ , y + y ′ ) et de la multiplication externe ∗ par les
complexes définie par : (a + i.b) ∗ (x, y ) = (a.x − b.y , a.y + b.x).
Montrer que E × E est alors un C-espace vectoriel.
Celui-ci est appelé complexifié de E .
Exercice 2. Soit R∗+ muni de la loi interne définie par
a ⊕ b = a.b, ∀a, b ∈ R∗+ et de la loi externe ⊗ telle que :
λ ⊗ a = aλ , ∀a ∈ R∗+ , ∀λ ∈ R.
Montrer que (R∗+ , ⊕, ⊗) est un R-espace vectoriel.
Exercice 3. Sur R2 , on définit les deux lois suivantes : pour tous
(x, y ), (x ′ , y ′ ) ∈ R2 et ∀λ ∈ R, on pose
    (x, y ) + (x ′ , y ′ ) = (x + x ′ , y + y ′ )   et      λ ⋆ (x, y ) = (λx, 0).
Le triplet (R2 , +, ⋆) est-il un espace vectorielsur R ?
Exercice 4. Les parties suivantes sont-elles des sous-espaces vectoriels de
R2 ?
 (a) {(x,
Debyaoui, Dussap, ∈ R2 |(CYU)
              y ) Nguyen  x ⩽ y} ;   CM Algèbre 2        Pré-Ing 1 – 2023-2024 155 / 231
~~~

## Page 156

~~~text
                       Matrices et inverses de matrices




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2     Pré-Ing 1 – 2023-2024   156 / 231
~~~

## Page 157

~~~text
Contenu



5   Matrices et inverses de matrices
          Définition
          (Mn,p (K), +, .) est un K-espace vectoriel
          Opérations
          Dimension
          Sous-espaces des matrices diagonales et triangulaires
          Propriétés du produit matriciel
          Puissance d’une matrice
       Matrices inversibles
          Détermination pratique de l’inverse d’une matrice carrée inversible




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2              Pré-Ing 1 – 2023-2024   157 / 231
~~~

## Page 158

~~~text
Définition

Définition
Soient n, p ∈ N∗ . On appelle matrice à n lignes et p colonnes à coefficients
dans K, un tableau à n lignes et p colonnes d’éléments de K. On note une
telle matrice
                                                          
                                      a11 a12 · · · a1P
                                   a21 a22 · · · a2p 
              M = (aij ) 1≤i≤n =  .         .. . .     ..  .
                                                          
                         1≤j≤p     ..        .     .    . 
                                      an1 an2 · · · anp

   • On dit que M est une matrice colonne si p = 1.
   • On dit que M est une matrice ligne si n = 1.
   • On dit que M est une matrice carrée si n = p.


Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2          Pré-Ing 1 – 2023-2024   158 / 231
~~~

## Page 159

~~~text
Notation :



   • On note Mn,p (K) l’ensemble des matrices à n lignes et p colonnes à
     coefficients dans K.
   • Si p = n, on note Mn (K) l’ensemble des matrices carrées à n lignes et
     à n colonnes.
   • Un élément de Mn (K) est dit matrice carrée de taille n.
   • Soit M = (aij ) 1≤i≤n , alors aij est le coefficient situé sur la i ième
                           1≤j≤p

      ligne et la j ième colonne de la matrice M.




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   159 / 231
~~~

## Page 160

~~~text
Matrice triangulaire supérieure



Définition
Soit M = (aij )1≤i,j≤n une matrice carrée de taille n. On dit que :
M est une matrice triangulaire supérieure (resp. triangulaire strictement
supérieure) si aij = 0 pour tout i > j (resp. i ≥ j). C’est-à-dire :
                                                                       
                                                   0 a12 · · ·      a1n
                               
           a11 a12 · · · a1n
        0 a22 · · · a2n                        .. . . . .         .. 
                                                 .      .     .      . 
  M= .                      .     , (resp.M =                         ).
                               
        ..       .    .
                    .. ..    .. 
                                                  .        ..
                                                 ..           . an−1,n 
                                                                       
            0 · · · 0 ann                          0 ··· ···         0




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2          Pré-Ing 1 – 2023-2024   160 / 231
~~~

## Page 161

~~~text
Matrice triangulaire inférieure



Définition
Soit M = (aij )1≤i,j≤n une matrice carrée de taille n. On dit que :
M est une matrice triangulaire inférieure (resp. triangulaire strictement
inférieure) si aij = 0 pour tout i < j (resp. i ≤ j). C’est-à-dire :
                                                                          
                                                       0    0      ···  0
                                  
          a11 0        ···     0
                                                                        .. 
        a21 a22       ···     0                  a21 . . .      ..
                                                  
                                                                      .  . 
M= .                          .     , (resp.M =                          ).
                                  
        ..     . ..   . ..    ..                    .           ..
                                                   ..                .
                                                                          
                                                                        0 
          an1 · · · an,n−1 ann                        an1 · · · an,n−1 0




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   161 / 231
~~~

## Page 162

~~~text
Matrice diagonale



Définition
Soit M = (aij )1≤i,j≤n une matrice carrée de taille n. On dit que :
M est une matrice diagonale si aij = 0 pour tout i ̸= j. C’est-à-dire :

                                     a11    0     ···0
                                                            
                                           ..      ..     .. 
                           
                                    0        .       .    . 
                         M=         ..    ..                .
                           
                                     .       . an−1,n−1 0  
                                                   ..
                                     0     ···        .  ann




Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2      Pré-Ing 1 – 2023-2024   162 / 231
~~~

## Page 163

~~~text
Matrice symétrique/ antisymétrique



Définition
Soit M = (aij )1≤i,j≤n une matrice carrée de taille n. On dit que :
M est symétrique (resp. antisymétrique) si aij = aji (resp. aij − aji ) pour
tout 1 ≤ i, j ≤ n. C’est-à-dire :
                                                                          
        a11 a12 · · · a1n                           a11   a12 · · · a1n
      a12 a22 · · · a2n                        −a12 a22 · · · a2n 
M= .           .          .      , ( resp. M =  ..        ..           .. ).
                                                                          
      ..       .. . . .   .. 
                              
                                                 .          .
                                                                 ..
                                                                    .     . 
            a1n a2n · · · ann                     −a1n −a2n · · · ann




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   163 / 231
~~~

## Page 164

~~~text
Matrice transposée


Définition
Soit M = (aij )1≤i,j≤n une matrice carrée de taille n. On dit que :
Soit M = (aij ) 1≤i≤n ∈ Mn,p (K). On appelle transposée de M la matrice
                     1≤j≤p
t M = (b )              ∈ Mp,n (K) où bij = aij . c’est-à-dire :
        ij 1≤i≤p
                1≤j≤n

                                                        
                                   a11     a21 · · · an1
                             t
                                  a12     a22 · · · an2 
                               M= .        ..        ..  .
                                                        
                                  ..          ..
                                             .     .   . 
                                     a1p   a2p · · · anp

Autrement dit, les n lignes de M sont les n colonnes de t M et les p
colonnes de M sont les p lignes de t M.



Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2           Pré-Ing 1 – 2023-2024   164 / 231
~~~

## Page 165

~~~text
Remarque
 (1) Une matrice carrée M est symétrique, si et seulement si, t M = M.
 (2) Une matrice carrée M est antisymétrique, si et seulement si,
     t M = −M.




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   165 / 231
~~~

## Page 166

~~~text
Somme de matrices

Définition
Soit A = (aij ) 1≤i≤n ∈ Mn,p (K) et B = (bij ) 1≤i≤n ∈ Mn,p (K). On
                1≤j≤p                          1≤j≤p
définit la matrice A + B ∈ Mn,p (K) de la façon suivante :
A + B = (aij + bij ) 1≤i≤n ∈ Mn,p (K). Ainsi
                           1≤j≤p

                                                          
             a11 a12 · · · a1P             b11 b12 · · · b1P
            a21 a22 · · · a2p   b21 b22 · · · b2p 
     A+B =  .      .. . .      ..  +  ..      ..       .. 
                                                          
            ..                                     ..
                     .     .     .   .          .    .   . 
             an1 an2 · · · anp             bn1 bn2 · · · bnp
                                                   
             a11 + b11 a12 + b12 · · · a1P + b1p
            a21 + b21 a22 + b22 · · · a2p + b2p 
         =      ..          ..               ..    .
                                                   
                                     . .
                 .           .          .     .    
                          an1 + bn1 an2 + bn2 · · · anp + bnp

Remarque On ne somme que des matrices de même types.
Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2       Pré-Ing 1 – 2023-2024   166 / 231
~~~

## Page 167

~~~text
Multiplication par un scalaire



Définition
Soit M = (aij ) 1≤i≤n ∈ Mn,p (K) et soit λ ∈ K. On définit la matrice λA
                1≤j≤p
de Mn,p (K) par λA = (λaij ) 1≤i≤n . Ainsi
                                     1≤j≤p

                                                     
                                 λa11 λa12 · · · λa1P
                                λa21 λa22 · · · λa2p 
                          λA =  .     ..          .. 
                                                     
                                ..        ..
                                        .      .    . 
                                 λan1 λan2 · · · λanp




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2   Pré-Ing 1 – 2023-2024   167 / 231
~~~

## Page 168

~~~text
Théorème
(Mn,p (K), +, .) est un K-espace vectoriel d’élément nul
                                                    
                                         0 ··· 0
                      0 = 0Mn,p (K) =  ...
                                                    
                                                 ··· 
                                          0 ···   0




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   168 / 231
~~~

## Page 169

~~~text
Définition
Soit 1 ≤ i ≤ n et 1 ≤ j ≤ p.
On appelle matrice élémentaire d’indice (i, j) de Mn,p (K) la matrice Eij ,
dont tous les coefficients sont nuls sauf à la iième ligne et la jième colonne
qui vaut 1.

Exemple
Dans M2 (K), les matrices élémentaires sont
                                                
                           1 0                 0 1
                 E11 =                 E12 =
                           0 0                 0 0

                                                                   
                                     0 0                       0 0
                         E21 =                     E22 =                  .
                                     1 0                       0 1



Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2              Pré-Ing 1 – 2023-2024   169 / 231
~~~

## Page 170

~~~text
Exemple
Dans Mn,1 (K) les matrices élémentaires sont :
                                              
                             1                   0
                          0                   .. 
                   E11 =  .  , . . . , En1 =  .  .
                                              
                             .
                          .                   0 
                             0                   1




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2       Pré-Ing 1 – 2023-2024   170 / 231
~~~

## Page 171

~~~text
Théorème
La famille B = (Eij , 1 ⩽ i ≤ n, 1 ⩽ j ⩽ p) est une base de Mn,p (K).




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   171 / 231
~~~

## Page 172

~~~text
Démonstration.
                                                                          X
Pour toute matrice X = (aij ) 1⩽j⩽p
                              1⩽i⩽n ∈ Mn,p (K), on a X =                          aij Eij . Donc B
                                                                          1⩽i⩽n
                                                                          1⩽j⩽p

est une famille génératrice de Mn,p (K). Montrons
                                                X maintenant que B est libre.
Soient λij ∈ K, 1 ⩽ i ⩽ n et 1 ⩽ j ⩽ p tel que       λij Eij = 0Mn,p (K) et
                                                        1⩽i⩽n
                                                        1⩽j⩽p
                                                                  X
montrons que λij = 0, ∀1 ⩽ i ⩽ n et 1 ⩽ j ⩽ p. On a                       λij Eij = 0Mn,p (K) est
                                                                  1⩽i⩽n
                                                                  1⩽j⩽p

équivalent à                                                       
                         λ11      ···   λ1p       0         ···    0
                         ..             ..  =  ..               ..  .
                         .               .   .                   . 
                            λn1   ···   λnp             0   ···    0
Par identification on obtient le résultat λij = 0, ∀1 ⩽ i ⩽ n, 1 ⩽ j ⩽ p.




Debyaoui, Dussap, Nguyen (CYU)           CM Algèbre 2                  Pré-Ing 1 – 2023-2024   172 / 231
~~~

## Page 173

~~~text
Corollaire
La dimension de l’espace vectoriel Mn,p (K) est m × p. En particulier
dim Mn (K) = n2 et dim Mn,1 (K ) = dim M1,n (K) = n.




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   173 / 231
~~~

## Page 174

~~~text
Exemple
Soient A1 , A2 , A3 , A4 les matrices de M2 (R) suivantes :
                                                       
                              1 0                 1 0
                    A1 =                  A2 =
                              0 1                 0 −1

                                                                   
                                     1 1                      0 −1
                         A3 =                     A4 =                    .
                                     1 1                      1 0

Montrons que B = (A1 , A2 , A3 , A4 ) est une base de M2 (R).
Nous remarquons que Card(B) = 4 = dim M2 (R).
Donc pour que B soit une base de M2 (R) il suffit que B soit libre sur
M2 (R).
Soient λ1 , . . . , λ4 ∈ R, tel que λ1 A1 + λ2 A2 + λ3 A3 + λ4 A4 = 0. Montrons
que λ1 = · · · = λ4 = 0.


Debyaoui, Dussap, Nguyen (CYU)             CM Algèbre 2              Pré-Ing 1 – 2023-2024   174 / 231
~~~

## Page 175

~~~text
Exemple
On a λ1 A1 + λ2 A2 + λ3 A3 + λ4 A4 = 0 est équivalent à
                                                      
               λ1 + λ2 + λ3      λ3 − λ4             0 0
                                               =           .
                  λ3 + λ4     λ1 − λ2 + λ3           0 0

Qui est équivalent à             
                                 
                                  λ1 + λ2 + λ3 = 0,
                                   λ3 − λ4 = 0,
                                 
                                   λ + λ4 = 0,
                                  3
                                 
                                 
                                   λ1 − λ2 + λ3 = 0.
On déduit facilement que λ1 = λ2 = λ3 = λ4 = 0.




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2    Pré-Ing 1 – 2023-2024   175 / 231
~~~

## Page 176

~~~text
Exemple
Montrons que :
                                                                 
                                   a + b −a − b
                      F =                                 | a, b ∈ K
                                  2a + b −a + 2b

est un sous-espace vectoriel de M2 (K). On a
                                                     
                         a −a           b −b
           F =                     +            | a, b ∈ K
                        2a −a           b 2b
                                                       
                          1 −1            1 −1
               =     a              +b            | a, b ∈ K
                          2 −1            1 2
                                           
                             1 −1         1 −1
               = vect                 ,             .
                             2 −1         1 2

Par suite F est un sous-espace vectoriel de M2 (K).


Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2             Pré-Ing 1 – 2023-2024   176 / 231
~~~

## Page 177

~~~text
Exemple
                                                              
                a b
Soit H =                 | a + b + c + d = 0, avec a, b, c, d ∈ K .
                c d
Montrons que H est un sous-espace vectoriel de M2 (K).
Soit f l’application suivante

                        f    : M2 (K) →        K
                                a b
                                        7→ a + b + c + d.
                                c d

Il est facile à vérifier que f est une application linéaire, c’est-à-dire, pour
tous λ, b ∈ K, A, B ∈ M2 (K) on a f (λA + bB) = λf (A) + bf (B).
On a

                    ker f    = {M ∈ M2 (K ) | f (M) = 0}
                                                      
                                  a b
                             =            |a+b+c +d =0
                                  c d

On remarque que ker f = H et on sait que le noyau d’une application
linéaire est un sous-espace vectoriel.
Debyaoui, Dussap, Nguyen (CYU)         On déduit
                                  CM Algèbre 2   alors que   H 1est
                                                        Pré-Ing      un
                                                                 – 2023-2024 177 / 231
~~~

## Page 178

~~~text
Sous-espaces des matrices diagonales et triangulaires



Proposition
Dn (K) l’ensemble des matrices diagonales de Mn (K) est un sous-espace
vectoriel de Mn (K) de dimension n.

Remarque Une base de                                                 
        
                            a11                    0                   
                                                                        
Dn (K) = M ∈ Mn (K) | M = 
                                         ..               , aij ∈ K
                                                          
                                                                            est
                                               .                       
                              0                     ann
                                                                       
B1 = (E11 , . . . , Enn ).




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2                 Pré-Ing 1 – 2023-2024   178 / 231
~~~

## Page 179

~~~text
Proposition
 (1) L’ensemble des matrices triangulaires supérieures (resp. triangulaires
     inférieures) est un sous-espace vectoriel de Mn (K) de dimension
     n(n+1)
        2   .
 (2) L’ensemble des matrices traingulaires strictement supérieures (resp.
     triangulaires strictement inférieures) est un sous-espace vectoriel de
     Mn (K) de dimension n(n−1)2   .




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   179 / 231
~~~

## Page 180

~~~text
Remarque
 (1) vect(Eij , ∀1 ≤ i ≤ j ≤ n) est l’ensemble des matrices triangulaires
     supérieures.
 (2) vect(Eij , ∀1 ≤ i < j ≤ n) est l’ensemble des matrices traingulaires
     strictement supérieures
 (3) vect(Eij , ∀1 ≤ j ≤ i ≤ n) est est l’ensemble des matrices triangulaires
     inféreiures.
 (4) vect(Eij , ∀1 ≤ j < i ≤ n) est l’ensemble des matrices traingulaires
     strictement strictement inférieures.




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   180 / 231
~~~

## Page 181

~~~text
Exercice




Montrer que :
 (1) Tn⩾ (K) ⊕ Tn< (K) = Mn (K).
 (2) Tn⩽ (K) ⊕ Tn> (K) = Mn (K).




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2   Pré-Ing 1 – 2023-2024   181 / 231
~~~

## Page 182

~~~text
Propriétés du produit matriciel



Définition
Soient A = (aij ) 1⩽i⩽n ∈ Mn,p (K), B = (bij ) 1⩽i⩽p ∈ Mp,q (K). On définit
                  1⩽j⩽p                        1⩽j⩽q
la matrice C = A × B = AB = (cij ) 1≤i≤n ∈ Mn,q (K), par
                                     1≤j≤q
∀1 ≤ i ≤ n, ∀1 ≤ j ≤ q, cij = pk=1 aik bkj .
                             P


Exemple Vérifier que pour tous Eij , Ekl ∈ Mn (K), on a Eij Ekl = δjk Eil .
Attention : Pour que cette multiplication matricielle soit possible il est
necessaire que le nombre de colonnes de A soit egal au nombre de ligne de
B. On apprend : “type(n,p)× type(p,q)=type(n,q).




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   182 / 231
~~~

## Page 183

~~~text
Exemple
                       
      1 2        1 0 0
    −1 1        2 1 −1                  
      1 × 1 + 2 × 2 0 + 2 × 1 0 + 2 × −1
 =
    −1 × 1 + 1× 2 0 + 1 × 1 0 + 1 × −1
     5 2 −2
 =
     1 1 −1




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   183 / 231
~~~

## Page 184

~~~text
Remarque Si les types de A et B permettent de calculer AB et BA, alors
en général on n’a pas AB = BA. Par exemple :
                                             
                       1 0     0 1           0 1
                                       =
                       0 0     0 0           0 0
                                                                 
                                 0 1         1 0                0 0
                                                        =
                                 0 0         0 0                0 0




Debyaoui, Dussap, Nguyen (CYU)              CM Algèbre 2              Pré-Ing 1 – 2023-2024   184 / 231
~~~

## Page 185

~~~text
Proposition
 (1) Pour tout A ∈ Mn,p (K), B ∈ Mp, q(K), C ∈ Mq, m, on a
     (AB)C = A(CB) ;
 (2) pour tous A, B ∈ Mn,p (K) et C ∈ Mp, q(K), on a
     (A + B)C = AC + BC ;
 (3) pour tous A ∈ Mn,p (K) et B, C ∈ Mp, q(K), on a
     A(B + C ) = AB + AC ;
 (4) Pour tout A ∈ Mn,p (K), B ∈ Mp, q(K), et pour tout λ ∈ K, on a
     λ(AB) = (λA)B = A(λB).




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2     Pré-Ing 1 – 2023-2024   185 / 231
~~~

## Page 186

~~~text
Remarque Dans l’ensemble des matrices Mn (K) des matrices carrées, la
multiplications est une loi de composition interne. Elle admet comme
élément neutre la matrice diagonale
                                              
                                    1        0
                             In = 
                                       ..     
                                           .   
                                   0            1




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2       Pré-Ing 1 – 2023-2024   186 / 231
~~~

## Page 187

~~~text
Puissance d’une matrice




Définition
Soit A ∈ Mn (K), on note
A0 = In , A1 = A, A2 = A × A, . . . , Am = A × · · · × A (m termes).

Attention : (A + B)2 = A2 + AB + BA + B 2 ̸= A2 + 2AB + B 2
(A + B)3 = A3 + A2 B + ABA + BA2 + AB 2 + BAB + B 2 .




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   187 / 231
~~~

## Page 188

~~~text
Contenu



5   Matrices et inverses de matrices
          Définition
          (Mn,p (K), +, .) est un K-espace vectoriel
          Opérations
          Dimension
          Sous-espaces des matrices diagonales et triangulaires
          Propriétés du produit matriciel
          Puissance d’une matrice
       Matrices inversibles
          Détermination pratique de l’inverse d’une matrice carrée inversible




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2              Pré-Ing 1 – 2023-2024   188 / 231
~~~

## Page 189

~~~text
Matrices inversibles




Définition
Une matrice A ∈ Mn (K) est dite inversible s’il existe B ∈ Mn (K) vérifiant
AB = BA = In .
Cette matrice B est alors unique, c’est l’inverse de A noté A−1 .




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2         Pré-Ing 1 – 2023-2024   189 / 231
~~~

## Page 190

~~~text
Exemple
La matrice In est inversible et In−1 = In .

Proposition
Soient A, B ∈ Mn (K).
 (1) Si A et B sont inversibles alors (AB)−1 = B −1 A−1 .
 (2) Si A est inversible alors A−1 est inversible et (A−1 )−1 = A.




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2       Pré-Ing 1 – 2023-2024   190 / 231
~~~

## Page 191

~~~text
Définition
On note GLn (K) l’ensemble des matrices inversibles de Mn (K).

Proposition
(GLn (K), ×) est un groupe.

Exemple
                       
                 1 2
Soit A =                  . On vérifie par le calcul que A2 − 5A = 2I2 . Par suite
                 3 4
A( 21 A − 25 I2 ) = I2 . On conclut alors que A−1 = 12 A − 52 I2 .




Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   191 / 231
~~~

## Page 192

~~~text
Remarque La somme de deux matrice inversible n’est pas toujours une
matrice inversible. Par example :
                                               
                     1 0          −1 0        0 0
                            +            =
                     0 1           0 −1       0 0




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2     Pré-Ing 1 – 2023-2024   192 / 231
~~~

## Page 193

~~~text
Lemme
Soient A, B ∈ Mn,p (K) si AX = BX , ∀X ∈ Mp,1 (K) alors A = B.




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2     Pré-Ing 1 – 2023-2024   193 / 231
~~~

## Page 194

~~~text
Comment chercher l’inverse d’une matrice carrée
A ∈ GLn (K) :

                                                             
                                                          x1
Soit A = (aij ) 1⩽i⩽n       ∈ GLn (K). On introduit X =  ...  ∈ Mn,1 (K) et
                                                             
                    1⩽j⩽n
                                                           xn
               
      y1
     .. 
Y =  .  = AX ∈ Mn,1 (K). On a
      yn
                                               
                        y1     a11 · · · a1n     x1
                       ..   ..         ..   ..  .
                       . = .            .  . 
                        yn     an1 · · · ann     xn



Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2        Pré-Ing 1 – 2023-2024   194 / 231
~~~

## Page 195

~~~text
Le système est équivalent à
                 
                  y1 = a11 x1 + a12 x2 + · · · + a1n xn
                 
                    ..  .. ..
                    .   . .
                     yn = an1 x1 + an2 x2 + ann xn .
                 

Si cela est possible, on résout ce système dont les inconnues sont x1 , . . . , xn
et on obtient :
                     
                      x1 = b11 y1 + b12 y2 + · · · + b1n yn
                     
               (S) :    ..   .. ..
                        .    . .
                         xn = bn1 y1 + bn2 y2 + · · · + bnn yn .
                     

Soit B = (bij ) 1≤i≤n ∈ GLn (K).
                1≤j≤n
Le système (S) est équivalent à X = BY . Ainsi
In X = BAX , ∀X ∈ Mn,1 (K), on a donc In = BA donc A−1 = B


Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   195 / 231
~~~

## Page 196

~~~text
Exemple
                  
            0 1 1
Soit A =  1 0 1  ∈ M3 (R). Déterminons A−1 . Soient
          1 1 0      
        x1          y1
X =  x2  , Y =  y2  ∈ M3,1 (R) tel que Y = AX . On a :
        x2          y3
                                               
                                                 x = 12 (y1 − y2 + y3 )
                                                2
                 
 y1 = x2 + x3     x2 = y1 − x3
                                               
                                               
   y2 = x1 + x3 ⇔    x3 = 12 (y2 − y3 + y1 ) ⇔   x3 = 21 (y1 + y2 − y3 )
   y3 = x1 + x2      x1 = y3 − y1 + x3
                                             
                                                x = 1 (−y + y + y )
                                               
                                                     1   2      1      2         3
                                                
                               −1 1            1
On déduit alors que A−1 = 21  1 −1            1 
                               1  1           −1



Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2        Pré-Ing 1 – 2023-2024       196 / 231
~~~

## Page 197

~~~text
Algorithme de Gauss Jordan


Proposition
(Algorithme de Gauss-Jordan) Soit A une matrice carrée de taille n
inversible. L’inverse A−1 de A se calcule de la manière suivante :
   1   On forme la matrice augmentée n × 2n suivante B = (A|In ).
   2   On applique l’algorithme de Gauss à B.
   3   Une fois le système échelonné obtenu, on continue sur le même
       principe que l’algorithme de Gauss afin d’obtenir une matrice de la
       forme (In |C ).
   4   L’inverse est A−1 = C .
Démonstration. Admis.



Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   197 / 231
~~~

## Page 198

~~~text
Exemple
Inverser la matrice A :                   
                                      1 2 3
                                 A = 2 3 4
                                      3 4 6




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2   Pré-Ing 1 – 2023-2024   198 / 231
~~~

## Page 199

~~~text
                                          
                              1 2 3 1 0 0
                            2 3 4 0 1 0
                              3 4 6 0 0 1
                                     
                      1 2   3   1 0 0
                    0 −1 −2 −2 1 0 L2 ← L2 − 2L1
                      0 −2 −3 −3 0 1      L3 ← L3 − 3L1
                                   
                       1 2 3 1 0 0
                     0 1 2 2 −1 0       L2 ← −L2
                       0 0 1 1 −2 1     L3 ← L3 + 2L2
                                     
                     1 2 0 −2 6 −3        L1 ← L1 − 3L3
                    0 1 0 0     3 −2    L2 ← L2 − 2L3
                      0 0 1 1 −2 1
                                     
                      1 0 0 −2 0    1     L1 ← L1 − 2L2
                    0 1 0 0     3 −2
                      0 0 1 1 −2 1
Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2    Pré-Ing 1 – 2023-2024   199 / 231
~~~

## Page 200

~~~text
L’inverse de A est donc
                                               
                                        −2 0  1
                                 A−1 =  0 3 −2
                                         1 −2 1




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2   Pré-Ing 1 – 2023-2024   200 / 231
~~~

## Page 201

~~~text
                                 Déterminants




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2   Pré-Ing 1 – 2023-2024   201 / 231
~~~

## Page 202

~~~text
Dans cette section, on suppose que A = (aij ) est une matrice carrée de
taille n × n
Définition (Mineure d’une matrice)
Pour tout couple (i, j) ∈ [[1; n]]2 , on appelle mineure d’indice i, j la matrice
de taille (n − 1) × (n − 1) obtenue en supprimant la i e ligne et la j e colonne
de A.

Exemple
                     
            1 2 3 4
         5 6 7 8
Soit A = 
          9 10 11 12.
                      

           13 14 15 16
                                              
                                        1 2 4
La mineure d’indice 2, 3 est : A2,3 =  9 10 12
                                       13 14 16


Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2           Pré-Ing 1 – 2023-2024   202 / 231
~~~

## Page 203

~~~text
Définition (Déterminant d’une matrice carrée)
Pour tout (i, j) ∈ [[1; n]]2 , Aij la matrice obtenue en supprimant la i e ligne
et la j e colonne de A. On appelle déterminant de A le nombre défini par :
                              a     a
     Si n = 2, det(A) = 11 12 = a11 a22 − a21 a12
                              a21 a22
                              n
                                (−1)i+1 ai1 det (Ai1 )
                             P
     Si n > 2, det(A) =
                                 i=1


Exemple
 2 −5
      = −4 − (−25) = 21
 5 −2
  1 1 2
             3 1     1 2    1 2
 −2 3 1 = 1      +2      +1     = (15−2)+2(5−4)+(1−6) = 10
             2 5     2 5    3 1
  1 2 5


Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2       Pré-Ing 1 – 2023-2024   203 / 231
~~~

## Page 204

~~~text
Proposition
   1   det (A⊺ ) = det(A)
   2   Soit Bj la matrice obtenue en intervertissant la première et la j e
       colonne (ou ligne) de A. Alors

                                 det (Bj ) = − det(A)

   3   Échanger deux colonnes (ou deux lignes) de A a pour effet de
       multiplier le déterminant par (−1).
   4   Le déterminant d’une matrice ayant deux colonnes (ou deux lignes)
       égales est nul.
   5   Multiplier une colonne (ou une ligne) d’une matrice par λ ∈ R,
       multiplie son déterminant par λ.



Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2          Pré-Ing 1 – 2023-2024   204 / 231
~~~

## Page 205

~~~text
Proposition
   6   Soit A et B deux matrice de taille n × n et λ ∈ R. Alors

                 det (λA) = λn det(A)
                 det(AB) = det(A) × det(B)
                               1
                 det A−1 =
                        
                                    si (A inversible ) ⇔ (det(A) ̸= 0)
                            det(A)
   7   Ajouter à une colonne (ou une ligne) une combinaison linéaire des
       autres colonnes (ou ligne) ne modifie par le déterminant.
   8   Développement selon une ligne et une colonne
                    n
                    X
       det(A) =           (−1)k+j akj det (Akj ) (développement selon la colonne j)
                    k=1
                    n
                    X
       det(A) =           (−1)i+k aik det (Aik ) (développement selon la ligne i)
                    k=1

Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2          Pré-Ing 1 – 2023-2024   205 / 231
~~~

## Page 206

~~~text
Exemple
      développement selon la première ligne
       1 0 2
                     4 5         3 4
       3 4 5 =1            +2         = (28 − 30) + 2(18 − 20) = −6
                     6 7         5 6
       5 6 7
      combinaison linéaire des lignes
        1    1     1      1 1 1
                                                   1 1
        2 −1 −1 = 3 0 0 = (−1)1+2 ×3                     = −3(6−5) = −3
                                                   5 6
       −4 5        6      −4 5 6
      deux lignes identiques
       1 1      6        1 1 6
       3 −2 5 = 2 3 −2 5 = 0
       2 2 12            1 1 6




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2      Pré-Ing 1 – 2023-2024   206 / 231
~~~

## Page 207

~~~text
Proposition
   9   Le déterminant d’une matrice triangulaire/diagonale est égal au
       produit des coefficients de la diagonale.
  10   Soit A la matrice définie par
                                                   
                                          B      C 
                                 A=
                                   
                                                    
                                                    
                                           0      D

       ici, B, C , D sont des matrices carrés. Alors det(A) = det(B) × det(D)

Exemple
   1        2   3    4 5
   6        7   8    9 10        a b c
                           1 2
A= 0        0   a    b c =     × d e f = −5g (ae − bd).
                           6 7
   0        0   d    e f         0 0 g
   0        0   0    0 g
Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2         Pré-Ing 1 – 2023-2024   207 / 231
~~~

## Page 208

~~~text
Définition (Déterminant de n vecteurs)
                                                                       
                                                             a11         a12
                                                            a21       a22 
Soit B = {e1 , e2 , · · · , en } une base de Rn . Soit u1 =  . , u2 =  . ,
                                                                       
                                                              .
                                                             .         .. 
                                                      an1          an2
                
             a1n
            a2n 
. . ., un =  . , n vecteurs de Rn dont les coordonnées sont données
             
             .. 
             ann
dans la base B. Soit A = (aij ) la matrice n × n construites à partir des
vecteurs ui . On définit le déterminant de la famille {u1 , u2 , · · · , un } dans la
base B par
                        det B {u1 , u2 , · · · , un } = det(A)



Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2            Pré-Ing 1 – 2023-2024   208 / 231
~~~

## Page 209

~~~text
Proposition (Caractérisation d’une famille liée)
Soit {u1 , u2 , · · · , un } une famille de n vecteurs de Rn . Il y a équivalence
entre les assertions suivantes :
   1   La famille {u1 , u2 , · · · , un } est liée.
   2   Pour toutes bases B de Rn , on a det B {u1 , u2 , · · · , un } = 0
   3   Il existe une base B de Rn telle que det B {u1 , u2 , · · · , un } = 0

Proposition (Caractérisation d’une base)
Soit {u1 , u2 , · · · , un } une famille de n vecteurs de Rn . Il y a équivalence
entre les assertions suivantes :
   1   La famille {u1 , u2 , · · · , un } est une base.
   2   Pour toutes bases B de Rn , on a det B {u1 , u2 , · · · , un } =
                                                                      ̸ 0
   3   Il existe une base B de Rn telle que det B {u1 , u2 , · · · , un } =
                                                                          ̸ 0


Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2        Pré-Ing 1 – 2023-2024   209 / 231
~~~

## Page 210

~~~text
Proposition (Formules de Cramer)
Soit B une matrice (colonne) de taille n × 1. Alors le système linéaire
AX = B possède une unique solution dont les composantes sont données
par :
                               det (C1 , . . . , Ci−1 , B, Ci+1 , . . . , Cn )
           ∀i ∈ [[1; n]], xi =
                                                  det(A)
où {C1 , C2 , · · · , Cn } sont les colonnes de A.

Exemple
         
          2x − y + z            = 0               2 −1 1
Résoudre    x − 2y − z           = 3 On a det(A) = 1 −2 −1 = 6. D’où
           3x + y + 2z           = 1               3 1  2
         

    0 −1 1                          2 0 1                2 −1 0
    3 −2 −1                         1 3 −1               1 −2 3
    1 1  2                          3 1 2                3 1 1
 x=         = 2;                 y=        = 1;       z=        = −3
       6                               6                    6
Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2        Pré-Ing 1 – 2023-2024   210 / 231
~~~

## Page 211

~~~text
       Représentation matricielle et changements de bases




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2   Pré-Ing 1 – 2023-2024   211 / 231
~~~

## Page 212

~~~text
Dans cette section, on suppose que E est un K-espace vectoriel de
dimension finie n, F est un espace vectoriel de dimension fini

Définition (Matrice d’une famille finie de vecteurs dans une base finie)
Soit B = {e1 , e2 , · · · , en } une base de E et X = {X1 , e2 , · · · , Xp } une
famille finie de vecteurs de E . Pour tout j ∈ [[1; p]] on note (a1j , . . . , anj )
les coordonnées de Xj dans la base B. La matrice (aij )1≤i≤n , notée
                                                               1≤j≤p
MatB (X ), est appelée matrice de X dans la base B.

                             X1             Xj             Xp
                              ↓              ↓              ↓
                             a11     ...    a1j      ...   a1p ←      e1
                                                               
                            ..              ..             .. 
                MatB (X ) =  .               .              . 
                            ai1     ...    aij      ...   aip  ←     ei
                                                               
                            .               ..              .. 
                            ..               .               . 
                             an1     ...    anj      ...   anp ←      en


Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2             Pré-Ing 1 – 2023-2024   212 / 231
~~~

## Page 213

~~~text
Théorème (Bases et matrices inversibles)
Soit B une base de E et F une famille de n vecteurs de E . Alors F est une
base de E si et seulement si MatB (F) est inversible.

Proposition
Soit E ̸= {0E }, B une base de E et X une famille de vecteurs de E . Alors

                                 rg(X ) = rg (MatB (X ))




Debyaoui, Dussap, Nguyen (CYU)         CM Algèbre 2        Pré-Ing 1 – 2023-2024   213 / 231
~~~

## Page 214

~~~text
Définition (Matrice d’une application linéaire dans des bases finies)
Soit dim(E ) = p et dim(F ) = n, B = {e1 , e2 , · · · , ep } une base de E ,
C = {κ1 , κ2 , · · · , κn } une base de F et f ∈ L(E , F ). On appelle matrice de
f dans B et C et on note MatB,C (f ) la matrice de la famille
f (B) = (f (e1 ), . . . , f (ep )) dans la base C.
Si E = F et B = C, la matrice MatB,B (f ) est simplement notée MatB (f ).

                               f (e1 )            f (ej )          f (ep )
                                  ↓                  ↓                ↓
                                 a11      ...       a1j     ...      a1p    ←         κ1
                                                                         
                              ..                    ..               .. 
 MatB,C (f ) = MatC (f (B)) =    .                   .                . 
                              ai1        ...      aij      ...      aip  ←          κi
                                                                         
                              .                    ..                 .. 
                              ..                    .                  . 
                                 an1      ...      anj      ...      anp    ←         κn


Coordonnées de f (ej ) dans C écrites en colonnes

Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2               Pré-Ing 1 – 2023-2024   214 / 231
~~~

## Page 215

~~~text
Exemple
      Si B est une base de E , alors MatB (IdE ) = In .
      Soit T l’endomorphisme P 7→ X 2 P ′′ + P(1) de R3 [X ] et
      B3 = {1, X , X 2 , X 3 } la base canonique de R3 [X ]. Alors

                          T (1) = 1                  T (X ) = 1
                                 2    2
                          T (X ) = 2X + 1            T (X 3 ) = 6X 3 + 1

                           T (1)      T (X )     T (X 2 )    T (X 3 )
                             ↓          ↓           ↓           ↓
                           1           1           1           1 ←              1
              MatB3 (T ) = 0           0           0           0 ←              X
                             0          0           2           0       ←         X2
                                                                     
                             0          0           0           6       ←         X3



Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2                Pré-Ing 1 – 2023-2024   215 / 231
~~~

## Page 216

~~~text
Proposition (Rang d’une application linéaire)
Soit B une base de E , C une base de F et f ∈ L(E , F ). Alors

                                 rg(f ) = rg (MatB,C (f ))

Démonstration.

      rg (MatB,C (f )) = rg (MatC (f (B)))
                           = rg (f (B)) = dim Vect(f (B)) = dim Im f = rg(f )




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2         Pré-Ing 1 – 2023-2024   216 / 231
~~~

## Page 217

~~~text
Théorème (Calcul matriciel de l’image d’un vecteur par une
application linéaire)
Soit E ̸= {0E } et F ̸= {0F } deux K-espace vectoriels de dimension finie, B
une base de E , C une base de F , u ∈ L(E , F ) et x ∈ E . Alors

                         MatC (u(x)) = MatB,C (u) × MatB (x)

Démonstration.
Soit B = {e1 , e2 , · · · , ep }, C = {f1 , f2 , · · · , fn }. Posons X = MatB (x) et
U = MatB,C (u).
                                                                                   
           X  p                 X p                X p      X n          n
                                                                         X   p
                                                                             X
 u(x) = u        xj ej  =         xj u(ej ) =          xj     uij fi =      uij xj  fi
                 j=1             j=1            j=1    i=1               i=1         j=1

                                                        p
                                                       X                      p
                                                                               X           
Donc les coordonnées de u(x) dans C sont                     u1jxj , . . . ,         unj xj ,
                                                       j=1                     j=1
c’est-à-dire le produit U × X .
Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2                 Pré-Ing 1 – 2023-2024      217 / 231
~~~

## Page 218

~~~text
Proposition (Lien entre L(E , F ) et Mn,p (K ))
Soit E et F deux K-espaces vectoriels de dimensions finies respectives p et
n, B une base de E et C une base de F . L’application f 7→ MatB,C (f ) est
un isomorphisme de L(E , F ) sur Mn,p (K ).

Proposition (Matrice d’une composée)
Soit E , F , G trois K-espaces vectoriels de dimensions finies non nulles de
bases respectives B, C, D et f ∈ L(E , F ) et g ∈ L(F , G ). Alors,

                      MatB,D (g ◦ f ) = MatC,D (g ) × MatB,C (f )




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2          Pré-Ing 1 – 2023-2024   218 / 231
~~~

## Page 219

~~~text
Proposition (Matrice d’un isomorphisme)
Soit E et F deux K-espaces vectoriels de mêmes dimensions finies non
nulles de bases respectives B, C et f ∈ L(E , F ). Alors f est un
isomorphisme de E sur F si et seulement si MatB,C (f ) est inversible. Dans
ce cas,
                      MatC,B f −1 = (MatB,C (f ))−1
                                   


Démonstration.
  ⇒ Si f est bijective et si on pose n = dim(F ), on a
    MatB,C (f ) × MatC,B (f −1 ) = MatC (IdF ) = In .
  ⇐ si A = MatB,C (f ) est inversible, notons g l’unique application linéaire
    de F dans E pour laquelle MatC,B (g ) = A−1 . Dans ces conditions,
    MatB (g ◦ f ) = MatC,B (g ) × MatB C(f ) = A−1 A = In . De même,
    MatC,B = In . Donc g ◦ f = IdE et f ◦ g = IdF et f est bijective de E
    sur F .


Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2           Pré-Ing 1 – 2023-2024   219 / 231
~~~

## Page 220

~~~text
Changement de base




Définition (Matrice de passage)
Soit B = (e1 , e2 , . . . , en ) et B ′ = (e1′ , e2′ , . . . , en′ ) deux bases de E . On
appelle matrice de passage de la base B à la base B ′ la matrice de
l’application IdE relativement aux bases B ′ et B. On la note :

                        PB B ′ = MatB (B ′ ) = MatB′ ,B (IdE )
                                  




Debyaoui, Dussap, Nguyen (CYU)            CM Algèbre 2               Pré-Ing 1 – 2023-2024   220 / 231
~~~

## Page 221

~~~text
Exemple
Soit E = R2 [X ], B = 1, X , X 2 et B ′ = 1, X − 1, (X − 1)2 . On a alors
                                                           


                                 1 = 1 donc IdE (1) = 1 + 0X + 0X 2
                 X − 1 = −1 + X , donc IdE (X − 1) = −1 + 1X + 0X 2
        (X − 1)2 = 1 − 2X + X 2 donc IdE ((X − 1)2 ) = 1 − 2X + 1X 2

La matrice de passage de B à B ′ est donc :

                             1        −1           1     !←      1
                             0         1          −2      ←      X
                    PB B ′ = 0
                                      0           1      ←      X2
                             ↑         ↑           ↑
                             1       X −1       (X − 1)2




Debyaoui, Dussap, Nguyen (CYU)          CM Algèbre 2          Pré-Ing 1 – 2023-2024   221 / 231
~~~

## Page 222

~~~text
Proposition
Si P = PB (B ′ ), alors P est inversible et P −1 = PB′ (B)

Proposition
Une matrice P est inversible si et seulement si il existe deux bases B et B ′
de E telles que P = PB (B ′ ) = MatB′ ,B (IdE ).

Proposition
Soit B, B ′ et B ′′ trois bases de E . Alors PB (B ′′ ) = PB (B ′ ) × PB′ (B ′′ ).




Debyaoui, Dussap, Nguyen (CYU)        CM Algèbre 2            Pré-Ing 1 – 2023-2024   222 / 231
~~~

## Page 223

~~~text
Proposition (Matrice de passage et coordonnées)
Soit vecteur x ∈ E , B et B ′ deux bases de E , et P = PB (B ′ ). On note XB
la matrice colonne des coordonnées de x dans la base B et XB′ ′ la matrice
colonne des coordonnées de x dans la base B ′ . Alors :

                                 XB = PXB′ ′

Démonstration.
x = IdE (x), donc le résultat découle simplement de la définition de la
matrice de passage.




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2         Pré-Ing 1 – 2023-2024   223 / 231
~~~

## Page 224

~~~text
Exemple
Soit X = (1, 2, 3) dans la base canonique Bc , soit
B ′ = {e1 , e1 + e2 , e3 − e2 − 3e1 } est une base de R3 . Déterminer les
coordonnées de X dans la base B ′ .
      Sans utiliser la formule.
                                       
                 ε1 = e1
                                       e1
                                                  = ε1
                    ε2 = e 1 + e 2     ⇔ e2        = ε2 − ε 1
                                       
                    ε3 = e3 − e2 − 3e1   e3        = ε3 + ε2 + 2ε1
                                       

      Ainsi, de X = e1 + 2e2 + 3e3 , nous arrivons à X = 5ε1 + 5ε2 + 3ε3
      En utilisant la formule de changement de bases. Nous avons
      XBc = PXB′ , d’où XB′ = P −1 XBc . Il faut donc calculer l’inverse de P
                         −1                
                1 1 −3              1 −1 2
      P −1 = 0 1 −1 = 0 1 1. Et on retrouve
                0 0 1               0 0 1
      XB′ = (5, 5, 3).
Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2          Pré-Ing 1 – 2023-2024   224 / 231
~~~

## Page 225

~~~text
Matrices équivalentes
Définition
Soit A, B ∈ Mn,p (K). On dit que B est équivalente à A s’il existe deux
matrices carrées inversibles Q ∈ GLn (K), P ∈ GLp (K) telles que :

                                  B = Q −1 AP

Proposition
La relation « est équivalente à » sur Mn,p (K) est une relation
d’équivalence.

Démonstration.
 Réflexivité : Nous avons simplement A = In−1 AIp .
   Symétrie : Nous avons B = Q −1 AP, donc A = QBP −1 . En posant
              Q ′ = Q −1 et P ′ = P −1 , on a bien A = Q ′ −1 BP ′ .
Transitivité : Nous avons C = Q −1 BP et B = Q ′ −1 AP ′ . En posant
               Q ′′ = Q ′ Q et P ′′ = P ′ P nous obtenons C = Q ′′ −1 AP ′′ .
Debyaoui, Dussap, Nguyen (CYU)      CM Algèbre 2           Pré-Ing 1 – 2023-2024   225 / 231
~~~

## Page 226

~~~text
Proposition
Soit A et B deux matrices de Mn,p (K). Les matrices A et B sont
équivalentes si et seulement si rg(A) = rg(B).




Debyaoui, Dussap, Nguyen (CYU)   CM Algèbre 2      Pré-Ing 1 – 2023-2024   226 / 231
~~~

## Page 227

~~~text
Matrices semblables
Définition
Soit A, B ∈ Mn (K). On dit que B est semblable à A s’il existe une matrice
inversible P ∈ GLn (K) telle que

                                 B = P −1 AP

Proposition
La relation « est semblable à » sur Mn (K) est une relation d’équivalence.

Démonstration.
 Réflexivité : Nous avons simplement A = In−1 AIn .
   Symétrie : Nous avons B = P −1 AP, donc A = PBP −1 . En posant
              P ′ = P −1 , on a bien A = P ′ −1 BP ′ .
Transitivité : Nous avons C = P −1 BP et B = P ′ −1 AP ′ . En posant
               P ′′ = P ′ P nous obtenons C = P ′′ −1 AP ′′ .

Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2        Pré-Ing 1 – 2023-2024   227 / 231
~~~

## Page 228

~~~text
Proposition
Si deux matrices A et B sont semblables alors elles sont équivalentes
(semblables ⇒ équivalentes).

Attention ! ! La réciproque est fausse.
Exemple
In est la seule matrice semblable à In alors que toute matrice inversible est
équivalente à In .




Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2          Pré-Ing 1 – 2023-2024   228 / 231
~~~

## Page 229

~~~text
Proposition (Matrices de passage et matrices semblables)
Soit f une application linéaire de E dans E , B et B ′ deux bases de E . On
note :
                                 P = PB B ′
                                            

Soit A la matrice de f relativement à la base B et B la matrice de f
relativement à la base B ′ . On a alors :

                                 B = P −1 AP

Proposition
Soit A, B ∈ Mn (K). Alors A et B sont semblables si et seulement si A et B
sont les deux matrices d’une même application linéaire dans deux bases
différentes.



Debyaoui, Dussap, Nguyen (CYU)    CM Algèbre 2         Pré-Ing 1 – 2023-2024   229 / 231
~~~

## Page 230

~~~text
Proposition (Invariance du déterminant et de la trace)
Deux matrices carrées semblables ont le même déterminant et la même
trace. Pour toute matrice carrée A et toute matrice carrée inversible P, on
a:

                          det P −1 AP = det(A)
                                      

                           Tr P −1 AP = Tr(A)
                                      


Démonstration.
Nous allons utiliser les deux propriété det(AB) = det(A) det(B) et
Tr(AB) = Tr(BA)

Attention ! La réciproque est fausse
Exemple
                                              
                                  1 1        1 0
                                        et
                                  0 1        0 1

Debyaoui, Dussap, Nguyen (CYU)       CM Algèbre 2     Pré-Ing 1 – 2023-2024   230 / 231
~~~

## Page 231

~~~text
Définition (Trace d’un endomorphisme)
Soit E ̸= {0E } et f ∈ L(E ). On appelle trace de f et l’on note Tr(f ) la
trace d’une matrice de f dans une base de E .

Proposition (trace)
Pour tout f , g ∈ L(E ),
      Pour tout λ ∈ K, Tr(λf + g ) = λTr(f ) + Tr(g ).
      Tr(f ◦ g ) = Tr(g ◦ f )

Démonstration.
Il suffit de revenir aux matrices et utiliser les propriétés précédentes.




Debyaoui, Dussap, Nguyen (CYU)     CM Algèbre 2           Pré-Ing 1 – 2023-2024   231 / 231
~~~
