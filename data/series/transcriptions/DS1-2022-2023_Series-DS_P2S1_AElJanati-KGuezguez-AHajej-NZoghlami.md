---
source: DS1-2022-2023_Series-DS_P2S1_AElJanati-KGuezguez-AHajej-NZoghlami.pdf, pages 1 et 2 (sujet scanné, sans corrigé)
transcription: manuelle
corrections: rédigées
---

# Séries — Devoir surveillé 1 (novembre 2022) (corrigé)

Devoir du dimanche 20 novembre 2022 (A. El Janati, K. Guezguez, A. Hajej, N. Zoghlami). Durée 1 h 30, appareils électroniques et documents interdits.

## Exercice 1 : Vrai ou faux

**Énoncé.** (7 points) Soit $(u_n)$ une suite à termes positifs. Déterminer en justifiant si les énoncés suivants sont vrais ou faux.

1. Si $\lim_{n\to+\infty} n^2u_n = +\infty$, alors $\sum_{n\geq 0} u_n$ est divergente.
2. Si à partir d'un certain rang $\frac{u_{n+1}}{u_n} < 1$, alors $\sum_{n\geq 0} u_n$ converge.
3. Si $\sum_{n\geq 0} u_n$ converge, alors $(u_n)_n$ converge vers $0$.
4. Pour tout réel $x \in \,]-1, 1[$, la série $\sum_{n\geq 0} x^n$ converge vers $\frac{1}{1-x}$.
5. Toute série télescopique est convergente.

**Correction.**

> **Complément :** le sujet n'a pas de corrigé ; toute la correction est rédigée pour cette transcription.

1. **Faux.** Contre-exemple : $u_n = \frac{1}{n^{3/2}}$ ($n \geq 1$). Alors $n^2u_n = \sqrt n \to +\infty$, mais $\sum \frac{1}{n^{3/2}}$ converge (Riemann, $\frac{3}{2} > 1$). (La règle « $n^\alpha u_n \to +\infty$ implique divergence » ne vaut que pour $\alpha \leq 1$.)

2. **Faux.** Contre-exemple : $u_n = \frac{1}{n}$ ($n \geq 1$) : $\frac{u_{n+1}}{u_n} = \frac{n}{n+1} < 1$ pour tout $n$, mais $\sum \frac{1}{n}$ diverge. (La règle de d'Alembert demande que la **limite** du rapport soit $< 1$, ou que le rapport reste inférieur à une constante $q < 1$.)

3. **Vrai.** Notons $S_n = \sum_{k=0}^{n} u_k$ et $S$ la somme de la série. Pour $n \geq 1$, $u_n = S_n - S_{n-1} \to S - S = 0$.

4. **Vrai.** Pour $x \neq 1$, $\sum_{k=0}^{n} x^k = \frac{1 - x^{n+1}}{1 - x}$. Si $|x| < 1$, $x^{n+1} \to 0$, donc les sommes partielles tendent vers $\frac{1}{1-x}$.

5. **Faux.** Une série télescopique $\sum (v_{n+1} - v_n)$ converge si et seulement si la suite $(v_n)$ converge, puisque $\sum_{k=0}^{n}(v_{k+1} - v_k) = v_{n+1} - v_0$. Contre-exemple : $v_n = n$ donne la série $\sum 1$, qui diverge. (Autre exemple : $v_n = \ln n$, $\sum \ln\left(1 + \frac{1}{n}\right)$ diverge.)

## Exercice 2 : Deux sommes

**Énoncé.** (4 points) Dans chaque cas, montrer que la série $\sum u_n$ converge et déterminer sa somme :

1. $u_n = 2^{n+1}3^{2-n}$ ($n \geq 0$) ;
2. $u_n = \ln\left(1 - \frac{1}{n^2}\right)$.

> **Note :** le sujet écrit $\sum_{n\geq 0}$ pour les deux séries ; la seconde n'est définie que pour $n \geq 2$ ($\ln 0$ pour $n = 1$), on la somme donc à partir de $n = 2$.

**Correction.**

**1.** $u_n = 2\cdot 2^n\cdot 9\cdot 3^{-n} = 18\left(\frac{2}{3}\right)^n$ : c'est une série géométrique de raison $\frac{2}{3} \in \,]-1, 1[$, donc convergente, et
$$\sum_{n=0}^{+\infty} u_n = 18\cdot\frac{1}{1 - \frac{2}{3}} = 54$$

**2.** Pour $n \geq 2$, $1 - \frac{1}{n^2} = \frac{(n-1)(n+1)}{n^2}$, donc
$$u_n = \big(\ln(n-1) - \ln n\big) + \big(\ln(n+1) - \ln n\big)$$
Pour $N \geq 2$, les deux sommes sont télescopiques :
$$\sum_{n=2}^{N} u_n = \big(\ln 1 - \ln N\big) + \big(\ln(N+1) - \ln 2\big) = \ln\left(\frac{N+1}{N}\right) - \ln 2 \xrightarrow[N\to+\infty]{} -\ln 2$$
La série converge et $\sum_{n=2}^{+\infty}\ln\left(1 - \frac{1}{n^2}\right) = -\ln 2$.

## Exercice 3 : Nature de trois séries

**Énoncé.** (4,5 points) Étudier la nature des séries suivantes :
$$\sum_{n\geq 1}\left(n\ln\left(1 + \frac{1}{n}\right) - \frac{2n}{2n+1}\right), \qquad \sum_{n\geq 2}\frac{n}{(\ln(n!))^2}, \qquad \sum_{n\geq 0}\ln\left(\cos\frac{1}{2^n}\right)$$

> **Note :** le sujet écrit $\sum_{n\geq 0}$ pour la première série, dont le terme n'est pas défini en $n = 0$ ; on commence à $n = 1$ (cela ne change pas la nature).

**Correction.**

**Première série.** Développements limités quand $n \to +\infty$ :
$$n\ln\left(1 + \frac{1}{n}\right) = n\left(\frac{1}{n} - \frac{1}{2n^2} + \frac{1}{3n^3} + o\left(\frac{1}{n^3}\right)\right) = 1 - \frac{1}{2n} + \frac{1}{3n^2} + o\left(\frac{1}{n^2}\right)$$
$$\frac{2n}{2n+1} = \frac{1}{1 + \frac{1}{2n}} = 1 - \frac{1}{2n} + \frac{1}{4n^2} + o\left(\frac{1}{n^2}\right)$$
Le terme général vaut donc $\left(\frac{1}{3} - \frac{1}{4}\right)\frac{1}{n^2} + o\left(\frac{1}{n^2}\right)$, c'est-à-dire qu'il est équivalent à $\frac{1}{12n^2} > 0$. La série de Riemann $\sum \frac{1}{n^2}$ converge : par équivalence (termes positifs à partir d'un certain rang), la série **converge**.

**Deuxième série.** Encadrons $\ln(n!) = \sum_{k=2}^{n}\ln k$. La fonction $\ln$ est croissante, donc $\ln k \geq \int_{k-1}^{k}\ln t\,dt$, et en sommant :
$$n\ln n \geq \ln(n!) \geq \int_1^n \ln t\,dt = n\ln n - n + 1$$
Donc $\ln(n!) \underset{+\infty}{\sim} n\ln n$ et
$$0 < \frac{n}{(\ln(n!))^2} \underset{+\infty}{\sim} \frac{n}{n^2\ln^2 n} = \frac{1}{n\ln^2 n}$$
La série $\sum_{n\geq 2}\frac{1}{n\ln^2 n}$ converge : la fonction $f(t) = \frac{1}{t\ln^2 t}$ est positive et décroissante sur $[2, +\infty[$, donc pour $n \geq 3$, $f(n) \leq \int_{n-1}^{n} f(t)\,dt$ et
$$\sum_{n=3}^{N}\frac{1}{n\ln^2 n} \leq \int_2^N\frac{dt}{t\ln^2 t} = \left[-\frac{1}{\ln t}\right]_2^N = \frac{1}{\ln 2} - \frac{1}{\ln N} \leq \frac{1}{\ln 2}$$
Les sommes partielles de cette série à termes positifs sont majorées : elle converge (série de Bertrand). Par équivalence, $\sum \frac{n}{(\ln(n!))^2}$ **converge**.

**Troisième série.** Pour $n \geq 0$, $\frac{1}{2^n} \in \,]0, 1]$, donc $\cos\frac{1}{2^n} \in \,]0, 1[$ et le terme général est bien défini et **négatif**. Quand $x \to 0$, $\ln(\cos x) = \ln\left(1 - \frac{x^2}{2} + o(x^2)\right) \sim -\frac{x^2}{2}$, donc
$$\ln\left(\cos\frac{1}{2^n}\right) \underset{+\infty}{\sim} -\frac{1}{2\cdot 4^n}$$
La série géométrique $\sum \frac{1}{4^n}$ converge (raison $\frac{1}{4}$). Les termes étant de signe constant, par équivalence la série **converge**.

## Exercice 4 : Deux preuves de la divergence de la série harmonique

**Énoncé.** (8 points) Notre objectif est de montrer la divergence de la série harmonique $\sum_{n\geq 1}\frac{1}{n}$ avec deux méthodes différentes.

1. **Méthode 1 :** On note, pour $n \in \mathbb{N}^*$, $S_n = \sum_{k=1}^{n}\frac{1}{k}$.
    a) Montrer que, pour tout $n \geq 1$,
$$\int_1^{n+1}\frac{1}{t}\,dt \leq S_n \leq 1 + \int_1^{n}\frac{1}{t}\,dt$$
    b) Déduire un équivalent de $(S_n)_n$.
    c) Déduire la divergence de la série harmonique $\sum_{n\geq 1}\frac{1}{n}$.
2. **Méthode 2 :** On pose, pour $n \in \mathbb{N}^*$, $H_n = \sum_{k=n+1}^{2n}\frac{1}{k}$.
    a) Vérifier que pour tout $n \geq 1$, $R_n \geq H_n$, avec $R_n = \sum_{k\geq n+1}\frac{1}{k}$.
    b) Montrer que pour tout $n \geq 1$, la suite $(H_n)_n$ est minorée par $\frac{1}{2}$.
    c) Déduire la divergence de la série harmonique $\sum_{n\geq 1}\frac{1}{n}$.

> **Erreur corrigée :** le sujet imprimé écrit $S_n \leq \int_1^n \frac{1}{t}\,dt$, ce qui est faux (par exemple $S_1 = 1 > 0$) ; il manque le terme $1$ (une correction manuscrite est visible sur la copie scannée).

**Correction.**

**1. a)** Soit $k \geq 1$. La fonction $t \mapsto \frac{1}{t}$ est décroissante sur $[k, k+1]$, donc $\frac{1}{k+1} \leq \frac{1}{t} \leq \frac{1}{k}$ et, en intégrant sur cet intervalle de longueur $1$,
$$\frac{1}{k+1} \leq \int_k^{k+1}\frac{dt}{t} \leq \frac{1}{k}$$
En sommant l'inégalité de droite pour $k = 1, \dots, n$ : $\int_1^{n+1}\frac{dt}{t} \leq S_n$. En sommant l'inégalité de gauche pour $k = 1, \dots, n-1$ : $S_n - 1 \leq \int_1^{n}\frac{dt}{t}$ (égalité $0 = 0$ si $n = 1$). D'où l'encadrement.

**b)** Il s'écrit $\ln(n+1) \leq S_n \leq 1 + \ln n$. Pour $n \geq 2$, en divisant par $\ln n > 0$ :
$$\frac{\ln(n+1)}{\ln n} = 1 + \frac{\ln\left(1 + \frac{1}{n}\right)}{\ln n} \leq \frac{S_n}{\ln n} \leq 1 + \frac{1}{\ln n}$$
Les deux bornes tendent vers $1$ : $S_n \underset{+\infty}{\sim} \ln n$.

**c)** $S_n \geq \ln(n+1) \to +\infty$ : les sommes partielles tendent vers $+\infty$, la série harmonique **diverge**.

**2.** On raisonne par l'absurde : supposons que $\sum \frac{1}{n}$ converge, de sorte que le reste $R_n = \sum_{k\geq n+1}\frac{1}{k}$ est bien défini et que $R_n \to 0$.

**a)** Tous les termes sont positifs, donc le reste est supérieur à n'importe laquelle de ses sommes partielles :
$$R_n = \sum_{k=n+1}^{2n}\frac{1}{k} + \sum_{k\geq 2n+1}\frac{1}{k} \geq \sum_{k=n+1}^{2n}\frac{1}{k} = H_n$$

**b)** $H_n$ est une somme de $n$ termes, chacun $\geq \frac{1}{2n}$ (car $k \leq 2n$) :
$$H_n \geq n\cdot\frac{1}{2n} = \frac{1}{2}$$

**c)** D'après a) et b), $R_n \geq \frac{1}{2}$ pour tout $n$, ce qui contredit $R_n \to 0$. La série harmonique **diverge**.

On peut aussi éviter l'absurde : $H_n = S_{2n} - S_n \geq \frac{1}{2}$. Si $(S_n)$ convergeait vers $S$, on aurait $S_{2n} - S_n \to S - S = 0$, impossible.
