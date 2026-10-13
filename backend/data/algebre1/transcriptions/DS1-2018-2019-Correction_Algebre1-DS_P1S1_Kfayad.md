# Algèbre 1 — Corrigé du DS1 du 12 octobre 2018

> Source : `PREING1-S1/Algebre1-DS/DS1-2018-2019-Correction_Algebre1-DS_P1S1_Kfayad.pdf`, 3 pages. Contact du corrigé : karam.fayad@eisti.eu.
> Transcription du 12 octobre 2026 : lecture visuelle intégrale des trois pages et comparaison au texte natif ; négations, table de vérité et formules restituées en Markdown/LaTeX. La notation $\subset$ du document désigne l’inclusion, sans exigence d’inclusion stricte.

## Exercice 1 — Logique et ensembles (page 1)

1. Soient les propositions $A$ : « l’étudiant reçoit une bourse », $B$ : « l’étudiant est bon », $C$ : « l’étudiant est pauvre ». L’énoncé exprime $A\Leftrightarrow B\land C$. Ainsi :

   $$\overline A\Leftrightarrow\overline{B\land C}\Leftrightarrow\overline B\lor\overline C.$$

   Les étudiants qui ne reçoivent pas de bourse sont donc ceux qui ne sont pas bons ou qui ne sont pas pauvres.

2. Avec $A$ : « ils parlent » et $B$ : « ils savent », les affirmations sont $A\Rightarrow\overline B$ et $B\Rightarrow\overline A$. Ces implications sont contraposées l’une de l’autre : elles veulent dire la même chose.

3. La suite $(u_n)_{n\geq0}$ n’est pas convergente si :

   $$\forall L\in\mathbb R,\ \exists\varepsilon>0,\ \forall n_0\in\mathbb N,\ \exists n\in\mathbb N,\quad(n\geq n_0\text{ et }|u_n-L|\geq\varepsilon).$$

4. L’ensemble proposé contient deux éléments : $\{a,\{\triangleright,\circ\},\alpha\}$ et $\star$.

## Exercice 2 — Ou exclusif (pages 1–2)

### 1. Expressions du ou exclusif

a. Table de vérité :

| $P$ | $Q$ | $P\oplus Q$ | $P\lor Q$ | $P\land Q$ | $\overline{P\land Q}$ | $(P\lor Q)\land\overline{P\land Q}$ |
| --- | --- | --- | --- | --- | --- | --- |
| V | V | F | V | V | F | F |
| V | F | V | V | F | V | V |
| F | V | V | V | F | V | V |
| F | F | F | F | F | V | F |

On a bien : $(P\oplus Q)\Leftrightarrow(P\lor Q)\land\overline{P\land Q}$.

b. Par distributivité :

$$
\begin{aligned}
P\oplus Q
&\Leftrightarrow(P\lor Q)\land\overline{P\land Q}\\
&\Leftrightarrow(P\lor Q)\land(\overline P\lor\overline Q)\\
&\Leftrightarrow\underbrace{(P\land\overline P)}_{\text{Faux}}\lor(P\land\overline Q)\lor(Q\land\overline P)\lor\underbrace{(Q\land\overline Q)}_{\text{Faux}}\\
&\Leftrightarrow(P\land\overline Q)\lor(Q\land\overline P).
\end{aligned}
$$

### 2. Propriétés

a. On obtient :

$$
\begin{aligned}
P\oplus P&\Leftrightarrow(P\lor P)\land\overline{P\land P}\Leftrightarrow P\land\overline P\Leftrightarrow\text{Faux},\\
P\oplus\text{Faux}&\Leftrightarrow(P\lor\text{Faux})\land\overline{P\land\text{Faux}}\Leftrightarrow P\land\text{Vrai}\Leftrightarrow P,\\
P\oplus\text{Vrai}&\Leftrightarrow(P\lor\text{Vrai})\land\overline{P\land\text{Vrai}}\Leftrightarrow\text{Vrai}\land\overline P\Leftrightarrow\overline P.
\end{aligned}
$$

D’après la table de vérité, $(P\oplus Q)\oplus Q\Leftrightarrow P$.

b. Remarquons d’abord que :

$$\overline{P\oplus Q}\Leftrightarrow(\overline P\lor Q)\land(\overline Q\lor P)\Leftrightarrow(\overline P\land\overline Q)\lor(P\land Q).$$

D’où :

$$
\begin{aligned}
(P\oplus Q)\oplus R
&\Leftrightarrow((P\oplus Q)\land\overline R)\lor(\overline{P\oplus Q}\land R)\\
&\Leftrightarrow\bigl(((P\land\overline Q)\lor(Q\land\overline P))\land\overline R\bigr)
\lor\bigl(((\overline P\land\overline Q)\lor(P\land Q))\land R\bigr)\\
&\Leftrightarrow(P\land\overline Q\land\overline R)\lor(Q\land\overline P\land\overline R)
\lor(\overline P\land\overline Q\land R)\lor(P\land Q\land R).
\end{aligned}
$$

Remplacer $P$ par $Q$, $Q$ par $R$ et $R$ par $P$ donne une proposition équivalente. Ainsi $(P\oplus Q)\oplus R\Leftrightarrow(Q\oplus R)\oplus P$. Par commutativité de $\oplus$ :

$$\boxed{(P\oplus Q)\oplus R\Leftrightarrow P\oplus(Q\oplus R).}$$

### 3. Lien avec le ou inclusif

Une table de vérité permet de constater que $(P\oplus Q)\oplus(P\land Q)\Leftrightarrow P\lor Q$.

Deuxième méthode :

$$
(P\oplus Q)\oplus(P\land Q)
\Leftrightarrow\bigl((P\oplus Q)\lor(P\land Q)\bigr)\land\overline{(P\oplus Q)\land(P\land Q)}.
$$

Or :

$$
\begin{aligned}
(P\oplus Q)\lor(P\land Q)
&\Leftrightarrow\bigl((P\lor Q)\land\overline{P\land Q}\bigr)\lor(P\land Q)\\
&\Leftrightarrow\bigl((P\lor Q)\lor(P\land Q)\bigr)\land\bigl(\overline{P\land Q}\lor(P\land Q)\bigr)\\
&\Leftrightarrow(P\lor Q)\land\text{Vrai}\Leftrightarrow P\lor Q,
\end{aligned}
$$

et :

$$\overline{(P\oplus Q)\land(P\land Q)}\Leftrightarrow\overline{P\lor Q}\lor(P\land Q)\lor\overline{P\land Q}\Leftrightarrow\text{Vrai}.$$

Conclusion : $(P\oplus Q)\oplus(P\land Q)\Leftrightarrow P\lor Q$.

## Exercice 3 — Récurrence double (page 2)

Pour $n\in\mathbb N$, notons $P_n$ la propriété $u_n=(-2)^n+3^n$. On procède par récurrence double.

**Initialisation.** $(-2)^0+3^0=2=u_0$ et $(-2)^1+3^1=1=u_1$. Attention : on ne commence pas par écrire $u_0=(-2)^0+3^0$, puisque c’est ce qu’il faut montrer.

**Hérédité.** Soit $n\in\mathbb N$. Supposons $P_n$ et $P_{n+1}$ vraies. D’après l’énoncé puis l’hypothèse de récurrence :

$$
\begin{aligned}
u_{n+2}&=u_{n+1}+6u_n\\
&=(-2)^{n+1}+3^{n+1}+6\bigl((-2)^n+3^n\bigr)\\
&=(-2)^n(-2+6)+3^n(3+6)\\
&=4(-2)^n+9\cdot3^n=(-2)^{n+2}+3^{n+2}.
\end{aligned}
$$

**Conclusion.** Pour tout $n\in\mathbb N$, $u_n=(-2)^n+3^n$.

## Exercice 4 — Opérations sur les ensembles (pages 2–3)

### 1. Intersection et complémentaire

Montrons :

$$A\cap B=A\cap C\quad\Longleftrightarrow\quad A\cap\overline B=A\cap\overline C.$$

Sens direct : supposons $A\cap B=A\cap C$. Soit $a\in A\cap\overline B$ ; alors $a\in A$ et $a\notin B$. Si $a\in C$, on aurait $a\in A\cap C=A\cap B$, donc $a\in B$ : contradiction. Ainsi $a\notin C$, donc $a\in A\cap\overline C$. Cela donne une inclusion ; l’autre s’obtient en échangeant $B$ et $C$.

Sens réciproque : appliquer le sens direct à $\overline B$ et $\overline C$, puis utiliser $\overline{\overline B}=B$ et $\overline{\overline C}=C$.

Deuxième méthode : si $A\cap B=A\cap C$, alors

$$A\setminus B=A\setminus(A\cap B)=A\setminus(A\cap C)=A\setminus C.$$

Procéder de même pour la réciproque en remplaçant $B$ et $C$ par leurs complémentaires.

### 2. Inclusion et ensemble des parties

Sens direct : supposons $A\subset B$. Si $X\in\mathcal P(A)$, alors $X\subset A\subset B$, donc $X\in\mathcal P(B)$.

Sens réciproque : supposons $\mathcal P(A)\subset\mathcal P(B)$. Si $x\in A$, alors $\{x\}\in\mathcal P(A)$, donc $\{x\}\in\mathcal P(B)$ et $x\in B$.

Deuxième méthode pour la réciproque : $A\in\mathcal P(A)\subset\mathcal P(B)$, donc $A\subset B$.

### 3. Produit cartésien et réunion

Pour tout $(x,y)\in E\times E$ :

$$
\begin{aligned}
(x,y)\in(A\cup B)\times C
&\Longleftrightarrow x\in A\cup B\text{ et }y\in C\\
&\Longleftrightarrow(x\in A\text{ ou }x\in B)\text{ et }y\in C\\
&\Longleftrightarrow(x\in A\text{ et }y\in C)\text{ ou }(x\in B\text{ et }y\in C)\\
&\Longleftrightarrow(x,y)\in A\times C\text{ ou }(x,y)\in B\times C\\
&\Longleftrightarrow(x,y)\in(A\times C)\cup(B\times C).
\end{aligned}
$$

Conclusion : $(A\cup B)\times C=(A\times C)\cup(B\times C)$.
