---
title: TD1 Structures Correction
author: [AhmedA]
date: 2024-02-03 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Ahmed A.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---


Exercices : [1](#exercice-1) [2](#exercice-2) [3](#exercice-3) [4](#exercice-4) 



> Regarder la correction uniquement après avoir travaillé par vous-même, car si vous ne le faites pas, c’est le meilleur moyen de rater vos DS/CC.
{: .prompt-danger }


## Exercice 1

![exercice 1](https://data.cy.deltahmed.fr/DATA/TD1-Structures_Informatique2p1s2/1.jpg){: .w-75 .shadow .rounded-10 }

On commence par importer les bibliothèques que l'on vas utiliser et créer la structure `Point` demandée

```c
#include <stdio.h>
#include <math.h>

typedef struct {
    float x;
    float y;
}Point;
```

+ On crée une fonction sécurisée pour le scanf

```c
float better_scan(char * message){
    int ret_var= 0;
    float val;
    while (ret_var != 1)
    {   
        printf(message);
        ret_var = scanf("%f", &val);
        while(getchar()!='\n'){} // Ligne facultative de sécurisation
    }
    return val;
}
```
> Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
{: .prompt-info }

+ On crée une fonction qui permet de créer un Point à partir des saisies de l'utilisateur et procédure pour afficher un Point

```c
// Constructeur
Point constructeur_Point() {
    Point p;
    p.x = better_scan("Entrez l'abscisse du point :" ); // on utilise le scanf ou la fonction facultative
    p.y = better_scan("Entrez l'ordonnée du point : ");
    return p;
}

// Affichage
void affiche_Point(Point p) {
    printf("(%f, %f)\n", p.x, p.y);
}
```

+ On crée la fonction pour ajouter deux Points et la fonction qui permet de calculer la longueur avec la formule $$\sqrt{(x_{b}-x_{a})^{2} + (y_{b} - y_{a})^{2}}$$

```c
// Additionner deux points
Point ajouter_Point(Point a, Point b) {
    Point resultat;
    resultat.x = a.x + b.x;
    resultat.y = a.y + b.y;
    return resultat;
}

// Calculer la longueur
float longueur(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2));
}
```
+ On crée maintenant la fonction qui vérifie si les points forment un carré et la fonction qui vérifie si les points sont alignées

```c
// Fonction pour vérifier si quatre Points forment un carré
int estCarre(Point a, Point b, Point c, Point d) {
    float AB = longueur(a, b);
    float AC = longueur(a, c);
    float AD = longueur(a, d);
    if (AB == AC && AB == AD) {
        float BC = longueur(b, c);
        float BD = longueur(b, d);
        float CD = longueur(c, d);
        if (BC == BD && BC == CD) {
            return 1; // Les côtés sont égaux, c'est un carré
        }
    }
    return 0;
}

// Fonction pour vérifier si trois Points sont alignés
int sontAlignes(Point a, Point b, Point c) {
    return (b.y - a.y) * (c.x - a.x) == (c.y - a.y) * (b.x - a.x);
}
```

+ On peut maintenant utiliser le tout dans le main 

```c
int main() {
    // Déclaration et initialisation de deux Points
    Point point1, point2;
    
    printf("Saisie des coordonnées du premier point :\n");
    point1 = constructeur_Point();
    printf("Saisie des coordonnées du deuxième point :\n");
    point2 = constructeur_Point();

    printf("Les coordonnées du premier point sont : ");
    affiche_Point(point1);
    printf("Les coordonnées du deuxième point sont : ");
    affiche_Point(point2);

    // Addition de deux Points
    Point resultatAddition = ajouter_Point(point1, point2);
    printf("La somme des deux points est : ");
    affiche_Point(resultatAddition);

    // Calcul de la longueur entre deux Points
    printf("La longueur entre le premier et le deuxième point est : %f\n", longueur(point1, point2));

    // Vérification si quatre Points forment un carré
    Point point3 = {4, 4};
    Point point4 = {8, 0};
    printf("Les quatre points forment-ils un carré ? %s\n", estCarre(point1, point2, point3, point4) ? "Oui" : "Non");

    // Vérification si trois Points sont alignés
    Point point5 = {2, 2};
    Point point6 = {3, 3};
    printf("Les trois points sont-ils alignés ? %s\n", sontAlignes(point1, point5, point6) ? "Oui" : "Non");

    return 0;
}

```

> La notation `variable = Condition ? X : Y` correspond a `si Condition est vraie ? alors variable = X : sinon variable = Y`
{: .prompt-info }

## Exercice 2

![exercice 2](https://data.cy.deltahmed.fr/DATA/TD1-Structures_Informatique2p1s2/2.jpg){: .w-75 .shadow .rounded-10 }

On commence par importer les bibliothèques que l'on vas utiliser et créer la structure `Date` demandée

```c
#include <stdio.h>

// Déclaration de la structure Date
typedef struct  {
    int jour;
    int mois;
    int annee;
}Date;
```

+ On crée deux fonctions qui vont nous permettre de créer le constructeur de `Date`
    + La première fonction est une fonction qui verifie si une date est valide ou non

    ```c
    int DateValide(Date date) {
        // Vérifie si le mois est entre 1 et 12
        if (date.mois < 1 || date.mois > 12)
            return 0;
        // Vérifie si le jour est entre 1 et 30 (pour simplifier)
        if (date.jour < 1 || date.jour > 30)
            return 0;
        // Toutes les conditions sont remplies, la date est valide
        return 1;
    }
    ```
    +  La deuxième fonction est un `scanf` sécurisé

    ```c
    int better_scan(char * message){
    int ret_var = 0;
    int value;
    while (ret_var != 1)
    {   
        printf(message);
        ret_var = scanf("%d", &value);
        while(getchar()!='\n'){}
    }
    return value;
    
    }   
    ```

    > Cette fonction est facultative, la ligne `while(getchar()!='\n'){}` permet de vider le buffer et d'avoir un `scanf` qui ne boucle pas a l'infinie lors d'une mauvaise saisie.
    {: .prompt-info }

    + On peut maintenant créer le constructeur de `Date`

    ```c
    Date constructeur_Date() {
        Date date;
    
        do { 
            printf("Saisir une date valide : \n");
            date.jour = better_scan("Saisissez le jour : \n");
            date.mois = better_scan("Saisissez le mois : \n");
            date.annee = better_scan("Saisissez l'année : \n");
        } while (!DateValide(date));
        return date;
    }
    ```

+ Mainteant on fait la procédure pour afficher une date

```c
void affiche_Date(Date date) {
    printf("%d/%d/%d\n", date.jour, date.mois, date.annee);
}
```

+ Mainteant que l'on a tout ce dont on a besoin on peut créer les deux fonction qui ajoute une date et qui en enlève une 

```c
// Ajoute un nombre de jours à une date
Date ajoute_jour(Date date, int jours) {
    
    date.jour += jours;
    while (date.jour > 30){// Vérifie si le jour dépasse 30
        date.jour -= 30;
        while(date.mois+1 > 12){ // Si le mois dépasse 12, on passe à l'année suivante
            date.mois = 1;
            date.annee++;
        }
        
    }
    return date;
}
```

```c
// Enlève un nombre de jours à une date
Date enlever_jour(Date date, int jours) {
    date.jour -= jours; // Enlève le nombre de jours
    while (date.jour < 1) { // Vérifie si le jour est négatif
        date.jour += 30; // Si oui, on revient au mois précédent
        while (date.mois -1 < 1) {
            date.mois = 12;
            date.annee--;
        }
    }
    return date;
}
```

+ on peut maintenant tester le tout dans le `main`

```c
int main() {
    // Déclaration d'une variable de type Date et saisie par l'utilisateur
    Date date = constructeur_Date();

    // Affichage de la date saisie
    printf("Date saisie : ");
    affiche_Date(date);

    // Ajout de jours à la date
    int jours_ajouter = 5;
    Date nouvelle_date = ajoute_jour(date, jours_ajouter);
    printf("Après l'ajout de %d jours : ", jours_ajouter);
    affiche_Date(nouvelle_date);

    // Enlèvement de jours à la date
    int jours_enlever = 3;
    Date date_modifiee = enlever_jour(nouvelle_date, jours_enlever);
    printf("Après l'enlèvement de %d jours : ", jours_enlever);
    affiche_Date(date_modifiee);

    return 0;
}
```


## Exercice 3

![exercice 3](https://data.cy.deltahmed.fr/DATA/TD1-Structures_Informatique2p1s2/3_1.jpg){: .w-75 .shadow .rounded-10 }
![exercice 3](https://data.cy.deltahmed.fr/DATA/TD1-Structures_Informatique2p1s2/3_2.jpg){: .w-75 .shadow .rounded-10 }

On commence par importer les bibliothèques nécessaires et définir la structure `Ninja` pour représenter un combattant.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_CHAR 50

// Structure représentant un Ninja
typedef struct {
    char nom[MAX_CHAR];
    float attaque;
    float defense;
    float esquive;
    float vie;
}Ninja;

```

+ On crée la fonction `initialiserNinja` qui permet d'initialiser un Ninja avec des valeurs aléatoires pour ses caractéristiques telles que l'attaque, la défense, l'esquive et la vie.

```c
// Fonction pour initialiser un Ninja avec des valeurs aléatoires
Ninja initialiserNinja() {
    Ninja ninja;
    ninja.attaque = 5.0 + (rand() % 6); // Entre 5.0 et 10.0
    ninja.defense = 2.0 + (rand() % 3); // Entre 2.0 et 4.0
    ninja.esquive = 0.1 + (float)rand() / RAND_MAX * (0.2 - 0.1); // Entre 0.1 et 0.2
    ninja.vie = 80.0 + (rand() % 21); // Entre 80.0 et 100.0
    return ninja;
}
```

+ On crée la fonction `afficherNinja` qui affiche les caractéristiques d'un `Ninja` donné.

```c
void afficherNinja(Ninja ninja) {
    printf("Nom : %s\n", ninja.nom);
    printf("Attaque : %f\n", ninja.attaque);
    printf("Défense : %f\n", ninja.defense);
    printf("Esquive : %f\n", ninja.esquive);
    printf("Vie : %f\n", ninja.vie);
}
```
+ on crée la fonction `combat` qui simule un combat entre deux `Ninjas` et affiche les résultats du combat.

```c
void combat(Ninja a, Ninja b) {
    printf("Le combat commence entre %s et %s!\n", a.nom, b.nom);
    while (a.vie > 0 && b.vie > 0) {
        // Ninja a attaque Ninja b
        float jet_a = (float)rand() / RAND_MAX;
        if (jet_a > b.esquive) {
            float degats_a = a.attaque - b.defense;
            if (degats_a < 0){
                degats_a = 0; // Ne peut pas être négatif
                }
            b.vie -= degats_a;
            printf("%s attaque %s et lui inflige %.1f dégâts!\n", a.nom, b.nom, degats_a);
        } else {
            printf("%s esquive l'attaque de %s!\n", b.nom, a.nom);
        }
        if (b.vie <= 0) {
            printf("%s tombe à terre! %s gagne le combat!\n", b.nom, a.nom);
            break;
        }

        // Ninja b attaque Ninja a
        float jet_b = (float)rand() / RAND_MAX;
        if (jet_b > a.esquive) {
            float degats_b = b.attaque - a.defense;
            if (degats_b < 0) degats_b = 0; // Ne peut pas être négatif
            a.vie -= degats_b;
            printf("%s attaque %s et lui inflige %.1f dégâts!\n", b.nom, a.nom, degats_b);
        } else {
            printf("%s esquive l'attaque de %s!\n", a.nom, b.nom);
        }
        if (a.vie <= 0) {
            printf("%s tombe à terre! %s gagne le combat!\n", a.nom, b.nom);
            break;
        }
    }
}
```
 
+ On peut maintenant tester les fonction : Le programme principal `main` initialise deux `ninjas`, récupère leurs noms depuis l'entrée standard, affiche leurs caractéristiques, puis simule un combat entre eux.

```c
int main() {
    srand(time(NULL));
    // Initialisation des deux ninjas avec des valeurs aléatoires
    Ninja ninja1, ninja2;
    ninja1 = initialiserNinja();
    ninja2 = initialiserNinja();

    printf("Nom du premier Ninja : ");
    if (fgets(ninja1.nom,MAX_CHAR,stdin) == NULL) {
        exit(1);
    }
    printf("Nom du deuxième Ninja : ");
    if (fgets(ninja2.nom,MAX_CHAR,stdin) == NULL) {
        exit(1);
    }
    ninja1.nom[strcspn(ninja1.nom, "\n")] = '\0';
    ninja2.nom[strcspn(ninja1.nom, "\n")] = '\0';

    // Affichage des caractéristiques des deux ninjas
    printf("Caractéristiques du premier Ninja :\n");
    afficherNinja(ninja1);
    printf("\n");
    printf("Caractéristiques du deuxième Ninja :\n");
    afficherNinja(ninja2);
    printf("\n");

    // Combat entre les deux ninjas
    combat(ninja1, ninja2);

    return 0;
}
```

> `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fontion renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`, `strcspn` prend en argument une chaîne de char et une liste (chaîne de char) de rejet, Elle Renvoie la longueur de la plus grande sous-chaîne (en partant du début de la chaîne initiale) ne contenant aucun des caractères spécifiés dans la liste des caractères en rejet, ici elle permet de trouver l'index avant le \n.
{: .prompt-info }

## Exercice 4

![exercice 4](https://data.cy.deltahmed.fr/DATA/TD1-Structures_Informatique2p1s2/4.jpg){: .w-75 .shadow .rounded-10 }

+ On commence par importer les bibliothèques nécessaires et définir la structure `Personne` pour représenter une personne avec son prénom et sa date de naissance.

```c

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_PRENOM 50 // on definie la taille max du prenom

typedef struct {
    char prenom[MAX_PRENOM];
    Date date_naissance;
} Personne;

```
+ on Ajoute toute les fonctions et structures/type définie dans [L'exercice 2](#exercice-2) soit :

```c
typedef struct  {
    int jour;
    int mois;
    int annee;
}Date;
```

```c
int DateValide(Date date)
```

```c
int better_scan(char * message)
```

```c
Date constructeur_Date()
```

```c
void affiche_Date(Date date)
```
+ On crée la procédure d'affichage d'une `Personne`

```c
void afficherPersonne(Personne personne) {
    printf("Prénom : %s\n", personne.prenom);
    printf("Date de naissance : ");
    affiche_Date(personne.date_naissance);
    printf("\n");
}

```

+ On peut ainsi créer le constructeur de `Personne`

```c
Personne constructeurPersonne(){
    Personne personne;
    printf("Entrez le prénom de la personne : ");
    // partie facultative : On peut aussi utiliser un scanf
    if (fgets(personne.prenom,MAX_PRENOM,stdin) == NULL) {
        exit(1);
    }
    personne.prenom[strcspn(personne.prenom, "\n")] = '\0';
    // fin de la partie facultative

    printf("Entrez la date de naissance : ");
    personne.date_naissance = constructeur_Date();
    return personne;
}

```

> `exit()` permet de sortir du programme avec un code d'erreur. `fgets` prend en argument la variable où stocker la valeur d'entrée, le nombre maximum de char qu'elle doit enregistrer et pour finir le `stream` qu'elle doit lire (ici `stdin`) cette fontion renvoie un pointeur vers la chaîne de char si la fonction échoue elle renvoie `NULL`, `strcspn` prend en argument une chaîne de char et une liste (chaîne de char) de rejet, Elle Renvoie la longueur de la plus grande sous-chaîne (en partant du début de la chaîne initiale) ne contenant aucun des caractères spécifiés dans la liste des caractères en rejet, ici elle permet de trouver l'index avant le \n.
{: .prompt-info }

+ On peut maintenant créer la procédure `bonAnniversaire` qui affiche les personnes dont c'est l'anniversaire, en comparant leur date de naissance à une date donnée

```c

void bonAnniversaire(Personne personnes[], int nb_personnes, Date date) {
    printf("Bon anniversaire à : \n");
    int nb = 0;
    for (int i = 0; i < nb_personnes; i++) {
        if (personnes[i].date_naissance.jour == date.jour && 
            personnes[i].date_naissance.mois == date.mois &&
            personnes[i].date_naissance.annee != date.annee) {
            printf("%s\n", personnes[i].prenom);
            nb++;
        }
    }
    if (!nb)
    {
        printf("Personne dommage \n");
    }
    
}
```

+ On peut donc tester dans le `main` tout cela

```c
int main() {
    srand(time(NULL));

    // Déclaration et initialisation du tableau de personnes
    Personne personnes[10];
    for (int i = 0; i < 10; i++) {
        printf("Personne %d :\n", i + 1);
        personnes[i] = constructeurPersonne();
    }

    // Affichage des personnes et de leurs dates de naissance
    printf("\nCaractéristiques des personnes :\n");
    for (int i = 0; i < 10; i++) {
        afficherPersonne(personnes[i]);
    }

    // Génération d'une date aléatoire pour tester
    Date date_test;
    date_test.jour = rand() % 31 + 1; // Jour entre 1 et 31
    date_test.mois = rand() % 12 + 1; // Mois entre 1 et 12
    date_test.annee = 2024; // Année arbitraire

    printf("\nDate de test : ");
    affiche_Date(date_test);
    printf("\n");

    // Vérification des anniversaires
    bonAnniversaire(personnes, 10, date_test);

    return 0;
}
```


Exercices : [1](#exercice-1) [2](#exercice-2) [3](#exercice-3) [4](#exercice-4) 