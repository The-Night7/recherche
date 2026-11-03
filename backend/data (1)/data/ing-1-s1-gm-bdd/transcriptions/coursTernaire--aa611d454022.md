# coursTernaire.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1BvjT3r9Pzz6LWR-BfSHNIOzp-jdvNKT1) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                                  Associations binaires ou ternaires ?
             Base de données
       Modèle Conceptuel de Données                                         Quel serait le MCD dans cet exemple ?
                                                                            Les professeurs enseignent dans des établissements dans
           Les associations ternaires                                       certaines matières. Il est possible qu’un professeur
                                                                            enseigne des matières différentes dans les établissements.
                                                                            Décomposons cet exemple en phrases simples :
                                                                               Un professeur peut enseigner dans plusieurs établissements
                                                                               Un établissement peut avoir plusieurs professeurs
                                                                               Une matière est enseignée par plusieurs professeurs
                        Philippe CHOCHOIS - Florence PETIT                     Un professeur peut enseigner plusieurs matières
                                                                               Un établissement propose plusieurs matières
                                  Octobre 2020
                                                                               Une matière est proposée dans plusieurs établissements



                                                                                                                                                    2




       Associations binaires ? Problème...                                          Intérêt d'une association ternaire

Avec cette modélisation, nous savons qu'un professeur enseigne              Pour savoir quelle matière est enseignée par tel professeur
certaines matières et travaillent dans certains établissements.             dans tel établissement, il faut relier les 3 entités par une
   Le professeur Dupont enseigne les mathématiques et l'informatique.       association ternaire.
   Le professeur Dupont travaille à l'UPEM et au lycée Descartes.
Mais nous ne savons pas quelles matières sont enseignées par le
professeur Dupont au lycée Descartes.




                                                                        3                                                                           4




                    Associations n-aires                                    Association ternaire et cardinalité maximale

• Il peut exister des quaternaires, voire des n-aires mais                  Dans une association ternaire,
  c'est extrêmement rare.                                                      • Les cardinalités minimales peuvent être à 0 ou 1 selon le
                                                                                 contexte (participation facultative ou obligatoire de l'entité à
• Il y a peut être une erreur de conception si le nombre                         l'association).
  d'entités reliées (arité) est supérieur ou égale à 4.                        • Toutes les cardinalités maximales sont obligatoirement à n.
                                                                                 La cardinalité maximale à n représente le fait qu'une occurrence
                                                                                 de l'entité peut participer n fois à l'association.
                                                                                 Si l'une des cardinalités maximales n'est pas à n, il y a une
                                                                                 erreur de conception.

                                                                                Entite1                                     Entite2

                                                                                                  0,n                 1,n

                                                                                                        Association
                                                                                                         ternaire                0,1

                                                                                                                                      Entite3
                                                                        5                                                                           6




                                                                                                                                                        1
~~~

## Page 2

~~~text
             Associations ternaires : limites                                             Association ternaire et agrégat

Une association ternaire met en jeu les 3 entités.                              Si un professeur peut enseigner plusieurs matières mais si
Dans l’association ternaire « enseigne », on ne peut pas                        un professeur ne peut enseigner qu’une seule matière par
mémoriser des professeurs qui enseignent des matières en                        établissement, nous sommes en présence d’une "fausse
dehors d’un établissement car dans ce cas, l’entité                             ternaire".
« établissement » ne serait pas concernée par la relation.                      Ce cas particulier s’appelle un agrégat et sera vu plus en
Par contre, on peut mémoriser des professeurs qui                               détail ultérieurement.
n’enseignent pas, car la cardinalité minimale est à zéro.                       Il est possible de le traiter comme une ternaire dans le
                                                                                MCD mais cela aura une répercussion sur la clé de la
                                                                                nouvelle table dans le MLD.




                                                                           7                                                                               8




             Association ternaire et réflexive                                        Interprétation d'un MCD : cas Sport

NB: Si les réflexives n’ont pas été vues, ignorez cette                         Nous allons proposer plusieurs cas qui modélisent un
diapositive.                                                                    même contexte avec 3 entités : Adhérent, Centre, Sport.
                                                                                Chaque modélisation a une signification différente.
L'étude concerne un seul établissement.                                         Indiquez en français ce que modélise chaque schéma.
Un professeur peut enseigner plusieurs matières à d'autres                      Essayez de voir les limites de chaque schéma.
professeurs.
                                                                                Il est fortement conseillé d'essayer de rédiger la
Il y a une association ternaire avec :                                          signification de chaque schéma avant de regarder la
- 1 lien vers l'entité Matière                                                  correction !
- 1 lien vers l'entité Professeur
    (rôle de professeur-formateur)
- 1 autre lien vers l'entité Professeur
    (rôle de professeur-formé).

                                                                           9                                                                               10




             Interprétation d'un MCD - cas 1                                              Interprétation d'un MCD - cas 2

Des adhérents sont inscrits dans des centres.                                   Des adhérents sont inscrits dans des centres.
Les centres proposent des sports.                                               Les adhérents pratiquent certains sports.
On ne sait pas quel(s) sport(s) pratique un adhérent.                           On ne sait pas quel(s) sport(s) propose un centre.

  ADHERENT                          CENTRE                         SPORT         CENTRE                          ADHERENT                          SPORT
                    inscrit                        propose                                 0,n   inscrit   0,n                    pratique   0,n
                              1,n            1,n             1,n
              1,n                                                                                                           0,n




                                                                           11                                                                              12




                                                                                                                                                                2
~~~

## Page 3

~~~text
         Interprétation d'un MCD - cas 3                                                         Interprétation d'un MCD - cas 4

Des adhérents sont inscrits dans des centres.                                        Des adhérents pratiquent des sports dans des centres.
Les adhérents pratiquent des sports.                                                 On ne sait pas quel sport est proposé par un centre si ce
Les centres proposent des sports.                                                    sport n’est pratiqué par aucun adhérent.
On ne sait pas dans quel(s) centre(s) un adhérent pratique
un sport donné.                                                                        CENT RE
                                                                                                                          pratique
                                                                                                                                                               SPORT
                                                                                                                                                         0,n
                                                                                                       0,n
CENTRE                          ADHERENT                                SPORT
         0,n   inscrit   1,n                      pratique     1,n                                                             1,n
                                            1,n
                                                                                                                        ADHERENT

               1,n                                       1,n
                                  propose




                                                                                13                                                                                     14




         Interprétation d'un MCD - cas 5                                                         Interprétation d'un MCD - cas 6

Des adhérents sont inscrits dans des centres pour                                    Des adhérents sont inscrits dans des centres pour
pratiquer des sports.                                                                pratiquer des sports.
Les centres proposent des sports à pratiquer.                                        Les centres proposent des sports à pratiquer.
On ne connaît pas les sports pratiqués par les adhérents                             Proposez une modification pour connaître les sports
hors de ces centres (ex : sports individuels).                                       pratiqués par les adhérents hors des centres.
                                propose
                                                                                                                            propose


                                                   1,n
                                                                                                                                                   1,n
                1,n
                                                                                                          1,n
   CENT RE                                                           SPORT
                                prati que                0,n                            CENT RE                                                                SPORT
                                                                                                                           prati que                     0,n
               0,n
                                                                                                         0,n

                                    1,n
                                                                                                                                   1,n

                               ADHERENT
                                                                                                                         ADHERENT




                                                                                15                                                                                     16




    Ternaires et modèle logique de données                                                        Passage au MLD d'une ternaire

- Les règles définies pour les binaires de type plusieurs à                          Table Centre (numCentre, nomCentre)
  plusieurs s’appliquent aux ternaires…
                                                                                         numCentre: clé primaire de la table Centre
- Les cardinalités maximales sont à n sur chaque lien de
  l'association dans le MCD, donc l'association est                                  Table Sport (idSport, nomSport, nbLicencies)
  transformée en une nouvelle table dans le MLD.
                                                                                         idSport: clé primaire de la table sport
- La clé primaire de cette nouvelle table est une clé
                                                                                     Table Adherent (numAdherent, nomAdherent, prenomAdherent, telAdherent)
  primaire composée des clés primaires des tables liées
  (donc clé composée de 3 éléments pour une ternaire).                                   numAdherent: clé primaire de la table Adherent

- Chaque élément de la clé primaire est une clé étrangère                            Table Pratique (numCentre, idSport, numAdherent, dateDebut)
  qui référence la clé primaire de chaque table associée.
- Si l'association porte des propriétés, ces propriétés                                  numCentre, idSport, numAdherent: clé primaire composée de la table Pratique
  deviennent des attributs de la table résultante.                                       numCentre clé étrangère qui référence numCentre de la table Centre
                                                                                         idSport clé étrangère qui référence idSport de la table Sport
                                                                                         numAdherent clé étrangère qui référence numAdherent de la table Adherent



                                                                                17                                                                                     18




                                                                                                                                                                            3
~~~

## Page 4

~~~text
                                Exercice Minis 1                                                                                             Exercice Minis 2
M. MINIS est responsable de la gestion du parc automobile du ministère de l'éducation nationale.             M. MINIS est responsable de la gestion du parc automobile du ministère de l'éducation nationale.
Il affecte des véhicules et des chauffeurs pour des missions de transport demandées par des services.        Il affecte des véhicules et des chauffeurs pour des missions de transport demandées par des services.
• Un véhicule est caractérisé par un n° d'immatriculation et une date de mise en circulation.                • Un véhicule est caractérisé par un n° d'immatriculation et une date de mise en circulation.
• Une mission est caractérisée par un numéro et son objet.                                                   • Une mission est caractérisée par un numéro et son objet.
• Un chauffeur est caractérisé par un numéro de matricule et un nom.                                         • Un chauffeur est caractérisé par un numéro de matricule et un nom.
• Un service est caractérisé par un code service et un nom de service.                                       • Un service est caractérisé par un code service et un nom de service
Règles de gestion                                                                                            Règles de gestion
1. Une mission nécessite un seul véhicule.                                                                   1. Une mission nécessite un seul véhicule et un seul chauffeur.
2. Une mission nécessite un seul chauffeur.                                                                  2. Un chauffeur peut être affecté à plusieurs missions.
3. Un chauffeur peut être affecté à plusieurs missions.                                                      3. Un chauffeur peut être en attente d'affectation.
4. Un chauffeur peut être en attente d'affectation.                                                          4. Un véhicule peut ne pas être utilisé pour une mission.
5. Un véhicule peut ne pas être utilisé pour une mission.                                                    5. Un véhicule peut être utilisé pour des missions différentes.
6. Un véhicule peut être utilisé pour des missions différentes.                                              6. Une mission est sous la responsabilité d'un seul service.
7. Une mission est sous la responsabilité d'un seul service.                                                 7. Un service peut être à l'origine de plusieurs missions ou d'aucune.
8. Un service peut être à l'origine de plusieurs missions ou d'aucune.                                       8. Un chauffeur a son propre véhicule qui lui est exclusivement affecté.
                                                                                                             9. Lorsque le chauffeur n’est pas en service, il peut emmener son véhicule avec lui.




                                                                                                        19                                                                                                           20




                                Exercice Minis 3
M. MINIS est responsable de la gestion du parc automobile du ministère de l'éducation nationale.
Il affecte des véhicules et des chauffeurs pour des missions de transport demandées par des services.
• Un véhicule est caractérisé par un n° d'immatriculation et une date de mise en circulation.
• Une mission est caractérisée par un numéro et son objet.
• Un chauffeur est caractérisé par un numéro de matricule et un nom.
• Un service est caractérisé par un code service et un nom de service.
Règles de gestion
1. Une mission peut nécessiter plusieurs véhicules et plusieurs chauffeurs.                                                              Ternaires avec date
2. Un chauffeur peut être affecté à plusieurs missions.
3. Un chauffeur peut être en attente d'affectation.
                                                                                                                                         Notion d’historique
4. Un véhicule peut ne pas être utilisé pour une mission.
5. Un véhicule peut être utilisé pour des missions différentes.
6. Une mission est sous la responsabilité d'un seul service.
7. Un service peut être à l'origine de plusieurs missions ou d'aucune.
8. Pour les missions de longue durée, il y a plusieurs chauffeurs par véhicule..
9. Un chauffeur peut conduire des véhicules différents lors d’une mission (pas en même temps !).
10. On doit pouvoir connaître quel chauffeur a conduit quel véhicule au cours d’une mission.




                                                                                                        21                                                                                                           22




                             Ternaire avec date                                                                  Passage au MLD d'une ternaire avec date
                                                                                                                        Modèle brut, non optimisé
Des individus pratiquent des sports à un certain niveau…
Au cours des années, leur niveau évolue…                                                                     Table Individu (numIndividu, nomIndividu, dateNaissance)
Le niveau dépend de l’individu, mais aussi du sport et aussi                                                      numIndividu: clé primaire de la table Individu
de l’année.
                                                                                                             Table Sport (idSport, nomSport)
La solution pour conserver l’historique des niveaux selon
                                                                                                                  idSport: clé primaire de la table Sport
les années est de faire une ternaire comme ci-dessous.
                                                                                                             Table Date (annee)
                                                                                                                  annee: clé primaire de la table Date

                                                                                                             Table Pratique (numIndividu, idSport, annee, niveau)
                                                                                                                  numIndividu, idSport, annee: clé primaire composée de la table Pratique
                                                                                                                  numIndividu clé étrangère qui référence numIndividu de la table Individu
                                                                                                                  idSport clé étrangère qui référence idSport de la table Sport
                                                                                                                  annee clé étrangère qui référence annee de la table Date



                                                                                                        23                                                                                                           24




                                                                                                                                                                                                                          4
~~~

## Page 5

~~~text
         Passage au MLD d'une ternaire avec date                                                                                        Comparaison
                    Modèle optimisé                                                                                         Gestion de dates: Binaire ou Ternaire ?
                                                                                                                                                                                Cas b
    Table Individu (numIndividu, nomIndividu, dateNaissance)                                                          Cas a
           numIndividu: clé primaire de la table Individu

    Table Sport (idSport, nomSport)
           idSport: clé primaire de la table Sport

    Table Pratique (numIndividu, idSport, annee, niveau)
           numIndividu, idSport, annee: clé primaire composée de la table Pratique                                    Voici 2 schémas permettant de gérer les dates d’obtention du permis de conduire.
           numIndividu clé étrangère qui référence numIndividu de la table Individu
                                                                                                                      Cas a: L’association binaire « obtenir » permet de mémoriser que des personnes obtiennent leur
           idSport clé étrangère qui référence idSport de la table Sport                                              permis de conduire à une date donnée (dateObtention).
                                                                                                                      Cas b: L’association ternaire « obtenir » permet de mémoriser que des personnes obtiennent leur
                                                                                                                      permis de conduire à une date donnée (dateObtention).
    Remarques:
    - La table Date disparaît                                                                                         Y a-t-il une différence notoire entre les 2 représentations ou sont-elles équivalentes ?
      car elle ne contenait aucune donnée intéressante
       à mémoriser.
                                                                                                                      Pour cela, nous allons essayer de répondre à une série de questions concernant les 2 modélisations
    - La référence de la clé étrangère
       vers le champ « annee » disparaît donc également.
                                                                                                             25                                                                                                             26




                       Comparaison                                                                                                      Comparaison
           Gestion de dates: Binaire ou Ternaire ?                                                                          Gestion de dates: Binaire ou Ternaire ?
                                                             Cas b                                                                                                              Cas b
    Cas a                                                                                                             Cas a




    Vous devez répondre aux questions ci-dessous en déterminant votre réponse en fonction
    du schéma ci-dessus !                                                                                         -     Dans le cas a, peut-il y avoir plusieurs personnes qui ont le même permis ?
                                                                                                                  -     Dans le cas b, peut-il y avoir plusieurs personnes qui ont le même permis ?
-       Dans le cas a, toutes les personnes ont-elles un permis ?                                                 -     Dans le cas a, des personnes différentes peuvent-elles avoir la même date d’obtention du permis ?
-       Dans le cas b, toutes les personnes ont-elles un permis ?                                                 -     Dans le cas b, des personnes différentes peuvent-elles avoir la même date d’obtention du permis ?
-       Dans le cas a, existe-t-il au moins une personne pour chaque permis ?                                     -     Dans le cas a, des personnes différentes peuvent-elles obtenir le même permis le même jour ?
-       Dans le cas b, existe-t-il au moins une personne pour chaque permis ?                                     -     Dans le cas b, des personnes différentes peuvent-elles obtenir le même permis le même jour ?
-       Dans le cas a, y a-t-il chaque jour quelqu’un qui obtient son permis ?                                    -     Dans le cas a, une personne peut-elle obtenir 2 permis différents le même jour ?
-       Dans le cas b, y a-t-il chaque jour quelqu’un qui obtient son permis ?                                    -     Dans le cas b, une personne peut-elle obtenir 2 permis différents le même jour ?
-       Dans le cas a, pour une date d’obtention d’un permis, y a-t-il toujours une personne concernée ?
-       Dans le cas b, pour une date d’obtention d’un permis, y a-t-il toujours une personne concernée ?
-       Dans le cas a, une personne peut-elle avoir plusieurs permis ?
-       Dans le cas b, une personne peut-elle avoir plusieurs permis ?
                                                                                                             27                                                                                                             28




                       Comparaison
           Gestion de dates: Binaire ou Ternaire ?
                                                             Cas b
    Cas a




    -   Donc, existe t-il une différence ?

    -   Dans le cas a, une personne peut elle obtenir un permis qu’elle a déjà obtenu ?   Non
    -   Dans le cas b, une personne peut elle obtenir un permis qu’elle a déjà obtenu ?   Oui

    -   Avec l’association binaire, une personne ne peut obtenir un permis qu’une seule fois
    -   Avec l’association ternaire, une personne peut obtenir plusieurs fois un permis.

    -   On utilisera donc une association binaire si le permis est acquis « à vie ». On ne peut pas le
        repasser.
    -   On utilisera donc une association ternaire si le permis peut être supprimé et dans ce cas, on doit
        pouvoir le repasser.
                                                                                                             29




                                                                                                                                                                                                                                 5
~~~
