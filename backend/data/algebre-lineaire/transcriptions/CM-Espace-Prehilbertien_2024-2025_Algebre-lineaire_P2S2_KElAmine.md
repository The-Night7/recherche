---
source: "PREING2-S2/Algebre-lineaire/CM-Espace-Prehilbertien_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf"
pages: 10
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Espace préhilbertien réel

Khalid El Amine I. — Department of Mathematics and Finance.

**Notations.** $\mathbb K$ désigne $\mathbb R$ ou $\mathbb C$ ; $E$ est un espace vectoriel réel.

> Transcription des dix pages. Les rubriques de preuve ou de solution laissées vides sont signalées. Dans les exemples intégrant sur $[a,b]$, l’hypothèse nécessaire $a<b$ est implicite dans le support.

## 1. Produit scalaire

### 1.1. Définition (pages 1 et 2)

**Définition 1.1.** Un **produit scalaire** sur $E$ est une forme bilinéaire symétrique positive définie. On abrège en **p.s.**

**Notation.** On note souvent $\varphi(x,y)$ par $\langle x,y\rangle$, $(x\mid y)$ ou $x.y$.

**Remarque.** Un produit scalaire sur $E$ induit naturellement un produit scalaire sur tout sous-espace de $E$.

**Exemple.** Pour $x=(x_1,\ldots,x_n)$ et $y=(y_1,\ldots,y_n)\in\mathbb R^n$, montrer que

$$
\langle x,y\rangle=\sum_{k=1}^n x_ky_k
$$

est un produit scalaire.

**Solution.** Pour $x,x',y\in\mathbb R^n$ et $\alpha\in\mathbb R$ :

1. $\langle x,y\rangle$ est réel comme somme finie de réels. C’est une forme sur $\mathbb R^n\times\mathbb R^n$.
2. $\langle x,y\rangle=\sum_{k=1}^n x_ky_k=\sum_{k=1}^n y_kx_k=\langle y,x\rangle$ : elle est symétrique.
3. La linéarité à gauche découle de

$$
\langle\alpha x+x',y\rangle=\sum_{k=1}^n(\alpha x_k+x'_k)y_k
=\alpha\sum_{k=1}^n x_ky_k+\sum_{k=1}^n x'_ky_k
=\alpha\langle x,y\rangle+\langle x',y\rangle.
$$

Par symétrie, elle est aussi linéaire à droite, donc bilinéaire.

4. $\langle x,x\rangle=\sum_{k=1}^n x_k^2\ge0$ : elle est positive.
5. $\langle x,x\rangle=0\iff\sum_{k=1}^n x_k^2=0\iff x_k=0$ pour tout $k\iff x=(0,\ldots,0)$ : elle est définie.

C’est donc un produit scalaire, appelé **produit scalaire canonique sur $\mathbb R^n$**.

**Remarque.** Sa matrice dans la base canonique est $I_n$, symétrique positive définie ; cela donne aussi une preuve matricielle.

### 1.2. Exemples fondamentaux (page 2)

Sur $\mathbb R^n$, pour $x=(x_k)$ et $y=(y_k)$ :

$$
\langle x,y\rangle=\sum_{k=1}^n x_ky_k.
$$

Sur $M_{n,1}(\mathbb R)$, pour $X=[x_k]$ et $Y=[y_k]$ :

$$
\langle X,Y\rangle=X^TY=\sum_{k=1}^n x_ky_k.
$$

Sur $M_{n,p}(\mathbb R)$, pour $A=[a_{ij}]$ et $B=[b_{ij}]$ :

$$
\langle A,B\rangle=\operatorname{tr}(A^TB)=\sum_{j=1}^p\sum_{i=1}^n a_{ij}b_{ij}.
$$

Sur $\mathbb R_n[X]$, pour $P=\sum_{k=0}^n a_kX^k$ et $Q=\sum_{k=0}^n b_kX^k$ :

$$
\langle P,Q\rangle=\sum_{k=0}^n a_kb_k.
$$

Sur $C([a,b],\mathbb R)$, pour $f,g$ continues :

$$
\langle f,g\rangle=\int_a^b f(t)g(t)\,dt.
$$

Le support appelle chacun de ces produits « produit scalaire canonique » sur l’espace considéré.

### 1.3. Inégalités de Schwarz et de Minkowski (pages 2 et 3)

**Théorème 1.2 — Inégalité de Schwarz.** Pour tout produit scalaire sur $E$ et tous $x,y\in E$,

$$
\langle x,y\rangle^2\le\langle x,x\rangle\langle y,y\rangle.
$$

Il y a égalité si et seulement si $x,y$ sont liés. Par passage à la racine,

$$
|\langle x,y\rangle|\le\sqrt{\langle x,x\rangle}\sqrt{\langle y,y\rangle}.
$$

*Preuve : non renseignée dans la source.*

**Exemples.** Dans les trois espaces munis des produits canoniques :

$$
\left(\sum_{k=1}^n x_ky_k\right)^2\le
\left(\sum_{k=1}^n x_k^2\right)\left(\sum_{k=1}^n y_k^2\right),\qquad x,y\in\mathbb R^n,
$$

$$
\bigl(\operatorname{tr}(A^TB)\bigr)^2\le\operatorname{tr}(A^TA)\operatorname{tr}(B^TB),\qquad A,B\in M_{n,p}(\mathbb R),
$$

$$
\left(\int_a^b f(t)g(t)\,dt\right)^2\le
\left(\int_a^b f(t)^2\,dt\right)\left(\int_a^b g(t)^2\,dt\right),\qquad f,g\in C([a,b],\mathbb R).
$$

**Théorème 1.3 — Inégalité de Minkowski.** Pour tous $x,y\in E$,

$$
\sqrt{\langle x+y,x+y\rangle}\le\sqrt{\langle x,x\rangle}+\sqrt{\langle y,y\rangle}.
$$

Il y a égalité si et seulement si $x,y$ sont **positivement liés**.

**Rappel.** Cela signifie qu’il existe $\lambda\ge0$ tel que $x=\lambda y$ ou $y=\lambda x$. C’est équivalent à : $x=0$, ou $y=0$, ou $x,y\ne0$ et $y=\lambda x$ pour un $\lambda>0$.

*Preuve : non renseignée dans la source.*

### 1.4. Norme associée (page 3)

**Définition 1.4 — Norme.** Une fonction $N:E\to\mathbb R$, sur un $\mathbb K$-espace vectoriel, est une norme si :

1. $N(x)=0\iff x=0_E$ (**séparation**).
2. $N(\lambda x)=|\lambda|N(x)$ pour $x\in E$, $\lambda\in\mathbb K$ (**homogénéité**).
3. $N(x+y)\le N(x)+N(y)$ pour tous $x,y\in E$ (**inégalité triangulaire**).

Un espace muni d’une norme est un **espace vectoriel normé**, noté $(E,N)$.

**Théorème 1.5.** Si $\langle\cdot,\cdot\rangle$ est un produit scalaire, l’application

$$
\|x\|=\sqrt{\langle x,x\rangle},\qquad x\in E,
$$

est une norme, appelée **norme associée au produit scalaire**.

*Preuve : non renseignée dans la source.*

### 1.5. Exemples de normes associées (page 4)

Dans $\mathbb R^n$ :

$$
\|x\|=\left(\sum_{k=1}^n x_k^2\right)^{1/2}.
$$

Dans $M_{n,p}(\mathbb R)$ :

$$
\|A\|=\bigl(\operatorname{tr}(A^TA)\bigr)^{1/2}
=\left(\sum_{j=1}^p\sum_{i=1}^n a_{ij}^2\right)^{1/2}.
$$

Dans $C([a,b],\mathbb R)$ :

$$
\|f\|=\left(\int_a^b f(t)^2\,dt\right)^{1/2}.
$$

## 2. Espace préhilbertien réel

### 2.1. Définitions (page 4)

**Définition 2.1.** Un espace vectoriel réel muni d’un produit scalaire est un **espace préhilbertien réel**, noté $(E,\langle\cdot,\cdot\rangle)$, abrégé **e.p.r.**

**Définition 2.2.** Un espace préhilbertien réel de dimension finie est un **espace euclidien**.

### 2.2. Inégalités et identités (pages 4 et 5)

**Convention.** La norme associée est appelée **norme préhilbertienne**, ou **norme euclidienne** si $\dim E<\infty$.

Les théorèmes précédents se reformulent avec $\|x\|=\sqrt{\langle x,x\rangle}$.

**Théorème 2.3 — Schwarz.** $|\langle x,y\rangle|\le\|x\|\|y\|$, avec égalité si et seulement si $x,y$ sont liés.

**Théorème 2.4 — Minkowski.** $\|x+y\|\le\|x\|+\|y\|$, avec égalité si et seulement si $x,y$ sont positivement liés, c’est-à-dire $x=\lambda y$ ou $y=\lambda x$ pour un $\lambda\ge0$.

**Proposition 2.5 — Identités remarquables.**

$$
\|x+y\|^2=\|x\|^2+2\langle x,y\rangle+\|y\|^2,\qquad
\|x-y\|^2=\|x\|^2-2\langle x,y\rangle+\|y\|^2.
$$

**Preuve.**

$$
\begin{aligned}
\|x+y\|^2&=\langle x+y,x+y\rangle=\langle x,x\rangle+2\langle x,y\rangle+\langle y,y\rangle,\\
\|x-y\|^2&=\langle x-y,x-y\rangle=\langle x,x\rangle-2\langle x,y\rangle+\langle y,y\rangle.
\end{aligned}
$$

**Proposition 2.6 — Identité du parallélogramme.**

$$
\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2).
$$

**Preuve.** Additionner les deux identités remarquables.

**Interprétation de la source.** Dans un parallélogramme, la somme des carrés des diagonales est égale à deux fois la somme des carrés des côtés. « Faire un dessin. »

> Ici, « les côtés » doit se comprendre comme les deux côtés adjacents de longueurs $\|x\|$ et $\|y\|$ ; si l’on somme les quatre côtés, le facteur 2 est déjà inclus. Aucun dessin n’est fourni dans le PDF.

**Remarque importante.** Toute norme vérifiant l’identité du parallélogramme est préhilbertienne. L’identité permet donc de déterminer si une norme est associée à un produit scalaire.

**Proposition 2.7 — Identités de polarisation.**

$$
\langle x,y\rangle=\frac12(\|x+y\|^2-\|x\|^2-\|y\|^2)
=\frac14(\|x+y\|^2-\|x-y\|^2).
$$

**Preuve.** À partir des identités remarquables.

**Remarque.** L’une ou l’autre des identités reconstitue le produit scalaire à partir de la norme associée.

**Note.** Tout e.p.r. est un espace vectoriel normé, puisqu’un produit scalaire fournit une norme. Réciproquement, si une norme vérifie l’identité du parallélogramme, l’espace peut être muni du produit scalaire obtenu par polarisation.

## 3. Orthogonalité

### 3.1. Définitions et généralités (pages 5 à 7)

**Définition 3.1.** Dans un e.p.r., $x,y$ sont **orthogonaux**, noté $x\perp y$, si $\langle x,y\rangle=0$.

**Remarques.** Par symétrie, dire que $x$ est orthogonal à $y$ équivaut à dire que $y$ est orthogonal à $x$. La notion dépend du produit scalaire : deux vecteurs peuvent être orthogonaux pour l’un et pas pour l’autre.

**Définition 3.2.** Un vecteur est **isotrope** s’il est orthogonal à lui-même : $\langle x,x\rangle=0$.

**Propriétés 3.3.** Le vecteur nul est orthogonal à tous les vecteurs. C’est le seul vecteur isotrope d’un e.p.r.

*Preuve : non renseignée dans la source.*

**Définition 3.4.** Pour $A\subset E$, on dit que $x\perp A$ si $\langle x,y\rangle=0$ pour tout $y\in A$. Pour $A,B\subset E$, on dit que $A\perp B$ si $\langle x,y\rangle=0$ pour tous $x\in A$ et $y\in B$.

**Proposition 3.5.** Si $F=\operatorname{Vect}(v_1,\ldots,v_p)$, alors

$$
x\perp F\iff x\perp v_i\text{ pour tout }i\in\{1,\ldots,p\}.
$$

*Preuve : non renseignée dans la source.*

**Proposition 3.6.** Si $F=\operatorname{Vect}(u_1,\ldots,u_p)$ et $G=\operatorname{Vect}(v_1,\ldots,v_q)$,

$$
F\perp G\iff\langle u_i,v_j\rangle=0\text{ pour tous }1\le i\le p,\ 1\le j\le q.
$$

*Preuve : non renseignée dans la source.*

**Exemple.** Dans $\mathbb R^4$ muni du produit scalaire usuel, on pose

$$
F=\operatorname{Vect}((1,0,0,1),(0,1,0,1)),\qquad
G=\operatorname{Vect}((0,0,1,0),(1,1,0,-1)).
$$

Montrer que $F\perp G$.

*Solution : non renseignée dans la source.*

**Définition 3.7.** L’**orthogonal** d’une partie $A\subset E$ est

$$
A^\perp=\{x\in E:\forall y\in A,\ \langle x,y\rangle=0\}.
$$

**Proposition 3.8.** $A^\perp$ est un sous-espace vectoriel de $E$.

**Remarque.** Cela reste vrai même si $A$ n’est pas un sous-espace.

*Preuve : non renseignée dans la source.*

**Propriétés 3.9.** $\{0_E\}^\perp=E$ et $E^\perp=\{0_E\}$.

**Preuve.** Pour tout $x$, $\langle x,0_E\rangle=0$, ce qui donne la première égalité. Si $x\in E^\perp$, alors $\langle x,y\rangle=0$ pour tout $y\in E$, en particulier $\langle x,x\rangle=0$, donc $x=0_E$.

**Proposition 3.10.** $A^\perp=(\operatorname{Vect}(A))^\perp$, où $\operatorname{Vect}(A)$ est le sous-espace engendré par $A$.

*Preuve : non renseignée dans la source.*

**Exemple.** Dans l’espace euclidien usuel $\mathbb R^3$, déterminer $F^\perp$ pour $F=\operatorname{Vect}((1,0,-1),(-1,1,0))$.

*Solution : non renseignée dans la source.*

**Remarque.** Deux parties orthogonales ne sont pas nécessairement l’orthogonal l’une de l’autre. Penser à deux droites perpendiculaires dans $\mathbb R^3$.

**Exemple.** Dans $\mathbb R^3$ usuel,

$$
D_1=\operatorname{Vect}((1,0,0))=\{(a,0,0):a\in\mathbb R\},\qquad
D_2=\operatorname{Vect}((0,1,0))=\{(0,b,0):b\in\mathbb R\}.
$$

$D_1\perp D_2$ car $\langle(1,0,0),(0,1,0)\rangle=0$, mais

$$
D_1^\perp=P=\operatorname{Vect}((0,1,0),(0,0,1))=\{(0,b,c):b,c\in\mathbb R\}.
$$

**Proposition 3.11.** Pour tout sous-espace $F$,

$$
F\cap F^\perp=\{0_E\},\qquad F\perp F^\perp,\qquad F\subset(F^\perp)^\perp.
$$

*Preuve : non renseignée dans la source.*

### 3.2. Familles orthogonales et orthonormales (page 8)

**Définition 3.12.** Pour un ensemble d’indices quelconque $I$, une famille $(x_i)_{i\in I}$ est **orthogonale** si $i\ne j\implies\langle x_i,x_j\rangle=0$. Elle est **orthonormale** si elle est orthogonale et $\|x_i\|=1$ pour tout $i$.

Si cette famille est une base, on parle de **base orthogonale** ou **base orthonormale**, abrégée **b.o.n.**

**Note.** Le delta de Kronecker est

$$
\delta_{ij}=\begin{cases}0&\text{si }i\ne j,\\1&\text{si }i=j.\end{cases}
$$

Une famille est donc orthonormale si $\langle x_i,x_j\rangle=\delta_{ij}$ pour tous $i,j\in I$.

**Proposition 3.13.** Toute famille orthogonale de vecteurs **tous non nuls** est libre.

**Preuve.** Soit $J\subset I$ fini. Si $\sum_{j\in J}\alpha_jx_j=0_E$, alors pour $k\in J$,

$$
0=\langle0_E,x_k\rangle
=\left\langle\sum_{j\in J}\alpha_jx_j,x_k\right\rangle
=\sum_{j\in J}\alpha_j\langle x_j,x_k\rangle
=\alpha_k\langle x_k,x_k\rangle=\alpha_k\|x_k\|^2.
$$

Comme $\|x_k\|\ne0$, on a $\alpha_k=0$.

**Théorème 3.14 — Pythagore.**

$$
x\perp y\iff\|x+y\|^2=\|x\|^2+\|y\|^2.
$$

**Preuve.** L’identité remarquable donne

$$
\begin{aligned}
x\perp y&\iff\langle x,y\rangle=0\\
&\iff\|x\|^2+\|y\|^2+2\langle x,y\rangle=\|x\|^2+\|y\|^2\\
&\iff\|x+y\|^2=\|x\|^2+\|y\|^2.
\end{aligned}
$$

**Proposition 3.15.** Pour $p\in\mathbb N^*$ et une famille de $p$ vecteurs,

$$
(x_i)_{1\le i\le p}\text{ orthogonale}\implies
\left\|\sum_{i=1}^p x_i\right\|^2=\sum_{i=1}^p\|x_i\|^2.
$$

La réciproque est fausse pour $p\ge3$.

*Preuve : non renseignée dans la source.*

### 3.3. Procédé de Gram–Schmidt (page 9)

**Théorème 3.16.** Soit $(v_1,\ldots,v_p)$ une famille libre d’un e.p.r. La famille définie par

$$
q_1=v_1,\qquad q_k=v_k-\sum_{i=1}^{k-1}\frac{\langle v_k,q_i\rangle}{\|q_i\|^2}q_i
\quad(2\le k\le p)
$$

est orthogonale et vérifie

$$
\operatorname{Vect}(v_1,\ldots,v_p)=\operatorname{Vect}(q_1,\ldots,q_p).
$$

Pour obtenir une famille orthonormale, on normalise :

$$
\varepsilon_i=\frac{q_i}{\|q_i\|},\qquad1\le i\le p.
$$

*Preuve : non renseignée dans la source.*

**Exemple.** Dans $\mathbb R^4$ canonique, soit $F=\operatorname{Vect}(v_1,v_2,v_3)$ avec $v_1=(0,0,1,1)$, $v_2=(0,0,1,0)$, $v_3=(1,1,1,0)$. Déterminer une base orthonormale de $F$.

*Solution : non renseignée dans la source.*

### 3.4. Base orthonormale et espace euclidien (pages 9 et 10)

**Définition 3.17.** Un espace euclidien est un espace vectoriel réel de dimension finie muni d’un produit scalaire.

**Proposition 3.18.** Tout espace euclidien admet une base orthonormale.

**Preuve.** Partir d’une base quelconque et appliquer le procédé d’orthonormalisation de Gram–Schmidt.

**Exemples dans les espaces canoniques.** La base canonique de $\mathbb R^n$ est orthonormale. Dans $\mathbb R^2$,

$$
\varepsilon_1=\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix},\qquad
\varepsilon_2=\begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix},\qquad \theta\in[0,2\pi[
$$

forment une base orthonormale. Dans $\mathbb R^3$,

$$
\varepsilon_1=\begin{pmatrix}\cos\theta\cos\varphi\\\sin\theta\cos\varphi\\\sin\varphi\end{pmatrix},\quad
\varepsilon_2=\begin{pmatrix}\cos\theta\sin\varphi\\\sin\theta\sin\varphi\\-\cos\varphi\end{pmatrix},\quad
\varepsilon_3=\begin{pmatrix}-\sin\theta\\\cos\theta\\0\end{pmatrix}
$$

forment une base orthonormale, avec $\theta\in[0,2\pi[$ et $\varphi\in[-\pi/2,\pi/2[$.

**Théorème 3.19.** Toute famille orthonormale d’un espace euclidien peut être complétée en une base orthonormale.

**Preuve.** Utiliser le théorème de la base incomplète, puis orthonormaliser les vecteurs ajoutés par Gram–Schmidt.

**Proposition 3.20.** Soit $\mathcal B$ une base et $A=M_{\mathcal B}(\langle\cdot,\cdot\rangle)$.

- $\mathcal B$ est orthogonale si et seulement si $A\in D_n(\mathbb R)$, l’ensemble des matrices diagonales.
- $\mathcal B$ est orthonormale si et seulement si $A=I_n$.

**Preuve.** Si $\mathcal B=(e_i)_{1\le i\le n}$, alors $A=[\langle e_i,e_j\rangle]_{1\le i,j\le n}$.

**Proposition 3.21.** Dans une base orthonormale, avec $X=M_{\mathcal B}(x)$ et $Y=M_{\mathcal B}(y)$,

$$
\langle x,y\rangle=X^TY.
$$

**Preuve.** La matrice du produit scalaire est $I_n$.

**Remarque importante.** Dans une b.o.n., le produit scalaire s’exprime comme le produit scalaire usuel de $\mathbb R^n$.

**Proposition 3.22 — Règles de calcul.** Si $\mathcal B=(e_1,\ldots,e_n)$ est orthonormale, alors

$$
x=\sum_{i=1}^n\langle x,e_i\rangle e_i,\qquad
\|x\|^2=\sum_{i=1}^n\langle x,e_i\rangle^2,\qquad
\langle x,y\rangle=\sum_{i=1}^n\langle x,e_i\rangle\langle y,e_i\rangle.
$$

*Preuve : non renseignée dans la source.*
