# Chap3-Classes-P-NP.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1EMBoou2Y-idnXDIRip_oVuMggGIFTtTS) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                       Classes de problèmes *



                                    ING2 MI
                                   2022-2023



* Ce cours est tiré d’un support déposé par   Houcine Senoussi
~~~

## Page 2

~~~text
1   Introduction


2 Classes P et NP



3 Problèmes NP-Complets




                    ING2 MI   Classes de Problèmes
~~~

## Page 3

~~~text
                             Introduction
                          Classes P et NP
                   Problèmes NP-Complets

Objectif


  Objectif :
  Proposer une classification des problèmes résolubles sur ordinateur
  (possédant un algorithme) en se basant sur leurs complexités.

  Précision :
  Nous considérons plus spécifiquement les problèmes de décision :
  ceux dont le résultat est binaire.
      Un graphe G possède-t-il un chemin hamiltonien ?
      Une formule F est-elle satifiable ?
      ...



                              ING2 MI       Classes de Problèmes
~~~

## Page 4

~~~text
                             Introduction
                          Classes P et NP
                   Problèmes NP-Complets

Définitions
  Définition :
  Une machine de Turing déterministe (resp. non déterministe) est
  dite polynomialement bornée, s’il existe un polynome (P), tel
  que, lorsque la machine reçoit en entrée un mot x , elle termine en
  un nombre d’étapes inférieur à P(|x|) où |x| est la longueur du
  mot x.

  Définition :
  La classe P est composée de tous les langages décidés par des
  machines de Turing déterministes polynomialement bornées.

  Définition :
  La classe NP est composée de tous les langages décidés par des
  machines de Turing non-déterministes polynomialement bornées.
                              ING2 MI       Classes de Problèmes
~~~

## Page 5

~~~text
                            Introduction
                         Classes P et NP
                  Problèmes NP-Complets

Définitions-2


  Définition :
  La classe P est l’ensemble des problèmes qui possèdent un
  algorithme de résolution de complexité au plus polynomiale.
  Autrement dit, une solution peut être trouvée en un temps
  polynomial.

  Définition :
  La classe NP est l’ensemble des problèmes pour lesquels une
  solution peut être vérifiée en un temps polynomial. Autrement dit
  étant donné une instance du problème, le temps pour vérifier si
  elle est solution du problème est polynomial.



                             ING2 MI       Classes de Problèmes
~~~

## Page 6

~~~text
                             Introduction
                          Classes P et NP
                   Problèmes NP-Complets

Propriétés et exemples

  Propriété :
  Nous avons P ⊆ NP.

       Les chercheurs ’pensent’ que cette inclusion est stricte mais il
       s’agit encore d’une conjecture.

   1   Dans la classe P on trouve par exemple :
           les problèmes de tri et de recherche,
           le problème 2 − SAT (voir premier TD),
           le problème du graphe eulérien.
   2   Dans la classe NP on trouve par exemple :
           le problème SAT ,
           le problème d’ordonnancement
           le problème du graphe hamiltonien (voyageur du commerce).
                              ING2 MI       Classes de Problèmes
~~~

## Page 7

~~~text
                             Introduction
                          Classes P et NP
                   Problèmes NP-Complets

Définitions


  Définition :
  On dit qu’un problème P1 est polynomialement transformable
  en un problème P2 s’il existe un algorithme de complexité
  polynomiale pour transformer toute instance du problème P1
  en une instance du problème P2.

  Définition :
  Un problème P0 est NP-Complet si tout problème de la classe
  NP est polynomialement transformable en P0.




                            ING2 MI         Classes de Problèmes
~~~

## Page 8

~~~text
                            Introduction
                         Classes P et NP
                  Problèmes NP-Complets

Problèmes NP-Complets Exemples




  Théorème de Cook :
  (Admis) Le problème SAT est NP-complet.

  Montrer que

      Le problème 3 − SAT est NP-Complet.
      Le problème 3 − SAT exact est NP-Complet.




                           ING2 MI         Classes de Problèmes
~~~

## Page 9

~~~text
                            Introduction
                         Classes P et NP
                  Problèmes NP-Complets

Problèmes NP-Complets : Démarche




     Pour démontrer qu’un problème P1 est NP-Complet :
         Partir d’un problème P0 dont on sait qu’il est NP-Complet.
         Démontrer que P0 est polynomialement transformable en P1.




                           ING2 MI         Classes de Problèmes
~~~

## Page 10

~~~text
                           Introduction
                        Classes P et NP
                 Problèmes NP-Complets

Problèmes NP-Complets : Démarche




   Pour démontrer que 3−SAT est NP-Complet :
      Partir de SAT qui est NP-Complet.
      Démontrer que SAT est polynomialement transformable en 3-SAT.




                          ING2 MI         Classes de Problèmes
~~~

## Page 11

~~~text
                             Introduction
                          Classes P et NP
                   Problèmes NP-Complets

Problèmes NP-Complets : Démarche




   Pour démontrer que 3−SAT exact est NP-Complet :
       Partir de 3-SAT qui est NP-Complet.
       Démontrer que 3-SAT est polynomialement transformable en 3-
       SAT exact.




                            ING2 MI         Classes de Problèmes
~~~
