---
source: "PREING2-S2/Algebre-lineaire-DS/cc-2025-2026/CC2_Algebre_lineaire_bilineaire_refait.pdf"
archive: "cc 2025 2026.zip"
pages: 2
semestre: "P2S2"
transcription: texte natif restructuré et contrôlé sur le rendu PDF
transcription_date: 2026-11-01
verification: comparaison du texte extrait avec le rendu des pages du PDF fourni
---

# CC2 Algebre lineaire bilineaire refait

## Page 1

CY TECH | ALGÈBRE LINÉAIRE ET BILINÉAIRE — CC2 2025/2026 · Semestre 2 · PréIng2 · Jeudi 9 avril 2026 · Durée : 90 min Documents et supports électroniques interdits. Trois exercices indépendants.

### Exercice 1 — Questions de cours

Soit E un espace vectoriel sur ℝ. Soit f : E × E → ℝ une application.

1) Que signifie : f est symétrique ?

2) On suppose que f est bilinéaire et symétrique : (a) Donner la définition de f est positive ; (b) Donner la définition de f est définie.

3) Soit ℝ² muni de sa base canonique. Soit f : ℝ² × ℝ² → ℝ définie pour x = (x₁,x₂) et y = (y₁,y₂) par :

f(x,y) = −x₁y₁ + x₁y₂ + y₁x₂ − x₂y₂.

(a) Montrer que f est bilinéaire et symétrique. (b) Expliciter la matrice de f dans la base canonique de ℝ². (c) Calculer f((1,1),(1,1)). Qu’en déduisez-vous ?

### Exercice 2 — Un système différentiel linéaire

On considère le système d’équations différentielles linéaires :

x′(t) = y(t) ; y′(t) = −x(t) + 2y(t) ; z′(t) = 3z(t).

1) Écrire ce système sous la forme matricielle X′(t) = AX(t), en précisant les différentes matrices.

2) Calculer le polynôme caractéristique de A et donner son expression sous forme factorisée. En déduire que le spectre de A est Sp(A) = {1,3}.

3) Déterminer les sous-espaces propres de A.

4) Trigonaliser la matrice A : expliciter les matrices P, T et P⁻¹, éléments de M₃(ℝ), telles que A = PTP⁻¹.

5) Par un changement de variable à expliciter, montrer que le système (S) est équivalent au système (S′) : U′(t) = TU(t), où U(t) = (u(t),v(t),w(t))ᵀ.

6) Résoudre le système (S′), d’inconnue U(t).

7) En déduire X(t), la solution générale du système (S).

8) Déterminer la solution unique X(t) du système (S) vérifiant X(0) = (1,0,1)ᵀ.

### Exercice 3 — Une suite de vecteurs

On considère la suite (Xₙ)ₙ∈ℕ de matrices colonnes de M₂,₁(ℝ), définie par :

Xₙ₊₁ = AXₙ + B

A = [[3/5, 1/5], [4/5, 3/5]] ; B = (1,1)ᵀ ; Xₙ = (xₙ,yₙ)ᵀ ; X₀ = (x₀,y₀)ᵀ.

1) Montrer que la matrice (I₂ − A) n’est pas inversible.

2) Montrer qu’il n’existe pas de solution constante à cette suite récurrente, c’est-à-dire de matrice X ∈ M₂,₁(ℝ) telle que X = AX + B.

## Page 2

3) Diagonaliser A : expliciter P, D et P⁻¹ dans M₂(ℝ) telles que A = PDP⁻¹.

4) On note Uₙ = (uₙ,vₙ)ᵀ et on pose Uₙ = P⁻¹Xₙ. (a) Montrer que Uₙ₊₁ = DUₙ + P⁻¹B, et calculer P⁻¹B. (b) Donner, en fonction de n, le terme général de (uₙ) et (vₙ). Indication : pour (vₙ), chercher un réel v tel que wₙ = vₙ − v soit géométrique. (c) En déduire xₙ et yₙ en fonction de n.

5) Étudier la convergence de (xₙ) et (yₙ). La suite (Xₙ) est-elle convergente ?
