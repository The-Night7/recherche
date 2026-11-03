# CM de Séries — Chapitre I : Séries numériques

**Sommaire du cours**

| Partie | CM | TD | Évaluation |
|---|---|---|---|
| I. Séries numériques | 5-6 | 8-9 | CC1 : 15 oct |
| II. Suites de fonctions | 3-4 | 8-9 | CC2 : 19 nov |
| III. Séries de fonctions | 3-4 | 8-9 | CC3 : semaine du 11 janvier |

---

## Introduction

Soit $(u_n)_{n\in\mathbb{N}}$ une suite numérique : $\forall n\in\mathbb{N},\ u_n\in\mathbb{R}$.
Le sujet de ce chapitre est l'étude des **sommes partielles** $S_n$ de la suite $(u_n)_{n\in\mathbb{N}}$.

---

# I. Généralités sur les séries numériques

## 1) Notions fondamentales

> **Définition.** Soit une suite $(u_n)_{n\in\mathbb{N}}$. On lui associe la suite $(S_n)$ donnée par
> $$\forall n\in\mathbb{N},\quad S_n=\sum_{k=0}^{n}u_k\;(=u_0+u_1+\dots+u_n).$$
> - La suite $(S_n)$ s'appelle la **série de terme général** $u_n$.
> - Pour $n$ fixé, $S_n$ s'appelle la **somme partielle d'ordre $n$**.

**Notation.** La série $\left(\sum_{k=0}^{n}u_k\right)_n$ est souvent notée $\sum_{n\in\mathbb{N}}u_n$ (ou $\sum u_n$).

Si $(u_n)_{n\ge n_0}$ n'est définie qu'à partir du rang $n_0$, on définit la série associée $\sum_{n\ge n_0}u_n$ comme la suite des sommes partielles $S_n=\sum_{k=n_0}^{n}u_k,\ \forall n\ge n_0$.

> **Définition.** On dit que $\sum_{n\in\mathbb{N}}u_n$ est une **série numérique** si $(u_n)$ est une suite numérique, c.-à-d. $\forall n\in\mathbb{N},\ u_n\in\mathbb{R}$ ou $\mathbb{C}$.

**Exemples**

- $\sum_{n\in\mathbb{N}}n$ est la série de terme général $u_n=n$, et $\forall n\in\mathbb{N},\ S_n=\sum_{k=0}^{n}k\;\left(=\dfrac{n(n+1)}{2}\right)$.
- $\sum_{n\in\mathbb{N}}q^n$ avec $q\in\mathbb{R}$ est la série de terme général $u_n=q^n$ :
  $$\forall n\in\mathbb{N},\quad S_n=\sum_{k=0}^{n}q^k=\begin{cases}\dfrac{1-q^{n+1}}{1-q} & \text{si } q\neq1\\[2mm] n+1 & \text{si } q=1\end{cases}$$
- $\sum_{n\ge1}\dfrac1n$ est la **série harmonique**, de terme général $u_n=\dfrac1n$ ; $\forall n\ge1,\ S_n=\sum_{k=1}^{n}\dfrac1k$.

## 2) Notion de convergence

> **Définition.** On dit qu'une série numérique $\sum_{n\in\mathbb{N}}u_n$ est **CV** (convergente) si la suite des sommes partielles $(S_n)_{n\in\mathbb{N}}$ converge.
> Dans ce cas, la limite de $(S_n)$ quand $n\to+\infty$ s'appelle la **somme de la série** $\sum_{n\in\mathbb{N}}u_n$, et se note $\sum_{n=0}^{+\infty}u_n$ :
> $$\sum_{n=0}^{+\infty}u_n=\lim_{n\to+\infty}S_n=\lim_{n\to+\infty}\sum_{k=0}^{n}u_k.$$

Si la série $\sum u_n$ ne converge pas, on dit qu'elle **diverge**.

> **Définition.** On appelle **nature d'une série** le fait qu'elle est convergente ou divergente.
> On dit que 2 séries ont la **même nature** si elles sont toutes les deux convergentes ou toutes les deux divergentes.

**Remarque.** La nature d'une série dépend uniquement du comportement asymptotique de la suite $(u_n)$ lorsque $n\to+\infty$.

**Remarque.** Si on somme à partir du rang $n_0$ alors :

- $\sum_{n\ge n_0}u_n$ a la même nature que $\sum_{n\ge0}u_n$ ;
- si elle converge, la valeur de la somme change (**relation de Chasles**) :
  $$\sum_{n=n_0}^{+\infty}u_n=\sum_{n=0}^{+\infty}u_n-\sum_{n=0}^{n_0-1}u_n$$
  (somme totale moins valeurs connues).

**Exemples**

- $\sum_{n\in\mathbb{N}}n$ diverge puisque $\displaystyle\lim_{n\to+\infty}S_n=\lim_{n\to+\infty}\sum_{k=0}^{n}k=\lim_{n\to+\infty}\frac{n(n+1)}{2}=+\infty$.
- $\sum_{n\in\mathbb{N}}q^n$ avec $q\in\mathbb{R},\ q\ne1$ : on sait que $\forall n,\ S_n=\dfrac{1-q^{n+1}}{1-q}$.
  - Si $|q|<1$, alors $\lim q^{n+1}=0$ donc $\sum q^n$ converge et $\displaystyle\sum_{n=0}^{+\infty}q^n=\frac1{1-q}$.
  - Si $|q|>1$, alors $(q^n)$ diverge donc $\sum q^n$ diverge.
  - Si $q=-1$, alors $(q^n)$ diverge donc $\sum q^n$ diverge.
  - Si $q=1$, $S_n=\sum_{k=0}^{n}1=n+1\xrightarrow[n\to+\infty]{}+\infty$ donc $\sum q^n$ diverge.

### Exemple fondamental : la série harmonique

On appelle $\sum_{n\ge1}\dfrac1n$ la série harmonique, on note ses sommes partielles $H_n=\sum_{k=1}^{n}\dfrac1k$.

> **Théorème.** La série harmonique diverge.

**Heuristique** : pour $n\in\mathbb{N}$,
$$H_n=1+\underbrace{\tfrac12}_{}+\underbrace{\tfrac13+\tfrac14}_{\ge 2\times\frac14=\frac12}+\underbrace{\tfrac15+\tfrac16+\tfrac17+\tfrac18}_{\ge 4\times\frac18=\frac12}+\cdots$$

On regarde $H_{2n}-H_n$ :
$$H_{2n}-H_n=\sum_{k=1}^{2n}\frac1k-\sum_{k=1}^{n}\frac1k=\frac1{n+1}+\frac1{n+2}+\dots+\frac1{2n}$$
$n$ termes tous $\ge\dfrac1{2n}$, donc $\ge n\times\dfrac1{2n}=\dfrac12$.

> **Prop.** Si une suite numérique converge alors toute sous-suite extraite converge aussi, vers la même limite.

**Preuve (arithmétique)** — par l'absurde. On suppose que $\sum_{n\ge1}\frac1n$ converge ; notons sa somme $S=\lim H_n=\sum_{n=1}^{+\infty}\frac1n$.

La suite $(H_n)_{n\ge1}$ converge vers $S$ donc la sous-suite $(H_{2n})_{n\ge1}$ converge aussi vers $S$ :
$$\lim_{n\to+\infty}(H_{2n}-H_n)=\lim_{n\to+\infty}H_{2n}-\lim_{n\to+\infty}H_n=S-S=0.$$

Or, $\forall n\ge1$ : $H_{2n}-H_n=\sum_{k=1}^{2n}\frac1k-\sum_{k=1}^{n}\frac1k=\sum_{k=n+1}^{2n}\frac1k$, et $\forall k\in[\![n+1,2n]\!],\ \frac1k\ge\frac1{2n}$, donc
$$H_{2n}-H_n\ge\sum_{k=n+1}^{2n}\frac1{2n}=n\times\frac1{2n}=\frac12.$$
L'inégalité étant vérifiée $\forall n\ge1$, on peut passer à la limite quand $n\to+\infty$ :
$$\lim_{n\to+\infty}(H_{2n}-H_n)\ge\lim_{n\to+\infty}\frac12=\frac12.$$
**Contradiction** : $0\ge\frac12$. Conclusion du raisonnement par l'absurde : $\sum_{n\ge1}\frac1n$ diverge. $\square$

**Heuristique géométrique** : $\sum_{n\ge1}\frac1n$.
On peut interpréter $\frac1n$ comme l'aire d'un rectangle de largeur $1$ et de longueur $\frac1n$ ; la somme partielle $H_n=\sum_{k=1}^{n}\frac1k$ est donc la somme des aires des $n$ premiers rectangles. On va comparer cette aire avec une intégrale de la fonction $f:x\mapsto\frac1x$.
On voit sur le dessin que $\forall k\ge1,\ \displaystyle\int_k^{k+1}f(x)\,dx\le u_k$. On somme cette inégalité pour $k$ allant de $1$ à $n$ :
$$\underbrace{\sum_{k=1}^{n}\int_k^{k+1}f(x)\,dx}_{\text{Chasles : }\int_1^{n+1}f(x)\,dx}\le\underbrace{\sum_{k=1}^{n}u_k}_{H_n}
\qquad\text{où}\quad\int_1^{n+1}f(x)\,dx=\int_1^{n+1}\frac1x\,dx=[\ln x]_1^{n+1}=\ln(n+1)-\ln(1).$$

**Preuve (géométrique)** : on note $f:x\mapsto\frac1x$ définie sur $\mathbb{R}_+^*$. La fonction $f$ est décroissante sur $\mathbb{R}_+^*$ donc $\forall k\ge1,\ \forall x\in[k,k+1],\ f(x)\le f(k)$. Ainsi
$$\int_k^{k+1}f(x)\,dx\le\int_k^{k+1}f(k)\,dx=f(k)\int_k^{k+1}1\,dx=f(k)\,(k+1-k)=\frac1k=u_k.$$
Cette inégalité est vraie pour tout $k\ge1$ donc on peut la sommer pour $k$ allant de $1$ à $n$ : $\sum_{k=1}^{n}\int_k^{k+1}f(x)\,dx\le\sum_{k=1}^{n}u_k=H_n$.

Par la relation de Chasles :
$$\sum_{k=1}^{n}\int_k^{k+1}f(x)\,dx=\int_1^{n+1}f(x)\,dx=\int_1^{n+1}\frac1x\,dx=[\ln x]_1^{n+1}=\ln(n+1)-\ln(1)=\ln(n+1).$$
Par conséquent, $\forall n\ge1 : \ln(n+1)\le H_n$. En passant à la limite quand $n\to+\infty$, comme $\lim\ln(n+1)=+\infty$, on en déduit que $(H_n)_{n\ge1}$ diverge, en d'autres termes que $\sum_{n\ge1}\frac1n$ diverge. $\square$

## Reste d'une série convergente

> **Définition.** Soit $\sum_{n\in\mathbb{N}}u_n$ une série convergente de somme $S$. Le **reste d'ordre $n$**, noté $R_n$, est défini par
> $$R_n=\sum_{k=n+1}^{+\infty}u_k.$$

**Conséquences de la définition**

- $\forall n\in\mathbb{N},\ R_n=S-S_n=\sum_{n=0}^{+\infty}u_n-\sum_{k=0}^{n}u_k$.
- $\displaystyle\lim_{n\to+\infty}R_n=0$.
- On peut interpréter $R_n$ comme la somme de la série $\sum_{n\ge n+1}u_n$.

## Condition nécessaire de convergence

> **Théorème.** Si $\sum_{n\in\mathbb{N}}u_n$ converge alors $\displaystyle\lim_{n\to+\infty}u_n=0$.
> Contraposée : si $(u_n)_{n\in\mathbb{N}}$ ne tend pas vers $0$ alors $\sum_{n\in\mathbb{N}}u_n$ diverge.

**Preuve.** Soit $\sum u_n$ une série convergente, on note $(S_n)$ sa suite de sommes partielles. On sait que $(S_n)$ converge vers une limite $S$.
On remarque que $\forall n\ge1,\ u_n=S_n-S_{n-1}\left(=\sum_{k=0}^{n}u_k-\sum_{k=0}^{n-1}u_k\right)$.
On prend la limite quand $n\to+\infty$ : $\lim u_n=\lim S_n-\lim S_{n-1}=S-S=0$. $\square$

> **Définition.** On dit que $\sum_{n\in\mathbb{N}}u_n$ **diverge grossièrement** lorsque $(u_n)_{n\in\mathbb{N}}$ ne tend pas vers $0$.

**Exemples**

- La série $\sum_{n\ge0}n$ diverge grossièrement.
- Les séries géométriques $\sum_{n\ge0}q^n$ avec $|q|\ge1$ divergent grossièrement.
- La série harmonique $\sum_{n\ge1}\frac1n$ diverge mais **pas** grossièrement.

> ⚠️ **Attention : la CN n'est pas suffisante.**
> $\displaystyle\lim_{n\to+\infty}u_n=0\ \not\Rightarrow\ \sum_{n\in\mathbb{N}}u_n\ \text{CV}$.

## Structure algébrique

**Prop. (opérations sur les séries numériques CV).** Soient $\sum u_n$, $\sum v_n$ et $\lambda\in\mathbb{K}$.

- **Addition** : $\sum_{n\in\mathbb{N}}u_n+\sum_{n\in\mathbb{N}}v_n=\sum_{n\in\mathbb{N}}(u_n+v_n)$.
- **Produit externe** : $\lambda\sum_{n\in\mathbb{N}}u_n=\sum_{n\in\mathbb{N}}(\lambda u_n)$.
- **Produit interne (produit de Cauchy)** :
  $$\left(\sum_{n\in\mathbb{N}}u_n\right)\times\left(\sum_{n\in\mathbb{N}}v_n\right)=\sum_{n\in\mathbb{N}}w_n\quad\text{avec}\quad\forall n\in\mathbb{N},\ w_n=\sum_{k=0}^{n}u_kv_{n-k}.$$

> **Théorème.** Soient $\sum_{n\in\mathbb{N}}u_n$ et $\sum_{n\in\mathbb{N}}v_n$ deux séries numériques et $\lambda\in\mathbb{K}$.
> Si $\sum u_n$ et $\sum v_n$ convergent alors la série $\sum(\lambda u_n+v_n)$ converge aussi, et
> $$\sum_{n=0}^{+\infty}(\lambda u_n+v_n)=\lambda\sum_{n=0}^{+\infty}u_n+\sum_{n=0}^{+\infty}v_n.$$

**Nature d'une addition de séries :**

| $\sum u_n$ | $\sum v_n$ | $\sum(u_n+v_n)$ |
|---|---|---|
| CV | CV | CV |
| CV | DV | DV |
| DV | DV | ? |

**Exemple** (cas « DV + DV ») : $\sum_{n\in\mathbb{N}}1$ DV et $\sum_{n\in\mathbb{N}}(-1)$ DV, mais $\sum_{n\in\mathbb{N}}\big((-1)+1\big)=\sum_{n\in\mathbb{N}}0$ CV (série nulle).

**Propriété.** Si $\sum u_n$ CV et $\forall n,\ u_n\ge0$ alors $\displaystyle\sum_{n=0}^{+\infty}u_n\ge0$.

**Propriété.** Si $\sum u_n$ et $\sum v_n$ CV et $\forall n,\ u_n\le v_n$ alors $\displaystyle\sum_{n=0}^{+\infty}u_n\le\sum_{n=0}^{+\infty}v_n$.

**Propriété (séries à valeurs complexes).** Soit $\sum_{n\in\mathbb{N}}u_n$ une série numérique avec $\forall n\in\mathbb{N},\ u_n=a_n+ib_n$, où $a_n,b_n\in\mathbb{R}$.
$$\sum u_n\ \text{CV}\iff\sum a_n\ \text{et}\ \sum b_n\ \text{CV}.$$
Si c'est le cas : $\displaystyle\sum_{n=0}^{+\infty}u_n=\sum_{n=0}^{+\infty}a_n+i\sum_{n=0}^{+\infty}b_n$.

---

# II. Séries numériques à termes positifs (SNTP)

## 1) Lemme fondamental

> **Définition.** $\sum_{n\in\mathbb{N}}u_n$ est une **série numérique à termes positifs (SNTP)** si $\forall n\in\mathbb{N},\ u_n\ge0$.

**Lemme fondamental.** Soit $\sum u_n$ une SNTP, alors sa suite de sommes partielles $(S_n)$ est **croissante**.

*Preuve.* $\forall n\in\mathbb{N},\ S_{n+1}-S_n=\sum_{k=0}^{n+1}u_k-\sum_{k=0}^{n}u_k=u_{n+1}\ge0$, donc $(S_n)$ est croissante. $\square$

> **Théorème.** Soit $\sum u_n$ une SNTP.
> $$\sum_{n\in\mathbb{N}}u_n\ \text{CV}\iff\text{la suite des sommes partielles est majorée}\iff\exists M>0,\ \forall n\in\mathbb{N},\ \sum_{k=0}^{n}u_k\le M.$$

*Preuve.*
- $\Rightarrow$ : si $\sum u_n$ CV alors $(S_n)$ converge donc elle est bornée.
- $\Leftarrow$ : si $(S_n)$ est majorée et croissante (car $\sum u_n$ est une SNTP, lemme fondamental), alors elle converge donc $\sum u_n$ CV. $\square$

**Prop.** Soit $\sum u_n$ une SNTP.
- Si $\sum u_n$ CV, alors $\forall n\in\mathbb{N},\ S_n=\sum_{k=0}^{n}u_k\le\sum_{n=0}^{+\infty}u_n$.
- Si $\sum u_n$ DV, alors $\displaystyle\lim_{n\to+\infty}S_n=+\infty$.

## 2) Théorème de majoration

> **Théorème.** Soient $\sum u_n$ et $\sum v_n$ deux SNTP. Si
> - $u_n\le v_n\ \ \forall n\in\mathbb{N}$ (ou $\exists n_0\in\mathbb{N},\ \forall n\ge n_0$),
> - $\sum v_n$ CV,
>
> alors $\sum u_n$ CV.

> **Corollaire.** Soient $\sum u_n$ et $\sum v_n$ deux SNTP.
> - Si $u_n=O(v_n)$ et $\sum v_n$ CV alors $\sum u_n$ CV.
> - Si $u_n=o(v_n)$ et $\sum v_n$ CV alors $\sum u_n$ CV.

*Preuve.* Si $\forall n\in\mathbb{N},\ u_k\le v_k$ alors on peut sommer : $\forall n,\ \sum_{k=0}^{n}u_k\le\sum_{k=0}^{n}v_k$. De plus $\sum v_n$ CV donc $\forall n,\ \sum_{k=0}^{n}v_k\le\sum_{n=0}^{+\infty}v_n=S$. Ainsi, $\forall n,\ \sum_{k=0}^{n}u_k\le S$. Par le lemme fondamental des SNTP, $\sum u_n$ CV. $\square$

## 3) Théorème de minoration

> **Théorème.** Soient $\sum u_n$ et $\sum v_n$ deux SNTP. Si
> - $u_n\ge v_n\ \ \forall n\in\mathbb{N}$,
> - $\sum v_n$ DV,
>
> alors $\sum u_n$ DV.

> **Corollaire.** Soient $\sum u_n$ et $\sum v_n$ deux SNTP.
> - Si $v_n=O(u_n)$ et $\sum v_n$ DV alors $\sum u_n$ DV.
> - Si $v_n=o(u_n)$ et $\sum v_n$ DV alors $\sum u_n$ DV.

*Preuve.* Si $\forall n,\ u_n\ge v_n$ alors on peut sommer : $\forall n,\ \sum_{k=0}^{n}u_k\ge\sum_{k=0}^{n}v_k$. Si $\sum v_n$ DV alors $\lim\sum_{k=0}^{n}v_k=+\infty$ (car SNTP). En passant à la limite on en déduit que $\lim\sum_{k=0}^{n}u_k=+\infty$ donc $\sum u_n$ DV. $\square$

## 4) Théorème d'équivalence

> **Théorème.** Soient $\sum u_n$ et $\sum v_n$ deux séries numériques. Si
> - $u_n\underset{n\to+\infty}{\sim}v_n$,
> - $(v_n)$ est **de signe constant à partir d'un certain rang**,
>
> alors $\sum u_n$ et $\sum v_n$ ont la même nature.
> (Alors $(u_n)$ est aussi de signe constant.)

*Preuve.* Soient $\sum u_n$ et $\sum v_n$ deux séries numériques telles que $u_n\sim v_n$ et $v_n\ge0\ \forall n\in\mathbb{N}$ (preuve identique dans le cas $n\ge n_0$ et/ou $v_n\le0$).

Puisque $u_n\sim v_n$, on sait qu'il existe $n_0\in\mathbb{N}$ et $\lambda,\Lambda>0$ tels que $\forall n\ge n_0,\ \lambda v_n\le u_n\le\Lambda v_n$.

Montrons que $\sum u_n$ a la même nature que $\sum v_n$ (la réciproque est vraie par symétrie des hypothèses) :
- Si $\sum v_n$ CV, comme on a $u_n\le\Lambda v_n$ et $v_n\ge0$, par le théorème de majoration $\sum u_n$ CV.
- Si $\sum v_n$ DV, comme on a $u_n\ge\lambda v_n$ et $v_n\ge0$, par le théorème de minoration $\sum u_n$ DV.

Donc $\sum u_n$ a la même nature que $\sum v_n$. $\square$

**Propriété.** Soient $\sum u_n$ et $\sum v_n$ telles que $u_n\underset{n\to+\infty}{\sim}v_n$ et $(v_n)$ de signe constant à partir d'un certain rang. Alors :
- Si $\sum u_n$ (et $\sum v_n$) CV, alors $\displaystyle\sum_{k=n+1}^{+\infty}u_k\underset{n\to+\infty}{\sim}\sum_{k=n+1}^{+\infty}v_k$ (équivalence des restes).
- Si $\sum u_n$ (et $\sum v_n$) DV, alors $\displaystyle\sum_{k=0}^{n}u_k\underset{n\to+\infty}{\sim}\sum_{k=0}^{n}v_k$ (équivalence des sommes partielles).

## 5) Séries de référence

### Séries géométriques

> **Définition.** On appelle **géométrique** les séries $\sum u_n$ de terme général $u_n=z^n$, $z\in\mathbb{C}$.
> **Prop.** Une série géométrique converge ssi $|z|<1$.

### Séries de Riemann

> **Définition.** On appelle **série de Riemann** les séries $\sum_{n\ge1}u_n$ de terme général $\forall n\ge1,\ u_n=\dfrac1{n^\alpha}$, $\alpha\in\mathbb{R}$.

> **Théorème.** Une série de Riemann $\sum_{n\ge1}\dfrac1{n^\alpha}$ converge si et seulement si $\alpha>1$.

*Preuve (d'après les photos de tableau).*
- **Cas $\alpha\le1$** : $\forall n\ge1,\ \frac1{n^\alpha}\ge\frac1n$ et $\sum\frac1n$ est une SNTP divergente, donc par le théorème de minoration, la série $\sum\frac1{n^\alpha}$ diverge.
- **Cas $\alpha>1$** : on note $f:x\mapsto\frac1{x^\alpha}$, décroissante sur $\mathbb{R}_+^*$. Donc $\forall k\ge2,\ \forall x\in[k-1,k],\ f(x)\ge f(k)$. En intégrant sur $[k-1,k]$ : $\int_{k-1}^{k}f(x)\,dx\ge\frac1{k^\alpha}$. En sommant pour $k\in[\![2,n]\!]$ :
  $$\sum_{k=2}^{n}\frac1{k^\alpha}\le\int_1^{n}\frac1{x^\alpha}\,dx=\left[\frac{x^{1-\alpha}}{1-\alpha}\right]_1^n=\frac1{\alpha-1}\left(1-\frac1{n^{\alpha-1}}\right)\le\frac1{\alpha-1}.$$
  La suite des sommes partielles est donc majorée ; comme $\sum\frac1{n^\alpha}$ est une SNTP, elle converge. $\square$

> **Lemme de Riemann.** Soit $\sum u_n$ une SNTP.
> - S'il existe $\alpha>1$ tel que $\displaystyle\lim_{n\to+\infty}n^\alpha u_n=0$, alors $\sum u_n$ CV.
> - S'il existe $\alpha\le1$ tel que $\displaystyle\lim_{n\to+\infty}n^\alpha u_n=+\infty$, alors $\sum u_n$ DV.

### Séries de Bertrand

> **Théorème.** La série de Bertrand $\displaystyle\sum\frac1{n^\alpha(\ln n)^\beta}$ converge ssi $\alpha>1,\ \forall\beta\in\mathbb{R}$, ou $\alpha=1$ et $\beta>1$.

## 6) Règles de convergence

### A. Règle de d'Alembert

> **Théorème.** Soit $\sum u_n$ une SNTP telle que les $u_n$ sont tous non nuls à partir d'un certain rang ($\exists n_0\in\mathbb{N},\ \forall n\ge n_0,\ u_n\ne0$).
> - Si $\displaystyle\lim_{n\to+\infty}\left|\frac{u_{n+1}}{u_n}\right|=\ell<1$ alors $\sum u_n$ CV.
> - Si $\displaystyle\lim_{n\to+\infty}\left|\frac{u_{n+1}}{u_n}\right|=\ell>1$ alors $\sum u_n$ DV.
> - Si $\displaystyle\lim_{n\to+\infty}\left|\frac{u_{n+1}}{u_n}\right|=1$ on ne peut rien dire.

*Intuition.* Si $\forall n,\ \frac{u_{n+1}}{u_n}=\ell$ alors $u_{n+1}=\ell u_n$, d'où $u_n=\ell^nu_0$ : on se ramène à une série géométrique.

*Preuve.* On distingue trois cas : $\ell<1$, $\ell>1$ et $\ell=+\infty$.

- **Cas $\ell<1$.** Par hypothèse $\lim\left|\frac{u_{n+1}}{u_n}\right|=\ell$ donc $\forall\varepsilon>0,\ \exists N\in\mathbb{N},\ \forall n\ge N,\ \ell-\varepsilon<\left|\frac{u_{n+1}}{u_n}\right|<\ell+\varepsilon$.
  On prend $\varepsilon=\frac{1-\ell}{2}$ : il existe un rang $N$ tel que $\forall n\ge N$,
  $$u_{n+1}<\left(\ell+\frac{1-\ell}{2}\right)u_n=\frac{\ell+1}{2}\,u_n,\qquad\text{où }\frac{\ell+1}{2}<1\text{ car }\ell<1.$$
  On montre par récurrence que $\forall n\ge N,\ u_n\le\left(\frac{\ell+1}{2}\right)^{n-N}u_N$. On reconnaît la série géométrique $\sum_{n\ge N}\left(\frac{\ell+1}{2}\right)^{n-N}u_N$ qui est CV puisque $\frac{\ell+1}{2}<1$. Donc par le théorème de majoration, $\sum u_n$ CV.

- **Cas $\ell>1$.** Par hypothèse $\lim\left|\frac{u_{n+1}}{u_n}\right|=\ell$ donc $\forall\varepsilon>0,\ \exists N,\ \forall n\ge N,\ \ell-\varepsilon<\left|\frac{u_{n+1}}{u_n}\right|<\ell+\varepsilon$.
  On prend $\varepsilon=\frac{\ell-1}{2}>0$ : $\exists N,\ \forall n\ge N,\ \ell-\frac{\ell-1}{2}<\frac{u_{n+1}}{u_n}$, où $\frac{\ell+1}{2}>1$ car $\ell>1$.
  On montre par récurrence que $\forall n\ge N,\ u_n\ge\left(\frac{\ell+1}{2}\right)^{n-N}u_N$, et on reconnaît la série géométrique $\sum\left(\frac{\ell+1}{2}\right)^{n-N}u_N$ qui diverge. Donc par le théorème de minoration, $\sum u_n$ DV.

- **Cas $\ell=+\infty$.** Par hypothèse $\lim\left|\frac{u_{n+1}}{u_n}\right|=+\infty$ donc $\forall M>0,\ \exists N\in\mathbb{N},\ \forall n\ge N,\ \left|\frac{u_{n+1}}{u_n}\right|>M$. Prenons $M=2$ : $\exists N,\ \forall n\ge N,\ u_{n+1}>2u_n$. On en déduit par récurrence que $u_n\ge2^{\,n-N}u_N$, etc. $\square$

**Exemple.** $\sum_{n\ge0}u_n$ avec $u_n=\dfrac{n+2}{n!}$. On a $u_n\ne0\ \forall n$ et
$$\lim_{n\to+\infty}\left|\frac{u_{n+1}}{u_n}\right|=\lim\frac{\frac{n+3}{(n+1)!}}{\frac{n+2}{n!}}=\lim\frac{n+3}{n+2}\times\frac{n!}{(n+1)!}=\lim\frac{n+3}{n+2}\times\frac1{n+1}=0<1.$$
Donc par la règle de d'Alembert, $\sum u_n$ CV.

### B. Règle de Cauchy

> **Théorème.** Soit $\sum u_n$ une SNTP.
> - Si $\displaystyle\lim_{n\to+\infty}\sqrt[n]{|u_n|}=\ell<1$ alors $\sum u_n$ CV.
> - Si $\displaystyle\lim_{n\to+\infty}\sqrt[n]{|u_n|}=\ell>1$ alors $\sum u_n$ DV.
> - Si $\displaystyle\lim_{n\to+\infty}\sqrt[n]{|u_n|}=1$ alors on ne peut pas conclure.

*Preuve (cas $\ell<1$).* Par hypothèse, $\forall\varepsilon>0,\ \exists N\in\mathbb{N},\ \forall n\ge N,\ \ell-\varepsilon<\sqrt[n]{|u_n|}<\ell+\varepsilon$, donc $|u_n|<(\ell+\varepsilon)^n$. On prend $\varepsilon=\frac{1-\ell}{2}$ : $|u_n|<\left(\frac{\ell+1}{2}\right)^n$ avec $\frac{\ell+1}{2}<1$. On reconnaît une série géométrique convergente donc, par le théorème de majoration, $\sum u_n$ CV. Les cas $\ell>1$ et $\ell=+\infty$ sont laissés **en exercice**.

**Exemples**

- $\sum u_n$ avec $u_n=\left(\frac12+\frac1{n^2}\right)^n$. On utilise la règle de Cauchy : $\displaystyle\lim\sqrt[n]{|u_n|}=\lim\left(\frac12+\frac1{n^2}\right)=\frac12<1$ donc $\sum u_n$ CV.
- Séries de Riemann $\sum_{n\ge1}\frac1{n^\alpha}$, $\alpha\in\mathbb{R}$ : on a $\displaystyle\lim\sqrt[n]{\frac1{n^\alpha}}=\lim n^{-\alpha/n}=\lim e^{-\frac\alpha n\ln n}=1$, on ne peut pas conclure par la règle de Cauchy.

### Comparaison de deux règles

> **Lemme.** Soit $\sum u_n$ une SNTP avec $u_n\ne0\ \forall n\in\mathbb{N}$.
> Si $\displaystyle\lim_{n\to+\infty}\left|\frac{u_{n+1}}{u_n}\right|=\ell$ alors $\displaystyle\lim_{n\to+\infty}\sqrt[n]{|u_n|}=\ell$ (la réciproque est **fausse**).

**Exemple.** $\sum u_n$ avec $u_n=2^{-n+(-1)^n}$.

- **Cauchy** : $\displaystyle\lim\sqrt[n]{u_n}=\lim2^{-1+\frac{(-1)^n}{n}}=\frac12<1$, donc $\sum u_n$ CV par la règle de Cauchy.
- **d'Alembert** ($u_n\ne0\ \forall n$) :
  $$\frac{u_{n+1}}{u_n}=\frac{2^{-(n+1)+(-1)^{n+1}}}{2^{-n+(-1)^n}}=\frac12\cdot2^{(-1)^{n+1}-(-1)^n}=\frac12\,2^{2(-1)^{n+1}}.$$
  Si $n$ est pair : $\frac{u_{n+1}}{u_n}=\frac12\times2^{-2}=\frac18$. Si $n$ est impair : $\frac{u_{n+1}}{u_n}=\frac12\times2^{2}=2$.
  Donc la suite $\left(\frac{u_{n+1}}{u_n}\right)$ diverge : la règle de d'Alembert ne permet pas de conclure.

---

# III. Séries numériques à termes quelconques

On considère une série numérique $\sum u_n$ avec $u_n\in\mathbb{R}\ \ \forall n\in\mathbb{N}$.

## 1) Convergence absolue et semi-convergence

> **Définition.** On dit qu'une série $\sum u_n$ **converge absolument (CVA)** si $\sum|u_n|$ converge.

> **Prop.** Si $\sum u_n$ CVA alors $\sum u_n$ CV. De plus, $\displaystyle\left|\sum_{n=0}^{+\infty}u_n\right|\le\sum_{n=0}^{+\infty}|u_n|$.

**Exemple.** $\sum_{n\ge1}\dfrac{(-1)^n}{n}$ CV mais ne CVA pas (car $\sum|u_n|=\sum\frac1n$ est la série harmonique, qui diverge).

> **Définition.** On dit qu'une série numérique $\sum u_n$ est **semi-convergente** si elle converge mais ne converge pas absolument.

**Exemple.** $\sum_{n\ge1}\dfrac{(-1)^n}{n}$ est semi-convergente.

> **Prop.** L'ensemble des séries absolument convergentes forme un sous-espace vectoriel (strict) de l'ensemble des séries convergentes.

> **Prop.** Soient $\sum u_n$ et $\sum v_n$ deux séries numériques. Si
> - $\sum u_n$ et $\sum v_n$ convergent,
> - au moins l'une des deux converge absolument,
>
> alors le produit de Cauchy $\sum w_n$ converge (avec $w_n=\sum_{k=0}^{n}u_kv_{n-k}$) et
> $$\sum_{n=0}^{+\infty}w_n=\left(\sum u_n\right)\times\left(\sum v_n\right).$$

*Preuve : admise.*

## 2) Étude de convergence absolue

Étudier la convergence absolue d'une série numérique à termes quelconques $\sum u_n$ revient à étudier la convergence de la série à termes positifs $\sum|u_n|$.

**Outils d'étude :**
- Théorèmes de comparaison ($|u_n|\le v_n$ ou $|u_n|\sim v_n$, …) ;
- Lemme de Riemann ($\lim n^\alpha|u_n|$) ;
- Règles de d'Alembert et de Cauchy.

**Remarque.** Soit $\sum u_n$ une série num. Si $\lim\left|\frac{u_{n+1}}{u_n}\right|=\ell<1$, alors par la règle de d'Alembert $\sum u_n$ CVA.

## 3) Étude de la semi-convergence

> **Définition.** On dit qu'une série $\sum u_n$ est **alternée** s'il existe $n_0\in\mathbb{N}$ tel que $\forall n\ge n_0,\ u_n=(-1)^n|u_n|$ ou $u_n=(-1)^{n+1}|u_n|$.

> **Théorème (Théorème Spécial des Séries Alternées, TSSA).** Soit $\sum u_n$ une série alternée. Si
> - $(|u_n|)_{n\in\mathbb{N}}$ est décroissante,
> - $\displaystyle\lim_{n\to+\infty}u_n=0$,
>
> alors $\sum u_n$ converge.
>
> Dans ce cas (si $\sum u_n$ CV) on a :
> - $\forall n\in\mathbb{N},\ R_n$ est de même signe que $u_{n+1}$ ;
> - $\forall n\in\mathbb{N},\ |R_n|\le|u_{n+1}|$.
>
> ($R_n$ : reste de rang $n$, $R_n=\sum_{k=n+1}^{+\infty}u_k$.)

**Théorème des suites adjacentes (rappel).** Soient $(u_n)$ et $(v_n)$ deux suites telles que $(u_n)\searrow$, $(v_n)\nearrow$, $\forall n,\ u_n\ge v_n$ et $\lim|u_n-v_n|=0$. Alors $(u_n)$ et $(v_n)$ convergent et $\lim u_n=\lim v_n$.

**Exemple traité en cours (tableau).** $\sum_{n\ge1}\frac{(-1)^n}{n}$ : on montre que $(S_{2n})$ et $(S_{2n+1})$ sont adjacentes.
- $\forall n\ge1,\ S_{2(n+1)}-S_{2n}=\frac{(-1)^{2n+1}}{2n+1}+\frac{(-1)^{2n+2}}{2n+2}=-\frac1{2n+1}+\frac1{2n+2}<0$ car $\frac1{2n+1}>\frac1{2n+2}$, donc $(S_{2n})$ est décroissante.
- $\forall n\ge0,\ S_{2(n+1)+1}-S_{2n+1}=\frac{(-1)^{2n+2}}{2n+2}+\frac{(-1)^{2n+3}}{2n+3}=\frac1{2n+2}-\frac1{2n+3}>0$, donc $(S_{2n+1})$ est croissante.
- $S_{2n}-S_{2n+1}=-\frac{(-1)^{2n+1}}{2n+1}=\frac1{2n+1}\ge0$ donc $S_{2n}\ge S_{2n+1}$, et $\lim|S_{2n}-S_{2n+1}|=\lim\frac1{2n+1}=0$.

Par le théorème des suites adjacentes, $\lim S_{2n}=\lim S_{2n+1}=S$. Comme $\mathbb{N}^*=\{2n,n\ge1\}\cup\{2n+1,n\ge0\}$, $(S_n)$ converge vers $S$, c.-à-d. $\sum_{n\ge1}\frac{(-1)^n}{n}$ converge.

*Preuve du TSSA.* On note $(S_n)$ la suite des sommes partielles $S_n=\sum_{k=0}^{n}u_k$. On va montrer que $(S_{2n})$ et $(S_{2n+1})$ sont adjacentes dans le cas où $\forall n,\ u_n=(-1)^n|u_n|$ (le cas $u_n=(-1)^{n+1}|u_n|$ ou celui où l'alternance commence à un rang $n_0$ sont similaires).

- **Monotonie de $(S_{2n})$** : $\forall n,\ S_{2(n+1)}-S_{2n}=u_{2n+1}+u_{2n+2}$. On sait que $u_{2n+1}\le0$, $u_{2n+2}\ge0$ et que $(|u_n|)$ est décroissante donc $|u_{2n+1}|\ge|u_{2n+2}|$, donc $S_{2n+2}-S_{2n}=-|u_{2n+1}|+|u_{2n+2}|\le0$ : $(S_{2n})$ est décroissante.
- **Monotonie de $(S_{2n+1})$** : $\forall n,\ S_{2(n+1)+1}-S_{2n+1}=u_{2n+2}+u_{2n+3}$ où $u_{2n+2}\ge0$, $u_{2n+3}\le0$ et $|u_{2n+3}|\le|u_{2n+2}|$ donc $S_{2(n+1)+1}-S_{2n+1}=|u_{2n+2}|-|u_{2n+3}|\ge0$ : $(S_{2n+1})$ est croissante.
- $\lim(S_{2n+1}-S_{2n})=\lim u_{2n+1}=0$.

**Conclusion** : $(S_{2n})$ et $(S_{2n+1})$ sont adjacentes donc elles convergent et ont la même limite $S\in\mathbb{R}$. Comme $\mathbb{N}=\{2n,n\in\mathbb{N}\}\cup\{2n+1,n\in\mathbb{N}\}$, on conclut que $(S_n)$ converge donc $\sum u_n$ converge.

**Estimation des restes $R_n$.** Par monotonie on sait que $\forall n,\ S_{2n+1}\le S\le S_{2n}$. Par conséquent, $\forall n$ :
- $R_{2n}=S-S_{2n}\le0$ et on a $u_{2n+1}\le0$ car $2n+1$ est impair ;
- $R_{2n+1}=S-S_{2n+1}\ge0$ et on a $u_{2n+2}\ge0$ car $2n+2$ est pair ;

donc on a bien $R_n$ du même signe que $u_{n+1}$. De plus, toujours avec l'encadrement $S_{2n+1}\le S\le S_{2n}$ :
- $|R_{2n}|=|S-S_{2n}|=S_{2n}-S\le S_{2n}-S_{2n+1}=|u_{2n+1}|$ ;
- $|R_{2n+1}|=|S-S_{2n+1}|=S-S_{2n+1}\le S_{2n+2}-S_{2n+1}=|u_{2n+2}|$.

### Séries de Riemann alternées

> **Définition.** On appelle **séries de Riemann alternées** les séries numériques de la forme $\displaystyle\sum\frac{(-1)^n}{n^\alpha}$ avec $\alpha\in\mathbb{R}$.

> **Théorème.** Une série de Riemann alternée converge ssi $\alpha>0$ *(cf. remarque ci-dessous)*.

*Preuve.*
- Si $\alpha\le0$ la suite $(u_n)$ ne tend pas vers $0$ donc la série diverge (grossièrement).
- Si $\alpha>1$ alors la série converge absolument.
- Si $0<\alpha\le1$ alors on peut utiliser le TSSA :
  - $\sum u_n$ est alternée puisque $|u_n|=\frac1{n^\alpha}$ donc $u_n=(-1)^n|u_n|$ ;
  - la suite $(|u_n|)_{n\in\mathbb{N}}$, c.-à-d. $\left(\frac1{n^\alpha}\right)_n$, est décroissante car les fonctions $x\mapsto\frac1{x^\alpha}$ pour $\alpha>0$ sont décroissantes sur $\mathbb{R}_+^*$ ;
  - $\lim u_n=\lim\frac{(-1)^n}{n^\alpha}=0$ car $\alpha>0$.

  Conclusion : par le TSSA, $\sum_{n\ge1}\frac{(-1)^n}{n^\alpha}$ avec $\alpha>0$ converge.

> **Remarque.** Dans ton cours, l'énoncé du théorème est écrit « ssi $\alpha>1$ », mais la preuve qui suit (et le TSSA) montre la convergence pour tout $\alpha>0$ (absolue si $\alpha>1$, semi-convergence si $0<\alpha\le1$). J'ai corrigé l'énoncé ; à vérifier avec le prof.

### Règle d'Abel

> **Théorème (règle d'Abel).** Soient $(\varepsilon_n)_{n\in\mathbb{N}}$ et $(v_n)_{n\in\mathbb{N}}$ deux suites numériques. Si
> - $(\varepsilon_n)$ est une suite de réels **positive décroissante** avec $\lim\varepsilon_n=0$,
> - la suite des sommes partielles $\left(\sum_{k=0}^{n}v_k\right)_{n\in\mathbb{N}}$ est **bornée**,
>
> alors la série $\sum_{n\in\mathbb{N}}\varepsilon_nv_n$ converge.

**Remarque.** Le TSSA est le cas particulier de la règle d'Abel avec $v_n=(-1)^n$ et $\varepsilon_n=|u_n|$.

*Preuve.* On note $V_n=\sum_{k=0}^{n}v_k$ ; par hypothèse $\exists M>0$ tel que $\forall n\in\mathbb{N},\ |V_n|\le M$. On remarque que $\forall k\in\mathbb{N}^*,\ v_k=V_k-V_{k-1}$ et on en déduit (**transformation d'Abel**) :
$$\sum_{k=1}^{n}\varepsilon_kv_k=\sum_{k=1}^{n}\varepsilon_k(V_k-V_{k-1})=\sum_{k=1}^{n}\varepsilon_kV_k-\sum_{k=0}^{n-1}\varepsilon_{k+1}V_k=\varepsilon_nV_n-\varepsilon_1V_0+\sum_{k=1}^{n-1}(\varepsilon_k-\varepsilon_{k+1})V_k.$$

- D'une part, $\lim(\varepsilon_nV_n-\varepsilon_1V_0)=-\varepsilon_1V_0$, car $(V_n)$ est bornée et $\varepsilon_n\to0$.
- D'autre part, montrons la CVA de $\sum(\varepsilon_k-\varepsilon_{k+1})V_k$ : comme $(\varepsilon_n)$ est décroissante,
  $$\sum_{k=1}^{n}|(\varepsilon_k-\varepsilon_{k+1})V_k|\le\sum_{k=1}^{n}(\varepsilon_k-\varepsilon_{k+1})M=M\left(\sum_{k=1}^{n}\varepsilon_k-\sum_{k=1}^{n}\varepsilon_{k+1}\right)=M(\varepsilon_1-\varepsilon_{n+1})\le M\varepsilon_1.$$
  Donc les sommes partielles de la SNTP $\sum|(\varepsilon_k-\varepsilon_{k+1})V_k|$ sont bornées par $M\varepsilon_1$ ; par le lemme fondamental des SNTP, cette série converge. On en déduit que $\sum(\varepsilon_k-\varepsilon_{k+1})V_k$ converge.

Par somme de suites convergentes, $\sum_{n\in\mathbb{N}}\varepsilon_nv_n$ converge. $\square$

**Exemple.** Étude de $\displaystyle\sum_{n}\frac{\cos(n^{?})}{n}$ *(exposant illisible sur le scan ; très probablement $\sum\frac{\cos n}{n}$, avec $\varepsilon_n=\frac1n$ et $v_n=\cos n$)*.

### Critère de Cauchy

> **Théorème (critère de Cauchy).** Soit $\sum u_n$ une série numérique. $\sum u_n$ CV ssi
> $$\forall\varepsilon>0,\ \exists N\in\mathbb{N},\ \forall p,q>N,\ p\le q:\ |S_q-S_p|<\varepsilon,$$
> c.-à-d. $\displaystyle\left|\sum_{k=p+1}^{q}u_k\right|<\varepsilon$.

### Remarque : regroupement de termes

> ⚠️ **On ne peut pas déterminer la nature d'une série en regroupant des termes.**

**Exemple.** Pour la série $\sum_{n\ge0}(-1)^n$, $u_n=(-1)^n$ : $\sum_{k=0}^{n}u_k=\underbrace{1-1}_{0}+\underbrace{1-1}_{0}+\cdots$.
On pourrait vouloir définir $v_n=u_{2n}+u_{2n+1}$ et penser que $\sum v_n$ et $\sum u_n$ sont similaires. **C'est faux** : $\forall n,\ v_n=0$ donc $\sum v_n=0$ CV, or $(u_n)$ diverge donc $\sum u_n$ DVG (diverge grossièrement).

---

# IV. Méthodes d'évaluation

## 1) Télescopage

> **Prop.** Soit $(u_n)$ une suite numérique et $\forall n\ge n_0,\ v_n=u_{n+1}-u_n$.
> La série $\sum_{n\ge n_0}v_n$ converge ssi la suite $(u_n)$ converge, et on a
> $$\sum_{n=n_0}^{+\infty}v_n=\lim_{n\to+\infty}u_n-u_{n_0}.$$

*Preuve.* Pour tout $n\ge n_0$ :
$$\sum_{k=n_0}^{n}v_k=\sum_{k=n_0}^{n}(u_{k+1}-u_k)=\sum_{k=n_0}^{n}u_{k+1}-\sum_{k=n_0}^{n}u_k=\sum_{k=n_0+1}^{n+1}u_k-\sum_{k=n_0}^{n}u_k=u_{n+1}-u_{n_0}.$$
On retrouve le résultat en passant à la limite. $\square$

## 2) Comparaison série-intégrale

Soit $\sum_{n\in\mathbb{N}}u_n$ une série numérique et $f:\mathbb{R}_+\to\mathbb{R}$ telle que $\forall n\in\mathbb{N},\ f(n)=u_n$.
*Exemple* : si $u_n=\dfrac{n^2+e^{-n}}{2n+3}$, on prend $f:x\mapsto\dfrac{x^2+e^{-x}}{2x+3}$.

Si $f$ est **monotone** sur un intervalle $[n_0,+\infty[$, $n_0\in\mathbb{N}$, alors on peut comparer les sommes partielles de $\sum u_n$ avec des intégrales de $f$.

**Cas où $f$ est décroissante.** $\forall k\ge2,\ \forall x\in[k-1,k],\ f(k)\le f(x)\le f(k-1)$ ; en intégrant sur l'intervalle de longueur $1$ :
$$\int_k^{k+1}f(x)\,dx\le u_k\le\int_{k-1}^{k}f(x)\,dx.$$
En sommant pour $k$ de $2$ à $n$ et avec la relation de Chasles :
$$\int_2^{n+1}f(x)\,dx\le\sum_{k=2}^{n}u_k\le\int_1^{n}f(x)\,dx.$$
Notons $F$ une primitive de $f$ ; on a alors $F(n+1)-F(2)\le\sum_{k=2}^{n}u_k\le F(n)-F(1)$.

On peut en déduire que :
- Si $\displaystyle\lim_{n\to+\infty}F(n)=+\infty$ alors $\sum_{n\ge2}u_n$ DV (la suite des sommes partielles est minorée par une fonction qui diverge vers $+\infty$).
- Si $\displaystyle\lim_{n\to+\infty}F(n)=\ell\in\mathbb{R}$ alors $\sum_{n\ge2}u_n$ CV (suite des sommes partielles monotone à partir d'un certain rang, car $f$ monotone, et bornée).
  Dans ce cas on a aussi une estimation de la somme :
  $$\ell-F(2)\le\sum_{n=2}^{+\infty}u_n\le\ell-F(1).$$

**Remarques.**
- Dans le cas $\lim F(n)=+\infty$ on a aussi un équivalent $S_n\underset{n\to+\infty}{\sim}F(n)$ (pour la série harmonique : $\sum_{k=1}^{n}\frac1k\sim\ln n$).
- Dans le cas $\lim F(n)=\ell\in\mathbb{R}$ on a $R_n=\sum_{k=n+1}^{+\infty}u_k\underset{n\to+\infty}{\sim}\ell-F(n)$.

## 3) Valeur approchée de la somme

**Question.** Si $\sum_{n\ge0}u_n$ CV et $\sum_{n=0}^{+\infty}u_n=S\in\mathbb{R}$, combien de termes de $(u_n)$ faut-il sommer pour obtenir une valeur approchée de $S$ à $10^{-p}$ près ($p\in\mathbb{N}$) ?

### Cas des séries alternées

Si $\sum u_n$ est alternée et CV, on sait par le TSSA que $|R_n|\le|u_{n+1}|$. Donc il faut sommer jusqu'à $u_n$ tel que $|u_{n+1}|<10^{-p}$.

**Exemple.** $\sum_{n\ge1}\frac{(-1)^n}{n^2}$ CV ; on note $S=\sum_{n=1}^{+\infty}\frac{(-1)^n}{n^2}$. Si on veut une valeur approchée de $S$ à $10^{-4}$ près, on cherche $n$ tel que $\left|\frac{(-1)^n}{n^2}\right|\le10^{-4}$, c.-à-d. $n^2\ge10^4\iff n\ge10^2$.
→ Si on somme les $100$ premiers termes $\sum_{k=1}^{100}u_k$, on a une valeur approchée à $10^{-4}$ près de $S$.

### Cas du type d'Alembert

Si $\sum u_n$ est une série numérique telle que $u_n>0\ \forall n\ge0$ et qu'il existe $\lambda<1$ et $n_0$ tels que $\forall n\ge n_0,\ 0<\dfrac{u_{n+1}}{u_n}<\lambda$, alors $\sum u_n$ CV et on a :
$$\forall n\ge n_0,\quad R_n\le\frac{u_{n_0}\,\lambda^{\,n+1}}{(1-\lambda)\,\lambda^{\,n_0}}.$$

*Preuve (esquisse).* Par récurrence on montre que $\forall n\ge n_0,\ u_n\le\lambda^{n-n_0}u_{n_0}$, d'où $R_n=\sum_{k\ge n+1}u_k\le u_{n_0}\lambda^{-n_0}\sum_{k\ge n+1}\lambda^k=\dfrac{u_{n_0}\lambda^{n+1}}{(1-\lambda)\lambda^{n_0}}$.

**Exemple.** $\sum_{n\in\mathbb{N}}u_n$, $u_n=\dfrac1{n!}$ : $\sum u_n$ CV et $\sum_{n=0}^{+\infty}u_n=e^1$.
On cherche une valeur approchée de $e$ à $10^{-5}$ près. Pour tout $n\ge0$, $\dfrac{u_{n+1}}{u_n}=\dfrac{n!}{(n+1)!}=\dfrac1{n+1}$. En particulier, pour $\lambda=\frac12$ et $\forall n\ge1$ : $0<\frac{u_{n+1}}{u_n}<\frac12$.
$$R_n\le\frac{u_1\left(\frac12\right)^{n+1}}{\left(1-\frac12\right)\left(\frac12\right)^{1}}=\left(\frac12\right)^{n-1}.$$
Ainsi $R_n<10^{-5}\Leftarrow\dfrac1{2^{n-1}}\le10^{-5}\iff10^5\le2^{n-1}\iff5\ln10\le(n-1)\ln2\iff n\ge1+5\,\dfrac{\ln10}{\ln2}\simeq17{,}6$.
Donc $R_{18}<10^{-5}$.

> *Note : ton cours écrit « $\simeq17{,}5$ » ; la valeur exacte est $\approx17{,}6$, ce qui donne bien $n=18$.*
