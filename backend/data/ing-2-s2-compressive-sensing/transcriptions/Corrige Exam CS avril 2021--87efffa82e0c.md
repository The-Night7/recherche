# Corrige Exam CS avril 2021.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1WEMX4jvT5PfSNiTgx126obKAD8vgdcSb) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
               Corrige Exam Compressive Sensing 2021

1. Exercice 1
Voir cours - TDs

2. Exercice 2
    1. En posant:
               f(𝛼) = ‖x - 𝛷 k 𝛼‖ 2 =< x - 𝛷 k 𝛼, x - 𝛷 k 𝛼 > = (x - 𝛷 k 𝛼) T (x - 𝛷 k 𝛼)
                 = x T - 𝛼 T 𝛷 kT (x - 𝛷 k 𝛼) = x T x - 𝛼 T 𝛷 kT x - x T 𝛷 k 𝛼 + 𝛼 T 𝛷 kT 𝛷 k 𝛼
      Les 2ème et troisième termes sont transposés l'un de l'autre. Comme ce sont des
      réels, ils sont égaux. On peut donc écrire :
                                    f(𝛼) = ‖x‖ 2 - 2𝛼 T 𝛷 kT x + 𝛼 T 𝛷kT 𝛷 k 𝛼
      La variable étant 𝛼, x est constant. Le calcul du gradient (voit cours d'optimisation
      déterministe) donne :
                                        ∇f(𝛼) = - 2𝛷 kT x + 2𝛷 kT 𝛷 k 𝛼
      Le minimim est atteint là où le gradient est nul, c à d là où on a :
                                                                                           -1
             -2𝛷 kT x + 2𝛷 kT 𝛷 k 𝛼 = 0     ⟺ 𝛷 kT 𝛷 k 𝛼 = 𝛷 kT x ⟺ 𝛼 = 𝛷 kT 𝛷 k                𝛷 kT x
    2. On sait que pour 𝛼 ∈ R k , on a :
                                                          k
                                               𝛷 k 𝛼 = ∑ 𝛼 i d mi
                                                         i=1
      Autrement dit :      𝛷 k 𝛼 ∈ F = Vect{ d m1 ,..., d mk }
      La recherche de      min ‖x - 𝛷 k 𝛼‖ 22 revient à la recherche de min ‖x - y‖ 22 .
                            𝛼∈R k                                                 y∈F
      F étant un sous-espace vectoriel, on sait que la solution est donnée par :
                        y = Proj F (x) : projection orthogonale de x sur F.
      On a donc bien :
                                              𝛷 k 𝛼 P(kk) = Proj F (x)
    3. A l'étape (k + 1), on part de l'écriture :
                                              x = 𝛷 k 𝛼 P(kk) + R (k)
      Dans cette écriture, le résidu R (k) = x - Proj F (x) est évidemment orthogonal à F.
      Donc il est orthogonal à tous les vecteurs d mi pour i = 1,.., k.
                                        | < d j , R (k) > |
      Conséquence : les rapports                               seront nuls pour tous les vecteurs déjà
                                               ‖d j ‖
      sélectionnés d mi pour i = 1,.., k.
      Lorsqu'on va chercher le maximum :
~~~

## Page 2

~~~text
                                                                  |<dj ,R (k) >|
                                         m k+1 = arg max              ‖d j ‖
                                                       j=1,..,K
      on est sûr que cet indice sera différent de ceux qui ont déjà été sélectionnés
      précédemment.
   4. Etant donné que l'on choisit, à chaque itération, un atome différent des précédents, on
      est sûr que l'algo converge en un maximum de K itérations.
                        1 1 0 1 0         2
   5. Avec D =          0 1 1 -1 1 et x = 1 , on commence par préciser que R (0) = x et
                        0 1 1 0 0         1
     on calcule les 5 rapports dont il faut chercher le maximum :

      j                        1               2                     2             4       5

       |<dj ,R (0) >|          2               4                     2             1       1
           ‖d j ‖                                  3                     2             2

     (a) Le maximum est atteint pour j = 2, donc m 1 = 2.
                        1                              -1
                                                                         2    4
     (b) 𝛷 1 = (d 2 ) = 1  ⟹𝛼 =          (1)
                                               𝛷 1T 𝛷 1 𝛷 1T x = (3) -1
                                                              1 1 1 1 = .
                                                                              3
                        1                                                1
                                                                               0
                                                                              4/3
     La 1ère approximation parcimonieuse de x dans ce dictionnaire est donc :  0
                                                                               0
                                                                               0


3. Exercice 3
   1. La représentation parcimonieuse d'un vecteur x dans un dictionnaire D est l'écriture
      de x comme une combinaison linéaire d'atomes (colonnes) de D avec très très peu
      de composantes non nulles.
   2. Le principe de la relaxation convexe est de remplacer le problème de représentation
      parcimonieuse :
                                 min ‖𝛼‖0 sous contrainte D𝛼 = x
                                     𝛼
     minimisation à l'aide de la pseudo-norme (ℓ 0 ) par une minimisation d'une norme ‖. ‖ p
     avec p ⩾ 1 en utilisant des solveurs convexes.
     Le problème devient :
                                min ‖𝛼‖p sous contrainte D𝛼 = x
                                     𝛼
   3. Le principe des méthodes gloutonnes est de sélectionner à chaque étape l'atome qui
      contribue le plus au signal résiduel R, d'ôter sa contribution et de recommencer si le
~~~

## Page 3

~~~text
  nouveau résidu n'est pas assez petit.
4. (a) L'algo s'arrêt à litération k = 2 car la norme du résidu est de 6, 429.10 -15 ≪ 𝜖
   (b) A la première itération, on sélectionne les atomes dont la contribution est
   supérieure au seuil : 2, 579. ce seront donc les atomes n° 2, 3, 4.
   (c) A la deuxième itération, on sélectionne les atomes dont la contribution est
   supérieure au seuil : 1, 266. ce seront donc les atomes n° 5; 6; 7; 9.
   (d) A l'itération k = 0, 𝛼 = 0.
                                                                                            T
  (e) A l'itération k = 1, 𝛼 =   0 0, 44 1, 20 -0, 32 0 0 0 0 0 0 0 0                           .
  (f) L'estimation finale de 𝛼 est donnée par :
                                                                                    T
   𝛼 = 0 -0, 74 3, 13 -0, 43 0, 75 -8, 74 11, 67 2, 01 0 0 0 0 .
5. (a) L'algo s'arrête à litération k = 6 car la norme du résidu est de 2, 631.10 -14 ≪ 𝜖
  (b) A chaque itération, on sélectionne l'atome dont la contribution est la plus grande.
  Un seul atome à chaquie itération. Soit dans l'ordre, les atomes n° 3; 6; 7; 11; 12; 5.
                                                                            T
  (c) A l'itération k = 1, 𝛼 =   0 0 1, 313 0 0 0 0 0 0 0 0 0                   .
                                                                                    T
  (d) A l'itération k = 2, 𝛼 = 0 0 1, 437 0 0 4, 654 0 0 0 0 0 0                        .
  (e) La représentation parcimonieuse donnée par OMP est :
                                                                        T
  𝛼 = 0 0 1, 92 0 -4, 52 6, 09 -1, 09 0 0 0 0, 84 0, 14                     .
  (f) L'algo. StOMP est très rapide, donne une réprésentation 7-parcimonieuse.
  OMP donne une représentation 6-parcimonieuse mais au bout de 6 itérations. De plus
  le résidu de la méthode StOMP est plus petit.
  Il faut donc choisir StOMP.
~~~
