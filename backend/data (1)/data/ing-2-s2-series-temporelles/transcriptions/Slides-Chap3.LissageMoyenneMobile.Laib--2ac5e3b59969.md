# Slides-Chap3.LissageMoyenneMobile.Laib.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14qr8Cjl0RUnzKVOeJby_kEOV66TCn3xh) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Chapitre III - Désaisonnalisation par la méthode des moyennes mobiles



                                     CY Tech


                               16 janvier 2025




     (CY Tech)       Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                            16 janvier
                                                                                   mobiles
                                                                                       2025   1 / 65
~~~

## Page 2

~~~text
Plan


1   Introduction


2   Filtre Moyenne Mobile


3   Moyenne mobile centrée ou symétrique


4   Application de moyenne mobile symétrique au modèle Additif


5   Désaisonnalisation au moyen d’un filtre du type différence


6   Annexes




           (CY Tech)          Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   2 / 65
~~~

## Page 3

~~~text
                                    Introduction

Plusieurs méthodes ont été proposées pour décomposer des séries chronologiques.
La méthode de moyenne mobile (ou moyenne glissante) est souvent utilisée et sert
à estimer la tendance-cycle.
Ce type de moyenne est généralement utilisé comme méthode de lissage :
    pour examiner des séries chronologiques macroéconomiques (produit intérieur brut,
    emploi ou d’autres),
    pour déterminer les prévisions de ventes.
L’objectif de ce chapitre est de présenter quelques-unes de ces moyennes mobiles.




     (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                16 janvier
                                                                                       mobiles
                                                                                           2025   3 / 65
~~~

## Page 4

~~~text
Introduction - Désaisonnalisation par la méthode des moyennes mobiles

▷ Principe

  • Utiliser des opérateurs "moyennes mobiles" comme des filtres qui annulent
    certaines composantes et en laissent d’autres invariantes.
  • Ces filtres font donc apparaître :
                     - exclusivement la tendance,
                     - et réduisent le "bruit" associé à la composante aléatoire.

▷ Cas des modèles additifs
Soit (Xt ) une série admettant une décomposition :

                              Xt = m(t) + St + ϵt ,        t = 1, . . . , T .


  • Appliquer à Xt une transformation linéaire φ :
        qui conserve m(t),
        annule St ,
        et rend la variance de ϵt faible.




         (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   4 / 65
~~~

## Page 5

~~~text
Plus précisément, notons :

                                 Xt∗ ,    m∗ (t),      St∗ ,    ϵ∗
                                                                 t,

les t ièmes composantes transformées par φ des séries Xt , m(t), St et ϵt .
  - Comme φ est linéaire, on obtient :
                                         Xt∗ = m∗ (t) + St∗ + ϵ∗t ;

  - D’autre part, φ annule la saisonnalité : St∗ = 0,
  - Rend la variance de la perturbation ϵ∗t faible,
  - Et conserve la tendance : m∗ (t) = m(t).


Ainsi, la série (Xt∗ ) transformée de la série initiale est donc approximativement
confondue avec la tendance m(t).




     (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                 16 janvier
                                                                                        mobiles
                                                                                            2025   5 / 65
~~~

## Page 6

~~~text
Introduction : Les méthodes de filtre ou de lissage

□ Le lissage par moyennes mobiles, appelé “moving average” (MA), est l’un des filtres les
plus utilisés.

Principe :
    Cette méthode repose sur des régressions locales, réalisées selon les étapes
    suivantes :
         Ajuster des polynômes sur des intervalles glissants, qui se décalent d’un point à chaque
         itération.
         Au centre de chaque intervalle, la donnée lissée correspond à la valeur du polynôme
         ajusté.
         Ces régressions locales sont équivalentes à l’application de moyennes mobiles.


Avantages :

    Permet d’éliminer les irrégularités dans la série avant d’effectuer un ajustement
    analytique.
    Produit une série transformée plus facile à interpréter.

Question clé : Quel type de moyenne mobile faut-il appliquer pour obtenir les meilleurs
résultats ?

             (CY Tech)         Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   6 / 65
~~~

## Page 7

~~~text
            Filtre Moyenne Mobile : F-MM




(CY Tech)     Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                     16 janvier
                                                                            mobiles
                                                                                2025   7 / 65
~~~

## Page 8

~~~text
Filtre Moyenne Mobile : F-MM

Définition 1
Soit (Xt )1≤i ≤T une chronique observée. La chronique Yt = M(Xt ), transformée de Xt
par un filtre moyenne mobile (MM), est définie par
         m
         X2
 Yt =            θi Xt +i = θ−m1 Xt −m1 + . . . + θ−1 Xt −1 + θ0 Xt + θ1 Xt +1 + . . . + θm2 Xt +m2 ,         (1)
        i =−m1

 où m1 + 1 ≤ t ≤ T − m2 , θi ∈ R
Le nombre de points m1 + m2 + 1 est appelée ordre de la moyenne mobile.


    Il s’agit d’une combinaison linéaire d’instants passés et futurs de la série initiale.
    La valeur à l’instant t de la série brute est donc remplacée par une
                                      série moyenne Yt := M(Xt )
    pondérée :
                        - de m1 valeurs "passées" de la série,
                        - de la valeur actuelle
                        - et de m2 valeurs "futures" de la série.
    Le calcul précédent a du sens uniquement lorsque : m1 + 1 ≤ t ≤ T − m2 .

           (CY Tech)                 Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                            16 janvier
                                                                                                   mobiles
                                                                                                       2025   8 / 65
~~~

## Page 9

~~~text
Filtre Moyenne Mobile et Prévision

□ Remarque Importante

    Les m1 premiers points et les m2 derniers points de la série brute ne peuvent pas
    être transformés par l’opérateur M.
    La méthode des moyennes mobiles (MM) présente un inconvénient majeur si l’on
    souhaite l’utiliser pour faire des prévisions.
      - En effet, considérons par exemple une moyenne mobile centrée (m1 = m2 ). Dans ce cas,
        les m observations les plus récentes, Xn−m+1 , . . . , Xn , ne peuvent pas être lissées,
      - et donc n’interviendront pas dans l’estimation de la tendance,
      - alors que, a priori, ces observations sont les plus importantes pour prévoir les valeurs
        futures.

    Les procédures basées sur les moyennes mobiles sont principalement utilisées pour
    la désaisonnalisation et non pour la prévision.
    Ces méthodes permettent d’obtenir la tendance et la saisonnalité d’une série ainsi
    qu’une série corrigée des variations saisonnières.




         (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   9 / 65
~~~

## Page 10

~~~text
Classement des moyennes mobiles
        Pm2
   Si     i =−m1 i
                   θ = 1,
        - La moyenne mobile est dite normalisée,
           (il s’agit d’une moyenne arithmétique au sens habituel).

   Lorsque m1 = m2 ,
        - La moyenne mobile est dite centrée,
          (on prend en compte autant d’instants passés que futurs). On note MMC.

   Si, en outre, on a θ−i = θi pour tout i, la moyenne mobile est dite :
        - Symétrique ou moyenne arithmétique symétrique,

        - C’est-à-dire, les poids sont symétriques,
          (on donne des poids similaires aux instants passés et futurs de même ordre).
        - Une moyenne mobile est symétrique si et seulement si le polynôme :
                                    Θ(B) = θ−m + θ−m+ 1 B + . . . + θm B 2m ,
          associé est symétrique,
          où B est l’opérateur retard. On note MMS.




          (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                       16 janvier
                                                                                              mobiles
                                                                                                  2025   10 / 65
~~~

## Page 11

~~~text
Classement des moyennes mobiles - Exemples

   Exemple 1 : Considérons la moyenne mobile suivante :
       M1 (Xt ) = 12 (Xt + Xt −1 ), avec
       M1 = 12 (I + B) = 12 B[I + F ],
   où B représente l’opérateur retard (BXt = Xt −1 ) et F = B −1 l’opérateur avance
   (FXt = Xt +1 ).
   ▷ Elle est d’ordre 2 dont le polynôme caractéristique est de degré 1. Elle n’est ni
   centrée ni symétrique. En effet
                a) Ordre et polynôme caractéristique :
                          L’ordre est défini par le nombre total de termes impliqués dans la
                          somme, ici m1 + m2 + 1 = 1 + 0 + 1 = 2.
                          Le polynôme caractéristique associé est donné par Θ(B) = 12 (1 + B),
                          qui est de degré 1 (le plus grand exposant de B est 1).

                b) Non centrée et non symétrique :
                          Cette moyenne mobile utilise une observation passée (Xt −1 ) et
                          l’observation actuelle (Xt ), mais pas d’observation future. Cela
                          signifie qu’elle n’est pas centrée.




        (CY Tech)              Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   11 / 65
~~~

## Page 12

~~~text
    Exemple 2 : Considérons maintenant une autre moyenne mobile :
         M2 (Xt ) = 14 (Xt −1 + 2Xt + Xt +1 ),
         qui peut également s’écrire : M2 = 1i =−1 θi B −i = 14 (B + 2I + B −1 ) = 14 B[I + 2F + F 2 ].
                                               P

                  a) Ordre et symétrie des poids :
                            Les paramètres sont m1 = m2 = 1, ce qui donne un ordre total de
                            m1 + m2 + 1 = 3.
                            Les poids associés sont θ−1 = θ1 = 14 et θ0 = 42 , ce qui montre que
                            θ−i = θi . Les poids sont donc symétriques.
                  b) Centrée et symétrique :
                            Étant donné que m1 = m2 , cette moyenne mobile prend en compte
                            autant d’instants passés (Xt −1 ) que futurs (Xt +1 ). Elle est donc
                            centrée.
                            Par ailleurs, la symétrie des poids implique qu’il s’agit également
                            d’une moyenne mobile symétrique. Elle satisfait donc les deux critères.


▷ Remarque : Les moyennes mobiles centrées et symétriques sont nécessairement
d’ordre impair.
Justification : Pour être centrées, elles doivent inclure un nombre égal d’observations
passées et futures autour de t, plus l’observation actuelle Xt . Cela nécessite m1 + m2 + 1
termes, qui est toujours un nombre impair.


          (CY Tech)              Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                        16 janvier
                                                                                               mobiles
                                                                                                   2025   12 / 65
~~~

## Page 13

~~~text
            Moyenne mobile centrée (symétrique)-MMS




(CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                           16 janvier
                                                                                  mobiles
                                                                                      2025   13 / 65
~~~

## Page 14

~~~text
Moyenne mobile centrée (symétrique)-MMS

▷ On va s’intéresser plus particulièrement au Moyenne mobile symétrique simple

             - en supposant que celle-ci conserve les constantes, i.e.,
                                                                                         Pm
                                                                                                θ = 1, et
                                                                                           i =−m i
               on étudié le cas d’ordre impair et cas d’ordre pair.

▷ L’intérêt de MMS.

  - L’objectif de lissage moyenne mobile est d’ajuster un même polynôme à toutes les
    observations, cela peut conduire à retenir un degré assez élevé, par conséquent :

  - L’estimation de ses nombreux paramètres risque d’être peu précise.

  • D’où l’idée est de faire un ajustement local, c’est-à-dire,

       - si l’on observe que le comportement de la série au voisinage d’un point est assez
         régulier, on estime alors la tendance en ce point par une moyenne pondérée des
         observations qui l’entourent.

       - Comme les résidus sont centrée, cette méthode conduit alors à atténuer
         considérablement leur influence, et donc rendre la série plus lisse.




         (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   14 / 65
~~~

## Page 15

~~~text
Moyenne mobile symétrique : m1 = m2 = m et θ−i = θi

Définition 2
Soit (Xt )1≤t ≤T une chronique observée. La chronique Yt , transformée de Xt par un filtre
moyenne mobile (M) centrée, est définie par :
        m                                                      m
                                                                     θk F k (Xt ),      m+1 ≤ t ≤ T −m       (2)
        X                                                      X
Yt =           θk Xt +k   ⇐⇒       Yt = M2m+1 (Xt ) =
       k =−m                                                 k =−m




• Lorsque, pour tout k, θk = p1 où p = 2m + 1, on définit la moyenne mobile simple
(arithmétique) d’ordre p :
                               1
                  Mp (Xt ) =     [Xt −m + . . . + Xt −1 + Xt + Xt +1 + . . . + Xt +m ]
                               p

  - Une moyenne mobile est calculée autour du temps t, ce qui signifie :
        - L’estimation de la tendance au temps t est obtenue en calculant la moyenne pondérée
          des valeurs de la série sur m périodes avant et après t.



            (CY Tech)               Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                           16 janvier
                                                                                                  mobiles
                                                                                                      2025   15 / 65
~~~

## Page 16

~~~text
- Pour p = 3, en considérant un instant avant (Xt −1 ) et un instant après (Xt +1 ), on
  calcule une moyenne mobile sur trois termes :

                                            1
                              M3 (Xt ) =      (X   + Xt + Xt +1 ).
                                            3 t −1

- Les caractéristiques d’une moyenne mobile symétrique (MMS) sont notées :

                            M = [2m + 1];          [θm , θm−1 , . . . , θ0 ]
                                  ©                                        ª


     - [2m + 1] désigne l’ordre de la moyenne mobile, qui correspond au nombre total de points
       pris en compte (par exemple, p = 2m + 1 = 3 pour une moyenne mobile sur 3 termes).
     - [θm , θm−1 , . . . , θ0 ] représente les coefficients de pondération associés aux termes de la
       série :
          - θ0 est le poids attribué à Xt (l’observation centrale).
          - θm est le poids attribué à Xt +m et Xt −m .
     - En pratique, ces coefficients permettent de donner plus ou moins d’importance aux
       observations dans le calcul de la moyenne. Pour une MMS simple, tous les coefficients
       sont égaux, par exemple θk = 31 pour p = 3.




       (CY Tech)               Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   16 / 65
~~~

## Page 17

~~~text
Les moyennes mobiles simples : Exemple 1

▷ Calcul d’une moyenne mobile arithmétique d’ordre p = 3. Notons Yt = Mp (Xt )
 Date t    Série Xt     Date de la série : Yt                Valeur de Yt
   1           5
   2           3           (1+2+3)/3= 2                    (5+3+4)/3=4
   3           4           (2+3+4)/3=3                     (3+4+5)/3=4
   4           5           (3+4+5)/3=4                    (4+5+4)/3=4.33
   5           4           (4+5+6)/3=5                    (5+4+4)/3=4.33
   6           4

    Lorsque l’ordre est impair, p = 2m + 1, la série des moyennes mobiles Mp (Xt ) est
    calculée aux mêmes instants que les observations initiales.
    En d’autres termes : si l’ordre p = 2m + 1,
       - alors la série des moyennes mobiles est calculée aux instants d’observations
                                 tm+1 , . . . , tT −m ,   i .e .,   (tj )j =m+1,...,T −m .

 ▷ Cette moyenne mobile :
       - est symétrique, car les coefficients de pondération sont égaux : θk = p1 = 13 .
       - d’ordre impair (p = 3), les moyennes mobiles sont centrées sur les dates
         correspondantes.

          (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                       16 janvier
                                                                                              mobiles
                                                                                                  2025   17 / 65
~~~

## Page 18

~~~text
Les moyennes mobiles simples : Exemples 2
▷ Calcul d’une Moyenne Mobile d’ordre pair p = 2. Notons Yt = Mp (Xt ) :

                      Date t   Série Xt        Date Yt                 Valeur de Yt
                        1          5        (1 + 2)/2 = 1.5            (5 + 3)/2 = 4
                        2          3        (2 + 3)/2 = 2.5           (3 + 4)/2 = 3.5
                        3          4        (3 + 4)/2 = 3.5         (4 + 3, 5)/2 = 3.75
                        4        3. 5       (4 + 5)/2 = 4.5         (3, 5 + 4)/2 = 3.75
                        5          4        (5 + 6)/2 = 5.5            (4 + 4)/2 = 4
                        6          4

    Lorsque l’ordre est pair, p = 2m, la moyenne mobile est calculée entre les dates
    d’observations. Ainsi :
       • prendre une moyenne arithmétique sur 2m valeurs ne permet pas d’avoir la symétrie
         des dates par rapport à t.
       • Si l’on veut comparer la série lissée avec la série initiale, on a besoin d’avoir les valeurs
         de la série lissée pour les mêmes dates d’observations
       • De plus, les périodes étant la plupart du temps paires (p = 4, p = 12, ..), on doit donc
         définir des moyennes mobiles centrées d’ordre pair :



          (CY Tech)              Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                        16 janvier
                                                                                               mobiles
                                                                                                   2025   18 / 65
~~~

## Page 19

~~~text
Exemple 3 : Ventes annuelles d’électricité : Australie du Sud. 1989–2008

autoplot(elecsales) + xlab("Year") + ylab("GWh") + ggtitle("Annual electricity sales :
South Australia")




     Figure – 1. Ventes résidentielles d’électricité pour l’Australie-Méridionale : 1989-2008

▷ La figure 1 montre le volume d’électricité vendu aux clients résidentiels en
Australie-Méridionale chaque année de 1989 à 2008 (les ventes d’eau chaude ont été
exclues).




          (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   19 / 65
~~~

## Page 20

~~~text
Tableau 1 : Ventes annuelles d’électricité aux clients résidentiels en Australie-Méridionale.
1989–2008.
 Années     Ventes (GWh)       5-MA
  1989         2354.34
  1990         2379.71
  1991         2318.52        2381.53
  1992         2468.99        2424.56
  1993         2386.09        2463.76
  1994         2569.47        2552.60
  1995         2575.72        2627.70
  1996         2762.72        2750.62
  1997         2844.50        2858.35
  1998         3000.70        3014.70
  1999         3108.10        3077.30
  2000         3357.50        3144.52
  2001         3075.70        3188.70
  2002         3180.60        3202.32
  2003         3221.60        3216.94
  2004         3176.20        3307.30
  2005         3430.60        3398.75
  2006         3527.48        3485.43
  2007         3637.89
  2008         3655.00
          (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   20 / 65
~~~

## Page 21

~~~text
▷ La dernière colonne 5-AM du tableau indique une moyenne mobile d’ordre 5. Elle
fournie une estimation de la tendance.

    La première valeur de cette colonne est la moyenne des cinq premières observations
    (1989-1993) ;
    la deuxième valeur est la moyenne des valeurs pour 1990-1994 ; etc.
                 - Chaque valeur dans la colonne 5-MA est la moyenne des
                   observations de cinq ans centrée sur l’année correspondante.
                      - Dans la notation du cours, la colonne 5-MA contient les valeurs de
                        M5 (X )t estimation de la tendance avec m = 2 et p = 2m + 1 = 5.
                      - Cela se calcule en utilisant
                        ma(elecsales, 5)

▷ Il n’y a pas de valeurs ni pour les deux premières années ni pour les deux dernières
années, car nous n’avons pas deux observations de part et d’autre.
▷ Pour voir à quoi ressemble l’estimation de la tendance, nous la traçons avec les
données d’origine




          (CY Tech)              Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                        16 janvier
                                                                                               mobiles
                                                                                                   2025   21 / 65
~~~

## Page 22

~~~text
Figure – 2. Ventes d’électricité résidentielles (noir) avec l’estimation 5-MA de la
tendance-cycle (rouge)


▷ On remarque que

              - la tendance-cycle (en rouge) est plus lisse que les données d’origine et
                capture le mouvement principal de la série.
              - L’ordre de la moyenne mobile détermine la régularité de l’estimation de la
                tendance-cycle.
              - En général, un ordre plus grand signifie une courbe plus lisse


          (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   22 / 65
~~~

## Page 23

~~~text
Impact de l’ordre de la moyenne mobile sur les ventes d’électricité
résidentielle




Figure – 3. Différentes moyennes mobiles appliquées aux données sur les ventes d’électricité
résidentielles
     Les moyennes mobiles simples sont généralement d’ordre impair (p = 2m + 1) (3, 5,
     7, etc.), assurant leur symétrie. Dans ce cas : l’observation centrale est moyennée
     avec m observations de chaque côté.
     Si p est pair, la moyenne mobile perdrait cette symétrie.
           (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                       16 janvier
                                                                                              mobiles
                                                                                                  2025   23 / 65
~~~

## Page 24

~~~text
Application de moyenne mobile symétrique (MMS) au modèle Additif




     (CY Tech)      Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                           16 janvier
                                                                                  mobiles
                                                                                      2025   24 / 65
~~~

## Page 25

~~~text
Application de la moyenne mobile symétrique au modèle additif

▷ Supposons que le modèle s’écrit :

                        Xt = Ψ(t) + ϵt      avec      Ψ(t) = m(t) + S(t),
où

     Ψ(t) représente la tendance m(t) additionnée à la composante saisonnière S(t),
     Les résidus ϵt sont centrés, non corrélés et de variance constante σ2 .

Filtrage avec une moyenne mobile symétrique

     Lorsqu’on applique le filtre M2m+1 , la valeur lissée Yt s’exprime comme :
                                                       m
                                                             θk Ψ(t + k) + ϵ∗                          (3)
                                                       X
                           Yt = M2m+1 (Xt ) =                               t,
                                                     k =−m
     avec
                                                   m
                                          ϵ∗
                                                   X
                                           t =           θk ϵt +k .
                                                 k =−m



            (CY Tech)         Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   25 / 65
~~~

## Page 26

~~~text
Hypothèse de régularité locale :

              • Les valeurs de m(t + k) sont proches de m(t) pour de petites valeurs de
                k :
                                                   m(t + k) ≃ m(t)
              • L’espérance de Yt est proche de m(t), à condition que le filtre M2m+1
                ait bien annulé la composante saisonnière :

                                                     E(Yt ) ≃ m(t).

    Ainsi, les deux chroniques Xt et Yt auront à peu près la même suite de valeurs
    moyennes, mais avec une dispersion plus faible pour la suite moyenne mobile.

▷ En effet, les résidus ϵ∗t sont encore centrés mais de variance :
                                                        m
                                    Var(ϵ∗t ) = σ2            θk2
                                                        X

                                                      k =−m

▷ Pour atténuer cette composante résiduelle, on choisit :
                                             m
                                                   θk2 < 1
                                             X

                                           k =−m


          (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   26 / 65
~~~

## Page 27

~~~text
Application au modèle additif - Réduction de la variance du bruit

▷ Inconvénient :
Les résidus transformés (ϵ∗t ) sont corrélés dans le temps (cet effet est appelé « effet de
Slutsky-Yule »). En effet :


                 ³             ´         ³        ´  m              m
            Cov ϵ∗t , ϵ∗t +h            E ϵ∗  ∗
                                                                    θk θℓ E (ϵt +k ϵt +h+ℓ )
                                                     X              X
                                   =       t ϵt +h =
                                                      k =−m ℓ=−m
                                              m        m
                                        σ2                 θℓ δkh+ℓ
                                             X         X
                                   =              θk
                                           k =−m     ℓ=−m
                                        (
                                           σ2 m           θ θ        si 0 ≤ h ≤ 2m,
                                               P
                                   =             k =−m+h k k −h
                                            0                               si h ≥ 2m + 1.

▷ Cette corrélation entre 2m termes consécutifs du processus (ϵ∗t ) introduit des
oscillations parasites.
▷ Il est impossible de les éliminer mais on peut les atténuer en réduisant la variance
résiduelle.



          (CY Tech)                Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                          16 janvier
                                                                                                 mobiles
                                                                                                     2025   27 / 65
~~~

## Page 28

~~~text
Application au modèle additif - Réduction de la variance du bruit

▷ On peut chercher le lissage optimal qui minimise la variance de la série lissée. Il faut
donc résoudre le problème suivant :
                                      2
                             Pm
                          min k =−m θk
                         

                          sous la contrainte
                                                        Pm
                                                                  θ =1
                                                             k =−m k


  • En utilisant le multiplicateur de Lagrange λ, la fonction à minimiser s’écrit :
                                                Ã             !
                                       m            m
                                 R=
                                       X    2
                                           θ −λ
                                                   X
                                                        θ −1
                                                 k                 k
                                       k =−m             k =−m

  • Les conditions nécessaires du premier ordre s’écrivent :

                                           ∂R
                                                 = 2θ k − λ = 0
                                           ∂θk

  • Ces équations ont pour solution :
                                                         λ
                                                  θk =                                                 (4)
                                                         2


          (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   28 / 65
~~~

## Page 29

~~~text
▷ La matrice des dérivées secondes est 2I , où I est la matrice identité :

    C’est une matrice diagonale définie positive,
    Donc, cette solution correspond bien à un minimum pour R.

▷ En tenant compte de la contrainte sur les θk , il vient, à partir de l’équation (4) :
         m                                  λ                      λ         1
               θk = 1        1 = (2m + 1)
         X
                        =⇒                         =⇒      θk =        =          ,    −m ≤ k ≤ m.
       k =−m                                2                      2       2m + 1


Proposition 1 (Lissage optimal)
Le lissage MMS optimal transforme la chronique Xt en la chronique Yt donnée par :
                                        1       m
                                                                   m + 1 ≤ t ≤ T − m.                  (5)
                                               X
                 Yt = M2m+1 (Xt ) =               X     ,
                                      2m + 1 k =−m t +k

Ce lissage est obtenu lorsque les coefficients sont égaux, c’est-à-dire :
                                                               1
                               ∀ i ∈ [−m, m],         θi =          .
                                                             2m + 1




          (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   29 / 65
~~~

## Page 30

~~~text
                            h              1            1 i
            On note   M = 2m + 1,               ,...,        ,              où
                                         2m + 1       2m + 1


    - M représente une notation condensée du filtre de moyenne mobile à
      2m + 1 termes.
    - Le premier élément (2m + 1) indique le nombre total de termes dans la
      fenêtre,
    - tandis que chaque coefficient 2m1+1 correspond au poids égal attribué à
      chaque terme de la série considérée.




(CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                             16 janvier
                                                                                    mobiles
                                                                                        2025   30 / 65
~~~

## Page 31

~~~text
Corollaire 1
▷ La variance des résidus transformés après lissage est bien diminuée, et on a :

                                                          σ2
                                          Var (ϵ∗t ) =
                                                         2m + 1

▷ Cependant, ces résidus sont corrélés, avec :
                       ³           ´ 2m + 1 − h
                   Cov ϵ∗t , ϵ∗t +h =           σ2              0 ≤ h ≤ 2m         =⇒
                                      (2m + 1)2
                                            (
                           ³          ´
                                                1 − 2mh+1          si 0 ≤ h ≤ 2m,
                      Corr ϵ∗t , ϵ∗t +h =
                                                0                  si 2m + 1 ≤ h.

Corollaire 2 (Transformation du bruit blanc)
    Le facteur de réduction du bruit ϵ∗t = M(ϵt ) est égal à :
                                                     1
                                                          .
                                                   2m + 1
    L’autocorrélation est égale à :
                                          2m + 1 − h
                               ρ (h) =                    si − 2m < h < 2m.
                                           2m + 1
          (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                       16 janvier
                                                                                              mobiles
                                                                                                  2025   31 / 65
~~~

## Page 32

~~~text
Application au modèle additif : Lissage Optimal - Exemples




(CY Tech)       Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                       16 janvier
                                                                              mobiles
                                                                                  2025   32 / 65
~~~

## Page 33

~~~text
Lissage MM Optimal : Application à la série Xt = at + b


    Ce filtre laisse inchangées les séries linéaires de la forme Xt = at + b.
    En effet, appliquons la moyenne mobile d’ordre 2m + 1 :
                                           1      Xm
                      M2m+1 (Xt ) =                  X
                                         2m + 1 k =−m t +k
                                           1      Xm
                                     =                (a(t + k) + b)
                                         2m + 1 k =−m
                                           a       m              b       m
                                                                             1.
                                                  X                      X
                                     =                (t + k) +
                                         2m + 1 k =−m           2m + 1 k =−m

    Calculons chaque terme :
         Pm
                 k = 0, car les indices sont symétriques autour de 0.
         Pkm=−m
           k =−m
                 1 = 2m + 1, car il y a 2m + 1 termes dans la somme.
    Ainsi, on obtient :

                                         M2m+1 (Xt ) = at + b .

    Cela montre que M2m+1 (Xt ) = Xt , donc les séries linéaires de la forme Xt = at + b
    traversent le filtre sans modification.

         (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   33 / 65
~~~

## Page 34

~~~text
Lissage MM Optimal : Application au cas général

    Plus généralement :
      • Toutes les séries X telles que M2m+1 (X ) = X sont préservées intactes par le filtre.

    D’autre part :
      • Toutes les séries qui sont bloquées par le filtre vérifient :
                                                    M2m+1 (X ) = 0.

    Séries bloquées par le filtre :
         Une série est bloquée par le filtre si M2m+1 (X ) = 0.
         Ces séries sont périodiques de période 2m + 1, car leurs oscillations sont telles que les
         termes symétriques autour de t s’annulent :
                                                   1      Xm
                                                             X     = 0.
                                                 2m + 1 k =−m t +k
         Elles peuvent s’exprimer sous la forme générale :
                                      m
                                      X
                                             µ
                                                       2π j              2π j
                                                                                 ¶
                               Xt =          Aj cos          t + Bj sin        t ,
                                      j =1            2m + 1            2m + 1

         où Aj , Bj ∈ R.




         (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   34 / 65
~~~

## Page 35

~~~text
            Le filtre moyenne mobile d’ordre pair




(CY Tech)        Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                        16 janvier
                                                                               mobiles
                                                                                   2025   35 / 65
~~~

## Page 36

~~~text
Le filtre moyenne mobile d’ordre pair

    Nous avons vu que le filtre moyenne mobile à coefficients tous égaux permet
    d’éliminer une composante saisonnière dont la période est égale à l’ordre 2m + 1.
    En revanche, il est impossible d’annuler une périodicité paire avec une moyenne
    mobile d’ordre pair.
    Cependant, on peut utiliser une moyenne mobile "presque" symétrique pour annuler
    une périodicité paire.
    Pour ce faire, on utilise une moyenne mobile d’ordre 2m, mais appliquée à 2m + 1
    observations, où les observations extrêmes sont affectées d’un poids moitié par
    rapport aux autres.
      • Les coefficients de cette moyenne mobile sont donnés par :
                                      h        1    1       1 i
                                  M = 2m + 1,     ,   ,...,       =⇒
                                                   4m 2m           2m




         (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                    16 janvier
                                                                                           mobiles
                                                                                               2025   36 / 65
~~~

## Page 37

~~~text
  • La transformation est donnée par :

                                 1 1                                      1
                                    ·                                            ¸
            Yt = M2m (Xt ) =           Xt −m + Xt −m+1 + . . . + Xt +m−1 + Xt +m
                                          2m 2                                                 2
                                           1 h            −1
                                                         mX                  i
                                  =           Xt −m +         2Xt +k + Xt +m
                                          4m          k =−m+1
                                           1 h1             −1
                                                           mX          1     i
                                  =             Xt −m +         Xt +k + Xt +m .
                                          2m 2          k =−m+1        2

▷ Remarque. Pour une moyenne mobile d’ordre 2m, avec 2m + 1 observations :
         h                            i
Poids = 2m + 1, 41m , 21m , . . . , 21m , cela signifié que :

                 - Les deux observations les plus extrêmes (à gauche et à droite) sont
                   pondérées par 41m , soit la moitié du poids central
                 - Toutes les autres observations reçoivent le poids 21m .




             (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                         16 janvier
                                                                                                mobiles
                                                                                                    2025   37 / 65
~~~

## Page 38

~~~text
Exemple : MM12

 • Pour des données mensuelles, le filtre moyenne mobile MM12 est appliqué sur 13
   observations successives, avec des poids spécifiques :
                                1
            Yt = MM12 (Xt ) =     (X     + 2Xt −5 + . . . + 2Xt + . . . + 2Xt +5 + Xt +6 )
                               24 µ t −6
                               1 1                                               1
                                                                                         ¶
                             =       Xt −6 + Xt −5 + . . . + Xt + . . . + Xt +5 + Xt +6 .
                               12 2                                              2

 • Les coefficients du filtre sont tels que :
                                                                       2 = 1 .
      · Les observations centrales (de t − 5 à t + 5) ont un poids de 24   12
                                                                           1 .
      · Les observations extrêmes (t − 6 et t + 6) ont un poids réduit de 24
 • La somme totale des poids est égale à 1, garantissant que le filtre réalise bien une
   moyenne.




         (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                    16 janvier
                                                                                           mobiles
                                                                                               2025   38 / 65
~~~

## Page 39

~~~text
Remarque 1
Hypothèses nécessaires pour appliquer ce filtre :
 (i) Tendance sensiblement linéaire, sinon elle pourrait être modifiée par le filtre.
(ii) Composante saisonnière rigide, avec une période fixe égale à l’ordre de l’opérateur
     moyenne mobile.
(iii) Aléas de faible amplitude, car les résidus corrigés (autocorrélés) pourraient
      introduire des oscillations parasites (effet Yule-Slutsky).

Résultats attendus :

    La série filtrée Yt constitue une estimation de la tendance m(t).
    La composante saisonnière peut être estimée par :
         Xt − Yt pour un modèle additif.
         Xt /Yt pour un modèle multiplicatif.




          (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   39 / 65
~~~

## Page 40

~~~text
(CY Tech)   Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                   16 janvier
                                                                          mobiles
                                                                              2025   40 / 65
~~~

## Page 41

~~~text
Moyennes Mobiles Arithmétiques (Symétriques) - Résumé et
                       Exemples

Considérons des moyennes mobiles centrées qui conservent les constantes,
c’est-à-dire telles que m     θ = 1, et qui minimisent :
                       P
                         i =−m i

                  le rapport de réduction de la variance                       θ2 .
                                                                     Pm
                                                                        i =−m i
La solution optimale est donnée par : θi = 2m1+1 .




     (CY Tech)           Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                16 janvier
                                                                                       mobiles
                                                                                           2025   41 / 65
~~~

## Page 42

~~~text
Définition des Moyennes Mobiles

Moyenne Mobile d’Ordre Impair (p = 2m + 1) :
                                          1       m
                                                                    m + 1 ≤ t ≤ T − m.
                                                 X
                     Yt = Mp (Xt ) =                X ,
                                        2m + 1 i =−m t +i
                                        h              1      1             1 i
                            Poids = 2m + 1,                ,        ,...,         .
                                                    |2m + 1 2m +{z1       2m + 1}
                                                           2m+1 coefficients


    Conserve les constantes : θi = 1.
                                   P

    Supprime les composantes saisonnières de période p.
Moyenne Mobile d’Ordre Pair (p = 2m) :
                                                 −1
                                        "                                            #
                                 1 1            mX          1
                           Yt =      Xt −m +         Xt +i + Xt +m .
                                2m 2         i =−m+1        2
                                  h 1  1        1 1 i
                        Poids =         ,,...,   ,   .
                                   4m 2m       2m 4m

    Considérée comme une moyenne d’ordre pair mais appliquée sur 2m + 1 observations.
    Supprime les composantes saisonnières de période 2m.
         (CY Tech)                Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                         16 janvier
                                                                                                mobiles
                                                                                                    2025   42 / 65
~~~

## Page 43

~~~text
Avantages et Inconvénients des Moyennes Mobiles

 □ Inconvénients des moyennes mobiles :
        Perte de données : Si on dispose d’une série de n années contenant p mois chacune
        (np observations),
                        - on ne pourra calculer une estimation de la tendance que pour
                          np − p + 1 ou np − p mois (selon la parité de p),
                        - soit une année de moins que la série.
        .
        Le choix de l’ordre et des coefficients est empirique et requiert de l’expérience

 □ Avantages des moyennes mobiles :
        Elles donnent une meilleure estimation de la tendance que la méthode des moindres
        carrés (voir chapitre 2).
        Elles sont très souples et résistent mieux aux changements de régime que les modèles
        linéaires.
        Elles permettent d’éliminer les perturbations.




        (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                    16 janvier
                                                                                           mobiles
                                                                                               2025   43 / 65
~~~

## Page 44

~~~text
Comparaison des Moyennes Mobiles


    Caractéristique        Ordre Impair (p = 2m + 1)                     Ordre Pair (p = 2m)
 Nombre d’observations             2m + 1                          2m + 1 (avec poids extrêmes 1/2)
                                h                         i                    h                           i
          Poids                       1              1                              1     1            1
                                    2m+1 , . . . , 2m+1                            4 m , 2m , . . . , 4m
 Saisonnalité supprimée               p = 2m + 1                                        p = 2m
  Tendance conservée          Polynômes de degré 1                          Polynômes de degré 1


▷ Conclusion

    Les moyennes mobiles permettent de filtrer efficacement les séries temporelles en
    supprimant les bruits et les composantes saisonnières.
    Le choix entre un ordre pair ou impair dépend de la périodicité à supprimer.
    Les notations avec crochets facilitent la représentation des poids.

Remarque : Toujours vérifier les propriétés des moyennes mobiles avant application.




          (CY Tech)          Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                    16 janvier
                                                                                           mobiles
                                                                                               2025            44 / 65
~~~

## Page 45

~~~text
Moyennes mobiles arithmétiques (symétriques) - Exemples
Exemple 1 : Données trimestrielles
    La moyenne mobile, M2×4 , est utilisée pour estimer les tendances dans le cas de
    données trimestrielles.
         M2×4 est d’ordre 5 avec des coefficients :
                                                  1 1 1 1 1i
                                                      h
                                            Poids = 5,
                                                    , , , , .
                                                  8 4 4 4 8
         La série transformée est calculée comme suit :
                                        1h                                   i
                           M2×4 (Xt ) = Xt −2 + 2Xt −1 + 2Xt + 2Xt +1 + Xt +2 .
                                        8
         Cette transformation élimine les saisonnalités trimestrielles et conserve les
         tendances linéaires.

Exemple 2 : Données mensuelles
    La moyenne mobile, M2×12 , est utilisée pour estimer les tendances dans le cas de
    données mensuelles.
         M2×12 est d’ordre 13 avec des coefficients :
                                           h      1 1 1            1 1 i
                                   Poids = 13,     ,    ,   ,...,      ,     .
                                                 24 12 12         12 24
         La série transformée est donnée par :
                                     1 h                                                 i
                       M2×12 (Xt ) =     Xt −6 + 2Xt −5 + 2Xt −4 + . . . + 2Xt +5 + Xt +6 .
                                     24
         (CY Tech)               Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                        16 janvier
                                                                                               mobiles
                                                                                                   2025   45 / 65
~~~

## Page 46

~~~text
Moyennes Mobiles Arithmétiques (Symétriques) - Exemples

Exemple 3. Moyenne Mobile Centrée d’Ordre 3.

    Il s’agit d’une moyenne arithmétique classique, calculée sur 3 observations :
                                                    1
                               Yt = M3 (Xt ) =        [X   + Xt + Xt +1 ]
                                                    3 t −1
Exemple 4. Moyenne Mobile Centrée d’Ordre 4.

    Elle est calculée sur 5 observations, avec des poids égaux à 21 pour les valeurs
    extrêmes :
                                    1 1                              1
                                      ·                                     ¸
                    Yt = M4 (Xt ) =      Xt −2 + Xt −1 + Xt + Xt +1 + Xt +2
                                    4 2                              2
Exemple 5. Moyenne Mobile Centrée d’Ordre 5.
                                        1
                      Yt = M5 (Xt ) =     [X   + Xt −1 + Xt + Xt +1 + Xt +2 ]
                                        5 t −2

▷ Ces filtres éliminent la saisonnalité et le bruit, tout en laissant la tendance inchangée,
à condition de choisir l’ordre p de Mp égal à la période de la série temporelle initiale.


          (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   46 / 65
~~~

## Page 47

~~~text
    Désaisonnalisation par les moyennes mobiles simples




(CY Tech)        Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                        16 janvier
                                                                               mobiles
                                                                                   2025   47 / 65
~~~

## Page 48

~~~text
Désaisonnalisation par les moyennes mobiles simples (exemple)

Si on applique cette désaisonnalisation à la série trimestrielle du trafic SNCF entre 1963
et 1968, on obtient

Figure – Moyenne mobile centrée sur série trimestrielle SNCF.
La M4 est le mieux adaptée car la série est de période 4




          (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   48 / 65
~~~

## Page 49

~~~text
Désaisonnalisation au moyen d’un filtre du type "différence"




 (CY Tech)       Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                        16 janvier
                                                                               mobiles
                                                                                   2025   49 / 65
~~~

## Page 50

~~~text
Désaisonnalisation au moyen d’un filtre du type "différence"

▷ Cette alternative permettant d’éliminer (ou tout au moins de réduire) une composante
saisonnière de période p en utilisant l’opérateur de différence.

                        ∇p Xt = Xt − Xt −p = (1 − B p )Xt              où     BXt = Xt −1


▷ considérons le modèle :

                        Xt = mt + St + ϵt ,         t = 1, . . . , T   avec     St = St +p .

                                  la série définie par :        Yt = (1 − B p )Xt
est sans composante saisonnière. En effet,


        Yt    =       (1 − B p )Xt = Xt − Xt −p = (mt − mt −p ) + (St − St −p ) + (ϵt − ϵt −p )
              =       (mt − mt −p ) + (ϵt − ϵt −p )
              =       mt∗ + ϵ∗t



          (CY Tech)                   Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                             16 janvier
                                                                                                    mobiles
                                                                                                        2025   50 / 65
~~~

## Page 51

~~~text
Désaisonnalisation au moyen d’un filtre du type "différence" : Exemple

Si on considère la série mensuelle du trafic voyageur alors la série
                                        Yt = (1 − B 12 )Xt
ne présente plus de composante saisonnière.

           Figure – Moyenne mobile centrée (différence) sur série trimestrielle SNCF




          (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   51 / 65
~~~

## Page 52

~~~text
Exemple d’application de MM
▷ On a comptabilisé pendant trois semaines consécutives le nombre journalier de
visiteurs d’un musée dont les jours de fermeture sont le samedi et le dimanche.

                      Lundi      Mardi       Mercredi         Jeudi       Vendredi
 Première semaine       7          5           35               5            6
 Deuxième semaine       8          9           45               8            9
 Troisième semaine     10         11           42               9           11
▷ Le graphe semble mettre en évidence une tendance linéaire ainsi qu’une saisonnalité de
période 5 :




                              Figure – Graphe de la série initiale

         (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   52 / 65
~~~

## Page 53

~~~text
Exemple d’application de MM- Calcule des MM et de la série Xscv ,t
    On choisit un modèle additif car les différences (maximum-minimum) semblent
    similaires sur chaque période (semaine).
        Les termes tendanciels pour t ∈ {3, . . . , 13} figurent dans le tableau ci-après.

    On utilise la moyenne mobile M5 afin d’estimer la tendance (supposée linéaire) de la
    série temporelle.
        Pour rappel cette moyenne mobile conserve les tendances linéaires et absorbe les
        saisonnalités de période 5.




         (CY Tech)              Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                       16 janvier
                                                                                              mobiles
                                                                                                  2025   53 / 65
~~~

## Page 54

~~~text
Exemple d’application de MM




               Figure – Superposition de Xt et de la série Moyenne Mobile




       (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                   16 janvier
                                                                                          mobiles
                                                                                              2025   54 / 65
~~~

## Page 55

~~~text
Exemple d’application de MM
▷ On calcule les coefficients saisonniers comme suit :
                                           23.4 + 29.2 + 25.4
                          cmercredi =                         = 26
                                                   3
                                           −6.8 − 8.2
                              cjeudi =                = −7.5
                                               2
                                           −6.6 − 7.6
                          cvendredi =                 = −7.1
                                               2
                                           −6.6 − 6
                              clundi =              = −6.3
                                              2
                                           −6.2 − 5.2
                             cmardi =                 = −5.7
                                               2
On constate que :c = −0.12.
▷ Les coefficients saisonniers centrés sont :
                          ′
                         cmercredi           =     26 − (−0.12) = 26.12
                                    ′
                               cjeudi        =     −7.5 − (−0.12) = −7.38
                           ′
                         cvendredi           =     = −7.1 − (−0.12) = −6.98
                                ′
                               clundi        =     −6.3 − (−0.12) = −6.18
                                ′
                               cmardi        =     −5.7 − (−0.12) = −5.58
          (CY Tech)                 Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                           16 janvier
                                                                                                  mobiles
                                                                                                      2025   55 / 65
~~~

## Page 56

~~~text
Exemple d’application de MM

La série corrigée des variations saisonnières, est ainsi représentée :




                       Figure – Série corrigée des variations saisonnières




          (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                      16 janvier
                                                                                             mobiles
                                                                                                 2025   56 / 65
~~~

## Page 57

~~~text
Bibliographie

[1] Aragon, Y. (2011). Séries temporelles avec R. Springer.
[2] Bosq, D. et Lecoutre, JP. (1992). Analyse et prévision des Séries Chronologiques.
Masson.
[3] Charpentier, A. (2015). Modèles de prévision Séries temporelles. M1 SE.
[4] Gouriéroux, C., Monfort, A. (1995) Séries temporelles et modèles dynamiques.
Economica.
[5] GRUN REHOMME, M. et D. LADIRAY, D. (1994). Moyennes mobiles centrées et
non-centrées.Construction et comparaison. Revue de statistique appliquée, tome 42, no 3,
p. 33–61.
[6] Lagnoux, A. Séries chronologiques.
ISMAG MASTER 1 - MI00141X. Université de Toulouse Le Mirail.




          (CY Tech)          Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                    16 janvier
                                                                                           mobiles
                                                                                               2025   57 / 65
~~~

## Page 58

~~~text
(CY Tech)   Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                   16 janvier
                                                                          mobiles
                                                                              2025   58 / 65
~~~

## Page 59

~~~text
                          Annexes




(CY Tech)   Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                   16 janvier
                                                                          mobiles
                                                                              2025   59 / 65
~~~

## Page 60

~~~text
Annexe 1. Réécriture de la moyenne mobile en termes d’opérateurs de
                                retard
                 et propriétés des moyennes mobiles




     (CY Tech)       Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                            16 janvier
                                                                                   mobiles
                                                                                       2025   60 / 65
~~~

## Page 61

~~~text
Notion d’opérateur de retard B

▷ La moyenne mobile peut être réécrite en termes d’opérateurs linéaires.
    Soit (Xt )t ∈Z . On note B l’opérateur de retard (backward operator ), défini par :
                     ∀t ∈ Z,     BXt = Xt −1 ,       B 2 Xt = Xt −2 ,       B k Xt = Xt −k ,
    avec la convention :
                      B k = |B ◦ B {z
                                   ◦ · · · ◦ B},   et B 0 = I , l’opérateur identité.
                                  k -fois
    L’opérateur B est linéaire et inversible. Son inverse, noté B −1 , est appelé opérateur
    d’avance (forward operator ), noté F . On a la relation :
                                              B ◦F = F ◦B = I,
    où F est défini par :
                                 ∀t ∈ Z, FXt = Xt +1 .
    Soit Θ un polynôme de degré p, donné par :
                                  Θ(z) = a0 + a1 z + a2 z 2 + . . . + ap z p .
    Le polynôme appliqué à B, noté Θ(B), est défini par :
                                                                               p
                       Θ(B) = a0 I + a1 B + a2 B 2 + . . . + ap B p =                ak B k .
                                                                               X

                                                                              k =0
         (CY Tech)               Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                        16 janvier
                                                                                               mobiles
                                                                                                   2025   61 / 65
~~~

## Page 62

~~~text
F-MM : Opérateur de retard

   La série Yt , résultant de la transformation de Xt par un filtre moyenne mobile
   (MM), peut s’écrire :
                                          m
                                          X2                     m
                                                                 X2
                       Yt = M(Xt ) =             θi Xt +i =             θi B −i Xt .
                                        i =−m1                i =−m1

   Ainsi, l’opérateur moyenne mobile M := Mm1 +m2 +1 est un polynôme en B (ou en
   F ). Cela donne :
                                       m
                                       X2                   m
                                                            X2
                              M=               θi B −i =            θi F i .
                                      i =−m1               i =−m1
   En factorisant par B m1 et en posant j = i + m1 , on obtient la forme canonique
   suivante :
                              m1X
                                +m2                              m
                                                                 X2
          Mm1 +m2 +1 = B m1            θj −m1 F j = B m1                θi F m1 +i =: B m1 Θ(F ).
                               j =0                          i =−m1




        (CY Tech)          Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                  16 janvier
                                                                                         mobiles
                                                                                             2025   62 / 65
~~~

## Page 63

~~~text
Polynôme caractéristique associé à M


    Le polynôme caractéristique Θ associé à M est donné par :
                            m
                            X2
                 Θ(z) =             θi z m1 +i = θ−m1 + θ−m1 +1 z + . . . + θm2 z m1 +m2 .
                           i =−m1
                     • m1 + m2 + 1 est l’ordre de M.
                     • Le degré de M est égal au degré du polynôme Θ :
                                                        deg(Θ) = m1 + m2 .

                     • Le polynôme Θ peut aussi s’écrire sous une forme alternative :
                                                               m1X
                                                                 +m2
                                                    Θ(z) =              θj −m1 z j .
                                                                 j =0

▷ Remarque : La donnée du polynôme Θ caractérise complètement la moyenne mobile
M.
             - L’ordre de cette moyenne est donné par :
                                                m1 + m2 + 1 = deg(Θ) + 1.
             - Les coefficients de M sont égaux à ceux du polynôme Θ.
         (CY Tech)               Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                        16 janvier
                                                                                               mobiles
                                                                                                   2025   63 / 65
~~~

## Page 64

~~~text
Propriétés des moyennes mobiles

Propriété 1
Pour toutes moyennes mobiles M et N, les propriétés suivantes sont vérifiées :

                                    M(B) + N(B) = (M + N)(B),

                                 ∀ λ ∈ R,      λM(B) = (λM)(B),
                        M(B) ◦ N(B) = (MN)(B) = N(B) ◦ M(B).
La moyenne mobile composée C = MN = NM vérifie :
                         Ã               ! Ã                 !       Ã               !
                             ∞                 ∞                         ∞
                                    ak B k ◦          bk B k =                  ci B i ,
                             X                 X                         X

                             k =0              k =0                      i =0

où
                                                 i
                                                 X
                                          ci =          ak bi −k .
                                                 k =0




          (CY Tech)             Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                       16 janvier
                                                                                              mobiles
                                                                                                  2025   64 / 65
~~~

## Page 65

~~~text
Propriétés des moyennes mobiles : Remarque sur la composition

    L’application composée M = M1 ◦ M2 est encore une moyenne mobile.
      - Ce résultat est très important en pratique, car il permet :
      - de définir des moyennes mobiles à partir de moyennes d’ordres inférieurs, qui sont donc
        plus simples à manipuler.

    La composition des moyennes mobiles possède les propriétés suivantes :
      - Associativité : (M1 ◦ M2 ) ◦ M3 = M1 ◦ (M2 ◦ M3 ).
      - Commutativité : M1 ◦ M2 = M2 ◦ M1 .
      - En d’autres termes, l’ordre d’application des moyennes mobiles est indifférent.




         (CY Tech)            Chapitre III - Désaisonnalisation par la méthode des moyennes
                                                                                     16 janvier
                                                                                            mobiles
                                                                                                2025   65 / 65
~~~
