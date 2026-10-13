---
source: CC2-2023-2024_Electromagnetisme-CC_P2S1_DPhysique.pdf, pages 1 à 8 (énoncés ; la feuille-réponse et les cadres de rédaction des pages 9 à 16 ne sont pas reproduits)
transcription: manuelle
---

# CC2 d'Électromagnétisme — 7 décembre 2023

> **Note :** contrôle de 1 h 30, sans document ni calculatrice, 24 questions. Une seule bonne réponse par question à choix multiples, pas de point négatif. Les questions 16, 20 et 23 sont à rédiger. Les corrections se trouvent dans la transcription du corrigé.

## Questions de cours : potentiel, circulation, Biot et Savart, force de Lorentz

**Énoncé.** (4 points, 0,5 point par question)

1. Dans le cas d'une distribution volumique de charges, le potentiel électrique est :
    A) défini sur la surface chargée et non continu à la traversée de la surface ;
    B) défini et continu en tout point de l'espace ;
    C) non défini aux points où se trouvent les charges ;
    D) aucune des réponses précédentes.
2. La variation d'un champ scalaire $V(M)$ est $dV(M) = \overrightarrow{\operatorname{grad}}\, V \cdot d\overrightarrow{OM}$. Le vecteur $\overrightarrow{\operatorname{grad}}\, V$ est donc : A) tangent à la surface équipotentielle passant par $M$ ; B) normal à la surface équipotentielle passant par $M$ ; C) un vecteur directeur de la surface équipotentielle passant par $M$ ; D) aucune des réponses précédentes.
3. Le champ $\vec E$ est à circulation conservative et on définit le potentiel électrostatique par : A) $\vec E = \overrightarrow{\operatorname{grad}}\, V$ ; B) $\vec V = \overrightarrow{\operatorname{grad}}\, E$ ; C) $\vec E = -\overrightarrow{\operatorname{grad}}\, V$ ; D) aucune des réponses précédentes.
4. La circulation $C$ du champ $\vec E$ est donnée par : A) $C = \oiint_S \vec E \cdot d\vec S$ ; B) $C = \iiint_V \vec E \cdot d\vec V$ ; C) $C = \int_A^B \vec E \cdot d\vec l$ ; D) aucune des réponses précédentes.
5. La loi de Biot et Savart donne le champ magnétique $\vec B$ d'une distribution de courant $I$, $P$ étant un point de la distribution. Elle s'énonce : A) $\vec B(M) = \displaystyle\oint_\Gamma \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{MP}}{MP^2}$ ; B) $\vec B(M) = \displaystyle\oint_\Gamma \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^3}$ ; C) $\vec B(M) = \displaystyle\oint_\Gamma \frac{\mu_0 I}{4\pi}\frac{d\vec l \wedge \overrightarrow{PM}}{PM^2}$ ; D) aucune des réponses précédentes.
6. En étudiant les plans de symétrie de la distribution de courant, on trouve que la direction de $\vec B$ en $M$ est :
    A) celle de la droite orthogonale à un plan $\Pi$ de symétrie passant par $M$ ;
    B) incluse dans tout plan $\Pi$ de symétrie passant par $M$ ;
    C) celle de la droite intersection d'au moins deux plans de symétrie passant par $M$ ;
    D) aucune des réponses précédentes.
7. En présence d'un champ magnétique $\vec B$, une charge $q$ de vitesse $\vec v$ est soumise à la force de Lorentz : A) $\vec f_L = qB\vec v$ ; B) $\vec f_L = qv\vec B$ ; C) $\vec f_L = q\,\vec v \cdot \vec B$ ; D) $\vec f_L = q\,\vec v \wedge \vec B$ ; E) aucune des réponses précédentes.
8. À l'intérieur d'un conducteur en équilibre électrostatique, le champ électrique créé par : A) les charges du conducteur est nul ; B) les charges extérieures au conducteur est nul ; C) toutes les charges (du conducteur et extérieures) est nul ; D) aucune des réponses précédentes.

## Exercice 1 : Cylindre chargé en volume

**Énoncé.** (8 points) Un cylindre infini d'axe $(Oz)$ et de rayon $R$ est chargé en volume avec la densité $\rho(r, \theta, z) = \dfrac{r}{a}$, où $a$ est une constante positive et $r$ la distance à l'axe ($a$ est telle que $\rho$ ait la dimension adéquate). On prend l'origine des potentiels en $r = 0$ : $V(0) = 0$.

1. (Question 9, 0,25 point) La charge $Q(r)$ contenue dans un cylindre d'axe $(Oz)$, de rayon $r$ et de hauteur $h$ vaut, pour $r \le R$ : A) $\dfrac{\pi h r^2}{a}$ ; B) $0$ ; C) $\dfrac{\pi h r^3}{a}$ ; D) $\dfrac{2\pi h r^3}{3a}$ ; E) aucune des réponses précédentes.
2. (Question 10, 0,25 point) Même question pour $r \ge R$ : A) $0$ ; B) $\dfrac{\pi h R^2}{a}$ ; C) $\dfrac{2\pi h R^3}{3a}$ ; D) $\dfrac{\pi h R^3}{a}$ ; E) aucune des réponses précédentes.
3. (Question 11, 0,5 point) La direction de $\vec E$ au point $M$ est radiale car :
    A) tous les plans passant par $O$ et par $M$ sont des plans de symétrie de la distribution ;
    B) les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_r, \vec u_z)$ sont des plans de symétrie de la distribution ;
    C) les plans $(M, \vec u_r, \vec u_\theta)$ et $(M, \vec u_r, \vec u_\varphi)$ sont des plans de symétrie de la distribution ;
    D) aucune des réponses précédentes.
4. (Question 12, 1 point) Par le théorème de Gauss, pour $r \le R$ : A) $\vec E = \dfrac{r^2}{a\varepsilon_0}\vec u_r$ ; B) $\vec E = \dfrac{r^2}{3a\varepsilon_0}\vec u_r$ ; C) $\vec E = \dfrac{R^3}{3ar\varepsilon_0}\vec u_r$ ; D) $\vec E = \dfrac{R^2}{3a\varepsilon_0}\vec u_r$ ; E) $\vec E = \vec 0$ ; F) aucune des réponses précédentes.
5. (Question 13, 1 point) Pour $r \ge R$ : A) $\vec E = \dfrac{r^2}{a\varepsilon_0}\vec u_r$ ; B) $\vec E = \dfrac{R^2}{3a\varepsilon_0}\vec u_r$ ; C) $\vec E = \dfrac{r^2}{3a\varepsilon_0}\vec u_r$ ; D) $\vec E = \vec 0$ ; E) $\vec E = \dfrac{R^3}{3ar\varepsilon_0}\vec u_r$ ; F) aucune des réponses précédentes.
6. (Question 14, 1 point) Le potentiel $V(r)$ pour $r \le R$ vaut : A) $\dfrac{R^3}{3a\varepsilon_0}\left[\ln\dfrac{R}{r} - \dfrac13\right]$ ; B) $\dfrac{R^3}{3a\varepsilon_0}\left[\ln\dfrac{R}{r} + \dfrac13\right]$ ; C) $\dfrac{r^3}{9a\varepsilon_0}$ ; D) $0$ ; E) $-\dfrac{r^3}{9a\varepsilon_0}$ ; F) aucune des réponses précédentes.
7. (Question 15, 1 point) Le potentiel $V(r)$ pour $r \ge R$ vaut : A) $\dfrac{R^3}{3a\varepsilon_0}\left[\ln\dfrac{R}{r} - \dfrac13\right]$ ; B) $\dfrac{r^3}{9a\varepsilon_0}$ ; C) $\dfrac{R^3}{3a\varepsilon_0}\left[\ln\dfrac{R}{r} + \dfrac13\right]$ ; D) $-\dfrac{r^3}{9a\varepsilon_0}$ ; E) $0$ ; F) aucune des réponses précédentes.
8. (Question 16, 3 points) Démontrer l'expression du champ $\vec E$ et du potentiel $V$ pour $r \ge R$, en détaillant les calculs (symétries, invariances, surface de Gauss, flux, charge intérieure…).

## Exercice 2 : Fil infini parcouru par un courant

**Énoncé.** (4 points) Un fil de longueur infinie, confondu avec l'axe $(Oz)$, est parcouru par un courant $I$ constant orienté vers les $z$ croissants. On repère un point $M$ dans la base cylindrique $(\vec u_r, \vec u_\theta, \vec u_z)$. On cherche le champ magnétique créé en $M$, qui s'écrit de manière générale $\vec B(M) = B(r, \theta, z)\,\vec u$, avec $\vec u$ à déterminer.

1. (Question 17, 0,5 point) En regardant les invariances, on constate que $B(r, \theta, z)$ ne dépend que de : A) $z$ ; B) $\theta$ ; C) $\varphi$ ; D) $r$ ; E) aucune des réponses précédentes.
2. (Question 18, 0,5 point) Du fait des plans de symétrie, $\vec B(M)$ s'écrit : A) $B(z)\,\vec u_z$ ; B) $B(z)\,\vec u_r$ ; C) $B(r)\,\vec u_\theta$ ; D) $B(\theta)\,\vec u_\theta$ ; E) aucune des réponses précédentes.
3. (Question 19, 1 point) Par le théorème d'Ampère : A) $\vec B(M) = \dfrac{2\mu_0 I}{\pi r}\vec u_z$ ; B) $\dfrac{\mu_0 I}{\pi z}\vec u_r$ ; C) $\dfrac{\mu_0 I}{\pi z}\vec u_\theta$ ; D) $\dfrac{\mu_0 I}{2\pi r}\vec u_\theta$ ; E) aucune des réponses précédentes.
4. (Question 20, 2 points) Démontrer l'expression de $\vec B(M)$, en détaillant les calculs (symétries, invariances, théorème d'Ampère…).

## Exercice 3 : Condensateur cylindrique

**Énoncé.** (4 points) Un condensateur cylindrique à air est formé de deux armatures coaxiales de rayons $R_1 < R_2$. On note $Q_{\text{int}}$ la charge portée par la surface du cylindre intérieur, de rayon $R_1$ et de hauteur $h$. On suppose ce conducteur de longueur infinie ($h \gg R_2 > R_1$).

1. (Question 21, 0,5 point) Le champ $\vec E$ en un point $M$ à la distance $r$ de l'axe, avec $R_1 < r < R_2$, vaut : A) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 h r}\vec u_r$ ; B) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 r}\vec u_r$ ; C) $\dfrac{Q_{\text{int}}}{2\pi\varepsilon_0 r^2}\vec u_r$ ; D) aucune des réponses précédentes.
2. (Question 22, 1 point) La capacité $C$ de ce condensateur vaut : A) $\dfrac{2\pi\varepsilon_0 h}{\ln(R_2/R_1)}$ ; B) $\dfrac{2\pi\varepsilon_0 h}{\ln(R_1/R_2)}$ ; C) $\dfrac{2\pi\varepsilon_0 h}{R_2/R_1}$ ; D) aucune des réponses précédentes.
3. (Question 23, 1,5 point) Sans redémontrer l'expression du champ électrique d'un cylindre, établir l'expression de la capacité $C$ en détaillant les calculs.
4. (Question 24, 1 point) Pour $R_2 - R_1 = e \ll R_1$, la capacité se simplifie en : A) $\dfrac{2\pi\varepsilon_0 R_1 e}{h}$ ; B) $\dfrac{2\pi\varepsilon_0 R_1 h}{e}$ ; C) $\dfrac{2\pi\varepsilon_0 e h}{R_1}$ ; D) aucune des réponses précédentes.
