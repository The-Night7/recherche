# Physique 1 — TD1 : prérequis de mathématiques pour la physique, corrigé manuscrit (2023–2024)

> Source : `PREING1-S1/Physique1/TD1-Prerequis-Correction-_2023-2024_Physique1_P1S1_EDupont.pdf`, 3 pages (énoncé imprimé annoté à la main sur fond de cahier ; aucun texte natif).
> Transcription du 13 octobre 2026 : lecture visuelle intégrale des trois pages ; énoncés imprimés et annotations manuscrites restitués. L’ordre de la source est conservé : la page 2 contient les exercices 3, 5 et 6, la page 3 l’exercice 4. Les énoncés sont en **gras** et les annotations manuscrites en texte courant.
> Les figures (secteur angulaire, cercle trigonométrique, triangle rectangle, configuration de Thalès) sont décrites, non reproduites. Les traits de liaison des exercices 2, 5 et 6 sont restitués d’après les calculs manuscrits ; dans l’exercice 2, leur tracé exact est peu lisible. L’exercice 1 renvoie à des réponses « 1/ » et « 2/ » dont les intitulés ne figurent pas sur la page.
> Vérification : tous les résultats ont été recalculés et sont justes.

# Prérequis de Mathématiques pour la physique

## Exercice 1 — Définition d’un angle

*Figure : secteur de disque de rayon $R$, d’angle au centre $\theta$, d’arc de longueur $L$.*

**Un arc de cercle de rayon $R=2\,m$ a pour longueur $L=4\,m$. Quelle est la valeur de l’angle $\theta$ ? Plusieurs réponses possibles.**

Annotations : $\theta$ sans dimension ; $\theta=\dfrac LR$ ; unité : radian.

$$\theta=\frac LR=\frac42=2\ \text{radians}\ \longrightarrow\ 1/$$

Conversion rad $\longleftrightarrow$ degré : $\pi\leftrightarrow180°$, donc

$$2\ \text{rad}=\frac{2\times180}{\pi}=\frac{360}{\pi}\ \text{degrés}\ \longrightarrow\ 2/$$

## Exercice 2 — Lecture sur le cercle trigonométrique

*Figure : cercle trigonométrique de centre $O$ ; point $M$ sur le cercle repéré par l’angle $\theta$ ; $A$ et $B$ projetés de $M$ sur les axes ; $I=(0,1)$ ; tangentes en $I$ et en $F=(1,0)$ ; la droite $(OM)$ coupe la tangente horizontale en $D$ et la tangente verticale en $E$ ; $C$ point de la verticale de $M$. Segments notés $a$ (de $A$ à $M$), $b$ (de $B$ à $M$), $c$ (de $F$ à $E$), $d$ (de $I$ à $D$).*

**Relier correctement le nom du segment à sa valeur :**

| Segment | Valeur |
| --- | --- |
| 1/ $a$ | 3 — $\cos\theta$ |
| 2/ $b$ | 1 — $\sin\theta$ |
| 3/ $c$ | 4 — $\tan\theta$ |
| 4/ $d$ | 2 — $\operatorname{cotan}\theta$ |

Annotations : $OB=AM=a$, $BM=OA=b$.

- $\cos\theta=\dfrac{OB}{OM}=\dfrac a1=a$
- $\sin\theta=\dfrac{BM}{OM}=\dfrac b1=b$
- $\tan\theta=\dfrac{\sin\theta}{\cos\theta}=\dfrac{BM}{OB}=\dfrac ba=c$
- $\operatorname{cotan}\theta=\dfrac{\cos\theta}{\sin\theta}=\dfrac{OB}{BM}=\dfrac ab=d$

Thalès :

- $\dfrac{OA}{OI}=\dfrac{OC}{OD}=\dfrac{AC}{ID}$, soit $\dfrac b1=\dfrac1{OD}=\dfrac ad$ ; d’où $OD=\dfrac1b$ et $bd=a$, donc $\dfrac ab=d$.
- $\dfrac{OB}1=\dfrac{OC}{OE}=\dfrac{CB}{EF}\implies\dfrac a1=\dfrac1{OE}=\dfrac bc\ \longrightarrow\ ac=b\ \longrightarrow\ \dfrac ba=c$ ; et $OE=\dfrac1a$.

## Exercice 3 — Les angles dans un triangle

*Figure : grand triangle rectangle d’angle $\pi/6$ en bas à droite et d’angle $\alpha$ en haut ; une hauteur issue d’un point de l’hypoténuse délimite les angles $\gamma$ et $\beta$.*

1. **Déterminer l’angle $\alpha$ en radian et en degré.**
2. **Déterminer l’angle $\beta$ en radian et en degré.**

Réponses (1/ et 2/) :

- $\beta$ ? On a $\boxed{\beta+\gamma=\dfrac\pi2}$ (et $\alpha=\gamma$).
  Triangle jaune : $\gamma+\dfrac\pi6+\dfrac\pi2=\pi$, donc
  $$\gamma=\pi-\left(\frac\pi2+\frac\pi6\right)=\left(\frac{6\pi}6-\frac{\pi\times3}6-\frac\pi6\right),$$
  donc $\gamma=\dfrac\pi3$, puis
  $$\beta=\frac\pi2-\gamma=\frac\pi2-\frac\pi3=\frac{3-2}6\pi=\frac\pi6\ \xrightarrow{\times\frac{180°}{\pi}}\ \frac{180}6=30°.$$
- $\alpha$ ? $\alpha+\dfrac\pi2+\dfrac\pi6=\pi\implies\alpha=\dfrac{6\pi}6-\left(\dfrac{3\pi}6+\dfrac\pi6\right)=\dfrac{2\pi}6=\dfrac\pi3$, soit $\dfrac{180}3=60°$.

## Exercice 5 — Formules d’addition des cosinus et sinus

**Relier correctement :**

| Expression | Formule |
| --- | --- |
| 1/ $\cos(a+b)$ | 2 — $\cos a\cos b-\sin a\sin b$ |
| 2/ $\sin(a+b)$ | 3 — $\sin a\cos b+\cos a\sin b$ |
| 3/ $\cos(a-b)$ | 1 — $\cos a\cos b+\sin a\sin b$ |
| 4/ $\sin(a-b)$ | 4 — $\sin a\cos b-\cos a\sin b$ |

## Exercice 6 — Dérivée des cosinus et sinus en 0

**Relier correctement :** **1/ $\cos'0$, 2/ $\sin'0$ avec 1 — $\pi/2$ ; 2 — $0$ ; 3 — $-1$ ; 4 — $1$.**

Liaisons : $\cos'0\to2$ ($0$) ; $\sin'0\to4$ ($1$).

Annotations : quand $\theta$ augmente, $\cos\theta$ diminue ($\cos'\theta<0$) et $\sin\theta$ augmente ($\sin'\theta>0$). *(Croquis du cercle trigonométrique avec $\cos\theta$ et $\sin\theta$ marqués.)*

$$\boxed{(\cos\theta)'=-\sin\theta,\qquad(\sin\theta)'=+\cos\theta}$$

- 1/ $\cos'0=-\sin0=0$
- 2/ $\sin'0=+\cos0=1$

## Exercice 4 — Théorème de Thalès

*Figure : deux segments en gras parallèles, $x$ à gauche et $1{,}8$ à droite, reliés par deux sécantes se coupant entre eux ; longueurs $6$ et $4$ sur l’une des sécantes ; les autres portions sont notées $a$ et $b$.*

**Sachant que les deux segments en gras sont parallèles que vaut $x$ :**

1. **2,7** *(entourée)*
2. 2
3. 3
4. 3,8
5. On ne peut pas conclure.

$$\boxed{\frac x{1{,}8}=\frac64=\frac ab}\quad\text{donc}\quad x=\frac64\times1{,}8=\frac{6\times\frac{18}{10}}4$$

$$x=\frac{6\times18}{40}=\frac{3\times9}{10}=\frac{27}{10}=2{,}7$$
