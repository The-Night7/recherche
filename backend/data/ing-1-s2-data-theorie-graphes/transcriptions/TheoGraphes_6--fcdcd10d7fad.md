# TheoGraphes_6.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1EndE9QDgQ9Gfb7_wn-vYSK-Zk0FfnWfn) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 3, 9, 63.

## Page 1

~~~text
Théorie des graphes

Maria Malek, Romain Dujol

      CY Tech – ING1-MA




        2025 – 2026




   Maria Malek, Romain Dujol   1
~~~

## Page 2

~~~text
Graphes bipartis et problèmes d’affectation


  Graphes bipartis
     Rappels
     Couplage
     Transversal
     Théorème de König


  Problèmes d’affectation
     Modélisation
     Méthode « hongroise »


  Problèmes de planification
     Rappels
     Problème de planification
     Application



                     Maria Malek, Romain Dujol   146
~~~

## Page 3

![Fac-similé de la page 3](../facsimiles/da74555239bdd4976573e68d.jpg)

~~~text
Graphes bipartis
~~~

**Lecture OCR à contrôler**

~~~text
& TECH

Graphes bipartis

& UNIVERSITÉ
~~~

## Page 4

~~~text
Rappels
  Définition (Graphe biparti G = (V1 , V2 , E))
  (V1 , V2 ) partition de V telle que :
          ∀e ∈ E, e a une extrêmité dans V1 et l’autre dans V2

  Définition (Graphe biparti complet Kn1 ,n2 (n1 ≥ 1,
  n2 ≥ 1))
  Graphe simple Kn1 ,n2 = (J1, n1 K , Jn1 + 1, n1 + n2 K , E) contenant
  toutes les arêtes possibles pour un graphe biparti :
                     ∀(v1 , v2 ) ∈ V1 × V2 , v1 v2 ∈ E

                               A
                                            D
                               B
                                             E
                               C
                                    K3,2
                         Maria Malek, Romain Dujol                        148
~~~

## Page 5

~~~text
Couplage

  Définition (Couplage de G = (V, E))
  Sous-ensemble C de E tel que deux arêtes de C n’aient jamais
  de sommet en commun.
  Couplage maximal ≡ Couplage maximal en nombre d’arêtes
  Couplage complet ou parfait ≡ couplage dont le
  sous-graphe engendré est couvrant
  Remarque       C couplage parfait =⇒ C couplage maximal
     A
                 D
                        ▶ {AD, BE} est un couplage de K3,2
     B
                        ▶ K3,2 n’admet pas de couplage
                 E        parfait.
     C
          K3,2


                     Maria Malek, Romain Dujol               149
~~~

## Page 6

~~~text
Transversal


  Définition (Transversal de G = (V, E))
  Sous-ensemble T de V tel que toute arête de E soit incidente
  à un sommet de T.
  Transversal minimal ≡ Transversal minimal en nombre de
  sommets

     A
                 D
     B                  ▶ {A, B, C} est un transversal de K3,2
                        ▶ {D, E} est un transversal de K3,2
                 E
     C
          K3,2



                     Maria Malek, Romain Dujol                   150
~~~

## Page 7

~~~text
Dualité faible




  Théorème
  Soit G un graphe non orienté.

     ∀C couplage de G, ∀T transversal de G, card C ≤ card T


  Démonstration.
  Soit C un couplage de G et T un transversal de G.
  Alors chaque sommet de T est extrémité d’au plus une arête
  de C. Donc card C ≤ card T.




                     Maria Malek, Romain Dujol                151
~~~

## Page 8

~~~text
Dualité forte : théorème de König

  Théorème (König, 1931)
  Soit G un graphe biparti.

    ∀C couplage maximal de G, ∀T transversal minimal de G,
                                                  card C = card T


     A
                 D      ▶ Couplage maximal de K3,2 : {AD, BE}
     B                    (non unique : {BD, CE} est maximal)
                        ▶ Transversal minimal de K3,2 : {D, E}
                 E
                          (unique)
     C
          K3,2


                      Maria Malek, Romain Dujol                     152
~~~

## Page 9

![Fac-similé de la page 9](../facsimiles/157df5fe2ad24db5566fb3eb.jpg)

~~~text
Problèmes d’affectation
~~~

**Lecture OCR à contrôler**

~~~text
& TECH

Problèmes d'affectation

& UNIVERSITÉ
~~~

## Page 10

~~~text
Problème d’affectation


  Définition (Problème d’affectation)
  Soit G = (V1 , V2 , E, w) un graphe biparti complet valué tel que
  card V1 = card V2 .
  Un problème d’affectation sur G est la recherche d’un
  couplage parfait C tel que ∑ w(e) soit minimal.
                               e∈C

  Applications
  On cherche à affecter n agents à n tâches :
   ▶ V1 est l’ensemble des n agents.
   ▶ V2 est l’ensemble des n tâches à réaliser.
   ▶ w({x1 , x2 }) est le coût d’affectation de l’agent x1 à la tache
     x2 .




                       Maria Malek, Romain Dujol                   154
~~~

## Page 11

~~~text
Problème d’affectation

  Définition (Matrice d’affectation de G = (V1 , V2 , E, w))
  Matrice carrée A d’ordre n = card V1 = card V2 telle que :
                                                      
                                               (1) (2)
                  ∀(i, j) ∈ J1, nK2 , aij = w vi vj

               (1)                   (2)
  avec V1 = {vi }1≤i≤n et V2 = {vi }1≤i≤n .

  Lien avec l’optimisation linéaire
  xij : affectation (ou non) de l’agent no i à la tâche no j
                               n n
                          min ∑ ∑ aij xij
                          
                          
                          
                          
                          
                              i=1 i=1
                          
                                n                 n
                     =⇒
                          
                          
                              ∑ xij = 1 , ∑ xij = 1
                          
                              i=1                j=1
                          
                                             2
                               ∀(i, j) ∈ J1, nK , xij ∈ {0, 1}
                          



                          Maria Malek, Romain Dujol              155
~~~

## Page 12

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :




                      Maria Malek, Romain Dujol          156
~~~

## Page 13

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;




                      Maria Malek, Romain Dujol          156
~~~

## Page 14

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.




                      Maria Malek, Romain Dujol          156
~~~

## Page 15

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation




                      Maria Malek, Romain Dujol            156
~~~

## Page 16

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré




                      Maria Malek, Romain Dujol               156
~~~

## Page 17

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré
   2. Barrer tous les autres « 0 » sur la même ligne et sur la
      même colonne que le « 0 » encadré




                      Maria Malek, Romain Dujol                  156
~~~

## Page 18

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré
   2. Barrer tous les autres « 0 » sur la même ligne et sur la
      même colonne que le « 0 » encadré
   3. Revenir à l’étape 1 tant qu’il y a des modifications.




                       Maria Malek, Romain Dujol                 156
~~~

## Page 19

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré
   2. Barrer tous les autres « 0 » sur la même ligne et sur la
      même colonne que le « 0 » encadré
   3. Revenir à l’étape 1 tant qu’il y a des modifications.
   4. Y a-t-il un unique « 0 » encadré par ligne et par colonne ?




                       Maria Malek, Romain Dujol                 156
~~~

## Page 20

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré
   2. Barrer tous les autres « 0 » sur la même ligne et sur la
      même colonne que le « 0 » encadré
   3. Revenir à l’étape 1 tant qu’il y a des modifications.
   4. Y a-t-il un unique « 0 » encadré par ligne et par colonne ?
                Oui Affectation valide → STOP




                       Maria Malek, Romain Dujol                 156
~~~

## Page 21

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré
   2. Barrer tous les autres « 0 » sur la même ligne et sur la
      même colonne que le « 0 » encadré
   3. Revenir à l’étape 1 tant qu’il y a des modifications.
   4. Y a-t-il un unique « 0 » encadré par ligne et par colonne ?
                Oui Affectation valide → STOP
               Non Affectation non valide → Étape B




                       Maria Malek, Romain Dujol                 156
~~~

## Page 22

~~~text
Algorithme de Kuhn-Munkres ou méthode
« hongroise »
  On part de la matrice d’affectation du graphe puis :
   ▶ on enlève à chaque ligne sa plus petite valeur ;
   ▶ on enlève à chaque colonne sa plus petite valeur.

  Étape A : Vérification de la validité de l’affectation
   1. Rechercher la ligne avec le moins de « 0 » non barrés
      Encadrer le premier « 0 » non barré
   2. Barrer tous les autres « 0 » sur la même ligne et sur la
      même colonne que le « 0 » encadré
   3. Revenir à l’étape 1 tant qu’il y a des modifications.
   4. Y a-t-il un unique « 0 » encadré par ligne et par colonne ?
                Oui Affectation valide → STOP
               Non Affectation non valide → Étape B
  Remarque        On peut remplacer l’étape A pour toute autre
  méthode donnant l’encadrement d’exactement un « 0 » par
  ligne et d’un par colonne.
                       Maria Malek, Romain Dujol                 156
~~~

## Page 23

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice




                   Maria Malek, Romain Dujol   157
~~~

## Page 24

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :




                    Maria Malek, Romain Dujol            157
~~~

## Page 25

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
      1.1 Marquer les lignes ne contenant pas de « 0 » encadré




                      Maria Malek, Romain Dujol                  157
~~~

## Page 26

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée




                      Maria Malek, Romain Dujol                    157
~~~

## Page 27

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée




                      Maria Malek, Romain Dujol                    157
~~~

## Page 28

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.




                      Maria Malek, Romain Dujol                     157
~~~

## Page 29

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.
     L’ensemble cherché sont les lignes NON marquées et les
     colonnes marquées.




                      Maria Malek, Romain Dujol                     157
~~~

## Page 30

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.
      L’ensemble cherché sont les lignes NON marquées et les
      colonnes marquées.
   2. Chercher la plus petite valeur non couverte :




                      Maria Malek, Romain Dujol                     157
~~~

## Page 31

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.
      L’ensemble cherché sont les lignes NON marquées et les
      colonnes marquées.
   2. Chercher la plus petite valeur non couverte :
       ▶ la soustraire à tous les élements non couverts ;




                       Maria Malek, Romain Dujol                    157
~~~

## Page 32

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.
      L’ensemble cherché sont les lignes NON marquées et les
      colonnes marquées.
   2. Chercher la plus petite valeur non couverte :
       ▶ la soustraire à tous les élements non couverts ;
       ▶ l’ajouter aux intersections des lignes et colonnes couvertes.




                       Maria Malek, Romain Dujol                    157
~~~

## Page 33

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.
      L’ensemble cherché sont les lignes NON marquées et les
      colonnes marquées.
   2. Chercher la plus petite valeur non couverte :
       ▶ la soustraire à tous les élements non couverts ;
       ▶ l’ajouter aux intersections des lignes et colonnes couvertes.
   3. → Étape A pour vérifier la validité de la mise à jour




                       Maria Malek, Romain Dujol                    157
~~~

## Page 34

~~~text
Algorithme de Kuhn-Munkres
  Étape B : Mise à jour de la matrice
   1. Déterminer un ensemble minimal de lignes et colonnes
      couvrant tous les « 0 » :
       1.1 Marquer les lignes ne contenant pas de « 0 » encadré
      1.2 Marquer les colonnes contenant un « 0 » barré dans une
           ligne marquée
      1.3 Marquer les lignes contenant un « 0 » encadré dans une
           colonne marquée
      1.4 Revenir à l’étape 1.2 tant qu’il y a des modifications.
      L’ensemble cherché sont les lignes NON marquées et les
      colonnes marquées.
   2. Chercher la plus petite valeur non couverte :
       ▶ la soustraire à tous les élements non couverts ;
       ▶ l’ajouter aux intersections des lignes et colonnes couvertes.
   3. → Étape A pour vérifier la validité de la mise à jour
  Remarque        On peut remplacer l’étape B.1 par n’importe
  quelle méthode donnant un sous-ensemble minimal de
  lignes et colonnes couvrant tous les « 0 ».
                       Maria Malek, Romain Dujol                    157
~~~

## Page 35

~~~text
Algorithme
         de Kuhn-Munkres : exemple
   7 1 3
   5 2 8
   6 9 4
  Matrice initiale




                     Maria Malek, Romain Dujol   158
~~~

## Page 36

~~~text
Algorithme
         de
             Kuhn-Munkres
                          : exemple
   7 1 3         6 0 2
   5 2 8 →  3 0 6 
   6 9 4         2 5 0
  On enlève à chaque ligne sa plus petite valeur.




                      Maria Malek, Romain Dujol     158
~~~

## Page 37

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7 1 3         6 0 2         4 0 2
   5 2 8 →  3 0 6  →  1 0 6 
   6 9 4         2 5 0         0 5 0
  On enlève à chaque colonne sa plus petite valeur.




                     Maria Malek, Romain Dujol        158
~~~

## Page 38

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1   3     6 0 2       4 0 2
  5    2   8 →  3 0 6  →  1 0 6 
   6    9   4      2 5 0      0 5 0


       Étape A




                     Maria Malek, Romain Dujol   158
~~~

## Page 39

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                      
                 4 0 2
       Étape A  1 0 6
                 0 5 0




                    Maria Malek, Romain Dujol   158
~~~

## Page 40

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3      6 0 2      4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4      2 5 0      0 5 0
                      
                 4 0 2
       Étape A  1 0 6
                 0 5 0




                    Maria Malek, Romain Dujol   158
~~~

## Page 41

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3      6 0 2      4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4      2 5 0      0 5 0
                      
                 4 0 2
       Étape A  1 
                   0 6
                 0 5 0




                    Maria Malek, Romain Dujol   158
~~~

## Page 42

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                        
       Étape A  1   0 6
                     
                 0   5 0




                    Maria Malek, Romain Dujol   158
~~~

## Page 43

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                        
       Étape A  1   0 6
                     
                 0   5 0




                    Maria Malek, Romain Dujol   158
~~~

## Page 44

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0   5 0




                    Maria Malek, Romain Dujol        158
~~~

## Page 45

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0   5 0
       Étape B   1. On marque




                     Maria Malek, Romain Dujol       158
~~~

## Page 46

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0   5 0
       Étape B   1. On marque L2




                      Maria Malek, Romain Dujol      158
~~~

## Page 47

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0   5 0
       Étape B   1. On marque L2 puis C2




                      Maria Malek, Romain Dujol      158
~~~

## Page 48

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2     4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0     0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0   5 0
       Étape B   1. On marque L2 puis C2 puis L1 :




                      Maria Malek, Romain Dujol      158
~~~

## Page 49

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0   5 0                                 
                                                   4 0   2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0   6 
                                                   0 5   0




                      Maria Malek, Romain Dujol            158
~~~

## Page 50

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2          4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0          0 5 0
                           
                 4    0 2
                      0 6 ⇒ Affectation non valide
                           
       Étape A  1    
                 0     5 0                                  
                                                      4 0   2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0      6 
                                                      0 5   0
                              
                      4 0 2
                2.  1 0 6 
                      0 5 0
                   Plus petite valeur non couverte : 1




                       Maria Malek, Romain Dujol              158
~~~

## Page 51

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2          4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0          0 5 0
                           
                 4    0 2
                      0 6 ⇒ Affectation non valide
                           
       Étape A  1    
                 0    5  0                              
                                                   4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                            
                     4 0 2             3 0 1
                2.  1 0 6  →  0 0 5 
                     0 5 0             0 5 0
                   Soustraire 1 aux éléments non couverts




                      Maria Malek, Romain Dujol           158
~~~

## Page 52

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2          4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0          0 5 0
                           
                 4    0 2
                      0 6 ⇒ Affectation non valide
                           
       Étape A  1    
                 0     5 0                             
                                                   4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                      4 0 2            3 0 1         3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                      0 5 0            0 5 0         0 6 0
                   Ajouter 1 aux intersections




                     Maria Malek, Romain Dujol          158
~~~

## Page 53

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4        2 5 0      0 5 0
                         
                  4   0 2
                       6 ⇒ Affectation non valide
                         
       Étape A  1    0
                  0      0
                       5                        
                                                   4 0 2
                                                         

       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                      4 0 2         3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                      0 5 0        0 5 0             0 6 0
                       
                 3 0 1
       Étape A 0 0 5 
                 0 6 0




                     Maria Malek, Romain Dujol          158
~~~

## Page 54

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4        2 5 0      0 5 0
                         
                  4   0 2
                       6 ⇒ Affectation non valide
                         
       Étape A  1    0
                  0      0
                       5                        
                                                   4 0 2
                                                         

       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                      4 0 2         3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                      0 5 0        0 5 0             0 6 0
                        
                 3 0 1
       Étape A 0 0 5 
                 0 6 0




                     Maria Malek, Romain Dujol          158
~~~

## Page 55

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4        2 5 0      0 5 0
                          
                  4    0 2
                        6 ⇒ Affectation non valide
                          
       Étape A  1     0
                  0       0
                        5                       
                                                   4 0 2
                                                         

       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                       4 0 2        3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                       0 5 0       0 5 0             0 6 0
                         
                 3 0 1
       Étape A 0    0 5
                 0 6 0




                     Maria Malek, Romain Dujol          158
~~~

## Page 56

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                      6 ⇒ Affectation non valide
                        
       Étape A  1   0
                 0      0
                      5                         
                                                   4 0 2
                                                         

       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                     4 0 2          3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0             0 6 0
                        
                 3   0 1
                        
       Étape A  0   0 5
                     
                 0   6 0




                     Maria Malek, Romain Dujol          158
~~~

## Page 57

~~~text
Algorithme
         de
             Kuhn-Munkres
                        : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                      6 ⇒ Affectation non valide
                        
       Étape A  1   0
                 0      0
                      5                         
                                                   4 0 2
                                                         

       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                     4 0 2          3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0             0 6 0
                        
                 3   0 1
                        
       Étape A  0   0 5
                     
                 0
                    6 0




                     Maria Malek, Romain Dujol          158
~~~

## Page 58

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0    5 
                        0                               
                                                   4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                     4 0 2          3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0             0 6 0
                          
                 3   0   1
                          
       Étape A  0   0
                        5
                 0
                    6   0




                     Maria Malek, Romain Dujol          158
~~~

## Page 59

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0    5 
                        0                               
                                                   4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                     4 0 2          3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0             0 6 0
                          
                 3   0   1
                              ⇒ Affectation valide
       Étape A  0   0
                        5
                 0
                    6   0




                     Maria Malek, Romain Dujol          158
~~~

## Page 60

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0    5 
                        0                               
                                                   4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                   0 5 0
                                                      
                     4 0 2          3 0 1            3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0             0 6 0
                          
                 3   0   1
                              ⇒ Affectation valide
       Étape A  0   0
                        5
                                   Coût :
                 0
                    6   0




                     Maria Malek, Romain Dujol          158
~~~

## Page 61

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0    5 
                        0                                 
                                                    4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                    0 5 0
                                                        
                     4 0 2          3 0 1              3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0               0 6 0
                          
                 3   0   1
                              ⇒ Affectation valide
       Étape A  0   0
                        5
                                   Coût : 1 + 5 + 4 = 10
                 0
                    6   0




                      Maria Malek, Romain Dujol           158
~~~

## Page 62

~~~text
Algorithme
        
           de
            
              Kuhn-Munkres
                       
                           : exemple
   7    1  3       6 0 2       4 0 2
  5    2  8 →  3 0 6  →  1 0 6 
   6    9  4       2 5 0       0 5 0
                        
                 4   0 2
                     0 6 ⇒ Affectation non valide
                        
       Étape A  1   
                 0    5 
                        0                                 
                                                    4 0 2
       Étape B 1. On marque L2 puis C2 puis L1 :  1 0 6 
                                                    0 5 0
                                                        
                     4 0 2          3 0 1              3 0 1
                2.  1 0 6  →  0 0 5  →  0 0 5 
                     0 5 0         0 5 0               0 6 0
                          
                 3   0   1
                              ⇒ Affectation valide
       Étape A  0   0
                        5
                                   Coût : 1 + 5 + 4 = 10
                 0
                    6   0

  Théorème (Kuhn, 1955 ; Munkres 1957)
  L’algorithme de Kuhn-Munkres le problème d’affectation en
  un temps polynômial.
                      Maria Malek, Romain Dujol           158
~~~

## Page 63

![Fac-similé de la page 63](../facsimiles/b9e330cf147a50601cbae964.jpg)

~~~text
Problèmes de planification
~~~

**Lecture OCR à contrôler**

~~~text
S TECH

Problèmes de planification

& UNIVERSITÉ
~~~

## Page 64

~~~text
Coloration des arêtes

  Définition (Coloration des arêtes de G = (V, E))
  Application c1 : E 7→ C (C ensemble de couleurs)
  Coloration des arêtes c1 propre :
  ∀(e, e′ ) ∈ E2 , e et e′ ont une extrémité commune ⇒ c1 (e) ̸= c1 (e′ )
  Définition (Graphe G = (V, E) colorable pour les
  arêtes)
  c1 k-coloration pour les arêtes ⇐⇒ card c1 (E) = k
  G k-colorable pour les arêtes
       ⇐⇒ ∃ k-coloration pour les arêtes propre de G
  Définition (Indice chromatique de G = (V, E))
  χ1 (G) = min{card c1 (E), c1 coloration propre des arêtes de G}
  Coloration des arêtes propre optimale
      ≡ χ1 (G)-coloration des arêtes propre


                        Maria Malek, Romain Dujol                     160
~~~

## Page 65

~~~text
Coloration des arêtes

  Propriété
  Soit G = (V, E) un graphe et ∆ = max{d(v), v ∈ V}.
  Alors χ1 (G) ≥ ∆

  Démonstration.
  Si d(v) = ∆, alors il faut au moins ∆ couleurs pour les arêtes
  incidentes en v.

  Théorème (König, 1916)
  Soit G = (V, E) un graphe biparti simple et ∆ = max{d(v), v ∈ V}.
  Alors χ1 (G) = ∆

  Théorème (Vizing, 1964)
  Soit G = (V, E) un graphe simple et ∆ = max{d(v), v ∈ V}.
  Alors χ1 (G) ≤ ∆ + 1
  Remarque        G simple =⇒ χ1 (G) ∈ {∆, ∆ + 1}


                       Maria Malek, Romain Dujol                   161
~~~

## Page 66

~~~text
Problème de planification

  Problématique
  Comment répartir des cours sur la période la plus courte
  possible ? (On fait l’hypothèse que tous les cours ont la
  même durée.)

  Modélisation par un graphe biparti G = (V1 , V2 , E)
   ▶ V1 : ensemble des enseignants
   ▶ V2 : ensemble des classes
   ▶ E : ensemble des cours (associations enseignant-classe)
  ⇒ Créneau horaire d’un emploi du temps ≡ couplage de G
  Définition (Emploi du temps T de G = (V1 , V2 , E))
  Partition (Ci )1≤i≤p de E telle que ∀i ∈ J1, pK , Ci couplage de G
  p : nombre de créneaux de T
  Remarque         T induit une coloration propre des arêtes de
  G.
  Objectif     Trouver T = (Ci )1≤i≤p tel que p soit minimal.

                        Maria Malek, Romain Dujol                      162
~~~

## Page 67

~~~text
Ajout de la contrainte des salles

  Problématique
  On suppose que le nombre de salles est limité.

  Définition (Emploi du temps de G = (V1 , V2 , E) à s
  salles)
  Emploi du temps T = (Ci )1≤i≤p tel que ∀ ∈ J1, pK , card Ci ≤ s

  Propriété (Nombre minimal d’heures)
  G = (V1 , V2 , E) graphe biparti et ∆ = max{d(v), v ∈ V1 ∪ V2 }.
  Le plus petit nombre de créneaux
                                       d’un
                                             emploi du temps de
                                     card E
  G à s salles est pmin = max ∆,              .
                                       s

  Remarque
        
        card E
  ∆≥           ⇒ contrainte de salles inutile
          s


                       Maria Malek, Romain Dujol                    163
~~~

## Page 68

~~~text
Existence d’emploi du temps équilibré


  Définition (Emploi du temps équilibré)
  Emploi du temps T = (Ci )1≤i≤p tel que

                ∀(i, j) ∈ J1, pK , | card Ci − card Cj | ≤ 1
                                                          
                               card E                 card E
  Remarque       ∀i ∈ J1, pK ,          ≤ card Ci ≤
                                 p                      p



  Pourquoi chercher des emplois de temps
  équilibrés ?
  On cherche à utiliser au maximum les salles disponibles à
  chaque créneau. =⇒ On doit éviter les emplois trop
  « disparates ».



                       Maria Malek, Romain Dujol                 164
~~~

## Page 69

~~~text
Existence d’emploi du temps équilibré


  Lemme (Existence d’emploi du temps équilibré)
  G = (V1 , V2 , E) graphe biparti et ∆ = max{d(v), v ∈ V1 ∪ V2 }.
  ∀p ≥ ∆, ∃ emploi du temps équilibré à p créneaux

  Démonstration.
  Soit T = (Ci )1≤i≤p un emploi du temps quelconque à p
  créneaux (existencenassurée par le théorème de König).          o
  Soit (i1 , j1 ) = argmax | card Ci − card Cj |, (i, j) ∈ J1, pK2 .
  On échange les appartenances des arêtes de Ci1 et Cj1 dans
  les chaînes de Ci1 ∪ Cj1 de longueur impaire jusqu’à ce que
  | card Ci1 − card Cj1 | ≤ 1.
  On recommence l’opération jusqu’à équilibrer l’emploi du
  temps dans son ensemble.




                        Maria Malek, Romain Dujol                      165
~~~

## Page 70

~~~text
Application

  Exemple traité

              1     ▶ card V1 = 4, card V2 = 5
    A               ▶ card E = 13
                    ▶ s=3
              2                   
                                    13
                   =⇒ pmin = max 4,    = max(4, 5) = 5
    B                               3
              3
                   Emploi du temps T = (Ci )1≤i≤5 équilibré :

                              ∀i ∈ J1, 5K , 2 ≤ card Ci ≤ 3
    C         4
                   Remarque
    D         5    Contrainte de salles inutile pour s ≥ 4



                   Maria Malek, Romain Dujol                  166
~~~

## Page 71

~~~text
Application

  Construction de l’emploi du temps initial
  On constitue la partition T = (C1 , C2 , C3 , C4 , C5 ) avec :

                   1
     A
                   2      ▶ C1 = {A1, B2, C3, D4} (bleu)
                          ▶ C2 = {A2, B3, C4, D5} (rouge)
     B
                          ▶ C3 = {A2, B1, C5} (marron)
                   3      ▶ C4 = {C2, D5} (vert)
                          ▶ C5 = 0/ (noir)
     C            4     =⇒ Emploi du temps non équilibré


     D             5


                         Maria Malek, Romain Dujol                 167
~~~

## Page 72

~~~text
Application

  Première itération : C1 (4 arêtes) et C5 (0 arête)

              1                                        1
   A                                            A
              2                                        2
   B                                            B
              3             −→                         3


   C         4                                  C      4


   D          5                                 D      5



                    Maria Malek, Romain Dujol              168
~~~

## Page 73

~~~text
Application

  Seconde itération : C2 (4 arêtes) et C4 (2 arêtes)

              1                                        1
   A                                           A
              2                                    2
   B                                           B
              3            −→                      3


   C         4                                 C   4


   D          5                                D   5



                   Maria Malek, Romain Dujol               169
~~~

## Page 74

~~~text
Application


  Terminaison
              1
   A                      Ci       C1    C2       C3       C4   C5
                        card Ci    2     3        3        3    2
              2
   B              ⇒ Emploi du temps équilibré à 3 salles :
              3                    1    2     3        4    5
                             C1    A    B
                             C2         C     B             D
   C       4                 C3    B    A                   C
                             C4         A              C    D
                             C5               C        D
   D          5



                  Maria Malek, Romain Dujol                          170
~~~
