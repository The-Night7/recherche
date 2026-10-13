---
source: PREING2-S2/Algebre-lineaire/Synthese_Trigonalisation_Espaces_Prehilbertiens.docx
transcription: manuelle
format_source: docx
verification: lecture intégrale du texte et des tableaux Word
---

# Synthèse complète : trigonalisation et espaces préhilbertiens

Ce document rassemble les fiches de cours, méthodes pratiques, exemples détaillés et propriétés fondamentales pour la trigonalisation et les espaces préhilbertiens.

## Fiche 1 — Méthode pratique de trigonalisation

### 1. Cadre théorique et critère fondamental

Soit $E$ un $\mathbb K$-espace vectoriel de dimension finie $n$, et $u\in\mathcal L(E)$, ou $A\in\mathcal M_n(\mathbb K)$.

**Définition.** $u$ est trigonalisable s’il existe une base de $E$ dans laquelle sa matrice est triangulaire supérieure.

**Théorème fondamental.** $u$ est trigonalisable sur $\mathbb K$ si et seulement si son polynôme caractéristique $\chi_u(X)$ est scindé sur $\mathbb K$.

**Cas complexe.** Tout endomorphisme d’un espace vectoriel complexe de dimension finie est trigonalisable, car tout polynôme y est scindé.

### 2. Algorithme général pas à pas

1. Calculer $\chi_A(X)=\det(XI-A)$ et déterminer les valeurs propres $\lambda_i$ et leurs multiplicités algébriques $m_i$.
2. Résoudre $(A-\lambda_iI)X=0$ pour obtenir une base de chaque sous-espace propre $E_{\lambda_i}$.
3. Si $\sum_i\dim E_{\lambda_i}<n$, la matrice n’est pas diagonalisable. Compléter la famille libre de vecteurs propres à l’aide des noyaux itérés $\ker((A-\lambda I)^2),\ldots$, ou en résolvant $Av_k=\lambda v_k+v_{k-1}$.
4. Poser $P=(v_1\mid\cdots\mid v_n)$. La matrice triangulaire est $T=P^{-1}AP$.

### 3. Exemple dans $\mathcal M_3(\mathbb R)$

$$A=\begin{pmatrix}-2&2&-1\\-1&1&-1\\-1&2&-2\end{pmatrix}.$$

$$\chi_A(X)=(X+1)^3.$$

La seule valeur propre est $-1$, de multiplicité 3. La résolution de $(A+I)X=0$ donne $-x+2y-z=0$. Ainsi, $\dim E_{-1}=2$, et une base est

$$v_1=(2,1,0)^{\mathsf T},\qquad v_2=(-1,0,1)^{\mathsf T}.$$

Le vecteur complémentaire $v_3=(1,0,0)^{\mathsf T}$ n’appartient pas à $E_{-1}$ et vérifie

$$Av_3=(-2,-1,-1)^{\mathsf T}=-v_1-v_2-v_3.$$

La matrice triangulaire dans cette base est

$$T=\begin{pmatrix}-1&0&-1\\0&-1&-1\\0&0&-1\end{pmatrix}.$$

## Fiche 2 — Espaces préhilbertiens réels

### 1. Définitions fondamentales

Un produit scalaire sur un espace vectoriel réel $E$ est une forme bilinéaire symétrique, définie et positive :

$$\langle x,y\rangle=\langle y,x\rangle,\qquad
\forall x\ne0,\quad\langle x,x\rangle>0.$$

Un espace vectoriel muni d’un produit scalaire est un espace préhilbertien réel ; il est dit euclidien si sa dimension est finie.

### 2. Norme et inégalités majeures

La norme associée est $\|x\|=\sqrt{\langle x,x\rangle}$.

**Cauchy–Schwarz :**

$$|\langle x,y\rangle|\leq\|x\|\,\|y\|,$$

avec égalité si et seulement si $x$ et $y$ sont colinéaires.

**Minkowski, ou inégalité triangulaire :**

$$\|x+y\|\leq\|x\|+\|y\|,$$

avec égalité si et seulement si les vecteurs sont positivement liés, en incluant le cas où l’un est nul.

**Pythagore :**

$$x\perp y\iff\|x+y\|^2=\|x\|^2+\|y\|^2.$$

**Identité du parallélogramme :**

$$\|x+y\|^2+\|x-y\|^2=2(\|x\|^2+\|y\|^2).$$

**Identité de polarisation :**

$$\langle x,y\rangle=\frac14\bigl(\|x+y\|^2-\|x-y\|^2\bigr).$$

### 3. Orthogonalité

Deux vecteurs sont orthogonaux si $\langle x,y\rangle=0$. Pour tout sous-espace $F$ de dimension finie dans $E$,

$$E=F\oplus F^\perp,\qquad(F^\perp)^\perp=F.$$

## Fiche 3 — Procédé de Gram–Schmidt et bases orthonormales

### 1. Théorème d’orthonormalisation

Toute famille libre $(v_1,\ldots,v_p)$ d’un espace préhilbertien engendre une unique famille orthonormale $(e_1,\ldots,e_p)$ telle que, pour tout $k$,

$$\operatorname{Vect}(e_1,\ldots,e_k)=\operatorname{Vect}(v_1,\ldots,v_k),\qquad
\langle v_k,e_k\rangle>0.$$

### 2. Formules récurrentes

**Orthogonalisation :**

$$u_1=v_1,\qquad u_k=v_k-\sum_{i=1}^{k-1}\frac{\langle v_k,u_i\rangle}{\|u_i\|^2}u_i.$$

**Normalisation :** $e_k=u_k/\|u_k\|$.

### 3. Exemple dans $\mathbb R^3$

Soit $v_1=(1,1,0)$, $v_2=(1,0,1)$, $v_3=(0,1,1)$.

**Vecteur 1 :**

$$u_1=(1,1,0),\qquad\|u_1\|=\sqrt2,\qquad e_1=\frac1{\sqrt2}(1,1,0).$$

**Vecteur 2 :**

$$\langle v_2,u_1\rangle=1,\qquad
u_2=(1,0,1)-\frac12(1,1,0)=\left(\frac12,-\frac12,1\right),$$

$$\|u_2\|=\frac{\sqrt6}{2},\qquad e_2=\frac1{\sqrt6}(1,-1,2).$$

**Vecteur 3 :**

$$\langle v_3,u_1\rangle=1,\qquad\langle v_3,u_2\rangle=\frac12,$$

$$u_3=\left(-\frac23,\frac23,\frac23\right),\qquad
\|u_3\|=\frac{2\sqrt3}{3},\qquad e_3=\frac1{\sqrt3}(-1,1,1).$$
