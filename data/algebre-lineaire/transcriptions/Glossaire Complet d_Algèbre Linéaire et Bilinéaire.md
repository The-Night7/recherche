---
source: "PREING2-S2/Glossaire Complet d_Algèbre Linéaire et Bilinéaire.docx"
transcription: texte structuré et relu
transcription_date: 2026-09-30
verification: lecture intégrale des paragraphes et formules natives ; tableaux reconstitués depuis le Word
---

# Glossaire Complet d'Algèbre Linéaire et Bilinéaire

Ce glossaire encyclopédique compile les définitions fondamentales et les résultats théoriques essentiels de l'algèbre linéaire et bilinéaire. Il est rédigé avec la rigueur mathématique requise pour les classes préparatoires et le premier cycle universitaire, en s'appuyant strictement sur les sources académiques de référence.

## 1. Raisonnement et Vocabulaire Ensembliste

### Assertion (ou propriété)

Un assemblage de mots dont la construction obéit à une syntaxe précise et auquel on peut attribuer une valeur de vérité : V (vrai) ou F (faux).

### Négation (¬P)

L'assertion ¬P est vraie lorsque P est fausse, et fausse lorsque P est vraie.

### Conjonction (Et)

L'assertion (P et Q) est vraie lorsque les deux assertions P et Q sont simultanément vraies, et fausse sinon.

### Disjonction (Ou)

L'assertion (P ou Q) est vraie lorsqu'au moins l'une des deux assertions P ou Q est vraie, et fausse lorsque les deux sont simultanément fausses.

### Implication

L'assertion P ⇒ Q est définie par (¬P) ou Q. Conformément à sa table de vérité, elle n'est fausse que dans le cas unique où P est vraie et Q est fausse. Si P est fausse, l'implication est toujours considérée comme vraie, quel que soit le statut de Q.

### Équivalence

L'assertion P ⇔ Q est définie par (P ⇒ Q) et (Q ⇒ P). Elle est vraie si et seulement si P et Q ont la même valeur de vérité.

### Inclusion

On dit qu'un ensemble A est inclus dans E (noté A ⊂ E) si tout élément de A appartient à E : ∀ x ∈ A, x ∈ E.

### Ensemble des parties P(E)

L'ensemble dont les éléments sont tous les sous-ensembles de l'ensemble E.

### Complémentaire

Soit A ⊂ E. Le complémentaire de A dans E, noté CE(A) (ou Aᶜ), est l'ensemble {x ∈ E ; x ∉ A}.

### Réunion

L'ensemble A ∪ B est constitué des éléments appartenant à A ou à B.

### Intersection

L'ensemble A ∩ B est constitué des éléments appartenant à la fois à A et à B.

### Différence

L'ensemble A \ B est constitué des éléments de A qui n'appartiennent pas à B.

### Différence symétrique

L'ensemble A Δ B est défini par (A \ B) ∪ (B \ A).

### Application

Un triplet f = (E, F, G) où E et F sont deux ensembles non vides (respectivement de départ et d'arrivée) et G un sous-ensemble de E × F (le graphe) tel que pour tout x ∈ E, il existe un unique y ∈ F tel que (x, y) ∈ G. On note alors y = f(x).

### Antécédent

Pour un élément y ∈ F, on appelle antécédent de y par f tout élément x ∈ E tel que f(x) = y.

### Restriction

Soit A ⊂ E. La restriction de f à A, notée f|A, est l'application de A dans F définie par f|A(x) = f(x) pour tout x ∈ A.

### Prolongement

Une application g définie sur un ensemble B contenant E est un prolongement de f si sa restriction à E est égale à f (∀ x ∈ E, g(x) = f(x)).

### Injectivité

Une application f: E → F est injective si tout élément de F admet au plus un antécédent par f : ∀ (x, x') ∈ E², f(x) = f(x') ⇒ x = x'.

### Surjectivité

Une application f: E → F est surjective si tout élément de F admet au moins un antécédent par f : ∀ y ∈ F, ∃ x ∈ E, y = f(x).

### Bijectivité

Une application est bijective si elle est à la fois injective et surjective. Tout élément de l'ensemble d'arrivée possède alors un unique antécédent.

### Application réciproque f⁻¹

Si f: E → F est bijective, son application réciproque f⁻¹: F → E est l'unique application telle que f⁻¹ ∘ f = IdE et f ∘ f⁻¹ = IdF.

### Composée

Soient f: E → F et g: F → G. La composée g ∘ f: E → G est définie par ∀ x ∈ E, (g ∘ f)(x) = g(f(x)).

### Image directe

Pour une partie A ⊂ E, l'image directe de A par f est l'ensemble f(A) = {f(x) ; x ∈ A}.

### Image réciproque

Pour une partie B ⊂ F, l'image réciproque de B par f est l'ensemble f⁻¹(B) = {x ∈ E ; f(x) ∈ B}.

### Relation binaire

Un triplet R = (E, E, G) où G ⊂ E × E. On note x R y si (x, y) ∈ G.

### Relation d'ordre

Une relation binaire R sur E est une relation d'ordre si elle satisfait les trois propriétés suivantes :

- Réflexivité : ∀ x ∈ E, x R x.

- Antisymétrie : ∀ (x, y) ∈ E², (x R y et y R x) ⇒ x = y.

- Transitivité : ∀ (x, y, z) ∈ E³, (x R y et y R z) ⇒ x R z.

### Relation d'équivalence

Une relation binaire R sur E est une relation d'équivalence si elle est réflexive, transitive et :

- Symétrique : ∀ (x, y) ∈ E², x R y ⇒ y R x.

### Classe d'équivalence

Pour un élément x ∈ E, la classe d'équivalence de x est l'ensemble x̄ = {y ∈ E ; x R y}.

### Partition

### On appelle partition d'un ensemble E une famille S de parties de E telles que

- ∀ A ∈ S, A ≠ ∅.

- Les parties sont disjointes deux à deux (∀ A, B ∈ S, A ≠ B ⇒ A ∩ B = ∅).

- La réunion de toutes les parties de S est égale à E.

## 2. Espaces Vectoriels et Applications Linéaires

### Sous-espace vectoriel (sev)

Une partie non vide F d'un K-espace vectoriel E est un sous-espace vectoriel si elle est stable par combinaison linéaire : ∀ (λ, μ) ∈ K², ∀ (x, y) ∈ F², λx + μy ∈ F.

### Famille libre

Une famille (v₁, ..., vₙ) de vecteurs est dite libre si toute combinaison linéaire nulle de ces vecteurs impose la nullité de tous ses coefficients : Σ λᵢvᵢ = 0E ⇒ λ₁ = ... = λₙ = 0.

### Famille génératrice

Une famille de vecteurs est génératrice de E si tout vecteur de E peut s'écrire comme une combinaison linéaire des vecteurs de cette famille.

### Base

Une famille de vecteurs qui est à la fois libre et génératrice.

### Somme de sous-espaces

Soient F et G deux sous-espaces vectoriels de E. La somme F+G est le sous-espace défini par {x+y ; x ∈ F, y ∈ G}. La somme est dite directe, notée F ⊕ G, si F ∩ G = {0E}.

### Rang

Le rang d'une application linéaire f ∈ L(E, F) est la dimension de son image : rg(f) = dim(Im f).

### - Théorème du rang

- Pour tout espace vectoriel E de dimension finie, dim(E) = dim(ker f) + rg(f).

### - Système de Cramer

- Un système linéaire AX = B de n équations à n inconnues est un système de Cramer si et seulement si la matrice A est inversible, ce qui équivaut à det(A) ≠ 0. Un tel système admet une solution unique.

### - Matrice associée à un produit scalaire

- Pour une forme bilinéaire φ sur E et une base B = (e₁, ..., eₙ), il s'agit de la matrice symétrique A = (aᵢⱼ) ∈ Mₙ(R) où chaque coefficient est défini par aᵢⱼ = φ(eᵢ, eⱼ). Pour tout couple de vecteurs (x, y), on a φ(x, y) = XᵀAY.

## 3. Réduction des Endomorphismes

### Valeur propre

Soit f ∈ L(E) et λ ∈ K. On dit que λ est une valeur propre de f s'il existe un vecteur v ∈ E \ {0E} tel que f(v) = λv.

### Vecteur propre

Soit f ∈ L(E). Un vecteur v est un vecteur propre de f s'il est non nul (v ∈ E \ {0E}) et s'il existe λ ∈ K tel que f(v) = λv.

### Spectre Spₖ(f)

L'ensemble de toutes les valeurs propres de l'endomorphisme f appartenant au corps K.

### Sous-espace propre Eλ

Pour une valeur propre λ de f, le sous-espace propre associé est défini par Eλ = ker(f - λIdE). Il contient le vecteur nul et l'ensemble des vecteurs propres associés à λ.

### Diagonalisabilité

Un endomorphisme f (ou une matrice A) est diagonalisable s'il existe une base de E composée exclusivement de vecteurs propres de f. Dans cette base, la matrice représentative de f est diagonale.

### Trigonalisabilité

Un endomorphisme f (ou une matrice A) est trigonalisable s'il existe une base de E dans laquelle sa matrice est triangulaire supérieure.

### Matrice nilpotente

Une matrice N est dite nilpotente s'il existe un entier k ∈ N* tel que Nᵏ = 0.

### - Ordre de nilpotence

- On appelle ordre de nilpotence le plus petit entier k ∈ N* satisfaisant l'égalité Nᵏ = 0. (Remarque : Conformément aux travaux dirigés, une matrice nilpotente diagonalisable est nécessairement nulle).

## 4. Formes Bilinéaires et Espaces Euclidiens

### Produit scalaire

Une forme bilinéaire symétrique sur un R-espace vectoriel E est un produit scalaire si elle est :

## 1. Positive : ∀ x ∈ E, ⟨x, x⟩ ≥ 0.

## 2. Définie : ∀ x ∈ E, ⟨x, x⟩ = 0E ⇒ x = 0E.

### Norme euclidienne

L'application notée ||.|| associée à un produit scalaire, définie par ||x|| = √⟨x, x⟩.

### Orthogonal F┴

Soit F un sous-espace de E. L'orthogonal de F est l'ensemble F┴ = {x ∈ E ; ∀ y ∈ F, ⟨x, y⟩ = 0}.

### Base orthonormale (ou orthonormée)

Une base (e₁, ..., eₙ) d'un espace euclidien E est orthonormale si ses vecteurs vérifient la condition de Kronecker : ⟨eᵢ, eⱼ⟩ = δᵢⱼ, où δᵢⱼ = 1 si i = j et δᵢⱼ = 0 si i ≠ j.

### Projection

Un endomorphisme p est une projection si p ∘ p = p. Dans un contexte matriciel (référence TD1 Exercice 5), cela se traduit par la relation A² = A.

## 5. Déterminants et Calcul Algébrique

### Somme simple

Soit (aₖ)ₖ ∈ ℕ une suite de scalaires. On note Σ aₖ = a₀ + a₁ + ... + aₙ.

### Somme double

Sommation effectuée sur deux indices, notée Σ Σ aᵢⱼ. L'ordre de sommation peut être inversé si le domaine est fini (Fubini fini).

### Produit simple

Noté Π aₖ, représentant le produit a₁ × a₂ × ... × aₙ. Par convention, un produit vide est égal à 1.

### Coefficients binomiaux (n p)

Pour n ∈ ℕ et p ∈ [0, n], (n p) = n! / (p!(n-p)!).

### - Propriété de nullité

- Par convention formelle, on note (n p) = 0 si p > n ou si p < 0.

### Déterminant

Le déterminant est une forme n-linéaire alternée des vecteurs colonnes d'une matrice carrée. Il constitue un outil scalaire fondamental pour caractériser l'inversibilité d'une matrice (det(A) ≠ 0) et calculer le rang d'une famille de vecteurs.

### Système de Cramer (Propriété du Déterminant)

Un système linéaire AX=B est dit de Cramer si son déterminant associé det(A) est non nul, garantissant l'existence et l'unicité de la solution.

## Notes de transcription — Précisions sur la source

- Dans « Matrice associée à un produit scalaire », la symétrie de la matrice suppose que la forme bilinéaire $\varphi$ soit symétrique ; elle ne découle pas de la seule bilinéarité.
- Dans la définition du produit scalaire, la source écrit $\langle x,x\rangle=0_E$. Le produit scalaire est un réel : il faut lire $\langle x,x\rangle=0\Rightarrow x=0_E$.
- Pour le coefficient binomial, $p$ est un entier de $\{0,\ldots,n\}$. Les notations de sommes et produits sans bornes du texte renvoient aux développements explicitement indiqués dans leurs définitions.
