# FICHE DE REVSION PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1YvfkTDpgev58BEDLxBg7Ts7X1RIyKkrm) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                         FICHE DE RÉVISION
                                                      Probabilités
                                            ING1 - Génie Mathématique




TD1 - PROBABILITÉS ET INDÉPENDANCE


 Propriétés de base
 1. Sous-additivité :                                     n
                                                                     !           n
                                                          [                      X
                                                  P             Ai       ≤             P (Ai )
                                                          i=1                    i=1

 2. Identité de Poincaré :
                   n
                              !
                   [                  X                   X                                  X
               P         Ai       =       P (Ai ) −             P (Ai ∩ Aj ) +                   P (Ai ∩ Aj ∩ Ak ) − · · ·
                   i=1                                    i<j                            i<j<k


 Inégalités de Bonferroni
                                           n                  n
                                                      !
                                           [                  X                        X
                                      P          Ai       ≥         P (Ai ) −                P (Ai ∩ Aj )
                                           i=1                i=1                      i<j


 Indépendance
 Événements : A et B indépendants si P (A ∩ B) = P (A)P (B)
 Variables : X et Y indépendantes si :
                         P (X ∈ A, Y ∈ B) = P (X ∈ A)P (Y ∈ B)                                   pour tous A, B
  ATTENTION
 Indépendance 2 à 2 ̸= Indépendance mutuelle
 Exemple : X, Y indépendantes, Z = XY . Alors X, Y, Z sont 2 à 2 indépendantes MAIS PAS mutuel-
 lement indépendantes.
 Formule de Bayes
                                                                      P (B|A)P (A)
                                                  P (A|B) =
                                                                          P (B)
 Formule des probabilités totales :
                                                                n
                                                                X
                                                 P (B) =              P (B|Ai )P (Ai )
                                                                i=1

 où (A ) est une partition de Ω.
      i


  ASTUCE
 Pour montrer l'indépendance :
   1. Calculer P (X ∩ Y ) et vérier si = P (X)P (Y )
   2. Pour des v.a. : vérier si f (x, y) = f (x)f (y)
                                          X,Y                   X            Y




                                                                         1
~~~

## Page 2

~~~text
     3. Pour des v.a. gaussiennes : vérier si Cov(X, Y ) = 0

TD2 - ESPÉRANCE ET VARIANCE


 Formules Fondamentales
 Variance :
                               Var(X) = E[X ] − E[X]                2             2


 Conséquence : E[X] ≤ E[X ] (Cauchy-Schwarz)
                         2         2

 Pour X ∈ N :                                                ∞
                                                             X
                                                  E[X] =           P (X > n)
                                                             n=0
                                                       ∞
                                                       X
                                           E[X 2 ] =         (2k + 1)P (X > k)
                                                       k=0


 * Inégalités Importantes
 1. Inégalité de Markov :
                                                                        E[|X|]
                                                   P (|X| ≥ a) ≤
                                                                          a
 Généralisation : Pour g croissante :
                                                                    E[g(|X|)]
                                                 P (|X| ≥ a) ≤
                                                                      g(a)

 2. Inégalité de Bienaymé-Tchebychev :

                                               P (|X − E[X]| ≥ ε) ≤
                                                                           Var(X)
                                                                                 ε2

 Lois Discrètes Classiques
  Bernoulli B(p) : P (X = 1) = p E[X] = p ,            , Var(X) = p(1 − p)
  Binomiale B(n, p) :                                  
                                                        n k
                                           P (X = k) =     p (1 − p)n−k
                                                        k
        , Var(X) = np(1 − p)
 E[X] = np
  Géométrique G(p) : P (X = k) = p(1 − p)k
 E[X] =   , Var(X) =
           1−p
            p
                             1−p
                              p2
  Poisson P(λ) :
                                                                        λk e−λ
                                                   P (X = k) =
                                                                          k!
 E[X] = λ   , Var(X) = λ
 ASTUCE
 Astuces Binomiale :
    Probabilité que X soit paire : (1 + (1 − 2p) )
                                       1
                                       2
                                                         n




                                                               2
~~~

## Page 3

~~~text
    Approximation de Poisson : Si n grand et p petit avec np = λ :
                                             B(n, p) ≈ P(λ)

  ASTUCE
 Pour Poisson :
    Moment factoriel : E[X(X − 1) · · · (X − r + 1)] = λr

    Somme de Poisson indépendantes : X ∼ P(λ ), Y ∼ P(λ ) indépendantes
                                                 1            2

                                          X + Y ∼ P(λ1 + λ2 )




TD3 - ESPÉRANCE ET MESURES


 Convergence et Espérance
 Si (A ) avec P (A ) → 0, alors pour X ∈ L :
        n            n
                                             1


                                            lim E[X1An ] = 0
                                           n→∞


 Changement de Mesure
 Si X ≥ 0 p.s. et E[X] = 1, dénir Q(A) = E[X1 ] donne une probabilité.
                                                     A
 Relation :
                                           EQ [Y ] = EP [XY ]
 pour toute v.a. Y ≥ 0 ou bornée.
  ATTENTION
 Loi de Cauchy :
              pour tout x ∈R R
 fX (x) = π1 1+x
               1

 N'admet PAS d'espérance! |x|f (x)dx = +∞
                 2

                                    X


  ASTUCE
 Pour montrer que E[XY ] = E[X]E[Y ] n'implique pas l'indépendance :
 Prendre X ∼ U ([−1, 1]) et Y = X   2

 On a E[XY ] = E[X ] = 0 = E[X]E[Y ] mais X et Y ne sont pas indépendantes.
                         3




TD4 - TRANSFORMATIONS ET DENSITÉS


 Fonction de Répartition
 Si F (x) ∈ {0, 1} pour tout x, alors X est constante p.s.
       X




                                                     3
~~~

## Page 4

~~~text
* Changement de Variable (Théorème)
Si Y = g(X) où g strictement monotone sur I , . . . , I (partition de R), alors :
                                                          1         n

                                              n
                                              X                       d −1
                                   fY (y) =         fX (gi−1 (y))      g (y) 1gi (Ii ) (y)
                                                                     dy i
                                              i=1


Transformations Classiques
 Si X ∼ N (0, 1) :
   Y = X ∼ χ (chi-deux à 1 degré de liberté)
              2       2

   Z = σX + µ ∼ N (µ, σ )
                      1
                                   2

   W = e ∼ Log-normale
              X

 Si X ∼ U ([a, b]) :
                                                                1
                                                fX (x) =           1 (x)
                                                              b − a [a,b]

Inégalité de Jensen
Si g convexe et X admettant une espérance :
                                                    E[g(X)] ≥ g(E[X])


ASTUCE
Pour trouver la densité de Y = g(X) :
Méthode 1 (fonction de répartition) :
  1. Calculer F (y) = P (Y ≤ y) = P (g(X) ≤ y)
                  Y
  2. Dériver : f (y) = F (y)
                  Y
                               ′
                               Y
Méthode 2 (théorème de changement de variable) :
  1. Identier les intervalles où g est monotone
  2. Sur chaque intervalle : f (y) = f (g (y))|((g ) (y)|
                                       Y       X
                                                     −1             −1 ′

  3. Sommer sur tous les intervalles
Loi Gamma γ(a
                                                         ba a−1 −bx
                                           fX (x) =          x e 1R+ (x)
                                                        Γ(a)
E[X] = ab   , Var(X) =    a

Propriété additive : Si X1 ∼ γ(a1 , b) et X2 ∼ γ(a2 , b) indépendantes :
                          b2



                                               X1 + X2 ∼ γ(a1 + a2 , b)

Lien avec χ2 : χ2n = γ(n/2, 1/2)

ASTUCE
Pour Y ∼ N (0, 1) :
Y 2 ∼ χ21 = γ(1/2, 1/2)
Donc : Γ(1/2) = π
                 √




                                                               4
~~~

## Page 5

~~~text
 Pour n v.a. i.i.d. Xi ∼ N (0, 1) :
                                                 n
                                                 X
                                                            Xi2 ∼ χ2n
                                                    i=1




TD5 - CONVERGENCES


 Types de Convergence
 1. Convergence p.s. (presque sûre) :
                                             P ( lim Xn = X) = 1
                                               n→∞

 2. Convergence en probabilité :
                                   ∀ε > 0,      lim P (|Xn − X| > ε) = 0
                                               n→∞

 3. Convergence en loi :
                            lim FXn (x) = FX (x)
                            n→∞
                                                             pour tout x de continuité
 4. Convergence dans Lp :
                                             lim E[|Xn − X|p ] = 0
                                         n→∞


 Hiérarchie des Convergences

                                      p.s. ⇒ prob. ⇒ loi
                                       L ⇒ prob. ⇒ loi
                                                p


 Les réciproques sont FAUSSES en général
 * Loi Faible des Grands Nombres
 Si (X ) i.i.d. avec E[X ] = µ et Var(X ) < ∞ :
      n                 1                1

                                                 n
                                              1X     L2 ,prob.
                                                 Xi −−−−−→ µ
                                              n
                                                i=1



 * Loi Forte des Grands Nombres
 Si (X ) i.i.d. avec E[X ] = µ :
      n                 1
                                                        n
                                                1X     p.s.
                                                   Xi −−→ µ
                                                n
                                                    i=1



 * Théorème Central Limite
 Si (X ) i.i.d. avec E[X ] = µ et Var(X ) = σ < ∞ :
      n                 1                1
                                                    2

                                        Pn
                                             i=1 Xi − nµ          loi
                                                 √                −→ N (0, 1)
                                               σ n




                                                              5
~~~

## Page 6

~~~text
 Équivalent :       −nµ loi
                 Sn √
                  σ n
                        −→ N (0, 1)


  ASTUCE
 Pour montrer la convergence en probabilité :
 Utiliser Bienaymé-Tchebychev :
                                                                                           E[(Xn − X)2 ]
                                                      P (|Xn − X| > ε) ≤
                                                                                                ε2

 Si E[(X − X) ] → 0, alors X −−−→ X
          n
                      2
                                                n
                                                    prob.




 ATTENTION
 Attention aux contre-exemples :
 Convergence en probabilité ̸⇒ convergence dans L                                     1

 Exemple : P (X = n ) = 1/n, P (X = 0) = 1 − 1/n
                      n
                                  2
                                                        n
 Alors X −−−→ 0 mais E[X ] = n → ∞
          n
              prob.
                                            n


  ASTUCE
 Pour appliquer le TCL :
     1. Vérier : (X ) i.i.d., µ = E[X ], σ = Var(X ) < ∞
                              n                         1
                                                                 2
                                                                                   1
     2. Former : Z =      n
                                     −nµ
                                  Sn √
                                   σ n

     3. Conclure : Z −→ N (0, 1)
                              n
                                  loi



     4. Pour n grand : S ≈ N (nµ, nσ )  n
                                                            2




TD6 - VECTEURS ALÉATOIRES


 Densité Conjointe et Marginales
 Si (X, Y ) admet une densité f , les densités marginales sont :
                                                X,Y
                                                                           Z
                                                                fX (x) =           fX,Y (x, y)dy
                                                                               R
                                                                           Z
                                                                fY (y) =           fX,Y (x, y)dx
                                                                           R


 * Indépendance
 X   et Y sont indépendantes si et seulement si :
                                                fX,Y (x, y) = fX (x)fY (y)                  pour tout (x, y)
 Transformation de Vecteurs
 Si (U, V ) = (g (X, Y ), g (X, Y )) avec g bijective, alors :
                  1                     2

                                                            fU,V (u, v) = fX,Y (x, y)|J|−1




                                                                                   6
~~~

## Page 7

~~~text
 où J est le jacobien :                                     ∂x   ∂x
                                                       J=   ∂u   ∂v
                                                            ∂y   ∂y
                                                            ∂u   ∂v

 et (x, y) = g (u, v)
               −1



  ASTUCE
 Pour montrer l'indépendance :
 Méthode 1 : Vérier que fX,Y (x, y) = fX (x)fY (y)
 Méthode 2 : Montrer que le support se factorise : {(x, y) : fX,Y (x, y) > 0} = A × B
 Attention : Indépendance 2 à 2 ̸= indépendance mutuelle!

 Loi de Student
 Si X ∼ N (0, 1) et Y ∼ χ indépendantes :
                                2
                                n
                                                √
                                            T = √
                                                  nX
                                                   Y
                                                     ∼ tn    (loi de Student)


TD7 - VECTEURS GAUSSIENS


 * Vecteur Gaussien
 X = (X1 , . . . , Xn )T   est gaussien si :
                                                       X ∼ Nn (m, Σ)
 où m = E[X] et Σ = Cov(X)
 Densité (si Σ inversible) :
                                                                            
                                               1           1       T −1
                              fX (x) =                exp − (x − m) Σ (x − m)
                                       (2π)n/2 |Σ|1/2      2

 Propriétés Gaussiennes
 1. Combinaison linéaire : Si X ∼ Nn (m, Σ) et Y = AX + b :
                                               Y ∼ Np (Am + b, AΣAT )

 2. Indépendance : Pour vecteurs gaussiens :
                          Cov(X, Y ) = 0 ⇔ X et Y indépendantes
 Propriété SPÉCIFIQUE aux vecteurs gaussiens!
 Matrice de Covariance
                                    Σij =   Cov(X , X ) = E[(X − m )(X − m )]
                                                   i    j        i     i   j    j

 Propriétés :
    Symétrique : Σ = Σ         T

    Semi-dénie positive : x Σx ≥ 0 pour tout x
                                     T




                                                            7
~~~

## Page 8

~~~text
  ASTUCE
 Pour montrer l'indépendance de gaussiennes :
   1. Calculer Cov(X, Y )
   2. Si Cov(X, Y ) = 0 : X et Y sont indépendantes!
 Pour trouver la loi de Y = AX + b :
   1. E[Y ] = AE[X] + b
   2. Cov(Y ) = ACov(X)A     T

   3. Y ∼ N (E[Y ], Cov(Y ))
 Loi Conditionnelle
 Si (X, Y ) gaussien avec X ∈ R , Y ∈ R :
                                 p          q


                                        X|Y = y ∼ N (µX|Y , ΣX|Y )

 où :
                                      µX|Y = mX + ΣXY Σ−1
                                                       Y (y − mY )

                                        ΣX|Y = ΣX − ΣXY Σ−1
                                                         Y ΣY X




TD8 - ESPÉRANCE CONDITIONNELLE


 * Dénition
 E[X|G]   est une v.a. G-mesurable telle que :
                                                 Z                   Z
                                     ∀A ∈ G,         E[X|G]dP =            XdP
                                                 A                     A


 Propriétés Fondamentales
 1. Linéarité : E[aX + bY |G] = aE[X|G] + bE[Y |G]
 2. Tour d'espérance : E[E[X|G]] = E[X]
 3. Sortie des constantes : Si Y est G -mesurable :
                                            E[XY |G] = Y E[X|G]

 4. Indépendance : Si X indépendante de G :
                                                E[X|G] = E[X]

 Espérance Conditionnelle pour Vecteurs
 Si (X, Y ) a une densité conjointe f :
                                      X,Y
                                                       Z
                                      E[X|Y = y] =             xfX|Y (x|y)dx
                                                           R

 où :                                                      fX,Y (x, y)
                                            fX|Y (x|y) =
                                                             fY (y)




                                                       8
~~~

## Page 9

~~~text
 ASTUCE
 Pour calculer E[X|Y ] :
 Cas discret :                                       X
                               E[X|Y = y] =                xP (X = x|Y = y)
                                                      x

 Cas continu :
   1. Trouver la loi de (X, Y )
   2. Calculer la densité conditionnelle : f (x|y) =
                                              X|Y
                                                                   fX,Y (x,y)
                                                                     fY (y)
   3. Intégrer : E[X|Y = y] = xf (x|y)dx
                                R

 Cas gaussien : Utiliser la formule directe!
                                     X|Y




 Cas Gaussien
 Si (X, Y ) gaussien :
                                                          Cov(X, Y ) (Y − E[Y ])
                              E[X|Y ] = E[X] +
                                                           Var(Y )
 Variance conditionnelle :

                                   Var(X|Y ) = Var(X) − CovVar(X,(YY) )
                                                                                2




 ATTENTION
 Pièges courants :
  E[X|Y ] = Y  et E[Y |X] = X n'impliquent PAS forcément X = Y p.s.
  Mais si en plus E[X ] = E[Y ], alors X = Y p.s.
                         2     2




FONCTIONS CARACTÉRISTIQUES


 Dénition
                                                               Z
                                                    itX
                                   φX (t) = E[e           ]=        eitx fX (x)dx
                                                               R


 Propriétés
 1. Linéarité : φaX+b (t) = eitb φX (at)
 2. Indépendance : Si X et Y indépendantes :
                                           φX+Y (t) = φX (t)φY (t)

 3. Moments :
                                                            1 (n)
                                             E[X n ] =       φ (0)
                                                           in X
 4. Unicité : φX = φY ⇔ X et Y ont même loi

 Fonctions Caractéristiques Classiques
  Gaussienne N (µ, σ 2 ) :
                                                                    σ 2 t2
                                             φX (t) = eiµt− 2



                                                           9
~~~

## Page 10

~~~text
  Poisson P(λ) :
                                                                it
                                                  φX (t) = eλ(e −1)
  Uniforme U ([−a, a]) :
                                                             sin(at)
                                                  φX (t) =
                                                                at

  ASTUCE
 Pour identier une loi via la fonction caractéristique :
     1. Calculer φ (t)
                   X
     2. Comparer avec les fonctions caractéristiques connues
     3. Si égalité : les lois sont identiques!

ASTUCES ET TECHNIQUES


  ASTUCE
 1. Pour montrer qu'une v.a. est constante p.s. :
    Montrer que Var(X) = 0
    Montrer que F (x) ∈ {0, 1}
     Si X + Y constante p.s. et X, Y indépendantes : alors X et Y constantes p.s.
                   X
 

  ASTUCE
 2. Lemme deP Borel-Cantelli :
  BC1 : Si P (An ) < ∞, alors PP(lim sup An ) = 0
  BC2 : Si (An ) indépendants et P (An ) = ∞, alors P (limP sup An ) = 1
 Interprétation : Il y a p.s. une innité de An réalisés si P (An ) = ∞ (et indép.)

 ASTUCE
 3. Pour calculer P (X = Y ) où X, Y continues :
 Utiliser la densité conjointe :
                                                                     (facteur correctif)
                                              Z
                             P (X = Y ) =          fX,Y (t, t)dt ·
                                              R

 Souvent : P (X = Y ) = 0 pour des v.a. continues!
  ASTUCE
 4. Sommes de v.a. indépendantes :
 Pour trouver f  X+Y   :                  Z
                             fX+Y (z) =       fX (x)fY (z − x)dx = (fX ∗ fY )(z)

 C'est le produit de convolution!
                                          R




                                                          10
~~~

## Page 11

~~~text
CHECKLIST POUR LES EXERCICES

 Pour montrer l'indépendance
 Variables discrètes :
   □   Vérier P (X = x, Y = y) = P (X = x)P (Y = y) pour tous x, y
 Variables continues :
   □ Vérier f (x, y) = f (x)f (y) pour tous x, y
               X,Y             X        Y
   □ Ou vérier que le support se factorise
 Variables gaussiennes :
   □   Vérier Cov(X, Y ) = 0
 Pour trouver une densité
 Méthode de la fonction de répartition :
   □ Calculer F (y) = P (Y ≤ y)
                 Y
   □ Dériver : f (y) = F (y)
                 Y
                           ′
                           Y
 Changement de variable :
   □ Identier les intervalles de monotonie
   □ Appliquer : f (y) = f (g (y))|(g ) (y)|
                     Y         X
                                   −1       −1 ′

   □ Sommer sur tous les intervalles
 Vecteurs :
   □ Trouver la transformation (U, V ) = (g (X, Y ), g (X, Y ))
                                               1         2
   □ Calculer le jacobien |J|
   □ Appliquer : f (u, v) = f
                     U,V         (x, y)|J|
                                   X,Y
                                               −1



 ATTENTION
 ERREURS FRÉQUENTES
   1. Confondre indépendance 2 à 2 et indépendance mutuelle
   2. Croire que E[XY ] = E[X]E[Y ] implique l'indépendance (FAUX!)
   3. Pour gaussiennes : Cov = 0 ⇔ indép. (vrai UNIQUEMENT pour gaussiennes)
   4. Oublier la valeur absolue dans le changement de variable : |J| ou |(g ) |
                                                                      −1 ′

   5. Pour convergence en loi : utiliser le TCL SEULEMENT si variance nie
   6. Pour v.a. continues : P (X = a) = 0 toujours!
   7. Pour espérance conditionnelle : penser à vérier la mesurabilité




                                                    11
~~~
