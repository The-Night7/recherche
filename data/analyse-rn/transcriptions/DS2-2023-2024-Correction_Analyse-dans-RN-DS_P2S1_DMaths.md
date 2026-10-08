---
source: "PREING2-S1/Analyse-dans-RN-DS/DS2-2023-2024-Correction_Analyse-dans-RN-DS_P2S1_DMaths.pdf"
pages: 6
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des pages rendues, comparaison au texte natif ; formules et annotations transcrites
---

# Analyse dans Rn — DS2 2023–2024 : limites, différentiabilité et classe C1

## Page 1

### Préing 2 — DS2, sujet 1 d’Analyse dans Rn

**Lundi 11 décembre 2023 à 16 h 30 — durée : 1 h.** Appareils électroniques et documents interdits. Barème indicatif. Trois exercices, à traiter dans l’ordre de son choix ; rédaction et justifications prises en compte. Le cartouche annonce un sujet d’une feuille recto verso ; ce fichier contient six pages de corrigé.

### Exercice 1 — Limite et continuité (6 points)

**1.** Étudier la continuité sur $\mathbb R^2$ de
$$f(x,y)=\begin{cases}\dfrac{xy}{|x|+|y|},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0),\end{cases}$$
annoncée sur 1 point, et de
$$g(x,y)=\begin{cases}\dfrac{x^4y^2}{x^4+y^6},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0),\end{cases}$$
annoncée sur 2 points. Les exposants $4$ sont corrigés en rouge dans l’énoncé.

**2.** Calculer les dérivées partielles premières de $g$ (2 points).

**3.** Déterminer la limite en $(0,0)$ de
$$h(x,y)=\frac{2xy+x^2-y^2+y}{x^2+3y^2-xy+2y}\quad(1\text{ point}).$$

**Correction de 1 pour $f$.** Hors de l’origine, quotient de fonctions continues à dénominateur non nul : continuité (barème révisé : 1 point). En coordonnées polaires,
$$f(\rho\cos\theta,\rho\sin\theta)=\rho\frac{\cos\theta\sin\theta}{|\cos\theta|+|\sin\theta|}.$$
Le facteur angulaire est borné uniformément : le dénominateur est au moins $1$. La limite est donc zéro, égale à $f(0,0)$ : continuité à l’origine (1 point).

## Page 2

**Exercice 1 — 1, $g$.** Le corrigé signale une erreur dans la fonction initialement distribuée et précise que la fonction souhaitée était celle avec $x^4$, déjà corrigée page 1. Hors de l’origine, elle est continue ; à l’origine,
$$0\le\left|\frac{x^4y^2}{x^4+y^6}\right|\le y^2\to0.$$
Donc cette fonction $g$ est continue sur $\mathbb R^2$. L’auteur indique avoir redistribué les 2 points de la question à cause de l’erreur initiale.

**2. Dérivées : incohérence conservée et signalée.** Les formules imprimées restent celles de $g_3(x,y)=x^3y^2/(x^3+y^6)$ :
$$\partial_xg_3=\frac{3x^2y^8}{(x^3+y^6)^2},\qquad\partial_yg_3=\frac{2yx^6-4x^3y^7}{(x^3+y^6)^2}.$$
Chaque dérivée hors de l’origine vaut 1 point au barème. Ces formules s’appliquent uniquement où $x^3+y^6\ne0$ ; $g_3$ n’est pas définie sur toute la droite courbe $x=-y^2$.

**Pour la fonction corrigée avec $x^4$, les dérivées correctes hors de l’origine sont**
$$\partial_xg=\frac{4x^3y^8}{(x^4+y^6)^2},\qquad\partial_yg=\frac{2yx^8-4x^4y^7}{(x^4+y^6)^2}.$$
En zéro, les restrictions aux axes sont nulles, donc $\partial_xg(0,0)=\partial_yg(0,0)=0$ (0,5 point chacune). Le même calcul sur les axes apparaît dans le corrigé imprimé.

**3.** La page rappelle la fraction $h$ de l’énoncé et prépare la comparaison de deux chemins.

## Page 3

**Exercice 1 — 3.** Sur la diagonale,
$$h(x,x)=\frac{2x^2+x}{3x^2+2x}=\frac{2x+1}{3x+2}\to\frac12.$$
Sur l’axe $y=0$, $h(x,0)=1$ pour $x\ne0$. Les limites diffèrent, donc la limite en $(0,0)$ n’existe pas (1 point).

### Exercice 2 — Différentiabilité (8 points)

Étudier la différentiabilité sur $\mathbb R^2$ de
$$f(x,y)=\begin{cases}\dfrac{x}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0),\end{cases}\quad(2,5\text{ points}),$$
$$g(x,y)=\begin{cases}\dfrac{x^2y+3y^3}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0),\end{cases}\quad(5,5\text{ points}).$$

**Pour $f$.** Hors de l’origine, la fraction rationnelle est de classe $C^1$, donc différentiable (1 point). En revanche, $f(x,0)=1/x$ ne tend pas vers zéro : $f$ n’est pas continue en $(0,0)$ et ne peut y être différentiable (1,5 point).

## Page 4

**Exercice 2 — $g$.** Hors de l’origine, la fonction est de classe $C^1$, donc différentiable (1 point). En zéro, ses dérivées partielles sont
$$\partial_xg(0,0)=\lim_{t\to0}\frac{g(t,0)}t=0\quad(0,5\text{ point}),$$
$$\partial_yg(0,0)=\lim_{t\to0}\frac{3t}t=3\quad(1\text{ point}).$$
La différentielle candidate est donc $L(h_1,h_2)=3h_2$. Le critère de différentiabilité (1 point) demande que
$$\varepsilon(h_1,h_2)=\frac{g(h_1,h_2)-3h_2}{\sqrt{h_1^2+h_2^2}}\to0.$$
En remplaçant $g$ (0,5 point) puis en simplifiant,
$$\varepsilon(h_1,h_2)=\frac{-2h_1^2h_2}{(h_1^2+h_2^2)^{3/2}}.$$
Sur $h_2=h_1=t>0$, cette expression vaut $-1/\sqrt2$. Elle ne tend pas vers zéro : $g$ n’est pas différentiable à l’origine (1,5 point).

### Exercice 3 — Propriété C¹ (6 points)

On considère
$$f(x,y)=\begin{cases}\dfrac{y^4}{x^2+y^2},&(x,y)\ne(0,0),\\0,&(x,y)=(0,0).\end{cases}$$

## Page 5

**Exercice 3 — questions.** Montrer que $f$ est continue sur $\mathbb R^2$ (1 point), puis déterminer son domaine de classe $C^1$ (5 points).

**1. Continuité.** En polaires, $f=\rho^2\sin^4\theta\to0$ uniformément en l’angle, donc continuité en zéro (0,5 point). Hors de zéro, c’est une fraction rationnelle à dénominateur non nul (0,5 point).

**2. Dérivées en zéro.**
$$\partial_xf(0,0)=0\quad(0,5\text{ point}),\qquad\partial_yf(0,0)=\lim_{t\to0}\frac{t^2}t=0\quad(1\text{ point}).$$
Hors de zéro,
$$\partial_xf(x,y)=-\frac{2xy^4}{(x^2+y^2)^2}\quad(1\text{ point}),$$
$$\partial_yf(x,y)=\frac{4y^3(x^2+y^2)-2y^5}{(x^2+y^2)^2}=\frac{4x^2y^3+2y^5}{(x^2+y^2)^2}\quad(1\text{ point}).$$
Les deux dérivées sont prolongées par zéro à l’origine. La page annonce l’étude de leur continuité et dit que celle par rapport à $x$ « semble clairement ne pas être continue » ; cette anticipation est contredite par le calcul suivant.

## Page 6

**Exercice 3 — 2, continuité des dérivées.** En coordonnées polaires,
$$\partial_xf(\rho\cos\theta,\rho\sin\theta)=-2\rho\cos\theta\sin^4\theta,$$
qui tend vers zéro uniformément en $\theta$. De même,
$$\partial_yf(\rho\cos\theta,\rho\sin\theta)=\rho(4\cos^2\theta\sin^3\theta+2\sin^5\theta),$$
qui tend uniformément vers zéro. Les deux dérivées partielles sont donc continues en zéro (1 point). Hors de l’origine, elles sont continues comme fractions rationnelles à dénominateur non nul (0,5 point). Ainsi
$$\boxed{f\in C^1(\mathbb R^2)}.$$

**Incohérence du texte source :** après une limite notée « $\pm0$ », le PDF écrit que la dérivée par rapport à $x$ « est pas continue », puis conclut que les dérivées sont continues. La limite vaut bien zéro et les deux dérivées sont continues. La classe $C^1$ s’étend à tout $\mathbb R^2$, pas seulement au plan privé de l’origine.
