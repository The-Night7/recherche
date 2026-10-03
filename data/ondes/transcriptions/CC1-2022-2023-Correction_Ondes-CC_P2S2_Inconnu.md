---
source: "PREING2-S2/Ondes-CC/CC1-2022-2023-Correction_Ondes-CC_P2S2_Inconnu.pdf"
pages: 4
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale des quatre pages manuscrites ; forces, signes, solutions et conditions initiales vérifiés
---

# Ondes — CC1 2022–2023 — Corrigé

> Le fichier contient le corrigé seul. Le schéma montre une masse $M$ entre deux ressorts verticaux identiques, de raideur $k$ et de longueur à vide $L_0$, attachés à deux supports fixes séparés de $2L_0$. La hauteur $h(t)$ est mesurée depuis le support inférieur ; le vecteur unitaire $\vec u$ est orienté vers le haut.

## Partie I — Oscillateur sans frottement (pages 1 à 3)

### a) Bilan des forces [2 pt]

Ressort inférieur :

$$
\vec F_1=-k(h(t)-L_0)\vec u.
$$

Ressort supérieur :

$$
\vec F_2=-k[L_0-(2L_0-h)]\vec u
=-k(h(t)-L_0)\vec u.
$$

Poids : $\vec F_g=-Mg\vec u$. Au total,

$$
\vec F_{\mathrm{tot}}=-2k(h(t)-L_0)\vec u-Mg\vec u.
$$

### b) Équation du mouvement [3 pt]

Avec $\vec F_{\mathrm{tot}}=M\vec a=M\ddot h\vec u$,

$$
M\ddot h+2kh=2kL_0-Mg,
$$

soit

$$
\ddot h+\frac{2k}{M}h=\frac{2kL_0}{M}-g.
$$

Le manuscrit pose

$$
\omega_0=\sqrt{\frac{2k}{M}},\qquad h_0=\frac{2kL_0}{M}-g,
$$

et écrit l’équation sous la forme $\ddot h+\omega_0^2h=h_0$.

> La notation $h_0$ est celle de la source : elle désigne ici un second membre de dimension accélération, pas une hauteur. La hauteur d’équilibre sera $h_0/\omega_0^2$.

### c) Solution générale [2 pt]

On cherche une solution particulière et on lui ajoute la solution générale du problème homogène.

L’équation homogène $\ddot h+\omega_0^2h=0$ a pour solution

$$
h_h(t)=A\cos(\omega_0t)+B\sin(\omega_0t).
$$

Pour une solution particulière constante $h_p=z$, on a $\omega_0^2z=h_0$, donc $z=h_0/\omega_0^2$. Finalement,

$$
h(t)=\frac{h_0}{\omega_0^2}+A\cos(\omega_0t)+B\sin(\omega_0t),
$$

avec $A,B$ arbitraires.

### d) Problème de Cauchy [3 pt]

Les conditions sont $h(0)=L_0$ et $\dot h(0)=0$. La première donne

$$
h(0)=\frac{h_0}{\omega_0^2}+A\cos0+B\sin0,
$$

$$
A=L_0-\frac{h_0}{\omega_0^2}
=L_0-\frac{\omega_0^2L_0-g}{\omega_0^2}
=\frac g{\omega_0^2}.
$$

La seconde donne $\dot h(0)=B\omega_0=0$, donc $B=0$. Ainsi

$$
h(t)=\frac{h_0}{\omega_0^2}
+\left(L_0-\frac{h_0}{\omega_0^2}\right)\cos(\omega_0t).
$$

## Partie II — Oscillateur amorti (pages 3 et 4)

### e) Ajout du frottement [2 pt]

On ajoute

$$
\vec F=-\gamma\vec v=-\gamma\dot h\vec u.
$$

L’équation devient

$$
M\ddot h=2k(L_0-h)-Mg-\gamma\dot h,
$$

soit

$$
\ddot h+\frac\gamma M\dot h+\frac{2k}{M}h
=\frac{2kL_0}{M}-g,
\qquad\Gamma=\frac\gamma M.
$$

Avec les notations précédentes, $\ddot h+\Gamma\dot h+\omega_0^2h=h_0$.

### f) Recherche exponentielle [3 pt]

On cherche $h(t)=A+Be^{-i\alpha t}$. Alors

$$
\dot h=-i\alpha Be^{-i\alpha t},\qquad
\ddot h=-\alpha^2Be^{-i\alpha t}.
$$

La substitution donne

$$
(-\alpha^2-i\alpha\Gamma+\omega_0^2)Be^{-i\alpha t}
+A\omega_0^2=h_0.
$$

Ainsi

$$
A=\frac{h_0}{\omega_0^2},\qquad
\alpha^2+i\alpha\Gamma-\omega_0^2=0,
$$

et

$$
\alpha=-\frac{i\Gamma}2\pm\sqrt{\omega_0^2-\frac{\Gamma^2}4}.
$$

### g) Régime critique [2 pt]

$$
\omega_0^2=\frac{\Gamma^2}4.
$$

### h) Cas pseudo-périodique donné [3 pt]

Pour $\omega_0^2=(\Gamma/2)^2+4$,

$$
\alpha=-\frac{i\Gamma}2\pm\sqrt4=-\frac{i\Gamma}2\pm2.
$$

La solution réelle donnée est

$$
h(t)=\frac{h_0}{\omega_0^2}
+e^{-\Gamma t/2}[A\cos(2t)+B\sin(2t)].
$$

Les lettres $A,B$ désignent dans cette dernière ligne les constantes de la solution réelle ; elles sont réutilisées par le manuscrit après l’essai exponentiel de f).
