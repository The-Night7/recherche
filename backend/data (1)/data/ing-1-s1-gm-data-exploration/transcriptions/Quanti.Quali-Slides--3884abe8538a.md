# Quanti.Quali-Slides.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Bc8Kl7fESNpUFx_Why4IYFvq8cb2wFrg) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                            Analyse bivariée quantitatif-qualitatif




                 Data exploration
        Statistiques descriptives bivariées
    Observer simultanément des individus d'une population sur deux
    caractères
    Mesurer un lien éventuel entre deux caractères en utilisant un
    résumé chiffré qui traduit l'importance de ce lien
    Qualifier ce lien :
–      en cherchant une relation numérique approchée entre deux caractères quantitatifs
–      en cherchant des correspondances entre les modalités de deux caractères qualitatifs


                                                     • qualitatif ×qualitatif
2 types de variables  3 types de croisements :      • qualitatif ×quantitatif
                                                     • quantitatif ×quantitatif
~~~

## Page 2

~~~text
                                                                                     Analyse bivariée quantitatif-qualitatif


                                      Croisement Quantitatif - Qualitatif
                                                  Sous-populations
 Pour étudier le lien entre une variable qualitative à p modalités et un caractère quantitatif,
 on partitionne la population p en sous-populations : une sous-population pour chaque
 modalité de la variable qualitative.

Prenons l’exemple de l’étude comparative de la taille entre les     HOMMES           FEMMES
hommes et les femmes.                                             200          200
La variable qualitative est le genre. On divise donc la
population en deux sous-populations, celui des hommes et          190          190
celui des femmes.
Sur chaque sous-population, il est possible de calculer les       180          180
résumés numériques usuels.
Une comparaison des boites de Tukey permet d’avoir une            170          170
première idée du lien antre les variables
                                                                  160          160

GENRE          Effectifs       Moyenne        Écart-type
                                                                  150          150
Hommes            23            162,30          14,21
Femmes            35            149,29          10,52             140          140
Total             58            154,45          13,61
                                                                  130          130


L’idée est de décomposer la moyenne et la variance sur les différents sous-populations.
~~~

## Page 3

~~~text
                                                                                      Analyse bivariée quantitatif-qualitatif


                                          Croisement Quantitatif - Qualitatif
                               Décomposition de la moyenne
Notons Y la variable quantitative et pour k=1,…,p
          • nk l’effectif de la kème sous-population
          •     la moyenne de Y sur la kème sous-population
          •     la variance de Y sur la kème sous-population
                                                  Sous-population   Sous-population
                 Sous-population
                      bleue                            verte             rouge




                                   y bleue                                 y rouge
                                   s 2bleue                                s 2rouge
                                                         y verte
                                                         s 2verte


 La moyenne de la population est égale à la moyenne pondérée des moyennes des
 sous-populations,
                                      1
                                   =



                                                                                                                           3
~~~

## Page 4

~~~text
                                                                                              Analyse bivariée quantitatif-qualitatif


                           Croisement Quantitatif - Qualitatif
                       Décomposition de la variance
Contrairement à la moyenne, la variance de la population n’est pas égale à la moyenne
pondérée des variances des sous-populations. Cette dernière s’appelle la variance
intra groupes,
                                                            Effectif de la sous-
                                                            population k
                                                1
                                          Y =
                                                                       Variance de la sous-
                                                                       population k



             Sous-population              Sous-population                 Sous-population
                                               verte                           rouge
                  bleue




                               y bleue                                             y rouge
                               s 2bleue                                            s 2rouge
                                                 y verte
                                                 s 2verte




                                                                                                                                   4
~~~

## Page 5

~~~text
                                                                                             Analyse bivariée quantitatif-qualitatif


                            Croisement Quantitatif - Qualitatif
                           Décomposition de la variance
A la variance intra groupes, on ajoute la variance inter groupes,

                                                 1
                                        Y =                    (    − )²

•   Pour chaque sous-population, on crée un individu virtuel dont la valeur sur Y est
    égale à la moyenne des valeurs de Y des individus de la sous-population.
•   On crée donc une nouvelle population formée de ces individus virtuels. Chaque
    individu aura un poids de nk , l'effectif de chaque sous-population.

                                        Sous-population            Sous-population
         Sous-population
                                        verte                      rouge
         bleue

                                                                     y rouge

     Individu virtuel
     représentant la          y bleue
     population bleue                                y verte
                                                                                Individu virtuel
                                                                                représentant la
                              Individu virtuel                                  population rouge
                              représentant la
                              population verte                                                                                    5
~~~

## Page 6

~~~text
                                                                                                 Analyse bivariée quantitatif-qualitatif


                                    Croisement Quantitatif - Qualitatif
                                 Décomposition de la variance
On peut donc définir trois variances sur variable Y.
     •       une première qui explique les variations de Y dans toute la population : totale
     •       une deuxième qui explique les variations de Y dans les sous-populations: intra
     •       une troisième qui explique les variations de Y entre les sous-populations : inter

Nous avons la décomposition de la variance suivante :

                                            ( )=                   +             ( )
                                                       Variance           Variance
                                                       expliquée         résiduelle


On en déduit une mesure du lien entre X et Y avec le rapport de corrélation


                                                    ( )
Le rapport de corrélation représente le pourcentage de variabilité de Y expliquée par X. Il varie entre 0
et 1. Si
    • S’il est nul alors la variance expliquée est nulle, il n’y a donc aucun lien entre Y et X
    • S’il vaut 1 alors la variance expliquée est égale à la variance de Y donc Y est entièrement
         expliquée par X.

                                                                                                                                      6
~~~

## Page 7

~~~text
                                                                                Analyse bivariée quantitatif-qualitatif


                            Croisement Quantitatif - Qualitatif
                                                Exemple
Etude comparative de la taille entre les hommes et les femmes.

GENRE  Effectifs       Moyenne       Variance            Var intra
Hommes    23            162,0         193,3          23×193,3=4444,9
Femmes    35            149,3         107,6          35×107,6 =3765,1
Total     58            154,4         182,1      (4444,9+3765,1)/58 =141,5

GENRE  Effectifs       Moyenne       Variance             Var inter
Hommes    23            162,3         193,3      23×(162,3-154,4)² =1419,5
Femmes    35            149,3         107,6       35×(149,3-154,4)² =932,8
Total     58            154,4         182,1       (1419,5+932,8)/58 = 40,6
  On vérifie la formule de la décomposition de la variance : 141,5+40,6=182,1



                                    40,6
     Rapport de corrélation :             = 0,22
                                    182,1
      22% de la variabilité de la taille est expliquée par le genre

                                                                                                                     7
~~~
