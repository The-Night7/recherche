# CM1-Systeme_2021-2022_Algebre2_P1S2_DCransac.pdf

[Ouvrir l’original](https://drive.google.com/open?id=15nenhRe5Z-rDWvzJbrlmd0EgY-ApI980) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                               Échelonner un système d'équations linéaires , par la méthode de Gauss
          Systèmes linéaires   Rang d'une matrice
        Systèmes de Cramer     La matrice des coecients
                               Le rang et les systèmes linéaires




Systèmes d'Equations Linéaires




                 D. Cransac    Analyse
~~~

## Page 2

~~~text
                                              Échelonner un système d'équations linéaires , par la méthode de Gauss
                         Systèmes linéaires   Rang d'une matrice
                       Systèmes de Cramer     La matrice des coecients
                                              Le rang et les systèmes linéaires
Convention
Dans les énoncés, K représentera l'ensemble C ou l'ensemble R.
Dénition (Équation linéaire)
Soit p ∈ N∗ .
On appelle équation linéaire à p inconnues x1 , . . . , xp , une équation de
la forme

           a1 x1 + · · · + ap xp = b avec (a1 , . . . , ap , b) ∈ Kp+1


Une solution d'une telle équation est notée sous fome d'un n-uplet
(qu'on appelera vecteur dans la suite du cours) :

                                (s1 , . . . , sp ) ∈ Kp


On appelle équation homogène associée à l'équation linéaire,
l'équation obtenue en remplaçant b par 0.
                                D. Cransac    Analyse
~~~

## Page 3

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




Example
   L'équation cartésienne d'une droite du plan est une équation linéaire
   à deux inconnues.

                                       3x + 2y = 5
    L'équation cartésienne d'un plan de l'espace est une équation
    linéaire à trois inconnues.

                                   x + 5y − 3z = 4




                               D. Cransac    Analyse
~~~

## Page 4

~~~text
                                                 Échelonner un système d'équations linéaires , par la méthode de Gauss
                            Systèmes linéaires   Rang d'une matrice
                          Systèmes de Cramer     La matrice des coecients
                                                 Le rang et les systèmes linéaires
Remarque
   Le n-uplet (0, . . . , 0) est toujours solution d'une équation homogène.
   En eet
                                a1 0 + · · · + ap 0 = 0


    Si (s1 , . . . , sp ) est solution d'une équation homogène alors pour tout
    λ ∈ K, (λs1 , . . . , λsp ) est aussi solution.
    En eet si a1 s1 + · · · + ap sp = 0 alors
    a1 λs1 + · · · + ap λsp = λ(a1 λs1 + · · · + ap λsp ) = λ0 = 0
    Si (s1 , . . . , sp ) et s1′ , . . . , sp′ sont solutions d'une équation
                                              

    homogène alors s1 + s1′ , . . . , sp + sp′ est aussi solution.
                                                      

    En eet si a1 s1 + · · · + ap sp = 0 et a1 s1′ + · · · + ap sp′ = 0 alors
    a1 (s1 + s1′ ) + · · · + ap (sp + sp′ )
    = (a1 s1 + · · · + ap sp ) + (a1 s1′ + · · · + ap sp′ )
    =0+0
    =
      0
Les deux dernières propriétés caractérisent une équation linéaire.
                                   D. Cransac    Analyse
~~~

## Page 5

~~~text
                                                    Échelonner un système d'équations linéaires , par la méthode de Gauss
                          Systèmes linéaires        Rang d'une matrice
                        Systèmes de Cramer          La matrice des coecients
                                                    Le rang et les systèmes linéaires


Dénition (Système linéaire)
Soit n et p appartenant à N∗ .
On appelle système linéaire de n équations à p inconnues x1 , . . . , xp
un système de la forme :
                      
                       a1.1 x1 + · · · + a1.p xp =                  b1
                                               ..                      ..
                      

                                               .                       .
                          an.1 x1 + · · · + an.p xp =                bn
                      

où les ai.j et bi (1 ⩽ i ⩽ n, 1 ⩽ j ⩽ p) sont des éléments de K.
Un vecteur (s1 , . . . , sp ) ∈ Kp est solution du système si et seulement si il
est solution de toutes les équations linéaires composant le système.
On appelle système d'équations homogènes le système obtenu en
remplaçant tous les bi par 0 .


                                 D. Cransac         Analyse
~~~

## Page 6

~~~text
                                                 Échelonner un système d'équations linéaires , par la méthode de Gauss
                            Systèmes linéaires   Rang d'une matrice
                          Systèmes de Cramer     La matrice des coecients
                                                 Le rang et les systèmes linéaires

Un premier exemple

  Résoudre le système :
                                  2y +                              = 4
                   
                    x     +                 z       − t
                                          − 3z       + 3t           = 5
                   
                                   y
                   
               S
                                         − 2z       + t            = −2
                                                       4t           = 16
                   
                   

  Solution
                              + 2y                                             4
                    
                     x
                                            + z        − t            =
                                 y           − 3z       + 3t           =       5
                    
              S⇔
                                            − 2z       + 4            =      −2
                                                                               4
                    
                                                          t            =
                    

                                  2y                                    4
                   
                    x
                          +              +      z     −       t      =
                   
                                   y      −      3z + 3t =              5
              ⇔
                                         −2     z                    = −6
                                                                      = 4
                   
                                                               t
                   

                                   D. Cransac    Analyse
~~~

## Page 7

~~~text
                                               Échelonner un système d'équations linéaires , par la méthode de Gauss
                      Systèmes linéaires       Rang d'une matrice
                    Systèmes de Cramer         La matrice des coecients
                                               Le rang et les systèmes linéaires

                          + 2y                           − t = 4
                
                 x                        + z
                                           − 9           + 12 = 5
                
                             y
                
        S⇔
                                            z                = 3
                                                            t = 4
                
                

                             2y + z − t =                              4
            
             x       +
                                                                      5−3
            
                              y                                =
            
        ⇔
                                          z                   =       3
                                                                       4
            
                                                         t     =
            

                             2y + z − t =                              4
            
             x       +
                                                                      5−3
            
                              y                                =
            
        ⇔
                                          z                   =       3
                                                                       4
            
                                                         t     =
            

                    4 + 3 − 4 = 4                                                       1
                                                                    
     x     +                        x                                          =
                              = 2                                                       2
                                   
                    y                 y                                          =
                                   
⇔                                 ⇔
                       z     = 3    z                                          =      3
                            t = 4                                                       4
                                   
                                      t                                          =
                                   

                             D. Cransac        Analyse
~~~

## Page 8

~~~text
                                                Échelonner un système d'équations linéaires , par la méthode de Gauss
                           Systèmes linéaires   Rang d'une matrice
                         Systèmes de Cramer     La matrice des coecients
                                                Le rang et les systèmes linéaires




Le système :
                                 2y +                              = 4
                   
                    x
                         +                 z       − t
                                  y      − 3z       + 3t           = 5
                   
               S
                                        − 2z       + t            = −2
                                                      4t           = 16
                   
                   

est tel qu'à chaque ligne on a une inconnue de moins.
Il ressemble à un escalier. On dit qu'il est échelonné.




                                  D. Cransac    Analyse
~~~

## Page 9

~~~text
                                                   Échelonner un système d'équations linéaires , par la méthode de Gauss
                              Systèmes linéaires   Rang d'une matrice
                            Systèmes de Cramer     La matrice des coecients
                                                   Le rang et les systèmes linéaires


Dénition (Système échelonnée)
Un système est dit échelonnée en lignes s'il vérie les deux propriétés
suivantes :
  1 Si une ligne est entièrement nulle (0 = 0), toutes les lignes suivantes
     le sont aussi.
  2 A partir de la deuxième ligne, dans chaque ligne non entièrement
     nulle (0 = 0), le premier coecient non nul à partir de la gauche est
     situé à droite (strictement) du premier coecient non nul de la ligne
     précédente.

                                     2y +                              = 4
                      
                       x     +                 z       − t
                                             − 3z       + 3t           = 5
                      
                                      y
                      
                 ′′
             S
                                            − 2z       + t            = −2
                                                          4t           = 16
                      
                      



                                     D. Cransac    Analyse
~~~

## Page 10

~~~text
                                                   Échelonner un système d'équations linéaires , par la méthode de Gauss
                              Systèmes linéaires   Rang d'une matrice
                            Systèmes de Cramer     La matrice des coecients
                                                   Le rang et les systèmes linéaires




Important
Les systèmes échelonnés sont très faciles à résoudre : on commence par
la dernière équation et on "remonte" pour exprimer l'inconnue
supplémentaire qui apparaît en fonction de celles obtenues dans les
équations en-dessous.

                                     2y +                              = 4
                      
                       x
                             +                 z       − t
                                      y      − 3z       + 3t           = 5
                      
                 ′′
             S
                                            − 2z       + t            = −2
                                                          4t           = 16
                      
                      




                                     D. Cransac    Analyse
~~~

## Page 11

~~~text
                                            Échelonner un système d'équations linéaires , par la méthode de Gauss
                       Systèmes linéaires   Rang d'une matrice
                     Systèmes de Cramer     La matrice des coecients
                                            Le rang et les systèmes linéaires



Tout système linéaire se ramène à un système échelonné équivalent en
utilisant trois types d'opérations élémentaires :
  1 Intervertir deux équations
  2 Intervertir l'ordre des inconnues
  3 Remplacer une équation par la somme d'elle même et d'une autre
      multipliée par un coecient.
Méthode du pivot de Gauss
Étant donné un système d'équations linéaires, la méthode du pivot de
Gauss a pour but de construire un système échelonné qui soit équivalent
au système donné.




                              D. Cransac    Analyse
~~~

## Page 12

~~~text
                                               Échelonner un système d'équations linéaires , par la méthode de Gauss
                          Systèmes linéaires   Rang d'une matrice
                        Systèmes de Cramer     La matrice des coecients
                                               Le rang et les systèmes linéaires

Deuxième exemple



  On va commencer par présenter la méthode du pivot de Gauss sur un
  exemple.
  Considérons le système dont les inconnues sont x, y , z, t et où a, b
  sont des paramètres xés.
                       + 2y
              
               x                   +      z   −      t     =        a        (E1 )
            S   2x     + 4y         −      z   −     5t = 5a                  (E2 )
                −x     − 2y         +      z   +     3t = b                   (E3 )
              

  Choisissons une équation avec un coecient non nul pour la première
  inconnue x .
  Ici la première équation convient avec le coecient 1, pour x , qu'on
  appelle le premier pivot.
  On va utiliser ce pivot pour faire disparaître l'inconnue x des autres
  équations.
                                 D. Cransac    Analyse
~~~

## Page 13

~~~text
                                                Échelonner un système d'équations linéaires , par la méthode de Gauss
                           Systèmes linéaires   Rang d'une matrice
                         Systèmes de Cramer     La matrice des coecients
                                                Le rang et les systèmes linéaires


                       + 2y
                
                 x                  +      z   −      t     =        a        (E1 )
              S   2x   + 4y          −      z   −     5t = 5a                  (E2 )
                  −x   − 2y          +      z   +     3t = b                   (E3 )
                

Pour cela on ajoute à ces équations la première multiplié par un
coecient convenable.
On obtient un système linéaire équivalent :
                  2y +                                              (E1′ ) = (E1 )
        
         x   +           z        − t          =   a
S   ′
                       − 3z        − 3t         =  3a               (E2′ ) = (E2 ) − 2(E1 )
                       + 2z        + 2t         = b+a               (E3′ ) = (E3 ) + (E1 )
        

Examinons maintenant le système obtenu en supprimant la première
équation.
On remarque que la variable x n'y apparaît pas. La variable suivante y
non plus. On est ramené à un système de deux équations avec ici deux
variables en moins.

                                  D. Cransac    Analyse
~~~

## Page 14

~~~text
                                                    Échelonner un système d'équations linéaires , par la méthode de Gauss
                               Systèmes linéaires   Rang d'une matrice
                             Systèmes de Cramer     La matrice des coecients
                                                    Le rang et les systèmes linéaires



                           + 2y                                                      (E1′ )
                     
                      x              +      z      −    t         =   a
             S   ′
                                      −      3z     −   3t         =  3a             (E2′ )
                     
                                      +      2z     +   2t         = b+a             (E3′ )
Choisissons un deuxième pivot.
On le trouve dans l'équation (E2′ ). C'est le coecient −3 de z .
Nous allons l'utiliser pour éliminer z des équations suivantes (ici, il n'en
reste qu'une).
Réécrivons le nouveau système :
             + 2y                                                         (E1′′ ) = (E1′ )
       
        x                 + z        − t           =          a
                           − 3z       − 3t                    3a
       
S ′′                                                =                     (E2′′ ) = (E2′ )
                                                                                                     2
                                              0     = b + 3a              (E3′′ ) = (E3′ ) + (E2′ )
       
                                                                                                     3
       

Le système obtenu est un système échelonné.


                                      D. Cransac    Analyse
~~~

## Page 15

~~~text
                                                  Échelonner un système d'équations linéaires , par la méthode de Gauss
                            Systèmes linéaires    Rang d'une matrice
                          Systèmes de Cramer      La matrice des coecients
                                                  Le rang et les systèmes linéaires

Description de l'algorithme du pivot de Gauss




  Rappelons que le but est d'obtenir un système équivalent au système
  donné et qui soit échelonné c'est-à-dire de la forme :

  
   x n1
          +   a1,n1 +1 xn1 +1    +      ...     ...                   ...                         +      a1,n xn
  
                                        x n2    +           a2,n2 +1 xn2 +1 + ...                 +      a2,n xn
                                                 ..
  
  
                                                      .
  
  
  
  
  
                                                          xnp + ap,np +1 xnp +1 + ... + ap,n xn
  
  
  
                                                                                                             0
  
  
  
  
  
                                                                                                              0
  
  

  avec 1 ⩽ p ⩽ m et 1 ⩽ n1 < n2 < ... < np ⩽ n.

                                   D. Cransac     Analyse
~~~

## Page 16

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires



Avec l'exemple précédent on peut comprendre facilement le
fonctionnement de l'algorithme pour un système quelconque d'équations.
  1 On cherche un pivot, premier coecient non nul d'une certaine
     variable x dans une des équations. Par permutation, cette équation
     devient la première équation.
  2 On utilise ce pivot et cette équation pour éliminer x des équations
     suivantes. Pour cela on ajoute cette équation multipliée par un
     coecient convenable aux équations suivantes
  3 S'il y a des équations dont le premier membre est nul 0 = . . . on les
     place en dernier.
  4 On recommence à l'étape 1 avec le système privé de la première
     équation.
L'algorithme s'arrête lorsqu'il ne reste plus que des équations 0 = . . ..



                               D. Cransac    Analyse
~~~

## Page 17

~~~text
                                                  Échelonner un système d'équations linéaires , par la méthode de Gauss
                             Systèmes linéaires   Rang d'une matrice
                           Systèmes de Cramer     La matrice des coecients
                                                  Le rang et les systèmes linéaires


Exprimons plus en détails une des étapes de cet algorithme.
L'objectif est d'obtenir, à l'issue de l'étape k un système de la forme Hk
suivante :

  xn1 + a1,n1 +1 xn1 +1 +...                                                  +a1,n xn =b1


xn2                    +...             +a2,nk xnk +a2,nk +1. xnk +1 + ... +a2,n xn =b2




                        .

                          .

                            .




                              xk−1,nk−1 +ak−1,nk xnk +ak−1,nk +1 xnk +1 + ...+ak−1,n xn =bk−1

                                                        ′                        ′
                                0         +xnk      +ak,n     x
                                                          k +1 nk +1
                                                                      + ... +ak,n   xn =bk′
                                                        ′                        ′           ′

                                                     +a          x
                                                        k+1,nk +1 nk +1 +  ...+a k+1,n xn =bk+1


                                           0

                                             .                                             .


                                             .                                             .

                                             .                                             .



                                                       ′                        ′           ′
                                            0        +am,nk +1 xnk +1 + ... +am,n xn =bm

avec 1   ⩽ n1 < n2 < ... < nk ⩽ n.




                                    D. Cransac    Analyse
~~~

## Page 18

~~~text
                                                      Échelonner un système d'équations linéaires , par la méthode de Gauss
                                 Systèmes linéaires   Rang d'une matrice
                               Systèmes de Cramer     La matrice des coecients
                                                      Le rang et les systèmes linéaires



Système à l'état k − 1

  xn +a1,n1 +1 xn1 +1 +...                                                        + a1,n xn = b1

 1



         xn2         +...                  +a2,nk xnk    +a2,nk +1. xnk +1 + ... + a2,n xn = b2

                      .

                        .

                          .




                              xk−1,nk−1 +ak−1,nk xnk +ak−1,nk +1 xnk +1 + ...+ak−1,n xn =bk−1


                                0       +ak,nk xnk +ak,nk +1 xnk +1 + ... + ak,n xn = bk
                                        +ak+1,nk xnk +ak+1,nk +1 xnk +1 + ...+ak+1,n xn =bk+1


                                0

                                   .                                                                           .


                                   .                                                                           .

                                   .                                                                           .




                                  0         +am,nk xnk    +am,nk +1 xnk +1 + ... + am,n xn = bm

avec 1   ⩽ n1 < n2 < ... < nk ⩽ n.




                                        D. Cransac    Analyse
~~~

## Page 19

~~~text
                                                      Échelonner un système d'équations linéaires , par la méthode de Gauss
                                 Systèmes linéaires   Rang d'une matrice
                               Systèmes de Cramer     La matrice des coecients
                                                      Le rang et les systèmes linéaires



Système après normalisation du pivot :

  xn +a1,n1 +1 xn1 +1 +...                                                        + a1,n xn = b1

 1



         xn2         +...                  +a2,nk xnk    +a2,nk +1. xnk +1 + ... + a2,n xn = b2

                      .

                        .

                          .




                              xk−1,nk−1 +ak−1,nk xnk +ak−1,nk +1 xnk +1 + ...+ak−1,n xn =bk−1

                                                        ′                       ′

                                0         +xnk       +ak,n    x
                                                           k +1 nk +1
                                                                       + ... + ak,n xn = bk′
                                        +ak+1,nk xnk +ak+1,nk +1 xnk +1 + ...+ak+1,n xn =bk+1


                                0

                                   .                                                                           .


                                   .                                                                           .

                                   .                                                                           .




                                  0         +am,nk xnk    +am,nk +1 xnk +1 + ... + am,n xn = bm

avec 1   ⩽ n1 < n2 < ... < nk ⩽ n.




                                        D. Cransac    Analyse
~~~

## Page 20

~~~text
                                                   Échelonner un système d'équations linéaires , par la méthode de Gauss
                              Systèmes linéaires   Rang d'une matrice
                            Systèmes de Cramer     La matrice des coecients
                                                   Le rang et les systèmes linéaires



Système à l'étape k

  xn + a1,n1 +1 xn1 +1 +...                                                         +a1,n xn   =b1

 1



 xn2                  +...             +a 2,n k xn k +a2  ,nk  + 1. xnk + 1 +  ... +a 2 ,n xn =b 2

                       .

                         .

                           .




                             xk−1,nk−1 +ak−1,nk xnk +ak−1,nk +1 xnk +1 + ... +ak−1,n xn =bk−1

                                                         ′                             ′

                               0         +xnk        +ak,n         x
                                                              k +1 nk +1
                                                                             + ... +ak,n    xn =bk′
                                                      +a”k+1,nk +1 xnk +1 + ...+a”k+1,n xn =b”k+1


                                            0

                                             .                                                  .


                                             .                                                  .

                                             .                                                  .




                                             0        +a”m,nk +1 xnk +1 + ... +a”m,n xn =b”m

avec 1   ⩽ n1 < n2 < ... < nk ⩽ n.




                                     D. Cransac    Analyse
~~~

## Page 21

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires
Décrivons à présent l'étape k de la méthode du Pivot de Gauss : étant
donné un système de la forme Hk−1 , nous allons le transformer de façon
à obtenir un système de la forme Hk .
Nous noterons Ej la j ème équation du système.
    On ne modie pas les k − 1 premières équations du système linéaire.
    Si tous les coecients al,m (avec l ⩾ k et m > nk−1 ) sont nuls,
    alors, pour tout l ⩾ k , l'équation El s'écrit : 0 = bl . Le système a
    donc la forme voulue. L'algorithme s'arrête.
    Sinon, on pose nk := min{m : ∃l ⩾ k : al,m ̸= 0}. Alors, quitte à
    échanger la ligne k avec une ligne p ⩾ k (telle que ap,nk ̸= 0), on se
    ramène au cas où ak,nk est non nul (ce sera notre pivot pour l'étape
    k ).
                                             1
    On remplace alors l'équation Ek par          Ek pour se ramener à :
                                           ak,nk
    ak,nk = 1.
    Puis, pour tout p > k , on remplace Ep par Ep − ap,nk Ek (an
    d'éliminer les termes en xnk des équations k + 1, ..., m).
    Le système d'équations linéaires ainsi obtenu est alors de la forme
    Hk , l'étape k est nie.
                               D. Cransac    Analyse
~~~

## Page 22

~~~text
                                                  Échelonner un système d'équations linéaires , par la méthode de Gauss
                            Systèmes linéaires    Rang d'une matrice
                          Systèmes de Cramer      La matrice des coecients
                                                  Le rang et les systèmes linéaires


Résolution du premier exemple
On avait obtenu :
                          2y +                                                       (E1′′ )
                
                 x   +            z             − t        =   a
       S   ′′
                                 − 3z            − 3t       =   3a                   (E2′′ )
                
                                                     0      = b + 3a                 (E3′′ )
Si b + 3a = 0, on peut déterminer x, y , z, t solutions du système.
Si b + 3a ̸= 0, le système n'admet aucune solution. En eet pour tout
x, y , z, t , la dernière équation ne sera pas vériée.
La dernière équation est appellée équation de compatiblité.
Par ailleurs, si t et y sont xées, on ne peut obtenir qu'une seule valeur
de z et de x .
On dit que x et z qui correspondent au pivot sont des inconnues
principales.


                                   D. Cransac     Analyse
~~~

## Page 23

~~~text
                                            Échelonner un système d'équations linéaires , par la méthode de Gauss
                       Systèmes linéaires   Rang d'une matrice
                     Systèmes de Cramer     La matrice des coecients
                                            Le rang et les systèmes linéaires




Proposition
 1 Les inconnues des lignes non nulles s'appellent les inconnues
              , ou pivots
    principales

 2 Un système échelonné possède des solutions si et seulement si les
    équations de compatibilité    sont satisfaites (portant sur les
   données).
 3 Si ces conditions sont satisfaites alors toute donnée des inconnues
   non principales détermine une unique solution du système. Cela
   équivaut à dire que les solutions du système sont paramétrées par les
   inconnues non principales.




                              D. Cransac    Analyse
~~~

## Page 24

~~~text
                                               Échelonner un système d'équations linéaires , par la méthode de Gauss
                          Systèmes linéaires   Rang d'une matrice
                        Systèmes de Cramer     La matrice des coecients
                                               Le rang et les systèmes linéaires



Un autre exemple
Pour résoudre le système suivant dans R4 , on veut échelonner ce
système :
                                                                           1
       
        x     +    y       −       z      +   t                   =              (E1 )
                                             8t                            2
       
                                                                   =              (E2 )
       
        2x    +    2y +            z      + 3t                    =       2      (E3 )
                                   2z                                      0
       
                                                      +      u     =              (E4 )
       


Nous allons utiliser la méthode du pivot de Gauss : à chaque étape, le
pivot sera encadré.
Les systèmes d'équations linéaires obtenus sont équivalents au système
donné.



                                 D. Cransac    Analyse
~~~

## Page 25

~~~text
                                                          Échelonner un système d'équations linéaires , par la méthode de Gauss
                                 Systèmes linéaires       Rang d'une matrice
                               Systèmes de Cramer         La matrice des coecients
                                                          Le rang et les systèmes linéaires


Le système est :
                                                                                      1
       
        x         +       y         −       z        +    t                   =             (E1 )
                                                        8t                            2
       
                                                                               =             (E2 )
       
        2x        + 2y              +       z        + 3t                     =      2      (E3 )
                                           2z                                         0
       
                                                                    + u        =             (E4 )
       

Il y a un terme en x dans la première équation, le premier pivot de Gauss
sera ce terme : nous l'utilisons pour éliminer les termes en x des autres
équations

    x                                                                      1
  
         + y          −         z       +       t                  =               (E1 )
                                                 8t                        2
  
                                                                    =               (E2 )
  
                               3z +             t                  =      0 (E3′ = E3 − 2E1 )
                                2z +             0                         0
  
                                                          + u       =               (E4 )
  




                                         D. Cransac       Analyse
~~~

## Page 26

~~~text
                                                         Échelonner un système d'équations linéaires , par la méthode de Gauss
                               Systèmes linéaires        Rang d'une matrice
                             Systèmes de Cramer          La matrice des coecients
                                                         Le rang et les systèmes linéaires

Nous oublions à présent la première ligne.Il n'y a pas de terme en y dans
les équations E2 , E3′ et E4 .Il y a un terme en z dans E3′ mais pas dans
E2 ; nous permutons donc les équations E2 et E3′

                                                                       = 1
      
       x
            +       y   −          z      +      t                                     (E1 )
      
                                 3z +             t                    = 0           (E2′ = E3′ )
                                                8t                    = 2          (E3′′ = E2 )
                                 2z +                0                 = 0
      
                                                         +         u                    (E4 )
      


Nous divisons la deuxième équation par 3 de sorte à avoir z au lieu de 3z
dans la deuxième équation
                                                 = 1
    
      x     +    y       −      z        +  t                                                 (E1 )
                                           1                                                       1 ′
    
    
                                                 = 0
    
                                                                                         ′′
                                z        +    t                                     (E2 =           E )
    
                                           3                                                       3 2
    
                                          8t    = 2                                      (E3 ) ′′

                               2z        + 0 + u = 0
    
                                                                                           (E4 )
    



                                        D. Cransac       Analyse
~~~

## Page 27

~~~text
                                              Échelonner un système d'équations linéaires , par la méthode de Gauss
                         Systèmes linéaires   Rang d'une matrice
                       Systèmes de Cramer     La matrice des coecients
                                              Le rang et les systèmes linéaires
Le terme en z de la deuxième équation est le nouveau pivot de Gauss ;
nous l'utilisons pour éliminer les termes en z des équations situés en
dessous
     x + y − z +                  t            = 1            (E1 )
  
                                 1
  
  
                       z +                     = 0           (E2′′ )
  
                                    t
  
                                 3
  
                                 8t            = 2           (E3′′ )
                                  2
  
  
                                − t + u = 0 (E4′ = E4 − 2E2′′ )
  
  
  
                                  3
Nous oublions à présent la deuxième équation ; il y a un terme en t dans
la troisième équation, nous divisons la troisième équation par 8 de sorte à
avoir t à la place de 8t dans cette équation
                                      1
    
      x    + y     −    z     +         t      (E1 )      =
                                       1
    
    
                                    = 0
    
                                              (E2′′ )
    
                       z +              t
                                       3
    
    
                                      1            1
                             t      =   (E3′′′ = E3′′ )
                                      4            8
    
    
                             2
    
    
                            − t + u = 0        (E4′ )
    
    
                             3
    

                                D. Cransac    Analyse
~~~

## Page 28

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




Le terme en t de la troisième équation devient le nouveau pivot de Gauss :
nous l'utilisons pour éliminer les termes en t de la quatrième équation
                 −                               1
  
    x    + y          z    +       t             =                          (E1 )
                          1
  
  
                                               = 0
  
                      z +   t                                               (E2′′ )
  
                          3
  
  
                                                 1                          1 ′′
  
                           t                   =                    (E3′′′ = E )
                                                 4                          8 3
  
  
                                                 1                            2
  
  
  
                                             u =                (E4′′ = E4′ + E3′′′ )
  
                                                 6                            3
  

Ce système d'équations linéaires est échelonné et équivalent au système
initial.




                               D. Cransac    Analyse
~~~

## Page 29

~~~text
                         Échelonner un système d'équations linéaires , par la méthode de Gauss
    Systèmes linéaires   Rang d'une matrice
  Systèmes de Cramer     La matrice des coecients
                         Le rang et les systèmes linéaires




Rang d'une matrice




           D. Cransac    Analyse
~~~

## Page 30

~~~text
                                              Échelonner un système d'équations linéaires , par la méthode de Gauss
                       Systèmes linéaires     Rang d'une matrice
                     Systèmes de Cramer       La matrice des coecients
                                              Le rang et les systèmes linéaires




Dénition (Dénition (temporaire) d'une matrice)
Soient n et m deux entiers naturels non nul.
Une matrice de dimension n × m est un tableau d'éléments de K avec n
lignes et m colonnes.
On note une telle matrice :
                                                           
                               a11          a12   . . . a1m
                             a21           a22   . . . a2m 
                    [aij ] = 
                             . . .
                                                            
                                            ...   ... ...
                              an1           an2   . . . anm




                              D. Cransac      Analyse
~~~

## Page 31

~~~text
                                            Échelonner un système d'équations linéaires , par la méthode de Gauss
                       Systèmes linéaires   Rang d'une matrice
                     Systèmes de Cramer     La matrice des coecients
                                            Le rang et les systèmes linéaires

A chaque système on peut associer la matrice des coecients et la
matrice des seconds membres.
Pour le système
                         + 2y
               
                x                      +   z    −        t       = a
             S   2x      + 4y           −   z    −       5t = 5a
                 −x      − 2y           +   z    +       3t = b
               

La matrice de dimension 3 × 4 des coecients est
                          1  2  1 −1
                                                             

                      A= 2  4 −1 −5
                         −1 −2 1   3
La matrice de dimension 3 × 1 des seconds membres est
                                        
                                         a
                                   A = 5a
                                        b

                              D. Cransac    Analyse
~~~

## Page 32

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




Denition
Une matrice B est dite échelonnée en lignes si
 1 chaque ligne non nulle de B commence avec strictement plus de 0
    que la ligne précédente, et
 2 les lignes nulles (ne contenant que des 0) de B viennent en bas après
    les lignes non nulles.
Toute matrice A peut se réduire à une matrice échelonnée en lignes B par
une suite d'opérations élémentaires sur les lignes.
On appelle B la forme échelonnée en lignes de A.




                               D. Cransac    Analyse
~~~

## Page 33

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




Une des concepts fondamentaux dans l'algèbre linéaire est le rang d'une
matrice.
Il admet de plusieurs dénitions équivalentes. En voici la première.
Denition
Le rang d'une matrice A est le nombre de lignes non nulles dans sa forme
échelonnée en lignes.
On le note rgA.




                               D. Cransac    Analyse
~~~

## Page 34

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




Example
La matrice suivante A se réduit en sa forme échelonnée en lignes par les
pivotages :
            1 −3 6 2
                                  

      A =  2 −5 10 3  L2 ← L2 − 2L1 et L3 ← L3 − 3L1
            3 −8 17 4

      1 −3 6  2                  1 −3 6  2
                                                                                       
     0 1 −2 −1  L3 ← L3 − L2  0 1 −2 −1  .
      0 1 −1 −2                  0 0  1 −1
Donc on a rgA = 3.




                               D. Cransac    Analyse
~~~

## Page 35

~~~text
                                              Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires    Rang d'une matrice
                      Systèmes de Cramer      La matrice des coecients
                                              Le rang et les systèmes linéaires




Example
Pour la matrice suivante
              1 3 2                  1 3 2
                                                                                   

        C =  1 4 1  L2 ← L2 − L1  0 1 −1 
              0 1 −1                 0 1 −1

                                               1 3 2
                                                                  

                    L3 ← L3 − L2              0 1 −1 
                                               0 0 0
On a rg (C ) = 2.




                               D. Cransac     Analyse
~~~

## Page 36

~~~text
                                                 Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires       Rang d'une matrice
                      Systèmes de Cramer         La matrice des coecients
                                                 Le rang et les systèmes linéaires

Theorem
Pour toute matrice A on a
    rgA ⩽ nombre de lignes de A,
    rgA ⩽ nombre de colonnes de A.

Démonstration.
Idée de la preuve. En réduisant la matrice A en une matrice échelonnée
en lignes similaire à celle-ci
                                                           
                                1     3      0    4     5
                            0        2      1    3     8   
                                                           
                            0        0      0    7     2   
                                0     0      0    0     0


 les pivots (les premiers coecients non nuls des lignes non nulles) sont
dans des lignes distinctes et dans des colonnes distinctes.
Donc
nombre de pivots ⩽ nombre de lignes de A,
nombre de pivots ⩽ nombre de colonnes de A.
                               D. Cransac        Analyse
~~~

## Page 37

~~~text
                            Échelonner un système d'équations linéaires , par la méthode de Gauss
       Systèmes linéaires   Rang d'une matrice
     Systèmes de Cramer     La matrice des coecients
                            Le rang et les systèmes linéaires




  0 0 0 0                     1 −3 6 2
                                                        
 0 0 0 0                   0 0 0 0 
  0 0 0 0                     0 0 0 0
   rang = 0                    rang = 1



  1 −3 6 2                    1 −3 6 2
                                                          
 0 0 1 5                   0 1 6 5 
  0 0 0 0                     0 0 1 −1
   rang = 2                     rang = 3




              D. Cransac    Analyse
~~~

## Page 38

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




Le nombre de pivots est aussi le nombre de lignes non nulles de la forme
échelonnée de A, d'où nombre de pivots = rgA.




                               D. Cransac    Analyse
~~~

## Page 39

~~~text
                                               Échelonner un système d'équations linéaires , par la méthode de Gauss
                          Systèmes linéaires   Rang d'une matrice
                        Systèmes de Cramer     La matrice des coecients
                                               Le rang et les systèmes linéaires
On a vu qu'on peut associer une matrice à chaque membre d'un système
linéaire. Pour le système
                     x − 3y + 6z + 2w                   = −1,
                    

                      2x − 5y + 10z + 3w                 = 0,
                    
                      3x − 8y + 17z + 4w                 = 1,
on a les matrices
                    1 −3 6 2                                           −1
                                                                           

              A =  2 −5 10 3                            b= 0 
                    3 −8 17 4                                            1
avec A la matrice des coecients regroupant les coecients des variables
du membre de gauche du système, et le vecteur colonne b contient le
membre de droite.
Quand on met les deux ensemble, on a la matrice dite augmentée.
                           1 −3 6 2 −1
                                                                  

                     B =  2 −5 10 3 0 
                           3 −8 17 4 1
                                 D. Cransac    Analyse
~~~

## Page 40

~~~text
                                              Échelonner un système d'équations linéaires , par la méthode de Gauss
                         Systèmes linéaires   Rang d'une matrice
                       Systèmes de Cramer     La matrice des coecients
                                              Le rang et les systèmes linéaires




Denition
Le rang d'un système linéaire est le rang de sa matrice des coecients A.
Par exemple, le rang du système ci-dessus est 3, selon les calculs faits sur
la page précédente.




                                D. Cransac    Analyse
~~~

## Page 41

~~~text
                                            Échelonner un système d'équations linéaires , par la méthode de Gauss
                       Systèmes linéaires   Rang d'une matrice
                     Systèmes de Cramer     La matrice des coecients
                                            Le rang et les systèmes linéaires




Résolution avec une matrice augmentée.
Proposition
Lorsque l'ont a appliqué la méthode de Gauss à une matrice
augmentée, on a deux cas de gures :
On considère la ligne la plus basse qui ne contient pas que des 0
     Si elle contient uniquement une valeur non nulle sur la dernière
     colonne (second membre) alors le système n'admet aucune solution.
     Sinon le système admet au moins une solution.
     Le nombre d'inconnues principales est égal au nombre de pivots, il
     est égal au rang de la matrice.




                              D. Cransac    Analyse
~~~

## Page 42

~~~text
                                        Échelonner un système d'équations linéaires , par la méthode de Gauss
                   Systèmes linéaires   Rang d'une matrice
                 Systèmes de Cramer     La matrice des coecients
                                        Le rang et les systèmes linéaires

                  = −2 E1

x + y − z
  x − y           = 0 E2
  x + 4y + z     = 2 E3

   x − y           = 0 E1′ = E2
⇔ x + y −        z = −2 E2′ = E1
   x + 4 y +    z = 2      E3′
   
   x − y           = 0         E1 ”
⇔        2y −    z = −2 E2 ” = E2′ − E1′
   
         5y +    z = 2 E3 ” = E3′ − E1′
                     = 0
   
     x −  y                          E1
         2        z = −2
   
   
⇔          y −                       E2
                 7
                   z =            7
                             E3 = E3 ” − 5/2E2 ”
   
                 2
   
                      = 0                    = 0
                            
   x − y                    x
⇔        2y −    z    = −1 ⇔       y         = 0
                 z    = 2                 z = 1
                            



                          D. Cransac    Analyse
~~~

## Page 43

~~~text
                                          Échelonner un système d'équations linéaires , par la méthode de Gauss
                     Systèmes linéaires   Rang d'une matrice
                   Systèmes de Cramer     La matrice des coecients
                                          Le rang et les systèmes linéaires
 1 1 −1 −2 E1
              
1 −1 0  0  E2
 1 4  1 2 E3

 1   −1    0  0 E1′ = E2
                  
1    1   −1 −2 E2′ = E1
 1    4    1 2       E3

 1 −1 0  0
              
                  E1 ”
0 2 −1 −2 E2 ” = E2′ − E1′
 0 5  1 2 E3 ” = E3′ − E1′
 1 −1 0  0
              
0 2 −1 −2

      7    
                      5
 0 0     7 E3 = E3 ” − E2 ”
      2               2
 1 −1 0  0
          
0 2 −1 −2
 0 0  1 2
                            D. Cransac    Analyse
~~~

## Page 44

~~~text
                                              Échelonner un système d'équations linéaires , par la méthode de Gauss
                         Systèmes linéaires   Rang d'une matrice
                       Systèmes de Cramer     La matrice des coecients
                                              Le rang et les systèmes linéaires

Apartir de la matrice échelonnée, on "remonte".
   1 −1 0         0
 0 2 −1 −2
   0 0        1   2
    1 −1 0 0
                  
   0 2 0 0
    0 0 1 2
    1 −1 0 0
                  
   0 1 0 0
    0 0 1 2
      1 0 0 0
                 
    0 1 0 0
      0 0 1 2
L'unique solution du système est (0, 0, 2) que l'on "lit" sur la dernière
colonne.
                                D. Cransac    Analyse
~~~

## Page 45

~~~text
                                         Échelonner un système d'équations linéaires , par la méthode de Gauss
                    Systèmes linéaires   Rang d'une matrice
                  Systèmes de Cramer     La matrice des coecients
                                         Le rang et les systèmes linéaires
                                           1 2 4 8
                                                                       

Si l'on obtient la matrice augmentée : 0 0 0 2
                                           0 0 0 0
Il n'y a pas de solution car sur la dernière ligne où il n'y a pas que
des 0, seul le second membre n'est pasnul.
                                           1 2 4 8
                                                        

Si l'on obtient la matrice augmentée : 0 0 1 1
                                           0 0 0 0
Il n'y a que deux pivots principaux donc il y a une innité de
solutions. Pour les décrire, on revient au système
   x + 2y + 4z = 8

                                ⇔
                     z = 1
   x + 2y + 4z = 8

                                ⇔Les inconnues principales sont x et
                     z = 1
z et s'expriment en fonction des autres inconnues y qui peuvent être
considérées
         comme des paramètres :
          x = −2y − 4z + 8             x = −2y + 4
(E ) ⇔                            ⇔
          z =            1             z =          1
L'ensemble des solutions est donc S = {(−2y + 4; y ; 1), y ∈ R}
                           D. Cransac    Analyse
~~~

## Page 46

~~~text
                                             Échelonner un système d'équations linéaires , par la méthode de Gauss
                        Systèmes linéaires   Rang d'une matrice
                      Systèmes de Cramer     La matrice des coecients
                                             Le rang et les systèmes linéaires




                                        1 2 4 8
                                                                  

Si l'on obtient la matrice augmentée : 0 1 1 1
                                        0 0 1 5
Il y a exactement 3 pivots principaux donc il n'y qu'une solution.




                               D. Cransac    Analyse
~~~

## Page 47

~~~text
                        Systèmes linéaires
                      Systèmes de Cramer




On peut donner des critères selon lesquels un système aura une solution
unique.
Theorem
Un système est de Cramer si et seulement si son système admet une seule
solution.

Theorem
Un système de n équations à n inconnues est un système de Cramer si la
méthode du pivot de Gauss fait apparaître successivement n pivots (non
nuls) ce qui est équivalent au fait que le rang de la matrice du système
est n.




                               D. Cransac    Analyse
~~~

## Page 48

~~~text
                         Systèmes linéaires
                       Systèmes de Cramer

Exercice
Pour quelles valeurs du paramètre ℓ le système suivant est-il de Cramer ?
                        2x + 3y + z = 4
                       

                         −x + y + 2z = 5
                       
                         7x + 3y + (ℓ − 5)z = 7

Solution
On construit  la matrice augmentée 
                                    et on 
                                          en détermine une forme
                   2 3       1   4          −1 1         2    5
                                                                 

échelonnée :  −1 1          2   5 ∼  2 3              1    4 
                   7 3 ℓ−    5 7           7 3 ℓ −5 7
      −1 1          2     5         −1 1       2      5
  

∼ 0         5      5    14  ∼  0 5          5     14 
       0 10 ℓ + 9 42                 0 0 ℓ − 1 14
     Si ℓ = 1, le système n'admet pas de solution.
     Si ℓ ̸= 1 le système admet une unique solution : il est de rang 3.
     C'est un système de Cramer.
                                D. Cransac    Analyse
~~~

## Page 49

~~~text
                        Systèmes linéaires
                      Systèmes de Cramer


Méthodologie pour résoudre un système d'équations linéaires
Avant tout calcul, observer le système, les inconnues, les coecients, les
signes.
Réorganiser le système et simplier les multiples s'il y a (diviser les
équations par une constante).
Regrouper les équations similaires.
Quelques cas classiques :
   1 Eectuer les somme, demi-somme, diérence, demi-diérence.
   2 Utiliser la substitution si les coecents sont simples (1 ou -1).
   3 Penser à essayer la somme de toutes les équations.
Résolution
     Attention aux équations de compatibilité.
     S'il a une innité de solutions, dénir les inconnues principales et
     celles qui joueront le rôle de paramètre.
     Prendre soin de bien décrire les solutions.

                               D. Cransac    Analyse
~~~
