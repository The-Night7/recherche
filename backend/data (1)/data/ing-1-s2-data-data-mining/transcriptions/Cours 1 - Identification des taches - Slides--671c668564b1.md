# Cours 1 - Identification des taches - Slides.pdf

[Ouvrir l’original](https://drive.google.com/open?id=17ymyHG7EAofhtsXvUr7oWWi6uN7zIWMu) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                       Datamining 1 : Introduction




                                Datamining 1
Les objectifs de cours sont :

•   Recenser l'ensemble des problématiques couvertes par le Datamining.
•   Mettre en face de chacune des problématiques, la ou les méthodes de
    résolution.
•   Aborder les principales méthodes des deux familles supervisée et non
    supervisée : concepts généraux de chaque famille, algorithmes et
    applications.

Modalités : 18h de cours et TD

Evaluation :
•          1ère session : Examen papier 2h
•          Rattrapage : Examen papier 2h
• Calculatrice, 2 feuilles manuscrites R/V autorisées
~~~

## Page 2

~~~text
                                                                                                           Datamining 1 : Introduction


                                    Process for a datamining study

   Definition of the                    Collect the data                                 Pre-processing the
        study                          select the data in                                       data
 what issues do you                   accordance with your                             outliers, standardisation,
 want to answer?                      issues                                           missing data, …
 Define the statistical
 unit and the variables
                                                                              p variables
                                                                                                   DATA is a table with
                                                                              x11   x1j   xp1      • p columns :




                                                             n observations
                                                                              x12   x2j   xp2      realizations of the
      A Quantitative variable                                                                     random variables
is numerical and represents a
                                                                              x1i  xij  xpi      • n rows :
measurable quantity (continuous or
                                                                                                  observations of the
discrete)
                                                                              x1n   xnj   xpn      statistical unit


               Family        Size
                                                                                         Apply methods
       A Categorial variable                                                    Choice of the method depends on
takes on values that are names or labels
         Ginger              Female
              Blond                                                             •The nature of the variables
      Brown                                                                     • The size of the data
              Black                                                             • The objective
                                                                                       2
                              Male
       Hair colors            Sex                                                                                                        2
~~~

## Page 3

~~~text
                                                                                             Datamining 1 : Introduction


                             Exploration et préparation des données
                                               (1/3)
   Données très variées :
   Statistiques : variables quantitatives, qualitatives   Texte : chaînes de caractères
   Signal : série indexée par le temps                    Images : données 2D
   Réseaux : graphes                                       ….
   souvent en flot continu et sans contrôle de l’acquisition, d’où la nécessité d’un pré-
   traitement : nettoyage, codage/normalisation, réduction de la dimension.

Nettoyage
                - Fiabiliser
                - Remplacer
                - Supprimer
les données incorrectes, c’est-à-dire
                - les données manquantes
                - les données aberrantes Boite de Tukey
                - les valeurs extrêmes (outliers)   ! méthodes basées sur la moyenne et la variance
 Si pour une variable étudiée, il y a peu d’individus présentant une donnée incorrecte,
     - soit on supprime l’individu de l’étude,
     - soit on remplace par une valeur vraisemblable (moyenne, mode,…)
 Si une variable présente trop de valeurs incorrectes alors on la supprime de l’étude
                                                                                                                           3
~~~

## Page 4

~~~text
                                                                                         Datamining 1 : Introduction


                    Exploration et préparation des données
                                      (2/3)
Codage
• Codage des données brutes : date en durée, âge ou ancienneté, transformation de
« bleu », « vert », « jaune » en « 1 », « 2 »,…,, transformation d’une variable continue en
classes,…
• Création d’indicateurs pertinents (ratio, moyenne sur une période, montant moyen d’un
achat à partir du nombre et du montant de chaque achat …)


Normalisation                                                   Problème des unités
                                                            (ordre de grandeurs des variables)
             Pop.          Taux nat.      Esp.   Nb.
             (milliers)    (pour mille)   vie    enfants
                                                                Centrage et réduction
  Argentine 41050         16,87           75,87 2,19
  Arménie    3099         15,47           74,44 1,77
                                                                        xki  x k
  Australie 21731         12,56           81,99 1,85               xi 
                                                                    k

  Autriche   8407         9,01            80,55 1,40
                                                                            sk
distance entre
l’Argentine et        (41050-3099)²+(16,87-15,47)²+(75,87-74,44)²+(2,19-1,77)²=1440278405
   l’Arménie                                                   (41050-3099)² =1440278401
                                                                     4


                                                                                                                       4
~~~

## Page 5

~~~text
                                                                                     Datamining 1 : Introduction


                   Exploration et préparation des données
                                     (3/3)
Réduction de la dimension
 Réduction du nombre d’individus
    - Elimination des individus hors norme (<1%-2%)
    - Echantillonnage (aléatoire, systématique ou stratifié) : diminue le temps de
    traitement
    - Partitionnement des individus (clustering) : permet de travailler sur des groupes plus
    homogènes d’individus

 Réduction des variables
     - Supprimer les variables non exploitables (trop de données incorrectes) ou non
     pertinentes par rapport à l’objectif
     - Ignorer des variables corrélées entre elles ou les combiner (ACP)
Diminuer le nombre de variables permet de diminuer la complexité du modèle. Au-delà de
20 variables un modèle de prédiction risque de voir sa capacité de généralisation diminuer.

 Réduction du nombre de modalités
    - Regrouper les modalités ou les valeurs discrètes ayant un faible effectif
    - Discrétiser une variable continue en classes (par exemple les quartiles)
                                                                                                                   5
~~~

## Page 6

~~~text
                                                                               Datamining 1 : Introduction


                             Basic datamining objective

  Supervised learning /Prediction       Unsupervised learning /Description
 Explain a target variable with other     Describe hidden structure from
               variables                          unlabeled data
• Quantitative target
                                        • Description
                                        Summarize the variables,
Regression                              detect link between
 linear regression                     Variables, detect outliers, …
 SVR                                   Graphical and numerical description
 neural network                        PCA, CA ,,…
…                                      Association rules, …

• Categorial target                     • Clustering
                                        Organizing objects into
                                        groups (clusters) such that
Classification                          the members in each
                                        Group are similar
logistic regression
decision tree                          K-means
 neural network                        Hierarchical clustering
…                                      …
                                                    6
                                                                                                             6
~~~

## Page 7

~~~text
                                                                                                             Datamining 1 : Introduction




                                              Sommaire
    Clustering
    • k-means
    • CAH
    Réduction de dimension
    • Réduire la dimension avec une ACP avant un k-means
    Découverte de règles
    • non-supervisé : Règles d'association
    • supervisé : Arbre de décision




                                  !! Attention à la terminologie !!
            Anglais                    Français
      Classification                Discrimination, classement (apprentissage supervisé)
      Clustering                    Segmentation,… (apprentissage non-supervisé)
Cela prête d’autant plus à confusion que la méthode appelée « classification hiérarchique ascendante » est
une méthode de clustering et non de classification !
                                                                                7                                                          7
~~~
