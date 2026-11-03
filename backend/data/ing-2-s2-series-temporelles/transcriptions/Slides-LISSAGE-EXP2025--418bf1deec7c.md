# Slides-LISSAGE-EXP2025.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Ysl9uMzuV5vIA6MR9fzSPl_g1Fd9gh5y) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
     Séries temporelles-Chapitre 4: LISSAGE-Exponentiel



                                 CY Tech


                           26 janvier 2025




(CY Tech)        Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   1 / 51
~~~

## Page 2

~~~text
Plan



1   Lissage exponentiel simple (LES)




2   Lissage exponentiel double (LED)




3   Méthode de Holt-Winters



4   Annexe 1 : Mise en œuvre sous R




          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   2 / 51
~~~

## Page 3

~~~text
                      Introduction




(CY Tech)   Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   3 / 51
~~~

## Page 4

~~~text
                                           Référénces
Julien JACQUES website :
https ://eric.univ-lyon2.fr/jjacques/index.html




          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   4 / 51
~~~

## Page 5

~~~text
Introduction [1]

▷ Dans l’industrie, les prévisions de ventes et de production s’appuient sur des
techniques de lissage exponentiel,

             développées par Brown (1959), Holt (1957) et Winters (1960).

▷ Ces méthodes utilisent des moyennes pondérées des observations passées, où :

    Les poids des observations diminuent exponentiellement avec le temps, donnant plus
    d’importance aux données récentes.

▷ Points clés :

    Simples et largement utilisées en économie et gestion.
    Fournissent des prévisions ponctuelles sans hypothèses probabilistes.
    Efficaces pour des prévisions à court terme.




          (CY Tech)          Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   5 / 51
~~~

## Page 6

~~~text
Introduction [2]- Idées générales

▷ On considère une série x = (x1 , . . . , xn ) de longueur n, observée aux dates 1, . . . , n.

     À la date n, on souhaite prévoir la valeur future xn+h à l’horizon h.
     Cette prévision est notée xbn,h , où n est parfois appelée base de la prévision.

▷ Les méthodes de lissage exponentiel sont des techniques les plus anciennes.
     Ces méthodes ajustent à la série, localement, une fonction simple :
          une constante pour le LES,
          une droite pour le lissage exponentiel double (LED),
          des fonctions polynomiales ou périodiques pour des lissages plus avancés.




           (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   6 / 51
~~~

## Page 7

~~~text
Introduction [3] - Idées générales

▷ Supposons que la série initiale suit le modèle :

            Xt = ft ,k + ϵt   avec    E(ϵt ) = 0,     E( ϵ 2   2
                                                           t)=σ ,        E(ϵt ϵs ) = 0 ∀s ̸= t .

▷ La fonction ft ,k est un polynôme de degré k, avec des paramètres dépendant du temps.

    Si k = 0 :
                      Xt = at + ϵt   avec     at = a     pour     t ∈ {T1 , T2 } ⊂ {1, T }.
    Dans ce cas, on utilise le lissage exponentiel simple (LES) pour ajuster localement
    une constante.

    Si k = 1 :

             Xt = at + bt t + ϵt     avec   at = a, bt = b        pour      t ∈ {T1 , T2 } ⊂ {1, T }.

    Ici, on utilise le lissage exponentiel double (LED) pour ajuster localement une droite.

    Si k est quelconque : La méthode employée est le lissage exponentiel généralisé, qui
    ajuste localement un polynôme de degré k.


          (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025    7 / 51
~~~

## Page 8

~~~text
                      1. Lissage exponentiel simple (LES)

▷ Cette méthode convient pour

    la prévision des données sans tendance claire ni modèle saisonnier.
    Elle s’applique à des séries chronologiques sans saisonnalité et à tendance
    localement constante.




         (CY Tech)          Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   8 / 51
~~~

## Page 9

~~~text
LES. Exemple

   les données de la figure 1 n’affichent aucun comportement de tendance clair ni
   saisonnalité.
   Il y a une augmentation au cours des dernières années, ce qui pourrait suggérer une
   tendance.

library(fpp2)
oildata <- window(oil, start=1996)
autoplot(oildata)+ ylab("Oil (millions of tonnes)") + xlab("Year")




           Figure – 1. Production de pétrole en Arabie Saoudite de 1996 à 2013

        (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   9 / 51
~~~

## Page 10

~~~text
Lissage Exponentiel Simple (LES)

▷ Caractéristiques principales du LES :

    La prévision est simple et indépendante de l’horizon de prévision h.
    L’indice h est conservé pour garantir la cohérence avec les notations ultérieures.

▷ Définition : La prévision xbn,h est construite en tenant compte :

              • De toute l’histoire de la série, c’est-à-dire de toutes les observations
                jusqu’à la base n.
              • Plus une observation est ancienne, moins son influence est importante
                dans la prévision.
              • Cette décroissance d’influence suit une loi exponentielle.

▷ Formalisation :

    On dispose de la série x1 , . . . , xn et on souhaite estimer xbn+h , où h ∈ N∗ .
    Pour un paramètre de lissage α ∈]0, 1[ (fixé), la prévision par lissage exponentiel
    simple (LES) est définie par :

                                        xbn+1 = αxn + (1 − α)xbn .

          (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   10 / 51
~~~

## Page 11

~~~text
Lissage Exponentiel Simple : Formules et Propriétés

                                                   −1
                                                  nX
                                xbn,h    =    α          (1 − α)j xn−j .                              (1)
                                                  j =0

▷ Caractéristiques principales :

 ▷ La prévision est constante (indépendante de l’horizon h).
 ▷ Elle correspond à une moyenne pondérée des observations passées.
 ▷ Si α est petit (α ≤ 0.3), les observations anciennes ont plus de poids.
 ▷ Si α est grand (α ≥ 0.7), le poids des observations passées décroît rapidement.
 ▷ La valeur de α doit être réglée en fonction des données.

▷ Formules récursives : La définition (1) se reformule de manière récursive :

                               xbn,h = αxn + (1 − α)xbn−1,h ,                                         (2)
                               xbn,h = xbn−1,h + α(xn − xbn−1,h ).                                    (3)
▷ Propriété clé :
    La prévision actuelle xbn,h dépend uniquement :
         De la prévision précédente xbn−1,h .
         De la nouvelle observation xn .

          (CY Tech)            Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   11 / 51
~~~

## Page 12

~~~text
Interprétation Géométrique
▷ Asymptotiquement, xbn,h est la meilleure approximation au sens des moindres carrés
(MC) de la série x = (x1 , . . . , xn ) par le vecteur constant a × 1, où : 1 = (1, . . . , 1)′ ∈ Rn .
La valeur de a minimise :
                                            −1
                                           nX
                                                  (1 − α)j (xn−j − a)2 .                                              (4)
                                           j =0
Résultat :

                                              α            −1
                                                          nX
                              abn =                               (1 − α)j xn−j .                                     (5)
                                      1 − (1 − α)n         j =0
▷ Propriétés :

  ▷ L’influence des observations décroît exponentiellement avec l’éloignement de la base
    n.
  ▷ L’ajustement par la constante a est local, au voisinage de n.

▷ Extension du modèle : Si on considère le vecteur transformé :

                            x = (x1 , . . . , xn )′ = (. . . , 0, . . . , 0, x1 , . . . , xn )′ ,

où les coordonnées pour les indices négatifs ou nuls sont nulles, l’interprétation
géométrique reste cohérente.
             (CY Tech)              Séries temporelles-Chapitre 4: LISSAGE-Exponentiel              26 janvier 2025   12 / 51
~~~

## Page 13

~~~text
Minimisation et Solution Asymptotique
▷ On cherche la valeur de a qui minimise :
                                   ∞
                                         (1 − α)j (xn−j − a)2 .
                                   X

                                  j =0
▷ La solution asymptotique à ce problème de minimisation est donnée par :
                                              −1
                                             nX
                                 xbn,h = α          (1 − α)j xn−j .
                                             j =0
▷ On peut montrer que les deux estimateurs abn (défini en (5)) et xbn,h sont
asymptotiquement équivalents, c’est-à-dire :
                                    lim abn = lim xbn,h .
                                  n→+∞       n→+∞
▷ Résultat Formel :
Lemme 1
La prédiction xbn,h est asymptotiquement la solution du problème de minimisation :

                                             −1
                                            nX
                           xbn,h = argmin           (1 − α)j (xn−j − a)2 .
                                     a       j =0

Ce résultat souligne que l’ajustement par la constante a est optimal au sens des moindres
carrés (MC) lorsqu’une pondération exponentielle est appliquée aux observations passées.
          (CY Tech)          Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   13 / 51
~~~

## Page 14

~~~text
Démonstration

▷ Soit la fonction à minimiser :
                                           −1
                                          nX
                                f (a) =          (1 − α)j (xn−j − a)2 .
                                          j =0


▷ Recherche des points critiques :

                                               −1
                                              nX
                               f ′ (a) = −2          (1 − α)j (xn−j − a).
                                              j =0

▷ La dérivée s’annule en a0 donné par :
                             Pn−1
                                    (1 − α)j xn−j α nj =−01 (1 − α)j xn−j
                                                   P
                              j =0
                      a0 =                       =                        .
                               Pn−1
                                      (1 − α)j        1 − (1 − α)n
                                 j =0


▷ Comportement asymptotique : lorsque n → +∞, on obtient :
                                                      −1
                                                     nX
                                 a0     ∼        α          (1 − α)j xn−j .
                                      n→+∞
                                                     j =0
          (CY Tech)            Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   14 / 51
~~~

## Page 15

~~~text
            Choix de la constante de lissage




(CY Tech)      Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   15 / 51
~~~

## Page 16

~~~text
Choix de la constante de lissage
▷ Limitations du lissage exponentiel simple :

    La méthode est peu performante :
                   - en présence de tendance ou de composante saisonnière,
                   - ou en cas de fluctuations de hautes fréquences.
▷ Utilisation pratique :

    Le lissage exponentiel simple est rarement utilisé en pratique.
    Des valeurs de α comprises entre 0.7 et 0.99 :
                 - produisent des prévisions rigides,
                 - tiennent compte du passé lointain mais sont peu sensibles aux
                   variations conjoncturelles.
   Au contraire, pour α ∈ [0.01, 0.3], les prévisions sont plus souples et influencées par
   les observations récentes.
▷ Détermination de α adapté :

    Pour un horizon donné h, on cherche la valeur de α qui minimise :
                                                                               !2
                                                        −1
                                       Ã
                                nX
                                 −h                    tX
                                           xt +h − α          (1 − α)j xt −j        .
                                t =1                   j =0
          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel        26 janvier 2025   16 / 51
~~~

## Page 17

~~~text
Choix optimal de α

▷ Objectif : Trouver la valeur de α qui minimise l’erreur quadratique moyenne des
prévisions à l’horizon h.

▷ Méthode :

    Sélectionner une grille de valeurs pour α.
    Calculer, pour chaque α, les prédictions xbt ,h (α).
    Évaluer l’erreur quadratique :
                                             nX
                                              −h ¡
                                 E2 (α) =           xt +h − xbt ,h (α) 2 .
                                                                      ¢
                                             t =1

    Retenir α comme :
                                         α = argminα E2 (α).


▷ Critère : Une erreur quadratique faible indique que α génère des prévisions
performantes.



          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   17 / 51
~~~

## Page 18

~~~text
Comparaison de modèles

▷ Méthode : Découper les données en apprentissage/test :

    Entraînement : Environ 23 (ou 80%) des données servent à estimer les paramètres
    des modèles.
    Test : Le reste ( 13 ou 20%) sert à évaluer les modèles via le RMSE (Root Mean
    Square Error ) :                      v
                                           un−m
                                                 xbm,h − xm+h 2 ,
                                           u X ¡
                               ϵerreur,h = t
                                                             ¢
                                             h=1

    où m est le nombre de données d’apprentissage.

▷ Ajustements possibles :

    Adapter la taille de l’échantillon test à l’horizon de prédiction souhaité.

Remarque : Une fois le meilleur modèle sélectionné, il est crucial de le réestimer sur
l’ensemble des données disponibles avant d’effectuer des prédictions finales.



          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   18 / 51
~~~

## Page 19

~~~text
Exemple-Prévision par LES avec α = 0.1




                    Figure – 2. Prévision par LES avec α = 0.1




        (CY Tech)       Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   19 / 51
~~~

## Page 20

~~~text
Exemple-Prévision par LES avec α = 0.9




                    Figure – 3. Prévision par LES avec α = 0.9




        (CY Tech)       Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   20 / 51
~~~

## Page 21

~~~text
Exemple-Prévision par LES-Choix automatique de α

Pour choisir α de façon optimale (apprentissage/test), il suffit d’indiquer "alpha=NULL"
dans les options.




                      Figure – 4. Prévision par LES avec choix optimal de α
          (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   21 / 51
~~~

## Page 22

~~~text
Exemple-Prévision par LES ajout d’intervalle de prédiction

On peut également ajouter un intervalle de prédiction.




                      Figure – 5. Prévision par LES avec choix optimal de α


          (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   22 / 51
~~~

## Page 23

~~~text
      Lissage exponentiel double (LED) non saisonnier




(CY Tech)        Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   23 / 51
~~~

## Page 24

~~~text
Lissage exponentiel double (LED)

▷ Problème : On cherche à ajuster une droite, à l’instant t, au voisinage de n, avec
l’équation suivante :
                                 yt = a1 + a2 (t − n).

▷ La prévision par lissage exponentiel double (LED) s’écrit :

                                            xbn,h = ab1 + ab2 h,

où les coefficients (ab1 , ab2 ) sont déterminés en résolvant le problème de minimisation
suivant :


                                                   −1
                                                  nX                                   ¢2
                                                         (1 − α)j xn−j − (a1 + a2 j) ,
                                                                 ¡
              (ab1 , ab2 ) = argmin(a1 ,a2 )∈R2                                                          (6)
                                                  j =0

avec 0 < α < 1.




          (CY Tech)               Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   24 / 51
~~~

## Page 25

~~~text
Proposition 1
Les solutions asymptotiques du e problème de minimisation (6) sont données par :

                               ab1 = −L2 (n) + 2L1 (n),
                                        α ¡                    ¢
                               ab2 =          − L2 (n) + L1 (n) ,
                                       1−α
où les termes L1 (n) et L2 (n) sont définis comme suit :
                                            −1
                                           nX
                              L1 (n) = α          (1 − α)j xn−j ,
                                           j =0

                                            −1
                                           nX
                              L2 (n) = α          (1 − α)j L1 (n − j).
                                           j =0


    L1 (n) représente une moyenne pondérée exponentiellement décroissante des
    observations passées xn−j .
    L2 (n) est une moyenne pondérée des valeurs de L1 (n − j), appliquant une double
    pondération exponentielle.
    La méthode permet d’obtenir des coefficients ab1 et ab2 qui ajustent la tendance
    linéaire à l’instant n, tout en tenant compte d’un lissage des observations passées.
          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   25 / 51
~~~

## Page 26

~~~text
Remarque 1
    On observe ici deux lissages exponentiels successifs, car L2 est un lissage
    exponentiel de L1 .
    C’est pour cette raison que l’on parle de lissage exponentiel double.

▷ Les formules de mise à jour

                                  ab1 (n − 1) + ab2 (n − 1) + (2α − α2 )(xn − xbn−1,1 )
                
                 ab1 (n) =
                                                                                                          (7)
                                            ab2 (n − 1) + α2 (xn − xbn−1,1 ) ,
                
                      ab2 (n) =

avec l’initialisation                  
                                        ab1 (0) =           x1

                                            ab2 (0)     = x2 − x1 .
                                       

Ces formules permettent de comprendre comment calculer récursivement les coefficients
(ce qui limite la complexité du calcul).




          (CY Tech)                Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   26 / 51
~~~

## Page 27

~~~text
                            Méthode de Holt-Winters

▷ Cette approche a pour but d’améliorer et de généraliser le Lissage Exponentiel Simple
(L.E.S.).




         (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   27 / 51
~~~

## Page 28

~~~text
Introduction.

▷ Nous examinons divers cas particuliers de la méthode de Holt-Winters :

              - Ajustement d’une droite affine (sans saisonnalité),
              - Ajustement d’une droite affine + une composante saisonnière,
              - Ajustement d’une constante + une composante saisonnière.

Le dernier cas peut être considéré comme un cas particulier du second.


1. Méthode de Holt-Winters non saisonnière :

    L’objectif est d’ajuster une droite au voisinage de l’instant n, décrite par l’équation :

                                         yt = a1 + (t − n)a2 .

    La prévision à l’instant n + h est donnée par :

                                       xn,h = ab1 (n) + hab2 (n).




          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   28 / 51
~~~

## Page 29

~~~text
Calcul des paramètres.

            ▷ On utilise deux constantes de lissage, α et β, définies dans l’intervalle
              ]0, 1[.
            ▷ Les paramètres ab1 (n) (niveau) et ab2 (n) (tendance) sont calculés de
              manière récursive comme suit :



                                      αxn + (1 − α) ab1 (n − 1) + ab2 (n − 1) ,
                                                   £                         ¤
                     ab1 (n)   =                                                                          (8)

                                      β ab1 (n) − ab1 (n − 1) + (1 − β)ab2 (n − 1).
                                       £                     ¤
                     ab2 (n)   =                                                                          (9)



    ab1 (n) : Estimation du niveau actuel de la série.
    ab2 (n) : Estimation de la tendance de la série (taux de variation).
    α : Contrôle le degré de réactivité de ab1 (n) aux nouvelles observations.
    β : Détermine la rapidité d’ajustement de la tendance ab2 (n) face aux variations des
    niveaux estimés.



         (CY Tech)                 Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   29 / 51
~~~

## Page 30

~~~text
Méthode non saisonnière - Remarque

   L’introduction des deux constantes α et β rend cette méthode plus flexible que le
   lissage exponentiel double classique :
       α intervient dans l’estimation de l’ordonnée à l’origine (a1 ) de la droite.
       β est utilisé pour estimer la pente (a2 ) de la droite.
   Lorsque α et β sont faibles, cela reflète une forte influence du passé lointain,
   accordant moins de poids aux observations récentes.


   Ordonnée à l’origine ab1 : Niveau estimé de la série à un instant donné.
   Pente ab2 : Variation ou tendance de la série dans le temps.
   Les paramètres α et β ajustent la réactivité des estimations selon que l’on privilégie
   les données récentes ou l’historique.




        (CY Tech)            Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   30 / 51
~~~

## Page 31

~~~text
Lissage Exponentiel de Holt-Winters non saisonnier-Exemple

▷ On prédit la suite de la série par une droite d’équation
                                        xbn,h = ab1 + hab2
où 2 constantes de lissage (α, β) interviennent respectivement sur a1 et a2 .




                            Figure – Lissage Exponentiel double

          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   31 / 51
~~~

## Page 32

~~~text
            2. Ajout d’une composante saisonnière.
                 Méthode saisonnière additive




(CY Tech)         Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   32 / 51
~~~

## Page 33

~~~text
2. Ajout d’une composante saisonnière : Méthode saisonnière additive

▷ Nous cherchons, au voisinage de n, à ajuster une courbe d’équation :
                                       yt = a1 + a2 (t − n) + st ,
où :
       a1 est l’ordonnée à l’origine, représentant le niveau de base de la série.
       a2 est la pente, représentant la tendance de la série.
       st est une composante périodique de période T , reflétant la saisonnalité (effets
       cycliques réguliers sur T périodes).

▷ Pour appliquer cette méthode, il est nécessaire de choisir trois constantes : α, β, γ,
toutes comprises dans [0, 1[, ainsi que la période T .
Les formules de récursion sont les suivantes :
                                                        h                         i
                                  α xn − sbn−T + (1 − α) ab1 (n − 1) + ab2 (n − 1) ,
                                   ¡          ¢
                   ab1 (n)    =


                                  β ab1 (n) − ab1 (n − 1) + (1 − β)ab2 (n − 1),
                                   £                     ¤
                   ab2 (n)    =

                                  γ xn − ab1 (n) + (1 − γ)sbn−T .
                                   £            ¤
                        sbn   =

            (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   33 / 51
~~~

## Page 34

~~~text
2. Ajout d’une composante saisonnière : Méthode saisonnière additive

▷ La prévision s’exprime comme suit :

                      xbn,h   =   ab1 (n) + hab2 (n) + sbn+h−T ,      1≤h ≤T,

                      xbn,h   =   ab1 (n) + hab2 (n) + sbn+h−2T ,      T + 1 ≤ h ≤ 2T ,

                        ...   =   ...

    Et ainsi de suite pour h > 2T , où les indices saisonniers sont ajustés en fonction des
    périodes multiples de T .
    Le choix des constantes α, β et γ est délicat et nécessite souvent des essais ou une
    optimisation sur des données historiques.

▷ Interprétation :

    ab1 (n) : Niveau estimé à l’instant n, ajusté pour tenir compte de la saisonnalité.
    ab2 (n) : Variation moyenne (tendance) entre deux instants consécutifs.
    sbn : Effet saisonnier estimé pour l’instant n, basé sur les valeurs T périodes plus tôt.
    xbn,h : Prévision pour l’instant n + h, intégrant le niveau, la tendance, et l’effet
    saisonnier ajusté.
          (CY Tech)                Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   34 / 51
~~~

## Page 35

~~~text
2. Ajout d’une composante saisonnière : Méthode saisonnière additive

▷ Avantages :

    Permet de modéliser des séries chronologiques présentant à la fois une tendance et
    une saisonnalité.
    Méthode flexible grâce aux paramètres α, β, γ, qui contrôlent respectivement le
    niveau, la tendance, et la saisonnalité.




         (CY Tech)          Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   35 / 51
~~~

## Page 36

~~~text
Initialisation

Les valeurs initiales suivantes permettent (mais on pourrait en proposer d’autres) de
commencer le calcul récursif des prévisions à partir de l’instant T + 2 :


            ab1 (T + 1)     =   xT +1
                                xT +1 − x1
            ab2 (T + 1)     =
                                     T
                      sbj   =   xj − (x1 + (T − 1)ab2 (T + 1)))         pour     j ∈ {1, . . . , T }.

    Les trois constantes de lissages, α, β, γ ont le même effet que précédemment,
    plus elles sont petites et plus l’importance des données éloignées est significative.
    Elles agissent respectivement sur les paramètres a1 , a2 et st .




          (CY Tech)              Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   36 / 51
~~~

## Page 37

~~~text
Lissage Exponentiel de Holt-Winters saisonnier additif-Exemple

▷ Pour pouvoir estimer la saisonnalité, il faut préciser la taille de celle-ci lors de la
définition de l’objet série temporelle

serie=0.5*(1 : 100) +rnorm (100,0,1) + 3*cos(pi/6*(1 : 100))
serie=ts(serie,start= c(1,1),end=c(9,4),frequency= 12)
LES= HoltWinters (serie,alpha=NULL,beta=NULL,gamma=NULL)
plot (serie,xlim= c(1,11),ylim=c(0,70))
p<- predict(LES,n.ahead=20)
lines(p,col=2)




          (CY Tech)                          Figure –
                               Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   37 / 51
~~~

## Page 38

~~~text
            Méthode saisonnière multiplicative




(CY Tech)       Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   38 / 51
~~~

## Page 39

~~~text
Méthode saisonnière multiplicative

On cherche, au voisinage de n, à ajuster une courbe d’équation

                                       yt = (a1 + a2 (t − n)) × st

 (avec s. périodique, de période T ). Il faut choisir α, β, γ dans ]0;1[. Les formules de
récursion sont
                        ab (n)    =     (1 − α) sbxn + α(ab1 (n − 1) + ab2 (n − 1))
                      
                       1
                      
                                                 n−T
                      
                      
                      
                        ab2 (n)   =    (1 − β)(ab1 (n) − ab1 (n − 1)) + βab2 (n − 1)
                      
                      
                      
                                                  (1 − γ) ab x(nn) + γsbn−T .
                      
                      
                       sb        =
                            n
                                                             1

La prévision prend la forme

                                      (ab1 (n) + hab2 (n)) × sbn+h−T , 1 ≤ h ≤ T
                  
                   xbn,h =
                    xb =          (ab1 (n) + hab2 (n)) × sbn+h−2T , T + 1 ≤ h ≤ 2T
                   n ,h
                       ...                                  ...

 Initialisation : c’est très dur mais on peut se contenter de mettre les premiers ab2 à 0 et
les premiers ab1 à 1 (et le système se corrige par la suite).

          (CY Tech)                Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   39 / 51
~~~

## Page 40

~~~text
Remarque 2
Les deux méthodes ci-dessus (saisonnière additive et saisonnière multiplicative)
    ne peuvent être mises en place que si nous disposons d’un certain nombre de période
    pour estimer la partie périodique.
    Si le nombre de données est insuffisant, R renvoie un message d’erreur.
    On choisit la méthode saisonnière additive ou saisonnière multiplicative en fonction
    de l’aspect graphique des données.
    En gros :
         amplitudes constantes −→ méthode saisonnière additive,
         amplitudes non constantes −→ méthode saisonnière multiplicative.


▷ Conclusion.

    La méthode de lissage exponentiel est une méthode de prévision déterministe
    efficace, qui permet de prendre en compte :
                   - une tendance linéaire dans la série
                      - et une composante saisonnière



          (CY Tech)             Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   40 / 51
~~~

## Page 41

~~~text
(CY Tech)   Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   41 / 51
~~~

## Page 42

~~~text
            Annexe 1 : mise en œuvre sous R




(CY Tech)      Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   42 / 51
~~~

## Page 43

~~~text
Mise en œuvre sous R

▷ Les méthodes de lissages exponentiels sont disponibles sous R, grâce à la fonction
HoltWinters. Pour une série temporelle x, cette procédure permet :

    un lissage exponentiel simple :
    xlisse <- HoltWinters(x,alpha=α,beta=FALSE,gamma=FALSE),
    un lissage exponentiel double de paramètre 1 − α′ :
    xlisse <- HoltWinters(x,alpha=α, beta=β, gamma=FALSE) avec α = 1 − (α′ )2 ,
          −α′
    β= 11+α′ ,
    un lissage de Holt-Winters sans composante saisonnière :
    xlisse <- HoltWinters(x,alpha=α,beta=β,gamma=FALSE),
    un lissage Holt-Winters additif :
    xlisse <- HoltWinters(x,alpha=α,beta=β,gamma=γ,seasonal=”add”),

    un lissage Holt-Winters multiplicatif :
    xlisse <- HoltWinters(x,alpha=α,beta=β,gamma=γ,seasonal=”mul”).

▷ Pour un lissage de Holt-Winters avec composante saisonnière la série temporelle x doit
être un objet de type série temporelle, défini avec la fonction ts en précisant la
saisonnalité.

         (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   43 / 51
~~~

## Page 44

~~~text
Mise en œuvre sous R- affichage et visualisation des résultats

    summary(xlisse) : description de l’objet xlisse obtenu précédemment par la
    procédure HoltWinters,
    plot(xlisse) : représentation des valeurs observées et des valeurs lissées,

▷ Les prévisions à l’horizon h sont réalisées à l’aide de la fonction predict :
    p<-predict(xlisse,n.ahead=h) (attention le n fait partie de la commande et le h
    est une variable qui peut prendre les valeurs 1, 2, . . . ).
    Un intervalle de confiance peut être obtenu en validant (à TRUE) l’option
    prediction.interval.
    Tracer la prédiction et la série sur le même graphique :
    xlisse=HoltWinters(x,...);
    p=predict(xlisse,n.ahead=50); plot(xlisse,p).

Remarque : lorsqu’aucune valeur n’est précisée pour les constantes de lissage, un
algorithme interne à la procédure HoltWinters se charge d’estimer la meilleur constante
possible à partir de la série des observations.




          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   44 / 51
~~~

## Page 45

~~~text
(CY Tech)   Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   45 / 51
~~~

## Page 46

~~~text
                        Annexe 2
            Démonstration de la Proposition 1 :
               à LIRE et à COMPRNDRE




(CY Tech)      Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   46 / 51
~~~

## Page 47

~~~text
Démonstration de la Proposition 1

▷ Notons
                                                 −1
                                                nX
                              C (a1 , a2 ) =           (1 − α)j (xn−j − (a1 + a2 j))2 .
                                                j =0
▷ On commence par chercher les points critiques de C . Nous avons

                       ∂C                                 −1
                                                         nX
                              (a1 , a2 )    =     −2            (1 − α)j (xn−j − (a1 + a2 j)) ,
                       ∂ a1                              j =0

                       ∂C                                 −1
                                                         nX
                              (a1 , a2 )    =     −2            (1 − α)j j (xn−j − (a1 + aj)) .
                       ∂ a2                              j =0

▷ Nous cherchons donc (a1 , a2 ) solutions du système
    Pn−1         j                          Pn−1                              Pn−1
  − j =0 (1 − α) xn−j                            (1 − α)j a1                       (1 − α)j j a2
 
                                   +        j =0
                                                                         +     j =0
                                                                                                       =       0
                                                                                                                    (10)
  − Pn−1 (1 − α)j j x
 
                                    +
                                           Pn−1
                                                 (1 − α)j j a1           +
                                                                              Pn−1
                                                                                    (1 − α)j j 2 a2    =       0.
      j =0             n−j                  j =0                               j =0




           (CY Tech)                    Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025        47 / 51
~~~

## Page 48

~~~text
▷ Rappelons les formules
                               +∞                         1
                                      (1 − α)j
                               X
                                                    =         ,
                               j =0                       α
                              +∞                          1−α
                                     j(1 − α)j
                              X
                                                    =             ,
                              j =0                         α2
                            +∞                            (1 − α)(2 − α)
                                   j 2 (1 − α)j
                            X
                                                    =
                            j =0                                  α3


▷ On obtient donc, en remplaçant certaines sommes partielles de séries par leurs limites,
               P −1
             −α n    (1 − α)j xn−j                                        1−α a
        
        
               j =0
                                         +           a1           +        α      2         =     0
        
                                                                                                        (11)
         −α2 Pn−1 (1 − α)j jx
                                                                      (1−α)(2−α)
                                         +        (1 − α)a1       +                   a2    =    0.
        
               j =0           n−j                                          α


▷ Attention, les systèmes (10) et (11) ne sont pas équivalents. Plus n est grand, plus ils
se ressemblent.
▷ Nous allons continuer le calcul à partir du système (11) et c’est pour cela que l’on
parle de solution « asymptotique » dans l’énoncé de la proposition.


          (CY Tech)           Séries temporelles-Chapitre 4: LISSAGE-Exponentiel      26 janvier 2025   48 / 51
~~~

## Page 49

~~~text
▷ Posons (pour tout n)                                P −1
                            L1 (n) =
                                                     α n
                                                        j =0
                                                             (1 − α)j xn−j

                                                P −1
                                               α n    (1 − α)j L1 (n − j) .
                           
                            L (n) =
                              2                  j =0
▷ Nous remarquons que
                                                −1
                                               nX
                         L2 (n)       =    α          (1 − α)j L1 (n − j)
                                               j =0

                                              nX−1          n−Xj −1
                                      =    α2      (1 − α)j         (1 − α)i xn−j −i
                                              j =0           i =0
                                              nX−1
                     (k = i + j)      =    α2      xn−k (1 − α)k (k + 1) .
                                              k =0
▷ Le système devient alors
                 (                                        (1−α)
                                    −L1 (n) + a1 +           α   a2                     =0
                                                                 (1−α)(2−α)
                     −L2 (n) + αL1 (n) + (1 − α)a1 +                  α        a2       = 0.
▷ D’où

            −L1 (n)(2 − α) + a1 (2 − α) + L2 (n) − αL1 (n)                  −(1 − α)a1 =        0
                                                −L2 (n) + 2L1 (n)                =              a1 ,
         (CY Tech)                 Séries temporelles-Chapitre 4: LISSAGE-Exponentiel     26 janvier 2025   49 / 51
~~~

## Page 50

~~~text
et
                                                     α
                                    a2      =            (L1 (n) − a1 )
                                                   1−α
                                                     α
                                            =            (L2 (n) − L1 (n)) .
                                                   1−α
▷ Montrons que la fonction C est convexe. Pour (a1 , a2 ) et (b1, b2 ) dans R2 et λ ∈ [0;1],
nous avons
                                         −1
                                        nX
C (λ(a1 , a2 ) + (1 − λ)(b1 , b2 )) =          (1 − α)j (xn−j − (λa1 + (1 − λ)b1 + (λa2 + (1 − λ)b2 )j))2
                                        j =0
                                     −1
                                    nX
                                =          (1 − α)j (λ(xn−j − (a1 + ja2 )) + (1 − λ)(xn−j − (b1 + jb2 ))2
                                    j =0
                                                                           −1
                                                                          nX
                           (convexité de la fonction carré) ≤                    (1 − α)j [λ(xn−j − (a1 + ja2 ))2
                                                                          j =0

                                                                                 +(1 − λ)(xn−j − (b1 + jb2 ))2 ]
                                                                          = λC (a1 , a2 ) + (1 − λ)C (b1 , b2 ) .

Ce qui montre que la fonction C est convexe.
L’unique point critique est donc le minimum absolu.                                                             □

            (CY Tech)               Séries temporelles-Chapitre 4: LISSAGE-Exponentiel     26 janvier 2025    50 / 51
~~~

## Page 51

~~~text
(CY Tech)   Séries temporelles-Chapitre 4: LISSAGE-Exponentiel   26 janvier 2025   51 / 51
~~~
