---
source: "PREING2-S2/Algebre-lineaire-DS/cc-2025-2026/CC3_Algebre_lineaire_bilineaire_refait.pdf"
archive: "cc 2025 2026.zip"
pages: 3
semestre: "P2S2"
transcription: texte natif restructuré et contrôlé sur le rendu PDF
transcription_date: 2026-11-01
verification: comparaison du texte extrait avec le rendu des pages du PDF fourni
---

# CC3 Algebre lineaire bilineaire refait

## Notes de transcription

> Exercice 1, question 3 b : l’énoncé omet l’hypothèse que les vecteurs sont non nuls. Une famille orthogonale contenant le vecteur nul n’est pas libre. L’énoncé est conservé.

## Page 1

CY TECH — 2025/2026 — Semestre 2, PréIng2 — Jeudi 28 mai 2026.

Algèbre linéaire et bilinéaire — CC3. Durée : 120 mn.

Les documents et les supports électroniques sont interdits. L’épreuve est composée d’exercices indépendants. La qualité de la rédaction et la rigueur des justifications seront prises en compte dans la notation.

### Exercice 1 — Le cours

Soit $E$ un $\mathbb R$-espace vectoriel de dimension finie, muni d’un produit scalaire $\langle\cdot,\cdot\rangle$.

1. Rappeler la définition d’un produit scalaire $\langle\cdot,\cdot\rangle$ sur $E$.
2. Soit $A\subset E$, un sous-ensemble de $E$.

   a) Donner la définition de l’orthogonal de $A$ noté $A^\perp$.

   b) Montrer que $A^\perp$ est un sous-espace vectoriel de $E$.

   c) Dans cette question $E=\mathbb R^3$ et $A=\operatorname{Vect}(u_1,u_2)$, avec $u_1=(1,2,-1)$ et $u_2=(0,1,3)$. Déterminer $A^\perp$, pour le produit scalaire canonique.

3. Soit $X=(x_1,\ldots,x_n)$ une famille de vecteurs de $E$.

   a) Donner la définition de : la famille $X$ est orthogonale.

   b) Montrer que si la famille $X$ est orthogonale alors $X$ est libre.

### Exercice 2 — L’orthonormalisation

On considère l’espace euclidien $(\mathbb R^3,\langle\cdot,\cdot\rangle)$, où $\langle\cdot,\cdot\rangle$ est le produit scalaire canonique. On notera $\|\cdot\|$ la norme associée à ce produit scalaire.

Soit $u_1=(1,1,0)$ et $u_2=(1,0,1)$ deux éléments de $\mathbb R^3$.

1. Montrer que la famille $U=(u_1,u_2)$ est libre.
2. Est-ce que la famille $U$ est orthogonale ? Justifier votre réponse.
3. Trouver $v_1\in\mathbb R^3$, tel que : $v_1$ est normé et $\operatorname{Vect}(v_1)=\operatorname{Vect}(u_1)$.

   **Rappel.** $u\in\mathbb R^3$ est dit normé si $\|u\|=1$.

4. Trouver $v_2\in\mathbb R^3$, tel que :

## Page 2

Suite de la question 4 de l’exercice 2 :

- $v_2\perp v_1$ ;
- $v_2$ est normé ;
- et $\operatorname{Vect}(v_1,v_2)=\operatorname{Vect}(u_1,u_2)$.

5. En déduire que $(v_1,v_2)$ forme une famille orthonormée (on dit aussi orthonormale).
6. Trouver $v_3$ tel que $V=(v_1,v_2,v_3)$ forme une base orthonormée de $\mathbb R^3$.

## Page 3

### Exercice 3 — Un système différentiel linéaire

Considérons le système différentiel linéaire homogène à coefficients constants :

$$
\begin{cases}
x'(t)=x(t)-4y(t),\\
y'(t)=x(t)-3y(t).
\end{cases}
$$

Les inconnues sont les fonctions $x$ et $y$ de la variable réelle $t\in\mathbb R$.

1. Écrire ce système sous la forme matricielle $X'(t)=AX(t)$ (I), en explicitant les différentes matrices.
2. Déterminer $X(t)$, la solution générale du système (I).

### Exercice 4 — Un espace euclidien

On travaille dans l’espace vectoriel $\mathbb R_3[X]$ des polynômes à coefficients réels et de degré au plus 3. On considère l’application $\langle\cdot,\cdot\rangle$ définie par

$$
\forall P,Q\in\mathbb R_3[X],\qquad
\langle P,Q\rangle=\int_{-1}^{1}P(x)Q(x)\,dx.
$$

1. Quelle est la dimension de l’espace vectoriel $\mathbb R_3[X]$ ? Justifier votre réponse.
2. Montrer que l’application $\langle\cdot,\cdot\rangle$ est un produit scalaire sur $\mathbb R_3[X]$. On notera $\|\cdot\|$ la norme associée à ce produit scalaire.
3. a) Calculer $\displaystyle\int_{-1}^{1}x^i x^j\,dx$, pour tout $(i,j)\in\llbracket0,3\rrbracket\times\llbracket0,3\rrbracket$. Donner la formule générale.

   b) Calculer $M$, la matrice de $\langle\cdot,\cdot\rangle$ dans la base canonique $\mathcal B=(1,X,X^2,X^3)$ de $\mathbb R_3[X]$.

4. La base canonique est-elle orthonormale pour ce produit scalaire $\langle\cdot,\cdot\rangle$ ? Justifier.
5. On considère $F$, le sous-espace vectoriel de $\mathbb R_3[X]$ engendré par la famille de vecteurs $(1,X)$, i.e. $F=\operatorname{Vect}(1,X)$. Déterminer $F^\perp$.
