# Séries — Devoir Surveillé 1 — Corrigé

**CY Tech — 2026/2027 — Semestre 1 — PréIng 2**
Jeudi 15 octobre 2026

---

## Exercice 1

**1. Faux.**
Contre-exemple : $v_n = \dfrac{1}{n}$ et $u_n = \dfrac{1}{n^2}$. On a $\dfrac{u_n}{v_n} = \dfrac{1}{n} \to 0$, donc $u_n = o(v_n)$. De plus $\sum v_n$ diverge (série harmonique), mais $\sum u_n$ converge (Riemann, $2>1$).

**2. Vrai.**
Comme $u_n = o(v_n)$, on a $\dfrac{u_n}{v_n} \to 0$. Il existe donc $N$ tel que, pour tout $n \ge N$, $\dfrac{u_n}{v_n} \le 1$, c'est-à-dire $0 \le u_n \le v_n$. Les séries étant à termes positifs et $\sum v_n$ convergeant, le critère de comparaison donne la convergence de $\sum u_n$.

**3. Faux.**
Même contre-exemple : $u_n = \dfrac{1}{n^2}$, $v_n = \dfrac{1}{n}$. On a $u_n = o(v_n)$ et $\sum u_n$ converge, mais $\sum v_n$ diverge.

---

## Exercice 2

**1. $\displaystyle\sum_{n\ge1} \frac{\ln n}{n^{5/4}}$ — converge.**

Série à termes positifs. On a
$$n^{9/8}\cdot\frac{\ln n}{n^{5/4}} = \frac{\ln n}{n^{1/8}} \xrightarrow[n\to+\infty]{} 0$$
par croissances comparées, donc $\dfrac{\ln n}{n^{5/4}} = o\!\left(\dfrac{1}{n^{9/8}}\right)$. Or $\sum \dfrac{1}{n^{9/8}}$ converge (Riemann, $\tfrac98>1$). Par comparaison de séries à termes positifs, la série converge.

**2. $\displaystyle\sum_{n\ge1} \ln\!\left(\cos\frac{1}{\sqrt n}\right)$ — diverge.**

Quand $x \to 0$ : $\cos x = 1 - \dfrac{x^2}{2} + o(x^2)$, donc $\ln(\cos x) \sim -\dfrac{x^2}{2}$. Avec $x = \dfrac{1}{\sqrt n} \to 0$ :
$$\ln\!\left(\cos\frac{1}{\sqrt n}\right) \sim -\frac{1}{2n}.$$
Le terme général est de signe constant (négatif) et équivalent à $-\dfrac{1}{2n}$. La série $\sum \dfrac{1}{2n}$ diverge, donc la série étudiée diverge.

**3. $\displaystyle\sum_{n\ge1} (-1)^n\left(\sqrt{n+1}-\sqrt n\right)$ — converge.**

On écrit
$$\sqrt{n+1}-\sqrt n = \frac{1}{\sqrt{n+1}+\sqrt n} =: a_n.$$
La suite $(a_n)$ est positive, décroissante et tend vers $0$. Par le critère spécial des séries alternées, $\sum (-1)^n a_n$ converge.

**4. $\displaystyle\sum_{n\ge1} \frac{1+(-1)^n\sqrt n}{1+n}$ — diverge.**

On décompose :
$$\frac{1+(-1)^n\sqrt n}{1+n} = \underbrace{\frac{1}{n+1}}_{\text{diverge}} + \underbrace{(-1)^n\frac{\sqrt n}{n+1}}_{\text{converge}}.$$

- $\sum \dfrac{1}{n+1}$ diverge (série harmonique décalée).
- Pour $b_n = \dfrac{\sqrt n}{n+1}$ : $b_n \to 0$ et, avec $f(x) = \dfrac{\sqrt x}{x+1}$, $f'(x) = \dfrac{1-x}{2\sqrt x\,(x+1)^2} \le 0$ pour $x \ge 1$, donc $(b_n)$ est décroissante. Le critère des séries alternées donne la convergence de $\sum (-1)^n b_n$.

La somme d'une série convergente et d'une série divergente diverge : la série diverge.

---

## Exercice 3

On simplifie d'abord :
$$u_n = \frac{2^n\,n(n-1)}{3^n\,n(n-1)} + \frac{3^n}{3^n\,n(n-1)} = \left(\frac{2}{3}\right)^n + \frac{1}{n(n-1)}.$$

**1. Convergence.**

- $\sum_{n\ge2} \left(\tfrac23\right)^n$ est géométrique de raison $\tfrac23 \in\, ]-1,1[$ : elle converge.
- $\dfrac{1}{n(n-1)} \sim \dfrac{1}{n^2}$, terme positif, et $\sum \dfrac{1}{n^2}$ converge (Riemann) : $\sum \dfrac{1}{n(n-1)}$ converge.

Somme de deux séries convergentes, $\sum_{n\ge2} u_n$ converge.

**2. Décomposition de $S_n$.**

Comme $\dfrac{1}{n(n-1)} = \dfrac{1}{n-1} - \dfrac{1}{n}$, on a, pour $n \ge 2$ :
$$S_n = \underbrace{\sum_{k=2}^{n}\left(\frac23\right)^k}_{T_n} + \underbrace{\sum_{k=2}^{n}\left(\frac{1}{k-1}-\frac1k\right)}_{W_n}.$$

- $T_n$ est la somme partielle d'une série géométrique de **raison $\tfrac23$** et de premier terme $\tfrac49$ :
$$T_n = \frac49\cdot\frac{1-\left(\frac23\right)^{n-1}}{1-\frac23} = \frac43\left(1-\left(\frac23\right)^{n-1}\right).$$
- $W_n$ est télescopique :
$$W_n = \left(1-\tfrac12\right)+\left(\tfrac12-\tfrac13\right)+\dots+\left(\tfrac{1}{n-1}-\tfrac1n\right) = 1-\frac1n.$$

**3. Valeur de la somme.**

Quand $n\to+\infty$ : $T_n \to \dfrac43$ et $W_n \to 1$. Donc
$$S = \sum_{n=2}^{+\infty} u_n = \frac43 + 1 = \boxed{\frac73}.$$

---

## Exercice 4

**1. Comparaison série/intégrale.**

Soit $f(x) = \dfrac{\ln x}{x}$, définie et dérivable sur $[3,+\infty[$ :
$$f'(x) = \frac{1-\ln x}{x^2}.$$
Pour $x \ge 3 > e$, $\ln x > 1$ donc $f'(x) < 0$ : $f$ est décroissante sur $[3,+\infty[$.

Pour $k \ge 3$ et $x \in [k,k+1]$, on a $f(x) \le f(k)$, d'où en intégrant
$$\int_k^{k+1} f(x)\,\mathrm dx \le f(k) = \frac{\ln k}{k}.$$
En sommant pour $k$ de $3$ à $n$ (relation de Chasles) :
$$\sum_{k=3}^{n}\frac{\ln k}{k} \ge \sum_{k=3}^{n}\int_k^{k+1} f(x)\,\mathrm dx = \int_3^{n+1}\frac{\ln x}{x}\,\mathrm dx.$$

**2. Calcul de l'intégrale.**

Une primitive de $\dfrac{\ln x}{x} = \ln x \cdot (\ln x)'$ est $\dfrac12\ln^2 x$. Donc
$$\int_3^{n+1}\frac{\ln x}{x}\,\mathrm dx = \left[\frac12\ln^2 x\right]_3^{n+1} = \frac12\left(\ln^2(n+1)-\ln^2(3)\right).$$

**3. Minoration.**

En combinant les questions 1 et 2 :
$$\sum_{k=3}^{n}\frac{\ln k}{k} \ge \frac12\left(\ln^2(n+1)-\ln^2(3)\right).$$

**4. Nature de la série.**

Pour $n\ge3$, $\dfrac{\ln n}{n} > 0$ : les sommes partielles sont croissantes. Or
$$\frac12\left(\ln^2(n+1)-\ln^2(3)\right) \xrightarrow[n\to+\infty]{} +\infty,$$
donc les sommes partielles tendent vers $+\infty$. La série $\displaystyle\sum_{n\ge3}\frac{\ln n}{n}$ **diverge**.
