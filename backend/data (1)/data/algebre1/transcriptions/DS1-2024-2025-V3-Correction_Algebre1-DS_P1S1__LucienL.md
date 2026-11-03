# Algèbre 1 — DS1 2024–2025, corrigé manuscrit (version 3)

> Source : `PREING1-S1/Algebre1-DS/DS1-2024-2025-V3-Correction_Algebre1-DS_P1S1__LucienL.pdf`, 3 pages. Année et attribution « LucienL » issues du nom du fichier ; aucune date ni signature dans les pages.
> Transcription du 12 octobre 2026 : lecture visuelle intégrale des trois scans ; table de vérité, démonstrations et barème manuscrit restitués. Les énoncés non présents ne sont pas reconstruits.

## Exercice 1 — Logique (page 1)

### 1. Table de vérité

| $P$ | $Q$ | $\neg P$ | $\neg P\Rightarrow Q$ | $P\lor Q$ | $P\land Q$ | $P\lor(P\land Q)$ | $(Q\lor P)\land P$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V | V | F | V | V | V | V | V |
| V | F | F | V | V | F | V | V |
| F | V | V | V | V | F | F | F |
| F | F | V | F | F | F | F | F |

Les quatre colonnes $\neg P\Rightarrow Q$, $P\lor Q$, $P\lor(P\land Q)$ et $(Q\lor P)\land P$ sont chacune affectées de 0,5 point. On a donc :

$$\boxed{(\neg P\Rightarrow Q)\Longleftrightarrow(P\lor Q)}\qquad\text{(0,5 point)},$$

$$\boxed{P\lor(P\land Q)\Longleftrightarrow(Q\lor P)\land P}\qquad\text{(0,5 point)}.$$

### 2. Quantificateurs

$$\exists M>0,\ \forall N\in\mathbb N,\ \exists n\in\mathbb N,\quad(n\geq N\text{ et }u_n\leq M).$$

Barème : 0,5 point pour les quantificateurs, 0,5 point pour les deux conditions.

## Exercice 2 — Factorisation et contraposée (page 1)

### 1. Identité (1 point)

Pour tout $(x,y)\in\mathbb R^2$ :

$$
\begin{aligned}
x(y^2+y+1)-y(x^2+x+1)
&=xy^2+xy+x-yx^2-xy-y\\
&=xy(y-x)+(x-y)\\
&=(y-x)(xy-1).
\end{aligned}
$$

### 2. Implication

Soit $(x,y)\in\mathbb R^2$. Notons $A$ la proposition $x(y^2+y+1)=y(x^2+x+1)$ et $B$ la proposition « $y=x$ ou $xy=1$ ».

Supposons $A$. D’après la question 1 :

$$x(y^2+y+1)=y(x^2+x+1)\ \Longrightarrow\ (y-x)(xy-1)=0\ \Longrightarrow\ y=x\text{ ou }xy=1.$$

Barème : 1,5 point pour cette implication.

Conclusion : par raisonnement direct, on a démontré $A\Rightarrow B$ ; par contraposée, $\overline B\Rightarrow\overline A$, ce qui est la proposition $P(x,y)$ demandée (0,5 point).

## Exercice 3 — Divisibilité par 7 (page 2)

La suite figurant dans les calculs est $A_n=3^{2n+2}-2^{n+1}$.

### 1. Relation entre deux termes

$$
\begin{aligned}
A_{n+1}-2A_n
&=3^{2n+4}-2^{n+2}-2\cdot3^{2n+2}+2^{n+2}\\
&=3^2\cdot3^{2n+2}-2\cdot3^{2n+2}\\
&=(9-2)3^{2n+2}=7\cdot3^{2n+2}.
\end{aligned}
$$

Barème : 0,5 point pour la première ligne, 1 point pour la simplification.

### 2. Récurrence

Pour $n\in\mathbb N$, notons $P_n$ : « $A_n$ est divisible par 7 ».

**Initialisation** (0,5 point). Pour $n=0$, $A_0=3^2-2=7$, divisible par 7. Donc $P_0$ est vraie.

**Hérédité.** Supposons $P_n$ vraie pour un certain $n\in\mathbb N$, c’est-à-dire $\exists k\in\mathbb N,\ A_n=7k$ (0,5 point). Alors, d’après la question 1 :

$$A_{n+1}=2A_n+7\cdot3^{2n+2}=2\times7k+7\cdot3^{2n+2}=7\underbrace{(2k+3^{2n+2})}_{k'}.$$

Donc $A_{n+1}$ est divisible par 7, et $P_{n+1}$ est vraie (1 point).

**Conclusion** (0,5 point). $P_0$ est vraie et, pour tout $n\in\mathbb N$, $P_n\Rightarrow P_{n+1}$. Ainsi $P_n$ est vraie pour tout $n\in\mathbb N$.

## Exercice 4 — Ensembles finis (pages 2–3)

1. (1 point) $B\setminus A=\{1,2,4,6\}$.
2. (1,5 point)

   $$A^c\cup(B\cap C)=\{1,2,4,6,7\}\cup\{2,4,6\}=\{1,2,4,6,7\}.$$

3. (1 point)

   $$A\mathbin{\Delta}B=(A\cup B)\setminus(A\cap B)=\{0,1,2,3,4,5,6\}\setminus\{3,5\}=\{0,1,2,4,6\}.$$

4. (1,5 point)

   $$\mathcal P(A)=\{\varnothing,\{0\},\{3\},\{5\},\{0,3\},\{0,5\},\{3,5\},A\}.$$

## Exercice 5 — Identités ensemblistes (page 3)

1. (1 point pour la distributivité, 1 point pour la conclusion)

   $$(A\cup B)\cap(A\cup B^c)=A\cup(B\cap B^c)=A\cup\varnothing=A.$$

2. (1 point pour le passage aux complémentaires, 1 point pour la conclusion)

   $$
   \begin{aligned}
   A\setminus(B\cup C)
   &=A\cap(B\cup C)^c\\
   &=A\cap(B^c\cap C^c)\\
   &=(A\cap B^c)\cap(A\cap C^c)\\
   &=(A\setminus B)\cap(A\setminus C).
   \end{aligned}
   $$
