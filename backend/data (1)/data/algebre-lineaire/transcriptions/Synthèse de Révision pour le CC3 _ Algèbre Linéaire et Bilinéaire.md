---
source: PREING2-S2/Algebre-lineaire/Synthèse de Révision pour le CC3 _ Algèbre Linéaire et Bilinéaire.docx
transcription: manuelle
format_source: docx
verification: lecture intégrale du texte et des tableaux Word
---

# Synthèse de révision pour le CC3 — Algèbre linéaire et bilinéaire

## 1. Systèmes différentiels linéaires du premier ordre

La résolution repose sur la réduction de l’opérateur linéaire associé pour découpler les équations du système.

### Mise sous forme matricielle

$$X'(t)=AX(t)+B(t),$$

où $X(t)$ est le vecteur colonne des fonctions inconnues, $A\in\mathcal M_n(\mathbb R)$ la matrice des coefficients constants et $B(t)$ le second membre. Le système est homogène lorsque $B(t)=0$.

### Résolution par changement de variable

Si $A$ est diagonalisable sur $\mathbb R$, il existe $P\in\mathrm{GL}_n(\mathbb R)$ telle que $A=PDP^{-1}$. On pose $Y(t)=P^{-1}X(t)$, soit $X(t)=PY(t)$.

Le système devient

$$Y'(t)=DY(t)+P^{-1}B(t).$$

Dans le cas homogène,

$$Y(t)=\bigl(c_1e^{\lambda_1t},\ldots,c_ne^{\lambda_nt}\bigr)^{\mathsf T}.$$

Les colonnes de $P$ sont les vecteurs propres : $P=(v_1\mid\cdots\mid v_n)$. La solution générale est

$$X(t)=Pe^{tD}C=\sum_{i=1}^nc_ie^{\lambda_it}v_i.$$

Pour le cas non homogène, on applique la méthode de variation de la constante. La diagonalisation constitue le cœur de l’étude algébrique suivante.

## 2. Réduction des endomorphismes — Fondements

Avant les calculs de réduction sur $\mathbb K$, vérifier que le polynôme caractéristique est scindé sur $\mathbb K$.

### Définitions et outils

La convention du document est

$$\chi_f(\lambda)=\det(f-\lambda\operatorname{id}_E).$$

Ses racines constituent le spectre $\operatorname{Sp}(f)$.

$\lambda$ est une valeur propre s’il existe $v\ne0_E$ tel que $f(v)=\lambda v$. Un vecteur propre est donc toujours non nul.

$$E_\lambda=\ker(f-\lambda\operatorname{id}_E)$$

est l’ensemble des vecteurs propres associés à $\lambda$, augmenté du vecteur nul.

### Conditions de diagonalisation

$f$ est diagonalisable si et seulement si $\chi_f$ est scindé sur $\mathbb K$ et, pour chaque $\lambda\in\operatorname{Sp}(f)$,

$$\dim E_\lambda=m_\lambda,$$

où $m_\lambda$ est sa multiplicité dans $\chi_f$.

**Réflexe TD1 :** 0 est valeur propre de $f$ si et seulement si $f$ n’est pas bijectif, soit $\det A=0$ en dimension finie.

## 3. Formes bilinéaires et produits scalaires

### Représentation matricielle

Soit $\phi$ une forme bilinéaire sur $E$, et $\mathcal B$ une base de $E$. Il existe une unique matrice $A\in\mathcal M_n(\mathbb R)$ telle que

$$\phi(x,y)=X^{\mathsf T}AY,$$

où $X,Y$ sont les colonnes de coordonnées dans $\mathcal B$. Préciser la base utilisée : la matrice en dépend, piège signalé pour le DS3.

### Conditions du produit scalaire réel

- Bilinéarité : linéarité à gauche et à droite.
- Symétrie : $\langle x,y\rangle=\langle y,x\rangle$, donc $A=A^{\mathsf T}$.
- Positivité : $\langle x,x\rangle\geq0$ pour tout $x$.
- Caractère défini : $\langle x,x\rangle=0\Rightarrow x=0_E$.

### Exemples de référence

Sur $\mathbb R^2$, DS3 exercice 2 :

$$\phi(x,y)=(x_1+x_2)(y_1+y_2)+x_1y_1+x_2y_2.$$

Sur $\mathbb R_2[X]$, DS3 exercice 4 :

$$\langle P,Q\rangle=\int_0^1xP(x)Q(x)\,dx.$$

La norme associée est $\|x\|=\sqrt{\langle x,x\rangle}$.

## 4. Espaces euclidiens et orthogonalité

Un espace euclidien est un espace vectoriel réel de dimension finie muni d’un produit scalaire.

### Orthogonalité et supplémentarité

$$F^\perp=\{x\in E\mid\forall y\in F,\ \langle x,y\rangle=0\}.$$

$$F\cap F^\perp=\{0_E\},\qquad E=F\oplus F^\perp,\qquad
\dim F^\perp=\dim E-\dim F.$$

### Bases orthonormales

$(e_1,\ldots,e_n)$ est orthonormale si $\langle e_i,e_j\rangle=\delta_{ij}$. Les vecteurs sont de norme 1 et orthogonaux deux à deux. Pour orthonormaliser une base, on utilise le procédé de Gram–Schmidt.

## 5. Méthodologie et points de vigilance

### Tableau de synthèse rédactionnelle

| Erreur classique (DS3/TD) | Réflexe correct |
| --- | --- |
| Inclure $0_E$ dans les vecteurs propres | Préciser $v\ne0_E$ |
| Chercher les éléments propres à tâtons | Calculer $\chi_f$ et vérifier s’il est scindé |
| Oublier la symétrie pour un produit scalaire | Vérifier que $A$ est symétrique |
| Négliger la dimension finie pour $F\oplus F^\perp$ | Mentionner que l’espace est euclidien |
| Utiliser $\|x\|=\sqrt{\sum x_i^2}$ par défaut | La norme dépend du produit scalaire défini par l’énoncé |

### Astuces de vérification

**Trace et déterminant, TD1 exercice 15.** Les valeurs propres sont comptées avec leurs multiplicités :

$$\operatorname{Tr}A=\sum_{i=1}^n\lambda_i,\qquad\det A=\prod_{i=1}^n\lambda_i.$$

**Théorème du rang :**

$$\dim E_\lambda=n-\operatorname{rg}(A-\lambda I).$$

### Détermination de $F^\perp$

Si $F=\operatorname{Vect}(u_1,\ldots,u_k)$, alors

$$x\in F^\perp\iff\forall i\in\{1,\ldots,k\},\quad\langle x,u_i\rangle=0.$$

Cela conduit à un système linéaire sur les coordonnées de $x$. Si $E=\mathbb R_n[X]$, les inconnues sont les coefficients du polynôme.
