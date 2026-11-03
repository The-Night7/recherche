---
source: DS1-2023-2024-V5-Correction_Series-DS_P2S1_EMasnada.pdf, pages 1 à 3
transcription: manuelle
---

# Séries — Devoir surveillé 1 (2023/2024, mercredi 25 octobre, version 5) (corrigé)

Durée 60 mn. Documents et supports électroniques interdits.

## Exercice 1 : Séries de Riemann

**Énoncé.** (2 pts) Énoncer les théorèmes de convergence des Séries de Riemann et des Séries de Riemann Alternées.

**Correction.**

> **Complément :** le corrigé d'origine ne contient pas de réponse à cet exercice de cours.

- **Séries de Riemann.** Soit $\alpha \in \mathbb{R}$. La série $\sum_{n\geq 1}\frac{1}{n^\alpha}$ converge si et seulement si $\alpha > 1$.
- **Séries de Riemann alternées.** Soit $\alpha \in \mathbb{R}$. La série $\sum_{n\geq 1}\frac{(-1)^n}{n^\alpha}$ converge si et seulement si $\alpha > 0$ (pour $\alpha > 0$, par le théorème spécial des séries alternées ; pour $\alpha \leq 0$, le terme général ne tend pas vers $0$). Elle converge absolument si et seulement si $\alpha > 1$ ; elle est donc semi-convergente pour $0 < \alpha \leq 1$.

## Exercice 2 : Nature de quatre séries

**Énoncé.** (8 pts) Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n\in\mathbb{N}}\frac{3n^3-4n+1}{n^4+2}$
2. $\displaystyle\sum_{n\geq 2}\ln\left(1 - \frac{1}{n\sqrt n}\right)$
3. $\displaystyle\sum_{n\geq 1}\frac{b^n}{n^a}$, $a, b \in \mathbb{R}$
4. $\displaystyle\sum_{n\in\mathbb{N}}\frac{\sin(n)}{1+n^2}$

**Correction.** On note $u_n$ le terme général des séries.

**1.** Fraction rationnelle : $u_n \underset{+\infty}{\sim} \frac{3n^3}{n^4} = \frac{3}{n}$, de signe constant (positif) à partir d'un certain rang, et la série harmonique diverge. Par le théorème des équivalents, la série **diverge**.

**2.** Pour $n \geq 2$, $0 < 1 - \frac{1}{n\sqrt n} < 1$, donc $u_n$ est bien défini et de signe constant (négatif). Avec $\ln(1 - x) \sim -x$ quand $x \to 0$ :
$$u_n \underset{+\infty}{\sim} -\frac{1}{n\sqrt n} = -\frac{1}{n^{3/2}}$$
terme d'une série de Riemann convergente ($\alpha = \frac{3}{2} > 1$). Par le théorème des équivalents, la série **converge**.

> **Note :** le corrigé d'origine écrit « pour tout $n \geq 1$ » ; pour $n = 1$, $1 - \frac{1}{n\sqrt n} = 0$ et le logarithme n'est pas défini, d'où la série indexée à partir de $2$.

**3.** Si $b = 0$, c'est la série nulle, convergente. Si $b \neq 0$, $u_n \neq 0$ pour $n \geq 1$ et la règle de d'Alembert donne
$$\left|\frac{u_{n+1}}{u_n}\right| = |b|\left(\frac{n}{n+1}\right)^a \xrightarrow[n\to+\infty]{} |b|$$
On distingue quatre cas :

- si $|b| < 1$, la série **converge absolument**, quel que soit $a \in \mathbb{R}$ ;
- si $|b| > 1$, la série **diverge grossièrement**, quel que soit $a \in \mathbb{R}$ (car $\frac{|b|^n}{n^a} \to +\infty$ par croissances comparées) ;
- si $b = 1$, la règle de d'Alembert ne permet pas de conclure, mais on reconnaît la série de Riemann $\sum \frac{1}{n^a}$ : elle **converge si $a > 1$** et diverge si $a \leq 1$ ;
- si $b = -1$, on reconnaît la série de Riemann alternée $\sum \frac{(-1)^n}{n^a}$ : elle **converge si $a > 0$** et diverge si $a \leq 0$.

> **Erreur corrigée :** dans le dernier cas, le corrigé d'origine écrit la condition avec $\alpha$ au lieu de $a$.

**4.** Pour tout $n \in \mathbb{N}$, $|u_n| = \frac{|\sin n|}{1+n^2} \leq \frac{1}{1+n^2}$, et $\frac{1}{1+n^2} \sim \frac{1}{n^2}$ est le terme d'une série convergente (Riemann, $\alpha = 2 > 1$). Par le théorème de majoration, la série à termes positifs $\sum |u_n|$ converge : la série $\sum u_n$ **converge absolument**.

## Exercice 3 : Équivalent de la somme des racines carrées

**Énoncé.** (6 pts) On considère la série de terme général $u_n = \sqrt n$ et on note $(S_n)$ sa suite de sommes partielles : $S_n = \sum_{k=1}^{n} u_k$.

1. Montrer que pour tout $n \geq 1$, $\displaystyle\int_0^n \sqrt x\,dx \leq S_n \leq \int_1^{n+1}\sqrt x\,dx$.
2. En déduire que $S_n$ est équivalent à $\frac{2}{3}n^{3/2}$ lorsque $n \to +\infty$.

**Correction.**

**1.** La fonction $x \mapsto \sqrt x$ est croissante sur $\mathbb{R}_+$. On en déduit que pour tout $k \geq 1$ :
$$\int_{k-1}^{k}\sqrt x\,dx \leq u_k \leq \int_k^{k+1}\sqrt x\,dx$$
(faire un dessin rapide sur la copie pour illustrer cet encadrement). En sommant pour $k$ allant de $1$ à $n$, avec la relation de Chasles :
$$\int_0^n \sqrt x\,dx \leq S_n \leq \int_1^{n+1}\sqrt x\,dx$$

**2.** On calcule les intégrales :
$$\int_0^n \sqrt x\,dx = \left[\frac{2}{3}x^{3/2}\right]_0^n = \frac{2}{3}n^{3/2}, \qquad \int_1^{n+1}\sqrt x\,dx = \frac{2}{3}\left((n+1)^{3/2} - 1\right)$$
Quand $n \to +\infty$, $\frac{2}{3}\left((n+1)^{3/2} - 1\right) \sim \frac{2}{3}n^{3/2}$. En divisant l'encadrement par $\frac{2}{3}n^{3/2}$, les deux bornes tendent vers $1$ ; par encadrement,
$$S_n \underset{+\infty}{\sim} \frac{2}{3}n^{3/2}$$

> **Erreur corrigée :** le corrigé d'origine écrit dans sa conclusion $\frac{3}{2}\left((n+1)^{3/2} - 1\right) \sim \frac{3}{2}n^{3/2}$ et $S_n \sim \frac{3}{2}n^{3/2}$ ; le coefficient correct est $\frac{2}{3}$, comme dans l'énoncé.

## Exercice 4 : Série alternée (−1)ⁿ(cos(1/nᵃ) − 1)

**Énoncé.** (6 pts) Pour $a \in \mathbb{R}$ et $n \geq 1$ on considère la série de terme général $u_n = (-1)^n\left(\cos\left(\frac{1}{n^a}\right) - 1\right)$.

1. Déterminer la nature de la série $\sum_{n\geq 1} u_n$ quand $a \leq 0$.
2. Pour $a > 0$, donner un équivalent de $u_n$ quand $n$ tend vers l'infini.
3. Déterminer la nature de la série $\sum_{n\geq 1} u_n$ quand $a > \frac{1}{2}$.
4. Justifier que pour tout $a \in \,]0, \frac{1}{2}[$ il existe un $k_0 \in \mathbb{N}$ tel que si $v_n = o\left(\frac{1}{n^{2k_0a}}\right)$ alors $\sum_{n\in\mathbb{N}} v_n$ converge.
5. Déterminer la nature de la série $\sum_{n\geq 1} u_n$ quand $a \in \,]0, \frac{1}{2}[$.

**Correction.**

**1.** *Cas $a = 0$* : $u_n = (-1)^n(\cos 1 - 1)$ avec $\cos 1 - 1 \neq 0$ ; cette suite n'a pas de limite, donc la série **diverge grossièrement**.

*Cas $a < 0$* : $\frac{1}{n^a} = n^{c}$ avec $c = -a > 0$, qui tend vers $+\infty$, et $\cos(n^c)$ n'a pas de limite ; en particulier $\cos(n^c) - 1$ ne tend pas vers $0$ et la série **diverge grossièrement**.

> **Note :** le corrigé d'origine affirme sans preuve que $\cos(n^c)$ ne tend pas vers $1$. Pour $0 < c \leq 1$, c'est facile : les pas $(n+1)^c - n^c$ sont $\leq 1$ (accroissements finis), donc la suite $(n^c)$, qui tend vers $+\infty$, tombe dans chacun des intervalles $[(2m+1)\pi - \frac{1}{2}, (2m+1)\pi + \frac{1}{2}]$, où $\cos \leq -\cos\frac{1}{2} < 0$ ; ainsi $|u_n| \geq 1$ pour une infinité de $n$. Pour $c > 1$, le résultat reste vrai mais sa preuve dépasse le programme (équirépartition modulo $2\pi$).

**2.** Pour $a > 0$, $\frac{1}{n^a} \to 0$ et, par développement limité du cosinus en $0$,
$$u_n = (-1)^n\left(1 - \frac{1}{2n^{2a}} + o\left(\frac{1}{n^{2a}}\right) - 1\right) = \frac{(-1)^{n+1}}{2n^{2a}} + o\left(\frac{1}{n^{2a}}\right)$$
donc $u_n \underset{+\infty}{\sim} \frac{(-1)^{n+1}}{2n^{2a}}$.

**3.** Si $a > \frac{1}{2}$, $|u_n| \sim \frac{1}{2n^{2a}}$, terme d'une série de Riemann convergente ($\alpha = 2a > 1$). Donc la série $\sum u_n$ **converge absolument**.

**4.** On sait que la série de Riemann $\sum_{n\geq 1}\frac{1}{n^\alpha}$ converge si et seulement si $\alpha > 1$. Pour $a \in \,]0, \frac{1}{2}[$, on peut choisir un entier $k_0 > \frac{1}{2a}$, de sorte que $2k_0a > 1$. Si $v_n = o\left(\frac{1}{n^{2k_0a}}\right)$, alors $|v_n| \leq \frac{1}{n^{2k_0a}}$ à partir d'un certain rang, et $\sum v_n$ converge (absolument) par comparaison.

**5.** Le développement limité du cosinus en $0$ à l'ordre $2k_0$ s'écrit
$$\cos(x) = \sum_{k=0}^{k_0}\frac{(-1)^k}{(2k)!}x^{2k} + o\left(x^{2k_0}\right)$$
On en déduit, le terme $k = 0$ se simplifiant avec le $-1$ :
$$u_n = (-1)^n\sum_{k=1}^{k_0}\frac{(-1)^k}{(2k)!}\left(\frac{1}{n^a}\right)^{2k} + o\left(\frac{1}{n^{2k_0a}}\right) = \sum_{k=1}^{k_0}\frac{(-1)^{n+k}}{(2k)!}\cdot\frac{1}{n^{2ka}} + o\left(\frac{1}{n^{2k_0a}}\right)$$
Pour tout $k \in [\![1, k_0]\!]$, la série de terme général $w_n^{(k)} = \frac{(-1)^{n+k}}{(2k)!}\cdot\frac{1}{n^{2ka}}$ converge : c'est un multiple d'une série de Riemann alternée avec exposant $2ka > 0$. De plus, par la question 4, la série de terme général $o\left(\frac{1}{n^{2k_0a}}\right)$ converge absolument. Pour tout $a \in \,]0, \frac{1}{2}[$, la série $\sum u_n$ est donc une somme finie de séries convergentes : elle **converge**.

> **Note :** en rassemblant les résultats, $\sum u_n$ converge pour tout $a > 0$ (y compris $a = \frac{1}{2}$, non demandé : $u_n = \frac{(-1)^{n+1}}{2n} + O\left(\frac{1}{n^2}\right)$) et diverge pour $a \leq 0$ ; elle converge absolument si et seulement si $a > \frac{1}{2}$.
