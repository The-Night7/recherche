# td1--exercices 8 et 9--24-26.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1KrxOn-4WSN32bnEFK3gn_9K37WNT3zOm) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
      Résolution Graphique des Équations Différentielles
                                          (Exercices 8 & 9)

                                            Yalçin Aktar

                                               08.02.26


Exercice 8 : Comprendre le sens des flèches
 Le secret des champs de vecteurs : Imaginez que le plan est quadrillé. En chaque point de
 coordonnées (t, x) de ce plan, l’équation différentielle définit une direction imposée.
      La règle est la suivante : Si une solution courbe x(t) passe par le point (t, x), alors sa pente
 x′ (t) doit valoir :
                                            Pente = f (t, x)
     Pour tracer le champ, on prend des points (t, x) au hasard et on applique la règle :
     — Résultat positif (+) → La flèche pointe vers le HAUT (↗).
     — Résultat négatif (-) → La flèche pointe vers le BAS (↘).
     — Résultat nul (0) → La flèche est HORIZONTALE (→).




1. L’équation x′ = 1 − t
   Étape 1 : On teste des points pour comprendre l’orientation. L’équation nous dit que la
pente vaut 1 − t. Remarquez que x ne joue aucun rôle (la hauteur ne change rien à la pente).
   — Test en t = 0 (sur l’axe vertical) :

                                             Pente = 1 − 0 = +1

     ⇒ C’est positif. La flèche monte à 45°.
   — Test en t = 1 :
                                           Pente = 1 − 1 = 0
     ⇒ C’est nul. La flèche est plate (horizontale).
   — Test en t = 3 :
                                           Pente = 1 − 3 = −2
      ⇒ C’est très négatif. La flèche plonge vers le bas très vite.
   Étape 2 : Visualisation par zones.




                                                   1
~~~

## Page 2

~~~text
CY TECH – ING1 GM                                                            Corrigé TD1 - Exercices 8 & 9


                                 Champ de vecteurs x′ = 1 − t
               3
                    ZONE DE MONTÉE                                ZONE DE DESCENTE
               2     t < 1 =⇒ Pente +                               t > 1 =⇒ Pente -




                                          Sommet (Pente 0)
                            ↗                                              ↘
               1
          x




                                                                       So
                                                                          l
               0




                                                                           ut
                                                                              io
                                                                                n
              −1

              −2
               −1     −0.5   0     0.5         1                 1.5   2       2.5   3    3.5
                                                             t




                                                     2
~~~

## Page 3

~~~text
CY TECH – ING1 GM                                                   Corrigé TD1 - Exercices 8 & 9


2. L’équation x′ = −x/2
   Étape 1 : On teste des points (Pourquoi les flèches se retournent ?). L’équation nous dit
que la pente vaut −x/2. Ici, t ne joue aucun rôle (avancer dans le temps ne change pas la pente).
   — Test en un point HAUT (ex : x = 2) :

                                             Pente = −2/2 = −1

     ⇒ C’est négatif. La flèche pointe vers le bas. (Logique : si on est trop haut, on redescend vers
     l’équilibre).
   — Test sur l’axe (x = 0) :
                                           Pente = −0/2 = 0
     ⇒ La flèche est plate. Si on est à 0, on y reste.
   — Test en un point BAS (ex : x = −4) :

                                      Pente = −(−4)/2 = +4/2 = +2

      ⇒ C’est positif ! La flèche pointe vers le haut. (C’est ça l’orientation "bizarre" : un x négatif
      donne une pente positive à cause du signe moins).
   Étape 2 : Visualisation par zones.

                                      Champ de vecteurs x′ = −x/2
                    3
                                               X POSITIF
                    2                         Pente Négative
                                                    ↘
                    1
                                                                 Équilibre (Pente 0)
                    0
               x




                   −1
                                              X NÉGATIF
                   −2                         Pente Positive
                                                   ↗
                   −3
                    −1    −0.5    0    0.5     1       1.5   2    2.5    3     3.5     4
                                                        t


  Bilan :
     — Dans le premier cas, la pente dépendait du temps (gauche/droite).
     — Dans le deuxième cas, la pente dépendait de la position (haut/bas).
  C’est pour cela que les dessins sont si différents !




                                                   3
~~~

## Page 4

~~~text
CY TECH – ING1 GM                                                   Corrigé TD1 - Exercices 8 & 9


Exercice 9 : Identification des Champs de Vecteurs
  Méthodologie d’Identification : Pour associer une équation différentielle x′ = f (t, x) à son
  champ de vecteurs, on étudie deux propriétés géométriques fondamentales :
      1. Les Isoclines : L’ensemble des points (t, x) où la pente est constante.
         — Isocline nulle : Où a-t-on x′ = 0 ? (Tangentes horizontales).
         — Isocline infinie : Où a-t-on x′ → ±∞ ? (Tangentes verticales).
      2. Les Invariances :
         — Si f (t, x) ne dépend pas de t, le dessin est identique par translation horizontale.
         — Si f (t, x) ne dépend pas de x, le dessin est identique par translation verticale.



Cas 1 : L’équation x′ = 2
   Analyse :
   — La pente est constante et vaut +2 pour tout point (t, x) du plan.
   — Résolution : x(t) = 2t + C. Les solutions sont des droites parallèles.
Signe distinctif : Une "pluie oblique" uniforme. Toutes les flèches sont parallèles.
                                                   x′ = 2
                                 2


                                            Pente = 2 partout
                                 0
                           x




                                             (Isocline globale)


                               −2
                                −2         −1          0        1        2
                                                       t

Cas 2 : L’équation x′ = x − t
   Analyse :
   — Isocline Nulle : La pente s’annule si x − t = 0 ⇐⇒ x = t.
   — Observation : Sur la première bissectrice (la droite y = x), toutes les tangentes doivent être
     horizontales.
   — Comportement :
     — Si x > t (au-dessus de la bissectrice), x′ > 0 (ça monte).
     — Si x < t (en dessous de la bissectrice), x′ < 0 (ça descend).

                                                 x′ = x − t
                                 2

                                 1
                                                       Isocline 0
                                 0
                           x




                               −1

                               −2
                                −2         −1          0        1        2
                                                       t


                                                   4
~~~

## Page 5

~~~text
CY TECH – ING1 GM                                              Corrigé TD1 - Exercices 8 & 9


Cas 3 : L’équation x′ = x
  Analyse :
  — Équation Autonome : La pente ne dépend pas de t. Le dessin est invariant par translation
    horizontale.
  — Isocline Nulle : x′ = 0 ⇐⇒ x = 0. L’axe des abscisses est une solution d’équilibre.
  — Signe : Si x > 0, ça monte. Si x < 0, ça descend.

                                                  x′ = x
                             2


                                  Isocline 0 (x = 0)
                             0
                        x




                            −2
                             −2          −1            0   1       2
                                                       t




                                                 5
~~~

## Page 6

~~~text
CY TECH – ING1 GM                                                             Corrigé TD1 - Exercices 8 & 9


Cas 4 : L’équation x′ = x/t
  Analyse :
  — Singularité : En t = 0, la pente est infinie (division par zéro).
  — Isocline Nulle : x′ = 0 ⇐⇒ x = 0.
  — Visuel : Un faisceau de droites passant par l’origine.

                                                x′ = x/t
                               2

                               1

                                                                        Isocline 0
                               0
                          x




                                                     Pente Infinie
                              −1

                              −2
                               −2        −1          0                   1           2
                                                     t


Cas 5 : L’équation x′ = t
  Analyse :
  — Isocline Nulle : x′ = 0 ⇐⇒ t = 0. Sur l’axe vertical, toutes les tangentes sont horizontales.
  — Invariance : Ne dépend pas de x (translation verticale possible).

                                                 x′ = t
                               2
                                                               Isocline 0


                               0
                          x




                              −2
                               −2        −1          0                   1           2
                                                     t


Cas 6 : L’équation x′ = −t/x
  Analyse :
  — Singularité : En x = 0, division par zéro (pente verticale).
  — Orthogonalité : La solution est perpendiculaire au rayon vecteur.
  — Visuel : Des cercles concentriques.




                                                 6
~~~

## Page 7

~~~text
CY TECH – ING1 GM                                      Corrigé TD1 - Exercices 8 & 9


                                       x′ = −t/x
                         2

                         1

                         0              Cercles



                    x
                        −1

                        −2
                             −2   −1       0       1   2
                                           t




                                       7
~~~
