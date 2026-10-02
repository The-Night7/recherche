---
source: "PREING2-S2/Algebre-lineaire/CM-Reduction-Endomorphismes_2024-2025_Algebre-lineaire_P2S2_KElAmine.pdf"
pages: 18
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Réduction des endomorphismes

Khalid El Amine I. — Department of Mathematics and Finance.

$\mathbb K$ désigne le corps $\mathbb R$ ou le corps $\mathbb C$.

> Transcription des dix-huit pages du support. Les preuves et solutions laissées vides sont signalées. Les erreurs et ambiguïtés de la source sont distinguées du texte mathématique.

## 1. Éléments propres d’un endomorphisme

### 1.1. Valeur propre et vecteur propre (page 1)

Dans cette section, $E$ est un $\mathbb K$-espace vectoriel de dimension quelconque.

**Définition 1.1 — Valeur propre.** Soit $f\in\mathcal L(E)$ et $\lambda\in\mathbb K$. Le scalaire $\lambda$ est une valeur propre de $f$ s’il existe $v\in E\setminus\{0_E\}$ tel que $f(v)=\lambda v$. Ce vecteur $v$ est appelé **vecteur propre associé** à $\lambda$.

**Définition 1.2 — Spectre.** L’ensemble des valeurs propres de $f$ est son **spectre**, noté $\operatorname{Sp}_{\mathbb K}(f)$ ou $\operatorname{Sp}(f)$.

**Définition 1.3 — Vecteur propre.** Un vecteur $v\ne0_E$ est propre pour $f$ s’il existe $\lambda\in\mathbb K$ tel que $f(v)=\lambda v$. Le scalaire est alors la valeur propre associée au vecteur.

**Remarque.** Un vecteur propre est non nul par définition.

**Définition 1.4 — Éléments propres.** Les valeurs et vecteurs propres de $f$ sont ses **éléments propres**. Un scalaire $\lambda$ et un vecteur $v$ sont des éléments propres associés si $v\ne0_E$ et $f(v)=\lambda v$.

**Exemple 1.** Soit $f:\mathbb R^2\to\mathbb R^2$, $f(x,y)=(x-y/2,-x/2+y)$.

- Vérifier que $v_1=(1,1)$ est propre pour $\lambda_1=1/2$.
- Vérifier que $v_2=(1,-1)$ est propre pour $\lambda_2=3/2$.

*Solution : non renseignée dans la source.*

### 1.2. Sous-espace propre (pages 2 et 3)

**Proposition 1.5.** Pour $f\in\mathcal L(E)$ et $\lambda\in\mathbb K$,

$$
E_\lambda=\{x\in E:f(x)=\lambda x\}=\ker(f-\lambda\operatorname{id}_E)
$$

est un sous-espace vectoriel de $E$.

*Preuve : non renseignée dans la source.*

**Définition 1.6.** Lorsque $\lambda$ est une valeur propre, $E_\lambda=\ker(f-\lambda\operatorname{id}_E)$ est appelé **sous-espace propre associé** à $\lambda$.

**Proposition 1.7.**

$$
\lambda\in\operatorname{Sp}(f)\iff E_\lambda\ne\{0_E\}\iff f-\lambda\operatorname{id}_E\text{ non injectif}.
$$

*Preuve : non renseignée dans la source.*

**Proposition 1.8.** Si $v_1,v_2$ sont propres pour des valeurs $\lambda_1\ne\lambda_2$, alors $(v_1,v_2)$ est libre.

*Preuve : non renseignée dans la source.*

**Théorème 1.9.** Une famille $(v_1,\ldots,v_p)$ de vecteurs propres de $f$ associés à des valeurs propres deux à deux distinctes est libre.

> La source écrit « vecteurs propres de $A$ » alors que l’endomorphisme de l’énoncé est $f$.

*Preuve : non renseignée dans la source.*

#### Rappel sur les sommes directes

**Définition 1.10.** Deux sous-espaces $E_1,E_2$ de $E$ sont **supplémentaires** si $E=E_1+E_2$ et $E_1\cap E_2=\{0_E\}$.

**Remarque de la source.** Pour deux espaces $E,F$ de dimension finie, le support imprime

$$
\dim(E+F)=\dim E+\dim F-\dim(F\cap F).
$$

> **Erreur dans cette formule :** dans un même espace ambiant, il faut retrancher $\dim(E\cap F)$, et non $\dim(F\cap F)$.

**Théorème 1.11.** En dimension finie, $E_1,E_2$ sont supplémentaires dès que l’une des conditions suivantes est satisfaite :

- Tout $x\in E$ admet un unique couple $(x_1,x_2)\in E_1\times E_2$ tel que $x=x_1+x_2$.
- $\dim E_1+\dim E_2=\dim E$ et $E_1\cap E_2=\{0_E\}$.
- $\dim E_1+\dim E_2=\dim E$ et $E=E_1+E_2$.

**Définition 1.12.** Une famille de sous-espaces $(F_1,\ldots,F_p)$ est **en somme directe** si

$$
\forall(x_1,\ldots,x_p)\in F_1\times\cdots\times F_p,\quad
x_1+\cdots+x_p=0\implies x_1=\cdots=x_p=0.
$$

Le sous-espace $F=F_1+\cdots+F_p$ est alors noté $F=F_1\oplus\cdots\oplus F_p$.

**Proposition 1.13.** La somme $\sum_{i=1}^p F_i$ est directe si et seulement si

$$
\forall i\in\{2,\ldots,p\},\qquad F_i\cap\left(\sum_{j=1}^{i-1}F_j\right)=\{0\}.
$$

> La source introduit $p$ sous-espaces, puis utilise $n$ dans les bornes ; ces bornes ont été harmonisées en $p$.

**Théorème 1.14.** Les sous-espaces propres associés à des valeurs propres deux à deux distinctes d’un endomorphisme sont en somme directe.

*Preuve : non renseignée dans la source.*

## 2. Éléments propres d’une matrice carrée

### 2.1. Valeur propre et vecteur propre (pages 3 et 4)

Ici $n\in\mathbb N^*$ et le vecteur nul de $M_{n,1}(\mathbb K)$ est noté $0_{n,1}$. Une matrice carrée peut être considérée comme un endomorphisme de cet espace de colonnes.

**Définition 2.1.** $\lambda\in\mathbb K$ est une valeur propre de $A\in M_n(\mathbb K)$ s’il existe $V\in M_{n,1}(\mathbb K)\setminus\{0_{n,1}\}$ tel que $AV=\lambda V$. Le vecteur $V$ est propre, associé à $\lambda$.

**Définition 2.2.** L’ensemble de ces valeurs propres est le **spectre** $\operatorname{Sp}(A)$ ou $\operatorname{Sp}_{\mathbb K}(A)$.

**Définition 2.3.** Un vecteur colonne $V\ne0_{n,1}$ est propre pour $A$ s’il existe un scalaire $\lambda$ tel que $AV=\lambda V$. Ce scalaire est la valeur propre associée.

**Définition 2.4.** Les valeurs et vecteurs propres sont les **éléments propres** de $A$. Ils sont associés lorsque $V\ne0_{n,1}$ et $AV=\lambda V$.

**Exemple.** Soient

$$
A=\begin{pmatrix}1&-1&-1\\-1&1&-1\\-1&-1&1\end{pmatrix},\quad
V_1=\begin{pmatrix}1\\1\\1\end{pmatrix},\quad V_2=\begin{pmatrix}1\\0\\-1\end{pmatrix},\quad V_3=\begin{pmatrix}0\\1\\-1\end{pmatrix}.
$$

Vérifier que les trois vecteurs sont propres et trouver les valeurs propres associées.

*Solution : non renseignée dans la source.*

### 2.2. Sous-espace propre (page 4)

**Proposition 2.5.** Pour $A\in M_n(\mathbb K)$ et $\lambda\in\mathbb K$,

$$
E_\lambda=\{X\in M_{n,1}(\mathbb K):AX=\lambda X\}=\ker(A-\lambda I_n)
$$

est un sous-espace vectoriel de $M_{n,1}(\mathbb K)$.

*Preuve : non renseignée dans la source.*

**Définition 2.6.** Si $\lambda$ est propre, $E_\lambda$ est le **sous-espace propre associé**.

**Proposition 2.7.**

$$
\lambda\in\operatorname{Sp}(A)\iff E_\lambda\ne\{0_{n,1}\}\iff A-\lambda I_n\text{ non inversible}.
$$

*Preuve : non renseignée dans la source.*

**Théorème 2.8.** Des vecteurs propres associés à des valeurs propres deux à deux distinctes forment une famille libre dans $M_{n,1}(\mathbb K)$.

**Preuve.** Même démonstration que pour les endomorphismes, à faire en exercice.

**Théorème 2.9.** Les sous-espaces propres de $A$ associés à des valeurs propres deux à deux distinctes sont en somme directe.

**Preuve.** Même démonstration que pour les endomorphismes, à faire en exercice.

## 3. Polynôme caractéristique

Dans cette section, $n\in\mathbb N^*$ et les espaces sont de dimension finie.

### 3.1. Préliminaire (page 5)

Dans une base $\mathcal B=(e_1,\ldots,e_n)$, tout vecteur possède une unique décomposition $x=\sum_{i=1}^n x_ie_i$. Les $x_i\in\mathbb K$ sont ses composantes. La base fixée permet d’identifier $E$ à $M_{n,1}(\mathbb K)$ ou à $\mathbb K^n$, et $x$ à la colonne $X=[x_1\ \cdots\ x_n]^T$.

Pour $f\in\mathcal L(E)$, on note $A=M_{\mathcal B}(f)=[a_{ij}]$. Alors $\operatorname{Sp}(f)=\operatorname{Sp}(A)$ et $x$ est propre pour $f$ si et seulement si $X$ est propre pour $A$.

On peut donc calculer les éléments propres sous la forme vectorielle $f(x)=\lambda x$ ou matricielle $AX=\lambda X$. Le chapitre utilise le plus souvent la seconde.

**Remarque.** La formulation vectorielle est indispensable en dimension infinie.

**Note.** Le support confond souvent le polynôme $P(X)\in\mathbb K_n[X]$ et sa fonction polynomiale associée $x\mapsto P(x)$ sur $\mathbb K$.

### 3.2. Définition et propriétés (pages 5 à 8)

**Définition 3.1.** Le **polynôme caractéristique** de $A$ est

$$
P_A(\lambda)=\det(A-\lambda I_n).
$$

$P_A(\lambda)=0$ est l’**équation caractéristique**.

**Proposition 3.2.** Deux matrices semblables ont le même polynôme caractéristique.

*Preuve : non renseignée dans la source.*

Des matrices semblables représentent un même endomorphisme dans des bases différentes ; cela permet la définition suivante.

**Définition 3.3.** Pour une base quelconque $\mathcal B$,

$$
P_f(\lambda)=\det\bigl(M_{\mathcal B}(f-\lambda\operatorname{id}_E)\bigr).
$$

**Proposition 3.4.** $\lambda$ est propre pour $A$ si et seulement si $P_A(\lambda)=0$.

**Preuve.** $\lambda$ propre $\iff A-\lambda I_n$ non inversible $\iff\det(A-\lambda I_n)=0\iff P_A(\lambda)=0$.

**Remarque.** $P_A(0)=\det A$. Donc 0 est une valeur propre si et seulement si $A$ est non inversible.

**Note pratique.** Pour un endomorphisme $f$, déterminer sa matrice dans une base quelconque puis chercher les valeurs propres de cette matrice.

**Exemple.** Soit $f\in\mathcal L(\mathbb R^3)$ de matrice canonique

$$
A=\begin{pmatrix}0&0&4\\1&2&1\\2&4&-2\end{pmatrix}.
$$

Déterminer son spectre, puis en déduire que $f$ n’est pas bijectif.

*Solution : non renseignée dans la source.*

**Théorème 3.5.** Pour $n\ge2$,

$$
P_A(\lambda)=(-1)^n\lambda^n+(-1)^{n-1}\operatorname{tr}(A)\lambda^{n-1}+\cdots+\det A.
$$

Ses coefficients appartiennent à $\mathbb K$ et son degré est $n$.

**Preuve de la source.** Cela résulte de la formule du déterminant

$$
P_A(\lambda)=\begin{vmatrix}
a_{11}-\lambda&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}-\lambda&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{n1}&a_{n2}&\cdots&a_{nn}-\lambda
\end{vmatrix}.
$$

Le support précise que la preuve est « loin d’être facile », sans autre développement.

**Remarque.** Le terme constant est $P_A(0)=\det A$ par définition.

**Exemple.** Pour $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
P_A(\lambda)=\lambda^2-\operatorname{tr}(A)\lambda+\det A=\lambda^2-(a+d)\lambda+ad-bc.
$$

**Corollaire 3.6.** Une matrice d’ordre $n$ possède au plus $n$ valeurs propres.

**Preuve.** Ce sont les racines de $P_A$, polynôme de degré $n$, qui a au plus $n$ racines.

#### Multiplicités et polynômes scindés (page 7)

Si $a$ est racine de $P$, celui-ci peut être divisible par $(X-a)^2$, $(X-a)^3$, etc.

**Définition 3.7.** L’**ordre de multiplicité** d’une racine $a$ est le plus grand entier $m$ tel que $(X-a)^m$ divise $P$. Une racine d’ordre 2 est double, d’ordre 3 triple, etc.

**Définition 3.8.** La multiplicité d’une valeur propre $\lambda$, notée $m_\lambda$ ou $\operatorname{mult}(\lambda)$, est sa multiplicité comme racine de $P_A$.

**Définition 3.9.** Un polynôme est **scindé dans $\mathbb K$** s’il est un produit de polynômes de degré 1, soit

$$
P(X)=c\prod_{i=1}^p(X-a_i)^{m_i},
$$

où les $a_i\in\mathbb K$ sont distincts, les $m_i\in\mathbb N^*$ sont leurs multiplicités et $c\in\mathbb K$ est constant.

**Remarques.** $\deg P=\sum_{i=1}^p m_i$. Un polynôme de degré $n\ge1$ est scindé si et seulement s’il possède exactement $n$ racines dans $\mathbb K$, comptées avec multiplicité.

> La définition de la multiplicité et la formule du degré supposent $P\ne0$ ; dans la factorisation, cela impose $c\ne0$. Cette précision n’est pas explicitée dans la source.

**Exemples.**

1. $X^2-5X+6=(X-2)(X-3)$ est scindé dans $\mathbb R$ : degré 2 et deux racines réelles.
2. $X^3-4X^2+5X-2=(X-1)^2(X-2)=(X-1)(X-1)(X-2)$ est scindé dans $\mathbb R$. Les trois racines comptées avec multiplicité sont $1,1,2$ ; 1 est double, 2 simple.
3. $X^2+1$ n’est pas scindé dans $\mathbb R$, mais l’est dans $\mathbb C$ : $(X-i)(X+i)$.

**Théorème 3.10 — D’Alembert–Gauss.** Tout polynôme de $\mathbb C[X]$ est scindé dans $\mathbb C$.

**Preuve.** Admis.

**Remarque.** Un polynôme réel est donc scindé dans $\mathbb C$ ; il est scindé dans $\mathbb R$ lorsque toutes ses racines complexes sont réelles.

**Corollaire 3.11.** Un endomorphisme d’un espace complexe de dimension $n$ admet exactement $n$ valeurs propres comptées avec multiplicité. Sur un espace réel de dimension $n$, il en admet au plus $n$ dans $\mathbb R$, comptées avec multiplicité.

**Preuve.** Admis.

**Exemple.** Pour $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $P_A(\lambda)=\lambda^2+1$. Ainsi $\operatorname{Sp}_{\mathbb R}(A)=\varnothing$ et $\operatorname{Sp}_{\mathbb C}(A)=\{-i,i\}$.

#### Trace, déterminant et dimension des sous-espaces propres (page 8)

**Rappel.** $\operatorname{tr}(A)=\sum_{i=1}^n a_{ii}$.

**Proposition 3.12.** Si $P_A$ est scindé et $\lambda_1,\ldots,\lambda_n$ sont les valeurs propres comptées avec multiplicité,

$$
\sum_{i=1}^n\lambda_i=\operatorname{tr}(A),\qquad\prod_{i=1}^n\lambda_i=\det A.
$$

**Preuve.** Comparer les coefficients de degrés $n-1$ et 0 dans

$$
P_A(\lambda)=(-1)^n\lambda^n+(-1)^{n-1}\operatorname{tr}(A)\lambda^{n-1}+\cdots+\det A
=(-1)^n\prod_{i=1}^n(\lambda-\lambda_i).
$$

**Remarque de la source.** Pour une matrice réelle ou complexe, la trace est la somme des valeurs propres complexes et le déterminant leur produit. Les formules imprimées sont

$$
\operatorname{tr}(A)=\sum_{\lambda\in\operatorname{Sp}_{\mathbb C}(A)}\lambda,\qquad
\det A=\prod_{\lambda\in\operatorname{Sp}_{\mathbb C}(A)}\lambda.
$$

> **Multiplicités omises dans cette notation :** le spectre étant un ensemble de valeurs distinctes, les écritures correctes sont $\operatorname{tr}(A)=\sum_\lambda m_\lambda\lambda$ et $\det A=\prod_\lambda\lambda^{m_\lambda}$. La proposition précédente compte bien les valeurs avec multiplicité.

**Théorème 3.13.** Pour $\lambda\in\operatorname{Sp}(A)$ de multiplicité $m_\lambda$,

$$
1\le\dim E_\lambda\le m_\lambda.
$$

*Preuve : non renseignée dans la source.*

**Remarque pratique.** Le théorème du rang donne $\dim E_\lambda=n-\operatorname{rg}(A-\lambda I_n)$. Pour en obtenir une base, résoudre $AX=\lambda X$.

**Corollaire 3.14.** Si $\lambda$ est simple, $\dim E_\lambda=1$.

**Preuve.** $m_\lambda=1$ entraîne $1\le\dim E_\lambda\le1$.

## 4. Diagonalisation

### 4.1. Endomorphisme (page 9)

**Définition 4.1.** En dimension quelconque, $f\in\mathcal L(E)$ est **diagonalisable** s’il existe une base de $E$ formée de vecteurs propres de $f$. Diagonaliser $f$ consiste à trouver une telle base.

**Exemple.** Reprendre $f(x,y)=(x-y/2,-x/2+y)$ sur $\mathbb R^2$ et montrer que $f$ est diagonalisable.

*Solution : non renseignée dans la source.*

**Proposition 4.2.** En dimension finie, $f$ est diagonalisable si et seulement s’il existe une base $\mathcal B$ telle que $M_{\mathcal B}(f)$ soit diagonale.

*Preuve : non renseignée dans la source.*

### 4.2. Matrice carrée (pages 9 et 10)

**Définition 4.3.** $A\in M_n(\mathbb K)$ est diagonalisable s’il existe une base de $M_{n,1}(\mathbb K)$ constituée de vecteurs propres. Diagonaliser $A$ consiste à trouver cette base.

**Définition 4.4 (bis).** De façon équivalente, $A$ est semblable à une matrice diagonale : il existe $D$ diagonale et $P$ inversible telles que $A=PDP^{-1}$. Diagonaliser $A$ consiste à trouver $D$ et $P$.

**Théorème 4.5 — Condition suffisante.** Une matrice d’ordre $n$ possédant $n$ valeurs propres deux à deux distinctes est diagonalisable.

*Preuve : non renseignée dans la source.*

**Exemple 1.** Une matrice triangulaire dont les coefficients diagonaux sont deux à deux distincts est diagonalisable. En effet, dans le cas supérieur,

$$
A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\0&a_{22}&\ddots&\vdots\\\vdots&\ddots&\ddots&a_{n-1,n}\\0&\cdots&0&a_{nn}\end{pmatrix},
$$

$$
P_A(\lambda)=\begin{vmatrix}a_{11}-\lambda&a_{12}&\cdots&a_{1n}\\0&a_{22}-\lambda&\ddots&\vdots\\\vdots&\ddots&\ddots&a_{n-1,n}\\0&\cdots&0&a_{nn}-\lambda\end{vmatrix}
=\prod_{i=1}^n(a_{ii}-\lambda).
$$

Les $n$ racines sont distinctes ; le spectre est $\{a_{ii}:1\le i\le n\}$ et $A$ est diagonalisable.

**Exemple 2.** Montrer que $A=\begin{pmatrix}3&1\\-2&0\end{pmatrix}$ est diagonalisable et la diagonaliser.

*Solution : non renseignée dans la source.*

**Remarque.** L’ordre des colonnes propres dans $P$ doit correspondre à l’ordre des valeurs propres sur la diagonale de $D$.

**Théorème 4.6.** $A$ est diagonalisable si et seulement si la somme des dimensions de ses sous-espaces propres est $n$.

*Preuve : non renseignée dans la source.*

**Théorème 4.7.** $A$ est diagonalisable si et seulement si $M_{n,1}(\mathbb K)$ est somme directe des sous-espaces propres.

*Preuve : non renseignée dans la source.*

**Remarque importante.** En pratique, on utilise souvent le polynôme caractéristique et la caractérisation fondamentale suivante.

**Théorème 4.8 — Condition nécessaire et suffisante.** $A$ est diagonalisable si et seulement si $P_A$ est scindé dans $\mathbb K$ et $\dim E_\lambda=m_\lambda$ pour toute valeur propre $\lambda$.

*Preuve : non renseignée dans la source.*

**Exemple.** La matrice suivante est-elle diagonalisable ?

$$
A=\frac12\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

**Synthèse — Diagonalisation.** Pour $A\in M_n(\mathbb K)$ :

- $n$ valeurs propres distinctes $\implies A$ diagonalisable.
- $P_A$ scindé et $\dim E_\lambda=m_\lambda$ pour tout $\lambda\in\operatorname{Sp}(A)$ $\iff A$ diagonalisable.
- $\sum_{\lambda\in\operatorname{Sp}(A)}\dim E_\lambda=n\iff A$ diagonalisable.
- $\bigoplus_{\lambda\in\operatorname{Sp}(A)}E_\lambda=M_{n,1}(\mathbb K)\iff A$ diagonalisable.
- $P_A$ non scindé $\implies A$ non diagonalisable.
- L’existence d’une valeur propre telle que $\dim E_\lambda<m_\lambda$ implique que $A$ n’est pas diagonalisable.

## 5. Trigonalisation

### 5.1. Matrices triangulaires (pages 11 et 12)

Une matrice **triangulaire supérieure** a la forme

$$
A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\0&a_{22}&\ddots&\vdots\\\vdots&\ddots&\ddots&a_{n-1,n}\\0&\cdots&0&a_{nn}\end{pmatrix}.
$$

L’ensemble de ces matrices est noté $U_n(\mathbb K)$, pour *upper triangular matrix*, ou $T_{n,s}(\mathbb K)$. Si les coefficients diagonaux sont nuls, la matrice est triangulaire supérieure **stricte**.

Une matrice **triangulaire inférieure** a la forme

$$
A=\begin{pmatrix}a_{11}&0&\cdots&0\\a_{21}&a_{22}&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\a_{n1}&\cdots&a_{n,n-1}&a_{nn}\end{pmatrix}.
$$

On note leur ensemble $L_n(\mathbb K)$, pour *lower triangular matrix*, ou $T_{n,i}(\mathbb K)$. Si les coefficients diagonaux sont nuls, la matrice est triangulaire inférieure **stricte**.

Une matrice est **triangulaire** si elle est triangulaire supérieure ou inférieure.

**Proposition 5.1.** Toute matrice triangulaire inférieure est semblable à une matrice triangulaire supérieure.

**Preuve.** Considérons la matrice d’ordre $n$

$$
P=\begin{pmatrix}0&0&\cdots&0&1\\0&0&\cdots&1&0\\\vdots&\vdots&\cdots&\vdots&\vdots\\0&1&\cdots&0&0\\1&0&\cdots&0&0\end{pmatrix}.
$$

Elle vérifie $P^2=I_n$, donc $P^{-1}=P$. Pour

$$
L=\begin{pmatrix}a_{11}&0&\cdots&0\\a_{21}&a_{22}&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\a_{n1}&\cdots&a_{n,n-1}&a_{nn}\end{pmatrix},
$$

on a

$$
PLP^{-1}=PLP=U
=\begin{pmatrix}a_{nn}&a_{n,n-1}&\cdots&a_{n1}\\0&a_{n-1,n-1}&\ddots&\vdots\\\vdots&\ddots&\ddots&a_{21}\\0&\cdots&0&a_{11}\end{pmatrix}.
$$

$U$ est triangulaire supérieure et semblable à $L$.

**Remarque.** Si $L$ est la matrice de $f$ dans $\mathcal B=(e_1,\ldots,e_n)$, $U$ est sa matrice dans la base renversée $\mathcal B'=(e_n,\ldots,e_1)$. Le support abrège ceci par $L=[f(e_1)\ \cdots\ f(e_n)]$ et $U=[f(e_n)\ \cdots\ f(e_1)]$.

> Les colonnes de la seconde expression doivent être exprimées dans $\mathcal B'$, et celles de la première dans $\mathcal B$ : inverser seulement l’ordre des colonnes en gardant leurs anciennes coordonnées ne suffit pas.

**Note.** Dans la suite, le terme « triangulaire » désigne par convention « triangulaire supérieure ».

### 5.2. Trigonalisation (pages 12 et 13)

**Définition 5.2.** Une matrice $A$ est **trigonalisable** s’il existe une matrice triangulaire $T$ semblable à $A$. Un endomorphisme $f$ est trigonalisable s’il existe une base dans laquelle sa matrice est triangulaire.

**Théorème 5.3.** $A$ est trigonalisable si et seulement si $P_A$ est scindé dans $\mathbb K$. De même, $f$ est trigonalisable si et seulement si $P_f$ est scindé dans $\mathbb K$.

*Preuve : non renseignée dans la source.*

**Remarque.** Les coefficients diagonaux de $T$ sont les valeurs propres de $A$.

**Exemple.** Trigonaliser dans $M_3(\mathbb R)$ la matrice

$$
A=\begin{pmatrix}-2&2&-1\\-1&1&-1\\-1&2&-2\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

**Corollaire 5.4.** Toute matrice complexe est semblable à une matrice triangulaire complexe.

**Preuve.** Tout polynôme complexe est scindé dans $\mathbb C$, donc $P_A$ l’est et $A$ est trigonalisable.

**En pratique : dimension 3.** Si $A\in M_3(\mathbb K)$ est trigonalisable mais non diagonalisable, trois cas se présentent.

**Cas 1.** $P_A(\lambda)=(\lambda_1-\lambda)(\lambda_2-\lambda)^2$, avec $\lambda_1\ne\lambda_2$, et $\operatorname{Sp}(A)=\{\lambda_1,\lambda_2\}$. Si $\dim E_{\lambda_2}=1$, alors $A$ est semblable à

$$
T=\begin{pmatrix}\lambda_1&0&0\\0&\lambda_2&a\\0&0&\lambda_2\end{pmatrix},\qquad a\ne0.
$$

**Cas 2.** $P_A(\lambda)=(\lambda_1-\lambda)^3$, $\operatorname{Sp}(A)=\{\lambda_1\}$. Si $\dim E_{\lambda_1}=2$, alors $A$ est semblable à

$$
T=\begin{pmatrix}\lambda_1&0&a\\0&\lambda_1&b\\0&0&\lambda_1\end{pmatrix},\qquad(a,b)\ne(0,0).
$$

**Cas 3.** Même polynôme caractéristique, mais $\dim E_{\lambda_1}=1$. Alors $A$ est semblable à

$$
T=\begin{pmatrix}\lambda_1&a&b\\0&\lambda_1&c\\0&0&\lambda_1\end{pmatrix},\qquad ac\ne0.
$$

**Synthèse — Trigonalisation.** $P_A$ scindé dans $\mathbb K\iff A$ trigonalisable dans $M_n(\mathbb K)$. Si $\mathbb K=\mathbb C$, toute matrice est trigonalisable.

## 6. Applications de la réduction d’une matrice carrée

### 6.1. Calcul des puissances

**Rappel (page 14).** Si $\lambda$ est une valeur propre de $A$, alors $\lambda^2$ est propre pour $A^2$, et plus généralement $\lambda^k$ est propre pour $A^k$ pour $k\in\mathbb N$. Si $A$ est inversible, $1/\lambda$ est propre pour $A^{-1}$ et $\lambda^{-k}$ est propre pour $A^{-k}$.

#### 6.1.1. Puissances d’une matrice (page 14)

**Définition 6.1.** Pour $k\in\mathbb N$,

$$
A^k=\underbrace{A\times\cdots\times A}_{k\text{ fois}},\qquad A^0=I_n.
$$

Si $A$ est inversible, $A^{-k}=(A^{-1})^k$.

**Remarque.** Une puissance peut être nulle alors que $A\ne O_n$ :

$$
A=\begin{pmatrix}1&-1\\1&-1\end{pmatrix},\qquad A^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$

**Propriétés 6.2.** Pour $i,k\in\mathbb N$, $A^iA^k=A^{i+k}$ et $(A^i)^k=A^{ik}$. Si $A$ est inversible, ces identités valent pour tous $i,k\in\mathbb Z$.

*Preuve : non renseignée dans la source.*

**Proposition 6.3.** Soient $D$ diagonale, $U$ triangulaire supérieure et $L$ triangulaire inférieure, de mêmes coefficients diagonaux $\lambda_1,\ldots,\lambda_n$ :

$$
D=\begin{pmatrix}\lambda_1&0&\cdots&0\\0&\lambda_2&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&\lambda_n\end{pmatrix},
$$

$$
U=\begin{pmatrix}\lambda_1&u_{12}&\cdots&u_{1n}\\0&\lambda_2&\ddots&\vdots\\\vdots&\ddots&\ddots&u_{n-1,n}\\0&\cdots&0&\lambda_n\end{pmatrix},\quad
L=\begin{pmatrix}\lambda_1&0&\cdots&0\\l_{21}&\lambda_2&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\l_{n1}&\cdots&l_{n,n-1}&\lambda_n\end{pmatrix}.
$$

Pour $k\in\mathbb N$, leurs puissances conservent ces formes, avec coefficients diagonaux $\lambda_1^k,\ldots,\lambda_n^k$ :

$$
D^k=\begin{pmatrix}\lambda_1^k&&0\\&\ddots&\\0&&\lambda_n^k\end{pmatrix},\quad
U^k=\begin{pmatrix}\lambda_1^k&&*\\&\ddots&\\0&&\lambda_n^k\end{pmatrix},\quad
L^k=\begin{pmatrix}\lambda_1^k&&0\\&\ddots&\\*&&\lambda_n^k\end{pmatrix},
$$

où les étoiles représentent des éléments de $\mathbb K$.

*Preuve : non renseignée dans la source.*

#### 6.1.2. Formule du binôme (page 15)

**Définition 6.4.** Une matrice est **nilpotente** s’il existe $p\in\mathbb N^*$ tel que $A^p=O_n$ et $A^{p-1}\ne O_n$. Cet entier unique est l’**ordre de nilpotence**.

**Exemples.**

$$
\begin{pmatrix}0&1\\0&0\end{pmatrix}\text{ est d’ordre 2},\qquad
\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}\text{ est d’ordre 3}.
$$

**Remarque.** Toute matrice triangulaire supérieure ou inférieure stricte d’ordre $n$ est nilpotente d’ordre au plus $n$.

**Théorème 6.5 — Binôme.** Si $A,B\in M_n(\mathbb K)$ commutent, alors, pour $k\in\mathbb N$,

$$
(A+B)^k=\sum_{i=0}^k\binom ki A^{k-i}B^i.
$$

*Preuve : non renseignée dans la source.*

**Remarque.** Sans commutation, cette formule est fausse en général.

**Exercice.** Calculer $A^k$ pour tout $k\in\mathbb N$ dans les deux cas

$$
\text{a) }A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
\text{b) }A=\begin{pmatrix}1&0\\-3&1\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

**Exercice.** Calculer $T^k$ pour tout $k\in\mathbb N$ avec

$$
T=\begin{pmatrix}-1&0&0\\0&3&1\\0&0&3\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

#### 6.1.3. Puissances de matrices semblables (pages 15 et 16)

**Proposition 6.6.** Si $A=PBP^{-1}$, alors $A^k=PB^kP^{-1}$ pour tout $k\in\mathbb N$.

**Preuve par récurrence.** Pour $k=0$, $A^0=I_n=PI_nP^{-1}=PB^0P^{-1}$. Si $A^k=PB^kP^{-1}$, alors

$$
\begin{aligned}
A^{k+1}&=A^kA=PB^kP^{-1}PBP^{-1}\\
&=PB^k(P^{-1}P)BP^{-1}=P(B^kB)P^{-1}=PB^{k+1}P^{-1}.
\end{aligned}
$$

**Remarque.** $A$ est inversible si et seulement si $B$ l’est, et $A^{-1}=PB^{-1}P^{-1}$. En effet,

$$
A^{-1}=(PBP^{-1})^{-1}=(P^{-1})^{-1}B^{-1}P^{-1}=PB^{-1}P^{-1}.
$$

> **Coquille de la source :** dans l’égalité intermédiaire, le dernier facteur est imprimé $P$ au lieu de $P^{-1}$. Le résultat final imprimé est correct.

**Corollaire 6.7.** Si $A,B,P$ sont inversibles et $A=PBP^{-1}$, alors $A^k=PB^kP^{-1}$ pour tout $k\in\mathbb Z$.

**Preuve.** Le cas $k\ge0$ est acquis. Pour $k<0$, poser $m=-k\in\mathbb N^*$ :

$$
A^k=A^{-m}=(A^{-1})^m=(PB^{-1}P^{-1})^m
=P(B^{-1})^mP^{-1}=PB^{-m}P^{-1}=PB^kP^{-1}.
$$

#### A. Matrice diagonalisable (page 16)

**Corollaire 6.8.** Si $A=PDP^{-1}$ avec $D$ diagonale, alors $A^k=PD^kP^{-1}$ pour $k\in\mathbb N$, et pour $k\in\mathbb Z$ si $A$ est inversible.

*Preuve : non renseignée dans la source.*

**Remarque.**

$$
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
\implies D^k=\operatorname{diag}(\lambda_1^k,\ldots,\lambda_n^k),
$$

et donc $A^k=P\operatorname{diag}(\lambda_1^k,\ldots,\lambda_n^k)P^{-1}$.

**Exemple.** Montrer que

$$
A=\begin{pmatrix}0&-8&6\\-1&-8&7\\1&-14&11\end{pmatrix}
$$

est inversible et calculer $A^k$ pour tout $k\in\mathbb Z$.

*Solution : non renseignée dans la source.*

#### B. Matrice trigonalisable (page 17)

**Corollaire 6.9.** Si $A=PTP^{-1}$ avec $T$ triangulaire, alors $A^k=PT^kP^{-1}$ pour $k\in\mathbb N$, et pour $k\in\mathbb Z$ si $A$ est inversible.

*Preuve : non renseignée dans la source.*

#### C. Matrice diagonale par blocs (page 17)

**Proposition 6.10.** Si les $A_i$ sont carrées et

$$
A=\begin{pmatrix}A_1&0&\cdots&0\\0&A_2&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&A_p\end{pmatrix},
$$

alors, pour $k\in\mathbb N$,

$$
A^k=\begin{pmatrix}A_1^k&0&\cdots&0\\0&A_2^k&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&A_p^k\end{pmatrix}.
$$

*Preuve : non renseignée dans la source.*

**Corollaire 6.11.** Si les $T_i$ sont triangulaires supérieures et

$$
T=\begin{pmatrix}T_1&0&\cdots&0\\0&T_2&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&T_p\end{pmatrix},
$$

alors, pour $k\in\mathbb N$,

$$
T^k=\begin{pmatrix}T_1^k&0&\cdots&0\\0&T_2^k&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&T_p^k\end{pmatrix}.
$$

*Preuve : non renseignée dans la source. Les rubriques « Exemple » et « Solution » qui suivent sont également vides.*

### 6.2. Suites récurrentes linéaires (page 18)

#### Rappel : suite arithmético-géométrique

**Définition 6.12.** Une suite $(u_n)_{n\in\mathbb N}$ à valeurs dans $\mathbb K$ est **arithmético-géométrique** s’il existe des scalaires $a,b$ tels que

$$
u_{n+1}=au_n+b\qquad(n\in\mathbb N).
$$

> La source écrit « $(a,b)\in\mathbb K$ » ; pour le couple, il faut $\mathbb K^2$.

**Cas $a=1$.** La suite est arithmétique : $u_n=u_0+nb$. Si $b\ne0$, elle diverge ; si $b=0$, elle est constante égale à $u_0$.

**Cas $a\ne1$.**

$$
u_n=a^n(u_0-u)+u,\qquad u=\frac b{1-a}.
$$

Si $|a|<1$, alors $u_n\to u$.

#### 6.2.1. Suites récurrentes linéaires du premier ordre

**Proposition 6.13.** Soit $A\in M_n(\mathbb R)$, $B\in M_{n,1}(\mathbb R)$ et une suite de colonnes définie par

$$
X_{n+1}=AX_n+B,\qquad X_0\text{ donné}.
$$

Si la suite converge, sa limite $X$ vérifie $X=AX+B$.

*Preuve : non renseignée dans la source.*

**Proposition 6.14.**

1. Si $I_n-A$ est inversible, pour tout $B$ il existe un unique $X\in M_{n,1}(\mathbb R)$ tel que $X=AX+B$.
2. Si $I_n-A$ n’est pas inversible, cette équation possède soit aucune solution, soit une infinité de solutions.

*Preuve : non renseignée dans la source.*

**Exemple.** Soient trois suites réelles avec $u_0=0$, $v_0=22$, $w_0=22$ et

$$
\forall n\in\mathbb N,\qquad
\begin{cases}
u_{n+1}=\dfrac14(2u_n+v_n+w_n),\\
v_{n+1}=\dfrac13(u_n+v_n+w_n),\\
w_{n+1}=\dfrac14(u_n+v_n+2w_n).
\end{cases}
$$

Calculer $u_n,v_n,w_n$ en fonction de $n$ et étudier la convergence des trois suites.

*Solution : non renseignée dans la source.*
