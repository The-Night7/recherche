# Corrigé examen Compressive Sensing 04-22.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1uAdhg79eQfvmRWBkjIMbBvlf0ai8NoTZ) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
           Corrigé examen Compressive Sensing 04-22
1. EXERCICE 1 (Questions de cours)
   1. Expliquer le principe général du procédé du compressive sensing.
      Le principe est de réduire la taille du signal dès l'acquisition, grâce à une matrice de
      mesure 𝛷, puis d'utiliser un dictionnaire D adapté pour avoir une représentation
      parcimonieuse 𝛼 de ce signal.
      Les choix de ces deux matrices sont faits pour faciliter d'une part l'obtention de 𝛼 et
      d'autre part la reconstruction du signal à partir de 𝛼.
   2. Expliquer l’intérêt d’un dictionnaire dans le procédé du compressive sensing.
      Le choix du dictionnaire est essentiel pour espérer obtenir une représentation
      parcimonieuse. Il y a des dictionnaires déjà connus pour être adaptés à certains types
      de signaux (Fourier discret, cosinus discret,..) et il y a des dictionnaires que l'on
      construit (que l'on apprend) à partir d'une famille de signaux donnés.
   3. Donner la définition de la cohérence mutuelle. Comment choisir la matrice de mesure
      Φ relativement à la cohérence mutuelle avec le dictionnaire D.
      La cohérence mutuelle de 2 matrices 𝛷 et D est :
                                                    | < 𝛷i,. , D.,j > |
                          𝜇(𝛷, D) =      N max
                                              i,j     ‖𝛷i,. ‖ ‖D.,j ‖
      Le choix de 𝛷 est fait de manière à avoir la plus petite cohérence mutuelle possible.
   4. Démontrer qu’à chaque itération k ⩾ 1 de la méthode de la poursuite gloutonne OMP,
      l’algorithme ne sélectionne pas un atome déjà sélectionné à l’itération k − 1.
      A l'étape k, le signal s'écrit :
                         x = z1(k-1) dm1 + z2(k-1) dm2 + ... + zk-
                                                                 (k-1)
                                                                   1 d mk-1 + R
                                                                                (k-1)

     La 1ère partie est la projection orthogonale de x sur F = Vect{ d m1 , d m2 ,..., d mk-1 } .
                                             x = ProjF (x) + R (k-1)
     Par conséquent, R (k-1) = x - Proj F (x) est orthogonal à F, et donc à tous les
     vecteurs d m1 , d m2 ,..., d mk-1 .
     Autrement dit : < d j , R (k-1) > = 0 pour j = m 1 , m 2 ,.., m k-1 .
     Le choix de l'atome suivant d mk se fait en cherchant le maximum suivant :
                                                         | < djT , R (k-1) |
                                         mk = Arg maxj
                                                              ‖dj ‖
     Ce maximum ne sera jamais atteint pour j = m 1 , m 2 ,.., m k-1 puisque les numérateurs
     sont nuls.
     Conclusion : m k sera différent de tous les m i déjà sélectionnés.

2. EXERCICE 2 (Apprentissage d’un dictionnaire )
   1. Rappeler la définition de la pseudo-norme ℓ 0 qu’on note communément ‖. ‖ 0 .
~~~

## Page 2

~~~text
   Pourquoi ‖. ‖ 0 n’est pas une norme?
   ℓ0 (x) = ‖x‖0 = nbre de composantes non nulles de x.
   Ce n'est pas une norme car ℓ 0 (2x) = ℓ 0 (x).
2. Que signifie s dans la contrainte ℓ 0 (𝛼) ⩽ s du problème (1) ?
   Cela signifie que l'on recherche une représentation s-paricimonieuse : avec au
   maximum s composantes non nulles.
3. Pour i = 1,..., K , on note 𝛬 i,. la i-ème ligne de la matrice 𝛬et on écrit :
          K
  D𝛬 = ∑ d (i) 𝛬i,.
          i=1
  (a) Montrer que rang d (i) 𝛬 i,. ⩽ 1 .
  Cette matrice est obtenue en multipliant une colonne par une ligne. Le résultat est une
  matrice dont toutes les colonnes sont des multiples de d (i) et toutes les lignes des
  multiples de 𝛬 i,. . Ce sera donc une matrice de rang ⩽ 1.
  (b) Établir une condition nécessaire et suffisante pour que rang d (i) 𝛬 i,. = 1.
  La seule chose qui peut l'empêcher d'avoir un rang = 1 est qu'elle soit nulle. Comme
  d (i) est un vecteur unitaire, il ne peut pas être nul. Ce serait donc à cause de 𝛬i,. qui
  serait nul.
  Il suffit donc que la ligne 𝛬 i,. contienne une seule composante non nulle pour que le
  rang soit égal à 1.
  (c) Montrer que ‖X - D𝛬‖ F = ‖E i - d (i) 𝛬 i,. ‖ F où E i est l’erreur sur les ℓ signaux
  lorsqu’on ne tient plus compte de la contribution de d (i) .
                         k                         k
  ‖X - D𝛬‖F = ‖X - ∑ D.,q 𝛬q,. ‖F = ‖X - ∑ D.,q 𝛬q,. - D.,i 𝛬i,. ‖F = ‖Ei - D.,i 𝛬i,. ‖F
                        q=1                     q=1,q≠i


4. (a) Expliquer le principe général de l’apprentissage d’un dictionnaire D.
   On part d'une famille de signaux et d'un dictionnaire initial donné. On construit de
   manière itérative un dico adapté à nos signaux.
   (b) Présenter les deux étapes majeurs de l’apprentissage du dictionnaire.
   Phase1 : on fixe le dictionnaire D et on construit la représentation parcimonieuse de
   tous les signaux. Phase 2 : on fixe la représentation parcimonieuse et on met à jour le
   dictionnaire colonne par colonne.
   (c) Donner 2 façons différentes pour initialiser le dictionnaire.
    On peut partir d'un dico construit de manière aléatoire ou d'un dico construit à partir
   de certains signaux normalisés.
   (d) Supposons que le dictionnaire initial D 0 est connu. Comment déterminer 𝛬?
   On utilise un algo. de représentation parcimonieuse, comme OMP, pour obtenir les
   repérsentations de tous les signaux dans le dictionnaire D 0 . Ces repréesentations
   constitueront les colonnes de la matrice 𝛬.
~~~

## Page 3

~~~text
   5. Pour que la condition établie à la question 3.(b) soit vérifiée, on s’intéresse au
     problème de minimisation de ‖E iR - D .,i 𝛬 iR,. ‖ F où 𝛬 iR,. = 𝛬 i,. 𝛺 i et E iR = E i 𝛺 i
     (a) Quel est le rôle de la matrice 𝛺 i ?
     La matrice 𝛺 i sert à ne conserver que les composantes non nulles de 𝛬 i,. .
     𝛬iR,. ne contient que des composantes non nulles, toutes celles de 𝛬i,.
     (b) Quelle est la meilleure approximation de E iR au sens de la norme de Frobenius?
     Justifier.
     D 'après le théorème d'Ekhart-Young, c'est la décomposition en valeurs singulières de
     EiR qui va nous donner : EiR = U 𝛥 V T et qui permet de déterminer la matrice de
     rang 1 la plus proche de E iR qui est:
                                          U.,1 𝛥1,1 (V.,1 ) T
     (c) Comment fait-on la mise à jour des vecteurs d (i) et 𝛬 iR,. ?
                                                   d (i) ← U.,1
                                             𝛬iR,. ← 𝛥1,1 (V.,1 ) T


3. Exercice 3




   1. Quelle est la taille du dictionnaire appris ?
      La taille de D sera 6 × 10 .
   2. Quelle condition doit-on imposer sur les atomes du dictionnaire initial?
      Les atomes du dictionnaire initial doivent être normalisés (norme = 1).
   3. Ci-dessous les résultats partiels du dictionnaire initial:




     À l’issue de cette initialisation, on applique la méthode gloutonne Orthogonal Matching
     Pursuit sur les x (j) , j = 1,..., 24 et on obtient la matrice 𝛬.
     Ci-dessous quelques résultats partiels:
~~~

## Page 4

~~~text
  Transposée de la 1ère colonne de 𝛬 :
                        (1.73 , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.)
  3ème ligne de 𝛬 :
           (0 0 9.3 0 0 0 0 0 0 0 0 0 0 0 0 0 - 2.4 0 0 0 0 0 0 0)
  (a) Que représente la 1ère colonne de 𝛬 relativement à X ?
  La première colonne de 𝛬 est la représentation parcimonieuse du 1er signal (1ère
  colonne de X) dans le dictionnaire courant.
  (b) Que représente la 3ème ligne de 𝛬 relativement à X ?
  La 3ème ligne de 𝛬 représente la contribution de l'atome n°3 du dictionnaire actuel à
  la représentation parcimonieuse de tous les signaux.
  (c) Afin de mettre à jour l’atome i, i = 1,..., 10 , on calcule le support de la i-ème ligne
  de 𝛬 qu’on note :
                           wi = k, 1 ⩽ k ⩽ 24 tel que 𝛬i,k ≠ 0
  Calculer w 3 .
  Ensemble des indices des composantes non nulles de 𝛬 3,.
                                          w3 = { 3 ; 17 }
4. Le dictionnaire a été entrainé L fois. On note C 5 et C 15 la cinquième et la quinzième
   colonne respectivement de la matrice 𝛬. DC 5 et DC 15 désignent les produits
  matriciels en utilisant le dictionnaire résultant de la mise à jour KSVD.
  Ci-dessous des résultats pour deux valeurs différentes de L :




Donner une analyse des résultats du tableau (Table 1): Le choix de L, la parcimonie, la
reconstruction du signal. . .
Attention au décalage lié à la numérotation de Python !!
A l'itération L = 1, le dictionnaire initial est constitué des 10 premiers signaux normalisés.
Il est donc normal que C 5 : représentation du signal de la 6ème colonne de X n'ait
qu'une seule composante, égale à la norme de cette colonne. La reconstruction de ce
signal, par DC 15 est donc parfaite.
~~~

## Page 5

~~~text
Le signal de la colonne 16 de X possède une représentation 6-parcimonieuse et est
bien reconstitué à environ 10 -13 près.
A l'itération L = 2, les 2 signaux ont une représentation 6-parcimonieuse et sont bien
reconstitués à environ 10 -13 près.
Si ça ne tenait quà ces 2 signaux, on pourrait s'arrêter à la 1ère itération. Mais il faut
tenir compte des 24 signaux formant X, ou plutôt de leur représentation parcimonieuse,
pour décider.
~~~
