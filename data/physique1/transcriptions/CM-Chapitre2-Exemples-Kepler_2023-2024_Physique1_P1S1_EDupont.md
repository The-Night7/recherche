---
source: PREING1-S1/Physique1/CM-Chapitre2-Exemples-Kepler_2023-2024_Physique1_P1S1_EDupont.pdf
pages: 2
transcription: manuelle
verification: lecture intégrale de la source
---

# Physique 1 — Chapitre 2 : analyse dimensionnelle de la formule de Kepler

## Exemple 3 — Vérifier l’homogénéité

Vérifier l’homogénéité de la formule

$$T=2\pi\sqrt{\frac{R^3}{GM}},\tag{1}$$

avec $T$ la période de révolution d’une planète, $G$ la constante de gravitation universelle, $R$ le rayon de l’orbite circulaire et $M$ la masse de l’astre attracteur.

## Page 1 — Dimensions des paramètres

**0. Faire un schéma.** Le schéma représente deux points $M_1$ et $M_2$ de masses $m_1$ et $m_2$. Le vecteur unitaire $\vec u_{1\to2}$ est dirigé de $M_1$ vers $M_2$. La force $\vec F_{1\to2}$ appliquée à $M_2$ est dirigée vers $M_1$ : elle est attractive.

**1. Liste des paramètres et de leurs dimensions.**

$$[M]=[m_1]=[m_2]=\mathsf M,\qquad [R]=[r_{12}]=\mathsf L,\qquad[T]=\mathsf T.$$

Il reste à déterminer $[G]$.

Le système étudié est $\Sigma=\{\text{point }M_2\text{ de masse }m_2\}$, dans le référentiel d’étude $\mathcal R$.

$$r_{12}=\|\overrightarrow{M_1M_2}\|,\qquad
\vec u_{1\to2}=\frac{\overrightarrow{M_1M_2}}{\|\overrightarrow{M_1M_2}\|},\qquad
[\vec u_{1\to2}]=1.$$

La loi de gravitation donne

$$\vec F_{1\to2}=-G\frac{m_1m_2}{r_{12}^2}\vec u_{1\to2}.$$

Donc

$$[G]=\frac{[F_{1\to2}][r_{12}^2]}{[m_1m_2]}
=\frac{(\mathsf M\mathsf L\mathsf T^{-2})\mathsf L^2}{\mathsf M^2}
=\boxed{\mathsf M^{-1}\mathsf L^3\mathsf T^{-2}}.$$

## Page 2 — Vérification de la formule

En élevant (1) au carré,

$$T^2=4\pi^2\frac{R^3}{GM}.$$

Le facteur numérique $4\pi^2$ est sans dimension. Le membre de droite a pour dimension

$$[4\pi^2]\frac{[R^3]}{[G][M]}
=1\times\frac{\mathsf L^3}{(\mathsf M^{-1}\mathsf L^3\mathsf T^{-2})\mathsf M}
=\frac1{\mathsf T^{-2}}=\mathsf T^2=[T^2].$$

La formule est donc homogène, conformément à la conclusion « OK » du manuscrit.

> L’homogénéité est la propriété vérifiée ici ; elle ne suffit pas à elle seule à démontrer la formule physique ou son facteur $2\pi$.
