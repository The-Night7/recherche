# Logique_slides_2.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1ABC_5KH0DQSME5quQ6tmyvQe-ohqRL6G) · Les deux lectures automatiques du PDF divergent sur les pages indiquées. Leur fac-similé accompagne le texte.

**Pages présentant un écart entre les deux extractions** — 1–21.

## Page 1

![Page 1 du PDF](../facsimiles/76cfcff0456c2118f9de3989.webp)

~~~text
                    Introduction
          Une définition de l’IA
            Applications de l’IA
 Outils informatiques pour l’IA
Outils mathématiques pour l’IA




                Éléments de base

                     Houcine Senoussi


                       April 18, 2016




              Houcine Senoussi      Éléments de base
~~~

## Page 2

![Page 2 du PDF](../facsimiles/657d1bfca8586d17c57c4d1e.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA
               Outils informatiques pour l’IA
              Outils mathématiques pour l’IA




1   Introduction

2   Une définition de l’IA

3   Applications de l’IA

4   Outils informatiques pour l’IA
      Rappels d’algorithmique

5   Outils mathématiques pour l’IA
      Éléments de logique
      Logique propositionnelle
      Logique des prédicats


                            Houcine Senoussi      Éléments de base
~~~

## Page 3

![Page 3 du PDF](../facsimiles/f79488a435fbc48e96cd8c61.webp)

~~~text
                                    Introduction
                          Une définition de l’IA
                            Applications de l’IA
                 Outils informatiques pour l’IA
                Outils mathématiques pour l’IA


Contenu du chapitre



  Le chapitre se compose de 4 paragraphes :
    1   Qu’est-ce que l’intelligence artificielle ?
    2   Applications de l’IA.
    3   Rappels d’algorithmique.
    4   Éléments de logique.




                              Houcine Senoussi      Éléments de base
~~~

## Page 4

![Page 4 du PDF](../facsimiles/e74d4bfc3098a7c75dd963fe.webp)

~~~text
                                    Introduction
                          Une définition de l’IA
                            Applications de l’IA
                 Outils informatiques pour l’IA
                Outils mathématiques pour l’IA


Qu’est-ce que l’intelligence artificielle ?


  L’objet de l’IA est double :
    1   comprendre les entités intelligentes.
    2   construire des entités intelligentes.
  Plusieurs définitions ont été données de l’IA. Dans ce cours nous
  allons lister un ensemble de tâches et nous poser les deux questions
  suivantes :
    1   Est-ce que cela suppose de l’intelligence ?
    2   Est-ce que la machine peut les exécuter efficacement ?
             Mieux ou aussi bien que l’homme ?



                              Houcine Senoussi      Éléments de base
~~~

## Page 5

![Page 5 du PDF](../facsimiles/43d0b20a54918de99c0e95f8.webp)

~~~text
                                    Introduction
                          Une définition de l’IA
                            Applications de l’IA
                 Outils informatiques pour l’IA
                Outils mathématiques pour l’IA


Qu’est-ce que l’intelligence artificielle ?-2


  Considérons les deux groupes de tâches suivantes :
      Groupe 1 :
         1   Faire des calculs longs, compliqués et précis :
                  Calcul du nombre Π avec un grand nombre de décimales.
                  Résoudre de grands systèmes d’équations.
                  ···
         2   Rechercher toutes les occurences d’un mot ou d’une phrase
             dans un grand nombre de documents (pages web par exemple).
         3   Trier un tableau de plusieurs centaines de milliers d’éléments
             (bacheliers par exemple).




                              Houcine Senoussi      Éléments de base
~~~

## Page 6

![Page 6 du PDF](../facsimiles/d07e37040d4ef16081238de4.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA
                Outils informatiques pour l’IA
               Outils mathématiques pour l’IA


Qu’est-ce que l’intelligence artificielle ?-3



      Groupe 2 :
        1   Jouer aux échecs.
        2   Conduire un véhicule.
        3   Reconnaı̂tre un visage dans une image.
        4   Discuter avec un humain.
        5   Trouver son chemin sans avoir à l’apprendre par coeur.




                             Houcine Senoussi      Éléments de base
~~~

## Page 7

![Page 7 du PDF](../facsimiles/99ce4a42c61d35d3940380b9.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA
                Outils informatiques pour l’IA
               Outils mathématiques pour l’IA


Qu’est-ce que l’intelligence artificielle ?-4


      Il est clair que pour le premier groupe de tâches la réponse
      aux deux questions est la suivante :
        1   La machine excelle dans ce genre de tâches.
        2   Ces tâches ne supposent aucune intelligence. La machine se
            contente d’exécuter des ordres de l’homme (le programmeur).
        3   Ces tâches supposent de la puissance. La machine en dispose
            grâce à ses composants électroniques.
      En revanche pour les tâches du deuxième groupe :
        1   Il y a besoin de : comprendre, raisonner, anticiper, analyser,
            être autonome, déduire, généraliser, comprendre, ...
        2   Ces facultés réunies forment ce qu’on appelle l’intelligence.



                             Houcine Senoussi      Éléments de base
~~~

## Page 8

![Page 8 du PDF](../facsimiles/999d1d6fd6549d18b3584407.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA
               Outils informatiques pour l’IA
              Outils mathématiques pour l’IA


Qu’est-ce que l’intelligence artificielle ?-5




      Nous caractériserons donc un programme (ou une machine)
      intelligent(e) par la possession de certaines de ces facultés.
      L’IA est la branche de l’informatique dont l’objectif principal
      est de construire des entités possédant ces facultés.
      La liste des facultés donnée ci-dessus non exhaustive.




                            Houcine Senoussi      Éléments de base
~~~

## Page 9

![Page 9 du PDF](../facsimiles/c6c4c676b85e735db88712f9.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA
                Outils informatiques pour l’IA
               Outils mathématiques pour l’IA


Qu’est-ce que l’intelligence artificielle ?-6


      Compte tenu de l’étendu du domaine, l’IA s’est décomposée
      en plusieurs sous-domaines :
        1   l’apprentissage automatique.
        2   la reconnaissance des formes (visages, écriture, scènes, ...).
        3   le traitement automatique du langage naturel.
        4   la planification.
        5   ···
      Ces sous-domaines ne s’excluent pas mutuellement. On les
      retrouve ensemble dans certaines applications (véhicule
      intelligent ou jeux par exemple).



                             Houcine Senoussi      Éléments de base
~~~

## Page 10

![Page 10 du PDF](../facsimiles/4b4c2c26fd016133d8bc15c3.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA
               Outils informatiques pour l’IA
              Outils mathématiques pour l’IA


Quelques applications de l’IA




      Véhicule intelligent.
      Jeux d’échecs (et autres jeux).
      Reconnaissance des mots manuscrits (et autres types de
      formes).




                            Houcine Senoussi      Éléments de base
~~~

## Page 11

![Page 11 du PDF](../facsimiles/cd5615c1ad77a779687847a3.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA    Rappels d’algorithmique
               Outils informatiques pour l’IA
              Outils mathématiques pour l’IA


Rappels d’algorithmique


      Un algorithme est une suite d’instructions servant à résoudre
      un problème.
      Complexité d’un algorithme : le nombre d’opérations
      élémentaires le composant.
      On calcule la complexité en fonction de la taille du problème
      (notée n).
      On présente la complexité sous la forme O(f (n))
          Exemples : O(n2 ), O(log (n)), O(2n ).




                            Houcine Senoussi      Éléments de base
~~~

## Page 12

![Page 12 du PDF](../facsimiles/39fcc78f56bbe73fa62a6c9a.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA    Rappels d’algorithmique
                Outils informatiques pour l’IA
               Outils mathématiques pour l’IA


Rappels d’algorithmique-2


      Une bonne complexité est logarithmique ou polynomiale (de
      degré faible).
      Un algorithme ayant une complexité exponentielle est
      inutilisable dans la pratique.
      Exercices :
        1   Calculer la complexité du tri à bulles.
        2   Calculer la complexité de la recherche dichotomique dans un
            tableau trié.
        3   Calculer le temps d’exécution d’un algorithme dont la
            complexité est n! pour différentes valeurs de n.



                             Houcine Senoussi      Éléments de base
~~~

## Page 13

![Page 13 du PDF](../facsimiles/ff064f9705256e2c42a58d20.webp)

~~~text
                                    Introduction
                          Une définition de l’IA
                            Applications de l’IA    Logique propositionnelle
                 Outils informatiques pour l’IA     Logique des prédicats
                Outils mathématiques pour l’IA


Éléments de logique


       Logique propositionnelle.
       Logique des prédicats.
  Pour les distinguer considérons les énoncés suivants :
       Tout homme est mortel.
       Il y a une matière que tous les élèves ont réussi sauf Pierre.
       En été il fait chaud.
       S’il pleut on va au cinéma.




                              Houcine Senoussi      Éléments de base
~~~

## Page 14

![Page 14 du PDF](../facsimiles/556995ccf30aa305f58d0a47.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA    Logique propositionnelle
                Outils informatiques pour l’IA     Logique des prédicats
               Outils mathématiques pour l’IA


Éléments de logique-2




  On constate que ce qui fait la différence entre les énoncés 3 et 4 et
  les énoncés 1 et 2est l’existence d’éléments variables (homme,
  matière, élève) dans les seconds.




                             Houcine Senoussi      Éléments de base
~~~

## Page 15

![Page 15 du PDF](../facsimiles/7d26b8a4d4c0496d1ecdf49f.webp)

~~~text
                                     Introduction
                           Une définition de l’IA
                             Applications de l’IA    Logique propositionnelle
                  Outils informatiques pour l’IA     Logique des prédicats
                 Outils mathématiques pour l’IA


Éléments de logique-3

  Logique propositionnelle
      Symbôles ayant une valeur de vérité : propositions.
      On a l’habitude de noter les propositions : p, q, r, · · ·
      Formation des formules bien formées :
           Une proposition est une fbf (un atome).
           Utilisation des connecteurs : ¬, ∨, ∧, =⇒, ⇐⇒ :
             1     Si F est une fbf alors ¬F est une fbf.
             2     Si F et G sont des fbf alors F ∨ G est une fbf.
             3     Si F et G sont des fbf alors F ∧ G est une fbf.
             4     Si F et G sont des fbf alors F =⇒ G est une fbf.
             5     Si F et G sont des fbf alors F ⇐⇒ G est une fbf.



                               Houcine Senoussi      Éléments de base
~~~

## Page 16

![Page 16 du PDF](../facsimiles/fcdca6e48d7680b85aa1e6f5.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA    Logique propositionnelle
               Outils informatiques pour l’IA     Logique des prédicats
              Outils mathématiques pour l’IA


Éléments de logique-5




  Logique propositionnelle-Exemples
      (p1 ∧ p2 ∧ p3 ) =⇒ q.
      (p ∧ ¬q) ∨ (¬p ∧ q).
      (¬p ∨ q) ∧ (¬q ∨ p).




                            Houcine Senoussi      Éléments de base
~~~

## Page 17

![Page 17 du PDF](../facsimiles/61236701efbf0833db07ae87.webp)

~~~text
                                 Introduction
                       Une définition de l’IA
                         Applications de l’IA    Logique propositionnelle
              Outils informatiques pour l’IA     Logique des prédicats
             Outils mathématiques pour l’IA


Éléments de logique-6


      Nous avons un ensemble V de variables et un ensemble C de
      constantes.
      Nous avons des fonctions :
          p : (V ∪ C ) × · · · × (V ∪ C ) −→ {Vrai, Faux}.
          p s’appelle un prédicat.
          n est l’arité du prédicat.
      Nous avons des fonctions :
          f : (V ∪ C ) × · · · × (V ∪ C ) −→ (V ∪ C ).
          f s’appelle un foncteur.
          n est l’arité du foncteur.



                           Houcine Senoussi      Éléments de base
~~~

## Page 18

![Page 18 du PDF](../facsimiles/76a9ee3842ba1b53981d23c8.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA    Logique propositionnelle
                Outils informatiques pour l’IA     Logique des prédicats
               Outils mathématiques pour l’IA


Éléments de logique-7

  Logique des prédicats-Exemples
      Si on considère l’ensemble des écrivains et des livres, nous
      avons :
            les foncteurs auteur, premier livre, · · ·
            les prédicats même auteur
       Si on considère l’ensemble des étudiants, des matières et des
       enseignants, nous avons :
            les foncteurs définis à partir de ”Le prof de telle matière est tel
            enseignant” ”Tel étudiant suit les cours de tel prof dans telle
            matière”, · · ·
            les prédicats définis à partir de ”Tel étudiant a validé telle
            matière”, ”Tel prof a enseigné telle matière à tel étudiant”,


                             Houcine Senoussi      Éléments de base
~~~

## Page 19

![Page 19 du PDF](../facsimiles/260226368ef0e750f4a29799.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA    Logique propositionnelle
               Outils informatiques pour l’IA     Logique des prédicats
              Outils mathématiques pour l’IA


Éléments de logique-8
  Logique des prédicats-Formules bien formées
      Nous définissons un terme de la manière suivante :
           Toute variable est un terme.
           Toute constante est un terme.
           Pour tout foncteur f d’arité n, pour tout n-uplet t1 , ..., tn ,
           f (t1 , ..., tn ) est un terme.
      Nous définissons les fbf de la manière suivante :
           Pour tout prédicat p d’arité n, pour tout n-uplet t1 , ..., tn ,
           f (t1 , ..., tn ) est une fbf (formule atomique).
           Si F est une fbf alors ¬F est une fbf.
           Si F et G sont des fbf alors F ∨ G , F ∧ G , F =⇒ G et
           F ⇐⇒ G sont des fbfs.
           Si F est une fbf et x une variable, alors ∀xF et ∃xF sont des
           fbfs.

                            Houcine Senoussi      Éléments de base
~~~

## Page 20

![Page 20 du PDF](../facsimiles/c0bce600fcd57a73a0349995.webp)

~~~text
                                   Introduction
                         Une définition de l’IA
                           Applications de l’IA    Logique propositionnelle
                Outils informatiques pour l’IA     Logique des prédicats
               Outils mathématiques pour l’IA


Éléments de logique-9
  Logique des prédicats-Exemples
      Traduisons à l’aide de la logique des prédicats les énoncés
      suivants :
            Tous les hommes sont mortels.
            Socrate est un homme.
            Il y a un étudiant qui n’a pas validé l’intelligence artificielle.
            Tous les étudiants qui ont suivi les cours d’IA ont validé la
            matière.
            Si la note obtenue par un étudiant dans une matière donnée
            est supérieure à 10 alors il valide la matière.
            S’il y a un chemin entre la ville x et la ville y et qu’il existe un
            chemin entre y et une ville z alors il existe un chemin entre x
            et z.
            Les liens de parenté du type grand père, grand mère, oncle,
            tante, cousin, · · ·
                             Houcine Senoussi      Éléments de base
~~~

## Page 21

![Page 21 du PDF](../facsimiles/960f36dd670306fdd6ef02a6.webp)

~~~text
                                  Introduction
                        Une définition de l’IA
                          Applications de l’IA    Logique propositionnelle
               Outils informatiques pour l’IA     Logique des prédicats
              Outils mathématiques pour l’IA


Éléments de logique-10




  Importance de la logique en IA
      C’est la base du raisonnement.
      Importance particulière des règles ”SI .... Alors”
      Première illustration : Langage PROLOG.




                            Houcine Senoussi      Éléments de base
~~~
