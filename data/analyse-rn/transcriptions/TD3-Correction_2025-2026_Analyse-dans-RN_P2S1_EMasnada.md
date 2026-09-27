---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 34 à 43 (ancienne correction, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD3 — Intérieur et adhérence (corrigé)

## Exercice 1 : Adhérence et fermé

**Énoncé.** Soit $(E, \|\cdot\|)$ un espace vectoriel normé. Soient $A$ et $B$ deux ensembles tels que $A \subset B \subset E$ et $B$ fermé.

1. Montrer alors que pour tout $x \in \complement_E B$, il existe $r > 0$ tel que $B(x, r) \cap A = \emptyset$.
2. Peut-on alors avoir $\overline{A} = B$ et si oui sous quelles conditions ?

**Correction.**

**1.** $B$ est fermé, donc $\complement_E B$ est ouvert : pour tout $x \in \complement_E B$, il existe $r > 0$ tel que $B(x, r) \subset \complement_E B$, c'est-à-dire $B(x, r) \cap B = \emptyset$. Comme $A \subset B$, on a a fortiori $B(x, r) \cap A = \emptyset$.

**2.** Rappel : $x \in \overline{A} \iff \forall r > 0,\ B(x, r) \cap A \ne \emptyset$.

La question 1 dit exactement qu'aucun point hors de $B$ n'est adhérent à $A$ : $\overline{A} \subset B$. (On retrouve le fait que $\overline{A}$ est le plus petit fermé contenant $A$.) Mais $B$ peut être trop grand. On a $\overline{A} = B$ si et seulement si tout point de $B$ est adhérent à $A$, c'est-à-dire :
$$\forall x \in B \setminus A,\quad \forall r > 0,\quad B(x, r) \cap A \ne \emptyset$$
Par exemple, avec $A = \,]0, 1[$ : $B = [0, 1]$ convient, mais pas $B = [0, 2]$ (le point $2$ n'est pas adhérent à $A$).

## Exercice 2 : Intérieur et ouvert

**Énoncé.** Soit $(E, \|\cdot\|)$ un espace vectoriel normé. Soient $A$ et $B$ deux ensembles tels que $B \subset A \subset E$ et $B$ ouvert.

1. Montrer alors que pour tout $x \in B$, il existe $r > 0$ tel que $B(x, r) \subset A$.
2. Peut-on alors avoir $\mathring{A} = B$ et si oui sous quelles conditions ?

**Correction.**

**1.** $B$ est ouvert : pour tout $x \in B$, il existe $r > 0$ tel que $B(x, r) \subset B$. Comme $B \subset A$, on a $B(x, r) \subset A$.

**2.** Rappel : $x \in \mathring{A} \iff \exists r > 0,\ B(x, r) \subset A$.

La question 1 montre que tout point de $B$ est intérieur à $A$ : $B \subset \mathring{A}$. (On retrouve le fait que $\mathring{A}$ est le plus grand ouvert contenu dans $A$.) Mais $B$ peut être trop petit. On a $\mathring{A} = B$ si et seulement si aucun point de $A \setminus B$ n'est intérieur à $A$ :
$$\forall x \in A \setminus B,\quad \forall r > 0,\quad B(x, r) \not\subset A$$
Par exemple, avec $A = [0, 1]$ : $B = \,]0, 1[$ convient, mais pas $B = \,]0, \frac{1}{2}[$ (le point $\frac{3}{4}$ est intérieur à $A$).

## Exercice 3 : Intérieur et adhérence d'une boule

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

## Exercice 4 : Intérieur et adhérence des ensembles du TD2

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
