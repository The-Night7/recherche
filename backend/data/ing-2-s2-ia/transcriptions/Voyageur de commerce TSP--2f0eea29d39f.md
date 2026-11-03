# Voyageur de commerce TSP.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Xh99l_7iV8tUcQneLOPj4nNOACXUO52W) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
    Voyageur de
     commerce
        TSP
Implémentation de l’algorithme de
         recuit simulé
~~~

## Page 2

~~~text
Rappels
1.   TSP: recherche du chemin hamiltonien de plus petit coût dans un
     graphe valué orienté (TSP non symétrique) ou non orienté (TSP
     symétrique)
2.   TSP: problème NP-complet, pas de solution optimale polynomiale
     connue. Algorithme naïf exponentiel: (n-1)! pour n sommets
3.   Algorithme de Little = utilisation de la technique SEP (Séparation
     Évaluation Progressive, B.Roy 1964-65): optimal et utilisable pour plus de
     1000 sommets, mais reste exponentiel
4.   Algorithme de Recuit Simulé: méthode approchée, polynomiale mais non
     optimale.
~~~

## Page 3

~~~text
Rappels: Complexité
P: complexité polynomiale: Il existe un algorithme polynomiale qui trouve la
solution exacte au problème (tris, recherche, comptage)

NP: complexité non déterministe polynomiale: Il existe un algorithme
polynomiale qui vériﬁe une solution

NP diﬃcile: problème auquel on peut ramener tous les autres problèmes NP
par réduction polynomiale

NP complet: NP + NP diﬃcile (SAT, Voyageur de commerce, Sac à Dos, Clique,
Coloration de graphe, Couverture d’ensembles)
~~~

## Page 4

~~~text
Méthodes (meta)heuristiques
On ne sait pas si P=NP: on ne connaît AUCUN algorithme polynomiale pour
résoudre les problèmes de la classe NP

Seule solution à l’heure actuelle pour grande valeur de N (taille du problème);
utiliser des méthodes approchées (dites heuristiques):

1.   Mono-agent: recuit-simulé, hill-climbing, méthode taboue
2.   Multi-agent: algorithmes génétiques (GA) , colonies de fourmies (ACO),
     particule swarm optimisation (PSO), artiﬁcial bee colony (ABC) ...
~~~

## Page 5

~~~text
Algorithme de recuit simulé
Engendrer une solution initiale S
S* = S
T = temperature initiale (valeur arbitraire en général assez
grande)
Repeter
   V = un voisin S
   Si f(V) < f(S) ou aleat() < metropolis(V,S,T) alors S=V
   Si f(S) < f(S*) alors S*=S
   Mettre a jour T Jusqu'a condition de fin
Retourner S*
~~~

## Page 6

~~~text
Voisinage pour TSP
Pour le TSP, une solution est un chemin hamiltonien. Un voisin est un chemin
hamiltonien assez proche.

Par exemple: A-B-C-D-E-A peut avoir pour voisin en permutant B et E, le
chemin hamiltonien A-E-C-D-B-A (modiﬁcation de 4 arêtes A-B, B-C, D-E et E-A).

Ce voisinage est assez distant. On préfèrera l’inversion du sous-chemin entre
B et E, qui donne le voisin A-E-D-C-B-A (modiﬁcation de 2 arêtes A-B et E-A,
dans le TSP symétrique (D-C = C-D)
~~~

## Page 7

~~~text
Critère de metropolis
●   Évalue la probabilité de choix d'une solution voisine V moins bonne que la
    solution courante S en fonction de leur diﬀérence de coût
    (abs(f(S)-f(V)) et de l'état d'avancement de l'algorithme
    (température T)

●   metropolis(V,S,T) = exp(-(abs(f(S)-f(V))/T)
~~~

## Page 8

~~~text
Initialisation et mise à jour température
Initialisation:

 ●   empiriquement (en fonction du problème par essais successifs) :
     CONSEILLE
 ●   à partir d’une solution initiale et de d’un voisin via la formule de
     métropolis (en ﬁxant une faible probabilité) RISQUE

Mise à jour:

 ●   diminution par palier (diminution toutes les k itérations)
 ●   continue (T=lambda*T avec lambda <1) en général 0.99
~~~

## Page 9

~~~text
Conditions d’arrêts
Plusieurs possibilités:

●   Convergence: pas d’amélioration de S* pendant un nombre déﬁni
    d’itérations
●   Nombre d’itérations max atteint sans convergence
●   Optimum théorique atteint (plus diﬃcile à détecter)
~~~
