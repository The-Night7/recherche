# Corrige Compressive Sensing avril 24.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1v-p9DyECj2Qk1uocKyl4YUo8TdCiSsA3) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                Corrige Compressive Sensing avril 24
1. Exercice 1
   1) y = vecteur des mesures associées au signal x par l'intermédiaire de la matrice de
      mesures 𝛷.
   2) 𝛼 = représentation parcimonieuse du signal x dans le dictionnaire D.
   3) 𝛴 s = ensemble des vecteurs s-parcimonieux =           x ∈ R N , ℓ0 (x) ⩽ s
      = ensemble des vecteurs dont le nombre de composantes non nulles ne dépasse
     pas s.
     𝛴 s n'est pas un sous-espace vectoriel car il n'est pas stable par addition.
                               K
   4) On sait que : y = A𝛼 =   ∑ 𝛼j Aj .
                               j=1
        a) Comme 𝛼 j = 0 pour j ∉ L, on en déduit :

                                             y = ∑ 𝛼j Aj
                                                    j∈L
        b) Supposons que les (A j , j ∈ L) ne sont pas linéairement indépendants, on peut
           donc exprimer l'une de ces colonnes, A j0 , comme combinaison linéaire des
           autres, mettons

                                           A j0 =     ∑ 𝛾j Aj
                                                    j∈L, j≠j0

          En remplçant A j0 dans l'expression y =      ∑ 𝛼j Aj , on arrive ainsi à exprimer y
                                                       j∈L
           comme combinaison linéaire des A j , j ∈ L, j ≠ j 0 , doit (s - 1) colonnes
           seulement.
           On trouve ainsi une représentation (s - 1)-parcimonieuse de y par rapport à A.
           Ceci contredit le fait que 𝛼, avec ℓ 0 (𝛼) = s, soit la solution du pb. de
           minimisation (ℓ 0 ).
           Conclusion : les vecteurs (A j , j ∈ L) sont forcément linéairement indépendants.
        c) Si la matrice A possède s colonnes indépendantes, alors son rang est supérieur
           à s.
           D'autre part, l'ordre de cette matrice est M × K, avec M < K. Par conséquent
           son rang est inférieur à M. En résumé :
                                            s ⩽ rang(A) ⩽ M.
   5) On suppose Ker(A) ∩ 𝛴 2s = { 0 K }.
        a) Supposons que le pb. de minimisation (ℓ 0 ) admette 2 solutions s-
           parcimonieuses 𝛼 et 𝛽.
~~~

## Page 2

~~~text
             On a donc :            𝛼, 𝛽 ∈ 𝛴 s et A𝛼 = A𝛽 = y.
             On en déduit :        𝛾 = 𝛼 - 𝛽 ∈ 𝛴 2s et A𝛾 = A𝛼 - A𝛽 = 0.
             Autrement dit :       𝛾 ∈ 𝛴 2s et 𝛾 ∈ Ker(A) ⟹ 𝛾 ∈ Ker(A) ∩ 𝛴 2s = { 0 K }.
             Conclusion :          𝛾 = 0 ⟹ 𝛼 = 𝛽.
             Il y a donc bien unicité de la solution dans 𝛴 s .
          b) Les seules composantes non nulles de 𝛼 sont les 𝛼'j , il y en a exactement 2s.
             Donc 𝛼 ∈ 𝛴 2s .
          c) On voit immédiatement que :
                                      A𝛼 = A [J] 𝛼' = 0     ⟹ 𝛼 ∈ Ker(A).
          d) A partir de n'importe quel vecteur 𝛼' ∈ Ker(A [J] ), on peut construire, comme
             précedemment, un vecteur 𝛼 ∈ Ker(A) ∩ 𝛴 2s = { 0 K } ⟹ 𝛼 = 0 ⟹ 𝛼' = 0.
             Donc Ker(A [J] ) = { 0 }.
          e) Ker(A [J] ) = { 0 } signifie que les 2s colonnes de A [J] sont indépendantes. En
             suivant le raisonnement de 4.c), on obtient M ⩾ 2s.


2. Exercice 2
Il y avait une ambiguïté dans la manière dont les indices sont ordonnés. Soit dans
l'ordre décroissant d'importance des contributions, soit dans l'ordre croissant des
indices. C'est ce dernier choix qui est fait dans ce corrigé.
J'en ai tenu compte dans la correction des copies.
      1) Itération 1 : On notera les indices en suivant la convention de Python. s = 4.
            a) On prend les 8 plus grandes contributions : Supp 1 = [0, 3, 5, 6, 7, 9, 10, 12].
            b) Supp = [∅] ∪ Supp 1 = Supp 1 = [0, 3, 5, 6, 7, 9, 10, 12].
            c) 𝛼 Supp est obtenu en résolvant le pb. aux moindres carrés A [Supp] 𝛼 Supp = y.
             La solution est obtenue à l'aide du pseudo-inverse A [†Supp] par : 𝛼 Supp = A [†Supp] y.
          d) On conserve les s plus grands coefs en valeur absolue : Supp = [0, 3, 7, 10].
          e) Après rejet, on peut écrire :
                            y = 1.374A 0 - 1.685A 3 + 1.09A 7 - 0.619A 10 + R (1) .
          f) ‖R (1) ‖ = ‖y - (1.374A 0 - 1.685A 3 + 1.09A 7 - 0.619A 10 )‖.
    2) Itération 2 :
          a) On prend les 8 plus grandes contributions : Supp 1 = [0, 1, 2, 3, 4, 7, 12, 13].
          b) Supp = [0, 3, 7, 10] ∪ Supp 1 = [0, 1, 2, 3, 4, 7, 10, 12, 13].
          c) En ne tenant pas compte des 2 dernières composantes de 𝛼 Supp , on retient :
                                           Supp = [0, 1, 2, 13].
          d) y = -2A 0 + A 1 + A 2 + A 13 + R (2) .
          e) ‖R (2) ‖ = ‖y - (-2A 0 + A 1 + A 2 + A 13 )‖ = 4.96 × 10 -15 . L'algorithme a
             convergé et donné une représentation exacte (résidu nul) :
~~~

## Page 3

~~~text
             y = -2A0 + A 1 + A 2 + A 13 .


3. Exercice 3
   1) f j (z) = ‖R (k-1) - zd j ‖ 2 .
         a) f j (z) = ‖R (k-1) - zd j ‖ 2 = ‖R (k-1) ‖ 2 + z 2 ‖d j ‖ 2 - 2 < R (k-1) , zd j >
                                        f(z) = z 2 ‖d j ‖ 2 - 2zd jT R (k-1) + ‖R (k-1) ‖ 2 .
         b) Il s'agit d'une fonction polynômiale de degré 2. Son minimum est atteint pour
                    2d jT R (k-1)       < d j , R (k-1) >
              *
             z =                    =                             .
                      2‖d j ‖ 2               ‖d j ‖ 2
         c) Ce minimum a pour valeur :
                                                         2
                                        d jT R (k-1)                          d jT R (k-1)
                        fj z   *
                                    =              2
                                                                  2
                                                             ‖d j ‖ - 2                  2
                                                                                              d jT R (k-1) + ‖R (k-1) ‖ 2
                                          ‖d j ‖                                ‖d j ‖
                                                                          2                                                  2
                                                        d jT R (k-1)                                     < d j , R (k-1) >
                    f j z * = ‖R (k-1) ‖ 2 -                          2
                                                                              = ‖R (k-1) ‖ 2 -                                   .
                                                             ‖d j ‖         ‖d j ‖ 2
         d) Le terme ‖R (k-1) ‖ 2 étant constant, chercher le minimum de f j z * , parmi les
                                                                                                              2
                                                                                     < d j , R (k-1) >
             indices j, revient à chercher le maximum de                                                          .
                                                                                              ‖d j ‖ 2
             Autrement dit, en prenant les racines carrées :
                                                                          | < d j , R (k-1) > |
                                            m k = arg max                                                .
                                                                                     ‖d j ‖
                                                       < d mk , R (k-1) >
                                *
   2) On a évidemment : z k = z m   =                                            .
                                  k
                                                    ‖d mk ‖ 2
   3) x = z 1 d m1 + z 2 d m2 + ... + z k-1 d mk-1 + R (k-1) , d'une part.
      x = z 1 d m1 + z 2 d m2 + ... + z k-1 d mk-1 + z k d mk + R (k) , d'autre part. Par conséquent :
                                              R (k) = R (k-1) - z k d mk
~~~
