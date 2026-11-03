# Cours 2 - Cluster - Slides.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1wwR1u1SqogXlLohteeQxwrwhWvLJzZz6) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                                      Datamining 1 : Clustering




                                  Clustering
Le clustering est la technique non supervisée la plus répandue en datamining.
Elle permet de distinguer des groupes homogènes (classes, segments, clusters) au sein d’un
grand volume de données.
    - De part leur constitution, ces groupes peuvent apporter une information pertinente
    sur les données, notamment s’ils sont représentés graphiquement à l’aide d’une ACP.
    - Ils peuvent aussi servir à découper une étude en sous-parties, chacune pouvant
    bénéficier de traitements particuliers.



Méthodes de clustering :
    • Généralités
    • K-means
    • Classification hiérarchique ascendante
~~~

## Page 2

~~~text
                                                                                              Datamining 1 : Clustering


                                                        Généralités

                                         L’objectif des méthodes est
                                          à la fois, de regrouper les observations ayant des
                                         caractéristiques similaires au sein d’une même classe,
                                                 distance entre observations
                                          à la fois de construire des classes les plus dissemblables
                                         possibles.
                                                 distance entre classes




Recherche exhaustive impossible
Notons que le nombres de partitions distinctes de n objets est
                                                   1 kn
                                                    
                                                   e k1 k!
Par exemple pour 30 objets, on a plus 1023 partitions possibles.

 Algorithme de recherche performant
                                                                                                                     2
~~~

## Page 3

~~~text
                                                                                                          Datamining 1 : Clustering


                               Les métriques sur les observations :
                                     variables quantitatives
Pour trouver des similarités entre les observations il faut définir une métrique
sur les observations :
                                                                    1/2

 Distance euclidienne : d2 (x , y)   (x i  yi )2 
                                       d                                                             1

                                       i1            

                                                    d
 Distance Manhattan : d1 (x , y)   x i  yi
                                                    i1
                                                                                                -1                   1
Atténue l’impact des individus hors norme car pas d’écart au carré


 Distance infinie : d (x , y)  maxx1  y1 ,..., x d  y d 
                                                                                                     -1

 Distance de Mahalanobis : d(x , y)  (x  y)T  1 (x  y)1 / 2
 =matrice carrée définie positive (permet d’introduire une corrélation entre les variables )




                                                                                                                                 3
~~~

## Page 4

~~~text
                                                                                                                                     Datamining 1 : Clustering


                                             Les métriques sur les classes
 Pour construire des classes dissemblables il faut définir une métrique
 sur les classes, c’est-à-dire une distance entre deux ensembles de                                                            C1
 points
                                                                                                                                          C2
 Distance minimale entre deux observations des deux classes :
                            dmin (C1 ,C2 )  min d(x , y)
                                              xC1 ,yC2

détecte les formes allongées voire sinueuses, sensible à l’effet de de                                                    g1
chaîne (2 points éloignés sont considérés comme appartenant à la même classe car reliés par une série
de points proches les uns des autres)                                                                                                    g2
 Distance maximale entre deux observations des deux classes :
                              dmax (C1 ,C2 )  max d(x , y)
                                                xC1 ,yC2

très sensible aux observations atypiques

 Distance moyenne entre deux observations des deux classes :
                                        dmoy (C1 ,C2 )  moyenne d(x , y)
                                                             xC1 ,yC2
moins sensible au bruit, tend à produire des classes de même variance.

  Distance de Ward :
                                                               n1  n2                           où ni et gi sont l’effectif et le
                                          dWard (C1 ,C2 )             d(g1 ,g2 )                centre de gravité de la classe Ci
                                                               n1  n2
 la plus utilisée, permet de fusionner les deux classes faisant le moins baisser l’inertie inter-classes,
 tend à produire des classes sphériques de même effectif .                   4                                                                              4
~~~

## Page 5

~~~text
                                                                                                                    Datamining 1 : Clustering


                                            Inertie inter et intra classes
                                                                                             Centre de gravité
                                                                                              d’une classe Ck
                                                                                                          1
              Centre de gravité
                                                        Ça ne vous
                                                                                               gk            
                                                                                                          nk xiCk
                                                                                                                   xi
                 du nuage                             rappelle rien?
                    1 n
                 g   xi
                    n i1


                            Inertie Totale       =          Inertie intra classes + Inertie inter classes
                              1 n 2                           1 p nk 2                   1 p
d=distance
euclidienne                   n
                                  d (x i ,g)
                                                  =           n
                                                                      d (x i  gk ) 
                                                                                         n
                                                                                              nkd2 (gk ,g)
                              i
                                 1
                                                           k1 i1
                                                                                    k1
                                                                                                    
                                    Itot                               Iintra                   Iint er

         Chercher la partition qui minimise l’inertie intra classes (homogénéité des observations dans les classes)
         Chercher la partition qui maximise l’inertie inter classes (dissimilarité des classes entre elles)
        Le coefficient                                  I
                                                 R2  inter
                                                         Itot
        est le pourcentage d’inertie du nuage expliquée par les classes. L’objectif est d’obtenir un R²
        proche de 1 avec un minimum de classes (si nb classes =n alors R²=1)
        Il peut servir pour
        • Comparer deux partitionnements ayant le même nombre de classes
        • Sélectionner le nombre de classes (courbe R² vs nb classes. on choisit le dernier
                                                                                     5      saut important du R²)                          5
~~~

## Page 6

~~~text
                                                                          Datamining 1 : Clustering


                           Algorithme des k-means (1/2)

Soit C le nombre de classes souhaitées.


                 Algorithme
Etape 1 : Choisir C individus au hasard
          comme centres initiaux des
          classes
Etape 2 : On calcule les distances entre
          chaque individu et chaque centre
          de classe, et on affecte                         Etape 1   Etape 2
          l’individu à la classe la plus
          proche
Etape 3 : On remplace les centres des
          classes par les C barycentres
          des classes définies à l’étape 2
Etape 4 : On itère à partir de l’étape 2
          jusqu’à convergence
                                                           Etape 4   Etape 3


                                            Basé sur la
                                          distance entre
                                             individus
                                                                 6
                                                                                                 6
~~~

## Page 7

~~~text
                                                                                                Datamining 1 : Clustering


                           Algorithme des k-means (2/2)


Caractéristiques
 Dépend de l’initialisation des centres  répéter plusieurs fois l’algorithme
 Nombre C de classes fixé à l’avance  tester plusieurs valeurs de C
 Un individu atypique est détecté car il forme une classe à lui tout seul (en général)
 Complexité linéaire  adapté à de grands volumes de données
 (attention toutefois car il faut tester plusieurs nombres de classes et répéter l’algorithme
  plusieurs fois pour chaque classe)




                                                                                                                       7
~~~

## Page 8

~~~text
                                                                       Datamining 1 : Clustering


                  Classification hiérarchique ascendante
                                    (1/2)
                 Algorithme
Etape 1 : Chaque individu forme une classe
          (n classes)
Etape 2 : On calcule les distances entre
          les classes et on regroupe les                Basé sur la
          deux classes les plus proches               distance entre
          (C classes  C-1 classes)                       classes
Etape 3 : On itère à partir de l’étape 2
          jusqu’à n’avoir qu’une seule
          classe
Etape 4 : Choix du partitionnement à
          partir de dendrogramme



Le dendrogramme représente la suite de
partitions obtenues au cours de l’algorithme.
L’axe des ordonnées représente une mesure de
dissimilarité/inertie inter-classes (R² partiel,…).

On coupe le dendrogramme où la hauteur des
branches est élevée. Cela permet d’obtenir
simultanément :
• Le nombre de classes
• La constitution des classes                            8
                                                                                              8
~~~

## Page 9

~~~text
                                                                                   Datamining 1 : Clustering


                   Classification hiérarchique ascendante
                                     (2/2)

Caractéristiques
 Regroupe des individus ou des variables dès qu’il y a une notion de distance
 Pas de dépendance à l’initialisation
 Nombre de classes non fixé à l’avance
 formes diverses des groupes grâce au choix de la distance
 A chaque étape le partitionnement dépend de celui obtenu avant  Optimum local
 Complexité exponentielle de l’algorithmique




                                                                                                          9
~~~

## Page 10

~~~text
                                                                                              Datamining 1 : Clustering


                                                                    Conclusion
        Méthodes non hiérarchiques
             Il faut avoir une idée a priori du nombre de classes
             L’initialisation de l’algorithme peut avoir un impact sur la partition finale
             L’algorithme converge assez vite (complexité linéaire)
        Algorithme hiérarchique
              La complexité de l’algorithme est exponentielle
              On n’a pas besoin de connaitre à l’avance le nombre de classes
        Quand cela est possible confirmer les résultats par plusieurs méthodes


                                  Avez-vous des questions?

Documents ayant servis à la rédaction des slides et TD :
     • DataMining et Statistiques décisionnelles, Stéphane Tufféry, Ed. Technip
     • https://penseeartificielle.fr/choisir-distance-machine-learning/
     • http://eric.univ-lyon2.fr/~ricco/cours/slides/classif_centres_mobiles.pdf
     • https://scikit-learn.org/stable/index.html




                                                                                                                    10
~~~
