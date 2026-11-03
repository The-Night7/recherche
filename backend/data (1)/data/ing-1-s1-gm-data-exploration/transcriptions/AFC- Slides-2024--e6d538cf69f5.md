# AFC- Slides-2024.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1UnlqZDES7_AJsB-W47GKMM3Pnw9h8s4h) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                                                                                                                Analyse bivariée AFC




                        Data exploration
            Analyse factorielle des correspondances
L’analyse factorielle des correspondances (AFC) fait suite au chapitre sur le croisement de 2 variables
qualitatives. Si suite à cette études les deux variables sont considérées comme dépendantes, alors on
est en droit de se demander comment?
                                      Y-a-il des modalités qui s’attirent ou se repoussent?
L’ AFC est une méthode descriptive permettant de représenter graphiquement l’essentielle de
l’information contenu dans le tableau de contingence.
                                                                                                                                    CA factor map

  Exemple : Etude des 275 plus importantes




                                                                                               1.0
  industries du numériques réparties selon le




                                                                                               0.8
  continent et le secteur d’activité                                                                                               Telecom




                                                                                               0.6
  Classement effectué par Eurostat, basé sur le capital en 2005
                                                                                                                  services




                                                                              Dim 2 (20.62%)

                                                                                               0.4
                                                                                                                                                                     ASIE




                                                                                               0.2
              Hardware Internet          Services Software         Mobile                                       EUROPE
                                                                  Telecom



                                                                                               0.0
                                                                                                                                             Internet         hardware

AMERIQUE          26            4            15           70        3                                        Software




                                                                                               -0.2
                                                                                                                               AMERIQUE
ASIE              7             1            4            18        1
EUROPE            27            5            16           75        3                          -0.4

                                                                                                      -0.5                   0.0                        0.5              1.0

                                                                                                                                     Dim 1 (79.38%)
~~~

## Page 2

~~~text
                                                                                        Analyse bivariée AFC


                          Analyse factorielle des correspondances
                                    Distribution conjointe


Comme nous l’avons vu dans le chapitre précédent la dépendance entre deux variables qualitatives se
mesure selon trois comparaisons de tableaux
     • Le tableau des effectifs théoriques avec le tableau des effectifs observés
     • Le tableau des profils lignes avec le profil moyen des lignes
     • Le tableau des profils colonnes avec le profil moyen des colonnes
L’AFC va s’intéresser à la structure des écarts qui apparaissent entre ces tableaux




                                                                                                          2
~~~

## Page 3

~~~text
                                                                                                        Analyse bivariée AFC


                             Analyse factorielle des correspondances
                                           Tableaux des effectifs
On rappelle le calcul du tableau des effectifs théoriques,
                                           fij=fi. ×f.j.

              Hardware Internet   Services Software         Mobile    Freq.
                                                           Telecom    Marg.
AMERIQUE       12,00%   1,82%     2,18%     26,55%         0,36%     42,91%    Fréquences
ASIE           6,55%    0,73%     1,45%     1,82%          0,73%     11,27%     observées
EUROPE         3,27%    1,09%     9,09%     30,91%         1,45%     45,82%
Freq. Marg.    21,82%   3,64%     12,73%    59,27%         2,55%     100,00%

                                                                                            On s’intéresse à
                                                                                            l’écart entre ces
              Hardware Internet   Services Software         Mobile    Freq.
                                                                                              deux tableaux
                                                           Telecom    Marg.
AMERIQUE       9,36%    1,56%     5,46%     25,43%         1,09%     42,91%
ASIE           2,46%    0,41%     1,43%     6,68%          0,29%     11,27%     Fréquences
EUROPE         10,00%   1,67%     5,83%     27,16%         1,17%     45,82%     théoriques
Freq. Marg.    21,82%   3,64%     12,73%    59,27%         2,55%     100,00%


                                                                                                                          3
~~~

## Page 4

~~~text
                                                                                                                            Analyse bivariée AFC


                                    Analyse factorielle des correspondances
                                                          Tableaux des effectifs
       Tableau des écarts :                                          Hardware Internet   Services Software       Mobile
                                                                                                                Telecom

                 fij − fi• × f• j                         AMERIQUE      0,28     0,17      -0,60      0,04        -0,67
           eij =                                          ASIE          1,66     0,77       0,01      -0,73        1,53
                     fi• × f• j
                                                          EUROPE       -0,67    -0,35      0,56       0,14        0,25

Cela signifie par exemple qu’il y a 60% d’entreprises américaines dans les services en
moins qu’il ne devrait y en avoir dans le cas de l’indépendance. A contrario, il y a 56%
d’entreprises européennes dans les services en plus que le nombre théorique.
 Remarque :
 • Les écarts positifs prennent des valeurs quelconques (même supérieure à 100%).
 • Les écarts négatifs sont entre -1 et 0 (déficit maximum de 100%)

                                                                                 Dans l’exemple ci-dessus on χ²=59.6 et le seuil
L’information est donc contenue dans l’écart à                                    pour (2-1)*(5-1)=8 d.d.l. est 15,51. Il y a donc
l’indépendance. On mesure l’inertie du                                           une forte dépendance entre les deux variables
tableau à l’aide du chi-deux

          χ2 = n ×   ij
                                (f − f × f )
                                       i•        •j
                                                      2


                        i   j       fi• × f• j                                              Comment
                                                                                         représenter la
L’AFC simple s’intéresse plus particulièrement                                            structure des
à la structure de ces écarts.                                                                écarts ?
                                                                                                                                              4
~~~

## Page 5

~~~text
                                                                                                                             Analyse bivariée AFC


                                   Analyse factorielle des correspondances
                                               Ecarts des profils lignes
            Hardware Internet Services Software Mobile                                   Profils lignes
                                                Telecom                                  Pourcentages par ligne :
AMERIQUE     27,97% 4,24% 5,08% 61,86%           0,85% 100%                                                  nij
ASIE         58,06% 6,45% 12,90% 16,13%          6,45% 100%                                           fj i =
EUROPE       7,14%    2,38% 19,84% 67,46%        3,17% 100%
                                                                                                             ni•
FREQ. MARG. 21,82% 3,64% 12,73% 59,27% 2,55% 100%
                                                                                         où i est la ligne et j la colonne

On considère chaque ligne (continent) comme un individu dans un espace de dimension
5 (le secteur d’activité). Il s’agit alors d’analyser un nuage de points de dimension 5, ce
qui n’est pas sans rappeler le problème de l’ACP.
                                                                                         Remarque : Diviser par la fréquence
La ‘’distance’’ entre deux individus-lignes est définie par,
                                                                  (             )
                                                                                         marginale permet d’attribuer le même
                                                        −
                                                                  2                      poids à chaque colonne. Sinon Software
                                                   fj i    f j i
                               d2 (Li1 , Li2 ) =  1            2                        aurait un poids trop important dans le
                                                 j      f• j                             calcul comparé à Internet

On s’intéresse plus particulièrement à la ‘’distance’’ entre un individu-ligne est le profil
ligne moyen (fréquences marginales lignes).
                                          2                     (0,28 − 0,58)² (0,042− ,065)²
 Dans l’exemple ci-dessus, on a: d (AMERIQUE, ASIE) =               0,22
                                                                              +
                                                                                   0,036
                                                                                              + ... = 0,953

                            (0,28 − 0,22)² (0,042− ,036)²
 d2 (AMERIQUE, Moyenne) =                  +                + ... = 0,077    On constate que l’Asie s’éloigne beaucoup
                                 0,22           0,036                        plus du profil moyen que l’Amérique
                     (0,58 − 0,22)² (0,064− ,036)²
 d2 (ASIE,Moyenne) =               +               + ... = 0,998
                         0,22             0,036
                                                                                                                                               5
~~~

## Page 6

~~~text
                                                                                                                                Analyse bivariée AFC


                                   Analyse factorielle des correspondances
                                        Ecarts des profils colonnes

            Hardware Internet Services Software Mobile Freq.                         Profils colonnes
                                                Telecom Marg.                        Pourcentages par colonne :
                                                                                                         nij
AMERIQUE 55,00%         50,00% 17,14% 44,79%            14,29% 42,91%                             fi j =
ASIE     30,00%         20,00% 11,43% 3,07%             28,57% 11,27%                                    n• j
EUROPE   15,00%         30,00% 71,43% 52,15%            57,14% 45,82%                où i est la ligne et j la colonne
              100,00%    100,00%   100,00%   100,00%     100,00%   100,00%

 On peut procéder de la même façon avec les profiles colonnes. On considère chaque
 colonne (secteur d’activité) comme un individu dans un espace de dimension 3 (le
 continent).
                                                                      (0,55 − 0,50)² (0,3 − 0,2)²
  Dans l’exemple ci-dessus, on a:          d2 (Harware, Internet) =                 +             + ... = 0,14
                                                                          0,43          0,11
                           (0,55 − 0,43)² (0,30 − 0,11)²
 d2 (Hardware, Moyenne) =                 +               + ... = 0,55           On constate que le Hardware est plus éloigné
                               0,43              0,11
                         (0,50 − 0,43)² (0,20 − 0,11)²
                                                                                 du profil colonne moyen que l’Internet
 d2 (Internet,Moyenne) =                +                + ... = 0,13
                              0,43              0,11



  Remarque : il n’existe pas de métrique mesurant la ‘’distance’’ entre une ligne et une colonne



                                                                                                                                                  6
~~~

## Page 7

~~~text
                                                                                                                     Analyse bivariée AFC


                              Analyse factorielle des correspondances
                                                 Lien avec l’ACP
        L’idée est toujours de rechercher les directions de plus grandes dispersion des ces nuages de
   points. La matrice dont on cherche les valeurs propres ici n’a pas de signification particulière comme
   en ACP. Il faut tout d’abord construire le tableau des
La matrice dont on cherche les valeurs propres icifijn'a pas de signification particulière comme en ACP. Elle
s'appelle la matrice de Burt et représente les produits scalaires entre les profils lignes et les profils colonnes.
                                                   i• × f• j
L'objectif est de choisir la combinaison avec de fdimensions    la moins élevée possible, afin de minimiser la perte
   La matrice  en question   est alors constituée des  produits
d'information lors de la projection des données dans un espace   scalaires des profiles
                                                                               lignes2.lignes
                                                                     de dimension       (ou
                                                                                          et colonnes)
                                                                                              et colonnes entre
   elles. On peut montrer que cela revient au même de travailler sur le nuage de points des profils
   lignes ou bien sur celui des profils colonnes.
                                                             Hardware   Internet   Services   Software   Mob. Tel.
                 AMERIQUE ASIE       EUROPE      Hardware      0,34       0,11       0,13      0,30        0,08
   AMERIQUE            0,46   0,23     0,40      Internet      0,11       0,04       0,06      0,13        0,03
   ASIE                0,23   0,23     0,16      Services      0,13       0,06       0,17      0,28        0,07
   EUROPE              0,40   0,16     0,53      Software      0,30       0,13       0,28      0,63        0,11
Valeurs propres : 1.0; 0.172; 0.045              Mob.Tel.      0,08       0,03       0,07      0,11        0,04

              χ²/n=59.6/275=0.22=0.172 + 0.045       Valeurs propres : 1.0; 0.172; 0.045; 6. 2×10⁻¹⁰; - 1. 1×10⁻¹⁰

Le nombre de valeurs propres de la méthode           > res$eig
est le minimum entre le nombre de lignes et le             eigenvalue percentage cumulative percentage
nombre de colonnes. La première valeur                                of variance     of variance
propre est toujours égale à 1. La somme des          dim 1 0.17203917            79.38283          79.38283
autres est égale à χ²/n. Comme pour l’ACP, les       dim 2 0.04468172            20.61717          100.00000
logiciels    retournent      un    tableau    de
pourcentages et pourcentages cumulés mais il                     Les nouveaux axes s’appellent les axes
ne s’agit plus ici de variance expliquée mais de                 factoriels. Le choix du nombre d’axes à
chi-deux expliqué.                                                  retenir se fait comme pour l’ACP
                                                                                                   7                                   7
~~~

## Page 8

~~~text
                                                                                                                                                         Analyse bivariée AFC


                                   Analyse factorielle des correspondances
                                                        Lien avec l’ACP
• Plus la distance euclidienne entre un individu
et l’origine du graphique est grande, plus                                                                           CA factor map

l’individu est éloigné du profil moyen (freq.




                                                                             1.0
marginales)




                                                                             0.8
                                                                                                                   Telecom
                        Software Mobile Freq.




                                                                             0.6
                                 Telecom Marg.
                                                                                                services
            AMERIQUE 44,79%         14,29% 42,91%                                                                    dist=0.7




                                                            Dim 2 (20.62%)

                                                                             0.4
            ASIE      3,07%         28,57% 11,27%                                                                                                    ASIE

            EUROPE   52,15%         57,14% 45,82%




                                                                             0.2
        Remarque : La distance entre un individu ligne et                              EUROPE
                                                                                                                  angle plat



                                                                             0.0
        un individu colonne ne s’interprète pas                                                  dist=0.3    O                                hardware
                                                                                                                             Internet
                                                                                           Software
                                                                             -0.2
• L’angle de sommet O de cotés passant par deux                                                               AMERIQUE
modalités s’interprète de la façon suivante :
                                                                             -0.4




  Angle aigu: les modalités s’attirent
  Angle plat: les modalités se repoussent                                          -0.5                    0.0                         0.5              1.0
   Angle droit: les modalités n’interagissent pas.
                                                                                                                       Dim 1 (79.38%)

        Remarque : Les deux modalités ne sont pas
        nécessairement de la même variable                                                                                                                                 8
~~~
