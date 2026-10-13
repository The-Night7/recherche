---
source: ING 2/Semestre 1/Modèle linéaire bis/Régression linéaire simple/Rappel-RLS.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Modèle linéaire — Rappel de régression linéaire simple

## Page 1 — Sommes de carrés

### Somme des carrés totale

$$\begin{aligned}
\mathrm{SCT}&=\sum_{i=1}^n(y_i-\bar y)^2\\
&=\sum_{i=1}^n(y_i^2-2y_i\bar y+\bar y^2)\\
&=\sum y_i^2-2\bar y\sum y_i+\sum\bar y^2\\
&=\sum y_i^2-2n\bar y^2+n\bar y^2\\
&=\sum y_i^2-n\bar y^2=n\operatorname{Var}(Y).
\end{aligned}$$

### Somme des carrés expliquée

$$\mathrm{SCE}=\sum_{i=1}^n(\widehat y_i-\bar y)^2.$$

Comme $\widehat\beta_0=\bar y-\widehat\beta_1\bar x$,

$$\begin{aligned}
\widehat y_i-\bar y
&=\widehat\beta_0+\widehat\beta_1x_i-\bar y\\
&=\bar y-\widehat\beta_1\bar x+\widehat\beta_1x_i-\bar y\\
&=\widehat\beta_1(x_i-\bar x).
\end{aligned}$$

Ainsi,

$$\begin{aligned}
\mathrm{SCE}&=\sum_{i=1}^n\widehat\beta_1^2(x_i-\bar x)^2\\
&=\widehat\beta_1^2\sum_{i=1}^n(x_i-\bar x)^2\\
&=\widehat\beta_1^2\left(\sum x_i^2-n\bar x^2\right)
=\widehat\beta_1^2n\operatorname{Var}(X).
\end{aligned}$$

### Estimation de la variance résiduelle

Le manuscrit note $S$ l’estimateur et écrit pour son carré :

$$S^2=\frac1{n-2}\sum e_i^2-\bar e^2
=\frac1{n-2}\sum(\widehat y_i-y_i)^2
=\frac{\mathrm{SCR}}{n-2},\qquad\bar e=0.$$

> Le terme $\bar e^2$ est barré dans le manuscrit, car la régression comporte une constante et la moyenne des résidus est nulle. Les variances empiriques $\operatorname{Var}(X)$ et $\operatorname{Var}(Y)$ ci-dessus utilisent le diviseur $n$.

## Page 2 — Test de Fisher

Le test est utilisé pour tester globalement la significativité du modèle, ou celle du coefficient de pente $b$ dans la régression simple.

Les hypothèses inscrites sont :

$$H_0:\beta=0\quad(r_{xy}=0),\qquad
H_1:\beta\ne0\quad(r_{xy}\ne0).$$

Une note précise que l’on pourrait tester une autre valeur $b$, mais que seule la valeur 0 est étudiée ici. L’alternative sur la pente est bilatérale.

### Calcul

$$F_{\mathrm{obs}}=\frac{\mathrm{CM}_M}{\mathrm{CM}_R},$$

où $\mathrm{CM}_M$ est le carré moyen du modèle (ou expliqué), et $\mathrm{CM}_R$ le carré moyen résiduel.

La source propose de comparer $F_{\mathrm{obs}}$ à $F_\alpha(p-2;n-p)$, puis indique $F_\alpha(1;n-2)$ pour un modèle simple avec seulement $X$ et $Y$.

> **Erreur de la source :** le premier couple de degrés de liberté n’est pas cohérent avec le cas simple annoncé. Pour une constante et $k$ variables explicatives, le test global utilise $(k,n-k-1)$ ; dans le cas simple, il utilise bien $(1,n-2)$.

La règle écrite est : si $F_{\mathrm{obs}}>F_\alpha(1;n-2)$, « on accepte $H_1$ », les variables sont liées et « le modèle est accepté » ; sinon, « on rejette $H_1$, les variables sont indépendantes ».

> **Rectification de l’interprétation :** au-dessus du seuil, on rejette $H_0$ au niveau choisi. Sinon, on ne rejette pas $H_0$ ; cela ne démontre ni l’indépendance des variables ni la validité ou l’invalidité globale du modèle. L’alternative sur la pente est bilatérale, mais la région de rejet de la statistique $F$ est dans la queue supérieure.
