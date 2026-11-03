# CM2-Representation-des-nombres-part1_2023-2024_Informatique1_P1S1_EAnsermin-RGrignon.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1UzCFGKwA9rUdvCvAnlBF0cgve3fh_NsH) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                         v1.1




INFORMATIQUE 1
I I . R E P R E S E N TAT I O N D E S
NOMBRES




                                        Eva Ansermin & Romuald Grignon
~~~

## Page 2

~~~text
Représentation des données
➢ Un ordinateur peut traiter/produire plusieurs types de données :
    ➢ textes, chiffres
    ➢ images
    ➢ sons
    ➢ ...
➢ Toutes ces informations sont stockées et traitées sous forme binaire : avec des 0 et des 1.
➢ Cette unité d’information (0 0u 1) est le binary digit (le bit).
➢ Ce type de données est plus facile à gérer au niveau électronique : 0 correspond à un circuit
  ouvert, 1 à un circuit fermé.



            0 : le courant ne passe pas           1 : le courant passe                                               2
                                                                                          Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 3

~~~text
Représentation des données
➢ Un ordinateur peut traiter/produire plusieurs types de données :
    ➢ textes, chiffres
    ➢ images
    ➢ sons
    ➢ ...
➢ Toutes ces informations sont stockées et traitées sous forme binaire : avec des 0 et des 1.
➢ Cette unité d’information (0 ou 1) est le binary digit (le bit).


➢ Comment sont représentés les nombres en binaire ?



                                                                                                                     3
                                                                                          Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 4

~~~text
Vocabulaire
➢ Bit : information élémentaire, valant 0 ou 1.
➢ Octet (Byte en Anglais) : information constituée de 8 bits.

➢ Mot : unité manipulée par le processeur (16, 32, 64bits, …).
➢ Capacités (norme commerciale depuis 1998).

Nom                             Capacité          Exemples
1 octet                         8 bits             1 octet ~ 2 caractères
1 Ko (kilo octet)               103 octets        500 ko ~ un roman
1 Mo (mega octet)               106 octets        100 Mo ~ une pile de livre de 1 mètre
1 Go (giga octet)               109 octets        1 Go ~ une camionnette de livres
1 To (téra octet)               1012 octets       2 To ~ une Bibliothèque Universitaire
1 Po (peta octet)               1015 octet        2 Po ~ toutes les BU des USA
1 Eo (exa octet)                1018 octet        5 Eo ~ tous les mots prononcés depuis
                                                  le début de l'humanité
                                                  2 Eo ~ volume annuel des informations                              4
                                                  du monde
                                                                                          Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 5

~~~text
Vocabulaire
➢ Bit : information élémentaire, valant 0 ou 1.
➢ Octet (Byte en Anglais) : information constituée de 8 bits.

➢ Mot : unité manipulée par le processeur (16, 32, 64bits, …).
➢ Capacités (norme commerciale depuis 1998).



         Nom                             Capacité          Capacité
         1 Kio (kibi octet)                       210      1 024 octets
         1 Mio (mébi octet)                       220      1 048 576 o
         1 Gio (Gibi octet)                       230      1 073 741 824 o
         1 Tio (Tébi octet)                       240      1 099 511 627 776 o
         1 Pio (Pébi octet)                       250      1 125 899 906 842 620 o
         1 Eio (Exbi octet)                       260      1 152 921 504 606 846 976 o

                                                                                                                    5
                                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 6

~~~text
Les bases
➢Nous comptons en base 10 (base décimale) : Les chiffres vont de 0 à 9.
➢Exemple de décomposition d’un nombre :
      542 = 5 ∗ 100 + 4 ∗ 10 + 2 ∗ 1 = 5 ∗ 10 2 + 4 ∗ 101 + 2 ∗ 1

➢Soit N un entier dont les chiffres sont {𝑎𝑛 , 𝑎𝑛−1 , 𝑎𝑛−2 , … , 𝑎0 } en base décimale:
                       𝑁 = 𝑎𝑛 ∗ 10𝑛 + 𝑎𝑛−1 ∗ 10𝑛−1 + … + 𝑎0 ∗ 100
                        𝑁 = σ𝑛𝑖=0 𝑎𝑖 ∗ 10𝑖




                                                                                                          6
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 7

~~~text
Les bases
➢Nous comptons en base 10 (base décimale) : Les chiffres vont de 0 à 9.
➢Exemple de décomposition d’un nombre :
      542 = 5 ∗ 100 + 4 ∗ 10 + 2 ∗ 1 = 5 ∗ 10 2 + 4 ∗ 101 + 2 ∗ 1

➢Soit N un entier dont les chiffres sont {𝑎𝑛 , 𝑎𝑛−1 , 𝑎𝑛−2 , … , 𝑎0 } en base décimale:
                       𝑁 = 𝑎𝑛 ∗ 10𝑛 + 𝑎𝑛−1 ∗ 10𝑛−1 + … + 𝑎0 ∗ 100
                        𝑁 = σ𝑛𝑖=0 𝑎𝑖 ∗ 10𝑖

                                    i est le poids du chiffre.

   On parle de poids fort pour le chiffre le plus à gauche (plus haute puissance)
   et de poids faible pour celui le plus à droite (puissance la plus faible)                              7
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 8

~~~text
Les bases
➢ Nous utilisons plusieurs bases dans notre vie quotidienne:




                                                                                          8
                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 9

~~~text
Les bases
➢En base décimale : chiffre allant de 0 à 9 et 𝑁 = σ𝑛𝑖=0 𝑎𝑖 ∗ 10𝑖


➢En base binaire (ou base 2) :
   ➢Les chiffres sont :




                                                                                               9
                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 10

~~~text
Les bases
➢En base décimale : chiffre allant de 0 à 9 et 𝑁 = σ𝑛𝑖=0 𝑎𝑖 ∗ 10𝑖


➢En base binaire (ou base 2) :
   ➢Les chiffres sont : {0,1}




                                                                                             10
                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 11

~~~text
Les bases
➢En base décimale : chiffre allant de 0 à 9 et 𝑁 = σ𝑛𝑖=0 𝑎𝑖 ∗ 10𝑖


➢En base binaire (ou base 2) :
   ➢Les chiffres sont : {0,1}
   ➢On multiplie les chiffres par des puissances de 2 :
   Soit N un entier dont les chiffres sont 𝑝𝑛 , 𝑝𝑛−1 , 𝑝𝑛−2 , … , 𝑝0 en base binaire :
                                 𝑛

                            𝑁 = ෍ 𝑝𝑖 ∗ 2𝑖
                                 𝑖=0

                           𝑁 = 𝑝𝑛 ∗ 2𝑛 + 𝑝𝑛−1 ∗ 2𝑛−1 + … +𝑝0 ∗ 20


                                                                                                        11
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 12

~~~text
Les bases
➢En base décimale : chiffre allant de 0 à 9 et 𝑁 = σ𝑛𝑖=0 𝑎𝑖 ∗ 10𝑖


➢En base binaire (ou base 2) :
   ➢Les chiffres sont : {0,1}
   ➢On multiplie les chiffres par des puissances de 2 :
   Soit N un entier dont les chiffres sont 𝑝𝑛 , 𝑝𝑛−1 , 𝑝𝑛−2 , … , 𝑝0 en base binaire :
                                 𝑛

                            𝑁 = ෍ 𝑝𝑖 ∗ 2𝑖
                                 𝑖=0

                           𝑁 = 𝑝𝑛 ∗ 2𝑛 + 𝑝𝑛−1 ∗ 2𝑛−1 + … +𝑝0 ∗ 20

➢Exemple : 0112 = 0 ∗ 22 + 1 ∗ 21 + 1 ∗ 20 = 0 + 2 + 1 = 3
                                                                                                        12
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 13

~~~text
  Binaire -> décimal
➢Il suffit d’ajouter les puissances de deux des chiffres dont le bit est à 1.


➢Il faut donc connaître les puissances de deux !




                                               1       0        0       1       0              0

➢Exemple : 1001002 → 25 + 22 = 32 + 4 = 36




                                                                                                             13
                                                                                    Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 14

~~~text
Décimal -> binaire
➢1ère méthode : la division Euclidienne. On utilise les restes successifs de la division
 entière par 2.

        173 / 2 = 86 reste 1
         86 / 2 = 43 reste 0
         43 / 2 = 21 reste 1
         21 / 2 = 10 reste 1
         10 / 2 =   5 reste 0
          5 / 2 =   2 reste 1
          2 / 2 =   1 reste 0
          1 / 2 =   0 reste 1

                                Arrêt lorsque le quotient est nul




                                                                                                        14
                                                                               Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 15

~~~text
Décimal -> binaire
➢1ère méthode : la division Euclidienne. On utilise les restes successifs de la division
 entière par 2.

        173 / 2 = 86 reste 1
         86 / 2 = 43 reste 0
         43 / 2 = 21 reste 1
         21 / 2 = 10 reste 1
                                                                    17310 => 101011012
         10 / 2 =   5 reste 0
          5 / 2 =   2 reste 1
          2 / 2 =   1 reste 0
          1 / 2 =   0 reste 1

                                Arrêt lorsque le quotient est nul




                                                                                                                  15
                                                                                         Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 16

~~~text
Décimal -> binaire
 ➢2ère méthode : Décomposition en puissance de deux (ou division par puissance de 2)
  On recherche successivement les plus grandes puissances de 2 dans le nombre:

  ➢Exemple : (173)10 = 128 + 45
                     = 128 + 32 + 13
                     = 128 + 32 + 8 + 5
                     = 128 + 32 + 8 + 4 + 1
                     → 10101101




                         1         0         1        0        1        1        0             1

                                                                                                              16
                                                                                     Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 17

~~~text
Opération en binaire
➢ Les règles de posage des opérations classiques restent les mêmes en binaire : opérations
  chiffre par chiffre avec les règles de retenue.

➢ Exemple : l’addition
                               11   11
                               1110 0011
                           +
                               0110 0110

                           1 0100 1001




                                                                                                                 17
                                                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 18

~~~text
Opération en binaire
➢ Les règles de posage des opérations classiques restent les mêmes en binaire : opérations
  chiffre par chiffre avec les règles de retenue.

➢ Exemple : l’addition
                               11   11
                               1110 0011   → 227
                           +
                               0110 0110   → 102

                           1 0100 1001     → 329




                                                                                                                 18
                                                                                        Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 19

~~~text
Conclusion
• Toutes les données d’un ordinateur sont stockées et gérées sous forme
  binaire qui représente la présence ou l’absence de courant.

• En binaire, les chiffres d’un nombre sont multipliés par des puissances de 2
  (puissances de 10 en base décimale)

• Nous avons vu comment représenter un entier en nombre binaire mais
  est-ce suffisant?

• Dans le prochain cours nous verront comment représenter d’autres
  nombres ainsi que d’autres types de données.
                                                                                                     19
                                                                            Eva ANSERMIN & Romuald GRIGNON
~~~
