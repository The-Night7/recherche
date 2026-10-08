---
source: "PREING2-S1/Analyse-dans-RN-DS/DS1-2021-2022-Correction_Analyse-dans-RN-DS_P2S1_Inconnu.pdf"
pages: 6
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 6 pages manuscrites ; calculs et barèmes transcrits
---

# Analyse dans Rn — DS1 2021–2022 : correction manuscrite

## Page 1

### Correction — Analyse dans Rn, DS1 (2021–2022)

#### Exercice 1

**1. Définition (1 point).** Un espace est séparé si deux points distincts $x,y$ admettent des voisinages respectifs $V_x,V_y$ tels que $V_x\cap V_y=\varnothing$.

**2. Tout espace vectoriel normé est séparé (3 points).** Pour $x\ne y$, posons $d=\|x-y\|>0$, $\varepsilon_1=d/2$, $\varepsilon_2=d/3$. Les boules ouvertes $B(x,\varepsilon_1)$ et $B(y,\varepsilon_2)$ sont des voisinages. Si $z$ appartenait aux deux,
$$d=\|x-y\|\le\|x-z\|+\|z-y\|<\varepsilon_1+\varepsilon_2=\frac{5d}6,$$
contradiction. Les boules sont donc disjointes.

#### Exercice 2

Le corrigé précise que plusieurs méthodes sont possibles.

**1.** $A=\{(x,y)\in\mathbb R^2:x=0,\ 1\le y\le2\}=\{0\}\times[1,2]$. Le singleton et le segment sont fermés ; leur produit est fermé (0,5 point). Le complémentaire n’est pas fermé : la suite $(1/n,1-1/n)$ est hors de $A$ et tend vers $(0,1)\in A$. Donc $A$ n’est pas ouvert (0,5 point).

## Page 2

**Exercice 2 — 1, suite.** Comme $A$ est fermé, $\overline A=A$ (0,5 point). Son intérieur est vide : $\mathring A=\mathring{\{0\}}\times]1,2[=\varnothing$ (0,5 point).

**2.**
$$B=\{(x,y)\in\mathbb R^2:|x-1|<1,\ |y-1|<1\}\cup\{(0{,}2;0{,}5)\}.$$
Le point ajouté appartient déjà au carré, donc $B=]0,2[^2$ (0,5 point). La suite $(1/n,1/n)\in B$ tend vers $(0,0)\notin B$, donc $B$ n’est pas fermé (0,5 point). Le produit d’intervalles ouverts est ouvert ; le corrigé observe aussi que son complémentaire est fermé (0,5 point).

Pour l’adhérence, on montre d’abord $\overline{]0,2[}=[0,2]$ : le segment est un fermé contenant l’intervalle, et ses extrémités sont limites des suites $1/n$ et $2-1/n$. En prenant le produit,
$$\overline B=[0,2]^2\quad(0,5\text{ point}).$$

## Page 3

**Exercice 2 — 2, intérieur.** Le carré ouvert $B$ est son propre intérieur : $\mathring B=]0,2[^2$ (0,5 point).

**3.** $C=]-5,-1[\cup]0,5]\cup\{6\}$. Il n’est pas fermé : pour $n\ge1$, $-5+1/n\in C$ et cette suite tend vers $-5\notin C$ (0,5 point). Il n’est pas ouvert : pour tout rayon $r>0$ autour de $6$, choisir $n$ avec $1/n<r$ ; le point $6+1/n$ est dans la boule et hors de $C$ (0,5 point). Par union finie des adhérences,
$$\overline C=[-5,-1]\cup[0,5]\cup\{6\}\quad(0,5\text{ point}),$$
et
$$\mathring C=]-5,-1[\cup]0,5[\quad(0,5\text{ point}).$$

#### Exercice 3

On note $\ell^\infty(\mathbb R)$ l’espace des suites réelles bornées. Pour $x=(x_n)_{n\ge0}$,
$$\nu(x)=\sup_{n\ge0}|x_n|,\qquad N(x)=\sup_{n\ge0}\left|\frac{2^n+1}{2^n+2}x_n\right|.$$
**1a.** La suite $a_n=(2^n+1)/(2^n+2)$ est bornée, car $0<a_n<1$ (0,5 point).

**1b.** Elle tend vers $1$ et s’écrit $a_n=1-1/(2^n+2)$, ce qui montre sa stricte croissance.

## Page 4

**Exercice 3 — 1b, bornes.** La croissance et la limite donnent
$$\sup_{n\ge0}a_n=1,\qquad\inf_{n\ge0}a_n=a_0=\frac23\quad(0,5\text{ point}).$$

**2a. $\nu$ est une norme.** Si $\nu(x)=0$, chaque $x_n=0$, donc $x=0$ (0,5 point). Pour $\lambda\in\mathbb R$,
$$\nu(\lambda x)=\sup_n|\lambda x_n|=|\lambda|\nu(x)\quad(0,5\text{ point}).$$
Pour $x,y\in\ell^\infty$,
$$|x_n+y_n|\le|x_n|+|y_n|\le\nu(x)+\nu(y).$$
Le membre de droite est un majorant indépendant de $n$, donc $\nu(x+y)\le\nu(x)+\nu(y)$ (1 point).

**2b. $N$ est une norme.** Si $N(x)=0$, tous les $a_nx_n$ sont nuls. Comme $a_n>0$, tous les $x_n$ sont nuls (0,5 point). La suite des coefficients est bornée, ce qui assure que $N$ est bien finie sur $\ell^\infty$.

## Page 5

**Exercice 3 — 2b, suite.** L’homogénéité donne
$$N(\lambda x)=\sup_n|a_n\lambda x_n|=|\lambda|N(x)\quad(0,5\text{ point}).$$
Pour l’inégalité triangulaire,
$$a_n|x_n+y_n|\le a_n|x_n|+a_n|y_n|\le N(x)+N(y),$$
donc $N(x+y)\le N(x)+N(y)$ en prenant le supremum (1 point).

**3. Équivalence.** Puisque $2/3\le a_n<1$,
$$\frac23|x_n|\le|a_nx_n|\le|x_n|.$$
En prenant les suprema,
$$\frac23\nu(x)\le N(x)\le\nu(x).$$
Les normes sont donc équivalentes, avec $\alpha=2/3$, $\beta=1$ (0,5 point pour l’encadrement ponctuel). La page renomme ponctuellement ces deux normes $N_1,N_2$ ; on conserve ici les noms de leur définition.

#### Exercice 4

L’application $\|\cdot\|:E\to\mathbb R$ est supposée vérifier la séparation, l’homogénéité et l’inégalité forte
$$\|x+y\|\le\max(\|x\|,\|y\|).$$
**1. Positivité.** L’homogénéité donne $\|0\|=0$ et $\|-x\|=\|x\|$. Ainsi
$$0=\|x-x\|\le\max(\|x\|,\|-x\|)=\|x\|.$$
Donc $\|x\|\ge0$. Le raisonnement se poursuit page suivante.

## Page 6

**Exercice 4 — 2, norme.** La séparation et l’homogénéité sont données. Comme les valeurs sont positives,
$$\|x+y\|\le\max(\|x\|,\|y\|)\le\|x\|+\|y\|.$$
L’inégalité triangulaire usuelle est donc satisfaite (annotations : 1 point pour chacune des premières étapes).

**3. Tout point d’une boule ouverte en est un centre (2 points, un par inclusion).** Soit $r>0$ et $x\in B(a,r)$. Si $y\in B(a,r)$,
$$\|y-x\|\le\max(\|y-a\|,\|a-x\|)<r,$$
donc $y\in B(x,r)$ et $B(a,r)\subset B(x,r)$. Réciproquement, si $y\in B(x,r)$,
$$\|y-a\|\le\max(\|y-x\|,\|x-a\|)<r,$$
donc $B(x,r)\subset B(a,r)$. Ainsi $B(a,r)=B(x,r)$.

**4. Deux boules qui se rencontrent sont emboîtées (2 points).** Si $z\in B(x,r_1)\cap B(y,r_2)$, la question 3 donne $B(x,r_1)=B(z,r_1)$ et $B(y,r_2)=B(z,r_2)$. Si $r_1\le r_2$, la première boule est incluse dans la seconde ; si $r_1>r_2$, c’est l’inverse.

**Précision :** ces propriétés découlent de l’inégalité forte donnée par l’exercice. Sur un espace vectoriel réel avec l’homogénéité usuelle, cette inégalité forte force en fait l’espace à être réduit à zéro : $\|2x\|=2\|x\|\le\|x\|$. Les arguments sur les boules restent valables sous ces hypothèses.
