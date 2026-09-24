---
title: DS2 2023 2024 V1 Correction
author: [AhmedA]
date: 2024-04-23 01:00:00 +0100
categories: [PREING1 S2,Informatique2-DS]
tags: [PREING1 S2,Informatique2-DS,DS2,Ahmed A.]
division_title : DS2
math: true
mermaid: true
---



Exercices : [1](#1) [2](#2) [3](#3)

<div id="1"></div>

## Exercice 1

+ On inclue les bibliothèque et on définie `better_scan`

```c
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

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

+ On crée la fonction `creerTableau` l'enoncé n'est pas clair sur si il faut un argument ou non, il en faut un pour communiquer `nbtab` vias un pointeur.

```c
int* creerTableau(int* nb_tab_ptr){

    int nbtab = better_scanf("Saisir la taille du tableau :\n");
    int* tab = (int*)malloc(sizeof(int)*nbtab);
    if (tab == NULL)
    {
        exit(EXIT_FAILURE) 
    }
    
    for (int i = 0; i < nbtab; i++)
    {
        tab[i] = 1+rand()%1000;
    }
    *nb_tab_ptr = nbtab;
    return tab;
}
```

> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-tip }

+ On crée la fonction `afficherRec`, notez que `tab+1` permet de se décaler en mémoire 

```c
void afficherRec(int* tab, int taille){
    if (taille == 0){
        return; 
    }
    
    printf(tab[0]);
    afficherec(tab+1, taille-1)
}
```

+ On crée la fonction `afficherRec` il faudra utiliser la fonction au depart avec `nbvaleur = 0`

```c
int compterTab(int* tab, int taille, int min, int max, int nbvaleur){ 
    if (taille == 0){
        return nbvaleur;
    }

    if (tab[0]<max && tab[0]>min){
        nbvaleur +=1;
    }
    return comptertab(tab+1, taille-1, min, max, nbvaleur); //on ne retourne que 

}
```

+ On crée la fonction `remplirTab`, attention a bien dissocier les cas ou on ce décale ou non pour `tab2`.

```c
void remplirTab(int* tab, int taille, int* tab2, int taille2, int min, int max){
    if (taille == 0 || taille2 == 0)
    {
        return;
    }
    if (tab[0]<max && tab[0]>min)
    {
        tab2[0] = tab[0]; 
        remplirtab(tab+1, taille-1, tab2+1, taille2-1, min,  max);

    } else{
        remplirtab(tab+1, taille-1, tab2, taille2, min,  max);
    }

    
}
```

+ On crée la fonction suivante en utilisant les fonctions déjà crée


```c
void fonction_segments(int* tab, int taille, int a, int b, int c, int d, int** returntab1, int** returntab2, int* returntaille1, int* returntaille2)
{
    
    *returntaille1 = compterTab(tab, taille, a, b, 0);
    *returntaille2 = compterTab(tab, taille, c, d, 0);
    *returntab1 = (int*)malloc(sizeof(int) * *returntaille1); 
    *returntab2 = (int*)malloc(sizeof(int) * *returntaille2);
    
    if (*returntab1 == NULL || *returntab2 == NULL )
    {
        exit(EXIT_FAILURE);
    }

    remplirTab(tab, taille, *tab1, *size1, a, b);
    remplirTab(tab, taille, *tab2, *size2, c, d);
}
```

> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-info }


<div id="2"></div>

## Exercice 2

+ On crée notre structure Chaussure qui modelise un modèle de chaussure dans un magasin, on crée aussi notre répétitif `better_scan`

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_SIZE 50

typedef struct Chaussure_struct{
    char marque[MAX_SIZE];
    int prix;
    int Series;
    int stock;

}Chaussure;


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

+ On crée le constructeur de `Chaussure` en utilisant `fgets` pour gérer les depassement de mémoire (`scanf` fonctionne aussi)

```c
Chaussure* creerChaussure(){
    Chaussure* sabat = (Chaussure*)malloc(sizeof(Chaussure));

    if (sabat == NULL)
    {
        exit(EXIT_FAILURE);
    }
    printf("Choisir la marque des chaussures :\n");
    if (fgets(sabat->marque, MAX_SIZE, stdin) == NULL){
        exit(EXIT_FAILURE);
    }
    sabat->marque[strlen(sabat->marque) - 1] = '\0'; //pas utile si on utilise le scanf 

    sabat->prix = better_scan("Saisir le prix :\n");
    sabat->serie = better_scan("Saisir le numero de série :\n");
    sabat->stock = better_scan("Saisir le stock de ce modele :\n");

    return sabat;

}
```

> `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fonction renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`, `strcspn` prend en argument une chaîne de char et une liste (chaîne de char) de rejet, Elle Renvoie la longueur de la plus grande sous-chaîne (en partant du début de la chaîne initiale) ne contenant aucun des caractères spécifiés dans la liste des caractères en rejet, ici elle permet de trouver l'index avant le `\n`.
{: .prompt-tip }

> `EXIT_SUCCESS` et `EXIT_FAILURE` sont définie dans `stdlib` et permettent une meilleur lecture du code, `exit()` permet de sortir du programme avec un code d'erreur.
{: .prompt-info }

+ On crée la fonction classique `creerStock`, ne pas oublier que tab est un tableau de pointeur et donc que l'on doit utiliser deux `*`

```c
Chaussure** creerStock(int* return_nb_modele){
    int nb_modele = better_scan("Saisir le nombre de modele");
    Chaussure** tab = (Chaussure**)malloc(sizeof(Chaussure*) * nb_modele);
    if (tab == NULL)
    {
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < nb_modele; i++)
    {
        tab[i] = creerChaussure();
    }
    *return_nb_modele = nb_modele;
    return tab;
}
```

+ On crée la fonction `achat`

```c
void achat(Chaussure** tab, int taille, int numserie){ 
    for (int i = 0; i < taille; i++) //1 + n+1 + 2n+1
    {
        if (numserie == tab[i]->serie) // + n
        {   
            if (tab[i]->stock > 0){ // + n
                tab[i]->stock--; // + 1 +1 (on par du principe qu'il n'y a pas de doublons)
            } else{
                printf("Stock null \n"); // printf(constante) est constant O(1)
            }
        }
        
    }
    // 1+n+1+2n+1+n+n+1+1+O(1) = O(n)
}
```

+ La complexité et en $O(n)$ et c'est démontrable facilement, la complexité dans le pire des cas, il y'aura moins d'iteration lorsqu'on `return` dès que l'on croise le modèle dans le stock, car on ne vas pas forcement parcourir toute la liste et on part du principe qu'il n'y a pas de doublons, dans le meilleur des cas et dans le cas moyen la complexité baisse. c'est le seul truc que j'ai trouvé, si vous avez d'autre propositions faites les.

```c
void achat(Chaussure** tab, int taille, int numserie){
    for (int i = 0; i < taille; i++)
    {
        if (numserie == tab[i]->serie)
        {
            if (tab[i]->stock > 0){
                tab[i]->stock--; 
            } else{
                printf("Stock null \n");
            }
            return;
        }
        
    }
    
}
```

<div id="3"></div>

## Exercice 3

+ On crée quelques fonction utile au fonctionnement de la fonction `levenshtein`

```c
int max(int a, int b){
    if (a > b)
    {
        return a;
    }
    return b;
}
int min(int a, int b){
    if (a < b)
    {
        return a;
    }
    return b;
}
int min3(int a, int b, int c){
    return min(a,min(b,c));
}
```

+ On recopie exactement le pseudo code donné 

```c
int levenshtein(char* strA, char* strB){
    int longeurA = strlen(strA);
    int longeurB = strlen(strB);

    if (min(longeurA, longeurB) == 0)
    {
        return max(longeurA, longeurB);
    }
    if (strA[0]==strB[0])
    {
        return levenshtein(strA+1,strB+1);
    }

    return 1 + min3(levenshtein(strA+1,strB),levenshtein(strA,strB+1),levenshtein(strA+1,strB+1));
}
```



Exercices : [1](#1) [2](#2) [3](#3)