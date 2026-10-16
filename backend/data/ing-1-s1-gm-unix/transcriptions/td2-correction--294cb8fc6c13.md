---
source: "ING 1/S1 GM /UNIX/Commande Unix TD & Solutions/td2-correction.pdf"
pages: 9
transcription: texte, questions, réponses et commandes transcrits et relus
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle de toutes les pages du PDF
---

# TP2 — Les entrées et sorties, corrigé

Les réponses sont celles du support. Le signe typographique ∼ des chemins est rendu par le tilde shell `~`. Les écarts et compléments de transcription sont indiqués séparément.

## Page 1

TP2 - Les entrées et sorties Inès de Courchelle 2021 - 2022

Consignes : Durant ce TD l’utilisation de la souris, Touchpad et/ou Trackpoint sont strictement interdit. Seul le clavier est autorisé.

Objectifs : Ce TD a pour objectif de :

- connaître et de se familiariser avec les entrées/sorties standards ainsi que les redirections

- d’étudier les spécificités de la suppression de fichiers et de répertoires

- traiter la lecture et l’écriture dans des fichiers de données de types CSV

- d’utiliser les liens symboliques et les variables shell

- créer des alias pour gagner du temps Fichiers attachés à la séance : soccer.csv

### 1 Avant de commencer

### 1.1 Les entrées et les sorties

Chaque commande a :

- une entrée standard ← par défaut le clavier

- une sortie standard ← par défaut l’écran

- une sortie d’erreur standard ← par défaut l’écran Il y a donc la possibilité de rediriger les différentes entrées et sorties via les commandes de redirection.

- `<` : redirection de l’entrée standard

- `>` : redirection de la sortie standard

- `2 >` : redirection de la sortie erreur standard

- `>>` : concaténation et redirection de la sortie standard

- `2 >>` : concaténation et redirection de la sortie erreur standard

## Page 2

### 1.2 Les redirections

En Unix, tout est fichier. Il existe un fichier appelé "null", dont le chemin absolu est /dev/null/. Tout ce qui est copié dans ce fichier n’existe plus, il est perdu. Ce fichier permet donc de rediriger les erreurs d’une commande ou encore d’un script

### 2 Exercices

### 2.1 Les entrées et les sorties standard de commandes Unix

1. Quelles sont les entrées et les sorties standard de la commande cat ?

**Réponse du support :**

entrée : clavier sortie : écran

2. Dans votre répertoire de connexion (home-directory), créer un dossier TP2 dans un répertoire CommandesUnix

**Réponse du support :**

```text
mkdir -p CommandesUnix/TP2
```

3. Sans utiliser VI, créer un fichier vide appelé HarryPotter.txt

**Réponse du support :**

```text
touch HarryPotter.txt
```

4. Sans utiliser VI, ajouter le texte suivant à l’intérieur du fichier "Mais Harry ! Ce n est pas n importe quel balai, c est un Nimbus 2000." indices : il faut utiliser la redirection de la sortie standard vers un fichier

**Réponse du support :**

```text
echo "Mais Harry ! Ce n'est pas n'importe quel balai, c'est un Nimbus 2000." > HarryPotter.txt
```

5. En une seule commande et sans utiliser VI, ajouter le texte suivant à l’intérieur du fichier "Un éclair de feu".

**Réponse du support :**

```text
echo "Un éclair de feu" >> HarryPotter.txt
```

## Page 3

6. En une seule commande et sans utiliser VI, créer le fichier hoy contenant la date et l’heure du jour.

**Réponse du support :**

```text
date > hoy
```

### 2.2 Les destructions de répertoires et leurs spécificités

1. Créer un répertoire vide appelé Gryffondor

**Réponse du support :**

```text
mkdir Gryffondor
```

2. Supprimer le répertoire vide appelé Gryffondor

**Réponse du support :**

```text
rmdir Gryffondor
```

3. Supprimer le répertoire TP2 (qui n’est pas vide). Que remarquez vous ?

**Réponse du support :**

```text
rmdir CommandesUnix/TP2
```

4. Comment faut-il faire pour supprimer entièrement le répertoire TP2 ?

**Réponse du support :**

```text
rm -rf CommandesUnix/TP2
```

le -r le fait aller récursivement dans n’importe quel sous-répertoire qu’il trouve le -f indique que vous n’êtes pas invité à confirmer

### 2.3 La lecture et l’écriture dans des fichiers de données

1. Afficher la première ligne du fichier soccer.csv

**Réponse du support :**

```text
head -n1 soccer.csv
```

## Page 4

2. Afficher les 100 premières lignes du fichier soccer.csv

**Réponse du support :**

```text
head -n100 soccer.csv
```

3. Afficher le fichier 7 lignes par 7 lignes à partir de la ligne 5. indice : more

**Réponse du support :**

```text
more -7 +5 soccer.csv
```

4. Créer un fichier data.csv contenant les lignes 12 à 14 (inclus) et 33 à 36 (inclus)

```text
du fichier soccer.csv, en utilisant uniquement les commandes head, tail, cat et la
```

redirection de la sortie standard).

**Réponse du support :**

```text
head -14 soccer.csv | tail -3 > data.csv
head -36 soccer.csv | tail -4 >> data.csv
```

5. Visualiser le fichier soccer.csv à l’aide de la commande cat. Puis le visualiser à l’aide de la commande more. Quelles sont les différences ?

**Réponse du support :**

```text
cat soccer.csv
more soccer.csv
```

La commande more affiche page par page, ce qui n’est pas le cas avec cat. De plus, la commande more permet de rechercher des motifs, et beaucoup d’autres choses.

6. Compter le nombre de lignes et de mots du fichier soccer.csv

**Réponse du support :**

```text
wc -lw soccer.csv
```

## Page 5

### 2.4 Les liens symboliques

Les liens symboliques permettent de donner plusieurs noms à un même fichier et de faire des économies de places.

1. Créer un répertoire tmp/ dans votre home-directory, et déplacer le fichier soccer.csv (existant dans votre home-directory) vers le répertoire tmp/.

**Réponse du support :**

```text
mkdir tmp
mv soccer.csv tmp/
```

2. Copier le fichier soccer.csv à la racine de votre compte et renommer le en mySoccer.csv (en une seule commande).

**Réponse du support :**

```text
cp tmp/soccer.csv ~/mySoccer.csv
```

3. Vérifier que le fichier s’y trouve bien.

**Réponse du support :**

```text
ls ~
```

4. Créer un lien symbolique de nom lienMySoccer sur le fichier mySoccer.csv.

**Réponse du support :**

```text
ln -s mySoccer.csv lienMySoccer
```

5. Lister le contenu du répertoire courant en affichant tous les détails des fichiers.

**Réponse du support :**

```text
ls -l
```

6. Supprimer le fichier mySoccer.csv se trouvant à la racine de votre répertoire de connexion (home-directory).

**Réponse du support :**

```text
rm mySoccer.csv
```

## Page 6

7. Lister le contenu de votre répertoire de connexion (home-directory). Que remarquez vous ?

**Réponse du support :**

```text
ls ~
```

le lien symbolique lienMySoccer existe toujours mais est brisé

### 2.5 Alias et fichier de configuration

1. Entrer le code suivant dans un terminal : alias cd=ls. Utiliser la commande cd. Que remarquez vous ?

**Réponse du support :**

Vous constatez que maintenant la commande cd se comporte comme la commande ls.

2. A votre avis à quoi sert la commande alias ?

**Réponse du support :**

La commande alias nous permet de surcharger une commande et/ou de donner un surnom à une longue commande utilisée de manière régulière.

3. Supprimer l’alias alias cd=ls

**Réponse du support :**

```text
unalias cd
```

4. Que fait la commande alias seule ?

**Réponse du support :**

elle affiche l’ensemble des alias déjà définis.

## Page 7

5. Lorsque le terminal est fermé l’ensemble des alias définis pendant la durée d’ouverture

```text
du terminal ne sont pas enregistré. Pour cela plusieurs solutions sont envisageable.
```

Afficher le contenu du fichier appelé .bashrc (attention il y a bien un point devant ce fichier), il se situe à la racine de votre home-directory. Utiliser vi, emacs ou tout simplement la commande cat. Le fichier .bashrc est un fichier de configuration lu à chaque démarrage d’un terminal. C’est donc l’endroit où vous pouvez rajouter des alias. Ajouter l’alias alias ls=ls -l suivant dans le .bashrc. Fermer le fichier et lancer la commande dans le terminal. Que remarquez vous ?

**Réponse du support :**

```text
cat .bashrc
```

ajouter la ligne de code suivante dans le fichier : alias ls=ls -l ecrire la commande suivante dans le terminal : ls l’alias rajouté n’est pas pris en compte. Pour cela, il faut fermer le terminal en cours et l’ouvrir de nouveau

6. Pour ne pas avoir à relancer le terminal vous pouvez remmettre à jour le fichier .bashrc depuis le terminal en utilisant la commande source.

**Réponse du support :**

```text
source ~/.bashrc
```

### 2.6 Les pipes et les filtres

Un pipe est un moyen de communication entre deux processus. En Unix, il nous permet de connecter le flot de sortie d’une commande au flot d’entrée d’une autre. Ainsi on peut enchaîner plusieurs commandes sur un flot initial. Autrement dit, la sortie de la première commande est redirigée en entrée de la seconde. Le pipe sur le terminal est représenté par |. Ce caractère est accessible au clavier via la touche AltGr (située à droite de la barre espace) et la touche 6 (située au dessus de la touche t et y)

## Page 8

1. Afficher le contenu du répertoire /bin à l’aide de la commande ls -l combinée avec

```text
more pour afficher petit à petit le contenu.
```

**Réponse du support :**

```text
ls -l /bin | more
```

2. Créer un fichier nbFic qui contient le nombre de d’éléments contenu dans le dossier /bin.

**Réponse du support :**

```text
ls -l | wc -l > nbFic
```

### 3 Et si je révisai !

1. Quelle est la différence entre :

```text
echo toto > toto
echo toto >> toto
```

**Réponse du support :**

```text
echo toto > toto ⇒ permet de remplacer le contenu du fichier toto par la chaîne de
```

caractères toto

```text
echo toto >> toto ⇒ permet d’ajouter à la fin du fichier toto, la chaîne de caractères
```

toto

2. Considérons un répertoire appelé toto.

(a) Ajouter à l’interieur un sous répertoire appelé tutu et un fichier tata

**Réponse du support :**

```text
mkdir -p toto/tutu
touch toto/tata
```

(b) Supprimer le repertoire tutu

**Réponse du support :**

```text
rmdir toto/tutu
```

(c) Supprimer le repertoire toto

**Réponse du support :**

```text
rm -rf toto
```

ou rmdir -rf toto

## Page 9

3. Considérons un fichier appelé maListe.csv contenant plus de 5000 lignes.

(a) Afficher dans le terminal le fichier. Quelle commande priviligiez vous et pourquoi ?

**Réponse du support :**

```text
more ou less car le fichier est trop important en nombre de lignes
```

(b) Combien de lignes exactes contient le fichier ?

**Réponse du support :**

```text
wc -l maListe.csv
```

(c) Combien de mots contient le fichier ?

**Réponse du support :**

```text
wc -w maListe.csv
```

4. De manière général, à quoi sert un alias ? Où peut-on le définir ?

**Réponse du support :**

Un alias sert à se créer des raccourcis de commandes afin de gagner du temps, et d’adapter le terminal à ses besoins. Le plus simple est de le définir dans le bashrc

5. De manière général, à quoi sert les pipes ?

**Réponse du support :**

Les pipes permettent de rediriger les sorties d’une commande vers une entrée d’une autre commande.

## Notes de transcription

- Page 1 : les redirections d’erreur s’écrivent `2>` et `2>>`, sans espace entre le descripteur 2 et l’opérateur ; le support espace cette notation.
- Page 2 : le chemin du périphérique est `/dev/null`, sans barre finale ; ce n’est pas un répertoire. La commande `echo` coupée par la mise en page a été réunie sur une ligne.
- Page 7 : l’alias imprimé `alias ls=ls -l` doit protéger sa valeur : `alias ls='ls -l'`. Le chargement automatique de `.bashrc` dépend du mode de démarrage de Bash ; `source ~/.bashrc` recharge son contenu dans le shell courant.
- Page 8 : `ls -l | wc -l > nbFic` ne désigne pas `/bin` et compte aussi la ligne `total` éventuelle. La réponse ne réalise donc pas exactement le comptage annoncé.
- Page 8 : `rmdir -rf toto` est une erreur du corrigé ; `rmdir` ne supprime pas récursivement les répertoires non vides. La première solution `rm -rf toto` est celle qui effectue cette suppression.
