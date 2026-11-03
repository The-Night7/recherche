# Feuille-Cours3-Espace-Vectoriel_2021-2022_Algebre2_P1S2_KGuezguez.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1x-27ZQMOLNIRo5JMGmCCK-Q20R5XIb7G) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 2, 4, 24.

## Page 1

~~~text
Cours d'Algèbre II : Première année préparatoire
                   CY-TECH
          Khaoula Ben Abdeljelil Guezguez
             Année scolaire 2020 − 2021
~~~

## Page 2

![Fac-similé de la page 2](../facsimiles/a7c45c91552fa09b6f10f059.jpg)

~~~text
2
~~~



## Page 3

~~~text
Table des matières

  Table des matières . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . i
1 Systèmes linéaires                                                               1
  1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
  1.2 Échelonner un système d'équations linéaires
      par la méthode de Gauss . . . . . . . . . . . . . . . . . . . . . . . . . 2
  1.3 Rang d'une matrice . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
      1.3.1 La matrice des coecients . . . . . . . . . . . . . . . . . . . . 7
      1.3.2 Le rang et les systèmes linèaires . . . . . . . . . . . . . . . . . 7
  1.4 Systèmes de Cramer . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2 Groupe                                                                           9
  2.1 Lois de composition internes . . . . . . . . . . . . . . . . . . . . . . 9
      2.1.1 Propriétés usuelles des lci . . . . . . . . . . . . . . . . . . . . 9
  2.2 Structure de groupe . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
      2.2.1 Dénition et exemples . . . . . . . . . . . . . . . . . . . . . 11
      2.2.2 Sous-groupes . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
      2.2.3 Morphismes de groupes . . . . . . . . . . . . . . . . . . . . . . 14
3 Espace vectoriel                                                                21
  3.1 Espace vectoriel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
  3.2 Sous-espace vectoriel . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
      3.2.1 Dénition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
  3.3 Sous-espace vectoriel engendré par une partie d'un espace vectoriel . . 23
      3.3.1 Combinaisons linéaires . . . . . . . . . . . . . . . . . . . . . . 23
      3.3.2 Dénitions et propriétés . . . . . . . . . . . . . . . . . . . . . 23
  3.4 Famille de vecteurs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
      3.4.1 Sous-espace vectoriel engendré par une famille nie de vecteurs 24
      3.4.2 Famille génératrice . . . . . . . . . . . . . . . . . . . . . . . . 25
      3.4.3 Famille libre, famille liée . . . . . . . . . . . . . . . . . . . . . 26
      3.4.4 Base d'un espace vectoriel . . . . . . . . . . . . . . . . . . . . 27
      3.4.5 Composante dans une base . . . . . . . . . . . . . . . . . . . . 28
  3.5 Somme, Somme directe, sous-espaces vectoriels supplémentaires . . . 29
      3.5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
      3.5.2 Somme de sous-espaces vectoriels . . . . . . . . . . . . . . . . 29
      3.5.3 Somme directe des sous-espaces vectoriels . . . . . . . . . . . 30
      3.5.4 Sous-espaces vectoriels supplémenatires dans un espace vectoriel 31

                                                                                    i
~~~

## Page 4

![Fac-similé de la page 4](../facsimiles/a380359aabf604318b918a9c.jpg)

~~~text
TABLE DES MATIÈRES




ii
~~~



## Page 5

~~~text
Chapitre 1
Systèmes linéaires

    L'objectif de ce chapitre est d'introduire et de résoudre des systèmes de n équa-
tions à p inconnues. La technique principale, appelée méthode du Pivot de Gauss est
très importante et on s'en servira beaucoup, notamment dans le cadre de l'algèbre
linéaire (et donc des matrices).
1.1       Introduction

Dénition 1.1. On appelle système linéaire (S) de n équations à p inconnues un
système d'équations de la forme
                       
                       
                        a1,1 x1 + a1,2 x2 + · · · + a1,p xp   = b1 (L1 )
                        a2,1 x1 + a2,2 x2 + · · · + a2,p xp
                       
                                                               = b2 (L2 )
                 (S) :                    ..                      .
                       
                       
                                          .                   = ..
                        a x + a x + ··· + a x                 = bn (Ln )
                          n,1 1     n,2 2             n,p p

où les ai,j sont des nombres réels xés appelés coecients du système et les (bi)i=1,...,n
sont des réels xés qui constituent le second membre du système. Les x1 , . . . , xp sont
les p inconnues du sytème.
Par commodité, chaque équation est repérée par un nom : Li pour i-ème ligne.
Une solution du système est un p-uplet (x1 ; x2 ; . . . ; xp ) pour lesquels toutes les équa-
tions sont vériées.
Résoudre le système (S), c'est trouver l'ensemble des solutions de ce système.
    Tout étudiant a déjà rencontré par exemple des systèmes de deux équations à
deux inconnues pour lesquelles deux méthodes de résolution ont été présentées : par
substitution ou combinaisons linéaires. On verra dans la suite qu'on va généraliser
la méthode de combinaisons linéaires. On peut commencer par vérier qu'on sait
faire sans diculté l'exercice suivant.
Dénition 1.2. Un système est dit :
    1. compatible lorsqu'il admet au moins une solution, incompatible s'il n'en admet
       aucune ;
    2. homogène lorsque le second membre est constitué uniquement de coecients
       nuls. On appelle système homogène associé à un système (S) le système ob-
       tenu en gardant les mêmes coecients et en remplaçant le second membre
       par des 0 ;
                                                                                           1
~~~

## Page 6

~~~text
1 .   Systèmes linéaires

      3. de Cramer lorsque n = p et lorsque le système possède une unique solution ;
      4. triangulaire (ou échelonné) lorsqu'il est de la forme :
                      
                      
                       a1,1 x1 + a1,2 x2 + · · · + a1,n xn = b1
                                  a2,2 x2 + · · · + a2,n xn = b2
                      
                      
                                            ...        ..      .
                      
                      
                                                       .   = ..
                                                   an,n xn = bn

      5. Deux systèmes sont dits équivalents lorsqu'ils ont le même ensemble de solu-
         tions.
    Tout système linéaire se ramène à un système échelonné équivalent en utilisant
trois types d'opérations élémentaires :
    1. Intervertir deux équations : ,
    2. Intervertir l'ordre des inconnues,
    3. Remplacer une équation par combinaisosns linéaires des autres équations.
1.2       Échelonner un système d'équations linéaires

          par la méthode de Gauss

   L'idée est de résoudre le système en combinant des lignes pour éliminer des
coecients, car ce genre d'opérations permet toujours de se ramener à un système
équivalent à celui de départ.
Proposition 1.3. Les opérations suivantes conduisent à un système équivalent au
système précédent : (1)Li ↔ Lj : échanger les lignes i et j .
(2)Li ← aLi , où a ∈ R : multiplier la ligne i par a.
(3)Li ← Li + bLj , où i 6= j, b ∈ R : ajouter b fois la ligne j à la ligne a.
(4)Li ← aLi + bLj , où i 6= j , a ∈ R, b ∈ R : remplacer Li par aLi + bLj


   Étant donné un système d'équations linéaires, la méthode du pivot de Gauss
a pour but est de construire un système échelonné qui soit équivalent au système
donné; les systèmes échelonnés sont, en eet, faciles à résoudre.
      Un premier exemple

   Pour expliquer cette méthode le plus simple est de commencer par un exemple.
Considérons le système dont les inconnues sont x, y, z, t et où a, b sont des
paramètres xés.
                                                                 
                      x + 2y + z − t = a                    (E1 )
                  S   2x + 4y − z − 5t = 5a                 (E2 ) 
                       −x − 2y + z + 3t = b                  (E3 )
                     

Choisissons une équation avec un coecient non nul pour la première inconnue x. Ici
la première équation convient avec le coecient 1, pour x, qu'on appelle le premier
2
~~~

## Page 7

~~~text
                                      1.2 Échelonner un système d'équations linéaires

                                                                par la méthode de Gauss


pivot. On va utiliser ce pivot de notre algorithme pour faire disparaître l'inconnue
x des autres équations. Pour cela on ajoute à ces équations la première multipliée
par un coecient convenable. On obtient un système linéaire équivalent :
            
                                                           (E10 ) = (E1 )
                                                                                  
             x + 2y + z − t =     a
       S 0          − 3z − 3t = 3a                        (E20 ) = (E2 ) − 2(E1 ) 
                     + 2z + 2t = b + a                     (E30 ) = (E3 ) + (E1 )
            

Examinons maintenant le système obtenu en supprimant la première équation. On
remarque que la variable x n'y apparaît pas. La variable suivante y non plus. On est
ramené à un système de deux équations avec ici deux variables en moins. Choisissons
notre deuxième pivot. On le trouve dans l'équation (E ). C'est le coecient −3 de
                                                            0

z . Nous allons l'utiliser pour éliminer z des équations suivantes (ici, il n'en reste
                                                            2


qu'une). Réécrivons notre nouveau système :
                                                           (E100 ) = (E10 )
          
           x + 2y + z − t =
                                                                                           
                                a
      00
     S            − 3z − 3t =  3a                         (E200 ) = (E20 )                 
                                                                             2
                                                                                            
                          0 = b + 3a                       (E300 ) = (E30 ) + (E20 )
          
          
                                                                             3
   Le système obtenu a la forme d'un escalier, avec deux grandes marches. On dit
qu'on a échelonné le système.
   Description de l'algorithme

   Rappelons que le but est d'obtenir un système équivalent au système donné et
qui soit échelonné c'est-à-dire de la forme :
                                                                                              
     x1 + a1,2 x2 + ...        ...              ...            + a1,n xn =        b1

                                ...
    
    
   
   
                    x2         +          a2,3 x3 + ...        + a2,n xn =        b2
                                                                                     
   
                                                                                    
   
                                                                                    
                                      xp + ap,p+1 xp+1 + ... + ap,n xn        = bp 
                                                                                    
   
                                                                  0           = bp+1 
                                                                                       ..
                                                                                   
   
    
   
                                                                                    
   
    
                                                                                    
    
    
                                                                        0     =   bm

avec 1 ≤ p ≤ m. Avec l'exemple précédent on peut comprendre facilement le fonc-
tionnement de l'algorithme pour un système quelconque d'équations.
    1. On cherche un pivot, premier coecient non nul d'une certaine variable x
       dans une des équations. Par permutation, cette équation devient la première
                                                                                                    i


       équation.
    2. On utilise ce pivot et cette équation pour éliminer x des équations suivantes.
       Pour cela on ajoute cette équation multipliée par un coecient convenable
                                                                i


       aux équations suivantes.
    3. S'il y a des équations dont le premier membre est nul 0 = . . . on les place en
       dernier.
                                                                                     3
~~~

## Page 8

~~~text
1 .   Systèmes linéaires

    4. On recommence à l'étape 1 avec le système privé de la première équation.
L'algorithme s'arrête lorsqu'il ne reste plus que des équations 0 = . . ..

Proposition 1.4.        1. Un système échelonné possède des solutions si et seule-
        ment si les équations de compatibilité sont satisfaites (portant sur les don-
        nées).
    2. Si ces conditions sont satisfaites alors toute donnée des inconnues non prin-
       cipales détermine une unique solution du système. C'est équivaut à dire les
       solutions du sytème sont paramétrées par les inconnues non principales :
   Les inconnues des lignes non nulles s'appellent les inconnues principales, ou
pivots

   Exprimons plus en détails une des étapes de cet algorithme. L'objectif est d'ob-
tenir, à l'issue de l'étape k un système de la forme H suivante :        k

                                                                                                             
  xn1 + a1,n1 +1 xn1 +1 + ...                   ...                ...                 +   a1,n xn   =   b1

                                                 ...
 
 


                          xn 2                  +        a2,n2 +1 xn2 +1 + ...         +   a2,n xn   =   b2    
                                                                                                                

                                                                                                               

                                                                                                               
                                                       xnk + ak,nk +1 xnk +1 + ... + ak,n xn = bk              ,
                                                                                                               

                                                       0 + ak+1,nk +1 xnk +1 + ... + ak+1,n xn = bk+1
                                                                                                          ..
                                                                                                              

                                                                                                               

                                                                                                               

 
                                                                                                               
 
 
                                                       0 + am,nk +1 xnk +1 + ...        +   am,n xn   =   bm

avec 1 ≤ n < n < ... < n ≤ n.
             1       2               k


    Décrivons à présent l'étape k de la méthode du Pivot de Gauss : étant donné un
système de la forme H , nous allons le transformer de façon à obtenir un système
de la forme H .
                              k−1


    Nous noterons E la j équation du système.
                 k
                                    ème

     On ne modie pas les k − 1 premières équations du système linéaire.
                          j


     Si tous les coecients a (avec l ≥ k et m > n ) sont nuls, alors, pour
        tout l ≥ k, l'équation E s'écrit : 0 = b . Le système a donc la forme voulue.
                                           l,m                               k−1


        L'algorithme s'arrête.
                                           l                l


     Sinon, on pose n := min{m : ∃l ≥ k : a 6= 0}. Alors, quitte à échanger
        la ligne k avec une ligne p ≥ k (telle que a 6= 0), on se ramène au cas où
                               k                                  l,m


              est non nul (ce sera notre pivot pour l'étape k).
                                                                  p,nk
        a
        On remplace alors l'équation E par E pour se ramener à : a = 1.
          k,nk
                                                            1

     Puis, pour tout p > k, on remplace E par E − a E (an d'éliminer les
                                                   k      ak,nk   k                            k,nk


        termes en x des équations k + 1, ..., m).
                                                           p            p    p,nk   k


     Le système d'équations linéaires ainsi obtenu est alors de la forme H , l'étape
                         nk


        k est nie.
                                                                                                k




Un autre exemple
4
~~~

## Page 9

~~~text
                                       1.2 Échelonner un système d'équations linéaires

                                                                        par la méthode de Gauss




Pour résoudre le système suivant dans R , on veut échelonner ce système :
                                                 4

                                                                                
                  x + y −
                                      z        +  t       =            1   (E1 )
                
                                                 8t       =            2   (E2 ) 
                                                                                  
                 2x + 2y +            z       + 3t       =            2   (E3 ) 
                 
                                       2z              + u =            0   (E4 )
                 

Nous allons utiliser la méthode précédente : à chaque étape, le pivot sera encadré.
Les systèmes d'équations linéaires obtenus sont équivalents au système donné.
    Il y a un terme en x dans la première équation, notre premier pivot de Gauss
sera ce terme : nous l'utilisons pour éliminer les termes en x des autres équations
          
            
              x   +   y  −    z   +   t          =   1        (E )
                                                                           
                                                                              1

         
                                  8t    = 2       (E2 )      
                                                                           
                                                0
         
                              3z + t     = 0 (E3 = E3 − 2E1 ) 
                               2z + 0 + u = 0       (E4 )
           

Nous oublions à présent la première ligne; il n'y a pas de terme en y dans les
équations E , E et E ; il y a un terme en z dans E mais pas dans E ; nous
                 0                                                  0

permutons donc les équations E et E
            2    3     4                                            3                       2
                                            0
                                   2        3
                                                                              
              x + y − z + t
                                                          =     1     (E1 )
            
                      3z + t                              =     0 (E20 = E30 ) 
                                                                                
            
                           8t                             =     2 (E300 = E2 ) 
                       2z + 0 + u                          =     0     (E4 )
             

Nous divisons la deuxième équation par 3 de sorte à avoir z au lieu de 3z dans la
deuxième équation
                                                                                      
           x + y −
                              z  t+   =                             1           (E1 )
         
                              z 1
                                 3
                                   +
                                   t = 0                       (E200 = 13 E20 )         
                                                                                        
         
                                8t    =                             2          (E300 ) 
                            2z + 0 + u =                             0           (E4 )
          

Le terme en z de la deuxième équation est notre nouveau pivot de Gauss; nous
l'utilisons pour éliminer les termes en z des équations situés en dessous
                                                                                 
          x + y −         z       +    t              =    1           (E1 )
                           z
         
        
                                  +    1
                                        3
                                          t            =    0          (E200 )     
                                                                                   
                                                                          00
        
                                       8t             =    2          (E3 )       
                                                                    0          00
                                       − 23 t + u      =    0     (E4 = E4 − 2E2 )
         

Nous oublions à présent la deuxième équation; il y a un terme en t dans la troisième
équation, nous divisons la troisième équation par 8 de sorte à avoir t à la place de
8t dans cette équation
                                                                            
             x + y − z +
                                           t              = 1       (E1 )
           
                     z +                   1
                                            3
                                              t            = 0       (E200 )  
                                                                              
                                                             1   000     1 00 
           
                                           t              = 4 (E3 = 8 E3 )
                                           − 23 t + u      = 0       (E40 )
            

                                                                                                5
~~~

## Page 10

~~~text
1 .   Systèmes linéaires

Le terme en t de la troisième équation devient notre nouveau pivot de Gauss : nous
l'utilisons pour éliminer les termes en t de la quatrième équation
                                                                          
              x + y − z +
                                    t       = 1              (E1 )
                       z +           1
                                       t     = 0              (E200 )
                                      t
                                                                          
                                    3                                      
            
                                            = 14       (E3000 = 18 E300 )  
                                                        00      0     2 000
                                           u = 16     (E4 = E4 + 3 E3 )
             

Ce système d'équations linéaires est échelonné et équivalent à notre système initial.
1.3        Rang d'une matrice

Dénition 1.5. Une matrice B est dite èchelonnèe en lignes si
      1. chaque ligne non nulle de B commence avec strictement plus de 0 que la ligne
         précédente, et
      2. les lignes nulles (ne contenant que des 0) de B viennent en bas après les
         lignes non nulles.
    Toute matrice A peut se réduire à une matrice échelonnée en lignes B par une
suite d'opérations élémentaires sur les lignes. On appelle B la forme échelonnée en
lignes de A.
Une des concepts fondamentaux dans l'algèbre linéaire est le rang d'une matrice. Il
admet de plusieurs dénitions équivalentes. En voici la première.
Dénition 1.6. Le rang d'une matrice A est le nombre de lignes non nulles dans
sa forme échelonnée en lignes. On le note rgA.
Exemple 1.7. La matrice suivante A se réduit en sa forme échelonnée en lignes
par les pivotages
                             
                    1 −3 6 2
              A =  2 −5 10 3  L2 ← L2 − 2L1 et L3 ← L3 − 3L1
                    3 −8 17 4
                                                  
                1 −3 6 2                   1 −3 6 2
               0 1 −2 −1  L3 ← L3 − L2  0 1 −2 −1  .
                0 1 −1 −2                  0 0  1 −1
Donc on a rgA = 3. Pour la matrice suivante
                                                     
      1 3 2                 1 3 2                  1 3 2
C =  1 4 1  L2 ← L2 −L1  0 1 −1  L3 ← L3 −L2  0 1 −1 
      0 1 −1                0 1 −1                 0 0 0

on a rg(C) = 2.
Théorème 1.8. Pour toute matrice A on a
   rgA ⩽ nombre de lignes de A,
rgA ⩽ nombre de colonnes de A.
6
~~~

## Page 11

~~~text
                                                              1.3 Rang d'une matrice




   Idée de la preuve. En réduisant la matrice A en une matrice échelonnée en lignes
similaire à celle-ci                            
                                   1   3   0   4   5
                                  0   2   1   3   8 
                                                    
                                  0   0   0   7   2 
                                   0   0   0   0   0
les pivots (les premiers coecients non nuls des lignes non nulles) sont dans lignes
distinctes et dans des colonnes distinctes. Donc on a
nombre de pivots ⩽ nombre de lignes de A,
nombre de pivots ⩽ nombre de colonnes de A.
Le nombre de pivots est aussi le nombre de lignes non nulles de la forme échelonnée
de A, d'où
nombre de pivots = rgA.

1.3.1 La matrice des coecients
   On peut associer une matrice à chaque membre d'un système linéaire. Pour le
système                
                           x − 3y + 6z + 2w   = −1,
                            2x − 5y + 10z + 3w = 0,
                            3x − 8y + 17z + 4w = 1,
                          

on a des matrices
                                                        
                           1 −3 6 2                     −1
                     A =  2 −5 10 3               b= 0 
                           3 −8 17 4                    1

avec A la matrice des coecients regroupant les coecients des variables du membre
de gauche du système, et le vecteur colonne b contient le membre de droite. Quand
on met les deux ensemble, on a la matrice augmentée quéon a déjà vue
                                             
                                  1 −3 6 2 −1
                            B =  2 −5 10 3 0 
                                  3 −8 17 4 1

1.3.2 Le rang et les systèmes linèaires
    On va étudier les systèmes linéaires en considérant le membre de gauche comme
xe, mais le membre de droite comme éventuellement variable. Dans cette optique,
il est convenable de considérer le rang d'un syst`eme linéaire comme dépendant
uniquement de son membre de gauche. D'où :
Dénition 1.9. Le rang d'un système linéaire est le rang de sa matrice des coe-
cients A.
   Par exemple, le rang du système ci-dessus est 3, selon les calculs faits sur la page
précédente.
                                                                                      7
~~~

## Page 12

~~~text
1 .   Systèmes linéaires

1.4       Systèmes de Cramer

      On peut donner des critères selon lesquels un système sera de Cramer.
Théorème 1.10. Un système de n équations à n inconnues est un système de
Cramer si la méthode du pivot de Gauss fait apparaître successivement n pivots
(non nuls).
Théorème 1.11. Un système est de Cramer si et seulement si son système admet
une seule solution.
      Exercice . Pour quelles valeurs du paramètre λ le système suivant est de Cramer.
                              
                               2x + 3y + z = 4
                                −x + λy + 2z = 5
                                7x + 3y + (λ − 5)z = 7
                              




8
~~~

## Page 13

~~~text
Chapitre 2
Groupe

2.1         Lois de composition internes

       Dans tout ce chapitre, E est un ensemble.
Dénition 2.1. On appelle loi de composition interne sur E (lci) toute application
de E × E dans E .
Dénition 2.2. On appelle magma tout couple constitué d'un ensemble et d'une
lci.
Exemple 2.3. (Z, −) est un magma, mais pas (N, −), car −4 ∈/ N.
       Dans toute la suite, ? est une lci sur E.
2.1.1 Propriétés usuelles des lci
Dénition 2.4. Soit (E, ?) un magma.
On dit que E est associatif si pour tout x, y, z ∈ E , on a : x ? (y ? z) = (x ? y) ? z .
L'élément x ? (y ? z) = (x ? y) ? z est alors noté x ? y ? z .
On dit que E est commutatif si pour tout x, y ∈ E , on a : x ? y = y ? x.
Soit ] une seconde lci sur E . On dit que dans E ? est distributive par rapport à ] si
pour tout x, y, z ∈ E , on a :
    x ? (y]z) = (x ? y)](x ∗ z)
    (y]z) ? x = (y ? x)](z ? x).
Remarque 2.5. On dit que dans (E, ?) est distributive à gauche par rapport à ] si
pour tout x, y, z ∈ E , on a : x ? (y]z) = (x ? y)](x ? z). De même, on a la notion de
distributivié à droite.
Exemple 2.6.            1. C, R, Q, Z, N avec + ou × sont associatifs, mais pas (Z, −)
          car 1 − (2 − 3) 6= (1 − 2) − 3.
       2. C, R, Q, Z, N avec + ou × sont commutatifs, mais pas (Z, −), ni (F(R, R), ◦).
       3. Sur C, R, Q, Z, N× est distributive par rapport à +, et sur P(E), ∩ et ∪ sont
          distributives l'une par rapport à l'autre.
                                                                                       9
~~~

## Page 14

~~~text
2 .   Groupe

Dénition 2.7.           1. Soit e ∈ E . on dit que e est un élément neutre à gauche
         (resp. à droite) pour ? si pour tout x ∈ E on a e ? x = x (resp. x ? e = x). On
         dit que e est un élément neutre pour ? si c'est un élément neutre à gauche et
         à droite, i.e. pour tout x ∈ E, e ? x = x ? e = x.
      2. Soit e un neutre pour ? et soit x ∈ E . On dit que x est inversible à gauche
         (resp. à droite) s'il existe un élément y ∈ E tel que y ? x = e (resp. x ? y = e).
         Un tel élément y s'appelle UN inverse à gauche (resp. à droite) de x. On dit
         que x est inversible s'il est inversible à gauche et à droite, i.e. il existe y ∈ E
         tel que y ? x = x ? y = e. Dans ce cas y est UN inverse de x.
Exemple 2.8.           0 est un élément neutre pour + dans R, C, Q, Z, N.

    1 est un élément neutre pour × dans R, C, Q.
    1E est un élément neutre pour dans F(E, E), et les bijections sont tous les
     éléments inversibles de cet ensemble.
Remarque 2.9.            1. Être inversible d'un seul côté ne sut pas pour être inver-
         sible tout court.
      2. Un neutre est toujours inversible et est son propre inverse.
Proposition 2.10. Si ? admet un neutre, alors ce neutre est unique.
      Preuve:
Soient e et e deux neutres. Alors e ? e = e et e ? e = e , donc e = e .
                0                          0             0   0             0
                                                                                           
Proposition 2.11. On suppose la loi ? associative, et admettant un neutre e. Si un
élément est inversible, alors il a un seul inverse.
      Preuve:
Soient y et y deux inverses de x ∈ E. Alors y ? x = e et x ? y = e. Donc y ? (x ? y ) =
                0                                                 0                    0

y ? e = y et (y ? x) ? y = e ? y = y , d'où y = y .
                         0        0    0             0
                                                                                      
Remarque 2.12. On utilise souvent les notations additives et multiplicatives.
      1. En notation additive, ? est en général notée +, x + x + · · · + x (n−fois(
         se note nx, et si x est inversible, son inverse se note −x. On l'appelle alors
         plutôt l'opposé de x. De même, on notera le neutre d'une telle structure 0,
         ou 0E .
      2. En notation multiplicative, ? est en général remplacée par × (et ce symbole
         est même souvent omis), x × x × · · · × x (n−fois) se note xn et si x est
         inversible, son inverse se note x−1 . De même, on notera le neutre d'une telle
         structure 1, ou 1E .
    Pour éviter toute erreur, on essaiera au maximum de n'utiliser la notation addi-
tive que pour des lois qui ont les mêmes propriétés que la loi + sur R.
Par exemple, noter + une lci non commutative peut-être déroutant, ainsi que pour
une lci pour laquelle tous les éléments ne sont pas inversibles. La notation + est
en général réservée à des lci commutatives et pour lesquelles les éléments sont tous
inversibles.
Ce n'est pas le cas pour la notation multiplicative, qui est la plus couramment utili-
sée pour des lois associatives, mais sans plus. Par exemple il est fréquent d'utiliser ×
10
~~~

## Page 15

~~~text
                                                                2.2 Structure de groupe




même pour une lci non commutative et pour laquelle les éléments ne sont pas tous
inversibles. Donc faites attention, par défaut on aura xy 6= yx, et x n'existera pas
                                                                        −1

forcément!
Dans toute la suite, on adoptera la notation multiplicative, et on suppose que E a
un neutre noté 1.
Proposition 2.13. On suppose la loi ? associative. Soient x, y, z ∈ E .
      1. Simplication par un inversible : si x est inversible, alors x?y = x?z ⇔ y = z .
      2. Inverse d'un produit : si x et y sont inversibles alors x ? y l'est aussi et
         (x ? y)−1 = y −1 ? x−1 . Attention : l'inverse de x ? y n'a aucune raison
         d'être x−1 ? y−1 .
      3. Puissances négatives : si x est inversible, on pose pour n ∈ N∗ , x−n = (x−1 )n .
         Alors x−n = (xn )−1 .
      4. Inverse d'un inverse : si x est inversible, x−1 l'est aussi et (x−1 )−1 = x.
      Preuve:




(3) Par récurrence. Vrai si n = 0 ou 1. Si vrai pour n, alors x           n+1
                                                                                ? x−n−1 =

x ? x ? x ? x = x ? e ? x = x ? x = e.
 n         −1    −n      n       −n     n    −n

(4) Vrai par unicité de l'inverse.                                                      

Dénition 2.14. Soit (E, ?) un magma et F une partie de E . On dit que F est
une partie stable (de E par ? ) si pour tous x, y ∈ F, x ? y ∈ F .
Exemple 2.15. {−1, 1} est une partie stable de (R, ×), mais pas {−2, 2}.


2.2       Structure de groupe

2.2.1       Dénition et exemples
Dénition 2.16. On appelle groupe tout magma associatif, ayant un neutre, et dont
tout élément est inversible. Si un groupe est commutatif (ce qui signie en fait que sa
loi est commutative), il est dit abélien. Par défaut on utilise la notation multiplicative
pour un groupe, sauf pour les groupes abéliens pour lesquels on utilise la notation
additive.
Exemple 2.17.             1. C, R, Q, Z sont des groupes avec la loi +, mais pas avec la
         loi ×.
      2. Pour n ∈ N∗ , Cn , Rn , Qn , Zn sont des groupes avec la loi +.
      3. C∗ , R∗ , Q∗ , sont des groupes avec la loi ×.
                                                                                       11
~~~

## Page 16

~~~text
2 .   Groupe

      4. N n'est un groupe ni avec la loi + ni avec la loi ×.




Dénition 2.18. Soit X un ensemble non vide. On appelle groupe des permutations
de X l'ensemble des bijections de X dans X . Comme son nom l'indique, c'est un
groupe, si on le munit de la loi de composition ◦. On le note SX .

2.2.2 Sous-groupes
   Dans toute la suite, (G, ?) est un groupe de neutre e. On adopte la notation
multiplicative
Dénition 2.19. On appelle sous-groupe de G tout ensemble H vériant les pro-
priétés suivantes :
    1. H ⊂ G ;
    2. e ∈ H ;
    3. Stabilité par produit : ∀x, y ∈ H, x ? y ∈ H ;
    4. Stabilité par passage à l'inverse : ∀x ∈ H , on a x−1 ∈ H .
Exemple 2.20. Sont des sous-groupes :
      1. {e} et G dans (G, ?).
      2. U dans (C∗ , ×).
      3. nZ dans (Z, +).
      4. H = {f ∈ SR | f (0) = 0} dans (SR , ◦).
Proposition 2.21. Un ensemble H est un sous groupe de G si et seulement si H
est un sous-ensemble non vide de G et pour tout (x, y) ∈ H 2 , on a x−1 ? y ∈ H .
      Preuve:
Montrons l'implication et sa réciproque :
   1. "⇒" Supposons que H est un sous-groupe de G. Alors H contient e et n'est
      donc pas vide. De plus, soit (x, y) ∈ H . H étant stable par passage à l'inverse,
      on a alors x ∈ H et par stabilité par produit, on a donc x ? y ∈ H .
                        −1                                               −1

   2. "⇐" Réciproquement, supposons que H est non vide et que pour tout (x, y) ∈
      H , on a x ? y ∈ H . Montrons que H possède les trois propriétés énumérées
           2        −1

      dans sa dénition :
     (a) H étant non vide, il possède au moins un élé- ment x . On a alors e =
         x ? x ∈ H.
                                                                     0
               −1
               0    0

12
~~~

## Page 17

~~~text
                                                                  2.2 Structure de groupe




      (b) Soit x ∈ H . On a alors (x, e) ∈ H , donc x ? e ∈ H .
                                                  2        −1

      (c) Soit (x, y) ∈ H . D'après ce qui précède, on a alors x             −1
                                                                                  ∈ H   , donc
          (x , y) ∈ H , donc x ∗ y = (x ) ? y ∈ H .
             −1         2                      −1 −1

                                                                                            
Remarque 2.22. On obtient une proposition vraie également en remplaçant ci-
dessus la condition x−1 ? y ∈ H par x ? y −1 ∈ H .
Théorème 2.23. Un sous-groupe muni de la loi induite du groupe est lui-même un
groupe.
   Preuve:
Soit (G, ?) un groupe de neutre e et H un sous-groupe de G.
    1. Montrons qu'on peut restreindre ? : G × G → G au départ à H × H et à
       l'arrivée à H . On appellera alors loi induite par ? sur H cette restriction de ?.
       On a H ×H ⊂ G×G, donc la restriction au départ est légitime, pour eectuer
       la restriction à l'arrivée, il sut de montrer que pour tout (x, y) ∈ H , on a   2

       x ? y ∈ H , c'est-à-dire que H est stable par ?. Or H est un sous-groupe de G
       donc c'est évident.
    2. H muni de la loi induite par ? est un magma associatif. En eet (G, ?) est
       un magma associatif, on a donc
                            ∀(x, y, z) ∈ G3      (x ? y) ? z = x ? (y ? z)
       Or H ⊂ G donc
                            ∀(x, y, z) ∈ H 3     (x ? y) ? z = x ? (y ? z)
       Donc la restriction de ? à 0H est associative, d'où le résultat.
    3. e est neutre pour la loi induite par ? sur H . En eet, e est le neutre de ?,
       donc
                                 ∀x ∈ G      e?x=x?e=x
       D'où le résultat.
    4. Tout élément de H admet un inverse pour la loi induite par ?. En eet tout
       élément x de H admet un inverse x dans G pour la loi ? et par stabilité de
                                                −1

       l'inverse sur le sous-groupe H , on a x ∈ H . Donc tout élément de H admet
                                                  −1

       un inverse dans H pour la loi induite par ?.
    5. On déduit des points précédents que H muni de la loi induite par ? est un
       groupe.
                                                                                            
Remarque 2.24. Il est plus facile de montrer qu'un ensemble est un sous-groupe
que de montrer que c'est un groupe (pas besoin de redémontrer l'associativité, etc.).
Par exemple (U, ×) est un groupe, vu comme sous-groupe de (C∗ , ×).
À chaque fois que l'on essaiera de montrer qu'un ensemble est muni d'une structure
de groupe, on tentera de le voir comme un sous-groupe d'un groupe bien connu.
Remarque 2.25. La réciproque de ce théorème est également vraie (bien que moins
utilisée) : si H est un sous-ensemble de G tel que, muni de la loi induite par celle
de G, H soit un groupe, alors H est un sous-groupe de G.
Exemple 2.26. Si n ∈ N∗ , Un est un sous-groupe de (U, ×), donc (Un , ×) est un
groupe.
                                                                                            13
~~~

## Page 18

~~~text
2 .   Groupe

2.2.3 Morphismes de groupes
Dénition 2.27. Soient (G, ?) et (G0 , ]) deux groupes et ϕ : G → G0 .
      1. On dit que ϕ est un morphisme du groupe (G, ?) dans le groupe (G0 , ]), si
                          ∀x, y ∈ G,          ϕ(x ? y) = ϕ(x)]ϕ(y).

      2. Tout morphisme d'un groupe dans lui-même est appelé endomorphisme.
      3. Tout morphisme de G dans G0 qui est une bijection est appelé isomorphisme
         de G sur G0 . Dans ce cas on dit que G et G0 sont isomorphes. Un morphisme
         qui est à la fois un isomorphisme et un endomorphisme est appelé automor-
         phisme.
Exemple 2.28.         1. (Z, +) → (Z, +), x 7→ 2x est un morphisme, mais pas un
         isomorphisme.




      2. (C∗ , ×) → (R∗ , ×), z 7→ |z|, est un morphisme, mais pas un isomorphisme.




      3. (R, +) → (C∗ , ×), x 7→ eix , est un morphisme, mais pas un isomorphisme.




      4. (R, +) → (R∗+ , ×), x 7→ ex est un isomorphisme de réciproque ln, qui est
         aussi un isomorphisme.




Exemple 2.29. Etudions les applications suivantes
      1. Si n ∈ N∗ ,
                                 ϕn : (C∗ , ×) → (C∗ , ×)
                                        z      7→  zn




14
~~~

## Page 19

~~~text
                                                                       2.2 Structure de groupe




   2. Si n ∈ N∗ et a1 , . . . , an ∈ Kn , l'application
                           ϕn :        (Kn , +)          →       (K, +)
                                     (x1 , . . . , xn ) 7→ a1 x1 + · · · + an xn




   Dans toute la suite, (G, ?) et (G , ]) sont deux groupes de neutres e et e , on
                                            0                                            0

adopte une notation muliplicative, et ϕ : G → G est un morphisme.
                                                           0


Théorème 2.30. Soit ϕ un morphisme de G sur G0 , on a, e et e0 désignant les
neutres de G et G0 :
   1. ϕ(e) = e0 ;
   2. ∀x ∈ G, ϕ(x−1 ) = (ϕ(x))−1 .
   Preuve:

   1. On a ϕ(e)]ϕ(e) = ϕ(e ? e) = ϕ(e) = ϕ(e)]e , donc en simpliant par ϕ(e), on
                                                               0

      en déduit ϕ(e) = e .  0

   2. Soit x ∈ G. Alors ϕ(x )]ϕ(x) = ϕ(x ? x) = ϕ(e) = e.
                                −1                    −1

                                                                                             
Corollaire 2.31. Sous les mêmes hypothèses, on a
                          ∀x ∈ G         ∀k ∈ Z         ϕ(xk ) = ϕ(x)k .
   Preuve:
Soit x ∈ G. D'après le théorème ci-dessus, on a
                                ϕ(x0 ) = ϕ(e) = e0 = ϕ(x)0 .
On peut alors démontrer par récurrence que pour tout n ∈ N, on a ϕ(x ) = ϕ(x)      n          n

(l'hérédité résulte directement de la dénition de morphisme).
D'après le théorème ci-dessus, pour tout n ∈ N,
                                      ϕ(x−n ) = ϕ(xn)−1
d'où ϕ(x ) = ϕ(x) . On en déduit le résultat.
        −n           −n
                                                                                             
Exemple 2.32.      1. C∗ → R∗ , z 7→ |z| est un morphisme de (C∗ , ×) dans (R∗ , ×),
      donc pour tout z ∈ C∗ , on a
                                                    1     1
                                                |     |=
                                                    z    |z|




                                                                                             15
~~~

## Page 20

~~~text
2 .   Groupe

      2. exp est un morphisme de (C, +) dans (C∗ , ×), donc pour tout z ∈ C, e−z =
          1
         ez
            .




      3. ln est un morphisme de (R∗+ , ×) dans (R, +), donc pour tout x ∈ R∗+ , on a
         ln( x1 ) = − ln(x).




Théorème 2.33.           1. La composée de deux morphismes de groupes est un mor-
         phisme de groupe. Plus précisément, soit (G1 , ?1 ), (G2 , ?2 ) et (G3 , ?3 ) trois
         groupes, ϕ un morphisme de G1 dans G2 et ϕ un morphisme de G2 dans G3 .
         Alors ψ ◦ ϕ est un morphisme de G1 dans G3 .
      2. La fonction réciproque d'un isomorphisme (en tant qu'application bijective)
         est un isomorphisme. Plus précisément, soit (G1 , ?1 ) et (G2 , ?2 ) deux groupes
         et ϕ un isomorphisme de G1 sur G2 . Alors ϕ−1 est un isomorphisme de G2
         sur G1 .
      Preuve:




                                                                                          

16
~~~

## Page 21

~~~text
                                                                                    2.2 Structure de groupe




Théorème 2.34.         1. L'image d'un sous-groupe par un morphisme de groupes
       est un sous-groupe.
    2. L'image réciproque d'un sous-groupe par un morphisme est un sous-groupe.
   Preuve:
Les démonstrations pour montrer qu'un ensemble est un sous-groupe ont TOU-
JOURS la même structure.
    1. Soient (G, ?) et (G , ]) deux groupes de neutres respectifs e et e , et ϕ : G → G
                                       0                                                         0                0

       un morphisme de groupes. Soit H un sous-groupe de G. Montrons que ϕ(H)
       est un sous-groupe de G .               0

      (a) On a évidemment ϕ(H) ∈ G et de plus e ∈ H et e = ϕ(e) ∈ ϕ(H).
                                                             0                          0

      (b) Soit x, y ∈ ϕ(H). Alors x possède un antécédent x ∈ H et y un antécédent  0

           y ∈ H par ϕ. On a alors successivement
                0


                     x]y          −1
                              = ϕ(x )]ϕ(y )         par dénition dex et y
                                                     0           0 −1                            0   0

                              = ϕ(x )]ϕ(y )         car ϕ est un morphisme
                                                     0           0−1

                              = ϕ(x ? y )         car ϕ est un morphisme
                                                     0       0−1


           Donc x]y ∈ ϕ(H).  −1

           ϕ(H) est donc un sous-groupe de G .                          0

    2. Gardons les même notations que dans le premier point, et notons H un                                  0

       sous-groupe de G .          0

      (a) On a évidemment ϕ (H ) ⊂ G et de plus e ∈ H et e = ϕ(e) ∈ H donc
                                               −1        0                      0   0       0            0

           e ∈ ϕ (H ).  −1    0

      (b) Soit x, y ∈ ϕ (H ). Alors ϕ(x), ϕ(y) ∈ H et donc ϕ(x?y ) = ϕ(x)](ϕ(y)) ∈
                                  −1       0                                0                   −1                    −1

           H donc x ? y ∈ ϕ (H ).
                    0              −1          −1        0

           ϕ (H) est donc un sous-groupe de G.
                −1

                                                                                                                 

Remarque 2.35. lorsque l'on veut montrer qu'un ensemble est muni d'une structure
de groupe, on commence toujours par essayer de l'identier comme image réciproque
(ou directe) d'un sous-groupe d'un groupe bien connu par un morphisme.
Dénition 2.36.        1. On appelle noyau de ϕ, noté Ker ϕ, l'image réciproque de
       {e } par ϕ, autrement dit l'ensemble des antécédents de e0 par ϕ
            0


                                               Ker ϕ = {x ∈ G | ϕ(x) = e0 }.

    2. On appelle image de ϕ notée Im ϕ, l'image directe de G par ϕ. Autrement dit

                                                    Im ϕ = {ϕ(x) | x ∈ G}.

Théorème 2.37. Les noyaux et les images sont des sous-groupes respectivement de
G et G0 .

   Preuve:
Montrons que Ker ϕ est un sous-groupe de G :
                                                                                                                 17
~~~

## Page 22

~~~text
2 .   Groupe

      1. On a évidemment Ker ϕ ⊂ G et de plus ϕ(e) = e donc Ker ϕ est un sous-
                                                             0

         ensemble non vide de G.
      2. Soit x, y ∈ Ker ϕ. Alors on a successivement
                                  ϕ(x ? y −1 ) = ϕ(x)]ϕ(y)−1
                                               = e0 ]e0−1
                                               = e0

         Donc x ? y ∈ Kerϕ.
                    −1

         Donc Ker ϕ est un sous-groupe de G.




                                                                                     


Remarque 2.38. lorsque l'on veut montrer qu'un ensemble est muni d'une structure
de groupe, on commence toujours par essayer de l'identier comme noyau ou image
d'un morphisme.
Exemple 2.39. U est le noyau du morphisme  module , de (C∗ , ×) dans (R∗ , ×).




Proposition 2.40. Soit ϕ : G → G0 un morphisme de groupes, soit x, y ∈ G. Alors
ϕ(x) = ϕ(y) si et seulement si x ? y −1 ∈ Ker ϕ.

      Preuve:
ϕ(x) = ϕ(y)     si et seulement si ϕ(x)]ϕ(y) = e si et seulement si ϕ(x ? y ) = e . 
                                           −1     0                       −1     0


Théorème 2.41.            1. ϕ injectif si et seulement si Ker ϕ = {e}.
      2. ϕ surjectif si et seulement si Im ϕ = G0 .
      Preuve:

18
~~~

## Page 23

~~~text
                                                          2.2 Structure de groupe




   1. On montre l'implication et sa réciproque :
      "⇒" Supposons ϕ injectif. Alors e a au plus un antécédent par ϕ. Or ϕ(e) = e
                                      0                                          0

      donc il en a au moins un : e. Donc Ker ϕ = {e}.
      "⇐" Réciproquement, supposons Ker ϕ = {e} et montrons que ϕ est injectif.
      Soit (x, y) ∈ G vériant ϕ(x) = ϕ(y). Alors on a succesivement
                     2


                   ϕ(x ? y ) = ϕ(x)]ϕ(y) car ϕ est un morphisme
                         −1                −1

                              = ϕ(x)]ϕ(x)−1
                              = e0

      Donc x ? y ∈ Kerϕ, donc x ? y = e, donc x = y.
                −1                    −1

                                                                                

Remarque 2.42. Pour montrer qu'un morphisme est injectif, on utilisera TOU-
JOURS le noyau et JAMAIS (ou presque) la méthode classique pour des fonctions
quelconques : c'est beaucoup plus rapide !




                                                                               19
~~~

## Page 24

![Fac-similé de la page 24](../facsimiles/8fecb02eee36dd924db299bf.jpg)

~~~text
2 .   Groupe




20
~~~



## Page 25

~~~text
Chapitre 3
Espace vectoriel

3.1      Espace vectoriel

  L'ensemble K désigne toujours R ou C.
Dénition 3.1. On appelle K-espace vectoriel (ou espace vectoriel sev K) tout
ensemble non vide E muni d'une loi de comoposition interne notée ? et d'une loi
de composition externe notée . :

                                      K×E →            E
                                       (λ, x)    7→ λ.x

telles que :
  (1) (E, ?) est un groupe abélien ;
  (2) ∀λ, µ ∈ K, ∀x ∈ E , on a (λ + µ).x = λ.x ? µ.x ;
  (3) ∀λ ∈ K, ∀x, y ∈ E , on a λ.(x ? y) = λ.x ? λ.y ;
  (4) ∀λ, µ ∈ K, ∀x ∈ E , on a λ.(µ.x) = (λ × µ).x ;
  (5) ∀x ∈ E , on a 1.x = x.
Les éléments d'un espace vectoriel sont appelésvecteurs ; et les éléments de K sont
appelés scalaires
                .

   Lorsqu'il n'y a pas de confusion, on dira espace vectoriel au lieu de K-espace
vectoriel.
Exemple 3.2.         (1) L'ensemble des vecteurs du plan est un espace vectoriel.
  (2) (K, +, ×) est un K-espace vectoriel.
  (4) Sur R2 , on dénit les deux lois suivantes : pour (x, y), (x0 , y 0 ) ∈ R2 et λ ∈ R,

               (x, y) ⊕ (x0 , y 0 ) := (x + x0 , y + y 0 ) et λ ⊗ (x, y) := (λ × x, λ × y)

       alors (R2 , ⊕, ⊗) est un R-espace vectoriel.
                                                                                             21
~~~

## Page 26

~~~text
3 .   Espace vectoriel

     (5) Plus généralement : Si E1 , E2 , . . . , En sont n espaces vectoriels, alors l'espace
         produit E := E1 ×E2 ×· · ·×En est un espace vectoriel pour les lois suivantes :
         Pour tous (x1 , x2 , . . . , xn ), (y1 , y2 , . . . , yn ) ∈ E et λ ∈ K, on dénit

                 (x1 , x2 , . . . , xn ) ⊕ (y1 , y2 , . . . , yn ) = (x1 + y1 , x2 + y2 , . . . , xn + yn )
                 λ ⊗ (x1 , x2 , . . . , xn ) = (λ × x1 , λ × x2 , . . . , λ × xn ).

     (6) L'ensemble (Kn [X], +, ×) des polynômes de degré inférieur ou égal à n ad-
         ditionné du polynôme nul est un espace vectoriel.
Proposition 3.3. Pour tout λ, µ ∈ K et pour tout x, y ∈ E , on a : λ.x = 0E ⇐⇒
λ = 0 ou x = 0E .


3.2        Sous-espace vectoriel

      Dans toute la suite l'ensemble (E, ?, .) désignera un espace vectoriel sur K.
3.2.1 Dénition
Dénition 3.4. Soit F un sous-ensemble de E . On dit que F est un sous-espace
vectoriel de E si F possède les propriétés suivantes :
   (1) 0E ∈ F ;
   (2) ∀x, y ∈ F , x ? y ∈ F . Autrement dit F est stable par l'addition ;
   (3) ∀x ∈ F et ∀λ ∈ K, λ.x ∈ F . Autrement dit, F est stable par la multiplication
       par scalaire.
Remarque 3.5. Tout sous-espace vectoriel de E , est un espace vectoriel pour les
lois induites par E .
Exemple 3.6.               (1) Si E est un espace vectoriel, alors {0E } et E sont des sous-
         espaces vectoriel de E .
     (2) Si E = R2 , alors F = {(x, 0); x ∈ R} est un sous-espace vectoriel de E .
         De même, si (x0 , y0 ) ∈ R2 , alors F {(λx0 , λy0 ); λ ∈ R} est un sous-espace
         vectoriel de E .
     (3) L'ensemble F = {(x, y, z) ∈ R3 | z = 0} est un sous-esapce vectoriel de R3 .
     (4) H = {(x1 , . . . , xn ) ∈ Rn | x1 + · · · + xn = 0} est un sous-espace vectoriel
         de Rn . En eet Rn est un R-espace vectoriel de vecteur nul 0 = (0, . . . , 0).
         H ⊂ Rn et 0 = (0, . . . , 0) ∈ H car 0 + · · · + 0 = 0. Soient λ, µ ∈ R et x =
         (x1 , . . . , xn ), y = (y1 , . . . , yn ) ∈ H . On a λx+µy = (λx1 +µy1 , . . . , λxn +µyn ).
         Or (λx1 + µy1 ) + · · · + (λxn + µyn ) = λ(x1 + · · · + xn ) + µ(y1 + · · · + yn ) = 0
         car x1 + · · · + xn = y1 + · · · + yn = 0 puisque x, y ∈ H donc λx + µy ∈ H .
Corollaire 3.7. Soit (E, ?, .) un espace vectoriel et F un sous-ensemble de E (F ⊂
E ). Si F vérie les propriétés         (1) et (2) suivantes alors F est un sous-espace vectoriel
de E :
     (1) F est non vide (F contient l'élément neutre de E ).
22
~~~

## Page 27

~~~text
                 3.3 Sous-espace vectoriel engendré par une partie d'un espace vectoriel




     (2) ∀(x, y) ∈ F × F, ∀λ ∈ K, alors λ.x ? y ∈ F .
Exemple 3.8. Les parties suivantes ne sont pas des sous-espaces vectoriels de R2 :
      {(x, y) ∈ R2 | x + y = 1} car ne contient par le vecteur nul ;
      {(x, y) ∈ R2 | xy = 0} car non stable par addition ;
      {(x, y) ∈ R2 | x + y ∈ Z} car non stable par produit extérieur.
Proposition 3.9. Soient (E, ?, .) un espace
                                        T vectoriel et E1 , . . . , En des sous-espaces
vectoriels de E , alors l'intersection F =                  n
                                                            k=1 Ei      est un sous-espace vectoriel de E .
     Preuve:
Pour tout i, on a 0 ∈ E , donc 0 ∈ F . Soient x, y ∈ F et λ ∈ K alors pour tout i,
on a λ.x ? µ.y ∈ E donc λ.x ? µ.y est dans l'intersection de tout les E .
                                i
                      i                                                                      i

Remarque 3.10. La réunion de deux sous-espace vectoriels n'est pas en général un
sous-espace vectoriel.
En eet, si (E, ?, .) = (R2 , ⊕, ⊗), les sous-ensembles :

                                        E1 = {(x, y) ∈ R2 | x + y = 0}

et
                                        E2 = {(x, y) ∈ R2 | x − y = 0}
sont deux sous-espaces vectoriels de R2 mais E1 ∪ E2 n'est pas un sous-espace vec-
toriel.
Car par exemple, soient x, y ∈ R∗ , on a (x, −x) ∈ E1 et (y, y) ∈ E2 mais (x, −x) ⊕
(y, y) n'appartient ni à E1 ni à E2 .


3.3       Sous-espace vectoriel engendré par une partie

          d'un espace vectoriel

3.3.1 Combinaisons linéaires
   Soit {x , . . . , x } une famille de vecteurs Pd'un espace vectoriel (E, ?, .). Tout
vecteur de E de la forme a .x + ? . . . a .x = a .x , où les a ∈ R est appelé
             1        p
                                                                        p

combinaison linéaire des vecteurs x , k = 1 . . . , p.
                                        1   1           p   p           k=1   k   k       k
                                                    k

Remarque 3.11. On peut généraliser cette notion à une famille innie de vecteurs,
mais dans ce cas il faut que la suite des scalaires soit à support ni.

3.3.2 Dénitions et propriétés
    Soit A un sous-ensemble non-vide de l'espace vectoriel (E, ?, .). On note vect(A),
l'ensemble des combinaisons linéaires d'éléments de A. On a donc
                           λ .a | (λ ) est une famille de scalaires à support ni}.
                  P
      vect(A) = {         a∈A       a           a


Donc un élément x de E appartient à vect(A), si et seulement si, il existe x , . . . , x ∈
A et des scalaires λ , . . . , λ , tels que : x = λ .x ? · · · ? λ .x .
                                                                                                  1    n
                          1             n                       1   1             n   n

                                                                                         23
~~~

## Page 28

~~~text
3 .      Espace vectoriel

Théorème 3.12. Soit A une partie d'un espace vectoriel (E, ?, .). vect(A) est l'unique
sous-espace vectoriel de E vériant :
   (1) A ⊂ vect(A),
   (2) vect(A) est inclus dans tout sous-espaces vectoriels contenant A.
Le sous-espace vectoriel vect(A) se comprend comme étant le plus petit sous-espace
vectoriel contenant A, on l'appelle espace vectoriel engendré par A.
Corollaire 3.13. vect(A) est l'intersection de tous les sous-espaces vectoriels de E
contenant A.
Corollaire 3.14. A est un sous-espace vectoriel, si et seulement si, vect(A) = A.
Exemple 3.15.            (1) vect{ensemble vide} = {0E } car l'espace nul est le plus petit
            sous-espace vectoriel de E .
        (2) vect(E) = E car vect E est le plus petit sous-espace vectoriel contenant E .
        (3) Soit A = {u}. Montrons que vect{u} = {λu | λ ∈ K} = Ku.
            Puisque u ∈ A ⊂ vect(A) et puisque vect(A) est un sous-espace vectoriel on
            a λu ∈ vect(A), pour tout λ ∈ K.
            Ainsi Ku ⊂ vect{u}.
            Par double inclusion on obtient Ku = vect{u}.
        (4) Soit A = {u, v}. Par double inclusion, on montre comme ci-dessus que
            vect{u, v} = {λu + µv | λ, µ ∈ K} = Ku + Kv .

Proposition 3.16. Si A et B deux parties de E alors A ⊂ B =⇒ vect(B) ⊂
vect(A).

        Preuve:
Supposons que A ⊂ B. On a alors A ⊂ vect(B) or vect(B) est un sous-espace
vectoriel donc vect(A) ⊂ vect(B).                                      

Proposition 3.17. Si A et B sont deux parties de E alors vect(A ∪ B) = vect(A) +
vect(B).

Exemple 3.18. Pour F et G deux sous-espaces vectoriels de E . vect(F ∪G) = F +G.
Ainsi F + G apparait comme étant le plus petit sous-espace vectoriel contenant F et
G.


3.4          Famille de vecteurs

3.4.1 Sous-espace vectoriel engendré par une famille nie de
      vecteurs
        Soient E un K-espace vectoriel et F = (e )           une famille nie de vecteurs de
    .
                                                   i 1≤i≤n
E

Dénition 3.19. On appelle combinaison linéaire desPvecteurs de la famille F =
(e1 , . . . , en ) tout vecteurs x de E pouvant s'écrire x =     n
                                                                 i=1 λi ei   avec λ1 , . . . , λn des
scalaires de K bien choisis.
24
~~~

## Page 29

~~~text
                                                                              3.4 Famille de vecteurs




Dénition 3.20. On appelle espace vectoriel engendré par la famille F = (ei )1≤i≤n ,
le sous-espace vectoriel engendré par la partie {e1 , . . . , en }. On le note vect F, vect(ei )1≤i≤n
ou vect(e1 , . . . , en ).
Exemple 3.21. Le sous-espace vectoriel engendré par la famille vide est l'espace
nul {0E }.
Théorème 3.22. Si (e1 , . . . , en ) est une famille de vecteurs de E alors vect(e1 , . . . , en )
est l'ensemble des combinaisons linéaires des vecteurs e1 , . . . , en , c'est-à-dire :
                                                   Pn
                      vect(e1 , . . . , en ) = {    i=1 λi ei | λ1 , . . . , λn ∈ K}.


Exemple 3.23.         (1) Cas n = 1, vect(u) = {λu | λ ∈ K} = Ku.
     (2) Cas n = 2, vect(u, v) = {λu + µv | λ, µ ∈ K} = Ku + Kv .
     (3) Dans R3 , considérons u = (1, 1, 1), v = (0, −1, 2).
         vect(u, v) = {(λ, λ + µ, 2µ) | λ, µ ∈ K}.

Remarque 3.24. Il est ecace d'établir qu'une partie est un sous-espace vectoriel
en observant que celle-ci est engendré par une famille de vecteurs.
Exemple 3.25.         (1) Dans R3 , considérons P = {(a + b, a − b, 2b) | a, b ∈ R}.
         Puisque P = vect(u, v), avec u = (1, 1, 0) et v = (1, −1, 2), P est un sous-
         espace vectoriel de R3 .
     (2) Dans R3 , considérons P = {(x, y, z) | x + y − z = 0}.
         Puisque x + y − z = 0 ↔ z = x + y , on a P = vect((1, 0, 1), (0, 1, 1)). ainsi P
         est un sous-espace vectoriel de R3 .

3.4.2 Famille génératrice
Dénition 3.26. On dit qu'une famille F = (ei )1≤i≤n de vecteurs de E est généra-
trice de E , si tout vecteur x de E s'écrit comme combinaison linéaire des vecteurs
de la famille F , c'est-à-dire :
                                                                                  Pn
             ∀x ∈ E, ∃(λ1 , . . . , λn ) ∈ Kn | x = λ1 e1 + · · · + λn en =             i=1 λi ei .


Remarque 3.27. La famille F est génératrice de E , si et seulement si, vect(F) =
E.

Exemple 3.28.         (1) Dans E = Rn , on pose ei = (0, . . . , 1, 0 . . . , 0) ∈ Rn où 1 se
         situe en ième position. La famille B = (ei )1≤i≤n est génératrice de Rn . En
         eet, ∀x = (x1 , . . . , xn ) ∈ Rn , on peut écrire x = x1 e1 + · · · + xn en .
     (2) Dans E = R, la famille (1) est génératrice. En eet, x ∈ R, x = x.1.
     (3) Dans E = C vu comme R-espace vectoriel, la famille F = (1, i) est généra-
         trice. En eet, pour tout z ∈ C, on peut écrire z = a.1 + b.i, avec a = <(z)
         et b = Im(z).
Proposition 3.29. Si (e1 , . . . , en , en+1 ) est une famille génératrice et si en+1 ∈
vect(e1 , . . . , en ) alors la sous-famille (e1 , . . . , en ) est génératrice.
                                                                                                      25
~~~

## Page 30

~~~text
3 .     Espace vectoriel

3.4.3 Famille libre, famille liée
Dénition 3.30. Un vecteur u est dit colinéaire à un vecteur v de E s'il existe
α ∈ K tel que u = αv . Deux vecteurs u et v sont dits colinéaires si l'un des deux est
colinéaire à l'autre.
      Attension
u est colinéaire à v n'équivaut pas à v est colinéaire à v . En eet, le vecteur nul est
colinéaire à tout vecteurs mais tout veceturs n'est pas colinéaire au vecetur nul.
Dénition 3.31.           (1) On dit que la famille (e1 , . . . , en ) de vecteurs de E est libre
         si elle vérie ∀λ1 , . . . , λn ∈ K, λ1 e1 + · · · + λn e = 0 → λ1 = . . . λn = 0. On
         dit que les veceturs e1 , . . . , en sont linéairement indépendants.
     (2) On dit que la famille (e1 , . . . , en ) est liée si elle n'est pas libre ce qui signie
         ∃λ1 , λn ∈ K, λ1 e1 + . . . λn en = 0 et (λ1 , . . . , λn ) 6= (0, . . . , 0). Une égalité
         λ1 e1 + · · · + λn en = 0 avec λ1 , . . . , λn non tous nuls est appelée relation
         linéaire sur les vecteurs e1 , . . . , en .
Exemple 3.32. Soit u ∈ E , étudions la liberté de la famille (u). Si u 6= 0 alors
∀λ ∈ K, λu = 0 ⇒ λ = 0. Par suite, la famille (u) est libre.
Si u = 0 alors on peut écrire λu = 0 avec λ = 1 6= 0. Par suite, la famillle (0) est
liée.
Proposition 3.33. Soient n ≥ 2 et (e1 , . . . , en ) une famille de vecteurs de E . On a
une équivalence entre :
   (i) (e1 , . . . , en ) est liée ;
  (ii) L'un des vecteurs e1 , . . . , en est combinaison linéaire des autres.
Exemple 3.34.            (1) Soient u, u ∈ E .
         (u, v) est liée, si et seulement si, (∃α ∈ K∗ , u = αv) ou (∃β ∈ K∗ , v = βu).
         Ansi, la famille (u, v) est liée, si et seulement si, u et v sont colinéaires.
     (2) Dans E = R3 , considérons les vecteurs u = (1, 2, 1), v = (1, −1, 1), w =
         (1, 1, 0) et la famille F = (u, v, w). Etudions la liberté de la famille F . Soient
         α, β, γ ∈ R.                                
                                                 
                                                 
                                                   α+β+γ =0
                                                 
                              αu + βv + γw = 0 ⇔   2α − β + γ = 0
                                                 
                                                 
                                                 
                                                  α + β = 0.

         Aprés résolution du système, on obtient αu + βv + γw = 0 ⇔ α = β = γ = 0,
         la famille F est donc libre.
     (3) Dans E = R3 , considérons les vecteurs u = (1, −1, 0), v = (2, −1, 1), w =
         (0, 1, 1) et la famille F = (u, v, w). Etudions la liberté de la famille F .
         Soient α, β, γ ∈ R.
                                                         
                                                         
                                                         
                                                          α + 2β = 0
                                                         
                                αu + βv + γw = 0 ⇔         −α − β = 0
                                                         
                                                         
                                                         
                                                          β + γ = 0.

26
~~~

## Page 31

~~~text
                                                                        3.4 Famille de vecteurs


                                                                                    
                                                                                        α = −2β
        Aprés la résolution du système, on obtient αu + βv + γw = 0 ⇔
                                                                                        γ = −β.
       On en déduit que la famille F est liée car on a notament la relation linéaire
       −2u + v − w = 0.
   (4) Dans E = F(R, R), considérons les fonctions f : x 7→ 1, g : x 7→ cos(x), h :
       x 7→ sin(x) et montrons que la famille (f, g, h) est libre. Soient α, β, γ ∈ R
       Supposons αf + βg + γh = 0. Pour tout x ∈ R, on a : α + βcosx + γsinx = 0.
       Pour x = 0, on obtient l'équation α + β = 0(1). Pour x = Π/2, on obtient
       l'équation α + γ = 0(2). Pour x = Π, on obtient l'équation αβ = 0(3). On
       a : (1) et (3) donnent α = β = 0 et par (2) on obtient γ = 0. Finalement la
       famille (f, g, h) est libre.
Remarque 3.35.        (1) Toute sous-famille d'une famille libre est libre.
   (2) Toute sur-famille d'une famille liée, en particulier toute famille contenant le
       vecteur nul est liée.
   (3) Une sur-famille d'une famille libre n'est pas nécessairement libre.
Proposition 3.36. Si (e1 , . . . , en ) est une famille libre et si en+1 ∈/ vect(e1 , . . . , en )
alors la sur-famille (e1 , . . . , en , en+1 ) est libre.

3.4.4 Base d'un espace vectoriel
Dénition 3.37. On dit qu'une famille B = (ei )1≤i≤n = (e1 , . . . , en ) de vecteurs de
E est une base de E si celle-ci est libre et génératrice.
Exemple 3.38.           (1) Dans E = Kn , on pose ei = (1, . . . , 0, 1, 0, . . . , 0) ∈ Kn où
       1 se situe en ième position. On a déja vu que B = (e1 , . . . , en ) est génératrice
       de Kn ; montrons qu'elle est libre. Soient λ1 , . . . , λn ∈ K. Supposons que
       λ1 e1 + · · · + λn en = 0. On a (λ1 , . . . , λn ) = (0, . . . , 0) et donc λ1 = · · · = λn =
       0. Finalement , la famille B est libre et génératrice de Kn , c'est une base de
       Kn .
   (2) Considérons la famille (1, i) déléments du R-espace vectoriel C. On a déja vu
       que cette famille est génratrice ; montrons qu'elle est libre. Soient λ, µ ∈ R.
       Supposons que λ.1 + µ.i = 0. En identiant parties réelles et imaginaires, on
       obtient λ = µ = 0. Finalement, la base B est libre est génératrice du R-espace
       vectoriel C, c'est une base de C.
Remarque 3.39. La famille (1, i) est liée dans le C-espace vectoriel C. Elle n'est
pas donc une base du C-espace vectoriel C.
Théorème 3.40 (Théorème de la base extraite). De toute famille génératrice nie
de E , on peut extraire une base de E . En particulier, un espace de dimension nie
admet une base.
Théorème 3.41 (Théorème de la base incomplète). Si E est de dimension nie,
alors toute famille libre de E peut-être complétée en une base de E . Pour la complé-
ter, il sut de considérer certains vecteurs d'une famille génératrice de E .
   En particulier, on déduit des résultats précédents que tout espace vectoriel de
dimension nie admet une base nie.
                                                                                27
~~~

## Page 32

~~~text
3 .   Espace vectoriel

Théorème 3.42 (Théorème et dénition). Si E est de dimension nie, alors toutes
les bases de E ont le même nombre d'éléments. Ce nombre s'appelle la dimension
de E et est noté dim(E).
Corollaire 3.43. Si E est de dimension n et si (x1 . . . , xn ) est une famille de n
vecteurs de E , alors les conditions suivantes sont équivalentes :
    1. (x1 , . . . , xn ) est une famille libre de E ;
    2. (x1 , . . . , xn ) est une famille génératrice de E ;
    3. (x1 , . . . , xn ) est une base de E .
Remarque 3.44.            1. En particulier, dans un espace de dimension n, une famille
         libre a toujours au plus néléments, et une famille génératrice a toujours au
         moins n éléments.
      2. Si E et F sont de dimension nie, alors dim(E × F ) = dim(E) + dim(F ).
         En particulier, dim(Kn ) = n.
      3. Si E et F sont de dimension nie, alors dim(L(E, F )) = dim(E) × dim(F ).
      4. dim(Kn [X]) = n + 1.
Dénition 3.45. Soit (x1 , . . . , xn ) une famille nie de vecteurs d'un K-espace vec-
toriel E , on appelle rang de (x1 , . . . , xn ) la dimension de F = vect(x1 , . . . , xn ).
Lemme 3.46. Dans un espace engendré par n vecteurs (u1 , . . . , un ), toute famille
(v1 , . . . , vn+1 ) de n + 1 vecteurs est liée.

Lemme 3.47. Le cardinal d'une famille libre est plus petit que celui d'une famille
génératrice Si F1 est une famille libre et F2 une famille génératrice de E , on a

                                       card(F1 ) ⩽ card(F2 )

Remarque 3.48. Soit E est K-espace vectoriel.
      1. Si E = {0E }, on a dim E = 0.
      2. Si F est une famille libre de E , on a : card F ⩽ dim E
      3. Si F est une famille génératrice de E , on a : card F ⩾ dim E
Proposition 3.49. Si E est un espace vectoriel de dimension nie et si F est un
sous-espace vectoriel de E , alors F est de dimension nie et on a dim(F ) ⩽ dim(E).
De plus, on a dim(F ) = dim(E) ⇔ F = E .

3.4.5 Composante dans une base
Théorème 3.50. Si B = (ei )1≤i≤n est une base d'un K-espace vectoriel de E alors
∀x ∈ E, ∃!(λ1 , . . . , λn ) ∈ Kn , x = λ1 e1 + . . . λn en .

Dénition 3.51. Avec les notations ci-dessous, les scalaires λ1 , . . . , λn sont appelés
les composants de x dans la base B (ou encore les composantes de x).
Remarque 3.52. Les composantes d'un vecteur dépendant de la base dans laquelle
on travaille.
28
~~~

## Page 33

~~~text
                      3.5 Somme, Somme directe, sous-espaces vectoriels supplémentaires




Exemple 3.53.       (1) Dans E = Kn , considérons la base canonique B = (e1 , . . . , en )
      et le vecteur x = (x1 , . . . , xn ). Puisque x = x1 e1 + · · · + xn en , les composantes
      du vecteurs x dans la base B sont les saclaires x1 , . . . , xn .
  (2) Dans le R-espace vectoriel C, les composantes de z ∈ C dans la base cano-
      nique (1, i) sont <(z) et Im(z)
Théorème 3.54. Si B = (ei )1≤i≤n est une base de E alors pour tout vecteur x et
y de composantes x1 , . . . , xn et y1 , . . . , yn dans B , les composantes de x + y sont
x1 + y1 , . . . , xn + yn et celle de λx sont λx1 , . . . , λxn .


3.5      Somme, Somme directe, sous-espaces vectoriels

         supplémentaires

3.5.1 Introduction
    La réunion de deux sous-espaces n'est pas en général un sous-espace, sauf cas
très particulier. L'opération d'addition permet de dénir la somme de deux sous-
espaces; cette somme s'avère être en fait le plus petit sous-espace contenant leur
réunion. La propriété d'unicité de l'écriture d'un vecteur comme somme de vecteurs
appartenant à deux sous-espaces donnés conduit à la notion de somme directe et de
sous-espaces supplémentaires.
3.5.2 Somme de sous-espaces vectoriels
Dénition 3.55. Soit E un K-espace vectoriel et soient F et G deux sous-espaces
vectoriels de E : On appelle somme de F et de G l'ensemble, noté F + G ; des
vecteurs qui sont la somme d'un vecteur de F et d'un vecteur de G :
                              F + G = {u ∈ E | u = f + g, f ∈ F, g ∈ G}.
En d'autres termes, les vecteurs de la somme F + G sont caractérisés par
                      u ∈ F + G ⇐⇒ ∃f ∈ F, ∃g ∈ G tels que u = f + g.
Remarque 3.56. La somme F + G des sous-espaces vectoriels F et G est donc est
un ensemble. Cet ensemble contient F . En eet, si f ∈ F , alors f = f + 0E ∈ F + G
car 0E ∈ G : Ainsi F ⊂ F + G.
Théorème 3.57. La somme F + G de deux sous-espaces vectoriels F et G d'un
espace vectoriel E est un sous-espace vectoriel de E .
      Preuve:
F + G ⊂ E puisque tout élément h de F + G s'écrit h = f + g ; avec f dans F (donc
dans E) et g dans G (donc dans E), et que la somme de deux éléments de E est un
élément de E.
Le vecteur nul 0 est dans F + G : en eet 0 = 0 + 0 avec 0 ∈ F et 0 ∈ G ;
puisque F et G sont des sous-espaces vectoriels de E.
                      E                                E       E   E       E         E


Si u et v sont dans H et si λ et µ sont des scalaires, on peut écrire u = f + g
et v = f + g ; avec f et f dans F et g et g dans G. Alors λu + µv = (λf +
                                                                                      1       1


µf ) + (λg + µug ). Or F est un sous-espace vectoriel de E ; donc λf + µf ∈ F .
          2       2               1   2            1       2                              1


De même, λg + µg ∈ G. Ainsi λu + µv2 ∈ F + G.
  2           1           2                                                    1      2
                  1           2                                                
                                                                               29
~~~

## Page 34

~~~text
3 .   Espace vectoriel

Exemple 3.58. Soient u1 ; u2 ; u3 trois vecteurs de l'espace vectoriel E .
Que peut-on dire de la somme vect(u1 ; u2 ) + vect(u3 )? On a
u ∈ vect(u1 ; u2 ) + vect(u3 ) ⇐⇒ ∃f ∈ vect(u1 ; u2 ); ∃g ∈ vect(u3 ); tels que u = f + g.
Or, on sait que
     f ∈ vect(u1 ; u2 ) ⇐⇒ ∃(a1 ; a2 ) ∈ K2 tel que f = a1 u1 + a2 u2 et g ∈ vect(u3 )
                        ⇐⇒ ∃a3 ∈ K tel que g = a3 u3 .
On en déduit donc nalement que
u ∈ vect(u1 , u2 ) + vect(u3 ) ⇐⇒ ∃(a1 , a2 , a3 ) ∈ K3 tel que u = a1 u1 + a2 u2 + a3 u3
                               ⇐⇒ u ∈ vect(u1 , u2 , u3 )
Ceci prouve que vect(u1 , u2 ) + vect(u3 ) = vect(u1 , u2 , u3 ).

3.5.3 Somme directe des sous-espaces vectoriels
Dénition 3.59. Soient F et G deux sous-espaces vectoriels de E : On dit que la
somme F + G est directe si tout vecteur de F + G se décompose de manière unique
comme la somme d'un élément de F et d'un élément de G.
   Lorsque F et G sont en somme directe, on note F +G = F ⊕G. Pratiquement, les
sous-espaces vectoriels en somme directe sont caractérisés par le théorème suivant :
Théorème 3.60. Soit E un K-espace vectoriel et soient F et G deux sous-espaces
vectoriels de E . Alors :
                            F + G est directe ⇔ F ∩ G = {0E }
      Preuve:
Supposons la somme F + G directe. Soit u ∈ F ∩ G. On peut alors écrire u = 0 + u ;
avec 0 ∈ F et u ∈ G et on a aussi u = u + 0 avec u ∈ F et 0 ∈ G. Puisque
                                                                                         E


la somme F + G est directe, la décomposition de u suivant F et G est unique et
          E                                                  E                   E


ainsi u = 0 . Ceci prouve que le seul vecteur qu'on puisse trouver dans F ∩ G est le
vecteur nul, c'est-à-dire que F ∩ G ⊂ {0 }. Mais l'inclusion inverse est vraie puisque
                  E


F et G sont deux sous-espaces vectoriels de E . Donc F ∩ G = {0 }.
                                              E


Réciproquement, supposons que F ∩ G = {0 } et montrons que la somme F + G
                                                                             E


est directe. Supposons que l'on ait
                                                     E



                                     u = f 1 + g1 = f 2 + g2 ,
avec f et f dans F et g et g dans G. Alors f − f = g − g . Puisque f − f ∈ F
et g − g ∈ G, le vecteur v = f − f = g − g appartient à F ∩ G. Puisque
          1       2         1    2                       1       2   2   1           1   2


F ∩ G = {0 }, on a donc f − f = g − g = 0 , ce qui assure que f = f et
      2       1                          1     2         2       1


g = g , Ainsi, l'écriture de u comme somme d'un élément de F et d'un élément de
                      E         1       2      2     1           E                   1       2


G est unique, ce qui signife que la somme F + G est directe.
 1        2
                                                                             
Exemple 3.61. Deux droites sécantes en vecteur nul du plan R2 ou de l'espace R3
sont en somme directe puisque leur intersection est réduite au vecteur nul. Deux
plans sécants de l'espace R3 ne peuvent être en somme directe puisque leur intersec-
tion est une droite et ne contient donc pas que le vecteur nul.
30
~~~

## Page 35

~~~text
                3.5 Somme, Somme directe, sous-espaces vectoriels supplémentaires




3.5.4 Sous-espaces vectoriels supplémenatires dans un espace
      vectoriel
Dénition 3.62. Soit E un K-espace vectoriel et soient F et G deux sous-espaces
vectoriels de E . On dit que F et G sont supplémentaires dans E si la somme F + G
est directe et si celle-ci vaut E . On a donc :
                  (F et G supplémentaires dans E) ⇔ E = F ⊕ G.

On dit aussi que G est un supplémentaire de F dans E .
   La caractérisation des sous-espaces espaces vectoriels supplémentaires se traduit
par le théorème suivant :
Théorème 3.63. Soient F et G sont deux sous-espaces vectoriels de E . Les propo-
sitions suivantes sont équivalents :
   (1) F et G sont supplémentaires dans E .
   (2) Pour tout u ∈ E ; il existe un couple unique de vecteurs f ∈ F et g ∈ G et
       tels que u = f + g .
   (3) dim F + dim G = dim E et F ∩ G = {0E }.
   (4) Si BF est une base de F et Si BG est une base de G alors B = BF ∪ BG est
       une base de E .
Remarque 3.64. Attention de ne pas confondre la notion d'espaces en somme
directe avec la notion d'espaces supplémentaires dans un autre. Par exemple, deux
droites sécantes de R3 sont supplémentaires dans le plan qui les contient, mais pas
dans l'espace R3 : en eet, leur somme est directe et vaut exactement le plan P =
D1 ∪ D2 , et non l'espace tout entier
Remarque 3.65. Un sous-espace possède plusieurs supplémentaires. Par exemple,
si D1 ; D2 ; D3 sont trois droites deux à deux sécantes en {(0, 0)} de E = R2 , alors D2
et D3 sont des supplémentaires de D1 dans R2 puique dim D1 +dim D2 = dim R2 = 2
et dim D1 + dim D3 = dim R2 et D1 ∩ D2 = D1 ∩ D3 = {(0, 0)}.
Exemple 3.66. Soit E = R3 . On demande de vérifer que F = {(x; y; z) ∈ R3 |
x − y + z = 0} et G = {(x; x; x) ∈ R3 } sont supplémentaires dans E .
On montre d'abord que F = vect((1, 1, 0), (0, 1, 1)). F est donc un plan vectoriel de
R3 et aussi un sous-espace vectoriel de R3 . De même G = vect((1, 1, 1)) est une
droite vectorielle de R3 est donc un sous-espace vectoreil de R3 .
Une méthode pour montrer que F et G sont supplémentaires dans R3 ; est de vérier
que tout vecteur u = (x1 ; x2 ; x3 ) de R3 se décompose de manière unique comme
somme d'un vecteur f = (f1 ; f2 ; f3 ) de F et d'un vecteur g = (g1 ; g2 ; g3 ) de G.
Nous devons donc résoudre l'équation u = f + g , d'inconnues f et g et montrer
qu'elle admet une solution unique.
Or, f ∈ F ⇐⇒ f2 = f1 + f3 ⇐⇒ f = (f1 ; f1 + f3 ; f3 ).
De même g ∈ G ⇐⇒ g = (g1 ; g1 ; g1 ). On a donc :
                                       
                  f1 + g1 = x1          f1 + g1 = x1
    x = f + g ⇐⇒   f1 + g1 + f3 = x2 ⇐⇒   f 3 = x2 − x1
                   f3 + g1 = x3           g 1 = x3 − f 3 = x1 − x2 + x3
                                       

                                                                                     31
~~~

## Page 36

~~~text
3 .   Espace vectoriel

On voit donc que ce système admet une unique solution donnée par :
                             
                              f 1 = x1 − g 1 = x2 − x 3
                               f 3 = x2 − x1
                               g 1 = x 1 − x2 + x3
                             

Ceci signie donc que les vecteurs f et g recherchés existent et qu'ils sont uniques.
On a bien prouvé que R3 = F ⊕ G.
Exemple 3.67. Soit E = F(R, R) : Vérier que F = {f : R → R | f est paire
et G = {f : R → R | f estimpaire} sont supplémentaires dans E . On a déjà vu
que F est un sous-espace vectoriel de E . On prouve de même que G est un sous-
espace vectoriel de E . Il nous reste à vérier que tout élément de E se décompose de
manière unique comme la somme d'un élément de F et d'un élément de G ; ce qui
revient à prouver que toute fonction f de R dans R peut s'écrire d'une seule façon
comme la somme d'une fonction paire et d'une fonction impaire. Contrairement
à l'exemple précédent, ceci ne débouche pas sur un système d'équations à résoudre.
Nous allons ici procéder à l'aide d'un raisonnement par analyse et synthèse. Analyse
du problème : Supposons que l'on puisse écrire f = p + i avec p paire et i impaire,
et essayons d'exprimer p et i en fonction de f . Pour tout x ∈ R, on a d'abord
f (x) = p(x) + i(x). Puisque p(−x) = p(x) et i(−x) = −i(x) ; on a aussi, pour tout
réel x, on a f (−x) = p(−x) + i(−x) = p(x) − i(x). En ajoutant et soustrayant
membre à membre f (x) et f (−x) ; il vient
                     1                                1
               p(x) = (f (x) + f (−x))          i(x) = (f (x) − f (−x))
                     2                                2
Cette analyse du problème nous permet donc de conclure que, si la décomposition de
f en somme d'une fonction paire et d'une fonction impaire est possible, alors celle-ci
est unique puisqu'on a trouvé une seule valeur posible de p(x) et de i(x) : Il nous
reste simplement à vérier que les fonctions données répondent bien aux exigences
du problème posé, c'est-à-dire que p est paire, que i est impaire et que p + i = f :
Synthèse du problème : Partant de f fonction quelconque de R dans R ; soient p et
i dénies par :
                     1                                1
               p(x) = (f (x) + f (−x))          i(x) = (f (x) − f (−x))
                     2                                2
On a bien p(x) + i(x) = f (x) ; c'est-à-dire f = p + i. De plus, on a p(−x) =
1
2
  (f (−x) + f (x)) = p(x) ; donc p est paire. On vérie de même que i est impaire.
Ainsi, F et G sont supplémentaires dans E .
Proposition 3.68. Tout sous-espace d'un espace de dimension nie admet un sup-
plémentaire.
Théorème 3.69 (Formule de Grassmann). Soit E un espace vectoriel de dimension
nie et soient F ,G deux sous-espaces vectoriels de E . Alors
                    dim(F + G) = dim(F ) + dim(G) − dim(F ∩ G).

En particulier, F et G sont en somme directe si et seulement si dim(F + G) =
dim(F ) + dim(G).

32
~~~
