---
source: TD0-Correction_2022-2023_Series_P2S1_Inconnu.pdf, pages 1 à 14 (correction manuscrite) ; énoncés : TD0_2022-2023_Series_P2S1_DMaths.pdf, pages 1 et 2
transcription: manuelle
---

# Séries — TD0 : comparaison locale des fonctions réelles (2022/2023, corrigé)

## Exercice 1 : Convergence de suites

**Énoncé.** Étudier la convergence des suites numériques suivantes, de terme général $u_n$ :

1. $u_n = \sqrt{n+1} - \sqrt{n}$
2. $u_n = \left(1 + \dfrac{1}{n}\right)^n$
3. $u_n = \sqrt{n}\, e^{-\sqrt{\ln(n)}}$
4. $u_n = \dfrac{\sin(n^2)}{n}$
5. $u_n = \dfrac{a^n - b^n}{a^n + b^n}$, $(a, b) \in (\mathbb{R}_+^*)^2$

**Correction.**

**1.** On multiplie par la quantité conjuguée :
$$u_n = \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}} \xrightarrow[n \to +\infty]{} 0$$

La suite converge vers $0$.

**2.** On passe à la forme exponentielle : $u_n = e^{n \ln(1 + 1/n)}$. Comme $\ln(1 + h) = h + o(h)$ quand $h \to 0$,
$$n \ln\left(1 + \frac{1}{n}\right) = n\left(\frac{1}{n} + o\left(\frac{1}{n}\right)\right) = 1 + o(1)$$

Par continuité de l'exponentielle, $u_n \to e$.

**3.** On écrit $\sqrt{n} = e^{\frac{1}{2}\ln n}$, donc
$$u_n = \exp\left(\frac{1}{2}\ln n - \sqrt{\ln n}\right) = \exp\left(\ln n \left(\frac{1}{2} - \frac{1}{\sqrt{\ln n}}\right)\right)$$

Quand $n \to +\infty$, $\ln n \to +\infty$ et $\frac{1}{2} - \frac{1}{\sqrt{\ln n}} \to \frac{1}{2}$ : l'exposant tend vers $+\infty$, donc $u_n \to +\infty$. La suite diverge.

**4.** Pour tout $n \ge 1$, $|u_n| \le \dfrac{1}{n} \to 0$, donc $u_n \to 0$.

**5.** On distingue trois cas.

- *Cas $a < b$.* On factorise par $b^n$ :
$$u_n = \frac{\left(\frac{a}{b}\right)^n - 1}{\left(\frac{a}{b}\right)^n + 1}$$
Comme $0 < \frac{a}{b} < 1$, $\left(\frac{a}{b}\right)^n \to 0$ et $u_n \to -1$.
- *Cas $a > b$.* On factorise par $a^n$ :
$$u_n = \frac{1 - \left(\frac{b}{a}\right)^n}{1 + \left(\frac{b}{a}\right)^n} \xrightarrow[n \to +\infty]{} 1$$
car $0 < \frac{b}{a} < 1$.
- *Cas $a = b$.* $u_n = 0$ pour tout $n$, donc $u_n \to 0$.

Dans tous les cas la suite converge : vers $-1$ si $a < b$, vers $0$ si $a = b$, vers $1$ si $a > b$.

## Exercice 2 : Équivalents de suites

**Énoncé.** Donner des équivalents simples lorsque $n$ tend vers $+\infty$ pour les suites numériques suivantes, de terme général $u_n$ :

1. $u_n = \left(\ln(1 + e^{-n^2})\right)^{\frac{1}{n}}$
2. $u_n = \left(\dfrac{e^n}{1 + e^{-n}}\right)^n$

**Correction.**

**1.** On pose $h_n = e^{-n^2} \to 0$. Alors $\ln(1 + h_n) = h_n(1 + o(1))$, donc
$$\ln\big(\ln(1 + h_n)\big) = \ln h_n + \ln(1 + o(1)) = -n^2 + o(1)$$

On en déduit
$$u_n = \exp\left(\frac{1}{n}\ln\big(\ln(1 + e^{-n^2})\big)\right) = \exp\left(-n + o\left(\frac{1}{n}\right)\right) = e^{-n}\, e^{o(1/n)}$$

Comme $e^{o(1/n)} \to 1$ : $u_n \underset{+\infty}{\sim} e^{-n}$.

**2.** On sépare le facteur dominant :
$$u_n = \frac{e^{n^2}}{(1 + e^{-n})^n} = e^{n^2} \exp\big(-n \ln(1 + e^{-n})\big)$$

Or $\ln(1 + e^{-n}) \sim e^{-n}$, donc $n \ln(1 + e^{-n}) \sim n e^{-n} \to 0$ (croissances comparées). Ainsi $\exp\big(-n \ln(1 + e^{-n})\big) \to 1$ et
$$u_n \underset{+\infty}{\sim} e^{n^2}$$

> **Erreur corrigée :** la correction manuscrite concluait par l'égalité $u_n = e^{n^2}$ ; il s'agit seulement d'un équivalent, le facteur $(1 + e^{-n})^{-n}$ n'étant pas égal à $1$ (il tend vers $1$).

## Exercice 3 : Équivalents de fonctions en +∞

**Énoncé.** Déterminer un équivalent au voisinage de $+\infty$ des fonctions suivantes :

1. $f_1(x) = \sqrt{x^3 + x^{5/2}} - x^{3/2}$
2. $f_2(x) = \dfrac{\sqrt{x^4 + 1} - \sqrt{x^4 - 1}}{\sqrt{x^2 + 1} - \sqrt{x^2 - 1}}$
3. $f_3(x) = \dfrac{e^{1/x} - \cos\frac{1}{x}}{1 - \sqrt{1 - \frac{1}{x^2}}}$
4. $f_4(x) = \dfrac{1}{\sqrt{x}} - \sqrt{x}\,\sin\dfrac{1}{x}$
5. $f_5(x) = e^{1/x} - e^{1/(x+1)}$

**Correction.**

**1.** On factorise par $x^{3/2}$ et on utilise $\sqrt{1 + h} = 1 + \frac{h}{2} + o(h)$ avec $h = x^{-1/2} \to 0$ :
$$f_1(x) = x^{3/2}\left(\sqrt{1 + x^{-1/2}} - 1\right) = x^{3/2}\left(\frac{1}{2}x^{-1/2} + o(x^{-1/2})\right) = \frac{x}{2} + o(x)$$

Donc $f_1(x) \underset{+\infty}{\sim} \dfrac{x}{2}$.

**2.** On multiplie numérateur et dénominateur par leurs quantités conjuguées : $\sqrt{x^4 + 1} - \sqrt{x^4 - 1} = \dfrac{2}{\sqrt{x^4 + 1} + \sqrt{x^4 - 1}}$ et de même pour le dénominateur, d'où
$$f_2(x) = \frac{\sqrt{x^2 + 1} + \sqrt{x^2 - 1}}{\sqrt{x^4 + 1} + \sqrt{x^4 - 1}} = \frac{x\left(\sqrt{1 + \frac{1}{x^2}} + \sqrt{1 - \frac{1}{x^2}}\right)}{x^2\left(\sqrt{1 + \frac{1}{x^4}} + \sqrt{1 - \frac{1}{x^4}}\right)}$$

Les deux parenthèses tendent vers $2$, donc $f_2(x) \underset{+\infty}{\sim} \dfrac{x}{x^2} = \dfrac{1}{x}$.

**3.** On pose $h = \frac{1}{x} \to 0$ et on fait un développement limité à l'ordre 2 :

- numérateur : $e^h - \cos h = \left(1 + h + \frac{h^2}{2}\right) - \left(1 - \frac{h^2}{2}\right) + o(h^2) = h + h^2 + o(h^2) \sim h$ ;
- dénominateur : $1 - \sqrt{1 - h^2} = 1 - \left(1 - \frac{h^2}{2} + o(h^2)\right) = \frac{h^2}{2} + o(h^2) \sim \frac{h^2}{2}$.

Donc $f_3(x) \sim \dfrac{h}{h^2/2} = \dfrac{2}{h}$, soit $f_3(x) \underset{+\infty}{\sim} 2x$.

> **Erreur corrigée :** la correction manuscrite écrivait le numérateur $\frac{1}{x} + o\left(\frac{1}{x^2}\right)$, en oubliant le terme $\frac{1}{x^2}$ ; il faut écrire $\frac{1}{x} + \frac{1}{x^2} + o\left(\frac{1}{x^2}\right)$ (ou simplement $\frac{1}{x} + o\left(\frac{1}{x}\right)$). L'équivalent $2x$ n'est pas affecté.

**4.** Avec $\sin u = u - \frac{u^3}{6} + o(u^3)$ et $u = \frac{1}{x}$ :
$$f_4(x) = \frac{1}{\sqrt{x}} - \sqrt{x}\left(\frac{1}{x} - \frac{1}{6x^3} + o\left(\frac{1}{x^3}\right)\right) = \frac{1}{6x^{5/2}} + o\left(\frac{1}{x^{5/2}}\right)$$

Donc $f_4(x) \underset{+\infty}{\sim} \dfrac{1}{6x^{5/2}}$. Il fallait aller jusqu'à l'ordre 3 car les termes d'ordre 1 se compensent.

**5.** On factorise par $e^{1/(x+1)}$ :
$$f_5(x) = e^{\frac{1}{x+1}}\left(e^{\frac{1}{x} - \frac{1}{x+1}} - 1\right) = e^{\frac{1}{x+1}}\left(e^{\frac{1}{x(x+1)}} - 1\right)$$

Comme $\frac{1}{x(x+1)} \to 0$, $e^{\frac{1}{x(x+1)}} - 1 \sim \frac{1}{x(x+1)} \sim \frac{1}{x^2}$, et $e^{\frac{1}{x+1}} \to 1$. Donc
$$f_5(x) \underset{+\infty}{\sim} \frac{1}{x^2}$$

> **Note :** la correction manuscrite obtient d'abord $f_5(x) \sim \frac{e^{1/x}}{x^2}$ (correct, mais pas « simple »), puis remarque que $\frac{e^{1/x}}{x^2} \sim \frac{1}{x^2}$.

## Exercice 4 : Une limite par le logarithme

**Énoncé.** Soit $f(x) = \left[\dfrac{\ln(1 + x)}{\ln(x)}\right]^{x \ln(x)}$.

1. Déterminer un équivalent de $\ln(f(x))$ en $+\infty$.
2. En déduire $\displaystyle\lim_{x \to +\infty} f(x)$.

**Correction.**

**1.** Pour $x > 1$, $\ln f(x) = x \ln x \cdot \ln\left(\dfrac{\ln(1 + x)}{\ln x}\right)$. On écrit $\ln(1 + x) = \ln x + \ln\left(1 + \frac{1}{x}\right)$, donc
$$\frac{\ln(1 + x)}{\ln x} = 1 + \frac{\ln\left(1 + \frac{1}{x}\right)}{\ln x} = 1 + \frac{1}{x \ln x} + o\left(\frac{1}{x \ln x}\right)$$

La quantité $\frac{1}{x \ln x}$ tend vers $0$, donc $\ln(1 + y) \sim y$ donne
$$\ln f(x) = x \ln x\left(\frac{1}{x \ln x} + o\left(\frac{1}{x \ln x}\right)\right) = 1 + o(1)$$

Ainsi $\ln f(x) \underset{+\infty}{\sim} 1$.

**2.** $\ln f(x) \to 1$, donc par continuité de l'exponentielle $\displaystyle\lim_{x \to +\infty} f(x) = e$.

## Exercice 5 : Calculs de limites

**Énoncé.** Calculer les limites suivantes :

1. $\displaystyle\lim_{x \to 0} \frac{4\sin^3(x) + x - 4(\cos x - 1)}{3x^2 + e^x - 1}$
2. $\displaystyle\lim_{x \to 0} \frac{(1 - e^x)\sin x}{e^x - \operatorname{ch} x}$
3. $\displaystyle\lim_{x \to 1} \frac{x^x - 1}{1 - x + \ln(1 + x)}$
4. $\displaystyle\lim_{x \to +\infty} \sqrt{x + \sqrt{x}} - \sqrt{x}$
5. $\displaystyle\lim_{x \to +\infty} \frac{(x^x)^x}{x^{(x^x)}}$
6. $\displaystyle\lim_{x \to +\infty} \left(\cos\left(\frac{1}{x}\right)\right)^{x^2}$
7. $\displaystyle\lim_{x \to 1} \frac{\sqrt[3]{2x - x^3} - \sqrt{x}}{1 - x^{3/4}}$
8. $\displaystyle\lim_{x \to 0} \left(\frac{x}{\sin x}\right)^{\frac{\sin x}{x - \sin x}}$
9. $\displaystyle\lim_{x \to 0} \left(\frac{a^x + b^x}{2}\right)^{\frac{1}{x}}$
10. $\displaystyle\lim_{x \to 0} \frac{(1 - \cos x)(1 + 2x)}{x^2 - x^4}$
11. $\displaystyle\lim_{x \to +\infty} \sqrt{4x + 1}\,\ln\left(1 - \frac{\sqrt{x + 1}}{x + 2}\right)$
12. $\displaystyle\lim_{x \to 0} x(3 + x)\frac{\sqrt{3 + x}}{\sqrt{x}\sin(\sqrt{x})}$
13. $\displaystyle\lim_{x \to 0} \exp\left(\frac{1}{x^2}\right) - \exp\left(\frac{1}{(x + 1)^2}\right)$

**Correction.**

**1.** Développements limités en $0$ : $4\sin^3 x = 4x^3 + o(x^3)$, $-4(\cos x - 1) = 2x^2 + o(x^3)$ et $e^x - 1 = x + \frac{x^2}{2} + o(x^2)$. Donc
$$\frac{x + 2x^2 + o(x^2)}{x + \frac{7}{2}x^2 + o(x^2)} = \frac{1 + 2x + o(x)}{1 + \frac{7}{2}x + o(x)} \xrightarrow[x \to 0]{} 1$$

La limite vaut $1$ (le numérateur et le dénominateur sont tous deux équivalents à $x$).

**2.** Numérateur : $(1 - e^x)\sin x = (-x + o(x))(x + o(x)) = -x^2 + o(x^2)$. Dénominateur : $e^x - \operatorname{ch} x = \operatorname{sh} x = x + o(x)$. Le quotient est équivalent à $\frac{-x^2}{x} = -x$ : la limite vaut $0$.

**3.** Ce n'est pas une forme indéterminée : en $x = 1$, le numérateur vaut $1^1 - 1 = 0$ et le dénominateur vaut $1 - 1 + \ln 2 = \ln 2 \ne 0$. Par continuité, la limite vaut $\dfrac{0}{\ln 2} = 0$.

**4.** Quantité conjuguée :
$$\sqrt{x + \sqrt{x}} - \sqrt{x} = \frac{\sqrt{x}}{\sqrt{x + \sqrt{x}} + \sqrt{x}} = \frac{1}{\sqrt{1 + \frac{1}{\sqrt{x}}} + 1} \xrightarrow[x \to +\infty]{} \frac{1}{2}$$

**5.** $(x^x)^x = e^{x^2 \ln x}$ et $x^{(x^x)} = e^{x^x \ln x}$, donc le quotient vaut
$$\exp\big((x^2 - x^x)\ln x\big) = \exp\left(x^2\left(1 - e^{(x - 2)\ln x}\right)\ln x\right)$$

Quand $x \to +\infty$, $(x - 2)\ln x \to +\infty$, donc $1 - e^{(x-2)\ln x} \to -\infty$ ; l'exposant tend vers $-\infty$ et la limite vaut $0$.

**6.** $\left(\cos\frac{1}{x}\right)^{x^2} = \exp\left(x^2 \ln\cos\frac{1}{x}\right)$ et $\ln\cos\frac{1}{x} = \ln\left(1 - \frac{1}{2x^2} + o\left(\frac{1}{x^2}\right)\right) = -\frac{1}{2x^2} + o\left(\frac{1}{x^2}\right)$. L'exposant tend vers $-\frac{1}{2}$, donc la limite vaut $e^{-1/2} = \dfrac{1}{\sqrt{e}}$.

**7.** On pose $y = 1 - x \to 0$, soit $x = 1 - y$. Alors
$$2x - x^3 = 2(1 - y) - (1 - y)^3 = 1 + y - 3y^2 + y^3$$

Un développement à l'ordre 1 suffit :

- $\sqrt[3]{1 + y - 3y^2 + y^3} = 1 + \frac{y}{3} + o(y)$ ;
- $\sqrt{x} = (1 - y)^{1/2} = 1 - \frac{y}{2} + o(y)$ ;
- $x^{3/4} = (1 - y)^{3/4} = 1 - \frac{3}{4}y + o(y)$.

Donc
$$\frac{\sqrt[3]{2x - x^3} - \sqrt{x}}{1 - x^{3/4}} = \frac{\frac{5}{6}y + o(y)}{\frac{3}{4}y + o(y)} \xrightarrow[y \to 0]{} \frac{5}{6} \times \frac{4}{3} = \frac{10}{9}$$

> **Erreur corrigée :** la correction manuscrite poussait les développements à l'ordre 3 avec des coefficients faux (par exemple $\frac{5}{243}$ au lieu de $\frac{5}{81}$ pour le terme en $Y^3$ de $(1 + Y)^{1/3}$, et $\frac{5}{344}$ au lieu de $\frac{5}{128}$ pour celui de $(1 - y)^{3/4}$). Ces termes ne servent pas : l'ordre 1 suffit, et la limite $\frac{10}{9}$ est juste.

**8.** On passe à l'exponentielle : la quantité vaut $\exp\left(\dfrac{\sin x}{x - \sin x}\ln\dfrac{x}{\sin x}\right)$. En $0$ :

- $\sin x \sim x$ ;
- $x - \sin x = \frac{x^3}{6} + o(x^3) \sim \frac{x^3}{6}$ ;
- $\ln\dfrac{x}{\sin x} = -\ln\dfrac{\sin x}{x} = -\ln\left(1 - \frac{x^2}{6} + o(x^2)\right) \sim \dfrac{x^2}{6}$.

L'exposant est donc équivalent à $\dfrac{x \cdot \frac{x^2}{6}}{\frac{x^3}{6}} = 1$ : il tend vers $1$, et la limite vaut $e$.

**9.** On suppose $a, b > 0$. On écrit $a^x = e^{x \ln a} = 1 + x \ln a + o(x)$, de même pour $b^x$, d'où
$$\frac{1}{x}\ln\left(\frac{a^x + b^x}{2}\right) = \frac{1}{x}\ln\left(1 + x\,\frac{\ln a + \ln b}{2} + o(x)\right) = \frac{\ln a + \ln b}{2} + o(1)$$

La limite vaut $e^{\frac{\ln a + \ln b}{2}} = e^{\ln\sqrt{ab}} = \sqrt{ab}$.

**10.** $1 - \cos x \sim \frac{x^2}{2}$, $1 + 2x \to 1$ et $x^2 - x^4 \sim x^2$. Le quotient est équivalent à $\frac{x^2/2}{x^2}$ : la limite vaut $\dfrac{1}{2}$.

**11.** $t = \dfrac{\sqrt{x + 1}}{x + 2} \to 0$, donc $\ln(1 - t) \sim -t$ et
$$\sqrt{4x + 1}\,\ln\left(1 - \frac{\sqrt{x + 1}}{x + 2}\right) \underset{+\infty}{\sim} -\frac{\sqrt{4x + 1}\sqrt{x + 1}}{x + 2} \underset{+\infty}{\sim} -\frac{2\sqrt{x}\sqrt{x}}{x} = -2$$

La limite vaut $-2$.

> **Erreur corrigée :** la correction manuscrite écrivait bien $\ln(1 - t) \sim -t$, puis perdait le signe moins à la ligne suivante et concluait que la limite vaut $2$. La bonne valeur est $-2$ (le logarithme d'un nombre $< 1$ est négatif).

**12.** Quand $x \to 0^+$, $\sin\sqrt{x} \sim \sqrt{x}$, donc $\sqrt{x}\sin\sqrt{x} \sim x$, et $(3 + x)\sqrt{3 + x} \to 3\sqrt{3}$. Donc
$$x(3 + x)\frac{\sqrt{3 + x}}{\sqrt{x}\sin(\sqrt{x})} \sim \frac{3\sqrt{3}\,x}{x} \xrightarrow[x \to 0^+]{} 3\sqrt{3}$$

**13.** Quand $x \to 0$, $\exp\left(\frac{1}{x^2}\right) \to +\infty$ tandis que $\exp\left(\frac{1}{(x + 1)^2}\right) \to e^1 = e$. La différence tend donc vers $+\infty$ (ce n'est pas une forme indéterminée).

> **Note :** la correction manuscrite factorise par $e^{1/x^2}$ et montre que le facteur $1 - \exp\left(\frac{1}{(x+1)^2} - \frac{1}{x^2}\right)$ tend vers $1$ ; elle aboutit au même résultat, $+\infty$.

## Exercice 6 : Comparaison de fonctions

**Énoncé.** Comparer les fonctions suivantes au voisinage des points indiqués :

1. $\cos(x) - 1$ et $\sin(x)$ au voisinage de $0$
2. $x \ln x$ et $\ln(1 + 2x)$ au voisinage de $0$
3. $x^{\ln(x)}$ et $(\ln x)^x$ au voisinage de $+\infty$
4. $x \ln(x)$ et $\sqrt{x^2 + 3x}\,\ln(x^2)\sin(x)$ au voisinage de $+\infty$

**Correction.** Méthode : on étudie la limite du quotient (ou on le majore).

**1.** $\cos x - 1 \sim -\frac{x^2}{2}$ et $\sin x \sim x$, donc $\dfrac{\cos x - 1}{\sin x} \sim -\dfrac{x}{2} \to 0$. Ainsi $\cos x - 1 \underset{0}{=} o(\sin x)$.

**2.** $\ln(1 + 2x) \sim 2x$, donc $\dfrac{\ln(1 + 2x)}{x \ln x} \sim \dfrac{2}{\ln x} \xrightarrow[x \to 0^+]{} 0$. Ainsi $\ln(1 + 2x) \underset{0}{=} o(x \ln x)$.

**3.** $x^{\ln x} = e^{(\ln x)^2}$ et $(\ln x)^x = e^{x \ln(\ln x)}$. Avec $X = \ln x \to +\infty$ ($x = e^X$), le quotient vaut
$$\frac{x^{\ln x}}{(\ln x)^x} = \exp\big(X^2 - e^X \ln X\big) = \exp\left(-e^X \ln X\left(1 - \frac{X^2}{e^X \ln X}\right)\right)$$

Par croissances comparées $\frac{X^2}{e^X \ln X} \to 0$, donc l'exposant tend vers $-\infty$ et le quotient vers $0$ : $x^{\ln x} \underset{+\infty}{=} o\big((\ln x)^x\big)$.

**4.** Pour $x \ge 1$, $\ln(x^2) = 2\ln x$ et $\sqrt{x^2 + 3x} = x\sqrt{1 + \frac{3}{x}} \le 2x$ (car $1 + \frac{3}{x} \le 4$). Donc, pour $x > 1$,
$$\left|\frac{\sqrt{x^2 + 3x}\,\ln(x^2)\sin x}{x \ln x}\right| = 2\sqrt{1 + \frac{3}{x}}\,|\sin x| \le 4$$

Ainsi $\sqrt{x^2 + 3x}\,\ln(x^2)\sin(x) \underset{+\infty}{=} O(x \ln x)$. On ne peut pas dire mieux : le quotient vaut $2\sqrt{1 + 3/x}\sin x$, qui n'a pas de limite (il n'y a ni $o$ ni équivalence).

## Exercice 7 : Négligeabilité et exponentielle

**Énoncé.** Soit $f, g : \mathbb{R} \to \mathbb{R}$. On suppose que $\displaystyle\lim_{x \to +\infty} f(x) = +\infty$.

1. On suppose que $g \underset{+\infty}{=} o(f)$. Montrer que $\exp(g) \underset{+\infty}{=} o(\exp(f))$.
2. Montrer que la réciproque est fausse.
3. Application : comparer $f(x) = (\ln(\ln x))^{x^{\ln x}}$ et $g(x) = (\ln x)^{x^{\ln(\ln(x))}}$ au voisinage de $+\infty$.

**Correction.**

**1.** Par définition, $g \underset{+\infty}{=} o(f)$ signifie qu'il existe une fonction $\varepsilon$ telle que $g(x) = \varepsilon(x) f(x)$ au voisinage de $+\infty$, avec $\varepsilon(x) \to 0$. Alors
$$\frac{\exp(g(x))}{\exp(f(x))} = \exp\big(\varepsilon(x) f(x) - f(x)\big) = \exp\big(f(x)(\varepsilon(x) - 1)\big)$$

Or $f(x) \to +\infty$ et $\varepsilon(x) - 1 \to -1$, donc $f(x)(\varepsilon(x) - 1) \to -\infty$ et le quotient tend vers $0$ : $\exp(g) \underset{+\infty}{=} o(\exp(f))$.

**2.** Contre-exemple : $f(x) = x^2$ et $g(x) = x^2 - x$. On a
$$\frac{e^{g(x)}}{e^{f(x)}} = e^{-x} \xrightarrow[x \to +\infty]{} 0$$
donc $\exp(g) = o(\exp(f))$, mais $\frac{g(x)}{f(x)} = 1 - \frac{1}{x} \to 1$ : $g \sim f$, et $g$ n'est pas négligeable devant $f$.

> **Erreur corrigée :** la correction manuscrite écrivait « donc $\exp(g) = o(\exp(g))$ » ; il faut lire $\exp(g) = o(\exp(f))$.

**3.**

> **Complément :** cette question n'était pas traitée dans la correction manuscrite.

Pour $x > e$, les deux fonctions sont strictement positives et
$$\ln f(x) = x^{\ln x}\,\ln(\ln(\ln x)), \qquad \ln g(x) = x^{\ln(\ln x)}\,\ln(\ln x)$$

On pose $F = \ln f$ et $G = \ln g$ et on compare $G$ à $F$. On écrit $x^{\ln x} = e^{(\ln x)^2}$ et $x^{\ln(\ln x)} = e^{\ln x \cdot \ln(\ln x)}$, donc
$$\frac{G(x)}{F(x)} = \exp\big(\ln x \cdot \ln(\ln x) - (\ln x)^2\big)\,\frac{\ln(\ln x)}{\ln(\ln(\ln x))}$$

Avec $X = \ln x \to +\infty$, l'exposant vaut $X\ln X - X^2 = -X^2\left(1 - \frac{\ln X}{X}\right) \to -\infty$, et le second facteur vaut $\frac{\ln X}{\ln(\ln X)}$. Or
$$\exp\left(-X^2\left(1 - \tfrac{\ln X}{X}\right)\right)\frac{\ln X}{\ln \ln X} \le e^{-X^2/2}\,\ln X \xrightarrow[X \to +\infty]{} 0$$
(pour $X$ assez grand, $1 - \frac{\ln X}{X} \ge \frac{1}{2}$ et $\ln\ln X \ge 1$). Donc $G = o(F)$.

De plus $F(x) = e^{(\ln x)^2}\ln(\ln(\ln x)) \to +\infty$. La question 1 s'applique à $F$ et $G$ : $\exp(G) = o(\exp(F))$, c'est-à-dire
$$g(x) \underset{+\infty}{=} o\big(f(x)\big)$$
