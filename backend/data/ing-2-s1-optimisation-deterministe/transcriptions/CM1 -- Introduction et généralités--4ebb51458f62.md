# CM1 -- Introduction et généralités.pdf

[Ouvrir l’original](https://drive.google.com/open?id=103acWHvODID7ugYSw_CTNnnpDsCMU-sB) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 3, 14, 39.

## Page 1

~~~text
Ingénieurs 2ème année : Mathématiques et Informatique

  Méthodes itératives d’optimisation déterministe




         CM1 – Introduction et généralités
             Nisrine FORTIN CAMDAVANT
~~~

## Page 2

~~~text
1   Introduction et généralités
       Classification générale des méthodes d’optimisation
       Principe des méthodes déterministes
       Optima locaux et globaux


2   Outils et notions fondamentales
      Développement de Taylor-Young
      Dérivée directionnelle


3   Forme quadratique


4   Convexité
~~~

## Page 3

![Fac-similé de la page 3](../facsimiles/46b18d954bad2e790cffb35c.jpg)

~~~text
Motivations et généralités
~~~



## Page 4

~~~text
  Introduction et généralités      Outils et notions fondamentales   Forme quadratique       Convexité




                                         Introduction
                 Objectif : l’optimisation non linéaire, comme son nom l’indique, s’attache
                 à résoudre des problèmes d’optimisation dont le critère et les contraintes
                 sont non linéaires.
                 L’optimisation sans contraintes consiste à rechercher les optimums d’une
                 fonction d’une ou plusieurs variables.


                 Domaines d’application de l’optimisation : minimiser le coût, minimiser
                 la distance, maximiser le bénéfice, maximiser le profit, . . ., en gestion de
                 ressources, rentabilisation des investissements, transport, . . ..
                 L’optimisation est essentiellement un outil d’aide à la décision.




4/46
~~~

## Page 5

~~~text
  Introduction et généralités     Outils et notions fondamentales   Forme quadratique   Convexité




                                            Terminologie

                 En général,
                 Un problème d’optimisation est défini par

                                                     min f (x)
                                                      x∈K



                    ↝ K est un sous-ensemble non vide de Rn qu’on appelle ensemble
                      ou domaine des contraintes
                    ↝ Tout élément de K est appelé un point admissible ou point
                      réalisable.
                    ↝ La fonction f ∶ Rn → R est appelée fonction coût, fonction
                      objectif ou encore critère.



5/46
~~~

## Page 6

~~~text
  Introduction et généralités     Outils et notions fondamentales            Forme quadratique          Convexité




             Classification générale des méthodes d’optimisation
          Les problèmes d’optimisation peuvent être classés en plusieurs grandes familles,
          deux grandes classes sont à différencier de façon générale :

             1   l’optimisation numérique où X ⊂ Rn ,
             2   l’optimisation discrète où X est fini ou dénombrable.
                                                       X
                                                       X
                                                       X
       Optimisation numérique                          X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                                    Optimisation discrète
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
       On peut distinguer deux cas :                   X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
         1   Cas linéaire                              X
                                                       X
                                                       X            On peut distinguer deux cas :
                                                       X
                                                       X
                                                       X
         2   cas non linéaire                          X
                                                       X
                                                       X
                                                                      1   Cas des méthodes exactes
                                                       X
                                                       X
                                                       X
       avec méthodes globales et méthodes              X
                                                       X
                                                       X
                                                                      2   Cas des méthodes approchées
       locales.                                        X
                                                       X
                                                       X
                                                       X


6/46
~~~

## Page 7

~~~text
  Introduction et généralités          Outils et notions fondamentales              Forme quadratique                    Convexité



  Optimisation numérique


                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
   Cas linéaire                                        X
                                                       X
                                                       X        Cas non linéaire
                                                       X
                                                       X
                                                       X
        ∎ Résoudre des problèmes                       X
                                                       X          ∎ Résoudre des problèmes d’optimisation dont le
           d’optimisation dont le critère et les       X
                                                       X
                                                       X                 critère et les contraintes ne sont pas
           contraintes sont linéaires.                 X
                                                       X
                                                       X                 forcément linéaires.
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
        ∎ En désignant par ⟨.∣.⟩ le produit            X
                                                       X
                                                       X           ∎ S’intéresser au problème d’optimisation
          scalaire euclidien, la forme standard        X
                                                       X
                                                       X             suivant :
          est exprimée comme suit :                    X
                                                       X
                                                       X
                                                       X       ⎧ min (f (x1 , ⋯, xn ) )
                                                       X
                                                       X
                                                       X
                                                               ⎪
                                                               ⎪
                                                               ⎪
                                                               ⎪ x∈D
       ⎧ minimiser⟨c∣x⟩                                X       ⎪
                                                               ⎪
       ⎪
       ⎪
       ⎪                                               X
                                                       X
                                                       X
                                                               ⎪
                                                               ⎪
                                                               ⎪
                                                               ⎪
       ⎨
       ⎪
                                                       X
                                                       X
                                                       X
                                                               ⎪
                                                               ⎪
                                                               ⎪
                                                               ⎪
                                                                                            ⎧
                                                                                            ⎪
                                                                                            ⎪    g1 (x1 , . . . , xn )           ⎫
                                                                                                                            = b1 ⎪
                                                                                                                                 ⎪
                                                                                            ⎪                                    ⎪
       ⎩ sous les contraintes   Ax = b, x ≥ 0
       ⎪                                               X       ⎪
       ⎪                                               X
                                                       X       ⎨ avec les contraintes : ⎪   ⎪
                                                                                            ⎨
                                                                                                 g2 (x1 , . . . , xn )      = b2 ⎪
                                                                                                                                 ⎪
                                                                                                                                 ⎬
                                                       X
                                                       X
                                                       X
                                                               ⎪
                                                               ⎪
                                                               ⎪
                                                               ⎪                            ⎪
                                                                                            ⎪    ⋮                               ⎪
                                                                                                                                 ⎪
                                                       X       ⎪                            ⎪
                                                                                            ⎪                                    ⎪
                                                                                                                                 ⎪
                                                       X
                                                       X       ⎪
                                                               ⎪
                                                               ⎪                            ⎪
                                                                                            ⎩    gm (x1 , . . . , xn )      = bm ⎪
                                                                                                                                 ⎭
                                                       X       ⎪
                                                               ⎪
  La programmation linéaire avec la méthode            X
                                                       X
                                                       X
                                                               ⎪
                                                               ⎪
                                                               ⎪
                                                               ⎪
  du simplexe et la méthode des tableaux de            X
                                                       X
                                                       X
                                                               ⎪
                                                               ⎩ bi ∈ R, ∀i ∈ {1, . . . , m}
  Dantzig ont déjà été vues en 1ère année du
                                                       X
                                                       X
                                                       X
  cycle ingénieur.
                                                       X
                                                       X
                                                       X       où D ⊂ Rn et m < n.
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X
                                                       X

7/46
~~~

## Page 8

~~~text
  Introduction et généralités     Outils et notions fondamentales           Forme quadratique         Convexité



  Optimisation numérique


                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X         Cas non linéaire avec méthodes locales
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
 Cas non linéaire avec méthodes globales            X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X           ∎ L’exploitation du gradient d’une fonction
                                                    X
                                                    X
                                                    X               (Méthodes avec gradient) s’efforce à diminuer
                                                    X
                                                    X
                                                    X               la valeur de la fonction objectif dans une
  ∎ Sous des conditions de régularité de la         X
                                                    X
                                                    X               direction choisie mais nous amène souvent à
     fonction objectif et des fontions contraintes, X
                                                    X
                                                    X               des minima locaux.
     on peut distinguer des méthodes de résolution XX
                                                    X
     globales (recherche d’un optimum global).      X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X           ∎ Ces méthodes sont très efficaces mais ont
                                                    X
                                                    X
                                                    X             l’inconvénient de ne pas fournir un minimum
  ∎ En l’absence des conditions de régularité, on X X
                                                    X             global.
     peut distinguer des méthodes globales dans un XX
                                                    X
     cadre métaheuristique.
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X           ∎ D’autres méthodes qui n’utilisent pas le
                                                    X
                                                    X
                                                    X             gradient (Méthodes sans gradient) amènent à
                                                    X
                                                    X
                                                    X             des minima locaux
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X
                                                    X

8/46
~~~

## Page 9

~~~text
  Introduction et généralités       Outils et notions fondamentales        Forme quadratique          Convexité



  Optimisation discrète


                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
         Cas des méthodes exactes                               X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
   ∎ lorsque l’ensemble des solutions d’un problème             X
                                                                X
                                                                X
     d’optimisation est fini, il est possible d’énumérer toutes X
                                                                       Cas des méthodes approchées
                                                                X
                                                                X
                                                                X
     ces solutions et de prendre celle qui nous arrange.        X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
   ∎ L’inconvénient principal est le nombre prohibitif du       X
                                                                X
                                                                X
     nombre de solutions car il n’est pas évident d’effectuer X X     Ces méthodes sont basées sur des
                                                                X
                                                                X
                                                                X     métaheuristiques, elles seront explorées
     cette énumération.                                         X
                                                                X
                                                                X
                                                                X     pendant le cours d’IA et Application du 2nd
                                                                X
                                                                X
                                                                X     semestre.
   ∎ L’une des méthodes utilisées est la procédure par          X
                                                                X
                                                                X
     évaluation et séparation progressive (branch and           X
                                                                X
                                                                X
     bound) qui repose sur une méthode arborescente de
                                                                X
                                                                X
                                                                X
     recherche d’une solution optimale par séparations et
                                                                X
                                                                X
                                                                X
     évaluations.
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X
                                                                X

9/46
~~~

## Page 10

~~~text
  Introduction et généralités     Outils et notions fondamentales      Forme quadratique   Convexité



  Optimisation sans contraintes




         Étudier le problème d’optimisation sans contraintes où on effectue une
         minimisation ou une maximisation de la fonction f ∶ Rn → R ∪ {+∞} sur tout
         l’espace.

         Formulation du problème
                                            (PSC)         minn f (x)
                                                          x∈R




                De ce module.

                 On va présenter quelques algorithmes permettant de calculer (de manière ap-
                 prochée) la ou les solution(s) du problème (PSC) sans contraintes.




10/46
~~~

## Page 11

~~~text
  Introduction et généralités        Outils et notions fondamentales   Forme quadratique   Convexité



  Optimisation sous contraintes

         Étudier le problème d’optimisation avec contraintes où on effectue une
         minimisation ou une maximisation de la fonction f ∶ Rn → R ∪ {+∞} sur
         l’ensemble des contraintes.
         Formulation du problème
                                ⎧
                                ⎪ min f (x)
                                ⎪
                                ⎪
                                ⎪  Rn
                                ⎪
                                ⎪                   ⎧  g (x) ≤ 0 (1) ⎫
                           (PC) ⎨                   ⎪
                                                    ⎪
                                                    ⎪                     ⎪
                                                                          ⎪
                                                                          ⎪
                                ⎪
                                ⎪
                                ⎪                   ⎨
                                  Sous les contraintes                    ⎬
                                ⎪
                                ⎪
                                ⎪                   ⎪
                                                    ⎪                     ⎪
                                                                          ⎪
                                ⎩                   ⎪
                                                    ⎩ h(x) = 0 (2) ⎪      ⎭
         où les fonctions f , g et h sont des fonctions généralement non linéaires.

            ↝ L’inéquation (1) désigne des contraintes d’inégalité.
            ↝ L’équation (2) des contraintes d’égalité.


                De ce module.

                 Les problèmes d’optimisation avec contrainte (PC) seront abordés avec des
                 techniques amenant à résoudre un problème d’optimisation sans contrainte.

11/46
~~~

## Page 12

~~~text
  Introduction et généralités      Outils et notions fondamentales   Forme quadratique     Convexité



  Principe des méthodes déterministes




            ∎ Les méthodes déterministes conduisent, pour une solution initiale donnée,
                 toujours au même résultat final.
             ∎ Elles s’appuient sur une direction de recherche qui peut être fournie par
               les dérivées de la fonction objectif.
             ∎ La plupart de ces algorithmes exploitent les conditions d’optimalité.
             ∎ La question de la détermination de minima globaux est difficile.
             ∎ Ces méthodes ont la réputation d’être efficaces lorsque la solution initiale
               est proche de l’optimum recherché.
             ∎ Inconvénients :
                    le cas d’une fonction objectif possédant plusieurs optimums,
                    peuvent converger vers un optimum local,
                    faire l’hypothèse de différentiabilité de la fonction objectif . . .




12/46
~~~

## Page 13

~~~text
                   Articulation du cours
Le cours d’optimisation déterministe sera présenté dans une durée de 22,5
heures et sera articulé autour de cinq thématiques :

  1   Une introduction à l’optimisation et une présentation des outils nécessaires
      pour traiter les problématiques d’optimisation dans le cadre déterministe.


  2   Une présentation des conditions d’optimalité.


  3   Une présentation de l’algorithme des méthodes de descente.


  4   La présentation des différentes méthodes de descente et variantes selon les
      directions de descente dans le cas de problème sans contraintes.


  5   La présentation de quelques de descente dans le cas de problème sous
      contraintes.
~~~

## Page 14

![Fac-similé de la page 14](../facsimiles/e7296e05fcb093427c568d6d.jpg)

~~~text
Optima locaux et globaux
~~~



## Page 15

~~~text
  Introduction et généralités   Outils et notions fondamentales        Forme quadratique   Convexité




         Soient X ⊂ Rn l’ensemble des contraintes et f un critère à optimiser sur X . On
         cherche à résoudre le problème (P) en cherchant des solutions locales au sens
         des définitions qui suivent.

             ∎ Minimum  local : x ∗ ∈ X réalise un minimum local de f sur X si et
               :::::::::::::
               seulement si il existe une boule ouverte B centrée en x ∗ telle que

                                        ∀x ∈ B ∩ X , f (x) ≥ f (x ∗ )


             ∎ Minimum  global : x ∗ ∈ X réalise un minimum global de f sur X si et
               ::::::::::::::
               seulement si
                                           ∀x ∈ X , f (x) ≥ f (x ∗ )




15/46
~~~

## Page 16

~~~text
  Introduction et généralités       Outils et notions fondamentales   Forme quadratique   Convexité



  Optima locaux et globaux




                         Figure 1 – Plusieurs minima locaux et un minimum global


16/46
~~~

## Page 17

~~~text
  Introduction et généralités        Outils et notions fondamentales         Forme quadratique   Convexité




                De façon standard.
                Les notions de maximum local et global peuvent être définies de façon
                équivalente dans le sens où

                           max f (x) = − min ( − f (x)) ou min f (x) = − max ( − f (x)).
                           x∈X           x∈X                           x∈X       x∈X

                 De façon standard, nous porterons la suite de ce cours sur des problèmes
                 de minimisation.




17/46
~~~

## Page 18

~~~text
  Introduction et généralités      Outils et notions fondamentales   Forme quadratique   Convexité


                 Fonction unimodale : On appelle fonction unimodale une fonction
                 présentant un seul maximum ou un seul minimum local. Si elle présente
                 plusieurs maxima ou minima locaux, elle est dite multimodale.

                 Exemple : La fonction de Schwefel d’équation
                                                      √              √
                                  f (x, y ) = −x sin ( ∣x∣) − y sin ( ∣y ∣)
                 illustre bien le caractère multimodal.




18/46
~~~

## Page 19

~~~text
        Outils et notions fondamentales

  ↝ Présenter quelques rappels utiles.


  ↝ Unifier les notations et le vocabulaire.


Soit f ∶ (x1 , x2 , . . . , xn ) ↦ f (x1 , . . . , xn ) une fonction réelle. Dans la suite, on
note
                x = (x1 , . . . , xn ), y = (y1 , . . . , yn ) et a = (a1 , . . . , an ).
~~~

## Page 20

~~~text
  Introduction et généralités       Outils et notions fondamentales            Forme quadratique   Convexité




                 On notera dans tout ce cours :

                    ↝ Un vecteur x de Rn sera noté x = (x1 , . . . , xn ), sa représentation
                                             ⎛ x1 ⎞
                         matricielle est x = ⎜ ⋮ ⎟.
                                             ⎝ xn ⎠
                    ↝ La transposée du vecteur x ∈ Rn est une matrice ligne :

                                                    x T = (x1 . . . xn ) .
                                                                               n
                     ▸ Produit scalaire canonique : ⟨x, y ⟩ = x T y = ∑ xi yi .
                       ::::::::::::::::::::::
                                                                               i=1
                                                                               ¿
                                                                      √        Án 2
                     ▸ Norme euclidienne canonique : ∥x∥ =
                       ::::::::::::::::::::::::
                                                                          x x =Á
                                                                           T   À∑ xi .
                                                                                      i=1

                     ▸ Boule ouverte centrée en x et de rayon r :
                       ::::::::::::::::::::::::::::::::

                                            Br (x) = {z ∈ Rn , ∥x − z∥ < r }.

                     ▸ Ouvert de Rn : X ⊂ Rn est ensemble ouvert si
                       ::::::::::::

                                         ∀x ∈ X , ∃ε > 0 tel que Bε (x) ⊂ X .
20/46
~~~

## Page 21

~~~text
  Introduction et généralités       Outils et notions fondamentales         Forme quadratique       Convexité



  Gradient et hessien d’une fonction


            ∎ Supposons que f admet des dérivées partielles d’ordre 1 en a ∈ Rn . On
                 appelle gradient de f en a, le vecteur défini par
                                                   ∂f       ∂f               ∂f
                                   ∇T f (a) = (        (a),     (a), . . . ,     (a))
                                                   ∂x1      ∂x2              ∂xn
             ∎ Si f admet des dérivées partielles d’ordre 2 en a. On appelle hessien de f
               en a la matrice n × n donnée par
                                        2
                                    ⎛ ∂ f                 ∂2f                        ∂2f        ⎞
                                    ⎜ ∂x12 (a)           ∂x1 ∂x2
                                                                 (a)    ......
                                                                                    ∂x1 ∂xn
                                                                                            (a) ⎟
                                    ⎜                                                           ⎟
                                    ⎜                                                           ⎟
                                    ⎜                                                           ⎟
                                    ⎜ ∂2f                                                       ⎟
                                    ⎜                     ∂2f                          2
                                                                                     ∂ f        ⎟
                         ∇2 f (a) = ⎜                                                       (a) ⎟
                                    ⎜ ∂x2 ∂x1 (a)         ∂x22
                                                               (a)      ......                  ⎟
                                    ⎜                                               ∂x2 ∂xn     ⎟
                                    ⎜ ⋮                  ⋮              ⋮          ⋮            ⎟
                                    ⎜                                                           ⎟
                                    ⎜                                                           ⎟
                                    ⎜ ∂2f                  ∂2f                      ∂2f         ⎟
                                    ⎝ ∂xn ∂x1 (a)         ∂xn ∂x2
                                                                  (a)   ......
                                                                                    ∂xn2
                                                                                         (a)    ⎠

                 Le hessien (ou la matrice hessienne) de f en a est couramment noté
                 Hf (a).

21/46
~~~

## Page 22

~~~text
  Introduction et généralités        Outils et notions fondamentales   Forme quadratique   Convexité




         Définition
         Une matrice carrée A symétrique d’ordre n est dite semi-définie positive et on
         note A ≥ 0 si
                                     hT Ah ≥ 0, ∀h ∈ Rn .
         On dit que A est une matrice définie positive et on note A > 0 si

                                         hT Ah > 0, ∀h ∈ Rn /{0Rn }.



                   Propriété 1.
           Soit A une matrice symétrique d’ordre n et symétrique. On a les équivalences
           suivantes :
               1    A ≥ 0 si et seulement si Sp(A) ⊂ R+ .
               2    A > 0 si et seulement si Sp(A) ⊂ R∗+ .


           Sp(A) désigne le spectre de la matrice A, ensemble des valeurs propres de A.

         Démonstration.
22/46
~~~

## Page 23

~~~text
  Introduction et généralités     Outils et notions fondamentales             Forme quadratique   Convexité



  Dérivée de composition


         Soient x et d deux vecteurs dans Rn , soit

                                               g ∶ t ↦ f (x + td)

         où t est un réel. On note que g (t) = f ○ u(t) où

                                              u( t ) =     x + td         .
                                                ®          ´¹¹ ¹ ¸¹¹ ¹¶
                                                réel     vecteur de Rn

         g est donc une composition de deux fonctions f et u. Si g est dérivable et f est
         différentiable alors       ′       ′
                                  g (t) = ⟨u (t), ∇f (u(t))⟩.


             ∎ u (t) = d (on dérive par rapport à la variable réelle t)
                   ′



             ∎ ∇f (u(t)) = ∇f (x + td)

                                        g (t) = ⟨d, ∇f (x + td)⟩.
                                          ′




23/46
~~~

## Page 24

~~~text
  Introduction et généralités         Outils et notions fondamentales       Forme quadratique     Convexité




                                                   Exemple
         Sur R3 , on considère la fonction f définie pour (x1 , x2 , x3 ) ∈ R3 par
                                                                         1
                                  f (x1 , x2 , x3 ) = x12 + x1 x2 + x22 + x32 .
                                                                         2
         La fonction f est de classe C 2 sur R3 . On note x = (x1 , x2 , x3 ).


                 Calcul du gradient de f en x.
                 :::::::::::::::::::::::

                          ⎧
                          ⎪ ∂f
                          ⎪
                          ⎪
                          ⎪     (x)     =     2x1 + x2 ,
                          ⎪
                          ⎪                                                      ⎛ 2x1 + x2 ⎞
                            ∂x
                          ⎪
                          ⎪
                          ⎪
                              1
                          ⎪
                          ⎪
                          ⎪                                                      ⎜          ⎟
                          ⎪ ∂f                                                   ⎜          ⎟
                          ⎨     (x)     =     x1 + 2x2           Donc   ∇f (x) = ⎜ x1 + 2x2 ⎟ .
                          ⎪
                          ⎪ ∂x2                                                  ⎜          ⎟
                          ⎪
                          ⎪                                                      ⎜          ⎟
                          ⎪
                          ⎪
                          ⎪                                                      ⎝ x3       ⎠
                          ⎪
                          ⎪
                          ⎪ ∂f
                          ⎪
                          ⎪
                          ⎪     (x)     =     x3
                          ⎩ ∂x3


24/46
~~~

## Page 25

~~~text
  Introduction et généralités     Outils et notions fondamentales          Forme quadratique         Convexité




                                             Exemple
                 Calcul du hessien de f en x.
                 ::::::::::::::::::::::::::

                  ⎧
                  ⎪ ∂2f                          ∂2f                          ∂2f
                  ⎪
                  ⎪      (x)        = 2,                (x)         = 1,             (x)       = 0
                  ⎪
                  ⎪
                  ⎪
                  ⎪ ∂x12                        ∂x1 ∂x2                      ∂x1 ∂x3
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪ ∂2f
                  ⎪                             ∂2f                           ∂2f
                  ⎨         (x)     = 1,             (x)            = 2,             (x)       = 0
                  ⎪
                  ⎪
                  ⎪ ∂x2 ∂x1                     ∂x22                         ∂x2 ∂x3
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪  ∂2f                         ∂2f                         ∂2f
                  ⎪
                  ⎪         (x)     = 0,                (x)         = 0,          (x)          = 1
                  ⎪
                  ⎩ ∂x3 ∂x1                     ∂x3 ∂x2                      ∂x32

                 Le Hessien de la fonction f en tout x ∈ R3 est donné par

                                                   ⎛ 2         1    0 ⎞
                                              Hf = ⎜ 1         2    0 ⎟.
                                                   ⎝ 0         0    1 ⎠


25/46
~~~

## Page 26

~~~text
  Introduction et généralités    Outils et notions fondamentales   Forme quadratique   Convexité




                                            Exemple
                 Nature de la matrice hessienne de f en x. La matrice hessienne
                 ::::::::::::::::::::::::::::::::::::::
                 est symétrique donc elle est diagonalisable et son ensemble des
                 valeurs propres est
                                            Sp (f ) = {1; 3} .
                 Les valeurs propres sont strictement positives donc la matrice Hf est
                 définie positive.




26/46
~~~

## Page 27

~~~text
  Introduction et généralités       Outils et notions fondamentales                                                                                                                            Forme quadratique   Convexité



                 Autre méthode : Soit h = (h1 , h2 , h3 ). On étudie le signe du réel hT Hf h.
                 :::::::::::::

                                                            ⎛ 2                                                                                                       1                       0 ⎞ ⎛ h1 ⎞
                                hT Hf h   =     (h1 h2 h3 ) ⎜ 1                                                                                                       2                       0 ⎟ ⎜ h2 ⎟
                                                            ⎝ 0                                                                                                       0                       1 ⎠ ⎝ h3 ⎠

                                          =     2h12 + 2h22 + h32 + 2h1 h2

                                                                1       3
                                          =     2 (h12 + h1 h2 + h22 ) + h22 + h32
                                                                4       2
                                                                                                                               2
                                                                                                   1                                                 3
                                          =     2 (h1 + h2 ) + h22 + h32
                                                                                                   2                                                 2
                                                ´¹¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¸ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¶
                                                                                                                        ≥0

                 La matrice hessienne est donc semi définie positive. De plus,
                                              ⎧
                                              ⎪    1
                                              ⎪
                                              ⎪ h + h                                                                                               =                        0
                                              ⎪ 1 2 2
                                h Hf h = 0 ⇐⇒ ⎨ h2
                                T
                                                                                                                                                    =                        0 ⇐⇒ h = 0R3
                                              ⎪
                                              ⎪
                                              ⎪
                                              ⎪
                                              ⎩ h3                                                                                                  =                        0
                 Hf est donc une matrice positive.

27/46
~~~

## Page 28

~~~text
    Développement de Taylor-Young

↝ On peut avoir besoin d’approcher localement une fonction par un
   polynôme de degré arbitraire.


↝ On va s’intéresser en particulier au développement de Taylor-Young
  jusqu’à l’ordre 2.


↝ Soient U un ouvert de Rn , x et y deux points de U et f ∶ U → R.
~~~

## Page 29

~~~text
  Introduction et généralités                  Outils et notions fondamentales                                  Forme quadratique                Convexité



  Développement de Taylor-Young




         À l’ordre 1 :
         Supposons que f est une fonction de classe C 1 sur U alors
                                                                                  T
                                      f (y ) = f (x) + (y − x) ∇f (x) + ∥y − x∥ϵ(y )                                                             (1)
                                                                        ´¹¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹¸¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¶
                                                                                                           lim ϵ(y )=0
                                                                                                        y −x→0




         À l’ordre 2 :
         Supposons que f est une fonction de classe C 2 sur U alors
                                     T        1       T
             f (y ) = f (x) + (y − x) ∇f (x) + (y − x) Hf (x)(y − x) + ∥y − x∥2 ϵ(y )                                                            (2)
                                              2                        ´¹¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¸¹¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¶
                                                                                                                                   lim ϵ(y )=0
                                                                                                                                  y −x→0




29/46
~~~

## Page 30

~~~text
  Introduction et généralités   Outils et notions fondamentales   Forme quadratique    Convexité



  Développement de Taylor-Young – Lemme


         Lemme 1.
         Soient f une fonction de classe C 1 sur un ouvert U de Rn , x ∈ U et d ∈ Rn alors

                                      f (x + θd) − f (x)
                                lim                      = ∇f (x)T d.
                                θ→0           θ

         Démonstration :
         ::::::::::
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
         X
30/46
~~~

## Page 31

~~~text
                 Dérivée directionnelle

Pour un vecteur donné d ∈ Rn , qu’on appelera direction, si on se place en
x ∈ Rn , on souhaite se déplacer de x vers un autre vecteur x .
                                                             ′
~~~

## Page 32

~~~text
  Introduction et généralités      Outils et notions fondamentales       Forme quadratique     Convexité




         Dérivée directionnelle
         On dit que f ∶ Rn → R admet une dérivée directionnelle au point a ∈ Rn dans la
         direction de d ∈ Rn si
                                            f (a + θd) − f (a)
                                      lim                      existe.
                                      θ→0           θ
         Notation : Cette limite est notée Dd f (a) et on peut écrire

                                            Dd f (a) = ∇f (a)T .d


                 Remarque.
                 On dira qu’on se déplacera dans la direction de d vers
                                                      ′
                                                    x = x + θd

                 avec θ > 0. θ sera appelé le pas de la descente et on imposera la condition
                 θ > 0.



32/46
~~~

## Page 33

~~~text
  Introduction et généralités       Outils et notions fondamentales   Forme quadratique   Convexité



  Dérivée directionnelle



         Fonction différentiable
         Soit f ∶ Rn → R une fonction continue. Si pour tout d ∈ Rn , la dérivée
         directionnelle Dd f existe en tout point de Rn alors la fonction est dite
         différentiable sur Rn .

         Lorsqu’elle existe, la dérivée directionnelle donne des informations sur la pente
         de la fonction dans la direction d :
                 si f ′ (x).d > 0 alors f est croissante dans la direction d.


                 si f ′ (x).d < 0 alors f est décroissante dans la direction d.

         Remarque : Lorsque la direction d ∈ Rn est telle que ∥d∥ = 1 alors la dérivée
         directionnelle (si elle existe) au point a ∈ Rn dans la direction de d est le taux
         d’accroissement de f dans la direction d au point a.




33/46
~~~

## Page 34

~~~text
                   Fonction quadratique
La forme quadratique joue sur Rn le même rôle que joue la fonction
x ↦ ax 2 + bx + c dans R.


Elle a son intérêt en optimisation car si une fonction n’est pas quadratique
mais de classe C 2 , on peut penser à l’approcher par une fonction
quadratique au voisinage d’un vecteur a.


On utilise la formule de Taylor Young à l’ordre 2 :
                         T        1       T
  f (x) = f (a) + (x − a) ∇f (a) + (x − a) Hf (a)(x − a) + ∥x − a∥2 ϵ(x)
                                  2                        ´¹¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¸¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¹ ¶
                                                                                                     lim ϵ(x)=0.
                                                                                                   x−a→0
~~~

## Page 35

~~~text
  Introduction et généralités      Outils et notions fondamentales       Forme quadratique   Convexité




         Dans plusieurs problèmes d’optimisation, on peut être ramené à résoudre un
         problème de minimisation des moindres carrés et donc à optimiser un critère
         sous une une forme particulière qu’on appelle forme quadratique.

         Forme quadratique.
         Soient A une matrice symétrique d’ordre n, b ∈ Rn un vecteur et c un réel. On
         définit la forme quadratique par

                                  f     ∶   Rn     →      R
                                                                     1
                                            x      ↦      c + b T x + x T Ax
                                                                     2




                 Lorsque cette fonction vérifie des propriétés particulières, nous pourrons en
                 déduire des propriétés importantes en optimisation. C’est pour cela qu’on
                 s’intéresse dans ce paragraphe au caractère positif, diagonalisable, . . . de
                 la matrice A.



35/46
~~~

## Page 36

~~~text
  Introduction et généralités           Outils et notions fondamentales           Forme quadratique            Convexité




                                Fonction quadratique – Remarque
         Si f est de classe C 2 au voisinage de a alors pour x ∈ V(a)
                                                      1        T                        2
           f (x)    =     f (a) + (x − a)T ∇f (a) +     (x − a) Hf (a) (x − a) + ∥x − a∥ ε (x)
                                                      2
                                                1 T            T        1 T           T                 2
                    =     f (a) − aT ∇f (a) +     a Hf (a)a + x ∇f (a) + x Hf (a)x − a Hf (a)x + ∥x − a∥ ε (x)
                                                2                       2
                                                                                           1 T                  2
                    =     (f (a) − aT ∇f (a) + 21 aT Hf (a)a) + x T (∇f (a) − Hf (a)a) +     x Hf (a)x + ∥x − a∥ ε(x)
                                                                                           2

                  ⎧
                  ⎪                          1
                  ⎪
                  ⎪ c = f (a) − aT ∇f (a) + aT Hf (a)a
                  ⎪
                  ⎪
                  ⎪                          2
                  ⎪
                  ⎪
                  ⎪
         On pose ⎨ b = ∇f (a) − H (a)a
                  ⎪
                  ⎪
                  ⎪
                                       f
                  ⎪
                  ⎪
                  ⎪
                  ⎪
                  ⎪ A = H (a)
                  ⎪
                  ⎩           f
         On pourra donc au voisinage de a approcher la fonction f par la fonction
                                    1
         quadratique x ↦ c + b T x + x T Ax.
                                    2



36/46
~~~

## Page 37

~~~text
Propriétés des formes quadratiques définies positives

Soit f la fonction quadratique de matrice A. Lorsque la matrice A est définie
positive (resp. semi définie positive), on dira que f est une fonction
quadratique définie positive (resp. semi-définie positive).
~~~

## Page 38

~~~text
  Introduction et généralités    Outils et notions fondamentales   Forme quadratique         Convexité




                 Propriété 2.
           Soit A une matrice symétrique définie positive, b ∈ Rn , c ∈ R et
                                                         1
                                      f ∶ x ↦ c + b T x + x T Ax
                                                         2
           une forme quadratique. Soit x̂ l’unique vecteur vérifiant Ax̂ + b = 0n alors x̂
           réalise le minimum global de f .

         Démonstration.
         ::::::::::::


                 Propriété 3.
           Soit A une matrice symétrique définie positive, b ∈ Rn , c ∈ R et
                                                         1
                                      f ∶ x ↦ c + b T x + x T Ax
                                                         2
           une forme quadratique. La fonction f est deux fois différentiable sur Rn et
           ∀x ∈ Rn ,
                                 ∇f (x) = Ax + b, Hf (x) = A.

         Démonstration.
         ::::::::::::
                        Voir TD1.
38/46
~~~

## Page 39

![Fac-similé de la page 39](../facsimiles/a137227f7b9240d627989adf.jpg)

~~~text
Convexité
~~~



## Page 40

~~~text
  Introduction et généralités     Outils et notions fondamentales      Forme quadratique         Convexité



         Ensemble convexe
         Une partie A ⊂ Rn est dite convexe si ∀x ∈ A, ∀y ∈ A, ∀α ∈ [0, 1],

                                            αx + (1 − α)y ∈ A.

         Cela revient à dire que le segment qui relie deux points de A reste dans A.


                 Cette définition se généralise de la façon suivante,
                                              n              n
           ∀xi ∈ A, ∀λi ∈ [0; 1] telle que ∑ λi = 1, ∑ αi xi ∈ A.
                                             i=1           i=1




                                                                    E est la zone bleue.
                                                                    Le segment AB sort de la zone E
                                                                    Donc E n'est pas convexe
                                              B
                                              x



                                                      Ax



                                    Figure 2 – Objet non convexe
40/46
~~~

## Page 41

~~~text
  Introduction et généralités      Outils et notions fondamentales   Forme quadratique   Convexité




             1   Rn et ∅ sont des convexes.
             2   Sur R, les intervalles sont des convexes.


               Proposition.
           L’intersection d’un nombre quelconque d’ensembles convexes est convexe.



         Remarque : La réunion de deux parties convexes n’est pas en général convexe.




41/46
~~~

## Page 42

~~~text
  Introduction et généralités      Outils et notions fondamentales   Forme quadratique     Convexité




         Convexité d’une fonction
         Une fonction f définie sur un convexe Ω de Rn dans R est convexe si et
         seulement si

              ∀x ∈ Ω, ∀y ∈ Ω, ∀α ∈ [0, 1], f (αx + (1 − α)y ) ≤ αf (x) + (1 − α)f (y ).


                 Lorsque l’inégalité est stricte, on dit que f est strictement convexe sur Ω.
                 On dit que f est concave lorsque −f est convexe.

             1   Toute fonction numérique affine est convexe.

             2   La fonction constante est convexe et concave à la fois.




42/46
~~~

## Page 43

~~~text
  Introduction et généralités        Outils et notions fondamentales         Forme quadratique   Convexité




         Enveloppe convexe
         On appelle enveloppe supérieure f (resp. enveloppe inférieure) d’une famille de
         fonctions {fi }i∈J et on note sup {fi } = f (resp. inf {fi } = f ) la fonction f ∶ I → R
                                            i∈J                        i∈J
         définie par : ∀x ∈ E , f (x) = sup {fi (x)} .
                                              i∈J




                 Proposition.
                  Toute combinaison linéaire de fonctions convexes (à coefficients positifs)
                  est une fonction convexe.
                   Toute limite simple de fonctions convexes est une fonction convexe.
                   Toute enveloppe supérieure finie de fonctions convexes est convexe.
                   Soit f ∶ Ω → R une fonction convexe avec f (Ω) ⊂ I et soit g ∶ I → R, une
                   fonction convexe croissante alors la fonction composée : g ○ f est
                   convexe.
                   Soit f ∶ I → R une fonction continue sur I. f est convexe si pour tout
                                      a+b       1
                   (a, b) ∈ I 2 on a f (    ) ≤ (f (a) + f (b))
                                        2       2

43/46
~~~

## Page 44

~~~text
  Introduction et généralités    Outils et notions fondamentales     Forme quadratique   Convexité



                                              Épigraphe
         L’epigraphe d’une fonction f est l’ensemble des points qui se trouvent au
         dessus du graphe G de la fonction f est appelé épigraphe de f .
                                Γ+ (f ) = {(x, y ) ∈ Ω × R, y ≥ f (x)}.




                                Figure 3 – Épigraphe de la fonction carrée

44/46
~~~

## Page 45

~~~text
  Introduction et généralités         Outils et notions fondamentales      Forme quadratique   Convexité



  Caractérisation différentielle de la convexité

                                 Lien entre propriétés
                   Propriété 4. Caractérisation de la convexité du 1er ordre
           Soit f ∶ Ω → R une fonction différentiable où Ω est une partie convexe de Rn .
           Les propriétés suivantes sont équivalentes :
               1    f est convexe.
               2    ∀ (x, y ) ∈ Ω × Ω, f (y ) ≥ f (x) + ⟨∇f (x), y − x⟩.
              ✓ On dit que les hyperplans tangants sont des minorants.
               3    ∀ (x, y ) ∈ Ω × Ω, ⟨∇f (y ) − ∇f (x), y − x⟩ ≥ 0.
              ✓ On dit que l’opérateur gradient est croissant.

         Démonstration. Voir TD1.
         ::::::::::::


                   Propriété 4. Caractérisation de la convexité du 2nd ordre

           Soit f ∶ Ω → R une fonction de classe C 2 où Ω est une partie convexe de Rn . f
           est convexe si et seulement si

               ∀x ∈ Rn , la matrice hessienne Hf (x) de f en x est semi-définie positive.
45/46
~~~

## Page 46

~~~text
  Introduction et généralités      Outils et notions fondamentales   Forme quadratique    Convexité



         Bibliographie :
                 Méthodes numériques et optimisation, Jean Pierre Corriou, LAVOISIER
                 2010
                 Linear and Nonlinear Programming, David G.LUENBERGER, Second
                 Edition Springer 2005
                 Introduction à l’optimisation, Jean Christophe Culioli, ellipses,1994.
                 Introduction à l’analyse numérique matricielle et à l’optimisation PG.
                 CIARLET MASSON 1990
                 Inverse Problem Theory and Methods for Model Parameter Estimation
                 Albert Tarantola SIAM 2005.
                 Convexité et optimisation Guy Cohen Ecole Nationale des Ponts et
                 Chaussées et INRIA 2000.
                 Optimisation sans contraintes M. Bergounioux http ://www.univ-
                 orleans.fr/mapmo/membres/maitine/MASTER2/FAP/optimFAP.pdf
                 Introduction à l’analyse numérique
                 http ://www.math.uvsq.fr/jaisson/ENSAE cours45.pdf
                 Algorithmes d’optimisation non-linéaire sans contrainte
                 http ://www.math.u-bordeaux1.fr/ bergmann/PDF/These/annexeC.pdf

46/46
~~~
