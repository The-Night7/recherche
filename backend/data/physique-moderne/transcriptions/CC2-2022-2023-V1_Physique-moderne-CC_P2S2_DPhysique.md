---
source: "PREING2-S2/Physique-moderne-CC/CC2-2022-2023-V1_Physique-moderne-CC_P2S2_DPhysique.pdf"
pages: 5
transcription: manuelle assistée par le texte natif
transcription_date: 2026-10-14
verification: lecture visuelle des cinq pages ; formules, normalisation et applications numériques vérifiées ; erreurs de la source signalées
---

# Physique moderne — Devoir nº 2 du 25 mai 2023 : sujet et corrigé

**PréIng2 — CY Tech — durée : 1 h 30 (2 h avec tiers temps).** Aucune sortie avant une heure. Documents, appareils électroniques, calculatrices, déplacements et échanges interdits. Justifier les réponses, définir les notations et donner les expressions littérales puis les applications numériques. Le sujet demande des ordres de grandeur à un chiffre significatif ; le barème est indicatif.

> Le cartouche annonce quatre pages, mais ce PDF contient cinq pages avec les solutions 1, 2 et 4. L’exercice 3 est explicitement retiré et n’a pas de solution dans la source. Le nom du fichier ne mentionne pas le corrigé.

**Données :** $\hbar=h/(2\pi)=1{,}05\times10^{-34}\ \mathrm{J\,s}$ ; $m_e=9{,}1\times10^{-31}\ \mathrm{kg}$ ; masse d’un nucléon $m_n=1{,}7\times10^{-27}\ \mathrm{kg}$ ; $1\ \mathrm{eV}=1{,}6\times10^{-19}\ \mathrm J$.

## Exercice 1 — Questions de cours (8 points ; pages 2–3)

**1. Énoncé.** Rappeler l’équation de Schrödinger dépendante du temps pour une particule de masse $m$ se déplaçant sur $Ox$ dans un potentiel quelconque.

**Solution (1 point).**

$$i\hbar\frac{\partial\psi}{\partial t}(x,t)
=-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}(x,t)+V(x,t)\psi(x,t).$$

**2. Énoncé.** Interpréter $|\psi|^2$ et nommer l’auteur de cette interprétation.

**Solution (2 points).** $|\psi(x,t)|^2\,dx$ est la probabilité de présence dans l’élément de longueur $dx$ autour de $x$. En trois dimensions, elle devient $|\psi(\vec r,t)|^2\,d^3r$. L’interprétation probabiliste est attribuée à Max Born (1926).

**3. Énoncé.** Quelle est la dimension physique de la fonction d’onde en dimension spatiale $d$ ?

**Solution (1 point).** La normalisation $\int|\psi|^2\,d^dr=1$ impose $[\psi]=L^{-d/2}$.

**4.a. Énoncé.** Rappeler l’inégalité d’Heisenberg pour $x$ et $p$ et définir les grandeurs.

**Solution (1 point).** $\Delta x$ et $\Delta p$ sont les dispersions (écarts types) de la position et de la quantité de mouvement selon le même axe. La relation précise est $\Delta x\,\Delta p\ge\hbar/2$ ; la version d’ordre de grandeur est $\Delta x\,\Delta p\gtrsim\hbar$.

**4.b. Énoncé.** Pourquoi le sujet préfère-t-il « indétermination » à « incertitude » ?

**Solution (1 point).** Le corrigé distingue les dispersions intrinsèques de l’état quantique des erreurs expérimentales liées aux instruments ou à la mesure. L’inégalité exprime une propriété de l’état, démontrable dans le formalisme quantique. Le mot « incertitude », courant dans le nom de cette relation, ne doit donc pas être compris ici comme une simple imprécision instrumentale.

**5. Énoncé.** Un électron rencontre une barrière de potentiel plus haute que son énergie : quel phénomène sans analogue classique peut apparaître ? Donner une application.

**Solution (2 points).** L’effet tunnel donne une probabilité non nulle de traverser une barrière de largeur finie. Exemples cités : microscope à effet tunnel ; interprétation de la radioactivité alpha par le modèle de Gamow.

## Exercice 2 — Applications directes (5 points ; pages 3–4)

**1. Énoncé.** Quelle énergie cinétique donne une longueur d’onde de de Broglie $\lambda=0{,}1\ \mathrm{nm}$ à un électron puis à un neutron ?

**Solution (3 points).** Les relations $p=\hbar k=h/\lambda$ et $E_c=p^2/(2m)$ donnent

$$E_c=\frac{h^2}{2m\lambda^2}.$$

> **Applications numériques rectifiées.** La source annonce $10^{-16}\ \mathrm J$ pour l’électron et $10^{-19}\ \mathrm J$ pour le neutron. Avec ses propres données, $h=2\pi\hbar\simeq6{,}60\times10^{-34}\ \mathrm{J\,s}$ et $\lambda=10^{-10}\ \mathrm m$ donnent en réalité
> $$E_{c,e}\simeq2{,}39\times10^{-17}\ \mathrm J\simeq149\ \mathrm{eV},\qquad E_{c,n}\simeq1{,}28\times10^{-20}\ \mathrm J\simeq0{,}080\ \mathrm{eV}.$$
> À un chiffre significatif : $2\times10^{-17}\ \mathrm J$ et $1\times10^{-20}\ \mathrm J$.

**2. Énoncé.** Pour $E_c=1\ \mathrm{MeV}$, déterminer la fréquence et la longueur d’onde de de Broglie de chaque particule.

**Solution du PDF (2 points).** Dans le modèle non relativiste utilisé,

$$\lambda=\frac h{\sqrt{2mE_c}},\qquad f=\frac{E_c}{h}.$$

La source donne $\lambda_e\simeq1\ \mathrm{pm}$, $\lambda_n\simeq0{,}1\ \mathrm{pm}$ et $f\simeq10^{20}\ \mathrm{Hz}$ pour les deux particules.

> **Vérification et domaine du modèle.** Avec $E_c=1{,}6\times10^{-13}\ \mathrm J$, les calculs non relativistes donnent $\lambda_e=1{,}22\ \mathrm{pm}$, $\lambda_n=0{,}0283\ \mathrm{pm}$ et $f=2{,}43\times10^{20}\ \mathrm{Hz}$. La valeur du neutron est donc à rectifier. À $1\ \mathrm{MeV}$, l’électron est relativiste : la formule classique n’est plus physiquement adaptée. La relation correcte est $pc=\sqrt{E_c(E_c+2mc^2)}$, soit $\lambda=hc/\sqrt{E_c(E_c+2mc^2)}$, environ $0{,}87\ \mathrm{pm}$ pour l’électron avec $c\simeq3\times10^8\ \mathrm{m\,s^{-1}}$. La fréquence $E_c/h$ correspond au choix d’origine d’énergie du modèle de Schrödinger ; avec l’énergie relativiste totale, elle serait $(mc^2+E_c)/h$.

## Exercice 3 — Diffraction d’électrons : exercice retiré (page 4)

**Énoncé conservé dans le PDF.** Une feuille d’or $^{197}_{79}\mathrm{Au}$ est bombardée d’électrons d’énergie de l’ordre de la centaine de MeV pour sonder un noyau de rayon $R=7\ \mathrm{fm}$. Les mots diffraction et interférence sont considérés comme synonymes dans cet exercice.

1. Montrer que cette gamme d’énergie permet la diffraction par le noyau.
2. Dans quelle partie du spectre se situeraient les photons d’une expérience analogue ?
3. Que confirme la diffraction sur la nature de l’électron, et qui a proposé cette hypothèse ?

> **Complément rédigé, absent de la source.** À ces énergies, $pc\simeq E$ pour l’électron. Une longueur d’onde de l’ordre du diamètre nucléaire $2R=14\ \mathrm{fm}$ correspond à $E\sim hc/(2R)\simeq90\ \mathrm{MeV}$ : l’ordre de grandeur annoncé est cohérent. Des photons de cette longueur d’onde appartiennent au domaine gamma. La diffraction met en évidence le comportement ondulatoire de l’électron, proposé par Louis de Broglie. L’exercice reste signalé comme retiré du devoir.

## Exercice 4 — Puits infini centré (7 points ; pages 4–5)

**Énoncé.** Sophie cherche les états stationnaires d’une particule dans

$$V(x)=\begin{cases}0,&-a/2\le x\le a/2,\\+\infty,&\text{sinon},\end{cases}$$

et propose $E_n=n\pi^2\hbar^2/(2ma^2)$, $n\in\mathbb N^*$, ainsi que

$$\psi(x,t)=\frac2a\sin(\pi x/a)e^{-iE_1t/\hbar}.$$

**1.** Quelle condition aux bords doit vérifier la fonction d’onde ?

**Solution (1 point).** $\psi(-a/2,t)=\psi(a/2,t)=0$, et la fonction d’onde est nulle en dehors du puits.

**2.** La fonction proposée respecte-t-elle cette condition ? La corriger.

**Solution (2 points).** Non, puisque $\sin(\pm\pi/2)=\pm1$. Dans le puits, une solution spatiale générale est $\phi(x)=C\cos(kx)+S\sin(kx)$ avec $k=\sqrt{2mE}/\hbar$. Pour le fondamental, $k=\pi/a$, $S=0$ et $\phi_1(x)=C\cos(\pi x/a)$.

> **Précision sur la source.** L’affirmation « les conditions aux bords imposent $S=0$ » vaut pour les états pairs, dont le fondamental, mais pas pour tous les états. Les valeurs permises sont $k_n=n\pi/a$ : cosinus pour $n$ impair, sinus pour $n$ pair.

**3.** La fonction est-elle normalisée ? La corriger.

**Solution (2 points).** On a

$$\int_{-a/2}^{a/2}\cos^2(\pi x/a)\,dx=\frac a2.$$

La condition $|C|^2a/2=1$ donne, en choisissant une phase globale nulle,

$$\psi_1(x,t)=\sqrt{\frac2a}\cos(\pi x/a)e^{-iE_1t/\hbar}\quad(|x|\le a/2).$$

> **Erreur de normalisation dans la source.** Le PDF nomme $\sqrt{a/2}$ « facteur de normalisation ». C’est la norme du sinus ou du cosinus brut ; il faut diviser par cette norme, donc multiplier par $\sqrt{2/a}$. Le préfacteur proposé $2/a$ a aussi une dimension physique incorrecte pour une fonction d’onde à une dimension.

**4.** Comment appelle-t-on l’état d’énergie $E_1$ ?

**Solution (1 point).** C’est l’état fondamental, de plus basse énergie.

**5.** Rectifier l’expression des énergies.

**Solution (1 point).** $E_n=\hbar^2k_n^2/(2m)$, donc

$$\boxed{E_n=\frac{n^2\pi^2\hbar^2}{2ma^2},\quad n\ge1.}$$

Le facteur est $n^2$, comme le corrige le PDF en rouge.
