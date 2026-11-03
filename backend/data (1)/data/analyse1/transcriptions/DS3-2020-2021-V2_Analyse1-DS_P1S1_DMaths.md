# Analyse 1 — DS3 2020–2021, corrigé (version 2)

> Source : `PREING1-S1/Analyse1-DS/DS3-2020-2021-V2_Analyse1-DS_P1S1_DMaths.pdf`, 3 pages (document dactylographié).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; formules restituées en LaTeX. Malgré son nom, le fichier est un **corrigé**, intitulé « Corrigé du DM 3 » (devoir maison et non devoir surveillé) ; le nom du fichier est conservé pour la traçabilité. Dans la source, les énoncés sont en noir et les réponses en rouge, avec quelques passages en bleu. Ici, les énoncés sont en **gras** et les réponses en texte courant. Les calculs ont été vérifiés. Seule anomalie : dans les réponses 5 et 6 du problème, la source écrit $\lim_{x\to+\infty}$ au lieu de $\lim_{n\to+\infty}$ ; la variable a été conservée et l’anomalie est signalée.

## 1. Exercice 1

**Calculer les limites suivantes :**

1. $\displaystyle\lim_{x\to+\infty}\sqrt{x^2+1}-x$.
2. $\displaystyle\lim_{x\to3}\frac{x^3-3^3}{x^5-3^5}$.
3. $\displaystyle\lim_{x\to+\infty}\frac{E(\sqrt x)}{x}$.
   **Où $E(\sqrt x)$ désigne la partie entière de $\sqrt x$.**

Réponses :

**1.**

$$\sqrt{x^2+1}-x=\frac{\left(\sqrt{x^2+1}-x\right)\left(\sqrt{x^2+1}+x\right)}{\sqrt{x^2+1}+x}=\frac{x^2+1-x^2}{\sqrt{x^2+1}+x}=\frac1{\sqrt{x^2+1}+x}.$$

$$\lim_{x\to+\infty}\sqrt{x^2+1}+x=+\infty\implies\lim_{x\to+\infty}\sqrt{x^2+1}-x=0.$$

**2.** On utilise l’identité remarquable : $(a^n-b^n)=(a-b)\left(a^{n-1}+a^{n-2}b+\dots+ab^{n-2}+b^{n-1}\right)$.

$$\frac{x^3-3^3}{x^5-3^5}=\frac{(x-3)(x^2+3x+3^2)}{(x-3)(x^4+3x^3+3^2x^2+3^3x+3^4)}=\frac{x^2+3x+9}{x^4+3x^3+9x^2+27x+81}.$$

On en déduit :

$$\lim_{x\to3}\frac{x^3-3^3}{x^5-3^5}=\frac{9+9+9}{81+81+81+81+81}=\frac{3\times9}{5\times81}=\frac1{15}.$$

**3.** On sait que $\forall y\in\mathbb R,\ E(y)\leqslant y$, et que $y\geqslant0\implies E(y)\geqslant0$.

On en déduit : $\forall x\in\mathbb R^+,\quad0\leqslant E\left(\sqrt x\right)\leqslant\sqrt x$.

Puis que :

$$0\leqslant\frac{E\left(\sqrt x\right)}{x}\leqslant\frac{\sqrt x}{x}=\frac1{\sqrt x}.$$

Finalement :

$$\lim_{x\to+\infty}\frac1{\sqrt x}=0\implies\lim_{x\to+\infty}\frac{E(\sqrt x)}{x}=0.$$

## 2. Exercice 2

1. **Donner la définition exacte, avec les quantificateurs, des propositions suivantes :**
   1. **a) $\displaystyle\lim_{x\to a}f(x)=-\infty$.**
   2. **b) $\displaystyle\lim_{x\to+\infty}f(x)=\ell\in\mathbb R$.**
2. **Utiliser la définition exacte (avec les quantificateurs) pour prouver que :**
   $$\lim_{x\to1}\frac{-3}{5(x-1)^2}=-\infty.$$

**Réponses :**

**1. a)** $\displaystyle\lim_{x\to a}f(x)=-\infty\iff\forall B<0,\ \exists\alpha>0,\ \forall x\in D_f,\ |x-a|<\alpha\implies f(x)<B$.

**b)** $\displaystyle\lim_{x\to+\infty}f(x)=\ell\iff\forall\epsilon>0,\ \exists A>0,\ \forall x\in D_f,\ x>A\implies|f(x)-\ell|<\epsilon$.

**2.** Soit $B<0$, on cherche un réel $\alpha>0$ tel que $\forall x\in D_f,\ |x-1|<\alpha\implies f(x)<B$.

$$f(x)<B\iff\frac{-3}{5(x-1)^2}<B\iff\frac{3}{5(x-1)^2}>-B>0$$

$$f(x)<B\iff\frac{5(x-1)^2}{3}<\frac1{-B}\iff(x-1)^2<\frac{3}{-5B}$$

$$f(x)<B\iff\sqrt{(x-1)^2}<\sqrt{\frac{-3}{5B}}\iff|x-1|<\sqrt{\frac{-3}{5B}}$$

Nous pouvons donc choisir $\alpha=\sqrt{\dfrac{-3}{5B}}$.

En effet : $\forall x\neq1,\ |x-1|<\sqrt{\dfrac{-3}{5B}}\implies(x-1)^2<\dfrac{3}{-5B}\implies f(x)<B$.

## 3. Problème

**Pour tout entier $n\in\mathbb N^*$, on considère la fonction $f_n:[0,+\infty[\to\mathbb R$ définie par :**

$$\forall x\in[0,+\infty[,\qquad f_n(x)=e^x+nx^2-3.$$

**On considère, dans cette question, un entier $n\in\mathbb N^*$ fixé.**

1. **Montrer que la fonction $f_n$ est strictement croissante.**
2. **Démontrer qu’il existe un unique réel $\alpha_n\in]0,1[$ tel que $f_n(\alpha_n)=0$.**
   **On pourra, éventuellement dresser le tableau de variation de $f_n$.**

**On considère maintenant la suite $(\alpha_n)_{n\in\mathbb N}$, d’éléments de $]0,1[$, définie dans la question précédente. On fixe un entier $n\in\mathbb N^*$.**

3. **Montrer que, pour un entier $n\in\mathbb N^*$, on a : $\forall x\in]0,1[,\quad f_{n+1}(x)-f_n(x)>0$.**
4. **En déduire le signe de $f_n(\alpha_{n+1})$, puis le sens de variations de la suite $(\alpha_n)_{n\in\mathbb N}$.**
   **Rappel : $f_{n+1}(\alpha_{n+1})=0$.**
5. **Justifier que la suite $(\alpha_n)_{n\in\mathbb N}$ est convergente vers un réel $\ell\in[0,1]$.**
6. **Si on suppose $\ell>0$, calculer la limite de : $e^{\alpha_n}+n(\alpha_n)^2-3$ et en déduire une contradiction.**
7. **Conclure quant à la seule valeur possible de $\ell$.**

**Réponses :**

**1.** $f_n(x)=e^x+nx^2-3$.
$f_n$ est une somme de fonctions strictement croissantes sur $[0,+\infty[$, donc elle est strictement croissante.
**Ou bien :** $f_n'(x)=e^x+2nx>0$ sur $[0,+\infty[$, donc elle est strictement croissante.

**2.** $f_n(0)=1-3=-2<0$ et $f_n(1)=e+n-3\geqslant e+1-3>0$ car $n\geqslant1$.
Le théorème des valeurs intermédiaires et la croissance stricte de $f_n$ permettent de conclure :

$$\exists!\,\alpha_n\in]0,1[\ \text{tel que}\ f_n(\alpha_n)=0.$$

**3.** $\forall x\in]0,1[,\quad f_{n+1}(x)-f_n(x)=e^x+(n+1)x^2-3-\left(e^x+nx^2-3\right)=x^2>0$.

**4.** En choisissant $x=\alpha_{n+1}$, on obtient : $f_{n+1}(\alpha_{n+1})-f_n(\alpha_{n+1})>0$.
Comme, par définition, $f_{n+1}(\alpha_{n+1})=0$, on en déduit : $f_n(\alpha_{n+1})<0$.

Nous avons donc, d’une part : $f_n(\alpha_{n+1})<0$, et d’autre part : $f_n(\alpha_n)=0$.
Comme $f_n$ est strictement croissante, on en déduit : $\alpha_{n+1}<\alpha_n$.
La suite est décroissante (et même strictement).

**5.** $(\alpha_n)_{n\in\mathbb N}$ est décroissante et minorée par $0$, donc convergente vers un réel $\ell$.
De plus : $\alpha_n\in]0,1[\implies\displaystyle\lim_{x\to+\infty}\alpha_n=\ell\in[0,1]$.

**6.** Si on suppose que $\ell>0$, alors : $\displaystyle\lim_{x\to+\infty}e^{\alpha_n}=e^\ell$.
De même $\displaystyle\lim_{x\to+\infty}n(\alpha_n)^2=+\infty\implies\lim_{x\to+\infty}\left(e^{\alpha_n}+n(\alpha_n)^2-3\right)=+\infty$.
Mais : $e^{\alpha_n}+n(\alpha_n)^2-3=f_n(\alpha_n)=0$ par construction même de la suite.
C’est une expression constante qui a donc pour limite $0$.
D’où la contradiction.

**7.** On sait que $\ell\in[0,1]$ et que $\ell>0$ est impossible, par conséquent : $\ell=0$.
