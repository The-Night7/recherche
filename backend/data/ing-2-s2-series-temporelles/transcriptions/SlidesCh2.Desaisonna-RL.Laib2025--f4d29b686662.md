# SlidesCh2.Desaisonna-RL.Laib2025.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1FBbW9byuUwwEqSxAyNvt6nut4AOizvM1) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Séries temporelles: Chapitre II. Désaisonnalisation par la méthode de
                         régression linéaire


                                      N. Laïb

                                      CY-Tech


                                14 janvier 2025




 N. Laïb (CY-Tech)   Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                méthode
                                                                                  janvier 2025
                                                                                          de régression linéaire
                                                                                                           1 / 67
~~~

## Page 2

~~~text
Plan


1   Introduction


2   Ajustement Tendanciel- Estimation du trend en l’absence de saisonnalité


3   Détermination des coefficients saisonniers


4   Détermination de la série corrigée


5   Désaisonnalisation par régression linéaire sur Variables Indicatrices (RVI)


6   Modèle trimestriel de Buys-Ballon (1847)




       N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                     2 / 67
~~~

## Page 3

~~~text
Introduction

▷ Pourquoi désaisonnaliser une série ?

    De nombreuses séries économiques présentent des comportements périodiques, ce
    qui rend difficile la comparaison de deux instants successifs.
    La désaisonnalisation permet
       - d’obtenir des séries dites corrigées des variations saisonnières (cvs).
       - De telles séries sont obtenues en éliminant la composante saisonnière de la série initiale.

    Ces techniques sont largement utilisées par les instituts de statistiques et de
    recherche économique. Elles permettent d’étudier
       - les indicateurs entre les différentes dates sans les effets introduits par la saisonnalité.
       - Ces instituts publient des séries temporelles "cvs" afin d’en faciliter les comparaisons.

    Les méthodes couramment employées pour désaisonnaliser une série temporelle sont
       - la régression linéaire et les filtres moyennes mobiles




      N. Laïb (CY-Tech)         Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                      3 / 67
~~~

## Page 4

~~~text
                       Ajustement Tendanciel.
           Estimation du trend en l’absence de saisonnalité




N. Laïb (CY-Tech)     Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                 méthode
                                                                                   janvier 2025
                                                                                           de régression linéaire
                                                                                                            4 / 67
~~~

## Page 5

~~~text
Modèle Additif

    Le modèle additif simple s’écrit :
                              Xt =          mt + st     +       ϵt
                                           | {z }              |{z}
                                     partie déterministe partie aléatoire

    où mt , st , et ϵt représentent respectivement : la Tendance, la Saisonnalité, et le
    Bruit.
         Tendance (mt ) : C’est une fonction décrite par un nombre fini de paramètres. Elle
         peut être une fonction linéaire du temps (a + bt) ou un polynôme en t.
         Saisonnalité (st ) : Si d est la période de st , alors st +d = st pour tout t. On suppose
         également que st ne contient pas de tendance, ce qui s’écrit :
                                                     d
                                                     X
                                                            st +j = 0.
                                                     j =1
         Autrement dit, toute la tendance est modélisée dans mt .
    Élimination des variations saisonnières : Pour simplifier l’analyse, on élimine les
    variations saisonnières et on considère la série :
                            Xt = mt + ϵt = β0 + β1 t + ϵt ,              t = 1, . . . , n.
     Les ϵt sont des variables aléatoires (gaussiennes) centrées et indépendantes
    identiquement distribuées (i.i.d.).
     N. Laïb (CY-Tech)         Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                     5 / 67
~~~

## Page 6

~~~text
Ajustement Tendanciel : Régression linéaire sur le temps (RGLT)

    Méthode des moindres carrés ordinaires (MCO). L’objectif est de déterminer la
    droite des moindres carrés y = β0 + β1 t qui ajuste au mieux le nuage de points
    (t , Xt ).
    Les estimations des paramètres β0 et β1 sont obtenues en minimisant la somme des
    carrés des écarts :
                                                   n
                                                         [Xt − (β0 + β1 t)]2 .
                                                   X
                               Q(β0 , β1 ) =
                                                  t =1
    Solutions des moindres carrés : Les estimations βb0 et βb1 sont données par :
                                        Pn
                                          t =1
                                                 (Xt − X )(t − t)         Cov (t , X )
                          β
                          b1     =           Pn                       =
                                                 t =1
                                                      (t − t)2             Var (t)
                          β
                          b0     =     X − βb1 t .                                                                  (1)

    Remarques :
        La moyenne de t est t = (n + 1)/2.
        Les expressions suivantes peuvent être utilisées :
                                                   1 X n               n2 − 1
                                      Var (t) =           t 2 − (t)2 =        ,
                                                   n t =1               12
                                                          1 X n
                                        Cov (t , X ) =           t · Xt − t · X .
                                                          n t =1
     N. Laïb (CY-Tech)         Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                     6 / 67
~~~

## Page 7

~~~text
Ajustement polynomial : RGLT

   Modèle polynomial : On considère le modèle suivant :

                  Xt = mt + ϵt = β0 + β1 t + β2 t 2 + . . . + βq t q + ϵt ,           t = 1, . . . , n .

   Choix de l’ordre q : Une analyse graphique permet souvent de suggérer une valeur
   pour q (généralement q = 1, 2 ou 3). Une fois q fixé, les coefficients
   β = (β0 , β1 , . . . , βq )′ sont estimés par (MCO), en minimisant la somme des carrés des
   résidus :
                                                          n
                                                               (Xt − mt )2 .
                                                          X
                                       β
                                       b = argminβ
                                                        t =1
   Formulation matricielle : Le modèle peut être exprimé en notation matricielle :
                                                                                     q
                                                                     t12
                                                      
                                   β0                   1      t1           ...    t1             ϵ1
                                                                                                
                    X1
                                                                                     q
                  X            β                1               t22                        ϵ 
                                                    
                   2            1                          t2           ...    t2           2
               X =
                   ..  ,     β=
                                  ..  ,       Z = .                                   ,    ϵ=
                                                                                                 .. 
                                                                                      
                                     
                                                    .          ..    ..            ..              
                   .            .               .           .     .    ...      .
                                                                                               .
                                   βq                                                q           ϵn
                   Xn                                   1      tn    tn2    ...    tn

   Le modèle : X = Z β + ϵ.


     N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                      7 / 67
~~~

## Page 8

~~~text
    Solution des (MCO) : Les estimations des coefficients β sont données par :

                    b = βb0 , βb1 , . . . , βbq ′ = argminβ ||X − Z β||2 = (Z ′ Z )−1 Z ′ X .
                    β
                       ¡                       ¢
                                                                       2

    Résidus estimés sont :

                                                b = X − Z (Z ′ Z )−1 Z ′ X .
                                ϵb := e = X − Z β

▷ Choix du degré du polynôme "q" :

    Observation du graphe : L’analyse graphique de la série permet d’estimer le degré
    "q", en fonction de la forme de la courbe observée.
    Compromis à réaliser : Le choix de "q" doit équilibrer deux objectifs :

        Obtenir des résidus qui fluctuent autour de 0 avec une amplitude minimale. (Cela
        nécessite d’augmenter le degré du polynôme.)

        Utiliser un polynôme avec le degré le plus faible possible, pour éviter un ajustement
        excessif ou une surmodélisation.

    Choix optimal : On sélectionne le degré minimal qui donne un ajustement
    satisfaisant. Il existe un degré à partir duquel augmenter davantage le degré du
    polynôme n’apporte pas d’amélioration significative.


     N. Laïb (CY-Tech)           Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                            méthode
                                                                                              janvier 2025
                                                                                                      de régression linéaire
                                                                                                                       8 / 67
~~~

## Page 9

~~~text
Ajustement tendanciel : Cas général (RGL-G)

Ajustement tendanciel : Cas général
    Objectif : Ajuster une série temporelle (Xt )1≤t ≤n à une tendance m(t) exprimée
    comme une combinaison linéaire de q fonctions linéairement indépendantes
    (exemples : polynômes, exponentielles, logarithmes, etc.).


    Le modèle s’écrit :
                                                q
                                                X
                          Xt = m(t) + ϵt =             βj fj (t) + ϵt ,   1 ≤ t ≤ n,                                  (2)
                                                j =0

     où ϵt représente les résidus d’ajustement.
    En notation matricielle, on a :
                                               X = Z β + ϵ,                                                           (3)
    où :
           X est le vecteur des observations (n composantes),
           ϵ est le vecteur des résidus (n composantes),
           β est le vecteur des paramètres à estimer (q + 1 composantes),
           Z est une matrice de taille n × (q + 1), dont les éléments sont définis par :
                                     Z = (zij )1≤i ≤n, 0≤j ≤q ,       où zij = fj (ti ).

      N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                            méthode
                                                                                              janvier 2025
                                                                                                      de régression linéaire
                                                                                                                       9 / 67
~~~

## Page 10

~~~text
Ajustement tendanciel : Cas général (RGL-G)

    L’estimateur des (MCO) βb est obtenu en minimisant la somme des carrés des
    résidus :
                               n                           n
                                      [Xt − m(t)]2 =          ϵ2    ′             ′
                               X                          X
                Rn (β)   =                                     t = ϵ ϵ = (X − Z β) (X − Z β).
                               t =1                      t =1

    Les équations normales (voir cours sur les modèles linéaires) sont données par :

                                                Z ′Z β = Z ′X .

    La solution unique est :
                                             b = (Z ′ Z )−1 Z ′ X .
                                             β
    Remarque :
        L’indépendance des fonctions fj implique que les q + 1 vecteurs colonnes de Z sont
        linéairement indépendants.
        Ainsi, Z est de rang q + 1, ce qui impose que le nombre d’observations n soit supérieur
        ou égal à q + 1.
        Dans ce cas, la matrice Z ′ Z est inversible.

    Exemple. Cas du modèle linéaire simple : Xt = at + b + ϵt ,                       1 ≤ t ≤ n,
    correspond à : q = 2, f1 (t) = 1, f2 (t) = t .
     N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                     10 / 67
~~~

## Page 11

~~~text
Ajustement tendanciel : Cas général (RGL-G) - Exemple : Modèle linéaire

Pour le modèle linéaire Xt = at + b + ϵt , on obtient :

                                                                                                       
                                                     µ                                ¶        1    1
                                                         1       ...          1            .       .. 
                                       Z ′Z   =                                            .
                                                                                           .        . 
                                                                                                       
                                                         1       ...          n
                                                                                               1    n
                                                                     P ¶
                                                         n             t
                                                     µ
                                              =          P           P 2
                                                           t              t
                                                         Ã                    !
                                                             1       t
                                              =      n                            ,
                                                             t       t2


où t = n1       t et t 2 = n1
                                P 2
                                 t .
            P


L’inverse de Z ′ Z est donné par :
                                                                                  Ã                     !
                                                                 1                        t2       −t
                                      (Z ′ Z )−1 =                                                          .
                                                     n(t 2 − (t)2 )                       −t       1


       N. Laïb (CY-Tech)                 Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                    méthode
                                                                                                      janvier 2025
                                                                                                              de régression linéaire
                                                                                                                              11 / 67
~~~

## Page 12

~~~text
Pour Z ′ X , on a :                                                       
                                          µ                    ¶     x1   µ P    ¶
                                              1    ...     1        .  = P xt .
                                                                    . 
                               Z ′X =                               . 
                                              1    ...     n                 txt
                                                                     xn

Ainsi, les estimateurs des moindres carrés sont :
                                                               Ã               !µ P
                                                   1               t2
                           µ         ¶                                                ¶
                                bb                                        −t        x
                                         =                                        P t .
                                ab           n(t 2 − (t)2 )        −t      1           txt


En explicitant :
                                     Pn
                                              txt − nt x                    nt 2 x − nt tx
                           ab = Pt =1                      ,           bb = P              .
                                         n t 2 − nt 2                         n t 2 − nt 2
                                         t =1                                 t =1




       N. Laïb (CY-Tech)                 Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                    méthode
                                                                                                      janvier 2025
                                                                                                              de régression linéaire
                                                                                                                              12 / 67
~~~

## Page 13

~~~text
                Détermination des coefficients saisonniers




N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                   méthode
                                                                                     janvier 2025
                                                                                             de régression linéaire
                                                                                                             13 / 67
~~~

## Page 14

~~~text
Détermination des coefficients saisonniers [1]

    La tendance mt est estimée par la méthode des MCO, et son estimation est notée
    bt .
    m
    On cherche maintenant à estimer les variations saisonnières St .
    Méthode : Le composant saisonnier St est estimé à partir d’une série (dt ) :
                                                        dt = Xt − m
                                                                  bt .

                                    On travaille ainsi sur la série (t , dt ).
    On identifie les données dt à l’aide de deux indices :
                   - i : représente l’année de l’observation.
                   - j : représente le mois ou la période correspondante. Cela peut être
                     un trimestre, un mois, ou un jour.

Exemple : Si les données s’étendent sur N années, avec p périodes (mois, trimestres,
etc.) par an :
    L’observation du j ème mois de la i ème année, notée di ,j , peut aussi s’écrire dt avec :
                                                      t = (i − 1) · p + j .
    Les indices prennent les valeurs suivantes :
                    - i : 1, 2, 3, . . . , N .
                    - j : 1, 2, 3, . . . , p .
                    - t : 1, 2, 3,Séries
     N. Laïb (CY-Tech)             . . . , Np  .
                                            temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                méthode
                                                                                                  janvier 2025
                                                                                                          de régression linéaire
                                                                                                                          14 / 67
~~~

## Page 15

~~~text
Détermination des coefficients saisonniers [2]

    Soit (Xt )1≤t ≤T une série temporelle.
    Les variations saisonnières se répètent identiquement à chaque période. Par
    conséquent :
      - On estime un coefficient saisonnier pour chaque mois, trimestre ou jour.
      - La variation saisonnière pour tous les mois j correspondra au coefficient saisonnier du
        mois j.
    Pour des données trimestrielles (période p = 4), nous obtenons :
      - 4 coefficients caractérisant la saisonnalité, notés :
                                                s j := c j ,   1 ≤ j ≤ 4.
      - Le coefficient du mois de janvier (ou du premier trimestre) est la moyenne de tous les
        mois de janvier dans la série dt .
      - Les coefficients sont calculés grâce à la formule suivante (modèle additif) :
                                           1        X
                                 cj =                  (Xt − m
                                                             b t ),         1 ≤ j ≤ 4.
                                        Card(Tj ) t ∈T
                                                           j

    Notations :
      - Xt représente les données brutes.
      - m
        b t est l’estimation de la tendance.
      - Tj est l’ensemble des temps associés au mois (ou trimestre) j.



     N. Laïb (CY-Tech)         Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    15 / 67
~~~

## Page 16

~~~text
Détermination des coefficients saisonniers [3]

    Exemple 1. Si T = 16, alors :
  - La saison j = 1 correspond au trimestre 1.
  - La saison j = 2 correspond au trimestre 5 = 1 + 4 (on ajoute une année pour retrouver
    la même saison).
  - Ainsi :
         T1 = {1, 5, 9, 13},     T2 = {2, 6, 10, 14},         T3 = {3, 7, 11, 15},         T4 = {4, 8, 12, 16}.

  - Les coefficients saisonniers cj pour un modèle additif sont calculés comme suit :
                                          1        X
                                cj =                  (Xt − m
                                                            b t ),            1 ≤ j ≤ p,
                                       Card(Tj ) t ∈T
                                                         j

    où p désigne la période (ici p = 4 pour des données trimestrielles).
  - Par exemple, pour la saison j = 2 (T2 = {2, 6, 10, 14}) :

                                    1       X
                  Sb2 = c2 =                   (Xt − m
                                                     bt )
                                Card(T2 ) t ∈T
                                                   2
                          1
                         = [(X2 − m
                                  b 2 ) + (X6 − m
                                                b 6 ) + (X10 − m
                                                               b 10 ) + (X14 − m
                                                                               b 14 )] .
                          4
     N. Laïb (CY-Tech)             Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                              méthode
                                                                                                janvier 2025
                                                                                                        de régression linéaire
                                                                                                                        16 / 67
~~~

## Page 17

~~~text
  Définition. La composante saisonnière provisoire estimée Sbt est définie par :

                                     Sbt = {cj , j ∈ Tj },      1 ≤ j ≤ p,

  où p désigne la période.
- Quel que soit l’année i (i = 1, . . . , N) :

                   Sbt = cj si t correspond au j ème trimestre d’une année i .

  Ceci peut aussi s’exprimer sous forme compacte :
                                            p
                                            X
                                    Sbt =          ck 1{trimestre=k } (t).
                                            k =1

  Enfin, nous avons Sij = Sj = cj , ce qui explicite que la composante saisonnière
  dépend uniquement du trimestre.




    N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    17 / 67
~~~

## Page 18

~~~text
Détermination des coefficients saisonniers [4]

    La composante saisonnière estimée Sbt est répétitive (périodique). Il suffit donc de
    calculer seulement les quatre premiers coefficients saisonniers.
    On obtient :
       - Pour 1 ≤ t ≤ 4, les quatre premiers coefficients saisonniers.
       - Ensuite, pour 5 ≤ t ≤ 8, les quatre coefficients saisonniers sont recopiés.
       - Et ainsi de suite.

    Calcul de Sb14 . En faisant la division euclidienne de 14 par 4, dont le reste est 2, on
    obtient :
                                             Sb14 = c2 .
    S12 = c4 , car le reste de la division euclidienne de 12 par 4 est 0. Le reste 0
    correspond à la saison 4.
    On peut utiliser la représentation à double indice de la série di ,j pour calculer sj :

                                1 X N
                   sj := cj =         (X − mb i ,j ),        1 ≤ j ≤ p,       t = (i − 1) × p + j .
                                N i =1 i ,j



     N. Laïb (CY-Tech)            Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                             méthode
                                                                                               janvier 2025
                                                                                                       de régression linéaire
                                                                                                                       18 / 67
~~~

## Page 19

~~~text
Calcul des coefficients saisonniers définitifs [5]

▷ Le principe de la conversion des aires :

               - Les moyennes annuelles de la série brute et de la série corrigée des
                 variations saisonnières (cvs) doivent être identiques.

▷ Dans le cas d’un schéma additif :

               - la somme des coefficients doit être nulle.

    Soit cj le j-ème coefficient provisoire, on calcule la somme de ces coefficients :
                               p
                               X
                          c=          cj   avec     p la période de la saisonnalité.
                               j =1

                     - Si c = 0, alors les cj sont les coefficients saisonniers définitifs.
                     - Si c ̸= 0, les coefficients saisonniers sont normés afin que leur somme
                       soit nulle. Les coefficients définitifs sont donnés par :

                                                                                   1 X p
                                                   cj∗ = cj − c       où     c=          c.
                                                                                   p j =1 j


      N. Laïb (CY-Tech)            Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                              méthode
                                                                                                janvier 2025
                                                                                                        de régression linéaire
                                                                                                                        19 / 67
~~~

## Page 20

~~~text
▷ Dans le cas d’un schéma multiplicatif : la moyenne des coefficients doit être égale à 1.

               - Soit Sj le j-ème coefficient provisoire, on calcule la somme des
                 coefficients :
                                                      1 Xp
                                                 c=        c.
                                                     p j =1 j

               - Les coefficients définitifs sont donnés par :
                                                                   cj
                                                           cj∗ =        .
                                                                    c




      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    20 / 67
~~~

## Page 21

~~~text
                    Détermination de la série corrigée




N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                   méthode
                                                                                     janvier 2025
                                                                                             de régression linéaire
                                                                                                             21 / 67
~~~

## Page 22

~~~text
Données corrigées des variations saisonnières Xcvs ,t à l’instant t

▷ La composante saisonnière estimée Sbt est remplacée par
                                     n               o
                              St∗ = cj∗ , j ∈ Tj ,          1 ≤ j ≤ p.



Définition 1
On appelle
    série désaisonnalisée ou série corrigée des variations saisonnières, notée série cvs ou
    Xcvs ,t ,
    la série chronologique Xt à laquelle on a enlevé les variations saisonnières.




      N. Laïb (CY-Tech)      Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                        méthode
                                                                                          janvier 2025
                                                                                                  de régression linéaire
                                                                                                                  22 / 67
~~~

## Page 23

~~~text
Données corrigées des variations saisonnières Xcvs ,t à l’instant t

    Modèle Additif. La série corrigée à l’instant t est

                 Xcvs ,t = Xt − St∗ ,    1≤t ≤T           ou encore         Xcvs ,(i ,j ) = Xij − cj∗ .


    Modèle Multiplicatif. La série corrigée à l’instant t est

                                         Xt                                          Xij
                             Xcvs ,t =           ou encore         Xcvs ,(i ,j ) =         .
                                         St∗                                         cj∗

        Si on retire les coefficients saisonniers de la série des observations, on reconstitue la
        série corrigée des variations saisonnières.
        Xcvs ,t représente l’évolution de la variable observée s’il n’y avait pas eu les
        mouvements saisonniers.




     N. Laïb (CY-Tech)           Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                            méthode
                                                                                              janvier 2025
                                                                                                      de régression linéaire
                                                                                                                      23 / 67
~~~

## Page 24

~~~text
Intérêt de la série Xcvs ,t à l’instant t : Exemple

□ La particularité de la série cvs est que les données de Xcvs ,t sont directement
comparables.
Exemple. Pour une série annuelle (p = 12) :

    on a enlevé l’effet des saisons et donc le caractère propre de chaque mois,
    cela permet par exemple comparer les données d’un mois de janvier et celle d’un
    mois de juillet.




           Figure – Évolution du trafic voyageur entre janvier 1963 et décembre 1966


      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    24 / 67
~~~

## Page 25

~~~text
Réajustement de la tendance sur la série Xcvs ,t

               On peut réévaluer la tendance par ajustement (moindres carrés sur
               Xcvs ,t ), afin d’avoir une meilleure estimation de la tendance.




         Figure – Évolution du trafic voyageur entre janvier 1963 et décembre 1966




    N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                        méthode
                                                                                          janvier 2025
                                                                                                  de régression linéaire
                                                                                                                  25 / 67
~~~

## Page 26

~~~text
Série ajustée et variations accidentelles

1. Série ajustée Xbt
     La série ajustée, notée Xbt , est obtenue en recomposant les deux composantes
     estimées :
       - la tendance, notée m  bt ,
       - et les variations saisonnières estimées Scvs ,t , selon le modèle choisi.

Recomposition selon le modèle

     Modèle additif :                    Xbt = m
                                               b t + Scvs ,t ,        ou encore         Xbij = m
                                                                                               b ij + Scvs ,j .
     Modèle multiplicatif :              Xbt = m
                                               b t × Scvs ,t ,        ou encore         Xbij = m
                                                                                               b ij × Scvs ,j .


Interprétation de Xbt :

               - L’évolution qu’aurait subi la grandeur observée,
               - si les variations saisonnières étaient parfaitement périodiques,
               - et en l’absence de variations accidentelles.



      N. Laïb (CY-Tech)         Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                     26 / 67
~~~

## Page 27

~~~text
Série ajustée et variations accidentelles

.
2. Variations accidentelles ou résiduelles ou résidus ϵbt .


           Modèle additif :      la différence entre la série Xt et sa série ajustée
                                 représente les variations accidentelles ou résiduelles :
                                 ϵbt = Xt − X
                                            bt
     Modèle multiplicatif :      le rapport entre la série Xt et sa série ajustée
                                 représente les variations accidentelles ou résiduelles :
                                      Xt
                                 ϵbt =
                                         Xbt




      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    27 / 67
~~~

## Page 28

~~~text
Décomposition d’une série chronologique Xt
Étapes de la décomposition :
  1 Tracer le graphe de (Xt ) et générer un graphique des courbes superposées.
  2 Estimer la tendance mt et la représenter graphiquement.
  3 Choisir le modèle de décomposition : additif ou multiplicatif.
  4 Estimer les variations saisonnières St .
  5 Calculer la série corrigée des variations saisonnières Xcvs ,t et la représenter
    graphiquement.
  6 Calculer la série ajustée Xbt .
  7 Estimer les variations accidentelles ϵbt .

Critère de validité :
      La décomposition est correcte lorsque la série ajustée, visualisée sur le graphique des
      courbes superposées, est proche de la série initiale Xt .




                Figure – Ajustement
       N. Laïb (CY-Tech)        Séries incorrect    et ajustement
                                       temporelles: Chapitre             correct par
                                                             II. Désaisonnalisation d’une
                                                                                      la14  série2025
                                                                                         méthode
                                                                                           janvier de régression linéaire
                                                                                                                   28 / 67
~~~

## Page 29

~~~text
Prévisions avec tendance ajustée

Principe des prévisions :

    Lorsque la tendance m  b t est ajustée et exprimée en fonction de t, il devient possible
    de réaliser des prévisions pour les périodes futures.
    Pour obtenir une prévision à une date T :
       - Calculer m
                  b T à partir de l’expression de la tendance en fonction de t.
       - Ajouter le coefficient saisonnier du mois en question à m
                                                                 b T , si le modèle est additif.
       - Multiplier m
                    b T par le coefficient saisonnier si le modèle est multiplicatif.

       - Cette démarche revient à prolonger le calcul de la série ajustée pour les périodes
         futures.


Formule de prévision :

    La prévision pour l’instant t + h est donnée par :
                                                p
                                             Xt +h = m
                                                     b t +h + cj

  - où cj = s(j) est le coefficient saisonnier associé à la période (t + h).


      N. Laïb (CY-Tech)         Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                     29 / 67
~~~

## Page 30

~~~text
Remarque :

              - Ces coefficients saisonniers c1 , c2 , . . . , cj reflètent le profil saisonnier
                moyen de la série.
              - En supposant que la saisonnalité se répète de manière identique, ils
                peuvent être utilisés pour prévoir les valeurs futures.
              - La prévision finale est obtenue en combinant les différentes composantes
                (tendance, saisonnalité, etc.).




     N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                     30 / 67
~~~

## Page 31

~~~text
Schéma de désaisonnalisation d’une série trimestrielle (p = 4)

Notations :
    (Xt )t =1,...,Np = (Xi ,j )1≤i ≤N , 1≤j ≤p : Série trimestrielle, où :
         t : Nombre de trimestres depuis la date initiale (0).
         i : Numéro de l’année.
         j : Numéro du trimestre dans l’année i.

Étapes du schéma :

                               Xt           ≃             mt      ⇒       Estimation par MCO
                                             ⇓
           Estimation de mt :        m
                                     b t = ab + bt
                                                b


Choix du modèle :

         Modèle Additif                                    Modèle Multiplicatif

         Méthode : Différence à la tendance                Méthode : Rapport à la tendance
                                                                Xt
         dt = Xt − m
                   bt                                      dt = m
                                                                b    t




      N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                            méthode
                                                                                              janvier 2025
                                                                                                      de régression linéaire
                                                                                                                      31 / 67
~~~

## Page 32

~~~text
Calcul des coefficients saisonniers provisoires :
                                            1        X
                                  cj =                  dt         avec 1 ≤ j ≤ p
                                         Card(Tj ) t ∈T
                                                          j



Normalisation des coefficients saisonniers :

            Additif : j cj = 0                                  Multiplicatif : j cj = p
                          P                                                           P
                                                                                                c
            Coefficients définitifs : cj∗ = cj − c              Coefficients définitifs : cj∗ = cj


Désaisonnalisation :

                              Additif : Xtcvs = Xt − St∗ ,         St∗ = {cj∗ | j ∈ Tj }

                                                          Xt
                          Multiplicatif : Xtcvs =             ,     St∗ = {cj∗ | j ∈ Tj }
                                                          St∗




      N. Laïb (CY-Tech)              Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                méthode
                                                                                                  janvier 2025
                                                                                                          de régression linéaire
                                                                                                                          32 / 67
~~~

## Page 33

~~~text
Tableau récapitulatif


         Dates (T = t)     Série (Xt )       m
                                             b t = ab + bt
                                                        b         dt = Xt − m
                                                                            bt            cj∗     Xscv ,t


                 ..             ..                   ..                    ..              ..         ..
                  .              .                    .                     .               .          .


Observations clés :

               - Élimination de la saisonnalité : Les données corrigées (Xscv ,t ) permettent
                 de supprimer les variations périodiques des données brutes (Xt ).
               - Indépendance saisonnière : L’évolution de Xscv ,t reflète la dynamique
                 propre de la série, en dehors de l’effet saisonnier.
               - Interprétation graphique : Lorsque Xscv ,t passe en dessous de la tendance
                 (mb t ), cela indique une baisse marquée, tandis qu’un dépassement traduit
                 une augmentation indépendante de la composante saisonnière.




      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    33 / 67
~~~

## Page 34

~~~text
                    Désaisonnalisation par régression linéaire
                     sur Variables Indicatrices (RL-Var Ind)


Cette méthode permet d’estimer simultanément la tendance et la saisonnalité.




      N. Laïb (CY-Tech)     Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                       méthode
                                                                                         janvier 2025
                                                                                                 de régression linéaire
                                                                                                                 34 / 67
~~~

## Page 35

~~~text
Variables Indicatrices

   Jusqu’à présent, nous avons supposé que chaque prédicteur (variable explicative)
   prend des valeurs numériques.
   Mais que se passe-t-il lorsqu’un
                           prédicteur est une variable catégorielle
   ne prenant que deux valeurs, comme "oui" et "non" ?
   Par exemple, dans le cadre de la prévision des ventes quotidiennes :
        On souhaite intégrer l’information sur le fait qu’un jour est férié ou non.
        Dans ce cas, le prédicteur prend la valeur "oui" pour un jour férié et "non" sinon.

   Cette situation peut être traitée dans les modèles de régression multiple en créant
   une variable muette :
        Une variable qui prend la valeur 1 pour "oui" et 0 pour "non".
        Cette variable est aussi appelée "variable indicatrice".

   Une variable indicatrice peut également être utilisée pour :
        Tenir compte d’une valeur aberrante dans les données, sans l’exclure complètement.
        Introduire des effets de saisonnalité, comme les trimestres ou les jours de la semaine.




     N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                         méthode
                                                                                           janvier 2025
                                                                                                   de régression linéaire
                                                                                                                   35 / 67
~~~

## Page 36

~~~text
Variables muettes saisonnières

▷ Supposons que nous prévoyons des données quotidiennes et que nous souhaitons
prendre en compte le jour de la semaine comme prédicteur.
On peut alors créer les variables indicatrices suivantes :

                                    d1,t d2,t d3,t d4,t d5,t d6,t
                            Lundi    1     0      0      0     0     0
                            Mardi    0     1      0      0     0     0
                          Mercredi   0     0      1      0     0     0
                            Jeudi    0     0      0      1     0     0
                          Vendredi   0     0      0      0     1     0
                           Samedi    0     0      0      0     0     1
                          Dimanche   0     0      0      0     0     0
                            Lundi    1     0      0      0     0     0
                                     ..     ..     ..    ..    ..     ..
                                      .      .      .     .     .      .
     Seules six variables fictives sont nécessaires pour coder sept catégories. La septième
     catégorie (dans ce cas, dimanche) est capturée par l’intercepte.




      N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                            méthode
                                                                                              janvier 2025
                                                                                                      de régression linéaire
                                                                                                                      36 / 67
~~~

## Page 37

~~~text
On utilise une variable muette de moins que les catégories.
              - Pour des données trimestrielles, trois variables muettes suffisent.
              - Pour des données quotidiennes, six variables fictives suffisent, et
                ainsi de suite.

Interprétation : Chaque coefficient des variables fictives mesure l’effet de sa
catégorie par rapport à la catégorie omise.
              - Par exemple, le coefficient de d1,t (lundi) mesure l’effet du lundi sur
                 la variable à prévoir par rapport à l’effet du dimanche.




 N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                    méthode
                                                                                      janvier 2025
                                                                                              de régression linéaire
                                                                                                              37 / 67
~~~

## Page 38

~~~text
Exemple : Production trimestrielle de bière en Australie




                        Figure – Production trimestrielle de bière australienne


▷ Modélisation :
    Ces données peuvent être modélisées à l’aide d’une régression avec tendance linéaire
    et variables muettes trimestrielles :
                         yt = β0 + β1 t + β2 d2,t + β3 d3,t + β4 d4,t + εt ,
où di ,t = 1 si t est dans le trimestre i, et 0 sinon.
▷ Nous voulons prévoir la valeur de la future production de bière.
    LaN.variable du premier trimestre
        Laïb (CY-Tech)                   a été Chapitre
                              Séries temporelles: omise,II. Désaisonnalisation par la14méthode
                                                                                        janvier 2025
                                                                                                de régression linéaire
                                                                                                                38 / 67
~~~

## Page 39

~~~text
   La fonction tslm() permet de gérer automatiquement cette situation en spécifiant
   la saison comme prédicteur.

fit.beer <- tslm(beer2 ~ trend + season)
summary(fit.beer)
#>
#> Call:
#> tslm(formula = beer2 ~ trend + season)
#>
#> Residuals:
#>    Min     1Q Median     3Q    Max
#> -42.90 -7.60 -0.46     7.99 21.79
#>
#> Coefficients:
#>             Estimate Std. Error t value Pr(>|t|)
#> (Intercept) 441.8004     3.7335 118.33 < 2e-16 ***
#> trend         -0.3403    0.0666   -5.11 2.7e-06 ***
#> season2     -34.6597     3.9683    -8.73 9.1e-13 ***
#> season3     -17.8216     4.0225    -4.43 3.4e-05 ***
#> season4       72.7964    4.0230   18.09 < 2e-16 ***
#> ---


     N. Laïb (CY-Tech)    Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                     méthode
                                                                                       janvier 2025
                                                                                               de régression linéaire
                                                                                                               39 / 67
~~~

## Page 40

~~~text
▷ Interprétation des coefficients estimés des variables fictives capturant la saisonnalité
trimestrielle de la production de bière en Australie. :

               - Une tendance moyenne à la baisse de -0,34 mégalitre par trimestre.
               - En moyenne :
                                - Le deuxième trimestre a une production de 34,7
                                  mégalitres inférieure à celle du premier trimestre.
                                - Le troisième trimestre a une production de 17,8
                                  mégalitres inférieure à celle du premier trimestre.
                                - Le quatrième trimestre a une production de 72,8
                                  mégalitres supérieure à celle du premier trimestre.




      N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                         méthode
                                                                                           janvier 2025
                                                                                                   de régression linéaire
                                                                                                                   40 / 67
~~~

## Page 41

~~~text
RL-Var Ind : Modèle Additif

Modèle Additif :
                                               Xt = mt + St + ϵt
▷ Hypothèses :

                   E(ϵt ) = 0,   Var(ϵt ) = σ2 ,                Cov(ϵt , ϵt −h ) = 0        ∀ h > 0.

▷ On suppose que mt et St sont des combinaisons linéaires de fonctions connues dans le
               j
temps, mti et St :
                                                                 q
                         mt = β1 mt1 + β2 mt2 + · · · + βq mt ,
                        (

                         St = c1 St1 + c2 St2 + · · · + cn Stn .

▷ Objectif : Estimer les coefficients β1 , . . . , βq et c1 , . . . , cn à partir des observations.
▷ On peut alors écrire le modèle :
                                   q                 n
                                                                j
                                          βi mti +
                                   X                 X
                            Xt =                            cj St + ϵt ,   t = 1, . . . , T .
                                   i =1              j =1




       N. Laïb (CY-Tech)            Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                               méthode
                                                                                                 janvier 2025
                                                                                                         de régression linéaire
                                                                                                                         41 / 67
~~~

## Page 42

~~~text
RL-Var Ind :données trimestrielles,

▷ La forme de St dépend du type de données et de la forme de la saisonnalité.

    Pour des données trimestrielles, St peut être représentée par une fonction périodique
    de période p = 4.
    Cette composante prend quatre valeurs (ou coefficients saisonniers) : c1 , c2 , c3 , c4 ,
    associées à chacun des trimestres.
    St = cj , si la date t correspond au trimestre j.
    Le modèle peut être écrit sous la forme :

                                          St = c1 St1 + c2 St2 + c3 St3 + c4 St4 ,
              j
     où St est une fonction indicatrice du trimestre j.
                  j
              St prend la valeur 1 si t correspond au trimestre j (ou t est congru à j modulo p).
                  j
              St prend la valeur 0 sinon.

                                    j
Les fonctions indicatrices St sont définies comme suit :
          j                                                     j
    (                                                     (
        St = 1        si t = trimestre j ,                    St = 1       si t ≡ j [modulo p],
         j                                        ou           j                                 = 1{j [p ]} (t).
        St = 0        si t ̸= trimestre j .                   St = 0       si t ̸≡ j [modulo p].

        N. Laïb (CY-Tech)               Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                   méthode
                                                                                                     janvier 2025
                                                                                                             de régression linéaire
                                                                                                                             42 / 67
~~~

## Page 43

~~~text
                Modèle trimestriel de Buys-Ballon (1847)




N. Laïb (CY-Tech)      Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                  méthode
                                                                                    janvier 2025
                                                                                            de régression linéaire
                                                                                                            43 / 67
~~~

## Page 44

~~~text
RL-Var Ind : Modèle trimestriel de Buys-Ballot

▷ Dans le cas où la tendance est linéaire et les données sont trimestrielles, en posant
mt1 = 1 et mt2 = t, le modèle s’écrit :

                     Xt =     β + β t + c1 St1 + c2 St2 + c3 St3 + c4 St4 +ϵt ,
                              | 1 {z 2 }   |            {z              }
                            Tendance (mt )     Saisonnalité (St )
où
                                           Xt = mt + St + ϵt .

▷ Application aux données SNCF
- On suppose que les données commencent au 1er trimestre.

     Au premier trimestre de 1963 : 1750 + 1560 + 1820 + 2090 = 5130,
     Au deuxième trimestre : 6410, etc.

Ainsi, le modèle peut être utilisé pour estimer les composantes de la tendance et de la
saisonnalité.




      N. Laïb (CY-Tech)           Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                             méthode
                                                                                               janvier 2025
                                                                                                       de régression linéaire
                                                                                                                       44 / 67
~~~

## Page 45

~~~text
RL-Var Ind : Modèle de Buys-Ballot. Application aux données SNCF


            5130                                                                        ϵ
                                                                                                     
                   
                     1         1      1         0     0       0
                                                                              1
           6410                                                           ϵ2                       
           8080   1         2      0         1     0       0 
                                                                                                  
                                                                           ϵ3
                                                                                                    
           5900   1         3      0         0     1       0   β
                                                                                                  
                                                                            ϵ
                                                                       1
                                                                                                      
                   1         4      0         0     0       1   β   4
                                                                                                  
           5110                                                  2   ϵ5
                                                                                                     
                   1         5      1         0     0       0  c  
                                                                                                      
           6680                                                  1   ϵ6
                                                                                                     
                 =                                                     +                        où
           8350   1         6      0         1     0       0 
                                                                                                      
                                                                    c2   ϵ
                                                                   
                                                                           7
                                                                                                      
           5910   1         7      0         0     1       0 
                                                                                                  
                                                                    c3   ϵ
                                                                            8
                                                                                                      
                  1         8      0         0     0       1  c
                                                                                                     
           5080   .                                                 4    ϵ9
                                                                                                  
                               ..     ..        ..    ..      ..                                     
                   ..
              ..                                                           ..
                                                                                                  
                               .      .         .     .       .                                     
               .                                                           .
                                     St1       St2   St3        4
                                                                                                     
                     1         t                             St
             Xt                                                                         ϵt

                                           ⇒         X = Dδ + ϵ

   X est le vecteur des observations (Xt ) ;
   D est la matrice des variables explicatives : la constante (1), la tendance (t), et les
   indicatrices de saisonnalité (St1 , St2 , St3 , St4 ) ;
   δ = (β1 , β2 , c1 , c2 , c3 , c4 )⊤ est le vecteur des paramètres ;
   ϵ est le vecteur des résidus (ϵt ).
     N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                     45 / 67
~~~

## Page 46

~~~text
RL-Var Ind : Modèle de Buys-Ballot. Application aux données SNCF

▷ Avec les définitions suivantes :
                          D = [m | S]       et        δ⊤ = [β1 , β2 | c1 , c2 , c3 , c4 ],

où
     m est la matrice des composantes liées à la tendance (mt1 , mt2 ) ;
     S est la matrice des composantes saisonnières (St1 , . . . , St4 ).
                                                               
                                                 1          1
                                                1          2 
                                                              
                                                1          3 
                m = [mti ]i =1,2; t =1,...,T = 
                                                .
                                                               ,      où mt1 = 1 et mt2 = t .
                                                .          .. 
                                                               
                                                .           . 
                                                 1          T

                                                         S1          S12      S13     S14
                                                                                            
                                                        11
                                                        S2          S22      S23     S24 
                                                                                          
                                                        1
                                                                     S32      S33     S34 
                                                                                          
                           j
                     S = [St ]j =1,...,4; t =1,...,T =  S3                               .
                                                       
                                                        .            ..       ..      .. 
                                                        .
                                                        .             .        .       . 
                                                                                          

                                                         S1   T
                                                                     ST2      ST3     ST4

      N. Laïb (CY-Tech)            Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                              méthode
                                                                                                janvier 2025
                                                                                                        de régression linéaire
                                                                                                                        46 / 67
~~~

## Page 47

~~~text
▷ Le modèle devient :
                                                X = D δ + ϵ,
où

     X est le vecteur des observations (Xt , pour t = 1, . . . , T ) ;
     δ = (β1 , β2 , c1 , c2 , c3 , c4 )⊤ est le vecteur des paramètres ;
     ϵ est le vecteur des résidus (ϵt , pour t = 1, . . . , T ).




      N. Laïb (CY-Tech)           Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                             méthode
                                                                                               janvier 2025
                                                                                                       de régression linéaire
                                                                                                                       47 / 67
~~~

## Page 48

~~~text
RL-Var Ind : Modèle trimestriel de Buys-Ballot. Identification du modèle

▷ L’estimateur des moindres carrés pour le vecteur δ est : δb = (D ′ D)−1 D ′ X ,
sous réserve que la matrice D ′ D soit inversible.

▷ **Problème d’inversibilité** : La matrice D ′ D n’est pas inversible car la première
colonne est égale à la somme des quatre dernières (composantes saisonnières).

▷ **Méthodes pour identifier le modèle** :
(a) Exclure la constante β1 : Le modèle devient :

                              Xt = β2 t + c1 St1 + c2 St2 + c3 St3 + c4 St4 + ϵt .

(b) Inclure une contrainte sur les composantes saisonnières : Ajouter la contrainte
c1 + c2 + c3 + c4 = 0 :

                          Xt = β1 + β2 t + c1 St1 + c2 St2 + c3 St3 + c4 St4 + ϵt ,
                          (

                               avec la contrainte c1 + c2 + c3 + c4 = 0.

▷ Remarque : La contrainte sur les coefficients saisonniers est arbitraire, mais fournit une
interprétation cohérente des composantes saisonnières.
      N. Laïb (CY-Tech)              Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                méthode
                                                                                                  janvier 2025
                                                                                                          de régression linéaire
                                                                                                                          48 / 67
~~~

## Page 49

~~~text
RL-Var Ind : Estimateur des moindres carrés ordinaires (m.c.o.)- Cas général

▷ Considérons le modèle général suivant
                                      q                n
                                                                   j
                                            βi mti +
                                      X                X
                              Xt =                             cj St + ϵ t ,   t = 1, . . . , T .
                                     i =1              j =1


▷ Nous cherchons les paramètres βi et cj qui minimisent la somme des carrés des erreurs
                                                                                 )2 
                                                            q
                           "         #              (
                              T                 T                        n
                              X    2            X          X       i    X       j
            β, cb = argmin        ϵt = argmin                  βi mt −
           ¡     ¢
             b                                      Xt −                   cj St  .
                             t =1              t =1       i =1         j =1

▷ Écriture matricielle. Soit
                                                                                 h     i
                β = (β1 , . . . , βq )′ ,    c = (c1 , . . . , cn )′ ,     m = mti                           ,
                                                                                           1≤i ≤q , 1≤t ≤T
                                                       j
                                                   h       i
                                             S = St                             .
                                                               1≤j ≤n, 1≤t ≤T

▷ En regroupant les composantes linéaires et saisonnières dans une matrice D, le modèle
peut s’écrire
                      X = D δ + ϵ, avec D = [m|S] et δ′ = [β′ , c ′ ].

      N. Laïb (CY-Tech)                Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                  méthode
                                                                                                    janvier 2025
                                                                                                            de régression linéaire
                                                                                                                            49 / 67
~~~

## Page 50

~~~text
RL-Var Ind : Estimateur des (m.c.o.) - Cas général

▷ Le modèle peut s’écrire sous forme matricielle

                                                               β
                                                              · ¸
                           X = mβ + Sc + ϵ = [m | S]                  + ϵ = D δ + ϵ,
                                                                 c

            β
           · ¸
avec δ =       .
           c
                                                  β
                                                 · ¸
                                                   b
▷ L’estimateur des moindres carrés δb =              satisfait l’équation normale suivante :
                                                  cb
                                                                 · ′¸          · ′¸
                                                                  m             m
                          D ′ D δb = D ′ X     ⇒       [m | S]          δb =          X.
                                                                     S′         S′

▷ En explicitant la solution, on obtient
                                     · ¸ · ′                     ¸−1 · ′ ¸
                                      βb   mm             m′ S        mX
                                δb =     =                                       .
                                      cb   S ′m           S ′S           S ′X


▷ Cas particulier : Si aucun effet saisonnier n’est présent (S = 0), alors X = mβ + ϵ, et on
retrouve le modèle linéaire usuel.
      N. Laïb (CY-Tech)           Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                             méthode
                                                                                               janvier 2025
                                                                                                       de régression linéaire
                                                                                                                       50 / 67
~~~

## Page 51

~~~text
RL-Var Ind - Cas particulier : le modèle trimestriel de Buys-Ballot

▷ Le modèle trimestriel de Buys-Ballot est défini par :

                                 Xt = β1 + β2 t + c1 St1 + c2 St2 + c3 St3 + c4 St4 ,
     j
où St (j = 1, . . . , 4) représentent les composantes saisonnières.
▷ On cherche à résoudre le problème de minimisation suivant :

                                                                                         j 2
                             (                      h                                      i
                                  minβ,c T      Xt − β1 − β2 t − 4j =1 cj St ,
                                            P                               P
                                           t =1
                                  sous la contrainte c1 + c2 + c3 + c4 = 0.

                                                j
▷ En utilisant la propriété 4j =1 St = 1 pour tout t, ce problème peut être réécrit comme
                                     P

suit :
                                                             j 2
                      
                                  PT h             P4         i
                       minβ2 ,τj t =1 Xt − β2 t − j =1 τj St ,
                      
                      
                      
                             
                             
                                                                   τ +τ +τ +τ
                                                              β1 = 1 2 4 3 4 ,
                             
                             
                              avec les relations
                                                                   cj = τj − β1
                             
                                                                                       ∀j .
                                                             

▷ Ces relations permettent de reformuler le problème en fonction des τj , simplifiant ainsi
l’identification des paramètres.
         N. Laïb (CY-Tech)               Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                                    méthode
                                                                                                      janvier 2025
                                                                                                              de régression linéaire
                                                                                                                              51 / 67
~~~

## Page 52

~~~text
RL-Var Ind- Cas particulier : le modèle trimestriel de Buys-Ballot

▷ Le système précédent montre que les estimateurs βb1 , βb2 , et cbj (j = 1, . . . , 4) peuvent
être calculés à l’aide d’une démarche en deux étapes.


▷ Étape 1. Chercher βb2 et τbj (j = 1, . . . , 4) en minimisant :
                                                                                    #2
                                                                    4
                                                  "
                                            T
                                            X                       X           j
                                                      Xt − β2 t −          τ j St
                                           t =1                     j =1
C’est-à-dire effectuer une régression de Xt sur les variables suivantes :
                                                t , St1 , St2 , St3 , St4 .
Cela correspond à une régression par les moindres carrés ordinaires (m.c.o.) sans
contrainte.


▷ Étape 2. Calculer ensuite βb1 et cbj (j = 1, . . . , 4) à l’aide des relations :
                                         1 P4
                                    β1 = 4 j =1 τbj ,
                                    b

                                    cb = τb − 1 P4 τb ,
                                   
                                                                        ∀j = 1, . . . , 4.
                                       j    j 4 j =1 j



▷ Cette approche
     N. Laïb        sépare l’estimation
             (CY-Tech)                     en deux
                                Séries temporelles:     étapes
                                                    Chapitre       claires : la régression
                                                             II. Désaisonnalisation par la14 janvierinitiale
                                                                                           méthode   2025      pour
                                                                                                     de régression linéaire
                                                                                                                     52 / 67
~~~

## Page 53

~~~text
RL-Var Ind - Cas particulier : le modèle trimestriel de Buys-Ballot

▷ Calcul de βb2 et τbj

  - Notons N le nombre d’années complètes, défini par N = T /4, où T est le nombre
    total d’observations.
  - Désignons par i le numéro de l’année, avec i = 1, . . . , N.
  - L’indice t correspond à l’observation Xt associée au j-ième trimestre (j = 1, . . . , 4) de
    la i-ième année (i = 1, . . . , N). L’indice t est donné par :
                                              t = 4(i − 1) + j .

  - xei : la moyenne des observations Xt pour les quatre trimestres de l’année i, définie
    par :
                                           1X  4
                                     xei =       X          .
                                           4 j =1 4(i −1)+j

  - x j : la moyenne des Xt pour tous les trimestres j (j = 1, . . . , 4) sur l’ensemble des
    années N, donnée par :
                                         1 X N
                                    xj =       X          .
                                         N i =1 4(i −1)+j
      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    53 / 67
~~~

## Page 54

~~~text
  - x : la moyenne globale de toutes les observations Xt , définie comme suit :

                                      1 XT        1 X N      1X4
                                x=           Xt =       xe =     x .
                                      T t =1      N i =1 i 4 j =1 j


▷ Ces définitions permettent de structurer le calcul des coefficients βb2 et τbj à partir des
moyennes par trimestre et par année.




      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    54 / 67
~~~

## Page 55

~~~text
- Cas particulier : le modèle trimestriel de Buys-Ballot

▷ On obtient

                                           PN          N (N +1)
                                                i xe −          x
                                     b2 = 3 i =1 i
                                     β
                                                          2
                                                      2
                                                N(N − 1)


                           τ
                           bj = x j − [j + 2(N − 1)]βb2        pour        j = 1, 2, 3, 4


▷ Et
                                                  h             i
                                    1P     τb = x − 5
                             βb1 = 4 4
                            
                                      j =1 j        2 + 2(N − 1) β2
                                                                   b

                                                                       ³       ´
                                   cbj = τbj − βb1 = x j − x − βb2 j − 52
                            
                            
                            




       N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                             méthode
                                                                                               janvier 2025
                                                                                                       de régression linéaire
                                                                                                                       55 / 67
~~~

## Page 56

~~~text
Explications

▷ Dans le calcul de βb2 :
                N (N +1)
  - Le terme    2    correspond à la somme des indices temporels t sur l’ensemble des
    N années (en supposant que les indices des années sont 1, 2, . . . , N).
  - Le dénominateur N(N 2 − 1) est une constante calculée à partir des indices temporels
    et garantit que le modèle est bien identifié.

▷ Dans le Calcul des τbj (coefficients trimestriels)

  - x j est la moyenne des Xt pour le trimestre j sur toutes les années.
  - Le terme [j + 2(N − 1)] correspond à l’effet du temps cumulé au trimestre j en
    fonction du nombre total d’années N.
  - En soustrayant cet effet temporel pondéré par βb2 , on isole l’effet saisonnier
    spécifique à chaque trimestre.




      N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                         méthode
                                                                                           janvier 2025
                                                                                                   de régression linéaire
                                                                                                                   56 / 67
~~~

## Page 57

~~~text
Explications

▷ Dans le Calcul de βb1 et cbj

  - βb1 est obtenu comme la moyenne des τbj . Cela reflète la valeur moyenne des
    coefficients trimestriels
                       h
                              sur l’ensemble
                                      i
                                             des trimestres.
  - Le second terme, 52 + 2(N − 1) βb2 , ajuste cette moyenne pour prendre en compte
    l’effet temporel global.
  - cbj est le coefficient centré pour chaque trimestre j, obtenu en soustrayant βb1 de τbj .
    Cette étape garantit que la contrainte 4j =1 cj = 0 est respectée.
                                             P

  - Le terme βb2 (j − 25 ) représente une correction pour l’effet temporel relatif à chaque
    trimestre.


▷ Résumé : Cette démarche en trois étapes permet de séparer les effets linéaires (β1 , β2 )
et saisonniers (cj ) tout en respectant les contraintes du modèle.




      N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                         méthode
                                                                                           janvier 2025
                                                                                                   de régression linéaire
                                                                                                                   57 / 67
~~~

## Page 58

~~~text
RVI- Généralisation des formules de Buys-Ballot (tendance linéaire)

▷ Les relations précédentes peuvent être généralises dans le cas d’une périodicité p. Le
modèle s’écrit alors

                                                                                            p
                 Xt = β1 + β2 t + c1 St1 + c2 St2 + c3 St3 + c4 St4 + . . . + cp St + ϵt ,

▷ On veut résoudre le problème de minimisation suivante :

                                                                                    j 2
                    (                         h                         Pp           i
                              minβ,c T      Xt − β1 − β2 t − j =1 cj St
                                      P
                                       t =1
                          sous la contreante c1 + c2 + c3 + c4 + . . . + cp = 0
▷ On obtient :

                                                  PN                N (N +1)
                                            12     i =1
                                                          i xei −2             x
                                    β
                                    b2 =
                                            p           N(N 2 − 1)
                                                           Np + 1
                                            β
                                            b1 = x − βb2
                                                              2
                                                                p +1
                                       cbj = xej − x − βb2 [j −      ]
                                                                  2
      N. Laïb (CY-Tech)            Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                              méthode
                                                                                                janvier 2025
                                                                                                        de régression linéaire
                                                                                                                        58 / 67
~~~

## Page 59

~~~text
                    RVI- Série Corrigée et prévision




N. Laïb (CY-Tech)     Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                 méthode
                                                                                   janvier 2025
                                                                                           de régression linéaire
                                                                                                           59 / 67
~~~

## Page 60

~~~text
La série corrigé des variations saisonnières Xt ,cvs peut être estimée par :
                                                                  q
                                                                  X              j
                               Xbt ,cvs = Xt − Sbt = Xt −                  cbj St
                                                                  j =1


Prévision. Les estimateurs βbi , cbj peuvent servir à prévoir une valeur de X non encore
observée : XT +h , h > 1.
Si on suppose que le modèle est encore vrai à l’instant T + h, on a :
                                     q                   n
                                     X         i         X             j
                          XT +h =          βi mT +h +           cj ST +h + ϵT +h
                                    i =1                 j =1

avec

         E(ϵT +h ) = 0,    V (ϵT +h ) = σ2 ,           Cov (ϵT +h , ϵT ) = 0,           t = 1, . . . , T .

La valeur XT +h peut être approchée par
                                           q                    n
                                           X
                                                  bi mi
                                                                X            j
                             XbT +h =             β   T +h +           cbj ST +h .
                                         ′ i =1                 j =1



 N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                       méthode
                                                                                         janvier 2025
                                                                                                 de régression linéaire
                                                                                                                 60 / 67
~~~

## Page 61

~~~text
Application au trafic voyageur-SNCF : Série agrégée par trimestre
▷ Considérons la série (xi ,j ) du trafic SNCF agrégée par trimestre en ligne les années,
 i \j   1        2           3          4    xei = x ij
   1  5130     6410      8080        5900      6380
   2  5110     6680      8350        5910      6513
   3  5080     6820      8190        5990      6520
   4  5310     6600      8090        6020      6505
   5  5320     6800      7650        6110      6470
   6  5486     6738      7258        6111      6398
   7  5629     6696      7491        6494      6578
   8  5682     7359      7836        6583      6865
   9  5963     6743      7844        6692      6811
                                                        et en colonne les trimestres,
 10 6270       7524      7997        6853      7161
 11 6472       7871      8188        7207      7435
 12 6892       8236      8978        7561      7917
 13 7505       9005      9591        8608      8677
 14 8139       9212      9522        8816      8922
 15 8088       9494      9583        9204      9092
 16 8983       9986      9907        9457      9583
 17 8829 10340 10070                 9669      9727
 18 9009 10265 10236 10458                     9992
  xj  6605     7932      8603        7425      7641
      N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                         méthode
                                                                                           janvier 2025
                                                                                                   de régression linéaire
                                                                                                                   61 / 67
~~~

## Page 62

~~~text
Application au trafic voyageur-SNCF : Série agrégée par trimestre




N. Laïb (CY-Tech)   Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                               méthode
                                                                                 janvier 2025
                                                                                         de régression linéaire
                                                                                                         62 / 67
~~~

## Page 63

~~~text
Application au trafic voyageur-SNCF : Modèle avec saisonnalité et tendance

▷ Considérons un modèle de la forme :

                      Xt   =   β1 + β2 t + c1 St1 + c2 St2 + c3 St3 + c4 St4 + ϵt
                               avec la contrainte : c1 + c2 + c3 + c4 = 0.                                          (4)

    Modèle avec une saisonnalité en 4 composantes,
    Les données sont trimestrielles, chaque composante correspondant à un trimestre.
    La tendance est supposée linéaire :

                                              mt = β1 + β2 t .

▷ Les paramètres sont estimés en deux étapes :

 (i) Estimation du modèle (4) sans contrainte et sans constante β1 ,
     en utilisant les expressions des estimateurs données à l’étape 1 du modèle de
     Buys-Ballot.
(ii) Reconstruction du modèle complet (4), avec contrainte et constante,
     en appliquant les relations de l’étape 2 du modèle de Buys-Ballot.

      N. Laïb (CY-Tech)        Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                          méthode
                                                                                            janvier 2025
                                                                                                    de régression linéaire
                                                                                                                    63 / 67
~~~

## Page 64

~~~text
Application : Série agrégée par trimestre- Calcul direct des estimateurs




                   Figure – xen = xei = x i ,j ( en utilisant les notaions du cours)


     N. Laïb (CY-Tech)          Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                           méthode
                                                                                             janvier 2025
                                                                                                     de régression linéaire
                                                                                                                     64 / 67
~~~

## Page 65

~~~text
Application : Série agrégée par trimestre - Calcul direct des estimateurs

▷ Pour chaque année (i) et chaque trimestre (j), il est possible de calculer des
moyennes afin d’obtenir des estimations des paramètres du modèle.

  - La moyenne annuelle pour 1963 (i = 1) est de 6380, et celle pour 1973 (i = 11) est
    de 7435.
  - De manière similaire, la moyenne du premier trimestre est de 6605, et celle du
    troisième trimestre est de 8603.
  - La moyenne totale des observations est de 7641, calculée sur un ensemble de 72
    observations (Ntotal = 18 × 4).
  - Le nombre total d’années observées est N = 18.
  - La pente de la droite de tendance, βb2 , est calculée à partir des moyennes annuelles
    comme suit :

                                               "                              #
                                    3      XN          N(N + 1)
                          β
                          b2 =                 i xei −          x ,
                                    2
                                 N(N − 1) i =1            2
où xei est la moyenne annuelle pour l’année i, et x est la moyenne totale.


      N. Laïb (CY-Tech)       Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                         méthode
                                                                                           janvier 2025
                                                                                                   de régression linéaire
                                                                                                                   65 / 67
~~~

## Page 66

~~~text
En remplaçant par les valeurs correspondantes :
                                     3
                          β
                          b2 =               [1419019 − 1306678] ≃ 57.97.
                                 18(182 − 1)


▷ Ce calcul utilise les moyennes par année et par trimestre présentées dans le tableau
précédent. Les relations de base des modèles de Buys-Ballot permettent ensuite de
compléter l’estimation des paramètres restants.




      N. Laïb (CY-Tech)            Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                              méthode
                                                                                                janvier 2025
                                                                                                        de régression linéaire
                                                                                                                        66 / 67
~~~

## Page 67

~~~text
Application : Série agrégée par trimestre- Calcul direct des estimateurs


                                                τ                   6605 − 35 × 57.97 ≃ 4577
                                              
                                               b1 =
                                                τ
                                              
                                              
                                                b2 =                7932 − 36 × 57.97 ≃ 5845
              bj = x j − [j + 2(N − 1)]βb2 =⇒
              τ
                                                τ
                                                b =                 8603 − 37 × 57.97 ≃ 6459
                                               3
                                              
                                              
                                                τ
                                                b4 =                7425 − 38 × 57.97 ≃ 5222

▷ Calcul de β1 et cj :

                                                          cb1          = 4577 − 5526 ≃ −949
                                                        
               βb1       =1       τ
              
                                   bj ≃ 5526
                               P                        
                           4
                                                        
                                                          cb2          = 5845 − 5526 ≃ +320
                                                        
                                                     =⇒
                                                          cb           = 6459 − 5526 ≃ +933
                              = τbj − βb1                3
                                                       
                   cbj                                  
                                                          cb1          = 5222 − 5526 ≃ −304

Le modèle s’écrit donc

                         Xt = 5526 + 58t − 949St1 + 320St2 + 933St3 − 304St4




      N. Laïb (CY-Tech)             Séries temporelles: Chapitre II. Désaisonnalisation par la14
                                                                                               méthode
                                                                                                 janvier 2025
                                                                                                         de régression linéaire
                                                                                                                         67 / 67
~~~
