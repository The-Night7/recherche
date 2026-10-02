---
source: "PREING2-S2/Algebre-lineaire-DS/DS1-2018-2019-Correction_Algebre-lineaire-DS_P2S2_KFayad.pdf"
pages: 3
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Corrigé DS1 — Algèbre linéaire et bilinéaire — Prépa 2

15 mars 2019. Karam Fayad — `karam.fayad@eisti.eu`.

## Exercice 1 — Endomorphisme de $\mathbb R_2[X]$ (pages 1 et 2)

### 1. Stabilité et linéarité

Soit $P=a+bX+cX^2\in\mathbb R_2[X]$. Alors

$$
f(P)=(b-2c)+(2b+2c)X+6cX^2\in\mathbb R_2[X].
$$

Montrons que $f$ est linéaire. Pour $\lambda\in\mathbb R$ et $(P,Q)\in\mathbb R_2[X]^2$,

$$
\begin{aligned}
f(\lambda P+Q)&=(X^2-1)(\lambda P+Q)''+(2X+1)(\lambda P+Q)'\\
&=(X^2-1)(\lambda P''+Q'')+(2X+1)(\lambda P'+Q')\\
&=\lambda[(X^2-1)P''+(2X+1)P']+(X^2-1)Q''+(2X+1)Q'\\
&=\lambda f(P)+f(Q).
\end{aligned}
$$

### 2. Matrice dans la base canonique

On a $f(1)=0$, $f(X)=1+2X$ et $f(X^2)=-2+2X+6X^2$. La matrice de $f$ dans la base canonique $(1,X,X^2)$ est donc

$$
A=\begin{pmatrix}0&1&-2\\0&2&2\\0&0&6\end{pmatrix}.
$$

### 3. Valeurs propres

La matrice $A$ est triangulaire supérieure. Son polynôme caractéristique, qui est aussi celui de $f$, est

$$
P_A(X)=-X(X-2)(X-6).
$$

Les valeurs propres sont $\lambda_1=0$, $\lambda_2=2$ et $\lambda_3=6$. Elles sont toutes simples.

### 4. Polynômes propres

Pour $\lambda_1=0$, il suffit de prendre $P_1=1$.

Soit $P_2=a+bX+cX^2$ tel que $f(P_2)=2P_2$. L’équation $(f-2\operatorname{id})(P_2)=0$ s’écrit

$$
(A-2I_3)\begin{pmatrix}a\\b\\c\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}
\iff c=0\text{ et }b=2a.
$$

Donc $P_2=a(1+2X)$. On prend par exemple $P_2=1+2X$.

De même, pour $P_3=a+bX+cX^2$ tel que $f(P_3)=6P_3$,

$$
(A-6I_3)\begin{pmatrix}a\\b\\c\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}
\iff c=-4a\text{ et }b=-2a.
$$

Donc $P_3=a(1-2X-4X^2)$. On prend $P_3=1-2X-4X^2$.

### 5. Base de polynômes propres

Les polynômes $P_1,P_2,P_3$ sont non nuls et de degrés deux à deux distincts. Ils forment donc une famille libre de $\mathbb R_2[X]$. Cet espace étant de dimension 3, $\mathcal C=(P_1,P_2,P_3)$ est une base.

### 6. Matrice dans la base $\mathcal C$

Par construction,

$$
\operatorname{Mat}_{\mathcal C}(f)=\begin{pmatrix}0&0&0\\0&2&0\\0&0&6\end{pmatrix}.
$$

### 7. Image et noyau

**a.** Les polynômes $P_2,P_3$ ne sont pas colinéaires, donc $\operatorname{Vect}(P_2,P_3)$ est de dimension 2. D’autre part, $\operatorname{rg}(A)=\operatorname{rg}(f)=2$, donc $\operatorname{Im}(f)$ est de dimension 2.

Comme $f(P_2)=2P_2$, on a $2P_2\in\operatorname{Im}(f)$, puis $P_2\in\operatorname{Im}(f)$ puisque l’image est un sous-espace vectoriel. De même, $P_3\in\operatorname{Im}(f)$. On obtient $\operatorname{Vect}(P_2,P_3)\subset\operatorname{Im}(f)$, puis, par égalité des dimensions,

$$
\operatorname{Im}(f)=\operatorname{Vect}(P_2,P_3).
$$

**b.** Le noyau est de dimension 1 et contient $P_1$, donc $\ker(f)=\operatorname{Vect}(P_1)$. La liberté de $(P_1,P_2,P_3)$ donne

$$
\ker(f)\cap\operatorname{Im}(f)=\operatorname{Vect}(P_1)\cap\operatorname{Vect}(P_2,P_3)=\{0\}.
$$

Le théorème du rang assure que $\dim\operatorname{Im}(f)+\dim\ker(f)=3=\dim\mathbb R_2[X]$. Ainsi, image et noyau sont supplémentaires.

**Remarque.** Comme $f$ possède trois valeurs propres simples, il est diagonalisable et $\mathbb R_2[X]$ est somme directe de ses sous-espaces propres :

$$
\mathbb R_2[X]=\operatorname{Vect}(P_1)\oplus\operatorname{Vect}(P_2)\oplus\operatorname{Vect}(P_3)
=\operatorname{Vect}(P_1)\oplus\operatorname{Vect}(P_2,P_3)=\ker(f)\oplus\operatorname{Im}(f).
$$

## Exercice 2 — Matrice dépendant de $a$ (page 2)

### 1. La valeur $a$ est propre

$$
\det(A-aI_3)
=\begin{vmatrix}-1-a&1+a&0\\1&0&1\\3&-1-a&2-a\end{vmatrix}
=\begin{vmatrix}-1-a&0&0\\1&1&1\\3&2-a&2-a\end{vmatrix}=0.
$$

On effectue $C_2\leftarrow C_2+C_1$, puis on constate que $C_2=C_3$. Ainsi, $a$ est une valeur propre de $A$.

### 2. Polynôme caractéristique

En développant selon la première ligne,

$$
\begin{aligned}
P_A(X)&=\det(A-XI_3)=\begin{vmatrix}-1-X&a+1&0\\1&a-X&1\\3&-1-a&2-X\end{vmatrix}\\
&=-(X+1)\bigl(X^2-(a+2)X+3a+1\bigr)-(a+1)(-X-1).
\end{aligned}
$$

On factorise par $X+1$ :

$$
P_A(X)=-(X+1)\bigl(X^2-(a+2)X+2a\bigr)=-(X+1)(X-2)(X-a).
$$

### 3. Rang de $A-aI_3$

Puisque $\det(A-aI_3)=0$, cette matrice n’est pas inversible et son rang est strictement inférieur à 3. Après échange des deux premières lignes,

$$
\begin{pmatrix}1&0&1\\-1-a&1+a&0\\3&-1-a&2-a\end{pmatrix}
\sim\begin{pmatrix}1&0&1\\0&1+a&1+a\\0&-1-a&-1-a\end{pmatrix}
\sim\begin{pmatrix}1&0&1\\0&1+a&1+a\\0&0&0\end{pmatrix}.
$$

On a effectué $L_2\leftarrow L_2+(1+a)L_1$ et $L_3\leftarrow L_3-3L_1$, puis $L_3\leftarrow L_3+L_2$. Par conséquent,

$$
\operatorname{rg}(A-aI_3)=\begin{cases}1&\text{si }a=-1,\\2&\text{si }a\ne-1.\end{cases}
$$

## Exercice 3 — Matrices semblables (pages 2 et 3)

### 1. Même polynôme caractéristique

Soient $A,B$ semblables et $P$ inversible telle que $A=PBP^{-1}$. Pour $\lambda\in\mathbb R$,

$$
\begin{aligned}
P_A(\lambda)&=\det(A-\lambda I_n)\\
&=\det(PBP^{-1}-\lambda I_n)\\
&=\det(PBP^{-1}-\lambda PI_nP^{-1})\\
&=\det\bigl(P(B-\lambda I_n)P^{-1}\bigr)\\
&=\det(P)\det(B-\lambda I_n)\det(P^{-1})\\
&=\det(P)\det(B-\lambda I_n)\det(P)^{-1}\\
&=\det(B-\lambda I_n)=P_B(\lambda).
\end{aligned}
$$

Les deux matrices ont donc le même polynôme caractéristique.

### 2. La réciproque est fausse

Posons

$$
A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$

On a $P_A(X)=P_B(X)=X^2$. Pourtant $A$ et $B$ ne sont pas semblables : toute matrice semblable à $B$ serait nulle.

## Exercice 4 — Endomorphisme défini avec la trace (page 3)

### 1. Linéarité

Pour $\lambda\in\mathbb R$ et $(M,N)\in M_n(\mathbb R)^2$, la linéarité de la trace donne

$$
\begin{aligned}
f(\lambda M+N)&=\operatorname{tr}(A)(\lambda M+N)-\operatorname{tr}(\lambda M+N)A\\
&=\lambda\operatorname{tr}(A)M+\operatorname{tr}(A)N-\lambda\operatorname{tr}(M)A-\operatorname{tr}(N)A\\
&=\lambda\bigl(\operatorname{tr}(A)M-\operatorname{tr}(M)A\bigr)+\operatorname{tr}(A)N-\operatorname{tr}(N)A\\
&=\lambda f(M)+f(N).
\end{aligned}
$$

Ainsi, $f$ est un endomorphisme de $M_n(\mathbb R)$.

### 2. Une valeur propre

$f(A)=\operatorname{tr}(A)A-\operatorname{tr}(A)A=0$. Comme $\operatorname{tr}(A)\ne0$, la matrice $A$ est non nulle : c’est un vecteur propre associé à $\alpha=0$.

### 3. Sous-espace propre pour $0$

Notons $E=\ker(f)$. Puisque $A\in E$, on a $\operatorname{Vect}(A)\subset E$. Réciproquement, si $M\in E$,

$$
f(M)=0\implies\operatorname{tr}(A)M-\operatorname{tr}(M)A=0
\implies M=\frac{\operatorname{tr}(M)}{\operatorname{tr}(A)}A\in\operatorname{Vect}(A).
$$

Donc $E=\operatorname{Vect}(A)$ et $\dim E=1$.

### 4. Sous-espace des matrices de trace nulle

Montrons que $F=\ker(f-\operatorname{tr}(A)\operatorname{id})$.

Si $M\in F$, alors $\operatorname{tr}(M)=0$, donc $f(M)=\operatorname{tr}(A)M$ et $(f-\operatorname{tr}(A)\operatorname{id})(M)=0$. Cela donne une inclusion.

Réciproquement, si $M\in\ker(f-\operatorname{tr}(A)\operatorname{id})$, alors $f(M)=\operatorname{tr}(A)M$, donc $\operatorname{tr}(M)A=0$. Comme $A\ne0$, on obtient $\operatorname{tr}(M)=0$ et $M\in F$.

On peut aussi raisonner par équivalences :

$$
M\in F\iff\operatorname{tr}(M)=0\iff f(M)=\operatorname{tr}(A)M
\iff M\in\ker(f-\operatorname{tr}(A)\operatorname{id}).
$$

### 5. Image et dimension

Si $M\in F$, alors $f(M)=\operatorname{tr}(A)M\in\operatorname{Im}(f)$. Puisque l’image est un sous-espace vectoriel et $\operatorname{tr}(A)\ne0$,

$$
M=(\operatorname{tr}(A))^{-1}\bigl(\operatorname{tr}(A)M\bigr)\in\operatorname{Im}(f).
$$

Donc $F\subset\operatorname{Im}(f)$.

Réciproquement, si $M\in\operatorname{Im}(f)$, il existe $N\in M_n(\mathbb R)$ tel que $M=f(N)=\operatorname{tr}(A)N-\operatorname{tr}(N)A$. Ainsi,

$$
\operatorname{tr}(M)=\operatorname{tr}\bigl(\operatorname{tr}(A)N-\operatorname{tr}(N)A\bigr)
=\operatorname{tr}(A)\operatorname{tr}(N)-\operatorname{tr}(N)\operatorname{tr}(A)=0.
$$

Donc $M\in F$ et $\operatorname{Im}(f)\subset F$. Finalement,

$$
F=\operatorname{Im}(f),\qquad \dim F=\dim\operatorname{Im}(f)=n^2-\dim\ker(f)=n^2-1.
$$

**Remarque.** Une matrice de trace nulle dépend de $n^2-1$ coefficients indépendants : la trace nulle impose une seule relation. On peut donc obtenir directement $\dim F=n^2-1$. Le théorème du rang donne la même dimension pour $\operatorname{Im}(f)$ ; une seule des deux inclusions suffit alors à conclure à l’égalité.
