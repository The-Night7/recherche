---
title: Fiche Gestion des Fichiers en C
author: [LucienL]
date: 2025-02-17 01:00:00 +0100
categories: [PREING1 S2,Informatique2]
tags: [PREING1 S2,Informatique2,Lucien L.,2024/2025]
math: true
mermaid: true
division_title : 2024/2025
---

# Fiche de Révision : Gestion des Fichiers en C

## 1. Introduction aux fichiers

En C, les fichiers permettent de stocker et de manipuler des données de manière persistante. On utilise la bibliothèque `<stdio.h>` pour les manipuler.



## 2. Types de fichiers

### 1. Fichiers Texte
- Stockent des caractères lisibles (`.txt`, `.csv`, etc.).
- Utilisent des fonctions comme `fprintf()`, `fscanf()`.
- Exemple : Fichier contenant du texte brut.

### 2. Fichiers Binaires
- Stockent des données sous forme binaire (`.dat`, `.bin`, etc.).
- Plus compacts et plus rapides.
- Utilisent `fwrite()`, `fread()`.



## 3. Ouverture et Fermeture d'un Fichier

Avant d'utiliser un fichier, il faut l'ouvrir avec `fopen()` et le fermer avec `fclose()`.

```c
FILE *fichier;
fichier = fopen("monfichier.txt", "r"); // Ouvre en lecture
if (fichier == NULL) {
    printf("Erreur d'ouverture du fichier !
");
    return 1;
}
fclose(fichier);
```

### Modes d'ouverture courants

| Mode | Type   | Description |
|------|--------|-------------|
| r    | Texte  | Lecture (erreur si le fichier n'existe pas) |
| w    | Texte  | Écriture (création ou écrasement du fichier) |
| a    | Texte  | Ajout à la fin du fichier (création si inexistant) |
| r+   | Texte  | Lecture/écriture (erreur si inexistant) |
| w+   | Texte  | Lecture/écriture (efface le fichier existant) |
| a+   | Texte  | Lecture/ajout (création si inexistant, ajoute à la fin) |
| rb   | Binaire| Lecture en mode binaire |
| wb   | Binaire| Écriture en mode binaire |
| ab   | Binaire| Ajout en mode binaire |
| rb+  | Binaire| Lecture/écriture binaire (erreur si inexistant) |
| wb+  | Binaire| Lecture/écriture binaire (efface le fichier existant) |
| ab+  | Binaire| Lecture/ajout binaire (ajoute à la fin) |



## 4. Lecture et Écriture

### 1. Fichiers Texte

#### Écriture

```c
FILE *f = fopen("test.txt", "w");
fprintf(f, "Bonjour monde !
");
fclose(f);
```

#### Lecture avec `fgets`

```c
char buffer[100];
FILE *f = fopen("test.txt", "r");
fgets(buffer, 100, f); // lit une ligne au maximum de 99 caractères
printf("%s", buffer);
fclose(f);
```

#### Lecture caractère par caractère avec `fgetc`

```c
FILE *f = fopen("test.txt", "r");
int c;
while ((c = fgetc(f)) != EOF) {
    putchar(c);
}
fclose(f);
```

### 2. Fichiers Binaires

#### Écriture

```c
int nombre = 42;
FILE *f = fopen("data.bin", "wb");
fwrite(&nombre, sizeof(int), 1, f);
fclose(f);
```

#### Lecture

```c
int nombre_lu;
FILE *f = fopen("data.bin", "rb");
fread(&nombre_lu, sizeof(int), 1, f);
printf("%d", nombre_lu);
fclose(f);
```



## 5. Manipulation Avancée

### 1. Déplacement dans un fichier

- `fseek(FILE* flux, long deplacement, int modeDeplacement)` : Déplace le curseur.
  - `SEEK_SET` (0) : Depuis le début du fichier.
  - `SEEK_CUR` (1) : Depuis la position actuelle.
  - `SEEK_END` (2) : Depuis la fin du fichier.

- `ftell(f)` : Renvoie la position actuelle.
- `rewind(f)` : Remet le curseur au début.

```c
fseek(f, 10, SEEK_SET); // Se déplace à la 10e position
long position = ftell(f);
rewind(f);
```

### 2. Fermeture

- `fclose(f)` libère la mémoire.



## 6. Résumé

- Ouvrir un fichier avec `fopen()` et vérifier si `NULL`.
- Lire et écrire avec `fprintf()`, `fscanf()` (texte) ou `fwrite()`, `fread()` (binaire).
- Utiliser `fgets()` pour lire des lignes et `fgetc()` pour lire caractère par caractère.
- Fermer le fichier avec `fclose()`.
- Déplacer le curseur avec `fseek()`, `ftell()`, `rewind()`.

**Bien choisir le mode (`r`, `w`, `a`, etc.) pour éviter les pertes de données !**
