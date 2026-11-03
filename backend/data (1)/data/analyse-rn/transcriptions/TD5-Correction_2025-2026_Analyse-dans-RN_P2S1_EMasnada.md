---
source: TD-Correction_2022-2023_Analyse-dans-RN_P2S1_EMasnada.pdf, pages 50 à 65 (ancienne correction, avant réforme)
transcription: manuelle, énoncés de la feuille 2025-2026 et correction réorganisée selon sa numérotation
---

# TD5 — Limites et continuité (corrigé)

## Exercice 1 : Limite le long de droites et de paraboles

**Énoncé.** On considère la fonction $f$ définie par
$$f(x, y) = \begin{cases} \dfrac{|y|}{x^2}\, e^{-|y|/x^2} & \text{pour } x \ne 0 \\ 0 & \text{pour } x = 0 \end{cases}$$

1. Soit $\lambda$ un réel et $A_\lambda = \{(x, \lambda x) \,/\, x \in \mathbb{R}\}$. On note $f_\lambda$ la restriction de $f$ à $A_\lambda$. Calculer la limite de $f_\lambda$ en $(0, 0)$.
2. Soit $B = \{(x, x^2) \,/\, x \in \mathbb{R}\}$. On note $g$ la restriction de $f$ à $B$. Calculer la limite de $g$ en $(0, 0)$.
3. Que peut-on dire de la continuité de $f$ en $(0, 0)$ ?

**Correction.**

**1.** Pour $x \ne 0$, $f(x, \lambda x) = \dfrac{|\lambda|}{|x|}\, e^{-|\lambda|/|x|}$ (et $f(0, 0) = 0$).

- Si $\lambda = 0$, $f_\lambda$ est nulle.
- Si $\lambda \ne 0$, posons $t = \frac{|\lambda|}{|x|}$, qui tend vers $+\infty$ quand $x \to 0$. Par croissances comparées, $t\, e^{-t} \to 0$.

Dans tous les cas, $\lim_{(0,0)} f_\lambda = 0$ : le long de **toute droite** passant par l'origine, $f$ tend vers $0 = f(0,0)$. (Sur l'axe $x = 0$, qui n'est pas de la forme $A_\lambda$, $f$ est nulle aussi.)

**2.** Pour $x \ne 0$, $f(x, x^2) = \dfrac{x^2}{x^2}\, e^{-x^2/x^2} = e^{-1}$. Donc $\lim_{(0,0)} g = \frac{1}{e}$.

**3.** Si $f$ avait une limite $\ell$ en $(0,0)$, toutes ses restrictions auraient la même limite $\ell$. Or elle tend vers $0$ le long des droites et vers $\frac{1}{e}$ le long de la parabole $y = x^2$ : $f$ n'a pas de limite en $(0, 0)$, et n'y est donc pas continue.

> **Remarque :** c'est l'exemple classique qui montre qu'étudier toutes les droites passant par un point **ne suffit pas** pour prouver l'existence d'une limite.

## Exercice 2 : Majorer pour trouver la limite

**Énoncé.**

1. Montrer que si $x$ et $y$ sont des réels, alors $2|xy| \le x^2 + y^2$.
2. Soit $f$ l'application de $A = \mathbb{R}^2 \setminus \{(0,0)\}$ dans $\mathbb{R}$ définie par $f(x, y) = \dfrac{3x^2 + xy}{\sqrt{x^2 + y^2}}$.
    a) Montrer que pour tout $(x, y) \in A$, $|f(x, y)| \le \frac{7}{2}\|(x, y)\|_2$, avec $\|(x, y)\|_2 = \sqrt{x^2 + y^2}$.
    b) En déduire que $f$ admet une limite en $(0, 0)$.

**Correction.**

**1.** $0 \le (|x| - |y|)^2 = x^2 + y^2 - 2|xy|$, donc $2|xy| \le x^2 + y^2$.

**2. a)** Notons $\|\cdot\| = \|(x,y)\|_2$. Par l'inégalité triangulaire,
$$|f(x, y)| \le \frac{3x^2}{\|(x,y)\|} + \frac{|xy|}{\|(x,y)\|}$$
Or $x^2 \le x^2 + y^2 = \|(x,y)\|^2$, et d'après la question 1, $|xy| \le \frac{1}{2}\|(x,y)\|^2$. Donc
$$|f(x, y)| \le \frac{3\|(x,y)\|^2}{\|(x,y)\|} + \frac{\|(x,y)\|^2}{2\|(x,y)\|} = \frac{7}{2}\|(x,y)\|$$

**2. b)** Quand $(x, y) \to (0, 0)$, $\|(x,y)\| \to 0$, donc $|f(x, y) - 0| \le \frac{7}{2}\|(x,y)\| \to 0$ : $\lim_{(0,0)} f = 0$.

> **Erreurs corrigées :** l'ancienne correction annonçait « montrons que $|f| \le 4\|(x,y)\|_2$ » (l'énoncé et le calcul donnent $\frac{7}{2}$), écrivait $|f| = \dots$ au lieu de $|f| \le \dots$, et confondait $\|(x,y)\|_2$ et $\|(x,y)\|_2^2$ dans « $x^2 \le \|(x,y)\|_2$ » et « $\sqrt{x^2 + y^2} = \|(x,y)\|_2^2$ ».

## Exercice 3 : Treize limites en (0, 0)

**Énoncé.** Étudier les limites en $(0, 0)$ des fonctions suivantes :

1. $f(x, y) = (x + y)\sin\Big(\dfrac{1}{x^2 + y^2}\Big)$
2. $f(x, y) = \dfrac{1}{x - y}$
3. $f(x, y) = \dfrac{x^2 - y^2}{x^2 + y^2}$
4. $f(x, y) = \dfrac{x^2 + xy + y^2}{x^2 + y^2}$
5. $f(x, y) = \dfrac{x^2 y}{x^2 + y^2}$
6. $f(x, y) = \dfrac{x^2 y^2}{x^2 + y^2}$
7. $f(x, y) = \dfrac{x^3}{y}$
8. $f(x, y) = \dfrac{x + 3y}{x^2 - y^2}$
9. $f(x, y) = \dfrac{x^2 + y^2}{|x| + |y|}$
10. $f(x, y) = \dfrac{xy}{\sqrt{x^2 + y^2}}$
11. $f(x, y) = \dfrac{\sin(xy)}{\sqrt{x^2 + y^2}}$
12. $f(x, y) = x^y$
13. $f(x, y) = \Big(\dfrac{x^2 + y^2 - 1}{x}\sin(x),\ \dfrac{\sin(x^2) + \sin(y^2)}{\sqrt{x^2 + y^2}}\Big)$

**Correction.** Deux stratégies :

- **pour montrer qu'il n'y a pas de limite**, on trouve deux chemins (ou deux suites) qui tendent vers $(0,0)$ et donnent deux limites différentes ;
- **pour montrer qu'une limite $\ell$ existe**, on majore $|f(x,y) - \ell|$ par une quantité qui tend vers $0$ (souvent avec $2|xy| \le x^2 + y^2$), ou on passe en coordonnées polaires $x = \rho\cos\theta$, $y = \rho\sin\theta$ en majorant **indépendamment de $\theta$**.

**1. Limite $0$.** $|\sin| \le 1$ donc $|f(x, y)| \le |x + y| \le |x| + |y| \to 0$.

**2. Pas de limite** (domaine $x \ne y$). Sur l'axe $(x, 0)$ avec $x \to 0^+$ : $f(x, 0) = \frac{1}{x} \to +\infty$. Sur l'axe $(0, y)$ avec $y \to 0^+$ : $f(0, y) = -\frac{1}{y} \to -\infty$. Avec des suites : $f(\frac{1}{n}, 0) = n$ et $f(0, \frac{1}{n}) = -n$. En polaires : $f = \frac{1}{\rho(\cos\theta - \sin\theta)}$, dont le signe dépend de $\theta$.

**3. Pas de limite.** $f(x, 0) = 1$ et $f(0, y) = -1$. En polaires : $f = \cos^2\theta - \sin^2\theta = \cos(2\theta)$, qui dépend de $\theta$.

**4. Pas de limite.** $f(x, 0) = 1$ et $f(x, x) = \frac{3x^2}{2x^2} = \frac{3}{2}$. En polaires : $f = 1 + \cos\theta\sin\theta$.

**5. Limite $0$.** Sur les axes et sur $y = x$, $f$ tend vers $0$ : c'est le candidat. Avec $|xy| \le \frac{1}{2}(x^2 + y^2)$ :
$$|f(x, y)| = \frac{|xy| \cdot |x|}{x^2 + y^2} \le \frac{|x|}{2} \to 0$$
En polaires : $f = \rho\cos^2\theta\sin\theta$, et $|f| \le \rho \to 0$ quel que soit $\theta$.

**6. Limite $0$.** Même méthode : $|f(x, y)| = \dfrac{|xy| \cdot |xy|}{x^2 + y^2} \le \dfrac{|xy|}{2} \to 0$.

**7. Pas de limite** (domaine $y \ne 0$). $f(x, x^3) = 1$ pour $x \ne 0$, alors que $f(x, x) = x^2 \to 0$. Avec des suites : $u_n = (\frac{1}{n}, \frac{1}{n^3})$ donne $f(u_n) = 1$, et $v_n = (\frac{1}{n}, \frac{1}{n})$ donne $f(v_n) = \frac{1}{n^2} \to 0$.

**8. Pas de limite** (domaine $x \ne \pm y$). $f(x, 0) = \frac{1}{x}$ tend vers $+\infty$ quand $x \to 0^+$ et vers $-\infty$ quand $x \to 0^-$.

**9. Limite $0$.** Comme $(|x| + |y|)^2 = x^2 + y^2 + 2|xy| \ge x^2 + y^2$ :
$$|f(x, y)| = \frac{x^2 + y^2}{|x| + |y|} \le \frac{(|x| + |y|)^2}{|x| + |y|} = |x| + |y| \to 0$$
En polaires : $f = \dfrac{\rho}{|\cos\theta| + |\sin\theta|}$ et $|\cos\theta| + |\sin\theta| \ge 1$, donc $|f| \le \rho$.

**10. Limite $0$.** $|f(x, y)| = \dfrac{|xy|}{\sqrt{x^2 + y^2}} \le \dfrac{x^2 + y^2}{2\sqrt{x^2 + y^2}} = \dfrac{1}{2}\sqrt{x^2 + y^2} \to 0$.

**11. Limite $0$.** Comme $|\sin u| \le |u|$ : $|f(x, y)| \le \dfrac{|xy|}{\sqrt{x^2 + y^2}} \le \dfrac{1}{2}\sqrt{x^2 + y^2} \to 0$.

**12. Pas de limite** (domaine $x > 0$). $f(x, y) = e^{y\ln x}$. Avec $u_n = (\frac{1}{n}, 0)$ : $f(u_n) = 1$. Avec $v_n = \big(\frac{1}{n}, \frac{1}{\ln n}\big)$ (qui tend bien vers $(0,0)$) : $f(v_n) = e^{-\ln n / \ln n} = \frac{1}{e}$.

**13. Limite $(-1, 0)$** (domaine $x \ne 0$). Une fonction à valeurs dans $\mathbb{R}^2$ a une limite si et seulement si chacune de ses composantes en a une.

- Première composante : $\frac{\sin x}{x} \to 1$ et $x^2 + y^2 - 1 \to -1$, donc elle tend vers $-1$.
- Deuxième composante : $|\sin(x^2) + \sin(y^2)| \le x^2 + y^2$, donc elle est majorée en valeur absolue par $\frac{x^2 + y^2}{\sqrt{x^2 + y^2}} = \sqrt{x^2 + y^2} \to 0$.

> **Compléments :** l'ancienne correction laissait les cas 6 et 13 sans corrigé, et le cas 7 renvoyait les suites « en exercice » ; ils ont été rédigés. Pour le cas 8, elle proposait les chemins $(0, -x)$ et $(0, x)$, qui ne suffisent pas ; l'axe $(x, 0)$ conclut directement. La remarque en polaires du cas 7 (« il est très difficile de conclure ») a été retirée.

## Exercice 4 : Une limite par produit

**Énoncé.** On considère la fonction $f : \mathbb{R} \times \mathbb{R}^* \to \mathbb{R}$, $(x, y) \mapsto (1 + x^2 + y^2)\,\dfrac{\sin(y)}{y}$. Déterminer si $f$ admet une limite en $(0, 0)$.

**Correction.** C'est un produit de deux fonctions qui ont une limite en $(0, 0)$ :
$$\lim_{(x,y) \to (0,0)} (1 + x^2 + y^2) = 1 \qquad \lim_{(x,y) \to (0,0)} \frac{\sin y}{y} = 1$$
(la seconde ne dépend que de $y$, qui tend vers $0$). Donc $\lim_{(0,0)} f = 1 \times 1 = 1$ : $f$ se prolonge par continuité en $(0,0)$ en posant $f(0, 0) = 1$.

> **Note :** c'est la question 1 de l'ancien exercice 4 ; la question 2 n'est plus dans la feuille 2025-2026.

## Exercice 5 : Continuité en (0, 0)

**Énoncé.** Pour chacune des fonctions, étudier sa continuité en $(0, 0)$ :

1. $f(x, y) = \dfrac{(x + y)^2}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$ ;
2. $f(x, y) = \dfrac{x^3 + y^3}{x^2 + y^2}$ si $(x, y) \ne (0, 0)$, et $f(0, 0) = 0$ ;
3. $f(x, y) = e^{-\left(\frac{x}{y} + \frac{y}{x}\right)^2}$ si $x \ne 0$ et $y \ne 0$, et $f(x, y) = 0$ si $x = 0$ ou $y = 0$.

**Correction.**

**1. Pas continue.** En polaires, $(x + y)^2 = \rho^2(\cos\theta + \sin\theta)^2 = \rho^2(1 + \sin 2\theta)$, donc
$$f(\rho\cos\theta, \rho\sin\theta) = 1 + \sin(2\theta)$$
qui dépend de $\theta$ : $f$ n'a pas de limite en $(0, 0)$. Par exemple $f(x, 0) = 1$ et $f(x, -x) = 0$.

> **Erreur corrigée :** l'ancienne correction trouvait $\tilde f(\rho, \theta) = \cos^2\theta + \sin^2\theta = 1$, en oubliant le double produit $2xy$ de $(x+y)^2$. Sa conclusion (« pas continue ») restait juste, mais pas pour la bonne raison.

**2. Continue.**
$$|f(x, y)| \le \frac{|x|\,x^2 + |y|\,y^2}{x^2 + y^2} = |x|\frac{x^2}{x^2 + y^2} + |y|\frac{y^2}{x^2 + y^2} \le |x| + |y| \to 0 = f(0, 0)$$

**3. Pas continue.** Pour $x \ne 0$, $f(x, x) = e^{-(1 + 1)^2} = e^{-4}$, qui ne tend pas vers $f(0, 0) = 0$.

## Exercice 6 : Prolongement par continuité

**Énoncé.** Les fonctions suivantes sont-elles prolongeables par continuité en $(0, 0)$ sur leur domaine de définition $D$ ?

1. $D = \{(x, y) \in \mathbb{R}^2 \,/\, xy > 0\}$, $f(x, y) = \dfrac{1 - \cos(\sqrt{xy})}{y}$
2. $D = \{(x, y) \in \mathbb{R}^2 \,/\, x \ne y\}$, $f(x, y) = \dfrac{\cos(x) - \cos(y)}{x - y}$
3. $D = \{(x, y) \in \mathbb{R}^2 \,/\, x \ne \pm y\}$, $f(x, y) = \dfrac{\sin(x^2) + \sin(y^2)}{x^2 - y^2}$
4. $D = \mathbb{R}^2 \setminus \{(0, 0)\}$, $f(x, y) = \dfrac{xy^2}{x^2 + y^4}$

**Correction.**

**1. Oui, par $0$.** Pour tout réel $u$, $0 \le 1 - \cos u \le \frac{u^2}{2}$. Avec $u = \sqrt{xy}$ :
$$|f(x, y)| \le \frac{xy}{2|y|} = \frac{|x|}{2} \to 0$$
On prolonge en posant $f(0, 0) = 0$.

**2. Oui, par $0$** (et même en tout point $(a, a)$). On utilise $\cos x - \cos y = -2\sin\big(\frac{x+y}{2}\big)\sin\big(\frac{x-y}{2}\big)$ :
$$f(x, y) = -\sin\Big(\frac{x + y}{2}\Big) \cdot \frac{\sin\big(\frac{x-y}{2}\big)}{\frac{x-y}{2}}$$
Quand $(x, y) \to (a, a)$ avec $x \ne y$, le premier facteur tend vers $-\sin(a)$ et le second vers $1$ (car $\frac{\sin u}{u} \to 1$ quand $u \to 0$). Donc $f$ tend vers $-\sin(a)$ ; en $(0,0)$, on prolonge par $f(0, 0) = 0$.

> **Erreur corrigée :** l'ancienne correction écrivait la formule avec $\cos(x) - \sin(x)$ au lieu de $\cos(x) - \cos(y)$.

**3. Non.** $f(x, 0) = \frac{\sin(x^2)}{x^2} \to 1$ et $f(0, y) = \frac{\sin(y^2)}{-y^2} \to -1$.

**4. Non.** Sur la droite $y = x$ : $f(x, x) = \frac{x^3}{x^2 + x^4} = \frac{x}{1 + x^2} \to 0$. Sur la parabole $x = y^2$ : $f(y^2, y) = \frac{y^4}{2y^4} = \frac{1}{2}$. Deux limites différentes.

## Exercice 7 : Continuité d'une fonction définie par morceaux

**Énoncé.** Soit $f$ la fonction définie sur $\mathbb{R}^2$ par
$$f(x, y) = \begin{cases} \frac{1}{2}x^2 + y^2 - 1 & \text{pour } x^2 + y^2 > 1 \\ -\frac{1}{2}x^2 & \text{pour } x^2 + y^2 \le 1 \end{cases}$$
Montrer que $f$ est continue.

**Correction.** Notons $P(x, y) = \frac{1}{2}x^2 + y^2 - 1$ et $Q(x, y) = -\frac{1}{2}x^2$ : ce sont des polynômes, donc des fonctions continues sur $\mathbb{R}^2$.

- **Hors du cercle** ($x^2 + y^2 \ne 1$) : l'ouvert $\{x^2 + y^2 > 1\}$ (resp. $\{x^2 + y^2 < 1\}$) contient une boule autour du point, sur laquelle $f = P$ (resp. $f = Q$) ; $f$ y est donc continue.
- **Sur le cercle** ($x_0^2 + y_0^2 = 1$) : $f(x_0, y_0) = Q(x_0, y_0) = -\frac{1}{2}x_0^2$, et comme $y_0^2 = 1 - x_0^2$,
$$P(x_0, y_0) = \frac{1}{2}x_0^2 + (1 - x_0^2) - 1 = -\frac{1}{2}x_0^2 = Q(x_0, y_0)$$
Quand $(x, y) \to (x_0, y_0)$, $f(x, y)$ vaut $P(x, y)$ ou $Q(x, y)$, qui tendent tous deux vers la même valeur $-\frac{1}{2}x_0^2$. Donc $f$ est continue en $(x_0, y_0)$.

Finalement $f$ est continue sur $\mathbb{R}^2$.
