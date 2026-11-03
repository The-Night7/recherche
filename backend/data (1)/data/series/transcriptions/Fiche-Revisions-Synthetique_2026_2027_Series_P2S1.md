# Fiche de Révision Synthétique & Rigoureuse : CC1 de Séries Numériques (CY Tech / PréIng 2)

## 1. Définitions Fondamentales & Théorèmes Principaux du Cours

### Définition : Somme Partielle, Somme et Reste d'une Série

Soit $(u_n)_{n \in \mathbb{N}}$ une suite réelle ou complexe.

- **p-ième somme partielle** : pour tout $p \in \mathbb{N}$, la p-ième somme partielle $S_p$ est la somme des premiers termes jusqu'à l'indice $p$ :
  $$S_p = \sum_{k=0}^p u_k$$
- **Somme de la série** : si la suite des sommes partielles $(S_n)_{n \in \mathbb{N}}$ converge vers une limite finie $S \in \mathbb{K}$ ($\mathbb{R}$ ou $\mathbb{C}$), la série $\sum u_n$ est dite convergente, et sa somme est notée :
  $$S = \sum_{k=0}^{+\infty} u_k = \lim_{n \to +\infty} S_n = \lim_{n \to +\infty} \sum_{k=0}^n u_k$$
- **Reste d'ordre n** : si la série $\sum u_n$ converge, on définit pour tout $n \in \mathbb{N}$ le reste d'ordre $n$ par :
  $$R_n = \sum_{k=n+1}^{+\infty} u_k = S - S_n$$

> **Remarque capitale** : on ne parle du reste d'une série que dans le cas où celle-ci est convergente.

### Théorème : Condition Nécessaire de Convergence (CNC)

Si la série $\sum u_n$ converge, alors la suite du terme général $(u_n)$ tend vers 0 :

$$\sum u_n \text{ converge} \implies \lim_{n \to +\infty} u_n = 0$$

- **Divergence grossière** : on dit qu'une série $\sum u_n$ diverge grossièrement si la suite $(u_n)$ ne tend pas vers 0 ($\lim_{n \to +\infty} u_n \neq 0$ ou la limite n'existe pas).
- **Avertissement** : la réciproque est absolument fausse en général (ex. la série harmonique $\sum \frac{1}{n}$ pour laquelle $\frac{1}{n} \to 0$ mais la série diverge).

### Définitions & Théorèmes : Séries de Référence

1. **Séries géométriques** : soit $z \in \mathbb{C}$. La série géométrique $\sum z^n$ converge si et seulement si $|z| < 1$. Dans ce cas :
   $$\sum_{n=0}^{+\infty} z^n = \frac{1}{1-z}$$
2. **Séries de Riemann** : soit $\alpha \in \mathbb{R}$. La série de Riemann $\sum_{n \ge 1} \frac{1}{n^\alpha}$ converge si et seulement si $\alpha > 1$.
   - Cas particulier : pour $\alpha = 1$, $\sum_{n \ge 1} \frac{1}{n}$ est la série harmonique, qui diverge.
3. **Séries de Riemann alternées** : la série alternée $\sum_{n \ge 1} \frac{(-1)^n}{n^\alpha}$ converge si et seulement si $\alpha > 0$.

### Définition : Série Alternée

On dit qu'une série numérique $\sum_{n \in \mathbb{N}} u_n$ est **alternée** s'il existe $n_0 \in \mathbb{N}$ tel que pour tout $n \ge n_0$ :

$$u_n = (-1)^n |u_n| \quad \text{ou} \quad u_n = (-1)^{n+1} |u_n|$$

### Définitions & Théorèmes : Convergence Absolue et Semi-convergence

- **Convergence absolue** : on dit que $\sum u_n$ converge absolument (ou est absolument convergente) si la série à termes positifs $\sum |u_n|$ converge.
- **Théorème** : toute série absolument convergente est convergente :
  $$\sum |u_n| \text{ converge} \implies \sum u_n \text{ converge}$$
- **Semi-convergence** : une série qui converge mais ne converge pas absolument est dite semi-convergente (ex. $\sum_{n \ge 1} \frac{(-1)^n}{n}$, convergente d'après le critère des séries alternées mais non absolument convergente car $\sum_{n \ge 1} \frac{1}{n}$ diverge).

---

## 2. Guide de Décision et Méthodologie Pas à Pas pour Étudier $\sum u_n$

> **Conseil du Professeur** : lors d'une épreuve de CC1, ne commencez jamais une étude de série à l'aveugle. Appliquez systématiquement la grille de décision ci-dessous. Identifier le signe du terme général $u_n$ est l'étape charnière qui conditionne le choix des théorèmes autorisés.

```
                  [Terme général u_n]
                           |
                           v
              Étape 0 : lim u_n != 0 ?
                       /        \
                    OUI          NON
                    /              \
         [Divergence Grossière]   [Analyse du signe de u_n]
                                       /              \
                         Signe constant               Signe variable / alterné
                         à partir de n_0              à partir de n_0
                               |                            |
                            Étape 1                      Étape 2
                    (Majoration, Équivalent,         (TSSA, Développement
                     Règle n^alpha, d'Alembert,       Limité, Sommation
                     Cauchy)                          d'Abel)
```

### Étape 0 : Test de Divergence Grossière

- **Action** : calculer la limite du terme général $\lim_{n \to +\infty} u_n$.
- **Décision** :
  - Si $\lim_{n \to +\infty} u_n \neq 0$ ou si la limite n'existe pas $\implies$ conclure immédiatement à la **divergence grossière**.
  - Si $\lim_{n \to +\infty} u_n = 0$ $\implies$ la CNC est vérifiée (condition nécessaire mais non suffisante), poursuivre impérativement vers l'Étape 1 ou l'Étape 2.

### Étape 1 : Séries à Termes Positifs (STP) (ou de signe constant à partir d'un certain rang $n_0$)

> **Attention – Condition de signe constant** : les règles de comparaison par inégalité, par équivalents et la règle $n^\alpha$ exigent strictement que les termes conservent un signe constant (positif ou négatif) à partir d'un certain rang $n_0$. L'utilisation d'équivalents sur des séries à signe variable est une **erreur éliminatoire** au CC1.

**Comparaison par inégalité / majoration**

Soient $0 \leq u_n \leq v_n$ pour tout $n \geq n_0$.
- Si $\sum v_n$ converge, alors $\sum u_n$ converge.
- Si $\sum u_n$ diverge, alors $\sum v_n$ diverge.

**Comparaison par équivalents**

Si $u_n \ge 0$, $v_n \ge 0$ (ou $u_n \le 0$, $v_n \le 0$) et $u_n \sim v_n$ au voisinage de $+\infty$ : les séries $\sum u_n$ et $\sum v_n$ sont de même nature.

**Règle de $n^\alpha$ (ou Lemme de Riemann)**

- Si $\lim_{n \to +\infty} n^\alpha u_n = 0$ avec $\alpha > 1$ $\implies$ $\sum u_n$ converge.
- Si $\lim_{n \to +\infty} n^\alpha u_n = +\infty$ (ou $\ell > 0$) avec $\alpha \leq 1$ $\implies$ $\sum u_n$ diverge.

**Règle de d'Alembert**

Si $u_n \neq 0$ à partir d'un certain rang et $\lim_{n \to +\infty} \left|\frac{u_{n+1}}{u_n}\right| = \ell \in \overline{\mathbb{R}_+}$ :
- Si $\ell < 1$ $\implies$ $\sum u_n$ converge absolument (donc converge).
- Si $\ell > 1$ ou $\ell = +\infty$ $\implies$ $\sum u_n$ diverge grossièrement.
- Si $\ell = 1$ $\implies$ cas douteux, la règle ne permet pas de conclure (utiliser une autre méthode).

**Règle de Cauchy**

Si $\lim_{n \to +\infty} \sqrt[n]{|u_n|} = \ell \in \overline{\mathbb{R}_+}$ :
- Si $\ell < 1$ $\implies$ $\sum u_n$ converge absolument.
- Si $\ell > 1$ ou $\ell = +\infty$ $\implies$ $\sum u_n$ diverge grossièrement.
- Si $\ell = 1$ $\implies$ cas douteux, la règle ne permet pas de conclure.

> **Conseil d'application d'Alembert vs. Cauchy**
> - Utilisez la règle de d'Alembert prioritairement en présence de factorielles ($n!$) ou de puissances de constantes ($a^n$).
> - Utilisez la règle de Cauchy prioritairement lorsque le terme général contient des puissances $n$-ièmes de suites ($(a_n)^n$ ou $a_n^{P(n)}$).

### Étape 2 : Séries Alternées & Termes de Signe Non Constant

**Critère Spécial des Séries Alternées (CSSA / TSSA)**

Pour une série de la forme $\sum (-1)^n a_n$ (ou $\sum (-1)^{n+1} a_n$) avec $a_n \geq 0$ pour tout $n \ge n_0$ :
1. Prouver rigoureusement que la suite $(a_n)_{n \ge n_0}$ est monotone décroissante.
2. Vérifier que $\lim_{n \to +\infty} a_n = 0$.

**Conclusion** : la série $\sum (-1)^n a_n$ converge.

**Majoration et signe du reste** : la somme $S$ vérifie $S_{2n+1} \le S \le S_{2n}$, et le reste vérifie $|R_n| \leq a_{n+1}$, $R_n$ étant du signe du premier terme négligé $(-1)^{n+1} a_{n+1}$.

**Méthode du Développement Limité (DL) au terme général**

*Indication* : indispensable lorsque la monotonie de $a_n$ est difficile à établir ou lorsque $u_n$ présente un comportement oscillant complexe.

*Principe et profondeur du développement* : on pousse le DL du terme général $u_n$ jusqu'à obtenir un reste négligeable d'ordre $o\left(\frac{1}{n}\right)$ ou $\mathcal{O}\left(\frac{1}{n^{3/2}}\right)$ sous la forme $u_n = b_n + c_n + d_n$ où :
- $b_n = \frac{(-1)^n}{n^\alpha}$ ($\alpha > 0$) est le terme principal alterné (convergent par le TSSA).
- $c_n = \frac{\lambda}{n^\beta}$ ($\beta \in \mathbb{R}$) est un terme correctif de signe constant (Riemann).
- $d_n = \mathcal{O}\left(\frac{1}{n^\gamma}\right)$ avec $\gamma > 1$ est un reste absolument convergent.

**Exemple classique du cours** : pour $u_n = \frac{(-1)^n}{\sqrt{n} + (-1)^n}$, un équivalent simple donne $u_n \sim \frac{(-1)^n}{\sqrt{n}}$ (dont la série converge). Pourtant, en poussant le DL :

$$u_n = \frac{(-1)^n}{\sqrt{n}\left(1 + \frac{(-1)^n}{\sqrt{n}}\right)} = \frac{(-1)^n}{\sqrt{n}}\left(1 - \frac{(-1)^n}{\sqrt{n}} + \mathcal{O}\left(\frac{1}{n}\right)\right) = \frac{(-1)^n}{\sqrt{n}} - \frac{1}{n} + \mathcal{O}\left(\frac{1}{n^{3/2}}\right)$$

La série $\sum \frac{(-1)^n}{\sqrt{n}}$ converge (TSSA), $\sum \mathcal{O}\left(\frac{1}{n^{3/2}}\right)$ converge (Riemann $\alpha=3/2 > 1$), mais $\sum -\frac{1}{n}$ diverge (série harmonique). La série $\sum u_n$ diverge donc, illustrant l'échec mortel de l'équivalent sur un signe non constant !

**Sommation / Critère d'Abel**

Pour une série de la forme $\sum a_n b_n$ :
1. $(a_n)$ est une suite à termes positifs, décroissante et de limite nulle ($a_n \downarrow 0$).
2. La suite des sommes partielles $B_n = \sum_{k=0}^n b_k$ est bornée ($\exists M > 0, \forall n, |B_n| \le M$).

**Conclusion** : la série $\sum a_n b_n$ converge.

---

## 3. Pièges Classiques d'Examen & Erreurs à Éviter

| Erreur / Piège classique | Règle exacte & Contre-exemple du cours |
|---|---|
| **Piège de la réciproque de la CNC**<br>Affirmer que $\lim_{n \to +\infty} u_n = 0 \implies \sum u_n$ converge. | La condition $\lim u_n = 0$ est nécessaire mais absolument pas suffisante.<br>*Contre-exemple* : la série harmonique $u_n = \frac{1}{n}$ vérifie $\lim \frac{1}{n} = 0$, mais la série $\sum \frac{1}{n}$ diverge vers $+\infty$. |
| **Piège des équivalents sur signe non constant**<br>Appliquer $u_n \sim v_n \implies \sum u_n$ et $\sum v_n$ de même nature pour des séries alternées. | Le théorème d'équivalence est strictement réservé aux séries à termes de signe constant à partir d'un certain rang.<br>*Contre-exemple* : $u_n = \frac{(-1)^n}{\sqrt{n}} + \frac{1}{n} \sim \frac{(-1)^n}{\sqrt{n}} = v_n$. La série $\sum v_n$ converge (Riemann alternée $\alpha=1/2>0$), mais $\sum u_n$ diverge à cause du terme $\sum \frac{1}{n}$. |
| **Cas douteux d'Alembert / Cauchy ($\ell = 1$)**<br>Conclure à la convergence ou la divergence lorsque $\ell = 1$. | Lorsque $\ell = 1$, les règles de d'Alembert et Cauchy ne fournissent aucune information.<br>*Contre-exemple* : pour la série de Riemann $\sum \frac{1}{n^\alpha}$, $\left\lvert\frac{u_{n+1}}{u_n}\right\rvert \to 1$ pour tout $\alpha$, alors qu'elle converge si $\alpha > 1$ et diverge si $\alpha \le 1$. |
| **Oubli de la monotonie dans le TSSA**<br>Invoquer le TSSA avec uniquement $u_n = (-1)^n a_n$ et $\lim a_n = 0$. | La décroissance de la suite $(a_n)$ est une hypothèse fondamentale du TSSA. Si $(a_n)$ n'est pas décroissante, la série peut diverger même si $a_n \to 0$. |

---

## 4. Méthodologie Complète : Calcul de Sommes de Séries par Télescopage

> **Règle préalable indispensable** : ne calculez JAMAIS la somme d'une série par télescopage sans avoir au préalable démontré sa convergence ! Manipuler des limites de sommes partielles sans garantie de convergence expose à des indéterminations mathématiques graves.

Pour calculer la somme exacte $S = \sum_{n=n_0}^{+\infty} u_n$ d'une série télescopique (fractions rationnelles) :

### Étape 1 : Décomposition en Éléments Simples (DES)

Décomposer la fraction rationnelle $u_k = \frac{P(k)}{Q(k)}$ dans $\mathbb{R}(X)$ en éléments simples afin d'exprimer $u_k$ sous forme d'une combinaison linéaire de termes de la forme $\frac{\lambda}{k+c}$.

*Exemple* : recherche de $a, b, c$ tels que $u_k = \frac{a}{k-1} + \frac{b}{k+1} + \frac{c}{k+2}$.

### Étape 2 : Écriture rigoureuse de la somme partielle $S_n = \sum_{k=n_0}^n u_k$

Scinder la somme partielle $S_n$ selon chaque sous-fraction et effectuer des changements d'indices explicites pour ramener chaque terme au même dénominateur simple $\frac{1}{k}$.

### Étape 3 : Changement d'indice, réalignement et simplification

Isoler les premiers et derniers termes non simplifiés dans des crochets explicites, et vérifier l'annulation algébrique de la partie centrale :

$$\frac{1}{2} \sum_{k=1}^{n-1} \frac{1}{k} = \frac{1}{2} \left( 1 + \frac{1}{2} + \frac{1}{3} + \sum_{k=4}^{n-1} \frac{1}{k} \right)$$

$$\frac{3}{2} \sum_{k=3}^{n+1} \frac{1}{k} = \frac{3}{2} \left( \frac{1}{3} + \sum_{k=4}^{n-1} \frac{1}{k} + \frac{1}{n} + \frac{1}{n+1} \right)$$

$$-2 \sum_{k=4}^{n+2} \frac{1}{k} = -2 \left( \sum_{k=4}^{n-1} \frac{1}{k} + \frac{1}{n} + \frac{1}{n+1} + \frac{1}{n+2} \right)$$

La somme des coefficients centraux s'annule : $\left(\frac{1}{2} + \frac{3}{2} - 2\right) \sum_{k=4}^{n-1} \frac{1}{k} = 0 \cdot \sum_{k=4}^{n-1} \frac{1}{k} = 0$.

Il reste : $S_n = C + \mathcal{O}\left(\frac{1}{n}\right)$.

### Étape 4 : Passage à la limite ($n \to +\infty$)

Calculer la limite de la somme partielle $S_n$ lorsque $n$ tend vers $+\infty$ pour obtenir la somme exacte :

$$S = \lim_{n \to +\infty} S_n = C$$

---

## 5. Exercices Types d'Annales Résolus Étape par Étape

### Exercice 1 : Définition, d'Alembert & étude de série (CC1 2025/2026, Ex 1)

**Consigne :**
1. Donner la définition de série alternée.
2. (a) Énoncer la règle de d'Alembert pour les séries numériques à termes quelconques. (b) Étudier la nature de la série $\sum_{n \ge 1} \frac{(-2)^n}{n(n+1)}$.

**Rédaction étape par étape :**

1. **Définition de série alternée** : on dit qu'une série numérique $\sum_{n \in \mathbb{N}} u_n$ est alternée s'il existe $n_0 \in \mathbb{N}$ tel que pour tout $n \ge n_0$ :
   $$u_n = (-1)^n |u_n| \quad \text{ou} \quad u_n = (-1)^{n+1} |u_n|$$

2. (a) **Énoncé de la règle de d'Alembert** : soit $\sum_{n \in \mathbb{N}} u_n$ une série numérique telle que $u_n \neq 0$ à partir d'un certain rang.
   - Si $\lim_{n \to +\infty} \left|\frac{u_{n+1}}{u_n}\right| = \ell < 1$, alors la série $\sum u_n$ converge (absolument).
   - Si $\lim_{n \to +\infty} \left|\frac{u_{n+1}}{u_n}\right| = \ell > 1$ ou $+\infty$, alors la série $\sum u_n$ diverge grossièrement.
   - Si $\lim_{n \to +\infty} \left|\frac{u_{n+1}}{u_n}\right| = 1$, le test est inconclusif.

   (b) **Étude de la série** $\sum_{n \ge 1} \frac{(-2)^n}{n(n+1)}$ :
   - *Non-nullité* : pour tout $n \ge 1$, $u_n = \frac{(-2)^n}{n(n+1)} \neq 0$.
   - *Calcul du rapport* :
     $$\left|\frac{u_{n+1}}{u_n}\right| = \frac{2^{n+1}}{(n+1)(n+2)} \times \frac{n(n+1)}{2^n} = 2 \times \frac{n}{n+2}$$
   - *Limite* : $\lim_{n \to +\infty} \left|\frac{u_{n+1}}{u_n}\right| = \lim_{n \to +\infty} 2 \frac{n}{n+2} = 2 = \ell$
   - *Conclusion* : comme $\ell = 2 > 1$, d'après la règle de d'Alembert, la série $\sum_{n \ge 1} \frac{(-2)^n}{n(n+1)}$ **diverge grossièrement**.

### Exercice 2 : Panel complet d'analyse de convergence (CC1 2025/2026, Ex 2)

**Consigne :** étudier la nature des séries numériques suivantes :

1. $\sum_{n \ge 1} \frac{n^2 - 1}{(n+1)^2 \sqrt{n}}$
2. $\sum_{n \ge 1} \frac{n^{\sqrt{n}}}{\sqrt{n}^n}$
3. $\sum_{n \ge 1} \frac{\ln(n)}{n^2 + n}$
4. $\sum_{n \ge 1} (-1)^n \ln\left(1 + \frac{1}{n}\right)$

**Rédaction étape par étape :**

#### Question 1 : $\sum_{n \ge 1} \frac{n^2 - 1}{(n+1)^2 \sqrt{n}}$

1. **Signe** : posons $u_n = \frac{n^2 - 1}{(n+1)^2 \sqrt{n}}$. Pour tout $n \ge 1$, $u_n \ge 0$ (série à termes positifs).
2. **Recherche d'équivalent** :
   $$u_n = \frac{n^2\left(1 - \frac{1}{n^2}\right)}{n^2\left(1 + \frac{1}{n}\right)^2 \sqrt{n}} \sim_{+\infty} \frac{n^2}{n^2 \sqrt{n}} = \frac{1}{\sqrt{n}} = \frac{1}{n^{1/2}}$$
3. **Référence** : la série $\sum_{n \ge 1} \frac{1}{n^{1/2}}$ est une série de Riemann de paramètre $\alpha = \frac{1}{2}$.
4. **Conclusion** : comme $\alpha = \frac{1}{2} \le 1$, la série de Riemann $\sum_{n \ge 1} \frac{1}{\sqrt{n}}$ diverge. Les termes étant positifs, par le théorème de comparaison par équivalents, la série $\sum_{n \ge 1} \frac{n^2 - 1}{(n+1)^2 \sqrt{n}}$ **diverge**.

#### Question 2 : $\sum_{n \ge 1} \frac{n^{\sqrt{n}}}{\sqrt{n}^n}$

1. **Signe** : posons $u_n = \frac{n^{\sqrt{n}}}{\sqrt{n}^n} > 0$. Présence d'une puissance $n$-ième $\implies$ règle de Cauchy.
2. **Application de la règle de Cauchy** :
   $$\sqrt[n]{|u_n|} = (u_n)^{1/n} = \frac{(n^{\sqrt{n}})^{1/n}}{(\sqrt{n}^n)^{1/n}} = \frac{n^{\frac{\sqrt{n}}{n}}}{\sqrt{n}} = \frac{n^{\frac{1}{\sqrt{n}}}}{\sqrt{n}} = \frac{\exp\left(\frac{\ln n}{\sqrt{n}}\right)}{\sqrt{n}}$$
3. **Calcul de limite** : par croissances comparées, $\lim_{n \to +\infty} \frac{\ln n}{\sqrt{n}} = 0$, donc $\lim_{n \to +\infty} \exp\left(\frac{\ln n}{\sqrt{n}}\right) = e^0 = 1$. D'où :
   $$\lim_{n \to +\infty} \sqrt[n]{|u_n|} = \lim_{n \to +\infty} \frac{1}{\sqrt{n}} = 0 = \ell$$
4. **Conclusion** : comme $\ell = 0 < 1$, d'après la règle de Cauchy, la série $\sum_{n \ge 1} \frac{n^{\sqrt{n}}}{\sqrt{n}^n}$ **converge**.

#### Question 3 : $\sum_{n \ge 1} \frac{\ln(n)}{n^2 + n}$

1. **Signe** : posons $u_n = \frac{\ln(n)}{n^2 + n} \ge 0$ pour tout $n \ge 1$.
2. **Méthode du lemme de Riemann (règle de $n^\alpha$)** : choisissons $\alpha = \frac{3}{2} > 1$. Formons le produit $n^{\alpha} u_n$ :
   $$n^{3/2} u_n = n^{3/2} \frac{\ln n}{n^2 + n} = \frac{n^{3/2} \ln n}{n^2\left(1 + \frac{1}{n}\right)} = \frac{\ln n}{n^{1/2}\left(1 + \frac{1}{n}\right)}$$
3. **Calcul de limite** : par croissances comparées, $\lim_{n \to +\infty} \frac{\ln n}{\sqrt{n}} = 0$, d'où :
   $$\lim_{n \to +\infty} n^{3/2} u_n = 0$$
4. **Conclusion** : puisque $\lim_{n \to +\infty} n^{3/2} u_n = 0$ avec $\alpha = \frac{3}{2} > 1$, la règle de $n^\alpha$ garantit que la série $\sum_{n \ge 1} \frac{\ln(n)}{n^2 + n}$ **converge**.

> **Conseil du Professeur** : pour $\sum \frac{\ln n}{n^2+n}$, on pouvait aussi observer que $u_n \sim \frac{\ln n}{n^2}$ (série de Bertrand avec $\alpha=2 > 1$, donc convergente), mais l'utilisation de la règle de $n^{3/2}$ évite d'avoir à réciter la théorie des séries de Bertrand hors-programme.

#### Question 4 : $\sum_{n \ge 1} (-1)^n \ln\left(1 + \frac{1}{n}\right)$

1. **Nature alternée** : pour tout $n \ge 1$, $\ln\left(1 + \frac{1}{n}\right) \ge 0$. La série s'écrit $u_n = (-1)^n |u_n|$ avec $|u_n| = \ln\left(1 + \frac{1}{n}\right)$ : il s'agit d'une série alternée.
2. **Décroissance de $(|u_n|)$** : la suite $\left(1 + \frac{1}{n}\right)_{n \ge 1}$ est strictement décroissante et à valeurs dans $]1, 2]$. La fonction $x \mapsto \ln(x)$ étant strictement croissante sur $]0, +\infty[$, la suite composée $(|u_n|)_{n \ge 1} = \left(\ln\left(1 + \frac{1}{n}\right)\right)_{n \ge 1}$ est monotone décroissante.
3. **Limite nulle** : $\lim_{n \to +\infty} |u_n| = \lim_{n \to +\infty} \ln\left(1 + \frac{1}{n}\right) = \ln(1) = 0$
4. **Conclusion** : les hypothèses du TSSA étant toutes satisfaites, la série $\sum_{n \ge 1} (-1)^n \ln\left(1 + \frac{1}{n}\right)$ **converge**.

### Exercice 3 : Calcul de somme par DES et télescopage (CC1 2025/2026, Ex 3)

**Consigne :** soit $u_n = \frac{3n}{(n^2-1)(n+2)}$ pour tout $n \ge 2$.

1. Montrer que la série $\sum_{n \ge 2} u_n$ converge.
2. Calculer sa somme $\sum_{n=2}^{+\infty} u_n$.

**Rédaction étape par étape :**

1. **Preuve de la convergence** :
   - Pour $n \ge 2$, $u_n > 0$.
   - Recherche d'un équivalent : $u_n = \frac{3n}{(n^2-1)(n+2)} \sim_{+\infty} \frac{3n}{n^3} = \frac{3}{n^2}$
   - La série $\sum_{n \ge 2} \frac{3}{n^2}$ est une série de Riemann convergente ($\alpha = 2 > 1$).
   - Les termes étant strictement positifs, le théorème de comparaison par équivalents garantit que la série $\sum_{n \ge 2} u_n$ converge.

2. **Décomposition en éléments simples (DES)** : soit $k \ge 2$. Factorisons le dénominateur : $(k^2-1)(k+2) = (k-1)(k+1)(k+2)$. Cherchons $a, b, c \in \mathbb{R}$ tels que :
   $$u_k = \frac{3k}{(k-1)(k+1)(k+2)} = \frac{a}{k-1} + \frac{b}{k+1} + \frac{c}{k+2}$$
   - En multipliant par $(k-1)$ et en posant $k = 1$ : $a = \frac{3(1)}{(2)(3)} = \frac{1}{2}$.
   - En multipliant par $(k+1)$ et en posant $k = -1$ : $b = \frac{3(-1)}{(-2)(1)} = \frac{3}{2}$.
   - En multipliant par $(k+2)$ et en posant $k = -2$ : $c = \frac{3(-2)}{(-3)(-1)} = -2$.

   D'où :
   $$u_k = \frac{1/2}{k-1} + \frac{3/2}{k+1} - \frac{2}{k+2}$$

3. **Sommation partielle et télescopage rigoureux** : écrivons la $n$-ième somme partielle $S_n = \sum_{k=2}^n u_k$ :
   $$S_n = \frac{1}{2} \sum_{k=2}^n \frac{1}{k-1} + \frac{3}{2} \sum_{k=2}^n \frac{1}{k+1} - 2 \sum_{k=2}^n \frac{1}{k+2}$$
   Effectuons un changement d'indice sur chaque somme pour faire apparaître le terme général $\frac{1}{k}$ :
   $$\sum_{k=2}^n \frac{1}{k-1} = \sum_{k=1}^{n-1} \frac{1}{k}, \quad \sum_{k=2}^n \frac{1}{k+1} = \sum_{k=3}^{n+1} \frac{1}{k}, \quad \sum_{k=2}^n \frac{1}{k+2} = \sum_{k=4}^{n+2} \frac{1}{k}$$
   Isolons les termes aux bornes pour faire apparaître la somme commune de $k=4$ à $n-1$ :
   $$\sum_{k=1}^{n-1} \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \sum_{k=4}^{n-1} \frac{1}{k}$$
   $$\sum_{k=3}^{n+1} \frac{1}{k} = \frac{1}{3} + \sum_{k=4}^{n-1} \frac{1}{k} + \frac{1}{n} + \frac{1}{n+1}$$
   $$\sum_{k=4}^{n+2} \frac{1}{k} = \sum_{k=4}^{n-1} \frac{1}{k} + \frac{1}{n} + \frac{1}{n+1} + \frac{1}{n+2}$$
   Injectons ces expressions dans $S_n$ :
   $$S_n = \frac{1}{2}\left(1 + \frac{1}{2} + \frac{1}{3}\right) + \frac{3}{2}\left(\frac{1}{3}\right) + \left(\frac{1}{2} + \frac{3}{2} - 2\right) \sum_{k=4}^{n-1} \frac{1}{k} + \mathcal{O}\left(\frac{1}{n}\right)$$
   Remarquons que la partie centrale s'annule exactement : $\left(\frac{1}{2} + \frac{3}{2} - 2\right) = 0$. Calculons la constante résiduelle :
   $$C = \frac{1}{2}\left(\frac{11}{6}\right) + \frac{1}{2} = \frac{11}{12} + \frac{6}{12} = \frac{17}{12}$$
   D'où : $S_n = \frac{17}{12} + \mathcal{O}\left(\frac{1}{n}\right)$

4. **Passage à la limite** :
   $$\sum_{n=2}^{+\infty} u_n = \lim_{n \to +\infty} S_n = \frac{17}{12}$$

### Exercice 4 : Encadrement série-intégrale (CC1 2025/2026, Ex 4)

**Consigne :** soit $u_n = \frac{2}{n^3+n}$ pour tout $n \ge 1$.

1. Déterminer la nature de la série $\sum_{n \ge 1} u_n$.
2. Montrer que pour tout $n \ge 2$ : $\displaystyle\int_2^{n+1} \frac{2}{x^3+x}\, dx \le \sum_{k=2}^n u_k \le \int_1^n \frac{2}{x^3+x}\, dx$.
3. Calculer la dérivée de $F : x \mapsto \ln\left(1 + \frac{1}{x^2}\right)$ sur $\mathbb{R}_+^*$.
4. En déduire un encadrement de la somme $\sum_{n=2}^{+\infty} u_n$.

**Rédaction étape par étape :**

1. **Nature de la série** : $u_n = \frac{2}{n^3+n} \sim_{+\infty} \frac{2}{n^3}$. Il s'agit d'une série à termes strictement positifs équivalente à une série de Riemann convergente ($\alpha = 3 > 1$). La série $\sum_{n \ge 1} u_n$ **converge**.

2. **Établissement de l'encadrement par intégrales** : posons $f(x) = \frac{2}{x^3+x}$. La fonction $f$ est continue, strictement positive et décroissante sur $\mathbb{R}_+^*$. Pour tout $k \ge 2$ :
   - Sur $[k-1, k]$, par décroissance de $f$ : $\forall x \in [k-1, k],\ f(k) \le f(x) \implies u_k \le \int_{k-1}^k f(x)\, dx$.
   - Sur $[k, k+1]$, par décroissance de $f$ : $\forall x \in [k, k+1],\ f(x) \le f(k) \implies \int_k^{k+1} f(x)\, dx \le u_k$.

   En sommant ces deux inégalités pour $k$ allant de 2 à $n$, nous obtenons par la relation de Chasles :
   $$\int_2^{n+1} \frac{2}{x^3+x}\, dx \le \sum_{k=2}^n u_k \le \int_1^n \frac{2}{x^3+x}\, dx$$

3. **Calcul de la dérivée $F'(x)$** : $F(x) = \ln\left(1 + \frac{1}{x^2}\right)$. Pour tout $x > 0$ :
   $$F'(x) = \frac{\frac{d}{dx}\left(1 + \frac{1}{x^2}\right)}{1 + \frac{1}{x^2}} = \frac{-\frac{2}{x^3}}{\frac{x^2+1}{x^2}} = \frac{-2}{x^3\left(\frac{x^2+1}{x^2}\right)} = \frac{-2}{x(x^2+1)} = -\frac{2}{x^3+x} = -f(x)$$

4. **Encadrement de la somme infinie** $\sum_{n=2}^{+\infty} u_n$ : une primitive de $f(x)$ est $-F(x)$. L'encadrement devient :
   $$\left[-\ln\left(1 + \frac{1}{x^2}\right)\right]_2^{n+1} \le \sum_{k=2}^n u_k \le \left[-\ln\left(1 + \frac{1}{x^2}\right)\right]_1^n$$
   $$\ln\left(1 + \frac{1}{4}\right) - \ln\left(1 + \frac{1}{(n+1)^2}\right) \le \sum_{k=2}^n u_k \le \ln(1 + 1) - \ln\left(1 + \frac{1}{n^2}\right)$$
   $$\ln\left(\frac{5}{4}\right) - \ln\left(1 + \frac{1}{(n+1)^2}\right) \le \sum_{k=2}^n u_k \le \ln(2) - \ln\left(1 + \frac{1}{n^2}\right)$$
   Puisque la série converge, nous pouvons passer à la limite quand $n \to +\infty$. Comme $\lim_{n \to +\infty} \ln\left(1 + \frac{1}{n^2}\right) = \ln(1) = 0$, nous concluons :
   $$\ln\left(\frac{5}{4}\right) \le \sum_{n=2}^{+\infty} u_n \le \ln(2)$$