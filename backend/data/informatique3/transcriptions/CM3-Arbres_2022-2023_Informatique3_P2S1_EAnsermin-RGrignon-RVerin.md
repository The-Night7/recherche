# Informatique 3 — CM3 : arbres (2022–2023)

Source : `PREING2-S1/Informatique3/CM3-Arbres_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.pdf` — 152 pages PDF. Eva Ansermin, Renaud Verin et Romuald Grignon ; version 1.01.

Transcription achevée le 11 octobre 2026. Texte natif intégral relu ; figures, codes et séquences de parcours confrontés aux rendus. Les animations sont regroupées avec leurs pages source. Comparaison du texte et des rendus des deux éditions : les différences portent sur la couverture et la présentation du parcours préfixe (pages 76–84), sans modification de l'arbre ni de l'algorithme. Les corrections ajoutées sont identifiées.

## Des listes aux arbres — pages 1–5

Une liste chaînée associe un élément et un pointeur `suivant`. Sa longueur n'est pas fixée à l'avance, dans la limite de la mémoire disponible. En donnant plusieurs successeurs à un chaînon, on peut construire une structure arborescente :

```c
typedef struct chainon {
    int elmt;
    struct chainon *suivant1;
    struct chainon *suivant2;
    struct chainon *suivant3;
} Chainon;
```

Le dessin montre une racine à trois enfants, eux-mêmes susceptibles d'avoir trois enfants. Un graphe est un ensemble d'éléments reliés entre eux. Les listes font partie des structures représentables par des graphes ; leur étude générale relève de la théorie des graphes.

## Définition et enracinement — pages 6–8

Un arbre est un graphe connexe et sans cycle. « Connexe » signifie que deux sommets quelconques peuvent être reliés par un chemin ; « sans cycle » exclut les boucles de parcours dans le graphe non orienté sous-jacent. On peut orienter ses arêtes.

**Schéma comparatif.** Le premier dessin relie les paires `1–2, 1–9, 1–3, 3–4, 3–5, 4–6, 4–7, 4–8` : c'est un arbre. Le second ajoute notamment les liaisons `2–6` et `4–5`, créant des cycles.

Un arbre non enraciné n'a pas de sommet privilégié. Choisir une racine permet d'établir des niveaux et d'orienter les liens du parent vers les enfants. Dans l'exemple enraciné : 1 a pour enfants 2 et 3 ; 3 a pour enfants 4 et 5 ; 4 a pour enfants 6, 7 et 8. Le dessin d'origine non enraciné comporte aussi un sommet 9, qui ne figure plus dans ce second dessin.

**Précision ajoutée.** Un graphe orienté seulement connexe et sans cycle orienté n'est pas nécessairement un arbre. La définition du support s'entend ici à partir d'un arbre non orienté, ensuite enraciné et orienté.

## Vocabulaire — pages 9–22

| Terme | Définition du support |
| --- | --- |
| Nœud | Élément de l'arbre |
| Racine | Nœud au sommet de l'arbre |
| Feuille, nœud externe | Nœud sans enfant, sans arc sortant |
| Nœud interne | Nœud qui n'est pas une feuille |
| Degré d'un nœud | Nombre de fils, donc d'arcs sortants dans cette convention |
| Frères ou sœurs | Nœuds ayant le même parent |
| Sous-arbre | Arbre issu d'un nœud et contenant ses descendants |
| Arbre numéroté | Nœuds étiquetés par des entiers positifs |
| Arbre ordonné | Les positions des enfants sont distinguées et ordonnées |
| Arbre $k$-aire | Chaque nœud a au plus $k$ enfants |
| Arbre binaire | Chaque nœud a au plus deux enfants |
| Profondeur | Distance, en nombre d'arêtes, depuis la racine |
| Hauteur | Profondeur maximale |

L'arbre de vocabulaire possède les enfants suivants : `1 → (2, 3, 4)`, `2 → (5)`, `3 → (6, 7)`, `4 → (8, 9)`, `5 → (10, 11)`, `7 → (12, 13, 14)`, `8 → (15, 16)`. Tous les autres nœuds sont des feuilles. C'est un arbre ternaire, de hauteur 3 : la racine est de profondeur 0, puis viennent les niveaux 1, 2 et 3. Les nœuds 12, 13 et 14 sont frères ; 7 est leur parent. Un sous-arbre est constitué d'un nœud et de toute la descendance qui lui est rattachée. Le dessin binaire supprime la branche issue de 3, laissant deux enfants au maximum à chaque nœud.

**Conventions et imprécisions de la source.** Le support définit la « taille » comme le nombre de **nœuds internes**, ici 7 ; le nombre total de nœuds du dessin est 16. Cette convention est conservée, mais d'autres cours appellent taille le nombre total de nœuds. La phrase sur le « $i$-ème enfant absent » ne doit pas confondre sa position avec l'étiquette numérique globale du nœud.

Les pages 14–15 rapprochent la liste simplement chaînée d'un arbre à un fils, puis la liste doublement chaînée d'une chaîne non orientée. Plus précisément, une liste simple sans cycle a **au plus** un fils par nœud, le dernier n'en ayant aucun. Les pointeurs aller et retour d'une liste double forment des arcs réciproques ; c'est son graphe sous-jacent, après identification des deux sens d'un même lien, qui est une chaîne non orientée.

## Utilisations — pages 23–25

Applications citées : compression, expressions arithmétiques, recherche, structures hiérarchiques, théorie des jeux, intelligence artificielle classique et compilation.

Le schéma de fichiers part d'un « Dossier Personnel » : Bureau (Document), Documents (Factures, Budget 2016, Projets), Images (Vacances, Anniversaire, Rando), Musique (Pop, Electro, Classique), Téléchargements (Logiciel, Document), Vidéos (Montage, Films, Séries). Un arbre de morpion représente les choix de coups successifs.

L'arbre syntaxique représente une séquence contenant une boucle `while` et `return a`. La condition compare `b` à 0 (`b != 0`) ; le corps contient un branchement comparant `a > b`, puis l'affectation `a = a - b` ou `b = b - a`. Opérateurs, variables et constantes deviennent des nœuds de l'arbre.

## Implantation binaire et création — pages 26–29

Le cours se limite aux arbres binaires, dont le nombre maximal d'enfants est connu. Une extension $k$-aire augmente le nombre de liens.

```text
Structure Arbre :
    elmt : Element
    fg, fd : pointeurs sur Arbre

FONCTION creerArbre(r : Element) : pointeur sur Arbre
VARIABLE noeud : pointeur sur Arbre
DEBUT
    noeud ← reserverMemoire(Arbre)
    elmt(noeud) ← r
    fg(noeud) ← NULL
    fd(noeud) ← NULL
    RETOURNER noeud
FIN
```

Le résultat est une feuille de valeur `r`. L'utilisation de nœuds alloués et de pointeurs permet de libérer leur mémoire ultérieurement. **Précondition implicite :** l'allocation réussit, ou `reserverMemoire` traite son échec ; le support ne montre pas cette vérification.

## Tests et accès aux enfants — pages 30–34

```text
FONCTION estFeuille(a : pointeur sur Arbre) : Booleen
    SI a = NULL ALORS ERREUR()
    SI fd(a) = NULL ET fg(a) = NULL ALORS RETOURNER VRAI
    SINON RETOURNER FAUX
FIN

FONCTION existeFilsGauche(a : pointeur sur Arbre) : Booleen
    SI a = NULL ALORS ERREUR()
    SINON SI fg(a) = NULL ALORS RETOURNER FAUX
    SINON RETOURNER VRAI
FIN

FONCTION existeFilsDroit(a : pointeur sur Arbre) : Booleen
    SI a = NULL ALORS ERREUR()
    SINON SI fd(a) = NULL ALORS RETOURNER FAUX
    SINON RETOURNER VRAI
FIN

FONCTION filsGauche(a : pointeur sur Arbre) : pointeur sur Arbre
    SI a = NULL ALORS ERREUR()
    SINON SI existeFilsGauche(a) ALORS RETOURNER fg(a)
    SINON RETOURNER NULL
FIN

FONCTION filsDroit(a : pointeur sur Arbre) : pointeur sur Arbre
    SI a = NULL ALORS ERREUR()
    SINON SI existeFilsDroit(a) ALORS RETOURNER fd(a)
    SINON RETOURNER NULL
FIN
```

`ERREUR()` doit arrêter l'opération. Une feuille existe et a deux enfants nuls ; elle ne se confond pas avec l'arbre vide.

## Modification et ajout — pages 35–38

```text
PROCEDURE modifierElement(a : pointeur sur Arbre, r : Element)
    SI a = NULL ALORS ERREUR()
    SINON elmt(a) ← r
FIN
```

La source ajoute à cette procédure un type de retour `pointeur sur Arbre`, mais ne retourne rien : le type de retour a été retiré de cette transcription de la procédure.

```text
FONCTION ajouterFilsGauche(a : pointeur sur Arbre, r : Element) : Booleen
    SI a = NULL ALORS
        a ← creerArbre(r)
        RETOURNER VRAI
    SINON SI NON existeFilsGauche(a) ALORS
        fg(a) ← creerArbre(r)
        RETOURNER VRAI
    SINON RETOURNER FAUX
FIN

FONCTION ajouterFilsDroit(a : pointeur sur Arbre, r : Element) : Booleen
    SI a = NULL ALORS
        a ← creerArbre(r)
        RETOURNER VRAI
    SINON SI NON existeFilsDroit(a) ALORS
        fd(a) ← creerArbre(r)
        RETOURNER VRAI
    SINON RETOURNER FAUX
FIN
```

**Erreur d'interface dans le cas nul.** Si `a` est passé par valeur comme un pointeur C, `a ← creerArbre(r)` ne modifie pas le pointeur de l'appelant : la racine nouvellement créée est perdue. Il faut soit imposer `a ≠ NULL` et créer séparément la racine, soit passer l'adresse du pointeur, soit retourner la nouvelle racine. Les branches d'ajout à un nœud existant modifient bien son champ enfant. Les dessins montrent une feuille 1 à laquelle est ajouté un fils de valeur `r`, à gauche ou à droite.

## Suppression d'un sous-arbre — pages 39–43

Libérer seulement le fils ne libère pas ses descendants et perd leur accès, provoquant une fuite mémoire. Il faut supprimer récursivement les descendants avant de libérer le nœud.

```text
PROCEDURE supprimerFilsGauche(a : pointeur sur Arbre)
    SI a = NULL ALORS ERREUR()
    SINON SI existeFilsGauche(a) ALORS
        SI existeFilsGauche(fg(a)) ALORS supprimerFilsGauche(fg(a))
        SI existeFilsDroit(fg(a)) ALORS supprimerFilsDroit(fg(a))
        libererMemoire(fg(a))
    FIN SI
FIN

PROCEDURE supprimerFilsDroit(a : pointeur sur Arbre)
    SI a = NULL ALORS ERREUR()
    SINON SI existeFilsDroit(a) ALORS
        SI existeFilsGauche(fd(a)) ALORS supprimerFilsGauche(fd(a))
        SI existeFilsDroit(fd(a)) ALORS supprimerFilsDroit(fd(a))
        libererMemoire(fd(a))
    FIN SI
FIN
```

**Omission du support :** ajouter `fg(a) ← NULL` immédiatement après sa libération dans la première procédure, et `fd(a) ← NULL` dans la seconde. Sans cela, le parent conserve un pointeur vers une zone libérée. Certains commentaires des étapes intermédiaires inversent « gauche » et « droit » ; les appels finaux ci-dessus suivent bien les champs concernés.

## Animation de suppression — pages 44–73

L'arbre employé dans les animations suivantes est :

```text
            1
          /   \
         2     8
        / \   / \
       3   6 9  10
      / \   \
     4   5   7
```

L'appel `supprimerFilsGauche` sur 1 descend au nœud 2, puis à 3. Il libère 4, puis 5, puis 3. Il explore ensuite la branche de 6 : 7 est libéré avant 6. Enfin 2 est libéré. Ordre des libérations : **4, 5, 3, 7, 6, 2**. La racine 1 et le sous-arbre droit `8(9,10)` restent présents. Les différentes couleurs des flèches distinguent les cadres d'appels récursifs ; elles ne désignent pas des arbres différents.

## Parcours : profondeur et largeur — pages 74–75

Un parcours visite tous les nœuds. Le support appelle **parcours en longueur** le parcours en profondeur : on termine un sous-arbre avant d'en explorer un autre, en allant vers les enfants avant les frères. Le parcours en largeur explore d'abord les nœuds d'un même niveau, puis le niveau suivant.

## Parcours préfixe — pages 76–84

On traite la racine, puis récursivement les sous-arbres de gauche à droite. Pour un arbre binaire : **R G D**, racine, gauche, droit.

```text
PROCEDURE parcoursPrefixe(a : pointeur sur Arbre)
    SI a ≠ NULL ALORS
        traiter(elmt(a))
        parcoursPrefixe(fg(a))
        parcoursPrefixe(fd(a))
    FIN SI
FIN
```

Sur l'arbre à dix nœuds représenté plus haut : **1, 2, 3, 4, 5, 6, 7, 8, 9, 10**. Le retour de 4 vers 3 ne traite pas une deuxième fois 3 ; il permet de passer à son sous-arbre droit, 5. Les étapes répétées matérialisent ces descentes et remontées.

## Parcours infixe — pages 85–140

Pour un arbre binaire, traiter le sous-arbre gauche, puis la racine, puis le sous-arbre droit : **G R D**. Le texte parle d'un parcours « en triangle ».

```text
PROCEDURE parcoursInfixe(a : pointeur sur Arbre)
    SI a ≠ NULL ALORS
        parcoursInfixe(fg(a))
        traiter(elmt(a))
        parcoursInfixe(fd(a))
    FIN SI
FIN
```

Parcours de l'arbre entier à dix nœuds : **4, 3, 5, 2, 6, 7, 1, 9, 8, 10**.

L'animation détaillée des pages 86–140 porte seulement sur le sous-arbre de racine 2. Elle descend successivement vers 3, puis 4, puis `NULL`. L'appel sur `NULL` retourne sans traitement. Elle traite 4, revient à 3 et le traite, parcourt 5, revient à 2 et le traite, puis parcourt 6 et son fils droit 7. Le résultat animé est donc **4, 3, 5, 2, 6, 7**, sans les valeurs de la partie extérieure au sous-arbre. Chaque retour d'appel reprend l'instruction qui suit l'appel récursif.

## Parcours en largeur avec une file — pages 141–152

Enfiler la racine ; tant que la file n'est pas vide, défiler un nœud, le traiter, puis enfiler ses enfants existants, gauche avant droit.

```text
PROCEDURE parcoursLargeur(a : pointeur sur Arbre)
VARIABLES noeud : pointeur sur Arbre ; f : File de pointeurs sur Arbre
DEBUT
    SI nonVide(a) ALORS
        creerFile(f)
        enfiler(f, a)
        TANT QUE NON fileVide(f) FAIRE
            noeud ← defile(f)
            traiter(noeud)
            SI existeFilsGauche(noeud) ALORS enfiler(f, fg(noeud))
            SI existeFilsDroit(noeud) ALORS enfiler(f, fd(noeud))
        FIN TANT QUE
    FIN SI
FIN
```

Le support transmet ici le nœud à `traiter`, alors que les parcours précédents transmettent son élément ; l'interface du traitement doit être adaptée à ce choix. `creerFile(f)` représente l'initialisation de la file selon la convention de passage choisie.

| Nœud retiré et traité | File après ajout de ses enfants |
| ---: | --- |
| État initial | 1 |
| 1 | 2, 8 |
| 2 | 8, 3, 6 |
| 8 | 3, 6, 9, 10 |
| 3 | 6, 9, 10, 4, 5 |
| 6 | 9, 10, 4, 5, 7 |
| 9 | 10, 4, 5, 7 |
| 10 | 4, 5, 7 |
| 4 | 5, 7 |
| 5 | 7 |
| 7 | Vide |

Résultat : **1, 2, 8, 3, 6, 9, 10, 4, 5, 7**. Les cases jaunes représentent la file des nœuds restant à traiter ; la case verte indique le nœud qui vient d'en sortir.
