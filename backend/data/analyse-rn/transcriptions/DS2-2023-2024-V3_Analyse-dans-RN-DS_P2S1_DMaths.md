---
source: "PREING2-S1/Analyse-dans-RN-DS/DS2-2023-2024-V3_Analyse-dans-RN-DS_P2S1_DMaths.pdf"
pages: 3
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-14
verification: lecture visuelle des trois pages ; dérivées, signes et limites vérifiés ; coquilles signalées
---

# Analyse dans ℝⁿ — DS2 2023–2024, V3 : corrigé

**Mercredi 13 décembre 2023 — groupes MI2 et MI3 — durée : 1 h.** Appareils électroniques interdits. Quatre exercices, à traiter dans l’ordre de son choix ; qualité de rédaction et précision des justifications prises en compte. Le PDF porte explicitement « Corrigé », bien que son nom ne contienne pas cette mention. Le barème affiché totalise 21 points.

## Exercice 1 — Prolongement continu et dérivées partielles (4 points ; page 1)

**Énoncé.** Sur $\mathbb R^2\setminus\{(0,0)\}$, on définit

$$f(x,y)=\frac{x^2}{(x^2+y^2)^{3/4}}.$$

1. Montrer que $f$ est prolongeable par continuité à l’origine.
2. Étudier les dérivées partielles premières du prolongement à l’origine.

**Correction — 1.** Hors de l’origine, $f$ est un quotient de fonctions continues à dénominateur non nul (0,5 point). Comme $x^2\le x^2+y^2$,

$$0\le f(x,y)\le(x^2+y^2)^{1/4}\longrightarrow0.$$

Le prolongement continu est donné par $f(0,0)=0$ (1,5 point).

**2.** La restriction $f(0,t)=0$ donne $\partial_yf(0,0)=0$ (1 point). En revanche,

$$\frac{f(t,0)-f(0,0)}t=\frac{|t|^{1/2}}t=\frac{\operatorname{sgn}(t)}{\sqrt{|t|}}.$$

Ce quotient tend vers $+\infty$ à droite et $-\infty$ à gauche. Il n’a pas de limite réelle : $\partial_xf(0,0)$ n’existe pas (1 point).

> **Erreur de signe de la source.** Le PDF écrit $|t|^{-1/2}$ et annonce $+\infty$ des deux côtés. Le facteur $\operatorname{sgn}(t)$ a été rétabli ; la conclusion sur l’absence de dérivée reste correcte.

## Exercice 2 — Absence de continuité uniforme (3 points ; pages 1–2)

**Énoncé.** Soit $f(x)=\sin(x^2)$ sur $\mathbb R$.

1. Écrire avec des quantificateurs que $f$ n’est pas uniformément continue.
2. Le démontrer à l’aide de $x_n=\sqrt{n\pi}$ et $y_n=\sqrt{n\pi+\pi/2}$.

**Correction — 1.** Une formulation équivalente à celle du PDF est

$$\exists\varepsilon_0>0,\ \forall\eta>0,\ \exists x,y\in\mathbb R:\quad
|x-y|<\eta\ \text{ et }\ |f(x)-f(y)|\ge\varepsilon_0$$

(1 point). La source utilise $|x-y|\le\eta$ et $|f(x)-f(y)|>\varepsilon$.

**2.** On a $f(x_n)=0$ et $f(y_n)=(-1)^n$, donc $|f(x_n)-f(y_n)|=1$. Par rationalisation,

$$x_n-y_n=\frac{-\pi/2}{\sqrt{n\pi}+\sqrt{n\pi+\pi/2}}\longrightarrow0.$$

En fixant par exemple $\varepsilon_0=1/2$, toute valeur $\eta>0$ est contredite par ces deux points pour $n$ assez grand. La fonction n’est pas uniformément continue (2 points).

> **Coquille de la source.** Le dénominateur imprimé après rationalisation contient un terme $n\pi$ supplémentaire. La formule exacte est celle ci-dessus.

## Exercice 3 — Compacité (6 points ; page 2)

**Énoncé.** Considérer

$$A=[-1,5[\,\cup\{8\},\quad B=\{(x,y)\in\mathbb R^2:x^2+y^6\le1\},$$
$$C=\{(x,y,t)\in\mathbb R^3:x^2+y^5\le1-t^2\}.$$

1. Rappeler le critère de compacité dans $\mathbb R^n$.
2. Déterminer si $A$, $B$ et $C$ sont compacts.

**Correction — 1.** Dans $\mathbb R^n$, une partie est compacte si et seulement si elle est fermée et bornée (0,5 point).

**2. $A$.** La suite $x_n=5-1/n$ appartient à $A$ mais converge vers $5\notin A$ (1 point). Donc $A$ n’est pas fermé et n’est pas compact (0,5 point).

**$B$.** Les deux termes $x^2,y^6$ sont positifs ; leur somme inférieure à $1$ implique $|x|\le1$ et $|y|\le1$. Ainsi $B$ est borné (1 point). C’est aussi l’image réciproque du fermé $[0,1]$ par la fonction continue $(x,y)\mapsto x^2+y^6$. Il est fermé, donc compact (1 point).

**$C$.** Pour tout $r>0$,

$$z_r=(r,\sqrt[5]{1-2r^2},r)\in C,\qquad \|z_r\|_\infty\ge r.$$

La racine cinquième réelle existe même pour un radicand négatif. La partie $C$ n’est pas bornée, donc pas compacte (2 points).

> **Coquille de la source.** Dans la norme, le PDF remplace par erreur $1-2r^2$ par $1-r^2$. Le même vecteur $z_r$ doit être utilisé dans les deux lignes.

## Exercice 4 — Continuité, classe C¹ et différentiabilité (8 points ; pages 2–3)

**Énoncé.** Soit

$$f(x,y)=\begin{cases}\dfrac{xy(x^2-y^2)}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$

1. La fonction est-elle continue sur $\mathbb R^2$ ?
2. Calculer ses dérivées partielles premières sur $\mathbb R^2$.
3. Est-elle de classe $C^1$ sur $\mathbb R^2$ ?
4. Est-elle différentiable sur $\mathbb R^2$ ?

**Correction — 1.** Hors de l’origine, la fraction rationnelle est continue (0,5 point). En utilisant $2|xy|\le x^2+y^2$,

$$|f(x,y)|\le\frac{|x^2-y^2|}{2}\le\frac{x^2+y^2}{2}\longrightarrow0.$$

La fonction est donc continue partout (1,5 point).

**2.** Pour $(x,y)\ne(0,0)$,

$$\partial_xf(x,y)=\frac{x^4y-y^5+4x^2y^3}{(x^2+y^2)^2},\qquad
\partial_yf(x,y)=\frac{-xy^4+x^5-4x^3y^2}{(x^2+y^2)^2}$$

(0,5 point chacune). Les restrictions aux deux axes étant identiquement nulles,

$$\partial_xf(0,0)=\partial_yf(0,0)=0$$

(0,5 point chacune).

**3.** Les dérivées sont données par les expressions précédentes hors de l’origine et par zéro à l’origine (0,5 point par définition par morceaux). Elles sont continues hors de l’origine (0,5 point). En posant $r=\sqrt{x^2+y^2}$, les bornes $|x|,|y|\le r$ donnent

$$|\partial_xf(x,y)|\le\frac{|x|^4|y|+|y|^5+4|x|^2|y|^3}{r^4}\le\frac{6r^5}{r^4}=6r\to0.$$

Le même raisonnement s’applique à $\partial_yf$ (0,75 point chacune). Les deux dérivées sont donc continues à l’origine, et **$f\in C^1(\mathbb R^2)$**.

**4.** Toute fonction de classe $C^1$ est différentiable : $f$ est différentiable sur tout $\mathbb R^2$ (1 point).
