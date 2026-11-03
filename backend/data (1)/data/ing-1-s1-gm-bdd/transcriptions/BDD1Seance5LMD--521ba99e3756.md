# BDD1Seance5LMD.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1XX466QilnzxOxaQ9MfL1jGsH6xsSDCJe) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
    Base de données


                Séance 5
Langage de Manipulation de Données (LMD)
~~~

## Page 2

~~~text
Plan
 INSERT
 UPDATE
 DELETE
 SELECT
 ◼ Projection
 ◼ Restriction
 ◼ Tri
 ◼ Fonction
~~~

## Page 3

~~~text
SQL : Langage de Manipulation
des Données (LMD)
 Le LDD :
  ◼ permet d’effectuer des opérations sur les structures
 Le LMD
  ◼ permet d’effectuer des opérations sur les données
  ◼ concerne le cycle de vie des données dans une
    application
  ◼ implémente le modèle «CRUDE» (Create, Read,
    Update, Delete).




                                                     3
~~~

## Page 4

~~~text
 L’implémentation du CRUDE en SQL

 Le CRUDE en SQL est constitué des
  quatre ordres :

  ◼ INSERT : insertion d’enregistrement(s)
  ◼ UPDATE : modification d’enregistrement(s)
  ◼ DELETE : suppression d’enregistrement(s)
  ◼ SELECT : accès aux enregistrement(s)



                                            4
~~~

## Page 5

~~~text
LMD : tables pour les exemples
CREATE TABLE employe (
  nom VARCHAR(30),
  prenom VARCHAR(30),
  date_embauche DATE);

CREATE TABLE etudiant (
  nom VARCHAR(30),
  prenom VARCHAR(30),
  classe CHAR(4) DEFAULT 'ING1');
                                    5
~~~

## Page 6

~~~text
INSERT : ajout d’une ligne
 Syntaxe simplifiée :
     INSERT INTO <nom_table>
     VALUES (<expr>[,<expr>...]);

 Exemple :
  INSERT INTO employe
  VALUES('DERAY', 'ODILE','1972-09-01');


 Attention à l’ordre des colonnes !

                                           6
~~~

## Page 7

~~~text
INSERT : ajout d’une ligne
 Syntaxe INSERT explicite (plus sûr) :
  INSERT INTO <nom_table> (<col1> [, … ])
  VALUES (<expr1> [, … ]);

 Exemple :
  INSERT INTO employe
    (nom,prenom,date_embauche)
  VALUES('DERAY','ODILE','1972-09-01');


                                          7
~~~

## Page 8

~~~text
 INSERT : insertion partielle
 N-uplet partiel complété par des valeurs
  NULL ou par défaut.
 Complétion explicite :
    INSERT INTO employe
    VALUES('DERAY','ODILE',NULL);
    CREATE TABLE etudiant (...,
    classe CHAR(4) DEFAULT 'ING1');
    INSERT INTO etudiant
    VALUES('DUPONT','EMILE',DEFAULT);

                                             8
~~~

## Page 9

~~~text
INSERT : insertion partielle
 Complétion implicite :
  ◼ avec la valeur NULL
    INSERT INTO employe (nom, prenom)
    VALUES('DERAY','ODILE');
  ◼ avec la valeur par défaut
    INSERT INTO etudiant (nom, prenom)
    VALUES('DUPONT','EMILE');




                                         9
~~~

## Page 10

~~~text
INSERT : insertion multiple
 Insérer le résultat d’un SELECT
    INSERT INTO personne (nom, prenom)
    SELECT nom, prenom FROM etudiant;

 Ajustements possibles
  ◼ Insertion conditionnelle
  ◼ Répartition sur plusieurs tables



                                       10
~~~

## Page 11

~~~text
 INSERT : contraintes
 Attention aux respects des contraintes !

  ◼ Clés primaires et UNIQUE (pas de doublons)

  ◼ Clés étrangères (existence)

  ◼ CHECK, NOT NULL




                                           11
~~~

## Page 12

~~~text
 UPDATE : modification des données
 Mettre à jour les n-uplets d'une table vérifiant
  un certain prédicat :
  UPDATE <nom_table>
  SET <col>=<expr>[,<col>=<expr>…]
  [WHERE <predicat>];

 Les expressions sont évaluées pour chaque n-
  uplets vérifiant le prédicat.
 Si aucune clause WHERE n'est spécifiée, tous
  les enregistrements de la table sont modifiés !

                                               12
~~~

## Page 13

~~~text
UPDATE : exemple


UPDATE personne
SET date_naissance = '1900-01-01’
WHERE date_naissance IS NULL;




                                    13
~~~

## Page 14

~~~text
DELETE : suppression des données
 Supprime d’une table les n-uplets qui
  vérifient un certain prédicat.
 Syntaxe générale :
              DELETE FROM <tab>
              [WHERE <predicat>];


 Si aucune clause WHERE n'est spécifiée,
  tous les tuples sont supprimés (cf.
  update) !
                                          14
~~~

## Page 15

~~~text
DELETE : exemples



 DELETE FROM personne;

 DELETE FROM personne
 WHERE date_naissance IS NULL;



                                 15
~~~

## Page 16

~~~text
SELECT : extraction de données
 Récupérer les informations stockées
  dans la base de manière structurée
 Syntaxe générale :
      SELECT { <col>[, <col>… ] | *}
      FROM <nom_table>
      [WHERE <expr>];



                                        16
~~~

## Page 17

~~~text
Forme simple du SELECT

 Récupérer tous les enregistrements
  de la table 'ma_table'
       SELECT * FROM ma_table;




                                       17
~~~

## Page 18

~~~text
Projection avec SELECT

 Récupérer seulement les colonnes c1
  et c2 :
    SELECT c1, c2 FROM ma_table;

 Garder les éventuels doublons
  (non ensembliste)


                                        18
~~~

## Page 19

~~~text
 Unicité avec DISTINCT
 Projection en éliminant les doublons:
    SELECT DISTINCT c1, c2
    FROM ma_table;

 Algèbre relationnelle :
    PC1,C2 (ma_table)


                                          19
~~~

## Page 20

~~~text
Restriction avec la clause WHERE
 Ajout d’un prédicat avec WHERE :
    SELECT *
    FROM ma_table
    WHERE <predicat>;
 Exemple :
    SELECT *
    FROM ma_table
    WHERE c1 = 600;
 Algèbre relationnelle : sC1=600(ma_table)

                                              20
~~~

## Page 21

~~~text
Les formes de la clause WHERE
 Opérateurs de comparaison :
      = , <> , <= , >= , < , >
 Opérateurs logiques
            AND, OR, NOT
 Exemple :
    SELECT *
    FROM ma_table
    WHERE c1 <> 12 AND c2 = 15;
                                  21
~~~

## Page 22

~~~text
Le cas particulier de la nullité
 Cas particulier des champs ‘NULL’ :
  Il sont testés avec le prédicat IS NULL ou
  IS NOT NULL.


 Exemple :
          SELECT *
          FROM ma_table
          WHERE c2 IS NULL;

                                               22
~~~

## Page 23

~~~text
L’opérateur LIKE

 L’opérateur LIKE permet de tester
  les chaînes de caractères avec
  l’expression d’un motif (pattern)

 Les méta-caractères sont :
  _ : un seul caractère
  % : zéro ou plusieurs caractères
                                      23
~~~

## Page 24

~~~text
L’opérateur LIKE : exemples
 Toutes les personnes dont le nom commence
  par 'A' :
     SELECT *
     FROM personne
     WHERE nom LIKE 'A%' ;
 Tous les prénoms dont le nom contient un 'X'
  en deuxième position.
     SELECT prenom
     FROM personne
     WHERE nom LIKE '_X%' ;
                                                 24
~~~

## Page 25

~~~text
Autres opérateurs de caractères
 Concaténation : CONCAT

  SELECT CONCAT(first_name,' ',last_name)
  FROM …;


 Sous-chaînes :
  SUBSTR(chaîne, pos, long)
    ATTENTION : En SQL les chaînes de caractères sont
                 indicées à partir de 1



                                                        25
~~~

## Page 26

~~~text
Conversion de caractères

 En majuscule : UPPER(chaîne)

 En minuscule : LOWER(chaîne)

 Exemple :
  SELECT * FROM personne
  WHERE UPPER(nom) = UPPER('Dupont');




                                        26
~~~

## Page 27

~~~text
Tri avec ORDER BY
 Syntaxe :

  SELECT ...
  FROM ma_table
  [WHERE ...]
  ORDER BY COL1 [ASC|DESC]
         [, COL2 [ASC|DESC]*;




                                27
~~~

## Page 28

~~~text
Tri avec ORDER BY : exemple
 Tri de personne par année décroissante puis par nom dans
  l’ordre alphabétique :
      SELECT *
      FROM PERSONNE
      ORDER BY ANNEE DESC, NOM;




                                                      28
~~~

## Page 29

~~~text
  Fonction sur une ligne
 Fonctions disponibles
  ◼ mathématiques : +, -, * , /
  ◼ chaînes de caractères, dates
 Exemple :
  ◼ Montant total d’une ligne de commande
  SELECT nom, quantite, prix_unitaire, quantite*prix_unitaire
  FROM ligne_commande;

  ◼ Renommage avec le mot-clé AS :
  SELECT nom, quantite*prix_unitaire AS prix_total
  FROM ligne_commande;

                                                          29
~~~

## Page 30

~~~text
Fonction sur une colonne
 Calcul sur toutes les occurrences d’une
  colonne: AVG, SUM, MIN, MAX, COUNT,
  VARIANCE, STDDEV


SELECT fonction(un_attribut) FROM ma_table;




                                            30
~~~

## Page 31

~~~text
Fonction sur une colonne : exemples

SELECT COUNT(*) FROM personne;
  personne   id nom           prenom
             1 DERAY           Odile    R count
             2   DUPONT       Emile         3
             3   DURAND       Norbert


SELECT AVG(prix) FROM produit;
  produit    libelle   prix
             chaise    25               R   avg
             table     225                   90
             lampe     20
                                                  31
~~~
