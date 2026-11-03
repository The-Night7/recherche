# Fiche de revision BDD.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Gx4o2imPPqFbnrbcaFys9p7jULcpA1pO) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
FICHE DE RÉVISION - BASE DE DONNÉES
Partiel ING1-GM - CY Tech



  TABLE DES MATIÈRES
    1. Modélisation - MCD
    2. Passage MCD → MLD
    3. Dépendances Fonctionnelles
    4. Normalisation
    5. LDD - Création de Tables
    6. LMD - Manipulation de Données
    7. Requêtes SQL Simples
    8. Requêtes SQL Avancées
    9. Exercices Types d'Examens




1. MODÉLISATION - MCD

1.1 Concepts de Base

ENTITÉ : Objet du monde réel avec des propriétés

        Possède un identifiant unique (clé)
        Représentée par un rectangle
        Exemples : Joueur, Pokemon, Livre, Patient

ASSOCIATION : Relation entre entités

        Représentée par un ovale/ellipse
        Peut avoir des attributs propres
        Exemples : Manger, Défendre, Enseigner

ATTRIBUTS : Propriétés d'une entité ou association

        Simples vs composés (adresse = rue + ville + CP)
        Obligatoires vs optionnels

CARDINALITÉS : Contraintes de participation

        Format : (min, max) pour chaque entité dans une association
        0,1 : optionnel, au plus une fois
        1,1 : obligatoire, exactement une fois
        0,N : optionnel, plusieurs fois possible
        1,N : obligatoire, au moins une fois


1.2 Méthodologie de Construction

    1. Recenser les informations du cahier des charges
    2. Identifier les entités (objets/concepts principaux)
    3. Définir les attributs de chaque entité
    4. Choisir les identifiants (clés primaires)
    5. Identifier les associations entre entités
    6. Déterminer les cardinalités
    7. Vérifier avec le cahier des charges


1.3 Cas Particuliers

Association réflexive : Une entité associée à elle-même

        Exemple : Matière → Pré-requis → Matière
        Cardinalités peuvent être différentes de chaque côté

Association ternaire : Lie 3 entités ou plus

        Exemple : Étudiant-Matière-Promotion avec note

Entité faible : N'existe que par une autre

        Dépend d'une entité forte pour son identification

Spécialisation/Héritage :

        Employé → Docteur / Infirmier
        Triangle avec "T" (totale) ou "P" (partielle)
~~~

## Page 2

~~~text
1.4 Pièges à Éviter

 Confusion attribut/entité

       Si une information peut être répétée → entité
       Si unique et atomique → attribut

 Oubli d'associations

       Toujours vérifier les liens entre entités

 Cardinalités incorrectes

       Relire le cahier des charges attentivement
       "Un" = 1, "Plusieurs" = N, "Peut" = 0




2. PASSAGE MCD → MLD

2.1 Règles de Transformation

Règle 1 : Entité → Relation (Table)


  Entité(Attribut1, Attribut2, ...)


       Clé primaire soulignée
       Tous les attributs de l'entité deviennent des colonnes


Règle 2 : Association selon cardinalités

CAS 1 : Association 1,1 ou 0,1 avec autre côté

       Ajouter clé étrangère du côté (0,1) ou (1,1)
       Plus les attributs de l'association


  Exemple : Joueur(0,N) -- Effectue_Sejour -- (1,1) Sejour
 → Sejour(id, date, durée, #idJoueur)


CAS 2 : Association N,M (plusieurs-à-plusieurs)

       Créer une table d'association
       Clé primaire = combinaison des clés étrangères
       Plus les attributs de l'association


  Exemple : Pokemon(0,N) -- Apparition -- (0,N) Emplacement
 → Apparition(#idPokemon, #idEmplacement, horaire, duree)


CAS 3 : Association 1,N (un-à-plusieurs)

       Ajouter clé étrangère du côté N
       Plus les attributs de l'association


  Exemple : Equipe(1,1) -- Possède -- (0,N) Joueur
 → Joueur(id, nom, #idEquipe)


CAS 4 : Association ternaire ou plus

       Toujours créer une table d'association
       Clé primaire = combinaison de toutes les clés étrangères


2.2 Notation Standard

  NomTable(clé_primaire, attribut1, attribut2, #clé_étrangère)


       Souligné = clé primaire
       # = clé étrangère (foreign key)
       Italique ou # = référence vers autre table


2.3 Cas Particuliers

Héritage :
~~~

## Page 3

~~~text
        Approche 1 : Une table par sous-type
        Approche 2 : Une seule table avec attribut discriminant
        Approche 3 : Table pour type parent + tables pour sous-types

Association réflexive :


  Matiere(id, nom)
  PreRequis(#idMatiere, #idPreRequis)




3. DÉPENDANCES FONCTIONNELLES

3.1 Définition

Dépendance Fonctionnelle (DF) : A → B

        "A détermine B"
        "B dépend fonctionnellement de A"
        Signifie : pour chaque valeur de A, il existe une seule valeur de B


3.2 Types de Dépendances

DF élémentaire :

        Partie droite = un seul attribut
        A, B → C n'est PAS élémentaire
        A → C et B → D sont élémentaires

DF directe :

        Non déductible par transitivité
        Si A → B et B → C , alors A → C n'est PAS directe

DF triviale :

        A → A (toujours vraie)
        Généralement ignorée


3.3 Règles d'Armstrong

     1. Réflexivité : Si Y ⊆ X, alors X → Y
     2. Augmentation : Si X → Y, alors XZ → YZ
     3. Transitivité : Si X → Y et Y → Z, alors X → Z
     4. Décomposition : Si X → YZ, alors X → Y et X → Z
     5. Union : Si X → Y et X → Z, alors X → YZ


3.4 Identification des DF

  CINEMA(NumSalleCinema, adresseSalleCinema, nomSalleCinema,
            NumFilm, titreFilm, NumCatégorieFilm, intituléCatégorieFilm,
            dateDébutProjectionFilm, duréeProjectionFilm)


  Dépendances Fonctionnelles :
  1. NumSalleCinema → adresseSalleCinema
  2. NumSalleCinema → nomSalleCinema
  3. NumFilm → titreFilm
  4. NumFilm → NumCatégorieFilm
  5. NumFilm → duréeProjectionFilm
  6. NumCatégorieFilm → intituléCatégorieFilm
  7. NumSalleCinema, NumFilm, dateDébutProjectionFilm → TOUS les attributs


Clé candidate : Ensemble minimal d'attributs déterminant tous les autres

        Ici : (NumSalleCinema, NumFilm, dateDébutProjectionFilm)




4. NORMALISATION

4.1 Première Forme Normale (1FN)
~~~

## Page 4

~~~text
Définition : Une relation est en 1FN si tous ses attributs sont atomiques

 Violations courantes :

       Valeurs multiples : adresse = "10 rue, Paris, 75001"
       Attributs répétés : tel1, tel2, tel3
       Listes : ingredients = "farine, sucre, oeufs"

 Solution : Décomposer en attributs simples ou créer nouvelle table


  BAD: Client(id, adresse)
        avec adresse = "10 rue de la Paix, Paris, 75001"


 GOOD: Client(id, numero, rue, ville, codePostal)



4.2 Deuxième Forme Normale (2FN)

Définition : 1FN + aucun attribut non-clé ne dépend d'une partie de la clé

S'applique uniquement aux relations avec clé composée


  Violation 2FN:
 Location(idLogement, nomClient, dateSignature, #idVille, nbPieces)
 Clé : (idLogement, dateSignature) supposée


 Si : idLogement → nbPieces
 Alors nbPieces dépend d'UNE PARTIE de la clé → violation 2FN


 Solution:
 Logement(idLogement, nbPieces, #idVille)
 Location(#idLogement, nomClient, dateSignature)



4.3 Troisième Forme Normale (3FN)

Définition : 2FN + aucune dépendance transitive entre attributs non-clés


  Violation 3FN:
 Ville(idVille, nomVille, departement, region)


 Si : idVille → departement → region
 Alors region dépend transitivement de idVille → violation 3FN


 Solution:
 Ville(idVille, nomVille, #idDepartement)
 Departement(idDepartement, nom, #idRegion)
 Region(idRegion, nom)



4.4 Forme Normale de Boyce-Codd (BCNF)

Définition : Pour toute DF non triviale X → Y, X est une clé candidate

Plus stricte que 3FN


  SuiviInstallation(numOrdi, nomLogiciel, marqueOrdi, dateInstallation, tailleRAM)


 Clé : (numOrdi, nomLogiciel, dateInstallation)
 DF : numOrdi → marqueOrdi
        numOrdi → tailleRAM


 numOrdi n'est PAS une clé candidate → violation BCNF


 Solution:
 Ordinateur(numOrdi, marqueOrdi, tailleRAM)
 Installation(#numOrdi, nomLogiciel, dateInstallation)



4.5 Méthodologie de Normalisation
~~~

## Page 5

~~~text
   1. Identifier toutes les DF (élémentaires et directes)
   2. Identifier la(les) clé(s) candidate(s)
   3. Vérifier 1FN : attributs atomiques ?
   4. Vérifier 2FN : pas de dépendance partielle ?
   5. Vérifier 3FN : pas de dépendance transitive ?
   6. Vérifier BCNF : déterminants sont des clés ?
   7. Décomposer si nécessaire en préservant les DF




5. LDD - CRÉATION DE TABLES

5.1 Syntaxe CREATE TABLE

 CREATE TABLE NomTable (
        attribut1 TYPE CONTRAINTES,
        attribut2 TYPE CONTRAINTES,
        ...
        CONSTRAINT nom_contrainte type_contrainte
 );



5.2 Types de Données Courants

 -- Numériques
 INT, SMALLINT, BIGINT                    -- Entiers
 DECIMAL(p,s), NUMERIC(p,s)               -- Décimaux exacts
 FLOAT, REAL, DOUBLE                      -- Décimaux approx.


 -- Texte
 CHAR(n)                -- Chaîne fixe
 VARCHAR(n)             -- Chaîne variable
 TEXT                   -- Texte long


 -- Date et Heure
 DATE                   -- Date (YYYY-MM-DD)
 TIME                   -- Heure (HH:MM:SS)
 DATETIME               -- Date + Heure
 TIMESTAMP              -- Horodatage


 -- Booléen
 BOOLEAN                -- TRUE/FALSE



5.3 Contraintes d'Intégrité

 CREATE TABLE Joueur (
        pseudonyme VARCHAR(30) PRIMARY KEY,
        personnage VARCHAR(30) NOT NULL UNIQUE,
        sexe CHAR(1),
        niveau SMALLINT DEFAULT 0 NOT NULL,
        idEquipe INT,


        -- Clé étrangère
        FOREIGN KEY fk_equipe(idEquipe)
              REFERENCES Equipe(id)
              ON DELETE CASCADE
              ON UPDATE RESTRICT,


        -- Contrainte de vérification
        CONSTRAINT check_sexe CHECK (sexe IN ('M', 'F')),
        CONSTRAINT check_niveau CHECK (niveau >= 0)
 );



5.4 Types de Contraintes
~~~

## Page 6

~~~text
PRIMARY KEY : Identifiant unique, non NULL


  id INT PRIMARY KEY
 -- ou
 PRIMARY KEY (attr1, attr2)        -- Clé composée


FOREIGN KEY : Référence vers autre table


  FOREIGN KEY (attr_local) REFERENCES TableEtrangere(attr_distant)


ON DELETE / ON UPDATE :

         CASCADE : Suppression/MAJ en cascade
         RESTRICT : Interdire si référencée
         SET NULL : Mettre à NULL
         SET DEFAULT : Valeur par défaut
         NO ACTION : Aucune action (par défaut)

UNIQUE : Valeurs uniques (mais NULL autorisé)


  email VARCHAR(100) UNIQUE


NOT NULL : Valeur obligatoire


  nom VARCHAR(50) NOT NULL


CHECK : Condition personnalisée


  CHECK (age >= 18)
 CHECK (latitude BETWEEN -90 AND 90)


DEFAULT : Valeur par défaut


  niveau INT DEFAULT 0
 dateCreation DATE DEFAULT CURRENT_DATE



5.5 Modification de Tables

  -- Ajouter une colonne
 ALTER TABLE NomTable ADD COLUMN nouvelAttribut TYPE;


 -- Supprimer une colonne
 ALTER TABLE NomTable DROP COLUMN attribut;


 -- Modifier un type
 ALTER TABLE NomTable MODIFY COLUMN attribut NOUVEAU_TYPE;


 -- Ajouter une contrainte
 ALTER TABLE NomTable ADD CONSTRAINT nom CHECK (condition);


 -- Supprimer une table
 DROP TABLE NomTable;


 -- Si dépendances
 DROP TABLE NomTable CASCADE;



5.6 Exemple Complet
~~~

## Page 7

~~~text
 -- Suppression si existe
 DROP TABLE IF EXISTS Defense;
 DROP TABLE IF EXISTS Arene;
 DROP TABLE IF EXISTS Pokemon;
 DROP TABLE IF EXISTS Joueur;
 DROP TABLE IF EXISTS Equipe;


 -- Création dans l'ordre (dépendances)
 CREATE TABLE Equipe (
      id INT PRIMARY KEY,
      nom VARCHAR(20) NOT NULL,
      couleur VARCHAR(10)
 );


 CREATE TABLE Joueur (
      pseudonyme VARCHAR(30) PRIMARY KEY,
      personnage VARCHAR(30) NOT NULL UNIQUE,
      sexe CHAR(1),
      niveau SMALLINT DEFAULT 0 NOT NULL,
      idEquipe INT,
      FOREIGN KEY (idEquipe) REFERENCES Equipe(id) ON DELETE CASCADE,
      CHECK (sexe IN ('M', 'F')),
      CHECK (niveau >= 0)
 );


 CREATE TABLE Pokemon (
      id INT PRIMARY KEY,
      nom VARCHAR(30),
      espece VARCHAR(20),
      pointCombat INT,
      idJoueur VARCHAR(30),
      FOREIGN KEY (idJoueur) REFERENCES Joueur(pseudonyme),
      CHECK (pointCombat >= 0)
 );




6. LMD - MANIPULATION DE DONNÉES

6.1 INSERT - Insertion

 -- Insertion complète
 INSERT INTO Equipe VALUES (1, 'Intuition', 'Jaune');


 -- Insertion partielle (colonnes spécifiées)
 INSERT INTO Joueur (pseudonyme, personnage, niveau)
 VALUES ('Shadow', 'Smith', 10);


 -- Insertion multiple
 INSERT INTO Pokemon VALUES
      (1, 'Bulbizarre', 'Graine', 1071, 'Shadow'),
      (25, 'Pikachu', 'Souris', 887, 'Root');


 -- Insertion depuis SELECT
 INSERT INTO NouvelleTable (col1, col2)
 SELECT attr1, attr2 FROM AutreTable WHERE condition;



6.2 UPDATE - Mise à Jour
~~~

## Page 8

~~~text
 -- Mise à jour simple
 UPDATE Joueur SET niveau = 15 WHERE pseudonyme = 'Shadow';


 -- Mise à jour multiple colonnes
 UPDATE Joueur
 SET niveau = niveau + 2, personnage = 'NewName'
 WHERE pseudonyme = 'Admin';


 -- Mise à jour conditionnelle
 UPDATE Pokemon
 SET pointCombat = pointCombat * 1.1
 WHERE espece = 'Souris';


 -- Mise à jour globale (ATTENTION !)
 UPDATE Joueur SET niveau = 10;     -- Tous les joueurs !



6.3 DELETE - Suppression

 -- Suppression conditionnelle
 DELETE FROM Pokemon WHERE pointCombat < 100;


 -- Suppression avec sous-requête
 DELETE FROM Joueur
 WHERE idEquipe = (SELECT id FROM Equipe WHERE nom = 'Bravoure');


 -- Suppression globale (DANGER !)
 DELETE FROM Joueur;   -- Supprime TOUT !


 -- Vider table mais garder structure
 TRUNCATE TABLE Joueur;



6.4 Contraintes et Erreurs

 --   Erreur : Violation clé primaire
 INSERT INTO Equipe VALUES (1, 'Test', 'Vert');     -- id=1 existe déjà


 --   Erreur : Violation clé étrangère
 INSERT INTO Joueur VALUES ('X', 'Y', 'M', 5, 999);     -- Equipe 999 n'existe pas


 --   Erreur : Violation CHECK
 INSERT INTO Pokemon VALUES (10, 'Test', 'Type', -50, 'Shadow');     -- pointCombat < 0


 --   Erreur : Suppression impossible (référencée)
 DELETE FROM Equipe WHERE id = 1;     -- Si joueurs existent avec idEquipe=1


 --   Solution : CASCADE
 -- Si défini avec ON DELETE CASCADE, supprime aussi les joueurs liés




7. REQUÊTES SQL SIMPLES

7.1 SELECT - Structure de Base

 SELECT colonnes
 FROM table
 WHERE conditions
 GROUP BY colonnes_groupement
 HAVING conditions_sur_groupes
 ORDER BY colonnes_tri [ASC|DESC]
 LIMIT nombre;
~~~

## Page 9

~~~text
7.2 Projection (SELECT)

  -- Toutes les colonnes
 SELECT * FROM Pokemon;


 -- Colonnes spécifiques
 SELECT nom, espece FROM Pokemon;


 -- Éliminer doublons
 SELECT DISTINCT espece FROM Pokemon;


 -- Alias de colonnes
 SELECT nom AS nomPokemon, pointCombat AS PC FROM Pokemon;


 -- Expressions calculées
 SELECT nom, pointCombat * 1.1 AS nouveauPC FROM Pokemon;



7.3 Restriction (WHERE)

  -- Comparaisons simples
 SELECT * FROM Pokemon WHERE pointCombat > 1000;
 SELECT * FROM Joueur WHERE sexe = 'F';


 -- Opérateurs logiques
 SELECT * FROM Pokemon WHERE pointCombat > 500 AND espece = 'Souris';
 SELECT * FROM Joueur WHERE niveau < 10 OR sexe = 'M';
 SELECT * FROM Pokemon WHERE NOT espece = 'Graine';


 -- BETWEEN
 SELECT * FROM Pokemon WHERE pointCombat BETWEEN 500 AND 1500;


 -- IN
 SELECT * FROM Joueur WHERE pseudonyme IN ('Shadow', 'Root', 'Admin');


 -- IS NULL / IS NOT NULL
 SELECT * FROM Pokemon WHERE idJoueur IS NULL;
 SELECT * FROM Joueur WHERE idEquipe IS NOT NULL;



7.4 Filtrage de Texte (LIKE)

  -- Commence par 'P'
 SELECT * FROM Pokemon WHERE nom LIKE 'P%';


 -- Contient 'ka'
 SELECT * FROM Pokemon WHERE nom LIKE '%ka%';


 -- Se termine par 'on'
 SELECT * FROM Pokemon WHERE nom LIKE '%on';


 -- Deuxième lettre 'i'
 SELECT * FROM Pokemon WHERE nom LIKE '_i%';


 -- Exactement 6 caractères
 SELECT * FROM Pokemon WHERE nom LIKE '______';


 -- Insensible à la casse (MySQL)
 SELECT * FROM Pokemon WHERE nom LIKE '%pikachu%';


 -- Expressions régulières (MySQL)
 SELECT * FROM Pokemon WHERE nom REGEXP '^[MP].*';


Caractères spéciaux :
~~~

## Page 10

~~~text
       % : n'importe quelle séquence (0 ou plus caractères)
       _ : exactement un caractère


7.5 Tri (ORDER BY)

  -- Tri croissant (par défaut)
 SELECT * FROM Pokemon ORDER BY pointCombat;
 SELECT * FROM Pokemon ORDER BY pointCombat ASC;


 -- Tri décroissant
 SELECT * FROM Pokemon ORDER BY pointCombat DESC;


 -- Tri sur plusieurs colonnes
 SELECT * FROM Pokemon ORDER BY espece, pointCombat DESC;


 -- Tri avec calcul
 SELECT nom, pointCombat * 2 AS double
 FROM Pokemon
 ORDER BY double DESC;



7.6 Fonctions d'Agrégation

  -- COUNT : Compter
 SELECT COUNT(*) FROM Pokemon;                                -- Nombre total
 SELECT COUNT(DISTINCT espece) FROM Pokemon;                  -- Espèces distinctes
 SELECT COUNT(idJoueur) FROM Pokemon;                         -- Non-NULL seulement


 -- SUM : Somme
 SELECT SUM(pointCombat) FROM Pokemon;
 SELECT SUM(pointCombat) FROM Pokemon WHERE espece = 'Souris';


 -- AVG : Moyenne
 SELECT AVG(pointCombat) FROM Pokemon;
 SELECT AVG(niveau) FROM Joueur;


 -- MIN / MAX : Minimum / Maximum
 SELECT MIN(pointCombat) FROM Pokemon;
 SELECT MAX(niveau) FROM Joueur;


 -- Plusieurs agrégations
 SELECT COUNT(*), AVG(pointCombat), MAX(pointCombat)
 FROM Pokemon;



7.7 Groupement (GROUP BY)

  -- Compter par espèce
 SELECT espece, COUNT(*) AS nombre
 FROM Pokemon
 GROUP BY espece;


 -- Moyenne par joueur
 SELECT idJoueur, AVG(pointCombat) AS moyenne
 FROM Pokemon
 GROUP BY idJoueur;


 -- Plusieurs colonnes de groupement
 SELECT espece, idJoueur, COUNT(*)
 FROM Pokemon
 GROUP BY espece, idJoueur;


⚠️ RÈGLE IMPORTANTE : Si vous utilisez GROUP BY , chaque colonne dans SELECT doit être :

       Soit dans GROUP BY
~~~

## Page 11

~~~text
       Soit dans une fonction d'agrégation


  --    ERREUR
 SELECT espece, nom, COUNT(*)
 FROM Pokemon
 GROUP BY espece;      -- nom n'est ni groupé ni agrégé


 --    CORRECT
 SELECT espece, COUNT(*)
 FROM Pokemon
 GROUP BY espece;



7.8 Filtrage sur Groupes (HAVING)

  -- Espèces avec plus de 1 pokemon
 SELECT espece, COUNT(*) AS nombre
 FROM Pokemon
 GROUP BY espece
 HAVING COUNT(*) > 1;


 -- Moyenne PC > 1000
 SELECT idJoueur, AVG(pointCombat) AS moyenne
 FROM Pokemon
 GROUP BY idJoueur
 HAVING AVG(pointCombat) > 1000;


 -- WHERE vs HAVING
 SELECT espece, COUNT(*) AS nombre
 FROM Pokemon
 WHERE pointCombat > 500            -- AVANT le groupement
 GROUP BY espece
 HAVING COUNT(*) >= 2;              -- APRÈS le groupement


Différence WHERE / HAVING :

       WHERE : Filtre les lignes AVANT groupement
       HAVING : Filtre les groupes APRÈS groupement


7.9 Fonctions de Chaînes

  -- Longueur
 SELECT nom, LENGTH(nom) FROM Pokemon;


 -- Concaténation
 SELECT CONCAT(nom, ' (', espece, ')') AS description FROM Pokemon;


 -- Majuscules / Minuscules
 SELECT UPPER(nom) FROM Pokemon;
 SELECT LOWER(nom) FROM Pokemon;


 -- Sous-chaîne
 SELECT SUBSTRING(nom, 1, 3) FROM Pokemon;            -- 3 premiers caractères


 -- Remplacement
 SELECT REPLACE(nom, 'i', 'I') FROM Pokemon;



7.10 Fonctions de Dates
~~~

## Page 12

~~~text
  -- Date actuelle
 SELECT CURRENT_DATE;
 SELECT NOW();


 -- Extraction
 SELECT YEAR(horaire), MONTH(horaire), DAY(horaire)
 FROM Apparition;


 -- Différence de dates
 SELECT DATEDIFF(NOW(), horaire) AS joursDepuis
 FROM Apparition;


 -- Ajout de durée
 SELECT DATE_ADD(horaire, INTERVAL 1 MONTH)
 FROM Apparition;


 -- Formatage
 SELECT DATE_FORMAT(horaire, '%d/%m/%Y')
 FROM Apparition;




8. REQUÊTES SQL AVANCÉES

8.1 Jointures

8.1.1 INNER JOIN (Jointure Interne)

Retourne uniquement les lignes avec correspondance dans les deux tables


  -- Syntaxe explicite (recommandée)
 SELECT J.pseudonyme, P.nom, P.pointCombat
 FROM Joueur J
 INNER JOIN Pokemon P ON J.pseudonyme = P.idJoueur;


 -- Syntaxe implicite (ancienne)
 SELECT J.pseudonyme, P.nom, P.pointCombat
 FROM Joueur J, Pokemon P
 WHERE J.pseudonyme = P.idJoueur;


 -- Jointures multiples
 SELECT J.pseudonyme, P.nom, E.nom AS equipe
 FROM Joueur J
 INNER JOIN Pokemon P ON J.pseudonyme = P.idJoueur
 INNER JOIN Equipe E ON J.idEquipe = E.id;



8.1.2 LEFT JOIN (Jointure Gauche)

Retourne toutes les lignes de la table de gauche + correspondances de droite


  -- Tous les joueurs (même sans pokemon)
 SELECT J.pseudonyme, COUNT(P.id) AS nbPokemon
 FROM Joueur J
 LEFT JOIN Pokemon P ON J.pseudonyme = P.idJoueur
 GROUP BY J.pseudonyme;


 -- Identifier les joueurs sans pokemon
 SELECT J.pseudonyme
 FROM Joueur J
 LEFT JOIN Pokemon P ON J.pseudonyme = P.idJoueur
 WHERE P.id IS NULL;



8.1.3 RIGHT JOIN (Jointure Droite)
~~~

## Page 13

~~~text
Retourne toutes les lignes de la table de droite + correspondances de gauche


  -- Tous les pokemon (même sans joueur)
 SELECT P.nom, J.pseudonyme
 FROM Joueur J
 RIGHT JOIN Pokemon P ON J.pseudonyme = P.idJoueur;



8.1.4 FULL OUTER JOIN

Retourne toutes les lignes des deux tables (rarement supporté)


  -- Simulation avec UNION
 SELECT J.pseudonyme, P.nom
 FROM Joueur J LEFT JOIN Pokemon P ON J.pseudonyme = P.idJoueur
 UNION
 SELECT J.pseudonyme, P.nom
 FROM Joueur J RIGHT JOIN Pokemon P ON J.pseudonyme = P.idJoueur;



8.1.5 Auto-Jointure (SELF JOIN)

Jointure d'une table avec elle-même


  -- Trouver les paires de pokemon de même espèce
 SELECT P1.nom AS pokemon1, P2.nom AS pokemon2
 FROM Pokemon P1
 JOIN Pokemon P2 ON P1.espece = P2.espece AND P1.id < P2.id;


 -- Matières et leurs pré-requis
 SELECT M.nom AS matiere, PR.nom AS prerequis
 FROM Matiere M
 JOIN PreRequis P ON M.id = P.idMatiere
 JOIN Matiere PR ON P.idPreRequis = PR.id;



8.2 Sous-Requêtes

8.2.1 Sous-Requête Scalaire (Valeur Unique)


  -- Pokemon avec PC supérieur à la moyenne
 SELECT nom, pointCombat
 FROM Pokemon
 WHERE pointCombat > (SELECT AVG(pointCombat) FROM Pokemon);


 -- Joueurs de l'équipe la plus nombreuse
 SELECT *
 FROM Joueur
 WHERE idEquipe = (
      SELECT idEquipe
      FROM Joueur
      GROUP BY idEquipe
      ORDER BY COUNT(*) DESC
      LIMIT 1
 );



8.2.2 Sous-Requête IN / NOT IN
~~~

## Page 14

~~~text
  -- Joueurs qui ont des pokemon
 SELECT pseudonyme
 FROM Joueur
 WHERE pseudonyme IN (SELECT DISTINCT idJoueur FROM Pokemon);


 -- Joueurs sans pokemon
 SELECT pseudonyme
 FROM Joueur
 WHERE pseudonyme NOT IN (
      SELECT idJoueur FROM Pokemon WHERE idJoueur IS NOT NULL
 );


 -- Pokemon dans certaines équipes
 SELECT nom
 FROM Pokemon
 WHERE idJoueur IN (
      SELECT pseudonyme
      FROM Joueur
      WHERE idEquipe IN (1, 2)
 );



8.2.3 Sous-Requête EXISTS / NOT EXISTS

Plus efficace que IN pour grandes tables


  -- Joueurs ayant des pokemon
 SELECT J.pseudonyme
 FROM Joueur J
 WHERE EXISTS (
      SELECT 1 FROM Pokemon P WHERE P.idJoueur = J.pseudonyme
 );


 -- Joueurs sans pokemon
 SELECT J.pseudonyme
 FROM Joueur J
 WHERE NOT EXISTS (
      SELECT 1 FROM Pokemon P WHERE P.idJoueur = J.pseudonyme
 );



8.2.4 Sous-Requête ALL / ANY


  -- Pokemon plus fort que TOUS les pokemon de type Souris
 SELECT nom
 FROM Pokemon
 WHERE pointCombat > ALL (
      SELECT pointCombat FROM Pokemon WHERE espece = 'Souris'
 );


 -- Pokemon plus fort qu'AU MOINS UN pokemon de type Souris
 SELECT nom
 FROM Pokemon
 WHERE pointCombat > ANY (
      SELECT pointCombat FROM Pokemon WHERE espece = 'Souris'
 );



8.2.5 Sous-Requête Corrélée

Dépend de la requête externe (réévaluée pour chaque ligne)
~~~

## Page 15

~~~text
  -- Pokemon ayant le max de PC pour leur espèce
 SELECT P1.nom, P1.espece, P1.pointCombat
 FROM Pokemon P1
 WHERE P1.pointCombat = (
      SELECT MAX(P2.pointCombat)
      FROM Pokemon P2
      WHERE P2.espece = P1.espece
 );


 -- Joueurs avec plus de pokemon que la moyenne de leur équipe
 SELECT J.pseudonyme
 FROM Joueur J
 WHERE (
      SELECT COUNT(*) FROM Pokemon P WHERE P.idJoueur = J.pseudonyme
 ) > (
      SELECT AVG(cnt)
      FROM (
           SELECT COUNT(*) AS cnt
           FROM Pokemon P2
           JOIN Joueur J2 ON P2.idJoueur = J2.pseudonyme
           WHERE J2.idEquipe = J.idEquipe
           GROUP BY J2.pseudonyme
      ) AS T
 );



8.3 Opérations Ensemblistes

8.3.1 UNION

Combine les résultats (élimine les doublons)


  -- Tous les noms (joueurs et pokemon)
 SELECT personnage AS nom FROM Joueur
 UNION
 SELECT nom FROM Pokemon;


 -- UNION ALL (garde les doublons, plus rapide)
 SELECT personnage FROM Joueur
 UNION ALL
 SELECT nom FROM Pokemon;



8.3.2 INTERSECT

Retourne les lignes présentes dans les deux résultats


  -- Noms présents comme joueur ET pokemon
 SELECT personnage FROM Joueur
 INTERSECT
 SELECT nom FROM Pokemon;


 -- Simulation avec IN (si INTERSECT non supporté)
 SELECT personnage FROM Joueur
 WHERE personnage IN (SELECT nom FROM Pokemon);



8.3.3 EXCEPT / MINUS

Retourne les lignes du premier résultat sauf celles du second
~~~

## Page 16

~~~text
  -- Noms de joueurs qui ne sont pas des noms de pokemon
 SELECT personnage FROM Joueur
 EXCEPT
 SELECT nom FROM Pokemon;


 -- Simulation avec NOT IN
 SELECT personnage FROM Joueur
 WHERE personnage NOT IN (SELECT nom FROM Pokemon);



8.4 Requêtes Complexes

8.4.1 Division Relationnelle

"Trouver X qui ont TOUS les Y"

MÉTHODE 1 : Double NOT EXISTS (recommandée)


  -- Joueurs ayant capturé toutes les espèces
 SELECT J.pseudonyme
 FROM Joueur J
 WHERE NOT EXISTS (
      -- Il n'existe pas d'espèce...
      SELECT DISTINCT espece FROM Pokemon P1
      WHERE NOT EXISTS (
           -- ...que ce joueur n'a pas
           SELECT * FROM Pokemon P2
           WHERE P2.idJoueur = J.pseudonyme
           AND P2.espece = P1.espece
      )
 );


MÉTHODE 2 : COUNT avec GROUP BY


  -- Pokémon apparus dans tous les emplacements
 SELECT P.nom
 FROM Pokemon P
 JOIN Apparition A ON P.id = A.idPokemon
 GROUP BY P.id, P.nom
 HAVING COUNT(DISTINCT A.idEmplacement) = (
      SELECT COUNT(*) FROM Emplacement
 );


MÉTHODE 3 : LEFT JOIN avec NULL


  -- Joueurs ayant capturé toutes les espèces
 SELECT J.pseudonyme
 FROM Joueur J
 WHERE NOT EXISTS (
      SELECT E.espece
      FROM (SELECT DISTINCT espece FROM Pokemon) E
      LEFT JOIN Pokemon P ON E.espece = P.espece AND P.idJoueur = J.pseudonyme
      WHERE P.id IS NULL
 );



8.4.2 TOP-N et Classement
~~~

## Page 17

~~~text
 -- Top 3 des pokemon les plus forts
 SELECT nom, pointCombat
 FROM Pokemon
 ORDER BY pointCombat DESC
 LIMIT 3;


 -- Top N par groupe (ex: meilleur pokemon par espèce)
 SELECT P.*
 FROM Pokemon P
 WHERE P.id = (
       SELECT P2.id
       FROM Pokemon P2
       WHERE P2.espece = P.espece
       ORDER BY P2.pointCombat DESC
       LIMIT 1
 );


 -- Avec ROW_NUMBER (si supporté)
 SELECT nom, espece, pointCombat
 FROM (
       SELECT nom, espece, pointCombat,
                 ROW_NUMBER() OVER (PARTITION BY espece ORDER BY pointCombat DESC) AS rn
       FROM Pokemon
 ) T
 WHERE rn = 1;



8.4.3 Requêtes avec Calculs Complexes


 -- Pourcentage de pokemon par espèce
 SELECT espece,
          COUNT(*) AS nombre,
          COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Pokemon) AS pourcentage
 FROM Pokemon
 GROUP BY espece;


 -- Évolution niveau par niveau
 SELECT niveau,
          COUNT(*) AS nb_joueurs,
          AVG(nb_pokemon) AS avg_pokemon
 FROM (
       SELECT J.niveau, COUNT(P.id) AS nb_pokemon
       FROM Joueur J
       LEFT JOIN Pokemon P ON J.pseudonyme = P.idJoueur
       GROUP BY J.pseudonyme, J.niveau
 ) T
 GROUP BY niveau;



8.4.4 Requêtes Hiérarchiques
~~~

## Page 18

~~~text
  -- Matières avec leurs pré-requis (récursif)
 WITH RECURSIVE PreRequisRecursif AS (
       -- Cas de base : matières sans pré-requis
       SELECT id, nom, 0 AS niveau
       FROM Matiere
       WHERE id NOT IN (SELECT idMatiere FROM PreRequis)


       UNION ALL


       -- Cas récursif
       SELECT M.id, M.nom, PR.niveau + 1
       FROM Matiere M
       JOIN PreRequis P ON M.id = P.idMatiere
       JOIN PreRequisRecursif PR ON P.idPreRequis = PR.id
 )
 SELECT * FROM PreRequisRecursif;



8.5 Optimisation de Requêtes

8.5.1 Bonnes Pratiques


  --     ÉVITER : SELECT *
 SELECT * FROM Pokemon;      -- Charge toutes les colonnes


 --      PRÉFÉRER : Colonnes spécifiques
 SELECT nom, espece FROM Pokemon;


 --      ÉVITER : Fonctions sur colonnes indexées dans WHERE
 SELECT * FROM Pokemon WHERE UPPER(nom) = 'PIKACHU';


 --      PRÉFÉRER : Comparaison directe
 SELECT * FROM Pokemon WHERE nom = 'Pikachu';


 --      ÉVITER : OR avec colonnes différentes
 SELECT * FROM Pokemon WHERE nom = 'Pikachu' OR espece = 'Souris';


 --      PRÉFÉRER : UNION ou IN
 SELECT * FROM Pokemon WHERE nom = 'Pikachu'
 UNION
 SELECT * FROM Pokemon WHERE espece = 'Souris';


 --      ÉVITER : Sous-requêtes dans SELECT
 SELECT nom, (SELECT COUNT(*) FROM Apparition WHERE idPokemon = P.id)
 FROM Pokemon P;


 --      PRÉFÉRER : JOIN ou GROUP BY
 SELECT P.nom, COUNT(A.idPokemon)
 FROM Pokemon P
 LEFT JOIN Apparition A ON P.id = A.idPokemon
 GROUP BY P.id, P.nom;



8.5.2 Index


  -- Créer un index (accélère les recherches)
 CREATE INDEX idx_pokemon_espece ON Pokemon(espece);
 CREATE INDEX idx_joueur_equipe ON Joueur(idEquipe);


 -- Index composé
 CREATE INDEX idx_apparition ON Apparition(idPokemon, idEmplacement);


 -- Supprimer un index
 DROP INDEX idx_pokemon_espece ON Pokemon;
~~~

## Page 19

~~~text
9. EXERCICES TYPES D'EXAMENS

9.1 Exercice Type : Modélisation

ÉNONCÉ : Un zoo veut gérer ses animaux. Chaque animal a un nom, appartient à une espèce, vit dans un enclos. Une espèce a un nom scientifique, une famille, une
population estimée. Un enclos a une désignation et une localisation. Une espèce a des besoins alimentaires (aliments avec quantités).

SOLUTION :

Entités :

        Animal (nomIndividu, sexe, dateNaissance, dateArrivee, remarques)
        Espece (nomScientifique, nomVulgaire, famille, populationEstimee)
        Enclos (designation, situation)
        Aliment (nom, stock)
        Zone (nom)

Associations :

        Est_De : Animal (1,1) -- (0,N) Espece
        Vit_Dans : Animal (1,N) -- (1,1) Enclos
        Besoin : Espece (0,N) -- (1,N) Aliment {quantiteKg}
        Localisation : Espece (1,N) -- (1,N) Zone {effectifZone}
        Substitution : Aliment (1,N) -- (0,N) Aliment {tauxRemplacement}

MLD :


  Animal(nomIndividu, sexe, dateNaissance, dateArrivee, remarques, #nomScientifique, #designation)
  Espece(nomScientifique, nomVulgaire, famille, populationEstimee)
  Enclos(designation, situation)
  Aliment(nom, stock)
  Zone(nom)
  Besoin(#nomScientifique, #nomAliment, quantiteKg)
  Localisation(#nomScientifique, #nomZone, effectifZone)
  Substitution(#nomAliment, #nomSubstitut, tauxRemplacement)



9.2 Exercice Type : Normalisation

ÉNONCÉ :


  CINEMA(NumSalleCinema, adresseSalleCinema, nomSalleCinema,
            NumFilm, titreFilm, NumCatégorieFilm, intituléCatégorieFilm,
            dateDébutProjectionFilm, duréeProjectionFilm)


SOLUTION :

Dépendances fonctionnelles :

    1. NumSalleCinema → adresseSalleCinema, nomSalleCinema
    2. NumFilm → titreFilm, NumCatégorieFilm, duréeProjectionFilm
    3. NumCatégorieFilm → intituléCatégorieFilm
    4. (NumSalleCinema, NumFilm, dateDébutProjectionFilm) → ALL

1FN : (attributs atomiques)

2FN :

        adresseSalleCinema dépend de NumSalleCinema (partie de clé)
        titreFilm dépend de NumFilm (partie de clé)

Décomposition en 2FN :


  SalleCinema(NumSalleCinema, adresseSalleCinema, nomSalleCinema)
  Film(NumFilm, titreFilm, NumCatégorieFilm, duréeProjectionFilm)
  Projection(NumSalleCinema, NumFilm, dateDébutProjectionFilm)


3FN : sur Film

        NumFilm → NumCatégorieFilm → intituléCatégorieFilm (transitive)

Décomposition en 3FN :
~~~

## Page 20

~~~text
  SalleCinema(NumSalleCinema, adresseSalleCinema, nomSalleCinema)
 Film(NumFilm, titreFilm, #NumCatégorieFilm, duréeProjectionFilm)
 Categorie(NumCatégorieFilm, intituléCatégorieFilm)
 Projection(#NumSalleCinema, #NumFilm, dateDébutProjectionFilm)



9.3 Exercice Type : Requêtes SQL

Base de données : Pokemon (voir données du cours)

Questions fréquentes :


9.3.1 Requête Simple


  -- Q: Quels sont les sanctuaires commençant par 'T' ?
 SELECT * FROM Sanctuaire WHERE nom LIKE 'T%';



9.3.2 Agrégation Simple


  -- Q: Combien de combats contre les créatures divines ?
 SELECT COUNT(*) FROM Combattre;



9.3.3 Jointure Simple


  -- Q: Nom du monde de "Vah Medoh" ?
 SELECT M.nom
 FROM CreatureDivine CD
 JOIN Monde M ON CD.idMonde = M.idMonde
 WHERE CD.nom = 'Vah Medoh';



9.3.4 Agrégation


  -- Q: Quel est le niveau de sanctuaire le plus bas ?
 SELECT MIN(niveau) FROM Sanctuaire;



9.3.5 NOT IN / NOT EXISTS


  -- Q: Joueurs qui n'ont jamais mangé de plat ?
 SELECT pseudo FROM Joueur
 WHERE idJoueur NOT IN (SELECT idJoueur FROM Manger);


 -- Alternative avec EXISTS
 SELECT pseudo FROM Joueur J
 WHERE NOT EXISTS (
      SELECT 1 FROM Manger M WHERE M.idJoueur = J.idJoueur
 );



9.3.6 Moyenne avec Sous-requête


  -- Q: Moyenne de plats consommés par joueur ?
 SELECT AVG(nbPlats) AS moyennePlats
 FROM (
      SELECT COUNT(*) AS nbPlats
      FROM Manger
      GROUP BY idJoueur
 ) AS T;


 -- Alternative
 SELECT COUNT(*) / COUNT(DISTINCT idJoueur)
 FROM Manger;
~~~

## Page 21

~~~text
9.3.7 TOP avec GROUP BY


 -- Q: Joueur ayant consommé le plus de plats ?
 SELECT pseudo
 FROM Joueur J
 JOIN Manger M ON J.idJoueur = M.idJoueur
 GROUP BY J.idJoueur, pseudo
 HAVING COUNT(*) = (
      SELECT MAX(cnt)
      FROM (
            SELECT COUNT(*) AS cnt
            FROM Manger
            GROUP BY idJoueur
      ) AS T
 );


 -- Alternative avec LIMIT
 SELECT J.pseudo
 FROM Joueur J
 JOIN Manger M ON J.idJoueur = M.idJoueur
 GROUP BY J.idJoueur, J.pseudo
 ORDER BY COUNT(*) DESC
 LIMIT 1;



9.3.8 COUNT DISTINCT


 -- Q: Plat avec le plus d'ingrédients différents ?
 SELECT P.nom
 FROM Plat P
 JOIN Composer C ON P.idPlat = C.idPlat
 GROUP BY P.idPlat, P.nom
 HAVING COUNT(DISTINCT C.idIngredient) = (
      SELECT MAX(nb)
      FROM (
            SELECT COUNT(DISTINCT idIngredient) AS nb
            FROM Composer
            GROUP BY idPlat
      ) AS T
 );



9.3.9 LEFT JOIN avec COUNT


 -- Q: Nombre de plats par joueur (y compris 0) ?
 SELECT J.pseudo, COUNT(M.idPlat) AS nbPlats
 FROM Joueur J
 LEFT JOIN Manger M ON J.idJoueur = M.idJoueur
 GROUP BY J.idJoueur, J.pseudo
 ORDER BY nbPlats DESC;



9.4 Exercice Type : CREATE TABLE

 -- Q: Créer la table Commande
 CREATE TABLE Commande (
      no_commande INT PRIMARY KEY,
      montant_achat DECIMAL(10,2) NOT NULL,
      date DATE NOT NULL,
      client_id INT NOT NULL,
      vendeur_id INT NOT NULL,
      FOREIGN KEY (client_id) REFERENCES Client(client_id),
      FOREIGN KEY (vendeur_id) REFERENCES Vendeur(vendeur_id),
      CHECK (montant_achat >= 0)
 );
~~~

## Page 22

~~~text
9.5 Exercice Type : UPDATE/DELETE

  -- Q: Augmenter la commission des vendeurs de Paris de 1%
 UPDATE Vendeur
 SET commission = commission * 1.01
 WHERE ville = 'Paris';


 -- Q: Supprimer les pokémons contenant "fruit"
 DELETE FROM Pokemon
 WHERE espece LIKE '%fruit%';



9.6 Piège Classiques

Piège 1 : COUNT(*) vs COUNT(colonne)


  -- Différence importante !
 SELECT COUNT(*) FROM Pokemon;             -- Compte toutes les lignes
 SELECT COUNT(idJoueur) FROM Pokemon;      -- Compte seulement les non-NULL



Piège 2 : NULL dans NOT IN


  --    ATTENTION : Si NULL dans sous-requête, retourne vide !
 SELECT * FROM Joueur
 WHERE pseudonyme NOT IN (SELECT idJoueur FROM Pokemon);
 -- Si un Pokemon a idJoueur = NULL, résultat VIDE !


 --     SOLUTION : Filtrer NULL
 SELECT * FROM Joueur
 WHERE pseudonyme NOT IN (
       SELECT idJoueur FROM Pokemon WHERE idJoueur IS NOT NULL
 );



Piège 3 : JOIN vs WHERE pour NULL


  -- Différence avec NULL
 SELECT * FROM Joueur J, Pokemon P
 WHERE J.pseudonyme = P.idJoueur;
 -- Exclut les Pokemon sans joueur


 SELECT * FROM Joueur J
 LEFT JOIN Pokemon P ON J.pseudonyme = P.idJoueur;
 -- Inclut tous les joueurs (même sans pokemon)



Piège 4 : GROUP BY obligatoire


  --    ERREUR
 SELECT espece, nom, COUNT(*)
 FROM Pokemon
 GROUP BY espece;
 -- nom n'est ni dans GROUP BY ni agrégé !


 --     CORRECT
 SELECT espece, COUNT(*)
 FROM Pokemon
 GROUP BY espece;




10. MÉMO RAPIDE - JOUR DE L'EXAMEN
~~~

## Page 23

~~~text
  Checklist Modélisation (MCD)

             Identifiants uniques pour chaque entité
             Cardinalités cohérentes avec énoncé
             Association pour chaque relation
             Attributs au bon endroit (entité vs association)
             Pas d'attributs multivalués


  Checklist MLD

             Clés primaires soulignées
             Clés étrangères avec #
             Règles de transformation respectées
             Pas de perte d'information


  Checklist Normalisation

    1. Lister TOUTES les DF
    2. Identifier la clé
    3. Vérifier 1FN → attributs atomiques ?
    4. Vérifier 2FN → pas de DF partielle ?
    5. Vérifier 3FN → pas de DF transitive ?
    6. Décomposer si nécessaire


  Checklist CREATE TABLE

             Types de données appropriés
             PRIMARY KEY définie
             FOREIGN KEY avec ON DELETE/UPDATE
             Contraintes CHECK pour validations
             NOT NULL pour obligatoires
             DEFAULT si valeur par défaut


  Checklist Requêtes SQL

             SELECT colonnes correctes
             FROM tables nécessaires
             JOIN si plusieurs tables
             WHERE pour filtrer lignes
             GROUP BY si agrégation
             HAVING pour filtrer groupes
             ORDER BY si tri demandé
             LIMIT si top N


  Stratégies Examen

Pour Modélisation :

    1. Surligner les noms (entités)
    2. Souligner les verbes (associations)
    3. Entourer les nombres (cardinalités)
    4. Dessiner schéma au brouillon
    5. Vérifier avec énoncé

Pour Normalisation :

    1. Écrire toutes les DF clairement
    2. Numéroter les étapes
    3. Justifier chaque décomposition
    4. Vérifier perte d'info

Pour SQL :

    1. Lire question 2 fois
    2. Identifier tables nécessaires
    3. Schématiser jointures si besoin
    4. Écrire requête étape par étape
    5. Relire et tester mentalement


  Formules Utiles
~~~

## Page 24

~~~text
  -- Moyenne par groupe
 SELECT colonne, AVG(valeur) FROM table GROUP BY colonne;


 -- Top N
 SELECT * FROM table ORDER BY colonne DESC LIMIT N;


 -- Pourcentage
 SELECT colonne, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM table)
 FROM table GROUP BY colonne;


 -- Division (tous les Y)
 SELECT X FROM TableX
 WHERE NOT EXISTS (
       SELECT * FROM TableY
       WHERE NOT EXISTS (
            SELECT * FROM TableXY
            WHERE TableXY.X = TableX.X AND TableXY.Y = TableY.Y
       )
 );




  BON COURAGE POUR TON PARTIEL !

Derniers conseils :

       Lis bien les énoncés (2 fois)
       Gère ton temps (modélisation = 30%, normalisation = 20%, SQL = 50%)
       Vérifie tes réponses
       N'oublie pas les points-virgules en SQL !
       Justifie tes choix en normalisation

Tu vas cartonner !
~~~
