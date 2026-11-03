---
source: "PREING2-S2/Integration-proba-DS/DS3-2020-2021-Correction_Integration-proba-DS_P2S2_DMaths.pdf"
pages: 4
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Correction du DS3 — Intégration et probabilités

CY Tech — Département de mathématiques — PréING2 — 31 mai 2021 — Durée : 1 h 30.

Appareils électroniques et documents interdits. Il est tenu compte de la qualité de la rédaction et de la précision des justifications. Le sujet comporte cinq exercices ; leur ordre de traitement n’est pas imposé.

## Exercice 1 — Ellipse et formule de Green–Riemann

On note $\mathcal E$ l’ellipse d’équation

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,
\qquad (a,b)\in\mathbb R^2,\quad a>0,\ b>0,
$$

et $D$ la partie de $\mathbb R^2$ définie par $x^2/a^2+y^2/b^2-1\leq0$.

1. Calculer $I=\iint_D(x^2+y^2)\,dx\,dy$.
2. Calculer $J=\int_{\mathcal E}(y^3\,dx-x^3\,dy)$.
3. Quelle relation existe entre $I$ et $J$ ? Est-elle conforme à la formule de Green–Riemann ?

**Indication pour la question 2 :**

$$
\cos^4t=\frac18\bigl(\cos4t+4\cos2t+3\bigr),
\qquad
\sin^4t=\frac18\bigl(\cos4t-4\cos2t+3\bigr).
$$

### Solution 1.1 — Intégrale double

On effectue le changement de variables

$$
\begin{cases}x=a\rho\cos\theta,\\y=b\rho\sin\theta.\end{cases}
$$

Sa matrice jacobienne et son déterminant sont

$$
\begin{pmatrix}
a\cos\theta&-a\rho\sin\theta\\
b\sin\theta&b\rho\cos\theta
\end{pmatrix},
\qquad \operatorname{Jac}=ab\rho.
$$

Ainsi,

$$
\begin{aligned}
I&=\int_0^1\int_0^{2\pi}
\bigl(a^2\rho^2\cos^2\theta+b^2\rho^2\sin^2\theta\bigr)ab\rho\,d\theta\,d\rho\\
&=ab\left(\int_0^1\rho^3\,d\rho\right)
\left(\int_0^{2\pi}(a^2\cos^2\theta+b^2\sin^2\theta)\,d\theta\right)\\
&=ab\left[\frac{\rho^4}{4}\right]_0^1
\left[a^2\left(\frac{\sin2\theta}{4}+\frac\theta2\right)
+b^2\left(\frac\theta2-\frac{\sin2\theta}{4}\right)\right]_0^{2\pi}\\
&=\frac{ab}{4}(a^2+b^2)\pi.
\end{aligned}
$$

> **Coquilles de la source, page 1.** L’ordre des différentiels est inversé dans la première intégrale itérée. Dans la primitive angulaire, le PDF écrit $\sin(2a)$ et $1/2$ au lieu de $\sin(2\theta)$ et $\theta/2$. La ligne est rectifiée ci-dessus ; le résultat final du PDF est correct. Le déterminant jacobien y est également noté $J$, comme l’intégrale curviligne.

### Solution 1.2 — Intégrale curviligne

On utilise le paramétrage direct

$$
x(t)=a\cos t,\qquad y(t)=b\sin t,\qquad t\in[0,2\pi].
$$

> L’orientation n’est pas précisée dans l’énoncé ; ce paramétrage du corrigé parcourt l’ellipse dans le sens trigonométrique.

On obtient

$$
J=\int_0^{2\pi}\bigl(-ab^3\sin^4t-a^3b\cos^4t\bigr)\,dt.
$$

Avec les formules de linéarisation,

$$
\begin{aligned}
J&=-\frac{ab}{8}\int_0^{2\pi}
\bigl((b^2+a^2)\cos4t+4(a^2-b^2)\cos2t+3(a^2+b^2)\bigr)\,dt\\
&=-\frac{ab}{8}(a^2+b^2)\left[\frac{\sin4t}{4}+3t\right]_0^{2\pi}
-\frac{ab}{2}(a^2-b^2)\left[\frac{\sin2t}{2}\right]_0^{2\pi}\\
&=-\frac{3ab(a^2+b^2)\pi}{4}.
\end{aligned}
$$

### Solution 1.3 — Relation entre les intégrales

On remarque que $J=-3I$, conformément à Green–Riemann. En posant

$$
y^3\,dx-x^3\,dy=P(x,y)\,dx+Q(x,y)\,dy,
$$

on a bien

$$
\frac{\partial Q}{\partial x}(x,y)-\frac{\partial P}{\partial y}(x,y)
=-3(x^2+y^2).
$$

## Exercice 2 — Intégrale sur une courbe fermée

Soit $\Gamma$ la courbe orientée dans le sens trigonométrique, constituée des portions de la droite $y=x$ et de la parabole $y=x^2$ comprises entre leurs points d’intersection.

1. Calculer $I=\int_\Gamma(y+xy)\,dx$.
2. Retrouver cette valeur avec la formule de Green–Riemann.

### Solution 2.1 — Paramétrage

Les deux intersections sont $(0,0)$ et $(1,1)$. La portion de parabole est paramétrée par $x=t$, $y=t^2$, pour $t$ de $0$ à $1$. La portion de droite est paramétrée par $x=y=t$, pour $t$ de $1$ à $0$ : attention au sens ! Ainsi,

$$
I=\int_0^1(t^2+t^3)\,dt-\int_0^1(t+t^2)\,dt=-\frac14.
$$

### Solution 2.2 — Green–Riemann

On pose $P(x,y)=y+xy$ et $Q(x,y)=0$. Alors

$$
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=-(1+x),
\qquad
I=-\iint_D(1+x)\,dx\,dy,
$$

avec $D=\{(x,y)\in\mathbb R^2:0\leq x\leq1,\ x^2\leq y\leq x\}$. D’où

$$
I=-\int_0^1\left(\int_{x^2}^x(1+x)\,dy\right)dx
=-\int_0^1(1+x)(x-x^2)\,dx=-\frac14.
$$

## Exercice 3 — Racines d’un polynôme aléatoire

On jette trois fois un dé à six faces, et l’on note $a,b,c$ les résultats successifs. On pose $P(X)=aX^2+bX+c$. Déterminer la probabilité que $P$ ait :

1. deux racines réelles distinctes ;
2. une racine réelle double.

### Solution 3.1 — Deux racines distinctes

Il y a $6^3$ possibilités. Le calcul du corrigé suppose les lancers indépendants et le dé équilibré.

Les racines sont réelles et distinctes si et seulement si $\Delta>0$, soit $b^2>4ac$. Les possibilités sont :

| $b$ | $b^2$ | Couples $(a,c)$ possibles |
| --- | ---: | --- |
| $1$ | $1$ | Aucun |
| $2$ | $4$ | Aucun |
| $3$ | $9$ | $(1,1),(1,2),(2,1)$ |
| $4$ | $16$ | $(1,1),(1,2),(1,3),(2,1),(3,1)$ |
| $5$ | $25$ | $(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(5,1),(6,1)$ |
| $6$ | $36$ | $(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2),(5,1),(6,1)$ |

Au total, il y a $38$ cas favorables, donc

$$
\mathbb P(\Delta>0)=\frac{19\times2}{6^2\times3\times2}
=\frac{19}{2^2\times3^3}=\frac{19}{108}.
$$

### Solution 3.2 — Racine double

Il y a une racine double si et seulement si $\Delta=0$, soit $b^2=4ac$, donc $b=2\sqrt{ac}$. Seules les valeurs paires de $b$ peuvent convenir :

- $b=2$ : $(a,c)=(1,1)$.
- $b=4$ : $ac=4$, donc $(a,c)=(1,4),(4,1),(2,2)$.
- $b=6$ : $ac=9$, donc $(a,c)=(3,3)$.

Il y a cinq cas favorables, donc

$$
\mathbb P(\Delta=0)=\frac5{3^3\times2^3}=\frac5{216}.
$$

## Exercice 4 — Probabilités de beau temps

Des études statistiques ont permis d’estimer que, s’il fait beau un jour, la probabilité qu’il fasse beau le lendemain est $0{,}7$. S’il ne fait pas beau, la probabilité qu’il fasse beau le lendemain est $0{,}4$.

1. Un mercredi, il fait beau. Quelle est la probabilité qu’il fasse beau le vendredi suivant ?
2. Quelle est la probabilité qu’il fasse beau un vendredi s’il n’a pas fait beau le mercredi précédent ?
3. Quelle est la probabilité $P_n$ qu’il fasse beau le $n$-ième jour après un jour où il a fait beau ?
4. Quelle est la limite de $P_n$ lorsque $n\to+\infty$ ?

### Solution 4.1 — Mercredi beau

On note $B_n$ l’événement « il fait beau le jour $n$ », et $BM,BJ,BV$ les événements correspondants pour mercredi, jeudi, vendredi. On a

$$
\mathbb P(B_2\mid B_1)=0{,}7,
\qquad
\mathbb P(B_2\mid\overline{B_1})=0{,}4.
$$

Comme il fait beau mercredi,

$$
\begin{aligned}
\mathbb P(BJ)
&=\mathbb P(BJ\mid BM)\underbrace{\mathbb P(BM)}_{=1}
+\mathbb P(BJ\mid\overline{BM})\underbrace{\mathbb P(\overline{BM})}_{=0}\\
&=\mathbb P(BJ\mid BM)=0{,}7.
\end{aligned}
$$

Donc

$$
\begin{aligned}
\mathbb P(BV)
&=\mathbb P(BV\mid BJ)\mathbb P(BJ)
+\mathbb P(BV\mid\overline{BJ})\mathbb P(\overline{BJ})\\
&=0{,}7\times0{,}7+0{,}4\times(1-0{,}7)=0{,}61.
\end{aligned}
$$

### Solution 4.2 — Mercredi sans beau temps

On a $\mathbb P(BJ)=0{,}4$ et $\mathbb P(\overline{BJ})=0{,}6$, donc

$$
\mathbb P(BV)=0{,}7\times0{,}4+0{,}4\times0{,}6=0{,}52.
$$

### Solution 4.3 — Expression de $P_n$

On a $P_0=1$, $P_1=0{,}7$, $P_2=0{,}61$. Puis

$$
\begin{aligned}
P_n
&=\mathbb P(B_n\mid B_{n-1})P_{n-1}
+\mathbb P(B_n\mid\overline{B_{n-1}})(1-P_{n-1})\\
&=0{,}7P_{n-1}+0{,}4(1-P_{n-1})\\
&=0{,}4+0{,}3P_{n-1}
=0{,}4+0{,}3(0{,}4+0{,}3P_{n-2})\\
&=\cdots\\
&=0{,}4\sum_{k=0}^{n-1}0{,}3^k+0{,}3^nP_0\\
&=0{,}4\frac{1-0{,}3^n}{0{,}7}+0{,}3^n
=\frac47(1-0{,}3^n)+0{,}3^n.
\end{aligned}
$$

> **Coquilles de la source, page 4.** La première ligne note la probabilité complémentaire $\overline{P_{n-1}}$ ; elle est explicitée ici par $1-P_{n-1}$. Dans la ligne contenant la somme géométrique, le PDF écrit $0{,}3^3P_0$ au lieu de $0{,}3^nP_0$ ; l’exposant $n$ apparaît correctement dans la ligne suivante.

### Solution 4.4 — Limite

Comme $0<0{,}3<1$,

$$
\lim_{n\to+\infty}P_n=\frac47.
$$

## Exercice 5 — Probabilités conditionnelles

Dans la forêt équatoriale, chaque naissance de gorilles donne un gorille gaucher avec une probabilité égale à $0{,}3$. Un gorille gaucher sur trois a les yeux bleus, et un gorille droitier sur quatre a les yeux bleus.

1. Calculer la probabilité qu’un gorille pris au hasard ait les yeux bleus.
2. Calculer la probabilité qu’un gorille ayant les yeux bleus soit gaucher.
3. Calculer la probabilité que, pour six naissances, il y ait au moins un gorille gaucher aux yeux bleus.

### Solution 5.1 — Yeux bleus

On note $B$ l’événement « yeux bleus », $G$ « gaucher », et $D$ « droitier ». Alors

$$
\begin{aligned}
\mathbb P(B)
&=\mathbb P(B\mid G)\mathbb P(G)+\mathbb P(B\mid D)\mathbb P(D)\\
&=\frac13\times0{,}3+\frac14\times0{,}7
=\frac1{10}+\frac7{40}=\frac{11}{40}.
\end{aligned}
$$

### Solution 5.2 — Gaucher sachant les yeux bleus

$$
\mathbb P(G\mid B)
=\frac{\mathbb P(G\cap B)}{\mathbb P(B)}
=\frac{\mathbb P(B\mid G)\mathbb P(G)}{\mathbb P(B)}
=\frac{\frac13\times0{,}3}{11/40}
=\frac4{11}.
$$

### Solution 5.3 — Au moins un sur six naissances

Soit $E$ l’événement « pour six naissances, au moins un gorille gaucher aux yeux bleus ». On a

$$
\mathbb P(G\cap B)=\frac3{10}\times\frac13=\frac1{10},
\qquad
\mathbb P(\overline{G\cap B})=\frac9{10}.
$$

Le calcul du corrigé suppose les six naissances indépendantes. Par suite,

$$
\mathbb P(\overline E)
=\bigl(\mathbb P(\overline{G\cap B})\bigr)^6
=\left(\frac9{10}\right)^6
=0{,}531441\simeq0{,}531.
$$

Donc

$$
\mathbb P(E)=1-0{,}531441=0{,}468559\simeq0{,}469.
$$

**Autre méthode indiquée par la source :** considérer une variable aléatoire suivant une loi binomiale.

> Les égalités avec $0{,}531$ et $0{,}469$ dans le PDF sont des arrondis, explicités ici par $\simeq$.
