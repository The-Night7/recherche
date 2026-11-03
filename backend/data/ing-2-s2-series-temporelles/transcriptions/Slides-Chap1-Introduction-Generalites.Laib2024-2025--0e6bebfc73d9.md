# Slides-Chap1-Introduction-Generalites.Laib2024-2025.pdf

[Ouvrir l’original](https://drive.google.com/open?id=17zhLDEyNGYtqeHmrwiOSgm2GkW0rTqGE) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives des
                         Séries Temporelles



                                      CY Tech


                                9 janvier 2025




    (CY Tech)        Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                              9 janvier des
                                                                                        2025Séries Temporelles
                                                                                                        1 / 72
~~~

## Page 2

~~~text
Plan


1   Introduction


2   Vocabulaire, Généralités et exemples


3   Mesures de Dépendance


4   Analyse descriptive d’une Série Temporelle


5   Annexe : mise en œuvre sous R


6   Références




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                 2 / 72
~~~

## Page 3

~~~text
Introduction

    La publication de l’indice des prix et du nombre de chômeurs est un indicateur clé
    de la réussite ou de l’échec d’une politique économique.
    De même, la publication de certaines statistiques monétaires ou financières influe
    fortement sur le comportement des investisseurs.
       Il est donc important de connaître la valeur des indices avant leur publication
                                         officielle.
    Ces exemples illustrent des séries d’observations mensuelles, c’est-à-dire :
        Une suite d’observations (xt )t ∈Z portant sur un même objet, recueillies à des instants
        équidistants, que l’on appelle séries chronologiques ou temporelles.

    Ces séries peuvent être considérées comme des réalisations d’une famille de variables
    aléatoires, ou processus stochastique (Xt ; t ∈ Z).
    On modélise un processus comme la somme ou le produit d’une partie déterministe
    et d’une partie aléatoire :
                                    Xt = f (t) + ϵt .




         (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                 3 / 72
~~~

## Page 4

~~~text
Introduction (suite)

▷ L’étude d’un processus aléatoire à partir de série d’observations

                                              (xt )1≤t ≤T

a deux objectifs :
  1 étudier l’évolution dans le temps d’un phénomène aléatoire décrit par ce processus et
    expliquer ces variations,
  2   prédire les valeurs futures

▷ Dans les deux cas, on recherche une structure (un modèle).

      La modélisation de la partie aléatoire se fera sur une série à laquelle on aura enlevé
      la partie fixe, on travaille sur un processus dit "stationnarisé ".

▷ Le cours de série temporelles se décompose en général en deux grandes parties.

      Initiation aux méthodes statistiques descriptives et la modélisation de la partie
      déterministe en vue de la prévision. C’est que nous allons étudier dans ce cours.
      La deuxième partie consiste à Présenter les modèles ARMA et ARIMA qui
      permettent la modélisation de la partie aléatoire (cours de modèles de prévision
      -DES et FINTECH-).
           (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                   4 / 72
~~~

## Page 5

~~~text
Objectifs du module / Compétences acquises

▷ Modélisation de la partie déterministe d’une série temporelle

    Acquérir les bases pour étudier, décrire et analyser une suite de valeurs numériques
    dépendantes représentant une évolution dans le temps.
    Construire un modèle statistique pour prévoir les observations futures à partir des
    données passées et présentes.
    Appliquer ces méthodes sur des données simulées et réelles, avec un tableur ou le
    logiciel R.

▷ Thèmes abordés

    Chapitre 1 : Introduction aux séries temporelles (Vocabulaire et généralités).
    Chapitre 2 : Désaisonnalisation par régression linéaire et prévision.
    Chapitre 3 : Désaisonnalisation par moyennes mobiles.
    Chapitre 4 : Lissage exponentiel et prévision.
    Chapitre 5 : Introduction aux processus stochastiques stationnaires (Modèles AR et
    AM).



         (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                                5 / 72
~~~

## Page 6

~~~text
            Vocabulaire, Généralités et exemples




(CY Tech)      Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                        9 janvier des
                                                                                  2025Séries Temporelles
                                                                                                  6 / 72
~~~

## Page 7

~~~text
Vocabulaire, Généralités et Exemples

□ Une série chronologique :

    Est la réalisation d’un processus aléatoire indicé par le temps : {Xt }.
    Pour chaque instant t, Xt (ω) est une variable aléatoire dont on observe une
    réalisation xt .

□ Exemple : Consommations mensuelles de viande bovine de 1980 à Octobre 1995 :

             x1 = 129.060, x2 = 129.075, x3 = 131.632, . . . , x190 = 118.565.

  - L’indice t représente le numéro du mois (ex. Octobre 1995 correspond à t = 190).
  - Les séries peuvent être journalières, hebdomadaires, mensuelles ou trimestrielles,
    selon l’unité de temps.
  - Si plusieurs séries sont observées simultanément (ex. consommation et prix), on
    parle de série multidimensionnelle.




         (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                 7 / 72
~~~

## Page 8

~~~text
Vocabulaire, Généralités et Exemples

□ Une série temporelle est une suite d’observations {xt }1≤t ≤T , pouvant être vue comme
une série statistique bidimensionnelle (t , xt ), avec :

  - t : le temps (ex. année, jour, heure, minute).
  - xt : une valeur numérique observée à l’instant t.

  - Les points de la série sont souvent reliés pour faciliter la lecture et identifier des
    tendances.
  - Un échantillon (t , xt )1≤t ≤n n’est pas constitué de variables indépendantes, car les
    observations successives sont corrélées.
  - La dépendance temporelle est une source clé d’information.




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                 8 / 72
~~~

## Page 9

~~~text
Propriétés des Séries Chronologiques

    Les observations sont généralement ordonnées dans le temps (ordre chronologique).
    Les séries peuvent être :
        Journalières (ex. cours boursiers).
        Mensuelles (ex. consommation d’électricité).
        Trimestrielles (ex. nombre de chômeurs).
        Annuelles (ex. bénéfices d’exportations).
    L’ordre des données est fondamental : une donnée x3 précède x4 , x5 , etc.
    Contrairement à d’autres données (ex. âges ou salaires dans un recensement), les
    séries chronologiques respectent cet ordre.




         (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                                9 / 72
~~~

## Page 10

~~~text
            Repérage des données dans le temps
             Graphique d’une Série Temporelle




(CY Tech)         Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                           9 janvier des
                                                                                     2025Séries Temporelles
                                                                                                    10 / 72
~~~

## Page 11

~~~text
Repérage des données dans le temps

     Les données d’une série temporelle trimestrielle, mensuelle, journalière peuvent être :
          Repérées par un seul indice t, représentant le nombre de périodes écoulées depuis la
          première observation.
          Repérées par deux indices i et j :
                i : l’année de l’observation.
                j : la période au sein de l’année (ex. : trimestre, mois, jour).

     On note la série (xt ) ou (xi ,j ) de manière équivalente.


▷ Lien entre (xt ) et (xi ,j )

     Les données s’étendent sur N années.
     Chaque année est divisée en p périodes (ex. : trimestres, mois, jours).
     L’observation du j ème mois de la i ème année xi ,j peut être convertie en xt avec :

                                 t = (i − 1) × p + j ,      1 ≤ i ≤ N; 1 ≤ j ≤ p .
Exemples :
     Série trimestrielle : x4,2 = 4370 =⇒ t = (4 − 1) × 4 + 2 = 14 ⇒ xt = 4370.
     Série mensuelle : x26 = 542 =⇒ 26 = 2 × 12 + 2 ⇒ i = 3, j = 2 ⇒ xi ,j = 542.


           (CY Tech)               Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                            9 janvier des
                                                                                                      2025Séries Temporelles
                                                                                                                     11 / 72
~~~

## Page 12

~~~text
Explication de la formule : t = (i − 1) × p + j

      La formule convertit un repérage bidimensionnel (i , j) (année et période) en un
      repérage unidimensionnel t (indice global).
      Cela simplifie l’organisation des données en une série chronologique linéaire.

Étapes :
  1   Structure des données :
           Les données s’étendent sur N années.
           Chaque année contient p périodes.
  2   Indice global t :
           t = (i − 1) × p + j.
           (i − 1) × p : nombre total de périodes avant l’année i.
           j : période au sein de l’année i.


Conditions :

      1 ≤ i ≤ N, 1 ≤ j ≤ p : indices valides.

Conclusion : La formule est essentielle pour analyser les séries temporelles en une
dimension.

           (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                          9 janvier des
                                                                                                    2025Séries Temporelles
                                                                                                                   12 / 72
~~~

## Page 13

~~~text
Deux présentations d’une série temporelle

▷ Une série temporelle peut être représentée sous deux formes principales :
    Tableau à deux colonnes contenant N × p lignes :
                                       t      Yt
                                       1      Y1
                                       2      Y2
                                       ..      ..
                                        .       .
                                      Np YNp
    Tableau en lignes et colonnes :
         p colonnes pour les périodes (par exemple, mois ou trimestres).
         N lignes pour les périodes complètes (souvent des années).




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                13 / 72
~~~

## Page 14

~~~text
Exemple de présentation : Série trimestrielle

▷ Illustration avec une série trimestrielle représentant le chiffre d’affaires (en milliers de
francs) d’un magasin de 1978 à 1982.




          (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                        9 janvier des
                                                                                                  2025Séries Temporelles
                                                                                                                 14 / 72
~~~

## Page 15

~~~text
Graphique d’une Série Temporelle

▷ Avant toute analyse, il est essentiel de commencer par explorer la série temporelle.

    Graphiques exploratoires : Ils permettent de comprendre la structure de la série et
    de guider sa modélisation.
    Chronogramme : Représentation des points (t , Yt ) pour visualiser l’évolution au fil
    du temps.
    Il révèle des aspects clés : valeurs atypiques, ruptures ou changements dans la
    dynamique.




          (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               15 / 72
~~~

## Page 16

~~~text
Exemple : Chiffre d’affaires

▷ Points (t , Yt ) reliés par des segments pour représenter l’évolution sur toute la période
observée.




                                   Figure – Chiffre d’affaire




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                16 / 72
~~~

## Page 17

~~~text
Courbes superposées : Exemple Chiffre d’affaires

▷ Représentation des points (j , Yi ,j ) reliés par segments pour chaque année i.

    Montre l’évolution mensuelle annuelle et permet de comparer les valeurs pour un
    même mois entre années.
    Ne met pas en évidence l’évolution globale au fil du temps.




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                17 / 72
~~~

## Page 18

~~~text
Exemples de Séries Temporelles




        (CY Tech)       Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                 9 janvier des
                                                                                           2025Séries Temporelles
                                                                                                          18 / 72
~~~

## Page 19

~~~text
Exemples de Séries Temporelles

    Population américaine : Croissance régulière sans grande variabilité.
    Ventes de champagne : Saisonnalité marquée avec un pic en fin d’année ; variance
    croissante.
    Consommation d’électricité : Deux cycles : jour/nuit et semaine/week-end.
    Ventes de voitures : Tendance à la hausse, deux saisonnalités et une rupture en
    1983.

Point commun : Une dépendance temporelle entre les observations.




         (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               19 / 72
~~~

## Page 20

~~~text
Bénéfices Trimestriels par Action de Johnson & Johnson

     Ces données couvrent 84 trimestres (21 ans) allant du premier trimestre de 1960 au
     dernier trimestre de 1980.
     La modélisation de telles séries commence par l’observation des motifs principaux
     dans l’historique temporel.




Figure – 1.1. Bénéfices trimestriels par action de Johnson & Johnson, du premier trimestre 1960
au quatrième trimestre 1980.

On note :
    une tendance sous-jacente croissante ;
     une variabilité accrue ;
     une oscillation régulière superposée à la tendance, qui semble se répéter chaque
     trimestre.
          (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  20 / 72
~~~

## Page 21

~~~text
Réchauffement Climatique : Écarts de Température Moyenne Globale
Annuelle




    Figure – 1.3 : Les écarts de température moyenne globale annuelle (1880–2009) en °C

Contexte : Ces données représentent l’indice moyen global des températures terre-océan
de 1880 à 2015, basé sur la période de référence 1951-1980.
Observations :
    Une tendance à la hausse est visible durant la seconde moitié du 20e siècle, utilisée
    comme argument pour soutenir l’hypothèse du changement climatique.
    Cette tendance est non linéaire, avec des phases de stabilisation alternant avec des
    augmentations rapides.
    La question centrale est de déterminer si cette tendance est naturelle ou causée par
    une intervention humaine.
         (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               21 / 72
~~~

## Page 22

~~~text
Indice Dow Jones Industrial Average (DJIA)

Exemple : Série temporelle financière (rendements quotidiens).




Figure – Rendements quotidiens de l’indice Dow Jones Industrial Average (20 avril 2006 - 20 avril
2016).

Observations :

     Les données représentent les rendements quotidiens (variations en pourcentage) de
     l’indice DJIA.
     La crise financière de 2008 est identifiable sur la figure par une forte volatilité.
           (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  22 / 72
~~~

## Page 23

~~~text
Analyse des rendements du DJIA

Caractéristiques principales :

    Moyenne stable : Le rendement moyen est proche de zéro.
    Volatilité groupée : Les périodes de forte volatilité tendent à se suivre (phénomène
    d’agrégation).

Formulation mathématique :

    Si xt est la valeur de l’indice DJIA et rt = xtx−tx−t1−1 le rendement, alors :
                                  xt
                      1 + rt =         ,    log(1 + rt ) = log(xt ) − log(xt −1 ) ≈ rt .
                                 xt −1

Problématique : Prévoir la volatilité future des rendements.

    Modèles adaptés : ARCH et GARCH, développés pour analyser ces dynamiques.
    Le jeu de données est disponible dans le package astsa avec le chargement de xts.




          (CY Tech)              Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                          9 janvier des
                                                                                                    2025Séries Temporelles
                                                                                                                   23 / 72
~~~

## Page 24

~~~text
                              Modèles de Séries Temporelles

▷ L’objectif principal de l’analyse des séries temporelles est de

    développer des modèles mathématiques qui fournissent des descriptions plausibles
    des données d’échantillons, comme celles rencontrées dans la section précédente.




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                24 / 72
~~~

## Page 25

~~~text
Bruit Blanc

▷ un bruit blanc simple est une suite de

    Variables aléatoires indépendantes et identiquement distribuées (iid).
    Moyenne 0 et variance σ2ϵ .
    Notation :
                                            ϵt ∼ iid(0, σ2
                                                         ϵ)

▷ Bruit blanc gaussien :

    Variables normales indépendantes.
    Moyenne 0 et variance σ2ϵ .
    de même loi gaussienne
    Notation :
                                        ϵt ∼ iid N (0, σw ϵ2)



Exemple :

    Série de 500 variables aléatoires normales indépendantes.
    Variance σ2ϵ = 1.
            (CY Tech)        Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               25 / 72
~~~

## Page 26

~~~text
Moyennes Mobiles et Filtrage

▷ On replace le bruit blanc ϵt par une moyenne mobile : Mt = 13 (ϵt −1 + ϵt + ϵt +1 ),
C’est-à-dire : la moyenne de sa valeur actuelle et de ses voisins immédiats dans le passé
et le futur.




Figure – 1.7 Série de bruit blanc gaussien (haut) et moyenne mobile à trois points de la série de
bruit blanc gaussien (bas)

           (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  26 / 72
~~~

## Page 27

~~~text
   la série des moyennes mobiles est représentée dans le panneau inférieur de la Figure
   1.7.
   Cette série est beaucoup plus lisse que la série de bruit blanc,
   il est claire que la moyenne supprime une partie du comportement haute fréquence
   du bruit.

w = rnorm(500,0,1) # 500 N(0,1) variables
v = filter(w, sides=2, rep(1/3,3)) # moyenne mobile
par(mfrow=c(2,1))
plot.ts(w, main="bruit blanc")
plot.ts(v, ylim=c(-3,3), main="moyenne mobile")




        (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                     9 janvier des
                                                                                               2025Séries Temporelles
                                                                                                              27 / 72
~~~

## Page 28

~~~text
Marche aléatoire avec dérive

 ▷ Un modèle pour analyser une tendance, comme celle observée dans les données de
   température globale à la Figure 1.3, est le modèle de marche aléatoire avec dérive :
                            Xt = δ + Xt −1 + ϵt ,         t = 1, 2, . . . ,   X 0 = 0,                              (1)
où ϵt est un bruit blanc.
    La constante δ est appelée la dérive.
    Lorsque δ = 0, le modèle devient une marche aléatoire, car la valeur Xt est
    simplement la somme de Xt −1 et d’un mouvement aléatoire ϵt .
Réécriture :
                                                 t
                                                 X
                                   Xt = δt +            ϵj ,   t = 1, 2, . . . .                                    (2)
                                                 j =1
▷ Cette expression peut être vérifiée par induction ou en substituant (2) dans (1).

set.seed(154) # pour reproduire les résultats
w = rnorm(200); x = cumsum(w) # deux commandes sur une ligne
wd = w + 0.2; xd = cumsum(wd)
plot.ts(xd, ylim=c(-5,55), main="marche aléatoire", ylab=’’)
abline(a=0, b=0.2, lty=2) # dérive
lines(x, col=4)
abline(h=0, col=4, lty=2)
          (CY Tech)               Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                           9 janvier des
                                                                                                     2025Séries Temporelles
                                                                                                                    28 / 72
~~~

## Page 29

~~~text
Marche aléatoire avec dérive




Figure – 1.9- Marche aléatoire, σϵ = 1, avec une dérive δ = 0.2 (ligne supérieure en dents de scie),
sans dérive, δ = 0 (ligne inférieure en dents de scie), et lignes en pointillés représentant les dérives.


▷ La Figure 1.9 montre

     200 observations générées à partir du modèle avec δ = 0 et δ = 0.2, et avec un bruit
     normal standard.
     Pour comparaison, nous avons superposé les lignes droites δ sur le graphique.



           (CY Tech)              Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                           9 janvier des
                                                                                                     2025Séries Temporelles
                                                                                                                    29 / 72
~~~

## Page 30

~~~text
                         Mesures de Dépendance




Ces mesures décrivent le comportement général d’un processus au cours du temps




    (CY Tech)         Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                               9 janvier des
                                                                                         2025Séries Temporelles
                                                                                                        30 / 72
~~~

## Page 31

~~~text
Fonction moyenne :

Définition 1
La fonction moyenne est définie par :

                                           µxt = E(xt ).                                                        (3)


    Exemple : Fonction Moyenne d’une Série à Moyenne Mobile
         Si ϵt est un bruit blanc, alors µϵt = 0.
         Lisser la série ne change pas la moyenne :
                                                1£
                             µMt = E(Mt ) =       E(ϵt −1 ) + E(ϵt ) + E(ϵt +1 ) = 0.
                                                                                ¤
                                                3
▷ Exemple : Fonction Moyenne d’une Marche Aléatoire avec Dérive

    Considérons le modèle xt = δ · t + tj=1 ϵj .
                                      P

    µxt = E(xt ) = δ · t.
    La fonction moyenne est une droite de pente δ.




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                31 / 72
~~~

## Page 32

~~~text
Fonction d’autocovariance

    Définition 1.2. La fonction d’autocovariance est définie comme :

                                     γx (s , t) = E[(xs − µs )(xt − µt )].                                          (4)

    Symétrie : γx (s , t) = γx (t , s).

    L’autocovariance mesure la dépendance linéaire entre deux instants temporels.
    Si γx (s , t) = 0, xs et xt ne sont pas linêirement liés.
    Variance :
                                    γx (t , t) = E[(xt − µt )2 ] = var(xt ).                                        (5)




          (CY Tech)               Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                           9 janvier des
                                                                                                     2025Séries Temporelles
                                                                                                                    32 / 72
~~~

## Page 33

~~~text
Propriétés de covariance dans les séries temporelles

▷ Pour étudier les propriétés de covariance de divers modèles de séries temporelles, le
résultat suivant sera utilisé de manière répétée :
▷ Résultat : Si c1 , c2 , . . . , cm et d1 , d2 , . . . , dn sont des constantes, et t1 , t2 , . . . , tm et
s1 , s2 , . . . , sn sont des points temporels, alors :

                                Ã                                 !
                                    m
                                    X                 n
                                                      X                 m X
                                                                        X n
                      Cov                  ci Xti ,          dj Xsj =               ci dj Cov(Xti , Xsj ).                         (6)
                                    i =1              j =1              i =1 j =1


▷ En particulier : La variance de la somme de variables aléatoires Yti , pour i = 1, . . . , n,
est donnée par :


                                                                              −1
                      Ã                     !
                          n                       n                      n iX
                                                     ci2 Var(Yti ) + 2
                          X                      X                      X
                Var             ci Yti =                                         ci cj Cov(Yti , Ytj ).                            (7)
                         i =1                   i =1                   i =2 j =1




             (CY Tech)                           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                                          9 janvier des
                                                                                                                    2025Séries Temporelles
                                                                                                                                   33 / 72
~~~

## Page 34

~~~text
Exemples de calculs de fonctions d’Autocovariance

▷ 1. Autocovariance du Bruit Blanc

    E(ϵt ) = 0.
    Autocovariance :
                                                    σ2
                                                   (
                                                     ϵ     si s = t ,
                                    γϵ (s , t) =                                                              (8)
                                                       0   si s ̸= t .

2. Autocovariance d’une Moyenne Mobile

    Pour une moyenne mobile Mt à partir d’un bruit blanc ϵt ,
                                              3 σ2
                                            
                                            
                                             9 ϵ           s = t,
                                             2 σ2
                                            
                                                            | s − t | = 1,
                                            
                                                 ϵ
                                γM (s , t) = 91 σ2                                                            (9)
                                            
                                            
                                             9  ϵ          | s − t | = 2,
                                            
                                                   0        | s − t | > 2.
                                            




          (CY Tech)         Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                     9 janvier des
                                                                                               2025Séries Temporelles
                                                                                                              34 / 72
~~~

## Page 35

~~~text
3. Autocovariance d’une Marche Aléatoire

    Pour une marche aléatoire xt = tj=1 ϵj ,
                                  P


                                         γx (s , t) = min(s , t)σ2
                                                                 ϵ.                                              (10)

    La variance croît linéairement avec le temps :

                                        var(xt ) = γx (t , t) = t σ2ϵ .                                          (11)


▷ La fonction d’autocorrélation (FAC)

Définition 2
La fonction d’autocorrélation est :
                                                       γ(s , t)
                                    ρ (s , t) = p                      .                                         (12)
                                                    γ(s , s)γ(t , t)


    ρ (s , t) mesure la prédictibilité linéaire entre xs et xt .
    −1 ≤ ρ (s , t) ≤ 1.



          (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  35 / 72
~~~

## Page 36

~~~text
    Analyse descriptive d’une Série Temporelle




(CY Tech)     Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                       9 janvier des
                                                                                 2025Séries Temporelles
                                                                                                36 / 72
~~~

## Page 37

~~~text
Objectifs de l’analyse d’une série temporelle

L’analyse des séries temporelles a pour objectifs principaux :

    Décrire l’évolution d’une variable au fil du temps ;
    Expliquer et interpréter les phénomènes observés ;
    Prédire les valeurs futures à partir des données passées et présentes ;
    Construire un modèle statistique capable de :
         Prévoir les observations futures,
         Prendre en compte la dépendance temporelle des données.




          (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               37 / 72
~~~

## Page 38

~~~text
Description et résumé d’une série temporelle

Pour décrire une série temporelle :

    On utilise un échantillon x1 , x2 , . . . , xn issu d’une réalisation d’un processus aléatoire
    {Xt (ω)}.
    Les représentations graphiques permettent de visualiser les tendances, les cycles ou
    les anomalies éventuelles.
    On calcule des indices numériques, notamment :
         La moyenne, la variance et la covariance empiriques,
         L’autocorrélation empirique, qui quantifie les relations temporelles.

    Les fonctions d’autocorrélation fournissent une meilleure compréhension des
    structures temporelles et des dépendances à différentes échelles de temps.




          (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                        9 janvier des
                                                                                                  2025Séries Temporelles
                                                                                                                 38 / 72
~~~

## Page 39

~~~text
1. Moyenne empirique

    À chaque instant t, on calcule la moyenne empirique des observations précédentes :

                                                    1X  t
                                            xt =          x
                                                    t i =1 i

    Cet indicateur donne une idée de la tendance centrale des données à un instant t
    donné.

Remarque : La moyenne empirique x t est un indicateur évolutif.

               Si la série temporelle est stationnaire, cette moyenne converge vers une
               constante correspondant à l’espérance de la série.




         (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                     9 janvier des
                                                                                               2025Séries Temporelles
                                                                                                              39 / 72
~~~

## Page 40

~~~text
Exemple : Étude des données de la SNCF

▷ Exemple :
    Nous considérons les données de la SNCF, représentant le trafic voyageurs entre
    1963 et 1980 (Gouriéroux et Monfort)
    Observation : Le trafic voyageur suit une croissance moyenne linéaire au cours du
    temps.




         (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                     9 janvier des
                                                                                               2025Séries Temporelles
                                                                                                              40 / 72
~~~

## Page 41

~~~text
Les données étant mensuelles,

il est possible de les moyenner par année (ou par mois) pour faire apparaître la
tendance ou une période.

                 Figure – Trafic SNCF-Moyenne annuelles et mensuelle




     (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                   9 janvier des
                                                                                             2025Séries Temporelles
                                                                                                            41 / 72
~~~

## Page 42

~~~text
2. Indices de dispersion : Variance empirique

▷ La dispersion. La variance empirique des observations jusqu’à l’instant t est donnée
par :
                                                1X  t
                            b2
                            σ t (0) := γ
                                       bt (0) =       (x − x t )2 .
                                                t i =1 i

⇓ Interprétation :
    Cet indice permet de juger la dispersion des observations autour de la tendance
    centrale.
    Il donne également une indication sur l’évolution de la variance dans le temps.




          (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               42 / 72
~~~

## Page 43

~~~text
3. Indices de dépendance temporelle : Auto-covariance empirique

▷ Auto-covariance empirique d’ordre h (covariance entre les valeurs décalées) :

    La dépendance temporelle est mesurée à l’aide de l’auto-covariance empirique.
    Ces indices γbt (h) sont calculés pour des décalages h = 1, 2, . . . à chaque instant t.
    Ils indiquent la dépendance entre deux observations séparées par h unités de temps.


                                 1 tX−h
                      γ
                      bt (h) =          (x − x t )(xi +h − x t ),        h = 1, 2, . . .
                                 t i =1 i

Exemples d’interprétation :

    Pour h = 1, l’auto-covariance indique la dépendance entre deux observations
    successives.
    Pour h = 2, elle mesure la dépendance entre deux observations séparées par deux
    unités de temps.

Remarque : Sur l’exemple du trafic SNCF, on observe une dépendance notable entre xt
et xt +1 , mais aussi entre xt et xt +12 , indiquant une périodicité potentielle dans les
données.

          (CY Tech)              Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                          9 janvier des
                                                                                                    2025Séries Temporelles
                                                                                                                   43 / 72
~~~

## Page 44

~~~text
4. Auto-corrélations empiriques

▷ Définition. L’auto-corrélation empirique est le quotient de l’auto-covariance par la
variance :
                                         γ
                                         bt (h)
                               ρbt (h) =        , |ρbt (h)| ≤ 1.
                                         γ
                                         bt (0)
Propriétés :
     ρbt (0) = 1.
     L’auto-corrélation mesure la force de la dépendance entre les observations séparées
     par h unités de temps.
     Plus |ρbt (h)| est proche de 1, plus la dépendance est forte.
Lien avec les données décalées : Pour h = 1, l’auto-corrélation est proche du coefficient
de corrélation entre :
                         (x1 , x2 , . . . , xn−1 ) et (x2 , x3 , . . . , xn ).
Visualisation :
▷ On peut avoir une première idée de l’auto-corrélation en visualisant les nuages de
points des séries {xt } et {xt +h }.
     La forme du nuage de points des séries décalées (xt , xt +h ) donne une indication
     visuelle sur l’auto-corrélation.
     Un nuage allongé indique une forte dépendance (auto-corrélation proche de ±1).
           (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                44 / 72
~~~

## Page 45

~~~text
Visualisation graphique des auto-corrélations empiriques

    Le «nuage» de points N1 est défini par :
                                  n                                          o
                              N1 = (xj , xj +1 ),         j = 1, . . . , n − 1 .

    Ce nuage constitue une bonne illustration de la valeur de ρbn (1).
    Si cette auto-corrélation est proche de ±1 :
        Le nuage est allongé selon une droite.
        La pente de cette droite a le signe de ρbn (1).

    Le nuage devient plus «arrondi» lorsque ρbn (1) se rapproche de zéro.

    Un raisonnement similaire s’applique en remplaçant ρbn (1) par ρbn (h) pour les nuages
    Nh définis par :
                           n                                       o
                       Nh = (xj , xj +h ),      j = 1, . . . , n − h ,    k = 2, . . . , h .




         (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                45 / 72
~~~

## Page 46

~~~text
Dépendance temporelle dans le trafic SNCF




         Figure – Trafic SNCF : Dépendance entre {xt } et {xt +1 }, {xt +2 }, {xt +3 }, {xt +12 }.

  • On observe :
        Une forte dépendance entre xt et xt +1 ,
        Une dépendance notable entre xt et xt +12 ,
  • Ces observations suggèrent la présence d’une périodicité dans les données.
          (CY Tech)               Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                           9 janvier des
                                                                                                     2025Séries Temporelles
                                                                                                                    46 / 72
~~~

## Page 47

~~~text
Comment utiliser l’auto-corrélation en pratique ?

 ▷ L’auto-corrélation est principalement utilisée sur les séries résiduelles ϵn , qui
   résultent après avoir retiré la tendance et les saisonnalités.
    La démarche habituelle :
         Retirer la tendance détectée dans la série brute, puis, si nécessaire, désaisonnaliser la
         série (voir Cours 2).
         Calculer les auto-covariances empiriques sur la série résiduelle, afin d’établir un modèle
         prédictif pour ces résidus.

    Il est néanmoins utile de comprendre l’allure de l’auto-corrélation sur une série
    brute comportant une tendance ou une saisonnalité. Les propositions suivantes
    illustrent ce comportement.



Proposition 1
Pour une tendance linéaire pure :

                      xj = aj + b ,   j = 1, . . . , n ,       alors pour tout h :

                                 ρbn (h) −→ 1,             quand n → ∞.

          (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  47 / 72
~~~

## Page 48

~~~text
Proposition 2
Pour une série périodique pure de période p :
                                       2j π
                                   µ       ¶
                      xj = a cos            ,   j = 1, . . . , n ,   alors tout h :
                                        p
                                                    2hπ
                                                µ       ¶
                           ρbn (h) −→ cos               ,       quand n → ∞.
                                                     p


  • Ce résultat montre que pour une série assez longue, la périodicité p est visible aussi
    bien dans l’auto-corrélation que dans la série elle-même.

  • Bien qu’une tendance ou une périodicité pure soit rarement rencontrée,
                      ces propositions fournissent des indications utiles pour les séries
                      présentant une composante additive de ces types.




          (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                        9 janvier des
                                                                                                  2025Séries Temporelles
                                                                                                                 48 / 72
~~~

## Page 49

~~~text
Résumé et Exemple

  1   Pour une série longue avec une tendance polynomiale :
           ρbn (h) reste positive et proche de 1 pour des valeurs de h petites par rapport à n.

  2   Pour une série présentant une périodicité :
           Cette périodicité est bien identifiable à travers l’auto-corrélation.

  3   Pour des séries résiduelles :
                       ρbn (h) devient rapidement très petite lorsque h augmente.



□ Exemple : Les graphiques 3.6, 3.7 et 3.8 illustrent :

      L’auto-corrélation empirique des ventes de champagne (série brute),
      Celle de la série différenciée (yn = xn − xn−1 ),
      Celle de la série désaisonnalisée (zn = xn − xn−12 ).




           (CY Tech)              Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                           9 janvier des
                                                                                                     2025Séries Temporelles
                                                                                                                    49 / 72
~~~

## Page 50

~~~text
(CY Tech)   Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                     9 janvier des
                                                                               2025Séries Temporelles
                                                                                              50 / 72
~~~

## Page 51

~~~text
Exemples-Varicelles

Le graphique qui suit représente le nombre de cas de varicelle mensuel de janvier 1931 à
juin 1972.
varicelle<-ts(data$x,start= c(1931,1),end= c(1972,6),freq=12) plot(varicelle)




          (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               51 / 72
~~~

## Page 52

~~~text
▷ Auto-covariance empirique d’ordre h, γb(h) et
▷ Auto-corrélation empirique d’ordre h, ρb(h)
(dépendance entre les données espacées de h pas de temps)
tmp=acf(varicelle,type="cov",plot = FALSE)
tmp= acf(varicelle,type="cor",plot= FALSE)
plot (tmp)




         (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                     9 janvier des
                                                                                               2025Séries Temporelles
                                                                                                              52 / 72
~~~

## Page 53

~~~text
Propriétés de l’autocorrélation- Vérification des Propositions 1 et 2

▷ Si la série (Xt )1≤t ≤n est une tendance linéaire pure : Xt = at + b , alors pour tout h
fixé :
ρbn (h) −→ 1      quand   n → +∞
serie=2*(1 :100)+4
par (mfrow= c (1,2))
plot(ts(serie))
acf (serie)




              (CY Tech)        Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                        9 janvier des
                                                                                                  2025Séries Temporelles
                                                                                                                 53 / 72
~~~

## Page 54

~~~text
▷ Si la série (Xt )1≤t ≤n est une série périodique pure Xt = a cos( 2pπt ), où p est la
période, alors pour tout h fixé :
ρbn (h) −→ cos( 2h π
                 p )   quand       n → +∞




▷ Conclusion :
on retrouve la présence d’une tendance et d’une saisonnalité en examinant les
auto-corrélations.



          (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                        9 janvier des
                                                                                                  2025Séries Temporelles
                                                                                                                 54 / 72
~~~

## Page 55

~~~text
Fonction d’auto-corrélation partielle

Définition 3
L’auto-corrélation partielle empirique d’ordre h est une fonction de h, noté r (h),
    qui quantifié la corrélation entre deux données espacées de h pas de temps, en
    enlevant l’effet des données intermédiaire

tmp= pacf (varicelle,type="cor",plot = FALSE)
plot(tmp)




            (CY Tech)         Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                55 / 72
~~~

## Page 56

~~~text
            Modélisation et Choix du modèle




(CY Tech)       Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                         9 janvier des
                                                                                   2025Séries Temporelles
                                                                                                  56 / 72
~~~

## Page 57

~~~text
Modéliser

▷ Modéliser une série de données afin d’expliquer ses variations à l’aide de peu de
paramètres.
▷ On cherche donc une fonction m, telle que

                      xt = m(xt −1 , xt −2 , . . . , ) + ϵt ,   ϵt représente une erreur.



▷ On cherche (en particulier) à repérer un certain nombre de comportement :

    y a-t-il une tendance générale à la hausse ou à la baisse ?
    y a-t-il des fluctuations répétitives ?
    y a-t-il des phénomènes qui se reproduisent sur des périodes longues ?
    y a-t-il des fluctuations exceptionnelles ?


▷ Les questions posées reviennent à rechercher :
trois types de composantes dans les séries temporelles :



          (CY Tech)                    Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                                9 janvier des
                                                                                                          2025Séries Temporelles
                                                                                                                         57 / 72
~~~

## Page 58

~~~text
Modéliser : Les différentes composantes d’une série (xt )

   La tendance (ou trend) (mt ).
                - Représente l’évolution à long terme de la série (xt ).
                - Elle traduit le comportement "moyen" de la série.
   La composante saisonnière ou saisonnalité (st ).
                 - Les variations saisonnières sont des fluctuations périodiques à
                 l’intérieur d’une année, et qui se reproduisent de façon plus ou moins
                 permanente d’une année sur l’autre (fêtes, vacances, solde, etc)
   Deux principes :
                    • Principe de répétition à l’identique :
                    Les saisonnières sont périodiques de période p (nb de mois) :
                    st +p = st . Il suffit de connaître ses p premières valeurs s1 , s2 , . . . , sp
                    • Principe de conservation des aires :
                    Par an, l’influence des variations saisonnières est nulle.
   La composante résiduelle ou bruit ou résidu (ϵt ).
               - Ce sont des fluctuations irrégulières,
               - en général de faible intensité mais de nature aléatoire (on parle aussi
                 des aléas).


        (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                58 / 72
~~~

## Page 59

~~~text
Modèle Additif

▷ Dans un modèle additif, on suppose que les 3 composantes :
   tendance,
      variations saisonnières
   et variations accidentelles
   sont indépendantes les unes des autres.
▷ On considère que la série xt s’écrit comme la somme de ces 3 composantes :
                             xt = mt + st + ϵt ,       t = 1, 2, . . . , n .                                      (13)

Hypothèses : pour des raisons d’unicité d’écriture du modèle (13), on suppose que :


                                 p
                                 X                      n
                                                        X
                                        sj = 0   et            ϵt = 0                                             (14)
                                 j =1                   t =1

  ⇒      (st ) et (ϵt ) sont centrées
  ⇒ toute l’information concernant la tendance (le comportement "moyen") est
uniquement contenu dans la composante (mt ).


           (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                          9 janvier des
                                                                                                    2025Séries Temporelles
                                                                                                                   59 / 72
~~~

## Page 60

~~~text
Modèle Additif-Remarque

   Composantes de la série.
              - Souvent on rajoute une autre composante : pt : représente les
                perturbations majeures liées à des évènements importants mais qui
                ne se répètent pas et dont l’influence est limitée dans le temps :
                grève des transports, catastrophe naturelle...

                    - Dans le langage de la statistique on parle de points aberrants.

   Concernant les résidus ϵt .
                - Une particularité nouvelle des modèles de séries chronologiques par
                  rapport au modèle linéaire classique est l’importance accordée à la
                  modélisation correcte de ϵt .
                - On ne peut pas se contenter de considérer que ce sont des variables
                  aléatoires indépendantes ; il faut donc prendre en compte la
                  structure de corrélation par des modèles appropriés.




        (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                60 / 72
~~~

## Page 61

~~~text
Reconnaître un Modèle Additif-Graphique

On relie par une courbe d’une part les maxima de la série, d’autre part les minima.

    Si les deux courbes obtenues sont parallèles, le modèle est de type additif

▷ Graphiquement on observe des fluctuations autour de la tendance d’amplitude
constante.




                                   Figure – Modèle Additif




          (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               61 / 72
~~~

## Page 62

~~~text
Modèle Multiplicatif



                              xt = mt × st × ϵt ,       t = 1, . . . , n                                         (15)

▷ L’amplitude de la composante saisonnière et du bruit n’est plus constante.
Elles varient au cours du temps proportionnellement à la tendance mt ⇒
Les moyennes et écarts types calculés sur chaque période augmentent avec le temps.
Hypothèses : pour assurer la cohérence de l’écriture de la décomposition (15), on suppose
                               p
                               X                      1 X n
                                      sj = p   et            ϵ t = 1.
                               j =1                   n t =1

                         En posant                  sj = 1 + sej et ϵt = 1 + ϵet ,
le modèle multiplicatif peut également être défini par :

                                xt = mt × (1 + set ) × (1 + ϵet )                                                (16)


                                                       p
                                                       X                      n
                                                                              X
                      avec les hypothèses :                   sej = 0   et          eet = 0
                                                       j =1                  t =1

          (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  62 / 72
~~~

## Page 63

~~~text
Reconnaître un Modèle Multiplicatif-Graphique

On relie par une courbe d’une part les maxima de la série, d’autre part les minima.

    Si les deux courbes ne sont pas parallèles, le modèle est de type multiplicatif.

▷ graphiquement on observe des fluctuations autour de la tendance d’amplitude variable.




                               Figure – Modèle Multiplicatif




          (CY Tech)          Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                      9 janvier des
                                                                                                2025Séries Temporelles
                                                                                                               63 / 72
~~~

## Page 64

~~~text
Choix du Modèle

• Méthode du Profil :

    On superpose les courbes de la série sur un graphique.
    Interprétation :
         Si les courbes sont parallèles : le modèle est additif.
         Sinon (les pics et creux s’accentuent) : le modèle est multiplicatif.


• Méthode du Tableau de Buys et Ballot :

    Calculs : Pour chaque année, on calcule la moyenne et l’écart type.
    Représentation graphique :
         Abscisse : les moyennes.
         Ordonnée : les écarts types.
    Analyse : On trace la droite des moindres carrés des points.
         Si l’écart type est indépendant de la moyenne :
              Le modèle est additif.
              La pente a de la droite est proche de 0.
         Si l’écart type dépend de la moyenne :
              Le modèle est multiplicatif.
              La pente a de la droite n’est pas nulle.


         (CY Tech)              Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  64 / 72
~~~

## Page 65

~~~text
Différentes Formes de la tendance

.
▷ La tendance reflète la croissance moyenne de la série. Elle peut prendre plusieurs
formes dont les plus courantes sont :

                             Linaire :         m(t) = at + b
                           Parabole :          m(t) = at 2 + bt + c
                         Polynmiale :          m(t) = ap t p + ap −1 t p −1 + . . . + a1 t + a0
                      Exponentielle :          m(t) = a exp(bt) + c
                      Logarithmique :          fθ (t) = a ln(t) + b
                                                                 1
                          Logistique :         mθ (t) =
                                                          b exp(−at) + c
            Double Exponentielle :             m(t) = exp[ae bt + c]




          (CY Tech)              Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                          9 janvier des
                                                                                                    2025Séries Temporelles
                                                                                                                   65 / 72
~~~

## Page 66

~~~text
Différentes formes de la tendance-Exemple

▷ Exemple. Série représente le logarithme de l’indice du New York Stock Exchange.
▷ Trois tendances ont été ajustées : linéaire (en haut à droite), quadratique (en bas à
gauche) et exponentiel (en bas à droite).
- La tendance quadratique est plus adaptée mais il est difficile de lui trouver un sens
physique.
-la tendance linéaire représente une croissance linéaire
- la tendance exponentielle indique une augmentation constante (rapport entre Xt /Xt −1
constant)




          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                66 / 72
~~~

## Page 67

~~~text
Validation du modèle : Examen des résidus

□ Une méthode pour valider la qualité d’un modèle est de regarder si celui-ci reproduit
bien les données observées. On examine donc les résidus,

                          et = xt − m(xt −1 , xt −2 , . . .),      t = 1, . . . , T


Plus les résidus sont petits, plus le modèle est proche des valeurs observées. Il existe
plusieurs fonctions d’erreurs pour mesurer cet écart.


▷ L’écart absolu moyen, noté MAD pour "mean absolute deviation"

                                       1 XT                              1 XT
                        MAD(e) =              | et − e |    où     e=           et
                                       T t =1                            T t =1

▷ Le carré moyen des erreurs, noté MSE pour "mean square error"

                                                       1 XT
                                        MSE(e) =             e2
                                                       T t =1 t

          (CY Tech)             Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  67 / 72
~~~

## Page 68

~~~text
Validation du modèle : Examen des résidus

▷ L’erreur quadratique moyenne, notée RMSE pour "root mean square error"
                                          v
                                             T
                                          u
                                          u1 X
                                RMSE(e) = t    e2
                                                     T t =1 t

L’erreur absolue moyenne, notée MAE pour "mean absolute error",

                                                  1 XT
                                  MAE(e) =               | et |
                                                  T t =1




         (CY Tech)         Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                    9 janvier des
                                                                                              2025Séries Temporelles
                                                                                                             68 / 72
~~~

## Page 69

~~~text
Prévoir

    On dispose des observations xt aux temps 1, . . . , T . Prévoir la valeur de xt à l’horizon
    h.
    La valeur prédite à l’instant t + h est notée xT (h).




▷ La prévision dépend du poids que l’on accorde aux observations passées.



          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                69 / 72
~~~

## Page 70

~~~text
Annexe : mise en œuvre sous R

Quelques fonctions R utiles à l’étude des séries temporelles :

    Avant de charger le fichier dans R, taper l’adresse dans le navigateur pour le
    visualiser.
       - Charger un fichier de données numériques en sautant les k premières lignes (s’il y a du
         texte au début) :
         data=scan(file=”donnee.dat”,skip=k).
       - Définir le répertoire courant :
         setwd(”~/Documents/”) (ici on veut être dans ~/Documents),
       - savoir quel est le répertoire courant : getwd().

    Créer un objet de type série temporelle :
       - serie <- ts (data,start,end,frequency).
       - data contient le vecteur des données (un fichier contenant les données peut être
         mentionné en remplaçant data par file=”donnees.dat”),
       - start et end mentionne les dates de début et de fin de la série (ex : start=c(1990,1)
         et end=c(1999,6) pour des données allant de janvier 90 à juin 99),
       - et enfin frequency mentionne le nombre de données par unité de temps (par exemple,
         si les dates de début et de fin sont des années,
       - et que les données sont mensuelles, il faudra indiquer frequency=12).
       - Découper une série temporelle de c(i,j) à c(k,l) : xd<-window(x,c(i,j),c(k,l)).
       - Transformer une série temporelle en vecteur de nombres : v=as.numeric(cp).



          (CY Tech)           Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                       9 janvier des
                                                                                                 2025Séries Temporelles
                                                                                                                70 / 72
~~~

## Page 71

~~~text
    Représenter graphiquement un objet de type série temporelle : plot.ts(serie).
    La fonction acf(x, lag.max = 10, type = c("correlation", "covariance"),
    plot = TRUE) calcule (et trace si l’option plot est à TRUE) les lag.max premières
    auto-corrélations ou auto-covariances (choisir corrélation OU covariance).

Quelques conseils utiles pour les graphiques en R :

    Pour représenter plusieurs courbes sur le même graphique,
       - tracer la première à l’aide de la commande plot qui créé la fenêtre graphique et y
         insère la courbe,
       - puis tracer les autres courbes à l’aide de la commande lines qui trace une courbe sur
         une fenêtre graphique existante.
    Pour partager la fenêtre graphique en plusieurs (n×p) sous-graphes, utiliser la
    commande par(mfrow=c(n,p)).
    Préciser les limites des axes des graphiques : plot(...,xlim=c(0,10),ylim=c(-10,10)).
    Pour exporter les graphiques en jpeg (idem pour bmp, png), suivez ces étapes :
       1   jpeg(filename=“nomfichier%d.jpeg”),
       2   réaliser le graphique,
       3   la commande dev.off() permet enfin de rediriger le dernier graphique tracé vers le
           fichier nomfichier1.jpeg, et ainsi de suite après chaque graphique. Le nom de fichier
           sera automatiquement incrémenté.
▷ Simulation de variables normales indépendantes : x<-rnorm(n,mean=0,sd=1) renvoie
une suite de variables normales indépendantes de moyenne 0 et d’écart-type 1.
           (CY Tech)            Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                         9 janvier des
                                                                                                   2025Séries Temporelles
                                                                                                                  71 / 72
~~~

## Page 72

~~~text
Références

    Hyndman, R. J., and Athanasopoulos, G. (2013). Forecasting : Principles and
    Practice. OTexts. https://robjhyndman.com/uwafiles/fpp-notes.pdf




         (CY Tech)         Chapitre I. Introduction, Vocabulaire et Statistiques Descriptives
                                                                                    9 janvier des
                                                                                              2025Séries Temporelles
                                                                                                             72 / 72
~~~
