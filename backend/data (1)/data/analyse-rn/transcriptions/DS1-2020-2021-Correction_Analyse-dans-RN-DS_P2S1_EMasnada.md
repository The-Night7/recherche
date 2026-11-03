---
source: "PREING2-S1/Analyse-dans-RN-DS/DS1-2020-2021-Correction_Analyse-dans-RN-DS_P2S1_EMasnada.pdf"
pages: 9
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Analyse dans Rn — DS1 2020–2021 : sujet et corrigé

## Page 1

### Exercice 1 — Questions de cours (5,25 points)

#### Partie 1 — Définitions (2,25 points)

1. Soit $E$ un espace vectoriel réel et $N$ une application de $E$ dans $\mathbb R_+$. Sous quelles conditions $N$ est-elle une norme ? (0,75 point.)
2. Donner la définition d’un ouvert. (0,5 point.)
3. Dans un espace vectoriel normé $(E,N)$, pour $A\subset E$, définir l’intérieur $\mathring A$ (0,5 point) et l’adhérence $\overline A$ (0,5 point).

**Solutions.**

1. $N$ est une norme si elle vérifie la séparation $N(x)=0\Rightarrow x=0_E$, l’homogénéité $N(\lambda x)=|\lambda|N(x)$ pour $\lambda\in\mathbb R$, et l’inégalité triangulaire $N(x+y)\le N(x)+N(y)$. Chaque propriété vaut 0,25 point. **Coquille de l’énoncé :** le PDF écrit une application à valeurs dans $\mathbb N$ ; le codomaine attendu est $\mathbb R_+$.
2. $A$ est ouvert si et seulement si $\forall x\in A,\ \exists r>0,\ B(x,r)\subset A$. On peut aussi dire que $A$ est voisinage de chacun de ses points.
3. Les définitions sont
$$x\in\mathring A\iff\exists r>0,\ B(x,r)\subset A,$$
$$x\in\overline A\iff\forall r>0,\ B(x,r)\cap A\ne\varnothing.$$

## Page 2

#### Exercice 1 — Partie 2 : démonstrations de cours (3 points)

Dans un espace vectoriel normé, pour $A,B\subset E$, montrer :
$$\overline{A\cup B}=\overline A\cup\overline B\quad(2\text{ points}),$$
$$\overline{A\cap B}\subset\overline A\cap\overline B\quad(1\text{ point}).$$

**1.** Comme $A\subset A\cup B$ et $B\subset A\cup B$, la monotonie de l’adhérence donne $\overline A\cup\overline B\subset\overline{A\cup B}$. Réciproquement, $A\cup B\subset\overline A\cup\overline B$, et cette dernière union est fermée, comme union finie de fermés. Donc
$$\overline{A\cup B}\subset\overline{\overline A\cup\overline B}=\overline A\cup\overline B.$$
Les deux inclusions établissent l’égalité (1 point chacune).

**2.** Les inclusions $A\cap B\subset A$ et $A\cap B\subset B$ donnent $\overline{A\cap B}\subset\overline A$ et $\overline{A\cap B}\subset\overline B$, donc l’inclusion dans leur intersection.

## Page 3

### Exercice 2 — Normes sur l’espace des fonctions (10,25 points)

Soit $E=\{f\in C^1([0,1],\mathbb R):f(0)=0\}$. On définit
$$N(f)=\sup_{[0,1]}|f|+\sup_{[0,1]}|f'|,\qquad\nu(f)=\sup_{[0,1]}|f+f'|.$$
1. Ces applications sont-elles des normes sur $E$ ? (4,5 points.)
2. Posons $g(x)=e^xf(x)$. Montrer : (a) $|g'(x)|\le e\nu(f)$ (0,5 point) ; (b) $|g(x)|\le e\nu(f)$ (1 point) ; (c) $|f(x)|\le e\nu(f)$ et $|f'(x)|\le(1+e)\nu(f)$ (2 points).
3. Trouver $\alpha,\beta>0$ tels que $\alpha\nu(f)\le N(f)\le\beta\nu(f)$. (2 points.)
4. Que déduire des deux normes ? (0,25 point.)

**1. Étude de $N$.** Si $N(f)=0$, alors $f=f'=0$ sur $[0,1]$, donc $f=0$ (0,25 point). Pour $\lambda\in\mathbb R$, $N(\lambda f)=|\lambda|N(f)$ (0,25 point). Pour l’inégalité triangulaire (1,5 point), on utilise séparément
$$|f(x)+g(x)|\le|f(x)|+|g(x)|\le\sup|f|+\sup|g|,$$
$$|f'(x)+g'(x)|\le|f'(x)|+|g'(x)|\le\sup|f'|+\sup|g'|.$$

## Page 4

**Exercice 2 — 1, suite.** En prenant le supremum dans chacune des deux inégalités puis en les ajoutant, on obtient $N(f+g)\le N(f)+N(g)$. Donc $N$ est une norme.

**Note sur le raisonnement imprimé :** le PDF additionne d’abord les expressions ponctuelles puis prend un seul supremum. Cela ne donne pas directement la somme des deux suprema définissant $N$ ; il faut les traiter séparément comme ci-dessus.

**Étude de $\nu$.** Si $\nu(f)=0$, $f'+f=0$, donc $f(x)=Ce^{-x}$. Comme $f(0)=0$, $C=0$, et $f=0$ (0,75 point). L’homogénéité $\nu(\lambda f)=|\lambda|\nu(f)$ est immédiate (0,25 point). Enfin,
$$|f+f'+g+g'|\le|f+f'|+|g+g'|\le\nu(f)+\nu(g).$$
En prenant le supremum, $\nu(f+g)\le\nu(f)+\nu(g)$ (1,5 point). Ainsi $\nu$ est une norme.

**2a.** $g'(x)=e^x(f(x)+f'(x))$, donc $|g'(x)|\le e\nu(f)$ pour $x\in[0,1]$ (0,5 point).

**2b.** Comme $g(0)=0$,
$$|g(x)|=\left|\int_0^xg'(t)\,dt\right|\le\int_0^x|g'(t)|\,dt\le xe\nu(f)\le e\nu(f)$$
(1 point).

## Page 5

**Exercice 2 — 2c.** $|f(x)|=e^{-x}|g(x)|\le|g(x)|\le e\nu(f)$ (0,5 point). Puis
$$|f'(x)|\le|f'(x)+f(x)|+|f(x)|\le(1+e)\nu(f)$$
(1,5 point).

**3.** Les deux bornes uniformes donnent
$$N(f)\le e\nu(f)+(1+e)\nu(f)=(1+2e)\nu(f),$$
donc $\beta=1+2e$ (1 point). D’autre part, $|f(x)+f'(x)|\le\sup|f|+\sup|f'|=N(f)$, d’où $\nu(f)\le N(f)$ et $\alpha=1$ (1 point). Ainsi
$$\nu(f)\le N(f)\le(1+2e)\nu(f).$$
**4.** Les deux normes sont équivalentes (0,25 point).

### Exercice 3 — Ouvert, fermé, adhérence et intérieur (5 points)

Pour chacun des ensembles, déterminer s’il est ouvert, fermé ou aucun des deux, puis son adhérence et son intérieur.

**1.** $U_1=A\cup B$, où
$$A=\{(x,y)\in\mathbb R^2:0\le x\le1,\ |y|\le1-x\},$$
$$B=\{(x,y)\in\mathbb R^2:-1\le x\le0,\ |y|\le1+x\}.$$

## Page 6

**Exercice 3 — ensembles 2 et 3.**
$$U_2=\{(x,y)\in\mathbb R^2:\tfrac12x^2+3y^2\le1\},$$
$$U_3=]-\infty,0]\cup]-1,1[\cup[3,6[\cup\{7\}.$$

**Solutions. 1.** $U_1=\overline B_1((0,0),1)=\{(x,y):|x|+|y|\le1\}$. Il est fermé et non ouvert (0,5 point), $\overline U_1=U_1$ (0,5 point), et $\mathring U_1=B_1((0,0),1)$ (0,5 point).

**2.** Pour $F(x,y)=x^2/2+3y^2$, continue, $U_2=F^{-1}(]-\infty,1])$ est fermé (0,5 point), donc $\overline U_2=U_2$ (0,5 point). Posons $C=\{F<1\}$. C’est un ouvert inclus dans $U_2$, donc $C\subset\mathring U_2$. Pour la réciproque, il reste à montrer que tout point de $U_2\setminus C=\{F=1\}$ a, dans chacune de ses boules, un point hors de $U_2$ (intérieur : 1 point).

**Remarque du corrigé et correction.** Le texte propose, sans preuve, la « conjecture » $\mathring{F^{-1}(B)}=F^{-1}(\mathring B)$ pour toute application continue. Elle est fausse en général : si $F$ est constante nulle et $B=\{0\}\subset\mathbb R$, le premier membre est tout le domaine ouvert, et le second est vide. La continuité assure seulement $F^{-1}(\mathring B)\subset\mathring{F^{-1}(B)}$. La preuve spécifique à l’ellipse évite cette conjecture.

## Page 7

**Exercice 3 — 2, fin.** Les points où $F=1$ constituent le bord de l’ellipse. Pour un tel point $X$, les points $(1+t)X$, $t>0$, sont arbitrairement proches de $X$ et vérifient $F((1+t)X)=(1+t)^2>1$. Ainsi aucun n’est intérieur, et $\mathring U_2=C$. En particulier, $U_2$ n’est pas ouvert.

**3.** $U_3=]-\infty,1[\cup[3,6[\cup\{7\}$. Il n’est pas ouvert, à cause de $3$ ou du point isolé $7$ (0,25 point), ni fermé, car il omet les points adhérents $1$ et $6$ (0,25 point). Par adhérence d’une union finie,
$$\overline U_3=]-\infty,1]\cup[3,6]\cup\{7\}\quad(0,5\text{ point}).$$
L’ouvert $C=]-\infty,1[\cup]3,6[$ est inclus dans $U_3$, tandis que les points restants $3$ et $7$ n’admettent aucune boule incluse dans $U_3$. Donc $\mathring U_3=C$ (0,5 point). Le PDF écrit ici $U_2$ dans une condition concernant $U_3$ : coquille d’indice.

### Exercice 4 — Limites de fonctions

Déterminer les limites en $(0,0)$ de
$$f_1(x,y)=\frac{x^3+y^3}{x^2+y^4}\quad(0,5\text{ point}),$$
$$f_2(x,y)=\frac{x^3y^2}{x^6+y^4}\quad(0,5\text{ point}),$$
$$f_3(x,y)=\frac{x^2+y^2}{1-e^{x^2+y^2}}\quad(1\text{ point}).$$

## Page 8

**Exercice 4 — suite de l’énoncé.**

**4.** Limite en $(0,0,0,0)$ de
$$f_4(x,y,u,v)=\frac{x^3+y^3-\tfrac12u^3-v^3}{x^3+y^2}\quad(1\text{ point}).$$
**5.** Limite en $(0,0)$ de
$$f_5(x,y)=\frac{\sqrt{x^2+y^2}}{|x|\sqrt{|y|}+|y|\sqrt{|x|}}\quad(1,5\text{ point}).$$
Indication : montrer $|x|\sqrt{|y|}+|y|\sqrt{|x|}\le2\max(|x|,|y|)^{3/2}$.

**Solutions.**

1. $f_1(0,y)=1/y$ tend vers des infinis de signes opposés suivant le côté : pas de limite (0,5 point).
2. Sur les axes, $f_2=0$, alors que pour $x>0$, $f_2(x,x^{3/2})=x^6/(2x^6)=1/2$. Pas de limite (0,5 point).
3. En coordonnées polaires, $x^2+y^2=\rho^2$ et $f_3=\rho^2/(1-e^{\rho^2})$. Puisque $e^t=1+t+o(t)$,
$$\frac{\rho^2}{1-e^{\rho^2}}=\frac{\rho^2}{-\rho^2+o(\rho^2)}\to-1.$$
La limite vaut $-1$ (1 point).
4. $f_4(x,0,0,0)=1$ et $f_4(x,0,x,0)=1/2$ pour $x\ne0$. Pas de limite (1 point).

## Page 9

**Exercice 4 — 5.** Si $M=\max(|x|,|y|)=|y|$, alors
$$|x|\sqrt{|y|}\le|y|^{3/2},\qquad|y|\sqrt{|x|}\le|y|^{3/2}.$$
Si $M=|x|$, le raisonnement symétrique donne la même borne. Donc
$$|x|\sqrt{|y|}+|y|\sqrt{|x|}\le2M^{3/2}\quad(0,5\text{ point}).$$
Or $\sqrt{x^2+y^2}\ge M$. Sur le domaine où le dénominateur est non nul (donc $xy\ne0$),
$$f_5(x,y)\ge\frac{M}{2M^{3/2}}=\frac1{2\sqrt M}\quad(0,5\text{ point}).$$
Quand $(x,y)\to(0,0)$ dans ce domaine, $M\to0$, donc $f_5(x,y)\to+\infty$ (0,5 point).

**Correction de la conclusion imprimée :** le PDF annonce « plus ou moins l’infini ». La fonction est positive sur son domaine ; la limite est précisément $+\infty$.
