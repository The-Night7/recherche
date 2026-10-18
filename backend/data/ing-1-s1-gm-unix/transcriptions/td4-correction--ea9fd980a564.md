---
source: "ING 1/S1 GM /UNIX/Commande Unix TD & Solutions/td4-correction.pdf"
pages: 7
transcription: texte, questions, réponses et commandes transcrits et relus
transcription_date: 2026-10-18
verification: comparaison du texte natif et contrôle visuel des sept pages du PDF
---

# TP4 — Des processus au shell, corrigé

Inès de Courchelle — 2021–2022.

Les réponses sont celles du support. Les apostrophes, le symbole de début de ligne et le tilde sont rendus par leurs caractères shell. Les erreurs de commandes sont conservées et commentées en fin de transcription.

## Page 1 — Consignes, objectifs et archives

Durant ce TD, souris, Touchpad et Trackpoint sont interdits : seul le clavier est autorisé.

Objectifs : archiver des dossiers et fichiers en ligne de commande ; afficher les processus en cours d’exécution ; gérer l’espace sur son ordinateur ; utiliser les expressions régulières ; se familiariser avec les variables prédéfinies du shell.

Fichier attaché : `tp4.tar`.

### 1. Exercices — 1.1. Les archives

**1.** Télécharger `tp4.tar` sur AREL et décompresser l’archive dans `CommandesUnix/tp4`.

```sh
tar -xvf tp4.tar
```

**2.** « Compresser l’archive en .zip et en .tar » dans `CommandesUnix/tp4`.

```sh
tar -cvz tp4 -f tp4.zip
tar -cv tp4 -f tp4.tar
```

## Page 2 — Fichiers et processus

**3.** Lister le contenu de `tp4` par date de modification décroissante.

```sh
ls -lart tp4
```

**4.** Afficher `lesListes.pas` avec ses numéros de ligne.

```sh
cat -n lesListes.pas
```

**5.** Vérifier que seul le propriétaire peut lire, écrire et exécuter ce fichier ; modifier les droits si nécessaire.

```sh
chmod 700 lesListes.pas
```

**6.** Ajouter le droit d’exécution au groupe pour l’ensemble des fichiers du dossier `TP4`.

```sh
chmod g+x *
```

**7.** Afficher uniquement les fichiers d’extension `.txt`.

```sh
ls *.txt
```

### 1.2. Les processus

**1.** Visualiser les processus du terminal courant.

```sh
ps
```

## Page 3 — Processus et gestion des espaces

**2.** Visualiser tous les processus du système. Quel est le père de la plupart des processus système ?

```sh
ps -ef
ps auwx
```

Le corrigé répond : « Le père de la plupart est systemd et non init ». Pour afficher l’arbre des processus, il propose :

```sh
ps -axjf
ps -ejH
pstree
```

Il ajoute à propos de `pstree` : « il faut installer tree ».

**3.** Visualiser les processus dont on est propriétaire. `<mon_login>` est un emplacement à remplacer.

```text
ps -x -u <mon_login>
```

### 1.3. Gestion des espaces

**1.** Afficher l’espace utilisé par le répertoire personnel.

```sh
du -hs ~
```

**2.** Visualiser la taille de chacun de ses sous-répertoires.

```sh
du -h ~
```

**3.** Trier les sous-répertoires par taille décroissante et commenter.

```sh
du -h ~ | sort -k1n | more
```

Le support observe que les caches, surtout celui du navigateur web, occupent le plus de place.

## Page 4 — 1.4. Les expressions régulières

**1.** Remplacer tous les H par Z dans `hp1.txt` et enregistrer dans `hp1Modif1.txt`. La réponse utilise un autre nom de destination :

```sh
sed -e 's/H/Z/g' hp1.txt > hp1Modif.txt
```

**2.** Remplacer les m en début de ligne par M, dans `hp1Modif2.txt`.

```sh
sed -e 's/^m/M/g' hp1.txt > hp1Modif2.txt
```

**3.** Remplacer les lettres précédées d’un espace par une virgule, dans `hp1Modif3.txt`.

```sh
sed -e 's/ [a-z|A-Z]/ ,/g' hp1.txt > hp1Modif3.txt
```

**4.** Remplacer les virgules par `+` et les points-virgules par `@`, dans `hp1Modif4.txt`.

```sh
sed -e 's/,/+/g;s/;/@/g' hp1.txt > hp1Modif4.txt
```

**5.** Copier le contenu de `hp1.txt`, sans les lignes 2, 3 et 4, dans `hp1Modif5.txt`.

```sh
sed -e '2,4d' hp1.txt > hp1Modif5.txt
```

## Page 5 — Recherche et variables du shell

**6.** Avec `ls` et `grep`, rechercher dans `/etc` et ses sous-répertoires les noms :

**(a)** Commençant par a, suivi de s ou t. La source omet l’espace entre l’option et le chemin :

```sh
ls -R/etc | grep -E '^a[st]'
```

**(b)** Contenant au et se terminant par t.

```sh
ls -R /etc | grep -E '*au.*t$'
```

**(c)** Contenant gre ou st.

```sh
ls -R /etc | grep -E 'gre|st'
```

### 1.5. Les variables prédéfinies du shell

**1.** Taper `printenv`, `env` et `set`. Que font ces commandes ?

- `printenv` affiche les variables d’environnement ; le corrigé la qualifie de commande ancienne.
- `env` affiche les mêmes variables.
- `set` affiche en plus les variables locales.

**2.** Qu’est-ce que le prompt et quelle variable privée le représente ? Le prompt est une invite de commande ; il indique généralement le nom de l’utilisateur, celui de la machine et le chemin du répertoire courant. La variable est `PS1`.

## Page 6 — Prompt, historique et révision

**3.** Remplacer le prompt par « Vous ne passerez pas ! ». Réponse du support :

```sh
export PS1="Vous ne passerez pas "
```

**4.** Combien de commandes sont mémorisées dans l’historique ? Changer ce nombre. Indice : `HISTSIZE`.

```sh
echo $HISTSIZE
export $HISTSIZE=3
```

### 2. Et si je revisai !

**1.** Extraire `monArchive.tar` dans le répertoire courant (le sujet écrit « déziper »).

```sh
tar xvf monArchive.tar
```

**2.** Afficher uniquement les fichiers `.txt` du répertoire `monExam`, situé dans le répertoire courant.

```sh
ls -R monExam/*.txt
```

**3.** Une variable d’environnement permet d’influencer le comportement du système, par exemple sa langue ou son encodage de caractères.

## Page 7 — Révision des expressions régulières

**4.** Avec `grep`, rechercher dans le répertoire courant et ses sous-répertoires :

**(a)** Les mots commençant par C.

```sh
ls -R | grep -e '^C'
```

**(b)** La chaîne `mesRevisions`.

```sh
ls -R | grep -e 'mesRevisions'
```

**5.** Les expressions régulières servent à identifier une chaîne de caractères répondant à plusieurs critères.

## Écarts relevés dans le document source

- Page 1 : `tar -cvz` crée une archive tar compressée avec gzip, même si son nom se termine par `.zip`. Une extension cohérente serait `.tar.gz` ; une archive ZIP nécessite un outil approprié tel que `zip`. Une archive `.tar` n’est pas nécessairement compressée.
- Page 2 : `ls -lart` inverse le tri temporel avec `-r`, affichant les plus anciens fichiers en premier. Pour les plus récents d’abord : `ls -lat tp4`.
- Page 2 : `chmod g+x *` suppose que le répertoire courant soit le dossier visé ; le motif `*` n’inclut pas les fichiers cachés par défaut.
- Page 3 : `pstree` et `tree` sont deux commandes distinctes ; installer `tree` ne fournit pas nécessairement `pstree`. La remarque sur `systemd` décrit le système utilisé dans le cours.
- Page 3 : `sort -k1n` trie par ordre croissant et ne compare pas correctement les suffixes K, M, G de `du -h`. Avec GNU sort, `du -h ~ | sort -hr | more` réalise le tri décroissant demandé.
- Page 4 : la réponse à la question 1 omet le chiffre 1 dans le nom de sortie. Dans `[a-z|A-Z]`, le caractère `|` fait partie de la classe et ne signifie pas « ou » ; `[a-zA-Z]` correspond aux lettres visées.
- Page 5 : question 6(a), écrire `ls -R /etc` avec un espace. Question 6(b), le `*` initial du motif n’a pas d’élément à répéter ; `au.*t$` suffit pour la recherche demandée.
- Page 6 : la réponse sur le prompt omet le point d’exclamation demandé. Pour affecter la taille de l’historique, écrire `export HISTSIZE=3`, sans `$` à gauche du signe égal.
- Pages 6–7 : `ls -R monExam/*.txt` n’effectue pas une recherche générale des fichiers `.txt` dans tous les sous-répertoires. Les pipelines de la question 4 filtrent des noms affichés par `ls`, pas les mots contenus dans les fichiers.
