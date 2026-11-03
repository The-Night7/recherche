---
source: "PREING2-S1/Analyse-dans-RN-DS/DS2-2023-2024-V2_Analyse-dans-RN-DS_P2S1_DMaths.pdf"
pages: 6
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-14
verification: lecture visuelle des six pages ; dérivées, limites et domaines vérifiés ; erreurs de la source signalées
---

# Analyse dans ℝⁿ — DS2 2023–2024, V2 : sujet 0 et corrigé

**Lundi 11 décembre 2023 à 10 h 15 — durée : 1 h.** Appareils électroniques et documents interdits. Trois exercices ; barème indicatif, qualité de la rédaction et précision des justifications prises en compte. Le cartouche annonce une feuille recto verso pour le sujet, mais le PDF comporte six pages avec les réponses en bleu et les points en rouge. Son nom ne porte pas la mention « Correction ».

## Exercice 1 — Limite, continuité, différentiabilité et classe C¹ (11,5 points ; pages 1–3)

**Énoncé.** Soit

$$f(x,y)=\begin{cases}x^2\sin\!\left(\dfrac1{\sqrt{x^2+y^2}}\right),&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$

1. Montrer que $f$ est continue sur $\mathbb R^2$ (1,5 point).
2. Sur quels domaines $f$ est-elle de classe $C^1$ (6,5 points) ?
3. Sur quels domaines $f$ est-elle différentiable et, le cas échéant, quelle est sa différentielle (3,5 points) ?

**Correction — 1.** Hors de l’origine, les opérations et compositions de fonctions continues ont des dénominateurs non nuls (0,5 point). À l’origine,

$$|f(x,y)|\le x^2\longrightarrow0=f(0,0).$$

La fonction est donc continue sur tout $\mathbb R^2$ (1 point).

**2. Dérivées partielles.** À l’origine,

$$\partial_xf(0,0)=\lim_{t\to0}t\sin(1/|t|)=0,\qquad
\partial_yf(0,0)=\lim_{t\to0}\frac{f(0,t)-f(0,0)}t=0$$

(1 point chacune). Pour $r=\sqrt{x^2+y^2}>0$,

$$\partial_xf(x,y)=2x\sin(1/r)-\frac{x^3}{r^3}\cos(1/r),\qquad
\partial_yf(x,y)=-\frac{x^2y}{r^3}\cos(1/r)$$

(1 point chacune). Ces expressions sont continues sur $\mathbb R^2\setminus\{(0,0)\}$ : $f$ y est $C^1$ (1 point).

En coordonnées polaires, la seconde dérivée s’écrit

$$\partial_yf(r\cos\theta,r\sin\theta)=-\cos^2\theta\sin\theta\cos(1/r).$$

Pour $\theta=\pi/4$, le facteur angulaire est non nul et $\cos(1/r)$ n’a pas de limite quand $r\to0^+$. Ainsi $\partial_yf$ n’est pas continue à l’origine et $f$ n’y est pas de classe $C^1$ (1,5 point).

> **Rectifications de la source (page 2).** La deuxième limite à l’origine est étiquetée $\partial_xf$ au lieu de $\partial_yf$. Dans le passage polaire, le cosinus est placé par erreur au dénominateur dans une égalité intermédiaire : il multiplie bien $-\cos^2\theta\sin\theta$. La formule n’est pas « non définie » pour $r>0$ ; elle n’a pas de limite en zéro pour un angle tel que $\pi/4$.

**3. Différentiabilité.** Hors de l’origine, la classe $C^1$ entraîne la différentiabilité (0,5 point), avec

$$D_{(x,y)}f(h_1,h_2)=h_1\left[2x\sin(1/r)-\frac{x^3}{r^3}\cos(1/r)\right]-h_2\frac{x^2y}{r^3}\cos(1/r)$$

(0,5 point). À l’origine, les deux dérivées partielles étant nulles, la différentielle candidate est nulle. Le reste normalisé est

$$\varepsilon(h_1,h_2)=\frac{h_1^2}{\sqrt{h_1^2+h_2^2}}\sin\!\left(\frac1{\sqrt{h_1^2+h_2^2}}\right).$$

Le critère et cette substitution valent chacun 0,5 point. Avec $h_1=\rho\cos\theta$ et $h_2=\rho\sin\theta$,

$$\varepsilon=\rho\cos^2\theta\sin(1/\rho),\qquad |\varepsilon|\le\rho\to0$$

(1 point). Donc $f$ est différentiable sur tout $\mathbb R^2$ et $D_{(0,0)}f=0$ (0,5 point).

> **Coquille (page 3).** Dans le sinus du reste, le PDF conserve $x^2+y^2$ au lieu de $h_1^2+h_2^2$. La majoration ci-dessus explicite le caractère uniforme en $\theta$ du passage à la limite.

## Exercice 2 — Continuité d’une fonction par morceaux (4 points ; pages 3–5)

**Énoncé.** On définit

$$f(x,y)=\begin{cases}
\dfrac{|x|}{y^2},&y>|x|,\\
\dfrac{4y}{(|x|+|y|)^2},&y\le|x|\text{ et }(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}$$

1. Représenter les domaines de définition des morceaux (1 point).
2. Étudier la continuité sur $\mathbb R^2$ (3 points).

**Correction — 1.** Posons $U=\{y>|x|\}$, $V=\{y<|x|\}$ et $F=\{y=|x|\}$. Le dessin page 4 montre en bleu le secteur ouvert situé au-dessus des deux demi-droites $y=x$ pour $x\ge0$ et $y=-x$ pour $x\le0$, et en rouge la région située en dessous. La frontière est le V formé par ces deux demi-droites. L’origine est à traiter séparément, comme le précise la légende du corrigé.

**2.** Sur $U$, $y>0$ et la première expression est continue (0,5 point). Sur $V$, $|x|+|y|>0$ et la seconde expression est continue (0,5 point).

Soit $(x_0,y_0)\in F\setminus\{(0,0)\}$ ; alors $y_0=|x_0|>0$. Les limites des deux expressions valent

$$\frac{|x_0|}{y_0^2}=\frac1{|x_0|},\qquad
\frac{4y_0}{(|x_0|+|y_0|)^2}=\frac1{|x_0|}=f(x_0,y_0).$$

Chaque limite vaut 0,5 point au barème. Les deux expressions se raccordent donc continûment sur la frontière hors de l’origine.

Pour $y<0$, $f(0,y)=4/y\to-\infty$ lorsque $y\to0^-$. La fonction n’est pas continue à l’origine (1 point). **Domaine de continuité : $\mathbb R^2\setminus\{(0,0)\}$.**

> **Erreur de signe (page 4).** La première limite sur $F$ est imprimée avec $x_0$ puis $1/x_0$ au lieu de $|x_0|$ puis $1/|x_0|$. La conclusion correcte concerne $F$ privé de l’origine.

## Exercice 3 — Continuité bis (4,5 points ; pages 5–6)

**Énoncé.** Déterminer la continuité des fonctions suivantes (respectivement 1 ; 1,5 ; 2 points) :

$$f_1(x,y)=\frac{xy^3}{x^2+y^2},\qquad
f_2(x,y)=\frac{x^2+y^2}{|x|+|y|},\qquad
f_3(x,y)=\begin{cases}\dfrac{y^3}{(x-1)^2+y^2},&(x,y)\ne(1,0),\\0,&(x,y)=(1,0).\end{cases}$$

**Correction.** Les trois fonctions sont continues là où leur dénominateur ne s’annule pas (0,5 point chacune).

Pour $f_1$, hors de l’origine,

$$|f_1(x,y)|=\frac{|xy|y^2}{x^2+y^2}\le|xy|\longrightarrow0$$

(0,5 point). Pour $f_2$, en coordonnées polaires,

$$f_2(\rho\cos\theta,\rho\sin\theta)=\frac\rho{|\cos\theta|+|\sin\theta|},\qquad
0\le f_2\le\rho\to0$$

car $|\cos\theta|+|\sin\theta|\ge1$ (1 point).

> **Lacune de l’énoncé.** Les valeurs $f_1(0,0)$ et $f_2(0,0)$ ne sont pas définies dans le PDF. Ces deux fonctions sont donc, telles qu’écrites, continues seulement sur leur domaine $\mathbb R^2\setminus\{(0,0)\}$ ; elles admettent un prolongement continu sur $\mathbb R^2$ en leur donnant la valeur zéro à l’origine. Le corrigé suppose implicitement ce prolongement. La seule positivité du facteur angulaire ne suffirait pas pour $f_2$ : la borne inférieure $1$ justifie la limite indépendamment de l’angle.

Pour $f_3$, écrivons $x=1+\rho\cos\theta$, $y=\rho\sin\theta$. Alors

$$f_3(x,y)=\rho\sin^3\theta,\qquad |f_3(x,y)|\le\rho\to0=f_3(1,0).$$

La fonction $f_3$ est continue sur tout $\mathbb R^2$ (1,5 point pour l’étude en $(1,0)$).

> **Coquille (page 6).** Le sous-titre « En $(0,0)$ » concerne en réalité le point $(1,0)$.
