---
source: "PREING2-S2/Ondes-CC/CC1-2021-2022-Correction_Ondes-CC_P2S2_Inconnu.pdf"
pages: 5
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale des cinq pages ; comparaison avec la version ORIGINAL et vérification des équations
---

# Ondes — CC1 2021–2022 — Corrigé

> La source porte le titre « DS I ». Elle contient le corrigé seul, avec une nouvelle rédaction de la question III insérée sur la première page. Les énoncés absents ne sont pas reconstitués.

## Questions courtes — sur 8 (pages 1 et 2)

### I. Pulsation et période [1 pt]

$$
\omega=2\pi f,\qquad f=\frac1\tau
\quad\Longrightarrow\quad
\boxed{\omega=\frac{2\pi}{\tau}}.
$$

### II. Combinaison de solutions [2 pt]

$$
\boxed{X(t)=2X_1(t)+3iX_2(t)}.
$$

### III. Équation différentielle

On pose $f(t)=f(0)e^{-i\omega t}$ dans

$$
\ddot f+3\dot f-4f=0.
$$

Les dérivées sont

$$
\dot f(t)=-i\omega f(0)e^{-i\omega t}=-i\omega f(t),
\qquad
\ddot f(t)=(i\omega)^2f(0)e^{-i\omega t}=(i\omega)^2f(t).
$$

Il vient

$$
f(t)\big[(i\omega)^2-3i\omega-4\big]=0,
\qquad \omega^2+3i\omega+4=0.
$$

Le discriminant est

$$
\Delta=(3i)^2-4\times4=-9-16=-25=(5i)^2.
$$

Ainsi,

$$
\boxed{\omega_1=\frac{-3i-5i}{2}=-4i},\qquad
\boxed{\omega_2=\frac{-3i+5i}{2}=i}.
$$

> Cette rédaction remplace le calcul erroné de la version « ORIGINAL », qui donnait $(-3i\pm\sqrt7)/2$. Aucun barème n’est visible dans l’encart qui remplace la question III.

### IV. Principe de superposition

Soient $F_1,F_2$ deux solutions et $\beta,\gamma\in\mathbb C$.

**a) Oui [1 pt].**

$$
\begin{aligned}
\frac{d^2}{dt^2}(\beta F_1+\gamma F_2)
+\omega^2(\beta F_1+\gamma F_2)
&=\beta(\ddot F_1+\omega^2F_1)
+\gamma(\ddot F_2+\omega^2F_2)\\
&=0.
\end{aligned}
$$

**b) Non [1 pt].** On prend $F(t)=\beta F_1(t)$ :

$$
\begin{aligned}
(\beta F_1)(\beta\ddot F_1)+\alpha(\beta\dot F_1)
&=\beta^2(F_1\ddot F_1)+\beta\alpha\dot F_1\\
&=(\beta-\beta^2)\alpha\dot F_1\ne0
\end{aligned}
$$

en général, puisque $F_1\ddot F_1=-\alpha\dot F_1$.

**c) Oui [1 pt].** Le coefficient dépendant du temps est noté $X(t)$ dans le manuscrit :

$$
\begin{aligned}
&\frac{d^2}{dt^2}(\beta F_1+\gamma F_2)
+\frac d{dt}(\beta F_1+\gamma F_2)
+X(t)(\beta F_1+\gamma F_2)\\
&\qquad=\beta\big(\ddot F_1+\dot F_1+X(t)F_1\big)
+\gamma\big(\ddot F_2+\dot F_2+X(t)F_2\big)=0.
\end{aligned}
$$

## Question longue — sur 12 (pages 3 à 5)

**Schéma.** Une masse $M$ se déplace horizontalement et est reliée au mur de gauche par un ressort de raideur $k$ et de longueur à vide $L_0$. La position $X(t)$ est mesurée depuis le mur ; le vecteur unitaire $\hat u_x$ pointe vers la droite.

### a) Forces [2 pt]

$$
\vec F_{\mathrm{ressort}}=-k(X-L_0)\hat u_x,
\qquad
\vec F_{\mathrm{friction}}=-\mu_c M\dot X\hat u_x.
$$

### b) Équation du mouvement [2 pt]

$$
\vec F_{\mathrm{tot}}=M\vec a=M\ddot X\hat u_x
=-\big[k(X-L_0)+\mu_cM\dot X\big]\hat u_x.
$$

Donc

$$
\ddot X+\mu_c\dot X+\frac{k}{M}X=\frac{kL_0}{M},
$$

ou encore

$$
\boxed{\ddot X+\Gamma\dot X+\omega_0^2X=y},\qquad
\Gamma=\mu_c,\quad \omega_0=\sqrt{\frac{k}{M}},\quad y=\frac{kL_0}{M}.
$$

### c) Pulsations complexes et régime critique [2 pt]

Pour l’équation homogène, on pose $X(t)=X_0e^{-i\lambda t}$ :

$$
\dot X=-i\lambda X,\qquad \ddot X=-\lambda^2X.
$$

L’équation (3) de l’énoncé, citée dans le corrigé, donne

$$
(-\lambda^2-i\lambda\Gamma+\omega_0^2)X=0,
$$

d’où

$$
\boxed{\lambda_\pm=\frac{i\Gamma\pm\sqrt{4\omega_0^2-\Gamma^2}}{-2}}.
$$

Le régime critique correspond à $\boxed{4\omega_0^2=\Gamma^2}$.

### d) Solution générale [2 pt]

La solution générale est la somme de la solution générale du problème homogène ($y=0$) et d’une solution particulière. On choisit la constante $X_p=y/\omega_0^2$, dont les deux dérivées sont nulles :

$$
\ddot X_p+\Gamma\dot X_p+\omega_0^2X_p
=0+0+\omega_0^2\frac y{\omega_0^2}=y.
$$

On obtient

$$
\boxed{X(t)=Ae^{-i\lambda_+t}+Be^{-i\lambda_-t}+\frac y{\omega_0^2}},
$$

avec

$$
\lambda_\pm=-\frac{i\Gamma}{2}\mp\sqrt{\omega_0^2-\frac{\Gamma^2}{4}},
\qquad A,B\in\mathbb C.
$$

Le manuscrit souligne que la quantité sous la racine est positive.

> La forme à deux exponentielles indépendantes s’applique lorsque les racines sont distinctes ; la suite traite le régime pseudo-périodique. Au régime critique, la solution homogène doit prendre la forme $(A+Bt)e^{-\Gamma t/2}$.

### e) Conditions initiales [2 pt]

On impose $X(0)=L_0/2$ et $\dot X(0)=0$. La seconde condition donne

$$
-i\lambda_+A-i\lambda_-B=0,
\qquad \boxed{A=-\frac{\lambda_-}{\lambda_+}B}.
$$

Puis

$$
X(0)=A+B+\frac y{\omega_0^2}
=\frac{\lambda_+-\lambda_-}{\lambda_+}B+\frac y{\omega_0^2}
=\frac{L_0}{2}.
$$

Comme $y/\omega_0^2=L_0$ et

$$
\frac{\lambda_+-\lambda_-}{\lambda_+}
=\frac{2\sqrt{\omega_0^2-\Gamma^2/4}}
{i\Gamma/2+\sqrt{\omega_0^2-\Gamma^2/4}},
$$

il vient

$$
\boxed{B=-\frac{L_0}{4}
\frac{i\mu_c/2+\sqrt{k/M-\mu_c^2/4}}
{\sqrt{k/M-\mu_c^2/4}}}.
$$

**Note de barème de la source :** pour les étudiants n’ayant pas réussi b), on peut donner des points partiels.

> Le titre annonce 12 points pour la question longue, mais les cinq sous-questions visibles sont chacune annotées « 2 ». Aucune sous-question supplémentaire ne figure dans ces cinq pages.
