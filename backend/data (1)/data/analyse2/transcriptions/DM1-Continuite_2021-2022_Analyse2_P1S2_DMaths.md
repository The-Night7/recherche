# Analyse 2 — Devoir Continuité (DM1) 2021–2022, sujet et solution

> Source : `PREING1-S2/Analyse2/DM1-Continuite_2021-2022_Analyse2_P1S2_DMaths.pdf`, 2 pages (PDF natif LaTeX). En-tête : « Cycle Préparatoire - Première Année — Analyse II - 2021/2022 ».
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, recoupée avec le texte natif ; formules restituées en LaTeX.
> Vérification : les raisonnements ont été refaits. Erreurs de la source, signalées et non corrigées dans le texte :
> - **Exercice 1, première solution** : pour $m>0$, c’est $h'$ qui est strictement négative sur $]-\infty;\ln(m)[$ et strictement positive sur $]\ln(m);+\infty[$, et non $h$, positive puis négative. $h$ admet donc un **minimum** en $\ln(m)$, et non un maximum. Les conclusions selon $m$ restent justes. Le cas $m=0$ n’y est pas traité : $e^x=0$ n’a pas de solution.
> - **Exercice 1, autre solution** : pour $x<1$ ($x\neq0$), $\varphi'(x)<0$, et non $\varphi'(x)>0$ ; la décroissance annoncée est juste.
> - **Conclusion de l’exercice 1** : « Si $m>e$ ou $0<m<e$, il y a deux solutions » est faux. Il y a **deux solutions si $m>e$** et **aucune solution si $0\le m<e$**, comme l’établit la première solution.
> - Le caractère parasite « ¨ » en fin de liste et l’intervalle non fermé « $]0;1.$ » sont des coquilles de la source.

# Devoir Continuité

## Exercice 1

Déterminer le nombre de solutions de l’équation

$$e^x=mx$$

selon les valeurs du paramètre réel $m$.

### Solution

(rédaction télégraphique)

On définit la fonction $h$ par $\forall x\in\mathbb R,\ h(x)=e^x-mx$. $h$ est dérivable et de dérivée $h'(x)=e^x-m$.

Si $m<0$, la fonction $h'$ ne s’annule pas donc la fonction $h$ est strictement croissante. La limite en $-\infty$ est $-\infty$ et en $+\infty$, $+\infty$ donc elle s’annule en un seul réel.

Si $m>0$ la fonction $h$ est strictement positive sur $]-\infty;\ln(m)[$ et strictement négative sur $]\ln(m);+\infty[$. Elle admet donc un maximum en $\ln(m)$ qui vaut $h(\ln m)=m-m\ln m=m(1-\ln m)$. Si $m<e$, la fonction est positive donc $h(x)$ ne s’annule pas. Si $m=e$, la fonction s’annule en un seul point. Si $m>e$, la fonction s’annule en deux points (utiliser le théorème des valeurs intermédiaires).

### Autre solution

Pour $x=0$, l’équation devient $1=0$ donc n’a pas de solution.

Pour $x\neq0$, on définit $\varphi:x\mapsto\dfrac{e^x}x$.

$$\varphi'(x)=\frac{xe^x-e^x}{x^2}=e^x\frac{x-1}{x^2}$$

Pour $x<1$, $\varphi'(x)>0$ donc la fonction est strictement décroissante sur $]-\infty;0[$ et sur $]0;1]$.
Pour $x>1$, $\varphi$ est strictement croissante.

On a $\displaystyle\lim_{x\to-\infty}\varphi(x)=0$ et $\displaystyle\lim_{x\to0^+}\varphi(x)=+\infty$.

De plus $\varphi$ est continue sur $]-\infty;0[$ donc elle réalise une bijection de $\mathbb R^-$ dans $\mathbb R^-$.

On a $\varphi(1)=e$, $\displaystyle\lim_{x\to+\infty}\varphi(x)=+\infty$ et $\displaystyle\lim_{x\to0^-}\varphi(x)=+\infty$.

> Note : la source écrit $\lim_{x\to0^-}\varphi(x)=+\infty$ ; en réalité $\lim_{x\to0^-}\varphi(x)=-\infty$, ce que suppose la bijection de $\mathbb R^-$ sur $\mathbb R^-$ annoncée juste avant. Il faut sans doute lire $\lim_{x\to0^+}$.

Donc $\varphi$ réalise une bijection de $]0;1]$ dans $[e;+\infty[$ et de $[1;+\infty[$ dans $[e;+\infty[$. Finalement,

- Si $m>e$ ou $0<m<e$, il y a deux solutions.
- Si $m=e$, il y a une unique solution
- Si $m=0$ pas de solution.
- Si $m<0$, une seule solution

## Exercice 2

1. Montrer que, si $f$ est strictement croissante, on a l’équivalence :
   $$(f\circ f)(x)=x\Leftrightarrow f(x)=x$$
2. Soit $f:\mathbb R\to\mathbb R$ définie par $f(x)=x^5+x-1$ pour $x\in\mathbb R$.
   1. (a) Montrer que f est bijective.
   2. (b) Résoudre dans $\mathbb R$ l’équation $f(x)=f^{-1}(x)$.

### Solution

1. On a $x\le f(x)\implies f(x)\le f(f(x))\implies f(x)\le x$. Donc si $x\le f(x)$ alors $x=f(x)$.
   De même $x\ge f(x)\implies f(x)\ge f(f(x))\implies f(x)\ge x$. Donc si $x\ge f(x)$ alors $x=f(x)$.
   Dans tous les cas, si $f((f(x))=x$ alors $f(x)=x$.
   La réciproque est évidente.
2. (a) La fonction $f$ est dérivable sur $\mathbb R$ et $\forall x\in\mathbb R,\ f'(x)=5x^4+1$.
   On a $\forall x\in\mathbb R,\ f'(x)>0$, donc $f$ est strictement croissante sur $\mathbb R$.
   Or $\displaystyle\lim_{x\to+\infty}f(x)=\lim_{x\to+\infty}x^5=+\infty$ et $\displaystyle\lim_{x\to-\infty}x^5=-\infty$.
   Or la fonction $f$ est une fonction polynôme donc elle est continue. L’image d’un intervalle étant un intervalle, l’image de $]-\infty;+\infty[$ est donc $]-\infty;+\infty[$. Par ailleurs, $f$ étant strictement croissante, elle réalise une bijection de $\mathbb R$ dans $\mathbb R$.

   (b) On résout $f(x)=f^{-1}(x)\Leftrightarrow f(f(x))=x\Leftrightarrow f(x)=x$ car $f$ est strictement croissante.
   $\Leftrightarrow x^5+x-1=x$
   $\Leftrightarrow x^5=1$

   Dans $\mathbb R$, la fonction $x\mapsto x^5$ étant strictement croissante, $1$ admet un unique antécédent : $1$ qui est la solution de l’équation.
