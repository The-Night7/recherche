# ALGEBRE LINEAIRE CORRIGÉ TD3.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1cZBL32zdo-aVmoKgbA5jjq0EtLCgj_gn) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                          Algèbre Linéaire Appliquée
                           Corrigé Détaillé du TD3
                          Représentation des nombres en machine

                                   Pour les étudiants ING1-GM

                                        Le 7 novembre 2025


Exercice 14 : Conversion en hexadécimal
Question : Convertir les nombres décimaux suivants en hexadécimal (base 16).

                                          Rappel du Cours
   Pour convertir un nombre x de la base 10 à la base 16, on traite séparément sa partie
   entière E et sa partie fractionnaire F .
      — Partie entière (E) : On utilise la méthode des divisions euclidiennes successives
          par 16. On lit les restes de bas en haut (Support de cours, Algorithme 3.1.1, page
          35).
      — Partie fractionnaire (F) : On utilise la méthode des multiplications successives
          par 16. On lit les parties entières obtenues de haut en bas (Support de cours,
          Algorithme 3.1.2, page 36).
      — Chiffres hexadécimaux : A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.


1. Conversion de 15,275
   Solution Détaillée
   Partie entière : E = 15.
                                         15 ÷ 16 = 0 reste 15
   Le reste est 15, qui correspond au chiffre F. Donc, 1510 = F16 .
   Partie fractionnaire : F = 0, 275.

                               0, 275 × 16 = 4, 4   → Partie entière = 4
                                 0, 4 × 16 = 6, 4   → Partie entière = 6
                                 0, 4 × 16 = 6, 4   → Partie entière = 6
                                          ..
                                           .

   La partie fractionnaire est 0, 466...16 .

   Conclusion
   15, 27510 = (F, 466...)16




                                                    1
~~~

## Page 2

~~~text
2. Conversion de 358,937
  Solution Détaillée
  Partie entière : E = 358.

                                      358 ÷ 16 = 22 reste 6
                                        22 ÷ 16 = 1 reste 6
                                         1 ÷ 16 = 0 reste 1

  En lisant les restes de bas en haut : 35810 = 16616 .
  Partie fractionnaire : F = 0, 937.

                       0, 937 × 16 = 14, 992     → Partie entière = 14 (E)
                       0, 992 × 16 = 15, 872     → Partie entière = 15 (F)
                       0, 872 × 16 = 13, 952     → Partie entière = 13 (D)
                                  ..
                                   .

  La partie fractionnaire est 0, EF D...16 .

  Conclusion
  358, 93710 ≈ (166, EF D)16


3. Conversion de 387,62
  Solution Détaillée
  Partie entière : E = 387.

                                      387 ÷ 16 = 24 reste 3
                                        24 ÷ 16 = 1 reste 8
                                         1 ÷ 16 = 0 reste 1

  En lisant les restes de bas en haut : 38710 = 18316 .
  Partie fractionnaire : F = 0, 62.

                         0, 62 × 16 = 9, 92    → Partie entière = 9
                         0, 92 × 16 = 14, 72    → Partie entière = 14 (E)
                         0, 72 × 16 = 11, 52    → Partie entière = 11 (B)
                         0, 52 × 16 = 8, 32    → Partie entière = 8
                                   ..
                                    .


  Conclusion
  387, 6210 ≈ (183, 9EB8...)16




                                                 2
~~~

## Page 3

~~~text
4. Conversion de 5233,618
  Solution Détaillée
  Partie entière : E = 5233.

                                    5233 ÷ 16 = 327 reste 1
                                     327 ÷ 16 = 20 reste 7
                                       20 ÷ 16 = 1 reste 4
                                        1 ÷ 16 = 0 reste 1

  En lisant les restes de bas en haut : 523310 = 147116 .
  Partie fractionnaire : F = 0, 618.

                       0, 618 × 16 = 9, 888    → Partie entière = 9
                       0, 888 × 16 = 14, 208    → Partie entière = 14 (E)
                       0, 208 × 16 = 3, 328    → Partie entière = 3
                                  ..
                                   .


  Conclusion
  5233, 61810 ≈ (1471, 9E3...)16




                                                3
~~~

## Page 4

~~~text
Exercice 15 : Représentation IEEE-754
Question : Calculer la représentation de 5,75 et 0,1 en simple et double précision.

                                         Rappel du Cours
   Un nombre est stocké au format IEEE-754 normalisé sous la forme x = (−1)s × (1, m)2 ×
   2e . Le format binaire est Signe (S) | Exposant décalé (E) | Fraction (m).
        — Simple Précision (32 bits) : 1 bit (S), 8 bits (E), 23 bits (m). Biais = 127. E = e+127.
        — Double Précision (64 bits) : 1 bit (S), 11 bits (E), 52 bits (m). Biais = 1023. E =
            e + 1023.
   (Support de cours, Table 3.1, page 39)


1. Représentation de 5,75

   Solution Détaillée

   Étape 1 : Conversion en binaire
        — Partie entière : 510 = 4 + 1 = 1 · 22 + 0 · 21 + 1 · 20 = 1012 .
        — Partie fractionnaire : 0, 7510 = 0, 5 + 0, 25 = 1 · 2−1 + 1 · 2−2 = 0, 112 .
        — Résultat : 5, 7510 = 101, 112 .
   Étape 2 : Normalisation On décale la virgule vers la gauche pour obtenir la forme 1, m ×
   2e :
                                      101, 112 = 1, 01112 × 22
   On identifie les composants : s = 0 (positif), e = 2, m = 0111.
   Étape 3 : Codage Simple Précision (32 bits)
      — S (1 bit) : 0
      — E (8 bits) : E = e+Biais = 2+127 = 12910 . 129 = 128+1 = 1·27 +1·20 = 100000012 .
      — m (23 bits) : On complète 0111 avec des zéros : 01110000000000000000000.
   Étape 4 : Codage Double Précision (64 bits)
      — S (1 bit) : 0
      — E (11 bits) : E = e + Biais = 2 + 1023 = 102510 . 1025 = 1024 + 1 = 1 · 210 + 1 · 20 =
         100000000012 .
      — m (52 bits) : On complète 0111 avec des zéros : 0111000...0.

   Conclusion
   Comme la conversion binaire de 5,75 est finie, la représentation est exacte.
     — Simple Précision : 0 | 10000001 | 01110000000000000000000
     — Double Précision : 0 | 10000000001 | 011100...0 (48 zéros)




                                                 4
~~~

## Page 5

~~~text
2. Représentation de 0,1

  Solution Détaillée

  Étape 1 : Conversion en binaire
     — Partie entière : 010 = 02 .
     — Partie fractionnaire : 0, 110 .

                             0, 1 × 2 = 0, 2 → 0
                             0, 2 × 2 = 0, 4 → 0
                             0, 4 × 2 = 0, 8 → 0
                             0, 8 × 2 = 1, 6 → 1
                             0, 6 × 2 = 1, 2 → 1
                             0, 2 × 2 = 0, 4 → 0   (Début de la répétition)

     — Résultat : 0, 110 = 0, 0001100110011...2 = 0, 000112 .
  Étape 2 : Normalisation On décale la virgule vers la droite :

                           0, 000110011...2 = 1, 100110011...2 × 2−4

  On identifie les composants : s = 0 (positif), e = −4, m = 100110011...

  Point Pédagogique (Important)

  La représentation binaire de 0,1 est infinie et périodique. Il y aura donc une erreur d’ar-
  rondi, car on ne peut pas stocker tous les bits.

  Solution Détaillée

  Étape 3 : Codage Simple Précision (32 bits)
     — S (1 bit) : 0
     — E (8 bits) : E = e + Biais = −4 + 127 = 12310 . 123 = 64 + 32 + 16 + 8 + 2 + 1 =
        0 · 128 + 11110112 = 011110112 .
     — m (23 bits) : La fraction infinie est m = |10011001100110011001100
                                                               {z          } |1001... Le
                                                                  23 bits
        24ème bit (le premier bit rejeté) est 1. On doit donc arrondir au plus près en ajou-
        tant 1 aux 23 bits gardés :
                                   10011001100110011001100
                                            +                     1
                                   10011001100110011001101
        La fraction stockée est 10011001100110011001101.
  Étape 4 : Codage Double Précision (64 bits)
     — S (1 bit) : 0
     — E (11 bits) : E = e + Biais = −4 + 1023 = 101910 . 1019 = 512 + 256 + 128 + 64 +
        32 + 16 + 8 + 2 + 1 = 29 + 28 + 27 + 26 + 25 + 24 + 23 + 21 + 20 . En 11 bits (avec
        210 = 1024) : E = 011111110112 .
     — m (52 bits) : La fraction est le motif ‘1001‘ répété 52 ÷ 4 = 13 fois. m =
        1001...1001
        |    {z    } |1001... Le 53ème bit est 1. On arrondit en ajoutant 1 :
            52 bits




                                               5
~~~

## Page 6

~~~text
                                       ...10011001
                                           +     1
                                       ...10011010
     La fraction stockée est 1001...10011010.

Conclusion
La représentation de 0,1 est approchée dans les deux cas.
   — Simple Précision : 0 | 01111011 | 10011001100110011001101
   — Double Précision : 0 | 01111111011 | 1001...10011010 (le motif 1001 12
      fois, suivi de 1010)




                                       6
~~~

## Page 7

~~~text
Exercice 16 : Système binaire simplifié (Facultatif)
Question : Analyser le code Python qui génère les nombres flottants d’un système simplifié.

                                       Rappel du Cours
   Le code Python (‘TD3-Exo16-TousNombresSaufDenormalises.py‘) simule un système en
   base 2 (radix = 2) avec :
       — p = 3 chiffres de mantisse au total.
       — Exposants e de emin = −2 à emax = 3.
   Un nombre normalisé s’écrit x = (1, m)2 × 2e . Avec p = 3, la mantisse a 3 chiffres au
   total (ex : 1, 002 ou 1, 112 ). La mantisse M (entière) va de M min = 2p−1 = 22 = 4 à
   M max = 2p − 1 = 23 − 1 = 7. La formule M × radix ∗ ∗(e − p + 1) calcule M × 2e−3+1 =
   M × 2e−2 = (M/4) × 2e .
       — M = 4 =⇒ (4/4) × 2e = 1, 002 × 2e
       — M = 5 =⇒ (5/4) × 2e = (1 + 1/4) × 2e = 1, 012 × 2e
       — M = 6 =⇒ (6/4) × 2e = (1 + 2/4) × 2e = 1, 102 × 2e
       — M = 7 =⇒ (7/4) × 2e = (1 + 3/4) × 2e = 1, 112 × 2e

   Solution Détaillée
   1. Retapez et lancez le script : Le script affiche un graphique avec des barres bleues
   représentant tous les nombres (positifs et négatifs) que ce système peut générer.
   2. Zoomer sur la zone proche de 0 : On observe un "trou" important entre 0 et le plus petit
   nombre positif normalisé. Ce plus petit nombre normalisé est obtenu pour l’exposant
   minimal (e = emin = −2) et la mantisse minimale (M = M min = 4) :

                         xmin_normal = 1, 002 × 2−2 = 1 × 0, 25 = 0, 25

   Il n’y a aucun nombre normalisé représentable entre 0 et 0,25 (ni entre 0 et -0,25).
   3. Suppression de la boucle pour les négatifs : Si on supprime la première boucle ‘for‘
   (celle avec ‘range(emax, emin - 1, -1)‘), on ne génère plus les nombres négatifs. Le gra-
   phique n’affichera que 0 et les barres bleues à droite de 0.
   4. Ajout des nombres sous-normalisés (dénormalisés) : Les nombres sous-normalisés
   (Support de cours, Déf. 3.2.3, page 38) comblent le "trou" autour de 0. Ils sont utilisés
   quand l’exposant est emin = −2 mais que la mantisse est de la forme 0, m2 (le ’1,’ im-
   plicite disparaît). Dans le code (‘TD3-Exo16-TousNombresAvecDenormalises.py‘), cela
   correspond aux boucles ajoutées :
       — e = emin
       — M va de 1 à Mmin-1 (soit 1, 2, 3) pour les positifs.
       — M va de -Mmin+1 à -1 (soit -3, -2, -1) pour les négatifs.
   Calculons ces nouveaux nombres (positifs) :
       — M = 1 =⇒ (1/4) × 2−2 = 0, 012 × 2−2 = 0, 00012 = 0, 0625
       — M = 2 =⇒ (2/4) × 2−2 = 0, 102 × 2−2 = 0, 00102 = 0, 125
       — M = 3 =⇒ (3/4) × 2−2 = 0, 112 × 2−2 = 0, 00112 = 0, 1875

   Conclusion
   En ajoutant les nombres sous-normalisés (0,0625, 0,125, 0,1875 et leurs négatifs), on
   comble le "trou" entre 0 et 0,25. L’espacement entre les nombres devient régulier près
   de 0, ce qui permet une "perte de précision gracieuse" (gradual underflow) plutôt qu’un
   arrêt brutal à 0,25.



                                               7
~~~

## Page 8

~~~text
Exercice 17 : Système en base β (Facultatif)
Question : Calculer le nombre de valeurs normalisées pour un système en base β, avec p places
de mantisse, et exposants E ∈ [Em , EM ].

                                         Rappel du Cours
   Pour β = 2 (notre cas IEEE-754), le bit implicite est 1. Pour β > 2 (comme β = 10), la
   convention est que le premier chiffre *après* la virgule est non nul (0, a1 a2 ...ap ).
   Un nombre normalisé s’écrit : x = (−1)s × (0, a1 a2 ...ap )β × β E avec a1 ̸= 0.

   Solution Détaillée
   Nous devons compter le nombre de combinaisons possibles pour s, E, et la mantisse.
      — Signes (s) : 2 choix (positif ou négatif).
      — Exposants (E) : Le nombre d’exposants disponibles est EM − Em + 1. Comme
         dans le cas binaire, on réserve les exposants extrêmes (min et max) pour les zéros,
         infinis et NaN (Support de cours, Remarque 20, page 37). Nombre d’exposants
         pour les normalisés : (EM − Em + 1) − 2 = EM − Em − 1.
      — Mantisses (0, a1 a2 ...ap ) :
         — a1 : ne peut pas être 0 (par définition de la normalisation pour β > 2). Il y a
             (β − 1) choix (de 1 à β − 1).
         — a2 , ..., ap : peuvent être n’importe quel chiffre de 0 à β − 1. Il y a β choix pour
             chacun des p − 1 chiffres, soit β p−1 combinaisons.
         Nombre total de mantisses : (β − 1) × β p−1 .
   Le nombre total de valeurs normalisées est le produit de ces possibilités :

                                2 × (EM − Em − 1) × (β − 1)β p−1
                           N = |{z}
                                    |    {z     } |      {z    }
                                signes      exposants        mantisses


   Conclusion
   Application numérique : β = 10, p = 3, Em = −15, EM = 16.
      — Signes : 2
      — Exposants : 16 − (−15) − 1 = 16 + 15 − 1 = 30
      — Mantisses : (10 − 1) × 103−1 = 9 × 102 = 900
   N = 2 × 30 × 900 = 54000.
   En ajoutant les deux zéros (positif et négatif), on obtient 54002 valeurs, ce qui corres-
   pond au corrigé.




                                                 8
~~~
