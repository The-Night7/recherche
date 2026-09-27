---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 44 à 49 (ancienne correction, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD4 — Suites et topologie (corrigé)

## Exercice 1 : Valeurs d'adhérence

**Énoncé.** Donner des exemples de suites ayant :

1. aucune valeur d'adhérence ;
2. une unique valeur d'adhérence ;
3. deux valeurs d'adhérence ;
4. trois valeurs d'adhérence ;
5. une unique valeur d'adhérence mais la suite ne converge pas.

**Correction.** Rappel : $\ell$ est une valeur d'adhérence de $(x_n)$ s'il existe une application $\varphi : \mathbb{N} \to \mathbb{N}$ strictement croissante telle que $x_{\varphi(n)} \to \ell$.

**1.** $x_n = n$ (ou, dans $\mathbb{R}^2$, $x_n = (2n, \frac{1}{n})$) : toute suite extraite tend vers $+\infty$, aucune ne converge.

**2.** Toute suite convergente convient, par exemple $x_n = \frac{1}{n}$ : toutes ses suites extraites tendent vers $0$.

**3.** $x_n = (-1)^n$ : les termes pairs valent $1$, les impairs $-1$. Les valeurs d'adhérence sont $1$ et $-1$.

**4.** $x_{2n} = (-1)^n$ et $x_{2n+1} = 3$, soit $1, 3, -1, 3, 1, 3, -1, \dots$ Les valeurs d'adhérence sont $1$, $-1$ et $3$ (suites extraites $x_{4n}$, $x_{4n+2}$ et $x_{2n+1}$).

**5.** $x_{2n} = 0$ et $x_{2n+1} = n$. La suite extraite des termes pairs tend vers $0$. Une suite extraite convergente ne peut contenir qu'un nombre fini de termes impairs (ceux-ci tendent vers $+\infty$), donc elle tend vers $0$ : $0$ est l'unique valeur d'adhérence. Mais la suite n'est pas bornée, donc ne converge pas.

> **Remarque :** en dimension finie, une suite **bornée** qui a une unique valeur d'adhérence converge. L'exemple 5 est donc forcément une suite non bornée.

## Exercice 2 : Suites dont la différence tend vers 0

**Énoncé.** Soient $(u_n)$ et $(v_n)$ deux suites réelles telles que $u_n - v_n$ converge vers $0$. Montrer que si $(u_n)$ et $(v_n)$ admettent des valeurs d'adhérence, alors les valeurs d'adhérence de $(u_n)$ et $(v_n)$ sont les mêmes.

**Correction.** Posons $z_n = u_n - v_n$, qui tend vers $0$.

Soit $\ell$ une valeur d'adhérence de $(u_n)$ : il existe $\varphi$ strictement croissante telle que $u_{\varphi(n)} \to \ell$. La suite extraite $z_{\varphi(n)}$ d'une suite qui converge vers $0$ converge aussi vers $0$. Donc
$$v_{\varphi(n)} = u_{\varphi(n)} - z_{\varphi(n)} \longrightarrow \ell - 0 = \ell$$
et $\ell$ est une valeur d'adhérence de $(v_n)$.

En échangeant les rôles de $u$ et $v$ (car $v_n - u_n = -z_n \to 0$ aussi), toute valeur d'adhérence de $(v_n)$ est une valeur d'adhérence de $(u_n)$. Les deux suites ont donc les mêmes valeurs d'adhérence.

> **Erreur corrigée :** l'ancienne correction écrivait $0 = \ell - \lim v_{\varphi(n)}$, ce qui suppose que $\lim v_{\varphi(n)}$ existe, alors que c'est justement ce qu'il faut démontrer. On l'obtient en écrivant $v_{\varphi(n)}$ comme différence de deux suites convergentes.

## Exercice 3 : Ouverts, fermés et adhérence par les suites

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
