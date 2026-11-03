# TD1 Correction.pdf

[Ouvrir l’original](https://drive.google.com/open?id=16vg679ZITRAf2zYVSChBGdCOcM6jikdE) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                  CY TECH: Théorie des langages [cite: 1]
                      TD1 - Introduction [cite: 2, 3]


                                          2025-2026 [cite: 4]


Objectifs [cite : 5]
   • Introduction à la théorie des langages [cite : 6]
   • Grammaire [cite : 7]
   • Dérivation de mots [cite : 8]
   • Décomposition d’un problème en analyse lexicale et syntaxique [cite : 9]
    Rappels et notations [cite : 10] : On rappelle que le mot langage s’écrit sans u en fran-
çais[cite : 11].


   Point de Cours : Grammaires et Dérivations
   Grammaire Formelle (G) : Elle est définie par un quadruplet G = (V, T, S, P ) où :
     — V (Variables) : Symboles non-terminaux qui peuvent être remplacés.
     — T (Terminaux) : Symboles finaux du langage (mots de l’alphabet).
     — S (Axiome) : Le symbole de départ.
     — P (Règles) : Les règles de production (ex : A → aB).
   Dérivation : C’est l’action de remplacer successivement les variables par des terminaux
   ou d’autres variables en suivant les règles P , jusqu’à obtenir un mot valide du langage.


Exercice 1. Dérivation de règles [cite : 12, 13]
   En théorie des langages, quand les symboles sont déjà des suites de symboles, on parlera de
vocabulaire plutôt que d’alphabet et de phrases plutôt que de mots[cite : 14, 15].
   On considère le langage naturel (simplifié) suivant[cite : 16] :
   • Le vocabulaire A = {le, la, fille, raisin, cueille}[cite : 17].
   • Une phrase est de la forme groupe nominal verbe groupe nominal[cite : 18].
   • Un groupe nominal est de la forme déterminant nom[cite : 19].
   • Les déterminants sont la ou le[cite : 20].
   • Les noms sont fille ou raisin[cite : 21].
   • Le verbe est cueille[cite : 22].




                                                    1
~~~

## Page 2

~~~text
Question 1. Etablir la grammaire de ce langage. [cite : 23]
   Correction :
Posons S pour Phrase, GN pour Groupe Nominal, V pour Verbe, D pour Déterminant, et N
pour Nom.

                                          S → GN V GN
                                        GN → D N
                                          D → le | la
                                         N → fille | raisin
                                          V → cueille

Question 2. Montrer par dérivation que la fille cueille le raisin est une phrase
du langage. [cite : 24]
   Correction :

                                  S ⇒ GN V GN
                                    ⇒ D N V GN
                                    ⇒ la N V GN
                                    ⇒ la fille V GN
                                    ⇒ la fille cueille GN
                                    ⇒ la fille cueille D N
                                    ⇒ la fille cueille le N
                                    ⇒ la fille cueille le raisin

Question 3. Montrer que le raisin cueille la fille est une phrase du langage en
construisant l’arbre de dérivation correspondant. [cite : 25]
   Correction :
L’arbre se construit ainsi depuis la racine S :

           S
         / | \
       /   |   \
    GN     V    GN
   / \     |    / \
 D    N cueille D N
 |    |          | |
le raisin       la fille

Question 4. Que pensez-vous de la deuxième phrase ? [cite : 26]
   Correction : Elle est syntaxiquement correcte (elle respecte la structure de la grammaire)
mais sémantiquement incorrecte (le sens est absurde).




                                                  2
~~~

## Page 3

~~~text
Question 5. Existe-t-il des phrases grammaticalement incorrectes dans le lan-
gage ? Comment corriger la grammaire pour les interdire ? [cite : 27]
    Correction : Oui, on peut générer "le fille" ou "la raisin" (erreur d’accord). Pour corriger
cela, on sépare les genres masculin et féminin :
                                        GN → GNmasc | GNf em
                                   GNmasc → Dmasc Nmasc
                                    GNf em → Df em Nf em
                                     Dmasc → le
                                      Df em → la
                                     Nmasc → raisin
                                      Nf em → fille

Question 6. Combien de phrases différentes contient ce langage ? [cite : 28]
   Correction : Avec la grammaire d’origine, un GN a 2×2 = 4 possibilités. La phrase contient
2 GN et 1 Verbe unique. Donc 4 × 1 × 4 = 16 phrases possibles.


   Point de Cours : Analyse Lexicale vs Syntaxique

     — Analyse Lexicale : Reconnaît les "mots" ou lexèmes (Tokens) à partir des ca-
       ractères bruts (ex : identifier qu’une suite de chiffres est un ‘ENTIER‘). Utilise les
       Grammaires Régulières (Type 3).
     — Analyse Syntaxique : Vérifie que l’agencement de ces lexèmes forme des "phrases"
       valides selon les règles du langage. Utilise les Grammaires Hors-Contexte (Type 2).


Exercice 2. Analyse lexicale et syntaxique [cite : 30, 31]
    On considère un mini-langage défini par 10 règles portant sur l’alphabet, les identificateurs,
les nombres, les opérateurs et les expressions[cite : 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43].
On cherche les expressions syntaxiquement correctes[cite : 44].

Question 1. Décomposer ce problème en analyse lexicale et analyse syntaxique.
[cite : 45]
   1. Parmi les termes mentionnés, lesquels correspondent à des lexèmes ? [cite : 46]
Correction : Les lexèmes sont les unités de base : Identificateur, Nombre (entier ou décimal),
Opérateur, Symbole_Egal (=), Littéral, et Symbole_Concat (&).
    2. Pour chaque spécification, relève-t-elle de l’analyse lexicale ou syntaxique ?
[cite : 47]
Correction :
   — Analyse Lexicale : Règles 1, 2, 3, 4 et 7 (construction des lexèmes).
   — Analyse Syntaxique : Règles 5, 6, 8, 9 et 10 (agencement des expressions et affectations).
    3. Quelles grammaires peuvent correspondre à chacune de ces analyses ? [cite :
48]
Correction : L’analyse lexicale utilise une grammaire régulière (Type 3). L’analyse syntaxique
utilise une grammaire hors-contexte (Type 2).



                                                   3
~~~

## Page 4

~~~text
Exercice 3. Le langage SQL [cite : 50]
    Soit un sous-langage SQL simplifié[cite : 51] :
SELECT champ, ,champ FROM table WHERE condition; [cite : 52]
Avec des conditions utilisant OR, AND, =,>,<, et des constantes ’chaine’ ou entier[cite : 53,
54, 55, 56, 57, 58, 59]. Les champs et tables sont des identificateurs[cite : 60].

Question 1. Donner une grammaire permettant d’identifier les différents lexèmes
nécessaires pour les requêtes de ce langage SQL. [cite : 61, 62]
   Correction : (Grammaire Régulière)

            LEXEME → MOT_CLE | IDENT | OPER | COMP | CONST | PONCT
          MOT_CLE → SELECT | FROM | WHERE
               OPER → OR | AND
               COMP →=|>|<
              PONCT →, |; | (|)

*(Note : On omet la définition détaillée lettre par lettre de IDENT et CONST pour la lisibilité,
mais elles relèvent aussi du type 3).*

Question 2. Proposer une grammaire hors-contexte qui reconnait les requêtes
syntaxiquement bien formées. [cite : 63, 64]
   Correction : Les lexèmes deviennent les terminaux[cite : 65].

                         S → SELECT Lchamps FROM IDENT WHERE C ;
                  Lchamps → IDENT | IDENT , Lchamps
                        C → IDENT COMP CONST | ( C OPER C )
                  CONST → CHAINE | ENTIER




Exercice 4. Langages binaires [cite : 66, 67]
   Soit A = {a, b} un alphabet binaire[cite : 68].

Question 1. Proposer une grammaire formelle définissant chacun des langages
suivants : [cite : 69]
  1. Le langage des mots de taille 6 : A6 [cite : 70]
Correction : S → CCCCCC avec C → a | b
  2. Le langage de tous les mots : A∗ [cite : 71]
Correction : S → aS | bS | ϵ
  3. Mots commencant par a et finissant par b : {a · u · b | u ∈ A∗ } [cite : 72]
Correction : S → aM b avec M → aM | bM | ϵ
  4. Le langage des palindromes [cite : 73]
Correction : S → aSa | bSb | a | b | ϵ
  5. Mots tels que ’a’ n’est jamais suivi d’un autre ’a’ [cite : 74, 75]
Correction : S → bS | aA | ϵ avec A → bS | ϵ

                                                4
~~~

## Page 5

~~~text
   6. L’intersection des deux langages précédents [cite : 76]
Correction : (Palindromes sans double ’a’).
S → bSb | abSba | a | b | ϵ
  7. Le langage des mots contenant autant de a que de b [cite : 77]
Correction : S → SS | aSb | bSa | ϵ




                                          5
~~~
