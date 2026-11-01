---
source: "PREING2-S2/Ondes-CC/cc-2025-2026/CC3_Ondes_retape.pdf"
archive: "cc 2025 2026.zip"
pages: 2
semestre: "P2S2"
transcription: texte natif restructuré et contrôlé sur le rendu PDF
transcription_date: 2026-11-01
verification: comparaison du texte extrait avec le rendu des pages du PDF fourni
---

# CC3 Ondes retape

## Notes de transcription

> L’année 2025–2026 provient du classement de l’archive ; aucune date d’épreuve n’est imprimée sur ce PDF.

> Exercice 2 : la condition initiale f(x) = x est incompatible en x = L avec le bord fixe F(L,t) = 0. Les coefficients bₙ sont déclarés nuls dans la question 2. Ces indications sont conservées.

## Page 1

CY TECH — CC3 ONDES PréIng 2 Durée : 1 h 30. Documents, calculatrices, portables et objets connectés interdits. Expliciter les raisonnements. Sujet de deux pages.

### Exercice 1 (3,5 pts)

Dans un référentiel supposé galiléen, on considère une onde F(x,t) vérifiant :

∂²F/∂t² = c² ∂²F/∂x² − α ∂⁴F/∂x⁴, α > 0, c > 0.

1. On cherche une solution F(x,t) = A exp[i(ωt−kx)]. Montrer que cette hypothèse conduit à la relation de dispersion ω(k).

2. À partir de cette relation, déterminer :

a. La vitesse de phase vφ(k).

b. La vitesse de groupe vg(k).

c. Est-ce que le milieu est dispersif ?

### Exercice 2 (5 pts)

Équation d’onde à 1D sur une corde de longueur L :

∂²F(x,t)/∂t² = c² ∂²F(x,t)/∂x², 0 < x < L

Conditions aux bords : F(0,t) = F(L,t) = 0. Conditions initiales : F(x,0) = f(x) = x, ∂F/∂t(x,0) = g(x).

aₙ = (2/L) ∫₀ᴸ sin(nπx/L) f(x) dx

bₙ = (2/(ωₙL)) ∫₀ᴸ sin(nπx/L) g(x) dx

La solution générale de l’équation différentielle est de la forme :

F(x,t) = Σₙ₌₁⁺∞ [aₙ cos(ωₙt) + bₙ sin(ωₙt)] sin(kₙx).

1. À partir des conditions aux bords, démontrer la quantification du vecteur d’onde k, puis exprimer kₙ et ωₙ en fonction des données du problème et de l’entier n.

2. Sachant que les coefficients bₙ sont nuls pour tout entier n, déterminer les coefficients aₙ pour n pair puis n impair.

3. Donner la solution finale F(x,t) sous forme réelle.

### Exercice 3 (8,5 pts) — Réflexion et transmission d’ondes

Deux cordes semi-infinies, de densités linéiques μ₁ et μ₂, s’étendent chacune sur l’axe x de part et d’autre de l’origine. Elles sont soumises à une tension constante T. Le référentiel d’étude est galiléen et lié au point d’attache.

x < 0 : corde 1, c₁ = √(T/μ₁) ; x > 0 : corde 2, c₂ = √(T/μ₂).

Les nombres d’onde sont k₁ = ω/c₁ et k₂ = ω/c₂, où ω est la pulsation.

On considère une onde incidente ψᵢ(x,t) = Aᵢ exp[i(ωt−k₁x)] arrivant de −∞ (se déplaçant vers +∞). On veut connaître l’onde réfléchie ψᵣ(x,t) sur la corde 1 et transmise ψₜ(x,t) sur la corde 2.

1. Donner les formes générales de ψᵣ(x,t) d’amplitude Aᵣ et ψₜ(x,t) d’amplitude Aₜ.

2. Donner l’expression totale des ondes sur chaque demi-corde : ψ₁(x,t) et ψ₂(x,t).

3. Écrire la condition de continuité de l’onde en x = 0.

## Page 2

4. Écrire la condition de continuité de ∂ψ/∂x en x = 0.

5. Définir les coefficients de réflexion et de transmission en amplitude R et T.

6. Exprimer R et T en fonction de k₁ et k₂.

7. Étudier la limite de R lorsque k₂ ≫ k₁. Commenter.

### Exercice 4 (4 pts) — Onde électromagnétique plane dans le vide

Dans le vide, le champ électrique complexe d’une onde électromagnétique plane est :

E⃗(M,t) = E₀ exp[i(ωt−kx)] u⃗ᵧ

où E₀ est une constante réelle, ω est la pulsation et k⃗ = k u⃗ₓ est le vecteur d’onde. Le référentiel d’étude est supposé galiléen.

1. Déterminer la direction et le sens de propagation de l’onde.

2. Déterminer le champ magnétique complexe B⃗(M,t).

3. Montrer que l’amplitude B₀ de B⃗ est liée à E₀ par B₀ = E₀/c, où c est la vitesse de l’onde.
