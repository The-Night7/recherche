# Informatique 3 — CM1 : listes chaînées (2024–2025)

Source : `PREING2-S1/Informatique3/CM1-Listes-Chainee_2024-2025_Informatique3_P2S1_EAnsermin-RGrignon.pdf` — 88 pages PDF.

Transcription achevée le 11 octobre 2026. Texte natif relu ; schémas mémoire, animations de pointeurs, tableaux et codes confrontés aux pages rendues. Les étapes répétées sont regroupées avec leurs pages source. Les deux éditions ont été comparées ; les différences sont conservées. Les corrections ajoutées sont identifiées.

## Présentation, organisation et évaluations — pages 1–3

Eva Ansermin et Romuald Grignon — version 1.3. Algorithmique : listes chaînées, piles, files et arbres ; introduction à Unix et au shell. Le semestre comporte 6 CM d'algorithmique, 2 CM d'Unix, et 13 semaines de TD : 7 d'algorithmique, 3 d'Unix et 3 de projet. Trois DS : deux de 90 minutes et un de 120 minutes. La moyenne des quiz compte comme une note de DS.

$$\mathrm{Note}=0{,}7\max\bigl(\mathrm{moy}(DS1,DS2,DS3,QUIZ),DS3\bigr)+0{,}3\,PROJET.$$

Des quiz réguliers commencent en octobre, au début du TD. La page de cours indiquée est `https://cours.cyu.fr/course/view.php?id=338` : cours, TD, quiz d'entraînement, anciens DS, groupes et modalités d'évaluation. Consigne : s'inscrire au cours avec son groupe. Ces informations sont celles de l'édition du support.

## Rappels : pointeurs — pages 4–15

Un pointeur est une variable dont la valeur est l'adresse d'une autre variable. L'opérateur `&` donne une adresse ; `*` permet d'accéder à la valeur située à cette adresse.

```c
int main(void) {
    int a;
    int *p1 = NULL;
    a = 5;
    p1 = &a;
    printf(" a =%d \n", a);
    printf("*p1=%d \n", *p1);
    *p1 = 10;
    printf(" a =%d \n", a);
    return 0;
}
```

Le support juxtapose le programme et sa traduction en pseudo-code :

```text
VARIABLES a : entier ; p1 : pointeur sur entier
DEBUT
    a ← 5
    p1 ← adresse(a)
    ECRIRE(a)
    ECRIRE(valeur(p1))
    valeur(p1) ← 10
    ECRIRE(a)
FIN
```

**Animation mémoire.** `a`, à l'adresse illustrative 1154, n'est pas initialisé ; `p1` vaut d'abord `NULL`. Après `a = 5`, la case de `a` contient 5. Après `p1 = &a`, le pointeur contient 1154 : il désigne cette même case. `*p1 = 10` remplace sa valeur par 10 sans changer l'adresse. Les affichages donnent successivement `a = 5`, `*p1 = 5`, `a = 10`. La variable pointeur possède elle-même une adresse, 10032 dans le schéma. Les autres adresses montrées ne représentent pas des variables supplémentaires du programme.

**Notes de transcription.** Le dessin de la sortie omet parfois l'astérisque devant `p1` ; c'est la valeur pointée qui est affichée. L'extrait nécessite `<stdio.h>`. Les adresses du dessin sont pédagogiques et ne décrivent pas une implantation C à reproduire.

## Tableaux et limites — pages 16–17

Un tableau réserve des cases contiguës en mémoire. Sa taille doit être connue au moment de la réservation, y compris pour une allocation dynamique. L'exemple `tab[5]` initialisé par `{1, 3}` représente les valeurs `1, 3, 0, 0, 0` ; le dessin relie le nom `tab` à la première case, d'adresse 1154, et montre des cases successives espacées de la taille d'un entier.

Surdimensionner un tableau gaspille de la mémoire et impose malgré tout une limite à l'utilisateur. Une liste chaînée permet de faire évoluer le nombre d'éléments sans réserver d'avance un bloc de cette taille.

**Précision sur le C.** Le support appelle le nom du tableau un « pointeur constant ». Un objet tableau n'est pas un objet pointeur : son nom est converti en pointeur vers son premier élément dans de nombreuses expressions, mais pas dans toutes, notamment avec `sizeof` et `&`. Le dessin d'une case séparée contenant son adresse est une représentation conceptuelle.

## I. Principe des listes chaînées — pages 18–29

Les éléments d'une liste ne sont pas nécessairement contigus. Chaque élément est accompagné d'un pointeur vers le suivant : l'ensemble constitue un **chaînon**. L'élément peut être un entier, un réel ou une structure, par exemple `Etudiant`.

```text
Structure Chainon :
    elmt : Element
    suivant : pointeur sur Chainon
```

Déclaration C proposée dans le support :

```c
struct chainon {
    int nombre;
    struct chainon *suivant;
};
typedef struct chainon Chainon;
```

Autre écriture équivalente :

```c
typedef struct chainon {
    int nombre;
    struct chainon *suivant;
} Chainon;
```

Un pointeur de tête désigne le premier chaînon ; le dernier a son champ `suivant` égal à `NULL`.

```text
pliste → [élément | suivant] → [élément | suivant] → … → NULL
```

**Incohérence de nom dans la source.** La structure C utilise `nombre`, mais les fonctions suivantes emploient `elmt`. Pour les réunir dans un programme, il faut utiliser partout le même nom. Dans les fonctions transcrites ci-dessous, le champ s'appelle `elmt`.

## Exemple d'implantation mémoire — page 30

La liste représentée est `10 → 2 → 25 → 103 → NULL`. `pliste`, stocké à l'adresse 1000, contient 1152.

| Adresse du chaînon | Élément | Adresse de son champ suivant | Contenu du champ suivant |
| --- | ---: | --- | --- |
| 1152 | 10 | 1160 | 5344 |
| 5344 | 2 | 5352 | 10016 |
| 10016 | 25 | 10024 | 22222 dans le PDF |
| 22216 | 103 | 22224 | 0, représentant `NULL` |

Les cases intermédiaires et les points de suspension illustrent des espaces mémoire ; les chaînons peuvent être éloignés.

**Erreur dans le dessin.** Pour désigner le dernier chaînon tel qu'il est placé dans le tableau, le troisième champ `suivant` devrait contenir **22216**, et non 22222.

## II. Initialisation et création — pages 31–36

Initialiser la liste vide consiste à affecter `NULL` au pointeur de tête. Pour obtenir une liste à un élément, créer un chaînon, renseigner sa valeur, fixer son suivant à `NULL`, puis faire pointer la tête dessus. Les schémas utilisent la valeur 10.

```c
Chainon *creationChainon(void) {
    Chainon *c = malloc(sizeof(Chainon));
    if (c == NULL) {
        exit(1);
    }
    printf("Entrer la valeur : ");
    if (scanf("%d", &(c->elmt)) != 1) {
        exit(2);
    }
    c->suivant = NULL;
    return c;
}
```

Dans `main` : déclarer `Chainon *pliste = NULL;`, puis affecter `pliste = creationChainon();`. La suite du programme est laissée sous forme de points de suspension dans la source.

**Notes.** Le support alterne `pliste` et `pListe` dans cet appel ; la casse est harmonisée ici. Les fonctions nécessitent `<stdlib.h>` et `<stdio.h>`. La gestion d'erreur du support arrête le programme ; elle n'est pas une interface générale de bibliothèque.

## Parcours — pages 37–44

Un pointeur temporaire `p1` parcourt `10 → 2 → 25 → 103 → NULL`. Initialement `p1 = pliste`, puis on traite l'élément, on avance avec `p1 = p1->suivant`, et on recommence jusqu'à `NULL`. Le pointeur de tête reste inchangé.

```text
PROCEDURE traiterListe(pliste : pointeur sur Chainon)
VARIABLE p1 : pointeur sur Chainon
DEBUT
    p1 ← pliste
    TANT QUE p1 ≠ NULL FAIRE
        traiter(element(p1))
        p1 ← suivant(p1)
    FIN TANT QUE
FIN
```

On doit parcourir les éléments un à un : on ne peut pas utiliser un indice comme pour accéder directement à une case de tableau. La source ferme le pseudo-code par une accolade ; la fermeture est harmonisée en `FIN`.

## Ajout en fin de chaîne — pages 45–50

L'animation insère 7 à la fin de `10 → 5 → 12 → NULL` :

1. Créer le chaînon 7, dont le suivant vaut `NULL`.
2. Partir de la tête et parcourir jusqu'au dernier chaînon, 12.
3. Faire pointer le suivant de 12 sur le nouveau chaînon.

```text
FONCTION insertFin(pliste : pointeur sur Chainon) : pointeur sur Chainon
VARIABLES nouveau, p1 : pointeurs sur Chainon
DEBUT
    nouveau ← creationChainon()
    p1 ← pliste
    TANT QUE suivant(p1) ≠ NULL FAIRE
        p1 ← suivant(p1)
    FIN TANT QUE
    suivant(p1) ← nouveau
    RETOURNER pliste
FIN
```

**Précondition omise dans le support :** cette version suppose la liste non vide. Si `pliste = NULL`, elle accède à `suivant(NULL)`. Pour gérer la liste vide, ajouter après la création : `SI pliste = NULL ALORS RETOURNER nouveau`. Sans pointeur de queue, le parcours prend $O(n)$.

## Ajout en tête — pages 51–56

Pour passer de `10 → 5 → 12` à `7 → 10 → 5 → 12`, créer le nouveau chaînon, le relier à l'ancienne tête, puis seulement déplacer la tête.

```text
FONCTION insertDebut(pliste : pointeur sur Chainon) : pointeur sur Chainon
VARIABLE nouveau : pointeur sur Chainon
DEBUT
    nouveau ← creationChainon()
    suivant(nouveau) ← pliste
    pliste ← nouveau
    RETOURNER pliste
FIN
```

Complexité temporelle : $O(1)$. Le pointeur de tête est modifié : il faut le retourner et récupérer sa nouvelle valeur chez l'appelant.

**Contre-exemple animé.** Si l'on affecte d'abord `pliste ← nouveau`, puis `suivant(nouveau) ← pliste`, le chaînon 7 se désigne lui-même : on crée une boucle et on perd l'accès au reste de la liste.

## Ajout au milieu — pages 57–64

Insertion de 7 entre 5 et 12 dans `10 → 5 → 12` : placer `p1` sur 5, créer le nouveau chaînon, puis exécuter **dans cet ordre** :

```text
suivant(nouveau) ← suivant(p1)
suivant(p1) ← nouveau
```

Résultat : `10 → 5 → 7 → 12 → NULL`. Les premiers états créent le chaînon avant le parcours ; le récapitulatif effectue le parcours avant sa création. Les deux conviennent si le parcours réussit. Inverser les deux affectations crée une boucle sur 7 et perd la suite, ici 12.

Pseudo-code imprimé dans le support :

```text
FONCTION insertPos(pliste : pointeur sur Chainon, pos : entier) : pointeur sur Chainon
VARIABLES nouveau, p1 : pointeurs sur Chainon ; i : entier
DEBUT
    SI pos = 0 OU pliste = NULL ALORS
        pliste ← insertDebut(pliste)
    SINON
        p1 ← pliste
        POUR i DE 0 A pos FAIRE
            SI p1 = NULL ALORS
                ERREUR()
            SINON
                p1 ← suivant(p1)
            FIN SI
        FIN POUR
        nouveau ← creationChainon()
        suivant(nouveau) ← suivant(p1)
        suivant(p1) ← nouveau
    FIN SI
    RETOURNER pliste
FIN
```

**Erreur de bornes.** Pour insérer à l'indice `pos` compté depuis 0, il faut atteindre le prédécesseur, donc avancer de `pos − 1` liens lorsque `pos > 0`. La boucle imprimée avance trop loin et peut laisser `p1 = NULL` avant l'affectation. Le cas de liste vide accepte aussi à tort n'importe quelle position.

**Correction ajoutée, distincte de la source :**

```text
FONCTION insertPosCorrige(pliste, pos)
    SI pos < 0 ALORS ERREUR()
    SI pos = 0 ALORS RETOURNER insertDebut(pliste)
    p1 ← pliste
    POUR i DE 1 A pos - 1 FAIRE
        SI p1 = NULL ALORS ERREUR()
        p1 ← suivant(p1)
    FIN POUR
    SI p1 = NULL ALORS ERREUR()
    nouveau ← creationChainon()
    suivant(nouveau) ← suivant(p1)
    suivant(p1) ← nouveau
    RETOURNER pliste
FIN
```

Ici `ERREUR()` interrompt l'opération. Les positions admises vont de 0 à la longueur de la liste, bornes incluses.

## Suppression — pages 65–71

Pour supprimer la tête de `10 → 2 → 25 → 103`, mémoriser son adresse, déplacer la tête sur le suivant, puis libérer l'ancien premier chaînon. Résultat : `2 → 25 → 103`. Libérer la mémoire évite une fuite de RAM.

```c
Chainon *suppDebut(Chainon *pliste) {
    Chainon *p1;
    if (pliste == NULL) {
        exit(1);
    }
    p1 = pliste;
    pliste = p1->suivant;
    free(p1);
    return pliste;
}
```

**Exercice du support :** supprimer un chaînon en milieu de chaîne. La diapositive montre la liste `10 → 2 → 25 → 103`, sans algorithme corrigé.

## III. Listes doublement chaînées — pages 72–78

Une liste simplement chaînée ne possède qu'un lien vers le suivant. Une liste doublement chaînée ajoute un lien vers le précédent et peut se parcourir dans les deux sens ; elle est plus complexe à implémenter.

```text
Structure Chainon :
    elmt : Element
    suivant : pointeur sur Chainon
    precedent : pointeur sur Chainon

NULL ← 10 ⇄ 2 ⇄ 25 ⇄ 103 → NULL
```

Insertion illustrée : le nouveau chaînon 8 est placé entre 1 et 3 dans `10 ⇄ 1 ⇄ 3 ⇄ 10`. Avec `p1` sur 1 :

```text
precedent(nouveau) ← p1
suivant(nouveau) ← suivant(p1)
precedent(suivant(p1)) ← nouveau
suivant(p1) ← nouveau
```

On obtient `10 ⇄ 1 ⇄ 8 ⇄ 3 ⇄ 10`. Le nouveau chaînon commence avec ses deux liens à `NULL`.

**Précondition du dessin :** `p1` et son suivant existent. Une insertion en queue nécessite un traitement distinct du lien de retour, car `precedent(NULL)` n'est pas défini.

## IV. Liste chaînée ou tableau ? — pages 79–87

Tableau récapitulatif du support, apparu progressivement :

| Critère | Tableau | Liste chaînée |
| --- | --- | --- |
| Nombre d'éléments | Fixe | « Illimité et non fixé » |
| Données contiguës | Oui | Non |
| Espace mémoire | Éléments + un pointeur, selon le dessin | Un ou plusieurs pointeurs associés à chaque élément |
| Ajout/suppression | Décalage des éléments : $O(n)$ | $O(1)$ en bout de chaîne ; $O(n)$ sinon |
| Accès à un élément | Accès direct : $O(1)$ | $O(1)$ en bout de chaîne ; $O(n)$ sinon |

**Précisions ajoutées.** « Illimité » signifie sans taille fixée d'avance, dans la limite de la mémoire disponible. Un tableau C n'exige pas un objet pointeur séparé. Pour une liste simplement chaînée possédant seulement une tête, l'accès, l'insertion et la suppression en tête sont constants ; atteindre la queue est linéaire. Un pointeur de queue rend son accès et l'ajout en queue constants, mais ne suffit pas à supprimer le dernier chaînon sans chercher son prédécesseur. Au milieu, la modification des liens est constante si les pointeurs nécessaires sont déjà connus ; leur recherche peut être linéaire. Le coût annoncé pour un tableau concerne les opérations avec décalage, pas tous les ajouts possibles en fin d'un espace déjà réservé.

Les listes chaînées ne sont pas toujours la meilleure solution : le choix dépend des opérations nécessaires.

## Récapitulatif du support — page 88

Une liste associe des éléments et des pointeurs indiquant l'emplacement du suivant et, éventuellement, du précédent. Il faut maîtriser les structures et les pointeurs. Le nombre d'éléments peut évoluer ; certaines opérations sont simplifiées par rapport aux tableaux. Ce principe sert de base à de nombreux objets informatiques et à la suite du programme d'algorithmique de deuxième année.
