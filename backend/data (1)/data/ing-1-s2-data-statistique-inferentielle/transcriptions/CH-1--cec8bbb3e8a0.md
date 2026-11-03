# CH-1.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1L8CO5qLc2DjJTxfH019UDJq337MrFnxP) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Les convergences
I Dénition - Rappel
   On appelle variable aléatoire réelle ( et on note ) v. a. r. une application X mesurable de
   c-a-d :
                           ∀ B ∈ β(R) , X −1 (B) = {ω ∈ Ω tq X(ω) ∈ B} ∈ A.


II Convergences
II.1    Convergence presque sérement : c.p.s.

Dénition. Soit (Xn )n∈N une suite de v. a. r. et X une v. a. r. On dit que la suite (Xn )n∈N converge
presque sérement ( ou presque partout ) vers X quand n → +∞ s'il existe un événement A négligeable tq.
                                ∀w∈
                                  / A,         on ait : lim Xn (ω) = X(ω).
                                                          n→+∞

soit encore :                                                         
                               ∀w∈
                                 / A,         P       lim Xn (ω) = X(ω) = 1.
                                                      n→+∞

Propriété. Soit (Xn )n∈N une suite de v. a. r. et X une v. a. r. Si :
                                               X
                                  ∀ ε > 0,            P (| Xn − X |> ε) < +∞
                                              n∈N

alors la suite (Xn )n∈N c.p.s. vers X quand n → +∞.

II.2    Convergence en moyenne, convergence en moyenne quadratique : c.m.,
        c.m.q.

Dénition.
1) La suite (Xn )n∈N de v. a. r. converge vers la v. a. r. X en moyenne ( ou dans L1 ) quand n → +∞ ssi :
                                             lim E(| Xn − X |) = 0
                                         n→+∞

2) La suite (Xn )n∈N de v. a. r. converge vers la v. a. r. X en moyenne quadratique( ou dans L2 ) quand
n → +∞ ssi :
                                             lim E(| Xn − X |2 ) = 0
                                         n→+∞

Théorème. La c.m.q. d'une suite de de v. a. r. entraîne la c.m. de cette suite.



                                                          1
~~~

## Page 2

~~~text
     La preuve de ce théorème utilise l'inégalité de Cauchy-Schwartz suivante :
Inégalité de Cauchy-Schwartz
     Soient X, Y deux v. a. r. admettant des variances, on a alors :
                                                        p          p
                                           E(XY ) ≤         E(X 2 ) E(Y 2 )

Preuve de l'inégalité de Cauchy-Schwartz
     Soit t ∈ R, on pose f (t) = E[(X + tY )2 ] alors
                                      f (t) = E(Y 2 )t2 + 2E(XY )t + E(X 2 )

   donc f (t) est un polynôme de degré deux en t qui est toujours positif, son discriminant réduit doit être
négatif ou nul d'où
                                                        p          p
                                           E(XY ) ≤         E(X 2 ) E(Y 2 )
Preuve du théorème
                                                                    p                  p
                        E(| Xn − X |) = E (| Xn − X | ·1) ≤             E(| Xn − X |2 ) E(12 )
or                                                       Z
                                      E(12 ) = E(1) =           1.dP = P (Ω) = 1
                                                            Ω
donc                                                                   1
                                    0 ≤ E(| Xn − X |) ≤ E(| Xn − X |2 ) 2
                                                       

par conséquent si E(| Xn − X |2 ) −−−−−→ 0 alors E(| Xn − X |) −−−−−→ 0.
                                     n→+∞                                  n→+∞


II.3     Convergence en probabilité : c.p.

Dénition.
La suite (Xn )n∈N de v. a. r. converge vers la v. a. r. X en probabilité quand n → +∞ ssi :
                                      ∀ε>0      lim P (| Xn − X |> ε) = 0.
                                               n→+∞

                               ou encore ∀ ε > 0 lim P (| Xn − X |< ε) = 1.
                                                        n→+∞

Théorème. La c.m ou la c.p.s. d'une suite de de v. a. r. entraîne la c.p. de cette suite.
     ♠ Pour montrer que la c.m. entraîne la c.p. on a besoin de l'inégalité de Markov suivante :
Inégalité Markov
     Si X est une v.a.r. positive, on a pour tout réel a strictement positif
                                                                 1
                                               P (X ≥ a) ≤         E(X).
                                                                 a
Preuve de l'inégalité de Markov : voire TD.
Preuve du théorème
                                           1
   D'où ∀ ε > 0, P (| Xn − X |> ε) ≤ E(| Xn − X |)
                                     ε
   donc la c.m. entraîne la c.p.
   ♠ Pour montrer que la c.p.s. entraîne la c.p. on utilise le théorème de la convergence dominée ( voir
cours mesure et intégration )
Théorème de la convergence dominée
     Etant donnée une suite de fonctions (fn )n∈N , et une fonction g positive tq. :

                                                            2
~~~

## Page 3

~~~text
        ♣∀
         Z n ≥ 0 | fn |≤ g          m.p.p.
        ♣    g dm < +∞
                     Z         Z
   alors on a : lim    fn dm =               lim fn dm
                n→+∞                         n→+∞
   D'où si (Xn )n∈N qui c.p.s. vers X alors on considère la suite de fonctions (1|Xn −X|>ε )n≥0 c.p.s. vers la
fonction nulle et est dominée par 1.
   Comme P (| Xn − X |> ε) = E(1|Xn −X|>ε ) alors
     lim P (| Xn − X |> ε) = lim E(1|Xn −X|>ε )
   n→+∞                             n→+∞
                                = E( lim 1|Xn −X|>ε )
                                       n→+∞
                           = E(0) = 0.
   donc (Xn )n∈N c.p. vers X cqfd.
   Nous pouvons résumer les implications entre ces diérentes notions de convergence dans le schema sui-
vant :
                                        Convergence L2
                                                          ⇓
                                                Convergence L1
                                                          ⇓
        Convergence p.s.        ⇒       Convergence en probabilité
                                                          ⇓
                                                Convergence en loi

III Loi des grands nombres
III.1    Loi faible des grands nombres

Dénition. Soit (Xn )n∈N une suite de v. a. r. indépendantes ayant même espérance, même variance et de
                            ∗
                                                                      n
                                                                   1X
carré intégrable. La suite des moyennes arithmétiques                    Xi converge dans L2 vers E(X1 ) c-a-d
                                                                   n i=1
                                                           n
                                                                              !
                                                        1X
                                         lim E      |         Xi − E(X1 ) |2    = 0.
                                        n→+∞            n i=1

Preuve              n
                 1X                                        1
   Posons Yn =         Xi  =⇒ E(Yn ) = E(X1 ) et var(Yn ) = var(X1 ).
                 n i=1                                     n
   comme E (Yn − E(Yn )) != var(Yn ) alors !
                          2
                            
          n                            n
       1X                           1X           1
   E |       Xi − E(X1 ) |2 = var         Xi = var(X1 )
       n i=1                        n i=1        n
   d'où la convergence dans L2 .
Remarque
    ✠ Comme la convergence dans L2 entraîne la convergence dans L1 et la convergence en probabilité ; la
         n
      1X
suite       Xi converge en probabilité vers E(X1 ). Ce résultat est très important en statistique, puisqu'il
      n i=1
                                      n
                                  1X
assure que la moyenne empirique         Xi des v. a. r. Xi indépendantes, ayant même variance et même
                                 n i=1
espérance est un estimateur convergent de l'espérance.
   ✠ La loi faible des grands nombres est obtenue sous la condition que les v. a. r. Xi aient même moments
d'ordre 1 et 2, mais pas forcément même loi. Il existe une loi forte des grands nombres relative à une

                                                               3
~~~

## Page 4

~~~text
convergence plus forte qui s'obtient sous la seule condition d'existence du moment d'ordre 1 mais en renforéant
par ailleurs les hypothèses en supposant que les v. a. r. Xi ont la même loi de probabilité.

III.2     Loi forte des grands nombres

Dénition. Soit (Xn )n∈N une suite de v. a. r. indépendantes, de même loi et intégrables. On a alors
                            ∗
 n
1X
        Xi converge presque sûrement vers E(X1 ) c-a-d
n i=1

                                                        n
                                                   1X
                                               lim       Xi = E(X1 ).
                                              n→+∞ n
                                                     i=1


IV Convergence en loi et théorème central limite
IV.1      Convergence en loi

Dénition. Une suite de v. a. r. (Xn )n∈N converge en loi vers une v. a. r. X si pour toute fonction continue
bornée φ : R −→ R on a :
                                              lim E (φ(Xn )) = E (φ(X)) .
                                          n→+∞

Remarque
    Cette dénition n'est pas très "utile" dans la pratique c'est pourquoi on a une autre dénition équivalente
à l'aide des fonctions de répartition.
Dénition. Soit F1 , · · · , Fn la suite des fonctions de répartition des v. a. r. X1 , · · · , Xn et F celle de X.
La suite de v. a. r. (Xn )n∈N∗ converge en loi vers la v. a. r. X si :
                                lim Fn (x) = F (x)    pour tout réel x où F est dénie.
                            n→+∞

Remarque
   ✠ La convergence en loi est la forme la plus faible ; au sens où, en général, elle n'implique pas les autres
formes de convergence.
   ✠ Soient (Xn )n∈N une suite de v. a. r. et X une autre v. a. r., toutes à valeurs dans Z. La suite (Xn )n∈N
converge en loi vers X ssi :
                                     ∀ k ∈ Z,     lim P (Xn = k) = P (X = k)
                                                n→+∞

   ✠ Soient (Xn )n∈N une suite de v. a. r. et X une autre v. a. r. admettant une densité de probabité fX .
Alors la suite (Xn )n∈N converge en loi vers X ssi :
                                                                                      Z b
               ∀ a, b ∈ R, avec a < b,     lim P (a ≤ Xn ≤ b) = P (a ≤ X ≤ b) =               fX (x) dx.
                                         n→+∞                                             a

Théorème. Si la suite (Xn )n∈N de v. a. r. converge en probabilité vers la v. a. r. X , alors elle converge en
loi vers X.
Preuve
   Soit (Xn )n∈N une suite de v. a. r. qui converge en probabilité vers la v. a. r. X. Si φ est une fonction
continue bornée sur un segment alors elle y est uniformément continue d'où :
                         ∀ ε > 0, ∃ η > 0 tq. | x − y | ≤ η =⇒| φ(x) − φ(y) |≤ ε
                                     Z
   d'où | E (φ(Xn )) − E (φ(X)) |= | [φ(Xn ) − φ(X)] dp |
                                          Ω


                                                            4
~~~

## Page 5

~~~text
                                       Z
                                   ≤        | [φ(Xn ) − φ(X)] | dp
                                        Ω
                              Z                 q                       Z
                                                | [φ(Xn ) − φ(X)] | dp +              | [φ(Xn ) − φ(X)] | dp
                                 {|Xn −X|≤η}
                                       Z            Z                     {|Xn −X|>η}

                                   ≤        ε dp +             2 sup | φ(y) | dp
                                        Ω           {|Xn −X|>η}   y∈R
                                ≤ ε + 2 ∥ φ ∥∞ P (| Xn − X |> η)
   =⇒ ∀ ε > 0,    lim | E (φ(Xn )) − E (φ(X)) |≤ ε
                 n→+∞
   =⇒ lim E (φ(Xn )) = E (φ(X))
        n→+∞


IV.2     Convergence vers la loi de Gauss : théorème central limite

Théorème. Soit (Xn )n∈N une suite de v. a. r. indépendantes et de même loi admettant des moments d'ordres
                                       √ Xn − µ
1 et 2 notés µ et V = σ 2 ̸= 0 alors            −−−−−→ X v. a. r. de loi N (0, 1).
                                                  loi
                                        n
                                           σ     n→+∞

Remarque                                        Z b
                                √ Xn − µ
                             
                                                           1   t2
   1) Si a, b ∈ R, lim P a ≤ n              ≤b =         √ e− 2 dt
                   n→+∞                σ              a    2π
                   √ Xn − µ
   2) L'expression n         peut s'écrire d'une autre façon :
                        σ
                         n
                                                   Sn
   souvent on pose Sn =     Xi de sorte que X n =      et donc
                        X

                        i=1
                                                   n
                                              √ 
                                   √ Xn − µ
                                                      
                                               n Sn      Sn − nµ
                                    n       =       −µ =    √
                                       σ      σ   n       σ n




                                                          5
~~~
