---
source: "ING 1/S1 GM /UNIX/Examen/Corrige_Examen_Unix_2024-2025.pdf"
pages: 5
transcription: questions, réponses et scripts transcrits et relus
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle des cinq pages du PDF
---

# Corrigé complet — Examen Commandes Unix 2024–2025

CY Tech — ING 1 GI/GM. Durée : une heure. Les commandes et explications sont celles du corrigé fourni. Les erreurs identifiées sont signalées à la fin.

## Exercice 1 (5pts): Questions de cours — pages 1–2

### 1.1 Que représentent ~ et / ? (0.5pt)

Réponse:

- ~ : Représente le répertoire personnel (home directory) de l'utilisateur courant. Par exemple: /home/user

- / : Représente la racine du système de fichiers Unix (root directory). C'est le point de départ de toute l'arborescence.

### 1.2 Comment obtenir la description d'une commande ? (0.5pt)

Réponse:
Utiliser la commande man suivie du nom de la commande.
Exemple: man ls
On peut aussi utiliser: man -k mot_clé pour chercher dans les manuels.

### 1.3 Que donne la commande ls -R ? (0.5pt)

Réponse: Une liste récursive de tous les sous-dossiers
L'option -R (Recursive) permet de lister le contenu du répertoire courant ET de tous ses sous-répertoires de manière récursive.

### 1.4 À quoi correspond le caractère | ? (0.5pt)

Réponse: Un moyen de communication inter-processus
Le pipe (|) redirige la sortie standard d'une commande vers l'entrée standard d'une autre commande. C'est un mécanisme de communication entre processus.
Exemple: ls -l | wc -l (compte le nombre de fichiers)

### 1.5 Permissions -rw-r--r-- pour le propriétaire ? (0.5pt)

Réponse: De lecture et d'écriture
Décomposition: -rw-r--r--

- 1er caractère (-): fichier normal

- rw- : propriétaire → lecture (r) et écriture (w), pas d'exécution

- r-- : groupe → lecture seulement

- r-- : autres → lecture seulement

### 1.6 Créer un lien symbolique ? (1pt)

Réponse: ln -s
Syntaxe complète: ln -s fichier_cible nom_du_lien
Exemple: ln -s /chemin/vers/fichier.txt mon_lien

### 1.7 Se connecter au système par réseau en mode texte ? (0.5pt)

Réponse: telnet ou ssh
En pratique, ssh est préféré car il est sécurisé (crypté). telnet est obsolète et non sécurisé.
Exemple: ssh user@hostname

### 1.8 Conversion permissions numériques → symboliques (1pt)

Réponse:

- 745 toto → rwxr--r-x (correct)
7=rwx (proprio: lecture+écriture+exéc), 4=r-- (groupe: lecture), 5=r-x (autres: lecture+exéc)

- 621 titi → rw--w---x (correct mais inhabituel)

6=rw- (proprio: lecture+écriture), 2=-w- (groupe: écriture seule), 1=--x (autres: exéc seule)

- 780 tutu → rwxrwx--- (correct)
7=rwx (proprio: tous droits), 8=invalide! → devrait être 7=rwx (groupe), 0=--- (autres: aucun)
Note: 780 est INCORRECT car 8 n'existe pas (max=7). Devrait être 770.

## Exercice 2 (6pts): Fichiers et répertoires — pages 2–3

### 2.1 Créer répertoires Supports/Unix hiérarchique (0.5pt)

Réponse: mkdir -p Supports/Unix
L'option -p (parents) crée tous les répertoires intermédiaires nécessaires. mkdir -p Supports/Unix

### 2.2 Créer deux fichiers TP1 et TP2 dans Supports (0.5pt)

Réponse:

```bash
touch Supports/TP1
touch Supports/TP2
# Ou en une seule commande:
touch Supports/TP1 Supports/TP2
```

### 2.3 Déplacer TP1 et TP2 dans Unix (0.5pt)

Réponse:

```bash
mv Supports/TP1 Supports/Unix/
mv Supports/TP2 Supports/Unix/
# Ou en une seule commande:
mv Supports/TP1 Supports/TP2 Supports/Unix/
```

### 2.4 Renommer TP1→TPunix1 et TP2→TPunix2 (0.5pt)

Réponse:

```bash
mv Supports/Unix/TP1 Supports/Unix/TPunix1
mv Supports/Unix/TP2 Supports/Unix/TPunix2
```

### 2.5 Supprimer Supports et son contenu (0.5pt)

Réponse:

```bash
rm -rf Supports/
# -r : récursif (sous-répertoires)
# -f : force (pas de confirmation)
```

### 2.6 Supprimer un répertoire vide ? (0.5pt)

Réponse:

```bash
rmdir nom_repertoire
# rmdir ne fonctionne QUE sur les répertoires vides
```

### 2.7 Rediriger la sortie d'erreur standard ? (0.5pt)

Réponse:

```bash
commande 2> fichier_erreurs.txt
# 2> redirige le flux d'erreur (stderr)
# Exemple pour ignorer les erreurs:
commande 2>/dev/null
```

### 2.8 Fichier ING12024_2025.csv

#### a) Compter le nombre d'étudiants (0.5pt)

```bash
wc -l ING12024_2025.csv
# Compte le nombre de lignes
# Si le fichier a une ligne d'en-tête, soustraire 1
```

#### b) Visualiser par ordre décroissant et pourquoi ? (0.5pt)

Réponse: Utiliser sort avec less ou more
Pourquoi ? Le fichier contient tous les étudiants ING1, donc potentiellement plusieurs centaines de lignes. Il est préférable d'utiliser un visualiseur page par page plutôt que cat qui afficherait tout d'un coup.

```bash
sort -r ING12024_2025.csv | less
# -r : ordre décroissant (reverse)
# less : visualisation page par page
```

#### c) Trouver le chemin absolu puis afficher les droits (1pt)

```bash
find ~ -name ING12024_2025.csv -exec ls -l {} \;
# OU en deux étapes:
find ~ -name ING12024_2025.csv                 # Trouve le chemin
# Puis avec le chemin obtenu:
ls -l /chemin/vers/ING12024_2025.csv
```

#### d) Seul le propriétaire a tous les droits (0.5pt)

```bash
chmod 700 ING12024_2025.csv
# 7 = rwx pour le propriétaire
# 0 = --- pour le groupe
# 0 = --- pour les autres
```

## Exercice 3 (4pts): Lecture des fichiers — pages 3

### 3.1 Fichier Doc.txt

#### a) Lignes commençant par majuscule (0.5pt)

```bash
grep '^[A-Z]' Doc.txt
# ^ : début de ligne
# [A-Z] : une majuscule
```

#### b) Supprimer lignes vides → DocCondense.txt (0.5pt)

```bash
grep -v '^$' Doc.txt > DocCondense.txt
# -v : inverse (lignes qui ne correspondent PAS)
# ^$ : ligne vide (début puis fin sans rien entre)
# OU avec sed:
sed '/^$/d' Doc.txt > DocCondense.txt
```

#### c) Remplacer Test → Test1 → DocFinal.txt (0.5pt)

```bash
sed 's/Test/Test1/g' DocCondense.txt > DocFinal.txt
# s/ : substitution
# g : global (toutes les occurrences)
```

### 3.2 Permissions: proprio(rwx), groupe(x), autres(rien) (0.5pt)

```bash
chmod 710 DocFinal.txt
# 7 = rwx (propriétaire: tous droits)
# 1 = --x (groupe: exécution seule)
# 0 = --- (autres: aucun droit)
```

### 3.3 Connexion à canard.volatiles.org en dupont-dupont (0.5pt)

```bash
ssh dupont-dupont@canard.volatiles.org
```

### 3.4 Copier DocFinal.txt → DocFinalBis.txt sur distant (0.5pt)

```bash
scp DocFinal.txt dupont-dupont@canard.volatiles.org:~/DocFinalBis.txt
# Syntaxe: scp source user@host:destination
```

### 3.5 Fichier Info.txt

#### a) Trier par score décroissant, afficher que noms (0.5pt)

```bash
sort -t':' -k3nr Info.txt | cut -d':' -f1
# -t':' : délimiteur = deux-points
# -k3 : tri sur colonne 3 (score)
# n : numérique
# r : reverse (décroissant)
# cut -d':' -f1 : extrait champ 1 (nom)
```

#### b) Remplacer : par espace, sauf lignes 4,5,6 → InfoModified.txt (0.5pt)

```bash
sed '4,6d; s/:/\ /g' Info.txt > InfoModified.txt
# 4,6d : supprime lignes 4 à 6
# s/:/ /g : remplace : par espace (partout)
# Note: l'espace doit être échappé ou entre quotes
```

## Exercice 4 (5pts): Script shell — pages 3–5

### 4.1 Que fait ce programme ? (2pts)

```bash
#!/bin/bash
cmpt=1

cm=3
echo -n " Tapez votre psw : "
read psw
while [ "$psw" != "UNIX-EXAM." ] && [ "$cmpt" -ne 4 ]
do
     echo "Erroné, plus que "$cm" chance(s): "
     read psw
     cmpt=$(($cmpt+1))
     cm=$(($cm-1))
done
echo "Accès bloqué !!"
```

Réponse:
Ce script implémente un système de vérification de mot de passe avec 3 tentatives.

Fonctionnement détaillé:

1. Initialise un compteur (cmpt=1) et un compteur de chances restantes (cm=3)
2. Demande à l'utilisateur de saisir un mot de passe
3. Entre dans une boucle WHILE qui continue tant que:

- Le mot de passe saisi n'est PAS "UNIX-EXAM." ET

- Le compteur n'a pas atteint 4 (donc max 3 tentatives)
4. À chaque tentative incorrecte:

- Affiche le nombre de chances restantes

- Incrémente le compteur de tentatives

- Décrémente le compteur de chances

- Redemande le mot de passe
5. Après la boucle (3 échecs ou mot de passe correct), affiche "Accès bloqué !!"

Note: Le script a un défaut: il affiche "Accès bloqué !!" même si le mot de passe est correct. Il faudrait ajouter un test après la boucle pour distinguer les deux cas.

### 4.2 Script avec menu interactif (3pts)

Réponse:

```bash
#!/bin/bash
# Demande le nom de l'utilisateur
echo -n "Entrez votre nom: "
read nom
echo "Bonjour $nom !"
echo ""
# Affiche le menu
echo "---------------------------------"
echo "Menu :"
echo "1. Afficher la date et l'heure"
echo "2. Afficher les fichiers du répertoire courant"
echo "3. Quitter"
echo "---------------------------------"
# Lit le choix
read -p "Votre choix: " choix
# Traite le choix avec case
case $choix in
     1)
        echo "Date et heure actuelles:"
        date
        ;;
     2)
        echo "Fichiers du répertoire courant:"
        ls -l
        ;;
     3)
        echo "Au revoir $nom !"
        exit 0
        ;;
     *)
        echo "Choix invalide !"
        exit 1
        ;;
esac
```

Explications:

- read nom : lit l'entrée utilisateur

- read -p "texte: " var : lit avec un prompt

- case $choix in ... esac : structure de menu

- 1) ... ;; : cas numéro 1

- *) ... ;; : cas par défaut (autre choix)

- exit 0 : sortie normale

- exit 1 : sortie avec erreur

## Fin du corrigé — page 5

Points clés à retenir pour l'examen:

1. Toujours mettre des espaces autour des [ ] dans les tests
2. Mettre les variables entre guillemets dans les tests: [ "$var" = "valeur" ]
3. Ne pas oublier le shebang #!/bin/bash au début des scripts
4. Utiliser -p avec mkdir pour créer des hiérarchies
5. L'option -R de find/grep/chmod signifie récursif
6. sort -t pour spécifier le délimiteur, -k pour la colonne, -n pour numérique, -r pour inverse
7. grep -v pour inverser (lignes qui ne correspondent PAS)
8. sed 's/old/new/g' pour remplacer (g = global)
9. Permissions: r=4, w=2, x=1 → additionner pour obtenir le chiffre
10. 2> pour rediriger les erreurs, 2>/dev/null pour les ignorer

## Notes de transcription sur les incohérences du corrigé

- Question 1.4 : `ls -l | wc -l` compte les lignes affichées, y compris la ligne `total` habituelle de `ls -l` ; cela ne donne pas en général exactement le nombre de fichiers.
- Question 1.8 : la mention « 780 tutu → rwxrwx--- (correct) » est contredite par la note immédiatement suivante. `780` n’est pas une permission octale valide ; `rwxrwx---` correspond à `770`.
- Question 3.5.b : `4,6d` supprime les lignes 4 à 6. Si « sauf lignes 4,5,6 » signifie les conserver sans remplacement, la commande attendue serait `sed '4,6!s/:/ /g' Info.txt > InfoModified.txt`. L’espace dans les apostrophes n’a pas besoin d’une barre oblique inverse.
- Question 4.1 : le programme lit une première saisie avant la boucle puis jusqu’à trois nouvelles saisies dans la boucle, soit **quatre saisies au maximum**, et non trois comme annoncé dans l’explication. Le `read` de chaque tour précède les mises à jour des compteurs. La remarque de la source sur « Accès bloqué !! » affiché même après succès est conservée.
- Récapitulatif, point 5 : `find` descend récursivement par défaut ; il ne possède pas l’option générale `-R` présentée ici pour la récursivité. Cette option concerne notamment `grep` et `chmod`.
