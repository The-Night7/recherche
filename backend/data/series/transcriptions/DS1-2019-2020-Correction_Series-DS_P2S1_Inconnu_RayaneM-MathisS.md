---
source: DS1-2019-2020-Correction_Series-DS_P2S1_Inconnu_RayaneM-MathisS.pdf, pages 1 à 5 (corrigé manuscrit ; énoncés : DS1-2019-2020_Series-DS_P2S1_KFayad-KGuezguez-NZoghlami-AElJanati.pdf, pages 1 et 2)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (octobre 2019) (corrigé)

Devoir du vendredi 18 octobre 2019 (A. El Janati, K. Fayad, K. Guezguez, N. Zoghlami). Durée 2 heures, appareils électroniques et documents interdits.

> **Note :** l'en-tête du sujet porte « Devoir surveillé 2 », mais il s'agit bien du premier devoir du semestre (18 octobre). Le corrigé manuscrit numérote les exercices dans un autre ordre (son exercice 1 est l'exercice 3 du sujet, ses exercices 2 et 3 sont les exercices 1 et 2) ; on suit ici la numérotation du sujet.

## Exercice 1 : Séries de terme général uₙ^α

**Énoncé.** Soit $\sum_{n\geq 1} u_n$ une série à termes positifs et $\alpha > 0$.

1. On suppose dans cette question que $\sum_{n\geq 1} u_n$ converge.
    a) Montrer que $u_n \leq 1$ à partir d'un certain rang.
    b) En déduire que si $\alpha \geq 1$, alors la série $\sum_{n\geq 1} u_n^\alpha$ converge.
2. On suppose dans cette question que $\sum_{n\geq 1} u_n$ diverge. Montrer que si $\alpha \leq 1$, alors la série $\sum_{n\geq 1} u_n^\alpha$ diverge. *On pourra raisonner selon si la divergence est grossière ou pas.*

**Correction.**

**1. a)** La série $\sum u_n$ converge, donc son terme général tend vers $0$. Avec $\varepsilon = \frac{1}{2}$ dans la définition de la limite : il existe $n_0 \in \mathbb{N}$ tel que pour tout $n \geq n_0$, $0 \leq u_n \leq \frac{1}{2}$. En particulier $u_n \leq 1$ à partir du rang $n_0$.

**b)** Pour $n \geq n_0$, $0 \leq u_n \leq 1$ et $\alpha \geq 1$, donc $u_n^\alpha = u_n \cdot u_n^{\alpha - 1} \leq u_n$. Comme $\sum u_n$ converge, le théorème de comparaison des séries à termes positifs donne la convergence de $\sum u_n^\alpha$.

**2.** On distingue deux cas.

- *Divergence grossière* : $(u_n)$ ne tend pas vers $0$. Comme $x \mapsto x^{1/\alpha}$ est continue en $0$ sur $\mathbb{R}_+$, si $u_n^\alpha$ tendait vers $0$, alors $u_n = (u_n^\alpha)^{1/\alpha}$ tendrait aussi vers $0$. Donc $(u_n^\alpha)$ ne tend pas vers $0$ et $\sum u_n^\alpha$ diverge grossièrement.
- *Divergence non grossière* : $u_n \to 0$. Il existe alors $n_0$ tel que $0 \leq u_n \leq 1$ pour $n \geq n_0$, et comme $\alpha \leq 1$, $u_n^\alpha \geq u_n$ (car $u_n^{\alpha} = u_n \cdot u_n^{\alpha-1}$ et $u_n^{\alpha - 1} \geq 1$ si $u_n > 0$ ; l'inégalité est triviale si $u_n = 0$). Comme $\sum u_n$ diverge, le théorème de comparaison (minoration) des séries à termes positifs donne la divergence de $\sum u_n^\alpha$.

## Exercice 2 : Série dépendant de deux paramètres

**Énoncé.** Soit $(a, b) \in \mathbb{R}^2$ tel que $a \geq b$. Le but de cet exercice est d'étudier la série numérique de terme général
$$u_n = \left(\sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1}\right)^n$$
définie à partir d'un certain rang.

1. Donner le développement limité en $\frac{1}{n}$ à l'ordre 1 au voisinage de $+\infty$ de $\sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1}$.
2. On suppose dans cette question que $a - b \neq 2$. Étudier la nature de la série $\sum u_n$.
3. On suppose dans cette question que $a - b = 2$.
    a) Calculer $\lim_{n\to+\infty} \ln(n u_n)$.
    b) Que peut-on en déduire ?

**Correction.**

**1.** On factorise par $n$ et on utilise $\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + o(x^2)$ :
$$\sqrt{n^2 + an + 2} = n\left(1 + \frac{a}{n} + \frac{2}{n^2}\right)^{1/2} = n\left(1 + \frac{a}{2n} + \frac{1}{n^2} - \frac{a^2}{8n^2} + o\left(\frac{1}{n^2}\right)\right)$$
$$\sqrt{n^2 + bn + 1} = n\left(1 + \frac{b}{n} + \frac{1}{n^2}\right)^{1/2} = n\left(1 + \frac{b}{2n} + \frac{1}{2n^2} - \frac{b^2}{8n^2} + o\left(\frac{1}{n^2}\right)\right)$$
En faisant la différence :
$$\sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1} = \frac{a-b}{2} + \frac{4 - a^2 + b^2}{8n} + o\left(\frac{1}{n}\right)$$
Autrement dit, en notant $x_n$ cette différence, $u_n = x_n^n$ et $\sqrt[n]{u_n} = x_n$ dès que $x_n \geq 0$.

**2.** D'après 1, $x_n \to \frac{a-b}{2} \geq 0$. Si $a > b$, $x_n > 0$ à partir d'un certain rang ; si $a = b$, $x_n \sim \frac{1}{2n} > 0$. Dans tous les cas $u_n \geq 0$ à partir d'un certain rang et $\sqrt[n]{u_n} \to \frac{a-b}{2}$. Par la règle de Cauchy :

- si $a - b < 2$, la limite est $< 1$ : $\sum u_n$ **converge** ;
- si $a - b > 2$, la limite est $> 1$ : $\sum u_n$ **diverge** (grossièrement).

**3.** Si $a = b + 2$, alors $a^2 - b^2 = (a-b)(a+b) = 2(a+b)$, donc $\frac{4 - a^2 + b^2}{8} = \frac{2 - a - b}{4}$ et
$$\sqrt[n]{u_n} = 1 + \frac{2 - a - b}{4n} + o\left(\frac{1}{n}\right)$$

**a)** $\ln(n u_n) = \ln n + n\ln\left(\sqrt[n]{u_n}\right) = \ln n + n\ln\left(1 + \frac{2-a-b}{4n} + o\left(\frac{1}{n}\right)\right)$, et
$$n\ln\left(1 + \frac{2-a-b}{4n} + o\left(\frac{1}{n}\right)\right) = \frac{2-a-b}{4} + o(1)$$
Donc $\ln(n u_n) = \ln n + \frac{2-a-b}{4} + o(1) \xrightarrow[n\to+\infty]{} +\infty$.

> **Erreur corrigée :** le corrigé d'origine écrit $\ln(n u_n) = \ln n + 2 - a - b + o(1)$ (il manque le facteur $\frac{1}{4}$) ; la conclusion ($+\infty$) n'est pas affectée.

**b)** Par continuité de l'exponentielle, $n u_n \to +\infty$ ; en particulier $n u_n \geq 1$ à partir d'un certain rang, c'est-à-dire $u_n \geq \frac{1}{n}$. Comme $\sum \frac{1}{n}$ diverge, la série à termes positifs $\sum u_n$ **diverge**.

## Exercice 3 : Une somme télescopique et cinq séries

**Énoncé.**

1. Montrer la convergence et calculer la somme de la série
$$\sum_{n\geq 1} \ln\left(\frac{(n+1)^2}{n(n+2)}\right)$$
2. Étudier la nature de la série numérique $\sum_{n\geq 1} u_n$ dans chacun des cas suivants :
    a) $u_n = n^{\frac{1}{n^2}} - 1$
    b) $u_n = \left(\cos\left(\frac{1}{n}\right)\right)^n - 1$
    c) $u_n = \dfrac{\ln(n)}{n^2}$
    d) $u_n = \sqrt{n^2 + n} - n$
    e) $u_n = \dfrac{(n!)^2}{(2n)!}$

**Correction.**

**1.** On calcule les sommes partielles : pour $n \geq 1$,
$$S_n = \sum_{k=1}^{n} \ln\left(\frac{(k+1)^2}{k(k+2)}\right) = 2\sum_{k=1}^{n}\ln(k+1) - \sum_{k=1}^{n}\ln k - \sum_{k=1}^{n}\ln(k+2)$$
En changeant d'indice :
$$S_n = 2\sum_{k=2}^{n+1}\ln k - \sum_{k=1}^{n}\ln k - \sum_{k=3}^{n+2}\ln k$$
Tous les $\ln k$ pour $3 \leq k \leq n$ se simplifient ($2 - 1 - 1 = 0$) ; il reste
$$S_n = 2\ln 2 + 2\ln(n+1) - \ln 2 - \ln(n+1) - \ln(n+2) = \ln 2 + \ln\left(\frac{n+1}{n+2}\right) \xrightarrow[n\to+\infty]{} \ln 2$$
La série **converge** et sa somme vaut $\ln 2$.

**2. a)** $u_n = e^{\frac{\ln n}{n^2}} - 1$ et $\frac{\ln n}{n^2} \to 0$, donc $u_n \sim \frac{\ln n}{n^2} =: v_n > 0$. Or $n^{3/2} v_n = \frac{\ln n}{\sqrt{n}} \to 0$, donc $v_n = o\left(\frac{1}{n^{3/2}}\right)$ et $\sum v_n$ converge (Riemann, $\frac{3}{2} > 1$). Par équivalence (termes positifs), $\sum u_n$ **converge**.

**b)**

> **Complément :** cette série n'est pas traitée dans le corrigé d'origine.

Pour $n \geq 1$, $\cos\frac{1}{n} \in \,]0, 1[$ donc $u_n < 0$ : la série est de signe constant. On a
$$n\ln\left(\cos\frac{1}{n}\right) = n\ln\left(1 - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right)\right) = -\frac{1}{2n} + o\left(\frac{1}{n}\right)$$
donc $u_n = e^{-\frac{1}{2n} + o(1/n)} - 1 \sim -\frac{1}{2n}$. Ainsi $-u_n \sim \frac{1}{2n}$, terme positif d'une série divergente : $\sum u_n$ **diverge**.

**c)**

> **Complément :** cette série n'est pas traitée dans le corrigé d'origine.

$u_n = \frac{\ln n}{n^2} \geq 0$ et, comme en a), $n^{3/2}u_n = \frac{\ln n}{\sqrt n} \to 0$ : $u_n = o\left(\frac{1}{n^{3/2}}\right)$, donc $\sum u_n$ **converge**.

**d)** Par la quantité conjuguée,
$$u_n = \sqrt{n^2+n} - n = \frac{n}{\sqrt{n^2+n} + n} = \frac{1}{\sqrt{1 + \frac{1}{n}} + 1} \xrightarrow[n\to+\infty]{} \frac{1}{2} \neq 0$$
La série **diverge grossièrement**.

**e)** $u_n > 0$ ; règle de d'Alembert :
$$\frac{u_{n+1}}{u_n} = \frac{((n+1)!)^2}{(n!)^2}\cdot\frac{(2n)!}{(2n+2)!} = \frac{(n+1)^2}{(2n+1)(2n+2)} \xrightarrow[n\to+\infty]{} \frac{1}{4} < 1$$
La série **converge**.

## Exercice 4 : Série harmonique et constante d'Euler

**Énoncé.** Soit $f$ la fonction décroissante définie sur $[1, +\infty[$ par $f(x) = \frac{1}{x}$. Pour $n \in \mathbb{N}^*$, on pose
$$S_n = \sum_{k=1}^{n} f(k)$$

1. Montrer que pour tout $n \in \mathbb{N}^*$,
$$\int_1^{n+1} f(x)\,dx \leq S_n \leq 1 + \int_1^{n} f(x)\,dx$$
2. En calculant les intégrales, déduire un équivalent simple de $S_n$ puis la nature de la série $\sum_{n\geq 1} \frac{1}{n}$.
3. Pour $n \geq 1$, on pose $a_n = S_n - \ln(n)$ et $b_n = S_n - \ln(n+1)$.
    a) Montrer que les deux suites $(a_n)_{n\geq 1}$ et $(b_n)_{n\geq 1}$ sont adjacentes. *Leur limite commune est notée $\gamma$ et est appelée la constante d'Euler.*
    b) Montrer que $S_n = \ln(n) + \gamma + o(1)$.
4. Pour $n \in \mathbb{N}^*$, on pose $u_n = \frac{1}{n(2n+1)}$.
    a) Justifier que la série $\sum_{n\geq 1} u_n$ converge.
    b) Décomposer en éléments simples la fraction rationnelle $F(X) = \frac{1}{X(2X+1)}$.
    c) Soit $N \in \mathbb{N}^*$. En regroupant les entiers pairs et impairs dans la somme $\sum_{n=1}^{2N+1} \frac{1}{n}$, et en utilisant la fraction rationnelle $F$, montrer que
$$\frac{1}{2}\sum_{n=1}^{N} \frac{1}{n(2n+1)} = S_N - S_{2N+1} + 1$$
    d) En déduire que
$$\sum_{n=1}^{+\infty} \frac{1}{n(2n+1)} = 2 - 2\ln(2)$$

> **Erreur corrigée :** le sujet d'origine écrit $\sum_{n=1}^{2N+1} \frac{1}{N}$ (au lieu de $\frac{1}{n}$) et « $= S_N - S_{2N+1} + 2$ » au 4.c) ; la bonne constante est $+1$ (sinon la limite du d) serait $4 - 2\ln 2$). Le corrigé d'origine obtient d'ailleurs $\sum_{n=1}^{N} \frac{1}{n(2n+1)} = 2S_N - 2S_{2N+1} + 2$, ce qui correspond à $+1$.

**Correction.**

**1.** Soit $k \in \mathbb{N}^*$. Pour $x \in [k, k+1]$, $\frac{1}{k+1} \leq \frac{1}{x} \leq \frac{1}{k}$ ($f$ est décroissante). En intégrant sur $[k, k+1]$ (intervalle de longueur $1$) :
$$\frac{1}{k+1} \leq \int_k^{k+1} \frac{dx}{x} \leq \frac{1}{k}$$
En sommant l'inégalité de droite pour $k = 1, \dots, n$ (relation de Chasles) : $\int_1^{n+1} f(x)\,dx \leq S_n$.

En sommant l'inégalité de gauche pour $k = 1, \dots, n-1$ ($n \geq 2$) : $S_n - 1 = \sum_{k=2}^{n}\frac{1}{k} \leq \int_1^{n} f(x)\,dx$. Pour $n = 1$ l'inégalité $S_1 = 1 \leq 1 + 0$ est vraie aussi. D'où l'encadrement.

**2.** Comme $\int_1^{m} \frac{dx}{x} = \ln m$, l'encadrement s'écrit
$$\ln(n+1) \leq S_n \leq 1 + \ln n$$
En divisant par $\ln n > 0$ ($n \geq 2$) :
$$\frac{\ln(n+1)}{\ln n} \leq \frac{S_n}{\ln n} \leq 1 + \frac{1}{\ln n}$$
Or $\frac{\ln(n+1)}{\ln n} = \frac{\ln n + \ln\left(1 + \frac{1}{n}\right)}{\ln n} \to 1$ et $1 + \frac{1}{\ln n} \to 1$. Par encadrement, $\frac{S_n}{\ln n} \to 1$ : $S_n \underset{+\infty}{\sim} \ln n$. En particulier $S_n \to +\infty$ : la série harmonique $\sum \frac{1}{n}$ **diverge**.

**3. a)** On utilise l'inégalité $\ln(1+x) \leq x$ pour $x > -1$. (Elle se prouve en étudiant $g(x) = x - \ln(1+x)$ : $g'(x) = \frac{x}{1+x}$, donc $g$ décroît sur $]-1, 0]$, croît sur $[0, +\infty[$ et $g \geq g(0) = 0$.)

- $a_{n+1} - a_n = \frac{1}{n+1} - \ln(n+1) + \ln n = \frac{1}{n+1} + \ln\left(1 - \frac{1}{n+1}\right) = -g\left(-\frac{1}{n+1}\right) \leq 0$ : $(a_n)$ est décroissante.
- $b_{n+1} - b_n = \frac{1}{n+1} - \ln\left(\frac{n+2}{n+1}\right) = \frac{1}{n+1} - \ln\left(1 + \frac{1}{n+1}\right) = g\left(\frac{1}{n+1}\right) \geq 0$ : $(b_n)$ est croissante.
- $a_n - b_n = \ln(n+1) - \ln n = \ln\left(1 + \frac{1}{n}\right) \to 0$.

Les suites $(a_n)$ et $(b_n)$ sont donc **adjacentes** ; elles convergent vers une même limite $\gamma$.

**b)** $a_n = S_n - \ln n \to \gamma$, c'est-à-dire $S_n - \ln n = \gamma + o(1)$, soit $S_n = \ln n + \gamma + o(1)$.

**4. a)** $u_n > 0$ et $u_n \underset{+\infty}{\sim} \frac{1}{2n^2}$ ; comme $\sum \frac{1}{n^2}$ converge, $\sum u_n$ **converge**.

**b)** On cherche $F(X) = \frac{\alpha}{X} + \frac{\beta}{2X+1}$. En multipliant par $X$ et en prenant $X = 0$ : $\alpha = 1$. En multipliant par $2X+1$ et en prenant $X = -\frac{1}{2}$ : $\beta = \frac{1}{-1/2} = -2$. Donc
$$F(X) = \frac{1}{X} - \frac{2}{2X+1}$$

**c)** On sépare les indices pairs $n = 2k$ ($1 \leq k \leq N$) et impairs $n = 2k+1$ ($0 \leq k \leq N$) :
$$S_{2N+1} = \sum_{k=1}^{N}\frac{1}{2k} + 1 + \sum_{k=1}^{N}\frac{1}{2k+1} = \frac{1}{2}S_N + 1 + \sum_{k=1}^{N}\frac{1}{2k+1}$$
D'après b), $\frac{2}{2k+1} = \frac{1}{k} - \frac{1}{k(2k+1)}$, donc $\frac{1}{2k+1} = \frac{1}{2k} - \frac{1}{2}\cdot\frac{1}{k(2k+1)}$ et
$$S_{2N+1} = \frac{1}{2}S_N + 1 + \frac{1}{2}S_N - \frac{1}{2}\sum_{k=1}^{N}\frac{1}{k(2k+1)} = S_N + 1 - \frac{1}{2}\sum_{k=1}^{N}\frac{1}{k(2k+1)}$$
D'où
$$\frac{1}{2}\sum_{n=1}^{N} \frac{1}{n(2n+1)} = S_N - S_{2N+1} + 1$$

**d)** D'après 3.b), $S_N = \ln N + \gamma + o(1)$ et $S_{2N+1} = \ln(2N+1) + \gamma + o(1)$, donc
$$S_N - S_{2N+1} = -\ln\left(\frac{2N+1}{N}\right) + o(1) = -\ln\left(2 + \frac{1}{N}\right) + o(1) \xrightarrow[N\to+\infty]{} -\ln 2$$
En faisant tendre $N$ vers $+\infty$ dans c) :
$$\sum_{n=1}^{+\infty} \frac{1}{n(2n+1)} = 2(1 - \ln 2) = 2 - 2\ln 2$$
