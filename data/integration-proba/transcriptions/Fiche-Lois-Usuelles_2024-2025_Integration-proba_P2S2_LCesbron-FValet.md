---
source: "PREING2-S2/Integration-proba/Fiche-Lois-Usuelles_2024-2025_Integration-proba_P2S2_LCesbron-FValet.pdf"
pages: 9
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Lois de variables aléatoires réelles discrètes usuelles

Ludovic Cesbron — Frédéric Valet — 2024–2025.

Dans cette transcription, « v.a.r. » signifie variable aléatoire réelle. La notation $X\sim\mathcal L$ restitue la notation de la source signifiant « $X$ suit la loi $\mathcal L$ ». Les intervalles d’entiers sont écrits sous forme d’ensembles. Les exemples posés sans solution dans la fiche restent sans solution ici.

## 1. Loi uniforme

De façon analogue à la probabilité uniforme, la loi uniforme est celle des v.a.r. discrètes qui prennent leurs différentes valeurs de manière équiprobable. Pour que cela soit possible, $X(\Omega)$ doit être fini.

### Définition 1.1

Soient $(\Omega,\mathbb P)$ un espace de probabilité et $X$ une v.a.r. telle que $X(\Omega)=\{a_1,a_2,\ldots,a_n\}$. On dit que $X$ suit une **loi uniforme sur $\{a_1,a_2,\ldots,a_n\}$** si

$$
\forall i\in\{1,\ldots,n\},\qquad\mathbb P(X=a_i)=\frac1n.
$$

On note $X\sim\mathcal U_{\{a_1,a_2,\ldots,a_n\}}$.

### Exemple 1.1

Si $X$ donne le résultat du lancer d’un dé équilibré, alors $X\sim\mathcal U_{\{1,\ldots,6\}}$.

### Proposition 1.1

Soient $n\in\mathbb N^*$ et $X\sim\mathcal U_{\{1,\ldots,n\}}$. Alors

$$
\mathbb E(X)=\frac{n+1}{2},
\qquad
\mathbb V(X)=\frac{n^2-1}{12}.
$$

L’espérance est la moyenne non pondérée des valeurs de $X$.

### Démonstration de la proposition 1.1

Pour l’espérance,

$$
\mathbb E(X)=\sum_{i=1}^n i\mathbb P(X=i)
=\sum_{i=1}^n i\frac1n=\frac1n\sum_{i=1}^n i.
$$

On reconnaît la somme d’une suite arithmétique de raison $1$ commençant à $i=1$ :

$$
\sum_{i=1}^n i=n\frac{n+1}{2}.
$$

D’où $\mathbb E(X)=\frac1n n\frac{n+1}{2}=\frac{n+1}{2}$.

Pour la variance, on calcule d’abord

$$
\mathbb E(X^2)=\sum_{i=1}^n i^2\mathbb P(X=i)=\frac1n\sum_{i=1}^n i^2.
$$

La somme des carrés, laissée en exercice dans la source, vaut

$$
\sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}6.
$$

Donc $\mathbb E(X^2)=(n+1)(2n+1)/6$ et

$$
\begin{aligned}
\mathbb V(X)&=\mathbb E(X^2)-\mathbb E(X)^2\\
&=\frac{(n+1)(2n+1)}6-\left(\frac{n+1}{2}\right)^2\\
&=\frac{2(n+1)(2n+1)-3(n+1)^2}{12}
=\frac{n^2-1}{12}.
\end{aligned}
$$

## 2. Loi de Bernoulli de paramètre $p\in[0,1]$

On s’intéresse à une expérience n’ayant que deux issues possibles : par exemple un pile ou face, ou un tirage unique dans une urne contenant deux types de boules. La première issue est appelée « succès », la seconde « échec ». Le paramètre $p$ est la probabilité du succès ; par complémentarité, l’échec a pour probabilité $1-p$.

On introduit $X:\Omega\to\{0,1\}$, avec $X=1$ en cas de succès et $X=0$ en cas d’échec.

### Définition 2.1

Soient $(\Omega,\mathbb P)$ un espace de probabilité, $p\in[0,1]$ et $X$ une v.a.r. discrète telle que $X(\Omega)=\{0,1\}$. On dit que $X$ suit une **loi de Bernoulli de paramètre $p$**, notée $X\sim\mathcal B(p)$, si

$$
\mathbb P(X=1)=p,
\qquad \mathbb P(X=0)=1-p.
$$

### Proposition 2.1

Si $X\sim\mathcal B(p)$, alors

$$
\mathbb E(X)=p,
\qquad\mathbb V(X)=p(1-p).
$$

### Démonstration de la proposition 2.1

Les résultats s’obtiennent directement :

$$
\mathbb E(X)=0(1-p)+1p=p,
$$

$$
\mathbb V(X)=\mathbb E(X^2)-\mathbb E(X)^2
=0^2(1-p)+1^2p-p^2=p-p^2=p(1-p).
$$

## 3. Loi binomiale de paramètres $(n,p)$

Les lois binomiales sont associées à la répétition indépendante d’une expérience de Bernoulli : par exemple une série de pile ou face, ou des tirages avec remise dans une urne contenant deux types de boules. Les paramètres sont $n$, le nombre de répétitions, et $p$, le paramètre de l’expérience de Bernoulli répétée.

La v.a.r. discrète $X$ compte le nombre de succès parmi les $n$ itérations ; on a $X(\Omega)=\{0,\ldots,n\}$.

### Définition 3.1

Soient $(\Omega,\mathbb P)$ un espace de probabilité, $p\in[0,1]$, $n\in\mathbb N$ et $X$ une v.a.r. discrète telle que $X(\Omega)=\{0,\ldots,n\}$. On dit que $X$ suit une **loi binomiale de paramètres $(n,p)$**, notée $X\sim\mathcal B(n,p)$, si

$$
\forall k\in\{0,\ldots,n\},\qquad
\mathbb P(X=k)=\binom nk p^k(1-p)^{n-k}.
$$

Pour avoir exactement $k$ succès parmi $n$ lancers, il faut $k$ réussites, d’où $p^k$, et $n-k$ échecs, d’où $(1-p)^{n-k}$. L’ordre des succès n’est pas imposé : il existe $\binom nk$ façons de répartir les $k$ succès parmi les $n$ lancers.

### Remarque 3.1

Une loi de Bernoulli de paramètre $p$ est une loi binomiale de paramètres $(1,p)$ : $\mathcal B(p)=\mathcal B(1,p)$, d’où l’utilisation de la même lettre $\mathcal B$.

### Remarque 3.2

Le binôme de Newton assure que l’on a bien défini une loi de probabilité :

$$
\sum_{k=0}^n\mathbb P(X=k)
=\sum_{k=0}^n\binom nk p^k(1-p)^{n-k}
=(p+1-p)^n=1.
$$

### Exemple 3.1

1. On lance une pièce équilibrée quinze fois. Quelle est la probabilité de faire exactement quatre fois pile ?
2. Une urne contient douze boules blanches et huit boules noires. On tire dix fois, avec remise, une boule dans l’urne. Quelle est la probabilité de tirer sept fois une boule blanche ?

### Proposition 3.1

Soient $p\in[0,1]$, $n\in\mathbb N$ et $X\sim\mathcal B(n,p)$. Alors

$$
\mathbb E(X)=np,
\qquad\mathbb V(X)=np(1-p).
$$

### Démonstration de la proposition 3.1

**Espérance :**

$$
\begin{aligned}
\mathbb E(X)
&=\sum_{k=0}^n k\mathbb P(X=k)
=\sum_{k=1}^n k\binom nk p^k(1-p)^{n-k}\\
&=\sum_{k=1}^n n\binom{n-1}{k-1}p^k(1-p)^{n-k}\\
&=n\sum_{i=0}^{n-1}\binom{n-1}{i}p^{i+1}(1-p)^{n-i-1}\\
&=np\sum_{i=0}^{n-1}\binom{n-1}{i}p^i(1-p)^{(n-1)-i}
=np.
\end{aligned}
$$

On a utilisé l’identité

$$
\begin{aligned}
k\binom nk
&=k\frac{n!}{k!(n-k)!}
=\frac{n!}{(k-1)!(n-1-k+1)!}\\
&=n\frac{(n-1)!}{(k-1)!(n-1-(k-1))!}
=n\binom{n-1}{k-1},
\end{aligned}
$$

puis le changement d’indice $i=k-1$, et enfin le binôme de Newton au rang $n-1$ (remarque 3.2).

**Moment d’ordre deux :** on décompose $k^2=(k-1+1)k=(k-1)k+k$ :

$$
\begin{aligned}
\mathbb E(X^2)
&=\sum_{k=0}^n k^2\mathbb P(X=k)\\
&=\sum_{k=2}^n(k-1)k\binom nk p^k(1-p)^{n-k}
+\sum_{k=1}^n k\mathbb P(X=k).
\end{aligned}
$$

Le second terme est $\mathbb E(X)=np$. Pour le premier, on utilise deux fois l’identité précédente :

$$
\begin{aligned}
&\sum_{k=2}^n(k-1)n\binom{n-1}{k-1}p^k(1-p)^{n-k}\\
&\quad=n\sum_{k=2}^n(n-1)\binom{n-2}{k-2}p^k(1-p)^{n-k}\\
&\quad=n(n-1)\sum_{j=0}^{n-2}\binom{n-2}{j}p^{j+2}(1-p)^{n-2-j}\\
&\quad=n(n-1)p^2\sum_{j=0}^{n-2}\binom{n-2}{j}p^j(1-p)^{n-2-j}\\
&\quad=n^2p^2-np^2.
\end{aligned}
$$

On a reconnu le binôme de Newton au rang $n-2$. Donc

$$
\mathbb E(X^2)=n^2p^2-np^2+np,
$$

et

$$
\mathbb V(X)=n^2p^2-np^2+np-(np)^2
=np(-p+1)=np(1-p).
$$

> **Coquille de la source, page 5.** La ligne donnant $\mathbb E(X^2)$ perd le $n$ du terme $n^2p^2$ et affiche un exposant $2$ isolé. Il est rétabli ci-dessus. Les calculs avec $n-1$ et $n-2$ concernent respectivement $n\geq1$ et $n\geq2$ ; les cas $n=0,1$ se vérifient directement.

## 4. Loi géométrique de paramètre $p\in]0,1]$

Comme les lois binomiales, les lois géométriques sont associées à des répétitions indépendantes d’une expérience de Bernoulli. La différence est que la variable compte le **rang du premier succès**. Pour le pile ou face, avec « pile » comme succès, $X$ compte le nombre d’essais nécessaires pour obtenir le premier pile. Le paramètre $p$ est celui de l’expérience de Bernoulli sous-jacente.

### Définition 4.1

Soient $(\Omega,\mathbb P)$ un espace de probabilité, $p\in]0,1]$ et $X$ une v.a.r. discrète telle que $X(\Omega)=\mathbb N^*$. On dit que $X$ suit une **loi géométrique de paramètre $p$**, notée $X\sim\mathcal G(p)$, si

$$
\forall k\in\mathbb N^*,\qquad\mathbb P(X=k)=p(1-p)^{k-1}.
$$

Pour que le premier succès ait lieu à la $k$-ième répétition, il faut d’abord $k-1$ échecs, d’où $(1-p)^{k-1}$, puis un succès, d’où $p$. L’ordre compte, contrairement à la loi binomiale : il n’y a donc pas de coefficient binomial.

### Remarque 4.1

On exclut $p=0$, car on aurait alors $\mathbb P(X=k)=0$ pour tout $k\in\mathbb N^*$ ; la propriété 2 de la définition d’une probabilité ne serait pas satisfaite.

Pour $p\in]0,1]$ et $n\in\mathbb N^*$, on reconnaît une somme géométrique de raison $1-p$ :

$$
\sum_{k=1}^n\mathbb P(X=k)
=\sum_{k=1}^n p(1-p)^{k-1}
=p\frac{1-(1-p)^n}{1-(1-p)}
=1-(1-p)^n.
$$

Puisque $1-p\in[0,1[$, on retrouve bien $\sum_{k=1}^{+\infty}\mathbb P(X=k)=1$.

### Exemple 4.1

1. On lance une pièce équilibrée. Quelle est la probabilité d’obtenir pile pour la première fois au cinquième lancer ?
2. Une urne contient dix boules blanches et trois boules noires. On effectue des tirages successifs avec remise. Quelle est la probabilité de tirer une boule noire pour la première fois au huitième tirage ?

### Proposition 4.1

Si $p\in]0,1]$ et $X\sim\mathcal G(p)$, alors

$$
\mathbb E(X)=\frac1p,
\qquad\mathbb V(X)=\frac{1-p}{p^2}.
$$

### Démonstration de la proposition 4.1

On dérive la série entière géométrique

$$
\sum_{k=0}^{+\infty}x^k=\frac1{1-x},\qquad x\in]0,1[,
$$

pour obtenir

$$
\sum_{k=1}^{+\infty}kx^{k-1}=\frac1{(1-x)^2}.
$$

> **Précision sur le rappel de la source, page 6.** Le PDF affirme qu’une série entière « CVN sur son disque ouvert de convergence ». La convergence normale est assurée sur tout disque fermé de rayon strictement inférieur au rayon de convergence, ici $R=1$. Ce résultat local permet de dériver terme à terme à l’intérieur du disque ; la convergence normale sur le disque ouvert entier n’est pas garantie.

On en déduit l’espérance :

$$
\mathbb E(X)=\sum_{k=1}^{+\infty}k\mathbb P(X=k)
=\sum_{k=1}^{+\infty}kp(1-p)^{k-1}
=p\frac1{(1-(1-p))^2}=\frac1p.
$$

Pour la variance, on dérive une deuxième fois la série entière géométrique :

$$
\sum_{k=2}^{+\infty}k(k-1)x^{k-2}=\frac2{(1-x)^3}.
$$

Une série entière a le même rayon de convergence que toutes ses séries dérivées. En décomposant $k^2=k(k-1)+k$,

$$
\begin{aligned}
\mathbb E(X^2)
&=\sum_{k=1}^{+\infty}k^2\mathbb P(X=k)\\
&=\sum_{k=1}^{+\infty}k(k-1)p(1-p)^{k-1}
+\sum_{k=1}^{+\infty}kp(1-p)^{k-1}\\
&=p(1-p)\sum_{k=2}^{+\infty}k(k-1)(1-p)^{k-2}+\mathbb E(X)\\
&=p(1-p)\frac2{(1-(1-p))^3}+\frac1p\\
&=\frac{2(1-p)}{p^2}+\frac1p.
\end{aligned}
$$

D’où

$$
\begin{aligned}
\mathbb V(X)
&=\mathbb E(X^2)-\mathbb E(X)^2\\
&=\frac{2(1-p)}{p^2}+\frac1p-\frac1{p^2}
=\frac{2-2p+p-1}{p^2}
=\frac{1-p}{p^2}.
\end{aligned}
$$

> **Précision d’indice et de bord.** Dans la somme contenant $(1-p)^{k-2}$, la source commence à $k=1$. Le terme de coefficient $k(k-1)=0$ est omis ici pour éviter une puissance négative de zéro lorsque $p=1$. Dans ce cas, $X=1$ presque sûrement, et les mêmes formules donnent directement l’espérance $1$ et la variance $0$.

## 5. Loi de Poisson de paramètre $\lambda>0$

Les lois de Poisson interviennent pour compter les occurrences d’un « événement rare ».

La source propose l’exemple du nombre de clients entrant dans un magasin entre 16 h et 17 h, lorsqu’un nouveau client arrive en moyenne toutes les dix minutes. Elle le modélise par une loi de Poisson. Le paramètre représente le nombre moyen d’occurrences sur l’intervalle considéré.

> **Erreur numérique de la source, page 7.** Le paramètre annoncé est « $1/6$ ($=1$ heure/$10$ minutes) ». Or $60/10=6$ : pour une heure, le paramètre correspondant à cette moyenne est $\lambda=6$. La moyenne seule ne suffit pas à imposer un modèle de Poisson ; il s’agit ici du modèle proposé par la fiche.

### Définition 5.1

Soient $(\Omega,\mathbb P)$ un espace de probabilité, $\lambda>0$ et $X$ une v.a.r. discrète telle que $X(\Omega)=\mathbb N$. On dit que $X$ suit une **loi de Poisson de paramètre $\lambda$**, notée $X\sim\mathcal P(\lambda)$, si

$$
\forall k\in\mathbb N,\qquad\mathbb P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}.
$$

### Remarque 5.1

On rappelle le développement de l’exponentielle :

$$
e^x=\sum_{k=0}^{+\infty}\frac{x^k}{k!}.
$$

On retrouve donc

$$
\sum_{k=0}^{+\infty}\mathbb P(X=k)
=\sum_{k=0}^{+\infty}\frac{e^{-\lambda}\lambda^k}{k!}
=e^{-\lambda}\sum_{k=0}^{+\infty}\frac{\lambda^k}{k!}
=e^{-\lambda}e^\lambda=1.
$$

### Remarque 5.2 — Lien avec la loi binomiale

Dans l’exemple des clients, une autre modélisation consisterait à donner à chaque minute une probabilité $p$ qu’un client entre : compter les arrivées sur une heure revient alors à répéter soixante expériences de Bernoulli, soit une loi $\mathcal B(60,p)$. Avec un pas de dix secondes et une probabilité $p'$, on utiliserait $\mathcal B(360,p')$.

On peut voir la loi de Poisson comme la limite de ces modélisations binomiales quand le pas de temps tend vers zéro. Plus le pas est court, plus la probabilité d’entrée est faible : $p$ dépend du nombre de pas nécessaires pour couvrir l’heure.

Plus précisément, pour $\lambda>0$ fixé, la loi $\mathcal B(N,\lambda/N)$ tend, dans le sens précisé par le calcul ci-dessous, vers une loi de Poisson lorsque $N\to+\infty$. On prend $N$ assez grand pour que $\lambda/N\leq1$.

Si $X_N\sim\mathcal B(N,\lambda/N)$, alors, pour $k\in\{0,\ldots,N\}$,

$$
\begin{aligned}
\mathbb P(X_N=k)
&=\binom Nk\left(\frac\lambda N\right)^k
\left(1-\frac\lambda N\right)^{N-k}\\
&=\frac{N!}{k!(N-k)!}\lambda^k\frac1{N^k}
\left(1-\frac\lambda N\right)^N
\left(1-\frac\lambda N\right)^{-k}\\
&=\frac{\lambda^k}{k!}\left(1-\frac\lambda N\right)^N
\left[\frac{N!}{N^k(N-k)!}\left(1-\frac\lambda N\right)^{-k}\right].
\end{aligned}
$$

Comme $\ln(1+x)\sim x$ lorsque $x\to0$,

$$
\lim_{N\to+\infty}\left(1-\frac\lambda N\right)^N
=\lim_{N\to+\infty}\exp\left(N\ln\left(1-\frac\lambda N\right)\right)
=e^{-\lambda}.
$$

D’autre part, pour $k$ fixé, $N-k\sim N$ et

$$
\begin{aligned}
\lim_{N\to+\infty}\frac{N!}{N^k(N-k)!}
\left(1-\frac\lambda N\right)^{-k}
&=\lim_{N\to+\infty}\frac{N(N-1)\cdots(N-k+1)}{N^k}\\
&=1.
\end{aligned}
$$

On retrouve ainsi l’expression de la loi de Poisson :

$$
\lim_{N\to+\infty}\mathbb P(X_N=k)=\frac{\lambda^k}{k!}e^{-\lambda}.
$$

> **Coquille de la source, page 8.** Dans le facteur entre crochets, puis dans la limite suivante, le PDF remplace $\lambda$ par $k$ et écrit $(1-k/N)^{-k}$. Le facteur correct est $(1-\lambda/N)^{-k}$, comme à la ligne précédente ; sa limite reste $1$. L’indice $N$ de $X_N$ est ajouté pour expliciter que la loi de la variable dépend de $N$.

### Exercice 5.1

1. Une entreprise constate en moyenne trois accidents du travail par an. Son effectif étant relativement élevé, on utilise une loi de Poisson pour modéliser leur nombre. Quelle est la probabilité que cinq accidents du travail aient lieu dans la même année ?
2. Dans le parking d’un centre commercial, il arrive en moyenne 120 voitures par heure les jours de soldes. Calculer la probabilité de voir quatre voitures arriver en une minute.

### Remarque 5.3

Le premier exercice précise que l’entreprise a un grand nombre d’employés : c’est ce qui motive le choix de modélisation proposé. Si elle n’avait que vingt employés et trois accidents par an, la fiche propose de modéliser chaque employé par une probabilité $3/20$ d’avoir un accident dans l’année, et d’utiliser une loi binomiale. Pour un effectif très grand, elle propose une loi de Poisson plutôt qu’une binomiale dont le paramètre de succès serait très proche de zéro. C’est dans ce sens que l’expression « événement rare » est employée.

### Proposition 5.1

Si $\lambda>0$ et $X\sim\mathcal P(\lambda)$, alors

$$
\mathbb E(X)=\lambda,
\qquad\mathbb V(X)=\lambda.
$$

### Démonstration de la proposition 5.1

**Espérance :**

$$
\begin{aligned}
\mathbb E(X)
&=\sum_{k=0}^{+\infty}k\frac{\lambda^k}{k!}e^{-\lambda}
=e^{-\lambda}\sum_{k=1}^{+\infty}\frac{\lambda^k}{(k-1)!}\\
&=e^{-\lambda}\sum_{j=0}^{+\infty}\lambda\frac{\lambda^j}{j!}
=e^{-\lambda}\lambda e^\lambda=\lambda.
\end{aligned}
$$

**Variance :** on commence par $\mathbb E(X^2)$ en écrivant $k^2=k(k-1)+k$ :

$$
\begin{aligned}
\mathbb E(X^2)
&=\sum_{k=0}^{+\infty}k^2\frac{\lambda^k}{k!}e^{-\lambda}\\
&=\sum_{k=2}^{+\infty}k(k-1)\frac{\lambda^k}{k!}e^{-\lambda}
+\sum_{k=0}^{+\infty}k\frac{\lambda^k}{k!}e^{-\lambda}\\
&=e^{-\lambda}\lambda^2\sum_{k=2}^{+\infty}\frac{\lambda^{k-2}}{(k-2)!}+\mathbb E(X)\\
&=e^{-\lambda}\lambda^2 e^\lambda+\lambda
=\lambda^2+\lambda.
\end{aligned}
$$

Donc

$$
\mathbb V(X)=\mathbb E(X^2)-\mathbb E(X)^2
=\lambda^2+\lambda-\lambda^2=\lambda.
$$
