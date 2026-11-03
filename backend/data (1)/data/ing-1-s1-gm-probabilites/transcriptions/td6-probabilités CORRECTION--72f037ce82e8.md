# td6-probabilités CORRECTION.pdf

[Ouvrir l’original](https://drive.google.com/open?id=193wcd2YO2ujeN5u6c11UHuQ8OvHbISIy) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                           TD 06 - Vecteurs Aléatoires
                               Correction Détaillée

                                               Année 2025-2026


Exercice 1. Considérons un vecteur aléatoire (Z1 , Z2 ) =: Z tel que Z1 (Ω) = Z2 (Ω) = {0, 1} et :
   — P(Z = (0, 0)) = (1 − p)2
   — P(Z = (1, 1)) = p2
   — P(Z = (0, 1)) = P(Z = (1, 0)) = p(1 − p)
où p ∈]0, 1[. Montrer que Z1 et Z2 sont indépendantes.
    Solution :
    1. Stratégie : Critère analytique
    Nous allons utiliser la caractérisation par les fonctions caractéristiques.
    Rappel : Deux variables Z1 et Z2 sont indépendantes si et seulement si pour tout (t1 , t2 ) ∈ R2 ,
la fonction caractéristique conjointe est le produit des marginales :

                                      φ(Z1 ,Z2 ) (t1 , t2 ) = φZ1 (t1 ) × φZ2 (t2 )

    Rappel : ϕZ (t) est par définition E[ei t·Z ] avec t · Z = dk=1 tk Zk avec Z vecteur aléatoire de taille
                                                              P
d et t ∈ Rd .
    2. Calcul des fonctions caractéristiques marginales
    Commençons par identifier la loi marginale de Z1 .

            P(Z1 = 1) = P(Z = (1, 0)) + P(Z = (1, 1)) = p(1 − p) + p2 = p(1 − p + p) = p

                                     P(Z1 = 0) = 1 − P(Z1 = 1) = 1 − p
Z1 suit donc une loi de Bernoulli B(p). Par symétrie, Z2 aussi.
   La fonction caractéristique d’une variable X ∼ B(p) est φX (t) = E[eitX ] = (1 − p) + peit .
   Formons le produit des marginales :

              φZ1 (t1 )φZ2 (t2 ) = (1 − p) + peit1 × (1 − p) + peit2
                                                                  

                                 = (1 − p)2 + p(1 − p)eit2 + p(1 − p)eit1 + p2 ei(t1 +t2 )    (∗)

    3. Calcul de la fonction caractéristique                  conjointe
                                                               
    Par définition, φ(Z1 ,Z2 ) (t1 , t2 ) = E ei(t1 Z1 +t2 Z2 ) . C’est une espérance discrète sur les 4 couples de
valeurs possibles donnés par l’énoncé :
                                                     X
                                     φZ (t1 , t2 ) =     ei(t1 z1 +t2 z2 ) P(Z = (z1 , z2 ))
                                                 z1 ,z2

   Détaillons la somme :
   — Pour (0, 0) : ei(0) (1 − p)2 = (1 − p)2
   — Pour (1, 0) : ei(t1 ·1+t2 ·0) p(1 − p) = p(1 − p)eit1
   — Pour (0, 1) : ei(t1 ·0+t2 ·1) p(1 − p) = p(1 − p)eit2

                                                           1
~~~

## Page 2

~~~text
   — Pour (1, 1) : ei(t1 ·1+t2 ·1) p2 = p2 ei(t1 +t2 )
   En sommant tout :

                   φZ (t1 , t2 ) = (1 − p)2 + p(1 − p)eit1 + p(1 − p)eit2 + p2 ei(t1 +t2 )   (∗∗)

     4. Conclusion En comparant les expressions (∗) et (∗∗), on constate l’égalité parfaite pour tout
(t1 , t2 ). L’indépendance est donc démontrée.




                                                         2
~~~

## Page 3

~~~text
Exercice 2. Soient X et Y deux v.a. dont la densité conjointe est f(X,Y ) (x, y) = c(2x+y)1]2,6[×]0,5[ (x, y).
   1. Que vaut c ?
   2. Trouvez les fonctions de répartitions marginales FX et FY .
   3. Trouver les fonctions de densités marginales fX et fY .
   4. Calculer P(X > 3, Y > 2), P(X > 3) et P(X + Y < 4).
   5. En déduire si X et Y sont indépendantes.
   Solution : 1. Calcul de la constante c
   Condition de normalisation : Pour que f(X,Y ) soit une densité de probabilité, son intégrale
totale par rapport à la mesure de Lebesgue λR2 doit valoir 1 :
                                        Z
                                           f(X,Y ) dλR2 = 1
                                              R2

  La fonction f(X,Y ) est mesurable et positive sur R2 . D’après le théorème de Fubini-
Tonelli, l’intégrale double par rapport à la mesure produit est égale aux intégrales itérées :
                         Z                  Z Z                      
                             f(X,Y ) dλR2 =       f(X,Y ) (x, y) dλ(y) dλ(x)
                            R2                     R       R

   Passage à l’intégrale de Riemann : Sur le pavé ouvert D =]2, 6[×]0, 5[, la fonction (x, y) 7→
c(2x + y) est continue (c’est un polynôme). Sur un domaine borné, pour une fonction continue (et
bornée), l’intégrale de Lebesgue coïncide avec l’intégrale de Riemann classique.
   On peut donc écrire le calcul avec les bornes et le symbole dxdy usuel :
                                         Z 6 Z 5             
                                    1=c            (2x + y) dy dx
                                               2       0

   Calculons l’intégrale intérieure (par rapport à y) :
                 Z 5                           y=5 
                                            y2
                                                             
                                                           25
                     (2x + y) dy = 2xy +           = 10x +      − 0 = 10x + 12.5
                   0                        2 y=0           2
   Calculons l’intégrale extérieure (par rapport à x) :
                                   Z 6
                                                                      6
                                       (10x + 12.5) dx = c 5x2 + 12.5x 2
                                                          
                             I=c
                                       2

                                 I = c [(5(36) + 12.5(6)) − (5(4) + 12.5(2))]
                          I = c [(180 + 75) − (20 + 25)] = c(255 − 45) = 210c
                                 1
   On a donc 210c = 1 =⇒ c = 210    .
   2. & 3. Marginales (Densités et Répartitions)
   — Pour la variable X —
   Densité : On intègre la densité conjointe par rapport à y sur R.
                         Z                                                Z 5
                fX (x) =    c(2x + y)1]2,6[ (x)1]0,5[ (y)dy = c1]2,6[ (x)     (2x + y)dy
                              R                                              0

                                                           4x + 5
                           = c1]2,6[ (x)(10x + 12.5) =             1]2,6[ (x)
                                             Rx              84
   Répartition : Par définition, FX (x) = −∞ fX (t)dt.
                           Z x                          Z
                                 4t + 5                    4t + 5
                 FX (x) =                1]2,6[ (t)dt =           1]2,6[ (t)1]−∞,x] (t)dt
                             −∞    84                    R   84
L’intégrale porte sur l’intersection des supports : ]2, 6[∩] − ∞, x].

                                                           3
~~~

## Page 4

~~~text
   — Si x ≤ 2, l’intersection est vide =⇒ 0. R
                                                       x                2
   — Si x ∈]2, 6[, l’intersection est ]2, x] =⇒ 2 4t+5    84
                                                               dt = 2x +5x−18
                                                                          84
                                                                                 .
   — Si x ≥ 6, l’intersection est ]2, 6[ =⇒ 1.
                                      2x2 + 5x − 18
                          FX (x) =                         1[2,6[ (x) + 1[6,+∞[ (x)
                                                84
   — Pour la variable Y —
   Densité : On intègre par rapport à x sur R.
                     Z 6
                         2x + y                     [x2 + xy]62       32 + 4y      16 + 2y
            fY (y) =             dx · 1]0,5[ (y) =                =             =          1]0,5[ (y)
                       2   210                          210             210          105
                                                  Ry
   Répartition : Par définition, FY (y) = −∞ fY (t)dt. En utilisant les indicatrices pour gérer les
bornes rigoureusement :                    Z
                                                16 + 2t
                                FY (y) =                1]0,5[ (t) · 1]−∞,y] (t)dt
                                              R   105
Le produit des indicatrices 1]0,5[ (t) · 1]−∞,y] (t) vaut 1]0,min(y,5)[ (t) (si y > 0).
   Calculons l’intégrale selon la position de y :
   — Si y ≤ 0 : Le domaine d’intégration est vide. FY (y) = 0.
   — Si y ∈]0, 5[ : Le domaine est ]0, y].
                                         Z y
                                             16 + 2t          1                   16y + y 2
                             FY (y) =                  dt =      [16t + t2 ]y0 =
                                           0   105          105                      105

   — Si y ≥ 5 : Le domaine est ]0, 5[. L’intégrale vaut 1 (densité totale).

                                            y 2 + 16y
                                FY (y) =            1[0,5[ (y) + 1[5,+∞[ (y)
                                           105
   4. Calculs de probabilités détaillés
   a) Calcul de P(X > 3, Y > 2)
   On cherche P((X, Y ) ∈ B) avec B = {(x, y) ∈ R2 | x > 3, y > 2}. L’intersection de cet événement
avec le support de la densité S =]2, 6[×]0, 5[ est :

                      A = B ∩ S = (]3, +∞[∩]2, 6[) × (]2, +∞[∩]0, 5[) =]3, 6[×]2, 5[

   Justification : A est un produit d’ouverts de R, c’est donc un ouvert de R2 , et par conséquent
un borélien. On peut intégrer la densité sur cet ensemble.

                                                    ZZ
                             P(X > 3, Y > 2) =         f(X,Y ) (x, y)1A (x, y)dxdy
                                                         R2
                                                      Z 6 Z 5               
                                                    1
                                                 =               (2x + y)dy dx
                                                   210 3       2
                                      h          i5
                                              y2
   Calculons l’intégrale intérieure : 2xy + 2 = (10x + 12.5) − (4x + 2) = 6x + 10.5.
                                                  2
   Calculons l’intégrale extérieure :
                                  Z 6
                               1                       1  2        6
                                      (6x + 10.5)dx =     3x + 10.5x 3
                             210 3                    210
                                   1                               112.5   15
                              =       [(108 + 63) − (27 + 31.5)] =       =
                                  210                               210    28


                                                          4
~~~

## Page 5

~~~text
   b) Calcul de P(X > 3)
   Nous pouvons procéder par deux méthodes rigoureuses.
   Méthode 1 : Par la densité conjointe (Marginalisation)
                                                 ZZ
                P(X > 3) = P(X > 3, Y ∈ R) =           f(X,Y ) (x, y)1]3,+∞[ (x)dxdy
                                                       R2

En restreignant au support y ∈]0, 5[ et x ∈]2, 6[∩]3, +∞[=]3, 6[ :
                            Z 6 Z 5                       Z 6
                                                                4x + 5              23
                P(X > 3) =            f(X,Y ) (x, y)dy dx =            dx = · · · =
                             3                                     84               28
                                | 0       {z          }      3

                                         =fX (x)

   Méthode 2 : Par la fonction de répartition

                               P(X > 3) = 1 − P(X ≤ 3) = 1 − FX (3)

Comme 3 ∈]2, 6[, nous utilisons l’expression fractionnelle calculée précédemment :

                                     2(3)2 + 5(3) − 18   18 + 15 − 18   15
                          FX (3) =                     =              =
                                            84                84        84
D’où P(X > 3) = 1 − 15  84
                              69
                           = 84    23
                                 = 28 .
    c) Calcul de P(X + Y < 4)
    On cherche P((X, Y ) ∈ A) où A = {(a, b) ∈ R2 | a + b < 4}.
    Justification topologique : Soit la fonction h : R2 → R définie par h(a, b) = a + b. h est
polynomiale en ses variables, elle est donc continue sur R2 . L’ensemble A est l’image réciproque de
l’ouvert ] − ∞, 4[ par h (A = h−1 (] − ∞, 4[)). A est donc un ouvert de R2 , c’est un borélien.
    Détermination des bornes d’intégration : On cherche l’intersection de A avec le support
S =]2, 6[×]0, 5[.                                               
                                            
                                             a + b <  4         a < 4 − b
                                                                 
                       (a, b) ∈ A ∩ S ⇐⇒ 2 < a < 6          ⇐⇒ 2 < a < 6
                                                                
                                              0<b<5                0<b<5
                                                                

Les conditions sur a se résument à : 2 < a < min(4 − b, 6). Pour que cet intervalle pour a soit non
vide, il faut que 2 < min(4 − b, 6).
   — Puisque b > 0, on a 4 − b < 4 < 6. Donc min(4 − b, 6) = 4 − b.
   — La condition d’existence devient 2 < 4 − b ⇐⇒ b < 2.
   — En combinant avec 0 < b < 5, on obtient 0 < b < 2.
   Le domaine d’intégration effectif est donc : 0 < b < 2 et 2 < a < 4 − b.
                                                 Z 2 Z 4−b           
                                             1
                           P(X + Y < 4) =                   (2a + b)da db
                                            210 0      2

   Calcul de l’intégrale intérieure :
                            2     a=4−b
                            a + ab a=2 = ((4 − b)2 + b(4 − b)) − (4 + 2b)

                            = (16 − 8b + b2 + 4b − b2 ) − 4 − 2b = 12 − 6b
   Calcul de l’intégrale extérieure :
                     Z 2
                  1                     1           2    1               12   2
                         (12 − 6b)db =      12b − 3b2 0 =     (24 − 12) =     =
                 210 0                 210                210             210   35

                                                   5
~~~

## Page 6

~~~text
       5. Indépendance
       Question : A-t-on indépendance entre X et Y ?
       Si X et Y étaient indépendantes, on aurait l’égalité presque partout :

                                        f(X,Y ) (x, y) = fX (x) × fY (y)

       Comparons les expressions sur le domaine ouvert D =]2, 6[×]0, 5[ :
                           1
       — f(X,Y ) (x, y) = 210 (2x + y). C’est un polynôme de degré 1.
       — Le produit des marginales est :
                                                           
                                            4x + 5    16 + 2y     64x + 8xy + 80 + 10y
                               P (x, y) =                       =
                                              84        105               8820

       C’est un polynôme comportant un terme en xy.
   Considérons la fonction différence ∆(x, y) = f(X,Y ) (x, y) − P (x, y) sur l’ouvert D. ∆ est une
                                                                                  8
fonction polynomiale (donc continue). Le terme en xy dans ∆(x, y) est − 8820        xy ̸= 0. Le polynôme
∆ n’est donc pas le polynôme nul.
   Argument de mesure non nulle : Puisque ∆ est continue et non nulle, il existe au moins un
point (x0 , y0 ) ∈ D tel que ∆(x0 , y0 ) ̸= 0. Par continuité, il existe une petite boule ouverte B ⊂ D
autour de (x0 , y0 ) sur laquelle ∆(x, y) ̸= 0. Une boule ouverte a une mesure de Lebesgue strictement
positive.
   L’égalité f(X,Y ) = fX fY est fausse sur un ensemble de mesure non nulle. Les variables
ne sont donc pas indépendantes.

       Alternative rigoureuse : Argument via la Fonction de Répartition
       Si X et Y étaient indépendantes, on aurait l’égalité F(X,Y ) (x, y) = FX (x)FY (y) pour tout (x, y) ∈
R2 .
   Comparons les expressions sur l’ouvert D =]2, 6[×]0, 5[ :
                                                  2x2 y+xy 2 −8y−2y 2
                        1
                           RxRy
   — F(X,Y ) (x, y) = 210   2 0
                                 (2u + v)dvdu  =         420
                                                                      .
                                                                        2         2)
   — Le produit des marginales est P (x, y) = FX (x)FY (y) = (2x +5x−18)(16y+y
                                                                          8820
                                                                                     .
   Considérons la fonction différence ∆(x, y) = F(X,Y ) (x, y)−P (x, y). C’est une fonction polynomiale
(car différence de polynômes), elle est donc continue sur D.
   Testons un point, par exemple (4, 2) :
                       56     2
   — F(X,Y ) (4, 2) = 420  = 15  ≈ 0.1333
   — P (4, 2) = 84 × 105 = 42 × 12
                  34    36    17
                                    35
                                         34
                                       = 245 ≈ 0.1387
On constate que ∆(4, 2) ̸= 0.
   Argument de mesure non nulle : Puisque ∆ est continue sur D et non nulle en (4, 2), il existe
un voisinage ouvert V ⊂ D autour de (4, 2) sur lequel ∆(x, y) reste strictement non nulle. Or, la
mesure de Lebesgue d’un ouvert non vide est strictement positive (λ(V ) > 0).
   L’égalité F(X,Y ) = FX FY est donc fausse sur un ensemble de mesure non nulle. Les
variables ne sont pas indépendantes.




                                                       6
~~~

## Page 7

~~~text
Exercice 3. Soient X, Y ∼ N (0, 1) i.i.d. Calculer la densité de (U, V ) avec U = X +Y et V = X −Y .
   Solution : 1. Identification de la transformation
   On cherche la loi du couple (U, V ) défini par le système :
                                           (
                                             U =X +Y
                                             V =X −Y

    Soit ϕ : R2 → R2 l’application définie par ϕ(x, y) = (x + y, x − y). On a donc (U, V ) = ϕ(X, Y ).
    2. Justification du C 1 -difféomorphisme
    Pour appliquer le théorème du changement de variable, nous devons montrer que ϕ est un C 1 -
difféomorphisme de R2 sur R2 .
    — Bijectivité : Résolvons le système u = x+y et v = x−y pour trouver l’application réciproque
       ψ = ϕ−1 . En additionnant les deux lignes : u + v = 2x =⇒ x = u+v                2
                                                                                          . En soustrayant    :
       u − v = 2y =⇒ y = u−v                                                               u+v u−v
                                                                                                    
                                  2
                                     . L’application   réciproque  est donc  ψ(u,   v) =    2
                                                                                               ,  2
                                                                                                     . Elle est
       bien définie sur tout R2 , donc ϕ est bijective.
    — Régularité : Rappel (Résultat classique) : Les applications ϕ et ψ sont des applications
       linéaires (ce sont des polynômes de degré 1 en leurs variables). Or, toute application linéaire
       sur un espace de dimension finie est de classe C ∞ (et donc C 1 ).
           Puisque ϕ est bijective, C 1 , et que sa réciproque ψ est aussi C 1 , ϕ est un C 1 -difféomorphisme
       de R2 sur R2 .
    3. Calcul du Jacobien
    Le théorème nécessite le déterminant de la matrice jacobienne de l’application inverse ψ :
                                                ∂x ∂x                  
                                                 ∂u   ∂v      1/2 1/2
                                 Jψ (u, v) = ∂y ∂y =
                                                 ∂u   ∂v
                                                              1/2 −1/2

   Calculons ce déterminant :
                                        
                                    1    1   1 1   1 1   1
                        det(Jψ ) =     −   −     =− − =−
                                    2    2   2 2   4 4   2

On prend la valeur absolue : | det(Jψ )| = | − 1/2| = 12 .
   4. Calcul de la densité
   Par hypothèse, X et Y sont i.i.d. N (0, 1). La densité conjointe est le produit des marginales :
                                            1   2      1   2      1 − x2 +y2
                          f(X,Y ) (x, y) = √ e−x /2 · √ e−y /2 =    e 2
                                            2π         2π        2π
   Appliquons la formule du changement de variable :

                                f(U,V ) (u, v) = f(X,Y ) (ψ(u, v)) · | det(Jψ )|
                                                                         
                                                           u+v u−v            1
                                f(U,V ) (u, v) = f(X,Y )         ,          ·
                                                             2        2       2
   Détaillons le calcul de l’exposant :
                                   2      2
                                                 u2 + 2uv + v 2 u2 − 2uv + v 2
                           
                  2    2      u+v       u−v
                x +y =                +        =               +
                                2        2             4              4
Les termes croisés 2uv s’annulent :
                                                  2u2 + 2v 2   u2 + v 2
                                     x2 + y 2 =              =
                                                      4           2
                                                       7
~~~

## Page 8

~~~text
   On injecte ce résultat dans la densité :

                                                  1 u2 + v 2
                                                            
                                           1                    1   1 − u2 − v2
                         f(U,V ) (u, v) =    exp − ·           · =    e 4e 4
                                          2π      2    2        2  4π
   5. Conclusion et Identification
   On peut séparer la densité en un produit de fonctions de u et de v :
                                                                 
                                              1 − u2         1 − v2
                            f(U,V ) (u, v) = √ e 4 × √ e 4
                                              4π             4π
                                                                   t2
                                                    1
   On rappelle qu’une densité N (0, σ 2 ) s’écrit √2πσ 2
                                                         e− 2σ2 . Ici, on identifie 2σ 2 = 4 =⇒ σ 2 = 2. Le
terme de normalisation correspond bien : √ 1 = √14π .
                                                       2π(2)
   Ainsi, U et V sont deux variables aléatoires indépendantes, et elles suivent toutes
deux la loi N (0, 2).

Exercice 4. Soit (X, Y, Z) un vecteur aléatoire de densité f(X,Y,Z) (x, y, z) = 1−sin(x)8π
                                                                                        sin(y) sin(z)
                                                                                           3          1[0,2π[3 (x, y, z).
Montrer que X, Y, Z sont 2 à 2 indépendantes mais pas (mutuellement) indépendantes.
   Solution : 1. Indépendance 2 à 2 (Exemple pour X et Y)
   Calculons la densité marginale du couple (X, Y ) en intégrant la densité conjointe par rapport à
z sur R. Pour (x, y) ∈ [0, 2π[2 :
                                              Z 2π
                                                   1 − sin(x) sin(y) sin(z)
                             f(X,Y ) (x, y) =                               dz
                                               0            8π 3
Par linéarité de l’intégrale :
                                               Z 2π                          Z 2π              
                                        1
                       f(X,Y ) (x, y) = 3               1dz − sin(x) sin(y)          sin(z)dz
                                       8π          0                           0
                                                                                                    R 2π
    Rappel : L’intégrale de la fonction sinus sur une période complète [0, 2π] est nulle :           0
                                                                                                           sin(z)dz =
[− cos(z)]2π
          0 = −1 − (−1) = 0.
    Le terme contenant le produit des sinus s’annule donc. Il reste :
                                  1                            2π                   1
              f(X,Y ) (x, y) =      3
                                      (2π − 0)1[0,2π[2 (x, y) = 3 1[0,2π[2 (x, y) = 2 1[0,2π[2 (x, y)
                                 8π                            8π                  4π
   On reconnaît le produit de deux densités uniformes sur [0, 2π] :
                                             1                          1
                                 fX (x) =      1[0,2π[ (x) et fY (y) =    1[0,2π[ (y)
                                            2π                         2π
Puisque f(X,Y ) (x, y) = fX (x)fY (y) presque partout, X et Y sont indépendantes.
    Par symétrie de l’expression en x, y, z, le même calcul montre que (X, Z) sont indépendantes et
(Y, Z) sont indépendantes.
    2. Non-indépendance mutuelle (globale)
    Les variables X, Y, Z seraient mutuellement indépendantes si et seulement si :

                           f(X,Y,Z) (x, y, z) = fX (x)fY (y)fZ (z) presque partout.

   Le produit des trois marginales est la densité uniforme sur le cube :
                                                   1   1   1            1
                                  P (x, y, z) =      ·   ·   1[0,2π[3 = 3 1[0,2π[3
                                                  2π 2π 2π             8π
                                                               8
~~~

## Page 9

~~~text
   Considérons la fonction différence ∆ sur l’ouvert D =]0, 2π[3 :

                                                                       sin(x) sin(y) sin(z)
                   ∆(x, y, z) = f(X,Y,Z) (x, y, z) − P (x, y, z) = −
                                                                               8π 3
    Cette fonction est continue sur D. Prenons le point M = ( π2 , π2 , π2 ). On a ∆(M ) = − 1·1·1
                                                                                             8π 3
                                                                                                   ̸= 0.
    Argument de mesure non nulle : Puisque ∆ est continue et non nulle en M , il existe un
voisinage ouvert V ⊂ D de M sur lequel ∆ ne s’annule pas. La mesure de Lebesgue de cet ouvert
est strictement positive (λ(V ) > 0).
    L’égalité f(X,Y,Z) = fX fY fZ est fausse sur un ensemble de mesure non nulle. Les trois
variables ne sont pas mutuellement indépendantes.




                                                     9
~~~

## Page 10

~~~text
                                                                            ∗
      √ 5.X Soient X ∼ N (0, 1) et Y ∼ Γ(n/2, 1/2) indépendantes, avec n ∈ N . Quelle est la loi
Exercice
de Z = n √Y ?

    Solution : 1. Analyse du problème
                                    √ X          de dimension et stratégie
    Nous cherchons la loi de Z = n √Y . La transformation (x, y) 7→ z est une application de R2 dans
R. Problème : On ne peut pas appliquer le théorème du changement de variable (difféomorphisme)
directement car les dimensions de l’espace de départ (2) et d’arrivée (1) ne sont pas identiques.
    Stratégie : Il faut créer artificiellement la seconde composante du vecteur aléatoire de dimension
2 (Z, W ) en√introduisant W par W = h(X, Y ). On cherche une application Φ : D → ∆, définie par
Φ(x, y) = ( n √xy , h(x, y)), qui soit un C 1 -difféomorphisme d’un ouvert D sur un ouvert ∆. Une fois
la densité conjointe f(Z,W ) trouvée, on obtiendra la densité marginale par intégration :
                                                   Z
                                         fZ (z) =     f(Z,W ) (z, w)dw
                                                    R

   2. Choix de la variable auxiliaire h(x, y)
   Le support du couple (X, Y ) est l’ouvert D = R × R∗+ (car Y ∼ Γ est strictement positive).
   — (Essai (mauvais) avec h(x, y) = x : Posons W = X. On cherche à inverser le système
             √    √
         z = nx/ y                        √        √       √                           √
                        . Cela implique y = n xz = n wz . Or, par définition y > 0. Cette
         w=x
      équation n’a de sens que si wz > 0 (i.e. w et z de même signe). Si w et z sont de signes opposés,
      il n’y a pas de solution. L’image ∆ ne serait pas un produit d’intervalles simples
      (forme complexe). Ce choix est rejeté.                                        (      √     √
                                                                                      z = nx/ y
   — Essai (bon) avec h(x, y) = y : Posons W = Y . Le système devient                                 .
                                                                                      w=y
                                          √ √
      L’inversion donne y = w et x = z w/ n. Comme y ∈ R∗+ , on a w ∈ R∗+ . Pour tout z ∈ R,
      x est bien défini. L’espace d’arrivée est ∆ = R × R∗+ , qui est un ouvert simple. Ce choix
      fonctionne parfaitement.
   3. Justification du C 1 -difféomorphisme                      √
   Considérons l’application Φ : D → ∆ définie par Φ(x, y) = ( n √xy , y).
                                                                                          √
  — Bijectivité : D’après l’étude ci-dessus, l’application réciproque est ψ(z, w) = ( z√nw , w). Elle
     est définie de manière unique pour tout (z, w) ∈ ∆.
  — Régularité : Les fonctions composantes utilisent la racine carrée, la multiplication et la
     division. Sur les ouverts D et ∆ (où y > 0 et w > 0), ces opérations sont C ∞ .
Donc Φ est un C 1 -difféomorphisme de D sur ∆.
  4. Calcul du Jacobien et de la densité conjointe
  Calculons le déterminant de la matrice jacobienne de l’application inverse ψ :
                                                        √         !
                                               ∂x       ∂x        w
                                                                         √z
                                                
                                                                 √
                                Jψ (z, w) =    ∂z       ∂w   =     n    2 nw
                                               ∂y       ∂y
                                               ∂z       ∂w       0       1
                                         r                   r
                                             w                   w
                            det(Jψ ) =         =⇒ |J| =                (car w > 0)
                                             n                   n
   La densité conjointe est donnée par la formule du changement de variable :

                            f(Z,W ) (z, w) = f(X,Y ) (ψ(z, w)) · |J| · 1∆ (z, w)
                                           √               r
                                               z w                  w
                       f(Z,W ) (z, w) = fX √            fY (w)         · 1R (z)1R∗+ (w)
                                                  n                 n

                                                        10
~~~

## Page 11

~~~text
   En remplaçant par les expressions (avec X ∼ N (0, 1) et Y ∼ Γ(n/2, 1/2)) :

                                 1 − 1 z2 w (1/2)n/2 n −1 − w w1/2
                                                           
              f(Z,W ) (z, w) = √ e 2 n               w2 e 2          1R (z)1R∗+ (w)
                                 2π           Γ(n/2)            n1/2

    5. Calcul de la densité marginale de Z
    La densité de Z s’obtient en intégrant la densité conjointe par rapport à w sur R. L’indicatrice
1R+ (w) restreint le domaine d’intégration à ]0, +∞[.
  ∗


                               Z +∞
                                        1 (1/2)n/2                        1 z2
                                                                             
                                                      n
                                                        −1+ 12
                    fZ (z) =          √            ·w 2        · exp −w    +      dw
                                0       2πn Γ(n/2)                        2 2n

   Regroupons les termes constants K et l’intégrale dépendant de z :
                                Z +∞
                                                                       z2
                                                                         
                                      n+1
                                          −1 −w·A               1
                     fZ (z) = K      w 2 e        dw avec A =       1+
                                 0                              2      n

   Astuce du noyau Gamma : On reconnaît (à la constante de normalisation près) l’intégrale
                                                                      R∞ ′      ′       Γ(α′ )
d’une densité Gamma de paramètres α′ = n+1
                                         2
                                             et β ′ = A. On sait que 0 xα −1 e−β x dx = (β ′ )α′ .

Donc :
                                                        Γ( n+1
                           Z +∞
                                  n+1                           )
                                w 2 −1 e−wA dw =           2
                                                                 n+1
                            0                       1       z2     2
                                                    2
                                                      (1 +  n
                                                               )
   6. Simplification Finale
                                                                                            !
                                            1 (1/2)n/2                 Γ( n+1
                                                        
                                                                           2
                                                                              )
                          fZ (z) =        √                  ·        n+1         2   n+1
                                           2πn Γ(n/2)            (1/2) 2 (1 + zn ) 2
   Simplifions les puissances de 1/2 :

                                 (1/2)n/2                                   √
                                    (n+1)/2
                                            = (1/2)n/2−(n+1)/2 = (1/2)−1/2 = 2
                               (1/2)

   Il reste :                                   √                   − n+1
                                                  2 Γ( n+1       z2
                                                             
                                                        2
                                                           )            2
                                      fZ (z) = √              1+
                                                2πn Γ(n/2)       n
                √
               2
On simplifie √2πn = √1πn .
                                                               − n+1
                                                 Γ( n+1 )   z2
                                                                  2
                                                     2
                                    fZ (z) = √           1+
                                               nπΓ(n/2)     n
   On reconnaît exactement la densité d’une loi de Student à n degrés de liberté, notée
t(n).




                                                         11
~~~
