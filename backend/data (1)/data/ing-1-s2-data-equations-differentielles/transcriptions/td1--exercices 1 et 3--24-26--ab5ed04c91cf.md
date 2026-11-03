# td1--exercices 1 et 3--24-26.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1HN_-iOJ2AEzfr5Z_37Mid9OyF0LfLqoW) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                        Un Corrigé des Exercices 1 & 3
                                                Yalçin Aktar

                                                   01.02.26



  Rappel Méthode (Notations du cours) :
  Pour résoudre une équation linéaire y ′ (t) + a(t)y(t) = b(t) avec t0 = 0 :
                                                          Z t         
     1. On calcule le facteur intégrant : µ(t) = exp           a(s) ds .
                                                                    0
                                              K
      2. La solution homogène est : vh (t) =      .
                                             µ(t)
                                                              Z t
                                                      1
      3. La solution particulière est : vp (t) =                    µ(s)b(s) ds.
                                                     µ(t)      0
      4. Solution générale : v(t) = vh (t) + vp (t).




Exercice 1 : Oscillateur et Masse Variable
1. Cas de la masse constante (m)
   Équation : mv ′ + kv = λ cos t ⇐⇒ v ′ + m
                                           k   λ
                                             v=m                    k
                                                 cos t. Ici, a(t) = m                       λ
                                                                      (constante) et b(t) = m cos t.

Step 1 : Calcul de µ(t)

                                                                             !
                                                                         k t
                                         Z t                       
                                             k                                     k
                            µ(t) = exp         ds         = exp           s     = emt
                                           0 m                           m 0

Step 2 : Solution homogène vh

                                                 K     K       k
                                     vh (t) =        = k = Ke− m t
                                                µ(t)  em t


Step 3 : Solution particulière vp
   On applique la formule intégrale :
                                     Z t                    Z t
                                 1                      k
                                                       −m t       k  λ
                       vp (t) =          µ(s)b(s)ds = e         e m s cos s ds
                                µ(t) 0                       0       m

Note : Pour le calcul effectif de cette intégrale, on peut procéder par double IPP ou Partie réelle d’une
intégrale complexe ou identification (forme A cos t + B sin t). Par identification (vu en TD), on trouve :

                                                  λ
                                    vp (t) =              (k cos t + m sin t)
                                               k 2 + m2




                                                          1
~~~

## Page 2

~~~text
CY TECH – ING1 GM                                                                 Corrigé TD1 - Groupe 1 et Groupe 3


2. Cas de la masse variable : m(t) = m0 (1 − t) sur I = [0, 1[
   L’équation devient : m0 (1 − t)v ′ + kv = λ cos t. Forme normalisée :

                                              k             λ
                                   v′ +              v=            cos t
                                          m0 (1 − t)    m0 (1 − t)
                                          | {z }        |     {z      }
                                                   a(t)                           b(t)


Step 1 : Calcul de µ(t)

                                                          Z t                  
                                                                       k
                                     µ(t) = exp                               ds
                                                                 0 m0 (1 − s)
              1
Primitive de 1−s est − ln(1 − s). Donc :
              Z t                              t
                      k             k                k                
                                                                              − k
                                                                                  
                             ds = −    ln(1 − s) = −    ln(1 − t) = ln (1 − t) m0
                0 m0 (1 − s)        m0           0   m0

D’où le facteur intégrant :
                                                   − k             − k
                                                     
                              µ(t) = exp ln (1 − t) m0    = (1 − t) m0

Step 2 : Solution homogène vh

                                           K         K                  k
                               vh (t) =        =          k = K(1 − t) m0
                                          µ(t)          −
                                                 (1 − t) m0

Step 3 : Solution particulière vp
   On applique la formule avec µ(t) :
                                                                 Z t
                                                 1
                                       vp (t) =                         µ(s)b(s) ds
                                                µ(t)              0
                                                   Z t
                                               k
                                                                      − mk         λ
                         vp (t) = (1 − t)     m0       (1 − s)              0 ·           cos s ds
                                                     0 |   {z                } m0 (1 − s)
                                                                 µ(s)           |    {z       }
                                                                                         b(s)

                                                          − mk                                     −(1+ mk )
On simplifie le terme dans l’intégrale : (1 − s)             0    · (1 − s)−1 = (1 − s)                     0   .
                                          k                             k   Rt              −(1+ mk )
                      v(t) = K(1 − t) m0 + mλ0 (1 − t) m0                       0 (1 − s)
                                                                                                  0     cos s ds




                                                                 2
~~~

## Page 3

~~~text
CY TECH – ING1 GM                                               Corrigé TD1 - Groupe 1 et Groupe 3


Exercice 3 : Équation Logistique (x′ = ax − bx2 )
Question 1 : Interprétation des constantes
   L’équation modélise une dynamique de population :
   — a > 0 : Taux de croissance intrinsèque (naissances - morts naturelles). Sans limitation, la
      population croîtrait exponentiellement (x′ ≈ ax).
   — b > 0 : Taux de limitation (compétition pour les ressources, prédation). Le terme −bx2 freine
      la croissance quand x devient grand.

Question 2 : Résolution par Variables Séparées
   On cherche x(t) tel que dx
                           dt = x(a − bx). On sépare les variables pour x ∈
                                                                          / {0, a/b} :

                                                  dx
                                                         = dt
                                               x(a − bx)
                                                                1
Décomposition en éléments simples : On cherche A, B tels que x(a−bx) =A    B
                                                                      x + a−bx .
                                       (
                                        x = 0 → 1 = Aa =⇒ A = 1/a
                 1 = A(a − bx) + Bx =⇒
                                        x = a/b → 1 = B(a/b) =⇒ B = b/a

L’intégrale devient :                    Z                         Z
                                     1         1    b
                                                 +            dx =       dt
                                     a         x a − bx
   ! Attention : Ne pas écrire + ln |a − bx| ! La dérivée de ln(u) est u′ /u. Ici u(x) = a − bx, donc
u′ = −b. La primitive deb
                      a−bx est donc − ln |a − bx| (à cause du signe − dans la dérivée interne).

                        1                                        x
                          (ln |x| − ln |a − bx|) = t + K =⇒ ln        = at + aK
                        a                                      a − bx
En passant à l’exponentielle et en isolant x :
                                              a
                                    x(t) = b+Ce −at       (avec C ∈ R)


Question 3 : Résolution type Bernoulli
   L’équation x′ − ax + bx2 = 0 est une équation de Bernoulli (r = 2).
                                                          1
    1. Changement de variable : On pose z(t) = x(t)1−2 = x(t) . Alors x = 1/z et x′ = −z ′ /z 2 .
    2. Équation en z :
                                     z′    1    1
                                    − 2 − a + b 2 = 0 ⇐⇒ z ′ + az = b
                                     z     z   z
    3. Résolution linéaire :
       — Facteur intégrant µ(t) = eat . Solution homogène zh = Ke−at .
       — Solution particulière constante : zp = b/a.
                                                             b
                                              z(t) = Ke−at +
                                                             a
    4. Retour à x :
                                             1        1           a
                                   x(t) =        =        b
                                                            =     −at
                                            z(t)   Ke−at +a   aKe     +b




                                                      3
~~~

## Page 4

~~~text
CY TECH – ING1 GM                                             Corrigé TD1 - Groupe 1 et Groupe 3


Question 4 : Comportement Asymptotique
                                                                        a
    On suppose une condition initiale x0 > 0. La solution est x(t) = b+Ce −at . Puisque a > 0, on a

limt→+∞ e−at = 0.
                                                    a      a
                                       lim x(t) =       =
                                      t→+∞        b+0      b
Conclusion : Quelle que soit la population initiale (positive), elle tend vers la capacité d’accueil limite
du milieu Klim = a/b.

Question 5 : Équilibres et Stabilité
   Les points d’équilibre sont les solutions stationnaires (x(t) = Cte), c’est-à-dire les racines de f (x) =
ax − bx2 = 0.
                                                                           a
                             x(a − bx) = 0 ⇐⇒ xeq1 = 0 ou xeq2 =
                                                                           b
   Étude de la stabilité : On étudie le signe de la dérivée f ′ (x) aux points d’équilibre (Critère de
stabilité linéaire). Ici f ′ (x) = a − 2bx.
    1. En xeq1 = 0 :
                                                  f ′ (0) = a > 0
       La dérivée est positive, donc une petite perturbation va s’amplifier (la solution s’éloigne de 0).
                                     L’équilibre x = 0 est INSTABLE.
    2. En xeq2 = ab :
                                                     a
                                  f ′ (a/b) = a − 2b( ) = a − 2a = −a < 0
                                                     b
       La dérivée est négative, donc une petite perturbation va s’amortir (la solution revient vers
       l’équilibre).
                        L’équilibre x = a/b est STABLE (Asymptotiquement).




                                                     4
~~~
