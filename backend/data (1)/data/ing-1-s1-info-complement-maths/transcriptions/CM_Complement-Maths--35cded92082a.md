# CM_Complement-Maths.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1kSDPjwlEB5KM600EZr_rR5doEW5rUris) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                  Compléments de Mathématiques
                                          Sam P.


Table des matières
1 Séries numériques                                                                         3
  1.1 Généralités et définitions fondamentales . . . . . . . . . . . . . . . . . . . .      3
  1.2 Structure algébrique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      4
  1.3 Condition nécessaire de convergence . . . . . . . . . . . . . . . . . . . . . .       4
  1.4 Séries de référence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     5
  1.5 Séries à termes positifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    5
  1.6 Séries alternées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    6
  1.7 Séries à termes quelconques . . . . . . . . . . . . . . . . . . . . . . . . . .       6

2 Intégrales                                                                                 7
  2.1 Fonctions en escalier et intégrale . . . . . . . . . . . . . . . . . . . . . . . .     8
  2.2 Fonctions continues par morceaux . . . . . . . . . . . . . . . . . . . . . . .         9
  2.3 Sommes de Riemann . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          9
  2.4 Primitives et intégrale définie . . . . . . . . . . . . . . . . . . . . . . . . .     10
  2.5 Méthodes de calcul . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      10
  2.6 Intégrales généralisées . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     10
  2.7 Intégrales usuelles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   11

3 Formes bilinéaires, espaces euclidiens et endomorphismes remarquables 11
  3.1 Formes bilinéaires . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
  3.2 Matrice associée à une forme bilinéaire . . . . . . . . . . . . . . . . . . . . 12
  3.3 Formes quadratiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
  3.4 Positivité des formes quadratiques . . . . . . . . . . . . . . . . . . . . . . . 13
  3.5 Diagonalisation des formes quadratiques . . . . . . . . . . . . . . . . . . . 14
  3.6 Applications géométriques . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
  3.7 Produit scalaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
  3.8 Inégalités fondamentales . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
  3.9 Espaces euclidiens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
  3.10 Bases orthonormées . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
  3.11 Projecteurs orthogonaux . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

                                              1
~~~

## Page 2

~~~text
3.12 Symétries orthogonales . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     16
3.13 Endomorphismes symétriques . . . . . . . . . . . . . . . . . . . . . . . . .         17
3.14 Théorème spectral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      17
3.15 Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   17




                                        Sam P.                                             2
~~~

## Page 3

~~~text
1     Séries numériques
1.1    Généralités et définitions fondamentales
Définition. Soit (un ) une suite à valeurs dans R ou dans C. La série numérique de
terme général un est la somme formelle :

                                          u0 + u1 + u2 + . . .

que l’on note :
                                                 +∞
                                                 X
                                                        un .
                                                 n=0

    Si la suite commence à l’indice n0 , on écrit :

                                                 +∞
                                                 X
                                                        un .
                                                 n=n0


Exemple.
                                                               +∞
                                                               X
                                      u1 + u 2 + · · · =             un .
                                                               n=1


Définition (Sommes partielles). Pour tout N ∈ N, la somme partielle d’ordre N
est :
                            XN
                      SN =      un = u0 + u1 + · · · + uN .
                                       n=0
                                                                                 P
La suite (SN ) est appelée suite des sommes partielles de la série                   un .

Exemple.
             +∞
             X  1
    — Pour              , il est difficile de calculer toutes les sommes partielles. Par exemple :
             n=1
                   n2

                                             1    1   1    1 1
                                     S3 =     2
                                                + 2 + 2 =1+ + .
                                             1   2   3     4 9
             +∞
             X
    — Pour         2n , il s’agit d’une série géométrique de raison q = 2, donc :
             n=0

                                          N
                                          X             1 − 2N +1
                                   SN =         2n =              = 2N +1 − 1.
                                          n=0
                                                          1−2




                                                 Sam P.                                          3
~~~

## Page 4

~~~text
                                                         P
Définition (Convergence et divergence). La série            un est dite convergente si la
suite de ses sommes partielles (SN ) converge. Dans ce cas, on définit :

                                                  +∞
                                                  X
                                       lim SN =         un .
                                    N →+∞
                                                  n=0


Sinon, la série est dite divergente.

                  +∞
                  X
Exemple. Pour           2n , on a SN = 2N +1 −1 et limN →+∞ SN = +∞, donc la série diverge.
                  n=0

                                                P
Définition (Reste d’une série convergente). Si      un converge vers S, on définit
pour tout N :
                                          +∞
                                          X
                           RN = S − SN =       un .
                                                     n=N +1


1.2    Structure algébrique
          P       P
   Soient   un et   v deux séries numériques et λ ∈ R.
                  Xn
   — Addition :      (un + vn ).
                                         X         X
   — Multiplication par un scalaire : λ      un =     (λun ).
                              X  X  X
                                                    wn où wn = nk=0 uk vn−k .
                                                              P
   — Produit de Cauchy :          un      vn =

                         P         P
Remarque. Si les séries      un et   vn convergent :
     P
  1.   (un + vn ) converge ;
     P
  2.   (λun ) converge ;
                                                               P
    3. Si au moins une des deux converge absolument, alors         wn converge.


1.3    Condition nécessaire de convergence
                 X
Théorème. Si         un converge, alors limn→+∞ un = 0.

Corollaire. Si lim un ̸= 0, alors la série diverge (divergence grossière). La réciproque
                 n→+∞                                P
est fausse : un → 0 n’implique pas la convergence de   un .




                                            Sam P.                                       4
~~~

## Page 5

~~~text
1.4   Séries de référence
                                             +∞
                                             X
Série géométrique. Soit q ∈ R. La série            qn :
                                             n=0

                                 
                                 converge si |q| < 1,
                                 diverge si |q| ≥ 1.

                                             +∞
                                             X  1
Série de Riemann. Soit γ ∈ R. La série                  :
                                             n=1
                                                   nγ
                                  
                                  converge si γ > 1,
                                  diverge si γ ≤ 1.


1.5   Séries à termes positifs
                        X
Définition. Une série       un est positive si un ≥ 0 pour tout n.

Propriété. Pour une série positive, la suite (SN ) est croissante. Elle converge si et
seulement si elle est majorée.

Critères de convergence

                                 un une série à termes positifs et l = limn→+∞ uun+1
                             P
Critère d’Alembert. Soit                                                          n
                                                                                     . Alors :
                            
                            
                            
                             l < 1 ⇒ la série converge,
                            
                              l > 1 ⇒ la série diverge,
                            
                            
                            l = 1 ⇒ pas de conclusion.
                            

                            P                                                 √
Critère de Cauchy. Soit         un une série à termes positifs et l = limn→+∞ n un . Alors :
                            
                            
                            
                             l < 1 ⇒ la série converge,
                            
                              l > 1 ⇒ la série diverge,
                            
                            
                            l = 1 ⇒ pas de conclusion.
                            


Critères de comparaison




                                          Sam P.                                            5
~~~

## Page 6

~~~text
Suites équivalentes. Deux suites (un ) et (vn ) non nulles à partir d’un certain rang
sont dites équivalentes, noté un ∼ vn , si :

                                             un
                                         lim    = 1.
                                        n→+∞ vn


Équivalences utiles. Si limn→+∞ un = 0, alors :

               sin(un ) ∼ un ,    cos(un ) ∼ 1,      ln(1 + un ) ∼ un ,   eun ∼ 1.

Tout polynôme en n est équivalent à son monôme de plus haut degré.

Comparaison par inégalité. Si 0 ≤ un ≤ vn à partir d’un certain rang :
                           X                         X
                                 vn converge ⇒           un converge,
                             X                       X
                                  un diverge ⇒           vn diverge.

                                                                           P            P
Comparaison par équivalence. Si un ∼ vn , alors les séries                      un et       vn sont de
même nature (convergentes ou divergentes).


1.6    Séries alternées
                                      X
                                          (−1)n un ou       (−1)n+1 un , avec un ≥ 0, est appelée
                                                           P
Définition. Une série de la forme
série alternée.
                                                                                            X
Critère de Leibniz. Si (un ) est décroissante et limn→+∞ un = 0, alors la série              (−1)n un
converge.

                                               +∞
                                               X  (−1)n
Exemple. La série harmonique alternée                        converge par le critère de Leibniz.
                                               n=1
                                                       n

1.7    Séries à termes quelconques
Convergence absolue et semi-convergence

                       P                                  P
Définition. La série     un est absolument convergente si   |un | converge. Toute
série absolument convergente est convergente.

             +∞
             X  (−1)n                                              P+∞ 1
Exemple.                converge (critère de Leibniz) mais             n=1 n   diverge, donc elle est
             n=1
                n
semi-convergente.


                                            Sam P.                                                  6
~~~

## Page 7

~~~text
Critères usuels de convergence absolue

                                                                   un+1
Critère d’Alembert (valeurs absolues). Si lim                           = l, alors :
                                                          n→+∞      un
                                  
                                  
                                  
                                   l < 1 ⇒ convergence absolue,
                                  
                                    l > 1 ⇒ divergence grossière,
                                  
                                  
                                  l = 1 ⇒ pas de conclusion.
                                  

                                                                 p
                                                                 n
Critère de Cauchy (valeurs absolues). Si lim                       |un | = l, alors :
                                                          n→+∞

                                  
                                  
                                  
                                   l < 1 ⇒ convergence absolue,
                                  
                                    l > 1 ⇒ divergence grossière,
                                  
                                  
                                  l = 1 ⇒ pas de conclusion.
                                  


Théorèmes spécifiques

Théorème spécial des séries alternées (TSSA). Si (|un |) est décroissante et tend
              P
vers 0, alors   un converge.

                                                  +∞
                                                  X  (−1)n
Série de Riemann alternée. La série                           converge si et seulement si λ > 0.
                                                   n=1
                                                         nλ

Série de Bertrand. Pour α, β ∈ R :
                                                              
             +∞                                               α > 1, pour tout β,
             X         1
                                converge si et seulement si
             n=2
                   nα (ln n)β                                 ou α = 1 et β > 1.


Sommes télescopiques. Si vn = un+1 − un , alors :
                                  X
                                      vn converge ⇔ (un ) converge,

et
                                      +∞
                                      X
                                             vn = lim (un − u0 ).
                                                  n→+∞
                                       n=0


2      Intégrales
     Dans tout ce chapitre, on fixe deux réels a, b ∈ R tels que a < b.



                                                 Sam P.                                            7
~~~

## Page 8

~~~text
2.1    Fonctions en escalier et intégrale
Définition (Subdivision). Soit n ∈ N∗ . On appelle subdivision du segment [a, b]
toute famille ordonnée
                              σ = (x0 , x1 , . . . , xn )

telle que
                                      a = x0 < x1 < · · · < xn = b.

On note S(a, b) l’ensemble des subdivisions de [a, b].

Exemple. La famille (0, 21 , 1) est une subdivision du segment [0, 1].

Définition (Subdivision régulière). On appelle subdivision régulière de rang n
du segment [a, b] la subdivision définie par

                                                 b−a
                                    xk = a + k       ,       k = 0, . . . , n.
                                                  n

Définition (Fonction en escalier). Une fonction φ : [a, b] → R est dite en escalier
s’il existe une subdivision σ = (x0 , . . . , xn ) de [a, b] et des réels c0 , . . . , cn−1 tels que

                     ∀k ∈ {0, . . . , n − 1},         ∀x ∈]xk , xk+1 [,     φ(x) = ck .

   On note E([a, b]) l’ensemble des fonctions en escalier sur [a, b].

Définition (Intégrale d’une fonction en escalier). Soit φ ∈ E([a, b]) associée à une
subdivision σ = (x0 , . . . , xn ). On appelle intégrale de φ sur [a, b] la quantité
                                    Z b               n−1
                                                      X
                                          φ(x) dx =         ck (xk+1 − xk ).
                                     a                k=0


Propriétés fondamentales. Soient φ, ψ ∈ E([a, b]) et λ ∈ R.
     Z b             Z b    Z b
  —       (φ + ψ) =      φ+     ψ
     Za b         Z b a      a

  —       λφ = λ      φ
       a           a Z
                         b
  — Si φ ≥ 0, alors        φ≥0
                          a


Relation de Chasles. Pour tout c ∈ [a, b] :
                              Z b               Z c                Z b
                                    φ(x) dx =         φ(x) dx +          φ(x) dx.
                               a                 a                   c




                                                  Sam P.                                          8
~~~

## Page 9

~~~text
2.2    Fonctions continues par morceaux
Définition. Une fonction f : [a, b] → R est dite continue par morceaux s’il existe
une subdivision σ = (x0 , . . . , xn ) telle que :
   — f est continue sur chaque intervalle ]xk , xk+1 [,
   — f admet des limites réelles à droite et à gauche en chaque xk .
              0
   On note Cpm  ([a, b]) l’ensemble des fonctions continues par morceaux sur [a, b].

Remarques.
  — Toute fonction continue est continue par morceaux :

                                         C 0 ([a, b]) ⊂ Cpm
                                                         0
                                                            ([a, b]).

   — Toute fonction en escalier est continue par morceaux :

                                                      0
                                         E([a, b]) ⊂ Cpm ([a, b]).

                                   0
Intégrabilité. Toute fonction f ∈ Cpm ([a, b]) est intégrable sur [a, b].

                    0
Positivité. Si f ∈ Cpm ([a, b]) et f (x) ≥ 0 sur [a, b], alors
                                         Z b
                                               f (x) dx ≥ 0.
                                          a


La réciproque est fausse.

                                                           0
Inégalité de Cauchy–Schwarz. Pour toutes fonctions f, g ∈ Cpm ([a, b]) :

                  Z b                    Z b             1/2 Z b         1/2
                                                      2                 2
                        f (x)g(x) dx ≤            f (x) dx          g(x) dx      .
                   a                          a                   a


Nullité de l’intégrale. Si f est continue, positive sur [a, b] et
                                         Z b
                                               f (x) dx = 0,
                                          a


alors f est identiquement nulle.


2.3    Sommes de Riemann
                       0
Proposition. Soit f ∈ Cpm ([a, b]). Alors :

                                    n                  Z b
                             b−aX                  b−a
                         lim        f          a+k      =    f (x) dx.
                        n→+∞  n k=1                 n     a


                                                  Sam P.                             9
~~~

## Page 10

~~~text
2.4    Primitives et intégrale définie
Définition (Primitive). Soit I un intervalle de R et f : I → R continue. Une fonction
F : I → R est une primitive de f si

                                         F ′ (x) = f (x),           ∀x ∈ I.

Théorème. Toute fonction continue sur un intervalle admet des primitives.

Définition (Intégrale définie). Si f est continue sur [a, b] et F une primitive de f ,
on définit                  Z                b
                                                 f (x) dx = F (b) − F (a).
                                         a


Théorème fondamental de l’analyse. Si f est continue sur [a, b] et
                                                           Z x
                                                 F (x) =         f (t) dt,
                                                            a


alors F est une primitive de f sur [a, b].


2.5    Méthodes de calcul
Intégration par parties

Proposition. Si f, g ∈ C 1 ([a, b]), alors :
                     Z b                                                Z b
                           f (x)g(x) dx = [f (x)g(x)]ba −
                            ′
                                                                                 f (x)g ′ (x) dx.
                      a                                                      a


Changement de variable

Proposition. Soit φ ∈ C 1 ([a, b]) strictement monotone et f continue sur φ([a, b]). Alors :
                                Z φ(b)                     Z b
                                         f (u) du =              f (φ(x))φ′ (x) dx.
                                 φ(a)                       a


2.6    Intégrales généralisées
Définition. Une intégrale est dite généralisée si :
  — l’intervalle est infini ;
  — ou la fonction n’est pas bornée.

Convergence. Une intégrale généralisée converge si la limite définissant l’intégrale
existe et est finie.

                                                       Sam P.                                       10
~~~

## Page 11

~~~text
Convergence absolue. Si                     Z b
                                                  |f (x)| dx
                                             a

converge, alors                             Z b
                                                  f (x) dx
                                              a
converge.


2.7    Intégrales usuelles
Intégrales de Riemann. Soit α ∈ R :
             Z 1                                     Z +∞
                    1                                           1
                      dx converge ssi α < 1,                      dx converge ssi α > 1.
               0   xα                                 1        xα

Exponentielle.                Z +∞
                                     e−αx dx converge ssi α > 0.
                                 0


Critère de comparaison. Soient f, g continues, positives sur [a, b[, avec f ≤ g.
        R                 R
   — Si g converge, alors f converge.
        R               R
   — Si f diverge, alors g diverge.

Théorème d’équivalence. Si f (x) ∼ g(x) au voisinage d’un point singulier, alors
                             Z          Z
                                 f et       g sont de même nature.


3     Formes bilinéaires, espaces euclidiens et endomor-
      phismes remarquables
    Dans tout ce chapitre, E désigne un espace vectoriel réel de dimension finie n.


3.1    Formes bilinéaires
Définition. Une application
                                        φ : E × E −→ R

est appelée forme bilinéaire si elle est linéaire par rapport à chacune de ses variables,
c’est-à-dire :
                                      
                                      φ(x + y, z) = φ(x, z) + φ(y, z),
               ∀x, y, z ∈ E, ∀λ ∈ R,
                                      φ(λx, z) = λφ(x, z),


                                                 Sam P.                                    11
~~~

## Page 12

~~~text
et de même pour la seconde variable.

Exemples.
  — Dans Rn , l’application (x, y) 7→ x⊤ y est une forme bilinéaire.
  — L’application (x, y) 7→ 0 est une forme bilinéaire.
  — L’application (x, y) 7→ ∥x∥ ∥y∥ n’est pas bilinéaire.

Définition (Forme symétrique). Une forme bilinéaire φ est dite symétrique si :

                              ∀x, y ∈ E,    φ(x, y) = φ(y, x).

Définition (Forme antisymétrique). Une forme bilinéaire φ est dite antisymé-
trique si :
                       ∀x, y ∈ E, φ(x, y) = −φ(y, x).

Propriété. Si φ est antisymétrique, alors :

                                  ∀x ∈ E,    φ(x, x) = 0.

Réciproque. La réciproque est fausse en général.


3.2    Matrice associée à une forme bilinéaire
Définition. Soit B = (e1 , . . . , en ) une base de E et φ une forme bilinéaire. On appelle
matrice associée à φ dans la base B la matrice
                                                   
                               MB (φ) = φ(ei , ej ) 1≤i,j≤n .

Expression matricielle. Si x, y ∈ E ont pour coordonnées X, Y ∈ Rn dans la base B,
alors :
                              φ(x, y) = X ⊤ MB (φ)Y.

Changement de base. Si P est la matrice de passage d’une base B à une base B′ ,
alors :
                         MB′ (φ) = P ⊤ MB (φ)P.

Symétrie matricielle.

                        φ est symétrique ⇐⇒ MB (φ)⊤ = MB (φ).




                                           Sam P.                                       12
~~~

## Page 13

~~~text
3.3   Formes quadratiques
Définition. Une application q : E → R est appelée forme quadratique s’il existe une
forme bilinéaire symétrique φ telle que :

                               ∀x ∈ E,     q(x) = φ(x, x).

Remarque fondamentale. Une forme quadratique ne détermine pas une unique forme
bilinéaire, mais elle détermine une unique forme bilinéaire symétrique associée.

Polarisation. La forme bilinéaire symétrique associée à q est donnée par :

                                      1                       
                          φ(x, y) =     q(x + y) − q(x) − q(y) .
                                      2

Expression matricielle. Dans une base B :

                                      q(x) = X ⊤ AX,

où A est une matrice symétrique réelle.

Exemple. Dans R2 :
                                                                  !
                                                              1 1
                    q(x, y) = x2 + 2xy + 3y 2    ⇐⇒     A=          .
                                                              1 3

3.4   Positivité des formes quadratiques
Définition. Une forme quadratique q est dite :
  — positive si ∀x, q(x) ≥ 0,
  — définie positive si ∀x ̸= 0, q(x) > 0,
  — négative si ∀x, q(x) ≤ 0,
  — indéfinie sinon.

Lien matriciel. q est définie positive si et seulement si sa matrice associée est symé-
trique définie positive.

Critère de Sylvester. Une matrice symétrique réelle est définie positive si et seulement
si tous ses mineurs principaux sont strictement positifs.




                                          Sam P.                                     13
~~~

## Page 14

~~~text
3.5   Diagonalisation des formes quadratiques
Théorème (Réduction de Gauss). Toute forme quadratique réelle peut être mise
sous forme diagonale dans une base convenable :

                               q(x) = λ1 x21 + · · · + λn x2n .

Signature. Le nombre de coefficients strictement positifs et strictement négatifs est
invariant par changement de base.

Théorème d’inertie de Sylvester. La signature (p, q) d’une forme quadratique réelle
est indépendante de la base choisie.

Cas particulier. Une forme quadratique est définie positive si et seulement si tous les
coefficients diagonaux sont strictement positifs.


3.6   Applications géométriques
Classification des coniques. Les formes quadratiques permettent de classifier les co-
niques selon leur signature :
   — ellipse,
   — hyperbole,
   — parabole (cas dégénéré).

Exemple.
                   x2 + y 2 = 1 ellipse,       x2 − y 2 = 1 hyperbole.


3.7   Produit scalaire
Définition. Un produit scalaire sur E est une forme bilinéaire symétrique ⟨·, ·⟩ :
E × E → R telle que :
   — ∀x ∈ E, ⟨x, x⟩ ≥ 0,
   — ⟨x, x⟩ = 0 ⇐⇒ x = 0.

Exemples.
  — Dans Rn :                                       n
                                                    X
                                        ⟨x, y⟩ =          xi y i .
                                                    i=1

   — Pour une matrice symétrique définie positive A :

                                         ⟨x, y⟩A = x⊤ Ay.


                                           Sam P.                                   14
~~~

## Page 15

~~~text
Norme associée. On définit :
                                              p
                                      ∥x∥ =    ⟨x, x⟩.


3.8    Inégalités fondamentales
Inégalité de Cauchy–Schwarz. Pour tous x, y ∈ E :

                                    |⟨x, y⟩| ≤ ∥x∥ ∥y∥.

Démonstration. Considérer la fonction t 7→ ⟨x + ty, x + ty⟩ et utiliser sa positivité.

Inégalité triangulaire.
                                  ∥x + y∥ ≤ ∥x∥ + ∥y∥.

Distance. La distance associée est :

                                    d(x, y) = ∥x − y∥.


3.9    Espaces euclidiens
Définition. Un espace vectoriel réel de dimension finie muni d’un produit scalaire est
appelé espace euclidien.

Orthogonalité. Deux vecteurs x, y sont orthogonaux si :

                                         ⟨x, y⟩ = 0.

Orthogonal d’un sous-espace. Pour un sous-espace F ⊂ E :

                           F ⊥ = {x ∈ E | ∀y ∈ F, ⟨x, y⟩ = 0}.

Propriétés.

                F ⊥ est un sous-espace de E,      dim F + dim F ⊥ = dim E.


3.10    Bases orthonormées
Définition. Une base (e1 , . . . , en ) est dite orthonormée si :
                                               
                                               1 si i = j,
                                  ⟨ei , ej ⟩ =
                                               0 si i ̸= j.

                                           Sam P.                                        15
~~~

## Page 16

~~~text
Coordonnées. Dans une base orthonormée :
                                     n
                                     X                        n
                                                              X
                                                        2
                          ⟨x, y⟩ =         xi y i ,   ∥x∥ =         x2i .
                                     i=1                      i=1


Théorème de Gram–Schmidt. Toute base d’un espace euclidien peut être transfor-
mée en une base orthonormée.


3.11    Projecteurs orthogonaux
Définition (Projecteur). Un endomorphisme p : E → E est un projecteur si :

                                             p2 = p.

Définition (Projecteur orthogonal). Un projecteur p est dit orthogonal s’il est sy-
métrique :
                             ⟨p(x), y⟩ = ⟨x, p(y)⟩.

Décomposition orthogonale. Pour tout sous-espace F :

                                      E = F ⊕ F ⊥.

Projection orthogonale. Pour tout x ∈ E, il existe un unique pF (x) ∈ F tel que :

                     x = pF (x) + (x − pF (x)),         x − pF (x) ∈ F ⊥ .

Distance à un sous-espace.

                                d(x, F ) = ∥x − pF (x)∥.


3.12    Symétries orthogonales
Définition. Une symétrie est un endomorphisme s tel que :

                                            s2 = Id.

Symétrie orthogonale. La symétrie orthogonale par rapport à F est :

                                 sF (x) = 2pF (x) − x.




                                            Sam P.                                  16
~~~

## Page 17

~~~text
3.13    Endomorphismes symétriques
Définition. Un endomorphisme u : E → E est dit symétrique si :

                           ∀x, y ∈ E,    ⟨u(x), y⟩ = ⟨x, u(y)⟩.

Lien matriciel. Dans une base orthonormée, la matrice de u est symétrique.

Propriété spectrale. Toutes les valeurs propres d’un endomorphisme symétrique sont
réelles.

Orthogonalité des sous-espaces propres. Deux sous-espaces propres associés à des
valeurs propres distinctes sont orthogonaux.


3.14    Théorème spectral
Théorème spectral réel. Tout endomorphisme symétrique d’un espace euclidien :
  — est diagonalisable,
  — admet une base orthonormée de vecteurs propres.

Conséquence matricielle. Toute matrice symétrique réelle est diagonalisable par une
matrice orthogonale.


3.15    Applications
Moindres carrés. Le problème

                                        min ∥x − y∥
                                        y∈F


admet une solution unique : la projection orthogonale de x sur F .

Interprétation géométrique. La projection orthogonale est le meilleur approximant
de x dans F au sens de la norme euclidienne.




                                          Sam P.                                17
~~~
