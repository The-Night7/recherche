---
source: "ING 1/S1 GM /UNIX/Commande Unix TD & Solutions/td1-correction.pdf"
pages: 11
transcription: texte, questions, réponses et commandes transcrits et relus
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle de toutes les pages du PDF
---

# TP1 — Les commandes de base, corrigé

Les réponses sont celles du support. Le signe typographique ∼ des chemins est rendu par le tilde shell `~`. Les écarts et compléments de transcription sont indiqués séparément.

## Page 1

TP1 - Les commandes de bases Inès de Courchelle 2021 - 2022

Consignes : Durant ce TD l’utilisation de la souris, Touchpad et/ou Trackpoint sont strictement interdit. Seul le clavier est autorisé.

Objectifs : Ce TD a pour objectif de connaı̂tre le fonctionnement et l’utilisation des systèmes Unix. Le premier concept abordé est le changement du mot de passe. Les caractèristiques du systèmes de fichier UNIX sont étudiées via les fonctionnalités de types : ajout, suppression, modification, affichage et déplacement dans l’arborescence. Une introduction à l’éditeur de texte VI est illustré à travers des exemples.

### 1 Le mot de passe

Les caractèristiques de chaque utilisateur sont enregistrées dans un fichier /etc/passwd qui est géré par l’administrateur système, mais que vous pouvez consulter. Dans ce fichier, vous trouverez pour chaque utilisateur, le numéro de son groupe, son nom, son prénom, et le shell ou programme à lancer. Le mot de passe est votre protection contre les intrusions. C’est la seul façon de protéger vos données.

### 1.1 Trouver un bon mot de passe

Voici quelques conseils qui vous permettront de trouver un mot de passe le plus sûr possible. Ce qu’il faut faire !

- appliquer des majuscules et des minuscules

- utiliser des chiffres et des caractères spéciaux

- adopter une longueur de 7 à 8 caractères minimum

- concaténer des mots pour en créer un autre Ce qu’il NE faut PAS faire !

- mettre un mot de passe que l’on peut trouver dans un dictionnaire

- avoir recours à un nom de famille (surtout si la famille est célèbre et qu’on peut trouver le nom dans un dictionnaire), un nom de lieu, le prénom de votre chat ...

- employer un mot trop court

## Page 2

### 1.2 Changer le mot de passe

Pour changer son mot de passe, il faut utiliser la commande passwd. Le programme demande alors l’ancien mot de passe puis deux fois le nouveau. Si le déroulement est normal, le nouveau mot de passe sera utilisé pour une prochaine session.

### 2 Editeur de texte VI

### 2.1 Qu’est ce que VI ?

VI est un éditeur de texte, directement disponible dans le terminal. Il a été développé à l’Université de Berkeley en Californie. Il possède trois modes de travail :

- Mode commande : Toutes les entrées claviers sont interprétées comme des commandes

- Mode insertion : Toutes les entrées claviers sont du textes écrits dans le fichier

- Mode étendu : Toutes les entrées claviers sont interprétées comme des commandes propres à l’éditeur

**Figure 1 — Les modes VI.** Le mode commande passe au mode insertion par `i`. Le retour se fait par Échap (*Escape*). Le mode commande passe au mode étendu par `:` ; une flèche de retour relie aussi le mode étendu au mode commande.

### 2.2 Quelques que commandes utiles (attention mode commande

activé)

- Sauvegarder : w

- Sauvegarder et quitter wq

- Sauvegarder, quitter et sans demande de confirmation wq!

- Rechercher dans le fichier / suivi du mot rechercher, n permet d’aller directement à l’occurence suivante.

## Page 3

### 3 Pour bien commencer

- Ouvrir un terminal = ctrl + alt + t

- Afficher le contenu d’un répertoire = ls

- Savoir où on se trouve dans l’arborescence = pwd

- Revenir à son répertoire courant = cd

- Aller au répertoire précédent = cd ..

- Connaı̂tre le principe d’une commande et ses options associées = man nom commande Pour parcourir le manuel (man) :

- q = permet de sortir du manuel

- man -k search = liste tous les manuels liés à ”search”

- man man = ouvre le manuel de man

- man ls puis = recherche un mot contenu dans le manuel

### 4 Exercices

A l’aide de la commande mkdir créer un répertoire à votre racine appelé CommandesUnix. Il ne doit pas y avoir d’espace dans le titre du répertoire.

### 4.1 Naviguer dans le système de fichier

1. Aller dans le répertoire bin et afficher son contenu

**Réponse du support :**

```text
cd /bin/
```

2. Revener dans votre home-directory. Réaliser les 3 solutions possibles.

**Réponse du support :**

```text
cd /home/eisti/
cd ~
cd
```

## Page 4

### 4.2 Mettre à jour sa machine (Sur vos machines perso uniquement)

1. A votre avis, çà sert à quoi de mettre à jour son système d’exploitation UNIX ?

**Réponse du support :**

Même si nous ne sommes pas sous windows, il existe cependant des failles de sécurité. Il est donc important de mettre à jour régulièrement son système. De plus, l’ensemble des logiciels, tel que firefox, propose des mises à jour réguliéres pour la sécurité, les dernières technologies etc. Il est donc important de mettre son ordinateur régulièrement à jour.

2. Afficher le manuel de la commande apt.

**Réponse du support :**

```text
man apt
```

3. La mise à jour se fait en deux étapes :

- resynchroniser un fichier repertoriant les paquets disponibles et sa source etc/apt/sources.list : update.

- Instalation des paquets sur le système : upgrade Réaliser cette mise à jour à l’aide de la commande apt. Que remarquez vous ?

**Réponse du support :**

il faut être en super utilisateur pour l’utiliser.

```text
sudo apt update
sudo apt upgrade
```

Attention : n’éteignez surtout pas votre ordinateur, si la mise à jour n’est pas terminée.

4. De plus, la commande apt permet d’installer des paquets (application, logiciels ...). A l’aide de la commande apt, rechercher l’existance d’un paquet appelé sl

**Réponse du support :**

```text
apt search sl
```

5. Installer le paquet sl

**Réponse du support :**

```text
sudo apt install sl
```

6. (Bonus) Lancer la commande sl dans le terminal. Que remarquez vous ?

## Page 5

### 4.3 Ecrire et lire dans un fichier

1. Créer un fichier mesMusiques. Attention, le nom du fichier ne doit pas contenir d’espace. Insérer une ou deux phrases en utilisant l’éditeur de texte vi.

**Réponse du support :**

```text
touch mesMusiques
vi mesMusiques Passez en mode insertion (touche i)
```

”Un grand pouvoir implique de grande responsabilité” Passez en mode commandes (touche esc)

```text
:wq !
```

2. Visualiser le contenu de mesMusiques dans le terminal, sans utiliser VI.

**Réponse du support :**

```text
cat mesMusiques
```

3. Quelle est la taille du fichier ? mesMusiques

**Réponse du support :**

```text
du -h mesMusiques
```

### 4.4 Copier/Coller

1. Faire une copie de mesMusiques appelée myMusic

**Réponse du support :**

```text
cp mesMusiques myMusic
```

2. Comparer leur taille

**Réponse du support :**

```text
du -h mesMusiques myMusic
```

3. Renommer myMusic en mySong

**Réponse du support :**

```text
mv myMusic mySong
```

## Page 6

4. Quelle différence y a-t-il entre mv myMusic mySong et cp myMusic mySong

**Réponse du support :**

La première commande renomme le fichier myMusic en mySong, et le fichier myMusic n’existe plus. La deuxième commande permet de copier et renommer le fichier myMusic en mySong, et le fichier myMusic existe toujours.

### 4.5 Créer des répertoires

1. Créer un répertoire myFiles

**Réponse du support :**

```text
mkdir myFiles
```

2. Déplacer mySong dans myFiles et renommer mySong en song2 (en une seule commande).

**Réponse du support :**

```text
mv mySong myFiles/song2
```

3. Créer deux sous répertoires dans myFiles :

- Albums/favorites

- Artistes

**Réponse du support :**

```text
mkdir -p myFiles/Albums/favorites ; mkdir myFiles/Artistes
```

4. Afficher le contenu du répertoire de manière détaillée, en affichant même les fichiers cachés myFiles

**Réponse du support :**

```text
ls -la myFiles
```

## Page 7

### 4.6 Détruire des fichiers ou des répertoires

1. Essayer de détruire le répertoire myFiles avec la commande rm. Que se passe-t-il ?

**Réponse du support :**

La commande rm indique qu’elle ne peut supprimer un répertoire.

2. Détruire tout ce que contient myFiles avec la commande rmdir. Que se passe-t-il ?

**Réponse du support :**

La commande rmdir indique qu’elle ne peut supprimer le répertoire car il n’est pas vide.

3. Détruire tout ce que contient myFiles avec la commande rm en mode récurcif.

**Réponse du support :**

```text
rm -rf myFiles
```

### 4.7 Lire le manuel

1. A quoi sert l’option -R de ls ?

**Réponse du support :**

Liste de manière récursive l’ensemble des répertoires et des sous-répertoires.

2. Dans quel ordre les fichiers et répertoires courant sont-ils classés par défaut ?

**Réponse du support :**

Les répertoires, par défaut, sont classés par ordre alphabétique.

3. Quelles sont les options qui peuvent servir à modifier ce critère de classement ?

**Réponse du support :**

Aller dans le man et recherchez le mot clé sort

## Page 8

4. Afficher le contenu de votre répertoire courant de telle sorte que les fichiers récemment utilisés apparaissent en premier.

**Réponse du support :**

```text
ls -lt ou ls -t1
```

5. Décriver le résultat de la commande ls -l

**Réponse du support :**

L’option l permet d’afficher une description détaillée de l’ensemble des fichiers dont les droits

6. Comment afficher les droits d’un répertoire donné ?

**Réponse du support :**

```text
ls -l < nom du repertoire >
```

7. Afficher le contenu de votre répertoire avec des signes distinctifs qui permettent d’identifier plus vite le type de fichiers (slash / pour les répertoires, @ pour les liens, etc.)

**Réponse du support :**

```text
ls -F
```

8. Un répertoire a les droits suivants : drwx-x-x. Je ne suis pas propriétaire, puis je afficher le contenu du répertoire ?

**Réponse du support :**

Ici, le propriétaire peut réaliser lecture / écriture / exécution, les membres de son groupe et les autres utilisateurs ne peuvent réaliser que l’éxécution du répertoire.

9. Créer un répertoire Moi, et metter lui les droits suivants : drwxr-x-wx. Sont-ils des droits pertinants à mettre sur un répertoire ou un fichier ?

**Réponse du support :**

```text
mkdir Moi
chmod -R 753
```

Ces droits sont peu pertinants car on autorise les gens qui n’appartiennent pas à notre groupe à modifier et exécuter les fichiers.

## Page 9

### 4.8 Aller plus loin ...

1. Quel est le Shell utilisé sur votre ordinateur ?

**Réponse du support :**

```text
echo $SHELL
```

le shell est un interpreteur de commandes dont le fonctionnement permet d’afficher un prompt et analyser et exécuter une commande. Il peut de plus créer des processus.

2. Afficher la version du système que vous utilisez.

**Réponse du support :**

```text
uname -v
```

3. Donner le chemin absolu du fichier cat

**Réponse du support :**

```text
whereis cat ou which cat
```

4. A quoi çà sert le bashrc ?

**Réponse du support :**

Ce fichier est un fichier de configuration du shell. C’est un fichier caché, situé à la racine de votre home-directory

5. A quoi sert la commande history ?

**Réponse du support :**

Cette commande permet d’afficher dans le terminal l’ensemble des commandes déjà réalisées.

## Page 10

### 5 Et si je révisai !

1. Quels sont les deux types de chemin ? Donnez une courte définition.

**Réponse du support :**

Les chemins relatifs : Le chemin part directement du répertoire courant. Les chemins absolus : Le chemin part directement du répertoire racine.

2. A quoi sert la commande man ?

**Réponse du support :**

```text
man affiche le manuel de la plupart des commandes unix installées sur votre système.
```

3. Qu’est ce qu’un répertoire ?

**Réponse du support :**

Un répertoire en informatique est un dossier contenant une liste ou une description de fichiers. Les répertoire sont traités comme des fichiers.

4. Comment accède t-on à notre home-directory ? Donner les 3 solutions.

**Réponse du support :**

```text
cd /home/eisti/
cd ~
cd
```

5. Afficher le contenu du répertoire courant de telle sorte que les fichiers récemment modifiés apparaissent en premier

**Réponse du support :**

```text
ls -lt ou ls -t
```

## Page 11

6. Créer en une seule commande un répertoire Cours avec un sous-répertoire Unix

**Réponse du support :**

```text
mkdir -p Cours/Unix
```

7. Créer 4 fichiers à l’intérieur du sous répertoire Unix s’appelant TD1 - TD2 - TD3 - TD4

**Réponse du support :**

```text
touch Cours/Unix/TD1
touch Cours/Unix/TD2
touch Cours/Unix/TD3
touch Cours/Unix/TD4
```

8. Écrire le texte ”Para bailar” dans TD1 et le texte ”La Bamba” dans TD2.

**Réponse du support :**

```text
echo ”Para bailar” > Cours/Unix/TD1
echo ”La Bamba” > Cours/Unix/TD2
```

9. Supprimer le fichier TD1

**Réponse du support :**

```text
rm Cours/Unix/TD1
```

10. Renommer le fichier TD2 en Rictchie

**Réponse du support :**

```text
mv Cours/Unix/TD2 Cours/Unix/Ritchie
```

11. Copier le fichier ”Ritchie” dans votre home-directory.

**Réponse du support :**

```text
cp Cours/Unix/Ritchie .
```

## Notes de transcription

- Les recommandations de mots de passe, dont le minimum de 7 à 8 caractères, sont celles du support de 2021–2022.
- Page 2 : les commandes de sauvegarde `w`, `wq`, `wq!` s’utilisent après `:` dans Vi. Page 5, la source espace `:wq !` ; la forme habituelle est `:wq!`.
- Page 3 : `cd` sans argument revient au répertoire personnel, et `cd ..` au parent, malgré les formulations « répertoire courant » et « répertoire précédent ». La ligne « man ls puis » est incomplète dans la source ; la recherche dans le manuel s’ouvre avec `/`.
- Page 3, exercice 4.1.1 : la réponse ne contient que `cd /bin/`, sans commande d’affichage. Page 4, le bonus sur `sl` n’a pas de réponse imprimée.
- `du -h` indique l’occupation disque, qui n’est pas forcément la taille exacte du contenu du fichier en octets.
- Page 8 : `ls -t` trie par date de modification. Pour afficher les droits du répertoire lui-même, ajouter `-d` à `ls -l`. Les chevrons de `ls -l < nom du repertoire >` sont une notation de remplacement, pas des redirections à exécuter.
- Page 8 : `drwx-x-x` est une notation abrégée de `drwx--x--x` ; le groupe et les autres peuvent traverser le répertoire mais ne peuvent pas en lister les entrées sans droit de lecture. La commande `chmod -R 753` omet sa cible `Moi`.
- Page 9 : `$SHELL` désigne habituellement le shell de connexion configuré, pas nécessairement le processus shell actuellement exécuté.
- Page 11 : les guillemets typographiques du PDF sont conservés dans les deux `echo` ; pour servir de délimiteurs shell, ils doivent être remplacés par des guillemets ASCII. La commande `cp Cours/Unix/Ritchie .` copie dans le répertoire courant et ne cible le répertoire personnel que si l’on s’y trouve. L’énoncé écrit « Rictchie », le corrigé `Ritchie`.
