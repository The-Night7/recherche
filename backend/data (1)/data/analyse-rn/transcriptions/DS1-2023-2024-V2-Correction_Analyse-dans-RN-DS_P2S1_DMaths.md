---
source: "PREING2-S1/Analyse-dans-RN-DS/DS1-2023-2024-V2-Correction_Analyse-dans-RN-DS_P2S1_DMaths.pdf"
pages: 7
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Analyse dans Rn — DS1 2023–2024, sujet 2 : énoncé et corrigé

## Page 1

### Préing 2 — DS1, sujet 2 d’Analyse dans Rn

**Mardi 14 novembre 2023 — durée : 1 h.** Aucun appareil électronique ni document autorisé. Barème indicatif. La rédaction et les justifications sont prises en compte ; ordre de traitement libre. Le cartouche annonce un sujet d’une feuille recto verso et quatre exercices ; ce corrigé de sept pages en présente trois.

### Exercice 1 — Questions de cours/TD (5 points)

Dans un espace vectoriel normé $(E,\|\cdot\|)$ :

1. Définir un ouvert et un fermé (1 point).
2. Montrer que $B(a,r)$ est ouverte pour $r>0$ (4 points).

**1. Définitions acceptées.** $A$ est ouvert si et seulement s’il est voisinage de chacun de ses points, ou, de façon équivalente,
$$\forall x\in A,\ \exists r>0,\ B(x,r)\subset A.$$
$A$ est fermé si et seulement si son complémentaire $E\setminus A$ est ouvert ; les deux formulations précédentes appliquées à ce complémentaire sont également acceptées. Chaque définition vaut 0,5 point. Le barème imprimé refuse toute autre définition et retire les points en cas d’imprécision.

**2.** Soit $X\in B(a,r)$ ; on a $\|X-a\|<r$.

## Page 2

**Exercice 1 — 2, preuve.** Posons $\varepsilon=r-\|X-a\|>0$. Pour $Y\in B(X,\varepsilon)$,
$$\|Y-a\|\le\|Y-X\|+\|X-a\|<\varepsilon+\|X-a\|=r.$$
Donc $Y\in B(a,r)$ et $B(X,\varepsilon)\subset B(a,r)$. Chaque point admet ainsi une boule incluse dans $B(a,r)$ : cette dernière est ouverte. Barème : 1 point pour le rayon, 1 pour sa positivité, 1 pour l’inégalité $\|Y-a\|<r$, 1 pour la conclusion.

### Exercice 2 — Deux normes sur l’espace des matrices (9 points)

Pour $n,p\ge1$ et $A=(a_{ij})\in M_{n,p}(\mathbb R)$,
$$f(A)=\sum_{i=1}^n\sum_{j=1}^p|a_{ij}|,\qquad g(A)=\max_{1\le i\le n,\,1\le j\le p}|a_{ij}|.$$
1. Montrer que $f,g$ sont des normes (4,5 points).
2. Trouver $\alpha,\beta>0$ tels que $\alpha g(A)\le f(A)\le\beta g(A)$ (2 points).
3. Sont-elles équivalentes ? (0,5 point.)
4. Pour $n=p=2$, donner un élément $C$ de la sphère unité de $f$ et un élément $D$ de la sphère unité de $g$, centrées en la matrice nulle (2 points).

## Page 3

**Exercice 2 — 1, correction.**

**Norme $f$.** Si $f(A)=0$, la somme de termes positifs est nulle, donc tous les $a_{ij}=0$ (0,5 point). Pour $\lambda\in\mathbb R$,
$$f(\lambda A)=\sum_{i,j}|\lambda a_{ij}|=|\lambda|\sum_{i,j}|a_{ij}|=|\lambda|f(A)$$
(0,5 point). Pour $A,B\in M_{n,p}$,
$$f(A+B)=\sum_{i,j}|a_{ij}+b_{ij}|\le\sum_{i,j}(|a_{ij}|+|b_{ij}|)=f(A)+f(B)$$
(1 point).

**Norme $g$.** Si $g(A)=0$, le maximum des $|a_{ij}|$ est nul, donc tous les coefficients sont nuls (0,5 point). L’homogénéité suit de
$$g(\lambda A)=\max_{i,j}|\lambda a_{ij}|=|\lambda|\max_{i,j}|a_{ij}|=|\lambda|g(A)$$
(0,5 point). Pour l’inégalité triangulaire (1,5 point), on établit d’abord, pour chaque couple $(i,j)$,
$$|a_{ij}+b_{ij}|\le|a_{ij}|+|b_{ij}|\le g(A)+g(B).\tag{1}$$

## Page 4

**Exercice 2 — 1, fin.** L’inégalité (1) vaut notamment au couple qui maximise $|a_{ij}+b_{ij}|$. Donc $g(A+B)\le g(A)+g(B)$. Le barème impose d’écrire l’inégalité ponctuelle (1), faute de quoi il attribue zéro à cette étape.

**2. Comparaison.** Choisir $(i_0,j_0)$ tel que $|a_{i_0j_0}|=g(A)$. Alors
$$f(A)=g(A)+\sum_{(i,j)\ne(i_0,j_0)}|a_{ij}|\ge g(A),$$
donc $\alpha=1$ (1 point). **Correction d’indice :** le PDF écrit deux sommes avec simultanément $i\ne i_0$ et $j\ne j_0$ ; cela omet les autres éléments de la ligne et de la colonne. Il faut exclure seulement le couple $(i_0,j_0)$.

Comme $|a_{ij}|\le g(A)$ pour chacun des $np$ coefficients,
$$f(A)\le np\,g(A),$$
donc $\beta=np$ (1 point). Ainsi
$$g(A)\le f(A)\le np\,g(A).$$
**3. Première méthode (0,5 point).** Cet encadrement prouve directement l’équivalence des deux normes.

## Page 5

**Exercice 2 — 3, seconde méthode.** L’espace $M_{n,p}(\mathbb R)$ est de dimension finie $np$ ; toutes ses normes sont équivalentes.

**4. Sphères unités.**
$$S_f(0,1)=\left\{C:\sum_{i,j=1}^2|c_{ij}|=1\right\},\qquad S_g(0,1)=\{D:\max_{i,j}|d_{ij}|=1\}.$$
Chaque définition vaut 0,5 point. Exemples proposés (0,5 point chacun) :
$$C=\begin{pmatrix}1/4&1/4\\1/4&1/4\end{pmatrix},\qquad D=\begin{pmatrix}0&1/4\\1&0\end{pmatrix}.$$

### Exercice 3 — Un peu de topologie dans R (6 points)

Pour $a\in\mathbb R$, on pose $I_1=]a,+\infty[$ et $I_2=[0,1[\cup]1,2]\cup\{3\}$.
1. Déterminer s’ils sont ouverts, fermés ou aucun des deux, par les définitions ou les suites (2 points).
2. Déterminer $\overline I_1$ et $\mathring I_2$ (4 points).

**1. $I_1$ est ouvert.** Pour $x>a$, le rayon $r=x-a$ est positif et $B(x,r)=]a,2x-a[\subset I_1$ (0,5 point). Il n’est pas fermé : $a+1/n\in I_1$ tend vers $a\notin I_1$.

## Page 6

**Exercice 3 — 1, suite.** La non-fermeture de $I_1$ vaut 0,5 point.

**$I_2$ n’est pas ouvert.** Pour tout $r>0$, $3+r/2\in B(3,r)\setminus I_2$ (0,5 point). **Il n’est pas fermé** : $1-1/n\in I_2$ pour $n>2$, mais cette suite tend vers $1\notin I_2$ (0,5 point).

**2. Adhérence de $I_1$.** Proposer le candidat $C=[a,+\infty[$ (étape 1 : 0,5 point). C’est un fermé contenant $I_1$, donc $\overline I_1\subset C$ (étape 2 : 0,5 point). Le seul point ajouté est $a$, limite de la suite $a+1/n\in I_1$. Ainsi $a\in\overline I_1$ et $C\subset\overline I_1$ (étape 3 : 1 point). Finalement,
$$\overline I_1=[a,+\infty[.$$

## Page 7

**Exercice 3 — 2, intérieur de $I_2$.** Proposer $C=]0,1[\cup]1,2[$ (étape 1 : 0,5 point). C’est une union d’ouverts incluse dans $I_2$, donc $C\subset\mathring I_2$ (étape 2 : 0,5 point).

Les points de $I_2\setminus C$ sont $0,2,3$. Aucun n’est intérieur : pour tout $r>0$, le point $-r/2$ est dans $B(0,r)\setminus I_2$ ; près de $2$, le point $2+\min(r/2,1/2)$ est dans la boule et dans $]2,3[$, donc hors de $I_2$ ; près de $3$, on prend $3+r/2$. Ainsi $\mathring I_2\subset C$ (étape 3 : 1 point), et
$$\mathring I_2=]0,1[\cup]1,2[.$$
Le PDF emploie accidentellement $I_1$ et $B(b,r)$ dans des lignes concernant ici $I_2$ et la boule centrée en zéro.

**Barème final :** 0,5 point pour chacun des deux résultats $\mathring I_2$ et $\overline I_1$ donné sans justification ou accompagné d’une démonstration fausse.
