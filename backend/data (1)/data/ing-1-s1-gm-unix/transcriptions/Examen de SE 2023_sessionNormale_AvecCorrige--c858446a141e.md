---
source: "ING 1/S1 GM /UNIX/Examen/Examen de SE 2023_sessionNormale_AvecCorrige.pdf"
pages: 10
transcription: énoncé et corrigé transcrits, erreurs de source signalées
transcription_date: 2026-10-16
verification: texte natif comparé aux dix pages du PDF ; QCM en gras et code en image lus visuellement ; chronogrammes, moyennes et adresses recalculés
---

# Système d’exploitation — Examen du 12 janvier 2023, session normale, avec corrigé

**CY Tech — année 2022–2023.** ING1 Informatique-Mathématiques appliquées et ING1 Informatique-Mathématiques Apprentissage.

**Enseignants :** A. Bertails, N. A. Diago, T. Guidini, J. A. Lorenzo.

Les réponses signalées dans le PDF sont conservées. Les observations de transcription et les rectifications sont explicitement séparées du corrigé d’origine.

## Modalités — page 1

- Durée : 2 heures.
- Rédiger exclusivement à l’aide d’un stylo à encre.
- Toutes les affaires — sacs, vestes, trousse, etc. — doivent être placées à l’avant de la salle.
- Aucun document autorisé ; calculatrice autorisée.
- Le QCM peut contenir une ou plusieurs réponses valides.
- Aucune question aux enseignants : poser des hypothèses en cas de doute.
- Aucune sortie avant une durée incompressible d’une heure.
- Aucun déplacement autorisé.

## QCM — 6 points — pages 1 et 2

Répondre sur la copie, pas sur le sujet. Les réponses en **gras** reproduisent le marquage du corrigé ; les cases du PDF ne sont pas cochées.

### a) La swap ou espace d’échange…

- ☐ Est disponible à l’utilisateur sur le point de montage `/swap`.
- ☐ Évite l’utilisation du système de pagination.
- ☐ Contient l’installation du système d’exploitation.
- ☐ **Aucune des réponses n’est valide.**

### b) Traduction d’une adresse virtuelle

Si le bit de validité V dans la table de pages est à 0 :

- ☐ La page est en mémoire réelle.
- ☐ **Un défaut de page est déclenché.**
- ☐ Le système choisira un algorithme de remplacement de pages.
- ☐ Aucune des réponses n’est valide.

### c) Installation d’un paquet .deb

On a téléchargé un paquet `*.deb` depuis Internet parce qu’il n’est pas disponible dans les dépôts officiels. Quelle commande utiliser ?

- ☐ `add-apt-repository`.
- ☐ `apt install`.
- ☐ **`dpkg`.**
- ☐ Aucune des réponses n’est valide.

### d) Un conteneur Docker…

- ☐ **N’a pas de noyau propre ; il utilise le noyau de l’hôte.**
- ☐ Nécessite un hyperviseur.
- ☐ N’a pas besoin d’une image.
- ☐ Aucune des réponses n’est valide.

### e) VirtualBox est un hyperviseur…

- ☐ De type I.
- ☐ **De type II.**
- ☐ De type III.
- ☐ Aucune des réponses n’est valide.

### f) Comment classifier les interruptions attendues par le processeur ?

- ☐ Externes, ou déroutements, et internes, matérielles et logicielles.
- ☐ **Externes, matérielles et logicielles, et internes, ou déroutements.**
- ☐ Internes logicielles et externes matérielles.
- ☐ Internes matérielles et externes logicielles.

## Questions de cours — 5 points — pages 2 à 4

### a) Gestionnaire de système de fichiers virtuels

**Question.** Expliquer ses fonctionnalités et son rôle dans le fonctionnement du système d’exploitation.

**Réponse du PDF.** Un système de gestion de fichiers, ou SGF, est une structure de données permettant de stocker les informations et de les organiser dans des fichiers sur des mémoires secondaires. Il est la partie la plus visible d’un SE. Il gère le stockage et la manipulation des fichiers sur le matériel physique et offre les primitives permettant de manipuler les fichiers.

Ses tâches sont :

- Fournir une interface « conviviale » facilitant la manipulation des fichiers.
- Gérer l’organisation des fichiers sur le disque et l’allocation de l’espace disque aux fichiers.
- Gérer l’espace libre.
- Gérer les fichiers dans un environnement multi-utilisateurs.

**Observation de transcription.** La question porte sur le gestionnaire de fichiers virtuels ; la réponse fournie décrit le SGF en général.

### b) Mémoire cache et mémoire centrale

**Question.** Expliquer leur différence.

**Réponse du PDF.** La mémoire cache évite de rechercher en mémoire centrale des données déjà recherchées, en les conservant près du processeur dans une petite mémoire à accès rapide. Elle est gérée par le matériel, hors du SE.

Principe de localité :

- **Temporelle :** tendance à réutiliser des données récemment consultées, par exemple les instructions d’une boucle.
- **Spatiale :** tendance à référencer des données voisines de données récemment consultées, par exemple `a[i]`, `a[i+1]` dans un tableau.

La mémoire centrale, vive ou RAM, est la mémoire dans laquelle les données et les processus sont placés lors de leur traitement. Elle présente les caractéristiques suivantes :

- Accès rapide.
- Mémoire volatile, nécessitant du courant électrique.
- Cases numérotées à partir de 0 ; le numéro correspond à l’adresse. Chaque case contient un octet, soit 8 bits ; un bit vaut 0 ou 1, d’où $2^8=256$ valeurs possibles pour un octet.
- Deux opérations : lecture et écriture.

### c) Machine virtuelle et conteneur Docker

**Question.** Expliquer leur différence.

**Réponse du PDF.** Une machine virtuelle, ou VM, est un environnement entièrement virtualisé fonctionnant sur une machine physique. Elle exécute son propre système d’exploitation et bénéficie des mêmes équipements qu’une machine physique : CPU, RAM, disque dur et carte réseau.

Docker est un logiciel libre de gestion des conteneurs. Un conteneur regroupe le code et toutes ses dépendances pour que l’application s’exécute rapidement et de manière fiable d’un environnement informatique à un autre. C’est l’exécution d’une image : il possède la copie du système de fichiers de l’image et la capacité de lancer des processus.

### d) Snap et Flatpak, comparés à .deb et .rpm

**Question.** Quel est l’avantage des paquets Snap et Flatpak par rapport aux paquets classiques `.deb` ou `.rpm` ?

**Réponse du PDF.** Snap est un système d’empaquetage et de déploiement pour les systèmes utilisant le noyau Linux. Les paquets, appelés *snaps*, et l’outil `snapd` fonctionnent sur une gamme de distributions Linux et permettent aux développeurs de distribuer leurs applications directement aux utilisateurs. Les snaps sont des applications autonomes exécutées dans un bac à sable avec un accès modéré au système hôte.

Flatpak, anciennement `xdg-app`, est un système de virtualisation d’applications pour les distributions GNU/Linux de bureau.

`dpkg`, outil de bas niveau, sert à installer, supprimer et fournir des informations sur les paquets `*.deb`, pris en charge par les distributions basées sur Debian.

`rpm` permet d’installer, mettre à jour, désinstaller, vérifier et rechercher des paquets avec les droits de l’utilisateur `root`.

### e) Commandes de mise à niveau

**Question.** Quelles sont les différences et le fonctionnement de `apt-get upgrade`, `apt upgrade`, `apt-get dist-upgrade` et `do-release-upgrade` ?

**Réponse du PDF :**

- **`apt-get upgrade` :** installe les versions les plus récentes des paquets présents sur le système à partir des sources de `/etc/apt/sources.list`. Les nouvelles versions sont récupérées et mises à niveau. Aucun paquet déjà installé n’est supprimé ; aucun paquet non installé n’est récupéré ou installé.
- **`apt upgrade` :** met à jour les paquets installés sans en supprimer. Installe de nouveaux paquets pour satisfaire les dépendances si nécessaire.
- **`apt-get dist-upgrade` :** ajoute à `upgrade` une gestion intelligente des changements de dépendances et une résolution des conflits. Si nécessaire, les paquets les plus importants sont mis à niveau aux dépens des moins importants. Les sources sont listées dans `/etc/apt/sources.list`.
- **`do-release-upgrade` :** démarre la mise à niveau du système d’exploitation ; met Ubuntu à niveau vers une nouvelle version.

## Exercice 1 — Programmation de processus — 1,5 point — pages 4 à 6

Concernant le programme suivant :

a) Quelles lignes affiche-t-il ? **0,75 point.**

b) Quels sont les ordres possibles de ces lignes ? **0,75 point.**

L’opérateur `!` de la ligne 31 du PDF est la négation : pour `pid = 0`, `!pid = 1` ; pour `pid != 0`, `!pid = 0`.

**Programme transcrit depuis l’image de la page 5 :**

```c
#include <unistd.h>     /* Symbolic Constants */
#include <sys/types.h>  /* Primitive System Data Types */
#include <errno.h>      /* Errors */
#include <stdio.h>      /* Input/Output */
#include <sys/wait.h>   /* Wait for Process Termination */
#include <stdlib.h>     /* General Utilities */
#include <string.h>     /* String utilities */

pid_t Fork(void)
{
    pid_t pid;

    pid = fork();

    if (pid < 0) {
        printf("Fork error");
        exit(-1);
    }

    return pid;
}

int main()
{
    int status;
    pid_t pid;

    printf("Hello\n");
    pid = Fork();
    printf("%d\n", !pid);
    if (pid != 0) {
        if (wait(&status) > 0) {
            if (WIFEXITED(status) != 0)
                printf("%d\n", WEXITSTATUS(status));
        }
    }
    printf("Bye\n");
    exit(2);
}
```

### Réponse du PDF

Deux sorties sont proposées. Si le père affiche sa sortie avant le fils :

```text
Hello
0
1
Bye
2
Bye
```

Si le fils affiche sa sortie avant le père :

```text
Hello
1
0
Bye
2
Bye
```

### Complément de vérification — cas omis par le corrigé

Dans le modèle d’affichage ligne par ligne utilisé par le sujet, le fils peut afficher `1`, puis son `Bye`, avant que le père n’affiche `0`. La sortie suivante est donc également possible :

```text
Hello
1
Bye
0
2
Bye
```

Le père attend la terminaison du fils avant d’afficher le code de sortie `2`, puis son propre `Bye`. Les exemples du PDF supposent que `Hello` a été affiché avant `fork` ; le comportement des tampons en cas de redirection n’est pas étudié dans le sujet.

## Exercice 2 — Système de fichiers — 1,5 point — page 6

Les blocs de données d’un fichier sont accessibles à partir de son i-nœud, comme dans UNIX.

- Taille d’un bloc : 1 K, soit 1 024 octets.
- L’i-nœud de chaque fichier ou répertoire comporte 12 pointeurs directs, un pointeur indirect simple, un indirect double et un indirect triple.
- Un pointeur, ou numéro de bloc, occupe 4 octets.

### a) Taille maximale d’un fichier — 0,75 point

**Réponse du PDF :**

$$12\times1\,\mathrm{ko}+256\times1\,\mathrm{ko}+256^2\times1\,\mathrm{ko}+256^3\times1\,\mathrm{ko}.$$

**Calcul explicité :** un bloc de pointeurs contient $1024/4=256$ adresses. La capacité est donc

$$T_{\max}=(12+256+256^2+256^3)\times1024=17\,247\,252\,480\ \text{octets}.$$

### b) Fichier de 100 000 octets — 0,75 point

Combien de blocs de données sont nécessaires au total sur disque ?

**Réponse du PDF :** « $100000/1024=97$ ou $98$ blocs ».

**Rectification :** $100000/1024=97{,}65625$ ; il faut arrondir au supérieur, soit **98 blocs de données**. Pour compter aussi les blocs d’adressage, les 12 premiers blocs sont directs et les 86 suivants nécessitent un bloc d’indirection simple : **99 blocs au total, hors stockage de l’i-nœud**.

## Exercice 3 — Ordonnancement — 3 points — pages 6 à 9

| Processus | Temps d’exécution | Temps d’arrivée |
| --- | ---: | ---: |
| P1 | 3 | 0 |
| P2 | 6 | 2 |
| P3 | 4 | 4 |
| P4 | 5 | 6 |
| P5 | 2 | 8 |

Pour FCFS (*First Come First Served*), RR (*Round Robin*, quantum 4), SJF (*Shortest Job First*, sans préemption) et SRT (*Shortest Remaining Time*) :

a) Dessiner l’exécution des processus : **0,25 point par technique**.

b) Calculer le temps de séjour de chacun, sa moyenne, le temps d’attente de chacun et sa moyenne : **0,50 point par technique**.

Le séjour est l’intervalle entre soumission et achèvement ; l’attente est le séjour moins le temps d’exécution. Les chronogrammes du PDF sont transcrits ci-dessous en intervalles $[\text{début},\text{fin}[$.

### FCFS — corrigé du PDF

```text
[0,3[ P1 → [3,9[ P2 → [9,13[ P3 → [13,18[ P4 → [18,20[ P5
```

| Processus | Séjour | Attente |
| --- | ---: | ---: |
| P1 | 3 | 0 |
| P2 | 7 | 1 |
| P3 | 9 | 5 |
| P4 | 12 | 7 |
| P5 | 12 | 10 |
| Moyenne | 8,6 | 4,6 |

### RR, quantum 4 — corrigé du PDF

```text
[0,3[ P1 → [3,7[ P2 → [7,11[ P3 → [11,15[ P4
→ [15,17[ P5 → [17,19[ P2 → [19,20[ P4
```

| Processus | Séjour | Attente |
| --- | ---: | ---: |
| P1 | 3 | 0 |
| P2 | 17 | 11 |
| P3 | 7 | 3 |
| P4 | 14 | 9 |
| P5 | 9 | 7 |
| Moyenne | 10 | 6 |

**Incohérence du corrigé.** Dans une file FIFO des processus prêts, P2 est réinséré à $t=7$, avant l’arrivée de P5 à $t=8$. Il doit donc repasser avant P5. Le chronogramme RR correspondant est :

```text
[0,3[ P1 → [3,7[ P2 → [7,11[ P3 → [11,15[ P4
→ [15,17[ P2 → [17,19[ P5 → [19,20[ P4
```

P2 a alors un séjour de 15 et une attente de 9 ; P5 a un séjour de 11 et une attente de 9. Les autres lignes et les moyennes, 10 et 6, restent identiques.

### SJF sans préemption — corrigé du PDF

```text
[0,3[ P1 → [3,9[ P2 → [9,11[ P5 → [11,15[ P3 → [15,20[ P4
```

| Processus | Séjour | Attente |
| --- | ---: | ---: |
| P1 | 3 | 0 |
| P2 | 7 | 1 |
| P3 | 11 | 7 |
| P4 | 14 | 9 |
| P5 | 3 | 1 |
| Moyenne | 7,6 | 3,6 |

### SRT — corrigé du PDF

```text
[0,3[ P1 → [3,4[ P2 → [4,8[ P3 → [8,10[ P5
→ [10,15[ P2 → [15,20[ P4
```

| Processus | Séjour | Attente |
| --- | ---: | ---: |
| P1 | 3 | 0 |
| P2 | 13 | 7 |
| P3 | 4 | 0 |
| P4 | 14 | 9 |
| P5 | 2 | 0 |
| Moyenne | 7,2 | 3,2 |

À $t=10$, P2 et P4 ont chacun 5 unités restantes ; le corrigé choisit P2.

## Exercice 4 — Mémoire virtuelle — 3 points — pages 9 et 10

Un système de mémoire virtuelle avec pagination utilise des pages de 8 KB. Son espace virtuel est de $2^{32}$ octets et sa mémoire physique de $2^{23}$ octets. Le support utilise KB et MB avec des puissances de 1024.

| Numéro de page | Cadre de page |
| --- | ---: |
| 0 | 1 |
| 1 | 7 |
| 2 | 9 |
| 3 | 14 |
| 4 | 8 |
| 5 | 3 |
| 6 | 25 |
| 7 | 16 |
| 8 | 23 |
| 9 | 78 |

### a) Format de l’adresse virtuelle — 1 point

Indiquer chaque champ et son nombre de bits.

**Corrigé :** $8\,\mathrm{KB}=2^{13}$ octets. Les 13 bits inférieurs codent l’offset, ou déplacement, et les $32-13=19$ bits supérieurs codent le numéro de page.

### b) Traduction d’adresse — 1 point

Adresse virtuelle :

```text
0000 0000 0000 0000 0110 0000 1000 1010
```

**Corrigé :** les 19 bits du numéro de page sont `0000 0000 0000 0000 011`, soit 3. La page 3 est dans le cadre 14, et $14=(1110)_2$.

Adresse physique affichée dans le PDF, complétée à gauche par des zéros sur 32 bits :

```text
0000 0000 0000 0001 1100 0000 1000 1010
```

**Vérification :** déplacement $=138$ ; adresse physique $=14\times8192+138=114826$. La mémoire physique de $2^{23}$ octets nécessite 23 bits d’adresse : 10 pour le cadre et 13 pour le déplacement. La même valeur sur ces 23 bits est :

```text
0000001110 | 0000010001010
```

### c) Espace virtuel occupé par ce processus — 0,5 point

**Corrigé :** la table contient 10 pages ; $10\times8\,\mathrm{KB}=80\,\mathrm{KB}$.

Ce résultat suppose que la table donnée décrit toutes les pages du processus ; il se distingue de la capacité d’adressage virtuelle totale de $2^{32}$ octets.

### d) Taille de la mémoire physique en MB — 0,5 point

**Corrigé :**

$$2^{23}\ \text{octets}=2^{13}\,\mathrm{KB}=2^3\,\mathrm{MB}=8\,\mathrm{MB}.$$
