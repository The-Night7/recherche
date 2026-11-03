---
source: ING 2/Semestre 1/Décidabilité & Complexité/Examen/Série-Révision.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Décidabilité et complexité — Série d’exercices de révision

## Exercice 1 — Machine de Turing : division par deux

Construire une machine de Turing à une bande qui divise par 2 un nombre donné $n$ représenté en système décimal. Les zéros au début du mot sont autorisés.

**Exemples.** Pour $n=215$, le résultat doit être `107.5` ; pour $n=172$, le résultat doit être `086`.

**Corrigé.** La machine de Turing est présentée dans le tableau suivant. Au début, la tête se trouve sur le chiffre le plus à gauche.

- Colonne A : état de la machine.
- Colonne B : symbole lu.
- Colonne C : symbole écrit.
- Colonne D : déplacement de la tête.
- Colonne E : état suivant.
- $q_0$ : état initial et état sans retenue.
- $q_1$ : état avec retenue.
- $q_f$ : état terminal.
- $\square$ : espace blanc.
- $\mid$ : la tête ne se déplace pas.

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| $q_0$ | 0 | 0 | $\to$ | $q_0$ |
| $q_0$ | 1 | 0 | $\to$ | $q_1$ |
| $q_0$ | 2 | 1 | $\to$ | $q_0$ |
| $q_0$ | 3 | 1 | $\to$ | $q_1$ |
| $q_0$ | 4 | 2 | $\to$ | $q_0$ |
| $q_0$ | 5 | 2 | $\to$ | $q_1$ |
| $q_0$ | 6 | 3 | $\to$ | $q_0$ |
| $q_0$ | 7 | 3 | $\to$ | $q_1$ |
| $q_0$ | 8 | 4 | $\to$ | $q_0$ |
| $q_0$ | 9 | 4 | $\to$ | $q_1$ |
| $q_0$ | $\square$ | $\square$ | $\leftarrow$ | $q_f$ |
| $q_1$ | 0 | 5 | $\to$ | $q_0$ |
| $q_1$ | 1 | 5 | $\to$ | $q_1$ |
| $q_1$ | 2 | 6 | $\to$ | $q_0$ |
| $q_1$ | 3 | 6 | $\to$ | $q_1$ |
| $q_1$ | 4 | 7 | $\to$ | $q_0$ |
| $q_1$ | 5 | 7 | $\to$ | $q_1$ |
| $q_1$ | 6 | 8 | $\to$ | $q_0$ |
| $q_1$ | 7 | 8 | $\to$ | $q_1$ |
| $q_1$ | 8 | 9 | $\to$ | $q_0$ |
| $q_1$ | 9 | 9 | $\to$ | $q_1$ |
| $q_1$ | $\square$ | `.` | $\to$ | $q_2$ |
| $q_2$ | $\square$ | 5 | $\mid$ | $q_f$ |

L’état $q_f$ n’a pas de transition.

## Exercice 2 — Réduction au voyageur de commerce

Donner une réduction polynomiale du problème **Circuit hamiltonien** au problème **Voyageur de commerce**.

### Énoncé du problème Circuit hamiltonien

**Instance :** un graphe non orienté $G$.

**On cherche :** un parcours fermé qui passe par tous les sommets du graphe une et une seule fois et qui revient au sommet de départ.

### Énoncé du problème Voyageur de commerce

**Instance :** un ensemble de $n$ villes ; les prix $p_{ij}$, $i,j=1,2,\ldots,n$, des trajets directs d’une ville $i$ à une ville $j$ ; la somme d’argent disponible $S$.

**On cherche :** un parcours fermé qui passe par toutes les villes une et une seule fois, qui revient à la ville de départ et dont le prix total ne dépasse pas $S$.

**Remarque.** Pour Circuit hamiltonien, les déplacements se font uniquement par les arêtes de $G$. Pour Voyageur de commerce, on peut aller de toute ville à toute autre ; les seules contraintes sont les prix.

### Corrigé

Soit $G$ une instance du problème Circuit hamiltonien. On fabrique l’instance suivante du problème Voyageur de commerce :

$$p_{ij}=\begin{cases}1&\text{si }(i,j)\text{ est une arête de }G,\\2&\text{sinon.}\end{cases}$$

On choisit $S=n$, où $n$ est le nombre de sommets de $G$, et donc le nombre d’arêtes que doit parcourir un circuit hamiltonien.

Un parcours de voyageur de commerce dont le prix total ne dépasse pas $n$ existe si et seulement si le voyageur emprunte uniquement des trajets $(i,j)$ qui sont des arêtes du graphe, donc si et seulement si $G$ contient un circuit hamiltonien.
