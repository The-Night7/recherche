# CM3-Representation-des-nombres-part2_2024-2025_Informatique1_P1S1_EAnsermin-RGrignon.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1ZbykCZEb3nJHXttc5LVL4OoXrG5rLtQn) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                         v1.4




INFORMATIQUE 1
I I . R E P R E S E N TAT I O N D E S
NOMBRES (PARTIE 2)




                                        Eva Ansermin & Romuald Grignon
~~~

## Page 2

~~~text
Rappel
 ➢Tableau des puissances de 2




➢Exemple :


                     1000 10102 → 2 + 8 + 128 = 138


                                                                                 2
                                                      Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 3

~~~text
L’hexadécimal
➢En base hexadécimale (ou base 16):
   ➢Les chiffres sont : {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
   ➢On multiplie les chiffres par des puissances de 16 :
   Soit N un entier dont les chiffres sont 𝑝𝑛 , 𝑝𝑛−1 , 𝑝𝑛−2 , … , 𝑝0   en base
   décimale :

                                  𝑛

                           𝑁 = ෍ 𝑝𝑖 ∗ 16𝑖
                                 𝑖=0



   Exemple : 2𝐶 16 → 2 ∗ 161 + C ∗ 160 = 32 + 12 = 44
                                                                                                   3
                                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 4

~~~text
L’hexadécimal
➢Connaître les puissances de 16 n’est pas simple ! Mais on peut remarquer que :
                          24 = 16 𝑒𝑡 1111 = 15
->Un chiffre en hexadécimal correspond donc à 4 bits en binaire.


Il est souvent plus aisé de passer par le binaire quand on souhaite faire une
conversion décimal/hexadécimal.


Exemple: 173 → 1010 1101 → 𝐴 𝐷
Exemple: 240 → 1111 0000 → 𝐹 0

                                                                                                   4
                                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 5

~~~text
Valeurs représentables :

➢Soit N, un nombre entier naturel codé sur n bits
   ➢ La plus petite valeur possible est 0
   ➢La plus grande valeur possible est 1111…11




                                                                               5
                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 6

~~~text
Valeurs représentables :

➢Soit N, un nombre entier naturel codé sur n bits
   ➢ La plus petite valeur possible est 0
   ➢La plus grande valeur possible est 1111…11

   On remarque que :

                       11111 … 111 + 1 = 1 0000 … 00
                              n                     n

                                            = 2𝑛


     Donc 𝟏𝟏𝟏𝟏 … 𝟏𝟏𝟏 = 𝟐𝒏 − 𝟏                                                      6
                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 7

~~~text
Valeurs représentables :

➢Soit N, un nombre entier naturel codé sur n bits, la gamme de valeurs
 représentables en base 2 est : [𝟎 ∶ 𝟐𝒏 − 𝟏]




➢Soit sur :
   ➢8 bits    :    [0 ∶ 255]
   ➢16 bits :      [0 ∶ 65535]
   ➢32 bits :      [0 ∶ 4 294 967 295]


                                                                                           7
                                                                Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 8

~~~text
Valeurs représentables : overflow
➢Soit un ordinateur dont les nombres sont encodés sur un octet.
➢Que se passe-t-il lorsqu’on effectue l’opération suivante ?
                           1110 0011
                       +
                           0110 0110
                       1 0100 1001


         Le résultat est sur 9 bits : le premier chiffre ne peut pas être stocké !


 ➢ Lorsque le résultat d’une opération ne peut pas être représenté avec
   le nombre de chiffres disponible on parle d’overflow (dépassement en
   français).
                                                                                                          8
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 9

~~~text
Conséquence sur la gestion de mémoire
➢Une mémoire est divisée en différentes « cases » de même capacité (~ octet).




➢Il faut prendre en compte la taille de nos données pour les stocker dans la
 mémoire!
                                                                                                  9
                                                                       Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 10

~~~text
Autre types de données
 ➢ La gestion des textes (données alphanumériques) : Des standards (code ASCII, unicode…)
   permettent d’associer des caractères à des nombres :




                                                                                                             10
                          Extrait de la table ASCII                                 Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 11

~~~text
Représentation du signe (1/2)
➢ I. Signe grandeur: Le bit de signe est le bit de plus fort poids (celui
  situé le plus à gauche du nombre binaire)
      -> Il vaut 0 lorsque le nombre est positif et 1 lorsqu’il est négatif.

➢   Exemple :

                 01001001 représente + 7310
                 11001001 représente - 7310
➢    Inconvénients :
    ➢ la soustraction ne marche pas avec cette méthode (A - A ≠ 0)
    ➢ Il y a deux manières de représenter le zéro

                                                                                                        11
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 12

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                               −𝑁 = 𝑁 + 1

   ➢ Le bit de poids fort indique le signe :
      ▪ si 0, nombre positif
      ▪ si 1 nombre négatif



                                                                                              12
                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 13

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                                  −𝑁 = 𝑁 + 1
   ➢ Méthode décimal -> binaire :
   1. On transforme la valeur absolue du nombre
               7310 = 0100 1001
   2. On passe au complément :
               73 = 0100 1001 = 1011 0110
   3. On ajoute +1 :
               −73 = 1011 0110 + 1 = 1011 0111

                                                                                              13
                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 14

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                                     −𝑁 = 𝑁 + 1
   ➢ Méthode binaire -> décimal :
   1 . On regarde le bit de poids fort : s’il vaut 0 alors le nombre est positif, traduire
   directement.
   2. Si le bit de poids fort vaut 1, le nombre est négatif, il faut faire l’opération inverse
       a. Retirer 1
                        1011 0111 − 1 = 1011 0110
       b. Faire le complément
                        1011 0110 = 0100 1001
       c. Traduire le nombre obtenu et le mettre en négatif                                                               14
                         0100 1001 ⇒ 7310 ⟺ 1011 0111 = −7310
                                                                                                 Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 15

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                             −𝑁 = 𝑁 + 1
   ➢ Valeurs représentables sur n bits:
          ▪ Le plus grand nombre :




                                                                                              15
                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 16

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                               −𝑁 = 𝑁 + 1
   ➢ Valeurs représentables sur n bits:
          ▪ Le plus grand nombre :
                       0111…111 = 2𝑛−1 − 1
                         n-1 bits




                                                                                              16
                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 17

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                               −𝑁 = 𝑁 + 1
   ➢ Valeurs représentables sur n bits:
          ▪ Le plus grand nombre :
                       0111…111 = 2𝑛−1 − 1
                         n-1 bits

          ▪ Le plus petit nombre :

                                                                                              17
                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 18

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:
    ➢ On appelle complément à 1 d’un nombre binaire N le nombre N dont
       les 1 et les 0 sont inversés.

   ➢ On représente –N de la manière suivante en complément à 2 :

                               −𝑁 = 𝑁 + 1
   ➢ Valeurs représentables sur n bits:
          ▪ Le plus grand nombre :
                       0111…111 = 2𝑛−1 − 1
                         n-1 bits

          ▪ Le plus petit nombre :
                       1000…000 ⇔ -(0111…111 +1) = −2𝑛−1
                                                                                              18
                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 19

~~~text
Représentation du signe (2/2)
➢ II. Le complément à 2:

   ➢ Intérêts :
       ➢ Une seule manière de représenter le 0 : on couvre un valeur de plus
         sur le même nombre de bits: sur n bits є −𝟐𝒏−𝟏 : 𝟐𝒏−𝟏 − 𝟏
       ➢ Les soustractions / additions fonctionnent !

   ➢ Soit sur
      ➢ 8 bits : [ -128 : 127 ]
      ➢ 16 bits : [ -32768 : 32767 ]
      ➢ 32 bits : [- 2 147 483 648 : 2 147 483 647 ]

   ➢ C’est cette convention qui est utilisée pour représenter les entiers
     négatifs dans les ordinateurs.
                                                                                                     19
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 20

~~~text
Représentation nombres réels (1/3)
➢ Principe

   ➢ Comme pour le symbole “-” il n’y a pas de moyen de représenter
     explicitement la virgule en binaire.

   ➢ En decimal, les chiffres derrière la virgule sont multipliés par des puissance
     de 10 negatives :

              Ex : 26,75 = 2 ∗ 10 + 6 ∗ 100 + 7 ∗ 10−1 + 5 ∗ 10−2

   ➢ Plus généralement :
                                                          𝑛

                        𝑁 = 𝑎𝑛 𝑎𝑛_1 … 𝑎0 . 𝑎−1 𝑎−2 … 𝑎−𝑝 = ෍ 𝑎𝑖 ∗ 10𝑖
                                                        𝑖=−𝑝

   ➢ En binaire, on utilise des puissances de 2 négatives.                                            20
                                                                             Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 21

~~~text
Représentation nombres réels (2/3)
➢ I. La virgule fixe

    ➢ On défini explicitement le nombre de bits avant (puissance de 2 positive)
      et après (puissance de 2 negatives) la virgule.




                                                       𝑚

                       𝑁 = 𝑏𝑚 𝑏𝑚−1 … 𝑏0 𝑏−1 𝑏−2 … 𝑎−𝑛 = ෍ 𝑎𝑖 ∗ 2𝑖
                                                      𝑖=−𝑛

                                                                                                    21
                                                                           Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 22

~~~text
Représentation nombres réels (2/3)
➢ I. La virgule fixe

    ➢ Exemple : Sur 8 bits, on définit 5 bits avant et 3 bits après la virgule.

       24 = 16    3
                 2 =8       2
                           2 =4      21 = 2   20 = 1   2−1 = 0,5   2−2 = 0,25   2−3 = 0,125



    ➢ 11000,1102 → 24 + 23 + 2−1 + 2−2 = 16 + 8 + 0,5 + 0,25 = 24,75


    ➢ 10,62510 → 8 + 2 + 0,5 + 0,125 = 23 + 21 + 2−1 + 2−3 = 010101012



                                                                                                            22
                                                                                   Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 23

~~~text
Représentation nombres réels (2/3)
➢ I. La virgule fixe :

    ➢ Exemple : Sur 8 bits, on définit 5 bits avant et 3 bits après la virgule.

       24 = 16   23 = 8    22 = 4     21 = 2   20 = 1   2−1 = 0,5    2−2 = 0,25   2−3 = 0,125




    ➢ 32,5 ? Il faudrait plus de bits avant la virgule et moins après.

       25 = 32 24 = 16    23 = 8     22 = 4    21 = 2   20 = 1   2−1 = 0,5   2−2 = 0,25



                                   32,5 → 100000,10
                                                                                                               23
    Mais ici on ne peut plus representer 10,625!
                                                                                      Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 24

~~~text
Représentation nombres réels (2/3)
➢ I. La virgule fixe :

    ➢ Exemple : Sur 8 bits, on définit 5 bits avant et 3 bits après la virgule.

       24 = 16    23 = 8     22 = 4    21 = 2   20 = 1    2−1 = 0,5   2−2 = 0,25   2−3 = 0,125




    ➢ 3,5625 ? Il faudrait plus de bits après la virgule et moins avant.

         23 = 8     22 = 4    21 = 2   20 = 1 2−1 = 0,5   2−2 = 0,25 2−3 = 0,125 2−4 = 0,0625



                                 3,5625 → 0011,1001
                                                                                                               24
    Mais dans ce cas 16 n’est plus représentable !
                                                                                      Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 25

~~~text
Représentation nombres réels (2/3)
➢ I. La virgule fixe :

    ➢ Avantages:
       - facile à calculer
       - Opération faciles à effectuer

   ➢ Inconvénients : nécessite de trouver un compromis entre précision et
     grand nombre !


   ➢ Ce n’est pas ce qui est utilisé dans les ordinateurs du fait du manque de
     souplesse de cette représentation.


                                                                                                     25
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 26

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante :

    ➢ La virgule flottante est la convention utilisée dans les ordinateurs.

    ➢ La norme d’utilisation des virgules flottantes est la norme IEEE754 avec :
       ➢ Simple precision pour les nombres sur 32 bits
       ➢ Double précision pour les nombres sur 64 bits

    ➢ Plus complexe que la virgule fixe, elle permet de représenter des nombres
      à la fois précis et grands sans changer de règle de représentation.




                                                                                                       26
                                                                              Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 27

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : principe

En decimal, on peut mettre les nombres sous forme “scientifique”:
                                𝑁 = ±𝑎𝑛 , 𝑎𝑛−1 𝑎𝑛−2 … 𝑎0 ∗ 10𝑝

            Un seul chiffre avant la virgule          Une puissance >0 ou <0




Exemple : 548,96 = 5,4896 ∗ 102

                                                                                                  27
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 28

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : principe

En decimal, on peut mettre les nombres sous forme “scientifique”:
                                𝑁 = ±𝑎𝑛 , 𝑎𝑛−1 𝑎𝑛−2 … 𝑎0 ∗ 10𝑝

            Un seul chiffre avant la virgule           Une puissance >0 ou <0

De la même façon en binaire :

                              𝑁 = ±𝑏𝑛 , 𝑏𝑛−1 𝑏𝑛−2 … 𝑏0 ∗ 2𝑝

Exemple : 7,125 → 111,001 = 1,11001 ∗ 22
                                                                                                   28
                                                                          Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 29

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : principe

L’écriture en virgule flottante consiste à traduire séparément les différentes
parties d’un nombre binaire écrit sous cette forme :
                           𝑁 = ±𝑏𝑛 , 𝑏𝑛−1 𝑏𝑛−2 … 𝑏0 ∗ 2𝑝

                              = −1 𝑠 ∗ 1, 𝑚 ∗ 2𝑒
Avec
   • s : le signe (qui vaut 0 ou 1)
   • m : la mantisse
   • e : l’exposant



                                                                                                          29
                                                                                 Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 30

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : principe

L’écriture en virgule flottante consiste à traduire séparément les différentes
parties d’un nombre binaire écrit sous cette forme :
                           𝑁 = ±𝑏𝑛 , 𝑏𝑛−1 𝑏𝑛−2 … 𝑏0 ∗ 2𝑝

                              = −1 𝑠 ∗ 1, 𝑚 ∗ 2𝑒
Avec
   • s : le signe (qui vaut 0 ou 1)
   • m : la mantisse
   • e : l’exposant



                                                                                                          30
                                                                                 Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 31

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : simple precision

En norme simple precision (32 bits) un nombre binaire sera représenté:




                                                −1 𝑠 ∗ 1, 𝑚 ∗ 2𝑒




                                                                                                  31
                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 32

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : simple precision

En norme simple precision (32 bits) un nombre binaire sera représenté:




                                                             −1 𝑠 ∗ 1, 𝑚 ∗ 2𝑒

Méthode de calcul de decimal à simple precision :
1. Traduire de decimal en binaire et mettre sous la forme
2. En déduire les différentes parties
         a. le signe ‘s’ sera à 0 si le nombre est positif, à 1 sinon

                                                                                                         32
                                                                                Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 33

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : simple precision

En norme simple precision (32 bits) un nombre binaire sera représenté:




                                                             −1 𝑠 ∗ 1, 𝑚 ∗ 2𝑒

Méthode de calcul de decimal à simple precision :
1. Traduire de decimal en binaire et mettre sous la forme
2. En déduire les différentes parties
         a. le signe ‘s’ sera à 0 si le nombre est positif, à 1 sinon
         b. la mantisse ‘m’ sur 23 bits
                                                                                                         33
                                                                                Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 34

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : simple precision

En norme simple precision (32 bits) un nombre binaire sera représenté:




                                                        −1 𝑠 ∗ 1, 𝑚 ∗ 2𝑒

Méthode de calcul de decimal à simple precision :
1. Traduire de decimal en binaire et mettre sous la forme
2. En déduire les différentes parties
         a. le signe ‘s’ sera à 0 si le nombre est positif, à 1 sinon
         b. la mantisse ‘m’ sur 23 bits
         c. 𝐸𝑥𝑝 = 𝑒 + 𝑏𝑖𝑎𝑖𝑠 = 𝑒 + 127 . Le biais sert à s’assurer que l’exposant est positif                            34
                                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 35

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : simple precision
Exemple : 45,25
1. Traduire de décimal en binaire
               -45,25 = − 32 + 8 + 4 + 1 + 0,25 = −(101101.01)
                      = − 1.0110101 ∗ 25
2. En déduire les différentes parties :
        a. le signe : 1 car nombre négatif
        b. la mantisse = 𝟎𝟏𝟏𝟎𝟏𝟎𝟏
        c. 𝐸𝑥𝑝 = 5 + 127 = 132
                 = 128 + 4 = 𝟏𝟎𝟎𝟎 𝟎𝟏𝟎𝟎

Donc on a −45,25 → 1 1000 0100                   01101010000000000000000                              35
                     signe   Exposant (8 bits)          Mantisse (23 bits)   Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 36

~~~text
Représentation nombres réels (3/3)
➢ II. La virgule flottante : remarques

➢ Valeurs particulières




➢ Il est impossible d’obtenir un nombre à la fois très grand et très précis
  (comme en décimal sur un nombre de chiffres fixe!).

➢ Certains nombres comme les irrationnels ne sont pas représentables : on
  utilise des arrondis.                                                                                36
                                                                              Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 37

~~~text
Représentation des nombres
➢ Lorsque l’on va stocker/utiliser un nombre binaire on doit faire plusieurs choix :
   1. Quelle convention de representation?
          ℕ (𝑒𝑛𝑡𝑖𝑒𝑟 𝑛𝑎𝑡𝑢𝑟𝑒𝑙)     ℚ (𝑒𝑛𝑡𝑖𝑒𝑟 𝑟𝑒𝑙𝑎𝑡𝑖𝑓)     ℚ (𝑛𝑜𝑚𝑏𝑟𝑒 𝑟𝑎𝑡𝑖𝑜𝑛𝑒𝑙)
        Binaire classique      Complément à 2         Virgule flottante

       Pour savoir comment interpréter un nombre binaire il faut connaître la
       convention avec laquelle il est encodé !

   2. Quelle taille (nombre de bits)?
       ➢ Pas assez de chiffres : nombre non représentable
       ➢ Trop : mémoire gâchée

➢ Lorsque l’on programme, on indique à l’ordinateur ces différentes propriétés.
  C’est le type .                                                                                      37
                                                                              Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 38

~~~text
Conclusion
➢ L’ordinateur ne pouvant stocker que des 1 et des 0, il est impossible
  d’utiliser les symboles habituels mathématiques pour représenter des
  nombres.

➢ On utilise diverses conventions (virgule flottante, complement à 2) pour
  gérer la représentation des nombres.

➢ Il est important de savoir la taille d’une donnée pour gérer son stockage
  ainsi que sa convention de représentation pour que l’ordinateur sache
  l’interpreter.

➢ Nous connaissons la forme de stockage des données d’un ordinateur.
  Comment se déroule des opérations sur ces données?
                                                                                                       38
                                                                              Eva ANSERMIN & Romuald GRIGNON
~~~
