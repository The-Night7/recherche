---
source: "PREING2-S2/Integration-proba/Synthèse de Cours _ Intégration et Probabilités (Préparation CC3).docx"
transcription: texte structuré et relu
transcription_date: 2026-09-30
verification: lecture intégrale des paragraphes et formules natives ; tableaux reconstitués depuis le Word
---

# Synthèse de Cours : Intégration et Probabilités (Préparation CC3)

## 1. Partie I : Intégration

### 1.1. Intégrales Généralisées et Fonctions de Référence

On considère l'intégrale d'une fonction f continue par morceaux sur un intervalle de type [a, b[. L'intégrale est dite convergente si la limite lim (M→b) ∫ f(t) dt existe et est finie.

**Distinction Cruciale :**

- Convergence : Existence de la limite de l'intégrale.

- Intégrabilité (f ∈ L¹) : Convergence de l'intégrale de la valeur absolue ∫ |f(t)| dt. L'intégrabilité (absolue convergence) est une condition suffisante de convergence.

A. Étalons de Croissance (Riemann et Bertrand)

Le calcul de la nature d'une intégrale repose prioritairement sur la comparaison aux fonctions de référence.

Tableau 1 : Critères de Riemann

| Type d'intégrale | Convergence si... | Divergence si... |
| --- | --- | --- |
| Voisinage de +∞ : ∫ (1/tᵅ) dt | α > 1 | α ≤ 1 |
| Voisinage de 0⁺ : ∫ (1/tᵅ) dt | α < 1 | α ≥ 1 |

Tableau 2 : Intégrales de Bertrand (Source : DS 2021)

L'intégrale I(α, β) = ∫ [dt / (tᵅ (ln t)ᵝ)] converge si et seulement si :

- α > 1 (quel que soit β)

- α = 1 et β > 1

B. La Fonction Gamma ( Γ ) (Source : TD1)

Définie pour x > 0 par Γ(x) = ∫ tˣ⁻¹ e⁻ᵗ dt.

- Relation fondamentale : Γ(x+1) = xΓ(x).

- Lien avec la factorielle : Pour n ∈ ℕ, Γ(n+1) = n!.

- Valeur remarquable : Γ(1/2) = √π.

C. Méthodes de Comparaison

Pour des fonctions positives (ou de signe constant au voisinage de la borne) :

- Domination : Si 0 ≤ |f| ≤ g et g est intégrable, alors f est intégrable.

- Équivalence : Si f ~ g en b, alors ∫ f et ∫ g sont de même nature.

- Note de l'Expert sur l'IPP : Lors d'une Intégration Par Parties sur un intervalle ouvert, veillez à toujours vérifier la convergence du terme entre crochets [u(t)v(t)] de a à b avant de conclure sur l'intégrale restante (Source : CC1).

### 1.2. Intégrales à Paramètres

On étudie F(x) = ∫ f(t, x) dt. La validité des interversions (limite/intégrale, dérivée/intégrale) dépend de l'Hypothèse de Domination.

- Théorème de Continuité : F est continue sur A si x ↦ f(t, x) est continue, t ↦ f(t, x) est continue par morceaux, et s'il existe une fonction g ∈ L¹(I) indépendante de x telle que ∀ (t, x) ∈ I × A, |f(t, x)| ≤ g(t).

- Théorème de Dérivation (Règle de Leibniz) : F est de classe C¹ si ∂f/∂x existe, est continue par rapport à x, et respecte la domination |∂f/∂x(t, x)| ≤ g(t) avec g intégrable et indépendante de x.

- Théorème de Convergence Dominée : Pour une suite (fₙ), si fₙ → f simplement et |fₙ| ≤ g (intégrable), alors lim ∫ fₙ = ∫ f.

### 1.3. Intégrales Multiples et Géométrie

Le passage d'une intégrale double à des intégrales simples suit le Théorème de Fubini.

- Méthodologie : Choisir l'intégration "par tranches" (domaine rectangulaire ou produit d'intervalles) ou "par piles" (si les bornes d'une variable dépendent de l'autre, ex: a ≤ x ≤ b et ϕ(x) ≤ y ≤ ψ(x)).

- Changement de variables : La transformation Φ doit être un C¹-diffeomorphisme. ∬ f(x, y) dxdy = ∬ f(Φ(u, v)) | det J_Φ(u, v) | dudv

- Coordonnées Polaires : x=r cos θ, y=r sin θ. L'élément d'aire est dxdy = r dr dθ.

- Green-Riemann (Application Aire) : Pour un domaine K de bord Γ orienté positivement : Aire(K) = 1/2 ∮ (x dy - y dx). Exemple classique (Source DS 2021) : Pour une ellipse de paramètres a, b, on utilise x = a cos t, y = b sin t pour obtenir Aire = πab.

## 2. Partie II : Probabilités

### 2.1. Dénombrement et Fondations

Le calcul de probabilités sur un univers fini repose sur le rapport card(A)/card(Ω) sous l'hypothèse d'équiprobabilité.

| Type de tirage (k parmi n) | Ordre | Remise | Formule |
| --- | --- | --- | --- |
| P-uplet (Liste) | Oui | Oui | nᵏ |
| Arrangement | Oui | Non | Aₙᵏ = n! / (n-k)! |
| Combinaison | Non | Non | Cₙᵏ = n! / [k!(n-k)!] |

- Formule de Bayes : P(B|A) = [P(A|B)P(B)] / P(A). Utilisée pour "remonter à la cause" à partir d'un effet observé.

- Système Complet d'Événements (SCE) : Une famille (Cᵢ) telle que ⋃ Cᵢ = Ω et Cᵢ ∩ Cⱼ = ∅. Condition sine qua non pour la formule des probabilités totales : P(A) = Σ P(A|Cᵢ)P(Cᵢ).

### 2.2. Variables Aléatoires Discrètes

Condition d'existence de l'Espérance : Pour une variable prenant une infinité de valeurs, EX existe si et seulement si la série Σ xᵢ P(X = xᵢ) est absolument convergente.

Tableau 3 : Lois Usuelles Discrètes

| Loi | Notation | P(X=k) | E(X) | Var(X) | Notes |
| --- | --- | --- | --- | --- | --- |
| Uniforme | U(1, n) | 1/n | (n+1)/2 | (n²-1)/12 | Équiprobabilité |
| Bernoulli | B(p) | pᵏ(1-p)¹⁻ᵏ | p | p(1-p) | Succès/Échec |
| Binomiale | B(n, p) | Cₙᵏ pᵏ qⁿ⁻ᵏ | np | npq | n répétitions |
| Poisson | P(λ) | e⁻λ λᵏ / k! | λ | λ | X(Ω) = ℕ |
| Géométrique | G(p) | p(1-p)ᵏ⁻¹ | 1/p | (1-p)/p² | Sans mémoire |

### 2.3. Analyse de la Dépendance

- Covariance : Cov(X, Y) = E(XY) - E(X)E(Y).

- Indépendance : X ⊥ Y ⟺ P(X=x, Y=y) = P(X=x)P(Y=y).

- Propriété : L'indépendance implique Cov(X, Y) = 0. La réciproque est fausse en général.

### 2.4. Variables Aléatoires à Densité (Continues)

Une variable est continue si sa fonction de répartition F(x) = P(X ≤ x) est continue et dérivable presque partout, de dérivée f (densité).

- Propriété : f ≥ 0 et ∫ f(t) dt = 1 sur ℝ.

- Espérance : E(X) = ∫ t f(t) dt, sous condition d'intégrabilité absolue.

Tableau 4 : Lois Usuelles Continues

| Loi | Densité f(x) | E(X) | Var(X) | Propriétés |
| --- | --- | --- | --- | --- |
| Uniforme | 1/(b-a) sur [a, b] | (a+b)/2 | (b-a)²/12 | Prop. à la longueur |
| Exponentielle | λ e⁻λˣ sur ℝ⁺ | 1/λ | 1/λ² | Sans mémoire |
| Normale | Cloche de Gauss (μ, σ) | μ | σ² | Centrée réduite si μ=0, σ=1 |

### 2.5. Temps d'arrêt et Processus (Source : CC3 Rattrapage)

Le temps d'arrêt modélise la durée nécessaire pour qu'un événement survienne dans une expérience répétée.

- Arrêt Presque Sûr : L'expérience s'arrête avec une probabilité de 1 si Σ P(Bₙ) = 1, où Bₙ est l'événement "arrêt au tirage n".

- Exemple (Urne évolutive) : Si l'on rajoute des boules blanches à chaque succès, le calcul de P(Bₙ) devient une probabilité composée. La convergence de la somme vers 1 garantit que le processus s'arrête.

## Notes de transcription — Précisions sur la source

Les notations Unicode et les tableaux sont conservés. Plusieurs intégrales sont écrites sans bornes dans le document ; pour Gamma, la définition usuelle est $\Gamma(x)=\int_0^{+\infty}t^{x-1}e^{-t}\,dt$ ($x>0$). Le critère de Bertrand donné concerne le voisinage de $+\infty$, avec une borne inférieure strictement supérieure à 1.

Dans le système complet d’événements, la disjonction $C_i\cap C_j=\varnothing$ concerne $i\ne j$. Les probabilités conditionnelles nécessitent un conditionnement de probabilité non nulle. Dans le tableau binomial, $q=1-p$.

La définition d’une variable à densité est insuffisante dans la source : une fonction de répartition continue et dérivable presque partout n’est pas nécessairement l’intégrale de sa dérivée. La propriété requise est l’absolue continuité, avec $F(x)=\int_{-\infty}^x f(t)\,dt$. Les identités d’espérance et de covariance supposent l’existence des moments concernés.
