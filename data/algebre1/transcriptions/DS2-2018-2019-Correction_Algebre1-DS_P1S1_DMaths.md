# Algèbre 1 — Correction du DS2 de 2018

> Source : `PREING1-S1/Algebre1-DS/DS2-2018-2019-Correction_Algebre1-DS_P1S1_DMaths.pdf`, 3 pages. EISTI, première année ; année scolaire 2018–2019 selon le nom du fichier.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif et restitution des formules. La source passe de l’exercice 3 à l’exercice 5 ; aucun exercice 4 n’est présent. Les erreurs du corrigé sont signalées.

## Exercice 1 — Congruences (page 1)

$100=5\times17+15$, donc $100^{2018}\equiv15^{2018}\pmod{17}$. Cherchons un entier $k$ tel que $15^k\equiv1\pmod{17}$.

$$15\equiv-2\pmod{17},\quad15^4\equiv(-2)^4=16\equiv-1\pmod{17},\quad15^8\equiv(-1)^2\equiv1\pmod{17}.$$

On peut prendre $k=8$. La division euclidienne de 2018 par 8 donne $2018=252\times8+2$. Ainsi :

$$100^{2018}\equiv15^{2018}=(15^8)^{252}15^2\equiv15^2\equiv4\pmod{17}.$$

Le reste de la division euclidienne est donc **4**.

## Exercice 2 — Exemples d’applications (page 1)

Les correspondances indiquent les ensembles $E_1=\{\text{garçon},\text{fille}\}$, $E_2=\{\text{lune},\text{soleil}\}$ et $E_3=\{\text{chaise},\text{armoire},\text{table}\}$.

| Cas | Départ et arrivée | Correspondances |
| --- | --- | --- |
| 1. Injective, non surjective | $f:E_1\to E_3$ | garçon $\mapsto$ chaise ; fille $\mapsto$ armoire |
| 2. Surjective, non injective | $f:E_3\to E_1$ | chaise $\mapsto$ garçon ; armoire $\mapsto$ fille ; table $\mapsto$ fille |
| 3. Ni injective ni surjective | $f:E_1\to E_3$ | garçon $\mapsto$ chaise ; fille $\mapsto$ chaise |
| 4. Bijective : injective et surjective | $f:E_1\to E_2$ | garçon $\mapsto$ lune ; fille $\mapsto$ soleil |

## Exercice 3 — L’application quotient (pages 1–2)

Les calculs du corrigé concernent $f:\mathbb Z\times\mathbb N^*\to\mathbb R$, $f(m,n)=m/n$.

1. $f$ n’est pas injective : $(4,2)\neq(6,3)$ et $f(4,2)=f(6,3)$.

2. $f$ n’est pas surjective : $\sqrt2$ n’a pas d’antécédent. Supposons en effet $\sqrt2=m/n$ avec $(m,n)\in\mathbb Z\times\mathbb N^*$. Nécessairement $m>0$. Il existe deux entiers premiers entre eux $a,b$ tels que $a/b=m/n=\sqrt2$.

   Alors $a^2=2b^2$, donc $a$ est pair. Écrivons $a=2p$ avec $p\in\mathbb N$ ; on obtient $b^2=4p^2/2=2p^2$, donc $b$ est aussi pair. C’est absurde, puisque $a$ et $b$ sont premiers entre eux.

3. $f(\mathbb Z\times\mathbb N^*)=\mathbb Q$.

4. Images réciproques :

   a.

   $$
   \begin{aligned}
   f^{-1}(\{1\})
   &=\{(m,n)\in\mathbb Z\times\mathbb N^*\mid m/n=1\}\\
   &=\{(m,n)\in\mathbb Z\times\mathbb N^*\mid m=n\}\\
   &=\{(n,n)\mid n\in\mathbb N^*\}.
   \end{aligned}
   $$

   b.

   $$
   \begin{aligned}
   f^{-1}(\{q\})
   &=\{(m,n)\in\mathbb Z\times\mathbb N^*\mid m/n=q\}\\
   &=\{(m,n)\in\mathbb Z\times\mathbb N^*\mid m=qn\}.
   \end{aligned}
   $$

   La dernière ligne imprimée est $\{(qn,n)\mid n\in\mathbb N^*\}$. **Précision :** si $q$ est un rationnel quelconque, il faut conserver la contrainte $qn\in\mathbb Z$ ; la ligne imprimée est valable sans restriction supplémentaire lorsque $q\in\mathbb Z$.

   c.

   $$
   \begin{aligned}
   f^{-1}(\mathbb Z)
   &=\{(m,n)\in\mathbb Z\times\mathbb N^*\mid m/n\in\mathbb Z\}\\
   &=\{(m,n)\in\mathbb Z\times\mathbb N^*\mid m\in n\mathbb Z\}\\
   &=\{(kn,n)\mid n\in\mathbb N^*,\ k\in\mathbb Z\}.
   \end{aligned}
   $$

   **Note sur la source :** le PDF écrit $f^{-1}(\{\mathbb Z\})$ au lieu de $f^{-1}(\mathbb Z)$ ; la variable entière de la dernière ligne est renommée $k$ pour la distinguer de la première coordonnée.

## Exercice 5 — Relations d’ordre (pages 2–3)

### 1. Relation $\mathcal R$

La relation étudiée est :

$$(x,y)\mathcal R(x',y')\quad\Longleftrightarrow\quad x\leq x'\text{ et }y\leq y'.$$

a. **Réflexivité.** Pour $(x,y)\in\mathbb R^2$, $x\leq x$ et $y\leq y$, donc $(x,y)\mathcal R(x,y)$.

**Antisymétrie.** Si $(x,y)\mathcal R(x',y')$ et $(x',y')\mathcal R(x,y)$, alors $x\leq x'\leq x$ et $y\leq y'\leq y$. Ainsi $x=x'$, $y=y'$, donc $(x,y)=(x',y')$.

**Transitivité.** Si $(x,y)\mathcal R(x',y')$ et $(x',y')\mathcal R(x'',y'')$, alors $x\leq x'\leq x''$ et $y\leq y'\leq y''$. Donc $(x,y)\mathcal R(x'',y'')$.

**Notes sur la source.** Le texte annonce un ordre « sur $\mathbb R$ » ; les éléments considérés sont des couples de $\mathbb R^2$. La dernière paire de la preuve de transitivité est imprimée $(x',y')$ au lieu de $(x'',y'')$.

b. L’ordre est partiel : $(1,2)$ et $(2,1)$ ne sont pas comparables pour $\mathcal R$.

c. Les couples tels que $(1,1)\mathcal R(x,y)$ vérifient $1\leq x$ et $1\leq y$.

**Description géométrique et correction de source.** Il s’agit du quart de plan $[1,+\infty[\times[1,+\infty[$. Ses bords sont $x=1,\ y\geq1$ et $y=1,\ x\geq1$, inclus. Le PDF donne par erreur $y\leq1$ pour le premier bord et une indication « à gauche » incohérente avec les inégalités.

### 2. Relation $\mathcal S$

La relation étudiée est l’ordre lexicographique :

$$(x,y)\mathcal S(x',y')\quad\Longleftrightarrow\quad x<x'\text{ ou }(x=x'\text{ et }y\leq y').$$

a. **Réflexivité.** $x=x$ et $y\leq y$, donc $(x,y)\mathcal S(x,y)$.

**Antisymétrie.** Supposons $(x,y)\mathcal S(x',y')$ et $(x',y')\mathcal S(x,y)$. Le développement des deux alternatives donne quatre cas :

- $x<x'$ et $x'<x$ : impossible ;
- $x<x'$ et $x'=x,\ y'\leq y$ : impossible ;
- $x=x',\ y\leq y'$ et $x'<x$ : impossible ;
- $x=x',\ y\leq y'$ et $x'=x,\ y'\leq y$ : alors $x=x'$ et $y=y'$.

Donc $(x,y)=(x',y')$.

**Transitivité.** Supposons $(x,y)\mathcal S(x',y')$ et $(x',y')\mathcal S(x'',y'')$. Quatre cas :

- $x<x'$ et $x'<x''$ : alors $x<x''$ ;
- $x<x'$ et $x'=x'',\ y'\leq y''$ : alors $x<x''$ ;
- $x=x',\ y\leq y'$ et $x'<x''$ : alors $x<x''$ ;
- $x=x',\ y\leq y'$ et $x'=x'',\ y'\leq y''$ : alors $x=x''$ et $y\leq y''$.

Dans tous les cas $(x,y)\mathcal S(x'',y'')$. Ainsi $\mathcal S$ est une relation d’ordre.

**Note sur la source.** Comme pour $\mathcal R$, l’ensemble est $\mathbb R^2$, bien que le texte écrive aussi $\mathbb R$ ou $E^2$. Une ligne intermédiaire de la transitivité remplace indûment $y'\leq y''$ par $y'<y''$ ; la présentation par cas ci-dessus conserve l’inégalité correcte.

b. Pour deux couples $(x,y)$ et $(x',y')$ :

- si $x<x'$, alors $(x,y)\mathcal S(x',y')$ ;
- si $x>x'$, alors $(x',y')\mathcal S(x,y)$ ;
- si $x=x'$ et $y<y'$, alors $(x,y)\mathcal S(x',y')$ ;
- si $x=x'$ et $y>y'$, alors $(x',y')\mathcal S(x,y)$ ;
- si $x=x'$ et $y=y'$, les couples sont égaux et en relation.

Tous les couples sont comparables : $\mathcal S$ est un **ordre total**.

c. Les couples tels que $(1,1)\mathcal S(x,y)$ vérifient :

$$1<x\quad\text{ou}\quad(1=x\text{ et }1\leq y).$$

**Description géométrique et correction de source.** L’ensemble est

$$\bigl(]1,+\infty[\times\mathbb R\bigr)\cup\bigl(\{1\}\times[1,+\infty[\bigr).$$

C’est le demi-plan ouvert $x>1$, complété par la demi-droite $x=1,\ y\geq1$. Le PDF le décrit à tort comme un « quart de plan » et exclut la demi-droite verticale ; cela contredit sa propre formule, correctement transcrite ci-dessus.
