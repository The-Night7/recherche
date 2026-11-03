# Slides3-Compressive-Sensing23.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1yUr4Wl8qK4aRQpBhrrmG_hhGuab7KjJU) · Les deux lectures automatiques du PDF divergent sur les pages indiquées. Leur fac-similé accompagne le texte.

**Pages présentant un écart entre les deux extractions** — 4–8, 11–13, 16, 21–26, 28–34, 36–39, 41–54, 59–60.

## Page 1

~~~text
                   Dictionnaire
Apprentissage d’un dictionnaire
            Algorithme k-SVD




      Compressive Sensing
 Apprentissage d’un dictionnaire

                         CY TECH


                         2022-2023




                    CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 2

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD




1   Dictionnaire


2   Apprentissage d’un dictionnaire


3   Algorithme k-SVD




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 3

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Propriétés de base




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 4

![Page 4 du PDF](../facsimiles/a19e6c45dab9ddd28d0167e7.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Propriétés de base


      Un dictionnaire est défini par une matrice D ∈ MN,K (R) où
      chaque colonne est appelé atome.




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 5

![Page 5 du PDF](../facsimiles/37bb0f3dc5a00e54eda7200c.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Propriétés de base


      Un dictionnaire est défini par une matrice D ∈ MN,K (R) où
      chaque colonne est appelé atome.
      On note D = (d1 |d2 |...|dK ), où les di sont les atomes du
      dictionnaire.




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 6

![Page 6 du PDF](../facsimiles/9ae58b1ef37a0d4cf33b463d.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Propriétés de base


      Un dictionnaire est défini par une matrice D ∈ MN,K (R) où
      chaque colonne est appelé atome.
      On note D = (d1 |d2 |...|dK ), où les di sont les atomes du
      dictionnaire.
      Les atomes sont des vecteurs de RN .




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 7

![Page 7 du PDF](../facsimiles/81db35bf31b360f17af4e14e.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Propriétés de base


      Un dictionnaire est défini par une matrice D ∈ MN,K (R) où
      chaque colonne est appelé atome.
      On note D = (d1 |d2 |...|dK ), où les di sont les atomes du
      dictionnaire.
      Les atomes sont des vecteurs de RN .
      Toute combinaison linéaire de ces atomes donne un vecteur
      x ∈ RN :
                    x = α1 d1 + α2 d2 + ... + αK dK .




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 8

![Page 8 du PDF](../facsimiles/7a47ed5ce87d82f2bc83fcfa.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Propriétés de base


      Un dictionnaire est défini par une matrice D ∈ MN,K (R) où
      chaque colonne est appelé atome.
      On note D = (d1 |d2 |...|dK ), où les di sont les atomes du
      dictionnaire.
      Les atomes sont des vecteurs de RN .
      Toute combinaison linéaire de ces atomes donne un vecteur
      x ∈ RN :
                    x = α1 d1 + α2 d2 + ... + αK dK .


      Autrement dit : x = Dα.


                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 9

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Choix d’un dictionnaire




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 10

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Choix d’un dictionnaire


      Le choix du dictionnaire D a une très grande influence sur la
      représentation α.




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 11

![Page 11 du PDF](../facsimiles/ae40ab9b03a77ed65d54aad3.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Choix d’un dictionnaire


      Le choix du dictionnaire D a une très grande influence sur la
      représentation α.
      Si les colonnes (atomes) de D ne correpsondent pas aux
      propriétés des signaux, leur représentation ne sera pas
      parcimonieuse.




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 12

![Page 12 du PDF](../facsimiles/4d61c1bf3d968fbf9be78a89.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Choix d’un dictionnaire


      Le choix du dictionnaire D a une très grande influence sur la
      représentation α.
      Si les colonnes (atomes) de D ne correpsondent pas aux
      propriétés des signaux, leur représentation ne sera pas
      parcimonieuse.
      Plusieurs dictionnaires peuvent être adaptés à une famille de
      signaux.




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 13

![Page 13 du PDF](../facsimiles/f1670f231235bb946330b4c6.webp)

~~~text
                                 Dictionnaire
              Apprentissage d’un dictionnaire
                          Algorithme k-SVD


Choix d’un dictionnaire


      Le choix du dictionnaire D a une très grande influence sur la
      représentation α.
      Si les colonnes (atomes) de D ne correpsondent pas aux
      propriétés des signaux, leur représentation ne sera pas
      parcimonieuse.
      Plusieurs dictionnaires peuvent être adaptés à une famille de
      signaux.
      Il y a donc plusieurs méthodes de construction de
      dictionnaires adaptés.




                                  CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 14

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Construction d’un dictionnaire




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 15

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Construction d’un dictionnaire


  Il y a essentiellement 2 manières de construire un dictionnaire
  adapté à une famille de signaux :




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 16

![Page 16 du PDF](../facsimiles/bb299a250d9658d95e305345.webp)

~~~text
                                   Dictionnaire
                Apprentissage d’un dictionnaire
                            Algorithme k-SVD


Construction d’un dictionnaire


  Il y a essentiellement 2 manières de construire un dictionnaire
  adapté à une famille de signaux :
    1   Soit on dispose de connaissances a priori sur les signaux :
        répartition fréquentielle, temporelle, etc.




                                    CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 17

~~~text
                                   Dictionnaire
                Apprentissage d’un dictionnaire
                            Algorithme k-SVD


Construction d’un dictionnaire


  Il y a essentiellement 2 manières de construire un dictionnaire
  adapté à une famille de signaux :
    1   Soit on dispose de connaissances a priori sur les signaux :
        répartition fréquentielle, temporelle, etc. Et on peut alors
        construire des dictionnaires de type Fourier ou cosinus ou
        sinus discrets, ou ondelettes qui exploitent cette connaissance.




                                    CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 18

~~~text
                                   Dictionnaire
                Apprentissage d’un dictionnaire
                            Algorithme k-SVD


Construction d’un dictionnaire


  Il y a essentiellement 2 manières de construire un dictionnaire
  adapté à une famille de signaux :
    1   Soit on dispose de connaissances a priori sur les signaux :
        répartition fréquentielle, temporelle, etc. Et on peut alors
        construire des dictionnaires de type Fourier ou cosinus ou
        sinus discrets, ou ondelettes qui exploitent cette connaissance.
    2   Soit on dispose d’une famille de signaux que l’on va utuiliser
        pour apprendre (construire) un dictionnaire adapté.




                                    CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 19

~~~text
                                   Dictionnaire
                Apprentissage d’un dictionnaire
                            Algorithme k-SVD


Construction d’un dictionnaire


  Il y a essentiellement 2 manières de construire un dictionnaire
  adapté à une famille de signaux :
    1   Soit on dispose de connaissances a priori sur les signaux :
        répartition fréquentielle, temporelle, etc. Et on peut alors
        construire des dictionnaires de type Fourier ou cosinus ou
        sinus discrets, ou ondelettes qui exploitent cette connaissance.
    2   Soit on dispose d’une famille de signaux que l’on va utuiliser
        pour apprendre (construire) un dictionnaire adapté. On
        exploite pour cela le critère de parcimonie.




                                    CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 20

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Principe général 1




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 21

![Page 21 du PDF](../facsimiles/e1359eba54d3680f6f5b19ff.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 1

       A partir d’une famille de ` signaux regroupés dans une matrice
       X = (X (1) |X (2) |, ...|X (`) |) ∈ MN,` (R)




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 22

![Page 22 du PDF](../facsimiles/e85e4a8e91b61780ecc55ecc.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 1

       A partir d’une famille de ` signaux regroupés dans une matrice
       X = (X (1) |X (2) |, ...|X (`) |) ∈ MN,` (R) et d’un dictionnaire
       initial quelconque D (0) ∈ MN,K (R),




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 23

![Page 23 du PDF](../facsimiles/c14a4ee04b1d575c1fe41c22.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 1

       A partir d’une famille de ` signaux regroupés dans une matrice
       X = (X (1) |X (2) |, ...|X (`) |) ∈ MN,` (R) et d’un dictionnaire
       initial quelconque D (0) ∈ MN,K (R), on va construire un
       dictionnaire D adapté à tous nos signaux.




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 24

![Page 24 du PDF](../facsimiles/b0d6d0aa6d77c6b4ad44d23a.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 1

       A partir d’une famille de ` signaux regroupés dans une matrice
       X = (X (1) |X (2) |, ...|X (`) |) ∈ MN,` (R) et d’un dictionnaire
       initial quelconque D (0) ∈ MN,K (R), on va construire un
       dictionnaire D adapté à tous nos signaux.
       Le calcul de la représentation parcimonieuse α(j) de chaque
       X (j) donnera X (j) = Dα(j) .




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 25

![Page 25 du PDF](../facsimiles/9d60971e6703c4bf1fcc6b03.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 1

       A partir d’une famille de ` signaux regroupés dans une matrice
       X = (X (1) |X (2) |, ...|X (`) |) ∈ MN,` (R) et d’un dictionnaire
       initial quelconque D (0) ∈ MN,K (R), on va construire un
       dictionnaire D adapté à tous nos signaux.
       Le calcul de la représentation parcimonieuse α(j) de chaque
       X (j) donnera X (j) = Dα(j) .
       On regroupe toutes ces représentations dans une matrice :

                                  Λ = (α(1) |α(2) |...|α(`) ).




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 26

![Page 26 du PDF](../facsimiles/8621c6276a165dcb0f79bbca.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 1

       A partir d’une famille de ` signaux regroupés dans une matrice
       X = (X (1) |X (2) |, ...|X (`) |) ∈ MN,` (R) et d’un dictionnaire
       initial quelconque D (0) ∈ MN,K (R), on va construire un
       dictionnaire D adapté à tous nos signaux.
       Le calcul de la représentation parcimonieuse α(j) de chaque
       X (j) donnera X (j) = Dα(j) .
       On regroupe toutes ces représentations dans une matrice :

                                  Λ = (α(1) |α(2) |...|α(`) ).


       On pourrait donc écrire : X = DΛ.


                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 27

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Principe général 2




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 28

![Page 28 du PDF](../facsimiles/113db5b97b2f90ec8a7a51af.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 29

![Page 29 du PDF](../facsimiles/0e8c8ab82608b54aff5cad3c.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :


   minkX − DΛkF sous les contraintes kα(j) k0 ⩽ s et kdj k2 = 1.
   D,Λ




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 30

![Page 30 du PDF](../facsimiles/6b04d9b6b51b6e0ae8163d63.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :


   minkX − DΛkF sous les contraintes kα(j) k0 ⩽ s et kdj k2 = 1.
   D,Λ


  où s traduit la contrainte de parcimonie,




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 31

![Page 31 du PDF](../facsimiles/9e065a8954714fd55e634e2a.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :


   minkX − DΛkF sous les contraintes kα(j) k0 ⩽ s et kdj k2 = 1.
   D,Λ


  où s traduit la contrainte de parcimonie, kdj k2 = 1 indique des
  atomes unitaires




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 32

![Page 32 du PDF](../facsimiles/43d0bddda345b1e1da97c48e.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :


   minkX − DΛkF sous les contraintes kα(j) k0 ⩽ s et kdj k2 = 1.
   D,Λ


  où s traduit la contrainte de parcimonie, kdj k2 = 1 indique des
  atomes unitaires et k.kF est la norme matricielle de Frobenius




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 33

![Page 33 du PDF](../facsimiles/d5fdbc812639b44f0b98989e.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :


   minkX − DΛkF sous les contraintes kα(j) k0 ⩽ s et kdj k2 = 1.
   D,Λ


  où s traduit la contrainte de parcimonie, kdj k2 = 1 indique des
  atomes unitaires et k.kF est la norme matricielle de Frobenius qui
  est la plus adaptée à l’algorithme qui suit.




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 34

![Page 34 du PDF](../facsimiles/fb2653c8294e8889d115205e.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général 2

  Le dictionnaire recherché est donc solution du problème suivant :


   minkX − DΛkF sous les contraintes kα(j) k0 ⩽ s et kdj k2 = 1.
   D,Λ


  où s traduit la contrainte de parcimonie, kdj k2 = 1 indique des
  atomes unitaires et k.kF est la norme matricielle de Frobenius qui
  est la plus adaptée à l’algorithme qui suit.
  Rappel :                          v
                                    u N `
                                    uX X
                          kAkF = t            |aij |2 .
                                                 i=1 j=1



                                   CY TECH         Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 35

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Principe général du k-SVD




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 36

![Page 36 du PDF](../facsimiles/57698eaee02f0733d076dbcb.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général du k-SVD



  L’apprentissage, selon k-SVD, se fait en deux étapes :




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 37

![Page 37 du PDF](../facsimiles/4270ec29f355dddf19dc5320.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général du k-SVD



  L’apprentissage, selon k-SVD, se fait en deux étapes :
      On fixe D et on cherche la représentation parcimonieuse Λ de
      nos signaux.




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 38

![Page 38 du PDF](../facsimiles/328e9129842c17507b65de3c.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général du k-SVD



  L’apprentissage, selon k-SVD, se fait en deux étapes :
      On fixe D et on cherche la représentation parcimonieuse Λ de
      nos signaux.
      L’erreur est alors f (D) = kX − DΛk2F .




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 39

![Page 39 du PDF](../facsimiles/5fc47bf79d9f212602a20b75.webp)

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Principe général du k-SVD



  L’apprentissage, selon k-SVD, se fait en deux étapes :
      On fixe D et on cherche la représentation parcimonieuse Λ de
      nos signaux.
      L’erreur est alors f (D) = kX − DΛk2F .
      On fixe Λ et on cherche à remplacer les atomes de D, l’un
      après l’autre, par de nouveaux vecteurs qui minimisent f (D).




                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 40

~~~text
                             Dictionnaire
          Apprentissage d’un dictionnaire
                      Algorithme k-SVD


Algorithme k-SVD




                              CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 41

![Page 41 du PDF](../facsimiles/d683de56a5af3bcc9783dfb0.webp)

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 42

![Page 42 du PDF](../facsimiles/b3bbb165793b62cc7c763826.webp)

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 43

![Page 43 du PDF](../facsimiles/3ea43b0bfbe8af91c3533a38.webp)

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 44

![Page 44 du PDF](../facsimiles/bc0e01f1039fe52d26f0a82e.webp)

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D.




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 45

![Page 45 du PDF](../facsimiles/4bfcc3edf3b9e7d1ed7835b7.webp)

~~~text
                               Dictionnaire
            Apprentissage d’un dictionnaire
                        Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne




                                CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 46

![Page 46 du PDF](../facsimiles/f6bf45ac14aabb8eec1f783c.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 47

![Page 47 du PDF](../facsimiles/14d1210f11a76090834d57d9.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,.




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 48

![Page 48 du PDF](../facsimiles/5bdde3b45bc820cd05ad0cb4.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 49

![Page 49 du PDF](../facsimiles/af159a12fb5420bff5e306ee.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.
     On remplace ensuite les atomes du dictionnaire l’un après
     l’autre. Arrivé au numéro i, on met de côté la contribution de
     di dans l’erreur f (D) = kX − DΛk2F = kEi − D.,i Λi,. k2F .




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 50

![Page 50 du PDF](../facsimiles/80f60f781314259531b04fba.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.
     On remplace ensuite les atomes du dictionnaire l’un après
     l’autre. Arrivé au numéro i, on met de côté la contribution de
     di dans l’erreur f (D) = kX − DΛk2F = kEi − D.,i Λi,. k2F .
     On introduit une matrice auxiliaire Ωi telle que




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 51

![Page 51 du PDF](../facsimiles/b5321f90be660c06ee4dbb4d.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.
     On remplace ensuite les atomes du dictionnaire l’un après
     l’autre. Arrivé au numéro i, on met de côté la contribution de
     di dans l’erreur f (D) = kX − DΛk2F = kEi − D.,i Λi,. k2F .
     On introduit une matrice auxiliaire Ωi telle que Λi,. Ωi
     conserve uniquement les composantes non nulles de Λi,. .



                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 52

![Page 52 du PDF](../facsimiles/a505e5f99d256fe1f5ebfdc4.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.
     On remplace ensuite les atomes du dictionnaire l’un après
     l’autre. Arrivé au numéro i, on met de côté la contribution de
     di dans l’erreur f (D) = kX − DΛk2F = kEi − D.,i Λi,. k2F .
     On introduit une matrice auxiliaire Ωi telle que Λi,. Ωi
     conserve uniquement les composantes non nulles de Λi,. .
     Après multiplication par Ωi ;


                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 53

![Page 53 du PDF](../facsimiles/559b09dd00c6f69ac658d145.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.
     On remplace ensuite les atomes du dictionnaire l’un après
     l’autre. Arrivé au numéro i, on met de côté la contribution de
     di dans l’erreur f (D) = kX − DΛk2F = kEi − D.,i Λi,. k2F .
     On introduit une matrice auxiliaire Ωi telle que Λi,. Ωi
     conserve uniquement les composantes non nulles de Λi,. .
     Après multiplication par Ωi ; on obtient
     f R (D) = kEiR − D.,i ΛR    2
                            i,. kF .

                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 54

![Page 54 du PDF](../facsimiles/559b09dd00c6f69ac658d145.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD

     La première étape fait appel à MP ou OMP afin de
     déterminer Λ.
     Chaque colonne de Λ est la représentation parcimonieuse d’un
     signal dans D. Et chaque ligne indique la contribution d’un
     atome aux représentations parcimonieuses de tous les signaux.
                    P
     On écrit DΛ = i D.,i Λi,. somme de matrices de rang ⩽ 1.
     On remplace ensuite les atomes du dictionnaire l’un après
     l’autre. Arrivé au numéro i, on met de côté la contribution de
     di dans l’erreur f (D) = kX − DΛk2F = kEi − D.,i Λi,. k2F .
     On introduit une matrice auxiliaire Ωi telle que Λi,. Ωi
     conserve uniquement les composantes non nulles de Λi,. .
     Après multiplication par Ωi ; on obtient
     f R (D) = kEiR − D.,i ΛR    2
                            i,. kF .

                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 55

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD


     Après multiplication par Ωi ; on obtient EiR = Ei Ωi .




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 56

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD


     Après multiplication par Ωi ; on obtient EiR = Ei Ωi .
     La recherche d’un remplaçant de D.,i = di et de Λi,. revient à
     la recherche d’une matrice de rang 1 la plus proche possible
     de EiR .




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 57

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD


     Après multiplication par Ωi ; on obtient EiR = Ei Ωi .
     La recherche d’un remplaçant de D.,i = di et de Λi,. revient à
     la recherche d’une matrice de rang 1 la plus proche possible
     de EiR .
     C’est la décomposition SVD de EiR qui va permettre de
     remplacer D.,i et Λi,. .




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 58

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD


     Après multiplication par Ωi ; on obtient EiR = Ei Ωi .
     La recherche d’un remplaçant de D.,i = di et de Λi,. revient à
     la recherche d’une matrice de rang 1 la plus proche possible
     de EiR .
     C’est la décomposition SVD de EiR qui va permettre de
     remplacer D.,i et Λi,. .
     Si Λi,. = 0,




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 59

![Page 59 du PDF](../facsimiles/e26b28f08777478478506bb2.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD


     Après multiplication par Ωi ; on obtient EiR = Ei Ωi .
     La recherche d’un remplaçant de D.,i = di et de Λi,. revient à
     la recherche d’une matrice de rang 1 la plus proche possible
     de EiR .
     C’est la décomposition SVD de EiR qui va permettre de
     remplacer D.,i et Λi,. .
     Si Λi,. = 0, l’étape précédente est remplacée par
     l’actualisation de D.,i par un vecteur aléatoire normalisé.




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 60

![Page 60 du PDF](../facsimiles/c09d02ea09b23c403eb754f3.webp)

~~~text
                                Dictionnaire
             Apprentissage d’un dictionnaire
                         Algorithme k-SVD


Algorithme k-SVD


     Après multiplication par Ωi ; on obtient EiR = Ei Ωi .
     La recherche d’un remplaçant de D.,i = di et de Λi,. revient à
     la recherche d’une matrice de rang 1 la plus proche possible
     de EiR .
     C’est la décomposition SVD de EiR qui va permettre de
     remplacer D.,i et Λi,. .
     Si Λi,. = 0, l’étape précédente est remplacée par
     l’actualisation de D.,i par un vecteur aléatoire normalisé.
     L’algorithme est arrêté au bout d’un nombre fixé d’itérations.




                                 CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 61

~~~text
                             Dictionnaire
          Apprentissage d’un dictionnaire
                      Algorithme k-SVD


Algorithme k-SVD




                              CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~

## Page 62

~~~text
                                  Dictionnaire
               Apprentissage d’un dictionnaire
                           Algorithme k-SVD


Algorithme k-SVD
  Entrées : X taille (N, `), D, taille (N, k) , Nombre itérations : m.
                               Sorties : D, Λ
                     Initialisation du compteur j = 0
                              Tant que j < m
               Etape 1 : Λ = OMP(D, X , iterMax, )
                        Etape 2 : Pour i = 1 à k.
                          Ei ← X − DΛ + D.,i Λi,.
                                 Si Λi,. 6= 0 :
                                ΛRi,. = Λi,. Ωi
                                 EiR = Ei Ωi  
                          [U, ∆, V ] = SVD EiR
                        D.,i ← U.,1  ΛR             T
                                       i,. ← ∆1,1 V.,1
                             Sinon : D.,i ← Alea
                                  j ←j +1
                                   CY TECH       Compressive Sensing Apprentissage d’un dictionnaire
~~~
