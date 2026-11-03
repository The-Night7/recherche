---
source: "PREING2-S1/Analyse-dans-RN/TD-(6-7)-Correction_2024-2025_Analyse-dans-RN_P2S1_KElAmine.pdf"
pages: 11
transcription: manuelle, depuis les pages manuscrites
transcription_date: 2026-10-08
verification: lecture visuelle intégrale des 11 pages manuscrites ; formules, raisonnements et schémas transcrits
---

# Analyse dans Rn — TD 6–7 : continuité uniforme et compacité — Correction (2024–2025)

## Page 1

### TD 6–7 — Correction manuscrite

#### Exercice 3 — la norme est lipschitzienne

Pour $x,y\in E$, l’inégalité triangulaire donne
$$\|x\|=\|x-y+y\|\le\|x-y\|+\|y\|,$$
donc $\|x\|-\|y\|\le\|x-y\|$. De même,
$$\|y\|=\|y-x+x\|\le\|y-x\|+\|x\|,$$
donc $\|y\|-\|x\|\le\|x-y\|$. On utilise le rappel : si $u\le a$ et $-u\le a$, alors $|u|\le a$. Ainsi
$$\big|\|x\|-\|y\|\big|\le\|x-y\|.$$
L’application norme est $1$-lipschitzienne.

## Page 2

#### Exercice 4 — application intégrale

Soit $E=C([0,1],\mathbb R)$, muni de la norme
$$\|f\|_1=\int_0^1|f(t)|\,dt.$$
On définit $\varphi:E\to\mathbb R$ par $\varphi(f)=\int_0^1tf(t)\,dt$. Pour $f,g\in E$,
$$\varphi(f)-\varphi(g)=\int_0^1t(f(t)-g(t))\,dt.$$
Par l’inégalité triangulaire pour l’intégrale et parce que $0\le t\le1$,
$$|\varphi(f)-\varphi(g)|\le\int_0^1t|f(t)-g(t)|\,dt\le\int_0^1|f(t)-g(t)|\,dt=\|f-g\|_1.$$
Donc $\varphi$ est $1$-lipschitzienne.

## Page 3

#### Exercice 5 — 1/3

Soient $(E,\|\cdot\|_E)$ et $(F,\|\cdot\|_F)$ deux espaces vectoriels normés, $D\subset E$ et $f:D\to F$.

**1. Continuité uniforme.**
$$\forall\varepsilon>0,\ \exists\delta>0,\ \forall x,y\in D,\quad\|x-y\|_E\le\delta\implies\|f(x)-f(y)\|_F\le\varepsilon.$$
**2. Négation.**
$$\exists\varepsilon>0,\ \forall\delta>0,\ \exists x,y\in D,\quad\|x-y\|_E\le\delta\quad\text{et}\quad\|f(x)-f(y)\|_F>\varepsilon.$$
**3.** Dans $E=F=\mathbb R$ muni de la valeur absolue, considérons $f(x)=x^2$ sur $[a,b]$, avec $0\le a<b$. Pour $x,y\in[a,b]$,
$$|f(x)-f(y)|=|x-y||x+y|\le|x-y|(|x|+|y|)\le2b|x-y|.$$
Pour $\varepsilon>0$, choisir $\delta=\varepsilon/(2b)$ établit la continuité uniforme.

**Autre méthode.** Le segment $[a,b]$ est compact et la fonction carré est continue ; le théorème de Heine donne la continuité uniforme. Une ligne intermédiaire de cette seconde méthode est barrée dans le manuscrit.

## Page 4

#### Exercice 5 — 2/3

**4.** $f:\mathbb R\to\mathbb R$, $f(x)=x^2$. Remarque : $\mathbb R$ n’est pas compact, car non borné ; cela ne suffit pas, à lui seul, à trancher la continuité uniforme. Pour $\delta>0$, choisissons $n\ge1$ tel que $1/n<\delta$, puis $x=n$, $y=n+1/n$. Alors
$$|x-y|=1/n<\delta,\qquad |f(x)-f(y)|=2+1/n^2>1.$$
Le choix fixe $\varepsilon=1$ prouve que $f$ n’est pas uniformément continue sur $\mathbb R$.

**5.** $f:]0,1]\to\mathbb R$, $f(x)=1/x$. L’intervalle n’est pas fermé dans $\mathbb R$, donc pas compact. Pour $\delta>0$, prendre $n$ tel que $1/n<\delta$, puis $x=1/n$, $y=1/(2n)$. Alors
$$|x-y|=1/(2n)<\delta,\qquad |f(x)-f(y)|=n>1/2.$$
Avec $\varepsilon=1/2$, on obtient la non-continuité uniforme. Le schéma représente la branche positive de l’hyperbole, avec asymptote verticale en zéro.

## Page 5

#### Exercice 5 — 3/3

**6.** $f:\mathbb R_+^*\to\mathbb R$, $f(x)=\ln x$. Le domaine n’est pas fermé dans $\mathbb R$, donc pas compact.

Fixons $\varepsilon=(\ln2)/2>0$. Pour tout $\delta>0$, choisissons $n\ge1$ tel que $1/n<\delta$, puis $x=1/n$, $y=1/(2n)$. Alors
$$|x-y|=1/(2n)<\delta,$$
mais
$$|\ln x-\ln y|=\left|\ln\frac{1/n}{1/(2n)}\right|=\ln2>\varepsilon.$$
Ainsi le logarithme n’est pas uniformément continu sur $\mathbb R_+^*$. La dernière phrase manuscrite dit « montrer la continuité uniforme » ; le choix des quantificateurs et le calcul établissent bien sa négation.

## Page 6

#### Exercice 6 — 1/2

Dans un espace vectoriel normé $(E,\|\cdot\|)$, on définit
$$f:E\to E,\qquad f(x)=\frac{x}{\max(1,\|x\|)}.$$
**1. Cas réel.** Si $E=\mathbb R$ avec la valeur absolue,
$$f(x)=\begin{cases}x,&|x|\le1,\\x/|x|,&|x|>1.\end{cases}$$
Le graphe suit la droite $y=x$ entre $-1$ et $1$, puis les plateaux $-1$ et $1$ à l’extérieur.

**2. Borne.** Si $\|x\|\le1$, $f(x)=x$ et $\|f(x)\|\le1$. Si $\|x\|>1$, $f(x)=x/\|x\|$ et $\|f(x)\|=1$. Donc $\|f(x)\|\le1$ pour tout $x\in E$ ; $f$ est bornée.

## Page 7

#### Exercice 6 — 2/2

**3. Continuité.** On considère
$$D_1=\{x:\|x\|<1\},\quad D_2=\{x:\|x\|>1\},\quad D_0=\{x:\|x\|=1\}.$$
Ces ensembles partitionnent $E$.

- Sur l’ouvert $D_1$, $f(x)=x$, donc $f$ est continue.
- Sur l’ouvert $D_2$, $f(x)=x/\|x\|$, quotient d’applications continues avec dénominateur non nul, donc $f$ est continue.
- Pour $x_0\in D_0$, la limite depuis $D_1\cup D_0$ vaut $x_0=f(x_0)$. Depuis $D_2$, la continuité de la norme donne $x/\|x\|\to x_0/\|x_0\|=x_0=f(x_0)$.

Le raccord est donc continu sur $D_0$, et $f$ est continue sur tout $E$. Les croquis représentent la sphère unité et une approche d’un point de sa frontière depuis les deux régions.

## Page 8

#### Exercice 7 — 1/4

On travaille dans $\mathbb R^2$ muni d’une norme. **Rappel :** dans un espace vectoriel normé de dimension finie, une partie est compacte si et seulement si elle est fermée et bornée.

**1.** $A_1=\{(x,y)\in\mathbb R^2:x^2+y^4=1\}$. L’application $F(x,y)=x^2+y^4-1$ est continue et $A_1=F^{-1}(\{0\})$ ; donc $A_1$ est fermée.

Pour $(x,y)\in A_1$, $x^2\le1$ et $y^4\le1$, donc $|x|\le1$ et $|y|\le1$. Ainsi
$$\|(x,y)\|_\infty=\max(|x|,|y|)\le1.$$
La partie est bornée, donc compacte dans $\mathbb R^2$.

## Page 9

#### Exercice 7 — 2/4

**2.** $A_2=\{(x,y)\in\mathbb R^2:x^2+y^5=1\}$. Comme $F(x,y)=x^2+y^5-1$ est continue, $A_2=F^{-1}(\{0\})$ est fermée.

L’équation s’écrit $y^5=1-x^2$. Si $|x|\le1$, $y=\sqrt[5]{1-x^2}$. Si $|x|>1$, $y=-\sqrt[5]{x^2-1}$. Le dessin représente la courbe passant par $(-1,0)$ et $(1,0)$, positive entre ces abscisses et descendant sous l’axe à l’extérieur.

Pour tout entier $n\ge1$, le point
$$\left(n+1,-\sqrt[5]{(n+1)^2-1}\right)\in A_2$$
a une norme $\|\cdot\|_1$ au moins égale à $n+1>n$. Donc $A_2$ n’est pas bornée, et n’est pas compacte.

## Page 10

#### Exercice 7 — 3/4

**3.** $A_3=\{(x,y)\in\mathbb R^2:x^2+8xy+y^2\le1\}$. L’application $F(x,y)=x^2+8xy+y^2-1$ est continue et
$$A_3=F^{-1}(]-\infty,0]),$$
donc $A_3$ est fermée.

Mais la droite $\Gamma=\{(x,-x):x\in\mathbb R\}$ est incluse dans $A_3$, puisque
$$F(x,-x)=x^2-8x^2+x^2-1=-6x^2-1\le0.$$
Or $\|(x,-x)\|_1=2|x|$ n’est pas bornée. La partie $A_3$ n’est donc pas bornée et n’est pas compacte.

## Page 11

#### Exercice 7 — 4/4

**4.** $A_4=\{(x,y)\in\mathbb R^2:y^2=x(1-2x)\}$. L’application $F(x,y)=y^2-x(1-2x)$ est continue ; son ensemble de zéros $A_4$ est fermé.

Pour $(x,y)\in A_4$, $y^2\ge0$ impose $x(1-2x)\ge0$, donc $0\le x\le1/2$. Le tableau de signes utilise les racines $0$ et $1/2$, avec produit positif entre elles et négatif à l’extérieur.

La dérivée de $x(1-2x)$ vaut $1-4x$, donc son maximum sur $[0,1/2]$ est atteint en $1/4$ et vaut $1/8$. Ainsi
$$|x|\le1/2,\qquad |y|\le\sqrt{1/8}=\frac1{2\sqrt2}.$$
Donc $\|(x,y)\|_\infty\le1/2$ : $A_4$ est bornée. Fermée et bornée en dimension finie, elle est compacte. Le dessin représente une ellipse entre $x=0$ et $x=1/2$, de hauteurs extrêmes $\pm1/(2\sqrt2)$.
