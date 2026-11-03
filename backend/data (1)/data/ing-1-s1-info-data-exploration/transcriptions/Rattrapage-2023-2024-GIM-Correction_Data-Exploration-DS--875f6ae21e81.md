# Rattrapage-2023-2024-GIM-Correction_Data-Exploration-DS.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1tZnGPoEcCgwqgy-uv7VCXJrLl-1m_ejI) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
            Corrigé Rattrapage Data Explo 2024
1. Exercice 1 :
   1) Population, taille : les 209 pays.
      Variables : Espérance de vie et PIB/habitant.
      Nature : les 2 variables sont quantitatives continues.
   2)
        a) Un nuage allongé suivant une ligne droite indiquerait une bonne régression
           linéaire.
        b) Une valeur atypique a tendance à détourner la droite de régression des autres
           points du nuage, et à induire une régression de mauvaise qualité.
        c) L'élimination d'une valeur pourrait révéler d'autres points atypiques qui étaient
           cachés.




   3)
                 3420                            14728
           x=
        a) ⏨                   = 16.36, y⏨=              = 70.47
                    209                           209
                                   126677
           Var(x) = s x2 =                  - (16.36) 2 = 338.34 ⟹ s x =       338.34 = 18.4
                                    209
                                   1058461
           Var(y) = s y2 =                   - (70.47) 2 = 98.54 ⟹ s y =       98.54 = 9.93
                                        209
                                         257436
           Cov(x, y) = c xy =                     - 16.36 × 70.47 = 78.62
                                         209
                        c xy             78.62
        b) r xy =              =                         = 0.43
                    sx sy          338.34 × 98.54
           Ce coefficient est positif, indiquant que le PIB/hab. évolue dans le même sens
           que l'espérance de vie.
           Mais il est plutôt faible. L'espérance de vie n'explique qu'une petite partie de la
           variabilité du PIB/hab.
                 c xy          78.62
        c) a =            =             = 0.232         et   b = y⏨- a x⏨= 70.47 - 0.232 × 16.36 = 66.67
                 s x2          338.34
           L'équation de la droite de régression est : y = 0.232 x + 66.67
        d) Pour x = 15, on obtient : y = 0.232 × 15 + 66.67 = 70.15
           L'epérance de vie serait de 70.15 ans pour un pays au PIB/hab. de 15 milles
           dollars.
~~~

## Page 2

~~~text
   4)
          a) R 2 = 0.02164 ⟹ 2.164 % seulement de la variabilité de l'espérance de vie
             sont expliqués par le PIB/hab.
          b) Le coef de corrélation est la racine carrée positive de R 2 car le coef. a = 3.27 × 10 -5 > 0
             r xy =      0.02164 = 0.147
          c) L'équation de la droite de régression donnée par R est la suivante :
                                          y = 3.27 × 10 -5 x + 75.69
          d) Le coef. de corrélation est passé de 0.43 à 0.147
             La nouvelle droite de régression explique encore moins l'espérance de vie
             qu'avant.
             La régression est encore moins justifiée. Ceci s'explique par le fait que l'on s'est
             limié aux pays les plus riches où les différences d'espérance de vie peuvent
             s'expliquer par des choses bien différentes du PIB/hab., par le système de santé
             par exemple.


2. Exercice 2 :




   1) n 2,1 = 74 conducteurs sont agés de 18 à 30 ans et ont eu un seul accident.
      n ▪,3 = 865 conducteurs sont agés de 41 à 50 ans.
                  338
        f 2,▪ =          = 6.76% des conducteurs ont eu un seul accident.
                  5000
~~~

## Page 3

~~~text
   2)
      La somme de chaque colonne vaut 1, il s'agit donc de profils-colonnes.
   3) Ces profils-colonnes doivent être comparés au profil-colonne moyen obtenu en
      divisant les effectifs marginaux des nombres d'accidents par l'effectif total. On obtient :
           0,9004        0,0676        0,0242         0,0078
   4) Le profil-colonne 18-30 est légèrement différent tout comme celui des >70.
      On peut s'attendre à un faible lien entre âge et nombre d'accidents.




   5)
   6) Ce tableau d'effectifs théoriques est calculé sous l'hypothèse d'indépendance entre
      les 2 variables.
                                            n i,▪ × n ▪,j   total ligne × total colonne
      La formule de calcul est n i,j,theo =               =
                                                 n ▪,▪               effectif total
                                                121 × 812
        L'effectif en gras a été obtenu par :                  = 19.7
                                                  5000
                                                                         2
                                                 (n i,j,theo - n i,j,obs )
   7) La distance du khi2 est donnée par : 𝜒 = ∑  2
                                                                           .
                                                           n i,j,theo
                                                         i,j
   8) Le nombre de degrés de liberté est : (4 - 1)(6 - 1) = 15 d.d.l.
      Le seuil est donc C = 25.00.
      𝜒 2 = 27.57 > C ⟹ Les 2 variables sont liées.


3. Exercice 3 :
~~~

## Page 4

~~~text
1) Si on note oq i les durées de chômage des ouvriers qualifiés, la moyenne est :
       50
   1
       ∑ oqi .
  50 i=1
  Si on note c i les durées de chômage des cadres, et ⏨
                                                      c la moyenne, la variance est
                         n                   n
                   1                     1
  donnée par :          ∑ (c i - ⏨
                                 c ) = ∑ c i2 - (c⏨) 2
                                     2
                   25 i=1                25 i=1
2) La variance intra-classes est donnée par :
                                1
                    Vintra =         (25 × 1.51 + 50 × 5.26 + 75 × 3.15) = 3.58
                               150
3) La variance inter-classes est donnée par :
                   1
       Vinter =          25 × (3.92 - 6.47) 2 + 50 × (7.34 - 6.47) 2 + 75 × (6.74 - 6.47) 2
                  150
                                             Vinter = 1.37
4) La formule de décomposition de la variance assure que :
                                   Vtotale = V intra + Vinter
   Et on a bien : 3.58 + 1.37 ≃ 4.96
                                            Vinter     1.37
5) Le rapport de corrélation donne : R 2 =          =         = 27.6%
                                            Vtotale    4.96
  Conclusion : La catégorie socio-professionnelle explique environ 27.6% de la
  variabilité de la durée de chômage.
~~~
