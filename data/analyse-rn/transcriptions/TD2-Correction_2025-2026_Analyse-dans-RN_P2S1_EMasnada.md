---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 23 à 31 (ancienne correction, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD2 — Ouverts et fermés (corrigé)

## Exercice 1 : Boules et ouverts

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

## Exercice 2 : Ouverts, fermés, les deux ou aucun des deux

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

## Exercice 3 : Ensemble ouvert et majoré

**Énoncé.** Soit $A$ un ouvert majoré de $(\mathbb{R}, |\cdot|)$. Montrer que $A$ ne contient pas son majorant.

**Correction.** Montrons plus précisément qu'**aucun majorant** de $A$ n'appartient à $A$ ; en particulier $A$ ne contient pas sa borne supérieure (et n'a donc pas de plus grand élément).

Par l'absurde, supposons qu'un majorant $M$ de $A$ appartienne à $A$. Comme $A$ est ouvert, $A$ est un voisinage de $M$ : il existe $\alpha > 0$ tel que
$$B(M, \alpha) = \,]M - \alpha, M + \alpha[\, \subset A$$
En particulier $M + \frac{\alpha}{2} \in A$. Mais $M + \frac{\alpha}{2} > M$, ce qui contredit le fait que $M$ majore $A$. Donc aucun majorant de $A$ n'est dans $A$.

> **Erreurs corrigées :** l'ancienne correction proposait d'abord une « méthode 1 » fausse : elle affirmait qu'un ouvert de $\mathbb{R}$ est de la forme $]\alpha, \beta[$ (c'est faux, par exemple $]0, 1[\, \cup \,]2, 3[$), puis que $A = \,]-M, M[$. Elle a été retirée. Dans la méthode 2, « $M + \alpha \subset A$ » est remplacé par « $M + \frac{\alpha}{2} \in A$ » : $M + \alpha$ n'est pas dans la boule ouverte $]M - \alpha, M + \alpha[$.
