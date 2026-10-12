---
source: "PREING2-S1/Series/2627/Annales-20261012/2025-2026/CC2_Series_2526_corrigé.pdf"
pages: 4
annee: 2025-2026
mise_a_disposition: 2026-2027
transcription: lecture visuelle intégrale et comparaison au texte natif
transcription_date: 2026-10-12
---

# Séries — Contrôle continu 2, corrigé (2025–2026)

CY Tech — PréIng 2, semestre 1 — jeudi 20 novembre. Pages 1 à 4. Les réponses proviennent du corrigé fourni.

**Consignes.** Durée : 90 minutes. Documents et supports électroniques interdits. Quatre exercices indépendants. Barème indicatif. La qualité de la rédaction et la rigueur des justifications sont prises en compte.

## Exercice 1 (3 points)

1. Énoncer la définition de la convergence simple et uniforme d’une suite de fonctions.
2. Soit la suite $(f_n)$ définie sur $\mathbb R_+$ par
   $$f_n(x)=\frac{n(x^3+x)e^{-x}}{nx+1}.$$
   Étudier sa convergence simple et uniforme sur $\mathbb R_+$.

### Réponse (page 1)

1. Voir cours. Le corrigé ne développe pas les définitions.

2. Fixons $x\in[0,+\infty[$. Si $x=0$, $f_n(0)=0$. Si $x>0$,
$$f_n(x)\sim\frac{n(x^2+1)e^{-x}}n=(x^2+1)e^{-x}.$$
Ainsi $(f_n)$ converge simplement vers
$$f(x)=\begin{cases}0,&x=0,\\(x^2+1)e^{-x},&x>0.\end{cases}$$
Toutes les $f_n$ sont continues sur $\mathbb R_+$, comme quotients de fonctions continues à dénominateur non nul. Or
$$\lim_{x\to0^+}f(x)=\lim_{x\to0^+}(x^2+1)e^{-x}=1\ne0=f(0).$$
La limite simple n’est pas continue en zéro. Il n’y a donc pas convergence uniforme sur $\mathbb R_+$.

> **Coquille corrigée :** dans la dernière limite, le PDF écrit $f_n(x)$ à la place de $f(x)$.

## Exercice 2 (6 points)

Pour $n\in\mathbb N^*$, on définit $f_n:\mathbb R\to\mathbb R$ par

$$\forall x\in\mathbb R,\qquad f_n(x)=\frac{2^n x}{1+n2^n x^2}.$$

1. Montrer que $(f_n)_{n\ge1}$ converge simplement sur $\mathbb R$ vers une fonction $f$ que l’on déterminera.
2. La convergence vers $f$ est-elle uniforme sur $\mathbb R$ ?
3. Montrer que $(f_n)$ converge uniformément vers $f$ sur $[a,+\infty[$ pour tout $a>0$.

### Réponse (page 2)

1. Pour $x=0$, $f_n(0)=0$. Pour $x\ne0$,
$$f_n(x)\sim\frac1{nx}\longrightarrow0.$$
La suite converge simplement sur $\mathbb R$ vers la fonction nulle.

2. Chaque $f_n$ est impaire. Sur $\mathbb R_+$,
$$f_n'(x)=\frac{2^n(1+n2^nx^2)-2^nx\,n2^{n+1}x}{(1+n2^nx^2)^2}
=\frac{2^n(1-n2^nx^2)}{(1+n2^nx^2)^2}.$$
En posant $x_n^*=\sqrt{1/(n2^n)}$, la fonction est croissante sur $[0,x_n^*]$, décroissante sur $[x_n^*,+\infty[$, et tend vers zéro en zéro et en $+\infty$. Par imparité,
$$\sup_{x\in\mathbb R}|f_n(x)|=|f_n(x_n^*)|=\frac{\sqrt{2^n}}{2\sqrt n}\longrightarrow+\infty.$$
La convergence n’est pas uniforme sur $\mathbb R$.

3. Soit $a>0$. Comme $x_n^*\to0$, on a $x_n^*\le a$ pour $n$ assez grand. Sur $[a,+\infty[$, $f_n$ est alors positive et décroissante, donc
$$\sup_{x\in[a,+\infty[}|f_n(x)|=f_n(a)=\frac{2^na}{1+n2^na^2}\sim\frac1{na}\longrightarrow0.$$
La convergence vers zéro est uniforme sur $[a,+\infty[$.

## Exercice 3 (7 points)

Pour $n\in\mathbb N^*$, on définit $\displaystyle f_n(x)=\sin\left(\frac xn\right)-x$ sur $\mathbb R$. Soient $a,b\in\mathbb R$ avec $a<b$.

1. Étudier la convergence simple de la suite des dérivées $(f_n')$ sur $[a,b]$ vers une fonction $g$ que l’on déterminera.
2. Étudier la convergence uniforme de $(f_n')$ sur $[a,b]$.
3. En déduire la convergence uniforme de $(f_n)$ sur $[a,b]$ vers une fonction $f$ que l’on déterminera.

### Réponse (pages 2–3)

1. Pour $n\ge1$, $f_n$ est dérivable sur $\mathbb R$ et
$$f_n'(x)=\frac1n\cos\frac xn-1.$$
Le cosinus étant borné, $(1/n)\cos(x/n)\to0$ pour tout $x$ fixé. La suite $(f_n')$ converge simplement sur $\mathbb R$ vers $g(x)=-1$.

2. Pour tout $x\in\mathbb R$,
$$|f_n'(x)-g(x)|=\left|\frac1n\cos\frac xn\right|\le\frac1n.$$
Ainsi $\sup_{x\in\mathbb R}|f_n'(x)-g(x)|\to0$ : convergence uniforme sur $\mathbb R$, donc aussi locale.

3. Sur tout $[a,b]\subset\mathbb R$, on applique le théorème d’interversion limite-dérivée :

- Les $f_n$ sont de classe $C^1$, comme sommes de fonctions $C^1$.
- $(f_n')$ converge uniformément sur $[a,b]$ vers $g$.
- En $a$, $\displaystyle f_n(a)=\sin(a/n)-a\longrightarrow-a$.

On en déduit que $(f_n)$ converge uniformément sur $[a,b]$ vers une fonction $f\in C^1([a,b])$, avec $f'=g=-1$. Donc $f(x)=-x+C$. Comme $f(a)=-a$, $C=0$ :
$$f(x)=-x.$$
La convergence est localement uniforme sur $\mathbb R$.

> Le corrigé écrit une fois $n\in\mathbb N$ dans la formule comportant $1/n$ ; il faut $n\in\mathbb N^*$, comme dans l’énoncé.

## Exercice 4 (4 points et 2 points bonus)

Pour $n\in\mathbb N^*$, on définit $\displaystyle f_n(x)=\frac{\cos x}{n+x}$ sur $[0,\pi]$.

1. (a) Étudier la convergence uniforme de $(f_n)$ sur $[0,\pi]$.
   (b) En déduire $\displaystyle\lim_{n\to+\infty}\int_0^\pi f_n(x)\,dx$.
2. **Bonus.** Montrer que $\displaystyle\int_0^\pi f_n(x)\,dx=o\left(\frac1n\right)$.

### Réponse (pages 3–4)

1. (a) Pour tout $x\in[0,\pi]$, $f_n(x)\to0$. De plus,
$$|f_n(x)|=\left|\frac{\cos x}{n+x}\right|\le\frac1n.$$
Le supremum tend vers zéro : la convergence est uniforme sur $[0,\pi]$.

(b) Toutes les $f_n$ sont continues sur $[0,\pi]$ ; la convergence uniforme permet l’interversion limite-intégrale :
$$\lim_{n\to+\infty}\int_0^\pi f_n(x)\,dx=\int_0^\pi0\,dx=0.$$

2. **Bonus.** Notons $I_n=\int_0^\pi f_n(x)\,dx$. Il faut montrer que $nI_n\to0$. Posons
$$h_n(x)=nf_n(x)=\frac{n\cos x}{n+x}.$$
Pour tout $x\in[0,\pi]$, $h_n(x)\to h(x)=\cos x$. De plus,
$$|h_n(x)-h(x)|=\frac{|-x\cos x|}{n+x}\le\frac\pi n.$$
La convergence est uniforme. Comme les $h_n$ sont continues, l’interversion limite-intégrale donne
$$\lim_{n\to+\infty}nI_n=\lim_{n\to+\infty}\int_0^\pi h_n(x)\,dx=\int_0^\pi\cos x\,dx=0.$$
Donc $I_n=o(1/n)$.

> La réponse du PDF renumérote les trois étapes « 1, 2, 3 » ; elles sont rattachées ici aux questions 1(a), 1(b) et 2.
