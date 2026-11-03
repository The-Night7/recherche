---
source: ING 2/Semestre 1/Modèle linéaire bis/Régression linéaire multiple/Parametre-Residu.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Modèle linéaire — Paramètres et résidus

## Page 1 — Équations normales

$$X^{\mathsf T}X\widehat\beta=X^{\mathsf T}Y.$$

### Cas $n=p+1$

Le schéma présente une matrice $X$ avec une première colonne de 1 et trois colonnes de variables $V_1,V_2,V_3$, pour quatre observations ; le vecteur des paramètres est $(\beta_0,\beta_1,\beta_2,\beta_3)^{\mathsf T}$.

La source indique « $X$ : matrice carrée, inversible ». Sous cette hypothèse :

$$\begin{aligned}
X^{\mathsf T}X\widehat\beta&=X^{\mathsf T}Y,\\
(X^{\mathsf T})^{-1}X^{\mathsf T}X\widehat\beta&=(X^{\mathsf T})^{-1}X^{\mathsf T}Y,\\
X\widehat\beta&=Y,\\
\widehat\beta&=X^{-1}Y.
\end{aligned}$$

> **Précision mathématique :** une matrice carrée n’est pas nécessairement inversible. Le raisonnement nécessite que $X$ soit de rang $p+1$.

### Cas $n>p+1$

Le schéma représente $n$ lignes et $p+1$ colonnes, dont une colonne de 1. $X$ n’est pas carrée, donc n’a pas d’inverse usuel. La source suppose $X^{\mathsf T}X$ inversible et écrit :

$$\begin{aligned}
X^{\mathsf T}X\widehat\beta&=X^{\mathsf T}Y,\\
(X^{\mathsf T}X)^{-1}(X^{\mathsf T}X)\widehat\beta
&=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y,\\
\widehat\beta&=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y.
\end{aligned}$$

> **Précisions sur la source :** $X^{\mathsf T}X$ est inversible si les colonnes de $X$ sont linéairement indépendantes ; la seule inégalité $n>p+1$ ne suffit pas. Le dernier coefficient du vecteur dessiné est étiqueté $\beta_{p+1}$, alors qu’avec $p+1$ colonnes et une numérotation commençant à 0, il devrait être $\beta_p$.

## Page 2 — Norme du vecteur des résidus

$$\|\varepsilon\|^2=\varepsilon_1^2+\cdots+\varepsilon_n^2.$$

La deuxième page ne contient que cette formule.
