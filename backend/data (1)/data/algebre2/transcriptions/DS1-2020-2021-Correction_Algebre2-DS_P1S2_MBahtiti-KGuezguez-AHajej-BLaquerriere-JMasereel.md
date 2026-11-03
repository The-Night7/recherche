# Algèbre 2 — DS 2020–2021 (titré « Devoir surveillé 4 »), sujet et correction

> Source : `PREING1-S2/Algebre2-DS/DS1-2020-2021-Correction_Algebre2-DS_P1S2_MBahtiti-KGuezguez-AHajej-BLaquerriere-JMasereel.pdf`, 5 pages (PDF natif). Dans la source, les énoncés sont en noir et les corrections en bleu, avec le barème en rouge. Ici, chaque correction suit le séparateur ◇◇◇.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale ; calculs refaits, système de l’exercice 5 vérifié numériquement.
> **Écart de nommage :** l’en-tête indique « Devoir surveillé 4 », jeudi 11 mars 2021, alors que le fichier est nommé DS1.
> Erreurs de la source, signalées et non corrigées dans le texte :
> - **Exercice 1.4** : $(a,b)\star((a',b')\star(a'',b''))=(a-2a'+4a'',\,b+3b'+9b'')$, et non $a-2a'-4a''$. La conclusion (non associative) reste juste.
> - **Exercice 2.3** : « $e'=f(e)\inf(H)$ » est une coquille pour « $e'=f(e)\in f(H)$ ».
> - **Exercice 2.4** : la conclusion doit porter sur $x\top x'^{-1}\in\operatorname{Ker}(f)$, et non sur $x\top x'$.
> - **Exercice 5.1** : le troisième argument est faux. Le système de l’élève est de rang 3, comme le système initial ; les rangs ne diffèrent pas. Les deux systèmes ont des solutions uniques différentes : $(-\frac25,-\frac25,-\frac7{30})$ contre $(-\frac{47}{45},\frac{17}{30},-\frac{79}{90})$.
> - **Exercice 5.2** : l’équation intermédiaire est $17y+3z=7$ (obtenue par $E_3+2E_1$), et non $17y+z=7$. La suite ($90z=-79$) et la solution finale sont justes.
> - **Partie B 2(c)** : l’image n’est pas égale à $\mathbb C^*$ (ensemble d’arrivée), la source écrit $\mathbb C$.

**Cycle préparatoire 1ère année — Devoir surveillé 4**
M. Bahtiti, K. Guezguez, A. Hajej, B. Laquerriere, J.-M. Masereel

| Matière | Date | Durée | Nombre de pages |
| --- | --- | --- | --- |
| Algèbre | Jeudi 11 mars 2021 | 1 heures 30 minutes | 5 |

Appareils électroniques et documents interdits.

**Il sera tenu compte de la qualité de la rédaction et de la précision des justifications.** *Le sujet comporte cinq exercices. L’ordre dans lequel ceux-ci sont traités n’est pas imposé.*

## Exercice 1 (Groupes : 3 points)

1. Montrer que $(\mathbb U,\times)$ est groupe.
2. $A=(\{2k\ /\ k\in\mathbb Z\},+)$ et $B=(\{2k+1\ /\ k\in\mathbb Z\},+)$ sont-ils des sous-groupes de $(\mathbb Z,+)$ ?
3. $C=\left(\{a\sqrt2+b\pi\ /\ a,b\in\mathbb Z\},+\right)$ est-il un sous-groupe de $(\mathbb R,+)$ ?
4. Soit $\mathbb R^2$ muni de la loi $\star$ définie par :
   $$(a,b)\star(a',b')=(a-2a',b+3b')$$
   $(\mathbb R^2,\star)$ est-il un groupe ?

◇◇◇

1. (0.75 point) On montre que c’est un sous-groupe de $(\mathbb C,\times)$ :
   - $\mathbb U\subset\mathbb C$
   - $|1|=1$ donc $1\in\mathbb U$.
   - Soit $z$ et $z'$ dans $\mathbb U$, alors $\left|\frac z{z'}\right|=\frac{|z|}{|z'|}=\frac11=1$. Donc $\frac z{z'}\in\mathbb U$.
2. - (0.75 point)
     - $A\subset\mathbb Z$
     - $0=2\times0$, donc $0\in A$.
     - Soit $n=2k$ et $n'=2k'$ dans $A$, alors $n-n'=2(k-k')$ avec $k-k'\in\mathbb Z$, donc $n-n'\in A$.

     Donc $A$ est bien un sous-groupe de $\mathbb Z$.
   - (0.25 points) $B$ n’est pas stable par addition car la somme de nombres impaires est paire.
3. (0.75 point)
   - $C\in\mathbb R$.
   - $0=0\sqrt2+0\pi\in C$.
   - Soit $r=a\sqrt2+b\pi$ et $r'=a'\sqrt2+b'\pi$ deux éléments de $C$. Alors $r-r'=(a-a')\sqrt2+(b-b')\pi$ avec $(a-a')\in\mathbb Z$ et $(b-b')\in\mathbb Z$. Donc $r-r'\in C$.

   Donc $C$ est un sous-groupe de $(\mathbb R,+)$.
4. (0.5 point)
   - Nous avons clairement une l.c.i.
   - Soit $(a,b)$, $(a',b')$ et $(a'',b'')$ trois éléments de $\mathbb R^2$. Alors
     $$\begin{aligned}
     ((a,b)\star(a',b'))\star(a'',b'')&=(a-2a',b+3b')\star(a'',b'')=(a-2a'-2a'',b+3b'+3b'')\\
     (a,b)\star((a',b')\star(a'',b''))&=(a,b)\star(a'-2a'',b'+3b'')=(a-2a'-4a'',b+3b'+9b'')
     \end{aligned}$$
     La loi n’est donc pas associative. Ce n’est donc pas un groupe.
     On peut aussi remarquer que le seul élément neutre possible à droite est $(0,0)$ qui n’est pas neutre à gauche.

## Exercice 2 (Groupes et Morphismes : 4 points)

Soit $(G,\top)$ et $(G',\star)$ deux groupes, et soit $f$ un morphisme de groupes de $(G,\top)$ dans $(G',\star)$.

1. Si $e$ est l’élément neutre de $(G,\top)$ et $e'$ est l’élément neutre de $(G',\star)$, montrer que $f(e)=e'$.
2. Montrer que pour tout $x$ de $G$, $f(x)^{-1}=f(x^{-1})$.
3. Soit $H$ un sous-groupe de $G$. Montrer que $f(H)$ est un sous-groupe de $G'$.
4. Montrer que $\operatorname{Ker}(f)$ est un sous-groupe de $(G,\top)$

◇◇◇

1. (1 point) Nous avons $e\top e=e$ et $f$ étant un morphisme, cela donne $f(e)\star f(e)=f(e)=f(e)\star e'$. Donc en simplifiant par $f(e)$ (on a le droit car on est dans un groupe), $f(e)=e'$.
2. (1 point) Pour tout $x$ dans $G$, nous avons $e=x\top x^{-1}=x^{-1}\top x$. Donc par morphisme, $e'=f(e)=f(x)\star f(x^{-1})=f(x^{-1})\star f(x)$. Donc $f(x)^{-1}=f(x^{-1})$.
3. (1 point)
   - $f(H)\subset G'$.
   - $e\in H$, donc $e'=f(e)\inf(H)$.
   - Soit $y$ et $y'$ dans $f(H)$, alors il existe $x$ et $x'$ tels que $y=f(x)$ et $y'=f(x')$. Ainsi, $y\star y'^{-1}=f(x)\star f(x')^{-1}=f(x\top x'^{-1})$. Or $x\top x'^{-1}\in H$ car $H$ est un groupe. Ainsi, $y\star y'^{-1}\in f(H)$.
4. (1 point)
   - $\operatorname{Ker}(f)\subset G$.
   - $e'=f(e)$, donc $e\in\operatorname{Ker}(f)$.
   - Soit $x$ et $'$ deux éléments de $\operatorname{Ker}(f)$, alors $f(x\top x'^{-1})=f(x)\star(f(x'))^{-1}=e'\star e'=e'$. Donc $x\top x'\in\operatorname{Ker}(f)$.

   Donc $\operatorname{Ker}(f)$ est un sous-groupe de $G$.

## Exercice 3 (Groupes et Morphismes : 3 points)

Soit $\star$ la loi de composition interne définie sur $\mathbb R$ par :

$$\forall(x,y)\in\mathbb R^2,\ x\star y=\left(x^3+y^3\right)^{\frac13}$$

1. Montrer que $(\mathbb R,\star)$ est un groupe commutatif.
2. Montrer que $f:(\mathbb R,+)\to(\mathbb R,\star)$ définie par $f(x)=x^{\frac13}$ est un isomorphisme de groupes.

◇◇◇

1. (2 points)
   - La loi $\star$ est clairement une lci.
   - La loi est clairement commutative.
   - Soit $x$, $y$ et $z$ trois réels. Alors
     $$\begin{aligned}
     x\star(y\star z)&=x\star\left(y^3+z^3\right)^{\frac13}=\left(x^3+y^3+z^3\right)^{\frac13}\\
     (x\star y)\star z&=\left(x^3+y^3\right)^{\frac13}\star z=\left(x^3+y^3+z^3\right)^{\frac13}
     \end{aligned}$$
     La loi est donc associative.
   - Pour tout $x$ dans $\mathbb R$, $x\star0=0\star x=(x^3)^{\frac13}=x$ (la fonction $x\mapsto x^{\frac13}$ est la bijection réciproque de la fonction cube dans $\mathbb R$). Donc $0$ est l’élément neutre.
   - Soit $x\in\mathbb R$, alors $x\star(-x)=(-x)\star x=\left(x^3+(-x)^3\right)^{\frac13}=\left(x^3-x^3\right)^{\frac13}=0$. Donc tout élément est inversible.

   Ainsi, $(\mathbb R,\star)$ est bien un groupe commutatif.
2. (1 point)
   - Vérifions que c’est un morphisme : Soit $x$ et $y$ deux réels, alors
     $$f(x)\star f(y)=\left(f(x)^3+f(y)^3\right)^{\frac13}=(x+y)^{\frac13}=f(x+y)$$
   - Nous savons déjà que la fonction $f$ est bijective, de réciproque $x\mapsto x^3$.

   La fonction $f$ est donc bien un morphisme de groupe entre $(\mathbb R,+)$ et $(\mathbb R,\star)$.

## Exercice 4 (Groupes et Morphismes : 11 points)

**Partie A :** Soit $\alpha$ un nombre complexe non nul vérifiant $\alpha^2=\alpha-1$ (on ne demande pas de calculer $\alpha$).

1. (a) Montrer que $\alpha^3=-1$.
   (b) Soit $k\in\mathbb N$. Calculer, $\alpha^{3k}$, $\alpha^{3k+1}$ et $\alpha^{3k+2}$ en fonction de $\alpha$.
   (c) En déduire $\alpha^n$ pour tout $n\in\mathbb N$.
   (d) Soit $p\in\mathbb Z$, déterminer $\alpha^p$ en fonction de $\alpha$ (et de $p$).
2. (a) Montrer que $H=\{n\in\mathbb Z\ /\ \alpha^n=1\}$ est un sous groupe de $(\mathbb Z;+)$.
   (b) Montrer que $H=6\mathbb Z=\{6z\ /\ z\in\mathbb Z\}$.
3. Déterminer le plus petit sous-groupe $G$, de $\mathbb C^*$, contenant $\alpha$.

**Partie B :** Soit $\beta\in\mathbb C^*$, on note $\varphi_\beta$ l’application :

$$\varphi_\beta:\begin{cases}\mathbb Z\longrightarrow\mathbb C^*\\ n\longmapsto\beta^n\end{cases}$$

1. Montrer que pour tout $\beta\in\mathbb C^*$, $\varphi_\beta$ est une morphisme de groupe.
2. Soit $\alpha$ le nombre complexe défini dans la partie $A$.
   (a) Montrer que $\operatorname{Ker}\varphi_\alpha=H$.
   (b) Montrer que $\operatorname{Im}\varphi_\alpha=G$.
   (c) L’application $\varphi_\alpha$ est-elle injective ? surjective ?
3. À quelle(s) condition(s) sur $\beta$, l’application $\varphi_\beta$ est injective ?

◇◇◇

**Partie A :**

1. (a) (0.5 point) $\alpha^3=\alpha\times\alpha^2=\alpha(\alpha-1)=\alpha^2-\alpha=\alpha-1-\alpha=-1$
   (b) (1 point) Nous avons alors $\alpha^{3k}=(-1)^k=-1$ si $k$ est impair et $1$ si $k$ est pair.
   Ensuite, $\alpha^{3k+1}=\alpha^{3k}\alpha=\pm\alpha$ suivant la parité de $k$.
   De même, $\alpha^{3k+2}=\pm(\alpha-1)$ suivant la parité de $k$.
   (c) (0.5 point) Il y a donc 6 cas possibles :

   | | | |
   | --- | --- | --- |
   | $\alpha^{6k}=1$ | $\alpha^{6k+1}=\alpha$ | $\alpha^{6k+2}=\alpha-1$ |
   | $\alpha^{6k+3}=-1$ | $\alpha^{6k+4}=-\alpha$ | $\alpha^{6k+5}=1-\alpha$ |

   (d) (0.5 point) Nous remarquons simplement que $\alpha^6=1$, donc $\alpha^{-1}=\alpha^5=1-\alpha=\alpha^{6(-1)+5}$. Ainsi, la formule trouvée précédemment est encore valable pour $k\in\mathbb Z$.
2. (a) (1 point)
   - $H\subset\mathbb Z$.
   - $\alpha^0=1$ donc $0\in H$.
   - Soit $n$ et $n'$ éléments de $H$, alors $\alpha^{n-n'}=\frac{\alpha^n}{\alpha^{n'}}=\frac11=1$. Donc $n-n'\in H$.

   Donc $H$ est un sous groupe de $\mathbb Z$.
   (b) (1 point) On a montré à la question précédente que $\alpha^n=1$ si et seulement si $n$ est un multiple de 6. Donc on a bien $H=6\mathbb Z$.
3. (2 points) Soit $Q$ un sous-groupe contenant $\alpha$. Par stabilité par produit et passage à l’inverse, il doit nécessairement contenir toutes les puissances de $\alpha$. Ainsi, d’après ce qui précède :
   $$P=\{\alpha^p\ /\ p\in\mathbb Z\}=\{1,\alpha,\alpha-1,-1,-\alpha,1-\alpha\}\subset Q$$
   Or :
   - $P\subset\mathbb C^*$
   - $1\in P$
   - Si $z_1$ et $z_2$ sont deux éléments de $P$, alors $\frac{z_1}{z_2}=\frac{\alpha^{p_1}}{\alpha^{p_2}}=\alpha^{p_1-p_2}\in P$.

   Ainsi $P$ est un sous-groupe (contenant $\alpha$). Donc puisqu’il contient tous les sous-groupes contenant $\alpha$, c’est le plus petit. Ainsi, $P=G$.

   > La source écrit « puisqu’il contient tous les sous-groupes » ; le raisonnement établit en fait que $P$ est **contenu dans** tout sous-groupe contenant $\alpha$.

**Partie B :**

1. (1 point) Soit $\beta\in\mathbb C^*$, $n\in\mathbb Z$ et $n'\in\mathbb Z$. Alors
   $$\varphi_\beta(n+n')=\beta^{n+n'}=\beta^n\times\beta^{n'}=\varphi_\beta(n)\times\varphi_\beta(n')$$
   Donc $\varphi_\beta$ est bien un morphisme de groupe entre $(\mathbb Z,+)$ et $(\mathbb C^*,\times)$.
2. (a) (0.5 point) Par définition du noyau, $\operatorname{Ker}(\varphi_\alpha)=\{n\in\mathbb Z\ /\ \alpha^n=1\}=H$.
   (b) (1 point) Soit $z\in\operatorname{Im}(\varphi_\alpha)$. Alors il existe $n\in\mathbb Z$ tel que $z=\alpha^n$, donc $z\in G$. Réciproquement, si $z\in G$, alors $z$ s’écrit $z=\alpha^n\in\operatorname{Im}(\varphi_\alpha)$. D’où l’égalité.
   (c) (1 point) Le noyau n’étant pas réduit à l’élément neutre, elle n’est pas injective et l’image n’était pas égale à $\mathbb C$ tout entier, elle n’est pas surjective.
3. (1 point) L’application est injective si et seulement si, pour tout $n$ non nul, $\beta^n\neq1$. Or s’il existe $n\neq0$ tel $\beta^n=1$, alors nécessairement $|\beta|=1$. Ainsi, si $|\beta|\neq1$, on est sûr que l’application n’est pas injective. Par contre, si $|\beta|=1$, on ne peut pas conclure. En effet, on sait qu’il existe des complexe (comme les racines n-ièmes de l’unitté) tel que $\varphi$ n’est pas injective. Mais il existe aussi des complexes de module un qui ne sont jamais racine n-ième de l’unité (par exemple $e^{i\sqrt2}$ vérifie que pour tout $n\in\mathbb Z$, $e^{ni\sqrt2}\neq1$ (car $n\sqrt2\neq2k\pi$).

   > Coquille de la source : si $|\beta|\neq1$, l’application **est** injective ; la source écrit « n’est pas injective ».

## Exercice 5 (Systèmes linéaires : 3 points)

Ayant à résoudre le système linéaire suivant :

$$\begin{cases}2x+7y+z=1 & (E_1)\\ 2x+3y-5z=4 & (E_2)\\ -4x+3y+z=5 & (E_3)\end{cases}$$

un étudiant démarre ainsi :

- j’élimine $x$ en retranchant $(E_2)$ de $(E_1)$ : $4y+6z=-3$
- j’élimine $y$ en retranchant $(E_3)$ de $(E_2)$ : $6x-6z=-1$
- j’élimine $z$ en retranchant $(E_1)$ de $(E_3)$ : $-6x-4y=4$

1. Le système ainsi obtenu est-il équivalent au système initial ?
2. Résoudre le système initial par la méthode de Gauss.

◇◇◇

1. (1 point) Il y a plusieurs niveaux de réponse acceptables.
   - L’élève n’a pas respecté scrupuleusement l’algorithme de Gauss. On ne peut donc pas certifier que les systèmes sont équivalents (même si peut-être, par chance, ils le sont).
   - En résolvant les 2 systèmes (et donc en faisant la question 2 avant), on remarque que l’on n’a pas le même ensemble de solution.
   - En calculant les rangs et trouvant qu’ils sont différents.
2. (2 points) Le système est équivalent successivement à
   $$\begin{cases}2x+7y+z=1\\ 4y+6z=-3\\ 17y+z=7\end{cases}\qquad\begin{cases}2x+7y+z=1\\ 4y+6z=-3\\ 90z=-79\end{cases}\qquad\begin{cases}x=-\frac{47}{45}\\ y=\frac{17}{30}\\ z=-\frac{79}{90}\end{cases}$$

   > Dans la seconde équation intermédiaire, la source remplace $(E_2)$ par $(E_1)-(E_2)$ ; la première équation de l’élève est donc reprise telle quelle.
