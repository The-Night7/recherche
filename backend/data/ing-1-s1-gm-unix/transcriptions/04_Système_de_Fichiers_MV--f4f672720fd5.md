---
source: "ING 1/S1 GM /UNIX/CM/04_Système_de_Fichiers_MV.pdf"
pages: 55
transcription: texte, tableaux, commandes et schémas de principe transcrits et relus
transcription_date: 2026-10-18
verification: comparaison du texte natif et contrôle visuel des cinquante-cinq pages du PDF ; les états successifs des animations de virtualisation sont regroupés
---

# Système d'exploitation — Système de fichiers et machine virtuelle

Juan Angel Lorenzo del Castillo ; contributions de Stefan Bornhofen, Florent Devin et Taisa Guidini Gonçalves. Les 55 pages physiques comprennent les états intermédiaires de plusieurs animations : les pages numérotées 45 dans le diaporama sont quatre états successifs, tous décrits ici.

## Pages 1–4 — système de gestion des fichiers

La page 1 est la couverture. Le plan (page 2) couvre système de fichiers, mise à jour et virtualisation. La page 3 est un intercalaire attribuant une partie du cours à Stefan Bornhofen.

Un système de gestion de fichiers (SGF) est une structure de données qui organise les informations en fichiers sur mémoires secondaires. Il est présenté comme la partie la plus visible d'un SE : il fournit une interface de manipulation, organise les fichiers sur disque, gère l'espace libre et les usages multi-utilisateurs. Les systèmes cités sont Ext3, Ext4, XFS, Btrfs, FAT et NTFS (page 4).

## Pages 5–14 — fichiers, répertoires et i-nœuds

Un fichier est une unité logique persistante et non volatile, unité d'allocation des données. Le SE décide de sa structure, son nommage, son usage et sa protection, et fait de façon transparente le lien avec sa représentation binaire (page 5).

Les attributs donnés page 6 sont UID, GID, droits, dates, taille et type (fichier, répertoire, lien symbolique, périphérique). `ls -l` ou `stat fichier` les affichent ; `ls -i fichier` affiche l'i-nœud. Les droits Unix ont trois catégories, propriétaire, groupe et autres, modifiables par `chmod`.

Les opérations de fichier sont création, suppression, lecture/écriture et changement d'attribut. Sous Windows, le nom est un attribut ; sous Linux, il est associé à un lien, ce qui permet plusieurs noms vers le même fichier (page 7). La page 8 illustre les métadonnées et souligne que le nom n'appartient pas à l'i-nœud.

Un répertoire est lui-même un fichier, contenant une table qui relie noms et fichiers/répertoires. Il se crée, s'efface s'il est vide et reçoit des liens ; le retrait d'un fichier le retire de cette table. La racine Unix est unique et notée `/` (page 9).

Un i-nœud est une structure qui décrit un fichier ou répertoire. Chaque fichier possède un numéro d'i-nœud unique dans son système de fichiers, même s'il a plusieurs noms. Il contient attributs, propriétaire, droits et, dans le modèle du cours, 13 adresses de blocs : 10 directes, trois indirectes (page 10–11). Les noms sont dans les répertoires ; le cours réserve i-nœud 0 au démarrage, 1 aux blocs défectueux, 2 à la racine, et rappelle que `.` vise le répertoire courant et `..` le parent (page 12).

### Calcul page 13–14

Avec des blocs de 1 Ko et un pointeur de 32 bits (4 octets), un bloc d'index contient `1024 / 4 = 256` numéros de blocs. Le support dénombre 10 blocs directs, 256 indirects simples, `256²` doubles et `256³` triples ; il estime donc `(10 + 256 + 256² + 256³) × 1 Ko`, soit environ 16 Go comme taille maximale.

## Pages 15–22 — hiérarchie et gestionnaires

Unix fournit une hiérarchie unique, indépendante des particularités des disques, et des appels pour créer, ouvrir, lire, écrire, fermer ou supprimer. Monter un système de fichiers le greffe dans cette arborescence ; autres partitions, clés et CD peuvent être accessibles par des répertoires. Les périphériques sont aussi des fichiers de `/dev`, par exemple `/dev/pts/X`, `/dev/hda`, `/dev/sda`, `/dev/mouse`, `/dev/keyboard` (pages 15–17).

Les noms `/dev/xxyz` sont expliqués ainsi : `xx` est le type de bus (`hd`, `sd`, `fd`), `y` la lettre de périphérique et `z` le numéro de partition ; `hda1` est la première partition du premier disque IDE. L'UUID a 128 bits, se consulte avec `blkid`, et les montages permanents sont dans `/etc/fstab` (page 18).

| Répertoire | Rôle donné page 19 |
| --- | --- |
| `/bin`, `/sbin` | exécutables ; `/sbin` réservé à l'administrateur |
| `/etc`, `/var`, `/tmp` | configuration ; données variables (journaux) ; temporaires |
| `/dev`, `/boot`, `/lib` | périphériques ; démarrage ; bibliothèques dynamiques |
| `/home`, `/root` | répertoires personnels ; celui de l'administrateur |
| `/media`, `/mnt` | supports et dispositifs éjectables |
| `/usr` | logiciels utilisateur, avec `bin`, `local`, `src`, `share`, `include`, `lib` |

L'implantation Linux est représentée en couches : VFS, gestionnaires FAT/Ext4/NTFS/ISO9660/NFS/Btrfs, buffers, pilotes disque/CD/USB et réseau, pilotes de bus IDE/SCSI/USB, puis matériel (page 20). Le VFS crée, supprime, lit et écrit par chemins, contrôle les droits, localise périphérique et système de fichiers, puis délègue au gestionnaire adéquat (page 21). Ce dernier gère les blocs pour son format particulier (page 22).

## Pages 23–29 — formats et accès au stockage

FAT est décrit comme simple mais limité : racine à emplacement fixe, table d'allocation peu efficace, fragmentation, blocs de taille dépendant de la partition ; FAT12, 16 et 32 sont cités. NTFS est présenté comme peu documenté, avec gestion POSIX des droits, taille maximale égale à la partition et journalisation. Ext4, très courant sous Linux, contient une liste d'i-nœuds, distingue fichiers normaux, répertoires, spéciaux de `/dev` et liens symboliques, est sensible à la casse, cache les noms commençant par `.`, est journalisé. Btrfs offre *copy on write*, sous-volumes, instantanés et compression (pages 23–24).

Le stockage séquentiel lit les octets dans l'ordre depuis le début et s'emploie encore pour les sauvegardes sur bande. L'accès aléatoire, permis par les disques, autorise un accès direct à un enregistrement, par exemple en base de données (page 25).

Un bloc est la plus petite unité physique manipulée ; un fichier est un ensemble de blocs que le système doit localiser par cylindre, piste et secteur. Le cours compare trois allocations :

| Allocation | Principe | Atouts et limites |
| --- | --- | --- |
| contiguë | blocs successifs | simple et très rapide ; taille difficile à faire grandir et fragmentation ; adaptée au CD-ROM |
| chaînée | chaque bloc pointe vers le suivant | croissance facile ; recherche lourde, accès séquentiel |
| indexée | tous les pointeurs dans un bloc d'index | croissance et accès aléatoire ; index coûteux et taille limitée |

## Pages 30–39 — disques, démarrage et `systemd`

Un disque possède un schéma de partitionnement et des partitions. Une partition est une portion de disque réel utilisée comme disque logique, contenant un système de fichiers, un type, un début et une taille. Le document emploie aussi « superbloc » dans cette description. Le formatage inspecte les secteurs, efface les données, crée le répertoire racine et le superbloc ; il sert à installer plusieurs systèmes, sauvegarder et séparer logiquement système, utilisateurs et journaux (pages 30–31).

| Terme | Définition du support |
| --- | --- |
| BIOS | firmware de carte mère, premier logiciel lancé, initialise le matériel |
| UEFI | remplace le BIOS, emploie GPT et renforce la sécurité |
| MBR | premier secteur : table de partitions et code d'amorçage, associé au BIOS |
| GPT | table de partitions associée à l'UEFI et remplaçant MBR |

Le schéma MBR admet quatre partitions principales et 2,1 To ; une partition étendue contient des partitions logiques sans système de fichiers propre. GPT est associé à UEFI, peut fonctionner avec Linux en BIOS traditionnel, autorise 128 partitions selon Microsoft, jusqu'à 256 To par partition et une taille théorique de 9,4 zettaoctets pour le disque (pages 32–34).

Au démarrage BIOS, le MBR du secteur 0 est lu, la table de partitions est en fin de MBR et une partition est marquée active (page 35). En MBR : BIOS → *first-stage boot loader* → partition active et son VBR/boot block → chargeur de second niveau (ex. GRUB2) → SE. En UEFI, le chargeur `.efi` de la partition EFI GPT est chargé directement (page 36).

Le scénario SysVinit (page 37) : décompresser le noyau ; initialiser périphériques et pilotes ; monter la racine en lecture seule ; lancer `init` PID 1 ; lire `/etc/inittab` ; exécuter `/etc/rc<n>.d/` ; passer en multi-utilisateur ; démarrer `getty` ; remonter en lecture-écriture ; lancer les démons et construire l'arbre de processus.

`systemd` remplace les scripts de lancement par des fichiers de configuration (page 38), centralise les briques de base, applique les cgroups, améliore surveillance et journal, peut relancer un service arrêté, sépare services de distribution et d'administrateur, et simplifie l'empaquetage (page 39).

## Pages 40–43 — mises à jour Debian/Ubuntu

Les pages 40–41 sont plan et intercalaire. La page 42 distingue :

- `apt-get update` : resynchronise les listes de paquets depuis `/etc/apt/sources.list`, à exécuter avant les autres commandes ;
- `apt-get upgrade` : met à niveau les paquets installés sans supprimer ni installer d'autres paquets ;
- `apt-get dist-upgrade` : résout les changements de dépendances, éventuellement au détriment de paquets moins importants ; le support le déconseille sur les machines CY Tech.

## Pages 44–55 — virtualisation

Les pages 43–44 ouvrent la partie. Les pages 45 à 48 sont les états successifs d'un même schéma : infrastructure matérielle, système invité (*guest OS*), environnement virtualisé, puis définition. La virtualisation crée une version virtuelle d'une plateforme matérielle, d'un SE, d'un stockage ou de ressources réseau.

Un hyperviseur crée et exécute les machines virtuelles ; il permet à l'hôte d'accueillir plusieurs VM clientes en partageant mémoire et calcul (page 49). Les approches citées sont traduction binaire, paravirtualisation et virtualisation matérielle (page 50). La page 51 représente les anneaux de privilèges x86 et la page 52 introduit la virtualisation matérielle par un schéma.

Un hyperviseur de type 1 (*bare metal*, natif) s'exécute directement sur le matériel pour gérer les SE invités (page 54). Un hyperviseur de type 2 est hébergé par un SE déjà installé, notamment pour créer des VM (page 55).

## Notes sur les écarts du support

- Le compte des adresses d'i-nœud (10 directes, 3 indirectes) est un modèle pédagogique, pas la structure générale de tous les systèmes de fichiers modernes.
- Sous Linux courant, `/bin`, `/sbin` et d'autres chemins peuvent être des liens vers `/usr`; la vue de la page 19 est une arborescence de référence historique.
- `apt-get` est conservé parce qu'il figure dans le support. Les interfaces actuelles recommandent généralement `apt` pour un usage interactif ; une mise à niveau majeure doit être évaluée avant exécution.
- Le PDF écrit « BIOS » à plusieurs endroits là où l'usage courant emploie aussi le féminin « la BIOS »; ce choix n'altère pas le contenu technique.
