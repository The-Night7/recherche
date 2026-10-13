# Analyse 1 — DS 2020–2021 (fichier « DS1 »), sujet et corrigé

> Source : `PREING1-S1/Analyse1-DS/DS1-2020-2021_Analyse1-DS_P1S1_DMaths.pdf`, 4 pages (document dactylographié).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. **Écart de nommage :** le document est intitulé « DS 4 » alors que le fichier est nommé DS1 ; le nom du fichier est conservé pour la traçabilité. Le document réunit énoncés (en noir) et corrections (en rouge) : ici, chaque correction suit l’en-tête « Correction ». Le barème totalise 20 points.
> Vérification : les calculs ont été refaits ; aucune erreur de résultat n’a été relevée. Dans l’exercice 2 (c), la source applique le TVI sur $]a,b[$ sans préciser que $a$ est choisi inférieur à $b$. C’est toujours possible, puisque $a$ peut être pris arbitrairement près de $0$. L’abréviation « strictt » (strictement) de la source est conservée.

## Exercice 1 (3 pts)

Soit $f$ la fonction définie sur $[1,5[\cup]5,+\infty[$ par :

$$f(x)=\frac{\sqrt{x-1}-2}{x-5}$$

1. Montrer que l’on peut prolonger $f$ par continuité en $5$, en posant : $f(5)=\frac14$.
2. Déterminer, si elle existe, la dérivée de $f$ en $5$, c’est-à-dire $f'(5)$.

**Correction :**

**1.**

$$f(x)=\frac{\sqrt{x-1}-2}{x-5}=\frac{\left(\sqrt{x-1}-2\right)\left(\sqrt{x-1}+2\right)}{(x-5)\left(\sqrt{x-1}+2\right)}=\frac{(x-1-4)}{(x-5)\left(\sqrt{x-1}+2\right)}=\frac1{\left(\sqrt{x-1}+2\right)}.$$

On en déduit : $\displaystyle\lim_{x\to5}f(x)=\lim_{x\to5}\frac1{\sqrt{x-1}+2}=\frac14$.

On peut donc prolonger $f$ par continuité en $5$ en posant : $f(5)=\frac14$.

**2.**

$$\frac{f(x)-f(5)}{x-5}=\frac{\frac1{\sqrt{x-1}+2}-\frac14}{x-5}=\frac{\frac{4-\left(\sqrt{x-1}+2\right)}{4\left(\sqrt{x-1}+2\right)}}{x-5}=\frac{\frac{2-\sqrt{x-1}}{4\left(\sqrt{x-1}+2\right)}}{x-5}=\frac{2-\sqrt{x-1}}{4\left(\sqrt{x-1}+2\right)(x-5)}$$

$$\frac{f(x)-f(5)}{x-5}=\frac{-\left(\sqrt{x-1}-2\right)}{4\left(\sqrt{x-1}+2\right)(x-5)}=\frac{-1}{4\left(\sqrt{x-1}+2\right)}\times\frac{\left(\sqrt{x-1}-2\right)}{(x-5)}=\frac{-1}{4\left(\sqrt{x-1}+2\right)}\times f(x)$$

$$\frac{f(x)-f(5)}{x-5}=\frac{-1}{4\left(\sqrt{x-1}+2\right)}\times\frac1{\left(\sqrt{x-1}+2\right)}.$$

Par suite :

$$\lim_{x\to5}\frac{f(x)-f(5)}{x-5}=\lim_{x\to5}\frac{-1}{4\left(\sqrt{x-1}+2\right)}\times\frac1{\left(\sqrt{x-1}+2\right)}=\frac{-1}{4\times4\times4}=\frac{-1}{64}.$$

Conclusion : $f$ est dérivable en $5$ et $f'(5)=\dfrac{-1}{64}$.

## Exercice 2 (4,5 pt)

1. Énoncer le théorème des valeurs intermédiaires pour une fonction $f$ continue sur un intervalle $I$.
2. Soit $f:\mathbb R^+\to\mathbb R^+$ une fonction continue.
   On suppose que : $\displaystyle\lim_{x\to+\infty}\frac{f(x)}x=\ell<1$ et on veut montrer que $f$ possède un point fixe, c’est-à-dire : $\exists c\in\mathbb R^+,\quad f(c)=c$.
   1. a) Supposer $f(0)=0$, conclure.
   2. b) Justifier l’existence de $b\in\mathbb R^+,\ \dfrac{f(b)}b<1$.
   3. c) Supposer $f(0)\neq0$, calculer $\displaystyle\lim_{x\to0^+}\frac{f(x)}x$, puis conclure.

**Correction :**

**1.** Voir cours.

**2. (a)** $f(0)=0\implies$ on peut prendre $c=0$.

**(b)** $\displaystyle\lim_{x\to+\infty}\frac{f(x)}x=\ell<1\iff\forall\epsilon>0,\ \exists A>0,\ \forall x>A,\ \left|f(x)-\ell\right|<\epsilon$.

> Note : la source écrit $|f(x)-\ell|$ là où l’on attend $\left|\frac{f(x)}x-\ell\right|$ ; la suite du raisonnement utilise bien $\frac{f(b)}b$.

Il suffit alors de choisir $\epsilon=\dfrac{1-\ell}2$ et de prendre $b=A+1$, pour avoir : $\dfrac{f(b)}b<\ell+\epsilon=\dfrac{1+\ell}2<1$.

**(c)** Si $f(0)\neq0$, alors $f(0)>0$ car $f:\mathbb R^+\to\mathbb R^+$.

Par conséquent : $\displaystyle\lim_{x\to0^+}\frac{f(x)}x=+\infty$.

On peut donc trouver $a$ au voisinage de $0$ tel que $\dfrac{f(a)}a>1$.
Il suffit pour cela de choisir $A=1$ dans la définition de la limite et de prendre $a\in]0,\alpha[$ avec $\alpha$ donné par cette limite.

Nous avons donc : $g:x\mapsto\dfrac{f(x)}x$ définie et continue sur $]0,+\infty[$ avec $g(a)>1$ et $g(b)<1$.
Le TVI, appliqué à $g$, implique $\exists c\in]a,b[,\quad g(c)=1\iff f(c)=c$.

## Exercice 3 (4 pts)

Soit $f:]a,b[\to\mathbb R$ une fonction continue telle que : $\displaystyle\lim_{x\to a}f(x)=\ell_1\in\mathbb R$ et $\displaystyle\lim_{x\to b}f(x)=\ell_2\in\mathbb R$.

1. Montrer que $f$ est bornée.
2. $f$ possède-t-elle forcément un maximum ? un minimum ?

**Correction :**

**1.** $\displaystyle\lim_{x\to a}f(x)=\ell_1\iff\forall\epsilon>0,\ \exists\alpha>0,\ \forall x\in]a,b[,\ |x-a|<\alpha\implies|f(x)-\ell_1|<\epsilon$.

Nous pouvons donc borner $f$ par $\ell_1-\epsilon$ et $\ell_1+\epsilon$ sur l’intervalle $]a,a+\alpha[$ (par exemple avec $\epsilon=1$).
De la même manière, nous pouvons borner $f$ par $\ell_2-\epsilon$ et $\ell_2+\epsilon$ sur l’intervalle $]b-\alpha,b[$.
Il restera, peut-être, un intervalle $[a+\alpha,b-\alpha]$ qui est un segment, et sur lequel $f$ est également bornée par le théorème sur l’image d’un segment par une fonction continue.
Finalement, $f$ est bornée sur $]a,a+\alpha[$, sur $[a+\alpha,b-\alpha]$ et sur $]b-\alpha,b[$.
Conclusion : $f$ est bornée sur $]a,b[$.

**2.** $f$ ne possède pas forcément de $\operatorname{Min}$ ni de $\operatorname{Max}$.
Prenons, par exemple, $f(x)=x$ et $]a,b[=]0,1[$. $f$ vérifie bien toutes les hypothèses de la question 1. Mais elle ne possède ni $\operatorname{Min}$ ni $\operatorname{Max}$.
En effet, $\operatorname{Inf}f(x)=0$ et $\operatorname{Sup}f(x)=1$, mais ni $0$, ni $1$ ne sont des valeurs prises sur $]0,1[$.

## Exercice 4 (5,5 pt)

On considère la fonction $f$ définie sur $\mathbb R$ par :

$$f(x)=\begin{cases}\ln\left(\dfrac1e-x\right) & \text{si } x<0\\[4pt] -x^2-2x-1 & \text{si } x\geqslant0\end{cases}$$

1. Montrer que $f$ est continue et strictement décroissante sur $\mathbb R$.
2. Justifier l’existence et la continuité de $f^{-1}$ et préciser son sens de variations.
3. Déterminer l’expression détaillée de $f^{-1}(x)$ pour tout réel $x$.

**Correction :**

**1.** $f$ est continue pour $x<0$ car composée de fonctions continues et strictement décroissante car composée d’une strictt croissante ($\ln$) et d’une strictt décroissante.
Pour $x\geqslant0$, $f$ est continue comme polynôme et strictt décroissante car ce trinôme l’est pour $x\geqslant-1$.
De plus $\displaystyle\lim_{x\to0^-}f(x)=-1=\lim_{x\to0^+}f(x)\implies f$ continue sur $\mathbb R$ et strictt décroissante.

**2.** $f$ continue et strictt décroissante réalise donc une bijection de $\mathbb R$ vers $f(\mathbb R)=\mathbb R$.
En effet : $\displaystyle\lim_{x\to-\infty}f(x)=+\infty$ et $\displaystyle\lim_{x\to+\infty}f(x)=-\infty$.
$f$ possède donc une réciproque : $f^{-1}:\mathbb R\to\mathbb R$.
De plus $f^{-1}$ a le même sens de variations que $f$ donc strictt décroissante.

**3.** On sait que : $f(]-\infty,0[)=]-1,+\infty[$ et que $f([0,+\infty[)=]-\infty,-1]$.

- Si $y\in]-1,+\infty[$, $y=f(x)\iff y=\ln\left(\dfrac1e-x\right)\iff x=\dfrac1e-e^y=f^{-1}(y)$.
- Si $y\in]-\infty,-1]$, $y=f(x)\iff y=-x^2-2x-1\iff y=-(x+1)^2$
  $\iff x+1=\pm\sqrt{-y}\iff x=-1+\sqrt{-y}=f^{-1}(y)$.

Finalement :

$$f^{-1}(x)=\begin{cases}-1+\sqrt{-x} & \text{si } x\leqslant-1\\[4pt] \dfrac1e-e^x & \text{si } x>-1\end{cases}$$

## Exercice 5 (3 pts)

On considère la fonction : $f:]0,+\infty[\to\mathbb R$, définie par : $f(x)=\dfrac{e^x}{x^e}$.

1. Étudier les variations de $f$.
2. Comparer, sans calculatrice, les nombres $e^\pi$ et $\pi^e$.

**Correction :**

**1.** $f(x)=\dfrac{e^x}{x^e}$ fonction continue et dérivable sur $]0,+\infty[$.

$$f'(x)=\frac{x^ee^x-ex^{e-1}e^x}{\left(x^e\right)^2}=\frac{x^{e-1}e^x(x-e)}{\left(x^e\right)^2}.$$

$f'$ a le même signe que $(x-e)$, donc négatif sur $]0,e]$ et positif sur $[e,+\infty[$.
$f$ possède donc un minimum en $x=e$ et ce minimum vaut $f(e)=1$.

**2.** On a vu que : $\forall x\in]0,+\infty[,\quad f(x)\geqslant f(e)=1$.
En particulier, pour $x=\pi$, on a :

$$f(\pi)\geqslant1\iff\frac{e^\pi}{\pi^e}\geqslant1\iff e^\pi\geqslant\pi^e.$$
