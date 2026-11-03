---
source: "PREING2-S1/Analyse-dans-RN-DS/DS3-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_EMasnada.pdf"
pages: 9
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Analyse dans Rn — Examen final 2023–2024 : EDP, changements de variables et classe C2

## Page 1

### Préing 2 — Examen final d’Analyse dans Rn

**Mercredi 24 janvier 2024 — durée : 2 h.** Appareils électroniques et documents interdits. Barème indicatif. Le cartouche annonce une feuille recto verso ; le corrigé comprend neuf pages.

### Exercice 1 — Système d’EDP d’ordre 1 (4 points)

$$\begin{cases}f_x=y\exp(xy+y^2)-(y+2x)\sin(xy+x^2),\\f_y=2y+(x+2y)\exp(xy+y^2)-x\sin(xy+x^2).\end{cases}$$
1. Préciser et justifier le domaine de résolution.
2. Résoudre le système.

**1.** Les deux membres de droite, notés $G$ et $H$, sont de classe $C^1$ sur $\mathbb R^2$, par sommes, produits et compositions de polynômes, exponentielle et sinus (0,5 point). La compatibilité ci-dessous, sur le domaine simplement connexe $\mathbb R^2$, permet la résolution globale ; la seule régularité $C^1$ ne suffirait pas à l’affirmer.

**2, étape 1.**
$$G_y=H_x=[1+y(x+2y)]e^{xy+y^2}-\sin(xy+x^2)-x(y+2x)\cos(xy+x^2)$$
(0,5 point). **Coquille :** le PDF ajoute un facteur $x$ dans le dernier terme de $H_x$ ; l’expression commune correcte est celle ci-dessus.

**Étape 2.** En intégrant la première équation en $x$,
$$f(x,y)=e^{xy+y^2}+\cos(xy+x^2)+K(y),\qquad K\in C^2(\mathbb R)$$
(1 point).

## Page 2

**Exercice 1 — étapes 3 à 5.** La dérivée en $y$ est
$$f_y=(x+2y)e^{xy+y^2}-x\sin(xy+x^2)+K'(y).$$
Comparée à la seconde équation, elle impose $K'(y)=2y$ (1 point), donc $K(y)=y^2+C$ (0,5 point). Finalement,
$$f(x,y)=e^{xy+y^2}+\cos(xy+x^2)+y^2+C,\qquad C\in\mathbb R$$
(0,5 point).

### Exercice 2 — EDP d’ordre 1 (4,5 points)

Soit $D=\{(x,y):y\ne\pm x,\ x\ne0\}$ et
$$\varphi(x,y)=(u,v)=\left(\frac{x+y}{x},x-y\right).$$
1. Montrer que $\varphi$ est un $C^1$-difféomorphisme de $D$ sur un domaine $V$ à préciser.
2. Résoudre sur $D$ l’équation $xf_x+yf_y=e^{x+y}$ avec $f\in C^1(D)$.

**1a.** Les composantes sont de classe $C^1$ sur $D$ : la première est une fraction rationnelle avec $x\ne0$, la seconde est affine (0,5 point).

**Correction du domaine annoncé :** le PDF écrit $V=(\mathbb R\setminus\{0,2\})\times(\mathbb R\setminus\{0,2\})$. La restriction $v\ne2$ n’est pas justifiée. Le domaine exact est
$$V=(\mathbb R\setminus\{0,2\})\times\mathbb R^*.$$

## Page 3

**Exercice 2 — 1b et 1c.** Les équations donnent $y=(u-1)x$, $v=(2-u)x$, puis
$$\varphi^{-1}(u,v)=\left(\frac v{2-u},\frac{(u-1)v}{2-u}\right).$$
Les conditions $u\ne0,2$ et $v\ne0$ assurent exactement l’appartenance à $D$. Il y a bijection (0,5 point), et l’inverse est de classe $C^1$ puisque $2-u\ne0$ (0,5 point).

**2.** Posons $f=g\circ\varphi$ (0,5 point). Alors
$$f_x=-\frac y{x^2}g_u+g_v\quad(0,5\text{ point}),\qquad f_y=\frac1xg_u-g_v\quad(0,5\text{ point}).$$
L’équation se réduit à
$$vg_v=e^{uv/(2-u)},\qquad g_v=\frac1v e^{uv/(2-u)}\quad(0,5\text{ point}).$$
Le corrigé note une primitive indéfinie $\int v^{-1}e^{uv/(2-u)}\,dv$ avec une fonction arbitraire de $u$ (0,5 point), puis revient à $x,y$ (0,5 point).

**Écriture précise de la famille de solutions.** Sur chacun des deux signes de $v$, choisir $v_0=1$ ou $v_0=-1$ respectivement. Alors
$$g(u,v)=K_\pm(u)+\int_{v_0}^v\frac1t\exp\left(\frac{ut}{2-u}\right)dt,$$
avec $K_\pm\in C^1(\mathbb R\setminus\{0,2\})$ indépendantes, et
$$f(x,y)=g\left(\frac{x+y}{x},x-y\right).$$
**Coquilles signalées :** le texte inclut $K(u)$ dans une fonction $H$ puis l’ajoute à nouveau ; une ligne met aussi $(x+y)/y$ au lieu de $(x+y)/x$. La primitive définie ci-dessus évite ce double comptage et ne traverse pas $v=0$.

## Page 4

### Exercice 3 — EDP d’ordre 2 (8 points)

Sur $A=\mathbb R_+^*\times\mathbb R$, on utilise le changement polaire $\varphi(r,\theta)=(r\cos\theta,r\sin\theta)$ et $g=f\circ\varphi$, avec $f\in C^2(A)$.

1. Donner l’inverse et $B=\varphi^{-1}(A)$.
2. Exprimer $g_r,g_\theta,g_{rr},g_{\theta\theta},g_{r\theta}$ avec les dérivées de $f$ et les seules variables $x,y$.
3. Résoudre
$$xy(f_{yy}-f_{xx})+(x^2-y^2)f_{xy}=yf_x-xf_y+(x^2+y^2)\cos\sqrt{x^2+y^2}.$$

**1.** Sur la branche polaire correspondant à $x>0$,
$$B=]0,+\infty[\times]-\pi/2,\pi/2[,\qquad\varphi^{-1}(x,y)=\left(\sqrt{x^2+y^2},\arctan(y/x)\right)$$
(0,5 point). Le domaine angulaire est nécessaire pour avoir un inverse univoque.

**2.** Notons $r=\sqrt{x^2+y^2}$. Par la chaîne,
$$g_r=\frac{x}{r}f_x+\frac yr f_y\quad(0,5\text{ point}),\qquad g_\theta=-yf_x+xf_y\quad(0,5\text{ point}).$$
À angle fixé, on applique une seconde fois $\cos\theta\,\partial_x+\sin\theta\,\partial_y$, d’où
$$g_{rr}=\frac{x^2}{r^2}f_{xx}+\frac{2xy}{r^2}f_{xy}+\frac{y^2}{r^2}f_{yy}\quad(1\text{ point}).$$
Les quelques occurrences de $f_v,v$ dans les lignes imprimées de la chaîne désignent ici $f_y,y$.

## Page 5

**Exercice 3 — 2, dérivées secondes.** En dérivant $g_\theta=-r\sin\theta f_x+r\cos\theta f_y$ en $\theta$, y compris ses coefficients,
$$g_{\theta\theta}=-xf_x-yf_y+y^2f_{xx}-2xyf_{xy}+x^2f_{yy}\quad(1\text{ point}).$$
En dérivant la même expression en $r$,
$$g_{r\theta}=-\frac yr f_x-\frac{xy}{r}f_{xx}+\frac{x^2-y^2}{r}f_{xy}+\frac xr f_y+\frac{xy}{r}f_{yy}\quad(1\text{ point}).$$

**3. Réduction de l’EDP.** En multipliant cette dernière expression par $r>0$,
$$rg_{r\theta}=xy(f_{yy}-f_{xx})+(x^2-y^2)f_{xy}+xf_y-yf_x.$$
L’équation de l’énoncé est donc équivalente à $rg_{r\theta}=r^2\cos r$, soit
$$g_{r\theta}=r\cos r.$$

## Page 6

**Exercice 3 — 3, solution.** L’équation réduite $g_{r\theta}=r\cos r$ vaut 2 points au barème. Le corrigé propose
$$g(r,\theta)=(\cos r+r\sin r)\theta+C$$
(1 point), puis
$$f(x,y)=\left[\cos\sqrt{x^2+y^2}+\sqrt{x^2+y^2}\sin\sqrt{x^2+y^2}\right]\arctan(y/x)+C$$
(0,5 point).

**Complément nécessaire pour toutes les solutions.** L’intégration d’une dérivée mixte introduit deux fonctions arbitraires, pas seulement une constante. La famille générale sur $B$ est
$$g(r,\theta)=(\cos r+r\sin r)\theta+P(r)+Q(\theta),$$
où $P\in C^2(]0,+\infty[)$ et $Q\in C^2(]-\pi/2,\pi/2[)$. Il faut donc ajouter $P(\sqrt{x^2+y^2})+Q(\arctan(y/x))$ à la solution particulière. La formule du PDF est une sous-famille correcte.

### Exercice 4 — Classe C² (8,5 points)

$$f(x,y)=\begin{cases}\dfrac{x^3y^3}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$
1. Montrer que $f\in C^2(\mathbb R^2)$.
2. Calculer le gradient et la Hessienne.

Hors de zéro, la fonction est lisse comme fraction rationnelle à dénominateur non nul (0,5 point). Les dérivées premières sont
$$f_x=\frac{x^2y^3(x^2+3y^2)}{(x^2+y^2)^2},\qquad f_y=\frac{y^2x^3(y^2+3x^2)}{(x^2+y^2)^2}$$
(0,5 point chacune). La seconde s’obtient aussi par symétrie en $x,y$.

## Page 7

**Exercice 4 — dérivées premières à l’origine.** Les restrictions $f(t,0)$ et $f(0,t)$ sont nulles, donc $f_x(0,0)=f_y(0,0)=0$ (0,5 point chacune).

**Précision de preuve :** le corrigé renonce à vérifier leur continuité en invoquant l’énoncé qui demande justement de démontrer la classe $C^2$. Pour éviter ce raisonnement circulaire, on constate que $|f|\le r^4$ et que les expressions de $f_x,f_y$ sont $r^3$ multiplié par des fonctions angulaires bornées. Elles tendent donc vers zéro et sont continues à l’origine.

**Dérivées secondes hors de zéro.** En appliquant la règle du quotient et en regroupant,
$$f_{xx}=\frac{6xy^7-2x^3y^5}{(x^2+y^2)^3}\quad(0,5\text{ point}),$$
$$f_{yy}=\frac{6yx^7-2y^3x^5}{(x^2+y^2)^3}\quad(0,5\text{ point}),$$
$$f_{xy}=f_{yx}=\frac{x^2y^2(14x^2y^2+3x^4+3y^4)}{(x^2+y^2)^3}\quad(0,5\text{ point}).$$
À l’origine,
$$f_{xx}(0,0)=\lim_{t\to0}\frac{f_x(t,0)-f_x(0,0)}t=0\quad(0,5\text{ point}).$$

## Page 8

**Exercice 4 — dérivées secondes à l’origine.** Les restrictions nécessaires sur les axes étant nulles,
$$f_{yy}(0,0)=\lim_{t\to0}\frac{f_y(0,t)}t=0,$$
$$f_{xy}(0,0)=\lim_{t\to0}\frac{f_y(t,0)}t=0,\qquad f_{yx}(0,0)=\lim_{t\to0}\frac{f_x(0,t)}t=0$$
(0,5 point chacune).

**Continuité.** Avec $x=\rho\cos\theta$, $y=\rho\sin\theta$ et $c=\cos\theta$, $s=\sin\theta$,
$$f_{xx}=\rho^2(6cs^7-2c^3s^5)\to0,$$
$$f_{yy}=\rho^2(6sc^7-2s^3c^5)\to0,$$
$$f_{xy}=\rho^2c^2s^2(14c^2s^2+3c^4+3s^4)\to0.$$
Les facteurs angulaires sont bornés, donc les limites sont uniformes en $\theta$ (0,5 point chacune). Les dérivées secondes sont continues, et $f\in C^2(\mathbb R^2)$.

**2. Gradient (0,5 point).** Le texte rappelle que la classe $C^2$ est une condition suffisante, sans être nécessaire, pour disposer du gradient et de la Hessienne. Hors de zéro,
$$\nabla f(x,y)=\frac1{(x^2+y^2)^2}\begin{pmatrix}x^2y^3(x^2+3y^2)\\y^2x^3(y^2+3x^2)\end{pmatrix},$$
et $\nabla f(0,0)=(0,0)$.

## Page 9

**Exercice 4 — 2, matrice Hessienne (0,5 point).** Pour $(x,y)\ne(0,0)$,
$$H_f(x,y)=\frac1{(x^2+y^2)^3}\begin{pmatrix}6xy^7-2x^3y^5&x^2y^2(14x^2y^2+3x^4+3y^4)\\x^2y^2(14x^2y^2+3x^4+3y^4)&6yx^7-2y^3x^5\end{pmatrix}.$$
À l’origine,
$$H_f(0,0)=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$
Le reste de la page est vide.
