---
source: DS2-2022-2023_Series-DS_P2S1_DMaths.pdf, pages 1 et 2 (sujet scanné, sans corrigé)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 2 (décembre 2022) (corrigé)

Devoir du jeudi 17 décembre 2022. Durée 1 h 30, appareils électroniques et documents interdits.

> **Note :** l'en-tête du sujet porte « Devoir surveillé 1 », mais il s'agit du deuxième devoir (séries alternées et suites de fonctions, décembre 2022).

## Exercice 1 : Série de terme sin((−1)ⁿ/nᵃ)

**Énoncé.** (5 points) Soit $a$ un réel strictement positif. Pour tout entier naturel non nul $n$, on pose
$$u_n = \sin\left(\frac{(-1)^n}{n^a}\right) \qquad\text{et}\qquad w_n = \frac{(-1)^n}{n^a}$$
On cherche à déterminer la nature (absolument convergente, semi-convergente ou divergente) de la série $\sum_{n\geq 1} u_n$ en fonction des valeurs de $a$.

1. Montrer que la série $\sum_{n\geq 1} w_n$ est convergente.
2. Montrer que $u_n \sim w_n$. En déduire les valeurs de $a$ pour lesquelles la série $\sum_{n\geq 1} u_n$ est absolument convergente.
3. Donner le développement limité à l'ordre 3 en $0$ de $\sin(x)$. En déduire que si $a \in \,]\frac{1}{3}; 1[$ alors la série $\sum_{n\geq 1} u_n$ est semi-convergente.

*Rappel : une série numérique est dite semi-convergente si elle est convergente et non absolument convergente.*

**Correction.**

> **Complément :** le sujet n'a pas de corrigé ; toute la correction est rédigée pour cette transcription.

**1.** $w_n = (-1)^n a_n$ avec $a_n = \frac{1}{n^a}$ ; comme $a > 0$, la suite $(a_n)$ est décroissante et tend vers $0$. Par le théorème spécial des séries alternées, $\sum w_n$ **converge**.

**2.** $w_n \to 0$ et $\sin x \sim x$ quand $x \to 0$, donc $u_n = \sin(w_n) \sim w_n$. En particulier $|u_n| \sim |w_n| = \frac{1}{n^a}$ ; par le théorème des équivalents (termes positifs), $\sum |u_n|$ converge si et seulement si $\sum \frac{1}{n^a}$ converge, c'est-à-dire si et seulement si $a > 1$. La série $\sum u_n$ est **absolument convergente si et seulement si $a > 1$**.

Attention : on ne peut pas déduire la convergence de $\sum u_n$ de l'équivalent $u_n \sim w_n$, car $w_n$ n'est pas de signe constant.

**3.** $\sin x = x - \frac{x^3}{6} + o(x^3)$. Avec $x = w_n$ et $w_n^3 = \frac{(-1)^{3n}}{n^{3a}} = \frac{(-1)^n}{n^{3a}}$ :
$$u_n = \frac{(-1)^n}{n^a} - \frac{(-1)^n}{6n^{3a}} + o\left(\frac{1}{n^{3a}}\right)$$
Si $a > \frac{1}{3}$, alors $3a > 1$ :

- $\sum \frac{(-1)^n}{n^a}$ converge (question 1) ;
- $\sum \frac{(-1)^n}{6n^{3a}}$ converge absolument (Riemann, $3a > 1$) ;
- le terme $o\left(\frac{1}{n^{3a}}\right)$ est, en valeur absolue, majoré par $\frac{1}{n^{3a}}$ à partir d'un certain rang : sa série converge absolument.

Donc $\sum u_n$ converge. Si de plus $a < 1$ (et même $a \leq 1$), elle n'est pas absolument convergente d'après 2. : pour $a \in \,]\frac{1}{3}; 1[$, la série $\sum u_n$ est **semi-convergente**.

> **Note :** on peut aussi conclure pour **tout** $a > 0$ sans développement limité : $\sin$ étant impaire, $u_n = (-1)^n\sin\left(\frac{1}{n^a}\right)$, et $\left(\sin\frac{1}{n^a}\right)$ décroît vers $0$ (car $\frac{1}{n^a} \in \,]0, 1] \subset [0, \frac{\pi}{2}]$). Le théorème spécial des séries alternées donne la convergence : la série est semi-convergente pour $0 < a \leq 1$ et absolument convergente pour $a > 1$.

## Exercice 2 : Deux séries non absolument convergentes

**Énoncé.** (5 points)

1. Montrer la convergence de la série numérique suivante :
$$\sum_{n\geq 2}\frac{\cos(n)}{\ln(n)}$$
2. Étudier la convergence de la série de terme général
$$u_n = \exp\left(\frac{(-1)^{n+1}}{\sqrt n}\right) - 1$$

**Correction.**

**1.** On utilise une **transformation d'Abel**. Posons $a_k = \frac{1}{\ln k}$ ($k \geq 2$), suite décroissante de limite nulle, et $C_n = \sum_{k=2}^{n}\cos k$ (avec $C_1 = 0$).

*Les sommes $C_n$ sont bornées.* Pour tout $n$, $\sum_{k=0}^{n}\cos k = \operatorname{Re}\left(\sum_{k=0}^{n} e^{ik}\right) = \operatorname{Re}\left(\frac{1 - e^{i(n+1)}}{1 - e^{i}}\right)$ (car $e^i \neq 1$), et $|1 - e^{i}| = 2\sin\frac{1}{2}$, donc
$$\left|\sum_{k=0}^{n}\cos k\right| \leq \frac{2}{2\sin\frac{1}{2}} = \frac{1}{\sin\frac{1}{2}}, \qquad |C_n| \leq M := \frac{1}{\sin\frac{1}{2}} + 2$$
*Transformation d'Abel.* Comme $\cos k = C_k - C_{k-1}$ pour $k \geq 2$ :
$$\sum_{k=2}^{N}\frac{\cos k}{\ln k} = \sum_{k=2}^{N} a_k(C_k - C_{k-1}) = a_N C_N + \sum_{k=2}^{N-1}(a_k - a_{k+1})C_k$$

- $|a_N C_N| \leq \frac{M}{\ln N} \to 0$ ;
- $|(a_k - a_{k+1})C_k| \leq M(a_k - a_{k+1})$ (car $a_k \geq a_{k+1}$), et $\sum (a_k - a_{k+1})$ est une série télescopique convergente (de somme $a_2$, car $a_k \to 0$). Donc $\sum (a_k - a_{k+1})C_k$ converge absolument.

Les sommes partielles ont donc une limite finie : la série $\sum_{n\geq 2}\frac{\cos n}{\ln n}$ **converge**. (Elle n'est pas absolument convergente, mais ce n'était pas demandé.)

**2.** Posons $x_n = \frac{(-1)^{n+1}}{\sqrt n} \to 0$. Avec $e^x = 1 + x + \frac{x^2}{2} + O(x^3)$ :
$$u_n = \frac{(-1)^{n+1}}{\sqrt n} + \frac{1}{2n} + O\left(\frac{1}{n^{3/2}}\right)$$

- $\sum \frac{(-1)^{n+1}}{\sqrt n}$ converge (théorème spécial des séries alternées, $\frac{1}{\sqrt n}$ décroît vers $0$) ;
- $\sum O\left(\frac{1}{n^{3/2}}\right)$ converge absolument (Riemann, $\frac{3}{2} > 1$) ;
- $\sum \frac{1}{2n}$ diverge.

Si $\sum u_n$ convergeait, $\sum \frac{1}{2n} = \sum\left(u_n - \frac{(-1)^{n+1}}{\sqrt n} - O\left(\frac{1}{n^{3/2}}\right)\right)$ convergerait comme somme de séries convergentes : absurde. Donc $\sum u_n$ **diverge** (bien que $u_n \sim \frac{(-1)^{n+1}}{\sqrt n}$, terme d'une série convergente : l'équivalent ne suffit pas pour des termes de signe non constant).

## Exercice 3 : Suite de fonctions xⁿ sin(x)

**Énoncé.** (4 points) Soit $f_n : [0; 1] \to \mathbb{R}$ définie par :
$$f_n(x) = x^n\sin(x)$$

1. Montrer que $(f_n)_n$ converge simplement sur $[0; 1]$ vers une fonction $f$ à déterminer.
2. Étudier la convergence uniforme de $(f_n)$ vers $f$ sur $[0; 1]$.
3. Montrer que $(f_n)_n$ converge uniformément vers $f$ sur tout intervalle $[0; \alpha]$ avec $\alpha \in \,]0; 1[$.

**Correction.**

**1.** Soit $x \in [0; 1[$ : $x^n \to 0$, donc $f_n(x) \to 0$. En $x = 1$ : $f_n(1) = \sin 1$ pour tout $n$. Donc $(f_n)$ converge simplement vers
$$f(x) = \begin{cases} 0 & \text{si } x \in [0; 1[ \\ \sin 1 & \text{si } x = 1 \end{cases}$$

**2.** Les $f_n$ sont continues sur $[0; 1]$, mais $f$ ne l'est pas en $1$ (car $\sin 1 \neq 0$). Une limite uniforme de fonctions continues étant continue, la convergence **n'est pas uniforme** sur $[0; 1]$.

On peut aussi le voir directement : pour $x \in [0; 1[$, $|f_n(x) - f(x)| = x^n\sin x$, qui tend vers $\sin 1$ quand $x \to 1^-$. Donc $\sup_{[0;1]}|f_n - f| \geq \sin 1$ pour tout $n$, qui ne tend pas vers $0$.

**3.** Soit $\alpha \in \,]0; 1[$. Sur $[0; \alpha]$, $f = 0$ et, comme $0 \leq \sin x \leq 1$,
$$\sup_{x\in[0;\alpha]}|f_n(x) - f(x)| = \sup_{x\in[0;\alpha]} x^n\sin x \leq \alpha^n \xrightarrow[n\to+\infty]{} 0$$
Donc $(f_n)$ converge **uniformément** vers $f$ sur $[0; \alpha]$.

## Exercice 4 : Suite de fonctions nᵃ x e^(−nx)

**Énoncé.** (4 points) Soit $a \in \mathbb{R}$ et soit $(f_n)_{n\geq 1}$ la suite de fonctions définies sur $\mathbb{R}_+$ par
$$f_n(x) = n^a x e^{-nx}$$
Étudier la convergence simple et uniforme de cette suite de fonctions sur $\mathbb{R}_+$.

**Correction.**

*Convergence simple.* $f_n(0) = 0$. Pour $x > 0$ fixé, $f_n(x) = x\,n^a e^{-nx} \to 0$ par croissances comparées (l'exponentielle l'emporte sur toute puissance de $n$). Donc $(f_n)$ converge simplement vers la **fonction nulle** sur $\mathbb{R}_+$, pour tout $a \in \mathbb{R}$.

*Convergence uniforme.* $f_n \geq 0$ et $f_n'(x) = n^a e^{-nx}(1 - nx)$ : $f_n$ croît sur $[0, \frac{1}{n}]$ et décroît sur $[\frac{1}{n}, +\infty[$. Donc
$$\|f_n - 0\|_\infty = f_n\left(\frac{1}{n}\right) = n^a\cdot\frac{1}{n}\cdot e^{-1} = \frac{n^{a-1}}{e}$$
qui tend vers $0$ si et seulement si $a < 1$. La convergence est **uniforme sur $\mathbb{R}_+$ si et seulement si $a < 1$** (pour $a = 1$ le sup vaut $\frac{1}{e}$, pour $a > 1$ il tend vers $+\infty$).

## Exercice 5 : Suite de fonctions à support dans [0 ; 1/n]

**Énoncé.** (4 points) Soit $f_n : [0; 1] \to \mathbb{R}$ définie par :
$$f_n(x) = \begin{cases} n^2x(1 - nx) & \text{si } x \in [0; \frac{1}{n}] \\ 0 & \text{sinon} \end{cases}$$

1. Montrer que la suite de fonctions $(f_n)_n$ converge simplement vers la fonction nulle sur $[0; 1]$.
2. Calculer $\int_0^1 f_n(x)\,dx$. Y a-t-il convergence uniforme de $(f_n)_n$ sur $[0; 1]$ ?
3. Étudier la convergence uniforme de $(f_n)_n$ sur $[\alpha; 1]$ avec $\alpha \in \,]0; 1[$.

> **Note :** la formule du scan est en partie illisible : on lit « $nx(1-nx) + n\ldots$ » suivi d'un symbole peu net. On retient $f_n(x) = n^2x(1-nx)$ (même exercice que dans le DS2 2023-2024, version 2), seule lecture cohérente avec la question 1 (une constante $+n$ empêcherait la convergence vers $0$ en $x = 0$) et avec la question 2 (intégrale constante). Les résultats pour $f_n(x) = nx(1-nx)$ sont indiqués au passage.

**Correction.**

**1.** $f_n(0) = 0$ pour tout $n$. Soit $x \in \,]0; 1]$ : dès que $n > \frac{1}{x}$, on a $x > \frac{1}{n}$ donc $f_n(x) = 0$. Ainsi $f_n(x) \to 0$ pour tout $x \in [0; 1]$ : $(f_n)$ converge simplement vers la **fonction nulle**.

**2.**
$$\int_0^1 f_n(x)\,dx = n^2\int_0^{1/n}(x - nx^2)\,dx = n^2\left(\frac{1}{2n^2} - \frac{n}{3n^3}\right) = n^2\cdot\frac{1}{6n^2} = \frac{1}{6}$$
Si $(f_n)$ convergeait uniformément vers $0$ sur le segment $[0; 1]$, on pourrait intervertir limite et intégrale : $\int_0^1 f_n \to \int_0^1 0 = 0$. Or $\int_0^1 f_n = \frac{1}{6}$ pour tout $n$ : il n'y a **pas convergence uniforme** sur $[0; 1]$. (Directement : le maximum de $f_n$ est atteint en $x = \frac{1}{2n}$ et vaut $n^2\cdot\frac{1}{2n}\cdot\frac{1}{2} = \frac{n}{4} \to +\infty$.)

Avec la lecture $f_n(x) = nx(1-nx)$, on trouverait $\int_0^1 f_n = \frac{1}{6n} \to 0$, qui ne permet pas de conclure, mais $\|f_n\|_\infty = \frac{1}{4}$ ne tend pas vers $0$ : pas de convergence uniforme non plus.

**3.** Soit $\alpha \in \,]0; 1[$. Pour $n > \frac{1}{\alpha}$, $\frac{1}{n} < \alpha$ donc $f_n$ est identiquement nulle sur $[\alpha; 1]$ : $\sup_{[\alpha;1]}|f_n| = 0$ à partir de ce rang. La convergence est **uniforme** sur $[\alpha; 1]$ (quelle que soit la lecture de la formule).
