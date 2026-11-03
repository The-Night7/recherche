---
source: "PREING2-S2/Integration-proba-DS/DS2-2024-2025-V2-Correction_Integration-proba-DS_P2S2_DMaths.pdf"
pages: 4
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Intégration et probabilités — Contrôle continu 2 — Version 2, corrigé

CY Tech — 2024/2025 — Semestre 2, PréIng 2 — Mercredi 2 avril. Durée : 60 minutes.

Les documents et les supports électroniques sont interdits. L’épreuve est composée d’exercices indépendants. Le barème est indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte dans la notation.

## Exercice 1 — Fubini par tranches (5 points)

1. Représenter graphiquement le domaine $D$ délimité par les courbes d’équation $y^2=x-1$ et $x^2+y^2=4$.
2. Soit une fonction $f$ définie sur $\mathbb R^2$. Énoncer le théorème de Fubini par tranches pour calculer

$$
I=\iint_D f(x,y)\,dx\,dy.
$$

### Réponse

On reconnaît la parabole $x=y^2+1$ et le cercle de centre $(0,0)$ et de rayon $2$, d’équation $x^2+y^2=4$.

**Figure de la source, page 1.** Le cercle est tracé en bleu-vert ; la parabole, en rouge, est ouverte vers la droite et a son sommet en $(1,0)$. Le domaine $D$ colorié est la région à l’intérieur du cercle située à droite de la parabole, entre leurs deux intersections. Il est symétrique par rapport à l’axe des abscisses.

**Théorème de Fubini par tranches.** Soient $c,d\in\mathbb R$, avec $c<d$, et $\psi_1,\psi_2$ deux fonctions continues par morceaux sur $[c,d]$ telles que

$$
\forall y\in[c,d],\qquad\psi_1(y)\leq\psi_2(y).
$$

Soient le domaine

$$
D=\{(x,y)\in\mathbb R^2:c\leq y\leq d,\ \psi_1(y)\leq x\leq\psi_2(y)\}
$$

et une fonction $f:\mathbb R^2\to\mathbb R$ continue sur $D$. Alors

$$
\iint_D f
=\int_c^d\left(\int_{\psi_1(y)}^{\psi_2(y)}f(x,y)\,dx\right)dy.
$$

## Exercice 2 — Intégrale à paramètre et sinus cardinal (8 points)

On rappelle que la fonction sinus cardinal,

$$
\operatorname{sinc}(y)=\frac{\sin y}{y},
$$

est continue sur $\mathbb R$ et bornée en valeur absolue par une constante positive $K$.

> **Précision de transcription.** La source donne cette formule sur $\mathbb R$ sans écrire le prolongement en zéro : on comprend $\operatorname{sinc}(0)=1$ et la formule du quotient pour $y\neq0$.

Soit

$$
F(x)=\int_0^{+\infty}e^{-t}\frac{\sin(xt)}t\,dt.
$$

1. Montrer que $F$ est de classe $C^1$ sur $\mathbb R$ et déterminer $F'(x)$.
2. À l’aide d’intégrations par parties, montrer que $F'(x)=1-x^2F'(x)$.
3. En déduire une expression explicite de $F'$ en fonction de $x$, puis de $F$. On pourra s’aider de la valeur de $F(0)$.

### Réponse 1 — Dérivation sous le signe intégral

On utilise le théorème de dérivation sous le signe intégral, avec

$$
f(t,x)=e^{-t}\frac{\sin(xt)}t.
$$

Vérifions les quatre hypothèses :

- Pour tout $t>0$ fixé, $x\mapsto f(t,x)$ est de classe $C^1$ sur $\mathbb R$, car le sinus l’est.
- Pour tout $x\in\mathbb R$ fixé et tout $t>0$,

$$
|f(t,x)|=|xe^{-t}\operatorname{sinc}(xt)|\leq K|x|e^{-t}.
$$

La majorante est intégrable sur $]0,+\infty[$, comme multiple de l’intégrale généralisée de référence de $t\mapsto e^{-t}$. Le théorème de majoration assure donc l’intégrabilité de $t\mapsto f(t,x)$.

- Pour tout $(t,x)\in\mathbb R_+^*\times\mathbb R$,

$$
\frac{\partial f}{\partial x}(t,x)=e^{-t}\cos(tx).
$$

Pour tout $x$ fixé, cette fonction est continue en $t$ sur $]0,+\infty[$, comme produit de fonctions continues.

- On pose $\psi(t)=e^{-t}$, fonction intégrable sur $]0,+\infty[$. Pour tout $(t,x)\in\mathbb R_+^*\times\mathbb R$,

$$
\left|\frac{\partial f}{\partial x}(t,x)\right|\leq\psi(t),
$$

car le cosinus est borné par $1$ en valeur absolue.

Les quatre hypothèses sont vérifiées, donc **$F\in C^1(\mathbb R)$** et

$$
\forall x\in\mathbb R,\qquad
F'(x)=\int_0^{+\infty}e^{-t}\cos(xt)\,dt.
$$

> La source écrit $xe^{-t}\sin(xt)/(xt)$ dans la majoration. L’écriture avec $\operatorname{sinc}$ ci-dessus inclut aussi $x=0$ grâce au prolongement précisé dans l’énoncé.

### Réponse 2 — Deux intégrations par parties

Fixons $x\in\mathbb R$. L’intégrale définissant $F'(x)$ converge d’après la question 1, et

$$
\lim_{t\to0^+}-e^{-t}\cos(xt)=-1,
\qquad
\lim_{t\to+\infty}-e^{-t}\cos(xt)=0.
$$

On peut appliquer le théorème d’intégration par parties pour les intégrales convergentes :

$$
\begin{aligned}
F'(x)
&=\bigl[-e^{-t}\cos(xt)\bigr]_0^{+\infty}
-\int_0^{+\infty}e^{-t}x\sin(xt)\,dt\\
&=1-x\int_0^{+\infty}e^{-t}\sin(xt)\,dt.
\end{aligned}
$$

On procède à une seconde intégration par parties. L’intégrale converge, et

$$
\lim_{t\to0^+}-e^{-t}\sin(tx)=0,
\qquad
\lim_{t\to+\infty}-e^{-t}\sin(tx)=0.
$$

Donc

$$
\begin{aligned}
\int_0^{+\infty}e^{-t}\sin(xt)\,dt
&=\bigl[-e^{-t}\sin(xt)\bigr]_0^{+\infty}
+\int_0^{+\infty}e^{-t}x\cos(xt)\,dt\\
&=0+x\int_0^{+\infty}e^{-t}\cos(xt)\,dt
=xF'(x).
\end{aligned}
$$

En regroupant les deux résultats,

$$
\boxed{F'(x)=1-x^2F'(x).}
$$

### Réponse 3 — Expression de $F$

L’égalité précédente donne immédiatement

$$
\forall x\in\mathbb R,\qquad F'(x)=\frac1{1+x^2},
$$

puisque $1+x^2\neq0$. Il existe donc $C\in\mathbb R$ tel que

$$
F(x)=\arctan x+C.
$$

Par définition de l’intégrale à paramètre,

$$
F(0)=\int_0^{+\infty}e^{-t}\frac0t\,dt=0.
$$

Comme $F(0)=\arctan0+C$, on a $C=0$. Finalement,

$$
\boxed{F(x)=\arctan x.}
$$

## Exercice 3 — Intégration par piles (7 points)

Soit $\Delta$ le domaine délimité par la droite $y=x$ et la courbe $y=2-x^2$, et soit $f(x,y)=xy$.

1. Représenter graphiquement $\Delta$.
2. En procédant à une intégration par piles, calculer $\iint_\Delta f(x,y)\,dx\,dy$.

### Réponse 1 — Domaine

On reconnaît une droite $y=x$ et une parabole $y=2-x^2$.

**Figure de la source, page 3.** La droite, en bleu-vert, passe par l’origine. La parabole, en rouge, est tournée vers le bas et a son sommet en $(0,2)$. Les intersections sont $(-2,-2)$ et $(1,1)$. Le domaine colorié se situe entre la droite, en dessous, et la parabole, au-dessus. Le dessin le note $D$, tandis que l’énoncé et le calcul le notent $\Delta$.

### Réponse 2 — Calcul

On peut écrire

$$
\Delta=\{(x,y)\in\mathbb R^2:x\leq y,\ y\leq2-x^2\}.
$$

Pour que les deux conditions soient simultanément remplies, il faut $x\leq2-x^2$, donc $x$ entre les deux racines du polynôme

$$
x^2+x-2=(x-1)(x+2).
$$

Ainsi,

$$
\Delta=\{(x,y)\in\mathbb R^2:-2\leq x\leq1,\ x\leq y\leq2-x^2\}.
$$

Les fonctions $\varphi_1(x)=x$ et $\varphi_2(x)=2-x^2$ sont continues sur $[-2,1]$. La fonction $f(x,y)=xy$ est continue sur $\mathbb R^2$ car polynomiale, donc en particulier sur $\Delta$. Le théorème de Fubini par piles donne

$$
\begin{aligned}
\iint_\Delta f
&=\int_{-2}^1\left(\int_x^{2-x^2}xy\,dy\right)dx\\
&=\int_{-2}^1\left[\frac{xy^2}{2}\right]_{y=x}^{y=2-x^2}dx\\
&=\int_{-2}^1\frac x2\bigl((2-x^2)^2-x^2\bigr)\,dx\\
&=\frac12\int_{-2}^1(x^5-5x^3+4x)\,dx\\
&=\frac12\left[\frac{x^6}{6}-\frac{5x^4}{4}+2x^2\right]_{-2}^1\\
&=\frac12\left(\frac16-\frac54+2-\frac{64}6+\frac{5\times16}4-2\times4\right)
=\frac98.
\end{aligned}
$$
