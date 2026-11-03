# Mécanique du point — Résumé 6 : systèmes de particules et collisions

> Source : `PREING1-S2/Mecanique-du-point/CM6_2013-2014_Mecanique-du-point_P1S2_DPhysique.pdf`, 2 pages, numérotées 12–13 dans le cours.
> Transcription du 13 octobre 2026 : lecture visuelle intégrale, comparaison au texte natif et restitution des formules. Les précisions sur le système considéré lors d’un choc sont indiquées séparément.

## Centre de masse, centre d’inertie ou barycentre (page 1)

Pour un système de $N$ masses $m_i$ placées en $M_i$, le centre de masse $G$ est défini par :

$$\overrightarrow{OG}=\frac{\sum_{i=1}^N m_i\overrightarrow{OM_i}}{\sum_{i=1}^N m_i},\qquad\text{ou encore}\qquad\sum_{i=1}^N m_i\overrightarrow{GM_i}=\vec0.$$

## Quantité de mouvement (page 1)

Si les masses se déplacent aux vitesses $\vec v_i$, la quantité de mouvement du système vaut :

$$\vec P=\sum_{i=1}^N m_i\vec v_i=M\vec v_G,\qquad M=\sum_{i=1}^N m_i,\qquad\vec v_G=\frac{d\overrightarrow{OG}}{dt}.$$

## Deuxième loi de Newton (page 1)

Les forces externes sont exercées par le milieu extérieur ; les forces internes sont exercées par les autres masses du système. D’après la troisième loi de Newton :

$$\sum\vec F_{\mathrm{int}}=\vec0\quad\Longrightarrow\quad\sum\vec F=\sum\vec F_{\mathrm{ext}}+\sum\vec F_{\mathrm{int}}=\sum\vec F_{\mathrm{ext}}.$$

La deuxième loi devient :

$$\boxed{\sum\vec F_{\mathrm{ext}}=\frac{d\vec P}{dt}=M\vec a_G.}$$

Si le système est isolé, sa quantité de mouvement $\vec P$ est constante.

## Énergie (page 1)

L’énergie cinétique du système est :

$$E_c=\sum_{i=1}^N E_{ci}=\frac12\sum_{i=1}^N m_i v_i^2.$$

Dans un référentiel galiléen, le théorème de l’énergie cinétique s’écrit :

$$\Delta E_c=\sum W_{\mathrm{ext}}+\sum W_{\mathrm{int}}.$$

Il faut inclure le travail de toutes les forces, internes comme externes.

- Si le système est rigide, $\sum W_{\mathrm{int}}=0$.
- Si le système est déformable, $\sum W_{\mathrm{int}}$ est en général non nul.

La résultante des forces internes est nulle, mais la somme de leurs travaux peut ne pas l’être.

## Collisions (page 2)

Une collision est une interaction très brève, localisée dans l’espace, et d’intensité très grande devant les forces externes.

Dans le modèle de collision du cours, la quantité de mouvement du système se conserve :

$$\vec P_{\mathrm{avant}}=\vec P_{\text{après}}.$$

La vitesse $\vec v_G$ est constante : le centre de masse suit un mouvement rectiligne uniforme.

Pour une collision **élastique**, l’énergie cinétique du système se conserve :

$$E_{c,\mathrm{avant}}=E_{c,\text{après}}.$$

Lors d’une collision élastique contre un mur, le document indique que le vecteur vitesse est réfléchi par le mur. Une collision est **parfaitement inélastique** lorsque les corps restent collés après le choc.

**Précisions.** La conservation de la quantité de mouvement suppose que l’impulsion des forces extérieures sur le système choisi soit négligeable pendant le choc. Pour le corps seul heurtant un mur, la force du mur est extérieure et sa quantité de mouvement n’est pas conservée. La réflexion du vecteur vitesse décrite par le cours correspond à un mur fixe et sans frottement.
