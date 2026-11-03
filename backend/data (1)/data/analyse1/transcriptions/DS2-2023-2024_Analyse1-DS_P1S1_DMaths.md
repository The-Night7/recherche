# Analyse 1 — DS2 2023–2024, sujet corrigé (12 décembre 2023)

> Source : `PREING1-S1/Analyse1-DS/DS2-2023-2024_Analyse1-DS_P1S1_DMaths.pdf`, 5 pages (PDF natif).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. Le sujet (énoncés en noir) est celui du fichier [DS1-2023-2024-V2](DS1-2023-2024-V2_Analyse1-DS_P1S1_DMaths.md) ; les solutions sont en rouge dans la source. Ici, les énoncés sont en **gras** et les solutions en texte courant.
> Vérification : les calculs ont été refaits. Erreurs de la source, signalées et non corrigées dans le texte :
> - **Exercice 4.3** : les lignes intermédiaires sont fausses. $4-\frac{18}{2x+12}=x$ équivaut à $2x^2+4x-30=0$, soit $x^2+2x-15=0$, et non à $2x^2-8x-30=0$ ou $x^2-4x-15=0$, dont les racines seraient $2\pm\sqrt{19}$. Les racines annoncées, $3$ et $-5$, sont celles de l’équation correcte : la conclusion est juste.
> - **Exercice 2.2** : la définition est écrite avec $m<0$, mais la rédaction commence par « Soit $M>0$ » puis utilise $m$ ; il faut lire « Soit $m<0$ ».
> - **Exercice 2.1** : le choix $N=E\left(\left(\frac5\epsilon-1\right)^{1/3}\right)+1$ suppose $\epsilon\le5$. Pour $\epsilon>5$, n’importe quel $N$ convient.
> - Coquilles conservées : « théoème », « décroissante est minorée », « toute couple ». La source écrit « $2x6+12$ » ; la transcription restitue $2\times6+12$.

**Préing 1 — Devoir Surveillé 2 — Analyse I**

| Date | Durée | Nombre de pages |
| --- | --- | --- |
| 12/12/2023 | 1 h 00 | 2 |

L’usage de tout appareil électronique est interdit.

**Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.** *Le sujet comporte 4 exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.*

## Exercice 1 (6 points)

**Déterminer, si elle existe, la limite de chacune des suites suivantes. Sinon, justifier pourquoi il n’y a pas de limite.**

### 1. $\forall n\in\mathbb N,\ u_n=\sqrt{n^4+3n^2}-\sqrt{n^4+n-1}$.

**Solution :** Nous avons

$$\begin{aligned}
\sqrt{n^4+3n^2}-\sqrt{n^4+n-1}&=\sqrt{n^4+3n^2}-\sqrt{n^4+n-1}\cdot\frac{\sqrt{n^4+3n^2}+\sqrt{n^4+n-1}}{\sqrt{n^4+3n^2}+\sqrt{n^4+n-1}}\\
&=\frac{n^4+3n^2-n^4-n+1}{\sqrt{n^4+3n^2}+\sqrt{n^4+n-1}}\\
&=\frac{3n^2-n+1}{n^2\sqrt{1+\frac3{n^2}}+n^2\sqrt{1+\frac1{n^3}-\frac1{n^4}}}\\
&=\frac{3-\frac1n+\frac1{n^2}}{\sqrt{1+\frac3{n^2}}+\sqrt{1+\frac1{n^3}-\frac1{n^4}}}
\end{aligned}$$

Ainsi

$$\lim_{n\to+\infty}u_n=\lim_{n\to+\infty}\frac{3-\frac1n+\frac1{n^2}}{\sqrt{1+\frac3{n^2}}+\sqrt{1+\frac1{n^3}-\frac1{n^4}}}=\frac32.$$

> La première ligne omet les parenthèses autour de $\sqrt{n^4+3n^2}-\sqrt{n^4+n-1}$ devant le facteur conjugué ; la suite du calcul est correcte.

### 2. $\forall n\in\mathbb N^*,\ v_n=\dfrac{E(\ln(n))}{n}$.

**Solution :** Pour tout $n\in\mathbb N^*$, nous avons

$$\ln(n)-1\le E(\ln(n))\le\ln(n)\quad\implies\quad\frac{\ln(n)-1}n\le\frac{E(\ln(n))}n\le\frac{\ln(n)}n$$

Ainsi, d’après le théorème d’encadrement, nous pouvons conclure

$$0=\lim_{n\to+\infty}\frac{\ln(n)-1}n\le\lim_{n\to+\infty}\frac{E(\ln(n))}n\le\lim_{n\to+\infty}\frac{\ln(n)}n=0.$$

Par conséquent,

$$\lim_{n\to+\infty}\frac{E(\ln(n))}n=0.$$

### 3. $\forall n\in\mathbb N,\ z_n=\dfrac{(-1)^nn^2+n^3}{1+3n^3}+i\cdot\dfrac{n^2+2n}{3n^2+2i}$.

**Solution :** Pour tout $n\in\mathbb N^*$, nous avons

$$\begin{aligned}
\frac{(-1)^nn^2+n^3}{1+3n^3}+i\cdot\frac{n^2+2n}{3n^2+2i}&=\frac{(-1)^nn^2+n^3}{1+3n^3}+i\cdot\frac{n^2+2n}{3n^2+2i}\cdot\frac{3n^2-2i}{3n^2-2i}\\
&=\frac{(-1)^nn^2+n^3}{1+3n^3}+i\cdot\frac{3n^4+6n^3-2in^2-4in}{9n^4+4}\\
&=\frac{(-1)^nn^2+n^3}{1+3n^3}+\frac{2n^2+4n}{9n^4+4}+i\cdot\frac{3n^4+6n^3}{9n^4+4}\\
&=\frac{\frac{(-1)^n}n+1}{\frac1{n^3}+3}+\frac{\frac2{n^2}+\frac4{n^3}}{9+\frac4{n^4}}+i\cdot\frac{3+6\frac1n}{9+\frac4{n^4}}
\end{aligned}$$

Ainsi

$$\lim_{n\to+\infty}z_n=\lim_{n\to+\infty}\frac{\frac{(-1)^n}n+1}{\frac1{n^3}+3}+\frac{\frac2{n^2}+\frac4{n^3}}{9+\frac4{n^4}}+i\cdot\frac{3+6\frac1n}{9+\frac4{n^4}}=\frac13+i\frac13.$$

## Exercice 2 (4 points)

**Montrer, en revenant à la définition de la limite, que :**

### 1. $\displaystyle\lim_{n\to+\infty}u_n=2$, pour $u_n=\dfrac{2n^3-3}{n^3+1}$.

**Solution :** Soit $\epsilon>0$, on cherche $N\in\mathbb N^*$, tel que

$$\forall n\ge N,\quad|u_n-2|<\epsilon.$$

C’est-à-dire, on cherche $N\in\mathbb N$, tel que

$$\begin{aligned}
\forall n\ge N,\ \left|\frac{2n^3-3}{n^3+1}-2\right|<\epsilon&\iff\forall n\ge N,\ \left|\frac{2n^3-3}{n^3+1}-\frac{2(n^3+1)}{n^3+1}\right|<\epsilon\\
&\iff\forall n\ge N,\ \left|\frac{2n^3-3-2n^3-2}{n^3+1}\right|<\epsilon\\
&\iff\forall n\ge N,\ \frac5{n^3+1}<\epsilon.
\end{aligned}$$

Sachant que

$$\frac5{n^3+1}<\epsilon\iff\frac5\epsilon<n^3+1\iff\frac5\epsilon-1<n^3\iff\left(\frac5\epsilon-1\right)^{\frac13}<n,$$

il suffit de poser

$$N=E\left(\left(\frac5\epsilon-1\right)^{\frac13}\right)+1.$$

Alors pour tout $n\ge N$, nous avons

$$n\ge N>\left(\frac5\epsilon-1\right)^{\frac13}\implies\left|\frac{2n^3-3}{n^3+1}-2\right|<\epsilon.$$

### 2. $\displaystyle\lim_{n\to+\infty}v_n=-\infty$, pour $v_n=-2\ln(3n+1)$.

**Solution :** On doit vérifier

$$\forall m<0,\ \exists N\in\mathbb N,\ \forall n\in\mathbb N,\quad(n\ge N\implies v_n<M).$$

Soit $M>0$, on cherche $N\in\mathbb N$, tel que

$$\forall n\ge N,\quad v_n<M.$$

C’est-à-dire, on cherche $N\in\mathbb N$, tel que pour tout $n>N$, nous avons

$$\begin{aligned}
-2\ln(3n+1)<m&\iff\ln(3n+1)>-\frac m2\\
&\iff3n+1>e^{-\frac m2}\\
&\iff n>\frac{e^{-\frac m2}-1}3
\end{aligned}$$

Ainsi, il suffit de poser

$$N=E\left(\frac{e^{-\frac m2}-1}3\right)+1,$$

pour conclure

$$n>N>\frac{e^{-\frac m2}-1}3\implies-2\ln(3n+1)<m$$

## Exercice 3 (4 points)

**Pour tout $n\in\mathbb N^*$, on pose**

$$a_n=\sum_{k=1}^{n}\frac1{k^3}\quad\text{et}\quad b_n=a_n+\frac1{n^2}.$$

### 1. Montrer que les suites $(a_n)_{n\in\mathbb N}$ et $(b_n)_{n\in\mathbb N}$ sont adjacentes.

**Solution :**

- Nous avons
  $$a_{n+1}-a_n=\sum_{k=1}^{n+1}\frac1{k^3}-\sum_{k=1}^{n}\frac1{k^3}=\frac1{(n+1)^3}>0.$$
  Donc $(a_n)$ est croissante.
- Nous avons
  $$\begin{aligned}
  b_{n+1}-b_n=a_{n+1}+\frac1{(n+1)^2}-a_n-\frac1{n^2}&=\frac1{(n+1)^3}+\frac1{(n+1)^2}-\frac1{n^2}\\
  &=\frac{n^2+(n+1)n^2-(n+1)^3}{(n+1)^3n^2}\\
  &=\frac{n^3+2n^2-n^3-3n^2-3n-1}{(n+1)^3n^2}\\
  &=\frac{-n^2-3n-1}{(n+1)^3n^2}<0.
  \end{aligned}$$
  Donc $(b_n)$ est décroissante.
- De plus
  $$b_n-a_n=a_n+\frac1{n^2}-a_n=\frac1{n^2}\implies\lim_{n\to+\infty}\frac1{n^2}=0.$$

Par conséquent, les suites $(a_n)_{n\in\mathbb N}$ et $(b_n)_{n\in\mathbb N}$ sont adjacentes.

### 2. En déduire la convergence des suites $(a_n)_{n\in\mathbb N}$ et $(b_n)_{n\in\mathbb N}$. Qu’est-ce qu’on peut dire à propos de la valeur de leur limite ?

**Solution :** D’après les théoème sur les suites adjacentes les suites $(a_n)_{n\in\mathbb N}$ et $(b_n)_{n\in\mathbb N}$ convergent vers la même limite.

## Exercice 4 (6 points)

**On considère la suite $(u_n)_{n\in\mathbb N}$ définie par récurrence de la manière suivante :**

$$u_0=6\quad\text{et}\quad u_{n+1}=4-\frac{18}{2u_n+12}.$$

**On se placera dans $I=[0,18]$. On pose**

$$f:I\longrightarrow\mathbb R,\qquad x\longmapsto4-\frac{18}{2x+12}.$$

### 1. Déterminer le sens de variation de la fonction $f$.

**Solution :** Pour toute couple $(x,y)\in\mathbb R^2$ avec $x<y$ nous avons

$$\begin{aligned}
x<y\implies2x+12<2y+12\implies\frac1{2y+12}<\frac1{2x+12}&\implies-\frac{18}{2x+12}<-\frac{18}{2y+12}\\
&\implies4-\frac{18}{2x+12}<4-\frac{18}{2y+12}.
\end{aligned}$$

Ainsi $f$ est strictement croissante.

### 2. Montrer que l’intervalle $I$ est stable par $f$.

**Solution :** Puisque $f$ est croissante, pour tout $x\in I$ nous avons

$$0\le x\le18\implies0<4-\frac{18}{12}=f(0)\le f(x)\le f(18)=4-\frac{18}{48}<18.$$

### 3. Déterminer le(s) point(s) fixe(s) de $f$ dans cet intervalle.

**Solution :** Nous avons

$$\begin{aligned}
f(x)=x&\iff4-\frac{18}{2x+12}=x\\
&\iff2x^2-8x-30=0\\
&\iff x^2-4x-15=0\\
&\iff x=3\ \text{ ou }\ x=-5.
\end{aligned}$$

Ainsi l’unique point fixe de $f$ dans $I$ est $3$.

> Erreur de la source : lire $2x^2+4x-30=0\iff x^2+2x-15=0$ (voir l’avertissement en tête).

### 4. Déterminer le sens de variation de la suite $(u_n)_{n\in\mathbb N}$.

**Solution :** Comme $f$ est croissante la suite $(u_n)$ est monotone. De plus

$$u_1=f(u_0)=4-\frac{18}{2\times6+12}<6=u_0.$$

Ainsi $u_n$ est décroissante.

### 5. Étudier la convergence de la suite $(u_n)_{n\in\mathbb N}$.

**Solution :** Puisque l’intervalle $I=[0,18]$ est stable par $f$ et $u_0=6\in I$, on conclut que

$$\forall n,\ u_n=f(u_{n-1})\in I.$$

La suite $(u_n)_{n\in\mathbb N}$ est donc décroissante est minorée, donc convergente. De plus, sa limite est un **point fixe** de $f$ dans $I$. Or l’unique point fixe de $f$ dans $I$ est $3$. Ainsi

$$\lim_{n\to+\infty}u_n=3.$$
