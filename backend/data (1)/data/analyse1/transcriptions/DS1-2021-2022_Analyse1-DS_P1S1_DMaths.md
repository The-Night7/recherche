# Analyse 1 — DS1 2021–2022, corrigé (18 novembre 2021)

> Source : `PREING1-S1/Analyse1-DS/DS1-2021-2022_Analyse1-DS_P1S1_DMaths.pdf`, 5 pages (PDF natif LaTeX).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. Le document est intitulé « Correction DS1 Analyse - 18 novembre 2021 » (Département de Mathématiques, PréING1-Analyse, 2021-2022). Dans la source, les énoncés sont en noir et les solutions et le barème en rouge. Ici, les énoncés sont en **gras** et les solutions en texte courant.
> Vérification : les calculs ont été refaits. Erreurs ou lacunes de la source, signalées et non corrigées dans le texte :
> - **Exercice 2.2** : $-1\le E(x)\le0\iff-1\le x<1$, et non $-1<x<1$. Le réel $x=-1$ est solution, puisque $(2E(-1)+1)^2=1<4$. L’ensemble correct est $S_2=[-1;1[$.
> - **Exercice 5** : l’hypothèse par l’absurde doit porter sur **tous** les $x\in A$ (« $\forall x\in A,\ \sqrt x\ge\sqrt{\inf(A)}+\epsilon$ ») pour que la contradiction avec la définition de $\inf(A)$ soit valide.
> - Coquilles conservées : « ce qui impossible », « $B$ ne possède de minimum », « $=\,]-2,-\sqrt2]\cup[\sqrt2,4[$ » sans le nom de l’ensemble $A$.

## Exercice 1

**Résoudre, dans $\mathbb R$, les équations suivantes :**

### 1. $\sin(3x)=\cos(x)$ (1 point)

**Solution :** Nous avons

$$\begin{aligned}
\sin(3x)=\cos(x)&\iff\sin(3x)=\sin\left(x+\frac\pi2\right)\\
&\iff3x\equiv x+\frac\pi2\ [2\pi]\ \text{ ou }\ 3x\equiv\pi-x-\frac\pi2\ [2\pi]\\
&\iff2x\equiv\frac\pi2\ [2\pi]\ \text{ ou }\ 4x\equiv\frac\pi2\ [2\pi]\\
&\iff2x=\frac\pi2+2k\pi,\ k\in\mathbb Z\ \text{ ou }\ 4x=\frac\pi2+2k\pi,\ k\in\mathbb Z\\
&\iff x=\frac\pi4+k\pi,\ k\in\mathbb Z\ \text{ ou }\ x=\frac\pi8+\frac{k\pi}2,\ k\in\mathbb Z
\end{aligned}$$

Ainsi, l’ensemble solution de l’équation $\sin(3x)=\cos(x)$ est donné par

$$\left\{\frac\pi4+k\pi,\ \frac\pi8+\frac{k\pi}2\ :\ k\in\mathbb Z\right\}=\left\{\frac\pi4+k\pi,\ \frac\pi8+k\pi,\ \frac{5\pi}8+k\pi\ :\ k\in\mathbb Z\right\}.$$

### 2. $\tan^2\left(3x+\frac\pi3\right)-3=0$ (1,5 point)

**Solution :** Pour tout $x\in\mathbb R$ tel que $3x+\frac\pi3\neq\frac\pi2+k\pi$, $k\in\mathbb Z$ (i.e. $x\neq\frac\pi{18}+\frac{k\pi}3$), nous avons

$$\begin{aligned}
\tan^2\left(3x+\frac\pi3\right)-3=0&\iff\tan^2\left(3x+\frac\pi3\right)=3\\
&\iff\tan\left(3x+\frac\pi3\right)=\pm\sqrt3\\
&\iff\tan\left(3x+\frac\pi3\right)=\pm\tan\left(\frac\pi3\right)\\
&\iff\tan\left(3x+\frac\pi3\right)=\tan\left(\frac\pi3\right)\ \text{ ou }\ \tan\left(3x+\frac\pi3\right)=\tan\left(-\frac\pi3\right)\\
&\iff3x+\frac\pi3=\frac\pi3\ [\pi]\ \text{ ou }\ 3x+\frac\pi3=-\frac\pi3\ [\pi]\\
&\iff3x=0\ [\pi]\ \text{ ou }\ 3x=-\frac{2\pi}3\ [\pi]\\
&\iff3x=k\pi,\ k\in\mathbb Z\ \text{ ou }\ 3x=-\frac{2\pi}3+k\pi,\ k\in\mathbb Z\\
&\iff x=\frac{k\pi}3,\ k\in\mathbb Z\ \text{ ou }\ x=-\frac{2\pi}9+\frac{k\pi}3,\ k\in\mathbb Z
\end{aligned}$$

Ainsi, l’ensemble solution de l’équation $\tan^2\left(3x+\frac\pi3\right)-3=0$ est donné par

$$\begin{aligned}
&\left\{\frac{k\pi}3,\ -\frac{2\pi}9+\frac{k\pi}3\ :\ k\in\mathbb Z\right\}\\
&=\left\{k\pi,\ \frac\pi3+k\pi,\ \frac{2\pi}3+k\pi,\ -\frac{2\pi}9+k\pi,\ \frac\pi9+k\pi,\ \frac{4\pi}9+k\pi\ :\ k\in\mathbb Z\right\}.
\end{aligned}$$

### 3. $(5E(x)+2)\cdot(3E(x)+6)=0$ (1,5 point)

**Solution :** Nous avons

$$(5E(x)+2)\cdot(3E(x)+6)=0\iff E(x)=-\frac25\ \text{ ou }\ E(x)=-\frac63=-2.$$

Or pour tout $x\in\mathbb R$, $E(x)$ est un entier. Donc l’équation $E(x)=-\frac25$ n’a pas de solution. Ainsi

$$(5E(x)+2)\cdot(3E(x)+6)=0\iff E(x)=-2\iff x\in[-2,-1[.$$

## Exercice 2

**Résoudre, dans $\mathbb R$, les inéquations suivantes :**

### 1. $\left|\frac1x+1\right|<1$ (1 point)

**Solution :** Il faut que $x\neq0$ : cette inéquation est équivalente à $-1<\frac1x+1<1$.

- Si $x>0$, on obtient $-x<1+x<x$ ce qui impossible.
- Si $x<0$, on obtient $x<1+x<-x$ ce qui implique que $x<-\frac12$.

Donc, $S_1=]-\infty;-\frac12[$.

### 2. $(2E(x)+1)^2<4$ (1,5 point)

**Solution :** On cherche à résoudre $(2E(x)+1)^2<4$ ce qui est équivalent à $|2E(x)+1|<2\Leftrightarrow-2<2E(x)+1<2$. On obtient

$$-\frac32<E(x)<\frac12\quad\Leftrightarrow\quad-1\le E(x)\le0\quad\Leftrightarrow\quad-1<x<1.$$

Donc, $S_2=]-1;1[$.

> Erreur de la source : la dernière équivalence donne $-1\le x<1$, soit $S_2=[-1;1[$ (voir l’avertissement en tête).

### 3. $\sqrt{x^2-1}<2-x$ (1,5 point)

**Solution :** On cherche à résoudre $\sqrt{x^2-1}<2-x$. Tout d’abord, cette inéquation est définie si $x^2-1\ge0$ et $0<2-x$, ce qui équivaut à

$$x\in\,]-\infty;-1]\cup[1;2[.$$

Dans ce cas, en passant au carré de deux côtés, on obtient

$$x^2-1<4-4x+x^2\quad\Leftrightarrow\quad4x<5\quad\Leftrightarrow x<\frac54.$$

Donc, $S_3=]-\infty;-1]\cup[1;\frac54[$.

## Exercice 3

**Calculer les sommes et les produits suivants :**

### 1. $\displaystyle\sum_{k=0}^{n}\frac{k}{(k+1)!}$ (1,5 point)

**Solution :** Nous avons

$$\begin{aligned}
\sum_{k=0}^{n}\frac{k}{(k+1)!}&=\sum_{k=0}^{n}\frac{(k+1)-1}{(k+1)!}\\
&=\sum_{k=0}^{n}\frac{k+1}{(k+1)!}-\frac1{(k+1)!}\\
&=\sum_{k=0}^{n}\frac1{k!}-\frac1{(k+1)!}\\
&=\frac1{0!}-\frac1{(n+1)!}=1-\frac1{(n+1)!}.
\end{aligned}$$

### 2. $\displaystyle\sum_{k=0}^{n}\frac{(-1)^k}{3^{k+1}}\binom nk$ (1,5 point)

**Solution :** Nous avons

$$\begin{aligned}
\sum_{k=0}^{n}\frac{(-1)^k}{3^{k+1}}\binom nk&=\frac13\sum_{k=0}^{n}\binom nk\left(-\frac13\right)^k\\
&=\frac13\sum_{k=0}^{n}\binom nk1^{n-k}\left(-\frac13\right)^k\\
&=\frac{\left(1-\frac13\right)^n}{3}\\
&=\frac{\left(\frac23\right)^n}{3}.
\end{aligned}$$

### 3. $\displaystyle\prod_{k=0}^{n}(-5)\cdot e^k$ (1 point)

**Solution :** Nous avons

$$\begin{aligned}
\prod_{k=0}^{n}(-5)\cdot e^k&=\prod_{k=0}^{n}(-5)\cdot\prod_{k=0}^{n}e^k\\
&=(-5)^{n+1}e^{\sum_{k=0}^{n}k}\\
&=(-5)^{n+1}e^{\frac{n(n+1)}2}.
\end{aligned}$$

## Exercice 4

**On considère les ensembles $A$ et $B$ suivants**

$$A=\left\{x\in\mathbb R : x^2-2\ge0\ \text{ et }\ |x-1|<3\right\}\quad;\quad B=\left\{(-1)^n+\frac1n : n\in\mathbb N^*\right\}.$$

### 1. Les ensembles $A$ et $B$ sont-ils majorés, minorés ? Justifier votre réponse.

**Solution :** (1 point) Commençons par étudier l’ensemble $A$. Nous avons

$$\begin{aligned}
x\in A&\iff x^2-2\ge0\ \text{ et }\ |x-1|<3\iff x^2\ge2\ \text{ et }\ -3<x-1<3\\
&\iff\left(x\le-\sqrt2\ \text{ ou }\ x\ge\sqrt2\right)\ \text{ et }\ -2<x<4\\
&\iff x\in\left(]-\infty,-\sqrt2]\cup[\sqrt2,\infty[\right)\cap\,]-2,4[\\
&\iff x\in\,]-2,-\sqrt2]\cup[\sqrt2,4[.
\end{aligned}$$

Ainsi

$$A=]-2,-\sqrt2]\cup[\sqrt2,4[.$$

Par conséquent, $A$ est majorée par tout réel supérieur ou égal à $4$, et $A$ est minorée par tout réel inférieur ou égal à $-2$.

(1 point) Étudions maintenant l’ensemble $B$. On commence par noter que

- si $n\neq0$ est pair, nous avons
  $$(-1)^n=1\quad\text{et}\quad0<\frac1n\le\frac12\quad\implies\quad1<(-1)^n+\frac1n\le1+\frac12=\frac32.$$
- si $n\neq0$ est impair, nous avons
  $$(-1)^n=-1\quad\text{et}\quad0<\frac1n\le1\quad\implies\quad-1<(-1)^n+\frac1n\le-1+1=0.$$

Ainsi

$$\forall n\in\mathbb N^*,\ (-1)^n+\frac1n\in\,]-1,0]\cup\left]1,\frac32\right]$$

Par conséquent, $B$ est majorée par tout réel supérieur ou égal à $\frac32$, et $B$ est minorée par tout réel inférieur ou égal à $-1$.

### 2. Pour chaque ensemble $A$ et $B$ déterminer, s’il existe, les bornes supérieure et inférieure ainsi que le plus grand et le plus petit élément.

**Solution :** (1,5 point) Commençons par étudier l’ensemble $A$. D’après la question précédente, nous avons

$$=\,]-2,-\sqrt2]\cup[\sqrt2,4[.$$

Donc

$$\sup A=4\quad\text{et}\quad\inf A=-2.$$

L’ensemble $A$ ne possède ni de maximum ni de minimum.

(2,5 points) Étudions maintenant l’ensemble $B$. D’après la question précédente, nous avons

$$\forall n\in\mathbb N^*,\ (-1)^n+\frac1n\in\,]-1,0]\cup\left]1,\frac32\right].$$

Or

$$\frac32=(-1)^2+\frac12\implies\frac32\in B.$$

Ainsi, $\frac32$ est un majorant de $B$ qui appartient à $B$. Ce qui nous permet de conclure

$$\sup B=\max B=\frac32.$$

Pour trouver la borne inférieure de $B$, étudions la suite

$$\forall k\in\mathbb N,\ u_k=(-1)^{2k+1}+\frac1{2k+1}=-1+\frac1{2k+1}.$$

Pour tout $k\in\mathbb N$, nous avons

$$u_k\ge\inf B.$$

Donc par passage à la limite (la limite préserve les inégalités larges), on obtient

$$-1=\lim_{k\to+\infty}u_k\ge\lim_{k\to+\infty}\inf B=\inf B.$$

Or comme $-1$ est un minorant de $B$, et $\inf B$ est le plus grand de minorants, on conclut $\inf B\ge-1$. Par conséquent, l’ensemble $B$ ne possède de minimum et

$$\inf B=-1.$$

## Exercice 5

**Soit $A$ un sous-ensemble non vide borné de $\mathbb R_+$. On définit**

$$\sqrt A=\left\{\sqrt x :\ x\in A\right\}.$$

**Montrer que**

$$\inf(\sqrt A)=\sqrt{\inf(A)}.$$

**Solution :** (2 points) Comme $A$ est borné et positive, alors $\inf(A)$ existe et il est positif. Comme $A$ est non vide, alors $\sqrt A$ l’est aussi. De plus, $\sqrt A$ est positive et borné. Donc, $\inf(\sqrt A)$ existe et positif.

Maintenant, pour tout $x\in A$, $x\ge\inf(A)\ge0$. Comme la fonction $x\mapsto\sqrt x$ est strictement croissante, on en déduit que

$$\sqrt x\ge\sqrt{\inf(A)},\quad\forall x\in A.$$

Donc, $\sqrt{\inf(A)}$ est un minorant de $\sqrt A$. Il reste à montrer que $\sqrt{\inf(A)}$ est le plus grand minorant de $\sqrt A$. Supposons par absurde qu’il existe $\epsilon>0$ tel que $\sqrt x\ge\sqrt{\inf(A)}+\epsilon>\sqrt{\inf(A)}\ge0$. En passant au carré, on obtient

$$x\ge\inf(A)+2\epsilon\sqrt{\inf(A)}+\epsilon^2>\inf(A).$$

Ce qui est impossible car $\inf(A)$ est le plus grand minorant de $A$. Finalement, $\inf(\sqrt A)=\sqrt{\inf(A)}$.
