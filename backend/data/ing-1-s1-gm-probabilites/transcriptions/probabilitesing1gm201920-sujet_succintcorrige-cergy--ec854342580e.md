# probabilitesing1gm201920-sujet_succintcorrige-cergy.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1ux6Jxp0-XyNYWW4VNnn0K0c0aDOwF53E) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
EISTI, ING1 GM, Examen de Probabilités – 7 janvier 2020


                                                          Règles
Les calculatrices et les documents sont interdits. Il est très important de rédiger proprement et de montrer
rigoureusement chaque étape d’un raisonnement.


Notations et quelques rappels de formules : Pour toute variable aléatoire réelle X la fonction F X désigne sa
fonction de répartition et φ X , définie sur R par φ X ( u) = E[ e iuX ] ∶= E[cos( uX )] + i E[sin( uX )] avec i2 = −1, désigne
sa fonction caractéristique et f X une densité de X si elle en admet. Dans tous les exercices K désigne un espace
de probabilité (Ω, F , P).
Exercice 1 [3 points] Soit X une v.a.r. définie sur K . On suppose que X suit une loi de Poisson de paramètre 1.
On pose Y = cos( X ). Calculer φ X ( u) pour tout u ∈ R.
Montrer que Y ∈ L2 (K ) et en déduire, en justifiant rigoureusement, les expressions simplifies de E[Y ] et Var(Y ).
Solution : X est une v.a.r. discrète à valeurs N et cos est continu sur R, donc Y est une v.a.r. discrète à valeurs
E ′ = {cos( k), k ∈ N}. Soit u ∈ R. Rappelons que d’après le cours φ X ( u) existe avec sa partie réelle et sa partie
imaginaire qui sont finies. Sachant que, pour tout u ∈ R, les v.a.r. cos( uX ) et sin( uX ) sont des v.a.r. discrètes et
                                                                                                         −1 k
                                                                                               e 1
                                                                                   k=0 cos( uk) k! et E[sin( uX )] =
bornées, on obtient donc d’après le cours E[cos( uX )] = ∑k∈N cos( uk)P( X = k) = ∑+∞
                  1                                                             cos( uk)+i sin( uk)           eiuk
e−1 ∑+∞                                                            −1 +∞
     k=0 sin( uk) k! qui sont deux sommes finies, donc φ X ( u) = e ∑ k=0               k!
                                                                                                    = e−1 ∑+∞
                                                                                                           k=0 k! ,
                                                                                  k
                                                                                c     c    cb    c b
i.e. φ X ( u) = exp(−1 + exp( iu)), en effet pour tout c ∈ C et b ∈ R on a ∑+∞
                                                                            k=0 k! = e et e = ( e )

Comme Y ≤ 1 d’où Y k ∈ L1 pour tout k ∈ R+ , en l’occurrence Y ∈ L2 , donc Y admet une variance (donc Y k ad-
                                                                      cos( k)
met une espérance et elle est finie) et d’après le cours E[Y ] = ∑+∞
                                                                  k=0   k!
                                                                              = Re(φ X (1)) = e−1+cos(1) cos(sin(1))
                                                                          −1             1+cos(2 k) 1
                                                                  2e
et Var(Y ) = E[Y 2 ] − E[Y ]2 . Sachant que E[Y 2 ] = ∑+∞                −1 +∞
                                                       k=0 cos( k) k! = e ∑ k=0              2      k!
                                                                                                       = 12 (1 + Re(φ X (2))) =
1
2
  (1 + e−1+cos(2) cos(sin(2))), d’où la variance de Y .
~~~

## Page 2

~~~text
Exercice 2 [5 points] Soit (Ω, F , P) un espace de probabilité que l’on note par E . Soit T une v.a.r. définie sur
E admettant une densité f T donnée par f T = Ct(1 − t)1[0,1] ( t) pour tout t ∈ R, où C ∈ R est une constante non
aléatoire.
    1. Quelle est la valeur de C ?
                                                                                                 1
Solution : f T étant une fonction de densité, on a ∫R f T ( t) dt = 1, i.e. C ∫0 t(1 − t) dt = 1, et donc C ( 12 − 13 ) = 1, i.e.
C = 6.
  2. Montrer que T est de carré intégrable. En déduire, en justifiant, que T admet une espérance E[T ] et une
variance Var(T ) que vous déterminerez.
Solution : Sachant que P(T ∈ [0, 1]) = ∫[0,1] f T ( t) dt = 1 d’où 0 ≤ T ≤ 1 p.s. et donc T 2 ≤ 1 d’où T 2 est de carré
intégrable, et donc la variance est bien définie, d’après la définition de cette dernière, d’où T admet une espérance
également, qui est finie. En utilisant le théorème de transfert avec [0, 1] ∋ t ↦ h k ( t) = t k ∈ R+ qui est continue (donc
mesurable) et positive pour tout k ∈ {1, 2} et T qui admet une densité, on a E[T 2 ] = E[ h 2 (T )] = ∫R h 2 ( t) f T ( t) dt =
    1                                                                    1
6 ∫0 t3 (1 − t) dt = 6 ( 14 − 51 ) = 20
                                     6
                                        et E[T ] = E[ h 1 (T )] = 6 ∫0 t2 (1 − t) dt = 6 ( 31 − 14 ) = 12
                                                                                                       1                 1
                                                                                                          , i.e. E[T ] = 12 , et donc Var(T ) =
 3    1                     1
10
   − 22
        , i.e. Var ( T ) =  20

    3. Donner l’expression de FT ( t) pour tout t ∈ R.
                                                                                                                                 t
Solution : Soit t ∈ R. On a FT ( t) = P(T ≤ t) = ∫−∞ Ca(1 − a)1]−∞,t]∩[0,1] (a) da = 1[0,1] ( t) ∫0 Ca(1 − a) da +
                                                                      +∞

1]1,+∞[ ( t), i.e. FT ( t) = (3 − 2 t) t2 1[0,1] ( t) + 1]1,+∞[ ( t)
                                                                 √
  4. Soit Y la v.a.r. définie sur E telle que Y =                    T 2 + 1. Montrer que Y admet une densité f Y et donner une
expression de f Y explicitement.
                                                         √
Solution :      Soit y ∈ R. On a FY ( y) = P( T 2 + 1 ≤ y) = 1[0,+∞[ ( y)P(T 2 ≤ y2 − 1) = 1[0,+∞[ ( y)1[1,+∞[ ( y)P(T ≤
√                                                                    √
    y2 − 1), donc FY ( y) = 1[0,+∞[ ( y)1[1,+∞[ ( y)((3 − 2              y2 − 1)( y2 − 1)1[0,√2] ( y) + 1]√2,+∞[ ( y)), et donc on obtient
                   √                                                                                                 √
F Y ( y) = ( 3 − 2     y2 − 1)( y2 − 1)1[1,√2] ( y) + 1]√2,+∞[ ( y), où on a FY dérivable sur [1,                        2]; cela implique que Y
                                                                        2    3                   √
admet une densité f Y donnée par                  f Y ( y) = C ( ddt ( t2 − t3 ))∣ √      (d         y2 − 1) 1
                                                                                                             [1, 2] ( y), c’est-à-dire qu’on a
                                                                                                                 √
                                                                                  t= y2 −1 d y
                       √
f Y ( y) = C y ( 1 −       y2 − 1)1[1,√2] ( y).




                                                                             2
~~~

## Page 3

~~~text
Exercice 3 [4 points] Soit ( X k )k∈N∗ une suie de v.a.r. indépendantes et identiquement distribuées de loi expo-
nentielle de paramètre λ > 0. On rappelle que une densité d’une loi exponentielle de paramètre λ est donnée par
f X ( x) = λ e−λ x 1R+ ( x) pour tout x ∈ R. On a E[ X ] = λ1 et Var( X ) = λ12 . On considère un entier n ≥ 100 et on note
X n = n1 ∑nk=1 X k la moyenne des n premiers X k .

  1. La suite ( X m )m≥1 converge vers quelle variable aléatoire ? et quels sont les types convergences valables
pour cette limite ?
Solution : On peut utiliser la loi forte des grands nombres, avec ( X n )n∈N∗ qui est bien une suite de v.a.r. i.i.d. de
carré intégrable avec µ = E[ X 1 ] = λ1 et σ2 = λ12 < ∞; et on obtient que ( X m )m≥1 converge p.s. et converge dans L2
vers µ (cela implique convergence dans L2 aussi).
On aurait pu utiliser la loi faible des grands nombres, en utilisant i.i.d. et X 1 ∈ L1 , avec convergence p.s. et dans
L1 .
  2. On suppose que λ = 21 et n = 100.
Estimer à l’aide du Théorème Limite Centrale la probabilité P(1, 9 ≤ X n ≤ 2, 1).
Solution : Ici on peut utiliser le Théorème limite centrale, en effet on réutilise les hypothèses utilisées dans la loi
                                                     √
forte des grands nombres, et on a (( nX n − nµ)/σ n)n converge en loi vers une v.a. X ∼ N (0, 1), i.e. limn→∞ P(a ≤
√                                                                √                    √
  n( X n −2)/2 ≤ b) = P(a ≤ X ≤ b), i.e. a et b sont tels que 2a/ n +2 = 1, 9 et 2 b/ n +2 = 2, 1, i.e. a = 5(1, 9−2) = −0, 5
et b = 5(2, 1 − 2) = 0, 5. Or P(a ≤ X ≤ b) = φ(0.5) − φ(−0.5) = 2φ(0.5) − 1 = 2 × 0, 69146 . . . − 1 = 0, 38292 . . .
  3. Déterminer αn et βn (ne dépendant que de n) tels que P(αn ≤ λ X n ≤ βn ) ≈ 0.99.
                                                     √                      √                                    √
Solution : Da façon analogue, on obtient 2a/ n + 2 = αn /λ et 2 b/ n + 2 = βn /λ, i.e. a = 2(αn − 1) n et b =
          √
2(βn −1) n, comme il y a une infinité de cas de (a, b) tels que P(a ≤ X ≤ b) = 0, 99... prenons comme précédemment
                                                                                                    √                  √
a = − b et b positif, i.e. que 2φ( b) − 1 = 0.99, i.e. φ( b) = 0.995, i.e. b = 2.57, d’où αn = 2λ(a/ n + 1) = 1 + 2.57/ n et
              √
βn = 1 − 2.57/ n.




                                                             3
~~~

## Page 4

~~~text
Exercice 4 [8 points] Soit X une v.a.r. de loi exponentielle de paramètre λ > 0.
  1. Calculer F X ( x) pour tout x ∈ R.
Solution : Soit x ∈ R. On a F X ( x) = P( X ≤ x) = ∫−∞ 1]−∞,x]∩[0,+∞[ ( u)λ e−λ u du, donc F X ( x) = (1 − e−λ x )1R+ ( x).
                                                                 +∞


  2. Soit k ∈ N∗ . Justifier que X k ∈ L1 (K ) et calculer E[ X k ].
Solution : Comme X ≥ 0 p.s. on a donc X k ≥ 0 p.s. i.e. X k qui admet une espérance, et par conséquent on
peut utiliser le théorème de transfert avec h k définie par h k ( x) = x k sur R+ , en effet X admet une densité; d’où
E[∣ X k ∣] = E[ X k ] = ∫R+ x k λ e−λ x dx, par une IPP et une petite récurrence (à détailler rigoureusement !) on obtient
que E[ X k ] = λkk! , et donc on a bien X k ∈ L1 .
  3. Déterminer φ X ( x) pour tout x ∈ R.
Solution :      Soit x ∈ R. D’après le cours (c’était justifié) on peut utiliser le théorème de transfert et donc on
                                                                                                                   2
                                                          λ
obtient Re(φ X ( x)) = ∫R+ cos( xu)λ e−λu du = λ2 +            [ e−λu ( x sin( xu) − λ cos( xu))]0 = λ2λ+ x2 (on justifie ces limites !
                                                                                                       +∞
                                                            x2
en bornant par exemple), et de même (en justifiant encore les limites ! ça prend une ou deux minutes) on obtient
Im(φ X ( x)) = λ2λ+xx2 , d’où φ X ( x) = λ2 +
                                            λ
                                              x2
                                                 (λ + i x)
  4. Soient x, y deux réels strictement positifs. Calculer P({ X > x + y}∣{ X > x}).
Solution : Sachant que x > 0 d’où en utilisant la question 2. on a P( X > x) = 1 − (1 − e−λ x ) = e−λ x > 0, d’où
P({ X > x + y}∣{ X > x}) = P( X > x + y et X > x)/P( X > x) = P( X > x + y)/P( X > x) = e−λ( x+ y) / e−λ x , i.e. P({ X >
x + y}∣{ X > x}) = e−λ y , on dit qu’il n’y a pas de dépendance du passé.
  5. Déterminer la loi de p( X ) où p( x) désigne la partie entière de x ∈ R.
Solution : X ≥ 0 p.s. et pour tout ω ∈ Ω on a ( p( X ))(ω) ∈ N par définition de la partie entière, donc p( X )
est une variable aléatoire discrète à valeurs entiers positifs, donc d’après le cours la loi de p( X ) est l’ensemble
{P( p( X ) = k), k ∈ N}. Or pour k ∈ N, on a P( p( X ) = k) = P( k ≤ X < k +1) = F X (( k +1)− )− F X (k− ) = F X (k +1)− F X ( k)
car F X est continue, alors on a P( p( X ) = k) = e−λk − e−λ(k+1) . Vérification se fait par ∑+∞                       +∞ −λk
                                                                                                   k=0 P( X = k) = ∑ k=0 e       −
  −λ( k+1)    −λ×0    −λ(+∞)
e          =e      −e        = 1−0 = 1
  6. Déterminer la loi de Z où Z = X − p( X ).
Solution : Sachant que Z ∈ [0, 1[ p.s. (partie fractionnaire) on a donc pour tout t ∈ R, F Z ( t) = P( Z ≤ t) =
1[0,1[ ( t)P( X − p( X ) ≤ t) + 1[1,+∞[ ( t), donc pour 0 ≤ t < 1 on a P( Z ≤ t) = P( X − p( X ) ≤ t) = P( X − p( X ) ≤ t, X ∈
∪k∈N [ k, k + 1[) = P( ⋃k∈N { X − p( X ) ≤ t, X ∈ [k, k + 1[}), comme il s’agit d’une union d’événements disjoints, d’où
grâce à la σ-additivité de P, on obtient P( Z ≤ t) = ∑+∞        k=0 P( k ≤ X < k + 1, X − k ≤ t) = ∑ k=0 P( k ≤ X ≤ t + k) =
                                                                                                    +∞
      −λ t    +∞ −λk           −λ t   1                   −λ
(1 − e ) ∑k=0 e        = (1 − e ) 1− e−λ , en effet 0 < e < 1 grâce à λ > 0. F Z est aussi dérivable sur [0, 1[, et donc Z
                                                          −λ z                                              −λ z
admet une densité f Z donnée par f Z ( z) = λ 1e− e−λ 1[0,1[ ( z), et on a aussi F Z ( z) = 11−−ee−λ 1[0,1[ ( z) + 1[1,+∞[ ( z).
  7. Montrer que Z est de carré intégrable. Calculer Var( Z ).
Solution : Comme Z ∈ [0, 1[ p.s. d’où Z 2 ≤ 1 p.s. et donc Z 2 ∈ L1 , i.e. Z est bien de carré intégrable, donc Var( Z )
                                                                                                                         2         2
existe et on a avec le théorème de transfert bien justifié Var( Z ) = 1−λe−λ ∫0 z2 e−λ z dz − (1−λe−λ )2 (∫0 ze−λ z dz) =
                                                                                                   1                           1

  1                                                                                                                2 e−λ
1− e−λ
       E[ X 2 ] − (1− e1−λ )2 E[ X ]2 , finalement Var( Z ) = 1−1e−λ λ22 − (1− e1−λ )2 λ12 , i.e. Var( Z ) = λ21(−
                                                                                                                 1− e−λ )2
                                                                                                                           .




                                                                         4
~~~
