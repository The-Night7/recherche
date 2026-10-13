# Analyse 1 — DS3 2020–2021, corrigé

> Source : `PREING1-S1/Analyse1-DS/DS3-2020-2021_Analyse1-DS_P1S1_DMaths.pdf`, 4 pages (document dactylographié).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. Le document est intitulé « Corrigé du DS 3 ». Dans la source, les énoncés sont en noir et les réponses en rouge (quelques passages en bleu). Ici, les énoncés sont en **gras** et les réponses en texte courant.
> Vérification : les calculs ont été refaits. Anomalies de la source, signalées et non corrigées dans le texte :
> - réponse 5 : la conclusion $\alpha_n<\alpha_{n+1}$ découle de la stricte croissance de $f_{n+1}$, et non de $f_n$ comme l’écrit la source ;
> - les limites de suites sont notées $\lim_{x\to+\infty}$ au lieu de $\lim_{n\to+\infty}$ ;
> - la dernière réponse est numérotée « 7 » au lieu de « 10 ».

## 1. Exercice 1

**Calculer les limites suivantes :**

1. $\displaystyle\lim_{x\to0^+}\frac{\sqrt x-x}{\sqrt x+x}$.
2. $\displaystyle\lim_{x\to2}\frac{x^2-4}{x^2-3x+2}$.
3. $\displaystyle\lim_{x\to0^+}\frac xaE\left(\frac bx\right)$.
   **Où $a,b$ sont des réels strictement positifs et $E(x)$ désigne la partie entière de $x$.**

**Réponses :**

**1.**

$$\frac{\sqrt x-x}{\sqrt x+x}=\frac{\sqrt x\left(1-\frac x{\sqrt x}\right)}{\sqrt x\left(1+\frac x{\sqrt x}\right)}=\frac{1-\sqrt x}{1+\sqrt x}\qquad\text{car }\frac x{\sqrt x}=\sqrt x.$$

On en déduit : $\displaystyle\lim_{x\to0^+}\frac{\sqrt x-x}{\sqrt x+x}=\lim_{x\to0^+}\frac{1-\sqrt x}{1+\sqrt x}=1$.

**2.**

$$\frac{x^2-4}{x^2-3x+2}=\frac{(x-2)(x+2)}{(x-2)(x-1)}=\frac{x+2}{x-1}.$$

D’où : $\displaystyle\lim_{x\to2}\frac{x^2-4}{x^2-3x+2}=\lim_{x\to2}\frac{x+2}{x-1}=4$.

**3.** On sait que pour tout réel $y$, on a l’encadrement : $y-1<E(y)\leqslant y$.

Appliqué à $y=\dfrac bx$, on obtient : $\dfrac bx-1<E\left(\dfrac bx\right)\leqslant\dfrac bx$.

Puis :

$$\frac xa\left(\frac bx-1\right)<\frac xaE\left(\frac bx\right)\leqslant\frac xa\,\frac bx\implies\frac ba-\frac xa<\frac xaE\left(\frac bx\right)\leqslant\frac ba.$$

Comme $\displaystyle\lim_{x\to0^+}\frac xa=0$, le théorème des gendarmes permet de conclure :

$$\lim_{x\to0^+}\frac xaE\left(\frac bx\right)=\frac ba.$$

## 2. Exercice 2

1. **Donner la définition exacte, avec les quantificateurs, des propositions suivantes :**
   1. **a) $\displaystyle\lim_{x\to a}f(x)=\ell$.**
   2. **b) $\displaystyle\lim_{x\to-\infty}f(x)=+\infty$.**
2. **Utiliser la définition exacte (avec les quantificateurs) pour prouver que :**
   $$\lim_{x\to1}\frac{3x+1}{x+1}=2.$$

**Réponses :**

**1. a)** $\displaystyle\lim_{x\to a}f(x)=\ell\iff\forall\epsilon>0,\ \exists\alpha>0,\ \forall x\in D_f,\ |x-a|<\alpha\implies|f(x)-\ell|<\epsilon$.

**b)** $\displaystyle\lim_{x\to-\infty}f(x)=+\infty\iff\forall A>0,\ \exists B<0,\ \forall x\in D_f,\ x<B\implies f(x)>A$.

**2.** Soit $\epsilon>0$, on cherche un réel $\alpha>0$ tel que
$\forall x\in D_f,\ |x-1|<\alpha\implies|f(x)-2|<\epsilon$.

$$|f(x)-2|<\epsilon\iff\left|\frac{3x+1}{x+1}-2\right|<\epsilon\iff\frac{|x-1|}{|x+1|}<\epsilon.$$

Comme nous cherchons la limite en $1$, nous pouvons supposer $x>0$, ce qui nous donne :

$$x>0\implies x+1>1\implies\frac1{x+1}<1\implies\frac{|x-1|}{x+1}<|x-1|.$$

Pour avoir : $\dfrac{|x-1|}{|x+1|}<\epsilon$, il suffit donc d’avoir : $|x-1|<\epsilon$.
Nous pouvons donc choisir $\alpha=\epsilon$.

En effet : $\forall x>0,\ |x-1|<\epsilon\implies\dfrac{|x-1|}{x+1}<|x-1|<\epsilon\implies|f(x)-2|<\epsilon$.

## 3. Problème

**Pour tout entier $n\in\mathbb N$, on considère la fonction $f_n:[0,1]\to\mathbb R$ définie par :**

$$\forall x\in[0,1],\qquad f_n(x)=x^n-(1-x)^2.$$

**Première partie :**

**On considère, dans cette question, un entier $n\in\mathbb N^*$ fixé.**

1. **Montrer que la fonction $f_n$ est strictement croissante sur $[0,1]$.**
2. **Démontrer qu’il existe un unique réel $\alpha_n\in]0,1[$ tel que $f_n(\alpha_n)=0$.**
   **On pourra, éventuellement dresser le tableau de variation de $f_n$ sur $[0,1]$.**
3. **Déterminer la valeur de $\alpha_1$, solution de $f_1(x)=0$.**

**Deuxième partie :**

**On considère maintenant la suite obtenue dans la question précédente $(\alpha_n)_{n\in\mathbb N^*}$.**
**Autrement dit : $(\alpha_n)_{n\in\mathbb N^*}$ est la suite d’éléments de $]0,1[$ obtenus de la manière suivante :**

$$\begin{aligned}
&\alpha_1,\ \text{solution de } f_1(x)=0\iff f_1(\alpha_1)=0\iff\alpha_1-(1-\alpha_1)^2=0,\\
&\alpha_2,\ \text{solution de } f_2(x)=0\iff f_2(\alpha_2)=0\iff\alpha_2^2-(1-\alpha_2)^2=0,\\
&\dots\\
&\alpha_n,\ \text{solution de } f_n(x)=0\iff f_n(\alpha_n)=0\iff\alpha_n^n-(1-\alpha_n)^2=0.\\
&\dots
\end{aligned}$$

4. **Écrire sous forme simple factorisée $f_{n+1}(\alpha_n)-f_n(\alpha_n)$ et en déduire le signe de cette différence.**
   **Rappel : $\alpha_n\in]0,1[$.**
5. **En déduire le signe de $f_{n+1}(\alpha_n)$, puis que la suite $(\alpha_n)_{n\in\mathbb N^*}$ est croissante.**
6. **Justifier la convergence de cette suite.**

**Troisième partie :**

**On note $\ell$ la limite de cette suite : $\displaystyle\lim_{x\to+\infty}\alpha_n=\ell$.**

7. **Montrer que l’on a forcément : $\ell>0$.**
8. **Si on suppose que $0<\ell<1$, montrer que l’on a : $\displaystyle\lim_{x\to+\infty}\alpha_n^n=0$.**
   **On pourra utiliser la forme exponentielle d’une puissance.**
9. **À l’aide de la relation $f_n(\alpha_n)$, montrer que, dans ce cas, on a : $(1-\ell)^2=0$.**
   **N’y a-t-il pas une contradiction ?**
10. **Conclure quant à la seule valeur possible de $\ell$.**

**Réponses :**

**Première partie :**

**1.** $f_n(x)=x^n-(1-x)^2=x^n-\left(1-2x+x^2\right)=x^n-x^2+2x-1$.

$f_n'(x)=nx^{n-1}-2x+2=nx^{n-1}-2(x-1)=nx^{n-1}+2(1-x)$.

Sur $[0,1[$ on a : $nx^{n-1}\geqslant0$ et $2(1-x)>0$.
Donc $f_n'(x)>0$ et par suite $f_n$ strictement croissante.

**2.** $f_n(0)=-1<0$ et $f_n(1)=1>0$.
Le théorème des valeurs intermédiaires et la croissance stricte de $f_n$ permettent de conclure :

$$\exists!\,\alpha_n\in]0,1[\ \text{tel que}\ f_n(\alpha_n)=0.$$

**3.** $\alpha_1$ est solution de l’équation : $f_1(x)=0\iff x-(1-x)^2=0\iff-x^2+3x-1=0$.

$\Delta=9-4=5$, ce qui donne deux solutions : $x_1=\dfrac{-3-\sqrt5}{-2}=\dfrac{3+\sqrt5}2>1$,
et $x_2=\dfrac{3-\sqrt5}2\simeq0{,}38$. Donc $\alpha_1=\dfrac{3-\sqrt5}2$.

**Deuxième partie :**

**4.** On a : $f_{n+1}(\alpha_n)-f_n(\alpha_n)=\alpha_n^{n+1}-(1-\alpha_n)^2-\left(\alpha_n^n-(1-\alpha_n)^2\right)$.
Puis : $f_{n+1}(\alpha_n)-f_n(\alpha_n)=\alpha_n^{n+1}-\alpha_n^n=\alpha_n^n(\alpha_n-1)$.
Comme on sait que $\alpha_n\in]0,1[$, on a $\alpha_n^n>0$ et $\alpha_n-1<0$.
Par conséquent : $f_{n+1}(\alpha_n)-f_n(\alpha_n)<0$.

**5.** Comme, par définition, $f_n(\alpha_n)=0$, on en déduit : $f_{n+1}(\alpha_n)<0$.
Nous avons donc, d’une part : $f_{n+1}(\alpha_n)<0$, et d’autre part : $f_{n+1}(\alpha_{n+1})=0$.
Comme $f_n$ est strictement croissante, on en déduit : $\alpha_n<\alpha_{n+1}$.
La suite est croissante (et même strictement croissante).

**6.** $(\alpha_n)_{n\in\mathbb N}$ est croissante et majorée par $1$, donc convergente vers un réel $\ell$.
De plus : $\alpha_n\in]0,1[\implies\displaystyle\lim_{x\to+\infty}\alpha_n=\ell\in[0,1]$.

**Troisième partie :**

**7.** $(\alpha_n)_{n\in\mathbb N}$ est croissante et $\alpha_1=\dfrac{3-\sqrt5}2>0$ ; on a donc forcément : $\ell>0$.

**8.** Si on suppose que $0<\ell<1$, alors comme $\alpha_n^n=e^{n\ln(\alpha_n)}$ et que $\ln(\ell)<0$, on aura :

$$\lim_{x\to+\infty}n\ln(\alpha_n)=-\infty\implies\lim_{x\to+\infty}\alpha_n^n=0.$$

**9.** Par construction de la suite, on a : $f_n(\alpha_n)=0\iff\alpha_n^n-(1-\alpha_n)^2=0$.
En passant à la limite, on obtient donc : $0-(1-\ell)^2=0\implies\ell=1$.
D’où la contradiction.

**7.** *(sic, pour 10)* On sait que $\ell\in]0,1]$ et que $0<\ell<1$ est impossible, par conséquent : $\ell=1$.
