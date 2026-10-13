---
title: DS2 2023 2024 V2 Correction
cyauthor: [RGrignon]
date: 2024-05-30 01:00:00 +0100
categories: [PREING1 S2,Informatique2-DS]
tags: [PREING1 S2,Informatique2-DS,R. Grignon,DS2]
division_title : DS2
---

LINK


+ Cette correction ajoute en plus des points de robustesse qui **n'etait pas demandé a ce ds mais qui vous sera demandé** au DS 3. Notament :
    - la vérification du retour des scanf
    - la vérification des paramètres des fonctions (pointeur ou autre si besoin)

```c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char *nom;
    unsigned int num;
    int dep;
    float salaire;
} Employe;

typedef struct
{
    int taille;
    Employe **tab;
    float prime;
} Activite;

Employe constructeur()
{
    Employe e;
    char nom[100]; // nom tampon
    printf("Nom : ");
    scanf("%s", nom);
    e.nom = malloc(sizeof(char) * (strlen(nom) + 1)); // obligation d'utiliser un malloc car la chaîne de caractère n'a pas été allouée
    if (e.nom == NULL)
    {
        exit(1);
    }

    strcpy(e.nom, nom); // ou le faire à la main

    do
    {
        printf("Numero : ");
        scanf("%d", &e.num);
    } while (e.num < 0);

    // 0.5
    do
    {
        printf("%d", e.dep);
        scanf("%d", &e.dep);
    } while (e.dep < 1 || e.dep > 95);
    // 0.5
    do
    {
        printf("Salaire : ");
        scanf("%f", &e.salaire);
    } while (e.salaire < 0);
    return e;
}

Employe *creationEntreprise(int *taille)
{ // utilisation d'un pointeur car on doit aussi récupérer la taille du tableau créé
    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (taille == NULL)
    {
        exit(2);
    }

    Employe *e = NULL;
    do
    {
        printf("Taille de l'entreprise : ");
        scanf("%d", taille);
    } while (*taille < 0);
    e = malloc(sizeof(Employe) * (*taille));
    if (e == NULL)
    {
        exit(3);
    }
    for (int i = 0; i < *taille; i++)
    {
        e[i] = constructeur();
    }
    return e;
}

float salaireDepartement(Employe *e, int taille, int dep, float sal)
{
    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (e == NULL || taille < 0)
    {
        exit(4);
    }

    if (taille == 0)
    {
        return sal;
    }
    else if (e->dep == dep)
    {
        return salaireDepartement(e + 1, taille - 1, dep, sal + e->salaire);
    }
    else
        return salaireDepartement(e + 1, taille - 1, dep, sal);
}

```

+ Question 4 : 
    + 0.5 pt. complexité linéaire O(n) (on parcours l'integralité du tableau une fois).


```c

int augment(Employe *e, int taille)
{
    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (taille < 0 || e == NULL)
    {
        exit(5);
    }

    if (taille == 0)
    {
        return 0;
    }
    else if (e->salaire < 2500)
    {
        e->salaire = e->salaire + e->salaire * 0.025;
        return 1 + augment(e + 1, taille - 1);
    }
    else
    {
        return augment(e + 1, taille - 1);
    }
}

Employe *rechercher(Employe *e, int taille, int num)
{
    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (e == NULL || taille < 0)
    {
        exit(7);
    }

    int a = 0;
    int b = taille - 1;
    int m = (a + b) / 2;
    while (a <= b)
    {
        if (e[m].num == num)
        {
            return e + m;
        }
        else if (e[m].num < num)
        {
            a = m + 1;
        }
        else
        {
            b = m - 1;
        }
        m = (a + b) / 2;
    }
    return NULL;
}
```

+ question 7 :
    + Le tableau tab va contenir des pointeurs sur employé. Ce choix permet d'optimiser la mémoire car
        +  un employé peut participer à plusieurs entreprise, donc on ne creera pas de doublon d'employé (raison principale et suffisante pour valider la réponse)
        + structure plus legere en mémoire

```c

Activite constructeurActivite(Employe *e)
{

    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (e == NULL)
    {
        exit(8);
    }

    Activite a;
    int taille;
    int num;
    do
    {
        printf("Taille de l'activité : ");
        scanf("%d", &taille);
    } while (taille < 0);
    a.taille = taille;
    a.tab = malloc(sizeof(Employe *) * taille);
    if (a.tab == NULL)
    {
        exit(9);
    }
    for (int i = 0; i < taille; i++)
    {
        do
        {
            printf("Saisir le numero de l'employé : ");
            scanf("%d", &num);
            a.tab[i] = rechercher(e, taille, num);
        } while (a.tab[i] != NULL); // verifier que l'employe existe bien
    }
    return a;
}

int participation(Activite a, int num)
{
    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (a.tab == NULL)
    {
        exit(11);
    }

    for (int i = 0; i < a.taille; i++)
    {
        if (a.tab[i]->num == num)
        {
            return 1;
        }
    }
    return 0;
}
```

+ Cette fonction a une complexité en O(n) (on doit parcourir le tableau d'employé). On ne peut pas avoir une complexité logarithmique dans ce cas car il est impossible d'effectuer une recherche dichotomique : le tableau d'employé n'est pas trié. 


+ On n'est même pas obligé d'utiliser le tableau d'employé (meuilleure complexité), mais compter juste si le tableau d'employé est parcouru quand même car il est demandé en argument dans l'énoncé ce qui peut induire en erreur.

>  si on fait une boucle sur le tableau d'employé il faut aussi vérifié s'il participe à l'activité avec la fonction précédente
{: .prompt-warning }

```c

void majSalaire(Employe *e, int taille_emp, Activite *a, int taille_a)
{
    // verification paramètre (pas obligatoire au DS2 mais obligatoire au DS3)
    if (e == NULL || taille_emp < 0 || a == NULL || taille_a < 0 || a->tab == NULL)
    {
        exit(12);
    }

    for (int i = 0; i < taille_a; i++)
    {
        for (int j = 0; j < a->taille; j++)
        { // ou sur le tableau d'employe
            a[i].tab[j]->salaire = a[i].tab[j]->salaire + a[i].prime;
        }
    }
}
```

+ question 12   :

    + si l'étudiant a parcourur le tableau tab d'activité : la complexité depent du nombre d'activité et d'employé par activité (taille)

    + si l'étudiant a parcouru le tableau d'employé total : la complexité depend du nombre d'activité; du nombre d'employé par activité et du nombre d'employé.

+ Dans tout les cas la complexité est polynomiale.

