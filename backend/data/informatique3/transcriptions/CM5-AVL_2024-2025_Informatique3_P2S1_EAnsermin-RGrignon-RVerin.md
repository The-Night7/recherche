# Informatique 3 — CM5 : AVL (2024–2025)

Eva Ansermin, Renaud Verin et Romuald Grignon — version 1.1, 198 pages PDF.

Source : `PREING2-S1/Informatique3/CM5-AVL_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.pdf`.

Transcription achevée le 11 octobre 2026. Texte natif relu ; codes, facteurs d'équilibre et arbres des animations confrontés aux rendus. Les étapes répétées sont regroupées avec les pages source. Les erreurs du support sont signalées séparément ; les algorithmes de suppression imprimés ne doivent pas être utilisés tels quels.

## I. Optimiser la recherche dans un ABR — pages 1–8

Un ABR impose une relation d'ordre, mais sa forme dépend de l'ordre d'insertion. Insérer successivement **1, 3, 5, 8, 9** produit une chaîne de fils droits, de racine 1. La recherche peut alors coûter $O(n)$. Le dessin équilibré contenant les mêmes valeurs est `3(1, 8(5,9))` ; sa hauteur est plus faible. Le nombre d'appels récursifs dépend de cette hauteur. Un arbre équilibré permet des opérations en $O(\log_2 n)$ au pire, tandis qu'un arbre filiforme peut imposer $O(n)$.

**Imprécision de la page 8.** La phrase « chaque nœud interne a le nombre maximum de fils » ne définit pas l'équilibre AVL. Un AVL peut avoir un nœud à un seul enfant. Le critère précis est la différence des hauteurs à chaque nœud, donnée ci-dessous. Le « meilleur cas » de la page 7 compare des formes d'arbres ; une recherche qui trouve immédiatement la racine reste en $O(1)$.

## II. Définition et facteur d'équilibre — pages 9–13

Un AVL est un arbre binaire de recherche qui conserve un équilibre de hauteur après les insertions et suppressions grâce à des rééquilibrages. Le facteur retenu dans tout ce support est :

$$b(a)=h(fd(a))-h(fg(a)).$$

Le critère AVL doit être vérifié **en chaque nœud** :

$$|b(a)|<2,\qquad b(a)\in\{-1,0,1\}.$$

Un facteur positif signifie que le sous-arbre droit est plus haut ; un facteur négatif, que le gauche est plus haut. Une convention cohérente est $h(NULL)=-1$ et une feuille de hauteur 0 ; ajouter une même constante aux hauteurs des sous-arbres non vides et vides ne change pas la différence si la convention est adaptée partout.

**Dessins du support.** Racine 10, fils 5 et 12 ; 5 possède 2 et 7, 2 un fils droit 4 ; 12 possède 13 à gauche et 15 à droite, 15 un fils droit 17. Le facteur de 12 vaut +1. Si l'on enlève le nœud gauche 13, il passe à +2 : l'arbre n'est plus équilibré en ce nœud.

**Erreur de valeurs du dessin :** 13 est placé à gauche de 12, donc l'ordre ABR n'est pas respecté. Les hauteurs illustrent le critère d'équilibre, mais ces valeurs ne constituent pas un exemple correct d'AVL.

## Structure et création d'un nœud — pages 14–16

```text
Structure Arbre :
    elmt : Element
    fg, fd : pointeurs sur Arbre
    equilibre : entier

FONCTION creerArbre(r : Element) : pointeur sur Arbre
    noeud ← reserverMemoire(Arbre)
    elmt(noeud) ← r
    fg(noeud) ← NULL
    fd(noeud) ← NULL
    equilibre(noeud) ← 0
    RETOURNER noeud
FIN
```

Le nouveau nœud est une feuille, d'équilibre nul. La vérification de l'allocation n'est pas détaillée dans le support.

## III. Recherche — pages 17–18

La recherche ne modifie pas l'arbre et n'exige aucun rééquilibrage. Cette version retourne l'adresse du nœud, plutôt qu'un booléen :

```text
FONCTION recherche(a : pointeur sur Arbre, e : Element) : pointeur sur Arbre
    SI a = NULL ALORS RETOURNER NULL
    SINON SI element(a) = e ALORS RETOURNER a
    SINON SI e < element(a) ALORS RETOURNER recherche(fg(a), e)
    SINON RETOURNER recherche(fd(a), e)
FIN
```

## Insertion : première étape et propagation — pages 19–27

Commencer comme dans un ABR : descendre à gauche ou à droite selon la comparaison, créer une feuille à la première position vide, ne rien ajouter si la valeur existe déjà.

```text
FONCTION insertionABR(a, e) : pointeur sur Arbre
    SI a = NULL ALORS RETOURNER creerArbre(e)
    SINON SI e < element(a) ALORS fg(a) ← insertionABR(fg(a), e)
    SINON SI e > element(a) ALORS fd(a) ← insertionABR(fd(a), e)
    FIN SI
    RETOURNER a
FIN
```

Ensuite, mettre à jour les équilibres en remontant. L'insertion d'une feuille fixe son équilibre à 0. Si la hauteur du sous-arbre gauche augmente, l'équilibre du parent diminue de 1 ; si celle du droit augmente, il augmente de 1. Seuls les ancêtres peuvent être concernés. La propagation s'arrête dès que la hauteur du sous-arbre courant ne change plus.

Le support appelle `h` une « différence d'équilibre ». **Précision :** à la sortie d'un appel récursif, `*h` représente la variation de **hauteur** du sous-arbre. Son signe est inversé après un retour du fils gauche pour devenir la variation du facteur d'équilibre du parent. Confondre ces deux rôles conduit à des erreurs, particulièrement lors d'une suppression.

## Animation : insertion de 9 — pages 28–65

Arbre initial :

```text
           10
         /    \
        5      15
       / \    /  \
      2   8  12  18
```

Tous les équilibres valent 0. Descendre par `10 → 5 → 8 → fils droit NULL` et créer 9 à droite de 8. Au retour :

| Nœud | Nouvel équilibre | Variation de hauteur retournée |
| ---: | ---: | ---: |
| Nouvelle feuille 9 | 0 | +1 |
| 8 | +1 | +1 |
| 5 | +1 | +1 |
| 10 | −1 | +1 |

À 10, la croissance vient du fils gauche : la variation d'équilibre vaut −1. Aucun facteur n'atteint ±2, donc aucune rotation n'est nécessaire. Les cadres `*h = ??`, `1` et `−1` suivent la valeur partagée au cours des appels et des retours.

## Animation : insertion de 1 — pages 66–100

Partir de l'arbre précédent, où 9 a été inséré. Descendre `10 → 5 → 2 → fils gauche NULL`, puis créer 1. L'équilibre de 2 devient −1 ; sa hauteur augmente de 1. L'équilibre de 5 passe de +1 à 0 : ses deux branches ont maintenant la même hauteur, mais sa hauteur totale ne change pas. Il retourne donc `*h = 0`. L'équilibre de 10 reste −1 ; aucune modification ne se propage plus haut. Le facteur de 8 reste +1, celui de 9 et de 1 vaut 0.

## Insertion complète avec équilibrage — page 101

La version des pages 27–100 ne faisait que mettre à jour les facteurs. La page 101 ajoute l'appel de rééquilibrage après cette mise à jour :

```text
FONCTION insertionAVL(a : pointeur sur Arbre, e : Element,
                      h : pointeur sur entier) : pointeur sur Arbre
    SI a = NULL ALORS
        *h ← 1
        RETOURNER creerArbre(e)
    SINON SI e < element(a) ALORS
        fg(a) ← insertionAVL(fg(a), e, h)
        *h ← -*h
    SINON SI e > element(a) ALORS
        fd(a) ← insertionAVL(fd(a), e, h)
    SINON
        *h ← 0
        RETOURNER a
    FIN SI
    SI *h ≠ 0 ALORS
        equilibre(a) ← equilibre(a) + *h
        a ← equilibrerAVL(a)
        SI equilibre(a) = 0 ALORS *h ← 0
        SINON *h ← 1
        FIN SI
    FIN SI
    RETOURNER a
FIN
```

La source nomme l'appel `equilibrageAVL`, puis définit `equilibrerAVL` page 196 : le nom est harmonisé ici. Les exemples abrègent parfois l'appel en omettant `h` ; l'interface complète exige un pointeur valide sur entier. L'appelant récupère toujours la nouvelle racine.

## Suppression : principe — pages 102–103

Procéder comme dans un ABR : retirer une feuille, remplacer un nœud à un enfant par celui-ci, ou remplacer la valeur par le minimum du sous-arbre droit ou le maximum du sous-arbre gauche. Mettre ensuite à jour les facteurs en remontant, puis rééquilibrer si nécessaire. Plusieurs ancêtres peuvent nécessiter une rotation.

Le premier exemple supprime 8 de l'arbre initial à sept nœuds : 5 n'a plus que son fils gauche 2 ; son facteur passe de 0 à −1. Sa hauteur ne change pas, donc l'équilibre de 10 reste 0.

## Algorithme de suppression imprimé — page 104

**Transcription de la source, avec ses erreurs, non corrigée dans ce bloc.** L'encadré latéral est intégré à l'endroit indiqué par sa flèche.

```text
FONCTION suppressionAVL(a : ptr sur Arbre, e : Element,
                        h : ptr sur Element) : ptr sur Arbre
VARIABLE tmp : ptr sur Arbre
DEBUT
    SI a = NULL ALORS
        *h ← 1
        RETOURNER a
    SINON SI e > element(a) ALORS
        fd(a) ← suppressionAVL(fd(a), e)
    SINON SI e < element(a) ALORS
        fg(a) ← suppressionAVL(fg(a), e)
        *h ← -*h
    SINON SI existeFilsDroit(a) ALORS
        fg(a) ← suppMinAVL(fd(a), h, adresse(element(a)))
    SINON
        tmp ← a
        a ← fg(a)
        liberer(tmp)
        *h ← -1
    FIN SI
    SI a = NULL ALORS *h ← 0
    SI *h ≠ 0 ALORS
        equilibre(a) ← equilibre(a) + *h
        SI equilibre(a) = 0 ALORS *h ← 0
        SINON *h ← 1
        FIN SI
    FIN SI
    RETOURNER a
FIN
```

**Erreurs et corrections nécessaires :**

- `h` doit pointer sur un entier ; il manque comme troisième argument des deux appels récursifs.
- Si `a = NULL` à l'entrée, aucune valeur n'a été retirée : `*h` doit valoir 0, et non 1.
- Le résultat de `suppMinAVL(fd(a), ...)` doit être affecté à **`fd(a)`**, et non `fg(a)`. Les pages d'animation suivantes corrigent ce champ.
- Après avoir remplacé le nœud par son enfant, il faut retourner immédiatement la nouvelle racine avec `*h = -1`, sans modifier le facteur de l'enfant. Mettre `*h = 0` parce que le résultat est vide masque la diminution de hauteur.
- La propagation finale recopie à tort celle de l'insertion. Pour une suppression valide, après mise à jour et rééquilibrage, un facteur nul conduit à propager une diminution de hauteur (`*h = -1`), un facteur non nul à arrêter (`*h = 0`), dans le schéma de mise à jour utilisé ici.
- L'appel de rééquilibrage manque dans cette première version ; la page 142 l'ajoute après la mise à jour du facteur. Il doit aussi être présent dans la suppression du minimum lorsque celle-ci modifie une hauteur.

Ces corrections portent sur le comportement, pas uniquement sur la typographie. Le PDF ne fournit pas de version finale débarrassée de toutes ces erreurs.

## Suppression du minimum — page 105

```text
FONCTION suppMinAVL(a : Arbre, h : pointeur sur entier,
                    pe : pointeur sur Element) : pointeur sur Arbre
VARIABLE tmp : pointeur sur Arbre
DEBUT
    SI fg(a) = NULL ALORS
        *pe ← element(a)
        *h ← -1
        tmp ← a
        a ← fd(a)
        liberer(tmp)
        RETOURNER a
    SINON
        fg(a) ← suppMinAVL(fg(a), h, pe)
        *h ← -*h
    FIN SI
    SI *h ≠ 0 ALORS
        equilibre(a) ← equilibre(a) + *h
        SI equilibre(a) = 0 ALORS *h ← -1
        SINON *h ← 0
        FIN SI
    FIN SI
    RETOURNER a
FIN
```

**Notes.** Le paramètre `a` est un pointeur sur arbre non nul, malgré le type abrégé de la source ; `h` et `pe` doivent être valides. Insérer `a ← equilibrerAVL(a)` après la mise à jour du facteur et avant le calcul de la variation de hauteur. Sans cet ajout, cette fonction peut laisser un sous-arbre déséquilibré.

## Animation : suppression de 20 — pages 106–142

Arbre initial :

```text
             15
           /    \
         10      20
        /  \    /  \
       5   12  17  50
      / \         /  \
     2   8       40  55
```

Facteurs initiaux : 15 vaut 0 ; 10 vaut −1 ; 20 vaut +1 ; tous les autres valent 0. On descend de 15 à 20. Comme 20 possède un fils droit, chercher le minimum du sous-arbre 50 : descendre à gauche, vers 40. Le pointeur `pe` désigne le champ qui contient encore 20. Copier 40 dans ce champ, puis libérer l'ancienne feuille 40 et mettre le fils gauche de 50 à `NULL`.

La suppression de la feuille retourne une variation de hauteur −1. Au niveau de 50, cette variation vient de gauche : son facteur passe de 0 à +1. Sa hauteur est inchangée, donc il retourne `*h = 0`. Le nœud qui contient maintenant 40 conserve son facteur +1 et la racine 15 son facteur 0. Aucune rotation n'est nécessaire dans cet exemple. La figure finale contient `15(10(5(2,8),12),40(17,50(NULL,55)))`.

Cet exemple particulier n'active pas tous les cas erronés de la fonction générale. La page 142 indique l'endroit où ajouter l'appel `equilibrageAVL` ; cela ne corrige pas à lui seul les erreurs précédemment listées.

## IV. Rotation simple à gauche — pages 143–160

L'équilibrage dépend du côté où la hauteur est excessive. Premier cas : une croissance dans la branche droite du fils droit.

L'exemple part de `10(5(2,8),15(12,18(NULL,20)))`. Insérer 21 à droite de 20 fait passer l'équilibre de 20 à +1 et celui de 18 à +2. La rotation se limite au sous-arbre de racine 18 : 20 devient sa racine, avec 18 à gauche et 21 à droite. Ces trois facteurs deviennent 0. Le sous-arbre rééquilibré est réattaché comme fils droit de 15.

Schéma général : avant la rotation, `a` a pour fils gauche $T_1$ et pour fils droit le pivot `p`, dont les fils sont $T_2,T_3$. Après rotation, `p` est la racine, son fils gauche est `a(T_1,T_2)` et son fils droit est $T_3$. L'ordre infixe $T_1<a<T_2<p<T_3$ est conservé.

L'exemple numérique utilise `a = 3`, `p = 6`, $T_1=1$, $T_2=4$, $T_3=8(7,9)$. Après rotation : `6(3(1,4),8(7,9))`.

```text
FONCTION rotationGauche(a : pointeur sur Arbre) : pointeur sur Arbre
    pivot ← fd(a)
    fd(a) ← fg(pivot)
    fg(pivot) ← a
    eq_a ← equilibre(a)
    eq_p ← equilibre(pivot)
    equilibre(a) ← eq_a - max(eq_p, 0) - 1
    equilibre(pivot) ← min(eq_a - 2, eq_a + eq_p - 2, eq_p - 1)
    a ← pivot
    RETOURNER a
FIN
```

Les anciennes valeurs `eq_a` et `eq_p` doivent être mémorisées avant de calculer les nouvelles. Préconditions : `a` et son fils droit existent, et les facteurs sont à jour. Les figures distinguent les cas `(b(a),b(p)) = (2,1)`, donnant `(0,0)`, et `(2,0)`, donnant pour l'ancienne racine +1 et pour le pivot −1. Ce dernier cas intervient notamment après une suppression.

## Rotation simple à droite — pages 161–171

Cas symétrique : croissance dans la branche gauche du fils gauche. Le dessin part de `10(5(4(3,NULL),8),15(12,18))`, puis ajoute 2 à gauche de 3. La rotation droite de racine 4 et pivot 3 donne `3(2,4)` ; ce sous-arbre reste le fils gauche de 5. La racine 10 et 5 ont finalement un facteur −1, les nœuds 2, 3 et 4 un facteur 0.

**Note sur les annotations.** Les facteurs affichés dans certains dessins intermédiaires ne sont pas tous encore actualisés ; les valeurs 0 portées par 10 et 5 avant la rotation ne correspondent déjà plus à la hauteur de leurs branches.

```text
FONCTION rotationDroite(a : pointeur sur Arbre) : pointeur sur Arbre
    pivot ← fg(a)
    fg(a) ← fd(pivot)
    fd(pivot) ← a
    eq_a ← equilibre(a)
    eq_p ← equilibre(pivot)
    equilibre(a) ← eq_a - min(eq_p, 0) + 1
    equilibre(pivot) ← max(eq_a + 2, eq_a + eq_p + 2, eq_p + 1)
    a ← pivot
    RETOURNER a
FIN
```

Préconditions symétriques. Si les facteurs initiaux sont `(-2,-1)`, les nouveaux sont `(0,0)` ; pour `(-2,0)`, l'ancienne racine prend −1 et le pivot +1. Les trois sous-arbres conservent leur ordre infixe.

## Rotation simple après suppression — pages 172–173

Arbre initial : `10(5(3,NULL),20(15(13,17),26(NULL,29)))`. Supprimer 3 réduit la hauteur du fils gauche de 10 ; son facteur passe de +1 à +2. Son fils droit 20 a un facteur 0. Une rotation gauche de pivot 20 donne :

```text
              20
            /    \
          10      26
         /  \       \
        5   15      29
           /  \
          13  17
```

Le facteur de 20 vaut −1, celui de 10 +1, celui de 26 +1. L'arbre respecte de nouveau le critère AVL, même si tous les facteurs ne sont pas nuls.

## Rotation double gauche, ou droite-gauche — pages 174–187

Cas où `a` est trop haut à droite, mais où son fils droit est plus haut à gauche. Exemple : `10(5(3,NULL),20(15(13,17),26))`. Après suppression de 3, 10 a un facteur +2 et son fils droit 20 un facteur −1.

Une simple rotation gauche donne une racine 20 de facteur −2 : le problème n'est pas résolu. Il faut d'abord faire une rotation **droite** du sous-arbre droit, autour de 15, puis une rotation **gauche** de 10, autour de 15. Résultat :

```text
             15
           /    \
         10      20
        /  \    /  \
       5   13  17  26
```

```text
FONCTION doubleRotationGauche(a : pointeur sur Arbre) : pointeur sur Arbre
    fd(a) ← rotationDroite(fd(a))
    RETOURNER rotationGauche(a)
FIN
```

Schéma général : `A` a pour fils droit `B`, dont le fils gauche est `P`. `P` devient la racine avec `A` à gauche et `B` à droite ; ses deux anciens sous-arbres intermédiaires deviennent respectivement le fils droit de `A` et le fils gauche de `B`. Les quatre sous-arbres périphériques restent dans le même ordre.

Pour les figures de facteurs `b(A)=2`, `b(B)=-1` :

| Ancien facteur de P | Nouveau facteur de A | Nouveau facteur de B | Nouveau facteur de P |
| ---: | ---: | ---: | ---: |
| −1 | 0 | +1 | 0 |
| 0 | 0 | 0 | 0 |
| +1 | −1 | 0 | 0 |

## Rotation double droite, ou gauche-droite — pages 188–193

Cas symétrique : le sous-arbre gauche est trop haut, avec une croissance du côté droit de ce sous-arbre. `A` a un facteur −2 ; son fils gauche `B` un facteur +1 ; `P = fd(B)` devient la nouvelle racine.

```text
FONCTION doubleRotationDroite(a : pointeur sur Arbre) : pointeur sur Arbre
    fg(a) ← rotationGauche(fg(a))
    RETOURNER rotationDroite(a)
FIN
```

Après les deux rotations, `B` est le fils gauche de `P`, `A` son fils droit ; les quatre sous-arbres restent ordonnés.

| Ancien facteur de P | Nouveau facteur de B | Nouveau facteur de A | Nouveau facteur de P |
| ---: | ---: | ---: | ---: |
| −1 | 0 | +1 | 0 |
| 0 | 0 | 0 | 0 |
| +1 | −1 | 0 | 0 |

## Choix de la rotation — pages 194–196

| Facteur du nœud | Facteur de l'enfant du côté haut | Opération |
| --- | --- | --- |
| +2 | Fils droit ≥ 0 | Rotation simple gauche |
| +2 | Fils droit < 0 | Double rotation gauche |
| −2 | Fils gauche ≤ 0 | Rotation simple droite |
| −2 | Fils gauche > 0 | Double rotation droite |

```text
FONCTION equilibrerAVL(a : pointeur sur Arbre) : pointeur sur Arbre
    SI equilibre(a) ≥ 2 ALORS
        SI equilibre(fd(a)) ≥ 0 ALORS RETOURNER rotationGauche(a)
        SINON RETOURNER doubleRotationGauche(a)
        FIN SI
    SINON SI equilibre(a) ≤ -2 ALORS
        SI equilibre(fg(a)) ≤ 0 ALORS RETOURNER rotationDroite(a)
        SINON RETOURNER doubleRotationDroite(a)
        FIN SI
    FIN SI
    RETOURNER a
FIN
```

La casse `A/a` est harmonisée. Cette fonction suppose un nœud non nul et un déséquilibre local issu d'une opération sur un AVL précédemment valide. Les comparaisons larges `≥ 2` et `≤ −2` du support ne garantissent pas qu'une seule rotation réparerait n'importe quel arbre arbitrairement déséquilibré.

## Complexité et récapitulatif — pages 197–198

Une rotation simple ou double coûte $O(1)$. Après insertion, un seul rééquilibrage local suffit, avec une rotation simple ou deux rotations simples constituant une rotation double. Après suppression, des rééquilibrages peuvent être nécessaires sur plusieurs ancêtres. La hauteur d'un AVL de $n$ nœuds est logarithmique, donc recherche, insertion et suppression ont un coût $O(\log n)$ au pire, lorsque les algorithmes et facteurs sont correctement maintenus.

Les AVL conservent l'ordre de l'ABR et l'équilibre des hauteurs grâce aux rotations autour d'un pivot. Le support cite aussi les arbres rouge-noir comme autre famille d'arbres autoéquilibrés. La convention de signe reste **hauteur droite moins hauteur gauche**, même si la dernière diapositive parle seulement d'une différence entre gauche et droite.
