# Regression Linéaire Multiple-CM.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1jsb0dt9efAD_t956S3akpsgwzbRMaad4) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
               Régression Linéaire Multiple (ING2-GM)

                                  Nom : Zahraa Maatouk
                                Département de Mathématiques
                                 ING2-Génie Mathématiques



                                CYtech Cergy Paris Université




Zahraa Maatouk / CYtech Cergy           Modèle Linéaire ING2-MI   2024-2025   1 / 35
~~~

## Page 2

~~~text
Plan I


1   Introduction



2   Modèle et hypothèse



3   Estimation des paramètres du modèle : Approche analytique



4   Evaluation du modèle : Test de Fisher



    Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-MI     2024-2025   2 / 35
~~~

## Page 3

~~~text
Plan



1   Introduction


2   Modèle et hypothèse


3   Estimation des paramètres du modèle : Approche analytique


4   Evaluation du modèle : Test de Fisher




    Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-MI     2024-2025   3 / 35
~~~

## Page 4

~~~text
Introduction


    Le modèle de régression simple étudié auparavant est trop simpliste et n’est
    pas bien adapté à la réalité.
    On cherche ici à généraliser le modèle précédent en considérant non pas une
    mais plusieurs variables explicatives.
    La régression multiple est réservé en général au cas où les variables
    explicatives sont quantitatives.
       ▶ Si les variables explicatives sont qualitatives on parle d’analyse de la
         variance.
       ▶ Si les variables explicatives sont un mélange de variables qualitatives et
         quantitatives on parle de l’analyse de la covariance.
    La théorie statistique qui englobe ces diverses techniques constitue le modèle
    linéaire. C’est en économétrie que les modèles linéaires trouvent leurs champ
    d’application.




  Zahraa Maatouk / CYtech Cergy      Modèle Linéaire ING2-MI           2024-2025      4 / 35
~~~

## Page 5

~~~text
Plan



1   Introduction


2   Modèle et hypothèse


3   Estimation des paramètres du modèle : Approche analytique


4   Evaluation du modèle : Test de Fisher




    Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-MI     2024-2025   5 / 35
~~~

## Page 6

~~~text
Modèle

 ▶ On dispose d’un ensemble de n observations sur lesquelles ont été effectuées
   p mesures des variables X1 , X2 , . . . , Xp .
 ▶ On veut approcher Y par une combinaison linéaire des variables
   X1 , X2 , . . . , Xp .
 ▶ On pose le modèle théorique :

                   Yi = β0 + β1 Xi1 + β2 Xi2 + . . . + βp Xip + ϵi ,   i = 1, . . . , n.


            Yi est la réponse mesurée (ou observée) pour l’unité i, c’est une v.a. ;
            Xij est la valeur (observée) de Xj pour l’unité i ;
            β0 , β1 , . . . , βp sont les p + 1 paramètres inconnus du modèle ;
            β0 est le coefficient d’une variable explicative particulière artificielle X0 dont
            les valeurs Xi0 seraient toujours égales à 1 ;
            ϵi v.a. (résidu). Il quantifie les écarts entre les valeurs réellement observées et
            les valeurs prédites par le modèle.
            Il résume les informations manquantes qui permettent d’expliquer les valeurs
            de Y à l’aide des p variables Xj .

  Zahraa Maatouk / CYtech Cergy          Modèle Linéaire ING2-MI             2024-2025        6 / 35
~~~

## Page 7

~~~text
Hypothèses du modèle




    Les conditions standards imposées aux ϵi sont :

                   (C1)                    E(ϵi ) = 0,          ∀i = 1, . . . , n
                   (C2)       Cov(ϵi ; ϵj ) = 0,    ∀i = 1, . . . , n (non corrélation),
                   (C3)            Var(ϵi ) = σ 2 (inconnue) ∀i = 1, . . . , n :
                              (homogénéité des variances ou homoscédasticité).




  Zahraa Maatouk / CYtech Cergy              Modèle Linéaire ING2-MI                2024-2025   7 / 35
~~~

## Page 8

~~~text
Écriture vectorielle du modèle



                                                                                   
              Y1       1           X11   ...      X1j       ...      X1p         β0        ϵ1
              ..   ..            ..    ..       ..        ..       ..   ..  ..   .. 
              .  .                .     .        .         .        .    . .   . 
                                                                                   
               
              Yi  = 1           Xi1   ...       Xij      ...      Xip        β i  +  ϵi 
                                                                              
              ..   ..            ..    ..        ..       ..       ..    ..  ..   .. 
              .  .                .     .         .        .        .     .  .   . 
              Yn       1           Xn1   ...      Xnj       ...      Xnp         βp        ϵn
La première colonne représentant la constante 1 = (1, . . . , 1). Le modèle peut
donc s’écrire comme suit :
                                  Y = X β + ϵ,
avec ϵ = (ϵ1 , . . . , ϵn ) ∈ Rn .




   Zahraa Maatouk / CYtech Cergy               Modèle Linéaire ING2-MI                  2024-2025   8 / 35
~~~

## Page 9

~~~text
Hypothèses du modèle


 ▶ Sous les hypothèses (C1) à (C3) on a

                          E[ϵ] = 0n   vecteur nul de dimension n
                          E[Y ] = X β ∈ Rn
                          Var(ϵ) = Var(Y ) = σ 2 In         où In est la matrice identité.

 ▶ Nous supposons de plus que :
                                  (C4) la matrice X est de plein rang.
    C’est-à-dire qu’il n’existe pas de liaison linéaire entre les Xi :

                                  p+1<n          et rang(X ) = p + 1.

 ▶ Dans certains cas le modèle peut être sans constante (c’est-à-dire β0 et
   dim(X ) = p).



  Zahraa Maatouk / CYtech Cergy           Modèle Linéaire ING2-MI                2024-2025   9 / 35
~~~

## Page 10

~~~text
Hypothèses sur le modèle : Commentaires




 ▶ (C4) condition d’absence de colinéarité (ou de multicolinéarité), on dit aussi
   condition d’identification du modèle.
            Elle signifiée qu’aucune des p + 1 colonnes de X ne peut être exprimée comme
            une combinaison linéaire des autres colonnes.
            Conséquence : la présence d’une colinéarité dans le modèle ne permet pas
            d’interpréter les paramètres de ce modèle.
            Il faut que n > p + 1, c’est-à-dire que la taille de l’échantillon est supérieure
            au nombre de régresseurs.




  Zahraa Maatouk / CYtech Cergy        Modèle Linéaire ING2-MI            2024-2025       10 / 35
~~~

## Page 11

~~~text
Plan



1   Introduction


2   Modèle et hypothèse


3   Estimation des paramètres du modèle : Approche analytique


4   Evaluation du modèle : Test de Fisher




    Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-MI     2024-2025   11 / 35
~~~

## Page 12

~~~text
Estimateur des moindres carrés de β
 ▶ On cherche l’équation de la droite de régression en dimension p + 1 pour
   laquelle les erreurs quadratiques (ϵ2i ) sont les plus faibles. Ce qui est équivaut
   à minimiser la quantité
                   n
                   X              n
                                  X
          ϵ′ ϵ =         ϵ2i =          (Yi − β0 − β1 Xi1 − . . . − βp Xip )2 = ∥Y − X β∥2
                   i=1            i=1
                                                                              ϵ = Y − Xβ ⇒
                          ϵ ϵ = (Y − X β) (Y − X β) = Y Y − 2Y ′ X β + β ′ X ′ X β
                            ′                   ′                         ′


 ▶ Par dérivation (vectorielle...) par rapport à β, on obtient

                                            ∂ϵ′ ϵ
                                                  = −2X ′ Y + 2X ′ X β.
                                            ∂β
 ▶ La condition nécessaire d’extremum est l’annulation des dérivées partielles
   premières, ce qui conduit à choisir l’estimateur β tel que

                                                    X ′ X βb = X ′ Y .

  Zahraa Maatouk / CYtech Cergy                 Modèle Linéaire ING2-MI            2024-2025   12 / 35
~~~

## Page 13

~~~text
Calcule de βb




    Si n > p + 1 (c’est le cas général, avec un nombre d’observations supérieur à
    celui des paramètres).
       ▶ La résolution des équations normales nécessite X ′ X inversible auquel cas on
         obtient,
                                       βb = (X ′ X )−1 X ′ Y .




  Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-MI           2024-2025          13 / 35
~~~

## Page 14

~~~text
Exemple

On considère le tableau des données suivantes :
                                  Nb d’observation         X1           X2     Y
                                         1                 -1            -1    4
                                         2                 -1             1    2
                                         3                  1            -1    0
                                         4                  1             1    2
                                     Moyenne                0             0    0
                                     Variance               1             1    6
                                    Cov(Xj , Y )            1             2
                                    Cor(Xj , Y )          .408         0.816
Ici, on a p = 2 et n = 4. Le modèle

          Yi = β0 + β1 Xi1 + β2 Xi2 + ϵi ,              i = 1, . . . , 4       ⇔   Y = X β + ϵ.

                                  Y
                                  b = X β,
                                        b     avec βb = (X ′ X )−1 X ′ Y .


  Zahraa Maatouk / CYtech Cergy              Modèle Linéaire ING2-MI                   2024-2025   14 / 35
~~~

## Page 15

~~~text
Exemple (suite)



On a
                           
     1           −1      −1                                                         
                                         0             4          0   0                 0
    1           −1       1 , X ′ Y = 4 , X ′ X = 0
 X =                                                             4   0 = 4I3 et βb = 1
    1            1      −1
                                         8             0          0   4                 2
     1            1       1

Le modèle peut donc s’écrire, en notant Y
                                        bi la valeur prédite pour l’observation i :

                                    Y
                                    bi = 0 + 1Xi1 + 2Xi2 .




  Zahraa Maatouk / CYtech Cergy         Modèle Linéaire ING2-MI             2024-2025    15 / 35
~~~

## Page 16

~~~text
Prédictions et résidus


 ▶ Le modèle théorique : Y = X β + ϵ.
 ▶ Une fois que β a été estimé, nous pouvons reconstruire nos données à l’aide
   de notre modélisation.
            Le vecteur des n valeurs prédites ou des valeurs ajustées (fitted values) s’écrit :
                                                                                 p
                                                                                 X
                                  Y
                                  b = X βb,      ou encore          Y
                                                                    bi = βb0 +         βbj Xij .
                                                                                 j=1


            Le vecteur des résidus observés (residuals) :

                                    ϵ=Y −Y
                                    b    b                        ϵi = Yi − Y
                                                        ou encore b         bi .

            Remarque : Y
                       bi est un estimateur de E[Yi ].




  Zahraa Maatouk / CYtech Cergy               Modèle Linéaire ING2-MI                         2024-2025   16 / 35
~~~

## Page 17

~~~text
Propriétés des estimateurs




Moyenne et variance des coefficients


Proposition 1
 1     E[β]
         b = β.
 2          b = σ 2 (X ′ X )−1 .
       Var(β)




     Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-MI   2024-2025   17 / 35
~~~

## Page 18

~~~text
Estimation de la variance résiduelle
    La quantité σ 2 est la
                         Pvariance  théorique des résidus, elle est inconnue. On
                           n
    l’estime à partir de i=1 bϵ2i .

Proposition 2
             Pn
Le ddl de            ϵ2i = nb de données (n) - nb des paramètres estimés = n − p − 1.
                 i=1 b
                                     Pn                         Pn
                      2
                                                b 2
                                      i=1 (Yi − Yi )                       ϵ2i         ϵ′ b
                                                                                          ϵ
                          =: Sσ2 =                                     i=1 b           b
                  σ                                       =                      =          .
                                       n−p−1                   n−p−1                 n−p−1
                  b

Remarque :
                                                                σ2 ] = σ2
                On montre que cet estimateur est sans biais : E[b
                   On en déduit un estimateur sans biais de Var(β)b


                                          Var(β) b2 (X ′ X )−1
                                              b =σ

                          L’erreur standard de βbj est σ           b2 (X ′ X )−1
                                                       b2 (βbj ) = σ          jj

  Zahraa Maatouk / CYtech Cergy              Modèle Linéaire ING2-MI                      2024-2025   18 / 35
~~~

## Page 19

~~~text
Exemple : estimation de la variance résiduelle



On utilise les données de l’exemple précédent, on obtient :

                            Nb d’observation      X1       X2      Y   Y
                                                                       b     ϵ
                                                                             b
                                   1              -1       -1      4   -3   -1
                                   2              -1       1       2    1    1
                                   3               1       -1      0   -1   1
                                   4               1       1       2    3   -1
                   P4                                             4
Ce qui donne               ϵ2i = 4, ddl = 4 − 2 − 1 = 1 et σ
                       i=1 b                               b2 = 4−2−1 = 4.




  Zahraa Maatouk / CYtech Cergy          Modèle Linéaire ING2-MI                 2024-2025   19 / 35
~~~

## Page 20

~~~text
Décomposition de la variance


La formule de la décomposition de la variance est :

                                  SCT    = SCE + SCR
                      n
                      X                    Xn             n
                                                          X
                            (Yi − Y )2   =             2
                                              (Yi − Y ) +
                                               b                  bi )2
                                                            (Yi − Y
                      i=1                     i=1                    i=1



                              Variabilité      notion          degrés de liberté
                                Total           SCT                 n−1
                            Due au modèle       SCE                   p
                              Résiduelle        SCR               n−p−1




  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-MI                 2024-2025   20 / 35
~~~

## Page 21

~~~text
Qualité de l’ajustement- R 2


Définition 1 (Coefficient de détermination)
 ▶ Le coefficient de détermination R 2 , donne le pourcentage de variance de Y
   expliquée par le modèle, il est défini par
                                   variance expliquée par le modèle   SCE
                            R2 =                                    =     ,
                                            variance totale           SCT
 ▶ Le R 2 peut aussi s’écrire en fonction des résidus

                                                  ϵ∥2
                                                 ∥b          SCR
                                   R2 = 1 −              =1−     .
                                              ∥Y − Y 1∥2     SCT

Le coefficient de détermination augmente automatiquement avec le nombre de
variables dans le modèle. On ne peut donc pas comparer deux modèles ayant un
nombre de variables différent. Pour cela, c’est mieux d’utiliser une version pondére
par le nombre de coefficients : le coefficient de détermination ajusté.


  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-MI       2024-2025   21 / 35
~~~

## Page 22

~~~text
Qualité de l’ajustement- R 2


Définition 2
 ▶ Le coefficient de détermination ajusté Ra2 est défini par

                                                   n ∥b ϵ∥ 2
                                  Ra2 = 1 −                  .
                                                 n − p ∥Y ∥2
 ▶ Si la constante fait partie des estimateurs par

              SCR/(n − p − 1)        n−1         ϵ∥2
                                                ∥b            n−1
    Ra2 =                     = 1−                      = 1−       (1−R 2 ).
               SCT /(n − 1)        n − p − 1 ∥Y − Y 1∥2      n−p−1

    Le coefficient de détermination ajusté peut prendre des valeurs négatives.
    Ra2 n’augmente pas forcément lorsque le nombre de variables introduites dans
    le modèle augmente.



  Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-MI      2024-2025       22 / 35
~~~

## Page 23

~~~text
Exemple



Nous retournons de l’exemple précédent, nous obtenons :
                              Variabilité      SC                    ddl
                                totale      SCT = 24               n−1=3
                              du modèle     SCE = 20                p=2
                              Résiduelle     SCR = 4              n−p−1=1
             SCE   20
Ainsi, R 2 = SCT = 24 = 0.833. Enfin,

                                  SCR/(n − p − 1)    4     12
                          Ra2 =                   =      =    = 0.5.
                                   SCT /(n − 1)     24/3   24




  Zahraa Maatouk / CYtech Cergy             Modèle Linéaire ING2-MI         2024-2025   23 / 35
~~~

## Page 24

~~~text
Plan



1   Introduction


2   Modèle et hypothèse


3   Estimation des paramètres du modèle : Approche analytique


4   Evaluation du modèle : Test de Fisher




    Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-MI     2024-2025   24 / 35
~~~

## Page 25

~~~text
Hypothèse supplémentaire : cas gaussien


 ▶ On ajoute l’hypothèse de normalité des erreurs :

                                    ϵi ∼ N (0, σ 2 )       ⇒        Yi ∼ N (βXi , σ 2 ).

 ▶ Matriciellement

                                  ϵ ∼ N (0n , σ 2 In )      ⇒        Y ∼ N (X β, σ 2 In ).

 ▶ Sous l’hypothèse de normalité, on a

                                             Var(ϵ) = Var(Y ) = σ 2 In .

 ▶ Le ϵ et les Yi sont indépendants.
 ▶ A noter que les variables {ϵi } sont maintenant supposées i.i.d. (mais les Yi
   seulement indépendantes).



  Zahraa Maatouk / CYtech Cergy                  Modèle Linéaire ING2-MI                     2024-2025   25 / 35
~~~

## Page 26

~~~text
Évaluation globale du modèle : Test de Fisher


    L’évaluation globale du modèle se fait par le bais du coefficient de
    détermination qui se déduit du tableau de l’analyse de variance ci-dessous :
                          n
                          X                          n
                                                     X                      n
                                                                            X
                            (Yi − Y )2        =              bi − Y )2 +
                                                            (Y                      bi )2
                                                                              (Yi − Y
                          i=1                         i=1                   i=1
                                       SCT    = SCE + SCR

    Tableau d’analyse de variance (ANOVA)

  Source de variation             Somme des carrés      Degrés de liberté          Carrés moyens
        Totale                        SCT                    n−1
       Modèle                         SCE                      p                 CMM := SCE /p
      Résiduelle                      SCR                  n−p−1              CMR := SCR/(n − p − 1)




  Zahraa Maatouk / CYtech Cergy                Modèle Linéaire ING2-MI                2024-2025        26 / 35
~~~

## Page 27

~~~text
Évaluation globale du modèle : Test de Fisher (suite)

 ▶ Hypothèses à tester :

          H0 : βj = 0, ∀j = 1, . . . , p          aucun prédicteur n’a un influence sur Y

    Remarque : (la constante β0 n’est pas concernée : elle ne traduit pas
    l’influence des pérdicteurs).
 ▶ Statistique de test : On peut montrer que sous H0

                                            SCE /p
                                  Fn =                   ∼ Fp,n−p−1 .
                                         SCR/(n − p − 1)
 ▶ Zone de rejet : La zone de rejet associé é cette statistique est :

                                    W = {X1 , . . . , Xn | Fobs > c},

    où c est la limite de la zone de rejet de W . Il est défini par 1 − α quantile de
    la loi de Fp,n−p−1 .


  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-MI          2024-2025       27 / 35
~~~

## Page 28

~~~text
Évaluation globale du modèle : Test de Fisher-(suite)


 ▶ Règle de décision
       ▶ Nous décidons de rejeter H0 et d’accepter H1 , au seuil α, si

                                      Fobs ≥ Fp,n−p−1 (1 − α).

       ▶ On peut aussi utiliser la probabilité critique pc := P(Fn ≥ Fobs ).
       ▶ Si pc < au seuil de risque α, on rejette l’hypothèse selon laquelle la variable Xj
         n’a pas d’influence réelle (avec un risque de α%).
 ▶ Remarque. Lien entre teste F et coefficient de détermination R 2 : On peut
   montrer que
                                 n − p − 1 R2
                            Fn =                    .
                                      p      1 − R2




  Zahraa Maatouk / CYtech Cergy      Modèle Linéaire ING2-MI             2024-2025      28 / 35
~~~

## Page 29

~~~text
Exemple : Évaluation globale du modèle : Test de Fisher


Application à l’exemple précédent

 Variabilité        Somme carrés      ddl                     Carrés moyens               Test
  Totale             SCT = 24       n−1=3
  Modèle             SCE = 20        p=2                       CMM = 10             Fobs =
                                                                                   CMM
                                                                                   CMR = 2.5
 Résiduelle             SCR = 4    n−p−1=1                      CMR = 4       p − value = 0.41

    La valeur Fobs = 2.5 est inférieure à la limite de zone Fνν21=1
                                                                 =2
                                                                    (0.95) = 200.
                                   On accepte donc H0 .
    On aboutit au même résultat en comparant la probabilité critique pc = 0.41 à
    α = 0.05 avec l’avantage que l’on se rend alors mieux compte que l’on est
    loin de la significativité.



  Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-MI                   2024-2025          29 / 35
~~~

## Page 30

~~~text
Test de signification d’un coefficient de régression : Test de
Student

    Lorsque le test global est significatif, on doit s’interroger sur :
         la signification de chaque coefficient ou la conformité de chaque βj à 0.
    On doit choisir entre :

                                  H0 : βj = 0     le prédicteur Xj n’est pas influent
                                  H1 : βj ̸= 0    le prédicteur Xj est influent.

    On sait que : E[βbj ] = βj .
    La variance de βbj notée σ 2 est obtenue à partir du j e terme de la diagonale
                                 β
                                 bj
    de la matrice (X ′ X )−1 , soit :
                                              2
                                             σb = (X ′ X )−1  2
                                                          jj σ .
                                                 βj




  Zahraa Maatouk / CYtech Cergy              Modèle Linéaire ING2-MI               2024-2025   30 / 35
~~~

## Page 31

~~~text
Test de signification d’un coefficient de régression : Test de
Student

 ▶ En utilisant les hypothèses sur les résidus, on montre que :
                                                      2
                                  L(βbj ) = N (βj , σ
                                                    bb  ).
                                                             βj


 ▶ La variance σ 2 étant inconnue, on l’estime par σ
                                                   b2 , alors la variance de βbj est

                                   σ
                                   bb2
                                       = (X ′ X )−1 b2 .
                                                 jj σ
                                     βj


 ▶ Du fait de ce remplacement, la loi de βbj standardisée n’est plus une loi
   normale centrée réduite mais une loi de Student à n − p − 1 degrés de liberté.
   Soit                                  !
                                βbj − βj
                            L              = Tν=n−p−1 .
                                   σ
                                   bβb
                                          j




  Zahraa Maatouk / CYtech Cergy    Modèle Linéaire ING2-MI         2024-2025      31 / 35
~~~

## Page 32

~~~text
Test de signification d’un coefficient de régression : Test de
Student

 ▶ Donc sous H0 :                                !
                                         βbj
                                  L                  = Tν=n−p−1 .
                                         σ
                                         bβb
                                             j

 ▶ La décision d’accepter ou rejeter H0 sera basée sur l’indicateur

                                                        βbj
                                            tobs =          .
                                                        σ
                                                        bβb
                                                            j


 ▶ La zone de rejet est bilatérale puisque aussi bien des valeurs grandes que
   petites de tobs conduisent à rejeter H0 (Xj peut influer positivement ou
   négativement sur y ).
                              W =] − ∞, c1 [∪]c2 , +∞[.



  Zahraa Maatouk / CYtech Cergy       Modèle Linéaire ING2-MI       2024-2025   32 / 35
~~~

## Page 33

~~~text
Test de signification d’un coefficient de régression : Test de
Student


 ▶ Règle de décision
   Nous décidons de rejeter H0 et d’accepter H1 , au seuil α, si

                                           |tobs | > tn−p−1;α .

 ▶ Application : exemple précédent toujours :

                                  4        βb2   2
          b2 = 4,
          σ               σ 2
                              =     = 1,        = =2                 et tν=n−p−1 (0.05) = 12.71.
                                           b2
                          bb
                            β2    4        σ     1
                                             β
                                             b2

    Ainsi, tobs < tν=n−p−1 (0.05). Donc, on accepte l’hypothèse nulle H0 .
                                   La variable X2 n’influence pas Y .




  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-MI                 2024-2025       33 / 35
~~~

## Page 34

~~~text
Test sur un sous-ensemble de coefficients (Test entre
modèles emboîtés)


 ▶ Le test précédent permet de tester l’un après l’autre la nullité de chaque
   coefficient.
 ▶ Le test suivant permet de tester la nullité simultanée de plusieurs coefficients
   de régression.
 ▶ On cherche à tester la nullité des q ≤ p premiers paramètres :

            H0 : β1 = . . . = βq = 0      contre H1 : ∃k ∈ {1, . . . , q} : βk ̸= 0

    Cela revient à comparer deux modèles :
       ▶ le modèle complet à p regresseurs (modèle 1) pour lequel on évalue la somme
         des carrés des résidus SCR1,
       ▶ le modèle réduit à p − q regresseurs (modèle 0) pour lequel on évalue la
         somme des carrés des résidus SCR0.



  Zahraa Maatouk / CYtech Cergy        Modèle Linéaire ING2-MI         2024-2025      34 / 35
~~~

## Page 35

~~~text
Test entre modèles emboîtés



On peut montrer que sous H0 :

                   (SCR0 − SCR1)/q        ∥Y
                                           b0 − Yb ∥2 /q
           F =                      =                        ∼ Fq,n−p−1 .
                   SCR1/(n − p − 1)        b ∥2 /(n − p − 1)
                                      ∥Y − Y

L’hypothèse H0 sera repoussée en faveur de H1 si Fobs est supérieure à
Fq,n−p−1 (1 − α), la valeur α est le niveau du test.

Remarque :Ce test est utile pour faire de la modélisation pas à pas et sélectionner
un ensemble optimal de régresseurs nécessaires à la reconstruction de Y .




  Zahraa Maatouk / CYtech Cergy      Modèle Linéaire ING2-MI      2024-2025     35 / 35
~~~
