---
source: TD4-Arbres_2024-2025_Informatique3_P2S1_DInformatique.pdf, pages 1-3
transcription: manuelle
---

# TD 04 : Arbres

> **Note :** la correction de ce TD est rédigée dans le document 2024-10-30-TD4-Arbres-Correction_2024-2025 (AhmedA) ; le même énoncé corrigé se trouve aussi dans la transcription de TD04-Arbres_2023-2024.

Consignes générales : créer un répertoire consacré au TD et y enregistrer ses codes. Pour compiler : `gcc -o nom_executable nom_programme.c` ; pour exécuter : `./nom_executable`.

## Exercice 1 : Question de cours

**Énoncé.** Soit l'arbre suivant :

```
                 1
       /         |         \
      2          4          6
    / | \       / \        /  \
   7  8  9    10   12     13   14
     / \               /  |  |  \
   15   16            17 18  19  20
```

> **Note :** la figure du document est redessinée ci-dessus : 1 a pour fils 2, 4 et 6 ; 2 a pour fils 7, 8, 9 ; 8 a pour fils 15 et 16 ; 4 a pour fils 10 et 12 ; 6 a pour fils 13 et 14 ; 13 a pour fils 17, 18, 19 et 20.

1. Donner :
    - l'ordre de l'arbre ;
    - le degré du nœud 4 et du nœud 2 ;
    - le nombre de feuilles ;
    - la hauteur de l'arbre.
2. Quel est le parcours en profondeur préfixe de cet arbre ?
3. Quel est le parcours en largeur de cet arbre ?

## Exercice 2 : Arbre binaire

**Énoncé.** Remarque : la plupart des fonctions demandées dans cet exercice sont disponibles en pseudo-code dans le cours.

1. Construction de l'arbre :
    a) Déclarer une structure `Arbre` permettant de gérer un arbre binaire contenant des entiers.
    b) Redéfinir le type pointeur sur arbre en `pArbre`.
    c) Créer la fonction `creerArbre` permettant de créer un arbre. Cette fonction prend en paramètre l'élément à insérer dans le nœud de l'arbre, initialise ses fils et retourne son adresse.
    d) Écrire la fonction `int estVide(pArbre a)` qui retourne 1 si `a` est un arbre vide, 0 sinon.
    e) Écrire la fonction `int estFeuille(pArbre a)` qui retourne 1 si l'arbre est une feuille, 0 sinon.
    f) Écrire la fonction `int element(pArbre a)` qui retourne l'élément stocké dans le nœud de `a`.
    g) Écrire une fonction `existeFilsGauche(pArbre a)` qui retourne 1 si l'arbre a un fils gauche, 0 sinon. Faire une fonction similaire `existeFilsDroit(pArbre a)`.
    h) Écrire une fonction `ajouterFilsGauche(pArbre a, int e)` qui crée à l'arbre un fils gauche qui va contenir `e`. Faire de même avec `ajouterFilsDroit(pArbre a, int e)`.
    i) À l'aide des fonctions réalisées précédemment, construire l'arbre suivant :

```
            1
         /     \
        2       8
      /   \    / \
     3     6  9   10
    / \     \
   4   5     7
```

2. Parcours de l'arbre :
    a) Écrire une fonction `traiter` qui affichera le contenu du nœud de l'arbre passé en paramètre.
    b) Écrire une procédure `parcoursPrefixe` permettant d'afficher tous les éléments d'un arbre par un parcours en profondeur préfixe.
    c) Vérifier que l'arbre que vous avez construit est correct en affichant son parcours préfixe.
    d) Écrire une procédure `parcoursPostfixe` permettant d'afficher tous les éléments d'un arbre par un parcours en profondeur postfixe. Tester la fonction sur l'arbre.
    e) Déclarer une structure permettant de gérer une FILE contenant des `pArbre`.
    f) Écrire une procédure `parcoursLargeur` permettant d'afficher tous les éléments d'un arbre par un parcours en largeur.
3. Modification de l'arbre :
    a) Écrire une fonction `pArbre modifierRacine(pArbre a, int e)` qui modifie l'élément stocké dans `a` par l'élément `e` et retourne `a`.
    b) Écrire une fonction `pArbre supprimerFilsGauche(pArbre)` qui supprime le fils gauche d'un arbre. Idem avec `supprimerFilsDroit(pArbre)`. Attention aux fuites mémoire ! (voir cours)
    c) Supprimer les nœuds 9, 15 et 3 de l'arbre. Quel devrait être son parcours en largeur ? Vérifier.
4. Analyse de l'arbre.
5. Écrire une fonction `nmbFeuille` qui retourne le nombre de feuilles d'un arbre.
6. Écrire une fonction `tailleArbre` qui retourne la taille (nombre de nœuds internes) de l'arbre.
7. *Pas facile !* Écrire une fonction `hauteur` qui retourne la hauteur d'un arbre. Elle renverra -1 si l'arbre est vide.

> **Note :** le document écrit `exitseFilsGauche` et `parbre modifierRacine` ; on a corrigé en `existeFilsGauche` et `pArbre`. Dans la figure, 7 est le fils **droit** de 6.

## Exercice 3 : Arbre binaire filiforme

**Énoncé.** Un arbre binaire est dit *filiforme* si chaque nœud a au plus un seul fils (qu'il soit gauche ou droit).

- À quoi va ressembler un tel arbre ?
- Écrire une fonction permettant de déterminer si un arbre est filiforme (plusieurs méthodes sont possibles !).
- Un arbre est dit *peigne gauche* si les nœuds n'ont qu'un fils gauche et pas de fils droit.
    - Écrire une fonction permettant de déterminer si un arbre est peigne gauche.
    - Écrire une fonction `pArbre constrPeigneGauche(int h)` qui va créer un arbre peigne gauche de hauteur h en le remplissant avec des valeurs aléatoires entre 0 et 10. L'afficher.

## Exercice 4 : Notation polonaise inversée

**Énoncé.** (Devoir de 2021-2022.) La notation polonaise inversée (NPI), utilisée par certaines calculatrices, permet d'écrire de façon non ambiguë les formules arithmétiques sans utiliser de parenthèses. Le principe est que les opérandes précèdent toujours leurs opérateurs et peuvent être eux-mêmes des nombres ou des expressions non triviales.

Exemples : $1 + 2$ s'écrit `1 2 +` ; $((1 + 2) * 4) + 3$ s'écrit `1 2 + 4 * 3 +` ; $\dfrac{a}{a + b}$ s'écrit `a a b + /`.

Dans cet exercice, nous abordons comment construire une notation polonaise à l'aide d'un arbre binaire. Chaque nœud de cet arbre contiendra un opérateur ou un nombre. On considère les structures suivantes :

```
Structure Terme
    typeTerme : Caractere
    valeur : Reel

Structure Arbre
    terme : Structure Terme
    fg, fd : Pointeur sur Structure Arbre
```

Le champ `typeTerme` servira à définir les opérateurs ; il ne pourra prendre que les valeurs suivantes : `'+'`, `'-'`, `'x'`, `'/'` et `'='`. Si `typeTerme` vaut `'='`, c'est que le nœud permet de stocker un nombre. Si ce n'est pas le cas, le champ `valeur` vaudra 0. Chaque nœud interne contient un opérateur binaire, et ses fils gauche et droit sont respectivement l'expression à gauche et l'expression à droite de l'opérateur. Les feuilles sont donc forcément des constantes.

1. Quelle est l'écriture en NPI du calcul suivant ?
$$
5 * \dfrac{(a + 1) * (b + 1)}{a + b}
$$
2. Quelle est la valeur de l'expression polonaise inversée suivante : `1 8 2 - 7 4 - * 3 6 + / /` ?
3. L'expression $((3 - 4) * 2 + 3)$ s'écrit sous forme d'arbre comme suit (chaque nœud est noté `(typeTerme, valeur)`) :

```
              (+,0)
             /     \
         (*,0)     (=,3)
         /    \
     (-,0)    (=,2)
     /    \
  (=,3)  (=,4)
```

La notation polonaise inversée de ce calcul est `3 4 - 2 * 3 +`. À quel type de parcours d'arbre correspond la notation polonaise inversée ?

4. À partir des structures définies ci-dessus et des fonctions écrites lors des exercices précédents, construire l'arbre représenté ci-dessus.
5. Écrire la procédure `void afficherNotationPolonaiseInversee(pArbre a)` qui permet d'afficher en notation polonaise inversée l'expression mathématique définie dans l'arbre binaire.
6. Écrire la fonction `float eval(pArbre a)` qui permet de donner le résultat de l'expression mathématique définie dans l'arbre binaire. La tester avec l'arbre, puis pour vérifier votre réponse à la question 2.

> **Note :** l'énoncé parle d'« opérandes » pour désigner les opérateurs ; on a rétabli les termes. Dans la figure, la multiplication est notée `*` alors que la liste des valeurs autorisées donne `'x'` ; le code accepte les deux.
