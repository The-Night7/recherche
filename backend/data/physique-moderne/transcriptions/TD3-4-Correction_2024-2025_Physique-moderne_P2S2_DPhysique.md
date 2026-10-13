---
source: "PREING2-S2/Physique-moderne/TD3-4-Correction_2024-2025_Physique-moderne_P2S2_DPhysique.pdf"
pages: 12
transcription: manuelle
transcription_date: 2026-10-03
verification: lecture visuelle intégrale des pages imprimées 17 à 28 ; équations, matrices et questions comparées au PDF ; erreurs de la source signalées séparément
---

# Physique moderne — TD 3 et 4 — Relations de Heisenberg et équation de Schrödinger

> Le fichier contient les douze dernières pages d’un cahier de 28 pages. La pagination imprimée est conservée dans les titres. Les expressions fautives sont reproduites et accompagnées de notes de vérification ; elles ne sont pas des incertitudes de lecture. Les solutions absentes ne sont pas inventées.

## Exercice préliminaire — Moyenne, écart-type et variance (pages 17 et 18)

### 1. Variable aléatoire discrète

On considère une grandeur aléatoire $g$ (note, salaire, nombre d’habitants, etc.), supposée discrète : elle ne peut prendre que $N$ valeurs $g_i$, avec $i\in[1,N]$.

**1.a)** Exprimer la valeur moyenne $\langle g\rangle$ en fonction des $g_i$.

On veut caractériser la dispersion des $g_i$ autour de la moyenne.

**1.b)** Montrer que la moyenne des écarts à la moyenne,

$$
\frac1N\sum_i(g_i-\langle g\rangle),
$$

n’est pas pertinente pour caractériser cette dispersion.

**1.c)** La variance $V=\langle(g-\langle g\rangle)^2\rangle$ est-elle directement pertinente ?

**1.d)** La grandeur pertinente est l’écart-type :

$$
\Delta g=\sqrt{\langle(g-\langle g\rangle)^2\rangle}.\tag{3.1}
$$

Montrer que

$$
(\Delta g)^2=\langle(g-\langle g\rangle)^2\rangle
=\langle g^2\rangle-\langle g\rangle^2.\tag{3.2}
$$

### 2. Variable aléatoire continue

Les valeurs d’une variable aléatoire continue $y$ sont réparties sur un intervalle (énergie, position, etc.). Leur répartition est caractérisée par une distribution de probabilité $\rho(y)$. La loi normale, ou distribution de Gauss, est

$$
\rho(y)=\frac1{\sigma\sqrt{2\pi}}
\exp\left[-\left(\frac{y-m}{\sigma\sqrt2}\right)^2\right],
\qquad y\in\mathbb R.\tag{3.3}
$$

$m=\langle y\rangle$ est l’espérance, moment d’ordre un, et $\sigma$ l’écart-type.

> La source appelle ici l’écart-type « carré du moment centré d’ordre 2 ». C’est sa **racine carrée**, conformément à (3.1).

**2.a)** Que vaut $\int_{-\infty}^{+\infty}\rho(y)\,dy$ pour la loi normale ?

**2.b)** Représenter graphiquement la gaussienne ; indiquer $m$ et approximativement $\sigma$.

**2.c)** Une aiguille horizontale peut tourner. Sa position est repérée par un angle $\theta$. Représenter la distribution de $\theta$ si toutes les directions sont équiprobables.

**2.d)** Quelle grandeur joue le rôle de distribution de probabilité en physique quantique ? À quelle variable aléatoire est-elle associée ?

**2.e)** En déduire le calcul de la position moyenne $\langle x\rangle$ et de son écart-type pour une particule décrite par la fonction d’onde $\Psi$.

*Aucune solution de cet exercice préliminaire n’est fournie dans ce fichier.*

## Exercice 7 — Particule dans un puits de potentiel infini (pages 18 à 20)

Une particule de masse $m$ est enfermée dans un puits de profondeur infinie et de largeur $L$. On veut montrer, à partir des inégalités de Heisenberg, que son énergie cinétique minimale n’est pas nulle.

### Énoncé

**1. Énergie minimale.**

- **1.a)** À partir de la relation spatiale de Heisenberg, déterminer une inégalité portant sur $\Delta p$ et $L$.
- **1.b)** Exprimer $\langle E\rangle$ en fonction de $\langle p^2\rangle$.
- **1.c)** À l’aide de l’exercice précédent, en déduire l’énergie cinétique minimale.
- **1.d)** Comparer avec une boule de billard dans une boîte.

**2.** Calculer $\Delta x$ pour les états stationnaires

$$
\psi_n(x)=\sqrt{\frac2L}\sin\left(\frac{n\pi x}{L}\right),
\qquad n\in\mathbb N^*.\tag{3.4}
$$

**3.** L’inégalité de Heisenberg serait-elle vérifiée pour une particule dont la probabilité de présence serait uniforme sur $[0,L]$ ?

### Solution 7 — Énergie

**1.a)** $\Delta x\le L$, donc $\Delta p\ge\hbar/(2L)$.

**1.b)** $\langle E\rangle=\langle p^2\rangle/(2m)$.

**1.c)** Par définition,

$$
(\Delta p)^2=\langle(p-\langle p\rangle)^2\rangle
=\langle p^2\rangle-\langle p\rangle^2.
$$

Ainsi $\langle p^2\rangle=(\Delta p)^2+\langle p\rangle^2\ge(\Delta p)^2$ et

$$
\langle E\rangle=\frac{\langle p^2\rangle}{2m}
\ge\frac{(\Delta p)^2}{2m}\ge\frac{\hbar^2}{8mL^2}.\tag{3.5}
$$

Le document encadre ensuite

$$
E_{\min}=\frac{\hbar^2}{8mL^2}.\tag{3.6 — source}
$$

Sa remarque précise pourtant qu’une moyenne supérieure à une borne ne signifie pas que le minimum soit cette borne. Elle ajoute que l’énergie moyenne serait l’énergie parce que celle-ci est conservée, « mais alors l’inégalité temps-énergie n’est pas vérifiée… ».

> **Note de vérification.** (3.5) établit seulement une borne. L’égalité (3.6) ne découle pas du raisonnement. La constance de l’énergie moyenne ne suffit pas non plus à conclure que sa dispersion est nulle ; la remarque sur une violation de l’inégalité temps-énergie n’est pas justifiée par ce calcul.

**1.d)** Pas de réponse distincte dans la source.

### Solution 7 — Moments de la position

Le calcul imprimé pour la moyenne est

$$
\begin{aligned}
\langle x_n\rangle
&=\int_0^L x|\psi_n|^2\,dx\\
&=\frac2L\int_0^L x\sin^2\left(\frac{n\pi x}{L}\right)dx
=\frac{2L}{n^2\pi^2}\int_0^{n\pi}x\sin^2x\,dx\\
&=\frac{L}{n^2\pi^2}\int_0^{n\pi}x\,dx
-\frac{L}{n^2\pi^2}\int_0^{n\pi}x\cos(2x)\,dx\\
&=\frac{L}{2n\pi}-\frac L2[x\sin(2x)]_0^{n\pi}
+\frac{L}{n^2\pi^2}\int_0^{n\pi}\cos(2x)\,dx.
\end{aligned}\tag{3.7 — source}
$$

Résultat encadré :

$$
\langle x_n\rangle=\frac L2.\tag{3.8}
$$

> **Erreur dans la dernière ligne de (3.7).** L’intégration par parties donne plutôt $L/2-L[x\sin(2x)]_0^{n\pi}/(2n^2\pi^2)+L\int_0^{n\pi}\sin(2x)\,dx/(2n^2\pi^2)$. Les deux termes trigonométriques s’annulent et le résultat (3.8) est correct.

Pour le second moment,

$$
\begin{aligned}
\langle x_n^2\rangle
&=\int_0^L x^2|\psi_n|^2\,dx\\
&=\frac2L\int_0^L x^2\sin^2\left(\frac{n\pi x}{L}\right)dx
=\frac{2L^2}{n^3\pi^3}\int_0^{n\pi}x^2\sin^2x\,dx\\
&=\frac16(2n^2\pi^2-3)\left(\frac L{n\pi}\right)^2,
\end{aligned}\tag{3.9}
$$

soit

$$
\langle x_n^2\rangle=\left(1-\frac3{2n^2\pi^2}\right)\frac{L^2}{3}.\tag{3.10}
$$

Le document en déduit

$$
(\Delta x_n)^2=\left(1-\frac{18}{n^2\pi^2}\right)\frac{L^2}{12}.\tag{3.11 — source}
$$

> **Erreur de calcul.** Soustraire $(L/2)^2$ à (3.10) donne $(\Delta x_n)^2=(1-6/(n^2\pi^2))L^2/12$. Le facteur $18$ imprimé rendrait la variance négative pour $n=1$.

### Solution 7 — Répartition uniforme et remarques

Le document pose $\psi(x)=1/\sqrt L$ sur $[0,L]$, d’où

$$
\langle x\rangle_{\mathrm{uni}}=\langle x_n\rangle=\frac L2,\tag{3.12}
$$

$$
\langle x^2\rangle_{\mathrm{uni}}=\frac{L^2}{3},\tag{3.13}
$$

$$
(\Delta x)^2_{\mathrm{uni}}=\frac{L^2}{12}.\tag{3.14}
$$

La première remarque invoque le principe de correspondance de Bohr : pour de grands nombres quantiques $n\gg1$, le système se comporte comme un système classique. La source écrit

$$
\langle x_n^2\rangle
=\left(1-\frac3{2n^2\pi^2}\right)\frac{L^2}3
=\left(1-\frac3{2n^2\pi^2}\right)\langle x^2\rangle_{\mathrm{uni}}
\xrightarrow[n\to\infty]{}\langle x^2\rangle_{\mathrm{uni}},\tag{3.15}
$$

$$
(\Delta x_n)^2
=\left(1-\frac{18}{n^2\pi^2}\right)\frac{L^2}{12}
=\left(1-\frac{18}{n^2\pi^2}\right)(\Delta x)^2_{\mathrm{uni}}
\xrightarrow[n\to\infty]{}(\Delta x)^2_{\mathrm{uni}}.\tag{3.16 — source}
$$

> (3.16) reprend la même erreur de facteur que (3.11). La limite reste inchangée avec le facteur correct $6$.

La deuxième remarque introduit l’opérateur $p=-i\hbar\,d/dx$ et la conjugaison $\psi^*=\overline\psi$. La formule (3.17) comporte une répétition dans son intégrande :

$$
\langle p_n\rangle=\int_0^L\psi^*p\psi
\left[-i\hbar\frac{d\psi_n}{dx}\right]dx=0.\tag{3.17 — source}
$$

La ligne suivante, appliquée à $\psi_n$ réel, donne correctement

$$
\langle p_n\rangle=\int_0^L\psi_n
\left[-i\hbar\frac{d\psi_n}{dx}\right]dx=0.\tag{3.18}
$$

Puis la source écrit

$$
\Delta p_n=\langle p_n^2\rangle
=\int_0^L\psi_n\left[-\hbar^2\frac{d^2\psi_n}{dx^2}\right]dx
=\cdots=\left(\frac{n\pi\hbar}{L}\right)^2,\tag{3.19 — source}
$$

et

$$
\Delta x_n\Delta p_n
=\sqrt{\frac{n^2\pi^2}{3}-2}\,\hbar
\ge\sqrt{\frac{\pi^2}{3}-2}\,\hbar
\simeq1{,}13\hbar>\frac\hbar2.\tag{3.20 — source}
$$

Le document conclut à l’accord avec Heisenberg. Pour la distribution uniforme, il affirme au contraire que Heisenberg ne serait pas respecté puisque $\langle p\rangle=\langle p^2\rangle=0$ avec un $\Delta x$ fini.

> **Vérification.** Dans (3.17), la forme générale est $\int\psi_n^*(-i\hbar\psi_n')\,dx$, sans facteur supplémentaire. Dans (3.19), il faut $(\Delta p_n)^2$ à gauche. Avec la variance corrigée, le produit est $\Delta x_n\Delta p_n=\frac\hbar2\sqrt{n^2\pi^2/3-2}$, soit environ $0{,}568\hbar$ pour $n=1$ ; Heisenberg est bien vérifié. Une fonction constante dans la boîte, prolongée par zéro à l’extérieur, est discontinue aux parois et ne satisfait pas les conditions du puits infini : calculer ses dérivées seulement à l’intérieur ne permet pas de conclure à une violation de Heisenberg.

Dernière remarque : les moments $\langle x_n^k\rangle$ pourraient se calculer à l’aide de la fonction Gamma incomplète, notée dans la source

$$
\Gamma(n;x)=\int_0^x t^{n-1}e^{-t}\,dt.\tag{3.21}
$$

Le texte affirme $\Gamma(n;0)=\Gamma(n)$ et $\Gamma(n)=(n-1)!$.

> **Erreur de borne.** Avec la définition (3.21), $\Gamma(n;0)=0$ ; la limite en $x\to+\infty$ vaut $(n-1)!$ pour $n\ge1$ entier.

## Exercice 8 — Électron dans un piège harmonique (page 21)

Un électron de masse $m$, de quantité de mouvement $p$, est piégé dans le potentiel $E_P=\frac12m\omega^2x^2$, avec $\omega=6\times10^8\ \mathrm{rad\,s^{-1}}$.

**1.** Écrire son énergie mécanique en fonction de $m,x,p,\omega$.

**2.** Les moyennes de la position et de la quantité de mouvement sont nulles. Exprimer $\langle E\rangle$ en fonction de $\langle x^2\rangle$.

**3.** Montrer que l’énergie mécanique est bornée inférieurement.

### Solution 8

**1.** $E=p^2/(2m)+m\omega^2x^2/2$.

**2.**

$$
\langle E\rangle=\frac{\langle p^2\rangle}{2m}
+\frac12m\omega^2\langle x^2\rangle
=\frac{(\Delta p)^2}{2m}+\frac12m\omega^2(\Delta x)^2.
$$

**3.** La source donne

$$
E\ge\left[\frac\hbar{\sqrt{2m}\,\Delta x}
-\sqrt{\frac m2}\omega\Delta x\right]^2
+\frac{\hbar\omega}2
\ge\frac{\hbar\omega}2
\simeq6\times10^{-26}\ \mathrm J=0{,}4\ \mu\mathrm{eV}.\tag{3.23 — source}
$$

> **Vérification.** Le développement du carré imprimé ne correspond pas à la borne issue de Heisenberg : il manque un facteur $2$ au dénominateur du premier terme. La formule cohérente est $\langle E\rangle\ge[\hbar/(2\sqrt{2m}\Delta x)-\sqrt{m/2}\,\omega\Delta x]^2+\hbar\omega/2$. Pour la pulsation donnée, $\hbar\omega/2\simeq3{,}2\times10^{-26}\ \mathrm J\simeq0{,}20\ \mu\mathrm{eV}$.

## Exercice 9 — Électron dans l’atome d’hydrogène (pages 21 et 22)

On considère un atome d’hydrogène de taille caractéristique $a$.

**1.** Donner l’expression générale de l’énergie mécanique de l’électron.

**2.** Trouver une borne inférieure $E_0$ en fonction de $a$ et de constantes fondamentales.

**3.** Déterminer $a_0$, la valeur de $a$ minimisant $E_0$.

**4.** Comparer $a_0$ au rayon $r_1$ du modèle de Bohr.

**5.** Expliquer en quoi Heisenberg justifie la stabilité de la matière.

**6.** En quoi le modèle de Bohr est-il en contradiction avec Heisenberg ?

### Solution 9

**1.**

$$
E=\frac{p^2}{2m}-\frac{e^2}{4\pi\varepsilon_0r}.
$$

**2.** Le document écrit

$$
\langle E\rangle=E
=\frac{\langle p^2\rangle}{2m}-\frac{e^2}{4\pi\varepsilon_0a}
\ge\frac{(\Delta p)^2}{2m}-\frac{e^2}{4\pi\varepsilon_0a}
\ge E_0=\frac{\hbar^2}{4ma^2}-\frac{e^2}{4\pi\varepsilon_0a}.
$$

**3.** Il donne ensuite

$$
\frac{dE_0}{da}=\frac{e^2}{2\pi\varepsilon_0a^2}-\frac{\hbar^2}{2ma^3},
\qquad a_0=\frac{2\pi\varepsilon_0\hbar^2}{me^2}.
$$

**4.** $a_0=r_1/2$.

> **Incohérence de dérivation.** La dérivée de l’expression affichée pour $E_0$ est $e^2/(4\pi\varepsilon_0a^2)-\hbar^2/(2ma^3)$. Elle conduit à la valeur de $a_0$ annoncée ; le coefficient $2\pi$ dans la dérivée imprimée est donc erroné. Le choix précis reliant $\Delta x$ à $a$ pour obtenir le facteur $1/4$ dans $E_0$ n’est pas explicité.

**5.** Selon la source, l’inégalité sur l’énergie impose une énergie minimale non nulle ; celle portant sur l’espace a montré une valeur minimale du rayon. Le texte conclut : « Cela confirme le modèle de Bohr. »

**6.** Dans le modèle de Bohr, les électrons ont des trajectoires précises et indépendantes du temps ; la source écrit qu’on aurait $\Delta r=0$ et $\Delta p=0$. Les inégalités de Heisenberg imposent d’abandonner la notion d’orbite précise au profit d’une interprétation probabiliste.

## 4. Équation de Schrödinger (page 23)

Référence donnée dans le support : Erwin Schrödinger, *An Undulatory Theory of the Mechanics of Atoms and Molecules*, Physical Review, vol. 28, no 6, p. 1049–1070, 1er décembre 1926.

Dans les deux exercices suivants, la particule provient de $-\infty$, a une énergie $E$ et une masse $m$.

## Exercice 10 — Marche de potentiel (pages 23 à 25)

$$
V(x)=\begin{cases}
0,&x\in I_1=]-\infty,0[,\\
V_0,&x\in I_2=[0,+\infty[.
\end{cases}
$$

### 1. Cas $E>V_0$

**1.a)** Montrer que, sur $I_1$, un état stationnaire peut être représenté par $\phi(x)=A_1e^{ik_1x}+B_1e^{-ik_1x}$ ; déterminer $k_1$.

**Solution.** On cherche une solution de l’équation indépendante du temps

$$
-\frac{\hbar^2}{2m}\phi''(x)+V(x)\phi(x)=E\phi(x),\qquad E>V_0.\tag{4.1}
$$

Sur $I_1$,

$$
\phi''+k_1^2\phi=0,\qquad k_1=\frac{\sqrt{2mE}}\hbar,\tag{4.2}
$$

et

$$
\phi(x)=A_1e^{ik_1x}+B_1e^{-ik_1x},\qquad A_1,B_1\in\mathbb C.\tag{4.3}
$$

**1.b)** Montrer que, sur $I_2$, on peut écrire $\phi(x)=A_2e^{ik_2x}$ ; déterminer $k_2$.

**Solution.**

$$
\phi''+k_2^2\phi=0,\qquad k_2=\frac{\sqrt{2m(E-V_0)}}\hbar.\tag{4.4}
$$

La solution mathématique est $\phi(x)=A_2e^{ik_2x}+B_2e^{-ik_2x}$, avec des constantes complexes. Le texte écrit par erreur $A_1,B_1\in\mathbb C$ à cet endroit.

Il n’y a ni réflexion à l’infini dans le potentiel constant, ni émission de particules depuis $+\infty$ ; la source invoque alors

$$
\lim_{x\to-\infty}\phi(x)=0\tag{4.5 — source}
$$

pour conclure $B_2=0$ et

$$
\phi(x)=A_2e^{ik_2x},\qquad A_2\in\mathbb C.\tag{4.6}
$$

> **Note de vérification.** La bonne condition est l’absence d’onde incidente depuis la droite. La limite (4.5), imprimée avec $-\infty$, n’est pas une condition satisfaite par ces ondes planes et ne justifie pas $B_2=0$.

**1.c)** Pourquoi $\phi$ et $\phi'$ sont-elles continues en zéro ? En déduire les rapports d’amplitudes.

**Solution.** La discontinuité du potentiel est finie. En utilisant simultanément les deux conditions,

$$
\phi(0^-)=\phi(0^+),\qquad \phi'(0^-)=\phi'(0^+),
$$

on obtient

$$
\frac{B_1}{A_1}=\frac{k_1-k_2}{k_1+k_2},\tag{4.7}
$$

$$
\frac{A_2}{A_1}=\frac{2k_1}{k_1+k_2}.\tag{4.8}
$$

**1.d)** Interpréter $R=|B_1/A_1|^2$ et l’exprimer en fonction de $k_1,k_2$.

**Solution.** $R$ est la probabilité de réflexion. La source écrit

$$
R=1-\frac{4k_1k_2}{(k_1+k_2)^2}
=\left(\frac{V_0}{2E-V_0}\right)^2.\tag{4.9 — source}
$$

**1.e)** Déterminer la probabilité de transmission à l’aide de l’interprétation de Born.

**Solution.** La particule est transmise ou réfléchie : $R+T=1$. La source donne

$$
T=\frac{4k_1k_2}{(k_1+k_2)^2}
=\frac{4E(E-V_0)}{(2E-V_0)^2}.\tag{4.10 — source}
$$

> **Erreurs des secondes égalités.** En substituant les définitions de $k_1,k_2$, on trouve $R=((\sqrt E-\sqrt{E-V_0})/(\sqrt E+\sqrt{E-V_0}))^2$ et $T=4\sqrt{E(E-V_0)}/(\sqrt E+\sqrt{E-V_0})^2$. Les premières égalités en nombres d’onde sont correctes.

**1.f)** Discuter le cas $E\gg V_0$.

**Solution imprimée.** En posant $\varepsilon=V_0/E$,

$$
R=\frac14\left(\frac\varepsilon{1-\varepsilon/2}\right)^2
\sim\frac\varepsilon4,\tag{4.11 — source}
$$

$$
T=\frac{1-\varepsilon}{(1-\varepsilon/2)^2},\tag{4.12 — source}
$$

$$
\lim_{\varepsilon\to0}R=0,\qquad\lim_{\varepsilon\to0}T=1.\tag{4.13}
$$

> Les deux premières lignes prolongent les erreurs précédentes ; même leur expression de $R$ serait équivalente à $\varepsilon^2/4$, pas $\varepsilon/4$. À partir de la bonne expression en racines, $R\sim\varepsilon^2/16$. Les limites (4.13) sont correctes.

### 2. Cas $E<V_0$ sur $I_2$

La solution stationnaire y est

$$
\phi(x)=A_3e^{\rho x}+B_3e^{-\rho x},\qquad
\rho=\frac{\sqrt{2m(V_0-E)}}\hbar.\tag{4.14}
$$

La fonction doit rester bornée lorsque $x\to+\infty$ : $A_3=0$, d’où $\phi(x)=B_3e^{-\rho x}$. Sur $I_1$, la solution garde sa forme précédente. Les raccordements donnent

$$
\frac{B_1}{A_1}=\frac{k_1-i\rho}{k_1+i\rho},\tag{4.15}
$$

$$
\frac{B_3}{A_1}=\frac{2k_1}{k_1+i\rho}.\tag{4.16}
$$

La probabilité de réflexion vaut $R=1$.

### 3. Caractère physique et normalisation

**Question.** En quoi les solutions précédentes ne décrivent-elles pas un état physique ? En quoi sont-elles utiles pour déterminer un état pertinent ?

**Solution source.** Pour $E>V_0$, les solutions ne sont pas normalisables. Pour $E<V_0$ et sur $I_2$, la source impose $B_3=\sqrt{2\rho}\,e^{i\theta}$, avec $\theta\in\mathbb R$, phase indéterminée.

> **Limite du corrigé.** Cette dernière valeur ne normalise que l’exponentielle isolée sur $I_2$, pas l’état de diffusion sur toute la droite, qui comporte encore des ondes planes sur $I_1$. La seconde partie de la question, sur la construction d’un état physique, n’est pas développée dans la source.

## Exercice 11 — Barrière de potentiel (pages 26 à 28)

La particule rencontre en zéro une barrière de hauteur $V_0>0$ et de largeur $a$ :

$$
V(x)=\begin{cases}
0,&x<0\quad\text{(région 1)},\\
V_0,&x\in[0,a]\quad\text{(région 2)},\\
0,&x>a\quad\text{(région 3)}.
\end{cases}
$$

On se place dans le cas $V_0>E>0$.

### 1. Fonctions d’onde dans les régions 1 et 3

**1.a)** Montrer que $\phi_{1/3}(x)=A_{1/3}e^{ikx}+B_{1/3}e^{-ikx}$ et déterminer $k$.

**Solution.** Dans ces deux régions, $\phi''+k^2\phi=0$ avec $k^2=2mE/\hbar^2$, ce qui donne les solutions proposées.

**1.b)** Justifier $B_3=0$.

**Solution source.** La particule provient de la gauche et est libre à droite de la barrière ; elle ne peut revenir de $+\infty$, d’où $B_3=0$. Le texte écrit aussi « $x>0$ » pour la droite de la barrière et $\lim_{x\to-\infty}\phi(x)=0$.

> La région libre à droite est $x>a$. Comme à l’exercice 10, l’absence d’onde incidente depuis la droite, et non cette limite d’onde plane, justifie $B_3=0$.

### 2. Fonction d’onde dans la barrière

**Question.** Montrer que $\phi_2(x)=A_2e^{qx}+B_2e^{-qx}$ et déterminer $q$.

**Solution.** $\phi''-q^2\phi=0$, avec $q^2=2m(V_0-E)/\hbar^2$, donne la forme demandée.

### 3. Conditions aux frontières

**Question.** Établir un système portant sur les $A_j,B_j$, $j\in\{1,2,3\}$, à partir des conditions aux points de discontinuité.

**Solution imprimée.** La hauteur du potentiel est finie ; $\phi$ et $\phi'$ doivent être continues. En zéro, la source donne

$$
\begin{cases}
\phi_1(0)=\phi_2(0),\\
\phi_1'(0)=\phi_2'(0),
\end{cases}
\qquad
\begin{cases}
A_1+B_1=A_2+B_2,\\
ik(A_1-B_1)=-q(A_2-B_2).
\end{cases}
$$

En $a$, elle écrit

$$
\begin{cases}
A_2e^{qa}+B_2e^{-qa}=A_3e^{ika},\\
q(A_2-B_2)=ikA_3.
\end{cases}
$$

Les deux formes matricielles imprimées sont

$$
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}A_2\\B_2\end{pmatrix}
=\begin{pmatrix}1&1\\-ik/q&ik/q\end{pmatrix}
\begin{pmatrix}A_1\\B_1\end{pmatrix},\tag{4.17 — source}
$$

$$
A_3\begin{pmatrix}e^{ika}\\1\end{pmatrix}
=\begin{pmatrix}e^{qa}&e^{-qa}\\-iq/k&iq/k\end{pmatrix}
\begin{pmatrix}A_1\\B_1\end{pmatrix}.\tag{4.18 — source}
$$

> **Erreurs de raccordement.** La dérivée de $A_2e^{qx}+B_2e^{-qx}$ est $q(A_2e^{qx}-B_2e^{-qx})$. Il faut donc $ik(A_1-B_1)=q(A_2-B_2)$ en zéro et $q(A_2e^{qa}-B_2e^{-qa})=ikA_3e^{ika}$ en $a$. Dans (4.17), les signes de la seconde ligne de la matrice de droite sont inversés. Dans (4.18), le vecteur doit contenir $A_2,B_2$ et les exponentielles doivent figurer aussi dans le raccordement des dérivées. Une écriture cohérente en $a$ est
>
$$
A_3e^{ika}\begin{pmatrix}1\\ik\end{pmatrix}
=\begin{pmatrix}e^{qa}&e^{-qa}\\qe^{qa}&-qe^{-qa}\end{pmatrix}
\begin{pmatrix}A_2\\B_2\end{pmatrix}.
$$

### 4. Amplitudes $A_1$ et $B_1$ en fonction de $A_3$

Le corrigé donne

$$
A_1=\left[\cosh(qa)-i\frac{k^2-q^2}{2kq}\sinh(qa)\right]e^{ika}A_3
$$

et

$$
B_1=-i\frac{k^2+q^2}{2kq}\sinh(qa)e^{ika}A_3
=i\operatorname{Im}\left[\frac{k^2+q^2}{k^2-q^2}A_1\right].
$$

> La première expression de chaque amplitude est compatible avec les conditions de raccordement corrigées. La dernière égalité faisant intervenir $\operatorname{Im}$ n’est pas générale : elle suppose notamment que la phase de $e^{ika}A_3$ ait été choisie réelle et elle est indéfinie pour $k=q$. Les premières expressions restent utilisables dans ce cas.

### 5. Réflexion et transmission

On définit

$$
R=\left|\frac{B_1}{A_1}\right|^2,\qquad
T=\left|\frac{A_3}{A_1}\right|^2.
$$

**5.a)** Interpréter $R,T$. Que vaudraient-ils pour une particule classique ?

**5.b)** Exprimer $T$ en fonction de $V_0$, de la masse $m$ et de l’énergie $E$.

**5.c)** Déterminer $T$ pour une barrière épaisse, $qa\gg1$.

**5.d)** Dans cette approximation, calculer $T$ pour un électron avec $E=1\ \mathrm{eV}$, $a=1\ \text{Å}$ et $V_0=2E$.

**Solution.** $R$ est la probabilité de réflexion sur la barrière et $T$ celle de transmission à sa droite. Le corrigé n’écrit pas séparément les valeurs classiques demandées.

$$
T=\left|\frac{A_3}{A_1}\right|^2
=\frac{4k^2q^2}{4k^2q^2+(k^2+q^2)^2\sinh^2(qa)}.
$$

Donc

$$
T=\frac{4E(V_0-E)}{4E(V_0-E)+V_0^2\sinh^2\left(a\sqrt{2m(V_0-E)}/\hbar\right)}
=\frac{4E(V_0-E)}{4E(V_0-E)+V_0^2\sinh^2(a/\ell)},
$$

avec $\ell=\hbar/\sqrt{2m(V_0-E)}$, appelée « longueur de pénétration ».

La source ajoute : la particule « ne pénètre pas dans la barrière » mais aurait une probabilité non nulle de « sauter » au-dessus en raison de fluctuations de son énergie.

> **Incohérence avec le calcul.** Les solutions ont été établies à énergie fixée $E<V_0$ et $\phi_2$ est non nulle dans la barrière. Le calcul ne décrit donc ni une hausse temporaire de l’énergie au-dessus de $V_0$, ni une probabilité de présence nulle dans la barrière.

Pour $a\gg\ell$, le corrigé obtient

$$
T\simeq\frac{16E(V_0-E)}{V_0^2}e^{-2a/\ell}.
$$

Il justifie cette expression par « pour $x\gg1$, $\sinh x\sim e^x$ », puis donne $T\simeq0{,}78$, soit environ huit chances sur dix de franchir la barrière, ce qui serait impossible classiquement.

> **Vérification de l’approximation.** L’équivalent correct est $\sinh x\sim e^x/2$ ; il conduit bien au facteur $16$ affiché. Pour les données de 5.d), $qa\simeq0{,}512$ : la barrière n’est pas épaisse. La formule exacte donne $T=1/\cosh^2(qa)\simeq0{,}786$, tandis que l’approximation donne environ $1{,}44$, ce qui confirme qu’elle ne s’applique pas. La valeur source $0{,}78$ correspond au calcul exact.
