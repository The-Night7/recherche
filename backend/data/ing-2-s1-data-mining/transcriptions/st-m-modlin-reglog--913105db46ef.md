# st-m-modlin-reglog.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1vQWJ3gOqxnnyAtjGN_uP7WXoWpdeDZdc) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                                                                             Régression logistique ou modèle binomial

                                                                                            où πj est la probabilité d’apparition de la jème modalité. Cette quantité est
        Régression logistique ou modèle                                                     estimée par le rapport nj /nk des effectifs observés sur un échantillon. Lorsque
                                                                                            la variable est binaire et suit une loi de Bernouilli de paramètre π, l’odds est le
                   binomial                                                                 rapport π/(1 − π) qui exprime une cote ou chance de gain.
                                                                                               Par exemple, si la probabilité d’un succès est 0.8, celle d’un échec est 0.2.
Résumé                                                                                      L’odds du succès est 0.8/0.2=4 tandis que l’odds de l’échec est 0.2/0.8=0.25.
                                                                                            On dit encore que la chance de succès est de 4 contre 1 tandis que celle d’échec
     Introduction au modèle linéaire et modèle linéaire général : la ré-                    est de 1 contre 4.
     gression logistique ou modèle binomial. Retour au plan du cours.
                                                                                            Table de contingence
1     Introduction                                                                    On considère maintenant une table de contingence 2 × 2 croisant deux va-
                                                                                   riables qualitatives binaires X 1 et X 2 . les paramètres de la loi conjointe se
   Dans ce chapitre, nous définissons le contexte pratique de la régression lo-
                                                                                   mettent dans une matrice :
gistique qui s’intéressent plus particulièrement à la description ou l’explication                                  
                                                                                                                      π11 π12
                                                                                                                                   
d’observations constitués d’effectifs comme, par exemple, le nombre de succès                                         π21 π22
d’une variable de Bernouilli lors d’une séquence d’essais. Contrairement aux
modèles du chapitre précédent basés sur l’hypothèse de normalité des obser- où πij = P [{X 1 = i} et {X 2 = j}] est la probabilité d’occurence de chaque
vations, les lois concernées sont discrètes et associées à des dénombrements : combinaison.
binomiale, multinomiale. Néanmoins, ce modèle appartient à la famille du mo-          – Dans la ligne 1, l’odds que la colonne 1 soit prise plutôt que la colonne 2
dèle linéaire général (annexe) et partagent à ce titre beaucoup d’aspects (esti-        est :
mation par maximum de vraisemblance, tests, diagnostics) et dont la stratégie                                                   π11
                                                                                                                        Ω1 =         .
de mise en œuvre, similaire au cas gaussien, n’est pas reprise.                                                                 π 12

   Une première section définit quelques notions relatives à l’étude de la liaison    – Dans la ligne 2, l’odds que la colonne 1 soit prise plutôt que la colonne 2
entre variables qualitatives. Elles sont couramment utilisées dans l’interpréta-        est :
                                                                                                                                π21
tion des modèles de régression logistique.                                                                              Ω2 =         .
                                                                                                                                π22
                                                                                   On appelle odds ratio (rapport de cote) le rapport
2     Odds et odds ratio
                                                                                                                                Ω1   π11 π22
Une variable                                                                                                              Θ=       =         .
                                                                                                                                Ω2   π12 π21
  Soit Y une variable qualitative à J modalités. On désigne la chance (ou
                                                                                                Ce rapport prend la valeur 1 si les variables sont indépendantes, il est supérieur
odds 1 de voir se réaliser la jème modalité plutôt que la kème par le rapport
                                                                                                à 1 si les sujets de la ligne 1 ont plus de chances de prendre la première colonne
                                                 πj                                             que les sujets de la ligne 2 et inférieur à 1 sinon.
                                       Ωjk =
                                                 πk                                                Exemple : supposons qu’à l’entrée dans une école d’ingénieurs, 7 garçons
  1. Il n’existe pas, même en Québécois, de traduction consensuelle de “odds” qui utilise néan- sur 10 sont reçus tandis que seulement 4 filles sur 10 le sont. L’odds des gar-
moins souvent le terme “cote”.                                                                  çons est alors de 0.7/0.3=2.33 tandis que celle des filles est de 0.4/0.6=0.67.


                                                                                        1
~~~

## Page 2

~~~text
                                                                                                                           Régression logistique ou modèle binomial


L’odds ratio est de 2.33/0.67=3.5. La chance d’être reçu est 3.5 plus grande logit est définie par
pour les garçons que pour les filles.
                                                                                                                          π                           ex
   L’odds ratio est également défini pour deux lignes (a, b) et deux colonnes                   g(π) = logit(π) = ln             avec g −1 (x) =            .
                                                                                                                        1−π                         1 + ex
(c, d) quelconques d’une table de contingence croisant deux variables à J et
K modalités. L’odds ratio est le rapport                                             Plusieurs raisons, tant théoriques que pratiques, font préférer cette dernière
          Ωa     πac πbd                                                          solution. Le rapport π/(1 − π), qui exprime une “cote”, est l’odds et la ré-
Θabcd =       =           estimé par l’odds ratio empirique Θ  b abcd = nac nbd . gression logistique s’interprète donc comme la recherche d’une modélisation
          Ωb     πad πbc                                                nad nbc
                                                                                  linéaire du “log odds” tandis que les coefficients de certains modèles expriment
                                                                                  des “odds ratio” c’est-à-dire l’influence d’un facteur qualitatif sur le risque (ou
3 Régression logistique                                                           la chance) d’un échec (d’un succès) de Z.
3.1     Type de données                                                              Cette section se limite à la description de l’usage élémentaire de la régres-
                                                                                  sion logistique. Des compléments concernant l’explication d’une variable qua-
   Cette section décrit la modélisation d’une variable qualitative Z à 2 moda- litative ordinale (plusieurs modalités), l’intervention de variables explicatives
lités : 1 ou 0, succès ou échec, présence ou absence de maladie, panne d’un avec effet aléatoire, l’utilisation de mesures répétées donc dépendantes, sont à
équipement, faillite d’une entreprise, bon ou mauvais client. . . . Les modèles rechercher dans la bibliographie.
de régression précédents adaptés à l’explication d’une variable quantitative ne
s’appliquent plus directement car le régresseur linéaire usuel Xβ ne prend pas 3.2 Modèle binomial
des valeurs simplement binaires. L’objectif est adapté à cette situation en cher-
                                                                                     On considère, pour i = 1, . . . , I, différentes valeurs fixées x1i , . . . , xqi des
chant à expliquer les probabilités
                                                                                  variables explicatives X 1 , . . . , X q . Ces dernières pouvant être des variables
                  π = P (Z = 1) ou 1 − π = P (Z = 0),                             quantitatives ou encore des variables qualitatives, c’est-à-dire des facteurs issus
                                                                                  d’une planification expérimentale.
ou plutôt une transformation de celles-ci, par l’observation conjointe des va-
riables explicatives. L’idée est en effet de faire intervenir une fonction réelle    Pour chaque groupe, c’est-à-dire pour chacune           PI des combinaisons de valeurs
monotone g opérant de [0, 1] dans R et donc de chercher un modèle linéaire de     ou facteurs, on   réalise n  i observations        (n   =    i=1 ni ) de la variable Z qui se
la forme :                                                                        mettent  sous  la forme   y 1 /n 1 , . . . , y I /n I  où yi désigne  le nombre de “succès”
                                            0
                                  g(πi ) = xi β.                                  observés  lors  des n i essais.  On      suppose      que toutes les observations  sont indé-
                                                                                  pendantes et qu’à l’intérieur d’un même groupe, la probabilité πi de succès est
   Il existe de nombreuses fonctions, dont le graphe présente une forme sig- constante. Alors, la variable Yi sachant ni et d’espérance E(Yi ) = ni πi suit
moïdale et qui sont candidates pour remplir ce rôle, trois sont pratiquement une loi binomiale B(ni , πi ) dont la fonction de densité s’écrit :
disponibles dans les logiciels :                                                                                              
                                                                                                                                ni yi
probit : g est alors la fonction inverse de la fonction de répartition d’une loi                       P (Y = yi ) =                  πi (1 − πi )(ni −yi ) .
      normale, mais son expression n’est pas explicite.                                                                         y  i

log-log avec g définie par                                                           On suppose que le vecteur des fonctions logit des probabilités π appartient  i
                                g(π) = ln[− ln(1 − π)]                                    au sous-espace vect{X 1 , . . . , X q } engendré par les variables explicatives :

      mais cette fonction est dissymétrique.                                                                       logit(πi ) = x0i β   i = 1, . . . , I


                                                                                      2
~~~

## Page 3

~~~text
                                                                                                                     Régression logistique ou modèle binomial


ce qui s’écrit encore                                                                       Ceci s’interprète en disant que Y a eb fois plus de chance de succès (ou
                                   0
                                                                                            de maladie comme par un exemple un cancer du poumon) quand X = 1
                                 exi β                                                      (par exemple pour un fumeur).
                        πi =           0   i = 1, . . . , I.
                               1 + exi β
                                                                                      3.3     Régressions logistiques polytomique et ordinale
   Le vecteur des paramètres est estimé par maximisation de la log-
vraisemblance. Il n’y a pas de solution analytique, celle-ci est obtenue par des      La régression logistique adaptée à la modélisation d’une variable dichoto-
méthodes numériques itératives (par exemple Newton Raphson) dont certaines         mique   se généralise au cas d’une variable Y à plusieurs modalités ou polyto-
reviennent à itérer des estimations de modèles de régression par moindres car-     mique.   Si ces modalités sont ordonnés, on dit que la variable est qualitative
rés généralisés avec des poids et des métriques adaptés à chaque itération.        ordinale. Ces types de modélisation sont très souvent utilisés en épidémiologie
                                                                                   et permettent d’évaluer ou comparer des risques par exemples sanitaires. Des
   L’optimisation fournit une estimation b de β, il est alors facile d’en déduire estimations d’odds ratio ou rapports de cotes sont ainsi utilisés pour évaluer et
les estimations ou prévisions des probabilités πi :                                interpréter les facteurs de risques associés à différents types (régression poly-
                                           x0i b                                   tomique) ou seuils de gravité (régression ordinale) d’une maladie ou, en mar-
                                         e
                                 π
                                 bi =            0                                 keting, cela s’applique à l’explication, par exemple, d’un niveau de satisfaction
                                       1 + ex i b                                  d’un client. Il s’agit de comparer entre elles des estimations de fonctions logit.
et ainsi celles des effectifs                                                         Dans une situation de data mining ou fouille de données, ce type d’approche
                                   ybi = ni π
                                            bi .                                   se trouve lourdement pénalisé lorsque, à l’intérieur d’un même modèle polyto-
                                                                                   mique ou ordinal, plusieurs types de modèles sont en concurrence pour chaque
Remarques                                                                          fonction logit associée à différentes modalités. Différents choix de variables,
                                                                                   différents niveaux d’interaction rendent trop complexe et inefficace cette ap-
  1. La matrice X issue de la planification expérimentale est construite avec proche. Elle est à privilégier uniquement dans le cas d’un nombre restreint de
      les mêmes règles que celles utilisées dans le cadre de l’analyse de co- variables explicatives avec un objectif explicatif ou interprétatif.
      variance mixant variables explicatives quantitatives et qualitatives. Ainsi,
      les logiciels gèrent avec plus ou moins de clarté le choix des variables        À titre illustratif, explicitons le cas simple d’une variable Y à k modalités
      indicatrices et donc des paramètres estimables ou contrastes associés.       ordonnées   expliquée par une seule variable dichotomique X. Notons πj (X) =
                                                                                                          Pk
                                                                                   P (Y = j|X) avec j=1 πj (X) = 1. Pour une variable Y à k modalités, il
  2. La situation décrite précédemment correspond à l’observation de données
                                                                                   faut, en toute rigueur, estimer k − 1 prédicteurs linéaires :
      groupées. Dans de nombreuses situations concrètes et souvent dès qu’il y
      a des variables explicatives quantitatives, les observations xi sont toutes                     gj (X) = αj + βj X pourj = 1, . . . , k − 1
      distinctes. Ceci revient donc à fixer ni = 1; i = 1, . . . , I dans les ex-
      pressions précédentes et la loi de Bernouilli remplace la loi binomiale. et, dans le cas d’une variable ordinale, la fonction lien logit utilisée doit tenir
      Certaines méthodes ne sont alors plus applicables et les comportements compte de cette situation particulière.
      asymptotiques des distributions des statistiques de test ne sont plus va-       Dans la littérature, trois types de fonction sont considérées dépendant de
      lides, le nombre de paramètres tendant vers l’infini.                        l’échelle des rapports de cote adoptée :
 3. Dans le cas d’une variable explicative X dichotomique, un logiciel                 – échelle basée sur la comparaison des catégories adjacentes deux à deux,
    comme SAS fournit, en plus de l’estimation d’un paramètre b, celle des             – sur la comparaison des catégories adjacentes supérieures cumulées,
    odds ratios ; b est alors le log odds ratio ou encore, eb est l’odds ratio.        – et enfin sur la comparaison des catégories adjacentes cumulées.


                                                                                  3
~~~

## Page 4

~~~text
                                                                                                                   Régression logistique ou modèle binomial


Pour k = 2, on retrouve les trois situations se ramènent à la même d’une              4.1   Recherche pas à pas
variable dichotomique. C’est le dernier cas qui est le plus souvent adopté ; il
conduit à définir les fonctions des “logits cumulatifs” de la forme :                 Principalement deux critères (test du rapport de vraisemblance et test de
                                                                                   Wald, cf. bibliographie), sont utilisés de façon analogue au test de Fisher du
                                                                                   modèle linéaire gaussien. Ils permettent de comparer un modèle avec un sous-
                      πj+1 + · · · + πk                                            modèle et d’évaluer l’intérêt de la présence des termes complémentaires. On
                  log                     pourj = 1, . . . , k − 1.                suit ainsi une stratégie descendante à partir du modèle complet. L’idée est de
                       π1 + · · · + πj
                                                                                   supprimer, un terme à la fois, la composante d’interaction ou l’effet principal
                                                                                   qui apparaît comme le moins significatif au sens du rapport de vraisemblance
                                                                                   ou du test de Wald. Les tests présentent une structure hiérarchisée. SAS faci-
Pour un seuil donné sur Y , les catégories inférieures à ce seuil, cumulées, sont
                                                                                   lite cette recherche en produisant une décomposition (Type III) de ces indices
comparées aux catégories supérieures cumulées. Les fonctions logit définies
                                                                                   permettant de comparer chacun des sous-modèles excluant un des termes avec
sur cette échelle dépendent chacune de tous les effectifs, ce qui peut conduire
                                                                                   le modèle les incluant tous.
à une plus grande stabilité des mesures qui en découlent.
                                                                                      Attention, du fait de l’utilisation d’une transformation non linéaire (logit),
   Si les variables indépendantes sont nombreuses dans le modèle ou si la va-
                                                                                   même si des facteurs sont orthogonaux, aucune propriété d’orthogonalité ne
riable réponse Y comporte un nombre élevé de niveaux, la description des
                                                                                   peut être prise en compte pour l’étude des hypothèses. Ceci impose l’élimina-
fonctions logit devient fastidieuse. La pratique consiste plutôt à déterminer un
                                                                                   tion des termes un par un et la ré-estimation du modèle. D’autre part, un terme
coefficient global b (mesure d’effet) qui soit la somme pondérée des coeffi-
                                                                                   principal ne peut être supprimé que s’il n’intervient plus dans des termes d’in-
cients bj . Ceci revient à faire l’hypothèse que les coefficients sont homogènes
                                                                                   teraction.
(idéalement tous égaux), c’est-à-dire à supposée que les rapports de cotes sont
proportionnels. C’est ce que calcule implicitement la procédure LOGISTIC de 4.2 Critère
SAS appliquée à une variable réponse Y ordinale en estimant un seul para-
mètre b mais k − 1 termes constants correspondant à des translations de la            L’approche précédente favorise la qualité d’ajustement du modèle. Dans un
fonctions logit. La procédure LOGISTIC fournit le résultat du test du score sur    but  prédictif, certains logiciels, comme Splus/R ou Enterpirse Miner, proposent
l’hypothèse H0 de l’homogénéité des coefficients βj .                              d’autres  critères de choix (AIC, BIC). Une estimation de l’erreur de prévision
                                                                                   par validation croisée est aussi opportune dans une démarche de choix de mo-
   Le coefficient b mesure donc l’association du facteur X avec la gravité de la
                                                                                   dèle.
maladie et peut s’interpréter comme suit : pour tout seuil de gravité choisi sur
Y , la cote des risques d’avoir une gravité supérieure à ce seuil est eb fois plus
grande chez les exposés (X = 1) que chez les non exposés (X = 0).                  5 Illustration élémentaire
  Attention dans SAS, la procédure LOGISTIC adopte une paramétrisation
(−1, 1) analogue à celle de la procédure CATMOD mais différente de celle
                                                                           5.1 Les données
de GENMOD ou SAS/Insight (0, 1). Ceci explique les différences observées      On étudie l’influence du débit et du volume d’air inspiré sur l’occurence
dans l’estimation des paramètre d’une procédure à l’autre mais les modèles (codée 1) de la dilatation des vaisseaux sanguins superficiels des membres in-
sont identiques.                                                           férieurs. Un graphique élémentaire représentant les modalités de Y dans les
                                                                           coordonnées de X 1 × X 2 est toujours instructif. Il montre une séparation rai-
                                                                           sonnable et de bon augure des deux nuages de points. Dans le cas de nom-
4 Choix de modèle                                                          breuses variables explicatives quantitatives, une analyse en composantes prin-



                                                                                  4
~~~

## Page 5

~~~text
                                                                                                                           Régression logistique ou modèle binomial


                                                                                 cipales s’impose. Les formes des nuages représentés, ainsi que l’allure des
                                                                                 distributions (étudiées préalablement), incitent dans ce cas à considérer par la
                                                                                 suite les logarithmes des variables. Une variable un ne contenant que des “1”
                                                                                 dénombrant le nombre d’essais est nécessaire dans la syntaxe de genmod. Les
                                                                                 données sont en effet non groupées.

                                                                                 proc logistic data=sasuser.debvol;
                                                                                 model dilat=l_debit l_volume;
                                                                                 run;
              DEBIT                                                              proc genmod data=sasuser.debvol;
                  4                                                              model dilat/un=l_debit l_volume/d=bin;
                                                                                 run;
                     3
                                                                                 The LOGISTIC Procedure
                                                                                                               Intercept
                                                                                                 Intercept        and
                     2                                                            Criterion        Only       Covariates    Chi-Square for Covariates
                                                                                  AIC               56.040        35.216         .
                                                                                  SC                57.703        40.206         .
                                                                                  -2 LOG L          54.040        29.216(1)    24.824 with 2 DF (p=0.0001)
                                                                                  Score               .             .          16.635 with 2 DF (p=0.0002)
                     1                                                                         Parameter(2) Standard    Wald(3)   Pr >    Standardized   Odds
                                                                                 Variable DF    Estimate    Error   Chi-Square Chi-Square Estimate       Ratio
                                                                                 INTERCPT 1       2.8782    1.3214     4.7443    0.0294            .      .
                                                                                 L_DEBIT 1       -4.5649    1.8384     6.1653    0.0130    -2.085068     0.010
                     0                                                           L_VOLUME 1      -5.1796    1.8653     7.7105    0.0055    -1.535372     0.006


                         0       1       2       3        4
                                                                                    Cette procédure fournit des critères de choix de modèle dont la déviance
                                     VOLUME                                      (1), le vecteur b des paramètres (2) et les statistiques des tests (3) comparant
               DILAT                   0                 1                       le modèle excluant un terme par rapport au modèle complet tel qu’il est décrit
                                                                                 dans la commande.

F IGURE 1 – Dilatation : Nuage des modalités de Y dans les coordonnées des                    Criteria For Assessing Goodness Of Fit
variables explicatives.                                                                 Criterion              DF         Value      Value/DF
                                                                                        Deviance               36       29.2156        0.8115 (1)
                                                                                        Scaled Deviance        36       29.2156        0.8115 (2)
                                                                                        Pearson Chi-Square     36       34.2516        0.9514 (3)
                                                                                        Scaled Pearson X2      36       34.2516        0.9514
                                                                                        Log Likelihood           .     -14.6078             .
                                                                                                    Analysis Of Parameter Estimates
                                                                                    Parameter    DF     Estimate (4) Std Err    ChiSquare (5) Pr>Chi
                                                                                    INTERCEPT     1      -2.8782      1.3214      4.7443      0.0294
                                                                                    L_DEBIT       1       4.5649      1.8384      6.1653      0.0130
                                                                                    L_VOLUME      1       5.1796      1.8653      7.7105      0.0055
                                                                                    SCALE (6)     0       1.0000      0.0000           .       .



                                                                             5
~~~

## Page 6

~~~text
                                                                                                                         Régression logistique ou modèle binomial


                                                                                                        sexe     Sfem vs Shom      0.536       0.511        0.562
                                                                                                        alcool   A_bu vs Ajeu      0.367       0.340        0.395
    (1)    Déviance du modèle par rapport au modèle saturé.                                             ceinture Cnon vs Coui      0.801       0.748        0.858
    (2)    Déviance pondérée si le paramètre d’échelle est différent de 1 en cas de sur-dispersion.
    (3)    Statistique de Pearson, voisine de la déviance, comparant le modèle au modèle saturé .
    (4)    Paramètres du modèle.
    (5)    Statistique des tests comparant le modèle excluant un terme par rapport au modèle complet.
    (6)    Estimation du paramètre d’échelle si la quasi-vraisemblance est utilisée.

5.2       Régression logistique ordinale
   On étudie les résultats d’une étude préalable à la législation sur le port de
la ceinture de sécurité dans la province de l’Alberta à Edmonton au Canada
(Jobson, 1991). Un échantillon de 86 769 rapports d’accidents de voitures ont
été compulsés afin d’extraire une table croisant :
 1. Etat du conducteur : Normal ou Alcoolisé
 2. Sexe du conducteur
 3. Port de la ceinture : Oui Non
 4. Gravité des blessures : 0 : rien à 3 : fatales
Les modalités de la variable à expliquer concernant la gravité de l’accident
sont ordonnées.

/* régression ordinale */
proc logistic data=sasuser.ceinture;
class sexe alcool ceinture;
model gravite=sexe alcool ceinture ;
weight effectif;
run;

                                              Standard          Wald
Parameter                 DF      Estimate       Error    Chi-Square    Pr > ChiSq
Intercept Gr0              1        1.8699      0.0236     6264.9373        <.0001
Intercept Gr1              1        2.8080      0.0269    10914.3437        <.0001
Intercept Gr2              1        5.1222      0.0576     7917.0908        <.0001
sexe      Sfem             1       -0.3118      0.0121      664.3353        <.0001
alcool    A_bu             1       -0.5017      0.0190      697.0173        <.0001
ceinture Cnon              1       -0.1110      0.0174       40.6681        <.0001
                                     Odds Ratio Estimates
                                              Point          95% Wald
            Effect                          Estimate      Confidence Limits



                                                                                               6
~~~
