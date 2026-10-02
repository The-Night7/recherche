---
source: "PREING2-S2/Algebre-lineaire/CM-Forme-bilineaire_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf"
pages: 9
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Forme bilinéaire

Khalid El Amine I. — Department of Mathematics and Finance.

**Notations et conventions.** $\mathbb K$ désigne $\mathbb R$ ou $\mathbb C$ ; $E$ désigne un espace vectoriel sur $\mathbb R$.

> Transcription des neuf pages. Les preuves et solutions laissées vides dans le support sont indiquées explicitement.

## 1. Forme (page 1)

**Définition 1.1 — Forme.** Soit $V$ un $\mathbb K$-espace vectoriel. Toute application $\varphi:V\to\mathbb K$ est appelée **forme sur $V$**.

**Remarques.** En général, une forme est une application d’un espace vectoriel dans son corps de base. En analyse, une application d’un $\mathbb K$-espace vectoriel $V$ à valeurs dans $\mathbb R$ est appelée **fonctionnelle** ; $V$ est souvent un espace de fonctions.

**Définition 1.2 — Forme symétrique et antisymétrique.** Soit $\varphi:V\times V\to\mathbb K$.

- $\varphi$ est **symétrique** si $\varphi(x,y)=\varphi(y,x)$ pour tous $x,y\in V$.
- $\varphi$ est **antisymétrique** si $\varphi(x,y)=-\varphi(y,x)$ pour tous $x,y\in V$.

**Exemple.** Pour $x=(x_1,x_2)$ et $y=(y_1,y_2)$ dans $\mathbb R^2$, soit $\varphi(x,y)=x_1y_2+x_2y_1$. Montrer qu’elle est symétrique.

**Solution.** Pour tous $x,y\in\mathbb R^2$,

$$
\varphi(x,y)=x_1y_2+x_2y_1=y_1x_2+y_2x_1=\varphi(y,x).
$$

**Exemple.** Soit maintenant $\varphi(x,y)=x_1y_2-x_2y_1$. Montrer qu’elle est antisymétrique.

**Solution.** Pour tous $x,y\in\mathbb R^2$,

$$
\varphi(x,y)=x_1y_2-x_2y_1=y_2x_1-y_1x_2=-(y_1x_2-y_2x_1)=-\varphi(y,x).
$$

## 2. Forme linéaire

### 2.1. Définition (page 2)

**Définition 2.1.** Une **forme linéaire** sur un $\mathbb K$-espace vectoriel $V$ est une application linéaire de $V$ dans $\mathbb K$, c’est-à-dire $\varphi\in\mathcal L(V,\mathbb K)$.

**Exemple.** Soient $a_1,a_2\in\mathbb R$ fixés et $\varphi(x)=a_1x_1+a_2x_2$ pour $x=(x_1,x_2)\in\mathbb R^2$. Montrer que $\varphi$ est une forme linéaire.

**Solution.** Pour tout $x$, $a_1x_1+a_2x_2$ est réel, comme somme finie de réels : $\varphi$ est une forme. Pour $x,x'\in\mathbb R^2$ et $\alpha,\beta\in\mathbb R$,

$$
\begin{aligned}
\varphi(\alpha x+\beta x')
&=\varphi(\alpha(x_1,x_2)+\beta(x'_1,x'_2))\\
&=\varphi((\alpha x_1+\beta x'_1,\alpha x_2+\beta x'_2))\\
&=a_1(\alpha x_1+\beta x'_1)+a_2(\alpha x_2+\beta x'_2)\\
&=\alpha(a_1x_1+a_2x_2)+\beta(a_1x'_1+a_2x'_2)\\
&=\alpha\varphi(x)+\beta\varphi(x').
\end{aligned}
$$

Elle est donc linéaire, ce qui conclut.

**Remarque.** Toute forme linéaire sur $\mathbb R^n$ s’écrit, avec des coefficients réels fixés,

$$
\varphi(x)=a_1x_1+\cdots+a_nx_n,\qquad x=(x_1,\ldots,x_n)\in\mathbb R^n.
$$

$[a_1\ \cdots\ a_n]$ est sa matrice dans les bases canoniques de $\mathbb R^n$ et $\mathbb R$.

**Exercice.** Montrer que $\varphi(A)=\operatorname{tr}(A)$ est une forme linéaire sur $M_n(\mathbb R)$.

**Solution.** $M_n(\mathbb R)$ est un espace vectoriel réel. Pour $A=[a_{ij}]$,

$$
\varphi(A)=\sum_{i=1}^n a_{ii}\in\mathbb R,
$$

car c’est une somme finie de réels. Pour $A=[a_{ij}],B=[b_{ij}]$ et $\alpha,\beta\in\mathbb R$, on a $\alpha A+\beta B=[\alpha a_{ij}+\beta b_{ij}]$, donc

$$
\begin{aligned}
\varphi(\alpha A+\beta B)&=\operatorname{tr}(\alpha A+\beta B)\\
&=\sum_{i=1}^n(\alpha a_{ii}+\beta b_{ii})\\
&=\alpha\sum_{i=1}^n a_{ii}+\beta\sum_{i=1}^n b_{ii}\\
&=\alpha\operatorname{tr}(A)+\beta\operatorname{tr}(B)=\alpha\varphi(A)+\beta\varphi(B).
\end{aligned}
$$

La trace est donc une forme linéaire.

### 2.2. Hyperplan (page 3)

**Définition 2.2.** Un **hyperplan** d’un $\mathbb K$-espace vectoriel $V$ est le noyau d’une forme linéaire non nulle sur $V$.

**Exemple.** Déterminer l’hyperplan associé à $\varphi(x)=x_1+x_2$ sur $\mathbb R^2$.

**Solution.** La forme est non nulle. Pour $x=(x_1,x_2)$,

$$
\begin{aligned}
x\in H&\iff x\in\ker\varphi\iff\varphi(x)=0\iff x_1+x_2=0\\
&\iff x_1=-x_2\iff x=(-x_2,x_2)=x_2(-1,1).
\end{aligned}
$$

Ainsi $H=\operatorname{Vect}\{(-1,1)\}$.

> Dans le couple intermédiaire, la seconde coordonnée est imprimée $x^2$ dans la source ; il s’agit de l’indice $x_2$, comme le montrent les égalités qui l’entourent.

**Remarque.** Un hyperplan est un sous-espace vectoriel, puisqu’il est le noyau d’une application linéaire.

**Théorème 2.3.** Soit $H$ un sous-espace de $V$. C’est un hyperplan si et seulement s’il existe une droite vectorielle $D$ de $V$ telle que $V=H\oplus D$.

*Preuve : non renseignée dans la source.*

**Corollaire 2.4.** Si $\dim V=n\ge1$, un sous-espace $H$ est un hyperplan si et seulement si $\dim H=n-1$.

*Preuve : non renseignée dans la source.*

## 3. Forme bilinéaire

### 3.1. Espace de dimension quelconque

Dans cette sous-section, $E$ est un espace vectoriel réel de dimension quelconque.

#### 3.1.1. Forme bilinéaire (pages 3 et 4)

**Définition 3.1.** Une **forme bilinéaire** sur $E$ est une application $\varphi:E\times E\to\mathbb R$ linéaire dans chacune des deux places :

$$
\forall x,x',y\in E,\ \forall\alpha,\beta\in\mathbb R,\quad
\varphi(\alpha x+\beta x',y)=\alpha\varphi(x,y)+\beta\varphi(x',y),
$$

$$
\forall x,y,y'\in E,\ \forall\alpha,\beta\in\mathbb R,\quad
\varphi(x,\alpha y+\beta y')=\alpha\varphi(x,y)+\beta\varphi(x,y').
$$

On note $\mathcal L_2(E\times E;\mathbb R)$ l’espace vectoriel réel des formes bilinéaires et on abrège « forme bilinéaire » en **f.b.**

**Remarque.** Attention : $\mathcal L_2(E\times E;\mathbb R)\ne\mathcal L(E\times E;\mathbb R)$.

**Exemple.** Donner un contre-exemple illustrant cette remarque.

*Solution : non renseignée dans la source.*

**Propriété 3.2.** Si $\varphi$ est bilinéaire, alors, pour tout $x\in E$,

$$
\varphi(x,0_E)=\varphi(0_E,x)=0.
$$

**Preuve.** La linéarité à droite donne

$$
\varphi(x,0_E)=\varphi(x,0_E+0_E)=\varphi(x,0_E)+\varphi(x,0_E)=2\varphi(x,0_E).
$$

Comme cette valeur est réelle, elle est nulle. L’autre égalité se démontre de même par linéarité à gauche.

**Proposition 3.3.** Pour une forme bilinéaire $\varphi$, pour $p,q\in\mathbb N^*$, des scalaires $\alpha_1,\ldots,\alpha_p,\beta_1,\ldots,\beta_q\in\mathbb R$ et des vecteurs $x_1,\ldots,x_p,y_1,\ldots,y_q\in E$,

$$
\varphi\left(\sum_{i=1}^p\alpha_i x_i,\sum_{j=1}^q\beta_j y_j\right)
=\sum_{i=1}^p\sum_{j=1}^q\alpha_i\beta_j\varphi(x_i,y_j).
$$

*Preuve : non renseignée dans la source.*

#### 3.1.2. Forme bilinéaire symétrique ou antisymétrique (pages 4 et 5)

**Proposition 3.4.** Une forme $\varphi:E\times E\to\mathbb R$ est bilinéaire symétrique si et seulement si elle est symétrique et linéaire dans la première place.

On note $\mathcal L_{2,s}(E\times E;\mathbb R)$ l’espace de ces formes ; l’abréviation est **f.b.s.**

**Preuve.** Simple vérification.

**Exemple.** $\varphi:\mathbb R\times\mathbb R\to\mathbb R$, $\varphi(x,y)=xy$, est une f.b.s. :

$$
\varphi(x,y)=xy=yx=\varphi(y,x),
$$

$$
\varphi(\alpha x+\beta x',y)=(\alpha x+\beta x')y=\alpha xy+\beta x'y
=\alpha\varphi(x,y)+\beta\varphi(x',y).
$$

La linéarité dans la première place et la symétrie donnent la bilinéarité.

**Proposition 3.5.** Une forme $\varphi:E\times E\to\mathbb R$ est bilinéaire antisymétrique si et seulement si elle est antisymétrique et linéaire dans la première place.

On note $\mathcal L_{2,a}(E\times E;\mathbb R)$ l’espace de ces formes ; l’abréviation est **f.b.a.**

**Preuve.** Simple vérification.

**Exercice.** Montrer que l’application déterminant sur $\mathbb R^2$ est une forme bilinéaire antisymétrique.

*Solution : non renseignée dans la source.*

**Proposition 3.6.** Les deux sous-espaces sont supplémentaires :

$$
\mathcal L_{2,s}(E\times E;\mathbb R)\oplus\mathcal L_{2,a}(E\times E;\mathbb R)
=\mathcal L_2(E\times E;\mathbb R).
$$

*Preuve : non renseignée dans la source.*

#### 3.1.3. Forme bilinéaire symétrique positive ou définie (page 5)

**Définition 3.7.** Une f.b.s. est **positive** si $\varphi(x,x)\ge0$ pour tout $x\in E$.

**Définition 3.8.** Une f.b.s. est **définie** si $\varphi(x,x)=0\implies x=0_E$ pour tout $x\in E$.

**Définition 3.9.** Une f.b.s. est **positive définie** si elle est positive et définie, c’est-à-dire

$$
\forall x\in E\setminus\{0_E\},\quad\varphi(x,x)>0.
$$

**Exemple.** Sur $\mathbb R^2$, soit $\varphi(x,y)=x_1y_1-x_2y_2$. Montrer que c’est une f.b.s. Est-elle positive ? Définie ?

*Solution : non renseignée dans la source.*

### 3.2. Espace de dimension finie

Dans cette sous-section, $n\in\mathbb N^*$ et $E$ est de dimension $n$.

#### 3.2.1. Matrice d’une forme bilinéaire (pages 6 et 7)

Soit $\mathcal B=(e_1,\ldots,e_n)$ une base de $E$. Pour $x\in E$, on note

$$
X=M_{\mathcal B}(x)=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

le vecteur colonne de ses composantes dans cette base.

**Définition 3.10.** La matrice d’une f.b. $\varphi$ dans $\mathcal B$ est

$$
M_{\mathcal B}(\varphi)=[\varphi(e_i,e_j)]_{1\le i,j\le n}
=\begin{pmatrix}
\varphi(e_1,e_1)&\cdots&\varphi(e_1,e_n)\\
\vdots&\ddots&\vdots\\
\varphi(e_n,e_1)&\cdots&\varphi(e_n,e_n)
\end{pmatrix}.
$$

**Exemple.** Dans la base canonique de $\mathbb R^2$, pour $a,b,c,d\in\mathbb R$,

$$
\varphi((x_1,x_2),(y_1,y_2))=ax_1y_1+bx_1y_2+cx_2y_1+dx_2y_2
$$

est bilinéaire et

$$
M_{\mathcal B}(\varphi)=\begin{pmatrix}\varphi(e_1,e_1)&\varphi(e_1,e_2)\\\varphi(e_2,e_1)&\varphi(e_2,e_2)\end{pmatrix}
=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
$$

**Proposition 3.11.** Si $A=M_{\mathcal B}(\varphi)$, alors, pour tous $x,y\in E$,

$$
\varphi(x,y)=X^TAY,\qquad X=M_{\mathcal B}(x),\quad Y=M_{\mathcal B}(y).
$$

*Preuve : non renseignée dans la source.*

**Remarque.** Réciproquement, toute matrice $A\in M_n(\mathbb R)$ définit une forme bilinéaire par $\varphi(x,y)=X^TAY$.

**Proposition 3.12.** Pour une base $\mathcal B$ fixée, l’application

$$
M_{\mathcal B}:\mathcal L_2(E\times E;\mathbb R)\longrightarrow M_n(\mathbb R),
\qquad \varphi\longmapsto M_{\mathcal B}(\varphi)
$$

est un isomorphisme d’espaces vectoriels.

*Preuve : non renseignée dans la source.*

**Remarque.** Une application sur $E\times E$ est bilinéaire si et seulement s’il existe $A\in M_n(\mathbb R)$ telle que $\varphi(x,y)=X^TAY$ pour tous $x,y\in E$. En particulier,

$$
\varphi\text{ f.b. sur }\mathbb R^n
\iff\exists(a_{ij})_{1\le i,j\le n}\in\mathbb R^{n^2},\quad
\forall x,y\in\mathbb R^n,\quad\varphi(x,y)=\sum_{1\le i,j\le n}a_{ij}x_i y_j.
$$

**Exemple.** Définir la f.b. de matrice $A=\begin{pmatrix}-1&3\\2&5\end{pmatrix}$ dans la base canonique de $\mathbb R^2$.

**Solution.** Pour $x=(x_1,x_2)$ et $y=(y_1,y_2)$,

$$
\begin{aligned}
\varphi(x,y)&=X^TAY
=\begin{pmatrix}x_1&x_2\end{pmatrix}\begin{pmatrix}-1&3\\2&5\end{pmatrix}\begin{pmatrix}y_1\\y_2\end{pmatrix}\\
&=\begin{pmatrix}x_1&x_2\end{pmatrix}\begin{pmatrix}-y_1+3y_2\\2y_1+5y_2\end{pmatrix}\\
&=-x_1y_1+3x_1y_2+2x_2y_1+5x_2y_2.
\end{aligned}
$$

**Proposition 3.13 — Changement de base.** Soient $\mathcal B,\mathcal B'$ deux bases et $P=P_{(\mathcal B,\mathcal B')}$ la matrice de passage. Si $A=M_{\mathcal B}(\varphi)$ et $A'=M_{\mathcal B'}(\varphi)$, alors

$$
A'=P^TAP.
$$

**Preuve.** Avec $X=M_{\mathcal B}(x)$ et $X'=M_{\mathcal B'}(x)$, on a $X=PX'$. Donc

$$
\varphi(x,y)=X^TAY=(PX')^TA(PY')=(X')^T(P^TAP)Y'.
$$

L’unicité de la matrice de $\varphi$ dans $\mathcal B'$ donne le résultat.

**Exemple.** Soit $A=\begin{pmatrix}0&0\\1&1\end{pmatrix}$ dans la base canonique et $\mathcal B'=(v_1,v_2)$, avec $v_1=(1,1)$ et $v_2=(-1,1)$. Déterminer $A'$.

**Solution.** $P=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$, d’où

$$
A'=P^TAP
=\begin{pmatrix}1&1\\-1&1\end{pmatrix}
\begin{pmatrix}0&0\\1&1\end{pmatrix}
\begin{pmatrix}1&-1\\1&1\end{pmatrix}
=\begin{pmatrix}2&0\\2&0\end{pmatrix}.
$$

**Définition 3.14.** Deux matrices $M,M'\in M_n(\mathbb R)$ sont **congrues** s’il existe une matrice inversible $P$ telle que $M'=P^TMP$.

**Remarque.** Elles représentent alors la même forme bilinéaire dans deux bases différentes.

#### 3.2.2. Matrice d’une forme symétrique ou antisymétrique (pages 7 et 8)

**Proposition 3.15.** Dans n’importe quelle base de $E$, une f.b. est symétrique si et seulement si sa matrice est symétrique ; elle est antisymétrique si et seulement si sa matrice est antisymétrique.

*Preuve : non renseignée dans la source.*

**Exercice.** Construire une f.b.s. $\varphi$ et une f.b.a. $\psi$ sur $\mathbb R^2$.

**Solution.** La matrice $A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ est symétrique et fournit

$$
\varphi(x,y)=X^TAY=x_1y_1+x_1y_2+x_2y_1+x_2y_2.
$$

La matrice $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ est antisymétrique et fournit

$$
\psi(x,y)=X^TAY=x_1y_2-x_2y_1.
$$

**Notations.** $S_n(\mathbb R)$ et $A_n(\mathbb R)$ désignent respectivement les sous-espaces de matrices symétriques et antisymétriques.

**Proposition 3.16.**

$$
S_n(\mathbb R)\oplus A_n(\mathbb R)=M_n(\mathbb R),
$$

$$
\dim S_n(\mathbb R)=\frac{n(n+1)}2,\qquad\dim A_n(\mathbb R)=\frac{n(n-1)}2.
$$

*Preuve : non renseignée dans la source.*

**Corollaire 3.17.** Si $\dim E=n$, $\mathcal L_{2,s}(E\times E;\mathbb R)$ est isomorphe à $S_n(\mathbb R)$ et $\mathcal L_{2,a}(E\times E;\mathbb R)$ est isomorphe à $A_n(\mathbb R)$. Ainsi,

$$
\dim\mathcal L_{2,s}(E\times E;\mathbb R)=\frac{n(n+1)}2,\qquad
\dim\mathcal L_{2,a}(E\times E;\mathbb R)=\frac{n(n-1)}2.
$$

> **Coquille de la source :** la deuxième dimension porte à nouveau l’indice $2,s$ ; l’indice attendu est $2,a$, conformément aux deux isomorphismes qui précèdent.

*Preuve : non renseignée dans la source.*

### 3.3. Matrice d’une forme symétrique positive ou définie (pages 8 et 9)

**Définition 3.18.** Soit $A\in M_n(\mathbb R)$ symétrique.

- Elle est **positive** si $X^TAX\ge0$ pour tout $X\in M_{n,1}(\mathbb R)$.
- Elle est **définie** si $X^TAX=0\iff X=0$ pour tout $X\in M_{n,1}(\mathbb R)$.

**Remarque.** Elle est positive définie si $X^TAX>0$ pour tout $X\ne0$.

**Définition 3.19.** Le support appelle **sous-matrice principale d’ordre $k$** la matrice

$$
A_k=\begin{pmatrix}a_{11}&\cdots&a_{1k}\\\vdots&\ddots&\vdots\\a_{k1}&\cdots&a_{kk}\end{pmatrix},\qquad1\le k\le n.
$$

**Théorème 3.20.** Pour une matrice réelle symétrique $A$, les propositions suivantes sont équivalentes :

1. $A$ est positive définie.
2. Les déterminants des $n$ sous-matrices principales $A_k$ sont strictement positifs.
3. Toutes les valeurs propres de $A$, considérées dans $\mathbb C$, sont réelles et strictement positives.

*Preuve : non renseignée dans la source.*

**Remarque.** Une matrice symétrique positive définie est inversible.

**Théorème 3.21.** Soit $E$ de dimension finie, $\varphi$ une forme bilinéaire et $A$ sa matrice dans une base quelconque. Alors $\varphi$ est symétrique positive définie si et seulement si $A$ est symétrique positive définie.

*Preuve : non renseignée dans la source.*
