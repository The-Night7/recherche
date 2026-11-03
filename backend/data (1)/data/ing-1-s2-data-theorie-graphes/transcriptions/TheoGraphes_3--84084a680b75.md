# TheoGraphes_3.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1FtppjITW2gXfiK4WFkAJC4W0zKcXaGqx) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Théorie des graphes

Maria Malek, Romain Dujol

      CY Tech – ING1-MA




   Maria Malek, Romain Dujol   1
~~~

## Page 2

~~~text
Coloration de graphes



  Coloration d’un graphe

  Polynôme chromatique d’un graphe

  Colorations des arêtes

  Graphes extrêmaux




                      Maria Malek, Romain Dujol   60
~~~

## Page 3

~~~text
Coloration d’un graphe


  Coloration d’un graphe
     Définition
     Recherche de coloration
     Calcul du nombre chromatique

  Polynôme chromatique d’un graphe

  Colorations des arêtes

  Graphes extrêmaux




                      Maria Malek, Romain Dujol   61
~~~

## Page 4

~~~text
Coloration

  Définition (Coloration (des sommets) de G = (V, E))
  Application c : V 7→ C (C ensemble de couleurs)
  Coloration c propre :
           ∀(v, v 0 ) ∈ V 2 , v et v 0 adjacents ⇒ c(v) 6= c(v 0 )

  Définition (Graphe G = (V, E) k-colorable)
  c k-coloration ⇐⇒ card c(V) = k
  G k-colorable ⇐⇒ ∃ k-coloration propre de G

  Définition (Nombre chromatique de G = (V, E))
  χ(G) = min{card c(V), c coloration propre de G}
  Coloration propre optimale ≡ χ(G)-coloration propre

  Applications
  Traduire des relations d’incompatibilité entre les sommets

                        Maria Malek, Romain Dujol                    62
~~~

## Page 5

~~~text
Coloration

  Exemple
   I Sommets : produits chimiques
   I Arêtes : entre deux produits non transportables ensembe
   ⇒ Coloration propre : sous-ensembles de produits
     transportables ensemble
   ⇒ Nombre chromatique : nombre minimal de transports
     simultanés
                    H
                                E
             F

                                        B
                        A
                                                 C

                            G            D



                     Maria Malek, Romain Dujol            63
~~~

## Page 6

~~~text
Coloration

  Exemple
   I Sommets : produits chimiques
   I Arêtes : entre deux produits non transportables ensembe
   ⇒ Coloration propre : sous-ensembles de produits
     transportables ensemble
   ⇒ Nombre chromatique : nombre minimal de transports
     simultanés
                    H
                                E
              F

                                        B
                        A
                                                 C

                            G            D



                     Maria Malek, Romain Dujol            63
~~~

## Page 7

~~~text
Recherche de coloration optimale
  Première solution : recherche exhaustive
   I Recenser toutes les colorations propres
   I Trouver celle dont le nombre de couleurs est minimale
  =⇒ Complexité exponentielle
  =⇒ Beaucoup trop coûteux, donc inutilisable

  Deuxième solution : algorithme glouton
  Tant qu’il reste des sommets non coloriés,
   1. colorer un sommet non coloré de plus haut degré avec
      une nouvelle couleur ;
   2. colorer itérativement, par degré décroissant, tous les
      sommets non colorés possibles en conservant une
      coloration propre.
  =⇒ Algorithme de Welsh et Powell

  Attention
  La convergence vers une coloration optimale n’est pas
  assurée.
                      Maria Malek, Romain Dujol                64
~~~

## Page 8

~~~text
Recherche de coloration optimale

  Exemple
    v   E A B H D F                     G   C
   d(v) 5        4             3            2
   I Couleur n 1 : E, G puis C
              o

   I Couleur no 2 : A puis D
   I Couleur no 3 : B puis H
   I Couleur no 4 : F

                        H
                                    E
               F

                                            B
                            A
                                                    C

                                G           D



                        Maria Malek, Romain Dujol       65
~~~

## Page 9

~~~text
Nombre chromatique d’un graphe



  Propriété (Majorant de χ(G))
  Soit G = (V, E) un graphe et ∆ = max{d(v), v ∈ V}.
  Alors χ(G) ≤ ∆ + 1.

  Démonstration.
  Soit v le dernier sommet coloré par l’algorithme glouton.
  Alors v est adjacent à toutes les couleurs précédentes (il y en
  a au plus d(v)) : donc χ(G) ≤ d(v) + 1 ≤ ∆ + 1.

  Théorème (Théorème des quatre couleurs, 1976)
  Si G est planaire, alors χ(G) ≤ 4.




                       Maria Malek, Romain Dujol                66
~~~

## Page 10

~~~text
Nombre chromatique d’un graphe

  Propriété (Nombre chromatique d’un graphe
  complet)
  χ(Kn ) = n

  Démonstration.
   I ∆ = n − 1 ⇒ χ(Kn ) ≤ n.
   I Tous les sommets voisins deux à deux ⇒ χ(Kn ) ≥ n

  Propriété (Croissance de χ)
  Si G0 est un sous-graphe de G, alors χ(G0 ) ≤ χ(G).

  Corollaire (Minoration de χ(G))
  Si G contient un sous-graphe complet à p sommets, χ(G) ≥ p.

  Démonstration.
  Comme Kp est un sous-graphe de G, χ(G) ≥ χ(Kp ) = p.


                       Maria Malek, Romain Dujol           67
~~~

## Page 11

~~~text
Polynôme chromatique d’un graphe



  Coloration d’un graphe

  Polynôme chromatique d’un graphe
     Contraction d’une arête d’un graphe
     Polynôme chromatique

  Colorations des arêtes

  Graphes extrêmaux




                      Maria Malek, Romain Dujol   68
~~~

## Page 12

~~~text
Contraction d’une arête d’un graphe


  Définition (Contraction d’une arête de G = (V, E))
  Soit e ∈ E une arête d’extrêmités v1 et v2 .
  On définit G.e = (V 0 , E0 ) avec :
   I V 0 = V\{v1 , v2 } ∪ {v ∗ }
   I E0 = E\{f ∈ E, v1 ou v2 extrêmité de f }
            ∪ {vv ∗ , v ∈ V adjacent à v1 ou v2 }

  Autrement dit. . .
   I on remplace les extrêmités v1 et v2 de e par un sommet
     commun v ∗ ;
   I on remplace les arêtes d’extrêmité v1 ou v2 par des arêtes
     d’extrêmité v ∗ .




                        Maria Malek, Romain Dujol            69
~~~

## Page 13

~~~text
Contraction d’une arête d’un graphe



  Exemple                     e2
                                                    e6
              e1                        v3     e5
                              e3
  G = v1            v2
                                        e4          v4



  G.e2 = v1        v∗              v4




                   Maria Malek, Romain Dujol             70
~~~

## Page 14

~~~text
Polynôme chromatique d’un graphe
  Théorème (Polynôme chromatique de G = (V, E)
  simple)
  ∃!P ∈ Z[X], deg P = card V, ∀k ∈ J1, card VK ,

              P(k) = card{k-colorations propres de G}

  P est le polynôme chromatique de G

  Démonstration.
  Par récurrence forte sur t(G) = card V + card E :
   I card E = 0 ⇒ P = X card V
   I card E > 0 : soit e ∈ E.
        I t(G − e) < t(G) ⇒ Q polynôme chromatique de G − e
        I t(G.e) < t(G) ⇒ R polynôme chromatique de G.e
      ⇒ P = Q−R

  Propriété (Polynômes chromatiques particuliers)
   I Arbre à n sommets : P = X(X − 1)n−1 .
   I Carré (cycle de long. 4) : P = X(X − 1)3 − X(X − 1)(X − 2)
                         Maria Malek, Romain Dujol                71
~~~

## Page 15

~~~text
Colorations des arêtes



  Coloration d’un graphe

  Polynôme chromatique d’un graphe

  Colorations des arêtes

  Graphes extrêmaux




                      Maria Malek, Romain Dujol   72
~~~

## Page 16

~~~text
Coloration des arêtes
  Définition (Coloration des arêtes de G = (V, E))
  Application c1 : E 7→ C (C ensemble de couleurs)
  Coloration des arêtes c1 propre :
  ∀(e, e0 ) ∈ E2 , e et e0 ont une extrémité commune ⇒ c1 (e) 6= c1 (e0 )
  Définition (Graphe G = (V, E) colorable pour les
  arêtes)
  c1 k-coloration pour les arêtes ⇐⇒ card c1 (E) = k
  G k-colorable pour les arêtes
       ⇐⇒ ∃ k-coloration pour les arêtes propre de G
  Définition (Indice chromatique de G = (V, E))
  χ1 (G) = min{card c1 (E), c1 coloration propre des arêtes de G}
  Coloration des arêtes propre optimale
      ≡ χ1 (G)-coloration des arêtes propre

  Applications
  Planification d’emplois du temps, organisation de tournois, . . .
                         Maria Malek, Romain Dujol                    73
~~~

## Page 17

~~~text
Coloration des arêtes

  Propriété
  Soit G = (V, E) un graphe et ∆ = max{d(v), v ∈ V}.
  Alors χ1 (G) ≥ ∆

  Démonstration.
  Si d(v) = ∆, alors il faut au moins ∆ couleurs pour les arêtes
  incidentes en v.

  Théorème (König, 1916)
  Soit G = (V, E) un graphe biparti et ∆ = max{d(v), v ∈ V}.
  Alors χ1 (G) = ∆

  Théorème (Vizing, 1964)
  Soit G = (V, E) un graphe simple et ∆ = max{d(v), v ∈ V}.
  Alors χ1 (G) ≤ ∆ + 1
  Remarque        G simple =⇒ χ1 (G) ∈ {∆, ∆ + 1}


                       Maria Malek, Romain Dujol                   74
~~~

## Page 18

~~~text
Graphes extrêmaux



  Coloration d’un graphe

  Polynôme chromatique d’un graphe

  Colorations des arêtes

  Graphes extrêmaux




                      Maria Malek, Romain Dujol   75
~~~

## Page 19

~~~text
Graphes extrêmaux

  Définition (Graphe extrêmal)
  Soit P(G) un prédicat sur l’ensemble
                                   ( des graphes.
                                    ¬P(G)
  G = (V, E) extrêmal pour P ⇐⇒
                                    ∀e ∈
                                       / E, P(G + e)

  Théorème (Mantel, 1907)
  Soit G = (V, E) un graphe simple sans sous-graphe de type K3 .
                  (card V)2
  Alors card E ≤            .
                      4
  Théorème (Turán, 1941)
  Soit G = (V, E) un graphe simple sans sous-graphe de type
  Kr+1 .
                            (card V)2
                       
                      1
  Alors card E ≤ 1 −      ·           .
                      r         2


                      Maria Malek, Romain Dujol               76
~~~
