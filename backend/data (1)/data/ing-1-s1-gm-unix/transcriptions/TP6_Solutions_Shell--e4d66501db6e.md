---
source: "ING 1/S1 GM /UNIX/Commande Unix TD & Solutions/TP6_Solutions_Shell.pdf"
pages: 3
transcription: texte et scripts transcrits et relus
transcription_date: 2026-10-16
verification: comparaison du texte natif et lecture visuelle des trois pages du PDF
---

# TP6 — Programmation en Shell : solutions

Les dix solutions du PDF sont transcrites ci-dessous. Les commandes sont celles de la source.

## 1. Tri d’un fichier de notes (sans trier l’entête) — page 1

```bash
#!/bin/bash
head -n 1 "$1"
tail -n +2 "$1" | sort
```

## 2. Répartir les fichiers par extension — page 1

```bash
#!/bin/bash
for file in *.*; do
     ext="${file##*.}"
     mkdir -p "$ext"
     mv "$file" "$ext/"
done
```

## 3. Ajout des options (-h, -d, -v) avec getopts — page 1

```bash
#!/bin/bash
verbose=0
rep="."

usage() {
    echo "Usage: $0 [-h] [-d repertoire] [-v]"
    exit 1
}

while getopts "hd:v" opt; do
     case $opt in
          h) usage ;;
          d) rep=$OPTARG ;;
          v) verbose=1 ;;
          *) usage ;;
     esac
done

for file in "$rep"/*.*; do
     ext="${file##*.}"
     [ $verbose -eq 1 ] && echo "Déplacement de $file vers $ext/"
     mkdir -p "$rep/$ext"
     mv "$file" "$rep/$ext/"
done
```

## 4. Traitement avec sed — page 1

```bash
# Remplacer ';' par '!'
sed 's/;/!/g' fichier.txt

# Remplacer 't' en début de ligne par 'T'
sed 's/^t/T/' fichier.txt

# Remplacer ' /' par ','
sed 's/ \/,/' fichier.txt

# Remplacer '/' par '+' et ';' par '@'
sed -e 's/\//+/g' -e 's/;/@/g' fichier.txt

# Supprimer lignes 2 à 4
sed '2,4d' fichier.txt

# Commandes données
sed -e 's/^\(\.\)/\1\1/g' fichier.txt
sed -e 's/^\(\.\)/\1\1\1\1/g' fichier.txt
```

## 5. Vérifier un login et afficher ses groupes — page 2

```bash
#!/bin/bash
while true; do
     read -p "Entrez un login (ou 'quit' pour arrêter): " login
     [ "$login" = "quit" ] && break
     if id "$login" >/dev/null 2>&1; then
          groups "$login"
     else
          echo "Login inexistant"
     fi
done
```

## 6. Informations sur un fichier — page 2

```bash
#!/bin/bash
file=$1
echo "Nom : $file"
echo "Taille : $(stat -c%s "$file")"
echo "md5sum : $(md5sum "$file" | awk '{print $1}')"
echo "cksum : $(cksum "$file" | awk '{print $1}')"
```

## 7. Informations sur tous les fichiers d’un répertoire — page 2

```bash
#!/bin/bash
for f in "$1"/*; do
     ./exo6.sh "$f"
done
```

## 8. Appliquer un script à tous les sous-répertoires — page 2

```bash
#!/bin/bash
script=$1
dir=$2

for sub in "$dir"/*; do
     [ -d "$sub" ] && $script "$sub"
done
```

## 9. Informations sur tous les fichiers d’une arborescence — page 2

```bash
#!/bin/bash
find . -type f | while read f; do
     ./exo6.sh "$f"
done
```

## 10. Détection de doublons — page 2–3

```bash
#!/bin/bash
tmpfile=$(mktemp)

find . -type f | while read f; do
    size=$(stat -c%s "$f")
    md5=$(md5sum "$f" | awk '{print $1}')
    cksumv=$(cksum "$f" | awk '{print $1}')
    echo "$f|$size|$md5|$cksumv"
done | sort -t'|' -k2,4 > "$tmpfile"

awk -F"|" '
{
    key=$2 FS $3 FS $4
    if (seen[key] != "")
        print "Doublon trouvé : " $1 " et " seen[key]
    else
        seen[key]=$1
}' "$tmpfile"

rm "$tmpfile"
```

## Notes de transcription

- Exercice 4 : la source écrit `sed 's/ \/,/' fichier.txt`. Cette expression manque d’un séparateur ; pour remplacer l’espace suivi de `/` par une virgule, on peut écrire `sed 's| /|,|' fichier.txt`. La commande source est conservée dans le bloc.
- Les boucles sur des motifs glob conservent le motif littéral si aucun nom ne correspond, sans option `nullglob`. Les scripts ne traitent pas tous les noms de fichiers possibles (notamment les retours à la ligne dans les exercices 9 et 10) et n’excluent pas systématiquement les répertoires. Ce sont les solutions simplifiées du support.
