# exercice 3 - td 4 - CORRECTION.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1TBGnlywIUBt3Ieauqm7qdbutwUnjSlee) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Exercice 1. Soient X et Y deux variables aléatoires réelles indépendantes telles que X + Y = α, où α ∈ R
est une constante (presque sûrement). Montrer que X et Y sont des variables aléatoires constantes presque
sûrement.
   Solution : On suppose que X et Y sont indépendantes et que X + Y = α, où α ∈ R est une constante
(presque sûrement). On veut prouver que X est une variable aléatoire constante p.s.
   1. Stratégie de la preuve
   Rappel (Exercice 2) : Nous avons prouvé qu’une v.a. X est constante p.s. si et seulement si sa
fonction de répartition FX (c) ne prend que les valeurs 0 ou 1 (c’est-à-dire ∀c ∈ R, FX (c) ∈ {0, 1}).
   Notre but est donc de prouver que pour un c ∈ R quelconque, FX (c) = (FX (c))2 . Cette équation
(p = p2 ) n’admet que 0 et 1 comme solutions, ce qui prouvera le résultat.
   2. Utilisation de l’indépendance
   De l’hypothèse X + Y = α, on tire Y = α − X. L’hypothèse d’indépendance devient : X et (α − X)
sont indépendantes.
   Par le lemme de l’indépendance (ou lemme de transformation), cela signifie que pour toutes
fonctions f et g (de R dans R) mesurables et bornées :

                                 E[f (X)g(α − X)] = E[f (X)]E[g(α − X)]

   3. Choix des fonctions f et g
   Soit c ∈ R fixé. Nous voulons obtenir FX (c) = P(X ≤ c) = E[1{X≤c} ].
   — Posons fc = 1[c,+∞[ . Cette fonction est mesurable car l’ensemble ] − ∞, c] est un borélien (un fermé
      de R). Elle est bornée par 1.
   — Nous avons besoin d’une fonction gc telle que fc (X) et gc (α − X) soient la même variable aléatoire.
      On cherche donc gc telle que gc (α − X) = fc (X) = 1{X≤c} .
          Pour trouver gc (y), posons y = α − x, ce qui donne x = α − y. La condition x ≤ c devient
      α − y ≤ c, ce qui est équivalent à α − c ≤ y.
   — On choisit donc gc = 1[α−c,+∞[ . Cette fonction est mesurable (car [α − c, +∞[ est un borélien) et
      bornée par 1.
   4. Application et Calcul
   Puisque fc et gc sont mesurables et bornées, on peut appliquer la formule d’indépendance :

                               E[fc (X)gc (α − X)] = E[fc (X)]E[gc (α − X)]

   Calculons rigoureusement chaque terme de cette égalité :
   — Terme de gauche : Par notre choix de gc , on a gc (α − X) = 1{α−X≥α−c} = 1{X≤c} .

                   E[fc (X)gc (α − X)] = E[1{X≤c} · 1{X≤c} ] = E[1{X≤c} ] = P(X ≤ c) = FX (c)

   — Terme de droite : On calcule chaque espérance séparément.

                                          E[fc (X)] = E[1{X≤c} ] = FX (c)

                               E[gc (α − X)] = E[1{α−X≥α−c} ] = E[1{X≤c} ] = FX (c)
      Le produit est donc FX (c) · FX (c) = (FX (c))2 .
   5. Conclusion
   L’égalité d’indépendance devient donc :

                                             FX (c) = (FX (c))2

Cette équation est vraie pour n’importe quel c ∈ R fixé. La seule solution à p = p2 est p = 0 ou p = 1.
   On a donc bien ∀c ∈ R, FX (c) ∈ {0, 1}.
   D’après le résultat de l’Exercice 2, cela implique que X est constante presque sûrement.
   (Puisque Y = α − X, Y est aussi constante p.s.)

                                                      1
~~~
