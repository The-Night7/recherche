---
source: "ING 1/S1 GM /UNIX/TD_TP_Sys.exploitation/TP4/Solutions TP4 partie2.txt"
pages: 0
transcription: fichier texte natif intégral remis en forme, commandes conservées
transcription_date: 2026-10-16
verification: lecture intégrale et comparaison avec le fichier texte source
---

# TP4 — Solutions, partie 2

Les commandes et le proxy ci-dessous sont ceux du support historique. Aucune commande n’a été exécutée pour cette transcription.

## 1. Problème de réseau

Si la machine est connectée au réseau de l’école et que le proxy est mal paramétré, modifier le fichier `apt.conf` sur la machine virtuelle :

```sh
sudo nano /etc/apt/apt.conf
```

Ajouter dans ce fichier :

```text
Acquire::http::Proxy "http://proxy.cergy.eisti.fr:3128/";
```

Le support indique de faire `Ctrl+X` pour sauvegarder. **Précision de transcription :** dans Nano, ce raccourci quitte l’éditeur et demande confirmation de l’enregistrement si le fichier a été modifié.

## 2. Sinon

Séquence de commandes telle qu’imprimée :

```sh
sudo apt update && apt upgrade && apt install transmission-cli transmission-daemon
sudo apt update
sudo apt clean
sudo apt update
sudo apt install ssh
```

Continuer le TP.

**Note de transcription :** sur la première ligne, `sudo` ne s’applique qu’à `apt update`. Les deux commandes suivantes ne sont pas élevées par le `sudo` initial ; le support les reproduit ainsi.
