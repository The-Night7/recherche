# Analyse dans Rn — Correction des TDs (ancienne numérotation)

> Source : `PREING2-S1/Analyse-dans-RN/TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf`.
> Auteur : Elian Masnada ; couverture du 25 novembre 2020. 154 pages. La copie intitulée 2024–2025 est identique octet pour octet.
> Transcription : texte natif confronté aux pages du PDF, formules et figures vérifiées ; rapprochement des exercices communs avec les neuf transcriptions de TD 2025–2026, puis rétablissement de l’ordre et des exercices de l’ancienne édition. Les raisonnements sont remis en forme sans reproduire les répétitions de mise en page. Les corrections, compléments et réponses absentes de la source sont signalés. Les repères de pages se chevauchent lorsqu’une page contient plusieurs exercices.
> Vérification : 10 octobre 2026.

## Couverture et attribution — pages 1–2

**Correction des TDs d’analyse dans $\mathbb R^n$ — Elian Masnada — 25 novembre 2020.** L’auteur invite à lui communiquer les remarques à `elian.masnada@cyu.fr`.

La note de la page 2 attribue les corrections rouge vif à Elian Masnada et les corrections bordeaux à M. Masereel (cinq exercices ou parties d’exercice). La transcription ne reprend pas les couleurs.

## TD1, exercice 1 — Normes de Rn — pages 2–6

> La question 7 est laissée en autonomie dans le PDF ; sa description géométrique ci-dessous est un complément de la transcription 2025–2026.


**Énoncé.** Soit $E = \mathbb{R}^n$. Pour tout $x = (x_1, \dots, x_n) \in \mathbb{R}^n$, on pose
$$\|x\|_1 = \sum_{i=1}^n |x_i| \qquad \|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} \qquad \|x\|_\infty = \max_{1 \le i \le n} |x_i|$$

1. Démontrer que $\|\cdot\|_1$, $\|\cdot\|_2$ et $\|\cdot\|_\infty$ sont des normes. *Indication :* pour $\|\cdot\|_2$, on utilisera l'inégalité de Cauchy-Schwarz, admise ici : $|\langle u | v \rangle| \le \|u\|_2 \|v\|_2$ où $\langle u | v \rangle = \sum_{i=1}^n u_i v_i$.
2. Démontrer que pour tous $a, b \ge 0$ : $\sqrt{a+b} \le \sqrt{a} + \sqrt{b}$.
3. Généralisation : montrer que pour tous $a_1, \dots, a_n \ge 0$, $\sqrt{\sum_{i=1}^n a_i} \le \sum_{i=1}^n \sqrt{a_i}$.
4. En déduire que pour tout $x$, $\|x\|_2 \le \|x\|_1$.
5. Démontrer que pour tout $x$, $\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le n \|x\|_\infty$.
6. Les 3 normes sont-elles équivalentes ?
7. Représenter, dans $\mathbb{R}^2$, la boule fermée unité $\overline{B}\big((0,0), 1\big)$ pour chacune de ces normes. (facultatif)

**Correction.**

**1.** Une application $N : E \to \mathbb{R}_+$ est une norme si elle vérifie :

- (séparation) $N(x) = 0 \Rightarrow x = 0_E$ ;
- (homogénéité) $N(\lambda x) = |\lambda|\, N(x)$ pour tout $\lambda \in \mathbb{R}$ ;
- (inégalité triangulaire) $N(x+y) \le N(x) + N(y)$.

*Norme $\|\cdot\|_1$.*

- Si $\|x\|_1 = \sum_i |x_i| = 0$, c'est une somme de termes positifs, donc tous sont nuls : $x_i = 0$ pour tout $i$, et $x = 0_{\mathbb{R}^n}$.
- $\|\lambda x\|_1 = \sum_i |\lambda x_i| = |\lambda| \sum_i |x_i| = |\lambda|\, \|x\|_1$.
- Pour tout $i$, $|x_i + y_i| \le |x_i| + |y_i|$ ; en sommant, $\|x+y\|_1 \le \|x\|_1 + \|y\|_1$.

*Norme $\|\cdot\|_2$.*

- Si $\|x\|_2 = 0$ alors $\sum_i x_i^2 = 0$, donc $x_i = 0$ pour tout $i$.
- $\|\lambda x\|_2 = \sqrt{\sum_i \lambda^2 x_i^2} = |\lambda| \sqrt{\sum_i x_i^2} = |\lambda|\, \|x\|_2$.
- On développe, puis on utilise Cauchy-Schwarz :
$$\|x+y\|_2^2 = \sum_{i=1}^n (x_i + y_i)^2 = \sum_{i=1}^n x_i^2 + \sum_{i=1}^n y_i^2 + 2\sum_{i=1}^n x_i y_i$$
$$\le \|x\|_2^2 + \|y\|_2^2 + 2\|x\|_2 \|y\|_2 = \big(\|x\|_2 + \|y\|_2\big)^2$$
Les deux membres sont positifs : en prenant la racine carrée, $\|x+y\|_2 \le \|x\|_2 + \|y\|_2$.

> **Erreur corrigée :** l'ancienne correction écrivait $(x_i + y_i)^2 = x_i^2 + y_i^2 + x_i y_i$ ; il manque le facteur $2$ devant $x_i y_i$.

*Norme $\|\cdot\|_\infty$.*

- Si $\max_i |x_i| = 0$ alors $|x_i| = 0$ pour tout $i$.
- $\|\lambda x\|_\infty = \max_i |\lambda|\,|x_i| = |\lambda| \max_i |x_i| = |\lambda|\, \|x\|_\infty$.
- Pour tout $i$, $|x_i + y_i| \le |x_i| + |y_i| \le \|x\|_\infty + \|y\|_\infty$. C'est vrai pour tout $i$, en particulier pour celui qui réalise le maximum de $|x_i + y_i|$ : $\|x+y\|_\infty \le \|x\|_\infty + \|y\|_\infty$.

Les trois applications sont donc des normes.

**2.** Pour $a, b \ge 0$, on a $2\sqrt{ab} \ge 0$, donc
$$0 \le a + b \le a + b + 2\sqrt{ab} = \big(\sqrt{a} + \sqrt{b}\big)^2$$
La fonction racine carrée est croissante sur $\mathbb{R}_+$ : $\sqrt{a+b} \le \sqrt{a} + \sqrt{b}$.

**3.** Même idée : en développant le carré de la somme,
$$0 \le \sum_{i=1}^n a_i \le \sum_{i=1}^n a_i + 2\sum_{i<j} \sqrt{a_i a_j} = \Big(\sum_{i=1}^n \sqrt{a_i}\Big)^2$$
et on prend la racine carrée : $\sqrt{\sum_i a_i} \le \sum_i \sqrt{a_i}$.

**4.** On applique la question 3 avec $a_i = x_i^2 \ge 0$, en remarquant que $\sqrt{x_i^2} = |x_i|$ :
$$\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} \le \sum_{i=1}^n \sqrt{x_i^2} = \sum_{i=1}^n |x_i| = \|x\|_1$$

**5.** L'inégalité $\|x\|_2 \le \|x\|_1$ vient d'être démontrée.

- $\|x\|_\infty \le \|x\|_2$ : si $k$ est un indice tel que $|x_k| = \|x\|_\infty$, alors $\|x\|_2^2 = x_k^2 + \sum_{i \ne k} x_i^2 \ge x_k^2 = \|x\|_\infty^2$.
- $\|x\|_1 \le n\|x\|_\infty$ : pour tout $i$, $|x_i| \le \|x\|_\infty$ ; en sommant les $n$ inégalités, $\sum_i |x_i| \le n \|x\|_\infty$.

Finalement, pour tout $x \in \mathbb{R}^n$ : $\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le n \|x\|_\infty$.

**6.** Oui, et de deux façons :

- en dimension finie, toutes les normes sont équivalentes (théorème du cours) ;
- directement avec la question 5 : $\|x\|_\infty \le \|x\|_1 \le n\|x\|_\infty$ montre que $\|\cdot\|_1$ et $\|\cdot\|_\infty$ sont équivalentes, et $\|x\|_\infty \le \|x\|_2 \le n\|x\|_\infty$ que $\|\cdot\|_2$ et $\|\cdot\|_\infty$ le sont. Par transitivité, les trois normes sont équivalentes.

**7.** Dans $\mathbb{R}^2$, la boule unité fermée est :

- pour $\|\cdot\|_1$ : le carré « sur la pointe » de sommets $(\pm 1, 0)$ et $(0, \pm 1)$ (d'équation $|x| + |y| \le 1$) ;
- pour $\|\cdot\|_2$ : le disque de centre $(0,0)$ et de rayon $1$ ;
- pour $\|\cdot\|_\infty$ : le carré $[-1, 1] \times [-1, 1]$.

On retrouve visuellement la question 5 : chaque boule contient la précédente.

## TD1, exercice 2 — Norme pondérée sur Rn — pages 6–7

**Énoncé.** Pour $a_1,\ldots,a_n\in\mathbb R$, on définit $N(x)=\sum_{i=1}^na_i|x_i|$. Donner une condition nécessaire et suffisante pour que $N$ soit une norme.

**Réponse.** Il faut et il suffit que tous les $a_i$ soient strictement positifs. Si $a_j=0$, tout vecteur porté par la $j$-ième coordonnée a une image nulle, ce qui contredit la séparation ; la positivité impose $a_j>0$ pour chaque vecteur de base. Réciproquement, une somme de termes positifs est nulle seulement si chaque $x_i$ est nul ;
$$N(\lambda x)=\sum_i a_i|\lambda x_i|=|\lambda|N(x),$$
et
$$N(x+y)\le\sum_i a_i(|x_i|+|y_i|)=N(x)+N(y).$$

> Coquille source : un $\lambda$ reste à tort dans la parenthèse après sa mise en facteur dans la preuve d’homogénéité.

## TD1, exercice 3 — Normes sur les matrices carrées — pages 7–10


**Énoncé.** Soit $a \in \mathcal{M}_n(\mathbb{R})$. On définit les deux applications
$$N_1 : a \longmapsto \max_{1 \le i \le n} \Big( \sum_{j=1}^n |a_{ij}| \Big) \qquad N_2 : a \longmapsto \sqrt{\operatorname{Tr}({}^t a\, a)}$$

1. Montrer que ces deux applications sont des normes.
2. Sont-elles équivalentes ?

**Correction.**

**1.** *Pour $N_1$.*

- Si $N_1(a) = 0$, alors pour chaque ligne $i$, $\sum_j |a_{ij}| \le N_1(a) = 0$ : tous les $a_{ij}$ sont nuls, et $a$ est la matrice nulle.
- $N_1(\lambda a) = \max_i \sum_j |\lambda a_{ij}| = |\lambda| \max_i \sum_j |a_{ij}| = |\lambda|\, N_1(a)$.
- Pour tous $i, j$, $|a_{ij} + b_{ij}| \le |a_{ij}| + |b_{ij}|$. En sommant sur la ligne $i$ :
$$\sum_{j=1}^n |a_{ij} + b_{ij}| \le \sum_{j=1}^n |a_{ij}| + \sum_{j=1}^n |b_{ij}| \le N_1(a) + N_1(b)$$
C'est vrai pour toute ligne $i$, donc aussi pour le maximum : $N_1(a+b) \le N_1(a) + N_1(b)$.

*Pour $N_2$.* On calcule d'abord $\operatorname{Tr}({}^t a\, a)$. Le coefficient $(i, j)$ de ${}^t a\, a$ est $\sum_k a_{ki} a_{kj}$, donc
$$\operatorname{Tr}({}^t a\, a) = \sum_{i=1}^n \sum_{k=1}^n a_{ki}^2 \qquad\text{et}\qquad N_2(a) = \sqrt{\sum_{i,k} a_{ki}^2}$$
Autrement dit, $N_2$ est la norme euclidienne des $n^2$ coefficients de la matrice. On peut conclure directement avec l'exercice 1 (c'est $\|\cdot\|_2$ sur $\mathbb{R}^{n^2}$), ou refaire la démonstration :

- Si $N_2(a) = 0$, la somme des carrés est nulle, donc tous les $a_{ij}$ sont nuls.
- $N_2(\lambda a) = \sqrt{\sum \lambda^2 a_{ij}^2} = |\lambda|\, N_2(a)$.
- Inégalité triangulaire : si $a$ ou $b$ est nulle, c'est immédiat ; sinon, pour tous réels $\alpha, \beta$, $\alpha\beta \le \frac{1}{2}(\alpha^2 + \beta^2)$. Avec $\alpha = |a_{ij}|/N_2(a)$ et $\beta = |b_{ij}|/N_2(b)$, puis en sommant sur tous les $(i,j)$ :
$$\sum_{i,j} \frac{|a_{ij} b_{ij}|}{N_2(a) N_2(b)} \le \frac{1}{2}\Big( \frac{\sum |a_{ij}|^2}{N_2(a)^2} + \frac{\sum |b_{ij}|^2}{N_2(b)^2} \Big) = \frac{1}{2}(1 + 1) = 1$$
donc $\sum_{i,j} |a_{ij} b_{ij}| \le N_2(a) N_2(b)$. Alors
$$N_2(a+b)^2 = \sum_{i,j} (a_{ij} + b_{ij})^2 \le N_2(a)^2 + N_2(b)^2 + 2\sum_{i,j} |a_{ij} b_{ij}| \le \big(N_2(a) + N_2(b)\big)^2$$
et on prend la racine carrée.

**2.** Oui : $\mathcal{M}_n(\mathbb{R})$ est de dimension finie ($n^2$), donc toutes les normes y sont équivalentes.

### Détail de la démonstration source pour la norme de Frobenius — pages 9–10

Pour $N_2(a)N_2(b)\ne0$, on applique $\alpha\beta\le(\alpha^2+\beta^2)/2$ à $\alpha=|a_{ij}|/N_2(a)$, $\beta=|b_{ij}|/N_2(b)$. En sommant :
$$\sum_{i,j}\frac{|a_{ij}b_{ij}|}{N_2(a)N_2(b)}\le\frac12\left(\frac{\sum_{i,j}|a_{ij}|^2}{N_2(a)^2}+\frac{\sum_{i,j}|b_{ij}|^2}{N_2(b)^2}\right)=1.$$
Ainsi $N_2(a+b)^2\le N_2(a)^2+N_2(b)^2+2N_2(a)N_2(b)$. On prend la racine. Si l’une des matrices est nulle, l’inégalité est immédiate.

> La source omet les carrés aux dénominateurs dans une ligne intermédiaire et ne sépare pas le cas des matrices nulles.

## TD1, exercice 4 — Normes sur les fonctions continues — pages 10–12


**Énoncé.** Soit $E$ l'ensemble des fonctions continues de $[0,1]$ dans $\mathbb{R}$. On définit, pour $f \in E$ :
$$\|f\|_1 = \int_0^1 |f(x)|\,dx \qquad \|f\|_2 = \sqrt{\int_0^1 f^2(x)\,dx} \qquad \|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$$

1. Montrer que $\|\cdot\|_1$ et $\|\cdot\|_\infty$ sont des normes (on admettra que $\|\cdot\|_2$ est bien une norme).
2. Ces trois normes sont-elles équivalentes ?
3. En déduire que $E$ n'est pas un espace de dimension finie.

**Correction.**

**1.** *Pour $\|\cdot\|_1$.*

- Si $\int_0^1 |f(x)|\,dx = 0$ : la fonction $|f|$ est **continue** et positive, d'intégrale nulle, donc elle est nulle sur $[0,1]$ : $f = 0$.
- $\|\lambda f\|_1 = \int_0^1 |\lambda|\,|f(x)|\,dx = |\lambda|\, \|f\|_1$.
- Pour tout $x$, $|f(x) + g(x)| \le |f(x)| + |g(x)|$ ; on intègre (croissance de l'intégrale) : $\|f+g\|_1 \le \|f\|_1 + \|g\|_1$.

> **Précision ajoutée :** l'ancienne correction disait « ce qui implique évidemment $f = 0$ ». C'est la continuité de $f$ qui le garantit : une fonction non continue peut être non nulle en un point et d'intégrale nulle.

*Pour $\|\cdot\|_\infty$* (le sup existe car $f$ est continue sur le segment $[0,1]$, donc bornée).

- Si $\sup |f| = 0$, alors $|f(x)| = 0$ pour tout $x$.
- $\|\lambda f\|_\infty = \sup_x |\lambda|\,|f(x)| = |\lambda|\, \|f\|_\infty$.
- Pour tout $x \in [0,1]$, $|f(x) + g(x)| \le |f(x)| + |g(x)| \le \|f\|_\infty + \|g\|_\infty$. Le membre de droite ne dépend pas de $x$ : c'est un majorant de $|f+g|$, donc $\|f+g\|_\infty \le \|f\|_\infty + \|g\|_\infty$.

**2.** Deux normes $N$ et $N'$ sont équivalentes s'il existe $a, b > 0$ tels que $a N \le N' \le b N$. Pour montrer qu'elles ne le sont pas, il suffit de trouver une suite de fonctions pour laquelle le rapport $N'(f_n) / N(f_n)$ tend vers $0$ ou vers $+\infty$.

Prenons $f_n(x) = x^n$. On calcule :
$$\|f_n\|_1 = \frac{1}{n+1} \qquad \|f_n\|_2 = \frac{1}{\sqrt{2n+1}} \qquad \|f_n\|_\infty = 1$$
Donc, quand $n \to +\infty$ :
$$\frac{\|f_n\|_2}{\|f_n\|_1} = \frac{n+1}{\sqrt{2n+1}} \to +\infty \qquad \frac{\|f_n\|_\infty}{\|f_n\|_1} = n + 1 \to +\infty \qquad \frac{\|f_n\|_\infty}{\|f_n\|_2} = \sqrt{2n+1} \to +\infty$$
Aucune des trois normes n'est équivalente à une autre.

**3.** En dimension finie, toutes les normes sont équivalentes. Ici, on a trouvé des normes non équivalentes : $E$ n'est donc pas de dimension finie (c'est la contraposée du théorème).

## TD1, exercice 5 — Norme elliptique — pages 13–14

**Énoncé.** Pour $a,b>0$, poser $N(x,y)=\sqrt{a^2x^2+b^2y^2}$. Montrer que c’est une norme, dessiner sa boule unité fermée, puis chercher le plus grand $q$ et le plus petit $p$ tels que $q\|\cdot\|_1\le N\le p\|\cdot\|_2$.

**Réponses présentes.** $N(x,y)=0$ entraîne $x=y=0$, car $a,b>0$, et $N(\lambda X)=|\lambda|N(X)$. Pour $X_i=(x_i,y_i)$, appliquer Cauchy–Schwarz aux vecteurs $(ax_1,by_1)$ et $(ax_2,by_2)$ :
$$|a^2x_1x_2+b^2y_1y_2|\le N(X_1)N(X_2).$$
En développant,
$$N(X_1+X_2)^2\le N(X_1)^2+N(X_2)^2+2N(X_1)N(X_2),$$
puis $N(X_1+X_2)\le N(X_1)+N(X_2)$.

La boule est la région $a^2x^2+b^2y^2\le1$, dont le contour est une ellipse de demi-axes $1/a$ et $1/b$.

**La réponse à la question 3 est laissée vide dans la source.** Dans le rappel d’homogénéité, la page 13 imprime $N(X)=|\lambda|N(X)$ ; le membre de gauche doit être $N(\lambda X)$.

## TD1, exercice 6 — Normes sur les polynômes — pages 14–16

Pour $n\ge1$ et $E=\mathbb R_n[X]$, on définit
$$\|P\|=\max_{0\le k\le n}|P^{(k)}(0)|,\qquad N(P)=\sup_{x\in\mathbb R}\frac{|P(x)|}{1+|x|^n}.$$
Montrer que $N$ est bien définie, que ces deux applications sont des normes et qu’il existe $C>0$ tel que $\|P\|\le CN(P)$ pour tout $P$.

**1.** Écrire $P(x)=\sum_{k=0}^na_kx^k$. Alors
$$\frac{P(x)}{1+|x|^n}=a_n\frac{x^n}{1+|x|^n}+\sum_{k=0}^{n-1}\frac{a_kx^k}{1+|x|^n}.$$
La somme tend vers zéro à l’infini et le premier terme est borné ; le quotient est continu sur $\mathbb R$, donc borné, et $N(P)$ est fini.

> Précisions : $\mathbb R_n[X]$ désigne les polynômes de degré **au plus** $n$. La limite du premier terme à $-\infty$ est $(-1)^na_n$, et non toujours $a_n$ comme écrit dans la source.

**2.** $P^{(k)}(0)=k!a_k$ : si $\|P\|=0$, tous les coefficients sont nuls. La linéarité de la dérivation donne l’homogénéité. Pour chaque $k$,
$$|(P+Q)^{(k)}(0)|\le|P^{(k)}(0)|+|Q^{(k)}(0)|\le\|P\|+\|Q\|,$$
puis prendre le maximum.

Pour $N$, séparation et homogénéité sont immédiates. Pour tout $x$,
$$\frac{|P(x)+Q(x)|}{1+|x|^n}\le\frac{|P(x)|}{1+|x|^n}+\frac{|Q(x)|}{1+|x|^n}\le N(P)+N(Q).$$
Le passage au supremum donne l’inégalité triangulaire.

**3.** L’espace est de dimension finie, donc les normes sont équivalentes : il existe $a,b>0$ tels que $aN(P)\le\|P\|\le bN(P)$. Prendre $C=b$.

## TD1, exercice 7 — Troisième inégalité triangulaire — page 17

Montrer $\|x\|+\|y\|\le\|x-y\|+\|x+y\|$.

La source écrit
$$2\|x\|=\|(x+y)+(x-y)\|\le\|x+y\|+\|x-y\|,$$
$$2\|y\|=\|(y+x)+(y-x)\|\le\|x+y\|+\|x-y\|.$$
Additionner et diviser par deux.

## TD1, exercice 8 — Autre norme — page 17

Pour $N(x,y)=4|x|+|y|$, demander si $N$ est une norme, dessiner sa boule unité fermée, en donner les symétries et préciser la symétrie générale d’une boule fermée.

**Réponse source :** « À rédiger plus tard car l’exercice est vraiment trivial. » Aucune correction n’est présente ici. Une correction ajoutée figure dans le TD1 2025–2026, exercice 4.

## TD1, exercice 9 — Distances — pages 17–20

> La démonstration de la question 6 est un complément du TD 2025–2026 : le PDF donne seulement la conclusion « distance, non issue d’une norme » et laisse la preuve en exercice.


**Énoncé.** On définit des applications de $\mathbb{R} \times \mathbb{R}$ dans $\mathbb{R}$ ($x, y \in \mathbb{R}$) :
$$d_1(x,y) = (x-y)^2 \qquad d_2(x,y) = \sqrt{|x-y|} \qquad d_3(x,y) = |x^2 - y^2|$$
$$d_4(x,y) = |x - 2y| \qquad d_5(x,y) = |x^3 - y^3|$$
Ces applications sont-elles des distances ? Sont-elles associées à des normes ?

**Correction.**

*Rappels.* Une application $d : E^2 \to \mathbb{R}_+$ est une distance si

- $d(x, y) = 0 \iff x = y$ ;
- $d(x, y) = d(y, x)$ ;
- $d(x, y) \le d(x, z) + d(z, y)$ pour tout $z$.

Si $d$ est associée à une norme ($d(x,y) = \|x - y\|$), alors en particulier $d(\lambda x, \lambda y) = |\lambda|\, d(x, y)$ et $x \mapsto d(x, 0)$ est une norme.

**$d_1(x,y) = (x-y)^2$ : pas une distance.** Les deux premières propriétés sont vraies, mais pas l'inégalité triangulaire. Avec $x = 3$, $z = 2$, $y = 1$ :
$$d_1(3, 1) = 4 \quad > \quad d_1(3, 2) + d_1(2, 1) = 1 + 1 = 2$$

> **Erreur corrigée :** l'ancienne correction concluait avec « $2(x-z)(z-y) = 1$ » ; pour ces valeurs, ce terme vaut $2$, et c'est lui qui fait dépasser : $(x-y)^2 = (x-z)^2 + (z-y)^2 + 2(x-z)(z-y)$.

**$d_2(x,y) = \sqrt{|x-y|}$ : une distance, non associée à une norme.**

- $d_2(x, y) = 0 \iff |x - y| = 0 \iff x = y$ ; la symétrie vient de $|x - y| = |y - x|$.
- $|x - y| \le |x - z| + |z - y|$, et la racine est croissante, donc avec l'exercice 1 (question 2) :
$$\sqrt{|x-y|} \le \sqrt{|x-z| + |z-y|} \le \sqrt{|x-z|} + \sqrt{|z-y|}$$
- Mais $d_2(\lambda x, 0) = \sqrt{|\lambda|}\sqrt{|x|} \ne |\lambda|\, d_2(x, 0)$ en général (par exemple $\lambda = 4$, $x = 1$ : $2 \ne 4$). Elle n'est donc pas associée à une norme.

**$d_3(x,y) = |x^2 - y^2|$ : pas une distance**, car $d_3(1, -1) = 0$ alors que $1 \ne -1$.

**$d_4(x,y) = |x - 2y|$ : pas une distance**, car $d_4(2, 1) = 0$ alors que $2 \ne 1$ (et même $d_4(x, x) = |x| \ne 0$ pour $x \ne 0$).

**$d_5(x,y) = |x^3 - y^3|$ : une distance, non associée à une norme.**

- $x \mapsto x^3$ est injective sur $\mathbb{R}$, donc $d_5(x, y) = 0 \iff x^3 = y^3 \iff x = y$ ; la symétrie est claire.
- C'est la distance usuelle entre $x^3$ et $y^3$ : $|x^3 - y^3| \le |x^3 - z^3| + |z^3 - y^3|$.
- $d_5(\lambda x, \lambda y) = |\lambda|^3\, d_5(x, y)$, différent de $|\lambda|\, d_5(x,y)$ pour $|\lambda| \ne 1$ et $x \ne y$ : elle n'est pas associée à une norme.

> **Complément :** l'ancienne correction laissait ce cas « en exercice » ; la rédaction ci-dessus a été ajoutée pour cette transcription.

## TD2, exercice 1 — Normes équivalentes et topologie — pages 21–23

Soient deux normes équivalentes sur $E$, avec $\alpha\|z\|_1\le\|z\|_2\le\beta\|z\|_1$ pour $\alpha,\beta>0$. Montrer les inclusions de boules, puis l’équivalence des notions d’ouvert et de fermé.

Si $\|x-a\|_1<r$, alors $\|x-a\|_2<\beta r$, d’où
$$B_1(a,r)\subset B_2(a,\beta r).$$
Si $\|x-a\|_2<r''$, alors $\|x-a\|_1<r''/\alpha$, donc
$$B_2(a,r'')\subset B_1(a,r''/\alpha).$$
Si $A$ est ouvert pour la norme 1, pour $x\in A$ choisir $R>0$ avec $B_1(x,R)\subset A$. Alors $B_2(x,\alpha R)\subset A$. Réciproquement, $B_2(x,R)\subset A$ implique $B_1(x,R/\beta)\subset A$. Les ouverts coïncident, donc leurs complémentaires, les fermés, également.

En dimension finie, toutes les normes étant équivalentes, les notions d’ouvert et de fermé ne dépendent pas de la norme choisie.

## TD2, exercice 2 — Boules ouvertes et fermées — pages 23–25


**Énoncé.** Soit $(E, \|\cdot\|)$ un espace vectoriel normé.

1. Montrer qu'une boule fermée n'est pas un ouvert.
2. Montrer qu'une boule ouverte n'est pas un fermé.

**Correction.** On suppose $E \ne \{0\}$ (sinon $E = \{0\}$ est à la fois ouvert et fermé, et l'énoncé est faux) et $r > 0$. On note $B(a, r)$ la boule ouverte et $\overline{B}(a, r)$ la boule fermée de centre $a$ et de rayon $r$.

Comme $E \ne \{0\}$, il existe des points sur la sphère : si $u \ne 0$, le point $x = a + \frac{r}{\|u\|} u$ vérifie $\|x - a\| = r$. C'est en un tel point du bord que tout se joue.

**1.** Soit $x$ tel que $\|x - a\| = r$ : il appartient à $\overline{B}(a, r)$. Montrons qu'**aucune** boule $B(x, \varepsilon)$ n'est contenue dans $\overline{B}(a, r)$. Soit $\varepsilon > 0$ ; on s'éloigne du centre en posant
$$y = x + \frac{\varepsilon}{2r}(x - a)$$

- $\|y - x\| = \frac{\varepsilon}{2r}\|x - a\| = \frac{\varepsilon}{2} < \varepsilon$, donc $y \in B(x, \varepsilon)$ ;
- $y - a = \big(1 + \frac{\varepsilon}{2r}\big)(x - a)$, donc $\|y - a\| = \big(1 + \frac{\varepsilon}{2r}\big) r > r$ : $y \notin \overline{B}(a, r)$.

Ainsi $\overline{B}(a, r)$ n'est un voisinage d'aucun point de sa sphère : ce n'est pas un ouvert.

**2.** $B(a, r)$ est un fermé si et seulement si son complémentaire $\complement_E B(a, r) = \{y : \|y - a\| \ge r\}$ est un ouvert. Le même point $x$ (avec $\|x - a\| = r$) est dans ce complémentaire. Soit $\varepsilon > 0$, qu'on peut supposer $< 2r$ (une boule plus petite suffit). On se rapproche du centre :
$$y = x - \frac{\varepsilon}{2r}(x - a)$$

- $\|y - x\| = \frac{\varepsilon}{2} < \varepsilon$, donc $y \in B(x, \varepsilon)$ ;
- $\|y - a\| = \big(1 - \frac{\varepsilon}{2r}\big) r < r$, donc $y \in B(a, r)$, c'est-à-dire $y \notin \complement_E B(a, r)$.

Aucune boule centrée en $x$ n'est contenue dans le complémentaire : il n'est pas ouvert, donc $B(a, r)$ n'est pas fermée.

> **Précision ajoutée :** l'ancienne correction ne mentionnait ni $E \ne \{0\}$ ni la condition $\varepsilon < 2r$, nécessaire pour que $1 - \frac{\varepsilon}{2r}$ reste positif.

## TD2, exercice 3 — Classification d’ensembles — pages 25–31


**Énoncé.** Déterminer si les ensembles suivants sont des ouverts, des fermés, les deux ou aucun des deux.

1. $A = [0, 1[$
2. $C = [0, +\infty[$
3. $D = \,]0, 1[\, \cup \{2\}$
4. $E = \mathbb{N}$
5. $F = \{(x, y) \in \mathbb{R}^2 \,/\, x^2 + y^2 < 4\}$
6. $G = \{(x, y) \in \mathbb{R}^2 \,/\, x^2 + y^2 \le 2\}$
7. $H = \{(x, y) \in \mathbb{R}^2 \,/\, 0 < |x - 1| < 1\}$
8. $I = \{(x, y) \in \mathbb{R}^2 \,/\, |x| < 1 \text{ et } |y| \le 1\}$

**Correction.** Méthode : pour montrer qu'un ensemble $X$ **n'est pas ouvert**, on cherche un point $p \in X$ tel que toute boule $B(p, r)$ contient un point hors de $X$. Pour montrer qu'il **n'est pas fermé**, on fait la même chose avec son complémentaire. En dimension finie, le choix de la norme ne change rien (TD2 de l'ancienne feuille, exercice 1) : on prend $|\cdot|$ dans $\mathbb{R}$ et $\|\cdot\|_2$ dans $\mathbb{R}^2$.

**1. $A = [0, 1[$ : ni ouvert, ni fermé.**

- *Pas ouvert* : le problème est en $0 \in A$. Pour tout $r > 0$, $y = -\frac{r}{2}$ est dans $B(0, r) = \,]-r, r[$ mais pas dans $A$.
- *Pas fermé* : $\complement_{\mathbb{R}} A = \,]-\infty, 0[\, \cup [1, +\infty[$ contient $1$. Pour tout $r \in \,]0, 1[$, $y = 1 - \frac{r}{2}$ est dans $B(1, r) = \,]1 - r, 1 + r[$ et dans $A$, donc pas dans le complémentaire : celui-ci n'est pas ouvert.

> **Erreur corrigée :** l'ancienne correction notait $B(0, r) = \,]1 - r, 1 + r[$ ; il s'agit de la boule $B(1, r)$.

**2. $C = [0, +\infty[$ : fermé, pas ouvert.**

- *Pas ouvert* : même argument que pour $A$ en $0$ ($y = -\frac{r}{2} \notin C$).
- *Fermé* : $\complement_{\mathbb{R}} C = \,]-\infty, 0[$ est ouvert. Trois façons de le voir :
  - (a) c'est un intervalle ouvert (résultat du cours) ;
  - (b) c'est une réunion d'ouverts : $\,]-\infty, 0[\, = \bigcup_{a < 0} \,]a, 0[$ ;
  - (c) directement : pour $x < 0$, la boule $B\big(x, \frac{|x|}{2}\big) = \,]\frac{3x}{2}, \frac{x}{2}[$ est contenue dans $]-\infty, 0[$ puisque $\frac{x}{2} < 0$.

**3. $D = \,]0, 1[\, \cup \{2\}$ : ni ouvert, ni fermé.**

- *Pas ouvert* : le problème est en $2 \in D$. Pour tout $r > 0$, $y = 2 + \frac{r}{2}$ est dans $B(2, r)$ mais pas dans $D$.
- *Pas fermé* : $\complement_{\mathbb{R}} D = \,]-\infty, 0] \cup [1, 2[\, \cup \,]2, +\infty[$ contient $0$. Pour tout $r \in \,]0, 2[$, $y = \frac{r}{2} \in \,]0, 1[\, \subset D$ est dans $B(0, r)$ : aucune boule centrée en $0$ n'est contenue dans le complémentaire, qui n'est donc pas ouvert.

> **Erreur corrigée :** l'ancienne correction concluait ici « donc $D$ n'est pas un ouvert » ; c'est le complémentaire qui n'est pas ouvert, donc $D$ qui n'est pas fermé.

**4. $E = \mathbb{N}$ : fermé, pas ouvert.**

- *Pas ouvert* : $0 \in \mathbb{N}$, et pour tout $r > 0$, $-\frac{r}{2} \in B(0, r)$ n'est pas un entier naturel.
- *Fermé* : $\complement_{\mathbb{R}} \mathbb{N} = \,]-\infty, 0[\, \cup \,]0, 1[\, \cup \,]1, 2[\, \cup \cdots$ est une réunion d'intervalles ouverts, donc un ouvert.

> **Erreur corrigée :** l'ancienne correction disait « $\mathbb{N}$ est une réunion de singletons, et un singleton n'est pas ouvert, donc $\mathbb{N}$ n'est pas ouvert ». Ce raisonnement est faux : une réunion d'ensembles non ouverts peut être ouverte (par exemple $\mathbb{R} = \bigcup_{x \in \mathbb{R}} \{x\}$). Il manquait aussi $]-\infty, 0[$ dans le complémentaire.

**5. $F$ : ouvert, pas fermé.** $F = \{(x,y) : \|(x,y)\|_2 < 2\}$ est la boule ouverte $B_{\|\cdot\|_2}\big((0,0), 2\big)$. D'après l'exercice 1 et le cours, c'est un ouvert et ce n'est pas un fermé.

**6. $G$ : fermé, pas ouvert.** $G$ est la boule fermée $\overline{B}_{\|\cdot\|_2}\big((0,0), \sqrt{2}\big)$ : c'est un fermé, et d'après l'exercice 1, pas un ouvert.

**7. $H$ : ouvert, pas fermé.** La condition ne porte que sur $x$ : $0 < |x - 1| < 1 \iff x \in \,]0, 1[\, \cup \,]1, 2[$. Donc $H = \big(]0, 1[\, \cup \,]1, 2[\big) \times \mathbb{R}$ : deux bandes verticales ouvertes.

- *Ouvert* : soit $(x, y) \in H$ et $r = \min(|x - 0|, |x - 1|, |x - 2|) > 0$ (la distance de $x$ aux trois droites « interdites » $x = 0$, $x = 1$, $x = 2$). Tout point $(x', y')$ de $B_2\big((x,y), r\big)$ vérifie $|x' - x| < r$, donc $x'$ reste dans le même intervalle que $x$ : $B_2\big((x,y), r\big) \subset H$. (Autre façon : on peut paver $H$ par des boules ouvertes de la norme $\|\cdot\|_\infty$, qui sont des carrés ; une réunion d'ouverts est un ouvert.)
- *Pas fermé* : le point $P = (0, 0)$ est dans le complémentaire ($|0 - 1| = 1$). Pour tout $r \in \,]0, 2[$, le point $Q = \big(\frac{r}{2}, 0\big)$ vérifie $\|Q - P\|_2 = \frac{r}{2} < r$ et $\frac{r}{2} \in \,]0, 1[$, donc $Q \in H$. Aucune boule centrée en $P$ n'est contenue dans le complémentaire : $H$ n'est pas fermé.

> **Erreurs corrigées :** l'ancienne correction écrivait « $y \in B_2(I, r)$ » au lieu de « $J \in B_2(I, r)$ », et concluait « $H$ n'est un fermé » au lieu de « $H$ n'est pas un fermé ».

**8. $I = \,]-1, 1[\, \times [-1, 1]$ : ni ouvert, ni fermé.**

- *Pas ouvert* : $p = (0, 1) \in I$. Pour tout $r > 0$, $q = \big(0, 1 + \frac{r}{2}\big)$ est dans $B_2(p, r)$ mais $|1 + \frac{r}{2}| > 1$, donc $q \notin I$.
- *Pas fermé* : $p = (-1, 0) \notin I$ (car $|-1| \not< 1$). Pour tout $r \in \,]0, 2[$, $q = \big(-1 + \frac{r}{2}, 0\big)$ est dans $B_2(p, r)$ et dans $I$. Aucune boule centrée en $p$ n'est contenue dans le complémentaire : il n'est pas ouvert.

> **Complément :** l'ancienne correction s'arrêtait à « même principe en utilisant le point $(-1, 0)$ » ; la démonstration a été rédigée.

## TD2, exercice 4 — Ouvert majoré — pages 31


**Énoncé.** Soit $A$ un ouvert majoré de $(\mathbb{R}, |\cdot|)$. Montrer que $A$ ne contient pas son majorant.

**Correction.** Montrons plus précisément qu'**aucun majorant** de $A$ n'appartient à $A$ ; en particulier $A$ ne contient pas sa borne supérieure (et n'a donc pas de plus grand élément).

Par l'absurde, supposons qu'un majorant $M$ de $A$ appartienne à $A$. Comme $A$ est ouvert, $A$ est un voisinage de $M$ : il existe $\alpha > 0$ tel que
$$B(M, \alpha) = \,]M - \alpha, M + \alpha[\, \subset A$$
En particulier $M + \frac{\alpha}{2} \in A$. Mais $M + \frac{\alpha}{2} > M$, ce qui contredit le fait que $M$ majore $A$. Donc aucun majorant de $A$ n'est dans $A$.

> **Erreurs corrigées :** l'ancienne correction proposait d'abord une « méthode 1 » fausse : elle affirmait qu'un ouvert de $\mathbb{R}$ est de la forme $]\alpha, \beta[$ (c'est faux, par exemple $]0, 1[\, \cup \,]2, 3[$), puis que $A = \,]-M, M[$. Elle a été retirée. Dans la méthode 2, « $M + \alpha \subset A$ » est remplacé par « $M + \frac{\alpha}{2} \in A$ » : $M + \alpha$ n'est pas dans la boule ouverte $]M - \alpha, M + \alpha[$.

## TD2, exercice 5 — Somme d’ensembles — pages 31–32

Pour $A,B\subset\mathbb R$, poser $A+B=\{a+b:a\in A,b\in B\}$. Montrer que si $A$ ou $B$ est ouvert, $A+B$ est ouvert. La réciproque est-elle vraie ?

Si $A$ est ouvert et $x=a+b\in A+B$, choisir $\varepsilon>0$ tel que $]a-\varepsilon,a+\varepsilon[\subset A$. Pour $y\in]x-\varepsilon,x+\varepsilon[$, $y-b\in A$, donc $y=(y-b)+b\in A+B$. Ainsi $A+B$ est ouvert. Le cas où $B$ est ouvert est symétrique.

La réciproque est fausse :
$$A=]0,1]\cup[2,3[,\qquad B=]1,2]\cup[3,4[,$$
qui ne sont ni l’un ni l’autre ouverts, alors que $A+B=]1,7[$.

> Coquille source : « ils sont tous les deux ouverts » doit se lire « ils ne sont ni l’un ni l’autre ouverts ».

## TD2, exercice 6 — Produit cartésien — pages 32–33

Sur $E\times F$, on pose $\|(x,y)\|=\max(\|x\|_E,\|y\|_F)$. Montrer que c’est une norme, puis que le produit de deux ouverts est ouvert et le produit de deux fermés est fermé.

**1.** Le maximum est nul si et seulement si les deux normes sont nulles, soit $(x,y)=(0_E,0_F)$. L’homogénéité découle de celle des deux normes. Enfin,
$$\|x_1+x_2\|_E\le\|x_1\|_E+\|x_2\|_E\le\|(x_1,y_1)\|+\|(x_2,y_2)\|,$$
et la même majoration vaut pour $\|y_1+y_2\|_F$. Prendre le maximum donne l’inégalité triangulaire.

**2.** Pour $(x,y)\in A\times B$, choisir $r_1,r_2>0$ avec $B_E(x,r_1)\subset A$ et $B_F(y,r_2)\subset B$. Poser $r=\min(r_1,r_2)$ et prendre $(z,t)\in B_{E\times F}((x,y),r)$.

**La correction s’arrête alors à « On a … ».** La fin de la question 2 et la réponse à la question 3 ne figurent pas dans le PDF.

## TD3, exercice 1 — Adhérence et fermé — pages 34–35


**Énoncé.** Soit $(E, \|\cdot\|)$ un espace vectoriel normé. Soient $A$ et $B$ deux ensembles tels que $A \subset B \subset E$ et $B$ fermé.

1. Montrer alors que pour tout $x \in \complement_E B$, il existe $r > 0$ tel que $B(x, r) \cap A = \emptyset$.
2. Peut-on alors avoir $\overline{A} = B$ et si oui sous quelles conditions ?

**Correction.**

**1.** $B$ est fermé, donc $\complement_E B$ est ouvert : pour tout $x \in \complement_E B$, il existe $r > 0$ tel que $B(x, r) \subset \complement_E B$, c'est-à-dire $B(x, r) \cap B = \emptyset$. Comme $A \subset B$, on a a fortiori $B(x, r) \cap A = \emptyset$.

**2.** Rappel : $x \in \overline{A} \iff \forall r > 0,\ B(x, r) \cap A \ne \emptyset$.

La question 1 dit exactement qu'aucun point hors de $B$ n'est adhérent à $A$ : $\overline{A} \subset B$. (On retrouve le fait que $\overline{A}$ est le plus petit fermé contenant $A$.) Mais $B$ peut être trop grand. On a $\overline{A} = B$ si et seulement si tout point de $B$ est adhérent à $A$, c'est-à-dire :
$$\forall x \in B \setminus A,\quad \forall r > 0,\quad B(x, r) \cap A \ne \emptyset$$
Par exemple, avec $A = \,]0, 1[$ : $B = [0, 1]$ convient, mais pas $B = [0, 2]$ (le point $2$ n'est pas adhérent à $A$).

## TD3, exercice 2 — Intérieur et ouvert — pages 35


**Énoncé.** Soit $(E, \|\cdot\|)$ un espace vectoriel normé. Soient $A$ et $B$ deux ensembles tels que $B \subset A \subset E$ et $B$ ouvert.

1. Montrer alors que pour tout $x \in B$, il existe $r > 0$ tel que $B(x, r) \subset A$.
2. Peut-on alors avoir $\mathring{A} = B$ et si oui sous quelles conditions ?

**Correction.**

**1.** $B$ est ouvert : pour tout $x \in B$, il existe $r > 0$ tel que $B(x, r) \subset B$. Comme $B \subset A$, on a $B(x, r) \subset A$.

**2.** Rappel : $x \in \mathring{A} \iff \exists r > 0,\ B(x, r) \subset A$.

La question 1 montre que tout point de $B$ est intérieur à $A$ : $B \subset \mathring{A}$. (On retrouve le fait que $\mathring{A}$ est le plus grand ouvert contenu dans $A$.) Mais $B$ peut être trop petit. On a $\mathring{A} = B$ si et seulement si aucun point de $A \setminus B$ n'est intérieur à $A$ :
$$\forall x \in A \setminus B,\quad \forall r > 0,\quad B(x, r) \not\subset A$$
Par exemple, avec $A = [0, 1]$ : $B = \,]0, 1[$ convient, mais pas $B = \,]0, \frac{1}{2}[$ (le point $\frac{3}{4}$ est intérieur à $A$).

## TD3, exercice 3 — Intérieur et adhérence d’une boule — pages 36–38


**Énoncé.** Soit $(E, \|\cdot\|)$ un espace vectoriel normé. Déterminer l'intérieur et l'adhérence de

1. l'ensemble $A$ qui est la boule fermée de rayon $r$ et de centre $a$ ;
2. l'ensemble $A$ qui est la boule ouverte de rayon $r$ et de centre $a$.

**Correction.** On suppose $E \ne \{0\}$ et $r > 0$, et on note $S(a, r) = \{x : \|x - a\| = r\}$ la sphère, qui est alors non vide.

**1. $A = \overline{B}(a, r)$ : $\overline{A} = A$ et $\mathring{A} = B(a, r)$.**

- *Adhérence* : $A$ est un fermé, donc $\overline{A} = A$.
- *Intérieur* : le candidat est $C = B(a, r)$. C'est un ouvert contenu dans $A$, donc $C \subset \mathring{A}$ (exercice 2). D'après l'exercice 2, il reste à voir qu'aucun point de $A \setminus C = S(a, r)$ n'est intérieur à $A$. Soit $x \in S(a, r)$ et $\varepsilon > 0$ ; posons $y = x + \frac{\varepsilon}{2r}(x - a)$. Alors $\|y - x\| = \frac{\varepsilon}{2} < \varepsilon$, et
$$\|y - a\| = \Big(1 + \frac{\varepsilon}{2r}\Big)\|x - a\| = \Big(1 + \frac{\varepsilon}{2r}\Big) r > r$$
donc $y \in B(x, \varepsilon)$ mais $y \notin A$ : $B(x, \varepsilon) \not\subset A$. Finalement $\mathring{A} = B(a, r)$.

**2. $A = B(a, r)$ : $\mathring{A} = A$ et $\overline{A} = \overline{B}(a, r)$.**

- *Intérieur* : $A$ est un ouvert, donc $\mathring{A} = A$.
- *Adhérence* : le candidat est $C = \overline{B}(a, r)$. C'est un fermé contenant $A$, donc $\overline{A} \subset C$ (exercice 1). Il reste à voir que tout point de $C \setminus A = S(a, r)$ est adhérent à $A$. Soit $x \in S(a, r)$ et $\varepsilon > 0$, qu'on peut prendre $< 2r$ ; posons $y = x - \frac{\varepsilon}{2r}(x - a)$. Alors $\|y - x\| = \frac{\varepsilon}{2} < \varepsilon$, et
$$\|y - a\| = \Big(1 - \frac{\varepsilon}{2r}\Big) r < r$$
donc $y \in B(x, \varepsilon) \cap A$ : cette intersection n'est jamais vide. Finalement $\overline{A} = \overline{B}(a, r)$.

> **Précision ajoutée :** comme au TD2, il faut $\varepsilon < 2r$ pour que $1 - \frac{\varepsilon}{2r} > 0$ ; ce n'est pas une restriction, puisqu'une petite boule $B(x, \varepsilon)$ est contenue dans les plus grandes.

## TD3, exercice 4 — Opérations sur intérieur et adhérence — pages 39–40

Montrer
$$\overline{A\cup B}=\overline A\cup\overline B,\qquad
\overline{A\cap B}\subset\overline A\cap\overline B,$$
$$(A\cap B)^\circ=A^\circ\cap B^\circ,\qquad
A^\circ\cup B^\circ\subset(A\cup B)^\circ.$$

**1.** La monotonie de l’adhérence donne $\overline A\cup\overline B\subset\overline{A\cup B}$. Inversement $A\cup B\subset\overline A\cup\overline B$, et ce dernier ensemble est fermé, donc contient $\overline{A\cup B}$.

**2.** Des inclusions $A\cap B\subset A$ et $A\cap B\subset B$, on tire $\overline{A\cap B}\subset\overline A$ et $\overline{A\cap B}\subset\overline B$, d’où le résultat.

**3.** La monotonie de l’intérieur donne $(A\cap B)^\circ\subset A^\circ\cap B^\circ$. L’intersection $A^\circ\cap B^\circ$ est un ouvert contenu dans $A\cap B$, donc est incluse dans son intérieur.

> La source mentionne que l’intersection des intérieurs est ouverte, mais abrège l’argument de cette seconde inclusion.

**4.** Laissée en exercice dans le PDF.

## TD3, exercice 5 — Intérieurs et adhérences des ensembles du TD2 — pages 40–43


**Énoncé.** Déterminer l'adhérence et l'intérieur des ensembles de l'exercice 2 du TD2 :
$A = [0, 1[$, $C = [0, +\infty[$, $D = \,]0, 1[\, \cup \{2\}$, $E = \mathbb{N}$, $F = \{x^2 + y^2 < 4\}$, $G = \{x^2 + y^2 \le 2\}$, $H = \{0 < |x - 1| < 1\}$, $I = \{|x| < 1 \text{ et } |y| \le 1\}$.

**Correction.** Méthode, à chaque fois :

- pour l'intérieur, on propose un ouvert $U \subset X$ (alors $U \subset \mathring{X}$), puis on vérifie qu'aucun point de $X \setminus U$ n'est intérieur ;
- pour l'adhérence, on propose un fermé $V \supset X$ (alors $\overline{X} \subset V$), puis on vérifie que tout point de $V \setminus X$ est adhérent à $X$.

**1. $A = [0, 1[$ : $\mathring{A} = \,]0, 1[$ et $\overline{A} = [0, 1]$.**

- $]0, 1[$ est un ouvert contenu dans $A$. Le seul point restant est $0$ : pour tout $r > 0$, $-\frac{r}{2} \in B(0, r)$ n'est pas dans $A$, donc $0$ n'est pas intérieur.
- $[0, 1]$ est un fermé contenant $A$. Le seul point restant est $1$ : pour tout $r \in \,]0, 2]$, $1 - \frac{r}{2} \in B(1, r) \cap A$, donc $1$ est adhérent à $A$.

**2. $C = [0, +\infty[$ : $\mathring{C} = \,]0, +\infty[$ et $\overline{C} = C$.**

- Même raisonnement que pour $A$ en $0$.
- $C$ est fermé (TD2), donc $\overline{C} = C$.

**3. $D = \,]0, 1[\, \cup \{2\}$ : $\mathring{D} = \,]0, 1[$ et $\overline{D} = [0, 1] \cup \{2\}$.**

- $]0, 1[$ est un ouvert contenu dans $D$. Le seul point restant est $2$ : pour tout $r > 0$, $2 + \frac{r}{2} \in B(2, r)$ n'est pas dans $D$.
- *Méthode 1 :* $[0, 1] \cup \{2\}$ est un fermé (réunion de deux fermés) contenant $D$. Les points restants sont $0$ et $1$ : pour tout $r \in \,]0, 2[$, $\frac{r}{2}$ et $1 - \frac{r}{2}$ sont dans $]0, 1[$, donc $B(0, r) \cap D \ne \emptyset$ et $B(1, r) \cap D \ne \emptyset$.
- *Méthode 2 :* l'adhérence d'une réunion finie est la réunion des adhérences : $\overline{D} = \overline{]0, 1[} \cup \overline{\{2\}} = [0, 1] \cup \{2\}$.

> **Erreur corrigée :** l'ancienne correction écrivait $B(1, r) \cup D \ne \emptyset$ ; il s'agit de l'intersection $B(1, r) \cap D$.

**4. $E = \mathbb{N}$ : $\mathring{E} = \emptyset$ et $\overline{E} = \mathbb{N}$.**

- Pour $n \in \mathbb{N}$ et $r > 0$, la boule $]n - r, n + r[$ contient $n + \frac{\min(r, 1)}{2}$, qui n'est pas un entier : elle n'est pas contenue dans $\mathbb{N}$. Aucun point n'est intérieur.
- $\mathbb{N}$ est fermé (TD2), donc $\overline{\mathbb{N}} = \mathbb{N}$.

**5. $F = B_{\|\cdot\|_2}\big((0, 0), 2\big)$ : $\mathring{F} = F$ et $\overline{F} = \overline{B}_{\|\cdot\|_2}\big((0, 0), 2\big)$**, d'après l'exercice 3 (question 2).

> **Erreur corrigée :** l'ancienne correction donnait $\overline{F} = B_{\|\cdot\|_2}(0, 2)$, sans la barre : l'adhérence est la boule **fermée** $\{x^2 + y^2 \le 4\}$.

**6. $G = \overline{B}_{\|\cdot\|_2}\big((0, 0), \sqrt{2}\big)$ : $\overline{G} = G$ et $\mathring{G} = B_{\|\cdot\|_2}\big((0, 0), \sqrt{2}\big)$**, d'après l'exercice 3 (question 1).

**7. $H = \big(]0, 1[\, \cup \,]1, 2[\big) \times \mathbb{R}$ : $\mathring{H} = H$ et $\overline{H} = [0, 2] \times \mathbb{R}$.**

- $H$ est ouvert (TD2), donc $\mathring{H} = H$.
- $V = \{(x, y) : 0 \le x \le 2\}$ est un fermé contenant $H$. Les points restants sont ceux des droites $x = 0$, $x = 1$ et $x = 2$. Pour $(x_0, y_0)$ sur l'une d'elles et $r \in \,]0, 1[$, le point $(x_0 + \frac{r}{2}, y_0)$ (ou $(x_0 - \frac{r}{2}, y_0)$ si $x_0 = 2$) est dans $B_2\big((x_0, y_0), r\big) \cap H$. Donc $\overline{H} = V$.

> **Complément :** l'ancienne correction disait « trivialement vrai » ; le point voisin est explicité ci-dessus.

**8. $I = \,]-1, 1[\, \times [-1, 1]$ : $\overline{I} = [-1, 1]^2$ et $\mathring{I} = \,]-1, 1[^2$.**

- $]-1, 1[^2$ est ouvert (c'est la boule ouverte $B_\infty\big((0,0), 1\big)$) et contenu dans $I$. Les points restants de $I$ sont ceux où $|y| = 1$ : pour $(x_0, \pm 1)$, le point $(x_0, \pm(1 + \frac{r}{2}))$ est dans la boule de rayon $r$ mais pas dans $I$.
- $[-1, 1]^2$ est fermé (c'est la boule fermée $\overline{B}_\infty\big((0,0), 1\big)$) et contient $I$. Les points restants sont ceux où $|x| = 1$ : pour $(\pm 1, y_0)$ et $r \in \,]0, 2[$, le point $(\pm(1 - \frac{r}{2}), y_0)$ est dans la boule de rayon $r$ et dans $I$.

## TD4, exercice 1 — Suite complexe sans valeur d’adhérence — page 44

Donner une suite $z_n=x_n+iy_n$ sans valeur d’adhérence dans $\mathbb C$, alors que $x_n$ et $y_n$ en ont dans $\mathbb R$.

La construction source est
$$x_{2n}=0,\quad x_{2n+1}=f(n),\qquad y_{2n}=g(n),\quad y_{2n+1}=0,$$
d’où $z_{2n}=ig(n)$ et $z_{2n+1}=f(n)$. Les suites réelles ont zéro comme valeur d’adhérence. Si $f(n),g(n)\to+\infty$, alors $|z_n|\to+\infty$ : aucune sous-suite complexe ne converge.

> Correction : la source demande seulement que $f,g$ soient strictement croissantes, ce qui ne garantit pas leur divergence. On peut prendre $f(n)=g(n)=n+1$. Elle écrit aussi $x_{2n+1}=0$ à la place de $y_{2n+1}=0$ dans la seconde définition.

Rappel : $\ell$ est valeur d’adhérence si une extraction $\varphi:\mathbb N\to\mathbb N$ strictement croissante vérifie $x_{\varphi(n)}\to\ell$.

## TD4, exercice 2 — Différence de deux suites tendant vers zéro — pages 44–45


**Énoncé.** Soient $(u_n)$ et $(v_n)$ deux suites réelles telles que $u_n - v_n$ converge vers $0$. Montrer que si $(u_n)$ et $(v_n)$ admettent des valeurs d'adhérence, alors les valeurs d'adhérence de $(u_n)$ et $(v_n)$ sont les mêmes.

**Correction.** Posons $z_n = u_n - v_n$, qui tend vers $0$.

Soit $\ell$ une valeur d'adhérence de $(u_n)$ : il existe $\varphi$ strictement croissante telle que $u_{\varphi(n)} \to \ell$. La suite extraite $z_{\varphi(n)}$ d'une suite qui converge vers $0$ converge aussi vers $0$. Donc
$$v_{\varphi(n)} = u_{\varphi(n)} - z_{\varphi(n)} \longrightarrow \ell - 0 = \ell$$
et $\ell$ est une valeur d'adhérence de $(v_n)$.

En échangeant les rôles de $u$ et $v$ (car $v_n - u_n = -z_n \to 0$ aussi), toute valeur d'adhérence de $(v_n)$ est une valeur d'adhérence de $(u_n)$. Les deux suites ont donc les mêmes valeurs d'adhérence.

> **Erreur corrigée :** l'ancienne correction écrivait $0 = \ell - \lim v_{\varphi(n)}$, ce qui suppose que $\lim v_{\varphi(n)}$ existe, alors que c'est justement ce qu'il faut démontrer. On l'obtient en écrivant $v_{\varphi(n)}$ comme différence de deux suites convergentes.

## TD4, exercice 3 — Exemples de valeurs d’adhérence — pages 45–46

Donner des suites avec aucune, une, deux, trois valeurs d’adhérence, puis une seule sans convergence.

Réponses de la source :

1. $u_n=(2n,1/n)$ pour $n\ge1$ : aucune valeur d’adhérence, car non bornée le long de toute extraction.
2. $u_{2n}=0$, $u_{2n+1}=n$ : zéro est la seule valeur d’adhérence.
3. $u_n=(-1)^n$ : valeurs d’adhérence $1,-1$.
4. $u_{2n}=(-1)^n$, $u_{2n+1}=3$ : valeurs d’adhérence $1,-1,3$.
5. La suite du point 2 ne converge pas, malgré son unique valeur d’adhérence.

> La source annonce $\mathbb R^2$ au point 2 alors que la suite donnée est réelle.

## TD4, exercice 4 — Topologie par les suites — pages 46–49

> Le PDF laisse la question sur N en exercice, traite seulement la fermeture de H et ne donne pas la correction de J. Les justifications supplémentaires du texte ci-dessous proviennent du TD 2025–2026 ; elles complètent explicitement ces lacunes.


**Énoncé.** Déterminer si les ensembles suivants sont des ouverts, des fermés, les deux ou aucun des deux. Déterminer également leur adhérence.

1. $A = [0, 1[$
2. $C = [0, +\infty[$
3. $D = \,]0, 1[\, \cup \{2\}$
4. $E = \mathbb{N}$
5. $H = \{(x, y) \in \mathbb{R}^2 \,/\, 0 < |x - 1| < 1\}$ (seulement : fermé ?)
6. $I = \{(x, y) \in \mathbb{R}^2 \,/\, |x| < 1 \text{ et } |y| \le 1\}$

**Correction.** Outils (caractérisation séquentielle) :

- $X$ est **fermé** si et seulement si la limite de toute suite convergente d'éléments de $X$ est dans $X$ ;
- $X$ est **ouvert** si et seulement si son complémentaire est fermé ;
- $\overline{X}$ est l'ensemble des limites des suites convergentes d'éléments de $X$.

**1. $A = [0, 1[$ : ni ouvert, ni fermé, $\overline{A} = [0, 1]$.**

- *Pas fermé* : $x_n = 1 - \frac{1}{n} \in A$ pour $n \ge 1$, mais $x_n \to 1 \notin A$.
- *Pas ouvert* : $y_n = -\frac{1}{n} \in \complement_{\mathbb{R}} A$, mais $y_n \to 0 \notin \complement_{\mathbb{R}} A$ : le complémentaire n'est pas fermé.
- *Adhérence* : si $x_n \in A$ converge vers $x$, le passage à la limite dans $0 \le x_n < 1$ donne $0 \le x \le 1$, donc $\overline{A} \subset [0, 1]$. Réciproquement $A \subset \overline{A}$, et $1 = \lim (1 - \frac{1}{n})$ est adhérent. Donc $\overline{A} = [0, 1]$.

**2. $C = [0, +\infty[$ : fermé, pas ouvert, $\overline{C} = C$.**

- *Fermé* : si $x_n \ge 0$ et $x_n \to x$, alors $x \ge 0$ (passage à la limite).
- *Pas ouvert* : $y_n = -\frac{1}{n} \in \complement_{\mathbb{R}} C$ tend vers $0 \notin \complement_{\mathbb{R}} C$.
- *Adhérence* : $C$ est fermé, donc $\overline{C} = C$.

**3. $D = \,]0, 1[\, \cup \{2\}$ : ni ouvert, ni fermé, $\overline{D} = [0, 1] \cup \{2\}$.**

- *Pas fermé* : $x_n = \frac{1}{n} \in D$ pour $n \ge 2$, mais $x_n \to 0 \notin D$.
- *Pas ouvert* : $\complement_{\mathbb{R}} D = \,]-\infty, 0] \cup [1, 2[\, \cup \,]2, +\infty[$ contient $y_n = 2 - \frac{1}{n}$ pour $n \ge 1$, qui tend vers $2 \notin \complement_{\mathbb{R}} D$.
- *Adhérence* : soit $(x_n)$ une suite de $D$ qui converge vers $x$. Si une infinité de termes valent $2$, la suite extraite correspondante montre que $x = 2$. Sinon, à partir d'un certain rang $x_n \in \,]0, 1[$, et le passage à la limite donne $x \in [0, 1]$. Donc $\overline{D} \subset [0, 1] \cup \{2\}$. Réciproquement, $0 = \lim \frac{1}{n}$ et $1 = \lim (1 - \frac{1}{n})$ (pour $n \ge 2$, ces suites sont dans $D$) sont adhérents.

> **Erreur corrigée :** l'ancienne correction utilisait $x_n = 1 - \frac{1}{n}$ et $x_n = \frac{1}{n}$ « pour tout $n \in \mathbb{N}$ » ; il faut $n \ge 2$ pour que ces termes soient dans $]0, 1[$.

**4. $E = \mathbb{N}$ : fermé, pas ouvert, $\overline{\mathbb{N}} = \mathbb{N}$.**

- *Fermé* : soit $(x_n)$ une suite d'entiers naturels qui converge vers $x$. À partir d'un certain rang, $|x_n - x| < \frac{1}{2}$, donc $|x_n - x_m| < 1$ ; deux entiers à distance $< 1$ sont égaux : la suite est constante à partir de ce rang, et sa limite $x$ est un entier naturel.
- *Pas ouvert* : $y_n = -\frac{1}{n} \in \complement_{\mathbb{R}} \mathbb{N}$ tend vers $0 \in \mathbb{N}$.
- *Adhérence* : $\mathbb{N}$ est fermé, donc $\overline{\mathbb{N}} = \mathbb{N}$.

> **Complément :** ce cas était « laissé en exercice » dans l'ancienne correction.

**5. $H$ n'est pas fermé** : $x_n = \big(\frac{1}{n}, 0\big) \in H$ pour $n \ge 2$ (car $|\frac{1}{n} - 1| \in \,]0, 1[$), mais $x_n \to (0, 0) \notin H$ (car $|0 - 1| = 1$).

> **Erreur corrigée :** l'ancienne correction prenait $n \in \mathbb{N}^*$ ; pour $n = 1$, $x_1 = (1, 0) \notin H$.

**6. $I = \,]-1, 1[\, \times [-1, 1]$ : ni ouvert, ni fermé, $\overline{I} = [-1, 1]^2$.**

- *Pas fermé* : $u_n = \big(1 - \frac{1}{n}, 0\big) \in I$, mais $u_n \to (1, 0) \notin I$.
- *Pas ouvert* : $u_n = \big(0, 1 + \frac{1}{n}\big) \in \complement_{\mathbb{R}^2} I$ (car $|1 + \frac{1}{n}| > 1$), mais $u_n \to (0, 1) \in I$ : le complémentaire n'est pas fermé.
- *Adhérence* : si $(x_n, y_n) \in I$ converge vers $(x, y)$, le passage à la limite dans $-1 < x_n < 1$ et $-1 \le y_n \le 1$ donne $(x, y) \in [-1, 1]^2$. Réciproquement, les points de $[-1, 1]^2 \setminus I$ sont ceux où $x = \pm 1$ ; pour $y \in [-1, 1]$, la suite $\big(\pm(1 - \frac{1}{n}), y\big)$ est dans $I$ et tend vers $(\pm 1, y)$. Donc $\overline{I} = [-1, 1]^2$.

> **Erreurs corrigées :** l'ancienne correction prenait $u_n = (0, 1 - \frac{1}{n})$ « dans le complémentaire de $I$ » : ces points sont **dans** $I$ ; il faut $(0, 1 + \frac{1}{n})$. Elle écrivait aussi que $(-1 + \frac{1}{n}, y)$ tend vers $(1, 0)$ : la limite est $(-1, y)$.

## TD5, exercice 1 — Majoration et limite — pages 50–51


**Énoncé.**

1. Montrer que si $x$ et $y$ sont des réels, alors $2|xy| \le x^2 + y^2$.
2. Soit $f$ l'application de $A = \mathbb{R}^2 \setminus \{(0,0)\}$ dans $\mathbb{R}$ définie par $f(x, y) = \dfrac{3x^2 + xy}{\sqrt{x^2 + y^2}}$.
    a) Montrer que pour tout $(x, y) \in A$, $|f(x, y)| \le \frac{7}{2}\|(x, y)\|_2$, avec $\|(x, y)\|_2 = \sqrt{x^2 + y^2}$.
    b) En déduire que $f$ admet une limite en $(0, 0)$.

**Correction.**

**1.** $0 \le (|x| - |y|)^2 = x^2 + y^2 - 2|xy|$, donc $2|xy| \le x^2 + y^2$.

**2. a)** Notons $\|\cdot\| = \|(x,y)\|_2$. Par l'inégalité triangulaire,
$$|f(x, y)| \le \frac{3x^2}{\|(x,y)\|} + \frac{|xy|}{\|(x,y)\|}$$
Or $x^2 \le x^2 + y^2 = \|(x,y)\|^2$, et d'après la question 1, $|xy| \le \frac{1}{2}\|(x,y)\|^2$. Donc
$$|f(x, y)| \le \frac{3\|(x,y)\|^2}{\|(x,y)\|} + \frac{\|(x,y)\|^2}{2\|(x,y)\|} = \frac{7}{2}\|(x,y)\|$$

**2. b)** Quand $(x, y) \to (0, 0)$, $\|(x,y)\| \to 0$, donc $|f(x, y) - 0| \le \frac{7}{2}\|(x,y)\| \to 0$ : $\lim_{(0,0)} f = 0$.

> **Erreurs corrigées :** l'ancienne correction annonçait « montrons que $|f| \le 4\|(x,y)\|_2$ » (l'énoncé et le calcul donnent $\frac{7}{2}$), écrivait $|f| = \dots$ au lieu de $|f| \le \dots$, et confondait $\|(x,y)\|_2$ et $\|(x,y)\|_2^2$ dans « $x^2 \le \|(x,y)\|_2$ » et « $\sqrt{x^2 + y^2} = \|(x,y)\|_2^2$ ».

## TD5, exercice 2 — Treize limites — pages 51–59


**Énoncé.** Étudier les limites en $(0, 0)$ des fonctions suivantes :

1. $f(x, y) = (x + y)\sin\Big(\dfrac{1}{x^2 + y^2}\Big)$
2. $f(x, y) = \dfrac{1}{x - y}$
3. $f(x, y) = \dfrac{x^2 - y^2}{x^2 + y^2}$
4. $f(x, y) = \dfrac{x^2 + xy + y^2}{x^2 + y^2}$
5. $f(x, y) = \dfrac{x^2 y}{x^2 + y^2}$
6. $f(x, y) = \dfrac{x^2 y^2}{x^2 + y^2}$
7. $f(x, y) = \dfrac{x^3}{y}$
8. $f(x, y) = \dfrac{x + 3y}{x^2 - y^2}$
9. $f(x, y) = \dfrac{x^2 + y^2}{|x| + |y|}$
10. $f(x, y) = \dfrac{xy}{\sqrt{x^2 + y^2}}$
11. $f(x, y) = \dfrac{\sin(xy)}{\sqrt{x^2 + y^2}}$
12. $f(x, y) = x^y$
13. $f(x, y) = \Big(\dfrac{x^2 + y^2 - 1}{x}\sin(x),\ \dfrac{\sin(x^2) + \sin(y^2)}{\sqrt{x^2 + y^2}}\Big)$

**Correction.** Deux stratégies :

- **pour montrer qu'il n'y a pas de limite**, on trouve deux chemins (ou deux suites) qui tendent vers $(0,0)$ et donnent deux limites différentes ;
- **pour montrer qu'une limite $\ell$ existe**, on majore $|f(x,y) - \ell|$ par une quantité qui tend vers $0$ (souvent avec $2|xy| \le x^2 + y^2$), ou on passe en coordonnées polaires $x = \rho\cos\theta$, $y = \rho\sin\theta$ en majorant **indépendamment de $\theta$**.

**1. Limite $0$.** $|\sin| \le 1$ donc $|f(x, y)| \le |x + y| \le |x| + |y| \to 0$.

**2. Pas de limite** (domaine $x \ne y$). Sur l'axe $(x, 0)$ avec $x \to 0^+$ : $f(x, 0) = \frac{1}{x} \to +\infty$. Sur l'axe $(0, y)$ avec $y \to 0^+$ : $f(0, y) = -\frac{1}{y} \to -\infty$. Avec des suites : $f(\frac{1}{n}, 0) = n$ et $f(0, \frac{1}{n}) = -n$. En polaires : $f = \frac{1}{\rho(\cos\theta - \sin\theta)}$, dont le signe dépend de $\theta$.

**3. Pas de limite.** $f(x, 0) = 1$ et $f(0, y) = -1$. En polaires : $f = \cos^2\theta - \sin^2\theta = \cos(2\theta)$, qui dépend de $\theta$.

**4. Pas de limite.** $f(x, 0) = 1$ et $f(x, x) = \frac{3x^2}{2x^2} = \frac{3}{2}$. En polaires : $f = 1 + \cos\theta\sin\theta$.

**5. Limite $0$.** Sur les axes et sur $y = x$, $f$ tend vers $0$ : c'est le candidat. Avec $|xy| \le \frac{1}{2}(x^2 + y^2)$ :
$$|f(x, y)| = \frac{|xy| \cdot |x|}{x^2 + y^2} \le \frac{|x|}{2} \to 0$$
En polaires : $f = \rho\cos^2\theta\sin\theta$, et $|f| \le \rho \to 0$ quel que soit $\theta$.

**6. Limite $0$.** Même méthode : $|f(x, y)| = \dfrac{|xy| \cdot |xy|}{x^2 + y^2} \le \dfrac{|xy|}{2} \to 0$.

**7. Pas de limite** (domaine $y \ne 0$). $f(x, x^3) = 1$ pour $x \ne 0$, alors que $f(x, x) = x^2 \to 0$. Avec des suites : $u_n = (\frac{1}{n}, \frac{1}{n^3})$ donne $f(u_n) = 1$, et $v_n = (\frac{1}{n}, \frac{1}{n})$ donne $f(v_n) = \frac{1}{n^2} \to 0$.

**8. Pas de limite** (domaine $x \ne \pm y$). $f(x, 0) = \frac{1}{x}$ tend vers $+\infty$ quand $x \to 0^+$ et vers $-\infty$ quand $x \to 0^-$.

**9. Limite $0$.** Comme $(|x| + |y|)^2 = x^2 + y^2 + 2|xy| \ge x^2 + y^2$ :
$$|f(x, y)| = \frac{x^2 + y^2}{|x| + |y|} \le \frac{(|x| + |y|)^2}{|x| + |y|} = |x| + |y| \to 0$$
En polaires : $f = \dfrac{\rho}{|\cos\theta| + |\sin\theta|}$ et $|\cos\theta| + |\sin\theta| \ge 1$, donc $|f| \le \rho$.

**10. Limite $0$.** $|f(x, y)| = \dfrac{|xy|}{\sqrt{x^2 + y^2}} \le \dfrac{x^2 + y^2}{2\sqrt{x^2 + y^2}} = \dfrac{1}{2}\sqrt{x^2 + y^2} \to 0$.

**11. Limite $0$.** Comme $|\sin u| \le |u|$ : $|f(x, y)| \le \dfrac{|xy|}{\sqrt{x^2 + y^2}} \le \dfrac{1}{2}\sqrt{x^2 + y^2} \to 0$.

**12. Pas de limite** (domaine $x > 0$). $f(x, y) = e^{y\ln x}$. Avec $u_n = (\frac{1}{n}, 0)$ : $f(u_n) = 1$. Avec $v_n = \big(\frac{1}{n}, \frac{1}{\ln n}\big)$ (qui tend bien vers $(0,0)$) : $f(v_n) = e^{-\ln n / \ln n} = \frac{1}{e}$.

**13. Limite $(-1, 0)$** (domaine $x \ne 0$). Une fonction à valeurs dans $\mathbb{R}^2$ a une limite si et seulement si chacune de ses composantes en a une.

- Première composante : $\frac{\sin x}{x} \to 1$ et $x^2 + y^2 - 1 \to -1$, donc elle tend vers $-1$.
- Deuxième composante : $|\sin(x^2) + \sin(y^2)| \le x^2 + y^2$, donc elle est majorée en valeur absolue par $\frac{x^2 + y^2}{\sqrt{x^2 + y^2}} = \sqrt{x^2 + y^2} \to 0$.

> **Compléments :** l'ancienne correction laissait les cas 6 et 13 sans corrigé, et le cas 7 renvoyait les suites « en exercice » ; ils ont été rédigés. Pour le cas 8, elle proposait les chemins $(0, -x)$ et $(0, x)$, qui ne suffisent pas ; l'axe $(x, 0)$ conclut directement. La remarque en polaires du cas 7 (« il est très difficile de conclure ») a été retirée.

## TD5, exercice 3 — Raccord sur un cercle — pages 59–60


**Énoncé.** Soit $f$ la fonction définie sur $\mathbb{R}^2$ par
$$f(x, y) = \begin{cases} \frac{1}{2}x^2 + y^2 - 1 & \text{pour } x^2 + y^2 > 1 \\ -\frac{1}{2}x^2 & \text{pour } x^2 + y^2 \le 1 \end{cases}$$
Montrer que $f$ est continue.

**Correction.** Notons $P(x, y) = \frac{1}{2}x^2 + y^2 - 1$ et $Q(x, y) = -\frac{1}{2}x^2$ : ce sont des polynômes, donc des fonctions continues sur $\mathbb{R}^2$.

- **Hors du cercle** ($x^2 + y^2 \ne 1$) : l'ouvert $\{x^2 + y^2 > 1\}$ (resp. $\{x^2 + y^2 < 1\}$) contient une boule autour du point, sur laquelle $f = P$ (resp. $f = Q$) ; $f$ y est donc continue.
- **Sur le cercle** ($x_0^2 + y_0^2 = 1$) : $f(x_0, y_0) = Q(x_0, y_0) = -\frac{1}{2}x_0^2$, et comme $y_0^2 = 1 - x_0^2$,
$$P(x_0, y_0) = \frac{1}{2}x_0^2 + (1 - x_0^2) - 1 = -\frac{1}{2}x_0^2 = Q(x_0, y_0)$$
Quand $(x, y) \to (x_0, y_0)$, $f(x, y)$ vaut $P(x, y)$ ou $Q(x, y)$, qui tendent tous deux vers la même valeur $-\frac{1}{2}x_0^2$. Donc $f$ est continue en $(x_0, y_0)$.

Finalement $f$ est continue sur $\mathbb{R}^2$.

## TD5, exercice 4, question 1 — Limite par produit — pages 60–61


**Énoncé.** On considère la fonction $f : \mathbb{R} \times \mathbb{R}^* \to \mathbb{R}$, $(x, y) \mapsto (1 + x^2 + y^2)\,\dfrac{\sin(y)}{y}$. Déterminer si $f$ admet une limite en $(0, 0)$.

**Correction.** C'est un produit de deux fonctions qui ont une limite en $(0, 0)$ :
$$\lim_{(x,y) \to (0,0)} (1 + x^2 + y^2) = 1 \qquad \lim_{(x,y) \to (0,0)} \frac{\sin y}{y} = 1$$
(la seconde ne dépend que de $y$, qui tend vers $0$). Donc $\lim_{(0,0)} f = 1 \times 1 = 1$ : $f$ se prolonge par continuité en $(0,0)$ en posant $f(0, 0) = 1$.

> **Note :** c'est la question 1 de l'ancien exercice 4 ; la question 2 n'est plus dans la feuille 2025-2026.

### TD5, exercice 4, question 2 — pages 60–61

Sur $D=\{(x,y):x^2-y^2\ne0\}$, on considère $f_2(x,y)=(1+x+y)/(x^2-y^2)$. Sur l’axe $y=0$, $(1+x)/x^2\to+\infty$ ; sur l’axe $x=0$, $(1+y)/(-y^2)\to-\infty$. La fonction n’a donc pas de limite en $(0,0)$.

> La source parle de continuité en zéro pour les deux fonctions, alors qu’elles n’y sont pas définies. Il s’agit de la possibilité d’un prolongement continu.

## TD5, exercice 5 — Autre raccord — page 61

La fonction
$$f(x,y)=\begin{cases}2x^2+y^2-1,&x^2+y^2>1,\\x^2,&x^2+y^2\le1\end{cases}$$
est-elle continue ? **Réponse source :** « Laissée en exercice (la fonction est continue). »

## TD5, exercice 6 — Droites et parabole — pages 61–62


**Énoncé.** On considère la fonction $f$ définie par
$$f(x, y) = \begin{cases} \dfrac{|y|}{x^2}\, e^{-|y|/x^2} & \text{pour } x \ne 0 \\ 0 & \text{pour } x = 0 \end{cases}$$

1. Soit $\lambda$ un réel et $A_\lambda = \{(x, \lambda x) \,/\, x \in \mathbb{R}\}$. On note $f_\lambda$ la restriction de $f$ à $A_\lambda$. Calculer la limite de $f_\lambda$ en $(0, 0)$.
2. Soit $B = \{(x, x^2) \,/\, x \in \mathbb{R}\}$. On note $g$ la restriction de $f$ à $B$. Calculer la limite de $g$ en $(0, 0)$.
3. Que peut-on dire de la continuité de $f$ en $(0, 0)$ ?

**Correction.**

**1.** Pour $x \ne 0$, $f(x, \lambda x) = \dfrac{|\lambda|}{|x|}\, e^{-|\lambda|/|x|}$ (et $f(0, 0) = 0$).

- Si $\lambda = 0$, $f_\lambda$ est nulle.
- Si $\lambda \ne 0$, posons $t = \frac{|\lambda|}{|x|}$, qui tend vers $+\infty$ quand $x \to 0$. Par croissances comparées, $t\, e^{-t} \to 0$.

Dans tous les cas, $\lim_{(0,0)} f_\lambda = 0$ : le long de **toute droite** passant par l'origine, $f$ tend vers $0 = f(0,0)$. (Sur l'axe $x = 0$, qui n'est pas de la forme $A_\lambda$, $f$ est nulle aussi.)

**2.** Pour $x \ne 0$, $f(x, x^2) = \dfrac{x^2}{x^2}\, e^{-x^2/x^2} = e^{-1}$. Donc $\lim_{(0,0)} g = \frac{1}{e}$.

**3.** Si $f$ avait une limite $\ell$ en $(0,0)$, toutes ses restrictions auraient la même limite $\ell$. Or elle tend vers $0$ le long des droites et vers $\frac{1}{e}$ le long de la parabole $y = x^2$ : $f$ n'a pas de limite en $(0, 0)$, et n'y est donc pas continue.

> **Remarque :** c'est l'exemple classique qui montre qu'étudier toutes les droites passant par un point **ne suffit pas** pour prouver l'existence d'une limite.

## TD5, exercice 7 — Continuité à l’origine — pages 62–63


**Énoncé.** Pour chacune des fonctions, étudier sa continuité en $(0, 0)$ :

1. $f(x, y) = \dfrac{(x + y)^2}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$ ;
2. $f(x, y) = \dfrac{x^3 + y^3}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$ ;
3. $f(x, y) = e^{-\left(\frac{x}{y} + \frac{y}{x}\right)^2}$ si $x \ne 0$ et $y \ne 0$, et $f(x, y) = 0$ si $x = 0$ ou $y = 0$.

**Correction.**

**1. Pas continue.** En polaires, $(x + y)^2 = \rho^2(\cos\theta + \sin\theta)^2 = \rho^2(1 + \sin 2\theta)$, donc
$$f(\rho\cos\theta, \rho\sin\theta) = 1 + \sin(2\theta)$$
qui dépend de $\theta$ : $f$ n'a pas de limite en $(0, 0)$. Par exemple $f(x, 0) = 1$ et $f(x, -x) = 0$.

> **Erreur corrigée :** l'ancienne correction trouvait $\tilde f(\rho, \theta) = \cos^2\theta + \sin^2\theta = 1$, en oubliant le double produit $2xy$ de $(x+y)^2$. Sa conclusion (« pas continue ») restait juste, mais pas pour la bonne raison.

**2. Continue.**
$$|f(x, y)| \le \frac{|x|\,x^2 + |y|\,y^2}{x^2 + y^2} = |x|\frac{x^2}{x^2 + y^2} + |y|\frac{y^2}{x^2 + y^2} \le |x| + |y| \to 0 = f(0, 0)$$

**3. Pas continue.** Pour $x \ne 0$, $f(x, x) = e^{-(1 + 1)^2} = e^{-4}$, qui ne tend pas vers $f(0, 0) = 0$.

## TD6–7, exercice 1 — Prolongements continus — pages 64–65


**Énoncé.** Les fonctions suivantes sont-elles prolongeables par continuité en $(0, 0)$ sur leur domaine de définition $D$ ?

1. $D = \{(x, y) \in \mathbb{R}^2 \,/\, xy > 0\}$, $f(x, y) = \dfrac{1 - \cos(\sqrt{xy})}{y}$
2. $D = \{(x, y) \in \mathbb{R}^2 \,/\, x \ne y\}$, $f(x, y) = \dfrac{\cos(x) - \cos(y)}{x - y}$
3. $D = \{(x, y) \in \mathbb{R}^2 \,/\, x \ne \pm y\}$, $f(x, y) = \dfrac{\sin(x^2) + \sin(y^2)}{x^2 - y^2}$
4. $D = \mathbb{R}^2 \setminus \{(0, 0)\}$, $f(x, y) = \dfrac{xy^2}{x^2 + y^4}$

**Correction.**

**1. Oui, par $0$.** Pour tout réel $u$, $0 \le 1 - \cos u \le \frac{u^2}{2}$. Avec $u = \sqrt{xy}$ :
$$|f(x, y)| \le \frac{xy}{2|y|} = \frac{|x|}{2} \to 0$$
On prolonge en posant $f(0, 0) = 0$.

**2. Oui, par $0$** (et même en tout point $(a, a)$). On utilise $\cos x - \cos y = -2\sin\big(\frac{x+y}{2}\big)\sin\big(\frac{x-y}{2}\big)$ :
$$f(x, y) = -\sin\Big(\frac{x + y}{2}\Big) \cdot \frac{\sin\big(\frac{x-y}{2}\big)}{\frac{x-y}{2}}$$
Quand $(x, y) \to (a, a)$ avec $x \ne y$, le premier facteur tend vers $-\sin(a)$ et le second vers $1$ (car $\frac{\sin u}{u} \to 1$ quand $u \to 0$). Donc $f$ tend vers $-\sin(a)$ ; en $(0,0)$, on prolonge par $f(0, 0) = 0$.

> **Erreur corrigée :** l'ancienne correction écrivait la formule avec $\cos(x) - \sin(x)$ au lieu de $\cos(x) - \cos(y)$.

**3. Non.** $f(x, 0) = \frac{\sin(x^2)}{x^2} \to 1$ et $f(0, y) = \frac{\sin(y^2)}{-y^2} \to -1$.

**4. Non.** Sur la droite $y = x$ : $f(x, x) = \frac{x^3}{x^2 + x^4} = \frac{x}{1 + x^2} \to 0$. Sur la parabole $x = y^2$ : $f(y^2, y) = \frac{y^4}{2y^4} = \frac{1}{2}$. Deux limites différentes.

## TD6–7, exercice 2 — Deux limites — pages 65–66

Étudier en $(0,0)$ : $f_1(x,y)=(x+2y)/(x^2-y^2)$ et $f_2(x,y)=xy/(x-y)$.

**1.** $f_1(x,0)=1/x$, qui tend vers $+\infty$ ou $-\infty$ selon le côté : pas de limite.

**2.** Laissée en exercice dans la source.

## TD6–7, exercice 3 — La norme est lipschitzienne — page 66

Montrer que $x\mapsto\|x\|$ est $1$-lipschitzienne de $(E,\|\cdot\|)$ vers $(\mathbb R,|\cdot|)$. L’inégalité recherchée,
$$\big|\|x\|-\|y\|\big|\le\|x-y\|,$$
est exactement la seconde inégalité triangulaire.

## TD6–7, exercice 4 — Forme linéaire intégrale — page 66

Sur $E=C([0,1],\mathbb R)$ muni de $\|f\|_1=\int_0^1|f(t)|\,dt$, étudier la continuité de $\varphi(f)=\int_0^1tf(t)\,dt$.

Comme $0\le t\le1$,
$$|\varphi(f)|=\left|\int_0^1tf(t)\,dt\right|\le\int_0^1|tf(t)|\,dt\le\|f\|_1.$$
Par linéarité, $|\varphi(f)-\varphi(g)|\le\|f-g\|_1$ : $\varphi$ est $1$-lipschitzienne, donc continue.

> Les barres de valeur absolue autour de l’intégrale sont absentes dans deux égalités du PDF ; elles sont rétablies.

## TD6–7, exercice 5 — Continuité uniforme — pages 67–71

Rappeler la définition et sa négation, puis étudier $x^2$ sur $[a,b]$ ($0\le a<b$) et sur $\mathbb R$, $1/x$ sur $]0,1]$ et $\ln x$ sur $\mathbb R_+^*$.

**Définition et négation, avec quantificateurs corrigés :**
$$\forall\varepsilon>0,\ \exists\eta>0,\ \forall x,y\in A,\quad
\|x-y\|_E<\eta\implies\|f(x)-f(y)\|_F<\varepsilon,$$
$$\exists\varepsilon_0>0,\ \forall\eta>0,\ \exists x,y\in A,\quad
\|x-y\|_E<\eta\quad\text{et}\quad\|f(x)-f(y)\|_F\ge\varepsilon_0.$$

> La source place $\exists\eta$ après $\forall(x,y)$ dans la définition ; sa négation inverse aussi les quantificateurs et utilise à tort une implication. Le rayon doit être indépendant des points.

**Carré sur un segment.** Les figures des pages 67–68 représentent la parabole et sa tangente : à variation verticale fixée, la variation horizontale nécessaire diminue quand la pente augmente. L’approximation locale est $\Delta f\simeq f'(x_0)\Delta x$. La source propose de choisir la pente maximale $2b$. La preuve exacte est
$$|x^2-y^2|=|x-y||x+y|\le2b|x-y|.$$
Pour $\varepsilon>0$, $\eta=\varepsilon/(2b)$ convient. C’est aussi la preuve directe que $f$ est $2b$-lipschitzienne.

La troisième méthode est annoncée par l’auteur comme une intuition : une dérivée bornée conduit à une fonction lipschitzienne. **Précision ajoutée :** sur un intervalle, le théorème des accroissements finis justifie rigoureusement cette implication. L’égalité avec la tangente imprimée dans le PDF est seulement une approximation locale.

**Carré sur $\mathbb R$.** Prendre $x_n=n$ et $y_n=n+1/n$. Alors $|x_n-y_n|\to0$ mais $|x_n^2-y_n^2|=2+1/n^2\to2$ : pas de continuité uniforme.

**Inverse sur $]0,1]$.** Prendre $x_n=1/n$, $y_n=1/(2n)$. Leur distance tend vers zéro, mais $|1/x_n-1/y_n|=n\to+\infty$.

**Logarithme sur $\mathbb R_+^*$.** Avec les mêmes suites, $|\ln x_n-\ln y_n|=\ln2$ : pas de continuité uniforme.

> La dérivée non bornée sert ici à chercher les contre-exemples. Contrairement à la généralisation suggérée page 70, elle ne suffit pas à exclure toute continuité uniforme ; par exemple $\sqrt{x}$ est uniformément continue sur $[0,+\infty[$. La source écrit aussi « convergence uniforme » pour « continuité uniforme ».

## TD6–7, exercice 6 — Projection radiale sur la boule — pages 71–73

Pour un EVN $E$, $f(x)=x/\max(1,\|x\|)$. Dessiner le cas réel, montrer que $f$ est bornée, continue et $2$-lipschitzienne.

Sur $\mathbb R$, le graphe est $y=x$ entre $-1$ et $1$, et les plateaux $-1$ et $1$ à l’extérieur. Si $\|x\|\le1$, $f(x)=x$ ; sinon $f(x)=x/\|x\|$. Donc $\|f(x)\|\le1$. Les deux expressions sont continues dans leurs régions et coïncident à la sphère $\|x\|=1$ : $f$ est continue.

La preuve lipschitzienne distingue trois cas.

- Si $\|x\|,\|y\|\le1$, $\|f(x)-f(y)\|=\|x-y\|$.
- Si $\|x\|\le1<\|y\|$, alors
$$\begin{aligned}\|f(x)-f(y)\|&=\frac{\|x\|y\|-y\|}{\|y\|}\le\|x(\|y\|-1)+(x-y)\|\\
&\le\|x\|(\|y\|-1)+\|x-y\|\le\|y\|-\|x\|+\|x-y\|\le2\|x-y\|.\end{aligned}$$
Le cas inverse est symétrique.
- Si les deux normes dépassent 1,
$$\begin{aligned}\left\|\frac{x}{\|x\|}-\frac{y}{\|y\|}\right\|
&\le\frac{\|(x-y)\|y\|\|+\|y(\|y\|-\|x\|)\|}{\|x\|\|y\|}\\
&=\frac{\|x-y\|+|\|y\|-\|x\||}{\|x\|}\le2\|x-y\|.\end{aligned}$$

> Coquilles source : pour $\|x\|>1$, $\|f(x)\|=1$, et non $\|x\|<1$ (p.72). Au début du dernier cas (p.73), la seconde fraction doit être $y/\|y\|$.

## TD6–7, exercice 7 — Compacité — pages 74–75

Décider si les ensembles suivants sont compacts dans $\mathbb R^2$.

1. $A_1=\{x^2+y^4=1\}$ : fermé comme image réciproque de $\{1\}$ par une fonction continue ; $|x|,|y|\le1$, donc borné et compact.
2. $A_2=\{x^2+y^5=1\}$ : fermé, mais $(x,\sqrt[5]{1-x^2})\in A_2$ pour tout $x$, donc non borné et non compact.
3. $A_3=\{x^2+xy+y^2\le1\}$ : fermé, et la source conclut qu’il est borné puis compact, **mais laisse la preuve de la borne vide**. Complément : $x^2+xy+y^2\ge(x^2+y^2)/2$, donc $x^2+y^2\le2$.
4. $A_4=\{x^2+8xy+y^2\le1\}$ : contient tous les $(x,-x)$, car $-6x^2\le1$. Il n’est pas borné, donc pas compact.
5. $A_5=\{y^2=x(1-2x)\}$ : fermé. La positivité de $y^2$ impose $0\le x\le1/2$ ; la source utilise $y^2\le1/2$, puis $x^2+y^2\le3/4$. Il est borné, donc compact.

## TD6–7, exercice 8 — Point fixe sur un compact — page 76

Soit $K$ compact non vide et $f:K\to K$ telle que $\|f(x)-f(y)\|<\|x-y\|$ si $x\ne y$. Montrer l’unicité d’un éventuel point fixe, l’existence de $c$ minimisant $\|f(x)-x\|$, puis l’existence du point fixe.

Deux points fixes distincts contrediraient immédiatement l’inégalité stricte. L’application est $1$-lipschitzienne, donc continue. Ainsi $\delta(x)=\|f(x)-x\|$ est continue sur le compact et atteint son minimum en $c$. Si $f(c)\ne c$,
$$\delta(f(c))=\|f(f(c))-f(c)\|<\|f(c)-c\|=\delta(c),$$
contradiction. Donc $f(c)=c$, et c’est l’unique point fixe.

## TD8, exercice 1 — Premières dérivées partielles — pages 77–78

Calculer les dérivées des trois fonctions suivantes. La source explique deux méthodes : dériver $t\mapsto f(x+t,y)$ ou $t\mapsto f(x,y+t)$ en zéro par la définition, puis dériver directement en maintenant l’autre variable constante.

| Fonction | $\partial_x f$ | $\partial_y f$ |
| --- | --- | --- |
| $e^x\cos y$ | $e^x\cos y$ | $-e^x\sin y$ |
| $(x^2+y^2)\cos(xy)$ | $2x\cos(xy)-y(x^2+y^2)\sin(xy)$ | $2y\cos(xy)-x(x^2+y^2)\sin(xy)$ |
| $\sqrt{1+x^2y^2}$ | $xy^2/\sqrt{1+x^2y^2}$ | $x^2y/\sqrt{1+x^2y^2}$ |

Par exemple, $[e^{x+t}\cos y-e^x\cos y]/t\to e^x\cos y$, en utilisant $(e^t-1)/t\to1$. Toutes les dérivées existent ; le radical de la troisième fonction ne s’annule jamais.

> Les premières colonnes de dérivées sont étiquetées à tort $\partial_y$ dans plusieurs lignes de la page 78 ; il faut $\partial_x$.

## TD8, exercice 2 — Gaz parfait et van der Waals — pages 78–80

**1.** Pour $PV=nRT$, montrer $(\partial P/\partial V)_T(\partial V/\partial T)_P(\partial T/\partial P)_V=-1$ et $T(\partial P/\partial T)_V(\partial V/\partial T)_P=nR$.

Les dérivées sont $-nRT/V^2$, $nR/P$, $V/(nR)$ et $nR/V$, respectivement. Le premier produit vaut $-nRT/(PV)=-1$ ; le second vaut $nRT\,nR/(PV)=nR$.

**2.** Pour $(P+n^2a/V^2)(V-nb)=nRT$, avec $a,b>0$,
$$T=\frac{(P+n^2a/V^2)(V-nb)}{nR},\qquad
\left(\frac{\partial T}{\partial P}\right)_V=\frac{V-nb}{nR},$$
$$P=\frac{nRT}{V-nb}-\frac{n^2a}{V^2},\qquad
\left(\frac{\partial P}{\partial V}\right)_T=-\frac{nRT}{(V-nb)^2}+\frac{2n^2a}{V^3}.$$

Les indices indiquant la variable maintenue constante sont explicités dans cette transcription.

## TD8, exercice 3 — Vingt-cinq calculs de dérivées — pages 80–82


**Énoncé.** Calculer toutes les dérivées partielles d'ordre 1, sans se préoccuper de leur domaine de définition (à faire partiellement en classe).

> **Note :** la liste des fonctions de la feuille 2025-2026 n'a pas pu être extraite ; c'est celle de l'ancienne feuille, dont cet exercice est repris.

1. $f(x,y) = xy$
2. $f(x,y) = \ln(xy)$
3. $f(x,y) = \dfrac{-3y}{x^2 + y^2 + 1}$
4. $f(x,y) = \dfrac{x^2 - y^2}{x^2 + y^2}$
5. $f(x,y) = \dfrac{\sin(x) - \sin(y)}{x - y}$
6. $f(x,y) = \dfrac{4xy(x^2 - y^2)}{x^2 + y^2}$
7. $f(x,y) = \operatorname{Arctan}\big(\frac{y}{x}\big)$
8. $f(x,y) = \operatorname{Arctan}\Big(\dfrac{x + y}{1 - xy}\Big)$
9. $f(x,y) = (x^2 + y^2)^{1/3}$
10. $f(x,y) = x^y$ (avec $x > 0$)
11. $f(x,y) = \cos(x + y^2)$
12. $f(x,y) = e^{\sin(y/x)}$
13. $f(x,y) = \ln\big(x + \sqrt{x^2 + y^2}\big)$
14. $f(x,y) = \dfrac{x}{\sqrt{x^2 - y}}$
15. $f(x,y,z) = x^2 y z^3 + xy - z$
16. $f(x,y,z) = x\sqrt{yz}$
17. $f(x,y,z) = x^{y/z}$
18. $f(x,y,z,t) = \dfrac{x - y}{z - t}$
19. $f(x,y,z,t) = xy^2 z^3 t^4$
20. $f(x,y) = y^5 - 3xy$
21. $f(x,y) = x^2 + 3xy - 6y^5$
22. $f(x,y) = x\cos(e^{xy})$
23. $f(x,y) = \dfrac{x}{y}$
24. $f(x,y) = x^y$
25. $f(x,y,z) = x\cos(xz) + \ln\big(2 - \sin^2(y + z)\big)$

**Correction.** On dérive par rapport à une variable en considérant les autres comme des constantes.

1. $\partial_x f = y$, $\quad \partial_y f = x$.
2. $\partial_x f = \frac{1}{x}$, $\quad \partial_y f = \frac{1}{y}$.
3. $\partial_x f = \dfrac{6xy}{(x^2 + y^2 + 1)^2}$, $\quad \partial_y f = \dfrac{-3(x^2 + y^2 + 1) + 6y^2}{(x^2 + y^2 + 1)^2} = \dfrac{-3x^2 + 3y^2 - 3}{(x^2 + y^2 + 1)^2}$.
4. $\partial_x f = \dfrac{2x(x^2 + y^2) - 2x(x^2 - y^2)}{(x^2 + y^2)^2} = \dfrac{4xy^2}{(x^2 + y^2)^2}$, $\quad \partial_y f = \dfrac{-4x^2 y}{(x^2 + y^2)^2}$.
5. $\partial_x f = \dfrac{(x - y)\cos(x) - (\sin x - \sin y)}{(x - y)^2}$, $\quad \partial_y f = \dfrac{-(x - y)\cos(y) + (\sin x - \sin y)}{(x - y)^2}$.
6. $\partial_x f = \dfrac{4x^4 y + 16x^2 y^3 - 4y^5}{(x^2 + y^2)^2}$, $\quad \partial_y f = \dfrac{4x^5 - 16x^3 y^2 - 4xy^4}{(x^2 + y^2)^2}$.
7. $\partial_x f = \dfrac{-y/x^2}{1 + (y/x)^2} = -\dfrac{y}{x^2 + y^2}$, $\quad \partial_y f = \dfrac{1/x}{1 + (y/x)^2} = \dfrac{x}{x^2 + y^2}$.
8. Avec $u = \frac{x + y}{1 - xy}$, $\partial_x u = \frac{1 + y^2}{(1 - xy)^2}$, et $(1 - xy)^2 + (x + y)^2 = (1 + x^2)(1 + y^2)$ ; donc $\partial_x f = \dfrac{\partial_x u}{1 + u^2} = \dfrac{1}{1 + x^2}$ et de même $\partial_y f = \dfrac{1}{1 + y^2}$.
9. $\partial_x f = \frac{2}{3}x(x^2 + y^2)^{-2/3}$, $\quad \partial_y f = \frac{2}{3}y(x^2 + y^2)^{-2/3}$.
10. $f = e^{y\ln x}$ : $\partial_x f = \frac{y}{x}e^{y\ln x} = yx^{y-1}$, $\quad \partial_y f = \ln(x)\, x^y$.
11. $\partial_x f = -\sin(x + y^2)$, $\quad \partial_y f = -2y\sin(x + y^2)$.
12. $\partial_x f = -\frac{y}{x^2}\cos\big(\frac{y}{x}\big)e^{\sin(y/x)}$, $\quad \partial_y f = \frac{1}{x}\cos\big(\frac{y}{x}\big)e^{\sin(y/x)}$.
13. $\partial_x f = \dfrac{1 + \frac{x}{\sqrt{x^2 + y^2}}}{x + \sqrt{x^2 + y^2}} = \dfrac{1}{\sqrt{x^2 + y^2}}$, $\quad \partial_y f = \dfrac{y}{\sqrt{x^2 + y^2}\,\big(x + \sqrt{x^2 + y^2}\big)}$.
14. $\partial_x f = \dfrac{(x^2 - y) - x^2}{(x^2 - y)^{3/2}} = -\dfrac{y}{(x^2 - y)^{3/2}}$, $\quad \partial_y f = \dfrac{x}{2(x^2 - y)^{3/2}}$.
15. $\partial_x f = 2xyz^3 + y$, $\quad \partial_y f = x^2 z^3 + x$, $\quad \partial_z f = 3x^2 y z^2 - 1$.
16. $\partial_x f = \sqrt{yz}$, $\quad \partial_y f = \dfrac{x\sqrt{z}}{2\sqrt{y}}$, $\quad \partial_z f = \dfrac{x\sqrt{y}}{2\sqrt{z}}$.
17. $f = e^{\frac{y}{z}\ln x}$ : $\partial_x f = \frac{y}{xz}x^{y/z}$, $\quad \partial_y f = \frac{1}{z}\ln(x)\, x^{y/z}$, $\quad \partial_z f = -\frac{y}{z^2}\ln(x)\, x^{y/z}$.
18. $\partial_x f = \frac{1}{z - t}$, $\quad \partial_y f = -\frac{1}{z - t}$, $\quad \partial_z f = -\frac{x - y}{(z - t)^2}$, $\quad \partial_t f = \frac{x - y}{(z - t)^2}$.
19. $\partial_x f = y^2 z^3 t^4$, $\quad \partial_y f = 2xyz^3 t^4$, $\quad \partial_z f = 3xy^2 z^2 t^4$, $\quad \partial_t f = 4xy^2 z^3 t^3$.
20. $\partial_x f = -3y$, $\quad \partial_y f = 5y^4 - 3x$.
21. $\partial_x f = 2x + 3y$, $\quad \partial_y f = 3x - 30y^4$.
22. $\partial_x f = \cos(e^{xy}) - xye^{xy}\sin(e^{xy})$, $\quad \partial_y f = -x^2 e^{xy}\sin(e^{xy})$.
23. $\partial_x f = \frac{1}{y}$, $\quad \partial_y f = -\frac{x}{y^2}$.
24. Comme 10 : $\partial_x f = yx^{y-1}$, $\quad \partial_y f = \ln(x)\, x^y$.
25. $\partial_x f = \cos(xz) - xz\sin(xz)$, $\quad \partial_y f = \dfrac{-2\sin(y + z)\cos(y + z)}{2 - \sin^2(y + z)}$, $\quad \partial_z f = -x^2\sin(xz) - \dfrac{2\sin(y + z)\cos(y + z)}{2 - \sin^2(y + z)}$.

> **Précision ajoutée :** au n° 8, l'ancienne correction s'arrêtait à $\frac{1 + y^2}{(1 - xy)^2 + (x + y)^2}$ ; l'identité $(1 - xy)^2 + (x + y)^2 = (1 + x^2)(1 + y^2)$ donne la forme simple $\frac{1}{1 + x^2}$.

## TD8, exercice 4 — Fonctions de deux variables séparées — pages 82


**Énoncé.** Soient $f$ et $g$ deux fonctions d'une variable réelle, à valeurs dans $\mathbb{R}$ et dérivables sur $\mathbb{R}$. Pour chacune des fonctions de deux variables $F_i$ suivantes, déterminer les dérivées partielles en fonction de $f'$ et $g'$.

1. $F_1(x, y) = f(x) + g(y)$
2. $F_2(x, y) = f(x)\,g(y)$
3. $F_3(x, y) = \dfrac{f(x)}{g(y)}$

**Correction.** Quand on dérive par rapport à $x$, $g(y)$ est une constante, et inversement.

1. $\partial_x F_1 = f'(x)$ et $\partial_y F_1 = g'(y)$.
2. $\partial_x F_2 = f'(x)\,g(y)$ et $\partial_y F_2 = f(x)\,g'(y)$.
3. Là où $g(y) \ne 0$ : $\partial_x F_3 = \dfrac{f'(x)}{g(y)}$ et $\partial_y F_3 = -\dfrac{f(x)\,g'(y)}{g(y)^2}$.

## TD8, exercice 5 — xy sur la somme des valeurs absolues — pages 83–84


**Énoncé.** Soit $f$ la fonction de $\mathbb{R}^2$ dans $\mathbb{R}$ définie par $f(x, y) = \dfrac{xy}{|x| + |y|}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$.

1. Justifier que $f$ est continue sur $\mathbb{R}^2$.
2. Étudier les dérivées partielles de $f$ en $(0, 0)$.

**Correction.**

**1.** Sur $\mathbb{R}^2 \setminus \{(0,0)\}$, $f$ est un quotient de fonctions continues dont le dénominateur ne s'annule pas : elle y est continue. En $(0,0)$ :
$$|f(x, y) - 0| = |x| \cdot \frac{|y|}{|x| + |y|} \le |x| \to 0$$
car $\frac{|y|}{|x| + |y|} \le 1$. Donc $f$ est continue sur $\mathbb{R}^2$.

**2.** Il faut revenir à la définition : $f(t, 0) = 0$ pour tout $t$, donc
$$\partial_x f(0,0) = \lim_{t \to 0} \frac{f(t, 0) - f(0, 0)}{t} = 0$$
et de même $f(0, t) = 0$ donne $\partial_y f(0,0) = 0$.

> **Erreur corrigée :** l'énoncé de l'ancienne feuille demandait « continue sur $\mathbb{R}$ » ; il s'agit de $\mathbb{R}^2$.

## TD8, exercice 6 — Dérivées d’un minimum — pages 84–85


**Énoncé.** Calculer les dérivées partielles de $f(x, y) = \min(x, y^2)$, avec $x, y \ge 0$.

**Correction.** On découpe le quart de plan en deux régions, séparées par la courbe $x = y^2$ (soit $y = \sqrt{x}$) :

- région I, $x < y^2$ : $f(x, y) = x$, donc $\partial_x f = 1$ et $\partial_y f = 0$ ;
- région II, $x > y^2$ : $f(x, y) = y^2$, donc $\partial_x f = 0$ et $\partial_y f = 2y$.

(Chaque région est un ouvert : au voisinage d'un de ses points, $f$ est donnée par une seule formule.)

*Sur la courbe $x_0 = y_0^2$ avec $x_0 > 0$.* On a $f(x_0, y_0) = x_0 = y_0^2$.

- Par rapport à $x$ : pour $t > 0$, $x_0 + t > y_0^2$, donc $f(x_0 + t, y_0) = y_0^2$ et le taux d'accroissement vaut $0$ ; pour $t < 0$, $f(x_0 + t, y_0) = x_0 + t$ et il vaut $1$. Les limites à droite et à gauche diffèrent : $\partial_x f(x_0, y_0)$ n'existe pas.
- Par rapport à $y$ : pour $t > 0$, $f(x_0, y_0 + t) = x_0$, taux $0$ ; pour $t < 0$ (petit), $f(x_0, y_0 + t) = (y_0 + t)^2$, taux $\to 2y_0 \ne 0$. $\partial_y f(x_0, y_0)$ n'existe pas.

*En $(0, 0)$* (dérivées à droite, puisque $x, y \ge 0$) : $f(t, 0) = \min(t, 0) = 0$ et $f(0, t) = \min(0, t^2) = 0$, donc les deux dérivées partielles valent $0$.

> **Erreur corrigée :** l'ancienne correction définissait les deux régions par la même inégalité $x < y^2$ ; la région II est $x > y^2$.

## TD8, exercice 7, fonctions 1 et 2 — Continuité et dérivées — pages 85–88


**Énoncé.** Étudier la continuité des fonctions suivantes, ainsi que l'existence et la continuité de leurs dérivées partielles premières :

1. $f_1(x, y) = \dfrac{(x + y)^2}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f_1(0, 0) = 0$ ;
2. $f_2(x, y) = (x^2 + y^2)\sin\Big(\dfrac{1}{\sqrt{x^2 + y^2}}\Big)$ si $(x, y) \ne (0, 0)$, et $f_2(0, 0) = 0$.

**Correction.** Hors de $(0, 0)$, ces fonctions sont des quotients et composées de fonctions $C^1$ dont le dénominateur ne s'annule pas : elles y sont $C^1$. Tout se joue en $(0, 0)$.

**1. $f_1$.**

- *Continuité en $(0,0)$* : en polaires, $f_1 = (\cos\theta + \sin\theta)^2 = 1 + \sin(2\theta)$, qui dépend de $\theta$ : pas de limite, $f_1$ n'est **pas continue** en $(0, 0)$.
- *Dérivées partielles hors de $(0,0)$* : en écrivant $f_1 = 1 + \frac{2xy}{x^2 + y^2}$,
$$\partial_x f_1 = \frac{2y(y^2 - x^2)}{(x^2 + y^2)^2} \qquad \partial_y f_1 = \frac{2x(x^2 - y^2)}{(x^2 + y^2)^2}$$
- *En $(0,0)$* : $f_1(t, 0) = 1$ pour $t \ne 0$, donc $\dfrac{f_1(t, 0) - f_1(0,0)}{t} = \dfrac{1}{t}$ n'a pas de limite finie : $\partial_x f_1(0,0)$ **n'existe pas**. De même $f_1(0, t) = 1$, donc $\partial_y f_1(0,0)$ n'existe pas.

Bilan : $f_1$ est $C^1$ sur $\mathbb{R}^2 \setminus \{(0,0)\}$, mais n'est ni continue ni dérivable (partiellement) en $(0,0)$.

> **Erreurs corrigées :** l'ancienne correction concluait que la dérivée partielle « n'est pas continue » en $(0,0)$, alors qu'elle n'y existe pas (la limite vaut $\pm\infty$), puis écrivait « $f_1$ n'est continue sur $\mathbb{R}^2$ » au lieu de « n'est pas continue ».

**2. $f_2$.** Notons $r = \sqrt{x^2 + y^2}$.

- *Continuité* : $|f_2(x, y)| \le r^2 \to 0 = f_2(0,0)$. Donc $f_2$ est continue sur $\mathbb{R}^2$.
- *Dérivées partielles hors de $(0,0)$* : comme $\partial_x r = \frac{x}{r}$,
$$\partial_x f_2 = 2x\sin\Big(\frac{1}{r}\Big) - \frac{x}{r}\cos\Big(\frac{1}{r}\Big) \qquad \partial_y f_2 = 2y\sin\Big(\frac{1}{r}\Big) - \frac{y}{r}\cos\Big(\frac{1}{r}\Big)$$
- *En $(0,0)$* : $\dfrac{f_2(t, 0) - 0}{t} = t\sin\Big(\dfrac{1}{|t|}\Big) \to 0$, donc $\partial_x f_2(0,0) = 0$, et de même $\partial_y f_2(0,0) = 0$.
- *Continuité des dérivées partielles en $(0,0)$* : avec $u_n = (\frac{1}{n}, 0) \to (0,0)$, on a $r = \frac{1}{n}$ et $\partial_x f_2(u_n) = \frac{2}{n}\sin(n) - \cos(n)$, qui n'a pas de limite. Donc $\partial_x f_2$ n'est pas continue en $(0,0)$ ; de même pour $\partial_y f_2$ avec $(0, \frac{1}{n})$.

Bilan : $f_2$ est continue sur $\mathbb{R}^2$, a des dérivées partielles partout, mais n'est pas $C^1$ sur $\mathbb{R}^2$ (elle l'est sur $\mathbb{R}^2 \setminus \{(0,0)\}$).

> **Remarque :** $f_2$ est pourtant **différentiable** en $(0,0)$, de différentielle nulle, car $|f_2(h, k)| \le h^2 + k^2 = o\big(\|(h,k)\|\big)$. C'est l'exemple classique d'une fonction différentiable qui n'est pas $C^1$.

### TD8, exercice 7, fonction 3 — pages 86 et 88–90

$$f_3(x,y)=\begin{cases}\dfrac{x\sin y-y\sin x}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$
Étudier continuité, existence et continuité des dérivées premières.

Hors de l’origine, la fonction est lisse. Avec $\sin t=t-t^3/6+t^3\varepsilon(t)$, $\varepsilon(t)\to0$,
$$f_3(x,y)=\frac{xy}{6(x^2+y^2)}\left[x^2-y^2+6y^2\varepsilon(y)-6x^2\varepsilon(x)\right].$$
Comme $|xy|/(x^2+y^2)\le1/2$, cette expression tend vers zéro. La fonction est donc continue à l’origine.

Hors de l’origine,
$$\partial_x f_3=\frac{\sin y-y\cos x}{x^2+y^2}-\frac{2x(x\sin y-y\sin x)}{(x^2+y^2)^2},$$
$$\partial_y f_3=\frac{x\cos y-\sin x}{x^2+y^2}-\frac{2y(x\sin y-y\sin x)}{(x^2+y^2)^2}.$$
Sur les axes, $f_3(t,0)=f_3(0,t)=0$ ; les deux dérivées en zéro valent donc zéro.

Pour la continuité de $\partial_x f_3$, développer
$$\sin y-y\cos x=y\left[-\frac{y^2}{6}+\frac{x^2}{2}+y^2\varepsilon_1(y)-x^2\varepsilon_2(x)\right].$$
Après division par $x^2+y^2$, la valeur absolue est majorée par $|y|$ fois une quantité bornée et tend vers zéro. Le second terme est également $O(|x|)$ : le numérateur $x\sin y-y\sin x$ est $O(|xy|(x^2+y^2))$. On procède de même pour $\partial_y f_3$. Ainsi $f_3$ est $C^1$ sur $\mathbb R^2$.

> La source résume la majoration du second terme par « en faisant une étude similaire » ; la borne est explicitée ici.

## TD8, exercice 8 — Interprétation de la différentielle — pages 91–92

Une résistance $R$ traversée par un courant $I$ dissipe une puissance $E_J=RI^2$. Relier l’incertitude à la différentielle, d’abord pour $R$ connu et $I$ connu à $\Delta I$ près, puis lorsque $R$ porte aussi une incertitude $\Delta R$.

Le dessin montre la courbe $E_J(I)$, le point $(I,E_J(I))$, sa tangente et l’accroissement $dE_J$ associé à $dI$. On développe
$$E_J(I+dI)=R(I+dI)^2=RI^2+2RIdI+R(dI)^2\simeq E_J(I)+2RIdI.$$
Donc $dE_J=2RI\,dI$. La source écrit $\Delta E_J=2RI\Delta I$ dans cette approximation du premier ordre.

Avec les deux variables,
$$dE_J=\frac{\partial E_J}{\partial R}\,dR+\frac{\partial E_J}{\partial I}\,dI=I^2dR+2RI\,dI.$$
La différentielle décrit la variation linéaire de $E_J$ près du point $(I,R)$ lors des variations $dI,dR$.

> Si les $\Delta$ désignent des bornes d’erreur positives, on utilise les valeurs absolues des coefficients pour une majoration au premier ordre ; une propagation statistique d’incertitudes nécessite des hypothèses supplémentaires, non présentes dans le PDF.

## TD8, exercice 9 — Différentiabilité et paramètre — pages 93–94


**Énoncé.**

1. Soit $a$ un réel non nul. Étudier la différentiabilité au point $(a, 0)$ de la fonction $f$ définie sur $\mathbb{R}^2 \setminus \{(0,0)\}$ par $f(x, y) = \dfrac{x^2 y}{x^2 + |y|}$.
2. Discuter selon la valeur du réel $\alpha$ de la différentiabilité au point $(0,0)$ de $g(x, y) = \dfrac{x^\alpha y}{x^2 + |y|}$ si $(x, y) \ne (0, 0)$, et $g(0, 0) = 0$.

**Correction.** Rappel : $f$ est différentiable en $p$ si ses dérivées partielles existent en $p$ et si
$$\varepsilon(h, k) = \frac{f(p + (h, k)) - f(p) - h\,\partial_x f(p) - k\,\partial_y f(p)}{\|(h, k)\|_2} \xrightarrow[(h,k) \to (0,0)]{} 0$$

**1.** *Dérivées partielles en $(a, 0)$.* $f(x, 0) = 0$ pour tout $x \ne 0$, donc $\partial_x f(a, 0) = 0$. Et
$$\frac{f(a, k) - f(a, 0)}{k} = \frac{a^2}{a^2 + |k|} \xrightarrow[k \to 0]{} 1 \quad (a \ne 0)$$
donc $\partial_y f(a, 0) = 1$.

*Reste.* Comme $f(a, 0) = 0$ :
$$f(a + h, k) - k = k\,\frac{(a + h)^2 - (a + h)^2 - |k|}{(a + h)^2 + |k|} = \frac{-k\,|k|}{(a + h)^2 + |k|}$$
donc, puisque $|k| \le \|(h,k)\|_2$,
$$|\varepsilon(h, k)| = \frac{k^2}{\big((a + h)^2 + |k|\big)\|(h, k)\|_2} \le \frac{|k|}{(a + h)^2} \xrightarrow[(h,k) \to (0,0)]{} \frac{0}{a^2} = 0$$
$f$ est différentiable en $(a, 0)$ et $df_{(a,0)}(h, k) = k$.

**2.** Pour que $x^\alpha$ ait un sens pour tout réel $\alpha$, on lit $|x|^\alpha$ (ou on se restreint à $x > 0$), comme dans l'ancienne correction.

- **$\alpha \le 0$ : pas continue, donc pas différentiable.** $g(\frac{1}{n}, \frac{1}{n}) = \dfrac{n^{-\alpha}\cdot\frac{1}{n}}{\frac{1}{n^2} + \frac{1}{n}} = \dfrac{n^{-\alpha}\, n}{n + 1} \sim n^{-\alpha}$, qui tend vers $1$ si $\alpha = 0$ et vers $+\infty$ si $\alpha < 0$, mais pas vers $g(0,0) = 0$.
- **$\alpha > 0$ : continue.** $|g(x, y)| \le \dfrac{|x|^\alpha |y|}{|y|} = |x|^\alpha \to 0$ (pour $y \ne 0$ ; et $g(x, 0) = 0$). De plus $g(h, 0) = g(0, k) = 0$, donc $\partial_x g(0,0) = \partial_y g(0,0) = 0$ : si $g$ est différentiable en $(0,0)$, sa différentielle est nulle, et il faut étudier $\varepsilon(h, k) = \dfrac{g(h, k)}{\sqrt{h^2 + k^2}}$.
    - **$\alpha > 1$ : différentiable.** $|\varepsilon(h, k)| \le \dfrac{|h|^\alpha}{\sqrt{h^2 + k^2}} \le \dfrac{|h|^\alpha}{|h|} = |h|^{\alpha - 1} \to 0$, et $dg_{(0,0)} = 0$. 
    - **$0 < \alpha \le 1$ : pas différentiable.** Sur la diagonale, pour $h > 0$ : $\varepsilon(h, h) = \dfrac{h^{\alpha + 1}}{(h^2 + h)\sqrt{2}\,h} = \dfrac{h^{\alpha - 1}}{\sqrt{2}(1 + h)}$, qui tend vers $\frac{1}{\sqrt{2}}$ si $\alpha = 1$ et vers $+\infty$ si $\alpha < 1$ : pas vers $0$.

> Rectification d’un complément de la transcription 2025–2026 : $\alpha>1$ assure ici la différentiabilité en zéro, mais pas toujours la classe $C^1$. Pour la lecture $|x|^\alpha$, $\partial_y g(x,0)=|x|^{\alpha-2}$ pour $x\ne0$ ; elle ne tend pas vers zéro pour $1<\alpha\le2$. Le domaine et la convention de prolongement doivent en outre être précisés quand $\alpha\le0$.

## TD8, exercice 10 — Continuité, différentiabilité et gradient — pages 94–98


**Énoncé.** Étudier la continuité et la différentiabilité, puis calculer le gradient (lorsqu'il existe), des fonctions suivantes.


1. $f_1(x, y) = x^3 + xy$ sur $\mathbb{R}^2$
2. $f_2(x, y) = e^{-x^2 - y^2}$ sur $\mathbb{R}^2$
3. $f_3(x, y) = \ln(1 - x^2 - y^2)$ sur $U = \{x^2 + y^2 < 1\}$
4. $f_4(x, y) = \sqrt{x^2 + y^2 - 1}$ sur $U = \{x^2 + y^2 \ge 1\}$
5. $f_5(x, y) = \sqrt{(x - a)^2 + (y - b)^2}$ sur $\mathbb{R}^2$
6. $f_6(x, y) = \sqrt{x^2 + (1 - y)^2} + \sqrt{(1 - x)^2 + y^2}$ sur $\mathbb{R}^2$
7. $f_7(x, y) = \dfrac{x^3 - y^3}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, $f_7(0, 0) = 0$
8. $f_8(x, y) = \dfrac{\sin(x) - \sin(y)}{x - y}$ si $x \ne y$, $f_8(x, x) = \cos(x)$

**Correction.** Outil principal : une fonction dont les dérivées partielles existent et sont continues sur un ouvert est $C^1$, donc différentiable, sur cet ouvert.

**1.** Polynôme, donc continu. $\partial_x f_1 = 3x^2 + y$ et $\partial_y f_1 = x$ sont continues : $f_1$ est $C^1$ sur $\mathbb{R}^2$ et $\nabla f_1(x, y) = (3x^2 + y,\ x)$.

**2.** Composée de fonctions continues. $\partial_x f_2 = -2x e^{-x^2 - y^2}$ et $\partial_y f_2 = -2y e^{-x^2 - y^2}$ sont continues : $f_2$ est $C^1$ et $\nabla f_2(x, y) = -2e^{-x^2 - y^2}(x,\ y)$.

**3.** Continue sur $U$ (composée, $1 - x^2 - y^2 > 0$). $\partial_x f_3 = \dfrac{-2x}{1 - x^2 - y^2}$ et $\partial_y f_3 = \dfrac{-2y}{1 - x^2 - y^2}$ sont continues sur $U$ : $f_3$ est $C^1$ sur $U$ et $\nabla f_3 = -\dfrac{2}{1 - x^2 - y^2}(x,\ y)$.

**4.** Continue sur $U$ (composée).

- Sur l'intérieur $\{x^2 + y^2 > 1\}$ : $\partial_x f_4 = \dfrac{x}{f_4}$, $\partial_y f_4 = \dfrac{y}{f_4}$, continues : $f_4$ y est $C^1$ et $\nabla f_4 = \dfrac{1}{\sqrt{x^2 + y^2 - 1}}(x,\ y)$.
- Sur le cercle $a^2 + b^2 = 1$ : $\dfrac{f_4(a + h, b) - f_4(a, b)}{h} = \dfrac{\sqrt{2ah + h^2}}{h}$. Si $a = 0$, cela vaut $\frac{|h|}{h} = \pm 1$ selon le signe de $h$ : pas de dérivée partielle (seulement des dérivées à droite et à gauche différentes). Si $a \ne 0$, le taux se comporte comme $\frac{\sqrt{2|a||h|}}{|h|} \to +\infty$ (du côté où il est défini) : pas de dérivée partielle. Même chose par rapport à $y$ : $f_4$ n'est pas différentiable sur le cercle.

**5.** $f_5(M) = \|\overrightarrow{AM}\|_2$ avec $A = (a, b)$ : continue sur $\mathbb{R}^2$.

- Sur $U = \mathbb{R}^2 \setminus \{A\}$ : $\partial_x f_5 = \dfrac{x - a}{f_5}$, $\partial_y f_5 = \dfrac{y - b}{f_5}$, continues : $f_5$ est $C^1$ sur $U$ et $\nabla f_5 = \dfrac{\overrightarrow{AM}}{\|\overrightarrow{AM}\|_2}$ (vecteur unitaire dirigé de $A$ vers $M$).
- En $A$ : $\dfrac{f_5(a + h, b) - 0}{h} = \dfrac{|h|}{h} = \pm 1$ : pas de dérivée partielle, donc pas différentiable.

**6.** $f_6(M) = \|\overrightarrow{AM}\|_2 + \|\overrightarrow{BM}\|_2$ avec $A = (0, 1)$ et $B = (1, 0)$ : continue.

- Sur $U = \mathbb{R}^2 \setminus \{A, B\}$, $f_6$ est $C^1$ et
$$\partial_x f_6 = \frac{x}{\sqrt{x^2 + (y - 1)^2}} + \frac{x - 1}{\sqrt{(x - 1)^2 + y^2}} \qquad \partial_y f_6 = \frac{y - 1}{\sqrt{x^2 + (y - 1)^2}} + \frac{y}{\sqrt{(x - 1)^2 + y^2}}$$
- En $A = (0, 1)$ : $f_6(0, 1) = \sqrt{2}$ et
$$\frac{f_6(h, 1) - f_6(0, 1)}{h} = \frac{|h|}{h} + \frac{\sqrt{h^2 - 2h + 2} - \sqrt{2}}{h} \xrightarrow[h \to 0^\pm]{} \pm 1 - \frac{1}{\sqrt{2}}$$
Les limites à droite et à gauche diffèrent : pas de dérivée partielle par rapport à $x$, donc pas différentiable en $A$. Même chose en $B$.

**7.** *Continuité* : en polaires, $|f_7| = \rho\,|\cos^3\theta - \sin^3\theta| \le 2\rho \to 0$, donc $f_7$ est continue sur $\mathbb{R}^2$.

- Sur $U = \mathbb{R}^2 \setminus \{(0,0)\}$, $f_7$ est $C^1$ et
$$\partial_x f_7 = \frac{x^4 + 3x^2 y^2 + 2xy^3}{(x^2 + y^2)^2} \qquad \partial_y f_7 = -\frac{y^4 + 3x^2 y^2 + 2x^3 y}{(x^2 + y^2)^2}$$
- En $(0,0)$ : $\frac{f_7(h, 0)}{h} = \frac{h^3}{h^3} = 1$ et $\frac{f_7(0, k)}{k} = -1$, donc $\partial_x f_7(0,0) = 1$ et $\partial_y f_7(0,0) = -1$. Si $f_7$ était différentiable en $(0,0)$, on aurait $df(h, k) = h - k$. Or
$$\varepsilon(h, k) = \frac{f_7(h, k) - h + k}{\sqrt{h^2 + k^2}} = \frac{hk(h - k)}{(h^2 + k^2)^{3/2}}$$
et $\varepsilon(h, -h) = \dfrac{-2h^3}{2\sqrt{2}\,|h|^3} = \mp\dfrac{1}{\sqrt{2}}$, qui ne tend pas vers $0$ : $f_7$ n'est pas différentiable en $(0,0)$ (et ses dérivées partielles n'y sont pas continues).

**8.** Posons $a \in \mathbb{R}$.

- *Continuité* : hors de la diagonale, $f_8$ est un quotient de fonctions continues. En $(a, a)$ : $\sin x - \sin y = 2\cos\big(\frac{x+y}{2}\big)\sin\big(\frac{x-y}{2}\big)$, donc pour $x \ne y$,
$$f_8(x, y) = \cos\Big(\frac{x + y}{2}\Big)\frac{\sin\big(\frac{x - y}{2}\big)}{\frac{x - y}{2}} \xrightarrow[(x,y) \to (a,a)]{} \cos(a)$$
et sur la diagonale $f_8(x, x) = \cos x \to \cos a$. Donc $f_8$ est continue sur $\mathbb{R}^2$.
- Sur $U = \{x \ne y\}$, $f_8$ est $C^1$ avec
$$\partial_x f_8 = \frac{\cos x}{x - y} - \frac{\sin x - \sin y}{(x - y)^2} \qquad \partial_y f_8 = \frac{-\cos y}{x - y} + \frac{\sin x - \sin y}{(x - y)^2}$$
- En $(a, a)$, dérivée partielle par rapport à $x$ :
$$\frac{f_8(a + h, a) - \cos a}{h} = \frac{\sin(a)(\cos h - 1) + \cos(a)(\sin h - h)}{h^2} \xrightarrow[h \to 0]{} -\frac{\sin a}{2}$$
et de même $\partial_y f_8(a, a) = -\frac{\sin a}{2}$.
- *Différentiabilité en $(a, a)$.* Posons $\varphi(t) = \sin(a + t) - \sin a - t\cos a + \frac{t^2}{2}\sin a$. Par Taylor, $\varphi'(t) = \cos(a + t) - \cos a + t\sin a = O(t^2)$. Pour $h \ne k$, par le théorème des accroissements finis appliqué à $\varphi$ entre $h$ et $k$ :
$$f_8(a + h, a + k) - \cos a + \frac{h + k}{2}\sin a = \frac{\varphi(h) - \varphi(k)}{h - k} = \varphi'(\xi) = O\big(\max(h^2, k^2)\big)$$
avec $\xi$ entre $h$ et $k$ ; pour $h = k$, c'est $\cos(a + h) - \cos a + h\sin a = O(h^2)$. Dans les deux cas, le reste est $o\big(\|(h, k)\|\big)$ : $f_8$ est différentiable en $(a, a)$, avec $df_{(a,a)}(h, k) = -\frac{\sin a}{2}(h + k)$.

> **Précision ajoutée :** l'ancienne correction faisait un développement limité de $\sin(a + h) - \sin(a + k)$ puis divisait par $h - k$ : le reste $o(h^2) + o(k^2)$, divisé par $h - k$ (qui peut être beaucoup plus petit), n'est pas contrôlé. Le passage par $\varphi$ et les accroissements finis règle ce point. Elle notait aussi $\partial_x f_8(0,0)$ au lieu de $\partial_x f_8(a,a)$.

## TD9–10, exercice 1 — Composition avec un chemin — pages 99–100

**1.** Pour $f\in C^1(\mathbb R^2)$ et $g(t)=f(2t,1+t^2)$, poser $u_1(t)=2t$, $u_2(t)=1+t^2$. La règle de la chaîne donne
$$g'(t)=2f_x(2t,1+t^2)+2t f_y(2t,1+t^2).$$

**2.** Pour $f(x,y)=xy$, $x(t)=\cos t$ et $y(t)=\sin t$, déterminer $g'(t)$ explicitement puis par composition. **Cette question n’est pas corrigée dans le PDF.**

**3.** Pour $f\in C^1(\mathbb R^n)$ et $g(t)=f(x_1+th_1,\ldots,x_n+th_n)$,
$$g'(t)=\sum_{i=1}^nh_i\partial_i f(x_1+th_1,\ldots,x_n+th_n).$$

> La source numérote par erreur la correction de la question 3 « 2 ».

## TD9–10, exercice 2 — Composition polynomiale — pages 100–101

Soit $f:\mathbb R^2\to\mathbb R$ différentiable et $g(u,v)=f(u^2+v^2,uv)$. Justifier sa différentiabilité et calculer ses dérivées.

Le changement $\varphi(u,v)=(u^2+v^2,uv)$ est polynomial, donc différentiable. Ainsi $g=f\circ\varphi$ est différentiable et
$$g_u=2u f_x(u^2+v^2,uv)+v f_y(u^2+v^2,uv),$$
$$g_v=2v f_x(u^2+v^2,uv)+u f_y(u^2+v^2,uv).$$

> Le PDF parle d’abord de classe $C^1$, puis se corrige : l’hypothèse sur $f$ est seulement la différentiabilité.

## TD9–10, exercice 3 — Coordonnées polaires — pages 101–102

Pour $g(\rho,\theta)=f(\rho\cos\theta,\rho\sin\theta)$, montrer la différentiabilité, exprimer les dérivées de $g$ en fonction de celles de $f$, inverser ces relations et vérifier avec $f(x,y)=x^2+y^2+x$.

Par composition,
$$\binom{g_\rho}{g_\theta}=\begin{pmatrix}\cos\theta&\sin\theta\\-\rho\sin\theta&\rho\cos\theta\end{pmatrix}\binom{f_x}{f_y}.$$
Pour $\rho\ne0$,
$$f_x=\cos\theta\,g_\rho-\frac{\sin\theta}{\rho}g_\theta,\qquad
f_y=\sin\theta\,g_\rho+\frac{\cos\theta}{\rho}g_\theta.$$
Dans l’exemple, $g=\rho^2+\rho\cos\theta$, d’où $g_\rho=2\rho+\cos\theta$ et $g_\theta=-\rho\sin\theta$. En utilisant $f_x=2x+1$, $f_y=2y$, on retrouve ces résultats : les termes en $\rho\sin\theta\cos\theta$ s’annulent dans $g_\theta$.

## TD9–10, exercice 4 — Invariance par translation — page 103

Si $f$ est différentiable et $f(x+t,y+t)=f(x,y)$ pour tout $t$, poser $g(t)=f(x+t,y+t)$. Cette fonction est constante, donc
$$0=g'(t)=f_x(x+t,y+t)+f_y(x+t,y+t).$$
Prendre $t=0$ : $f_x(x,y)+f_y(x,y)=0$.

## TD9–10, exercice 5 — Invariance par dilatation — pages 103–104

Si $f$ est différentiable et $f(xt,yt)=f(x,y)$, poser $g(t)=f(xt,yt)$. Alors
$$0=g'(t)=x f_x(xt,yt)+y f_y(xt,yt).$$
Prendre $t=1$ : $xf_x+yf_y=0$.

> L’énoncé impose cette identité pour tout réel $t$, y compris zéro : il force en fait $f$ à être constante. La dérivation source reste valide.

## TD9–10, exercice 6 — Jacobien nul — pages 104–105


**Énoncé.** On considère l'application $f$ de $\mathbb{R}^2$ dans $\mathbb{R}^2$ définie par
$$f(x, y) = \Big(x\sqrt{1 + y^2} + y\sqrt{1 + x^2}\ ;\ \big(x + \sqrt{1 + x^2}\big)\big(y + \sqrt{1 + y^2}\big)\Big)$$

1. Montrer que $f$ est de classe $C^1$ sur $\mathbb{R}^2$.
2. Calculer le jacobien de $f$ en tout point $(x, y) \in \mathbb{R}^2$. Qu'en déduit-on pour $f$ ?

**Correction.** Notons $w(t) = \sqrt{1 + t^2}$, de sorte que $w'(t) = \frac{t}{w(t)}$, et $f = (f_1, f_2)$ avec
$$f_1(x, y) = x\,w(y) + y\,w(x) \qquad f_2(x, y) = \big(x + w(x)\big)\big(y + w(y)\big) = xy + w(x)w(y) + f_1(x, y)$$

**1.** $w$ est $C^1$ sur $\mathbb{R}$ ($1 + t^2 > 0$ ne s'annule jamais) ; $f_1$ et $f_2$ sont des sommes et produits de fonctions $C^1$ : $f$ est $C^1$ sur $\mathbb{R}^2$.

**2.** On calcule, en simplifiant à chaque fois avec l'expression de $f_2 - f_1 = xy + w(x)w(y)$ :
$$\frac{\partial f_1}{\partial x} = w(y) + \frac{xy}{w(x)} = \frac{f_2 - f_1}{w(x)} \qquad \frac{\partial f_1}{\partial y} = \frac{xy}{w(y)} + w(x) = \frac{f_2 - f_1}{w(y)}$$
$$\frac{\partial f_2}{\partial x} = \Big(1 + \frac{x}{w(x)}\Big)\big(y + w(y)\big) = \frac{f_2}{w(x)} \qquad \frac{\partial f_2}{\partial y} = \frac{f_2}{w(y)}$$
Le jacobien (déterminant de la matrice jacobienne) vaut
$$\det J_f(x, y) = \frac{f_2 - f_1}{w(x)}\cdot\frac{f_2}{w(y)} - \frac{f_2 - f_1}{w(y)}\cdot\frac{f_2}{w(x)} = 0$$
en tout point. Un $C^1$-difféomorphisme a une matrice jacobienne inversible en tout point : $f$ n'est donc **pas** un $C^1$-difféomorphisme (ni même un difféomorphisme local, nulle part).

> **Remarque :** on peut comprendre ce résultat. En posant $x = \operatorname{sh} a$ et $y = \operatorname{sh} b$ (alors $w(x) = \operatorname{ch} a$), on trouve $f_1 = \operatorname{sh} a \operatorname{ch} b + \operatorname{sh} b \operatorname{ch} a = \operatorname{sh}(a + b)$ et $f_2 = e^a e^b = e^{a+b}$. $f$ ne dépend que de $a + b$ : elle écrase le plan sur la courbe $\{(\operatorname{sh} s, e^s)\}$, et n'est pas injective.

## TD9–10, exercice 7 — Rotation — pages 105–106

Pour $g(x,y)=(x\cos\theta-y\sin\theta,x\sin\theta+y\cos\theta)=(u,v)$ et $F=f\circ g$, la source demande l’existence des dérivées de $F$ et leur calcul en $(a,b)$, en supposant seulement les dérivées partielles de $f$ existantes partout.

Le calcul donné est
$$F_x(a,b)=\cos\theta\,f_u(u(a,b),v(a,b))+\sin\theta\,f_v(u(a,b),v(a,b)),$$
$$F_y(a,b)=-\sin\theta\,f_u(u(a,b),v(a,b))+\cos\theta\,f_v(u(a,b),v(a,b)).$$

> **Hypothèse manquante dans la source :** ces conclusions sont garanties si $f$ est différentiable (en particulier $C^1$). L’existence des seules dérivées partielles ne suffit pas à appliquer la règle de la chaîne. La ligne donnant $v(a,b)$ page 106 porte aussi un signe moins erroné : c’est $a\sin\theta+b\cos\theta$.

> Contre-exemple ajouté pour expliciter la réserve : $f(u,v)=uv/(u^2+v^2)$ hors de zéro, prolongée par zéro, possède ses dérivées partielles partout. Pour $\theta=\pi/4$, $F(t,0)=1/2$ si $t\ne0$, tandis que $F(0,0)=0$ ; $F_x(0,0)$ n’existe pas.

## TD9–10, exercice 8 — EDP et changement direct — pages 106–108


**Énoncé.** On cherche toutes les fonctions $f$ de $\mathbb{R}^2$ dans $\mathbb{R}$, $C^1$ sur $\mathbb{R}^2$, telles que
$$(E) : \quad \forall (x, y) \in \mathbb{R}^2,\quad \frac{\partial f}{\partial x}(x, y) + 2x\,\frac{\partial f}{\partial y}(x, y) = 0$$
On considère l'application $\varphi$ qui à $(u, v) \in \mathbb{R}^2$ associe $\varphi(u, v) = (u, v + u^2)$.

1. Montrer que $\varphi$ est bijective de classe $C^1$ sur $\mathbb{R}^2$.
2. Montrer que $\varphi^{-1}$ est de classe $C^1$ sur $\mathbb{R}^2$.
3. Que peut-on en déduire pour $\varphi$ ?
4. On introduit la fonction $g = f \circ \varphi$.
    a) Montrer que $g$ est de classe $C^1$ sur $\mathbb{R}^2$.
    b) Montrer que $f$ est solution de $(E)$ si et seulement si $\dfrac{\partial g}{\partial u}(u, v) = 0$ pour tout $(u, v)$.
5. En déduire que $f(x, y) = h(y - x^2)$, où $h$ est $C^1$ sur $\mathbb{R}$, est solution de $(E)$.

**Correction.**

**1.** Les composantes de $\varphi$ sont des polynômes : $\varphi$ est $C^1$. Pour $(x, y) \in \mathbb{R}^2$ :
$$\varphi(u, v) = (x, y) \iff \begin{cases} u = x \\ v + u^2 = y \end{cases} \iff \begin{cases} u = x \\ v = y - x^2 \end{cases}$$
Chaque $(x, y)$ a exactement un antécédent : $\varphi$ est bijective, et $\varphi^{-1}(x, y) = (x, y - x^2)$.

**2.** Les composantes de $\varphi^{-1}$ sont des polynômes : $\varphi^{-1}$ est $C^1$.

**3.** $\varphi$ est un $C^1$-difféomorphisme de $\mathbb{R}^2$ sur $\mathbb{R}^2$.

**4. a)** $f$ et $\varphi$ sont $C^1$, donc $g = f \circ \varphi$ l'est aussi.

**4. b)** Avec $x = u$ et $y = v + u^2$, la règle de la chaîne donne
$$\frac{\partial g}{\partial u}(u, v) = \frac{\partial f}{\partial x}\big(\varphi(u, v)\big)\cdot 1 + \frac{\partial f}{\partial y}\big(\varphi(u, v)\big)\cdot 2u = \Big(\frac{\partial f}{\partial x} + 2x\,\frac{\partial f}{\partial y}\Big)\big(\varphi(u, v)\big)$$
puisque $x = u$. Ainsi $\partial_u g(u, v)$ est exactement le membre de gauche de $(E)$ évalué au point $\varphi(u, v)$. Comme $\varphi$ est bijective, quand $(u, v)$ parcourt $\mathbb{R}^2$, $\varphi(u, v)$ parcourt tout $\mathbb{R}^2$ : $(E)$ est vraie en tout point si et seulement si $\partial_u g = 0$ en tout point.

**5.** $\partial_u g = 0$ sur $\mathbb{R}^2$ signifie que, pour chaque $v$ fixé, $u \mapsto g(u, v)$ est de dérivée nulle sur l'intervalle $\mathbb{R}$, donc constante : $g(u, v) = h(v)$ avec $h(v) = g(0, v)$, qui est $C^1$. Alors
$$f(x, y) = g\big(\varphi^{-1}(x, y)\big) = g(x, y - x^2) = h(y - x^2)$$
Réciproquement, toute fonction $f(x, y) = h(y - x^2)$ avec $h$ de classe $C^1$ vérifie $(E)$ : $\partial_x f = -2x\,h'(y - x^2)$ et $\partial_y f = h'(y - x^2)$, donc $\partial_x f + 2x\,\partial_y f = 0$. Les solutions de $(E)$ sont exactement ces fonctions.

> **Précision ajoutée :** l'ancienne correction ne montrait que le sens « $f$ solution $\Rightarrow \partial_u g = 0$ » à la question 4.b ; la bijectivité de $\varphi$ donne l'équivalence.

## TD9–10, exercice 9 — Quatre EDP du premier ordre — pages 108–110

L’inconnue est $f\in C^1(U)$, $U=\mathbb R_+^*\times\mathbb R$. Poser $f=g\circ\varphi$ pour les changements proposés.

**1. $xf_x+yf_y=0$, $(u,v)=(x,y/x)$.** L’inverse est $(u,v)\mapsto(u,uv)$, de classe $C^1$. Les dérivées
$$f_x=g_u-\frac{y}{x^2}g_v,\qquad f_y=\frac1x g_v$$
donnent $xf_x+yf_y=u g_u=0$. Donc $g(u,v)=h(v)$ et
$$f(x,y)=h(y/x),\qquad h\in C^1(\mathbb R).$$

**2. $xf_x+yf_y=\sqrt{x^4+y^4}$, $(u,v)=(y/x,x^2+y^2)$.** L’image est $\mathbb R\times\mathbb R_+^*$ ; l’inverse est
$$x=\sqrt{\frac{v}{1+u^2}},\qquad y=u\sqrt{\frac{v}{1+u^2}}.$$
La règle de la chaîne donne
$$f_x=-\frac{y}{x^2}g_u+2xg_v,\qquad f_y=\frac1xg_u+2yg_v.$$
Ainsi $2(x^2+y^2)g_v=\sqrt{x^4+y^4}$, soit
$$g_v=\frac{\sqrt{1+u^4}}{2(1+u^2)},\quad
g=\frac{v\sqrt{1+u^4}}{2(1+u^2)}+h(u).$$
Donc
$$f(x,y)=\frac12\sqrt{x^4+y^4}+h(y/x).$$

**3. $xf_x-yf_y=xy^2$, $(u,v)=(x,xy)$.** L’inverse est $(u,v)\mapsto(u,v/u)$. Ici $f_x=g_u+yg_v$, $f_y=xg_v$, donc $u g_u=v^2/u$, soit $g_u=v^2/u^2$. En intégrant,
$$g=-v^2/u+h(v),\qquad f(x,y)=-xy^2+h(xy).$$

**4. $xf_x+yf_y=af$, avec $a\in\mathbb R$, coordonnées polaires.** Prendre $\rho>0$, $-\pi/2<\theta<\pi/2$. Pour $g(\rho,\theta)=f(\rho\cos\theta,\rho\sin\theta)$,
$$\rho g_\rho=xf_x+yf_y=ag.$$
L’équation en $\rho$ donne $g(\rho,\theta)=\rho^ah(\theta)$, donc
$$f(x,y)=(x^2+y^2)^{a/2}h\big(\arctan(y/x)\big),\quad h\in C^1(]-\pi/2,\pi/2[).$$

## TD9–10, exercice 10 — Vrai ou faux — page 110

Le mot « gradient » désigne ici le vecteur des dérivées partielles, sans supposer a priori la différentiabilité.

| N° | Affirmation | Réponse source |
| --- | --- | --- |
| 1 | Si $f$ est $C^1$, elle est différentiable en tout point. | Vrai |
| 2 | Si $f$ est $C^1$, son gradient existe en tout point. | Vrai |
| 3 | Si $f$ est $C^1$, elle est continue. | Vrai |
| 4 | Si $f$ est différentiable en tout point, elle est $C^1$. | Faux |
| 5 | Si le gradient existe en tout point, $f$ est $C^1$. | Faux |
| 6 | Si $f$ est continue, elle est $C^1$. | Faux |
| 7 | Si $f$ est différentiable en $(x_0,y_0)$, son gradient y existe. | Vrai |
| 8 | Si $f$ est différentiable, elle est continue. | Vrai |
| 9 | Si le gradient existe en $(x_0,y_0)$, $f$ y est différentiable. | Faux |
| 10 | Si $f$ est continue, elle est différentiable. | Faux |
| 11 | Si $f$ est continue, son gradient existe en tout point. | Faux |
| 12 | Si le gradient existe en tout point, $f$ est continue. | Faux |

La phrase introductive utilise $\mathbb R^n$ ; certaines propositions imprimées utilisent $\mathbb R^2$. Les implications ne changent pas en dimension au moins deux.

## TD9–10, exercice 11 — EDP avec second membre constant — pages 111–112

Résoudre $g_x-g_y=a$. Poser $f(u,v)=g((u+v)/2,(v-u)/2)$. Le changement est un difféomorphisme linéaire, d’inverse $u=x-y$, $v=x+y$.

Par composition, $f_u=(g_x-g_y)/2=a/2$. Ainsi $f(u,v)=au/2+h(v)$, puis
$$g(x,y)=\frac a2(x-y)+h(x+y),\qquad h\in C^1(\mathbb R).$$

## TD9–10, exercice 12 — EDP linéaire et radiale — pages 112–116

**1.** $2f_x-f_y=0$, avec $u=x+y$, $v=x+2y$. Le changement est un difféomorphisme linéaire. Pour $f=g\circ\varphi$, $f_x=g_u+g_v$, $f_y=g_u+2g_v$, donc $g_u=0$. Les solutions sont
$$f(x,y)=h(x+2y),\quad h\in C^1(\mathbb R).$$

**2.** Sur $V=\{x>0\}$, $xf_x+yf_y=\sqrt{x^2+y^2}$. Utiliser $\varphi(r,\theta)=(r\cos\theta,r\sin\theta)$ pour $r>0$ et $\theta\in]-\pi/2,\pi/2[$. L’inverse est $r=\sqrt{x^2+y^2}$, $\theta=\arctan(y/x)$ ; les dérivées sont
$$r_x=\cos\theta,\quad r_y=\sin\theta,\quad\theta_x=-\sin\theta/r,\quad\theta_y=\cos\theta/r.$$
Les deux applications sont $C^1$. Avec $g=f\circ\varphi$,
$$f_x=\cos\theta\,g_r-\frac{\sin\theta}{r}g_\theta,\qquad f_y=\sin\theta\,g_r+\frac{\cos\theta}{r}g_\theta.$$
L’EDP devient $r g_r=r$, donc $g_r=1$ et $g(r,\theta)=r+h(\theta)$. Finalement
$$f(x,y)=\sqrt{x^2+y^2}+h(\arctan(y/x)).$$

> Coquilles de notation rectifiées : les domaines $U,V$ sont intervertis dans une phrase page 114 et la dernière dérivée de $\theta$ page 115 est étiquetée $\partial_x$ au lieu de $\partial_y$.

## TD9–10, exercice 13 — Autres EDP — pages 116–118

**Énoncés :**

1. $f_x-3f_y=0$ sur $\mathbb R^2$, $(u,v)=(2x+y,3x+y)$.
2. $f_x+f_y=f$ sur $\mathbb R^2$, $(u,v)=(x,y-x)$.
3. $yf_x-xf_y=f$ sur $\mathbb R\times\mathbb R_+^*$, en coordonnées polaires.
4. $xf_x+yf_y=0$ sur $\mathbb R\times\mathbb R_+^*$, en coordonnées polaires.
5. $xf_x+yf_y=\sqrt{x^2+y^2}$ sur $\mathbb R\times\mathbb R_+^*$, en coordonnées polaires.

**Corrections présentes :**

1. $f_x=2g_u+3g_v$, $f_y=g_u+g_v$. L’équation donne $-g_u=0$, donc $g=h(v)$ et $f(x,y)=h(3x+y)$.
2. $f_x=g_u-g_v$, $f_y=g_v$. Ainsi $g_u=g$, d’où $g(u,v)=C(v)e^u$ et $f(x,y)=C(y-x)e^x$.

Dans ces deux cas, $h,C$ sont $C^1$ sur $\mathbb R$. **Les questions 3 à 5 ne sont pas corrigées dans la source.**

> L’intitulé global dit « sur $\mathbb R^2$ », mais les trois derniers items précisent le demi-plan supérieur. La ligne de composition page 118 recopie à tort $g(2x+y,3x+y)$ ; il faut $g(x,y-x)$.

## TD11–12, exercice 1 — Recherche d’un potentiel — pages 119–121

Chercher une fonction $f$ dont les dérivées partielles sont les fonctions données. Une condition nécessaire pour un potentiel $C^2$ est $\partial_y(f_x)=\partial_x(f_y)$.

**1.** $f_x=xy^2$, $f_y=x^2y$. Les dérivées croisées valent $2xy$. L’intégration en $x$ donne $f(x,y)=x^2y^2/2+K(y)$ ; la seconde condition impose $K'=0$, donc
$$f(x,y)=\frac{x^2y^2}{2}+C.$$

**2.** $f_x=x/\sqrt{x^2+y^2}$, $f_y=y/\sqrt{x^2+y^2}$, hors de l’origine. Les dérivées croisées valent $-xy/(x^2+y^2)^{3/2}$. L’intégration donne
$$f(x,y)=\sqrt{x^2+y^2}+C.$$
La constante est déterminée composante connexe par composante connexe du domaine considéré. **Précision :** l’égalité des dérivées croisées seule ne garantit pas un potentiel global sur un ouvert quelconque ; ici, la formule explicite le vérifie.

**3.** $f_x=x/(x^2+y^2)$, $f_y=-y/(x^2+y^2)$. On trouve respectivement $-2xy/(x^2+y^2)^2$ et $2xy/(x^2+y^2)^2$. Ces expressions ne sont pas identiques sur un ouvert non vide : le potentiel demandé n’existe pas.

## TD11–12, exercice 2 — Dérivées secondes (questions 1 à 4) — pages 121–124


**Énoncé.** Pour toutes les fonctions suivantes, calculer l'expression de toutes les dérivées secondes en précisant les domaines d'existence, et vérifier le théorème de Schwarz (à faire partiellement en classe) :

1. $f(x, y) = x^2 y + x\sqrt{y}$
2. $f(x, y) = \sin(x + y) + \cos(x - y)$
3. $f(x, y) = (x^2 + y^2)^{3/2}$
4. $f(x, y) = \cos^2(5x + 2y)$

**Correction.** Notation : $\dfrac{\partial^2 f}{\partial x \partial y} = \dfrac{\partial}{\partial x}\Big(\dfrac{\partial f}{\partial y}\Big)$. Le théorème de Schwarz dit que si $f$ est $C^2$ sur un ouvert, les deux dérivées croisées y sont égales.

**1.** $f$ est définie pour $y \ge 0$ ; ses dérivées, pour $y > 0$.
$$\frac{\partial f}{\partial x} = 2xy + \sqrt{y} \qquad \frac{\partial f}{\partial y} = x^2 + \frac{x}{2\sqrt{y}}$$
$$\frac{\partial^2 f}{\partial x^2} = 2y \qquad \frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y} = 2x + \frac{1}{2\sqrt{y}} \qquad \frac{\partial^2 f}{\partial y^2} = -\frac{x}{4y^{3/2}}$$
sur $\mathbb{R} \times \mathbb{R}_+^*$ : les dérivées croisées sont bien égales.

**2.** Sur $\mathbb{R}^2$ :
$$\frac{\partial f}{\partial x} = \cos(x + y) - \sin(x - y) \qquad \frac{\partial f}{\partial y} = \cos(x + y) + \sin(x - y)$$
$$\frac{\partial^2 f}{\partial x^2} = \frac{\partial^2 f}{\partial y^2} = -\sin(x + y) - \cos(x - y) \qquad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = -\sin(x + y) + \cos(x - y)$$

**3.** Notons $r = \sqrt{x^2 + y^2}$, de sorte que $f = r^3$ et $\partial_x r = \frac{x}{r}$. Sur $\mathbb{R}^2$ :
$$\frac{\partial f}{\partial x} = 3xr \qquad \frac{\partial f}{\partial y} = 3yr$$
(en $(0,0)$ aussi, car $\frac{f(t, 0)}{t} = \frac{|t|^3}{t} \to 0$). Sur $\mathbb{R}^2 \setminus \{(0,0)\}$ :
$$\frac{\partial^2 f}{\partial x^2} = 3r + \frac{3x^2}{r} \qquad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = \frac{3xy}{r} \qquad \frac{\partial^2 f}{\partial y^2} = 3r + \frac{3y^2}{r}$$
Ces expressions tendent vers $0$ en $(0,0)$ (elles sont majorées par $6r$), et les dérivées secondes en $(0,0)$ valent $0$ (par exemple $\frac{\partial_x f(t, 0)}{t} = 3|t| \to 0$) : $f$ est même $C^2$ sur $\mathbb{R}^2$.

> **Erreur corrigée :** l'ancienne correction avait un facteur $\frac{1}{2}$ en trop : $\frac{3x^2}{2r}$, $\frac{3xy}{2r}$ et $\frac{3y^2}{2r}$. En dérivant $3xr$ par rapport à $y$, on obtient $3x \cdot \frac{y}{r}$, sans $\frac{1}{2}$.

**4.** Sur $\mathbb{R}^2$, avec $2\sin a \cos a = \sin(2a)$ et $\cos^2 a - \sin^2 a = \cos(2a)$ :
$$\frac{\partial f}{\partial x} = -10\sin(5x + 2y)\cos(5x + 2y) = -5\sin(10x + 4y) \qquad \frac{\partial f}{\partial y} = -2\sin(10x + 4y)$$
$$\frac{\partial^2 f}{\partial x^2} = -50\cos(10x + 4y) \qquad \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = -20\cos(10x + 4y) \qquad \frac{\partial^2 f}{\partial y^2} = -8\cos(10x + 4y)$$
(Avec $\cos(10x + 4y) = \cos^2(5x + 2y) - \sin^2(5x + 2y)$.)

> **Erreur corrigée :** l'ancienne correction écrivait $-20\cos(5x + 2y) + 20\sin(5x + 2y)$ pour les dérivées croisées : il manquait les carrés, c'est $-20\cos^2(5x + 2y) + 20\sin^2(5x + 2y)$.

### Questions 5 et 6 — page 124

**5.** $f(x,y)=x^2(x+y)$, sur $\mathbb R^2$ :
$$f_x=3x^2+2xy,\quad f_y=x^2,\quad f_{xx}=6x+2y,\quad f_{xy}=f_{yx}=2x,\quad f_{yy}=0.$$

**6.** $f(x,y)=\cos(xy)$, sur $\mathbb R^2$ :
$$f_x=-y\sin(xy),\quad f_y=-x\sin(xy),$$
$$f_{xx}=-y^2\cos(xy),\quad f_{yy}=-x^2\cos(xy),\quad f_{xy}=f_{yx}=-\sin(xy)-xy\cos(xy).$$
Dans ces deux cas, les dérivées croisées sont égales, conformément au théorème de Schwarz.

## TD11–12, exercice 3 — Dérivées d’ordre trois — pages 125–126

**1.** Pour $f=x^2y^4+2x^4y$, $f_x=2xy^4+8x^3y$, $f_{xx}=2y^4+24x^2y$, puis $f_{xxx}=48xy$.

**2.** Pour $f=e^{xy^2}$, $f_y=2xy e^{xy^2}$, $\partial_x f_y=(2y+2xy^3)e^{xy^2}$, donc
$$\partial_x^2\partial_y f=(4y^3+2xy^5)e^{xy^2}.$$

**3.** Pour $f=x^5+4x^4y^4z^3+yz^2$, $f_x=5x^4+16x^3y^4z^3$, $\partial_y f_x=64x^3y^3z^3$, puis
$$\partial_z\partial_y\partial_x f=192x^3y^3z^2.$$

**4.** Pour $f=e^{xyz}$, $f_y=xz e^{xyz}$, $\partial_z f_y=x(1+xyz)e^{xyz}$, puis
$$\partial_y\partial_z\partial_y f=x^2z(2+xyz)e^{xyz}.$$

**5.** Pour $f=\ln(x+2y^2+3z^2)$, poser $D=x+2y^2+3z^2>0$. Alors $f_z=6z/D$, $\partial_y f_z=-24yz/D^2$ et
$$\partial_x\partial_y\partial_z f=\frac{48yz}{D^3}.$$

## TD11–12, exercice 4 — Vérification de Schwarz — page 126

**1.** Pour $f=x^5y^4-3x^2y^3+2x^2$, les dérivées premières sont $f_x=5x^4y^4-6xy^3+4x$ et $f_y=4x^5y^3-9x^2y^2$ ; les deux dérivées croisées valent $20x^4y^3-18xy^2$.

**2.** Pour $f=\sin^2x\cos y$, les dérivées premières sont $f_x=2\sin x\cos x\cos y$, $f_y=-\sin^2x\sin y$ ; les dérivées croisées valent $-2\sin x\cos x\sin y$.

## TD11–12, exercice 5 — Laplacien — pages 127–128

On calcule $\Delta f=f_{xx}+f_{yy}$.

| Fonction | $f_{xx}$ | $f_{yy}$ | $\Delta f$ |
| --- | --- | --- | --- |
| $x^2-y^2$ | $2$ | $-2$ | $0$ |
| $x^2+y^2$ | $2$ | $2$ | $4$ |
| $\ln\sqrt{x^2+y^2}$ | $(y^2-x^2)/(x^2+y^2)^2$ | $(x^2-y^2)/(x^2+y^2)^2$ | $0$ |
| $x/(x^2+y^2)$ | $(2x^3-6xy^2)/(x^2+y^2)^3$ | $(6xy^2-2x^3)/(x^2+y^2)^3$ | $0$ |

Les deux dernières fonctions sont définies hors de $(0,0)$. Pour la dernière, les dérivées premières sont $f_x=(y^2-x^2)/(x^2+y^2)^2$ et $f_y=-2xy/(x^2+y^2)^2$.

## TD11–12, exercice 6 — Dérivées croisées différentes — pages 128–130

> La conclusion source « pas C¹ » est une coquille : les calculs établissent C¹ et réfutent C².


**Énoncé.** Soit $f(x, y) = \dfrac{xy^3}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$.

1. Montrer que $f$ est $C^1$ sur $\mathbb{R}^2$.
2. Montrer que $\dfrac{\partial^2 f}{\partial x \partial y}$ et $\dfrac{\partial^2 f}{\partial y \partial x}$ sont définies en $(0, 0)$ mais n'ont pas même valeur.
3. Que peut-on en déduire ?

**Correction.**

**1.** *Hors de $(0,0)$*, $f$ est une fraction rationnelle dont le dénominateur ne s'annule pas : elle est $C^1$ (et même $C^\infty$), avec
$$\frac{\partial f}{\partial x} = \frac{y^3(x^2 + y^2) - 2x^2 y^3}{(x^2 + y^2)^2} = \frac{y^5 - x^2 y^3}{(x^2 + y^2)^2} \qquad \frac{\partial f}{\partial y} = \frac{3x^3 y^2 + xy^4}{(x^2 + y^2)^2}$$
*En $(0,0)$* : $f(t, 0) = f(0, t) = 0$, donc $\partial_x f(0,0) = \partial_y f(0,0) = 0$.

*Continuité des dérivées en $(0,0)$* : en polaires, $\partial_x f = \rho\sin^3\theta(\sin^2\theta - \cos^2\theta)$ et $\partial_y f = \rho(3\cos^3\theta\sin^2\theta + \cos\theta\sin^4\theta)$, majorées en valeur absolue par $\rho$ et $4\rho$, qui tendent vers $0$ indépendamment de $\theta$. Les dérivées partielles sont continues sur $\mathbb{R}^2$ : $f$ est $C^1$ sur $\mathbb{R}^2$.

**2.** Par définition, en utilisant $\partial_y f(t, 0) = 0$ et $\partial_x f(0, t) = \frac{t^5}{t^4} = t$ :
$$\frac{\partial^2 f}{\partial x \partial y}(0,0) = \lim_{t \to 0} \frac{\partial_y f(t, 0) - \partial_y f(0, 0)}{t} = 0 \qquad \frac{\partial^2 f}{\partial y \partial x}(0,0) = \lim_{t \to 0} \frac{\partial_x f(0, t) - \partial_x f(0,0)}{t} = 1$$
Les deux dérivées croisées existent mais sont différentes.

**3.** Si $f$ était $C^2$ sur un voisinage de $(0,0)$, le théorème de Schwarz donnerait l'égalité des dérivées croisées. Donc $f$ n'est pas $C^2$ : ses dérivées secondes croisées ne sont pas continues en $(0,0)$. $f$ est exactement de classe $C^1$.

## TD11–12, exercice 7 — Dérivées croisées égales, question 1 — pages 130–132


**Énoncé.** Soit $f(x, y) = \dfrac{y^4}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$.

1. Montrer que $f$ est $C^1$ sur $\mathbb{R}^2$.
2. Montrer que $\dfrac{\partial^2 f}{\partial x \partial y}$ et $\dfrac{\partial^2 f}{\partial y \partial x}$ sont définies en $(0, 0)$ et ont même valeur.
3. Que peut-on en déduire ?

**Correction.**

**1.** *Hors de $(0,0)$* :
$$\frac{\partial f}{\partial x} = -\frac{2xy^4}{(x^2 + y^2)^2} \qquad \frac{\partial f}{\partial y} = \frac{4x^2 y^3 + 2y^5}{(x^2 + y^2)^2}$$
*En $(0,0)$* : $f(t, 0) = 0$ donne $\partial_x f(0,0) = 0$ ; $f(0, t) = t^2$ donne $\frac{t^2}{t} = t \to 0$, donc $\partial_y f(0,0) = 0$.

*Continuité* : en polaires, $\partial_x f = -2\rho\cos\theta\sin^4\theta$ et $\partial_y f = \rho(4\cos^2\theta\sin^3\theta + 2\sin^5\theta)$, majorées par $2\rho$ et $6\rho$ : elles tendent vers $0$. $f$ est $C^1$ sur $\mathbb{R}^2$.

**2.** $\partial_y f(t, 0) = 0$ et $\partial_x f(0, t) = 0$, donc
$$\frac{\partial^2 f}{\partial x \partial y}(0,0) = \lim_{t \to 0}\frac{0 - 0}{t} = 0 = \frac{\partial^2 f}{\partial y \partial x}(0,0)$$

**3.** On **ne peut rien en déduire** sur le caractère $C^2$ : l'égalité des dérivées croisées en un point est une conséquence du théorème de Schwarz, pas une réciproque. Ici d'ailleurs $f$ n'est pas $C^2$ : hors de $(0,0)$,
$$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x} = -\frac{8x^3 y^3}{(x^2 + y^2)^3}$$
qui vaut $-\frac{8x^6}{8x^6} = -1$ sur la diagonale $y = x$ : elle ne tend pas vers $0$ en $(0,0)$ et n'y est pas continue.

> **Erreur corrigée :** l'ancienne correction trouvait $+1$ sur la diagonale ; le signe est $-1$. La conclusion ne change pas.

### Question 2 — page 132

Refaire l’étude pour $f(x,y)=xy^2/(x+y)$ si $x+y\ne0$, et $f(x,y)=0$ sinon. **Cette question est laissée en exercice dans le PDF.** L’intitulé « mêmes questions » doit se comprendre comme une étude, sans supposer a priori les mêmes conclusions de régularité.

## TD11–12, exercice 8 — Classes de régularité — pages 132–139


**Énoncé.** Déterminer la classe exacte des applications suivantes (toutes prolongées par $0$ en $(0,0)$) :

1. $f(x, y) = \dfrac{(x^2 - y^2)^2}{x^2 + y^2}$
2. $f(x, y) = \dfrac{xy^2}{x^2 + (y - x^2)^2}$
3. $f(x, y) = \dfrac{(e^{x^2} - 1)(e^{y^2} - 1)}{x^2 + y^2}$

**Correction.** Chaque fonction est $C^\infty$ sur $\mathbb{R}^2 \setminus \{(0,0)\}$ (dénominateur non nul) ; on étudie $(0,0)$ en testant successivement la continuité, le caractère $C^1$, puis $C^2$.

**1. Classe $C^1$ exactement.** Comme $(x^2 - y^2)^2 = (x^2 + y^2)^2 - 4x^2y^2$,
$$f(x, y) = x^2 + y^2 - 4\,\frac{x^2 y^2}{x^2 + y^2}$$

- *Continue* : $|f| \le x^2 + y^2 \to 0$.
- *$C^1$* : hors de $(0,0)$, $\partial_x f = \dfrac{2x(x^2 - y^2)(x^2 + 3y^2)}{(x^2 + y^2)^2}$ et $\partial_y f = \dfrac{-2y(x^2 - y^2)(3x^2 + y^2)}{(x^2 + y^2)^2}$ ; en $(0,0)$, $f(t, 0) = f(0, t) = t^2$ donne des dérivées nulles. En majorant, $|\partial_x f| \le \frac{2|x|(x^2 + y^2) \cdot 3(x^2 + y^2)}{(x^2 + y^2)^2} = 6|x| \to 0$, et de même pour $\partial_y f$ : elles sont continues.
- *Pas $C^2$* : hors de $(0,0)$, $\dfrac{\partial^2 f}{\partial x \partial y} = -4\,\dfrac{8x^3 y^3}{(x^2 + y^2)^3} = -\dfrac{32x^3 y^3}{(x^2 + y^2)^3}$ (même calcul qu'à l'exercice 4), qui vaut $-4$ sur la diagonale et $0$ sur les axes : pas de limite en $(0,0)$.

**2. Classe $C^0$ exactement.**

- *Continue* : en polaires, le dénominateur vaut $\rho^2(1 + \rho\,a(\rho, \theta))$ avec $a = \rho\cos^4\theta - 2\cos^2\theta\sin\theta$, et $|a| \le \rho + 2$. Pour $\rho \le \frac{1}{4}$, $1 + \rho a \ge 1 - \frac{1}{4}\cdot\frac{9}{4} = \frac{7}{16}$, donc
$$|f| = \frac{\rho\,|\cos\theta\sin^2\theta|}{1 + \rho a} \le \frac{16}{7}\rho \le 3\rho \to 0$$
- *Pas $C^1$* : $f(t, 0) = 0$ et $f(0, t) = 0$, donc $\partial_x f(0,0) = \partial_y f(0,0) = 0$. Mais sur l'axe $x = 0$, pour $y \ne 0$ :
$$\frac{\partial f}{\partial x}(0, y) = \frac{y^2}{0 + y^2} - 0 = 1$$
(le second terme de la dérivée contient le facteur $x$). Donc $\partial_x f(0, y) \to 1 \ne 0 = \partial_x f(0,0)$ : $\partial_x f$ n'est pas continue en $(0,0)$.

**3. Classe $C^1$ exactement.** Posons $\psi(s) = \frac{e^s - 1}{s}$ (et $\psi(0) = 1$), fonction $C^\infty$ qui vaut $1$ en $0$. Alors
$$f(x, y) = \psi(x^2)\,\psi(y^2)\,\frac{x^2 y^2}{x^2 + y^2}$$

- *Continue* : $\frac{x^2 y^2}{x^2 + y^2} \le \frac{x^2 + y^2}{4} \to 0$, et les $\psi$ tendent vers $1$.
- *$C^1$* : les dérivées en $(0,0)$ sont nulles ($f(t, 0) = 0$). Hors de $(0,0)$,
$$\frac{\partial f}{\partial x} = \frac{2xe^{x^2}(e^{y^2} - 1)}{x^2 + y^2} - \frac{2x(e^{x^2} - 1)(e^{y^2} - 1)}{(x^2 + y^2)^2}$$
Près de $(0,0)$, $|e^{s} - 1| \le 2|s|$ ; donc le premier terme est majoré par $4|x|e^{x^2}\frac{y^2}{x^2 + y^2} \le 4|x|e^{x^2}$ et le second par $\frac{8|x|\,x^2 y^2}{(x^2 + y^2)^2} \le 2|x|$. Les deux tendent vers $0$ : $\partial_x f$ est continue, et de même $\partial_y f$.
- *Pas $C^2$* : le facteur $\frac{x^2 y^2}{x^2 + y^2}$ n'est pas $C^2$ (sa dérivée croisée $\frac{8x^3 y^3}{(x^2 + y^2)^3}$ vaut $1$ sur la diagonale et $0$ sur les axes), et $\psi(x^2)\psi(y^2)$ vaut $1$ en $(0,0)$. Concrètement, la dérivée croisée de $f$ tend vers $1$ le long de la diagonale, alors qu'elle vaut $0$ en $(0,0)$ (car $\partial_y f(t, 0) = 0$ pour tout $t$).

## TD11–12, exercice 9 — EDP du second ordre — pages 139–153

On cherche les solutions $f\in C^2(U)$, en utilisant les changements de variables proposés. Les fonctions arbitraires ci-dessous sont de classe $C^2$ sur leur domaine.

### 1. Équation des ondes — pages 139–142

Sur $\mathbb R^2$, résoudre $f_{xx}-f_{yy}=0$ avec $(u,v)=(x+y,x-y)$. L’inverse est $(x,y)=((u+v)/2,(u-v)/2)$, donc le changement est un difféomorphisme $C^2$. Pour $f(x,y)=g(u,v)$ :
$$f_x=g_u+g_v,\quad f_y=g_u-g_v,$$
$$f_{xx}=g_{uu}+2g_{uv}+g_{vv},\quad f_{yy}=g_{uu}-2g_{uv}+g_{vv}.$$
Ainsi $4g_{uv}=0$, $g(u,v)=h(v)+k(u)$ et
$$f(x,y)=h(x-y)+k(x+y).$$

### 2. Équation radiale homogène — pages 142–144

Sur $\mathbb R_+^*\times\mathbb R$, résoudre $x^2f_{xx}+2xyf_{xy}+y^2f_{yy}=0$ avec $(u,v)=(x,y/x)$, d’inverse $(u,uv)$. Les domaines sont $u>0$, $v\in\mathbb R$.
$$f_x=g_u-\frac y{x^2}g_v,\qquad f_y=\frac1xg_v,$$
$$f_{xx}=g_{uu}-\frac{2y}{x^2}g_{uv}+\frac{2y}{x^3}g_v+\frac{y^2}{x^4}g_{vv},$$
$$f_{xy}=\frac1xg_{uv}-\frac1{x^2}g_v-\frac y{x^3}g_{vv},\qquad f_{yy}=\frac1{x^2}g_{vv}.$$
L’EDP devient $u^2g_{uu}=0$, donc $g=u h(v)+k(v)$ et
$$f(x,y)=x h(y/x)+k(y/x).$$

### 3. Produit et quotient — pages 145–147

Sur $(\mathbb R_+^*)^2$, résoudre
$$x^2f_{xx}-y^2f_{yy}-xf_x+yf_y=0$$
avec $(u,v)=(xy,y/x)$ ; l’inverse est $(x,y)=(\sqrt{u/v},\sqrt{uv})$, pour $u,v>0$.
$$f_x=yg_u-\frac y{x^2}g_v,\quad f_y=xg_u+\frac1xg_v,$$
$$f_{xx}=y^2g_{uu}-\frac{2y^2}{x^2}g_{uv}+\frac{2y}{x^3}g_v+\frac{y^2}{x^4}g_{vv},$$
$$f_{yy}=x^2g_{uu}+2g_{uv}+\frac1{x^2}g_{vv}.$$
On obtient $-4y^2g_{uv}+4(y/x)g_v=0$, soit $u g_{uv}=g_v$. Pour $h=g_v$, l’EDO $u\partial_u h=h$ donne $h(u,v)=u c(v)$ ; une intégration en $v$ donne
$$g(u,v)=u C(v)+D(u),\qquad f(x,y)=xy C(y/x)+D(xy).$$

> Le passage de la source par $\ln|h|$ exclut provisoirement $h=0$ ; la formule finale comprend aussi cette solution. Les fonctions arbitraires peuvent prendre des valeurs réelles, sans condition de positivité.

### 4. Variables logarithmiques — pages 148–150

Sur $(\mathbb R_+^*)^2$, résoudre
$$x^2f_{xx}-y^2f_{yy}+xf_x-yf_y=0$$
avec $(u,v)=(\ln x,\ln y)$, d’inverse $(e^u,e^v)$. On a
$$f_x=g_u/x,\quad f_y=g_v/y,\quad f_{xx}=(g_{uu}-g_u)/x^2,\quad f_{yy}=(g_{vv}-g_v)/y^2.$$
L’équation devient $g_{uu}-g_{vv}=0$. Avec $(s,t)=(u+v,u-v)$ et $g=h(s,t)$, on obtient $h_{st}=0$, d’où
$$f(x,y)=K(\ln(x/y))+L(\ln(xy)).$$

### 5. Changement quadratique — pages 150–152

Sur $\mathbb R_+^*\times\mathbb R$, résoudre
$$f_{xx}-4x^2f_{yy}-\frac1x f_x=0$$
avec $(u,v)=(x^2-y,x^2+y)$. Son image est le demi-plan $u+v>0$, et l’inverse est
$$x=\sqrt{(u+v)/2},\qquad y=(v-u)/2.$$

> Rectification du domaine : la source annonce un difféomorphisme sur $\mathbb R^2$, alors que l’image est $\{u+v>0\}$. Elle utilise ensuite correctement $u+v>0$ dans les calculs.

Pour $f=g\circ\varphi$ :
$$f_x=2x(g_u+g_v),\quad f_y=-g_u+g_v,$$
$$f_{xx}=2(g_u+g_v)+4x^2(g_{uu}+2g_{uv}+g_{vv}),\quad f_{yy}=g_{uu}-2g_{uv}+g_{vv}.$$
L’équation donne $16x^2g_{uv}=0$. Les sections horizontales et verticales du demi-plan étant des intervalles, on obtient $g=K(u)+L(v)$, puis
$$f(x,y)=K(x^2-y)+L(x^2+y).$$

### 6. Dérivée directionnelle seconde — page 153

Sur $\mathbb R^2$, résoudre $f_{xx}-2f_{xy}+f_{yy}=0$ avec $(u,v)=(x,x+y)$. L’inverse donne $g(u,v)=f(u,v-u)$.
$$g_u=f_x-f_y,\qquad g_{uu}=f_{xx}-2f_{xy}+f_{yy}=0.$$
Donc $g(u,v)=u C(v)+D(v)$ et
$$f(x,y)=x C(x+y)+D(x+y).$$

### 7. Variante produit-quotient — page 153

Sur $(\mathbb R_+^*)^2$, résoudre $x^2f_{xx}-y^2f_{yy}=0$ avec $(u,v)=(xy,x/y)$. Poser
$$g(u,v)=f(\sqrt{uv},\sqrt{u/v}).$$
La dérivation donne
$$g_v=\frac{\sqrt u}{2\sqrt v}f_x-\frac{\sqrt u}{2v\sqrt v}f_y,$$
$$g_{uv}=\frac1{2u}g_v+\frac14f_{xx}-\frac1{4v^2}f_{yy}.$$
L’EDP implique $2u g_{uv}=g_v$. À $v$ fixé, $g_v=C(v)\sqrt u$, donc $g(u,v)=D(v)\sqrt u+H(u)$ et
$$f(x,y)=D(x/y)\sqrt{xy}+H(xy).$$

## TD11–12, exercice 10 — Points critiques et extrema — pages 153–154

Déterminer les points critiques et les extrema des fonctions suivantes :

1. $f(x,y)=x^2+xy+y^2-3x-6y$.
2. $f(x,y)=x^2+2y^2-2xy-2y+5$.
3. $f(x,y)=x^3+y^3$.
4. $f(x,y)=(x-y)^2+(x+y)^3$.
5. $f(x,y)=x^3+y^3-3xy$.
6. $f(x,y)=x(\ln^2x+y^2)$ sur $x>0$.

**Aucune correction de cet exercice n’est fournie dans ce PDF.**

## TD11–12, exercice 11 — Extrema locaux et globaux — page 154

Déterminer les extrema locaux et globaux des applications suivantes :

| Fonction | Domaine | Expression |
| --- | --- | --- |
| $f_1$ | $\mathbb R^2$ | $-3x^2y+2z^4$ (coquille source : variable $z$ pour une fonction de $x,y$) |
| $f_2$ | $\mathbb R^2$ | $(y^2-x^2)(y^2-2x^2)$ |
| $f_3$ | $\mathbb R^2$ | $(x+y)^2-(x^4+y^4)$ |
| $f_4$ | $(\mathbb R_+^*)^2$ | $4xy+1/x+1/y$ |
| $f_5$ | $\mathbb R^2$ | $x^4+y^4-2(x-y)^2$ |
| $f_6$ | $\mathbb R^2$ | $3xy-x^3-y^3$ |
| $f_7$ | $\mathbb R^2$ | $x^3+y^3-9xy+27$ |
| $f_8$ | $(\mathbb R_+^*)^2$ | $x\ln y-y\ln x$ |
| $f_9$ | $\mathbb R^2$ | $x^2+xy+y^2-3x-6y$ |
| $f_{10}$ | $\mathbb R^2$ | $x^2+2y^2-2xy-2y+5$ |
| $f_{11}$ | $\mathbb R^2$ | $x^3+y^3$ |
| $f_{12}$ | $\mathbb R^2$ | $(x-y)^2+(x+y)^3$ |
| $f_{13}$ | $\mathbb R^2$ | $x^4+y^4-4xy$ |

**Aucune correction de cet exercice n’est fournie dans ce PDF.**

## TD11–12, exercice 12 — Extrema d’une fonction positive — page 154

On considère $g:(\mathbb R_+^*)^2\to\mathbb R$,
$$g(x,y)=\frac12\left(\frac1x+\frac1y\right)(1+x)(1+y).$$

1. Déterminer les extrema locaux de $g$.
2. On considère $f:\mathbb R_+^*\to\mathbb R$, $f(x)=\frac12(x+1/x)$.
   - a) Montrer que $f(x)\ge1$ pour tout $x>0$.
   - b) Montrer que $g(x,y)=1+f(x)+f(y)+f(x/y)$.
   - c) En conclure que les extrema locaux de $g$ sont globaux.

**Aucune correction de cet exercice n’est fournie dans ce PDF.**
