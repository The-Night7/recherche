---
source: "PREING2-S1/Informatique3-DS/cc-2025-2026/DS3_Informatique_III_retape.pdf"
archive: "cc 2025 2026.zip"
pages: 2
semestre: "P2S1"
transcription: texte natif restructuré et contrôlé sur le rendu PDF
transcription_date: 2026-11-01
verification: comparaison du texte extrait avec le rendu des pages du PDF fourni
---

# DS3 Informatique III retape

## Notes de transcription

> Le PDF ne contient que deux pages. La rubrique « Documentation fournie (pages 3 et 4) » résume des annexes photographiées absentes de cette archive. Le code complet de la fonction d’insertion AVL à déboguer n’est pas fourni.

## Page 1

DS n°3 — Informatique III CY TECH — Pré-ING2 — Semestre 1, 2025/2026

DS n°3 Informatique III — Calculatrice et documents non autorisés. Langage C obligatoire. Attention à la robustesse du programme. Barème indicatif.

### Exercice 1 — Arbres et sécurité sociale (8,5 pts) — ABR

On souhaite stocker dans un système les données personnelles d’un grand groupe de personnes. Chaque usager est identifié par son numéro de sécurité sociale unique. Afin d’optimiser les recherches, on utilise un arbre de recherche binaire (ABR) ordonné par numéro de sécurité sociale.

1. Justifier le choix d’un ABR par rapport à d’autres structures pour stocker ces informations.

2. Quel parcours permet d’afficher tous les numéros dans l’ordre décroissant ? Justifier.

3. Définir la structure Personne contenant nom, prénom, âge (entier positif sur au plus 3 chiffres en base

10) et numéro de sécurité sociale (nombre positif sur 15 chiffres en base 10).

4. Définir la structure Arbre contenant une Personne allouée dynamiquement et deux pointeurs vers des Arbre. Définir aussi le type Parbre pointant vers un nœud.

5. Écrire Parbre creation_noeud(Personne* p1) qui crée un nœud en copiant les données de la personne. La personne pointée par p1 sera libérée après l’appel ; il faut donc effectuer une copie.

6. Écrire Parbre insertion(Parbre arbreSecu, Personne* p1) qui ajoute une personne à l’ABR, correctement placée. Si elle existe déjà, afficher un message d’erreur sans arrêter le programme.

7. Écrire une fonction recherche(...) recherchant une personne par son numéro de sécurité sociale et renvoyant ses informations ou une valeur particulière si elle est absente.

8. Écrire void afficheSecu(Parbre arbreSecu) qui affiche les numéros en parcourant d’abord les enfants puis le parent.

9. On suppose Arbre* suppmax(Arbre *a, int *e) déjà implémentée. Écrire filtrerRetraites(...) qui parcourt l’ABR initial, retire les personnes d’âge strictement supérieur à 62 ans, les insère dans un nouvel ABR et renvoie sa racine, en mettant également à jour la racine initiale.

### Exercice 2 — Debug d’une fonction d’insertion d’AVL (6,5 pts + 1,5 bonus)

Thème : AVL et liste chaînée. Structure donnée :

```c

typedef struct arbre {

char *mot;

int eq; // valeur de l’équilibre

struct arbre *fg;

struct arbre *fd;

} Arbre;

```

Arbre *insertAVL(Arbre *a, char *nouveau_mot);

Cet AVL est censé être ordonné alphabétiquement. L’insertion est implémentée mais fonctionne imparfaitement. Il faut détecter les erreurs d’équilibrage et concevoir un outil de diagnostic.

1. Pourquoi utiliser une liste chaînée pour stocker les nœuds problématiques ?

2. Définir la structure Chainon contenant un pointeur sur un Arbre.

3. Écrire insertionChainon(...) insérant un nouveau chaînon à l’emplacement choisi (début ou fin).

4. Écrire afficherListe(...) affichant tous les mots des nœuds listés.

## Page 2

5. Écrire estAVL(...) retournant 1 si l’arbre est un AVL (facteur d’équilibre dans {-1,0,1}), sinon 0. Ajouter toujours les nœuds problématiques à la liste passée en paramètre.

6. Écrire main() : demander 20 mots, les insérer avec insertAVL, appeler estAVL et afficher les nœuds problématiques ou « L’arbre est bien un AVL ».

7. Bonus : écrire supprimerNoeudsDefectueux(...) supprimant les nœuds listés tout en conservant un AVL valide.

### Exercice 3 — Analyse de connexions Shell (5 pts)

Fichier logins.csv au format <utilisateur>;<dateHeure>;<ip>. Exemples :

```text
alice;2023-10-01T12:10:00;192.168.1.12
bob;2023-10-01T13:15:00;192.168.1.14
charlie;2023-10-02T09:22:00;192.168.1.24
alice;2024-02-14T13:07:00;192.168.1.17
```

Écrire analyse.sh : premier argument obligatoire, fichier à analyser (erreur si absent ou invalide) ; afficher les noms d’utilisateurs sans doublon ; si deuxième argument, filtrer sur cet utilisateur et n’afficher que ses dates de connexion ; si troisième argument entier n, afficher uniquement les n dernières connexions triées par date croissante, par utilisateur ; si quatrième argument fichier, concaténer son contenu au premier avant traitement ; plus de quatre arguments : erreur ; toute erreur doit arrêter le script avec un message.

### Documentation fournie (pages 3 et 4)

Extraits de manuels Unix : cut (sélection de champs : -d, -f), head (-n), tail (-n), grep (-i, -v, -n), sort (-n, -r, -u), uniq (-c, -d, -u). Les photographies originales contiennent les descriptions détaillées de ces options.
