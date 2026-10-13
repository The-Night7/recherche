---
source: "PREING2-S1/Analyse-dans-RN/CM-Annotee_2022-2023_Analyse-dans-RN_P2S1_MX.pdf"
pages: 18
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 18 pages manuscrites ; OCR natif non fiable remplacé, lacunes et corrections signalées
---

# Analyse dans Rn — CM annoté : limites, continuité, compacité (2022–2023)

## Page 1

### Analyse dans Rn

**CM — 2022–2023.** Page de couverture manuscrite, titre blanc sur fond gris foncé. Aucun autre contenu de cours sur cette page.

## Page 2

### 1. Limite et continuité

**Définition : limite d’une fonction en un point.** Soient $(E,\|\cdot\|_E)$, $(F,\|\cdot\|_F)$ deux espaces vectoriels normés, $A\subset E$, $f:A\to F$, $x\in\overline A$ et $\ell\in F$. On dit que $f(y)$ tend vers $\ell$ quand $y\to x$ si l’une des formulations équivalentes suivantes est satisfaite :

1. $\forall\varepsilon>0,\ \exists\delta>0,\ \forall y\in A,\ \|y-x\|_E<\delta\Rightarrow\|f(y)-\ell\|_F<\varepsilon$.
2. $\forall\varepsilon>0,\ \exists\delta>0,\ f(A\cap B_E(x,\delta))\subset B_F(\ell,\varepsilon)$.
3. La page amorce une formulation avec des boules $V_F$ autour de $\ell$ et $V_E$ autour de $x$, mais laisse la condition finale vide.
4. Pour tout voisinage $V_F$ de $\ell$, il existe un voisinage $V_E$ de $x$ tel que $f(V_E\cap A)\subset V_F$.

**Précisions :** la formulation 2 omet $A$ dans le manuscrit ; il faut y restreindre les arguments pour lesquels $f$ est définie. La définition utilisée inclut $y=x$ lorsque $x\in A$ ; pour une limite épointée, on remplacerait $A$ par $A\setminus\{x\}$.

## Page 3

On note $\lim_{y\to x}f(y)=\ell$ ou $f(y)\to\ell$ quand $y\to x$.

**Proposition — unicité.** Si $f:A\to F$ admet une limite en $a\in\overline A$, cette limite est unique.

**Remarque dans $\mathbb R$.** Pour étudier une limite bilatérale en $a$, on examine les limites à droite et à gauche. Lorsqu’elles existent et sont égales à $\ell$, la limite bilatérale est $\ell$.

La page introduit ensuite les **limites le long d’un chemin**.

## Page 4

**Proposition — chemins.** Soit $f$ définie au voisinage d’un point $x_0\in\mathbb R^n$, éventuellement sauf en ce point. Si $f$ admet une limite $\ell$ en $x_0$, alors sa restriction à chaque courbe approchant $x_0$ dans le domaine admet la même limite. Par contraposition, deux chemins donnant des limites différentes suffisent à exclure l’existence de la limite.

**Précision sur le « si et seulement si » manuscrit :** une caractérisation réciproque doit quantifier sur toutes les courbes admissibles, et pas seulement sur quelques directions ou droites.

**Exemple.** $f(x,y)=xy/(x^2+y^2)$ hors de l’origine. Sur les axes, $f(t,0)=f(0,t)=0$. Sur les diagonales,
$$f(t,t)=\frac12,\qquad f(t,-t)=-\frac12\quad(t\ne0).$$
Donc $f$ n’admet pas de limite en $(0,0)$. La ligne concernant l’axe vertical écrit $f(t,0)$ au lieu de $f(0,t)$ ; les valeurs nulles restent correctes.

## Page 5

**Proposition — opérations sur les limites.** Si $f,g:A\to F$ tendent respectivement vers $\ell_1,\ell_2$ en $a\in\overline A$, alors, pour $\lambda\in\mathbb R$,
$$\lim_{x\to a}(f+\lambda g)(x)=\ell_1+\lambda\ell_2.$$
La convergence vers $\ell$ équivaut à $\|f(x)-\ell\|_F\to0$.

Pour des fonctions réelles, $fg\to\ell_1\ell_2$ ; si $\ell_2\ne0$, $f/g\to\ell_1/\ell_2$ sur le domaine où le quotient est défini.

**Limite d’une application à plusieurs composantes.** Pour $f:E\to\mathbb R^p$, on écrit $f(x)=(f_1(x),\ldots,f_p(x))$. Le résultat correspondant se poursuit page suivante.

## Page 6

**Limite composante par composante.** L’application $f$ tend vers $\ell=(\ell_1,\ldots,\ell_p)$ si et seulement si chacune des composantes $f_i$ tend vers $\ell_i$.

**Exemple.**
$$f(x,y)=\left(\frac{xy^2}{x^2+y^2},\ x^2+y^2x\right).$$
Quand $(x,y)\to(1,0)$, la première composante tend vers zéro et la seconde vers $1$. Donc $f(x,y)\to(0,1)$.

**Coordonnées polaires.** Le schéma situe un point $M(x,y)$ dans un repère orthonormé : $r=OM$ et $\theta$ est l’angle entre l’axe horizontal positif et $OM$ ; les projections sont $x,y$.

## Page 7

**Coordonnées polaires, suite.**
$$x=r\cos\theta,\qquad y=r\sin\theta,\qquad r=\sqrt{x^2+y^2}.$$
La page prend $r\ge0$ et $\theta$ sur un tour complet. Dans le premier quadrant, pour $x>0$, $\theta=\arctan(y/x)$. Cette expression ne choisit pas à elle seule le bon quadrant sur tout le plan ; à l’origine, l’angle n’est pas unique.

**Critère de limite en polaires.** Le manuscrit indique qu’une limite de $f(r\cos\theta,r\sin\theta)$ « indépendante de $\theta$ » donnerait la limite en $(0,0)$.

**Hypothèse à préciser :** il faut une convergence **uniforme en l’angle**, ou une majoration indépendante de l’angle tendant vers zéro. Une même limite pour chaque angle fixé ne suffit pas en général.

**Exemple.** Pour $f(x,y)=x^2y^3/(x^2+y^2)^2$,
$$f(r\cos\theta,r\sin\theta)=\frac{r^5\cos^2\theta\sin^3\theta}{r^4}.$$
Le calcul se poursuit page suivante.

## Page 8

**Premier exemple polaire.**
$$f(r\cos\theta,r\sin\theta)=r\cos^2\theta\sin^3\theta.$$
Sa valeur absolue est au plus $r$, donc la limite en $(0,0)$ est zéro. Les lignes réservées à la limite sont laissées incomplètes sur la page ; cette conclusion découle directement de la formule transcrite.

**Deuxième exemple.** Pour $f(x,y)=xy/(x^2+y^2)$,
$$f(r\cos\theta,r\sin\theta)=\sin\theta\cos\theta=\tfrac12\sin(2\theta).$$
La limite radiale dépend de $\theta$, donc la fonction n’a pas de limite en $(0,0)$.

## Page 9

**Exemple près de $(1,1)$.**
$$f(x,y)=\frac{(x-1)(y-1)^2}{(x-1)^2+(y-1)^2}.$$
On pose $x-1=r\cos\theta$, $y-1=r\sin\theta$. Alors
$$f(1+r\cos\theta,1+r\sin\theta)=r\cos\theta\sin^2\theta\to0,$$
avec une valeur absolue majorée par $r$. Donc $f(x,y)\to0$ quand $(x,y)\to(1,1)$.

**Caractérisation séquentielle de la limite.** Soient $E,F$ normés, $A\subset E$, $a\in\overline A$, $f:A\to F$. La fonction tend vers $\ell$ en $a$ si et seulement si, pour toute suite $(x_n)$ d’éléments de $A$ convergeant vers $a$, la suite $(f(x_n))$ converge vers $\ell$.

## Page 10

**Contraposée de la caractérisation séquentielle.** S’il existe deux suites $(x_n),(y_n)$ de points de $A$ tendant vers $a$, mais telles que $f(x_n)\to\ell_1$, $f(y_n)\to\ell_2$ avec $\ell_1\ne\ell_2$, alors $f$ n’admet pas de limite en $a$.

**Exemple.** $f(x,y)=1+x^3/(x^2+y^2)$ hors de zéro. En polaires,
$$f(r\cos\theta,r\sin\theta)=1+r\cos^3\theta\to1.$$
La borne $|f-1|\le r$ rend la conclusion uniforme en l’angle.

Pour comparer à l’approche séquentielle, la page choisit $u_n=(1/n,1/n)$ et $v_n=(0,1/n)$, deux suites tendant vers $(0,0)$. Une annotation initiale « $\to0$ » près de la formule ne correspond pas à la limite de $f$, qui vaut $1$ ; c’est le terme ajouté à $1$ qui tend vers zéro.

## Page 11

**Exemple, deux suites.**
$$f(u_n)=1+\frac{(1/n)^3}{2/n^2}=1+\frac1{2n}\to1,\qquad f(v_n)=1.$$
Ces deux vérifications seules ne suffisent pas à établir une limite pour tous les chemins.

**Approche cartésienne.** Une ligne « chemin 1 » est laissée vide. Le chemin 2 est $(x,0)$ : $f(x,0)=1+x\to1$. Là encore, un chemin isolé ne prouve pas l’existence de la limite.

**Par la définition.** La page commence la majoration
$$|f(x,y)-1|=\left|\frac{x^3}{x^2+y^2}\right|=|x|\frac{x^2}{x^2+y^2}.$$
Elle se complète par $|f-1|\le|x|\le\sqrt{x^2+y^2}\to0$, ce qui établit la limite $1$.

## Page 12

### Continuité

**Définition.** Une fonction $f:A\to F$ est continue en $a\in A$ si sa limite quand $x\to a$ est $f(a)$, c’est-à-dire
$$\forall\varepsilon>0,\ \exists\delta>0,\ \forall x\in A,\quad\|x-a\|_E<\delta\implies\|f(x)-f(a)\|_F<\varepsilon.$$
Sinon elle est discontinue en $a$. Elle est continue sur $A$ si elle l’est en chaque point de $A$ ; l’ensemble de ces fonctions est noté $C(A,F)$.

**Formulations équivalentes.**

1. Pour tout $\varepsilon>0$, il existe $\delta>0$ tel que $f(A\cap B(a,\delta))\subset B(f(a),\varepsilon)$. La page explique l’inclusion en prenant un élément image $y=f(x)$ de la boule de départ.
2. Pour tout voisinage $V_F$ de $f(a)$, il existe un voisinage $V_E$ de $a$ tel que $x\in V_E\cap A\Rightarrow f(x)\in V_F$.
3. De façon équivalente, $f(V_E\cap A)\subset V_F$.

Certains centres de voisinages sont écrits $f(a)$ dans l’espace de départ ; ils doivent être $a$.

## Page 13

**4.** La continuité en $a$ s’écrit aussi $\lim_{x\to a}f(x)=f(a)$.

**Continuité des composantes.** Une application $f:E\to\mathbb R^p$, $f=(f_1,\ldots,f_p)$, est continue en un point, ou sur une partie, si et seulement si toutes ses composantes le sont.

**Opérations.** Une combinaison linéaire de fonctions continues est continue. La composition d’applications continues est continue. Pour les fonctions réelles, le produit est continu ; le quotient $f/g$ est continu là où $g$ ne s’annule pas.

**Caractérisation séquentielle.** $f$ est continue en $a\in A$ si et seulement si, pour **toute** suite $(x_n)\subset A$ tendant vers $a$, $f(x_n)\to f(a)$.

**Correction du quantificateur :** le manuscrit emploie un symbole existentiel ; l’existence d’une seule suite ne suffit pas. La propriété exige toutes les suites convergeant vers $a$.

## Page 14

**Prolongement par continuité.** Soit $f:E\to\mathbb R$ avec $E\subset\mathbb R^n$, $x_0\in\overline E\setminus E$. Si $f(x)\to\ell$ quand $x\to x_0$ dans $E$, on peut étendre la définition en posant $\widetilde f(x_0)=\ell$ ; le prolongement est continu au point ajouté.

**Exemple.** Sur $\mathbb R^2\setminus\{(0,0)\}$,
$$f(x,y)=2+\frac{x^2y}{x^2+y^2}.$$
En polaires, le terme ajouté est $r\cos^2\theta\sin\theta$, de valeur absolue au plus $r$ ; la limite est $2$. On prolonge donc $f$ en lui donnant la valeur $2$ à l’origine.

**Théorème — images réciproques des ouverts et fermés.** La page énonce que l’image réciproque d’un ouvert par une application continue est ouverte, puis commence une seconde ligne laissée inachevée. Pour une application continue définie sur tout $E$, l’image réciproque d’un fermé est également fermée ; sur un sous-domaine, ces propriétés s’entendent relativement à celui-ci.

## Page 15

**Preuve pour les ouverts.** Soit $f:E\to F$ continue et $U\subset F$ ouvert. Si $x\in f^{-1}(U)$, il existe $r>0$ tel que $B(f(x),r)\subset U$. Par continuité, il existe $\delta>0$ avec $f(B(x,\delta))\subset B(f(x),r)\subset U$. Donc $B(x,\delta)\subset f^{-1}(U)$ : la préimage est ouverte.

### Compacité

**Définition.** Une partie $A$ d’un espace vectoriel normé est compacte si toute suite de points de $A$ possède une sous-suite convergeant vers un point de $A$.

**Exemples et remarques.** Dans $\mathbb R$, la suite $x_n=n$ n’a aucune sous-suite convergente. Le manuscrit écrit ensuite « tout fermé est compact », mais ajoute aussitôt que $\mathbb R$ est fermé sans être compact : la première affirmation est donc erronée. Les segments $[a,b]$ sont compacts.

**Propriétés.** L’ensemble vide est compact. Toute partie compacte d’un espace vectoriel normé est fermée et bornée. Toute partie fermée d’un compact est compacte.

## Page 16

**Un compact est fermé.** Si $x\in\overline A$, il existe une suite $(x_n)\subset A$ tendant vers $x$. Par compacité, une sous-suite tend vers $y\in A$. Mais elle tend aussi vers $x$ ; l’unicité de la limite impose $x=y\in A$. Donc $\overline A=A$.

**Un compact est borné.** Par contraposition, si $A$ n’est pas borné, choisir $x_n\in A$ avec $\|x_n\|\ge n$. Toute sous-suite a encore une norme tendant vers l’infini ; aucune ne converge. Donc $A$ n’est pas compact.

**Complétude.** La page rappelle qu’un compact d’un espace vectoriel normé est complet, et que tout espace vectoriel normé de dimension finie est complet. Les espaces $\mathbb R^n$ et $\mathbb C^n$ munis d’une norme sont des espaces de Banach. L’espace $C([a,b],\mathbb R)$ est complet pour la norme uniforme $\|f\|_\infty=\sup_{[a,b]}|f|$. Rappel pour $z=x+iy$ : $|z|=\sqrt{x^2+y^2}$.

**Produit cartésien.** Si $A\subset E$ et $B\subset F$ sont compacts, $A\times B$ est compact dans $E\times F$.

La page introduit enfin une application continue $f:E\to F$ pour la propriété suivante.

## Page 17

**Image d’un compact.** Si $A$ est compact et $f$ continue, $f(A)$ est compact. Toute réunion finie de compacts est compacte ; toute intersection d’une famille non vide de compacts est compacte. La précision « famille non vide » évite le cas où l’intersection vide de contraintes est tout l’espace.

**Bolzano–Weierstrass.** Toute suite bornée d’un espace vectoriel normé de dimension finie possède une sous-suite convergente. Pour une suite de $[a,b]$, une sous-suite converge dans $\mathbb R$ et sa limite reste entre $a$ et $b$ ; donc le segment est compact.

**Caractérisation en dimension finie.** Si $\dim E<\infty$, une partie $A\subset E$ est compacte si et seulement si elle est fermée et bornée.

### Continuité uniforme

Une application $f:A\to F$ est uniformément continue si
$$\forall\varepsilon>0,\ \exists\delta>0,\ \forall x,a\in A,\quad\|x-a\|_E<\delta\implies\|f(x)-f(a)\|_F<\varepsilon.$$
Le même $\delta$ convient à tous les points $a\in A$.

Exemples : $x\mapsto1/x$ n’est pas uniformément continue sur $\mathbb R^*$ ; $x\mapsto\sqrt x$ est uniformément continue sur $\mathbb R_+$.

## Page 18

Une ligne « propriété » au début de la page est laissée sans contenu.

**Définition — application lipschitzienne.** Soient $E,F$ normés. Une application $f:E\to F$ est lipschitzienne s’il existe $K\ge0$, indépendant de $x,y$, tel que
$$\forall x,y\in E,\qquad\|f(x)-f(y)\|_F\le K\|x-y\|_E.$$
On dit alors qu’elle est $K$-lipschitzienne.

**Remarque.** Toute application $0$-lipschitzienne est constante : pour tous $x,y$, $0\le\|f(x)-f(y)\|\le0$, donc $f(x)=f(y)$. Le manuscrit utilise $K>0$ dans la définition, puis étend implicitement le vocabulaire au cas $K=0$ dans cette remarque.
