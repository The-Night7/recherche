# TheoGraphes_5bis.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1l_LIwmmsLrprb22SGoipKeM-UnY9qHnQ) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Théorie des graphes

Maria Malek, Romain Dujol

      CY Tech – ING1-MA




   Maria Malek, Romain Dujol   1
~~~

## Page 2

~~~text
Graphes orientés : chemins optimaux




  Recherche de chemin optimal




                   Maria Malek, Romain Dujol   132
~~~

## Page 3

~~~text
Recherche de chemin optimal




  Recherche de chemin optimal
    Définition
    Problème à source unique
    Problème à sources multiples




                    Maria Malek, Romain Dujol   133
~~~

## Page 4

~~~text
Chemin optimal dans un graphe orienté valué
  Définition (Valeur d’un chemin C de G = (V, A, w))
  Valeur de C : w(C) = ∑ w(a)
                         a∈C

  Définition (Chemin optimal de s à t)
  Chemin reliant s à t dont la valeur est minimale parmi tous
  les chemins reliant s à t

  Définition (Circuit absorbant de G = (V, A, w))
  Circuit de valeur négative

  Théorème (Condition d’existence de chemin
  optimal)
  Soit G = (V, A, w) un graphe orienté valué et (s, t) ∈ V 2 . Si :
   I ∃ chemin reliant s à t
   I
       ∀C chemin reliant s à t, C n’admet aucun circuit absorbant
  alors il existe un chemin optimal de s à t
                        Maria Malek, Romain Dujol                     134
~~~

## Page 5

~~~text
Chemin optimal dans un graphe orienté valué


  Lien avec l’optimisation linéaire                    (
                                                        w(vi vj ) si vi vj ∈ A
  On note V = {v1 , v2 , . . . , vn }, ainsi que wij =                         .
                                                        0         sinon
  xij : appartenance (ou non) de vi vj au chemin optimal de v1 à
  vn                n n
               
               
               
               min ∑ ∑ wij xij
               
               
                   i=1 i=1
               
                                                
               
                                  n          n   1
                                                        si i = 1
          =⇒
               
                   ∀i ∈ J1, nK , ∑ xki − ∑ xik = 0      si i ∈ J2, n − 1K
                                                
                                  k=1    k=1
                                                  −1
               
                                                         si i = n
               
                                                
               
               
               
                    ∀(i, j) ∈ J1, nK2 , xij ∈ {0, 1}
               




                            Maria Malek, Romain Dujol                         135
~~~

## Page 6

~~~text
Chemin optimal dans un graphe orienté valué


  Lors de la recherche d’un chemin optimal de s à t. . .
  . . . on trouve également tous les chemins optimaux de s aux
  sommets intermédiaires
  ⇒ Recherche de chemins optimaux à « source unique »

  Deux types de problématiques
  Recherche de chemins optimaux à « source unique » v0
             Chemins optimaux de v0 à v pour tout v ∈ V
             =⇒ Algorithmes de Dijkstra, de Bellman-Ford
  Recherche de chemins optimaux à « sources multiples »
             Chemins optimaux de v1 à v2 pour tout
             (v1 , v2 ) ∈ V 2
             =⇒ Algorithme de Floyd-Warshall




                      Maria Malek, Romain Dujol              136
~~~

## Page 7

~~~text
Recherche de chemin optimal à source unique
v0
  Propriété (Structure de l’ensemble des chemins
  optimaux)
  Arborescence couvrante de racine v0

  Première solution : recherche exhaustive
   I Recenser tous les chemins depuis v0
   I Calculer leurs valeurs et trouver ceux de valeur minimale
  =⇒ Complexité exponentielle
  =⇒ Beaucoup trop coûteux, donc inutilisable

  Deuxième solution : algorithme glouton
   I Initialisation : tous les sommets sont à distance infinie de
     v0
   I Tant qu’il reste des sommets non visités,
       I visiter un sommet non visité de distance minimale ;
       I mettre à jour les distances de ses successeurs.
  =⇒ Algorithmes de Dijkstra, Bellman-Ford
                      Maria Malek, Romain Dujol                137
~~~

## Page 8

~~~text
Recherche de chemin optimal à source unique
v0


  Algorithmes
  Dijkstra (1959)
              Algorithme le plus adapté aux valuations
              positives
              Non-adapté à l’existence de circuit absorbant
              Peu adapté aux graphes de grande taille
  Bellman-Ford (1956)
            Algorithme adapté aux valuations quelconques
            Adapté à l’existence de circuit absorbant
            (détection)




                     Maria Malek, Romain Dujol                138
~~~

## Page 9

~~~text
Algorithme de Dijkstra

  Calcul de l’arborescence des chemins optimaux
    préconditions : G = (V, A, w) graphe orienté valué et v0 ∈ V
    postconditions : G(B) est l’arborescence des chemins optimaux depuis v0
    postconditions : ∀v ∈ V, d[v] est la valeur du chemin optimal de v0 à v
   d : Tableau associatif de<Sommet> de réel
   pour v ∈ V\{v0 } faire
       d[v] ← +∞
   fin pour
   d[v0 ] ← 0
   Vc ← ∅
   B←∅
   tant que V c 6= V faire
       s est choisi dans argmin{d[v], v ∈    / V c}
       V c ← V c ∪ {s}
       pour v ∈ / V c successeur de s faire
          si d[v] > d[s] + w(sv) alors
             B ← B\{v 0 v, v 0 v ∈ B} ∪ {sv}
             d(v) ← d(s) + w(sv)
          fin si
       fin pour
   fin tant que


                         Maria Malek, Romain Dujol                      139
~~~

## Page 10

~~~text
Algorithme de Dijkstra




  Propriété (Convergence sur G = (V, A, w))
  Si w ≥ 0 et G n’admet aucun circuit absorbant, alors
  l’algorithme de Dijkstra converge pour tout v0 ∈ V.
  Sa complexité est O card E + (card V) · log(card V) .



  Recherche du chemin optimal de v0 à v ∗
  Possibilité d’anticiper la terminaison en s’arrêtant dès que
  v∗ ∈ V c




                      Maria Malek, Romain Dujol                  140
~~~

## Page 11

~~~text
Algorithme de Dijkstra
  Initialisation
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy           0
                           119
                                                                            Orléans             ∞
              Tours                 273
                                                                            Tours               ∞
               108                                                          Poitiers            ∞
   Poitiers
                     118
                                 Limoges
                                                                            Limoges             ∞
                                                                            Angoulême           ∞
          120              107                    96
                                                                            Brive-la-G.         ∞
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux            ∞
          135              147                             246              Langon          ∞
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban           ∞
                                                         89
                                                                            Auch                ∞
                                                                            CY Tech Pau         ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol                 141
~~~

## Page 12

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {CY Tech Cergy}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy             0
                           119
                                                                            Orléans                 150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours               ∞
               108                                                          Poitiers            ∞
   Poitiers
                     118
                                 Limoges
                                                                            Limoges             ∞
                                                                            Angoulême           ∞
          120              107                    96
                                                                            Brive-la-G.         ∞
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux            ∞
          135              147                             246              Langon          ∞
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban           ∞
                                                         89
                                                                            Auch                ∞
                                                                            CY Tech Pau         ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol                   141
~~~

## Page 13

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Orléans}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy           0
                           119
                                                                            Orléans               150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours                 269   (Orléans)
               108                                                          Poitiers            ∞
   Poitiers
                     118
                                 Limoges
                                                                            Limoges               423   (Orléans)
                                                                            Angoulême           ∞
          120              107                    96
                                                                            Brive-la-G.         ∞
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux            ∞
          135              147                             246              Langon          ∞
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban           ∞
                                                         89
                                                                            Auch                ∞
                                                                            CY Tech Pau         ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol                 141
~~~

## Page 14

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Tours}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy         0
                           119
                                                                            Orléans             150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours               269   (Orléans)
               108                                                          Poitiers            377   (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges             423   (Orléans)
                                                                            Angoulême           ∞
          120              107                    96
                                                                            Brive-la-G.         ∞
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux            ∞
          135              147                             246              Langon          ∞
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban           ∞
                                                         89
                                                                            Auch                ∞
                                                                            CY Tech Pau         ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol               141
~~~

## Page 15

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Poitiers}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy           0
                           119
                                                                            Orléans               150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours                269    (Orléans)
               108                                                          Poitiers              377   (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges              423    (Orléans)
                                                                            Angoulême            497    (Poitiers)
          120              107                    96
                                                                            Brive-la-G.         ∞
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux            ∞
          135              147                             246              Langon          ∞
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban           ∞
                                                         89
                                                                            Auch                ∞
                                                                            CY Tech Pau         ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol                 141
~~~

## Page 16

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Limoges}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy         0
                           119
                                                                            Orléans             150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours               269   (Orléans)
               108                                                          Poitiers            377   (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges             423   (Orléans)
                                                                            Angoulême           497   (Poitiers)
          120              107                    96
                                                                            Brive-la-G.         519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux          ∞
          135              147                             246              Langon          646       (Limoges)
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban         ∞
                                                         89
                                                                            Auch              ∞
                                                                            CY Tech Pau       ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol               141
~~~

## Page 17

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Angoulême}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy       0
                           119
                                                                            Orléans           150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours             269   (Orléans)
               108                                                          Poitiers          377   (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges           423   (Orléans)
                                                                            Angoulême         497   (Poitiers)
          120              107                    96
                                                                            Brive-la-G.       519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux          632   (Angoulême)
          135              147                             246              Langon           644               (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban       ∞
                                                         89
                                                                            Auch            ∞
                                                                            CY Tech Pau     ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol             141
~~~

## Page 18

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Brive-la-Gaillarde}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy       0
                           119
                                                                            Orléans           150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours             269   (Orléans)
               108                                                          Poitiers          377   (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges           423   (Orléans)
                                                                            Angoulême         497   (Poitiers)
          120              107                    96
                                                                            Brive-la-G.       519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux          632   (Angoulême)
          135              147                             246              Langon           644               (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban         765   (Brive-la-G.)
                                                         89
                                                                            Auch            ∞
                                                                            CY Tech Pau     ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol             141
~~~

## Page 19

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Bordeaux}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy       0
                           119
                                                                            Orléans           150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours             269   (Orléans)
               108                                                          Poitiers          377   (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges           423   (Orléans)
                                                                            Angoulême         497   (Poitiers)
          120              107                    96
                                                                            Brive-la-G.       519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux          632   (Angoulême)
          135              147                             246              Langon           644               (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban         765   (Brive-la-G.)
                                                         89
                                                                            Auch            ∞
                                                                            CY Tech Pau     ∞
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol             141
~~~

## Page 20

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Langon}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy        0
                           119
                                                                            Orléans           150    (CY Tech Cergy)
              Tours                 273
                                                                            Tours             269    (Orléans)
               108                                                          Poitiers          377    (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges           423    (Orléans)
                                                                            Angoulême         497    (Poitiers)
          120              107                    96
                                                                            Brive-la-G.        519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux          632    (Angoulême)
          135              147                             246              Langon           644                (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban         765    (Brive-la-G.)
                                                         89
                                                                            Auch            ∞
                                                                            CY Tech Pau       794    (Langon)
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol              141
~~~

## Page 21

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Montauban}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy      0
                           119
                                                                            Orléans          150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours           269    (Orléans)
               108                                                          Poitiers        377    (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges         423    (Orléans)
                                                                            Angoulême       497    (Poitiers)
          120              107                    96
                                                                            Brive-la-G.      519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux        632    (Angoulême)
          135              147                             246              Langon          644               (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban       765    (Brive-la-G.)
                                                         89
                                                                            Auch            854    (Montauban)
                                                                            CY Tech Pau     794    (Langon)
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol            141
~~~

## Page 22

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {CY Tech Pau}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy      0
                           119
                                                                            Orléans          150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours           269    (Orléans)
               108                                                          Poitiers        377    (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges         423    (Orléans)
                                                                            Angoulême       497    (Poitiers)
          120              107                    96
                                                                            Brive-la-G.      519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux        632    (Angoulême)
          135              147                             246              Langon          644               (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban       765    (Brive-la-G.)
                                                         89
                                                                            Auch            854    (Montauban)
                                                                            CY Tech Pau     794    (Langon)
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol            141
~~~

## Page 23

~~~text
Algorithme de Dijkstra
  V c ← V c ∪ {Auch}
                CY Tech Cergy


                             150


                      Orléans
                                                                            CY Tech Cergy      0
                           119
                                                                            Orléans          150   (CY Tech Cergy)
              Tours                 273
                                                                            Tours           269    (Orléans)
               108                                                          Poitiers        377    (Tours)
   Poitiers
                     118
                                 Limoges
                                                                            Limoges         423    (Orléans)
                                                                            Angoulême       497    (Poitiers)
          120              107                    96
                                                                            Brive-la-G.      519   (Limoges)
   Angoulême                         223         Brive-la-Gaillarde
                                                                            Bordeaux        632    (Angoulême)
          135              147                             246              Langon          644               (Angoulêm
   Bordeaux
                      48
                                 Langon           Montauban                 Montauban       765    (Brive-la-G.)
                                                         89
                                                                            Auch            854    (Montauban)
                                                                            CY Tech Pau     794    (Langon)
                                           150      Auch


                                                   107


                                    CY Tech Pau


                                                              Maria Malek, Romain Dujol            141
~~~

## Page 24

~~~text
Algorithme de Dijkstra
  Terminaison
                CY Tech Cergy


                          150


                      Orléans
                                                                         CY Tech Cergy      0
                        119
                                                                         Orléans          150   (CY Tech Cergy)
              Tours               273
                                                                         Tours           269    (Orléans)
               108                                                       Poitiers        377    (Tours)
   Poitiers                    Limoges
                                                                         Limoges         423    (Orléans)
                                                                         Angoulême       497    (Poitiers)
          120                                   96
                                                                         Brive-la-G.      519   (Limoges)
   Angoulême                                   Brive-la-Gaillarde
                                                                         Bordeaux        632    (Angoulême)
          135            147                             246             Langon          644               (Angoulêm
   Bordeaux                    Langon           Montauban                Montauban       765    (Brive-la-G.)
                                                      89
                                                                         Auch            854    (Montauban)
                                                                         CY Tech Pau     794    (Langon)
                                         150      Auch




                                  CY Tech Pau


                                                           Maria Malek, Romain Dujol            141
~~~

## Page 25

~~~text
Recherche de chemin optimal à source
multiples


  Première solution : recherche exhaustive
   I Recenser tous les chemins
   I Calculer leurs valeurs et trouver ceux de valeur minimale
  =⇒ Complexité exponentielle
  =⇒ Beaucoup trop coûteux, donc inutilisable

  Deuxième solution : algorithme glouton
   I Initialisation : matrice d’adjacence
   I Pour chaque sommet, on met à jour les distances des
     chemins passant par ce sommet
  =⇒ Algorithme de Floyd-Warshall




                      Maria Malek, Romain Dujol             142
~~~

## Page 26

~~~text
Algorithme de Floyd-Warshall
  Calcul des distances optimales
    préconditions : M est la matrice d’adjacence de G = (V, A, w)
    postconditions : M contient les distances optimales
   pour k ∈ J1, nK faire
      pour i ∈ J1, nK faire
         pour j ∈ J1, nK faire
            si Mij > Mik + Mkj alors
               Mij ← Mik + Mkj
               si Mii < 0 alors
                  /* Existence de circuit absorbant */
               fin si
            fin si
         fin pour
      fin pour
   fin pour




                       Maria Malek, Romain Dujol                    143
~~~

## Page 27

~~~text
Algorithme de Floyd-Warshall
  Calcul des distances optimales
     préconditions : M est la matrice d’adjacence de G = (V, A, w)
     postconditions : M contient les distances optimales
    pour k ∈ J1, nK faire
       pour i ∈ J1, nK faire
          pour j ∈ J1, nK faire
             si Mij > Mik + Mkj alors
                Mij ← Mik + Mkj
                si Mii < 0 alors
                   /* Existence de circuit absorbant */
                fin si
             fin si
          fin pour
       fin pour
    fin pour

  ... et les chemins ?
  On crée une matrice des prédecesseurs P de G = (V, A, w) :
                     ∀(i, j) ∈ J1, nK2 , Pij = vi si vi vj ∈ A
  Les cases restantes étant indéfinies.

                        Maria Malek, Romain Dujol                    143
~~~

## Page 28

~~~text
Algorithme de Floyd-Warshall
  Calcul des distances optimales
    préconditions : M est la matrice d’adjacence de G = (V, A, w)
    préconditions : P est la matrice des prédecesseurs de G = (V, A, w)
    postconditions : M contient les distances optimales
    postconditions : P contient prédecesseurs optimaux
   pour k ∈ J1, nK faire
      pour i ∈ J1, nK faire
         pour j ∈ J1, nK faire
            si Mij > Mik + Mkj alors
               Mij ← Mik + Mkj
               Pij ← Pkj
               si Mii < 0 alors
                  /* Existence de circuit absorbant */
               fin si
            fin si
         fin pour
      fin pour
   fin pour




                       Maria Malek, Romain Dujol                    143
~~~

## Page 29

~~~text
Algorithme de Floyd-Warshall
  Exemple
                           CY Tech Cergy


                                        150


                                 Orléans


                                      119


                         Tours                 273


                          108

                                118
              Poitiers                      Limoges


                     120              107                    96


              Angoulême                         223         Brive-la-Gaillarde


                     135              147                             246

                                 48
              Bordeaux                      Langon           Montauban


                                                                    89


                                                      150      Auch


                                                              107


                                               CY Tech Pau


               Maria Malek, Romain Dujol                                         144
~~~

## Page 30

~~~text
Algorithme de Floyd-Warshall

  Matrice des distances
  Ordre des sommets : CY Tech Cergy, Orléans, Tours, Poitiers,
  Limoges, Angoulême, Brive-la-Gaillarde, Bordeaux, Langon,
  Montauban, Auch et CY Tech Pau
          C   O     T   P     L    A     B-G   B    La   M   Au   Pa
                                                                     
  C     0     150    ∞  ∞     ∞     ∞    ∞      ∞   ∞  ∞  ∞        ∞
  O ∞
              0    119 ∞    273    ∞    ∞      ∞   ∞  ∞  ∞        ∞ 
  T   ∞
              ∞     0 108    ∞     ∞    ∞      ∞   ∞  ∞  ∞        ∞ 
  P   ∞
              ∞     ∞  0    118   120   ∞      ∞   ∞  ∞  ∞        ∞ 
  L   ∞
              ∞     ∞  ∞     0    107   96     ∞ 223  ∞  ∞        ∞ 
  A   ∞
              ∞     ∞  ∞     ∞     0    ∞     135 147 ∞  ∞        ∞ 
      ∞
  B-G         ∞     ∞  ∞     ∞     ∞    0      ∞   ∞ 246 ∞        ∞ 
  B   ∞
              ∞     ∞  ∞     ∞     ∞    ∞      0  48  ∞  ∞        ∞ 
  La ∞       ∞     ∞  ∞     ∞     ∞    ∞      ∞   0  ∞  ∞       150 
                                                                      
  M  ∞       ∞     ∞  ∞     ∞     ∞    ∞      ∞   ∞  0  89       ∞ 
  Au  ∞       ∞     ∞  ∞     ∞     ∞    ∞      ∞   ∞  ∞  0       107 
  Pa    ∞      ∞     ∞  ∞     ∞     ∞    ∞      ∞   ∞  ∞  ∞       0


                        Maria Malek, Romain Dujol                      145
~~~

## Page 31

~~~text
Algorithme de Floyd-Warshall

  Matrice des distances
  Ordre des sommets : CY Tech Cergy, Orléans, Tours, Poitiers,
  Limoges, Angoulême, Brive-la-Gaillarde, Bordeaux, Langon,
  Montauban, Auch et CY Tech Pau
        C   O      T    P      L      A    B-G    B     La   M    Au    Pa
                                                                           
 C     0    150   269   377 423     497 519      632    644 765   854   794
 O ∞
            0    119   227 273     347 369      482    494 615   704   644 
                                                                            
 T   ∞
            ∞     0    108 226     228 322      363    375 568   657   525 
                                                                            
 P   ∞
            ∞     ∞     0  118     120 214      255    267 460   549   417 
                                                                            
 L   ∞
            ∞     ∞     ∞   0      107 96       242    223 342   431   373 
                                                                            
 A   ∞
            ∞     ∞     ∞   ∞       0   ∞       135    147  ∞     ∞    297 
                                                                            
     ∞
 B-G        ∞     ∞     ∞   ∞       ∞   0        ∞      ∞  246   335   442 
                                                                            
 B   ∞
            ∞     ∞     ∞   ∞       ∞   ∞        0      48  ∞     ∞    198 
                                                                            
 La ∞      ∞     ∞     ∞   ∞       ∞   ∞        ∞      0   ∞     ∞    150 
                                                                            
 M  ∞      ∞     ∞     ∞   ∞       ∞   ∞        ∞      ∞   0     89   196 
                                                                            
 Au  ∞      ∞     ∞     ∞   ∞       ∞   ∞        ∞      ∞   ∞     0    107 
 Pa    ∞     ∞     ∞     ∞   ∞       ∞   ∞        ∞      ∞   ∞     ∞     0


                            Maria Malek, Romain Dujol                    145
~~~

## Page 32

~~~text
Algorithme de Floyd-Warshall

  Matrice des prédecesseurs
              C   O   T    P   L   A   B-G   B   La   M     Au   Pa
                                                                     
      C           C
      O 
                     O        O                                    
                                                                    
      T   
                          T                                        
                                                                    
      P   
                              P   P                                
                                                                    
      L   
                                  L    L        L                  
                                                                    
      A   
                                            A   A                  
                                                                    
      B-G 
                                                     B-G           
                                                                    
      B   
                                                B                  
                                                                    
      La                                                       La 
                                                                    
      M                                                   M       
                                                                    
      Au                                                        Au 
      Pa




                          Maria Malek, Romain Dujol                       146
~~~

## Page 33

~~~text
Algorithme de Floyd-Warshall

  Matrice des prédecesseurs
              C   O   T    P   L   A   B-G   B   La   M     Au   Pa
                                                                   
      C           C   O    T   O P      L    A   A    B-G   M    La
      O 
                     O    T   O P      L    A   A    B-G   M    La 
                                                                    
      T   
                          T   P P      L    A   A    B-G   M    La 
                                                                    
      P   
                              P P      L    A   A    B-G   M    La 
                                                                    
      L   
                                L      L    A   L    B-G   M    La 
                                                                    
      A   
                                            A   A               La 
                                                                    
      B-G 
                                                     B-G   M    Au 
                                                                    
      B   
                                                B               La 
                                                                    
      La                                                       La 
                                                                    
      M                                                   M    Au 
                                                                    
      Au                                                        Au 
      Pa




                          Maria Malek, Romain Dujol                     146
~~~

## Page 34

~~~text
Algorithme de Floyd-Warshall

  Matrice des prédecesseurs
               C   O   T    P   L   A   B-G   B   La   M     Au   Pa
                                                                    
       C           C   O    T   O P      L    A   A    B-G   M    La
       O 
                      O    T   O P      L    A   A    B-G   M    La 
                                                                     
       T   
                           T   P P      L    A   A    B-G   M    La 
                                                                     
       P   
                               P P      L    A   A    B-G   M    La 
                                                                     
       L   
                                 L      L    A   L    B-G   M    La 
                                                                     
       A   
                                             A   A               La 
                                                                     
       B-G 
                                                      B-G   M    Au 
                                                                     
       B   
                                                 B               La 
                                                                     
       La                                                       La 
                                                                     
       M                                                   M    Au 
                                                                     
       Au                                                        Au 
       Pa

  Lecture des chemins optimaux
   I Orléans → Angoulème : A ← P ← T ← O (valeur : 347)
   I Cergy@Pau : Pa ← La ← A ← P ← T ← O ← C (valeur : 794)

                           Maria Malek, Romain Dujol                     146
~~~
