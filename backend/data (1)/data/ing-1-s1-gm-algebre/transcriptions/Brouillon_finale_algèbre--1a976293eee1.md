# Brouillon_finale_algèbre.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1P3cAq1enDVjYQ7up3_wFxkq7tdRSrogf) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
         1. DÉMONSTRATIONS (TD1 & TD3)                                                                 — Col 1 : |α| + |1| + 0 = |α| + 1
                                                                                                       — Col 2 : |1| + |α| + |1| = |α| + 2 ← Max
Ex 4 TD1 : Norme    Infinie Matricielle         Montrer que    — Col 3 : 0 + |1| + |α| = |α| + 1
             Pn
||A||∞ = maxi j=1 |aij |. Soit K = maxi nj=1 |aij |.
                                       P
                                                            D’où ||Aα ||1 = |α| + 2.
                                                                                                    2. Norme 2 (Rayon Spectral) : On cherche les VP    via det(Aα −µI) =
1. Majoration (≤) : Pour tout vecteur x ̸= 0 :                                                                                                                     
                                                                                                                                                         β 1 0
                         n                                           n
                         X                                           X                              0. En posant β = α − µ, le déterminant est celui de  1 β 1 .
               (Ax)i =         aij xj =⇒ |(Ax)i | ≤                        |aij ||xj |                                                                    0 1 β
                         j=1                                         j=1
                                                                                                                ∆ = β(β 2 − 1) − 1(β) = β 3 − 2β = β(β 2 − 2)
   Or |xj | ≤ ||x||∞ . Donc :
                                                                                                                      √      √
                                            n                                                       Racines
                                                                                                    √       en β : 0, 2, − 2. Comme µ = α − β, les VP sont : α, α −
                                                                                                            √
                                            X
                   |(Ax)i | ≤ ||x||∞                |aij | ≤ ||x||∞ · K                               2, α + 2.                             √        √
                                            j=1                                                                     ||Aα ||2 = max(|α|, |α − 2|, |α + 2|)

   En prenant le max sur i, on a ||Ax||∞ ≤ K||x||∞ , donc ||A||∞ ≤ K.                               Ex 20 TD3 : Calcul complet Conditionnement                      A =
                                                                                                                           
2. Minoration (≥) : On construit un x spécifique pour atteindre la                                    1 10              1 −10
   borne. Soit k l’indice de la ligne réalisant le maximum K. On pose le
                                                                                                            =⇒ A−1 =
                                                                                                      0 1               0  1
   vecteur x tel que xj = signe(akj ). Alors ||x||∞ = 1 et :                                        1. Conditionnement κ1 (Norme 1)
                          n
                          X                                    n
                                                               X                                    Norme 1 = Max somme des valeurs absolues des colonnes.
               (Ax)k =          akj · signe(akj ) =                   |akj | = K                       — ||A||1 = max(|1| + |0|, |10| + |1|) = max(1, 11) = 11.
                          j=1                                  j=1
                                                                                                       — ||A−1 ||1 = max(|1| + |0|, | − 10| + |1|) = 11.
   Donc ||Ax||∞ ≥ K. Ainsi, ||A||∞ = K.                                                                                     κ1 (A) = 11 × 11 = 121
Ex 5 TD1 : Norme 1 et Transposée               Montrer que 2. Conditionnement κ2 (Norme 2)
            T
                                                                                                p
||A||1 = ||A ||∞ . Par définition : ||A||1 = maxj i |aij | (Max A n’est pas              ||A||       T
                                                 P
                                                                          symétrique =⇒    2 = ρ(A A). Calcul de M =
                            T
                                                                                     
sommes colonnes). Calculons ||A ||∞ :                                                                          1   0    1     10           1    10
                                                                                                    AT A =                          =               . Valeurs propres de M
                                   X                                                                          10 1      0      1           10   101
                    ||AT ||∞ = max    |(AT )ij |                                                    (det(M − λI) = 0) :
                                            i
                                                    j
                                                                                                                  (1 − λ)(101 − λ) − 100 = λ2 − 102λ + 1 = 0
Or, par définition de la transposée, (AT )ij = aji .
                                                                                                                   ∆ = (−102)2 − 4 = 10404 − 4 = 10400
                                                                                                                         √
                                                    X
                          ||AT ||∞ = max                    |aji |
                                                i                                                                 102 + 10400                      1
                                                        j                                                 λmax =               ≈ 101.99, λmin =        ≈ 0.0098
                                                                                                                         2                        λmax
Si on renomme les indices (i devient colonne, j devient ligne), cela re-                                         √                      √      √
                                                                                                    On a ||A||2 = λmax et ||A−1 ||2 = 1/ λmin = λmax .
vient exactement à calculer la somme max des colonnes de A. Donc                                                           p        p
||A||1 = ||AT ||∞ .                                                                                               κ2 (A) = λmax × λmax = λmax ≈ 102
Ex 17 TD3 : Cond. Spectral (SDP) Si A est SDP,
κ2 (A) = λmax /λmin . On sait que κ2 (A) = ||A||2 · ||A−1 ||2 .                                                4. CHOLESKY (RAPPEL & EX 1)
— Pour A : A est symétrique réelle, donc ||A||2 = ρ(A) = maxi |λi |.                                Théorème : A symétrique définie positive ⇐⇒ ∃L triangulaire inf.
  Comme A est définie positive, λi > 0, donc ||A||2 = λmax .
                                                                                                                                                      q
                                                                                                    à diagonale > 0 tq A = LLT . Formules : lii =       aii − i−1    2
                                                                                                                                                             P
                                                                                                                                                                k=1 lik et
— Pour A−1 : Les valeurs propres de A−1 sont 1/λi .                                                        1      P j−1
                                                                                                    lij = l (aij − k=1 lik ljk ).
                                                                                                           jj
                                        1       1          1
                  ||A−1 ||2 = max
                                                                                                                                                                
                                           =            =                                                                                             4    2   2
                                  i     λi   mini |λi |   λmin                                      Application Ex 1 (Fiche Cholesky) A = 2 10               7 , b =
                                                                                                                                                      2    7  21
D’où κ2 (A) = λmax · λ 1       = λλmax .                                                             
                         min          min                                                              0
                                                                                                     0 . 1. Factorisation A = LLT :
                2. POINT FIXE (TD2 EX 9)                                                               96
                                                                                                                     √
Étude de g(x) = λx(1 − x) 1. Points fixes (g(x) = x) :                                              — Col 1 : l11 = 4 = 2. l21 = 2/2 = 1. l31 = 2/2 = 1.
                                                                                                                     √
                                                                                                    — Col 2 : l22 = 10 − 12 = 3. l32 = 31 (7 − 1 × 1) = 2.
                λx(1 − x) = x ⇐⇒ x(λ(1 − x) − 1) = 0                                                                 p                √
                                                                                                    — Col 3 : l33 = 21 − (12 + 22 ) = 16 = 4.
Deux solutions : x∗1 = 0 et λ(1 − x) = 1 =⇒ 1 − x = 1/λ =⇒ x∗2 =                                                                           
                                                                                                                                    2 0 0
1 − 1/λ = λ−1
            λ
              .
                                                                                                                              L = 1 3 0
2. Attractivité (|g ′ (x)| < 1) : Dérivée : g ′ (x) = λ(1 − x) + λx(−1) =
                                                                                                                                    1 2 4
λ − 2λx = λ(1 − 2x).
                                                                                                    2. Résolution Ax = b ⇐⇒          T                      T
— En x∗1 = 0 : g ′ (0) = λ. Stable si |λ| < 1.                                                                                 LL x = b : Posons y = L x. On ré-
                                                                                                                               2y
                                                                                                                               1  = 0 →  y 1 = 0
— En x∗2 = λ−1
                                                                                                                              
            λ
               :
                                                                                                    sout Ly = b (Descente) : 1(0) + 3y2 = 0 → y2 = 0             =⇒
                                     
                                  λ−1
                                                                                                                              
                                                                                                                               1(0) + 2(0) + 4y3 = 96 → y3 = 24
                                                                                                                              
             g ′ (x∗2 ) = λ 1 − 2       = λ − 2(λ − 1) = 2 − λ
                                   λ
                                                                                                                
                                                                                                                  0
                                                                                                    y    =      0  On résout LT x             =    y (Remontée) :
   Condition de stabilité : |2 − λ| < 1.
                                                                                                                 24
           −1 < 2 − λ < 1 ⇐⇒ −3 < −λ < −1 ⇐⇒ 1 < λ < 3
                                                                                                    
                                                                                                    4x3 = 24 → x3 = 6
                                                                                                    
                                                                                                      3x2 + 2(6) = 0 → 3x2 = −12 → x2 = −4
3. Conv. Quadratique (g ′ (x∗ ) = 0) : Pour x∗2 , on cherche 2 − λ =                                
                                                                                                      2x1 + 1(−4) + 1(6) = 0 → 2x1 = −2 → x1 = −1
                                                                                                    
0 =⇒ λ = 2. Dans ce cas, g ′′ (x) = −2λ ̸= 0, donc convergence d’ordre
2.

              3. NORMES & COND (TD1/3)
                                                                                              
                                                                           α             1   0
Ex 7 TD1 : Calcul complet sur Aα                                     Aα =  1            α   1 .
                                                                            0            1   α
1. Norme 1 (Max Somme Colonnes) : On additionne les valeurs
absolues de chaque colonne.
~~~

## Page 2

~~~text
                                       4. FACTORISATION LU (TD5)


Exercice 23 : LU avec Pivot Partiel (PA = LU)
                                                         
                                   0        3   1          1
Énoncé : Résoudre Ax = b avec A = 4        1   1 et b = 5.
                                   2        2   4          6
Problème : Le pivot a11 = 0. Impossible sans permutation. On permute L1 et L2 (P12 ) pour avoir le pivot max (4).
                                                                     
                                                4 1 1                   5
                                 A′ = P A = 0 3 1 , b′ = P b = 1
                                                2 2 4                   6

Étape 1 : Factorisation de A′ On cherche A′ = LU .
  — Colonne 1 : Pivot u11 = 4. On élimine le 2 en ligne 3.
                                                               2
                                                       l31 =     = 0.5
                                                               4
                                                                                                              
                                                                                                 4    1     1
    Opération : L3 ← L3 − 0.5L1 ⇒ (2 − 2, 2 − 0.5, 4 − 0.5) = (0, 1.5, 3.5). Matrice courante : 0    3     1 .
                                                                                                 0   1.5   3.5
  — Colonne 2 : Pivot u22 = 3. On élimine le 1.5 en ligne 3.
                                                               1.5
                                                      l32 =        = 0.5
                                                                3
     Opération : L3 ← L3 − 0.5L2 ⇒ (0, 1.5 − 1.5, 3.5 − 0.5) = (0, 0, 3).
Résultat LU :                                                        
                                          1   0 0                4 1 1
                                      L= 0   1 0 , U = 0 3 1
                                         0.5 0.5 1               0 0 3
                                             
                                             y1 = 5
                                             
                                          ′
Étape 2 : Résolution 1. Descente (Ly = b ) : y2 = 1
                                             
                                               0.5(5) + 0.5(1) + y3 = 6 ⇒ 2.5 + 0.5 + y3 = 6 ⇒ y3 = 3
                                             
                       
                       3x3 = 3 ⇒ x3 = 1
                       
2. Remontée (U x = y) : 3x2 + 1(1) = 1 ⇒ 3x2 = 0 ⇒ x2 = 0
                       
                         4x1 + 0 + 1 = 5 ⇒ 4x1 = 4 ⇒ x1 = 1
                       




Exercice 24 : Conditions d’existence LU
                         
                1 1−ϵ 3
Énoncé : A = 2    2    2. 1) LU existe ? 2) A inversible ?
                3  6    4
1. Existence LU (Théorème des Mineurs Principaux) : Une matrice admet une factorisation LU (sans pivot)
ssi tous ses sous-déterminants principaux sont non nuls.
  — ∆1 = det(a11 ) = 1 ̸= 0.
                         
                 1 1−ϵ
  — ∆2 = det                = 2 − 2(1 − ϵ) = 2ϵ.
                 2     2
Condition : ∆2 ̸= 0 ⇒ ϵ ̸= 0.
2. Inversibilité (det(A) ̸= 0) : det(A) = 1(8 − 12) − (1 − ϵ)(8 − 6) + 3(12 − 6) = −4 − 2(1 − ϵ) + 18 = 12 + 2ϵ.
Condition : 12 + 2ϵ ̸= 0 ⇒ ϵ ̸= −6.
~~~

## Page 3

~~~text
                              5. MÉTHODE DE JACOBI (PARAMÉTRIQUE)


Exercice 29 : Étude Paramétrique Complète
                        
                   1 a a
Énoncé : Soit A = a 1 a.
                   a a 1
  1. Pour quelles valeurs de a, A est-elle Symétrique Définie Positive (SDP) ?
  2. Pour quelles valeurs de a, la méthode de Jacobi converge-t-elle ?

1. Condition A Définie Positive Une matrice symétrique est définie positive si toutes ses valeurs propres
sont strictement positives.
Calcul des Valeurs Propres de A : On cherche λ tel que det(A − λI) = 0.

                                               1−λ       a   a
                                                a       1−λ  a  =0
                                                a        a  1−λ

On somme les colonnes C1 ← C1 + C2 + C3 :

                             1 + 2a − λ     a      a                1            a     a
                             1 + 2a − λ    1−λ     a = (1 + 2a − λ) 1           1−λ    a
                             1 + 2a − λ     a     1−λ               1            a    1−λ

On soustrait L1 aux autres lignes :

                                      1      a     a
                         (1 + 2a − λ) 0    1−λ−a   0   = (1 + 2a − λ)(1 − a − λ)2
                                      0      0   1−λ−a

Valeurs propres : λ1 = 1 + 2a et λ2 = 1 − a (double).
Condition SDP :                 (                                             
                                  1 + 2a > 0 ⇒ a > −1/2                    1
                                                                   =⇒ a ∈ − , 1
                                  1−a>0⇒a<1                                2



2. Convergence de Jacobi La méthode converge ssi le rayon spectral de la matrice d’itération BJ est < 1.
                                      BJ = I − D−1 A = I − I · A    (car D = I ici)

Attention : BJ = D−1 (E + F ). Plus simplement, les coefficients diagonaux sont nuls, et les extra-diagonaux sont
−aij /aii .                                                      
                                                    0 −a −a
                                           BJ = −a 0 −a
                                                   −a −a 0
Calcul du Rayon Spectral ρ(BJ ) : Valeurs propres de BJ (même calcul que pour A, mais avec 0 sur diag) :

                                            µ1 = −2a,     µ2 = a   (double)

                                            ρ(BJ ) = max(| − 2a|, |a|) = 2|a|
Condition Convergence :
                                                                        1
                                        ρ(BJ ) < 1 ⇐⇒ 2|a| < 1 ⇐⇒ |a| <
                                                                        2
                                                             
                                                         1 1
                                                    a∈ − ,
                                                         2 2

Remarque : L’intervalle de convergence de Jacobi est plus restreint que celui où A est définie positive.
~~~

## Page 4

~~~text
                                      6. MÉTHODE DE JACOBI (SUITE - EX 30)


Exercice 30 (Partie 1) : Itérations et Convergence
                                                   
              2           −1     0         1           0
Énoncé : A = −1           2     −1, b = 0, x(0) = 0.
              0           −1     2         1           0

1. Écriture Matricielle (x(k+1) = BJ x(k) + cJ ) On décompose A = D − E − F . Pour Jacobi : M = D et N = E + F .

                                              BJ = D−1 (E + F ) et cJ = D−1 b
                                                                           
                                                 2 0 0                 0 1 0
                                           D = 0 2 0 , E + F = 1 0 1
                                                 0 0 2                 0 1 0
                                                                                
                                           1/2   0    0     0 1 0        0 0.5     0
                                     BJ =  0   1/2 0  1 0 1 = 0.5 0          0.5
                                            0    0   1/2    0 1 0        0 0.5     0
                                                                  
                                                                  0.5
                                                    cJ = D−1 b =  0 
                                                                  0.5

2. Convergence (ρ(BJ )) On calcule les valeurs propres de BJ : det(BJ − λI) = 0.

                 −λ    0.5 0
                 0.5   −λ 0.5 = −λ(λ2 − 0.25) − 0.5(−0.5λ) = −λ3 + 0.25λ + 0.25λ = λ(0.5 − λ2 )
                  0    0.5 −λ

Racines : λ = 0 et λ = ± √12 ≈ ±0.707.

                                                  1
                                        ρ(BJ ) = √ < 1 =⇒ La méthode converge.
                                                   2

                                                                                  (k+1)                            (k)
3. Calcul des itérations (x(1) et x(2) ) Formule composante par composante : xi           = a1ii (bi −
                                                                                                         P
                                                                                                         j̸=i aij xj )
Itération 1 (k = 0) : Partant de x(0) = (0, 0, 0)T .
       (1)                 (0)
  — x1 = 12 (1 − (−1)x2 ) = 0.5(1 + 0) = 0.5
       (1)                 (0)            (0)
  — x2 = 21 (0 − (−1)x1 − (−1)x3 ) = 0.5(0 + 0) = 0
       (1)                 (0)
  — x3 = 21 (1 − (−1)x2 ) = 0.5(1 + 0) = 0.5
                                                     x(1) = (0.5, 0, 0.5)T
Itération 2 (k = 1) : Partant de x(1) = (0.5, 0, 0.5)T .
       (2)          (1)
  — x1 = 21 (1 + x2 ) = 0.5(1 + 0) = 0.5
       (2)          (1)        (1)
  — x2 = 21 (0 + x1 + x3 ) = 0.5(0.5 + 0.5) = 0.5
       (2)          (1)
  — x3 = 21 (1 + x2 ) = 0.5(1 + 0) = 0.5
                                                    x(2) = (0.5, 0.5, 0.5)T
~~~
