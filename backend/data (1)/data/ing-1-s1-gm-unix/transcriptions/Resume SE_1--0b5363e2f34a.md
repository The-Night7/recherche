---
source: "ING 1/S1 GM /UNIX/TD_TP_Sys.exploitation/Resume SE_1.pdf"
pages: 2
transcription: texte, identifiants et signatures de fonctions transcrits et relus
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle des deux pages du PDF
---

# Résumé 1 — Système d’exploitation

Introduction aux systèmes d’exploitation et programmation de processus.

## Appels système — page 1

Ensemble d’instructions étendues, spécifiques d’un système d’exploitation, constituant l’interface entre celui-ci et les programmes utilisateurs.

Exemples d’actions donnés par le support :

- Création d’un processus fils par un processus actif : `fork`.
- Attendre la fin d’un fils : `wait`.
- Destruction d’un processus : `kill`.
- Mise en attente, réveil d’un processus : `sleep`, `wait`.
- Suspension et reprise grâce à l’ordonnanceur de processus, *scheduler*.
- Demande de mémoire supplémentaire ou restitution de mémoire inutilisée : allocation dynamique, `malloc`, `free`.

## Informations sur les processus — page 1

Notion de père et de fils.

| Identifiant | Signification dans le support |
| --- | --- |
| `pid` | Identifiant unique du processus, PID |
| `ppid` | Identifiant du processus père |
| `uid` | Identifiant réel de l’utilisateur exécutant le processus |
| `euid` | Identifiant effectif de l’utilisateur, correspondant aux privilèges |
| `gid` | Identifiant réel du groupe de l’utilisateur exécutant le processus |
| `egid` | Identifiant effectif du groupe |

## Hiérarchie des processus — page 1

Lorsqu’un processus en crée un autre, père et fils restent associés. Chaque processus connaît le PPID de son parent. Un enfant peut lui-même créer plusieurs processus, formant une hiérarchie. Un processus a un seul parent et peut avoir aucun ou plusieurs fils.

## Création d’un processus — pages 1 et 2

Appel système `fork()` en C ou `os.fork()` en Python. La création se fait par clonage, comparé à une mitose : le père demande la création dynamique d’un fils en appelant `fork()`. Le fils s’exécute ensuite de façon concurrente avec le père.

```c
pid_t fork(void);
```

Le support décrit `pid_t` comme un type `long int` défini dans `<sys/types.h>`.

Propriétés attribuées au fils dans le support :

- Partage le segment de texte du père.
- Dispose d’une copie du segment de données.
- Hérite du terminal de contrôle.
- Hérite d’une copie des descripteurs de fichiers ouverts.
- N’hérite pas du temps d’exécution, ni de la priorité.
- N’hérite pas des signaux en suspens.

**Page 2 :** `fork()` retourne zéro au fils, le PID du fils au père, ou −1 en cas d’échec.

## Synchronisation — page 2

### Terminaison

La source écrit `exit (int etat))` : une parenthèse fermante y est en trop.

- Termine normalement un processus. Le support présente `etat` comme un octet, donc de 0 à 255, renvoyé au père dans une variable de type `int`.
- État zéro : succès ; état non nul : code d’erreur.
- Constantes de `<stdlib.h>` : `EXIT_SUCCESS`, `EXIT_FAILURE`.

### Attente

```c
pid_t wait(int *status);
pid_t waitpid(pid_t pid, int *status, int options);
```

- Suspend le processus jusqu’à la terminaison de l’un de ses fils. Le PDF répète « de fils » à la fin de cette phrase.
- À l’achèvement du père, les fils sont pris en charge par `init`, PID 1, selon le modèle présenté.
- `status` : valeur de `exit` ou autre, dans le cas d’un signal, selon la formulation du support.
- `wait` attend n’importe quel fils et renvoie son PID, ou −1 s’il n’y a pas ou plus de fils.
- `waitpid` permet d’attendre un processus particulier dont on connaît le PID.

### Identifiants

La source écrit `getpitd()` et `getppid()` pour obtenir l’identifiant du processus et celui de son père. `getpitd` est une coquille pour `getpid`.

## Précisions de transcription

Les affirmations ci-dessus sont celles du résumé. `malloc` et `free` sont des fonctions de bibliothèque, et `kill` envoie un signal qui ne termine pas nécessairement le processus. Le type sous-jacent de `pid_t` dépend de l’implémentation ; il ne faut pas supposer systématiquement `long int`. La priorité n’est pas généralement perdue lors de `fork`. Enfin, le statut d’attente est encodé : le code de sortie s’obtient avec `WEXITSTATUS(status)` après vérification de `WIFEXITED(status)` ; ce n’est pas directement la valeur entière brute écrite dans `status`.
