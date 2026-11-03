# Informatique 3 — CM4 : arbres binaires de recherche (2024–2025)

Eva Ansermin, Renaud Verin et Romuald Grignon — version 1.1, 155 pages PDF.

Source : `PREING2-S1/Informatique3/CM4-ABR_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.pdf`.

Transcription achevée le 11 octobre 2026. Texte natif relu ; arbres, algorithmes et étapes de modification confrontés aux rendus. Les animations sont regroupées avec leurs renvois aux pages. Les imprécisions et erreurs du support sont signalées explicitement.

## Rappel et principe — pages 1–3

Un arbre binaire possède au plus deux enfants par nœud. Le mot « de recherche » figure à tort dans la définition de rappel de la page 2 : l'arbre dessiné, de racine 1 et de fils gauche 2, n'est pas un ABR. Dans un arbre quelconque sans ordre sur les valeurs, une recherche peut nécessiter de parcourir tous les nœuds : coût $O(n)$. Comme le tri d'un tableau, une organisation des valeurs dans un arbre peut accélérer la recherche.

## Définition d'un ABR — page 4

Un arbre binaire `a` est un **arbre binaire de recherche** si toutes les valeurs du sous-arbre gauche sont strictement inférieures à la valeur de sa racine, toutes celles du sous-arbre droit sont strictement supérieures, et chacun de ses sous-arbres est lui-même un ABR.

Le cours choisit des **valeurs toutes distinctes**. D'autres conventions peuvent autoriser des doublons en modifiant les inégalités et les règles d'insertion.

Exemple du support :

```text
          8
        /   \
       3    10
      / \     \
     1   6    14
        / \   /
       4   7 13
```

La contrainte concerne tout le sous-arbre, pas seulement les deux enfants immédiats.

## Exercice : compléter un ABR — pages 5–6

L'arbre à compléter a pour racine 15, fils 10 et 30 ; 10 a un fils gauche 5 et un fils droit inconnu ; 30 a un fils gauche inconnu et un fils droit 50 ; les deux fils de 50 sont inconnus, et son fils gauche a lui-même deux enfants inconnus.

Une solution proposée :

```text
             15
           /    \
         10      30
        /  \    /  \
       5   12  20  50
                  /  \
                 40  55
                /  \
               35  45
```

Les six valeurs ajoutées sont 12, 20, 40, 55, 35 et 45. Ce choix n'est pas unique, mais chaque valeur doit aussi respecter les contraintes imposées par ses ancêtres.

## Recherche — pages 7–18

Comparer l'élément recherché à la valeur du nœud : égalité, succès ; valeur plus petite, descendre à gauche ; valeur plus grande, descendre à droite. Atteindre un sous-arbre vide signifie que la valeur n'existe pas.

```text
FONCTION recherche(a : pointeur sur Arbre, e : Element) : Booleen
DEBUT
    SI a = NULL ALORS
        RETOURNER FAUX
    SINON SI element(a) = e ALORS
        RETOURNER VRAI
    SINON SI e < element(a) ALORS
        RETOURNER recherche(fg(a), e)
    SINON
        RETOURNER recherche(fd(a), e)
    FIN SI
FIN
```

Sur l'arbre de racine 15 :

| Recherche | Nœuds examinés | Résultat |
| --- | --- | --- |
| 40 | 15 → 30 → 50 → 40 | VRAI |
| 14 | 15 → 10 → 12 → fils droit `NULL` | FAUX |

Les retours récursifs propagent le même booléen jusqu'à l'appel initial.

## Complexité — pages 19–20

Le support annonce $O(1)$ au meilleur cas, quand la racine est l'élément recherché ; $O(n)$ au pire, pour un arbre filiforme ; $O(\log_2 n)$ en moyenne.

**Précision ajoutée.** Le coût est borné par la hauteur de l'arbre, soit $O(h+1)$. Le coût moyen logarithmique suppose un modèle d'arbres ou d'insertions suffisamment favorable ; il n'est pas garanti pour un ABR arbitraire. L'équilibrage sera précisément l'objet du cours suivant.

## Insertion — pages 21–23

L'insertion descend l'unique branche déterminée par les comparaisons, puis crée une feuille. Si l'élément existe déjà, ne rien ajouter.

Sur l'exemple de racine 8, insérer 2 le place à droite de 1 ; insérer 9 le place à gauche de 10. Les dessins successifs conservent 2 après son ajout.

```text
FONCTION insertionABR(a : pointeur sur Arbre, e : Element) : pointeur sur Arbre
DEBUT
    SI a = NULL ALORS
        RETOURNER creerArbre(e)
    SINON SI e < element(a) ALORS
        fg(a) ← insertionABR(fg(a), e)
    SINON SI e > element(a) ALORS
        fd(a) ← insertionABR(fd(a), e)
    FIN SI
    RETOURNER a
FIN
```

Il faut récupérer les pointeurs retournés : ils peuvent désigner une nouvelle racine de sous-arbre. Chez l'appelant : `a ← insertionABR(a, e)`.

## Animation : insertion de 11 — pages 24–48

Départ : l'arbre de racine 15 de l'exercice. Comme `11 < 15`, descendre à 10 ; comme `11 > 10`, descendre à 12 ; comme `11 < 12`, descendre sur son fils gauche, vide. Créer la feuille 11 et retourner son adresse. Le champ gauche de 12 reçoit cette adresse. Les retours suivants réaffectent le fils droit de 10 puis le fils gauche de 15 ; ces deux racines de sous-arbre sont inchangées. Résultat : 12 possède maintenant un fils gauche 11. Les autres liens restent ceux de l'arbre initial.

## Suppression : trois cas — pages 49–56

Supprimer une valeur doit conserver les autres nœuds et la relation d'ordre.

1. **Feuille.** La retirer et mettre à `NULL` le lien du parent. L'exemple supprime 45, fils droit de 40.
2. **Un enfant.** Remplacer le nœud par cet enfant. Dans le dessin réduit `15(10(5,12),30(20,NULL))`, supprimer 30 fait de 20 le fils droit de 15.
3. **Deux enfants.** Remplacer la valeur par son prédécesseur, maximum du sous-arbre gauche, ou par son successeur, minimum du sous-arbre droit ; retirer ensuite le nœud qui portait cette valeur. Pour la racine 15, le prédécesseur est 12 : 12 remplace 15 et disparaît de son ancienne position. Pour le sous-arbre de racine 30 et de fils droit 50, le successeur est 35, atteint par `50 → 40 → 35`.

**Imprécision du support :** le maximum du sous-arbre gauche est le **nœud** le plus à droite, pas nécessairement une feuille : il peut avoir un enfant gauche. De même, le minimum du sous-arbre droit peut avoir un enfant droit. La fonction auxiliaire ci-dessous conserve justement cet enfant éventuel.

## Algorithme de suppression et suppression du maximum — pages 57–61

Le support choisit la variante avec prédécesseur. Rechercher le nœud. S'il n'a pas de fils gauche, le remplacer par son fils droit, qui peut lui aussi être nul. Sinon, extraire le maximum du sous-arbre gauche et recopier sa valeur dans le nœud visé.

```text
FONCTION suppression(a : pointeur sur Arbre, e : Element) : pointeur sur Arbre
VARIABLE tmp : pointeur sur Arbre
DEBUT
    SI a = NULL ALORS
        RETOURNER a
    SINON SI e > element(a) ALORS
        fd(a) ← suppression(fd(a), e)
    SINON SI e < element(a) ALORS
        fg(a) ← suppression(fg(a), e)
    SINON SI NON existeFilsGauche(a) ALORS
        tmp ← a
        a ← fd(a)
        liberer(tmp)
    SINON
        fg(a) ← suppMax(fg(a), adresse(element(a)))
    FIN SI
    RETOURNER a
FIN

FONCTION suppMax(a : pointeur sur Arbre,
                pe : pointeur sur Element) : pointeur sur Arbre
VARIABLE tmp : pointeur sur Arbre
DEBUT
    SI existeFilsDroit(a) ALORS
        fd(a) ← suppMax(fd(a), pe)
    SINON
        *pe ← element(a)
        tmp ← a
        a ← fg(a)
        liberer(tmp)
    FIN SI
    RETOURNER a
FIN
```

**Corrections de notation.** Une parenthèse fermante manque dans l'appel à `suppMax` du PDF ; elle est rétablie. Son paramètre `a`, imprimé de type `arbre`, est un pointeur sur arbre. Le commentaire « on a le successeur » dans `suppMax` doit se lire **prédécesseur du nœud initial**, ou maximum du sous-arbre parcouru. Le terme « échange » employé dans le texte désigne ici une copie vers `*pe`, suivie de la suppression du nœud donneur.

**Préconditions.** `suppMax` est appelée sur un sous-arbre non vide, et `pe` pointe sur un élément valide du nœud conservé. `creerArbre` traite l'échec d'allocation ou suppose sa réussite. L'appelant doit récupérer la racine retournée par `suppression`.

## Animation : suppression de 8 — pages 62–91

Arbre de départ de cette série :

```text
             15
           /    \
         10      20
        /  \    /  \
       5   12  17  50
      / \         /  \
     2   8       40  55
                /  \
               35  45
```

Descente `15 → 10 → 5 → 8`. La valeur est trouvée ; 8 n'a pas de fils gauche et son fils droit est `NULL`. Mémoriser son adresse dans `tmp`, remplacer le pointeur local par `NULL`, puis libérer `tmp`. Au retour, le fils droit de 5 devient `NULL`. Les racines 5, 10 et 15 sont retournées successivement ; tous les autres nœuds sont conservés.

## Animation : suppression d'une valeur absente — pages 92–115

L'arbre est celui obtenu après la suppression de 8. Rechercher 6 : `15 → 10 → 5 → fils droit NULL`. La condition initiale retourne `NULL` sans libération. Les retours récursifs rétablissent les mêmes liens ; l'arbre est inchangé. Cette animation illustre bien une **valeur absente**, et non la suppression d'un nœud à un enfant.

## Animation : suppression de 50 — pages 116–154

Le support repart d'un arbre plus grand : la branche gauche recontient 8 ; dans le sous-arbre de 40, 45 a pour fils 42 et 48, et 35 possède un enfant dessiné à gauche, étiqueté 38.

**Erreur dans ce dessin.** 38 est placé à gauche de 35, ce qui viole l'ordre de l'ABR. Cette valeur et sa position sont conservées comme une anomalie de la source ; cette branche n'est pas utilisée dans la recherche du maximum.

Chercher 50 par `15 → 20 → 50`. Comme il a un fils gauche 40, appeler `suppMax(40, adresse(element(50)))`. Descendre à droite : `40 → 45 → 48`. Le nœud 48 n'a pas de fils droit : écrire 48 dans le champ élément du nœud qui portait 50 ; mémoriser l'adresse de l'ancien 48 ; le remplacer par son fils gauche `NULL` et le libérer.

Les retours réaffectent successivement le fils droit de 45 à `NULL`, le fils droit de 40 à 45, puis le fils gauche du nœud nouvellement étiqueté 48 à 40. Le lien droit de 20 désigne toujours ce même nœud, mais sa valeur est désormais 48. Les autres branches sont conservées, y compris l'anomalie 38 à gauche de 35. La figure finale montre donc la racine de ce sous-arbre **48**, avec fils gauche 40 et fils droit 55 ; l'ancienne feuille 48 a disparu.

## Récapitulatif — page 155

Les ABR imposent un ordre strict aux valeurs de chaque sous-arbre ; ce cours exclut les doublons. Cet ordre guide recherche, insertion et suppression. Les opérations qui modifient l'arbre doivent le préserver. Le gain logarithmique annoncé dans le résumé n'est garanti que lorsque la hauteur reste logarithmique ; un arbre filiforme garde un coût linéaire. Les méthodes d'équilibrage du cours suivant répondent à cette limite.
