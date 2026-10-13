# Algèbre 1 — Corrigé du DS1 du 28 octobre 2021 (version 2)

> Source : `PREING1-S1/Algebre1-DS/DS1-2021-2022-V2-Correction_Algebre1-DS_P1S1_DMaths.pdf`, 2 pages. CY Tech, cycle préparatoire, première année. Jeudi 28 octobre 2021, durée 1 h 30 ; appareils électroniques et documents interdits.
> Transcription du 12 octobre 2026 : lecture visuelle intégrale et comparaison au texte natif ; table de vérité, intervalles et formules restitués. Les énoncés absents du corrigé ne sont pas inventés. Les incohérences de barème et les précisions mathématiques sont signalées séparément.

## Exercice 1 — Ensembles (3,5 points, page 1)

1. Résultats :

   - (0,5 point) $B\setminus A=]3;6[$.
   - (1 point) $A^c=]3;8]$, $B\cap C=]5;6[$ et $A^c\cup(B\cap C)=]3;8]$.
   - (1 point) $A\mathbin{\Delta}B=(A\cup B)\setminus(A\cap B)=[0;6[\setminus[1;3]=[0;1[\cup]3;6[$.

2. $A_1=[0;1[$, $A_2=[1;3]$, $A_3=]3;8]$.

## Exercice 2 — Table de vérité (3 points, page 1)

Les deux propositions ont la même table de vérité :

| $P$ | $Q$ | $R$ | $P\lor Q$ | $(P\lor Q)\Rightarrow R$ | $P\Rightarrow R$ | $Q\Rightarrow R$ | $(P\Rightarrow R)\land(Q\Rightarrow R)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V | V | V | V | V | V | V | V |
| V | V | F | V | F | F | F | F |
| V | F | V | V | V | V | V | V |
| V | F | F | V | F | F | V | F |
| F | V | V | V | V | V | V | V |
| F | V | F | V | F | V | F | F |
| F | F | V | F | V | V | V | V |
| F | F | F | F | V | V | V | V |

## Exercice 3 — Négations et fonctions (3 points, page 1)

1. (1 point) La négation donnée est :

   $$\exists x\in\mathbb R,\quad f(x)>0\text{ et }(3\geq x\text{ ou }7\leq x).$$

   **Précision de transcription.** Le PDF ne parenthèse pas le « ou » ; les parenthèses ci-dessus explicitent le regroupement de la condition « $x$ hors de $]3;7[$ ».

2. a. (1 point)

   $$(\exists x\in\mathbb R,\ f(x)\neq0)\text{ et }(\exists x\in\mathbb R,\ g(x)\neq0)\text{ et }(\forall x\in\mathbb R,\ f(x)g(x)=0).$$

   b. (0,5 point) Il existe bien deux fonctions qui ont cette propriété :

   $$
   f:\mathbb R\longrightarrow\mathbb R,\quad
   f(x)=\begin{cases}0&\text{si }x\neq0,\\1&\text{si }x=0,\end{cases}
   \qquad
   g:\mathbb R\longrightarrow\mathbb R,\quad
   g(x)=\begin{cases}1&\text{si }x\neq0,\\0&\text{si }x=0.\end{cases}
   $$

   Ce sont deux fonctions non nulles dont le produit $f\times g$ est nul.

## Exercice 4 — Irrationalité (3 points, page 2)

Supposons que $a$ soit irrationnel et montrons que $\sqrt a$ est irrationnel. Le corrigé annonce un raisonnement par contraposée.

Supposons qu’il existe deux entiers $p,q$, avec $q\neq0$, tels que $\sqrt a=p/q$. En élevant au carré :

$$a=\frac{p^2}{q^2}.$$

Les nombres $p^2,q^2$ sont entiers et $q^2\neq0$, donc $a$ est rationnel, ce qui contredit l’hypothèse. D’où le résultat.

**Précision.** Dans $\mathbb R$, l’affirmation suppose $a\geq0$, afin que $\sqrt a$ soit définie. Le texte commence par annoncer une contraposée, puis conclut par contradiction ; l’argument établit bien $\sqrt a\in\mathbb Q\Rightarrow a\in\mathbb Q$.

## Exercice 5 — Récurrence double (4 points, page 2)

### 1. Principe (1 point)

On applique une récurrence double lorsqu’une propriété au rang $n$ dépend des rangs $n-1$ et $n-2$.

1. Vérifier la propriété aux deux premiers rangs.
2. Fixer un entier naturel $n$ ; supposer la propriété vraie aux rangs $n$ et $n+1$, puis la démontrer au rang $n+2$.
3. Conclure que la propriété est vraie à tous les rangs considérés.

### 2. Application (1,5 + 1,5 points)

Pour $n\geq1$, posons $P(n)$ : « $1\leq a_n\leq n^2$ ». La suite utilisée dans le corrigé vérifie $a_1=1$, $a_2=2$ et $a_{n+2}=a_{n+1}+a_n/(n+1)$.

**Initialisation.** $a_1=1$, donc $1\leq a_1\leq1^2$ ; $a_2=2$, donc $1\leq a_2\leq2^2$. Les propriétés $P(1)$ et $P(2)$ sont vraies.

**Hérédité.** Soit $n\geq1$. Supposons $P(n)$ et $P(n+1)$ vraies. On a :

$$a_{n+1}\leq(n+1)^2=n^2+2n+1,\qquad\frac{a_n}{n+1}\leq\frac{n^2}{n+1}\leq\frac{(n+1)^2}{n+1}=n+1.$$

Donc :

$$a_{n+2}=a_{n+1}+\frac{a_n}{n+1}\leq n^2+2n+1+n+1\leq n^2+4n+4=(n+2)^2.$$

De plus :

$$a_{n+2}=a_{n+1}+\frac{a_n}{n+1}\geq1+\frac1{n+1}\geq1.$$

D’où $P(n+2)$. Conclusion : $1\leq a_n\leq n^2$ pour tout entier $n\geq1$.

## Exercice 6 — Identités ensemblistes (2,5 points annoncés, page 2)

### 1. Équivalence (2 points)

Sens direct : supposons $A\cup B=A\cap B$. Si $x\in A$, alors $x\in A\cup B=A\cap B$, donc $x\in B$. Ainsi $A\subset B$. En permutant $A$ et $B$, on obtient $B\subset A$, d’où $A=B$.

Sens réciproque : si $A=B$, alors $A\cup B=A=A\cap B$.

### 2. Différences d’ensembles (1,5 point indiqué)

$$
\begin{aligned}
A\setminus(B\setminus C)
&=A\cap(B\setminus C)^c\\
&=A\cap(B^c\cup C)\\
&=(A\cap B^c)\cup(A\cap C)\\
&=(A\setminus B)\cup(A\cap C).
\end{aligned}
$$

**Note sur les barèmes.** Les points détaillés de l’exercice 6 totalisent 3,5, alors que son titre annonce 2,5. Ceux de l’exercice 3 totalisent 2,5 pour 3 annoncés. Ces valeurs sont celles du PDF.
