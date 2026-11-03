# FICHE REVISION-BDD.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1SOIceGt8pv44-yZzN5iLN6o88xf5CgMu) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Guide de Révision
Bases de Données
SQL  Modélisation  Normalisation



    Analyse des examens 2020-2025




        CY Tech - ING1 GM
          Année 2024-2025
~~~

## Page 2

~~~text
Révision Bases de Données                                                               CY Tech ING1-GM


Contents


1 Patterns SQL Récurrents (10-12 points)                                                                    2
   1.1 Pattern #1 : SELECT Simple avec WHERE (5/5 examens) . . . . . . . . . . . . . .                      2
   1.2 Pattern #2 : LIKE avec Wildcards (5/5 examens) . . . . . . . . . . . . . . . . . . . .               2
   1.3 Pattern #3 : Agrégations (COUNT, MAX, MIN, AVG) (5/5 examens) . . . . . . . .                        3
   1.4 Pattern #4 : INNER JOIN (5/5 examens) . . . . . . . . . . . . . . . . . . . . . . . .                3
   1.5 Pattern #5 : GROUP BY avec COUNT/SUM (5/5 examens) . . . . . . . . . . . . .                         4
   1.6 Pattern #6 : HAVING (Filtrer après GROUP BY) (5/5 examens) . . . . . . . . . . .                     4
   1.7 Pattern #7 : LEFT JOIN (inclure tous) (4/5 examens) . . . . . . . . . . . . . . . . .                5
   1.8 Pattern #8 : Sous-requêtes avec NOT IN (5/5 examens) . . . . . . . . . . . . . . . .                 6
   1.9 Pattern #9 : Sous-requêtes avec MAX/MIN (5/5 examens) . . . . . . . . . . . . . . .                  7
   1.10 Pattern #10 : DIVISION RELATIONNELLE (4/5 examens) DIFFICILE . . . . . . .                          7
   1.11 Pattern #11 : UPDATE (3/5 examens) . . . . . . . . . . . . . . . . . . . . . . . . . .              9
   1.12 Pattern #12 : CREATE TABLE (3/5 examens) . . . . . . . . . . . . . . . . . . . . .                 10
   1.13 Pattern #13 : INSERT INTO (2/5 examens) . . . . . . . . . . . . . . . . . . . . . . .              10
2 Récapitulatif : Ordre d'une requête SQL                                                                  12
   2.1 Ordre d'écriture (syntaxe) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      12
   2.2 Ordre d'exécution (logique) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       12
3 Modélisation : MCD et MLD (5-7 points)                                                                   13
   3.1   Concepts clés . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
   3.2   Relations N:M avec attributs (5/5 examens) . . . . . . . . . . . . . . . . . . . . . . . .        13
   3.3   Cardinalités importantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    13
   3.4   Checklist MCD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     13
   3.5   Checklist MLD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     14
4 Normalisation : 3FN et BCNF (3-4 points)                                                                 15
   4.1   Dénitions essentielles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   15
   4.2   Les 3 formes normales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     15
   4.3   BCNF (Forme Normale de Boyce-Codd) . . . . . . . . . . . . . . . . . . . . . . . . . .            15
   4.4   Méthode pour lister les DF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      15
   4.5   Exemple : CINEMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        15
   4.6   Exemple : Ville/Location . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      16
5 Pièges Fréquents et Erreurs à Éviter                                                                     17
   5.1 Erreurs SQL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     17
   5.2 Erreurs Modélisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      17
   5.3 Erreurs Normalisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       17
6 Stratégie d'Examen                                                                                       18
   6.1 Répartition du temps (2h = 120 minutes) . . . . . . . . . . . . . . . . . . . . . . . . .           18
   6.2 Ordre de traitement recommandé . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          18
   6.3 Points à vérier en relecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     18
7 Récapitulatif : Les 20 Points Clés                                                                       19
8 Exemples Complets d'Examens                                                                              20
   8.1 Exemple 1 : Mario Kart (2021) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         20
   8.2 Exemple 2 : Commandes (2022-2023) . . . . . . . . . . . . . . . . . . . . . . . . . . . .           20




                                                      1
~~~

## Page 3

~~~text
Révision Bases de Données                                                               CY Tech ING1-GM


9 Annexe : Aide-mémoire SQL                                                                                21
   9.1   Fonctions d'agrégation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
   9.2   Opérateurs de comparaison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       21
   9.3   Opérateurs logiques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   21
   9.4   Fonctions de chaînes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21




                                                      2
~~~

## Page 4

~~~text
     Révision Bases de Données                                                CY Tech ING1-GM


     1     Patterns SQL Récurrents (10-12 points)

     1.1 Pattern #1 : SELECT Simple avec WHERE (5/5 examens)
          EXEMPLE
          Questions types :
             Sanctuaires commençant par la lettre T
             Usines de Marseille
             Vendeurs de Paris
 1 SELECT colonne1 , colonne2 , ...
 2 FROM Table
 3 WHERE condition ;
 4
 5 -- Exemple
 6 SELECT nom , niveau
 7 FROM Sanctuaire
 8 WHERE nom LIKE 'T % ';

                                 Listing 1: Template SELECT avec WHERE


     1.2 Pattern #2 : LIKE avec Wildcards (5/5 examens)
          IMPORTANT
          À maîtriser ABSOLUMENT - Tombe dans 100% des examens !
 1   -- 1. Commence par ( ex : commence par 'T ')
 2   WHERE nom LIKE 'T % '
 3
 4   -- 2. Se termine par ( ex : termine par 'Z ')
 5   WHERE nom LIKE '% Z '
 6
 7   -- 3. Contient ( ex : contient ' citron ')
 8   WHERE description LIKE '% citron % '
 9
10   -- 4. Longueur fixe ( ex : 6 caracteres , commence par DEF , termine par Z )
11   WHERE nom LIKE ' DEF___Z ' -- 3 underscores = 3 caracteres

                                  Listing 2: Les 4 patterns LIKE essentiels

          EXEMPLE
          Exemples des examens :
      1 -- Clients avec nom de 6 caracteres commencant par DEF et terminant par Z
      2 SELECT *
      3 FROM Client
      4 WHERE nom LIKE ' DEF___Z ' AND LENGTH ( nom ) = 6;
      5
      6 -- Patisseries dont la description contient le mot " sale "
      7 SELECT nom
      8 FROM Patisserie
      9 WHERE description LIKE '% sale % ';




                                                       3
~~~

## Page 5

~~~text
     Révision Bases de Données                                                     CY Tech ING1-GM


     1.3 Pattern #3 : Agrégations (COUNT, MAX, MIN, AVG) (5/5 examens)
 1 -- COUNT : Compter le nombre de lignes
 2 SELECT COUNT (*) AS nombre_total
 3 FROM Table ;
 4
 5 -- MAX : Valeur maximale
 6 SELECT MAX ( attribut ) AS maximum
 7 FROM Table ;
 8
 9 -- MIN : Valeur minimale
10 SELECT MIN ( attribut ) AS minimum
11 FROM Table ;
12
13 -- AVG : Moyenne
14 SELECT AVG ( attribut ) AS moyenne
15 FROM Table ;
16
17 -- SUM : Somme
18 SELECT SUM ( attribut ) AS total
19 FROM Table ;

                            Listing 3: Les 5 fonctions d'agrégation essentielles

          EXEMPLE
          Questions types des examens :
      1 -- 1. Compter le nombre de combats
      2 SELECT COUNT (*) AS nb_combats
      3 FROM Combattre ;
      4
      5 -- 2. Note la plus elevee
      6 SELECT MAX ( note ) AS note_max
      7 FROM Client ;
      8
      9 -- 3. Niveau de sanctuaire le plus bas
     10 SELECT MIN ( niveau ) AS niveau_min
     11 FROM Sanctuaire ;
     12
     13 -- 4. Moyenne de temps de cuisson
     14 SELECT AVG ( tempsCuisson ) AS temps_moyen
     15 FROM Patisserie ;




     1.4 Pattern #4 : INNER JOIN (5/5 examens)
 1 SELECT a . colonne1 , b . colonne2
 2 FROM Table1 a
 3 INNER JOIN Table2 b ON a . id = b . fk_id
 4 WHERE condition ;

                                    Listing 4: Template INNER JOIN




                                                     4
~~~

## Page 6

~~~text
    Révision Bases de Données                                              CY Tech ING1-GM


         EXEMPLE
         Exemples des examens :
     1 -- 1. Nom du monde de la creature divine " Vah Medoh "
     2 SELECT m . nom
     3 FROM CreatureDivine cd
     4 INNER JOIN Monde m ON cd . idMonde = m . idMonde
     5 WHERE cd . nom = ' Vah Medoh ';
     6
     7 -- 2. Voitures appartenant a Mario
     8 SELECT p . nom AS joueur , v . nom AS voiture , v . vitesse
     9 FROM Voiture v
    10 INNER JOIN Personnage p ON v . idPerso = p. id
    11 WHERE p . nom = ' Mario ';
    12
    13 -- 3. Commission des vendeurs a Paris
    14 SELECT vendeur_id , nom , commission
    15 FROM Vendeur
    16 WHERE ville = ' Paris ';




    1.5 Pattern #5 : GROUP BY avec COUNT/SUM (5/5 examens)
         IMPORTANT
         Règle d'or : Si vous utilisez COUNT/SUM/AVG avec d'autres colonnes, GROUP BY est
         OBLIGATOIRE !
1 SELECT colonne_groupe , COUNT (*) AS compteur
2 FROM Table
3 GROUP BY colonne_groupe ;

                                    Listing 5: Template GROUP BY

         EXEMPLE
         Questions types :
     1 -- 1. Note la plus elevee par ville
     2 SELECT ville , MAX ( note ) AS note_max
     3 FROM Client
     4 GROUP BY ville ;
     5
     6 -- 2. Nombre total de plats consommes par joueur
     7 SELECT j . pseudo , COUNT ( m . idPlat ) AS nb_plats
     8 FROM Joueur j
     9 LEFT JOIN Manger m ON j . idJoueur = m . idJoueur
    10 GROUP BY j . idJoueur , j . pseudo
    11 ORDER BY nb_plats DESC ;
    12
    13 -- 3. Nombre de produits delivres par fournisseur
    14 SELECT NumF , COUNT (*) AS nb_produits
    15 FROM PUF
    16 GROUP BY NumF ;




    1.6 Pattern #6 : HAVING (Filtrer après GROUP BY) (5/5 examens)
         ATTENTION
         Piège fréquent : WHERE ltre AVANT le regroupement, HAVING ltre APRÈS !

                                                    5
~~~

## Page 7

~~~text
    Révision Bases de Données                                                         CY Tech ING1-GM


1 -- WHERE : filtre les lignes AVANT le regroupement
2 SELECT ville , COUNT (*) AS nb_clients
3 FROM Client
4 WHERE note > 3
5 GROUP BY ville ;
6
7  -- HAVING : filtre les groupes APRES le regroupement
8  SELECT ville , COUNT (*) AS nb_clients
 9 FROM Client
10 GROUP BY ville
11 HAVING COUNT (*) > 5;

                                       Listing 6: WHERE vs HAVING

         EXEMPLE
         Exemples des examens :
     1 -- Montant max > 2000 euros par client
     2 SELECT client_id , date , MAX ( montant_achat ) AS montant_max
     3 FROM Commande
     4 GROUP BY client_id , date
     5 HAVING MAX ( montant_achat ) > 2000;
     6
     7 -- Patisserie avec le plus d ' ingredients
     8 SELECT p . nom
     9 FROM Plat p
    10 JOIN Composer c ON p . idPlat = c . idPlat
    11 GROUP BY p . idPlat , p . nom
    12 HAVING COUNT (*) = (
    13     SELECT MAX ( nb_ingredients )
    14     FROM (
    15          SELECT COUNT (*) AS nb_ingredients
    16          FROM Composer
    17          GROUP BY idPlat
    18     ) AS temp
    19 ) ;




    1.7 Pattern #7 : LEFT JOIN (inclure tous) (4/5 examens)
         ASTUCE
         Indice : Utilisez LEFT JOIN quand la question dit "y compris ceux qui..." ou "même ceux qui
         n'ont pas..."

1 SELECT a . nom , COUNT ( b . id ) AS compteur
2 FROM TablePrincipale a
3 LEFT JOIN TableSecondaire b ON a . id = b . fk_id
4 GROUP BY a . id , a . nom ;

                         Listing 7: LEFT JOIN pour inclure tous les enregistrements




                                                     6
~~~

## Page 8

~~~text
    Révision Bases de Données                                             CY Tech ING1-GM


         EXEMPLE
         Questions types :
     1 -- 1. Joueurs y compris ceux qui n ' ont rien consomme
     2 SELECT j . pseudo , COUNT ( m . idPlat ) AS nb_plats
     3 FROM Joueur j
     4 LEFT JOIN Manger m ON j . idJoueur = m . idJoueur
     5 GROUP BY j . idJoueur , j . pseudo
     6 ORDER BY nb_plats DESC ;
     7
     8 -- 2. Clients avec ou sans commande
     9 SELECT c . nom , COUNT ( cmd . no_commande ) AS nb_commandes
    10 FROM Client c
    11 LEFT JOIN Commande cmd ON c . client_id = cmd . client_id
    12 GROUP BY c . client_id , c . nom
    13 ORDER BY nb_commandes DESC ;
    14
    15 -- 3. Personnages avec nombre de courses ( meme 0)
    16 SELECT p . nom , COUNT ( r . dateCourse ) AS nb_courses
    17 FROM Personnage p
    18 LEFT JOIN RealiserUneCourse r ON p . id = r . idPerso
    19 GROUP BY p . id , p . nom ;




    1.8 Pattern #8 : Sous-requêtes avec NOT IN (5/5 examens)
         IMPORTANT
         Question type : "Quels sont ceux qui n'ont JAMAIS..."  NOT IN
1 SELECT colonne
2 FROM Table1
3 WHERE id NOT IN (
4     SELECT fk_id
5     FROM Table2
6 );

                                      Listing 8: Template NOT IN

         EXEMPLE
         Exemples des examens :
     1 -- 1. Joueurs qui n ' ont jamais mange de plat
     2 SELECT pseudo
     3 FROM Joueur
     4 WHERE idJoueur NOT IN (
     5     SELECT idJoueur
     6     FROM Manger
     7 );
     8
     9 -- 2. Usines qui ne recoivent aucun produit rouge d ' un fournisseur parisien
    10 SELECT NumU
    11 FROM Usine
    12 WHERE NumU NOT IN (
    13     SELECT DISTINCT puf . NumU
    14     FROM PUF puf
    15     JOIN Produit p ON puf . NumP = p . NumP
    16     JOIN Fournisseur f ON puf . NumF = f . NumF
    17     WHERE p . Couleur = ' rouge ' AND f . VilleF = ' Paris '
    18 ) ;




                                                   7
~~~

## Page 9

~~~text
    Révision Bases de Données                                                       CY Tech ING1-GM


    1.9 Pattern #9 : Sous-requêtes avec MAX/MIN (5/5 examens)
1 -- Methode 1 : Sous - requete
2 SELECT nom
3 FROM Table
4 WHERE attribut = ( SELECT MAX ( attribut ) FROM Table ) ;
5
6  -- Methode 2 : ORDER BY + LIMIT
7  SELECT nom
 8 FROM Table
 9 ORDER BY attribut DESC
10 LIMIT 1;

                            Listing 9: Template pour trouver le maximum/minimum

         EXEMPLE
         Exemples des examens :
     1 -- 1. Joueur qui a consomme le plus de plats ( sans doublon )
     2 SELECT DISTINCT j . pseudo
     3 FROM Joueur j
     4 JOIN Manger m ON j . idJoueur = m . idJoueur
     5 GROUP BY j . idJoueur , j . pseudo
     6 HAVING COUNT (*) = (
     7     SELECT MAX ( nb_plats )
     8     FROM (
     9         SELECT COUNT (*) AS nb_plats
    10         FROM Manger
    11         GROUP BY idJoueur
    12     ) AS temp
    13 ) ;
    14
    15 -- 2. Produit le plus leger
    16 SELECT NumP
    17 FROM Produit
    18 WHERE Poids = ( SELECT MIN ( Poids ) FROM Produit ) ;
    19
    20 -- 3. Circuit realise le plus recemment
    21 SELECT c . nom , r . dateCourse , p . nom
    22 FROM Circuit c
    23 JOIN RealiserUneCourse r ON c . id = r . idCircuit
    24 JOIN Personnage p ON r . idPerso = p . id
    25 WHERE r . dateCourse = ( SELECT MAX ( dateCourse ) FROM RealiserUneCourse ) ;




    1.10 Pattern #10 : DIVISION RELATIONNELLE (4/5 examens) DIFFICILE
         IMPORTANT
         Question magique : Dès que vous voyez le mot "TOUS"  Division relationnelle !
         Exemples : "tous les circuits", "tous les vendeurs", "toutes les usines"

1  -- Template general
2  SELECT a . nom
 3 FROM TableA a
 4 WHERE NOT EXISTS (
 5     SELECT *
 6     FROM TableTous t
 7     WHERE NOT EXISTS (
 8          SELECT *
 9          FROM TableRelation r
10          WHERE r . fk_a = a . id AND r . fk_t = t . id


                                                         8
~~~

## Page 10

~~~text
     Révision Bases de Données                                                     CY Tech ING1-GM


11         )
12   );

                       Listing 10: Méthode 1 : Double NOT EXISTS (recommandée)

          EXEMPLE
          Exemple 1 : Joueurs qui ont réalisé TOUS les circuits
      1 SELECT p . nom
      2 FROM Personnage p
      3 WHERE NOT EXISTS (
      4     SELECT *
      5     FROM Circuit c
      6     WHERE NOT EXISTS (
      7          SELECT *
      8          FROM RealiserUneCourse r
      9          WHERE r . idPerso = p . id AND r . idCircuit = c . id
     10     )
     11 ) ;




 1 -- Template general
 2 SELECT a . nom
 3 FROM TableA a
 4 JOIN TableRelation r ON a . id = r . fk_a
 5 GROUP BY a . id , a . nom
 6 HAVING COUNT ( DISTINCT r . fk_t ) = ( SELECT COUNT (*) FROM TableTous ) ;

                              Listing 11: Méthode 2 : COUNT avec HAVING

          EXEMPLE
          Exemple 2 : Clients qui ont commandé à TOUS les vendeurs
      1 SELECT c . nom
      2 FROM Client c
      3 JOIN Commande cmd ON c . client_id = cmd . client_id
      4 GROUP BY c . client_id , c . nom
      5 HAVING COUNT ( DISTINCT cmd . vendeur_id ) = ( SELECT COUNT (*) FROM Vendeur ) ;




          EXEMPLE
          Exemple 3 : Fournisseurs qui approvisionnent TOUTES les usines
      1 SELECT f . NumF
      2 FROM Fournisseur f
      3 JOIN PUF puf ON f . NumF = puf . NumF
      4 GROUP BY f . NumF
      5 HAVING COUNT ( DISTINCT puf . NumU ) = ( SELECT COUNT (*) FROM Usine ) ;




                                                      9
~~~

## Page 11

~~~text
    Révision Bases de Données                                               CY Tech ING1-GM


         EXEMPLE
         Exemple 4 : Usines qui achètent TOUS les produits du fournisseur 3
     1 -- Methode 1 : Double NOT EXISTS
     2 SELECT u . NumU
     3 FROM Usine u
     4 WHERE NOT EXISTS (
     5     SELECT *
     6     FROM PUF puf1
     7     WHERE puf1 . NumF = 3
     8     AND NOT EXISTS (
     9          SELECT *
    10          FROM PUF puf2
    11          WHERE puf2 . NumU = u . NumU
    12          AND puf2 . NumF = 3
    13          AND puf2 . NumP = puf1 . NumP
    14     )
    15 ) ;
    16
    17 -- Methode 2 : COUNT avec HAVING
    18 SELECT puf . NumU
    19 FROM PUF puf
    20 WHERE puf . NumF = 3
    21 GROUP BY puf . NumU
    22 HAVING COUNT ( DISTINCT puf . NumP ) = (
    23     SELECT COUNT ( DISTINCT NumP )
    24     FROM PUF
    25     WHERE NumF = 3
    26 ) ;




    1.11 Pattern #11 : UPDATE (3/5 examens)
1 UPDATE Table
2 SET colonne = nouvelle_valeur
3 WHERE condition ;

                                     Listing 12: Template UPDATE

         ATTENTION
         ATTENTION : Toujours mettre un WHERE sauf si vous voulez modier TOUTES les lignes
         !




                                                  10
~~~

## Page 12

~~~text
    Révision Bases de Données                                             CY Tech ING1-GM


         EXEMPLE
         Exemples des examens :
     1 -- 1. Augmenter la commission des vendeurs de Paris de 1%
     2 UPDATE Vendeur
     3 SET commission = commission * 1.01
     4 WHERE ville = ' Paris ';
     5
     6 -- 2. Changer la ville du fournisseur 7
     7 UPDATE Fournisseur
     8 SET VilleF = ' Lyon '
     9 WHERE NumF = 7;
    10
    11 -- 3. Changer le niveau de difficulte des patisseries contenant " citron "
    12 UPDATE Patisserie
    13 SET difficulte = ' Difficile '
    14 WHERE nom LIKE '% citron % ';




    1.12 Pattern #12 : CREATE TABLE (3/5 examens)
1 CREATE TABLE NomTable (
2     id INT PRIMARY KEY ,
3     attribut1 VARCHAR (50) NOT NULL ,
4     attribut2 INT ,
5     attribut3 DATE ,
6     fk_id INT ,
7     FOREIGN KEY ( fk_id ) REFERENCES AutreTable ( id )
8 );

                            Listing 13: Template CREATE TABLE complet

         EXEMPLE
         Exemples des examens :
     1 -- 1. Creer la table Commande
     2 CREATE TABLE Commande (
     3     no_commande INT PRIMARY KEY ,
     4     montant_achat DECIMAL (10 ,2) ,
     5     date DATE ,
     6     client_id INT ,
     7     vendeur_id INT ,
     8     FOREIGN KEY ( client_id ) REFERENCES Client ( client_id ) ,
     9     FOREIGN KEY ( vendeur_id ) REFERENCES Vendeur ( vendeur_id )
    10 ) ;
    11
    12 -- 2. Creer la table PUF ( cle primaire composite )
    13 CREATE TABLE PUF (
    14     NumP INT ,
    15     NumU INT ,
    16     NumF INT ,
    17     Quantite INT ,
    18     PRIMARY KEY ( NumP , NumU , NumF ) ,
    19     FOREIGN KEY ( NumP ) REFERENCES Produit ( NumP ) ,
    20     FOREIGN KEY ( NumU ) REFERENCES Usine ( NumU ) ,
    21     FOREIGN KEY ( NumF ) REFERENCES Fournisseur ( NumF )
    22 ) ;




    1.13 Pattern #13 : INSERT INTO (2/5 examens)


                                                 11
~~~

## Page 13

~~~text
    Révision Bases de Données                                         CY Tech ING1-GM


1   INSERT INTO Table ( colonne1 , colonne2 , ...)
2   VALUES ( valeur1 , valeur2 , ...) ;
3
4 -- Inserer plusieurs lignes
5 INSERT INTO Table ( colonne1 , colonne2 )
6 VALUES
7     ( valeur1a , valeur2a ) ,
8     ( valeur1b , valeur2b ) ,
9     ( valeur1c , valeur2c ) ;

                                 Listing 14: Template INSERT INTO

         EXEMPLE
         Exemple :
     1 -- Ajouter des donnees dans la table Contenir
     2 INSERT INTO Contenir ( idRecette , idIngredient , quantite )
     3 VALUES
     4     (3 , 1 , 300) ,
     5     (3 , 5 , 150) ,
     6     (3 , 6 , 200) ,
     7     (3 , 7 , 3) ;




                                                12
~~~

## Page 14

~~~text
    Révision Bases de Données                                                    CY Tech ING1-GM


    2        Récapitulatif : Ordre d'une requête SQL

        IMPORTANT
        Ordre d'écriture vs Ordre d'exécution
    2.1 Ordre d'écriture (syntaxe)
1 SELECT colonne1 , colonne2 , ...
2 FROM table1
3 JOIN table2 ON condition
4 WHERE condition
5 GROUP BY colonne
6 HAVING condition_agregation
7 ORDER BY colonne ASC / DESC
8 LIMIT nombre ;

                         Listing 15: Ordre dans lequel vous ÉCRIVEZ la requête


    2.2 Ordre d'exécution (logique)
        1. FROM : Identier les tables sources
        2. JOIN : Joindre les tables
        3. WHERE : Filtrer les lignes AVANT agrégation
        4. GROUP BY : Regrouper les données
        5. HAVING : Filtrer les groupes APRÈS agrégation
        6. SELECT : Sélectionner les colonnes
        7. ORDER BY : Trier les résultats
        8. LIMIT : Limiter le nombre de résultats




                                                  13
~~~

## Page 15

~~~text
    Révision Bases de Données                                                       CY Tech ING1-GM


    3     Modélisation : MCD et MLD (5-7 points)

    3.1 Concepts clés
        ASTUCE
        Pattern le plus fréquent (4/5 examens) : Distinction Type vs Instance
           Type = Catalogue, référence (données stables)
           Instance = Occurrence réelle (données dynamiques)
    3.2 Relations N:M avec attributs (5/5 examens)
        EXEMPLE
        Règle : Une relation N:M devient une table d'association avec :
           Clé primaire composite (les deux FK)
           Les attributs de la relation
1   MCD :
2   TYPE_PRODUIT (1 , N ) -- COMPOSE ( quantite ) -- (1 , N ) TYPE_COMPOSANT
3
4 MLD :
5 COMPOSE      ( ref_type_produit , ref_type_composant , quantite )
6       PK :   ( ref_type_produit , ref_type_composant )
7       FK :   ref_type_produit REFERENCES TYPE_PRODUIT
8       FK :   ref_type_composant REFERENCES TYPE_COMPOSANT

                                       Listing 16: Exemple : COMPOSE


    3.3 Cardinalités importantes

                             Cardinalité Traduction en MLD
                             (1,N) (1,1)    FK dans la table du côté (1,1)
                             (1,N) (1,N)    Table d'association avec PK composite
                             (N,1) (1,N)    FK dans la table du côté (N,1)


    3.4 Checklist MCD
        ✓ Identier toutes les entités (noms)

        ✓ Distinguer les types des instances

        ✓ Repérer les relations N:M et leurs attributs

        ✓ Vérier les cardinalités

        ✓ Identier les acteurs (expert, correspondant, etc.)

        ✓ Ajouter tous les attributs descriptifs




                                                         14
~~~

## Page 16

~~~text
Révision Bases de Données                                             CY Tech ING1-GM


3.5 Checklist MLD
  ✓ Transformer les relations N:M en tables d'association

  ✓ Ajouter les FK pour les relations (N,1)

  ✓ Souligner toutes les PK

  ✓ Préxer toutes les FK avec #

  ✓ Vérier les REFERENCES

  ✓ Identier les attributs nullable (exemple : code_entrepot NULL)




                                               15
~~~

## Page 17

~~~text
     Révision Bases de Données                                                 CY Tech ING1-GM


     4        Normalisation : 3FN et BCNF (3-4 points)

     4.1 Dénitions essentielles
          Dépendance fonctionnelle (DF) : X → Y signie que Y est déterminé par X
          DF élémentaire : Y est atomique (un seul attribut)
          DF transitive : X → Y et Y → Z donc X → Z
          DF partielle : Dans une clé composite AB, si A → C (violation 2FN)
     4.2 Les 3 formes normales
         1. 1FN : Tous les attributs sont atomiques (pas de listes)
         2. 2FN : 1FN + Pas de dépendances partielles (par rapport à la clé)
         3. 3FN : 2FN + Pas de dépendances transitives

     4.3 BCNF (Forme Normale de Boyce-Codd)
         IMPORTANT
         BCNF : Pour toute DF X → Y , X doit être une clé candidate
     4.4 Méthode pour lister les DF
         1. Identier la ou les clés primaires candidates
         2. Pour chaque attribut non-clé, déterminer de quoi il dépend
         3. Chercher les dépendances transitives (X → Y → Z )
         4. Si clé composite, vérier les dépendances partielles
         5. Éliminer les DF redondantes

     4.5 Exemple : CINEMA
 1 CINEMA ( NumSalleCinema , adresseSalleCinema , nomSalleCinema ,
 2          NumFilm , titreFilm , NumCategorieFilm , intituleCategorieFilm ,
 3          dateD butProjectionFilm , dur eProjectionFilm )
 4
 5 Dependances fonctionnelles :
 6 - NumSalleCinema -> adresseSalleCinema , nomSalleCinema
 7 - NumFilm -> titreFilm
 8 - NumCategorieFilm -> intituleCategorieFilm
 9 - NumFilm -> NumCategorieFilm ( transitive !)
10 - ( NumSalleCinema , NumFilm ) -> dateDebutProjectionFilm , dureeProjectionFilm
11
12   Probleme : DF transitives ( NumFilm -> NumCategorieFilm -> intituleCategorieFilm )
13
14 Decomposition en 3 FN :
15 SALLE ( NumSalleCinema , adresseSalleCinema , nomSalleCinema )
16 FILM ( NumFilm , titreFilm , NumCategorieFilm )
17 CATEGORIE ( NumCategorieFilm , intituleCategorieFilm )
18 PROJECTION ( NumSalleCinema , NumFilm , dateDebutProjectionFilm , dureeProjectionFilm )




                                                            16
~~~

## Page 18

~~~text
     Révision Bases de Données                                                    CY Tech ING1-GM


     4.6 Exemple : Ville/Location
 1   Ville ( idVille , nomVille , departement , region )
 2   Location ( idLogement , nomClient , dateSignature , # idVille , nbPieces )
 3
 4 DF dans Ville :
 5 - idVille -> nomVille , departement , region
 6 - departement -> region   ( VIOLATION BCNF !)
 7
 8   Pourquoi violation ?
 9   departement determine region , mais departement n ' est pas une cle candidate .
10
11 Decomposition en BCNF :
12 Ville ( idVille , nomVille , departement )
13 Departement ( departement , region )
14 Location ( idLogement , nomClient , dateSignature , # idVille , nbPieces )




                                                   17
~~~

## Page 19

~~~text
Révision Bases de Données                                     CY Tech ING1-GM


5   Pièges Fréquents et Erreurs à Éviter

5.1 Erreurs SQL
    ATTENTION
     1. Oublier DISTINCT quand "sans doublons" est demandé
     2. Utiliser WHERE avec agrégation     utiliser HAVING
     3. Oublier GROUP BY avec COUNT/SUM + autres colonnes
     4. Mal gérer LEFT JOIN (vérier IS NULL si nécessaire)
     5. Division : oublier DISTINCT dans COUNT
     6. Utiliser = NULL au lieu de IS NULL

5.2 Erreurs Modélisation
    ATTENTION
     1. Oublier les attributs portés par les relations N:M
     2. Confondre type et instance
     3. Mauvaises cardinalités
     4. Oublier des FK dans le MLD
     5. Ne pas souligner les PK ou préxer les FK avec #

5.3 Erreurs Normalisation
    ATTENTION
     1. Oublier les dépendances transitives
     2. Ne pas identier toutes les clés candidates
     3. Confondre 3FN et BCNF
     4. Mauvaise décomposition (perte d'information)




                                                 18
~~~

## Page 20

~~~text
Révision Bases de Données                                                 CY Tech ING1-GM


6        Stratégie d'Examen

6.1 Répartition du temps (2h = 120 minutes)

                    Exercice                       Points Temps recommandé
                    Modélisation (MCD/MLD)          5-7       40-45 min
                    Normalisation                   3-4       20-25 min
                    Requêtes SQL                   10-12      50-60 min
                    Relecture                        -        10-15 min


6.2 Ordre de traitement recommandé
    1. Lire TOUT l'énoncé (2-3 minutes)
    2. Commencer par les requêtes SQL faciles
          SELECT simple, LIKE, COUNT, MAX
          Ces questions rapportent 4-5 points faciles
    3. Faire la modélisation (MCD puis MLD)
    4. Faire la normalisation
    5. Retour aux requêtes SQL diciles
          Jointures complexes, division relationnelle
    6. Relecture complète

6.3 Points à vérier en relecture
    ✓ MLD : Tous les # pour FK et soulignements pour PK

    ✓ SQL : Points-virgules, parenthèses fermées

    ✓ SQL : DISTINCT si "sans doublons"

    ✓ SQL : GROUP BY si agrégation + autres colonnes

    ✓ Normalisation : Toutes les DF listées et justication

    ✓ Pas de questions faciles oubliées




                                                   19
~~~

## Page 21

~~~text
Révision Bases de Données                                                     CY Tech ING1-GM


7      Récapitulatif : Les 20 Points Clés

     1. Relations N:M    Table d'association avec PK composite + attributs
     2. Distinction Type vs Instance dans 80% des modélisations
     3. Cardinalités : (1,N) = FK côté N, (N,M) = table intermédiaire
     4. MLD : # pour FK, souligné pour PK
     5. DF transitives = violation de 3FN
     6. LIKE '%texte%' pour contient, 'texte%' pour commence
     7. COUNT(*) compte les lignes, COUNT(colonne) les non-NULL
     8. GROUP BY obligatoire avec agrégation et autres colonnes
     9. HAVING pour ltrer après GROUP BY, WHERE avant
    10. LEFT JOIN pour inclure tous (même sans correspondance)
    11. NOT IN pour "qui n'ont jamais"
    12. Division relationnelle = double NOT EXISTS ou COUNT = COUNT total
    13. DISTINCT pour éviter les doublons
    14. ORDER BY ... LIMIT 1 pour "le plus/moins"
    15. Sous-requête avec agrégation pour comparaison à moyenne/max
    16. CREATE TABLE : dénir PK et FK avec REFERENCES
    17. UPDATE : toujours avec WHERE sauf mise à jour globale
    18. JOIN : toujours préciser la condition ON
    19. NULL : utiliser IS NULL / IS NOT NULL (jamais = NULL)
    20. Tester mentalement chaque requête




                                                   20
~~~

## Page 22

~~~text
    Révision Bases de Données                                                         CY Tech ING1-GM


    8    Exemples Complets d'Examens

    8.1 Exemple 1 : Mario Kart (2021)
1 Personnage ( id , nom , dateNaissance )
2 Circuit ( id , nom , nbTour )
3 R a l i s e r U n e C o u r s e (# idPerso , # idCircuit , dateCourse , d u r e )
4 Voiture ( id , nom , vitesse , poids , # idPerso )

                                          Listing 17: Schéma relationnel
        Question : Quels personnages ont réalisé TOUS les circuits ?
1  SELECT p . nom
2  FROM Personnage p
 3 WHERE NOT EXISTS (
 4     SELECT *
 5     FROM Circuit c
 6     WHERE NOT EXISTS (
 7          SELECT *
 8          FROM R a l i s e r U n e C o u r s e r
 9          WHERE r . idPerso = p . id AND r . idCircuit = c . id
10     )
11 ) ;

                                         Listing 18: Solution - Méthode 1

1 SELECT p . nom
2 FROM Personnage p
3 JOIN R a l i s e r U n e C o u r s e r ON p . id = r . idPerso
4 GROUP BY p . id , p . nom
5 HAVING COUNT ( DISTINCT r . idCircuit ) = ( SELECT COUNT (*) FROM Circuit ) ;

                                         Listing 19: Solution - Méthode 2


    8.2 Exemple 2 : Commandes (2022-2023)
1 Commande ( no_commande , montant_achat , date , # client_id , # vendeur_id )
2 Client ( client_id , nom , ville , note )
3 Vendeur ( vendeur_id , nom , ville , commission )

                                          Listing 20: Schéma relationnel
        Question : Clients dont la somme des achats est supérieure à la moyenne
1  SELECT c . nom
2  FROM Client c
 3 JOIN Commande cmd ON c . client_id = cmd . client_id
 4 GROUP BY c . client_id , c . nom
 5 HAVING SUM ( cmd . montant_achat ) > (
 6     SELECT AVG ( total_achats )
 7     FROM (
 8          SELECT SUM ( montant_achat ) AS total_achats
 9          FROM Commande
10          GROUP BY client_id
11     ) AS moyennes
12 ) ;

                                                Listing 21: Solution




                                                          21
~~~

## Page 23

~~~text
Révision Bases de Données                                                          CY Tech ING1-GM


9    Annexe : Aide-mémoire SQL

9.1 Fonctions d'agrégation

                     Fonction                      Description
                     COUNT(*)                      Compte toutes les lignes
                     COUNT(colonne)                Compte les valeurs non-NULL
                     COUNT(DISTINCT col)           Compte les valeurs distinctes
                     SUM(colonne)                  Somme des valeurs
                     AVG(colonne)                  Moyenne des valeurs
                     MAX(colonne)                  Valeur maximale
                     MIN(colonne)                  Valeur minimale


9.2 Opérateurs de comparaison

                        Opérateur                   Description
                        =                           Égal
                        != ou <>                    Diérent
                        >                           Supérieur
                        <                           Inférieur
                        >=                          Supérieur ou égal
                        <=                          Inférieur ou égal
                        BETWEEN a AND b             Entre a et b (inclus)
                        IN (val1, val2, ...)        Dans la liste
                        NOT IN (val1, val2, ...)    Pas dans la liste
                        IS NULL                     Est NULL
                        IS NOT NULL                 N'est pas NULL
                        LIKE                        Correspondance de motif


9.3 Opérateurs logiques
     AND : Les deux conditions doivent être vraies
     OR : Au moins une condition doit être vraie
     NOT : Inverse la condition
9.4 Fonctions de chaînes

                      Fonction                          Description
                      LENGTH(str)                       Longueur de la chaîne
                      UPPER(str)                        Convertir en majuscules
                      LOWER(str)                        Convertir en minuscules
                      CONCAT(str1, str2, ...)           Concaténer des chaînes
                      SUBSTRING(str, pos, len)          Extraire sous-chaîne
                      TRIM(str)                         Enlever espaces début/n



                            Bon courage pour tes révisions !



                                                   22
~~~
