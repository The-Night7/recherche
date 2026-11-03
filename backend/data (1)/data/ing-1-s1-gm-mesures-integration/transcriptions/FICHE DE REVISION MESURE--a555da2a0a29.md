# FICHE DE REVISION MESURE.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Pj2cyz1i9GfVaRvK6LsBW3YOxa4VKBCl) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                               FICHE DE RÉVISION
                                            Mesure & Intégration
                                             ING1 - Génie Mathématique




TD1 - TRIBUS ET APPLICATIONS MESURABLES


 Dénition : Tribu
 T ⊂ P(Ω)      est une tribu si :
    1. Ω ∈ T
    2. A ∈ T ⇒ A S∈ T  c

    3. (A ) ∈ T ⇒ A ∈ T
           n               n∈N     n


 ASTUCE
 De la dénition, on déduit automatiquement :
    ∅ ∈ T (car ∅ = Ω )        c

    Stabilité par intersection dénombrable : T A = (S A ) ∈ T
                                                           n
                                                                    c c
                                                                    n


 Application Mesurable
 f : (Ω1 , T1 ) → (Ω2 , T2 )   est mesurable si :
                                               ∀B ∈ T2 ,   f −1 (B) ∈ T1

 Propriétés Importantes
  Tribu trace : TU = {A ∩ U : A ∈ T }  est une tribu sur
                                                  U
  Tribu image réciproque : f (F) = {f (B) : B ∈ F}
                               −1      −1                 est une tribu
  Composition : fSi mesurable et continue, alors mesurable
                                   g          g◦f
               Si mesurable :
  Stabilité : f
    |f |, f , f sont mesurables
               +   −

    inf f , sup f , lim inf f , lim sup f sont mesurables
           n n         n n             n n          n n


 ASTUCE
 Pour montrer qu'une fonction est mesurable :
    1. Vérier directement f (B) ∈ T pour tout borélien B
                                       −1

    2. OU montrer que f est limite de fonctions mesurables
    3. OU montrer que f est composée de fonctions mesurables/continues




                                                           1
~~~

## Page 2

~~~text
TD2 - MESURES


 Dénition : Mesure
 m : T → [0, +∞]   est une mesure si :
   1. m(∅) = 0
   2. σ-additivité : Si (A ) sont disjoints, alors m (S A ) = P m(A )
                            n                                          n   n       n   n


 Propriétés des Mesures
 1. Monotonie : A ⊂ B ⇒S m(A) ≤ P  m(B)
 2. Sous-additivité : m ( n An ) ≤ n m(An )
 3. Continuité croissante : Si An ↑ A, alors m(An ) → m(A)
 4. Continuité décroissante : Si An ↓ A et m(A0 ) < ∞, alors m(An ) → m(A)

 Mesures Classiques
  Mesure de Lebesgue : λ([a, b]) = b −(a
  Mesure de Dirac : δx (A) = 1A (x) =
                                       si x ∈ A        1
                                       sinon           0
  Mesure de comptage : µ (A)P= Card   (nombre d'éléments)
                                                      (A)
                                 a δ est une mesure si a > 0
                                    c
  Combinaison linéaire : µ =               k
                                            i=1   i xi                             i


 ASTUCE
 Propriétés importantes de la mesure de Lebesgue :
    Les singletons : λ({x}) = 0
    Les ensembles dénombrables     : λ(Q) = 0
    Pour calculer : λ ( [a , b ]), attention aux recouvrements!
                        S
                                n       n


 ATTENTION
 Pièges courants :
    Suite d'événements disjoints (A ) : TOUJOURS P (A ) → 0
                                             n                                 n
    Pour la continuité décroissante, il FAUT m(A ) < ∞ !          0




TD3 - INTÉGRATION DE FONCTIONS POSITIVES


 Intégrale d'une Fonction Étagée
 Pour φ = P  m
             i=1 ai 1Ai   (forme canonique) :
                                                  Z            m
                                                               X
                                                       φdµ =           ai µ(Ai )
                                                   Ω           i=1

 Propriétés : Linéarité, Monotonie, Additivité domaniale




                                                               2
~~~

## Page 3

~~~text
 Théorème de Convergence Monotone (Beppo-Levi)
 Si (f ) est une suite croissante de fonctions positives et f → f µ-p.p., alors :
     n                                                                         n

                                               Z                     Z
                                                   f dµ = lim                fn dµ
                                                            n→∞



 ASTUCE
 Quand utiliser Beppo-Levi ?
   Suite CROISSANTE de fonctions POSITIVES
    Permet d'intervertir limiteRetPintégraleP R
    Très utile pour les séries : f = f    n               n


 Lemme de Fatou
 Pour (f ) fonctions positives :
         n
                                       Z                                       Z
                                           lim inf fn dµ ≤ lim inf                 fn dµ
                                           n→∞                      n→∞


 Formules Utiles
  Espérance pour X ∈ N :
                                                           ∞
                                                           X
                                               E[X] =              P (X > n)
                                                           n=0

  Pour X ∈ N avec variance nie :
                                                     ∞
                                                     X
                                       E[X 2 ] =           (2k + 1)P (X > k)
                                                     k=0

 Astuce : Utiliser P (X = k) = P (X > k − 1) − P (X > k)

 ASTUCE
 Pour calculer une intégrale de fonction positive :
   1. Si fonction étagée : appliquer directement la formule
   2. Si limite de suite croissante : utiliser Beppo-Levi
   3. Si somme de fonctions positives : f = P R f (Beppo-Levi)
                                           RP
                                                      n                  n




TD4 - INTÉGRATION DE FONCTIONS DE SIGNE QUELCONQUE


 Fonction Intégrable
 f :Ω→R    est µ-intégrable si :
    fR est mesurable R
    f dµ < ∞ ET f dµ < ∞
             +                −

 où f =Z max(f, 0)Z et f = max(−f,
     +                    −        0)
 Alors : f dµ = f dµ − f dµ
                             Z
                      +            −




                                                               3
~~~

## Page 4

~~~text
Théorème de Convergence Dominée (Lebesgue)
Si :
    f → f µ-p.p.
       n
    ∃g intégrable telle que |f | ≤ g pour tout n
                                       n
Alors f est intégrable et :             Z                           Z
                                                    f dµ = lim              fn dµ
                                                           n→∞



ASTUCE
La clé : Trouver une bonne fonction dominante g !
Exemples classiques de dominantes :
        xn
            ≤
       1+xn+2
                   (intégrable sur R )
                      1
                    1+x2
                                               +


   sin    x
            n
                   n
                   ≤
                x(1+x2 )
                                  1
                                1+x2

   |e sin(xy)| ≤ e (intégrable sur [0, ∞[)
       −y                  −y



ATTENTION
Attention : La fonction g doit être INTÉGRABLE !
Si g n'est pas intégrable, on ne peut PAS appliquer la convergence dominée.
ASTUCE
Technique : Découper le domaine
Pour montrer l'intégrabilité, séparer :
   A = {|f | ≤ 1} : sur cet ensemble, |f | ≤ 1
       1
   A = {|f | > 1} : sur cet ensemble, utiliser |f | ≤ f si R f < ∞
       2
                                                                        2           2



Mesure à Densité
Si f ≥ 0 mesurable, alors ν(A) = R f dµ dénit une mesure.
                                           A
Formule de changement de variable :
                                                    Z           Z
                                                        gdν =       gf dµ

Intégrabilité : g est ν -intégrable ⇔ gf est µ-intégrable

Mesure Image
Si T : (Ω, T ) → (Ω , A) mesurable, alors :
                     ′


                                       µT (B) = µ(T −1 (B))     dénit une mesure
Formule :                                       Z               Z
                                                    gdµT =          g ◦ T dµ




                                                            4
~~~

## Page 5

~~~text
ESPACES Lp


 Dénitions
 Pour p ∈ [1, ∞[ :                                               Z               
                                                  p                         p
                                                L =          f:        |f | dµ < ∞
                                                                  Z                 1/p
                                                                                p
                                                 Np (f ) =                 |f | dµ

 Pour p = ∞ :
                                           L∞ = {f : ∃M, |f | ≤ M µ -p.p.}
                                          N (f ) = inf{M : |f | ≤ M µ-p.p.}
                                            ∞


 Inégalités Fondamentales
 1. Inégalité de Hölder : Pour p1 + 1q = 1 :

                                                  N1 (f g) ≤ Np (f ) · Nq (g)

 2. Inégalité de Cauchy-Schwarz : (cas p = q = 2)
                                            Z                 sZ                    sZ
                                                 f gdµ ≤                   f 2 dµ            g 2 dµ


 3. Inégalité de Minkowski :
                                                Np (f + g) ≤ Np (f ) + Np (g)


 Inclusions
 Si µ(Ω) < ∞ et 1 ≤ p ≤ p ≤ ∞ :
                      1           2


                                                     L∞ ⊂ Lp2 ⊂ Lp1 ⊂ L1

 ASTUCE
 Pour montrer f g est intégrable :
   1. Si f ∈ L et g ∈ L avec + = 1 : utiliser Hölder
                  p       q           1
                                      p
                                            1
                                            q
   2. Si f ∈ L et g ∈ L : |f g| ≤ N (g)|f |, donc f g ∈ L
                  1       ∞
                                                ∞
                                                                                     1




TD5 - MESURE PRODUIT ET FUBINI

 Théorème de Fubini-Tonelli
 Si f : Ω × Ω → [0, +∞] est mesurable, alors :
        1     2

                              Z                                   Z        Z                         
                                          f d(µ1 ⊗ µ2 ) =                            f (x1 , x2 )dµ2 dµ1
                              Ω1 ×Ω2                                  Ω1        Ω2

                                                 Z       Z                              
                                            =                     f (x1 , x2 )dµ1 dµ2
                                                    Ω2       Ω1




                                                                      5
~~~

## Page 6

~~~text
Condition : f ≥ 0 (fonction POSITIVE)

ASTUCE
Fubini-Tonelli : Pour fonctions POSITIVES
On peut TOUJOURS inverser l'ordre d'intégration pour des fonctions positives!
Très utile pour vérier l'intégrabilité : appliquer à |f |
Théorème de Fubini
Si f : Ω × Ω → R est µ-intégrable, alors :
        1    2
    Pour µ -presque tout x , x 7→ f (x , x ) est µ -intégrable
            1                   1   2          1      2            2
    Les intégrales itérées existent et sont
                                          
                                             égales                                          
                     Z                   Z        Z                             Z    Z
                                f dµ =                    f dµ2 dµ1 =                     f dµ1 dµ2
                       Ω1 ×Ω2            Ω1        Ω2                           Ω2   Ω1

Condition : f INTÉGRABLE (i.e.                                )
                                         R
                                             |f |dµ < ∞

ATTENTION
ATTENTION : Fubini vs Fubini-Tonelli
 Fubini-Tonelli                   Fubini
 f ≥0  (positive)                                         fintégrable
 Toujours applicable                                      Vérier intégrabilité d'abord
 Résultat peut être +∞                                    Résultat ni
ASTUCE
Méthodologie pour Fubini :
Étape 1 : Appliquer Fubini-Tonelli à |f | pour vérier :
                                              Z
                                                   |f |d(µ1 ⊗ µ2 ) < ∞

Étape 2 : Si oui, appliquer Fubini à f pour calculer l'intégrale
Étape 3 : Choisir l'ordre d'intégration le plus simple!

ATTENTION
Contre-exemples importants :
1. Mesure non σ-nie :
   Mesure de dénombrement sur [0, 1] n'est PAS σ-nie
   Fubini peut échouer même si les intégrales itérées existent
2. Fonction non intégrable :
   Les intégrales itérées peuvent exister
   Mais donner des résultats diérents! (Ex :                 x2 −y 2
                                                              (x2 +y 2 )2
                                                                            )




                                                               6
~~~

## Page 7

~~~text
INÉGALITÉS DE PROBABILITÉ


 Inégalité de Markov
 Pour a > 0 :
                                                             E[|X|]
                                           P (|X| ≥ a) ≤
                                                               a
 Généralisation : Pour g croissante :
                                                         E[g(|X|)]
                                         P (|X| ≥ a) ≤
                                                           g(a)

 Inégalité de Bienaymé-Tchebychev
 Pour ε > 0 :
                                      P (|X − E[X]| ≥ ε) ≤
                                                                Var(X)
                                                                  ε2

 Formules de Variance
                                Var(X) = E[X ] − E[X]    2            2


 Conséquence : E[X] ≤ E[X ] (par Cauchy-Schwarz)
                        2        2




LOIS DE PROBABILITÉ CLASSIQUES


 Loi Binomiale B(n
                                                   
                                                   n k
                                      P (X = k) =     p (1 − p)n−k
                                                   k
                                     E[X] = np,   Var(X) = np(1 − p)
 Astuce : Probabilité que X soit paire : 21 (1 + (1 − 2p)n )

 Loi de Poisson P(λ)
                                                             λk e−λ
                                           P (X = k) =
                                                               k!
                                         E[X] = λ,    Var    (X) = λ
 Moment factoriel : E[X(X − 1) · · · (X − r + 1)] = λr

 Loi Géométrique G(p)

                                      P (X = k) = p(1 − p)k ,     k∈N
                                                         1−p
                                              E[X] =
                                                          p




                                                     7
~~~

## Page 8

~~~text
ASTUCES ET TECHNIQUES DE CALCUL


 ASTUCE
 1. Découpage du domaine
 Pour montrer l'intégrabilité, séparer :
    {|f | ≤ 1} : majorer par une constante ou utiliser |f | ≤ |f | si p > q
                                                                       p        q

    {|f | > 1} : majorer par |f | si on connaît |f | < ∞
                                 p
                                                R              p



 ASTUCE
 2. Coordonnées polaires
 Pour intégrales sur R :
                      2

                                          x = r cos θ,         y = r sin θ
                                                     dxdy = r dr dθ
 Attention : Bien vérier les bornes d'intégration!

 Intégrales Classiques
                                     Z ∞
                                                                           b
                                                e−ax sin(bx)dx =
                                      0                                a2 + b2
                                     Z ∞
                                                                           a
                                                e−ax cos(bx)dx =
                                      0                                a2 + b2
                                                Z +∞
                                                           1
                                                               dx = π
                                                 −∞     1 + x2
                                                Z +∞
                                                           1        π
                                                               dx =
                                                 0      1 + x2      2

 ASTUCE
 3. Séries géométriques

                                                                   si |r| < 1
                                          ∞
                                          X               1
                                                 rn =
                                                         1−r
                                          n=0

 Utile pour :
    Vérier qu'on a une mesure : P p = 1        i,j
    Calculer des espérances de lois géométriques
                                          i,j




                                                           8
~~~

## Page 9

~~~text
CHECKLIST POUR LES EXERCICES

 Pour calculer une intégrale
 Étape 1 : Identier le type
    Fonction positive? → Fubini-Tonelli ou Beppo-Levi
    Fonction de signe quelconque? → Vérier intégrabilité d'abord
    Suite de fonctions? → Chercher théorème de convergence
    Intégrale double? → Fubini
 Étape 2 : Vérier les conditions
    Mesurabilité? (souvent Rdonnée ou évidente)
    Intégrabilité? (calculer |f | < ∞)
    Hypothèses du théorème? (croissance, dominante, etc.)
 Étape 3 : Appliquer et calculer

 Pour appliquer un théorème de convergence
 Beppo-Levi :
   □ Suite CROISSANTE?
   □ Fonctions POSITIVES?
   □ Convergence µ-p.p.?
 Convergence Dominée :
   □ Convergence µ-p.p.?
   □ Fonction dominante INTÉGRABLE trouvée?
   □ |f | ≤ g pour tout n ?
       n
 Fubini :
   □ D'abordRappliquer Fubini-Tonelli à |f |
   □ Vérier |f | < ∞
   □ Mesures σ -nies?
   □ Choisir l'ordre d'intégration le plus simple

 ATTENTION
 PIÈGES À ÉVITER
   1. Ne pas confondre convergence ponctuelle et convergence en mesure
   2. Pour convergence dominée : la dominante doit être INTÉGRABLE
   3. Pour Fubini : vérier d'abord l'intégrabilité avec Fubini-Tonelli sur |f |
   4. Mesure de Lebesgue : singletons et dénombrables sont de mesure nulle
   5. Pour continuité décroissante : il FAUT m(A ) < ∞
                                                    0
   6. Suite d'événements disjoints : P (A ) → 0 TOUJOURS
                                          n
   7. Les mesures doivent être σ-nies pour Fubini




                                                    9
~~~
