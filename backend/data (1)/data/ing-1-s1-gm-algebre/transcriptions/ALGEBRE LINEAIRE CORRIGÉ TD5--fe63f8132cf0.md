# ALGEBRE LINEAIRE CORRIGÉ TD5.pdf

[Ouvrir l’original](https://drive.google.com/open?id=15fIW8Gk3Ta2XbvF8DcNFMVcr4D6VCBex) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                         Algèbre Linéaire Appliquée
                          Corrigé Détaillé du TD5
                  Méthodes directes (LU, Cholesky, Matrices creuses)

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
                                ln1 ln2 . . .     lnn      xn             bn

   La méthode utilisée est la descente (ou substitution avant).

   Point Pédagogique (Le "Pourquoi")

   Pourquoi cet algorithme ? On ne cherche pas à inverser la matrice L (trop coûteux).
   On exploite la structure : la première ligne ne contient qu’une seule inconnue (x1 ), la
   deuxième en contient deux (x1 , x2 ), etc. On peut donc calculer les inconnues une par
   une, dans l’ordre croissant des indices.

   Solution Détaillée

   Écrivons la ligne i du système :

                                  li1 x1 + li2 x2 + · · · + lii xi = bi

   On cherche à calculer xi . On suppose que x1 , . . . , xi−1 ont déjà été calculés aux étapes
   précédentes. On isole xi :
                                                                              
                                  i−1                               i−1
                                  X                        1       X
                    lii xi = bi −     lij xj =⇒ xi =           bi −     lij xj 
                                                          lii
                                  j=1                               j=1
                                  | {z }
                                  Termes connus

   Algorithme :
     Entrées : L (matrice n × n triangulaire inf.), b (vecteur taille n)
     Sortie : x (vecteur solution)


                                                   1
~~~

## Page 2

~~~text
for i allant de 1 à n do
    S←0
    for j allant de 1 à i − 1 do
        S ← S + Lij × xj                              ▷ Somme des termes déjà connus
    end for
    if Lii = 0 then
        Erreur : Matrice non inversible (pivot nul)
    else
        xi ← (bi − S)/Lii
    end if
end for




                                          2
~~~

## Page 3

~~~text
Exercice 23 : Factorisation LU et Pivotage
                                               
                                    0 3 1        1
Question : Résoudre Ax = b avec A = 4 1 1 et b = 5 par factorisation LU.
                                              
                                    2 2 4        6

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
                                                      
                                         4 1 1           5
                               P A = 0 3 1 , P b = 1
                                         2 2 4           6
                                              
                                       0 1 0
  La matrice de permutation est P = 1 0 0.
                                       0 0 1
  Étape 2 : Élimination de Gauss (Factorisation LU de PA)
     — Colonne 1 : Pivot = 4.
     — On veut annuler le 2 en position (3,1). Multiplicateur l31 = 24 = 0.5.
     — Opération : L3 ← L  3 − 0.5L1 =⇒ (2, 2, 4) − (2, 0.5, 0.5) = (0, 1.5, 3.5).
                              4 1     1
     — Matrice courante : 0 3        1 .
                              0 1.5 3.5
     — Colonne 2 : Pivot = 3.
     — On veut annuler le 1.5 en position (3,2). Multiplicateur l32 = 1.5 3 = 0.5.
     — Opération : L3 ← L3 − 0.5L2 =⇒ (0, 1.5, 3.5) − (0, 1.5, 0.5) = (0, 0, 3).
  Étape 3 : Construction de L et U
                                  
                           4 1 1
                    U = 0 3 1 (Matrice finale triangulaire sup.)
                           0 0 3
                          
                  1   0 0
              L= 0   1 0            (Diagonale de 1 et multiplicateurs stockés)
                 0.5 0.5 1
  Étape 4 : Résolution de LU x = P b On pose y = U x. On résout d’abord Ly = P b =
  (5, 1, 6)T (descente) :
      — y1 = 5
      — y2 = 1
      — y3 = 6 − 0.5(5) − 0.5(1) = 6 − 2.5 − 0.5 = 3
  On résout ensuite U x = y = (5, 1, 3)T (remontée) :


                                                3
~~~

## Page 4

~~~text
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




                                          4
~~~
