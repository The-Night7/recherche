# ALGEBRE TD1 correction.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1TISq0_ts7xd1Smd43EQvCzOggegO8zBH) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Correction des Exercices
Exercice 1 : Calcul de Normes Vectorielles
Énoncé : Calculer les normes 1, 2, et ∞ du vecteur x = (1, 0, 1, −4)T .


Rappel de Cours : Normes Vectorielles
Une norme sur un espace vectoriel est une fonction qui associe à chaque vecteur une
longueur. Pour un vecteur v = (v1 , v2 , . . . , vn ) ∈ Rn , les normes usuelles sont :

   • La norme 1 (∥ · ∥1 ) : C’est la somme des valeurs absolues des composantes du
     vecteur.                                n
                                             X
                                      ∥v∥1 =   |vi |
                                                i=1

   • La norme 2 (∥ · ∥2 ) : C’est la norme euclidienne, qui correspond à la longueur
     "habituelle" du vecteur.               v
                                            u n
                                            uX
                                     ∥v∥2 = t     vi2
                                                   i=1


   • La norme infinie (∥ · ∥∞ ) : C’est la plus grande des valeurs absolues des com-
     posantes.
                                   ∥v∥∞ = max |vi |
                                               i=1,...,n




Solution de l’Exercice 1
                     
                      1
                    0
Soit le vecteur x = 
                     1 .
                        

                      −4

  1. Calcul de la norme 1 : On somme les valeurs absolues des composantes de x.

                      ∥x∥1 = |1| + |0| + |1| + | − 4| = 1 + 0 + 1 + 4 = 6

     Le résultat est donc ∥x∥1 = 6.

  2. Calcul de la norme 2 : On calcule la racine carrée de la somme des carrés des
     composantes.
                          p                       √              √
                 ∥x∥2 = 12 + 02 + 12 + (−4)2 = 1 + 0 + 1 + 16 = 18
                                   √     √          √
     On peut simplifier la racine : 18
                                     √ =   9 × 2 = 3  2.
     Le résultat est donc ∥x∥2 = 3 2.



                                           1
~~~

## Page 2

~~~text
   3. Calcul de la norme infinie : On cherche la plus grande valeur absolue parmi les
      composantes.

                       ∥x∥∞ = max(|1|, |0|, |1|, | − 4|) = max(1, 0, 1, 4) = 4

      Le résultat est donc ∥x∥∞ = 4.




Exercice 2 : Calcul de Normes Matricielles
Énoncé : Calculer la norme de In pour les normes matricielles ||| · |||1 , ||| · |||2 , ||| · |||∞
et ∥ · ∥F .


Rappel de Cours : Normes Matricielles
Pour une matrice A ∈ Rm×n avec des coefficients aij , les normes principales sont :

   • La norme 1 (||| · |||1 ) : Maximum de la somme des valeurs absolues des éléments
     de chaque colonne.
                                                  m
                                                  X
                                   |||A|||1 = max   |aij |
                                                 j=1,...,n
                                                                i=1

   • La norme infinie (||| · |||∞ ) : Maximum de la somme des valeurs absolues des
     éléments de chaque ligne.
                                                                n
                                                                X
                                      |||A|||∞ = max                  |aij |
                                                    i=1,...,m
                                                                j=1


   • La norme 2 ou spectrale (||| · |||2 ) : Racine carrée de la plus grande valeur propre
     de AT A.                                 p
                               |||A|||2 = λmax (AT A)

   • La norme de Frobenius (∥ · ∥F ) : Racine carrée de la somme des carrés de tous
     les éléments.                     v
                                       u m X   n
                                       uX
                             ∥A∥F =    t         |aij |2
                                                      i=1 j=1




Solution de l’Exercice 2
On considère la matrice identité In .

   1. Calcul de la norme 1 : Chaque colonne de In contient un seul ’1’. La somme des
      valeurs absolues pour chaque colonne est donc 1.
                                         X
                        |||In |||1 = max   |(In )ij | = max(1, 1, . . . , 1) = 1
                                      j
                                           i


                                                2
~~~

## Page 3

~~~text
   2. Calcul de la norme infinie : Chaque ligne de In contient un seul ’1’. La somme
      des valeurs absolues pour chaque ligne est donc 1.
                                        X
                       |||In |||∞ = max   |(In )ij | = max(1, 1, . . . , 1) = 1
                                        i
                                             j


   3. Calcul de la norme 2 (spectrale) : On calcule InT In = In × In = In . Les valeurs
      propres de In sont toutes égales à 1. La plus grande valeur propre, λmax (In ), est
      donc 1.                      p                p            √
                       |||In |||2 = λmax (InT In ) = λmax (In ) = 1 = 1

   4. Calcul de la norme de Frobenius : La matrice In a n éléments égaux à 1 sur
      sa diagonale et des 0 partout ailleurs.
                             v
                             u n X  n
                                                                             √
                             uX                     s
                    ∥In ∥F = t          |(In )ij | = 1| 2 + 12 +
                                                  2                       2
                                                               {z· · · + 1} = n
                                   i=1 j=1                        n fois



Exercice 3 : Calcul de Normes Matricielles
Énoncé : Calculer les normes ||| · |||1 , ||| · |||2 , ||| · |||∞ de la matrice
                                                           
                                               2 1 1
                                   A = 2 3 2
                                               1 1 2


Solution de l’Exercice 3
   1. Calcul de la norme 1 (|||A|||1 )
      Cette norme est la somme maximale des valeurs absolues par colonne.

         • Colonne 1 : |2| + |2| + |1| = 5
         • Colonne 2 : |1| + |3| + |1| = 5
         • Colonne 3 : |1| + |2| + |2| = 5

      Le maximum de ces sommes est 5.

                                       |||A|||1 = max(5, 5, 5) = 5

   2. Calcul de la norme infinie (|||A|||∞ )
      Cette norme est la somme maximale des valeurs absolues par ligne.

         • Ligne 1 : |2| + |1| + |1| = 4
         • Ligne 2 : |2| + |3| + |2| = 7
         • Ligne 3 : |1| + |1| + |2| = 4

      Le maximum de ces sommes est 7.

                                       |||A|||∞ = max(4, 7, 4) = 7

                                                  3
~~~

## Page 4

~~~text
  3. Calcul de la norme 2 (|||A|||2 )
     La norme 2 (norme spectrale) est |||A|||2 = λmax (AT A). Cependant, la matrice
                                                p

     A est symétrique (A = AT ). Dans ce cas particulier, la norme 2 est simplement
     égale au rayon spectral de A, noté ρ(A), qui est le maximum des valeurs absolues
     de ses valeurs propres.
      Nous devons donc calculer les valeurs propres de A en résolvant l’équation carac-
      téristique det(A − λI) = 0.
                                                      
                                    2−λ      1      1
                               det  2     3−λ      2 =0
                                      1      1    2−λ
      En développant le déterminant :
           0 = (2 − λ) [(3 − λ)(2 − λ) − 2] − 1 [2(2 − λ) − 2] + 1 [2 − (3 − λ)]
             = (2 − λ)(λ2 − 5λ + 4) − (4 − 2λ − 2) + (2 − 3 + λ)
             = (2 − λ)(λ − 1)(λ − 4) − (2 − 2λ) + (λ − 1)
             = (2 − λ)(λ − 1)(λ − 4) + 2(λ − 1) + (λ − 1)
             = (λ − 1) [(2 − λ)(4 − λ) + 2 + 1]
             = (λ − 1) 8 − 6λ + λ2 + 3
                                       

             = (λ − 1)(λ2 − 6λ + 11) Erratum dans le calcul manuel, reprenons :
             = (λ − 1) [(2 − λ)(4 − λ) + 3] = (λ − 1)[λ2 − 6λ + 8 + 3] ̸= 0
            Correction du développement :
             = (λ − 1) [−(λ − 2)(λ − 4) + 3]
             = (λ − 1)[−(λ2 − 6λ + 8) + 3] = (λ − 1)(−λ2 + 6λ − 5)
             = −(λ − 1)(λ2 − 6λ + 5) = −(λ − 1)(λ − 1)(λ − 5) = −(λ − 1)2 (λ − 5)
      L’équation caractéristique est donc −(λ − 1)2 (λ − 5) = 0. Les valeurs propres de A
      sont λ1 = 5 (multiplicité 1) et λ2 = 1 (multiplicité 2).
      Le rayon spectral est ρ(A) = max(|λi |) = max(|5|, |1|) = 5. Puisque A est symétrique,
      sa norme 2 est égale à son rayon spectral.
                                           |||A|||2 = 5




Exercice 4 : Démonstration de la Norme Infinie
Énoncé : Démontrer le résultat : |||A|||∞ = maxi=1,...,m
                                                            Pn
                                                               j=1 |aij |.




Démonstration
Par définition, la norme matricielle induite par la norme vectorielle infinie est :
                                         ∥Ax∥∞
                          |||A|||∞ = sup       = sup ∥Ax∥∞
                                     x̸=0 ∥x∥∞  ∥x∥∞ =1

La preuve se fait en deux temps.

                                             4
~~~

## Page 5

~~~text
Étape 1 : Montrer que |||A|||∞ ≤ maxi Pj |aij | Soit x ∈ Rn tel que ∥x∥∞ = 1. Soit
                                         P
y = Ax. La i-ème composante de y est yi = nj=1 aij xj . Regardons la norme de y = Ax :
                                                                          n
                                                                          X
                           ∥Ax∥∞ = max |yi | = max                                  aij xj
                                         i=1,...,m                   i
                                                                              j=1

Par l’inégalité triangulaire :
                            n
                            X                 n
                                              X                          n
                                                                         X
                                  aij xj ≤              |aij xj | =            |aij ||xj |
                            j=1               j=1                        j=1


Puisque ∥x∥∞ = 1, on a |xj | ≤ 1 pour tout j. Ainsi :
                            n
                            X                     n
                                                  X                            n
                                                                               X
                                  |aij ||xj | ≤             |aij | × 1 =             |aij |
                            j=1                       j=1                      j=1


Donc, pour n’importe quelle ligne i : |yi | ≤                                        Le maximum de |yi | est donc
                                                                Pn
                                                                   j=1 |aij |.
majoré par le maximum de ces sommes :
                                                                          n
                                                                          X
                             ∥Ax∥∞ = max |yi | ≤ max                             |aij |
                                                  i                  i
                                                                          j=1

Comme ceci est vrai pour tout vecteur x de norme 1, le supremum l’est aussi :
                                                                                n
                                                                                X
                          |||A|||∞ = sup ∥Ax∥∞ ≤ max                                   |aij |
                                        ∥x∥∞ =1                           i
                                                                                j=1


Étape 2 : Montrer qu’il existe un vecteur x0 qui atteint cette     P borne Nous
devons maintenant prouver que l’égalité est possible. Soit M = maxi nj=1 |aij |. Soit i0
l’indice de la ligne où ce maximum est atteint :
                                             n
                                             X
                                                      |ai0 j | = M
                                             j=1

Construisons un vecteur spécifique x0 ∈ Rn dont les composantes sont définies par :
                                                (
                                                 1  si ai0 j ≥ 0
                         (x0 )j = sgn(ai0 j ) =
                                                 −1 si ai0 j < 0

Par construction, ∥x0 ∥∞ = maxj |(x0 )j | = 1. Calculons la i0 -ème composante du vecteur
Ax0 :
                                   n
                                   X                 n
                                                     X
                        (Ax0 )i0 =    ai0 j (x0 )j =   ai0 j sgn(ai0 j )
                                       j=1                         j=1

Par définition de la fonction signe, a × sgn(a) = |a|. Donc :
                                                        n
                                                        X
                                     (Ax0 )i0 =                 |ai0 j | = M
                                                        j=1


                                                            5
~~~

## Page 6

~~~text
La norme ∥Ax0 ∥∞ est le maximum des valeurs absolues des composantes de Ax0 . Elle est
donc au moins aussi grande que la valeur absolue de sa i0 -ème composante :

                                ∥Ax0 ∥∞ ≥ |(Ax0 )i0 | = M

En combinant avec le résultat de l’Étape 1 (|||A|||∞ ≤ M ), nous avons :

                             M ≤ ∥Ax0 ∥∞ ≤ |||A|||∞ ≤ M

Cela implique que toutes ces valeurs sont égales.
                                                              n
                                                              X
                             |||A|||∞ = M = max                     |aij |
                                                  i=1,...,m
                                                              j=1


Ce qui conclut la démonstration.

Exercice 5 : Démonstration d’une Propriété de Norme
Énoncé : Démontrer le résultat suivant pour toute matrice A ∈ Rm×n :

                                     |||A|||1 = |||AT |||∞



Démonstration
La preuve repose sur la simple application des définitions des normes matricielles 1 et ∞.

  1. Définition de la norme 1 pour A
     La norme 1 d’une matrice A ∈ Rm×n est le maximum de la somme des valeurs
     absolues des éléments de chaque colonne.
                                                      m
                                                      X
                                   |||A|||1 = max             |aij | (∗)
                                             1≤j≤n
                                                       i=1


  2. Définition de la norme infinie pour AT
     Soit B = AT . B est une matrice de taille n × m où l’élément bij est égal à aji . La
     norme infinie de B est le maximum de la somme des valeurs absolues des éléments
     de chaque ligne.
                                                        m
                                                        X
                                            T
                             |||B|||∞ = |||A |||∞ = max     |bij |
                                                              1≤i≤n
                                                                      j=1

     En remplaçant bij par aji , on obtient :
                                                       m
                                                       X
                                     T
                                |||A |||∞ = max               |aji | (∗∗)
                                              1≤i≤n
                                                       j=1




                                              6
~~~

## Page 7

~~~text
  3. Comparaison
     L’expression (∗∗) calcule la somme sur l’indice j des termes |aji |. Pour un i fixé,
     cela correspond à la somme des éléments de la i-ème colonne de la matrice A. On
     prend ensuite le maximum sur toutes les colonnes (indexées ici par i).
    L’expression (∗) calcule la somme sur l’indice i des termes |aij |. Pour un j fixé, cela
    correspond à la somme des éléments de la j-ème colonne de la matrice A. On prend
    ensuite le maximum sur toutes les colonnes (indexées par j).
    Les deux expressions calculent donc exactement la même chose : le maximum de la
    somme des valeurs absolues des colonnes de A.
    Par conséquent, |||A|||1 = |||AT |||∞ .




Exercice 6 : Vrai ou Faux
  1. Affirmation : Si A et B sont deux matrices carrées de même taille, on a |||A|||1 ·
     |||B|||1 = |||AB|||1 .


    Réponse : FAUX Les normes matricielles induites sont sous-multiplicatives,
    ce qui signifie que la propriété générale est |||AB|||1 ≤ |||A|||1 · |||B|||1 . L’égalité
    n’est pas toujours vraie.

                                                             
                                                          0 2
    Contre-exemple : Soit la matrice A =                       . Calculons sa norme 1 :
                                                          0 0

                      |||A|||1 = max(|0| + |0|, |2| + |0|) = max(0, 2) = 2

    Calculons A2 :
                                              
                          2      0 2   0 2     0 0
                        A =A·A=             =        =O
                                 0 0   0 0     0 0

    La norme de la matrice nulle est :

                                              |||A2 |||1 = 0

    Comparons les deux termes :

                                  |||A|||1 · |||A|||1 = 2 × 2 = 4

    On a bien |||A2 |||1 = 0 ̸= 4 = (|||A|||1 )2 . L’affirmation est donc fausse.

  2. Affirmation : Si A et B sont deux matrices carrées de même taille, on a |||AB|||2 ≤
     |||A|||2 · |||B|||2 .


    Réponse : VRAI C’est la propriété de sous-multiplicativité qui est vraie pour
    toutes les normes matricielles induites, y compris la norme 2.

                                                7
~~~

## Page 8

~~~text
     Démonstration : Par définition, |||M |||2 = supx̸=0 ∥M x∥2
                                                          ∥x∥2
                                                                . Ainsi, pour tout vecteur
     y, on a ∥M y∥2 ≤ |||M |||2 · ∥y∥2 .
     Appliquons cette propriété deux fois :

                            ∥ABx∥2 = ∥A(Bx)∥2 ≤ |||A|||2 · ∥Bx∥2

     Et de même :
                                      ∥Bx∥2 ≤ |||B|||2 · ∥x∥2
     En combinant ces deux inégalités :

                ∥ABx∥2 ≤ |||A|||2 · (|||B|||2 · ∥x∥2 ) = (|||A|||2 · |||B|||2 ) · ∥x∥2

     Pour tout x ̸= 0, on peut diviser par ∥x∥2 :

                                   ∥ABx∥2
                                          ≤ |||A|||2 · |||B|||2
                                    ∥x∥2
     Puisque cette majoration est valable pour tout x ̸= 0, elle est aussi valable pour le
     supremum :
                                        ∥ABx∥2
                       |||AB|||2 = sup          ≤ |||A|||2 · |||B|||2
                                   x̸=0  ∥x∥2

  3. Affirmation : Pour toute matrice A de Rn×n , il existe un x ∈ Rn et une norme
     vectorielle notée ∥ · ∥ tels que |||A|||F = ∥A.x∥
                                                  ∥x∥
                                                       .


     Réponse : FAUX L’affirmation sous-entend que la norme de Frobenius ∥ · ∥F
     est une norme induite par une norme vectorielle. Ce n’est pas le cas.


     Argument : Une propriété fondamentale de toute norme matricielle ||| · ||| induite
     par une norme vectorielle est que la norme de la matrice identité In vaut 1.
                                              ∥In x∥        ∥x∥
                               |||In ||| = sup       = sup      =1
                                          x̸=0 ∥x∥     x̸=0 ∥x∥

     Or, comme nous l’avons vu dans l’exercice 2, la norme de Frobenius de la matrice
     identité est :                                √
                                          ∥In ∥F = n
                                        √
     Pour toute dimension n > 1, on a n ̸= 1. Puisque la norme de Frobenius ne vérifie
     pas la condition |||In |||F = 1 pour n > 1, elle ne peut pas être une norme induite
     par une norme vectorielle. L’affirmation est donc fausse.


Correction de l’Exercice 7
Énoncé : Pour tout réel α, on note Aα la matrice
                                               
                                        α 1 0
                                Aα =  1 α 1 
                                        0 1 α

                                                 8
~~~

## Page 9

~~~text
  1. Quelles sont les valeurs propres de la matrice Aα ?

  2. Pour quelles valeurs de α, la matrice Aα est-elle inversible ?

  3. Calculer les normes |||Aα |||1 , |||Aα |||2 et |||Aα |||∞ .



Solution
  1. Calcul des valeurs propres de Aα
     Les valeurs propres λ sont les racines du polynôme caractéristique, défini par det(Aα −
     λI) = 0.
                                               α−λ     1       0
                            det(Aα − λI) =       1   α−λ       1
                                                 0     1     α−λ
     En développant par rapport à la première ligne :

                                         α−λ      1         1    1
                          det = (α − λ)                 −1           +0
                                           1    α−λ         0 α−λ
                               = (α − λ) (α − λ)2 − 1 − 1 [(α − λ) − 0]
                                                    

                               = (α − λ) (α − λ)2 − 1 − 1
                                                         

                               = (α − λ) (α − λ)2 − 2
                                                      


     On cherche les racines de (α − λ) ((α − λ)2 − 2) = 0.

        • Soit α − λ = 0 =⇒ λ1 = α.
                                                               √
        • Soit (α − λ)2 − 2 = 0 =⇒ (α − λ)2 = 2√=⇒ α − λ = ±√ 2. Cela nous donne
          deux autres valeurs propres : λ2 = α − 2 et λ3 = α + 2.

     Les valeurs propres de Aα sont donc :
                                                       √                   √
                               λ1 = α,     λ2 = α −        2,   λ3 = α +       2

  2. Condition d’inversibilité de Aα
     Une matrice est inversible si et seulement si aucune de ses valeurs propres n’est
     nulle. Nous devons donc avoir λ1 ̸= 0, λ2 ̸= 0 et λ3 ̸= 0.

        • λ1 ̸= 0 =⇒ α ̸= 0.
                          √             √
        • λ2 ̸= 0 =⇒ α − 2 ̸= 0 =⇒ α ̸= 2.
                          √              √
        • λ3 ̸= 0 =⇒ α + 2 ̸= 0 =⇒ α ̸= − 2.

     La matrice Aα est donc inversible si et seulement si α n’est pas une de ces trois
     valeurs.                                            √     √
                       Aα est inversible pour α ∈ R \ {− 2, 0, 2}

  3. Calcul des normes matricielles de Aα

        • Norme 1 (|||Aα |||1 ) : Maximum de la somme des valeurs absolues par colonne.

                                                  9
~~~

## Page 10

~~~text
    – Colonne 1 : |α| + |1| + |0| = |α| + 1
    – Colonne 2 : |1| + |α| + |1| = |α| + 2
    – Colonne 3 : |0| + |1| + |α| = |α| + 1
                 |||Aα |||1 = max(|α| + 1, |α| + 2, |α| + 1) = |α| + 2

• Norme infinie (|||Aα |||∞ ) : Maximum de la somme des valeurs absolues par
  ligne. La matrice Aα étant symétrique (Aα = ATα ), sa norme ∞ est égale à sa
  norme 1.
                          |||Aα |||∞ = |||Aα |||1 = |α| + 2

• Norme 2 (|||Aα |||2 ) : Norme spectrale. Puisque la matrice Aα est symétrique,
  sa norme 2 est égale à son rayon spectral ρ(Aα ), qui est le maximum des valeurs
  absolues de ses valeurs propres.

                      |||Aα |||2 = ρ(Aα ) = max(|λ1 |, |λ2 |, |λ3 |)
                                               √             √ 
                    |||Aα |||2 = max |α|, |α − 2|, |α + 2|
                                   √         √
  Les deux valeurs propres α − 2 et α + 2 √      sont les plus √     éloignées de α. Le
  maximum de leurs valeurs absolues est |α| + 2. Comme 2 > 0, on a |α| +
  √
    2 > |α|. Le maximum est donc déterminé par les deux valeurs propres
  extrêmes.                              √        √                  √
                |||Aα |||2 = max(|α − 2|, |α + 2|) = |α| + 2




                                     10
~~~
