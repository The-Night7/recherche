# td5 corrigé possible_revu.pdf

[Ouvrir l’original](https://drive.google.com/open?id=11rTU4AsBdcBIjOn-1s-wdgD67PG1iwv5) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                        Algèbre Linéaire Appliquée
                         Corrigé Détaillé du TD5
                        Méthodes directes (Correction Officielle)

                                Pour les étudiants ING1-GM

                                        Année 2025-2026


Exercice 22 : Résolution d’un système triangulaire inférieur
Question : Écrire l’algorithme de résolution d’un système triangulaire inférieur Lx = b.

                                        Rappel du Cours
   Un système est dit triangulaire inférieur si tous les coefficients au-dessus de la diagonale
   sont nuls (lij = 0 si j > i). Le système s’écrit :
                                                       
                                  l11 0 . . . 0         x1        b1
                                l21 l22 . . . 0   x2   b2 
                                                  ..   ..  =  .. 
                                                       
                                ..     .. ..
                                .       .    .    .  .   . 
                               ln1 ln2 . . .    lnn       xn             bn

   La méthode utilisée est la descente (ou substitution avant).

   Solution Détaillée

   Écrivons la ligne i du système :

                                 li1 x1 + li2 x2 + · · · + lii xi = bi

   On cherche à calculer xi . On suppose que x1 , . . . , xi−1 ont déjà été calculés aux étapes
   précédentes. On isole xi :
                                                                             
                                   i−1                             i−1
                                   X                     1        X
                     lii xi = bi −     lij xj =⇒ xi =         bi −     lij xj 
                                                        lii
                                  j=1                                    j=1

   Algorithme :
     Entrées : L (matrice n × n triangulaire inf.), b (vecteur taille n)
     Sortie : x (vecteur solution)
     x1 ← b1 /l11
     for i allant de 2 à n do
         S←0
         for j allant de 1 à i − 1 do
              S ← S + lij × xj                               ▷ Somme des termes déjà connus
         end for
         if lii = 0 then
              Erreur : Matrice non inversible (pivot nul)


                                                  1
~~~

## Page 2

~~~text
        else
           xi ← (bi − S)/lii
        end if
     end for

  Point Pédagogique (Le "Pourquoi")

  Il est important de prévoir le cas où lii = 0 pour éviter une division par zéro, ce qui
  rendrait la matrice non inversible.


Exercice 23 : Factorisation LU et Pivotage
                                                  
                                     0 3 1          1
Question : Résoudre Ax = b avec A = 4 1 1 et b = 5 par factorisation LU.
                                     2 2 4          6

  Point Pédagogique (Le "Pourquoi")

  Problème critique : Regardez le coefficient a11 = 0. La méthode du pivot de Gauss (et
  donc la factorisation LU standard) nécessite de diviser par le pivot pour éliminer les
  termes sous la diagonale. Ici, on ne peut pas diviser par 0.
  Solution : Il faut effectuer un pivotage partiel, c’est-à-dire échanger la ligne 1 avec une
  autre ligne pour amener un coefficient non nul (et idéalement le plus grand possible en
  valeur absolue) sur la diagonale.

  Solution Détaillée

  Étape 1 : Permutation (Pivotage) On regarde la 1ère colonne : |0|, |4|, |2|. Le maximum
  est 4 (ligne 2). On échange L1 et L2 .
                                                             
                                         4 1 1                   5
                               P A = 0 3 1 , P b = 1
                                         2 2 4                   6
                                                 
                                           0 1 0
  La matrice de permutation est P = 1 0 0.
                                           0 0 1
  Étape 2 : Élimination de Gauss (Factorisation LU de PA)
      — Colonne 1 : Pivot = 4.
      — On veut annuler le 2 en position (3,1). Multiplicateur l31 = 24 = 0.5.
      — Opération : L3 ← L  3 − 0.5L1 =⇒    (2, 2, 4) − (2, 0.5, 0.5) = (0, 1.5, 3.5).
                               4 1        1
      — Matrice courante : 0 3           1 .
                               0 1.5 3.5
      — Colonne 2 : Pivot = 3.
      — On veut annuler le 1.5 en position (3,2). Multiplicateur l32 = 1.5    3 = 0.5.
      — Opération : L3 ← L3 − 0.5L2 =⇒ (0, 1.5, 3.5) − (0, 1.5, 0.5) = (0, 0, 3).
  Étape 3 : Construction de L et U
                                   
                            4 1 1
                      U = 0 3 1 (Matrice finale triangulaire sup.)
                            0 0 3


                                              2
~~~

## Page 3

~~~text
                          
                  1   0 0
              L= 0   1 0           (Diagonale de 1 et multiplicateurs stockés)
                 0.5 0.5 1
   Étape 4 : Résolution de LU x = P b On pose y = U x. On résout d’abord Ly = P b =
   (5, 1, 6)T (descente) :
       — y1 = 5
       — y2 = 1
       — y3 = 6 − 0.5(5) − 0.5(1) = 6 − 2.5 − 0.5 = 3
   On résout ensuite U x = y = (5, 1, 3)T (remontée) :
       — 3x3 = 3 =⇒ x3 = 1
       — 3x2 + x3 = 1 =⇒ 3x2 + 1 = 1 =⇒ 3x2 = 0 =⇒ x2 = 0
       — 4x1 + x2 + x3 = 5 =⇒ 4x1 + 0 + 1 = 5 =⇒ 4x1 = 4 =⇒ x1 = 1

   Conclusion
                                                                            
                                                          0       3        1       1
                                T
   La solution est x = (1, 0, 1) . Vérification : A · x = 4 · 1 + 1 · 0 + 1 · 1 = 5 = b.
                                                                           
                                                          2       2        4       6
   Correct.


Exercice 24 : Condition d’existence LU
                                                      
                                             1 1−ϵ 3
Question : Soit ϵ un réel quelconque et A = 2    2   2.
                                             3    6   4
   1. Déterminer les valeurs de ϵ pour lesquelles A admet une factorisation LU .
   2. Déterminer les valeurs de ϵ pour lesquelles A n’est pas inversible. Pour ces valeurs, A
      admet-elle une factorisation LU ?

                                       Rappel du Cours
   Théorème d’existence (Critère de Sylvester) : Une matrice carrée A admet une facto-
   risation LU (unique si A est inversible) si et seulement si tous ses mineurs principaux
   d’ordre 1 à n − 1 sont non nuls.

                         ∆k = det(A1:k,1:k ) ̸= 0    ∀k ∈ {1, . . . , n − 1}

   Solution Détaillée
   1. Existence de la factorisation LU Calculons les déterminants des sous-matrices princi-
   pales :
       — ∆1 = det(A  1 ) = 1 ̸=0 (Toujours vrai).
                      1 1−ϵ
       — ∆2 = det                 = 1(2) − 2(1 − ϵ) = 2 − 2 + 2ϵ = 2ϵ.
                      2    2
   La condition d’existence est ∆2 ̸= 0, soit ϵ ̸= 0.
   Dans ce cas, on peut calculer explicitement les coefficients de L et U par identification
   (algorithme de Doolittle) :
                                                                        
                            1       0   0              1 1−ϵ         3
                     L = 2         1   0  , U = 0       2ϵ       −4     
                                 3(1+ϵ)                                1+ϵ
                            3      2ϵ   1              0   0     −5 + 6 ϵ


                                                 3
~~~

## Page 4

~~~text
2. Inversibilité et cas singulier La matrice A est inversible si et seulement si det(A) ̸= 0.
On peut calculer le déterminant via la factorisation LU (produit des éléments diagonaux
de U ) :                                    
                                      6 + 6ϵ
              det(A) = 1 · 2ϵ · −5 +            = −10ϵ + 12 + 12ϵ = 2ϵ + 12
                                         ϵ
A n’est pas inversible (singulière) si 2ϵ + 12 = 0 =⇒ ϵ = −6.
Pour cette valeur ϵ = −6 :
   — La condition d’existence LU (ϵ ̸= 0) est bien vérifiée (−6 ̸= 0).
   — La factorisation existe donc, mais U aura un zéro sur sa diagonale. En remplaçant
       ϵ par −6 dans les formules ci-dessus :
                                                                 
                                 1     0    0           1    7    3
                           L = 2      1    0 , U = 0 −12 −4
                                 3 1.25 1               0    0    0


Conclusion
   — A admet une factorisation LU si et seulement si ϵ ̸= 0.
   — A est singulière (non inversible) si ϵ = −6. Dans ce cas précis, la factorisation LU
     existe tout de même.

Point Pédagogique (Le "Pourquoi")

Notez la distinction importante : une matrice peut être singulière (déterminant nul) et
pourtant admettre une factorisation LU (comme ici pour ϵ = −6). Ce qui empêche la
factorisation LU classique, c’est un pivot nul en cours de route (ici ∆2 = 0 si ϵ = 0), pas
un pivot nul à la toute fin.




                                             4
~~~

## Page 5

~~~text
Exercice 25 : Complexité de la factorisation LU
Question : Soit n un entier naturel non nul et A la matrice définie par A = (ij−1 )1≤i,j≤n .
    1. Modifier l’algorithme de factorisation LU pour compter le nombre d’opérations arith-
       métiques.
    2. Calculer ce nombre pour n ∈ {10, 20, 30, 40, 50, 60} et représenter le résultat graphique-
       ment.
    3. Retrouver l’ordre de complexité de la méthode.

   Point Pédagogique (Le "Pourquoi")

   Pourquoi cet exercice ? En théorie, la factorisation LU a une complexité de O(n3 ), ce qui
   signifie que le temps de calcul augmente de façon cubique avec la taille de la matrice
   (si n double, le temps est multiplié par 8). L’objectif est de vérifier cette loi théorique
   par l’expérience numérique. L’outil mathématique pour cela est le logarithme : si Ops ≈
   C · nk , alors log(Ops) ≈ k · log(n) + constante. On cherche donc une droite de pente k sur
   un graphique log-log.

   Solution Détaillée
   1. Implémentation et comptage Dans l’algorithme de Doolittle (vu à l’exercice 23), les
   opérations arithmétiques principales se trouvent dans la triple boucle imbriquée. On
   insère un compteur ‘compt += 2‘ à chaque opération élémentaire de type aik ← aik − aij ·
   ajk (une multiplication et une soustraction).
   2.    Résultats    expérimentaux      En     exécutant le    script   (par   exemple
   TD5-Exo23-DecoLU.py) pour les valeurs de n demandées, on obtient un tableau de
   valeurs croissant très rapidement.
   3. Analyse de la complexité Pour retrouver l’ordre, on trace le graphique en échelle
   logarithmique :
       — Axe X : log(n)
       — Axe Y : log(Nombre d’opérations)
   On observe que les points sont alignés sur une droite.
   En effectuant une régression linéaire sur ces points (par exemple avec
   scipy.stats.linregress en Python), on obtient l’équation de la droite :

                                           Y = aX + b

   Le coefficient directeur (la pente) a calculé par le programme est 3.

   Conclusion
   Puisque la pente de la droite en échelle log-log est 3, cela confirme expérimentalement
   que le nombre d’opérations croît comme n3 . La complexité de la factorisation LU est
   donc bien d’ordre cubique : O(n3 ).




                                                5
~~~

## Page 6

~~~text
Exercice 26 : Instabilité Numérique
                     1 1 + 5 · 10−16 3
                                       

Question : Soit A = 2       2       20.
                     3       6        4
   1. Vérifier que A est inversible et admet une factorisation LU.
   2. Calculer la factorisation LU avec l’algorithme "naïf" (sans pivot). Vérifier que A − LU ̸=
      0. Expliquer.
   3. Comparer avec le résultat obtenu via une bibliothèque robuste (Scipy).

  Point Pédagogique (Le "Pourquoi")

  Cet exercice illustre le danger des pivots petits (proches de zéro). Même si une matrice
  est théoriquement inversible, diviser par un nombre minuscule (10−15 ou 10−16 ) lors du
  calcul des pivots peut engendrer des erreurs d’arrondi catastrophiques. C’est pourquoi
  les algorithmes professionnels utilisent toujours des échanges de lignes (pivotage par-
  tiel) pour diviser par le plus grand nombre possible.

  Solution Détaillée
  1. Existence théorique : Le théorème d’existence requiert que les mineurs principaux
  soient non nuls.
      — ∆1 = 1 ̸=0.
                      1 1 + 5 · 10−16
                                      
      — ∆2 = det                        = 2 − 2(1 + 5 · 10−16 ) = 2 − 2 − 10−15 = −10−15 .
                      2        2
  ∆2 ̸= 0, donc mathématiquement, la factorisation LU existe.
  2. Résultat numérique (Algorithme sans pivot) : Le pivot à l’étape 2 est ≈ −10−15 . L’or-
  dinateur ne le considère pas comme nul (il est supérieur à l’epsilon machine ≈ 10−16 ),
  donc il effectue la division.
  Cependant, cela crée des termes gigantesques dans L et U . Le calcul numérique donne :
                                                                             
                         1       0       0             1      1           3
                 L ≈ 2          1       0 , U ≈ 0 −10−15              14 
                         3 −3.3 · 1015   1             0      0      4.7 · 1016

  Lorsqu’on vérifie le produit, on trouve une erreur massive sur le dernier coefficient :
                                                      
                                                0 0 0
                                    A − LU = 0 0 0 
                                                0 0 4

  Le coefficient 4 a été "perdu" dans les erreurs d’arrondi face aux nombres en 1016 .
  3. Résultat avec Scipy (Algorithme avec pivot) : La fonction scipy.linalg.lu effec-
  tue un pivotage partiel (P A = LU ). Elle échange la ligne 2 avec la ligne 3 pour utiliser le
  pivot 6 (au lieu de 10−15 ). On obtient des matrices L et U avec des coefficients de taille
  raisonnable, et l’erreur de reconstruction A − LU est proche de 0 (10−16 ).

  Conclusion
  La factorisation LU "naïve" est numériquement instable pour cette matrice. L’utilisation
  du pivotage partiel est indispensable pour garantir la précision des résultats.



                                               6
~~~

## Page 7

~~~text
Exercice 27 : Calcul de l’inverse
Question : Soit A une matrice inversible d’ordre n.
   1. Montrer qu’il existe un algorithme de complexité O(n3 ) pour calculer A−1 en utilisant la
      factorisation LU .
   2. Est-ce toujours possible si A admet une factorisation LU avec pivot partiel ?

                                       Rappel du Cours
   L’inverse d’une matrice A, notée X = A−1 , est l’unique matrice telle que AX = In . Si on
   note xj la j-ème colonne de X et ej la j-ème colonne de la matrice identité In (le vecteur
   avec un 1 à la ligne j et 0 ailleurs), alors l’équation matricielle AX = In se décompose en
   n systèmes linéaires indépendants :

                                 Axj = ej      pour j = 1, . . . , n

   Solution Détaillée

   1. Algorithme et Complexité (Cas LU standard) L’algorithme pour calculer A−1 se dé-
   roule en deux phases :
       — Phase 1 : Décomposition de la matrice (Faite 1 seule fois) On factorise A = L · U .
          Coût : ≈ 23 n3 opérations (terme dominant).
       — Phase 2 : Résolution des systèmes (Répétée n fois) Pour chaque colonne j de 1 à
          n, on cherche le vecteur xj solution de L(U xj ) = ej .
          — Descente : Résoudre Ly = ej . Coût ≈ n2 opérations.
          — Remontée : Résoudre U xj = y. Coût ≈ n2 opérations.
          Le coût pour une colonne est donc en O(n2 ). Pour les n colonnes de l’inverse, le
          coût total de cette phase est n × O(n2 ) = O(n3 ).
   Coût Total :
                             Total = O(n3 ) + O(n3 ) = O(n3 )
                                       | {z }       | {z }
                                    Factorisation   n Résolutions

   2. Cas du pivot partiel (P A = LU ) Si on utilise le pivotage, l’équation devient P Axj =
   P ej , soit LU xj = P ej .
       — La factorisation P A = LU a la même complexité O(n3 ).
       — La permutation du vecteur ej par P a un coût négligeable (O(n)).
       — La résolution des systèmes triangulaires reste en O(n2 ).
   Conclusion : Oui, c’est toujours possible et cela conserve la même complexité globale de
   O(n3 ).

   Point Pédagogique (Le "Pourquoi")

   Ce résultat est important : il montre que calculer l’inverse d’une matrice coûte "aussi
   cher" (en ordre de grandeur) que de résoudre un seul système via Gauss-Jordan, ou que
   de multiplier deux matrices. Cependant, en pratique, si l’on a besoin de résoudre Ax = b,
   on ne calcule jamais A−1 explicitement ; on préfère factoriser A puis résoudre, car c’est
   plus stable numériquement et 3 fois moins coûteux en opérations (le facteur constant
   devant n3 est plus petit).




                                                    7
~~~

## Page 8

~~~text
Exercice 28 : Matrices Creuses et Largeur de bande
Question : Soit A la matrice suivante :
                                                                    
                                      1   0   0    0    1   0   0   0
                                    0    1   1    0    0   1   0   1
                                                                    
                                    0    1   1    0    1   0   0   0
                                                                    
                                    0    0   0    1    0   0   1   0
                               A=  1
                                                                     
                                         0   1    0    1   0   0   0
                                                                     
                                    0    1   0    0    0   1   0   1
                                                                    
                                    0    0   0    1    0   0   1   1
                                      0   1   0    0    0   1   1   1
   1. Quelle est la largeur de bande de A ?
   2. Quelle est la nouvelle largeur de bande après application de l’algorithme de Cuthill-
      McKee ?
   3. Même question pour Cuthill-McKee inversé.

                                      Rappel du Cours
   La largeur de bande β d’une matrice A est l’écart maximal à la diagonale pour les coef-
   ficients non nuls :
                                     β = max |i − j|
                                              aij ̸=0

   Pour les matrices creuses (contenant beaucoup de zéros), on cherche à réduire β pour op-
   timiser le stockage et la rapidité des algorithmes (comme Cholesky ou LU). L’algorithme
   de Cuthill-McKee permet de renuméroter les indices pour concentrer les coefficients
   non nuls près de la diagonale.

   Solution Détaillée
   1. Largeur de bande initiale On examine les coefficients non nuls les plus éloignés de la
   diagonale :
       — Ligne 1 : a1,5 ̸= 0 =⇒ |1 − 5| = 4.
       — Ligne 2 : a2,8 ̸= 0 =⇒ |2 − 8| = 6.
       — Ligne 8 : a8,2 ̸= 0 =⇒ |8 − 2| = 6.
   La largeur de bande initiale est β = 6.
   2. Algorithme de Cuthill-McKee (CM) On modélise la matrice par un graphe dont les
   sommets sont les indices de 1 à 8.
   Calcul des degrés (nombre de voisins) :
       — Degré 1 : Sommets 1 (voisin 5) et 4 (voisin 7).
       — Degré 2 : Sommets 3, 5, 6, 7.
       — Degré 3 : Sommets 2, 8.
   Parcours en largeur (BFS) : On part du sommet de degré minimal (disons 1).
       1. Niveau 0 : {1}. (On numérote 1 → 1).
       2. Niveau 1 : Voisins de 1 → {5}. (On numérote 5 → 2).
       3. Niveau 2 : Voisins de 5 (non visités) → {3}. (On numérote 3 → 3).
       4. Niveau 3 : Voisins de 3 → {2}. (On numérote 2 → 4).
       5. Niveau 4 : Voisins de 2 → {6, 8}. On les trie par degré croissant : deg(6)=2,
          deg(8)=3. Ordre : 6 puis 8. (On numérote 6 → 5, 8 → 6).
       6. Niveau 5 : Voisins de 8 (non visités) → {7}. (On numérote 7 → 7).
       7. Niveau 6 : Voisins de 7 (non visités) → {4}. (On numérote 4 → 8).


                                                  8
~~~

## Page 9

~~~text
Nouvelle numérotation (Ordre R) : 1, 5, 3, 2, 6, 8, 7, 4.
Nouvelle largeur de bande : Calculons les écarts avec la nouvelle numérotation pour les
arêtes les plus critiques :
    — L’arête (2,8) relie le 4ème et le 6ème sommet dans la nouvelle liste : écart |4−6| = 2.
    — L’arête (1,5) relie le 1er et le 2ème : écart 1.
En vérifiant toutes les arêtes, l’écart maximal est 2. La nouvelle largeur de bande est
βCM = 2. (Gain considérable par rapport à 6).
3. Cuthill-McKee Inversé (RCM) On inverse simplement l’ordre obtenu :
4, 7, 8, 6, 2, 3, 5, 1. La largeur de bande reste 2, mais cette forme repousse souvent
les coefficients vers le "bas" de la bande, ce qui est avantageux pour le profil de la
matrice (stockage enveloppe).




                                             9
~~~
