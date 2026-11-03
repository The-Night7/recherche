# Brouillon optimisation_complete.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Ag51pZuM7v2oIgB7G8FOeobmeJ1vZMj0) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
FICHE OPTIMISATION - CY TECH ING1-GM                                                 Point régulier : ∇h1 (x∗ ), ..., ∇hp (x∗ ) linéairement indépendants                             s1
                                                                                                                                                                                              x1
                                                                                                                                                                                              −3
                                                                                                                                                                                                       x2
                                                                                                                                                                                                        2
                                                                                                                                                                                                            s1
                                                                                                                                                                                                             1
                                                                                                                                                                                                               s2
                                                                                                                                                                                                                0
                                                                                                                                                                                                                    s3
                                                                                                                                                                                                                     0          2
                                                                                     Espace tangent : T (x∗ ) = {y ∈ Rn : ∇hi (x∗ )T y = 0, ∀i}                 Tableau initial :     s2      −1        2    0  1    0          4
=== I. OPTIMISATION LINEAIRE ===                                                     Condition 2nd ordre (susante) :                                                                 s3       1        1    0  0    1          5
1. MÉTHODE SIMPLEXE - FORME STANDARD                                                      xx L(x , λ )y > 0 ∀y ∈ T (x ), y ̸= 0
                                                                                     y T ∇2     ∗   ∗                ∗                                                                 z      −1       −2    0  0    0          0
Forme standard : max cT x s.c. Ax ≤ b, x ≥ 0                                         Méthode substitution : Exprimer variables via contraintes puis optimiser   Pivot sur x2 (colonne 2), ligne s2 (ratio min 4/2 = 2)
Avec variables d'écart : Ax + s = b, s ≥ 0                                           9. OPTIMISATION AVEC CONTRAINTES INÉGALITÉ                                 Solution nale : x1 = 2, x2 = 3, z = 8
                                                                                                                                                                                    ∗        ∗       ∗

Base réalisable : Variables hors base = 0                                            Problème : min f (x) s.c. gj (x) P
                                                                                                                      ≤ 0, j = 1, ..., m                        15. EXEMPLE 2KKT2 COMPLET
Critère d'optimalité : Tous coef. ligne z ≤ 0                                        Lagrangien : L(x, µ) = f (x) + m  j=1 µj gj (x)
                                                                                                                                                                min f (x1 , x2 ) = x1 − x2 + x1 x2
Choix pivot : Colonne : coef. > 0 en ligne z | Ligne : min ratio bi /aik (aik > 0)   Conditions KKT :                                                           s.c. g1 (x1 , x2 ) = x21 + x22 − 1 ≤ 0, g2 (x1 , x2 ) = x1 + x2 − 1 ≤ 0
Pivotage : (1) Diviser ligne pivot par pivot | (2) Annuler colonne pivot              ∇x L(x∗ , µ∗ ) = 0 (stationnarité)                                       L = x2 1 −
                                                                                                                                                                          2
                                                                                                                                                                            x2 + x1 x2 + µ1 (x2       2
                                                                                                                                                                                                1 + x2 − 1) + µ2 (x1 + x2 − 1)
Solution non bornée : Colonne pivot sans coef. > 0                                    gj (x∗ ) ≤ 0 ∀j (admissibilité primale)                                               2x1 + x2 + 2µ1 x1 + µ2
Dégénérescence : bi = 0 dans base ⇒ risque cyclage                                      j ≥ 0 ∀j (admissibilité duale)
                                                                                      µ∗
                                                                                                                                                                ∇x L =
                                                                                                                                                                           −2x2 + x1 + 2µ1 x2 + µ2
                                                                                                                                                                                                          =0
2. MÉTHODE      2 PHASES                                                                                                                                        Cas 1 : µ1 = µ2 = 0 ⇒ x∗ = (0, 0)
                                                                                        j gj (x ) = 0 ∀j (complémentarité)
                                                                                      µ∗       ∗
Phase I : min P yi avec variables articielles yi                                    Contraintes actives : I(x∗ ) = {j : gj (x∗ ) = 0}
                                                                                                                                                                Vérier : g1 (0, 0) = −1 ≤ 0 , g2 (0, 0) = −1 ≤ 0
Si min = 0 ⇒ base réalisable trouvée                                                                                                                            Hessienne en (0, 0) : indénie ⇒ point selle
Si min > 0 ⇒ problème impossible                                                     Si j ∈/ I(x∗ ) ⇒ µ∗j = 0                                                   Cas 2 : µ1 > 0, µ2 = 0 ⇒ g1 (x∗ ) = 0
Phase II : Simplexe normal avec base phase I                                         Point qualié (LICQ) : ∇gj (x∗ ) pour j ∈ I(x∗ ) lin. indép.               Système : x21 + x22 = 1, ...
3. DUALITÉ                                                                           Cône tangent : K(x∗ ) = {d : ∇gj (x∗ )T d ≤ 0, j ∈ I(x∗ )}                 Cas 3 : µ1 = 0, µ2 > 0 ⇒ g2 (x∗ ) = 0
Primal (P) : max cT x, Ax ≤ b, x ≥ 0                                                                                                                            Cas 4 : µ1 > 0, µ2 > 0 ⇒ les deux actives
                                                                                     Condition 2nd ordre : dT ∇2xx L(x∗ , µ∗ )d > 0 ∀d ∈ K(x∗ ), d ̸= 0         Résoudre chaque cas, garder solutions avec µj ≥ 0
Dual (D) : min bT y, AT y ≥ c, y ≥ 0                                                 10. CAS MIXTE (ÉGALITÉ + INÉGALITÉ)                                        16. EXEMPLE MOINDRES CARRÉS
Théorème dualité faible : cT x ≤ bT y ∀x, y réalisables                              min f (x) s.c. hi (x) = 0, gj (x) ≤ 0
                                                                                                                                                                    
                                                                                                                                                                     1
                                                                                                                                                                        
                                                                                                                                                                          0
                                                                                                                                                                              
                                                                                                                                                                                    6
Théorème dualité forte : Si x∗ , y∗ optimaux ⇒ cT x∗ = bT y∗                                               P              P
                                                                                     L(x, λ, µ) = f (x) − i λi hi (x) + j µj gj (x)                             A = 0    1, b = 3
Complémentarité (KKT) :                                                              KKT :                                                                           1    1         3

    j > 0 ⇒ contrainte duale j saturée : (A y )j = cj
                                                                                                                                                                                                            
 x∗                                        T ∗
                                                                                      ∇x L = 0                                                                 AT A =
                                                                                                                                                                         2  1
                                                                                                                                                                                , (AT A)−1 = 3
                                                                                                                                                                                             1    2          −1
                                                                                                                                                                         1  2                    −1          2
 yi∗ > 0 ⇒ contrainte primale i saturée : (Ax∗ )i = bi                               hi (x∗ ) = 0 ∀i                                                                  
 x∗          T ∗                                                                     gj (x∗ ) ≤ 0 ∀j                                                          AT b =
                                                                                                                                                                        9
    j (cj − (A y )j ) = 0                                                                                                                                               6
 yi∗ (bi − (Ax∗ )i ) = 0                                                             µ∗
                                                                                        j ≥ 0 ∀j                                                                                              
                                                                                                                                                                                          12     4
Variables d'écart : si > 0 ⇒ yi∗ = 0                                                  µ∗       ∗
                                                                                        j gj (x ) = 0 ∀j                                                        x∗ = (AT A)−1 AT b = 1 3  3
                                                                                                                                                                                             =
                                                                                                                                                                                                 1
Trouver dual depuis tableau nal : Lire valeurs y∗ dans ligne z sous colonnes        Cas à examiner : 2m combinaisons contraintes actives/inactives             === V. PIÈGES À ÉVITER ===
si                                                                                   Pour chaque cas : résoudre système KKT, vérier µj ≥ 0 et admissibilité    17. ERREURS FRÉQUENTES
4. OPTIMISATION EN ENTIERS                                                           === III. FORMULES ESSENTIELLES ===                                         Simplexe :
Méthode des coupes de Gomory :                                                       11. CALCUL DIFFÉRENTIEL                                                     Oublier de changer signe si bi < 0
(1) Résoudre relaxation continue                                                                             ∂f
                                                                                                                                                                 Choisir mauvais ratio (ignorer aik ≤ 0)
                                                                                                     

(2) Si solution entière ⇒ FIN                                                                         ∂x1 
                                                                                                      .                                                        Ne pas vérier si solution non bornée
(3) Sinon, choisir ligne avec xi non entier                                          Gradient : ∇f = 
                                                                                                      .. 
                                                                                                                                                               Dualité :
(4) Coupe :
              P
                {aij }xj + s = {bi } où {x} = x − ⌊x⌋                                                                                                          Confondre primal max et dual min
(5) Ajouter coupe au tableau et pivoter
                                                                                                             ∂f
                                                                                                            ∂xn                                                  Oublier y ≥ 0 dans le dual
Branch & Bound :                                                                     Dérivées usuelles :                                                         Complémentarité : si > 0 ⇒ yi = 0 (pas l'inverse !)
(1) Résoudre relaxation                                                               ∇(xT Ax) = (A + AT )x (si A symétrique : 2Ax)                            KKT :
                                                                                                                                                                 Signe Lagrangien : L = f + µj gj (pas −)
                                                                                                                                                                                                   P
(2) Si entier ou pire que borne ⇒ élaguer                                             ∇(bT x) = b                                                               µj ≥ 0 toujours ! (sinon solution invalide)
(3) Sinon brancher : xi ≤ ⌊x∗ i ⌋ et xi ≥ ⌈xi ⌉
                                            ∗
                                                                                      ∇(xT x) = 2x                                                              Vérier admissibilité gj (x∗ ) ≤ 0
=== II. OPTIMISATION NON LINEAIRE ===                                                 ∇(∥Ax − b∥2 ) = 2AT (Ax − b)                                              Test 2nd ordre sur K(x∗ ), pas Rn
5. CONDITIONS D'OPTIMALITÉ SANS CONTRAINTE                                           Hessiennes usuelles :                                                      Hessienne :
Point critique : ∇f (x∗ ) = 0                                                       H(xT Ax) = A + AT (si A sym. : 2A)                                        Critère Sylvester pour déf. nég. : (−1)k det(Hk ) > 0
Hessienne : Hf (x) = ∂x∂i ∂x
                            2f                                                        H(∥Ax − b∥2 ) = 2AT A                                                     Semi-dénie ̸= dénie (test non concluant)
                               j                                                     12. ALGÈBRE LINÉAIRE                                                       18. VÉRIFICATIONS RAPIDES
Test du second ordre :                                                               Valeurs propresP: det(A − λI) = 0                                          Solution trouvée :
 H dénie positive ⇒ minimum local strict                                           Trace : tr(A) = λi                                                          Réinjecter dans contraintes
 H dénie négative ⇒ maximum local strict                                           Déterminant : det(A) = Q λi                                                Vérier signes multiplicateurs
 H indénie ⇒ point selle                                                                                                                                       Comparer valeurs objectif (dualité)
                                                                                     Inverse 2 × 2 : A−1 = det(A)                                               Convexité :
                                                                                                                                                 
                                                                                                                         −b
 H semi-dénie ⇒ test non concluant                                                                          1     d
                                                                                                                              pour A = ac         b
Matrice dénie positive : Tous VP > 0 OU tous mineurs principaux > 0                                                −c    a                       d              f convexe + contraintes convexes ⇒ KKT susantes
Critère de Sylvester (déf. pos.) : det(H1 ) > 0, det(H2 ) > 0, ..., det(Hn ) > 0     Projection orthogonale : P = A(AT A)−1 AT                                   Min local = min global si f convexe
Critère déf. nég. : (−1)k det(Hk ) > 0 ∀k                                            Distance point-plan : d(x0 , {Ax = b}) = |Ax∥A∥
                                                                                                                                  0 −b|                         === VI. TABLEAUX RÉCAP ===
                                                                                                                                                                19. PASSAGE PRIMAL-DUAL
6. CONVEXITÉ                                                                         13. ASTUCES EXAMEN                                                          Primal             Dual
Fonction convexe : f (λx + (1 − λ)y) ≤ λf (x) + (1 − λ)f (y)                         Reconnaître un min/max :                                                     max cT x                      min bT y
Critère Hessienne : f convexe ⇔ Hf (x) semi-dénie positive ∀x                        Coecients négatifs ⇒ max probable                                         Contrainte i : aTi x ≤ bi     Variable yi ≥ 0
Propriété : Si f convexe, tout minimum local est global                               Forme −x2 ⇒ max                                                            Contrainte i : aTi x ≥ bi     Variable yi ≤ 0
Ensemble convexe : λx + (1 − λ)y ∈ C ∀x, y ∈ C , λ ∈ [0, 1]                           Forme x2 ou ∥...∥2 ⇒ min                                                   Contrainte i : aTi x = bi     Variable yi libre
Forme quadratique : f (x) = 12 xT Qx + bT x + c                                      Tester convexité rapide : Calculer H en un point, vérier VP ou mineurs      Variable xj ≥ 0               Contrainte j : (AT y)j ≥ cj
Convexe ⇔ Q semi-dénie positive                                                     KKT - énumérer cas :                                                         Variable xj ≤ 0               Contrainte j : (AT y)j ≤ cj
7. MOINDRES CARRÉS                                                                    2 contraintes ⇒ 4 cas : (0, 0), (1, 0), (0, 1), (1, 1)
                                                                                      Commencer par cas sans contraintes actives                                 Variable xj libre             Contrainte j : (AT y)j = cj
Problème : min 21 ∥Ax − b∥2                                                           Vérier µj ≥ 0 et gj (x∗ ) ≤ 0                                           20. NATURE POINTS CRITIQUES
Développement : f (x) = 12 xT AT Ax − bT Ax + 12 bT b                                Simplexe - trouver base initiale : Si bi < 0 ⇒ multiplier ligne par −1      Hessienne   Nature
Gradient : ∇f (x) = AT Ax − AT b                                                     Si pas de base évidente ⇒ méthode 2 phases                                   Déf. positive    Min local strict
                                                                                     === IV. EXEMPLES TYPES ===                                                   Déf. négative    Max local strict
Hessienne : Hf = AT A (semi-dénie positive)                                                                                                                      Semi-déf. pos.   Min local possible
Solution : Si AT A inversible : x∗ = (AT A)−1 AT b                                   14. EXEMPLE SIMPLEXE COMPLET                                                 Semi-déf. nég.   Max local possible
                                                                                     max(x1 + 2x2 ) s.c. −3x1 + 2x2 ≤ 2, −x1 + 2x2 ≤ 4, x1 + x2 ≤ 5
8. OPTIMISATION AVEC CONTRAINTES D'ÉGALITÉ                                           Forme standard : max z = x1 + 2x2                                            Indénie         Point selle
Problème : min f (x) s.c. hi (x) P
                                 = 0, i = 1, ..., p                                                                                                             Valeurs propres : Toutes > 0 : déf. pos. | Toutes < 0 : déf. nég.
Lagrangien : L(x, λ) = f (x) − pi=1 λi hi (x)                                                                          −3x1 + 2x2 + s1 = 2                      Toutes ≥ 0 : semi-déf. pos. | Signes mixtes : indénie
Conditions nécessaires (KKT) :                                                                                                                                  21. FORMULES CLÉS À RETENIR
 ∇x L(x∗ , λ∗ ) = 0 (stationnarité)
                                                                                                                        −x1 + 2x2 + s2 = 4                      Gradient forme quad. : ∇( 12 xT Qx + bT x) = Qx + b
 hi (x∗ ) = 0 ∀i (admissibilité)                                                                                           x1 + x2 + s3 = 5                    Projection : projC (x) = C(C T C)−1 C T x
~~~

## Page 2

~~~text
Distance : d(x0 , {h = 0}) = ∥∇h(x
                              |h(x0 )|
                                                             Exemple bon format :                                              (3) Convexe : H = AT A semi-déf. pos.
                                   0 )∥
                                                             "On calcule le gradient : ∇f (x) = (2x1 + x2 , −2x2 + x1 )        (4) Solution : x∗ = (AT A)−1 AT b
Plan tangent en qx0 : ∇h(x0 ) (x − x0 ) = 0
                              T
                                                             Point critique : ∇f
                                                                                (x ) =0 donne x = (0, 0)
                                                                                   ∗                ∗
                                                                                                                               (5) Application numérique
Norme : ∥x∥2 = x21 + ... + x2n                               Hessienne : H = 21 −2    1                                        Type 2 : KKT avec 2 contraintes (7-9 pts)
                                                                                                                               min f (x) s.c. g1 (x) ≤ 0, g2 (x) ≤ 0
Produit scalaire : ⟨x, y⟩ = xT y = P xi yi                   det(H) = −5 < 0 donc H indénie                                   (1) Lagrangien : L = f + µ1 g1 + µ2 g2
=== VII. STRATÉGIE EXAMEN ===                                Conclusion : (0, 0) est un point selle."                          (2) Points réguliers : vérier ∇g1 , ∇g2 lin. indép.
22. GESTION DU TEMPS                                         24. CAS PARTICULIERS EXAM                                         (3) Conditions KKT : écrire système
Lecture (5 min) :                                            Si "Optimiser" sans préciser :                                    (4) Énumérer 4 cas : résoudre, vérier µj ≥ 0 et admissibilité
 Identier types exos (simplexe, KKT, moindres carrés...)   Regarder fonction : coef. négatifs ou forme −x2 ⇒ max             (5) Test 2nd ordre et conclusion
 Noter barème et temps par exo                              Sinon calculer limite ∥x∥ → ∞ ou Hessienne                        Type 3 : Optimisation sans contrainte (5-6 pts)
Résolution (1h45) :                                          Si plusieurs solutions KKT :                                      (1) Points critiques : ∇f = 0
 Commencer par exos maîtrisés                               Calculer f (x) pour chaque, choisir min pour minimisation         (2) Nature : calculer H , VP ou Sylvester
 Questions indép. : faire celles qu'on sait                 Si demande "justier sans calcul" :                               (3) Min/max global : limite inni, convexité
 Si bloqué : passer et revenir                              Utiliser propriétés : convexité, théorème existence, unicité...   Type 4 : Simplexe + dual (6-7 pts)
Vérication (10 min) :                                       Si problème impossible :                                          (1) Résoudre primal par tableaux
 Relire calculs importants                                  Phase I donne min y > 0 ou contradictions contraintes             (2) Lire y ∗ dans tableau nal (ligne z , colonnes si )
 Vérier signes et contraintes                              === VIII. ANNALES TYPES ===                                       (3) Vérier dualité forte : cT x∗ = bT y ∗
23. RÉDACTION                                                25. EXOS RÉCURRENTS                                               26. PIÈGES EXAMENS PASSÉS
Ce qu'on attend :                                            Type 1 : Moindres carrés (5-7 pts)                                Exam 23-24 : Confusion min/max (regarder coef. fonction !)
                                                             min 1 ∥Ax − b∥2 avec A, b donnés
 Justier chaque étape                                          2                                                             Exam 24-25 : KKT avec point non régulier (vérier LICQ d'abord)
 Écrire formules avant calculs                              (1) Montrer quadratique : développer ∥Ax − b∥2                    Rattrapage 23-24 : Oubli λ > 0 dans convexité
 Conclure clairement                                        (2) Points critiques : ∇f = AT Ax − AT b = 0                      Courant : Simplexe avec phase I nécessaire, ne pas oublier étape
~~~
