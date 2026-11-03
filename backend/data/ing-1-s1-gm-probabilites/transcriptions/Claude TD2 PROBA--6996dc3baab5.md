# Claude TD2 PROBA.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1IFYI2doaqwZfDNffephyx445rxCX75dC) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                      CYTech 2025-2026
                                   ING1 - GM : Probabilités

                                             TD 2


Exercice 1 Soit g : [0, ∞[→ [0, ∞[ strictement croissante avec g(0) ̸= 0. Montrer que

                                          E[g(|X|)]
                          P (|X| ≥ a) ≤             ,       pour tout a > 0.
                                            g(a)


Correction :
   Pour a > 0, considérons l'événement {|X| ≥ a}. Puisque g est strictement croissante, on a :

                                    |X| ≥ a ⇒ g(|X|) ≥ g(a)

Donc sur l'événement {|X| ≥ a}, on a g(|X|) ≥ g(a), d'où :
                                                     g(|X|)
                                       1{|X|≥a} ≤
                                                      g(a)

En prenant l'espérance des deux côtés :
                                                                
                                                    g(|X|)
                                    E[1{|X|≥a} ]≤ E
                                                     g(a)
                                                 E[g(|X|)]
                                    P (|X| ≥ a)≤
                                                   g(a)

Ce qui est l'inégalité demandée. Il s'agit d'une généralisation de l'inégalité de Markov.


Exercice 2 Soit h : R → [0, α]. Montrer que pour 0 ≤ a < α on a

                                                     E[h(X)] − a
                                  P (h(X) ≥ a) ≥                 .
                                                        α−a


Correction :
   Décomposons l'espérance de h(X) :

                       E[h(X)]= E[h(X)1{h(X)≥a} ] + E[h(X)1{h(X)<a} ]
                                ≤ E[α1{h(X)≥a} ] + E[a1{h(X)<a} ]
                                = αP (h(X) ≥ a) + aP (h(X) < a)
                                = αP (h(X) ≥ a) + a(1 − P (h(X) ≥ a))
                                = a + (α − a)P (h(X) ≥ a)

Donc :
                              E[h(X)] − a ≤ (α − a)P (h(X) ≥ a)
D'où :
                                                     E[h(X)] − a
                                  P (h(X) ≥ a) ≥
                                                        α−a


                                                 1
~~~

## Page 2

~~~text
Exercice 3 Montrer que σX
                        2 = E[X 2 ] − E[X]2 si E[X 2 ] < +∞.


Correction :
   Par dénition, la variance est :
                                2
                               σX = E[(X − E[X])2 ]
                                  = E[X 2 − 2XE[X] + E[X]2 ]
                                  = E[X 2 ] − 2E[X]E[X] + E[X]2
                                  = E[X 2 ] − 2E[X]2 + E[X]2
                                  = E[X 2 ] − E[X]2

On a utilisé la linéarité de l'espérance et le fait que E[X] est une constante.


Exercice 4 Montrer que E[X]2 ≤ E[X 2 ] si X admet une espérance.


Correction :
   D'après l'exercice précédent, on a :
                                       2
                                      σX = E[X 2 ] − E[X]2

Or la variance est toujours positive ou nulle : σX
                                                 2 ≥ 0. Donc :


                                       E[X 2 ] − E[X]2 ≥ 0

D'où :
                                          E[X]2 ≤ E[X 2 ]
Cette inégalité est aussi une conséquence de l'inégalité de Cauchy-Schwarz appliquée à la constante
1 et à X : E[1 · X]2 ≤ E[12 ]E[X 2 ] = E[X 2 ].


Exercice 5 Soit X une v.a.r. qui suit une loi binomiale B(n, p). Montrer que la probabilité pour
que X soit paire est de 12 (1 + (1 − 2p)n ).

Correction :
   Notons Ppaire = P (X paire) et Pimpaire = P (X impaire).
   On a Ppaire + Pimpaire = 1.
   Calculons Ppaire − Pimpaire :
                                                n
                                                X
                          Ppaire − Pimpaire =         (−1)k P (X = k)
                                                k=0
                                                n       
                                                X       n k
                                                          k
                                           =     (−1)      p (1 − p)n−k
                                                        k
                                             k=0
                                              n  
                                             X     n
                                           =          (−p)k (1 − p)n−k
                                                   k
                                                k=0
                                           = (1 − p − p)n = (1 − 2p)n

par la formule du binôme de Newton.


                                                      2
~~~

## Page 3

~~~text
   En résolvant le système avec les deux équations, on obtient :
                                                  1 + (1 − 2p)n
                                       Ppaire =
                                                        2



Exercice 6 Soit Xn ∼ B(n, pn ) avec λ = npn constant. Soit An = {Xn ≥ 1}, et soit Y ∼
Poisson(λ).
  1. Montrer que limn→∞ P (Xn = j|An ) = P (Y = j|Y ≥ 1).
                                                                                λ −λ
  2. On suppose que la constante λ est un entier. Montrer que E[|Y − λ|] = 2λ
                                                                           (λ−1)! .
                                                                              e



Correction :
   1. On a pn = nλ . Par dénition :
                                               P (Xn = j)
                         P (Xn = j|An ) =                   pour j ≥ 1
                                             1 − P (Xn = 0)
Quand n → ∞, on sait que Xn → Y en loi (approximation de Poisson), donc :
                                                                λj e−λ
                               P (Xn = j) → P (Y = j) =
                                                                  j!
Et :
                                                 λ n
                                                  
                                P (Xn = 0) = 1 −     → e−λ
                                                 n
Donc :
                                              λj e−λ
                                                 j!
                        lim P (Xn = j|An ) =         = P (Y = j|Y ≥ 1)
                       n→∞                   1 − e−λ
    2. La loi de Poisson de paramètre λ entier a ses modes en λ − 1 et λ. Par calculs (utilisant
les relations de récurrence de la loi de Poisson), on obtient :
                                                        2λλ e−λ
                                       E[|Y − λ|] =
                                                        (λ − 1)!



Exercice 7 Soit X une v.a. qui prend ses valeurs dans N. Montrer que E[X] =      n=0 P (X > n).
                                                                              P∞


Correction :
   On a :
                              ∞
                              X                   ∞ X
                                                  X ∞
                                    P (X > n)=                P (X = k)
                              n=0                 n=0 k=n+1
                                                  ∞ X
                                                  X k−1
                                              =             P (X = k)
                                                  k=1 n=0
                                                  X∞
                                              =         kP (X = k)
                                                  k=1
                                              = E[X]

On a inversé l'ordre de sommation (justié car les termes sont positifs) et utilisé le fait que
  n=0 1 = k .
Pk−1


                                                   3
~~~

## Page 4

~~~text
Exercice 8 Soit X une variable aléatoire de loi de Poisson de paramètre λ. Montrer que pour
r ∈ N∗ \ {1}, on a E[X(X − 1)(X − 2) · · · (X − r + 1)] = λr .

Correction :
   On calcule :
                                                      ∞
                                                      X                                    λk e−λ
                  E[X(X − 1) · · · (X − r + 1)]=            k(k − 1) · · · (k − r + 1)
                                                                                             k!
                                                      k=0
                                                      ∞
                                                      X        k! λk e−λ
                                                  =
                                                            (k − r)! k!
                                                      k=r
                                                      ∞
                                                      X λk e−λ
                                                  =
                                                            (k − r)!
                                                      k=r
                                                                ∞
                                                         r −λ
                                                                X  λk−r
                                                  =λ e
                                                                  (k − r)!
                                                                k=r
                                                                ∞
                                                                X λj
                                                  = λr e−λ
                                                                      j!
                                                                j=0

                                                  = λr e−λ · eλ = λr



Exercice 9 Soit X : Ω → N une variable aléatoire tel que X(Ω) = N. On suppose que X admet
une variance.
  1. Montrer que ∞ k=0 k P (X = k) converge.
                         2
                 P

  2. En déduire que limn→∞ n2 P (X > n) = 0.
  3. Montrer que E[X 2 ] = ∞k=0 (2k + 1)P (X > k).
                           P


Correction :
    1. Si X admet une variance, alors E[X 2 ] < +∞. Or E[X 2 ] =                   k=0 k P (X = k), donc cette
                                                                                 P∞     2

série converge.
    2. Pour n ≥ 1 :
                               ∞
                               X
                                     k 2 P (X = k) ≥ (n + 1)2 P (X > n)
                             k=n+1

Puisque k=0 k2 P (X = k) converge, on a ∞    k=n+1 k P (X = k) → 0 quand n → ∞.
        P∞                                       P  2

   Donc (n + 1) P (X > n) → 0, ce qui implique n P (X > n) → 0.
                 2                                2

   3. En utilisant l'astuce P (X = k) = P (X > k − 1) − P (X > k) :
                                    ∞
                                    X
                         E[X 2 ]=         k 2 [P (X > k − 1) − P (X > k)]
                                    k=1
                                    ∞
                                    X                             ∞
                                                                  X
                               =          (k + 1)2 P (X > k) −             k 2 P (X > k)
                                    k=0                           k=1
                                                   ∞
                                                   X
                               = P (X > 0) +             [(k + 1)2 − k 2 ]P (X > k)
                                                   k=1
                                    ∞
                                    X
                               =          (2k + 1)P (X > k)
                                    k=0



                                                      4
~~~

## Page 5

~~~text
Exercice 10 Soit X ∼ Poisson(λ). Rappeler l'espérance et la variance de X , et montrer que
P (X ≤ λ/2) ≤ 4/λ.

Correction :
     Pour une loi de Poisson de paramètre λ : E[X] = λ et Var(X) = λ.
     On a X ≤ λ/2 équivaut à |X − λ| ≥ λ/2.
     Par l'inégalité de Bienaymé-Tchebychev :
                                                                 λ      4
                                    P (|X − λ| ≥ λ/2) ≤             2
                                                                      =
                                                               (λ/2)    λ

Donc :
                                                                              4
                                  P (X ≤ λ/2) ≤ P (|X − λ| ≥ λ/2) ≤
                                                                              λ



Exercice 11 Soient α, β ∈]0, 1[ deux réels xés. Soit Ω = N2 . Pour tout (i, j) ∈ Ω, on pose
pi,j = αβ(1 − α)i (1 − β)j .
     1. Montrer qu'en posant P ({(i, j)}) = pi,j pour tout (i, j) ∈ Ω, on dénit une mesure de
        probabilité.
     2. Pour tout (i, j) ∈ Ω, on pose X((i, j)) = i et Y ((i, j)) = j . Déterminer la loi de X et la loi
        de Y .
     3. Calculer P (X < Y ), P (X = Y ) et P (X > Y ).

Correction :
     1. Il faut vérier que    (i,j)∈N2 pi,j = 1 :
                              P

                              ∞ X
                                ∞
                              X                                        1 1
                                        αβ(1 − α)i (1 − β)j = αβ ·      · =1
                                                                       α β
                              i=0 j=0

     2. Pour la loi de X :                           ∞
                                                     X
                                    P (X = i) =            pi,j = α(1 − α)i
                                                     j=0

Donc X ∼ Géométrique(α). De même, Y ∼ Géométrique(β).
   3. Calcul de P (X < Y ) :
                                                            α(1 − β)
                                         P (X < Y ) =
                                                           α + β − αβ
     Calcul de P (X = Y ) :
                                                               αβ
                                         P (X = Y ) =
                                                           α + β − αβ
     Calcul de P (X > Y ) :
                                                            β(1 − α)
                                         P (X > Y ) =
                                                           α + β − αβ



Exercice 12 Soit (An )n≥1 une suite d'événements deux à deux disjoints. Montrer que limn→∞ P (An ) =
0.

Correction :



                                                       5
~~~

## Page 6

~~~text
   Supposons par l'absurde qu'il existe ε > 0 et une sous-suite (Ank ) tels que P (Ank ) ≥ ε pour
tout k.
   Les événements étant deux à deux disjoints :
                                      N                 N
                                                !
                                      [                 X
                                P         Ank       =         P (Ank ) ≥ N ε
                                    k=1                 k=1

Quand N → ∞, cela tend vers +∞, ce qui contredit P (Ω) = 1.
  Donc limn→∞ P (An ) = 0.


Exercice 13 Soit (Aβ )β∈B une famille d'événements deux à deux disjoints.

  1. Montrer que si P (Aβ ) > 0 pour tout β ∈ B , alors B est dénombrable.
  2. En déduire que pour une fonction de répartition F qui admet une innité de points de
     discontinuités B , B est dénombrable.

Correction :
   1. Pour tout n ∈ N∗ , posons An = {Aβ : P (Aβ ) > 1/n}. Chaque An est ni car :
                                                1
                                Card(An ) ·
                                                    X
                                                  <   P (Aβ ) ≤ 1
                                                n
                                                        Aβ ∈An

Or :                                                              ∞
                                                                  [
                                    {Aβ : P (Aβ ) > 0} =               An
                                                                 n=1

C'est une union dénombrable d'ensembles nis, donc dénombrable.
   2. Les points de discontinuité correspondent aux sauts P ({x}) > 0. Par la question 1, leur
ensemble est dénombrable.


Exercice 14 Soit P une probabilité sur R admettant une densité f Borel mesurable. Montrer
que P ({x0 }) = 0 pour tout x0 ∈ R.

Correction :
   On a {x0 } =    n=1 [x0 − 1/n, x0 ]. Par continuité décroissante :
                  T∞

                                                                       Z x0
                  P ({x0 }) = lim P ([x0 − 1/n, x0 ]) = lim                    f (x)dx = 0
                              n→∞                                n→∞ x −1/n
                                                                      0


car la longueur de l'intervalle tend vers 0.


Exercice 15 Soit F (x) =       i=1 2i 1[1/i,∞[ (x). Montrer que c'est une fonction de répartition et
                            P∞     1

calculer les probabilités demandées.

Correction :
   F est croissante, limx→−∞ F (x) = 0, limx→+∞ F (x) = 1, et continue à droite. Donc F est
une fonction de répartition.
   a) P ([1, ∞[) = 1 − ∞      1    1
                         P
                          i=2 2i = 2
   b) P ([ 10
           1
              , ∞[) = 1 − ∞      1   210 −1
                          P
                           i=11 2i = 210


                                                        6
~~~

## Page 7

~~~text
   c) P ({0}) = 0 P
   d) P ([0, 12 [) = ∞   1    1
                     i=3 2i = 4
   e) P (] − ∞, 0[) = 0
   f) P (]0, ∞[) = 1


Exercice 16 Soient X, Y : Ω → R telles que {X ̸= Y } ∈ N (i.e. X = Y p.s.). Montrer que
X : (Ω, A′ ) → (R, B(R)) est mesurable si et seulement si Y l'est.

Correction :
   Supposons Y mesurable. Pour tout B ∈ B(R), notons N = {X ̸= Y } ∈ N .
   Sur {X = Y }, on a X −1 (B) = Y −1 (B). Donc :

                       X −1 (B) = (Y −1 (B) ∩ {X = Y }) ∪ (X −1 (B) ∩ N )

Puisque Y −1 (B) ∈ A′ et N ∈ N ⊂ A′ , on a X −1 (B) ∈ A′ .
   Par symétrie, si X est mesurable, alors Y l'est.



                                                                                   2/2




                                               7
~~~
