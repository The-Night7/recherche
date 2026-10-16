---
source: "ING 1/S1 GM /UNIX/Examen/Corrige_DS-2017-2018_Unix-DS.pdf"
pages: 3
transcription: énoncés, commandes, tableau et script transcrits et relus
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle des trois pages du PDF
---

# Commandes Unix — Examen corrigé de janvier 2019

EISTI, Cergy–Pau. Cycle ingénieur, première année. L’équipe enseignante. Durée : une heure. Trois pages.

**Écart de date :** le nom du fichier indique 2017–2018 ; l’en-tête du PDF indique janvier 2019.

## Modalités — page 1

Épreuve sur papier, aucun document autorisé. Rédiger exclusivement au stylo à encre. Déplacements et échanges interdits. Aucune question aux enseignants ; poser des hypothèses en cas de doute.

## Exercice 1 — 11 points — pages 1 et 2

L’utilisateur **Jimmy** vient de se connecter et se trouve dans `/home/Jimmy`. Les réponses du corrigé, en vert dans le PDF, sont reproduites sous chaque question.

1. Afficher le contenu de `/home/Jimmy`, fichiers récemment modifiés en premier — 0,5 point.

```sh
ls -lt
# ou
ls -t
```

2. Créer en une commande un répertoire `Cours` avec un sous-répertoire `Unix` — 1 point.

```sh
mkdir -p Cours/Unix
```

Barème du corrigé : 1 point pour la réponse correcte ; 0,5 point si plusieurs commandes sont utilisées.

3. Créer quatre fichiers `TD1`, `TD2`, `TD3`, `TD4` « à l’intérieur du sous-répertoire Cours » — 1 point. Le corrigé les place dans `Cours/Unix` :

```sh
touch Cours/Unix/TD1
touch Cours/Unix/TD2
touch Cours/Unix/TD3
touch Cours/Unix/TD4
```

4. Modifier en une commande les droits de tous ces fichiers : `rwxr–r–` dans la source, soit `rwxr--r--` — 1 point.

```sh
chmod 744 Cours/Unix/TD*
```

5. Écrire « Para bailar » dans `TD1` et « La Bamba » dans `TD2` — 1 point. La source juxtapose les deux commandes sans séparateur :

```sh
echo "Para bailar" > Cours/Unix/TD1 echo "La Bamba" > Cours/Unix/TD2
```

6. Compter les lignes de `TD1` — 0,5 point.

```sh
wc -l TD1
```

7. Afficher le contenu de `Cours/Unix` avec des signes distinctifs permettant d’identifier le type des fichiers — 0,5 point.

```sh
ls -F
```

**Page 2 :**

8. Supprimer `TD1` — 0,5 point.

```sh
rm Cours/Unix/TD1
```

9. Renommer `TD3` en « Rictchie » dans l’énoncé ; le corrigé écrit `Ritchie` — 1 point.

```sh
mv Cours/Unix/TD3 Cours/Unix/Ritchie
```

10. Copier `Ritchie` dans `Cours` — 1 point.

```sh
cp Cours/Unix/Ritchie Cours/
```

11. Rechercher `TD4` et le renommer `notes`, en une seule commande — 1,5 point.

```sh
find ./ -name TD4 -exec mv {} Cours/Unix/notes \;
```

12. Rechercher le mot `Jimmy` dans `etc/` et ses sous-répertoires — 1,5 point. Réponses de la source :

```sh
grep -wi Jimmy /etc/*
grep Jimmy /etc/*
```

## Exercice 2 — 5 points — page 2

Fichier `notes.txt` de Jimmy :

| Identifiant de matière | Intitulé | Note | Classement |
| --- | --- | ---: | ---: |
| 5896 | Java | 14 | 15 |
| 4589 | BD | 20 | 1 |
| 7415 | Algorithme | 17 | 3 |
| 4568 | Pascal | 8 | 20 |
| 4567 | Web | 15 | 7 |

1. Trier par note décroissante — 1 point.

```sh
sort -k3nr notes.txt
```

2. Trier par ordre sur l’intitulé des matières — 1 point.

```sh
sort -k2d notes.txt
# ou
sort -k2 notes.txt
```

3. Trier par classement croissant, quatrième colonne, et afficher seulement les matières — 1,5 point.

```sh
sort -k4n notes.txt | cut -d " " -f2
```

4. Chercher `Algorithme` et afficher le résultat en majuscules — 1,5 point. La source annonce « Deux solutions acceptées », mais n’imprime qu’une ligne :

```sh
grep -wi Algorithme notes.txt | tr [ :lower :] [ :upper :]
```

## Exercice 3 — 4 points — pages 2 et 3

Écrire un script prenant un fichier `F1.txt` en argument, par exemple `./test.sh F1.txt` :

1. Afficher le nombre d’arguments et vérifier qu’il vaut un — 2 points.
2. Créer `Partiel`, chercher le fichier dans le répertoire courant et le déplacer dans `Partiel` — 2 points.

**Script de la source, page 3 :**

```sh
#!/bin/sh
echo "Le nombre d'argument passé en paramètre est égal à $#"

if [ $# != 1 ]
then
        echo "Le nombre d'argument passé en paramètre est différent de 1"
        exit 2
fi
mkdir -p Partiel
find . -iname $1 -exec mv{} Partiel \;
```

## Notes de transcription sur les commandes du corrigé

- Exercice 1.5 : les deux `echo` doivent être séparés par un retour à la ligne ou un point-virgule pour réaliser les deux écritures demandées.
- Exercice 1.6–7 : `wc -l TD1` et `ls -F` supposent d’être dans `Cours/Unix`, alors que l’énoncé place initialement l’utilisateur dans `/home/Jimmy`. Depuis ce répertoire initial, utiliser les chemins `Cours/Unix/TD1` et `Cours/Unix`.
- Exercice 1.12 : les commandes imprimées ne parcourent pas récursivement les sous-répertoires ; l’option `-r` est nécessaire pour cette demande.
- Exercice 2.3 : `cut -d " " -f2` suppose un seul espace délimiteur ; plusieurs espaces ou des tabulations changent les champs obtenus.
- Exercice 2.4 : les classes de caractères attendues sont `'[:lower:]'` et `'[:upper:]'`, sans espaces internes.
- Exercice 3 : il manque une espace entre `mv` et `{}` ; l’argument `$1` doit être protégé par des guillemets pour conserver les noms contenant des espaces. La recherche peut aussi rencontrer le fichier déjà déplacé dans `Partiel`. Le code imprimé est conservé, sans présenter ces erreurs comme des commandes corrigées.
