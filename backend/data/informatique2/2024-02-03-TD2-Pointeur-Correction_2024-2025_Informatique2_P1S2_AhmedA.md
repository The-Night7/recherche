---
title: TD2 Pointeur Correction
author: [AhmedA]
date: 2024-02-03 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Ahmed A.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

Exercices : [1](#exercice-1) [2](#exercice-2) [3](#exercice-3) [4](#exercice-4) [5](#exercice-5) [6](#exercice-6) [7](#exercice-7) [8](#exercice-8) 

> Regarder la correction uniquement après avoir travaillé par vous-même, car si vous ne le faites pas, c’est le meilleur moyen de rater vos DS/CC.
{: .prompt-danger }

## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/1.jpg){: .w-75 .shadow .rounded-10 }

| ligne | a   | b   | c   | pa           | pb           | *pa | *pb |
| ----- | --- | --- | --- | ------------ | ------------ | --- | --- |
| 6     | ?   | ?   | ?   | adresse de a | ?            | ?   | ?   |
| 7     | ?   | ?   | ?   | adresse de a | adresse de b | ?   | ?   |
| 9     | 2   | ?   | ?   | adresse de a | adresse de b | 2   | ?   |
| 10    | 2   | 3   | ?   | adresse de a | adresse de b | 2   | 3   |
| 11    | 2   | 3   | 5   | adresse de a | adresse de b | 2   | 3   |
| 12    | 2   | 3   | 5   | adresse de a | adresse de b | 2   | 3   |
| 13    | 7   | 3   | 5   | adresse de a | adresse de b | 7   | 3   |
| 14    | 7   | -2  | 5   | adresse de a | adresse de b | 7   | -2  |
| 15    | 7   | -2  | 5   | adresse de a | adresse de c | 7   | 5   |
| 16    | 7   | -2  | 5   | adresse de a | adresse de c | 7   | 5   |
| 17    | 7   | -2  | 12  | adresse de a | adresse de c | 7   | 12  |
| 18    | 144 | -2  | 12  | adresse de a | adresse de c | 7   | 12  |


+ Le programme affiche :

```bash
2 3 
7 -2 ♣ 
144 -2 12
```
> Le programme affiche `♣` car il correspond a `5` dans la table [ASCII](https://cy.deltahmed.fr/posts/ASCII_Table/)
{: .prompt-info }

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/2.jpg){: .w-75 .shadow .rounded-10 }


## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/3.jpg){: .w-75 .shadow .rounded-10 }

> Question 1 : il n'est pas possible de faire cela avec des paramètres classique car il est impossible de manipuler directement la structure, la solution a ce problème est d'utiliser des pointeurs
{: .prompt-info }

On commence par importer les bibliothèques que l'on vas utiliser et crée la structure `Temps` demandée

```c
#include <stdio.h>

typedef struct {
    int heures;
    int minutes;
    int secondes;
} Temps;
```

+ On crée une fonction sécurisée pour le scanf

```c
int better_scan(char * message){
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

+ On crée la procédure qui modifie la structure en ajoutant du temps 

```c
void ajouteSeconde(Temps* t, int secondes) {
    t->secondes += secondes; // on ajoute les seconde
    while (t->secondes >= 60) // tant que seconde est supérieur a 60
    {
        t->secondes -= 60; // on ajoute une minute
        t->minutes++;
    }
    
    while (t->minutes >= 60) // tant que minute est supérieur a 60
    {
        t->minutes -= 60; // on ajoute des heures
        t->heures++;
    }
    
}
```

+ On peut tester le tout dans le `main`

```c
int main() {
    Temps t;

    t.heures = better_scan("Entrez heures : ");
    t.minutes = better_scan("Entrez minutes : ");
    t.secondes = better_scan("Entrez secondes :");

    int s;
    s = better_scan("Entrez le nombre de secondes à ajouter : ");

    ajouteSeconde(&t, s);

    printf("Nouvelle heure: %02d:%02d:%02d\n", t.heures, t.minutes, t.secondes);

    return 0;
}
```

## Exercice 4

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/4.jpg){: .w-75 .shadow .rounded-10 }

+ On peut directement écrire le tout dans le `main`

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));

    int* arr = malloc(20 * sizeof(int)); // equivalent a int arr[20] (vous pouvez juste remplacer)

    int i;
    for(i = 0; i < 20; i++) {
        *(arr + i) = rand() % 11;
    }

    int sum = 0;
    for(i = 0; i < 20; i++) {
        sum += *(arr + i);
    }

    printf("Somme des elements de l'array : %d\n", sum);

    free(arr); // (uniquement si vous utiliser malloc)

    return 0;
}
```

> `malloc(20 * sizeof(int))` premet d'allouer de la mémoire il retourne un pointeur vers cette mémoire ou NULL si `malloc` échoue, `free(arr)` permet de libérer la mémoire allouée, dans ce cas precis on peut juste utiliser `arr[20]`
{: .prompt-info }

## Exercice 5

![exercice 5](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/5.jpg){: .w-75 .shadow .rounded-10 }

+ On utilise les formules des polynôme de degrés 1 et 2 
+ \$$ax+b=0 \Longrightarrow \frac{-b}{a}; a \neq 0$$

```c
#include <stdio.h>

int resoudre1(float a, float b, float *res) {
    if (a == 0) {
        if (b == 0) {
            return -1; // Tout x est une solution
        } else {
            return 0; // Pas de solution
        }
    } else {
        *res = -b / a; // Calcul de la solution
        return 1; // Une solution
    }
}
```

+ \$$ax^{2}+bx+c=0 ; \Delta = b^{2} - 4ac > 0 \Longrightarrow x_{1} = \frac{-b-\sqrt{\Delta}}{2a} \text{ et } x_{1} = \frac{-b+\sqrt{\Delta}}{2a}$$

+ \$$\text{si }\Delta = 0 \Longrightarrow x = \frac{-b}{2a}$$

+ \$$\text{si }\Delta < 0 \Longrightarrow x \notin \mathbb{R}$$ 

```c
int resoudre2(float a, float b, float c, float *res1, float *res2) {
    float discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
        *res1 = (-b + sqrt(discriminant)) / (2 * a);
        *res2 = (-b - sqrt(discriminant)) / (2 * a);
        return 2; // Deux solutions distinctes
    } else if (discriminant == 0) {
        *res1 = -b / (2 * a);
        return 1; // Une solution
    } else {
        return 0; // Pas de solution réelle
    }
}
```

## Exercice 6

![exercice 6](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/6.jpg){: .w-75 .shadow .rounded-10 }

+ On utilise juste les formules donnée dans l'exercice 

```c
#include <math.h>

void cartesian2polar(float x, float y, float* radius, float* angle) {
    // Calcul du rayon
    *radius = sqrt(x * x + y * y);

    // Calcul de l'angle
    if (*radius == 0) {
        *angle = 0; // l'angle est indéfini si le rayon est nul
    } else {
        *angle = atan2(y, x);
    }
}
void polar2cartesian(float radius, float angle, float* x, float* y) {
    // Calcul des coordonnées cartésiennes
    *x = radius * cos(angle);
    *y = radius * sin(angle);
}

```

## Exercice 7

![exercice 7](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/7.jpg){: .w-75 .shadow .rounded-10 }

+ On crée la procédure puis on l'utilise dans le `main`

```c
#include <stdio.h>
int getExtremums(int* tab, int N, int** min_ptr, int** max_ptr) {
    if (tab == NULL || N == 0){
        return 1;
    }
    // Initialiser les extrémités avec la première valeur du tableau
    **min_ptr = &tab[0];
    **max_ptr = &tab[0];

    // Parcourir le tableau pour trouver les extrémités
    for (int i = 1; i < N; i++) {
        if (tab[i] < **min_ptr) {
            *min_ptr = &tab[i]; // Mettre à jour l'adresse du minimum
        }
        if (tab[i] > **max_ptr) {
            *max_ptr = &tab[i]; // Mettre à jour l'adresse du maximum
        }
    }
    return 0;
}

int main() {
    int tableau[] = {5, 3, 9, 2, 7};
    int taille = 5;

    int* adresse_min;
    int* adresse_max;

    // Appeler la fonction pour obtenir les extrémités
    getExtremums(tableau, taille, &adresse_min, &adresse_max);

    // Afficher les résultats

    printf("Valeur du minimum : %d\n", adresse_min);
    printf("Valeur du maximum : %d\n", adresse_max);


    return 0;
}
```

## Exercice 8

![exercice 8](https://data.cy.deltahmed.fr/DATA/TD2-Pointeur_Informatique2p1s2/8.jpg){: .w-75 .shadow .rounded-10 }


+ On commence par importer les librairies et définir une taille max pour les mot

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 100
```

+ On crée maintenant la fonction `estPalindromeIndices` qui prend une chaine de char et qui verifie si c'est un palindrome

```c
// Fonction pour vérifier si une chaîne de caractères est un palindrome en utilisant des indices
int estPalindromeIndices(char chaine[]) { // ou char * chaine
    int longueur = strlen(chaine);
    for (int i = 0; i < longueur / 2; i++) {
        if (chaine[i] != chaine[longueur - i - 1]) {
            return 0; // La chaîne n'est pas un palindrome
        }
    }
    return 1; // La chaîne est un palindrome
}
```

+ On crée maintenant la fonction `estPalindromePointeurs` qui fait la même chose mais avec des pointeurs

```c
// Fonction pour vérifier si une chaîne de caractères est un palindrome en utilisant des pointeurs
int estPalindromePointeurs(char chaine[]) {
    char *debut = chaine;
    char *fin = chaine + strlen(chaine) - 1;
    while (debut < fin) {
        if (*debut != *fin) {
            return 0; // La chaîne n'est pas un palindrome
        }
        debut++;
        fin--;
    }
    return 1; // La chaîne est un palindrome
}
```

+ On test le tout dans le programme principal

```c
int main() {
    char chaine[MAX_LENGTH];

    // Vous pouvez utiliser un scanf ici
    printf("Saisissez une chaîne de caractères : ");
    if (fgets(chaine, MAX_LENGTH, stdin) == NULL){
        exit(EXIT_FAILURE); //EXIT_FAILURE est egal a 1
    }
    chaine[strcspn(chaine, "\n")] = 0;
    // fin de la saisie

    // Vérifier si la chaîne est un palindrome en utilisant des indices
    if (estPalindromeIndices(chaine)) {
        printf("La chaîne \"%s\" est un palindrome (indices).\n", chaine);
    } else {
        printf("La chaîne \"%s\" n'est pas un palindrome (indices).\n", chaine);
    }

    // Vérifier si la chaîne est un palindrome en utilisant des pointeurs
    if (estPalindromePointeurs(chaine)) {
        printf("La chaîne \"%s\" est un palindrome (pointeurs).\n", chaine);
    } else {
        printf("La chaîne \"%s\" n'est pas un palindrome (pointeurs).\n", chaine);
    }

    return EXIT_SUCCESS; //EXIT_SUCCESS est egal a 0
}

```

> `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fontion renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`, `strcspn` prend en argument une chaîne de char et une liste (chaîne de char) de rejet, Elle Renvoie la longueur de la plus grande sous-chaîne (en partant du début de la chaîne initiale) ne contenant aucun des caractères spécifiés dans la liste des caractères en rejet, ici elle permet de trouver l'index avant le \n.
{: .prompt-info }


> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-tip }


Exercices : [1](#exercice-1) [2](#exercice-2) [3](#exercice-3) [4](#exercice-4) [5](#exercice-1) [6](#exercice-2) [7](#exercice-3) [8](#exercice-4) 