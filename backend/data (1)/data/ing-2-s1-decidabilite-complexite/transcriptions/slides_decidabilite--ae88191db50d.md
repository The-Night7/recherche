# slides_decidabilite.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1cCrw65C2S_NfXiIPNC9QdBaTnHg_MJds) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                Introduction
  Algorithmes et complexité
        Théorie des langages
                  Définitions
                  Propriétés
Machine de Turing universelle
         Problème de l’arrêt
                    P et NP




     Décidabilité et complexité

                Jean-Paul FOREST


                       2024-2025




                                   1 / 52
~~~

## Page 2

~~~text
                                  Introduction
                    Algorithmes et complexité
                          Théorie des langages
                                    Définitions
                                    Propriétés
                  Machine de Turing universelle
                           Problème de l’arrêt
                                      P et NP



1   Introduction
2   Algorithmes et complexité
3   Théorie des langages
4   Définitions
5   Propriétés
6   Machine de Turing universelle
7   Problème de l’arrêt
8   P et NP

                                                  2 / 52
~~~

## Page 3

~~~text
                                 Introduction
                   Algorithmes et complexité
                         Théorie des langages
                                   Définitions
                                   Propriétés
                 Machine de Turing universelle
                          Problème de l’arrêt
                                     P et NP


Objectif

  Question centrale
  Étant donné un problème P :
    1   peut-on le résoudre sur ordinateur ?
    2   et si oui, avec quel coût ?

  Résolution sur ordinateur : existence d’un algorithme.
  Décidabilité (problème décidable : soluble sur ordinateur)
  Coût de la résolution : en temps et en espace.
  Complexité (temporelle et spatiale)


                                                               3 / 52
~~~

## Page 4

~~~text
                             Introduction
               Algorithmes et complexité
                     Théorie des langages
                               Définitions
                               Propriétés
             Machine de Turing universelle
                      Problème de l’arrêt
                                 P et NP




Objectif du cours :
Présenter les concepts, les méthodes et les outils permettant pour
un problème P de répondre à cette (double) question centrale.




                                                                     4 / 52
~~~

## Page 5

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Rappels et définitions

  Un algorithme est une suite d’instructions servant à résoudre un
  problème.
  La complexité temporelle (resp. spatiale) caractérise le coût en
  temps (resp. en espace) d’un algorithme.
  La complexité (temporelle) d’un algorithme est le nombre
  d’opérations élémentaires qui le composent.
  Ce nombre d’opérations est calculé en fonction de la taille du
  problème notée n.
  Taille d’un problème : taille d’une instance du problème.
  Dans le cas du tri c’est le nombre d’éléments du tableau à trier.


                                                                      5 / 52
~~~

## Page 6

~~~text
                             Introduction
               Algorithmes et complexité
                     Théorie des langages
                               Définitions
                               Propriétés
             Machine de Turing universelle
                      Problème de l’arrêt
                                 P et NP




On donne la complexité sous la forme O(f (n))
Signification de cette notation : le nombre d’opérations a comme
terme de plus haut degré f (n).
Exemples : O(n2 ), O(n log n), O(2n ).




                                                                   6 / 52
~~~

## Page 7

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Complexité des algorithmes


  f (n) = O(g(n)) si ∃n0 ∈ N tels que pour n ≥ n0 , f (n) ≤ c.g(n).
  Autrement dit, f augmente au plus aussi vite que g.

  f (n) = Ω(g(n)) si g(n) = O(f (n))
  f augmente au moins aussi vite que g.

  f (n) = Θ(g(n)) si f (n) = O(g(n)) et f (n) = (g(n))
  f et g augmentent aussi vite l’une que l’autre.



                                                                      7 / 52
~~~

## Page 8

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Complexité des algorithmes - exemple 1



  Donnée : un tableau d’entiers de taille n
  Résultat : le même tableau trié

  Le tri par sélection est en O(n2 ).




                                                8 / 52
~~~

## Page 9

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Complexité des algorithmes - exemple 2


  Donnée : un tableau trié d’entiers de taille n et un entier e
  Résultat : l’indice le plus à gauche où insérer e pour que le tableau
  reste trié

  La recherche dichotomique est en O(ln n).
  https://www.youtube.com/watch?v=tgVSkMA8joQ




                                                                          9 / 52
~~~

## Page 10

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Complexité d’un problème




  La complexité d’un problème est celle du meilleur algorithme qui
  le résout.
  Le problème du tri est en Θ(n ln n).




                                                                     10 / 52
~~~

## Page 11

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Définitions

  Graphe
  Un graphe non orienté G(S, A) (ou G(V , E )) est constitué de
  deux ensembles :
  un ensemble S de sommets S = {s1 , . . . , sn }
  un ensemble A d’ arêtes A = {a1 , . . . , an }. Une arête ai est une
  paire de sommets {si1 , si2 }.

  Dans un graphe orienté, les paires de sommets sont remplacées
  par des couples de sommets (si1 , si2 ) appelés arcs.
  Un graphe (orienté ou non) peut être valué : à chaque liaison
  (arête ou arc) est attribué une valeur (une distance, un coût, ...).

                                                                         11 / 52
~~~

## Page 12

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions



  Chemin et cycle
  Chemin (cycle) eulérien
  Chemin (cycle) hamiltonien
  Sous-graphe et graphe partiel
  Graphe complet et clique




                                               12 / 52
~~~

## Page 13

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Définitions

  La logique propositionnelle est composée de :
  - propositions : symboles avec une valeur de vérité dans
  B = {0, 1} = {Faux , Vrai}.
  - opérateurs logiques :
      - 22 = 4 opérateurs unaires dont ¬ ;
      - 24 = 16 opérateurs binaires dont ∨, ∧, ⇒, ⇔, ↓ (non-ou
  Peirce arrow ou Quine dagger) et ↑ (non-et barre de Sheffer).

  {¬, ∨, ∧}, {¬, ∨}, {¬, ∧}, {↑} et {↓} sont des ensembles
  fonctionnels complets, i.e. ils suffisent pour exprimer n’importe
  quelle fonction de Bn → B.

                                                                      13 / 52
~~~

## Page 14

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions (2)

  Formule bien formée (fbf)
  Une proposition est une formule bien formée.
  Si A est une fbf, alors ¬A est une fbf.
  Si A et B sont des fbf, alors A ∨ B est une fbf.
  Si A et B sont des fbf, alors A ∧ B est une fbf.
  Si A et B sont des fbf, alors A ⇒ B est une fbf.
  Si A et B sont des fbf, alors A ⇔ B est une fbf.

  NB : analogie avec les expressions arithmétiques


                                                     14 / 52
~~~

## Page 15

~~~text
                                   Introduction
                     Algorithmes et complexité
                           Théorie des langages
                                     Définitions
                                     Propriétés
                   Machine de Turing universelle
                            Problème de l’arrêt
                                       P et NP


Définitions (3)

  Interprétation
  Étant donnée une fbf A, soit ∆A l’ensemble des propositions
  intervenant dans A. On appelle interprétation de A une fonction
  de ∆A dans {Vrai, Faux }. Autrement dit une interprétation de A
  est une valuation des propositions intervenant dans A.

  Satisfiabilité
  Étant donnée une fbf A et I une interprétation de A. On dit que A
  est satisfiable par I si A a la valeur Vrai lorque les propositions
  intervenant dans A prennent les valeurs que I leur associe.

                                                                        15 / 52
~~~

## Page 16

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Définitions (4)


  Modèle
  Étant donnée une fbf A et une interprétation I de A, I est un
  modèle de A si A est satisfiable par I.

  Formule insatisfiable
  Étant donnée une fbf A, A est dite insatisfiable si elle n’a pas de
  modèle.




                                                                        16 / 52
~~~

## Page 17

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Définitions (5)


  Littéral
  Étant donnée une proposition p, un littéral relatif à cette
  proposition est soit p soit ¬p.

  Clause
  Une clause C est une disjonction de littéraux l1 ∨ l2 ∨ . . . ∨ ln .

  NB : Le langage prolog raisonne automatiquement à partir de
  clauses particulières appelées des clauses de Horn.


                                                                         17 / 52
~~~

## Page 18

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Définitions (6)



  Forme normale conjonctive
  Une forme normale conjonctive (fnc) est une conjonction de
  clauses C1 ∧ C2 ∧ . . . ∧ Cn .

  NB : le problème de satisfiabilité d’une telle formule ressemble à un
  système d’inéquations linéaires




                                                                          18 / 52
~~~

## Page 19

~~~text
                             Introduction
               Algorithmes et complexité
                     Théorie des langages
                               Définitions
                               Propriétés
             Machine de Turing universelle
                      Problème de l’arrêt
                                 P et NP




Proposition
Toute formule logique peut être mise en fnc. De plus, la
transformation a une complexité linéaire.




                                                           19 / 52
~~~

## Page 20

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions
  Alphabet
  Un alphabet Σ est un ensemble fini de symboles.

  Mot
  Un mot w défini sur un alphabet Σ est une suite de symboles
  s1 , s2 , . . . , sn appartenant à l’alphabet Σ.
  (Le mot vide est noté ε.)

  Langage
  Un langage L défini sur un alphabet Σ est un ensemble (fini ou
  infini) de mots définis sur Σ.

                                                                   20 / 52
~~~

## Page 21

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Modèles de calcul




  - fonctions récursives
  - lamba-calcul
  - machines de Turing




                                                21 / 52
~~~

## Page 22

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Machine de Turing




  La définition suivante est inspirée du livre de Wolper Introduction à
  la calculabilité et compatible avec le logiciel JFLAP (version 7.1
  téléchargeable sur https://www.jflap.org/jflaptmp/)




                                                                          22 / 52
~~~

## Page 23

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Paramétrage JFLAP


  Preferences
  Set empty string character ε
  Preferences Turing machine preferences :
  - Enable transitions from final state : non
  - Accept by final state : oui
  - Accept by halting : non
  - Allow stay for tape head on transition : oui




                                                   23 / 52
~~~

## Page 24

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Machine de Turing
  Machine de Turing
  Une machine de Turing (déterministe) est définie par un septuplet
  (Q, Γ, Σ, δ, q0 , B, {qs , qe }) où :
  - Q est un ensemble fini d’états ;
  - Γ est un alphabet fini de ruban ;
  - Σ est un alphabet fini d’entrée ;
  - q0 ∈ Q est l’état initial ; (un triangle en JFLAP)
  - B ∈ Γ − Σ est le ‘symbole blanc’ (□ en JFLAP) ;
  - qs ∈ Q est l’état de succès et qe ∈ Q est l’état d’échec ;
  - δ : Q × Γ → Γ × {L, S, R} × Q une fonction de transition avec
  {L,S,R} ≡ {Left,Stay,Right}.

  NB : dans l’article de Turing, elle est appelée a-machine pour
  automatic machine                                                   24 / 52
~~~

## Page 25

~~~text
                                  Introduction
                    Algorithmes et complexité
                          Théorie des langages
                                    Définitions
                                    Propriétés
                  Machine de Turing universelle
                           Problème de l’arrêt
                                      P et NP


Machine de Turing (fonctionnement)
  Elle dispose d’un ruban bi-infini sur laquelle il est possible de lire et
  d’écrire.
  Elle dispose d’une tête de lecture/écriture.
  Elle reçoit en entrée un mot s0 s1 . . . sn où si ∈ Σ.
  Au départ elle est dans l’état q0 .
  Elle commence la lecture par le symbole le plus à gauche de la
  chaîne.
  À chaque fois qu’un symbole s est lu :
     - elle trouve la transition (q, s) → (s ′ , dep, q ′ ), où q est l’état en
  cours.
     - elle écrit s ′ .
     - elle effectue le déplacement dep.
     - elle passe dans l’état q ′ .
  Elle s’arrête lorsqu’elle atteint qs ou qe .                                  25 / 52
~~~

## Page 26

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Turing-complétude




  Tout système qui peut calculer n’importe quelle fonction calculable
  sur une machine de Turing est dit Turing-complet.




                                                                        26 / 52
~~~

## Page 27

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Machine de Turing non déterministe

  Machine de Turing non déterministe
  Une machine de Turing non déterministe est définie par un
  septuplet (Q, Γ, Σ, δ, q0 , B, {qs , qe }) : identique à une machine
  standard sauf que la fonction de transition est une fonction
  multivaluée.
  À partir d’une situation donnée (état + symbole lu), la MdT ‘a le
  choix’ entre plusieurs transitions.

  NB : dans l’article de Turing, elle est appelée c-machine pour
  choice machine


                                                                         27 / 52
~~~

## Page 28

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Machine de Turing à plusieurs rubans


  Machine de Turing à plusieurs rubans
  Une machine de Turing à k rubans est définie par un septuplet
  (Q, Γ, Σ, δ, q0 , B, {qs , qe }) identique à une machine standard sauf
  que la fonction de transition permet des écritures et des
  déplacements différents pour chaque ruban.

  À chaque étape la machine lit k symboles (1 symbole par ruban)
  et en fonction de l’état et des k symboles lus, elle écrit k symboles,
  effectue k déplacements et prend un nouvel état.


                                                                           28 / 52
~~~

## Page 29

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Bibliographie


  On computable numbers with an application to the
  Entscheidungsproblem (1936) :
  https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf
  The annotated Turing :
  http://theannotatedturing.com/toc.htm
  Math’s Fundamental Flaw :
  https://www.youtube.com/watch?v=HeQX2HjkcNo



                                                        29 / 52
~~~

## Page 30

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Bibliographie


  Voyage au pays des maths
  L’ Entscheidungsproblem ou la fin des mathématiques ?
  https://www.youtube.com/watch?v=Zci9m08HQws
  Le théorème de Gödel :
  https://www.youtube.com/watch?v=Brj1LC42vLM
  Sur la route de l’infini :
  https://www.youtube.com/watch?v=o79bss3Hc60



                                                          30 / 52
~~~

## Page 31

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Bibliographie




  History of undecidability :
  https://www.youtube.com/playlist?list=
  PLzH6n4zXuckpIQPv8hiHpJkSyv0fmXEYr




                                                31 / 52
~~~

## Page 32

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions


  Une machine de Turing M décide un langage si :
  - ∀x ∈ L, M(x ) = qs
  - ∀x ̸∈ L, M(x ) = qe

  i.e. si la machine s’arrête toujours en donnant la bonne réponse


  Un langage est dit décidable (ou récursif) s’il existe une machine
  de Turing qui le décide.



                                                                       32 / 52
~~~

## Page 33

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions

  Une machine de Turing M accepte un langage si :
  - ∀x ∈ L, M(x ) = qs
  - ∀x ̸∈ L, M(x ) =↗

  i.e. si la machine donne toujours la bonne réponse lorsqu’elle
  répond oui.


  Un langage est dit semi-décidable (ou récursivement
  énumérable) s’il existe une machine de Turing qui l’accepte.


                                                                   33 / 52
~~~

## Page 34

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Propriétés


  Si un langage est décidable (récursif) alors il est semi-décidable
  (récursivement énumérable).


  Si un langage L est décidable (récursif) alors son complémentaire L̄
  est aussi décidable.

  Un langage L est récursif si et seulement si L et son
  complémentaire L̄ sont semi-décidables.



                                                                         34 / 52
~~~

## Page 35

~~~text
                             Introduction
               Algorithmes et complexité
                     Théorie des langages
                               Définitions
                               Propriétés
             Machine de Turing universelle
                      Problème de l’arrêt
                                 P et NP




Une machine de Turing universelle est une machine de Turing à
deux rubans qui :
- interprète ce qu’elle reçoit en entrée comme la concaténation
d’une description M d’une machine de Turing et d’un mot w fourni
àM ;
- imite (simule) le comportment de M lorsque M reçoit w .




                                                                   35 / 52
~~~

## Page 36

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Fonctionnement

  Notons R1 et R2 les rubans de U.
  On inscrit sur R1 la description de la machine de Turing M (i.e le
  quadruplet (Q, Σ, δ, q0 ) ) et le mot w .
  Nous noterons M le mot contenant la description de la machine
  M. Le ruban R2 contiendra la configuration de M à tout instant :
  son état q et la position de la tête de lecture.
  La position de la tête de lecture est représentée par un couple
  (u, v ) tel avec w la concaténation de u et v .
  La tête de lecture de M est positionnée sur le premier symbole de
  v.


                                                                       36 / 52
~~~

## Page 37

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Fonctionnement (2)


  Pour simuler M, U procède comme suit :
  Elle récupère l’état en cours q (lecture de R2 ).
  Elle récupère le symbole lu s (lecture de R2 ).
  Elle récupère la transition associée au couple (q, s) (lecture de R1 ).
  Soit (q0 , s0 , d) le triplet qui définit cette transition.
  Elle écrit le symbole s0 (écriture sur R2 ).
  Elle effectue le déplacement d (écriture sur R2 ).
  Elle simule le passage à l’état q0 (écriture sur R2 ).



                                                                            37 / 52
~~~

## Page 38

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Problème de l’arrêt (halting)




  Données : une machine de Turing M et un mot w
  Question : M s’arrête-t-elle lorsqu’elle reçoit w en entrée ?
  (i.e. a-t-on M(x ) ̸=↗ ?)




                                                                  38 / 52
~~~

## Page 39

~~~text
                             Introduction
               Algorithmes et complexité
                     Théorie des langages
                               Définitions
                               Propriétés
             Machine de Turing universelle
                      Problème de l’arrêt
                                 P et NP




Propriétés
On associe à ce problème LH défini par
LH = {X = (M, x ) t.q. M(x ) ̸=↗}.




                                             39 / 52
~~~

## Page 40

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Propriétés




  LH est semi-décidable (récursivement énumérable).

  LH n’est pas décidable (récursif).




                                                      40 / 52
~~~

## Page 41

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Autres problèmes indécidables


      10ème problème de Hilbert :
      Soit un polynôme de plusieurs variables comme
      x 3 yz + 2y 4 z 2 − 7xy 5 z − 6, a-t-il des racines x , y , z ∈ N ?
      deux programmes calculent-ils la même fonction ?
      une ligne donnée d’un programme finira-t-elle par être
      exécutée ?
      quel est le programme le plus court qui calcule la même
      fonction qu’un autre programme ?



                                                                            41 / 52
~~~

## Page 42

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Objectif


  Proposer une classification des problèmes résolubles sur ordinateur
  (avec un algorithme) en se basant sur leurs complexités.

  Nous considérons plus spécifiquement les problèmes de décision,
  i.e. ceux dont le résultat est booléen.
  Un graphe G possède-t-il un chemin hamiltonien ?
  Une formule F est-elle satisfiable ?
  ...



                                                                        42 / 52
~~~

## Page 43

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions



  Définition
  Une machine de Turing déterministe (resp. non déterministe) est
  dite polynomialement bornée, s’il existe un polynome P, tel que,
  lorsque la machine reçoit en entrée un mot w , elle termine en un
  nombre d’étapes inférieur à P(|w |) où |w | est la longueur du mot
  w.




                                                                       43 / 52
~~~

## Page 44

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions


  Définition
  La classe P est composée de tous les langages décidés par des
  machines de Turing déterministes polynomialement bornées.

  Définition
  La classe NP est composée de tous les langages décidés par des
  machines de Turing non déterministes polynomialement bornées.




                                                                   44 / 52
~~~

## Page 45

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Définitions (2)

  Définition
  La classe P est l’ensemble des problèmes qui possèdent un
  algorithme de résolution de complexité au plus polynomiale.
  Autrement dit, une solution peut être trouvée en un temps
  polynomial.

  Définition
  La classe NP est l’ensemble des problèmes pour lesquels une
  solution peut être vérifiée en un temps polynomial. Autrement dit
  étant donné une instance du problème, le temps pour vérifier si
  elle est solution du problème est polynomial.

                                                                      45 / 52
~~~

## Page 46

~~~text
                                Introduction
                  Algorithmes et complexité
                        Théorie des langages
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                         Problème de l’arrêt
                                    P et NP


Propriétés et exemples

  Définition
  P ⊆ NP

  La majorité des chercheurs pensent que l’inclusion est stricte.

            P                                   NP
        recherche
            tri
      cycle eulérien             cycle hamiltonien
          2-SAT                         SAT
   optimisation linéaire        optimisation linéaire
         dans Q                       dans N
                                                                    46 / 52
~~~

## Page 47

~~~text
                              Introduction
                Algorithmes et complexité
                      Théorie des langages
                                Définitions
                                Propriétés
              Machine de Turing universelle
                       Problème de l’arrêt
                                  P et NP


Définitions

  Définition
  On dit qu’un problème P1 est polynomialement transformable
  en un problème P2 s’il existe un algorithme de complexité
  polynomiale pour transformer toute instance du problème P1 en
  une instance du problème P2 .

  Définition
  Un problème P0 est NP-complet si tout problème de la classe NP
  est polynomialement transformable en P0 .


                                                                   47 / 52
~~~

## Page 48

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Exemples


  Théorème de Cook-Levin (1971,1973)
  Le problème SAT est NP-complet, i.e. si SAT peut être résolu en
  temps polynomial, alors P = NP.


  3SAT (CNF avec au plus 3 littéraux par clause) est NP-complet.
  3SAT exact (CNF avec exactement 3 littéraux par clause) est
  NP-complet.



                                                                    48 / 52
~~~

## Page 49

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


Démonstration qu’un problème est NP-complet



  Montrer qu’un problème P1 est NP-complet s’effectue en 2
  étapes :
  - montrer que P1 est dans NP ;
  - montrer qu’un problème de référence P0 est polynomialement
  transformable en P1 .




                                                                 49 / 52
~~~

## Page 50

~~~text
                               Introduction
                 Algorithmes et complexité
                       Théorie des langages
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                        Problème de l’arrêt
                                   P et NP


21 problèmes NP-complets de Karp




  Reducibility among combinatorial problems 1972
  Richard Karp (prix Turing 1985)




                                                   50 / 52
~~~

## Page 51

~~~text
                            Introduction
              Algorithmes et complexité
                    Théorie des langages
                              Définitions
                              Propriétés
            Machine de Turing universelle
                     Problème de l’arrêt
                                P et NP


Polylog : What P vs NP is really about




  https://www.youtube.com/watch?v=6OPsH8PK7xM




                                                51 / 52
~~~

## Page 52

~~~text
                            Introduction
              Algorithmes et complexité
                    Théorie des langages
                              Définitions
                              Propriétés
            Machine de Turing universelle
                     Problème de l’arrêt
                                P et NP


P vs NP and the computational complexity zoo




  https://www.youtube.com/watch?v=YX40hbAHx3s




                                                52 / 52
~~~
