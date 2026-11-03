# Notes-de-cours_Mesures-et-integration.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1K5GoJfIKYRlK7eZ9ME61wAoUMypoqi3P) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                         Département de Mathématiques
                                            Cycle ingénieur 1ère année

                               Semestre 1 – Mathématiques appliquées




Mesure et intégration
     Notes de cours
    Nisrine FORTIN CAMDAVANT
~~~

## Page 2

*Page blanche.*

## Page 3

~~~text
Table des matières

   0.1   Approche intuitive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     5
   0.2   Exemple d’application : les probabilités . . . . . . . . . . . . . . . . . . . . . . . .       6
   0.3   Terminologie et définitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    7

1 Tribu et application mesurable                                                                       11
  1.1 Algèbre de Boole et tribu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        11
  1.2 Tribu engendrée, tribu borélienne . . . . . . . . . . . . . . . . . . . . . . . . . . . .        13
      1.2.1 Tribu engendrée . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          13
      1.2.2 Tribu borélienne . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         14
  1.3 Applications mesurables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        14
  1.4 Quelques propriétés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        16

2 Introduction à la mesure                                                                             20
  2.1 Fonction d’ensembles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       20
  2.2 Mesure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     21
       2.2.1 Exemples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        21
       2.2.2 Conséquences de la σ-additivité . . . . . . . . . . . . . . . . . . . . . . . . .         23
  2.3 Ensembles négligeables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       25
  2.4 Espaces mesurés complets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         27

3 Intégration de fonctions étagées positives                                                           31
  3.1 Fonction indicatrice de Q sur [0; 1] . . . . . . . . . . . . . . . . . . . . . . . . . . .       31
  3.2 Fonctions étagées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      33
  3.3 Intégrale d’une fonction étagée positive . . . . . . . . . . . . . . . . . . . . . . . . .       35
  3.4 Intégration de fonctions mesurables positives . . . . . . . . . . . . . . . . . . . . .          37
  3.5 Principaux théorèmes d’intégration de fonctions positives . . . . . . . . . . . . . .            40

4 Intégration de fonctions mesurables                                                                  46
  4.1 Intégration de fonctions réelles . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       46
  4.2 Propriétés de l’intégrale de fonctions réelles . . . . . . . . . . . . . . . . . . . . . .       48
  4.3 Mesures à densité - Théorème de Radon-Nikodym . . . . . . . . . . . . . . . . . .                51
      4.3.1 Mesure définie par une densité . . . . . . . . . . . . . . . . . . . . . . . . .           51
  4.4 Espaces Lp et Lp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         54
  4.5 Normes sur Lp (p ∈ [1, +∞[) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          57
  4.6 Espaces L∞ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       58
      4.6.1 Théorème de Radon Nikodym . . . . . . . . . . . . . . . . . . . . . . . . . .              60
      4.6.2 Mesure image . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         61


                                                    3
~~~

## Page 4

~~~text
Table des matières                                                                                   4



5 Produit de mesures                                                                                62
  5.1 Produit de tribus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   62
  5.2 Mesure produit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    64
  5.3 Théorème de Fubini . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      65
~~~

## Page 5

~~~text
Introduction générale au module

    La théorie de la mesure permet d’associer une grandeur numérique à un ensemble. Plusieurs
types de "mesures" ont déjà été rencontrés : le cardinal d’un ensemble discret, la longueur d’une
courbe, l’aire d’une figure plane, le volume d’un solide en dimension 3, la probabilité d’un évène-
ment. . ..
    Ces mesures sont courantes et forment des cas particuliers d’une notion plus générale de mesures
(Chapitre 2), outil de base pour une nouvelle théorie de l’intégration, dite intégrale de Lebesgue
(Chapitre 3).
    L’intégrale au sens de Lebesgue généralise la notion de l’intégrale de Riemann. Cette nouvelle
théorie s’applique à une classe de fonctions beaucoup plus grande (les fonctions mesurables), cette
dernière étend la notion de continuité de fonctions (Chapitre 1).
    Une mesure est associée à une famille d’ensembles à mesurer, appelée tribu de parties (Cha-
pitre 1). Ainsi, une tribu va englober des ensembles mesurables par une mesure donnée.



0.1     Approche intuitive
    Intuitivement, si on se place dans un ensemble non vide Ω, une tribu définie sur Ω contiendra
des sous-ensembles de Ω. Ces ensembles qu’on mesure seront "rassemblés" de la façon suivante :


      • La mesure choisie doit nous permettre de mesurer Ω donc

                                      Ω doit appartenir à la tribu ;

      • Si A appartient à la tribu, on peut donc la mesurer et on souhaite que le complémentaire
        de A dans Ω soit aussi mesurable donc on impose dans la définition

                        la condition de stabilité par passage au complémentaire ;

      • Si on sait mesurer deux parties A et B (appartiennent donc à la tribu), on souhaite que
        leur union soit aussi mesurable donc on impose dans la définition

                            la condition de stabilité par union dénombrable.



    On définira les fonctions qui préservent la propriété de mesurabilité de l’image réciproque d’un
ensemble mesurable. Cette théorie s’appliquera à des théorèmes de convergence beaucoup plus
puissants : théorème de convergence monotone, théorème de convergence dominée (Chapitre 5).

                                                 5
~~~

## Page 6

~~~text
Table des matières                                                                                                6



0.2      Exemple d’application : les probabilités
    Le calcul des probabilités s’intéresse à mesurer la "chance" qu’un certain "événement", résultat
d’une expérience, a de se produire. Considérons par exemple "l’expérience" qui consiste à lancer
un dé. On appelle "éventualité" associée à cette expérience un des résultats possibles de cette
expérience, et "univers des possibles" l’ensemble Ω de ces éventualités. Dans notre exemple, les
éventualités peuvent être 1, 2, 3, 4, 5 ou 6

                                                Ω = {1, 2, 3, 4, 5, 6} .

    On pourrait choisir aussi comme éventualités les résultats correspondant au "dé cassé". On peut
donc tout de suite remarquer que l’ensemble Ω des univers du possible dépend de la modélisation,
c’est à dire de la formalisation mathématique que l’on fait du problème. Notons qu’il est parfois
difficile de définir l’ensemble Ω.
    Supposons que toutes les faces paires d’un dé soient effacées. Dans ce cas, si le résultat du
lancer est pair, il nous est impossible de déterminer si la face 2 est survenue. On peut seulement
déterminer si le résultat est pair ou impair et dans ce dernier cas, déterminer quelle était la face
obtenue (1,3,5). Un sous-ensemble E de Ω correspond à l’événement et qu’un des éléments de E
s’est réalisé. Si l’on retourne à l’expérience du lancer du dé, les événements qui sont observables
seront tous les sous-ensembles de Ω. Par exemple, l’événement {1; 2; 3} est observable. Par contre,
si l’on est dans le cas où les faces paires sont non différentiables, l’événement {1; 2; 3} n’est plus
observable puisqu’on n’est plus en mesure de déterminer si l’événement 2 est survenu. Dans ce
dernier cas, les seuls événements possibles sont

                        ∅, {1} , {3} , {5} , {1; 3} , {1; 5} , {3; 5} , {1; 3; 5} , {1; 2; 4; 6} ,

             {2; 3; 4; 6} , {2; 4; 5; 6} , {1; 2; 3; 4; 6} , {1; 2; 4; 5; 6} , {2; 3; 4; 5; 6} , {2; 4; 6} , Ω.

    Intuitivement, si deux événements sont observables, leur réunion devrait l’être aussi. De plus, le
complémentaire d’un événement observable devrait être observable aussi car si on peut déterminer
si l’événement E est survenu, alors on peut également déterminer si l’événement Ec est survenu.
Finalement, Ω survient à tous les coups, donc ce sont toujours des événements observables.
~~~

## Page 7

~~~text
7                                                                               0.3. Terminologie et définitions




0.3      Terminologie et définitions

    Classe de parties
      Soit Ω une partie d’éléments non vide. La classe (ensemble) des parties de Ω, notée P(Ω) est
      définie par :
                                              P(Ω) = {A, A ⊆ Ω} .


Exemple 1. Ω = {a, b, c}. L’ensemble des parties de Ω est donné par :
                            n                                                         o
                      P(Ω) = ∅, {a} , {b} , {c} , {a, b} , {a, c} , {b, c} , {a, b, c} .

                                                                  
Attention, on dit que a ∈ Ω, {a} ⊂ Ω, {a} ∈ P(Ω) et                   {a}   ⊂ P(Ω).


    Le complémentaire d’un ensemble
      Pour toute partie A ∈ P(Ω), on note le complémentaire de A dans Ω par

                                           Ac = Ω\A = x ∈ Ω, x ∈
                                                               /A .
                                                     



      Propriété 1.

      Soient A et B deux parties de Ω alors

                                       c                          c
                               (A ∪ B) = Ac ∩ Bc et (A ∩ B) = Ac ∪ Bc .




    Dénombrabilité d’un ensemble
      Soit Ω un ensemble d’éléments. On dit que

         ■ Ω est infini s’il existe x0 ∈ Ω et une injection de Ω dans Ω\ x0 .
                                                                        


         ■ Ω est dénombrable s’il existe une bijection entre l’ensemble Ω et N.

         ■ Ω est au plus dénombrable s’il est fini ou dénombrable.


Exemple 2. N est infini car 0 ∈ N et l’application

                                             f   :   N →      N
                                                     n   7→   n+1

est une injection.
~~~

## Page 8

~~~text
Table des matières                                                                                        8



Exemple 3.

    • N, Z, Q, N × N sont dénombrables.

        ⇝ L’application
                                                     f    : N       → N
                                                               n    7→ n

             est une bijection.
        ⇝ L’application
                                                     f    : N       → Z
                                                               n    7→ xn

             où x2k = k et x2k+1 = −k − 1, k étant un entier naturel, est une bijection.
        ⇝ L’application
                                                 f       : N       → N×N
                                                          n        7→ xn

             où xn = (i, j) tel que i + j = n est une bijection.

    • R n’est pas dénombrable.


     Une partition
     On dit que (Ai )n∈N∗ forme une partition de Ω si :

         • ∀n ∈ N∗ , An ̸= ∅.

         • ∀n ∈ N∗ , ∀m ∈ N∗ , n ̸= m, An ∩ Am = ∅.
             +∞
         •         An = Ω.
             S
             n=1




     Différence symétrique
     Soient A et B deux parties de Ω. La différence symétrique de A et B notée A       B est l’ensemble
                                                                                   a

     des éléments appartenant à A ou à B exclusivement.

                                            i
                                        A       B = (A ∪ B) \ (A ∩ B)



     Image réciproque et image directe
     Soient E et F deux ensembles et f : E → F une application.

         • Soit B ⊂ F. On appelle image réciproque de B par f l’ensemble des éléments x de E
~~~

## Page 9

~~~text
9                                                                                            0.3. Terminologie et définitions



          dont l’image f (x) par f est dans B. C’est un sous-ensemble de E ; on le note

                                                  f −1 (B) = {x ∈ E, f (x) ∈ B} .


       • Soit A ⊂ E. On appelle image directe de A par f l’ensemble des images f (x) des
          éléments x de A. C’est un sous-ensemble de F ; on le note

                                        f (A) = {y ∈ F, ∃x ∈ A tel que y = f (x)}.

    Propriété 2.

       • On a f −1 (∅) = ∅, mais même si B est non vide, f −1 (B) peut être vide.

       • Pour toute partie B de F, f f −1 (B) ⊂ B.
                                             


             f f −1 (B) = B ⇐⇒ f est surjective.
                       


       • Pour toute partie A de E, A ⊂ f −1 (f (A)) .

             A = f −1 (f (A)) ⇐⇒ f est injective.

       • Pour toute famille (Bi )i∈I de parties de F,
                         !
                    \         \
           ▶ f −1
                      Bi =         f −1 (Bi ).
                     i∈I                i∈I
                                !
                     [                  [
            ▶ f −1         Bi       =         f −1 (Bi ).
                     i∈I                i∈I




    Limite inférieure et limite supérieure
    Soit (fn )n une suite de fonctions définies sur Ω. On définit :
                                                                                                   
                  lim inf fn = sup             inf fn (x)        et lim sup fn = inf        sup fn (x) .
                                    p∈N       n≥p                                 p∈N       n≥p




    Partie positive et partie négative
                                                                                        +
                                f + = sup (f, 0) , f − = sup (−f, 0) = (−f ) .


    Propriétés 1.


                                    f = f+ − f−             et    | f |= f + + f − .
~~~

## Page 10

~~~text
Table des matières                                                                               10




     Fonction indicatrice
     Soit A ⊂ Ω. On appelle fonction indicatrice de A, notée 1A (ou χA ), la fonction de Ω dans
     {0, 1} qui, à tout x ∈ Ω, associe 1 si x ∈ A et 0 si x ∈
                                                            /A:
                                                  (
                                                      1   si   x∈A
                                       1A (x) =
                                                      0   si   x∈
                                                                /A



      Propriété 3 (Quelques propriétés sur la fonction indicatrice).

        a) ∀x ∈ Ω, 1∅ (x) = 0 et 1Ω (x) = 1.

        b) A ⊂ B ⇔ 1A ≤ 1B ;

         c) 1A∩B = 1A .1B = inf(1A , 1B ) ;

        d) 1A∪B = 1A + 1B − 1A∩B = sup(1A , 1B ) ;

         e) 1Ω\A = 1 − 1A ;

         f) si (Ai )i∈N est une famille dénombrable de parties de Ω telle que An ∩ Ap = ∅ pour
                                   X
            n ̸= p alors 1 S Ai =      1Ai .
                         i∈N
                                 i∈N
~~~

## Page 11

~~~text
1 | Tribu et application mesurable


Sommaire
          1.1    Algèbre de Boole et tribu . . . . . . . . . . . . . . . . . . . . . . . . .             11
          1.2    Tribu engendrée, tribu borélienne . . . . . . . . . . . . . . . . . . . .               13
                1.2.1   Tribu engendrée . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    13
                1.2.2   Tribu borélienne . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   14
          1.3    Applications mesurables . . . . . . . . . . . . . . . . . . . . . . . . . .             14
          1.4    Quelques propriétés . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           16




1.1      Algèbre de Boole et tribu

      Définition 1.

      Soit A ⊂ P(Ω). On dit que A est une algèbre de Boole (de parties de Ω) si elle vérifie :

        1. Ω ∈ A,

        2. A ∈ A =⇒ Ω\A ∈ A,

        3. A ∈ A, B ∈ A =⇒ A ∪ B ∈ A.


      Définition 2.

      Soit T ⊂ P (Ω), on dit que T est une tribu de parties (ou σ-algèbre) si elle vérifie :

        1. Ω ∈ T ,

        2. la stabilité par passage au complémentaire : A ∈ T =⇒ Ω\A ∈ T ,

        3. la stabilité par réunion dénombrable : Si An ∈ T pour tout n ∈ N alors
               An ∈ T .
            S
           n∈N



Remarque 1.


                                                        11
~~~

## Page 12

~~~text
Chapitre 1. Tribu et application mesurable                                                         12



    • Une tribu est donc une algèbre de Boole stable par réunion dénombrable.

    • Si An ∈ T pour tout n ∈ N alors                An ∈ T . (Démonstration en TD1)
                                                T
                                               n∈N


      Définition 3.

     On appelle espace mesurable tout couple (Ω, T ) formé par un ensemble Ω et une tribu
     T sur Ω. Les ensembles mesurables sont les parties de Ω qui appartiennent à T .




   Exemple 4.

      ♢ La plus petite tribu de Ω est T = {∅, Ω}, elle est appelée tribu grossière.

      ♢ La plus grande tribu de Ω est T = P (Ω), elle est appelée tribu discrète.




   Exemple 5 (La tribu trace). Soient T une tribu de parties sur Ω et U ⊂ Ω.

                                              TU = {A ∩ U, A ∈ T }

   est une tribu sur U. Cette tribu est appelée la tribu trace sur U.
   En effet,

      ⇝ U ∈ TU car U = Ω ∩ U et Ω ∈ T .

      ⇝ Soit B ∈ TU , donc B = A ∩ U avec A ∈ T . Pour simplifier les notations, on notera ∗c le
          complémentaire de ∗ dans Ω.

                                                                 c
                           U \ B = U ∩ Bc = U ∩ (A ∩ U) = U ∩ (Ac ∪ Uc ) = U ∩ Ac .


          Comme A ∈ T , T est une tribu sur Ω alors Ac ∈ T , il s’en suit que

                                               U \ B = U ∩ Ac , Ac ∈ T

          Donc U \ B ∈ TU .

      ⇝ Soit Bn ∈ TU pour n ∈ N. Donc ∀n ∈ N, Bn = U ∩ An avec An ∈ T .
                                                                                       !
                                      [             [                       [
                                             Bn =         (U ∩ An ) = U ∩         An
                                      n∈N           n∈N                     n∈N
~~~

## Page 13

~~~text
13                                                                         1.2. Tribu engendrée, tribu borélienne




           Et comme An ∈ T et T est une tribu alors             n∈N An ∈ T . Finalement
                                                            S

                                                   [
                                                         Bn ∈ TU .
                                                   n∈N




1.2       Tribu engendrée, tribu borélienne
      En général, une tribu contient énormément d’éléments d’où le nom de tribu. Souvent, on ne
peut pas décrire tous les éléments d’une tribu mais cela n’a pas d’importance. En effet, ce qu’il
faut retenir, sont certaines parties de Ω de la tribu et on doit rester dans la tribu lorsqu’on itère
sur les éléments de la tribu les opérations de complémentarité et de réunion dénombrable.

1.2.1      Tribu engendrée
       Définition 4.

       Soit Ω un ensemble. Ω quelconque, H ⊂ P(Ω). On dit que T est la tribu engendrée par
       H si T est la plus petite tribu (au sens de l’inclusion) de parties de Ω contenant H.
       On note dans ce cas, T = σ(H).



       Proposition 4.

       On considère un ensemble quelconque Ω et H ⊂ P(Ω). σ(H) existe toujours, c’est l’in-
       tersection de toutes les tribus sur Ω contenant H.


Remarque 2. Soient H1 ⊂ P(Ω) et H2 ⊂ P(Ω).

     1. H1 ⊂ σ(H1 ). (Par définition de σ(H1 ).)

     2. Si T est une tribu contenant H alors σ(H) ⊂ T . (Par définition de σ(H).)

     3. Si H1 ⊂ H2 alors σ(H1 ) ⊂ σ(H2 ).

         ⇝ H1 ⊂ H2 ⊂ σ (H2 ) .
         ⇝ σ (H2 ) est une tribu donc σ (H2 ) est une tribu qui contient H1 . Comme σ (H1 ) est la
             plus petite tribu contenant H1 alors σ (H1 ) ⊂ σ (H2 ) .


     Exemple 6.

        • Si H = {∅} ou bien si H = {Ω}, alors σ(H) = {∅, Ω}

        • Si H = {A} ou bien si H = {Ac } où A ̸= ∅ et A ̸= Ω, alors σ(H) = {∅, A, Ac , Ω}.
~~~

## Page 14

~~~text
Chapitre 1. Tribu et application mesurable                                                                            14




        • Soient Ω = {a, b, c}, H = {{a}; {b}} ; on peut décrire la tribu engendrée par H :
                                                                                                        
                                
                                                                                                        
                                                                                                         
                      σ(H) =       Ω ; ∅; {a} ; {b} ; {b, c}; {a, c}; {a, b} ;
                                  |{z}                                                        {c}            .
                                
                                Ω∈tribu  | {z } | {z } | {z } | {z }                         |{z}       
                                                                                                         
                                                                                                     c
                                              les éléments de H   {a}c    {b}c   {a}∪{b} ({a}∪{b})




1.2.2      Tribu borélienne

     Si l’ensemble Ω possède une structure topologique 1 , la notion de tribu engendrée permet de
définir la plus petite tribu adaptée à cette structure.


       Définition 5.

      Soit (Ω, d) un espace métrique a . On appelle tribu borélienne de Ω, la tribu engendrée
      par les ouverts de (Ω, d). On la note B(Ω) et ses éléments sont appelés les boréliens de
      Ω.
          a. (Ω, d) est un espace métrique si Ω est muni d’une distance d : Ω → R+ vérifiant les propriétés
      suivantes 1. d(x, y) = 0 ⇔ x = y, 2. d(x, y) = d(y, x) et 3. d(x, z) ≤ d(x, y) + d(y, z).




La tribu borélienne sur R (respectivement R) est la tribu engendrée par les intervalles ouverts de
R.



     Exemple 7. [1; 2[ ∈ B(R), en effet, [1; 2[ = ]1; 2[ ∪ {1} avec
                                                         +∞
                                                                         
                                                                  1     1
                                                                           .
                                                          T
       ♢ ]1; 2[ ∈ B(R),                   ♢      {1} =         1 − ;1 +
                                                         n=1      n     n
                                                             |     {z     }
                                                                           An ∈B(R)




1.3        Applications mesurables

     La notion de fonction mesurable étend la notion de fonctions continues. Elle prend son sens
sur des ensembles munis d’une tribu et joueront un rôle important dans l’intégration au sens de
Lebsgue.

    1. T définit une topologie sur Ω si Ω ∈ T , ∅ ∈ T , la stabilité par union finie ou infinie et par intersection finie
est vérifiée.
~~~

## Page 15

~~~text
15                                                                                    1.3. Applications mesurables



       Définition 6.

      Soient (Ω1 , T1 ) et (Ω1 , T1 ) deux espaces mesurables. Soit f : Ω1 → Ω1 . On dit que f est
      (T1 , T2 )-mesurable si l’image réciproque de tout élément de T2 par f appartient à T1 :

                                            ∀B ∈ T2 , f −1 (B) ∈ T1 .




Quand il n’y a pas de confusion possible, on dit que f est mesurable.


     Exemple 8. Si f est une fonction constante sur Ω1 où Ω1 est muni de la tribu T1 alors f
     est mesurable. En effet :
                                        ∀x ∈ Ω, f (x) = y0 , où y0 ∈ Ω2 .

     Ω2 est munie de la tribu T2 . Soit B ∈ T2 , donc
                                                                
                                                                 ∅
                                                                
                                                                         si y0 ∈
                                                                                /B
                           f   −1
                                    (B) = {x ∈ Ω1 , y0 ∈ B} =
                                                                
                                                                          si y0 ∈ B
                                                                
                                                                 Ω
                                                                      1


     Puisque T1 est une tribu sur Ω1 alors Ω1 ∈ T1 et ∅ ∈ T1 , ainsi f −1 (B) ∈ T1 .


       Définition 7.

      Si (X, d) et (Y, δ) sont deux espaces métriques et si f : X → Y est (B(X), B(Y))-
      mesurable, on dit que f est borélienne.


       Propriété 5.

      Soit f : (Ω1 , T1 ) → (Ω2 , T2 ). Si T2 est engendrée par une classe C2 , T2 = σ (C2 ) alors f
      est mesurable si et seulement si ∀B ∈ C2 , f −1 (B) ∈ T1 .



Démonstration .

     • ⇒) Supposons que f est (T1 , T2 )-mesurable. Soit B ∈ C2 .


       Comme T2 = σ (C2 ) alors C2 ⊂ T2 et donc B ∈ T2 . La fonction f étant (T1 , T2 )-mesurable,
       par définition, on obtient le résultat, f −1 (B) ∈ T1 .


     • ⇐) Supposons que ∀B ∈ C2 , f −1 (B) ∈ T1 . Soit D ∈ T2 .
~~~

## Page 16

~~~text
Chapitre 1. Tribu et application mesurable                                                                   16

                                                                                        [
      Comme T2 = σ (C2 ) alors ∃J ⊂ N, ∃Bj ∈ C2 , j ∈ J tels que D =                          Bj .
                                                                                        j∈J

                                                                
                                                           [            [
                                     f −1 (D) = f −1          Bj  =         f −1 (Bj ) .
                                                        j∈J             j∈J


      Comme Bj ∈ C2 alors, par hypothèse, f −1 (Bj ) ∈ T1 . La propriété de stabilité par union
      dénombrable d’une tribu nous conduit à déduire que

                                                 [
                                                       f −1 (Bj ) ∈ T1 .
                                                 j∈J


      Par conséquent, f −1 (D) ∈ T1 . f est donc (T1 , T2 )-mesurable.

      Corollaire 1.

      Soient (X, d) et (Y, δ) deux espaces métriques et soit f : X → Y. Si f est continue a , elle
      est borélienne.
          a. Si f : X → Y avec X et Y munis respectivement d’une structure topologique TX et TY , alors on
      dit que f est continue si f −1 OY ∈ TX .
                                          
                                     |{z}
                                    ∈TY




Attention : la réciproque est fausse. Voir exemple 9

Démonstration . Soit OY un ouvert de l’espace métrique Y, δ). Comme f est continue alors
f −1 (OY ) est un ouvert de l’espace métrique (X, d).

  ⇝ D’après la définition 5, OY ∈ B(Y) et f −1 (OY ) ∈ B(X).

  ⇝ D’après la propriété 5, l’application f est mesurable.


1.4      Quelques propriétés

      Proposition 6.

      Soient (Ω1 , T1 ), (Ω2 , T2 ) et (Ω3 , T3 ) des espaces mesurables. Soient

                               f : Ω1 → Ω2 une fonction (T1 , T2 )-mesurable

                               g: Ω2 → Ω3 une fonction (T2 , T3 )-mesurable

      alors g ◦ f est (T1 , T3 )-mesurable.
~~~

## Page 17

~~~text
17                                                                                                 1.4. Quelques propriétés



Démonstration . Soit B ∈ TZ ,

                                 −1
                                      (B) = f −1 ◦ g −1 (B) = f −1 g −1 (B) ∈ TX .
                                                                          
                          (g ◦ f )
                                                                  | {z }
                                                                                 ∈TY


       Proposition 7 (Opérations sur les fonctions numériques).

       Soient (Ω, T ) un espace mesurable, f, g : (Ω, T ) → (R, B(R)) des fonctions mesurables
       et λ ∈ R, alors les fonctions

                                     f + g, f g, λf, min(f, g), max(f, g)

       sont mesurables.



Démonstration .

     1. On commence par démontrer la mesurabilité de f + g, f g et λf . Pour cela, on utilisera la
       proposition 5.

       On pose Φ l’application définie comme suit :

                                             Φ    :   Ω    → R×R
                                                      x    7→ (f (x), g(x))

       On note Ψ1 et Ψ2 deux applications réelles de R2 définies comme suit :

                     Ψ1     : R×R          → R                          Ψ2      : R×R           → R
                                (x1 , x2 ) 7→ x1 + x2                               (x1 , x2 ) 7→ x1 x2

       Ψ1 et Ψ2 sont continues sur R2 donc d’après le corollaire 1., Ψ1 et Ψ2 sont boréliennes.

       L’application Φ est borélienne, en effet, si V un ouvert de R2 alors il existe des intervalles
       ouverts In et Jn de R tels que il

                                                          [
                                                  V =           (In × Jn ) .
                                                          n∈N


       En particulier,

                                          [                            [
                             Φ−1 (V ) =         Φ−1 (In × Jn ) =             f −1 (In ) ∩ g −1 (Jn ).
                                          n∈N                          n∈N


       Par la mesurabilité de f et de g, f −1 (In ) ∈ T et g −1 (Jn ) ∈ T . Puisque T est stable par
                                                       [
       intersection et par réunion dénombrable alors     f −1 (In ) ∩ g −1 (Jn ) ∈ T . On en déduit que
                                                                 n∈N
~~~

## Page 18

~~~text
Chapitre 1. Tribu et application mesurable                                                                18



      Φ−1 (V ) ∈ T . L’application Φ est donc une fonction mesurable.

        (a) Notons que f + g = Ψ1 ◦ Φ. Ψ1 est borélienne, Φ est (T , B(R))-mesurable. d’après la
            proposition 5., Ψ1 ◦ Φ est donc mesurable.

       (b) Notons que f g = Ψ2 ◦ Φ. Ψ2 est borélienne, Φ est (T , B(R))-mesurable. d’après la
            proposition 5., Ψ2 ◦ Φ est donc mesurable.

        (c) λf est un cas particulier de f g avec g = λ une application constante. Donc λf est
            mesurable.

   2. Soit a ∈ R. Puisque
                            −1                                     
                    min(f, g)      ] − ∞, a[       =       min(f, g) < a    = {f < a} ∩ {g < a} .

                            −1                                     
                    max(f, g)      ]a, +∞[         =       max(f, g) > a    = {f > a} ∪ {g > a} .


      f et g sont mesurables donc {f < a} ∈ T , {f > a} ∈ T , {g < a} ∈ T et {g > a} ∈ T .

      Puisque T est stable par union et par intersection alors

                               {f < a} ∩ {g < a} ∈ T et {f < a} ∪ {g < a} ∈ T

      On déduit que les fonctions min(f, g) et max(f, g) sont mesurables.



     Conséquences
         • Soient fn : Ω → R des fonctions mesurables, alors inf fn , sup fn , lim inf fn et lim sup fn
                                                                     n       n       n             n
            sont mesurables à valeurs dans R.

         • Soit f : Ω → R une fonction mesurable, alors |f | est une fonction mesurable.



      Proposition 8.

     Soient (Ω1 , T1 ) et (Ω2 , T2 ) deux espaces mesurables. Soit (Un )n une suite finie ou infinie
     d’éléments dans T1 telle que Ω1 =         Un . Soit f : Ω1 → Ω2 , alors f est (T1 , T2 )-mesurable
                                            S
                                             n∈N
     si et seulement si f|Un (restriction de f à Un ) est (TUn , TY )-mesurable pour tout n.
~~~

## Page 19

~~~text
19                                                                       1.4. Quelques propriétés




     Exemple 9. X = Y = R, TX = TY = B(R).

                                 f : X→Y
                                                      1
                                                     
                                                      x
                                                            si x ̸= 0
                                      x 7→ f (x) =
                                                     
                                                     
                                                         1   si x = 0
                                                     


     On applique la proposition (8) avec U0 = R∗ et U1 = {0}.


        • R∗ est ouvert ⇒ U0 ∈ B(R)

        • {0} est fermé ⇒ U1 ∈ B(R)

        • U0 ∪ U1 = R

        • f|U0 est continue ⇒ f est (TR∗ , B(R))-mesurable.

        • f|U1 est constante ⇒ f est (T{0} , B(R))-mesurable.
     D’où f est (B(R), B(R))-mesurable.
~~~

## Page 20

~~~text
2 | Introduction à la mesure
    La notion de mesure va étendre la notion usuelle de longueur pour les ensembles de R, ou de
volume pour ceux de Rd , et ceci de deux manières :

   • on veut pouvoir considérer des espaces de base plus généraux, ou plus "abstraits" (espaces
      de dimension infinie, espaces sur lesquels on définit les probabilités, etc . . .)

   • on veut englober dans le même cadre mathématique d’une part les notions de longueur,
      surface, volume, et d’autre part la notion de "masses" ou "charges ponctuelles" que l’on
      rencontre en mécanique ou en électricité.
Sommaire
          2.1    Fonction d’ensembles . . . . . . . . . . . . . . . . . . . . . . . . . . . .            20
          2.2    Mesure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        21
                2.2.1   Exemples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   21
                2.2.2   Conséquences de la σ-additivité . . . . . . . . . . . . . . . . . . . . . . .    23
          2.3    Ensembles négligeables . . . . . . . . . . . . . . . . . . . . . . . . . . .            25
          2.4    Espaces mesurés complets . . . . . . . . . . . . . . . . . . . . . . . . .              27



2.1      Fonction d’ensembles
    Soient Ω un ensemble non vide et P(Ω) l’ensemble des parties de Ω. Soit T ⊂ P(Ω).

      Définition 1.

      Une fonction m : T −→ [0, +∞] est une fonction d’ensembles positive.


Une propriété que l’on exigera d’une telle fonction sera la σ-additivité au sens suivant :

      Définition 2.

      Une fonction m : T −→ [0, +∞] est σ-additive si et seulement si pour toute suite (An )n∈N
      dans T telle que    An ∈ T et An ∩ Ap = ∅ pour n ̸= p,
                        S
                          n∈N

                                                        !
                                              [                 X
                                        m          An       =         m (An ) .
                                             n∈N                n∈N




                                                        20
~~~

## Page 21

~~~text
21                                                                                        2.2. Mesure




2.2       Mesure
      Une "mesure abstraite" est une fonction d’ensemble vérifiant certaines propriétés. Soit Ω un
ensemble non vide.

       Définition 3.

      Soient T une tribu de parties de Ω et m : T −→ [0, +∞] une fonction d’ensembles
      positive. m est une mesure positive sur T si et seulement si les conditions suivantes sont
      vérifiées :

         1. m(∅) = 0 ;

         2. m est σ-additive.




2.2.1      Exemples


     Masse  ou mesure de Dirac
     :::::::::::::::::::::::::::


     Soient x0 ∈ Ω et A ∈ P (Ω). On pose :
                                                 (
                                                     1   si x0 ∈ A
                                     δx0 (A) =
                                                     0   si x0 ∈
                                                               /A

     Si Ω est muni d’une tribu T alors δx0 est une mesure appelée mesure de Dirac de masse 1 et
     concentrée au point x0 .



     Mesure  de comptage
     :::::::::::::::::::::


         Soit m : P(Ω) −→ [0, +∞] définie par
                                         
                                          card A        si A est fini
                                         
                                         
                                m(A) =
                                         
                                                         si A est infini
                                         
                                          +∞




Remarque 1. Par convention, +∞ est considéré ici comme un élément de R = R ∪ {−∞} ∪ {+∞}

     ♢ m est une mesure.

     ♢ m aura beaucoup d’intérêt pour Ω = N.
~~~

## Page 22

~~~text
Chapitre 2. Introduction à la mesure                                                                     22




   Mesure  de Lebesgue sur R
   :::::::::::::::::::::::::::


        Soit Ω l’ensemble des unions finies d’intervalles semi-ouverts. On se donne la fonction
   croissante F : R → R . Si

                                       A = [a1 , b1 [∪[a2 , b2 [∪ · · · ∪ [an , bn [

   avec a1 < b1 < a2 < b2 < · · · < an < bn . On pose

                                                        n
                                                        X
                                           m(A) =             (F (bi ) − F (ai )
                                                        i=1


   avec F (+∞) = sup F (x) et F (−∞) = inf F (x).
                      x∈R                          x∈R
   m est additive sur Ω.
   En prenant F (x) = x pour tout x ∈ R, F (bi ) − F (ai ) est la longueur de l’intervalle [ai , bi [.
   On a alors
                                                              n
                                                              X
                                               m(A) =               (bi − ai )
                                                              i=1

   En prolongeant m à la plus petite tribu contenant Ω, on obtient la mesure de Lebesgue sur
   R, notée λ. On a

                λ ({x}) = 0, ∀x ∈ R et λ ([ai , bi [) = λ (]ai , bi [) = λ ([ai , bi ]) = bi − ai .




Remarque 2. pourquoi ne pas aller plus loin que la σ-additivité ?
On pourrait supposer pour une mesure m définie sur une tribu T , la propriété suivante :
Si {Ai , i ∈ I} est une famille d’éléments de T deux à deux disjoints et tel que   Ai ∈ T avec I
                                                                                 T
                                                                                             i∈I
quelconque (pas forcément dénombrable) alors
                                                [         X
                                            m           Ai =  m(Ai )
                                                  i∈I               i∈I

                                                                                    
Cette propriété n’est pas naturelle, si λ est la mesure de Lebesgue sur R, on a λ {x} = 0 pour
tout x ∈ R, avec la condition précédente, et en écrivant [0, 1] =     {x} on aurait
                                                                  S
                                                                                   x∈[0,1]

                                            X     
                                   λ [0, 1] =   λ {x} = 0, 0 ̸= 1.
                                                   x∈[0,1]
~~~

## Page 23

~~~text
23                                                                                             2.2. Mesure



2.2.2      Conséquences de la σ-additivité
      Soient Ω un ensemble, T une tribu de parties de Ω et m une mesure positive sur T . On a les
propriétés suivantes :

       1. Si (A, B) ∈ T 2 tels que A ⊂ B alors m(A) ≤ m(B).
                                                S     X
       2. Si An ∈ T pour tout n ∈ N, alors m       An ≤     m(An ).
                                                  n∈N         n∈N

       3. Si An ∈ T pour tout n ∈ N, avec An ⊂ An+1 alors
                                           [      
                                       m         An = lim m(An ).
                                                        n→+∞
                                           n∈N


       4. Si An ∈ T pour tout n ∈ N, avec An+1 ⊂ An et m(A0 ) < +∞ alors
                                           \      
                                       m         An = lim m(An ).
                                                        n→+∞
                                           n∈N




Démonstration .

     1. Soit A et B deux ensembles mesurables tels que A ⊂ B. On note

                                            B\A = B ∩ Ω\A .
                                                         


       Remarquons que,
                                    A ∪ B\A = B et A ∩ B\A = ∅.
                                                         


       Comme m est σ-additive alors

                                                        (d’après A ∪ B\A = B)
                                                                        
                           m(B) = m(A) + m(B\A)
                                         | {z }
                                                 ≥0


       Donc m(A) ≤ m(B).

     2. Soit (An )n∈N une suite d’éléments de T . On pose
                                                      [    
                                            A′n = An \   Aj
                                                        j<n


       (A′n ∈ T et A′n peut être éventuellement vide). ∀n ∈ N, on a

                                                                    [             [
                         A′n ⊂ An , A′p ∩ A′q = ∅ pour p ̸= q et          A′n =         An .
                                                                    n∈N           n∈N
~~~

## Page 24

~~~text
Chapitre 2. Introduction à la mesure                                                                                                       24


                                                           S ′
       Comme m est σ-additive, m                    An = m  An =   m(A′n ).
                                               S                P
                                              n∈N                     n∈N               n∈N



      D’après la première propriété, A′n ⊂ An ⇒ m(A′n ) ≤ m(An ). D’où
                                                   [    X
                                                  m   An ≤  m(An ).
                                                       n∈N                n∈N



   3. On garde la construction de la suite (A′n )n∈N de 2. Comme An ⊂ An+1 pour tout entier n
      alors
                                       k
                                       [               k
                                                       [
                                              A′n =          An = Ak , (pour tout k).
                                       n=0             n=0


                                     An                         A′n
                                S                         S          
                          m                   =     m
                               n∈N                        n∈N



                                                           m A′n
                                                    P                 
                                              =                                       ♯ par σ − additivité
                                                    n∈N


                                                               n
                                                                     m A′k
                                                               P                 
                                              =        lim                            ♯ série à termes positifs
                                                    n→+∞ k=0


                                                                      n
                                                                           A′k
                                                                      S          
                                              =        lim m                          ♯ par σ − additivité
                                                    n→+∞             k=0



                                              =        lim m (An )
                                                    n→+∞



   4. Soit Bn = A0 \An . On a Bn ⊂ Bn+1 . D’après Pr.3.

                                                       [
                                                           Bn = lim m(Bn ).
                                                             
                                               m
                                                                      n→+∞
                                                    n∈N


      On a A0 = An ∪ Bn avec An ∩ Bn = ∅ et comme m est σ-additive, alors :

                                                  m(A0 ) = m(An ) + m(Bn )
                                                                                                                                    
      et donc m(Bn ) = m(A0 ) − m(An ). De même     Bn = A0 \                                                    donc m           Bn
                                                 S                                                T                           S
                                                                                                        An                                 =
                                              n∈N                                               n∈N                     n∈N

                       An . Ainsi
                    T
      m(A0 ) − m
                       n∈N

                                                   !
                                          \
                      m(A0 ) − m              An       = lim m(Bn ) = lim [m(A0 ) − m(An )]
                                                           n→+∞                       n→+∞
                                       n∈N

                                                                              
      Par linéarité de la limite, on en déduit m                          An         = lim m(An ) car m(A0 ) < +∞.
                                                                    T
                                                                    n∈N                n→+∞
~~~

## Page 25

~~~text
25                                                                                   2.3. Ensembles négligeables



Remarque 3.         Dans la propriété 4., on peut remplacer l’hypothèse

                                           ”m(A0 ) < +∞”

par "il existe k ∈ N tel que m(Ak ) < +∞".



     Mise en garde.
      Si on ne met pas l’hypothèse m(A0 ) < +∞ (ou il existe k ∈ N tel que m(Ak ) < +∞), la
      propriété 4. n’est plus valable.
      Prenons Ω = N, T = P (N), m la mesure de comptage sur N définie par
                                           (
                                               card A   si A est fini
                                  m(A) =
                                               +∞       si A est infini
                                                                      
      Soit An = {n, n + 1, . . .},     An = ∅, donc m             An       = 0. D’autre part m(An ) = +∞
                                  T                         T
                      T          n∈N                      n∈N

      ∀n ∈ N, donc m        An ̸= lim m(An ).
                        n∈N           n




2.3      Ensembles négligeables
     Les ensembles négligeables jouent un rôle très important dans la théorie de la mesure et de
l’intégration. Les ensembles négligeables vont permettre d’exprimer le fait que certaines proprié-
tés ponctuelles (continuité, convergence simple, majoration,...) n’ont pas lieu en tout point mais
seulement "presque partout", c’est à dire sur le complémentaire d’un ensemble négligeable.
     Il s’avère techniquement nécessaire de ne pas restreindre la notion d’ensemble négligeable aux
seuls sous-ensembles mesurables.
     Dans tout ce chapitre, Ω désigne un ensemble quelconque non vide, T une tribu de parties de
Ω et m une mesure positive sur T . Le triplet (Ω, T , m) est appelé un espace mesuré.

      Définition 4.

      Soit (Ω, T , m) un espace mesuré.

         1. On dit qu’un ensemble N ∈ T est m-négligeable si m(N) = 0.

         2. On dit qu’une partie N de Ω est m-négligeable s’il existe A ∈ T tel que N ⊂ A et
            m(A) = 0.
~~~

## Page 26

~~~text
Chapitre 2. Introduction à la mesure                                                                  26




   Exemple 1. On considère l’espace mesuré (Ω, T , m) où Ω = {a; b; c}, a, b et c des réels et
   T = {Ω, ∅, {a, b}, {c}}.

       • Cas où m = δc :::
         :::::::::::::
                        est::
                            la:::::::
                               mesure:::
                                      de :::::
                                         Dirac::::::::::
                                               concentrée:::
                                                          en ::
                                                             c.

            ⇝ Les parties mesurables de mesure nulle : δc (∅) = 0, δc ({a, b}) = 0 car c ∈
                                                                                         / {a, b}.

            ⇝ Les parties non mesurables négligeables :

                  ♢ {a} ⊂ {a, b} et δc ({a, b}) = 0 donc {a} est δc -négligeable.
                  ♢ {b} ⊂ {a, b} et δc ({a, b}) = 0 donc {b} est δc -négligeable.

          Les ensembles δc -négligeables sont donc ∅, {a, b}, {a} et {b}.

       • :::
         Cas:::
             où::::::: est ::
                m = µd:::: la :::::::
                              mesure ::
                                      de::::::::::
                                         comptage.

            ⇝ Les parties mesurables de mesure nulle : µd (∅) = 0.

            ⇝ Les parties non mesurables négligeables : La seule partie mesurable de mesure
                nulle est l’ensemble vide et ce dernier ne contient aucune partie de Ω.

          L’unique ensemble µd -négligeable est donc ∅.

       • Cas où m = λ est la mesure de Lebesgue.
         ::::::::::::::::::::::::::::::::::::


            ⇝ Les parties mesurables de mesure nulle : λ (∅) = 0, λ (Ω) = λ ({a, b, c}) = 0 car
                {a, b, c} est dénombrable.

                {a, b} ⊂ Ω, {c} ⊂ Ω et λ (Ω) = 0 donc λ ({a, b}) = λ ({c}) = 0.

            ⇝ Les parties non mesurables négligeables : Toutes les parties de Ω sont par définition
                inclues dans Ω, λ (Ω) = 0 donc toutes les parties de Ω sont λ-négligeables.

          Les ensembles λ-négligeables sont donc toutes les parties de Ω.


      Proposition 1.

         1. ∅ est m-négligeable.

         2. Si N est un ensemble m-négligeable, N ′ ∈ T avec N ′ ⊂ N , alors N ′ est m-
            négligeable.

         3. La réunion d’une famille dénombrable d’ensembles m-négligeables est m-
            négligeable.


Remarque 4.        Si Ω = R, m = λ la mesure de Lebesgue et T = B(R), alors pour tout x ∈ R,
{x} est λ-négligeable. {x} est fermé et λ {x} = 0.
                                             
~~~

## Page 27

~~~text
27                                                                         2.4. Espaces mesurés complets




      Mise en garde.
      La réunion d’une famille infinie non dénombrable d’ensembles m-négligeables n’est pas m-
      négligeable.
      En effet, pour Ω = R, T = B(R) et m = λ où λ est la mesure de Lebesgue, on considère

                                                A = [0, 1].

      A ∈ T et λ(A) = 1. A n’est pas λ-négligeable.
      De plus, on peut écrire A =      {x} avec {x} λ-négligeable, ∀x ∈ [0, 1]. Donc
                                   S
                                   x∈[0,1]

                                                  [
                                                          {x}
                                                x∈[0,1]


      n’est pas λ-négligeable.



       Définition 5.

       Une propriété P(x) dépendant de l’élément x ∈ Ω est dite vérifiée m-presque partout
       (ou simplement presque partout quand il n’y a pas d’ambiguïté) si l’ensemble des x de
       Ω pour lesquels la propriété P(x) est fausse est m-négligeable.




On écrira en abrégé P(x) est m-p.p. (ou simplement p.p. quand il n’y a pas d’ambiguïté).



2.4       Espaces mesurés complets
     On a vu dans la définition (4) qu’une partie N de Ω m-négligeable n’est pas nécessairement un
élément de T . Pourtant pour respecter le principe de monotonie croissante de la mesure m, il est
naturel d’attribuer à N la mesure 0. On est alors en train d’élargir la tribu T . D’où la définition
suivante :

       Définition 6.

       Si toutes les parties de Ω m-négligeables sont mesurables, on dit que l’espace (Ω, T , m)
       est complet.



     Exemple 2. On considère l’espace mesuré (Ω, T , m) où Ω = {a; b; c}, a, b et c des réels et
     T = {Ω, ∅, {a, b}, {c}}.
~~~

## Page 28

~~~text
Chapitre 2. Introduction à la mesure                                                                28




       • :::
         Cas:::
             où:::::::: est:::
                m = δc :::  la :::::::
                                mesure :::
                                        de :::::
                                            Dirac:::::::::::
                                                  concentrée ::
                                                             en:::
                                                                c. L’ensemble des parties δc -
          négligeables est
                                             N = {∅, {a, b} , {a} , {b}}

          {a} est δc -négligeable mais non mesurable donc (Ω, T , δc ) n’est pas un espace mesuré
          complet.

       • Cas où m = µ est la mesure de comptage. L’ensemble des parties µd -négligeables est
         :::::::::::::d:::::::::::::::::::::::::



                                                     N = {∅} .

          ∅ est µd -négligeable et mesurable donc (Ω, T , µd ) est un espace mesuré complet.

       • :::
         Cas:::
             où:::::: est ::
                m = λ:::: la :::::::
                             mesure ::
                                     de:::::::::
                                        Lebesgue. L’ensemble des parties λ-négligeables est

                                                    N = P (Ω) .

          {a} est λ-négligeable mais non mesurable donc (Ω, T , λ) n’est pas un espace mesuré
          complet.


    Lorsqu’un espace mesuré (Ω, T , m) n’est pas complet, on peut le compléter canoniquement de
la façon suivante :

      Proposition 2.

     Soit (Ω, T , m) un espace mesuré et soit N l’ensemble des parties m-négligeables. On
     considère
                                       Te = {A ∪ N ; A ∈ T et N ∈ N }.

     Pour tout A ∈ T et pour tout N ∈ N , on pose m(A
                                                  e   ∪ N ) = m(A). Alors

         1. Te est une tribu sur Ω contenant T ;

         2. m
            e définit une mesure positive sur Te qui coïncide avec m sur T ;

         3. Si on note N
                       e la famille des sous-ensembles de X m-négligeables
                                                            e              alors N
                                                                                 e =N;

         4. (Ω, Te , m)
                     e est un espace mesuré complet.



      Définition 7.

     On dit que (Ω, Te , m)
                         e est le complété de l’espace mesuré (Ω, T , m).
~~~

## Page 29

~~~text
29                                                                              2.4. Espaces mesurés complets



Remarque 5.

     • Un espace mesuré complet est égal à son complété.

     • Si P(x) est une propriété dépendant de x ∈ Ω alors, P(x) est vraie m-p.p. si et seulement si
       P(x) est vraie m-p.p.
                      e



      Mise en garde.
      La tribu Te dépend et de la tribu T et de la mesure m par rapport à laquelle on effectue la
      complétion.




     Exemple 3. On considère l’espace mesuré (Ω, T , m) où Ω = {a; b; c}, a, b et c des réels et
     T = {Ω, ∅, {a, b}, {c}}.

        • Cas où m = δc :::
          ::::::::::::::
                         est:::
                             la :::::::
                                 mesure :::
                                         de :::::
                                             Dirac:::::::::::
                                                   concentrée ::
                                                              en:::
                                                                 c. L’ensemble des parties δc -
           négligeables est
                                             N = {∅, {a, b} , {a} , {b}}

           (Ω, T , δc ) n’est pas un espace mesuré complet et son complété est obtenu par union des
           ensembles mesurables et les ensembles négligeables :
                    XX
                       XX       XXX         A∈T
                                       XXX             Ω          ∅        {a, b}       {c}
                      N ∈N                    XXX
                                   ∅                   Ω          ∅        {a, b}       {c}
                                 {a, b}                Ω       {a, b}      {a, b}        Ω
                                  {a}                  Ω        {a}        {a, b}     {a, c}
                                  {b}                  Ω        {b}        {a, b}      {b, c}

                                          Tableau 1. Les unions A ∪ N


           La tribu complétée dans ce cas est donc T̃ = {Ω, ∅, {a, b}, {c}, {a}, {b}, {a, c}, {b, c}}.

        • Cas où m = µd :::
          ::::::::::::::
                         est::
                             la:::::::
                                mesure:::
                                       de::::::::::
                                          comptage. (Ω, T , µd ) est un espace mesuré complet
           donc T̃ = T .

        • Cas où m = λ est la mesure de Lebesgue. L’ensemble des parties λ-négligeables est
          ::::::::::::::::::::::::::::::::::::



                                                    N = P (Ω) .

           (Ω, T , λ) n’est pas un espace mesuré complet et dans ce cas T̃ = P (Ω).
~~~

## Page 30

~~~text
Chapitre 2. Introduction à la mesure                                                            30



Remarque 6 (La tribu de Lebesgue L(R)). Si (Ω, T , m) = (R, B(R), λ). L’espace (R, B(R), λ)
n’est pas complet.

    • La tribu Te est la tribu de Lebesgue sur R et on la note L(R) ;

    • La mesure m
                e s’appelle aussi la mesure de Lebesgue et sera aussi notée λ au lieu de λ
                                                                                         e;

    • Les éléments de L(R) sont appelés parties mesurables au sens de Lebesgue ou parties Lebesgue-
      mesurables.
~~~

## Page 31

~~~text
3 | Intégration de fonctions étagées positives

    Dans la suite de ce cours, on considère l’espace mesuré (Ω, T , µ). Les fonctions étagées jouent,
dans la construction de l’intégrale de Lebesgue, le rôle réservé aux fonctions en escalier dans la
théorie de l’intégrale de Riemann.


Sommaire
            3.1    Fonction indicatrice de Q sur [0; 1]            . . . . . . . . . . . . . . . . . . . .    31

            3.2    Fonctions étagées        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       33

            3.3    Intégrale d’une fonction étagée positive . . . . . . . . . . . . . . . . .                 35

            3.4    Intégration de fonctions mesurables positives                  . . . . . . . . . . . . .   37

            3.5    Principaux théorèmes d’intégration de fonctions positives . . . . . .                      40




3.1         Fonction indicatrice de Q sur [0; 1]
                                                                              (
                                                                                  1     si   x∈Q
    Soit la fonction f définie sur l’intervalle [0; 1] par : f (x) =
                                                                 0   si x ∈/Q
On va montrer que cette fonction n’est pas intégrable au sens de Riemann. Notons
                                          n                              o
                                            (n)  (n)          (n)
                                      Pn = x0 , x1 , · · · , xn−1 , x(n)
                                                                     n


      (n)      (n)              (n)   (n)          (n)
où x0       < x1     < · · · < x n , x0     = 0, xn      = 1 une subdivision du segment [0; 1]. Soit de plus
Cn = {Cn (i)}1≤i≤n un ensemble de points tels que

                                                 (n)                  (n)
                                               xi−1 < Cn (i) < xi .

On définit alors la somme de Riemann S (f, Pn , Cn ) associée à la fonction f , à la subdivision Pn ,
et à l’ensemble Cn par :

                                                       n                         
                                                                         (n)  (n)
                                                       X
                                 S (f, Pn , Cn ) =           f (Cn (i)) xi − xi−1 .
                                                       i=1


                                                              31
~~~

## Page 32

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                                 32



On sait alors que l’intégrale de Riemann IR (f ) de f , si elle existe, est définie par :
                                                 Z 1
                                     IR (f ) =         f (x)dx = lim S (f, Pn , Cn ) .              (3.1)
                                                  0                n→+∞


De plus, cette définition est indépendante du choix de la suite de subdivisions Pn et de l’ensemble
Cn . On considère la subdivision suivante :
                                                                              
                                                            1 2          n−1
                                            Pn =          0; ; ; · · · ;     ;1 ,
                                                            n n           n

et les deux ensembles distincts suivants :
                                                                              i            h
                                                                                (n)    (n)
                         Cn     = {Cn (i)}1≤i≤n                avec   Cn (i) ∈ xi−1 ; xi     ∩ Q.

                           ′
                                       n ′ o                           ′
                                                                              i            h
                                                                                (n)    (n)
                         Cn     =       Cn (i)                 avec   Cn (i) ∈ xi−1 ; xi     \Q.
                                                     1≤i≤n

                                 ′
Autrement dit, Cn (i) et Cn (i) sont respectivement rationnel et irrationnel, on a :
                                                                         ′ 
                           ∀i ∈ {1, · · · , n − 1} , f (Cn (i)) = 1 et f Cn (i = 0.

La relation (3.1) entraine que
                                                                          ′
                                                                             
                                      lim S (f, Pn , Cn ) = lim S f, Pn , Cn .                      (3.2)
                                     n→+∞                          n→+∞


Or
                                                       n                             n
                                                       X                  1       1X
                         S (f, Pn , Cn )         =           f (Cn (i))       =         1   =   1
                                                       i=1
                                                                          n       n i=1

                                                        n    ′ 1                   n
                                   ′
                                                      X                          1X
                         S f, Pn , Cn   =                  f Cn (i)           =         0   =   0
                                                       i=1
                                                                    n             n i=1

ce qui contredit l’égalité (3.2) ainsi la fonction f n’est pas Riemann-intégrable.


Autre point de vue ?

     Construire une subdivision de f ([0; 1]). On sait que f ([0; 1]) = {0; 1} donc on prendra la
subdivision
                                                           Fn = {y0 ; y1 }

où y0 = 0 et y1 = 1, on a bien y0 < y1 . On définit alors la somme S (f, Fn ) associée à la fonction
f et à la subdivision Fn par :

                                                       2
                                                       X
                                                              mesure def −1 ({yi }) yi .
                                                                                   
                                      S (f, Fn ) =
                                                       i=1
~~~

## Page 33

~~~text
33                                                                                    3.2. Fonctions étagées



Si on fait le choix de travailler avec la mesure de Lebesgue λ, alors

                                      = λ f −1 ({0}) × 0 + λ f −1 ({1}) × 1
                                                                      
                         S (f, Fn )


                                      = λ ([0; 1] \Q) × 0 + λ ([0; 1] ∩ Q) × 1


                                      =     1×0+0×1


                                      =     0.

N’ayant qu’une seule subdivision possible, la somme S correspond alors à l’intégrale qu’on souhaite
calculer.




3.2       Fonctions étagées

       Définition 1.
      Soit f une fonction de Ω dans R. La fonction f est dite T -étagée si f est (T , B(R))-
      mesurable et f (Ω) est un sous-ensemble fini de R.



                                       n
     Exemple 1. Soit n ∈ N∗ . φ =           ai 1Ai où ai ∈ R et Ai ∈ T pour tout i ∈ J1, nK.
                                       P
                                      i=1

        • φ est mesurable car c’est une combinaison linéaire de fonctions mesurables.

        • φ prend un nombre fini de valeurs (ai )i=1,··· ,n

     φ est donc une fonction T -étagée.



     Notations :
                                  E(Ω, T ) = {f : Ω → R T - étagées}

                              E+ (Ω, T ) = {f : Ω → [0, +∞[ T - étagées}



Représentation  canonique d’une fonction étagée
::::::::::::::::::::::::::::::::::::::::::::::::


     Soit f une fonction étagée. Désignons par a1 , . . . , am les éléments de f (Ω), la suite (ai )1≤i≤m
étant strictement croissante, et posons pour tout i ∈ J1, mK

                                                 Ai = f −1 ({ai }) .
~~~

## Page 34

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                                    34



Les sous-ensembles A1 , A2 , . . . , Am de Ω sont non vides, mesurables, deux à deux disjoints et de
réunion Ω. Ainsi f s’écrit sous la forme

                                                              m
                                                              X
                                                         f=         ai 1Ai                             (3.3)
                                                              i=1


Inversement, étant données une suite strictement croissante (ai )1≤i≤m d’éléments de R et une suite
(Ai )1≤i≤m de sous-ensembles de Ω, mesurables, non vides, deux à deux disjoints et dont la réunion
est Ω, il existe une fonction étagée f de Ω dans R et une seule telle que

                                                              m
                                                              X
                                                     f=             ai 1Ai .
                                                              i=1


On dira que le couple (a1 , . . . , am ), (A1 , . . . , Am ) est le couple canonique de f et que (3.3) est la
                                                            

représentation canonique de f .


   Exemple 2.

       1. Soit A ∈ T \ {∅}. La fonction u = 1A est étagée et a pour représentation canonique

                                                    u = 0 × 1AC + 1 × 1A .


       2. Ω = R, T = B(R). Soit φ = 1]0,+∞[ , son écriture canonique est :

                                             φ = 0 × 1]−∞,0] + 1 × 1]0,+∞] .

          D’autres écritures non canoniques de φ :

             0 ×1]−∞,0]+ 1 ×1]0,1[ + 1 ×1[1,+∞[
        φ = |{z}                                                         a2 = a3 =⇒ pas canonique
                        |{z}        |{z}
                 a1                 a2              a3




                            1            2
        φ = 0 × 1] − ∞, 0] + × 1]0, +∞[ + × 1]0, +∞[ , A2 ∩ A3 ̸= ∅ =⇒ pas canonique
                 | {z } 3       | {z } 3     | {z }
                          A1                   A2                         A3




      Propriétés 2 (Opérations sur les fonctions étagées).

      Soient φ et ψ deux fonctions étagées sur Ω, α et β deux réels alors les fonctions

                               • αφ + βψ       • φψ           • sup(φ, ψ)       • inf(φ, ψ)

      sont des fonctions étagées sur Ω.
~~~

## Page 35

~~~text
35                                                                              3.3. Intégrale d’une fonction étagée positive




3.3       Intégrale d’une fonction étagée positive

       Définition 2.
                               m
                               X
      Soit φ ∈ E+ (Ω, T ) et         ai 1Ai sa représentation canonique. On appelle intégrale de φ sur
                               i=1
                                                       Z               Z                              m
                                                                                                      X
      Ω par rapport à la mesure µ et on note                φdµ ou           φ(x)dµ(x), la somme             ai µ(Ai ) :
                                                        Ω                Ω                             i=1

                                             Z               m
                                                             X
                                                     φdµ =         ai µ(Ai )
                                                 Ω           i=1




                                                                                       m
En vertu de la convention 0 × µ(A) = 0 si µ(A) = +∞, la somme                                ai µ(Ai ) a toujours un sens
                                                                                       P
                                                                                       i=1
dans [0, +∞] puisque chaque terme ai µ(Ai ) appartient à [0, +∞].
                                                              Z
On dit qu’une fonction étagée et positive φ est µ-intégrable si                       φdµ < +∞.
                                                                                  Ω




     Exemple 10. On prend (Ω, T ) = (R, B(R)) et φ = 1R . Il est clair que φ ∈ E+ (X, T ).
                          Z
       • Pour µ = λ, on a   φdλ = λ(R) = +∞.
                                R
                                Z
        • Pour µ = δ0 , on a         φdδ0 = δ0 (R) = 1
                                 R




       Définition 3.           m
                               X
      Soit φ ∈ E+ (Ω, T ) et         ai 1Ai sa représentation canonique. Soit A une partie mesurable.
                               i=1
      On définit l’intégrale de φ sur A :
                                     Z           Z                 m
                                                                   X
                                         φdµ =       φ1A dµ =            ai µ(Ai ∩ A).
                                     A           Ω                 i=1




     Le calcul de l’intégrale d’une fonction étagée à partir de la définition (2) nécessite la dé-
composition canonique. Le lemme suivant nous permet d’alléger le recours systématique à cette
décomposition.
~~~

## Page 36

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                                                                    36



      Lemme 1.
                                                                                        p
                                                                                        X
      Soit φ une fonction étagée positive telle que φ =                                          ti 1Ci où Ci sont des ensembles
                                                                                         i=1
      mesurables et disjoints deux à deux et ti sont des constantes pas forcément distinctes
      alors                                               Z                 p
                                                                            X
                                                               φdµ =              ti µ(Ci ).
                                                          Ω                 i=1




      Propriétés 3.

      Soient φ ∈ E+ (Ω, T ), ψ ∈ E+ (Ω, T ) et r ∈ [0, +∞[.
                              Z             Z
            Homogénéité :
         ♠ ::::::::::::::        rφdµ = r      φdµ.
                                        Ω                         Ω
                              Z                               Z               Z
         ♠ Additivité
           :::::::::::
                      :               (φ + ψ)dµ =                     φdµ +           ψdµ.
                                Ω                              Ω                  Ω
                                                  Z                    Z
         ♠ Croissance :φ≤ψ ⇒
           ::::::::::::
                                                          φdµ ≤             ψdµ.
                                                  Ω                     Ω




Démonstration .
                                        m
                                        X
   1. Soient φ ∈ E+ (Ω, T ) et                ai 1Ai sa représentation canonique. Si r = 0,
                                        i=1

                                                      Z                                      Z
                                                              0 × φdµ = 0 = 0 ×                    φdµ.
                                                      Ω                                        Ω

                                                      Z                                          Z
       Il convient de remarquer que si                        φdµ = +∞ alors 0 ×                       φdµ = 0 en vertu de la convention
                                                          Ω                                        Ω
       0 × µ(A) = 0 si µ(A) = +∞.

       Si r > 0. La suite (ai )1≤i≤m est strictement croissante donc la suite (rai )1≤i≤m est strictement
                                                 m
                                                 X
       croissante car r est strictement positif.    rai 1Ai est donc la représentation canonique de rφ
                                                                      i=1
       donc rφ est une fonction étagée positive. D’après la définition de l’intégrale d’une fonction
       étagée :
                                  Z                   m
                                                      X                               m
                                                                                      X                     Z
                                        rφdµ =                rai µ(Ai ) = r                ai µ(Ai ) = r         φdµ.
                                    Ω                 i=1                             i=1                     Ω

                                                                              n
                                                                              X                            m
                                                                                                           X
                                              2
   2. Soient (φ, ψ) ∈ (E+ (Ω, T )) telles que φ =                                     ai 1Ai et ψ =               bi 1Bi leur représentation
                                                                              i=1                          i=1
       canonique. φ + ψ est une fonction étagée et

                                                                      n X
                                                                      X m
                                                  φ+ψ =                           (ai + bj ) 1Ai ∩Bj ,
                                                                      i=1 j=1
~~~

## Page 37

~~~text
37                                                                                       3.4. Intégration de fonctions mesurables positives



       (Ai ∩ Bj )i,j sont disjoints deux à deux. Notons que ai + bj ne sont pas forcément distincts
       deux à deux.

       D’après le lemme
                           Z                              n X
                                                          X m
                                (φ + ψ) dµ =                            (ai + bj ) µ (Ai ∩ Bj )
                            Ω                             i=1 j=1


                                                          n
                                                          X            m
                                                                       X                       m
                                                                                               X            n
                                                                                                            X
                                                   =              ai         µ (Ai ∩ Bj ) +            bj         µ (Ai ∩ Bj )
                                                          i=1          j=1                     j=1          i=1


                                                          n
                                                          X                        m
                                                                                   X
                                                   =              ai µ (Ai ) +           bj µ (Bj )
                                                          i=1                      j=1

                                                                                                        
                     m
                     X                               m
                                                     [                                        m
                                                                                              [                              m
                                                                                                                             [
       En effet,           µ (Ai ∩ Bj ) = µ               Ai ∩ Bj  = µ Ai ∩                      Bj  et comme                  Bj = Ω alors
                     j=1                             j=1                                     j=1                             j=1
       m
       X                                                                                     n
                                                                                             X
              µ (Ai ∩ Bj ) = µ(Ai ). De la même façon, on obtient                                  µ (Ai ∩ Bj ) = µ(Bj ).
        j=1                                                                                  i=1

                     Z              n
                                    X                     Z                  m
                                                                             X
       Puisque           φdµ =            ai µ (Ai ) et           ψdµ =            bj µ (Bj ), on en déduit l’égalité recherchée.
                     Ω              i=1                    Ω                 j=1

     3. Si φ ∈ E+ (Ω, T ), ψ ∈ E+ (Ω, T ) et φ ≤ ψ alors ψ − φ ∈ E+ (Ω, T ). Remarquons que

                                                                  ψ = (ψ − φ) + φ.
                                                   Z                   Z                       Z                         Z
       Par additivité, on peut écrire   ψdµ =   (ψ − φ) dµ +                                        φdµ. Puisque              (ψ − φ) dµ ≥ 0
             Z         Z              Ω Z      Ω Z                                              Ω                         Ω

       alors   ψdµ −      φdµ ≥ 0, soit    φdµ ≤    ψdµ.
                 Ω              Ω                             Ω                Ω


       Proposition 9.

       Si (φn )n∈N est une suite croissante
                                         Zde fonctions
                                                       étagées positives qui tend µ-p.p vers une
                                                                   Z
       fonction étagée φ, alors la suite     φn dµ       tend vers    φdµ :
                                                           Ω                 n∈N                   Ω

                                              Z           Z                                      Z
                                      lim            φn dµ =                   lim φn dµ =                 φdµ.
                                    n→+∞         Ω                         Ω n→+∞                      Ω




3.4       Intégration de fonctions mesurables positives
      Soit (Ω, T ) un espace mesurable. On note
~~~

## Page 38

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                                           38



                         L+ (Ω, T ) = f : Ω → [0, +∞], T , B R+ -mesurables.
                                                              


Le théorème suivant nous permettra de faire le lien entre les fonctions étagées positives et les
fonctions mesurables positives. Il sera d’une grande utilité dans la démonstration de beaucoup de
propriétés dans les exercices.

      Théorème 1.

      Si f ∈ L+ (Ω, T ), il existe une suite croissante (φn )n dans E+ (Ω, T ) telle que (φn )n
      converge simplement vers f sur Ω. Si de plus, f est bornée, alors (φn )n converge unifor-
      mément vers f sur Ω.




Démonstration . Pour n et k dans N, on pose
                                                                  
                                      k           k+1
                  An,k =       x ∈ Ω, n ≤ f (x) <                        et An = {x ∈ Ω, f (x) ≥ n} .
                                      2            2n

                           n
                                              !
                           X k
On considère φn =                     1An,k       + n1An .
                                 2n
                           k=0
À n fixé :

    • Si f (x) ≥ n alors φn (x) = n.
                                                                      
                                                                 k k+1              k
    • Sinon il existe k ∈ {0, · · · , n2n }, f (x) ∈               ,     ⇒ φn (x) = n .
                                                                 2n 2n             2
       Montrons que φn ≤ φn+1 (n ∈ N).
                                  k
       ⇝ Si x ∈ An,k , φn (x) = n , calculons φn+1 (x).
                                 2
                                                                       
                                k k+1           2k 2k + 1     2k + 1 2k + 2
                       f (x) ∈ n , n       = n+1 , n+1 ∪            ,
                                2    2        2       2        2n+1 2n+1
                                                                                                   
                                          2k   k                                         2k2k + 1
                                      
                                      
                                        n+1
                                             = n                           si f (x) ∈ n+1 , n+1
                                      
                                      
                                       2     2                                       2     2
                      φn+1 (x) =
                                                                                                      
                                       2k + 1   k    1                               2k + 1 2k + 2
                                                                           si f (x) ∈
                                      
                                      
                                              = n + n+1                                    ,
                                         2n+1   2   2                                  2n+1 2n+1
       donc φn+1 (x) ≥ φn (x).                                                                   
                                                                                1        1
       ⇝ Si x ∈ An alors φn (x) = n et φn+1 (x) =                       n, n + n+1 , n + n , . . . Donc φn+1 ≥ |{z}
                                                                                                                n .
                                                                              2         2
                                                                                                               φn
       Soit x ∈ Ω, alors

          ⋆ ou bien f (x) = +∞,
             ∀n ∈ N, x ∈ An ⇒ φn (x) = n → +∞ lorsque n → +∞ et donc f (x) = lim φn (x)
                                                                                                    n→+∞
~~~

## Page 39

~~~text
39                                                                            3.4. Intégration de fonctions mesurables positives



          ⋆ ou bien f (x) < +∞, il existe n0 ∈ N tel que f (x) ≤ n0 .

                                                                                  1
                       ∀n ≥ n0 , x ∈ An,k , | φn (x) − f (x) |≤                     → 0,        lorsque n → +∞
                                                                                 2n

            donc (φn )n converge simplement vers f sur Ω.
            Si f est bornée, il existe n0 ∈ N, ∀n ≥ n0 , | f (x) |≤ n0 , on se replace dans le deuxième
            cas et on a la convergence uniforme de (φn )n vers f sur Ω.


       Définition 4.

      Soit f une fonction de f de L+ (Ω,ZT ). On appelle
                                                   Z     intégrale de Lebesgue de f sur Ω par
      rapport à la mesure µ, et on note               f dµ ou        f (x)dµ(x), l’élément de [0, +∞] suivant
                                                  Ω             Ω

                                             Z                                             
                               I(f ) = sup          φdµ, φ ∈ E+ (Ω, T ), φ ≤ f                  .


      Autrement dit,       Z                   Z                                              
                                  f dµ = sup          φdµ, φ ∈ E+ (Ω, T ), φ ≤ f                    .
                              Ω
                                                      Z              Z
      Plus généralement, si A ∈ T , on pose                 f dµ =           f 1A dµ.
                                                        A             Ω




      Mise en garde.
                                      Z                                                                          Z
      Bien distinguer le fait que      f dµ a toujours un sens dans [0, +∞] et le fait que                             f dµ est
                          Z         Ω                                                                              Ω

      finie, c’est à dire   f dµ ∈ [0, +∞[. D’où la définition suivante :
                          Ω




       Définition 5.

      Soit f ∈ L+ (Ω, T ). On dit que f est µ-intégrable Zsur Ω (ou simplement intégrable quand
      il n’y a pas de risque de confusion) si l’intégrale                    f dµ est finie.
                                                                         Ω




     Exemple 3. La fonction 1R est δ0 -intégrable sur R mais n’est pas λ-intégrable sur R.
~~~

## Page 40

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                             40




3.5       Principaux théorèmes d’intégration de fonctions positives


    Le développement de la théorie de l’intégration sur L+ (Ω, T ) repose sur un important théorème
de convergence des intégrales, propre aux suites croissantes d’éléments de L+ (Ω, T ), qui permet
sous un minimum d’hypothèses de commuter "intégration" et "passage à la limite".




      Théorème 2 (Théorème de convergence monotone ou de Beppo-Levi).

      Soit (fn )n∈N une suite croissante de fonctions de L+ (Ω, T ) qui tend µ-p.p vers une
      fonction f , alors

         1. f ∈ L+ (Ω, T ),
                     Z                                                 Z
         2. La suite      fn dµ             converge en croissant vers         f dµ.
                                      n∈N




     Cas particulier :
      Soit (An )n∈N une suite d’ensembles de T , telle que An ⊂ An+1 pour n ∈ N. Alors
                                                                           !
                                                                [
                                              lim µ (An ) = µ         An       .
                                             n→+∞
                                                                n∈N


      En effet, la fonction indicatrice 1An est mesurable, positive, croissante et lim 1An = 1S An .
                                                                                  n→+∞        n
                                                    Z             Z
      D’après le théorème de Beppo-Lévi : lim          1An dµ =       1 An dµ.
                                                                       S
                                              n→+∞ Ω               Ω! n
                Z                                             [
      Puisque       1An dµ = µ(An ) alors lim µ (An ) = µ         An .
                  Ω                             n→+∞
                                                                    n
~~~

## Page 41

~~~text
41                                                                                     3.5. Principaux théorèmes d’intégration de fonctions positives



       Propriétés 4 (Propriétés de l’intégrale de fonctions positives).

      Soient f et g deux fonctions mesurables et positives sur Ω. Soient A et B deux ensembles
      mesurables. α ∈ [0, +∞].
           Z               Z
        1.    (αf ) dµ = α   f dµ (Homogénéité positive).
                  Ω                         Ω
               Z                            Z                    Z
         2.           (f + g) dµ =              f dµ +                   gdµ (Additivité).
                  Ω                         Ω                     Ω
                             Z                      Z
         3. f ≤ g =⇒                f dµ ≤                  gdµ (Croissance de l’intégrale).
                                Z                       Z
         4. A ⊂ B =⇒                    f dµ ≤                  f dµ.
                                   A                        B

         5. Soit (Ai )i une famille d’ensembles mesurables et disjoints deux à deux, alors
                                                                     Z                         XZ
                                                                         S
                                                                                   f dµ =                     f dµ.
                                                                              Ai               i≥1       Ai
                                                                      i≥1



                                                                     Z                             Z                          Z
         6. Si N est µ-négligeable alors                                      f dµ = 0 et                      f dµ =                 f dµ.
                                                                         N                           Ω\N                          Ω
                                                                          Z
         7. f = 0 µ-p.p si et seulement si                                       f dµ = 0.
                                                                             Ω
                                                        Z
         8. Si f ∈ L+ (X, T ) et si                             f dµ < +∞, alors {x ∈ Ω, f (x) = +∞} est µ-négligeable.
                                                        Ω




Démonstration .                  f, g ∈ L+ (Ω, T ), donc d’après le théorème (2), il existe (φn )n et (ψn )n dans
E+ (Ω, T ) telles que φn ↗n f et ψn ↗n g.

                                    Z                                             Z
     1. αφn ↗n αf          ⇒                (αf ) dµ = lim                             αφn dµ, et puisque φn ∈ E+ (Ω, T ) alors
                                        Ω                            n→+∞          Ω

                                    Z                                              Z                                  Z                       Z
                          lim               αφn dµ = lim α                                φn dµ = α lim                       φn dµ = α               f dµ;
                         n→+∞          Ω                         n→+∞                 Ω                  n→+∞             Ω                       Ω



     2. φn + ψn ↗n f + g
           Z                                    Z                                             Z                 Z                    
       ⇒           (f + g) dµ = lim                 (φn + ψn ) dµ = lim                            φn dµ +                ψn dµ           car φn , ψn ∈ E+ (Ω, T )
              Ω                         n       Ω                                         n    Ω                      Ω

                               Z                                          Z                          Z                        Z               Z
                           ⇒           (f + g) dµ = lim                            φn dµ + lim             ψn dµ =                f dµ +          gdµ
                                 Ω                                   n        Ω                n       Ω                      Ω               Ω
~~~

## Page 42

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                                                                           42



   3. La croissance. Soient f et g deux fonctions mesurables et positives. On a
                                          Z                         Z                                                     
                                               f dµ = sup                  φdµ, φ ∈ E+ (Ω, T ), φ ≤ f

                                          Z                         Z                                                     
                                               gdµ = sup                   φdµ, φ ∈ E+ (Ω, T ), φ ≤ g

        Si on suppose que f ≤ g alors on a
                        Z                                                                Z                                               
                                  φdµ, φ ∈ E+ (Ω, T ), φ ≤ f                           ⊂            φdµ, φ ∈ E+ (Ω, T ), φ ≤ g


        Par passage au sup, on obtient                                 Z                   Z
                                                                           f dµ ≤                  gdµ.

   4. Soient A et B deux ensembles mesurables donc 1A et 1B sont deux fonctions mesurables et
        positives. Puisque A ⊂ B alors 1A ≤ 1B . Donc 1A f ≤ 1B f.
                                                  Z          Z
        Par croissance de l’intégrale, on obtient   1A f dµ ≤ 1B f dµ. Donc

                                                                       Z                   Z
                                                                           f dµ ≤                  f dµ.
                                                                       A                       B

        Z                     Z
   5.       S
                     f dµ =           f 1 S Ai dµ. Comme les ensembles Ai sont mesurables et disjoints deux à
                Ai                Ω     i≥1
         i≥1
                                        X
        deux alors 1 S Ai =                   1Ai . Donc
                            i≥1
                                        i≥1

                                                                                                       
                                                    Z                                  Z        X
                                                             f 1 S Ai dµ =                       f 1Ai  dµ
                                                         Ω       i≥1                   Ω           i≥1

                                              
                        Z         X                           X Z                     
        Et comme                       f 1Ai  dµ =                           f 1Ai           d’après le lemme de Fatou (3.4) alors
                         Ω        i≥1                         i≥1          Ω


                                           Z                           X Z                               X Z            
                                               S
                                                         f dµ =                        f 1Ai           =               f       .
                                                    Ai                 i≥1         Ω                       i≥1    Ai
                                              i≥1



                                                                                           Z                Z             
   6. Par la propriété de la croissance, f ≤ sup f ⇒                                               f dµ ≤         sup f            dµ. De plus
                                                                           Ω               N                 N     Ω

                                         Z                                               Z
                                                   sup f         dµ = sup f ×                      dµ = sup f × µ(N ).
                                           N        Ω                          Ω               N            Ω


        N est µ-négligeable donc µ(N ) = 0, ainsi sup f × µ(N ) = 0.
                                                                                   Ω
~~~

## Page 43

~~~text
43                                                             3.5. Principaux théorèmes d’intégration de fonctions positives



          Même si supΩ f = +∞, on a par covnetion +∞(N ) = 0 si µ(N ) = 0.


          On démontre l’autre égalité en remarquant que f = 1N f + 1Ω\N f et en appliquant la
          propriété de linéarité.

     7.        • Supposons que f = 0 µ-p.p. Soit A = {x ∈ Ω, f (x) > 0} = f −1 (]0; +∞[). Donc A ∈ T
                 et par hypothèse, A est µ-négligeable. Considérons la fonction g définie sur Ω par
                                                               (
                                                                    +∞           si x ∈ A
                                                      g(x) =
                                                                    0            sinon
                                                                        Z               Z
                 g ∈ L+ (Ω, T ), g ≥ f donc par croissance,                     gdµ ≥        f dµ.
                                                                         Ω               Ω
                 En appliquant le théorème de Beppo-Lévi à la suite de fonctions mesurables positive et
                 croissante (n1A )n ,
                                                          Z                     Z
                               g = lim (n1A ) ⇒               gdµ = lim             n1A dµ = lim nµ(A) = 0.
                                          n                                 n                        n

                                  Z               Z
                 Finalement, de                       f dµ ≥ 0 et       gdµ, on déduit que
                                                                    R                                    R
                                          gdµ ≥                                                              f dµ = 0.
                                      Ω           Ω
               • Supposons que        f dµ = 0. Comme f est (T , B(R))-mesurable, alors
                                  R


                                              {x ∈ Ω, f (x) > 0} = f −1 (]0, +∞[) ∈ T .

                 D’autre part, on a

                                                                             [                          1
                                                                                                             
                                              {x ∈ Ω, f (x) > 0} =                   x, f (x) ≥
                                                                                                         n
                                                                            n∈N∗

                                              
                                             1               1
                 On pose An = x, f (x) ≥         , donc f ≥ 1An , ∀n ∈ N∗ .
                                             n               n      Z         Z       
                                                                                  1
                 D’après la propriété de croissance de l’intégrale,    f dµ ≥       1An dµ.
                                                                     Ω         Ω  n
                         Z         
                              1             1                1
                 De plus        1A dµ = µ(An ) et 0 ≥ µ(An ) ≥ 0, ainsi ∀n ∈ N∗ , µ(An ) = 0 donc
                              n n           n                n
                 l’ensemble {x ∈ Ω, f (x) > 0} est réunion dénombrable d’ensembles µ-négligeables, donc
                 il est µ-négligeable.

                 Conclusion.
                 ::::::::::
                             {x ∈ Ω, f (x) > 0} est µ-négligeable donc f = 0 µ-p.p.

     8. Soit A = {x ∈ Ω, f (x) = +∞}, A ∈ T car A = f −1 ({+∞}).
                                    Z                               Z
                                                                  1
        ∀n ∈ N∗ , f ≥ n1A ⇒ ∀n ∈ N∗     f dµ ≥ nµ(A) ⇒ 0 ≤ µ(A) ≤      f dµ ∀n ∈ N∗ .
                                      Ω                           n  Ω
        Z
           f dµ < +∞ donc µ(A) = 0.
           Ω
~~~

## Page 44

~~~text
Chapitre 3. Intégration de fonctions étagées positives                                                             44



En l’absence de l’hypothèse de croissance sur la suite de fonctions de L+ (Ω, T ), on a tout de même
le résultat partiel suivant :

      Corollaire 2 (Lemme de Fatou).

      Soit (fn )n une suite de fonctions de L+ (Ω, T ) alors
                                        Z                                     Z
                                              lim inf fn dµ ≤ lim inf              fn dµ.




Démonstration . Pour tout x ∈ Ω, on note pour p ∈ N, gp (x) = inf fn (x). On a
                                                                                                n≥p


                       (lim inf fn )(x) = lim inf fn (x) = sup[ inf fn (x)] = sup[gp (x)]
                                                                      p∈N n≥p                      p


    • ∀p ∈ N, gp ≤ gp+1 et gp ≥ 0 donc                        lim [gp (x)] = sup[gp (x)] et d’après le théorème de la
                                                          p→+∞                    p∈N
       convergence monotone, on a
                                        Z                 Z                           Z
                                  lim         gp dµ =              lim gp dµ =              (lim inf fn )dµ.    (3.4)
                                p→+∞      Ω                    Ω p→+∞                   Ω


    • D’autre part, on a pour tout entier p, gp = inf fn , donc
                                                                    n≥p


                                                          ∀n ≥ p, gp ≤ fn .

       Par la propriété de la croissance de l’intégrale, on obtient pour tout entier p et tout entier n
       tel que n ≥ p                                      Z              Z
                                                               gp dµ ≤       fn dµ.

       Ceci étant vrai pour tout entier n supérieur à l’entier p, on en déduit par passage à la borne
       inférieure que                                          Z                   Z
                                              ∀p ∈ N,              gp dµ ≤ inf            fn dµ
                                                                             n≥p

       Ainsi                                          Z                           Z
                                               sup        gp dµ ≤ sup inf              fn dµ.                   (3.5)
                                               p∈N                   p∈N n≥p

       Comme (gp )p est croissante, la propriété de la croissance de l’intégrale nous permet de déduire
           Z                                      Z              Z
       que    gp dµ est croissante et que lim          gp dµ = sup gp dµ. De (3.4) et (3.5), on déduit
                                                          p→+∞                    p∈N
                         p
       que                                                Z                       Z
                                                lim            gp dµ ≤ lim inf            fn dµ.
                                              p→+∞


    Les séries de fonctions sont d’utilisation courante, il est utile de donner l’expression du théorème
de la convergence monotone dans ce cas.
~~~

## Page 45

~~~text
45                                                      3.5. Principaux théorèmes d’intégration de fonctions positives



      Théorème 3 (intégration d’une série de fonctions de L+ (Ω, T )).

     Soit (fn )n≥0 une suite d’éléments de L+ (Ω, T ). Alors
           Z     +∞
                      !        +∞ Z        
                X              X
        1.          fn dµ =            fn dµ ;
            Ω    n=0               n=0   Ω

                +∞ Z
                X                
        2. Si               fn dµ < +∞ alors il existe un ensemble N mesurable et µ-négligeable
                n=0    Ω
                      +∞
                      X
           tel que          fn < +∞ sur Ω\N.
                      n=0




     En pratique, on utilisera souvent des intégrales par rapport à la mesure de Lebesgue, les
théorèmes suivants expriment des cas où on peut se ramener à un calcul d’intégrale au sens de
Riemann. Les propriétés suivantes seront valables pour des fonctions mesurables positives ou de
signe quelconque.

      Théorème 4.

     Soit f : [a, b] → R une fonction mesurable.

        1. Si f est Riemann intégrable, alors f est Lebesgue intégrable et les intégrales sont
           égales, autrement dit
                                             Z                 Z b
                                                      f dλ =         f (x) dx
                                              [a,b]             a


        2. Si f est bornée alors f est Riemann intégrable ssi

                               λ ({x ∈]a, b[ tel que f n’est pas continue en x}) = 0,

           autrement dit, si et seulement si l’ensemble des points de discontinuités de f dans
           ]a, b[ est de mesure de Lebesgue nulle.



      Corollaire 3.

     Soit f : [0, +∞[→ R une fonction mesurable et Riemann intégrable sur tout intervalle
     [0, n], n ∈ N.                                         Z n
     f est Lebesgue intégrable sur [0, +∞[ ssi lim                   |f (x)| dx < +∞.
                                              n→∞              0
                  Z +∞             Z
     Dans ce cas,       f (x) dx =       f dλ.
                       0                 [0,+∞[
~~~

## Page 46

~~~text
4 | Intégration de fonctions mesurables
    Dans tout ce chapitre, Ω désigne un ensemble quelconque non vide, T une tribu de parties de
Ω et µ une mesure positive sur T . Dans la suite de ce cours, on considère l’espace mesuré (Ω, T , µ).

Sommaire
          4.1    Intégration de fonctions réelles . . . . . . . . . . . . . . . . . . . . . .            46
          4.2    Propriétés de l’intégrale de fonctions réelles . . . . . . . . . . . . . .              48
          4.3    Mesures à densité - Théorème de Radon-Nikodym . . . . . . . . . .                       51
                4.3.1   Mesure définie par une densité . . . . . . . . . . . . . . . . . . . . . . .     51
                             p      p
          4.4    Espaces L et L         . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    54
          4.5    Normes sur Lp (p ∈ [1, +∞[) . . . . . . . . . . . . . . . . . . . . . . . . .           57
          4.6    Espaces L∞ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          58
                4.6.1   Théorème de Radon Nikodym . . . . . . . . . . . . . . . . . . . . . . . .        60
                4.6.2   Mesure image . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   61

    On présentera les théorèmes fondamentaux d’intégration au sens de Lebesgue de fonctions
mesurables positives ou de signe quelconque. On s’intéressera à la définition de nouvelles mesures
à partir d’autres mesures. Ces mesures ont une grande importance dans l’articulation du cours de
probabilité.



4.1      Intégration de fonctions réelles
    On étend la notion d’intégrale et d’intégrabilité aux fonctions réelles mesurables de signe quel-
conque en se basant sur les définitions et les propriétés de fonctions mesurables et positives. Soit
(Ω, T ) un espace mesurable. On note

                             L(Ω, T ) = f : Ω → R, (T , B (R)) -mesurables.
                                       


      Définition 1.
      Une fonction f de Ω dans R est dite µ-intégrable si f est (T , B(R))-mesurable et
                                    Z                       Z
                                        f + dµ < +∞ et          f − dµ < +∞.




                                                       46
~~~

## Page 47

~~~text
47                                                                                                4.1. Intégration de fonctions réelles



          Définition 2.
                                                                                    Z             Z              Z
          Si f est µ-intégrable. On appelle intégrale de f , notée                      f dµ ou        f dµ ou       f (x)dµ(x)
                                                                                                   Ω             Ω
          le nombre                               Z                    Z
                                                           +
                                                           f dµ −           f − dµ.
                                                      Ω                 Ω

          On note L1R (Ω, T , µ) (ou en abrégé L1 ) l’ensemble des fonctions µ-intégrables.




          Théorème 1.

            1. Si f ∈ L(Ω, T ), on a l’équivalence suivante
                                                                            Z
                                                       1
                                          f ∈ L (Ω, T , µ) ⇐⇒                   |f | dµ < +∞

                                              Z                Z
            2. Si f ∈ L1 (Ω, T , µ), alors            f dµ ≤        |f | dµ.




Démonstration .

                                                  Z                             Z
     1. ⇝ Soit f ∈ L1 (Ω, T , µ), donc                 f + dµ < +∞ et               f − dµ < +∞. Comme | f |= f + + f −
          alors par la propriété de l’additivité des intégrales de fonctions mesurables et positives
                                              Z                    Z         Z
                                                      | f | dµ =     f + dµ + f − dµ .
                                                                   | {z } | {z }
                                                                       <+∞              <+∞

                             Z
          Il s’en suit que       | f | dµ < +∞.
          ⇝ Réciproquement, on a 0 ≤ f + ≤ |f | et 0 ≤ f − ≤ |f |. D’après la propriété de la croissance
          de l’intégrale,
                             Z            Z                                 Z               Z
                                  +
                                 f dµ <       |f | dµ < +∞ et                       −
                                                                                f dµ <          |f | dµ < +∞.

          La fonction f est donc µ-intégrable.


           Z        Z         Z                 Z           Z        Z          Z
     2.      f dµ =   f + dµ − f − dµ . Comme      f + dµ − f − dµ ≤   f + dµ +   f − dµ et
              Z       Z         Z             Z           Z
          que f + dµ + f − dµ = |f | dµ alors    f dµ ≤ |f | dµ.
~~~

## Page 48

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                                             48




4.2       Propriétés de l’intégrale de fonctions réelles

      Corollaire 4.

      Soient f ∈ L(Ω, T ) et g ∈ L1 (Ω, T , µ). Si | f |≤| g | µ-p.p alors
                                                                 Z                    Z
                                f ∈ L1 (Ω, T , µ) et                  | f | dµ ≤          | g | dµ.




Démonstration . Par hypothèse, il existe N ∈ T , N est µ-négligeable tel que ∀x ∈ Ω\N ,

                                                       |f (x)| ≤ |g(x)| .

D’après les propriétés de l’intégrale de fonctions mesurables et positives,
                                  Z                  Z                     Z
                                       |f | dµ =             |f | dµ =             1Ω\N |f | dµ.                        (4.1)
                                   Ω                   Ω\N                     Ω


Par la croissance de l’intégrale de fonctions mesurables et positives,
                                        Z                             Z
                                                1Ω\N |f | dµ ≤             1Ω\N |g| dµ                                  (4.2)
                                          Ω                            Ω

et comme                                      Z                            Z
                                                     1Ω\N |g| dµ =             |g| dµ
                                                 Ω                         Ω
                                                  Z            Z
alors les relations (4.1) et (4.2) impliquent que    |f | dµ ≤    |g| dµ.
                 Z                   Z             Ω            Ω

Si g ∈ L1 alors |g| dµ < +∞ ⇒ |f | dµ < +∞. On en déduit que

                                                           Z                   Z
                                        f ∈ L1 et                |f | dµ ≤          |g| dµ.




     Notation.
                                                             Z                 Z
      Pour f ∈ L (Ω, T , µ) et A ∈ T , on note
                   1
                                                                     f dµ =         1A f dµ car d’après le corollaire (4), si
                                                               A
      f ∈ L (Ω, T , µ) alors 1A f ∈ L (Ω, T , µ).
            1                               1
~~~

## Page 49

~~~text
49                                                                                      4.2. Propriétés de l’intégrale de fonctions réelles



       Théorème 2.

          1. Soient f et g deux fonctions de L1 (Ω, T , µ) et α ∈ R, alors
                  Z              Z
              (a)    (αf ) dµ = α f dµ ;
                  Z               Z        Z
              (b)    (f + g) dµ = f dµ + gdµ ;
                            Z        Z
              (c) f ≤ g ⇒ f dµ ≤ gdµ.

          2. L1 (Ω, T , µ) est un espace vectoriel réel.



Démonstration .
                                            Z                Z              Z
     1. Si f est µ-intégrable alors                 f dµ =       f + dµ −           f − dµ. Comme
                                             Ω               Ω                  Ω


                                  (−f ) = (−f )+ − (−f )− , (−f )+ = f − et (−f )− = f +

        alors
          Z              Z                   Z                        Z                         Z                          Z
                f dµ =        (−f )− dµ −           (−f )+ dµ = −               (−f )+ dµ −            (−f )− dµ       =−        (−f )dµ.
           Ω              Ω                     Ω                           Ω                      Ω                         Ω


         (a) On distingue le cas où α ≥ 0 et le cas α ≤ 0 puis on applique les propriétés de l’intégrale
                de fonctions mesurables et positives.
        (b) On pose (f + g) = (f + g)+ − (f + g)− = (f )+ + (g)+ − (f )− − g − .
                Z                   Z                   Z                        Z              Z        Z          Z       
                                                +                    −                     +        +           −        −
                     (f +g)dµ =          (f +g) dµ−          (f +g) dµ =                (f ) dµ+ (g) dµ−    (f ) dµ + (g) dµ
                 Ω                   Ω                   Ω                          Ω                  Ω                 Ω              Ω


                La commutativité nous permet d’écrire
                         Z                       Z                  Z            Z             Z     
                                 (f + g)dµ =         (f )+ dµ −          (f )− dµ +    (g)+ dµ − (g)− dµ .
                             Ω
                                                 | Ω        Z {z
                                                                       Ω
                                                                                 } | Ω       Z {z
                                                                                                   Ω
                                                                                                        }
                                                             =       f dµ                                  =       gdµ
                                                                 Ω                                             Ω


         (c) Comme g = (g − f ) +f , on applique la propriété précédente (linéarité) et on obtient
                          | {z }
             Z        Z     ≥0         Z
                gdµ =    (g − f ) dµ +    f dµ. Le résultat est immédiat.
              Ω
                      | Ω {z       }    Ω
                                     ≥0

     2. Il est aisé de montrer que L1 (Ω, T , µ) est un sous-espace vectoriel de l’espace vectoriel
        L(T , B(R)) pour en déduire que L1 (Ω, T , µ) est espace vectoriel réel.
~~~

## Page 50

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                   50



      Corollaire 5.

     Si f ∈ L1 et si N ∈ T est µ-négligeable alors
                                    Z                     Z              Z
                                            f dµ = 0 et         f dµ =       f dµ.
                                     N                    Ω\N            Ω




      Théorème 3 (Théorème de la convergence dominée).

     Soient (fn )n∈N une suite de fonctions de L(Ω, T ) et g ∈ L1 (Ω, T , µ). On suppose que

          • (fn )n∈N converge vers f µ-p.p

          • Pour tout n ∈ N, |fn | ≤ g.

     Alors                                   
                                              f ∈ L1 (Ω, T , µ)
                                             
                                             
                                             
                                                    Z           Z
                                             
                                              lim
                                                       fn dµ = f dµ
                                                n→+∞




      Théorème 4.

     Soit f ∈ L(Ω, T ). Il existe une suite (φn )n∈N dans E(Ω, T ) qui converge simplement vers
     f sur Ω. Si de plus, f est bornée, alors (φn )n∈N converge uniformément vers f sur Ω.




Démonstration . f = f + − f − et d’après le théorème 1 du chapitre 6,

    • il existe une suite ψn ∈ E + (Ω, T ) avec ψn ↗ f + ,

    • il existe une suite φn ∈ E + (Ω, T ) avec φn ↗ f − .

Posons Φn = ψn − φn Φn ∈ E(Ω, T ) et ∀x ∈ Ω

                                     lim Φn (x) = f + (x) − f − (x) = f (x).
                                        n


Si f est bornée, f + et f − sont bornées donc

    • ψn converge uniformément vers f + ;

    • φn converge uniformément vers f − ;

donc Φn converge uniformément vers f + − f − = f .
~~~

## Page 51

~~~text
51                                                                       4.3. Mesures à densité - Théorème de Radon-Nikodym




4.3       Mesures à densité - Théorème de Radon-Nikodym
   L’objectif est de construire des mesures à partir de mesures connues ou de "transporter" une
mesure d’un espace à un autre. En particulier sur R, B (R) , nous n’avons construit que la mesure
                                                          

de Lebesgue λ.
En théorie de l’intégration, le théorème de Radon-Nykodym est un théorème très important qui
aura des répercussions du côté des probabilités notamment en probabilité conditionnelle. Ce théo-
rème aura sa place importante en analyse fonctionnelle par rapport à la dualité des espaces Lp .
C’est un théorème de décomposition. Étant données deux mesures λ et µ, on va essayer de relier
l’une à l’autre par la décomposition :
                                                         λ = λa + λs .

     • La mesure λa est une mesure absolument continue par rapport à µ, autrement dit si la mesure
       d’un ensemble mesurable par µ est nulle alors la mesure de cet ensemble par λa est nulle.
     • La mesure λs est une mesure qu’on appellera mesure étrangère, autrement dit λs charge un
       ensemble qui est disjoint de l’ensemble chargé par µ ce qui veut encore dire que dès qu’un
       ensemble est mesuré par µ alors il est de mesure nulle par λs .


4.3.1      Mesure définie par une densité

       Proposition 10.

       Si f est une fonction positive mesurable, la fonction d’ensemble positive ν : T → R+
       définie pour tout A ∈ T par
                                                         Z              Z
                                        ν(A) =                f dµ =         1A f dµ.
                                                          A              Ω


       définit une nouvelle mesure sur (Ω, T ). La fonction f s’appelle la densité de ν par rapport
                                                                                 dν
       à µ, et la mesure ν est aussi notée ν = f • µ. On note également f =         .
                                                                                 dµ


Démonstration . ν est une fonction d’ensembles positive.
           Z      Z
  1. ν(∅) = f dµ = 1A f dµ = 0.
                ∅         ∅


     2. Soit An n∈N une famille d’ensembles mesurables et disjoints deux à deux.
                

                                  [                Z                          Z X              
                              ν         An       =           1S     An f dµ =                 1An f dµ.              (4.3)
                                  n∈N                Ω        n∈N               Ω       n∈N


       Puisque la fonction 1An f est mesurable et positive alors d’après le théorème d’intégration
~~~

## Page 52

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                                          52



      d’une série de fonctions mesurables positives, on peut écrire
                                      Z X                      XZ         
                                                      1An f dµ =     1An f dµ .                                       (4.4)
                                          Ω   n∈N                        n∈N         Ω


      Des égalités (4.3) et (4.4), on déduit


                                                                           X
                                                          S                            
                                                  ν             An       =         ν An .
                                                          n∈N                n∈N




ν définit donc bien une mesure sur (Ω, T ).


Remarque 3.
                                                          Z                  Z
   1. Si f1 = f2 µ−p.p alors ∀A ∈ T ,                          f1 dµ =             f2 dµ ainsi ν est définie par une classe
                                                           A                  A
      d’équivalence de densités, égales µ−p.p.


   2. Si f est µ-intégrable,
                          Z on peut de cette façon engendrer une probabilité sur Ω, A en écrivant :
                                                                                     

                                   f dµ
      ∀A ∈ A, P (A) = ZA                  .
                                   f dµ
                               Ω



   Exemple 1.

       1. La mesure sur R de densité g(x) = θe−θx 1[0;+∞[ (x) s’appelle la loi de probabilité
          exponentielle de paramètre θ : c’est une mesure de probabilité (une mesure de masse
                                   Z +∞
          totale égale à 1 puisque      θe−θx dx = 1). Plus généralement, toute mesure sur R de
                              Z +∞  0

          densité g vérifiant      g(x)dx = 1 est une mesure de probabilité.
                                   −∞

       2. On considère des mesures définies par des densités par rapport à la mesure de Lebesgue
          sur R, B (R) , comme :
                       


                                                                                                  1
                               La densité de Cauchy :                            f (x)   =               ,
                                                                                             π (1 + x2 )

                                                                                              1  x2
                                   La densité de Gauss               :           f (x)   =   √ e− 2 ,
                                                                                              2π

                            La densité exponentielle :                           f (x)   =   λe−λx 1R+ (x) .
~~~

## Page 53

~~~text
53                                                                        4.3. Mesures à densité - Théorème de Radon-Nikodym



       Définition 3.

       Soient µ et ν deux mesures sur l’espace mesurable (Ω, T ). On dit que :

          1. ν est absolument continue par rapport à µ et on note ν ≪ µ si :

                                             ∀A ∈ T , µ(A) = 0 ⇒ ν(A) = 0.


          2. ν est étrangère à µ et on note ν⊥ µ s’il existe A ∈ T tel que µ (A) = 0 et ν (Ac ) = 0.


       Théorème 5.

       Soit f : (Ω, T ) → R, B (R) . La mesure ν de densité f par rapport à la mesure µ est
                                  

       absolument continue par rapport à µ.


Démonstration . Soit A ∈ T tel que µ (A) = 0. D’après les propriétés de l’intégrale de fonctions
positives,                                             Z
                                                            f dµ = 0
                                                        A

Ainsi ν (A) = 0.
       Théorème 6.

       Soient f : (Ω, T ) → R, B (R)   une fonction mesurable et positive et ν une mesure de
                                             

       densité f par rapport à µ. Soit g : (Ω, T ) → R, B (R) une fonction mesurable ; on a
                                                             

       alors la propriété suivante :
                                                   Z             Z
                                                       gdν =          gf dµ.
                                                   Ω              Ω


                       g est ν-intégrable si et seulement si gf est µ-intégrable.



Démonstration . g et f g sont mesurables donc leur intégrales existent. On distingue 4 cas :

     1. Si g = 1A , A ∈ T ,
                          Z            Z                          Z                Z               Z
                               gdν =        1A dν = ν(A) =                f dµ =       1A f dµ =       f gdµ.
                           Ω            Ω                             A            Ω               Ω

               Z                                        Z
        Donc       gdν < +∞ si et seulement si                  f gdµ < +∞.
               Ω                                            Ω
                                X
     2. Si g ∈ E + alors g =        ai 1Ai , Ai ∈ T .

                   Z            X                  X        Z             Z X               Z
                        gdν =       ai ν (Ai ) =       ai             f dµ =    ai 1Ai f dµ =   f gdµ.
                    Ω                                            Ai                Ω                       Ω
~~~

## Page 54

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                                                              54

              Z                                                 Z
      Donc         gdν < +∞ si et seulement si                          f gdµ < +∞.
               Ω                                                    Ω

   3. Si g ∈ M+ alors g est une limite simple d’une suite croissante de fonctions mesurables et
      positives. g = lim ↑ gn , gn ∈ E + .
                            n→+∞

      Z             Z                                           Z                            Z                    Z                          Z
            gdν =           lim ↑ gn dν = lim ↑    gn dν = lim ↑                                     f gn dµ =             lim ↑ f gn dν =            f gdµ.
        Ω           Ω n→+∞               n→+∞             n→+∞                                                            n→+∞
                                         |    {z Ω     }                                      Ω
                                                                                                                  |Ω          {z       }          Ω
                                                        Beppo-Levi                                                        Beppo-Levi

              Z                                                 Z
      Donc         gdν < +∞ si et seulement si                          f gdµ < +∞.
               Ω                                                    Ω

   4. Si g = g + − g − .
                                             Z                                           Z
                                            
                                            
                                               g + dν           < + ∞                   
                                                                                         
                                                                                            f g + dµ            <        + ∞
                                             Ω
                                                                                         Ω
                                                                                         
      g est ν−intégrable ⇔                                                           ⇔                                             ⇔ f g est µ−intégrable
                                            
                                             Z                                          
                                                                                          Z
                                                g − dν           < + ∞                       f g − dµ            < + ∞
                                            
                                                                                        
                                                                                         
                                                                                        
                                                    Ω                                         Ω




      et                Z               Z                  Z              Z                  Z                    Z
                                gdν =           g + dν −       g − dν =         f g + dµ −           f g − dµ =           f gdµ.
                        Ω               Ω                  Ω                Ω                    Ω                    Ω



4.4        Espaces Lp et Lp

      Définition 1.

      Soit p ∈ [1, +∞[, on note Lp (X, T , µ) (en abrégé Lp ), l’ensemble des fonctions f ∈
                                  p
      L (X, T ) tel que |f | ∈ L1 (X, T , µ) :
                                                                                     Z
                                                                                                 p
                            f ∈ Lp (X, T , µ) ⇔ f ∈ L (X, T ) et                             |f | dµ < +∞.
                                                                                         X


      On dit que f ∈ Lp (X, T , µ) est de puissance pième -intégrable.



Remarque 4.
                            p                                                    p
   1. La fonction |f | désigne la fonction x 7−→ (|f (x)|) (ce n’est pas la composée.)

   2. Pour p = 1, on obtient les fonctions µ-intégrables.
      Pour p = 2, on obtient les fonctions de carré intégrables.
                                            p
   3. Si f ∈ L (X, T ) alors |f | ∈ L (X, T ).
~~~

## Page 55

~~~text
55                                                                                                       4.4. Espaces Lp et Lp



Propriété 4.4.1. Lp (X, T , µ) est un espace vectoriel.

Démonstration . On montre que Lp (X, T , µ) est un sous-espace vectoriel de L (X, T ).

     • Lp (X, T , µ) ⊂ L (X, T ) (par définition) ;

     • 0 ∈ Lp donc Lp ̸= ∅ ;

     • soient f ∈ Lp et α ∈ R donc αf ∈ L (X, T ) et
                         Z                Z                                   Z
                                   p                     p                              p
                             |αf | dµ =       | α |p |f | dµ =| α |p            |f | dµ              < +∞
                                                                              | {z }
                                                                             <+∞ car f ∈Lp


       donc αf ∈ Lp ;

     • Soit (f, g) ∈ Lp × Lp alors f + g ∈ L (X, T ).
       ∀x ∈ X, |f (x) + g(x)| ≤ 2 max (|f (x)| , |g(x)|)
                                                                                   p
                                                    p
                               ⇒ |f (x) + g(x)|         ≤ 2p max (|f (x)| , |g(x)|)

                                   Z                             Z                  
                                                                             p     p
                               ⇒       |f + g| dµ       ≤ 2p         sup |f | , |g| dµ

                                                                 Z                     
                                                                         p          p
                                                        ≤ 2p           |f | + |g|           dµ

                                                                 Z                 Z                
                                                             p           p                       p
                                                        ≤2             |f | dµ +            |g| dµ



Notation


                                   N = {f ∈ L(X, T ), f = 0 µ -p.p} .



       Proposition 11.

      N est un espace vectoriel réel et pour tout p ∈ [1, +∞[, N ⊂ Lp .



Remarque 5. Pour f ∈ L(X, T ) et g ∈ L(X, T ), f − g ∈ N ⇔ f = g µ p.p.
       Définition 2.

      Lp (X, T, µ) (ou en abrégé Lp ) est l’espace vectoriel quotient de Lp (X, T, µ) par N . C’est
      à dire l’ensemble des classes d’équivalence d’éléments de Lp par la relation f = g µ-p.p.
~~~

## Page 56

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                              56



Remarque 6.               Bien que ses éléments soient des classes d’équivalence des fonctions. On a
l’habitude de dire qu’un élément de Lp (X, T, µ) est une fonction, bien que strictement il s’agisse
d’une classe de fonctions.
                                                                       
                                                    
                                                     ∃g ∈ L (X, T , µ) 
                                                                        
                                                    
                                                                       
                                                                        
                                                    
                                                                       
                                                                        
                                                    
                                                                       
                                                                        
                                                                       
                                      p
                                 f ∈ L (X, T , µ) ⇔   f = g µp.p
                                                    
                                                                       
                                                                        
                                                    
                                                                       
                                                                        
                                                    
                                                     Z                 
                                                                        
                                                           p           
                                                    
                                                        |g| dµ < +∞.  
                                                           X




   Exemple 11.

       1. On considère l’espace probabilisé (X, P (X) , P). La loi binomiale B(n, p), p ∈ ]0, 1[, mo-
          délise le nombre de succès dans une répétition indépendante de n expériences aléatoires
          identiques où la probabilité de succès de chaque expérience est égale à p.

          P la mesure de probabilité telle que si k ∈ {0, 1, . . . , n}

                              P {k} = P (nombre de sucès = k) = Cnk pk (1 − p)n−k .
                                   


                 • Si X = {0, 1, . . . , n} alors le plus gros ensemble P-négligeable est l’ensemble vide.

                 • Si X = N et si P (k) = 0 pour k ≥ n alors N = {n + 1, . . .} est le plus gros
                   ensemble P-négligeable.

       2. Il n’existe pas toujours de plus gros ensemble µ-négligeable. Pour la mesure de Lebesgue
          sur R, il n’en existe pas.

          En effet, supposons par l’absurde que N est le plus gros λ-négligeable. On peut dire
          dans ce cas que N est mesurable sinon il est contenu strictement dans un mesurable de
          mesure égale à 0 ce qui contredit l’hypothèse que N est le plus gros négligeable.
                                                                                            ′
          On sait que λ (R) = +∞ donc N ⊊ R. Il existe x ∈ R avec x ∈
                                                                    / N . Soit N = N ∪ {x}.
             ′                    ′                                 ′                           ′
          N ∈ B (R) et λ(N ) = λ(N ) + λ ({x}) = 0 donc N est λ-négligeable et N ⊃ N .
~~~

## Page 57

~~~text
57                                                                                   4.5. Normes sur Lp (p ∈ [1, +∞[)




4.5       Normes sur Lp (p ∈ [1, +∞[)

Notations

     1. Pour f ∈ L(X, T ) et p ∈ [1, +∞[, on note

                                                   Z                     p1
                                                              p
                                       Np (f ) =        |f (x)| µ (dx)          .



     2. Pour fe ∈ Lp et p ∈ [1, +∞[, on note

                                               ∥fe∥p = Np (f ).


Remarque 7. Si f ∈ L(X, T ) alors


                                       f ∈ Lp ⇔ Np (f ) < +∞.


       Définition 3.

                                                                                    1 1
       Soient p et q dans [1, +∞[, on dit que p et q sont conjugués si                + = 1. On dit alors
                                                                                    p  q
       que q est l’exposant conjugué de p (il est unique).




Remarque 8. On convient que 1 et +∞ sont conjugués.


       Lemme 2 (Inégalité de Young).

       Soient a et b deux réels strictement positifs, p et q conjugués dans [1, +∞[. Alors ab ≤
       1 p  1 q
       pa + qb .




       Lemme 3 (Inégalité de Hölder).

       Soient p et q conjugués dans [1, +∞[. Soient f ∈ Lp et g ∈ Lq alors

                            N1 (f × g) ≤ Np (f ) × Nq (g) et f × g ∈ L1 .




Remarque 9. Si p = q = 2, on obtient l’inégalité de Cauchy-Schwartz.
~~~

## Page 58

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                       58



      Lemme 4 (Inégalité de Minkowski).

      Soient p dans [1, +∞[, f ∈ Lp et g ∈ Lp alors

                                          Np (f + g) ≤ Np (f ) + Np (g).




Théorème 4.5.1. Pour p ∈ [1, +∞[, ∥.∥p est une norme sur Lp .

      Théorème 5 (Fischer-Riesz).

      Pour p ∈ [1, +∞[, (Lp , ∥.∥p ) est un espace de Banach.




4.6       Espaces L∞
      Définition 4.

      Une fonction f de L(X, T ) est dite essentiellement bornée s’il existe r ≥ 0 tel que |f | ≤ r
      µ-p.p.
      On note L∞ (X, T, µ) l’ensemble des fonctions essentiellement bornées de L(X, T ).



      Proposition 12.

         1. L∞ est un espace vectoriel réel.

         2. N ⊂ L∞ .



      Définition 5.

         1. L∞ (X, T, µ) est l’espace vectoriel quotient de L∞ (X, T, µ) par N .

         2. Si f ∈ L(X, T ),
                                       N∞ (f ) = inf {r ≥ 0 / |f | ≤ r µ-p.p}

         3. Si fe ∈ L∞ alors ∥fe∥∞ = N∞ (f ).




Conséquence
    Si f ∈ L(X, T ),
~~~

## Page 59

~~~text
59                                                                                                     4.6. Espaces L∞



                                             f ∈ L∞ (X, T ) ⇔ N∞ (f ) < +∞.


       Théorème 6.

         1. ∥.∥∞ est une norme sur L∞ .

         2. (L∞ , ∥.∥∞ ) est complet.

         3. Inégalité de Hölder : pour 1 et +∞ : si f ∈ L1 et g ∈ L∞ alors f g est µ-intégrable
            et

                                                     N1 (f × g) ≤ N1 (f ) × N∞ (g).




       Proposition 13 (Relations entre les Lp ).

      Si µ(X) < +∞ et 1 ≤ p1 ≤ p2 ≤ +∞ alors

                                                     L∞ ⊂ Lp2 ⊂ Lp1 ⊂ L1 .




Démonstration .

     • L∞ ⊂ Lp pour p fini, en effet,

                                                 f ∈ L∞ ⇒ |f | ≤ N∞ (f ) µ − p.p
                                                              Z
                                             p                                        p
                 ⇒ |f |p ≤ (N∞ (f ))             µ − p.p ⇒         |f |p dµ ≤ (N∞ (f )) µ(X) < +∞ µ − p.p

       Donc f ∈ Lp .


     • Si p1 ≤ p2 . Soit f ∈ Lp2 . On distingue deux cas :


          – |f | ≤ 1 donc
                                                 Z                 Z
                              |f |p1 ≤ 1 ⇒           |f |p1 dµ ≤     1dµ < ∞ ⇒ f ∈ Lp1 ⇒ Lp2 ⊂ Lp1 .
                                                                   | {z }
                                                                   =µ(X)



          – |f | ≥ 1 donc
                                                 Z                 Z
                              p1        p2              p1
                       |f |        ≤ |f |    ⇒       |f | dµ ≤         |f |p2 dµ < ∞ ⇒ f ∈ Lp1 ⇒ Lp2 ⊂ Lp1 .
~~~

## Page 60

~~~text
Chapitre 4. Intégration de fonctions mesurables                                                        60



4.6.1      Théorème de Radon Nikodym
    Sur un espace probabilisé (Ω, A, P), on considère B une sous-tribu de A. On veut définir, à
partir d’une variable aléatoire réelle X ∈ L1 Ω, A, P , une autre variable aléatoire réelle qui va
                                                     

"oublier" tout se qui se passe en dehors de B.
    L’espérance conditionnelle sert à modéliser la réponse à la question suivante : si X est une
variable aléatoire liée à une certaine expérience, que sait-on d’elle si l’on n’a pas toute l’information
(donnée par la tribu A) des événements, mais seulement une information partielle (donnée par une
sous-tribu B).
    En pratique, il est fréquent de travailler sur R, B (R) , Rn , B n (R) et N, P (N) munis des
                                                                                    

lois de probabilités qui seront dominées par λ, mesure de Lebesgue sur R, λn , mesure de Lebesgue
sur Rn et µ, mesure discrète de comptage sur N. Ces lois admettront donc des densités par rapport
à λ, λn et µ.
    Les théorèmes suivants énoncent des conditions générales d’existence de densités.

      Définition 4.

     Soit (Ω, T ) un espace mesurable, µ : T → [0, +∞] une mesure positive, on dit que µ est
     σ-finie, si

         1. il existe une suite (An )n∈N , An ∈ T pour tout entier n, telle que
                                                                                  S
                                                                                        An = Ω,
                                                                                  n∈N

         2. µ(An ) < +∞, pour tout n ∈ N.



     Mise en garde.
         • Une mesure σ-finie peut être de masse totale infinie, par exemple la mesure de Lebesgue.

         • La mesure de Lebesgue sur R et la mesure de comptage sur N sont σ-finies.


      Théorème 7 (Théorème de Radon-Nikodym, Lebesgue-Nikodym).

     Soient µ et ν deux mesures σ−finies sur (Ω, T ). Il existe alors un unique couple de mesures
     σ−finies (µa , µs ) sur (Ω, T ) telles que

         1. µ = µa + µs ,

         2. µa ≪ ν et µs ⊥ ν.

     De plus, il existe une fonction mesurable f : Ω → R+ telle que
                                                              Z
                                          ∀A ∈ T , µa (A) =       f dν
                                                              A

     et la fonction f est unique à un ensemble de ν−mesure nulle près.
~~~

## Page 61

~~~text
61                                                                                    4.6. Espaces L∞



4.6.2      Mesure image
       Définition 5.
                                          ′                                         ′ 
      Soient (Ω, T , µ) un espace mesuré, Ω , A un espace mesurable, et T : (Ω, T ) → Ω , A
      une application mesurable. On appelle mesure image de µ par T, la mesure µT définie
          ′ 
      sur Ω , A par :

                           ∀B ∈ A, µT (B) = µ T−1 (B) = µ ◦ T−1 (B) .
                                                     




     Exemple 2. Soient (Ω, A, P) un espace probabilisé et R, B (R) l’espace mesurable des
                                                                         

     boréliens. Soit X une variable aléatoire de (Ω, A, P) dans R, B (R) . On définira l’image par
                                                                        

     X de P par :
                                                                      
                                     − ∞, b = P X−1 − ∞, b    = P X ∈ − ∞, b .
                                                                       
                ∀b ∈ R, PX


     On retrouve ici la notion de la fonction de répartition de X.

       Théorème 8 ( Théorème de transfert).
                                          ′                                         ′ 
      Soient (Ω, T , µ) un espace mesuré, Ω , A un espace mesurable, et T : (Ω, T ) → Ω , A
                                                                                  ′ 
      une application mesurable. µT la mesure image de µ par T définie sur Ω , A . Soit
          ′ 
      f : Ω , A → R, B (R) une fonction mesurable. Alors
                                


        f est µT −intégrable si et seulement si l’application mesurable f ◦ T est µ−intégrable

      et on a                             Z               Z
                                                f dµT =       f ◦ Tdµ.
                                           Ω′             Ω
~~~

## Page 62

~~~text
5 | Produit de mesures
     Soient A et B deux ensembles mesurables respectivement dans deux espaces mesurés
(Ω1 , T1 , µ) et (Ω2 , T2 , ν). On construit intuitivement la mesure de A × B égale à µ(A) × ν(B). La
théorie de la mesure nous donne ce résultat. Le théorème de Fubini nous permettra d’intégrer
par rapport à une mesure produit et facilitera le calcul des intégrales multiples.


Sommaire
          5.1      Produit de tribus     . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    62
          5.2      Mesure produit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       64
          5.3      Théorème de Fubini . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         65


5.1      Produit de tribus
      Définition 8.
      On appelle pavé mesurable tout ensemble A1 × A2 avec Ai ∈ Ti , i ∈ {1, 2}.



Remarque 10. Le complémentaire d’un pavé peut s’écrire comme une union finie de pavés :
                                                            !                         !                      !
 (Ω1 × Ω2 ) \ (A1 × A2 ) =        (Ω1 \ A1 ) × (Ω2 \ A2 )       ∪   (Ω1 \ A1 ) × Ω2       ∪   Ω1 × (Ω2 \ A2 ) .


      Propriété 14.
      Une union finie de pavés mesurables est égale à une union finie de pavés mesurables
      disjoints.


      Définition 9.
      On appelle tribu produit, T1 ⊗ T2 , de T1 par T2 la tribu de parties de Ω1 × Ω2 engendrée
                                                                                           
      par les pavés mesurables de Ω1 × Ω2 : T1 ⊗ T2 := σ {A1 × A2 ; A1 ∈ T1 , A2 ∈ T2 }


Remarque 11.

  1. La famille des pavés mesurables n’est pas elle même une tribu en général. Elle n’est stable ni
      par réunion finie ni par complémentaire.


                                                      62
~~~

## Page 63

~~~text
63                                                                               5.1. Produit de tribus



     2. Le produit de deux tribus n’est pas commutatif. La tribu T1 ⊗ T2 n’est pas en général égale
       à T2 ⊗ T1 , tout simplement parce que le produit cartésien n’est pas commutatif : Ω1 × Ω2 ̸=
       Ω2 × Ω1 . Par conséquent le produit de deux mesures que nous allons définir sur T1 ⊗ T2 ne
       sera pas non plus commutatitif.

Conséquence : B R2 = B (R) ⊗ B (R). Par récurrence, on peut démontrer à partir du résultat
                  

précédent que pour tout n ∈ N∗ B (Rn ) = B (R) ⊗ . . . ⊗ B (R) .
                                         |       {z          }
                                                          n fois

       Propriété 15.

          1. Tout ouvert de R2 est réunion dénombrable de pavés ouverts.

          2. B R2 = B (R) ⊗ B (R).
                 




       Proposition 1.

       Soit (Y, F) un espace mesurable. On considère pour i = 1, 2 la projection canonique de
       Ω1 × Ω2 sur Ωi ,
                                          πi   :   Ω1 × Ω2         → Ωi
                                                   (x1 , x2 )      7→   xi

       La fonction g : Y → Ω1 × Ω2 est (F, T1 ⊗ T2 )-mesurable si et seulement si ∀i ∈ {1, 2},
       πi ◦ g est (F, Ti )-mesurable.



       Définition 10.
       Si A ∈ T1 ⊗ T2 et si x1 ∈ Ω1 , on appelle coupe de A par rapport à x1 , notée Ax1 ,
       l’ensemble
                                          {x2 ∈ Ω2 , (x1 , x2 ) ∈ A} .

       On a Ax1 = π2 (A ∩ {x1 } × Ω2 ).


       Proposition 2.

       Soient (Ω1 , T1 ), (Ω2 , T2 ) et (Ω3 , T3 ) trois espaces mesurables.

          1. Si f : Ω1 × Ω2 → Ω3 est (T1 ⊗ T2 , T3 )-mesurable, alors

                ↬ ∀x2 ∈ Ω2 , x1 7→ f (x1 , x2 ) est (T1 , T3 ) − mesurable.


                ↬ ∀x1 ∈ Ω1 , x2 7→ f (x1 , x2 ) est (T2 , T3 ) − mesurable.

          2. Si A ∈ T1 ⊗ T2 alors Ax1 ∈ T2 pour tout x1 ∈ Ω1 .
~~~

## Page 64

~~~text
Chapitre 5. Produit de mesures                                                                              64




5.2      Mesure produit
      Définition 11.

      Soit (Ω, T , µ) un espace mesuré, on dit que µ est σ-finie, si

         1. il existe une suite (An )n∈N , An ∈ T pour tout entier n, telle que
                                                                                      S
                                                                                           An = Ω,
                                                                                     n∈N

         2. µ(An ) < +∞, pour tout n ∈ N.


Remarque 12.

   • Une mesure σ-finie peut être de masse totale infinie, par exemple la mesure de Lebesgue.

   • La mesure de Lebesgue sur R et la mesure de comptage sur N sont σ-finies.

      Théorème 7.

      Soient (Ω1 , T1 , µ1 ) et (Ω2 , T2 , µ2 ) deux espaces mesurés et µ1 et µ2 σ-finies alors il existe
      une mesure unique µ sur T1 ⊗ T2 telle que :

                       ∀A1 ∈ T1 , ∀A2 ∈ T2 , µ (A1 × A2 ) = µ1 (A1 ) × µ2 (A2 ) .

         • µ est une mesure σ-finie

         • x1 7→ µ2 (Ax1 ) est T1 -mesurable pour tout A ∈ T1 ⊗ T2
                   Z
         • µ(A) =     µ2 (Ax1 ) dµ1 (x1 ).
                       Ω1

      µ est la mesure produit de µ1 par µ2 et on la note µ1 ⊗ µ2 .


Remarque 13.

   1. Si on a trois espaces mesurés (Ωi , Ti , µi ), i ∈ {1, 2, 3} avec µi σ-finies alors on a l’associativité
      du produit : µ1 ⊗ µ2 ⊗ µ3 = µ1 ⊗ (µ2 ⊗ µ3 ) . Comme on avait (T1 ⊗ T2 ) ⊗ T3 = T1 ⊗ (T2 ⊗ T3 ),
      on peut donc définir la mesure sur T1 ⊗ T2 ⊗ T3 comme l’unique mesure µ sur ce produit de
      tribus telle que

                 µ (A1 × A2 × A3 ) = µ(A1 ) × µ(A2 ) × µ(A3 ) avec          Ai ∈ Ti , i ∈ {1, 2, 3} .

      Idem avec n facteurs (n ∈ N∗ ) (par récurrence).

   2. La mesure de Lebesgue sur R2 est le produit des mesures de Lebesgue sur (R, B(R)). et la
      mesure de Lebesgue sur Rn (n ∈ N∗ ) est le produit des mesures de Lebesgue sur chaque
      facteur.
~~~

## Page 65

~~~text
65                                                                                             5.3. Théorème de Fubini




5.3      Théorème de Fubini




     Dans la suite, on suppose que (Ω1 , T1 , µ1 ) et (Ω2 , T2 , µ2 ) deux espaces mesurés et µ1 et µ2
σ-finies et µ = µ1 ⊗ µ2 . L’intégration d’une fonction numérique définie sur T1 ⊗ T2 par rapport à
la mesure µ est précisée par les deux théorèmes ci-dessous.
Le premier traite le cas d’une fonction positive, connu sous le nom du théorème de Fubini-
Tonelli ; le deuxième traite le cas d’une fonction de signe quelconque, connu sous le nom du
théorème de Fubini.




      Théorème 8 (Théorème de Fubini-Tonelli).

      Si f : Ω1 × Ω2 → [0, +∞] est T1 ⊗ T2 -mesurable, alors les fonctions φ et ψ définies
      respectivement sur Ω1 et Ω2 par
                            Z                                             Z
                φ : x1 7→           f (x1 , x2 ) dµ2 (x2 ) et ψ : x2 7→         f (x1 , x2 ) dµ1 (x1 )
                            Ω2                                             Ω1

                                Z                   Z      Z                          
                                         f dµ =                  f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 )
                                Ω1 ×Ω2                Ω1    Ω2
      sont mesurables. et
                                                    Z      Z                          
                                                =                f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 ) .
                                                      Ω2    Ω1
~~~

## Page 66

~~~text
Chapitre 5. Produit de mesures                                                                                           66



      Théorème 9 (Théorème de Fubini).

     Si f : Ω1 × Ω2 → R est µ-intégrable, alors

        1. Pour presque tout x1 ∈ Ω1 , la fonction x2 7→ f (x1 , x2 ) est intégrable sur Ω2 et la
            fonction φ définie presque partout sur Ω1 par
                                                             Z
                                                φ : x1 7→             f (x1 , x2 ) dµ2 (x2 )
                                                                Ω2


            est µ1 -intégrable sur Ω1 .

        2. Pour presque tout x2 ∈ Ω2 , la fonction x1 7→ f (x1 , x2 ) est intégrable sur Ω1 et la
            fonction ψ définie presque partout sur Ω2 par
                                                             Z
                                                ψ : x2 7→             f (x1 , x2 ) dµ1 (x1 )
                                                                 Ω1


            est µ2 -intégrable sur Ω2 .

        3. Z                          Z     Z                             
                          f dµ =                     f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 )
                 Ω1 ×Ω2                Ω1       Ω2

                                      Z     Z                             
                                 =                   f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 ) .
                                       Ω2       Ω1




Si l’une des trois intégrales suivantes
                                            Z
                                 I1   =                |f |dµ
                                            Ω1 ×Ω2

                                            Z    Z                               
                                 I2   =                    |f (x1 , x2 ) dµ2 (x2 ) |dµ1 (x1 )
                                            Ω1        Ω2

                                            Z    Z                               
                                 I3   =                    |f (x1 , x2 ) dµ1 (x1 ) |dµ2 (x2 )
                                            Ω2        Ω1


est finie alors il en est de même pour les deux autres, f est intégrable et
          Z      Z                                                  Z      Z                           
                          f (x1 , x2 ) dµ2 (x2 ) dµ1 (x1 ) =                        f (x1 , x2 ) dµ1 (x1 ) dµ2 (x2 ) .
            Ω1      Ω2                                                  Ω2     Ω1


Mode d’emploi :

    Pour prouver que f est intégrable sur T1 ⊗ T2 , on applique le théorème de Fubini-Tonelli à |f |
qui affirme que I1 , I2 et I3 sont égales (qu’elles soient finies ou non), puis montrer que I2 ou I3 est
finie. Souvent, l’une d’elles est facile à estimer.
~~~

## Page 67

~~~text
67                                                                                           5.3. Théorème de Fubini



Mise en garde :

     Bien distinguer le cas f mesurable positive où les trois intégrales I1 , I2 et I3 ont toujours un
sens (valeur finie ou infinie) du cas où f est de signe variable pour lequel les intégrales
                             Z    Z                         Z     Z            
                                          f dµ2 dµ1 et                      f dµ1 dµ2
                             Ω1      Ω2                        Ω2      Ω1


peuvent ne pas exister, ou bien peuvent exister avec des valeurs finies ou infinies distinctes ou
égales, sans que f soit intégrable. Autrement dit, si f est en général mesurable mais pas intégrable,
les expressions              Z    Z                         Z     Z           
                                          f dµ2 dµ1 et                      f dµ1 dµ2
                             Ω1      Ω2                        Ω2      Ω1

peuvent exister mais avoir des valeurs différentes.


Fonctions à variables séparées
     Si f1 et f2 sont deux fonctions mesurables positives (ou intégrables), définies respectivement
sur Ω1 et Ω2 . On pose f (x1 , x2 ) = f1 (x1 ) × f2 (x2 ). Alors f est T1 ⊗ T2 -mesurable et
                         Z                             Z               Z             
                                    f d (µ1 × µ2 ) =          f1 dµ1              f2 dµ2 .
                           Ω1 ×Ω2                        Ω1                  Ω2
~~~
