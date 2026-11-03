---
title: TD3 Tableaux dynamique Correction
author: [AhmedA]
date: 2024-02-03 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Ahmed A.,2023/2024]
math: true
mermaid: true
division_title : 2023/2024
---


Exercices : [1](#exercice-1) [2](#exercice-2) [3](#exercice-3) [4](#exercice-4) [5](#exercice-1)


## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/1.jpg){: .w-75 .shadow .rounded-10 }

| line | a   | b   | c   | pa           | pb           | ppa           | *pa | *pb | *ppa              | **paa |
| ---- | --- | --- | --- | ------------ | ------------ | ------------- | --- | --- | ----------------- | ----- |
| 9    | ?   | ?   | ?   | adresse de a | ?            | ?             | ?   | ?   | ?                 | ?     |
| 10   | ?   | ?   | ?   | adresse de a | adresse de b | ?             | ?   | ?   | ?                 | ?     |
| 11   | ?   | ?   | ?   | adresse de a | adresse de b | adresse de pa | ?   | ?   | pa = adresse de a | ?     |
| 12   | 10  | ?   | ?   | adresse de a | adresse de b | adresse de pa | 10  | ?   | pa = adresse de a | 10    |
| 13   | 10  | -2  | ?   | adresse de a | adresse de b | adresse de pa | 10  | -2  | pa = adresse de a | 10    |
| 14   | 10  | -2  | -4  | adresse de a | adresse de b | adresse de pa | 10  | -2  | pa = adresse de a | 10    |
| 15   | 3   | -2  | -4  | adresse de a | adresse de b | adresse de pa | 3   | -2  | pa = adresse de a | 3     |
| 16   | 3   | -2  | -4  | adresse de c | adresse de b | adresse de pa | -4  | -2  | pa = adresse de c | -4    |
| 17   | 3   | -2  | 1   | adresse de c | adresse de b | adresse de pa | 1   | -2  | pa = adresse de c | 1     |


## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/2.jpg){: .w-75 .shadow .rounded-10 }

+ On importe tout d'abord toute les librairies utiles, on créer une fonction qui génère un nombre aléatoire et une procédure qui permet d'afficher les Tableaux

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// générer un entier aléatoire entre x et y inclu
int randomInt(int x, int y) {
    return rand() % (y - x + 1) + x;
}

// afficher un tableau d'entiers
void afficherTab(int* tableau, int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d", tableau[i]);
        if (i < n - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}
```

+ On crée deux fonction sécurisée pour le scanf, une pour les nombre et une pour les nombre positifs

```c
int better_scan(char * message){
    int ret_var = 0;
    int value = 1;
    while (ret_var != 1)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}
int better_scan_pos(char * message){
    int ret_var = 0;
    int value = 1;
    while (ret_var != 1 || value < 0)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}
```

> Ces fonctions sont facultatives, les lignes `while(getchar()!='\n'){}` permetent de vider le buffer et d'avoir des `scanf` qui ne bouclent pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }

+ On crée maintenant la fonction qui crée un tableau d'entiers aléatoires entre x et y

```c
int* randTab(int n, int x, int y) {
    int* tableau = (int*)malloc(n * sizeof(int)); //allocation de la mémoire 
    if (tableau == NULL) {
        printf("Erreur d'allocation de mémoire.\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < n; i++) {
        tableau[i] = randomInt(x, y);
    }
    return tableau;
}

```

> `EXIT_FAILURE` est définie dans `stdlib` et permettent une meilleur lecture du code, , `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-info }

+ On créer mainteant la fonction qui pemet de filtrer les valeurs pair du tableau

```c
int* tabPair(int* tableau, int n, int *nbpaire_ptr) {
    int nbPairs = 0;
    // Compte le nombre de valeurs paires dans le tableau
    for (int i = 0; i < n; i++) {
        if (tableau[i] % 2 == 0) {
            nbPairs++;
        }
    }
    *nbpaire_ptr = nbPairs; // Stocke le nombre de valeurs paires
    int* tableauPairs = (int*)malloc(nbPairs * sizeof(int));
    if (tableauPairs == NULL) {
        printf("Erreur d'allocation de mémoire.\n");
        exit(EXIT_FAILURE);
    }

    int index = 0;
    // Remplit le tableau avec les valeurs paires
    for (int i = 0; i < n; i++) {
        if (tableau[i] % 2 == 0) {
            tableauPairs[index] = tableau[i];
            index++;
        }
    }
    return tableauPairs;
}
```

+ On écrit maintenant la fonction qui permet de supprimer les valeurs identiques côtes a côtes l'une de l'autre 

```c
int* noDouble(int* tableau, int n, int *nbdoublon) {
    int* tableauSansDoublons = (int*)malloc(n * sizeof(int));
    if (tableauSansDoublons == NULL) {
        printf("Erreur d'allocation de mémoire.\n");
        exit(EXIT_FAILURE);
    }
    int index = 0;
    tableauSansDoublons[index] = tableau[0]; // Première valeur toujours conservée
    index++;
    // Parcourt le tableau pour supprimer les doublons contigus
    for (int i = 1; i < n; i++) {
        if (tableau[i] != tableau[i - 1]) { // Si la valeur actuelle est différente de la précédente
            tableauSansDoublons[index] = tableau[i]; // On la conserve dans le nouveau tableau
            index++;
        }
    }
    *nbdoublon = index - 1; // Stocke le nombre de valeurs uniques
    return realloc(tableauSansDoublons, index * sizeof(int)); // Redimensionne le tableau
}
```

> `EXIT_FAILURE` est définie dans `stdlib` et permettent une meilleur lecture du code
{: .prompt-info }

+ On peut mainteant tester le tout dans le `main`

```c
int main() {
    srand(time(NULL));
    int n, x, y;

    n = better_scan_pos("Entrez la taille du tableau : ");
    x = better_scan("Entrez la borne inférieure (x) : ");
    y = better_scan("Entrez la borne supérieure (y) : ");

    
    // Génère un tableau aléatoire et l'affiche
    int* tableau = randTab(n, x, y);
    printf("Tableau original : ");
    afficherTab(tableau, n);

    int nombre_de_paire;
    int* tableauPairs = tabPair(tableau, n, &nombre_de_paire);
    printf("Tableau des valeurs paires : ");
    afficherTab(tableauPairs, nombre_de_paire);

    int nombre_de_doublon;
    int* tableauSansDoublons = noDouble(tableau, n, &nombre_de_doublon);
    printf("Tableau sans doublons contigus : ");
    afficherTab(tableauSansDoublons, nombre_de_doublon);

    // On oublie pas de libérer la mémoire meme si dans ce cas ce n'est pas important
    free(tableau);
    free(tableauPairs);
    free(tableauSansDoublons);

    return 0;
}
```

## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/3.jpg){: .w-75 .shadow .rounded-10 }
![exercice 3_2](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/3_2.jpg){: .w-75 .shadow .rounded-10 }

+ On importe tout d'abord toute les librairies utiles et on crée une procédure qui permet d'afficher les prénoms

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void AfficherPrenom(char **tabPrenom, int nbPrenoms){
    printf("\nPrénoms stockés :\n");
    for (int i = 0; i < nbPrenoms; i++) {
        printf("%s\n", tabPrenom[i]);
    }
}
```

+ On réutilise notre fonction de `scanf` sécurisé 

```c
int better_scan_pos(char * message){
    int ret_var = 0;
    int value = 1;
    while (ret_var != 1 || value < 0)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}
```

> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }

+ On crée la procédure qui permet de mettre la première lettre de chaque prénom en majuscules

```c
void Maj(char* prenom) {
    if (prenom[0]>=65 && prenom[0]<=90) {
        prenom[0] += 32; // Met la première lettre en majuscule
    }
}
```

+ Il existe une autre méthode pour y parvenir on peut utiliser les fonction de la bibliothèque `ctype.h`

```c
void Maj(char* prenom) {
    if (!isupper(prenom[0])) {
        prenom[0] = toupper(prenom[0]); // Met la première lettre en majuscule
    }
}
```



+ On peut tout faire directement dans le main 

```c
int main() {
    char** tabPrenom = NULL;
    int nbPrenoms;

    // Demander à l'utilisateur combien de prénoms il souhaite stocker
    nbPrenoms = better_scan_pos("Combien de prénoms souhaitez-vous stocker ? \n");
    // Allouer de l'espace pour le tableau de pointeurs vers les prénoms
    tabPrenom = (char**)malloc(nbPrenoms * sizeof(char*));
    if (tabPrenom == NULL) {
        printf("Erreur d'allocation de mémoire.\n");
        exit(EXIT_FAILURE);
    }

    // Saisir et stocker chaque prénom dans le tableau
    for (int i = 0; i < nbPrenoms; i++) {
        int taillePrenom;
        printf("Entrez la taille du prénom %d ", i + 1);
        taillePrenom = better_scan_pos(": \n");

        // Allouer de l'espace pour le prénom et ajouter 1 pour le caractère de fin de chaîne '\0'
        tabPrenom[i] = (char*)malloc((taillePrenom + 1) * sizeof(char));
        if (tabPrenom[i] == NULL) {
            printf("Erreur d'allocation de mémoire.\n");
            exit(EXIT_FAILURE);
        }

        // Saisir le prénom
        printf("Entrez le prénom %d : ", i + 1);
        if (fgets(tabPrenom[i], taillePrenom + 1, stdin)==NULL){
            exit(EXIT_FAILURE);
        }
        tabPrenom[i][strcspn(tabPrenom[i], "\n")] = 0;
    }

    AfficherPrenom(tabPrenom, nbPrenoms);

    // Libérer la mémoire
    for (int i = 0; i < nbPrenoms; i++) {
        free(tabPrenom[i]);
    }
    free(tabPrenom);

    return 0;
}

```


> `EXIT_FAILURE` est définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur. `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fontion renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`, `strcspn` prend en argument une chaîne de char et une liste (chaîne de char) de rejet, Elle Renvoie la longueur de la plus grande sous-chaîne (en partant du début de la chaîne initiale) ne contenant aucun des caractères spécifiés dans la liste des caractères en rejet, ici elle permet de trouver l'index avant le \n.
{: .prompt-info }




## Exercice 4

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/4.jpg){: .w-75 .shadow .rounded-10 }

+ On importe tout d'abord toute les librairies utiles et on crée directement le programme dans le `main`

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    // Vérifie si le nombre d'arguments est correct
    if (argc != 4) {
        printf("Usage: %s <nombre1> <opérateur> <nombre2>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // Convertit les arguments en nombres réels
    double nombre1 = atof(argv[1]);
    double nombre2 = atof(argv[3]);

    // Effectue l'opération en fonction de l'opérateur
    double resultat;
    char operateur = argv[2][0]; // Prend le premier caractère de l'opérateur
    switch (operateur) {
        case '+':
            resultat = nombre1 + nombre2;
            break;
        case '-':
            resultat = nombre1 - nombre2;
            break;
        case '*':
            resultat = nombre1 * nombre2;
            break;
        case '/':
            // Vérifie si la division par zéro
            if (nombre2 == 0) {
                printf("Erreur: Division par zéro\n");
                exit(EXIT_FAILURE);
            }
            resultat = nombre1 / nombre2;
            break;
        default:
            printf("Erreur: Opérateur non valide\n");
            exit(EXIT_FAILURE);
    }

    // Affiche le résultat
    printf("Résultat de l'opération : %f\n", resultat);

    return EXIT_SUCCESS;
}

```

> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-info }



## Exercice 5

![exercice 5](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/5.jpg){: .w-75 .shadow .rounded-10 }
![exercice 5_2](https://data.cy.deltahmed.fr/DATA/TD3-Tableaux-dynamique_Informatique2p1s2/5_2.jpg){: .w-75 .shadow .rounded-10 }

+ On commence par importer les bibliothèque et on crée nos deux fonctions de saisie

```c
#include <stdio.h>
#include <stdlib.h>

int better_scan_pos(char * message){
    int ret_var = 0;
    int value = 1;
    while (ret_var != 1 || value < 0)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return value;
    
}

int choixNMax(){
    int n = better_scan_pos("Choisir n_max : \n");
    return n;
}
```

> La ligne `while(getchar()!='\n'){}` est facultative elle permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-warning }

> Question 2 : Le triangle de pascal doit faire $$n+1$$ lignes 
{: .prompt-info }

+ On crée la fonction crée triangle en utilisant les formules donnée dans l'énoncée 

```c
int** creerTriangle(int n_max){

    int** result = (int**)malloc((n_max+1)*sizeof(int*)); // on alloue la mémoire
    if (result == NULL){
        exit(EXIT_FAILURE); 
    }

    for (int i = 0; i < n_max+1; i++)
    {
        result[i] = (int*)malloc((i+1)*sizeof(int)); // on alloue la ligne
        if (result[i] == NULL){
            exit(EXIT_FAILURE);
        }
        
        for (int j = 0; j < i+1; j++) //pour chaque Nouvelle ligne on calcule les coef
        {                             // en fonction des regles donnée 
            if (j == 0 || j == i){
                result[i][j] = 1;
            } else {
                result[i][j] = result[i-1][j-1] + result[i-1][j];
            }

        }      
    }
    return result;
}
```

> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-info }

> On peut aussi aborder une approche récursive de la fonction en ayant pour conditions d'arret les conditions donnée dans l'exercice.
{: .prompt-tip }

+ On crée la procédure d'affichage demandée en Parcourant le tableau

```c
void affichePascal(int **tab, int n_max){
    for (int i = 0; i < n_max+1; i++)
    {
        for (int j = 0; j < i+1; j++)
        {
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }
    
}
```

+ On peut tester tout cela dans le `main`

```c
int main(){
    int n_max = choixNMax();

    int** triangle = creerTriangle(n_max);

    affichePascal(triangle, n_max);

    int n = n_max + 2;
    int k = n_max + 2;
    while (n > n_max+1) //on verifie les conditions demandée
    {
        n = better_scan_pos("choisir n :\n"); // si on utilise un scanf il faudra augmenter le nombre de conditions 
    }
    while (k > n_max+1)
    {
        k = better_scan_pos("choisir k :\n");
    }

    printf("Résultat : de %d parmis %d : %d \n", k,n,triangle[n][k]);
}
```

