# CM1-Analyse-Univariee_Data-Exploration.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Y4PhSYg2xCKzrk38v34oPMWO0XA9hY9W) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                      Data exploration
         30h TD/TP
         Évaluation (1ère et 2nde session) : Examen 2h sur machine / Etude préalable d’un ou plusieurs jeux de données
         Supports pédagogiques : Support de présentation et énoncé de TD/TP à chaque séance
                                 Tutoriel sur l’ensemble du programme

         L’objectif de ce module est d’introduire les méthodes permettant d’extraire de l’information
         pertinente de corpus de données.
         A l’issue de cette formation, vous serez capables de :
         • faire apparaitre des comportements particuliers des objets observés (détecter les
           individus ayant un comportement atypique, trouver des ensemble d’individus ayant un
           comportement similaire),
         • trouver des liens entre les variables étudiées (ex: est-ce que le PIB d’un pays est lié à
           l’investissement en R&D, est-ce qu’un médicament a un impact sur le taux de guérison?),
         • utiliser le langage dédié aux statistiques R (pas programmer mais utiliser).

         Seules les méthodes descriptives seront abordées dans ce module. Il se complète avec les
         modules de 2ème année : IA (modèles de prévision/machine learning) et statistiques (gestion
         de l’incertitude)


CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 2

~~~text
                                                             Corpus/jeu de données
                                      Un jeu de données est un tableau avec
                                          –     en ligne les individus/instances observés (unité statistique)
                                          –     en colonne les variables/attributs étudiées
     Sur l’exemple ci-dessous les individus sont les incidents survenus dans la ville de Chicago depuis 2001 et les variables sont la date, le type
     d’incident, la position géographique, etc…




     Pour tirer de l’information pertinente et compréhensible par tout le monde à partir de ce genre de tableau
     il faut produite :

            –       une présentation la plus synthétique possible
            –       une représentation graphique appropriée
            –       un résumé numérique




                                                                                                                                                      2
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 3

~~~text
                                                  Population et échantillon

            –        Population : Ensemble des individus
            –        Echantillon : Sous-ensemble de la population



                                  Individus                                         Echantillon



                                                                                     Population




                –      Recensement : Etude de tous les individus d’une population
                –      Sondage : Etude d’une partie de la population

                Remarque : la population peut être infinie et le recensement impossible.

                Les statistiques inférentielles (ING2) permettent d’extrapoler des résultats observés sur un
                échantillon à toute une population.

                                                                                                               3
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 4

~~~text
                                                      Analyse exploratoire et
                                                      statistique inférentielle
                    Analyse exploratoire:
                –        Présentation synthétique des données (tableau de contingence,…)
                –        Description à travers des résumés chiffrés : moyennes, médianes, écarts-types,
                         corrélations, …
                –        Description à travers des résumés graphiques : histogrammes, diagrammes en bâton ou
                         circulaire, …
                –        Recherche de sous-groupes homogènes (clustering)
                    Statistique inférentielle :
                –        Trouver des estimateurs non biaisés et efficients pour passer de l'échantillon à la
                         population.
                –        L'outil mathématique sous jacent est la théorie des probabilités



                                                 Echantillonnage                                  Analyse
                                Population          aléatoire             Echantillon           exploratoire   Caractéristiques


                                                                   Statistiques inférentielle
                                                                                                                                  4
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 5

~~~text
                                                    Nature des variables

                 Chaque individu est décrit par un ensemble de caractéristiques appelées
                 variables (ou attributs)

                 Les variables sont classées suivant leur nature :

                                                 Discrètes : nombre d’enfants, nombre de
             Quantitatives                       pièces défectueuses,…
                                                                                                   Passage du quantitatif
          (Echelle numérique)
                                                                                                   au qualitative ordinal
                                                 Continues : Taille, température,…                  (regroupement par
                                                                                                        intervalle)


                                                 Ordinales : Mentions au bac, catégories de         Perte d’information
              Qualitatives                       résistance (fort, moyen, faible)
               (modalités)

                                                 Nominales : couleurs, catégories socio-
                                                 professionnelles,…
                                                 Dichotomiques : présence/absence d’un caractère

                                                                                                                          5
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 6

~~~text
       Vu au lycée                                   Différents types d’analyse

                     Les statistiques univariées : On ne s'intéresse qu'à une seule variable.
                     Ex : Les salaires en Europe, nombre d'enfants par ménage, Temps de visite sur un site, Etude de l'âge des
                     habitants d'un pays par classe d'âge.

                     Les statistiques bivariées : On s'intéresse à l'étude simultanée de deux variables pour
                     mesurer leur dépendance.
                     Ex : le vote est-il différent d'une CSP à l'autre ?

                     Les statistiques multivariées : On s'intéresse à l'étude simultanée de p variables.
                     Même problématique que pour le bidimensionnel mais avec p assez grand.
                     Ex : Etude du bien-être par département à travers de critères géo-socio-économiques (ensoleillement,
                     nombre de théâtres, taux de suicides, infrastructure routière, …)



                                       A chaque type de variable (qualitatif nominal,
                                      quantitatif continu,…) correspond un traitement
                                                         spécifique.


                                                                                                                                 6
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 7

~~~text
                                                 Méthodologie d'étude statistique
            Etape 1 : Définir précisément le problème étudié :
                   1) Quels sont les objectifs de l'étude ?
                                 recensement des différentes questions posées
                                 déduction des différentes études statistiques à opérer
                                 définition des variables étudiées avec leur type

                   2) Quelle est la population étudiée ?
                                 définition précise de l'unité statistique
                                 définition du périmètre spatio-temporel

                   3) Comment récupérer et stocker l'information?
                                Enquête ou données existantes ou un mixte
                                Choix de la technique d'échantillonnage
                                Récupération des données et validation des données récupérées

            Etape 2 : Exécution des études statistiques avec les logiciels appropriés

            Etape 3 : Rédaction du document de synthèse
                   1)      Rappel du contexte : objectifs de l'étude, périmètre de l'étude, définitions des études statistiques
                   2)      Insertion par étude des résumés chiffrés et graphiques
                   3)      Interprétation des résultats en cohérence avec le périmètre et les résumés



                                                                                                                                  7
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 8

~~~text
                                                 Analyse univariée
                                                    (Rappels et compléments)




                                                                               8
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 9

~~~text
                                                      Représentation synthétique
                                                  Une présentation synthétique des données
                                                  commence par un tableau de contingence.

         Effectif : Pour chaque variable, il s’agit de compter le nombre d’individus ayant la même
                    valeur/modalité xi. On utilisera le terme effectif de la valeur/modalité i. On notera
                    cet effectif ni.
                                    Taux de                 Zone Euro      Zone Euro (avant 2010)          Taux de chômage
                      Pays         chômage         PIB     (avant 2010)   Pas Euro              7     [4,4;9,6[             9
                   Allemagne          5,5        37430,1    Zone Euro     Zone Euro            13     [9,6;14,8[            7
                    Autriche          4,4        40064,8    Zone Euro     Total                20     [14,8;19,9[           1
                    Belgique          7,6        37727,8    Zone Euro                                 [19,9;25,1[           2
                   Danemark           7,5        40189,9     Pas Euro                                 Total                20
                       …               …            …           …               N.B. Le tableau de contingence des variables continues
                                                                                nécessite une regroupement des valeurs (cf. histogramme)



         Fréquence : Quand on aura besoin de ramener les effectifs en pourcentage. On parlera alors
                     de fréquences. On notera cette fréquence fi,
                                                                               Zone Euro (avant 2010)
                                                  fi = n i / n                Pas Euro            35%
                     où n est l'effectif total.                               Zone Euro           65%
                     La fréquence permet de comparer des échantillons         Total              100%

                     de tailles différentes
                                                                                                                                           9
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 10

~~~text
                                                        Variables quantitatives :
                                                       Représentation graphique
      Représentation graphique d’une variable discrète                                 Pointures de chaussures
                                                                              12
               Diagramme en bâtons                                            10

                     • bâton par valeur discrète                               8
                                                                               6

                     • hauteur du bâton proportionnelle                        4
                                                                               2
                     à l’effectif de la valeur                                 0
                                                                                   35 36 37 38 39 40 41 42 43 44 45 46


       0,035
                                          Taille
        0,03                                            Représentation graphique d’une variable continue
       0,025                                                             Histogramme
        0,02                                            • regroupement des valeurs par intervalle (classe)
                                                        • nombre de classes ≈ E[1+10×log10(n)/3]
       0,015

        0,01

       0,005
                                                        • base du rectangle proportionnelle à la longueur
                                                        de l’intervalle
           0
               130     150    170      190       210
                                                        • hauteur du rectangle proportionnelle à l’effectif
                                                                                                                         10
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 11

~~~text
                                                 Variables quantitatives :
                                                  Résumés numériques

              On distingue deux types de résumés numériques :
              • Les indicateurs de position (moyenne, mode, médiane, quartiles). Ils
              positionnent la série des valeurs observées autour d’une tendance
              centrale.

              • Les indicateurs de dispersion (variance, écart-type, étendue inter-
              quartile). Ils indiquent la fluctuation des valeurs de la série autour
              d’une tendance centrale en général.




                                                                                       11
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 12

~~~text
                                                   Variables quantitatives :
                                                 Indicateurs de position (1/3)
           Le mode est la valeur observée d'effectif
            maximum.
            Il sert notamment à détecter si la population est
            homogène ou éventuellement constituée de
            deux ou plusieurs sous-populations.
            Dans le cas du type quantitatif continu il faut
            tenir compte des classes adjacentes.




                                                            La moyenne
                                                                                              Garde les mêmes
                                                                           1
                                                                        x =  n ix i           propriétés que
                              le mode                                      n i                  l’espérance




                                                        !!! Cet indicateur est très sensible aux valeurs
                                                        extrêmes de la série !!!

                                                                                                                12
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 13

~~~text
                                                    Variables quantitatives :
                                                  Indicateurs de position (2/3)
          Les quartiles :
         - La médiane est la valeur qui sépare la population en deux groupes d’effectifs égaux. Elle n’a
         de sens que sur une série rangée par ordre croissant.
          - Le 1er quartile Q1 est la valeur qui sépare la série en ¼ inférieur et ¾ supérieur.
          - Le 3ème quartile Q3 est la valeur qui sépare la série en ¾ inférieur et ¼ supérieur.
         La représentation graphique des ces indicateurs est la boite de Tukey. Elle permet d’avoir une
         aperçu graphique rapide de la distribution des valeurs de la série et permet beaucoup
         d’interprétation.




         Les valeurs extrêmes de cette représentation sont les « moustaches » définies en général par
                                                 m=Q1-1,5×(Q3-Q1)   et   M=Q3+1,5×(Q3-Q1)
         Toutes valeurs de la série en dehors des moustaches est considérée comme atypique


                                                                                                           13
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 14

~~~text
                                                          Variables quantitatives :
                                                        Indicateurs de position (3/3)

                      Note           1           2       3   4        5         6          7
                                                                                                          Elève P
                        Elève L       9          10      8    7       10        9          11
                                                                                                Elève L
                        Elève P      14          2      16    5       6         5          16


                     Série ordonnée

                       Elève L      7        8          9    9       10        10        11

                      Elève P       2        5          5    6       14        16        16



                                  Moyenne             Médiane Q1 Q3        m        M
                     Elève L         9,1                9        8   10    5        13

                     Elève P         9,1                6        5   14    0        27,5




                      Différence de fluctuation des notes  indicateurs de dispersion

                                                                                                                    14
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 15

~~~text
                                                           Variables quantitatives :
                                                           Indicateurs de dispersion
            La variance mesure l’écart au carré entre les valeurs de la série et leur moyenne
                                                                                Garde les mêmes
                                              1
                                        s =  n i (x i − x )
                                         2                      2               propriétés que la
                                                                                variance théorique
                                              n i
             Afin de garder la même unité que la variable, on utilise l’écart-type s =            s2

        Tout comme la moyenne ces deux indicateurs sont sensibles aux valeurs extrêmes de la
        série.
        L’écart-médian mesure l’écart entre les valeurs de la série et leur médiane
                                     1
                            em =  n i x i − med
                                     n i
           On peut aussi utiliser l’étendue de la série max {x i } − min {x i } ou l’écart inter-
           quartiles Q 3 − Q 1

                                                           Variance   Ecart-type   em     Q3-Q1

                                                 Elève L     1,81        1,34       1       8

                                                 Elève P     35,48       5,96      4,85     5


                                                                                                       15
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 16

~~~text
                                                        Variables quantitatives :
                                                       Variables centrées-réduites
               On définit la série centrée-réduite de la façon suivante :

                                                               ~x i =  x i − x 
                                                                        s        
                                                                             x   
                                                                                                                           Démonstration

               La série est dite :                                                    ~x = 1
                                                                                               n
                                                                                                  ~x k = 1
                                                                                                             n
                                                                                                               xk − x 1 1 n                         n         
                                                                                                                   =           (x k − x ) = 1  1 x k − x  = 1 (x − x )
                                                                                                                                                   
                   •     centrée car de moyenne nulle                                      n k =1        n k =1 s x    s x n k =1              s x  n k =1     sx
                   •     réduite car de variance égale à 1                            s2~x =
                                                                                             1   n

                                                                                                               
                                                                                                                      n

                                                                                                                           
                                                                                                                               n
                                                                                                                                  
                                                                                                                                         2
                                                                                                                                                 n
                                                                                                                                                    
                                                                                                                                                                  
                                                                                                   (~xk − ~x )2 = 1 ~x 2 = 1  x k − x  = 12  1 (x k − x )2  = 12 s2x = 1
                                                                                            n k =1                n k =1   n k =1  s x  s x  n k =1             sx




                                    Taux de                                                              Taux de
                     Pays          chômage          PIB                               Pays              chômage               PIB
                     Allemagne         5,5        37430,1                             Allemagne           -0,88               0,18
                     Autriche          4,4        40064,8                             Autriche            -1,08               0,37
                     Belgique          7,6        37727,8
                                                            normalisation             Belgique            -0,52               0,20
                     Danemark          7,5        40189,9                             Danemark            -0,54               0,38
                     Espagne          25,1        31903,8                             Espagne              2,51              -0,21
                     Estonie          10,1        20393,3                             Estonie             -0,09              -1,02
                     …                  …            …                                …                     …                  …
                     Moyenne          10,6        34851,6                             Moyenne                0                 0
                     Ecart-type       5,77       14203,93                             Ecart-type             1                 1


                                                                                                                                                                                   16
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 17

~~~text
                                                 Variables qualitatives

       Les observations d’une variable qualitative sont des modalités et ne sont pas numériques.
       Les traitements précédents n’ont donc pas lieu d’être (moyenne, variance,…) sauf le mode.
       On se contente de faire des tableaux de contingence et des représentations graphiques.


       Représentation des variables nominales
         diagramme en secteurs ou en barre




                            Temps passé sur
                            Internet




                                                 Représentation des variables ordinales
                                                        diagramme en bâtons


                                                                                                   17
CM 1 : Arbres de décision et forêts aléatoires
~~~

## Page 18

~~~text
                                      Résumé des représentations graphiques


                     Variables qualitatives                                   Variables quantitatives




                  nominales                      ordinales             discrètes              continues




                     EISTI : Département Mathématique : Introduction à la statistique                   18
                                                                                                        18
                     descriptive

                                                                                                             18
CM 1 : Arbres de décision et forêts aléatoires
~~~
