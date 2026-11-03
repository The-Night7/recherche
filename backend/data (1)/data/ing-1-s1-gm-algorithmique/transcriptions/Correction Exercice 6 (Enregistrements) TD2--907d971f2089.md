---
source: ING 1/S1 GM /ALGO/TD/Correction Exercice 6 (Enregistrements) TD2.pdf
pages: 3
transcription: manuelle
verification: lecture intégrale de la source
---

# Correction de l’exercice 6 — TD2 : enregistrements

## Page 1 — Type étudiant et affichage

```text
enregistrement Etudiant
    nom : chaîne
    prenom : chaîne
    moyenne : réel
fin enregistrement

préconditions : tab est initialisé
procédure afficheGroupe(tab : Tableau [0..20] de Etudiant)
Variables
    i : entier
début
    pour i ← 1 à 20 faire
        Ecrirenl(tab[i].nom, " ", tab[i].prenom, " : ", tab[i].moyenne)
    fin pour
fin procédure
```

## Page 2 — Initialisation du groupe

```text
préconditions : tab est créé
postconditions : renvoie tab initialisé avec les étudiants
procédure initGroupe(tab : Tableau [0..20] de Etudiant (E/S))
Variables
    i, j, nbNotes : entier
    note, sommeNotes : réel
début
    Ecrire("Saisir le nombre de notes : ")
    Lire(nbNotes)
    tant que nbNotes ≤ 0 faire
        Ecrire("La valeur doit être positive")
        Ecrire("Resaisir le nombre de notes ")
        Lire(nbNotes)
    fin tant que
    pour i ← 1 à 20 faire
        Ecrire("Saisir le nom du ", i, "ème étudiant :")
        Lire(tab[i].nom)
        Ecrire("Saisir le prénom du ", i, "ème étudiant :")
        Lire(tab[i].prenom)
        sommeNotes ← 0
        pour j ← 1 à nbNotes faire
            Ecrire("Saisir la ", j, "ième note : ")
            Lire(note)
            tant que (note < 0 ou note > 20) faire
                Ecrire("La note doit être comprise entre 0 et 20")
                Ecrire("Resaisir la ", j, "ième note : ")
                Lire(note)
            fin tant que
            sommeNotes ← note + sommeNotes
        fin pour
        tab[i].moyenne ← sommeNotes / nbNotes
    fin pour
fin procédure
```

## Page 3 — Tri et programme principal

```text
préconditions : tab est initialisé
postconditions : tab est trié par ordre décroissant de moyenne selon le tri à bulle
procédure triGroupe(tab : Tableau [0..20] de Etudiant (E/S))
Variables
    i, n : entier
    trie : booléen
    tmp : Etudiant
début
    trie ← FAUX
    n ← longueur(tab) - 1
    tant que non(trie) faire
        trie ← VRAI
        pour i ← 1 à n faire
            si tab[i].moyenne < tab[i+1].moyenne alors
                tmp ← tab[i]
                tab[i] ← tab[i+1]
                tab[i+1] ← tmp
                trie ← FAUX
            fin si
        fin pour
        n ← n - 1
    fin tant que
fin procédure

Algorithme Exercice6
Variables
    tab : Tableau [0..20] de Etudiant
début
    initGroupe(tab)
    triGroupe(tab)
    afficheGroupe(tab)
fin
```

## Note sur les indices de la source

Les bornes `[0..20]`, les boucles commençant à 1 et l’initialisation `n ← longueur(tab) - 1` sont transcrites telles qu’imprimées. Avec les bornes inclusives usuelles, le tableau comporte 21 cases : la case 0 n’est pas initialisée, et le premier passage du tri atteint `tab[21]`, hors limites. Pour traiter les 20 étudiants d’indices 1 à 20, une version cohérente déclare `[1..20]` et initialise `n ← 19` ; le reste de l’algorithme est inchangé.
