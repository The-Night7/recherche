# un corrigé de l_exercice 4 du TD2.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1GDVsKNILXgQqpBY6AZ-SgM5reGAcY-la) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
CY TECH – ING1 GM                                                                           TD 2 : Équations Différentielles


Corrigé Détaillé - Exercice 4 : Explosion en temps fini
  Énoncé : On considère le problème de Cauchy non linéaire de Riccati :
                                             (
                                              u′ (t) = u(t)2 + t2
                                     (P C) :
                                              u(0) = 0

  La fonction f (t, u) = u2 + t2 étant de classe C ∞ sur R2 (donc localement lipschitzienne par rapport à u),
  le théorème de Cauchy-Lipschitz non linéaire garantit l’existence d’une unique solution maximale u,
  définie sur un intervalle ouvert J =] − a, b[.


1. Linéarisation et positivité stricte de z
                                       Z t        
   Pour tout t ∈ J, on pose z(t) = exp −    u(s) ds .
                                                       0
    Régularité et garantie de non-annulation Rt     : Puisque u est de classe C 1 sur J, le théorème fondamental
de l’analyse nous assure que la fonction t 7→ 0 u(s) ds est de classe C 2 . Par composition, z est de classe C 2 sur
J. Surtout, la fonction exponentielle ne s’annulant jamais sur R, on a rigoureusement z(t) > 0 pour tout
                                                       z ′ (t)
t ∈ J. Cela garantit que la relation inverse u(t) = −          est toujours licite (sans division par zéro) sur tout
                                                       z(t)
l’intervalle J.
    Équation différentielle vérifiée :
                                                    Z t             
                                  ′
                                z (t) = −u(t) · exp −         u(s) ds = −u(t)z(t)
                                                                   0
En dérivant une seconde fois :
             z ′′ (t) = −u′ (t)z(t) − u(t)z ′ (t) = −(u2 + t2 )z − u(−uz) = −u2 z − t2 z + u2 z = −t2 z(t)
La fonction z vérifie l’équation différentielle linéaire : (E) : z ′′ (t) + t2 z(t) = 0.
Conditions initiales : l’intégrale étant nulle en t = 0, z(0) = e0 = 1. Comme u(0) = 0, z ′ (0) = 0.

2. Recherche de la solution formelle : Argument d’analyticité
  Justification théorique : L’équation (E) est linéaire et homogène. Son coefficient t 7→ t2 est une fonction
  polynomiale, donc analytique (développable en série entière avec un rayon infini). D’après le théorème de
  Cauchy linéaire pour les séries entières, la solution globale du problème de Cauchy est analytique
                                                                            +∞
                                                                            X
  sur R et peut donc être cherchée sous la forme d’une série entière S(t) =      an tn de rayon R = +∞.
                                                                                              n=0

   En injectant S et S ′′ dans (E) et en réindexant (posons k = n − 2 dans la première somme) :
                                                 +∞
                                                 X
                             2a2 + 6a3 t +             [(m + 4)(m + 3)am+4 + am ] tm+2 = 0
                                             m=0

Par unicité du développement en série entière (valide autour de 0), on identifie : a2 = a3 = 0, et
             am
am+4 = − (m+4)(m+3) . Avec a0 = 1 et a1 = 0, seuls les indices multiples de 4 subsistent. Pour m = 4k :
                                   +∞                                    k
                                   X             t4k                     Y
                          S(t) =         (−1)k             avec   bk =         4j(4j − 1)    (et b0 = 1)
                                                 bk                      j=1
                                   k=0


3. Validation du rayon de convergence infini
                                                                                      4k
   Appliquons le critère de d’Alembert sur le terme général uk (t) = tbk pour t ̸= 0 :
                                         uk+1 (t)          t4
                                                  =                  −−−−−→ 0
                                          uk (t)    (4k + 4)(4k + 3) k→+∞
La limite étant nulle (donc < 1), la convergence est absolue pour tout t ∈ R. Le rayon de convergence est bien
R = +∞, justifiant pleinement notre cadre analytique.


                                                                  1
~~~

## Page 2

~~~text
CY TECH – ING1 GM                                                               TD 2 : Équations Différentielles


4. Le cœur du problème : Existence de la première racine τ
   La série étant délicate à évaluer à l’infini, prouvons par l’absurde l’existence d’une racine : Supposons que
S(t) > 0 pour tout t ≥ 0.
   — Puisque S ′′ (t) = −t2 S(t) ≤ 0, la fonction S ′ est strictement décroissante sur R+ .
   — Or S ′ (0) = 0, donc pour t = 1, on a S ′ (1) = −α < 0.
   — Pour t ≥ 1, la décroissance de S ′ impose S ′ (t) ≤ −α. En intégrant :

                                            S(t) ≤ S(1) − α(t − 1) −−−−→ −∞
                                                                     t→+∞

   — Contradiction avec l’hypothèse S(t) > 0.
La fonction S s’annule donc au moins une fois sur R∗+ . L’image réciproque de {0} par la fonction continue S
étant fermée, elle admet un minimum. Soit τ le plus petit zéro strictement positif de S.

5. Majoration par le CSSA et localisation (τ > 2)
                                P+∞          k
   Posons x = t4 et f (x) = 1 + k=1 (−1)k xbk . Sur [0, 16], la suite des termes est positive, décroissante et
tend vers 0. Le Critère Spécial des Séries Alternées nous autorise à encadrer la somme par ses sommes
partielles.
   a) Décroissance de f : Majorons f ′ (x) en tronquant au terme positif (indice k = 2) :
                                        1   2      1  32    7  4     3
                          f ′ (x) ≤ −     +    x≤− +     =− +    =−    <0
                                        12 672    12 672   84 84    84
Cette majoration grossière mais valide prouve que f est strictement décroissante sur [0, 16].
   b) Signe strict sur [0, 16] : Minorons le minimum f (16) en tronquant au terme négatif (indice k = 3) :
                                         16 256   4096   1  8   32    1
                          f (16) ≥ 1 −     +    −      =− +   −    =     >0
                                         12 672 88704    3 21 693    693
Ainsi, f (x) > 0 sur [0, 16], donc S(t) > 0 sur [0, 2]. Ce qui assure τ > 2.

6. Synthèse : Symétrie, Explosion et Intervalle Maximal J
  Conclusion globale :
      1. Symétrie et Parité : L’équation u′ = u2 +t2 est invariante par le changement (t, u) → (−t, −u). Si
         u(t) est solution, v(t) = −u(−t) l’est aussi. Par unicité, v = u, donc u est impaire. Son intervalle
         d’existence est nécessairement symétrique : J =]−b, b[. De fait, z (et donc S) est une fonction paire.
         Le premier zéro négatif de S est exactement −τ .
      2. Coïncidence et Explosion : Sur J, par unicité globale linéaire, l’exponentielle z coïncide avec S.
                                          ′
         Pour tout t ∈ [0, b[, u(t) = − SS(t)
                                            (t)
                                                . Lorsque t → τ − , on a S(t) → 0+ . Surtout, la décroissance stricte
         de S garantit que S ′ (τ ) < 0, donc le numérateur −S ′ (τ ) est strictement positif.

                                                               −S ′ (τ )
                                                 lim− u(t) =             = +∞
                                                t→τ             0+

      3. Intervalle Maximal : Cette explosion vers l’infini positif bloque tout prolongement au-delà de τ .
         L’imparité de u implique une explosion symétrique vers −∞ en −τ . L’intervalle maximal est donc
         parfaitement scellé : J =] − τ, τ [ avec τ > 2.




                                                          2
~~~
