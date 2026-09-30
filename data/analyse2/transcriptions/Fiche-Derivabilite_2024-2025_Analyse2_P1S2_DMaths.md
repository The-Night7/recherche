---
source: "PREING1-S2/Analyse2/Fiche-Derivabilite_2024-2025_Analyse2_P1S2_DMaths.pdf"
pages: 1
transcription: manuelle
transcription_date: 2026-09-30
verification: lecture visuelle intégrale du PDF et vérification des formules
---

# Synthèse du chapitre 4 — Dérivabilité

CY-Tech — PréIng 1 — Analyse. Le texte extractible porte l’année 2020-2021, alors que le nom du fichier indique 2024-2025.

## 1. Dérivabilité : ce qu’il faut retenir

1. Les deux définitions de la dérivabilité en $a$ :

   $$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=\lambda\in\mathbb R,$$

   $$f(x)=f(a)+\lambda(x-a)+o(x-a)\quad(x\to a).$$

   On a alors $f'(a)=\lambda$.

2. La dérivabilité à gauche et à droite.
3. Les opérations sur les dérivées, en particulier $(g\circ f)'=f'\times(g'\circ f)$.
4. La dérivée de la réciproque : si $f'\ne0$, alors

   $$(f^{-1})'=\frac1{f'\circ f^{-1}}.$$

5. Théorème de Rolle, attention aux hypothèses : continuité sur $[a,b]$, dérivabilité sur $]a,b[$ et $f(a)=f(b)$ impliquent qu’il existe $c\in]a,b[$ tel que $f'(c)=0$.
6. Théorème des accroissements finis : continuité sur $[a,b]$ et dérivabilité sur $]a,b[$ impliquent qu’il existe $c\in]a,b[$ tel que

   $$f'(c)=\frac{f(b)-f(a)}{b-a}.$$

7. L’inégalité des accroissements finis dans ses deux versions : $m\le f'\le M$ ou $|f'|\le k$.
8. Relation entre dérivée et sens de variations, en particulier pour les fonctions strictement monotones.
9. Dérivées successives et fonctions de classe $C^k$.
10. Formule de Leibniz pour la dérivée énième d’un produit. La formule imprimée est

    $$(uv)^{(n)}=\sum_{k=1}^{n}\binom nk u^{(k)}v^{(n-k)}.$$

> **Coquille de la source :** la somme de Leibniz doit commencer à $k=0$. La formule correcte est $(uv)^{(n)}=\sum_{k=0}^{n}\binom nk u^{(k)}v^{(n-k)}$. Le terme $uv^{(n)}$ manque dans la formule imprimée.

## 2. Dérivabilité : ce qu’il faut savoir faire

1. Étudier la dérivabilité d’une fonction, en général en faisant appel aux opérations de somme, produit, rapport et composée de fonctions dérivables ; puis en étudiant la limite du taux d’accroissement en certains points particuliers.
2. Utiliser le théorème de Rolle pour montrer qu’une dérivée s’annule en certains points en l’appliquant entre deux points où la fonction prend la même valeur.
3. Utiliser le théorème des accroissements finis (TAF) pour exprimer un taux d’accroissement comme dérivée en un point.
4. Utiliser le TAF sur l’intervalle $[n,n+1]$ pour minorer, majorer ou encadrer une expression de type $f(n+1)-f(n)$.
5. Dans le cas général, pour déterminer la dérivée énième d’une fonction, calculer les premières dérivées et conjecturer une forme générale à démontrer par récurrence.
6. Utiliser la formule de Leibniz pour dériver une fonction de la forme $f(x)=P(x)e^{ax}$ avec $P$ polynomiale.
