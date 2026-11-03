# DS2-2020-2021-Correction-(V1-et-V2)_Algebre2-DS_P1S2_MBahtiti-KGuezguez-AHajej-BLaquerriere-JMasereel.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1NEmZ2nB8JjZb9USZEYSDIHc_yupq5Y95) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                Cycle préparatoire 1ère année
                                                          Devoir surveillé 5
                                            M. Bahtiti, K. Guezguez, A. Hajej, B. Laquerriere, J.-M. Masereel
                        Matière : Algèbre                                            Date : Jeudi 29 avril 2021
                        Appareils électroniques et documents interdits               Durée : 1 heures 30 minutes
                                                                                     Nombre de pages : 10


     Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.
        Le sujet comporte cinq exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.


                                                         

Exercice 1 (Espaces vectoriels : (3 point(s).)). Parmi les ensembles suivants, déterminer ceux qui sont
des espaces vectoriels.

              (E1 , ⊕, ⊗) avec E1 = R∗+ , ∀x , y ∈ E1 , x ⊕ y = x y   et   ∀λ ∈ R, λ ⊗ x = x λ
              (E2 , ⊕, ⊗) avec E1 = R[X ], ∀P,Q ∈ E2 , P ⊕ Q = P 0 + Q 0    et     ∀λ ∈ R, λ ⊗ P = λP

                                                      
    (1.5 point(s).) E1 est un espace vectoriel (c’est un exercice du TD).
(1.5 point(s).) E2 pas un ev car, il n’est pas possible d’avoir d’élément neutre (P 6= P 0 en général)

Exercice 2 (Espaces vectoriels : (3 point(s).)). On rappelle que R3 [X ] est l’espace vectoriel des polynômes
à coefficients réels de degré inférieur ou égal à 3.
  1. Donner une base et la dimension de R3 [X ].
  2. Montrer que la famille B = (X 3 + 1, X 3 − 1, X 2 + X , X 2 − X ) est une base de R3 [X ].
  3. Calculer les coordonnées du polynôme X 3 + 2X + 1 dans la base B .
                                                         
  1. (0.25+0.25 point(s).) La dimension est 4 et la base canonique est (1, X , X 2 , X 3 ).
  2. (1 point(s).) La famille possède 4 vecteurs, il suffit donc de montrer qu’elle est libre.

                                                                                   a +b = 0
                                                                                 
                                                                                 
                                                                                   c +d = 0
                                                                                 
                      a (X 3 + 1)b (X 3 − 1) + c (X 2 + X ) + d (X 2 − X ) = 0 ⇔
                                                                                  c −d = 0
                                                                                   a −b = 0
                                                                                 

                                                                             ⇔a =b =c =d =0

     La famille est donc bien une base.
  3. (1.5 point(s).) En reprenant le système précédent, on obtient :

                                                                                    a +b       =   1
                                                                                  
                                                                                  
                                                                                    c +d       =   0
                                                                                  
            a (X 3 + 1)b (X 3 − 1) + c (X 2 + X ) + d (X 2 − X ) = X 3 + 2X + 1 ⇔
                                                                                   c −d       =   2
                                                                                               =
                                                                                  
                                                                                    a −b           1
                                                                                 ⇔ a = 1, b = 0, c = 1, d = −1

     Les coordonnées sont donc (1, 0, 1, −1).

                                                       - 1 / 10 -
~~~

## Page 2

~~~text
Exercice 3 (Espaces vectoriels : (7 point(s).)). Soit E le sous-espace vectoriel de R4 défini par

                           E = {x , y , z , t ) ∈ R4 / x + y + z − t = 0 et 2y + z + t = 0}

  1. Déterminer une base et la dimension de E .
  2. Soit F le sous-espace vectoriel de R4 engendré par

                             u 1 = (1, −2, 1, 1)       u 2 = (2, 1, −1, 1)    u 3 = (0, 5, −3, −1)

     Déterminer une base et la dimension de F .
  3. Déterminer un système d’équation de F .
  4. Déterminer une base et la dimension de E ∩ F .
  5. Déduire de ce qui précède la dimension de E + F .
  6. Déterminer une base de E + F .
                                                           
  1. (1+0.25 point(s).) On résout le système et on obtient t = −2y − z et x = t − y − z = −3y − 2z . Donc
     une base est ((−3, 1, 0, −2), (−2, 0, 1, −1)). La dimension est 2.
  2. (0.5+0.25 point(s).) On remarque que u 3 = u 2 − 2u 1 . Donc F est engendré par u 1 , u 2 qui est une
     famille libre (vecteurs non colinéaires), donc base. La dimension est 2.
  3. (1.5 point(s).) Soit u (x , y , z , t ) ∈ R4 , alors nous avons les équivalences :

                                                                                   x = a + 2b
                                                                                 
                                                                                 
                                                                                   y = −2a + b
                                                                                 
                   u ∈ F ⇔ ∃(a , b ) ∈ R2 , u = a u 1 + b u 2 ⇔ ∃(a , b ) ∈ R2 ,
                                                                                  z = a −b
                                                                                   t = a +b
                                                                                 
                                            
                                                        1
                                            
                                              a = 2 (z + t )
                                               b = 12 (t − z )
                                            
                         ⇔ ∃(a , b ) ∈ R2 ,
                                              x = 12 (z + t ) + t − z = 12 (3t − z )
                                               y = −(z + t ) + 12 (t − z ) = − 21 (3z + t )
                                            
                                            
                           
                              2x + z − 3t = 0
                         ⇔
                              2y + 3z + t = 0
                                                   
                                                        2x + z − 3t     = 0
     Un système d’équations de F est donc
                                                        2y + 3z + t     = 0




                                                        - 2 / 10 -
~~~

## Page 3

~~~text
  4. (1+0.25 point(s).) Le plus simple est de résoudre le système linéaire de E ∩ F : Soit u ∈ R4 , alors

                                                                             x +y +z −t = 0
                                                                           
                                                                           
                                                                               2y + z + t = 0
                                                                           
              u ∈ E ∩ F ⇔ ∃(x , y , z , t ) ∈ R4 , u = (x , y , z , t ) et
                                                                             2x + z − 3t = 0
                                                                              2y + 3z + t = 0
                                                                           

                                                                             x +y +z −t = 0
                                                                           
                                                                           
                                                                               2y + z + t = 0
                                                                           
                        ⇔ ∃(x , y , z , t ) ∈ R4 , u = (x , y , z , t ) et
                                                                              2y + z + t = 0 (2L 1 − L 3 )
                                                                                       2z = 0 (L 4 − L 2 )
                                                                           
                                                                           
                                                                                     z = 0
                                               4
                        ⇔ ∃(x , y , z , t ) ∈ R , u = (x , y , z , t ) et         x+y = t
                                                                             2y + x + y = 0
                                                                           
                                                                           
                                                                            z = 0
                        ⇔ ∃(x , y , z , t ) ∈ R4 , u = (x , y , z , t ) et   x = −3y
                                                                             t = −2y
                                                                           

                           ⇔ ∃(x , y , z , t ) ∈ R4 , u = y (−3, 1, 0, −2)
                           ⇔ u ∈ Vect ((−3, 1, 0, −2))

       Donc E ∩ F = Vect ((−3, 1, 0, −2)), le vecteur étant non nul, il forme donc une base. La dimension est
       donc 1.
  5. (0.5 point(s).) En utilisant la formule de Grassmann, on obtient dim(E + F ) = dim(E ) + dim(F ) −
     dim(E ∩ F ) = 3.
  6. (1 point(s).) Nous avons E +F = Vect (() E ∪F ). Pour simplifier, nous allons nous appuyer sur l’inter-
     section. Puisque E ∩ F ⊂ F , nous avons F = Vect ((1, −2, 1, 1), (−3, 1, 0, −2)), ainsi en réunissant cette
     base de F et celle de E (qui contient déjà un vecteur de l’intersection), nous avons directement une
     base de E + F = Vect ((−3, 1, 0, −2), (−2, 0, 1, −1), (1, −2, 1, 1))

Exercice 4 (Espaces vectoriels et Morphismes : (12 point(s).)). Soit f1 l’application définie par :
                                        
                                                   R4 −→ R
                                   f1 :
                                          x ; y ;z ;t  7−→ x − y + 2t

  1. Montrer que f1 est une application linéaire.
Soit f l’application définie par :
                       
                                       R4 −→ R3
                     f :                                                                    
                              x ; y ;z ;t  7−→ f1 (x , y , z , t ) ; x + y + 2z ; y + z − t

On admet par la suite que f est une application linéaire.
  2.
        (a) Déterminer une base du noyau de f .
       (b) Déterminer les dimension du noyau et de l’image de f .
        (c) Déterminer l’image de f .
  3. L’application f est-elle injective ? surjective ? bijective ?
              
  4. Soit F = (x ; y ; z ) ∈ R3 / x = y − 2z
        (a) Montrer que F est un espace vectoriel.

                                                         - 3 / 10 -
~~~

## Page 4

~~~text
     (b) Montrer que Im(f ) = F .
5.
     (a) Compléter la base trouvée en 2.(a) en une base de R4 .
     (b) En déduire un supplémentaire du noyau.
6. Soit H = Vect ((1; 0; 0; 0); (0; 1; 0; 0)).
     (a) Montrer que R4 = Ker(f ) ⊕ H .
     (b) Montrer que ϕ(1, 0, 0, 0) = (−1; 1; 1) et ϕ(0, 1, 0, 0) = (0; 2; 1) suffit à déterminer une application
         linéaire ϕ de H dans Im(f ).
     (c) Montrer que                            
                                                               H −→ Im(f )
                                           ϕ:                                              
                                                    (x ; y ; 0; 0) 7−→ −x ; x + 2y ; x + y

     (d) L’application ϕ est-elle injective ? surjective ? bijective ?
     (e) Montrer que Im(f ) est isomorphe à un supplémentaire de Ker(f ).
                                                             
1. (1 point(s).) On montre aisément que f1 (u + λv ) = f (u ) + λf (v ).
2.
                                                                
                                                              x − y + 2t = 0
     (a) (1 point(s).) f x ; y ; z ; t = (0 ; 0 ; 0 ; 0 ; 0) ⇔                (après réduction du système).
                                                                y +z −t = 0
                                                      
                                      −1           −1
                                 −1   1 
         Donc Ker(f ) = Vect    1  ;  0 . Cette famille est génératrice et comme elle est libre
                                                       

                                       0             1
         (vecteurs non colinéaires) c’est une base.
     (b) (0.5 point(s).) Le noyau est donc de dimension 2. L’image est alors, d’après le théorème du
         rang, de dimension 4-2=2.
                                                                                       
     (c) (1 point(s).) Nous savons que Im(f ) = Vect f (e1 ); f (e2 ); f (e3 ); f (e4 ) . La dimension étant 2,
         il suffit 
                   doncde prendre   2 vecteurs
                                             non colinéaires dans cette famille pour avoir une base.
                     1                  −1
         f (e1 ) =  1  et f (e2 ) =  1 . Ces deux vecteurs n’étant pas colinéaires, ils forment une
                     0                   1
         base de l’image de f et                                     
                                                            1       −1
                                           Im(f ) = Vect  1  ;  1 
                                                                        0       1

3. (0.5 point(s).) L’application ne peut pas être injective puisque l’on va d’un espace de dimension 4
   à un espace de dimension 3. Elle n’est pas surjective puisque l’image n’est pas R3 . Elle n’est donc
   pas non plus bijective.
4. (1 point(s).)
     (a) Nous avons :
          — F ⊂ R3 par définition.
          — (0 ; 0 ; 0) ∈ F .
          — On montre, en rédigeant correctement que F est stable par combinaison linéaire.
         Donc F est bien un sous-espace vectoriel de R3 .

                                                           - 4 / 10 -
~~~

## Page 5

~~~text
     (b) (1.5 point(s).) Plusieurs méthodes (de la plus calculatoire à la moins calculatoire, ou de la
         moins bonne maîtrise du cours à la meilleure maîtrise) :
          — On cherche une base de F à partir de ses équations et on montre que chacune est combi-
              naison linéaire de
                                l’autre.
                                               
                                   1         −1
          — On constate que  1  et  1  sont dans F . Nous pouvons donc affirmer (par stabilité
                                   0          1
              de F ) que Im(f ) ⊂ F . Il reste donc à montrer l’inclusion réciproque. Pour cela, on peut
              chercher une base de F (comme au point précédent) et on montre que les vecteurs de
              cette base sont combinaisons linéaires de celle de Im(f ).
          — Toujours en partant de la constatation précédente (Im(f ) ⊂ F ), on remarque que la di-
            mension de F est égale au nombres d’inconnues moins le rang du système, c’est-à-dire
            3 − 1 = 2. D’où l’égalité sans faire un seul calcul de base.
5.
     (a) (1.5 point(s).) D’après le théorème de la base incomplète, on peut compléter la famille libre
         avec les vecteurs de la base canonique. On constate que les deux derniers
                                                                                   ne peuvent
                                                                                            pas      
                                                                              −1      −1        1      0
                                                                          −1   1   0   1 
         convenir (en même temps), mais les deux premiers conviennent :   1  ;  0  ;  0  ;  0 
                                                                                                  

                                                                               0       1        0      0
         est une famille libre :
                                    −λ1 − λ2 + λ3 = 0
                                 
                                 
                                    −λ1 + λ2 + λ4 = 0
                                 
                                                         ⇔ λ1 = λ2 = λ3 = λ4 = 0
                                              λ1 = 0
                                               λ2 = 0
                                 

                                                                                              
                                                                                       1       0
                                                                                    0   1 
     (b) (0.5 point(s).) Donc un supplémentaire du noyau est tout simplement Vect   0  ;  0  .
                                                                                               

                                                                                                  0        0
6.
     (a) (1 point(s).) De la même manière, comme dit dans la question précédente, la famille
                                                            
                                         −1      −1       1       0
                                     −1   1   0   1 
                                      1  ;  0  ;  0  ;  0 
                                                            

                                               0         1         0       0
         est libre. Elle forme donc une base de R4 , constituée d’une base de Ker(f ) et de H . Donc H et
         Ker(f ) sont bien supplémentaires.
     (b) (0.5+0.5 point(s).) Nous savons qu’une application linéaire est entièrement déterminée par
         l’image d’une base. Nous avons ici l’image de la base de H , donc l’application linéaire ϕ est
         entièrement déterminée (unique). On constate de plus que ces deux vecteurs images vérifient
         les équations de F = Im(f ). Donc ϕ est bien à valeurs dans Im(f ).
                                                                                                               
                                                                                                             −1
     (c) (0.5 point(s).) Soit u = (x ; y ; 0; 0) ∈ H , alors ϕ(u ) = x ϕ(1, 0, 0, 0) + y ϕ(0, 1, 0, 0) = x  1  +
                                                                                                              1
                             
              0           −x
         y   2  =    x + 2y 
              1          x+y

                                                   - 5 / 10 -
~~~

## Page 6

~~~text
       (d) (0.5 point(s).) L’image de la base de H étant une base de Im(f ), on en déduit que l’application
           est bijective (théorème de cours). (Ou alors on montre qu’elle est injective en calculant son
           noyau, et comme les espaces de départ et d’arrivée sont de dimension 2, c’est bijectif ).
  7. (0.5 point(s).) Trois réponses possibles
        — On vient de construire un isomorphisme entre H et Im(f ).
        — H est un supplémentaire au noyau, or Im(f ) est isomorphe à tout supplémentaire du noyau.
        — H et Im(f ) ont même dimension, ils sont donc supplémentaires.

                                                 Exos rejetés

Exercice 5 (Questions de cours : ( ? point(s).)). Voir pdf de Khaoula.

Exercice 6 (Espaces vetoriels : (5 point(s).)). Soit E un espace vectoriel, U , V , W trois sous-espaces de
E tels que
                                U ∩ V = {0}       et     (U + V ) ∩ W = {0}                              (1)
  1. Démontrer qu’en général, si E , F et G sont des espaces vectoriels, alors (E + F )∩G 6= E ∩G + F ∩G .
  2.
        (a) Montrer par l’absurde que V ∩ W = {0}.
       (b) Montrer que U ∩ (V + W ) = {0}.
  3. On rappelle un théorème de cours et sa démonstration :
       Propriété 1. Soit E un    et F et G deux sev de E . Alors F et G sont en somme directe si et
                             K-ev,
       seulement si F ∩ G =   0 E .
                                                           
       Démonstration 1. ⇐ : Supposons que F ∩ G =         0 E . Soit u ∈ F + G et montrons que u se
            décompose de manière unique en u = u 1 + u 2 avec u 1 ∈ F et u 2 ∈ G . Supposons que

                                              u = u 1 + u 2 = v1 + v2
                                                 |{z} |{z} |{z} |{z}
                                                   ∈F         ∈G               ∈F   ∈G
                                                                                                                
           On a alors u 1 − v1 = v2 − u 2 = w ∈ F ∩G . Or F ∩G étant réduit au vecteur nul, on a w =        0       E
                                                                                                                        ,
                      | {z } | {z }
                         ∈F        ∈G
           d’où u 1 = v1 et u 2 = v2 et l’écriture de u est unique.
       ⇒ : Supposons maintenant que F et G sont en somme directe et montrons que leur intersection
          est réduite au vecteur nul. Soit u ∈ F ∩ G . On a tout simplement
                                                              
                                          u = |{z}
                                               u + 0 E = 0 E + |{z} u
                                                   | {z } | {z }
                                                  ∈F                                 ∈G
                                                          ∈G                   ∈F
                                                                   
           Par unicité de la décomposition, on a u =          0        E
                                                                           .

                                                                                                                    

       En adaptant cette démonstration, montrer que (1) est équivalent à

                              ∀x ∈ U + V + W , ∃!(u , v, w ) ∈ U × V × W , x = u + v + w                        (2)

                                                        
  1. (1 point(s).) C’est évident, c’était juste pour que vous n’écriviez pas d’absurdités : Soit E = Vect ((1, 0)),
     F = Vect ((0, 1)), G = Vect ((1, 2)) alors E + F = R2 donc (E + F ) ∩ G = G et E ∩ G = {0} = F ∩ G , donc
     E ∩ G + F ∩ G = {0} = 6 R2 .

                                                   - 6 / 10 -
~~~

## Page 7

~~~text
  2.
       (a) (1 point(s).) Supposons que l’intersection est non vide, et soit x ∈ V ∩ W . Alors x ∈ V ⊂ U + V
           (car x = 0 + x ), ainsi x ∈ (U + V ) ∩ W . Ce qui est contraire à l’hypothèse.
       (b) (1 point(s).) De même, soit x ∈ U ∩(V +W ), alors x ∈ U et x ∈ V +W , donc x = v +w avec v ∈ V
           et w ∈ W . Finalement, w = x − v ∈ U + V (car x ∈ U et v ∈ V ). Or w ∈ W . D’où l’intersection
           (U + V ) ∩ W non vide, ce qui est contraire à l’hypothèse.
  3.
       ⇒ (1 point(s).) S’il existe deux écriture x = u 1 + v1 + w1 = u 2 + v2 + w2 , alors (u 1 + v1 ) − (u 2 + v2 ) =
         w2 − w1 ∈ {0}. Donc w1 = w2 . De même, (v1 + w1 ) − (v2 + w2 ) = u 2 − u 1 ∈ {0}. Donc v1 = v2 .
         Finalement, u 1 = u 2 .
       ⇐ (1 point(s).) Soit x ∈ U ∩ V , alors x = x + 0 + 0 = 0 + x + 0. Donc par unicité de l’écriture, x = 0.
         Enfin, soit x ∈ (U + V ) ∩ W , alors x = u + v + 0 = 0 + 0 + w . Par unicité de l’écriture, on a w = 0,
         donc x = 0.

Exercice 7. (3 point(s).) Soit E = {(u n )n ∈ RN / (u n )n converge }. On admet que l’ensemble des suites
réelles (RN ) est un espace vectoriel sur R (munit des lois d’addition de suites et de multiplications par
un scalaire usuelles)..
  1. Montrer que E est un espace vectoriel.
  2.
       (a) Montrer que l’ensemble des suites constante (S C ) est un sous-espace de E .
       (b) Montrer que l’ensemble des suites convergentes vers 0 (C V0 ) est un sous-espace de E .
  3. Montrer que E = C S ⊕ C V0 .
                                                        
  1. (0.5 point(s).)
       — E ⊂ RN .
       — La suite nulle converge.
       — Toute C.L de suite convergente est une suite convergente.
  2. (0.5 point(s).)
       (a)
             — S C ⊂ E car une suite constante converge.
             — La suite nulle est constante.
             — Toute C.L de suite constante est constante.
       (b) (0.5 point(s).)
             — C V0 ⊂ E car une suite qui converge vers 0 converge.
             — La suite nulle converge vers 0.
             — Toute C.L de suite onvergente vers 0 est convergente.
  3.
       — (0.5 point(s).) Soit (u n )n ∈ S C ∩ C V0 , alors (u n ) est une suite constante qui converge vers 0.
         C’est donc la suite nulle.
       — (1 point(s).) Soit (u n )n ∈ E , et notons l ∈ R sa limite. Nous avons alors (vn )n , définie par vn =
         u n −l qui est une suite convergente vers 0. Donc (vn ) ∈ C V0 . Et la suite (wn )n définie par wn = l
         est une suite constante (∈ S C ). Ainsi

                                                    u = v + w ∈ C v0 + S C

                                                      - 7 / 10 -
~~~

## Page 8

~~~text
       D’où E = C V0 ⊕ S C .

Exercice 8 (Espaces vectoriels et Morphismes : (11.5 point(s).)). Soit f1 l’application définie par :
                                     
                                                R4 −→ R
                                f1 :
                                       x ; y ;z ;t  7−→ 5x − 2y + z + 4t

et f l’application définie par :
     
                 R4 −→ R5
 f :                                                                                                        
        x ; y ;z ;t  7−→ f1 (x , y , z , t ) ; 5x + y + 2z + 3t ; x + 2y + z ; 4x − y + z + 3t ; 3y + z − t

  1. Montrer que f1 est une application linéaire.
On admet par la suite que f est une application linéaire.
  2.
        (a) Déterminer une base du noyau de f .
       (b) Déterminer les dimension du noyau et de l’image de f .
        (c) Déterminer l’image de f .
  3. L’application f est-elle injective ? surjective ? bijective ?
              
  4. Soit F = (a ; b ; c ; d ; e ) ∈ R5 / a = 5c − 4e et b = 5c − 3e et d = 4c − 3e
        (a) Montrer que F est un espace vectoriel.
       (b) Montrer que Im(f ) = F .
  5.
        (a) Compléter la base trouvée en 2.(a) en une base de R4 .
       (b) En déduire un supplémentaire du noyau.
  6. Soit H = Vect ((0; 0; 1; 0); (0; 0; 0; 1)).
        (a) Montrer que R4 = Ker(f ) ⊕ H .
       (b) Montrer que ϕ((0; 0; 1; 0)) = (5; 0; −3; 3; −5) et ϕ((0; 0; 0; 1)) = (0; 5; 4; 1; 5) suffit à définir/déterminer
           une application linéaire ϕ de H dans Im(f ).
        (c) Donner une définition de ϕ avec des équations. / ou car pas fait en TD / Montrer que
                                 
                                             H −→ Im(f )
                              ϕ:
                                   (0; 0; z ; t ) 7−→ (5z ; 5t ; 4t − 3z ; 3z + t ; 5t − 5z )

       (d) L’application ϕ est-elle injective ? surjective ? bijective ?
        (e) Montrer que Im(f ) est isomorphe à un supplémentaire de Ker(f ).
                                                         
  1. (1 point(s).) On montre aisément que f1 (u + λv ) = f (u ) + λf (v ).
  2.
                                                             
                                                                 x + 2y + z = 0
        (a) (1 point(s).) f x ; y ; z ; t = (0 ; 0 ; 0 ; 0 ; 0) ⇔                (après réduction du système).
                                                                  3y + z − t = 0
                                                         
                                          −2          −1
                                    1   0 
            Donc Ker(f ) = Vect    0  ;  1 . Cette famille est génératrice et comme elle est libre
                                                          

                                           3            1
            (vecteurs non colinéaires) c’est une base.

                                                       - 8 / 10 -
~~~

## Page 9

~~~text
     (b) (0.5 point(s).) Le noyau est donc de dimension 2. L’image est alors, d’après le théorème du
         rang, de dimension 4-2=2.
                                                                                       
     (c) (1 point(s).) Nous savons que Im(f ) = Vect f (e1 ); f (e2 ); f (e3 ); f (e4 ) . La dimension étant 2,
         il suffit 
                   doncde prendre   2 vecteurs
                                             non colinéaires dans cette famille pour avoir une base.
                     5                  −2
                    5                1 
                                         
                    1  et f (e2 ) =  2 . Ces deux vecteurs n’étant pas colinéaires, ils forment une
         f (e1 ) =                       
                    4                −1 
                     0                   3
         base de l’image de f et                                     
                                                             5       −2
                                                          5   1  
                                                                     
                                           Im(f ) = Vect 
                                                         
                                                            1  ;  2 
                                                                       
                                                          4   −1 
                                                              0       3

3. (0.5 point(s).) L’application ne peut pas être surjective puisque l’on va d’un espace de dimension
   4 à un espace de dimension 5. Elle n’est pas injective puisque le noyau n’est pas réduit au vecteur
   nul. Elle n’est donc pas non plus bijective.
4. (1 point(s).)
     (a) Nous avons :
          — F ⊂ R5 par définition.
          — (0 ; 0 ; 0 ; 0 ; 0) ∈ F .
          — On montre, en rédigeant correctement que f est stable par combinaison linéaire.
         Donc F est bien un sous-espace vectoriel de R5 .
     (b) (1.5 point(s).) Plusieurs méthodes (de la plus calculatoire à la moins calculatoire, ou de la
         moins bonne maîtrise du cours à la meilleure maîtrise) :
          — On cherche une base de F à partir de ses équations et on montre que chacune est combi-
            naison linéaire de l’autre.
                                            
                                 5         −2
                              5   1 
                                            
          — On constate que    1  et  2  sont dans F . Nous pouvons donc affirmer (par stabilité
                                             
                              4   −1 
                                 0          3
            de F ) que Im(f ) ⊂ F . Il reste donc à montrer l’inclusion réciproque. Pour cela, on peut
            chercher une base de F (comme au point précédent) et on montre que les vecteurs de
            cette base sont combinaisons linéaires de celle de Im(f ).
          — Toujours en partant de la constatation précédente (Im(f ) ⊂ F ), on remarque que la di-
            mension de F est égale au nombres d’inconnues moins le rang du système, c’est-à-dire
            5 − 3 = 2. D’où l’égalité sans faire un seul calcul de base.
5.
     (a) (1.5 point(s).) D’après le théorème de la base incomplète, on peut compléter la famille libre      
                                                                                                      −2     −1
                                                                                                  1   0 
         avec les vecteurs de la base canonique. On constate que les deux premiers conviennent : 
                                                                                                  0  ;  1  ;
                                                                                                             

                                                                                                       3     1


                                                 - 9 / 10 -
~~~

## Page 10

~~~text
         est une famille libre :

                                       −2λ1 − λ2 + λ3    =       0
                                     
                                     
                                              λ1 + λ4    =       0
                                     
                                                                   ⇔ λ1 = λ2 = λ3 = λ4 = 0
                                                  λ2    =       0
                                            3λ2 + λ3     =
                                     
                                                                 0

         Il semblerait que n’importe quelle paire de vecteurs canoniques fonctionne.
                                                                                            
                                                                                      1       0
                                                                                   0   1 
                                                                                    0  ;  0  .
     (b) (0.5 point(s).) Donc un supplémentaire du noyau est tout simplement Vect           

                                                                                      0       0
6.
     (a) (1 point(s).) De la même manière, comme dit dans la question précédente, la famille
                                                            
                                         −2      −1       0       0
                                      1   0   0   0 
                                      0  ;  1  ;  1  ;  0 
                                                            

                                                3            1         0      1

         est libre. Elle forme donc une base de R4 , constituée d’une base de Ker(f ) et de H . Donc H et
         Ker(f ) sont donc bien supplémentaires.
     (b) (0.5+0.5 point(s).) Nous savons qu’une application linéaire est entièrement déterminée par
         l’image d’une base. Nous avons ici l’image de la base de H , donc l’application linéaire ϕ est
         entièrement déterminée (unique). On constate de plus que ces deux vecteurs images vérifient
         les équations de F = Im(f ). Donc ϕ est bien à valeur dans Im(f ).
                                                                                                               
                                                                                                              5
                                                                                                            0 
                                                                                                               
     (c) (0.5 point(s).) Soit u = (0; 0; z ; t ) ∈ H , alors ϕ(u ) = z ϕ(0, 0, 1, 0) + t ϕ(0, 0, 0, 1) = z 
                                                                                                            −3 +
                                                                                                                
                                                                                                            3 
                                                                                                         −5
                                  
            0         5z
           5        5t   
                         
           4  =  4t − 3z 
         t               
           1   3z + t 
               5           5t − 5z
     (d) (0.5 point(s).) L’image de la base de H étant une base de Im(f ), on en déduit que l’application
         est bijective (théorème de cours). (Ou alors on montre qu’elle est injective en calculant son
         noyau, et comme les espaces de départ et d’arrivée sont de dimension 2, c’est bijectif ).




                                                    - 10 / 10 -
~~~
