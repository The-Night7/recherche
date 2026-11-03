# CM4-Algebre-de-Boole_2023-2024_Informatique1_P1S1_EAnsermin-RGrignon.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1xpKVMhC8xLML695gT7R2HRJ2s9fbGU-G) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                         v1.1




INFORMATIQUE 1
III. ALGEBRE DE BOOLE




                        Eva Ansermin & Romuald Grignon
~~~

## Page 2

~~~text
Algèbre de Boole : introduction
➢ Nous avons vu que les ordinateurs ne peuvent manipuler que
  des 0 et des 1.


➢ Comment parviennent-ils à effectuer des opérations ?


➢ Les opérations effectuées « électroniquement » dans un
  ordinateur sont basées sur l’algèbre de Boole.               George BOOLE
                                                                (1815-1864)

➢ L’algèbre de Boole est une approche algébrique de la
  logique.
                                                                                              2
                                                                   Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 3

~~~text
Algèbre de Boole : Variables
➢ L’algèbre de Boole permet de modéliser des raisonnements
  logiques.

➢ Elle manipule des données qui ne peuvent prendre que 2 valeurs:
   ➢ VRAI
   ➢ FAUX
   Ce sont des variables logiques ou booléennes

➢ L’algèbre de Boole est donc exploité pour faire des opérations par
                                                                       George BOOLE
  l’ordinateur. On aura :
                                                                        (1815-1864)
    ➢ VRAI ≈ 0
    ➢ FAUX ≈ 1

➢ On peut construire des fonctions dépendant d’une ou plusieurs
  variables logiques : ce sont des fonctions logiques                                                 3
                                                                           Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 4

~~~text
Algèbre de Boole : Fonctions logiques
➢ Les fonctions logiques permettent d’exprimer une sortie logique en fonction
  d’entrées logiques.
➢ Les fonctions logiques peuvent se représenter sous plusieurs formes :




                𝑒1       𝑒2   …             𝑒𝑛      𝑠
            0        0        …         0
            0        0        …         1
            …        …        …         …
            1        1        ….        0
            1        1        ….        1                                                           4
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 5

~~~text
Algèbre de Boole : Table de vérité
 ➢ Une table de vérité est un tableau indiquant la sortie d’une fonction logique selon
   toutes les combinaisons possibles d’entrées.

                                  Entrées logiques
                                                               sortie

                   𝑒1        𝑒2          𝑒3      …        𝑒𝑛       𝑠
               0         0           0           …    0        0
               0         0           0           …    1        1
Combinaison                                                               Sortie associée
               …         …           …           …    …
d’entrées
               1         1           1           ….   0        1
               1         1           1           ….   1        0




                                                                                                       5
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 6

~~~text
Algèbre de Boole : Table de vérité
➢ Exemple avec 2 entrées

                           𝑒1       𝑒2       𝑠
                       0        0
                       0        1
                       1        0
                       1        1




➢ Pour ne pas oublier de lignes, on peut compter en binaire.


➢ Pour n entrées, il y a 2𝑛 combinaisons différentes d’entrées, soit 2𝑛 lignes dans la
  table de vérité.
                                                                                                       6
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 7

~~~text
Algèbre de Boole : Opérateurs de base
➢ L’inversion NON/NOT : la sortie vaut 1 si l’entrée vaut 0 et inversement. La sortie est
  le complément de l’entrée.




          𝑎      𝑠 = 𝑎ത
      0          1
      1          0

                                                                                                       7
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 8

~~~text
Algèbre de Boole : Opérateurs de base
➢ Le ET/AND: La sortie vaut 1 si TOUTES les entrées valent 1
            (la sortie vaut 0 si AU MOINS une entrée vaut 0)




    𝑎        𝑏    𝑠 = 𝑎. 𝑏
0        0        0
0        1        0
1        0        0
1        1        1



                                                                                          8
                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 9

~~~text
Algèbre de Boole : Opérateurs de base
➢ Le OU/OR : La sortie vaut 1 si AU MOINS une entrée vaut 1
            (la sortie vaut 0 si TOUTES les entrées valent 0)




    𝑎        𝑏      𝑠 =𝑎+𝑏
0        0          0
0        1          1
1        0          1
1        1          1



                                                                                           9
                                                                Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 10

~~~text
Algèbre de Boole : Opérateurs de base
➢ Le XOR/OU EXCLUSIF: La sortie vaut 1 si UNE SEULE entrée vaut 1




                                  a
    𝑎        𝑏    𝑠 = a⨁𝑏                            s
                                  b
0        0        0
0        1        1
1        0        1
1        1        0


                                                                                             10
                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 11

~~~text
Algèbre de Boole : Opérateurs de base
➢ On peut associer le NON à d’autre portes pour obtenir la fonction complémentaire :
➢ Exemple: le NON-ET/NAND




     𝑎       𝑏   𝑠 = 𝑎. 𝑏
 0       0       1
 0       1       1
 1       0       1
 1       1       0



                                                                                                 11
                                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 12

~~~text
Algèbre de Boole : Implémentation physique
➢ Les circuits électroniques peuvent reproduire ces opérateurs!
➢ Les transistors sont la base de cette implémentation.




                                                                                           12
                                                                  Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 13

~~~text
Algèbre de Boole : Implémentation physique
➢ Les circuits électroniques peuvent reproduire ces opérateurs!
➢ Les transistors sont la base de cette implémentation.




                                                                                           13
                                                                  Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 14

~~~text
Algèbre de Boole : Implémentation physique
➢ Les circuits électroniques peuvent reproduire ces opérateurs!
➢ Les transistors sont la base de cette implémentation.

➢ Les portes logiques pouvant être reproduites par des circuits électroniques,
  on peut donc implanter physiquement des fonctions logiques dans un
  ordinateur pour effectuer des opérations.

➢ Pour économiser des ressources, il faut utiliser le moins de portes logiques
  possibles pour une même fonction logique.

➢ A l’aide des propriétés de l’algèbre de Boole, on va chercher à réduire et
  simplifier les fonctions logiques.

                                                                                                        14
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 15

~~~text
Algèbre de Boole : Propriétés




                                                         15
                                Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 16

~~~text
Algèbre de Boole : Loi de Morgan




                                                            16
                                   Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 17

~~~text
Algèbre de Boole : Loi de Morgan
➢ Démonstration de la loi de Morgan avec une table de vérité :


    𝑎             𝑏        𝑎ത          𝑏ത         𝑎ത . 𝑏ത       𝑎+𝑏       𝑎+𝑏
0             0        1          1           1             0         1
0             1        1          0           0             1         0
1             0        0          1           0             1         0
1             1        0          0           0             1         0



On a bien :

                           𝑎 + 𝑏 = 𝑎ത . 𝑏ത
                                                                                                   17
                                                                          Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 18

~~~text
Algèbre de Boole : Loi de Morgan

➢ Démonstration de la loi de Morgan par énoncé logique:

Soit l’énoncé suivant :

« Je sors s’il ne pleut pas et s’il fait chaud. »

Quelle est la contraposée de cet énoncé?

        → « Je ne sors pas s’il pleut ou s’il fait froid »



                                                                                      18
                                                             Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 19

~~~text
Algèbre de Boole : Simplification d’expression

➢ A l’aide de propriétés Booléennes démontrer les règles suivantes:

1. Règle d’absorption : 𝑎. 𝑎 + 𝑏 = 𝑎

Démonstration :
        𝑎. 𝑎 + 𝑏 = 𝑎. 𝑎 + 𝑎. 𝑏     (distributivité du ET)
                 = 𝑎 + 𝑎. 𝑏        (𝑎. 𝑎 = 𝑎)
                   =𝑎 1+𝑏           (factorisation par a et a. 1 = a)
                   =𝑎               (1 + b = 1 ∀ b)


                                                                                                 19
                                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 20

~~~text
Algèbre de Boole : Simplification d’expression

➢ A l’aide de propriétés Booléennes démontrer les règles suivantes:

1. Règle de simplification : 𝑎 + 𝑎.
                                 ത 𝑏 =𝑎+𝑏

Démonstration :
            𝑎 + 𝑎.
                ത 𝑏 = 𝑎. 𝑎 + 𝑏 + 𝑎.  ത 𝑏       (voir slide précédente)
                    = 𝑎. 𝑎 + 𝑎. 𝑏 + 𝑎.
                                     ത 𝑏
                    = 𝑎 + 𝑎. 𝑏 + 𝑎.
                                  ത 𝑏           (𝑎. 𝑎 = 𝑎)
                    = 𝑎 + 𝑏( 𝑎 + 𝑎)ത           (factorisation)
                    =𝑎+𝑏                       (𝑎 + 𝑎ത = 1)

                                                                                                  20
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 21

~~~text
Algèbre de Boole : Tableau de Karnaugh
  ➢ Pour simplifier une expression logique, on peut :
     1. La simplifier à l’aide des propriétés de l’algèbre de Boole (slides précédentes)
     2. Utiliser un tableau de Karnaugh

  ➢ Un tableau de Karnaugh est une représentation différente de la table de vérité : il s’agit
    d’un tableau à double entrée donnant les valeurs de la sortie en fonction des entrées.
                                     Valeurs possibles du couple d’entrées b et c


                    b c
                a
Valeurs
possibles
de l’entrée a


                                                                                                             21
                                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 22

~~~text
Algèbre de Boole : Tableau de Karnaugh
  ➢ Pour simplifier une expression logique, on peut :
     1. La simplifier à l’aide des propriétés de l’algèbre de Boole (slides précédentes)
     2. Utiliser un tableau de Karnaugh

  ➢ Un tableau de Karnaugh est une représentation différente de la table de vérité : il s’agit
    d’un tableau à double entrée donnant les valeurs de la sortie en fonction des entrées.
                                     Valeurs possibles du couple d’entrées b et c


                        b c
                a
Valeurs             0
possibles
de l’entrée a       1


                                                                                                             22
                                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 23

~~~text
Algèbre de Boole : Tableau de Karnaugh
  ➢ Pour simplifier une expression logique, on peut :
     1. La simplifier à l’aide des propriétés de l’algèbre de Boole (slides précédentes)
     2. Utiliser un tableau de Karnaugh

  ➢ Un tableau de Karnaugh est une représentation différente de la table de vérité : il s’agit
    d’un tableau à double entrée donnant les valeurs de la sortie en fonction des entrées.
                                      Valeurs possibles du couple d’entrées b et c


                        b c   0   0           0   1             1   1                1   0
                a
Valeurs             0
possibles
de l’entrée a       1


                                                                                                                      23
                                                                                             Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 24

~~~text
Algèbre de Boole : Tableau de Karnaugh
  ➢ Pour simplifier une expression logique, on peut :
     1. La simplifier à l’aide des propriétés de l’algèbre de Boole (slides précédentes)
     2. Utiliser un tableau de Karnaugh

  ➢ Un tableau de Karnaugh est une représentation différente de la table de vérité : il s’agit
    d’un tableau à double entrée donnant les valeurs de la sortie en fonction des entrées.
                                              Valeurs possibles du couple d’entrées b et c


                        b c          0   0            0   1             1    1               1   0
                a
Valeurs             0
possibles
de l’entrée a       1


                        Dans la construction du tableau les valeurs des variables ne                                          24
                        doivent varier que d’un seul bit entre chaque ligne / colonne !
                                                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 25

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Pour simplifier une expression logique, on peut :
   1. La simplifier à l’aide des propriétés de l’algèbre de Boole (slides précédentes)
   2. Utiliser un tableau de Karnaugh

➢ Un tableau de Karnaugh est une représentation différente de la table de vérité : il
  s’agit d’un tableau à double entrée donnant les valeurs de la sortie en fonction
  des entrées.

➢ Une fois le tableau rempli, on regroupe TOUTES les cases contenant ‘1’ par des
  groupes de tailles en puissances de 2 (1, 2, 4, …). Il faut prendre les groupes les
  plus grands possibles.

➢ En analysant ces groupes, on peut trouver une équation directement simplifiée.
                                                                                                     25
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 26

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée



          b c    0   0         0   1        1       1    1   0
  a
      0              1             1            1            0

      1              0             0            1            0




      𝑠=

                                                                                                  26
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 27

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée



          b c       0   0        0   1       1       1    1   0
  a
      0                 1            1           1            0

      1                 0            0           1            0


                On remarque que dans ce paquet de 1 on a b=a=0


          ത 𝑏ത
      𝑠 = 𝑎.

                                                                                                  27
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 28

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée



          b c       0   0        0   1       1       1    1   0
  a
      0                 1            1           1            0

      1                 0            0           1            0


                On remarque que dans ce paquet de 1 on a b=c=1


          ത 𝑏ത + 𝑏. 𝑐
      𝑠 = 𝑎.

                                                                                                  28
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 29

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée


       c d      0       0   0       1   1       1   1   0
 a b
  0    0            0           1           1       0
  0    1            0           1           1       1

  1    1            0           1           1       1
  1    0            0           1           1       0




           𝑠=

                                                                                                  29
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 30

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée


       c d   0       0   0       1   1       1   1   0
 a b
  0    0         0           1           1       0       On remarque que dans ce paquet, on a : d=1
  0    1         0           1           1       1

  1    1         0           1           1       1
  1    0         0           1           1       0




           𝑠=𝑑+

                                                                                                           30
                                                                                  Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 31

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée


       c d      0       0   0       1   1       1   1   0
 a b
  0    0            0           1           1       0
                                                            On pourrait regrouper ces deux 1,
  0    1            0           1           1       1
                                                            mais il est possible d’obtenir un
  1    1            0           1           1       1
                                                            plus grand groupe
  1    0            0           1           1       0




           𝑠 = 𝑑 + 𝑏. 𝑐. 𝑑ҧ

                                                                                                            31
                                                                                   Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 32

~~~text
Algèbre de Boole : Tableau de Karnaugh
➢ Exemple: soit le tableau de Karnaugh suivant, trouvez l’équation logique associée


       c d     0       0   0       1   1       1   1   0
 a b
  0    0           0           1           1       0
  0    1           0           1           1       1
                                                           Dans ce groupe on a c=1 et b=1
  1    1           0           1           1       1
  1    0           0           1           1       0




           𝑠 = 𝑑 + 𝑏. 𝑐

                                                                                                             32
                                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 33

~~~text
Algèbre de Boole : Tableau de Karnaugh
 ➢ On peut « reboucler sur le tableau »

        c d   0       0   0       1   1       1   1   0
  a b
   0    0         0           0           0       0
   0    1         1           0           0       1
                                                          𝑠 = 𝑏. 𝑑ҧ
   1    1         1           0           0       1
   1    0         0           0           0       0




➢ Il faut que TOUS les 1 appartiennent à un groupe.


                                                                                               33
                                                                      Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 34

~~~text
Algèbre de Boole : Construction de circuit logique

 ➢ Pour construire un circuit logique à partir d’un énoncé:

    1. Construire la table de vérité

    2. Déterminer l’équation logique grâce :
             à la simplification de l’équation logique
                     OU
             au tableau de Karnaugh

    3.   Dessiner le circuit à l’aide de portes logiques.


                                                                                       34
                                                              Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 35

~~~text
Algèbre de Boole : Représentation logique
Exemple : « S(A,B,C) = 1 si et seulement si la majorité des trois variables A, B, C valent 1. »

1. Table de vérité​ :

                             A​    B​    C​    S​
                             0​    0​    0​    ​0
                             0​    0​    1​     ​0
                              0​    1​   0​    ​0
                              0​    1​   1​     ​ 1
                              1​    0​   0​    ​0
                              1​    0​   1​    ​1
                              1​    1​   0​     ​ 1
                              1​    1​   1​    ​1                                                        35
                                                                                Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 36

~~~text
Algèbre de Boole : Représentation logique
« S(A,B,C) = 1 ssi la majorité des
trois variables A, B, C valent 1. »

2 Equation :
1. On regroupe les cas ou S=1
2. On simplifie l’équation

𝑠 = 𝑎𝑏𝑐
    ത + 𝑎𝑏cത + ab𝑐ҧ + 𝑎𝑏𝑐              𝑎+𝑎 =𝑎
𝑠 = 𝑎𝑏𝑐
    ത + 𝑎𝑏cത + ab𝑐ҧ + 𝑎 + 𝑎 + 𝑎 𝑏𝑐
𝑠 = 𝑎𝑏𝑐
    ത + 𝑎𝑏c ത + ab𝑐ҧ + 𝑎𝑏𝑐 + 𝑎𝑏𝑐 + 𝑎𝑏𝑐
𝑠 = 𝑏𝑐 𝑎ത + 𝑎 + 𝑎𝑏 𝑐ҧ + 𝑐 + 𝑎𝑐 𝑏ത + 𝑏
𝒔 = 𝒃𝒄 + 𝒂𝒃 + 𝒂𝒄                      𝑎 + 𝑎ത = 1


                                                                            36
                                                   Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 37

~~~text
Algèbre de Boole : Tableau de Karnaugh
Ou utilisation du tableau de Karnaugh




             0      0      1      0

             0      1      1      1




                                                                  37
                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 38

~~~text
Algèbre de Boole : Tableau de Karnaugh
Ou utilisation du tableau de Karnaugh




             0      0      1      0

             0      1      1      1


             𝒔 = 𝒃𝒄 + 𝒂𝒃 + 𝒂𝒄

 On retrouve bien le même résultat.                               38
                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 39

~~~text
Algèbre de Boole : Représentation logique
« S(A,B,C) = 1 si et seulement si la majorité des trois variables A, B, C valent 1. »

3.Circuit :

S=BC+AC+AB
      A       B   C
                                𝐴. 𝐵
                                                      𝐴. 𝐵 + 𝐵. 𝐶
                                                                             𝐴. 𝐵 + 𝐵. 𝐶 + 𝐴. 𝐶 = 𝑆
                                 𝐵. 𝐶


                                  𝐴. 𝐶



                                                                                                          39
                                                                                 Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 40

~~~text
Algèbre de Boole : Représentation logique
« S(A,B,C) = 1 si et seulement si la majorité des trois variables A, B, C valent 1. »

3.Circuit :

S=BC+AC+AB




                                                                                                          40
                                                                                 Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 41

~~~text
Conclusion
➢ L’algèbre de Boole permet de modéliser des énoncés logiques et utilise des
  variables dont les valeurs possibles sont VRAI (1) ou FAUX (0).

➢ A partir d’un énoncé, on peut déterminer une équation et un circuit logique
  répondant au problème.

➢ Les différents opérateurs de l’algèbre de Boole sont implémentables sur des
  circuits électroniques grâce aux transistors.

➢ Le fonctionnement d’un ordinateur se base sur l’algèbre de Boole : les différents
  calculs et traitements de données effectués par un ordinateur (comparaison,
  addition etc. ) sont modélisés par des circuits logiques implémentés sur carte
  électronique.
                                                                                                   41
                                                                          Eva ANSERMIN & Romuald GRIGNON
~~~
