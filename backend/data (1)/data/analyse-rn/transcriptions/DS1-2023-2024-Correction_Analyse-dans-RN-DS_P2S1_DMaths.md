---
source: "PREING2-S1/Analyse-dans-RN-DS/DS1-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_DMaths.pdf"
pages: 8
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Analyse dans Rn — DS1 2023–2024, sujet 1 : énoncé et corrigé

## Page 1

### Préing 2 — DS1, sujet 1 d’Analyse dans Rn

**Lundi 13 novembre 2023 — durée : 1 h.** Aucun appareil électronique ni document autorisé. Barème indicatif ; qualité de rédaction et précision des justifications prises en compte. L’ordre de traitement est libre. Le cartouche annonce « 1 page recto » et le texte « 4 exercices » ; ce fichier contient huit pages de corrigé et utilise les numéros 1, 2 et 4.

### Exercice 1 — Question de cours/TD (4,5 points)

Dans un espace vectoriel normé $(E,\|\cdot\|)$, montrer que la boule fermée $\overline B(a,r)$, $r>0$, est fermée.

**Correction.** On montre que son complémentaire est ouvert. Pour $X\notin\overline B(a,r)$, posons $r'=\|X-a\|-r>0$. Si $Y\in B(X,r')$, l’inégalité triangulaire donne
$$\|Y-a\|\ge\|X-a\|-\|X-Y\|>\|X-a\|-r'=r.$$
Ainsi $Y$ est extérieur à la boule fermée. Donc $B(X,r')\subset E\setminus\overline B(a,r)$ pour tout point $X$ de ce complémentaire : il est ouvert et la boule est fermée.

**Barème :** 0,5 point pour le passage au complémentaire ; 1 point pour le choix du rayon ; 1 point pour sa stricte positivité ; 1 point pour $\|Y-a\|>r$ ; 1 point pour la conclusion. Les signes d’équivalence utilisés dans la chaîne imprimée sont à lire comme des implications lors du passage à l’inégalité stricte.

## Page 2

### Exercice 2 — Deux normes sur R² (9 points)

$$N_1(x,y)=|3x+y|+|x+y|,\qquad N_2(x,y)=\tfrac12|x|+|y|.$$
1. Montrer que ce sont des normes (4,5 points).
2. Définir leur équivalence (1 point).
3. Sont-elles équivalentes ? (0,5 point.)
4. Tracer la sphère unité de $N_1$ (3 points).

**1. Pour $N_1$.** Si $N_1(x,y)=0$, la positivité des deux termes impose
$$\begin{cases}3x+y=0,\\x+y=0\end{cases}\iff\begin{cases}2x=0,\\y=-x\end{cases}\iff x=y=0.$$
Barème : 1 point seulement si toutes les étapes figurent ; 0 sans système d’équations.

Pour $\lambda\in\mathbb R$, $N_1(\lambda x,\lambda y)=|\lambda|N_1(x,y)$ (0,5 point). Pour $X=(x,y)$ et $X'=(x',y')$,
$$N_1(X+X')=|3x+3x'+y+y'|+|x+x'+y+y'|\le N_1(X)+N_1(X')$$
(1 point). Ainsi $N_1$ est une norme.

**Pour $N_2$.** $N_2(x,y)=0$ implique $x=y=0$ (0,5 point). Les autres propriétés se poursuivent page suivante.

**Coquilles de notation :** le PDF écrit parfois $N$ pour $N_1$ et $(x'+y')$ au lieu du couple $(x',y')$ dans l’addition vectorielle.

## Page 3

**Exercice 2 — 1, suite pour $N_2$.**
$$N_2(\lambda x,\lambda y)=\tfrac12|\lambda x|+|\lambda y|=|\lambda|N_2(x,y)$$
(0,5 point), et
$$N_2(x+x',y+y')\le\tfrac12|x|+|y|+\tfrac12|x'|+|y'|=N_2(x,y)+N_2(x',y')$$
(1 point). Donc $N_2$ est une norme.

**2.** L’équivalence signifie
$$\exists\alpha,\beta>0,\ \forall X\in\mathbb R^2,\quad\alpha N_1(X)\le N_2(X)\le\beta N_1(X).$$
Barème : 1 point sans ambiguïté, 0,5 en cas d’ambiguïté, 0 à la moindre erreur.

**3.** Oui : toutes les normes sur un espace vectoriel de dimension finie sont équivalentes, et $\dim\mathbb R^2=2$. Barème : 0,5 point ; 0 sans justification ou si elle est fausse, même partiellement.

**4. Sphère unité.**
$$\mathcal S=\{(x,y):N_1(x,y)=1\}=\{(x,y):|3x+y|+|x+y|=1\}.$$
Équation et/ou définition correcte : 0,5 point. Premier cas : si $3x+y>0$ et $x+y>0$, l’équation devient $4x+2y=1$, soit $y=1/2-2x$ (0,5 point).

## Page 4

**Exercice 2 — 4, autres cas.**

| Signes de $3x+y$ et $x+y$ | Équation de la sphère dans la région |
|---|---|
| Négatif, positif | $-2x=1$, donc $x=-1/2$ |
| Positif, négatif | $2x=1$, donc $x=1/2$ |
| Négatif, négatif | $-4x-2y=1$, donc $y=-1/2-2x$ |

Chaque cas vaut 0,5 point. Le dessin (0,5 point) montre le contour d’un parallélogramme, bord de la région remplie, dont les sommets sont
$$(-\tfrac12,\tfrac32),\quad(-\tfrac12,\tfrac12),\quad(\tfrac12,-\tfrac32),\quad(\tfrac12,-\tfrac12).$$
Les côtés obliques sont portés par $y=\pm1/2-2x$ et les deux autres par $x=\pm1/2$. Les cas d’égalité des formes linéaires fournissent les sommets ; ils complètent les inégalités strictes du découpage imprimé.

### Exercice 4 — Un peu de topologie dans R (6,5 points)

On munit $\mathbb R$ de sa valeur absolue. Pour $a<b$, on considère
$$I_1=]a,b],\qquad I_2=([-1,1[\cap]0,2])\cup\{3\}.$$

## Page 5

**Exercice 4 — 1.** Déterminer si les ensembles sont ouverts, fermés ou aucun des deux, à l’aide des définitions ou des suites (2,5 points).

**$I_1$ n’est pas fermé.** Posons $u_n=a+1/n$. Dès que $n\ge n_0$, avec $n_0$ entier supérieur ou égal à $1/(b-a)$, $u_n\in I_1$. Mais $u_n\to a\notin I_1$. Barème : 0,5 point si l’appartenance à partir d’un certain rang est précisée, 0,25 sinon. L’autre méthode acceptée dans le corrigé est de montrer que le complémentaire n’est pas ouvert en $a$.

**$I_1$ n’est pas ouvert.** Pour tout $r>0$, $y=b+r/2$ appartient à $B(b,r)$ mais pas à $I_1$. Aucune boule centrée en $b$ n’est incluse dans $I_1$. Barème : 0,5 point si le raisonnement vaut pour tout $r>0$. L’autre méthode acceptée consiste à montrer par une suite que le complémentaire n’est pas fermé.

**Simplification de $I_2$.** $I_2=]0,1[\cup\{3\}$ (0,5 point).

## Page 6

**Exercice 4 — 1, suite pour $I_2$.**

**Non fermé.** Pour $n\ge2$, $u_n=1/n\in I_2$, tandis que $u_n\to0\notin I_2$. Barème : 0,5 point si le rang est précisé, 0,25 sinon. Autre méthode acceptée : montrer que le complémentaire n’est pas ouvert en zéro.

**Non ouvert.** Pour tout $r>0$, $3+r/2\in B(3,r)$ et $3+r/2\notin I_2$. Donc aucune boule centrée en $3$ n’est incluse dans $I_2$. Barème : 0,5 point si le raisonnement est valable pour tout rayon. Autre méthode acceptée : montrer par les suites que le complémentaire n’est pas fermé. Le texte écrit une fois $B(b,r)$ au lieu de $B(3,r)$.

**2.** Déterminer $\mathring I_1$ et $\overline I_2$, par la méthode de son choix (4 points).

Pour l’intérieur de $I_1$, proposer le candidat $C=]a,b[$, puisque l’intérieur est le plus grand ouvert inclus dans $I_1$ (étape 1 : 0,5 point). Vérifier ensuite que $C$ est ouvert et $C\subset I_1$ (étape 2 : 0,5 point).

## Page 7

**Exercice 4 — 2, intérieur de $I_1$.**
$$C=]a,b[=B\left(\frac{a+b}2,\frac{b-a}2\right)$$
est ouvert et $I_1=C\cup\{b\}$, donc $C\subset\mathring I_1$. Pour la réciproque (étape 3 : 1 point), le seul point de $I_1\setminus C$ est $b$. Pour tout $r>0$, $b+r/2\in B(b,r)\setminus I_1$ ; ainsi $b$ n’est pas intérieur. Donc
$$\mathring I_1=]a,b[.$$

**Adhérence de $I_2$.** Proposer $C=[0,1]\cup\{3\}$ (0,5 point). C’est un fermé contenant $I_2$, donc $\overline I_2\subset C$ (0,5 point). Les seuls points de $C\setminus I_2$ sont $0$ et $1$. Les suites $u_n=1/n$ et $v_n=1-1/n$, pour $n\ge2$, appartiennent à $I_2$ et tendent respectivement vers $0$ et $1$. Donc ces deux points sont adhérents (1 point), et
$$\overline I_2=[0,1]\cup\{3\}.$$

**Coquille du corrigé :** la phrase après les limites indique « $\{1\}$ et $\{2\}$ » ; les points établis par les deux suites sont $0$ et $1$.

## Page 8

**Consignes de barème finales.**

- 0,5 point si $\mathring I_1$ est donné sans justification ou si le reste de la démonstration est faux.
- 0,5 point si $\overline I_2$ est donné sans justification ou si le reste de la démonstration est faux.

Le reste de cette page est vide.
