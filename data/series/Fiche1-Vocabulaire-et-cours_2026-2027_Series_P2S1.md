# Fiche 1 : Vocabulaire et questions de cours

CC1 Séries, jeudi 15 octobre 2026. Notation : $S_n=\sum_{k=0}^{n}u_k$ la somme partielle, $S$ la somme, $R_n=S-S_n$ le reste.

## Définitions

- $\sum u_n$ **converge** si la suite $(S_n)$ a une limite finie $S$. Le reste $R_n=\sum_{k\ge n+1}u_k$ n'existe que si la série converge, et alors $R_n\to 0$.
- **Condition nécessaire** : $\sum u_n$ converge $\Rightarrow u_n\to 0$. Si $u_n\not\to 0$, la série **diverge grossièrement**.
- **Absolument convergente** : $\sum |u_n|$ converge. Cela entraîne la convergence de $\sum u_n$.
- **Semi-convergente** : $\sum u_n$ converge mais $\sum |u_n|$ diverge. Exemple : $\sum \frac{(-1)^n}{n}$.

## Opérations

- $\sum u_n$ et $\sum \lambda u_n$ ($\lambda\ne 0$) ont même nature.
- Convergente + convergente = convergente.
- Convergente + divergente = divergente.
- Divergente + divergente : on ne peut rien dire. Contre-exemples : $\frac1n+\frac1n$ diverge, mais $\frac1n-\frac1n$ converge.
- Dans $\mathbb{C}$ : $\sum u_n$ converge $\iff \sum \mathrm{Re}(u_n)$ et $\sum \mathrm{Im}(u_n)$ convergent.

## Critère de Cauchy

$\sum u_n$ converge si et seulement si

$$\forall \varepsilon>0,\ \exists n_0,\ \forall n\ge n_0,\ \forall p\in\mathbb{N},\ \left|\sum_{k=n+1}^{n+p}u_k\right|\le\varepsilon$$

Application à la série harmonique : $\sum_{k=n+1}^{2n}\frac1k\ge n\cdot\frac{1}{2n}=\frac12$, le critère n'est pas vérifié, donc $\sum\frac1n$ diverge.

## Piège

$u_n\to 0$ ne prouve rien : $\frac1n\to 0$ et pourtant $\sum\frac1n$ diverge.

## Démonstrations à savoir refaire

Elles sont tombées en exercice 1 des DS1.

1. **Convergence implique $u_n\to0$.** On a $u_n=S_n-S_{n-1}$. Si $S_n\to S$, alors $u_n\to S-S=0$.
2. **Comparaison par inégalité.** Soit $0\le u_n\le v_n$ avec $\sum v_n$ convergente. Alors $S_n\le T_n\le \sum_{k\ge0} v_k$. La suite $(S_n)$ est croissante et majorée, donc elle converge.
3. **Domination.** Soit $u_n=O(v_n)$, termes positifs, $\sum v_n$ convergente. Il existe $M>0$ et $n_0$ tels que $u_n\le Mv_n$ pour $n\ge n_0$. Or $\sum Mv_n$ converge. Par comparaison, $\sum u_n$ converge.
4. **Convergence absolue implique convergence.** Pour tous $n,p$ : $\left|\sum_{k=n+1}^{n+p}u_k\right|\le\sum_{k=n+1}^{n+p}|u_k|\le\varepsilon$ dès que $n\ge n_0$, car $\sum|u_n|$ vérifie le critère de Cauchy. Donc $\sum u_n$ vérifie le critère de Cauchy.
