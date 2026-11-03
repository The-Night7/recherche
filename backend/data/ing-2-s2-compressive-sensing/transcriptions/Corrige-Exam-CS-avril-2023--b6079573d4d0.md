# Corrige-Exam-CS-avril-2023.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1ZdsDx3sL0S7_yCfezJI4ivtL3O2zYeB-) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                  Corrigé examen Compressive Sensing
                                              13 avril 2023
Exercice 1
               (0)                                                  (1)        ‖R (0) ‖           ‖x‖
  1. (a) R           = x et le seuil est donné par S                      =t              = 2.5          = 4.3
                                                                                   K                12
     (b) Seules les contributions des atmoes n°2 et 3 dépassent le seuil. P 1 = [2, 3].
  2. On construit la matrice 𝛷 1 = [d 2 , d 3 ], on résout le problème aux moindres carrés
                                                               𝛼 (1) = arg min ‖x - 𝛷 1 𝛼‖ 2
                                                                                  𝛼
                                                             -1
    La solution étant : 𝛼 (1) = 𝛷 1T 𝛷 1                          𝛷 1T x, le nouveau résidu est : R (1) = x - 𝛷 1 𝛼 (1) .
  3. On calcule les contributions des différents atomes d i au résidu R (1) ,
                             | < d j , R (1) > |                                                  (2)        ‖R (1) ‖           3.03
    à savoir les :                                     et on les compare au seuil : S                   =t              = 2.5          .
                                    ‖d j ‖ 2                                                                     K                12
    On sélectionne les indices dont la contribution dépasse le seuil :
                         | < d j , R (1) > |
    𝛬 2 = j,                                        > S (2) . On actualise l'ensemble des indices P 2 = [P 1 , 𝛬 2 ].
                               ‖d j ‖ 2
    On construit la matrice 𝛷 2 = [d i ] i∈𝛬2 , on résout le problème aux moindres carrés
                                                               𝛼 (2) = arg min ‖x - 𝛷 2 𝛼‖ 2
                                                                                  𝛼
                                                             -1
    La solution étant : 𝛼                 (2)
                                                =    𝛷 2T 𝛷 2 𝛷 2T x, le nouveau résidu est : R (2) = x - 𝛷 2 𝛼 (2) .


Exercice 2
                                            𝛼 i = 1 si i ⩽ s
  1. Si on prend 𝛼 = (𝛼 1 ,..., 𝛼 K ) avec
                                            𝛼 i = 0 sinon
                                 𝛽 i = 1 si 2 ⩽ i ⩽ s + 1
    et 𝛽 = (𝛽 1 ,..., 𝛽 K ) avec                           , alors on a bien 𝛼, 𝛽 ∈ 𝛴 s .
                                 𝛽 i = 0 sinon
    Mais 𝛼 + 𝛽 ∉ 𝛴 s car il possède exactement s + 1 composantes non nulles. Par conséquent 𝛴 s n'est
    pas un espace vectoriel (non stable par addition).
  2. x = (x 1 ,..., x K ) ∈ 𝛴 2 ⟺ ∃i 1 ≠ i 2 ∈ ⟦1, K⟧, ∀j ∈ ⟦1, K⟧, j ≠ i 1 et j ≠ i 2 ⟹ x j = 0.
    ⟺ ∃i 1 , i 2 ∈ ⟦1, K⟧, x ∈ Vect(e i1 , e i2 ) avec e j = jème vecteur de la base canonique de R K
                                                                                  K     K(K-1)
    Chaque couple (i 1 , i 2 ) est une combinaison de 2 parmi K. Il y en a donc       = 2 .
                                                                                  2
                                                              K(K-1)
    Autrement dit, 𝛴 2 est la réunion de                             sous-espaces vectoriels engendrés par les couples
                                                                2
    (e i 1 , e i 2 ) .
  3. Le même raisonnement conduit à une réunion de sous-espaces engendrés par ℓ vecteurs de la
                                                                                                                        K
    base canonique parmi les K. Le nombre de ces sous-espaces est donc                                                    .
                                                                                                                        ℓ
~~~

## Page 2

~~~text
  4. Supposons que :        ∀𝛼, 𝛽 ∈ 𝛴 s , 𝛼 ≠ 𝛽 ⟹ A𝛼 ≠ A𝛽
  Ou bien, par contraposée :       ∀𝛼, 𝛽 ∈ 𝛴 s , A𝛼 = A𝛽 ⟹ 𝛼 = 𝛽
  On veut montrer : Ker(A) ∩ 𝛴 2s = { 0 }.
  Soit donc 𝛾 ∈ Ker(A) ∩ 𝛴 2s .
  On a donc d'une part : 𝛾 possède au maximum 2s composantes non nulles et d'autre part : A𝛾 = 0.
  Or tout vecteur 2s-parcimonieux peut être écrit comme la différence entre 2 vecteurs s-parcimonieux.
  Il suffit pour cela de prendre uniquement les s premières composantes non nulles pour former le 1er
  vecteur et les opposés des autres pour former le 2ème.
  Nous pouvons donc écrire 𝛾 = 𝛼 - 𝛽 avec 𝛼, 𝛽 ∈ 𝛴 s .
  On en déduit :
                   0 = A𝛾 = A(𝛼 - 𝛽)                ⟹ A𝛼 = A𝛽 ⟹ 𝛼 = 𝛽 ⟹ 𝛾 = 𝛼 - 𝛽 = 0

  5. Supposons que Ker(A) ∩ 𝛴 2s = { 0 }.
  Soient maintenant : 𝛼, 𝛽 ∈ 𝛴 s , A𝛼 = A𝛽.
  On a alors 𝛼 - 𝛽 = 𝛾 ∈ 𝛴 2s et évidemment A𝛾 = 0
  L'hypothèse implique immédiatement 𝛾 = 0, c à d 𝛼 = 𝛽.


Exercice 3
  1. Chaque matrice d (i) 𝛬 i,⋅ est le produit matriciel de la colonne d (i) par la ligne 𝛬 i . Donc toutes les
    colonnes de cette matrice sont colinéaires à d (i) et toutes les lignes sont colinéaire à 𝛬 i, . Par
    conséquent, le rang de cette matrice est inférieur à 1.
    Pour que ce rang soit égal à 0, il faudrait que la matrice soit nulle. Ce qui ne peut être garanti que
    par la nullité de l'un des 2 vecteurs. Le vecteur d (i) étant unitaire (parce que atome du dictionnaire)
    ne peut être nul, c'est donc 𝛬 i⋅ qui doit être nulle.
    Conclusion : rang d (i) 𝛬 i,⋅ = 1 ⟺ 𝛬 i,⋅ ≠ 0.
                             k                k
  2. On sait que D𝛬 =       ∑ d 𝛬j,⋅ = ∑ d (j) 𝛬j,⋅ + d (i) 𝛬i,⋅ . On en déduit :
                                   (j)

                            j=1              j=1
                                              j≠i
                                                         k
                                 E = X - D𝛬 = X - ∑ d (j) 𝛬 j,⋅ - d (i) 𝛬 i,⋅ = Ei - d (i) 𝛬 i,⋅
                                                        j=1
                                                         j≠i
                      k
    avec E i = X -   ∑ d (j) 𝛬j,⋅ = erreur sans tenir compte de la contribution de l'atome d (i).
                     j=1
                      j≠i

  3. Etape 0 : on initialise le dictionnaire D aléatoirement ou à partir de certaines colonnes de X,
     normalisées.
     Etape k :
  • on fixe le dictionnaire actuel D et on calcule les représentations parcimonieuses 𝛬 par un algorithme
     tel que OMP
  • on fixe 𝛬 et on remplace successivement les atomes d (i) de D afin de minimiser l'erreur E i .
    on utilise pour cela la décomposition en valeurs singulières.
~~~

## Page 3

~~~text
  • on recommence jusqu'à ce que la représentation parcimonieuse soit suffisamment précise ou
    jusqu'à un nombre fixe d'itérations.


Exercice 4
                                K
                         p
  1. (a) On sait que ‖𝛼‖ p =   ∑ |𝛼i | p . On peut donc l'écrire :
                               i=1
                                       K                        K      p                    K
                                p
                             ‖𝛼‖p =   ∑ |𝛼i | p-2 |𝛼i | 2 = ∑ ||𝛼i | 2 -1 𝛼i | 2 = ∑ |wi 𝛼i | 2
                                      i=1                       i=1                        i=1
                      p
                        -1
    avec   wi = |𝛼i | 2 .
                                                                                p
    Si on note W la matrice diagonale de coefs w i , on a donc : ‖𝛼‖ p = ‖W𝛼‖ 22 .
    Ainsi le problème (P p ) devient :
                                      (MCP 2 ) : min ‖W𝛼‖22 , tel que x = D𝛼
    (b) Si on pose 𝛽 = W𝛼, alors D𝛼 = DW -1 W𝛼 = DW -1 𝛽.
    Le problème (MCP 2 ) s'écrit alors :
                                       (MCP 2 ) : min ‖𝛽‖22 , tel que x = A𝛽
    où la matrice A est donnée par A = DW -1 .
  2. (a) Les matrices AA T et A T A sont symétriques semi-définies positives et possèdent donc des
     valeurs propres positives.
    Comme 𝜆 > 0, les matrices A T A + 𝜆I K et AA T + 𝜆I N auront des valeurs propres strictement
    positives. Elle sont donc inversibles.
                                                                                      -1
    (b) Calculons le produit matriciel : A T A + 𝜆I K A T AA T + 𝜆I N
                                                           -1                                            -1
                     A T A + 𝜆I K A T AA T + 𝜆IN                = A T AA T + 𝜆A T AA T + 𝜆I N
                                                                                 -1
                                      = A T AA T + 𝜆I N AA T + 𝜆I N                     = AT
                                                      -1
    Il suffit alors de multiplier par A T A + 𝜆I K         pour obtenir le résultat attendu :
                                                      -1                                    -1
                                       A T A + 𝜆I K        A T = A T AA T + 𝜆I N
    (c) Soit 𝛽 * la solution de (PSC 2 ) : min ‖x - A𝛽‖ 22 + 𝜆‖𝛽‖ 22 = min f(𝛽),
                                                 𝛽                                  𝛽
    On peut écrire cette fonction f sous la forme :
                  f(𝛽) = (x - A𝛽) T (x - A𝛽) + 𝜆𝛽 T 𝛽 = x T x - 2𝛽 T A T x + 𝛽 T A T A𝛽 + 𝜆𝛽 T 𝛽
    Le gradient de cette fonction par rapport à la variable 𝛽 est donné par :
                                      ∇f(𝛽) = - 2A T x + 2A T A𝛽 + 2𝜆𝛽
    Le point critique est déterminé par :
                 ∇f(𝛽) = 0 ⟺ - 2A T x + 2A T A𝛽 + 2𝜆𝛽 = 0 ⟺                             A T A + 𝜆I K 𝛽 = A T x
                                                                           -1
                                              ⟺ 𝛽 * = A T A + 𝜆I K              ATx
                                                                                      -1
    (d) Grâce à la question (b) on peut écrire : 𝛽 * = A T AA T + 𝜆I N                     x.
                                      -1
    Comme 𝛽 = W𝛼 et A = DW                 , on peut encore transformer cette écriture en :
~~~

## Page 4

~~~text
                                                                                               -1
                                  *              -1 T            -1        -1 T
                             W𝛼 = DW                        DW        DW          + 𝜆I N            x
                                                        T                         T             -1
                            𝛼 * = W -1 DW -1                DW -1 DW -1               + 𝜆I N         x
  En tenant compte du fait que W est diagonale, on peut simplifier et obtenir :
                                                                                      -1
                                          𝛼 * = W -2 D T DW -2 D T + 𝜆I N                  x
  Soit encore :
                                                                             -1
                                             𝛼 * = QD T DQD T + 𝜆I N              x
                             2
  avec Q = W -2 = W -1
3. (a) Le coefficient 𝜖 est là pour garantir l'inversibilité de la matrice W dans le cas ou l'une des
   composantes 𝛼 i est nulle.
  (b) A l'étape k, nous disposons de 𝛼 (k-1) .
                                                                                                         p
                                                                                                           -1
                                                                                                         2
  Nous construisons la matrice W (k) = diag w i(k) , à partir des w i(k) = |𝛼 i(k-1) | + 𝜖                      .
                                 -2
  On en déduit Q (k) = W (k)          .
  Ensuite on résout le pb aux moindres carrés (MCP 2 ) dont la solution nous donne 𝛼 (k) :
                                                                                      -1
                                          𝛼 (k) = Q (k) D T DQ (k) D T + 𝜆I N              x
~~~
