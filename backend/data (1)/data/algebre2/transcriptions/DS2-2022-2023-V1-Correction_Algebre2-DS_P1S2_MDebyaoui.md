# Algèbre 2 — DS2 2022–2023 (version 1), sujet et correction

> Source : `PREING1-S2/Algebre2-DS/DS2-2022-2023-V1-Correction_Algebre2-DS_P1S2_MDebyaoui.pdf`, 5 pages (PDF natif LaTeX). En-tête : « Cycle Pré-ingenieur — Première Année — Agèbre I - 2022/2023 — D. Mohamed Ali ». Le document est classé en Algèbre 2 (S2) ; l’en-tête indique « Algèbre I ».
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; matrices, systèmes et barème (en rouge dans la source) restitués. Rangs, relation de dépendance, inverse de la matrice de $\beta$ et solutions du système vérifiés numériquement.
> Erreurs de la source, signalées et non corrigées dans le texte :
> - **Exercice 2.3** : l’argument d’engendrement est faux. Un vecteur quelconque de $\mathbb R^5$ ne s’écrit pas comme combinaison de $e_4$ et $e_5$. La conclusion est juste : la famille $(v_1,v_2,v_3,e_4,e_5)$ est de rang 5, c’est donc une famille libre de 5 vecteurs, ce qui suffit.
> - **Exercice 3.6** : $c=-x+z$, et non $c=-x-y+2z$. Les expressions de $a$ et $b$ sont justes.
> - **Exercice 4.2** : dans le vecteur central, lire $-3z-7t$, et non $-3z-9t$ ; la décomposition qui suit, avec $(9,-7,0,1)$, est juste.

# Correction DS2 Algèbre

## Exercice 1 (5 pts)

Soit $E$ un $\mathbb R$-espace vectoriel ainsi que deux sous-espaces vectoriels $F\subseteq E$ et $G\subseteq E$.
Soit $\gamma$ une famille de vecteurs de $E$.

1. Rappeler la définition d’un $\mathbb R$-espace vectoriel (1 pt).
2. Rappeler la définition du sous-espace vectoriel engendré par une famille de vecteurs $\gamma$ (1 pt).
3. Rappeler la définition de la somme $F+G$ (1 pt).
4. Montrer que $F+G=\operatorname{Vect}(F\cup G)$ (2 pts).

### Correction

Toutes les réponses se trouvent dans votre cours

## Exercice 2 (6 pts)

Considérons la famille de vecteurs $\beta=\{v_1,v_2,v_3,v_4,v_5\}$ de $\mathbb R^5$ telle que $v_1=(1,2,1,2,1)$, $v_2=(2,1,2,1,2)$, $v_3=(1,0,1,1,0)$, $v_4=(0,1,0,0,1)$ et $v_5=(1,0,1,0,1)$.

1. La famille $\beta$ est-elle liée ? Dans le cas positif, fournir les relations de dépendance linéaire (2 pts).
2. Déterminer une base $\Omega$ pour le sous-espace vectoriel $\operatorname{Vect}(\beta)$. Vous préciserez la dimension de $\operatorname{Vect}(\beta)$ (2 pts).
3. Considérons la famille $\gamma=\{e_4,e_5\}$, avec $e_4=(0,0,1,0,0)$ et $e_5=(0,0,0,0,1)$. Montrer que la famille $\gamma\cup\Omega$ forme une base pour $\mathbb R^5$ (2 pts).

### Correction

1. Pour vérifier si la famille $\beta$ est liée, on cherche à savoir s’il existe des scalaires $\lambda_1,\lambda_2,\lambda_3,\lambda_4,\lambda_5$, pas tous nuls, tels que :
   $$\lambda_1v_1+\lambda_2v_2+\lambda_3v_3+\lambda_4v_4+\lambda_5v_5=0$$
   où $0$ est le vecteur nul de $\mathbb R^5$. En d’autres termes, on cherche à savoir s’il existe une solution non triviale du système linéaire homogène suivant :
   $$\begin{pmatrix}1&2&1&0&1\\2&1&0&1&0\\1&2&1&0&1\\2&1&1&0&0\\1&2&0&1&1\end{pmatrix}\begin{pmatrix}\lambda_1\\\lambda_2\\\lambda_3\\\lambda_4\\\lambda_5\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\\0\end{pmatrix}$$
   Pour résoudre le système, on peut appliquer la méthode de pivot de Gauss qui permet d’obtenir sa forme échelonnée réduite :
   $$\begin{pmatrix}1&2&1&0&1\\0&-3&-2&1&-2\\0&0&1&-1&0\\0&0&0&0&0\\0&0&0&0&0\end{pmatrix}\begin{pmatrix}\lambda_1\\\lambda_2\\\lambda_3\\\lambda_4\\\lambda_5\end{pmatrix}=\begin{pmatrix}0\\0\\0\\0\\0\end{pmatrix}$$
   Le rang de la matrice est 3, donc la dimension de l’espace vectoriel engendré par $\beta$ est inférieure à 5. Comme $\beta$ contient 5 vecteurs, la famille $\beta$ est liée
   $$(-\lambda_4+\lambda_5)v_1-(\lambda_4+2\lambda_5)v_2+3\lambda_4v_3+3\lambda_4v_4+3\lambda_5v_5=0$$
2. Pour déterminer une base $\Omega$ pour le sous-espace vectoriel $\operatorname{Vect}(\beta)$, on peut voir que d’après la question précédente, la matrice des coefficients indique que les trois premiers vecteurs de $\beta$ sont linéairement indépendants. Par conséquent, on peut prendre $\Omega=\{v_1,v_2,v_3\}$ comme base de $\operatorname{Vect}(\beta)$. La dimension de $\operatorname{Vect}(\beta)$ est donc 3.
3. Pour montrer que $\gamma\cup\Omega$ forme une base pour $\mathbb R^5$, on doit montrer qu’elle est libre et qu’elle engendre tout $\mathbb R^5$. Comme $\Omega$ est une base pour $\operatorname{Vect}(\beta)$, tout vecteur $w\in\operatorname{Vect}(\beta)$ peut s’écrire comme une combinaison linéaire de $v_1$, $v_2$, et $v_3$ :
   $$w=\lambda_1v_1+\lambda_2v_2+\lambda_3v_3$$
   De même, tout vecteur de $\mathbb R^5$ peut s’écrire comme une combinaison linéaire de $e_4$ et $e_5$ :
   $$u=b_1e_4+b_2e_5$$
   Alors, tout vecteur de $\mathbb R^5$ peut s’écrire comme une combinaison linéaire de $\gamma\cup\Omega$ :
   $$u+w=\lambda_1v_1+\lambda_2v_2+\lambda_3v_3+b_1e_4+b_2e_5$$
   Par conséquent, $\gamma\cup\Omega$ engendre tout $\mathbb R^5$.
   Montrons maintenant que $\gamma\cup\Omega$ est libre. Supposons qu’il existe des coefficients $\lambda_1$, $\lambda_2$, $\lambda_3$, $b_1$, et $b_2$ tels que
   $$\lambda_1v_1+\lambda_2v_2+\lambda_3v_3+b_1e_4+b_2e_5=0$$
   En écrivant les coordonnées de chaque vecteur et en résolvant ce système, on trouve que $\lambda_1=\lambda_2=\lambda_3=b_1=b_2=0$. Par conséquent, $\gamma\cup\Omega$ est une famille libre de 5 vecteurs dans un espace de dimension 5, donc c’est une base pour $\mathbb R^5$.

## Exercice 3 (7 pts)

Soient $E\subseteq\mathbb R^3$ et $F\subseteq\mathbb R^3$ deux parties de $\mathbb R^3$ telles que : $E=\{(x,y,z)\in\mathbb R^3/x+y-z=0$ et $x-y-z=0\}$ et $F=\{(x,y,z)\in\mathbb R^3/x+y-2z=0\}$ ainsi que les vecteurs $u=(1,0,1)$, $v=(1,1,1)$ et $w=(0,2,1)$.

1. Montrer que les parties $E$ et $F$ sont des sous-espaces vectoriels de $\mathbb R^3$ (2 pts).
2. Déterminer une base du sous-espace vectoriel $E$. Vous préciserez la dimension de $E$ (1 pt).
3. Montrer que la famille $\{v,w\}$ est une base de $F$. Vous préciserez la dimension de $F$ (1 pt).
4. Montrer que la famille $\beta=\{u,v,w\}$ est une base de $\mathbb R^3$ (1 pt).
5. Montrer que $E\cap F=\{\mathbf 0_{\mathbb R^3}\}$ (1 pt).
6. Soit $\sigma=(x,y,z)\in\mathbb R^3$, alors exprimer $\sigma$ dans la base $\beta$ (1 pt).

### Correction

1. Pour montrer que $E$ est un sous-espace vectoriel de $\mathbb R^3$, il faut vérifier que :
   - $\mathbf 0_{\mathbb R^3}\in E$ ;
   - si $\mathbf u,\mathbf v\in E$, alors $\mathbf u+\mathbf v\in E$ ;
   - si $\mathbf u\in E$ et $k\in\mathbb R$, alors $k\mathbf u\in E$.

   On vérifie facilement que $\mathbf 0_{\mathbb R^3}\in E$, car $0+0-0=0$ et $0-0-0=0$.
   Soient $\mathbf u=(x_1,y_1,z_1)$ et $\mathbf v=(x_2,y_2,z_2)$ deux vecteurs de $E$. Alors on a $x_1+y_1-z_1=0$, $x_1-y_1-z_1=0$ et $x_2+y_2-z_2=0$, $x_2-y_2-z_2=0$. En additionnant ces équations, on obtient $(x_1+x_2)+(y_1+y_2)-(z_1+z_2)=0$ et $(x_1+x_2)-(y_1+y_2)-(z_1+z_2)=0$, ce qui montre que $\mathbf u+\mathbf v\in E$.
   Soit maintenant $\mathbf u=(x,y,z)\in E$ et $k\in\mathbb R$. Alors on a $x+y-z=0$ et $x-y-z=0$. En multipliant les deux équations par $k$, on obtient $kx+ky-kz=0$ et $kx-ky-kz=0$, donc $k\mathbf u\in E$.
   On peut procéder de la même façon pour montrer que $F$ est un sous-espace vectoriel de $\mathbb R^3$.

   **Deuxième méthode :**
   On a $E=\{\mathbf u\in\mathbb R^3\mid\mathbf u=(x,y,z)$ avec $x+y-z=0$ et $x-y-z=0\}$. En résolvant ce système d’équations, on trouve $x=z$ et $y=0$, donc $E=\{\lambda(1,0,1)\mid\lambda\in\mathbb R\}$. Ainsi, $E=\operatorname{Vect}\{(1,0,1)\}$ ce qui implique que $E$ est un sous espace vectoriel de $\mathbb R^3$. De la même manière, on a $F=\{\mathbf u\in\mathbb R^3\mid\mathbf u=(x,y,z)$ avec $x+y-2z=0\}$. On peut réécrire cette équation sous la forme $z=\frac12(x+y)$, ce qui montre que tout vecteur de $F$ peut s’écrire comme une combinaison linéaire de $(1,0,\frac12)$ et $(0,1,\frac12)$. Par conséquent $F=\operatorname{Vect}\{(1,0,\frac12),(0,1,\frac12)\}$ ce qui implique que $F$ est un sous espace vectoriel de $\mathbb R^3$.
2. On a montré dans la question précédente que $E=\operatorname{Vect}\{(1,0,1)\}$, alors $\{(1,0,1)\}$ est une base de $E$, et $\dim E=1$.
3. On peut remarquer que $w=2(0,1,\frac12)$, que $v=(1,0,\frac12)+(0,1,\frac12)$. De plus $v$ et $w$ sont linéairement indépendants (ne sont pas colinéaires), donc $\{v,w\}$ est une base de $F$, et $\dim F=2$.
4. La famille $\beta=u,v,w$ est une base de $\mathbb R^3$ si et seulement si $\beta$ est une famille libre et engendre $\mathbb R^3$. On peut vérifier facilement que $\beta$ est une famille libre de 3 vecteurs dans un espace de dimension 3, donc c’est une base pour $\mathbb R^3$.
5. Supposons qu’il existe un vecteur non nul $\mathbf u\in E\cap F$. Alors $\mathbf u\in E$, donc $\mathbf u$ est de la forme $\mathbf u=\lambda(1,0,1)$ pour un certain $\lambda\in\mathbb R$. D’autre part, $\mathbf u\in F$, donc $\mathbf u$ est de la forme $\mathbf u=(x,y,z)$ avec $x+y-2z=0$. En combinant ces deux expressions pour $\mathbf u$, on obtient $\lambda(1,0,1)=(x,y,z)$ avec $x+y-2z=0$, ce qui implique $\lambda+0-2\lambda=0$, donc $\lambda=0$ et $u=\mathbf 0_{\mathbb R^3}$. Ainsi, $E\cap F=\mathbf 0_{\mathbb R^3}$, où $\mathbf 0_{\mathbb R^3}$ est le vecteur nul de $\mathbb R^3$.
6. Soit $\mathbf u=(x,y,z)\in\mathbb R^3$. On a montré dans la question 4 que $\beta=\{u,v,w\}$ est une base de $\mathbb R^3$, donc il existe des scalaires $a,b,c\in\mathbb R$ tels que $\mathbf u=au+bv+cw$. En utilisant les coordonnées des vecteurs $u$, $v$ et $w$ dans la base canonique de $\mathbb R^3$, on peut exprimer $\mathbf u$ sous la forme $(x,y,z)=a(1,0,1)+b(1,1,1)+c(0,2,1)$, avec
   $$\begin{cases}a=-x-y+2z\\ b=2x+y-2z\\ c=-x-y+2z\end{cases}.$$

## Exercice 4 (5 pts)

Soit le système linéaire suivant :

$$(S):\begin{cases}x+2y+2z+5t=0\\-x-y+z+2t=0\\2x+3y+z+3t=0\\y+3z+7t=0\end{cases}$$

1. Résoudre le système linéaire $(S)$ et déterminer son rang (3 pts).
2. Soit $E$ l’ensemble des solutions de ce système. Montrer que $E$ est un sous-espace vectoriel de $\mathbb R^4$ (1 pt).
3. Déterminer une base du sous-espace vectoriel $E$. Préciser la dimension de $E$ (1 pt).

### Correction

1. En utilisant la méthode du pivot de Gauss, on peut réduire la matrice augmentée du système $(S)$ :
   $$\left(\begin{array}{cccc|c}1&2&2&5&0\\-1&-1&1&2&0\\2&3&1&3&0\\0&1&3&7&0\end{array}\right)\longrightarrow\left(\begin{array}{cccc|c}1&2&2&5&0\\0&1&3&7&0\\0&-1&-3&-7&0\\0&1&3&7&0\end{array}\right)\longrightarrow\left(\begin{array}{cccc|c}1&0&-4&-9&0\\0&1&3&7&0\\0&0&0&0&0\\0&0&0&0&0\end{array}\right)$$
   Le système linéaire réduit nous donne deux équations indépendantes :
   $$\begin{cases}x+2y+2z+5t=0\\y+3z+7t=0\end{cases}$$
   On peut écrire la solution générale de $(S)$ sous la forme :
   $$\begin{pmatrix}x\\y\\z\\t\end{pmatrix}=\begin{pmatrix}4z+9t\\-3z-7t\\z\\t\end{pmatrix}$$
   On a donc une infinité de solutions $(x,y,z,t)=(4z+9t,-3z-7t,z,t)$, ce qui montre que le système $(S)$ admet une solution pour tout choix des scalaires $z$ et $t$. Le rang de la matrice augmentée est donc 2 (il y a deux pivots).
2. Soit $E$ l’ensemble des solutions du système $(S)$. Tout vecteur $u=(x,y,z,t)$ de $E$ peut être exprimé sous la forme suivante :
   $$\begin{pmatrix}x\\y\\z\\t\end{pmatrix}=\begin{pmatrix}4z+9t\\-3z-9t\\z\\t\end{pmatrix}=z\begin{pmatrix}4\\-3\\1\\0\end{pmatrix}+t\begin{pmatrix}9\\-7\\0\\1\end{pmatrix}$$
   Ainsi $E=\operatorname{Vect}\{(4,-3,1,0),(9,-7,0,1)\}$. On en déduit que $E$ est un sous-espace vectoriel de $\mathbb R^4$ de dimension 2.

   **Autre méthode :**
   Pour montrer que $E$ est un sous-espace vectoriel de $\mathbb R^4$, il faut montrer que $E$ contient le vecteur nul, que $E$ est stable par addition et par multiplication par un scalaire.
   Le vecteur nul est solution du système (S), donc appartient à $E$. Soient $(x_1,y_1,z_1,t_1)$ et $(x_2,y_2,z_2,t_2)$ deux solutions de (S) et soit $\lambda\in\mathbb R$. Alors, $(x_1+x_2,y_1+y_2,z_1+z_2,t_1+t_2)$ est solution de (S), car :
   - $(x_1+x_2)+2(y_1+y_2)+2(z_1+z_2)+5(t_1+t_2)=(x_1+2y_1+2z_1+5t_1)+(x_2+2y_2+2z_2+5t_2)=0+0=0$,
   - $(y_1+y_2)+3(z_1+z_2)+7(t_1+t_2)=(y_1+3z_1+7t_1)+(y_2+3z_2+7t_2)=0+0=0$.

   Ainsi, $E$ est stable par addition. De plus, pour tout $(x,y,z,t)\in E$ et tout $\lambda\in\mathbb R$, on a $\lambda(x,y,z,t)=(\lambda x,\lambda y,\lambda z,\lambda t)$, qui est solution de $(S)$ car :
   - $\lambda x+2\lambda y+2\lambda z+5\lambda t=\lambda(x+2y+2z+5t)=\lambda\times0=0$,
   - $\lambda y+3\lambda z+7\lambda t=\lambda(y+3z+7t)=\lambda\times0=0$.

   Ainsi, $E$ est stable par multiplication par un scalaire. Donc, $E$ est un sous-espace vectoriel de $\mathbb R^4$.
3. On a démontré dans la question 2 que la famille de vecteurs $\{(4,-3,1,0),(9,-7,0,1)\}$ engendre $E$. De plus, comme ces deux vecteurs sont linéairement indépendants, ils forment une base du sous-espace vectoriel $E$. Ainsi, la base de $E$ est donnée par :
   $$\left\{\begin{pmatrix}4\\-3\\1\\0\end{pmatrix},\begin{pmatrix}9\\-7\\0\\1\end{pmatrix}\right\}$$
   La dimension de $E$ est donc 2.
