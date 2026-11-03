# Algèbre 1 — DS1 du 22 octobre 2020, sujet et corrigé

> Source : `PREING1-S1/Algebre1-DS/DS1-2020-2021-Correction_Algebre1-DS_P1S1_NArancibia-MBahtiti-KGuezguez-AHajej-BLaquerriere-JMasereel.pdf`, 3 pages.
> CY Tech, cycle préparatoire, première année. N. Arancibia, M. Bahtiti, K. Guezguez, A. Hajej, B. Laquerriere, J.-M. Masereel. Jeudi 22 octobre 2020 ; durée : 1 h 30 ; appareils électroniques et documents interdits.
> Transcription du 12 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif, restitution des formules et du barème manuscrit par exercice. Les erreurs de source sont distinguées dans des notes.

Il sera tenu compte de la qualité de la rédaction et de la précision des justifications. Le sujet comporte cinq exercices, à traiter dans l’ordre choisi. Barème manuscrit : exercice 1, 4 points ; exercice 2, 3,5 points ; exercice 3, 1,5 point ; exercice 4, 7 points ; exercice 5, 4 points.

## Exercice 1 — Négation et contraposée (page 1)

Dans chacun des cas, donner, lorsque c’est possible, la négation et la contraposée.

1. $\forall\varepsilon>0,\ \exists\eta>0,\ \forall a>0,\ \forall b>0,\quad (|a-b|<\eta\Rightarrow|f(a)-f(b)|<\varepsilon)$.
2. $[\forall u\in E,\ (f(u)=0\Rightarrow g(u)=0)]\Rightarrow[\exists\beta>0,\ g\leq\beta f]$.

### Corrigé

1. Négation imprimée :

   $$\exists\varepsilon,\ \forall\eta>0,\ \exists a>0,\ \exists b>0,\quad (|a-b|<\eta\text{ ET }|f(a)-f(b)|\geq\varepsilon).$$

   Pas de contraposée, car l’énoncé global n’est pas une implication.

2. Négation imprimée :

   $$[\forall u\in E,\ (f(u)=0\Rightarrow g(u)=0)]\text{ ET }[\forall\beta>0,\ g>\beta f].$$

   Contraposée imprimée :

   $$[\forall\beta>0,\ g>\beta f]\Rightarrow[\exists u\in E,\ (f(u)=0\text{ ET }g(u)\neq0)].$$

**Notes sur la source.** La négation de la première proposition omet la condition $\varepsilon>0$ : il faut écrire $\exists\varepsilon>0$. Pour la seconde, si $f$ et $g$ sont des fonctions et $g\leq\beta f$ désigne l’ordre ponctuel, sa négation n’est pas $g>\beta f$ en tout point : c’est $\exists x\in E,\ g(x)>\beta f(x)$. Les deux formules du corrigé se lisent donc rigoureusement avec $[\forall\beta>0,\ \neg(g\leq\beta f)]$ à la place de $[\forall\beta>0,\ g>\beta f]$.

## Exercice 2 — Différence de carrés (pages 1–2)

1. Démontrer : $\forall a,b\in\mathbb N^*,\ b>a\Rightarrow b^2-a^2\geq3$.
2. En déduire que, pour tout $n\in\mathbb N^*$, $\sqrt{n^2+1}$ n’est pas entier.

### Corrigé

1. Première solution : $b^2-a^2=(b-a)(b+a)$. Puisque $b>a>0$ sont entiers, $b-a\geq1$, $b\geq2$ et $b+a\geq2+1=3$. Donc $b^2-a^2\geq3$.

   Seconde solution : $b\geq a+1$. Par croissance de la fonction carré sur les nombres positifs :

   $$b^2\geq(a+1)^2=a^2+2a+1,\qquad b^2-a^2\geq2a+1\geq2\times1+1=3.$$

2. Par l’absurde, supposons que $\sqrt{n^2+1}$ soit entier pour un $n\in\mathbb N^*$. Posons $b=\sqrt{n^2+1}\in\mathbb N^*$ et $a=n\in\mathbb N^*$. Alors $b>a$ et $b^2-a^2=1<3$, en contradiction avec la propriété précédente. Ainsi :

   $$\forall n\in\mathbb N^*,\quad\sqrt{n^2+1}\notin\mathbb N.$$

## Exercice 3 — Parité (page 2)

Soit $n\in\mathbb Z$. Montrer que $n^2-6n+5$ pair implique $n$ impair.

**Corrigé par contraposée.** Supposons $n$ pair. Alors $n^2$ est pair ; $n^2-6n$ est pair et $n^2-6n+5$ est impair.

## Exercice 4 — Suite récurrente (page 2)

Soit la suite $(x_n)_{n\in\mathbb N}$ définie par :

$$x_0=4,\qquad x_{n+1}=\frac{2x_n^2-3}{x_n+2}.$$

1. Montrer que $\forall n\in\mathbb N,\ x_n>3$. Indication : $2x^2-3x-9=(x-3)(2x+3)$.
2. En déduire que $\forall n\in\mathbb N,\ x_{n+1}-3>\frac32(x_n-3)$.
3. En déduire que $\forall n\in\mathbb N,\ x_n\geq(\frac32)^n+3$.

### Corrigé

1. Par récurrence sur $P(n)$ : « $x_n>3$ ».

   Initialisation : $x_0=4>3$.

   Hérédité : supposons $x_n>3$. Alors :

   $$
   \begin{aligned}
   x_{n+1}-3
   &=\frac{2x_n^2-3}{x_n+2}-3
   =\frac{2x_n^2-3-3(x_n+2)}{x_n+2}\\
   &=\frac{2x_n^2-3x_n-9}{x_n+2}
   =\frac{(2x_n+3)(x_n-3)}{x_n+2}.
   \end{aligned}
   $$

   Le numérateur et le dénominateur sont strictement positifs, donc $x_{n+1}>3$. La propriété est vraie pour tout $n\in\mathbb N$.

2. Calcul direct :

   $$
   \begin{aligned}
   x_{n+1}-3-\frac32(x_n-3)
   &=\frac{(2x_n+3)(x_n-3)}{x_n+2}-\frac32(x_n-3)\\
   &=(x_n-3)\frac{2(2x_n+3)-3(x_n+2)}{2(x_n+2)}\\
   &=\frac{x_n(x_n-3)}{2(x_n+2)}>0.
   \end{aligned}
   $$

   D’où $x_{n+1}-3>\frac32(x_n-3)$.

   **Note sur la source.** Le facteur $2$ du dénominateur de la ligne intermédiaire est absent dans le PDF ; il est rétabli ici. La dernière expression imprimée est correcte.

3. Par récurrence sur $P(n)$ : « $x_n\geq(\frac32)^n+3$ ».

   Initialisation : $x_0=4=(\frac32)^0+3$.

   Hérédité : si la propriété est vraie au rang $n$, alors

   $$x_{n+1}-3>\frac32(x_n-3)\geq\frac32\left(\frac32\right)^n=\left(\frac32\right)^{n+1}.$$

   Donc $P(n+1)$ est vraie, et $\forall n\in\mathbb N,\ x_n\geq(\frac32)^n+3$.

## Exercice 5 — Produits cartésiens (page 3)

Soient $A,B,C,D$ quatre ensembles. Quelle relation existe entre $(A\times C)\cup(B\times D)$ et $(A\cup B)\times(C\cup D)$ ?

### Corrigé

Soit $x=(x_1,x_2)\in(A\times C)\cup(B\times D)$.

- Si $x\in A\times C$, alors $x_1\in A\subset A\cup B$ et $x_2\in C\subset C\cup D$.
- Sinon, $x\in B\times D$, donc $x_1\in B\subset A\cup B$ et $x_2\in D\subset C\cup D$.

Dans les deux cas, $x\in(A\cup B)\times(C\cup D)$. Ainsi :

$$\boxed{(A\times C)\cup(B\times D)\subset(A\cup B)\times(C\cup D).}$$

Il n’y a pas d’inclusion réciproque en général. Par exemple, dans $\mathbb R$, prendre $A=C=[1;3]$ et $B=D=[4;6]$. Alors $5\in B\subset A\cup B$ et $2\in C\subset C\cup D$, donc $(5,2)\in(A\cup B)\times(C\cup D)$. Pourtant $5\notin A$ et $2\notin D$ ; par conséquent $(5,2)$ n’appartient ni à $A\times C$, ni à $B\times D$, ni à leur réunion.
