# CM05-Recursivite_2023-2024_Informatique2_P1S2_EAnsermin-RGrignon.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1LG9FXAODk0wYrmxRn6p8sFDO_L8VTUI6) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 1.

## Page 1

![Fac-similé de la page 1](../facsimiles/1f53aaaae5d66c6a8673f46a.jpg)

~~~text
INFORMATIQUE 1
I V. L A R É C U R S I V I T É
~~~



## Page 2

~~~text
Rappel: un exemple de fonction
 ●   L’opérateur factoriel se note “!”. Par définition :
                                    𝑁! = 1 ∗ 2 ∗ 3 … ∗ 𝑁 − 1 ∗ 𝑁
~~~

## Page 3

~~~text
Rappel: un exemple de fonction
 ●   L’opérateur factoriel se note “!”. Par définition :
                                    𝑁! = 1 ∗ 2 ∗ 3 … ∗ 𝑁 − 1 ∗ 𝑁

 ●     La fonction suivante permet de calculer la factorielle d’un nombre passé en paramètre :

 // Fonction qui calcule la factorielle d’un nombre
 // Conditions d’appel : nb un entier positif ou nul
 FONCTION factorielle(nb : ENTIER) : ENTIER
 VARIABLE
        i, res : ENTIER
 DÉBUT
        res ← 1
        POUR i DE 1 à nb+1 FAIRE //pourquoi cet encadrement? Peut-
 on faire mieux ?
                res ← res*i
        FIN POUR

           RETOURNER res // on retourne le résultat
 FIN
~~~

## Page 4

~~~text
Rappel: un exemple de fonction
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER
VARIABLE
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER
DEBUT
       a ← 5
       ECRIRE(factorielle(a))
FIN
~~~

## Page 5

~~~text
Rappel: un exemple de fonction
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER
VARIABLE
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                            Variable programme principal
DEBUT
       a ← 5                                          a
       ECRIRE(factorielle(a))
FIN
~~~

## Page 6

~~~text
Rappel: un exemple de fonction
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER
VARIABLE
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                            Variable programme principal
DEBUT
       a ← 5                                          a
       ECRIRE(factorielle(a))                         5
FIN
~~~

## Page 7

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 8

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 9

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5                              1
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 10

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              2               1
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
~~~

## Page 11

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              2               2
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 12

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              3               2
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 13

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              3               2
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 14

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              3               6
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 15

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              4               6
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 16

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              4               6
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 17

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              4               24
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 18

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              5               24
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 19

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              5               24
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 20

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              5               120
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 21

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              6               120
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 22

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              6               120
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 23

~~~text
Rappel: un exemple de fonction
                                                  Variables fonction factorielle
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER   nb             i               res
VARIABLE                                     5              6               120
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                   Variable programme principal
DEBUT
       a ← 5                                                    a
       ECRIRE(factorielle(a))                                   5
FIN
~~~

## Page 24

~~~text
Rappel: un exemple de fonction
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER
VARIABLE
       i, res : ENTIER
DÉBUT
       res ← 1
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                            Variable programme principal
DEBUT
       a ← 5                                         a
       ECRIRE(factorielle(a))                        5
FIN
~~~

## Page 25

~~~text
Rappel: un exemple de fonction
PROGRAMME test_factorielle
FONCTION factorielle(nb : ENTIER) : ENTIER
VARIABLE
       i, res : ENTIER
DÉBUT
       res ← 1                               120
       POUR i DE 2 à nb+1 FAIRE
               res ← res*i
       FIN POUR

       RETOURNER res
FIN

VARIABLE
       a : ENTIER                                  Variable programme principal
DEBUT
       a ← 5                                               a
       ECRIRE(factorielle(a))                              5
FIN
~~~

## Page 26

~~~text
Des boucles partout !
●   La fonction factorielle, comme de très nombreux algorithmes, exploite une boucle explicite
    (TANT QUE, POUR)
~~~

## Page 27

~~~text
Une autre écriture.
●   La fonction factorielle, comme de très nombreux algorithmes, exploite une boucle explicite
    (TANT QUE, POUR)


●   On a par definition 𝑁! = 1 ∗ 2 ∗ 3 … ∗ 𝑁 − 1 ∗ 𝑁. Cette formule peut-être récrite de la manière
    suivante :
                                𝑁! = 𝑁 ∗ 𝑁 − 1 !     𝑎𝑣𝑒𝑐 1! = 1
~~~

## Page 28

~~~text
Une autre écriture
●   La fonction factorielle, comme de très nombreux algorithmes, exploite une boucle explicite
    (TANT QUE, POUR)


●   On a par definition 𝑁! = 1 ∗ 2 ∗ 3 … ∗ 𝑁 − 1 ∗ 𝑁. Cette formule peut-être récrite de la manière
    suivante :
                                 𝑁! = 𝑁 ∗ 𝑁 − 1 !        𝑎𝑣𝑒𝑐 1! = 1




                        Cette relation entre N! et (N-1)! est dites de recurrence.
~~~

## Page 29

~~~text
Les fonctions récursives : définition
●   Une fonction est recursive recursive lorsqu’elle s’apelle elle-même.
●   Elle se base sur des relations de recurrence.
●   Puisqu’elle s’apelle elle-même, certaines instructions seront répétées plusieures fois. Une
    fonction récursive va donc faire office de boucle implicite.
●   Une fonction qui utilise une boucle explicite (POUR, TANT QUE) est dite itérative
~~~

## Page 30

~~~text
Les fonctions récursives : définition
●   Une fonction est recursive recursive lorsqu’elle s’apelle elle-même.
●   Elle se base sur des relations de recurrence.
●   Puisqu’elle s’apelle elle-même, certaines instructions seront répétées plusieures fois. Une
    fonction récursive va donc faire office de boucle implicite.
●   Une fonction qui utilise une boucle explicite (POUR, TANT QUE) est dite itérative


●   Un même algorithme peut avoir une definition recursive ou iterative !


    𝑁! = 𝑁 ∗ 𝑁 − 1 ∗ 𝑁 − 2 ∗ ⋯ ∗ 2 ∗ 1                                     1 𝑠𝑖 𝑁 = 1
                                                               𝑁! = ቊ
                                                                        𝑁 ∗ 𝑁 − 1 ! 𝑠𝑖𝑛𝑜𝑛

              Definition iterative
                                                               Définition récursive
~~~

## Page 31

~~~text
Un exemple complet                                𝑁! = ቊ
                                                              1 𝑠𝑖 𝑁 = 1
                                                           𝑁 ∗ 𝑁 − 1 ! 𝑠𝑖𝑛𝑜𝑛



 // Fonction qui calcule la factorielle d’un nombre
 // Conditions d’appel : nb un entier positif
 FONCTION factorielle(nb : ENTIER) : ENTIER
 VARIABLE
       res : ENTIER // on déclare une variable résultat
 DÉBUT
       SI (nb = 1) ALORS          // cas trivial
             res ← 1
       SINON
         res ← nb * factorielle(nb - 1) // récursivité
       FIN SI
       RETOURNER res // on retourne le résultat
 FIN
~~~

## Page 32

~~~text
Arbre de récursivité.

 ●   Un arbre de récursivité illustre les appels et le retours successif d’une fonction recursive.


 ●   Il permet, entre autre, de comprendre la manière dont fonctionne l’algorithme récursif.


 ●   Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
~~~

## Page 33

~~~text
Arbre de récursivité.
●   Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?




                                                                  FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                  VARIABLE
                                                                           res : ENTIER DÉBUT
                                                                           SI (nb = 1) ALORS
                                                                                     res ← 1
                                                                           SINON
                                                                              res ← nb * factorielle(nb - 1)

                                                                           FIN SI
                                                                           RETOURNER res
                                                                  FIN
~~~

## Page 34

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?




    factorielle(5) ← 5*factorielle(4)                              FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                   VARIABLE
                                                                            res : ENTIER DÉBUT
                                                                            SI (nb = 1) ALORS
                                                                                      res ← 1
                                                                            SINON
                                                                               res ← nb * factorielle(nb - 1)

                                                                            FIN SI
                                                                            RETOURNER res
                                                                   FIN
~~~

## Page 35

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?




    factorielle(5) ← 5*factorielle(4) la fonction a donc besoin         FONCTION factorielle(nb : ENTIER) : ENTIER
                                      du résultat de factorielle(4)     VARIABLE
                                                                                 res : ENTIER DÉBUT
                                      pour renvoyer un résultat!                 SI (nb = 1) ALORS
                                                                                           res ← 1
                                                                                 SINON
                                                                                    res ← nb * factorielle(nb - 1)

                                                                                 FIN SI
                                                                                 RETOURNER res
                                                                        FIN
~~~

## Page 36

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                    FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                    VARIABLE
                                                                             res : ENTIER DÉBUT
                                                                             SI (nb = 1) ALORS
                                                                                       res ← 1
    factorielle(5) ← 5*factorielle(4)                                        SINON
                                                                                res ← nb * factorielle(nb - 1)

                        factorielle(4) ←                                     FIN SI
                                                                             RETOURNER res
                                                                    FIN
~~~

## Page 37

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                    FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                    VARIABLE
                                                                             res : ENTIER DÉBUT
                                                                             SI (nb = 1) ALORS
                                                                                       res ← 1
    factorielle(5) ← 5*factorielle(4)                                        SINON
                                                                                res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                    FIN SI
                                                                             RETOURNER res
                                                                    FIN
~~~

## Page 38

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                    FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                    VARIABLE
                                                                             res : ENTIER DÉBUT
                                                                             SI (nb = 1) ALORS
                                                                                       res ← 1
    factorielle(5) ← 5*factorielle(4)                                        SINON
                                                                                res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                    FIN SI
                                                                             RETOURNER res
                                                                    FIN

                                            factorielle(3) ←
~~~

## Page 39

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                                FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                                VARIABLE
                                                                                         res : ENTIER DÉBUT
                                                                                         SI (nb = 1) ALORS
                                                                                                   res ← 1
    factorielle(5) ← 5*factorielle(4)                                                    SINON
                                                                                            res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                                FIN SI
                                                                                         RETOURNER res
                                                                                FIN

                                            factorielle(3) ← 3*factorielle(2)
~~~

## Page 40

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                                FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                                VARIABLE
                                                                                         res : ENTIER DÉBUT
                                                                                         SI (nb = 1) ALORS
                                                                                                   res ← 1
    factorielle(5) ← 5*factorielle(4)                                                    SINON
                                                                                            res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                                FIN SI
                                                                                         RETOURNER res
                                                                                FIN

                                            factorielle(3) ← 3*factorielle(2)


                                                                 factorielle(2) ←
~~~

## Page 41

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                                FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                                VARIABLE
                                                                                         res : ENTIER DÉBUT
                                                                                         SI (nb = 1) ALORS
                                                                                                   res ← 1
    factorielle(5) ← 5*factorielle(4)                                                    SINON
                                                                                            res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                                FIN SI
                                                                                         RETOURNER res
                                                                                FIN

                                            factorielle(3) ← 3*factorielle(2)


                                                                 factorielle(2) ← 2*factorielle(1)
~~~

## Page 42

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?
                                                                                FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                                VARIABLE
                                                                                         res : ENTIER DÉBUT
                                                                                         SI (nb = 1) ALORS
                                                                                                   res ← 1
    factorielle(5) ← 5*factorielle(4)                                                    SINON
                                                                                            res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                                FIN SI
                                                                                         RETOURNER res
                                                                                FIN

                                            factorielle(3) ← 3*factorielle(2)


                                                                 factorielle(2) ← 2*factorielle(1)


                                                                                        factorielle(1) ←
~~~

## Page 43

~~~text
Arbre de récursivité.
●    Exemple : que se passe-t-il lorsque l’on appelle factorielle (5)?
                                                                                FONCTION factorielle(nb : ENTIER) : ENTIER
                                                                                VARIABLE
                                                                                         res : ENTIER DÉBUT
                                                                                         SI (nb = 1) ALORS
                                                                                                   res ← 1
    factorielle(5) ← 5*factorielle(4)                                                    SINON
                                                                                            res ← nb * factorielle(nb - 1)

                        factorielle(4) ← 4*factorielle(3)                                FIN SI
                                                                                         RETOURNER res
                                                                                FIN

                                            factorielle(3) ← 3*factorielle(2)


                                                                 factorielle(2) ← 2*factorielle(1)


                                                                                        factorielle(1) ← 1
~~~

## Page 44

~~~text
Arbre de récursivité.
●     Exemple : que se passe-t-il lorsque l’on appelle factorielle (5)?




     factorielle(5) ← 5*factorielle(4)


                         factorielle(4) ← 4*factorielle(3)


                                             factorielle(3) ← 3*factorielle(2)


                                                                  factorielle(2) ← 2*factorielle(1)


                                                                                        factorielle(1) ← 1
    On fait remonter les retours succéssifs !
~~~

## Page 45

~~~text
Arbre de récursivité.
●     Exemple : que se passe-t-il lorsque l’on appelle factorielle (5)?




     factorielle(5) ← 5*factorielle(4)


                         factorielle(4) ← 4*factorielle(3)


                                             factorielle(3) ← 3*factorielle(2)


                                                                  factorielle(2) ← 2*factorielle(1) =2


                                                                                       factorielle(1) ← 1
    On fait remonter les retours succéssifs !
~~~

## Page 46

~~~text
Arbre de récursivité.
●     Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?




     factorielle(5) ← 5*factorielle(4)


                         factorielle(4) ← 4*factorielle(3)


                                             factorielle(3) ← 3*factorielle(2) = 6


                                                                  factorielle(2) ← 2*factorielle(1) = 2


                                                                                       factorielle(1) ← 1
    On fait remonter les retours succéssifs !
~~~

## Page 47

~~~text
Arbre de récursivité.
●     Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?




     factorielle(5) ← 5*factorielle(4)


                         factorielle(4) ← 4*factorielle(3) = 24


                                             factorielle(3) ← 3*factorielle(2) = 6


                                                                  factorielle(2) ← 2*factorielle(1) = 2


                                                                                       factorielle(1) ← 1
    On fait remonter les retours succéssifs !
~~~

## Page 48

~~~text
Arbre de récursivité.
●     Exemple : que se passe-t-il lorsque l’on appelle factorielle(5)?




     factorielle(5) ← 5*factorielle(4) = 120


                         factorielle(4) ← 4*factorielle(3) = 24


                                               factorielle(3) ← 3*factorielle(2) = 6


                                                                    factorielle(2) ← 2*factorielle(1) = 2


                                                                                         factorielle(1) ← 1
    On fait remonter les retours succéssifs !
~~~

## Page 49

~~~text
Arbre de récursivité.
●      Arbre de récursivité de factorielle (5):


    factorielle(5) ← 5*factorielle(4) = 120


                        4*factorielle(3) = 24


                              3*factorielle(2) = 6


                                  2*factorielle(1) = 2


                                                1
~~~

## Page 50

~~~text
Composantes d’une fonction récursive
    f(x) = si c(x) alors
                   g(x)
             sinon
                   h(f(s(x)), x)

●   c(x) est dite condition d’arrêt ;
●   g(x) est le cas trivial, il peut retourner une valeur constante ;
●   s(x) est la fonction “successeur” de x ;
●   h(f(s(x)),x) est l’appel récursif, fonction de x et du successeur de x. Si h est la fonction identité, la
    récursivité est dite terminale; non terminale sinon.
~~~

## Page 51

~~~text
Types de récursivité
●   Une fonction récursive peut être simple ou multiple (cf fibonacci) ;
●   Une fonction récursive peut être terminale ou non terminale ;
●   Une fonction récursive peut être croisée ;
●   Dans tous les cas, une fonction récursive doit se terminer !! Il faut définir une bonne condition
    d’arret.
~~~

## Page 52

~~~text
Récursivité non terminale
Une fonction recursive est non terminale lorsqu’il y’ a une opération sur la valeur retounée et pas uniquement
un appel à la fonction.


 FONCTION factorielle(nb : ENTIER) : ENTIER
 DÉBUT
       SI (nb = 0) ALORS           // condition d’arret
             RETOURNER 1          // cas trivial
       SINON
         RETOURNER nb * factorielle(nb - 1) // récursivité
       FIN SI
 FIN
~~~

## Page 53

~~~text
Récursivité terminale
Une fonction recursive est terminale lorsque la valeur retournée est directement la valeur obtenue
par un appel récursif.

 // Conditions : nb un entier positif, acc = 1
 FONCTION factoRT(nb, acc : ENTIER) : ENTIER
 DÉBUT
        SI (nb = 0) ALORS         // cas trivial
               RETOURNER acc
        SINON
          RETOURNER factoRT(nb - 1, acc * nb) // récursivité
        FIN SI
 FIN
 VARIABLE
 nb: ENTIER
 DEBUT
        nb ← 5
        factoRT(nb, 1) // le second paramètres est fixé à 1
 FIN
~~~

## Page 54

~~~text
Arbre de récursivité                                       FONCTION factoRT(nb, acc : ENTIER) : ENTIER
                                                           DÉBUT
                                                                    SI (nb = 0) ALORS
Dessinons l’arbre de récursivité de factoRT(5,1) :                            RETOURNER acc
                                                                    SINON
                                                                       RETOURNER factoRT(nb - 1, acc * nb)
                                                                    FIN SI
                                                           FIN
factoRT(5,1) ← factoRT(4,5)


                    factoRT(3,20)


                          factoRT(2,60)


                              factoRT(1,120)


                                          factoRT(0,120)



                                               120
~~~

## Page 55

~~~text
Arbre de récursivité
Dessinons l’arbre de récursivité de factoRT(5,1) :



factoRT(5,1) ← factoRT(4,5)

                                                           La récursivité terminale permet d’obtenir le résultat
                    factoRT(3,20)                          souhaité au dernier appel de la fonction : pas besoin de
                                                           “remonter” les résultats.

                          factoRT(2,60)                    La récursivité terminale est donc plus performante.


                              factoRT(1,120)


                                          factoRT(0,120)



                                               120
~~~

## Page 56

~~~text
Récursivité multiple
• La récursivité d’une fonction est multiple lorsqu’elle comporte plusieurs invocations
  récursives.


• Exemple: la suite de Fibonacci
  la suite de Fibonacci est une suite dans laquelle chaque terme est la somme des deux
termes qui le précèdent.


                                         0 𝑠𝑖 𝑛 = 0
                            𝐹 𝑛 =ቐ       1 𝑠𝑖 𝑛 = 1
                                  𝐹 𝑛 − 1 + 𝐹 𝑛 − 2 𝑠𝑖𝑛𝑜𝑛
~~~

## Page 57

~~~text
Fibonacci non terminale
// ATTENTION ! Les versions non terminales des récursions peuvent
poser des problèmes de performance
FONCTION fibo(nb : ENTIER) : ENTIER
DÉBUT
      SI (nb < 2) ALORS          // cas trivial
            RETOURNER nb
      SINON
        RETOURNER fibo(nb - 1) + fibo(nb - 2)    // récursivité
      FIN SI
FIN
~~~

## Page 58

~~~text
                                                                   FONCTION fibo(nb : ENTIER) : ENTIER
 Fibonacci non terminale                                           DÉBUT
                                                                           SI (nb < 2) ALORS
         Arbre de récursivité de fibo(5):                                          RETOURNER nb
                                                                           SINON
                                                                              RETOURNER fibo(nb - 1) + fibo(nb - 2)
                      fibo(5)← fibo(4)+fibo(3)                                FIN SI
                                                                   FIN

                   fibo(3)+fibo(2)
                                                       fibo(2)+fibo(1)

        fibo(2)+fibo(1)      fibo(1)+fibo(0)     fibo(1)+fibo(0)     1


fibo(1)+fibo(0)   1           1        0          1        0


 1        0
~~~

## Page 59

~~~text
Fibonacci terminale
FONCTION fiboRT(nb, fnm2, fnm1 : ENTIER) : ENTIER
DÉBUT
      SI (nb = 0) ALORS          // cas trivial
            RETOURNER fnm2
      SINON
        RETOURNER fiboRT(nb - 1, fnm1, fnm1 + fnm2)   //récursivité
      FIN SI
FIN


FONCTION fibo(nb : ENTIER) : ENTIER
DÉBUT
      RETOURNER fiboRT(nb, 0, 1)
FIN
~~~

## Page 60

~~~text
Fibonacci terminale
                                     FONCTION fiboRT(nb, fnm2, fnm1 : ENTIER) : ENTIER
                                     DÉBUT
                                                SI (nb = 0) ALORS
                                                           RETOURNER fnm2
  Arbre de récursivité de fibo(5):              SINON
                                                    RETOURNER fiboRT(nb - 1, fnm1, fnm1 + fnm2)

                                               FIN SI
            fibo(5)←fiboRT(5,0,1)    FIN


                                     FONCTION fibo(nb : ENTIER) : ENTIER
                  fiboRT(4,1,1)      DÉBUT
                                                RETOURNER fiboRT(nb, 0, 1)
                                     FIN

                  fiboRT(3,1,2)


                  fiboRT(2,2,3)

                  fiboRT(1,3,5)


                  fiboRT(0,5,8)


                        5
~~~

## Page 61

~~~text
Problème de terminaison
// Cet algorithme se termine-t-il ?
FONCTION exemple1(n : ENTIER) : ENTIER
DÉBUT
    SI (n = 0) ALORS
        RETOURNER 1
    SINON
        RETOURNER n * exemple1(n‐2)
    FIN SI
FIN


Si n est impair, la fonction ne finis jamais!
~~~

## Page 62

~~~text
Problème de terminaison
// Cet algorithme se termine-t-il ?
FONCTION exemple2(n : REEL) : REEL
DÉBUT
    SI (n = 0) ALORS
        RETOURNER 1
    SINON
            RETOURNER exemple2(n/2)
    FIN SI
FIN


n va tendre vers 0 mais ne l’atteind pas !
~~~

## Page 63

~~~text
Récursivité croisée
// ATTENTION ! Ici encore aux problèmes de terminaison
FONCTION estPair(nb : ENTIER) : BOOLEEN
DÉBUT
         SI (nb = 0) ALORS           // cas trivial
                   RETOURNER VRAI
         FIN SI
         SI (nb = 1) ALORS           // cas trivial
                   RETOURNER FAUX
         FIN SI
            RETOURNER estImpair(nb - 1)       // récursivité
         FIN SI
FIN

FONCTION estImpair(nb : ENTIER) : BOOLEEN
DÉBUT
         SI (nb = 1) ALORS           // cas trivial
                   RETOURNER VRAI
         FIN SI
         SI (nb = 0) ALORS           // cas trivial
                   RETOURNER FAUX
         FIN SI
            RETOURNER estPair(nb - 1)         // récursivité
         FIN SI
FIN
~~~

## Page 64

~~~text
Récursivité croisée                        FONCTION estPair(nb : ENTIER) : BOOLEEN
                                           DÉBUT
                                                      SI (nb = 0) ALORS
   Arbre de récursivité de estPair(5):                           RETOURNER VRAI
                                                      FIN SI
                                                      SI (nb = 1) ALORS
                                                                 RETOURNER FAUX
                                                      FIN SI
                                                          RETOURNER estImpair(nb - 1)
              estPaire(5)← estImpair(4)
                                           FIN

                                           FONCTION estImpair(nb : ENTIER) : BOOLEEN
                            estPair(3)     DÉBUT
                                                      SI (nb = 1) ALORS
                                                                 RETOURNER VRAI
                                                      FIN SI
                            estImpair(2)              SI (nb = 0) ALORS
                                                                 RETOURNER FAUX
                                                      FIN SI
                                                          RETOURNER estPair(nb - 1)
                            estPair(1)     FIN



                             FAUX
~~~

## Page 65

~~~text
Boucle explicite ou récursivité ?
• Les boucles explicites c’est pratique mais …

     o   Il existe des énoncés qui sont par essence récursif : cf les tours de Hanoï, le démineur, ... ;

     o   Il existe des objets mathématiques récursifs : les suites, les fractales, les chaînes de Markov... ;

     o   Il existe des objets informatiques récursifs : les listes chaînées, piles, files ;

     o   On peut exprimer naturellement des problèmes sous forme récursive :                  n! = n * (n-1)!
~~~

## Page 66

~~~text
Boucle explicite ou récursivité ?

•   Les boucles explicites c’est pratique mais …

      o   Il existe des énoncés qui sont par essence récursif.




      o Il existe de nombreux cas où la récursivité est plus efficace (plus rapide) que la version itérative :
          parcours d’arbre, recursivité multiple … Mais ce n’est pas toujours le cas ! Les fonctions recursives non-
          terminales sont généralement similaires en terme de rapidité à leur equivalent iterative.
~~~

## Page 67

~~~text
Avantages et inconvénients
●   Intuitive et économique pour le programmeur
     ○   compacte et élégante, facile à analyser
     ○   proche des mathématiques (cela devrait être un avantage pour vous !)
     ○   adapté aux structures de données récursives (cf listes chaînées au 2nd semestre)
●   Peut-être coûteuse pour la machine
     ○   Sauvegarde des résultats intermédiaires, peut être dépassée (stack overflow)
     ○   utilisation de la récursivité terminale (pas toujours possible)
●   Tout algorithme récursif peut être exprimé sous forme itérative (pas toujours simplement…)
~~~
