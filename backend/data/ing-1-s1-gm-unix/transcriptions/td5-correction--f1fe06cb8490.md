---
source: "ING 1/S1 GM /UNIX/Commande Unix TD & Solutions/td5-correction.pdf"
pages: 10
transcription: texte, questions, réponses, scripts et données transcrits et relus
transcription_date: 2026-10-18
verification: comparaison du texte natif et contrôle visuel des dix pages, notamment des scripts et de leurs commentaires
---

# TP5 — Les scripts et les jobs, corrigé

Inès de Courchelle — 2021–2022.

Les scripts ci-dessous reproduisent ceux du PDF, avec leurs variables et commentaires d’origine. Les numéros de ligne et les flèches de continuation de la mise en page sont retirés. Les erreurs du support sont signalées à la fin.

## Page 1 — 1. Quelques conseils !

### 1.1. Quote, quote-quote ou back-quote

Taper dans un shell :

```sh
ls -l
ls -l | wc -l
echo "ls -l | wc -l"
echo 'ls -l | wc -l'
echo `ls -l | wc -l`
```

Le support indique `AltGr + 7` pour les back-quotes. Le premier `echo` utilise des doubles quotes, aussi appelées « quote-quote » ; le deuxième des simples quotes ; le dernier des back-quotes. Observer la différence entre les deux dernières commandes : elle est utile pour inclure des commandes dans d’autres.

## Page 2 — 2. Exercices — 2.1. Mon premier script

**1.** Recopier `script1.sh` dans un éditeur (`vi`, `emacs` ou autre), puis l’exécuter.

```bash
#!/bin/bash
for i in `seq 1 10`
# on peut aussi faire for i in $(seq 1 10)
do
    echo "Rock n roll"
done
```

Réponse : ouvrir `vi script1.sh`, passer en mode insertion, recopier le texte, quitter avec Échap puis `:wq!`, puis exécuter `./script1.sh`.

**2.** Décrire le programme suivant ligne par ligne.

```bash
#!/bin/bash
i1=`ls -a`
i2="grep -R 'tutu' ~"
echo $i1
echo $i2
```

Réponses du support :

1. Indique le chemin du « compilateur » pour le shell utilisé.
2. Crée une variable « contenant une commande ».
3. Génère une chaîne de caractères.
4. Affiche le résultat de la commande passée dans une variable.
5. Affiche la chaîne de caractères.

## Page 3 — Shell interactif et deuxième script

**3.** Exécuter un shell qui affiche « bonjour » directement dans le terminal, sans éditeur.

```sh
echo $0
sh
echo $0
echo "bonjour"
exit
echo $0
```

Le deuxième `echo $0` permet de voir le changement de shell ; `exit` quitte le shell lancé.

### 2.2. Mon deuxième script

Écrire `petitScript.sh`, prenant cinq arguments, qui affiche son nom, le nombre d’arguments, le numéro du processus qui l’exécute et la liste de ses arguments.

| Variable | Signification donnée dans le support |
| --- | --- |
| `$0` | Nom du programme en cours |
| `$1` à `$9` | Valeurs des arguments |
| `$#` | Nombre d’arguments |
| `$*` | Liste de l’ensemble des arguments |
| `$?` | État de sortie de la dernière commande : 0 en cas de succès, valeur non nulle sinon |
| `$$` | Numéro du processus en cours |

## Page 4 — Réponse : petitScript.sh

```bash
#!/bin/bash
echo "Le nom de mon programme est $0"

echo "Le nombre de paramètre est $#"
echo "Le numéro du processus courant est $$"

for i in $(seq 0 $#)
do
    echo " Le parametre numero $i est ${!i} "
done
```

## Page 5 — 2.3. Mon troisième script

1. Créer dans le répertoire personnel `monTroisieme`, contenant les fichiers éventuellement vides `p1.c`, `p2.pas`, `p3.py`, `memo`, `p4.c`, `p5.txt`, `p6.sh` et `p7.sh`.
2. Ajouter manuellement le droit d’exécution à quelques fichiers, par exemple `p3.py`, `p6.sh` et `p7.sh`.
3. Créer dans le répertoire personnel `maTache.sh`, appelé avec exactement un argument, et vérifier que cet argument désigne un répertoire.
4. Parcourir les fichiers du répertoire fourni et afficher les noms de ceux qui sont exécutables. Tester avec `monTroisieme` (écrit `monTroisième` dans cette question). Un fichier Unix est dit exécutable s’il possède les droits d’exécution.
5. Afficher la taille de chaque fichier exécutable.
6. Compter les fichiers exécutables.
7. Créer un répertoire `exec` et y déplacer tous les exécutables.

## Page 6 — Réponse : maTache.sh

```bash
#!/bin/bash

if [ $# -ne 1 ] #if test $# -ne 1 ou if [ $# < 2 ]
then
    echo "il y a $# paramètres. Il faut un seul paramètre"
    exit 1
fi
if [ ! -d $1 ]
then
    echo "$1 n'est pas un répertoire"
    exit 2
fi
#Initialisation du compteur de fichiers executables
nbFic=0
#Création du dossier executable
nomRep="exec"
mkdir -p $1/$nomRep
#Parcours des différents fichiers
for i in $1/*
do
    #Attention un fichier est dit exécutable si et seulement si il a des droits x
    if [ -x $i ] && [ ! -d $i ]
    then
        #---------------------------------------------------
        #Il existe plusieurs solution pour l'incrémentation
        let nbFic++
        #solution 2 => nbFic=$(($nbFic+1))
        #---------------------------------------------------
        #information du fichier concernant la taille
        taille=$(du -hs $i)
        echo "$i a une taille $taille"
        #---------------------------------------------------
        #Deplacement du fichier
        mv $i $1/$nomRep
    fi
done
echo "il y a $nbFic executables deplaces dans $1/$nomRep"
```

## Page 7 — 2.4. Les modes d’exécution des processus

**1.** Créer un script comportant une boucle infinie avec `sleep`. Consulter son manuel.

```bash
#!/bin/bash
while [ 1 ]
do
    sleep 2
done
```

**2.** Lancer le script au premier plan (*foreground*). Peut-on encore exécuter des commandes dans ce terminal ? Réponse : non.

**3.** Arrêter le script et vérifier sa disparition de la liste des processus : `Ctrl+C` arrête le processus, puis :

```sh
ps -ef | grep -wi "script"
```

**4.** Exécuter le script en gardant l’usage du terminal.

```sh
./script &
```

**5.** Lancer `./script` au premier plan, puis `Ctrl+Z` pour le suspendre, `bg` pour reprendre le dernier job en arrière-plan (*background*) et `fg` pour le ramener au premier plan.

## Page 8 — Arrêt des jobs et fichier de notes

**6.** Lancer le script en arrière-plan, le chercher dans les processus, puis le tuer.

```sh
./script &
```

Le corrigé propose un autre terminal pour envoyer `kill -9` au PID du bash exécutant le script. Il propose aussi `jobs`, puis `kill -9 %n` avec le numéro de job approprié.

**7.** Lancer deux scripts en arrière-plan, puis tuer les deux processus.

```sh
./script &
./script &
jobs
```

`jobs` donne les identifiants locaux des processus lancés. La dernière ligne de réponse est imprimée sans séparateur :

```sh
kill %1 kill %2
```

### 3. Et si je révisai !

**1.** Fichier de notes :

```text
Liste de notes EISTI 2017
paco 10
pepe 5
jose 18
juan 15
luis 19.5
toto 2
titi 5
```

## Page 9 — Réponse : trier sans déplacer l’en-tête

Créer un script affichant les notes triées sans trier la première ligne.

```bash
#!/bin/bash

# On teste si le premier argument est un fichier
if [ -f $1 ]
then
    # On affiche la première ligne
    head -n 1 $1
    # On compte le nombre de ligne du fichier
    NBLIGNES=`wc -l $1`
    # On vérifie que le fichier contient bien assez de ligne
    if [ ${NBLIGNE} -gt 1 ]
    then
        # On en enlève un (l'entete)
        NBLIGNE=$((NBLIGNE - 1))
        # On n'affiche donc les n-1 dernieres lignes, puis on trie sur le deuxième champ
        tail -n ${NBLIGNE} $1 | sort -k2n
    else
        # Sinon, il n'y a pas assez de ligne
        echo "Le fichier ne contient pas assez de ligne"
    fi
else
    # Sinon on n'a pas un fichier valide
    echo "$1 n'est pas un fichier valide"
fi
```

## Page 10 — Révision des jobs

**2.** Afficher les jobs dont on est propriétaire. Réponse :

```sh
ps -ux
```

**3.** Afficher les identifiants locaux des processus lancés.

```sh
jobs
```

**4(a).** Exécuter `toto.sh` : `./toto.sh`.

**4(b).** Le passer en arrière-plan : `Ctrl+Z`, puis `bg %1`.

**4(c).** L’arrêter : `kill -9 %1`.

## Écarts relevés dans le document source

- Page 2 : `#!/bin/bash` désigne l’interpréteur, pas un compilateur. La substitution de commande affecte à `i1` la sortie de `ls -a`, pas la commande elle-même. L’exécution par `./script1.sh` suppose un droit d’exécution ; on peut aussi lancer `bash script1.sh`.
- Page 4 : le script ne vérifie pas qu’il reçoit cinq arguments et sa boucle inclut l’indice 0, donc le nom du script.
- Page 6 : le commentaire `if [ $# < 2 ]` n’est pas une variante correcte du test « exactement un argument ». Le caractère `<` non protégé est une redirection du shell. Les expansions de chemins devraient être protégées, par exemple `"$1"`, `"$i"` et `"$1/$nomRep"`, pour accepter les espaces. Le parcours `$1/*` omet les fichiers cachés par défaut.
- Page 6 : `du -hs` indique l’espace disque occupé, avec le nom du fichier ; ce n’est pas simplement une taille en octets. Le test « exécutable et pas un répertoire » n’exige pas explicitement un fichier ordinaire.
- Page 8 : écrire `kill %1; kill %2` ou `kill %1 %2`, au lieu de `kill %1 kill %2`. Les identifiants `%1`, `%2`, `%n` sont ceux de la table des jobs du shell concerné, pas des PID utilisables depuis n’importe quel terminal.
- Page 9 : `NBLIGNES` est affectée mais `NBLIGNE` est lue. De plus, `wc -l $1` renvoie le nombre accompagné du nom de fichier. Une affectation cohérente serait `NBLIGNE=$(wc -l < "$1")`, avec le même nom utilisé ensuite. Les chemins et les expansions du test doivent aussi être protégés.
- Page 10 : `ps -ux` liste des processus ; `jobs` liste les jobs connus du shell courant. Le numéro `%1` n’est valable que s’il correspond au script visé.
