# Analyse 1 — DS1 2020–2021, corrigé (version 3)

> Source : `PREING1-S1/Analyse1-DS/DS1-2020-2021-V3_Analyse1-DS_P1S1_DMaths.pdf`, 3 pages (document dactylographié).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. Malgré son nom, le fichier est un **corrigé** (titre « Corrigé DS1 ») : énoncés en noir, solutions en rouge dans la source. Ici, les énoncés sont en **gras** ou en titre et les solutions en texte courant. Les calculs ont été vérifiés ; aucune erreur mathématique n’a été relevée.

## Exercice 1

**Résoudre l’inéquation : $\sqrt{2x^2-8}\geqslant x-1$.**

$D_f=]-\infty,-2]\cup[2,+\infty[$.

- Sur $]-\infty,-2]$, on a : $x\leqslant-2\implies x-1\leqslant-3\leqslant0\leqslant\sqrt{2x^2-8}$.
  Tous les éléments de $S_1=]-\infty,-2]$ sont solution.
- Sur $[2,+\infty[$ :
  On élève au carré : $2x^2-8\geqslant x^2-2x+1\iff x^2+2x-9\geqslant0$.
  Racines : $-1-\sqrt{10}$ et $-1+\sqrt{10}$, donc $S_2=[-1+\sqrt{10},+\infty[$.

$$S=]-\infty,-2]\cup[-1+\sqrt{10},+\infty[$$

## Exercice 2

**Résoudre les 2 équations suivantes :**

### 1. $2\cos^2(x)+9\cos(x)+4=0$

$2x^2+9x+4=0$ a pour solutions : $-\frac12$ et $-4<-1$.

$$\cos(x)=-\frac12=\cos\left(\frac{2\pi}3\right)\iff\begin{cases}x=\dfrac{2\pi}3+2k\pi, & k\in\mathbb Z\\ \text{ou}\\ x=-\dfrac{2\pi}3+2k\pi, & k\in\mathbb Z\end{cases}$$

### 2. $\sin\left(2x+\frac\pi4\right)=-\sin(x)$

$$\sin\left(2x+\frac\pi4\right)=-\sin(x)=\sin(-x)\iff\begin{cases}2x+\dfrac\pi4=-x+2k\pi, & k\in\mathbb Z\\ \text{ou}\\ 2x+\dfrac\pi4=\pi-(-x)+2k\pi, & k\in\mathbb Z\end{cases}$$

$$\iff\begin{cases}3x=-\dfrac\pi4+2k\pi, & k\in\mathbb Z\\ \text{ou}\\ x=\pi-\dfrac\pi4+2k\pi, & k\in\mathbb Z\end{cases}\iff\begin{cases}x=-\dfrac\pi{12}+\dfrac{2k\pi}3, & k\in\mathbb Z\\ \text{ou}\\ x=\dfrac{3\pi}4+2k\pi, & k\in\mathbb Z\end{cases}$$

## Exercice 3

**On considère la fonction : $f(x)=\dfrac{E(x)}{2E(x)-1}$, où $E(x)$ désigne la partie entière de $x$.**

1. **Justifier que $f$ est définie sur $\mathbb R$ tout entier.**

   $2E(x)-1=0\iff E(x)=\frac12$, impossible car $E(x)\in\mathbb Z$.

2. **Donner l’expression de $f(x)$ lorsque $x\in\mathbb Z$.**

   $$x\in\mathbb Z\implies E(x)=x\implies f(x)=\frac{E(x)}{2E(x)-1}=\frac{x}{2x-1}$$

3. **Déterminer, s’il en existe, tous les antécédents de $1$.**

   On vous demande donc de résoudre : $f(x)=1$.

   $$f(x)=1\iff\frac{E(x)}{2E(x)-1}=1\iff E(x)=2E(x)-1\iff E(x)=1$$

   Donc $x\in[1,2[$.

4. **Même question pour $-3$.**

   $$f(x)=-3\iff\frac{E(x)}{2E(x)-1}=-3\iff E(x)=-6E(x)+3\iff7E(x)=3\iff E(x)=\frac73$$

   Impossible !! Donc il n’y a pas d’antécédent pour $-3$.

## Exercice 4

**Calculer les sommes ou produits suivants :**

1. $\displaystyle S_1=\sum_{k=0}^{n}2^{2k+1}$

   $$S_1=\sum_{k=0}^{n}2^{2k+1}=2\sum_{k=0}^{n}4^k=2\,\frac{1-4^{n+1}}{1-4}$$

2. $\displaystyle S_2=\sum_{k=0}^{n}\frac{(-1)^k}{2^k}\binom nk$

   $$S_2=\sum_{k=0}^{n}\binom nk\left(\frac{-1}2\right)^k=\sum_{k=0}^{n}\binom nk\left(\frac{-1}2\right)^k1^{n-k}=\left(1+\frac{-1}2\right)^n=\frac1{2^n}$$

3. $\displaystyle P=\prod_{k=2}^{n}2\,\frac{k^2-2k+1}{k^2}$

   $$P=\prod_{k=2}^{n}2\,\frac{k^2-2k+1}{k^2}=\left(\prod_{k=2}^{n}2\right)\left(\prod_{k=2}^{n}\frac{k^2-2k+1}{k^2}\right)=2^{n-2+1}\left(\prod_{k=2}^{n}\frac{(k-1)^2}{k^2}\right)$$

   $$P=2^{n-1}\,\frac{(2-1)^2}{n^2}=\frac{2^{n-1}}{n^2}$$

## Exercice 5

**Pour les deux ensembles qui suivent, on vous demande de préciser si l’ensemble est majoré, minoré, de déterminer, si elles existent les bornes supérieures et inférieures ainsi que le plus grand et le plus petit élément.**

1. $A=\left\{x\in\mathbb R,\ \begin{cases}|x-2|<2\\ x^2-3x+2\geqslant0\end{cases}\right\}$.

   $$\begin{cases}|x-2|<2\\ x^2-3x+2\geqslant0\end{cases}\iff\begin{cases}0<x<4\\ x\leqslant1\ \text{ou}\ x\geqslant2\end{cases}$$

   Donc $A=]0,1]\cup[2,4[$.
   $\operatorname{Inf}(A)=0$ et $\operatorname{Sup}(A)=4$.
   Pas de Min ni de Max.

2. $B=\left\{\dfrac{2^n}{2^n-1},\ n\in\mathbb N^*\right\}$.

   - $\dfrac{2^n}{2^n-1}=1+\dfrac1{2^n-1}>1$ et $2^n-1\geqslant1\implies\dfrac1{2^n-1}\leqslant1\implies1+\dfrac1{2^n-1}\leqslant2$.
     $B$ est minorée par $1$ et majorée par $2$.
   - $2\in B\implies2=\operatorname{Max}(B)=\operatorname{Sup}(B)$.
   - $\forall\epsilon>0,\ \exists n\in\mathbb N^*,\ 2^n-1>\dfrac1\epsilon\implies\dfrac1{2^n-1}<\epsilon\implies1+\dfrac1{2^n-1}<1+\epsilon$.
     Donc $\forall\epsilon>0,\ \exists x\in B,\ x<1+\epsilon$.
   - $1=\operatorname{Inf}(B)$ et $1\notin B\implies\operatorname{Min}(B)$ n’existe pas.

## Exercice 6

**Soient $A$ et $B$ deux parties bornées de $\mathbb R$. Démontrer les propositions suivantes :**

1. **$A\subset B\implies\operatorname{Sup}(A)\leqslant\operatorname{Sup}(B)$.**

   $\forall x\in A,\ x\in B\implies\forall x\in A,\ x\leqslant\operatorname{Sup}(B)\implies\operatorname{Sup}(B)$ est un majorant de $A$.
   Donc $\operatorname{Sup}(A)\leqslant\operatorname{Sup}(B)$.

2. **$\operatorname{Sup}(A\cup B)=\operatorname{Max}(\operatorname{Sup}(A),\operatorname{Sup}(B))$.**

   - $\forall x\in A\cup B,\ x\in A$ ou $x\in B\implies\forall x\in A\cup B,\ x\leqslant\operatorname{Sup}(A)$ ou $x\leqslant\operatorname{Sup}(B)$
     $\implies\forall x\in A\cup B,\ x\leqslant\operatorname{Max}(\operatorname{Sup}(A),\operatorname{Sup}(B))$.
     $\operatorname{Max}(\operatorname{Sup}(A),\operatorname{Sup}(B))$ est donc un majorant de $A\cup B$, par conséquent :
     $$\operatorname{Sup}(A\cup B)\leqslant\operatorname{Max}(\operatorname{Sup}(A),\operatorname{Sup}(B))$$
   - D’un autre côté, en utilisant la première question, on peut dire :
     $A\subset A\cup B\implies\operatorname{Sup}(A)\leqslant\operatorname{Sup}(A\cup B)$
     $B\subset A\cup B\implies\operatorname{Sup}(B)\leqslant\operatorname{Sup}(A\cup B)$, et par suite :
     $$\operatorname{Max}(\operatorname{Sup}(A),\operatorname{Sup}(B))\leqslant\operatorname{Sup}(A\cup B)$$
     d’où l’égalité souhaitée.
