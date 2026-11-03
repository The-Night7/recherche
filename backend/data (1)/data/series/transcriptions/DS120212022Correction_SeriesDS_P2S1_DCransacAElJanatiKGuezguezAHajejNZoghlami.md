---
source: DS1-2021-2022-Correction_Series-DS_P2S1_DCransac-AElJanati-KGuezguez-AHajej-NZoghlami.pdf, pages 1 à 3
transcription: manuelle
---

# Séries — Devoir surveillé 1 (novembre 2021) (corrigé)

Devoir du vendredi 12 novembre 2021 (D. Cransac, A. El Janati, K. Guezguez, A. Hajej, N. Zoghlami). Durée 1 h 30, appareils électroniques et documents interdits.

## Exercice 1 : Nature de cinq séries

**Énoncé.** (8 points)

A) Déterminer la nature de convergence des séries de terme général :
$$u_n = \left(\frac{1}{3}\right)^{\sqrt{n}}\ ; \qquad v_n = 2\ln(n^3+1) - \ln(n^2+1)$$

B) Déterminer la nature de convergence des séries de terme général :
$$a_n = (-1)^n\sin\left(\frac{1}{n}\right)\ ; \qquad b_n = \left(1 + \frac{1}{n^3}\right)^n - 1\ ; \qquad c_n = \ln n \times b_n$$

**Correction.**

**A) (1)** $u_n > 0$ et
$$n^2u_n = e^{2\ln n - \sqrt{n}\ln 3} = e^{\sqrt{n}\left(\frac{2\ln n}{\sqrt n} - \ln 3\right)} \xrightarrow[n\to+\infty]{} 0$$
car $\frac{\ln n}{\sqrt n} \to 0$ (croissances comparées), donc l'exposant tend vers $-\infty$. Ainsi $u_n = o\left(\frac{1}{n^2}\right)$ et, par la règle de Riemann ($\alpha = 2 > 1$), $\sum u_n$ **converge**.

**(2)** $v_n = \ln\left(\dfrac{(n^3+1)^2}{n^2+1}\right)$ et $\dfrac{(n^3+1)^2}{n^2+1} \sim n^4 \to +\infty$. Par continuité de $\ln$, $v_n \to +\infty \neq 0$ : $\sum v_n$ **diverge grossièrement**.

**B) (1)** Pour $n \geq 1$, $\frac{1}{n} \in \,]0, 1] \subset \,]0, \frac{\pi}{2}[$, donc $\sin\left(\frac{1}{n}\right) > 0$. La suite $\left(\sin\frac{1}{n}\right)_{n\geq 1}$ est décroissante (composée de $\sin$, croissante sur $[0, \frac{\pi}{2}]$, et de $n \mapsto \frac{1}{n}$, décroissante) et tend vers $0$. Par le critère des séries alternées, $\sum a_n$ **converge**.

**(2)** $b_n \geq 0$ pour $n \geq 1$. On a $n\ln\left(1 + \frac{1}{n^3}\right) \sim n\cdot\frac{1}{n^3} = \frac{1}{n^2} \to 0$, donc
$$b_n = e^{n\ln\left(1 + \frac{1}{n^3}\right)} - 1 \underset{+\infty}{\sim} n\ln\left(1 + \frac{1}{n^3}\right) \underset{+\infty}{\sim} \frac{1}{n^2}$$
$\sum \frac{1}{n^2}$ converge (Riemann, $\alpha = 2 > 1$) : par le théorème des équivalents pour les séries à termes positifs, $\sum b_n$ **converge**.

**(3)** $c_n \geq 0$ pour $n \geq 1$ et, d'après (2), $c_n \sim \frac{\ln n}{n^2} =: d_n$. Or $n^{3/2}d_n = \frac{\ln n}{n^{1/2}} \to 0$ (croissances comparées), donc $\sum d_n$ converge (règle de Riemann, $\frac{3}{2} > 1$), et par équivalence $\sum c_n$ **converge**.

## Exercice 2 : Deux calculs de sommes

**Énoncé.** (5,5 points)

1. 
    a) Montrer que, pour tout entier naturel $k$, $k^3 = k + 3k(k-1) + k(k-1)(k-2)$.
    b) Montrer que la série $\sum_{k\geq 0} \frac{k^3}{k!}$ est convergente et déterminer sa somme.
2. Montrer que la série $\sum_{n\geq 2} u_n$ où $u_n = \dfrac{1}{\sqrt{n-1}} - \dfrac{2}{\sqrt{n}} + \dfrac{1}{\sqrt{n+1}}$ est convergente et déterminer sa somme.

> **Erreur corrigée :** le sujet imprimé écrit $u_n = \frac{1}{\sqrt{n-1}} - \frac{2}{n} + \frac{1}{\sqrt{n+1}}$ ; avec $\frac{2}{n}$ la série diverge ($u_n \sim \frac{2}{\sqrt n}$). Le corrigé utilise $\frac{2}{\sqrt n}$, qui est la version voulue.

**Correction.**

**1. a)** En développant : $k(k-1)(k-2) = k^3 - 3k^2 + 2k$ et $3k(k-1) = 3k^2 - 3k$, donc
$$k + 3k(k-1) + k(k-1)(k-2) = k + 3k^2 - 3k + k^3 - 3k^2 + 2k = k^3$$

**b)** Pour $k \geq 3$, d'après a) :
$$\frac{k^3}{k!} = \frac{k}{k!} + \frac{3k(k-1)}{k!} + \frac{k(k-1)(k-2)}{k!} = \frac{1}{(k-1)!} + \frac{3}{(k-2)!} + \frac{1}{(k-3)!}$$
Soit $S_n = \sum_{k=0}^{n}\frac{k^3}{k!}$, $n \geq 3$. Les termes $k = 0, 1, 2$ valent $0 + 1 + 4 = 5$, donc
$$S_n = 5 + \sum_{k=2}^{n-1}\frac{1}{k!} + 3\sum_{k=1}^{n-2}\frac{1}{k!} + \sum_{k=0}^{n-3}\frac{1}{k!}$$
En utilisant $5 = 2 + 3$, avec $2 = \frac{1}{0!} + \frac{1}{1!}$ et $3 = 3\cdot\frac{1}{0!}$ :
$$S_n = \sum_{k=0}^{n-1}\frac{1}{k!} + 3\sum_{k=0}^{n-2}\frac{1}{k!} + \sum_{k=0}^{n-3}\frac{1}{k!}$$
Comme $\sum_{k\geq 0}\frac{1}{k!}$ converge vers $e$, $S_n \to e + 3e + e = 5e$. La série converge et
$$\sum_{k=0}^{+\infty}\frac{k^3}{k!} = 5e$$

**2.** On sépare en deux sommes télescopiques : pour $n \geq 2$,
$$S_n = \sum_{k=2}^{n}\left(\frac{1}{\sqrt{k-1}} - \frac{1}{\sqrt k}\right) + \sum_{k=2}^{n}\left(\frac{1}{\sqrt{k+1}} - \frac{1}{\sqrt k}\right) = \left(1 - \frac{1}{\sqrt n}\right) + \left(\frac{1}{\sqrt{n+1}} - \frac{1}{\sqrt 2}\right)$$
Donc $S_n \to 1 - \frac{1}{\sqrt 2}$ : la série converge et
$$\sum_{n=2}^{+\infty} u_n = 1 - \frac{1}{\sqrt 2} = \frac{2 - \sqrt 2}{2}$$

## Exercice 3 : Suite récurrente uₙ₊₁ = uₙ − uₙ²

**Énoncé.** (6,5 points) Soit $a \in \,]0, 1[$ et $(u_n)_{n\in\mathbb{N}}$ la suite définie par :
$$\begin{cases} \forall n \in \mathbb{N},\ u_{n+1} = u_n - u_n^2 \\ u_0 = a \end{cases}$$

1. Montrer que : $\forall n \in \mathbb{N}$, $u_n \in \,]0, 1[$.
2. Montrer que la suite $(u_n)_{n\in\mathbb{N}}$ est convergente. Quelle est sa limite ?
3. Montrer que la série $\sum_{n\geq 0} u_n^2$ est convergente et déterminer sa somme.
4. Montrer que la série $\sum_{n\geq 0}\ln\left(\frac{u_{n+1}}{u_n}\right)$ est divergente (on pourra utiliser la définition).
5. Quelle est la nature de la série $\sum_{n\geq 0} u_n$ ?

**Correction.**

**1.** Par récurrence sur $n$ ; soit $P(n)$ : « $u_n \in \,]0, 1[$ ».

- *Initialisation* : $u_0 = a \in \,]0, 1[$.
- *Hérédité* : si $u_n \in \,]0, 1[$, alors $u_{n+1} = u_n(1 - u_n)$ est le produit de deux réels de $]0, 1[$, donc $u_{n+1} \in \,]0, 1[$.

Donc $u_n \in \,]0, 1[$ pour tout $n$.

**2.** $u_{n+1} - u_n = -u_n^2 \leq 0$ : la suite est décroissante, et minorée par $0$, donc convergente. Notons $\ell$ sa limite. En passant à la limite dans la relation de récurrence (la fonction $x \mapsto x - x^2$ est continue), $\ell = \ell - \ell^2$, donc $\ell = 0$.

**3.** Pour tout $n$, $u_n^2 = u_n - u_{n+1}$. La somme partielle est télescopique :
$$\sum_{k=0}^{n} u_k^2 = \sum_{k=0}^{n}(u_k - u_{k+1}) = u_0 - u_{n+1} \xrightarrow[n\to+\infty]{} u_0 = a$$
La série $\sum u_n^2$ converge et sa somme vaut $a$.

**4.** Encore une somme télescopique (tous les $u_k$ sont $> 0$) :
$$\sum_{k=0}^{n}\ln\left(\frac{u_{k+1}}{u_k}\right) = \sum_{k=0}^{n}\big(\ln u_{k+1} - \ln u_k\big) = \ln(u_{n+1}) - \ln(a)$$
Comme $u_{n+1} \to 0^+$, cette somme tend vers $-\infty$ : par définition, la série **diverge**.

**5.** $\frac{u_{n+1}}{u_n} = 1 - u_n \in \,]0, 1[$, donc $\ln\left(\frac{u_{n+1}}{u_n}\right) = \ln(1 - u_n) < 0$. Comme $u_n \to 0$,
$$-\ln\left(\frac{u_{n+1}}{u_n}\right) = -\ln(1 - u_n) \underset{+\infty}{\sim} u_n$$
Les deux suites sont positives, et $\sum -\ln\left(\frac{u_{n+1}}{u_n}\right)$ diverge d'après 4. Par le théorème des équivalents, $\sum u_n$ **diverge**.
