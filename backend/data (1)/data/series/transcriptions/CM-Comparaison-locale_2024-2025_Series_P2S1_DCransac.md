---
source: "PREING2-S1/Series/CM-Comparaison-locale_2024-2025_Series_P2S1_DCransac.pdf"
pages: 28
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-07
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Comparaison locale de fonctions réelles — 9 septembre 2024

## Page 1

Comparaison locale de fonctions réelles.

9 septembre 2024.

Le bandeau de navigation répété sur les diapositives annonce : négligeabilité ; domination ; équivalence ; lien entre négligeabilité, domination et équivalence.

## Page 2

## Plan

1. Négligeabilité.
2. Domination.
3. Équivalence : équivalences et exponentielle ; équivalences et logarithme.
4. Lien entre négligeabilité, domination et équivalence.

## Page 3

## Négligeabilité — définition : voisinage

Soit $a\in\overline{\mathbb R}=\mathbb R\cup\{\pm\infty\}$. On appelle voisinage de $a$ toute partie de $\mathbb R$ contenant un intervalle de la forme :

- $]a-\varepsilon,a+\varepsilon[$, avec $\varepsilon>0$, si $a\in\mathbb R$ ;
- $]A,+\infty[$ si $a=+\infty$ ;
- $]-\infty,A[$ si $a=-\infty$.

Dans la suite, $V(a)$ désigne un voisinage de $a$.

## Page 4

## Définition

Soit $a\in\overline{\mathbb R}=\mathbb R\cup\{\pm\infty\}$ et $f,g:V(a)\to\mathbb R$. On suppose que $g$ ne s’annule pas sur $V(a)$, sauf éventuellement en $a$, avec dans ce cas $f(a)=0$.

On dit que $f$ est négligeable devant $g$ au voisinage de $a$ si

$$\lim_{x\to a}\frac{f(x)}{g(x)}=0.$$

On note $f\underset a=o(g)$ et on lit « $f$ est un petit $o$ de $g$ au voisinage de $a$ ». Une autre notation possible est $f\underset a\ll g$.

## Page 5

## Exemples

$$x^2\underset{+\infty}=o(x^4),\qquad x^4\underset0=o(x^2),\qquad
\frac1{x^2}\underset{+\infty}=o\left(\frac1x\right),\qquad
\frac1x\underset0=o\left(\frac1{x^2}\right).$$

Remarque : pour alléger les énoncés, on notera parfois tout court $f\underset a=o(g)$, en supposant satisfaites les hypothèses de la définition précédente.

## Page 6

## Définition pour les suites

Soient $(u_n)_n$ et $(v_n)_n$ deux suites réelles telles que $(v_n)_n$ ne s’annule pas à partir d’un certain rang. On dit que $(u_n)_n$ est négligeable devant $(v_n)_n$ si

$$\lim_{n\to+\infty}\frac{u_n}{v_n}=0.$$

On note $u_n=o(v_n)$ et on lit « $u_n$ est un petit $o$ de $v_n$ ». Une autre notation possible est $u_n\ll v_n$.

Exemples : $2^n=o(3^n)$, $n^2=o(2^n)$, $\ln n=o(n)$.

## Page 7

## Proposition

Soit $f:V(a)\to\mathbb R$ et $\ell\in\mathbb R$. On a

$$\lim_{x\to a}f(x)=\ell\quad\Longleftrightarrow\quad f\underset a=\ell+o(1).$$

En particulier, $\lim_{x\to a}f(x)=0\Longleftrightarrow f\underset a=o(1)$. Ainsi, $o(1)$ est une fonction de limite nulle en $a$.

## Page 8

## Proposition — opérations sur les petits $o$

1. Transitivité : si $f=o(g)$ et $g=o(h)$, alors $f=o(h)$.
2. Multiplication par un réel non nul : si $f=o(g)$, alors, pour tout $\lambda\in\mathbb R^*$, $f=o(\lambda g)$ et $\lambda f=o(g)$.
3. Somme de petits $o$ d’une même fonction : si $f_1=o(g)$ et $f_2=o(g)$, alors $f_1+f_2=o(g)$.
4. Produit : si $f_1=o(g_1)$ et $f_2=o(g_2)$, alors $f_1f_2=o(g_1g_2)$. Si $f=o(g)$, alors $fh=o(gh)$.
5. Composition à droite : si $f\underset a=o(g)$ et $\lim_{x\to b}h(x)=a$, alors $f\circ h\underset b=o(g\circ h)$.

**Note de transcription :** le premier point imprime « $g=o(g)$ » au lieu de $f=o(g)$ ; la coquille est corrigée ci-dessus. Les opérations sont comprises sous les hypothèses de définition annoncées page 5, notamment pour les quotients et les compositions.

## Page 9

## Remarque — composition à droite

La composition à droite s’interprète comme un changement de variable. Voici deux exemples.

- Pour comparer $\sqrt{\ln x}$ et $\ln x$ au voisinage de $+\infty$, on pose $u=h(x)=\ln x$. On a $\lim_{x\to+\infty}h(x)=+\infty$ et $\sqrt x\underset{+\infty}=o(x)$ ; alors $\sqrt{\ln x}\underset{+\infty}=o(\ln x)$.
- Pour comparer $e^{1/x}$ et $1/x$ au voisinage de $0^+$, on pose $u=h(x)=1/x$. On a $\lim_{x\to0^+}h(x)=+\infty$ et $x\underset{+\infty}=o(e^x)$ ; alors $1/x\underset{0^+}=o(e^{1/x})$.

## Page 10

## Opérations interdites !

1. Il est interdit d’additionner des relations de négligeabilité membre à membre. Les égalités $f_1=o(g_1)$ et $f_2=o(g_2)$ n’entraînent pas $f_1+f_2=o(g_1+g_2)$. Par exemple, $x-1\underset{+\infty}=o(x^2)$ et $1\underset{+\infty}=o(1-x^2)$, mais $x\underset{+\infty}\ne o(1)$.
2. Il est interdit de composer une relation de négligeabilité par la gauche. Si $f=o(g)$, on n’a pas forcément $h\circ f=o(h\circ g)$. Par exemple, $\ln x\underset{+\infty}=o(x)$, mais $1/\ln x\underset{+\infty}\ne o(1/x)$. Ainsi, on ne peut pas composer par $x\mapsto1/x$ par la gauche.

**Note de transcription :** le PDF écrit $f\circ f$ au lieu de $h\circ f$ dans le deuxième point.

## Page 11

## Théorème — croissances comparées usuelles

Soit $(a,b)\in\mathbb R^2$.

Au voisinage de $+\infty$ :

1. Si $a<b$, alors $x^a\underset{+\infty}=o(x^b)$.
2. Si $0<a<b$, alors $a^x\underset{+\infty}=o(b^x)$.
3. Si $a>0$, alors $(\ln x)^b\underset{+\infty}=o(x^a)$.
4. Si $a>0$, alors $x^b\underset{+\infty}=o(e^{ax})$.

Au voisinage de $0$ :

1. Si $a<b$, alors $x^b\underset0=o(x^a)$.
2. Si $a>0$, alors $x^a\underset0=o(|\ln x|^b)$.

**Précision de transcription :** les deux derniers énoncés s’entendent en $0^+$ pour des puissances réelles et le logarithme réel ; le PDF indique seulement $0$.

## Page 12

## Domination — définition

Soit $a\in\overline{\mathbb R}=\mathbb R\cup\{\pm\infty\}$ et $f,g:V(a)\to\mathbb R$. On suppose que $g$ ne s’annule pas sur $V(a)$, sauf éventuellement en $a$, avec dans ce cas $f(a)=0$.

On dit que $f$ est dominée par $g$ au voisinage de $a$ si la fonction $f/g$ est bornée au voisinage de $a$.

On note $f\underset a=O(g)$ et on lit « $f$ est un grand $O$ de $g$ au voisinage de $a$ ».

Exemples, dans l’ordre du document :

$$\sin\left(\frac1x\right)\underset0=O(1),\quad x^2\underset0=O(x),\quad 2x^2\underset{+\infty}=O(x^2),\quad x^2\underset0=O(x).$$

## Page 13

## Remarque

$f\underset a=O(1)$ si et seulement si $f$ est bornée au voisinage de $a$.

## Proposition — opérations sur les grands $O$

Toutes les opérations énoncées pour les petits $o$ restent valables pour les grands $O$.

## Opérations interdites !

Les opérations interdites pour les petits $o$ (additionner membre à membre et composition par la gauche) restent interdites pour les grands $O$.

## Page 14

## Équivalence — définition

Soit $a\in\overline{\mathbb R}=\mathbb R\cup\{\pm\infty\}$ et $f,g:V(a)\to\mathbb R$. On suppose que $g$ ne s’annule pas sur $V(a)$, sauf éventuellement en $a$, avec dans ce cas $f(a)=0$.

On dit que $f$ est équivalente à $g$ au voisinage de $a$ si

$$\lim_{x\to a}\frac{f(x)}{g(x)}=1.$$

On note dans ce cas $f\underset a\sim g$.

Remarque importante : ne jamais écrire $f\sim0$, car la fonction nulle ne vérifie pas les conditions de la définition.

## Page 15

## Remarque

Pour alléger les énoncés, on notera parfois tout court $f\underset a\sim g$, en supposant satisfaites les hypothèses de la définition précédente.

Exemples : $x+x^2\underset0\sim x$ ; $x^3+x^2+1\underset{+\infty}\sim x^3$.

## Page 16

## Définition pour les suites

Soient $(u_n)_n$ et $(v_n)_n$ deux suites réelles qui ne s’annulent pas à partir d’un certain rang. On dit que $(u_n)_n$ est équivalente à $(v_n)_n$ si

$$\lim_{n\to+\infty}\frac{u_n}{v_n}=1.$$

On note dans ce cas $u_n\sim v_n$.

Exemples : $1/n+1/n^2\sim1/n$ ; $3^n+2^n\sim3^n$.

## Page 17

## Proposition — équivalents usuels

- Tout polynôme est équivalent à son terme de plus haut degré au voisinage de $\pm\infty$.
- Tout polynôme est équivalent à son terme de plus petit degré au voisinage de $0$.
- Si $f$ admet un développement limité au voisinage de $0$, alors $f$ est équivalente au terme non nul de plus faible ordre au voisinage de $0$.

| N° | Équivalent en $0$ |
| --- | --- |
| 1 | $e^x-1\sim x$ |
| 2 | $\ln(1+x)\sim x$ |
| 3 | $(1+x)^\alpha-1\sim\alpha x$ |
| 4 | $\sin x\sim x$ |
| 5 | $1-\cos x\sim x^2/2$ |
| 6 | $\tan x\sim x$ |
| 7 | $\arcsin x\sim x$ |
| 8 | $\arctan x\sim x$ |
| 9 | $\operatorname{sh}x\sim x$ |
| 10 | $\operatorname{ch}x-1\sim x^2/2$ |
| 11 | $\operatorname{th}x\sim x$ |

**Précision de transcription :** les polynômes et termes dominants doivent être non nuls ; dans la ligne 3, $\alpha\ne0$. Ces restrictions ne sont pas écrites dans la diapositive.

## Page 18

## Proposition

La relation « est équivalente à » est une relation d’équivalence : pour toutes fonctions $f,g,h$ satisfaisant les hypothèses annoncées, on a :

- réflexivité : $f\underset a\sim f$ ;
- symétrie : si $f\underset a\sim g$, alors $g\underset a\sim f$ ;
- transitivité : si $f\underset a\sim g$ et $g\underset a\sim h$, alors $f\underset a\sim h$.

Il s’agit d’une vérification directe.

## Page 19

## Proposition

**1. Lien limites / équivalence.**

- Pour tout $\ell\in\mathbb R^*$, $\lim_{x\to a}f(x)=\ell\Longleftrightarrow f\underset a\sim\ell$.
- Si $f\underset a\sim g$, alors soit $f$ et $g$ ont toutes les deux une limite en $a$, en l’occurrence la même, soit aucune de ces deux fonctions ne possède de limite en $a$.

**2. Lien négligeabilité / équivalence.**

- $f\underset a\sim g\Longleftrightarrow f\underset a=g+o(g)$.
- $f\underset a=o(g)\Longleftrightarrow f+g\underset a\sim g$.

**3. Signe et équivalence.**

- Si $f\underset a\sim g$, alors $f$ et $g$ sont de même signe au voisinage de $a$.
- Si $f$ ne s’annule pas au voisinage de $a$ et $f\underset a\sim g$, alors $g$ ne s’annule pas au voisinage de $a$.

**Note de transcription :** la première limite du PDF omet $f(x)$ ; il a été rétabli. Les mots « même » et « possède », affichés avec un encodage défectueux, ont été normalisés.

## Page 20

## Proposition — opérations sur les équivalences

1. **Produit.** Si $f\underset a\sim f_1$ et $g\underset a\sim g_1$, alors $fg\underset a\sim f_1g_1$.
2. **Inverse.** Si $f\underset a\sim g$ et $f$ ne s’annule pas au voisinage de $a$, alors $1/f\underset a\sim1/g$.
3. **Puissance.** Si $f\underset a\sim g$ et $f$ est strictement positive au voisinage de $a$, alors, pour tout réel $\alpha$, $f^\alpha\underset a\sim g^\alpha$. Attention : $\alpha$ ne dépend pas de la variable $x$.
4. **Composition à droite.** Si $f\underset a\sim g$ et $\lim_{x\to b}h(x)=a$, alors $f\circ h\underset b\sim g\circ h$.

**Note de transcription :** dans le dernier résultat, la diapositive imprime $g\circ g$ ; il s’agit de $g\circ h$.

## Page 21

## Opérations interdites !

1. Il est interdit d’additionner des équivalents : si $f\underset a\sim f_1$ et $g\underset a\sim g_1$, on n’a pas nécessairement $f+g\underset a\sim f_1+g_1$. Par exemple, $x+1\underset{+\infty}\sim x$ et $-x+3\underset{+\infty}\sim-x+1$, mais on n’a clairement pas $4\underset{+\infty}\sim1$.
2. Il est interdit de composer un équivalent par la gauche : si $f\underset a\sim g$, on n’a pas forcément $h\circ f\underset a\sim h\circ g$. Par exemple, $x\underset{+\infty}\sim x+\ln x$, mais on n’a pas $e^x\underset{+\infty}\sim xe^x$ en composant par $x\mapsto e^x$ par la gauche.

## Page 22

## Exercice

Calculer les limites suivantes en utilisant les équivalences :

1. $\displaystyle\lim_{x\to0}\frac{\sqrt[5]{1+6x}-\sqrt[3]{1+x}}{3\sin x-\ln(1+x)}$.
2. Pour tous $a,b>0$, $\displaystyle\lim_{x\to+\infty}\left(\frac{a^{1/x}+b^{1/x}}2\right)^x$.

Aucune correction n’est donnée sur cette page.

## Page 23

## Équivalence et exponentielle — remarque importante

On ne peut pas composer un équivalent à gauche par l’exponentielle : si $f\underset a\sim g$, on n’a pas forcément $e^f\underset a\sim e^g$.

Par exemple, $x\underset{+\infty}\sim x+1$, mais on n’a pas $e^x\underset{+\infty}\sim e^{x+1}$, car

$$\lim_{x\to+\infty}\frac{e^{x+1}}{e^x}=e\ne1.$$

Toutefois, sous certaines hypothèses, on peut composer à gauche par l’exponentielle.

**Proposition :** $e^f\underset a\sim e^g\Longleftrightarrow\lim_{x\to a}(f-g)=0$.

**Note de transcription :** dans le quotient du contre-exemple, le PDF imprime $e^x+1$ au numérateur, alors que le raisonnement porte sur $e^{x+1}$ ; la formule est rétablie ci-dessus.

## Page 24

## Démonstration

Si $e^f\underset a\sim e^g$, alors $\lim_{x\to a}e^{f(x)}/e^{g(x)}=1$, d’où $\lim_{x\to a}e^{f(x)-g(x)}=1$. En utilisant la continuité de $x\mapsto\ln x$ en $1$, on a

$$\begin{aligned}
\lim_{x\to a}(f(x)-g(x))
&=\lim_{x\to a}\ln\left(e^{f(x)-g(x)}\right)\\
&=\ln\left(\lim_{x\to a}e^{f(x)-g(x)}\right)=\ln1=0.
\end{aligned}$$

Réciproquement, si $\lim_{x\to a}(f(x)-g(x))=0$, en utilisant la continuité de $x\mapsto e^x$ en $0$, on a

$$\lim_{x\to a}\frac{e^{f(x)}}{e^{g(x)}}=\lim_{x\to a}e^{f(x)-g(x)}
=e^{\lim_{x\to a}(f(x)-g(x))}=e^0=1.$$

## Page 25

## Équivalences et logarithme — remarque importante

On ne peut pas composer un équivalent à gauche par le logarithme : si $f\underset a\sim g$ et $f$ est strictement positive au voisinage de $a$, on n’a pas forcément $\ln f\underset a\sim\ln g$.

Par exemple, $1+x\underset0\sim1+2x$, mais on n’a pas $\ln(1+x)\underset0\sim\ln(1+2x)$, car

$$\lim_{x\to0}\frac{\ln(1+2x)}{\ln(1+x)}=2\ne1.$$

Toutefois, sous certaines conditions, on peut composer à gauche par le logarithme.

## Page 26

## Proposition

Si $f\underset a\sim g$, avec $f$ strictement positive au voisinage de $a$, et si la fonction $x\mapsto1/\ln g(x)$ est bornée au voisinage de $a$ (en particulier, si $\lim_{x\to a}g(x)\ne1$), alors $\ln f\underset a\sim\ln g$.

## Page 27

## Lien entre négligeabilité, domination et équivalence

**Proposition.**

- La négligeabilité entraîne la domination : $f\underset a=o(g)\Longrightarrow f\underset a=O(g)$.
- L’équivalence entraîne la domination : $f\underset a\sim g\Longrightarrow f\underset a=O(g)$.

En effet, si la limite en $a$ d’une fonction (ici $f/g$) vaut $0$ ou $1$, alors cette fonction est bornée au voisinage de $a$.

## Page 28

## Exemples

$$e^x\underset0=1+x+\frac{x^2}2+\frac{x^3}6+o(x^3)
\quad\Longrightarrow\quad e^x\underset0=1+x+\frac{x^2}2+O(x^3).$$

$$\cos x\underset0=1-\frac{x^2}2+o(x^2)
\quad\Longrightarrow\quad\cos x\underset0=1+O(x^2).$$

## Exercice

Montrer que

$$\sum_{k=1}^n\frac1k\underset{+\infty}=\ln n+O(1),\qquad\text{ou encore}\qquad
\sum_{k=1}^n\frac1k\underset{+\infty}\sim\ln n.$$

Indications :

1. Rappelons que, pour tout $x>-1$, $\ln(1+x)\le x$.
2. Posons $u_n=\sum_{k=1}^n1/k-\ln(n+1)$ et $v_n=\sum_{k=1}^n1/k-\ln n$. Montrer que les suites $u_n$ et $v_n$ sont adjacentes.

Le support s’arrête à ces indications.
