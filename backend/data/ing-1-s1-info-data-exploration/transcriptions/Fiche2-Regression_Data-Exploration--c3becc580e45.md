---
source: ING 1/S1 INFO/Data-Exploration/Fiche2-Regression_Data-Exploration.pdf
pages: 1
transcription: manuelle
---

# Data exploration — Résumé du cours de régression

## Régression de Y en X

La droite ajustée s'écrit $\widehat y=\widehat a x+\widehat b$, avec

$$\widehat a=\frac{C_{xy}}{S_x^2},\qquad
\widehat b=\overline y-\widehat a\,\overline x.$$

Les moyennes sont

$$\overline x=\frac1n\sum_{i=1}^n x_i,\qquad
\overline y=\frac1n\sum_{i=1}^n y_i.$$

La covariance entre $X$ et $Y$ vaut

$$C_{xy}=\frac1n\sum_{i=1}^n(x_i-\overline x)(y_i-\overline y)
=\frac1n\sum_{i=1}^n x_i y_i-\overline x\,\overline y.$$

La variance de $X$ est

$$S_x^2=\frac1n\sum_{i=1}^n(x_i-\overline x)^2
=\frac1n\sum_{i=1}^n x_i^2-\overline x^{\,2}.$$

## Corrélation et coefficient de détermination

Le coefficient de corrélation est

$$r_{xy}=\frac{C_{xy}}{S_xS_y}\in[-1,1].$$

Le coefficient de détermination est

$$R^2=r_{xy}^2=\frac{S_{\widehat y}^2}{S_y^2}\in[0,1].$$

$S_{\widehat y}^2$ est la variance expliquée, c'est-à-dire la variance des valeurs prédites. $S_y^2$ est la variance totale de $Y$.

## Résidus et décomposition de la variance

Le résidu de l'observation $i$ est $e_i=y_i-\widehat y_i$.

$$S_y^2=S_{\widehat y}^2+S_e^2,$$

soit : variance totale = variance expliquée + variance résiduelle. On en déduit

$$S_{\widehat y}^2=r_{xy}^2S_y^2,\qquad
S_e^2=S_y^2(1-r_{xy}^2),$$

avec

$$S_y^2=\frac1n\sum_{i=1}^n(y_i-\overline y)^2.$$

> **Conditions explicitées :** la pente suppose $S_x^2>0$ ; la corrélation et $R^2$ supposent aussi $S_y^2>0$. Les identités $R^2=r_{xy}^2$ et la décomposition ci-dessus concernent la régression linéaire simple par moindres carrés avec constante.
