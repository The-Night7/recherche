---
source: TD0_2024-2025_Series_P2S1_DMaths.pdf, page 1 (plusieurs questions reprennent le TD0 de 2022/2023, dont le corrigé est TD0-Correction_2022-2023_Series_P2S1_Inconnu.pdf)
transcription: manuelle
corrections: rédigées
---

# Séries — TD0 : rappels, limites et équivalents (2024/2025, corrigé)

## Exercice 1 : Calculs de limites

**Énoncé.** Calculer les limites suivantes :

1. $\displaystyle\lim_{t \to 1} \frac{t^t - 1}{1 - t + \ln(1 + t)}$
2. $\displaystyle\lim_{t \to 1} \frac{\ln(t)}{t - 1}$
3. $\displaystyle\lim_{x \to +\infty} \frac{x^{\sqrt{x}}}{\sqrt{x}^{\,x}}$
4. $\displaystyle\lim_{x \to 0^+} \frac{1}{1 - x^x} + \frac{1}{x\ln(x)}$
5. $\displaystyle\lim_{x \to +\infty} \sqrt{x + \sqrt{x}} - \sqrt{x}$

**Correction.**

> **Complément :** ce document n'a pas de corrigé ; les corrections sont rédigées pour cette transcription.

**1.** Ce n'est pas une forme indéterminée : en $t = 1$, le numérateur vaut $1 - 1 = 0$ et le dénominateur $1 - 1 + \ln 2 = \ln 2 \ne 0$. Par continuité, la limite vaut $\dfrac{0}{\ln 2} = 0$.

> **Note :** l'énoncé est peut-être une coquille pour $1 - t + \ln(t)$ ; on a traité l'énoncé tel qu'il est écrit.

**2.** C'est le taux d'accroissement de $\ln$ en $1$ : $\dfrac{\ln t - \ln 1}{t - 1} \to \ln'(1) = 1$. La limite vaut $1$.

**3.** On passe à l'exponentielle : $x^{\sqrt{x}} = e^{\sqrt{x}\ln x}$ et $\sqrt{x}^{\,x} = e^{\frac{x}{2}\ln x}$, donc
$$\frac{x^{\sqrt{x}}}{\sqrt{x}^{\,x}} = \exp\left(\ln x\left(\sqrt{x} - \frac{x}{2}\right)\right)$$

Or $\sqrt{x} - \frac{x}{2} = -\frac{x}{2}\left(1 - \frac{2}{\sqrt{x}}\right) \to -\infty$ et $\ln x \to +\infty$ : l'exposant tend vers $-\infty$, la limite vaut $0$.

**4.** On pose $u = x\ln x$ ; quand $x \to 0^+$, $u \to 0^-$ (croissances comparées) et $x^x = e^u$. Alors
$$1 - e^u = -u - \frac{u^2}{2} + o(u^2) = -u\left(1 + \frac{u}{2} + o(u)\right)$$

donc
$$\frac{1}{1 - e^u} = -\frac{1}{u}\left(1 - \frac{u}{2} + o(u)\right) = -\frac{1}{u} + \frac{1}{2} + o(1)$$

En ajoutant $\frac{1}{x\ln x} = \frac{1}{u}$, il reste $\frac{1}{2} + o(1)$. La limite vaut $\dfrac{1}{2}$.

**5.** Quantité conjuguée :
$$\sqrt{x + \sqrt{x}} - \sqrt{x} = \frac{\sqrt{x}}{\sqrt{x + \sqrt{x}} + \sqrt{x}} = \frac{1}{\sqrt{1 + \frac{1}{\sqrt{x}}} + 1} \xrightarrow[x \to +\infty]{} \frac{1}{2}$$

## Exercice 2 : Équivalents simples

**Énoncé.** Déterminer des équivalents simples de

1. $x + \sin(x)$ en $0$ puis en $+\infty$.
2. $x - \sin(x)$ en $0$ puis en $+\infty$.
3. $\ln(\tan(x))$ en $0^+$ puis en $\frac{\pi}{4}$.
4. $\dfrac{1}{x} - \dfrac{1}{\tan(x)}$ en $0$.
5. $\sqrt{x^2 + x} - \sqrt[3]{x^3 + 2x^2}$ en $0^+$ puis en $+\infty$.

**Correction.**

> **Complément :** correction rédigée pour cette transcription.

**1.** En $0$ : $\sin x = x + o(x)$, donc $x + \sin x = 2x + o(x) \sim 2x$.
En $+\infty$ : $|\sin x| \le 1$, donc $\frac{\sin x}{x} \to 0$ et $x + \sin x = x\left(1 + \frac{\sin x}{x}\right) \sim x$.

**2.** En $0$ : les termes d'ordre 1 se compensent, il faut l'ordre 3 : $x - \sin x = x - \left(x - \frac{x^3}{6} + o(x^3)\right) = \frac{x^3}{6} + o(x^3)$, donc $x - \sin x \sim \dfrac{x^3}{6}$.
En $+\infty$ : comme au 1, $x - \sin x \sim x$.

**3.** En $0^+$ : $\tan x = x(1 + o(1))$, donc $\ln(\tan x) = \ln x + \ln(1 + o(1)) = \ln x + o(1)$. Comme $\ln x \to -\infty$, le $o(1)$ est négligeable devant $\ln x$ : $\ln(\tan x) \sim \ln x$.

En $\frac{\pi}{4}$ : $\tan\frac{\pi}{4} = 1$ et $\tan' = 1 + \tan^2$ vaut $2$ en $\frac{\pi}{4}$, donc $\tan x = 1 + 2\left(x - \frac{\pi}{4}\right) + o\left(x - \frac{\pi}{4}\right)$. Avec $\ln(1 + h) \sim h$ :
$$\ln(\tan x) \underset{\pi/4}{\sim} 2\left(x - \frac{\pi}{4}\right)$$

**4.** $\tan x = x + \frac{x^3}{3} + o(x^3)$, donc
$$\frac{1}{\tan x} = \frac{1}{x}\cdot\frac{1}{1 + \frac{x^2}{3} + o(x^2)} = \frac{1}{x}\left(1 - \frac{x^2}{3} + o(x^2)\right) = \frac{1}{x} - \frac{x}{3} + o(x)$$

Ainsi $\dfrac{1}{x} - \dfrac{1}{\tan x} = \dfrac{x}{3} + o(x) \sim \dfrac{x}{3}$.

**5.** En $0^+$ : $\sqrt{x^2 + x} = \sqrt{x}\sqrt{1 + x} \sim x^{1/2}$ et $\sqrt[3]{x^3 + 2x^2} = x^{2/3}(2 + x)^{1/3} \sim 2^{1/3}x^{2/3}$. Comme $\frac{x^{2/3}}{x^{1/2}} = x^{1/6} \to 0$, le second terme est négligeable devant le premier :
$$\sqrt{x^2 + x} - \sqrt[3]{x^3 + 2x^2} \underset{0^+}{\sim} \sqrt{x}$$

En $+\infty$ : les deux termes sont équivalents à $x$, il faut développer. Avec $(1 + h)^{\alpha} = 1 + \alpha h + o(h)$ :

- $\sqrt{x^2 + x} = x\left(1 + \frac{1}{x}\right)^{1/2} = x\left(1 + \frac{1}{2x} + o\left(\frac{1}{x}\right)\right) = x + \frac{1}{2} + o(1)$ ;
- $\sqrt[3]{x^3 + 2x^2} = x\left(1 + \frac{2}{x}\right)^{1/3} = x\left(1 + \frac{2}{3x} + o\left(\frac{1}{x}\right)\right) = x + \frac{2}{3} + o(1)$.

La différence vaut $\frac{1}{2} - \frac{2}{3} + o(1) = -\frac{1}{6} + o(1)$ : elle est équivalente à la constante $-\dfrac{1}{6}$.

## Exercice 3 : Équivalents en 0

**Énoncé.** Déterminer des équivalents en $0$ de

1. $f_1 : x \mapsto \dfrac{\ln(1 + x^2)}{x\arctan(x)}$
2. $f_2 : x \mapsto \dfrac{1 - \operatorname{ch}(x)}{1 - \cos(x)}$
3. $f_3 : x \mapsto \dfrac{e^x - \cos(x) - x}{x - \ln(1 + x)}$
4. $f_4 : x \mapsto \dfrac{\sin^2(x) - x\ln(1 + x)}{e^x + \cos(x) - \sin(x) - 2}$

**Correction.**

> **Complément :** correction rédigée pour cette transcription.

Dans les quatre cas, le quotient a une limite finie non nulle $\ell$ en $0$, et l'équivalent cherché est la constante $\ell$.

**1.** $\ln(1 + x^2) \sim x^2$ et $\arctan x \sim x$, donc $f_1(x) \sim \dfrac{x^2}{x^2} = 1$ : $f_1(x) \underset{0}{\sim} 1$.

**2.** $1 - \operatorname{ch} x = -\frac{x^2}{2} + o(x^2)$ et $1 - \cos x = \frac{x^2}{2} + o(x^2)$, donc $f_2(x) \underset{0}{\sim} -1$.

**3.** À l'ordre 2 :

- numérateur : $\left(1 + x + \frac{x^2}{2}\right) - \left(1 - \frac{x^2}{2}\right) - x + o(x^2) = x^2 + o(x^2)$ ;
- dénominateur : $x - \left(x - \frac{x^2}{2}\right) + o(x^2) = \frac{x^2}{2} + o(x^2)$.

Donc $f_3(x) \sim \dfrac{x^2}{x^2/2}$, soit $f_3(x) \underset{0}{\sim} 2$.

**4.** Il faut aller à l'ordre 3 (les ordres inférieurs s'annulent).

- $\sin^2 x = \left(x - \frac{x^3}{6} + o(x^3)\right)^2 = x^2 + o(x^3)$ et $x\ln(1 + x) = x\left(x - \frac{x^2}{2} + o(x^2)\right) = x^2 - \frac{x^3}{2} + o(x^3)$, donc le numérateur vaut $\frac{x^3}{2} + o(x^3)$.
- $e^x + \cos x - \sin x - 2 = \left(1 + x + \frac{x^2}{2} + \frac{x^3}{6}\right) + \left(1 - \frac{x^2}{2}\right) - \left(x - \frac{x^3}{6}\right) - 2 + o(x^3) = \frac{x^3}{3} + o(x^3)$.

Donc $f_4(x) \sim \dfrac{x^3/2}{x^3/3}$, soit $f_4(x) \underset{0}{\sim} \dfrac{3}{2}$.

## Exercice 4 : Équivalents de suites en +∞

**Énoncé.** Déterminer des équivalents en $+\infty$ de :

1. $u_n = \dfrac{e^{1/n} - \cos\left(\frac{1}{n}\right)}{1 - \sqrt{1 - \frac{1}{n^2}}}$
2. $u_n = \dfrac{1}{\sqrt{n}} - \sqrt{n}\sin\left(\dfrac{1}{n}\right)$
3. $u_n = \dfrac{\ln\left(\cos\left(\frac{a}{n}\right)\right)}{\ln\left(\cos\left(\frac{b}{n}\right)\right)}$, $a, b \in \mathbb{R}^*$
4. $u_n = e^{1/n} - e^{1/(n+1)}$
5. $u_n = \dfrac{\ln\left(\frac{n+1}{n+2}\right)}{\sin\left(\frac{n+1}{n^2+2}\right)}$
6. $u_n = e\sqrt{n^2 - n + 1} - n\left(1 + \dfrac{1}{n}\right)^n$

**Correction.**

> **Complément :** correction rédigée pour cette transcription (les questions 1, 2 et 4 sont les fonctions $f_3$, $f_4$, $f_5$ de l'exercice 3 du TD0 de 2022/2023).

**1.** Avec $h = \frac{1}{n} \to 0$ : le numérateur vaut $e^h - \cos h = h + h^2 + o(h^2) \sim h$ et le dénominateur $1 - \sqrt{1 - h^2} = \frac{h^2}{2} + o(h^2)$. Donc $u_n \sim \frac{2}{h}$ : $u_n \sim 2n$.

**2.** $\sin\frac{1}{n} = \frac{1}{n} - \frac{1}{6n^3} + o\left(\frac{1}{n^3}\right)$, donc
$$u_n = \frac{1}{\sqrt{n}} - \frac{1}{\sqrt{n}} + \frac{1}{6n^{5/2}} + o\left(\frac{1}{n^{5/2}}\right) \sim \frac{1}{6n^{5/2}}$$

**3.** Comme $\frac{a}{n} \to 0$, $\cos\frac{a}{n} = 1 - \frac{a^2}{2n^2} + o\left(\frac{1}{n^2}\right)$ et $\ln(1 + y) \sim y$ donne $\ln\cos\frac{a}{n} \sim -\frac{a^2}{2n^2}$ (non nul car $a \ne 0$) ; de même pour $b$. Donc
$$u_n \sim \frac{-a^2/(2n^2)}{-b^2/(2n^2)} = \frac{a^2}{b^2}$$

La suite est équivalente à la constante $\dfrac{a^2}{b^2}$.

**4.** $\frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)}$, donc
$$u_n = e^{\frac{1}{n+1}}\left(e^{\frac{1}{n(n+1)}} - 1\right) \sim 1 \cdot \frac{1}{n(n+1)} \sim \frac{1}{n^2}$$

**5.** $\ln\frac{n+1}{n+2} = \ln\left(1 - \frac{1}{n+2}\right) \sim -\frac{1}{n+2} \sim -\frac{1}{n}$. D'autre part $\frac{n+1}{n^2+2} \to 0$ donc $\sin\frac{n+1}{n^2+2} \sim \frac{n+1}{n^2+2} \sim \frac{1}{n}$. Ainsi $u_n \sim \dfrac{-1/n}{1/n}$ : $u_n \sim -1$.

**6.** Les deux termes sont équivalents à $en$ : il faut des développements à trois termes.

- Racine, avec $h = -\frac{1}{n} + \frac{1}{n^2}$ et $\sqrt{1 + h} = 1 + \frac{h}{2} - \frac{h^2}{8} + O(h^3)$ :
$$\sqrt{n^2 - n + 1} = n\left(1 - \frac{1}{2n} + \frac{1}{2n^2} - \frac{1}{8n^2} + O\left(\frac{1}{n^3}\right)\right) = n - \frac{1}{2} + \frac{3}{8n} + O\left(\frac{1}{n^2}\right)$$
- Puissance : $n\ln\left(1 + \frac{1}{n}\right) = 1 - \frac{1}{2n} + \frac{1}{3n^2} + O\left(\frac{1}{n^3}\right)$, donc
$$\left(1 + \frac{1}{n}\right)^n = e \cdot \exp\left(-\frac{1}{2n} + \frac{1}{3n^2} + O\left(\frac{1}{n^3}\right)\right) = e\left(1 - \frac{1}{2n} + \frac{11}{24n^2} + O\left(\frac{1}{n^3}\right)\right)$$
(le coefficient de $\frac{1}{n^2}$ est $\frac{1}{3} + \frac{1}{2}\cdot\frac{1}{4} = \frac{11}{24}$), puis $n\left(1 + \frac{1}{n}\right)^n = e\left(n - \frac{1}{2} + \frac{11}{24n} + O\left(\frac{1}{n^2}\right)\right)$.

En soustrayant :
$$u_n = e\left(\frac{3}{8} - \frac{11}{24}\right)\frac{1}{n} + O\left(\frac{1}{n^2}\right) = -\frac{e}{12n} + O\left(\frac{1}{n^2}\right)$$

Donc $u_n \sim -\dfrac{e}{12n}$.

## Exercice 5 : Une limite par le logarithme

**Énoncé.** Pour tout $n \ge 2$ on note $u_n = \left(\dfrac{\ln(1 + n)}{\ln(n)}\right)^{n\ln(n)}$.

1. Déterminer un équivalent de $\ln(u_n)$ en $+\infty$.
2. En déduire $\displaystyle\lim_{n \to +\infty} u_n$.

**Correction.**

> **Complément :** correction rédigée pour cette transcription (c'est l'exercice 4 du TD0 de 2022/2023).

**1.** $\ln(1 + n) = \ln n + \ln\left(1 + \frac{1}{n}\right)$, donc
$$\frac{\ln(1 + n)}{\ln n} = 1 + \frac{\ln\left(1 + \frac{1}{n}\right)}{\ln n} = 1 + \frac{1}{n\ln n} + o\left(\frac{1}{n\ln n}\right)$$

Comme $\frac{1}{n\ln n} \to 0$, $\ln(1 + y) \sim y$ donne
$$\ln u_n = n\ln n \cdot \ln\left(\frac{\ln(1 + n)}{\ln n}\right) = n\ln n\left(\frac{1}{n\ln n} + o\left(\frac{1}{n\ln n}\right)\right) = 1 + o(1)$$

Donc $\ln(u_n) \sim 1$.

**2.** $\ln u_n \to 1$, donc par continuité de l'exponentielle $u_n \to e$.
