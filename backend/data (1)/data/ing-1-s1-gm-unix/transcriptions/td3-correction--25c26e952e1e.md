---
source: "ING 1/S1 GM /UNIX/Commande Unix TD & Solutions/td3-correction.pdf"
pages: 9
transcription: texte, questions, réponses, commandes et tableau transcrits et relus
transcription_date: 2026-10-18
verification: comparaison du texte natif et contrôle visuel des neuf pages du PDF
---

# TP3 — La recherche et le tri, corrigé

Inès de Courchelle — 2021–2022.

Les réponses sont celles du support, y compris ses commandes incomplètes. Les apostrophes typographiques, le symbole de début de ligne et le tilde sont rendus par leurs caractères shell. Les écarts de fond sont signalés séparément en fin de transcription.

## Page 1 — Consignes et objectifs

Durant ce TD, l’utilisation de la souris, du Touchpad et du Trackpoint est strictement interdite. Seul le clavier est autorisé.

Objectifs : réaliser des recherches ciblées sur des noms et contenus de fichiers ; trier des données suivant des critères définis ; connaître les commandes distantes et se familiariser avec elles.

Fichiers attachés : `hp1.txt`, `soccer.csv`.

### 1. Exercices — 1.1. Find et grep

**1.** Lister les lignes de `hp1.txt` contenant le chiffre 1 ; afficher ce chiffre en rouge.

```sh
grep --color=always 1 hp1.txt
```

**2.** Faire apparaître au début de chaque ligne son numéro dans le fichier d’origine.

```sh
grep --color=always -n 1 hp1.txt
```

**3.** Afficher les lignes contenant le chiffre 1 ou la lettre V (le sujet écrit « le chiffre V »).

```sh
grep --color=always -n [1V] hp1.txt
grep --color=always -n '1\|V' hp1.txt
```

## Page 2 — Find et grep, suite

**4.** Afficher `hp1.txt` avec les numéros de ligne, sans `grep`.

```sh
cat -n hp1.txt
```

**5.** Chercher `hp1.txt` depuis le répertoire de connexion.

```sh
find ./ -name "hp1.txt"
```

**6.** Avec `find` et `ls -l`, vérifier ses droits d’accès.

```sh
find ./ -name "hp1.txt" -exec ls -l {} \;
```

**7.** Avec `find` et `grep`, afficher les lignes contenant 1 ou V, avec les motifs trouvés en couleur.

```sh
find ./ -name "hp1.txt" -exec grep --color=always '[1V]' {} \;
find ./ -name "hp1.txt" -exec grep --color=always '1\|V' {} \;
```

**8.** Avec `find` et `mv`, renommer le fichier en `HarryPotter.txt`.

```sh
find ./ -name "hp1.txt" -exec mv {} HarryPotter.txt \;
```

## Page 3 — Filtrage et comptage

**9(a).** Sur combien de lignes de `HarryPotter.txt` le mot `muggles` apparaît-il, sans tenir compte de la casse ?

```sh
grep -i muggles HarryPotter.txt -c
```

**9(b).** Extraire les lignes vides, ne contenant pas de blancs, dans `hp1bis.txt`.

```sh
grep "^$" HarryPotter.txt > hp1bis.txt
```

Le corrigé précise qu’une ligne contenant seulement des tabulations ou espaces n’est pas vide et propose `"^ *$"` pour inclure les lignes de blancs.

**9(c).** Éliminer les lignes vides et écrire le résultat dans `hp1ter.txt`.

```sh
grep -v "^$" HarryPotter.txt > hp1ter.txt
```

**9(d).** « Vérifier que les sommes de hp1bis.txt et hp1ter.txt sont bien égale. »

```sh
wc -l HarryPotter.txt ; wc -l hp1bis.txt ; wc -l hp1ter.txt
```

**10.** Compter les éléments du répertoire `/etc`.

```sh
ls -r1 /etc | wc -l
```

**11.** Compter uniquement les fichiers de `/etc`.

```sh
ls -r1 /etc | grep "^-" | wc -l
```

## Page 4 — Recherche du login

**12.** Chercher le login dans les fichiers de configuration de `/etc`, sans parcourir ses sous-répertoires. Le login utilisé dans la réponse est `eisti`.

```sh
grep "eisti" /etc/*
```

**13.** Supprimer les messages d’erreur tels que « permission denied » ou fichier/répertoire introuvable. Indice du sujet : redirection des erreurs.

```sh
grep "eisti" /etc/* 2>/dev/null
```

**14.** Étendre la recherche aux sous-répertoires de `/etc`.

```sh
grep -R "eisti" /etc/* 2>/dev/null
```

## Page 5 — 1.2. Le traitement des données

**1(a).** Trier `soccer.csv` par ordre alphabétique des joueurs.

```sh
sort -k1 soccer.csv
```

**1(b).** Trier par note (« Rating », dixième colonne) décroissante. Le corrigé donne d’abord `sort -k10nr soccer.csv`, puis précise que cette commande ne marche pas sans indiquer le délimiteur des colonnes.

```sh
sort -t',' -k10nr soccer.csv
sort -t',' -k10nr soccer.csv | cut -d',' -f10,1
```

La seconde commande est proposée pour vérifier le résultat.

**1(c).** Trier par nom d’équipe, cinquième colonne.

```sh
sort -k5 soccer.csv
```

**2.** Filtrer les joueurs du Real Madrid et afficher uniquement les prénoms.

```sh
grep -wi "Real Madrid" soccer.csv | cut -d',' -f1
```

**3.** Créer `joueurs.txt` avec les joueurs du Real Madrid triés par ordre alphabétique de nom.

```sh
grep -wi "Real Madrid" soccer.csv | sort -k1 | cut -d',' -f1 > joueurs.txt
```

## Page 6 — 1.3. Les protocoles de communications

Le compte créé à l’école permet de consulter les mails, de se connecter sur AREL et de sauvegarder ses données.

**1.** Se connecter à une machine de l’école via la machine nommée `ssh`. La réponse indique seulement les destinations : `login@ssh.pau.eisti.fr` pour Pau et `login@ssh.cergy.eisti.fr` pour Cergy.

**2.** Compter les personnes connectées sur cette machine. Indice : `who`.

```sh
who | sort | cut -f1 -d ' ' | uniq | wc -l
```

**3.** Créer dans le répertoire de connexion local un fichier nommé `monMemo.txt`. Réponse du support :

```sh
touch memo.txt
```

**4.** Copier `monMemo.txt` dans le répertoire personnel du compte distant.

```sh
scp monMemo.txt login@ssh.pau.eisti.fr:.
scp monMemo.txt login@ssh.pau.eisti.fr:~
```

**5.** Copier l’ensemble du répertoire `CommandesUnix` sur le compte distant.

```sh
scp -r CommandesUnix login@ssh.pau.eisti.fr:.
scp -r CommandesUnix login@ssh.pau.eisti.fr:
```

**6.** Créer `thisIsTheInternet.txt` sur le compte distant, puis le télécharger dans le répertoire local `CommandesUnix`.

```sh
touch thisIsTheInternet.txt
scp login@ssh.pau.eisti.fr:thisIsTheInternet.txt ~/CommandesUnix/
```

La première commande s’effectue sur le compte distant ; la seconde depuis la machine locale. Les espaces typographiques autour des deux-points des adresses `scp` sont supprimés dans ces commandes.

## Page 7 — Connexions et révision

**7.** Afficher les utilisateurs connectés sur la même machine et la date du dernier démarrage.

```sh
who -b -u
```

**8.** Créer un fichier `toto` sur le compte distant et y ajouter du texte. À quoi sert `vi` ? Réponse : cet éditeur permet de se passer d’interface graphique, car, selon le support, les comptes distants ne permettent pas de lancer des commandes graphiques.

### 2. Et si je révisai !

**1.** Différence entre `find` et `grep` : `find` recherche un nom de fichier ; `grep` recherche une chaîne de caractères dans des fichiers.

**2(a).** Trouver le mot `tux` dans `monCours.txt`.

```sh
grep --color=always "tux" monCours.txt
```

**2(b).** « Compter le nombre de fois où le mot tux apparaît. »

```sh
grep --color=always "tux" monCours.txt -c
```

**2(c).** Afficher les lignes contenant le chiffre 4 ou la lettre t.

```sh
grep --color=always -n [4t] monCours.txt
```

## Page 8 — Révision, suite

**3.** Rechercher `reponsePartiel.txt` depuis le répertoire personnel et compter ses lignes. Réponse incomplète du support :

```sh
find ./ -name "reponsePartiel.txt" -exec wc -l
```

**4.** Rechercher le mot `Eisti` dans `/etc` et ses sous-répertoires. Réponses du support :

```sh
grep -wi eisti /etc
grep eisti /etc
```

**5.** Différence entre un pipe classique et `exec` : dans le contexte de `find`, `exec` permet d’effectuer des commandes sur tous les fichiers recherchés ; le pipe redirige la sortie d’une commande vers l’entrée d’une autre.

**6.** Fichier `notes.txt` :

```text
5896 Java       14 15
4589 BD         20 1
7415 Algorithme 17 3
4568 Pascal     8 20
4567 Web        15 7
```

**6(a).** Copier `notes.txt`, situé dans le répertoire courant, sur le compte distant dans `monAnnee`. Réponse du support, avec ses espaces :

```sh
scp notes.txt login@ssh.pau.eisti.fr : /monAnnee/.
```

**6(b).** Trier par note décroissante, troisième colonne.

```sh
sort -k3nr notes.txt
```

## Page 9 — Tri des notes, suite

**6(c).** Trier par ordre croissant des intitulés de matière.

```sh
sort -k2d notes.txt
sort -k2 notes.txt
```

**6(d).** Trier par classement croissant, quatrième colonne, puis afficher uniquement les matières.

```sh
sort -k4n notes.txt | cut -d " " -f2
```

**6(e).** Chercher la matière Algorithme et afficher le résultat en majuscules.

```sh
grep -wi Algorithme notes.txt | tr [:lower:] [:upper:]
```

## Écarts relevés dans le document source

- Page 3, question 9(b) : `^ *$` inclut les lignes d’espaces, mais pas celles contenant des tabulations. Le motif `^[[:blank:]]*$` couvrirait les deux.
- Page 3, question 9(d) : le contrôle attendu est l’égalité entre le nombre de lignes initial et la somme des nombres de lignes des deux fichiers obtenus.
- Page 3, question 11 : `ls -r1` affiche les noms et ne fournit pas les caractères de type de fichier du format long. Le filtre `^-` ne compte donc pas les fichiers ordinaires ; il faudrait notamment utiliser le format `ls -l` pour cette approche.
- Page 5, question 1(c) : le tri de la cinquième colonne du CSV nécessite le délimiteur `-t','`, comme pour la dixième colonne.
- Page 6, question 1 : les destinations doivent être précédées de la commande `ssh`. Question 3 : `touch memo.txt` ne crée pas le fichier `monMemo.txt` demandé.
- Page 7, question 2(b) : `grep -c` compte les lignes correspondantes, pas toutes les occurrences si une ligne en contient plusieurs.
- Page 8, question 3 : la réponse omet le fichier et le terminateur de `-exec` ; une commande complète est `find ./ -name "reponsePartiel.txt" -exec wc -l {} \;`.
- Page 8, question 4 : les deux réponses omettent la récursivité ; `grep -Rwi eisti /etc` correspond à la recherche demandée sans distinction de casse.
- Page 8, question 6(a) : la destination `scp` doit être un seul argument. Pour un dossier du répertoire personnel distant, on peut écrire `scp notes.txt login@ssh.pau.eisti.fr:monAnnee/`. Le chemin `/monAnnee/` du support désigne au contraire un chemin absolu.
- Page 9, question 6(d) : `cut -d " " -f2` suppose un seul espace entre les champs ; avec l’alignement par blancs multiples, le champ peut être vide. Question 6(e) : les classes de `tr` devraient être protégées par des quotes : `tr '[:lower:]' '[:upper:]'`.
- Les motifs non protégés `[1V]` et `[4t]` peuvent subir l’expansion des noms de fichiers par le shell. Les écrire `'[1V]'` et `'[4t]'` évite cette ambiguïté.
