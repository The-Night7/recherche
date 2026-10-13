---
source: "PREING2-S2/Fiche de Révision Algèbre.docx"
transcription: texte structuré et relu
transcription_date: 2026-09-30
verification: lecture intégrale des paragraphes et formules natives ; tableaux reconstitués depuis le Word
---

# Fiche de Révision — Algèbre Linéaire et Bilinéaire

## 1. Algèbre Linéaire : Réduction d'Endomorphismes

### A. Éléments propres et Polynôme Caractéristique

- **Polynôme caractéristique** : Pour une matrice $A \in \mathcal{M}_n(\mathbb{K})$, il est défini par $P_A(\lambda) = \det(A - \lambda I_n)$. Ses racines sont exactement les valeurs propres de $A$.

- **Sous-espace propre** : Associé à la valeur propre $\lambda$, c'est $E_\lambda = \ker(A - \lambda I_n)$.

- **Propriétés de la trace et du déterminant** : Si le polynôme caractéristique est scindé, la trace de $A$ est la somme des valeurs propres (avec multiplicité) et le déterminant est leur produit.

### B. Diagonalisation et Trigonalisation

- **Condition suffisante** : Si une matrice de taille $n$ admet $n$ valeurs propres distinctes, elle est diagonalisable.

- **Condition Nécessaire et Suffisante (CNS) de diagonalisation** : Une matrice est diagonalisable si et seulement si son polynôme caractéristique $P_A$ est scindé **ET** pour chaque valeur propre $\lambda$, la dimension de l'espace propre est égale à la multiplicité algébrique de $\lambda$ ($\dim(E_\lambda) = m_\lambda$).

- **Trigonalisation** : Une matrice est trigonalisable si et seulement si son polynôme caractéristique est scindé. **Conséquence** : Dans $\mathbb{C}$, toute matrice est trigonalisable.

## 2. Applications de la Réduction

- **Puissances de matrices** : Si $A = P D P^{-1}$, alors pour tout entier $k$, **$A^k = P D^k P^{-1}$**.

- **Formule du binôme matricielle** : $(A+B)^k = \sum_{i=0}^k \binom{k}{i} A^{k-i} B^i$.

    **Attention** : Cette formule n'est valable **que si $A$ et $B$ commutent** ($AB = BA$). Elle est extrêmement utile pour calculer les puissances en décomposant une matrice $A$ sous la forme $A = \lambda I_n + N$, où $N$ est une matrice nilpotente ($N^p = 0$).

- **Systèmes Différentiels Linéaires ($X'(t) = AX(t)$)** : La résolution passe par un changement de variable. On pose $Y(t) = P^{-1}X(t)$, ce qui amène à résoudre un système plus simple $Y'(t) = D Y(t)$ (ou $T Y(t)$ si trigonalisée). La solution générale utilise l'exponentielle $e^{\lambda t}$, ou directement l'exponentielle de matrice $e^{tA}$.

## 3. Algèbre Bilinéaire : Formes Bilinéaires

### A. Définitions

- **Forme bilinéaire** : Une application $\phi : E \times E \to \mathbb{R}$ linéaire par rapport à chacune de ses deux variables.

- Elle est **symétrique** si $\forall x,y \in E, \phi(x,y) = \phi(y,x)$, et **antisymétrique** si $\phi(x,y) = -\phi(y,x)$.

- Elle est **définie positive** si $\forall x \in E, \phi(x,x) \geq 0$ (positive) et $\phi(x,x) = 0 \implies x = 0$ (définie).

### B. Représentation Matricielle

- Soit une base $B$. Si $X$ et $Y$ sont les vecteurs colonnes des coordonnées de $x$ et $y$, alors **$\phi(x,y) = X^T A Y$**.

- **Congruence (Changement de base)** : Si $P$ est la matrice de passage d'une base $B$ à une base $B'$, la nouvelle matrice de $\phi$ est **$A' = P^T A P$**. *(Ne pas confondre avec la similitude $A' = P^{-1} A P$ utilisée en réduction !)*.

- **Critère de Sylvester** : Une matrice symétrique $A$ est définie positive si et seulement si les déterminants de toutes ses sous-matrices principales (extraites depuis le coin supérieur gauche) sont strictement positifs.

## 4. Espaces Préhilbertiens et Euclidiens

### A. Produit Scalaire et Norme

- **Produit scalaire (p.s.)** : C'est une forme bilinéaire symétrique, positive et définie. On le note souvent $\langle x, y \rangle$.

- Un **espace euclidien** est un espace vectoriel de dimension **finie** muni d'un produit scalaire.

- **Norme associée** : $\|x\| = \sqrt{\langle x, x \rangle}$. Elle caractérise un produit scalaire en vérifiant **l'identité du parallélogramme** : $\|x+y\|^2 + \|x-y\|^2 = 2(\|x\|^2 + \|y\|^2)$.

- **Inégalité de Cauchy-Schwarz** : Absolument incontournable. **$|\langle x, y \rangle| \leq \|x\| \|y\|$**. L'égalité a lieu si et seulement si $x$ et $y$ sont colinéaires (liés).

### B. Orthogonalité

- Deux vecteurs sont **orthogonaux** ($x \perp y$) si $\langle x, y \rangle = 0$.

- **Théorème de Pythagore** : $x \perp y \iff \|x+y\|^2 = \|x\|^2 + \|y\|^2$.

- **Orthogonal d'un sous-espace $F$ ($F^\perp$)** : C'est l'ensemble des vecteurs orthogonaux à *tous* les vecteurs de $F$. En dimension finie, $F$ et $F^\perp$ sont supplémentaires : **$E = F \oplus F^\perp$**. Par conséquent, $F \cap F^\perp = \{0_E\}$ et $\dim(F) + \dim(F^\perp) = \dim(E)$.

### C. Bases Orthonormales et Gram-Schmidt

- Toute famille orthogonale de vecteurs non nuls est libre.

- **Procédé de Gram-Schmidt** : Il permet de fabriquer une base orthogonale $(q_1, \dots, q_p)$ à partir d'une base libre $(v_1, \dots, v_p)$.
    La formule de récurrence à retenir est : **$q_k = v_k - \sum_{i=1}^{k-1} \frac{\langle v_k, q_i \rangle}{\|q_i\|^2} q_i$**. Pour la rendre orthonormale, il suffit ensuite de diviser chaque $q_k$ par sa norme.

- Dans une base orthonormale, le calcul du produit scalaire redevient "usuel" : $\langle x, y \rangle = X^T Y = \sum_{i} x_i y_i$.

> **Précision sur la source :** l’égalité $A^k=PD^kP^{-1}$ est annoncée « pour tout entier $k$ ». Pour $k<0$, il faut en plus que $A$ (donc $D$) soit inversible. Sans cette hypothèse, la formule vaut pour $k\ge0$.
