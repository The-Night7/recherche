---
title: DS1 2024 2025 V1 Correction
author: [AhmedA] 
date: 2024-11-05 01:00:00 +0100
categories: [PREING2 S1,Informatique3-DS]
tags: [PREING2 S1,Informatique3-DS,Ahmed A.,DS1]
math: true
mermaid: true
division_title : DS1
---


Exercices : [1](#1) [2](#2)

<div id="1"></div>

## Exercice 1

[Télécharger l'exercice exo1.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2022-2023-Correction_Informatique3-DSp2s1/exo3.c){:target="_blank"} 

![page 1](https://data2.cy.deltahmed.fr/DATA/info/DS1-2024-2025-V1_Informatique3-DSp2s1-2024-2025/1.jpg){: .w-75 .shadow .rounded-10 }

![page 1](https://data2.cy.deltahmed.fr/DATA/info/DS1-2024-2025-V1_Informatique3-DSp2s1-2024-2025/1_2.jpg){: .w-75 .shadow .rounded-10 }

+ On utilise une pile dynamique car le nombre de disque n'est pas limité, une pile statique peut être utilisé losque que la tour est limité en taille ce qui est plus réaliste

+  On définie la structure Disque pour représenter un disque
 

```c 
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

typedef struct chainon_struct
{
    int value; // Valeur (diamètre) du disque
    struct chainon_struct* next; // Pointeur vers le disque suivant
} Disque;

``` 


+  On définie la structure Tour pour représenter une tour de disques
 

```c 
typedef struct tour_struct
{
    Disque* tete; // Pointeur vers le disque du dessus de la tour
    int len; // Longueur (nombre de disques) de la tour
} Tour;

``` 


+  On crée la fonction qui enlève le disque du dessus de la tour et retourne sa valeur
 

```c 
int enleverDisque(Tour* ptour){
    if (ptour == NULL) // Vérifie si la tour est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    if (ptour->tete == NULL || ptour->len < 1 ) // Vérifie si la tour est vide
    {
        return 0; // Retourne 0 si la tour est vide
    }
    
    int val = ptour->tete->value; // Sauvegarde la valeur du disque
    Disque* tmp = ptour->tete->next; // Sauvegarde le pointeur vers le disque suivant
    free(ptour->tete); // Libère la mémoire allouée pour le disque du dessus
    ptour->tete = tmp; // Met à jour le pointeur vers le disque du dessus
    ptour->len--; // Réduit la longueur de la tour
    return val; // Retourne la valeur du disque enlevé
}

``` 


+  On crée la fonction qui crée un nouveau disque avec le diamètre spécifié
 

```c 
Disque* creerDisque(int diam){
    Disque* d = (Disque*)malloc(sizeof(Disque)); // Allocation mémoire pour un nouveau disque
    if (d == NULL) // Vérification si l'allocation a échoué
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'échec
    }
    d->next = NULL; // Le disque n'a pas de disque suivant
    d->value = diam; // Assigne la valeur (diamètre) du disque
    return d; // Retourne un pointeur vers le disque créé
}

``` 


+  On crée la fonction qui ajoute un disque à une tour en respectant l'ordre décroissant des diamètres
 

```c 
int ajouterDisque(Tour* ptour, int diam){
    if (ptour == NULL) // Vérifie si la tour est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    if (ptour->tete == NULL) // Si la tour est vide
    {
        ptour->tete = creerDisque(diam); // Crée le premier disque et le place en tête
        ptour->len++; // Augmente la longueur de la tour
        return 1;
    }
    if (ptour->tete->value > diam) // Si le disque à ajouter est plus petit que celui du dessus
    {
        Disque* d = creerDisque(diam); // Crée un nouveau disque
        d->next = ptour->tete; // Relie le nouveau disque au disque du dessus
        ptour->tete = d; // Le nouveau disque devient le disque du dessus
        ptour->len++; // Augmente la longueur de la tour
        return 1;
    }
    return 0; // Retourne 0 si l'ajout du disque échoue (disque trop grand)
}

``` 


+  On crée la fonction qui affiche tous les disques d'une tour
 

```c 
void afficheTour(Tour* ptour){
    if (ptour == NULL) // Vérifie si la tour est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    Disque* actual = ptour->tete; // Pointeur pour parcourir les disques de la tour
    while (actual != NULL) // Parcourt tous les disques de la tour
    {     
        printf("%d \n", actual->value); // Affiche la valeur (diamètre) du disque
        actual = actual->next; // Avance au disque suivant
    }
}

``` 


+  On crée la fonction qui effectue une lecture sécurisée d'un entier dans une plage de nombre spécifiée
 

```c 
int better_scan(char* message, int min, int max){
    if (message == NULL)   // Vérifie si le message est NULL
    {
        exit(EXIT_FAILURE); // Arrêt du programme en cas d'erreur
    }
    
    int retvar = 0;
    int value = min-1;
    // C'est mieux d'utiliser un do while, c'est une mauvaise habitude de ma part
    while (min > value || value > max || retvar != 1 )
    {   
        printf("%s", message); // Affiche le message pour demander la valeur
        retvar = scanf("%d", &value); // Lit l'entier entré par l'utilisateur
        while (getchar()!='\n'); // Nettoie le buffer pour éviter des entrées incorrectes
    }
    return value; // Retourne la valeur valide entrée par l'utilisateur
}

``` 


>  `while (getchar()!='\n');` est equivalent a `while (getchar()!='\n'){}`
{: .prompt-tip }


+  On crée la fonction principale pour résoudre le problème des tours de Hanoi avec 3 tours
 

```c 
int main(){
    srand(time(NULL)); // Initialise le générateur de nombres aléatoires
    
    Tour tours[3]; // Déclaration de 3 tours
    for (int i = 0; i < 3; i++)
    {
        tours[i].tete = NULL; // Initialisation de la tête des tours à NULL
        tours[i].len = 0; // Initialisation de la longueur des tours à 0
    }
    
    int nb = better_scan("Entrer Nombre de disques \n", 3, 10); // Demande à l'utilisateur le nombre de disques
    int tour_dep, tour_fin;
    int disque;
    // On ajoute les disques sur la première tour en ordre décroissant
    for (int i = nb; i > 0; i--)
    {  
        ajouterDisque(tours,  i); // Ajoute un disque sur la première tour
    }
    
    // On commence à déplacer les disques jusqu'à ce que la dernière tour ait tous les disques
    while (tours[2].len < nb)
    {   
        // Demande à l'utilisateur de sélectionner une tour de départ
        tour_dep = better_scan("Entrer le numero de tour 1-3 ou on enlève un disque\n", 1, 3);
        tour_dep--;
        disque = enleverDisque(tours + tour_dep); // Enlève un disque de la tour sélectionnée
        if (disque) // Si un disque a été enlevé
        {
            // Demande à l'utilisateur de sélectionner une tour de destination
            tour_fin = better_scan("Entrer le numero de tour 1-3 ou on ajoute un disque\n", 1, 3);
            tour_fin--;
            if (!ajouterDisque(tours + tour_fin, disque)) // Si l'ajout du disque échoue (disque trop grand)
            {
                printf("Le disque est plus grand que le disque en dessous \n");
                ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
            }
        } else
        {
            printf("La tour est vide \n");
            ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
        }
        
        // Affiche l'état actuel des 3 tours
        for (int i = 0; i < 3; i++)
        {   
            printf("Tour %d :\n", i+1);
            afficheTour(tours+i);
        }
    }

    return 0;
}

``` 


+  On crée la fonction principale avec un nombre variable de tours
 

```c 
int main(){
    srand(time(NULL)); // Initialise le générateur de nombres aléatoires

    int nb_tours = better_scan("Entrer Nombre de Tours \n", 3, 20); // Demande à l'utilisateur le nombre de tours
    Tour* tours = malloc(sizeof(int) * 20); // Allocation mémoire pour un tableau de tours (max 20)
    for (int i = 0; i < nb_tours; i++)
    {
        tours[i].tete = NULL; // Initialisation de la tête des tours à NULL
        tours[i].len = 0; // Initialisation de la longueur des tours à 0
    }
    
    int nb = better_scan("Entrer Nombre de disques \n", 3, 500); // Demande à l'utilisateur le nombre de disques
    int tour_dep, tour_fin;
    int disque;
    // On ajoute les disques sur la première tour en ordre décroissant
    for (int i = nb; i > 0; i--)
    {  
        ajouterDisque(tours,  i); // Ajoute un disque sur la première tour
    }
    
    // On commence à déplacer les disques jusqu'à ce que la dernière tour ait tous les disques
    while (tours[nb_tours-1].len < nb)
    {   
        // Demande à l'utilisateur de sélectionner une tour de départ
        tour_dep = better_scan("Entrer le numero de tour 1-nb_tours ou on enlève un disque\n", 1, nb_tours);
        tour_dep--;
        disque = enleverDisque(tours + tour_dep); // Enlève un disque de la tour sélectionnée
        if (disque) // Si un disque a été enlevé
        {
            // Demande à l'utilisateur de sélectionner une tour de destination
            tour_fin = better_scan("Entrer le numero de tour 1-nb_tours ou on ajoute un disque\n", 1, nb_tours);
            tour_fin--;
            if (!ajouterDisque(tours + tour_fin, disque)) // Si l'ajout du disque échoue (disque trop grand)
            {
                printf("Le disque est plus grand que le disque en dessous \n");
                ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
            }
        } else
        {
            printf("La tour est vide \n");
            ajouterDisque(tours + tour_dep, disque); // Remet le disque sur la tour de départ
        }
        
        // Affiche l'état actuel des tours
        for (int i = 0; i < nb_tours; i++)
        {   
            printf("Tour %d :\n", i+1);
            afficheTour(tours+i);
        }
    }

    return 0;
}

``` 

<div id="2"></div>

## Exercice 2
[Télécharger l'exercice exo2.c](https://data2.cy.deltahmed.fr/DATA/info/DS1-2024-2025-V1_Informatique3-DSp2s1-2024-2025/exo2.c){:target="_blank"} 

![exercice 4](https://data2.cy.deltahmed.fr/DATA/info/DS1-2024-2025-V1_Informatique3-DSp2s1-2024-2025/2.jpg){: .w-75 .shadow .rounded-10 }

+ On déclare la structure Employe, représentant un employé
+ On déclare la structure Arbre, représentant un nœud de l'arbre d'entreprise


```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_NOM 20 // On définie de la longueur maximale pour le nom d'un employé

typedef struct employe_struct {
    char nom[MAX_NOM]; // Nom de l'employé
    float salaire;     // Salaire de l'employé
    int annee;         // Année d'embauche de l'employé
} Employe;

typedef struct arbre_struct {
    Employe* employe;                // Pointeur vers les informations de l'employé
    struct arbre_struct* sub1;       // Pointeur vers le premier subordonné
    struct arbre_struct* sub2;       // Pointeur vers le deuxième subordonné
    struct arbre_struct* sub3;       // Pointeur vers le troisième subordonné
} Arbre;
```

+ On crée la fonction qui affiche les subordonnés directs d'un employé donné

```c
void afficherSubordonnes(Arbre* entreprise) {
    if (entreprise == NULL) {        // Vérifie si l'arbre est vide
        printf("Vide \n");
    } else {
        // Affiche le nom des subordonnés s'ils existent
        if (entreprise->sub1 != NULL && entreprise->sub1->employe != NULL) {
            printf("%s \n", entreprise->sub1->employe->nom);
        }
        if (entreprise->sub2 != NULL && entreprise->sub2->employe != NULL) {
            printf("%s \n", entreprise->sub2->employe->nom);
        }
        if (entreprise->sub3 != NULL && entreprise->sub3->employe != NULL) {
            printf("%s \n", entreprise->sub3->employe->nom);
        }
    }
}
```

+ On crée la fonction qui affiche les subordonnés de niveau 2 d'un employé

```c
void AfficherN2(Arbre* entreprise) {
    if (entreprise == NULL) {         // Vérifie si l'arbre est vide
        printf("Vide \n");
    } else {
        // Appelle afficherSubordonnes pour chaque subordonné direct
        if (entreprise->sub1 != NULL) {
            afficherSubordonnes(entreprise->sub1);
        }
        if (entreprise->sub2 != NULL) {
            afficherSubordonnes(entreprise->sub2);
        }
        if (entreprise->sub3 != NULL) {
            afficherSubordonnes(entreprise->sub3);
        }
    }
}
```

+ On crée une fonction max qui retourne le maximum entre deux entiers
+ On crée une fonction max3 qui retourne le maximum entre trois entiers
+ On crée la fonction qui détermine le niveau de profondeur de l'arbre

```c
int max(int a, int b) {
    return a > b ? a : b;
}
int max3(int a, int b, int c) {
    return max(max(a, b), c);
}
int niveauEntreprise(Arbre* entreprise) {
    if (entreprise == NULL) {       // Cas de l'arbre vide
        return -1;
    }
    if (entreprise->sub1 == NULL && entreprise->sub2 == NULL && entreprise->sub3 == NULL) {
        return 0;                    // Cas où l'employé n'a pas de subordonnés
    }
    // Calcul récursif du niveau le plus profond des subordonnés
    return 1 + max3(niveauEntreprise(entreprise->sub1), niveauEntreprise(entreprise->sub2), niveauEntreprise(entreprise->sub3));
}
```

>  la notation `a > b ? a : b` est équivalente à `if (a > b) {return a;} else {return b;}`
{: .prompt-tip }

+ On crée la fonction qui recherche un employé par son nom dans l'arbre

```c
Employe* rechercherChef(Arbre* entreprise, char* nom) {
    if (nom == NULL) {
        exit(EXIT_FAILURE);          // Quitte si le nom recherché est invalide
    }
    if (entreprise == NULL || entreprise->employe == NULL) {
        return NULL;                 // Cas où l'arbre est vide ou que l'employé est inexistant
    }
    if (!strcmp(entreprise->employe->nom, nom)) {
        return entreprise->employe;  // Employé trouvé
    }
    // Recherche récursive dans les sous-arbres
    Employe* r1 = rechercherChef(entreprise->sub1, nom);
    Employe* r2 = rechercherChef(entreprise->sub2, nom);
    Employe* r3 = rechercherChef(entreprise->sub3, nom);
    if (r1 != NULL) {
        return r1;
    }
    if (r2 != NULL) {
        return r2;
    }
    if (r3 != NULL) {
        return r3;
    }
    return NULL;                     // Employé non trouvé
}
```

+ Déclaration des structures nécessaires pour le parcours en largeur de l'arbre

```c
typedef struct chainon_struct {
    Arbre* value;                   // Pointeur vers le nœud de l'arbre
    struct chainon_struct* next;    // Pointeur vers l'élément suivant
} Chainon;

typedef struct file_struct {
    Chainon* tete;                  // Pointeur vers le début de la file
    Chainon* fin;                   // Pointeur vers la fin de la file
} File;
```

+ On crée la fonction qui initialise une file vide

```c
File* creationFile() {
    File* nouvelleFile = malloc(sizeof(File));
    if (nouvelleFile == NULL) {
        exit(EXIT_FAILURE);
    }
    nouvelleFile->tete = NULL;
    nouvelleFile->fin = NULL;
    return nouvelleFile;
}
```

+ On crée la fonction qui crée un chainon pour stocker un nœud de l'arbre

```c
Chainon* creationChainon(Arbre* a) {
    Chainon* nouveau = malloc(sizeof(Chainon));
    if (nouveau == NULL) {
        exit(EXIT_FAILURE);
    }
    nouveau->value = a;
    nouveau->next = NULL;
    return nouveau;
}
```

+ La fonction défilé est donnée comme déjà écrite

```c
void enfiler(File* pfile, Arbre* a);
```

+ On crée la fonction qui retire un nœud de la file (défiler)

```c
int defiler(File* pfile, Arbre** value) {
    if (pfile == NULL || pfile->tete == NULL) {
        return -1;                  // Erreur si la file est vide
    }
    Chainon* tmp = pfile->tete->next;
    *value = pfile->tete->value;    // Sauvegarde la valeur de tête
    free(pfile->tete);              // Libère l'espace mémoire de la tête
    pfile->tete = tmp;              // Avance la tête de la file
    if (pfile->tete == NULL) {      // Met fin à NULL si la file est vide
        pfile->fin = NULL;
    }
    return 0;
}
```

+ On crée la fonction qui effectue le parcours en largeur de l'arbre

```c
void parcoursLargeur(Arbre* a) {
    File* f = creationFile();        // Création de la file pour le parcours en largeur
    Arbre* value;
    enfiler(f, a);                   // Enfile la racine de l'arbre
    while (f->tete != NULL) {        // Tant que la file n'est pas vide
        defiler(f, &value);
        traiter(value);              // Affiche ou traite le nœud actuel
        if (!estVide(value)) {       // Si le nœud n'est pas vide, enfile ses subordonnés
            if (value->sub1 != NULL) {
                enfiler(f, value->sub1);
            }
            if (value->sub2 != NULL) {
                enfiler(f, value->sub2);
            }
            if (value->sub3 != NULL) {
                enfiler(f, value->sub3);
            }
        }
    }
}
```

Exercices : [1](#1) [2](#2)
