# RLogistique-CM-2023-2024.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1ViCHJOqV1wPlgUnW8BJMCag1NSjyCcUU) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                Régression Logistique

                                     Zahraa Maatouk
                                Département de Mathématiques
                                 ING2-Génie Mathématiques



                                CYtech Cergy Paris Université




Zahraa Maatouk / CYtech Cergy          Modèle Linéaire ING2-GMA   2023/2024   1 / 29
~~~

## Page 2

~~~text
Plan I


1   Introduction



2   Spécification du modèle



3   Interprétation des coefficients



4   Estimation et test du modèle



    Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-GMA   2023/2024   2 / 29
~~~

## Page 3

~~~text
Plan



1   Introduction


2   Spécification du modèle


3   Interprétation des coefficients


4   Estimation et test du modèle




    Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-GMA   2023/2024   3 / 29
~~~

## Page 4

~~~text
Introduction à la Régression Logistique


 1
       La régression logistique s’applique au cas où :
          Y est qualitative à 2 modalités
          Xp qualitatives ou quantitatives

 2
       Le plus souvent appliquée à la santé :
          Identification des facteurs liés à une maladie
          Recherche des causes de décès ou de survie de
          patients



     Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA   2023/2024   4 / 29
~~~

## Page 5

~~~text
Plan



1   Introduction


2   Spécification du modèle


3   Interprétation des coefficients


4   Estimation et test du modèle




    Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-GMA   2023/2024   5 / 29
~~~

## Page 6

~~~text
Spécification du modèle


Contexte
    Y est une variable binaire :
       0 en cas de non occurrence de l’évènement.
       1 si occurrence.
    Y aléatoire et Xi non aléatoires.
    On cherche à expliquer la survenue d’un évènement.
    On cherche la probabilité de succès.
    On travaille en terme d’espérance.


  Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA   2023/2024   6 / 29
~~~

## Page 7

~~~text
Spécification du modèle

Notations
     On note
             (Y, X1 , X2 , . . . , Xp ) les variables de la population dont on extrait un
             échantillon de n individus i.

             (yi , xi ) est le vecteur des réalisations de (Yi , Xi ).

             p variables explicatives.


Objectif
    Décrire la liaison entre Y et les (X1 , . . . , Xp ) et prédire les valeurs prises par
    Y.
             Régression logistique simple (p = 1)
             Régression logistique multiple (p > 1)



   Zahraa Maatouk / CYtech Cergy           Modèle Linéaire ING2-GMA            2023/2024    7 / 29
~~~

## Page 8

~~~text
Spécification du modèle

Contexte
    Le but est de prédire la valeur de Y par 0 ou 1. On définit la probabilité
    p = p(x) = P (Y = 1/X = x). Si p > 0.5 alors Yb = 1 et si p < 0.5 donc
    Yb = 0.
    Pour calculer la valeur de p qui nous permet de prédire la valeur de Y , on
    utilise la fonction logistique définie par :

                                                        p(x)
                                  logit(p(x)) = ln             = β0 + β1 x.
                                                      1 − p(x)

    Donc,
                                         p(x)
                                                = exp(β0 + β1 x).
                                       1 − p(x)
    et
                                    exp(β0 + β1 x)              1
                       p(x) =                        =                       .
                                  1 + exp(β0 + β1 x)   1 + exp(−(β0 + β1 x))


  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-GMA           2023/2024   8 / 29
~~~

## Page 9

~~~text
Plan



1   Introduction


2   Spécification du modèle


3   Interprétation des coefficients


4   Estimation et test du modèle




    Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-GMA   2023/2024   9 / 29
~~~

## Page 10

~~~text
Interprétation des coefficients
Cas d’une seule variable exogène binaire
Définition 1 (Odds ou Côte)
    Soit p une probabilité. L’odds (chance ou côte) ou rapport de chances est
    défini comme un rapport de probabilités dans un groupe. L’odds est défini
    par :
                                  p(x)      P(Y = 1 | X = x)
                     Oddsp =             =                    .
                                1 − p(x)    P(Y = 0 | X = x)
    Par exemple, si un étudiant a 3 chances sur 4 d’être reçu, contre 1 chance sur
    4 d’être collé, son Odds est de “ 3 contre 1”, soit
                                                 3/4
                                   Odds =            = 3.
                                                 1/4

Règles d’affectation

    Si odds > 1 alors Yb = 1.
    Si odds < 1 alors Yb = 0.
  Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA       2023/2024      10 / 29
~~~

## Page 11

~~~text
Interprétation des coefficients

Définition 2 (Odds Ratio)
     L’odds ratio (rapport des chances) entre deux individus x et x′ est
                                                                       p(x)
                                                           Oddsx      1−p(x)
                                   RC = OR(x, x′ ) =              =    p(x′ )
                                                           Oddsx′
                                                                      1−p(x′ )


     C’est le rapport entre l’odds du groupe exposé et l’odds du groupe témoin.


Exemple
C’est le rapport des odds des probabilités d’avoir la maladie pour ceux qui ont un
symptôme X d’une part et de ceux qui ne l’ont pas d’autre part.

     OR=1, la maladie est indépendante du symptôme.
     OR>1, la maladie est plus fréquente pour les individus qui ont le symptôme.
     OR<1, la maladie est plus fréquente pour les individus qui n’ont pas le symptôme.

   Zahraa Maatouk / CYtech Cergy          Modèle Linéaire ING2-GMA               2023/2024   11 / 29
~~~

## Page 12

~~~text
Interprétation des coefficients



Cas d’une seule variable exogène binaire X de valeurs 0 et 1
                                   P(Yi =1 | X=1)
                                  1−P(Yi =1 | X=1)          exp(β0 + β1 )
               RC = OR =           P(Yi =1 | X=0)
                                                        =                 = exp(β1 ).
                                                              exp(β0 )
                                  1−P(Yi =1 | X=0)


    X = 0 : symptôme absent.
    X = 1 : symptôme présent.
    Y = 0 : la maladie est absente.
    Y = 1 : la maladie est présente.




  Zahraa Maatouk / CYtech Cergy           Modèle Linéaire ING2-GMA             2023/2024   12 / 29
~~~

## Page 13

~~~text
Interprétation des coefficients



Cas d’une seule variable exogène binaire X de valeurs 0 et 1
    Avec l’estimateur de β1 : OR = exp(β1 ), permet de comparer les individus
    qui possèdent le symptôme X avec ceux qui ne le possède pas. Pour cela, on
    compare le OR à 1.

    Avec l’estimateur de β0 : On peut calculer

                                                                 exp(β0 )
                                  P(Yi = 1 | X = 0) =                       .
                                                               1 + exp(β0 )

    C’est-à-dire la proportion observée de malades n’ayant pas le symptôme.




  Zahraa Maatouk / CYtech Cergy         Modèle Linéaire ING2-GMA                2023/2024   13 / 29
~~~

## Page 14

~~~text
Interprétation des coefficients


Cas d’une seule variable exogène quantitative



    X une variable quantitative (ex : âge).

    Y = 0 : la maladie est absente.

    Y = 1 : la maladie est présente.



    On a encore :
                                  Logit[P(Yi = 1 | X = x)] = β0 + β1 x.




  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-GMA       2023/2024   14 / 29
~~~

## Page 15

~~~text
Interprétation des coefficients
Modèle logistique multiple

Dans le cas où on a plusiers variables exogène X1 , ..., Xp binaires ou quantitatives.
Le modèle devient :
                              p(x)
          logit(p(x)) = ln            = β0 + β1 X1 + β2 X2 + ... + βp Xp .
                           1 − p(x)
Donc,
                         p(x)
                                = exp(β0 + β1 X1 + β2 X2 + ... + βp Xp ).
                       1 − p(x)
     Exemple :
           Logit[P(M aladie = 1 | Age, f ume)] = β0 + β1 × Age + β2 × f ume,
     avec βb0 = 1.3982, βb1 = 0.4118 et βb2 = 0.6708.
     L’interprétation de β0 n’a pas de sens.
     OR = exp(β1 ) = 1.5068 > 1 : Si l’âge augmente d’une unité, le risque de
     contracter la maladie augmente.
     OR = exp(β2 ) = 1.9558 > 1 : Le risque de contracter la maladie est plus
     élevé si l’individu est fumeur.
   Zahraa Maatouk / CYtech Cergy        Modèle Linéaire ING2-GMA       2023/2024   15 / 29
~~~

## Page 16

~~~text
Plan



1   Introduction


2   Spécification du modèle


3   Interprétation des coefficients


4   Estimation et test du modèle




    Zahraa Maatouk / CYtech Cergy     Modèle Linéaire ING2-GMA   2023/2024   16 / 29
~~~

## Page 17

~~~text
Estimation et test du modèle

Maximum de vraisemblance

    Estimateurs des paramètres sans biais et de faible variance.
    n variables aléatoires Yi iid qui suivent une loi de B(pi ).
    La vraisemblance d’un n-échantillon y1 , y2 , . . . , yn est définie comme la
    probabilité d’observer cet échantillon.
        P(Yi = yi ) = pyi i (1 − pi )1−yi , avec pi = P(Y = yi | X = xi ).


    Les variables Yi étant indépendantes :
                                       n
                                       Y                                 n
                                                                         Y
            L(β, y1 , . . . , yn ) =         P(Y = yi | X = xi ) =         pyi i × (1 − pi )1−yi .
                                       i=1                               i=1




  Zahraa Maatouk / CYtech Cergy               Modèle Linéaire ING2-GMA              2023/2024        17 / 29
~~~

## Page 18

~~~text
Estimation et test du modèle


Maximum de vraisemblance

    On cherche βb = (βb0 , . . . , βbp ) qui maximise la vraisemblance du modèle. Or,
    selon le modèle logistique

                                                                exp(β0 + β1 xi )
                        pi = P(Y = 1 | X = xi ) =                                  .
                                                              1 + exp(β0 + β1 xi )

    Cela implique que
                                   n                 yi                    1−yi
                                  Y      eβ0 +β1 xi              eβ0 +β1 xi
                      L(β) =                               1 −                      .
                                  i=1
                                       1 + eβ0 +β1 xi          1 + eβ0 +β1 xi




  Zahraa Maatouk / CYtech Cergy             Modèle Linéaire ING2-GMA                   2023/2024   18 / 29
~~~

## Page 19

~~~text
Estimation et test du modèle

Maximum de vraisemblance

    On note L(β) = log(L(β)) := LL(β) Log-vraisemblance.
    Objectifs : trouver β0 et β1 qui maximisent la probabilité d’observer
    l’échantillon (i.e. maximisation de la vraisemblance) :

                                  max (L(β))             ⇔        max L(β).
                                  β0 ,β1                          β0 ,β1


    βb obtenu est un estimateur :
            asymptotiquement sans biais ;
            de variance minimale ;
            asymptotiquement normal (important pour l’inférence).
    On manipule souvent la quantité [−2LL] que l’on appelle DEVIANCE.
    Donc
                                  max L(β)            ⇔        min DM (β).
                                    β                            β



  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-GMA           2023/2024   19 / 29
~~~

## Page 20

~~~text
Estimation et test du modèle




La déviance donne la «distance» entre le modèle et les observations. Elle est utile
pour comparer des modèles en particulier le modèle basique ne contenant aucune
variable explicative et le modèle complet où on a toutes nos variables.




  Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA        2023/2024      20 / 29
~~~

## Page 21

~~~text
Estimation et test du modèle

Définition 3 (Déviance)
    Déviance résiduelle : on définit la déviance résiduelle par
                                    b) := DM = −2LL(βb0 , βb1 , . . . , βbp ).
                                  D(β

    Déviance nulle : on définit la déviance nulle (null deviance) par

                                       Dnul := D0 = −2LL(β
                                                         b0nul ),
       b0null a été calculé dans le modèle sans covariable, donc avec l’intercepte seul.
    où β
       ▶ La déviance nulle (D0 ) est calculée sur le modèle uniquement composée de la
         constante.

    DM est positive, et mesure l’écart entre les données et le modèle.
    Permet de quantifier la qualité d’ajustement du modèle, et la comparaison de modèles
    emboîté.

Remarque
    DM peut être comparer à la somme des carrés des résidus de la régression multiple.
    D0 correspondrait alors à la somme des carrés totaux.

  Zahraa Maatouk / CYtech Cergy            Modèle Linéaire ING2-GMA              2023/2024   21 / 29
~~~

## Page 22

~~~text
Estimation et test du modèle


Test 1 : Test de significativité globale

    Les variables explicatives influencent-elles simultanément le risque de
    survenue de l’événement ?
    On va effectuer un test du rapport de vraisemblance...
    M1 : Modèle sans variables
    M2 : Modèle avec toutes les variables
    On teste :
           
                     H0 : M1 ⇒ Logit[P(Y = 1)] = β0
                     H1 : M2 ⇒ Logit[P(Y = 1)] = β0 + β1 x1 + . . . + βp xp




  Zahraa Maatouk / CYtech Cergy       Modèle Linéaire ING2-GMA      2023/2024   22 / 29
~~~

## Page 23

~~~text
Estimation et test du modèle
Comme si on teste la nullité simultanée des p coefficients (β1 , . . . , βp ) :

                                   H0 : β 1 = . . . = β p = 0


     On utilise la statistique du rapport de vraisemblance

                                      LR = D(βbnul ) − D(β),
                                                         b

     qui suit, sous H0 , si n est grand, une loi du χ2 (p)
     on rejette H0 au niveau α si
                                         LR > qα ,
     où qα est la quantile de la loi de χ2 (p).

Remarque
     C’est l’équivalent du test de Fisher.
     Ce test revient à comparer la vraisemblance du modèle complet avec
     celle du modèle trivial constitué uniquement de la constante.
   Zahraa Maatouk / CYtech Cergy        Modèle Linéaire ING2-GMA        2023/2024   23 / 29
~~~

## Page 24

~~~text
Estimation et test du modèle
Test 2 : Test sur les modèles emboîtés
    Compare 2 modèles emboités :
       ▶ M1 : k paramètres
       ▶ M2 : p paramètres (p > k) qui contient toutes les paramètres de M1.
    Les hypothèses de test sont :
         H0 : on choisit M1 (meilleure qualité prédictive que le 2 mais moins de
                                    paramètres) VS
                   H1 : on choisit M2 (meilleure qualité prédictive).
    La statistique de test est :
                             
                      L(M1 )
       LR = −2 ln                = −2LL(M1 ) − (−2LL(M2 )) = DM 1 − DM 2 ,
                      L(M2 )

    où LL(M ) est la log-vraisemblance, D la déviance.
    Sous l’hypothèse H0 , les coefficients des variables supplémentaires que l’on
    retrouve dans M2 sont tous nuls. La statistique LR suit une loi du Khi-deux
    à p − k degrés de libertés.

  Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA         2023/2024       24 / 29
~~~

## Page 25

~~~text
Estimation et test du modèle



Test 3 : Tester la nullité de q (q < p) coefficients

    La démarche est toujours la même si nous souhaitons tester la nullité de q
    coefficients. On test
                             H0 : β1 = . . . = βq = 0
    On compare
       ▶ le modèle complet avec p variables
       ▶ au sous modèle emboîté avec βq+1 , βq+2 , . . . , βp coefficients, soit (p − q)
         variables.
    Le rapport de vraisemblance suit une loi du χ2 à (p − (p − q) = q) degrés
    de liberté.




  Zahraa Maatouk / CYtech Cergy       Modèle Linéaire ING2-GMA            2023/2024        25 / 29
~~~

## Page 26

~~~text
Estimation et test du modèle

Test 4 : Test de significativité d’un seul coefficient βj avec le test de
rapport de vraisemblance

     M1 : Modèle sans la variable testée βj
     M2 : Modèle avec la variable testée βj
     On teste :
         
          H0 : M1 ⇒ Logit[P(Y = 1)] = β0 + β1 x + . . . + βj−1 xj−1
                                            +βj+1 xj+1 + . . . + βp xp
             H1 : M2 ⇒ Logit[P(Y = 1)] = β0 + β1 x + . . . + βp xp
         

C’est-à-dire                       
                                       H0 : β j = 0
                                       H1 : βj ̸= 0
Pour tester la significativité d’un βj , il suffit de comparer la déviance du modèle
complet (avec βj ) et la déviance du modèle sans βj .

   Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA         2023/2024      26 / 29
~~~

## Page 27

~~~text
Estimation et test du modèle
Test 5 : Test de significativité d’un seul coefficient βj avec le test du Ward

    On teste l’hypothése : H0 βj = 0. Le test s’appuie sur la statistique de Wald

                                                   βbj2
                                        Wj =            ,
                                                   b2
                                                   σ
                                                     β
                                                     bj

       b2 est la variance du coefficient βbj .
    où σ
        βbj
    Sous H0 , Wj suit une loi du χ2 à 1 degré de liberté.

Remarque
Si n est assez grand, on peut utiliser la loi normale :
  ▶ Asymptotiquement, pour toute observation Xj , sous H0

                                          βbj2
                                  Zj =         ∼ N (0, 1).
                                          b2
                                          σ
                                            β
                                            bj
  Zahraa Maatouk / CYtech Cergy   Modèle Linéaire ING2-GMA      2023/2024     27 / 29
~~~

## Page 28

~~~text
Modèle avec interaction



Dans un modèle statistique classique, on fait l’hypothèse implicite que chaque
variable explicative est indépendante des autres. Cependant, cela ne se vérifie pas
toujours. Par exemple, l’effet de l’âge peut varier en fonction du genre. Il est donc
parfois nécessaire de prendre en compte dans un modèle les effets d’interaction.
Dans le cas d’un modèle logistique multiple, le modèle avec interaction peut
s’ecrire :

logit(p(x)) = β0 + β1 X1 + β2 X2 + ... + βp Xp + ...β12 X1 X2 + .. + βp−1p Xp−1 Xp

Si on accepte H0 alors on retire l’interaction.




  Zahraa Maatouk / CYtech Cergy    Modèle Linéaire ING2-GMA        2023/2024      28 / 29
~~~

## Page 29

~~~text
Estimation et test du modèle

Tester l’interaction
    On considère le modèle suivant avec les deux variables explicatives X1 et X2 :

                  Logit[P(Y = 1 | X1 , X2 )] = β0 + β1 X1 + β2 X2 + β3 X1 X2 .

    Si β3 est significative, alors X2 modifie l’effet de X1 . En effet, dans ce cas :
            Si X2 = 0 alors l’effet de X1 est β1
            Si X2 = 1 alors l’effet de X1 est β1 + β3 .
    On teste par le test du rapport de vraisemblance :
                                  
                                     H0 : β 3 = 0
                                     H1 : β3 ̸= 0

    Si on rejette H0 alors il y a modification d’effet et on laisse l’interaction dans
    le modèle.
    Si on accepte H0 alors on retire l’interaction.


  Zahraa Maatouk / CYtech Cergy       Modèle Linéaire ING2-GMA       2023/2024      29 / 29
~~~
