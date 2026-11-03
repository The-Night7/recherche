# 2425_MI2_EDP_Rattrapage_cor.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1iahBZ4SR-ai9Ze_o6ZnWTXMsCFpVEZlE) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                 RATTRAPAGE - 2ème session


  Année universitaire 2024-2025                         Filière :                      Matière :
                                                        Date :                          Durée :
                                                                  ING2 MI                          EDP


                                                        Responsables :
                                                                22 mai 2025                        2h
                                                                           Kortchemski I. ; Barrau N.


   Aucun document n'est autorisé, Aucun appareil électronique n'est autorisé.
   La qualité de la rédaction sera prise en compte dans la note. Les réponses devront
    être soigneusement justiées.
   Le barème est signalé à titre indicatif (sur 24). Cet examen est composé de deux exercices
    indépendants.


Soit Ω = Ω × Ω =]0; T [×]0; L[ . L'équation de Black-Scholes (transformée) avec condition initiale
Problème 1     Schéma de Crank-Nicolson pour l'équation de Black and Scholes [10pts]


et conditions aux limites peut être écrite sous la forme :
           t    s

                                                 1 2 2 ∂2V
           ∂t (t, x) + rV (t, x) − rx ∂x (t, x) − 2 σ x ∂x2 (t, x)                                 ∀(t, x) ∈ Ω
           ∂V                         ∂V
   
    (1)                                                                  =   0
   
     (2)                                                     V (t = 0, x) =   max(x − K, 0)        ∀x ∈ Ωs
   
    (3)                                                    ∂V
                                                            ∂x (t, x = 0) =   0                    ∀t ∈ Ωt
   
     (4)                                                    V (t, x = L) =    L − Ke−r(T −t)       ∀t ∈ Ωt
où
   la fonction V modélise l'évolution du prix d'un contrat,
   la variable spatiale x représente le prix d'une action,
   les paramètres {r, K, σ} ∈ R .       ∗
                                         +


    PARTIE I : Discrétisation

     1. Décrire votre maillage de Ω : utiliser un dessin; expliciter les quantités h = ∆x et k = ∆t
        en fonction du nombre de discrétisation des intervalles Ω et Ω ; ainsi que les suites de
        noeuds.
                                                                               s       t


     2. La(es) condition(s) initiale(s) correspond(ent) à quelle(s) équation(s) (parmi (1); (2); (3)
        et (4))? Discrétiser les.
     3. La(es) condition(s) aux limites correspond(ent) à quelle(s) équation(s) (parmi (1); (2); (3)
        et (4))? Préciser la nature de chaque condition aux limites et discrétiser-les.
     4. Sur le maillage (de la question 1), marquer les conditions initiales et aux limites.
    PARTIE II : Implémentation

     1. Discrétiser l'équation (1) par la méthode de Crank-Nicolson. Quelle est la précision de la
        méthode?
     2. Écrire l'équation sous la forme matricielle M V = K , préciser la matrice M et le
                                                                     n+1       n

        vecteur K .      n

     3. Proposer un algorithme pour trouver V à chaque instant t . Visualiser l'algorithme sur
                                                         n+1

        le maillage.
                                                                                   n




Soit Ω = Ω × Ω =]0; T [×] − 1; 1[ et considérons les équations suivantes :
Question de cours 2          Questions de cours [14pts]

           t     s

                                                             ∂u         ∂2u
     (1) − u′′ (x) = f1 (x), ∀x ∈ Ωs ,                (2)       (t, x) − 2 (t, x) = f2 (t, x), ∀(t, x) ∈ Ω,
                                                             ∂t         ∂x
                                   ∂u           ∂u
                             (3)      (t, x) +     (t, x) = f3 (t, x),     ∀(t, x) ∈ Ω
où les fonctions f (pour tout                    ) sont des termes source, données.
                                   ∂t           ∂x
                     i              i ∈ {1; 2; 3}


                                                                                                   Tournez svp →
~~~

## Page 2

~~~text
  Considérons également les équations suivantes :
             (i) u(x) = 0, ∀x ∈ ∂Ωs ,           (ii) u′ (−1) = 0,         (iii) u′ (1) + u(1) = 0.

                     (iv) u(0, x) = g(x), ∀x ∈ ∂Ωs ,          (v) u(t, x) = 0, ∀x ∈ ∂Ωs .
où la fonction g est donnée.
  1.   PARTIE I

       (a) Décrire votre maillage de Ω . Préciser votre discrétisation (à pas constats) pour Ω et Ω
           et vos suites de noeuds.
                                          s                                                          s      t


           Ce schéma et ces notations vous serviront également pour la suite.
       (b) L'équation (1) est une équation connue : laquelle? Rappeler sa nature, son ordre, sa di-
           mension.
           Même question pour les équations (2) et (3).
       (c) Que représente ∂Ω et que vaut-il?
                                s
       (d) Que représentent les équations (i) jusqu'à (v) ? Donner leur nom.
        Pour les parties suivantes, on utilisera les notations décrites dans PARTIE I 1.
  2.   PARTIE II

       (a)   Équation (1)

               i. Discrétiser (ii) et (iii). Marquer-les sur votre schéma (PARTIE I 1.)
              ii. Discrétiser (1). Donner les équations discrètes et exprimer-les sous forme matricielle de
                  la forme M · U = K .
             iii. Montrer que la schéma suivant est consistant avec (1)
                                          ui+2 − 16ui+1 + 30ui − 16ui−1 + ui−2
                                                        12(∆x)2
               Quel est l'ordre d'approximation de ce schéma?
       (b)   Équation  (2) muni de (iv) et (v)
            i. Discrétiser (iv) et (v).
           ii. Discrétisons (2) à l'aide du θ-schéma (θ ∈ R ) :+

                    un+1 − uni     un+1 − 2un+1 + un+1            uni+1 − 2uni + uni−1
                     i
                               = βθ i+1     i      i−1
                                                       + β(1 − θ)                      + f2 (tn , xi )
                       ∆t                 (∆x)2                          (∆x)2

             iii. Pour quelle valeur de θ le schéma précédent correspond au schéma d'Euler explicite?
                  d'Euler implicite? Crank-Nicolson?
             iv. Rappeler l'ordre des 3 schémas précédents.
              v. Pour quelle valeur de θ le θ-schéma est-il inconditionnellement stable? Pour quelle
                  valeur de θ le θ-schéma est-il conditionnellement stable (préciser la condition CFL)?
       (c)   Équation (3)

               i. Discrétiser (3) à l'aide d'un schéma upwind (ou explicite décentré en amont). Rappeler
                  son ordre et sa condition de stabilité.
              ii. Discrétiser (3) à l'aide d'un schéma saute-mouton. Rappeler son ordre et sa condition
                  de stabilité.
             iii. Discrétiser (3) à l'aide d'un schéma implicite centré. Rappeler son ordre et sa condition
                  de stabilité.

                                                                                                         Fin.
~~~
