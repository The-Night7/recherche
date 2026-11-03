# Analyse dans $\mathbb{R}^n$ — Cours (Pré-ING 2, CY Tech)

> Cours de Elian Masnada — polycopié (version du 1er juillet 2026), complété par les slides.
> Notations : $\|\cdot\|$ norme, $B(a,r)$ boule ouverte, $\overline{B}(a,r)$ boule fermée, $S(a,r)$ sphère, $\mathcal{C}_E A$ complémentaire de $A$ dans $E$, $\mathring{A}$ intérieur, $\overline{A}$ adhérence.

## Table des matières

1. Introduction et objectifs
2. Espace vectoriel normé (topologie, suites)
3. Limite et continuité d'applications
4. Calcul différentiel du 1er ordre
5. Calcul différentiel d'ordre supérieur (EDP d'ordre 2, extremums)
A. Annexe : coordonnées polaires dans les EDP

---

# Chapitre 1 — Introduction et objectifs du cours

En Analyse de 1ère année, on a étudié $\mathbb{R}$ et les fonctions $\mathbb{R}\to\mathbb{R}$. Ici on étend ces notions aux fonctions d'un espace vectoriel (souvent $\mathbb{R}^n$, $n\ge1$) vers un autre (souvent $\mathbb{R}^p$).

Exemples : l'énergie interne $U(T,P)$ est une fonction scalaire de $\mathbb{R}^2\to\mathbb{R}$ ; en électromagnétisme, $\vec E,\vec B:\mathbb{R}^3\to\mathbb{R}^3$ sont des champs vectoriels.

Notions généralisées :

1. **Topologie** : norme et distance, EVN, boules ouvertes/fermées, ouvert, fermé, compact, intérieur, adhérence.
2. **Suites** d'éléments d'un EVN : convergence, suites extraites, valeurs d'adhérence.
3. **Fonctions** : limite, continuité (et continuité uniforme), dérivées partielles, différentiabilité, classe $C^k$, développement de Taylor.
4. **Équations aux dérivées partielles (EDP)**, équations dont l'inconnue est une fonction de $\mathbb{R}^n\to\mathbb{R}^p$. Exemple : équation de Gauss
 $$\operatorname{div}\vec E=\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}=\frac{\rho}{\varepsilon_0}.$$
5. **Extremums** d'une fonction (dernier chapitre, applications $\mathbb{R}^2\to\mathbb{R}$).

---

# Chapitre 2 — Espace vectoriel normé

## 2.1 Objectifs

Toutes les notions d'analyse (limite, continuité, dérivée) reposent sur l'idée de **proximité**. Dans $\mathbb{R}$, la limite s'écrit
$$\forall\varepsilon>0,\ \exists\eta>0\ /\ \forall x\in D,\ |x-a|<\eta\implies|f(x)-l|<\varepsilon$$
et $|x-a|$ mesure une distance. Il faut donc : des **normes/distances**, la notion de **voisinage**, de **point intérieur** (on peut bouger légèrement autour sans sortir de l'ensemble), d'**ouvert** (tous les points sont intérieurs), d'**adhérence** (points de $A$ + points approchables par $A$ ; plus petit fermé contenant $A$), de **fermé**. Enfin les **suites** permettent de caractériser ces notions et d'étudier les limites (caractérisation séquentielle).

## 2.2 Éléments de topologie dans $\mathbb{R}^n$

### 2.2.1 Norme et distance

**Définition 1 (norme).** Soit $E$ un espace vectoriel. Une application $\|\cdot\|:E\to\mathbb{R}$ est une **norme** si :

1. $\forall x\in E,\ \|x\|=0\implies x=0_E$ (séparation)
2. $\forall x\in E,\ \forall\lambda\in\mathbb{R},\ \|\lambda x\|=|\lambda|\,\|x\|$ (absolue homogénéité)
3. $\forall x,y\in E,\ \|x+y\|\le\|x\|+\|y\|$ (inégalité triangulaire)

$(E,\|\cdot\|)$ est alors un **espace vectoriel normé (EVN)**.

*Remarque.* On a aussi $x=0_E\implies\|x\|=0$ car $\|0_E\|=\|0\times0_E\|=0\cdot\|0_E\|=0$.

*Remarque.* Sur un espace vectoriel il existe une infinité de normes.

**Normes usuelles sur $\mathbb{R}^n$** ($x=(x_1,\dots,x_n)$) :
$$\|x\|_1=\sum_{i=1}^n|x_i|,\qquad \|x\|_2=\sqrt{\sum_{i=1}^n x_i^2},\qquad \|x\|_\infty=\max_{1\le i\le n}|x_i|.$$

- $\|\cdot\|_2$ : norme **euclidienne** (« à vol d'oiseau ») ; $\|\cdot\|_1$ : norme de **Manhattan** (en suivant le quadrillage).
- Dans $E=\mathbb{R}$ les trois normes coïncident avec $|x|$.
- Les preuves pour $\|\cdot\|_2$ et $\|\cdot\|_\infty$ sont faites en TD1.

*Preuve que $\|\cdot\|_1$ est une norme.*
1. $\|x\|_1=0\Rightarrow\forall i,\ x_i=0\Rightarrow x=0_E$.
2. $\|\lambda x\|_1=\sum|\lambda x_i|=|\lambda|\sum|x_i|=|\lambda|\|x\|_1$.
3. $\|x+y\|_1=\sum|x_i+y_i|\le\sum(|x_i|+|y_i|)=\|x\|_1+\|y\|_1$.

**Normes sur $E=C([0,1],\mathbb{R})$** (fonctions continues de $[0,1]$ dans $\mathbb{R}$) :
$$\|f\|_1=\int_0^1|f(x)|\,dx,\qquad \|f\|_2=\sqrt{\int_0^1 f^2(x)\,dx},\qquad \|f\|_\infty=\sup_{0\le x\le1}|f(x)|.$$

**Exemple (non-norme).** $N:\mathbb{R}^2\to\mathbb{R},\ (x,y)\mapsto|4x+7y|$. Alors $N(x,y)=0\iff x=-\tfrac74y$, ce qui n'implique pas $(x,y)=(0,0)$ : la propriété 1 échoue, $N$ n'est **pas** une norme.

**Propriété 1 (positivité).** $\forall x,\ \|x\|\ge0$.
*Preuve.* $0=\|0_E\|=\|x-x\|\le\|x\|+\|-x\|=2\|x\|$.

**Propriété 2.** Pour la norme euclidienne : $\|x+y\|=\|x\|+\|y\|\iff x=\lambda y$ avec $\lambda\in\mathbb{R}_+$ (admis, cours d'algèbre bilinéaire).
*Contre-exemple pour $\|\cdot\|_\infty$ :* $X=(1,1)$, $Y=(1,0)$, $X+Y=(2,1)$ : $\|X+Y\|_\infty=2=\|X\|_\infty+\|Y\|_\infty$ alors que $X\ne\lambda Y$.

**Propriété 3 (seconde inégalité triangulaire).** $\forall x,y\in E,\ \|x-y\|\ge\big|\,\|x\|-\|y\|\,\big|$.
*Preuve.* $\|x\|=\|x-y+y\|\le\|x-y\|+\|y\|$ et symétriquement $\|y\|\le\|y-x\|+\|x\|$ ; donc $\|x-y\|\ge\max(\|x\|-\|y\|,\|y\|-\|x\|)=\big|\|x\|-\|y\|\big|$.

**Définition 2 (normes équivalentes).** $\|\cdot\|_a$ et $\|\cdot\|_b$ sont **équivalentes** s'il existe $\alpha,\beta>0$ tels que
$$\forall x\in E,\quad \alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a.$$
C'est une relation d'équivalence :
- *réflexive* : $\|x\|_a\le\|x\|_a\le\|x\|_a$ ;
- *symétrique* : de $\alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a$ on tire $\tfrac1\beta\|x\|_b\le\|x\|_a\le\tfrac1\alpha\|x\|_b$ ;
- *transitive* : si $\alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a$ et $\eta\|x\|_b\le\|x\|_c\le\gamma\|x\|_b$, alors $\eta\alpha\|x\|_a\le\|x\|_c\le\gamma\beta\|x\|_a$.

**Théorème 1 (équivalence des normes).** Si $E$ est de **dimension finie**, toutes les normes sur $E$ sont équivalentes. (Admis.)

**Définition 3 (distance).** Soit $X$ un ensemble. $d:X\times X\to\mathbb{R}_+$ est une **distance** si :
1. $d(X,Y)=0\iff X=Y$
2. $d(X,Y)=d(Y,X)$ (symétrie)
3. $d(X,Y)\le d(X,Z)+d(Z,Y)$ (inégalité triangulaire)

**Propriété 4 (positivité).** $d(X,Y)\ge0$ : $0=d(X,X)\le d(X,Y)+d(Y,X)=2d(X,Y)$.

**Propriété 5 (distance associée à une norme).** Si $(E,\|\cdot\|)$ est un EVN, $d(X,Y)=\|X-Y\|$ est une distance.
*Preuve.* (1) $d(X,X)=\|0_E\|=0$ et $\|X-Y\|=0\Rightarrow X=Y$ ; (2) $\|X-Y\|=\|-(Y-X)\|=|{-1}|\,\|Y-X\|$ ; (3) $\|X-Y\|=\|X-Z+Z-Y\|\le\|X-Z\|+\|Z-Y\|$.

**Propriété 6.** Pour la distance associée à une norme : $d(\lambda X,\lambda Y)=|\lambda|\,d(X,Y)$. *(Sert à montrer qu'une distance ne provient d'aucune norme.)*

**Exemples de distances.**
- Sur $(\mathbb{R}^2,\|\cdot\|_2)$ : $d(X,Y)=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2}$.
- **Distance discrète** sur un espace vectoriel quelconque :
$$d_0(X,Y)=\begin{cases}0&\text{si }X=Y\\1&\text{si }X\ne Y\end{cases}$$
 C'est une distance (on vérifie l'inégalité triangulaire par cas), mais elle ne provient d'aucune norme : pour $X\ne Y$ et $\lambda=3$, $d_0(3X,3Y)=1\ne3\,d_0(X,Y)=3$.

### 2.2.2 Boule ouverte, boule fermée, sphère

**Définition 4.** Soit $(E,\|\cdot\|)$ un EVN, $a\in E$, $r>0$.
- Boule ouverte : $B(a,r)=\{x\in E\ /\ \|x-a\|<r\}$
- Boule fermée : $\overline{B}(a,r)=\{x\in E\ /\ \|x-a\|\le r\}$
- Sphère : $S(a,r)=\{x\in E\ /\ \|x-a\|=r\}$

On a $\overline{B}(a,r)=B(a,r)\cup S(a,r)$. La forme des boules dépend de l'espace et de la norme.

**Dans $(\mathbb{R},|\cdot|)$** : $B(a,r)=\,]a-r,a+r[$ et $\overline{B}(a,r)=[a-r,a+r]$.

**Dans $\mathbb{R}^2$, boule fermée de centre $(0,0)$ et rayon $1$ :**
- $\|\cdot\|_1$ : $|x|+|y|\le1$, un **losange** (sphère : $y=\pm(1-x)$, $y=\pm(1+x)$ selon les quadrants) ;
- $\|\cdot\|_2$ : $x^2+y^2\le1$, un **disque** ;
- $\|\cdot\|_\infty$ : $\max(|x|,|y|)\le1$, le **carré** $[-1,1]^2$.

**Propriété 7.** $\forall r,r'>0$, $\forall a$ : $r<r'\iff B(a,r)\subset B(a,r')$ (idem pour les boules fermées).
*Preuve ($\Rightarrow$).* $\|x_0-a\|<r<r'$. *($\Leftarrow$)* Si $r\ge r'$ il existerait $y$ avec $r'\le\|y-a\|<r$, donc $y\in B(a,r)\setminus B(a,r')$.

### 2.2.3 Voisinage

**Définition 5.** $V\subset E$ est un **voisinage** de $a$ si $V$ contient une boule ouverte centrée en $a$ de rayon $r>0$ :
$$V\text{ voisinage de }a\iff\exists r>0\ /\ B(a,r)\subset V.$$
On note $\mathcal{V}(a)$ l'ensemble des voisinages de $a$.

**Propriété 8.** En **dimension finie**, être voisinage de $a$ ne dépend pas de la norme.
*Preuve.* Si $B_{N_1}(a,r)\subset V$ et $\alpha N_1\le N_2\le\beta N_1$, alors pour $X\in B_{N_2}(a,\alpha r)$ : $\alpha N_1(X-a)\le N_2(X-a)<\alpha r$ donc $N_1(X-a)<r$, d'où $B_{N_2}(a,\alpha r)\subset B_{N_1}(a,r)\subset V$.

**Propriété 9.** $\forall V\in\mathcal{V}(a),\ a\in V$ (car $a\in B(a,r)$ puisque $\|a-a\|=0<r$).

**Propriété 10.** Toute boule (ouverte ou fermée) de centre $a$ est un voisinage de $a$ (car $B(a,r/2)\subset B(a,r)$).

**Propriété 11.** Toute **réunion** (quelconque) de voisinages de $a$ est un voisinage de $a$.

**Propriété 12.** Toute **intersection finie** de voisinages de $a$ est un voisinage de $a$ (on prend $r=\min_i r_i>0$).

> ⚠️ **Attention.** Une intersection **infinie** de voisinages n'est pas forcément un voisinage : dans $(\mathbb{R},|\cdot|)$, $V_n=\left]-\tfrac1n,\tfrac1n\right[$ vérifie $\bigcap_{n\ge1}V_n=\{0\}$, qui ne contient aucune boule ouverte.

**Définition 6 (espace séparé).** $E$ est **séparé** si pour tous $a\ne b$ il existe $V_a\in\mathcal{V}(a)$, $V_b\in\mathcal{V}(b)$ avec $V_a\cap V_b=\varnothing$.

**Propriété 13.** Tout EVN est séparé.
*Preuve.* Prendre $V_a=B\!\left(a,\tfrac{\|b-a\|}{2}\right)$ et $V_b=B\!\left(b,\tfrac{\|b-a\|}{2}\right)$. Si $x\in V_a\cap V_b$ : $\|a-b\|\le\|a-x\|+\|x-b\|<\|a-b\|$, absurde.

### 2.2.4 Ouvert, fermé

**Définition 7 (ouvert).** $U\subset E$ est un **ouvert** s'il est voisinage de chacun de ses points :
$$U\text{ ouvert}\iff\forall x\in U,\ \exists r>0\ /\ B(x,r)\subset U.$$
Le rayon $r$ dépend de $x$ (plus on s'approche du bord, plus $r$ doit être petit). Sur les schémas, un ouvert a un contour en pointillé.

*Exemple de non-ouvert.* $A=\{(x,y)\in\mathbb{R}^2\ /\ |y|\le1,\ |x|<1\}$ et $a=(\tfrac12,1)\in A$. Pour tout $r>0$, $M=(\tfrac12,1+\tfrac r2)\in B(a,r)$ (car $\|M-a\|_2=\tfrac r2<r$) mais $M\notin A$. Donc $A$ n'est pas ouvert.

**Propriété 14.** En dimension finie, être ouvert ne dépend pas de la norme (conséquence de la propriété 8).

**Propriété 15.** $\varnothing$ et $E$ sont des ouverts.

**Propriété 16.** Une **boule ouverte est un ouvert.**
*Preuve.* Soit $X\in B(a,r)$ et $r'=r-\|X-a\|>0$. Pour $Y\in B(X,r')$ : $\|Y-a\|\le\|Y-X\|+\|X-a\|<r'+\|X-a\|=r$. Donc $B(X,r')\subset B(a,r)$.

**Propriété 17.** Toute **union quelconque** d'ouverts est un ouvert.
**Propriété 18.** Toute **intersection finie** d'ouverts est un ouvert (en $x$, intersection finie de voisinages de $x$).

**Corollaire.** Pour $a<b$, les intervalles $]-\infty,b[$, $]a,b[$, $]a,+\infty[$ sont ouverts :
$]a,b[=B\!\left(\tfrac{a+b}2,\tfrac{b-a}2\right)$, $]-\infty,b[=\bigcup_{\alpha<b}]\alpha,b[$, $]a,\infty[=\bigcup_{\alpha>a}]a,\alpha[$.

**Définition 8 (fermé).** $F\subset E$ est un **fermé** si $\mathcal{C}_EF$ est un ouvert.

*Intuition.* (i) un ensemble est ouvert s'il ne contient pas son bord ; (ii) il n'est pas ouvert s'il contient au moins un point de son bord ; (iii) il est fermé s'il contient son bord ; (iv) il n'est pas fermé s'il lui manque au moins un point de son bord.

**Propriété 19.** $\varnothing$ et $E$ sont des fermés (donc à la fois ouverts et fermés).

**Propriété 20.** Une **boule fermée est un fermé.**
*Preuve.* Soit $X\in\mathcal{C}_E\overline{B}(a,r)$, i.e. $\|X-a\|>r$. Pour $Y\in B(X,\|X-a\|-r)$ : $\|X-a\|\le\|X-Y\|+\|Y-a\|<\|X-a\|-r+\|Y-a\|$, d'où $\|Y-a\|>r$. Donc $B(X,\|X-a\|-r)\subset\mathcal{C}_E\overline{B}(a,r)$ avec rayon $>0$.

**Propriété 21.** Toute **intersection quelconque** de fermés est un fermé (passage au complémentaire : $\mathcal{C}_E(\bigcup U_i)=\bigcap\mathcal{C}_EU_i$).
**Propriété 22.** Toute **union finie** de fermés est un fermé.

**Corollaire.** Pour $a<b$, $]-\infty,b]$, $[a,b]=\overline{B}\!\left(\tfrac{a+b}2,\tfrac{b-a}2\right)$, $[a,+\infty[$ sont fermés.

### 2.2.5 Intérieur et adhérence

**Définition 9 (intérieur).** Soit $A\subset E$. Un point $a$ est **intérieur** à $A$ si $A$ est un voisinage de $a$. L'ensemble des points intérieurs est l'**intérieur** de $A$, noté $\mathring{A}$ :
$$x\in\mathring{A}\iff\exists r>0\ /\ B(x,r)\subset A.$$
Intuitivement, $\mathring{A}$ s'obtient en « enlevant le bord » de $A$.

**Propriété 23.** $\mathring{A}\subset A$.

**Propriété 24.** $\mathring{A}$ est le **plus grand ouvert contenu dans $A$** (c'est la réunion de tous les ouverts inclus dans $A$).
*Preuve.* (i) Tout ouvert $U\subset A$ vérifie $\forall x\in U,\ \exists r,\ B(x,r)\subset U\subset A$, donc $U\subset\mathring{A}$. (ii) Si $x\in\mathring{A}$, $B(x,r)\subset A$ est un ouvert contenant $x$ et inclus dans $A$. Donc $\mathring{A}=\bigcup\{U\text{ ouvert},\ U\subset A\}$.

**Propriété 25.**
1. $A$ ouvert $\iff\mathring{A}=A$
2. $\mathring{\mathring{A}}=\mathring{A}$
3. $A\subset B\implies\mathring{A}\subset\mathring{B}$

**Exemples.** Dans $\mathbb{R}$ (pour $a<b$) : l'intérieur de $]a,b[$, de $[a,b[$, de $]a,b]$ et de $[a,b]$ est toujours $]a,b[$. Dans $\mathbb{R}^n$ : l'intérieur de $\overline{B}(a,r)$ est $B(a,r)$, et celui de $B(a,r)$ est $B(a,r)$.

**Définition 10 (adhérence).** $a$ est **adhérent** à $A$ si tout voisinage de $a$ rencontre $A$. L'ensemble des points adhérents est l'**adhérence** $\overline{A}$ :
$$x\in\overline{A}\iff\forall r>0,\ B(x,r)\cap A\ne\varnothing.$$

**Propriété 26.** $A\subset\overline{A}$ (car $x\in A\cap B(x,r)$).

**Propriété 27.** $\overline{A}$ est un fermé.
*Preuve.* Si $x\in\mathcal{C}_E\overline{A}$ alors $\exists r>0$, $B(x,r)\cap A=\varnothing$, donc $B(x,r)\subset\mathcal{C}_E\overline{A}$ : le complémentaire est ouvert.

**Propriété 28.** $\overline{A}$ est le **plus petit fermé contenant $A$** (démontré plus tard).

**Propriété 29.**
1. $A$ fermé $\iff\overline{A}=A$
2. $\overline{\overline{A}}=\overline{A}$
3. $A\subset B\implies\overline{A}\subset\overline{B}$

**Propriété 30.** Pour $A,B\subset E$ :
1. $\overline{A\cup B}=\overline{A}\cup\overline{B}$
2. $\overline{A\cap B}\subset\overline{A}\cap\overline{B}$ (inclusion stricte possible)
3. $\operatorname{int}(A\cap B)=\mathring{A}\cap\mathring{B}$
4. $\mathring{A}\cup\mathring{B}\subset\operatorname{int}(A\cup B)$ (inclusion stricte possible)

*Contre-exemples dans $\mathbb{R}$.* Pour 2 : $A=]0,1[$, $B=[1,2[$ : $A\cap B=\varnothing$ donc $\overline{A\cap B}=\varnothing$, mais $\overline{A}\cap\overline{B}=[0,1]\cap[1,2]=\{1\}$. Pour 4 : $A=[0,1]$, $B=[1,2]$ : $\mathring{A}\cup\mathring{B}=]0,1[\,\cup\,]1,2[$ mais $\operatorname{int}(A\cup B)=\,]0,2[$.

**Définition 11 (frontière).** $\partial A=\operatorname{Fr}(A)=\overline{A}\setminus\mathring{A}$.
Exemple : $\partial B(a,r)=\overline{B}(a,r)\setminus B(a,r)=S(a,r)$.

**Propriété 31.** $\overline{A}=\mathring{A}\cup\partial A$ et $\mathring{A}=\overline{A}\setminus\partial A$.

### 2.2.6 Méthodologies

- **Montrer que $A$ n'est pas ouvert** : trouver un point (de la frontière) tel que toute boule centrée en ce point sorte de $A$.
- **Montrer que $A$ n'est pas fermé** : montrer que $\mathcal{C}_EA$ n'est pas ouvert (même méthode sur le complémentaire).
- **Trouver l'adhérence $\overline{A}$** (voir TD3) : on propose un candidat $B$ et on vérifie
 1. $B$ est fermé ;
 2. $A\subset B$ (donc $\overline{A}\subset B$ : $B$ n'est pas trop petit) ;
 3. $B$ n'est pas trop grand : pour tout $x\in B\setminus A$, $\forall r>0,\ B(x,r)\cap A\ne\varnothing$. Sinon on retire les points qui ne vérifient pas cette condition.
- **Trouver l'intérieur $\mathring{A}$** : on propose un candidat $B$ et on vérifie
 1. $B$ est ouvert ;
 2. $B\subset A$ (donc $B\subset\mathring{A}$) ;
 3. $B$ n'est pas trop petit : pour tout $x\in A\setminus B$, $\forall r>0,\ B(x,r)\not\subset A$. Sinon $B$ est trop petit.

## 2.3 Suites d'éléments d'un EVN

### 2.3.1 Rappels

Une suite réelle est une application $\mathbb{N}\to\mathbb{R}$, notée $(x_n)_{n\in\mathbb{N}}$. Elle converge vers $l\in\mathbb{R}$ si
$$\forall\varepsilon>0,\ \exists N\in\mathbb{N}\ /\ \forall n\ge N,\ |x_n-l|<\varepsilon,$$
et la limite, si elle existe, est unique.

### 2.3.2 Généralisation

**Définition 12.** Une **suite d'éléments d'un EVN** $E$ est une application $\mathbb{N}\to E$. Exemple dans $\mathbb{R}^3$ : $n\mapsto\left(\tfrac1n,\ 2n+3,\ (\tfrac32)^n\right)$.

**Définition 13 (suite bornée).** $(x_n)$ est **bornée** si la suite réelle $(\|x_n\|)$ est bornée :
$$\exists M>0\ /\ \forall n\in\mathbb{N},\ \|x_n\|\le M\quad(M\text{ indépendant de }n).$$
- $x_n=-1/n$ dans $(\mathbb{R},|\cdot|)$ : $\|x_n\|=1/n\le1$, bornée.
- $x_n=(2n,-3n,1/n)$ dans $(\mathbb{R}^3,\|\cdot\|_2)$ : $\|x_n\|_2=\sqrt{13n^2+1/n^2}\to+\infty$, non bornée.

### 2.3.3 Suites convergentes

**Définition 14.** $(x_n)$ **converge** vers $l\in E$ si l'une des propriétés équivalentes suivantes est vérifiée :
1. $\forall\varepsilon>0,\ \exists N\ /\ \forall n\ge N,\ \|x_n-l\|<\varepsilon$
2. $\forall\varepsilon>0,\ \exists N\ /\ \forall n\ge N,\ x_n\in B(l,\varepsilon)$
3. $\forall V\in\mathcal{V}(l),\ \exists N\ /\ \forall n\ge N,\ x_n\in V$

**Propriété 32 (unicité de la limite).** Si $(x_n)$ converge, sa limite est unique, notée $\lim_{n\to\infty}x_n=l$.
*Preuve.* Si $l_1\ne l_2$ étaient deux limites, comme $E$ est séparé il existe $V_1\in\mathcal{V}(l_1)$, $V_2\in\mathcal{V}(l_2)$ disjoints ; pour $n\ge\max(N_1,N_2)$, $x_n\in V_1\cap V_2=\varnothing$ : absurde.

**Propriété 33.** Si $x_n\to l$ et $y_n\to l'$ :
1. $x_n\to l\implies\|x_n\|\to\|l\|$ (**réciproque fausse** : $x_n=(-1)^n$, $\|x_n\|=1$ mais $(x_n)$ diverge)
2. $x_n\to0_E\iff\|x_n\|\to0$
3. $x_n+\lambda y_n\to l+\lambda l'$ ($\lambda\in\mathbb{R}^*$)

*Preuve de 1.* $\big|\|x_n\|-\|l\|\big|\le\|x_n-l\|<\varepsilon$ (seconde inégalité triangulaire).
*Preuve de 3.* $\|(x_n+\lambda y_n)-(l+\lambda l')\|\le\|x_n-l\|+|\lambda|\|y_n-l'\|<\tfrac\varepsilon2+|\lambda|\tfrac{\varepsilon}{2|\lambda|}=\varepsilon$ pour $n\ge\max(N,N')$.

**Propriété 34 (convergence composante par composante).** Dans $\mathbb{R}^p$, $x_n=(x_n^{(1)},\dots,x_n^{(p)})$ :
$$\lim_{n\to\infty}x_n=(l_1,\dots,l_p)\quad\text{avec}\quad l_i=\lim_{n\to\infty}x_n^{(i)}.$$
*(Preuve : décomposer sur une base $(e_i)$ et majorer par $\sum_i\frac\varepsilon p$.)*

**Exemple.** $x_n=\left(1-\tfrac1n,\ \tfrac1{n^2}\right)\to(1,0)$.

### 2.3.4 Valeur d'adhérence et point adhérent

**Suite extraite.** Soit $\varphi:\mathbb{N}\to\mathbb{N}$ **strictement croissante**. La suite $(y_n)$ avec $y_n=x_{\varphi(n)}$ est une suite extraite de $(x_n)$. (On ne peut pas « revenir en arrière » : par ex. $n=1,2,20,18$ n'est pas permis.)
Exemple : de $x_n=\left((-1)^n,\tfrac1{n^2}\right)$, la suite extraite des rangs pairs est $y_n=x_{2n}=\left(1,\tfrac1{(2n)^2}\right)$.

**Propriété 35.** Si $x_n\to l$, toute suite extraite converge aussi vers $l$.
*Preuve.* $\varphi$ strictement croissante implique $\varphi(n)\ge n$ (récurrence), donc $n\ge N\implies\varphi(n)\ge N\implies\|x_{\varphi(n)}-l\|<\varepsilon$.

**Définition 15 (valeur d'adhérence).** $a\in E$ est **valeur d'adhérence** de $(x_n)$ si l'une des propriétés équivalentes suivantes est vraie :
1. il existe une suite extraite de $(x_n)$ qui converge vers $a$ ;
2. $\forall\varepsilon>0,\ \{n\in\mathbb{N}\ /\ \|x_n-a\|<\varepsilon\}$ est **infini** ;
3. $\forall V\in\mathcal{V}(a),\ \{n\ /\ x_n\in V\}$ est infini.

Exemple : $x_n=(-1)^n$ est bornée, a deux valeurs d'adhérence ($1$ et $-1$) et ne converge pas.

**Propriété 36.** Si $x_n\to l$, alors $l$ est l'**unique** valeur d'adhérence.
**Attention** : la réciproque est fausse. Ex. $x_{2n}=2n$, $x_{2n+1}=1$ : $1$ est la seule valeur d'adhérence mais la suite diverge.

**Propriété 37.** Pour $A\subset E$ et $a\in E$, équivalence de :
1. $a\in\overline{A}$ ;
2. il existe une suite d'éléments de $A$ dont $a$ est valeur d'adhérence ;
3. il existe une suite d'éléments de $A$ qui converge vers $a$.

*Preuve de 1 ⇒ 3.* Pour tout $n\ge1$, $B(a,\tfrac1n)\cap A\ne\varnothing$ : choisir $x_n$ dedans, alors $\|x_n-a\|<\tfrac1n\to0$.

**Propriété 38 (caractérisation séquentielle).**
1. $\overline{A}$ est l'ensemble des limites des suites convergentes d'éléments de $A$.
2. $A$ est **fermé** $\iff$ toute suite convergente d'éléments de $A$ a sa limite dans $A$.

---

# Chapitre 3 — Limite et continuité d'applications

## 3.1 Objectifs

Généraliser limite et continuité aux fonctions $\mathbb{R}^p\to\mathbb{R}^n$ (plusieurs variables). Rappels de pré-ING 1 :
- $\lim_{x\to a}f(x)=l\iff\forall\varepsilon,\ \exists\alpha>0,\ (\forall x\in D,\ |x-a|<\alpha)\Rightarrow|f(x)-l|<\varepsilon$.
- Si $a\in D$ et pas de forme indéterminée, $\lim_{x\to a}f(x)=f(a)$ ; sinon on lève l'indétermination : $\lim_{x\to0}\dfrac{x^3}{x^2-x}=\lim\dfrac{x^2}{x-1}=0$.
- $f$ continue en $a$ $\iff\lim_{x\to a^-}f=\lim_{x\to a^+}f=f(a)$. Exemple : la fonction de Heaviside n'a pas de limite en $0$.

Exemples de fonctions étudiées : $f(x,y)=\dfrac{xy}{x^2+y^2}$ et $g(x,y)=\left(\dfrac{x^2+y^2-1}{x},\ \dfrac{\sin(x^2)+\sin(y^2)}{\sqrt{x^2+y^2}}\right)$.

## 3.2 Limite, continuité

**Définition 1 (limite).** Soient $(E,\|\cdot\|_E)$, $(F,\|\cdot\|_F)$ deux EVN, $A\subset E$, $f:A\to F$, $a\in A$ (adhérent à $A$), $l\in F$. $f$ admet pour limite $l$ en $a$ si l'une des propriétés équivalentes suivantes est vérifiée :

1. $\forall\varepsilon>0,\ \exists\eta>0,\ \forall x\in A,\ \|x-a\|_E<\eta\implies\|f(x)-l\|_F<\varepsilon$
2. $\forall\varepsilon>0,\ \exists\eta>0,\ \forall x\in A,\ x\in B_E(a,\eta)\implies f(x)\in B_F(l,\varepsilon)$
3. $\forall V_F\in\mathcal{V}(l),\ \exists V_E\in\mathcal{V}(a),\ \forall x\in A,\ (x\in V_E\implies f(x)\in V_F)$
4. $\forall V_F\in\mathcal{V}(l),\ \exists V_E\in\mathcal{V}(a),\ f(V_E\cap A)\subset V_F$

*Remarques.* $\varepsilon$ est la précision sur $f(x)$ ; si $\varepsilon\to0$ alors $\eta\to0$. Si $f$ est définie en $a$ et sans indétermination, la limite est $f(a)$. Exemple : $f(x,y)=\dfrac{xy}{x^2+y^2}$ vaut $f(1,1)=\tfrac12$ en $a=(1,1)$ ; en $(0,0)$ c'est une forme indéterminée $\tfrac00$.

**Propriété 1 (unicité de la limite).** Si $f$ admet une limite en $a$, elle est unique : $\lim_{x\to a}f(x)=l$.
*Preuve.* Si $l\ne l'$, poser $\varepsilon=\tfrac13\|l-l'\|_F$ ; pour $\|x-a\|<\min(\eta,\eta')$, $3\varepsilon=\|l-l'\|\le\|l-f(x)\|+\|f(x)-l'\|<2\varepsilon$, absurde.

**Exemple (absence de limite, coordonnées polaires).** $f(x,y)=\dfrac{xy}{x^2+y^2}$ devient $\tilde f(\rho,\theta)=\cos\theta\sin\theta$. En $(0,0)$ : pour $\theta=\tfrac\pi4$ on trouve $\tfrac12$, pour $\theta=-\tfrac\pi4$ on trouve $-\tfrac12$. Deux chemins, deux valeurs : **$f$ n'a pas de limite en $(0,0)$**.

*Remarque.* Dans $\mathbb{R}$, on ne s'approche d'un point que par deux côtés ; dans $\mathbb{R}^p$ ($p>1$) il y a une **infinité de chemins**, et la limite n'existe que si **tous** donnent la même valeur.

**Propriété 2.** Remplacer $\|\cdot\|_E$, $\|\cdot\|_F$ par des normes équivalentes ne change ni l'existence ni la valeur de la limite.
*Preuve.* Avec $\alpha\|\cdot\|_2\le\|\cdot\|_1\le\beta\|\cdot\|_2$ sur $E$ et $\gamma\|\cdot\|_{2}\le\|\cdot\|_{1}$ sur $F$ : si $\|x-a\|_{1,E}<\eta$ alors $\|x-a\|_{2,E}<\eta/\alpha$, et $\|f(x)-l\|_{1,F}<\varepsilon\implies\|f(x)-l\|_{2,F}<\varepsilon/\gamma$.

**Propriété 3 (linéarité).** Si $f\to l_1$ et $g\to l_2$ en $a$ alors $f+\lambda g\to l_1+\lambda l_2$.

**Propriété 4 (produit, quotient).** Pour $f,g:A\to\mathbb{R}$ de limites $l_1,l_2$ en $a$ : $\lim fg=l_1l_2$ et, si $l_2\ne0$, $\lim f/g=l_1/l_2$.

**Propriété 5 (composantes).** Pour $f:\mathbb{R}^p\to\mathbb{R}^n$, $f$ a pour limite $l=(l_1,\dots,l_n)$ en $a$ ssi chaque composante $f_i$ a pour limite $l_i$.

*Exemple.* $f(x,y)=\left(\dfrac{xy^2}{x^2+y^2},\ \dfrac{xy}{x^2+y^2}\right)$ : la 2ᵉ composante n'a pas de limite en $(0,0)$, donc $f$ non plus. La 1ʳᵉ, en polaires, vaut $\dfrac{\rho^3\cos\theta\sin^2\theta}{\rho^2}=\rho\cos\theta\sin^2\theta\to0$ pour tout $\theta$.

**Définition 2 (continuité).** $f:A\to F$ est **continue en $a$** si elle admet une limite en $a$ (qui vaut alors $f(a)$) ; **continue sur $A$** si elle l'est en tout point. On note $C(A,F)$ l'ensemble des fonctions continues de $A$ dans $F$.

**Théorème 1 (caractérisation séquentielle de la limite).** $f$ admet la limite $l$ en $a$ ssi pour **toute** suite $(x_n)$ d'éléments de $A$ convergeant vers $a$, la suite $(f(x_n))$ converge vers $l$. (Admis.)

**Corollaire (continuité séquentielle).** $f$ est continue en $a$ ssi pour toute suite $x_n\to a$ dans $A$, $f(x_n)\to f(a)$.

*Exemple.* $f(x,y)=\dfrac{xy}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. Avec $u_n=(\tfrac1n,\tfrac1n)\to(0,0)$ : $f(u_n)=\tfrac12\not\to f(0,0)=0$. Donc $f$ n'est pas continue en $(0,0)$.

### 3.2.1 Méthodologie : limite de $f(x,y)$ en $(x_0,y_0)$

**Étape 1.** Calculer $f(x_0,y_0)$. Pas de forme indéterminée ($0\times\infty$, $\infty/\infty$, $0/0$, $\infty-\infty$…) ⇒ $\lim f=f(x_0,y_0)$. Sinon, étape 2.

**Étape 2.** Objectif : soit montrer que **deux chemins** donnent des valeurs différentes (⇒ pas de limite), soit trouver un **candidat** $l_c$ commun à tous les chemins testés.
1. **Coordonnées polaires** (si le dénominateur s'y prête, p. ex. $(x-x_0)^2+(y-y_0)^2$) : $x=x_0+\rho\cos\theta$, $y=y_0+\rho\sin\theta$, $\tilde f(\rho,\theta)=f(x,y)$ et
 $$\lim_{(x,y)\to(x_0,y_0)}f(x,y)=\lim_{(\rho,\theta)\to(0,\theta)}\tilde f(\rho,\theta).$$
 Si le résultat **ne dépend pas de $\theta$** : limite. S'il **dépend de $\theta$** : pas de limite.
2. Sinon, tester des chemins :
 - (a) **caractérisation séquentielle** : suites $u_n\to(x_0,y_0)$, on calcule $\lim f(u_n)$ ;
 - (b) **chemins cartésiens** $(x,\alpha(x))$ avec $\alpha:\mathbb{R}\to\mathbb{R}$.

**Étape 3.** Si tous les chemins donnent $l_c$ : calculer $|f(x,y)-l_c|$. S'il tend vers $0$ quand $(x,y)\to(x_0,y_0)$, alors $\lim f=l_c$ ; sinon, pas de limite.

> ⚠️ Que deux chemins donnent la même valeur ne prouve pas l'existence de la limite : l'étape 3 est nécessaire.

**Exemple 2.** $f_2(x,y)=1+\dfrac{x^3}{x^2+y^2}$ en $(0,0)$ ($0/0$). Les chemins testés donnent tous $1$ (candidat $l_c=1$). Puis
$$|f_2(x,y)-1|=\frac{|x|^3}{x^2+y^2}=\frac{x^2}{x^2+y^2}|x|\le|x|\xrightarrow[(x,y)\to(0,0)]{}0,$$
donc $\lim_{(x,y)\to(0,0)}f_2(x,y)=1$.

*(En TD : usage des équivalents et développements limités pour les limites de fonctions $\mathbb{R}^2\to\mathbb{R}$.)*

---

# Chapitre 4 — Calcul différentiel du 1er ordre

## 4.1 Objectifs

Généraliser la dérivée (dérivée partielle), la différentiabilité (différentielle, classe $C^1$) et les équations différentielles d'ordre 1 (EDP du 1er ordre).

Exemple : $f(x,y)=(x+y,\ x^2-y^2,\ x^2y)$ donne
$$\frac{\partial f}{\partial x}=(1,2x,2xy),\qquad\frac{\partial f}{\partial y}=(1,-2y,x^2).$$
Gradient d'un champ scalaire (ex. $\vec F=-\vec\nabla V$) : pour $f(x,y)=x^2+xy$, $\vec\nabla f=(2x+y,\ x)$.

## 4.2 Dérivée partielle

**Définition 1 (dérivée partielle).** Soit $U$ un ouvert de $\mathbb{R}^p$, $a\in U$, $f:U\to\mathbb{R}$, $(e_1,\dots,e_p)$ la base canonique. $f$ admet une **dérivée partielle première en $a$ par rapport à la $j$-ème variable** si
$$\varphi_j:t\mapsto f(a+te_j)$$
(définie sur $D_j=\{t\in\mathbb{R}\ /\ a+te_j\in U\}$) est dérivable en $0$. Alors
$$\frac{\partial f}{\partial x_j}(a)=\varphi_j'(0)=\lim_{t\to0}\frac{f(a+te_j)-f(a)}{t}.$$
Notation physicienne : $\left.\dfrac{\partial f}{\partial x_j}\right|_a$.

**Exemple.** $f(x,y)=3x^2+xy-2y^2$ : $\dfrac{\partial f}{\partial x}=\lim_{t\to0}\dfrac{f(x+t,y)-f(x,y)}{t}=\lim(3t+6x+y)=6x+y$ (équivaut à **fixer $y$** et dériver en $x$), et $\dfrac{\partial f}{\partial y}=x-4y$.

*Signification graphique.* $\dfrac{\partial f}{\partial x}(x_0,y_0)$ est la dérivée en $x_0$ de $x\mapsto f(x,y_0)$ (intersection du graphe avec le plan $y=y_0$).

> ⚠️ **Remarque importante.** L'existence de toutes les dérivées partielles en $a$ n'implique **pas** la continuité en $a$ (les dérivées partielles ne regardent que les directions de la base canonique). Exemple : $f(x,y)=\dfrac{xy}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$ n'est pas continue en $0$ (cf. $u_n=(1/n,1/n)$), mais $\dfrac{\partial f}{\partial x}(0,0)=\lim\dfrac{f(t,0)-f(0,0)}{t}=0$ et $\dfrac{\partial f}{\partial y}(0,0)=0$.

**Propriété 1.** Pour $f:U\to\mathbb{R}^n$, $f$ admet une dérivée partielle par rapport à $x_j$ ssi chaque composante $f_i$ en admet une, et
$$\frac{\partial f}{\partial x_j}(a)=\left(\frac{\partial f_1}{\partial x_j}(a),\dots,\frac{\partial f_n}{\partial x_j}(a)\right).$$

## 4.3 Fonctions différentiables sur un ouvert

### 4.3.1 Généralités

**Définition 2 (différentiabilité).** Soit $U$ ouvert de $\mathbb{R}^p$, $a\in U$, $f:U\to(F,\|\cdot\|_F)$, $U_0=\{h\in\mathbb{R}^p\ /\ a+h\in U\}$. $f$ est **différentiable en $a$** s'il existe une application **linéaire** $l:\mathbb{R}^p\to F$ et une application $\varepsilon:U_0\to F$ telles que
1. $\lim_{h\to0_{\mathbb{R}^p}}\varepsilon(h)=0_F$
2. $\forall h\in U_0,\ f(a+h)=f(a)+l(h)+\|h\|\,\varepsilon(h)$ (développement limité à l'ordre 1).

$f$ est différentiable sur $U$ si elle l'est en tout point de $U$.

**Théorème 1 (différentielle).** Si $f$ est différentiable en $a$, l'application linéaire $l$ est **unique** ; c'est la **différentielle** de $f$ en $a$, notée $D_af$.
*Idée de preuve.* Si $l_1,l_2$ conviennent, alors $0=l_1(h)-l_2(h)+\|h\|(\varepsilon_1-\varepsilon_2)(h)$. En remplaçant $h$ par $th_0$ ($t\to0$, $h_0\in B(0,r)$) et en simplifiant par $t$, on obtient $l_1(h_0)=l_2(h_0)$ sur la boule ; par linéarité (poser $\tilde h=\frac{r}{2\|h\|}h$) on étend à tout $\mathbb{R}^p$.

**Propriété 2.** Toute application **linéaire** $\varphi:\mathbb{R}^p\to F$ est différentiable et $D_a\varphi=\varphi$ pour tout $a$.

**Propriété 3.** Si $f$ est différentiable en $a$, alors toutes ses dérivées partielles premières existent en $a$ et
$$D_af:h=(h_1,\dots,h_p)\mapsto D_af(h)=\sum_{i=1}^p h_i\,\frac{\partial f}{\partial x_i}(a).$$
*Preuve.* $\dfrac{\partial f}{\partial x_j}(a)=\lim_{t\to0}\dfrac{D_af(te_j)+\|te_j\|\varepsilon(te_j)}{t}=D_af(e_j)$, puis linéarité sur $h=\sum h_ie_i$.

*Lien avec la physique.* La différentielle de l'énergie interne $U(T,V)$ est $dU=\dfrac{\partial U}{\partial T}dT+\dfrac{\partial U}{\partial V}dV$ : c'est exactement $D_af(h)$ avec $(dT,dV)\leftrightarrow h$. $D_af(h)$ est la variation de $f$ lorsqu'on se déplace de $h$ à partir de $a$ (d'autant plus juste que $h\to0$).

**Propriété 4.** $f$ différentiable en $a$ $\implies$ $f$ continue en $a$.
*Preuve.* $\|f(a+h)-f(a)\|_F\le\sum_j|h_j|\left\|\dfrac{\partial f}{\partial x_j}(a)\right\|_F+\|h\|\,\|\varepsilon(h)\|_F\to0$.

**Théorème 2 (différentiabilité sur $\mathbb{R}^2$).** Soit $U$ ouvert de $\mathbb{R}^2$, $(x,y)\in U$, $f:U\to F$. Alors $f$ est différentiable en $(x,y)$ si et seulement si
$$\lim_{(h_1,h_2)\to(0,0)}\frac{1}{\|(h_1,h_2)\|}\left(f(x+h_1,y+h_2)-f(x,y)-h_1\frac{\partial f}{\partial x}(x,y)-h_2\frac{\partial f}{\partial y}(x,y)\right)=0_F,$$
la norme choisie n'ayant pas d'influence sur le résultat.

*Preuve.* ($\Rightarrow$) Si $f$ est différentiable, $f(x+h_1,y+h_2)=f(x,y)+h_1\partial_xf+h_2\partial_yf+\|h\|\varepsilon(h)$ avec $\varepsilon\to0$ : on divise par $\|h\|$. ($\Leftarrow$) On pose $\varepsilon(h_1,h_2)$ égal à l'expression de la limite (qui tend vers $0_F$) ; en la réarrangeant on retrouve exactement la définition de la différentielle.

### 4.3.2 Fonctions de classe $C^1$

**Définition 3 ($C^1$).** $f:U\to F$ ($U$ ouvert de $\mathbb{R}^p$) est de **classe $C^1$ sur $U$** si toutes ses dérivées partielles premières existent et sont **continues** en tout point de $U$. On note $C^1(U,F)$ l'ensemble de ces applications.

**Propriété 5.** Toute application linéaire $\varphi:\mathbb{R}^p\to F$ est $C^1$ sur $\mathbb{R}^p$ ($\partial_{x_i}\varphi(a)=\varphi(e_i)$ est constante).

**Théorème 3.** Si $f$ est de classe $C^1$ sur $U$, alors
1. $f$ est **différentiable** sur $U$ (admis) ;
2. $f$ est **continue** sur $U$ (par la propriété 4).

**Schéma récapitulatif.**
$$f\ \text{de classe }C^1\ \Longrightarrow\ f\ \text{différentiable}\ \Longrightarrow\ \begin{cases}f\ \text{continue}\\ \text{dérivées partielles premières existent}\end{cases}$$
Aucune réciproque n'est vraie en général. Si $f$ est seulement différentiable en $a$, les dérivées partielles existent mais ne sont pas forcément continues.

**Contre-exemple : différentiable mais pas $C^1$.**
$$f(x,y)=\begin{cases}(x^2+y^2)\sin\dfrac{1}{\sqrt{x^2+y^2}}&\text{si }(x,y)\ne(0,0)\\[2mm]0&\text{si }(x,y)=(0,0)\end{cases}$$
- *Continue* : $|f(x,y)|\le x^2+y^2\to0$.
- *Différentiable en $(0,0)$* : $\partial_xf(0,0)=\lim_{t\to0}t\sin\frac1{|t|}=0=\partial_yf(0,0)$, puis $\dfrac{f(h)-0}{\|h\|_2}=\|h\|_2\sin\dfrac1{\|h\|_2}\to0$.
- *Pas $C^1$* : pour $(x,y)\ne(0,0)$,
 $$\frac{\partial f}{\partial x}(x,y)=2x\sin\frac1{\sqrt{x^2+y^2}}-\frac{x}{\sqrt{x^2+y^2}}\cos\frac1{\sqrt{x^2+y^2}}.$$
 Avec $u_n=(\tfrac1n,0)\to(0,0)$ : $\dfrac{\partial f}{\partial x}(u_n)=\dfrac{2\sin n}{n}-\cos n$, qui n'a pas de limite (à cause de $\cos n$) et en particulier ne tend pas vers $\partial_xf(0,0)=0$. La dérivée partielle n'est donc pas continue en $0$ : $f$ n'est pas $C^1$.

**Théorème 4.** $C^1(U,F)$ est un sous-espace vectoriel de $C(U,F)$.
**Théorème 5.** Si $f,g\in C^1(U,F)$ alors $f\times g\in C^1(U,F)$ (produit, exercice).
**Théorème 6 (composition).** Si $f\in C^1(U,\mathbb{R}^q)$, $g\in C^1(V,\mathbb{R}^n)$ avec $V$ ouvert de $\mathbb{R}^q$ et $f(U)\subset V$, alors $g\circ f\in C^1(U,\mathbb{R}^n)$ (admis).

### 4.3.3 Paramétrisation d'un chemin et dérivée le long d'un chemin

*Motivation.* Un avion suit une trajectoire $(x(t),y(t),z(t))$ ; la température extérieure est $\theta(x,y,z)$. Ce qui compte n'est pas $\partial_x\theta,\partial_y\theta,\partial_z\theta$ mais $\dfrac{d}{dt}\theta(x(t),y(t),z(t))$. On peut calculer $T(t)=\theta(x(t),y(t),z(t))$ puis dériver, ou utiliser la propriété suivante.

**Propriété 6 (dérivée le long d'un chemin / règle de la chaîne).** Soit $U$ ouvert de $\mathbb{R}^n$, $u_1,\dots,u_n$ des fonctions $C^1$ sur un intervalle $I$ telles que $\gamma(t)=(u_1(t),\dots,u_n(t))\in U$, et $f:U\to\mathbb{R}$ de classe $C^1$. Alors $g=f\circ\gamma$ est $C^1$ sur $I$ et
$$g'(t)=u_1'(t)\frac{\partial f}{\partial x_1}\Big|_{\gamma(t)}+\dots+u_n'(t)\frac{\partial f}{\partial x_n}\Big|_{\gamma(t)}.$$

*Preuve ($n=2$).* $g(t+h)-g(t)=\big[f(u(t+h),v(t+h))-f(u(t+h),v(t))\big]+\big[f(u(t+h),v(t))-f(u(t),v(t))\big]$. On divise par $h$ et on multiplie/divise par $v(t+h)-v(t)$ (resp. $u(t+h)-u(t)$) ; comme $\partial_yf,\partial_xf$ sont continues, on trouve à la limite
$$g'(t)=u'(t)\frac{\partial f}{\partial x}\Big|_{(u(t),v(t))}+v'(t)\frac{\partial f}{\partial y}\Big|_{(u(t),v(t))}.$$

*Intuition (différentielles).* $df=\dfrac{\partial f}{\partial x}du+\dfrac{\partial f}{\partial y}dv$ avec $du=u'(t)dt$, $dv=v'(t)dt$.

*Remarque.* Avec le gradient : $g'=\big[(\vec\nabla f)\circ\gamma\big]\cdot\gamma'$ (produit scalaire).

### 4.3.4 Dérivation d'un changement de variables

**Propriété 7.** Soient $U,V$ ouverts de $\mathbb{R}^2$, $f:U\to\mathbb{R}$ et $g_1,g_2:V\to\mathbb{R}$ de classe $C^1$, avec $(g_1(u,v),g_2(u,v))\in U$ pour tout $(u,v)\in V$. Alors $h(u,v)=f\big(g_1(u,v),g_2(u,v)\big)$ est $C^1$ sur $V$ et
$$\begin{cases}\dfrac{\partial h}{\partial u}=\dfrac{\partial f}{\partial x}\Big|_{(g_1,g_2)}\dfrac{\partial g_1}{\partial u}+\dfrac{\partial f}{\partial y}\Big|_{(g_1,g_2)}\dfrac{\partial g_2}{\partial u}\\[3mm]\dfrac{\partial h}{\partial v}=\dfrac{\partial f}{\partial x}\Big|_{(g_1,g_2)}\dfrac{\partial g_1}{\partial v}+\dfrac{\partial f}{\partial y}\Big|_{(g_1,g_2)}\dfrac{\partial g_2}{\partial v}\end{cases}$$
*Preuve.* À $v$ fixé, appliquer la propriété 6 à $H(u)=f(g_1^v(u),g_2^v(u))$.

Cette propriété sert à exprimer les dérivées de $h$ (variables $u,v$) à partir de celles de $f$ (variables $x,y$) : c'est l'outil pour résoudre les EDP par changement de variables.

**Exemple.** $f(x,y)=2x^2y+y^2+x$, $x=u+v$, $y=u-v$. Alors $\partial_xf=4xy+1$, $\partial_yf=2x^2+2y$ et
$$\frac{\partial h}{\partial u}=(4xy+1)\cdot1+(2x^2+2y)\cdot1,\qquad\frac{\partial h}{\partial v}=(4xy+1)\cdot1+(2x^2+2y)\cdot(-1).$$
En remplaçant $x=u+v$, $y=u-v$ :
$$\frac{\partial h}{\partial u}=6u^2-2v^2+2u-2v+4uv+1,\qquad\frac{\partial h}{\partial v}=2u^2-6v^2+1-2u+2v-4uv,$$
ce que l'on vérifie en calculant directement $h(u,v)=2u^3-2v^3+2u^2v-2uv^2+u^2+v^2-2uv+u+v$ puis ses dérivées.

### 4.3.5 Matrice de Jacobi et gradient

**Définition 4 (matrice jacobienne).** Soit $f:U\subset\mathbb{R}^p\to\mathbb{R}^n$ différentiable en $a$. La **matrice de Jacobi** de $f$ en $a$ est la matrice $n\times p$ de $D_af$ dans les bases canoniques :
$$J_f(a)=\left(\frac{\partial f_i}{\partial x_j}(a)\right)_{\substack{1\le i\le n\\1\le j\le p}}=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}(a)&\cdots&\frac{\partial f_1}{\partial x_p}(a)\\\vdots&&\vdots\\\frac{\partial f_n}{\partial x_1}(a)&\cdots&\frac{\partial f_n}{\partial x_p}(a)\end{pmatrix}.$$
Si $n=p$, le **jacobien** de $f$ en $a$ est $\det J_f(a)$.

**Définition 5 (gradient).** Pour $f:U\to\mathbb{R}$ différentiable en $a$ :
$$\vec\nabla_af=\overrightarrow{\mathrm{grad}}\,f(a)=J_f(a)^{\top}=\begin{pmatrix}\frac{\partial f}{\partial x_1}(a)\\\vdots\\\frac{\partial f}{\partial x_p}(a)\end{pmatrix}.$$

**Propriété 8.** $D_af(h)=\vec\nabla_af\cdot h$ (produit scalaire) pour tout $h$.

**Propriété 9 (interprétation du gradient).** Le gradient d'une fonction $f:\mathbb{R}^n\to\mathbb{R}$ est
- **perpendiculaire** aux directions où $f$ est constante ;
- dirigé selon la direction de **plus grande pente** (variation maximale de $f$) ;
- de norme d'autant plus grande que $f$ varie vite.

*Preuve.* Avec $p(t)=a+tv$ : $\dfrac{d}{dt}f(p(t))\big|_{t=0}=\vec\nabla_af\cdot v$. (1) si $v\perp\vec\nabla_af$, la dérivée est nulle : $f$ constante. (2) pour $v=\vec\nabla_af$, la dérivée vaut $\|\vec\nabla_af\|^2>0$. (3) pour $\|v\|=1$, $\vec\nabla_af\cdot v$ est maximal ssi $v$ est colinéaire à $\vec\nabla_af$ et de même sens.

## 4.4 EDP du 1er ordre et $C^1$-difféomorphisme

### 4.4.1 Généralités

Une **équation différentielle** relie une fonction d'**une** variable à ses dérivées ; une **équation aux dérivées partielles (EDP)** relie une fonction de **plusieurs** variables à ses dérivées partielles. On considère les EDP du 1er ordre de la forme
$$F\!\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},f,x,y\right)=0,\qquad f:\mathbb{R}^2\to\mathbb{R}.$$

**Théorème 7 (EDP la plus simple).** Soit $g$ continue sur un ouvert $U\subset\mathbb{R}^2$. Les solutions $C^1$ sur $U$ de
$$\frac{\partial f}{\partial x}(x,y)=g(x,y)\tag{4.4}$$
sont
$$f(x,y)=K(y)+\int g(x,y)\,dx,$$
où $\int g\,dx$ est une primitive de $g$ par rapport à $x$ et $K$ est une fonction $C^1$ quelconque de $y$ (sur la projection de $U$ sur l'axe $Oy$).

Pour résoudre des EDP plus générales, on fait un **changement de variables** pour se ramener à (4.4).

### 4.4.2 $C^1$-difféomorphisme et changement de variables

**Définition 6.** Soit $U$ ouvert de $\mathbb{R}^p$, $V$ ouvert de $\mathbb{R}^n$. $\varphi:U\to V$ est un **$C^1$-difféomorphisme** si
1. $\varphi$ est de classe $C^1$ sur $U$ ;
2. $\varphi$ est une **bijection** de $U$ sur $V$ ;
3. $\varphi^{-1}$ est de classe $C^1$ sur $V$.

*Pourquoi ?* Avec $h=f\circ\varphi$ : (1) $\varphi\in C^1\Rightarrow h\in C^1$ ; (2) la bijection permet de passer des nouvelles variables aux anciennes et inversement ; (3) $\varphi^{-1}\in C^1\Rightarrow f=h\circ\varphi^{-1}\in C^1$.

**Propriété 10.** Une application **linéaire bijective** $\varphi:\mathbb{R}^p\to\mathbb{R}^n$ impose $p=n$ et est un $C^1$-difféomorphisme.

**Propriété 11 (caractérisation rapide).** Si $\varphi:U\to V$ est (1) $C^1$ sur $U$, (2) une bijection de $U$ sur $V$, (3) telle que $D_a\varphi$ est linéaire **bijective** pour tout $a\in U$, alors $p=n$ et $\varphi$ est un $C^1$-difféomorphisme de $U$ sur $V$ (admis).

**Propriété 12.** Si le jacobien de $\varphi$ en $a$ est non nul ($\det J_\varphi(a)\ne0$), alors $D_a\varphi$ est bijective.
*Preuve.* Règle de composition : $J_{\psi\circ\varphi}(a)=J_\psi(\varphi(a))\,J_\varphi(a)$. Avec $\psi=\varphi^{-1}$ : $I=J_{\varphi^{-1}}(\varphi(a))J_\varphi(a)$, donc $J_\varphi(a)$ est inversible.

**Exemple (coordonnées sphériques).** $U=\mathbb{R}_+^*\times]0,2\pi[\times]0,\pi[$, $V=\mathbb{R}^3\setminus(\mathbb{R}_+\times\{0\}\times\mathbb{R})$ et
$$f(\rho,\theta,\varphi)=(\rho\cos\theta\sin\varphi,\ \rho\sin\theta\sin\varphi,\ \rho\cos\varphi).$$
$f$ est $C^1$ (composantes $C^1$), bijective de $U$ sur $V$, et
$$J_f=\begin{pmatrix}\cos\theta\sin\varphi&-\rho\sin\theta\sin\varphi&\rho\cos\theta\cos\varphi\\\sin\theta\sin\varphi&\rho\cos\theta\sin\varphi&\rho\sin\theta\cos\varphi\\\cos\varphi&0&-\rho\sin\varphi\end{pmatrix},\qquad\det J_f=-\rho^2\sin\varphi\ne0.$$
Donc $f$ est un $C^1$-difféomorphisme.

### 4.4.3 Résolution des EDP par changement de variables

On cherche $f:\mathbb{R}^2\to\mathbb{R}$ solution d'une EDP $(E)$ du 1er ordre. On utilise un $C^1$-difféomorphisme $\varphi:U\to V$ (changement de variables). Deux présentations, mais la distinction n'est pas indispensable :

| | **Direct** | **Indirect** |
|---|---|---|
| Changement | $(x,y)=\varphi(u,v)$, avec $\varphi:V\to U$, $(u,v)\mapsto(x(u,v),y(u,v))$ | $(u,v)=\varphi(x,y)$, avec $\varphi:U\to V$, $(x,y)\mapsto(u(x,y),v(x,y))$ |
| Nouvelle fonction | $g=f\circ\varphi$ avec $f\in C^1(U,\mathbb{R})$, donc $g\in C^1(V,\mathbb{R})$ | $g$ définie par $f=g\circ\varphi$, i.e. $g=f\circ\varphi^{-1}$, donc $g\in C^1(V,\mathbb{R})$ |
| Dérivées | $\dfrac{\partial g}{\partial u}=\dfrac{\partial f}{\partial x}\dfrac{\partial x}{\partial u}+\dfrac{\partial f}{\partial y}\dfrac{\partial y}{\partial u}$ et $\dfrac{\partial g}{\partial v}=\dfrac{\partial f}{\partial x}\dfrac{\partial x}{\partial v}+\dfrac{\partial f}{\partial y}\dfrac{\partial y}{\partial v}$. On exprime $(E)$ avec $\partial_ug,\partial_vg$ en reportant $\partial_xf,\partial_yf$ en fonction de $\partial_ug,\partial_vg$. Si le changement est simple à inverser, il vaut mieux passer au cas « indirect ». | $\dfrac{\partial f}{\partial x}=\dfrac{\partial g}{\partial u}\dfrac{\partial u}{\partial x}+\dfrac{\partial g}{\partial v}\dfrac{\partial v}{\partial x}$ et $\dfrac{\partial f}{\partial y}=\dfrac{\partial g}{\partial u}\dfrac{\partial u}{\partial y}+\dfrac{\partial g}{\partial v}\dfrac{\partial v}{\partial y}$. On injecte directement $\partial_xf,\partial_yf$ dans $(E)$ en fonction de $\partial_ug,\partial_vg$. |
| Résolution | On résout $(E')\ :\ F\!\left(\dfrac{\partial g}{\partial u},\dfrac{\partial g}{\partial v},g,u,v\right)=0$ | idem |
| Retour | Revenir aux variables initiales $x,y$ avec $(u,v)=\varphi^{-1}(x,y)$ | Revenir à $x,y$ avec $(u,v)=\varphi(x,y)$ |

*(Les changements en coordonnées polaires sont traités en annexe.)*

**Exemple.** Résoudre sur $\mathbb{R}^2$
$$2\frac{\partial f}{\partial x}-\frac{\partial f}{\partial y}=x^2y\tag{4.5}$$
avec $(u,v)=(x,\ x+2y)$.

1. $\varphi(x,y)=(x,x+2y)$ est linéaire ; elle est bijective ($x=u$, $y=(v-u)/2$), donc c'est un $C^1$-difféomorphisme de $\mathbb{R}^2$ sur $\mathbb{R}^2$, avec $\varphi^{-1}(u,v)=(u,\tfrac{v-u}{2})$.
2. Changement **indirect** : $f=g\circ\varphi$, $g\in C^1(\mathbb{R}^2)$.
3. Dérivées : $\dfrac{\partial f}{\partial x}=\dfrac{\partial g}{\partial u}+\dfrac{\partial g}{\partial v}$ et $\dfrac{\partial f}{\partial y}=2\dfrac{\partial g}{\partial v}$.
4. Injection dans (4.5) : $2\dfrac{\partial g}{\partial u}=x^2y=u^2\cdot\dfrac{v-u}{2}$, soit
 $$\frac{\partial g}{\partial u}(u,v)=\frac14\,(u^2v-u^3).$$
5. Théorème 7 : $g(u,v)=\dfrac{u^3v}{12}-\dfrac{u^4}{16}+K(v)$, avec $K$ de classe $C^1$ quelconque.
6. Retour : 
$$f(x,y)=\frac{x^3(x+2y)}{12}-\frac{x^4}{16}+K(x+2y).$$

---

# Chapitre 5 — Calcul différentiel d'ordre supérieur

## 5.1 Objectifs

Résoudre des EDP faisant intervenir des dérivées partielles d'ordre $\ge2$, puis étudier les **extremums** de fonctions $\mathbb{R}^2\to\mathbb{R}$.

## 5.2 Différentiation d'ordre supérieur ou égal à 2

**Définition 1 (dérivées partielles d'ordre $k$).** Soit $U$ ouvert de $\mathbb{R}^p$, $f:U\to\mathbb{R}^n$, $a\in U$, $k\in\mathbb{N}^*$, $(i_1,\dots,i_k)\in\llbracket1,p\rrbracket^k$. $f$ admet une dérivée partielle $k$-ième en $a$ par rapport aux variables $i_1,\dots,i_k$ si
- $f$ admet une dérivée $(k-1)$-ième par rapport à $i_1,\dots,i_{k-1}$ sur un voisinage de $a$ ;
- cette dérivée admet elle-même une dérivée partielle première en $a$ par rapport à $x_{i_k}$.

On la note $\dfrac{\partial^kf}{\partial x_{i_k}\cdots\partial x_{i_2}\partial x_{i_1}}(a)$ (ex. $\dfrac{\partial^2f}{\partial x^2}$, $\dfrac{\partial^2f}{\partial x\partial y}$, $\dfrac{\partial^3f}{\partial x\partial y\partial z}$).

**Exemple.** $f(x,y,z)=xy^2z^3$ : $\dfrac{\partial^3f}{\partial x\partial y\partial z}=\dfrac{\partial^2}{\partial x\partial y}(3xy^2z^2)=\dfrac{\partial}{\partial x}(6xyz^2)=6yz^2$. Ici l'ordre de dérivation n'influe pas (voir Schwarz).

**Définition 2 (classe $C^k$, $C^\infty$).** $f$ est de classe $C^k$ sur $U$ si toutes ses dérivées partielles d'ordre $k$ existent et sont continues sur $U$ ; de classe $C^\infty$ si elle est $C^k$ pour tout $k$.

**Propriété 1.** Si $f$ est $C^k$ alors toutes ses dérivées partielles d'ordre $\le k$ existent et sont continues (admis).

La structure algébrique de $C^k(U,F)$ est la même que celle de $C^1$ (espace vectoriel, produit, composition).

**Théorème 1 (composition).** Si $f\in C^k(U,\mathbb{R}^q)$, $g\in C^k(V,\mathbb{R}^n)$ et $f(U)\subset V$, alors $g\circ f\in C^k(U,\mathbb{R}^n)$ (admis).

**Théorème 2.** $f$ est $C^k$ ssi ses fonctions coordonnées sont $C^k$.

**Théorème 3 (Schwarz).** Soit $U$ ouvert de $\mathbb{R}^p$, $f$ de classe $C^1$ de $U$ dans $\mathbb{R}^q$, $a\in U$, $(i,j)\in\llbracket1,p\rrbracket^2$. Si $\dfrac{\partial^2f}{\partial x_j\partial x_i}$ et $\dfrac{\partial^2f}{\partial x_i\partial x_j}$ sont définies **et continues** en $a$, alors
$$\frac{\partial^2f}{\partial x_j\partial x_i}(a)=\frac{\partial^2f}{\partial x_i\partial x_j}(a).$$
(Admis.) En particulier, pour une fonction $C^2$ l'ordre de dérivation n'a pas d'importance.

**Contre-exemple (sans continuité des dérivées secondes).**
$$f(x,y)=\begin{cases}\dfrac{xy(x^2-y^2)}{x^2+y^2}&(x,y)\ne(0,0)\\0&(x,y)=(0,0)\end{cases}$$
Dérivées premières : $\partial_xf(0,0)=\partial_yf(0,0)=0$ et, hors de l'origine,
$$\frac{\partial f}{\partial x}=\frac{y(x^4+4x^2y^2-y^4)}{(x^2+y^2)^2},\qquad\frac{\partial f}{\partial y}=\frac{x(x^4-4x^2y^2-y^4)}{(x^2+y^2)^2},$$
continues (polaires). Mais
$$\frac{\partial}{\partial x}\!\left(\frac{\partial f}{\partial y}\right)(0,0)=\lim_{t\to0}\frac{1}{t}\frac{\partial f}{\partial y}(t,0)=1\ne-1=\lim_{t\to0}\frac1t\frac{\partial f}{\partial x}(0,t)=\frac{\partial}{\partial y}\!\left(\frac{\partial f}{\partial x}\right)(0,0).$$
Les dérivées secondes croisées ne sont donc pas continues en $(0,0)$.

## 5.3 EDP d'ordre 2

Même démarche que pour l'ordre 1 : changement de variables pour se ramener à une EDP dont on connaît la solution.

**Théorème 4.** Les solutions $C^2$ sur un ouvert $U\subset\mathbb{R}^2$ de $\dfrac{\partial^2f}{\partial x^2}=0$ sont
$$f(x,y)=x\,G(y)+H(y),$$
$G,H$ de classe $C^2$ sur la projection de $U$ sur l'axe $Oy$ (on intègre deux fois en $x$).

**Théorème 5.** Les solutions $C^2$ sur $U$ de $\dfrac{\partial^2f}{\partial x\partial y}=0$ sont
$$f(x,y)=G(x)+H(y),$$
$G,H$ de classe $C^2$ sur les projections de $U$ sur $Ox$ et $Oy$.

**Définition 3 ($C^2$-difféomorphisme).** $\varphi:U\to V$ est un $C^2$-difféomorphisme si $\varphi\in C^2(U)$, $\varphi$ est bijective de $U$ sur $V$ et $\varphi^{-1}\in C^2(V)$. (Un changement de variables n'est licite que si c'est un $C^2$-difféomorphisme.)

**Exemple : équation des ondes.** Trouver les $f\in C^2(\mathbb{R}^2)$ telles que
$$\forall(x,t)\in\mathbb{R}^2,\quad\frac{\partial^2f}{\partial x^2}-\frac1{c^2}\frac{\partial^2f}{\partial t^2}=0$$
avec $(X,Y)=(x+ct,\ x-ct)$.

1. $\varphi(x,t)=(x+ct,x-ct)$ est linéaire bijective ($\ker\varphi=\{0\}$), donc un $C^2$-difféomorphisme de $\mathbb{R}^2$.
2. $f=g\circ\varphi$, $f(x,t)=g(x+ct,x-ct)=g(X,Y)$, $g\in C^2$.
3. Dérivées premières : $\dfrac{\partial f}{\partial x}=\dfrac{\partial g}{\partial X}+\dfrac{\partial g}{\partial Y}$, $\dfrac{\partial f}{\partial t}=c\dfrac{\partial g}{\partial X}-c\dfrac{\partial g}{\partial Y}$.
4. Dérivées secondes :
$$\frac{\partial^2f}{\partial x^2}=\frac{\partial^2g}{\partial X^2}+\frac{\partial^2g}{\partial Y^2}+2\frac{\partial^2g}{\partial X\partial Y},\qquad\frac{\partial^2f}{\partial t^2}=c^2\frac{\partial^2g}{\partial X^2}+c^2\frac{\partial^2g}{\partial Y^2}-2c^2\frac{\partial^2g}{\partial X\partial Y}.$$
5. Dans l'EDP : $\dfrac{\partial^2g}{\partial X\partial Y}\times4=0$, soit $\dfrac{\partial^2g}{\partial X\partial Y}=0$, donc (théorème 5) $g(X,Y)=k(X)+h(Y)$.
6. Retour : $$f(x,t)=k(x+ct)+h(x-ct)\quad(h,k\ \text{quelconques }C^2).$$

> *Remarque.* Le polycopié écrit à cette étape « $\dfrac{\partial^2g}{\partial X^2}=0$ » mais la combinaison obtenue en injectant les dérivées secondes est bien $\dfrac{\partial^2g}{\partial X\partial Y}=0$ (les termes en $\partial_X^2g$ et $\partial_Y^2g$ s'annulent), ce qui donne la solution $k(X)+h(Y)$ indiquée.

## 5.4 Extremums de fonctions à valeurs dans $\mathbb{R}$

Motivations : économie (maximiser profits, minimiser coûts), physique (principes variationnels : loi de Snell-Descartes par minimisation du temps de parcours de la lumière), deep learning (minimisation d'une fonction de coût).

### 5.4.1 Définitions

**Définition 4 (extremums locaux).** Soit $A\subset\mathbb{R}^n$ quelconque, $a\in\mathring{A}$ et $f:A\to\mathbb{R}$.
1. **minimum local** en $a$ : $\exists V\subset A$ voisinage de $a$, $\forall x\in V,\ f(x)\ge f(a)$ ;
2. **minimum local strict** : $\forall x\in V\setminus\{a\},\ f(x)>f(a)$ ;
3. **maximum local** : $\forall x\in V,\ f(x)\le f(a)$ ;
4. **maximum local strict** : $\forall x\in V\setminus\{a\},\ f(x)<f(a)$.

Les maximums et minimums sont appelés **extremums**. Un extremum **local** ne se cherche qu'en un point **intérieur** (il faut pouvoir évaluer $f$ tout autour de $a$).

**Définition 5 (extremums globaux).** Soit $a\in A$, $f:A\to\mathbb{R}$.
1. **minimum global** en $a$ : $\forall x\in A,\ f(x)\ge f(a)$ ;
2. **maximum global** en $a$ : $\forall x\in A,\ f(x)\le f(a)$.

Plus de notion de voisinage : un extremum global peut être **sur la frontière**.

*Remarques.*
1. Un extremum global $a$ est soit dans $\mathring{A}$ (alors c'est aussi un extremum local), soit sur la frontière (alors ce n'est pas un extremum local).
2. Sur un **ouvert**, on cherche les extremums locaux ; les globaux, s'ils existent, sont les minimums locaux les plus profonds / maximums locaux les plus hauts. Sur un **fermé**, il faut en plus évaluer $f$ sur la frontière.
3. Si $f$ n'est pas majorée, pas de maximum global ; si elle n'est pas minorée, pas de minimum global.

### 5.4.2 Cas des fonctions de $\mathbb{R}$ dans $\mathbb{R}$ (rappel)

Pour $f\in C^2$ et $a\in\mathring{A}$ : $f'(a)=0$ est une condition **nécessaire** (tangente horizontale) mais non suffisante ; c'est le signe de $f''$ qui donne la nature de $a$ (minimum, maximum, ou méplat si $f''$ change de signe en $a$).

### 5.4.3 Cas général : $\mathbb{R}^n\to\mathbb{R}$

**Définition 6 (point critique).** $a\in U$ est un **point critique** de $f:U\to\mathbb{R}$ si toutes les dérivées partielles premières de $f$ en $a$ existent et sont nulles, i.e. $\vec\nabla_af=0_{\mathbb{R}^p}$.

**Propriété 2 (condition nécessaire).** Si $f$ admet un extremum local en $a\in U$ (ouvert) et que toutes ses dérivées partielles existent en $a$, alors $a$ est un point critique.
*Preuve (minimum local).* Pour $|h|<r$, $f(a+he_i)-f(a)\ge0$, donc $\lim_{h\to0^+}\frac{f(a+he_i)-f(a)}{h}\ge0$ et $\lim_{h\to0^-}\ldots\le0$ : la dérivée partielle vaut $0$ pour tout $i$.

**Propriété 3 (développement limité d'ordre 2).** Si $f\in C^2(U,\mathbb{R})$, $a\in U$, il existe $\varepsilon:U_0\to\mathbb{R}$ avec $\lim_{h\to0}\varepsilon(h)=0$ et
$$f(a+h)=f(a)+\sum_{j=1}^p h_j\frac{\partial f}{\partial x_j}(a)+\frac12\sum_{i=1}^p\sum_{j=1}^p h_ih_j\frac{\partial^2f}{\partial x_i\partial x_j}(a)+\|h\|^2\varepsilon(h).$$
(Admis.)

**Théorème 6 (condition suffisante d'ordre 2).** Soit $f\in C^2(U,\mathbb{R})$ et $a$ un point critique. On pose
$$Q(h)=\sum_{i=1}^p\sum_{j=1}^p h_ih_j\frac{\partial^2f}{\partial x_i\partial x_j}(a).$$
- Si $Q>0$ (et ne s'annule qu'en $h=0$) : **minimum local strict** en $a$.
- Si $Q<0$ (et ne s'annule qu'en $h=0$) : **maximum local strict** en $a$.
- Si $Q$ prend des valeurs positives **et** négatives dans tout voisinage de $0$ : **pas d'extremum local** en $a$.

*Idée.* Comme $\vec\nabla_af=0$, $f(a+h)-f(a)\approx\tfrac12Q(h)$.

**Définition 7 (matrice hessienne).** Pour $f\in C^2$ et $a$ point critique :
$$H_f(a)=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}(a)&\cdots&\dfrac{\partial^2f}{\partial x_1\partial x_p}(a)\\\vdots&&\vdots\\\dfrac{\partial^2f}{\partial x_p\partial x_1}(a)&\cdots&\dfrac{\partial^2f}{\partial x_p^2}(a)\end{pmatrix}.$$

**Définition 8 (notations de Monge, cas $\mathbb{R}^2\to\mathbb{R}$).**
$$r=\frac{\partial^2f}{\partial x^2}(a),\qquad s=\frac{\partial^2f}{\partial x\partial y}(a)=\frac{\partial^2f}{\partial y\partial x}(a),\qquad t=\frac{\partial^2f}{\partial y^2}(a),\qquad H_f(a)=\begin{pmatrix}r&s\\s&t\end{pmatrix}.$$

**Théorème 7 (condition suffisante d'ordre 2 sur $\mathbb{R}^2$).** Soit $f\in C^2(U,\mathbb{R})$, $U$ ouvert de $\mathbb{R}^2$, et $a$ un point critique.
1. Si $\det H_f(a)=rt-s^2>0$ :
 - (a) si $r>0$ : **minimum local strict** en $a$ ;
 - (b) si $r<0$ : **maximum local strict** en $a$.
2. Si $rt-s^2<0$ : **pas d'extremum local** ; $a$ est un **point-col** (point-selle).
3. Si $rt-s^2=0$ : on ne peut pas conclure sans étude locale poussée (par exemple un développement limité à l'ordre 3, ou l'étude du signe de $f(a+h)-f(a)$).

**Plan général de recherche d'extremums de $f:U\subset\mathbb{R}^2\to\mathbb{R}$.**
- **Étape 0** : vérifier que $f$ est de classe $C^2$ sur $U$.
- **Étape 1** : trouver les points critiques en résolvant
 $$\begin{cases}\dfrac{\partial f}{\partial x}(x,y)=0\\[2mm]\dfrac{\partial f}{\partial y}(x,y)=0\end{cases}$$
- **Étape 2** : pour chaque point critique, calculer $r,s,t$ puis appliquer le théorème 7 (min local strict, max local strict, point-selle, ou étude locale si $rt-s^2=0$).
- **Étape 3** : extremums **globaux**. Recherche de minima globaux : si $f$ n'est pas minorée, pas de minimum global. Recherche de maxima globaux : si $f$ n'est pas majorée, pas de maximum global. Sinon, comparer les valeurs aux candidats (et sur la frontière si l'ensemble est fermé).

---

# Annexe A — Changement de variable en coordonnées polaires dans les EDP

Les coordonnées polaires $\varphi:\mathbb{R}_+^*\times\mathbb{R}\to\mathbb{R}^2\setminus\{(0,0)\}$, $(\rho,\theta)\mapsto(\rho\cos\theta,\rho\sin\theta)$ ne sont **pas** un difféomorphisme global (non injective). Pour les EDP, il faut des restrictions qui sont des $C^1$-difféomorphismes.

### A) Demi-plan $x>0$

$$\varphi:\mathbb{R}_+^*\times\left]-\tfrac\pi2,\tfrac\pi2\right[\to\mathbb{R}_+^*\times\mathbb{R},\quad(\rho,\theta)\mapsto(\rho\cos\theta,\rho\sin\theta)$$
$$\varphi^{-1}:\mathbb{R}_+^*\times\mathbb{R}\to\mathbb{R}_+^*\times\left]-\tfrac\pi2,\tfrac\pi2\right[,\quad(x,y)\mapsto\left(\sqrt{x^2+y^2},\ \operatorname{Arctan}\tfrac yx\right).$$

Vérification (caractérisation rapide) :
- $\varphi$ est $C^1$ (composantes $\rho\cos\theta$, $\rho\sin\theta$).
- **Bijection** : $\varphi^{-1}\circ\varphi=\mathrm{id}$ car $\sqrt{\rho^2}=\rho$ ($\rho>0$) et $\operatorname{Arctan}(\tan\theta)=\theta$ sur $]-\tfrac\pi2,\tfrac\pi2[$ ; $\varphi\circ\varphi^{-1}=\mathrm{id}$ car, pour $x>0$, $\cos\operatorname{Arctan}\tfrac yx=\dfrac{x}{\sqrt{x^2+y^2}}$ et $\sin\operatorname{Arctan}\tfrac yx=\dfrac{y}{\sqrt{x^2+y^2}}$.
- **Jacobien** : $J_\varphi=\begin{pmatrix}\cos\theta&-\rho\sin\theta\\\sin\theta&\rho\cos\theta\end{pmatrix}$, $\ |J_\varphi|=\rho\cos^2\theta+\rho\sin^2\theta=\rho>0$.

Donc $\varphi$ est un $C^1$-difféomorphisme du demi-plan $x>0$.

### B) Demi-plan $x<0$ (sans démonstration)
$$\varphi:\mathbb{R}_+^*\times\left]\tfrac\pi2,\tfrac{3\pi}2\right[\to\mathbb{R}_-^*\times\mathbb{R},\ (\rho,\theta)\mapsto(\rho\cos\theta,\rho\sin\theta),\qquad\varphi^{-1}(x,y)=\left(\sqrt{x^2+y^2},\ \pi+\operatorname{Arctan}\tfrac yx\right).$$

### C) Demi-plan $y>0$ (sans démonstration)
$$\varphi:\mathbb{R}_+^*\times]0,\pi[\to\mathbb{R}\times\mathbb{R}_+^*,\ (\rho,\theta)\mapsto(\rho\cos\theta,\rho\sin\theta),\qquad\varphi^{-1}(x,y)=\left(\sqrt{x^2+y^2},\ \operatorname{Arccos}\tfrac{x}{\sqrt{x^2+y^2}}\right).$$

### Complément (formules usuelles, hors polycopié)

Pour $f(x,y)=g(\rho,\theta)$ avec $x=\rho\cos\theta$, $y=\rho\sin\theta$ (propriété 7) :
$$\frac{\partial f}{\partial x}=\cos\theta\,\frac{\partial g}{\partial\rho}-\frac{\sin\theta}{\rho}\frac{\partial g}{\partial\theta},\qquad\frac{\partial f}{\partial y}=\sin\theta\,\frac{\partial g}{\partial\rho}+\frac{\cos\theta}{\rho}\frac{\partial g}{\partial\theta}.$$
