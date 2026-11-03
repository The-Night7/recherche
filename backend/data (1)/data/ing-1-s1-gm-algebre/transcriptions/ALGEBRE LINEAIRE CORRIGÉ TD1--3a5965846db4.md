# ALGEBRE LINEAIRE CORRIGÉ TD1.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1fA3tHknaXaDz3a6rggJHpLnCP2g4i6iX) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                         Algèbre Linéaire Appliquée
                              Corrigé du TD1
                               CY Tech - ING1 Mathématiques

                                          2 octobre 2025


Exercice 1 : Calcul de normes vectorielles
  Question : Calculer les normes ||.||1 , ||.||2 , ||.||∞ du vecteur x = (1, 0, 1, −4)⊤ .

                                         Rappel du Cours
  Les p-normes pour un vecteur x = (x1 , ..., xn ) ∈ Rn sont définies dans le support de
  cours (Définition 1.2.6, page
                           Pn 16).
     — Norme 1 : ||x||1 = i=1 |xi |         qP
                                                  n    2
     — Norme 2 (euclidienne) : ||x||2 =           i=1 xi
     — Norme infinie : ||x||∞ = max1≤i≤n |xi |

  Solution Détaillée

  Pour le vecteur x = (1, 0, 1, −4)⊤ :
      1. Calcul de la norme 1 : On somme les valeurs absolues.

                           ||x||1 = |1| + |0| + |1| + | − 4| = 1 + 0 + 1 + 4 = 6

      2. Calcul de la norme 2 : On calcule la racine de la somme des carrés.
                              p                      √                √
                    ||x||2 = 12 + 02 + 12 + (−4)2 = 1 + 0 + 1 + 16 = 18
                                         √    √         √
         On peut simplifier le résultat : 18 = 9 × 2 = 3 2.
      3. Calcul de la norme infinie : On cherche le maximum des valeurs absolues.

                          ||x||∞ = max(|1|, |0|, |1|, | − 4|) = max(1, 0, 1, 4) = 4

  Conclusion
  Les normes du vecteur x sont :
     — ||x||1 = 6√
     — ||x||2 = 3 2
     — ||x||∞ = 4




                                                  1
~~~

## Page 2

~~~text
Exercice 2 : Normes matricielles de la matrice identité
      Question : Calculer la norme de In pour les normes matricielles |||.|||1 , |||.|||2 , |||.|||∞ et
|||.|||F .

                                             Rappel du Cours
   Les définitions des normes matricielles
                                       Pmsont données dans le chapitre 1 :
      — Norme 1 : |||A|||1 = maxj i=1 |aij | (max des sommes de colonnes) (page 20,
          formule 43).
      — Norme ∞ : |||A|||∞ = maxi nj=1 |aij | (max des sommes de lignes) (page 20,
                                         P
          formule 44).
      — Norme 2 (spectrale) : Pour une matrice A symétrique, |||A|||2 = ρ(A) (rayon
          spectral) (Théorème 1.3.5, page q  20).
                                               Pn             2
      — Norme de Frobenius : |||A|||F =           i,j=1 |aij | (Exemple 2, page 18).



   Solution Détaillée
   La matrice identité In a des 1 sur sa diagonale et des 0 ailleurs.
       1. Norme 1 : Chaque colonne de In contient un seul 1 et des 0. La somme des valeurs
          absolues de chaque colonne est donc 1. Le maximum est alors 1.
       2. Norme ∞ : De même, chaque ligne de In contient un seul 1. La somme des valeurs
          absolues de chaque ligne est donc 1. Le maximum est 1.
       3. Norme 2 : La matrice In est symétrique. Ses valeurs propres sont toutes égales à
          1. Son rayon spectral ρ(In ) est donc max |λi | = 1. D’après le Théorème 1.3.5, on
          a |||In |||2 = ρ(In ) = 1.
       4. Norme de Frobenius : On somme les carrés de tous les éléments. Il y a n éléments
          égaux à 1.                p                               √
                        |||In |||F = 12 + 12 + · · · + 12 (n fois) = n

   Conclusion
                                                                    √
   |||In |||1 = 1, |||In |||∞ = 1, |||In |||2 = 1 et |||In |||F =       n.




                                                        2
~~~

## Page 3

~~~text
Exercice 3 : Calcul de normes pour une matrice spécifique
                                                                                       
                                                                                   2 1 1
  Question : Calculer les normes |||.|||1 , |||.|||2 , |||.|||∞ de la matrice A = 2 3 2.
                                                                                   1 1 2

                                      Rappel du Cours
  Les définitions des normes matricielles subordonnées sont données dans le chapitre 1 du
  support de cours :
     — Norme 1 : |||A|||1 = max1≤j≤n m
                                            P
                                              i=1 |aij | (maximum de la somme des valeurs
         absolues des colonnes) (page 20, formule       43).
     — Norme ∞ : |||A|||∞ = max1≤i≤m nj=1 |aij | (maximum de la somme des valeurs
                                            P
         absolues des lignes) (page 20, formule
                                             p      44).
     — Norme 2 (spectrale) : |||A|||2 = ρ(AT A), où ρ(M ) est le rayon spectral de M
         (la plus grande de ses valeurs propres en module) (Théorème 1.3.5, page 20).

  Solution Détaillée
  Calcul de la norme 1 (Somme maximale des colonnes)
  On calcule la somme des valeurs absolues pour chaque colonne de la matrice A.
     — Colonne 1 : |2| + |2| + |1| = 5
     — Colonne 2 : |1| + |3| + |1| = 5
     — Colonne 3 : |1| + |2| + |2| = 5
  Le maximum de ces sommes est 5. Donc, |||A|||1 = 5.




  Calcul de la norme ∞ (Somme maximale des lignes)
  On calcule la somme des valeurs absolues pour chaque ligne de la matrice A.
     — Ligne 1 : |2| + |1| + |1| = 4
     — Ligne 2 : |2| + |3| + |2| = 7
     — Ligne 3 : |1| + |1| + |2| = 4
  Le maximum de ces sommes est 7. Donc, |||A|||∞ = 7.




  Calcul de la norme 2 (Norme spectrale)
     1. Calcul de la matrice AT A :
                                                    
                                                2 2 1
                                          AT = 1 3 1
                                                1 2 2
                                                      
                                   2 2 1   2 1 1     9 9 8
                           AT A = 1 3 1 2 3 2 = 9 11 9
                                   1 2 2   1 1 2     8 9 9

     2. Calcul du polynôme caractéristique de AT A : Soit B = AT A. On calcule




                                               3
~~~

## Page 4

~~~text
     P (λ) = det(B − λI).
                                         9−λ    9    8
                               P (λ) =    9  11 − λ  9
                                          8     9   9−λ
     En développant par rapport à la première ligne :

                           11 − λ  9     9  9     9 11 − λ
         P (λ) = (9 − λ)              −9       +8
                              9   9−λ    8 9−λ    8    9
              = (9 − λ)[(11 − λ)(9 − λ) − 81] − 9[9(9 − λ) − 72] + 8[81 − 8(11 − λ)]
              = (9 − λ)[λ2 − 20λ + 99 − 81] − 9[81 − 9λ − 72] + 8[81 − 88 + 8λ]
              = (9 − λ)(λ2 − 20λ + 18) − 9(9 − 9λ) + 8(−7 + 8λ)
              = (9λ2 − 180λ + 162 − λ3 + 20λ2 − 18λ) − (81 − 81λ) + (−56 + 64λ)
              = −λ3 + 29λ2 − 198λ + 162 − 81 + 81λ − 56 + 64λ
              = −λ3 + 29λ2 − 53λ + 25

   3. Recherche des valeurs propres (racines de P (λ)) : On remarque que λ = 1
      est une racine évidente car P (1) = −1 + 29 − 53 + 25 = 0. On peut donc factoriser
      P (λ) par (λ − 1) :
                               P (λ) = −(λ − 1)(λ2 − 28λ + 25)
     On résout l’équation du second degré λ2 − 28λ + 25 = 0. Le discriminant
                                                                        √         ∆=
                                                                              est √
     (−28)2 − 4(1)(25) = 784 −   100 = 684. Comme  684 =  36 × 19, on a   684 = 6   19.
                               √
                           28±6 19
                                            √                                 T
     Les racines sont λ =     2    = 14 ± 3 19. Les trois valeurs propres de A A sont
     donc :                                  √                  √
                        λ1 = 1, λ2 = 14 − 3 19, λ3 = 14 + 3 19

   4. Calcul du rayon spectral et de la norme 2 : Le rayon spectral est la plus grande
      valeur propre en module. Comme les valeurs propres d’une matrice symétrique
      définie positive (AT A l’est) sont positives, la plus grande est λ3 .
                                                                  √
                            ρ(AT A) = max(λ1 , λ2 , λ3 ) = 14 + 3 19

     La norme 2 est la racine carrée du rayon spectral :
                                                    √
                                             q
                                   |||A|||2 = 14 + 3 19

Conclusion
Les normes de la matrice A sont :
   — |||A|||1 = 5
   — |||A|||∞ =p 7
                        √      √
   — |||A|||2 = 14 + 3 19 ≈ 27.08 ≈ 5.20




                                          4
~~~

## Page 5

~~~text
Exercice 4 : Démonstration de la formule de la norme matricielle
infinie
                                                                                                Pn
  Question : Démontrer le résultat (43) du cours : |||A|||∞ = max1≤i≤m                           j=1 |aij |.

                                         Rappel du Cours
  Une norme matricielle |||.||| est dite subordonnée à une norme vectorielle ||.|| si elle est
  définie par :
                                                 ||Ax||
                            |||A||| = sup               = sup ||Ax||
                                       x∈Rn ,x̸=0 ||x||  ||x||=1

  Cette définition est donnée dans le Théorème 1.3.4 (page 19) du support de cours.
  Pour cet exercice, nous utilisons la norme vectorielle infinie ||.||∞ .

  Solution Détaillée
  La démonstration se fait en deux étapes :
      1. Montrer que |||A|||∞ ≤ max1≤i≤m nj=1 |aij |.
                                           P

      2. Montrer qu’il existe un vecteur x0 tel que ||x0 ||∞P= 1 pour lequel l’égalité est
         atteinte, ce qui prouvera que |||A|||∞ ≥ max1≤i≤m nj=1 |aij |.

  Étape 1 : Majoration de la norme
  Soit x ∈ Rn un vecteur quelconque. La i-ème composante du vecteur Ax est (Ax)i =
  P n
    j=1 aij xj .
  Calculons la norme infinie de Ax :
                                                                           n
                                                                           X
                            ||Ax||∞ = max |(Ax)i | = max                         aij xj
                                        1≤i≤m                 1≤i≤m
                                                                           j=1

  En utilisant l’inégalité triangulaire pour les nombres réels :
                               n
                               X                n
                                                X                   n
                                                                    X
                                     aij xj ≤         |aij xj | =         |aij ||xj |
                               j=1              j=1                 j=1

  Par définition de la norme infinie d’un vecteur, on a |xj | ≤ ||x||∞ pour tout j. On peut
  donc majorer la somme :
                                                                           
                      Xn               n
                                       X                           Xn
                         |aij ||xj | ≤   |aij | · ||x||∞ = ||x||∞    |aij |
                      j=1               j=1                                      j=1

  En combinant ces inégalités, on obtient :
                                                   
                                          X n                        n
                                                                     X
               ||Ax||∞ ≤ max ||x||∞          |aij | = ||x||∞ · max   |aij |
                              1≤i≤m                                              1≤i≤m
                                                j=1                                       j=1

  En divisant par ||x||∞ (pour x ̸= 0) et en prenant le supremum, on a :
                                                                            n
                                              ||Ax||∞        X
                             |||A|||∞ = sup           ≤ max    |aij |
                                          x̸=0 ||x||∞  1≤i≤m
                                                                           j=1




                                                       5
~~~

## Page 6

~~~text
Étape 2 : Atteindre la borne supérieure
Il faut maintenant prouver que cette borne est bien atteinte. Soit i0 l’indice de la ligne
pour laquelle la somme des valeurs absolues est maximale :
                                    n
                                    X                          n
                                                               X
                                            |ai0 j | = max           |aij |
                                                    1≤i≤m
                                    j=1                        j=1

Construisons un vecteur spécifique x0 ∈ Rn de norme ||x0 ||∞ = 1 de la manière suivante :
pour j = 1, . . . , n,                   (
                                          1   si ai0 j ≥ 0
                                (x0 )j =
                                          −1 si ai0 j < 0
Cette définition est équivalente à (x0 )j = sign(ai0 j ). Par construction, on a bien ||x0 ||∞ = 1
(sauf si la ligne i0 est nulle, auquel cas la norme de la matrice est 0 et le résultat est trivial).
Maintenant, calculons la i0 -ème composante de Ax0 :
                                                    n
                                                    X
                                      (Ax0 )i0 =          ai0 j (x0 )j
                                                    j=1

Par notre choix de x0 , chaque terme ai0 j (x0 )j est égal à |ai0 j |. Donc :
                                                         n
                                                         X
                                          (Ax0 )i0 =           |ai0 j |
                                                         j=1

La norme infinie de Ax0 est le maximum de ses composantes en valeur absolue. Elle est
donc au moins égale à la valeur absolue de sa i0 -ème composante :

                                                         n
                                                         X                    n
                                                                              X
                        ||Ax0 ||∞ ≥ |(Ax0 )i0 | =              |ai0 j | =           |ai0 j |
                                                         j=1                  j=1

Par définition de i0 , cela signifie :
                                                               n
                                                               X
                                    ||Ax0 ||∞ ≥ max                  |aij |
                                                    1≤i≤m
                                                               j=1

Puisque ||x0 ||∞ = 1, on a :
                                                                                      n
                                                                                      X
                   |||A|||∞ =     sup ||Ax||∞ ≥ ||Ax0 ||∞ ≥ max                                |aij |
                                ||x||∞ =1                                     1≤i≤m
                                                                                      j=1


Conclusion
Nous avons montré les deux P
                           inégalités :
   — |||A|||∞ ≤ max1≤i≤m Pnj=1 |aij |
   — |||A|||∞ ≥ max1≤i≤m nj=1 |aij |
On peut donc conclure que l’égalité est vérifiée :
                                                               n
                                                               X
                                     |||A|||∞ = max                  |aij |
                                                   1≤i≤m
                                                               j=1




                                                     6
~~~

## Page 7

~~~text
Exercice 4 : Démonstration de la formule de la norme matricielle
infinie
                                                                                            Pn
  Question : Démontrer le résultat (43) du cours : |||A|||∞ = max1≤i≤m                         j=1 |aij |.

                                           Rappel du Cours
  Une norme matricielle subordonnée est définie par |||A||| = sup||x||=1 ||Ax|| (Théorème
  1.3.4, page 19).

  Notations suggérées :
     — Notons Li (A) le i-ème vecteur-ligne de la matrice P A.
     — La norme 1 de ce vecteur-ligne est ||Li (A)||1 = nj=1 |aij |.
     — Posons L∗ (A)1 = max1≤i≤m ||Li (A)||1 .
  Avec ces notations, l’objectif est de démontrer que |||A|||∞ = L∗ (A)1 .

  Lemme (Inégalité de Hölder) : Pour deux vecteurs u, v ∈ Rn , on a |u·v| ≤ ||u||1 ·||v||∞ .

  Solution Détaillée

  Étape 1 : Montrer que |||A|||∞ ≤ L∗ (A)1
  Pour tout vecteur x de norme ||x||∞ = 1, la i-ème composante de Ax est le produit scalaire
  Li (A) · x. En appliquant le lemme de Hölder :

             |(Ax)i | = |Li (A) · x| ≤ ||Li (A)||1 · ||x||∞ = ||Li (A)||1 · 1 = ||Li (A)||1

  Cette inégalité est valable pour chaque composante i. On peut donc passer au maximum
  sur toutes les composantes :

                           ||Ax||∞ = max |(Ax)i | ≤ max ||Li (A)||1
                                          1≤i≤m                1≤i≤m

  Par définition de notre notation L∗ (A)1 , on a :

                                            ||Ax||∞ ≤ L∗ (A)1

  Ceci étant vrai pour tout vecteur x de norme 1, c’est aussi vrai pour le supremum :

                               |||A|||∞ =        sup ||Ax||∞ ≤ L∗ (A)1
                                              ||x||∞ =1



  Étape 2 : Montrer que |||A|||∞ ≥ L∗ (A)1
  Il faut prouver que cette borne supérieure est atteinte. Soit i0 l’indice de la ligne qui réalise
  le maximum, c’est-à-dire :
                                     ||Li0 (A)||1 = L∗ (A)1
  Construisons un vecteur x0 de norme ||x0 ||∞ = 1 dont les composantes (x0 )j sont définies
  par le signe des composantes de Li0 (A) = (ai0 ,1 , . . . , ai0 ,n ) :

                                            (x0 )j = sign(ai0 j )

  Calculons la i0 -ème composante de Ax0 :
                                    n
                                    X                              n
                                                                   X
        (Ax0 )i0 = Li0 (A) · x0 =         ai0 j · sign(ai0 j ) =         |ai0 j | = ||Li0 (A)||1 = L∗ (A)1
                                    j=1                            j=1



                                                       7
~~~

## Page 8

~~~text
La norme infinie de Ax0 est supérieure ou égale à la valeur absolue de n’importe laquelle
de ses composantes, donc en particulier pour la i0 -ème :

                             ||Ax0 ||∞ ≥ |(Ax0 )i0 | = L∗ (A)1

Puisque nous avons trouvé un vecteur x0 de norme 1 tel que ||Ax0 ||∞ ≥ L∗ (A)1 , le
supremum doit être au moins aussi grand :

                     |||A|||∞ =     sup ||Ax||∞ ≥ ||Ax0 ||∞ ≥ L∗ (A)1
                                  ||x||∞ =1


Conclusion
Les deux étapes nous ont permis de montrer que |||A|||∞ ≤ L∗ (A)1 et |||A|||∞ ≥ L∗ (A)1 .
On peut donc conclure à l’égalité :
                                                              n
                                                              X
                                              ∗
                           |||A|||∞ = L (A)1 = max                  |aij |
                                                      1≤i≤m
                                                              j=1




                                                  8
~~~

## Page 9

~~~text
Démonstration de la formule de la norme matricielle 1
                                                                                          Pm
  Question : Démontrer que pour A ∈ Rm×n , on a |||A|||1 = max1≤j≤n                         i=1 |aij |.

                                                Rappel du Cours
  Une norme matricielle subordonnée est définie par |||A||| = sup||x||=1 ||Ax|| (Théorème
  1.3.4, page 19).

  Notations suggérées :
     — Notons Cj (A) le j-ème vecteur-colonne de la matrice   PmA.
     — La norme 1 de ce vecteur-colonne est ||Cj (A)||1 = i=1 |aij |.
     — Posons C ∗ (A)1 = max1≤j≤n ||Cj (A)||1 .
  Avec ces notations, l’objectif est de démontrer que |||A|||1 = C∗ (A)1 .

  Solution Détaillée

  Étape 1 : Montrer que |||A|||1 ≤ C ∗ (A)1
  Soit x ∈ Rn . Le produit Ax peut s’écrire comme une combinaison linéaire des colonnes de
  A:
                                             Xn
                                      Ax =      xj Cj (A)
                                                            j=1

  Appliquons la norme 1 et utilisons l’inégalité triangulaire pour les vecteurs :

                            n
                            X
              ||Ax||1 =            xj Cj (A)
                            j=1
                                                1
                           n
                           X
                       ≤         ||xj Cj (A)||1                   (Par l’inégalité triangulaire)
                           j=1
                           Xn
                       =         |xj | · ||Cj (A)||1              (Par homogénéité de la norme)
                           j=1

  Par définition de C ∗ (A)1 , on sait que ||Cj (A)||1 ≤ C ∗ (A)1 pour tout j. On peut donc
  majorer la somme :
     n
     X                             n
                                   X
           |xj | · ||Cj (A)||1 ≤         |xj | · C ∗ (A)1
     j=1                           j=1
                                              n
                                              X
                                     ∗
                             = C (A)1               |xj |     (Mise en facteur de la constante C ∗ (A)1 )
                                              j=1
                                     ∗
                             = C (A)1 · ||x||1                (Par définition de la norme 1 de x)

  Nous avons donc montré que ||Ax||1 ≤ C ∗ (A)1 · ||x||1 . En passant au supremum pour
  ||x||1 = 1, on obtient :
                                  |||A|||1 ≤ C ∗ (A)1


  Étape 2 : Montrer que |||A|||1 ≥ C ∗ (A)1
  Il faut prouver que cette borne est atteinte. Soit j0 l’indice de la colonne qui réalise le
  maximum, c’est-à-dire :
                                   ||Cj0 (A)||1 = C ∗ (A)1



                                                              9
~~~

## Page 10

~~~text
Construisons le vecteur x0 comme étant le j0 -ème vecteur de la base canonique de Rn . Ses
composantes sont :                       (
                                           1 si j = j0
                                (x0 )j =
                                           0 si j ̸= j0
La norme de ce vecteur est clairement ||x0 ||1 = 1.
Calculons maintenant le produit Ax0 :
             n
             X
     Ax0 =     (x0 )j Cj (A) = 0 · C1 (A) + · · · + 1 · Cj0 (A) + · · · + 0 · Cn (A) = Cj0 (A)
             j=1

Le produit Ax0 est simplement la j0 -ème colonne de A.
Calculons la norme 1 de ce résultat :

                                     ||Ax0 ||1 = ||Cj0 (A)||1

Par définition de j0 , ceci est égal à C ∗ (A)1 . Nous avons donc trouvé un vecteur x0 de
norme 1 tel que :
                                     ||Ax0 ||1 = C ∗ (A)1
La norme subordonnée étant le supremum de ||Ax||1 pour tous les vecteurs de norme 1,
elle doit être au moins aussi grande que cette valeur particulière :

                        |||A|||1 = sup ||Ax||1 ≥ ||Ax0 ||1 = C ∗ (A)1
                                   ||x||1 =1


Conclusion
Les deux étapes nous ont permis de montrer que |||A|||1 ≤ C ∗ (A)1 et |||A|||1 ≥ C ∗ (A)1 .
On conclut donc à l’égalité :
                                                             m
                                                             X
                              |||A|||1 = C ∗ (A)1 = max            |aij |
                                                     1≤j≤n
                                                             i=1




                                                10
~~~

## Page 11

~~~text
Démonstration : Le produit Matrice-Vecteur comme Combinaison
Linéaire des Colonnes
   Propriété à démontrer : Pour une matrice A ∈ Rm×n et un vecteur x ∈ Rn , le produit
Ax est une combinaison linéaire des colonnes de A, où les coefficients sont les composantes de x.
                                                   n
                                                   X
                                            Ax =         xj Cj (A)
                                                   j=1


                                            Rappel du Cours
   Par définition du produit matriciel, la i-ème composante du vecteur résultant y = Ax est
   le produit scalaire de la i-ème ligne de A, notée Li (A), avec le vecteur x :
                                                          n
                                                          X
                                       yi = (Ax)i =             aij xj
                                                          j=1


   Solution Détaillée
   Partons de cette définition pour écrire le vecteur y = Ax dans son intégralité :
                                                                        
                               y1         a11 x1 + a12 x2 + · · · + a1n xn
                              y2   a21 x1 + a22 x2 + · · · + a2n xn 
                        y= . =
                                                                        
                                                         ..
                              ..  
                                                                           
                                                          .                
                              ym             am1 x1 + am2 x2 + · · · + amn xn

   Nous pouvons décomposer ce vecteur en une somme de vecteurs, en regroupant les termes
   selon chaque composante de x (c’est-à-dire x1 , x2 , . . . , xn ) :
                                                                         
                             a11 x1        a12 x2                      a1n xn
                            a21 x1   a22 x2                     a2n xn 
                       y =  .  +  .  + ··· +  . 
                                                                         
                            ..   ..                             .. 
                               am1 x1            am2 x2                  amn xn

   Maintenant, nous pouvons mettre en facteur le scalaire xj de chaque vecteur de la somme :
                                                                 
                               a11           a12                  a1n
                              a21         a22                a2n 
                      y = x1  .  + x2  .  + · · · + xn  . 
                                                                 
                                .
                              .              .
                                            .                    .
                                                                 . 
                              am1           am2                   amn

   On reconnaît que chaque vecteur de cette somme est une colonne de la matrice A :
                                                             
                                a11          a12              a1n
                               a21       a22             a2n 
                       y = x1  .  +x2  .  + · · · + xn  . 
                                                             
                               ..        ..              .. 
                                  am1                am2                   amn
                                | {z }             | {z }                | {z }
                                   C1 (A)           C2 (A)                Cn (A)




                                                     11
~~~

## Page 12

~~~text
Conclusion
Cette décomposition montre bien que le vecteur Ax est la somme des vecteurs colonnes
de A, chacun étant pondéré par la composante correspondante du vecteur x. On a donc
bien :
                                       Xn
                                  Ax =     xj Cj (A)
                                       j=1




                                        12
~~~

## Page 13

~~~text
Exercice 5 : Égalité entre la norme 1 et la norme infinie de la
transposée
  Question : Démontrer le résultat suivant pour toute matrice A ∈ Rm×n :

                                        |||A|||1 = |||AT |||∞

                                        Rappel du Cours
  Les définitions des normes matricielles 1 et infinie sont données dans le chapitre 1 du
  support de cours (page 20, formules 43 et 44).
     — Norme 1 : Pour A ∈ Rm×n , |||A|||1 = max1≤j≤n m
                                                           P
                                                              i=1 |aij |. C’est le maximum des
          sommes des valeurs absolues des éléments de chaque colonne. P
     — Norme ∞ : Pour une matrice B ∈ Rn×m , |||B|||∞ = max1≤i≤n m                 j=1 |bij |. C’est
          le maximum des sommes des valeurs absolues des éléments de chaque ligne.
  De plus, l’élément (i, j) de la matrice transposée AT est l’élément (j, i) de la matrice A :
  (AT )ij = aji .

  Solution Détaillée
  Le but est de montrer que la définition de la norme 1 de A coïncide avec celle de la norme
  ∞ de sa transposée AT .
      1. Partons de la définition de |||AT |||∞ :
         La matrice A est de taille m × n, donc sa transposée AT est de taille n × m. En
         appliquant la définition de la norme ∞ à la matrice AT , on obtient :
                                                           m
                                                           X
                                          T
                                      |||A |||∞ = max            |(AT )ij |
                                                   1≤i≤n
                                                           j=1


      2. Utilisons la relation entre les coefficients de A et AT :
         On sait que (AT )ij = aji . Remplaçons cela dans l’expression précédente :
                                                                m
                                                                X
                                              T
                                        |||A |||∞ = max               |aji |
                                                        1≤i≤n
                                                                j=1


      3. Interprétons l’expression obtenue :
         L’expression m
                       P
                         j=1 |aji | représente la somme des valeurs absolues des éléments de
         la i-ème colonne de la matrice A (l’indice de colonne i est fixe, et l’indice de ligne
         j varie de 1 à m).
         L’opération max1≤i≤n prend donc le maximum de ces sommes sur toutes les co-
         lonnes de A.
         Cette opération est exactement la définition de la norme 1 de la matrice A :
                                                               m
                                                               X
                                          |||A|||1 = max             |aij |
                                                       1≤j≤n
                                                               i=1

         En changeant simplement les noms des indices (en remplaçant j par i et i par j),
         on voit que les deux expressions sont identiques.




                                                  13
~~~

## Page 14

~~~text
Conclusion
Nous avons montré que :
                                   m
                                   X                     X
               |||AT |||∞ = max          |aji | = max            |élément| = |||A|||1
                           1≤i≤n               colonne
                                   j=1                   ligne

L’égalité est donc démontrée.




                                               14
~~~

## Page 15

~~~text
Exercice 6 : Vrai ou Faux
   Question : Pour chacune des affirmations ci-dessous, dire si elle est vraie ou fausse et justifier.

1. Si A et B sont deux matrices carrées de même taille, on a |||A|||1 · |||B|||1 =
|||AB|||1
  Réponse : FAUX

                                     L’affirmation est fausse.

  Solution Détaillée
  Justification :
  La propriété générale pour les normes matricielles est la sous-multiplicativité, qui sti-
  pule que |||AB||| ≤ |||A||| · |||B||| (voir Définition 1.3.3, page 18 du cours). L’égalité
  n’est pas garantie et est même rare en pratique. Pour prouver que l’affirmation est fausse,
  il suffit de fournir un contre-exemple.

  Contre-exemple :                         
                            1 3           1 1
  Soient les matrices A =         et B =        .
                            2 4           1 1
      — Calculons |||A|||1 (max des sommes de colonnes) :

                            |||A|||1 = max(|1| + |2|, |3| + |4|) = max(3, 7) = 7

      — Calculons |||B|||1 :

                            |||B|||1 = max(|1| + |1|, |1| + |1|) = max(2, 2) = 2

      — Le produit des normes est donc :

                                       |||A|||1 · |||B|||1 = 7 × 2 = 14

      — Calculons maintenant le produit matriciel AB :
                                                          
                              1 3     1 1         1+3 1+3    4 4
                      AB =                  =              =
                              2 4     1 1         2+4 2+4    6 6

      — Et la norme de AB :

                                 |||AB|||1 = max(|4| + |6|, |4| + |6|) = 10

  On constate que 10 ̸= 14. L’affirmation est donc fausse.


2. Si A et B sont deux matrices carrées de même taille, on a |||AB|||2 ≤ |||A|||2 ·
|||B|||2
  Réponse : VRAI

                                     L’affirmation est vraie.




                                                 15
~~~

## Page 16

~~~text
  Solution Détaillée
  Justification :
  Cette inégalité est la définition même de la sous-multiplicativité. Le Théorème 1.3.6
  (page 21) du support de cours stipule que toute norme matricielle subordonnée à une
  norme vectorielle est sous-multiplicative.
  La norme 2, |||.|||2 , est une norme subordonnée (elle est induite par la norme vectorielle
  euclidienne, comme indiqué dans l’Exemple 3, page 19). Par conséquent, elle vérifie la
  propriété de sous-multiplicativité.


3. Pour toute matrice A de Rn×n , il existe un x ∈ Rn et une norme vectorielle
notée ||.|| tels que |||A|||F = ||Ax||
                                 ||x||

  Réponse : FAUX

                                  L’affirmation est fausse.

  Solution Détaillée
  Justification :
  L’affirmation implique que la norme de Frobenius (|||.|||F ) serait une norme subordonnée.
  Une norme subordonnée est définie par |||A||| = supx̸=0 ||Ax||
                                                            ||x|| .
  Cependant, le Théorème 1.3.6 (page 21) du cours énonce une propriété fondamentale
  de toutes les normes subordonnées : la norme de la matrice identité est toujours égale à 1.

                                          |||In ||| = 1

  Vérifions si la norme de Frobenius respecte cette condition. Comme nous l’avons calculé
  dans l’exercice 2 :                               √
                                        |||In |||F = n
            √
  Puisque n ̸= 1 pour tout n > 1, la norme de Frobenius ne vérifie pas une propriété
  essentielle des normes subordonnées. Elle ne peut donc pas être définie par la relation
  ||Ax||
   ||x|| pour une norme vectorielle donnée.




                                               16
~~~

## Page 17

~~~text
Exercice 7 : Étude de la matrice Aα
                                          
                                    α 1 0
   Question : Pour la matrice Aα =  1 α 1 , répondre aux questions suivantes.
                                     0 1 α

1. Quelles sont les valeurs propres de la matrice Aα ?
                                     Rappel du Cours
  Les valeurs propres d’une matrice A sont les scalaires λ tels que Ax = λx pour un vecteur
  non nul x (Définition 1.1.18, page 11). Elles sont les racines du polynôme caractéris-
  tique pA (λ) = det(A − λI) = 0 (Proposition 1.1.20, page 11).

  Solution Détaillée
  On calcule le déterminant de Aα − λI :

                                               α−λ  1   0
                           det(Aα − λI) =       1  α−λ  1
                                                0   1  α−λ

  En développant par rapport à la première ligne :

                                            α−λ      1         1  1
                   det(Aα − λI) = (α − λ)                  −1·
                                              1    α−λ         0 α−λ
                                                   2
                                                         
                                  = (α − λ) (α − λ) − 1 − (α − λ)
                                  = (α − λ) (α − λ)2 − 1 − 1
                                                           

                                  = (α − λ) (α − λ)2 − 2
                                                        


  On cherche les racines de ce polynôme :
     — α − λ = 0 =⇒ λ1 = α                √         √
     — (α − λ)2 − 2 = 0 =⇒ α − λ = ± 2 =⇒ λ2,3 = α ∓ 2

  Conclusion
                                          √               √
  Les valeurs propres de Aα sont α, α −       2, et α +       2.


2. Pour quelles valeurs de α, la matrice Aα est-elle inversible ?
                                     Rappel du Cours
  Une matrice carrée est inversible si et seulement si son déterminant est non nul (Propo-
  sition 1.1.12, page 9). De plus, le déterminant est égal au produit des valeurs propres
  (Proposition 1.1.21, page 11). Une matrice est donc inversible si et seulement si 0
  n’est pas une de ses valeurs propres.

  Solution Détaillée
  La matrice Aα n’est pas inversible si l’une de ses valeurs propres est nulle.
     — λ1 = 0 ⇐⇒ √ α=0               √
     — λ2 = α − √2 = 0 ⇐⇒ α = √         2
     — λ3 = α + 2 = 0 ⇐⇒ α = − 2


                                                17
~~~

## Page 18

~~~text
   Pour que Aα soit inversible, il faut donc que α soit différent de ces trois valeurs.

   Conclusion
                                                    √     √
   La matrice Aα est inversible pour tout α ∈ R \ {− 2, 0, 2}.


3. Calculer les normes |||Aα |||1 , |||Aα |||2 et |||Aα |||∞
   Solution Détaillée
       1. Norme 1 (Somme max des colonnes) :
          — Somme colonne 1 : |α| + |1| + |0| = |α| + 1
          — Somme colonne 2 : |1| + |α| + |1| = |α| + 2
          — Somme colonne 3 : |0| + |1| + |α| = |α| + 1
                           |||Aα |||1 = max(|α| + 1, |α| + 2) = |α| + 2

       2. Norme ∞ (Somme max des lignes) : La matrice Aα est symétrique, donc sa
          norme ∞ est égale à sa norme 1.

                                            |||Aα |||∞ = |α| + 2

       3. Norme 2 (Norme spectrale) : Puisque Aα est une matrice symétrique, sa norme
          2 est égale à son rayon spectral (Théorème 1.3.5, page 20).

                                |||Aα |||2 = ρ(Aα ) = max(|λ1 |, |λ2 |, |λ3 |)
                                                          √             √
                                           = max(|α|, |α − 2|, |α + 2|)

   Conclusion
      — |||Aα |||1 = |α| + 2
      — |||Aα |||∞ = |α| + 2      √        √
      — |||Aα |||2 = max(|α|, |α − 2|, |α + 2|)




                                                 18
~~~
