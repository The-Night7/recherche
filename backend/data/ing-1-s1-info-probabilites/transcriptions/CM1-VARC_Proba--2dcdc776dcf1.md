# CM1-VARC_Proba.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Elf5CDobdor75pWO7_NmpWmirsI0VnGK) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                      Variables aléatoires réelles continues
                                        Khalid El Amine I.
                                       Department of Mathematics
                                                FFF


Dans tout ce chapitre :
     Ω est un univers.

     (Ω, A) est un espace probabilisable.

     (Ω, A, P ) est un espace probabilisé.

     R sera toujours muni de la tribu de Borel, B(R).

     Toutes les variables aléatoires sont dénies sur un espace probabilisé (Ω, A, P ) et à valeurs dans
      l'espace probabilisable (R, B(R)).
     On considère les variables aléatoires réelles X telles que X(Ω) est non discret.


1     Variable aléatoire réelle

Dénition 1.1 (Variable aléatoire réelle)
On appelle variable aléatoire réelle (v.a.r. en abrégé) sur (Ω, A) toute fonction
                                       X : (Ω, A) −→ (R, B(R))

vériant :
                                       X −1 (B) ∈ A, ∀B ∈ B(R)
• X(Ω) est appelé univers image de Ω par X .

Proposition 1.2 Soit X : (Ω, A) −→ (R, B(R)) une fonction. Alors
             X est une v.a.r. sur (Ω, A), si et seulement si, X −1 (] − ∞, x]) ∈ A, ∀x ∈ R

Preuve.


1.1 Loi d'une variable aléatoire réelle
Dénition 1.3 (Loi d'une v.a.r.)
Soit X : (Ω, A) → (R, B(R)) une v.a.r.. Soit P une probabilité sur (Ω, A). La fonction

                               PX : B(R)      −→    R
                                    B         7−→   PX (B) = P (X −1 (B))

est appelée probabilité image de P par X , ou loi de X sous P .

Remarque. PX est parfois notée L(X) et simplement appelée loi de X.

                                                    1
~~~

## Page 2

~~~text
2                                                                                                K. El Amine




Proposition 1.4 Soit X : (Ω, A) → (R, B(R)) une v.a.r.. Soit P une probabilité sur (Ω, A). Alors
                                    PX est une probabilité sur (R, B(R))

i.e
                                   (R, B(R), PX ) est un espace probabilisé.

Proof.

Remarque. Dans la suite, on notera simplement X : Ω −→ R au lieu de X : (Ω, A) −→ (R, B(R)).

1.2 Fonction de répartition d'une variable aléatoire réelle
Dénition 1.5 (Fonction de répartition d'une v.a.r.)
Soit X une v.a.r.. La fonction
                                   FX : R     −→    R
                                        x     7−→   FX (x) = PX (] − ∞, x])

est appelée fonction de répartition de X , (abrégée en f.r.).
Remarque.
• ∀x ∈ R, FX (x) ∈ [0, 1].
• FX (x) représente la probabilité de toutes les réalisations inférieures ou égales au réel x.
• La f.r. FX est aussi appelée fonction de distribution cumulative de X , (abrégée en f.d.c.).

Proposition 1.6 Soit X une v.a.r. et FX sa f.r.. Alors :
      1) FX est croissante sur R
      2)   lim FX (x) = 0 et lim FX (x) = 1
           x→−∞              x→+∞

      3) FX est continue à droite sur R
Preuve.

Remarque. Comme FX est monotone et bornée, elle admet une limite (nie) à gauche en tout point
de R.

On rappelle le théorème suivant
Théorème 1.7 Si une fonction est monotone sur un intervalle de R, alors l'ensemble des points où
elle n'est pas continue est ni ou dénombrable.

Remarque. Toute f.r. est donc continue sur R, sauf éventuellement sur une partie discrète.
Proposition 1.8 Soit F : R → R une fonction.
Si
      1) F est croissante sur R
      2)   lim F (x) = 0 et lim F (x) = 1
           x→−∞              x→+∞

      3) F est continue à droite sur R
Alors, F est la f.r. d'une certaine v.a.r..
Proof.
~~~

## Page 3

~~~text
v.a.r. continues                                                                                  3


Notations. Pour alléger les notations, on écrira :
     {X ∈ B} pour l'ensemble X −1 (B) où B ∈ B(R), i.e. :
                                   {X ∈ B} = X −1 (B) = {ω ∈ Ω : X(w) ∈ B}
      De même :
     {X = x} = X −1 ({x}) = {ω ∈ Ω : X(w) = x}, où x ∈ R.
     {X ≤ x} = X −1 (] − ∞, x]) = {ω ∈ Ω : X(ω) ≤ x}
     {X < x} = X −1 (] − ∞, x[) = {ω ∈ Ω : X(ω) < x}
     {a < X ≤ b} = X −1 (]a, b]) = {ω ∈ Ω : a < X(ω) ≤ b}
     etc.

     ∀a ∈ R
                               FX (a− ) = lim− FX (x) and FX (a+ ) = lim+ FX (x)
                                          x→a                           x→a

Proposition 1.9 Soit X une v.a.r. et FX sa f.r.. Soit a, b ∈ R avec a < b. Alors :
  1) P ({X ≤ a}) = FX (a)
  2) P ({X > a}) = 1 − FX (a)
  3) P ({a < X ≤ b}) = FX (b) − FX (a)
  4) P ({X = a}) = FX (a+ ) − FX (a− )
Preuve.

Proposition 1.10 Soit X et Y deux v.a.r. sur le même (Ω, A, P ). Alors
                                  FX = FY , si et seulement si, PX = PY

Preuve.

Remarque. La fonction de répartition FX d'une v.a.r. caractérise complètement sa loi PX .

1.3 Indépendance de variables aléatoires réelles
1.3.1 Indépendance de deux variables aléatoires réelles
Dénition 1.11 (Indépendance de deux v.a.rs)
Sot X et Y deux v.a.rs sur le même (Ω, A, P ). X et Y sont dites indépendantes, si et seulement si,
                   ∀B, B 0 ∈ B(R) les événement X −1 (B) et Y −1 (B 0 ) sont indépendants

Notation. Notons I , l'ensemble des intervalles de R.

Proposition 1.12 Soit X et Y deux v.a.rs sur le même (Ω, A, P ).
Les assertions suivantes sont équivalentes
  1) X et Y sont indépendantes.
  2) ∀(B, B 0 ) ∈ (B(R))2 ,       P ({X ∈ B} ∩ {Y ∈ B 0 }) = P ({X ∈ B})P ({Y ∈ B 0 })
  3) ∀(I, I 0 ) ∈ (I)2 ,     P ({X ∈ I} ∩ {Y ∈ I 0 }) = P ({X ∈ I})P ({Y ∈ I 0 })
  4) ∀(x, y) ∈ R2 ,        P ({X ≤ x} ∩ {Y ≤ y}) = P ({X ≤ x})P ({Y ≤ y})

Preuve.
~~~

## Page 4

~~~text
4                                                                                                       K. El Amine




Rappel. Si A est un événement, alors sa fonction indicatrice IA est une v.a.r..

Proposition 1.13 Deux événements A et A0 sont indépendant, si et seulement si, leurs fonctions
indicatrices IA et IA0 sont indépendantes.

Proof.


1.3.2 Indépendance d'une suite de variables aléatoires réelles
Dénition 1.14 (Indépendance d'une suite nie de v.a.rs)
Soit n ∈ N avec n > 1. Soit (X1 , . . . , Xn ) une suite nie de n v.a.rs sur le même (Ω, A, P ).
La suite (X1 , . . . , Xn ) est dite indépendante, si et seulement si,

      ∀(B1 , . . . , Bn ) ∈ (B(R))n , la suite d'événements (X1−1 (B1 ), . . . , Xn−1 (Bn )) est indépendante

Proposition 1.15 Soit n ∈ N avec n > 1. Soit (X1 , . . . , Xn ) une suite nie de n v.a.rs sur (Ω, A, P ).
Les assertions suivantes sont équivalentes

    1) (X1 , . . . , Xn ) est une suite indépendante
    2) ∀(B1 , . . . , Bn ) ∈ (B(R))n , P ({X1 ∈ B1 } ∩ . . . ∩ {Xn ∈ Bn }) = P ({X1 ∈ B1 }) · · · P ({Xn ∈ Bn })
    3) ∀(I1 , . . . , In ) ∈ (I)n , P ({X1 ∈ I1 } ∩ . . . ∩ {Xn ∈ In }) = P ({X1 ∈ I1 }) · · · P ({In ∈ Bn })
    4) ∀(x1 , . . . , xn ) ∈ Rn , P ({X1 ≤ x1 } ∩ . . . ∩ {Xn ≤ xn }) = P ({X1 ≤ x1 }) . . . P ({Xn ≤ xn })

Proof.

Proposition 1.16 Soit n ∈ N avec n > 1. Soit (X1 , . . . , Xn ) une suite nie de n v.a.rs sur (Ω, A, P ).
Pour chaque i ∈ [[1, n]], soit fi : R → R une fonction quelconque. Alors

               (X1 , . . . , Xn ) est indépendante =⇒ (f1 (X1 ), . . . , fn (Xn )) est indépendante

Preuve.
Dénition 1.17 (Indépendance d'une suite innie de v.a.rs)
Soit (Xn )n∈N∗ une suite de v.a.rs sur (Ω, A, P ). La suite (Xn )n∈N∗ est dite indépendante, si et
seulement si, pour toute partie nie I de N∗ , avec |I| > 1, la suite nie (Xi )i∈I est indépendante.
~~~

## Page 5

~~~text
v.a.r. continues                                                                                        5


2      Variable aléatoire réelle continue

Dénition 2.1 (v.a.r. continue)
Une v.a.r. X est dite continue, si et seulement si, sa f.r. FX est continue sur R.

Proposition 2.2 Soit X une v.a.r.. Alors
                       X est continue, si et seulement si, P ({X = x}) = 0, ∀x ∈ R

Preuve.


Remarque. Soit a ∈ R. P ({X = a}) = 0 n'implique pas que l'événement {X = a} est impossible. Si
c'était le cas, alors pour tout x ∈ R, l'événement {X = x} serait impossible et X ne pourrait prendre
aucune valeur.

Proposition 2.3 Soit X une v.a.r. continue. Alors, ∀B ∈ B(R),
                                  B est discret =⇒ P ({X ∈ B}) = 0

Preuve.


Exercice. Supposons que X soit une v.a.r. continue.
    1) Que vaut P ({X ∈ Q}) ?
    2) Que vaut P ({X ∈ [0, 1] ∩ Q})?

Solution.

Proposition 2.4 Soit X une v.a.r. continue de f.r. FX . Pour tout a, b ∈ R avec a < b :
• P ({X < a}) = P ({X ≤ a}) = FX (a)
• P ({X ≥ a}) = P ({X > a}) = 1 − FX (a)
• P ({a < X < b}) = P ({a ≤ X < b}) = P ({a ≤ X ≤ b}) = P ({a < X ≤ b}) = FX (b) − FX (a)

Preuve. Par application de de l'égalité P ({X = x}) = 0, ∀x ∈ R et de la dénition d'une f.r. d'une
v.a.r..


3      Variable aléatoire réelle absolument continue


3.1 Fonction de densité de probabilité
Dénition 3.1 (Fonction de densité de probabilité)
Soit f : R −→ R une fonction.
On dit que f est une fonction de densité de probabilité (f.d.p. en abrégé) sur R, si et seulement si,

 (1) f (x) ≥ 0, ∀x ∈ R
 (2) f est continue sur R sauf sur une partie nie.
       Z +∞
 (3)           f (x)dx = 1
          −∞
~~~

## Page 6

~~~text
6                                                                                                           K. El Amine




Exemple. Soit f : R −→ R la fonction dénie par
                                               f (x) = |x|I[−1,1]
Vérier que f est une fonction de densité de probabilité.
Solution.
Remarque. Soit f une fonction de densité de probabilité.
     f peut ne pas être bornée.
                       Z
     (f ≥ 0 sur R et     f (x)dx = 1) ; (f ≤ 1 sur R) ; contrairement à la fonction de masse de
                          R
      probabilité. f (x) ne correspond pas à une valeur de probabilité.
Exemple. Soit f : R −→ R dénit par
                                              (
                                                  4
                                                   √1
                                                       |x|
                                                                  si 0 < |x| ≤ 1
                                    f (x) =
                                                    sinon
                                                      0
Montrer que f est fonction de densité de probabilité.
Solution.


3.2 Variable aléatoire réelle absolument continue
Dénition 3.2 (v.a.r. absolument continue)
Une v.a.r. X est dite absolument continue (ou de loi absolument continue), si et seulement si,
il existe une f.d.p. noté fX , telle que :
                                                                         Z
                                ∀B ∈ B(R)         P ({X ∈ B}) =               fX (x)dx
                                                                          B
Dans ce cas
• fX est alors appelée fonction de densité de probabilité de X .
• SX = {x ∈ R : fX (x) 6= 0} est appelé support de la loi de X .

Rappel. La loi de probabilité d'une v.a.r. X , noté PX , est une probabilité sur (R, B(R)). Elle est
dénit par
                                   ∀B ∈ B(R)          PX (B) = P ({X ∈ B})
Remarque. Il n'y a pas d'unicité de la f.d.p. pour une v.a.r. X .
Si fX est une f.d.p. de X , alors n'importe quelle f.d.p. f égale à fX sauf (par exemple) sur un
ensemble ni de points est aussi une f.d.p. de X . Par exemple
                    f1 (x) = I[0,1] ; f2 (x) = I]0,1] ; f3 (x) = I[0,1[ ; f4 (x) = I]0,1[
sont des f.d.p. de la même v.a.r..
Exemple. Si X est une v.a.r. absolument continue de f.d.p. fX , alors :
                                                   Z                         Z 3
                              P ({X ∈ [1, 3]}) =              fX (x)dx =           fX (x)dx
                                                      [1,3]                   1

On rappelle que {X ∈ [1, 3]} se note {1 ≤ X ≤ 3}.
Proposition 3.3 Soit X une v.a.r..
                          Si X est absolument continue, alors X est continue
Preuve. ∀a ∈ R
                                   Z                      Z a                          Z a
P ({X = a}) = P ({X ∈ {a}}) =              fX (x)dx =             fX (a)dx = fX (a)          1dx = fX (a) × 0 = 0
                                     {a}                      a                          a
~~~

## Page 7

~~~text
v.a.r. continues                                                                                7


3.3 Fonction de répartition d'une variable aléatoire réelle absolument con-
    tinue
Théorème 3.4 Soit X une v.a.r. absolument continue, de f.d.p. fX . La f.r. de X , notée FX est
donnée par :                                   Z x
                                   FX (x) =             fX (t)dt   ∀x ∈ R
                                                   −∞

Preuve. Vient de la formule de la loi d'une v.a.r. absolument continue.
                                                                            Z x
                     FX (x) = P ({X ≤ x}) = P ({X ∈] − ∞, x]}) =                  fX (t)dt
                                                                             −∞

Graphe de FX :




Exemple. Soit f : R −→ R la fonction dénie par f (x) = c(1 − x)I[0,1] (x), où c ∈ R.
  1) Déterminer la constante c pour que f soit une f.d.p.. Tracer la courbe de f .
  2) Supposons que X soit une v.a.r. absolument continue ayant f pour f.d.p..
     Déterminer FX , la f.r. de X et dessiner sa courbe.
Solution.

Proposition 3.5 Soit X une v.a.r. absolument continue de f.d.p. fX et de f.r. FX .
Pour tout a, b ∈ R avec a < b :
                                             Z a
• P ({X < a}) = P ({X ≤ a}) = FX (a) =             fX (t)dt
                                              −∞
                                                   Z +∞
• P ({X ≥ a}) = P ({X > a}) = 1 − FX (a) =                fX (t)dt
                                                   a
                                        Z b
• P ({a < X ≤ b}) = FX (b) − FX (a) =         fX (t)dt
                                         a

• P ({a < X < b}) = P ({a ≤ X < b}) = P ({a ≤ X ≤ b}) = P ({a < X ≤ b})

Preuve. Par application de de l'égalité P ({X = x}) = 0, ∀x ∈ R ; de la dénition d'une f.r. d'une
v.a.r. et de la dénition de la loi d'une v.a.r. absolument continue.
Représentations graphique de P ({X < a}), P ({X ≥ a}) et P ({a < X < b}) :
~~~

## Page 8

~~~text
8                                                                                          K. El Amine




Proposition 3.6 Soit X une v.a.r. et FX sa f.r..
Si X est absolument continue de f.d.p. fX , alors

    1) FX est continue sur R.
    2) FX est de classe C 1 sur R, sauf sur une partie nie.
    3) Si fX est continue en x0 ∈ R, alors FX est dérivable en ce point et on a :
                                                      0
                                                     FX (x0 ) = fX (x0 )

Preuve.

La réciproque du résultat ci-dessus est donnée par le

Théorème 3.7 Soit X une v.a.r. de f.r. FX .
Si FX vérie :

    (1) FX est continue sur R.
    (2) FX est de classe C 1 sur R, sauf en un nombre ni de points.

Alors

    1) X est une v.a.r. absolument continue.
    2) Toute fonction f : R → R telle que
                                (
                                    f ≥0             sur R
                                                     en tout point x où FX est dérivable
                                             0
                                    f (x) = FX (x)

        est une f.d.p. de X .

Preuve.


Remarque Importante. Si X est une v.a.r. absolument continue de f.r. FX , alors FX est dérivable
presque partout (théorème de diérentiation de Lebesgue). Ceci permet d'associer à X une f.d.p.
fX de façon canonique. Dans la pratique on prendra
                             (
                               FX0
                                   (x) en tout point x où FX est dérivable
                    fX (x) =
                               0        ailleurs

Exemple. Soit X une v.a.r. dont la f.r. FX est dénit par
                                                    
                                                    
                                                    
                                                    
                                                      0      if x ≤ 0
                                                    
                                            FX (x) = x       if 0 ≤ x ≤ 1
                                                    
                                                    
                                                    
                                                    1       if 1 ≤ x
Montrer que X est absolument continue et proposer une f.d.p. de X .

Solution.
~~~

## Page 9

~~~text
v.a.r. continues                                                                                         9




                                    Figure 1: Fonction de Cantor

Discussion. Existence de v.a.r. continue mais non absolument continue.
Dans tous les cas raisonnables, une v.a.r. continue aura une f.d.p. ; c'est-à-dire qu'elle sera absolument
continue. Toutefois, il est possible d'établir l'existence de v.a.rs qui sont continues mais pas absolument
continues. Un exemple remarquable est la loi de Cantor. La f.r. F de la loi de Cantor est continue
sur R et dérivable (de dérivée nulle) presque partout, mais elle n'est pas absolument continue.

La loi de Cantor est une loi de probabilité singulière dont le support est l'ensemble de Cantor. Sa
f.r. est représentée par l'escalier de Cantor, aussi appelé escalier du diable (voir gure 1).

La loi de Cantor a les propriétés suivantes :
     Elle n'est pas absolument continue (par rapport à la mesure de Lebesgue), car elle n'admet pas
      de fonction de densité de probabilité.
     Elle n'est pas discrète, car elle n'admet pas de fonction de masse de probabilité.
     Elle n'est pas non plus une loi mixte (des deux lois citées ci-dessus).
     Son support est non discret et de mesure de Lebesgue nulle.


4     Moments d'une variable aléatoire réelle absolument continue

On abrégera souvent variable aléatoire réelle absolument continue en v.a.r.a.c..

4.1 Espérance
Dénition 4.1 (Espérance)
Soit X une v.a.r.a.c. de f.d.p. fX . On dit que X admet une espérance, si est seulement si,
                                        Z +∞
                                                |x|fX (x)dx < +∞
                                          −∞

Dans ce cas, l'espérance de X est notée E(X) et elle est dénie par :
                                                  Z +∞
                                        E(X) =           xfX (x)dx
                                                   −∞
~~~

## Page 10

~~~text
10                                                                                      K. El Amine




              Z +∞
Remarque.            |x|fX (x)dx existe toujours, c'est un élément de [0, +∞].
               −∞
La nitude de cette intégrale garantie que l'espérance E(X) est bien dénie.

Exemple. Loi de Cauchy standard
Soit X une v.a.r.a.c. de f.d.p.
                                                  1 1
                                       fX (x) =            ∀x ∈ R
                                                  π 1 + x2
Montrer que X n'admet pas d'espérance.

Solution.


4.2 Propriétés de l'espérance
Théorème 4.2 (Théorème de transfert)
Soit X : Ω → R une v.a.r.a.c. de f.d.p. fX .
Soit g : R −→ R une fonction continue par morceaux (g mesurable sut). Alors
• La v.a.r. g(X) est absolument continue.
     Z +∞
• Si       |g(x)|fX (x)dx < ∞, alors, g(X) admet une espérance. Elle est donnée par
      −∞
                                                  Z +∞
                                     E(g(X)) =           g(x)fX (x)dx
                                                   −∞

Preuve.

Exemple. Soit X une v.a.r.a.c. de f.d.p.
                                          fX (x) = 3x2 I[0,1] (x)
Que vaut (a) E(X) ? (b) E(X 2 ) ? (c) E(X + X 2 ) ?

Solution.

Corollaire 4.3 Soit X une v.a.r.a.c. admettant une espérance. Soit a, b ∈ R. Alors la v.a.r. aX + b
est absolument continue et admet un espérance donnée par
                                        E(aX + b) = aE(X) + b

Preuve.
Remarque. En paticulier
                                    E(aX) = aE(X)        ;   E(a) = a

Proposition 4.4 (Croissance de l'espérance)
Soit X et Y deux v.a.r.a.cs. sur le même (Ω, A, P ), chacune admettant une espérance. Alors
                                    Y ≤X       =⇒       E(Y ) ≤ E(X)
En particulier :
                                       0≤X        =⇒     0 ≤ E(X)
et pour a, b ∈ R :
                                   a≤X≤b          =⇒     a ≤ E(X) ≤ b

Preuve.
~~~

## Page 11

~~~text
v.a.r. continues                                                                                    11


Théorème 4.5 (Linéarité de l'espérance)
Soit X et Y deux v.a.r.a.cs. sur le même (Ω, A, P ), chacune admettant une espérance. Soit a, b ∈ R.
Alors, la v.a.r. aX + bY admet une espérance et :

                                   E(aX + bY ) = aE(X) + bE(Y )

En particulier
                                      E(X + Y ) = E(X) + E(Y )

Preuve.

Note. Même si X et Y sont absolument continues, rien ne garantie que la v.a.r. aX + bY soit
absolument continue.

4.3 Variance & Ecart-type
Dénition 4.6 (Variance & Ecart-type)
Soit X une v.a.r.a.c. de f.d.p. fX et admettant une espérance E(X).

     La variance de X est dénit par :
                                                       Z +∞
                          V (X) = E((X − E(X))2 ) =           (x − E(X))2 fX (x)dx
                                                         −∞

      sous réserve de convergence de l'intégrale.
     L'écart-type de X est dénit par :               p
                                              σ(X) =       V (X)
      sous réserve d'existence de V (X).

Remarque.
• V (X) est l'écart quadratique moyen de la variable aléatoire X par rapport à sa valeur moyenne.
• V (X) est donc un indicateur mesurant la dispersion
                                                 p des valeurs x de X autour de leurs moyenne
pondérée E(X). Plus précisément, c'est σ(X) = V (X) qui mesure l'étendue de cette dispersion.
Une petite variance signie que X est fortement concentré et une grande variance signie que X est
dispersée.

Dénition 4.7 (v.a.r. centrée (resp. centrée réduite))
Soit X une v.a.r.a.c.. On dit que :

     X est centrée, si elle admet une espérance nulle, (i.e. E(X) = 0).

     X est centrée réduite, si elle admet une espérance nulle et une variance égale à 1,
      (i.e. E(X) = 0 et V (X) = 1).

Théorème 4.8 Soit X une v.a.r.a.c..
     Si X admet une espérance, alors X − E(X) est centrée.

                                                       X − E(X)
     Si X admet une variance non nulle, alors X ∗ =            est centrée réduite.
                                                         σ(X)

Preuve.
~~~

## Page 12

~~~text
12                                                                                            K. El Amine




4.4 Moments d'ordre supérieur
Dénition 4.9 (Moments)
Soit X une v.a.r.a.c. de f.d.p. fX . Soit m ∈ N∗ . Sous réserve de convergence absolue de l'intégrale :
      Le moment d'ordre m de X est déni par
                                                     Z +∞
                                         E(X m ) =          xm fX (x)dx
                                                     −∞

      Le moment centré d'ordre m de X est déni par
                                                Z +∞
                             E((X − E(X))m ) =       (x − E(X))m fX (x)dx
                                                      −∞

Proposition 4.10 Soit X une v.a.r.. Si X admet un moment d'ordre m ∈ N∗ alors X admet des
moments de tout ordre j ∈ J1, mK.

Preuve.

Théorème 4.11 (Formule de Köenig-Huyghens)
Soit X une v.a.r.. Si E(X 2 ) existe, alors V (X) existe et elle est donné par :
                                        V (X) = E(X 2 ) − E 2 (X)

Preuve.

Proposition 4.12 Soit X une v.a.r. admettant une variance. Alors :
      V (X) ≥ 0
      V (aX + b) = a2 V (X),    ∀a, b ∈ R

Preuve.

Exemple. Soit X une v.a.r.a.c. telle que
                                                3              3
                                       E(X) =     et E(X 2 ) =
                                                4              5
     1) Calculer V (X).
     2) Soit Y une nouvelle v.a.r. dénie par Y = 3X − 2. Calculer (a) E(Y ) et (b) V (Y ).

Solution.


4.5 Cas de deux v.a.r.a.cs indépendantes
Proposition 4.13 Soit X et Y deux v.a.rs admettant chacune un moment d'ordre 2.
Si X et Y sont indépendantes, alors :
                                         E(XY ) = E(X)E(Y )
and
                                       V (X + Y ) = V (X) + V (Y )

Preuve.
~~~

## Page 13

~~~text
v.a.r. continues                                                                                     13


5     Lois continues usuelles

     Toutes les v.a.rs absolument continues ci-après sont dénies sur un espace probabilisé (Ω, A, P ).

     v.a.r. absolument continue sera abrégée en v.a.r.a.c..


5.1 Loi continue uniforme
Dénition 5.1 Soit a et b deux réels, avec a < b. On dit qu'une v.a.r.a.c. X suit une loi continue
uniforme sur [a, b], si et seulement si, elle admet pour f.d.p.
                                                       1
                                           fX (x) =       I[a,b] (x)
                                                      b−a
On note alors
                                                X ∼ U([a, b])

Modélisation. La distribution uniforme U([a, b]) est utiliser pour modéliser une v.a.r. pouvant se
produire équitablement entre a et b.

Interprétation. X ∼ U([a, b]) signie : ∀ [u, v] ⊂ [a, b] et ∀ [u0 , v0 ] ⊂ [a, b]
                          v − u = v 0 − u0 =⇒ P (X ∈ [u, v]) = P (X ∈ [u0 , v 0 ])

i.e. si [u, v] et [u0 , v 0 ] sont deux segments de même longueur, alors les événements {X ∈ [u, v]} et
{X ∈ [u0 , v 0 ]} sont équiprobable.

Exemple. Un nombre représenté par X est choisie au hasard entre a et b. X est supposé être
uniformément distribuée veut dire que la probabilité que X tombe dans un intervalle de longueur l ne
dépend que de l, pas de la position de l'intervalle dans [a, b].

Exercice. Soit X ∼ U([a, b]). Vérier que fX est une f.d.p..

Solution.


Proposition 5.2 Si X ∼ U([a, b]), alors :
                                            a+b                     (b − a)2
                                  E(X) =              et V (X) =
                                             2                         12

Preuve.


Proposition 5.3 Si X ∼ U([a, b]), alors sa f.r. est donnée par :
                                              
                                              
                                              
                                              
                                               0            si x < a
                                              
                                              x − a
                                     FX (x) =               si a ≤ x ≤ b
                                              
                                               b−a
                                              
                                              
                                              1            si b < x

Preuve.
~~~

## Page 14

~~~text
14                                                                                                  K. El Amine




             fX (x)                                                    FX (x)



                                                                            1


                1
               b−a




                         a                         x                              a                       x
                                    b                                                        b

           Figure 2: f.d.p. de X ∼ U([a, b])                          Figure 3: f.r. de X ∼ U([a, b])

Exercice. Soit c ∈ R∗ . Soit f : R → R la fonction dénie par :
                                                   (
                                                       c    si x ∈ [0, 1]
                                         f (x) =
                                                       0    sinon

     1) Déterminer c pour que f soit une f.d.p.. Représenter graphiquement f .
     2) Soit X une v.a.r.a.c. ayant f pour f.d.p..
         a) Reconnaitre la loi de X .
         b) Déterminer FX , la f.r. de X .
         c) Calculer E(X) et V (X).

Solution.

Proposition 5.4 Soit X une v.a.r.a.c.. Soit a, b ∈ R tels que a < b. Alors :
                                X ∼ U([0, 1]) ⇐⇒ a + (b − a)X ∼ U([a, b])

et
                                                           X −a
                                  X ∼ U([a, b]) ⇐⇒              X ∼ U([0, 1])
                                                           b−a

Preuve.


5.2 Loi exponentielle
Dénition 5.5 Soit λ ∈ R∗+ . On dit qu'une v.a.r.a.c. X suit une loi exponentielle de paramètre λ,
si et seulement si, elle admet pour f.d.p.
                                         fX (x) = λe−λx I[0,+∞[ (x)

On note alors
                                                   X ∼ E(λ)

Modélisation. (a faire).
~~~

## Page 15

~~~text
v.a.r. continues                                                                                                 15


Exercice. Soit X ∼ E(λ). Vérier que fX est une f.d.p..

Solution.

Proposition 5.6 Si X ∼ E(λ), alors :
                                                 1                          1
                                     E(X) =              and V (X) =
                                                 λ                          λ2
Preuve.

Proposition 5.7 Si X ∼ E(λ), alors sa f.r. est donnée par
                                      FX (x) = (1 − e−λx )I[0,+∞[ (x)

i.e.                                             (
                                                     0            si x < 0
                                     FX (x) =
                                                     1−e   −λx
                                                                  si 0 ≤ x

Preuve.

       fX (x)                                                    FX (x)
         1.5                                                       1.5


             1                                                         1


            0.5                                                       0.5



       −1            1     2     3     4     5       x           −1               1     2     3     4    5   x

        −0.5                                                      −0.5

              Figure 4: f.d.p. de X ∼ E(1)                                  Figure 5: f.r. de X ∼ E(1)


Exercice. La durée de vie d'un atome d'un élément radioactif, représentée par X , est une v.a.r.a.c.
ayant pour f.d.p. la fonction fX dénie sur R par :
                                                 (
                                                     0            si t < 0
                                      fX (t) =
                                                     0.2e−0.2t    si 0 ≤ t
   1) Déterminer la loi de X et donner sa f.r. FX .
   2) Représenter graphiquement fX et FX .
   3) On mesure t en seconde.
        a) Calculer E(X) et V (X).
        b) Quelle est la probabilité pour qu'un atome ait une durée de vie supérieure à 4 secondes ?
        c) Quelle est la probabilité pour qu'un atome ait une durée de vie comprise entre 1 et 3
           secondes ?
~~~

## Page 16

~~~text
16                                                                                         K. El Amine




Solution.

Proposition 5.8 Soit X une v.a.r.a.c.. Soit λ ∈ R∗+ . alors :
                                                            1
                                      X ∼ E(1) ⇐⇒             X ∼ E(λ)
                                                            λ
et
                                      X ∼ E(λ) ⇐⇒ λX ∼ E(1)

Preuve.


5.3 Loi normale ou loi de Gauss
La distribution normale joue un rôle central dans la théorie des probabilités et les statistiques. Une
de ses premières applications était due à C.F. Gauss, qui l'utilisa en 1809 pour modéliser les erreurs
d'observation en astronomie.

5.3.1 Loi Normale
Dénition 5.9 Soit µ ∈ R et σ ∈ R∗+ . On dit qu'une v.a.r.a.c. X suit une loi normale (ou loi de
Gauss) de paramètres (µ, σ 2 ), si et seulement si, elle admet pour f.d.p.

                                                    1   1 x−µ 2
                                       fX (x) =    √ e− 2 ( σ )
                                                  σ 2π
On note alors
                                               X ∼ N (µ, σ 2 )

Remarque. Il n'existe pas d'expression analytique simple d'une primitive de la fonction x 7→ e−x .
                                                                                                    2


On admettra que                          Z +∞
                                                    1   2       √
                                                 e− 2 x dx =        2π
                                          −∞


Exercice. Soit X ∼ N (µ, σ2 ). Vérier que fX est une f.d.p.. Représenter graphiquement fX .

Solution.

Propriété 5.10 Si X ∼ N (µ, σ2 ), alors sa f.d.p. vérie les propriétés suivantes :
     1) fX est symétrique par rapport au point µ : fX (µ − x) = fX (µ + x), ∀x ∈ R.
     2) fX est maximale au point µ : fX (x) ≤ fX (µ), ∀x ∈ R.
     3)   lim fX (x) = lim fX (x) = 0.
          x→−∞         x→+∞


Preuve.

Proposition 5.11 Si X ∼ N (µ, σ2 ), sa f.r. est donnée par
                                         Z x
                                               1   1 t−µ 2
                              FX (x) =        √ e− 2 ( σ ) dt            ∀x ∈ R
                                          −∞ σ 2π

Preuve. C'est simplement la dénition d'une f.r..
~~~

## Page 17

~~~text
v.a.r. continues                                                                                   17


Remarque. Soit X ∼ N (µ, σ2 ).
Puisque fX est de classe C ∞ sur R, FX est aussi de classe C ∞ sur R et
                                          0
                                         FX (x) = fX (x) ∀x ∈ R

Proposition 5.12 Si X ∼ N (µ, σ2 ), alors
                                       E(X) = µ     et V (X) = σ 2

Preuve. Voir la sous-section sur la loi normale standard.
Proposition 5.13 (Transformation ane)
Soit a, b ∈ R avec a 6= 0. Alors
                        X ∼ N (µ, σ 2 ) =⇒ Y = aX + b ∼ N (aµ + b, (|a|σ)2 )

Preuve.

Corollaire 5.14 Soit X une v.a.r.a.c.. soit µ ∈ R et σ ∈ R∗+ . Alors :
                                                         X −µ
                              X ∼ N (µ, σ 2 ) ⇐⇒ X ∗ =        ∼ N (0, 1)
                                                           σ
et
                                   X ∼ N (0, 1) ⇐⇒ σX + µ ∼ N (µ, σ 2 )

Preuve.

Remarque. L'intérêt de ce résultat est de ramener tous les calculs sur les lois normales à des calculs
sur la loi normale standard (voir ci-après).

5.3.2 Loi normale Standard
Dénition 5.15 La loi normale N (µ, σ2 ) où µ = 0 et σ = 1 est appelée loi normale standard, et est
notée donc N (0, 1).
• La f.d.p. de la loi normale standard est souvent noté par la lettre grecque ϕ, i.e.
                                               1   1 2
                                       ϕ(x) = √ e− 2 x      ∀x ∈ R
                                               2π

• La f.r. de la loi normale standard est souvent noté par la lettre grecque Φ, i.e.
                                            Z x
                                    Φ(x) =       ϕ(t)dt ∀x ∈ R
                                               −∞


Proposition 5.16 Si X ∼ N (0, 1), alors :
                                        E(X) = 0    et V (X) = 1

Preuve.

Corollaire 5.17 Si X ∼ N (µ, σ2 ), alors
                                       E(X) = µ     et V (X) = σ 2

Preuve.
~~~

## Page 18

~~~text
18                                                                                          K. El Amine




Propriété 5.18 (f.d.p. de N (0, 1))
     1) ϕ est paire: ϕ(−x) = ϕ(x), ∀x ∈ R
     2) ϕ est maximale en 0.
     3)   lim ϕ(x) = lim ϕ(x) = 0
          x→−∞        x→+∞


Preuve.


Proposition 5.19 (f.r. de N (0, 1))
                                       Φ(−x) = 1 − Φ(x)   ∀x ∈ R

Preuve.


Exercice. Soit X ∼ N (0, 1). Montrer que −X ∼ N (0, 1).

Solution.

                          ϕ(x)                                             Φ(x)
                        0.5
                                                                           1
                        0.4                √1
                                            2π



                        0.3


                        0.2
                                       σ=1                               1/2


                        0.1



 −4              −2       0            2         4        −4       −2          0      2         4
                         µ=0                                                   x

            Figure 6: f.d.p. de X ∼ N (0, 1)                   Figure 7: f.r. de X ∼ N (0, 1)


5.3.3 Règle de 68-95-99%
Propriété 5.20 Si X ∼ N (µ, σ2 ) alors
• P ({µ − σ ≤ X ≤ µ + σ}) ≃ 0.68
• P ({µ − 2σ ≤ X ≤ µ + 2σ}) ≃ 0.95
• P ({µ − 3σ ≤ X ≤ µ + 3σ}) ≃ 0.99

Preuve.
~~~

## Page 19

~~~text
v.a.r. continues                                                                                            19


                                                             68.2%

                                                                95%



                     Fréquence
                                                             99.7%



                                 2.1%        13.6%        34.1%       34.1%          13.6%       2.1%

                           −3           −2           −1           0              1           2          3
                                                                Score
                                 Figure 8: Règle de 68-95-99% pour X ∼ N (0, 1)

5.3.4 Table de la loi normale standard
La f.r. Φ de la loi normale standard N (0, 1) est
                                                      Z x
                                                              1   1 2
                                             Φ(x) =          √ e− 2 t dt ∀xR
                                                          −∞  2π
Comme il n'existe pas d'expression analytique simple pour la fonction de distribution Φ autre que sa
formulation intégrale, les valeurs de la fonction Φ pour x entre 0 et 4, par incréments de 0.01, sont
rassemblées dans une table appelée table de la loi normale standard (cf n de ce document).

Valeurs pour la loi normale standard :
• Cas 0 ≤ x ≤ 4.
La valeur de Φ(x) est lu sur la table à l'intersection de la ligne et de la colonne dont la somme vaut x.
Par exemple, Φ(1.37) = 0.914657
• Cas −4 ≤ x ≤ 0.
On utilise la relation Φ(−x) = 1 − Φ(x).
Par exemple, Φ(−1.37) = 1 − Φ(1.37) = 0, 085343
• Approximation de Φ(x). Dans certains calculs très précis, on a besoin des valeurs de Φ(x) pour
x > 4. La formule suivante donne une très bonne approximation :
                                                                      1 − 1 x2
                                                 Φ(x) ≃ 1 −             e 2
                                                                      x
Par exemple, Φ(5) = 1 − 7.45 × 10−7 = 0.999999255.

Valeurs pour une loi normale non-standard :
Par transformation ane, on peut toujours se ramener à loi loi normale standard.
Proposition 5.21 Si X ∼ N (µ, σ2 ), alors sa f.r. FX satisfait la relation
                                                                       
                                                                x−µ
                                             FX (x) = Φ                     ∀x ∈ R
                                                                 σ

Preuve.

Remarque. Cette relation permet de ramener tous les calculs sur les loi normales aux calculs sur la
loi normale standard.
~~~

## Page 20

~~~text
20                                                                                                 K. El Amine




Exemple. Soit X ∼ N (µ, σ2 ) = N (6, 22 ). Calculer FX (3).

Solution. On a
                                                    
                              3−µ                3−6
             FX (3) = Φ                 =Φ                 = Φ(−1.5) = 1 − Φ(1.5) ≃ 1 − 0.933193
                               σ                  2
                   ≃ 0, 066807
~~~

## Page 21

~~~text
                                                                                     Rz       t2
Fonction de répartition de Z ⇠ N(0, 1):                          (z) = p12⇡              e    2   dt
                                                                                     1
      z        0.00     0.01     0.02     0.03     0.04     0.05     0.06     0.07     0.08     0.09
    0.00   0.500000 0.503989 0.507978 0.511966 0.515953 0.519939 0.523922 0.527903 0.531881 0.535856
    0.10   0.539828 0.543795 0.547758 0.551717 0.555670 0.559618 0.563559 0.567495 0.571424 0.575345
    0.20   0.579260 0.583166 0.587064 0.590954 0.594835 0.598706 0.602568 0.606420 0.610261 0.614092
    0.30   0.617911 0.621720 0.625516 0.629300 0.633072 0.636831 0.640576 0.644309 0.648027 0.651732
    0.40   0.655422 0.659097 0.662757 0.666402 0.670031 0.673645 0.677242 0.680822 0.684386 0.687933
    0.50   0.691462 0.694974 0.698468 0.701944 0.705401 0.708840 0.712260 0.715661 0.719043 0.722405
    0.60   0.725747 0.729069 0.732371 0.735653 0.738914 0.742154 0.745373 0.748571 0.751748 0.754903
    0.70   0.758036 0.761148 0.764238 0.767305 0.770350 0.773373 0.776373 0.779350 0.782305 0.785236
    0.80   0.788145 0.791030 0.793892 0.796731 0.799546 0.802337 0.805105 0.807850 0.810570 0.813267
    0.90   0.815940 0.818589 0.821214 0.823814 0.826391 0.828944 0.831472 0.833977 0.836457 0.838913
    1.00   0.841345 0.843752 0.846136 0.848495 0.850830 0.853141 0.855428 0.857690 0.859929 0.862143
    1.10   0.864334 0.866500 0.868643 0.870762 0.872857 0.874928 0.876976 0.879000 0.881000 0.882977
    1.20   0.884930 0.886861 0.888768 0.890651 0.892512 0.894350 0.896165 0.897958 0.899727 0.901475
    1.30   0.903200 0.904902 0.906582 0.908241 0.909877 0.911492 0.913085 0.914657 0.916207 0.917736
    1.40   0.919243 0.920730 0.922196 0.923641 0.925066 0.926471 0.927855 0.929219 0.930563 0.931888
    1.50   0.933193 0.934478 0.935745 0.936992 0.938220 0.939429 0.940620 0.941792 0.942947 0.944083
    1.60   0.945201 0.946301 0.947384 0.948449 0.949497 0.950529 0.951543 0.952540 0.953521 0.954486
    1.70   0.955435 0.956367 0.957284 0.958185 0.959070 0.959941 0.960796 0.961636 0.962462 0.963273
    1.80   0.964070 0.964852 0.965620 0.966375 0.967116 0.967843 0.968557 0.969258 0.969946 0.970621
    1.90   0.971283 0.971933 0.972571 0.973197 0.973810 0.974412 0.975002 0.975581 0.976148 0.976705
    2.00   0.977250 0.977784 0.978308 0.978822 0.979325 0.979818 0.980301 0.980774 0.981237 0.981691
    2.10   0.982136 0.982571 0.982997 0.983414 0.983823 0.984222 0.984614 0.984997 0.985371 0.985738
    2.20   0.986097 0.986447 0.986791 0.987126 0.987455 0.987776 0.988089 0.988396 0.988696 0.988989
    2.30   0.989276 0.989556 0.989830 0.990097 0.990358 0.990613 0.990863 0.991106 0.991344 0.991576
    2.40   0.991802 0.992024 0.992240 0.992451 0.992656 0.992857 0.993053 0.993244 0.993431 0.993613
    2.50   0.993790 0.993963 0.994132 0.994297 0.994457 0.994614 0.994766 0.994915 0.995060 0.995201
    2.60   0.995339 0.995473 0.995604 0.995731 0.995855 0.995975 0.996093 0.996207 0.996319 0.996427
    2.70   0.996533 0.996636 0.996736 0.996833 0.996928 0.997020 0.997110 0.997197 0.997282 0.997365
    2.80   0.997445 0.997523 0.997599 0.997673 0.997744 0.997814 0.997882 0.997948 0.998012 0.998074
    2.90   0.998134 0.998193 0.998250 0.998305 0.998359 0.998411 0.998462 0.998511 0.998559 0.998605
    3.00   0.998650 0.998694 0.998736 0.998777 0.998817 0.998856 0.998893 0.998930 0.998965 0.998999
    3.10   0.999032 0.999065 0.999096 0.999126 0.999155 0.999184 0.999211 0.999238 0.999264 0.999289
    3.20   0.999313 0.999336 0.999359 0.999381 0.999402 0.999423 0.999443 0.999462 0.999481 0.999499
    3.30   0.999517 0.999534 0.999550 0.999566 0.999581 0.999596 0.999610 0.999624 0.999638 0.999651
    3.40   0.999663 0.999675 0.999687 0.999698 0.999709 0.999720 0.999730 0.999740 0.999749 0.999758
    3.50   0.999767 0.999776 0.999784 0.999792 0.999800 0.999807 0.999815 0.999822 0.999828 0.999835
    3.60   0.999841 0.999847 0.999853 0.999858 0.999864 0.999869 0.999874 0.999879 0.999883 0.999888
    3.70   0.999892 0.999896 0.999900 0.999904 0.999908 0.999912 0.999915 0.999918 0.999922 0.999925
    3.80   0.999928 0.999931 0.999933 0.999936 0.999938 0.999941 0.999943 0.999946 0.999948 0.999950
    3.90   0.999952 0.999954 0.999956 0.999958 0.999959 0.999961 0.999963 0.999964 0.999966 0.999967
    4.00   0.999968 0.999970 0.999971 0.999972 0.999973 0.999974 0.999975 0.999976 0.999977 0.999978



Quantile z↵ défini par P (Z > z↵ ) = ↵ avec Z ⇠ N(0, 1)
α              0.25      0.1     0.05     0.025    0.01     0.005    0.001  0.0005
z_α        0.674490 1.281552 1.644854 1.959964 2.326348 2.575829 3.090232 3.290527
z_α/2      1.150349 1.644854 1.959964 2.241403 2.575829 2.807034 3.290527 3.480756
~~~
