---
source: TD1-Correction_2024-2025_Series_P2S1_DMaths.pdf, pages 1 à 15
transcription: manuelle
---

# Séries — TD1 : séries numériques (2024/2025, corrigé)

## Exercice 1 : Condition nécessaire de convergence

**Énoncé.** Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n \ge 1} \cos\frac{1}{n^2}$
2. $\displaystyle\sum_{n \ge 0} \frac{(-1)^n n}{n+1}$
3. $\displaystyle\sum_{n \ge 1} \left(1 + \frac{1}{n}\right)^n$
4. $\displaystyle\sum_{n \ge 1} \left(\cos\frac{1}{n}\right)^{n^2}$

**Correction.** Dans les quatre cas, le terme général ne tend pas vers $0$ : les séries **divergent grossièrement** (elles ne vérifient pas la condition nécessaire de convergence).

**1.** $\cos\frac{1}{n^2} \to \cos 0 = 1 \ne 0$.

**2.** $\left|\dfrac{(-1)^n n}{n+1}\right| = \dfrac{n}{n+1} \to 1$, donc le terme général ne tend pas vers $0$.

> **Erreur corrigée :** le corrigé écrivait $\frac{(-1)^n n}{n+1} = \frac{n}{n+1}$ ; l'égalité n'a lieu qu'en valeur absolue (le terme général lui-même n'a pas de limite, il oscille entre des valeurs proches de $1$ et de $-1$).

**3.** $\ln\left(1 + \frac{1}{n}\right)^n = n\ln\left(1 + \frac{1}{n}\right) = n\left(\frac{1}{n} + o\left(\frac{1}{n}\right)\right) = 1 + o(1) \to 1$, donc $\left(1 + \frac{1}{n}\right)^n \to e \ne 0$.

**4.** $\ln\left(\cos\frac{1}{n}\right)^{n^2} = n^2\ln\left(1 - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right)\right) = n^2\left(-\frac{1}{2n^2} + o\left(\frac{1}{n^2}\right)\right) = -\frac{1}{2} + o(1)$, donc $\left(\cos\frac{1}{n}\right)^{n^2} \to \frac{1}{\sqrt{e}} \ne 0$.

## Exercice 2 : Séries à termes positifs

**Énoncé.** Déterminer la nature des séries suivantes :

1. $\displaystyle\sum_{n \ge 1} \frac{n^2 + 1}{n^2}$
2. $\displaystyle\sum_{n \ge 1} \frac{2}{\sqrt{n}}$
3. $\displaystyle\sum_{n \in \mathbb{N}} \frac{(2n+1)^4}{(7n^2+1)^3}$
4. $\displaystyle\sum_{n \ge 1} \left(n e^{\frac{1}{n}} - n\right)$
5. $\displaystyle\sum_{n \ge 2} \frac{1}{(\ln(n))^n}$
6. $\displaystyle\sum_{n \in \mathbb{N}} \ln\left(1 + e^{-n}\right)$

**Correction.** Toutes ces séries sont à termes positifs.

**1.** $\dfrac{n^2 + 1}{n^2} \to 1 \ne 0$ : divergence grossière.

**2.** $\dfrac{2}{\sqrt{n}} = 2 \cdot \dfrac{1}{n^{1/2}}$ : c'est (à la constante $2$ près) le terme général d'une série de Riemann avec $\alpha = \frac{1}{2} \le 1$. La série diverge.

**3.** $\dfrac{(2n+1)^4}{(7n^2+1)^3} \sim \dfrac{2^4 n^4}{7^3 n^6} = \dfrac{16}{343} \cdot \dfrac{1}{n^2}$. Série de Riemann convergente ($\alpha = 2 > 1$) : par le théorème d'équivalence pour les séries à termes positifs, la série converge.

**4.** $n e^{1/n} - n = n\left(e^{1/n} - 1\right) = n\left(\frac{1}{n} + o\left(\frac{1}{n}\right)\right) = 1 + o(1) \to 1 \ne 0$ : divergence grossière.

**5.** Règle de Cauchy : $\sqrt[n]{u_n} = \dfrac{1}{\ln n} \to 0 < 1$, donc la série converge.

**6.** $\ln(1 + e^{-n}) \sim e^{-n} = \left(\frac{1}{e}\right)^n$, terme général d'une série géométrique de raison $\frac{1}{e} \in \,]-1, 1[$, donc convergente. Par équivalence (termes positifs), la série converge.

## Exercice 3 : Même nature que u sur 1+u

**Énoncé.** Soit $(u_n)$ une suite de réels positifs et $v_n = \dfrac{u_n}{1 + u_n}$. Montrer que $\displaystyle\sum_{n \in \mathbb{N}} u_n$ et $\displaystyle\sum_{n \in \mathbb{N}} v_n$ sont de même nature.

**Correction.** Il s'agit de montrer : $\sum u_n$ converge $\iff$ $\sum v_n$ converge. Les deux séries sont à termes positifs.

- $(\Rightarrow)$ Si $\sum u_n$ converge, alors $u_n \to 0$, donc $1 + u_n \to 1$ et $v_n = \dfrac{u_n}{1 + u_n} \sim u_n$. Par le théorème d'équivalence, $\sum v_n$ converge. (On peut aussi dire directement $0 \le v_n \le u_n$.)
- $(\Leftarrow)$ Si $\sum v_n$ converge, alors $v_n \to 0$. De $v_n(1 + u_n) = u_n$ on tire $u_n = \dfrac{v_n}{1 - v_n}$ (on a $v_n < 1$ pour tout $n$). Donc $u_n \sim v_n$ et, par équivalence, $\sum u_n$ converge.

*Remarque :* de même, $\sum u_n$ diverge grossièrement si et seulement si $\sum v_n$ diverge grossièrement, puisque $u_n \to 0 \iff v_n \to 0$.

## Exercice 4 : Sommes télescopiques

**Énoncé.** Étudier la nature et, le cas échéant, calculer la somme des séries de terme général :

1. $u_n = \dfrac{1}{n(n+1)}$
2. $u_n = \dfrac{1}{n(n+1)(n+2)}$
3. $u_n = \dfrac{2n - 1}{n(n^2 - 4)}$
4. $u_n = \ln\left(1 - \dfrac{1}{(n+2)^2}\right)$

**Correction.** Méthode : l'équivalent donne la nature ; pour la somme, on décompose en éléments simples et on fait apparaître des sommes télescopiques.

**1.** $u_n \sim \frac{1}{n^2}$ : la série converge (Riemann, $\alpha = 2$). On a $u_n = \frac{1}{n} - \frac{1}{n+1}$, donc
$$\sum_{k=1}^n u_k = \sum_{k=1}^n \frac{1}{k} - \sum_{k=2}^{n+1} \frac{1}{k} = 1 - \frac{1}{n+1} \xrightarrow[n \to +\infty]{} 1$$

Donc $\displaystyle\sum_{n=1}^{+\infty} \frac{1}{n(n+1)} = 1$.

**2.** $u_n \sim \frac{1}{n^3}$ : la série converge. Décomposition : $u_n = \dfrac{1}{2n} - \dfrac{1}{n+1} + \dfrac{1}{2(n+2)}$. On écrit
$$u_n = \frac{1}{2}\left(\frac{1}{n} - \frac{1}{n+1}\right) - \frac{1}{2}\left(\frac{1}{n+1} - \frac{1}{n+2}\right)$$

donc, par télescopage,
$$\sum_{k=1}^n u_k = \frac{1}{2}\left(1 - \frac{1}{n+1}\right) - \frac{1}{2}\left(\frac{1}{2} - \frac{1}{n+2}\right) = \frac{1}{4} - \frac{1}{2(n+1)} + \frac{1}{2(n+2)}$$

Donc $\displaystyle\sum_{n=1}^{+\infty} \frac{1}{n(n+1)(n+2)} = \frac{1}{4}$.

> **Note :** le corrigé fait le même calcul en regroupant les trois sommes $\sum \frac{1}{k}$ décalées ; le résultat $\frac{1}{4}$ est le même.

**3.** Le terme n'est défini que pour $n \ge 3$ ($n^2 - 4 = 0$ pour $n = 2$). $u_n \sim \frac{2n}{n^3} = \frac{2}{n^2}$ : la série converge. Décomposition en éléments simples :
$$u_n = \frac{2n - 1}{n(n-2)(n+2)} = \frac{1/4}{n} + \frac{3/8}{n-2} - \frac{5/8}{n+2}$$

(on trouve les coefficients en évaluant $\frac{2n-1}{(n-2)(n+2)}$ en $n = 0$, $\frac{2n-1}{n(n+2)}$ en $n = 2$ et $\frac{2n-1}{n(n-2)}$ en $n = -2$). Pour $n \ge 5$ :
$$\sum_{k=3}^n u_k = \frac{1}{4}\sum_{k=3}^n \frac{1}{k} + \frac{3}{8}\sum_{j=1}^{n-2} \frac{1}{j} - \frac{5}{8}\sum_{j=5}^{n+2} \frac{1}{j}$$

Comme $\frac{1}{4} + \frac{3}{8} - \frac{5}{8} = 0$, les termes d'indice $5$ à $n - 2$ se compensent. Il reste
$$\sum_{k=3}^n u_k = \frac{1}{4}\left(\frac{1}{3} + \frac{1}{4}\right) + \frac{3}{8}\left(1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4}\right) + \varepsilon_n$$

où $\varepsilon_n$ est une combinaison des termes $\frac{1}{n-1}, \frac{1}{n}, \frac{1}{n+1}, \frac{1}{n+2}$, qui tend vers $0$. Donc
$$\sum_{n=3}^{+\infty} u_n = \frac{1}{4} \cdot \frac{7}{12} + \frac{3}{8} \cdot \frac{25}{12} = \frac{7}{48} + \frac{25}{32} = \frac{89}{96}$$

**4.** $u_n \sim -\frac{1}{(n+2)^2} \sim -\frac{1}{n^2}$ : la série est de signe constant (négatif) et converge par équivalence avec une série de Riemann. Pour la somme :
$$1 - \frac{1}{(k+2)^2} = \frac{(k+2)^2 - 1}{(k+2)^2} = \frac{(k+1)(k+3)}{(k+2)^2}$$

donc $u_k = \big[\ln(k+3) - \ln(k+2)\big] - \big[\ln(k+2) - \ln(k+1)\big]$, et par télescopage
$$\sum_{k=1}^n u_k = \big[\ln(n+3) - \ln 3\big] - \big[\ln(n+2) - \ln 2\big] = \ln\frac{n+3}{n+2} + \ln\frac{2}{3}$$

Comme $\frac{n+3}{n+2} \to 1$ : $\displaystyle\sum_{n=1}^{+\infty} \ln\left(1 - \frac{1}{(n+2)^2}\right) = \ln\frac{2}{3}$.

> **Erreur corrigée :** le corrigé écrivait $(k+2-1)(k+2-1)$ au lieu de $(k+2-1)(k+2+1)$, et obtenait la somme partielle $\ln\frac{(n+2)(n+3)}{(n+1)^2} + \ln 2 - \ln 3$, qui est fausse (pour $n = 1$ elle vaut $\ln 2$ au lieu de $\ln\frac{8}{9}$). La bonne somme partielle est $\ln\frac{n+3}{n+2} + \ln\frac{2}{3}$ ; la limite $\ln\frac{2}{3}$ était juste.

## Exercice 5 : Séries de Bertrand

**Énoncé.**

1. Montrer que
$$\forall n \ge 2, \quad \sum_{k=2}^n \frac{1}{k\ln k} \ge \ln(\ln(n+1)) - \ln(\ln 2)$$
2. En déduire la nature de la série $\displaystyle\sum_{n \ge 2} \frac{1}{n\ln n}$.
3. Montrer que
$$\forall n \ge 3, \quad \sum_{k=3}^n \frac{1}{k\ln^2 k} \le \frac{1}{\ln 2}$$
4. En déduire la nature de la série $\displaystyle\sum_{n \ge 2} \frac{1}{n\ln^2 n}$.

**Correction.** Méthode : comparaison série-intégrale pour une fonction décroissante.

**1.** La fonction $f : t \mapsto \frac{1}{t\ln t}$ est décroissante sur $]1, +\infty[$ (car $t \mapsto t\ln t$ y est croissante et strictement positive). Pour $k \ge 2$ et $t \in [k, k+1]$, $f(t) \le f(k)$, donc en intégrant sur $[k, k+1]$ (intervalle de longueur $1$) :
$$\int_k^{k+1} \frac{dt}{t\ln t} \le \frac{1}{k\ln k}$$

En sommant pour $k$ de $2$ à $n$, et comme une primitive de $\frac{1}{t\ln t} = \frac{(\ln t)'}{\ln t}$ est $\ln(\ln t)$ :
$$\sum_{k=2}^n \frac{1}{k\ln k} \ge \int_2^{n+1} \frac{dt}{t\ln t} = \ln(\ln(n+1)) - \ln(\ln 2)$$

**2.** $\ln(\ln(n+1)) \to +\infty$, donc les sommes partielles de la série à termes positifs $\sum \frac{1}{n\ln n}$ ne sont pas majorées : **la série diverge**.

**3.** La fonction $g : t \mapsto \frac{1}{t\ln^2 t}$ est décroissante sur $]1, +\infty[$. Pour $k \ge 3$ et $t \in [k-1, k]$, $g(k) \le g(t)$, donc
$$\frac{1}{k\ln^2 k} \le \int_{k-1}^k \frac{dt}{t\ln^2 t}$$

Une primitive de $\frac{1}{t\ln^2 t} = \frac{(\ln t)'}{\ln^2 t}$ est $-\frac{1}{\ln t}$. En sommant pour $k$ de $3$ à $n$ :
$$\sum_{k=3}^n \frac{1}{k\ln^2 k} \le \int_2^n \frac{dt}{t\ln^2 t} = \frac{1}{\ln 2} - \frac{1}{\ln n} \le \frac{1}{\ln 2}$$

**4.** Les sommes partielles de la série à termes positifs $\sum \frac{1}{n\ln^2 n}$ sont majorées (par $\frac{1}{2\ln^2 2} + \frac{1}{\ln 2}$) : **la série converge**.

> **Erreur corrigée :** le corrigé affirmait que $t \mapsto \frac{1}{t\ln t}$ et $t \mapsto \frac{1}{t\ln^2 t}$ sont décroissantes sur $]0, +\infty[$ : elles ne sont même pas définies en $1$ ; c'est sur $]1, +\infty[$ qu'elles sont décroissantes. À la question 3, il écrivait aussi $\frac{1}{t\ln t}$ au lieu de $\frac{1}{t\ln^2 t}$ dans l'inégalité de départ (il comparait $g(t)$ à $g(k+1)$ sur $[k, k+1]$, ce qui revient au même que ci-dessus).

## Exercice 6 : Exercices supplémentaires, quinze séries

**Énoncé.** Étudier la nature de la série de terme général

1. $u_n = \dfrac{n+1}{n^3 - 7}$
2. $u_n = \dfrac{n+1}{n^2 - 7}$
3. $u_n = \dfrac{n+1}{n - 7}$
4. $u_n = \sin\left(\dfrac{1}{n^2}\right)$
5. $u_n = \dfrac{1}{n^{1 + \frac{1}{\sqrt{n}}}}$
6. $u_n = \dfrac{1}{\ln(n^2 + 2)}$
7. $u_n = \dfrac{\ln(n)}{n^{3/2}}$
8. $u_n = \dfrac{n^n}{2^n}$
9. $u_n = \dfrac{2^n + 3^n}{n^2 + \ln(n) + 5^n}$
10. $u_n = \dfrac{1}{n!}$
11. $u_n = \dfrac{n^{10000}}{n!}$
12. $u_n = \dfrac{4^{n+1}((n+1)!)^2}{(2n-1)!}$
13. $u_n = \left(\sin\left(\dfrac{1}{n}\right)\right)^n$
14. $u_n = \left(1 - \dfrac{1}{n}\right)^{n^2}$
15. $u_n = \left(1 + \dfrac{1}{n}\right)^{n^2}$

**Correction.** Tous ces termes sont positifs à partir d'un certain rang (pour les trois premiers, dès $n \ge 8$).

**1.** $u_n \sim \frac{1}{n^2}$ : Riemann avec $\alpha = 2 > 1$, la série **converge**.

**2.** $u_n \sim \frac{1}{n}$ : série harmonique, la série **diverge**.

**3.** $u_n \to 1 \ne 0$ : **divergence grossière**.

**4.** $u_n \sim \frac{1}{n^2}$ : la série **converge**.

**5.** Méfiance : l'exposant dépend de $n$. $u_n = \dfrac{1}{n} \cdot n^{-1/\sqrt{n}} = \dfrac{1}{n}\,e^{-\frac{\ln n}{\sqrt{n}}}$. Comme $\frac{\ln n}{\sqrt{n}} \to 0$, $e^{-\frac{\ln n}{\sqrt{n}}} \to 1$ et $u_n \sim \frac{1}{n}$ : la série **diverge**.

**6.** $\ln(n^2 + 2) = 2\ln n + \ln\left(1 + \frac{2}{n^2}\right) \sim 2\ln n$, donc $u_n \sim \frac{1}{2\ln n}$ et $\sqrt{n}\,u_n \to +\infty$ (croissances comparées). Donc $u_n \ge \frac{1}{\sqrt{n}}$ à partir d'un certain rang : la série **diverge** (règle de Riemann « $n^\alpha u_n \to +\infty$ avec $\alpha \le 1$ »).

**7.** $n^{5/4}u_n = \dfrac{\ln n}{n^{1/4}} \to 0$, donc $u_n = o\left(\frac{1}{n^{5/4}}\right)$ avec $\frac{5}{4} > 1$ : la série **converge**.

> **Erreur corrigée :** le corrigé énonçait ici la règle « $n^\alpha u_n \to +\infty$ avec $\alpha > 1$ entraîne la convergence », ce qui est faux ; la règle correcte est « $n^\alpha u_n \to 0$ avec $\alpha > 1$ ».

**8.** $u_n = \left(\dfrac{n}{2}\right)^n \to +\infty$ : **divergence grossière**. (Par d'Alembert : $\dfrac{u_{n+1}}{u_n} = \dfrac{n+1}{2}\left(1 + \dfrac{1}{n}\right)^n \to +\infty$.)

> **Erreur corrigée :** le corrigé calculait $\frac{u_{n+1}}{u_n} = \frac{n+1}{n} \times \frac{1}{2} \to \frac{1}{2}$ et concluait à la convergence. C'est faux : $\frac{(n+1)^{n+1}}{n^n} = (n+1)\left(1 + \frac{1}{n}\right)^n$, et non $\frac{n+1}{n}$. La série diverge grossièrement.

**9.** $u_n \sim \dfrac{3^n}{5^n} = \left(\dfrac{3}{5}\right)^n$, terme d'une série géométrique convergente : la série **converge**.

**10.** $\dfrac{u_{n+1}}{u_n} = \dfrac{1}{n+1} \to 0 < 1$ : d'après la règle de d'Alembert, la série **converge** (sa somme vaut $e$ si elle commence à $n = 0$).

**11.** $\dfrac{u_{n+1}}{u_n} = \left(\dfrac{n+1}{n}\right)^{10000} \cdot \dfrac{1}{n+1} \to 0 < 1$ : la série **converge**.

**12.** $\dfrac{u_{n+1}}{u_n} = \dfrac{4^{n+2}((n+2)!)^2}{(2n+1)!} \cdot \dfrac{(2n-1)!}{4^{n+1}((n+1)!)^2} = \dfrac{4(n+2)^2}{(2n+1)(2n)} = \dfrac{4n^2 + 16n + 16}{4n^2 + 2n}$.

Ce rapport tend vers $1$ : la règle de d'Alembert ne conclut pas directement. Mais il est **strictement supérieur à $1$** pour tout $n \ge 1$. La suite $(u_n)$ est donc strictement croissante et positive : elle ne tend pas vers $0$, et la série **diverge grossièrement**.

> **Note :** le corrigé disait « la limite est $1^+$ donc la série diverge » ; l'argument exact est que $u_{n+1} > u_n > 0$ empêche $u_n \to 0$.

**13.** Pour $n \ge 1$, $0 < \sin\frac{1}{n} \le \frac{1}{n}$, donc $0 < u_n \le \left(\frac{1}{n}\right)^n \le \left(\frac{1}{2}\right)^n$ pour $n \ge 2$. Par comparaison avec une série géométrique convergente, la série **converge**.

> **Erreur corrigée :** le corrigé écrivait $\left(\sin\frac{1}{n}\right)^n = e^{n\sin(1/n)}$ au lieu de $e^{n\ln(\sin(1/n))}$, trouvait une limite $e \ne 0$ et concluait à une divergence grossière. En réalité $n\ln\left(\sin\frac{1}{n}\right) \to -\infty$, $u_n \to 0$ très vite et la série converge.

**14.** $u_n = \exp\left(n^2\ln\left(1 - \frac{1}{n}\right)\right) = \exp\left(n^2\left(-\frac{1}{n} - \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right)\right)\right) = e^{-n}\,e^{-\frac{1}{2} + o(1)}$, donc
$$u_n \sim \frac{1}{\sqrt{e}}\left(\frac{1}{e}\right)^n$$

Série géométrique de raison $\frac{1}{e} < 1$ : la série **converge**.

**15.** $u_n = \left(1 + \frac{1}{n}\right)^{n^2} > 1$ (et même $u_n \to +\infty$) : **divergence grossière**.

## Exercice 7 : Règle de Cauchy avec paramètres

**Énoncé.** Étudier la nature de la série de terme général :
$$u_n = \left(\sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1}\right)^n, \qquad (a, b) \in \mathbb{R}^2,\ a \ge b$$

**Correction.** La forme du terme général suggère la règle de Cauchy. Pour $n$ assez grand, les racines sont définies et
$$x_n = \sqrt{n^2 + an + 2} - \sqrt{n^2 + bn + 1} = \frac{(a - b)n + 1}{\sqrt{n^2 + an + 2} + \sqrt{n^2 + bn + 1}} > 0$$

car $a \ge b$. Donc $u_n = x_n^n > 0$ et $\sqrt[n]{u_n} = x_n$. Développons avec $\sqrt{1 + h} = 1 + \frac{h}{2} - \frac{h^2}{8} + O(h^3)$ :
$$\sqrt{n^2 + an + 2} = n + \frac{a}{2} + \left(1 - \frac{a^2}{8}\right)\frac{1}{n} + O\left(\frac{1}{n^2}\right)$$
$$\sqrt{n^2 + bn + 1} = n + \frac{b}{2} + \left(\frac{1}{2} - \frac{b^2}{8}\right)\frac{1}{n} + O\left(\frac{1}{n^2}\right)$$

d'où
$$\sqrt[n]{u_n} = x_n = \frac{a - b}{2} + \frac{4 - a^2 + b^2}{8n} + O\left(\frac{1}{n^2}\right) \xrightarrow[n \to +\infty]{} \frac{a - b}{2}$$

- Si $\frac{a - b}{2} < 1$, c'est-à-dire $a - b < 2$ : la série **converge** (règle de Cauchy).
- Si $\frac{a - b}{2} > 1$ : la série **diverge** (grossièrement, $u_n \to +\infty$).
- Si $\frac{a - b}{2} = 1$, c'est-à-dire $a = b + 2$ : alors $a^2 - b^2 = (a - b)(a + b) = 4b + 4$, donc $x_n = 1 + \frac{c}{n} + O\left(\frac{1}{n^2}\right)$ avec $c = \frac{4 - 4b - 4}{8} = -\frac{b}{2}$. Par suite
$$u_n = \exp\left(n\ln\left(1 + \frac{c}{n} + O\left(\frac{1}{n^2}\right)\right)\right) = \exp\left(c + O\left(\frac{1}{n}\right)\right) \xrightarrow[n \to +\infty]{} e^{-b/2} \ne 0$$
La série **diverge grossièrement**.

**Conclusion :** la série converge si et seulement si $a - b < 2$.

> **Erreur corrigée :** dans le cas $\frac{a-b}{2} = 1$, le corrigé distinguait $a + b < 2$ et $a + b \ge 2$ et écrivait $\ln(n^\alpha u_n) = \alpha\ln n + 2 - (a+b) + o(1)$ ; le terme constant est en fait $\frac{2 - (a+b)}{4}$. Surtout, la distinction est inutile : $u_n \to e^{\frac{2-(a+b)}{4}} = e^{-b/2} \ne 0$ dans tous les cas, d'où la divergence grossière. (Le corrigé écrivait aussi $o\left(\frac{1}{n^2}\right)$ là où le reste est un $O\left(\frac{1}{n^2}\right)$.)

## Exercice 8 : Termes équivalents, natures différentes

**Énoncé.** Considérons les séries
$$\sum_{n \ge 1} \frac{(-1)^n}{\sqrt{n}} \quad \text{et} \quad \sum_{n \ge 1} \ln\left(1 + \frac{(-1)^n}{\sqrt{n}}\right)$$

Montrer que les termes généraux de ces séries sont équivalents mais que les séries n'ont pas la même nature.

**Correction.** Pour $n \ge 2$, $\frac{(-1)^n}{\sqrt{n}} \in \,]-1, 1[$ et le logarithme est défini (pour $n = 1$ le terme $\ln(1 - 1)$ n'est pas défini : on commence en fait à $n = 2$, ce qui ne change pas la nature).

*Équivalence.* $\frac{(-1)^n}{\sqrt{n}} \to 0$ et $\ln(1 + x) \sim x$ en $0$, donc $\ln\left(1 + \frac{(-1)^n}{\sqrt{n}}\right) \sim \frac{(-1)^n}{\sqrt{n}}$.

*Première série.* C'est une série alternée : $\frac{1}{\sqrt{n}}$ décroît vers $0$, donc elle converge (critère spécial des séries alternées).

*Seconde série.* Avec $\ln(1 + x) = x - \frac{x^2}{2} + O(x^3)$ :
$$\ln\left(1 + \frac{(-1)^n}{\sqrt{n}}\right) = \frac{(-1)^n}{\sqrt{n}} - \frac{1}{2n} + O\left(\frac{1}{n^{3/2}}\right)$$

Posons $w_n = -\frac{1}{2n} + O\left(\frac{1}{n^{3/2}}\right)$. Alors $w_n \sim -\frac{1}{2n}$ est de signe constant à partir d'un certain rang, et $\sum \frac{1}{n}$ diverge : $\sum w_n$ diverge. La seconde série est la somme d'une série convergente et d'une série divergente : **elle diverge**.

Le théorème d'équivalence ne s'applique pas ici car les termes ne sont pas de signe constant.

> **Note :** le corrigé écrivait la seconde partie comme $\sum O\left(\frac{1}{n}\right)$ « divergente » ; un $O\left(\frac{1}{n}\right)$ peut très bien être le terme d'une série convergente, c'est l'équivalent $-\frac{1}{2n}$ qui donne la divergence.

## Exercice 9 : Développements asymptotiques

**Énoncé.** Étudier les séries :

1. $\displaystyle\sum_{n \ge 1} \left(\sqrt{1 + \frac{(-1)^n}{\sqrt{n}}} - 1\right)$
2. $\displaystyle\sum_{n \ge 1} (-1)^n\sqrt{n}\sin\frac{1}{n}$
3. $\displaystyle\sum_{n \ge 0} \frac{(-1)^n}{n + (-1)^n}$

**Correction.** Méthode : on développe le terme général en « terme alterné + reste absolument convergent ou de signe constant ».

**1.** Avec $\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + o(x^2)$ et $x = \frac{(-1)^n}{\sqrt{n}}$ :
$$\sqrt{1 + \frac{(-1)^n}{\sqrt{n}}} - 1 = \frac{(-1)^n}{2\sqrt{n}} - \frac{1}{8n} + o\left(\frac{1}{n}\right)$$

$\sum \frac{(-1)^n}{2\sqrt{n}}$ converge (série alternée) et le reste est équivalent à $-\frac{1}{8n}$, de signe constant, terme d'une série divergente. La série **diverge**.

**2.** $\sin\frac{1}{n} = \frac{1}{n} + O\left(\frac{1}{n^3}\right)$, donc
$$(-1)^n\sqrt{n}\sin\frac{1}{n} = \frac{(-1)^n}{\sqrt{n}} + O\left(\frac{1}{n^{5/2}}\right)$$

$\sum \frac{(-1)^n}{\sqrt{n}}$ converge (série alternée) et $\sum O\left(\frac{1}{n^{5/2}}\right)$ converge absolument. La série **converge**.

> **Note :** le corrigé écrivait le reste $O\left(\frac{1}{n\sqrt{n}}\right)$ ; c'est vrai mais moins précis (le reste est même $O(n^{-5/2})$) ; la conclusion est la même.

**3.** Pour $n = 1$, $n + (-1)^n = 0$ : le terme n'est pas défini, on étudie donc la série à partir de $n = 2$. Avec $\frac{1}{1 + x} = 1 - x + O(x^2)$ :
$$\frac{(-1)^n}{n + (-1)^n} = \frac{(-1)^n}{n} \cdot \frac{1}{1 + \frac{(-1)^n}{n}} = \frac{(-1)^n}{n} - \frac{1}{n^2} + O\left(\frac{1}{n^3}\right)$$

$\sum \frac{(-1)^n}{n}$ converge (série alternée) et le reste est un $O\left(\frac{1}{n^2}\right)$, terme d'une série absolument convergente. La série **converge**.

> **Note :** l'énoncé fait commencer la somme à $n = 0$, mais le terme d'indice $n = 1$ n'est pas défini ; le corrigé ne le signalait pas.

## Exercice 10 : Convergence de séries de termes quelconques

**Énoncé.** Étudier la convergence de la série numérique de terme général

1. $u_n = (-1)^n\dfrac{n^3}{n!}$
2. $u_n = \dfrac{a^n}{n!}$, $a \in \mathbb{C}$
3. $u_n = na^{n-1}$, $a \in \mathbb{C}$
4. $u_n = \sin\left(\dfrac{n^2 + 1}{n}\pi\right)$
5. $u_n = (-1)^n(\sqrt{n + 1} - \sqrt{n})$
6. $u_n = n\ln\left(1 + \dfrac{1}{n}\right) - \cos\left(\dfrac{1}{\sqrt{n}}\right)$

**Correction.**

> **Note :** dans l'énoncé, les questions 5 et 6 sont numérotées 3 et 4 (coquille) ; on les a renumérotées.

**1.** $v_n = |u_n| = \frac{n^3}{n!}$ et $\dfrac{v_{n+1}}{v_n} = \left(\dfrac{n+1}{n}\right)^3\dfrac{1}{n+1} \to 0 < 1$. Par la règle de d'Alembert, $\sum |u_n|$ converge : la série **converge absolument**, donc converge.

**2.** Si $a = 0$ c'est immédiat. Sinon $v_n = \frac{|a|^n}{n!}$ et $\dfrac{v_{n+1}}{v_n} = \dfrac{|a|}{n+1} \to 0$ : la série **converge absolument** pour tout $a \in \mathbb{C}$ (sa somme est $e^a$).

**3.** Si $|a| < 1$ : pour $a \ne 0$, $v_n = n|a|^{n-1}$ et $\dfrac{v_{n+1}}{v_n} = \dfrac{n+1}{n}|a| \to |a| < 1$, donc la série **converge absolument** (pour $a = 0$, tous les termes sont nuls sauf $u_1 = 1$). Si $|a| \ge 1$ : $|u_n| = n|a|^{n-1} \ge n \to +\infty$, la série **diverge grossièrement**.

**4.** $\dfrac{n^2 + 1}{n}\pi = n\pi + \dfrac{\pi}{n}$, donc $u_n = \sin\left(n\pi + \frac{\pi}{n}\right) = (-1)^n\sin\frac{\pi}{n}$. Pour $n \ge 2$, $a_n = \sin\frac{\pi}{n} \ge 0$ ; comme $\frac{\pi}{n} \in \,]0, \frac{\pi}{2}]$ décroît et que $\sin$ est croissante sur $[0, \frac{\pi}{2}]$, $(a_n)$ est décroissante, et elle tend vers $0$. D'après le critère spécial des séries alternées, la série **converge**. Elle n'est pas absolument convergente car $a_n \sim \frac{\pi}{n}$ : elle est **semi-convergente**.

**5.** $u_n = (-1)^n\dfrac{1}{\sqrt{n + 1} + \sqrt{n}}$ ; $a_n = \dfrac{1}{\sqrt{n + 1} + \sqrt{n}}$ est positive, décroissante et tend vers $0$. D'après le critère spécial des séries alternées, la série **converge** (semi-convergente, car $a_n \sim \frac{1}{2\sqrt{n}}$).

**6.** On développe à l'ordre $\frac{1}{n^2}$. Le facteur $n$ fait perdre un ordre dans le premier terme, et la variable du cosinus est $\frac{1}{\sqrt{n}}$ :
$$n\ln\left(1 + \frac{1}{n}\right) = n\left(\frac{1}{n} - \frac{1}{2n^2} + \frac{1}{3n^3} + o\left(\frac{1}{n^3}\right)\right) = 1 - \frac{1}{2n} + \frac{1}{3n^2} + o\left(\frac{1}{n^2}\right)$$
$$\cos\frac{1}{\sqrt{n}} = 1 - \frac{1}{2n} + \frac{1}{24n^2} + o\left(\frac{1}{n^2}\right)$$

Donc $u_n = \left(\dfrac{1}{3} - \dfrac{1}{24}\right)\dfrac{1}{n^2} + o\left(\dfrac{1}{n^2}\right) = \dfrac{7}{24n^2} + o\left(\dfrac{1}{n^2}\right) \sim \dfrac{7}{24n^2}$.

Le terme est positif à partir d'un certain rang et équivalent au terme d'une série de Riemann convergente : la série **converge**.

## Exercice 11 : Série harmonique alternée et ln 2

**Énoncé.** On considère la série : $\displaystyle\sum_{n \ge 0} \frac{(-1)^n}{n+1}$

1. Montrer que la série est convergente.
2. Montrer que $\forall n \in \mathbb{N}$ :
$$\sum_{k=0}^n \frac{(-1)^k}{k+1} = \int_0^1 \frac{dt}{1+t} - (-1)^{n+1}\int_0^1 \frac{t^{n+1}}{1+t}\,dt$$
3. Montrer que :
$$\forall n \in \mathbb{N}, \quad 0 \le \int_0^1 \frac{t^{n+1}}{1+t}\,dt \le \frac{1}{n+2}$$
4. En déduire que :
$$\sum_{n=0}^{+\infty} \frac{(-1)^n}{n+1} = \ln 2$$
5. Donner une valeur approchée de $\ln 2$ à la précision $10^{-3}$.

**Correction.**

**1.** La série est alternée et $\left(\frac{1}{n+1}\right)_{n \in \mathbb{N}}$ est décroissante de limite nulle : d'après le critère spécial des séries alternées, elle converge.

**2.** Soit $n \in \mathbb{N}$. Pour $t \in [0, 1]$, la somme géométrique de raison $-t \ne 1$ donne
$$\sum_{k=0}^n (-t)^k = \frac{1 - (-t)^{n+1}}{1 + t} = \frac{1}{1+t} - (-1)^{n+1}\frac{t^{n+1}}{1+t}$$

On intègre sur $[0, 1]$ : $\displaystyle\int_0^1 (-1)^k t^k\,dt = \frac{(-1)^k}{k+1}$, d'où
$$\sum_{k=0}^n \frac{(-1)^k}{k+1} = \int_0^1 \frac{dt}{1+t} - (-1)^{n+1}\int_0^1 \frac{t^{n+1}}{1+t}\,dt$$

**3.** Pour $t \in [0, 1]$, $1 + t \ge 1$ donc $0 \le \frac{t^{n+1}}{1+t} \le t^{n+1}$. En intégrant :
$$0 \le \int_0^1 \frac{t^{n+1}}{1+t}\,dt \le \int_0^1 t^{n+1}\,dt = \frac{1}{n+2}$$

**4.** Par encadrement, $\int_0^1 \frac{t^{n+1}}{1+t}\,dt \to 0$. De plus $\int_0^1 \frac{dt}{1+t} = [\ln(1+t)]_0^1 = \ln 2$. En passant à la limite dans l'égalité de la question 2 :
$$\sum_{n=0}^{+\infty} \frac{(-1)^n}{n+1} = \ln 2$$

**5.** D'après les questions 2 et 3,
$$\left|\ln 2 - \sum_{k=0}^n \frac{(-1)^k}{k+1}\right| = \int_0^1 \frac{t^{n+1}}{1+t}\,dt \le \frac{1}{n+2}$$

(c'est aussi la majoration du reste dans le critère des séries alternées). Il suffit donc que $\frac{1}{n+2} \le 10^{-3}$, soit $n \ge 998$ : la somme partielle $\displaystyle\sum_{k=0}^{998} \frac{(-1)^k}{k+1}$ est une valeur approchée de $\ln 2 \approx 0{,}693$ à $10^{-3}$ près.

## Exercice 12 : Produits de Cauchy

**Énoncé.** Montrer la convergence et calculer les sommes des séries de terme général

1. $u_n = \displaystyle\sum_{k=0}^n \frac{1}{(n-k)!\,k!}$
2. $u_n = \displaystyle\sum_{k=0}^n \frac{(-1)^{n-k}}{k!\,2^{n-k}}$

**Correction.** Méthode : reconnaître le **produit de Cauchy** de deux séries absolument convergentes ; il converge (absolument) et sa somme est le produit des sommes.

**1.** Soit $v_n = \frac{1}{n!}$. Par la règle de d'Alembert ($\frac{v_{n+1}}{v_n} = \frac{1}{n+1} \to 0$), $\sum v_n$ converge absolument, et $\sum_{n=0}^{+\infty} \frac{1}{n!} = e$. Or $u_n = \sum_{k=0}^n v_{n-k}v_k$ est le terme général du produit de Cauchy de $\sum v_n$ par elle-même. Donc $\sum u_n$ converge et
$$\sum_{n=0}^{+\infty} \sum_{k=0}^n \frac{1}{(n-k)!\,k!} = e \times e = e^2$$

(On peut aussi remarquer que $u_n = \frac{1}{n!}\sum_{k=0}^n \binom{n}{k} = \frac{2^n}{n!}$, et $\sum \frac{2^n}{n!} = e^2$.)

**2.** Soient $a_n = \frac{1}{n!}$ et $b_n = \frac{(-1)^n}{2^n} = \left(-\frac{1}{2}\right)^n$. $\sum a_n$ converge absolument (somme $e$) et $\sum b_n$ est géométrique de raison $-\frac{1}{2}$, absolument convergente, de somme $\frac{1}{1 + \frac{1}{2}} = \frac{2}{3}$. Or $u_n = \sum_{k=0}^n a_k b_{n-k}$ : c'est le produit de Cauchy. Donc $\sum u_n$ converge et
$$\sum_{n=0}^{+\infty} \sum_{k=0}^n \frac{(-1)^{n-k}}{k!\,2^{n-k}} = e \times \frac{2}{3} = \frac{2e}{3}$$
