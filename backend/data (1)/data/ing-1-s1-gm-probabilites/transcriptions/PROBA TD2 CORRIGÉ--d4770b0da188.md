# PROBA TD2 CORRIGÉ.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14BFk9h5qMYYfykEToVL3Ud9dA81Q-e89) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
            Correction Détaillée - TD 2 de Probabilités
                             ING1-GM – CYTech 2025-2026


Exercice 1 : Inégalité de Markov Généralisée
Rappel de Cours : L’inégalité de Markov
    L’inégalité de Markov est un résultat fondamental qui fournit une borne supérieure sur la
probabilité qu’une variable aléatoire non négative dépasse une certaine valeur.
    Pour une variable aléatoire Y ≥ 0 admettant une espérance, et pour tout réel a > 0,
l’inégalité s’écrit :
                                                     E[Y ]
                                        P(Y ≥ a) ≤
                                                       a
Intuitivement, cela signifie qu’une variable ne peut pas avoir une forte probabilité de prendre
de grandes valeurs si son espérance (sa "moyenne") est faible.
    L’exercice 1 est une généralisation de cette inégalité. En appliquant une fonction crois-
sante g à la variable |X|, on peut obtenir des bornes plus fines ou adaptées à des contextes
différents. Par exemple, en choisissant g(x) = x2 , cette inégalité mène directement à l’inégalité
de Bienaymé-Tchebychev.

   Énoncé : Soit g : [0, ∞[→ [0, ∞[ une fonction strictement croissante avec g(0) ̸= 0. Montrer
que pour tout a > 0 :
                                                 E[g(|X|)]
                                  P(|X| ≥ a) ≤             .
                                                    g(a)

Démonstration
   La méthode de démonstration est classique pour les inégalités de ce type. Elle repose sur la
décomposition de l’espérance.
    1. Partir de la définition de l’espérance.
       Soit Y = g(|X|). Comme g est à valeurs positives, Y est une variable aléatoire positive.
       Son espérance est :                           Z
                                E[Y ] = E[g(|X|)] =      g(|X|) dP
                                                         Ω

    2. Décomposer l’intégrale.
       On sépare l’espace de probabilité Ω en deux parties disjointes : l’ensemble où |X| ≥ a et
       son complémentaire où |X| < a.
                               Z                          Z
                   E[g(|X|)] =                g(|X|) dP +                   g(|X|) dP
                                 {ω∈Ω | |X(ω)|≥a}            {ω∈Ω | |X(ω)|<a}


    3. Minorer l’expression.
       La fonction g est à valeurs dans [0, ∞[, donc l’intégrande g(|X|) est toujours positif ou



                                                    1
~~~

## Page 2

~~~text
      nul. Par conséquent, la deuxième intégrale est positive ou nulle. On peut donc la retirer
      pour obtenir une inégalité :
                                               Z
                                   E[g(|X|)] ≥         g(|X|) dP
                                                   {|X|≥a}

   4. Utiliser la croissance de g.
      Sur l’ensemble d’intégration {|X| ≥ a}, on a |X| ≥ a. Comme la fonction g est stricte-
      ment croissante sur [0, ∞[, on a :
                                            g(|X|) ≥ g(a)
      En substituant cette minoration dans l’intégrale :
                               Z                    Z
                                       g(|X|) dP ≥                 g(a) dP
                                  {|X|≥a}                {|X|≥a}

   5. Finaliser le calcul.
      g(a) est une constante par rapport à l’intégration. On peut donc la sortir :
                      Z                       Z
                              g(a) dP = g(a)          1 dP = g(a) · P(|X| ≥ a)
                        {|X|≥a}                {|X|≥a}

   6. Conclusion.
      En combinant les étapes, nous avons montré que :
                                    E[g(|X|)] ≥ g(a) · P(|X| ≥ a)
      Puisque a > 0 et g est strictement croissante, g(a) > g(0). L’énoncé précise g(0) ̸= 0, et
      comme g est à valeurs positives, on a g(0) > 0. Donc g(a) est strictement positif et on
      peut diviser par g(a) sans changer le sens de l’inégalité :
                                        E[g(|X|)]
                                                  ≥ P(|X| ≥ a)
                                          g(a)
      Ce qui est le résultat demandé.




Exercice 2 : Inégalité de Cantelli (variante)
Rappel de Cours : Inégalités à sens inverse
    Tandis que l’inégalité de Markov borne la probabilité d’un événement par une valeur maxi-
male, d’autres inégalités permettent de la borner par une valeur minimale. C’est le cas de
l’exercice 2. Ces inégalités sont souvent utiles pour montrer qu’une variable aléatoire a une
probabilité non nulle de s’éloigner de sa moyenne.
    La condition clé pour ce type d’inégalité est que la variable aléatoire soit bornée, ce qui
n’est pas requis pour l’inégalité de Markov standard.

   Énoncé : Soit h : R → [0, α]. Montrer que pour 0 ≤ a < α, on a :
                                                   E[h(X)] − a
                                  P(h(X) ≥ a) ≥
                                                      α−a

                                               2
~~~

## Page 3

~~~text
Démonstration
  La démarche est similaire à celle de l’exercice 1, mais cette fois nous allons chercher à
majorer l’espérance.
   1. Partir de la définition de l’espérance.
      Soit Y = h(X). Par hypothèse, Y est une variable aléatoire bornée, avec 0 ≤ Y ≤ α.
      On écrit son espérance en décomposant l’intégrale :
                                        Z             Z
                                E[Y ] =       Y dP +       Y dP
                                           {Y ≥a}            {Y <a}


   2. Majorer chaque partie de l’intégrale.
      Nous utilisons les bornes de Y sur chaque sous-ensemble :
      — Sur l’ensemble {Y ≥ a}, on a Y ≤ α. Donc :
                               Z             Z
                                     Y dP ≤        α dP = α · P(Y ≥ a)
                                {Y ≥a}          {Y ≥a}

      — Sur l’ensemble {Y < a}, on a (trivialement) Y < a. Donc :
                            Z               Z
                                   Y dP ≤         a dP = a · P(Y < a)
                                {Y <a}              {Y <a}

   3. Combiner les majorations.
      En additionnant les deux inégalités, on obtient une borne supérieure pour l’espérance :

                                E[Y ] ≤ α · P(Y ≥ a) + a · P(Y < a)

   4. Exprimer en fonction d’une seule probabilité.
      On sait que P(Y < a) = 1 − P(Y ≥ a). En substituant :

                             E[Y ] ≤ α · P(Y ≥ a) + a · (1 − P(Y ≥ a))

   5. Isoler le terme de probabilité.
      Il s’agit maintenant d’une manipulation algébrique pour isoler P(Y ≥ a) :

                                E[Y ] ≤ α · P(Y ≥ a) + a − a · P(Y ≥ a)
                            E[Y ] − a ≤ (α − a) · P(Y ≥ a)

   6. Conclusion.
      L’énoncé précise que a < α, donc (α − a) est un réel strictement positif. On peut diviser
      les deux côtés de l’inégalité par ce terme sans en changer le sens :

                                         E[Y ] − a
                                                   ≤ P(Y ≥ a)
                                          α−a
      En remplaçant Y par h(X), on obtient le résultat final :

                                                         E[h(X)] − a
                                    P(h(X) ≥ a) ≥
                                                            α−a




                                               3
~~~

## Page 4

~~~text
Exercice 3 : Formule de Huygens-König
Rappel de Cours : Définition de la Variance
                                                           2
   La variance d’une variable aléatoire X, notée V (X) ou σX , est une mesure de la dispersion
(ou de l’étalement) des valeurs de X autour de son espérance E[X].
   Formellement, la variance est définie comme l’espérance du carré de l’écart à la moyenne :
                                 2
                                   = V (X) = E (X − E[X])2
                                                            
                                σX

Une variance faible indique que les valeurs de X sont très regroupées autour de la moyenne,
tandis qu’une variance élevée indique qu’elles sont très dispersées.
   La formule de l’énoncé, connue sous le nom de formule de Huygens-König ou formule
de la variance développée, est une manière alternative et souvent plus simple de calculer la
variance. Elle est valable à condition que X admette un moment d’ordre 2 fini, c’est-à-dire
E[X 2 ] < ∞.

                                   2
   [cites tart]Énoncé :M ontrerqueσX = E[X 2 ] − E[X]2 si E[X 2 ] < +∞[cite : 8].

Démonstration
   La démonstration repose sur la linéarité de l’espérance.
   1. Partir de la définition de la variance.
      Par définition, en posant µ = E[X] pour alléger les notations :
                                          2
                                         σX = E[(X − µ)2 ]

   2. Développer le carré.
      On développe l’identité remarquable à l’intérieur de l’espérance :

                                    (X − µ)2 = X 2 − 2µX + µ2

      L’expression devient :
                                       2
                                      σX = E[X 2 − 2µX + µ2 ]
   3. Utiliser la linéarité de l’espérance.
      L’espérance d’une somme est la somme des espérances. On peut donc séparer les termes :

                           E[X 2 − 2µX + µ2 ] = E[X 2 ] − E[2µX] + E[µ2 ]

   4. Simplifier chaque terme.
      Rappelons que µ = E[X] est une constante (un nombre réel, pas une variable aléatoire).
      — E[X 2 ] reste tel quel.
      — E[2µX] = 2µ · E[X] = 2µ · µ = 2µ2 .
      — L’espérance d’une constante est la constante elle-même, donc E[µ2 ] = µ2 .
   5. Combiner les résultats.
      En substituant les termes simplifiés, on obtient :
                                        2
                                       σX = E[X 2 ] − 2µ2 + µ2
                                        2
                                       σX = E[X 2 ] − µ2



                                              4
~~~

## Page 5

~~~text
   6. Conclusion.
      En remplaçant µ par E[X], on aboutit à la formule de Huygens-König :
                                         2
                                        σX = E[X 2 ] − (E[X])2




Exercice 4 : Inégalité de Jensen (cas particulier)
Rappel de Cours : Positivité de la Variance et Inégalité de Jensen
   — Positivité de la variance : La variance, étant l’espérance d’une quantité au carré
     ((X − µ)2 ), est toujours positive ou nulle. C’est une propriété fondamentale :
                                                 2
                                                σX ≥0
     L’inégalité de l’exercice 4 est une conséquence directe de cette propriété.
   — Inégalité de Jensen : C’est un résultat beaucoup plus général. Pour toute variable
     aléatoire X et toute fonction convexe φ, on a :
                                          φ(E[X]) ≤ E[φ(X)]
      L’inégalité de l’exercice est un cas particulier de l’inégalité de Jensen, obtenu en choisis-
      sant la fonction φ(x) = x2 , qui est une fonction convexe.

   [cites tart]Énoncé :M ontrerqueE[X]2 ≤ E[X 2 ] si X admet une espérance (et un moment
d’ordre 2 pour que E[X 2 ] soit défini)[cite : 9].

Démonstration
   Cette démonstration est une conséquence immédiate de l’exercice 3.
   1. Partir de la positivité de la variance.
      Pour toute variable aléatoire X admettant un moment d’ordre 2, sa variance est bien
      définie et est toujours positive ou nulle :
                                                     2
                                            V (X) = σX ≥0
   2. Utiliser la formule de Huygens-König.
      D’après l’exercice 3, nous savons que :
                                         2
                                        σX = E[X 2 ] − (E[X])2
   3. Combiner les deux points.
      En substituant la formule de la variance dans l’inégalité de positivité, on obtient :
                                         E[X 2 ] − (E[X])2 ≥ 0
   4. Conclusion.
      En réarrangeant les termes, on trouve directement l’inégalité recherchée :
                                           E[X 2 ] ≥ (E[X])2
Cette inégalité montre que le moment d’ordre 2 est toujours supérieur ou égal au carré du
moment d’ordre 1.

                                                5
~~~

## Page 6

~~~text
Exercice 5 : Parité d’une Variable Aléatoire Binomiale
Rappel de Cours : Loi Binomiale et Formule du Binôme
   — Loi Binomiale B(n, p) : Elle modélise le nombre de succès k obtenus après la répétition
     de n épreuves de Bernoulli indépendantes, où la probabilité d’un succès est p. Sa loi de
     probabilité est donnée par :
                                   
                                   n k
                      P(X = k) =      p (1 − p)n−k , pour k ∈ {0, 1, . . . , n}
                                   k

   — Formule du binôme de Newton : Pour tous nombres a et b et tout entier n ≥ 0 :
                                       n  
                                   n
                                      X    n k n−k
                            (a + b) =         a b
                                      k=0
                                           k

       Cette formule est l’outil clé pour résoudre cet exercice de manière élégante.

    Énoncé : Soit X une v.a.r. qui suit une loi binomiale B(p, n). [cites tart]M ontrerquelaprobabilitpourqueX
[cite : 10, 11]

Démonstration
    La méthode consiste à utiliser astucieusement la formule du binôme de Newton pour isoler
les termes pairs.
    1. Exprimer la probabilité recherchée.
       Nous cherchons Ppair = P(X est pair), ce qui correspond à la somme des probabilités
       pour tous les k pairs :
                                     X                    X n
                        Ppair =               P(X = k) =          pk (1 − p)n−k
                                k pair, 0≤k≤n            k pair
                                                                k

    2. Utiliser la formule du binôme de Newton.
       Appliquons la formule du binôme avec a = p et b = 1 − p. La somme de toutes les
       probabilités doit valoir 1 :
                                                    n  
                                      n    n
                                                    X  n
                         (p + (1 − p)) = 1 = 1 =              pk (1 − p)n−k   (1)
                                                    k=0
                                                          k

       Appliquons maintenant la formule avec a = −p et b = 1 − p :
                                                n  
                                  n
                                               X
                                               n     n
                   (−p + (1 − p)) = (1 − 2p) =          (−p)k (1 − p)n−k
                                               k=0
                                                     k
                                                n         
                                                       k n
                                               X
                                             =     (−1)      pk (1 − p)n−k          (2)
                                               k=0
                                                          k

       Dans cette deuxième somme, les termes sont positifs pour k pair et négatifs pour k
       impair.




                                               6
~~~

## Page 7

~~~text
   3. Combiner les deux égalités.
      Additionnons les équations (1) et (2) :
                                            n
                                            X                    n
                                                                 X
                                      n
                         1 + (1 − 2p) =            P(X = k) +          (−1)k P(X = k)
                                             k=0                 k=0

                                                    n
                                                    X
                                             n
                                                            1 + (−1)k P(X = k)
                                                                     
                              1 + (1 − 2p) =
                                                    k=0
                                     k
      Analysons le terme (1 + (−1) ) :
      — Si k est pair, 1 + (−1)k = 1 + 1 = 2.
      — Si k est impair, 1 + (−1)k = 1 − 1 = 0.
      La somme ne retient donc que les termes pairs, qui sont multipliés par 2 :
                                           X
                           1 + (1 − 2p)n =     2 · P(X = k) = 2 · Ppair
                                                   k pair


   4. Conclusion.
      Il suffit maintenant d’isoler Ppair pour obtenir le résultat final :

                                                    1
                                          Ppair =     (1 + (1 − 2p)n )
                                                    2




Exercice 6 : Convergence de la Loi Binomiale Conditionnelle
Rappel de Cours : Approximation de Poisson
   — Loi de Poisson P(λ) : Elle modélise le nombre d’événements se produisant dans un
     intervalle de temps ou d’espace fixé, si ces événements se produisent avec une fréquence
     moyenne connue λ. Sa loi de probabilité est :

                                                     e−λ λk
                                   P(Y = k) =               ,   pour k ∈ N
                                                       k!
   — Théorème de convergence : Si Xn ∼ B(n, pn ) est une suite de variables aléatoires
     binomiales telle que n → ∞, pn → 0 et npn → λ (une constante), alors la loi de Xn
     converge vers la loi de Poisson P(λ). Formellement, pour tout entier j ≥ 0 :

                                                                 e−λ λj
                                          lim P(Xn = j) =
                                          n→∞                      j!

Partie 1 : Limite de la probabilité conditionnelle
   Énoncé : Soit Xn ∼ B(pn , n) avec λ = npn constant. Soit An = {Xn ≥ 1}, et soit
Y ∼ Poisson(λ). [cites tart]M ontrerquelimn→∞ P(Xn = j|An ) = P(Y = j|Y ≥ 1). [cite : 12]




                                                     7
~~~

## Page 8

~~~text
Démonstration
      1. Analyser le membre de gauche. Pour tout j ≥ 1 :
                                                           P({Xn = j} ∩ {Xn ≥ 1})     P(Xn = j)
            P(Xn = j|An ) = P(Xn = j|Xn ≥ 1) =                                    =
                                                                 P(Xn ≥ 1)          1 − P(Xn = 0)
      2. Calculer la limite. En utilisant le théorème de l’approximation de Poisson :
                                                                      −λ j
         — Limite du numérateur : limn→∞ P(Xn = j) = P(Y = j) = e j!λ .
         — Limite du dénominateur : limn→∞ (1 − P(Xn = 0)) = 1 − P(Y = 0) = 1 − e−λ .
         Comme la limite du dénominateur est non nulle (pour λ > 0), la limite du quotient est
         le quotient des limites :
                                                          P(Y = j)
                                    lim P(Xn = j|An ) =
                                   n→∞                     1 − e−λ
      3. Analyser le membre de droite. Par définition :
                                       P({Y = j} ∩ {Y ≥ 1})     P(Y = j)     P(Y = j)
                 P(Y = j|Y ≥ 1) =                           =              =
                                            P(Y ≥ 1)          1 − P(Y = 0)    1 − e−λ
      4. Conclusion. Les deux expressions étant identiques, l’égalité est démontrée.

Partie 2 : Espérance de l’écart absolu à la moyenne
                                                                                                    λ −λ
      Énoncé : On suppose que λ est un entier. [cites tart]M ontrerqueE[|Y-λ|] = 2λ e
                                                                                 (λ−1)!
                                                                                        . [cite :
13]

Démonstration
      1. Décomposer l’espérance. Par définition de l’espérance d’une variable discrète :
                             ∞
                             X
              E[|Y − λ|] =         |k − λ|P(Y = k)
                             k=0
                             λ−1
                             X                                                    ∞
                                                                                  X
                         =         (λ − k)P(Y = k) + |λ − λ|P(Y = λ) +                (k − λ)P(Y = k)
                                                     |      {z     }
                             k=0                                  =0             k=λ+1


      2. Utiliser une propriété de l’espérance. On sait que E[Y − λ] = E[Y ] − λ = λ − λ = 0.
                                          ∞
                                          X
                     0 = E[Y − λ] =             (k − λ)P(Y = k)
                                          k=0
                                          λ−1
                                          X                            ∞
                                                                       X
                                      =         (k − λ)P(Y = k) +          (k − λ)P(Y = k)
                                          k=0                          k=λ+1
                                            λ−1
                                            X                            ∞
                                                                         X
                                      =−          (λ − k)P(Y = k) +            (k − λ)P(Y = k)
                                            k=0                          k=λ+1
                                                                                P∞
         On en déduit que les deux sommes sont égales : λ−1
                                                        P
                                                          k=0 (λ − k)P(Y = k) =  k=λ+1 (k −
         λ)P(Y = k).
      3. Simplifier le calcul. L’espérance recherchée est la somme des deux termes, elle est
         donc égale à deux fois le second terme :
                                          ∞                                ∞
                                          X                                X               e−λ λk
                       E[|Y − λ|] = 2             (k − λ)P(Y = k) = 2            (k − λ)
                                          k=λ+1                           k=λ+1
                                                                                             k!

                                                       8
~~~

## Page 9

~~~text
    4. Manipuler la somme.
                                                                 "   ∞        ∞
                                                                                       #
                                                                      k              k
                                                                    λX       X     λ
                                          E[|Y − λ|] = 2e−λ        k −           λ
                                                             k=λ+1
                                                                    k! k=λ+1 k!
                                                            " ∞                    ∞
                                                                                            #
                                                                        k                 k
                                                              X       λ           X      λ
                                                     = 2e−λ                   −λ
                                                             k=λ+1
                                                                   (k −   1)!    k=λ+1
                                                                                         k!
       On pose j = k − 1 dans la première somme :
                                                                 "∞                      ∞
                                                                                                       #
                                                                  X λj+1                 X λk
                                                       = 2e−λ                     −λ
                                                                     j=λ
                                                                             j!         k=λ+1
                                                                                                k!
                                                                   "∞                 ∞
                                                                                                #
                                                                    X λj              X λk
                                                       = 2λe−λ                    −
                                                                       j=λ
                                                                             j!       k=λ+1
                                                                                              k!
                                                                   "            ∞
                                                                                              !            ∞
                                                                                                                    #
                                                                           λλ   X   λk                     X λk
                                                       = 2λe−λ                +                    −
                                                                           λ! k=λ+1 k!                 k=λ+1
                                                                                                               k!
                                                                   λλ            λλ
                                                       = 2λe−λ        = 2λe−λ
                                                                   λ!         λ(λ − 1)!
    5. Conclusion. Après simplification, on obtient le résultat :

                                                        2λλ e−λ
                                        E[|Y − λ|] =
                                                        (λ − 1)!


Exercice 7 : Formule de l’Espérance par la Survie
Rappel de Cours : Deux Visions de l’Espérance
    Pour une variable aléatoire X à valeurs dans l’ensemble des entiers naturels N, l’espérance
est classiquement définie comme la somme des valeurs pondérées par leur probabilité :
                                            ∞
                                            X
                                   E[X] =         k · P(X = k)
                                            k=0

Cette formule peut être vue comme une "somme par valeurs".
   L’exercice 7 présente une formule alternative, souvent appelée formule de la somme de
la queue de distribution (ou "tail-sum formula"). Elle exprime l’espérance en fonction de la
fonction de survie P(X > n).
                                            ∞
                                            X
                                   E[X] =       P(X > n)
                                             n=0
Cette vision est très puissante en théorie et s’avère souvent plus simple à manipuler, notamment
                                                                                        R∞
pour les variables aléatoires continues non-négatives où la formule devient E[X] = 0 P(X >
x)dx.
                                                                                              P∞
   Énoncé : Soit X une v.a. qui prend ses valeurs dans N. Montrer que E[X] =                    n=0 P(X > n).


Démonstration
   La démonstration repose sur une astuce classique : l’interversion de l’ordre de sommation
dans une somme double.

                                                  9
~~~

## Page 10

~~~text
1. Partir du membre de droite.
   Nous commençons par l’expression que nous souhaitons transformer :
                                              ∞
                                              X
                                                    P(X > n)
                                              n=0

2. Exprimer la probabilité comme une somme.
   La probabilité que X soit strictement plus grand que n est la somme des probabilités
   que X prenne n’importe quelle valeur entière de n + 1 à l’infini :
                                                         ∞
                                                         X
                                 P(X > n) =                      P(X = k)
                                                         k=n+1

   En substituant, on obtient une somme double :
                                    ∞              ∞
                                                                     !
                                    X              X
                                                          P(X = k)
                                       n=0     k=n+1

3. Intervertir l’ordre de sommation.
   Nous sommons sur tous les couples d’entiers (n, k) tels que n ≥ 0 et k ≥ n + 1. Cette
   condition est équivalente à k ≥ 1 et 0 ≤ n ≤ k − 1. Au lieu de sommer d’abord sur n
   puis sur k, nous pouvons sommer d’abord sur k puis sur n :
                                     ∞    k−1
                                                      !
                                    X     X
                                              P(X = k)
                                       k=1         n=0

   Visualisation : Imaginez un tableau infini. La somme initiale parcourt les lignes, la nou-
   velle somme parcourt les colonnes.
4. Calculer la somme intérieure.
   Dans la somme intérieure k−1
                              P
                                n=0 , le terme P(X = k) est une constante par rapport à
   l’indice de sommation n. On somme donc cette constante de n = 0 à n = k − 1, ce qui
   représente k termes.
                                k−1
                                X
                                    P(X = k) = k · P(X = k)
                                 n=0

5. Conclure.
   En substituant ce résultat dans l’expression principale, on obtient :
                                         ∞
                                         X
                                                   k · P(X = k)
                                             k=1

   Cette expression est la définition de l’espérance de X. Le terme pour k = 0 est nul
   (0 · P(X = 0) = 0), on peut donc faire commencer la somme à k = 0 sans changer le
   résultat :                       ∞
                                   X
                                      k · P(X = k) = E[X]
                                   k=0
   Nous avons ainsi montré que le membre de droite est égal au membre de gauche, ce qui
   achève la démonstration.




                                                   10
~~~

## Page 11

~~~text
Exercice 8 : Moments Factoriels de la Loi de Poisson
Rappel de Cours : Moments Factoriels
   Le moment factoriel d’ordre r d’une variable aléatoire X est l’espérance de sa "factorielle
descendante" :
                         E[X(X − 1)(X − 2) . . . (X − r + 1)]
Ces moments sont particulièrement utiles pour des lois discrètes comme la loi de Poisson ou la
loi binomiale, car leur calcul est souvent plus simple que celui des moments classiques E[X r ].
                                                                     −λ k
    La loi de Poisson P(λ) a pour loi de probabilité : P(X = k) = e k!λ pour k ∈ N.

   Énoncé : Soit X une variable aléatoire de loi de Poisson de paramètre λ. Montrer que pour
r ∈ N∗ \ {1}, on a E[X(X − 1) · · · (X − r + 1)] = λr . Note : La formule est en fait valide pour
tout entier r ≥ 1. La démonstration qui suit le prouve.

Démonstration
    1. Écrire l’espérance par définition.
                                                        ∞
                                                        X
                E[X(X − 1) . . . (X − r + 1)] =               k(k − 1) . . . (k − r + 1) · P(X = k)
                                                        k=0


    2. Simplifier le domaine de sommation.
       Le produit k(k − 1) . . . (k − r + 1) est nul pour tous les entiers k < r. La somme peut
       donc commencer à l’indice k = r :
                                  ∞
                                  X                                      e−λ λk
                                        k(k − 1) . . . (k − r + 1) ·
                                  k=r
                                                                           k!

    3. Simplifier les termes factoriels.
       On peut simplifier le quotient des termes factoriels :

                           k(k − 1) . . . (k − r + 1)   k!/(k − r)!      1
                                                      =             =
                                       k!                   k!        (k − r)!

       L’expression devient :
                                                  ∞
                                                  X e−λ λk
                                                  k=r
                                                         (k − r)!

    4. Manipuler la somme pour faire apparaître une série connue.
       On met en évidence les termes constants par rapport à k et on fait un changement de
       variable.                              ∞
                                          −λ
                                             X      λk
                                         e
                                             k=r
                                                 (k − r)!

       Factorisons λr pour faire apparaître λk−r :
                                                      ∞
                                                 −λ r
                                                     X     λk−r
                                             e     λ
                                                     k=r
                                                         (k − r)!




                                                   11
~~~

## Page 12

~~~text
  5. Changement d’indice.
     Posons un nouvel indice j = k − r. Lorsque k = r, j = 0. Lorsque k → ∞, j → ∞. La
     somme devient :                            ∞
                                          −λ r
                                               X   λj
                                         e λ
                                               j=0
                                                   j!

  6. Reconnaître
             P la λsérie    exponentielle.
     La somme ∞
                     j
                j=0 j! est le développement en série de Taylor de eλ .
  7. Conclusion.
     En substituant, on obtient :

                                      e−λ λr · eλ = λr (e−λ eλ ) = λr

     Le résultat est donc bien :

                                   E[X(X − 1) . . . (X − r + 1)] = λr


Exercice 9 : Propriétés des Variables à Variance Finie
Rappel de Cours : Variance et Moments
  — Une variable aléatoire X admet une variance si sa variance V (X) est finie.
  — Par la formule de Huygens-König, V (X) = E[X 2 ] − (E[X])2 . Pour que V (X) soit finie,
    il est nécessaire que le moment d’ordre 2, E[X 2 ], soit lui-même fini.
  — L’existence d’un moment d’ordre 2 implique l’existence du moment d’ordre 1 (l’espé-
    rance).
    Pour une variable à valeurs dans N, le moment d’ordre 2 est défini par la série : E[X 2 ] =
  — P
       ∞    2                          2
       k=0 k P(X = k). Dire que E[X ] est fini signifie que cette
                                                               P série converge.
  — Une propriété   des séries à termes positifs convergentes ( uk ) est que le reste d’ordre n,
    Rn = ∞
           P
              k=n+1 k , tend vers 0 lorsque n → ∞.
                    u

Partie 1 : Convergence du moment d’ordre 2
                          P∞      2
  Énoncé : Montrer que       k=0 k P(X = k) converge.


Démonstration
  C’est une conséquence directe de l’hypothèse.
  1. On suppose que X admet une variance, ce qui signifie V (X) < ∞.
  2. La variance est définie par V (X) = E[(X − E[X])2 ]. Pour qu’elle soit finie, il faut que
     l’espérance E[X] et le moment d’ordre 2, E[X 2 ], soient finis.
  3. Le moment d’ordre 2, E[X 2 ], est précisément la somme ∞          2
                                                               P
                                                                  k=0 k P(X = k).
  4. Donc, si X admet une variance, la série ∞       2
                                              P
                                                k=0 k P(X = k) converge nécessairement.


Partie 2 : Limite de la queue de distribution
  Énoncé : En déduire que limn→∞ n2 P(X > n) = 0.




                                                12
~~~

## Page 13

~~~text
Démonstration
   Cette preuve utilise le fait que le reste d’une série convergente tend vers zéro.
   1. D’après la partie 1, la série S = ∞         2
                                          P
                                             k=0 k P(X = k) converge. Soit Rn son reste d’ordre
      n:                                         ∞
                                                X
                                         Rn =        k 2 P(X = k)
                                                   k=n+1

      Puisque la série converge, on a limn→∞ Rn = 0.
   2. Considérons l’expression n2 P(X > n). En utilisant la définition de la probabilité de
      queue :
                                        ∞
                                        X                X∞
                       2              2
                      n P(X > n) = n        P(X = k) =        n2 P(X = k)
                                               k=n+1                 k=n+1

   3. Pour chaque terme de la somme, on a k ≥ n + 1, ce qui implique k 2 > n2 . On peut donc
      majorer chaque terme :
                                  n2 P(X = k) ≤ k 2 P(X = k)
   4. En sommant cette inégalité de k = n + 1 à l’infini, on obtient :
                                ∞
                                X                          ∞
                                                           X
                                         2
                                        n P(X = k) ≤               k 2 P(X = k)
                                k=n+1                      k=n+1

      Ce qui se traduit par :
                                               n2 P(X > n) ≤ Rn
   5. Comme n2 ≥ 0 et P(X > n) ≥ 0, on a l’encadrement :

                                             0 ≤ n2 P(X > n) ≤ Rn

      Puisque limn→∞ Rn = 0, par le théorème des gendarmes, on conclut :

                                              lim n2 P(X > n) = 0
                                             n→∞


Partie 3 : Autre formule pour le moment d’ordre 2
                                     P∞
   Énoncé : Montrer que E[X 2 ] =        k=0 (2k + 1)P(X > k).


Démonstration
   Cette démonstration utilise une transformation de somme, similaire à une sommation par
parties pour les séries (transformation d’Abel).
   1. On part de la définition de E[X 2 ] et on utilise l’astuce P(X = j) = P(X > j −1)−P(X >
      j) :
                                         ∞
                                         X
                                 2
                             E[X ] =           j 2 P(X = j)
                                         j=1
                                         ∞
                                         X
                                     =         j 2 (P(X > j − 1) − P(X > j))
                                         j=1




                                                    13
~~~

## Page 14

~~~text
   2. On sépare la somme en deux et on regroupe les termes par probabilité P(X > k).

               E[X 2 ] = 12 P(X > 0) − 12 P(X > 1)
                                                    

                       + 22 P(X > 1) − 22 P(X > 2)
                                                    

                       + 32 P(X > 2) − 32 P(X > 3) + . . .
                                                    

                       = 12 P(X > 0) + (22 − 12 )P(X > 1) + (32 − 22 )P(X > 2) + . . .
                         X∞
                              (k + 1)2 − k 2 P(X > k)
                                            
                       =
                         k=0


   3. On simplifie le terme (k + 1)2 − k 2 = (k 2 + 2k + 1) − k 2 = 2k + 1.
   4. On obtient donc le résultat final :
                                               ∞
                                               X
                                   E[X 2 ] =         (2k + 1)P(X > k)
                                               k=0




Exercice 10 : Inégalité de Bienaymé-Tchebychev
Rappel de Cours
  — Loi de Poisson P(λ) : Une variable aléatoire X suivant cette loi a pour espérance et
    variance :
                               E[X] = λ et V (X) = λ
  — Inégalité de Bienaymé-Tchebychev : Pour toute variable aléatoire X d’espérance µ
    et de variance σ 2 finies, et pour tout réel a > 0, on a :

                                                              σ2
                                        P(|X − µ| ≥ a) ≤
                                                              a2
      Cette inégalité donne une borne universelle (indépendante de la loi de X) sur la proba-
      bilité que X s’écarte de sa moyenne de plus d’une certaine quantité a.

   Énoncé : Soit X     Poisson(λ). Rappeler l’espérance et la variance de X, et montrer que
P(X ≤ λ/2) ≤ 4/λ.

Démonstration
   1. Identifier les paramètres et l’objectif.
      Pour une loi de Poisson, on a µ = E[X] = λ et σ 2 = V (X) = λ. Nous voulons majorer
      P(X ≤ λ/2).
   2. Relier l’événement à la forme de Tchebychev.
      L’inégalité de Tchebychev porte sur l’événement |X − µ| ≥ a. Nous devons montrer que
      notre événement {X ≤ λ/2} est inclus dans un événement de cette forme.

                                λ           λ                 λ
                          X≤      =⇒ X − λ ≤ − λ =⇒ X − λ ≤ −
                                2           2                 2

                                                14
~~~

## Page 15

~~~text
     Si X−λ est inférieur ou égal à −λ/2, alors sa valeur absolue est nécessairement supérieure
     ou égale à λ/2.
                                             λ                   λ
                                  X − λ ≤ − =⇒ |X − λ| ≥
                                             2                   2
     On a donc l’inclusion d’événements :
                                                             
                                          λ                   λ
                                     X≤       ⊆ |X − λ| ≥
                                          2                   2
  3. Appliquer la monotonie de la probabilité.
     Puisqu’un événement est inclus dans l’autre, sa probabilité est plus petite :
                                                             
                                       λ                      λ
                               P X≤         ≤ P |X − λ| ≥
                                       2                      2
  4. Appliquer l’inégalité de Bienaymé-Tchebychev.
     Nous pouvons maintenant majorer le membre de droite avec l’inégalité de Tchebychev,
     en posant a = λ/2 :                     
                                            λ      V (X)
                               P |X − λ| ≥      ≤
                                            2      (λ/2)2
  5. Substituer et conclure.
     En remplaçant V (X) par λ :
                                      λ      λ   4λ  4
                                         2
                                           = 2 = 2 =
                                    (λ/2)   λ /4 λ   λ
     En combinant toutes les étapes, on obtient :
                                                  
                                                 λ     4
                                       P X≤          ≤
                                                 2     λ


Exercice 11 : Loi Jointe de Variables Géométriques
Rappel de Cours
  — Mesure de probabilité discrète : Pour définir une mesure de probabilité sur un
    univers dénombrable Ω (comme N2 ), il faut et il suffit de vérifier deux points pour la
    fonction pω = P({ω}) :
     1. pω ≥ 0 pour tout ω ∈ Ω.
        P
     2.    ω∈Ω pω = 1.
  — Série géométrique : Pour tout réel r tel que |r| < 1, on a ∞        k    1
                                                                P
                                                                  k=0 r = 1−r .
  — Loi marginale : Si on connaît la loi jointe d’un couple de variables aléatoires (X, Y ),
    la loi de X seule (appelée loi marginale) s’obtient en sommant sur toutes les valeurs
    possibles de Y :                       X
                               P(X = i) =      P(X = i, Y = j)
                                               j

  — Indépendance : Deux variables X et Y sont indépendantes si et seulement si pour tout
    couple (i, j), P(X = i, Y = j) = P(X = i)P(Y = j).

Partie 1 : Vérification de la mesure de probabilité
  Énoncé : Montrer que pi,j = αβ(1 − α)i (1 − β)j définit une mesure de probabilité sur N2 .

                                             15
~~~

## Page 16

~~~text
Démonstration
    1. Positivité : Comme α, β ∈]0, 1[, tous les termes α, β, (1 − α) et (1 − β) sont strictement
       positifs. Donc pi,j ≥ 0 pour tout (i, j) ∈ N2 .
    2. Somme égale à 1 : On calcule la somme sur tout l’univers Ω = N2 .
                             X                  ∞ X
                                                X ∞
                                       pi,j =             αβ(1 − α)i (1 − β)j
                            (i,j)∈N2            i=0 j=0
                                                      ∞
                                                                           !      ∞
                                                                                               !
                                                      X                           X
                                           = αβ              (1 − α)i               (1 − β)j
                                                       i=0                        j=0


       Les deux sommes sont des séries géométriques convergentes car 0 < 1 − α < 1 et
       0 < 1 − β < 1.
                                        ∞
                                        X                           1        1
                                          (1 − α)i =                       =
                                        i=0
                                                               1 − (1 − α)   α
                                        ∞
                                        X                           1        1
                                              (1 − β)j =                   =
                                        j=0
                                                               1 − (1 − β)   β

       En substituant, la somme totale devient :
                                                             1 1
                                                   αβ ·       · =1
                                                             α β

Les deux conditions sont vérifiées, donc pi,j définit bien une mesure de probabilité.

Partie 2 : Lois marginales de X et Y
   Énoncé : Déterminer la loi de X((i, j)) = i et de Y ((i, j)) = j.

Démonstration
   — Loi de X : On somme sur toutes les valeurs possibles de j :
                                                ∞
                                                X                ∞
                                                                 X
                             P(X = i) =               pi,j =             αβ(1 − α)i (1 − β)j
                                                j=0              j=0
                                                                         ∞
                                                                                          !
                                                                         X
                                           = α(1 − α)i               β         (1 − β)j
                                                                         j=0
                                                                           
                                                             i          1
                                           = α(1 − α)                β·          = α(1 − α)i
                                                                        β

     On reconnaît la loi de probabilité d’une loi géométrique de paramètre α, notée G(α).
   — Loi de Y : Par un calcul symétrique, on trouve :

                                                P(Y = j) = β(1 − β)j

       Y suit une loi géométrique G(β). Remarque : On constate que P(X = i, Y = j) = P(X =
       i)P(Y = j), ce qui signifie que les variables X et Y sont indépendantes.


                                                       16
~~~

## Page 17

~~~text
Partie 3 : Calcul de probabilités
  Énoncé : Calculer P(X < Y ), P(X = Y ) et P(X > Y ).

Démonstration
  — Calcul de P(X = Y ) :
                                      ∞
                                      X                                ∞
                                                                       X
                    P(X = Y ) =             P(X = k, Y = k) =                αβ(1 − α)k (1 − β)k
                                      k=0                              k=0
                                            ∞
                                            X
                                  = αβ            [(1 − α)(1 − β)]k
                                            k=0

     C’est une série géométrique de raison r = (1 − α)(1 − β), avec |r| < 1.

                                         1                    αβ                αβ
          P(X = Y ) = αβ ·                         =                      =
                                1 − (1 − α)(1 − β)   1 − (1 − α − β + αβ)   α + β − αβ

  — Calcul de P(X < Y ) :
                    ∞ X
                    X ∞                                     ∞
                                                            X                 ∞
                                                                              X
     P(X < Y ) =                P(X = i, Y = j) =                 P(X = i)           P(Y = j) (par indépendance)
                    i=0 j=i+1                               i=0              j=i+1
                    ∞                   ∞
                                                              !
                    X                   X
                =         α(1 − α)i               β(1 − β)j
                    i=0                 j=i+1

                                                                               P∞             j    (1−β)i+1
     La somme intérieure est le reste d’une série géométrique :                   j=i+1 β(1−β) = β 1−(1−β) =
     (1 − β)i+1 .
                                ∞
                                X                                                ∞
                                                                                 X
                                                   i          i+1
              P(X < Y ) =             α(1 − α) (1 − β)              = α(1 − β)         [(1 − α)(1 − β)]i
                                i=0                                              i=0

                                                           1            α(1 − β)
                             = α(1 − β) ·                            =
                                                  1 − (1 − α)(1 − β)   α + β − αβ

  — Calcul de P(X > Y ) : Par symétrie, on peut intervertir les rôles de X et Y , et de α et
    β:
                                                      β(1 − α)
                          P(X > Y ) = P(Y < X) =
                                                     α + β − αβ
     On peut vérifier que la somme des trois probabilités vaut bien 1.




                                                       17
~~~

## Page 18

~~~text
Exercice 12 : Limite de la Probabilité d’Événements Dis-
joints
Rappel de Cours
     — Axiome de σ-additivité : Pour une suite (An )n≥1 d’événements deux à deux dis-
       joints, la probabilité de leur union est la somme de leurs probabilités :
                                            ∞
                                                  !    ∞
                                           [          X
                                       P       An =      P(An )
                                           n=1          n=1

       Séries convergentes : Une condition nécessaire pour qu’une série à termes positifs
     — P
         ∞
         n=1 un converge est que son terme général tende vers zéro :

                                                 lim un = 0
                                               n→∞



     Énoncé : Soit (An )n≥1 une suite d’événements deux à deux disjoints. Montrer que limn→∞ P(An ) =
0.

Démonstration
     La démonstration est une conséquence directe des axiomes des probabilités.
     1. Soit A = ∞
                  S
                    n=1 An . Puisque les An sont des événements, leur union A est aussi un
        événement de la tribu A.
     2. Par définition d’une mesure de probabilité, la probabilité de tout événement est bornée
        par 1. On a donc :
                                                    ∞
                                                          !
                                                    [
                                       P(A) = P        An ≤ 1
                                                      n=1

     3. L’hypothèse nous dit que les événements (An ) sont deux à deux disjoints. Nous pouvons
        donc appliquer l’axiome de σ-additivité :
                                           ∞
                                                  !    ∞
                                          [           X
                                       P      An =        P(An )
                                           n=1          n=1


     4. En combinant les deux points, on obtient que la série des probabilités est finie :
                                             ∞
                                             X
                                                   P(An ) ≤ 1
                                             n=1


     5. La série ∞
                P
                   n=1 P(An ) est une série à termes positifs dont la somme est finie. C’est donc
        une série convergente.
     6. Une condition nécessaire fondamentale pour la convergence d’une série est que son terme
        général doit tendre vers 0. On en déduit donc immédiatement :

                                             lim P(An ) = 0
                                             n→∞


Ceci conclut la démonstration.

                                                 18
~~~

## Page 19

~~~text
Exercice 13 : Familles Dénombrables d’Événements
Rappel de Cours
   — Ensemble dénombrable : Un ensemble est dit dénombrable s’il est fini ou s’il peut
     être mis en bijection avec l’ensemble des entiers naturels N. Une union dénombrable
     d’ensembles dénombrables est elle-même dénombrable.
   — Fonction de Répartition (F.d.R.) : La fonction de répartition FX d’une variable
     aléatoire X est définie par FX (x) = P(X ≤ x).
   — Points de discontinuité d’une F.d.R. : Une fonction de répartition est continue
     à droite en tout point. Ses points de discontinuité correspondent aux valeurs x0 pour
     lesquelles la variable aléatoire a une probabilité non nulle de se réaliser, i.e., P(X =
     x0 ) > 0. La valeur du saut en x0 est précisément cette probabilité : P(X = x0 ) =
     FX (x0 ) − limx→x−0 FX (x).

Partie 1 : Caractère dénombrable d’une famille d’événements
   Énoncé : Soit (Aβ )β∈B une famille d’événements deux à deux disjoints. Montrer que si
P(Aβ ) > 0 pour tout β ∈ B, alors l’ensemble des indices B est dénombrable.

Démonstration
   La démonstration suit l’astuce proposée dans l’énoncé.
   1. Construire une partition de B. Pour chaque entier n ≥ 1, définissons le sous-
      ensemble d’indices Bn par :
                                                         
                                                        1
                                  Bn = β ∈ B | P(Aβ ) >
                                                        n
      Tout indice β ∈ B a une probabilité P(Aβ ) > 0. Par la propriété d’Archimède, il existe
      un entier n tel que P(Aβ ) > 1/n. Par conséquent, chaque β ∈ B appartient à au moins
      un Bn . On peut donc écrire B comme l’union de tous les Bn :
                                                         ∞
                                                         [
                                                   B=          Bn
                                                         n=1

   2. Montrer que chaque Bn est fini. Soit un ensemble Bn fixé. Prenons k éléments
      distincts de Bn , notés β1 , . . . , βk . Les événements correspondants Aβ1 , . . . , Aβk sont deux
      à deux disjoints par hypothèse. La probabilité de leur union est donc la somme de leurs
      probabilités, et cette somme doit être inférieure ou égale à 1 :
                                                k
                                                      !    k
                                               [          X
                                          P       Aβi =      P(Aβi ) ≤ 1
                                           i=1            i=1

      Par définition de Bn , pour chaque i ∈ {1, . . . , k}, on a P(Aβi ) > 1/n.
                                          k                  k
                                          X                  X 1           k
                                                 P(Aβi ) >             =
                                          i=1                i=1
                                                                   n       n

      En combinant les deux inégalités, on a nk < 1, ce qui implique k < n. Cela signifie que
      l’on ne peut pas trouver n éléments (ou plus) dans Bn . L’ensemble Bn est donc fini pour
      tout n.

                                                    19
~~~

## Page 20

~~~text
   3. Conclusion. L’ensemble B est une union dénombrable d’ensembles finis. Une telle
      union est au plus dénombrable. Comme B est supposé infini dans le contexte de la
      question 2, B est donc dénombrable.

Partie 2 : Ensemble des points de discontinuité d’une F.d.R.
    Énoncé : En déduire que l’ensemble B des points de discontinuité d’une fonction de répar-
tition F est dénombrable.

Démonstration
   1. Soit B l’ensemble des points de discontinuité de F . Pour chaque x0 ∈ B, la fonction F
      présente un saut, ce qui correspond à une probabilité ponctuelle non nulle :

                                          P(X = x0 ) > 0

   2. Considérons la famille d’événements (Ax0 )x0 ∈B où Ax0 = {X = x0 }.
   3. Ces événements sont deux à deux disjoints. En effet, si x1 ̸= x2 , il est impossible que
      X prenne simultanément les deux valeurs, donc {X = x1 } ∩ {X = x2 } = ∅.
   4. Nous sommes exactement dans la situation de la Partie 1 : nous avons une famille
      d’événements (Ax0 )x0 ∈B deux à deux disjoints, et pour chaque indice x0 ∈ B, on a
      P(Ax0 ) > 0.
   5. D’après le résultat de la Partie 1, l’ensemble des indices, qui est ici l’ensemble B des
      points de discontinuité, est nécessairement dénombrable.




Exercice 14 : Probabilité ponctuelle pour une loi à densité
Rappel de Cours
   — Loi à densité : Une probabilité P sur R admet une densité f si, pour tout événement
     A (borélien), sa probabilité est donnée par l’intégrale de f sur A :
                                                Z
                                        P(A) =      f (x) dx
                                                   A
                                                            Rb
     En particulier, pour un intervalle [a, b], P([a, b]) = a f (x) dx.
   — Continuité de la probabilité : Pour une suite d’événements décroissante (Cn )n≥1
     (i.e., Cn+1 ⊆ Cn ), la probabilité de l’intersection est la limite des probabilités :
                                           ∞
                                                  !
                                          \
                                      P        Cn = lim P(Cn )
                                                       n→∞
                                        n=1



   Énoncé : Soit P une probabilité sur R admettant une densité f . Montrer que P({x0 }) = 0
pour tout x0 ∈ R.



                                              20
~~~

## Page 21

~~~text
Démonstration
   La démonstration utilise la continuité de la mesure de probabilité.
    1. Représenter le singleton comme une intersection.
       Pour un x0 ∈ R fixé, on peut l’écrire comme l’intersection d’une suite d’intervalles
       emboîtés dont la longueur tend vers 0. Soit la suite d’événements (Cn )n≥1 définie par :
                                                           
                                                          1
                                        Cn = x0 , x0 +
                                                          n

       Cette suite est décroissante (Cn+1 ⊆ Cn ) et son intersection est exactement le singleton
       {x0 } :
                                           ∞
                                           \
                                             Cn = {x0 }
                                             n=1

    2. Appliquer la continuité de la probabilité.
       D’après la propriété de continuité pour les suites décroissantes, on a :
                                                ∞
                                                      !
                                                \
                                 P({x0 }) = P      Cn = lim P(Cn )
                                                              n→∞
                                                   n=1


    3. Calculer la probabilité de l’intervalle Cn .
       Puisque la probabilité admet une densité f , on a :
                                                   Z x0 +1/n
                                                  1
                            P(Cn ) = P x0 , x0 +       =         f (x) dx
                                                  n        x0

    4. Calculer la limite de l’intégrale.
       On cherche la limite de cette intégrale lorsque n → ∞. Quand n → ∞, la longueur de
       l’intervalle d’intégration, 1/n, tend vers 0. L’intégrale d’une fonction (intégrable) sur un
       intervalle de longueur nulle est nulle.
                                              Z x0 +1/n
                                          lim           f (x) dx = 0
                                       n→∞    x0

    5. Conclusion.
       En combinant les étapes, on obtient :

                                       P({x0 }) = lim P(Cn ) = 0
                                                        n→∞

       Pour une variable aléatoire continue (à densité), la probabilité de tomber exactement
       sur une valeur ponctuelle est toujours nulle.


Exercice 15 : Fonction de Répartition d’une Loi Discrète
Rappel de Cours : Fonction de Répartition (F.d.R)
    Une fonction F : R → [0, 1] est une fonction de répartition d’une probabilité si et seulement
si elle vérifie les trois propriétés suivantes :
    1. Croissance : F est une fonction croissante.
    2. Limites aux bornes : limx→−∞ F (x) = 0 et limx→∞ F (x) = 1.

                                                   21
~~~

## Page 22

~~~text
    3. Continuité à droite : Pour tout x0 ∈ R, limx→x+0 F (x) = F (x0 ).
À partir d’une F.d.R. F , on peut calculer la probabilité de n’importe quel intervalle :
   — P(]a, b]) = F (b) − F (a)
   — P({a}) = F (a) − F (a− ) (où F (a− ) est la limite à gauche en a)
   — P([a, b[) = F (b− ) − F (a− )
                             P∞ 1
   Énoncé : Soit F (x) =       i=1 2i · 1[1/i,∞[ (x). Montrer que c’est une F.d.R. et calculer les
probabilités de plusieurs événements.

Partie 1 : Vérification que F est une F.d.R.
    1. Croissance : Pour chaque i, la fonction indicatrice x 7→ 1[1/i,∞[ (x) est croissante. La
       fonction F est une somme de fonctions croissantes avec des coefficients positifs (1/2i > 0),
       elle est donc elle-même croissante.
    2. Limites aux bornes :
       — PLorsque x → −∞, pour tout i ≥ 1, x < 1/i, donc 1[1/i,∞[ (x) = 0. Ainsi, limx→−∞ F (x) =
            ∞ 1
            i=1 2i · 0 = 0.
       — PLorsque x → ∞, pour tout i ≥ 1, x > 1/i, donc 1[1/i,∞[ (x) = 1. Ainsi, limx→∞ F (x) =
            ∞ 1
            i=1 2i . C’est une série géométrique de raison 1/2 et de premier terme 1/2, dont la
                        1/2
          somme est 1−1/2    = 1.
    3. Continuité à droite : La fonction F est une somme de fonctions en escalier. Chaque
       fonction x 7→ 1[1/i,∞[ (x) est continue à droite. Une somme (convergente) de fonctions
       continues à droite est continue à droite.
Les trois propriétés étant vérifiées, F est bien la fonction de répartition d’une mesure de pro-
babilité.

Partie 2 : Calcul de probabilités
    La fonction F est une fonction en escalier dont les sauts se situent aux points {1, 1/2, 1/3, . . . }.
La probabilité est donc concentrée sur ces points. La masse de probabilité en un point x = 1/i
est la hauteur du saut :
                                                                     1
                              P({1/i}) = F (1/i) − F ((1/i)− ) = i
                                                                     2
La probabilité est nulle partout ailleurs.
    a) P([1, ∞[) : Le seul point de masse dans cet intervalle est x = 1 (pour i = 1).
                                                                 1    1
                                        P([1, ∞[) = P({1}) =      1
                                                                    =
                                                                 2    2
   b) P([1/2, ∞[) : Les points de masse sont 1/2 et 1.
                                                                 1   1   1 1   3
                        P([1/2, ∞[) = P({1/2}) + P({1}) =          +   =  +  =
                                                                 22 21   4 2   4
    c) P({0}) : 0 ne fait pas partie des points {1/i | i ∈ N∗ }.

                                                  P({0}) = 0

   d) P([0, 1/2[) : Les points de masse dans cet intervalle sont {1/3, 1/4, 1/5, . . . }.
                                                    ∞                  ∞
                                                    X                  X 1
                                    P([0, 1/2[) =         P({1/i}) =
                                                    i=3                i=3
                                                                             2i

                                                    22
~~~

## Page 23

~~~text
         C’est une série géométrique de premier terme (1/2)3 = 1/8 et de raison 1/2.

                                        premier terme     1/8     1/8   1
                             Somme =                  =         =     =
                                          1 − raison    1 − 1/2   1/2   4

      e) P(] − ∞, 0[) : Il n’y a pas de points de masse négatifs.

                                             P(] − ∞, 0[) = 0

      f) P(]0, ∞[) : Tous les points de masse {1/i} sont strictement positifs.
                                                ∞                  ∞
                                                X                  X 1
                                  P(]0, ∞[) =         P({1/i}) =            =1
                                                i=1                i=1
                                                                       2i




Exercice 16 : Mesurabilité et Égalité Presque Sûre
Rappel de Cours
      — Fonction mesurable : Une fonction X : (Ω, F) → (R, B(R)) est dite mesurable si pour
        tout ensemble B de la tribu borélienne B(R), l’image réciproque X −1 (B) = {ω ∈ Ω |
        X(ω) ∈ B} est un événement de la tribu F.
      — Égalité presque sûre (p.s.) : On dit que deux variables aléatoires X et Y sont égales
        presque sûrement, noté X = Y p.s., si l’ensemble où elles diffèrent est de probabilité
        nulle : P({X ̸= Y }) = 0. L’ensemble {X ̸= Y } est appelé un ensemble négligeable.
      — Tribu complétée : La tribu A′ décrite dans l’énoncé est la complétée de A. Elle
        contient A ainsi que tous les sous-ensembles des ensembles négligeables de A. L’intérêt
        est que si un événement N est négligeable, alors tout sous-ensemble N ′ ⊆ N devient
        mesurable (et de probabilité nulle) dans la nouvelle tribu A′ .

   Énoncé : Soient X et Y deux applications telles que X = Y p.s. Montrer que X est
(A , B(R))-mesurable si et seulement si Y est (A′ , B(R))-mesurable.
  ′



Démonstration
  La preuve étant symétrique, il suffit de montrer une seule implication : Si X est A′ -
mesurable, alors Y est A′ -mesurable.
      1. Hypothèse : X est A′ -mesurable. Cela signifie que pour tout borélien B ∈ B(R), on a
         X −1 (B) ∈ A′ .
      2. Objectif : Montrer que pour tout borélien B ∈ B(R), l’ensemble Y −1 (B) appartient
         aussi à A′ .
      3. Décomposer l’ensemble Y −1 (B). On peut écrire Y −1 (B) en le séparant sur l’ensemble
         où X = Y et l’ensemble où X ̸= Y . Soit N = {X ̸= Y }. On sait que N est un ensemble
         négligeable, donc N ∈ A′ .

                        Y −1 (B) = Y −1 (B) ∩ {X = Y } ∪ Y −1 (B) ∩ {X ̸= Y }
                                                                            


                               Y −1 (B) = Y −1 (B) ∩ N c ∪ Y −1 (B) ∩ N
                                                                       


                                                  23
~~~

## Page 24

~~~text
4. Analyser chaque partie de l’union.
   — Première partie : Sur l’ensemble N c = {X = Y }, la condition Y (ω) ∈ B est
     équivalente à X(ω) ∈ B. Donc :

                                 Y −1 (B) ∩ N c = X −1 (B) ∩ N c

    Par hypothèse, X −1 (B) ∈ A′ . Comme N ∈ A′ , son complémentaire N c est aussi dans
    A′ . Puisqu’une tribu est stable par intersection, on a X −1 (B) ∩ N c ∈ A′ .
  — Seconde partie : Considérons l’ensemble E = Y −1 (B) ∩ N . Cet ensemble est un
    sous-ensemble de N .
                                            E⊆N
      Par hypothèse, N est un ensemble négligeable. Par définition de la tribu complétée
      A′ , tout sous-ensemble d’un ensemble négligeable appartient à A′ . Donc, E ∈ A′ .
5. Conclusion. Nous avons montré que Y −1 (B) est l’union de deux ensembles qui appar-
   tiennent tous les deux à la tribu A′ :

                         Y −1 (B) = (X −1 (B) ∩ N c ) ∪ (Y −1 (B) ∩ N )
                                    |      {z      } |         {z    }
                                           ∈A′               ∈A′


  Puisqu’une tribu est stable par union, on conclut que Y −1 (B) ∈ A′ . Ceci étant vrai pour
  tout borélien B, la fonction Y est bien A′ -mesurable. L’autre implication se prouve de
  manière identique en échangeant les rôles de X et Y .




                                           24
~~~
