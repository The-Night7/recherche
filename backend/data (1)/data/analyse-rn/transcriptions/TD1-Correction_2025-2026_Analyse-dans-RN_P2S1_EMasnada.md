---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 2 à 20 (ancienne correction, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD1 — Normes, distances et boules (corrigé)

Les notes encadrées signalent ce qui a été corrigé ou ajouté par rapport à l'ancienne correction.

## Exercice 1 : Normes de ℝⁿ

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

## Exercice 2 : Norme sur l'espace des matrices carrées

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

## Exercice 3 : Norme sur l’espace des fonctions continues sur [0, 1]

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

## Exercice 4 : Autre norme

**Énoncé.** Soit l'application $N$ de $\mathbb{R}^2$ dans $\mathbb{R}$ qui à tout $(x, y)$ associe $N(x, y) = 4|x| + |y|$.

1. $N$ est-elle une norme ?
2. Dessiner la boule fermée de centre $(0,0)$ et de rayon $1$. Quelles sont ses symétries ?

**Correction.**

> **Complément :** cet exercice n'était pas corrigé dans l'ancienne correction (« à rédiger plus tard »). La correction ci-dessous a été rédigée pour cette transcription.

**1.** Oui.

- Si $4|x| + |y| = 0$, c'est une somme de deux termes positifs, donc $|x| = |y| = 0$ : $(x, y) = (0, 0)$.
- $N(\lambda x, \lambda y) = 4|\lambda|\,|x| + |\lambda|\,|y| = |\lambda|\, N(x, y)$.
- $N(x + x', y + y') = 4|x + x'| + |y + y'| \le 4|x| + 4|x'| + |y| + |y'| = N(x, y) + N(x', y')$.

C'est l'exercice 2 de l'ancienne feuille avec $a_1 = 4 > 0$ et $a_2 = 1 > 0$.

**2.** La boule fermée est $\{(x, y) : 4|x| + |y| \le 1\}$. Dans le quart de plan $x \ge 0$, $y \ge 0$, c'est la région sous la droite $4x + y = 1$, qui passe par $(\tfrac{1}{4}, 0)$ et $(0, 1)$. Par symétrie, on obtient un losange de sommets $(\pm \tfrac{1}{4}, 0)$ et $(0, \pm 1)$.

Ses symétries : l'axe des abscisses ($y \mapsto -y$), l'axe des ordonnées ($x \mapsto -x$) et le centre $(0,0)$ ($(x,y) \mapsto (-x,-y)$). Toute boule d'une norme est symétrique par rapport à son centre, puisque $N(-u) = N(u)$ ; ici, les valeurs absolues donnent en plus les deux symétries axiales.

## Exercice 5 : À propos des distances

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
