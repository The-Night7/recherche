---
source: "PREING2-S2/Algebre-lineaire-DS/DS3-2022-2023-Correction_Algebre-lineaire-DS_P2S2_DMaths.pdf"
pages: 5
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Algèbre linéaire et bilinéaire — Devoir surveillé 3 corrigé

CY Tech — Département Mathématiques — PreIng2 — Année 2022/2023.

7 juin 2023. Durée : 90 minutes.

## Consignes (page 1)

Les documents et les supports électroniques sont interdits. L’épreuve est composée de trois exercices indépendants.

Écrire lisiblement le NOM et le PRÉNOM en lettres majuscules. Noter également le NOM ou le NUMÉRO du groupe sur la copie. Tout manquement à ces consignes entraînera des sanctions.

## Exercice 1 — Système différentiel (5 points ; pages 1 et 2)

Résoudre le système différentiel linéaire

$$
\begin{cases}
x'=5x-7y+7z,\\
y'=3x-3y+5z,\\
z'=3x-y+3z.
\end{cases}
$$

### Réponse

On pose

$$
A=\begin{pmatrix}5&-7&7\\3&-3&5\\3&-1&3\end{pmatrix},\qquad
X(t)=\begin{pmatrix}x(t)\\y(t)\\z(t)\end{pmatrix}.
$$

Le système se réécrit $X'(t)=AX(t)$. Pour réduire $A$, on calcule son polynôme caractéristique :

$$
\begin{aligned}
p_A(X)&=(5-X)(-3-X)(3-X)-21-5\times21-21(-3-X)+5(5-X)+21(3-X)\\
&=-X^3+5X^2+9X-45-21-5\times21+3\times21+21X+25-5X+3\times21-21X\\
&=-X^3+5X^2+4X-20\\
&=-(X-2)(X^2-3X-10)\\
&=-(X-2)(X-5)(X+2).
\end{aligned}
$$

La matrice est diagonalisable car $p_A$ est scindé à racines simples. En résolvant les systèmes linéaires pour les valeurs propres $5,2,-2$, on obtient

$$
A=PDP^{-1},\qquad
D=\begin{pmatrix}5&0&0\\0&2&0\\0&0&-2\end{pmatrix},\qquad
P=\begin{pmatrix}1&0&2\\1&1&1\\1&1&-1\end{pmatrix}.
$$

Avec $Y=P^{-1}X$,

$$
\begin{aligned}
X'=AX&\iff Y'=DY\\
&\iff Y(t)=\begin{pmatrix}c_1e^{5t}\\c_2e^{2t}\\c_3e^{-2t}\end{pmatrix}\\
&\iff X(t)=P\begin{pmatrix}c_1e^{5t}\\c_2e^{2t}\\c_3e^{-2t}\end{pmatrix}\\
&\iff X(t)=\begin{pmatrix}c_1e^{5t}+2c_3e^{-2t}\\c_1e^{5t}+c_2e^{2t}+c_3e^{-2t}\\c_1e^{5t}+c_2e^{2t}-c_3e^{-2t}\end{pmatrix},\quad c_1,c_2,c_3\in\mathbb R.
\end{aligned}
$$

L’ensemble des solutions du système homogène est donc

$$
\boxed{\begin{cases}
x(t)=c_1e^{5t}+2c_3e^{-2t},\\
y(t)=c_1e^{5t}+c_2e^{2t}+c_3e^{-2t},\\
z(t)=c_1e^{5t}+c_2e^{2t}-c_3e^{-2t},
\end{cases}\quad c_1,c_2,c_3\in\mathbb R.}
$$

## Exercice 2 — Forme bilinéaire (7 points ; pages 2 à 4)

On fixe $a,b\in\mathbb R$. Pour $x=(x_1,x_2)$ et $y=(y_1,y_2)$, on pose

$$
\varphi(x,y)=ax_1y_1+bx_1y_2+3x_2y_1+x_2y_2.
$$

1. Montrer que, pour tout $a,b\in\mathbb R$, $\varphi$ est une forme bilinéaire sur $\mathbb R^2\times\mathbb R^2$.
2. Montrer que $\varphi$ est symétrique si et seulement si $b=3$.
3. On fixe $b=3$. Montrer que, pour tout $x=(x_1,x_2)$, $\varphi(x,x)=(a-9)x_1^2+(3x_1+x_2)^2$.
4. En déduire une condition nécessaire et suffisante sur $a$ pour que $\varphi$ soit un produit scalaire.

Dans la suite, on fixe $a=13$ et $b=3$.

5. Montrer que $v_1=(1,1)$ et $v_2=(1,-4)$ sont orthogonaux pour $\varphi$.
6. En déduire $\{v_1\}^{\perp}$.
7. Transformer la base $\mathcal B=\{v_1,v_2\}$ en une base orthonormale de $\mathbb R^2$.

### Réponse 1 — Bilinéarité

**Forme.** Pour tous $x,y\in\mathbb R^2$, $\varphi(x,y)$ est réel, car c’est une somme de réels. $\mathbb R^2$ est un espace vectoriel réel.

**Linéarité à gauche.** Pour $x,x',y\in\mathbb R^2$ et $\lambda\in\mathbb R$,

$$
\begin{aligned}
\varphi(x+\lambda x',y)
&=a(x_1+\lambda x'_1)y_1+b(x_1+\lambda x'_1)y_2+3(x_2+\lambda x'_2)y_1+(x_2+\lambda x'_2)y_2\\
&=ax_1y_1+bx_1y_2+3x_2y_1+x_2y_2+\lambda(ax'_1y_1+bx'_1y_2+3x'_2y_1+x'_2y_2)\\
&=\varphi(x,y)+\lambda\varphi(x',y).
\end{aligned}
$$

**Linéarité à droite.** Pour $x,y,y'\in\mathbb R^2$ et $\lambda\in\mathbb R$,

$$
\begin{aligned}
\varphi(x,y+\lambda y')
&=ax_1(y_1+\lambda y'_1)+bx_1(y_2+\lambda y'_2)+3x_2(y_1+\lambda y'_1)+x_2(y_2+\lambda y'_2)\\
&=ax_1y_1+bx_1y_2+3x_2y_1+x_2y_2+\lambda(ax_1y'_1+bx_1y'_2+3x_2y'_1+x_2y'_2)\\
&=\varphi(x,y)+\lambda\varphi(x,y').
\end{aligned}
$$

Ainsi $\varphi$ est bilinéaire sur $\mathbb R^2\times\mathbb R^2$.

### Réponse 2 — Symétrie

$$
\begin{aligned}
\varphi\text{ symétrique}
&\iff \forall x,y\in\mathbb R^2,\quad\varphi(x,y)=\varphi(y,x)\\
&\iff \forall x,y\in\mathbb R^2,\quad ax_1y_1+bx_1y_2+3x_2y_1+x_2y_2=ax_1y_1+bx_2y_1+3x_1y_2+x_2y_2\\
&\iff \forall x,y\in\mathbb R^2,\quad(b-3)x_1y_2=(b-3)x_2y_1\\
&\iff b=3.
\end{aligned}
$$

### Réponse 3 — Forme quadratique

Pour $b=3$ et $x\in\mathbb R^2$,

$$
\begin{aligned}
(a-9)x_1^2+(3x_1+x_2)^2
&=(a-9)x_1^2+9x_1^2+6x_1x_2+x_2^2\\
&=ax_1^2+3x_1x_2+3x_2x_1+x_2^2\\
&=\varphi(x,x).
\end{aligned}
$$

### Réponse 4 — Produit scalaire

Pour $b=3$, la forme est déjà bilinéaire et symétrique. Il reste à déterminer quand elle est définie positive.

Elle est **positive** lorsque $\varphi(x,x)\ge0$ pour tout $x\in\mathbb R^2$. En particulier, pour $x=(1,-3)$,

$$
\varphi(x,x)\ge0\implies(a-9)1^2+0^2\ge0\implies a\ge9.
$$

Cette condition nécessaire est suffisante : si $a\ge9$, les deux termes de $(a-9)x_1^2+(3x_1+x_2)^2$ sont positifs ou nuls.

Elle est **définie** lorsque $\varphi(x,x)=0\iff x=(0,0)$. Pour $a\ge9$, la somme de termes positifs donne

$$
\varphi(x,x)=0\iff
\begin{cases}(a-9)x_1^2=0,\\3x_1+x_2=0.\end{cases}
$$

Cela équivaut aux deux cas suivants : $a\ne9$ et $x_1=x_2=0$, ou $a=9$ et $x_2=-3x_1$. La forme est donc positive et définie si et seulement si $a>9$.

**Conclusion :** avec $b=3$, $\varphi$ est un produit scalaire si et seulement si $a>9$.

### Réponse 5 — Orthogonalité

$$
\varphi(v_1,v_2)=13\times1\times1+3\times1\times(-4)+3\times1\times1+1\times(-4)=0.
$$

Les vecteurs sont donc orthogonaux pour $\varphi$.

### Réponse 6 — Orthogonal de $v_1$

Pour $x=(x_1,x_2)$,

$$
\begin{aligned}
x\in\{v_1\}^{\perp}&\iff\varphi(x,v_1)=0\\
&\iff13x_1+3x_1+3x_2+x_2=0\\
&\iff x_2=-4x_1.
\end{aligned}
$$

Ainsi $\{v_1\}^{\perp}=\operatorname{Vect}(v_2)$.

### Réponse 7 — Normalisation

La base est déjà orthogonale ; il suffit de la normaliser :

$$
\|v_1\|=\sqrt{\varphi(v_1,v_1)}=\sqrt{20}=2\sqrt5,\qquad
\|v_2\|=\sqrt{\varphi(v_2,v_2)}=\sqrt5.
$$

La base orthonormale $\widetilde{\mathcal B}=\{\widetilde v_1,\widetilde v_2\}$ est donnée par

$$
\widetilde v_1=\left(\frac1{2\sqrt5},\frac1{2\sqrt5}\right),\qquad
\widetilde v_2=\left(\frac1{\sqrt5},-\frac4{\sqrt5}\right).
$$

> **Coquilles de la source :** la réponse 3 écrit $x\in\mathbb R$ au lieu de $\mathbb R^2$. La réponse 4 abrège $\varphi(x,x)$ en $\varphi(1,-3)$ lors de l’évaluation en $x=(1,-3)$. Dans la dernière formule de la réponse 7, le second vecteur normalisé est noté $v_2$ au lieu de $\widetilde v_2$. Les notations sont explicitées ci-dessus. Une parenthèse surnuméraire dans le développement de la linéarité à droite a été retirée.

## Exercice 3 — Produit scalaire sur les polynômes (8 points ; pages 4 et 5)

On considère $E=\mathbb R_2[X]$. Pour $P,Q\in E$, on pose

$$
\langle P,Q\rangle=P(-1)Q(-1)+2P(0)Q(0)+P(1)Q(1).
$$

1. Montrer que $\langle\cdot,\cdot\rangle$ est un produit scalaire. On note $\|\cdot\|$ la norme associée.
2. Calculer la norme du polynôme constant $P=1$. On note $P_0=1/\|1\|$.
3. Montrer que $P=X$ est orthogonal à $P_0$.
4. Calculer $\|X\|$. On note $P_1=X/\|X\|$.
5. On pose $Q=X^2-\langle X^2,P_0\rangle P_0-\langle X^2,P_1\rangle P_1$ et $P_2=Q/\|Q\|$. Calculer les coefficients de $P_2$.
6. Montrer que $(P_0,P_1,P_2)$ forme une base orthonormée de $\mathbb R_2[X]$.

### Réponse 1 — Propriétés du produit scalaire

**Forme.** L’application est à valeurs réelles.

> La source écrit « va de $E$ [...] dans $\mathbb R$ » ; le domaine de cette application à deux arguments est $E\times E$.

**Symétrie.** Pour $P,Q\in E$,

$$
\begin{aligned}
\langle Q,P\rangle&=Q(-1)P(-1)+2Q(0)P(0)+Q(1)P(1)\\
&=P(-1)Q(-1)+2P(0)Q(0)+P(1)Q(1)=\langle P,Q\rangle.
\end{aligned}
$$

**Bilinéarité.** Pour $P,\widetilde P,Q\in E$ et $\lambda\in\mathbb R$,

$$
\begin{aligned}
\langle P+\lambda\widetilde P,Q\rangle
&=(P(-1)+\lambda\widetilde P(-1))Q(-1)+2(P(0)+\lambda\widetilde P(0))Q(0)+(P(1)+\lambda\widetilde P(1))Q(1)\\
&=P(-1)Q(-1)+2P(0)Q(0)+P(1)Q(1)+\lambda\bigl(\widetilde P(-1)Q(-1)+2\widetilde P(0)Q(0)+\widetilde P(1)Q(1)\bigr)\\
&=\langle P,Q\rangle+\lambda\langle\widetilde P,Q\rangle.
\end{aligned}
$$

La symétrie permet d’en déduire la linéarité dans le second argument.

**Positivité.** Pour $P\in E$,

$$
\langle P,P\rangle=P(-1)^2+2P(0)^2+P(1)^2\ge0,
$$

car c’est une somme de termes positifs ou nuls.

**Caractère défini.**

$$
\langle P,P\rangle=0\iff P(-1)^2+2P(0)^2+P(1)^2=0
\iff\begin{cases}P(-1)=0,\\P(0)=0,\\P(1)=0.\end{cases}
$$

Le polynôme admet alors les trois racines distinctes $-1,0,1$. Or les éléments de $E$ ont un degré inférieur ou égal à 2 : seul le polynôme nul peut avoir plus de deux racines. Ainsi $\langle P,P\rangle=0\iff P=0$.

> La source écrit deux fois « éléments de $P$ » au lieu de « éléments de $E$ ». Une parenthèse manquante dans le développement de la bilinéarité a également été rétablie.

### Réponse 2 — Norme du polynôme constant

$$
\|1\|=\sqrt{\langle1,1\rangle}=\sqrt{1\times1+2\times1\times1+1\times1}=2.
$$

Donc $P_0=\frac12$.

### Réponse 3 — Orthogonalité de $X$ et $P_0$

$$
\left\langle X,\frac12\right\rangle=-1\times\frac12+2\times0\times\frac12+1\times\frac12=0.
$$

Donc $X$ et $P_0$ sont orthogonaux.

### Réponse 4 — Norme de $X$

$$
\|X\|=\sqrt{\langle X,X\rangle}=\sqrt{-1\times(-1)+2\times0\times0+1\times1}=\sqrt2.
$$

Donc $P_1=\frac1{\sqrt2}X$.

### Réponse 5 — Calcul de $P_2$

D’une part,

$$
\langle X^2,P_0\rangle=(-1)^2\times\frac12+2\times0^2\times\frac12+1^2\times\frac12=1.
$$

D’autre part,

$$
\langle X^2,P_1\rangle=(-1)^2\times\frac1{\sqrt2}(-1)+2\times0^2\times\frac1{\sqrt2}0+1^2\times\frac1{\sqrt2}1=0.
$$

On en déduit

$$
Q=X^2-1\times\frac12-0\times P_1=X^2-\frac12.
$$

De plus,

$$
\|Q\|=\sqrt{\langle Q,Q\rangle}
=\sqrt{\left((-1)^2-\frac12\right)^2+2\left(0-\frac12\right)^2+\left(1-\frac12\right)^2}=1.
$$

Donc $P_2=X^2-\frac12$.

### Réponse 6 — Base orthonormée

Par construction, les trois polynômes ont une norme égale à 1, et l’on sait déjà que $P_0\perp P_1$. Vérifions les deux autres orthogonalités :

$$
\langle P_2,P_0\rangle=\left((-1)^2-\frac12\right)\frac12+2\left(0-\frac12\right)\frac12+\left(1-\frac12\right)\frac12=0,
$$

$$
\langle P_2,P_1\rangle=\left((-1)^2-\frac12\right)\frac{-1}{\sqrt2}+2\left(0-\frac12\right)\frac0{\sqrt2}+\left(1-\frac12\right)\frac1{\sqrt2}=0.
$$

La famille $(P_0,P_1,P_2)$ est libre. Comme $\dim\mathbb R_2[X]=3$, c’est une base. Ses éléments sont de norme 1 et orthogonaux deux à deux : c’est une base orthonormée.
