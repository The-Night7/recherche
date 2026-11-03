# Chap2_slides.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1pOw5r-7WE7uUBlpCBIl0akUF9J5rQ1cC) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                           Problèmes décidables *



                                    ING2 MI
                                   2022-2023



*Ce chapitre est adapté d’un cours déposé par Houcine Senoussi
~~~

## Page 2

~~~text
Plan


 1. Définitions
 2. Propriétés
 3. Machine de Turing universelle
 4. Le problème de l’arrêt




                  ING2 GI   Problèmes décidables
~~~

## Page 3

~~~text
                                Définitions
                                Propriétés
              Machine de Turing universelle
                    Le problème de l’arrêt

Définition
s

  Définition 1 :
  Une machine de Turing M décide un langage si
      ∀x ∈ L M(x ) = qs
      ∀x ∉ L M(x ) = qe

  Définition 2 :
  Un langage est dit décidable ou récursif s’il existe une
  machine de Turing qui le décide.




                                 ING2 MI      Problèmes décidables
~~~

## Page 4

~~~text
                                Définitions
                                Propriétés
              Machine de Turing universelle
                    Le problème de l’arrêt

Définition
s

  Définition 3:
  Une machine de Turing M accepte un langage si
      ∀x ∈ L M(x ) = qs
      ∀x ∉ L M(x ) = ↗

  Définition 4 :
  Un langage est dit récursivement énumérable s’il existe une
  machine de Turing qui l’accepte.



                                 ING2 MI      Problèmes décidables
~~~

## Page 5

~~~text
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                      Le problème de l’arrêt

Propriétés


   Propriété 1 :
   Si un langage est récursif alors il est récursivement énumérable.

Demonstration
Soit L un langage récursif. Soit M une machine qui le décide.




                                   ING2 MI      Problèmes décidables
~~~

## Page 6

~~~text
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                     Le problème de l’arrêt

Propriétés

Démonstration
Soit L un langage récursif. Soit M une machine qui le décide.
       ∀x ∈ L M(x ) = qs
       ∀x ∉ L M(x ) = qe
Soit M' une machine dont le fonctionnement est le suivant :
Lorsqu'elle reçoit un mot x en entrée, elle imite le fonctionnement de
M jusqu’à l'avant dernière étape.
A la dernière étape, si M passe à l’état qs, M' fait de même, mais si
M passe à l’état qe, M' se met à se déplacer indéfiniment vers la
droite. Nous avons donc
       ∀x ∈ L M’(x ) = qs
       ∀x ∉ L M’(x ) = ↗
M' accepte donc L qui est donc récursivement énumerable.
                                  ING2 MI      Problèmes décidables
~~~

## Page 7

~~~text
                                    Définitions
                                    Propriétés
                  Machine de Turing universelle
                        Le problème de l’arrêt

Propriétés


  Propriété 1 :
  Propriété 2 :
  Si un langage L est récursif alors son complémentaire L est aussi
  récursif.




                                     ING2 MI      Problèmes décidables
~~~

## Page 8

~~~text
                                     Définitions
                                     Propriétés
                   Machine de Turing universelle
                         Le problème de l’arrêt

Propriétés


   Propriété 1 :
   Propriété 2 :
   Si un langage L est récursif alors son complémentaire L est aussi
   récursif.

Démonstration
Un langage est récursif, cela signifie qu'il existe une machine de
Turing M qui le décide,
On obtient une machine qui décide tout simplement en
inversant les rôles de qs et de qe.



                                      ING2 MI      Problèmes décidables
~~~

## Page 9

~~~text
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                     Le problème de l’arrêt

Propriétés


  Propriété 3 :
  Un langage L est récursif si et seulement si L et son
  complémentaire L sont récursivement énumérables.




                                  ING2 MI      Problèmes décidables
~~~

## Page 10

~~~text
                                  Définitions
                                  Propriétés
                Machine de Turing universelle
                      Le problème de l’arrêt

Propriétés


   Propriété 3 :
   Un langage L est récursif si et seulement si L et son
   complémentaire L sont récursivement énumérables.

Démonstration
⇒
Si L est récursif alors est récursif (propriété 2). L et étant
récursifs, ils sont récursivement énumerables (propriété 1).




                                   ING2 MI      Problèmes décidables
~~~

## Page 11

~~~text
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                     Le problème de l’arrêt

Propriétés

Démonstration (suite)
⇐
Supposons maintenant que L et soient récursivement énumerables.
Cela signifie qu'il existe deux machines de Turing M et tque
       ∀x ∈ L M(x ) = qs             ∀x ∉ L (x ) = qs
       ∀x ∉ L M(x ) = ↗              ∀x ∈ L      (x ) = ↗
Considérons la machine M' qui fonctionne comme suit : Quand elle
reçoit en entrée un mot x, elle imite alternativement le comportement
de M et celui de . Donc M' termine lorsque M ou termine.
Plus précisement :
{ Si x ∈ L , M' termine comme M dans l'etat qs.
{ Si x ∉ L , M' termine lorsque s’arrête, cet état final de M' sera
appelé qe.
                                  ING2 MI      Problèmes décidables
~~~

## Page 12

~~~text
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                     Le problème de l’arrêt

Définition



  Définition :
  la machine de Turing universelle est une machine de Turing à
  deux bandes qui :
       interprète ce qu’elle reçoit en entrée comme la concaténation
       d’une description M d’une machine de Turing et d’un mot x
       fourni à l’entrée de M,
      imite (simule) le comportment de M lorsque M reçoit en
      entrée x .




                                  ING2 MI      Problèmes décidables
~~~

## Page 13

~~~text
                                Définitions
                                Propriétés
              Machine de Turing universelle
                    Le problème de l’arrêt

Fonctionnement


 Notons B1 et B2 les bandes de U.
 Sur B1 sera inscrite la description de la machine de Turing M (càd
 le quadruplet (K , Σ, δ, q0)) et le mot x . Nous noterons M le mot
 contenant la description de la machine M .
 La bande B2 contiendra la configuration de M à tout instant
 : son état q et la position de la tête de lecture.
 La position de la tête de lecture sera représentée par un
 couple (u, v ) tel que :
     x est la concaténation de u et v.
     La tête de lecture de M est positionnée sur le premier symbôle de
     v.


                                 ING2 MI      Problèmes décidables
~~~

## Page 14

~~~text
                               Définitions
                               Propriétés
             Machine de Turing universelle
                   Le problème de l’arrêt

Fonctionnement-2



     Pour simuler M, U procède comme suit :
         Elle récupère l’état en cours q (lecture de B2).
         Elle récupère le symbôle lu s (lecture de B2).
         Elle récupère la transition associée au couple (q, s) (lecture de
         B1).
               Soit (q′, s′, d ) le triplet définissant cette transition.
         Elle écrit le symbôle s′ (écriture sur B2).
         Elle effectue le déplacement d (écriture sur B2).
         Elle simule le passage à l’état q′ (écriture sur B2).




                                ING2 MI      Problèmes décidables
~~~

## Page 15

~~~text
                                Définitions
                                Propriétés
              Machine de Turing universelle
                    Le problème de l’arrêt

Formulation



  Formulation du problème H (Halting) :
      Etant donné une machine de Turing M,
      étant donné un mot x ,
      est-ce que M s’arrête lorsqu’elle reçoit x en entrée ?
      Autrement dit,
      avons nous M (x ) ≠↗ ?




                                 ING2 MI      Problèmes décidables
~~~

## Page 16

~~~text
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                     Le problème de l’arrêt

Formulation-2




  Langage associé :
  Pour étudier le problème d’arrêt nous lui associons le langage LH
  défini comme suit :
       LH {X = (M, x ) M (x ) ≠↗ }.




                                  ING2 MI      Problèmes décidables
~~~

## Page 17

~~~text
                               Définitions
                               Propriétés
             Machine de Turing universelle
                   Le problème de l’arrêt

Propriétés



  Propriété 1 :
  LH est récursivement énumérable.




                                ING2 MI      Problèmes décidables
~~~

## Page 18

~~~text
                                 Définitions
                                 Propriétés
               Machine de Turing universelle
                     Le problème de l’arrêt

Propriétés



  Propriété 1 :
  LH est récursivement énumérable.

  Propriété 2 :
  LH n’est pas récursif.




                                  ING2 MI      Problèmes décidables
~~~

## Page 19

~~~text
                               Définitions
                               Propriétés
             Machine de Turing universelle
                   Le problème de l’arrêt

Propriétés

Démonstration
Il nous faut démontrer qu’il n’existe pas de machine de
Turing qui décide LH. Pour ce faire supposons qu’il en existe
une et nous allons aboutir à une contradiction.

Soit donc une machine de Turing MH qui décide LH.
Nous avons donc
– X = (M, x) LH MH(X) = qs
– X = (M, x) ∉ LH MH(X) = qe


                                ING2 MI      Problèmes décidables
~~~

## Page 20

~~~text
                                Définitions
                                Propriétés
              Machine de Turing universelle
                    Le problème de l’arrêt

Propriétés

Démonstration (suite)
Soit D la machine de Turing dont le fonctionnement est le suivant :
– D reçoit en entrée un mot M représentant la description d’une
machine de Turing.
– D imite MH lorsque MH reçoit en entrée le couple (M, M) jusqu’à
l’avant dernière étape, ensuite :
     – Si MH termine en qs D se déplace indéfiniment vers la droite.
     – Si MH termine en qe D termine en qs.
     Autrement dit,
     – Si MH (M, M) = qs alors D(M) =↗.
     – Si MH(M, M) = qe alors D(M) = qs.


                                 ING2 MI      Problèmes décidables
~~~

## Page 21

~~~text
                                Définitions
                                Propriétés
              Machine de Turing universelle
                    Le problème de l’arrêt

Propriétés

Démonstration (suite)
Nous nous posons la question : comment se comporte D lorsqu’elle
reçoit en entrée sa propre description. Deux possibilités :
 – Soit D(D) = ↗ ce qui signifie que MH(D, D) = qs donc puisque MH
décide LH, (D, D) LH ce qui signifie compte tenu de la définition de
LH que D(D) = qs. Contradiction.
 – Soit D(D) = qs ce qui signifie que MH(D, D) = qe donc puisque MH
décide LH, (D, D) ∉ LH ce qui signifie compte tenu de la définition de
LH que D(D) = ↗. Contradiction.
Supposer qu’il existe une machine de Turing qui décide LH conduit
donc à une contradiction. Il n’existe donc aucune machine de Turing
qui décide LH et LH est donc indécidable.

                                 ING2 MI      Problèmes décidables
~~~
