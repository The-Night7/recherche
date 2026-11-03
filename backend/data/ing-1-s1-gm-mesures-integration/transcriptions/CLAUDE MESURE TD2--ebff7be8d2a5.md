# CLAUDE MESURE TD2.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1bQJigXUS4Z4gCsZb0tBS2yqz4fEPxtO1) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                      TD 2 – Introduction à la mesure
                         CY-Tech - Département Mathématiques
                         ère
                        1 année Ingénieurs - Génie Mathématique
                                 Mesure & intégration



  Mesure – Rappel 1.
     Soient T une tribu de parties de Ω et m : T → [0, +∞] une fonction d’ensembles positive.
  m est une mesure positive sur T si et seulement si les conditions suivantes sont vérifiées :
      1. m(∅) = 0 ;
      2. m est σ-additive.


EXERCICE 1
    Soient Ω un ensemble, T une tribu de parties de Ω et m une mesure positive sur T . Montrer
les propriétés suivantes :
    1. (A, B) ∈ T 2 tels que A ⊂ B alors m(A) ≤ m(B).
                                         S       P
    2. An ∈ T pour tout n ∈ N, alors m n∈N An ≤ n∈N m(An ).


  Correction Exercice 1
    1. Croissance de la mesure :
    Soit A ⊂ B avec A, B ∈ T .
    On peut écrire B = A ∪ (B \ A) où A et B \ A sont disjoints.
    Comme T est une tribu, B \ A ∈ T .
    Par σ-additivité (ou additivité finie) :

                                    m(B) = m(A) + m(B \ A)

     Puisque m(B \ A) ≥ 0 (car m est une mesure positive), on obtient :

                                          m(A) ≤ m(B)

     2. Sous-additivité dénombrable (σ-sous-additivité) :
     Soit (An )n∈N une suite d’ensembles de T .
     On construit une suite disjointe (Bn )n∈N telle que :
                                                     n−1
                                                     [
                             B0 = A0 ,   Bn = An \         Ak pour n ≥ 1
                                                     k=0

     Les Bn sont dans T (car T est une tribu), deux à deux disjoints, et vérifient :
                                     [          [
                                         Bn =      An
                                         n∈N       n∈N

     De plus, Bn ⊂ An pour tout n, donc par croissance : m(Bn ) ≤ m(An ).


                                               1
~~~

## Page 2

~~~text
      Par σ-additivité sur les ensembles disjoints :
                                !               !
                         [               [           X          X
                    m        An = m          Bn =      m(Bn ) ≤   m(An )
                              n∈N                   n∈N               n∈N                  n∈N



EXERCICE 2
    Soit (Ω, T ) un espace mesurable. Soient x1 , . . . , xk des éléments distincts de Ω et a1 , . . . , ak
des réels strictement positifs. On note

                                                     µ : T → [0; ∞]
                                                            k
                                                            X
                                                   B 7→           ai δxi (B)
                                                            i=1

où δxi est la mesure de Dirac concentrée en xi . Montrer que µ est une mesure positive sur (Ω, T ).

  Correction Exercice 2
    Pour montrer que µ est une mesure, il faut vérifier les deux propriétés :
    1. µ(∅) = 0 :
                                                   k
                                                   X                    k
                                                                        X
                                      µ(∅) =             ai δxi (∅) =         ai · 0 = 0
                                                   i=1                  i=1

      car δxi (∅) = 0 (aucun point n’appartient à l’ensemble vide).
      2. σ-additivité :
      Soit (Bn )n∈N une suite         Pde T deux à deux disjoints.
                            S d’ensembles
      On doit montrer : µ n∈N Bn = n∈N µ(Bn ).
                                                k
                                         !                      !
                                   [          X           [
                               µ       Bn =        ai δxi    Bn
                                            n∈N               i=1             n∈N
               S                   S
      Or, δxi S n∈N Bn = 1 si xi ∈ n∈N Bn et 0 sinon.
      Si xi ∈ n∈N          ∃!n
                 SBn , alors   P0 tel que xi ∈ Bn0 (car les Bn sont disjoints).
      Donc : δxi   n∈N Bn =      n∈N δxi (Bn ).
      Par conséquent :
                             k
                       !
                 [         X      X
             µ     Bn =        ai     δxi (Bn )
                   n∈N              i=1     n∈N
                                     k
                                    XX
                               =              ai δxi (Bn ) (par Fubini pour les séries positives)
                                    n∈N i=1
                                    X
                               =          µ(Bn )
                                    n∈N

      Ainsi, µ est bien une mesure positive sur (Ω, T ).


EXERCICE 3
                          n, n + 21n . Calculer λ(A).
               S                   
    Soit A =       n≥0


                                                               2
~~~

## Page 3

~~~text
  Correction Exercice 3
      Les intervalles In = n, n + 21n ne sont pas nécessairement disjoints, mais on peut ma-
                                     

  jorer :
      Par σ-sous-additivité de la mesure de Lebesgue :
                                          
                                      [        X            X 1
                          λ(A) = λ     In  ≤     λ(In ) =       =2
                                                               2n
                                          n≥0             n≥0                    n≥0


     En fait, pour n ≥ 1, on a n + 21n < n + 1 car 21n < 1, donc les intervalles sont disjoints
  pour n ≥ 1.
     Vérifions si I0 = [0, 1] et I1 = [1, 1.5] se chevauchent : ils se touchent en 1 mais ne se
  chevauchent pas strictement.
     En termes de mesure de Lebesgue, les points isolés sont de mesure nulle, donc :
                                         X                X 1              1
                               λ(A) =          λ(In ) =              =          =2
                                         n≥0              n≥0
                                                                2n       1 − 12

     Réponse : λ(A) = 2


EXERCICE 4
                                                        S               
   1. Soit x0 , x1 , x2 , . . . des réels. Calculer λ        n≥0 {xn }       .
   2. En déduire λ(Q).


  Correction Exercice
                   S 4          
    1. Calcul de λ    n≥0 {x n }   :
    Chaque singleton {xn } est un borélien et λ({xn }) = 0 (un point a une mesure nulle).
    Par σ-sous-additivité :
                                    
                               [          X              X
                          λ  {xn } ≤        λ({xn }) =     0=0
                                   n≥0             n≥0                       n≥0

                                                       S                
     Comme une mesure est toujours positive, on a : λ       n≥0    {x n }  = 0.
     2. Calcul de λ(Q) :
     Q est dénombrable, donc on peut écrire Q = {q0 , q1 , q2 , . . .}.
     D’après la question 1 :                       
                                            [
                                λ(Q) = λ  {qn } = 0
                                                        n≥0

     Réponse : λ(Q) = 0


EXERCICE 5
   Montrer que tout ensemble fini ou dénombrable A est borélien, de mesure de Lebesgue nulle
λ(A) = 0.




                                                        3
~~~

## Page 4

~~~text
  Correction Exercice 5
    Cas 1 : A est fini
    Si A = {x1 , . . . , xn } est fini, alors :
    — ChaqueS singleton {xi } est un fermé de R, donc un borélien.
    — A = ni=1 {xi } est une union P        finie de boréliens,
                                                             Pdonc    est borélien.
                                                n               n
    — Par additivité finie : λ(A) = i=1 λ({xi }) = i=1 0 = 0.
    Cas 2 : A est dénombrable
    Si A est dénombrable, on peut écrire A = {x0 , x1 , x2 , . . .}.
    — Chaque S singleton {xn } est borélien.
    — A = n≥0 {xn } est une union dénombrable de boréliens, donc est borélien (car la
       tribu des boréliens est stable par union dénombrable).
    — Par σ-sous-additivité :
                                                    
                                             [             X               X
                               λ(A) = λ  {xn } ≤             λ({xn }) =     0=0
                                      n≥0           n≥0            n≥0

      Donc λ(A) = 0.
      Conclusion : Tout ensemble fini ou dénombrable est borélien et de mesure de Lebesgue
  nulle.



  ensemble négligeable – Rappel 2.
      1. On dit qu’un ensemble N ∈ T est m-négligeable si m(N ) = 0.
      2. On dit qu’une partie N de Ω est m-négligeable s’il existe A ∈ T tel que N ⊂ A et
         m(A) = 0.


EXERCICE 6
   Soit (Ω, T , m) un espace mesuré et soit N l’ensemble des parties m-négligeables. On considère
                               Te = {A ∪ N ; A ∈ T et N ∈ N }.
Pour tout A ∈ T et pour tout N ∈ N , on pose m(Ae    ∪ N ) = m(A). Montrer que
   1. Te est une tribu sur Ω contenant T .
   2. me définit une mesure positive sur Te qui coïncide avec m sur T .

  Correction Exercice 6
    1. Te est une tribu contenant T :
    a) Te contient T :
    Pour tout A ∈ T , on peut écrire A = A ∪ ∅ avec ∅ ∈ N (car m(∅) = 0).
    Donc A ∈ Te .
    b) Ω ∈ Te :
    Ω ∈ T (car T est une tribu), donc Ω ∈ Te d’après (a).
    c) Stabilité par complémentaire :
    Soit E = A ∪ N ∈ Te avec A ∈ T et N ∈ N .
    Il existe B ∈ T tel que N ⊂ B et m(B) = 0.
    On a : E c = (A ∪ N )c = Ac ∩ N c .
    Or Ac \ B ⊂ E c ⊂ Ac , donc E c = (Ac \ B) ∪ (E c ∩ B).
    Posons A′ = Ac \ B ∈ T et N ′ = E c \ A′ = E c ∩ B.


                                               4
~~~

## Page 5

~~~text
    Alors N ′ ⊂ B donc N ′ ∈ N .
    Ainsi E c = A′ ∪ N ′ ∈ Te .
    d) Stabilité par union dénombrable :
    Soit (EnS)n∈N avec ESn = An ∪ Nn où AnS∈ T et Nn ∈SN .         
    Alors : n∈NSEn = n∈N (An ∪ Nn )S=          n∈N An ∪      n∈N Nn .
    Posons A = n∈N An ∈ T et N = n∈N Nn .
    Pour chaque Sn, il existe Bn ∈ T tel que NnP⊂ Bn et m(Bn ) = 0.
    Alors N ⊂ n∈N Bn =: B ∈ T et m(B) ≤ n∈N m(Bn ) = 0.
                      S
    Donc N ∈ N et n∈N En ∈ Te .
       e est une mesure positive qui coïncide avec m sur T :
    2. m
    a) Bonne définition :
    Si A1 ∪ N1 = A2 ∪ N2 avec Ai ∈ T et Ni ∈ N , montrons que m(A1 ) = m(A2 ).
    On a A1 ⊂ A2 ∪ N2 ⊂ A2 ∪ B2 où m(B2 ) = 0.
    Donc m(A1 ) ≤ m(A2 ∪ B2 ) ≤ m(A2 ) + m(B2 ) = m(A2 ).
    Par symétrie, m(A2 ) ≤ m(A1 ), d’où m(A1 ) = m(A2 ).
    b) m(∅)
        e    = 0 : Clair car ∅ = ∅ ∪ ∅ et m(∅) = 0.
    c) σ-additivité : Soit (En ) des ensembles
                                       S       disjoints de Te avec En = An ∪ Nn .
    Quitte à remplacer An par An \ k<n (Ak ∪ Bk ) où Bk ⊃ Nk , on peut supposer les An
disjoints.     S               S         P             P
            e ( n En ) = m ( n An ) = n m(An ) = n m(E
    Alors : m                                              e n ).
    d) Coïncidence : Pour A ∈ T : m(A)  e    = m(A
                                                e     ∪ ∅) = m(A).




                                                                 ING1 GM – TD2       2/2




                                          5
~~~
