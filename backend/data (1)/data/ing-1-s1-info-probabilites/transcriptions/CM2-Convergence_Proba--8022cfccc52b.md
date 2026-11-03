# CM2-Convergence_Proba.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1QrmT2DiJV6wcaAO5AhZ3gEUuvslaKqwl) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                      Suites de variables aléatoires réelles
                                  Convergence
                                        Khalid El Amine I.
                                       Department of Mathematics

                                                 ⋆⋆⋆


Dans tout ce chapitre :

    • Ω est un ensemble non vide.

    • (Ω, A) est un espace probabilisable.

    • (Ω, A, P ) est un espace probabilisé.

    • R sera toujours muni de la tribu de Borel, B(R).

    • Toutes les variables aléatoires sont définies sur un espace probabilisé (Ω, A, P )
      et à valeurs dans l’espace probabilisable (R, B(R)).


1     Inégalités de Markov et Chebyshev
Les inégalités de cette section fournissent des majorations sur la probabilité qu’une variable aléatoire
prenne une valeur «extrême» dans la queue droite et/ou gauche d’une distribution.

Théorème 1.1 (Inégalité de Markov)
Soit X une v.a.r.. Si X admet une espérance, alors :

                                                                 E(|X|)
                                  ∀a ∈ R+∗ ,     P (|X| > a) ≤
                                                                   a

Preuve. bigbreak

Théorème 1.2 (Inégalité de Markov)
Soit X une v.a.r.. Si X admet un moment d’ordre m ∈ N∗ alors :
                                                                 E(|X|m )
                                 ∀a ∈ R+∗ ,     P (|X| > a) ≤
                                                                   am

Preuve.


Théorème 1.3 (Inégalité de Chebyshev)
Soit X une v.a.r.. Si X admet une variance, alors :

                                                                     V (X)
                               ∀a ∈ R+∗ ,     P (|X − E(X)| > a) ≤
                                                                       a2

Preuve.



                                                    1
~~~

## Page 2

~~~text
2                                                                                Variables aléatoires réelles


2     Convergence en loi
Définition 2.1 (Convergence en loi)
Soit (Xn )n∈N∗ une suite de v.a.rs et (FXn )n∈N∗ la suite des fonctions de répartition associées.
Soit X une v.a.r. et FX sa fonction de répartition.
On dit que (Xn )n∈N∗ converge en loi vers X, si et seulement si, (FXn )n∈N∗ converge simplement vers
FX en tout point de continuité de FX .
Notation :
                                                    L
                                              Xn −−−→ X

Remarque. Notons C(FX ) = {x ∈ R : FX est continue en x}. Alors
                       L
                 Xn −−−→ X       ⇐⇒ FXn (x) −−−−−→ FX (x) , ∀x ∈ C(FX )
                                                 n→+∞

                                 ⇐⇒ P (Xn ≤ x) −−−−−→ P (X ≤ x) , ∀x ∈ C(FX )
                                                    n→+∞


Exemple. Soit (Xn )n≥1 une suite de v.a.r. discrètes tel que ∀n ∈ N∗ ,

                                             Xn (Ω) = {0, 1}

et de fonction de masse de probabilité
                                             
                                             1/n
                                                           si x = 0
                                    pXn (x) = 1 − 1/n       si x = 1
                                                            si non
                                             
                                               0
                                             

i.e
                                          1                1
                                    pXn =   · I{0} + (1 − ) · I{1}
                                         n                 n
Montrer que la suite (Xn )n≥1 converge en loi vers la v.a.r. constante égale à 1.

Solution.


Théorème 2.2 Soit g : R −→ R une fonction continue.
Si une suite de v.a.rs (Xn )n∈N∗ converge en loi vers une v.a.r. X, alors la suite de v.a.r. (g(Xn ))n∈N∗
converge en loi vers la v.a.r. g(X).

Preuve.


3     Convergence en probabilité
Définition 3.1 (Convergence en probabilité)
Soit (Xn )n∈N∗ une suite de v.a.rs et X une v.a.r.. On dit que (Xn )n∈N∗ converge en probabilité vers
X, si et seulement si,
                              ∀ϵ ∈ R+∗ ,   P (|Xn − X| > ϵ) −−−−−→ 0
                                                                n→+∞

Notation :
                                                    P
                                              Xn −−−→ X

Remarque.
                   P (|Xn − X| > ϵ) −−−−−→ 0      ⇐⇒     P (|Xn − X| ≤ ϵ) −−−−−→ 1
                                      n→+∞                                  n→+∞

Notons que (P (|Xn − X| > ϵ))n∈N∗ est une suite de nombre réels.
~~~

## Page 3

~~~text
Convergence                                                                                          3


Exemple. Suite de v.a.rs discrètes
Soit X une v.a.r. discrète avec X(Ω) = {0, 1} et f.m.p. pX définie par :
                                              
                                              2/3 si x = 0
                                              
                                     pX (x) = 1/3 si x = 1
                                                       sinon
                                              
                                                 0
                                              

Soit (Xn )n∈N∗ une suite de v.a.rs discrètes de terme général
                                                        
                                                       1
                                           Xn = 1 +        X
                                                       n
                   P
Montrer que Xn −−−→ X.

Solution.


Exemple. Suite de v.a.rs absolument continues
Soit (Xn )n∈N∗ une suite de v.a.rs absolument continues. Supposons que pour tout n ∈ N∗ , Xn suit une
distribution exponentielle de paramètre n, i.e. Xn ∼ E(n). Montrer que Xn converge en probabilité
vers 0.

Solution.


Théorème 3.2 Soit g : R −→ R une fonction continue.
Si une suite de v.a.rs (Xn )n∈N∗ converge en probabilité vers une v.a.r. X, alors la suite de v.a.rs
(g(Xn ))n∈N∗ converge en probabilité vers la v.a.r. g(X).

Preuve.


Proposition 3.3 Si (Xn )n∈N∗ converge en probabilité vers X, alors elle converge en loi vers X.

Preuve.



4     Convergence en moyenne
4.1    Espace Lr
Définition 4.1 (Lr space)
Soit r ∈ [1, +∞[ et X une v.a.r..
• On dit que X est r-intégrable, si et seulement si, E(|X|r ) < ∞.
• On appelle espace Lr , l’ensemble des v.a.rs r-intégrable, i.e

                                    Lr = {X : Ω → R ; E(|X|r ) < ∞}

En particulier, si X est une v.a.r., alors

• On dit que X est intégrable, et on note X ∈ L1 , si X admet un moment d’ordre 1. i.e. :

                                      X ∈ L1 ⇐⇒ E(|X|) < +∞

• On dit que X est de carré intégrable, et on note X ∈ L2 , si X admet un moment d’ordre 2. i.e. :

                                     X ∈ L2 ⇐⇒ E(|X|2 ) < +∞
~~~

## Page 4

~~~text
4                                                                               Variables aléatoires réelles


4.2    Convergence en moyenne et en moyenne quadratique
Définition 4.2 (Convergence en moyenne)
Soit (Xn )n∈N∗ une suite de v.a.rs intégrables et X une v.a.r. intégrable.
On dit que (Xn )n∈N∗ converge en moyenne (ou converge dans L1 ) vers X, si et seulement si,

                                        E(|Xn − X|) −−−−−→ 0
                                                        n→+∞

Notation :
                                                   L1
                                             Xn −−−→ X

Remarque. Notons que pour la convergence en moyenne, il est nécessaire que E(|Xn − X|) < +∞,
ce qui est généralement assuré en exigeant que Xn et X soient intégrables.

Définition 4.3 (Convergence en moyenne quadratique)
Soit (Xn )n∈N∗ une suite de v.a.rs de carré intégrable et X une v.a.r. de carré intégrable.
On dit que (Xn )n∈N∗ converge en moyenne quadratique (ou converge dans L2 ) vers X, si et seulement
si,
                                     E(|Xn − X|2 ) −−−−−→ 0
                                                        n→+∞

Notation :
                                                   L2
                                             Xn −−−→ X

Remarque. Notons que pour la convergence en moyenne quadratique, il est nécessaire que E(|Xn −
X|2 ) < +∞, ce qui est généralement assuré en exigeant que Xn et X soient de carré intégrable.

Exemple 1. Soit (Xn )n≥1 une suite de v.a.rs discrètes telle que pour tout n ∈ N∗

                                           Xn (Ω) = {0, n}

et f.m.p.
                                                   1
                                              
                                              
                                               1− 3       si x = 0
                                              
                                                  n
                                    pXn (x) =    1
                                                           si x = n
                                               n3
                                              
                                                           sinon
                                              
                                              0

Montrer que (Xn )n≥1 convergence en moyenne quadratique et en moyenne vers la v.a.r. X = 0.

Solution.



Exemple 2. Soit (Xn )n≥1 une suite de v.a.rs discrètes telle que pour tout n ∈ N∗

                                           Xn (Ω) = {0, n}

et f.m.p.
                                                   1
                                             
                                             
                                              1− 2       if x = 0
                                             
                                                  n
                                   pXn (x) =    1
                                                 2
                                                          if x = n
                                             
                                              n
                                                          otherwise
                                             
                                             0

La suite (Xn )n≥1 converge-elle en moyenne quadratique vers la v.a.r. X = 0 ? et en moyenne ?

Solution.
~~~

## Page 5

~~~text
Convergence                                                                                                  5


Théorème 4.4 Soit g : R −→ R une fonction continue.
soit (Xn )n∈N∗ une suite de v.a.rs et X une v.a.r..
• Si (Xn )n∈N∗ converge en moyenne quadratique vers X, alors la suite de v.a.rs (g(Xn ))n∈N∗ converge
en moyenne quadratique vers g(X).
• Si (Xn )n∈N∗ converge en moyenne vers X, alors la suite de v.a.rs (g(Xn ))n∈N∗ converge en moyenne
vers g(X).

Preuve.


Proposition 4.5 Soit (Xn )n∈N∗ une suite de v.a.rs et X une v.a.r.
• Si (Xn )n∈N∗ converge en moyenne quadratique vers X, alors elle converge en moyenne vers X.
• Si (Xn )n∈N∗ converge en moyenne vers X, alors elle converge en probabilité vers X.

Preuve.


4.3    Convergence en moyenne d’ordre r
Définition 4.6 (Convergence en moyenne d’ordre r)
Soit r ∈ [1, +∞[. Soit (Xn )n∈N∗ une suite de v.a.rs et X une v.a.r. telles que E(|Xn |r ) < ∞ et
E(|X|r ) < ∞.
On dit que (Xn )n∈N∗ converge en moyenne d’ordre r (ou converge dans Lr ) vers X, si et seulement
si,
                                    E(|Xn − X|r ) −−−−−→ 0
                                                       n→+∞
Notation :
                                                  Lr
                                              Xn −−−→ X

Exemple 1. Soit (Xn )n≥1 une suite de v.a.rs discrètes telle que pour tout n ∈ N∗
                                        Xn (Ω) = {−1, 0, 1}
et f.m.p.
                                                1
                                             
                                             
                                                       si x = −1
                                             
                                              2n
                                             1 − 1
                                             
                                                        si x = 0
                                             
                                   pXn (x) =      n
                                                1
                                                        si x = 1
                                             
                                             
                                             
                                              2n
                                             
                                             
                                                        sinon
                                             
                                               0
                                             Lr
Montrer que, pour tout r ∈ [1, +∞[, Xn −−−→ 0.

Solution.

                                                                                                  
                                                                                                1
Exemple 2. Soit (Xn )n≥1 une suite de v.a.rs absolument continues telle que Xn ∼ U           0,          .
                                                                                                n
                      r
                  L
Montrer que Xn −−−→ 0 pour tout r ∈ [1, +∞[.

Solution.


Théorème 4.7 Soit (Xn )n∈N∗ une suite de v.a.rs et X une v.a.r.. Alors pour tout s > r ≥ 1
                                        Ls                 Lr
                                  Xn −−−→ X =⇒ Xn −−−→ X

Preuve.
~~~

## Page 6

~~~text
6                                                                                     Variables aléatoires réelles


5     Convergence presque sûre
Définition 5.1 (Convergence presque sûre)
Soit (Xn )n∈N∗ une suite de v.a.rs et X une v.a.r.. On dit que (Xn )n∈N∗ converge presque sûrement
vers X, si et seulement si,
                                              
                                              (1) P (M ) = 1
              existe un événement M tel que :
                                              (2) ∀ω ∈ M, Xn (ω) −−−−−→ X(ω)
                                                                                n→+∞

Notation :
                                                       p.s.
                                                 Xn −−−−→ X

Remarque. On dit aussi que (Xn ) converge vers X avec probabilité 1.
          p.s.
    Xn −−−−→ X ⇐⇒ P ({ω ∈ Ω : Xn (ω) −−−−−→ X(ω)}) = 1
                                      n→+∞
                                                  
                                                  (1) P (N ) = 0
               ⇐⇒ existe un événement N tel que :
                                                  (2) ∀ω ∈ N c , Xn (ω) −−−−−→ X(ω)
                                                                                          n→+∞




• La convergence presque sûre est la version probabilistique de la convergence simple des suites de
fonctions en analyse réelle.

Exemple. On travaille dans l’espace probabilisé (R, B(R), P ) où P est la probabilité uniforme sur le
segment [0, 1], i.e :           Z                Z
                            P (B) =       I[0,1] (x)dx =             dx , ∀B ∈ B(R)
                                      B                    B∩[0,1]

Soit (Xn )n≥1 une suite de v.a.r. sur (R, B(R)).
1. Si Xn = I]0, n1 ] . Montrer que (Xn )n≥1 converge simplement sur R vers la variable certaine X = 0.
2. Si Xn = I[0, n1 ] . Montrer que (Xn )n≥1 converge presque sûrement vers la variable certaine X = 0.

Solution.


Théorème 5.2 Soit g : R −→ R une fonction continue.
Si une suite de v.a.rs (Xn )n∈N∗ converge presque sûrement vers une v.a.r. X, alors la suite de v.a.rs
(g(Xn ))n∈N∗ converge presque sûrement vers la v.a.r. g(X).

Preuve.


Proposition 5.3 Si (Xn )n∈N∗ converge presque sûrement vers X, alors elle converge en probabilité
vers X.

Preuve.


Theorem 5.1 Soit (Xn )n∈N∗ une suite de v.a.rs.
si la suite converge

    • presque sûrement ;
    • ou en probabilité ;
    • ou en moyenne d’ordre r ;
~~~

## Page 7

~~~text
Convergence                                                                                              7


    • ou en loi ;

alors, la variable aléatoire limite est unique.

Preuve.



                                   Diagramme des convergences

Le diagramme ci-dessous récapitule les liens entre les divers modes de convergence.


                                 Convergence L2


                                 Convergence L1


 Convergence p.s.          Convergence en probabilité           Convergence en loi



                                    Composition et convergences

Soit g : R −→ R une fonction continue. Alors :
                L                      L                        P                      P
        • Xn −−−→ X =⇒ g(Xn ) −−−→ g(X)                 • Xn −−−→ X =⇒ g(Xn ) −−−→ g(X)

                L1                      L1                      L2                      L2
        • Xn −−−→ X =⇒ g(Xn ) −−−→ g(X)                 • Xn −−−→ X =⇒ g(Xn ) −−−→ g(X)
                p.s.                       p.s.
        • Xn −−−−→ X =⇒ g(Xn ) −−−−→ g(X)


6     V.A.Rs Indépendantes et Identiquement Distribuées
La f.r. (ou f.d.p./f.m.p.) d’une v.a.r. caractérise complètement sa distribution. En d’autres termes,
elle contient tout ce que nous devons savoir sur la loi du caractère aléatoire de cette variable aléatoire.
Si deux variables aléatoires donnent la même f.r., alors elles ont la même distribution.

Définition 6.1 Soit X et Y deux v.a.rs.
• On dit que X et Y sont identiquement distribuées (i.d. en abrégé),
si et seulement si, elles ont même distribution (i.e. même f.r ou même f.d.p./f.m.p.).
• On dit que X et Y sont indépendantes identiquement distribuées, (i.i.d. en abrégé),
si et seulement si, elles sont indépendantes et elles ont même distribution (loi).

Note. On généralise cette définition pour une suite finie de v.a.rs (Xi )ni=1 .

Définition 6.2 Soit (Xn )n∈N∗ une suite de v.a.rs.
• On dit que (Xn )n∈N∗ est identiquement distribuée (i.d. en abrégé),
si et seulement si, les Xn ont même distribution (i.e. même f.r ou même f.d.p./f.m.p.).
• On dit que (Xn )n∈N∗ est indépendante identiquement distribuée, (i.i.d. en abrégé),
si et seulement si, les Xn sont indépendantes et elles ont même distribution.

Définition 6.3 Soit (Xn )n∈N∗ une suite de v.a.rs.
~~~

## Page 8

~~~text
8                                                                                       Variables aléatoires réelles


Pour tout n ≥ 1, on pose
                                     n                                    n
                                     X                            Sn   1X
                              Sn =         Xi     et       Mn =      =       Xi
                                     i=1
                                                                  n    n i=1

     Sn est appelée somme partielle d’ordre n de la suite (Xn )n∈N∗ .
     Mn est appelée moyenne arithmétique d’ordre n de la suite (Xn )n∈N∗ .

Note. Notons que Sn et Mn , étant des sommes de variables aléatoires, sont elles-mêmes des variables
aléatoires.

Remarque. En statistique, Mn est notée X n et est appelée moyenne empirique.

Propriété 6.4 Soit (Xn )n∈N∗ une suite de v.a.rs.

    • Si (Xn )n∈N∗ est identiquement distribuée et E(|X1 |) < ∞, alors, ∀n ∈ N∗
                                  E(Sn ) = nE(X1 )          et    E(Mn ) = E(X1 )

    • Si (Xn )n∈N∗ indépendante identiquement distribuée et E(|X1 |2 ) < ∞, alors, ∀n ∈ N∗
                                                                              V (X1 )
                                  V (Sn ) = nV (X1 )       et     V (Mn ) =
                                                                                 n
Preuve.


7     Loi des grands nombres
7.1    Loi faible des grands nombres
Théorème 7.1 (Loi faible des grands nombres (LfGN))
Soit (Xn )n∈N∗ une suite de v.a.r.-i.i.d.. Si E(|X1 |2 ) < ∞, alors
                                                       P
                                                Mn −−−→ E(X1 )

Preuve. On applique l’inégalité de Chebyshev. ∀ϵ > 0
                                                                      V (Mn )   V (X1 )
            P (|Mn − E(X1 )| > ϵ) = P (|Mn − E(Mn )| > ϵ) ≤               2
                                                                              =         −−−−−→ 0
                                                                         ϵ        nϵ2 n→+∞
La limite du terme à droite existe puisque V (X1 ) est finie (car E(|X1 |2 ) est finie).

Remarque.
                P (|Mn − E(X1 )| > ϵ) −−−−−→ 0 ⇐⇒ P (|Mn − E(X1 )| ≤ ϵ) −−−−−→ 1
                                           n→+∞                                         n→+∞

La LfGN dit que lorsque n augmente, la probabilité de l’événement "Mn est à moins de ϵ autour de
la moyenne E(X1 )" tend vers 1. Nous pouvons considérer ϵ comme une petite tolérance d’erreur par
rapport à la moyenne E(X1 ).

Application de la LfGN.
Exemple 1. Considérons l’expérience aléatoire qui consiste à lancer une pièce de monnaie n fois. Si
Sn représente le nombre de faces observées dans ces n lancers, alors Sn /n représente la proportion de
faces dans ces n lancers.
La loi des grands nombres prédit que les résultats de la variable aléatoire Sn /n seront, pour les grands
n, proches de 1/2.
Rigoureusement, cela signifie que pour tout ϵ > 0 arbitrairement petit, la probabilité de l’événement
"la proportion de faces diffère de 1/2 de plus de ϵ" tend vers 0 lorsque n tend vers ∞.
~~~

## Page 9

~~~text
Convergence                                                                                        9


En effet. Soit (Xi )i∈N∗ la suite de v.a.rs définie par
                                       (
                                         1 si le i-ème lancer est face
                                 Xi =
                                         0 sinon
Soit
                                        Sn = X1 + X2 + · · · + Xn
La v.a.r. Sn compte le nombre de faces obtenues lors des n lancers.
Les v.a.rs Xi sont i.i.d., Xi ∼ B(1/2) et nous avons
                                              1                              1
                          E(Xi ) = E(X1 ) =     et E(|Xi |2 ) = E((X1 )2 ) =
                                              2                              2
                       1
Puisque E(|X1 |2 ) =     < ∞, par la LfGN, il vient
                       2
                                          Sn          P  1
                                               = Mn −−−→
                                           n             2
Exemple 2. Considérons l’expérience aléatoire qui consiste à lancer un dé honnête à six face, n fois.
Notons Xi le résultat du i-ème lancer. Alors Sn = X1 + X2 + · · · + Xn est la somme des nombre de
points obtenus lors des n lancers. Nous savons que
                                              E(X1 ) = 7/2
Les v.a.rs Xi sont i.i.d. avec E(|X1 | ) = E((X1 )2 ) = 91/6 < ∞. Ainsi par la LfGN,
                                    2

                                            Sn        P  7
                                               = Mn −−−→
                                            n            2

7.2    Loi forte des grands nombres
Théorème 7.2 (Loi forte des grands nombres (LFGN)[Kolmogorov-Khintchine])
Soit (Xn )n≥1 est une suite de v.a.r.-i.i.d.. Alors
                           Mn converge presque sûrement ⇐⇒ E(|X1 |) < ∞
En cas de convergence :
                                                 p.s.
                                           Mn −−−−→ E(X1 )

Preuve.


Application de la LFGN.
Soit (Xn )n∈N∗ une suite de v.a.rs indépendantes
  1) Si pour tout n ∈ N∗ , Xn ∼ B(α), alors E(X1 ) = α.
     Puisque E(|X1 |) = α < ∞, la suite (Mn )n≥1 converge presque sûrement. Donc
                                                        p.s.
                                                 Mn −−−−→ α

  2) Si pour tout n ∈ N∗ , Xn ∼ P(λ), alors E(X1 ) = λ.
     Puisque E(|X1 |) = λ < ∞, la suite (Mn )n≥1 converge presque sûrement. Donc
                                                        p.s.
                                                 Mn −−−−→ λ

  3) Si pour tout n ∈ N∗ , Xn ∼ N (0, 1), alors E(X1 ) = 0.
     Puisque                                                                   r
                                    Z +∞                     Z +∞
                                 1              − 21 x2   2          − 21 x2     2
                     E(|X1 |) = √          |x|e         =√        xe         =     <∞
                                  2π −∞                    2π 0                  π
     la suite (Mn )n≥1 converge presque sûrement. Donc
                                                        p.s.
                                                 Mn −−−−→ 0
~~~

## Page 10

~~~text
10                                                                                  Variables aléatoires réelles


Remarque. Comme la convergence presque sûr implique la convergence en probabilité, nous avons,

                                                         P
     1) Si pour tout n ∈ N∗ , Xn ∼ B(α), alors Mn −−−→ α
                                                         P
     2) Si pour tout n ∈ N∗ , Xn ∼ P(λ), alors Mn −−−→ λ
                                                             P
     3) Si pour tout n ∈ N∗ , Xn ∼ N (0, 1), alors Mn −−−→ 0


8      Central Limit Theorem
Étant donné une v.a.r. X d’espérance E(X) et d’écart type σ(X), nous définissons sa standardisée
comme la nouvelle v.a.r.
                                            X − E(X)
                                      X∗ =
                                               σ(X)

X ∗ est donc obtenue en soustrayant de X son espérance et en divisant par son écart-type. On dit
qu’on centre et on réduit. Rappelons que X ∗ a pour espérance 0 et pour variance 1.
Rappelons aussi que si X suit une distribution normale, alors sa standardisée X ∗ suit une distribution
normale standard et donc a pour espérance 0 et variance 1.

Notons maintenant Sn∗ la v.a.r. standardisée de Sn , i.e.

                                                      Sn − E(Sn )
                                              Sn∗ =
                                                         σ(Sn )

Nous avons le théorème fondamental

Théorème 8.1 (Central Limit Theorem (CLT))
Soit (Xn )n≥1 une suite de v.a.r.-i.i.d.. Si E(|X1 |2 ) < ∞ et V (X1 ) > 0, alors
• la suite de terme général
                                          Sn − E(Sn )  Sn − nE(X1 )
                                  Sn∗ =               = p
                                             σ(Sn )       nV (X1 )
converge en loi vers une v.a.r. Z ∗ suivant une loi normale standard N (0, 1). i.e. :

                                                        L
                                                 Sn∗ −−−→ Z ∗

• En notant Φ la fonction de répartition de Z ∗ , il vient

                                       lim FSn∗ (z) = Φ(z) , ∀z ∈ R
                                    n→+∞


Preuve.


Corollaire 8.2 Soit (Xn )n∈N∗ une suite de v.a.r-i.i.d.. Si E(|X1 |2 ) < ∞ et V (X1 ) > 0, alors

                                          d
                                   Mn∗ −−→ Z ∗ avec Z ∗ ∼ N (0, 1)

Preuve. La v.a.r. Mn∗ , standardisée de, Mn vérifie

                                       Mn − E(Mn )   Sn − E(Sn )
                               Mn∗ =               =             = Sn∗
                                         σ(Mn )         σ(Sn )

On peut par conséquent appliquer le CLT à la suite de v.a.rs de terme générale Mn∗ .
~~~

## Page 11

~~~text
Convergence                                                                                             11


9     Application du Central Limit Theorem
9.1    Préliminaires
Notations:
• Le symbol ≃ est lu "est égal approximativement".
• Le symbol ≈ est lu "suit approximativement".

Définition 9.1 (Échantillon aléatoire)
Une suite finie (Xi )ni=1 de n v.a.r-i.i.d. est appelée échantillon aléatoire de taille n (ou n-échantillon
aléatoire).

Proposition 9.2 (Formule de transformation affine)
Soit a ∈ R∗ , b ∈ R. Alors
                          X ∼ N (µ, σ 2 ) ⇐⇒ Y = aX + b ∼ N (aµ + b, a2 σ 2 )

Preuve.


9.2    Approximation normale standard pour la somme partielle standardisée
       et la moyenne arithmétique standardisée
Proposition 9.3 Soit (Xi )ni=1 un n-échantillon aléatoire avec 0 < V (X1 ) < ∞. Pour n assez grand
                                        FSn∗ (z) ≃ Φ(z) , ∀z ∈ R
et
                                        FMn∗ (z) ≃ Φ(z) , ∀z ∈ R

Preuve.


Interprétation. Pour n assez grand,
Sn∗ et Mn∗ suivent approximativement une loi normale standard, i.e.
                                   Sn∗ ≈ N (0, 1) et     Mn∗ ≈ N (0, 1)

En pratique. En général, pour n ≥ 30, on utilise les approximations ci-dessus.


9.3    Approximation normale pour la moyenne arithmétique
Proposition 9.4 Soit (Xi )ni=1 un n-échantillon aléatoire avec 0 < V (X1 ) < ∞. Pour n assez grand
                                       Mn ≈ N (E(Mn ), V (Mn ))
i.e                                                                    
                                                              V (X1 )
                                       Mn ≈ N       E(X1 ),
                                                                 n
Interprétation. Pour n assez grand,
Mn suit approximativement une loi normale de paramètres µ = E(X1 ) et σ 2 = V (X1 )/n.

Preuve.


Exemple. Soit (Xn )n∈N∗ une suite de v.a.r.-i.i.d. de Bernoulli de paramètre α = 1/2.
Utilisez le CLT pour déterminer une distribution approximative de la moyenne arithmétique des 100
premiers termes de la suite.

Solution.
~~~

## Page 12

~~~text
12                                                                               Variables aléatoires réelles


9.4       Approximation normale pour la somme partielle
Proposition 9.5 Soit (Xi )ni=1 un n-échantillon aléatoire avec 0 < V (X1 ) < ∞. Alors pour n assez
grand
                                          Sn ≈ N (E(Sn ), V (Sn ))

i.e
                                        Sn ≈ N (nE(X1 ), nV (X1 ))


Interprétation. Pour n assez grand,
Sn suit approximativement une loi normale de paramètres µ = nE(X1 ) et σ 2 = nV (X1 ).




Preuve.




Exemple. Une pièce de monnaie équilibrée est lancée 400 fois. Utilisez le CLT pour calculer une
approximation de la probabilité d’obtenir au moins 205 faces.


Solution.




Algorithme. Comment appliquer le CLT.

      1) Écrire la v.a.r. X qui nous intéresse comme la somme de n v.a.r.-i.i.d. Xi :

                                               X = X1 + · · · + Xn


      2) Calculer E(X) et V (X) en utilisant les formules

                                     E(X) = nE(X1 ) et V (X) = nV (X1 )


      3) pour n assez grand
                                            L(X) ≃ N (E(X), V (X))

         Ou bien, utiliser la standardisée de X.
               X − E(X)
         X∗ = p             suit approximativement une loi normale standard.
                  V (X)

                                                    FX ∗ ≃ Φ


Exemple. Un caissier de banque sert un par un les clients debout dans la file d’attente. Supposons que
le temps de service (en minutes) Xi pour le client i a pour moyenne E(Xi ) = 2 min et V (Xi ) = 1 min2 .
Supposons que les délais de service pour les différents clients de la banque sont indépendants. Soit X
le temps total que le caissier de banque passe à servir les 50 clients. Trouvez P (90 < X ≤ 110).


Solution.
~~~

## Page 13

~~~text
Convergence                                                                                       13


9.5     Approximation normale pour la loi binomiale
Définition 9.6 Soit α ∈ ]0, 1[. On dit qu’une v.a.r. discrète X suit une loi de Bernoulli de
paramètre α, si et seulement si, sa fonction de masse de probabilité est
                                              
                                              1 − α si k = 0
                                              
                                      pX (k) = α       si k = 1
                                                       sinon
                                              
                                                0
                                              

Notation:
                                                X ∼ B(α)

• Une v.a.r. qui suit une loi de Bernoulli est dite v.a.r. de Bernoulli.

Proposition 9.7 Soit α ∈]0, 1[. Soit (Xi )ni=1 un n-échantillon aléatoire avec X1 ∼ B(α). Alors
                                                n
                                                X
                                         Sn =         Xi ∼ B(n, α)
                                                i=1


Preuve.



Proposition 9.8 Soit X ∼ B(n, α). Alors pour n assez grand

                                        X ≈ N (nα, nα(1 − α))

Preuve.



En pratique. Lorsque (n ≥ 30 et nα ≥ 5 et n(1 − α) ≥ 5) ou bien (nα ≥ 15 et n(1 − α) ≥ 15), on
utilise l’approximation
                                 B(n, α) ≃ N (nα, nα(1 − α))

Preuve. Pour n assez grand, le CLT nous permet d’approcher la loi de Sn par une loi normale, i.e :

                                    B(n, α) ≃ N (nE(X1 ), nV (X1 ))

Comme E(X1 ) = α et V (X1 ) = α(1 − α)), il vient

                                      B(n, α) ≃ N (nα, nα(1 − α))

Exemple. Soit n ∈ N∗ et c ∈ R. Soit X une v.a.r. discrète telle que : X ∼ B(n, 0.6). On donne

                       pX (0) = 10−39 et P (E[X] − c < X ≤ E[X] + c) = 0.95

1)    a) Donner la f.m.p. de X.
      b) Calculer approximativement la valeur de n.

2)    a) Par quelle loi peut-on approcher la loi de X ? Justifier.
      b) Calculer approximativement la valeur de c.

Solution.
~~~

## Page 14

~~~text
14                                                                                Variables aléatoires réelles


9.6      Approximation normale pour la loi de Poisson
Définition 9.9 Soit λ ∈ R∗+ . On dit qu’une v.a.r. X suit une loi de Poisson de paramètre λ, si et
seulement si, sa fonction de masse de probabilité est
                                            
                                             −λ λk
                                               e       , ∀k ∈ N
                                   pX (k) =         k!
                                            0           sinon

où k! est le factoriel de k.
Notation :
                                                 X ∼ P(λ)

• Une v.a.r. qui suit une loi de Poisson est dite v.a.r. de Poisson.

Proposition 9.10 Soit α ∈ R∗+ . Soit (Xi )ni=1 un n-échantillon aléatoire avec X1 ∼ P(α). Alors
                                                 n
                                                 X
                                          Sn =         Xi ∼ P(nα)
                                                 i=1


Preuve.


Proposition 9.11 Soit X ∼ P(λ). Alors, pour λ assez grand

                                              X ≈ N (λ, λ)

Preuve.


En pratique. Lorsque λ ≥ 15, on utilise l’approximation

                                             P(λ) ≃ N (λ, λ)

En posant λ = nα, la valeur minimale de n sera fixé par la valeur de α. On doit avoir n ≥ 15/α.

Preuve. Pour n assez grand, le CLT nous permet d’approcher la loi de Sn par une loi normale, i.e :

                                     P(nα) ≃ N (nE(X1 ), nV (X1 ))

Comme E(X1 ) = α et V (X1 ) = α, il vient

                                          P(nα) ≃ N (nα, nα)

Exemple. Le nombre d’étudiants X qui s’inscrivent à un cours de statistique est une variable aléatoire
de Poisson de moyenne 100. Le professeur responsable du cours a décidé que si le nombre d’inscrits
est de 120 ou plus, il enseignera le cours en deux sections distinctes, alors que si moins de 120 étudiants
s’inscrivent, il enseignera à tous les étudiants ensemble dans une seule section. Quelle est la probabilité
que le professeur doive enseigner deux sections ?

     1) Donnez la solution exacte.
     2) Donnez une solution approximative.

Solution.


                                                 Résumé
~~~

## Page 15

~~~text
Convergence                                                                                             15


CLT en théorie.
• FSn∗ (z) −−−−−→ Φ(z) , ∀z ∈ R
          n→+∞

• FMn∗ (z) −−−−−→ Φ(z) , ∀z ∈ R
           n→+∞


CLT en pratique. Pour n assez grand
• Sn∗ ≈ N (0, 1). i.e. FSn∗ (z) ≃ Φ(z) , ∀z ∈ R.
• Mn∗ ≈ N (0, 1). i.e. FMn∗ (z) ≃ Φ(z) , ∀z ∈ R.

• Sn ≈ N (E(Sn ), V (Sn )) = N (nE(X1 ), nV (X1 )).
                                                  
                                           V (X1 )
• Mn ≈ N (E(Mn ), V (Mn )) = N E(X1 ),               .
                                              n

9.7    Correction de continuité pour les v.a.rs discrètes
Lorsqu’on approche une loi discrète par une loi continue, dans le but de faire des calculs de probabilités,
le résultat est parfois peu satisfaisant. Afin d’améliorer la précision des calculs, un ajustement, connu
sous le nom de correction de continuité, est parfois nécessaire.
Supposons que X soit une v.a.r. qui ne prend que des valeurs entières et telles que

                                          X ≈ N (E(X), V (X))

Pour tenir compte du caractère discret de X, nous écrivons la probabilité P (X = k) (qui serait
exactement 0 sous l’approximation par la loi normale) comme P (k − 1/2 < X ≤ k + 1/2) (pour que
X prenne ses valeurs dans un intervalle de longueur non nulle) et appliquer l’approximation normale
à ce dernier. Ainsi
• Pour k ∈ X(Ω), on obtient

                     P (X = k) = P (k − 1/2 < X ≤ k + 1/2)
                                                    !                              !
                                     k + 1/2 − E(X)               k − 1/2 − E(X)
                               ≃Φ        p            −Φ              p
                                           V (X)                        V (X)

• Pour i, j ∈ X(Ω) avec i ≤ j, on obtient

                    P (i ≤ X ≤ j) = P (i − 1/2 < X ≤ j + 1/2)
                                                        !                            !
                                         j + 1/2 − E(X)             i − 1/2 − E(X)
                                  ≃Φ         p            −Φ            p
                                               V (X)                      V (X)

Application à la loi binomiale.
Si X ∼ B(n, α), alors pour n assez grand,

                              X ≈ N (E(X), V (X)) = N (nα, nα(1 − α))

et donc

                        P (X = k) = P (k − 1/2 < X ≤ k + 1/2)
                                                     !                   !
                                        k + 1/2 − np        k − 1/2 − np
                                  ≃Φ p                 −Φ p
                                           np(1 − p)           np(1 − p)

Exemple. Supposons que X ∼ B(50, 0.4). Calculer P (X = 20).

  1) Donner la solution exacte.
  2) Donner une solution approchée.
~~~

## Page 16

~~~text
16                                                                            Variables aléatoires réelles


Solution.


Application à la loi de Poisson. Si X ∼ P(λ), alors pour λ assez grand,

                                     X ≈ N (E(X), V (X)) = N (λ, λ)

et donc

                           P (X = k) = P (k − 1/2 < X ≤ k + 1/2)
                                                                       
                                           k + 1/2 − λ        k − 1/2 − λ
                                     ≃Φ        √         −Φ       √
                                                 λ                  λ

Exemple. Supposons que X ∼ P(25). Calcules P (X = 20).

     1) Donner la solution exacte.
     2) Donner une solution approchée.

Solution.


Free Online Statistical Table :
http://stattrek.com/online-calculator/binomial.aspx      (loi binomiale)
http://stattrek.com/online-calculator/normal.aspx        (loi normale)
~~~
