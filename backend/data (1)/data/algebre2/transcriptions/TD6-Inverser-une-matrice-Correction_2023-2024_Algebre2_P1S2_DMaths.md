# Algèbre 2 — Corrigé TD6 : calcul de l’inverse d’une matrice (2023–2024)

> Source : `PREING1-S2/Algebre2/TD6-Inverser-une-matrice-Correction_2023-2024_Algebre2_P1S2_DMaths.pdf`, 5 pages (PDF natif LaTeX). En-tête : « Cycle Pré-ingenieur — Première Année — Agèbre II - 2023/2024 » (coquilles d’origine).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; matrices restituées en LaTeX. Tous les carrés, cubes, inverses, produits $P^{-1}AP$ et formules de $A^n$ ont été vérifiés numériquement ; ils sont justes.
> Remarques sur la source, sans correction dans le texte :
> - **Exercice 2** : $A$ est une matrice $2\times2$ ; lire $\mathscr M_2(\mathbb K)$ au lieu de $\mathscr M_n(\mathbb K)$.
> - **Exercice 4** : « $-A^2-3a-3I_3$ » est une coquille pour $-A^2-3A-3I_3$.
> - **Exercice 9.4** : l’expression de $A^n$ donnée vaut pour $n\ge1$ ; pour $n=0$, $A^0=I_3$.
> - Coquilles conservées : « Ce qui montrer », « la rang », « la pivot », « les système récurrent », « consdier », « l’expression explicites ».

# Corrigé TD6 : Calcul de l’inverse d’une matrice

## Exercice 1

Soit $A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$

1. Calculer $A^2$ et vérifier que $A^2=A+2I_3$.
2. En déduire que $A$ est inversible et donner son inverse en fonction de $A$.

*Correction.*

1. $$A^2=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}=A+2I_3$$
2. Nous avons donc $A^2-A=2I_3$, c’est-à-dire $A\left(\frac{A-I_3}2\right)=I_3$. Ce qui montrer que $A$ est inversible et que son inverse est $A^{-1}=\frac12(A-I_3)=\frac12\begin{pmatrix}-1&1&1\\1&-1&1\\1&1&-1\end{pmatrix}$.

## Exercice 2

Démontrer que pour toute matrice $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathscr M_n(\mathbb K)$ :

$$A^2-(a+d)A+(ad-bc)I_2=0$$

En déduire une condition nécessaire et suffisante pour que $A$ soit inversible et exprimer $A^{-1}$ dans ce cas.

*Correction.* La relation $A^2-(a+d)A+(ad-bc)I_2=0$ est facilement vérifiable une fois calculé :

$$A^2=\begin{pmatrix}a^2+bc&ab+bd\\ac+cd&bc+d^2\end{pmatrix}$$

On a donc : $A((a+d)I_2-A)=(ad-bc)I_2$.

Supposons que $\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc\neq0$. On a alors :

$$A\left[\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\right]=\left[\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\right]A=I_2$$

Donc $A$ est inversible et :

$$A^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$

Réciproquement, si $ad-bc=0$, alors $A(A-(a+d)I_2)=0$ et donc la matrice $A$ n’est pas inversible.

Conclusion : $A$ est inversible $\Leftrightarrow\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc\neq0$, l’inverse éventuel étant celui formulé plus haut.

## Exercice 3

Soit $A=\begin{pmatrix}1&0&2\\0&-1&1\\1&-2&0\end{pmatrix}$. Calculer $A^3-A$. En déduire l’inversibilité de $A$ et l’expression de son inverse.

*Correction.* On vérifie que $A^2=\begin{pmatrix}3&-4&2\\1&-1&-1\\1&2&0\end{pmatrix}$ et $A^3=\begin{pmatrix}5&0&2\\0&3&1\\1&-2&4\end{pmatrix}$. On en déduit $A^3-A=4I_3$. Par conséquent :

$$A\left(\frac14(A^2-I_3)\right)=\left(\frac14(A^2-I_3)\right)A=I_3$$

Il en résulte que $A$ est inversible et que :

$$A^{-1}=\frac14(A^2-I_3)=\frac14\begin{pmatrix}2&-4&2\\1&-2&-1\\1&2&-1\end{pmatrix}$$

## Exercice 4

On considère la matrice $A=\begin{pmatrix}2&-1&2\\5&-3&3\\-1&0&-2\end{pmatrix}$. Calculer $(A+I_3)^3$. En déduire l’inversibilité de $A$ et l’expression de son inverse.

*Correction.* On vérifie sans difficulté que $(A+I_3)^3=0$. On a donc, en utilisant la formule du binôme :

$$A^3+3A^2I_3+3AI_3^2+I_3^3=0$$

C’est-à-dire aussi : $A^3+3A^2+3A+I_3=0$. On en déduit :

$$A(-A^2-3A-3I_3)=(-A^2-3A-3I_3)A=I_3$$

Par conséquent, $A$ est inversible et :

$$A^{-1}=-A^2-3a-3I_3=\begin{pmatrix}-6&2&-3\\-7&2&-4\\3&-1&1\end{pmatrix}$$

## Exercice 5

Calculer l’inverse des matrices suivantes, s’il existe, par la méthode de Gauss-Jordan :

$$A=\begin{pmatrix}1&0&1\\2&-1&1\\-1&1&-1\end{pmatrix}\ ;\ B=\begin{pmatrix}1&1&-1\\2&0&1\\2&1&-1\end{pmatrix}\ ;\ C=\begin{pmatrix}2&0&1\\-1&1&1\\1&0&1\end{pmatrix}$$

$$D=\begin{pmatrix}3&2&-1\\2&0&1\\-2&2&1\end{pmatrix}\ ;\ E=\begin{pmatrix}1&1&0\\0&1&1\\1&-1&0\end{pmatrix}\ ;\ F=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&-1\end{pmatrix}.$$

*Correction.*

$$A^{-1}=\begin{pmatrix}0&1&1\\1&0&1\\1&-1&-1\end{pmatrix}\ ;\ B^{-1}=\begin{pmatrix}-1&0&1\\4&1&-3\\2&1&-2\end{pmatrix}\ ;\ C^{-1}=\begin{pmatrix}1&0&-1\\2&1&-3\\-1&0&2\end{pmatrix}$$

$$D^{-1}=\frac1{18}\begin{pmatrix}2&4&-2\\4&-1&5\\-4&10&4\end{pmatrix}\ ;\ E^{-1}=\frac12\begin{pmatrix}1&0&1\\1&0&-1\\-1&2&1\end{pmatrix}\ ;\ F^{-1}=\frac12\begin{pmatrix}1&0&0&1\\0&1&0&-1\\0&0&1&-1\\1&-1&-1&1\end{pmatrix}$$

## Exercice 6

On considère la matrice $A=\begin{pmatrix}1&-2&2&1\\2&-4&3&4\\3&-3&4&7\\-1&5&0&-4\end{pmatrix}$.

Démontrer que $A$ est inversible et calculer son inverse par la méthode de Gauss-Jordan.

*Correction.* En effectuant la pivot de Gauss on montre que la rang de $A$ est 4, donc $A$ est inversible. En terminant avec la méthode de Gauss-Jordan, on obtient

$$A^{-1}=\frac13\begin{pmatrix}53&-58&17&-15\\1&-2&1&0\\-18&21&-6&6\\-12&12&-3&3\end{pmatrix}$$

## Exercice 7

On considère les matrices $A=\begin{pmatrix}2&-1&0\\-2&1&-2\\1&1&3\end{pmatrix}$ et $P=\begin{pmatrix}1&1&1\\1&0&-1\\-1&-1&0\end{pmatrix}$.

1. Montrer que $P$ est inversible et exprimer son inverse.
2. Montrer que $T=P^{-1}AP$ est triangulaire supérieure.
3. Calculer $A^n$ pour tout $n\in\mathbb N$.

*Correction.* Comme Exo 8. DM pour les étudiants

1. $P^{-1}=\begin{pmatrix}1&1&1\\-1&-1&-2\\1&0&1\end{pmatrix}$
2. $T=\begin{pmatrix}1&0&0\\0&2&0\\0&0&3\end{pmatrix}$
3. $A^n=PT^nP^{-1}=\begin{pmatrix}-2^n+3^n+1&-2^n+1&-2.2^n+3^n+1\\-3^n+1&1&-3^n+1\\2^n-1&2^n-1&2.2^n-1\end{pmatrix}$

## Exercice 8

On considère les matrices $A=\begin{pmatrix}2&1&-1\\0&1&0\\1&1&0\end{pmatrix}$ et $P=\begin{pmatrix}1&-1&1\\0&1&1\\1&0&1\end{pmatrix}$.

1. Montrer que $P$ est inversible et exprimer son inverse.
2. Montrer que $T=P^{-1}AP$ est triangulaire supérieure.
3. Calculer $A^n$ pour tout $n\in\mathbb N$.

*Correction.*

1. On trouve $P^{-1}=\begin{pmatrix}-1&-1&2\\-1&0&1\\1&1&-1\end{pmatrix}$ par la méthode de Gauss-Jordan.
2. On trouve $T=\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}$, qui est bien triangulaire supérieure.
3. On a : $T=I_3+N$, où $N=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$, avec $N^k=0$ pour tout $k\ge2$. D’où par la formule du binôme :
   $$\forall n\in\mathbb N,\ T^n=\sum_{k=0}^{1}\binom nkN^k=\binom n0I_3+\binom n1N=I_3+nN=\begin{pmatrix}1&0&n\\0&1&0\\0&0&1\end{pmatrix}$$
   On peut alors en déduire, en tenant compte de $A=PTP^{-1}$ :
   $$\forall n\in\mathbb N,\ A^n=PT^nP^{-1}=\begin{pmatrix}n+1&n&-n\\0&1&0\\n&n&1-n\end{pmatrix}$$

## Exercice 9

On considère les suites réelles $(u_n)$, $(v_n)$ et $(w_n)$ définies par les système récurrent

$$\begin{cases}(u_0,v_0,w_0)=(1,1,2)\\ u_{n+1}=4u_n-2v_n-2w_n\\ v_{n+1}=u_n-w_n\\ w_{n+1}=3u_n-2v_n-w_n\end{cases}$$

On pose $X_n=\begin{pmatrix}u_n\\v_n\\w_n\end{pmatrix}$ pour tout $n\in\mathbb N$

1. Justifier qu’il existe une matrice $A\in\mathcal M_3(\mathbb R)$ que l’on précisera telle que
   $$\forall n\in\mathbb N,\ X_{n+1}=AX_n$$
2. En déduire $X_n$ en fonction de $A$, $X_0$ et de $n$.
3. On consdier la matrice $P=\begin{pmatrix}1&0&1\\1&1&0\\1&-1&1\end{pmatrix}$. Montrer que $P$ est inversible et calculer $P^{-1}AP$
4. En déduire l’expression explicites des suites $(u_n)$, $(v_n)$ et $(w_n)$.

*Correction.*

1. $$A=\begin{pmatrix}4&-2&-2\\1&0&-1\\3&-2&-1\end{pmatrix}$$
2. $X_n=A^nX_0$ ici $X_0=(1,1,2)$ par récurrence.
3. Deux méthodes pour calculer $P^{-1}=\begin{pmatrix}-1&1&1\\1&0&-1\\2&-1&-1\end{pmatrix}$ Et $P^{-1}AP=\begin{pmatrix}0&0&0\\0&1&0\\0&0&2\end{pmatrix}$
4. $$X_n=A^nX_0=\begin{pmatrix}2^{n+1}&-2^n&-2^n\\1&0&-1\\2^{n+1}-1&-2^n&-2^n+1\end{pmatrix}\begin{pmatrix}1\\1\\2\end{pmatrix}$$
