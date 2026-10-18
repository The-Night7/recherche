---
source: "ING 1/S1 GM /UNIX/CM/01_IntroSE_IntroProcessus.pdf"
pages: 65
transcription: texte, programmes, tableaux et schémas de principe transcrits et relus
transcription_date: 2026-10-18
verification: comparaison du texte natif et contrôle visuel des soixante-cinq pages du PDF ; les pages d'intercalaire, les figures et les animations sont signalées
---

# Système d'exploitation — Introduction aux SE et programmation de processus

Juan Angel Lorenzo del Castillo ; contributions de Thierry Garcia, Florent Devin et Taisa Guidini Gonçalves. Le cours suit le plan : introduction, système d'exploitation, rappel matériel, éléments de base, appels système et interruptions, structures de SE, puis processus. Les renvois citent les **65 pages physiques** du PDF.

## Pages 1–8 — introduction

La page 1 est la couverture. La page 2 annonce les sept parties du cours. La page 3 est un intercalaire « Introduction ». La page 4 place le système d'exploitation entre matériel, logiciel et utilisateur, et demande comment un programme est transposé au plan physique et comment le matériel est protégé des programmes.

Les objectifs (page 5) sont de connaître structure, gestion des ressources matérielles, administration des programmes et interface utilisateur, du point de vue de l'utilisateur, de l'administrateur et du concepteur, avec un accent Linux/Unix. Les thèmes (page 6) sont : processus et cycle de vie ; ordonnanceur ; mémoire ; fichiers ; démarrage ; installation et configuration ; Docker. La bibliographie (page 7) montre la couverture de *Modern Operating Systems*, quatrième édition, d'Andrew S. Tanenbaum et Herbert Bos. L'évaluation (page 8) est un examen papier de deux heures, calculatrice autorisée, avec annales sur Teams.

## Pages 9–16 — rôle du système d'exploitation

Les pages 9 et 10 ouvrent la partie. L'ordinateur moderne comprend processeur(s), mémoires, disques, clavier, souris, écrans, réseau et autres E/S (page 11). Les composants sont répartis entre matériel, programmes applicatifs utilisateur et programmes système : les seconds s'exécutent en mode utilisateur avec un accès restreint, les premiers en mode noyau/système/superviseur avec accès aux instructions et au matériel (page 12).

Administrer les ressources, accéder aux périphériques ou à la mémoire physique et traiter les erreurs sont les problèmes que le SE résout. Il est la couche qui donne aux applications un modèle plus simple de la machine et gère son usage (page 13).

Ses deux fonctions explicitées sont :

- **présentation** : fournir des abstractions aux programmes ; l'utilisateur interagit avec un shell ou une interface graphique ;
- **gestion** : connaître le matériel, distribuer et arbitrer les ressources, gérer E/S, processus et mémoire, partager le temps processeur et l'espace mémoire.

Le « zoo » des SE (page 16) énumère mainframes, serveurs, systèmes multiprocesseurs, ordinateurs personnels, mobiles, systèmes embarqués, nœuds-capteurs et systèmes temps réel, avec notamment Unix/Linux, Windows, Android, iOS, QNX, VxWorks, TinyOS, RTLinux et eCos.

## Pages 17–27 — rappel du matériel

Les pages 17 à 19 ouvrent la partie ; les pages 18 et 19 sont des intercalaires sans contenu pédagogique supplémentaire. Le CPU est le « cerveau » : il exécute les instructions assembleur des programmes placés en mémoire, possède un jeu d'instructions dépendant de sa famille (exemple Intel x86 contre ARM) et des registres rapides (page 20).

| Registre | Rôle donné page 21 |
| --- | --- |
| PC, compteur ordinal | adresse de la prochaine instruction à charger |
| Pointeur de pile | adresse supérieure de la pile mémoire |
| PSW (*Program Status Word*) | PC, masquage des interruptions, mode utilisateur/noyau, priorités et autres informations propres au processeur |

La page 22 représente l'architecture processeur–mémoire. La page 23 distingue les systèmes multi-threads (plusieurs fils d'exécution partageant les ressources d'un cœur, vus comme plusieurs CPU par le SE) et multi-cœurs (plusieurs cœurs physiques ; cache L2 partagé ou intégré ; Xeon Phi et GPU cités).

La mémoire centrale contient instructions et données à exécuter. Avec disque et cache, elle forme une hiérarchie qui tente de concilier rapidité, capacité et coût (page 24). La mémoire secondaire comprend disques magnétiques à plateaux et SSD à mémoire flash (page 25).

Un périphérique E/S comprend un contrôleur et le dispositif. Chaque contrôleur requiert un pilote, en mode noyau, chargé dynamiquement sous Linux ou après démarrage sous Windows. Trois modèles de lecture sont indiqués : interrogation continue (*polling*), interruption du contrôleur, ou DMA (*Direct Memory Access*) (page 26). La page 27 montre les bus comme voies partagées de communication entre composants, avec SCSI en exemple.

## Pages 28–35 — éléments de base d'un SE

La page 28 rappelle le plan, la 29 est un intercalaire, et la 30 énumère processus, système de fichiers, E/S, mémoire, protection et interprète de commandes.

Un processus est un programme en cours d'exécution : programme, données, pile, PC, pointeur de pile et état des registres constituent son information nécessaire. La multiprogrammation impose de sauvegarder cette information pour arrêter et reprendre un processus, de tenir une table des processus et de gérer les priorités (page 31). La page 32 avertit qu'un processus est dynamique, contrairement au code source statique.

Un programme s'exécute en mémoire principale avec d'autres programmes ; une protection évite leurs interférences. La mémoire virtuelle répartit les adresses d'un processus entre mémoire et disque et découple son espace d'adressage de la mémoire physique (page 33).

Pour les fichiers, le cours illustre les permissions Unix par trois champs `rwx` — propriétaire, groupe et autres — et convertit `rwx r-x --x` en `111 101 001₂`, donc `751₈` (page 34). Le shell ne fait pas partie du SE ; `sh`, `csh`, `bash`, `zsh`, `ksh` sont des interprètes qui exécutent des commandes au moyen d'appels système (page 35).

## Pages 36–49 — appels système et interruptions

Les pages 36–37 ouvrent la partie. Un appel système est l'interface d'instructions étendues entre programmes utilisateurs et SE. La lecture est donnée comme `count = read(fd, buffer, nbytes);`. L'appel ressemble à l'appel d'une procédure mais entre dans le noyau via des bibliothèques, de façon transparente pour l'utilisateur (page 38).

Les actions citées sont `fork`, `wait`, `kill`, `sleep`, suspension/reprise via ordonnanceur et allocation dynamique `malloc`/`free` (page 39).

Une interruption permet au processeur de traiter un événement externe sans cesser normalement sa séquence : requête de périphérique, bouton ou capteur. La procédure associée est présentée comme une tâche à exécuter (page 40). Une entrée IRQ et un bit d'interruption sont testés avant l'instruction suivante ; un bit à 1 signale la demande (page 41).

Le déroulement (page 42) est :

1. terminer l'instruction courante et arrêter le processus ;
2. sauvegarder le contexte — registres matériels vers le PCB ;
3. exécuter la routine dépendant de l'interruption ;
4. restaurer le contexte.

Dans le schéma de la page 43, l'unité d'échange envoie `INTR`, la CPU accuse réception avec `INTA`, puis l'unité transmet le numéro IRQ. Celui-ci indexe le vecteur d'interruptions, qui associe chaque numéro à l'adresse de sa routine. `RESET IN` remet le compteur à zéro ; `RESET OUT` réinitialise les périphériques.

La page 44 distingue interruptions externes matérielles ou logicielles, et interruptions internes (erreurs telles que division par zéro, débordement ou adressage) conduisant à des *traps* pour passer du mode utilisateur au noyau. La page 45 décrit priorité, masquage temporaire — via un indicateur du PSW — et désarmement/réarmement.

Les quatre pages 46–49 construisent le schéma d'une interruption d'horloge. Un programme utilisateur contient notamment `open("fichier", "wr")`, `read(fd, j, 1)` puis `j = j / i`. Le diagramme sépare mode utilisateur et superviseur par une protection : `open()` provoque l'exécution d'un appel système ; la division peut déclencher une *trappe* pour erreur irrécouvrable et arrêt du programme ; enfin un signal d'horloge mène au traitement d'interruption avant le retour au programme.

## Pages 50–56 — structures des SE

Après le plan et l'intercalaire (pages 50–51), trois catégories sont citées : monolithique, micro-noyau et autres (page 52).

Dans un SE monolithique, toutes les procédures sont compilées dans un grand programme en mode noyau ; elles peuvent s'appeler librement. Le cours relève qu'il est difficile à comprendre et qu'une procédure qui s'écrase peut arrêter l'ensemble, mais le décrit comme la structure la plus commune (page 53).

L'appel monolithique (page 54) récupère les paramètres sur la pile, les place dans un registre, bascule en mode noyau, exécute la procédure correspondante, puis revient en mode utilisateur. Modules dynamiques, bibliothèques partagées Unix et DLL Windows sont cités.

Le micro-noyau réduit le noyau aux procédures essentielles et déplace les services dans des programmes externes de l'espace utilisateur, pour réduire taille et surface d'erreur (page 55). Les autres architectures (page 56) sont systèmes en couches, client–serveur par passage de messages, machines virtuelles et exokernels, où chaque utilisateur reçoit un sous-ensemble de ressources et le processus superviseur les répartit.

## Pages 57–65 — programmation de processus

Les pages 57–58 ouvrent cette dernière partie. Sous Unix/Linux, les informations mises en avant sont PID, PPID, propriétaire et priorité. Lorsqu'un processus crée un enfant, le parent et l'enfant restent liés : chaque enfant connaît son PPID, peut créer ses propres enfants, possède un seul parent et zéro ou plusieurs fils (page 59).

### `fork()` — page 60

`pid_t fork(void)` crée un fils par clonage. Selon la diapositive, le fils partage le segment texte, reçoit une copie des données, hérite du terminal de contrôle et d'une copie des descripteurs ouverts, mais non du temps d'exécution, de la priorité ni des signaux en attente. Le retour vaut zéro dans le fils, le PID du fils dans le père, ou `-1` à l'échec. Père et descendants forment un arbre/groupe de processus.

La page 61 est une illustration de l'arbre père–fils. La page 62 propose l'exemple suivant, ici rétabli malgré les espaces introduits par l'extraction :

```c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void) {
    pid_t p = fork();
    switch (p) {
    case 0:
        printf("Je suis le fils : mon PID est %d et mon PPID est %d\n",
               getpid(), getppid());
        break;
    case -1:
        perror("Erreur de creation de processus avec fork");
        break;
    default:
        printf("Je suis le pere : mon PID est %d et mon PPID est %d\n",
               getpid(), getppid());
    }
    return 0;
}
```

La compilation affichée est `gcc -o useoffork useoffork.c`.

### Terminaison et attente — pages 63–64

`exit(int etat)` termine normalement un processus. Le cours dit que `etat`, un octet de 0 à 255, revient au père dans un `int` ; zéro signifie succès et toute autre valeur un code d'erreur. `EXIT_SUCCESS` et `EXIT_FAILURE` sont cités. Les prototypes sont :

```c
pid_t wait(int *status);
pid_t waitpid(pid_t pid, int *status, int options);
```

`wait` suspend le père jusqu'à la fin d'un fils, renvoie le PID de celui-ci ou `-1` s'il n'y a plus de fils. `waitpid` cible un PID donné. Le cours indique qu'à l'achèvement du père, `init` (PID 1) prend les fils en charge. La page 64 est une capture d'exemple, compilé par `gcc -o useofwait useofwait.c`. La page 65 fournit le code Teams `f4kcv83`.

## Notes sur les écarts du support

- Le terme « appels système » est utilisé page 40 pour les procédures associées à des événements externes ; une interruption matérielle et un appel système sont cependant deux mécanismes distincts, même s'ils entraînent un passage en noyau.
- La page 44 associe les *traps* à des erreurs « normalement irrécouvrables » ; certaines exceptions et certains appels système sont au contraire récupérables.
- Le support écrit `exit(int etat))` avec une parenthèse fermante de trop et « fils de fils » dans la description de `wait`.
- Après `fork`, les détails de partage et d'héritage dépendent du noyau. La mémoire est en pratique souvent copiée à l'écriture ; l'état d'attente ne s'interprète pas directement comme une valeur brute de `status`.
