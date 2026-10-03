---
source: "PREING2-S2/Physique-moderne/Cours _ Introduction à la physique moderne _ CoursCY _ 2025-2026 (PROD).pdf"
pages: 9
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale des neuf pages, y compris les annotations manuscrites ; équations et conditions aux limites vérifiées
---

# CC2 — Introduction à la physique moderne — 7 mai 2026

PréIng 2 MI, option physique — CY Tech. Durée : 1 h 30, ou 2 h avec tiers-temps.

> Malgré son nom de fichier, le document est un sujet de CC2 corrigé. Les pages 1 à 3 contiennent l’énoncé annoté ; la page 4 reprend la question 1 ; les pages 5 à 9 donnent le corrigé manuscrit. Les reprises de l’énoncé sont réunies ci-dessous. Les erreurs identifiées sont signalées sans effacer la formulation source.

Les objets électroniques, les documents, les déplacements et les échanges sont interdits. Numéroter toutes les feuilles de la copie. La qualité des explications et de la rédaction est prise en compte. En cas d’erreur dans l’énoncé, l’indiquer sur la copie et continuer.

Les questions sont indépendantes. Les sous-questions précédées d’un astérisque ne dépendent pas des précédentes ; le sujet conseille néanmoins de tout lire, au cas où un astérisque aurait été oublié.

Le barème imprimé $3+6+5+6$ est remplacé à la main par $2{,}5+2{,}5+3{,}5+11{,}5$.

## 1. Équation de Schrödinger et fonction d’onde (2,5 points ; pages 1 et 4)

L’équation vérifiée par la fonction d’onde $\Psi(\vec r,t)$, dans un potentiel $V(\vec r,t)$, s’écrit

$$
i\hbar\frac{\partial\Psi}{\partial t}(\vec r,t)
=-\frac{\hbar^2}{2m}\Delta\Psi(\vec r,t)+V(\vec r,t)\Psi(\vec r,t).\tag{1}
$$

**a) [1 pt] À quelles conditions cette équation est-elle valable ?**

Réponse manuscrite : $m\ne0$ et $v\ll c$, « sans spin ».

**b) [0,5 pt] Quel est l’ensemble $X$ d’arrivée de la fonction d’onde ?**

$$
\Psi:\mathbb R^3\times\mathbb R\longrightarrow X,
\qquad(\vec r,t)\longmapsto\Psi(\vec r,t).\tag{2}
$$

Réponse : $X=\mathbb C$.

**c) [1 pt] Donner la dimension et l’unité SI de $V$.**

Réponse, sans démonstration demandée : $[V]=ML^2T^{-2}$, en joules.

## 2. États stationnaires (2,5 points ; pages 1 et 5)

Le potentiel $V(\vec r)$ est indépendant du temps. Pour une particule d’énergie $E$, on cherche

$$
\Psi(\vec r,t)=\phi(\vec r)f(t).\tag{3}
$$

**a) [1,5 pt] Déterminer l’équation différentielle de $f$.**

En injectant (3) dans (1),

$$
i\hbar f'(t)\phi(\vec r)
=-\frac{\hbar^2}{2m}f(t)\Delta\phi(\vec r)
+V(\vec r)f(t)\phi(\vec r),
$$

puis, là où la division est définie,

$$
i\hbar\frac{f'(t)}{f(t)}
=-\frac{\hbar^2}{2m}\frac{\Delta\phi(\vec r)}{\phi(\vec r)}+V(\vec r).
$$

Le premier membre dépend seulement de $t$, le second seulement de $\vec r$. Puisqu’ils sont égaux pour tout $t$ et tout $\vec r$, ils sont égaux à une constante $A$. Ainsi

$$
i\hbar f'(t)-Af(t)=0,
\qquad f'(t)+\frac{iA}{\hbar}f(t)=0.
$$

**b) [0,5 pt] Vérifier que $f(t)=\exp(-iEt/\hbar)$ est solution.**

Le corrigé confirme cette solution en prenant $A=E$ et un facteur multiplicatif égal à un devant l’exponentielle.

**c) [0,5 pt] Déterminer l’équation différentielle de $\phi$.**

La même démarche donne

$$
-\frac{\hbar^2}{2m}\Delta\phi(\vec r)+V(\vec r)\phi(\vec r)
=A\phi(\vec r),\qquad A=E.
$$

## 3. Puits infini et inégalités de Heisenberg (3,5 points annoncés ; pages 2 et 6)

Une particule de masse $m$, d’énergie $E>0$, est enfermée dans le puits

$$
V(x)=\begin{cases}
+\infty,&x<0,\\
0,&x\in[0,a],\\
+\infty,&x>a.
\end{cases}\tag{4}
$$

Pour une variable aléatoire $y$, $\langle y\rangle$ désigne sa moyenne et $\Delta y$ son écart-type.

> Dans le rappel imprimé, la moyenne autour de $(y-\langle y\rangle)^2$ manque sous la racine. La définition utilisée dans le corrigé est $\Delta y=\sqrt{\langle(y-\langle y\rangle)^2\rangle}$.

**a) [0,5 pt] Rappeler l’inégalité pour $x$ et $p$.**

$$
\Delta x\,\Delta p\ge\frac\hbar2.
$$

Le corrigé accepte aussi une écriture d’ordre de grandeur avec $\hbar$.

**b) [0,5 pt] En déduire une inégalité pour $\Delta p$ et $a$.**

Le manuscrit utilise $\Delta x\sim a$, d’où $\Delta p\gtrsim\hbar/(2a)$ ; il accepte également un choix de taille caractéristique $a/2$.

**c) [1 pt] Exprimer $\langle E\rangle$ en fonction de $\langle p^2\rangle$.**

$$
E=\frac{p^2}{2m},\qquad \langle E\rangle=\frac{\langle p^2\rangle}{2m}.
$$

**d) [1,5 pt] En déduire une borne inférieure de l’énergie moyenne.**

$$
\Delta p=\sqrt{\langle(p-\langle p\rangle)^2\rangle}
=\sqrt{\langle p^2\rangle-\langle p\rangle^2}.
$$

Le corrigé prend $\langle p\rangle=0$ et obtient

$$
\langle p^2\rangle=(\Delta p)^2,
\qquad
\langle E\rangle\ge\frac1{2m}\left(\frac\hbar{2a}\right)^2
=\frac{\hbar^2}{8ma^2}=\frac{h^2}{32\pi^2ma^2}.
$$

> **Note de vérification.** La borne reste valable sans supposer $\langle p\rangle=0$, car $\langle p^2\rangle\ge(\Delta p)^2$. La ligne alternative du manuscrit donnant des dénominateurs $4ma^2$ et $16\pi^2ma^2$ ne découle pas du remplacement de $\hbar/2$ par $\hbar$ dans Heisenberg : ce remplacement multiplierait la borne par quatre, pas par deux.

**e) [0,5 pt] Peut-on en déduire l’énergie minimale ?**

Le corrigé répond non : la seule borne obtenue sur la moyenne ne donne pas la valeur exacte de l’énergie minimale.

> Les points inscrits par sous-question totalisent quatre, alors que l’en-tête manuscrit annonce $3{,}5$.

## 4. Puits fini et barrière de potentiel (11,5 points ; pages 2, 3 et 7 à 9)

Une particule de masse $m$ et d’énergie $E>0$ provient de $+\infty$ et se propage de la droite vers la gauche. Elle rencontre en $x=a>0$ un puits de profondeur $-V_0<0$, de longueur $a$. La région $x<0$ est inaccessible :

$$
V(x)=\begin{cases}
+\infty,&x<0,\\
-V_0,&x\in[0,a]\quad\text{(région 1)},\\
0,&x>a\quad\text{(région 2)}.
\end{cases}\tag{7}
$$

**a) [1 pt] Représenter le potentiel.**

Le schéma manuscrit trace $V$ verticalement et $x$ horizontalement : paroi infinie à gauche de zéro, plateau à $-V_0$ de zéro à $a$, remontée à zéro en $a$, puis plateau nul jusqu’à $+\infty$. Une énergie $E>0$ est repérée au-dessus du plateau nul. Les régions 1 et 2 sont indiquées sous l’axe.

**b) [1 pt] Quel serait le mouvement classique ?**

À l’entrée du puits en $a$, l’énergie cinétique augmente, l’énergie mécanique restant constante. La particule subit un choc élastique contre la paroi en zéro, puis repart vers $+\infty$.

**c) [2 pt] Montrer que $\phi(x)=A_j e^{ixk_j}+B_j e^{-ixk_j}$ dans la région $j\in\{1,2\}$.**

L’équation stationnaire donne

$$
\begin{aligned}
-\frac{\hbar^2}{2m}\phi''-V_0\phi&=E\phi&&\text{(région 1)},\\
-\frac{\hbar^2}{2m}\phi''&=E\phi&&\text{(région 2)}.
\end{aligned}
$$

Soit $\phi''+k_j^2\phi=0$, avec

$$
k_1^2=\frac{2m(E+V_0)}{\hbar^2},\qquad k_2^2=\frac{2mE}{\hbar^2}.
$$

L’équation caractéristique, ou l’analogie avec l’oscillateur harmonique où la variable est $x$, conduit à la forme demandée. Le corrigé accepte aussi une solution réelle trigonométrique, mais précise que la suite du calcul sera différente.

**d) [1 pt] Utiliser la condition en zéro pour montrer $B_1=-A_1$.**

La paroi infinie impose $\phi(0)=A_1+B_1=0$.

**e) [1 pt] Justifier que ni $A_2$ ni $B_2$ ne sont nuls.**

$B_2e^{-ik_2x}$ représente l’onde incidente allant vers les $x$ décroissants, donc $B_2\ne0$. La particule est réfléchie par la paroi ; l’onde $A_2e^{ik_2x}$ se propage vers les $x$ croissants, donc $A_2\ne0$.

**f) [2 pt] Établir les conditions de raccordement en $a$.**

La continuité de $\phi$ donne, puisque $B_1=-A_1$,

$$
A_1(e^{ik_1a}-e^{-ik_1a})=A_2e^{ik_2a}+B_2e^{-ik_2a}.
$$

La continuité de $\phi'$ donne

$$
ik_1A_1(e^{ik_1a}+e^{-ik_1a})
=ik_2(A_2e^{ik_2a}-B_2e^{-ik_2a}).
$$

D’où le système demandé :

$$
\begin{cases}
A_2e^{ik_2a}+B_2e^{-ik_2a}=2iA_1\sin(k_1a),\\
A_2e^{ik_2a}-B_2e^{-ik_2a}=2A_1\dfrac{k_1}{k_2}\cos(k_1a).
\end{cases}\tag{8}
$$

L’annotation de barème insiste sur les conditions de continuité, davantage que sur le calcul menant à (8). Un $B_1$ écrit dans la première ligne intermédiaire du manuscrit est remplacé ici par $B_2$, conformément au système final et à la région considérée.

**g) [1 pt] Exprimer $A_2$ et $B_2$ en fonction de $A_1$.**

En additionnant puis en soustrayant les deux lignes,

$$
A_2=A_1\left(\frac{k_1}{k_2}\cos(k_1a)+i\sin(k_1a)\right)e^{-ik_2a},
$$

$$
B_2=A_1\left(-\frac{k_1}{k_2}\cos(k_1a)+i\sin(k_1a)\right)e^{ik_2a}.
$$

Le corrigé prévoit la moitié des points pour des résultats cohérents avec une réponse précédente erronée.

**h) [0,5 pt] Exprimer $B_2$ à l’aide de $\overline{A_2}$.**

La conclusion manuscrite est $B_2=-\overline{A_2}$.

> **Précision nécessaire.** Cette conclusion suppose un choix de phase tel que $A_1$ soit réel. Pour $A_1\in\mathbb C\setminus\{0\}$ quelconque, les expressions précédentes donnent $B_2=-(A_1/\overline{A_1})\overline{A_2}$. Dans la ligne intermédiaire de h), le manuscrit écrit $e^{-ik_2a}$ ; il faut $e^{ik_2a}$ pour rester cohérent avec g).

**i) [1 pt] Donner la probabilité de réflexion. j) [1 pt] La calculer et commenter.**

Le manuscrit utilise $R=|B_2/A_2|^2$ et conclut $R=1$ grâce à l’égalité des modules. La particule ne peut qu’être réfléchie.

> **Sens du quotient.** Avec les sens de propagation établis en e), l’onde incidente est $B_2$ et l’onde réfléchie $A_2$ : la définition est donc $R=|A_2/B_2|^2$. Ici les modules sont égaux, si bien que le quotient inversé du manuscrit conduit tout de même à la bonne valeur $R=1$.

## 5. Bonus (pages 3 et 9)

**a)** Écrire la seizième lettre de l’alphabet grec. Réponse manuscrite : $\pi$ **[0,5 pt]**.

**b)** Dissertation : qu’est-ce que la réalité ? La physique décrit-elle la réalité ? Aucun corrigé fourni.

**c)** Commenter cette phrase attribuée dans le sujet à Lord Kelvin en 1900 : « Il n’y a plus rien à découvrir en physique aujourd’hui, tout ce qui reste est d’améliorer la précision des mesures. » Aucun corrigé fourni.
