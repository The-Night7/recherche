---
source: "PREING2-S2/Ondes/CM-Chapitre3_2022-2023_Ondes_P2S2_ABoumiz.pdf"
pages: 15
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle des quinze pages et comparaison des deux versions ; matrices, modes et erreurs de la source vérifiés
---

# Ondes — Chapitre 3 : oscillations couplées et modes normaux — 2022–2023

## I. Deux oscillateurs couplés (pages 1 à 4)

Deux blocs de masses $m_1,m_2$ sont posés sur un plan horizontal et reliés par un ressort idéal de raideur $k$, de longueur au repos $L_0$. On néglige les frottements.



### Forces et équations du mouvement (page 2)

$$\vec F_1=k(x_2-x_1)\vec u_x,\qquad \vec F_2=k(x_1-x_2)\vec u_x.$$

La deuxième loi de Newton donne

$$\begin{cases}m_1\ddot x_1=k(x_2-x_1),\\m_2\ddot x_2=k(x_1-x_2).\end{cases}$$

> Ces formules utilisent implicitement des déplacements mesurés par rapport à l’équilibre. Avec des abscisses absolues, l’allongement du ressort serait $x_2-x_1-L_0$.

En posant $\omega_1^2=k/m_1$ et $\omega_2^2=k/m_2$,

$$\frac{d^2}{dt^2}\begin{pmatrix}x_1\\x_2\end{pmatrix}
=\begin{pmatrix}-\omega_1^2&\omega_1^2\\\omega_2^2&-\omega_2^2\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}.\tag{*}$$

Pour résoudre le système, on cherche les modes propres, ou modes normaux.

### Recherche des modes propres (page 3)

$$\begin{pmatrix}x_1\\x_2\end{pmatrix}
=e^{i\omega t}\begin{pmatrix}A\\B\end{pmatrix},\qquad
\frac{d^2}{dt^2}\begin{pmatrix}x_1\\x_2\end{pmatrix}
=-\omega^2\begin{pmatrix}x_1\\x_2\end{pmatrix}.$$

La source note

$$M=\begin{pmatrix}-\omega_1^2&\omega_1^2\\\omega_2^2&-\omega_2^2\end{pmatrix}.$$

On doit avoir

$$M\begin{pmatrix}A\\B\end{pmatrix}=-\omega^2\begin{pmatrix}A\\B\end{pmatrix}.$$

Le vecteur non nul $(A,B)^T$ est donc un vecteur propre de $M$ de valeur propre $-\omega^2$, d’où $\det(M+\omega^2I)=0$.

> Attention aux notations : $M$ désigne ici la matrice dynamique. Dans la section suivante, la même lettre désigne la matrice des masses.

### Déterminant et pulsations (page 4)

$$\begin{aligned}
0&=\det\begin{pmatrix}-\omega_1^2+\omega^2&\omega_1^2\\\omega_2^2&-\omega_2^2+\omega^2\end{pmatrix}\\
&=(-\omega_1^2+\omega^2)(-\omega_2^2+\omega^2)-\omega_1^2\omega_2^2\\
&=\omega^4-\omega_1^2\omega^2-\omega_2^2\omega^2\\
&=\omega^2(\omega^2-\omega_1^2-\omega_2^2).
\end{aligned}$$

Ainsi $\omega^2=0$ ou $\omega^2=\omega_1^2+\omega_2^2$.

La diapositive commence ensuite une « solution générale » par

$$\begin{pmatrix}x_1\\x_2\end{pmatrix}
=(A_+e^{i\omega_+t}+B_+e^{-i\omega_+t})\vec V_+
+\bigl(A_-e^{i\omega_-t}+\cdots\bigr),$$

mais la ligne source s’arrête après le dernier signe $+$. Les points de suspension et la parenthèse fermante ci-dessus signalent cette interruption et ne restituent pas une partie lisible.

> **Mode nul à traiter séparément :** pour $\omega=0$, les deux exponentielles sont identiques. La coordonnée correspondante vérifie $\ddot\alpha=0$ et sa solution générale est $a+bt$. Une écriture complète peut donc utiliser $(a+bt)(1,1)^T$ pour la translation uniforme, plus un mode oscillant de pulsation $\sqrt{\omega_1^2+\omega_2^2}$ et de vecteur propre proportionnel à $(\omega_1^2,-\omega_2^2)^T$. Ce complément n’est pas imprimé sur la diapositive.

## II. N oscillateurs couplés (page 5)

Les équations du mouvement de $n$ oscillateurs couplés linéairement sont

$$M\frac{d^2\vec X}{dt^2}+k\vec X=\vec0,
\qquad\vec X=(x_1,x_2,\ldots,x_n)^T.$$

Le couplage linéaire provient d’un potentiel polynomial d’ordre 2 :

$$V(\vec X)=\sum_{i,j}k^{i,j}x_ix_j.$$

Puisque $x_ix_j=x_jx_i$, la source indique que $k$ est symétrique. La matrice de masse est la matrice diagonale symétrique d’ordre $n$,

$$M=\begin{pmatrix}M_1&0&\cdots\\0&M_2&\cdots\\\vdots&\vdots&\ddots\end{pmatrix}.$$

> La partie antisymétrique des coefficients ne contribue pas à la forme quadratique ; on peut donc choisir une matrice symétrique. Pour employer la même matrice de raideur dans l’équation et dans le potentiel, la convention usuelle est $V=\frac12\vec X^TK\vec X$. Le facteur $1/2$ manque dans la formule de la diapositive si son $k$ est la matrice de raideur.

## II.1. Méthodes générales (pages 6 et 7)

L’équation s’écrit

$$\ddot{\vec X}+M^{-1}K\vec X=\vec0.$$

Le cours suppose un ensemble complet de vecteurs propres orthonormés $(\vec Y_i)_{i=1}^n$ de $M^{-1}K$ :

$$M^{-1}K\vec Y_i=\lambda_i\vec Y_i,\qquad
\vec Y_i^{\,T}\vec Y_j=\delta_{ij}
=\begin{cases}0&i\ne j,\\1&i=j.\end{cases}$$

Il existe alors des fonctions $\alpha_j(t)$ telles que

$$\vec X=\sum_{j=1}^n\alpha_j\vec Y_j.$$

En remplaçant dans l’équation,

$$\sum_{j=1}^n\ddot\alpha_j\vec Y_j+
\sum_{j=1}^n\alpha_jM^{-1}K\vec Y_j=\vec0,$$

puis

$$\sum_{j=1}^n(\ddot\alpha_j+\lambda_j\alpha_j)\vec Y_j=\vec0.$$

Donc, pour tout $j$,

$$\ddot\alpha_j+\lambda_j\alpha_j=0.$$

Les $\alpha_j$ sont les **coordonnées normales**. Pour $\lambda_j>0$, elles se comportent comme des oscillateurs harmoniques simples de pulsation $\omega_j=\sqrt{\lambda_j}$.

Remarques de la source : les $\vec Y_i$ forment une base de $\mathbb R^n$ ; on ne peut pas être certain que $\lambda_j>0$.

> **Hypothèse d’orthonormalité à préciser :** $M^{-1}K$ n’est pas généralement symétrique pour le produit scalaire euclidien, même si $M$ et $K$ sont symétriques. Pour des masses positives, on diagonalise la matrice symétrique $M^{-1/2}KM^{-1/2}$, ou on choisit les modes orthonormés pour le produit scalaire pondéré $u^TMv$. Les projections euclidiennes ci-dessous supposent donc une situation particulière, par exemple des masses égales, ou des coordonnées déjà normalisées.

## II.2. Valeurs initiales (page 8)

On résout $\ddot{\vec X}+M^{-1}K\vec X=\vec0$ avec

$$\vec X(0)=\vec X_0,\qquad\dot{\vec X}(0)=\vec V_0.$$

La source écrit $\alpha_j(t)=\vec Y_j^{\,T}\vec X(t)$.

La diapositive donne ensuite

$$\alpha_j(t)=\vec Y_j^{\,T}\vec X_0,\qquad
\dot\alpha_j(t)=\vec Y_j^{\,T}\vec V_0.$$

> **Argument temporel erroné :** ces deux égalités définissent $\alpha_j(0)$ et $\dot\alpha_j(0)$, et non leurs valeurs à tout instant $t$. Avec des modes normalisés pour le produit scalaire de masse, les projections correspondantes comportent en outre le facteur $M$.

## II.3. Frottements (page 9)

Avec une matrice de frottement $\Gamma$,

$$\ddot{\vec X}+\Gamma\dot{\vec X}+M^{-1}K\vec X=\vec0.\tag{**}$$

On pose $\vec X(t)=e^{-i\omega t}\vec X(0)$, où $\vec X(0)$ est indépendant du temps. On obtient

$$(-\omega^2I-i\omega\Gamma+M^{-1}K)\vec X(0)=\vec0,$$

avec $I$ la matrice identité. Pour un mode non nul, $\vec X(0)$ est un vecteur propre de valeur propre nulle de $-\omega^2I-i\omega\Gamma+M^{-1}K$.

## II.4. Oscillations entretenues (pages 10 et 11)

Sous l’action d’une force extérieure $\vec F(t)$,

$$\ddot{\vec X}+\Gamma\dot{\vec X}+M^{-1}K\vec X=M^{-1}\vec F(t).$$

On suppose $\vec F(t)=\vec F_0e^{-i\omega_dt}$. Si la force n’oscille pas dans la même direction sur toutes les composantes, le cours propose d’utiliser le principe de superposition.

En posant $\vec X(t)=\vec A e^{-i\omega_dt}$, la source affiche

$$\vec A=(-\omega^2I-i\omega\Gamma+M^{-1}K)^{-1}\vec F_0.\tag{source}$$

> **Facteur manquant :** avec le second membre affiché à la page précédente, il faut

$$\vec A=(-\omega_d^2I-i\omega_d\Gamma+M^{-1}K)^{-1}M^{-1}\vec F_0.$$

> La formule source emploie ici $\omega$ alors que l’excitation est notée $\omega_d$.

**Remarque 1 de la source :** si $-\omega^2I-i\omega\Gamma+M^{-1}K$ n’est pas inversible, il y a résonance.

> Cette singularité caractérise une fréquence propre de l’opérateur considéré. La réponse forcée résonante dépend aussi du couplage de la force au mode ; avec amortissement, un maximum de réponse peut exister sans singularité pour une pulsation réelle.

**Remarque 2 :** la solution générale est la somme de la solution générale de l’équation homogène et d’une solution particulière, par exemple $\vec A e^{-i\omega_dt}$ lorsqu’elle existe.

## Rappels : oscillateurs simple, amorti et entretenu (pages 11 à 13)

### Oscillateur harmonique simple

$$\ddot X+\omega^2X=0,\qquad X(t)=A\cos(\omega t)+B\sin(\omega t).$$

$\omega$ est la pulsation.

### Avec friction

$$\ddot X+\Gamma\dot X+\omega_0^2X=0.$$

Les trois formes données sont :

| Régime | Solution $x(t)$ | Pulsation ou paramètre |
| --- | --- | --- |
| Surcritique, apériodique | $e^{-\Gamma t/2}(Ae^{\omega t}+Be^{-\omega t})$ | $\omega=\sqrt{\Gamma^2/4-\omega_0^2}$ |
| Critique | $e^{-\Gamma t/2}(A+Bt)$ | $\Gamma^2/4=\omega_0^2$ |
| Sous-critique, pseudo-périodique | $e^{-\Gamma t/2}[A\cos(\omega t)+B\sin(\omega t)]$ | $\omega=\sqrt{\omega_0^2-\Gamma^2/4}$ |

### Oscillateur entretenu

$$\ddot X+\Gamma\dot X+\omega_0^2X=\frac{F(t)}{M}.$$

La solution générale est $X_0(t)+X_F(t)$, où $X_0$ est la solution générale de l’équation homogène et $X_F$ une solution particulière de l’équation avec force.

## Rappel : système de N oscillateurs (page 14)

$$M\frac{d^2\vec X}{dt^2}+k\vec X=\vec0,
\qquad \vec X=(x_1,\ldots,x_n)^T.$$

$M$ est la matrice de masse. Le cours affiche

$$\vec X(t)=\sum_{j=1}^n(A_je^{i\omega_jt}+B_je^{-i\omega_jt})\vec V_j,$$

et les modes propres

$$\vec X_j^{\,\pm}=e^{\pm i\omega_jt}\vec V_j.$$

> La diapositive appelle $\omega_j$ la valeur propre de $M^{-1}K$ ; il faut lire $\omega_j^2$, en accord avec la page 7. Cette écriture oscillante suppose les valeurs propres strictement positives. Les valeurs nulles ou négatives demandent respectivement des solutions affines ou exponentielles réelles.

La page 15 est blanche.
