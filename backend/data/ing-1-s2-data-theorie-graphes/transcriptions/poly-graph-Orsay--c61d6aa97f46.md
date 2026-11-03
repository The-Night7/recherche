# poly-graph-Orsay.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1pCygvLJvvfEaUpix-sVdggkq40lVKiPZ) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Introduction à la théorie des graphes


                                                 Eric Sigward
                                     e.sigward@ac-nancy-metz.fr




           Les sept ponts de Königsberg
~~~

## Page 2

~~~text
      Introduction                                                                                                                                   2
      Définitions et premiers exemples                                                                                                               2
         Graphes non orientés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
         Graphes orientés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
      Terminologie                                                                                                                                   7
      Éléments de la théorie des graphes                                                                                                             9
         Graphes eulériens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
         Graphes hamiltoniens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
         Matrice d’adjacence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
         Distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
         Coloriage des sommets d’un graphe . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
         Graphes valués et problème du plus court chemin . . . . . . . . . . . . . . . . . . . . . . . . . . 20
         Graphes probabilistes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
                     Chaîne de Markov . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
                     Graphes probabilistes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
      Les graphes en Terminale ES                                                                                                                   34
      Exercices                                                                                                                                     35

      Solutions des exercices                                                                                                                      38
      Complément : les arbres                                                                                                                      43
        Définition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
        Arbre de recouvrement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
        Arbre partiel de coût minimum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44




Eric Sigward         Introduction à la théorie des graphes                             Mars 2002




                                                                                                                                                   1
~~~

## Page 3

~~~text
A    Introduction
    L’histoire de la théorie des graphes débute peut-être avec les travaux d’Euler au
    XVIIIe siècle et trouve son origine dans l’étude de certains problèmes, tels que celui
    des ponts de Königsberg (voir page de couverture, les habitants de Königsberg se
    demandaient s’il était possible, en partant d’un quartier quelconque de la ville, de
    traverser tous les ponts sans passer deux fois par le même et de revenir à leur point
    de départ), la marche du cavalier sur l’échiquier ou le problème de coloriage de
    cartes.
       La théorie des graphes s’est alors développée dans diverses disciplines telles
    que la chimie, la biologie, les sciences sociales. Depuis le début du XXe siècle,
    elle constitue une branche à part entière des mathématiques, grâce aux travaux de
    König, Menger, Cayley puis de Berge et d’Erdös.
       De manière générale, un graphe permet de représenter la structure, les connex-
    ions d’un ensemble complexe en exprimant les relations entre ses éléments : réseau
    de communication, réseaux routiers, interaction de diverses espèces animales, cir-
    cuits électriques,. . .
       Les graphes constituent donc une méthode de pensée qui permet de modéliser
    une grande variété de problèmes en se ramenant à l’étude de sommets et d’arcs.
    Les derniers travaux en théorie des graphes sont souvent effectués par des infor-
    maticiens, du fait de l’importance qu’y revêt l’aspect algorithmique.



B    Définitions et premiers exemples

    B.1     Graphes non orientés

    1. Définition
       Un graphe simple G est un couple formé de deux ensembles : un ensemble
       X = fx1 ; x2; : : : ; xn g dont les éléments sont appelés sommets, et un ensemble
       A = fa1; a2 ; : : : ; am g, partie de l’ensemble P 2(X ) des parties à deux éléments
       de X , dont les éléments sont appelé s arêtes. On notera G = (X; A).
       Lorsque a = fx; y g 2 A, on dit que a est l’arête de G d’extrémités x et y , ou que
       a joint x et y , ou que a passe par x et y . Les sommets x et y sont dits adjacents
       dans G.




                                                                                         2
~~~

## Page 4

~~~text
2. Définition
   Un multigraphe G = (X; A; f ) est déterminé par :
  – un ensemble X de sommets
  – un ensemble A; cette fois abstrait
  – une application f : A !P 2 (X )




     Dans cet exemple, x, y , z , t sont les sommets du multigraphe et : f (a1 ) =
     f (a2 ) = f (a3) = fx; tg ; f (a4 ) = fx; y g ; f (a5 ) = fx; z g ; f (a6 ) = fz; tg ;
     Un multigraphe avec boucles est un triplet (X; A; f ) où f est une application
     de A dans P 2(X )[P 1 (X ); en d’autres termes, un multigraphe avec boucles
     peut comprendre des arêtes multiples entre deux sommets donnés ainsi que
     des boucles multiples en un sommet.
3. Exemples :
   a. Le graphe d’un tournoi, T = (X; A) où :
      X est l’ensemble des participants au tournoi
      A est l’ensemble des paires de joueurs se rencontrant dans le tournoi.
  b. La carte routière de la France, F = (X; A) où
     X est l’ensemble des villes de la France.
     A = ffx; y g= il y a au moins une route directe reliant les villes x et y g:
   c. Le graphe discret d’ordre n, Dn = (X; ;):
  d. Le graphe complet d’ordre n, Kn ; où X = f1; 2; : : : ; ng et A = P 2(X )




               K1       K2           K3            K4             K5

   e. Le graphe biparti-complet Kp;q où X = fx1 ; x2; : : : ; xp ; y1; y2; : : : ; yq g et
      A = ffxi ; yj g=1 6 i 6 p et 1 6 j 6 q g




                                                                                         3
~~~

## Page 5

~~~text
                                              K4 2
                                                 ;




   f. Le cycle Cn , où X = f1; 2; : : : ; ng et A = ff1; 2g; f2; 3g; : : : ; fn   1; ng; fn; 1gg




                                               C4

4. Définition
   Soit G = (X; A) un graphe simple, et x un sommet de ce graphe. Le degré
   de x, noté d(x), est le nombre d’arêtes incidentes à x; c’est–à-dire contenant x.
   Lorsque d(x) = 0, on dit que le sommet x est isolé, lorsque x = 1, il est dit
   pendant.
   Exemples :
        si x est un sommet de Cn , d(x) = 2
        si x est un sommet de Kn , d(x) = n           1

5. Définition
   Un graphe simple est dit régulier de degré r, lorsque tous ses sommets sont de
   degré r.
6. Lemme des poignées de mains
   Soit G = (X; A) un graphe simple, alors
                                    X
                                             d(x) = 2 jAj
                                    x2   X

   En effet, chaque paire fx; y g de A est comptée deux fois, une fois pour d(x) et
   une seconde fois pour d(y ):
   Remarque
   Le lemme des poignées de mains reste valable pour les multigraphes avec boucles
   en convenant qu’une boucle contribue pour 2 dans le calcul du degré d’un som-
   met.
7. Exercices
   a. Montrer qu’un graphe simple a un nombre pair de sommets de degré impair.
      Notons P l’ensemble des sommets de degré pair et I l’ensemble des sommets
      de degré impair d’un graphe simple G = (X; A): P et I forment une partition




                                                                                          4
~~~

## Page 6

~~~text
      de X; d’après le lemme des poignées de mains, on a :
                      X                        X                X
                              d(x) = 2 jAj =           d(x) +           d(x)
                 X
                      x 2 X                    x   2
                                                   P            2
                                                                x   I
                                                                               X
      Or 2 jAj et        d(x) sont des entiers pairs, on en déduit alors que x2I d(x)
                     x2P
      est également pair, comme différence de deux entiers pairs. Chaque terme de
      cette dernière somme est impair, elle ne peut donc être paire que si et seule-
      ment si le nombre de termes est pair, on a donc montré que jI j est un entier
      pair.

   b. Est-il possible de relier 15 ordinateurs de sorte que chaque appareil soit relié
      avec exactement trois autres ?
      Considérons le graphe simple dont les sommets sont les 15 ordinateurs, les
      arêtes étant les liaisons entre ces ordinateurs. Si chaque appareil est relié à
      exactement 3 ordinateurs du réseau, les sommets du graphe sont tous de degré
      impair. D’après le résultat établi dans l’exercice précédent, un tel graphe doit
      posséder un nombre pair de sommets, le réseau est donc impossible.

   c. Montrer que le nombre total de gens qui ont habité la Terre et qui ont donné
      un nombre impair de poignées de mains est pair.
      Considérons le graphe dont les sommets sont les gens qui ont habité la Terre et
      dont les arêtes représentent les poignées de mains échangées entre ces person-
      nes. La réponse à la question découle immédiatement du résultat du premier
      exercice.



B.2     Graphes orientés

1. Définition
   Un graphe orienté G est formé de deux ensembles : un ensemble X = fx 1; x2; : : : ; xn g
   dont les éléments sont appelés sommets, et un ensemble A = fa1; a2 ; : : : ; am g,
   partie du produit cartésien X  X , dont les éléments sont appelés arcs. On notera
   G = (X; A).




   Si a = (x; y ) est un arc du graphe G, x est l’extrémité initiale de a et y l’extrémité
   finale de a.



                                                                                        5
~~~

## Page 7

~~~text
    Remarque
  À tout graphe orienté G = (X; A); on associe le graphe simple (X; B ) où :
  fx; yg 2 B , ((x; y) 2 A ou (y; x) 2 A))
2. Définition
   Soit x un sommet d’un graphe orienté. On note d + (x) le nombre d’arcs ayant x
   comme extrémité initiale, et d (x) le nombre d’arcs ayant x comme extrémité
   finale. Ainsi, on a :
                                 d(x) = d+ (x) + d (x)
3. Exercice
  G = (X; A) est un graphe X
                           orienté, montrer que :
                                        X
                               d+ (x) =      d (x)
                                 x2  X              x   2
                                                        X


  En effet, on a clairement :
                         X                  X
                                 d+ (x) =           d (x) = jAj :
                         x2  X              2
                                            x   X




                                                                               6
~~~

## Page 8

~~~text
C    Terminologie

     Sous-graphe : H = (Y; B ) est un sous-graphe de G = (X; A) si Y  X et
      B  A:
     Graphe partiel :H = (Y; B ) est un graphe partiel de G = (X; A) si Y = X et
      B  A:
     Ordre d’un graphe : l’ordre d’un graphe est le nombre de sommets de ce graphe.
     Chaîne : suite finie de sommets reliés entre eux par une arête.
     Chaîne simple : chaîne qui n’utilise pas deux fois la même arête.
     Chaîne eulérienne : chaîne simple passant par toutes les arêtes d’un graphe.
     Chaîne hamiltonienne : chaîne simple passant par tous les sommets d’un graphe
      une et une seule fois.
     Chemin : suite de sommets reliés par des arcs dans un graphe orienté.
     Cycle : chaîne qui revient à son point de départ.
     Cycle eulérien : cycle simple passant par toutes les arêtes d’un graphe une et
      une seule fois.
     Cycle hamiltonien : cycle simple passant par tous les sommets d’un graphe une
      et une seule fois.
     Graphe connexe : un graphe G est dit connexe si pour toute paire de sommets
      fx; yg de G, il existe une chaîne de premier terme x et de dernier terme y.
     Arbre : graphe connexe sans cycle simple et sans boucle.
     Graphe eulérien : graphe qui possède un cycle eulérien.
     Graphe semi-eulérien : graphe qui possède une chaîne eulérienne.
     Graphe hamitonien : graphe qui possède un cycle hamiltonien.
     Graphe semi-hamiltonien : graphe qui possède une chaîne hamiltonienne.
     Graphe valué : graphe où des réels sont associés aux arêtes. Dans cet exposé,
      on ne considérera que des valuations positives.
     Longueur d’une chaîne : nombre des arêtes qui composent la chaîne.
     Valeur d’une chaîne : somme des valeurs des arêtes (arcs) d’une chaîne d’un
      graphe valué.
     Distance entre deux sommets : longueur de la plus courte chaîne joignant ces
      deux sommets.
     Diamètre d’un graphe : maximum des distances entre les sommets d’un graphe.
     Indice chromatique : nombre minimal de couleurs permettant de colorier les
                                                                                  7
~~~

## Page 9

~~~text
  arêtes d’un graphe, de telle sorte que deux arêtes adjacentes n’aient pas la même
  couleur.
 Nombre chromatique d’un graphe : nombre minimal de couleurs permettant
  de colorier les sommets d’un graphe, de telle sorte que deux sommets adjacents
  n’aient pas la même couleur.




                                                                                 8
~~~

## Page 10

~~~text
D    Éléments de la théorie des graphes

    D.1     Graphes eulériens

    1. Théorème d’Euler (1766)
       Un graphe simple connexe G = (X; A) est eulérien si et seulement si pour tout
       sommet x de X , d(x) est pair.
       Démonstration
       Supposons G eulérien, soit alors c un cycle eulérien et x un sommet de G. Le
       cycle c contient toutes les arêtes de G, donc toutes les d(x) arêtes ayant x comme
       extrémité. Lors d’un parcourt de c on arrive en x autant de fois qu’on en repart,
       chaque arête de G étant présente une et seule fois dans c, d(x) est nécessairement
       un nombre pair.
       Réciproquement, supposons que tous les sommets de G soient de degré pair.
       Formons une chaîne simple c1 , aussi longue que possible, à partir d’un sommet
       arbitraire x0. Cette chaîne c1 est en fait un cycle, sinon, son extrémité finale
       serait de degré impair. Si ce cycle c1 contient toutes les arêtes du graphe G, c1
       est le cycle eulérien cherché. Dans le cas contraire, on considère le sous-graphe
       H obtenu à partir de G en éliminant les arêtes de c1 et ses sommets qui ne sont
       incidents à aucune des arêtes restantes. Comme G est connexe, H possède au
       moins un sommet commun avec le cycle c1 . Soit x1 un tel sommet. Les sommets
       de H sont encore de degré pair. Construisons alors, de la même manière que
       précédemment, un cycle c2 dans H à partir de x1. Rallongeons le cycle c1 en
       insérant à partir du sommet x 1 le cycle c2 pour former un cycle c 01 de x0 à x0 .
       Si ce cycle c01 possède toutes les arêtes de G, c01 est le cycle eulérien cherché.
       Sinon, on continue ce processus, qui se terminera car les sommets du graphe G
       sont en nombre fini.
          Remarques
       – Le théorème d’Euler reste valable pour des multigraphes connexes.
       – La démonstration fournit un algorithme de construction de cycle eulérien

          Exemples
          i.




                                G1                   G2
            G1 n’est pas eulérien, ses sommets ne sont pas tous pairs.

                                                                                       9
~~~

## Page 11

~~~text
   G2 est eulérien, un cycle eulérien est par exemple : a; b; c; d; c; e; d; b; e; a; e; a
ii. Le problème des ponts de Königsberg
    La ville de Königsberg en Prusse (maintenant Kaliningrad) comprenait 4
    quartiers, séparés par les bras du Prégel. Les habitants de Königsberg se
    demandaient s’il était possible, en partant d’un quartier quelconque de la
    ville, de traverser tous les ponts sans passer deux fois par le même et de
    revenir à leur point de départ.
    Le plan de la ville peut se modéliser à l’aide du multigraphe ci-dessous, les
    quartiers sont représentés par les 4 sommets, les 7 ponts par des arêtes :




   La question posée devient alors : ce graphe est-il eulérien ? Le théorème
   d’Euler répond immédiatement de façon négative aux habitants de Königs-
   berg.
iii. Est-il possible de tracer une courbe continue coupant chacun des 16 seg-
     ments de la figure ci-dessous exactement une et une seule fois ?




   Considérons le multigraphe dont les sommets sont les 6 régions de la fig-
   ure, a; b; c; d; e; f; et dont les arêtes sont les 16 segments qui sont frontières
   entre les différentes régions.




                                                                                    10
~~~

## Page 12

~~~text
        Le problème consiste à construire un cycle eulérien, ce qui est impossible,
        car le sommet e; par exemple, est de degré 5.

2. Théorème
   Un graphe simple connexe est semi-eulérien si et seulement si il admet 0 ou ex-
   actement 2 sommets de degré impair.
   La démonstration est identique à celle du théorème d’Euler. Si le nombre de
   sommets de degré impair est nul, la chaîne sera un cycle et le graphe sera en
   fait eulérien, et s’il est égal à deux, les chaînes eulériennes du graphe auront ces
   deux sommets pour extrémités.




D.2     Graphes hamiltoniens
Contrairement aux graphes eulériens, il n’existe pas de caractérisation simple des
graphes hamiltoniens ou semi-hamiltoniens. On peut cependant énoncer quelques
propriétés et conditions suffisantes.
1. Un graphe possédant un sommet de degré 1 ne peut être hamiltonien.
2. Si un sommet dans un graphe est de degré 2, alors les deux arêtes incidentes à
   ce sommet doivent faire partie du cycle hamiltonien.
3. Les graphes Kn sont hamiltoniens.
4. Théorème (Ore)
   Soit G = (X; A) un graphe simple d’ordre n > 3: Si pour toute paire fx; y g de
   sommets non adjacents, on a d(x) + d(y ) > n; alors G est hamiltonien.
5. Corollaire (Dirac)
   Soit G = (X; A) un graphe simple d’ordre n > 3: Si pour tout sommet x de G;
                 n
   on a d(x) > ; alors G est hamiltonien.
                 2
   En effet, un tel graphe vérifie les conditions du théorème précédent, si x et y ne
   sont pas adjacents, on a bien :
                                              n       n
                             d(x) + d(y ) >       +       =   n
                                              2       2
6. Exemples




                               G1                             G2

   G1 n’est pas hamiltonien, car il possède un sommet de degré 1.

                                                                                    11
~~~

## Page 13

~~~text
   G2 est hamiltonien : a; b; c; d; e; a est un cycle hamiltonien. (La condition du
                                                                             5
   corollaire de Dirac n’est pas nécessaire : G2 est d’ordre 5, et d(a) = 2 < )
                                                                                                 2



D.3     Matrice d’adjacence

1. Définition
   Soit G = (X; A) un graphe orienté, avec X = fx1; x2 : : : ; xn g: La matrice
   d’adjacence du graphe G est la matrice M (G) 2Mn (R ) dont les coefficients
   mi;j sont définis par :       
                                     si (xi ; xj ) 2 A
                           mi;j = 01 si (xi; xj ) 2=A
   exemple :



                                                                     0                       1
                                                                         0   0   0   0   1
                                                                   B 1 0 1 0 0 C
                                                                   B           C
                                                           M (G) = B           C
                                                                   B 0 0 0 0 0 C
                                                                   @ 0 1 0 1 0 A
                                                                         1   0   1   0   0
                            G
2. Propriétés
   Avec les notations précédentes, nous avons les propriétés immédiates suivantes :
   a. Pour tout i 2 f1; 2; : : : ; ng;
                                          X
                                          n


                      d+ (x ) = i                m   i;j

                                          j =1


                                          X
                                          n


                      d (x ) =  i                m   j;i

                                          j =1


                     X                    X
                                          n
                                                               X
                            m   i;j   =          d+ (x ) = i         d (x ) = jAj
                                                                         i

                      i;j                 i=1                  i=1


   b. La trace de M (G) est égale au nombre de boucles du graphe G

      Remarque La représentation matricielle est également utilisable pour des
      graphes non orientés, leurs matrices sont symétriques.
3. Théorème
   Soit G = (X; A) un graphe orienté, avec X = fx1; x2 : : : ; xn g; de matrice
   d’adjacence M = (mi;j ): Pour tout entier naturel k; non nul notons M k =
   (mi;j ): Alors mi;j est égal au nombre de chemins de longueur k du sommet x i
      (k )         (k )




                                                                                                     12
~~~

## Page 14

~~~text
au sommet xj :
Démonstration
Effectuons une récurrence sur k : mi;j = mi;j désigne bien le nombre de
                                        (1)

chemins allant de xi à xj : Supposons le résultat vrai pour l’entier k 1; comme
M k = M k 1  M; on a :
                                          X
                                          n


                            m (k )
                              i;j
                                     =             m(   k
                                                       i;l
                                                                 1)
                                                                      :m  l;j

                                          l=1


Par hypothèse de récurrence, mi;l est le nombre de chemins de longueur k 1
                                     (k   1)

allant de xi à xl et ml;j est égal à 1 si (xl ; xj ) est une arête de G et à 0 sinon.
m(i;lk 1) :ml;j est donc le nombre de chemins de longueur k allant de xi à xj dont
la dernière arête est (xl ; xj ); la somme de ces termes est donc bien le nombre de
chemins de longueur k allant de xi à xj :

     Exemples
 Déterminons le nombre de chemins de longueur 4 allant de a à b dans le graphe
G1




                                               G1
La matrice d’adjacence de G1 est :
                                      0                                   1
                                              0    0         1        1
                                      B
                                 0 0 1 1 C                                C
                            M =B
                               @ 1 1 0 0 A
                                              1    1         0        0
Le nombre de chemins cherché est le terme (1; 2) de la matrice
                                          0                                1
                                               8   8         0        0
                                          B
                                  8 8 0 0 C                                C
                           M4 = B
                                @ 0 0 8 8 A
                                               0   0         8        8
c’est-à-dire 8.
 Déterminons le nombre de circuits de longueur 4 dans le graphe G 2 :




                                                                                  13
~~~

## Page 15

~~~text
                                              G2
   La matrice d’adjacence de G2 est :
                                          0                1
                                              0    1   1
                                    M =@ 1 0 1 A
                                              0    1   1


   Le nombre de circuits de longueur 4 dans G2 est égale à la trace de M 4 :
                                          0                1
                                              3    5   8
                                   M4 = @ 2 6 8 A
                                              3    5   8
   et tr(M ) = 17:
            4



4. Exercice
   Soit G un graphe simple orienté d’ordre n; de matrice d’adjacence M: Mon-
   trer que si M n n’est pas nulle, alors le graphe G contient des cycles. Étudier la
   réciproque.

   Si M n n’est pas la matrice nulle, il existe (i; j ) 2 f1; 2; : : : ; ng2 ; tel que mi;j 6=
                                                                                        (n)


   0: Il existe donc au moins un chemin de longueur n de x i à xj : Or un chemin
   de longueur n dans un graphe d’ordre n passe au moins deux fois par le même
   sommet, c’est qu’il existe un cycle dans G:
   Réciproquement; si G contient un cycle, alors on peut trouver un chemin de
   longueur arbitraire dans le graphe, en particulier un chemin de longueur n: On
   en déduit que M n 6= 0:


D.4     Distance

1. Définition
   Soit G = (X; A) un graphe orienté. Pour tout (x; y ) 2 X 2 ; la distance entre le
   sommet x et le sommet y est le nombre d(x; y ) défini par :
                             
                d(x; y ) =       1 s’il n’existe pas de chemin de x à y
                                 minfl(c) j c est un chemin de x à y g

   l(c) désigne la longueur du chemein c: La matrice des distances du graphe G est
   la matrice D = (di;j ) = (d(xi ; xj )):



                                                                                              14
~~~

## Page 16

~~~text
  exemple




                                           G
  La matrice des distances de G est :
                                     0                 1
                                           0   1   1
                               D=@ 1           0   1 A
                                           1 1 0
2. Algorithme de Moore
   Soit x et y deux sommets d’un graphe G = (X; A): L’algorithme suivant calcule
   la distance d(x; y ) :
   On étiquette les sommets de G en observant les règles suivantes :
  – le sommet x reçoit l’étiquette 0
  – si (u; v ) 2 A et u est étiqueté k :
     i. si v n’est pas étiqueté, alors v reçoit l’étiquette k + 1
     ii. si v est étiqueté l; alors l’étiquette de v est remplacée par min(l; k + 1)
       Si, à la fin, y à une étiquette k; alors d(x; y ) = k; sinon d(x; y ) = 1:
     Exemple




     On a dans cet exemple: d(x; y ) = 3
     Remarque : lorsque d(x; y ) = k; l’algorithme précédent permet d’exhiber
     de façon récursive les chemins de longueur k de x à y : on part de y et on
     détermine les sommets z tels que (z; y ) 2 A avec d(x; z ) = k 1 et ainsi de
     suite jusqu’en x:




                                                                                       15
~~~

## Page 17

~~~text
D.5     Coloriage des sommets d’un graphe

1. Définitions
   Soit G = (X; A) un graphe non orienté. Un sous-ensemble S de X est stable
   s’il ne comprend que des sommets non adjacents deux à deux. Le cardinal de la
   plus grande partie stable est le nombre de stabilité de G; on le note (G):
   La coloration des sommets d’un graphe consiste à affecter tous les sommets de
   ce graphe d’une couleur de telle sorte que deux sommets adjacents ne portent
   pas la même couleur. Une coloration avec k couleurs est donc une partition de
   l’ensemble des sommets en k parties stables. Le nombre chromatique, noté
     (G); du graphe G est le plus petit entier k pour lequel il existe une partition de
   X en k sous-ensembles stables.
2. Encadrement du nombre chromatique


   a. Proposition
      Soit G = (X; A) un graphe simple d’ordre n: On a l’encadrement suivant :
                                                
                                         n
                                         (G)
                                                     6 (G) 6 r + 1
      où r est le degré maximal des sommets du graphe G:
      Démonstration
      Notons fS1; S2 ; : : : ; Sk g une partition de X en k parties stables avec k =
       (G): Alors :
                      X
                      k
                                         X
                                         k


                 n=            jS j 6
                                 i                   (G) = k: (G) = (G): (G)
                         i=1             i=1

      n; (G) et (G) étant des entiers naturels, l’inégalité de gauche est établie.
      Construisons une partition de X en sous-ensembles stables de la manière
      suivante :
       on considère un sommet x arbitraire de X; et S est une plus grande partie
                                             1                       1
        stable de X contenant x1
       s’il existe un sommet x de X qui n’est pas dans S , on construit S ; une
                                         2                               1       2
        plus grande partie stable de X contenant x2 disjointe de S1
       s’il existe un sommet x de X qui n’est pas dans S [ S ; on construit S ;
                                         3                               1   2       3
        plus grande partie stable de X contenant x3 telle que S1 ; S2 et S3 soient
        deux à deux disjointes.
       X étant un ensemble fini, ce procédé se terminera et nous obtenons une
        partition fS ; S ; : : : ; S g de X: En choisissant une couleur par élément de
                     1     2
        la partition, nous aurons nécessairement : (G) 6 k:
                                         k




        Considérons à présent un sommet x de la partie Sk : Le caractère maximal
        des parties construites assure que ce sommet x est adjacent à au moins un
        sommet de chaque partie Si ; i 2 f1; 2; : : : ; k 1g: On en déduit alors que


                                                                                     16
~~~

## Page 18

~~~text
          d(x) > k        ;
                        1 d’où :
                              r > d(x) > k        1   > (G)     1
          ce qui établit la deuxième inégalité.
  b. Proposition
     Soit G = (X; A) un graphe simple d’ordre n; alors :
                                       (G) + (G) 6 n + 1
    Démonstration
    Considérons S; une partie stable de X de cardinal (G): Une coloration pos-
    sible des sommets consiste à colorier les sommets de S d’une même couleur
    et les n    (G) autres sommets de couleurs toutes différentes. On en déduit
    que :
                                   (   G) 6 1 + (n      ( G))
3. Exemples

     i.    C2 ) = 2
            (     n


      ii. (C2 +1 ) = 3; pour n > 1:
                  n


    iii. (D ) = 1n


     iv. (K ) = nn


     v. Déterminons le nombre chromatique du graphe G suivant :




          Considérons la partition de l’ensemble des sommets de G en sous-ensembles
          stables :

                                           S1 = fa; dg
                                           S2 = fb; eg
                                           S3 = fc; f g
          on a donc      (G) 6 3: D’autre part, G contient un cycle d’ordre 3, donc
            (   G) > 3: Finalement, le nombre chromatique de G est donc 3. La parti-
          tion précédente en donne une 3_coloration :




                                                                                 17
~~~

## Page 19

~~~text
4. Exemples d’application
  a. Problème d’emploi du temps
     Une université doit organiser les horaires des examens. On suppose qu’il y a
     7 épreuves à planifier, correspondant aux cours numérotés de 1 à 7 et que les
     paires de cours suivantes ont des étudiants communs : 1 et 2, 1 et 3, 1 et 4, 1
     et 7, 2 et 3, 2 et 4, 2 et 5, 2 et 7, 3 et 4, 3 et 6, 3 et 7, 4 et 5, 4 et 6, 5 et 6, 5 et
     7 et 6 et 7. Comment organiser ces épreuves de façon qu’aucun étudiant n’ait
     à passer deux épreuves en même temps et cela sur une durée miminale ?
     Solution :
     Construisons le graphe G dont les sommets sont les épreuves numérotées de 1
     à 7, une arête relie deux de ses sommets lorsque les deux cours correspondant
     possèdent des étudiants communs :




        Planifier les examens en un temps minimal consiste à déterminer une k _
     coloration de G; avec k = (G):
     G possède un sous-graphe complet d’ordre 4 (de sommets 1,2,3,4), donc
       (G) > 4: Déterminons une partition des sommets de G en sous-ensembles
     stables :
                              S1 = f1; 6g
                              S2 = f2g
                              S3 = f3; 5g
                              S4 = f4; 7g
     d’où (G) 6 4; et finalement (G) = 4: Les examens peuvent être répartis
     en 4 périodes, de la manière suivante :

                                                                                           18
~~~

## Page 20

~~~text
   1 période, épreuves des cours 1 et 6
      re




   2 période, épreuve du cours 2
      e




   3 période, épreuves des cours 3 et 5
      e




   4 période, épreuves des cours 4 et 7.
      e




b. Un problème d’aquariophilie (exercice du document d’accompagnement )
   A, B, C, D, E, F, G et H désignent huit poissons ; dans le tableau ci-dessous,
   une croix signifie que les poissons ne peuvent cohabiter dans un même aquar-
   ium :
                          A B C D E F G H
                      A        x x x               x x
                      B x                  x x x
                      C x              x       x x x
                      D x          x       x           x
                      E        x       x       x x
                      F        x x         x
                     G x x x               x
                     H x           x x
  Quel nombre minimum d’aquariums faut-il ?
  Solution :
  Construisons le graphe G dont les sommets sont les huit poissons tel que
  deux de ses sommets sont reliés lorsque les poissons associés à ces sommets
  ne peuvent cohabiter. Le nombre minimum d’aquariums est égal au nombre
  chromatique de ce graphe.




  G contient un sous-graphe complet d’ordre 4 (de sommets A; C; D; H ); donc
   (G) > 4: Déterminons une partition des sommets de G en sous-ensembles
  stables :
                             S1   = fA; E g
                             S2   = fB; C g
                             S3   = fD; F; Gg


                                                                              19
~~~

## Page 21

~~~text
                                  S4   =   fH g
      donc   (G) 6 4; et on en déduit que (G) = 4:
5. Algorithme de coloriage des sommets d’un graphe simple
   Voici un algorithme permettant de colorier un graphe simple. Nommons les
   sommets du graphe en ordre de degré décroissant : x 1 ; x2; : : : ; xn ; avec d(xi ) >
   d(xj ) pour 16 i < j 6 n: Attribuons la couleur c 1 à x1 et au sommet suivant
   de la liste qui n’est pas adjacent à x1 et ainsi de suite avec les sommets de la
   liste qui ne sont pas adjacents aux sommets déjà coloriés. Ensuite, on attribue
   la couleur c2 au premier sommet non colorié ainsi qu’aux sommets suivants qui
   ne sont pas adjacents aux sommets coloriés par la couleur c2 : On continue ce
   processus jusqu’à épuisement des sommets de la liste. Remarquons bien que le
   nombre de couleurs ainsi utilisées n’est pas nécessairement minimal.
   Appliquons cet algorithme au graphe de l’exemple précédent. Rangeons les som-
   mets par ordre de degré décroissant :

                                   Sommet      degré
                                     A           5
                                     C           5
                                     B           4
                                     D           4
                                     E           4
                                     G           4
                                     F           3
                                     H           3

   On attribue la couleur c 1 aux sommets : A et E
   On attribue la couleur c 2 aux sommets : C et B
   On attribue la couleur c 3 aux sommets : D,F et G
   On attribue enfin la couleur c 4 au sommet H.


D.6     Graphes valués et problème du plus court chemin
Beaucoup de problèmes peuvent être modélisés en utilisant des graphes valués.
Les problèmes de cheminement dans les graphes, en particulier la recherche du
plus court chemin, comptent parmi les problèmes les plus anciens de la théorie des
graphes et les plus importants par leurs applications : coût de transport, temps de
parcours, problème de trafic,. . . Les algorithmes de recherche de plus court chemin
seront différents selon les caractérisitiques du graphe.
1. Définition
   Un graphe valué est un graphe orienté G = (X; A); muni d’une fonction               :
   A !R + ; appelée fonction de coût.
   Remarque On peut également définir la notion de graphe valué non orienté



                                                                                      20
~~~

## Page 22

~~~text
2. Exemple




                   Graphe valué de modélisation d’un réseau aérien
3. Définitions
   Le coût d’un chemin est la somme des coûts des arcs de ce chemin. On peut
   définir la matrice des coûts du graphe, c’est la matrice C = (c i;j ) où :
                           8
                           < 0 si i = j
                     ci;j = 1 si i 6= j et (xi ; xj ) 2= A
                                (xi ; xj ) si i 6= j et (xi; xj ) 2 A
                           :

4. Définition
   Soit G = (X; A; ) un graphe valué, x et y deux éléments de X: Une chemin c
   de G de x à y est dit minimum lorsque pour tout chemin c 0 de G allant de x à y
   on a : (c0 ) > (c): On définit la matrice M = (mi;j ) de coût minimum par :
                        8
                        < 0 si i = j
                mi;j = 1 s’il n’existe pas de chemin de x à y
                           minf (c) j c chemin de x à y g
                        :




       Décrivons à présent deux algorithmes de recherche de chemin minimum.

5. Algorithme de Dijkstra 1 ( 1959 )
   Numérotons les sommets du graphe de 1 à n: Cet algorithme calcule le plus
   court chemin du sommet 1 à tous les sommets du graphe ( il donnera donc la
   première ligne de la matrice de coût minimum ). On construit un vecteur  =
   ( (1); (2); : : : ; (n)) ayant n composantes tel que  (i) soit égal à la longueur
   du plus court chemin allant de 1 au sommet i: On initialise ce vecteur à (c 1;i );
   c’est-à-dire à la première ligne de la matrice des coûts du graphe. On considère
   ensuite deux ensembles de sommets, S initialisé à f1g et S son complémentaire
   dans X; ensemble des sommets du graphe. À chaque pas de l’algorithme, on
   ajoute à S des sommets jusquà ce que S = X de telle sorte que le vecteur 
   donne à chaque étape le coût minimal des chemins de 1 aux sommets de S:
   1   Edsger Dijsktra, Université d’Amsterdam

                                                                                     21
~~~

## Page 23

~~~text
Description de l’algorithme :
     initialisations
                         = (c1 ) pour i 2 f1; 2; : : : ; ng
                        S = f1g ; S = f2; 3; : : : ; ng
                                 ;i




      itérations
                        Tant que S 6= ;
                        Choisir i dans S tel que (i) est minimum
                        Retirer i de S et l’ajouter à S
                        Pour chaque successeur j de i dans S
                                   (j ) := min( (j ); (i) + (i; j ))


Exemple :
Appliquons l’algorithme de Dijkstra au graphe suivant :




Initialisation
S = f1g ; S = f2; 3; 4; 5g ;  = (0; 15; 1; 1; 4)
1re itération : i = 5 car  (5) = min(15; 1; 1; 4) = 4
S = f1; 5g ; S = f2; 3; 4g ; les successeurs de 5 dans S sont 3 et 4,  (3)
prend la nouvelle valeur min(1; (5) + (5; 3)) = min(1; 4 + 7) = 11;  (4)
prend la nouvelle valeur min(1; (5) + (5; 4)) = 9; d’où le nouveau vecteur
 = (0; 15; 11; 9; 4)
2 itération : i = 4 ; (4) = 9
 e


S = f1; 5; 4g ; S = f2; 3g ;  = (0; 12; 11; 9; 4)
3 itération : i = 3 ;  (3) = 11
 e


S = f1; 5; 4; 3g ; S = f2g ;  = (0; 12; 11; 9; 4)
4 itération : i = 2 ;  (2) = 12
 e


S = f1; 5; 4; 3; 2g ; S = ; ;  = (0; 12; 11; 9; 4)
Le chemin minimal de 1 à 4 par exemple est de coût 9, c’est le chemin 1; 5; 4:
Remarque
Si G = (X; A) est un graphe orienté, on peut considérer la fonction de coût :
                                      :   A ! f1g
                                          a!1

                                                                                22
~~~

## Page 24

~~~text
Le coût d’un chemin du graphe G ainsi valué par est la longueur de ce chemin.
La matrice des coûts est la matrice des distances. L’algorithme de Dijkstra dans
ce cas particulier est en fait l’algorithme de Moore. (voir D.4.2)
Exercice
La matrice qui suit donne en heures les durées des vols entre certaines villes
v1 ; v2; : : : ; v6 :
                        0
                            0   3    1 5 1 11
                        B 3     0    5 2 4 1C
                        B
                        B   1 4      0 1 4 3 C
                                             C
                        B
                        B 6     2    1 0 4 4 C
                                             C
                        @   1 4 4         5
                                             A 0       2
                            1 1 5         4    3       0


le terme (i; j ) de cette matrice est égal à 1 lorque le vol au départ de la ville v i
à destination de vj n’existe pas.
a. Quel est l’itinéraire le plus rapide de v1 à v6 ?
b. S’il y a une escale obligatoire de respectivement 2,3,1,1,4,5 heures aux villes
   v1 ; v2; : : : ; v6; quel est alors l’itinéraire le plus rapide de v 1 à v6 ?
   (a) Appliquons l’algorithme de Dijkstra pour déterminer la valeur d’un chemin
   minimal de v1 à v6 :
   Initialisation
   S = f1g ; S = f2; 3; 4; 5g ;  = (0; 3; 1; 5; 1; 1)
   1re itération : i = 2
   S = f1; 2g ; S = f3; 4; 5; 6g ;  = (0; 3; 8; 5; 7; 1)
   2e itération : i = 4 ;
   S = f1; 2; 4g ; S = f3; 5; 6g ;  = (0; 3; 8; 5; 7; 9)
   3e itération : i = 5 ;
   S = f1; 2; 4; 5g ; S = f3; 6g ;  = (0; 3; 8; 5; 7; 9)
   4e itération : i = 3 ;
   S = f1; 2; 4; 5; 3g ; S = f6g ;  = (0; 3; 8; 5; 7; 9)
   5e itération : i = 6 ;
   S = f1; 2; 4; 5; 3; 6g ; S = ; ;  = (0; 3; 8; 5; 7; 9)
   L’itinéraire le plus rapide nécessite donc 9 heures pour aller de la ville v 1 à
   la ville v6: L’itinéraire v1; v4; v6 est un itinéraire minimum. (Il y en a deux
   autres...)
   (b) On applique le même algorithme à la nouvelle matrice des durées, obtenue
   en ajoutant au vol de vi à vj la durée de l’escale en vj ; c’est-à-dire au graphe
   de matrice des coûts :




                                                                                   23
~~~

## Page 25

~~~text
                               0
                                    0            6       1 6 1 11
                               B 5               0       6 3 8 1C
                               B
                               B    1 7                  0 1 8 3 C
                                                                 C
                               B
                               B 8    5                  1 0 8 4 C
                                                                 C
                               @    1 7 5                   6
                                                                 A     0     2
                                    1 1 6                   5          7     0

      on trouve à nouveau v1; v4; v6 comme itinéraire minimal (en terme de durée),
      de durée 10 heures.
6. L’algorithme de Maria Hasse2
   Cette méthode consiste à calculer la matrice des coûts minimums. Considérons
   les opérations  et définies sur [0; 1] =R + [ f0; 1g par :
                                        a  b = min(a; b)
                                        a b = a+b
  Définissons alors un nouveau produit matriciel en remplaçant l’addition et la
  multiplication des réels par  et    respectivement. Le produit des matrices
  M = (mi;j ) et N = (ni;j ) de Mn (R ) est la matrice P = (pi;j ) où :
                     p
                     i;j   =   n
                                k =1
                                       m   i;k       nk;j   =
                                                                k
                                                                     min
                                                                    2f1 2
                                                                       ; ;:::ng
                                                                                 (   m
                                                                                     i;k   +   nk;j   )

  a. Théorème
     Soit G = (X; A; ) un graphe valué de matrice des coûts C = (ci;j ): Si k est
     un entier naturel tel que C k = C k+1 ; alors C k est la matrice des coûts mini-
     mums.(les puissances successives de la matrice C é tant calculées à l’aide des
     opérations décrites précédemment)
     Démonstration
     Montrons par récurrence sur k que c i;j est le minimum parmi les coûts des
                                            (k )

     chemins de longueur inférieure à k de x i à xj : Pour k = 1; c’est clair. Sup-
     posons le résulat vrai pour l’entier k 1; alors minl (ci;l        + cl;j ) = ci;j
                                                                 (k 1)             (k )

     représente bien le minimum des coûts des chemins de longueur k allant de x i
     à xj : Si pour un certain entier k on a C k = C k+1 ; alors pour tout entier na-
     turel m > k; C m = C k ; ci;j désigne alors le minimum des coûts des chemins
                                (k )


     de longueur quelconque allant de x i à xj ; C k est bien la matrice des coûts
     minimums.
  b. Voici une procédure Maple calculant la matrice des coûts minimums en util-
     isant la méthode de Maria Hasse.
     On prend 1 000 000 pour représenter l’infini

  > i:=10^6:
  La procédure produit calcule le produit de 2 matrices à l’aide des nouvelles
opérations
  > produit:=proc(A,B::matrix)
  local i,j,k,n,C;

  2   Maria Hasse, Université de Halle Wittenberg

                                                                                                          24
~~~

## Page 26

~~~text
  n:=rowdim(A):
     for i to n do
          for j to n do
             C[i,j]:=min(seq(A[i,k]+B[k,j],k=1..n)):
          od;
     od;
  matrix(n,n,[seq(seq(C[i,j],j=1..n),i=1..n)]):
  end:
  La procédure hasse détermine le plus petit entier k et affiche la matrice des coûts
minimums.
  > hasse:=proc(C::matrix)local k,n,A,B;
  k:=1:
  n:=rowdim(C);
  A:=copy(C);
  B:=produit(A,A);
     while not equal(A,B) do
          A:=copy(B);
          B:=produit(B,C);
          k:=k+1;
     od;
  print(cat(‘k=‘,k,‘ ‘,‘la matrice des coûts minimums est‘));
  evalm(matrix(n,n,[seq(seq(B[i,j],j=1..n),i=1..n)]));
  end:

Exemple
Appliquons la métode de Hasse pour déterminer la matrice des coûts minimums du
graphe valué suivant :




                                                                                  25
~~~

## Page 27

~~~text
La matrice des coûts de ce graphe est :
                                    0
                                         01 1 4 11
                                                 8
                                   B 1 0 3 1 8 1 C
                                   B 1 1 0 2 1 1 C
                                   B              C
                               C = B 13 3 1 0 1 5 C
                                   B              C
                                   @ 1 1 1 5 0 1 A
                                     1  1 1 1 6 0
La procédure Maple renvoie la matrice des coûts minimums au bout de la qua-
trième itération
                                     0                                       1
                                         0       8       11   9    4    14
                                  B 11           0       3    5    8    10 C
                                  B                                      C
                               M =B
                                  B
                                    8            5       0    2    12   7C
                                                                         C
                                  B 6            3       6    0    10 5 C
                                  @ 11           8       11   5    0  10
                                                                         A
                                         1       9       12   10   5    0


La connaissance des puissances intermédiaires de C est nécessaire pour déterminer
un chemin minimal. Cherchons par exemple un chemin de coût minimal de x 2 à x1 :

                  0
                      0   8    11   9   11   4
                                               0
                                                 0 8 11                               9    4    14
                                                                                                     1
             B        1 0 3         5 8 1 C    B 18 0 3                               5    8    10 C
                                    2 1 7 C
             B                            C    B                                                 C
             B 15         5     0              B 8 5 0                                2    13   7C
   C   2
           = B                            CC = B
                                                              3
                                                                                                 C
             B 6          3     6   0    11          5   C         B 6 3 6            0    10 5 C
             @ 18         8 1 5              0   10
                                                         A         @ 11 8 11          5     0 10
                                                                                                 A
                      1   9 1 11             5       0                  1    9   12   10   5    0
                  0                                      1
                      0   8    11   9        4   14
                  B 11    0     3   5        8   10 C
             B                                 C
             B 8 5 0                2    12    C     7
   C   4
           = B                                 C
             B 6 3 6                0    10 5 C
             @ 11 8 11              5     0 10
                                               A
                      1   9    12   10       5       0


Comme c2;1 = 18 6= c2;1 = 11; le coût du chemin minimal de x 2 à x1 est égal à 11.
            (3)               (4)


Comme c2;i +ci;1 = 11 pour i = 6; le chemin se termine par l’arc (x 6; x1) ; de même
           (3)


c(3)
 2;6 = 10 = c2;i + ci;6 pour i = 4; les deux derniers arcs sont (x4 ; x6 ); (x6 ; x1 ): ;
               (2)


enfin, c2;4 = 5 = c2;3 + c3;4; le deuxième arc est (x3; x4 ): Finalement, le chemin
        (2)

cherché est : x2; x3; x4 ; x6; x1:



                                                                                                         26
~~~

## Page 28

~~~text
D.7     Graphes probabilistes


D.7.1     Chaîne de Markov

1. Définitions
   Soit n un entier naturel non nul. Un vecteur stochastique de R n est un vecteur
   X tel que :
                                                                                  X
                                                                                  n


                               8i 2 f1; 2; : : : ng; X > 0;    i                            X = 1:
                                                                                                i

                                                                                  i=1

   Une matrice P de Mn (R ) est dite stochastique, lorsque :

                               8(i; j ) 2 f1; 2; : : : ; ng ; P > 0       2
                                                                                      i;j

                                                            X                     n


                                    8i 2 f1; 2; : : : ; ng P = 1                            i;j

                                                                              j =1

   Une matrice stochastique est donc une matrice dont chacune des lignes est un
   vecteur stochastique.
2. Propriété
   Si X est un vecteur stochastique de R n et si P est une matrice stochastique de
   Mn (R ), alors XP est un vecteur stochatisque de R n :
   En effet, pour tout j 2 f1; 2; : : : ; ng;
                                                          X
                                                          n


                                         (XP ) = j                 XPi    i;j     >0
                                                          i=1

   et
            X
            n
                                  X
                                  n
                                    X
                                    n
                                                                   X
                                                                   n
                                                                                  X
                                                                                  n
                                                                                                           X
                                                                                                           n


                   (XP ) = j                   XPi   i;j =                X   i             P i;j =                  X =1
                                                                                                                      i

            j =1                  j =1   i=1                       i=1            j =1                     i=1


3. Propriété
   Si P et Q sont deux matrices stochastiques de Mn (R ), alors P Q est encore une
   matrice stochastique de Mn (R ).
   En effet, pour tout (i; j ) 2 f1; 2; : : : ; ng2;
                                                         X
                                                         n


                                     (   P Q)  i;j   =             P Q
                                                                    i;k       k;j     >0
                                                         k =1

   et pour tout i 2 f1; 2; : : : ; ng
               X
               n
                                         X
                                         n
                                           X
                                           n
                                                                          X
                                                                          n
                                                                                                    X
                                                                                                    n


                       (P Q)    i;j =                P Q i;k    k;j =                  P    i;k            Q   k;j   =1
                j =1                     j =1 k =1                         k =1                     j =1

   On montre alors par récurrence que pour tout entier naturel m; P m est une ma-
   trice stochastique.




                                                                                                                            27
~~~

## Page 29

~~~text
4. Définition
   Fixons S un ensemble fini, appelé ensemble des états. Une chaîne de Markov 3
   à temps discret sur S est une suite de variables aléatoires à valeurs dans S;
   X= (Xn )n0 satisfaisant les deux conditions suivantes :
          (a). (Condition d’indépendance)
               Pour tout n > 0 et pour tout choix de i 0; i1; : : : ; in 1 et i dans S pour
               lesquels P[(X0; X1 ; : : : ; Xn ) = (io ; i1; : : : ; in 1 ; i)] > 0; on a :
                    P[X     n+1          = j j (X0 ; X1 ; : : : ; X ) = (i ; i1 ; : : : ; i
                                                                                n        o            n   1   ; i)]
                                         = P[X +1 = j j X = i]
                                                      n                 n


          (b). (Condition d’homogénéité)
               Pour tout i et pour tout j dans S et pour tous les entiers n tels que
               P[Xn = i] > 0; la probabilité conditionnelle P[X n+1 = j j Xn = i]
               ne dépend pas de n:

5. Définitions
   Soit X= (Xn )n>0 une chaîne de Markov sur un ensemble S
   La matrice P = (pi;j )(i;j )2S 2 définie par :
                                               pi;j   =   P[X     n+1   =   j j X = i]
                                                                                    n

   s’appelle la matrice de transition de la chaîne de Markov.
   La distribution  0 = (P[X0 = i])i2S s’appelle la loi initiale de la chaîne de
   Markov.
   Remarque : la matrice P est une matrice stochastique, en effet :
      X                     X
              p   i;j   =               P[X   n+1   =   j j X = i] = P( n = ) [[ 2 (X +1 = j )] = 1
                                                              n                     X    i    j   S   n

      j   2
          S                 j   2   S



   Exemple
   Considérons une particule qui se déplace de façon aléatoire, l’ensemble S représente
   l’ensemble de toutes les positions possibles (que l’on suppose être en nombre
   fini). Pour tout n 2N , la variable X n représente la position de la particule à
   l’instant n; donc après n déplacements. Si après n transitions la particule est à
   la position i; alors elle choisira aléatoirement sa (n + 1)ième position selon la
   distribution de probabilité (P i;j )j 2S et ce indépendamment de n et de ses états
   aux instants qui ont précédé:
6. Propriété
   Notons S = f1; 2; : : : ; rg et pour tout instant n;
    n = (P(Xn = 1);P[Xn = 2]; : : : ;P[Xn = r]): On a alors pour tout n 2N :
                                                            +1 =  P
                                                              n             n

   En effet, pour tout j 2 S :
              ( +1 )
                   n        j       =     P[X   n+1       j
                                                        = ]=       P[([ 2 (Xi   S       n+1   = ) j \ (X = i))]
                                                                                                          n




  3   Andrei Andreyevich Markov (1856-1922) Élève de Chebyshev, professeur à St Petersburg.
   Ses travaux ont porté sur l’analyse, la théorie des nombres et les processus aléatoires.

                                                                                                                      28
~~~

## Page 30

~~~text
                                               X
                                   =                       P[X = i]P[(X    n                               n+1       = )     j j (X = i)]    n

                                               i   2   S
                                               X
                                   =                       ( )p   n   i           i;j   =(     P)n            j

                                               i   2   S

   La loi de la chaîne de Markov est donc entièrement déterminée par la donnée de
   sa matrice de transition P et de l’état initial  0:
7. Théorème
   Si la matrice de transition P a tous ses coefficients strictement positifs, alors :
   – la suite ( n ) converge vers un vecteur  indépendant de la distribution initiale.
   – La suite des matrices (P m ) converge vers une matrice stochastique P1 dont
     toutes les lignes sont égales au vecteur : De plus,  = P1
     Démonstration
     Soit n un entier naturel supérieur ou égal à 2. Notons P n l’ensemble des ma-
     trices stochastiques de Mn (R ) et K n l’ensemble des vecteurs lignes stochas-
     tiques de M1;n (R ).
     Pour une matrice P = (p i;j ) de P n ; introduisons les notations suivantes :
                    !       =
                                      1  1 
                                           i
                                                p ; 8m 2 N , P
                                               min
                                                   n;          j       n
                                                                                   i;j
                                                                                                                             m
                                                                                                                                 = ( i;j ) p( )
                                                                                                                                             m




                8m 2 N , 8j 2 f1; 2; : : : ; ng;
                (m)
                j
                            =         min
                                      1   
                                           i       n
                                                        p( ) ;
                                                           i;j
                                                               m                   (m)
                                                                                   j
                                                                                         = max
                                                                                               1     i    n
                                                                                                                    p( ) et Æ ( ) =
                                                                                                                      m
                                                                                                                     i;j               j
                                                                                                                                        m                (m)
                                                                                                                                                         j
                                                                                                                                                                     (m)
                                                                                                                                                                     j



     Établissons les deux inégalités :
                                                                       (m+1)
                                                                       j
                                                                                         6         (m)
                                                                                                   j
                                                                                                         !Æ ( )              j
                                                                                                                              m
                                                                                                                                                                               (1)
                                                                       (m+1)
                                                                                         >         ( )
                                                                                                       + !Æ
                                                                                                       m    ( )               m
                                                                                                                                                                               (2)
     pour j 2 f1; 2; : : : ; ng et m 2N .
                                                                       j                           j                         j




     Soit k0 vérifiant pk0 ;j = j : On a :
                         (m)       (m)



                            X
                            n
                                                                                                               X
     p(m+1)
      i;j
                    =                     p p( ) = p ; 0 p( 0 ) +
                                           i;k
                                                        m

                                                       k;j                         i k    k ;j
                                                                                              m
                                                                                                                             p p( )
                                                                                                                              i;k   k;j
                                                                                                                                        m



                              k =1                                                                              6
                                                                                                               k =k0
                                                                                               !
                                                                           X
                    6 p; p        i k0
                                               (m)
                                               k0 ;j
                                                           +                             p;
                                                                                         i k
                                                                                                            (m)
                                                                                                            j
                                                                                                                         =    p ; 0 p( 0 ) + (1 p 0 ) ( )
                                                                                                                                 i k         k ;j
                                                                                                                                                 m
                                                                                                                                                                     i;k
                                                                                                                                                                           m
                                                                                                                                                                           j

                                                                               6
                                                                           k =k0


                    =   p 0(      (m)
                                  j
                                      p( 0 ) ) = ( ) p 0 ( ( )
                                                       i;k
                                                                  ( )
                                                                      )
                                                                           (m)
                                                                           j
                                                                                              m
                                                                                              k ;j                       j
                                                                                                                          m
                                                                                                                                           i;k
                                                                                                                                                     m
                                                                                                                                                     j
                                                                                                                                                                 m
                                                                                                                                                                 j


            =
                  ( )
                        p 0Æ 6( )
                                  j
                                      ( )
                                      m
                                                !Æ ( )
                                                       i;k         j
                                                                       m
                                                                                          j
                                                                                              m
                                                                                                                     j
                                                                                                                         m




     En prenant le max sur i; on obtient :
                                               ( +1)
                                                     6 ( ) !Æ( ):                                          j
                                                                                                            m
                                                                                                                                    j
                                                                                                                                        m
                                                                                                                                                         j
                                                                                                                                                             m




     L’inégalité (2) se démontre de la même manière en considérant k 0 tel que
     p( 0 ) =
         m
         k ;j
                        (m)
                        j
                              :
                                                                                                            (m)
     L’inégalité (1) montre que la suite ( j )m est décroissante, l’inégalité (2)
     permet d’établir la croissance de la suite ( j )m : En faisant la différence de
                                                  (m)




                                                                                                                                                                               29
~~~

## Page 31

~~~text
(1) et de (2), on obtient :
                       (m+1)
                       j
                                             (m+1)
                                             j
                                                             6       (m)
                                                                     j
                                                                                         (m)
                                                                                         j
                                                                                                     2   !Æ ( )
                                                                                                           j
                                                                                                            m



c’est-à-dire :
                                       Æ ( +1) 6 (1
                                         j
                                             m
                                                                                 ! Æ( )
                                                                             2 ) j
                                                                                             m



D’où, pour tout entier m :
                               0   6Æ            (m+1)
                                                                6 (1             2 ) ! Æ(1)  m



          ! 2 [0; 1[; en effet :
                                                 j                                               j

Or (1    2 )
                           X
                           n
                                                     X
                                                     n


                   1=              p   i;j       >               ! = n! ) ! 6
                                                                                                     1
                                                                                                      6
                                                                                                     n 2
                                                                                                        1

                           j =1                          j =1

et ! > 0, car on a supposé que les coefficients de P étaient strictement positifs.
On en déduit alors que :

                                                     m
                                                      lim
                                                      !+1
                                                                  Æ( ) = 0
                                                                     j
                                                                         m




                 (m)               (m)
Les suites ( j )m et ( j )m sont alors adjacentes et vont converger vers une
limite commune lj:
Or pour tout (i; j ) 2 f1; 2; : : : ; ng 2
                                                 (m)
                                                 j
                                                          6p 6    (m)
                                                                  i;j
                                                                                     (m)
                                                                                     j

Le théorème des limites par encadrement permet alors d’affirmer que la suite
(pi;j )m converge vers lj :
  (m)

Posons alors L = (l1; l2; : : : ; ln ) et soit P1 la matrice dont toutes les lignes
sont égales à L; on a alors :
                                                 m
                                                     lim
                                                     !+1
                                                                 P   m
                                                                             =   P1
De plus, si Xn est la matrice colonne dont les coefficients valent 1:
P1 Xn = lim P m Xn = lim Xn (car chaque P m est stochastique)
               m !+1                                 m    !+1
         =     X   n

ce qui prouve bien que la matrice limite P 1 est stochastique.
D’autre part, on a vu que pour tout m;  m = 0 P m ; la suite ( m ) converge
alors vers le vecteur ligne  =  0P1 vérifiant :
                        P1 = 0 P12 = P1 = 
en effet, la suite (P 2 ) converge vers P1 comme sous-suite de la suite con-
                            m


vergente (P ); et comme P 2 = (P )2 ; elle converge également vers P1
             m                                           m               m  2
                                                                              :
Par unicité de la limite, on a bien P 1 = P1 :
                                      2

Il reste à démontrer que le vecteur ligne  est indépendant de la distribution
initiale  0:
Le vecteur ligne L obtenu précédemment, vérifie également LP 1 = L; en
effet, pour tout entier m; on a P P = P +1 ; par passage à la limite, P1 P =
                                                             m                   m

                                                                     0
                                                                       LP 1
P1 : En interprétant le produit par blocs, on constate que : P 1 P = @ ... A :
                                                                       LP
On en déduit alors que LP = L: Soit maintenant L 0 un vecteur ligne vérifi-
ant L0 P = L0 ; alors L0 P = L0 pour tout entier m; à la limite, L 0 P1 = L0 :
                                        m




                                                                                                                  30
~~~

## Page 32

~~~text
 Notons L0 = (l10 ; l20 ; : : : ; ln0 ); alors :
                                                                       !
                                                           X
                                                           n


                                  L0P1 = L0 )                      l 0 L = L0
                                                                   i

                                                           i=1

 L0 est donc colinéaire à L: On en déduit que l’espace des vecteurs lignes X
 vérifiant XP = X est la droite engendrée par L; son seul élément stochastique
 est le vecteur L = : En particulier, le vecteur ligne  ne dépend pas de  0 ;
 puisque sa caractérisation n’évoque que P:
    Autre démonstration (dans le cas :jS j = 2; ) voir exercice F.9 pour une
 application numérique)

 On considère la décomposition de la matrice P suivante :
                                            
      P=        1       p         p              =   Q + (1 p q )R; avec (p; q ) 2]0; 1[2
                    q         1          q
 où
                                                                       0
                        0        q               p    1  p 1               p
        Q = @ p +q q p +p q A et R = B    @
                                              p+q p+q C
                                                q       q A
                 p+q p+q                      p+q p+q
 On remarquera que Q est une matrice stochastique dont les lignes sont égales.
 Calculons le produit QR :
                                                                                      
                        (1  p q)
                              q p        p      p = 0 0
        QR =                  q p          q q
                         (p + q )2                        0 0
 Un calcul identique montre que RQ est la matrice nulle. Calculons maintenant
 les puissances successives de Q et de R :
                                                                                          
Q =
 2              1   q p        q p = 1                 q 2 + pq pq + p2
        (p + q )2   q p        q p        (p + q )2    q 2 + pq pq + p2
                                        
           1        q (p + q ) p(p + q )
    =
        (p + q )2   q (p + q ) p(p + q ) = Q
 On en déduit par récurrence, que pour tout entier n; Q = Q: On montre de la       n




 même manière que pour tout entier n; R n = R: Finalement, en développant
 par la formule du binôme, on obtient :

                P   Q + (1 p q )R) = Q + (1 p q ) R
                    n
                        =(
                                                           n                           n



 et comme j1 p q j < 1; la suite (P ) converge vers la matrice stochas-
                                                               n
                                                                   n



 tique à lignes égales Q :
                                   0 q       p 1
                 lim P = P
                           1 =Q=@ p+q p+q A
                !+1 n
                                     n
                                      q      p
                                     p+q p+q


                                                                                                   31
~~~

## Page 33

~~~text
     On conclut alors de la même manière que dans la démonstration précédente.




D.7.2     Graphes probabilistes

1. Définitions
   Un graphe probabiliste est un graphe orienté et valué tel que la somme des coûts
   des arcs issus d’un sommet donné est égal à 1.
   La matrice de transition d’un graphe probabiliste G = (X; A; ) d’ordre n; est
   la matrice P = (pi;j ) 2Mn (R ) où :
                                 
                                                   (i; j ) 2 A
                           pi;j = 0 (sii; (ji;) si
                                                j ) 2= A
   Remarques :
   – pour tout i 2 f1; 2; : : : ; ng;
                                        X
                                        n


                                               pi;j   =1
                                        j =1

     La matrice de transition d’un graphe probabiliste est donc une matrice stochas-
     tique.
   – Les graphes probabilistes sont utilisés pour modéliser l’évolution d’un indi-
     vidu pouvant changer aléatoirement d’état : les sommets sont les états possi-
     bles et le coût de l’arc (i; j ) est la probabilité de transition de l’état i à l’état
     j:
   – L’état probabiliste de l’individu à l’instant n 2N est une loi de probabilité sur
     l’ensemble des états possibles et qui est représentée par un vecteur stochas-
     tique  n : Lorsque les hypothèses d’indé pendance et d’homogénéité sont véri-
     fiées (cf définition d’une chaîne de Markov), on :  n =  0P n

     Exemple
     Un dispositif comprend deux éléments fonctionnant indépendamment l’un de
     l’autre. Chaque élément a une probabilité égale à p de tomber en panne au
     cours d’une journée. Au départ, les deux éléments fonctionnent correctement
     et il n’y a pas de réparation possible.
     Ce processus sera dans l’état 0; 1 ou 2 selon qu’il y a zéro, une ou deux ma-
     chines en panne au début d’une journée. Le processus aléatoire peut être
     représenté par le graphe probabiliste :




                                                                                        32
~~~

## Page 34

~~~text
La matrice de transition est :
                        0                       1
                            (1   p)2 2p(1 p) p2
                  P =@ 0             1   p   p A
                            0       0       1




                                                    33
~~~

## Page 35

~~~text
E    Les graphes en Terminale ES

    1. Le programme
       a. Vocabulaire élémentaire des graphes
          Sommets, sommets adjacents, arêtes, degré d’un sommet, ordre d’un graphe,
          chaîne, longueur d’une chaîne, graphe complet, distance entre deux sommets,
          diamètre, sous-graphe stable, graphe connexe, nombre chromatique, chaîne
          eulérienne, matrice associée à un graphe, matrice de transition pour un graphe
          pondéré par des probabilités.
          Un lexique sera fourni dans le document d’accompagnement, il définira claire-
          ment les limites du programme, toute notion qui ne correspondrait pas à l’un
          des termes du lexique est hors programme.
          Les termes du lexique seront introduits à l’occasion de résolution de prob-
          lèmes.
       b. Résultats élémentaires sur les graphes


           Lien entre la somme des degrés des sommets et le nombre d’arêtes
           Conditions d’existence de chaînes et de cycles eulériens (théorème d’Euler)
           Le terme (i; j ) de la matrice A (A est la matrice associée à un graphe)
                                              n


            donne le nombre de chaînes de longueur n reliant les sommets i et j
           Le nombre chromatique d’un graphe est inférieur ou égal à r + 1; r étant le
            plus haut des degrés du graphe.
           Si P est la matrice de transition d’un graphe probabiliste à n sommets,
            l’état probabiliste à l’étape n est  0P n ; où 0 est la matrice ligne décrivant
            l’état initial
           Exemple de convergence pour des graphes probabilistes à deux sommets :
            lorsque la matrice P de transition ne comporte pas de 0, l’état  n à l’état n;
            converge vers un état  indépendant de l’état initial  0 vérifiant  = P:
            Ces propriétes figurent au programme, elles seront introduites à l’occasion
            de problèmes. Elles pourront être démontrées ou commentées.

    2. Commentaires
       L’enseignement des graphes en Terminale ES est entièrement fondé sur la ré-
       solution de problèmes. L’objectif est de savoir modéliser des situations par des
       graphes et d’identifier en terme de propriétés de graphes la question à résoudre.




                                                                                          34
~~~

## Page 36

~~~text
F    Exercices

      F.1 Tracer le graphe de la matrice d’adjacence suivante :
       0                   1
           1   1   1   0
       B 0 0 1 0 C
       B         C
       @ 1 1 0 1 A
           1   1   1   0

     F.2 Montrer que dans une assemblée, il y a au moins deux personnes qui ont le
    même nombre d’amis.

      F.3 Combien y-a-t-il de graphes simples G = (X; A) tels que X = f1; 2; : : : ; ng?

      F.4 Existe-t-il un graphe simple d’ordre 5 dont les sommets ont les degrés suiv-
    ants ? Si oui, tracer un tel graphe :

       a. 3,3,3,3,2
       b. 1,2,3,4,5


      F.5 Combien y-a-t-il de sommets dans un graphe régulier de degré 4 ayant 10
    arêtes ?

      F.6 Calculer le diamètre des graphes Kn ; Cn et Kp;q :

       F.7 Pour traverser une chaîne de montagnes, il faut passer par plusieurs sommets,
    reliés entre eux par des voies ne pouvant être franchies que dans un seul sens. On
    donne ci-dessous le graphe associé à cette situation (E est le point d’entrée et S le
    point de sortie). L’office de tourisme cherche toutes les traversées qui partent de E
    et arrivent en S en 4,5 ou 8 étapes (une étape est le passage d’un sommet à un autre,
    ou du départ à un sommet, ou d’un sommet à l’arrivée).




                                                                                      35
~~~

## Page 37

~~~text
Les sommets étant classés dans l’ordre E; A; B; C; G; D; F; S; la matrice d’adjacence
du graphe est :
                              0                                   1
                                  0   1   1   1   0   0   0   0
                          B 0         0   0   0   1   1   0   0 C
                          B                                     C
                          B 0         1   0   0   0   0   0   0 C
                          B                                     C
                       M =B
                          B
                            0         0   1   0   1   0   1   0 C
                                                                C
                          B 0         0   0   0   0   0   1   0 C
                          B                                     C
                          B 0         0   0   0   1   0   0   1 C
                          @ 0         0   0   0   0   1   0   1
                                                                A
                                  0   0   0   0   0   0   0   0


Après calcul des puissances successives de la matrice M; on obtient :
                              0                                   1
                                  0   0   0   0   3   3   2   4
                          B 0         0   0   0   1   1   0   2 C
                          B                                     C
                          B 0         0   0   0   0   1   1   1 C
                          B                                     C
                       M =B
                        4
                          B
                            0         0   0   0   2   0   2   2 C
                                                                C
                          B 0         0   0   0   0   0   1   0 C
                          B                                     C
                          B 0         0   0   0   1   0   0   1 C
                          @ 0         0   0   0   0   1   0   1
                                                                A
                                  0   0   0   0   0   0   0   0


  – la première ligne de M 3 est : 0 1 0 0 2 2 2 2
  – la première ligne de M 5 est : 0 0 0 0 3 2 3 5
  – la première ligne de M 6 est : 0 0 0 0 2 3 3 5
  – la première ligne de M 7 est : 0 0 0 0 3 3 2 6
  – la première ligne de M 8 est : 0 0 0 0 3 2 3 5


   a. Combien de traversées peut-on faire en 4 (respectivement 5) étapes ?
   b. Trouver toutes les traversées en 8 étapes.
      (exercice proposé par le GEPS)


  F.8 Un individu vit dans un milieu où il est susceptible d’attraper une maladie
par piqûre d’insecte. Il peut être dans l’un des trois états suivants : immunisé (I),
malade (M), non malade et non immunisé (S). D’un mois à l’autre, son état peut
changer selon les règles suivantes :
– étant immunisé, il peut le rester avec une probabilité 0,9 ou passer à l’état S avec
  une probabilié 0,1;
– étant dans l’état S, il peut le rester avec une probabilité 0,5 ou passer à l’état M
  avec une probabilité 0,5 ;

                                                                                   36
~~~

## Page 38

~~~text
– étant malade, il peut le rester avec une probabilité 0,2 ou passer à l’état I avec
  une probabilité 0,8.
   Tracer un graphe probabiliste pour décrire cette situation et écrire la matrice de
transition. Calculer l’état de probabilité de l’individu au bout de trois mois, de six
mois, d’un an, de deux ans, pour chacune des situations suivantes :
– au, départ, il est immunisé,
– au départ, il est non malade et non immunisé,
– au départ, il est malade.
  Pouvez-vous donner des éléments sur la proportion d’individus malades dans la
population étudiée ?
(exercice proposé par le GEPS)

  F.9 Chaque matin, l’allumeur de réverbère du Petit Prince change l’état de sa
planète avec une probabilité 0,75. Au jour 0, le réverbère est éteint.
– Qu’observe-t-on en simulant une grande population de réverbères régis par le
  même système probabiliste de changements d’états ?
– Faire un arbre permettant de trouver l’état probabiliste du réverbère au deuxième
  jour.
– Décrire cette situation à l’aide d’un graphe proababiliste. Soit M la matrice de
  transition associée à ce graphe. Vérifier que :
                                                                             
                                          1                   1       1   1
                       M      =   N           R; oùN =                1   1
                                          2                   2
                                                     
                                  1           1   1
                     et R     =                           :
                                  2           1   1

– Calculer N 2 ; R2 ; NR et RN puis en déduire M n ; pour n entier naturel.
– Au jour 0, le reverbère est allumé (respectivement éteint). Calculer la probabilité
  pn (respectivement p0n ) que le réverbère soit allumé (respectivement éteint) au
  nième matin. Faire le lien avec les résultats des simulations observées en pre-
  mière question.
  (exercice proposé par le GEPS)

   F.10 Montrer que, parmi 6 personnes, il y a un groupe de 3 qui se connaissent
mutuellement, ou bien un groupe de 3 qui ne se connaissent pas. (on suppose que
la relation de connaissance est une relation symétrique)




                                                                                   37
~~~

## Page 39

~~~text
G     Solutions des exercices

      F.1




       F.2 Considérons le graphe dont les sommets sont les n personnes de l’assemblée.
    On suppose bien entendu, que la relation d’amitié est une relation symétrique. Deux
    sommets du graphe sont reliés par une arê te lorsque les deux personnes correspon-
    dantes sont amies. Il suffit alors de prouver que deux sommets au moins de ce
    graphe ont même degré. Supposons que les n sommets soient tous de degré dis-
    tinct. On peut alors numéroter les sommets de x1 à xn avec :
                               0   6 d(x ) < d(x ) < : : : < d(x
                                           0       1                n   1)

    Or le degré maximal d’un sommet d’un graphe simple d’ordre n est égal à n 1:
    On a donc nécessairement d(xi ) = i; pour tout i de f0; 1; : : : ; n 1g: Avec notre
    hypothèse, le graphe comprendrait un sommet de degré 0 (c’est une personne bien
    seule ...) et un sommet de degré n 1; donc relié à tous les autres sommets du
    graphe, en particulier au sommet isolé, ce qui est contradictoire. Nous avons donc
    montré qu’un graphe simple contient au moins deux sommets de même degré.

      F.3 Un graphe simple G = (f1; 2; : : : ; ng; A) est déterminé par ladonnée de A
                                                                                   n
    qui est une partie de P 2 (f1; 2; : : : ; ng). Or jP 2(f1; 2; : : : ; ng)j =       : Le nombre
                                                                                  2
                                     n

    de graphe est donc égal à 2 2

      F.4

       a. Oui, par exemple :




       b. Non, la somme des degrés est impaire


                                                                                               38
~~~

## Page 40

~~~text
    F.5 Notons G = (X; A) le graphe, on a :
                                       X
                                               d(x)   =   2   j Aj
                                       2
                                       x   X


                                                      ) 4 jX j = 20
                                                      ) jX j = 5

  F.6 Pour tout sommet x de Kn ; maxy2X (d(x; y )) = 1; donc Æ(Kn ) = 1:
                                               n
Pour tout sommet x de C n ; maxy2X (d(x; y )) = si n est pair, et maxy2X (d(x; y )) =
                                                                2
n     1                                                         n                                   n   1
       lorsque n est impair. Donc Æ(Cn ) =    si n est pair, et Æ (Cn ) =
   2                                        2                             2
lorsque n est impair.
Pour tout sommet x de K p;q maxy2X (d(x; y )) = 2; donc Æ(Kp;q ) = 2; lorsque
(p; q ) 6= (1; 1); Æ(K1 1 ) = 1:
                       ;




    F.7

     i. m1;8 = 4; il y a donc 4 traversées possibles en 4 étapes.
           (4)


        m(5)
         1;8 = 5; il y a donc 5 traversées possibles en 5 étapes.


    ii. m1;8 = 5; il y a donc 5 traversées possibles en 8 étapes. Déterminons ces
           (8)


        traversées. Pour cela, notons X la quatrième étape des traversées possibles.
        D’après la première ligne de M 4 ; l’étape X ne peut être que l’un des sommets
        G; D; F ou S:
           X ne peut être le sommet G; en effet, m                  (4)
                                                                     5;8   = 0 et on ne peut joindre le
           sommet S à partir de G en 4 étapes.
           Si X = D : m       (4)
                               1;6    ; il a donc 3 chemins de longueur 4 allant de E
                                       = 3
            à D; ce sont les chemins :E; A; G; F; D ; E; C; B; A; D et E; C; G; F; D:
            D’autre part, m6 8 = 1; il y a un chemin joignant D à S; c’est le chemin
                              (4)
                               ;

            D; G; F; D; S: Nous obtenons ainsi 3 traversées en 8 é tapes ayant le som-
            met D comme 4 étape : E; A; G; F; D; G; F; D; S ; E; C; B; A; D; G; F; D; S
                           e


            et E; C; G; F; D; G; F; D; S:
           Si X = F : m(4)    1 7 = 2; il a donc 2 chemins de longueur 4 allant de E
                                   ;

            à F; ce sont les chemins : E; B; A; G; F et E; A; D; G; F: D’autre part
            m(4)
               7 8 = 1; il n’y a qu’un seul chemin de longueur 4 allant de F à S: Nous
                 ;

            obtenons ainsi 2 traversées en 8 étapes ayant le sommet F comme 4 étape             e


            : E; B; A; G; F; D; G; F; S et E; A; D; G; F; D; G; F; S:

           Finalement, les cinq traversées cherchées sont : E; A; G; F; D; G; F; D; S ;
           E; C; B; A; D; G; F; D; S ; E; C; G; F; D; G; F; D; S ; E; B; A; G; F; D; G; F; S
           et E; A; D; G; F; D; G; F; S:




                                                                                                        39
~~~

## Page 41

~~~text
  F.8 Voici le graphe probabiliste traduisant la situation dé crite :




Les sommets étant classés dans l’ordre I, M, S la matrice de transition est :
                                   0                      1
                                      ;  0 90    0; 1
                            P = @ 0; 8 0; 2 0 A
                                      0    0; 5 0; 5
Notons  l’état probabiliste de l’individu au nième mois, à l’aide de la calculatrice
         n



ou de l’ordinateur, on obtient les résultats suivants :

   i. si 0 = (1; 0; 0) : 3 = (0; 769; 0; 08; 0; 151);  6 = (0; 753921; 0; 094805; 0; 151274);
       12 = (0; 7547190369; 0; 09433818392; 0; 1509427793);
       24 = (0; 7547169811; 0; 09433962264; 0; 1509433962);
  ii. Lorsque 0 = (0; 1; 0) ou 0 = (0; 0; 1) on constate que l’état probabiliste de
      l’individu se stabilise également vers (0; 755; 0; 094; 0; 151):
      Remarque
      Le théorème D7.7 admet la généralisation suivante : s’il existe un entier m tel
      que la matrice P m ait tous ses coefficients strictement positifs, alors la suite
      (P n ) est convergente vers une matrice stochastique0ayant ses lignes toutes   1
                                                                  ;
                                                                0 81     ;
                                                                        0 05  0; 14
      égales à une même ligne. Dans l’exercice F.8, P 2 = @ 0; 88        ;
                                                                        0 04  0; 08 A
                                                                  ;
                                                                0 4     0; 35 0; 25
      et la généralisation s’applique.
  iii. La probabilité que l’individu soit malade au bout d’un certain temps est donc
       voisine de 0,094. On peut donc estimer à 9,4% la proportion d’individus
       malades dans la population.


   F.9 Notons E (respectivement A) l’événement «le réverbère est éteint (respec-
tivement allumé».
– Simulation de la situation (effectuée à l’aide d’un tableur ou d’une calculatrice)
  pour une population de 500 réverbères sur une durée de 6 jours :

                                   jour 0 jour 1     jour 2 jour 3 jour 4 jour 5 jour 6
 Nombre de réverbères éteints        500    121        295    232    266    226    255
 Nombre de réverbère allumés            0   379        205    268    234    274    245
  On constate une stabilisation assez rapide vers la situation où un réverbère sur

                                                                                     40
~~~

## Page 42

~~~text
    deux est allumé..
–




    La probabilité que le réverbère soit éteint le deuxième jour est :

                                     3
                                     4
                                        3
                                         4
                                           + 
                                            1
                                            4
                                               1
                                               4
                                                 =
                                                   5
                                                   8
                                     3
    et celle qu’il soit allumé est       :
                                     8
– Le graphe probabiliste de la situation est :




    et la matrice de transition associée à ce graphe, en classant les sommets dans
    l’ordre E,A est :
                                             0           1
                                                 1   3

                                         P =B 4
                                            @ 3      4 C
                                                     1 A
                                                 4   4
    nous sommes dans la situation décrite dans le théorème D.7.7 (deuxième dé-
                                     3
    monstration) avec p = q = . La suite des états probabilistes converge alors vers
                                  4
                q       p       1 1
    l’état (      ;    ) = ( ; ), résultat cohérent avec les simulations effectué es
               p+q p+q      2 2
    en première question.

   F.10 Construisons un graphe dont les sommets sont les 6 personnes, deux som-
mets sont reliés par une arête en trait plein lorsque les personnes correspondantes
se connaissent et en trait discontinu dans le cas contraire. Il s’agit de prouver que
ce graphe contient un cycle simple de longueur 3 dont les arêtes sont de même na-
ture. Si l’on ne tient pas compte de la nature des arêtes, ce graphe est complet, deux
personnes au hasard, ou bien se connaissent ou bien ne se connaissent pas. Chaque
sommet est donc de degré 5 et parmi les 5 arêtes issues d’un sommet, trois d’entre
elles sont de même nature. Supposons, par exemple, que les arêtes fa; bg; fa; cg et
fa; dg soient en trait plein. Considérons alors le cycle b; c; d: Si ses arêtes sont en
trait discontinu, c’est terminé, sinon, l’une des trois arêtes sera en trait plein et per-

                                                                                       41
~~~

## Page 43

~~~text
mettra de former avec deux arêtes du triangle abd un cycle dont les trois arêtes sont
en trait plein.




                                                                                  42
~~~

## Page 44

~~~text
H     Complément : les arbres

    H.1     Définition
    Un arbre est un graphe simple connexe ne possédant pas de cycle simple.
    Exemple




    H.2     Arbre de recouvrement

    1. Définition
       Soit G = (X; A) un graphe simple. Un arbre de recouvrement de G est un
       sous-graphe de G qui est un arbre contenant chaque sommet de G:
    2. Algorithme de construction d’un arbre de recouvrement
       On choisit un sommet arbitraire du graphe, puis on construit à partir de ce som-
       met une chaîne simple en ajoutant des arêtes de G tant que c’est possible. Si la
       chaîne ainsi construit contient tous les sommets du graphe, la chaîne est un arbre
       de recouvrement. Sinon, on retourne à l’avant-dernier sommet de la chaîne et
       à partir de celui-ci, et si c’est possible, on construit une nouvelle chaîne sim-
       ple aussi longue que possible et ne contenant aucun sommet du premier chemin
       construit. Si ce n’est pas possible, il faut remonter à l’antépénultième sommet
       et recommencer. Si le graphe est connexe, on peut réitèrer ce processus jusqu’à
       épuisement des sommets pour obtenir un arbre de recouvrement.
       Exemple
       Appliquons l’algorithme précédent pour trouver un arbre de recouvrement du




                                                                                      43
~~~

## Page 45

~~~text
   graphe connexe suivant :




  – Partons par exemple du sommet a
  – 1re étape : on construit la chaîne simple a; b; c; d; g; h; i; j; k; l; f
  – 2e étape : on remonte jusqu’au sommet g pour former la chaîne g; e
  – Un arbre de recouvrement est alors :




H.3     Arbre partiel de coût minimum

1. Exemple introductif
   On considère le réseau routier représenté par le graphe ci-dessous. Ces routes
   sont souvent enneigées en hiver et l’équipement décide de déneiger un nombre
   minimal de routes de telle sorte que deux villages quelconques du réseau soient
   toujours reliés par une route déneigée.




                                                                                44
~~~

## Page 46

~~~text
  Le problème consiste à construire un graphe partiel, connexe, comprenant un
  nombre minimal d’arêtes. Le graphe contient 6 sommets, le sous-graphe cherché
  doit donc contenir 5 arêtes. Il s’agit donc de construire un arbre de recouvrement
  du graphe (On peut montrer que la relation jAj = jX j 1 caractérise les arbres
  parmi les graphes simples connexes).




  Voici un algorithme de recherche d’arbre partiel de coût minimum lorsque le
  graphe est simple, connexe et valué.
2. Algorithme de Sollin-Calestagne

       G = (X; A; ) est un graphe simple connexe valué.
  – (1) a1 = fx1; y1g est une arête de coût minimum. On pose S = fx1 ; y1g et
    T = fa1 g: Passer à (2)
  – (2) Si S = X; alors l’arbre (S; T ) est l’arbre cherché, sinon, passer en (3)
  – (3) On choisit une arête a = fx; y g de coût minimum ayant un sommet dans S
    et l’autre dans le complémentaire de S dans X: On remplace S par S [ fx; y g
    et T par T [ fag: Passer en (2).

    Exemple
    Utiliser l’algorithme de Sollin-Calestagne pour concevoir un réseau de com-
    munication à coût minimal reliant tous les ordinateurs représentés par le graphe
    suivant :




                                                                                    45
~~~

## Page 47

~~~text
Solution possible (le coût minimal est égal à 4700 euros)




                                                            46
~~~
