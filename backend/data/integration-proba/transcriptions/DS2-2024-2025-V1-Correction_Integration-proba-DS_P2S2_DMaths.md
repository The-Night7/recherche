---
source: "PREING2-S2/Integration-proba-DS/DS2-2024-2025-V1-Correction_Integration-proba-DS_P2S2_DMaths.pdf"
pages: 4
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Intégration et probabilités — Contrôle continu 2 — Version 1, corrigé

CY Tech — 2024/2025 — Semestre 2, PréIng 2 — Mercredi 2 avril. Durée : 60 minutes.

Les documents et les supports électroniques sont interdits. L’épreuve est composée d’exercices indépendants. Le barème est indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte dans la notation.

## Exercice 1 — Fubini par piles (5 points)

1. Représenter graphiquement le domaine $D$ délimité par les courbes d’équation $y=x^2+1$ et $y=2x^2$.
2. Soit une fonction $f$ définie sur $\mathbb R^2$. Énoncer le théorème de Fubini par piles pour calculer

$$
I=\iint_D f(x,y)\,dx\,dy.
$$

### Réponse

**Figure de la source, page 1.** Dans le repère $(x,y)$, la parabole $y=2x^2$ (en bleu-vert) a son sommet à l’origine ; la parabole $y=x^2+1$ (en rouge) a son sommet en $(0,1)$. Les courbes se coupent en $(-1,2)$ et $(1,2)$. Le domaine $D$ colorié se trouve entre ces deux courbes, au-dessus de $y=2x^2$ et au-dessous de $y=x^2+1$, pour $-1\leq x\leq1$.

On pose les fonctions continues $\varphi_1(x)=2x^2$ et $\varphi_2(x)=x^2+1$, et

$$
D=\{(x,y)\in\mathbb R^2:-1\leq x\leq1,\ \varphi_1(x)\leq y\leq\varphi_2(x)\}.
$$

Si $f$ est continue sur $D$, le théorème de Fubini par piles donne

$$
\iint_D f(x,y)\,dx\,dy
=\int_{-1}^1\left(\int_{2x^2}^{x^2+1}f(x,y)\,dy\right)dx.
$$

> **Coquille de la source.** Le membre de gauche de cette formule porte $dx\,dx$ au lieu de $dx\,dy$.

## Exercice 2 — Intégrale à paramètre (8 points)

Soit l’application $F$ définie par

$$
F(x)=\int_{\mathbb R}\frac{\ln(t^2+x)}{1+t^2}\,dt.
$$

1. Montrer que $F$ est définie sur $\mathbb R_+$.
2. Montrer que $F\in C^0(\mathbb R_+)$.
3. Montrer que $F\in C^1(\mathbb R_+^*)$ et calculer sa dérivée.
4. La fonction $F$ admet-elle un minimum sur $\mathbb R_+$ ?

### Réponse 1 — Domaine de définition

On pose $f(t,x)=\ln(t^2+x)/(1+t^2)$, avec les domaines de paramètre et d’intégration $A=\mathbb R_+$ et $I=\mathbb R$.

Pour $x=0$, $t\mapsto f(t,0)$ présente une singularité en zéro ; ce n’est pas le cas pour $x>0$.

Si $x>0$, $t\mapsto f(t,x)$ est continue sur $\mathbb R$. En $+\infty$,

$$
f(t,x)\sim\frac{\ln(t^2)}{t^2},
\qquad t^{3/2}f(t,x)\longrightarrow0.
$$

La fonction est paire en $t$ : on obtient le même contrôle en $-\infty$ avec $|t|^{3/2}$. Par le critère de Riemann d’exposant $\alpha=3/2>1$, l’intégrale converge.

Si $x=0$, la fonction

$$
f(t,0)=\frac{\ln(t^2)}{1+t^2}
$$

est continue sur $\mathbb R_+^*$ et $\mathbb R_-^*$. Par parité, on se limite à $\mathbb R_+^*$. Le comportement en $+\infty$ est traité comme ci-dessus. En zéro,

$$
f(t,0)\underset{t\to0^+}{\sim}\ln(t^2),
\qquad t^{1/2}f(t,0)\longrightarrow0.
$$

Le critère de Riemann en zéro, avec $\alpha=1/2<1$, assure la convergence au voisinage de zéro. Ainsi, pour tout $x\in\mathbb R_+$, l’intégrale définissant $F(x)$ converge : **$F$ est bien définie sur $\mathbb R_+$.**

### Réponse 2 — Continuité

**Indication du corrigé.** Cette question est plus difficile que la question 3. Il vaut mieux traiter d’abord la question 3, puis établir la continuité de $F$ en zéro. Cette question compte donc très peu dans le barème. Le corrigé donne néanmoins d’abord une preuve de la continuité sur $\mathbb R_+^*$, puis une preuve en zéro.

#### Continuité sur $\mathbb R_+^*$

On utilise le théorème de continuité sous le signe intégral. On ne peut pas borner $\ln(t^2+x)$ uniformément en $x$ lorsque $x\to+\infty$ ; on se restreint donc à $x\in[\varepsilon,A]$, où $0<\varepsilon<A$.

On a $t^2+x\geq t^2+\varepsilon\geq\varepsilon$. La fonction $y\mapsto y^{-1/4}\ln y$ est continue sur $[\varepsilon,+\infty[$ et tend vers zéro à l’infini par croissance comparée. Elle est donc bornée en valeur absolue par une constante $K$, dépendant de $\varepsilon$. Ainsi,

$$
\begin{aligned}
|f(t,x)|
&=\left|(t^2+x)^{1/4}\frac{\ln(t^2+x)}{(t^2+x)^{1/4}}\frac1{1+t^2}\right|\\
&\leq K\left(\frac{t^2}{(1+t^2)^4}+\frac{x}{(1+t^2)^4}\right)^{1/4}\\
&\leq K\left(\frac1{(1+t^2)^3}+\frac{A}{(1+t^2)^4}\right)^{1/4}\\
&\leq\frac{K(1+A)^{1/4}}{(1+t^2)^{3/4}}.\tag{1}
\end{aligned}
$$

On applique le théorème sur $[\varepsilon,A]$ :

- Pour tout $t\in I$, $x\mapsto f(t,x)$ est continue sur $[\varepsilon,A]$.
- Pour tout $x\in[\varepsilon,A]$, $t\mapsto f(t,x)$ est continue sur $\mathbb R$.
- La majoration (1) fournit une fonction dominante indépendante de $x$ et intégrable sur $\mathbb R$.

Donc $F$ est continue sur $[\varepsilon,A]$. Comme cela vaut pour tous $0<\varepsilon<A$, **$F$ est continue sur $\mathbb R_+^*$.**

#### Continuité en zéro

On se restreint à $x\in[0,1]$ et on décompose, en utilisant la parité,

$$
F(x)=F_-(x)+F_+(x),
\qquad
F_-(x)=\int_{-\infty}^0 f(t,x)\,dt,
\qquad
F_+(x)=\int_0^{+\infty}f(t,x)\,dt.
$$

On applique la convergence dominée à $F_+$ ; le raisonnement est identique pour $F_-$. On sépare $]0,+\infty[$ en $]0,1]$ et $]1,+\infty[$.

Pour $x\in]0,1]$ et $t\in]0,1]$, on a $t^2+x\in]0,2]$. La fonction $y\mapsto y^{1/4}\ln y$ est continue sur $]0,2]$ et prolongeable par continuité en zéro ; elle est donc bornée en valeur absolue par une constante $K_1$. Ainsi,

$$
|f(t,x)|
=\left|(t^2+x)^{1/4}\ln(t^2+x)\frac1{(t^2+x)^{1/4}(1+t^2)}\right|
\leq\frac{K_1}{t^{1/2}}.
$$

Pour $x\in]0,1]$ et $t\in]1,+\infty[$, on a $t^2+x>1$. On reprend l’argument (1) avec une constante $K_2$ :

$$
|f(t,x)|
\leq\left|\frac{\ln(t^2+x)}{(t^2+x)^{1/4}}\frac{(t^2+x)^{1/4}}{1+t^2}\right|
\leq\frac{K_2\,2^{1/4}}{(1+t^2)^{3/4}}.
$$

On définit la fonction dominante

$$
\varphi(t)=K_1t^{-1/2}\mathbf1_{]0,1]}(t)
+K_2\,2^{1/4}(1+t^2)^{-3/4}\mathbf1_{]1,+\infty[}(t).
$$

Les hypothèses de convergence dominée sur $]0,+\infty[$ sont les suivantes :

- Pour tout $t>0$, $f(t,x)\to\ell(t)=\ln(t^2)/(1+t^2)$ lorsque $x\to0^+$.
- Pour tout $x\in]0,1]$, $t\mapsto f(t,x)$ est continue sur $\mathbb R_+^*$.
- La fonction $\ell$ est continue sur $\mathbb R_+^*$.
- Pour tout $(t,x)\in\mathbb R_+^*\times]0,1]$, $|f(t,x)|\leq\varphi(t)$, avec $\varphi$ intégrable.

Par conséquent,

$$
\lim_{x\to0^+}F_+(x)=\int_0^{+\infty}\frac{\ln(t^2)}{1+t^2}\,dt=F_+(0).
$$

La fonction $F_+$ est donc continue sur $[0,1]$. On procède de même pour $F_-$, et l’on conclut que **$F$ est continue sur $[0,1]$, puis sur $\mathbb R_+$.**

> **Coquilles de la source, page 3.** Dans la dernière intégrale donnant $\lim_{x\to0^+}F_+(x)$, le PDF écrit $\ln t$ au lieu de $\ln(t^2)$. Il indique ensuite que $F_-$ est continue sur « $[0,-1]$ » ; le paramètre est toujours $x\in[0,1]$. Ces deux expressions sont rectifiées ici.

### Réponse 3 — Dérivation sous le signe intégral

On considère $[\varepsilon,+\infty[$, avec $\varepsilon>0$.

Pour tout $t\in\mathbb R$, $x\mapsto f(t,x)$ est de classe $C^1$ sur cet intervalle, et

$$
\frac{\partial f}{\partial x}(t,x)=\frac1{t^2+x}\frac1{1+t^2}.
$$

Pour tout $x>0$, l’intégrabilité de $t\mapsto f(t,x)$ a été établie à la question 1. La fonction $t\mapsto\partial f/\partial x(t,x)$ est continue sur $\mathbb R$. Enfin,

$$
\forall(t,x)\in\mathbb R\times[\varepsilon,+\infty[,
\qquad
\left|\frac{\partial f}{\partial x}(t,x)\right|
\leq\frac1\varepsilon\frac1{1+t^2}.
$$

Cette majorante est intégrable et indépendante de $x$. Le théorème de dérivation sous le signe intégral donne donc $F\in C^1(\mathbb R_+^*)$ et

$$
F'(x)=\int_{\mathbb R}\frac1{t^2+x}\frac1{1+t^2}\,dt.
$$

### Réponse 4 — Minimum

Pour tout $x>0$, $F'(x)>0$. La fonction $F$ est donc strictement croissante sur $\mathbb R_+^*$. Par continuité sur $\mathbb R_+$, elle **atteint son minimum en zéro**.

## Exercice 3 — Coordonnées polaires (7 points)

Dans un plan muni d’un repère orthonormé, on considère

$$
\Omega=\{(x,y)\in\mathbb R^2:x\geq0,\ x^2+y^2\leq1\}.
$$

1. Représenter graphiquement $\Omega$.
2. Soit $f(x,y)=\exp(-x^2-y^2)$. Calculer $\iint_\Omega f(x,y)\,dx\,dy$.

### Réponse

**Figure de la source, page 4.** Le domaine colorié est le demi-disque unité à droite de l’axe des ordonnées, limité par le segment joignant $(0,-1)$ à $(0,1)$ et le demi-cercle passant par $(1,0)$. Le dessin désigne ce domaine par $D$.

> **Erreur de légende.** La courbe du dessin est étiquetée $y=\sqrt{x^2+1}$, ce qui ne décrit pas ce demi-cercle. Sa frontière courbe vérifie $x^2+y^2=1$ avec $x\geq0$, soit $x=\sqrt{1-y^2}$.

On effectue le changement de variables polaires

$$
\varphi(r,\theta)=(r\cos\theta,r\sin\theta),
\qquad \operatorname{Jac}(\varphi)=r.
$$

Le corrigé décrit le domaine sous la forme

$$
D=\{(x,y)\in\mathbb R^2:-1\leq y\leq1,\ 0\leq x\leq\sqrt{1-y^2}\}=\Omega,
$$

avec $0<r\leq1$ et $-\pi/2<\theta<\pi/2$.

> **Précision sur les frontières.** La source qualifie $\varphi$ de $C^1$-difféomorphisme de $]0,1]\times]-\pi/2,\pi/2[$ sur le domaine fermé $D$ ; ces ensembles ne correspondent pas exactement sur leur frontière. L’énoncé rigoureux s’applique aux intérieurs ($0<r<1$, $-\pi/2<\theta<\pi/2$), et les frontières n’affectent pas l’intégrale.

Comme $f$ est continue sur $D$,

$$
\iint_D f(x,y)\,dx\,dy
=\int_0^1\int_{-\pi/2}^{\pi/2}e^{-r^2}r\,d\theta\,dr.
$$

L’intégrande est à variables séparées, donc

$$
\begin{aligned}
\iint_D f(x,y)\,dx\,dy
&=\left(\int_{-\pi/2}^{\pi/2}d\theta\right)
\left(\int_0^1re^{-r^2}\,dr\right)\\
&=\pi\left[-\frac12e^{-r^2}\right]_0^1
=\frac\pi2(1-e^{-1}).
\end{aligned}
$$
