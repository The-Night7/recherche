---
source: ING 2/Semestre 1/Décidabilité & Complexité/fiche déci.pdf
pages: 3
transcription: manuelle
verification: lecture intégrale de la source
---

# Décidabilité et complexité — Fiche manuscrite

## Page 1 — 3-SAT, problème NP-complet

Exemple de formule :

$$(v_1\lor v_2\lor\neg v_3)\land(\neg v_1\lor\neg v_2\lor v_3).$$

Les annotations désignent les littéraux et une clause avec trois littéraux.

Soit une formule en forme normale conjonctive avec exactement trois littéraux par clause. La formule est-elle satisfiable ? Autrement dit, existe-t-il une affectation des variables qui la rende vraie ?

**3-SAT appartient à NP :** la fiche indique seulement « ez » à cet endroit.

**3-SAT est NP-difficile.** Pour prouver cela, on part d’une formule quelconque de SAT. La fiche admet qu’elle peut être mise en forme normale conjonctive, puis en formule 3-SAT. L’objectif est de montrer que SAT, NP-complet, est polynomialement réductible à 3-SAT.

### Cas d’un littéral

Remplacer $(x_1)$ par :

$$(x_1\lor y_1\lor y_2)\land(x_1\lor y_1\lor\neg y_2)
\land(x_1\lor\neg y_1\lor y_2)\land(x_1\lor\neg y_1\lor\neg y_2).$$

La clause initiale est satisfiable si et seulement si la formule obtenue l’est aussi.

### Cas de deux littéraux

Remplacer $(x_1\lor x_2)$ par :

$$(x_1\lor x_2\lor y)\land(x_1\lor x_2\lor\neg y).$$

Même équivalence de satisfiabilité.

### Cas de quatre littéraux ou plus

Pour $\ell\geq4$, remplacer $(x_1\lor x_2\lor\cdots\lor x_\ell)$ par la chaîne :

$$(x_1\lor x_2\lor y_1)
\land(\neg y_1\lor x_3\lor y_2)
\land(\neg y_2\lor x_4\lor y_3)
\land\cdots
\land(\neg y_{\ell-4}\lor x_{\ell-2}\lor y_{\ell-3})
\land(\neg y_{\ell-3}\lor x_{\ell-1}\lor x_\ell).$$

Les clauses intermédiaires n’existent que lorsque leurs indices sont définis ; pour $\ell=4$, la chaîne se réduit à $(x_1\lor x_2\lor y_1)\land(\neg y_1\lor x_3\lor x_4)$.

La fiche veut montrer « clause satisfiable $\Rightarrow$ formule satisfiable » en choisissant les $y_j$. Elle écrit, si $x_i$ est vrai, de donner la valeur vrai aux $y_j$ pour $j\in\{0,\ldots,\ell-3\}\setminus\{i\}$. Cette indication est reproduite comme une erreur de la source : $y_0$ n’est pas défini, et le choix proposé ne prouve pas le résultat.

## Page 2 — Suite de la preuve et machine de Turing

### Sens réciproque et conclusion pour 3-SAT

Si la formule obtenue est vraie, au moins un $x_i$ est vrai. Par l’absurde, supposons tous les $x_i$ faux : les clauses successives imposent tous les $y_j$ vrais, mais la dernière impose $y_{\ell-3}$ faux. Contradiction.

La fiche affirme que cette transformation à partir d’une formule quelconque de SAT est polynomiale, puis conclut :

$$3\text{-SAT}\in\mathrm{NP}\quad\text{et}\quad3\text{-SAT est NP-difficile}
\quad\Longrightarrow\quad3\text{-SAT est NP-complet}.$$

### Machine de Turing

$$M=(Q,\Gamma,\Sigma,\delta,q_0,B,F).$$

| Symbole | Annotation de la fiche |
| --- | --- |
| $Q$ | Ensemble d’états |
| $\Gamma$ | Alphabet du ruban |
| $\Sigma$ | Alphabet d’entrée |
| $\delta$ | Annotation $\{L,S,R\}$ : gauche, sur place, droite |
| $q_0$ | État initial |
| $B$ | Symbole blanc |
| $F$ | Ensemble des états accepteurs |

Le diagramme est décrit comme une « machine qui vérifie si un mot finit par man ». Chaque étiquette donne le symbole lu, le symbole écrit et le déplacement. Les flèches visibles se transcrivent ainsi :

| État | Lu | Écrit | Déplacement | État suivant |
| --- | --- | --- | --- | --- |
| $q_0$ | m | m | R | $q_0$ |
| $q_0$ | a | a | R | $q_0$ |
| $q_0$ | n | n | R | $q_0$ |
| $q_0$ | blanc | blanc | L | $q_1$ |
| $q_1$ | n | n | L | $q_2$ |
| $q_1$ | m | m | S | $q_8$ |
| $q_1$ | a | a | S | $q_8$ |
| $q_2$ | a | a | L | $q_3$ |
| $q_2$ | n | n | S | $q_8$ |
| $q_2$ | m | m | S | $q_8$ |
| $q_3$ | m | m | S | $q_9$ |
| $q_3$ | a | a | S | $q_8$ |
| $q_3$ | n | n | S | $q_8$ |

Le dessin montre $q_8$ et $q_9$ avec un double cercle, sans légende de rejet. Pour réaliser le test annoncé, $q_9$ doit accepter et $q_8$ rejeter. Les transitions sur blanc depuis $q_1$, $q_2$ et $q_3$ ne sont pas dessinées ; elles concernent notamment les mots trop courts.

### Problème de l’arrêt — Indécidabilité

Soit $H$ une machine de Turing prenant en entrée une machine et l’entrée de cette machine. Elle répondrait « oui » si la machine s’arrête et « non » si elle ne s’arrête pas. La source emploie aussi « résout son problème » comme synonyme d’arrêt, ce qui n’est pas en général équivalent.

Supposons $H$ existante. La fiche construit une machine $X$ qui reçoit une machine $M$, copie son entrée pour former $H(M,M)$, puis « renvoie l’inverse de $H$ ».

## Page 3 — Diagonalisation, définitions et tris

### Suite de l’argument de diagonalisation

La notation du manuscrit est :

$$X(X)\longrightarrow H(X,X)\longrightarrow\neg H(X,X).$$

Le texte évoque deux cas : si $H$ répond oui, il prévoit que $X$ ne soit pas bloquée, mais $X$ se bloque ; si $H$ répond non, il prévoit que $X$ soit bloquée. La seconde phrase manuscrite ajoute pourtant que $X$ « ne se termine donc pas » et que $H$ avait tort. Cette phrase ne donne pas une contradiction : le comportement attendu dans ce second cas est un arrêt. La conclusion écrite est : « On a une contradiction, donc $H$ ne peut exister. »

### Quelques définitions

- **P :** classe de problèmes décisionnels pouvant être résolus efficacement, en temps polynomial en fonction de la taille de l’entrée.
- **NP :** problèmes dont on peut vérifier un certificat de réponse positive en temps polynomial. La source abrège cette définition en « problèmes que l’on peut vérifier en temps polynomial ».
- **NP-difficile :** au moins aussi difficile que les problèmes les plus difficiles de NP.
- $G(V,E)$ : graphe d’ensemble de sommets $V$ et d’ensemble d’arêtes $E$.

La fiche écrit :

$$\binom nk=\frac{n(n-1)\cdots(n-k)}{k!},\qquad\text{« polynôme de degré }k+1\text{ »}.$$

Cette formule est erronée ; voir la rectification ci-dessous.

### Tris

**Tri par sélection :** $O(n^2)$ dans tous les cas. On regarde tous les éléments de la liste, on place le plus petit en premier, puis on recommence en réduisant la liste des éléments à trier.

**Tri par insertion :** $O(n^2)$ en moyenne et dans le pire cas ; $O(n)$ dans le meilleur cas. On place les éléments de la liste à la bonne place un à un, comme des cartes.

## Rectifications mathématiques

Ces précisions corrigent les erreurs signalées, sans les attribuer au manuscrit.

1. Une affectation des variables constitue le certificat pour 3-SAT ; vérifier chaque clause prend un temps polynomial.
2. Une transformation naïve d’une formule quelconque en FNC peut être exponentielle. Pour justifier la réduction polynomiale, on peut partir de CNF-SAT ou employer une transformation avec variables auxiliaires et équivalence de satisfiabilité, de taille polynomiale. Chaque clause utilise des variables auxiliaires fraîches.
3. Pour la chaîne de longueur $\ell$, un choix correct est $y_j=\neg(x_1\lor\cdots\lor x_{j+1})$, pour $1\leq j\leq\ell-3$. Si la clause initiale est vraie, toutes les clauses de la chaîne le sont.
4. $\delta$ est une fonction de transition ; $\{L,S,R\}$ est l’ensemble des déplacements possibles, et non la fonction elle-même.
5. Pour la preuve de l’arrêt, définir $X(M)$ ainsi : si $H(M,M)$ répond oui, boucler indéfiniment ; sinon, s’arrêter. Alors $X(X)$ s’arrête si et seulement s’il ne s’arrête pas. Inverser simplement une réponse booléenne ne suffit pas.
6. Pour $k$ fixé, $\displaystyle\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}$ est un polynôme de degré $k$ en $n$.

Les fragments du cahier voisin visibles sur les bords des photographies ne font pas partie de cette fiche.
