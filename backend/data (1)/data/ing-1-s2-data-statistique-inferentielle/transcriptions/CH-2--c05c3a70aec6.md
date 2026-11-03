# CH-2.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1WC-uhrGLMIEkwFejL-CRjMZje37QyL6Y) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Estimations
I Echantillon
Dénition.
   Un échantillon désigne un sous ensemble d'individus extraits d'une population, sur lesquels vont être
étudiées des grandeurs aléatoires.
   Soit une expérience aléatoire à laquelle on associe une v. a. r. X, tq. E(X) = m et V (X) = σ 2 . Un
échantillon de taille n ou un n-échantillon est une suite de v. a. r. X1 , · · · , Xn indépendantes et de même loi
que X .
                                                                                    n
                                                                       1X
   On appelle moyenne empirique sur cet échantillon, la v. a. r. X n =       Xi et on a :
                                                                       n i=1
                                     σ2
   E(X n ) = m et V (X n ) =
                                     n
                                                                                    n
                                                                                 1X            2
   On appelle variance empirique sur cet échantillon, la v. a. r. Sn2 =                Xi − X n on peut écrire la
                                                                                 n i=1
variance empirique d'une autre façon, en eet :
   n                         n
   X                2       X                            2
         Xi − X n        =         (Xi − m) − (X n − m)
   i=1                       i=1
                             n
                             X                                           n
                                                                         X
                                           2
                         =         (Xi − m) + n(X n − m)2 − 2(X n − m)         (Xi − m)
                             i=1                                         i=1
                             Xn
                                           2
                         =         (Xi − m) + n(X n − m)2 − 2(X n − m)[nX n − nm]
                             i=1
                             n
                             X             2
                         =         (Xi − m) − n(X n − m)2
                             i=1
                 n
              1X                          2
   d'où Sn2 =                2
                    (Xi − m) − X n − m
              n i=1
                        n
                     1X                                      2
   et donc E(Sn ) =
               2                          2
                           E (Xi − E(Xi )) − E X n − E(X n )
                     n i=1
                    1                              σ2
                  = · n V (X) − V (X n ) = V (X) −
                    n                              n
                 n−1 2
   d'où E(Sn ) =
           2
                      σ
                  n
   La valeur moyenne de la variance empirique n'est pas exsactement égale à la variance théorique, c'est




                                                               1
~~~

## Page 2

~~~text
pourquoi on introduit la variance empirique modiée :
                                               n                          n
                                 2        1 X                      n 1X
                               Sn =               (Xi − X n )2 =             (Xi − X n )2
                                        n − 1 i=1                n − 1 n i=1
                                                                       |       {z       }
                                                                               2
                                                                              Sn

               2
    d'où E(S n ) = σ 2 .

II Estimation
    On considère généralement deux types d'estimation : l'estimation ponctuelle (on cherche à estimer une
valeur) et l'estimation par intervalle de conance oé l'on estime la probabilité que la valeur vraie d'un
paramètre appartienne à un intervalle donné.

II.1     Estimation ponctuelle

   Problème : Soit X une v. a. r. qui suit une loi de probabilité Lθ dépendant du paramètre θ inconnu.
On cherche à utiliser l'information connue dans l'échantillon (X1 , · · · , Xn ) pour estimer θ.
Dénition.
1) Etant donné un échantillon (X1 , · · · , Xn ), on appelle statistique toute v. a. r. Tn de la forme Tn =
ϕ(X1 , · · · , Xn ) où ϕ est une fonction mesurable de Rn → R.
2) On appelle estimateur de θ, toute statistique Tn dont la valeur observée sur l'échantillon est utilisée pour
estimer θ.
Exemple Si le paramètre à estimer est la moyenne théorique de la loi de X c-a-d θ = E(X) alors l'estimateur
                                         n
                                      1X
naturel est Tn (X1 , · · · , Xn ) =         Xi = X n puisque E(X n ) = θ.
                                      n i=1

II.2     Biais d'un estimateur

Dénition.
1) Un estimateur Tn est dit sans biais ou non biaisé si :
                                                       E(Tn ) = θ.

2) Un estimateur Tn est dit asymptotiquement sans biais si :
                                                     lim E(Tn ) = θ.
                                                    n→+∞

Exemple
   ♣ X n est un estimateur sans biais de la moyenne de X.
                n
            1X               2
        2
   ♣ Sn =          Xi − X n est un estimateur asymptotiquement sans biais de la variance théorique de
            n i=1
                                                                n−1
X ; en eet si on pose θ = V (X) alors on sait que : E(Sn2 ) =        θ et donc lim E(Tn ) = θ. Par contre
                                                                  n              n→+∞
             n
 2       1 X                                                                                   2
Sn =            (Xi − X n )2 est un estimateur sans biais de la variance théorique puisque E(S n ) = θ.
      n − 1 i=1




                                                            2
~~~

## Page 3

~~~text
II.3      Convergence d'un estimateur

Dénition.
    Un estimateur Tn est convergent s'il tend en probabilité vers θ quand n → +∞ c-a-d :
                                                    ∀ ε > 0, P (| Tn − θ |< ε) −−−−−→ 1.
                                                                                    n→+∞
    ou encore
                                                    ∀ ε > 0, P (| Tn − θ |> ε) −−−−−→ 0.
                                                                                    n→+∞

Théorème. Tout estimateur sans biais dont la variance tend vers 0 quand n tend vers +∞ est convergent
c-a-d :                                         (
                                                      E(Tn ) = θ               P
                                                      V (Tn ) −−−−−→ 0 =⇒ Tn −
                                                                             −−−−→ θ
                                                                             n→+∞
                                                              n→+∞

Preuve L'inégalité de Bienaymé-Tchebychev donne :
                                                                          V (Tn )
                                                    P (| Tn − θ |> ε) ≤           −−−−−→ 0.
                                                                            ε2     n→+∞


II.4      Qualité d'un estimateur

   La qualité d'un estimateur se mesure à l'aide d'une distance au paramètre estimé. Pour obtenir un
indicateur numérique on retient Eh (Tn − θ)2 qu'on appelle risque
                                                               i quadratique, on a la relation suivante :
                                                            2
    EQ(Tn ) = E (Tn − θ)2 = E [(Tn − E(Tn )) + (E(Tn ) − θ)]
                                                                           2
            = E (Tn − E(Tn ))2 + 2(E(Tn ) − θ) E [Tn − E(Tn )] + (E(Tn ) − θ)
                                               |     {z      }
                                                                   E(Tn )−E(Tn )=0

                                                                                              2
                                               =⇒        EQ(Tn ) = V (Tn ) + (E(Tn ) − θ)
   Pour un estimateur sans biais l'erreur quadratique est égale à la variance.
   Pour deux estimateurs Tn et Tn′ sans biais, on dira que Tn est plus ecace que Tn′ si V (Tn ) ≤ V (Tn′ ). La
question se pose alors si on peut trouver un troisième estimateur qui serait meilleur que Tn et si oui, il faudrait
poursuivre la recherche ce qui nous conduit à essayer d'améliorer indéniment un estimateur. Existe-il un
meilleur estimateur ? Pour répondre à cette question on a besoin de l'inégalité de Fréchet-Darmois-Cramer-
Rao (FDCR) suivante :
Dénition.
    On appelle vraisemblance (Likelihood) de l'échantillon (X1 , · · · , Xn ) la loi de probabilité de ce n-uplet,
                                                                          n
notée L(x1 , · · · , xn ) et est dénie par L(x1 , · · · , xn ) =               P (Xi = xi|θ ) si X est une v. a. r. discréte et par
                                                                          Y

                                                                          i=1
                        n
                              f (xi , θ) si X est une v. a. r. continue de densité f (x, θ).
                        Y
L(x1 , · · · , xn ) =
                        i=1
    Le théorème suivant va préciser la borne inférieure pour la variance des estimateurs sans biais, sous cer-
taines hypothèses relatives à la loi de X et que nous appellerons hypothèses de Cramer-RAO (ces hypothèses
portent sur l'existence de dérivée de f densité de X et la possibilité d'intervertir les opérateurs de dérivation
et d'intégration).
Dénition.
    On appelle quantité d'information de Fisher :
                               "            2 #      2                         
                                    ∂ ln L               ∂ ln L(x1 , · · · , xn )
              In (θ) = E                            =E −                            expression plus facile à calculer
                                      ∂θ                        ∂θ2

                                                     ↑ si X(Ω) est indépendant de θ


                                                                      3
~~~

## Page 4

~~~text
Remarque                                                                                                             
                                                                                             ∂ ln L(x1 , · · · , xn )
   Si les v. a. r. sont indépendantes et de même loi on a In (θ) = n I1 (θ) si E                                        =0
                                                                                                     ∂θ
Preuve
   Sous les mêmes hypothèses et puisque :
                                                                        
                                                ∂ ln L(x1 , · · · , xn )
                                       E                                   = 0 alors :
                                                        ∂θ
                                       "            2 #           2                   
                                            ∂ ln L             ∂ ln L               ∂ ln L
                          In (θ) = E                   − E                 = var
                                              ∂θ                 ∂θ                    ∂θ
                                  "            n
                                                           !#       "      n
                                                                                            #
                                    ∂        Y                         ∂ X
                            = var       ln       f (xi , θ    = var           ln(f (xi , θ)
                                    ∂θ       i=1
                                                                      ∂θ i=1
                                   " n                      #   n                        
                                    X ∂                        X          ∂
                            = var             ln(f (xi , θ) =      var       ln(f (xi , θ)
                                     i=1
                                          ∂θ                   i=1
                                                                          ∂θ
                                                        
                                       ∂
                            = n var        ln(f (x1 , θ) = n I1 (θ)
                                       ∂θ
Théorème. Sous les hypothèses de Cramer-RAO, en particulier si X(Ω) est indépendant du paramètre à
estimer θ ; pour tout estimateur sans biais Tn de θ on a
                                                                      1
                                                       V (Tn ) ≥           .
                                                                    In (θ)
    Ce théorème donne une borne inférieure pour la variance d'un estimateur sans biais, qui peut ou non être
atteinte. Si cette borne est eectivement atteinte pour un estimateur, il sera alors le meilleur ou l'optimal.
Dénition.
   Un estimateur sans biais Tn est dit ecace si sa variance est égale à la borne de FDCR c-a-d
                                                                      1
                                                       V (Tn ) =           .
                                                                    In (θ)

III Méthode de construction d'un estimateur
   En l'absence d'un estimateur évident, on est amené à construire un estimateur, on dispose de deux
méthode : la méthode du maximum de vraissemblance et celle des moments.

III.1    Méthode du maximum de vraisemblance

Dénition. L'estimation de maximum de vraisemblance de θ est la valeur θ̂n de θ qui rend maximale la
fonction de vraisemblance L(x1 , · · · , xn , θ). L'estimateur du maximum de vraisemblance (evm) de θ est la v.
a. r. correspondante.
Remarque
   θ̂n est le maximum de la fonction L(x1 , · · · , xn , θ) donc θ̂n est solution de :
                                                     
                                                          ∂L
                                                      ∂θ = 0
                                                     
                                                     
                                                     
                                                (I)
                                                           2
                                                      ∂ L <0
                                                     
                                                     
                                                     
                                                          ∂θ2

                                                                4
~~~

## Page 5

~~~text
    mais comme la fonction de vraisemblance L(x1 , · · · , xn , θ) se calcule à partir d'un produit on remplace
le problème (I) par un problème équivalent pour la log-vraisemblance c-a-d θ̂n est solution de :
                                                      
                                                        ∂ ln L
                                                       ∂θ = 0
                                                      
                                                      
                                                      
                                               (II)
                                                         2
                                                       ∂ ln L < 0
                                                      
                                                      
                                                      
                                                         ∂θ2
Exemple
                                                                          1
   Considérons X une v. a. r. de loi exponentielle de paramètre             où θ > 0, de densité dénie pour x > 0
                                                                          θ
                   1 −x
par : f (x, θ) =     e θ
                   θ
                                                                n                     n
                                                                               1 − 1X
   La fonction de vraissemblance est L(x1 , · · · , xn , θ) =
                                                                Y
                                                                    f (xi , θ) = e        xi
                                                               i=1
                                                                              θn θ i=1
                                                   n                              n
                                                1X          ∂ ln L    −n     1 X
   d'où ln L(x1 , · · · , xn , θ) = −n ln(θ) −        xi et        =       + 2       xi
                                                θ i=1         ∂θ       θ    θ i=1
                                        n                                                 n
         ∂ ln L                      1X                            ∂ 2 ln L     n      2 X         n
   ainsi         = 0 ⇐⇒ θ =                xi = xn ; d'autre part        2
                                                                            =    2
                                                                                    −   3
                                                                                             xi = 3 (θ − 2xn ). Pour
           ∂θ                        n i=1                           ∂θ        θ      θ i=1       θ
              2                                                                                n
               ∂ ln L                −n                                                       1
θ = xn on a                 (xn ) = 2 < 0 d'où θ̂n = xn et par conséquent Tn = X n =
                                                                                                X
                                                                                                    Xi
                 ∂θ2                  xn                                                      n i=1

III.2     Méthode des moments

   Dans le cas où le paramètre à estimer θ est la moyenne théorique de la r. a. r. X , l'estimateur naturel est
                                                n
                                        1X
la moyenne empirique c-a-d Tn = X n =         Xi ; de même pour estimer la variance θ = V (X), on prend
                                        n i=1
                                                   n
                                                1X
comme estimateur la variance empirique Sn =
                                          2
                                                      (Xi − X n )2 . Ce principe se généralise aux moments
                                                n i=1
                                         n
                                      1X
d'ordre supérieur en considérant Tn =       (Xi − X n )k pour k ≥ 3.
                                      n i=1


IV Intervalles de conance
    Jusqu'à présent on a estimé un paramètre θ par une unique valeur θ̂n (estimation ponctuelle). Si l'esti-
mateur θ̂n possède de bonnes propriétés (sans biais, de variance minimale, ecace) on peut s'attendre à ce
que θ̂n soit proche de la vraie valeur valeur de θ. Cependant il est peu probable que ce soit le cas. Il est plus
raisonnable de proposer un ensemble de valeurs vraissemblables pour θ plutôt que de l'estimer par une seule
valeur. Fournir un intervalle I tq. θ ∈ I s'appelle donner une estimation par intervalle de θ ou estimation
ensembliste.
Dénition. Un intervalle de conance de seuil (ou de niveau se signication) α ∈ [0, 1] pour un paramètre
θ, est un intervalle aléatoire I tq. P (θ ∈ I) = 1 − α.
Remarque
   ✠ α est la probabilité que θ n'appartienne pas à I c-a-d c'est la probabilité de se tromper en armant
que θ ∈ I.
   ✠ 1 − α est le niveau de conance que θ appartienne à I.



                                                          5
~~~

## Page 6

~~~text
    Le problème à régler est de trouver un procédé pour déterminer un intervalle de conance pour un para-
mètre θ. On choisira dans la plupart des cas un intervalle de conance centré sur un estimateur performant
θ̂n c-a-d de la forme I = [ θ̂n − ε, θ̂n + ε ] ; il reste à trouver ε tq. P (θ ∈ I) = P (θ̂n − ε ≤ θ ≤ θ̂n + ε) = 1 − α.

IV.1      Intervalles associés aux paramètres de la loi normale

IV.1.1 Intervalle pour la moyenne d'une loi normale avec variance connue
                                                                                                              n
                                                                                                    1X
   Si X1 , · · · , Xn sont des v. a. r. indépendantes et de même loi N (m, σ 2 ), on sait que X n =       Xi est
                                                                                                    n i=1
un estimateur sans biais, de variance minimale de m. Cherchons un intervalle de conance pour m sous la
forme [ X n − ε, X n + ε ] le problème revient, pour  α√xé, à chercher ε tq. P√    − ε ≤ m ≤ X n + ε) = 1 − α
                                                                                (X n 
                                                         n ε √ Xn − m             nε
c-a-d P (−ε ≤ X n − m ≤ ε) = 1 − α ou bien P −               ≤ n             ≤         =1−α
                                                         σ             σ         σ
             √ X −m
on sait que n n              −−−−−→ N (0, 1). Si ϕ est la fonction de répartition de la loi N (0, 1) alors ε est
                                loi
                     σ        n→+∞
                             √            √ 
                                 n               n
solution de : 1 − α = ϕ             ε −ϕ −         ε
                               σ√             σ
                                      n
                            = 2ϕ        ε −1
           √                       σ   √
               n             α             n             α
    d'où ϕ        ε =1−            =⇒        ε = ϕ−1 1 −
              σ              2           σ                2
                            α               α                                            α
Si on pose uα = ϕ−1 1 −           ⇐⇒ 1 − = ϕ(uα ), uα s'appelle le fractile d'ordre 1 − de la loi N (0, 1).
      √                      2                2                                             2
        n                      σ
alors     ε = uα =⇒ ε = √ uα et par conséquent l'intervalle de conance pour m de niveau de conance
       σ                       n                
                           σ               σ
1 − α est : I = X n − √ uα , X n + √ uα
                            n               n

IV.1.2 Intervalle pour la moyenne d'une loi normale avec variance inconnue
   La statistique utilisée dans la situation précédente n'est utilisable que si on connait la valeur de σ; or,
dans la pratique on ne connait pas la valeur de σ et va donc devoir être remplacé par un estimateur sans
                                                     n
                                         2      1 X
biais de la variance théorique σ 2 : S n =              (Xi − X n )2 . On utilise donc comme nouvelle statistique
                                              n − 1 i=1
√ Xn − m
   n           qui suit une loi de Student à n − 1 degrés de liberté.
        Sn                                                    √                         √ 
                                                                   n ε √ Xn − m            nε
de P (X n − ε ≤ m ≤ X n + ε) = 1 − α on en déduit que P −             ≤ n             ≤          =1−α
                                                                  Sn           Sn         Sn
si on√appelle
            F la fonction   √ de répartition  de la loi Student St(n − 1) à n − 1 degrés de liberté on aura
        nε          α          nε      −1
                                              α
F           =1−         =⇒         =F       1−     (∗)
       Sn           2       Sn α              2
                                                              α                                        α
Si on pose tn−1,α = F −1 1 −          c-a-d F (tn−1,α ) = 1 − , tn−1,α est donc le fractile d'ordre 1 − de la
                                 2                            2                                        2
                                                                      Sn
loi de Student à n − 1 degrés de liberté ; on deduit de (∗) que ε = √ tn−1,α ; d'où l'intervalle de conance
                                                                      n              
                                                            Sn              Sn
pour m de niveau de conance 1 − α vaut : I = X n − √ tn−1,α , X n + √ tn−1,α
                                                             n                n




                                                           6
~~~

## Page 7

~~~text
IV.1.3 Intervalle pour la variance d'une loi normale avec espérance connue
                 n
              1X                                                       nσ̂n
      σ̂n =         (Xi − m)2 est le meilleur estimateur de σ 2 de plus 2 suit la loi du χ2n . On a donc (la loi
              n i=1                                                     σ
du χ2n n'est pas symétrique) ∀ a, b ∈ R tq. 0 < a < b
                                                     
                              nσ̂n       nσ̂n   2  nσ̂n
                          P a≤ 2 ≤b =P        ≤σ ≤        = Fχ2n (b) − Fχ2n (a)
                               σ          b         a

                                                                     α α
                                                1−α=1−                 −
                                                                     2   2
Il y a une innité de façons de choisir a et b. La façon la plus usuelle de procéder est "d'équilibrer les risques"
c-a-d de prendre a et b tq. Fχ2n (b) = 1 − α2 et Fχ2n (a) = α2
si on obtient b = χ2n,1− α2 et a = χ2n, α2 alors l'intervalle de conance pour σ 2 de niveau de conance 1 − α est :
                                                    "                             #
                                                        nσ̂n
                                                           nσ̂n
                                               I=  2     , 2
                                                  χn,1− α χn, α
                                                                 2            2



IV.1.4 Intervalle pour la variance d'une loi normale avec espérance inconnue
      Lorsque l'espérance m de la loi normale est inconnue, l'estimateur sans biais et convergent de σ 2 est :
               n                                2
 2        1 X                                 S
Sn =              (Xi − X n )2 de plus (n − 1) n2 suit la loi du χ2n−1 . De même on cherche les valeurs de a et b
        n − 1 i=1                             σ
tq.
                                                                 2
                                                                             !
                                                         S
                                         P    a ≤ (n − 1) n2 ≤ b                  =1−α
                                                         σ
ce qui conduit à :
                                          2                          2
                                                                         !
                                        S                 S
                             P   (n − 1) n ≤ σ 2 ≤ (n − 1) n                 = Fχ2n−1 (b) − Fχ2n−1 (a)
                                         b                 a
                                                                                                  α α
                                                                         =1−α=1−                    −
                                                                                                  2   2
usuellement on choisit b = χ2n−1,1− α2 et a = χ2n−1, α2 alors l'intervalle de conance pour σ 2 de niveau de
conance 1 − α est :
                                                         2                                2
                                      "                                    #
                                                        Sn                              Sn
                                      I = (n − 1)                    , (n − 1)
                                                    χ2n−1,1− α                        χ2n−1, α
                                                                 2                            2




                                                             7
~~~
