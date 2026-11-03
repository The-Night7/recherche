---
source: "PREING2-S1/Informatique3-DS/cc-2025-2026/DS1_Informatique_III_refait.pdf"
archive: "cc 2025 2026.zip"
pages: 2
semestre: "P2S1"
transcription: texte natif restructuré et contrôlé sur le rendu PDF
transcription_date: 2026-11-01
verification: comparaison du texte extrait avec le rendu des pages du PDF fourni
---

# DS1 Informatique III refait

## Page 1

CY TECH

DS N° 1 — INFORMATIQUE III Pré-ING2 · Semestre 1 · 2025/2026 · Langage C obligatoire

Calculatrice et documents non autorisés. Attention à la robustesse du programme. Vous pouvez définir autant de fonctions que vous le souhaitez. Une question ne correspond pas nécessairement à une fonction.

### Exercice 1 — File : gestion de la file d’attente de l’attraction Toutatis (11,25 points)

L’attraction Toutatis, au parc Astérix, est l’une des plus populaires du parc. En raison de sa fréquentation élevée, le parc cherche à optimiser la gestion de la file d’attente pour réduire le temps d’attente moyen des visiteurs. Nous allons simuler le fonctionnement de la file et du remplissage des trains à l’aide de structures dynamiques.

1. Modélisation de la file Les visiteurs arrivent par groupes, composés de plusieurs personnes souhaitant embarquer ensemble dans le même train.

(a) Définir une (ou plusieurs) structures permettant de représenter une file dynamique dont chaque élément correspond à un groupe. Chaque groupe contient : un identifiant (ou numéro d’arrivée) ; le nombre de personnes dans le groupe (entre 2 et 10) ; un pointeur vers le groupe suivant.

(b) Écrire la fonction/procédure entrerFile(...) permettant de simuler l’arrivée d’un nouveau groupe dans la file. Cette fonction créera également le groupe arrivant dans la file. Le nombre de personnes du groupe sera tiré aléatoirement entre 2 et 10 et l’identifiant sera l’incrémentation de l’identifiant du dernier groupe de la file (si la file est vide cet identifiant vaudra 1).

(c) Écrire la fonction/procédure sortirFile(...) permettant de retirer de la file le premier groupe (celui qui embarque). Cette fonction devra également retourner le nombre de personnes du groupe retiré pour que la fonction appelante puisse le récupérer.

2. Remplissage d’un train Chaque train de Toutatis comporte 10 rangées de 2 sièges, soit 20 places au total. Écrire une fonction/procédure remplirTrain(...) qui prend en paramètre uniquement la file de groupe, et qui remplit progressivement le train à partir de cette file :

— Les groupes défilent dans l’ordre d’arrivée ;

— Les groupes remplissent les places vides dans l’ordre ;

— Si le prochain groupe à embarquer ne tient pas entièrement dans les places restantes, il attendra le train suivant ;

— Dans ce dernier cas, le train part alors avec quelques places vides.

La fonction retournera le taux de remplissage du train (en valeur normalisée).

Exemple : si le train contient 20 places et que 18 sont occupées, le taux de remplissage est de 0,9.

3. Amélioration : la file Single Rider Le mode précédent n’est pas optimal : certains trains partent avec des places vides ; certains groupes peuvent être séparés dans des rangées différentes.

Exemples illustrés sur le sujet : un groupe de 6 et un de 2 : OK ; deux groupes de 3 : OK ; un groupe B trop séparé : non. L’ajout d’un single rider permet de regrouper B.

## Page 2

Pour mieux remplir les trains, on ajoute une seconde file d’attente appelée Single Rider. Cette file contient uniquement des visiteurs seuls, qui peuvent être placés pour combler les vides laissés par les groupes. On peut simplifier la file Single Rider comme étant une file de groupes dont chaque groupe possède une taille de 1.

Écrire une nouvelle version de remplirTrain(...) prenant en paramètre deux files : la file classique (groupes de 2 à 10 personnes) ; la file Single Rider (groupes d’une seule personne).

La fonction doit remplir le train avec les visiteurs de la file classique et uniquement utiliser la file Single Rider pour combler d’éventuelles places vides ou éviter un mauvais placement de groupe (voir schéma). Elle retourne le nombre de visiteurs seuls ayant embarqué dans le train.

ATTENTION : si la file des Single Rider est vide, on laisse les places vides éventuelles entre chaque groupe (comme s’il y avait un single rider).

4. Simulation du temps d’attente En fonctionnement optimal, un train complet part toutes les 57 secondes.

Écrire une fonction/procédure tempsAttente(...) qui prend en paramètre les deux files (classique et single rider) et affiche le temps minimum nécessaire pour vider entièrement les files en minutes entières arrondies au plus proche.
