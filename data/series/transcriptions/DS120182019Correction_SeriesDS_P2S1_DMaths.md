---
source: DS1-2018-2019-Correction_Series-DS_P2S1_DMaths.pdf, pages 1 à 4 (énoncés : DS1-2018-2019_Series-DS_P2S1_KFayad-KGuezguez-AElJanati.pdf, pages 1 et 2)
transcription: manuelle
---

# Séries — Devoir surveillé 1 (octobre 2018) (corrigé)

Devoir du vendredi 12 octobre 2018 (A. El Janati, K. Fayad, K. Guezguez). Durée 2 heures, appareils électroniques et documents interdits.

## Exercice 1 : Vrai ou faux sur les séries à termes positifs

**Énoncé.** (4 points) Soit $\sum_{n\geq 0} u_n$ une série à termes réels positifs. Répondre par VRAI ou FAUX **en justifiant**.

1. Si la suite $(u_n)_{n\geq 0}$ tend vers $0$, alors la série $\sum_{n\geq 0} u_n$ converge.
2. Si la série $\sum_{n\geq 0} u_n$ diverge, alors la suite $(u_n)_{n\geq 0}$ ne tend pas vers $0$.
3. Si la série $\sum_{n\geq 0} u_n$ diverge, alors la série $\sum_{n\geq 0} u_n^2$ diverge.
4. Si la série $\sum_{n\geq 0} u_n$ converge, alors la série $\sum_{n\geq 0} u_n^2$ converge.

**Correction.**

> **Note :** le corrigé d'origine traite les assertions 2 et 3 dans l'ordre inverse ; on suit ici la numérotation de l'énoncé.

1. **Faux.** Contre-exemple : $u_n = \frac{1}{n}$ pour $n \geq 1$. La suite tend vers $0$, mais $\sum_{n\geq 1} \frac{1}{n}$ diverge (série de Riemann avec $\alpha = 1 \leq 1$).
2. **Faux.** Le même contre-exemple convient : $\sum \frac{1}{n}$ diverge alors que $\frac{1}{n} \to 0$. (La condition $u_n \to 0$ est nécessaire pour la convergence, pas suffisante.)
3. **Faux.** Avec $u_n = \frac{1}{n}$, la série $\sum u_n$ diverge, mais $\sum u_n^2 = \sum \frac{1}{n^2}$ converge (Riemann avec $\alpha = 2 > 1$).
4. **Vrai.** Si $\sum u_n$ converge, son terme général tend vers $0$ ; il existe donc un rang $n_0$ à partir duquel $0 \leq u_n \leq 1$, d'où
$$0 \leq u_n^2 \leq u_n \quad (n \geq n_0)$$
Comme $\sum u_n$ converge, le théorème de comparaison des séries à termes positifs donne la convergence de $\sum u_n^2$.

## Exercice 2 : Nature de trois séries

**Énoncé.** (5 points) Étudier la nature des séries numériques de terme général :

1. $u_n = \cos\left(\dfrac{1}{n^2}\right)$, $n \geq 1$.
2. $v_n = \left(\dfrac{2n+1}{2n+5}\right)^{n^2}$, $n \geq 0$.
3. $w_n = \dfrac{(n!)^3}{(3n)!}\,3^n$, $n \geq 0$.

**Correction.**

1. Quand $n \to +\infty$, $\frac{1}{n^2} \to 0$ donc $u_n \to \cos 0 = 1 \neq 0$ : le terme général ne tend pas vers $0$, la série $\sum u_n$ **diverge grossièrement**.

2. $v_n > 0$ ; on applique la règle de Cauchy :
$$(v_n)^{1/n} = \left(\frac{2n+1}{2n+5}\right)^{n} = \left(1 - \frac{4}{2n+5}\right)^{n} = \exp\left(n\ln\left(1 - \frac{4}{2n+5}\right)\right)$$
Comme $\ln\left(1 - \frac{4}{2n+5}\right) \underset{+\infty}{\sim} -\frac{4}{2n+5}$, on a $n\ln\left(1 - \frac{4}{2n+5}\right) \underset{+\infty}{\sim} -\frac{4n}{2n+5} \to -2$, donc
$$\lim_{n\to+\infty} (v_n)^{1/n} = e^{-2} < 1$$
La série $\sum v_n$ **converge**.

> **Erreur corrigée :** le corrigé d'origine écrit $n\ln\left(1-\frac{4}{2n+5}\right) \sim -\frac{4}{2n+5}$ (il manque le facteur $n$) ; la limite $-2$ annoncée est bien la bonne.

3. $w_n > 0$ ; on applique la règle de d'Alembert :
$$\frac{w_{n+1}}{w_n} = \frac{((n+1)!)^3}{(n!)^3}\cdot\frac{(3n)!}{(3n+3)!}\cdot\frac{3^{n+1}}{3^n} = \frac{3(n+1)^3}{(3n+3)(3n+2)(3n+1)} = \frac{(n+1)^2}{(3n+2)(3n+1)}$$
Donc $\lim_{n\to+\infty} \frac{w_{n+1}}{w_n} = \frac{1}{9} < 1$ : la série $\sum w_n$ **converge**.

## Exercice 3 : Somme de la série de terme (n+1)/3ⁿ

**Énoncé.** (3 points) Pour $n \in \mathbb{N}$, on pose
$$u_n = \frac{n+1}{3^n}$$

1. Montrer que la série $\sum_{n\geq 0} u_n$ converge. On note $S$ sa somme.
2. Calculer $S$. *Indication :* on pourra trouver un réel $\alpha$ tel que $\frac{1}{3}S = S - \alpha$.

**Correction.**

1. La série est à termes positifs. Par croissances comparées,
$$n^2 u_n = \frac{n^2(n+1)}{3^n} = n^2(n+1)e^{-n\ln 3} \xrightarrow[n\to+\infty]{} 0$$
Donc $u_n = o\left(\frac{1}{n^2}\right)$ et, $\sum \frac{1}{n^2}$ convergeant (Riemann, $\alpha = 2 > 1$), la série $\sum u_n$ **converge** (règle « $n^\alpha u_n$ » avec $\alpha = 2$).

2. On décale l'indice :
$$\frac{1}{3}S = \sum_{n=0}^{+\infty} \frac{n+1}{3^{n+1}} = \sum_{n=1}^{+\infty} \frac{n}{3^{n}} = \sum_{n=1}^{+\infty} \frac{n+1}{3^{n}} - \sum_{n=1}^{+\infty} \frac{1}{3^{n}}$$
Toutes ces séries convergent. La première somme vaut $S - u_0 = S - 1$ et la seconde est géométrique : $\sum_{n\geq 1} \frac{1}{3^n} = \frac{1/3}{1 - 1/3} = \frac{1}{2}$. Donc
$$\frac{1}{3}S = S - \frac{3}{2}, \qquad \text{d'où} \qquad \frac{2}{3}S = \frac{3}{2} \quad\text{et}\quad S = \frac{9}{4}$$
(Vérification : $\sum_{n\geq 0}(n+1)x^n = \frac{1}{(1-x)^2}$ pour $|x| < 1$, qui vaut $\frac{9}{4}$ en $x = \frac{1}{3}$.)

## Exercice 4 : Série définie par une récurrence

**Énoncé.** (8 points) On considère la suite réelle $(u_n)_{n\geq 0}$ définie par la donnée de $u_0 > 0$ et la relation :
$$\forall n \geq 0, \quad u_{n+1} = \frac{n+1}{n+3}\,u_n$$

1. Le but de cette question est d'étudier la nature de la série $\sum_{n\geq 0} u_n$. Pour $n > 0$, on pose
$$v_n = \ln(n^2 u_n) \quad\text{et}\quad w_n = v_{n+1} - v_n$$
    a) Donner le développement limité à l'ordre 2 de $w_n$ et en déduire la nature de la série $\sum_{n>0} w_n$.
    b) Que peut-on dire de la suite $(v_n)_{n>0}$ ? Justifier.
    c) En déduire qu'il existe un réel $L > 0$ (que l'on ne cherchera pas à déterminer) tel que $u_n \underset{+\infty}{\sim} \frac{L}{n^2}$, et conclure.
2. Le but de cette question est de calculer la somme de la série $\sum_{n\geq 0} u_n$.
    a) Déterminer $\lim_{n\to+\infty} n u_n$.
    b) Pour $n \geq 0$, on pose $z_n = (n+1)u_{n+1} - n u_n$. Calculer $\lim_{N\to+\infty} \sum_{n=0}^{N} z_n$.
    c) En utilisant la question précédente et la relation de récurrence vérifiée par la suite $(u_n)_{n\geq 0}$, calculer $\sum_{n=0}^{+\infty} u_n$ en fonction de $u_0$.

**Correction.** Par récurrence immédiate, $u_n > 0$ pour tout $n$ (car $u_0 > 0$ et $\frac{n+1}{n+3} > 0$), donc $v_n$ est bien défini.

**1. a)** Pour $n \geq 1$ :
$$w_n = \ln\left(\frac{(n+1)^2 u_{n+1}}{n^2 u_n}\right) = \ln\left(\left(\frac{n+1}{n}\right)^2 \frac{n+1}{n+3}\right)$$
Comme $\frac{n+1}{n+3} = \frac{1 + 1/n}{1 + 3/n}$, on obtient
$$w_n = 3\ln\left(1 + \frac{1}{n}\right) - \ln\left(1 + \frac{3}{n}\right)$$
Avec $\ln(1+x) = x - \frac{x^2}{2} + o(x^2)$ :
$$w_n = 3\left(\frac{1}{n} - \frac{1}{2n^2}\right) - \left(\frac{3}{n} - \frac{9}{2n^2}\right) + o\left(\frac{1}{n^2}\right) = \frac{3}{n^2} + o\left(\frac{1}{n^2}\right)$$
Donc $w_n \underset{+\infty}{\sim} \frac{3}{n^2}$. Les deux suites sont positives à partir d'un certain rang et $\sum \frac{3}{n^2}$ converge (Riemann, $\alpha = 2 > 1$) : par le théorème des équivalents, $\sum w_n$ **converge**.

**b)** $\sum w_n = \sum (v_{n+1} - v_n)$ est une série télescopique : $\sum_{n=1}^{N-1} w_n = v_N - v_1$. Elle converge, donc la suite $(v_n)_{n\geq 1}$ **converge** ; notons $\ell$ sa limite.

**c)** Par définition de $v_n$, $u_n = \frac{e^{v_n}}{n^2}$. Comme $v_n \to \ell$, $e^{v_n} \to L := e^{\ell} > 0$, d'où
$$u_n \underset{+\infty}{\sim} \frac{L}{n^2}$$
La série de Riemann $\sum \frac{1}{n^2}$ converge et les termes sont positifs : $\sum u_n$ **converge**.

**2. a)** D'après 1.c), $n u_n \underset{+\infty}{\sim} \frac{L}{n} \to 0$ : $\lim_{n\to+\infty} n u_n = 0$.

**b)** C'est une somme télescopique :
$$\sum_{n=0}^{N} z_n = \sum_{n=0}^{N} \big((n+1)u_{n+1} - n u_n\big) = (N+1)u_{N+1} - 0\cdot u_0 = (N+1)u_{N+1}$$
D'après a), $\lim_{N\to+\infty} \sum_{n=0}^{N} z_n = 0$.

**c)** La récurrence s'écrit $(n+3)u_{n+1} = (n+1)u_n$, soit $(n+1)u_{n+1} = (n+1)u_n - 2u_{n+1}$. Donc
$$z_n = (n+1)u_n - 2u_{n+1} - n u_n = u_n - 2u_{n+1}$$
Notons $S = \sum_{n=0}^{+\infty} u_n$. Les séries $\sum u_n$ et $\sum u_{n+1}$ convergent, donc en passant à la limite dans b) :
$$0 = \sum_{n=0}^{+\infty} u_n - 2\sum_{n=0}^{+\infty} u_{n+1} = S - 2(S - u_0) = 2u_0 - S$$
d'où
$$S = \sum_{n=0}^{+\infty} u_n = 2u_0$$

> **Erreur corrigée :** le corrigé d'origine écrit $-2(S - u_0) + S = u_0 - S$ et conclut $S = u_0$ ; le bon calcul donne $2u_0 - S$, donc $S = 2u_0$.

*Vérification.* En itérant la récurrence, $u_n = u_0 \prod_{k=0}^{n-1} \frac{k+1}{k+3} = \frac{2u_0}{(n+1)(n+2)}$, et $\sum_{n\geq 0} \frac{2}{(n+1)(n+2)} = 2\sum_{n\geq 0}\left(\frac{1}{n+1} - \frac{1}{n+2}\right) = 2$. On retrouve $S = 2u_0$, et au passage $L = 2u_0$.
