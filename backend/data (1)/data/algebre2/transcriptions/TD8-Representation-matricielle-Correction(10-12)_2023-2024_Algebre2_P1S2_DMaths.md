# Algèbre 2 — TD8 Représentation matricielle : correction des exercices 10 et 12 (2023–2024)

> Source : `PREING1-S2/Algebre2/TD8-Representation-matricielle-Correction(10-12)_2023-2024_Algebre2_P1S2_DMaths.pdf`, 4 pages (PDF natif). En-tête : « Algèbre 2 — Préing 1, 2023-2024 ».
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; matrices, déterminants, systèmes et diagramme de changement de base restitués. Les étiquettes de colonnes et de lignes des matrices (en bleu dans la source) sont indiquées en note sous chaque matrice. Matrices, inverses, noyau et déterminants vérifiés numériquement. Les énoncés ne figurent pas dans la source.
> Erreurs de la source, signalées et non corrigées dans le texte :
> - **Exercice 10.5** : la première colonne de $B=\operatorname{Mat}_{\mathscr C}(f)$ est $\begin{pmatrix}0\\-1\\0\end{pmatrix}$, puisque $f(Q_1)=0Q_1-1Q_2+0Q_3$ comme l’écrit la solution 1, et non $\begin{pmatrix}0\\1\\0\end{pmatrix}$. Le calcul $P^{-1}AP$ donne bien $\begin{pmatrix}0&0&-2\\-1&0&-1\\0&2&2\end{pmatrix}$. L’erreur figure dans les deux solutions.
> - **Exercice 12.4, solution 2** : le développement porte sur la **ligne 1**, et non sur « $C_2$ » ; le résultat $-1$ est juste. « ker $f$ est $F$ » est une coquille pour « ker $f$ et $F$ ».

# Correction des exercices 10 et 12

## Exercice 10

1. Pour tout $P=aX^2+bX+c\in\mathbb R_2[X]$, on a :
   $$\begin{aligned}
   f(P)&=(X^2+X+1)2a+X^2(2aX+b)-2X(aX^2+bX+c)\\
   &=2a(X^2+X+1)+2aX^3+bX^2-2aX^3-2bX^2-2cX\\
   &=2a(X^2+X+1)+bX^2-2bX^2-2cX\in\mathbb R_2[X].
   \end{aligned}$$

2. D’après la question 1, $f$ est une application de $E$ dans $E$. Montrons que $f$ est linéaire. Soient $P,Q\in E$, et $\lambda\in\mathbb R$, on a :
   $$\begin{aligned}
   f(\lambda P+Q)&=(X^2+X+1)(\lambda P+Q)''+X^2(\lambda P+Q)'-2X(\lambda P+Q)\\
   &=(X^2+X+1)(\lambda P''+Q'')+X^2(\lambda P'+Q')-2X(\lambda P+Q)\\
   &=\lambda\left((X^2+X+1)P''+X^2P'-2XP\right)+(X^2+X+1)Q''+X^2Q'-2XQ\\
   &=\lambda f(P)+f(Q).
   \end{aligned}$$
   Donc $f$ est un endomorphisme de $E$.

3. Notons $\mathscr B=(P_0,P_1,P_2)$ la base canonique de $\mathbb R_2[X]$, c’est-à-dire $P_0=1$, $P_1=X$ et $P_2=X^2$. Alors :
   $$\begin{aligned}
   f(P_0)&=-2X=0P_0-2P_1+0P_2,\\
   f(P_1)&=-X^2=0P_0+0P_1-1P_2,\\
   f(P_2)&=2+2X+2X^2=2P_0+2P_1+2P_2,
   \end{aligned}$$
   donc la matrice de $f$ dans la base canonique est :
   $$A=\operatorname{Mat}_{\mathscr B}(f)=\begin{pmatrix}0&0&2\\-2&0&2\\0&-1&2\end{pmatrix}.$$
   *(Colonnes : $f(P_0)$, $f(P_1)$, $f(P_2)$ ; lignes : $P_0$, $P_1$, $P_2$.)*

4. On calcule le déterminant de $A$ en développant suivant la ligne 1 :
   $$\det(A)=\begin{vmatrix}0&0&2\\-2&0&2\\0&-1&2\end{vmatrix}=2\begin{vmatrix}-2&0\\0&-1\end{vmatrix}=4.$$
   Puisque $\det(A)\neq0$, la matrice $A$ est inversible, donc $f$ est bijective. Par conséquent, $f$ est un isomorphisme.

5. Notons $Q_1=X$, $Q_2=X^2$ et $Q_3=X^2+X+1$. Écrivons la matrice de la base $\mathscr C=(Q_1,Q_2,Q_3)$ relativement à la base $\mathscr B$ :
   $$P=\operatorname{Mat}_{\mathscr B}(\mathscr C)=\begin{pmatrix}0&0&1\\1&0&1\\0&1&1\end{pmatrix}.$$
   *(Colonnes : $Q_1$, $Q_2$, $Q_3$ ; lignes : $P_0$, $P_1$, $P_2$.)*

   On a $\det(P)=1\neq0$ donc $\mathscr C$ est une base de $E$ (ou alors, en permutant les lignes on voit que $\operatorname{rg}(P)=3$). Cherchons la matrice de $f$ dans la base $\mathscr C$.

   *Solution 1.* On calcule les images des vecteurs de $\mathscr C$ :
   $$\begin{aligned}
   f(Q_1)&=-X^2=0Q_1-1Q_2+0Q_3,\\
   f(Q_2)&=2X^2+2X+2=0Q_1+0Q_2+2Q_3,\\
   f(Q_3)&=X^2+2=-2Q_1-1Q_2+2Q_3,
   \end{aligned}$$
   où la dernière égalité peut se trouver en résolvant l’équation $X^2+2=\alpha X+\beta X^2+\gamma(X^2+X+1)$ d’inconnues $\alpha,\beta,\gamma$. Par conséquent :
   $$B=\operatorname{Mat}_{\mathscr C}(f)=\begin{pmatrix}0&0&-2\\1&0&-1\\0&2&2\end{pmatrix}.$$
   *(Colonnes : $f(Q_1)$, $f(Q_2)$, $f(Q_3)$ ; lignes : $Q_1$, $Q_2$, $Q_3$. Erreur de signe sur le coefficient $(2,1)$ : lire $-1$.)*

   *Solution 2.* On utilise la formule du changement de bases. La matrice de passage de $\mathscr B$ à $\mathscr C$ est la matrice $P$ écrite plus haut. Son inverse est la matrice (faire le calcul !) :
   $$P^{-1}=\begin{pmatrix}-1&1&0\\-1&0&1\\1&0&0\end{pmatrix}.$$
   La matrice de $f$ dans la base $\mathscr C$ est donnée par :

   *Diagramme : $(E,\mathscr C)\xrightarrow[B]{f}(E,\mathscr C)$ en haut, $(E,\mathscr B)\xrightarrow[A]{f}(E,\mathscr B)$ en bas ; flèche $P$ de $(E,\mathscr C)$ vers $(E,\mathscr B)$ à gauche, flèche $P^{-1}$ de $(E,\mathscr B)$ vers $(E,\mathscr C)$ à droite.*

   $$B=P^{-1}AP=\begin{pmatrix}0&0&-2\\1&0&-1\\0&2&2\end{pmatrix}.$$

   On retrouve bien la matrice de la solution 1.

## Exercice 12

1. Notons $\mathscr B_c=(e_1,e_2,e_3)$ la base canonique de $\mathbb R^3$. Calculons l’image des vecteurs $e_1,e_2,e_3$ par $f$ :
   $$\begin{aligned}
   f(e_1)&=f(1,0,0)=(17,12,16)=17e_1+12e_2+16e_3,\\
   f(e_2)&=f(0,1,0)=(-28,-20,-28)=-28e_1-20e_2-28e_3,\\
   f(e_3)&=f(0,0,1)=(4,3,5)=4e_1+3e_2+5e_3,
   \end{aligned}$$
   donc la matrice de $f$ dans la base canonique est :
   $$\operatorname{Mat}_{\mathscr B_c}(f)=\begin{pmatrix}17&-28&4\\12&-20&3\\16&-28&5\end{pmatrix}.$$

2. Soit $u=(x,y,z)\in\mathbb R^3$. On a :
   $$\begin{aligned}
   u\in\ker f\iff f(u)=0_{\mathbb R^3}
   &\iff\begin{cases}17x-28y+4z=0\\12x-20y+3z=0\\16x-28y+5z=0\end{cases}
   \iff\begin{cases}x-z=0 & L_1\leftarrow L_1-L_3\\12x-20y+3z=0\\16x-28y+5z=0\end{cases}\\
   &\iff\begin{cases}z=x\\15x-20y=0\\21x-28y=0\end{cases}
   \iff\begin{cases}z=x\\3x-4y=0 & L_2\leftarrow\frac15L_2\\3x-4y=0 & L_3\leftarrow\frac17L_3\end{cases}\\
   &\iff\begin{cases}z=x\\y=\frac34x\end{cases}
   \iff u=\left(x,\tfrac34x,x\right).
   \end{aligned}$$
   Donc $\ker f=\operatorname{Vect}(u_1)$ avec $u_1=(4,3,4)$. Une base $\mathscr B_1$ de $\ker f$ est formée du vecteur $u_1$.
   *Remarque : on pouvait prendre $(1,\frac34,1)$ comme vecteur directeur, mais n’importe quel multiple non nul est aussi vecteur directeur. Je choisis un vecteur à coordonnées entières pour faciliter les calculs par la suite.*

3. Une façon de montrer que $F$ est un s.e.v. est de remarquer que l’équation $f(u)=u$ est équivalente à $f(u)-u=0_{\mathbb R^3}$, c’est-à-dire $(f-\mathrm{id}_{\mathbb R^3})(u)=0_{\mathbb R^3}$. Ainsi, $F$ est le noyau de l’application linéaire $f-\mathrm{id}_{\mathbb R^3}$, donc c’est un s.e.v.
   Une autre façon est de résoudre l’équation $f(u)=u$ et montrer que $F$ est l’espace engendré par une famille de vecteurs, ce qui permet de déterminer une base de $F$ en même temps. Soit $u=(x,y,z)\in\mathbb R^3$, on a :
   $$\begin{aligned}
   u\in F\iff f(u)=u
   &\iff\begin{cases}17x-28y+4z=x\\12x-20y+3z=y\\16x-28y+5z=z\end{cases}
   \iff\begin{cases}16x-28y+4z=0\\12x-21y+3z=0\\16x-28y+4z=0\end{cases}\\
   &\iff\begin{cases}4x-7y+z=0 & L_1\leftarrow\frac14L_1\\4x-7y+z=0 & L_2\leftarrow\frac13L_2\\4x-7y+z=0 & L_3\leftarrow\frac14L_3\end{cases}\\
   &\iff z=-4x+7y\iff u=(x,\ y,\ -4x+7y)\iff u=xu_2+yu_3,
   \end{aligned}$$
   avec $u_2=(1,0,-4)$ et $u_3=(0,1,7)$. Donc $F=\operatorname{Vect}(u_2,u_3)$. De plus, les vecteurs $u_2$ et $u_3$ sont libres (car non colinéaires), donc ils forment une base $\mathscr B_2$ de $F$.

4. *Solution 1.* Montrons que $\ker f$ et $F$ sont en somme directe. Le vecteur directeur $u_1$ de $\ker f$ n’appartient pas à $F$ car $f(u_1)\neq u_1$, donc la droite $\ker f$ n’est pas incluse dans le plan $F$. Par conséquent, $\ker f\cap F=\{0_{\mathbb R^3}\}$. Par la formule de Grassmann, on a :
   $$\dim(\ker f\oplus F)=\dim(\ker f)+\dim(F)=1+2=3,$$
   donc $\ker f\oplus F=\mathbb R^3$. Ainsi, $\ker f$ est $F$ sont supplémentaires dans $\mathbb R^3$.

   *Solution 2.* Pour montrer que $\ker f$ et $F$ sont supplémentaires dans $\mathbb R^3$, on peut montrer que la réunion de $\mathscr B_1$ et $\mathscr B_2$ est une base de $\mathbb R^3$. Calculons par exemple le déterminant de la famille $(u_1,u_2,u_3)$ relativement à la base canonique :
   $$\begin{aligned}
   \det\left(\operatorname{Mat}_{\mathscr B_c}(u_1,u_2,u_3)\right)&=\begin{vmatrix}4&1&0\\3&0&1\\4&-4&7\end{vmatrix}\\
   &=\begin{vmatrix}0&1&0\\3&0&1\\20&-4&7\end{vmatrix}\qquad(C_1\leftarrow C_1-4C_2)\\
   &=-\begin{vmatrix}3&1\\20&7\end{vmatrix}\qquad(\text{developpement }C_2)\\
   &=-1.
   \end{aligned}$$
   Le déterminant est non nul, donc $\mathscr B=(u_1,u_2,u_3)$ est une base de $\mathbb R^3$. Par conséquent, les sous-espaces $\ker f$ et $F$ sont supplémentaires.

5. Puisque $u_1\in\ker f$, on a $f(u_1)=0_{\mathbb R^3}$, et puisque $u_2,u_3\in F$, on a $f(u_2)=u_2$ et $f(u_3)=u_3$ (par définition, les vecteurs de $F$ sont solutions de $f(u)=u$). Ainsi, la matrice de $f$ dans la base $\mathscr B$ est :
   $$\operatorname{Mat}_{\mathscr B}(f)=\begin{pmatrix}0&0&0\\0&1&0\\0&0&1\end{pmatrix}.$$
   *(Colonnes : $f(u_1)$, $f(u_2)$, $f(u_3)$ ; lignes : $u_1$, $u_2$, $u_3$.)*
