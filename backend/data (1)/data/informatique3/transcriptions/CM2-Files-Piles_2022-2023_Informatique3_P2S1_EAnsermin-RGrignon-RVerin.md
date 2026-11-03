# Informatique 3 — CM2 : files et piles (2022–2023)

Auteurs : Eva Ansermin, Renaud Verin et Romuald Grignon ; version 1.00. 127 pages PDF.

Source : `PREING2-S1/Informatique3/CM2-Files-Piles_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.pdf`.

Transcription achevée le 11 octobre 2026. Texte natif relu, états finaux des algorithmes et schémas confrontés aux rendus. Les diapositives à trous sont regroupées avec leur correction progressive. Les erreurs de la source sont conservées ou explicitement signalées ; les corrections ajoutées sont distinguées.

## Rappel et objectifs — pages 1–2

Une liste chaînée permet d'insérer et de supprimer à toute position. Les piles et les files imposent des règles d'accès particulières. Le rappel représente `10 → 2 → 25 → 103 → NULL`.

## I. Piles : principe et applications — pages 3–12

Une pile ajoute et retire les éléments à son **sommet**. C'est une structure **LIFO**, *last in, first out* : dernier entré, premier sorti, comme une pile d'assiettes.

L'exemple, lu du sommet vers le fond, commence par `120, 8, 15, 2`. Empiler 33 donne `33, 120, 8, 15, 2`. Deux dépilages retirent successivement 33 puis 120 ; il reste `8, 15, 2`.

Applications : annulation d'actions (`Ctrl+Z`), retour arrière d'un navigateur, appels récursifs non terminaux, appels de fonctions dans les processeurs, simulations mathématiques ou de situations réelles. Deux implantations : tableau (« pile statique ») ou liste chaînée (« pile dynamique »). La question du choix entre les deux est posée.

## Pile statique : structure et exemple — pages 13–20

```text
Structure PileStat :
    tabPile : tableau d'Element de capacité N constante
    taille : entier, capacité du tableau
    tete : entier, indice du sommet
```

Variante : `tabPile` est un pointeur sur un bloc alloué dynamiquement, de capacité `taille`. Le support appelle encore cette représentation une pile statique : c'est la représentation par tableau qui est visée.

Exemple : capacité 7, tableau `[10, 2, 25, 103, 55, 16, 147]`, `tete = 3`. Seules les quatre premières cases appartiennent à la pile ; les autres ne sont pas nécessairement vides, mais sont ignorées. Dépiler : récupérer `tabPile[tete] = 103`, puis décrémenter `tete` à 2. Empiler ensuite 40 : incrémenter `tete` à 3, puis écrire 40 à cet indice ; le tableau devient `[10, 2, 25, 40, 55, 16, 147]`.

## Création et vérification — pages 21–27

```text
FONCTION creationPileStat() : PileStat
VARIABLE pile : PileStat
DEBUT
    tete(pile) ← -1
    RETOURNER pile
FIN
```

`-1` signifie que la pile est vide. **Limite de cet extrait :** l'allocation du tableau et l'initialisation de sa capacité ne sont pas montrées ; elles doivent être assurées avant utilisation.

```text
FONCTION verificationPileStat(pile : pointeur sur PileStat) : entier
VARIABLE result : entier ← 0
DEBUT
    SI pile = NULL ALORS
        result ← -1
    SINON SI taille(pile) ≤ 0 OU tete(pile) < -1
             OU tete(pile) > taille(pile) - 1 ALORS
        result ← -2
    FIN SI
    RETOURNER result
FIN
```

Codes : 0, données cohérentes ; −1, pointeur d'entrée nul ; −2, structure incohérente. Ces tests doivent précéder les opérations. Pour la variante à tableau alloué, le support n'ajoute pas de test du pointeur `tabPile` ; la fonction ne peut pas certifier toute l'intégrité de la mémoire.

## Empilage statique — pages 28–34

```text
FONCTION empilagePileStat(pile : pointeur sur PileStat, elmt : Element) : entier
VARIABLE result : entier
DEBUT
    result ← verificationPileStat(pile)
    SI result = 0 ALORS
        SI tete(pile) = taille(pile) - 1 ALORS
            result ← 1                         // pile pleine
        SINON
            tete(pile) ← tete(pile) + 1
            tabPile(pile)[tete(pile)] ← elmt
        FIN SI
    FIN SI
    RETOURNER result
FIN
```

L'animation passe d'un sommet d'indice 3 à l'indice 4, où le nouvel élément remplace l'ancienne valeur 55. Le `tete` isolé dans l'indice de la source est explicité ici en `tete(pile)`.

## Dépilage statique — pages 35–41

```text
FONCTION depilagePileStat(pile : pointeur sur PileStat,
                         pelmt : pointeur sur Element) : entier
VARIABLE result : entier
DEBUT
    result ← verificationPileStat(pile)
    SI pelmt = NULL ALORS result ← -1
    SI result = 0 ALORS
        SI tete(pile) = -1 ALORS
            result ← 1                         // pile vide
        SINON
            *pelmt ← tabPile(pile)[tete(pile)]
            tete(pile) ← tete(pile) - 1
        FIN SI
    FIN SI
    RETOURNER result
FIN
```

La valeur retirée est transmise par le pointeur `pelmt` ; le retour entier indique le succès ou l'erreur. La valeur ancienne peut rester dans le tableau : c'est l'indice de sommet qui délimite la pile.

## Pile dynamique — pages 42–49

La tête de pile est le premier chaînon de la liste. Pour `10 → 2 → 25 → 103`, le sommet est 10.

```text
Structure Chainon :
    elmt : Element
    suivant : pointeur sur Chainon

FONCTION creationPileDyn() : pointeur sur Chainon
    tete ← NULL
    RETOURNER tete
FIN
```

Empiler correspond à `insertDebut` : ajouter un chaînon en tête. Le schéma insère 7 devant `10 → 5 → 12`. Dépiler correspond à `suppDebut`, avec récupération de la valeur avant libération : 10 est retiré de `10 → 2 → 25 → 103`, laissant 2 en tête. Seul le début de la chaîne est modifié.

## II. Files : principe et applications — pages 50–58

Une file ajoute les éléments en **queue** et les retire en **tête**. C'est une structure **FIFO**, *first in, first out* : premier entré, premier sorti, comme une file d'attente. La tête est le début et la sortie ; la queue est la fin et l'entrée.

L'exemple commence, de la tête à la queue, par `120, 8, 15, 2`. Enfiler 33 donne `120, 8, 15, 2, 33`. Les états suivants retirent d'abord 120, puis 8 : il reste `15, 2, 33`.

Les files stockent les données à traiter dans leur ordre d'arrivée, par exemple les tâches d'impression. Elles servent également à simuler les files d'attente.

## File dynamique : représentation et opérations — pages 59–65

Sur une liste chaînée `10 → 2 → 25 → 103`, enfiler ajoute en fin : l'exemple ajoute 58. Défiler retire le premier chaînon en récupérant sa valeur : l'exemple retire 10. Deux pointeurs évitent un parcours à chaque ajout :

```text
Structure FileDyn :
    tete : pointeur sur Chainon
    queue : pointeur sur Chainon
```

La tête désigne le premier chaînon, la queue le dernier. Le sens inverse serait moins efficace : supprimer en fin d'une liste simplement chaînée nécessite de retrouver le prédécesseur. Le mot « pile » utilisé une fois dans cette section est un lapsus du support.

## Vérification d'une file dynamique — pages 66–69

Version imprimée :

```text
FONCTION verificationFileDyn(file : pointeur sur FileDyn) : entier
    result ← 0
    SI file = NULL ALORS
        result ← -1
    SINON SI (tete(file) = NULL) ≠ (queue(file) = NULL) ALORS
        result ← -2
    SINON SI suivant(queue(file)) ≠ NULL ALORS
        result ← -3
    FIN SI
    RETOURNER result
FIN
```

Le deuxième test impose que tête et queue soient simultanément nulles ou simultanément non nulles. Le dernier exige que la queue soit bien une extrémité.

**Erreur :** pour une file vide cohérente, `queue(file) = NULL`, mais le dernier test accède à son suivant. Le remplacer par `SINON SI queue(file) ≠ NULL ET suivant(queue(file)) ≠ NULL`, avec évaluation conditionnelle de la seconde partie. Ces tests locaux ne prouvent pas que la queue est accessible depuis la tête ni que la liste est dépourvue de cycle.

## Enfilage dynamique — pages 70–79

La version finale du support est :

```text
FONCTION enfilerDyn(file : pointeur sur FileDyn, elmt : Element) : entier
    result ← verificationFileDyn(file)
    SI result > -2 ALORS
        nouveau ← creationChainon()
        elmt(nouveau) ← elmt
        SI queue(file) = NULL ALORS
            tete(file) ← nouveau
            queue(file) ← nouveau
        SINON
            suivant(queue(file)) ← nouveau
        FIN SI
    FIN SI
    RETOURNER result
FIN
```

**Deux erreurs dans la source.** `result > -2` admet −1, donc le cas `file = NULL`. Il faut exiger `result = 0`. Pour une file non vide, l'affectation `queue(file) ← nouveau` manque après la liaison de l'ancienne queue. Elle est indispensable pour l'ajout suivant. `creationChainon()` doit rendre un chaînon dont le suivant est `NULL` et dont l'allocation a réussi.

**Version corrigée ajoutée :**

```text
FONCTION enfilerDynCorrige(file, valeur)
    result ← verificationFileDynCorrige(file)
    SI result ≠ 0 ALORS RETOURNER result
    nouveau ← creationChainon()       // échec d'allocation traité par cette fonction
    elmt(nouveau) ← valeur
    suivant(nouveau) ← NULL
    SI queue(file) = NULL ALORS
        tete(file) ← nouveau
    SINON
        suivant(queue(file)) ← nouveau
    FIN SI
    queue(file) ← nouveau
    RETOURNER 0
FIN
```

La fonction de vérification corrigée est celle décrite à la section précédente. Le support ne donne pas de fonction complète de défilage dynamique ; en retirant le dernier élément, il faut aussi remettre la queue à `NULL`.

## File statique — page 80

Une file peut être représentée par un tableau et deux indices. Le support nomme le tableau `tabPile` dans la structure, puis `tabFile` dans les opérations : on retient ici `tabFile` pour cohérence.

```text
Structure FileStat :
    tabFile : tableau d'Element de capacité N
    tete : entier
    queue : entier
```

Exemple : tableau `[10, 15, 87, 6, 8, 65, 13, 87, 55, 87]`, `tete = 2`, `queue = 8`. Les éléments de la file vont de l'indice 2 à 8 inclus ; les autres valeurs sont ignorées. La capacité `taille(file)` utilisée dans les fonctions suivantes est supposée connue.

## Enfilage statique — pages 81–88

```text
FONCTION enfilerStat(file : pointeur sur FileStat, elmt : Element) : entier
    result ← vérification du pointeur et du contenu de la structure
    SI result = 0 ALORS
        SI queue(file) = taille(file) - 1 ALORS
            result ← 1
        SINON
            queue(file) ← queue(file) + 1
            tabFile(file)[queue(file)] ← elmt
        FIN SI
    FIN SI
    RETOURNER result
FIN
```

La vérification est laissée sous forme d'instruction descriptive dans le PDF. Les figures utilisent ensuite la valeur 72 à l'indice 7 et insèrent `elmt` à l'indice 8. L'indice `queue` isolé est explicité en `queue(file)`.

## Défilage statique — pages 89–96

```text
FONCTION defilerStat(file : pointeur sur FileStat,
                    pElmt : pointeur sur Element) : entier
    result ← vérification des pointeurs et du contenu de la structure
    SI result = 0 ALORS
        SI tete(file) = queue(file) + 1 ALORS
            result ← 1                         // file vide
        SINON
            *pElmt ← tete(file)                 // ligne imprimée, erronée
            tete(file) ← tete(file) + 1
        FIN SI
    FIN SI
    RETOURNER result
FIN
```

**Correction :** `*pElmt ← tabFile(file)[tete(file)]`. La ligne imprimée retourne l'indice au lieu de l'élément. Le schéma retire 87 à l'indice 2, puis place la tête sur 6 à l'indice 3.

## Initialisation — pages 97–101

Le support initialise `tete = 0` et `queue = -1`, ce qui satisfait la condition de file vide. Il teste `file = NULL` et fixe `result = -1`, mais poursuit ensuite les écritures dans la structure : cela reste invalide si le pointeur est nul.

**Pseudo-code corrigé, avec retour immédiat ajouté :**

```text
FONCTION initFileStat(file : pointeur sur FileStat) : entier
    SI file = NULL ALORS RETOURNER -1
    tete(file) ← 0
    queue(file) ← -1
    RETOURNER 0
FIN
```

L'allocation et la capacité du tableau sont supposées déjà définies.

## Limites de la file statique linéaire — pages 102–104

Les indices avancent vers la fin du tableau au fil des opérations. Quand la queue atteint la dernière case, un nouvel ajout est impossible avec l'algorithme précédent, même si des cases au début ne font plus partie de la file. Le dessin montre une tête au milieu du tableau, une queue en dernière case et des cases anciennes grisées à gauche.

## File statique cyclique : principe — pages 105–113

On réutilise les premières cases quand on atteint la fin du tableau. Un premier dessin ajoute 30 dans la case 0, puis 72 dans la case 1, tandis que la tête reste plus loin dans le tableau.

Dans la convention du support, `tete` et `queue` sont des **positions logiques croissantes**, comme si le tableau était infini. L'indice physique est la position modulo la capacité.

Exemple avec 10 cases : `tete = 7`, `queue = 9`, les valeurs actives sont 87, 55, 15. Enfiler 15 donne `queue = 10`, avec écriture en case 0. Enfiler 20 donne `queue = 11`, avec écriture en case 1. Trois défilages avancent la tête à 8, puis 9, puis 10 : la tête physique se retrouve en case 0, la queue en case 1, et il reste 15, 20.

## Enfilage cyclique — pages 114–120

Version imprimée :

```text
FONCTION enfilerStatCyclique(file : pointeur sur FileStat, elmt : Element) : entier
    result ← vérification du pointeur et du contenu de la structure
    SI queue(file) - tete(file) = taille(file) - 1 ALORS
        result ← 1                             // file pleine
    SINON
        queue(file) ← queue(file) + 1
        tabFile(file)[queue(file) MOD taille(file)] ← elmt
    FIN SI
    RETOURNER result
FIN
```

**Omission du support :** entourer le test de capacité et l'insertion par `SI result = 0 ... FIN SI`, comme pour les autres opérations. Sinon la fonction agit même lorsque la vérification échoue. Le nombre d'éléments est `queue - tete + 1`, ce qui explique le test de file pleine.

## Défilage cyclique — pages 121–126

```text
FONCTION defilerStatCyclique(file : pointeur sur FileStat,
                            pelmt : pointeur sur Element) : entier
    result ← vérification des pointeurs et du contenu de la structure
    SI result = 0 ALORS
        SI queue(file) - tete(file) = -1 ALORS
            result ← 1                         // file vide
        SINON
            *pelmt ← tabFile(file)[tete(file) MOD taille(file)]
            tete(file) ← tete(file) + 1
        FIN SI
    FIN SI
    RETOURNER result
FIN
```

**Précisions ajoutées.** La capacité doit être strictement positive. La vérification doit accepter des positions logiques supérieures à la capacité, tout en imposant `0 ≤ queue - tete + 1 ≤ taille`. Avec des entiers machine, une implantation durable doit aussi gérer leur dépassement ; ce point n'est pas développé dans le support.

## Récapitulatif — page 127

Piles et files stockent des données avec des règles précises d'insertion et de suppression : LIFO pour les piles, FIFO pour les files. Le choix d'une implantation statique, dynamique ou cyclique dépend des besoins. Ces structures interviennent dans le fonctionnement de l'ordinateur et dans de nombreux algorithmes, notamment ceux du cours suivant.
