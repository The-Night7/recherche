# fiche_revision_proba.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1K0t6zIVqPuYkey6pGrXRmoV7YTM7NvjA) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
             Fiche de Révision : Probabilités (ING1 GM)

                                    Basée sur les annales 2019-2024




1     1. Probabilités Conditionnelles (L'Incontournable)

Tombe systématiquement en Exercice 1 (Tests, Alarmes, Usines).


    Formules Clés
        Probabilité Conditionnelle :
                                                            P (A ∩ B)
                                                P (A|B) =
                                                              P (B)

        Formule des Probabilités Totales : Si (An ) est une partition de Ω :
                                   X                 X
                          P (B) =     P (B ∩ An ) =      P (B|An )P (An )
                                            n                   n


        Formule de Bayes (Inversion du conditionnement) :

                                                       P (B|Ak )P (Ak )
                                          P (Ak |B) = P
                                                       n P (B|An )P (An )



Astuce Examen :

     Dénis clairement tes événements (ex: M : Malade, T : Test positif).

     Fais un arbre si nécessaire pour visualiser P (B).

     Indépendance : A et B indépendants ⇐⇒ P (A ∩ B) = P (A)P (B).


2     2. Variables Aléatoires à Densité

Le c÷ur de l'examen. Savoir manipuler une fonction          f (x) avec une constante C .

2.1    Les Outils de Base
Soit X une v.a. de densité f .

                                    −∞ f (x)dx = 1 (Sert à trouver la constante C ).
                                   R +∞
     Condition de densité :

                                                                          −∞ f (t)dt.
                                                                         Rx
     Fonction de Répartition (F.R.) : FX (x) = P (X ≤ x) =

                                 −∞ xf (x)dx.
                             R +∞
     Espérance : E[X] =

                                                                               −∞ x f (x)dx − (E[X]) .
                                                                              R +∞
     Variance (Koenig-Huygens) : V ar(X) = E[X 2 ] − (E[X])2 =                    2                2




                                                      1
~~~

## Page 2

~~~text
2.2    Méthode : Changement de Variable (Crucial)
Comment trouver la loi de     Y = ϕ(X) (ex: Y = X 2 , Y = eX ) ?

    1. Passer par la Fonction de Répartition de Y :

                                       FY (y) = P (Y ≤ y) = P (ϕ(X) ≤ y)

                                               √
    2. Isoler X dans l'inégalité (ex: P (X ≤y)).
                                             √
    3. Réexprimer en fonction de FX (ex: FX ( y)).
    4. Dériver le résultat par rapport à y pour obtenir la densité fY (y).

3     3. Lois Usuelles à Connaître Par C÷ur

                              Loi           Densité f (x)           Espérance   Variance
                                              1                        a+b       (b−a)2
                     Uniforme U([a, b])      b−a · ⊮[a,b] (x)           2          12
                     Exponentielle E(λ)     λe−λx · ⊮R+ (x)             1
                                                                        λ
                                                                                    1
                                                                                   λ2
                                                        (x−µ)2
                      Normale N (µ, σ 2 )       √1 e−     2σ 2          µ          σ2
                                               σ 2π


Notes importantes :

     Loi Exponentielle : "Sans mémoire" =⇒ P (X > t + s|X > t) = P (X > s).

                                                                                  σ ∼ N (0, 1).
     Loi Normale Centrée Réduite (Z ∼ N (0, 1)) : Si X ∼ N (µ, σ 2 ), alors Z = X−µ


4     4. Convergences et Théorèmes Limites

Pour les questions d'approximation et de taille d'échantillon.


    Inégalités

        Markov (si X ≥ 0) : P (X ≥ a) ≤ E[X]
                                          a

        Bienaymé-Tchebychev (Incontournable pour trouver n) :

                                                                     V ar(X)
                                         P (|X − E[X]| ≥ ε) ≤
                                                                        ε2
          Souvent utilisé avec la moyenne empirique         X̄n :

                                                                     σ2
                                            P (|X̄n − µ| ≥ ε) ≤
                                                                     nε2


4.1    Théorème Central Limite (TCL)
Si (Xn ) i.i.d avec E[X] = µ et V ar(X) = σ 2 , alors pour n grand :
                                                X̄n − µ L
                                         Zn =      √ −  → N (0, 1)
                                                 σ/ n

Utilisation :
                                       b−µ
                 P (a ≤ X̄n ≤ b) ≈ Φ( σ/          √ ).
                                        √ ) − Φ( a−µ
                                          n     σ/ n




                                                        2
~~~

## Page 3

~~~text
5    5. Statistiques d'Ordre (Le Max)

Soient X1 , ..., Xn i.i.d. On pose Mn = max(X1 , ..., Xn ).
     Fonction de répartition du Max :

                         FMn (t) = P (Mn ≤ t) = P (X1 ≤ t ∩ ... ∩ Xn ≤ t) = [FX (t)]n

     Pour obtenir la densité du max, on dérive [FX (t)]n .




                                                     3
~~~
