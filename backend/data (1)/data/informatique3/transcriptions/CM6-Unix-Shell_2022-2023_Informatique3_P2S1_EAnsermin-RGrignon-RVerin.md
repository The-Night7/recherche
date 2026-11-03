# Informatique 3 — CM6 : Unix et script shell (2022–2023)

Eva Ansermin, Renaud Verin et Romuald Grignon — version 1.01, 126 pages PDF.

Source : `PREING2-S1/Informatique3/CM6-Unix-Shell_2022-2023_Informatique3_P2S1_EAnsermin-RGrignon-RVerin.pdf`.

Transcription achevée le 12 octobre 2026. Texte natif intégral relu ; schémas de fichiers, redirections et exemples de code confrontés aux rendus. Les répétitions sont regroupées avec leurs pages source. Les apostrophes typographiques et tirets non ASCII sont normalisés dans le code ; les corrections de fond sont identifiées. Les exemples visent principalement **Bash**.

## I. Contexte : système d'exploitation — pages 1–5

Le système d'exploitation relie le matériel et les applications. Schéma : **utilisateur → applications → système d'exploitation → matériel**.

Il assure l'interface utilisateur (interpréteur de commandes, interface graphique), la gestion de la RAM (allocation, libération, segmentation, besoins du noyau et des tâches), celle du stockage persistant (disques, clés USB, fichiers), les fonctions du noyau (processus, allocation du CPU, interruptions) et les pilotes des périphériques.

Une distribution regroupe système, pilotes et applications. Le diagramme historique du support porte les mentions suivantes : Unix (1969), DOS (1981), System 1 (1984), Windows 1 (1985), Linux (1991), BSD 4 (1991), Debian (1993), Mac OS 9 (1999), Mac OS X (2000), Ubuntu 4.10 (2004), puis Debian 11.5, Ubuntu 22.10 et Mac OS 12.5 (2022), Windows 11 (2021). Il relie Unix aux branches Linux et BSD, Linux à Debian et Ubuntu, BSD à Mac OS X, la lignée System 1/Mac OS 9 à Mac OS X, et DOS/Windows 1 à Windows 11.

**Note.** Ce diagramme est un aperçu historique simplifié de l'édition 2022 ; ses flèches ne constituent pas une généalogie technique précise. Les versions mentionnées ne sont pas présentées comme actuelles.

## II. Concepts Unix — pages 6–8

Unix est multitâche et multiutilisateur. Quatre concepts structurent le cours : fichiers, droits d'accès, processus et communication entre processus. Les pages 29, 35 et 37 reprennent ce plan comme transitions.

## Fichiers, inodes et liens — pages 9–15

Le fichier est l'unité de gestion des ressources. Les informations associées comprennent propriétaire, groupe, droits de lecture/écriture/exécution, date de modification, taille et références des blocs de données. Unix expose de nombreuses ressources sous forme de fichiers : données ordinaires, répertoires, liens, périphériques et flux.

Les métadonnées et références aux données sont portées par un **inode**. Le schéma représente `FILE1 → INODE1 → DATA BLOCK #1, #2, …`. Pour ouvrir un fichier par son nom, on résout son entrée dans le répertoire, puis l'inode et les données.

**Correction de formulation.** Le support attribue au « fichier » le seul couple nom/numéro d'inode : c'est plus précisément **l'entrée de répertoire** qui associe un nom à un numéro d'inode. L'unicité de ce numéro est locale au système de fichiers. La formule « inode = index of node » est celle du support.

| Type de lien | Représentation | Si le nom cible disparaît |
| --- | --- | --- |
| Symbolique, souple | Un autre fichier et son propre inode contiennent le chemin de la cible | Le lien devient inutilisable si ce chemin ne résout plus la cible |
| Physique, dur | Un autre nom désigne le même inode | Les données restent accessibles par ce nom |

Les deux schémas de lien symbolique montrent le chemin stocké soit dans un bloc de données, soit directement dans l'inode pour un lien court (*fast symlink*). Le schéma de lien dur montre `FILE1` et `link-H` pointant tous deux vers `INODE1`.

**Précision ajoutée.** Les données peuvent être libérées lorsque plus aucun lien dur ne subsiste **et** que plus aucune ouverture ne les maintient accessibles. Supprimer un nom ne supprime pas immédiatement un fichier encore ouvert par un processus.

## Répertoires et chemins — pages 16–28

Les répertoires regroupent les entrées de fichiers dans une hiérarchie. Le dessin part de `/` et contient les branches suivantes :

| Chemin | Rôle indiqué |
| --- | --- |
| `/` | Racine de l'arborescence |
| `/bin` | Commandes de base |
| `/dev` | Fichiers de périphériques |
| `/etc` | Configuration et démarrage |
| `/home` | Dossiers des utilisateurs, ici `ean` et `rgn` |
| `/lib` | Bibliothèques compilées, notamment pour `/bin` |
| `/tmp` | Fichiers de travail temporaires |
| `/usr/include` | Fichiers d'en-tête des langages |
| `/usr/bin` | Commandes complémentaires |
| `/var` | Données variables, journaux, courrier, etc. |
| `/home/rgn` | Dossier personnel de l'utilisateur `rgn` |

Un chemin commençant par `/` est absolu ; un chemin relatif est interprété depuis le répertoire courant. `.` désigne le courant, `..` son parent ; `~` est développé par le shell en dossier personnel. Le support cite `-` pour le dossier précédent : **c'est l'argument spécial de `cd -`**, pas un nom de répertoire universel. La racine `/` est celle de l'arborescence montée, pas nécessairement celle d'un unique disque physique.

## Noms et droits d'accès — pages 30–34

Les noms n'imposent ni suffixe ni préfixe. `/` sépare les composants et ne peut faire partie d'un nom ; un octet nul ne le peut pas non plus. Un nom commençant par `.` est masqué par les affichages ordinaires. Espaces et caractères tels que `?`, `&`, `*` sont possibles, mais exigent de maîtriser les protections du shell.

Le propriétaire est généralement le créateur ; il peut modifier les permissions, même lorsqu'il s'est retiré les droits ordinaires sur le contenu. L'administrateur dispose de pouvoirs supplémentaires. **Correction :** contrairement à la généralisation de la page 31, un utilisateur ordinaire ne peut pas nécessairement transférer un fichier à un autre propriétaire ; le changement de propriétaire est normalement réservé à un utilisateur privilégié sous Linux.

| Droit | Fichier ordinaire | Répertoire |
| --- | --- | --- |
| `r`, lecture | Lire son contenu | Lire la liste des noms |
| `w`, écriture | Modifier son contenu | Modifier les entrées, sous réserve des autres permissions |
| `x`, exécution | L'exécuter si son format le permet | Traverser/rechercher dans le répertoire |

**Correction :** le droit d'écriture sur un fichier ne commande pas directement sa suppression. Retirer son nom dépend surtout des droits sur le répertoire parent, avec les restrictions éventuelles telles que le *sticky bit*.

Les trois groupes de permissions concernent le propriétaire, le **groupe du fichier** et les autres utilisateurs. Exemple `-rwxr-x--- my_application` : propriétaire `rwx`, groupe `r-x`, autres `---`. Le premier caractère indique le type : `-` fichier ordinaire, `d` répertoire, `l` lien symbolique. Le support donne aussi `-rwxrwxrwx my_application`, `drwxrwxrwx my_folder`, `lrwxrwxrwx my_link`.

## Processus et communication — pages 35–38

Un processus est une unité de traitement : instructions, espace mémoire et ressources comme les descripteurs de fichiers et connexions réseau. Il possède un identifiant PID et l'identifiant de son parent, PPID. Un thread est un fil d'exécution partageant des données et ressources avec d'autres threads du même processus.

Les processus communiquent par signaux, mémoire partagée, tubes (*pipes*) ou sockets. Mutex et sémaphores permettent de coordonner l'accès aux ressources partagées.

## III. Terminal et commandes — pages 39–44

L'interpréteur analyse la commande saisie dans le terminal et l'exécute. Forme générale :

```text
nom_commande options arguments
```

Les options peuvent être courtes (`-o`, `-l`, `-r`, `-f`) ou longues (`--color`, `--version`). Les arguments désignent notamment fichiers et expressions. Aide détaillée : `man nom_commande` ; aide succincte, lorsque disponible : `nom_commande --help`.

Une commande retourne un statut : 0 pour le succès, une autre valeur pour un résultat non réussi. Le shell expose le dernier statut dans `$?` :

```bash
ls myDir
echo $?
```

**Précision :** les commandes peuvent être des exécutables externes, mais aussi des commandes internes du shell ou des fonctions. Un statut non nul peut signifier un résultat normal négatif, par exemple aucune correspondance, pas nécessairement une anomalie du programme.

Les motifs de noms emploient `?` pour un caractère, `*` pour zéro ou plusieurs caractères, `[df]` pour un caractère parmi d et f. La source imprime les trois motifs suivants entre guillemets, ce qui **empêche leur développement par le shell**. Voici les exemples corrigés pour l'intention annoncée :

```bash
ls *.png
ls ???.png
ls [df]*.png
```

Ils sélectionnent respectivement les noms PNG, ceux dont le radical a trois caractères, ceux commençant par d ou f. Les comportements sans correspondance et pour les noms cachés dépendent des options du shell ; le support ne les développe pas.

## IV. Entrées, sorties et redirections — pages 45–54

Un programme peut lire l'entrée standard (`stdin`, descripteur 0), écrire sur la sortie standard (`stdout`, 1) et sur l'erreur standard (`stderr`, 2). Les schémas relient ces trois flux à des fichiers ou à d'autres programmes.

| Syntaxe du support | Effet |
| --- | --- |
| `sort < "my_file.txt"` | Lire le fichier, trier ses lignes et les écrire sur la sortie standard |
| `ls > "my_file.txt"` | Créer ou remplacer le fichier par la sortie de `ls` |
| `ls >> "my_file.txt"` | Créer ou ajouter la sortie à la fin du fichier |
| `cat < my_file.txt \| sort > my_file2.txt` | Transmettre la sortie de `cat` à l'entrée de `sort`, puis écrire le résultat |
| `cat < my_file.txt 2>erreurs.txt \| sort > my_file2.txt` | Rediriger aussi l'erreur standard de la première commande vers un fichier |
| `cat < my_file.txt 2>&1 \| sort > my_file2.txt` | Fusionner ses sorties standard et d'erreur dans le tube |

Un tube ordinaire transmet la sortie standard, pas l'erreur standard. `2>&1` duplique la destination courante du descripteur 1 sur le descripteur 2.

**Précisions ajoutées.** L'erreur standard peut aussi recevoir diagnostics et messages d'avancement. L'ordre des redirections compte : dans les exemples imprimés, un échec d'ouverture de `my_file.txt` arrive avant la redirection de `stderr`. Pour capturer également cet échec, placer `2>erreurs.txt` ou `2>&1` **avant** `< my_file.txt`.

## V. Scripts et familles de shells — pages 55–59

Un script est un fichier texte dont l'interpréteur exécute les instructions. Il automatise des commandes, accepte des paramètres et demande généralement peu d'interactions. Le support oppose langages compilés (C/C++, Java) et interprétés (Python, PHP, JavaScript), et place le shell dans le second groupe. **Nuance :** compilation et interprétation décrivent aussi des stratégies d'implémentation ; certains environnements combinent les deux.

Familles citées : `sh`, `csh` (syntaxe proche du C), `bsh` (nom employé pour Bourne Shell dans le support), `tcsh` (complétion et historique), `ksh`, `bash` (*Bourne Again Shell*, libre) et `zsh`. Le PDF présente `ksh` et `zsh` comme des « fusions » : c'est une simplification des influences entre shells, pas une description précise de leur implémentation. Les syntaxes ne sont pas toutes interchangeables.

```bash
bash my_script.sh
```

Ou, avec le droit d'exécution :

```bash
./my_script.sh
```

Pour indiquer l'interpréteur lors de cette seconde forme, placer en toute première ligne :

```bash
#!/bin/bash
```

## VI. Variables — pages 60–62

Les affectations créent implicitement les variables. **Aucun espace autour de `=`.**

```bash
a='Hello'
b=5
c=32.759
echo "$a"
echo "${a}"
```

Le `$` introduit une expansion, et les accolades délimitent le nom, particulièrement utile lorsqu'un suffixe le suit. Les guillemets doubles des affichages sont ajoutés ici pour conserver espaces et caractères spéciaux. Les valeurs sont généralement des chaînes ; Bash propose aussi des attributs particuliers, non développés dans le cours.

## Chaînes et substitution de commandes — pages 63–68

```bash
a=987
b='$a'       # valeur littérale : $a
b="$a"       # valeur développée : 987
b=`ls`       # sortie de la commande ls
b=$(ls)      # autre syntaxe de substitution
```

Le support appelle ces formes « chaînes littérales », « substituées » et « exécutées ». La dernière est une **substitution de commande** : sa sortie standard, privée des sauts de ligne finaux, est utilisée comme valeur.

L'exemple imbriqué de la page 66, avec apostrophes normalisées, est :

```bash
varA=$(ls 'my_file_'$(date '+%Y%m%d'))
```

Il construit un nom tel que `my_file_20261012` à partir de la date d'exécution, puis récupère la sortie de `ls` sur ce nom. Le contre-exemple à accents graves imbriqués est barré dans le PDF : `varB=\`ls -lai 'my_file_'\`date '+%Y%m%d'\`\``. Les délimiteurs se ferment au mauvais endroit ; la syntaxe `$(...)` permet l'imbrication montrée.

Suppression de préfixe ou suffixe selon un motif :

```bash
my_str='A.coucou.Z'
echo "${my_str#*cou}"    # cou.Z : préfixe correspondant le plus court
echo "${my_str##*cou}"   # .Z    : préfixe correspondant le plus long
echo "${my_str%cou*}"    # A.cou : suffixe correspondant le plus court
echo "${my_str%%cou*}"   # A.    : suffixe correspondant le plus long
```

Concaténer revient à juxtaposer :

```bash
a='ABC'
b='DEF'
c="$a$b"                # autre affectation montrée : c=$a$b
echo "$c"               # ABCDEF
```

## Arithmétique entière et réelle — pages 69–71

```bash
a=51
b=-37
echo "la variable a vaut : $a"
echo 'et b vaut : '"${b}"
add=$(( a + b ))
sub=$(( a - b ))
mul=$(( a * b ))
div=$(( a / b ))
mod=$(( a % b ))
echo "$add $sub $mul $div $mod"
```

La sortie arithmétique est `14 88 -1887 -1 14`. Bash effectue ici des opérations entières ; la division tronque vers zéro.

Pour les réels, le support appelle un outil externe :

```bash
a=51.65
b=-37.98
r=`echo "$a+$b" | bc`
```

La valeur obtenue est `13.67`, si `bc` est disponible. La limitation aux entiers concerne l'arithmétique Bash utilisée ici ; elle ne décrit pas tous les shells possibles.

## VII. Branchements conditionnels — pages 72–76

Un `if` teste le **statut de sortie d'une commande** : 0 signifie vrai/succès ; non nul signifie faux/échec.

```text
if commande1; then
    instructions_A
elif commande2; then
    instructions_B
else
    instructions_C
fi
```

`elif` et `else` sont facultatifs. `then` peut être placé sur une ligne distincte ; sur la même ligne que la commande testée, il est précédé d'un point-virgule.

## Opérateurs logiques et commande test — pages 77–83

`commande1 && commande2` n'exécute la seconde commande que si la première réussit. `commande1 || commande2` ne l'exécute que si la première échoue. C'est l'évaluation conditionnelle, dite paresseuse.

```text
if commande1 && commande2; then
    instructions_A
else
    instructions_B
fi

if commande1 || commande2; then
    instructions_A
else
    instructions_B
fi
```

`test expression` effectue une comparaison ; `[ expression ]` en est une autre écriture. Les espaces autour de l'expression et de ses opérateurs sont nécessaires : `[` est une commande et `]` son dernier argument. On peut combiner plusieurs tests avec `&&` et `||`.

## Comparaisons entières — pages 84–85

Pour `a=5`, `b=12` :

| Test | Signification | Forme arithmétique Bash |
| --- | --- | --- |
| `[ "$a" -eq "$b" ]` | Égal | `(( a == b ))` |
| `[ "$a" -ne "$b" ]` | Différent | `(( a != b ))` |
| `[ "$a" -ge "$b" ]` | Supérieur ou égal | `(( a >= b ))` |
| `[ "$a" -gt "$b" ]` | Strictement supérieur | `(( a > b ))` |
| `[ "$a" -le "$b" ]` | Inférieur ou égal | `(( a <= b ))` |
| `[ "$a" -lt "$b" ]` | Strictement inférieur | `(( a < b ))` |

Ces commandes peuvent suivre `if`. Dans le contexte arithmétique, les noms de variables entières peuvent s'écrire sans `$`. Les guillemets des tests entre crochets sont ajoutés pour protéger les expansions ; les tirets typographiques du support sont normalisés en `-`.

## Comparaisons de chaînes — pages 86–89

Avec `a='Coucou'`, `b='Hello'` :

```bash
[ "$a" = "$b" ]
[ "$a" == "$b" ]       # accepté par Bash ; = est la forme portable
[ "$a" != "$b" ]
```

**Erreur de la page 88 :** `[ "$a" > "$b" ]` et `[ "$a" < "$b" ]` déclenchent des redirections shell au lieu des comparaisons voulues. Les formes corrigées sont :

```bash
[ "$a" \> "$b" ]
[ "$a" \< "$b" ]
```

Ou, en syntaxe Bash, `[[ "$a" > "$b" ]]` et `[[ "$a" < "$b" ]]`. L'ordre est lexicographique, avec des détails dépendant de la locale et de la forme de test.

```bash
a='Coucou'
b=''
[ -n "$a" ]            # chaîne non vide : vrai
[ -z "$b" ]            # chaîne vide : vrai
```

## Tests de fichiers et négation — pages 90–92

Pour `my_file='mon_programme.c'`, les tests sont :

| Test | Signification |
| --- | --- |
| `[ -s "$my_file" ]` | Le fichier existe et sa taille est strictement positive |
| `[ -e "$my_file" ]` | La cible existe |
| `[ -f "$my_file" ]` | Fichier ordinaire |
| `[ -d "$my_file" ]` | Répertoire |
| `[ -L "$my_file" ]` | Lien symbolique |
| `[ -r "$my_file" ]` | Lecture autorisée pour l'utilisateur effectif du test |
| `[ -w "$my_file" ]` | Écriture autorisée |
| `[ -x "$my_file" ]` | Exécution ou traversée autorisée |
| `[ -N "$my_file" ]` | Fichier modifié depuis sa dernière lecture, selon ses horodatages |

**Erreur du support :** `-s` ne teste pas une « string déclarée et non vide ». C'est un test de **taille de fichier**. Pour une chaîne non vide, utiliser `-n`.

La négation peut se placer dans l'expression :

```bash
[ ! s1 = s2 ]
[ ! 5 -eq 7 ]
[ ! -d 'mon_fichier.txt' ]
```

L'espace après `!` est nécessaire.

## Branchement case — pages 93–95

`case ... in ... esac` compare une chaîne à des motifs. Un motif est suivi de `)` ; chaque branche se termine ici par `;;`. Les branches sont examinées dans l'ordre, et `*)` sert de défaut.

```text
case "$a" in
    1)        instructions_1 ;;
    2)        instructions_2 ;;
    'Hello')  instructions_hello ;;
    *toto*)   instructions_toto ;;
    ???.txt)  instructions_txt ;;
    "$b.png") instructions_nom ;;
    *)        instructions_defaut ;;
esac
```

Les textes `instructions_...` représentent des blocs à écrire ; ce sont les points de suspension du support remis en forme.

## VIII. Boucles for — pages 96–101

Boucle avec compteur, de 5 à 12 inclus :

```bash
for (( i=5; i<=12; i++ )); do
    echo "$i"
done
```

La source montre aussi `do` sur la ligne suivante ; ce sont deux dispositions alternatives, pas deux `do` à conserver ensemble. Autre écriture Bash :

```bash
for k in {5..12}; do
    echo "$k"
done
```

Itération sur des mots :

```bash
liste='abc def ghi jkl'
for var in $liste; do
    echo "$var"
done
```

L'expansion non protégée de `liste` produit ici quatre mots. La source propose ensuite :

```bash
fichiers=`ls`
for fic in $fichiers; do
    echo "$fic"
done
```

**Limite du dernier exemple :** des noms contenant espaces, tabulations ou sauts de ligne ne sont plus conservés comme des unités. Une expansion non protégée peut aussi développer des motifs de noms.

## Séparateurs et IFS — pages 102–104

`IFS` contrôle le découpage de certaines expansions en champs. Sa valeur par défaut contient espace, tabulation et saut de ligne. Le support propose de sauvegarder la valeur puis de ne garder que le saut de ligne comme séparateur :

```bash
oldIFS=$IFS
IFS=$'\n'
fichiers=`ls`
for fic in $fichiers; do
    echo "$fic"
done
IFS=$oldIFS
```

**Limites et précision ajoutées.** Cette variante gère certains espaces, mais ne rend pas fiable l'analyse de la sortie de `ls`, notamment pour les noms contenant des sauts de ligne. Pour parcourir les entrées ordinaires du répertoire, une forme adaptée est `for fic in ./*; do ...; done`, avec gestion du cas sans correspondance et, si besoin, des fichiers cachés. Le script lancé comme processus séparé ne modifie pas l'`IFS` du shell parent ; un fichier chargé avec `source` ou `.` s'exécute en revanche dans le contexte courant.

## Boucle while — pages 105–108

`while commande; do ...; done` répète le bloc tant que la commande retourne 0. Exemple du compteur **corrigé** : le PDF omet le `$` dans `[ a -le 10 ]`.

```bash
a=1
while [ "$a" -le 10 ]; do
    echo "$a"
    a=$((a+1))
done
```

Lecture d'un fichier ligne par ligne, exemple du support avec guillemets ajoutés :

```bash
fichier='my_file.txt'
while read row; do
    echo "$row"
done < "$fichier"
```

**Précision :** `read` ainsi utilisé traite les antislashs et les espaces selon ses règles. Pour préserver les lignes, on emploie couramment `IFS= read -r row` ; une dernière ligne sans saut de ligne demande un traitement supplémentaire. Le `do` grisé de la page 106 présente à nouveau une autre mise en page, pas une instruction supplémentaire.

## IX. Arguments — pages 109–111

| Paramètre | Contenu |
| --- | --- |
| `$0` | Nom utilisé pour lancer le script |
| `$#` | Nombre d'arguments |
| `$1`, `$2`, `$3`, etc. | Arguments positionnels |
| `${10}`, etc. | Arguments de rang supérieur à 9 |
| `$*`, `$@` | Ensemble des arguments, avec des règles d'expansion différentes |

Affectations du support : `nom_script=$0`, `nb_args=$#`, `arg1=$1`, `arg2=$2`, `arg3=$3`, `all_args=$*` ou `all_args=$@`.

**Précision essentielle :** la mention « identiques en bash » ne vaut pas comme règle générale. `"$@"` conserve **un mot par argument**, y compris les arguments vides ou contenant des espaces ; `"$*"` forme un seul mot joint avec le premier caractère d'`IFS`. Affecter l'ensemble à une variable scalaire ne préserve pas la structure d'une liste d'arguments.

## X. Fonctions — pages 112–117

Deux déclarations sont montrées : `function nom { ...; }` et `nom() { ...; }`. Une fonction s'appelle comme une commande, reçoit des arguments et retourne un statut. **Précision :** une fonction ordinaire s'exécute dans le shell courant ; ce n'est pas automatiquement un processus fils ou un « sous-script » indépendant.

Exemple fidèle, nommé `test` dans le PDF :

```bash
test() {
    if [ "$#" -ge 1 ]; then
        echo 'Il y a 1+ argument(s)'
        return 0
    else
        echo 'argument manquant'
        return 1
    fi
}
```

Ce nom masque la commande habituelle `test` dans le contexte où la fonction est définie ; le test intérieur utilise ici `[`.

```bash
if test; then
    echo 'OK'
else
    echo 'ERROR'
fi

if test 1 2 3; then
    echo 'OK'
else
    echo 'ERROR'
fi
```

Le premier appel affiche `argument manquant`, puis `ERROR`. Le second affiche `Il y a 1+ argument(s)`, puis `OK`.

Récupérer séparément la sortie et le statut :

```bash
var1=`test`
ret1=$?
var2=`test 1 2 3`
ret2=$?
echo "$var1"    # argument manquant
echo "$ret1"    # 1
echo "$var2"    # Il y a 1+ argument(s)
echo "$ret2"    # 0
```

Le statut doit être mémorisé immédiatement, avant qu'une autre commande ne remplace `$?`. La sortie capturée et le statut de retour sont deux informations différentes.

## XI. Commandes courantes — pages 118–126

Les arguments entre chevrons dans le PDF sont des emplacements à remplacer, pas des caractères à saisir.

| Commande | Usage et options cités |
| --- | --- |
| `ls options chemin` | Lister ; `-l` format long, `-a` noms cachés, `-h` tailles lisibles ; un répertoire donne son contenu, un fichier sa description |
| `pwd` | Afficher le chemin absolu du répertoire courant |
| `who` | Lister les utilisateurs connectés |
| `date options format` | Afficher date et heure |
| `file fichier` | Identifier la nature d'un fichier |
| `echo valeur` | Afficher une chaîne |
| `cat fichier` | Afficher le contenu complet |
| `head fichier` | Premières lignes |
| `tail fichier` | Dernières lignes |
| `more fichier` | Affichage paginé |
| `wc fichier` | Compter lignes, mots et octets ; options possibles pour compter les caractères |
| `cd dossier` | Changer de répertoire courant |
| `touch fichier` | Créer un fichier vide s'il manque, sinon actualiser ses horodatages |
| `mkdir dossier` | Créer un répertoire |
| `ln cible nom_lien` | Créer un lien dur ; `-s` pour un lien symbolique |
| `mv source destination` | Déplacer ou renommer |
| `cp source destination` | Copier |
| `rm fichier` | Retirer des fichiers ; options nécessaires pour des répertoires |
| `chmod mode fichier` | Modifier les permissions |
| `tar options fichiers` | Archiver ou extraire : `-c` créer, `-x` extraire, `-v` détailler, `-f` nom d'archive, `-z` compression/décompression gzip |
| `grep motif fichiers` | Filtrer les lignes selon un motif |
| `cut options fichier` | Extraire des champs, caractères ou octets ; choix du séparateur et des champs |
| `sort fichiers` | Trier les lignes, ordre lexical ou numérique, croissant ou décroissant |
| `ps` | Afficher les processus |
| `top` | Afficher leur activité en temps réel |
| `kill pid` | Envoyer un signal à un processus, souvent pour demander sa terminaison |

**Précisions de transcription.** Le PDF résume `wc` comme un compteur de caractères : par défaut, il compte notamment des **octets** ; `-m` demande les caractères. Le séparateur de champs de `cut -d` est un caractère, pas une chaîne arbitraire. `tar -z` désigne gzip, pas tout format de compression. Les noms et options restent ceux présentés dans ce support.
