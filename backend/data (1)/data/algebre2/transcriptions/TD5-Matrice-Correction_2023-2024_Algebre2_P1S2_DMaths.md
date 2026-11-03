# Algèbre 2 — Corrigé TD5 : Matrices (2023–2024)

> Source : `PREING1-S2/Algebre2/TD5-Matrice-Correction_2023-2024_Algebre2_P1S2_DMaths.pdf`, 4 pages (PDF natif LaTeX). En-tête : « Cycle Pré-ingenieur — Première Année — Agèbre II - 2023/2024 » (coquilles d’origine).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; matrices et formules restituées en LaTeX. Tous les produits matriciels et les formules de puissances ont été vérifiés numériquement.
> Erreurs de la source, signalées et non corrigées dans le texte :
> - **Exercice 1** : les réponses des cas 2 et 3 sont inversées. Pour le cas 2, $BA=\begin{pmatrix}1&2\\5&8\\3&4\end{pmatrix}$ ; pour le cas 3, $BA=\begin{pmatrix}0&0\\0&0\\0&1\end{pmatrix}$.
> - **Exercice 4.2** : dans la dernière ligne, il faut lire $(2-2^n)$, et non $(2-X^n)$. Le $x$ minuscule de $X^2-3x+2$ est aussi une coquille.
> - **Exercice 5.3** : le coefficient « $03^p$ » de la première matrice est une coquille pour $0\quad3^p$.
> - Autres coquilles conservées : « consid‘ere », « deduire », « est-e-elle ».

# Corrigé TD5 : Matrices

## Exercice 1

Dans chacun des cas suivants, les produits $AB$ et $BA$ existent-ils ? Si oui, les calculer

1. $A=\begin{pmatrix}1&2&1\\3&4&-1\end{pmatrix}$, $B=\begin{pmatrix}1&0\\2&1\\0&1\end{pmatrix}$,
2. $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}1&0\\2&1\\0&1\end{pmatrix}$
3. $A=\begin{pmatrix}0&1\\0&1\end{pmatrix}$, $B=\begin{pmatrix}0&0\\1&-1\\0&1\end{pmatrix}$
4. $A=\begin{pmatrix}1&0&1\\1&2&-1\\3&1&0\end{pmatrix}$, $B=\begin{pmatrix}1&1&-1\\0&1&2\\-1&-2&0\end{pmatrix}$

*Correction.*

1. $AB=\begin{pmatrix}5&3\\11&3\end{pmatrix}$, $BA=\begin{pmatrix}1&2&1\\5&8&1\\3&4&-1\end{pmatrix}$
2. il n’existe pas $AB$, $BA=\begin{pmatrix}0&0\\0&0\\0&1\end{pmatrix}$ *(sic : résultat du cas 3)*
3. il n’existe pas $AB$, $BA=\begin{pmatrix}1&2\\5&8\\3&4\end{pmatrix}$ *(sic : résultat du cas 2)*
4. $AB=\begin{pmatrix}0&-1&-1\\2&5&3\\3&4&-1\end{pmatrix}$, $BA=\begin{pmatrix}-1&1&0\\7&4&-1\\-3&-4&1\end{pmatrix}$

## Exercice 2

On consid‘ere les matrices

$$A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\ B=\begin{pmatrix}1&1\\1&2\end{pmatrix}$$

Calculer $AB$, $BA$, $(A-B)^2$ et $A^2-2AB+B^2$. Que remarque-t-on ?

*Correction.*

- $AB=\begin{pmatrix}3&5\\7&11\end{pmatrix}$
- $BA=\begin{pmatrix}4&6\\7&10\end{pmatrix}$
- $(A-B)^2=\begin{pmatrix}2&2\\4&6\end{pmatrix}$

$A^2-2AB+B^2=\begin{pmatrix}3&3\\4&5\end{pmatrix}$

$AB\neq BA$ donc on ne peut pas utiliser l’identité remarquable pour les matrices.

## Exercice 3

Soit

$$A=\begin{pmatrix}1&-2&-2\\-2&1&-2\\-2&-2&1\end{pmatrix}$$

Calculer ${}^tA\,A$. La matrice $A$ est-e-elle inversible ? si oui, quel est son inverse ?

*Correction.* ${}^tA\,A=A^2=\begin{pmatrix}9&0&0\\0&9&0\\0&0&9\end{pmatrix}=9I_3$. Donc $A$ inversible et $A^{-1}=\frac19A=\frac19\begin{pmatrix}1&-2&-2\\-2&1&-2\\-2&-2&1\end{pmatrix}$

## Exercice 4

Soit $A=\begin{pmatrix}-1&-2\\3&4\end{pmatrix}$

1. Calculer $A^2-3A+2I_2$. En deduire que A est inversible et calculer son inverse.
2. Pour $n\ge2$, déterminer le reste de la division euclidienne de $X^n$ par $P(X)=X^2-3X+2$.
3. Déterminer l’expression de $A^n$ pour tout $n\in\mathbb N$.

*Correction.*

1. On vérifie sans difficultés que $A^2-3A+2I_2=0$. Alors $A(A-3I_2)=-2I_2$. Alors
   $$A^{-1}=\frac{-1}2(A-3I_2)=\begin{pmatrix}2&1\\-\frac32&-\frac12\end{pmatrix}$$
2. Compte tenu de $\deg(P)=2$, la division euclidienne de $X^n$ par $P(X)=X^2-3X+2$ s’écrit sous la forme :
   $$X^n=(A^2-3X+2)Q_n(X)+(a_nX+b_n)$$
   En remarquant que $1$ et $2$ sont les racines de $P$, on en déduit : $\forall n\in\mathbb N$, $\begin{cases}1^n=a_n(1)+b_n\\ 2^n=a_n(2)+b_n\end{cases}$.
   D’où immédiatement, par addition et soustraction de lignes : $\forall n\in\mathbb N$, $\begin{cases}a_n=2^n-1\\ b_n=2-2^n\end{cases}$.
   On a ainsi : $\forall n\in\mathbb N,\ X^n=(X^2-3x+2)Q_n(X)+(2^n-1)X+(2-X^n)$.
   > La source écrit aussi $(A^2-3X+2)$ au lieu de $(X^2-3X+2)$ dans la première égalité.
3. En appliquant la relation précédente à $X=A$, puis en utilisant le résultat du 1, on obtient que :
   $$\forall n\in\mathbb N,\ A^n=(A^2-3A+2I_2)Q_n(A)+(2^n-1)A+(2-2^n)I_2=(2^n-1)A+(2-2^n)I_2$$
   Soit aussi :
   $$\forall n\in\mathbb N,\ A^n=\begin{pmatrix}3-2^{n+1}&2-2^{n+1}\\3\times2^n-3&3\times2^n-2\end{pmatrix}$$

## Exercice 5

Soit $A=\begin{pmatrix}3&1&0\\0&3&2\\0&0&3\end{pmatrix}$

1. Vérifier que l’on peut écrire $A=3I_3+N$ où $N$ est une matrice à déterminer.
2. Calculer $N^2$, $N^3$ puis $N^p$ pour $p\ge3$.
3. En déduire $A^p$ pour tout $p\ge1$.
4. Application. Soit $(x_n)$, $(y_n)$ et $(z_n)$ trois suites réelles telles que
   $$x_0=1,\ y_0=2,\ z_0=7$$
   $$\begin{cases}x_{n+1}=3x_n+y_n\\ y_{n+1}=3y_n+2z_n\\ z_{n+1}=3z_n\end{cases}$$
   Soit $X_n=(x_n,y_n,z_n)^t$
   1. (a) Trouver une matrice $M$ telle que $X_{n+1}=MX_n$.
   2. (b) En déduire que $X_n=M^nX_0$.
   3. (c) Calculer $M^n$.
   4. (d) En déduire les expressions de $x_n,y_n,z_n$ en fonction de $n$.

*Correction.*

1. $A=\begin{pmatrix}3&0&0\\0&3&0\\0&0&3\end{pmatrix}+\begin{pmatrix}0&1&0\\0&0&2\\0&0&0\end{pmatrix}=3I_3+N$
2. $N^2=\begin{pmatrix}0&0&2\\0&0&0\\0&0&0\end{pmatrix}$, $N^3=\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}$ donc $N^p=\mathbf 0$ pour tout $p\ge3$.
3. Remarquons $I_3N=NI_3$ donc
   $$A^p=(3I_3+N)^p=\sum_{k=0}^{n}\binom pk(3I_3)^{p-k}N^k=3^pI_3+p3^{p-1}N+\frac{p(p-1)}23^{p-2}N^2$$
   $$=\begin{pmatrix}3^p&0&0\\0&3^p&0\\0&03^p\end{pmatrix}+p3^{p-1}\begin{pmatrix}0&1&0\\0&0&2\\0&0&0\end{pmatrix}+\frac{p(p-1)}23^{p-2}\begin{pmatrix}0&0&2\\0&0&0\\0&0&0\end{pmatrix}$$
   $$=\begin{pmatrix}3^p&p.3^{p-1}&3^{p-2}(p^2-p)\\0&3^p&2p.3^{p-1}\\0&0&3^p\end{pmatrix}$$
   > La borne supérieure de la somme est notée $n$ dans la source ; il faut lire $p$.
4. (a) $M=A$
   (b) Par récurrence
   (c) $M^n=A^n$
   (d) $X_n=A^nX_0$ donc
   $$\begin{cases}x_n=3^n+2n3^{n-1}+7(n^2-n)3^{n-2}\\ y_n=2.3^n+14n3^{n-1}\\ z_n=7.3^n\end{cases}$$
