---
source: "PREING2-S2/Algebre-lineaire/CM-Systemes-differentiels_2022-2023_Algebre-lineaire_P2S2_KElAmine.pdf"
pages: 8
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Systèmes différentiels linéaires

Khalid El Amine I. — Department of Mathematics and Finance.

> Transcription des huit pages du support. Les rubriques « Preuve » et « Solution » laissées vides dans le PDF sont signalées ; aucun développement absent de la source n’est ajouté.

## 1. Équation différentielle linéaire du premier ordre

### 1.1. Équation homogène (page 1)

**Définition 1.1.** Soit $I\subset\mathbb R$ un intervalle ouvert et $a\in C(I,\mathbb R)$. Une équation différentielle linéaire homogène du premier ordre est une équation de la forme

$$
x'(t)=a(t)x(t).\tag{EH}
$$

Une fonction $f$ est solution de $(EH)$ sur $I$ si elle est dérivable sur $I$ et si $f'(t)=a(t)f(t)$ pour tout $t\in I$.

**Remarques.** La fonction nulle est solution de $(EH)$. Cette équation peut admettre une infinité de solutions.

**Proposition 1.2.** L’ensemble $E_h$ des solutions de $(EH)$ est un espace vectoriel sur $\mathbb R$.

*Preuve : non renseignée dans la source.*

**Théorème 1.3.** Si $A$ est une primitive de $a$ sur $I$, alors

$$
E_h=\{f:t\in I\mapsto ce^{A(t)}\ ;\ c\in\mathbb R\}.
$$

$E_h$ est un espace vectoriel réel de dimension 1. L’application $x:t\mapsto ce^{A(t)}$ est appelée **solution générale** de $(EH)$.

*Preuve : non renseignée dans la source.*

**Exemple 1.** La solution générale sur $\mathbb R$, ou sur tout intervalle ouvert $I\subset\mathbb R$, de $x'(t)=-2x(t)$ est $x(t)=ce^{-2t}$, avec $c\in\mathbb R$.

### 1.2. Équation non homogène

#### 1.2.1. Solution générale (pages 2 et 3)

**Définition 1.4.** Soit $I\subset\mathbb R$ un intervalle ouvert et $a,b\in C(I,\mathbb R)$. Une équation différentielle linéaire non homogène du premier ordre est de la forme

$$
x'(t)=a(t)x(t)+b(t).\tag{E}
$$

Une fonction $f$ est solution sur $I$ si elle est dérivable et vérifie $f'(t)=a(t)f(t)+b(t)$ pour tout $t\in I$.

L’équation homogène associée est $x'(t)=a(t)x(t)$, notée $(EH)$.

**Théorème 1.5.** Soit $f_p$ une solution particulière sur $I$ de $(E)$ et $A$ une primitive de $a$ sur $I$. L’ensemble des solutions est

$$
E=\{f:t\in I\mapsto ce^{A(t)}+f_p(t)\ ;\ c\in\mathbb R\}.
$$

*Preuve : non renseignée dans la source.*

**Méthode de la variation de la constante.** On cherche une solution particulière de la forme $f_p(t)=c(t)e^{A(t)}$. La fonction inconnue $c$ est déterminée en imposant l’équation :

$$
\begin{aligned}
f_p\text{ solution de }(E)
&\iff f'_p(t)=a(t)f_p(t)+b(t)\\
&\iff(c(t)e^{A(t)})'=a(t)c(t)e^{A(t)}+b(t)\\
&\iff c'(t)e^{A(t)}+c(t)a(t)e^{A(t)}=a(t)c(t)e^{A(t)}+b(t)\\
&\iff c'(t)e^{A(t)}=b(t)\\
&\iff c'(t)=b(t)e^{-A(t)}\\
&\iff c(t)=\int b(t)e^{-A(t)}\,dt.
\end{aligned}
$$

Ainsi,

$$
f_p(t)=\left(\int b(t)e^{-A(t)}\,dt\right)e^{A(t)}
$$

est bien une solution particulière de $(E)$.

**Proposition 1.6.** L’ensemble des solutions est

$$
E=\left\{f:t\in I\mapsto\left(c+\int b(t)e^{-A(t)}\,dt\right)e^{A(t)}\ ;\ c\in\mathbb R\right\},
\qquad A(t)=\int a(t)\,dt.
$$

Cette expression est appelée solution générale de $(E)$. On écrit souvent

$$
x(t)=x_h(t)+x_p(t),\qquad
x_h(t)=ce^{A(t)},\qquad x_p(t)=\left(\int b(t)e^{-A(t)}\,dt\right)e^{A(t)}.
$$

Les courbes représentatives des solutions de $(E)$ sont appelées **courbes intégrales** de $(E)$.

*Preuve : non renseignée dans la source.*

**Exemple.** Déterminer la solution générale sur $\mathbb R$ de $x'(t)=2x(t)-2t$.

*Solution : non renseignée dans la source.*

#### 1.2.2. Problème à valeur initiale : existence et unicité (page 3)

**Théorème 1.7 — Cauchy–Lipschitz [Fr] / Picard–Lindelöf [En].** Soit $I\subset\mathbb R$ ouvert et $a,b\in C(I,\mathbb R)$. Pour tout $t_0\in I$ et tout $x_0\in\mathbb R$, il existe une unique solution sur $I$ du problème à valeur initiale (PVI)

$$
\begin{cases}x'(t)=a(t)x(t)+b(t),\\x(t_0)=x_0.\end{cases}
$$

L’égalité $x(t_0)=x_0$ est appelée **condition initiale**.

*Preuve : non renseignée dans la source.*

## 2. Système différentiel linéaire du premier ordre

### 2.1. Solution générale (pages 3 et 4)

**Définition 2.1.** Soit $I\subset\mathbb R$ un intervalle ouvert. Un système différentiel linéaire du premier ordre sur $I$ est de la forme

$$
X'(t)=A(t)X(t)+B(t).\tag{S}
$$

- $A(t)=[a_{ij}(t)]\in M_n(\mathbb R)$ est donnée ; ses coefficients sont des fonctions continues de $t\in I$.
- $B(t)=[b_i(t)]\in M_{n,1}(\mathbb R)$ est un vecteur donné, appelé **second membre** ; ses composantes sont continues.
- $X(t)=[x_i(t)]\in M_{n,1}(\mathbb R)$ est le vecteur inconnu, et $X'(t)=[x'_i(t)]$.

Le système est **à coefficients constants** si $A$ ne dépend pas de $t$. Il est **homogène** si $B(t)=0$ pour tout $t\in I$, c’est-à-dire

$$
X'(t)=A(t)X(t).\tag{SH}
$$

**Théorème 2.2 — Solution générale du système non homogène.** Soit $X_h$ la solution générale de $(SH)$ et $X_p$ une solution particulière de $(S)$ sur $I$. La solution générale de $(S)$ est

$$
X(t)=X_h(t)+X_p(t).
$$

*Preuve : non renseignée dans la source.*

### 2.2. Problème à valeur initiale : existence et unicité (page 4)

**Théorème 2.3 — Cauchy–Lipschitz / Picard–Lindelöf.** Soit $I\subset\mathbb R$ ouvert, $A\in C(I,M_n(\mathbb R))$ et $B\in C(I,M_{n,1}(\mathbb R))$. Pour tout $t_0\in I$ et $X_0\in M_{n,1}(\mathbb R)$, il existe une unique solution sur $I$ du PVI

$$
\begin{cases}X'(t)=A(t)X(t)+B(t),\\X(t_0)=X_0.\end{cases}
$$

$X(t_0)=X_0$ est la condition initiale.

*Preuve : non renseignée dans la source.*

### 2.3. Résolution des systèmes à coefficients constants

Dans cette sous-section, $A$ ne dépend plus de $t$. On considère uniquement les systèmes $X'(t)=AX(t)+B(t)$.

#### 2.3.1. Résolution par réduction de matrice — Cas diagonalisable (pages 4 et 5)

Supposons $A=PDP^{-1}$, où $D$ est diagonale. Alors

$$
\begin{aligned}
X'(t)=AX(t)+B(t)
&\iff X'(t)=PDP^{-1}X(t)+B(t)\\
&\iff P^{-1}X'(t)=DP^{-1}X(t)+P^{-1}B(t)\\
&\iff(P^{-1}X(t))'=D(P^{-1}X(t))+P^{-1}B(t)\\
&\iff Y'(t)=DY(t)+P^{-1}B(t),\qquad Y(t)=P^{-1}X(t).
\end{aligned}
$$

Le système en $Y$ est découplé. On le résout, puis on en déduit $X(t)=PY(t)$.

**Remarque.** On ne calcule pas $P^{-1}$ si $B(t)=0$.

**Algorithme.** Poser $Y=P^{-1}X$, résoudre $Y'=DY+P^{-1}B$, puis calculer $X=PY$.

**Proposition 2.4.** Si $A=PDP^{-1}$ avec $D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$ et $P=[V_1\ \cdots\ V_n]$, la solution générale de $X'=AX$ est

$$
X(t)=\sum_{i=1}^n c_i e^{\lambda_i t}V_i,\qquad c_i\in\mathbb R.
$$

La famille $\{e^{\lambda_1t}V_1,\ldots,e^{\lambda_nt}V_n\}$ est appelée **système fondamental de solutions**. Toute solution de $(SH)$ est combinaison linéaire de cette famille.

> La source écrit ici « $(DH)$ » au lieu de « $(SH)$ » et comporte un crochet fermant surnuméraire dans la famille.

**Exemple 1.** Résoudre $X'=AX$ avec

$$
X(t)=\begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix},\qquad A=\begin{pmatrix}2&0\\0&3\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

**Exemple 2.** Résoudre $X'=AX$ avec

$$
X(t)=\begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix},\qquad A=\begin{pmatrix}1&-1\\2&4\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

**Exemple 3.** Résoudre $X'=AX+B(t)$ avec

$$
X(t)=\begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix},\quad
A=\begin{pmatrix}1&-1\\2&4\end{pmatrix},\quad B(t)=\begin{pmatrix}t\\2t\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

#### Cas trigonalisable (pages 5 et 6)

Supposons $A=PTP^{-1}$ avec $T$ triangulaire supérieure. Alors

$$
\begin{aligned}
X'(t)=AX(t)+B(t)
&\iff X'(t)=PTP^{-1}X(t)+B(t)\\
&\iff P^{-1}X'(t)=TP^{-1}X(t)+P^{-1}B(t)\\
&\iff(P^{-1}X(t))'=T(P^{-1}X(t))+P^{-1}B(t)\\
&\iff Y'(t)=TY(t)+P^{-1}B(t),\qquad Y(t)=P^{-1}X(t).
\end{aligned}
$$

Le système en $Y$ n’est pas totalement découplé. On le résout par une démarche rétrograde, en commençant par la dernière équation, puis on en déduit $X=PY$.

**Remarque.** On ne calcule pas $P^{-1}$ si $B(t)=0$.

**Algorithme.** Poser $Y=P^{-1}X$, résoudre $Y'=TY+P^{-1}B$ par démarche rétrograde, puis calculer $X=PY$.

**Exemple 1.** Résoudre

$$
\begin{cases}x'_1(t)=2x_1(t)+x_2(t),&(1)\\x'_2(t)=-x_2(t).&(2)\end{cases}
$$

*Solution : non renseignée dans la source.*

**Exemple 2.** Résoudre $X'=AX$, avec

$$
X(t)=\begin{pmatrix}x_1(t)\\x_2(t)\end{pmatrix},\qquad A=\begin{pmatrix}1&1\\-1&3\end{pmatrix}.
$$

*Solution : non renseignée dans la source.*

#### 2.3.2. Résolution par exponentielle de matrice (pages 6 à 8)

**Proposition 2.5.** Pour $n\in\mathbb N^*$ et $A\in M_n(\mathbb K)$, la série

$$
\sum_{k\ge0}\frac{A^k}{k!}=I_n+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots
$$

est absolument convergente dans $M_n(\mathbb K)$, donc convergente.

*Preuve : non renseignée dans la source.*

**Définition 2.6 — Exponentielle de matrice.** Pour $n\in\mathbb N^*$ et $A\in M_n(\mathbb K)$,

$$
e^A=\sum_{k=0}^{+\infty}\frac{A^k}{k!}.
$$

**Exemple.** Soit $D=\begin{pmatrix}3&0\\0&-2\end{pmatrix}$. Calculer $e^D$ et $e^{tD}$ pour tout $t\in\mathbb R$.

*Solution : non renseignée dans la source.*

**Exercice.** Soit $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Calculer $e^N$ et $e^{tN}$ pour tout $t\in\mathbb R$.

*Solution : non renseignée dans la source.*

**Exercice.** Calculer $e^N$ et $e^{tN}$ pour tout $t\in\mathbb R$, avec

$$
N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}.
$$

*Aucune solution n’est fournie dans la source.*

**Proposition 2.7.** Soit $n\in\mathbb N^*$ et $A,B,D,P\in M_n(\mathbb K)$, avec $P$ inversible et $D$ diagonale.

1. $e^{O_n}=I_n$.
2. $e^{I_n}=eI_n$.
3. Si $D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)$, alors $e^D=\operatorname{diag}(e^{\lambda_1},\ldots,e^{\lambda_n})$.
4. Si $A=PBP^{-1}$, alors $e^A=Pe^BP^{-1}$.
5. Si $AB=BA$, alors $e^{A+B}=e^Ae^B$.
6. $e^A$ est toujours inversible et $(e^A)^{-1}=e^{-A}$.

*Preuve : non renseignée dans la source.*

**Propriété 2.8.** Soit $A\in M_n(\mathbb R)$. Pour tous $s,t\in\mathbb K$ :

1. $e^{sA}e^{tA}=e^{(s+t)A}$.
2. $e^{tA}e^{-tA}=I_n$.
3. $\dfrac d{dt}(e^{tA})=Ae^{tA}$.
4. $Ae^{tA}=e^{tA}A$.

*Preuve : non renseignée dans la source.*

**Proposition 2.9 — Exponentielle d’une matrice diagonale par blocs.** Si les $A_i$ sont des matrices carrées et

$$
A=\begin{pmatrix}A_1&0&\cdots&0\\0&A_2&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&A_p\end{pmatrix},
$$

alors

$$
e^A=\begin{pmatrix}e^{A_1}&0&\cdots&0\\0&e^{A_2}&\ddots&\vdots\\\vdots&\ddots&\ddots&0\\0&\cdots&0&e^{A_p}\end{pmatrix}.
$$

**Théorème 2.10 — Résolution homogène.** Soit $I\subset\mathbb R$ un intervalle ouvert, $t_0\in I$ et $A\in M_n(\mathbb R)$. La solution générale sur $I$ de $X'=AX$ est

$$
X(t)=e^{tA}C,\qquad C\in M_{n,1}(\mathbb R).
$$

L’unique solution du PVI $X'=AX$, $X(t_0)=X_0$ est

$$
X(t)=e^{(t-t_0)A}X_0.
$$

**Remarque.** La constante du PVI vaut $C=e^{-t_0A}X_0$.

*Preuve : non renseignée dans la source.*

**Remarque de calcul (page 8).** Pour un PVI, le support conseille de conserver une décomposition $e^{tA}=PBP^{-1}$ sans développer le produit des trois matrices. Dans $e^{tA}X_0=PBP^{-1}X_0$, effectuer les produits de droite à gauche économise multiplications et additions.

> Cette remarque utilise $e^{tA}X_0$, qui correspond à $t_0=0$ ; pour une condition initiale en $t_0$, le théorème précédent donne $e^{(t-t_0)A}X_0$. Le $B$ de cette décomposition matricielle est distinct du second membre $B(t)$.

**Théorème 2.11 — Résolution non homogène.** Soit $I\subset\mathbb R$ ouvert, $t_0\in I$, $A\in M_n(\mathbb R)$ et $B\in C(I,M_{n,1}(\mathbb R))$. La solution générale de $X'=AX+B(t)$ est

$$
\begin{aligned}
X(t)&=X_h(t)+X_p(t)\\
&=e^{tA}C+e^{tA}\int e^{-tA}B(t)\,dt\\
&=e^{tA}\left(C+\int e^{-tA}B(t)\,dt\right),\qquad C\in M_{n,1}(\mathbb R).
\end{aligned}
$$

L’unique solution du PVI

$$
\begin{cases}X'(t)=AX(t)+B(t),\\X(t_0)=X_0\end{cases}
$$

est

$$
\begin{aligned}
X(t)&=X_h(t)+X_p(t)\\
&=e^{(t-t_0)A}X_0+e^{(t-t_0)A}\int_{t_0}^t e^{-(s-t_0)A}B(s)\,ds\\
&=e^{(t-t_0)A}X_0+e^{tA}\int_{t_0}^t e^{-sA}B(s)\,ds.
\end{aligned}
$$

*Preuve : non renseignée dans la source.*

**Théorème 2.12 — Couple propre conjugué.** Si une matrice réelle $A\in M_n(\mathbb R)$ admet un couple propre complexe $\{\lambda,v\}$, alors $\{\overline\lambda,\overline v\}$ est également un couple propre de $A$.

*Preuve : non renseignée dans la source.*

**Remarque.** Les racines complexes d’un polynôme à coefficients réels apparaissent par paires conjuguées.
