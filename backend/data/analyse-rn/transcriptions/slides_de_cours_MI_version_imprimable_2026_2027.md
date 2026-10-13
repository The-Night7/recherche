---
source: "PREING2-S1/Analyse-dans-RN/slides_de_cours_MI_version_imprimable_2026_2027.pdf"
pages: 203
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Analyse dans Rⁿ — Diapositives imprimables 2026–2027 — Elian Masnada

## Page 1

### Chapitre 1 — Introduction générale

**Analyse dans $\mathbb R^n$ — Mathématiques préING 2 — Ph.D. Elian Masnada — CY Tech. Version imprimable 2026–2027.** Les bandeaux et menus de navigation répétés ne sont pas recopiés à chaque page.

Les fonctions $f:\mathbb R\to\mathbb R$, étudiées en préING 1, ne suffisent pas à décrire de nombreux phénomènes. Exemples de fonctions de plusieurs variables : en thermodynamique, $U(T,P):\mathbb R^+\times\mathbb R^+\to\mathbb R$ ; en électromagnétisme, $\vec E,\vec B:\mathbb R^3\to\mathbb R^3$.

## Page 2

**Prédiction du prix d’un appartement par deep learning.** Trois données d’entrée sont représentées : surface en $\mathrm m^2$, notée $x_1^{(0)}$ ; nombre de chambres, $x_2^{(0)}$ ; revenu moyen dans l’immeuble, $x_3^{(0)}$.

## Page 3

Le schéma du réseau neuronal relie les trois entrées $\vec x^{(0)}$ à une couche cachée de trois neurones $x_1^{(1)},x_2^{(1)},x_3^{(1)}$, puis à une deuxième couche cachée de deux neurones $x_1^{(2)},x_2^{(2)}$, et enfin à la sortie $x_1^{(3)}$, le prix prédit en euros.

Chaque neurone d’une couche est relié aux neurones de la couche suivante. Les couleurs distinguent les connexions issues des différentes entrées ; les couches 1 et 2 sont les « neurones profonds (cachés) ».

## Page 4

Le réseau précédent est repris ; un encadré met en évidence le premier neurone de la première couche cachée, $x_1^{(1)}$, recevant les trois données d’entrée. Il prépare le détail du calcul effectué dans un neurone.

## Page 5

**Poids, biais, agrégation et activation.** Pour le neurone $j$ de la couche $n$, le signal provenant du neurone $k$ de la couche précédente a pour poids $w_{jk}^{(n)}$. L’agrégation est

$$p_j^{(n)}=\sum_k w_{jk}^{(n)}x_k^{(n-1)}+b_j^{(n)},$$

où $b_j^{(n)}$ est le biais. Une fonction d’activation transforme cette valeur ; l’exemple donné est

$$x_j^{(n)}=\max(0,p_j^{(n)}).$$

Le schéma détaille les poids $w_{11}^{(1)},w_{12}^{(1)},w_{13}^{(1)}$ des trois liaisons entrant dans $x_1^{(1)}$. Les légendes expliquent les indices : $n$ indique la couche, $j$ le neurone receveur, $k$ le neurone émetteur.

## Page 6

Si les poids $w_{jk}^{(n)}$ et biais $b_j^{(n)}$ sont connus, on peut déduire le prix de sortie :

$$x_1^{(3)}=f\bigl(\vec x^{(0)},w_{jk}^{(n)},b_j^{(n)}\bigr).$$

L’erreur représentée dans le support est

$$e^{(n)}=(x_1^{(3)}-PR)^2,$$

où $PR$ est le prix réel. Le schéma reprend le réseau complet et relie sa sortie au calcul de cette erreur quadratique.

## Page 7

**Comment trouver les poids et biais ?** C’est la phase d’entraînement du réseau.

1. Initialiser les poids et biais à des valeurs quelconques.
2. Effectuer un entraînement.
3. Calculer l’erreur de sortie $e^{(n)}$.
4. Appliquer la rétropropagation de l’erreur, illustrée par la règle de chaîne

$$\frac{\partial e}{\partial w}=\frac{\partial e}{\partial x}\frac{\partial x}{\partial p}\frac{\partial p}{\partial w}.$$

5. Actualiser les poids grâce aux dérivées ainsi calculées.

Le schéma boucle les étapes jusqu’à convergence. La formule est l’illustration d’une chaîne de dépendances ; dans un réseau comportant plusieurs chemins, les contributions des différents chemins se somment.

## Page 8

**Objectifs du cours.** En préING 1, pour $f:\mathbb R\to\mathbb R$ : limites, continuité ; dérivée, dérivabilité, développement limité ; équations différentielles.

En préING 2, généraliser ces notions aux applications $\mathbb R^n\to\mathbb R^p$, et plus généralement $E\to F$ entre espaces vectoriels.

## Page 9

**Plan — Chapitre 2 : espace vectoriel normé.**

Éléments de topologie dans $\mathbb R^n$ : normes et distances ; boules ouvertes et fermées ; ouverts, fermés et compacts ; intérieur et adhérence.

Suites d’éléments d’un EVN : convergence ; suites extraites et valeurs d’adhérence.

## Page 10

**Plan — Chapitre 3 : limite et applications continues.** Notions de limite et de continuité.

## Page 11

Le plan du chapitre 3 (limites, continuité) est rappelé.

**Chapitre 4 — Calcul différentiel du premier ordre :** dérivées partielles premières ; différentiabilité ; classe $\mathcal C^1$ ; EDP du premier ordre.

## Page 12

**Chapitre 5 — Calcul différentiel d’ordre supérieur :** dérivées partielles d’ordre supérieur à 1 ; classe $\mathcal C^k$ ; EDP du second ordre ; recherche d’extrema de fonctions de $\mathbb R^2$ dans $\mathbb R$.

## Page 13

Dernière remarque : le cours étudiera les applications d’un espace vectoriel quelconque dans un autre. Les applications connues $\mathbb R\to\mathbb R$ en sont un cas particulier, puisque $\mathbb R$ est un espace vectoriel. Les nouvelles définitions et les nouveaux théorèmes contiennent donc les notions déjà connues comme cas particuliers.

## Page 14

### Chapitre 2 — Espace vectoriel normé

Pour $f:D\subset\mathbb R\to\mathbb R$, rappel de la limite :

$$\lim_{x\to a}f(x)=\ell\Longleftrightarrow\forall\varepsilon>0,\ \exists\eta>0,\ \forall x\in D,\quad |x-a|<\eta\Rightarrow|f(x)-\ell|<\varepsilon.$$

Le dessin d’une courbe souligne la notion de distance $|x-a|$. C’est cette notion qu’il faudra généraliser. La convention de limite du support inclut $x=a$ lorsque ce point appartient au domaine.

## Page 15

La formule de limite de la page 14 est rappelée. La généralisation aux espaces vectoriels exige les notions de **norme** et de **distance**.

## Page 16

Rappel de la dérivée en une variable :

$$f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}.$$

Le schéma représente $x_0$ à l’intérieur de l’intervalle ouvert $D=]a,b[$, avec des approches possibles des deux côtés. Le support indique « alors bien défini pour tout $x_0\in D$ ».

> L’ouverture rend possible l’étude d’une limite bilatérale locale ; elle ne garantit pas l’existence de la dérivée d’une fonction quelconque.

## Page 17

Même quotient différentiel que page 16. Si $D=[a,b]$ est fermé, les points du bord demandent une attention particulière : le dessin place $x_0=a$, barre l’approche par la gauche hors du domaine, et conserve l’approche par la droite. On doit alors préciser une éventuelle dérivée unilatérale.

## Page 18

La généralisation de la dérivée motive l’étude :

- des normes et distances ;
- des ouverts et fermés, puis de l’intérieur et de l’adhérence.

C’est la raison de la partie de topologie qui suit. Le quotient différentiel $f'(x_0)=\lim_{x\to x_0}(f(x)-f(x_0))/(x-x_0)$ est rappelé.

## Page 19

### Partie 1 — Éléments de topologie : norme et distance

**Définition 1 — Norme.** Soit $E$ un espace vectoriel réel. Une application $\|\cdot\|:E\to\mathbb R$ est une norme si :

1. $\|x\|=0\Rightarrow x=0_E$ (séparation) ;
2. $\|\lambda x\|=|\lambda|\|x\|$ pour tous $x\in E$, $\lambda\in\mathbb R$ (homogénéité absolue) ;
3. $\|x+y\|\le\|x\|+\|y\|$ pour tous $x,y\in E$ (inégalité triangulaire).

$(E,\|\cdot\|)$ est alors un **espace vectoriel normé (EVN)**.

Remarque : $\|0_E\|=\|0\times0_E\|=0\times\|0_E\|=0$, d’où la réciproque de la séparation.

Exemple connu dans $\mathbb R^3$ : pour $\vec X=(x,y,z)$, $\|\vec X\|=\sqrt{x^2+y^2+z^2}$.

## Page 20

Pour $x=(x_1,\ldots,x_n)\in\mathbb R^n$, trois exemples de normes sont

$$\|x\|_1=\sum_{i=1}^n|x_i|,\qquad \|x\|_2=\sqrt{\sum_{i=1}^n x_i^2},\qquad \|x\|_\infty=\max_{1\le i\le n}|x_i|.\tag{2.2}$$

Si $E=\mathbb R$, les trois normes sont égales à $|x|$.

Dans $\mathbb R^3$, $\|(x,y,z)\|_2=\sqrt{x^2+y^2+z^2}$ : c’est la norme euclidienne connue.

## Page 21

Les trois normes de la page précédente sont rappelées. Illustration dans le plan entre $A=(3,5)$ et $B=(7,2)$ :

- la norme 1, dite de Manhattan, correspond au trajet horizontal puis vertical ;
- la norme 2, euclidienne, correspond au segment direct.

Le dessin compare ainsi les distances associées aux deux normes, $\|B-A\|_1$ et $\|B-A\|_2$ (respectivement $7$ et $5$, valeurs déduites des coordonnées du schéma).

## Page 22

Vérification que $\|x\|_1=\sum_{i=1}^n|x_i|$ est une norme.

**Séparation :** $\|x\|_1=0\Rightarrow\forall i,\ x_i=0\Rightarrow x=0_E$.

**Homogénéité :** pour $\lambda x=(\lambda x_1,\ldots,\lambda x_n)$,

$$\|\lambda x\|_1=\sum_{i=1}^n|\lambda x_i|=|\lambda|\sum_{i=1}^n|x_i|=|\lambda|\|x\|_1.$$

**Inégalité triangulaire :** pour $x+y=(x_1+y_1,\ldots,x_n+y_n)$,

$$\|x+y\|_1=\sum_{i=1}^n|x_i+y_i|\le\sum_{i=1}^n(|x_i|+|y_i|)=\|x\|_1+\|y\|_1.$$

## Page 23

L’application $N:\mathbb R^2\to\mathbb R$, $N(x,y)=|4x+7y|$, est-elle une norme ? **Non.** En effet,

$$N(x,y)=0\Longleftrightarrow |4x+7y|=0\Longleftrightarrow x=-\frac74y.$$

La séparation n’est donc pas vérifiée.

Sur $E=\mathcal C([0,1],\mathbb R)$, les trois normes fréquemment utilisées sont

$$\|f\|_1=\int_0^1|f(x)|\,dx,\qquad \|f\|_2=\sqrt{\int_0^1f(x)^2\,dx},\qquad \|f\|_\infty=\max_{0\le x\le1}|f(x)|.$$

## Page 24

**Propriété 1 — Positivité.** Pour tout $x\in E$, $\|x\|\ge0$.

Démonstration : $0=\|0_E\|=\|x-x\|\le\|x\|+\|-x\|=2\|x\|$.

**Propriété 2 — Cas d’égalité pour la norme euclidienne.** La diapositive imprime

$$\|x+y\|=\|x\|+\|y\|\Longleftrightarrow x=\lambda y,\quad\lambda\in\mathbb R.$$

La preuve est renvoyée au cours d’algèbre bilinéaire. Avertissement : cette propriété ne vaut pas pour une norme quelconque (renvoi au polycopié, p. 17).

> Correction de l’énoncé imprimé : en norme euclidienne, l’égalité signifie que les vecteurs sont positivement colinéaires, avec prise en compte des vecteurs nuls. Si $y\ne0$, il faut $x=\lambda y$ avec $\lambda\ge0$ ; si $y=0$, tout $x$ convient. La seule colinéarité avec un réel quelconque ne suffit pas.

## Page 25

**Propriété 3 — Seconde inégalité triangulaire.**

$$\forall x,y\in E,\qquad \|x-y\|\ge\bigl|\|x\|-\|y\|\bigr|.$$

Démonstration :

$$\|x\|=\|x-y+y\|\le\|x-y\|+\|y\|\ \Longrightarrow\ \|x-y\|\ge\|x\|-\|y\|,$$

$$\|y\|=\|y-x+x\|\le\|y-x\|+\|x\|\ \Longrightarrow\ \|x-y\|\ge\|y\|-\|x\|.$$

On obtient $\|x-y\|\ge\max(\|y\|-\|x\|,\|x\|-\|y\|)=|\|x\|-\|y\||$.

## Page 26

**Définition 2 — Normes équivalentes.** Deux normes $\|\cdot\|_a$ et $\|\cdot\|_b$ sur $E$ sont équivalentes s’il existe $\alpha,\beta>0$ tels que

$$\forall x\in E,\quad \alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a.$$

Cette relation est une relation d’équivalence. **Réflexivité :** $\|x\|_a\le\|x\|_a\le\|x\|_a$, avec $\alpha=\beta=1$.

## Page 27

**Symétrie de l’équivalence des normes.** Si

$$\alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a,\qquad\alpha,\beta>0,$$

alors $\|x\|_a\le\alpha^{-1}\|x\|_b$ et $\beta^{-1}\|x\|_b\le\|x\|_a$. Ainsi

$$\frac1\beta\|x\|_b\le\|x\|_a\le\frac1\alpha\|x\|_b,$$

ce qui établit l’équivalence dans l’autre sens.

## Page 28

**Transitivité.** Supposons les normes $a,b$ équivalentes et les normes $b,c$ équivalentes. Il existe $\alpha,\beta,\eta,\gamma>0$ tels que

$$\alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a,\qquad \eta\|x\|_b\le\|x\|_c\le\gamma\|x\|_b.$$

Donc $\|x\|_c\ge\eta\|x\|_b\ge\eta\alpha\|x\|_a$ et $\|x\|_c\le\gamma\|x\|_b\le\gamma\beta\|x\|_a$, d’où

$$\eta\alpha\|x\|_a\le\|x\|_c\le\gamma\beta\|x\|_a.$$

## Page 29

Réflexivité, transitivité et symétrie établissent une relation d’équivalence.

**Théorème 1 — Équivalence des normes.** Sur un espace vectoriel de dimension finie, toutes les normes sont équivalentes.

Démonstration admise. Ce théorème sera fondamental dans la suite du cours.

## Page 30

**Définition 3 — Distance.** Soit $X$ un ensemble. Une application $d:X\times X\to\mathbb R^+$ est une distance si :

1. $d(P,Q)=0\Longleftrightarrow P=Q$ ;
2. $d(P,Q)=d(Q,P)$ ;
3. $d(P,Q)\le d(P,R)+d(R,Q)$ pour tous $P,Q,R\in X$.

La distance est nulle seulement entre deux points confondus et elle est symétrique. Le schéma de trois points illustre l’inégalité triangulaire : passer par un troisième point ne réduit pas la distance, et peut faire un détour. Les points sont notés $X,Y,Z$ dans le dessin.

## Page 31

**Propriété 4 — Positivité de la distance.** $d(X,Y)\ge0$.

La preuve repose sur $0=d(X,X)\le d(X,Y)+d(Y,X)=2d(X,Y)$.

**Propriété 5 — Distance associée à une norme.** Dans un EVN, $d(X,Y)=\|X-Y\|$ est une distance. La preuve est renvoyée au polycopié.

## Page 32

**Propriété 6.** Pour une distance associée à une norme,

$$\forall X,Y\in E,\ \forall\lambda\in\mathbb R,\qquad d(\lambda X,\lambda Y)=|\lambda|d(X,Y).$$

Démonstration : $\|\lambda X-\lambda Y\|=|\lambda|\|X-Y\|$.

Exemple dans $\mathbb R^2$, avec $X=(x_1,x_2)$ et $Y=(y_1,y_2)$ :

$$d(X,Y)=\|X-Y\|_2=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2}.$$

## Page 33

Soit $E$ un espace vectoriel et

$$d_0(X,Y)=\begin{cases}0,&X=Y,\\1,&X\ne Y.\end{cases}$$

Vérification : la séparation est immédiate et $d_0$ est symétrique. Pour l’inégalité triangulaire, la source examine les cas :

- $X=Y=Z$ : $0\le0+0$ ;
- $X=Y\ne Z$ : $0\le1+1$ ;
- $X=Z\ne Y$ : $1\le0+1$ ;
- $X\ne Y=Z$ : $1\le1+0$ ;
- les trois points distincts : $1\le1+1$.

C’est donc une distance. Sur un espace non nul, elle n’est pas associée à une norme : pour $X\ne Y$ et $\lambda=3$, $d_0(3X,3Y)=1\ne3d_0(X,Y)$.

## Page 34

### Boule ouverte, boule fermée et sphère

**Définition 4.** Dans $(E,\|\cdot\|)$, pour $a\in E$ et $r>0$ :

$$B(a,r)=\{x\in E:\|x-a\|<r\},$$

$$\overline B(a,r)=\{x\in E:\|x-a\|\le r\},$$

$$S(a,r)=\{x\in E:\|x-a\|=r\}.$$

Ainsi $\overline B(a,r)=B(a,r)\cup S(a,r)$.

## Page 35

**Boules dans $(\mathbb R,|\cdot|)$.** Pour un centre $a$ et un rayon $\varepsilon>0$ :

$$|x-a|\le\varepsilon\Longleftrightarrow x\in[a-\varepsilon,a+\varepsilon],$$

$$|x-a|<\varepsilon\Longleftrightarrow x\in]a-\varepsilon,a+\varepsilon[.$$

Le premier intervalle est la boule fermée, représentée avec des crochets fermés ; le second est la boule ouverte, avec des extrémités exclues. Les schémas marquent le centre $a$ et le rayon $\varepsilon$.

## Page 36

La forme des boules dépend de la norme choisie. On compare les boules fermées unitaires de centre $(0,0)$ dans $\mathbb R^2$.

**Norme 1 :** $\|(x,y)\|_1=|x|+|y|\le1$. Sur la frontière :

- $x>0,y>0$ : $x+y=1$, donc $y=1-x$ ;
- $x>0,y<0$ : $x-y=1$, donc $y=x-1$ ;
- $x<0,y>0$ : $-x+y=1$, donc $y=1+x$ ;
- $x<0,y<0$ : $-x-y=1$, donc $y=-1-x$.

Le dessin représente le losange plein de sommets $(1,0),(0,1),(-1,0),(0,-1)$. Les axes font partie de la boule ; les signes stricts ci-dessus servent seulement à décrire les quatre côtés hors sommets.

## Page 37

**Norme 2 :** $\|(x,y)\|_2=\sqrt{x^2+y^2}$. La boule fermée unité est le disque plein $x^2+y^2\le1$, dont la frontière est le cercle unité.

**Norme infinie :** le cas est laissé en exercice, avec un dessin du carré plein $[-1,1]^2$. Il correspond à $\max(|x|,|y|)\le1$.

## Page 38

**Propriété 7.** Pour des boules de même centre, dans un EVN non nul, et pour $r,r'>0$ :

$$r<r'\Longleftrightarrow B(a,r)\subsetneq B(a,r'),\qquad r<r'\Longleftrightarrow\overline B(a,r)\subsetneq\overline B(a,r').$$

Preuve pour les boules ouvertes. Si $r<r'$ et $x_0\in B(a,r)$, alors $\|x_0-a\|<r<r'$, donc $x_0\in B(a,r')$. Réciproquement, l’inclusion stricte fournit un point $y\in B(a,r')\setminus B(a,r)$, d’où $r\le\|y-a\|<r'$.

> Précisions : le symbole $\subset$ de la source doit signifier ici une inclusion stricte pour l’équivalence. L’espace doit être non nul. La stricte inclusion du sens direct, non justifiée dans la source, se vérifie en prenant un vecteur de norme comprise entre $r$ et $r'$.

## Page 39

### Voisinage

**Définition 5.** Une partie $V\subset E$ est un voisinage de $a\in E$ si elle contient au moins une boule ouverte centrée en $a$ et de rayon strictement positif :

$$V\in\mathcal V(a)\Longleftrightarrow\exists r>0,\quad B(a,r)\subset V.$$

$\mathcal V(a)$ désigne l’ensemble des voisinages de $a$. Le dessin montre, dans le plan euclidien, un ensemble de contour irrégulier contenant $B(a,0{,}3)$.

## Page 40

**Propriété 8.** En dimension finie, être un voisinage de $a$ ne dépend pas du choix de la norme. Preuve renvoyée au polycopié.

**Propriété 9.** Un point appartient à chacun de ses voisinages : $V\in\mathcal V(a)\Rightarrow a\in V$.

En effet, $V$ contient $B(a,r)$ pour un $r>0$. Or $\|a-a\|=\|0_E\|=0<r$, donc $a\in B(a,r)\subset V$.

## Page 41

**Propriété 11.** Toute boule ouverte ou fermée de centre $a$ et de rayon $r>0$ est un voisinage de $a$.

Pour la boule ouverte, prendre $r'=r/2$ : d’après la propriété 7, $B(a,r')\subset B(a,r)$, donc $B(a,r)$ est un voisinage de $a$. Pour la boule fermée, le même choix donne $B(a,r')\subset\overline B(a,r)$, donc celle-ci est également un voisinage de $a$.

## Page 42

**Propriété 12.** Toute intersection **finie** de voisinages de $a$ est un voisinage de $a$. Démonstration : voir le polycopié.

La finitude est nécessaire. Dans $(\mathbb R,|\cdot|)$, $B(a,r)=\{x:|x-a|<r\}=]a-r,a+r[$ ; un voisinage de $a$ contient une telle boule. Pour $a=0$ et $r=1/n$, $n\ge1$, les intervalles $V_n=]-1/n,1/n[$ sont des voisinages de $0$ d’après la propriété 11, mais

$$\bigcap_{n=1}^{\infty}V_n=\{0\},$$

qui n’est pas un voisinage de $0$ dans $\mathbb R$.

## Page 43

**Définition 6 — Espace séparé.** Un espace muni d’une notion de voisinage est séparé si deux points distincts ont des voisinages disjoints :

$$a\ne b\Longrightarrow\exists V_a\in\mathcal V(a),\ \exists V_b\in\mathcal V(b),\quad V_a\cap V_b=\varnothing.$$

Le schéma représente deux ensembles disjoints $V_a,V_b$, contenant respectivement une petite boule autour de $a$ et autour de $b$.

## Page 44

**Propriété 13.** Tout EVN est séparé.

Pour $a\ne b$, poser

$$V_a=B\left(a,\frac{\|b-a\|}{2}\right),\qquad V_b=B\left(b,\frac{\|b-a\|}{2}\right).$$

Si $x\in V_a\cap V_b$, alors $\|x-a\|<\|b-a\|/2$ et $\|x-b\|<\|b-a\|/2$. L’inégalité triangulaire donnerait

$$\|a-b\|\le\|a-x\|+\|x-b\|<\|a-b\|,$$

contradiction ; l’intersection est donc vide. Le dessin en dimension 1 marque $a$, $b$ et leur milieu $(a+b)/2$.

## Page 45

### Ouverts et fermés

**Définition 7 — Ouvert.** Une partie $U$ de l’EVN $E$ est ouverte si chaque point de $U$ possède un voisinage contenu dans $U$ :

$$U\text{ ouvert}\Longleftrightarrow\forall x\in U,\ \exists r>0,\quad B(x,r)\subset U.$$

Le dessin place des boules de tailles différentes autour de deux points d’un ouvert. Convention graphique : les contours des ouverts seront dessinés en pointillés. Autrement dit, $U$ est un voisinage de chacun de ses points.

## Page 46

**Propriété 14.** En dimension finie, être ouvert ne dépend pas du choix de la norme. Cela résulte de la propriété 8.

**Propriété 15.** Dans un EVN, $\varnothing$ et $E$ sont ouverts. Le support qualifie l’ouverture du vide de conventionnelle et celle de $E$ de triviale.

Précision logique : le vide satisfait la définition par absence de point à vérifier ; pour $E$, toute boule centrée en un de ses points est contenue dans $E$.

## Page 47

**Propriété 16.** Une boule ouverte est un ouvert.

Soit $X\in B(a,r)$. Introduire

$$r'=r-\|X-a\|>0,\qquad B(X,r').$$

Le schéma dans le plan montre cette petite boule à l’intérieur de $B(a,r)$, tangente intérieurement à sa frontière. Il suggère $B(X,r')\subset B(a,r)$. La preuve doit valoir dans tout EVN, pas seulement dans $\mathbb R^2$.

## Page 48

Preuve de l’inclusion : pour $Y\in B(X,r')$,

$$\|Y-a\|=\|Y-X+X-a\|\le\|Y-X\|+\|X-a\|<r'+\|X-a\|=r.$$

Donc $B(X,r')\subset B(a,r)$. Comme tout $X\in B(a,r)$ vérifie $r'=r-\|X-a\|>0$, chaque point possède une boule ouverte contenue dans $B(a,r)$.

## Page 49

**Propriété 17.** Une union quelconque d’ouverts est ouverte.

Soit $U=\bigcup_{i\in I}U_i$. Pour $x\in U$, il existe $i$ tel que $x\in U_i$. Puisque $U_i$ est ouvert, il existe $r_i>0$ tel que $B(x,r_i)\subset U_i\subset U$. Le raisonnement vaut pour tout $x\in U$ ; donc $U$ est ouvert.

## Page 50

**Propriété 18.** Toute intersection finie d’ouverts est ouverte.

Pour $U=\bigcap_{i=1}^nU_i$ et $x\in U$, chaque $U_i$ est un voisinage de $x$. Leur intersection finie est encore un voisinage de $x$. Donc $U$ est voisinage de chacun de ses points et est ouvert.

## Page 51

**Corollaire.** Si $a<b$ dans $\mathbb R$, les intervalles $]-\infty,b[$, $]a,b[$ et $]a,+\infty[$ sont ouverts.

Démonstration :

$$]a,b[=B\left(\frac{a+b}{2},\frac{b-a}{2}\right),$$

$$]a,+\infty[=\bigcup_{\alpha>a}]a,\alpha[,\qquad ]-\infty,b[=\bigcup_{\alpha<b}]\alpha,b[.$$

Le premier est une boule ouverte ; les deux autres sont des unions d’ouverts.

## Page 52

**Définition 8 — Fermé.** Une partie $F\subset E$ est fermée si et seulement si son complémentaire $C_EF=E\setminus F$ est ouvert.

**Propriété 19.** $\varnothing$ et $E$ sont fermés, donc à la fois ouverts et fermés.

Preuve : $C_E\varnothing=E$ est ouvert, et $C_EE=\varnothing$ est ouvert.

## Page 53

**Propriété 20.** Une boule fermée est fermée.

Démonstration renvoyée au polycopié. Le dessin représente un point $X$ extérieur à $\overline B(a,r)$, et une boule ouverte autour de $X$ contenue dans le complémentaire ; son rayon peut être choisi $r'=\|X-a\|-r>0$. Le centre de cette petite boule est $X$.

## Page 54

**Propriété 21.** Toute intersection de fermés est fermée.

Rappel de la loi de De Morgan :

$$C_E\left(\bigcup_iU_i\right)=\bigcap_i(C_EU_i).$$

Si les $U_i$ sont ouverts, $U=\bigcup_iU_i$ est ouvert. Chaque $C_EU_i$ est fermé, et leur intersection est $C_EU$, fermé puisque $U$ est ouvert. En prenant les $U_i$ complémentaires des fermés donnés, on obtient l’énoncé.

## Page 55

**Propriété 22.** Toute union finie de fermés est fermée. La démonstration s’obtient comme précédemment en passant aux complémentaires, à partir de l’intersection finie d’ouverts.

**Corollaire.** Dans $\mathbb R$, pour $a<b$, les intervalles $]-\infty,b]$, $[a,b]$ et $[a,+\infty[$ sont fermés. La source indique « trivial ».

## Page 56

### Intérieur et adhérence

**Définition 9 — Intérieur.** Soit $A\subset E$. Un point $a$ est intérieur à $A$ si $A$ est un voisinage de $a$. L’ensemble des points intérieurs se note $\mathring A$.

$$x\in\mathring A\Longleftrightarrow\exists r>0,\quad B(x,r)\subset A,$$

$$x\in\mathring A\Longleftrightarrow\exists U\subset A,\quad U\text{ ouvert et }x\in U.$$

Le schéma représente une boule $B(a,0{,}3)$ entièrement contenue dans $A$.

## Page 57

**Propriété 23.** $\mathring A\subset A$.

Preuve : si $x\in\mathring A$, une boule $B(x,r)$ est contenue dans $A$, et $x$ appartient à cette boule ; donc $x\in A$.

**Propriété 24.** $\mathring A$ est le plus grand ouvert contenu dans $A$. Démonstration renvoyée au polycopié.

## Page 58

**Propriété 25.** Pour $A,B\subset E$ :

1. $A$ est ouvert si et seulement si $\mathring A=A$.
2. $\operatorname{int}(\mathring A)=\mathring A$.
3. $A\subset B\Rightarrow\mathring A\subset\mathring B$.

Démonstrations :

1. Si $A$ est ouvert, c’est lui-même le plus grand ouvert contenu dans $A$. Réciproquement, $A=\mathring A$ est ouvert puisque tout intérieur est ouvert.
2. Appliquer 1 à l’ouvert $\mathring A$.
3. Si $x\in\mathring A$, il existe $r>0$ tel que $B(x,r)\subset A\subset B$, donc $x\in\mathring B$.

## Page 59

Exemples dans $\mathbb R$, pour $a<b$ :

$$\operatorname{int}(]a,b[)=\operatorname{int}([a,b[)=\operatorname{int}(]a,b])=\operatorname{int}([a,b])=]a,b[.$$

Dans $\mathbb R^n$, pour $r>0$ :

$$\operatorname{int}(B(a,r))=B(a,r),\qquad \operatorname{int}(\overline B(a,r))=B(a,r).$$

## Page 60

**Définition 10 — Adhérence.** Un point $a$ est adhérent à $A$ si tout voisinage de $a$ rencontre $A$. L’ensemble des points adhérents, l’adhérence de $A$, se note $\overline A$.

$$x\in\overline A\Longleftrightarrow\forall r>0,\quad B(x,r)\cap A\ne\varnothing.$$

Le dessin distingue trois points : $a$ intérieur, donc $a\in\mathring A$ et $a\in\overline A$ ; $b$ sur la frontière, donc $b\notin\mathring A$ mais $b\in\overline A$ ; $c$ extérieur à l’adhérence, donc $c\notin\mathring A$ et $c\notin\overline A$.

## Page 61

**Propriété 26.** $A\subset\overline A$.

Si $x\in A$, alors pour tout $r>0$, $x\in B(x,r)\cap A$, donc $x\in\overline A$.

**Propriété 27.** $\overline A$ est fermé. On étudie $C_E\overline A$. Si $x\notin\overline A$, il existe $r>0$ tel que $B(x,r)\cap A=\varnothing$.

> La source conclut directement $B(x,r)\subset C_E\overline A$. Pour justifier cette étape, si $y\in B(x,r)$, la boule $B(y,r-\|y-x\|)$ est contenue dans $B(x,r)$ et évite $A$ ; donc $y\notin\overline A$. Le complémentaire de $\overline A$ est bien ouvert.

## Page 62

**Propriété 28 — Admise.** $\overline A$ est le plus petit fermé contenant $A$.

**Propriété 29.**

1. $A$ fermé $\Longleftrightarrow\overline A=A$.
2. $\overline{\overline A}=\overline A$.
3. $A\subset B\Rightarrow\overline A\subset\overline B$.

Preuves :

1. Si $A=\overline A$, il est fermé ; si $A$ est fermé, le plus petit fermé qui le contient est lui-même.
2. $\overline A$ étant fermé, appliquer 1.
3. Si $a\in\overline A$ et $V$ est un voisinage de $a$, alors $A\cap V\ne\varnothing$. Comme $A\cap V\subset B\cap V$, ce dernier est non vide ; donc $a\in\overline B$.

## Page 63

**Propriété 30.** Pour deux parties $A,B$ d’un EVN :

1. $\overline{A\cup B}=\overline A\cup\overline B$.
2. $\overline{A\cap B}\subset\overline A\cap\overline B$.
3. $\operatorname{int}(A\cap B)=\mathring A\cap\mathring B$.
4. $\mathring A\cup\mathring B\subset\operatorname{int}(A\cup B)$.

Démonstration : voir le polycopié.

**Illustration du point 2.** Pour $A=]0,1[$ et $B=[1,2[$, l’intersection est vide, donc $\overline{A\cap B}=\varnothing$. En revanche, $\overline A=[0,1]$ et $\overline B=[1,2]$, donc $\overline A\cap\overline B=\{1\}$. L’inclusion peut être stricte.

## Page 64

**Propriété 30.** Pour deux parties $A,B$ d’un EVN :

1. $\overline{A\cup B}=\overline A\cup\overline B$.
2. $\overline{A\cap B}\subset\overline A\cap\overline B$.
3. $\operatorname{int}(A\cap B)=\mathring A\cap\mathring B$.
4. $\mathring A\cup\mathring B\subset\operatorname{int}(A\cup B)$.

Démonstration : voir le polycopié.

**Illustration du point 4.** Pour $A=[0,1]$ et $B=[1,2]$, $A\cup B=[0,2]$ et $\operatorname{int}(A\cup B)=]0,2[$. Or $\mathring A=]0,1[$ et $\mathring B=]1,2[$ : leur réunion omet $1$. L’inclusion peut donc être stricte.

## Page 65

**Définition 11 — Frontière.** La frontière de $A$, notée $\operatorname{Fr}(A)$ ou $\partial A$, est

$$\partial A=\overline A\setminus\mathring A.$$

Exemple : $\overline B(a,r)$ est fermé et son intérieur est $B(a,r)$, donc

$$\partial\overline B(a,r)=\overline B(a,r)\setminus B(a,r)=S(a,r).$$

**Propriété 31.** $\overline A=A\cup\partial A$ et $\mathring A=A\setminus\partial A$.

## Page 66

**Méthodologie — Montrer qu’un ensemble $A$ n’est pas ouvert.** Trouver au moins un point **appartenant à $A$**, situé sur sa frontière, tel que toute boule ouverte centrée en ce point déborde de $A$.

Exemple représenté :

$$A=\{(x,y)\in\mathbb R^2:-1\le x<1,\ -1\le y\le1\}.$$

Le point $(-1,0)$ appartient à $A$, mais toute boule centrée en ce point contient des points d’abscisse inférieure à $-1$, extérieurs à $A$. Donc $A$ n’est pas ouvert.

## Page 67

**Méthodologie — Montrer qu’un ensemble $A$ n’est pas fermé.** Trouver un point du complémentaire $C_EA$, sur la frontière, tel que toute boule centrée en ce point déborde de $C_EA$.

Pour le même rectangle $A=[-1,1[\times[-1,1]$, le point $(1,0)$ appartient au complémentaire, mais toute boule centrée en lui rencontre $A$. Le complémentaire n’est donc pas ouvert et $A$ n’est pas fermé. Sur le schéma, le complémentaire est hachuré en rouge.

## Page 68

**Méthodologie — Trouver l’intérieur de $A$ (démonstration en TD3).**

0. Proposer un candidat $B$, en sachant que $\mathring A$ est le plus grand ouvert contenu dans $A$.
1. Vérifier que $B$ est ouvert.
2. Vérifier $B\subset A$. Les deux étapes entraînent : pour tout $x\in B$, il existe $r>0$ tel que $B(x,r)\subset A$, donc $B\subset\mathring A$. Le candidat peut toutefois être trop petit, comme l’illustre le dessin d’ensembles emboîtés.
3. Vérifier $\mathring A\subset B$ : pour tout $x\in A\setminus B$, montrer que, pour tout $r>0$, $B(x,r)\not\subset A$.

On conclut $\mathring A=B$.

## Page 69

**Méthodologie — Trouver l’adhérence de $A$ (démonstration en TD3).**

0. Proposer un candidat $B$, en sachant que $\overline A$ est le plus petit fermé contenant $A$.
1. Vérifier que $B$ est fermé.
2. Vérifier $A\subset B$. Pour $x\notin B$, une boule $B(x,r)$ est contenue dans le complémentaire de $B$ et évite $A$. Donc $x\notin\overline A$ et $\overline A\subset B$. Le candidat peut être trop grand.
3. Vérifier $B\subset\overline A$ : pour tout $x\in B\setminus A$ et tout $r>0$, établir $B(x,r)\cap A\ne\varnothing$.

On conclut $\overline A=B$.

## Page 70

### Partie 2 — Suites d’éléments d’un EVN : généralités

**Rappel 1.** Une suite réelle est une application de $\mathbb N$ dans $\mathbb R$, notée $(x_n)_{n\in\mathbb N}$. Exemples indiqués : $x_n=1/n$ (pour $n\ge1$) et $x_n=2.3n$ (notation décimale imprimée, soit $2{,}3n$).

**Rappel 2.** Une suite réelle converge vers $\ell\in\mathbb R$ si et seulement si

$$\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\quad |x_n-\ell|<\varepsilon.$$

On note $\lim_{n\to\infty}x_n=\ell$.

## Page 71

**Définition 12.** Une suite d’éléments de l’EVN $E$ est une application $\mathbb N\to E$, de terme général $x_n$, notée $(x_n)_{n\in\mathbb N}$.

Exemples : dans $E=\mathbb R$, $n\mapsto2{,}3n$ ; dans $E=\mathbb R^3$,

$$n\longmapsto\left(\frac1n,\ 2n+3,\ \left(\frac32\right)^n\right),\qquad n\ge1.$$

## Page 72

**Définition 13 — Suite bornée.** Une suite $(x_n)$ de $E$ est bornée si et seulement si la suite réelle $(\|x_n\|)$ est bornée :

$$\exists M>0,\ \forall n\in\mathbb N,\quad \|x_n\|\le M.$$

Exemple dans $(\mathbb R^3,\|\cdot\|_2)$ : $x_n=(2n,-3n,1/n)$, $n\ge1$. Alors

$$\|x_n\|_2=\sqrt{4n^2+9n^2+\frac1{n^2}}\longrightarrow+\infty.$$

Cette suite n’est pas bornée.

## Page 73

**Définition 14 — Suite convergente.** Pour $\ell\in E$, les trois formulations suivantes sont équivalentes et signifient $x_n\to\ell$ :

1. $\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\ \|x_n-\ell\|<\varepsilon$.
2. $\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\ x_n\in B(\ell,\varepsilon)$.
3. $\forall V\in\mathcal V(\ell),\ \exists N\in\mathbb N,\ \forall n\ge N,\ x_n\in V$.

La preuve de l’équivalence est renvoyée au polycopié.

## Page 74

**Propriété 32 — Unicité de la limite.** Si une suite d’un EVN converge, sa limite est unique.

Supposer deux limites distinctes $\ell_1,\ell_2$. Puisque l’EVN est séparé, choisir des voisinages disjoints $V_1\in\mathcal V(\ell_1)$ et $V_2\in\mathcal V(\ell_2)$. La convergence fournit des rangs $N_1,N_2$ tels que $n\ge N_i\Rightarrow x_n\in V_i$. Pour $n\ge\max(N_1,N_2)$, on aurait $x_n\in V_1\cap V_2=\varnothing$, contradiction.

> La ligne du deuxième voisinage répète l’indice 1 : il faut lire $V_2\in\mathcal V(\ell_2)$.

## Page 75

**Propriété 33.** Si $x_n\to\ell$ et $y_n\to\ell'$ dans $E$ :

1. $\|x_n\|\to\|\ell\|$.
2. $x_n\to0_E\Longleftrightarrow\|x_n\|\to0$.
3. Pour $\lambda\in\mathbb R$, $x_n+\lambda y_n\to\ell+\lambda\ell'$.

Remarque : $(\|x_n\|)$ est une suite réelle positive ; sa convergence vers $\|\ell\|$ signifie

$$\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\quad\bigl|\|x_n\|-\|\ell\|\bigr|<\varepsilon.$$

## Page 76

Preuve du premier point de la propriété 33, dont l’énoncé est rappelé en haut de page.

La convergence $x_n\to\ell$ donne, pour tout $\varepsilon>0$, un rang $N$ au-delà duquel $\|x_n-\ell\|<\varepsilon$. Par la seconde inégalité triangulaire,

$$\bigl|\|x_n\|-\|\ell\|\bigr|\le\|x_n-\ell\|<\varepsilon.$$

Donc $\|x_n\|\to\|\ell\|$.

## Page 77

Preuve du deuxième point : les deux assertions $x_n\to0_E$ et $\|x_n\|\to0$ s’écrivent toutes deux

$$\forall\varepsilon>0,\ \exists N\in\mathbb N,\ \forall n\ge N,\quad\|x_n\|<\varepsilon.$$

Elles sont donc équivalentes. Le zéro limite de la suite réelle des normes est le réel $0$ (le support répète à cet endroit $0_E$).

## Page 78

Preuve du troisième point de la propriété 33. Pour $\lambda\ne0$ et $\varepsilon>0$, la convergence fournit $N,N'$ tels que

$$n\ge N\Rightarrow\|x_n-\ell\|<\frac\varepsilon2,\qquad n\ge N'\Rightarrow\|y_n-\ell'\|<\frac{\varepsilon}{2|\lambda|}.$$

Pour $N_0=\max(N,N')$ et $n\ge N_0$,

$$\|(x_n+\lambda y_n)-(\ell+\lambda\ell')\|\le\|x_n-\ell\|+|\lambda|\|y_n-\ell'\|<\frac\varepsilon2+|\lambda|\frac{\varepsilon}{2|\lambda|}=\varepsilon.$$

Ainsi $x_n+\lambda y_n\to\ell+\lambda\ell'$. Le cas $\lambda=0$ découle directement de $x_n\to\ell$.

## Page 79

**Propriété 34 — Convergence coordonnée par coordonnée.** Dans $E=\mathbb R^p$ muni d’une norme, si $x_n=(x_n^{(1)},\ldots,x_n^{(p)})$, alors

$$x_n\longrightarrow(\ell_1,\ldots,\ell_p)\Longleftrightarrow\forall i\in\{1,\ldots,p\},\quad x_n^{(i)}\longrightarrow\ell_i.$$

Exemple : dans $\mathbb R^2$,

$$x_n=\left(1-\frac1n,\frac1{n^2}\right)\longrightarrow(1,0).$$

## Page 80

### Valeurs d’adhérence — Rappel sur les suites extraites

Pour une suite $(x_n)$ de $E$ et une application $\phi:\mathbb N\to\mathbb N$ strictement croissante, la suite $y_n=x_{\phi(n)}$ est une **suite extraite**, ou sous-suite.

Exemple : $x_n=(e^{n^2},n+4)$ dans $\mathbb R^2$ et $\phi(n)=2n+1$. Alors

$$y_n=x_{2n+1}=\left(e^{(2n+1)^2},\ 2n+5\right).$$

> La dernière ligne du support mélange les indices $y_{\phi(n)}$ et $x_n$ ; c’est bien le terme $y_n=x_{\phi(n)}$ défini ci-dessus.

## Page 81

**Propriété 35.** Toute suite extraite d’une suite convergeant vers $\ell$ converge également vers $\ell$.

Preuve, étape 1 : une application $\phi:\mathbb N\to\mathbb N$ strictement croissante vérifie $\phi(n)\ge n$.

Récurrence : $\phi(0)\ge0$. Si $\phi(n)\ge n$, alors $\phi(n+1)>\phi(n)\ge n$, et comme les valeurs sont entières, $\phi(n+1)\ge n+1$.

## Page 82

Preuve de la propriété 35, étape 2. Si $x_n\to\ell$, pour tout $\varepsilon>0$ il existe $N$ tel que $n\ge N\Rightarrow\|x_n-\ell\|<\varepsilon$.

Or $\phi(n)\ge n$. Ainsi, pour $n\ge N$, $\phi(n)\ge N$ et

$$\|x_{\phi(n)}-\ell\|<\varepsilon.$$

Donc $x_{\phi(n)}\to\ell$.

## Page 83

**Définition 15 — Valeur d’adhérence d’une suite**. Pour $a\in E$, les propriétés suivantes sont équivalentes et signifient que $a$ est une valeur d’adhérence de $(x_n)$ :

1. Une suite extraite de $(x_n)$ converge vers $a$.
2. Pour tout $\varepsilon>0$, l’ensemble $\{n\in\mathbb N:\|x_n-a\|<\varepsilon\}$ est infini.
3. Pour tout $V\in\mathcal V(a)$, l’ensemble $\{n\in\mathbb N:x_n\in V\}$ est infini.

Exemple : $x_{2n}=1$ et $x_{2n+1}=-1$. La sous-suite paire converge vers $1$, l’impaire vers $-1$ ; ces deux nombres sont des valeurs d’adhérence.

## Page 84

**Propriété 36.** Si $x_n\to\ell$, alors $\ell$ est l’unique valeur d’adhérence de $(x_n)$.

Preuve : la suite elle-même est une suite extraite, avec $\phi(n)=n$, donc $\ell$ est valeur d’adhérence. Toute autre suite extraite converge aussi vers $\ell$, d’après la propriété 35.

**Attention : la réciproque est fausse.** Une suite peut n’avoir qu’une valeur d’adhérence et ne pas converger. Exemple :

$$x_{2n}=2n,\qquad x_{2n+1}=1.$$

## Page 85

**Propriété 37 — Caractérisation séquentielle de l’adhérence.** Pour $A\subset E$ et $a\in E$, sont équivalentes :

1. $a\in\overline A$.
2. Il existe une suite d’éléments de $A$ dont $a$ est une valeur d’adhérence.
3. Il existe une suite d’éléments de $A$ convergeant vers $a$.

Preuve de $1\Rightarrow3$ : pour tout $n\ge1$, $B(a,1/n)\cap A\ne\varnothing$. Choisir $x_n$ dans cette intersection. Alors $\|x_n-a\|<1/n$, donc $x_n\to a$.

## Page 86

La propriété 37 est rappelée. Preuve de $3\Rightarrow1$ : soit $(x_n)$ une suite d’éléments de $A$ convergeant vers $a$, et $V$ un voisinage de $a$.

Il existe $N$ tel que $n\ge N\Rightarrow x_n\in V$. Comme $x_n\in A$, on a $x_n\in A\cap V$, donc $A\cap V\ne\varnothing$. Ceci vaut pour tout voisinage $V$ de $a$ ; ainsi $a\in\overline A$.

## Page 87

La propriété 37 est rappelée. Fin de la démonstration :

- $2\Rightarrow3$ : extraire de la suite fournie une sous-suite convergeant vers la valeur d’adhérence $a$ ; elle est encore à valeurs dans $A$.
- $3\Rightarrow2$ : une suite convergeant vers $a$ possède $a$ comme valeur d’adhérence, et même comme unique valeur d’adhérence.

Finalement $1\Longleftrightarrow2\Longleftrightarrow3$.

## Page 88

Exemple pour $A=[-1,1[\times[-1,1]$ : le point $a=(0,1)$ est adhérent à $A$. La suite

$$x_n=\left(0,1-\frac1n\right),\qquad n\ge1,$$

est à valeurs dans $A$ et converge vers $(0,1)$. Le schéma reprend le rectangle dont le bord droit est exclu.

## Page 89

**Propriété 38.**

1. $\overline A$ est l’ensemble des valeurs d’adhérence des suites d’éléments de $A$ ; c’est aussi l’ensemble des limites de toutes les suites convergentes d’éléments de $A$.
2. $A$ est fermé si et seulement si toute suite d’éléments de $A$ convergeant dans $E$ a sa limite dans $A$.

La première assertion est la propriété 37. Pour la seconde : si $A$ est fermé, $\overline A=A$, donc toute limite est dans $A$. Réciproquement, si toutes ces limites sont dans $A$, la caractérisation séquentielle donne $\overline A\subset A$, donc $\overline A=A$.

> La première ligne de preuve imprime « converge vers $A$ » au lieu de « vers $a$ ».

## Page 90

### Chapitre 3 — Limite et continuité d’applications

But du chapitre : généraliser les notions de limite et de continuité des fonctions $\mathbb R\to\mathbb R$ aux fonctions $\mathbb R^p\to\mathbb R^n$.

Plan : introduction ; limite et continuité ; continuité uniforme ; topologie et fonctions continues.

## Page 91

**Rappel préING 1 — Limite.** Pour $f:D\subset\mathbb R\to\mathbb R$, la formulation du support est

$$\forall\varepsilon>0,\ \exists\alpha>0,\ \forall x\in D,\quad |x-a|<\alpha\Longrightarrow|f(x)-\ell|<\varepsilon.$$

On note $\lim_{x\to a}f(x)=\ell$. Le support ajoute : « Si $a$ appartient au domaine de définition de la fonction alors $\lim_{x\to a}f(x)=f(a)$. »

> Convention importante : la définition choisie inclut $x=a$. Si cette limite existe et si $a\in D$, elle vaut donc nécessairement $f(a)$. La seule existence de $f(a)$ ne garantit pas celle d’une limite. Avec la convention usuelle de limite épointée ($0<|x-a|$), il faut ajouter la continuité pour obtenir cette égalité.

## Page 92

**Rappel : limites latérales.** Le support affiche

$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=f(a).$$

Un axe indique les approches à gauche et à droite. Exemple de la fonction de Heaviside :

$$f(x)=\begin{cases}1&x\ge0,\\0&x<0.\end{cases}$$

Le graphe montre les deux demi-droites horizontales aux hauteurs $0$ et $1$.

> L’égalité avec $f(a)$ exige la continuité (ou l’existence de la limite avec la convention non épointée adoptée). Pour Heaviside en $0$, les limites latérales sont différentes : $0$ à gauche, $1$ à droite.

## Page 93

La fonction de Heaviside est représentée à nouveau. Pour un grand $\varepsilon$, la bande verticale de tolérance contient les deux niveaux de la fonction ; pour un petit $\varepsilon$, aucun voisinage de $0$ ne permet de contenir toutes les images dans une bande autour de $f(0)=1$.

Le critère rappelé est

$$\forall\varepsilon>0,\ \exists\alpha>0,\ \forall x\in D,\quad |x-a|<\alpha\Rightarrow|f(x)-\ell|<\varepsilon.$$

Le saut en $0$ empêche donc l’existence de la limite bilatérale.

## Page 94

Exemples motivant les questions « limite ? continuité ? » en plusieurs variables :

$$f(x,y)=\frac{xy}{x^2+y^2},$$

$$g(x,y)=\left(\frac{x^2+y^2-1}{x},\ \frac{\sin(x^2)+\sin(y^2)}{\sqrt{x^2+y^2}}\right).$$

Le support annonce $f:\mathbb R^2\to\mathbb R$ et $g:\mathbb R^2\to\mathbb R^2$, mais ces domaines doivent être restreints : $(x,y)\ne(0,0)$ pour $f$, et $x\ne0$ pour $g$. Aucun prolongement n’est encore défini.

## Page 95

**Définition 1 — Limite d’une fonction en un point.** Soient deux EVN $(E,\|\cdot\|_E)$, $(F,\|\cdot\|_F)$, $A\subset E$, $f:A\to F$, $a\in\overline A$ et $\ell\in F$. Les deux formulations équivalentes définissent la limite $\ell$ en $a$ :

$$\forall\varepsilon>0,\ \exists\eta>0,\ \forall x\in A,\quad \|x-a\|_E<\eta\Longrightarrow\|f(x)-\ell\|_F<\varepsilon,$$

$$\forall\varepsilon>0,\ \exists\eta>0,\ \forall x\in A,\quad x\in B_E(a,\eta)\Longrightarrow f(x)\in B_F(\ell,\varepsilon).$$

Le schéma associe une petite boule autour de $a$ dans le domaine à une boule autour de $\ell$ dans le codomaine. La convention inclut le point $a$ lorsqu’il appartient à $A$.

## Page 96

Le support rappelle que si $f$ est définie en $a$, sa limite, **si elle existe selon la définition précédente**, vaut $f(a)$.

Exemple : $f(x,y)=xy/(x^2+y^2)$.

- En $a=(1,1)$, $f(a)=1/2$ et $\lim_{(x,y)\to(1,1)}f(x,y)=1/2$.
- En $a=(0,0)$, le quotient donne une forme indéterminée $0/0$ : quelles techniques utiliser ?

> La première phrase imprimée omet la condition d’existence de la limite. Dans le premier exemple, la continuité du quotient sur son domaine justifie bien la limite.

## Page 97

**Propriété 1 — Unicité de la limite.** Avec les hypothèses de la définition 1, si $f$ admet une limite en $a$, elle est unique.

Supposer deux limites $\ell\ne\ell'$ et poser $\varepsilon=\frac13\|\ell-\ell'\|_F>0$. Il existe $\eta,\eta'>0$ tels que, pour $x\in A$ assez proche de $a$,

$$\|f(x)-\ell\|_F<\varepsilon,\qquad\|f(x)-\ell'\|_F<\varepsilon.$$

Comme $a\in\overline A$, choisir $x\in A$ avec $\|x-a\|_E<\min(\eta,\eta')$. Alors

$$3\varepsilon=\|\ell-\ell'\|_F\le\|\ell-f(x)\|_F+\|f(x)-\ell'\|_F<2\varepsilon,$$

contradiction.

## Page 98

Reprise de $f(x,y)=xy/(x^2+y^2)$. Une représentation tridimensionnelle montre une surface variant selon la direction d’approche de l’origine.

Le schéma du plan illustre plusieurs chemins vers $a=(0,0)$ : des demi-droites d’inclinaisons différentes et une courbe. Il prépare l’étude de la limite le long de chemins distincts.

## Page 99

**Coordonnées polaires.** Les définitions géométriques de sinus et cosinus donnent

$$x=\rho\cos\theta,\qquad y=\rho\sin\theta,\qquad \rho>0,\quad\theta\in[0,2\pi[.$$

Le point $M=(x,y)$ se situe à distance $\rho$ de l’origine, sous l’angle $\theta$. Pour l’exemple,

$$f(x,y)=\frac{xy}{x^2+y^2}=\cos\theta\sin\theta.$$

Le long de $\theta=\pi/4$, la valeur est $1/2$ ; le long de $\theta=-\pi/4$ (ou $7\pi/4$), elle est $-1/2$. Les deux limites de restrictions diffèrent : **la limite en $(0,0)$ n’existe pas**.

> La source écrit abusivement deux fois la limite générale de $f$ ; ce sont bien deux limites le long de chemins particuliers.

## Page 100

**Propriété 2 — Normes équivalentes.** Remplacer les normes de $E$ et $F$ par des normes équivalentes ne change ni l’existence ni la valeur de la limite. Démonstration : voir le polycopié.

Dans

$$\forall\varepsilon>0,\ \exists\eta>0,\ \forall x\in A,\quad\|x-a\|_E<\eta\Rightarrow\|f(x)-\ell\|_F<\varepsilon,$$

le changement de normes ne modifie que le choix de $\eta$ en fonction de $\varepsilon$.

## Page 101

**Propriété 3 — Combinaisons linéaires.** Si $f,g:A\subset E\to F$ ont respectivement pour limites $\ell_1,\ell_2$ en $a\in\overline A$, alors, pour $\lambda\in\mathbb R$,

$$\lim_{x\to a}(f(x)+\lambda g(x))=\ell_1+\lambda\ell_2.$$

Pour $\varepsilon>0$ et $\lambda\ne0$, choisir $\eta,\eta'>0$ tels que $\|x-a\|_E<\eta$ entraîne $\|f(x)-\ell_1\|_F<\varepsilon/2$, et $\|x-a\|_E<\eta'$ entraîne $\|g(x)-\ell_2\|_F<\varepsilon/(2|\lambda|)$. Pour $\eta_0=\min(\eta,\eta')$, on a

$$\|x-a\|_E<\eta_0\Rightarrow\|f(x)+\lambda g(x)-(\ell_1+\lambda\ell_2)\|_F\le\|f(x)-\ell_1\|_F+|\lambda|\|g(x)-\ell_2\|_F<\varepsilon.$$

Le cas $\lambda=0$ est immédiat.

## Page 102

**Propriété 4 — Produits et quotients de fonctions réelles.** Si $f,g:A\to\mathbb R$ ont pour limites $\ell_1,\ell_2$ en $a$, alors

$$\lim_{x\to a}f(x)g(x)=\ell_1\ell_2.$$

Si $\ell_2\ne0$, le quotient est défini au voisinage de $a$ dans $A$ et

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{\ell_1}{\ell_2}.$$

Démonstration laissée en exercice.

## Page 103

**Applications composantes.** Une application $f:\mathbb R^n\to\mathbb R^p$ s’écrit

$$f(x_1,\ldots,x_n)=\bigl(f_1(x_1,\ldots,x_n),\ldots,f_p(x_1,\ldots,x_n)\bigr),$$

où les $f_i$ vont de $\mathbb R^n$ dans $\mathbb R$.

Exemple : $f:\mathbb R^2\to\mathbb R^3$, $f(x,y)=(x^2+y^2,x-y,y^3)$. Ses trois composantes sont $f_1(x,y)=x^2+y^2$, $f_2(x,y)=x-y$ et $f_3(x,y)=y^3$. La source alterne les noms de coordonnées $(x_1,x_2)$ et $(x,y)$.

## Page 104

La décomposition $f=(f_1,\ldots,f_p)$ est rappelée.

**Propriété 5 — Limite composante par composante.** Pour $f:\mathbb R^n\to\mathbb R^p$ et $\ell=(\ell_1,\ldots,\ell_p)$, $f(x)\to\ell$ en $a$ si et seulement si chaque composante $f_i(x)\to\ell_i$. Démonstration laissée en exercice.

## Page 105

Exemple vectoriel :

$$f(x,y)=\left(\frac{xy^2}{x^2+y^2},\frac{xy}{x^2+y^2}\right),\qquad(x,y)\ne(0,0).$$

Pour étudier la limite en $(0,0)$, examiner les deux composantes. En polaires :

$$f_1(\rho\cos\theta,\rho\sin\theta)=\rho\cos\theta\sin^2\theta\longrightarrow0,$$

uniformément en $\theta$, puisque sa valeur absolue est majorée par $\rho$. En revanche,

$$f_2(\rho\cos\theta,\rho\sin\theta)=\cos\theta\sin\theta$$

dépend de la direction : cette composante n’a pas de limite générale à l’origine. Donc $f$ n’en a pas non plus.

## Page 106

**Définition 2 — Application continue.** Pour $f:A\subset E\to F$ et $a\in A$, $f$ est continue en $a$ si elle admet une limite en $a$, suivant la convention non épointée adoptée ici ; cette limite vaut $f(a)$. Elle est discontinue si elle n’est pas continue.

Elle est continue sur $A$ si elle est continue en tout point de $A$. L’ensemble des applications continues de $A$ dans $F$ se note $\mathcal C(A,F)$.

Les dessins comparent les deux approches latérales en dimension 1 aux nombreux chemins d’approche possibles dans $\mathbb R^2$.

## Page 107

**Théorème 1 — Caractérisation séquentielle de la limite.** Pour $f:A\subset E\to F$, $a\in\overline A$ et $\ell\in F$, on a $\lim_{x\to a}f(x)=\ell$ si et seulement si, pour **toute** suite $(x_n)$ d’éléments de $A$ convergeant vers $a$, $f(x_n)\to\ell$. Démonstration admise.

**Corollaire — Caractérisation séquentielle de la continuité.** Pour $a\in A$, $f$ est continue en $a$ si et seulement si $x_n\to a$, avec $x_n\in A$, entraîne $f(x_n)\to f(a)$ pour toute suite.

> L’énoncé imprimé du corollaire écrit $a\in\overline A$ ; comme il utilise $f(a)$, il faut $a\in A$.

## Page 108

Exemple :

$$f(x,y)=\begin{cases}\dfrac{xy}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$

Prendre $u_n=(1/n,1/n)$, $n\ge1$. Alors $u_n\to(0,0)$, mais

$$f(u_n)=\frac{1/n^2}{2/n^2}=\frac12\longrightarrow\frac12\ne f(0,0)=0.$$

Ainsi $f$ n’est pas continue en $(0,0)$. La source écrit $n^2/(2n^2)$ dans le quotient intermédiaire ; la valeur $1/2$ reste correcte.

## Page 109

**Méthodologie — Calculer une limite en $a=(x_0,y_0)$.**

1. Calculer l’expression au point. Si les opérations et fonctions qui la composent y sont continues et bien définies, la limite est $f(x_0,y_0)$.
2. En présence d’une indétermination, étudier l’approche du point : soit toutes les approches conduisent à une même valeur, soit on exhibe deux chemins conduisant à des valeurs différentes.

> La source présente l’absence de forme indéterminée comme suffisante sans mentionner la continuité des expressions utilisées ; cette hypothèse est nécessaire, notamment pour une fonction définie par morceaux.

## Page 110

**Méthode 1 — Coordonnées polaires centrées en $a$.** Quand la forme de l’expression s’y prête, poser

$$x=x_0+\rho\cos\theta,\qquad y=y_0+\rho\sin\theta,\qquad \widetilde f(\rho,\theta)=f(x,y).$$

Étudier $\widetilde f$ quand $\rho\to0$. Si deux angles fixes donnent deux limites différentes, la limite en $a$ n’existe pas.

> Correction d’une insuffisance du support : celui-ci affirme que si le résultat ne dépend pas de $\theta$, la limite existe. L’existence d’une même limite pour chaque angle fixé ne suffit pas en général. Pour conclure, il faut contrôler aussi les angles variables, par exemple par une majoration $|\widetilde f(\rho,\theta)-\ell|\le h(\rho)$ indépendante de $\theta$, avec $h(\rho)\to0$.

## Page 111

**Méthode 2 — Chemins d’approche, lorsque les polaires ne sont pas adaptées.**

(a) **Caractérisation séquentielle.** Prendre diverses suites $u_n\to(x_0,y_0)$ et calculer $\lim f(u_n)$. Si la limite générale existe, toutes ces limites doivent lui être égales.

(b) **Chemins cartésiens.** Décrire des chemins par exemple sous la forme $(x,\alpha(x))$, où $\alpha:\mathbb R\to\mathbb R$, et restreindre $f$ à ces chemins.

Deux limites différentes prouvent l’absence de limite. Si les chemins testés donnent tous la même valeur $\ell_c$, celle-ci est seulement un **candidat** ; passer à l’étape 3 pour conclure.

## Page 112

**Étape 3 — Vérification du candidat.** Étudier $|f(x,y)-\ell_c|$.

Si cette quantité tend vers $0$ lorsque $(x,y)\to(x_0,y_0)$, alors $f(x,y)\to\ell_c$. Si l’on démontre qu’elle ne tend pas vers $0$, le candidat est exclu ; lorsqu’il était imposé par un chemin déjà testé, aucune limite n’existe.

Deux exemples illustreront la méthode : l’un admet une limite en $(0,0)$, l’autre non.

## Page 113

**Exemple 1 : $f_1(x,y)=xy/(x^2+y^2)$.** Comparaison des trois méthodes à l’origine.

- **Polaires :** $\widetilde f_1(\rho,\theta)=\cos\theta\sin\theta$. Pour $\theta=\pi/4$, la limite vaut $1/2$ ; pour $\theta=\pi/2$, elle vaut $0$.
- **Suites :** $u_n=(1/n,1/n)$ et $v_n=(0,1/n)$ tendent vers $(0,0)$, mais $f_1(u_n)=1/2$ et $f_1(v_n)=0$.
- **Chemins cartésiens :** $f_1(x,x)=1/2$ pour $x\ne0$, et $f_1(0,y)=0$ pour $y\ne0$.

Le schéma représente la diagonale $y=x$ et l’axe vertical. Conclusion : **pas de limite en $(0,0)$**.

## Page 114

**Exemple 2 : $f_2(x,y)=1+x^3/(x^2+y^2)$.**

- **Polaires :** $\widetilde f_2(\rho,\theta)=1+\rho\cos^3\theta\to1$. Ici $|\rho\cos^3\theta|\le\rho$ assure une convergence indépendante de l’angle.
- **Suites :** $u_n=(1/n,1/n)$ et $v_n=(1/n,0)$ donnent tous deux $f_2(u_n)\to1$, $f_2(v_n)\to1$ ; ces deux tests seuls ne suffisent pas à conclure.
- **Chemins :** les restrictions à $(x,x)$ et $(x,0)$ ont toutes deux pour limite $1$ ; ces tests seuls ne suffisent pas non plus.

La conclusion « continue » imprimée dans la colonne polaire signifie qu’un prolongement continu par $f_2(0,0)=1$ est possible.

Vérification directe du candidat $\ell_c=1$ :

$$|f_2(x,y)-1|=\left|\frac{x^3}{x^2+y^2}\right|=\frac{x^2}{x^2+y^2}|x|\le|x|\longrightarrow0.$$

Donc $\lim_{(x,y)\to(0,0)}f_2(x,y)=1$.

## Page 115

### Chapitre 4 — Calcul différentiel du premier ordre

Objectif : généraliser les notions étudiées pour les applications de $\mathbb R$ dans $\mathbb R$.

1. Dérivée première $f'(x)$ → dérivées partielles $\partial_xf(x,y)$, $\partial_yf(x,y)$.
2. Différentiabilité, différentielle, classe $\mathcal C^1$. La forme $f(a+h)=f(a)+D_af(h)+o(h)$ reste le modèle. En une variable, $D_af(h)=f'(a)h$ ; en plusieurs variables,

$$D_af(h)=\sum_{i=1}^nh_i\frac{\partial f}{\partial x_i}(a).$$

3. Équations différentielles d’ordre 1 → équations aux dérivées partielles du premier ordre. Exemple :

$$\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}=\frac\rho{\varepsilon_0}.$$

> Dans le développement en plusieurs variables, le reste s’entend comme $o(\|h\|)$.

## Page 116

**À quoi sert la dérivée en une variable ?** Un graphe de $\omega$ indique $x$, $x+dx$, $\omega(x)$ et $\omega(x+dx)$, puis rappelle

$$\omega'(x)=\frac{d\omega}{dx}=\lim_{dx\to0}\frac{\omega(x+dx)-\omega(x)}{dx}.$$

La dérivée décrit la variation locale de la fonction au point $x$.

## Page 117

Pour une fonction de deux variables, on peut étudier les variations dans les directions $x$ et $y$ séparément. Exemple représenté par un paraboloïde rouge :

$$f(x,y)=(x-2)^2+(y-2{,}5)^2.$$

## Page 118

Pour une fonction de deux variables, on peut étudier les variations dans les directions $x$ et $y$ séparément. Exemple représenté par un paraboloïde rouge :

$$f(x,y)=(x-2)^2+(y-2{,}5)^2.$$

Un second dessin coupe ce paraboloïde par le plan vertical bleu $y=0{,}5$. La courbe d’intersection représente la variation selon $x$ lorsque $y$ est fixé.

## Page 119

Le plan $y=0{,}5$ et sa section du paraboloïde $f(x,y)=(x-2)^2+(y-2{,}5)^2$ sont repris. À côté, le graphe plan de $x\mapsto f(x,0{,}5)$ montre une parabole de sommet $(2,4)$.

C’est une fonction d’une variable, que l’on peut dériver par les règles habituelles.

## Page 120

La section $x\mapsto f(x,0{,}5)$ illustre la dérivée partielle par rapport à $x$, calculée à $y$ constant :

$$\frac{\partial f}{\partial x}(x,y)=\lim_{t\to0}\frac{f(x+t,y)-f(x,y)}t.$$

La notation désigne la dérivée de $f$ selon $x$, évaluée au point $(x,y)$.

## Page 121

Avec $a=(x,y)$ et $(e_1,e_2)$ la base canonique de $\mathbb R^2$, les deux directions donnent :

$$\frac{\partial f}{\partial x}(x,y)=\lim_{t\to0}\frac{f(x+t,y)-f(x,y)}t=\lim_{t\to0}\frac{f(a+te_1)-f(a)}t,$$

$$\frac{\partial f}{\partial y}(x,y)=\lim_{t\to0}\frac{f(x,y+t)-f(x,y)}t=\lim_{t\to0}\frac{f(a+te_2)-f(a)}t.$$

Dans le premier cas on fixe $y$, dans le second on fixe $x$.

## Page 122

### Dérivées partielles du premier ordre

**Définition 1.** Soit $U$ un ouvert de $\mathbb R^p$, $a\in U$ et $f:U\to\mathbb R$. Noter $(e_1,\ldots,e_p)$ la base canonique. La dérivée partielle première en $a$ selon la $j$e variable existe si

$$\phi_j:D_j\to\mathbb R,\qquad\phi_j(t)=f(a+te_j),\qquad D_j=\{t\in\mathbb R:a+te_j\in U\}$$

est dérivable en $0$. Alors

$$\frac{\partial f}{\partial x_j}(a)=\phi_j'(0)=\lim_{t\to0}\frac{f(a+te_j)-f(a)}t.$$

Notations présentées : $\left.\frac{\partial f}{\partial x_j}\right|_a$, $\frac{\partial f(a)}{\partial x_j}$ et $\frac{\partial f}{\partial x_j}(a)$ ; toutes indiquent une dérivée évaluée au point $a$.

## Page 123

Exemple : $f:\mathbb R^2\to\mathbb R$, $f(x,y)=3x^2+xy-2y^2$.

$$\begin{aligned}
\partial_xf(x,y)&=\lim_{t\to0}\frac{f(x+t,y)-f(x,y)}t\\
&=\lim_{t\to0}\frac{3(x+t)^2+(x+t)y-2y^2-3x^2-xy+2y^2}{t}\\
&=\lim_{t\to0}\frac{3t^2+6xt+ty}{t}=\lim_{t\to0}(3t+6x+y)=6x+y.
\end{aligned}$$

Cela revient bien à fixer $y$ et à dériver par rapport à $x$.

## Page 124

**Signification graphique.** $\partial_x f(x_0,y_0)$ est la dérivée en $x_0$ de la fonction d’une variable $x\mapsto f(x,y_0)$.

Le schéma montre la surface $z=f(x,y)$ coupée par le plan $y=y_0$, parallèle au plan $xOz$. L’intersection fournit la courbe de $f(x,y_0)$ ; la dérivée partielle est la pente de sa tangente au point d’abscisse $x_0$.

## Page 125

**Calcul pratique des dérivées partielles.** Comme pour les fonctions d’une variable, on emploie généralement les dérivées usuelles et les règles de calcul, par exemple $(uv)'=u'v+v'u$.

Dériver par rapport à une variable revient à fixer toutes les autres. On revient à la définition, notamment, aux points de prolongement par continuité ou de changement d’expression d’une fonction définie par morceaux.

## Page 126

Exemple proposé :

$$f(x,y)=\frac{xy^3}{x^2+y^2}.$$

Cette diapositive ne comporte pas de calcul de dérivées ni de valeur prescrite à l’origine.

## Page 127

**Propriété 1 — Dérivation composante par composante.** Pour $f=(f_1,\ldots,f_n):U\subset\mathbb R^p\to\mathbb R^n$, $\partial_{x_j}f(a)$ existe si et seulement si toutes les $\partial_{x_j}f_i(a)$ existent. Alors

$$\partial_{x_j}f(a)=\bigl(\partial_{x_j}f_1(a),\ldots,\partial_{x_j}f_n(a)\bigr).$$

Preuve : écrire

$$\frac{f(a+te_j)-f(a)}t=\left(\frac{f_1(a+te_j)-f_1(a)}t,\ldots,\frac{f_n(a+te_j)-f_n(a)}t\right)$$

et passer à la limite coordonnée par coordonnée.

## Page 128

### Fonctions différentiables

**Définition 2.** Soient $U\subset\mathbb R^p$ ouvert, $a\in U$, $f:U\to F$ et $U_0=\{h\in\mathbb R^p:a+h\in U\}$.

$f$ est différentiable en $a$ s’il existe une application **linéaire** $L:\mathbb R^p\to F$ et une application $\varepsilon:U_0\to F$ telles que

$$\lim_{h\to0}\varepsilon(h)=0_F,\qquad f(a+h)=f(a)+L(h)+\|h\|\varepsilon(h).$$

La seconde relation est le développement limité d’ordre 1 de $f$ en $a$. $f$ est différentiable sur $U$ si elle l’est en chaque point de $U$. La lettre $L$ correspond au $l$ imprimé dans le support.

## Page 129

**Théorème 1 — Différentielle.** Si $f$ est différentiable en $a$, l’application linéaire $L$ de

$$f(a+h)=f(a)+L(h)+\|h\|\varepsilon(h),\qquad\varepsilon(h)\to0_F$$

est unique. Elle est appelée différentielle de $f$ en $a$, et notée $D_af$.

Démonstration renvoyée au polycopié.

## Page 130

**Propriété 2.** Toute application linéaire $\phi:\mathbb R^p\to F$ est différentiable et $D_a\phi=\phi$ pour tout $a$.

En effet, la linéarité donne $\phi(a+h)=\phi(a)+\phi(h)+0_F$. Prendre $D_a\phi=\phi$ et $\varepsilon(h)=0_F$.

## Page 131

**Propriété 3.** Si $f:U\subset\mathbb R^p\to F$ est différentiable en $a$, toutes ses dérivées partielles premières existent en $a$, et

$$D_af(h)=\sum_{j=1}^p h_j\partial_{x_j}f(a),\qquad h=(h_1,\ldots,h_p).$$

Démonstration : voir le polycopié.

## Page 132

**Propriété 4.** La différentiabilité en $a$ entraîne la continuité en $a$.

La formule de la différentielle donne, pour $h\to0$,

$$\begin{aligned}
\|f(a+h)-f(a)\|_F
&=\left\|\sum_{j=1}^p h_j\partial_{x_j}f(a)+\|h\|_E\varepsilon(h)\right\|_F\\
&\le\sum_{j=1}^p|h_j|\,\|\partial_{x_j}f(a)\|_F+\|h\|_E\|\varepsilon(h)\|_F\longrightarrow0.
\end{aligned}$$

Donc $f(a+h)\to f(a)$. La limite de la norme est le réel $0$ ; le support la note ici $0_F$.

## Page 133

**Théorème 2 — Critère de différentiabilité sur $\mathbb R^2$.** Pour $f:U\subset\mathbb R^2\to F$ et $a=(x,y)\in U$, avec dérivées partielles en $a$, la différentiabilité équivaut à

$$\lim_{(h_1,h_2)\to(0,0)}\frac{f(x+h_1,y+h_2)-f(x,y)-h_1\partial_xf(x,y)-h_2\partial_yf(x,y)}{\|(h_1,h_2)\|}=0_F.\tag{1}$$

La norme choisie dans $\mathbb R^2$ n’influe pas sur le résultat.

Sens direct : le développement différentiel s’écrit

$$f(x+h_1,y+h_2)=f(x,y)+h_1\partial_xf(x,y)+h_2\partial_yf(x,y)+\|(h_1,h_2)\|\varepsilon(h_1,h_2).$$

Le quotient de (1) est donc $\varepsilon(h_1,h_2)\to0_F$.

## Page 134

Le critère de la page précédente est rappelé. Sens réciproque : définir, pour $h\ne0$,

$$\varepsilon(h_1,h_2)=\frac{f(x+h_1,y+h_2)-f(x,y)-h_1\partial_xf(x,y)-h_2\partial_yf(x,y)}{\|(h_1,h_2)\|},$$

et poser $\varepsilon(0,0)=0_F$. Par hypothèse, $\varepsilon(h)\to0_F$. Réarranger les termes fournit le développement de la définition, avec l’application linéaire $h\mapsto h_1\partial_xf(x,y)+h_2\partial_yf(x,y)$. Donc $f$ est différentiable.

## Page 135

**Interprétation de la différentielle.** $D_af(h)$ représente la variation de $f$ au premier ordre lors d’un déplacement $h$ à partir de $a$ :

$$f(a+h)=f(a)+D_af(h)+\|h\|\varepsilon(h),\qquad\varepsilon(h)\to0.$$

Pour une fonction $f:\mathbb R^2\to\mathbb R$, le plan tangent en $A=(a,f(a))$ est

$$T_A=\{(a+h,f(a)+D_af(h)):h\in\mathbb R^2\}.$$

Le dessin montre $z=x^2+y^2$ et son plan tangent $z=2x+2y-2$ au point $A=(1,1,2)$.

## Page 136

**Définition 3 — Classe $\mathcal C^1$.** Une application $f:U\subset\mathbb R^p\to F$ est de classe $\mathcal C^1$ si toutes ses dérivées partielles premières sont définies et continues sur $U$. On note $\mathcal C^1(U,F)$ l’ensemble de ces applications.

**Propriété 5.** Toute application linéaire $\phi:\mathbb R^p\to F$ est $\mathcal C^1$. Pour tout $a$,

$$\partial_{x_i}\phi(a)=\lim_{t\to0}\frac{\phi(a+te_i)-\phi(a)}t=\phi(e_i).$$

Les dérivées partielles sont donc constantes, et par conséquent continues.

## Page 137

**Théorème 3.** Si $f$ est de classe $\mathcal C^1$ sur un ouvert $U\subset\mathbb R^p$, alors :

1. $f$ est différentiable sur $U$ ;
2. $f$ est continue sur $U$.

Le point 1 est admis ; le point 2 résulte de « différentiable $\Rightarrow$ continue ».

Le diagramme récapitule : $\mathcal C^1\Rightarrow$ différentiable, puis deux conséquences de la différentiabilité en un point : continuité et existence de toutes les dérivées partielles.

## Page 138

Illustration :

$$f(x,y)=\begin{cases}(x^2+y^2)\sin\!\dfrac1{\sqrt{x^2+y^2}},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$

Continuité en $(0,0)$ :

$$|f(x,y)|\le x^2+y^2\longrightarrow0=f(0,0).$$

Hors de l’origine, $f$ est une composée de fonctions continues ; elle est donc continue sur $\mathbb R^2$.

## Page 139

Différentiabilité de la même fonction à l’origine. D’abord,

$$\partial_xf(0,0)=\lim_{t\to0}\frac{t^2\sin(1/|t|)}t=\lim_{t\to0}t\sin(1/|t|)=0,$$

et de même $\partial_yf(0,0)=0$. Le reste normalisé vaut

$$\frac{(h_1^2+h_2^2)\sin\bigl(1/\sqrt{h_1^2+h_2^2}\bigr)}{\sqrt{h_1^2+h_2^2}}\longrightarrow0.$$

Donc $f$ est différentiable en $(0,0)$, de différentielle nulle.

## Page 140

Les dérivées partielles de cette fonction ne sont toutefois pas continues à l’origine : $f$ n’est pas $\mathcal C^1$.

**Calcul imprimé dans la source :** hors de l’origine, elle donne

$$\partial_xf(x,y)=2x\sin\!\frac1{\sqrt{x^2+y^2}}-\frac{x}{(x^2+y^2)^{3/2}}\cos\!\frac1{\sqrt{x^2+y^2}},$$

puis, pour $u_n=(1/n,0)$, $\frac2n\sin n-n^2\cos n$, et à la ligne suivante $\frac{\sin n}{n}-n^2\cos n$. Elle conclut à la non-continuité de la dérivée.

> Correction : le second terme du produit a perdu le facteur $x^2+y^2$, et un facteur $2$ disparaît ensuite. La dérivée correcte est
>
> $$\partial_xf(x,y)=2x\sin(1/r)-\frac{x}{r}\cos(1/r),\qquad r=\sqrt{x^2+y^2},$$
>
> avec $\partial_xf(0,0)=0$. Sur $u_n=(1/n,0)$, elle vaut $2\sin n/n-\cos n$, qui ne tend pas vers $0$. Pour une démonstration immédiate, sur $v_n=(1/(2\pi n),0)$ elle vaut exactement $-1$. La conclusion de la source reste juste.

Bilan en $(0,0)$ : $f$ est continue et différentiable ; ses dérivées partielles existent, mais ne sont pas continues.

## Page 141

**Propriété 5.** Toute application linéaire $\phi:\mathbb R^p\to F$ est $\mathcal C^1$. Pour tout $a$,

$$\partial_{x_i}\phi(a)=\lim_{t\to0}\frac{\phi(a+te_i)-\phi(a)}t=\phi(e_i).$$

Les dérivées partielles sont donc constantes, et par conséquent continues.

## Page 142

**Théorème 4.** Pour un ouvert $U\subset\mathbb R^p$ et un EVN $F$, $\mathcal C^1(U,F)$ est un sous-espace vectoriel de $\mathcal C(U,F)$.

Preuve :

1. La fonction nulle a toutes ses dérivées partielles nulles, donc continues ; elle appartient à $\mathcal C^1(U,F)$.
2. Si $f,g\in\mathcal C^1(U,F)$ et $\lambda\in\mathbb R$, alors $f+\lambda g$ est continue et ses dérivées partielles, sommes des dérivées correspondantes, sont continues. Ainsi $f+\lambda g\in\mathcal C^1(U,F)$.

## Page 143

**Théorème 5.** Le produit de deux fonctions réelles de classe $\mathcal C^1$ sur $U$ est de classe $\mathcal C^1$. Preuve laissée en exercice.

> L’énoncé source dit « $F$ un EVN quelconque » puis écrit $f\times g$. Un EVN quelconque ne possède pas de produit interne défini ; l’énoncé usuel vaut pour $F=\mathbb R$, ou pour un produit bilinéaire continu précisé.

**Théorème 6 — Composition.** Si $U\subset\mathbb R^p$ et $V\subset\mathbb R^q$ sont ouverts, $f:U\to\mathbb R^q$ est $\mathcal C^1$, $g:V\to\mathbb R^n$ est $\mathcal C^1$ et $f(U)\subset V$, alors $g\circ f$ est $\mathcal C^1$ sur $U$. Démonstration admise.

## Page 144

**Paramétrisation d’un chemin et dérivée le long de ce chemin.** Illustration : un vol Paris–Washington. La carte indique Paris (CDG), Washington D.C. (IAD), environ $6175$ km, $8$ h $15$ min, un Boeing 777-200ER et une altitude de croisière d’environ $11000$ m ($36000$ ft).

La trajectoire est $\gamma(t)=(x(t),y(t),z(t))$. Le champ de température est $\theta(x,y,z)$, supposé stationnaire (le mot « constante » du support signifie ici indépendant du temps, puisqu’il varie dans l’espace).

Contrainte donnée : la variation de température ne doit pas dépasser $5\ \mathrm K/\text{minute}$. Comment calculer cette variation ? Il s’agit de dériver $\theta$ le long de la trajectoire.

## Page 145

La carte du vol est reprise. **Méthode explicite :**

$$\gamma(t)=\left(1000t,\ 2000\sin\frac{\pi t}{6},\ 10000(1-e^{-3t})(1-e^{-3(6-t)})\right).$$

Le champ de température choisi est

$$\theta(x,y,z)=15-\frac{6{,}5}{1000}z+\frac{x}{6000}+\frac{y}{800}.$$

Le support ne précise pas ici les unités de la variable $t$.

## Page 146

**Méthode explicite :**

$$\gamma(t)=\left(1000t,\ 2000\sin\frac{\pi t}{6},\ 10000(1-e^{-3t})(1-e^{-3(6-t)})\right).$$

Le champ de température choisi est

$$\theta(x,y,z)=15-\frac{6{,}5}{1000}z+\frac{x}{6000}+\frac{y}{800}.$$

La température ressentie à l’instant $t$ est

$$T(t)=\theta(\gamma(t))=15-65(1-e^{-3t})(1-e^{-18+3t})+\frac t6+\frac52\sin\frac{\pi t}{6}.$$

Par dérivation usuelle :

$$T'(t)=-195\left[e^{-3t}(1-e^{-18+3t})-e^{-18+3t}(1-e^{-3t})\right]+\frac16+\frac{5\pi}{12}\cos\frac{\pi t}{6}.$$

## Page 147

Diapositive de transition : « Mais on peut aussi faire le calcul de la façon suivante ». Aucun calcul supplémentaire n’est affiché.

## Page 148

**Propriété 6 — Dérivée d’une composée dépendant d’un paramètre.** Soit $f:U\subset\mathbb R^n\to\mathbb R$ de classe $\mathcal C^1$, et $u_1,\ldots,u_n$ des fonctions $\mathcal C^1$ sur un intervalle $I$, avec $u(t)=(u_1(t),\ldots,u_n(t))\in U$.

Alors $g(t)=f(u_1(t),\ldots,u_n(t))$ est $\mathcal C^1$ et

$$g'(t)=\sum_{j=1}^n u_j'(t)\partial_{x_j}f(u_1(t),\ldots,u_n(t)).$$

Démonstration renvoyée au polycopié.

## Page 149

**Propriété 7 — Composée à deux variables.** Soient $U,V\subset\mathbb R^2$ ouverts, $f:U\to\mathbb R$ et $g_1,g_2:V\to\mathbb R$ de classe $\mathcal C^1$, avec $(g_1(u,v),g_2(u,v))\in U$. Alors

$$h(u,v)=f(g_1(u,v),g_2(u,v))$$

est $\mathcal C^1$ et, en notant $g=(g_1,g_2)$,

$$\partial_uh(u,v)=\partial_xf(g(u,v))\partial_ug_1(u,v)+\partial_yf(g(u,v))\partial_ug_2(u,v),$$

$$\partial_vh(u,v)=\partial_xf(g(u,v))\partial_vg_1(u,v)+\partial_yf(g(u,v))\partial_vg_2(u,v).$$

Preuve de la première égalité : fixer $v$ et poser $g_1^v(u)=g_1(u,v)$, $g_2^v(u)=g_2(u,v)$, $H(u)=h(u,v)=f(g_1^v(u),g_2^v(u))$. Alors $\partial_uh(u,v)=H'(u)$. La seconde égalité se démontre de la même façon.

## Page 150

La propriété 7 est rappelée. Appliquer la règle de chaîne à

$$H(u)=f(g_1^v(u),g_2^v(u))$$

donne

$$H'(u)=\partial_xf(g_1^v(u),g_2^v(u))(g_1^v)'(u)+\partial_yf(g_1^v(u),g_2^v(u))(g_2^v)'(u).$$

Comme $(g_1^v)'(u)=\partial_ug_1(u,v)$ et $(g_2^v)'(u)=\partial_ug_2(u,v)$, on obtient

$$\partial_uh(u,v)=\partial_xf(g(u,v))\partial_ug_1(u,v)+\partial_yf(g(u,v))\partial_ug_2(u,v).$$

## Page 151

Exemple : $f(x,y)=2x^2y+y^2+x$, avec $x=g_1(u,v)=u+v$ et $y=g_2(u,v)=u-v$. On pose $h=f\circ g$.

**Méthode 1 — Calcul explicite :**

$$\begin{aligned}
h(u,v)&=2(u+v)^2(u-v)+(u-v)^2+u+v\\
&=2u^3-2v^3+2u^2v-2uv^2+u^2+v^2-2uv+u+v.
\end{aligned}$$

D’où

$$\partial_uh=6u^2-2v^2+2u-2v+4uv+1,$$

$$\partial_vh=2u^2-6v^2+1-2u+2v-4uv.$$

## Page 152

Même exemple, **méthode 2 — Règle de chaîne.** Puisque $\partial_xf=4xy+1$ et $\partial_yf=2x^2+2y$,

$$\partial_uh=(4xy+1)\times1+(2x^2+2y)\times1,$$

$$\partial_vh=(4xy+1)\times1+(2x^2+2y)\times(-1).$$

Remplacer $x=u+v$, $y=u-v$ redonne

$$\partial_uh=6u^2-2v^2+2u-2v+4uv+1,\qquad\partial_vh=2u^2-6v^2+1-2u+2v-4uv.$$

## Page 153

**Définition 4 — Matrice de Jacobi.** Pour $f:U\subset\mathbb R^p\to\mathbb R^n$ différentiable en $a$, la matrice jacobienne $J_f(a)$ est la matrice de $D_af$ dans les bases canoniques. Elle possède $n$ lignes et $p$ colonnes :

$$J_f(a)=\left(\partial_{x_j}f_i(a)\right)_{1\le i\le n,\,1\le j\le p}.$$

Si $n=p$, son déterminant s’appelle le jacobien de $f$ en $a$.

Exemple : $f(x,y,z)=(xyz,ye^x,ze^z)$ est $\mathcal C^1$ sur $\mathbb R^3$ et

$$J_f(x,y,z)=\begin{pmatrix}yz&xz&xy\\ye^x&e^x&0\\0&0&(1+z)e^z\end{pmatrix},$$

$$\det J_f(x,y,z)=yz(1+z)(1-x)e^{x+z}.$$

## Page 154

**Définition 5 — Gradient.** Pour une application réelle $f:U\subset\mathbb R^p\to\mathbb R$ différentiable en $a$,

$$\nabla_af={}^tJ_f(a)=\begin{pmatrix}\partial_{x_1}f(a)\\\vdots\\\partial_{x_p}f(a)\end{pmatrix}.$$

Il se note aussi $\overrightarrow{\operatorname{grad}}(f)(a)$.

Exemple : $f(x,y,z)=xyz+ye^x+z^2$ est $\mathcal C^1$ et

$$\nabla f(x,y,z)=\begin{pmatrix}yz+ye^x\\xz+e^x\\xy+2z\end{pmatrix}.$$

## Page 155

**Propriété 8 — Gradient et différentielle.** Pour une fonction réelle différentiable en $a$,

$$D_af(h)=\nabla_af\cdot h=\sum_{i=1}^ph_i\partial_{x_i}f(a).$$

Le point $a$ appartient à $U$ et le vecteur $h$ à $\mathbb R^p$ ; la source écrit inutilement $(a,h)\in U^2$.

Pour $f(x,y,z)=xyz+ye^x+z^2$,

$$D_{(x,y,z)}f(h)=(yz+ye^x)h_1+(xz+e^x)h_2+(xy+2z)h_3.$$

## Page 156

**Propriété 9 — Interprétation du gradient.** Le gradient est perpendiculaire aux directions tangentes à une surface de niveau, et indique la direction de plus forte augmentation de $f$. Sa norme mesure l’intensité de cette variation au premier ordre.

Pour $p(t)=a+tv$, la règle de chaîne donne

$$\left.\frac d{dt}f(p(t))\right|_{t=0}=\nabla_af\cdot v.$$

Si $v\perp\nabla_af$, cette dérivée est nulle. Pour $\|v\|_2=1$, le produit scalaire est maximal lorsque $v$ a la direction et le sens du gradient ; le maximum vaut $\|\nabla_af\|_2$ si le gradient est non nul. Pour $v=\nabla_af$, la dérivée vaut $\|\nabla_af\|_2^2>0$ lorsque le gradient est non nul.

> La source écrit « dérivée nulle en $t=0\Leftrightarrow f$ constante ». Ce n’est pas une équivalence : une dérivée directionnelle nulle en un point signifie seulement une variation nulle au premier ordre dans cette direction. Elle ne prouve pas que la restriction à la droite est constante.

## Page 157

### EDP du premier ordre et difféomorphismes

Les EDP du premier ordre considérées sont des équations fonctionnelles de la forme

$$F(\partial_xf,\partial_yf,f,x,y)=0,$$

où l’inconnue $f$ est une fonction de deux variables à valeurs réelles.

Exemples :

$$2\partial_xf+3\partial_yf=x^2e^y,\qquad 2y\partial_xf+3x\partial_yf=xy.$$

## Page 158

**Théorème 7 — Intégration par rapport à une variable.** Pour $g$ continue, l’équation

$$\partial_xf(x,y)=g(x,y)\tag{4.4}$$

conduit à

$$f(x,y)=K(y)+\int g(x,y)\,dx,$$

où l’intégrale désigne une primitive par rapport à $x$, et $K$ une fonction arbitraire de $y$. La source demande des solutions et une fonction $K$ de classe $\mathcal C^1$, et qualifie la preuve de triviale.

> Portée de la formule : sur un rectangle, ou localement, la différence de deux solutions est indépendante de $x$. Sur un ouvert quelconque dont les sections horizontales ne sont pas connexes, plusieurs fonctions de $y$ peuvent être nécessaires selon les composantes. De plus, la seule continuité de $g$ ne garantit pas qu’une primitive choisie soit $\mathcal C^1$ aussi par rapport à $y$ ; il faut vérifier la régularité requise pour les solutions.

## Page 159

Pour les EDP du premier ordre plus complexes, le support indique qu’il n’existe pas de méthode générale présentée dans ce cours.

La méthode retenue est la résolution par changement de variables au moyen d’un $\mathcal C^1$-difféomorphisme. Les deux pictogrammes illustrent la difficulté initiale puis la simplification recherchée.

## Page 160

**Définition 6 — $\mathcal C^1$-difféomorphisme.** Pour des ouverts $U\subset\mathbb R^p$ et $V\subset\mathbb R^n$, une application $\phi:U\to V$ est un $\mathcal C^1$-difféomorphisme si :

1. $\phi$ est $\mathcal C^1$ sur $U$ ;
2. $\phi$ est bijective de $U$ sur $V$ ;
3. $\phi^{-1}$ est $\mathcal C^1$ sur $V$.

Intérêt pour une EDP : un changement $(x,y)=\phi(u,v)$ permet de poser $h=f\circ\phi$. La composition préserve la classe $\mathcal C^1$, la bijection relie les anciennes et nouvelles variables, et $f=h\circ\phi^{-1}$ permet le retour aux variables initiales.

Le diagramme oppose l’équation initiale $F(\partial_xf,\partial_yf,f,x,y)=0$, difficile, à une équation transformée $H(\partial_uh,\partial_vh,h,u,v)=0$, plus facile.

## Page 161

**Propriété 10.** Si $\phi:\mathbb R^p\to\mathbb R^n$ est linéaire et bijective, alors $p=n$ et $\phi$ est un $\mathcal C^1$-difféomorphisme.

Preuve : une bijection linéaire entre espaces de dimension finie impose l’égalité des dimensions. $\phi$ et son inverse sont linéaires, donc de classe $\mathcal C^1$.

> La première phrase de preuve source dit qu’une application linéaire est bijective « si et seulement si $n=p$ ». Seule l’implication de la bijectivité vers l’égalité des dimensions est vraie sans autre hypothèse : une matrice carrée peut être singulière.

## Page 162

**Propriété 11 — Caractérisation rapide.** Soient $U\subset\mathbb R^p$ et $V\subset\mathbb R^n$ ouverts. Si $\phi:U\to V$ est $\mathcal C^1$, bijective, et si $D_a\phi$ est une application linéaire bijective pour tout $a\in U$, alors $p=n$ et $\phi$ est un $\mathcal C^1$-difféomorphisme. Démonstration admise.

**Propriété 12.** Dans le cas $p=n$, si $\phi$ est différentiable en $a$ et $\det J_\phi(a)\ne0$, alors $D_a\phi$ est bijective. Démonstration renvoyée au polycopié.

> Les hypothèses $p=n$ et l’existence de la différentielle sont implicites dans la référence au jacobien ; un déterminant n’est défini que pour une matrice carrée.

## Page 163

Exemple des coordonnées sphériques :

$$U=\mathbb R_+^*\times]0,2\pi[\times]0,\pi[,\qquad V=\mathbb R^3\setminus\bigl(\mathbb R_+\times\{0\}\times\mathbb R\bigr),$$

$$f(\rho,\theta,\phi)=(\rho\cos\theta\sin\phi,\ \rho\sin\theta\sin\phi,\ \rho\cos\phi).$$

Ici $\mathbb R_+=[0,+\infty[$ : on retire le demi-plan $y=0,x\ge0$, y compris l’axe vertical. La source affirme que $f$ est bijective de $U$ sur $V$. Ses composantes sont $\mathcal C^1$, et

$$J_f=\begin{pmatrix}
\cos\theta\sin\phi&-\rho\sin\theta\sin\phi&\rho\cos\theta\cos\phi\\
\sin\theta\sin\phi&\rho\cos\theta\sin\phi&\rho\sin\theta\cos\phi\\
\cos\phi&0&-\rho\sin\phi
\end{pmatrix}.$$

Son déterminant est $-\rho^2\sin\phi\ne0$ sur $U$. Ainsi $f$ est un $\mathcal C^1$-difféomorphisme.

## Page 164

**Résolution des EDP par changement de variables — Tableau méthodologique.**

| Étape | Changement direct | Changement indirect |
| --- | --- | --- |
| Variables | $(x,y)=\phi(u,v)$, $\phi:V\to U$ | $(u,v)=\phi(x,y)$, $\phi:U\to V$ |
| Nouvelle fonction | $g=f\circ\phi$ | $g=f\circ\phi^{-1}$, donc $f=g\circ\phi$ |
| Régularité | $f\in\mathcal C^1(U)$ implique $g\in\mathcal C^1(V)$ | même conclusion |
| Retour | $(u,v)=\phi^{-1}(x,y)$ | substituer directement $(u,v)=\phi(x,y)$ |

Dans les deux cas, $\phi$ doit être un $\mathcal C^1$-difféomorphisme entre les domaines indiqués (la ligne commune du tableau source donne un sens unique, inadapté à la colonne directe).

**Direct :**

$$g_u=f_x\,x_u+f_y\,y_u,\qquad g_v=f_x\,x_v+f_y\,y_v.$$

Ces expressions signifient les produits $f_x\,x_u$, $f_y\,y_u$, etc. Résoudre le système pour exprimer $f_x,f_y$ en fonction de $g_u,g_v$, puis substituer dans l’EDP. Si le changement s’inverse simplement, on peut passer à la méthode indirecte.

**Indirect :**

$$f_x=g_u\,u_x+g_v\,v_x,\qquad f_y=g_u\,u_y+g_v\,v_y.$$

Substituer directement dans l’EDP. Résoudre ensuite l’équation transformée, de la forme $\widetilde F(g_u,g_v,g,u,v)=0$, puis revenir à $x,y$. Toutes les dérivées des fonctions composées sont évaluées aux points correspondants.

## Page 165

**Exemple : résoudre $2f_x-f_y=x^2y$ avec $(u,v)=(x,x+2y)$.**

Étape 0 : identifier $\phi:\mathbb R^2\to\mathbb R^2$, $\phi(x,y)=(x,x+2y)$.

Étape 1 : $\phi$ est linéaire, donc $\mathcal C^1$. Le système

$$u=x,\quad v=x+2y\Longleftrightarrow x=u,\quad y=\frac{v-u}{2}$$

montre qu’elle est bijective, d’inverse

$$\phi^{-1}(u,v)=\left(u,\frac{v-u}{2}\right).$$

L’inverse est également linéaire, donc $\mathcal C^1$. Ainsi $\phi$ est un $\mathcal C^1$-difféomorphisme.

## Page 166

Même EDP $2f_x-f_y=x^2y$ et même changement $\phi(x,y)=(x,x+2y)$.

Étape 2 : introduire la nouvelle fonction $g$ par

$$f=g\circ\phi,\qquad f(x,y)=g(\phi(x,y)),\qquad g=f\circ\phi^{-1}.$$

La proposition erronée $g=f\circ\phi$ est barrée sur la diapositive. La régularité $\mathcal C^1$ de $g$ découle de celle de $f$ et de $\phi^{-1}$ par composition ; la dernière phrase du support mentionne $\phi$, alors que l’inverse est celui qui intervient dans cette expression de $g$.

## Page 167

Étape 3 : pour $f=g\circ\phi$, les dérivées sont reliées par

$$f_x(x,y)=g_u(u,v)u_x(x,y)+g_v(u,v)v_x(x,y),$$

$$f_y(x,y)=g_u(u,v)u_y(x,y)+g_v(u,v)v_y(x,y).$$

Puisque $u=x$ et $v=x+2y$,

$$f_x=g_u+g_v,\qquad f_y=2g_v,$$

les dérivées de $g$ étant évaluées en $(u,v)=(x,x+2y)$.

## Page 168

Étape 4 : substitution dans $2f_x-f_y=x^2y$ :

$$2g_u=u^2\frac{v-u}{2}\Longleftrightarrow g_u=\frac14(u^2v-u^3).$$

Étape 5 : intégrer selon $u$ :

$$g(u,v)=\frac{u^3v}{12}-\frac{u^4}{16}+K(v),$$

où $K$ est une fonction quelconque de classe $\mathcal C^1$ sur $\mathbb R$.

## Page 169

Étape 6 : revenir à $f=g\circ\phi$ :

$$f(x,y)=g(x,x+2y)=\frac{x^3(x+2y)}{12}-\frac{x^4}{16}+K(x+2y),\qquad K\in\mathcal C^1(\mathbb R).$$

Ce sont les solutions de $2f_x-f_y=x^2y$ sur $\mathbb R^2$.

## Page 170

### Chapitre 5 — Calcul différentiel d’ordre supérieur

Programme :

- définir les dérivées partielles d’ordre supérieur ou égal à 2 ;
- résoudre des EDP du second ordre ;
- rechercher les extrema des fonctions de $\mathbb R^2$ dans $\mathbb R$.

## Page 171

Pour $f:\mathbb R^2\to\mathbb R$, les dérivées partielles premières sont elles-mêmes des fonctions de $(x,y)$. On peut les dériver à nouveau :

$$\partial_x(\partial_xf)=\frac{\partial^2f}{\partial x^2},\quad \partial_y(\partial_xf)=\frac{\partial^2f}{\partial y\partial x},$$

$$\partial_x(\partial_yf)=\frac{\partial^2f}{\partial x\partial y},\quad \partial_y(\partial_yf)=\frac{\partial^2f}{\partial y^2}.$$

Les dérivées d’ordre 2 se calculent donc comme les dérivées premières des fonctions dérivées premières. La référence au « chapitre suivant » dans le rappel est une coquille : les dérivées premières viennent du chapitre précédent.

## Page 172

Exemple proposé pour les dérivées d’ordre supérieur :

$$f(x,y)=\frac{xy^3}{x^2+y^2}.$$

Aucun calcul supplémentaire n’est affiché sur cette page.

## Page 173

**Définition 1 — Dérivées partielles d’ordre supérieur.** Soient $U\subset\mathbb R^p$ ouvert, $f:U\to\mathbb R^n$, $a\in U$, $k\ge1$ et $(i_1,\ldots,i_k)\in\{1,\ldots,p\}^k$.

On dérive successivement selon les variables $x_{i_1},\ldots,x_{i_k}$. Pour définir la dérivée d’ordre $k$ en $a$, la dérivée précédente d’ordre $k-1$ doit exister dans un voisinage de $a$ et être dérivable en $a$ selon $x_{i_k}$.

Notation :

$$\frac{\partial^kf}{\partial x_{i_k}\cdots\partial x_{i_2}\partial x_{i_1}}(a).$$

Exemples de notations : $\partial^2f/\partial x^2$, $\partial^2f/(\partial x\partial y)$, $\partial^3f/(\partial x\partial y\partial z)$. L’opérateur le plus à droite agit en premier.

## Page 174

Exemple : pour $f(x,y,z)=xy^2z^3$,

$$\frac{\partial^3f}{\partial x\partial y\partial z}=\partial_x\partial_y(3xy^2z^2)=\partial_x(6xyz^2)=6yz^2.$$

**Définition 2 — Classes $\mathcal C^k$ et $\mathcal C^\infty$.** Une application $f:U\subset\mathbb R^p\to\mathbb R^n$ est de classe $\mathcal C^k$ si toutes ses dérivées partielles d’ordre $k$ existent et sont continues sur $U$. Elle est $\mathcal C^\infty$ si elle est $\mathcal C^k$ pour tout entier $k$.

## Page 175

**Propriété 1.** Si $f$ est de classe $\mathcal C^k$ sur $U$, toutes ses dérivées partielles d’ordre inférieur ou égal à $k$ sont définies et continues.

Démonstration admise.

## Page 176

La structure algébrique de $\mathcal C^k(U,F)$ est analogue à celle de $\mathcal C^1(U,F)$ : c’est un espace vectoriel ; les produits de fonctions scalaires $\mathcal C^k$ restent $\mathcal C^k$.

> Comme au chapitre précédent, la multiplication nécessite un codomaine où un produit approprié est défini ; le seul fait que $F$ soit un EVN ne suffit pas.

**Théorème 1 — Stabilité par composition.** Pour $f:U\subset\mathbb R^p\to\mathbb R^q$ et $g:V\subset\mathbb R^q\to\mathbb R^n$ de classe $\mathcal C^k$, avec $U,V$ ouverts et $f(U)\subset V$, la composée $g\circ f$ est $\mathcal C^k$ sur $U$. Démonstration admise.

## Page 177

**Théorème 2 — Régularité composante par composante.** Pour $f=(f_1,\ldots,f_n):U\subset\mathbb R^p\to\mathbb R^n$,

$$f\in\mathcal C^k(U,\mathbb R^n)\Longleftrightarrow\forall i\in\{1,\ldots,n\},\quad f_i\in\mathcal C^k(U,\mathbb R).$$

La démonstration est indiquée « évidente ». La régularité vectorielle se vérifie sur toutes les fonctions coordonnées.

## Page 178

**Théorème 3 — Théorème de Schwarz.** Soit $f:U\subset\mathbb R^p\to\mathbb R^q$ de classe $\mathcal C^1$. Si les deux dérivées partielles secondes croisées sont définies dans un voisinage de $a$ et continues en $a$, alors

$$\frac{\partial^2f}{\partial x_j\partial x_i}(a)=\frac{\partial^2f}{\partial x_i\partial x_j}(a).$$

Démonstration admise. Dans le cas de deux variables, cela donne $\partial_x\partial_yf=\partial_y\partial_xf$ sous les mêmes hypothèses.

Remarque 2 : être de classe $\mathcal C^2$ au voisinage du point est une condition suffisante pour obtenir l’égalité des dérivées croisées.

## Page 179

Le théorème de Schwarz est rappelé. Exemple 1 : $f(x,y)=x\sin x\sin y$ est $\mathcal C^\infty$ sur $\mathbb R^2$, produit de fonctions $\mathcal C^\infty$.

$$\partial_xf=(\sin x+x\cos x)\sin y,\qquad\partial_yf=x\sin x\cos y,$$

$$\partial_y\partial_xf=\partial_x\partial_yf=(\sin x+x\cos x)\cos y.$$

## Page 180

**Exemple 2 — Cas où les dérivées croisées diffèrent.**

$$f(x,y)=\begin{cases}\dfrac{xy(x^2-y^2)}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$

À l’origine, $f(t,0)=f(0,t)=0$, donc $\partial_xf(0,0)=\partial_yf(0,0)=0$.

Hors de l’origine :

$$\partial_xf(x,y)=\frac{y(x^4+4x^2y^2-y^4)}{(x^2+y^2)^2},$$

$$\partial_yf(x,y)=-\frac{x(4x^2y^2-x^4+y^4)}{(x^2+y^2)^2}.$$

Le point d’évaluation de la seconde formule est $(x,y)$ ; l’étiquette source conserve à tort $(0,0)$.

## Page 181

Les dérivées partielles premières sont les formules rationnelles précédentes hors de $(0,0)$, et valent $0$ à l’origine. Un passage en polaires montre qu’elles sont continues : chaque expression est $\rho$ multiplié par une fonction bornée de l’angle.

> Coquilles de l’encadré supérieur : les conditions « $(x,y)=(0,0)$ » et « $(x,y)\ne(0,0)$ » sont inversées dans les deux définitions par morceaux ; la seconde dérivée est aussi étiquetée $\partial_x$ au lieu de $\partial_y$.

À l’origine, calcul des dérivées secondes croisées :

$$\partial_x(\partial_yf)(0,0)=\lim_{t\to0}\frac{\partial_yf(t,0)-\partial_yf(0,0)}t=\lim_{t\to0}\frac{t}{t}=1,$$

$$\partial_y(\partial_xf)(0,0)=\lim_{t\to0}\frac{\partial_xf(0,t)-\partial_xf(0,0)}t=\lim_{t\to0}\frac{-t}{t}=-1.$$

Elles existent et sont différentes. Le support présente les mêmes quotients sous les formes $t^5/t^5$ et $-t^5/t^5$.

## Page 182

**EDP d’ordre 2.** On étudie désormais les équations aux dérivées partielles qui font apparaître les dérivées secondes de la fonction inconnue.

## Page 183

### EDP du second ordre

**Théorème 4.** Les solutions $\mathcal C^2$ de $\partial_{xx}f=0$ sont de la forme

$$f(x,y)=xG(y)+H(y),$$

avec $G,H$ de classe $\mathcal C^2$. Preuve : intégrer deux fois par rapport à $x$.

**Théorème 5.** Les solutions $\mathcal C^2$ de $\partial_x\partial_yf=0$ sont de la forme

$$f(x,y)=G(x)+H(y),$$

avec $G,H$ de classe $\mathcal C^2$ sur les projections respectives du domaine. La source indique que la preuve est tout aussi immédiate.

> Ces formules décrivent les solutions sur un rectangle et localement. L’énoncé les affirme sur tout ouvert $U$ ; globalement, un domaine aux sections non connexes peut nécessiter des fonctions différentes selon les composantes, comme pour le théorème d’intégration du premier ordre.

## Page 184

Comme pour les EDP du premier ordre, on emploie des changements de variables pour simplifier les EDP du second ordre, cette fois par des $\mathcal C^2$-difféomorphismes.

**Définition 3.** Une application $\phi:U\to V$ entre ouverts est un $\mathcal C^2$-difféomorphisme si elle est $\mathcal C^2$, bijective, et si son inverse est $\mathcal C^2$.

## Page 185

**Équation des ondes.** Chercher $f\in\mathcal C^2(\mathbb R^2)$ telle que

$$f_{xx}-\frac1{c^2}f_{tt}=0,$$

avec le changement $(X,Y)=(x+ct,x-ct)$, où $c\ne0$ est nécessaire pour l’équation et le changement.

Étape 0 : $\phi(x,t)=(x+ct,x-ct)$.

Étape 1 : $\phi$ est linéaire, son noyau est réduit à $(0,0)$, donc c’est une bijection de $\mathbb R^2$ dans lui-même. Elle et son inverse sont $\mathcal C^2$ : c’est un $\mathcal C^2$-difféomorphisme.

Étape 2 : $f=g\circ\phi$, donc $f(x,t)=g(x+ct,x-ct)=g(X,Y)$ et $g=f\circ\phi^{-1}$. La composition assure $g\in\mathcal C^2$.

## Page 186

Étape 3 : exprimer les dérivées de $f$ avec celles de $g$ :

$$f_x=g_X\,X_x+g_Y\,Y_x=g_X+g_Y,\qquad f_t=g_X\,X_t+g_Y\,Y_t=cg_X-cg_Y.$$

En dérivant encore et en utilisant Schwarz :

$$f_{xx}=g_{XX}+g_{YY}+2g_{XY},\qquad f_{tt}=c^2g_{XX}+c^2g_{YY}-2c^2g_{XY}.$$

Les dérivées de $f$ sont évaluées en $(x,t)$ et celles de $g$ en $(X,Y)=(x+ct,x-ct)$.

## Page 187

Étape 4 : remplacer les dérivées dans l’équation des ondes.

> Coquille du support : l’encadré affiche $g_{XX}=0$. Les expressions de la page précédente donnent en réalité $f_{xx}-f_{tt}/c^2=4g_{XY}$, donc l’équation transformée est $g_{XY}=0$.

Étape 5 : la solution générale annoncée, cohérente avec $g_{XY}=0$, est

$$g(X,Y)=h(Y)+k(X),\qquad h,k\in\mathcal C^2(\mathbb R).$$

Étape 6 : retour à $f=g\circ\phi$ :

$$f(x,t)=g(x+ct,x-ct)=h(x-ct)+k(x+ct).$$

## Page 188

### Extrema — Introduction

La recherche de minima et maxima de fonctions de $\mathbb R^n$ dans $\mathbb R$ intervient dans l’optimisation : économie (maximiser les profits, minimiser les coûts), physique (principes variationnels), intelligence artificielle, etc.

Après les définitions d’extrema locaux et globaux, on présente des méthodes pour les fonctions $\mathcal C^2$. Des algorithmes numériques de recherche de minima locaux, comme le gradient conjugué, seront étudiés plus tard. Le cours fait le lien avec les fonctions d’une variable connues depuis le lycée.

## Page 189

### Extrema des fonctions à valeurs réelles

**Définition 4 — Extrema locaux et stricts.** Le support considère $A\subset\mathbb R^p$, un point **intérieur** $a\in\mathring A$ et $f:A\to\mathbb R$.

1. Minimum local en $a$ : il existe un voisinage $V\subset A$ de $a$ tel que $f(x)\ge f(a)$ pour tout $x\in V$.
2. Minimum local strict en $a$ : il existe un tel $V$ avec $f(x)>f(a)$ pour tout $x\in V\setminus\{a\}$.
3. Maximum local en $a$ : il existe un tel $V$ avec $f(x)\le f(a)$ pour tout $x\in V$.
4. Maximum local strict en $a$ : il existe un tel $V$ avec $f(x)<f(a)$ pour tout $x\in V\setminus\{a\}$.

Les maxima et minima sont appelés génériquement des **extrema**.

## Page 190

**Illustration des extrema locaux stricts en une variable.** La courbe présente un sommet en $a$ et un creux en $b$.

Sur un voisinage $V_a=]a-r,a+r[$, tout $x\ne a$ vérifie $f(x)<f(a)$ : maximum local strict. Sur un voisinage $V_b=]b-r',b+r'[$, tout $x\ne b$ vérifie $f(x)>f(b)$ : minimum local strict. Les arcs concernés et leurs projections sur l’axe sont colorés en rouge et bleu.

## Page 191

**Illustration en deux variables.** Le graphe $z=f(x,y)$ montre une portion de surface en forme de creux au-dessus de $a=(x_a,y_a)$, avec un voisinage $V_a$, et une portion en forme de sommet au-dessus de $b=(x_b,y_b)$, avec un voisinage $V_b$.

- Minimum local strict en $a$ : $f(x,y)>f(x_a,y_a)$ pour $(x,y)\in V_a\setminus\{a\}$.
- Maximum local strict en $b$ : $f(x,y)<f(x_b,y_b)$ pour $(x,y)\in V_b\setminus\{b\}$.

Les disques dessinés dans le plan du domaine représentent les voisinages ; les surfaces correspondantes sont dessinées au-dessus.

## Page 192

**Définition 5 — Extremum global.** Pour une partie quelconque $A\subset\mathbb R^n$, $a\in A$ et $f:A\to\mathbb R$ :

- minimum global en $a$ si $\forall x\in A,\ f(x)\ge f(a)$ ;
- maximum global en $a$ si $\forall x\in A,\ f(x)\le f(a)$.

Sur un domaine fermé, un extremum global peut se trouver sur la frontière. Si $f$ n’est pas minorée, elle n’a pas de minimum global ; si elle n’est pas majorée, elle n’a pas de maximum global.

> Le support oppose ici extrema globaux au bord et extrema locaux intérieurs : cette opposition suit la convention restrictive de la définition 4. Avec les voisinages relatifs au domaine, la définition générale permet aussi des extrema locaux au bord.

## Page 193

Pour une fonction réelle $\mathcal C^2$ et un point intérieur $a$, une condition nécessaire d’extremum est $f'(a)=0$, mais elle n’est pas suffisante.

Trois graphes illustrent, en $a=0$ :

- $f(x)=x^2$ : $f'(0)=0$ et $f''(0)>0$, minimum ;
- $f(x)=-x^2$ : $f'(0)=0$ et $f''(0)<0$, maximum ;
- $f(x)=x^3$ : $f'(0)=f''(0)=0$, aucun extremum.

La dérivée seconde permet de conclure lorsqu’elle est strictement positive ou négative ; si elle est nulle, une étude supplémentaire est nécessaire.

## Page 194

**Définition 6 — Point critique.** Pour $U\subset\mathbb R^p$ ouvert, $f:U\to\mathbb R$ et $a\in U$, le point $a$ est critique si toutes les dérivées partielles premières existent en $a$ et sont nulles :

$$\nabla f(a)=\begin{pmatrix}\partial_{x_1}f(a)\\\vdots\\\partial_{x_p}f(a)\end{pmatrix}=0_{\mathbb R^p}.$$

## Page 195

**Propriété 2 — Condition nécessaire.** Si $f:U\subset\mathbb R^p\to\mathbb R$ admet un extremum local en $a\in U$ et si toutes ses dérivées partielles premières existent en $a$, alors $a$ est critique.

Preuve pour un minimum : il existe $r>0$ tel que $B(a,r)\subset U$ et $f(x)\ge f(a)$ dans cette boule. Pour une direction canonique $e_i$ et $h$ assez petit,

$$f(a+he_i)-f(a)\ge0.$$

Le quotient par $h$ est donc positif ou nul pour $h>0$, négatif ou nul pour $h<0$. Comme les deux limites définissent la même dérivée,

$$\partial_{x_i}f(a)\ge0\quad\text{et}\quad\partial_{x_i}f(a)\le0,$$

donc $\partial_{x_i}f(a)=0$. Cela vaut pour chaque $i$, d’où $\nabla_af=0$. Pour une norme quelconque, la condition suffisante sur $h$ est $|h|\|e_i\|<r$ ; la source utilise $|h|<r$.

## Page 196

Pour conclure sur la nature des points critiques, étudier les dérivées secondes.

**Propriété 3 — Développement limité d’ordre 2.** Si $f:U\subset\mathbb R^p\to\mathbb R$ est $\mathcal C^2$, $a\in U$ et $U_0=\{h:a+h\in U\}$, il existe $\varepsilon:U_0\to\mathbb R$ avec $\varepsilon(h)\to0$ tel que

$$f(a+h)=f(a)+\sum_{j=1}^ph_j\partial_{x_j}f(a)+\frac12\sum_{i=1}^p\sum_{j=1}^ph_ih_j\partial_{x_i}\partial_{x_j}f(a)+\|h\|^2\varepsilon(h).$$

C’est le développement limité de $f$ à l’ordre 2 en $a$. Démonstration admise.

## Page 197

**Théorème 6 — Conditions suffisantes d’ordre 2.** Soit $a$ un point critique de $f\in\mathcal C^2(U,\mathbb R)$. Poser

$$Q(h)=\sum_{i=1}^p\sum_{j=1}^ph_ih_j\partial_{x_i}\partial_{x_j}f(a).$$

- Si $Q$ est positive et ne s’annule qu’en $h=0$, $a$ est un minimum local strict.
- Si $Q$ est négative et ne s’annule qu’en $h=0$, $a$ est un maximum local strict.
- Si $Q$ prend des valeurs positives et négatives dans tout voisinage de $0$, $f$ n’a pas d’extremum local en $a$.

## Page 198

**Théorème 6 — Conditions suffisantes d’ordre 2.** Soit $a$ un point critique de $f\in\mathcal C^2(U,\mathbb R)$. Poser

$$Q(h)=\sum_{i=1}^p\sum_{j=1}^ph_ih_j\partial_{x_i}\partial_{x_j}f(a).$$

- Si $Q$ est positive et ne s’annule qu’en $h=0$, $a$ est un minimum local strict.
- Si $Q$ est négative et ne s’annule qu’en $h=0$, $a$ est un maximum local strict.
- Si $Q$ prend des valeurs positives et négatives dans tout voisinage de $0$, $f$ n’a pas d’extremum local en $a$.

Le support esquisse la preuve par une approximation $f(a+h)-f(a)\approx Q(h)$.

> Précision : le développement exact est $f(a+h)-f(a)=\frac12Q(h)+o(\|h\|^2)$, puisque $\nabla f(a)=0$. Si $Q$ est définie positive, la compacité de la sphère unité donne $Q(h)\ge c\|h\|^2$ avec $c>0$, ce qui contrôle le reste ; le cas négatif s’en déduit. Si $Q$ change de signe, deux directions donnent des signes opposés pour $f(a+th)-f(a)$ à petit $t$. L’approximation du gradient en $a+h$ mentionnée dans le support ne remplace pas cette justification.

## Page 199

**Définition 7 — Matrice hessienne.** Pour une fonction réelle $\mathcal C^2$,

$$H_f(a)=\left(\partial_{x_i}\partial_{x_j}f(a)\right)_{1\le i,j\le p}.$$

La source la présente en un point critique, mais la matrice est définie en tout point de $U$.

**Définition 8 — Notations de Monge en dimension 2.**

$$r=f_{xx}(a),\qquad s=f_{xy}(a)=f_{yx}(a),\qquad t=f_{yy}(a),$$

$$H_f(a)=\begin{pmatrix}r&s\\s&t\end{pmatrix}.$$

## Page 200

**Théorème 7 — Conditions suffisantes en dimension 2.** Soient $f\in\mathcal C^2(U,\mathbb R)$ et $a$ un point critique. Poser $\Delta=\det H_f(a)=rt-s^2$.

1. Si $\Delta>0$ : $r>0$ donne un minimum local strict ; $r<0$ donne un maximum local strict.
2. Si $\Delta<0$, aucun extremum local : $a$ est un **point-col**, ou **point-selle**.
3. Si $\Delta=0$, aucune conclusion sans une étude plus poussée.

Le dessin représente une surface en selle, montant dans une direction et descendant dans une autre autour du point central.

## Page 201

**Démonstration du critère en dimension 2.** Au point critique $a$, le développement de Taylor donne

$$f(a+(h,k))-f(a)=\frac12(rh^2+2shk+tk^2)+(h^2+k^2)\varepsilon(h,k),\qquad\varepsilon(h,k)\to0.$$

Poser $Q(h,k)=rh^2+2shk+tk^2$ et $\Delta=rt-s^2$.

**Si $\Delta>0$**, $r\ne0$ et la mise sous forme de carrés donne

$$Q(h,k)=r\left(h+\frac srk\right)^2+\frac{rt-s^2}{r}k^2.$$

Les deux coefficients ont le signe de $r$ ; $Q=0$ équivaut à $h+sk/r=0$ et $k=0$, donc à $(h,k)=(0,0)$. Si $r>0$, $Q$ est définie positive et $a$ est un minimum local strict ; si $r<0$, elle est définie négative et $a$ est un maximum local strict.

**Si $\Delta<0$**, distinguer les cas :

- Si $r\ne0$, $Q(h,0)=rh^2$ a le signe de $r$, tandis que $Q(-sk/r,k)=(\Delta/r)k^2$ a le signe opposé. On obtient les deux signes arbitrairement près de $(0,0)$.
- Si $r=0$, on a $s\ne0$. Si $t\ne0$,

$$Q(th,sh)Q(th,-sh)=(3ts^2h^2)(-ts^2h^2)=-3t^2s^4h^4<0\quad(h\ne0).$$

- Si $r=t=0$, $Q(h,h)Q(h,-h)=(2sh^2)(-2sh^2)=-4s^2h^4<0$ pour $h\ne0$.

Dans tous les cas avec $\Delta<0$, $Q$ prend les deux signes près de l’origine : $a$ n’est pas un extremum local. Le développement d’ordre 2 relie ces signes à ceux de $f(a+(h,k))-f(a)$ le long des directions considérées.

## Page 202

**Plan général de recherche d’extrema de $f:U\subset\mathbb R^2\to\mathbb R$.**

0. Vérifier que $f$ est de classe $\mathcal C^2$ sur $U$.
1. Chercher les points critiques en résolvant $\partial_xf(x,y)=0$ et $\partial_yf(x,y)=0$.
2. Pour chaque point critique, calculer $r,s,t$ : si $rt-s^2>0$ et $r>0$, minimum local strict ; si $rt-s^2>0$ et $r<0$, maximum local strict ; si $rt-s^2<0$, point-selle ; si $rt-s^2=0$, étude locale supplémentaire, par exemple un développement à un ordre supérieur.
3. Rechercher les extrema globaux : si $f$ n’est pas minorée, pas de minimum global ; si elle n’est pas majorée, pas de maximum global. La diapositive ne donne pas d’autre critère à cette étape.

## Page 203

**Merci pour votre attention.** Deux illustrations de fin accompagnent le texte : un personnage de bande dessinée quittant les lieux et un carton « The End ».
