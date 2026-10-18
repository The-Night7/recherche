---
source: "ING 1/S1 GM /EXAMEN/Brouillon_Unix_Shell.pdf"
pages: 2
transcription: mémento, commandes, exemples Bash et syntaxes transcrits et relus
transcription_date: 2026-10-18
verification: comparaison du texte natif et contrôle visuel des deux pages du PDF ; disposition en trois colonnes restituée par rubriques
---

# Brouillon Unix/Shell — commandes, théorie et Bash

Le document est un mémento de révision CY Tech ING1. La première page couvre les notions et commandes Unix ; la seconde couvre l'écriture de scripts Bash. Les commandes sont données telles qu'elles apparaissent dans le support, avec des précisions séparées en fin de transcription.

## Page 1 — notions de base

### Chemins, shell et documentation

| Notation ou commande | Rôle indiqué |
| --- | --- |
| `~` | répertoire personnel, par exemple `/home/user` |
| `/` | racine du système |
| `.` / `..` | répertoire courant / répertoire parent |
| `/home/user/file` | chemin absolu |
| `../file` | chemin relatif |
| `man cmd` / `man -k mot` | consulter une page de manuel / chercher un mot-clé dans les manuels |

Le pipe `|` envoie la sortie de `cmd1` vers l'entrée de `cmd2` ; l'exemple `ls | wc -l` compte les fichiers. Le support le présente comme un moyen de communication inter-processus. `find` cherche les **noms** de fichiers ou répertoires, tandis que `grep` cherche leur **contenu**.

Un répertoire est un fichier spécial de type `d` contenant une liste ou description de fichiers. Le shell est l'interpréteur de commandes : il affiche l'invite, analyse puis exécute les commandes et crée des processus. `echo $SHELL` affiche le shell courant.

`~/.bashrc` est présenté comme un fichier de configuration lu au démarrage du terminal, qui peut contenir alias, variables et réglages personnels ; `source ~/.bashrc` le recharge. Un alias est un surnom de commande : `alias ll='ls -la'`, supprimé par `unalias ll`. Le support recommande de le placer dans `.bashrc` pour le rendre permanent.

Un lien symbolique est un pointeur vers un fichier ou répertoire : `ln -s cible lien`. S'il perd sa cible, le lien est cassé ; il évite de dupliquer les données.

### Navigation et fichiers

```sh
pwd                         # répertoire courant
cd /path ; cd ~ ; cd        # changer de répertoire (répertoire personnel)
cd ..                       # parent
ls ; ls -l ; ls -a ; ls -la # listes courante, détaillée, cachée, détaillée+cachée
ls -lt ; ls -ltr            # tri par date récent→ancien / ancien→récent
ls -R ; ls -F ; ls *.txt    # récursif ; indicateurs ; seulement les .txt
mkdir rep ; mkdir -p a/b/c  # créer un répertoire / une hiérarchie
touch file                  # créer un fichier vide ou mettre sa date à jour
rm file ; rmdir rep         # supprimer un fichier / un répertoire vide
cp src dest ; cp -r rep1/ rep2/ ; mv old new
cat file ; cat -n file      # afficher, avec numéros de ligne
more file ; less file       # lecture paginée et navigation
head file ; head -n5 file   # dix ou cinq premières lignes
tail file ; tail -n5 file   # dix ou cinq dernières lignes
wc file ; wc -l file ; wc -w file
```

Le support affiche également `rm -rf rep/` pour une suppression récursive forcée.

### Redirections, recherche et filtres

| Forme | Effet indiqué |
| --- | --- |
| `cmd > file`, `cmd >> file`, `cmd < file` | rediriger la sortie en écrasant, en ajoutant, ou rediriger l'entrée |
| `cmd 2> file`, `cmd 2>> file` | écrire les erreurs en écrasant ou en ajoutant |
| `cmd > file 2>&1` | réunir sortie standard et erreurs |
| `cmd 2>/dev/null` | ignorer les erreurs |
| `echo 'txt' > file`, `echo 'txt' >> file`, `date > hoy` | écrire ou ajouter du texte, écrire la date |
| `find . -name 'file'`, `find . -name '*.txt'` | rechercher un nom exact ou une extension |
| `find . -type f`, `find . -type d` | sélectionner fichiers ou répertoires |
| `find . -name 'f' -exec cmd {} \;` | exécuter une commande sur chaque résultat |
| `grep 'mot' file`, `grep -i`, `-n`, `-c`, `-v` | chercher, ignorer la casse, numéroter, compter, exclure |
| `grep -r 'mot' rep/`, `grep -R 'mot' /etc/ 2>/dev/null` | recherche récursive |

Les expressions montrées sont `^deb` (début de ligne), `fin$` (fin), `^$` (ligne vide), `-v '^$'` (ligne non vide), `[0-9]`, `^[A-Z]` et `-wi` (mot entier sans casse).

Le mémento récapitule aussi :

```sh
sort file ; sort -r file ; sort -n file
sort -k2 file ; sort -k2n file ; sort -k2nr file
sort -t',' -k2 file
cut -d',' -f1 file ; cut -d' ' -f1,3 file
uniq file ; sort | uniq
tr 'a' 'A' < file ; tr [:lower:] [:upper:] ; tr -d 'a' < file
```

### Droits, édition, processus et réseau

Les droits sont chiffrés avec `r=4`, `w=2`, `x=1`. Le support donne `chmod 755 file` (`rwxr-xr-x`), `644`, `777`, `700`, `744`, puis `chmod u+x file`, `g+w file`, `o-r file` et `chmod -R 755 rep/`. Les trois chiffres concernent respectivement propriétaire, groupe et autres ; l'exemple `754` vaut `rwxr-xr--`.

`sed` est illustré par les substitutions `s/old/new/`, `s/old/new/g`, `s/old/new/gi`, les suppressions `2,4d` et `/mot/d`, l'affichage `-n '5,10p'`, les ancres `^` et `$`, plusieurs expressions `-e`, et le remplacement de `;` par `!`.

Pour les processus et travaux : `ps`, `ps -ef`, `ps aux`, `ps -u user`, `top` (quitter avec `q`), `kill PID`, `kill -9 PID`, `./script &`, `Ctrl+Z`, `bg`, `fg`, `jobs`, `kill %1`.

Pour liens, archives et espace : `ln -s cible lien`, `tar -cvf a.tar rep/`, `tar -xvf a.tar`, `tar -czvf a.tar.gz r/`, `tar -xzvf a.tar.gz`, `du -h file`, `du -hs rep/`, `df -h`.

Pour le réseau : `ssh user@host`, `ssh user@ssh.pau.eisti.fr`, `scp file user@host:~`, `scp -r rep/ user@h:~`, `scp user@h:file .`, `who`, `who -b`. Les autres commandes signalées sont notamment `history`, `date`, `clear`, `passwd`, `which`, `whereis`, `env`, `export VAR=val` et `echo $HOME`.

Les jokers et expressions régulières de la page sont `*`, `?`, `[abc]`, `[0-9]`, `[a-z]`, `[A-Z]`, `^`, `$`, `.`, `.*`.

## Page 2 — scripts Bash

### Structure et variables

Un script commence par `#!/bin/bash`; les commentaires commencent par `#`. Les exemples d'entrée-sortie sont `echo 'Hello World'`, `read var` et `read -p 'Msg: ' var`. Le support donne trois modes de lancement : rendre le fichier exécutable avec `chmod +x script.sh` puis `./script.sh`, ou l'appeler avec `bash script.sh` ou `sh script.sh`.

Les affectations ne comportent pas d'espace : `var='valeur'`; on l'affiche par `$var` ou `${var}`. Paramètres et états : `$0` nom du script ; `$1` à `$9` arguments ; `$#` nombre d'arguments ; `$*` tous les arguments en chaîne ; `$@` tous les arguments ; `$$` PID ; `$?` code de retour (zéro si succès).

La substitution moderne indiquée est `result=$(ls -l)`, préférée à ``result=`ls -l` ``. L'arithmétique est illustrée par `n=$((n+1))`, `let n++`, `n=$(($n * 2))` et `n=$((n-3))`.

### Tests et contrôle

```bash
if [ condition ]; then
    commandes
elif [ autre_condition ]; then
    commandes
else
    commandes
fi
```

Le support insiste sur les espaces autour de `[` et `]`. Comparaisons numériques : `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`. Chaînes : `[ "$s1" = "$s2" ]`, `!=`, `-z`, `-n`. Fichiers : `-e`, `-f`, `-d`, `-r`, `-w`, `-x`. Opérateurs : `&&`, `||`, `!`.

Les boucles `for` parcourent une liste, `{1..10}`, `$(seq 1 10)`, `*.txt`, `$*` ou `$@`. Les formes `while [ condition ]; do … done` et `until [ condition ]; do … done` sont données, ainsi qu'une boucle infinie `while true; do sleep 2; done`. L'exemple de contrôle saute 5 avec `continue`, s'arrête à 8 avec `break`.

Un menu utilise `read -p "Choix: " choix` et :

```bash
case $choix in
  1) echo "Option 1" ;;
  2) echo "Option 2" ;;
  3) echo "Option 3" ;;
  *) echo "Invalide" ;;
esac
```

### Exemples et éditeur

Les exemples demandent un argument (`[ $# -ne 1 ]`), un fichier (`[ ! -f "$1" ]`) ou un répertoire (`[ ! -d "$1" ]`), puis parcourent les fichiers de `$1/*`, comptent les exécutables avec `-x` et `-f`, ou déplacent le résultat de `find . -name $1 -exec mv {} Partiel \;` dans `Partiel`. Le mémento montre aussi un tri de notes (`head -n 1`, puis `tail -n +2 | sort`) et une boucle demandant un login jusqu'à `quit`, utilisant `id` et `groups`.

Pour `vi` : `vi file`, `i`, `Esc`, `:w`, `:q`, `:wq` ou `:x`, `:wq!`, `:q!`, `/mot`, `n`, `dd`, `yy`, `p`, `u`.

Les « astuces exam » réunissent notamment `ls -l | grep '^d'`, `ls -l | grep '^-'`, `find . -name '*.txt' | wc -l`, `grep -c`, `sort | uniq`, `grep -v '^$'`, `sed '/^$/d'`, `sort -t',' -k2 f | cut -d',' -f2`, `ls -1`. Le support met en garde contre l'absence d'espaces dans les tests, les chaînes non protégées par des guillemets, l'oubli du *shebang*, de `chmod +x`, ou l'emploi de `=` au lieu de `-eq` pour les entiers.

## Précisions de transcription

- `rm -rf`, `kill -9` et les redirections avec `>` ont les effets destructifs indiqués par leur usage ; ils ne sont pas des commandes à appliquer sans vérification de la cible.
- Dans Bash, préférer `"$@"` à `$@` ou `$*` dans une boucle afin de préserver les arguments contenant des espaces. Les noms de fichiers devraient aussi être cités, par exemple `"$file"`.
- `sort | uniq` ne supprime que les doublons adjacents : le pipeline doit être relié à une entrée, par exemple `sort file | uniq`.
- La page présente `find … -exec … \;` sans protections de glob ou de nom ; cela restitue le mémento, pas une règle de sécurité complète.
