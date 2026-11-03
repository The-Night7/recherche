# PROBA TD1 CORRIGÉ.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Iis1fcBeFqTjdi6lqRwbWU-dHOsprRPU) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                     Correction TD 1 de Probabilités
                                           ING1-GM
                                     CYTech 2025-2026


Exercice 1
       [cites tart]L′ objectif estdedémontrerlarelationsuivanteconcernantlesf onctionsindicatricesetleslim
4] :
                     lim sup 1An − lim inf 1An = 1lim supn→∞ An \ lim inf n→∞ An
                                     n→∞
                       n→∞


Rappels de Cours
1. Limite Supérieure et Inférieure d’Ensembles
       Soit (An )n≥1 une suite d’ensembles.
       — La limite supérieure (lim supn→∞ An ) est l’ensemble des éléments qui appar-
          tiennent à une infinité d’ensembles An .
                                                         ∞ [
                                                         \ ∞
                                         lim sup An =             Ak
                                          n→∞           n=1 k=n

       — La limite inférieure (lim inf n→∞ An ) est l’ensemble des éléments qui appar-
         tiennent à tous les ensembles An à partir d’un certain rang.
                                                        ∞ \
                                                        [ ∞
                                         lim inf An =             Ak
                                          n→∞
                                                        n=1 k=n

       — On a toujours l’inclusion : lim inf n→∞ An ⊆ lim supn→∞ An .

2. Fonction Indicatrice
    La fonction indicatrice d’un ensemble A, notée 1A , est définie pour tout élément ω de
l’espace Ω par :                           
                                           1 si ω ∈ A
                                  1A (ω) =
                                           0 si ω ∈/A

3. Lien entre Indicatrices et Limites d’Ensembles
   Il existe un lien fondamental entre les limites d’une suite d’indicatrices et l’indicatrice
des limites de la suite d’ensembles correspondante :
   — 1lim sup An = lim sup 1An
   — 1lim inf An = lim inf 1An


                                                 1
~~~

## Page 2

~~~text
Démonstration
   Nous allons démontrer l’égalité en utilisant les propriétés des fonctions indicatrices.
   1. Réécriture du membre de gauche : En utilisant les relations rappelées ci-
      dessus, nous pouvons remplacer les limites de fonctions par les fonctions indica-
      trices des limites d’ensembles. Le membre de gauche de l’équation devient :
                         lim sup 1An − lim inf 1An = 1lim sup An − 1lim inf An
                           n→∞               n→∞

   2. Propriété de la différence d’ensembles : La fonction indicatrice de la différence
      de deux ensembles A et B (A \ B) est donnée par :
                                             1A\B = 1A − 1A∩B
      Appliquons cette propriété au membre de droite de l’équation à prouver :
                       1lim sup An \lim inf An = 1lim sup An − 1(lim sup An )∩(lim inf An )

   3. Utilisation de l’inclusion : Comme rappelé, on a toujours lim inf An ⊆ lim sup An .
      Par conséquent, l’intersection de ces deux ensembles est simplement la limite in-
      férieure :
                            (lim sup An ) ∩ (lim inf An ) = lim inf An
      En substituant ce résultat dans l’équation de l’étape 2, on obtient :
                              1lim sup An \lim inf An = 1lim sup An − 1lim inf An

   4. Conclusion : Nous avons montré que le membre de gauche et le membre de droite
      de l’équation initiale sont tous deux égaux à 1lim sup An −1lim inf An . L’égalité est donc
      bien vérifiée :
                      lim sup 1An − lim inf 1An = 1lim supn→∞ An \ lim inf n→∞ An
                        n→∞               n→∞




Exercice 2 (Identité de Poincaré)
      [cites tart]Ils′ agitdedémontrerlaformule du crible de Poincaré(ouprinciped′ inclusion−
exclusion)pouruneprobabilité[cite : 7] : P ( ni=1 Ai ) = ni=1 P(Ai )− 1≤i<j≤n P(Ai ∩Aj )+
                                             S          P            P

· · · + (−1)n+1 P ( ni=1 Ai )
                     T



Démonstration par Récurrence
Étape 1 : Initialisation (n=2)
   Pour n = 2, la formule s’écrit : P(A1 ∪ A2 ) = P(A1 ) + P(A2 ) − P(A1 ∩ A2 ). On
décompose A1 ∪ A2 en une union d’ensembles disjoints : A1 ∪ A2 = A1 ∪ (A2 \ A1 ). Par
additivité de la probabilité :
                              P(A1 ∪ A2 ) = P(A1 ) + P(A2 \ A1 )
Comme A1 ∩ A2 ⊆ A2 , on a P(A2 \ A1 ) = P(A2 ) − P(A1 ∩ A2 ). En substituant, on obtient
bien le résultat attendu. La propriété est vraie pour n = 2.

                                                   2
~~~

## Page 3

~~~text
Étape 2 : Hérédité
    Supposons la formule vraie pour un entier n ≥ 2 (hypothèse de récurrence). Montrons
qu’elle est vraie pour n + 1. Posons B = ni=1 Ai . On a n+1
                                                         i=1 Ai = B ∪ An+1 . En utilisant
                                         S             S

le cas n = 2 :
                   P(B ∪ An+1 ) = P(B) + P(An+1 ) − P(B ∩ An+1 ) (∗)
Par hypothèse de récurrence sur P(B) et sur P(B ∩ An+1 ) = P ( ni=1 (Ai ∩ An+1 )), on a :
                                                                                  S

                                n
                                    (−1)k+1
                                X                     X
                      P(B) =                                       P(Ai1 ∩ · · · ∩ Aik )
                                k=1              1≤i1 <···<ik ≤n
                                 n
                                    (−1)k+1
                                X                     X
            P(B ∩ An+1 ) =                                         P(Ai1 ∩ · · · ∩ Aik ∩ An+1 )
                                k=1              1≤i1 <···<ik ≤n

En substituant dans (∗) et en réarrangeant les sommes, on regroupe les termes selon le
nombre d’éléments dans l’intersection. Par exemple, pour les intersections de 2 éléments :
                  X                       n
                                          X                                  X
            −             P(Ai ∩ Aj ) −         P(Ai ∩ An+1 ) = −                     P(Ai ∩ Aj )
                1≤i<j≤n                   i=1                            1≤i<j≤n+1

Le même regroupement s’opère pour toutes les tailles d’intersections, ce qui nous amène
à la formule au rang n + 1.

Étape 3 : Conclusion
   La propriété étant vraie pour n = 2 et étant héréditaire, elle est vraie pour tout entier
n ≥ 2 par le principe de récurrence.


Exercice 3
    L’objectif est de démontrer que si P(A) = 34 et P(B) = 13 , alors on a nécessairement
l’encadrement suivant pour la probabilité de l’intersection :
                                          1               1
                                             ≤ P(A ∩ B) ≤
                                          12              3

Démonstration de la borne supérieure
   Cette borne découle de la monotonie de la probabilité.
    1. L’intersection A ∩ B est un sous-ensemble de A et de B :

                                      A ∩ B ⊆ A et A ∩ B ⊆ B

    2. La propriété de monotonie de la probabilité (si E ⊆ F , alors P(E) ≤ P(F ))
       implique :
                                             3                            1
                      P(A ∩ B) ≤ P(A) =         et P(A ∩ B) ≤ P(B) =
                                             4                            3
    3. La probabilité de l’intersection doit donc être inférieure à la plus petite des deux
       valeurs :
                                                     3 1       1
                                                         
                                   P(A ∩ B) ≤ min ,         =
                                                     4 3       3

                                                      3
~~~

## Page 4

~~~text
Démonstration de la borne inférieure
   Cette borne se démontre en utilisant la formule de la probabilité de l’union.
   1. La formule générale est :
                                    P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
   2. En réarrangeant, on obtient :
                                    P(A ∩ B) = P(A) + P(B) − P(A ∪ B)
   3. La probabilité d’un événement est toujours inférieure ou égale à 1, donc P(A∪B) ≤
      1. Cela implique −P(A ∪ B) ≥ −1.
   4. En substituant cette inégalité dans la formule, on a :
                                            P(A ∩ B) ≥ P(A) + P(B) − 1
    5. En remplaçant par les valeurs numériques :
                                             3 1
                                  P(A ∩ B) ≥ + − 1
                                             4 3
                                              9    4   12
                                           ≥     +   −
                                             12 12 12
                                              1
                                           ≥
                                             12
L’encadrement est donc entièrement démontré.



Exercice 4 (Sous-additivité)
   Il s’agit de démontrer l’inégalité de Boole pour un cas fini et un cas infini dénombrable.

1. Cas Fini
   Nous devons montrer par récurrence sur n que :
                                                n              n
                                                       !
                                                [              X
                                            P         Ai ≤           P(Ai )
                                                i=1            i=1


Initialisation (n=2) : On sait que P(A1 ∪ A2 ) = P(A1 ) + P(A2 ) − P(A1 ∩ A2 ). Comme
P(A1 ∩ A2 ) ≥ 0, on a bien P(A1 ∪ A2 ) ≤ P(A1 ) + P(A2 ). La base est vérifiée.

Hérédité : Supposons la propriété vraie pour un entier n ≥ 2. Montrons-la pour n + 1.
Posons B = ni=1 Ai .
          S

             n+1
                     !
             [
         P         Ai = P(B ∪ An+1 )
             i=1
                         ≤ P(B) + P(An+1 ) (par le cas n=2)
                              n
                                            !
                              X
                         ≤          P(Ai ) + P(An+1 ) (par hypothèse de récurrence)
                              i=1
                             n+1
                             X
                         =         P(Ai )
                             i=1


                                                           4
~~~

## Page 5

~~~text
La propriété est héréditaire.

Conclusion : Par le principe de récurrence, l’inégalité est vraie pour tout n ≥ 1.

2. Cas Infini Dénombrable
    Nous devons montrer que :
                                                   ∞                 ∞
                                                            !
                                                   [                 X
                                            P           Ai ≤               P(Ai )
                                                  i=1                i=1

    1. On construit une suite d’événements (Bi )i≥1 disjoints :
                                                                                               n−1
                                                                                                      !
                                                                                               [
                       B1 = A1 ,   B2 = A2 \ A1 ,                   ...,     Bn = An \               Ai ,   ...
                                                                                               i=1

    2. Par construction, les Bi sont deux à deux disjoints (Bi ∩ Bj = ∅ pour i ̸= j) et
       S∞        S∞
        i=1 Bi = i=1 Ai .
    3. Par σ-additivité de la probabilité sur des événements disjoints :
                                            ∞                         ∞             ∞
                                                    !                        !
                                            [                         [             X
                                       P          Ai = P                   Bi =           P(Bi )
                                            i=1                      i=1            i=1

    4. Comme Bi ⊆ Ai pour tout i, la monotonie de la probabilité implique P(Bi ) ≤
       P(Ai ).
    5. En combinant les deux derniers points, on obtient le résultat :
                                             ∞                  ∞                   ∞
                                                        !
                                             [                  X                   X
                                       P           Ai =               P(Bi ) ≤            P(Ai )
                                             i=1                i=1                 i=1


Rappel de Cours : Le Principe d’Inclusion-Exclusion
(Formule de Poincaré)
   Avant d’aborder les inégalités de Bonferroni, il est utile de rappeler la formule de
Poincaré, également connue sous le nom de principe d’inclusion-exclusion. Cette formule
donne la probabilité de l’union d’un nombre fini d’événements.
   Pour n événements A1 , A2 , . . . , An , la formule est la suivante :
    n            n                                                                                                      n
           !                                                                                                                       !
                                                                                                              n+1
    [            X                 X                                X                                                   \
P         Ai =         P(Ai )−             P(Ai ∩Aj )+                        P(Ai ∩Aj ∩Ak )−· · ·+(−1)             P         Ai
    i=1          i=1         1≤i<j≤n                        1≤i<j<k≤n                                                   i=1

    Cette formule fonctionne en additionnant les probabilités des événements individuels,
puis en soustrayant les probabilités des intersections deux à deux (car elles ont été comp-
tées deux fois), puis en ajoutant les probabilités des intersections trois à trois (car elles
ont été soustraites trop de fois), et ainsi de suite.
    Les inégalités de Bonferroni sont des approximations de cette formule, fournissant
des bornes inférieures et supérieures pour la probabilité de l’union.




                                                                5
~~~

## Page 6

~~~text
Exercice 5 : Inégalités de Bonferroni
  L’objectif est de démontrer les deux inégalités suivantes.

a) Borne inférieure
  Énoncé : Montrer que P ( ni=1 Ai ) ≥
                                                           Pn
                                                            i=1 P(Ai ) −         1≤i<j≤n P(Ai ∩ Aj ).
                                         S                                    P


  Démonstration par récurrence :
  — Initialisation (n=2) : Nous savons que P(A1 ∪A2 ) = P(A1 )+P(A2 )−P(A1 ∩A2 ).
    L’inégalité devient une égalité, donc la propriété est vraie pour n = 2.
  — Hérédité : Supposons que la propriété est vraie pour un certain rang n ≥ 2.
    Montrons qu’elle est vraie pour n + 1. Posons Bn = ni=1 Ai . On a :
                                                          S

                         n+1
                                 !
                         [
                P              Ai = P(Bn ∪ An+1 ) = P(Bn ) + P(An+1 ) − P(Bn ∩ An+1 )
                         i=1

     En utilisant l’hypothèse de récurrence sur P(Bn ) :
                                                    n
                                                    X                   X
                                     P(Bn ) ≥             P(Ai ) −              P(Ai ∩ Aj )
                                                    i=1               1≤i<j≤n

     Donc :
                                                                        
         n+1                n                                                                       n
                    !                                                                                     !          !
         [                 X                       X                                                [
     P         Ai       ≥  P(Ai ) −                       P(Ai ∩ Aj ) + P(An+1 ) − P                   Ai ∩ An+1
         i=1                   i=1               1≤i<j≤n                                           i=1

     Réorganisons les termes :
                        n+1          n+1                                                 n
                                !                                                                           !
                        [            X                      X                            [
               P              Ai ≥           P(Ai ) −                P(Ai ∩ Aj ) − P           (Ai ∩ An+1 )
                        i=1          i=1                  1≤i<j≤n                        i=1

     En utilisant la sous-additivité (Exercice 4), on sait que P( ni=1 Ci ) ≤
                                                                                          S               Pn
                                                                                                           i=1 P(Ci ).
     Appliquons cela à la dernière union :
                                             n                         n
                                                                 !
                                             [                         X
                                     P           (Ai ∩ An+1 ) ≤              P(Ai ∩ An+1 )
                                           i=1                         i=1

     En injectant cette majoration dans notre inégalité (attention au signe négatif) :
                         n+1             n+1                                           n
                                 !
                         [               X                   X                         X
                   P           Ai ≥            P(Ai ) −               P(Ai ∩ Aj ) −          P(Ai ∩ An+1 )
                         i=1             i=1               1≤i<j≤n                     i=1

     Le terme ni=1 P(Ai ∩ An+1 ) correspond aux paires (i, n + 1) avec i < n + 1. En le
                    P

     combinant avec 1≤i<j≤n P(Ai ∩ Aj ), on obtient exactement la somme de toutes
                        P

     les paires (i, j) avec 1 ≤ i < j ≤ n + 1 :
                                     n+1             n+1
                                               !
                                     [               X                       X
                                 P         Ai ≥            P(Ai ) −                 P(Ai ∩ Aj )
                                     i=1             i=1               1≤i<j≤n+1

    La propriété est donc vraie au rang n + 1.
  — Conclusion : Par le principe de récurrence, l’inégalité est vraie pour tout n ≥ 2.

                                                             6
~~~

## Page 7

~~~text
b) Borne supérieure
   Énoncé : Montrer que P ( ni=1 Ai ) ≤
                                          Pn
                                                             1≤i<j≤n P(Ai ∩Aj )+   1≤i<j<k≤n P(Ai ∩
                             S                          P                      P
                                           i=1 P(Ai )−
Aj ∩ Ak ).

    Explication : La démonstration est similaire à la précédente, en utilisant une récur-
rence et en s’appuyant sur l’inégalité démontrée en (a). La formule de Poincaré est une
somme alternée. La première inégalité de Bonferroni (Exercice 4, sous-additivité) montre
que la somme s’arrête après un nombre impair de termes (1) est une borne supérieure.
La deuxième (ci-dessus) montre que s’arrêter après un nombre pair de termes (2) est une
borne inférieure. Cette propriété continue : la somme partielle de la formule de Poincaré
est alternativement une borne supérieure et une borne inférieure de la probabilité de
l’union.




Rappel de Cours : Tribu et Mesure de Probabilité
   — Tribu (ou σ-algèbre) : Soit Ω un ensemble. Une famille F de sous-ensembles de
     Ω est une tribu si elle vérifie les trois axiomes suivants :
     1. Ω ∈ F (L’univers est dans la tribu).
     2. Stabilité par passage au complémentaire : Si A ∈ F, alors son complé-
         mentaire Ac est aussi dans F.
     3. Stabilité par union dénombrable : Si (An )n≥1 est une suite d’ensembles de
         F, alors leur union ∞  n=1 An est aussi dans F.
                              S

   — Mesure de Probabilité : Soit (Ω, F) un espace mesurable. Une application
     P : F → [0, 1] est une mesure de probabilité si elle vérifie :
     1. P(Ω) = 1.
     2. σ-additivité : Pour toute suite (An )n≥1 d’ensembles de F qui sont deux à
         deux disjoints (c’est-à-dire Ai ∩ Aj = ∅ pour i ̸= j), on a :
                                          ∞            ∞
                                                   !
                                          [            X
                                     P          An =         P(An )
                                          n=1          n=1




Exercice 6
Partie 1 : Montrer que F est une tribu
    On définit F = {A ⊂ R | A est dénombrable ou Ac est dénombrable}. Vérifions les
trois axiomes d’une tribu.
   1. R ∈ F ?
      Le complémentaire de R est ∅. L’ensemble vide est dénombrable (fini, de cardinal
      0). Donc, par définition, R ∈ F.

                                               7
~~~

## Page 8

~~~text
   2. Stabilité par passage au complémentaire ?
      Soit A ∈ F. Par définition, cela signifie que (A est dénombrable) ou (Ac est dénom-
      brable). Considérons le complémentaire de A, noté Ac . Pour que Ac ∈ F, il faut
      que (Ac est dénombrable) ou ((Ac )c = A est dénombrable). Ceci est exactement la
      même condition. La définition est symétrique pour A et Ac , donc la stabilité est
      vérifiée.
   3. Stabilité par union dénombrable ?
      Soit (An )n≥1 une suite d’éléments de F. Montrons que A = ∞        n=1 An ∈ F. On
                                                                       S

      distingue deux cas :
      — Cas 1 : Tous les An sont dénombrables.
          Une union dénombrable d’ensembles dénombrables est elle-même dénombrable.
          Donc, A = ∞  n=1 An est dénombrable. Par définition de F, si A est dénombrable,
                     S

          alors A ∈ F.
      — Cas 2 : Il existe au moins un An0 tel que Acn0 est dénombrable.
          On veut montrer que A = ∞     n=1 An est dans F. Pour cela, montrons que son
                                      S
                            c
          complémentaire A est dénombrable.
                                                  ∞
                                                             !c       ∞
                                          c
                                                                            Acn
                                                  [                   \
                                      A =               An        =
                                                  n=1                 n=1

          Nous savons que l’intersection est un sous-ensemble de chacun de ses membres.
          En particulier :
                                                 ∞
                                                      Acn ⊂ Acn0
                                                 \

                                                n=1

          Puisque Acn0 est dénombrable, et que tout sous-ensemble d’un ensemble dé-
        nombrable est au plus dénombrable, Ac est dénombrable. Par définition de F,
        si Ac est dénombrable, alors A ∈ F.
      Dans tous les cas, l’union dénombrable est dans F.
Les trois axiomes étant vérifiés, F est bien une tribu sur R.

Partie 2 : Montrer que P est une mesure de probabilité
   On définit P : F → [0, 1] par :
                                     
                                     0       si A est dénombrable
                          P(A) =
                                     1       si Ac est dénombrable

Note : Un ensemble A ∈ F ne peut pas être à la fois dénombrable et avoir un complé-
mentaire dénombrable. Si c’était le cas, R = A ∪ Ac serait une union de deux ensembles
dénombrables, et serait donc dénombrable, ce qui est faux. La fonction P est donc bien
définie.

   Vérifions les deux axiomes.
   1. P(R) = 1 ?
      Le complémentaire de R est ∅, qui est dénombrable. On est donc dans le second
      cas de la définition : P(R) = 1. L’axiome est vérifié.



                                                 8
~~~

## Page 9

~~~text
   2. σ-additivité ?
      Soit (An )n≥1 une suite d’éléments de F deux à deux disjoints. Posons A =
      S∞                                      P∞
       n=1 An . On doit montrer que P(A) =      n=1 P(An ). On distingue deux cas :
      — Cas 1 : Tous les An sont dénombrables.
         Dans ce cas, P(An ) = 0 pour tout n. La somme est ∞
                                                                 P
                    S∞                                             n=1 0 = 0. D’un autre
         côté, A = n=1 An est une union dénombrable d’ensembles dénombrables, donc
                                                                            P
         A est dénombrable. Par définition, P(A) = 0. On a bien P(A) = P(An ).
      — Cas 2 : Il existe un unique indice n0 tel que Acn0 est dénombrable.
         Il ne peut y avoir plus d’un tel indice. Si Acn0 et Acn1 (pour n0 ̸= n1 ) étaient
         dénombrables, leur union le serait aussi. Or An0 ∩ An1 = (Acn0 ∪ Acn1 )c . Le
         complémentaire d’un ensemble dénombrable ne peut être vide, ce qui contredit
         le fait que An0 et An1 sont disjoints.
             Donc, un seul terme P(An0 ) vaut 1, et tous les autres sont nuls. La somme
         vaut :                            ∞   X
                                                     P(An ) = 1
                                               n=1
                                                        S∞                         c
         Maintenant, calculons P(A). On a A =               n=1 An . Montrons que A est dénom-
         brable.                           !c
                                          ∞                  ∞
                                 Ac =                             Acn ⊂ Acn0
                                          [                  \
                                                An      =
                                          n=1               n=1

         Puisque Acn0  est dénombrable, son sous-ensemble Ac est aussi dénombrable.
         Par définition, comme Ac est dénombrable, on a P(A) = 1. On a bien P(A) =
         P
           P(An ).
Les deux axiomes sont vérifiés, P définit bien une mesure de probabilité sur (R, F).


Rappel de Cours : Indépendance et Inégalité Utile
   — Indépendance d’événements : Une famille d’événements (Ai )i∈I est dite mu-
     tuellement indépendante si pour toute sous-partie finie J ⊂ I, on a :
                                                   
                                         \               Y
                                    P         Aj  =          P(Aj )
                                         j∈J             j∈J


     Une propriété importante est que si les événements (Ai ) sont indépendants, alors
     leurs complémentaires (Aci ) le sont aussi.
   — Inégalité de convexité : Pour tout nombre réel x, on a l’inégalité suivante :

                                               1 + x ≤ ex

      En posant u = −x, cela est équivalent à 1 − u ≤ e−u pour tout u ∈ R. Cette
      inégalité est fondamentale pour borner des produits de probabilités.




                                                9
~~~

## Page 10

~~~text
Exercice 7
   Énoncé : Soit (Ai )1≤i≤n une suitePd’événements indépendants. [cites tart]M ontrerquelaprobabilitépou
                                       n
                                     − i=1 P(Ai )
ne soit réalisé est au plus égale à e             . [cite : 18, 19]

   Démonstration :
   1. L’événement "aucun des Ai n’est réalisé" correspond à l’intersection des événements
      complémentaires Aci . Nous cherchons donc à majorer la probabilité :
                                                                                n
                                                                                            !
                              P(Ac1 ∩ Ac2 ∩ · · · ∩ Acn ) = P                         Aci
                                                                                \

                                                                                i=1


   2. Les événements Ai sont indépendants, donc leurs complémentaires Aci le sont aussi.
      Par définition de l’indépendance, la probabilité de l’intersection est le produit des
      probabilités :
                                            n                   n
                                             !
                                                  Aci =                P(Aci )
                                            \                   Y
                                       P
                                            i=1                 i=1

   3. Pour chaque événement, on sait que P(Aci ) = 1 − P(Ai ). L’expression devient :
                                             n
                                             Y
                                                   (1 − P(Ai ))
                                             i=1


   4. Nous utilisons maintenant l’inégalité fondamentale 1 − x ≤ e−x . En posant x =
      P(Ai ) pour chaque terme du produit (ce qui est légitime car P(Ai ) ∈ [0, 1]), on
      obtient :
                                     1 − P(Ai ) ≤ e−P(Ai )
   5. En appliquant cette majoration à chaque terme du produit (tous les termes étant
      positifs), on a :
                                    n                             n
                                                                        e−P(Ai )
                                    Y                             Y
                                          (1 − P(Ai )) ≤
                                    i=1                           i=1

   6. En utilisant la propriété de l’exponentielle (ea eb = ea+b ), le produit des exponen-
      tielles devient l’exponentielle de la somme :
                           n                     Pn                             Pn
                                 e−P(Ai ) = e              (−P(Ai ))
                                                                       = e−                 P(Ai )
                           Y
                                                   i=1                                i=1

                           i=1


   7. En combinant toutes les étapes, nous arrivons à la conclusion souhaitée :
                                           n
                                                       !
                                                                  Pn
                                                 Aci       ≤ e−              P(Ai )
                                           \
                                     P                                 i=1

                                           i=1




                                                  10
~~~

## Page 11

~~~text
Rappel de Cours : Probabilité Conditionnelle
      — Définition : La probabilité conditionnelle d’un événement E sachant un événe-
        ment F (de probabilité non nulle) est définie par :

                                                    P(E ∩ F )
                                        P(E|F ) =
                                                      P(F )

      — Monotonie de la probabilité : Si un événement E1 est inclus dans un événement
        E2 (c’est-à-dire E1 ⊆ E2 ), alors leurs probabilités respectent la même relation
        d’ordre :
                                         P(E1 ) ≤ P(E2 )




Exercice 8
      Énoncé : Soit P(A) > 0. [cites tart]M ontrerqueP(A ∩B|A ∪ B) ≤ P(A ∩ B|A). [cite :
20]

      Démonstration :
      1. Commençons par écrire les définitions des deux termes de l’inégalité en utilisant
         la formule de la probabilité conditionnelle.
             Pour le terme de gauche :

                                                   P((A ∩ B) ∩ (A ∪ B))
                            P(A ∩ B|A ∪ B) =
                                                        P(A ∪ B)

            Pour le terme de droite :
                                                   P((A ∩ B) ∩ A)
                                  P(A ∩ B|A) =
                                                        P(A)

      2. Simplifions les numérateurs.
         — L’ensemble A ∩ B est par définition inclus dans A et dans B, il est donc
            nécessairement inclus dans A∪B. Par conséquent, l’intersection (A∩B)∩(A∪B)
            est simplement A ∩ B.
         — De même, l’ensemble A ∩ B est inclus dans A. L’intersection (A ∩ B) ∩ A est
            donc aussi A ∩ B.
            Les deux expressions deviennent :

                                        P(A ∩ B)                          P(A ∩ B)
                   P(A ∩ B|A ∪ B) =                  et P(A ∩ B|A) =
                                        P(A ∪ B)                            P(A)

      3. L’inégalité que nous devons démontrer est donc équivalente à :

                                        P(A ∩ B)   P(A ∩ B)
                                                 ≤
                                        P(A ∪ B)     P(A)

                                             11
~~~

## Page 12

~~~text
  4. Analysons cette dernière inégalité.
     — Si P(A ∩ B) = 0, l’inégalité devient 0 ≤ 0, ce qui est vrai.
     — Si P(A ∩ B) > 0, nous pouvons diviser les deux côtés par ce terme positif sans
       changer le sens de l’inégalité. On obtient :
                                          1         1
                                                ≤
                                       P(A ∪ B)   P(A)

        Ce qui est équivalent à :
                                       P(A) ≤ P(A ∪ B)
  5. Cette dernière inégalité est toujours vraie. En effet, l’événement A est inclus dans
     l’événement A ∪ B (c’est-à-dire A ⊆ A ∪ B). Par la propriété de monotonie de la
     probabilité, on a bien P(A) ≤ P(A ∪ B).
  6. Puisque nous sommes arrivés à une proposition toujours vraie, l’inégalité de départ
     est démontrée.


Rappel de Cours : Indépendance et Continuité de la
Probabilité
        [cites tart]

 — Indépendance mutuelle : [cite : 21] Des événements A, B, C sont dits mutuel-
   lement indépendants si les conditions suivantes sont toutes vérifiées :
     1. P(A ∩ B) = P(A)P(B)
     2. P(A ∩ C) = P(A)P(C)
     3. P(B ∩ C) = P(B)P(C)
     4. P(A ∩ B ∩ C) = P(A)P(B)P(C)
   L’indépendance de A et B est une condition nécessaire mais non suffisante pour
   l’indépendance mutuelle de A, B, C.
 — Continuité de la mesure de probabilité : Soit (An )n∈N une suite d’événements.
   Si la suite converge vers un événement A (noté An → A), alors la suite de leurs
   probabilités converge vers la probabilité de A.

                                      lim P(An ) = P(A)
                                      n→∞

     Cette propriété, issue du théorème de la convergence dominée, s’étend aux inter-
     sections : si An → A et Bn → B, alors (An ∩ Bn ) → (A ∩ B) et donc :

                                lim P(An ∩ Bn ) = P(A ∩ B)
                                n→∞




                                            12
~~~

## Page 13

~~~text
Exercice 9
   Énoncé : Soient A, B, C sont indépendants et P(A∩B) ̸= 0. [cites tart]M ontrerqueP(C
| A ∩B) = P(C)[cite : 21].

   Démonstration :
    1. Par définition de la probabilité conditionnelle, et puisque P(A ∩ B) ̸= 0, on peut
       écrire :
                                        P(C ∩ (A ∩ B))      P(A ∩ B ∩ C)
                        P(C|A ∩ B) =                     =
                                           P(A ∩ B)           P(A ∩ B)
    2. On utilise l’hypothèse d’indépendance mutuelle des événements A, B et C.
       — Pour le numérateur : P(A ∩ B ∩ C) = P(A)P(B)P(C).
       — Pour le dénominateur : L’indépendance de A et B (qui est une conséquence de
          l’indépendance mutuelle) implique P(A ∩ B) = P(A)P(B).
    3. En substituant ces expressions dans la fraction, on obtient :
                                                   P(A)P(B)P(C)
                                  P(C|A ∩ B) =
                                                     P(A)P(B)
    4. La condition P(A ∩ B) ̸= 0 implique que P(A) ̸= 0 et P(B) ̸= 0. Nous pouvons
       donc simplifier la fraction en toute sécurité :
                                        P(C|A ∩ B) = P(C)
Ceci démontre que la connaissance de la réalisation de l’événement A ∩ B ne modifie pas
la probabilité de l’événement C, ce qui est une illustration de la notion d’indépendance.




Exercice 10
   Énoncé : Soit (An )n∈N∗ → A et (Bn )n∈N∗ → B. [cites tart]SupposonsaussiqueP(B)>0etP(Bn ) >
0 pour tout n[cite : 22]. Montrer les convergences suivantes.

a) limn→∞ P(An |B) = P(A|B)
                                               n ∩B)
   [cites tart]P ardéf inition,P(An |B) = P(AP(B)    [cite : 24]. Prenons la limite lorsque n →
∞:
                                                       P(An ∩ B)
                                 lim P(An |B) = lim
                                n→∞              n→∞       P(B)
Le dénominateur P(B) est une constante positive. La limite du quotient est donc le
quotient de la limite :
                                               limn→∞ P(An ∩ B)
                              lim P(An |B) =
                             n→∞                        P(B)
Comme An → A, on a aussi (An ∩ B) → (A ∩ B). Par la propriété de continuité de la
mesure de probabilité, limn→∞ P(An ∩ B) = P(A ∩ B). On a donc :
                                             P(A ∩ B)
                            lim P(An |B) =            = P(A|B)
                           n→∞                 P(B)

                                              13
~~~

## Page 14

~~~text
b) limn→∞ P(A|Bn ) = P(A|B)
                                                 n)
    [cites tart]P ardéf inition,P(A|Bn ) = P(A∩B
                                            P(Bn )
                                                    [cite : 25]. En passant à la limite :

                                                       P(A ∩ Bn )
                                 lim P(A|Bn ) = n→∞
                                                 lim
                                n→∞                      P(Bn )

Ici, le numérateur et le dénominateur dépendent de n. On utilise la propriété que la limite
d’un quotient est le quotient des limites (si la limite du dénominateur est non nulle).
     — Pour le numérateur : Bn → B =⇒ (A ∩ Bn ) → (A ∩ B). Par continuité,
         limn→∞ P(A ∩ Bn ) = P(A ∩ B).
     — Pour le dénominateur : Bn → B. Par continuité, limn→∞ P(Bn ) = P(B). [cites tart]OnnousdonneP
         22].
Ainsi, la limite est bien définie et vaut :

                                                 P(A ∩ B)
                              lim P(A|Bn ) =              = P(A|B)
                             n→∞                   P(B)

c) limn→∞ P(An |Bn ) = P(A|B)
    La logique est identique à celle des points précédents. [cites tart]P ardéf inition,P(An |Bn ) =
P(An ∩Bn )
  P(Bn )
           [cite : 26].

                                             P(An ∩ Bn )   limn→∞ P(An ∩ Bn )
                    lim P(An |Bn ) = n→∞
                                      lim                =
                   n→∞                         P(Bn )         limn→∞ P(Bn )

   — Pour le numérateur : An → A et Bn → B =⇒ (An ∩ Bn ) → (A ∩ B). Par
      continuité, limn→∞ P(An ∩ Bn ) = P(A ∩ B).
   — Pour le dénominateur : Comme en b), limn→∞ P(Bn ) = P(B) > 0.
On conclut donc :
                                          P(A ∩ B)
                         lim P(An |Bn ) =          = P(A|B)
                        n→∞                 P(B)

Rappel de Cours : Formule des Probabilités Totales
et Formule de Bayes
    — Formule des probabilités totales : Soit (Bi )ni=1 une famille d’événements qui
      forme une partition de l’univers Ω. Cela signifie que les Bi sont deux à deux
      disjoints (Bi ∩ Bj = ∅ pour i ̸= j) et que leur union est l’univers entier ( ni=1 Bi =
                                                                                  S

      Ω).
          Pour tout événement A, sa probabilité peut être calculée en le décomposant
      selon la partition :
                                       n
                                       X                    n
                                                            X
                              P(A) =         P(A ∩ Bi ) =         P(A|Bi )P(Bi )
                                       i=1                  i=1

        Cette formule est très utile lorsqu’une expérience se déroule en plusieurs étapes.




                                                 14
~~~

## Page 15

~~~text
   — Formule de Bayes : La formule de Bayes permet d’"inverser" une probabilité
     conditionnelle, c’est-à-dire de calculer P(B|A) quand on connaît P(A|B). La for-
     mule est la suivante :
                                               P(A|B)P(B)
                                    P(B|A) =
                                                  P(A)
      Le dénominateur P(A) est souvent calculé à l’aide de la formule des probabilités
      totales. Cette formule est centrale en inférence statistique et pour les problèmes
      de diagnostic.




Exercice 11
   Énoncé : On dispose de deux urnes, la première contenant 1 boule et 3 boules, la
seconde contenant 2 boules et 2 boules. L’expérience consiste à choisir d’abord une urne,
puis à tirer une boule dans l’urne choisie. On cherche la probabilité de l’événement A =
"on tire une boule."

   Interprétation et résolution : L’énoncé est incomplet. Nous allons l’interpréter de
la manière la plus classique :
   — Urne 1 (U1 ) : 1 boule Noire (N) et 3 boules Blanches (B). Total : 4 boules.
   — Urne 2 (U2 ) : 2 boules Noires (N) et 2 boules Blanches (B). Total : 4 boules.
   — L’événement A est "on tire une boule Noire".
   — Le choix de l’urne est équiprobable : P(U1 ) = P(U2 ) = 12 .
   Nous cherchons P(A). Les événements {U1 , U2 } forment une partition de l’univers.
Nous pouvons donc utiliser la formule des probabilités totales :

                         P(A) = P(A|U1 )P(U1 ) + P(A|U2 )P(U2 )

   Calculons les probabilités conditionnelles :
   — P(A|U1 ) est la probabilité de tirer une boule noire sachant qu’on a choisi l’urne 1.

                                    nombre de boules noires dans U1   1
                       P(A|U1 ) =                                   =
                                    nombre total de boules dans U1    4
   — P(A|U2 ) est la probabilité de tirer une boule noire sachant qu’on a choisi l’urne 2.

                                  nombre de boules noires dans U2  2  1
                     P(A|U2 ) =                                   = =
                                  nombre total de boules dans U2   4  2
   Appliquons la formule :
                               1 1   1 1  1 1 1 2  3
                                               
                  P(A) =        ×  +  ×  = + = + =
                               4 2   2 2  8 4 8 8  8
   La probabilité de tirer une boule noire est de 83 .




                                             15
~~~

## Page 16

~~~text
Exercice 12
    Énoncé : Chaque don de sang est soumis à un test du Col. On suppose que ce test
a une efficacité de 99%, et une probabilité de fausse alarme de 5%. Enfin, on suppose
la fréquence de séropositivité est 10−4 . Quelle est la probabilité pour qu’une personne
obtenant un test positif soit atteinte du Col ?

   Résolution : C’est un problème d’application directe de la formule de Bayes.
    1. Définir les événements :
       — C : "La personne est atteinte du Col".
       — C c : "La personne n’est pas atteinte du Col".
       — T + : "Le test est positif".
       — T − : "Le test est négatif".
    2. Traduire les données de l’énoncé :
       — Efficacité de 99% (sensibilité) : P(T + |C) = 0.99.
       — Fausse alarme de 5% (taux de faux positifs) : P(T + |C c ) = 0.05.
       — Fréquence de séropositivité (prévalence) : P(C) = 10−4 = 0.0001.
       On en déduit la probabilité de ne pas être atteint :

                            P(C c ) = 1 − P(C) = 1 − 0.0001 = 0.9999

    3. Identifier l’objectif : On cherche la probabilité qu’une personne soit atteinte
       sachant que son test est positif, c’est-à-dire P(C|T + ).
    4. Appliquer la formule de Bayes :

                                                   P(T + |C)P(C)
                                     P(C|T + ) =
                                                      P(T + )

    5. Calculer le dénominateur P(T + ) : On utilise la formule des probabilités totales
       avec la partition {C, C c } :

                            P(T + ) = P(T + |C)P(C) + P(T + |C c )P(C c )

                           P(T + ) = (0.99 × 0.0001) + (0.05 × 0.9999)
                            P(T + ) = 0.000099 + 0.049995 = 0.050094
    6. Calculer le résultat final :
                                     0.99 × 0.0001   0.000099
                       P(C|T + ) =                 =          ≈ 0.001976
                                       0.050094      0.050094
    Conclusion et interprétation : La probabilité qu’une personne ayant un test positif
soit réellement atteinte du Col est d’environ 0.2%. Ce résultat, qui peut paraître surpre-
nant, est typique des situations de dépistage de maladies rares. Même avec un test assez
fiable, un résultat positif est beaucoup plus susceptible d’être un "faux positif" (une per-
sonne saine testée positive) qu’un "vrai positif", car la population saine est immensément
plus grande que la population atteinte.




                                             16
~~~

## Page 17

~~~text
Analyse du problème et définitions
   Ce problème illustre la différence entre l’indépendance conditionnelle et l’indépen-
dance globale. On nous donne les informations suivantes :
   — Une partition de la population en deux groupes de taille égale : les conducteurs
      masculins (Hommes, H) et féminins (Femmes, F ). On a donc :
                                                      1
                                       P(H) = P(F ) =
                                                      2
   — La probabilité annuelle d’accident est constante pour chaque groupe :
      — Pour un homme : P(Accident|H) = α
      — Pour une femme : P(Accident|F ) = β
   — Les accidents sont indépendants d’une année sur l’autre pour une personne
      donnée.
   Définissons l’événement Ai = "la personne sélectionnée a un accident l’année i".
L’énoncé nous dit donc :
                            P(Ai |H) = α et P(Ai |F ) = β
L’indépendance des années pour une personne donnée se traduit par :
                        P(A2 ∩ A1 |H) = P(A2 |H)P(A1 |H) = α2
                        P(A2 ∩ A1 |F ) = P(A2 |F )P(A1 |F ) = β 2




a) Probabilité d’un accident une année donnée
   On cherche P(A1 ). Puisque {H, F } forme une partition de l’univers, on utilise la
formule des probabilités totales :
                        P(A1 ) = P(A1 |H)P(H) + P(A1 |F )P(F )
En remplaçant par les valeurs connues :
                                         1      1     α+β
                            P(A1 ) = α ·   +β· =
                                         2      2       2
La probabilité qu’une personne choisie au hasard ait un accident est bien la moyenne des
probabilités des deux groupes.

b) Probabilité d’un accident deux années consécutives
   On cherche P(A1 ∩ A2 ). On utilise à nouveau la formule des probabilités totales :
                P(A1 ∩ A2 ) = P(A1 ∩ A2 |H)P(H) + P(A1 ∩ A2 |F )P(F )
Grâce à l’indépendance conditionnelle (les accidents sont indépendants pour un type de
conducteur donné) :
                                              1           1  α2 + β 2
                      P(A1 ∩ A2 ) = (α2 ) ·     + (β 2 ) · =
                                              2           2     2
                                              17
~~~

## Page 18

~~~text
c) Montrer que P(A2 |A1 ) ≥ P(A1 )
   Calculons d’abord P(A2 |A1 ) en utilisant sa définition :
                                                  P(A1 ∩ A2 )
                                  P(A2 |A1 ) =
                                                    P(A1 )
En utilisant les résultats de a) et b) :
                                            (α2 + β 2 )/2   α2 + β 2
                            P(A2 |A1 ) =                  =
                                             (α + β)/2       α+β
Nous devons maintenant prouver l’inégalité :
                                      α2 + β 2   α+β
                                               ≥
                                       α+β        2
Comme α et β sont des probabilités, les dénominateurs sont positifs. On peut multiplier
sans changer le sens de l’inégalité :
                                   2(α2 + β 2 ) ≥ (α + β)2
                                2α2 + 2β 2 ≥ α2 + 2αβ + β 2
En réarrangeant tous les termes d’un côté :
                                     α2 − 2αβ + β 2 ≥ 0
On reconnaît une identité remarquable :
                                           (α − β)2 ≥ 0
Le carré d’un nombre réel est toujours positif ou nul. L’inégalité est donc toujours vraie.
   Interprétation : Ce résultat est très important. Il montre que même si les acci-
dents sont indépendants pour une personne donnée, les événements A1 et A2 ne sont pas
indépendants dans la population globale. Le fait d’avoir eu un accident l’année 1 (A1 )
nous donne une information sur la personne : il est plus probable qu’elle appartienne au
groupe ayant le plus haut risque d’accident (le groupe où la probabilité, α ou β, est la
plus grande). Cette information met à jour notre croyance et augmente la probabilité
d’un accident pour l’année 2.

d) Probabilité qu’un accidenté soit une conductrice
   On cherche la probabilité que la personne soit une femme, sachant qu’elle a eu un
accident l’année 1, c’est-à-dire P(F |A1 ). C’est une application directe de la formule de
Bayes :
                                              P(A1 |F )P(F )
                                 P(F |A1 ) =
                                                    P(A1 )
Nous avons déjà calculé tous les termes nécessaires :
   — P(A1 |F ) = β
   — P(F ) = 1/2
   — P(A1 ) = α+β2
En substituant :
                                              β · 21       β
                                 P(F |A1 ) = α+β =
                                                2
                                                       α+β


                                                18
~~~
