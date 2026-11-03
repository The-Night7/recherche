# Mesure_Exo1_2024_Corrigé.pdf

[Ouvrir l’original](https://drive.google.com/open?id=12MPejD1ob5jw535SAYotRHFelDox3KhV) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Correction : Examen Mesure & Intégration - Exercice 1
Rappels de cours (issus de la Fiche de Révision)
    Avant d’attaquer l’exercice, voici les points essentiels de votre fiche nécessaires pour
résoudre ce problème :


   1. Définition d’une Mesure (Page 2)
 Une application m : T → [0, +∞] est une mesure si :
   — m(∅) = 0                                        S      P
   — σ-additivité : Si (An ) sont disjoints, alors m( An ) = m(An ).



     2. Mesure à Densité (Page 4)
 Si f ≥ 0 est mesurable et µ est une mesure, on peut définir une nouvelle mesure ν
 par :                                   Z
                                  ν(A) =    f dµ
                                                 A
 Formule de changement de variable :
                           Z         Z
                              g dν = gf dµ

 Intégrabilité : g est ν-intégrable ⇐⇒ gf est µ-intégrable.



     3. Propriétés de l’Intégrale (Page 2 et 3)
                   R                 R       R
     — Linéarité : (αf + βg)dµ = α R f dµ + β gdµ.
     — Fonction positive : Si g ≥ 0, gdµ = 0 =⇒ g = 0 µ-p.p. (et inversement
       sur un ensemble de mesure nulle).




                                             1
~~~

## Page 2

~~~text
Solution de l’Exercice 1
Données :
  — (Ω, T ) un espace mesurable.
  — f : (Ω, T ) → (R+ , B(R+ )) mesurable (f ≥ 0).
  — m1 , m2 deux mesures positives.
  — α1 , α2 ∈ R∗+ .                          R       R
  — Définition de m : ∀A ∈ T , m(A) = α1 A f dm1 + α2 A f dm2 .


1. Montrer que (Ω, T , m) est un espace mesuré.
                                                 R T . D’après le cours (Mesure à densité,
    Il faut vérifier que m Rest bien une mesure sur
page 4), posons ν1 (A) = A f dm1 et ν2 (A) = A f dm2 . Comme f ≥ 0, ν1 et ν2 sont des
mesures sur (Ω, T ). On a alors m = α1 ν1 + α2 ν2 . Comme α1 , α2 > 0, une combinaison
linéaire à coefficients positifs de mesures est une mesure.
    Vérification détaillée (si nécessaire) :
    — Ensemble vide :
                                  Z            Z
                      m(∅) = α1 f dm1 + α2 f dm2 = α1 × 0 + α2 × 0 = 0.
                                 ∅                   ∅

   — σ-additivité : Soit (An )n∈N une suite d’ensembles disjoints de T .
                    !                !                !
             [                  [                [
         m      An = α1 ν1         An + α2 ν2      An
                 n                    n                        n
                                 X                   X
                         = α1        ν1 (An ) + α2           ν2 (An ) (car νi sont des mesures)
                                 n                       n
                             X                                         X
                         =       (α1 ν1 (An ) + α2 ν2 (An )) =             m(An ).
                             n                                         n

Conclusion : m est bien une mesure.

2. Montrer que m est finie ssi f est mi -intégrable pour i = 1, 2.
   Une mesure m est finie si m(Ω) < +∞. Calculons m(Ω) :
                                    Z           Z
                         m(Ω) = α1 f dm1 + α2 f dm2 .
                                           Ω                       Ω

Puisque f ≥ 0, α1 > 0 et α2 > 0, les deux termes de la somme sont positifs. Une somme
de termes positifs est finie si et seulement si chaque terme est fini.
                                     Z                      Z
              m(Ω) < +∞ ⇐⇒              f dm1 < +∞ ET          f dm2 < +∞.
                                      Ω                                    Ω
                             R
Or, comme f ≥ 0, dire que Ω f dmi < +∞ est exactement la définition de "f est mi -
intégrable".
    Conclusion : m est finie ⇐⇒ ∀i = 1, 2, f est mi -intégrable.



                                                2
~~~

## Page 3

~~~text
3. Soit A ∈ T . Montrer que m1 (A) = 0 et m2 (A) = 0 =⇒ m(A) = 0.
   Supposons m1 (A) = 0 et m2 (A) = 0. Par définition :
                 Z              Z             Z             Z
       m(A) = α1    f dm1 + α2    f dm2 = α1 f · 1A dm1 + α2 f · 1A dm2 .
                     A                   A                     Ω                     Ω

Rappelons une propriété classique (Page 2, astuce "suites d’événements" ou simplement
propriété de l’intégrale) : l’intégrale sur un ensemble de mesure nulle est nulle.R
   — Puisque m1 (A) = 0, la fonction f ·1A est nulle m1 -presque partout. Donc A f dm1 =
       0.                             R
   — De même, m2 (A) = 0 =⇒ A f dm2 = 0.
Ainsi, m(A) = α1 × 0 + α2 × 0 = 0.

4. Soit g : (Ω, T ) → (R, B(R)) mesurable et positive.
                         Z                Z                        Z
   (a) Montrer que           gdm = α1            f gdm1 + α2           f gdm2 .
                         Ω                   Ω                     Ω
   C’est la généralisation de la formule de changement de variable pour les mesures à
densité (Page 4). On procède par la méthode de la fonction étagée (standard machine) :
   1. Si g = 1A (fonction indicatrice) :
   Z                          Z                      Z                  Z                    Z
         1A dm = m(A) = α1           f dm1 + α2           f dm2 = α1         f 1A dm1 + α2       f 1A dm2 .
     Ω                           A                   A                   Ω                   Ω

La formule est
             Pvraie.
   2. Si g = k ak 1Ak (fonction étagée positive) : Par linéarité de l’intégrale (Page 2), la
formule reste vraie (combinaison linéaire de l’étape 1).
   3. Si g est mesurable positive quelconque : Il existe une suite croissante de fonctions
étagées positives (gn ) telle que gn ↑ g. On applique le Théorème de Convergence
Monotone (Beppo-Levi) (Page 3) :
                                  Z              Z
                                    gdm = lim      gn dm
                                                         n→∞


Et pour le membre de droite :
              Z              Z            Z           Z
          lim α1 f gn dm1 + α2 f gn dm2 = α1 f gdm1 + α2 f gdm2 .
           n→∞


(Car f gn ↑ f g puisque f ≥ 0). La formule est donc démontrée.
    (b) En déduire condition R d’intégrabilité.
    g est m-intégrable ⇐⇒ Ω |g|dm < +∞. Ici g ≥ 0, donc |g| = g. D’après la formule
(a) :                     Z            Z             Z
                                 gdm = α1       f gdm1 +α2 f gdm2 .
                             Ω                   Ω
                                              | {z }      | Ω {z }
                                                     A                   B

   R α1 , α2 > 0 et A, B ≥ 0, la somme est finie si et seulement si A < ∞ et B < ∞.
Comme
Or, f gdmi < ∞ signifie exactement que f g est mi -intégrable (car f g ≥ 0).
   Conclusion : g est m-intégrable ⇐⇒ f g est mi -intégrable pour i = 1, 2.


                                                         3
~~~

## Page 4

~~~text
5. Soit g mesurable de signe quelconque.
    (a) Condition d’intégrabilité.
    Par définition, g est m-intégrable si et seulement si |g| est m-intégrable. On applique
le résultat de la question 4.(b) à la fonction positive |g|. g est m-intégrable ⇐⇒ |g| est
m-intégrable ⇐⇒ f |g| est mi -intégrable pour i = 1, 2. Or, f |g| = |f g| (car f ≥ 0). Donc
⇐⇒ f g est mi -intégrable pour i = 1, 2.
    (b) Formule intégrale.
    Supposons g intégrable. On décompose g = g + − g − (parties
                                                             R + positive et négative, Page
                       −
                  +
                                                                              R −
3). On a |g| = g + g . L’intégrabilité de g implique que g dm < ∞ et g dm < ∞.
On peut appliquer la formule de la question 4.(a) à g + et g − séparément :
                         Z              Z                Z
                           g dm = α1 f g dm1 + α2 f g + dm2
                             +                +


                        Z               Z                  Z
                            −                 −
                            g dm = α1       f g dm1 + α2       f g − dm2

En soustrayant ces deux égalités (ce qui est légitime car toutes les intégrales sont finies) :
                Z         Z            Z
                   gdm = g dm − g − dm
                               +

                              Z                        Z
                        = α1 f (g − g )dm1 + α2 f (g + − g − )dm2
                                    +     −

                              Z                Z
                        = α1 f gdm1 + α2 f gdm2 .




                                              4
~~~
