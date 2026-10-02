---
source: "PREING2-S2/Integration-proba-DS/DS1-2021-2022-(DM1)-Correction_Integration-proba-DS_P2S2_DMaths.pdf"
pages: 7
transcription: manuelle
transcription_date: 2026-10-02
verification: lecture visuelle intégrale des 7 pages, restitution des deux tableaux et vérification des formules
---

# TD Révision — Intégrales généralisées — Corrigé

CY Tech — Département de mathématiques — Préing 2 — Intégration et probabilités — 2021–2022.

## Exercice 1 — Nature de six intégrales

Étudier la nature des intégrales suivantes.

### a) Intégrale de $(1-\cos x)/x^2$

$$
\int_1^{+\infty}\frac{1-\cos x}{x^2}\,dx.
$$

La fonction $f(x)=(1-\cos x)/x^2$ est continue sur $\mathbb R^*$, donc sur $[1,+\infty[$. Le seul problème de convergence est à l’infini. Puisque $|\cos x|\leq1$,

$$
\left|\frac{1-\cos x}{x^2}\right|
\leq\frac{|1-\cos x|}{x^2}
\leq\frac{1+|\cos x|}{x^2}
\leq\frac2{x^2}.
$$

L’intégrale $\int_1^{+\infty}dx/x^2$ est une intégrale de Riemann convergente, d’exposant $2>1$. Par comparaison, l’intégrale proposée converge.

### b) Intégrale de $1/[x(x+2)]$

$$
\int_{-1}^0\frac{dx}{x(x+2)}.
$$

La fonction est continue sur $\mathbb R\setminus\{-2,0\}$, donc sur $[-1,0[$. Le problème est en $0$. Pour $-1<\varepsilon<0$, on étudie l’intégrale arrêtée en $\varepsilon$. Cherchons $\lambda,\mu$ tels que

$$
\frac1{x(x+2)}=\frac\lambda x+\frac\mu{x+2}
=\frac{(\lambda+\mu)x+2\lambda}{x(x+2)}.
$$

L’identification donne $\lambda+\mu=0$, $2\lambda=1$, donc $\lambda=1/2$ et $\mu=-1/2$. Ainsi

$$
\frac1{x(x+2)}=\frac1{2x}-\frac1{2(x+2)}
$$

et

$$
\begin{aligned}
\int_{-1}^{\varepsilon}\frac{dx}{x(x+2)}
&=\frac12\int_{-1}^{\varepsilon}\frac{dx}{x}
-\frac12\int_{-1}^{\varepsilon}\frac{dx}{x+2}\\
&=\frac12[\ln|x|]_{-1}^{\varepsilon}
-\frac12[\ln|x+2|]_{-1}^{\varepsilon}\\
&=\frac12\ln|\varepsilon|-\frac12\ln|\varepsilon+2|
\underset{\varepsilon\to0^-}{\longrightarrow}-\infty.
\end{aligned}
$$

L’intégrale diverge.

**Autre méthode.** Pour $-1\leq x<0$, on a $1\leq x+2\leq2$, donc $1/2\leq1/(x+2)\leq1$ et

$$
\left|\frac1{x(x+2)}\right|\geq\frac1{2|x|}.
$$

L’intégrale $\int_{-1}^0dx/|x|$ diverge. L’intégrande étant de signe constant négatif, l’intégrale proposée diverge par comparaison.

> **Coquille de la source, page 2.** La première décomposition imprimée omet le facteur $1/2$ devant $1/x$. Les coefficients calculés page 1 et l’intégration qui suit confirment la formule restituée ci-dessus.

### c) Intégrale de $x^2/(x^{17/5}+1)$

$$
\int_0^{+\infty}\frac{x^2}{x^{17/5}+1}\,dx.
$$

La fonction est continue sur $[0,+\infty[$ ; pour $x>0$, le dénominateur est strictement supérieur à $1$. Seul l’infini pose problème. Puisque $x^{17/5}+1\geq x^{17/5}$,

$$
0\leq\frac{x^2}{x^{17/5}+1}
\leq\frac{x^2}{x^{17/5}}
=\frac1{x^{17/5-2}}
=\frac1{x^{7/5}}.
$$

L’intégrale $\int_1^{+\infty}dx/x^{7/5}$ converge, car $7/5>1$. L’intégrale proposée converge par comparaison.

### d) Intégrale de $e^{\cos x}/x$

$$
\int_{-\infty}^{-1}\frac{e^{\cos x}}x\,dx.
$$

La fonction est continue sur $]-\infty,-1]$. Puisque $-1\leq\cos x\leq1$, on a $e^{-1}\leq e^{\cos x}\leq e$. Pour $x<-1$,

$$
\frac{e^{-1}}x\geq\frac{e^{\cos x}}x\geq\frac ex.
$$

L’intégrale de $e^{-1}/x$ sur $]-\infty,-1]$ diverge vers $-\infty$. Par comparaison, l’intégrale proposée diverge aussi vers $-\infty$.

> **Justification rectifiée, page 2.** Le corrigé invoque la divergence de l’intégrale de $e/x$, qui constitue ici la borne inférieure. Pour conclure avec cet encadrement de fonctions négatives, il faut utiliser la borne supérieure $e^{-1}/x$. La conclusion de la source est conservée.

### e) Intégrale avec arctangente

$$
\int_3^{+\infty}\frac{\arctan x}{x^2+2x+7}\,dx.
$$

Le polynôme $x^2+2x+7$ ne s’annule pas. Sur $[3,+\infty[$,

$$
\left|\frac{\arctan x}{x^2+2x+7}\right|
\leq\frac{\pi/2}{x^2}=\frac\pi{2x^2}.
$$

L’intégrale majorante converge ; l’intégrale proposée converge absolument.

### f) Intégrale de Bertrand

$$
\int_2^{+\infty}\frac{dx}{x(\ln x)^2}.
$$

Le changement de variable $u=\ln x$ donne

$$
\int\frac{dx}{x(\ln x)^2}=\int\frac{du}{u^2}
=-\frac1u=-\frac1{\ln x}.
$$

Donc l’intégrale converge et

$$
\int_2^{+\infty}\frac{dx}{x(\ln x)^2}
=\left[-\frac1{\ln x}\right]_2^{+\infty}
=\frac1{\ln2}.
$$

## Exercice 2 — Intégrale dépendant de $n$

Étudier pour quelles valeurs de $n\in\mathbb N$ l’intégrale

$$
I(n)=\int_1^{+\infty}\frac{\ln x}{x^n}\,dx
$$

converge, puis calculer sa valeur.

**Solution.** Le critère de Bertrand à l’infini pour $1/[x^\alpha(\ln x)^\beta]$ est : $\alpha>1$, ou $\alpha=1$ et $\beta>1$. Ici $\alpha=n$ et $\beta=-1$ ; l’intégrande est continue en $1$. Ainsi $I(n)$ converge si et seulement si $n\geq2$.

Pour $n\geq2$, une intégration par parties donne

$$
\begin{aligned}
\int\frac{\ln x}{x^n}\,dx
&=\frac{x^{1-n}}{1-n}\ln x
-\int\frac{x^{1-n}}{1-n}\frac{dx}{x}\\
&=\frac{x^{1-n}}{1-n}\ln x-\frac{x^{1-n}}{(n-1)^2}.
\end{aligned}
$$

Par conséquent,

$$
I(n)=\left[\frac{x^{1-n}}{1-n}\ln x
-\frac{x^{1-n}}{(n-1)^2}\right]_1^{+\infty}
=\frac1{(n-1)^2}.
$$

> **Précision sur le rappel de la source, page 3.** Le critère général de Bertrand cité concerne le voisinage de l’infini. Il ne garantit pas, à lui seul, la convergence à la borne $1$ pour tous les exposants $\beta$. Dans cet exercice, il n’y a pas de singularité en $1$.

## Exercice 3 — Développements limités et changements de variable

Étudier la nature de

$$
I=\int_2^{+\infty}\left(1-\cos\frac1t\right)dt,
\qquad J=\int_0^1\sin\frac1t\,dt,
\qquad K=\int_{2/\pi}^{+\infty}\ln\left(\cos\frac1t\right)dt.
$$

### Intégrale $I$

Le problème est en $+\infty$. Le développement limité donne

$$
1-\cos\frac1t
=1-\left(1-\frac1{2t^2}+o(t^{-2})\right)
=\frac1{2t^2}+o(t^{-2})\sim\frac1{2t^2}.
$$

L’intégrale de Riemann correspondante converge, donc $I$ converge.

### Intégrale $J$

Le problème est en $0$. On ne peut pas utiliser le développement limité de sinus en zéro, puisque $1/t$ tend vers l’infini. Pour $0<\varepsilon<1$, posons

$$
J(\varepsilon)=\int_\varepsilon^1\sin\frac1t\,dt.
$$

Avec $u=1/t$, $t=1/u$ et $dt=-du/u^2$, les bornes deviennent $1/\varepsilon$ et $1$, d’où

$$
J(\varepsilon)
=\int_{1/\varepsilon}^1\sin u\left(-\frac{du}{u^2}\right)
=\int_1^{1/\varepsilon}\frac{\sin u}{u^2}\,du.
$$

Comme $|\sin u/u^2|\leq1/u^2$, la fonction est absolument intégrable à l’infini. Donc $J$ converge absolument.

> **Erreur de signe de la source, page 4.** Les bornes du changement de variable y sont inversées sans compenser le signe de $dt$. La formule correcte est celle ci-dessus ; la conclusion de convergence est inchangée.

### Intégrale $K$

Deux bornes sont à examiner : $2/\pi$, car $\cos(1/(2/\pi))=\cos(\pi/2)=0$, et $+\infty$.

Au voisinage de $2/\pi$, on pose $u=t-2/\pi$. Pour $a>2/\pi$, les bornes $t=2/\pi$ et $t=a$ donnent $u=0$ et $u=a-2/\pi$. Alors

$$
\begin{aligned}
\ln\left(\cos\frac1t\right)
&=\ln\left(\cos\left(\frac\pi2\frac1{1+\pi u/2}\right)\right)\\
&=\ln\left(\cos\left(\frac\pi2-\frac{\pi^2}4u+o(u)\right)\right)\\
&=\ln\left(\sin\left(\frac{\pi^2}4u+o(u)\right)\right)\\
&=\ln\left(\frac{\pi^2}4u+o(u)\right)
=\ln\frac{\pi^2}4+\ln(u+o(u))\sim\ln u.
\end{aligned}
$$

Or

$$
\int_0^{a-2/\pi}\ln u\,du
=[u\ln u-u]_0^{a-2/\pi}
=\left(a-\frac2\pi\right)\ln\left(a-\frac2\pi\right)
-\left(a-\frac2\pi\right)
$$

est finie. L’intégrale converge donc à la borne inférieure.

À l’infini,

$$
\ln\left(\cos\frac1t\right)
=\ln\left(1-\frac1{2t^2}+o(t^{-2})\right)
=-\frac1{2t^2}+o(t^{-2})\sim-\frac1{2t^2}.
$$

L’intégrale de comparaison converge. Par conséquent, $K$ converge.

> **Coquilles de la source, page 4.** L’argument du cosinus au point singulier est imprimé $2/(2/\pi)$ au lieu de $1/(2/\pi)$ ; la condition sur la borne auxiliaire est parfois imprimée $a>\pi/2$. On utilise ici $a>2/\pi$, conformément à la borne de l’intégrale.

## Exercice 4 — Conditions sur deux paramètres

Déterminer les couples $(\alpha,\beta)\in\mathbb R^2$ pour lesquels les intégrales suivantes convergent :

$$
\int_0^{+\infty}\frac{dx}{x^\alpha(1+x^\beta)},
\qquad
\int_0^{+\infty}\frac{\ln(1+x^\alpha)}{x^\beta}\,dx.
$$

### Première intégrale

On cherche les équivalents de $f(x)=1/[x^\alpha(1+x^\beta)]$ en zéro et à l’infini. Ils dépendent du signe de $\beta$.

| Cas | Équivalent en $0$ | Équivalent en $+\infty$ | Convergence de $\int_0^1 f$ | Convergence de $\int_1^{+\infty} f$ |
| --- | --- | --- | --- | --- |
| $\beta>0$ | $1/x^\alpha$ | $1/x^{\alpha+\beta}$ | $\alpha<1$ | $\alpha+\beta>1$ |
| $\beta=0$ | $1/(2x^\alpha)$ | $1/(2x^\alpha)$ | $\alpha<1$ | $\alpha>1$ |
| $\beta<0$ | $1/x^{\alpha+\beta}$ | $1/x^\alpha$ | $\alpha+\beta<1$ | $\alpha>1$ |

L’ensemble recherché est délimité par les droites $\alpha+\beta=1$ et $\alpha=1$, exclues. Explicitement, il faut $\alpha<1<\alpha+\beta$ ou $\alpha+\beta<1<\alpha$. Le cas $\beta=0$ est impossible.

### Seconde intégrale

Cette fois, les équivalents dépendent du signe de $\alpha$. En zéro, si $\alpha>0$, alors $x^\alpha\to0$ et $\ln(1+x^\alpha)\sim x^\alpha$. Si $\alpha<0$,

$$
\ln(1+x^\alpha)=\ln(x^\alpha)+\ln(1+x^{-\alpha})
=\alpha\ln x\left(1+\frac{\ln(1+x^{-\alpha})}{\alpha\ln x}\right)
\sim\alpha\ln x.
$$

Les rôles sont inversés à l’infini. Pour $f(x)=\ln(1+x^\alpha)/x^\beta$ :

| Cas | Équivalent en $0$ | Équivalent en $+\infty$ | Convergence de $\int_0^1 f$ | Convergence de $\int_1^{+\infty} f$ |
| --- | --- | --- | --- | --- |
| $\alpha>0$ | $1/x^{\beta-\alpha}$ | $\alpha\ln x/x^\beta$ | $\beta-\alpha<1$ | $\beta>1$ |
| $\alpha=0$ | $\ln2/x^\beta$ | $\ln2/x^\beta$ | $\beta<1$ | $\beta>1$ |
| $\alpha<0$ | $\alpha\ln x/x^\beta$ | $1/x^{\beta-\alpha}$ | $\beta<1$ | $\beta-\alpha>1$ |

L’ensemble recherché est délimité par les droites $\beta-\alpha=1$ et $\beta=1$, exclues. Explicitement, $\beta-\alpha<1<\beta$ ou $\beta<1<\beta-\alpha$. Le cas $\alpha=0$ est impossible.

## Exercice 5 — Deux singularités différentes

Étudier la nature de

$$
I=\int_0^1\frac{dx}{1-\sqrt x},
\qquad J=\int_0^{+\infty}\frac{e^{-x}-e^{-2x}}x\,dx.
$$

### Intégrale $I$

La fonction $1/(1-\sqrt x)$ est continue sur $[0,1[$. Au voisinage de $1$, posons $x=1+u$ ; alors $u\to0^-$ et

$$
1-\sqrt x=1-\sqrt{1+u}
=1-\left(1+\frac u2+o(u)\right)
=-\frac u2+o(u)\sim\frac{1-x}2.
$$

Ainsi $1/(1-\sqrt x)\sim2/(1-x)$ en $1$. L’intégrale de comparaison diverge, donc $I$ diverge.

### Intégrale $J$

Au voisinage de zéro,

$$
e^{-t}-e^{-2t}=1-t-(1-2t)+o(t)=t+o(t),
\qquad \lim_{t\to0}\frac{e^{-t}-e^{-2t}}t=1.
$$

La fonction se prolonge par continuité en zéro ; l’intégrale sur $]0,1]$ converge. Pour $t\geq1$,

$$
0\leq\frac{e^{-t}}t\leq e^{-t},
\qquad 0\leq\frac{e^{-2t}}t\leq e^{-2t}.
$$

Les intégrales des deux exponentielles sur $[1,+\infty[$ convergent, donc celles de $e^{-t}/t$ et $e^{-2t}/t$ aussi. L’intégrale de leur différence converge à l’infini ; par conséquent, $J$ converge.
