---
source: "ING 1/S1 GM /UNIX/TD_TP_Sys.exploitation/TP4/Solutions TP4 partie3.txt"
pages: 0
transcription: fichier texte natif intégral remis en forme, commandes et commentaires conservés
transcription_date: 2026-10-16
verification: lecture intégrale et comparaison avec le fichier texte source
---

# TP4 — Solutions, partie 3

Les indications, commandes et versions sont celles du support historique. Aucune commande n’a été exécutée pour cette transcription.

## Environnement des exercices

- **2.1, 2.2 et 3.1 :** travailler sous Linux sur la machine physique ou sur la machine virtuelle.
- **3.2, installation de Haroopad :** utiliser la machine physique sous Linux, car l’interface graphique est nécessaire.
- **4.1 :** utiliser la machine physique sous Linux ; le dossier GitHub à télécharger est plus facile à récupérer avec son navigateur et son interface graphique.
- **4.2 :** utiliser la machine virtuelle.

## Problèmes rencontrés lors de l’installation du PPA

### 3.1. Ajouter le dépôt

```sh
sudo add-apt-repository ppa:<nom_du_dépôt>
sudo apt update
```

Faire ensuite les commandes suivantes, reproduites à cet endroit du fichier source :

```sh
docker system df # which can show disk usage and size of ‘Build Cache’
docker image prune # add -f or --force to not prompt for confirmation
docker container prune # add -f or --force to not prompt for confirmation
```

### 3.1. Examiner et retirer le dépôt

```sh
ls -l /etc/apt/sources.list.d/
sudo add-apt-repository --remove ppa:phoerious/keepassxc
```

### 3.2. Installer le paquet

Il suffit d’installer le paquet avec `dpkg -i nomDuPaquet` :

```sh
sudo dpkg -i haroopad-v0.13.1-x64.deb
```

### 4.1. Compiler les sources

Suivre ensuite les instructions du fichier `README.md` :

```sh
make
sudo make install
make test
```
