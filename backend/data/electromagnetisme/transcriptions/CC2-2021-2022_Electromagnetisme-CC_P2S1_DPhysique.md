---
source: "PREING2-S1/Electromagnetisme-CC/CC2-2021-2022_Electromagnetisme-CC_P2S1_DPhysique.pdf"
pages: 8
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-14
verification: lecture visuelle des huit pages, dont les quatre pages manuscrites ; formules et courbes vérifiées
---

# Électromagnétisme — CC2 du 2 décembre 2021 : sujet et corrigé

**PréIng 2 — durée : 1 h 30 (2 h avec tiers temps).** Documents, appareils électroniques, déplacements et échanges interdits. Le sujet annonce une seule réponse vraie par question à choix multiples, à noircir complètement au crayon ; une simple coche ne compte pas. La page 1 contient les consignes et le cartouche d’identification.

> **Nature du document.** Le nom du fichier ne porte pas « Correction », mais le PDF l’indique et comporte les réponses manuscrites aux questions 13, 14, 20 et 21. Les QCM ne montrent pas de cases cochées : leurs réponses et justifications ci-dessous sont des compléments rédigés, distincts de la transcription manuscrite. Les lettres A, B, etc. désignent ici l’ordre des propositions, non lettrées dans le PDF.

## Questions de cours — Q1 à Q6 (3 points ; page 2)

Chaque question vaut 0,5 point.

**Q1.** La circulation $C$ du champ électrostatique est : A) $\iint_S\vec E\cdot d\vec S$ ; B) $\iiint_V\vec E\cdot d\vec V$ ; C) $\int_A^B\vec E\cdot d\vec l$ ; D) aucune de ces réponses.

**Réponse rédigée : C.** La circulation est une intégrale le long d’un chemin ; la proposition A est un flux.

**Q2.** Le champ étant à circulation conservative, on définit le potentiel par : A) $\vec E=-\overrightarrow{\mathrm{grad}}V$ ; B) $\vec E=\overrightarrow{\mathrm{grad}}V$ ; C) $\vec V=\overrightarrow{\mathrm{grad}}E$ ; D) aucune.

**Réponse rédigée : A.** Le champ pointe vers les potentiels décroissants.

**Q3.** Pour une surface fermée $S$ entourant la charge $q_{\mathrm{int}}$, le théorème de Gauss est : A) $\Phi=\iint_S\vec E\cdot d\vec S=q_{\mathrm{int}}$ ; B) $\Phi=\iiint_V\vec E\cdot d\vec V=q_{\mathrm{int}}/\varepsilon_0$ ; C) $\Phi=\iint_S\vec E\cdot d\vec S=q_{\mathrm{int}}/\varepsilon_0$ ; D) aucune.

**Réponse rédigée : C.** La surface est fermée et orientée vers l’extérieur.

**Q4.** Puisque $dV(M)=\overrightarrow{\mathrm{grad}}V\cdot d\overrightarrow{OM}$, le gradient est : A) tangent à l’équipotentielle ; B) un vecteur directeur de l’équipotentielle ; C) normal à l’équipotentielle ; D) aucune.

**Réponse rédigée : C.** Tout déplacement tangent à une équipotentielle vérifie $dV=0$.

**Q5.** Pour une distribution volumique de charges, le potentiel est : A) défini sur la surface chargée mais discontinu à sa traversée ; B) non défini aux points portant des charges ; C) défini et continu en tout point de l’espace ; D) aucune.

**Réponse rédigée : C**, pour les densités volumiques régulières considérées dans ce cours, avec un choix de référence du potentiel adapté à la distribution.

**Q6.** L’énergie potentielle d’une charge $q$ dans le potentiel $V$ est : A) $E_p=qV+K$ ; B) $E_p=qE+K$ ; C) $E_p=-qV+K$ ; D) aucune.

**Réponse rédigée : A.** La constante $K$ fixe l’origine des énergies potentielles.

## Exercice 1 — Cylindre uniformément chargé en volume (9 points ; pages 3–5)

**Énoncé commun.** Un cylindre plein de rayon $R$, de longueur infinie et d’axe $Oz$ porte une densité volumique uniforme $\rho>0$. La distance à l’axe est $r$.

**Q7 (1 point).** Le champ est : A) dirigé selon $Oz$ ; B) de direction quelconque ; C) radial ; D) contenu dans les plans d’antisymétrie ; E) aucune.

**Réponse rédigée : C.** Les invariances et symétries donnent $\vec E=E(r)\vec e_r$.

**Q8 (1 point).** À l’extérieur du cylindre : A) $E=\rho R^2/(2\varepsilon_0r)$ ; B) $E=\rho r/(2\varepsilon_0)$ ; C) $E=\rho R^2/(4\varepsilon_0r)$ ; D) $E=\rho R^2/(3\varepsilon_0r)$ ; E) aucune.

**Réponse rédigée : A.** Voir la démonstration de Q13.

**Q9 (1 point).** À l’intérieur : A) $E=\rho R^2/(2\varepsilon_0r)$ ; B) $E=\rho r/(2\varepsilon_0)$ ; C) $E=2\rho r/\varepsilon_0$ ; D) $E=\rho r/\varepsilon_0$ ; E) aucune.

**Réponse rédigée : B.** Voir Q13.

**Q10 (1 point).** Le potentiel intérieur est, à une constante près : A) $-\rho R^2\ln r/(2\varepsilon_0)$ ; B) $\rho r^2/(4\varepsilon_0)$ ; C) $-\rho r^2/(4\varepsilon_0)$ ; D) $\rho r^2/\varepsilon_0$ ; E) aucune.

**Réponse rédigée : C.** Intégrer $V'(r)=-E(r)$.

**Q11 (1 point).** Le potentiel extérieur est, à une constante près : A) $-\rho R^2\ln r/\varepsilon_0$ ; B) $-\rho R^2\ln r/(2\varepsilon_0)$ ; C) $\rho R^2/(\varepsilon_0r)$ ; D) $-\rho r^2/(4\varepsilon_0)$ ; E) aucune.

**Réponse rédigée : B.** Pour rendre l’argument du logarithme sans dimension, on peut écrire $\ln(r/r_0)$ et absorber le choix de $r_0>0$ dans la constante.

**Q12 (1 point).** Si $V(R)=0$, la constante du potentiel intérieur vaut : A) $-\rho R^2/(4\varepsilon_0)$ ; B) $-\rho R^2/\varepsilon_0$ ; C) $\rho R^2/(4\varepsilon_0)$ ; D) $\rho R^2\ln R/(2\varepsilon_0)$ ; E) aucune.

**Réponse rédigée : C.** Ainsi

$$V_{\mathrm{int}}(r)=\frac{\rho}{4\varepsilon_0}(R^2-r^2),\qquad
V_{\mathrm{ext}}(r)=-\frac{\rho R^2}{2\varepsilon_0}\ln(r/R).$$

**Q13 (2 points ; page 4).** Retrouver le champ intérieur et extérieur par le théorème de Gauss.

**Transcription du corrigé manuscrit.** Une distribution volumique régulière donne un champ défini et continu dans tout l’espace. Les rotations autour de $Oz$ et les translations selon $Oz$ laissent la distribution inchangée : les composantes du champ ne dépendent que de $r$.

Les plans $(M,\vec e_r,\vec e_\theta)$ et $(M,\vec e_r,\vec e_z)$ sont des plans de symétrie. Le champ appartient à leur intersection, donc

$$\vec E(M)=E(r)\vec e_r\quad(0,5\text{ point}).$$

En coordonnées cylindriques,

$$d\vec l=dr\,\vec e_r+r\,d\theta\,\vec e_\theta+dz\,\vec e_z.$$

Les éléments de surface sont $r\,d\theta\,dz$ sur une surface à $r$ constant, $dr\,dz$ à $\theta$ constant et $r\,dr\,d\theta$ à $z$ constant. Le dessin représente un cylindre de Gauss coaxial de rayon $r$ et hauteur $h$, avec sa surface latérale et deux disques de normales opposées $\pm\vec e_z$. Le flux sur ces disques est nul ; sur la surface latérale,

$$\Phi=2\pi rhE(r)=\frac{q_{\mathrm{int}}}{\varepsilon_0}\quad(0,5\text{ point}).$$

Si $r\ge R$, $q_{\mathrm{int}}=\rho\pi R^2h$, donc

$$E(r)=\frac{\rho R^2}{2\varepsilon_0r}\quad(0,5\text{ point}).$$

Si $r\le R$, $q_{\mathrm{int}}=\rho\pi r^2h$, donc

$$E(r)=\frac{\rho r}{2\varepsilon_0}\quad(0,5\text{ point}).$$

**Q14 (1 point ; page 5).** Tracer $E(r)$ pour $r$ de zéro à l’infini, notamment au raccord $R$.

**Transcription du graphique.** Axes horizontal $r$ et vertical $E(r)$. Un segment croissant relie $(0,0)$ à $(R,\rho R/(2\varepsilon_0))$. À partir de ce maximum, une branche en $1/r$ décroît vers zéro. Le champ est continu à $R$ ; des pointillés repèrent $R$ et $\rho R/(2\varepsilon_0)$.

## Exercice 2 — Potentiel d’une sphère uniformément chargée (8 points ; pages 6–8)

**Énoncé commun.** Une sphère pleine de rayon $R$ et centre $O$ porte une densité volumique uniforme $\rho$.

**Q15 (1 point).** Le champ est : A) défini partout sauf à la traversée de la surface ; B) défini partout ; C) défini partout sauf sur les points de la distribution ; D) aucune.

**Réponse rédigée : B.** Il est aussi continu à $r=R$.

**Q16 (1 point).** Le champ est radial car sont plans de symétrie : A) les plans $(M,\vec u_r,\vec u_\theta)$ et $(M,\vec u_\theta,\vec u_\varphi)$ ; B) les plans $(M,\vec u_r,\vec u_\theta)$ et $(M,\vec u_\theta,\vec u_z)$ ; C) tous les plans passant par $O$ et $M$ ; D) aucune.

**Réponse rédigée : C.** Leur intersection est la droite $OM$.

**Q17 (1 point).** Pour $r<R$, le champ vaut : A) $\rho r\vec u_r/(3\varepsilon_0)$ ; B) $\rho r\vec u_r/\varepsilon_0$ ; C) $-\rho r\vec u_r/(3\varepsilon_0)$ ; D) aucune.

**Réponse rédigée : A.** Gauss donne $4\pi r^2E=\rho(4\pi r^3/3)/\varepsilon_0$.

**Q18 (1 point).** Pour $r>R$, le champ vaut : A) $-\rho R^3\vec u_r/(3\varepsilon_0r^2)$ ; B) $\rho R^3\vec u_r/(\varepsilon_0r^2)$ ; C) $\rho R^3\vec u_r/(3\varepsilon_0r^2)$ ; D) aucune.

**Réponse rédigée : C.** La charge intérieure vaut alors $Q=4\pi\rho R^3/3$.

**Q19 (1 point).** Le potentiel est : A) défini et continu partout sauf à la traversée de la surface ; B) défini et continu partout ; C) non défini aux points portant des charges ; D) aucune.

**Réponse rédigée : B.** Voir les expressions raccordées de Q20.

**Q20 (2 points ; page 7).** Donner le potentiel intérieur et extérieur à partir du champ, avec $V(\infty)=0$.

**Transcription du corrigé manuscrit.** Pour $r\ge R$,

$$E(r)=\frac{Q}{4\pi\varepsilon_0r^2}=\frac{\rho R^3}{3\varepsilon_0r^2}=-\frac{dV}{dr}.$$

Pour $r\le R$, $E(r)=\rho r/(3\varepsilon_0)=-dV/dr$. Par intégration (1 point),

$$V_{\mathrm{ext}}(r)=\frac{\rho R^3}{3\varepsilon_0r}+K',\qquad
V_{\mathrm{int}}(r)=-\frac{\rho r^2}{6\varepsilon_0}+K''.$$

La condition à l’infini donne $K'=0$. La continuité à $R$ impose

$$\frac{\rho R^2}{3\varepsilon_0}=-\frac{\rho R^2}{6\varepsilon_0}+K'',\qquad K''=\frac{\rho R^2}{2\varepsilon_0}.$$

Finalement (1 point),

$$V(r)=\begin{cases}\dfrac{\rho}{6\varepsilon_0}(3R^2-r^2),&0\le r\le R,\\
\dfrac{\rho R^3}{3\varepsilon_0r},&r\ge R.\end{cases}$$

**Q21 (1 point ; page 8).** Tracer $V(r)$ pour $r$ de zéro à l’infini, notamment au raccord $R$.

**Transcription du graphique.** Le dessin correspond à $\rho>0$. La courbe part de $V(0)=\rho R^2/(2\varepsilon_0)$ avec une tangente horizontale, décroît suivant une parabole jusqu’à $V(R)=\rho R^2/(3\varepsilon_0)$, puis suivant une branche en $1/r$ qui tend vers zéro. Les deux branches se raccordent continûment, avec la même pente $-\rho R/(3\varepsilon_0)$. Les deux valeurs du potentiel et le rayon $R$ sont marqués en pointillés. Si $\rho<0$, toutes les ordonnées changent de signe.
