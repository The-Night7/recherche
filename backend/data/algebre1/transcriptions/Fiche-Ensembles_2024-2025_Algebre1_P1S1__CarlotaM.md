---
source: PREING1-S1/Algebre1/Fiche-Ensembles_2024-2025_Algebre1_P1S1__CarlotaM.pdf
pages: 1
transcription: manuelle
---

# Algèbre 1 — Fiche sur les ensembles

## Opérations et vocabulaire

Pour des parties $A,B$ d'un ensemble $E$ :

- **Différence :** $A\setminus B=\{x\in E:x\in A\text{ et }x\notin B\}$.
- **Intersection :** $A\cap B=\{x\in E:x\in A\text{ et }x\in B\}$. Si $A\cap B=\varnothing$, les ensembles sont disjoints.
- **Union :** $A\cup B=\{x\in E:x\in A\text{ ou }x\in B\}$.
- **Complémentaire dans $E$ :** $A^c=E\setminus A=\{x\in E:x\notin A\}$, également noté $C_A^E$ sur la fiche.
- **Différence symétrique :** $A\mathbin\triangle B=(A\cup B)\setminus(A\cap B)=(A\setminus B)\cup(B\setminus A)$.

On utilise $\in$ pour l'appartenance d'un élément et $\subseteq$ pour l'inclusion d'un ensemble dans un autre.

$$\bigcap_{i=1}^n A_i=\{x\in E:\forall i\in\{1,\ldots,n\},\ x\in A_i\},$$

$$\bigcup_{i=1}^n A_i=\{x\in E:\exists i\in\{1,\ldots,n\},\ x\in A_i\}.$$

> **Rectification de la fiche :** la définition manuscrite de l'union emploie $\forall$ ; il faut $\exists$. Les dessins de Venn colorient respectivement la partie de $A$ hors de $B$, la zone commune, les deux disques, l'extérieur de $A$ et les deux parties hors de l'intersection.

## Propriétés des opérations

**Commutativité :**

$$A\cap B=B\cap A,\qquad A\cup B=B\cup A.$$

**Associativité :**

$$A\cap(B\cap C)=(A\cap B)\cap C=A\cap B\cap C,$$

$$A\cup(B\cup C)=(A\cup B)\cup C=A\cup B\cup C.$$

Pour $A\subseteq E$, $A\cap E=A$ et $A\cup\varnothing=A$.

**Distributivité :**

$$A\cap(B\cup C)=(A\cap B)\cup(A\cap C),$$

$$A\cup(B\cap C)=(A\cup B)\cap(A\cup C).$$

> La première formule manuscrite comporte un $B$ corrigé en $C$ ; la formule ci-dessus reprend cette correction.

## Complémentaires et lois de Morgan

$$ (A^c)^c=A,\qquad\varnothing^c=E,\qquad E^c=\varnothing.$$

Si $A\subseteq B$, alors $B^c\subseteq A^c$.

$$ (A\cap B)^c=A^c\cup B^c,\qquad(A\cup B)^c=A^c\cap B^c.$$

Les diagrammes de la fiche illustrent ces deux égalités en hachurant les complémentaires.

**Identités utiles :**

$$A\setminus B=A\cap B^c,\qquad A\cap B=B\iff B\subseteq A,$$

$$ (A\cap B)^c\cap(A\cap B)=\varnothing,$$

$$ (A\cap B)\mathbin\triangle(A\cap C)
=\bigl((A\cap B)\setminus(A\cap C)\bigr)
\cup\bigl((A\cap C)\setminus(A\cap B)\bigr).$$

> **Rectification de la fiche :** la ligne « $A\cap B=B$ » est accompagnée d'une inclusion insuffisante. L'équivalence correcte est celle écrite ci-dessus. « $\cup$ » correspond au « ou » et « $\cap$ » au « et ».

## Partition

Une partition finie de $E$ est une famille $\{A_1,\ldots,A_n\}$ de parties de $E$ telle que :

1. Pour chaque $k$, $A_k\ne\varnothing$.
2. $\bigcup_{k=1}^n A_k=E$.
3. Pour $i\ne j$, $A_i\cap A_j=\varnothing$ : les parties sont deux à deux disjointes.

Le dessin de la fiche représente $E$ découpé en sept régions disjointes $A_1,\ldots,A_7$.

## Produit cartésien

$$A\times B=\{(x,y):x\in A,\ y\in B\}.$$

Exemple : si $C=\{1,2\}$ et $D=\{1,2,3\}$,

$$C\times D=\{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)\}.$$

Plus généralement,

$$A_1\times\cdots\times A_n
=\{(x_1,\ldots,x_n):x_i\in A_i\text{ pour tout }i\}.$$

La diagonale de $A^2$ est $\Delta=\{(x,x):x\in A\}$.

$$ (A\times C)\cup(A\times D)=A\times(C\cup D),$$

$$ (A\times C)\cap(B\times D)=(A\cap B)\times(C\cap D).$$

## Nombre de parties

Si $E$ possède $n$ éléments, l'ensemble $\mathcal P(E)$ de ses parties possède $2^n$ éléments.

> Le titre manuscrit de cette ligne mentionne « $A\times B$ », mais la propriété porte sur $\mathcal P(E)$.
