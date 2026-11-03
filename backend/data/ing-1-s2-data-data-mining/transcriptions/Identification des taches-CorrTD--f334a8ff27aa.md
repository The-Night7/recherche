# Identification des taches-CorrTD.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1VHneZwPqTUG3MlFIqCUbEwCeQxwFNBr4) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Ingénieurs 1ère année MI                                                                                   Datamining 1
                                                                                         T.P.1. Identification de taches




                                       TP1 : Identification de taches
                                                         Durée : 1h

L’objectif de ce TP est d’identifier une ou plusieurs taches de datamining liées à
une situation concrète.


Credit Scoring
Dans une banque, un service s’occupe d’accorder (ou pas) des prêts à des particuliers. Pour tous les
prêts déjà accordés, elle dispose des informations suivantes : salaire, métier (fonction et secteur
d’activité), nombre d’enfants, situation matrimoniale, …. Elle désire mettre en place un outil afin de
prévoir à l’avance si un futur emprunteur posera ou pas des problèmes si on lui accorde un prêt.
     •    Identifier la tâche de Data Mining permettant de résoudre le problème.
          Corrigé : Le banquier a réparti ses clients dans des classes qui traduisent la qualité du client en
          termes de remboursement. C’est le banquier qui définit ces classes à priori. Par ailleurs, on
          connait pour chaque client les informations suivantes : salaire, métier (fonction et secteur
          d’activité), nombre d’enfants, situation matrimoniale, ….. Il désire construire un modèle qui
          permet sur les crédits déjà accordés d’avoir une règle de décision pour affecter un potentiel
          client dans une des classes en connaissant les informations citées ci-dessus. Il s’agit donc
          d’une tâche de classification.
     •    Quelles sont les informations nécessaires pour alimenter l’outil ?
          Corrigé : Il faut disposer de la liste des crédits déjà accordés. Pour chaque crédit, on doit
          connaître l’ensemble des informations données par le client (attributs non cibles) et la classe
          dans laquelle le banquier l’a affectée en fonction de la qualité de ces remboursements.


Prévision du chiffre d’affaire
Le service commercial d’une entreprise désire prévoir le chiffre d’affaire d’un produit en fonction de
sa politique commerciale. Elle émet l’hypothèse que ce chiffre dépend directement du prix de vente,
du nombre d’enseignes dans lesquelles il est vendu, du budget de publicité.
      • Identifier la tâche de Data Mining permettant de résoudre le problème.
          Corrigé : Il s’agit d’une tâche de prédiction. Il faut prédire dans le futur le chiffre d’affaire en
          fonction de la politique de vente : prix de vente, nombre d’enseignes, budget de publicité.
      • Quelles sont les informations nécessaires pour alimenter l’outil ?
          Corrigé : Il faut disposer sur une période donnée déjà écoulée, un corpus de données dont
          chaque ligne est identifiée par une date donnée. Les autres éléments de la ligne sont d’une
          part le CA réalisé (attribut cible) pour cette date et le triplet prix unitaire, nombre d’enseignes
          et budget de publicité pour cette même date.



                                                                                                                      1
~~~

## Page 2

~~~text
Ingénieurs 1ère année MI                                                                             Datamining 1
                                                                                   T.P.1. Identification de taches




Evolution du marché de l’automobile
Dans ce secteur comme dans beaucoup d’autres, les professionnels segmentent le marché en fonction
des besoins des clients. En fonction des différents segments identifiés, le constructeur définit sa
gamme de produits. Dans notre cas, cela pourrait être : utilitaires, familiales, sport, luxe, ….
Nous supposerons que nous sommes dans une période où les habitudes des consommateurs sont en
train d’évoluer de façon plus ou moins significative. Pour ne pas passer à côté de ce changement, il
s’agit donc d’anticiper les nouveaux segments. Le service marketing décide donc lancer une enquête
auprès de ces clients actuels et des clients potentiels. Le questionnaire contient deux séries de
questions : une première série sur les besoins futurs dans le cas d’un achat d’une nouvelle voiture et
une deuxième série sur la description du client (situation matrimoniale, métier, nombre d’enfants,
salaire, sexe, …).
      1. Identifier la tâche de Data Mining permettant de redéfinir de nouvelles gammes de voiture en
         fonction des attentes des clients.
         Corrigé : Créer de nouveaux segments consiste à identifier parmi les acheteurs potentiels, des
         groupes homogènes en termes de comportement d’achat. Il s’agit donc d’une tâche de
         clusterisation.
         Pour cette tâche quelles sont les informations nécessaires ?
         Corrigé : Chaque ligne du corpus de données correspond aux réponses d’un des clients actuels
         ou potentiels. Dans ce corpus, on a retenu que la première série de questions portant sur les
         besoins futurs d’achat.
      2. Identifier la tâche de Data Mining permettant d’identifier pour chaque gamme, un profil type
         des clients. Pour une analyse plus fine, le service marketing désire avoir les différences
         significatives entre les différents profils.
         Corrigé : Les résultats de la clusterisation précédente permettent de définir un nouvel attribut
         nominal qui permet d’identifier pour chaque interviewé son segment.
         Pour cette tâche quelles sont les informations nécessaires ?
         Corrigé : Chaque ligne du corpus de données correspond aux réponses d’un des clients actuels
         ou potentiels. Dans ce corpus, on a retenu que la deuxième série de questions portant sur la
         description du client. On a ajouté de plus la colonne permettant d’identifier le segment.


Reporting et Datamining
Nous avons les deux questionnements suivants :
   • Le responsable des ventes d’une entreprise demande au service des systèmes d’information
       des graphiques donnant le chiffre d’affaire par produit, par région et par mois.
   • Le directeur du marketing demande au service des systèmes d’information de mesurer le lien
       entre les prix des produits et le budget de publicité d’une part et le chiffre d’affaire réalisé.
Lequel des deux questionnements est de l’ordre du Data Mining ?
Corrigé : Dans le premier cas il s’agit de croiser et agréger des tables de bases de données pour
présenter des résultats. On ne cherche pas à extraire de l’information des données mais juste à les
représenter. Il s’agit d’une tache de reporting.

                                                                                                                2
~~~

## Page 3

~~~text
Ingénieurs 1ère année MI                                                                     Datamining 1
                                                                           T.P.1. Identification de taches



Dans le deuxième cas, il faut extraire de l’information des données en construisant un modèle de
prévision du chiffre d’affaire en fonction des autres variables.




                                                                                                        3
~~~
