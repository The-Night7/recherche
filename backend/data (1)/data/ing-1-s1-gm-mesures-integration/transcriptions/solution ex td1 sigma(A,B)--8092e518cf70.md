# solution ex td1 sigma(A,B).pdf

[Ouvrir l’original](https://drive.google.com/open?id=1b7Dgud15SNtTPJLfzXYkWTbCfAmmncrW) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
      Structure de la tribu engendrée par deux ensembles


  Énoncé de l’exercice
  Soient A et B deux sous-ensembles d’un univers Ω. Décrire explicitement la tribu
  engendrée par ces deux ensembles, notée σ(A, B).

Démonstration. Nous allons appliquer directement la Proposition sur la structure d’une
tribu finiment engendrée.
   1. Identification des paramètres :
      La famille génératrice est {A1 , A2 } avec A1 = A et A2 = B. Nous avons donc n = 2.
   2. Construction des "atomes" :
      La proposition
                   T nous dit de construire les atomes en considérant toutes les intersections
      de la forme 2i=1 Avi i où v = (v1 , v2 ) est un vecteur binaire dans {0, 1}2 . Les 2n = 22 = 4
      vecteurs binaires possibles sont (1, 1), (1, 0), (0, 1) et (0, 0).
         Calculons les 4 atomes correspondants, en rappelant que C 1 = C et C 0 = C c :
      — Pour v = (1, 1) : P1 := A11 ∩ A12 = A ∩ B
      — Pour v = (1, 0) : P2 := A11 ∩ A02 = A ∩ B c
      — Pour v = (0, 1) : P3 := A01 ∩ A12 = Ac ∩ B
      — Pour v = (0, 0) : P4 := A01 ∩ A02 = Ac ∩ B c
   3. Formation de la partition :
      Comme démontré dans le cours, ces quatre atomes forment une partition de Ω. Notons
      Pne la collection des atomes non vides parmi {P1 , P2 , P3 , P4 }.
   4. Conclusion sur la structure de la tribu :
      La proposition énonce que la tribu engendrée est l’ensemble de toutes les unions
      possibles des atomes non vides.
                                 S
         Formellement, σ(A, B) =    P ∈J P | J ⊆ Pne .




                                                1
~~~

## Page 2

~~~text
Illustration : Les 16 éléments de σ(A, B)

En supposant que les quatre atomes P1 , P2 , P3 , P4 sont tous non vides, la tribu engendrée
σ(A, B) contient exactement 24 = 16 éléments. Voici la liste exhaustive, montrant comment
chaque élément peut être exprimé à partir de A et B.
Unions de 0 ou 4 atomes (les éléments triviaux) :
   — ∅ (union de zéro atome)
   — Ω = P1 ∪ P 2 ∪ P 3 ∪ P 4
Unions de 1 atome (la partition de base) :
   — P1 = A ∩ B
   — P2 = A ∩ B c = A \ B
   — P3 = Ac ∩ B = B \ A
   — P4 = Ac ∩ B c = (A ∪ B)c
Unions de 2 atomes :
   — A = P1 ∪ P 2
   — B = P1 ∪ P3
   — Ac = P3 ∪ P4
   — B c = P2 ∪ P4
   — La différence symétrique : A∆B = (A \ B) ∪ (B \ A) = P2 ∪ P3
   — Le complémentaire de la différence symétrique : (A∆B)c = P1 ∪ P4
Unions de 3 atomes (les complémentaires des atomes) :
   — (A ∩ B)c = Ac ∪ B c = P2 ∪ P3 ∪ P4
   — (A \ B)c = Ac ∪ B = P1 ∪ P3 ∪ P4
   — (B \ A)c = B c ∪ A = P1 ∪ P2 ∪ P4
   — (A ∪ B) = (Ac ∩ B c )c = P1 ∪ P2 ∪ P3

                                                                                               ■




                                             2
~~~
