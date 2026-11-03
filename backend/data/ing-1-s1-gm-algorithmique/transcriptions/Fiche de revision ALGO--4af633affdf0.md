# Fiche de revision ALGO.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1um0MPCXfRh2G4Hl34lz3eKO8Ip3FAEvD) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
               Fiche de Révision : Algorithmique
                            Tri, Complexité, Structures de Données & Récursivité



1     Analyse d’Algorithmes
1.1     1. Complexité (Temps & Espace)
L’efficacité se mesure en nombre d’opérations élémentaires en fonction de la taille de l’entrée (n).
  — Grand O (O) : Borne supérieure (pire des cas). C’est celle qu’on utilise le plus souvent pour garantir qu’un
       programme ne sera pas trop lent.
  — Ordres de grandeur usuels (du plus rapide au plus lent) :

                                   O(1) < O(log n) < O(n) < O(n log n) < O(n2 ) < O(2n )

1.2     2. Invariant de Boucle (Preuve de Correction)
Pour prouver qu’une boucle fait bien ce qu’elle doit faire, on utilise un invariant (propriété vraie tout le temps). Il faut
prouver 3 points :
   1. Initialisation : Vrai avant la première itération.
   2. Conservation : Si vrai à l’étape k, alors vrai à l’étape k + 1.
   3. Terminaison : Quand la boucle s’arrête, l’invariant nous donne le résultat voulu.


2     Les Algorithmes de Tri (Comparaison)

             Algorithme            Meilleur       Moyen          Pire
                                                                            Principe clé
                                                       2             2
             Insertion               O(n)         O(n )          O(n )      Comme un jeu de cartes : on in-
                                                                            sère l’élément courant à sa place
                                                                            dans la partie triée.
             Fusion (Merge)        O(n log n)   O(n log n)    O(n log n)    Diviser pour régner : coupe en
                                                                            2, trie récursivement, puis fu-
                                                                            sionne. Stable.
             Rapide (Quick)        O(n log n)   O(n log n)       O(n2 )     Diviser pour régner : choisit un
                                                                            pivot, place les petits à gauche,
                                                                            les grands à droite (partition).
             Bulles                  O(n)         O(n2 )         O(n2 )     Echange les voisins adjacents
                                                                            mal triés. Fait remonter le max
                                                                            à la fin.
             Sélection               O(n2 )       O(n2 )         O(n2 )     Cherche le minimum de la partie
                                                                            non triée et l’échange avec le dé-
                                                                            but.

Cas particuliers à connaître :
 — Tableau déjà trié : Insertion est le meilleur (O(n)), Rapide (avec pivot fixe) et Sélection sont mauvais (O(n2 )).
 — Tris non-comparatifs : Tri par Comptage (O(n + k)) et Tri Drapeau Hollandais (0,1,2 en un passage).


3     Récursivité & Diviser pour Régner
3.1     1. Structure type (Ex : Tri Fusion)
    — Diviser : Découper le problème en sous-problèmes (ex : couper tableau en 2).
    — Régner : Appeler la fonction récursivement sur les sous-parties.
    — Combiner : Fusionner les résultats (ex : procédure Fusion).


                                                             1
~~~

## Page 2

~~~text
3.2     2. Calcul de complexité (Master Theorem simplifié)
Pour une récurrence du type T (n) = aT (n/b) + f (n) (ex : T (n) = 2T (n/2) + n pour Fusion) :
    — On regarde la hauteur de l’arbre d’appels (logb n).
    — On regarde le travail à chaque étage.
    — Résultat classique Fusion/Rapide : O(n log n).


4      Structures de Données
4.1     1. Structures Linéaires
    — Pile (Stack) : LIFO (Last In First Out). Opérations : empiler, dépiler. (Ex : Pile d’appels récursifs).
    — File (Queue) : FIFO (First In First Out). Opérations : enfiler, défiler. (Ex : File d’attente).
    — Liste Chaînée : Éléments liés par des pointeurs. Insertion/Suppression facile, accès lent (O(n)).

4.2     2. Tables de Hachage (Maps)
Structure pour stocker des couples (Clé, Valeur) avec accès très rapide (visé O(1)).
    — Fonction de hachage h(k) : Transforme la clé (ex : string) en entier (index du tableau).
    — Collision : Quand h(k1) == h(k2).
    — Résolution des collisions (Chaînage) : Chaque case du tableau contient une Liste Chaînée des éléments
      ayant le même hash.
    — Complexité :
        — Moyenne : O(1) (si bonne fonction de hachage).
        — Pire (toutes clés collisionnent) : O(n) (recherche dans une liste).


5      Mémo Technique pour l’Examen
    1. Partition (QuickSort) : On parcourt, si val ≤ pivot, on échange et on avance l’index de séparation. Le pivot
       finit entre les petits et les grands.
    2. Dichotomie : Complexité O(log n). Divise l’espace de recherche par 2 à chaque étape.
    3. Invariant : Toujours écrire : "Au début de la boucle, le sous-tableau T [0..i] est trié/contient les min/etc."




                                                            2
~~~
