# CM01-Les-structures_2023-2024_Informatique2_P1S2_EAnsermin-RGrignon.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1mOYA0M5t5LqmwicfEnGeWWlEd7vEE2fk) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 1.

## Page 1

![Fac-similé de la page 1](../facsimiles/d1502daec96db135af7552d9.jpg)

~~~text
INFORMATIQUE 1
IX. LES STRUCTURES ET
COMPAGNIE
~~~



## Page 2

~~~text
Les différents type en programmation
• Nous avons vu jusqu’à maintenant les types “de base” (int, float, char, double).

• Les différents types sont réparties en deux categories :
     • Les types primitifs : la variable contient directement une valeur (c’est le cas de int, flaot etc…)
     • Les types references: la variable fait reference à une ou plusieurs valeurs stockés en mémoire.
~~~

## Page 3

~~~text
Les différents type en programmation
• Nous avons vu jusqu’à maintenant les types “de base” (int, float, char, double).

• Les différents types sont réparties en deux categories :
     • Les types primitifs : la variable contient directement une valeur (c’est le cas de int, flaot etc…)
     • Les types references: la variable fait reference à une ou plusieurs valeurs stockés en mémoire.
           •     Ex : les tableaux !




                                                             tab[0]

               tab<-{10, 23, 505 ,8}                         tab[1]         tab fait reference à tout
                                                                           cet espace mémoire et à
                                                             tab[2]
                                                                           toutes ces valeurs
                                                             tab[3]
~~~

## Page 4

~~~text
Le monde n’est pas fait d’entiers et de réels….




                                   http://www.spencerauthor.com/pblproblems/
~~~

## Page 5

~~~text
Le monde n’est pas fait d’entiers et de réels….
● En géométrie, nous manipulons des Coordonnées, des rectangles, des droites ... ;

● Un magasin gère des produits, des clients, des factures, des fournisseurs ;

● Dans une médiathèque, il y a des documents, des usagers, qui louent, réservent ces documents ...

• Exemple : On souhaite faire un programme qui va gérer des étudiants:
➢       Chaque étudiant a : un nom, un prénom, un numéro d’étudiant, un groupe, une ou plusieurs
    notes…
~~~

## Page 6

~~~text
Exemple : gestion des étudiants

Programme gestion_etudiants
     VARIABLE
     nom_etudiant1, nom_etudiant2 : chaîne de caractère
     pnom_etudiant1, pnom_etudiant2 : chaîne de caractère
     num_etudiant1, num_etudiant2 : entier
     gp_etudiants1, gp_etudiant2 : entier
     note_etudiant1, note_etudiant2 : reel

     DEBUT
     …
~~~

## Page 7

~~~text
Une première définition des structure
Un type structuré représente une donnée complexe, composée de plusieurs valeurs pouvant être de
types différents :

     ● Un nombre complexe possède une partie réelle et une partie imaginaire ;

     ● Un Coordonnée est composé de coordonnées réelles (x, y) dans un espace de dimension 2, (x, y, z) pour
     un Coordonnée en 3D, etc. ;

     ● Une date est définie par un jour, un mois, une année, une heure, des minutes, secondes, millisecondes ;

     ● Une adresse est définie par un numéro et nom de rue, un code postal et une ville, etc.
~~~

## Page 8

~~~text
Une définition étendue des structures
●   Un type structuré définit un type de donnée (au même titre qu’entier, chaîne ou réel) ;


●   À la différence des variables de type primitif, une variable d’un tel type structuré contient
    plusieurs valeurs stockée dans des champs (ou attributs) ;


●   Les variables de type structuré sont appelées parfois enregistrements.


●   C’est le programmeur qui definit la structure, lui donne un nom et défini ses champs.
~~~

## Page 9

~~~text
Exemple simple
●   Un Coordonnée dans un espace 2D est définie par son abscisse est son ordonnée.
●   On va construire une structure appellee Coordonnée, qui sera defines par deux champs:
    l’abcsisse et l’ordonnée.




                         STRUCTURE Coordonnée
                              abscisse : réel
                              ordonnée : réel
                         FIN STRUCTURE
~~~

## Page 10

~~~text
Exemple simple
●   Coordonnée est maintenant un nouveau type!


    STRUCTURE Coordonnée // définition de la structure
         abscisse : réel
         ordonnée : réel
    FIN STRUCTURE

    VARIABLE // déclaration des variables
         a: entier
         x : Coordonnée // x et y sont des coordonnées
         y : Coordonnée
~~~

## Page 11

~~~text
Exemple simple
●   Coordonnée est maintenant un nouveau type!


    STRUCTURE Coordonnée // définition de la structure
         abscisse : réel
         ordonnée : réel
    FIN STRUCTURE

    VARIABLE // déclaration des variables
         a: entier
         x : Coordonnée // x et y sont des Coordonnée
         y : Coordonnée

●   Les Coordonnées sont des variables possédant deux attributs de type reel: abscisse et
    ordonnée.
~~~

## Page 12

~~~text
Exemple simple
  STRUCTURE Coordonnée // définition de la structure
       abscisse : réel
       ordonnée : réel
  FIN STRUCTURE

  VARIABLE // déclaration des variables
        a: entier
        x : Coordonnée // x et y sont des Coordonnée
        y : Coordonnée
  DEBUT
        x.abscisse <- 3 // acceder au champs
        x.ordonnée <- 5,5
        y.abscisse <- x.abscisse +2
        …
~~~

## Page 13

~~~text
Syntaxe
 ●   Définition du type structuré
STRUCTURE nomType
       nomChamp1 : TYPE1,
       nomChamp2      : TYPE2,
               ....,
       nomChampn      : TYPEn
FIN STRUCTURE


 ●   Déclaration de variable
elt1, elt2 : nomType

 ●   Manipulation :
Accéder au champ nomChampi de la variable elt1 se fait selon : elt1.nomChampi
~~~

## Page 14

~~~text
Manipulation des structure
• Chaque champs d’un occurrence de la structure peut être considérée comme une
  variable indépendante.

• Les opérations se font champs par champs ! (comme les cases pour les tableaux)

   • Exemple : x, y et z sont des Coordonnées


                z<- x+y

                z. abscisse <- x. abscisse + y. abscisse
                z.ordonnee<-x.ordonnee + y.ordonnee
~~~

## Page 15

~~~text
Manipulation des structure
• Chaque champs d’un occurrence de la structure peut être considérée comme une
  variable indépendante.

• Les opérations se font champs par champs ! (comme les cases pour les tableaux)

• On a par contre le droit d’écrire :

                               z<- x
           Les valeurs des champs de z seront égales à ceux de x
~~~

## Page 16

~~~text
Constructeur
 ●   Constructeur de variable de type structuré (permet de valider les préconditions sur le type
     et de retourner la variable ou bien de planter le programme)
FONCTION creerType(val1 : TYPE1, val2 : TYPE2, ...) : nomType
VAR res : nomType
DÉBUT
    SI (condition(val1, val2, ...)) ALORS
       écrire (“Un message d’erreur explicite”)
       erreur() // met fin au programme en erreur
    FIN SI
    res.nomChamp1 <- val1
       res.nomChamp2 <- val2
              ....
       retourner res
FIN
~~~

## Page 17

~~~text
Exemple simple
STRUCTURE Coordonnée
                                         VARIABLE
       abscisse : réel
       ordonnée : réel                           x : Coordonnée
FIN STRUCTURE                                    a : réel
                                                 b : réel
FONCTION creerCoordonnée(x, y: reel) :   DEBUT
Coordonnée
VAR p : Coordonnée
                                              ECRIRE(“donner les
DÉBUT                                    coordonnées du Coordonnée”)
      p.abscisse <- x                         LIRE(a)
     p.ordonnee<- y                           LIRE(b)
     RETOURNER p                              x<- creerCoordonnée(a,b)
FIN
                                         FIN
~~~

## Page 18

~~~text
Remarques
• Le nom des structures commence toujours par une majuscule.

• Il ne faut pas confondre la structure (le type créé) et les variables de cette
  structure.

• Les différents champs d’une variable de type structure sont à la suite dans la
  mémoire (comme les cases d’un tableau).




                                                     x.abcisse
          x : Coordonnée
                                                      x.ordonnée
~~~

## Page 19

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a :


    STRUCTURE Etudiant




    FIN STRUCTURE
~~~

## Page 20

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom


    STRUCTURE Etudiant
              nom : chaîne de caractère




    FIN STRUCTURE
~~~

## Page 21

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom


    STRUCTURE Etudiant
              nom : chaîne de caractère
              prenom : chaîne de catactère




    FIN STRUCTURE
~~~

## Page 22

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant


    STRUCTURE Etudiant
              nom : chaîne de caractère
              prenom : chaîne de catactère
              num : entier



    FIN STRUCTURE
~~~

## Page 23

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe


    STRUCTURE Etudiant
              nom : chaîne de caractère
              prenom : chaîne de catactère
              num : entier
              groupe : entier


    FIN STRUCTURE
~~~

## Page 24

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, des notes


    STRUCTURE Etudiant
              nom : chaîne de caractère
              prenom : chaîne de catactère
              num : entier
              groupe : entier
              note1 : reel


    FIN STRUCTURE
~~~

## Page 25

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes


    STRUCTURE Etudiant
              nom : chaîne de caractère
           prenom : chaîne de catactère
           num : entier
           groupe : entier
           note1 : reel
           note2: reel
           …
           noteN : reel
    FIN STRUCTURE
~~~

## Page 26

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes


    STRUCTURE Etudiant
              nom : chaîne de caractère
              prenom : chaîne de catactère
              num : entier
              groupe : entier
              note[N] : tableau de réél

    FIN STRUCTURE
~~~

## Page 27

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes, une adresse


    STRUCTURE Etudiant
              nom : chaîne de caractère
           prenom : chaîne de catactère
           num : entier
           groupe : entier
            note[N] : tableau de réél
           adresse : ???
    FIN STRUCTURE
~~~

## Page 28

~~~text
Un exemple plus compliqué…
  • Une adresse est compose de plusieures information: le nom de la rue, le numéro de la maison, la ville,
     le code postal…

  • Une structure semble donc approprié pour representer une adresse

    STRUCTURE Adresse
              num : entier
           rue : chaîne de catactère
           ville : chaîne de caractère
           code : entier
    FIN STRUCTURE
~~~

## Page 29

~~~text
Un exemple plus compliqué…
 • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes, une adresse
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactère
           ville : chaîne de caractère
           code : entier
    FIN STRUCTURE

    STRUCTURE Etudiant
             nom : chaîne de caractère
           prenom : chaîne de catactère
           num : entier
           groupe : entier
            note[N] : tableau de réél
           add : Adresse
    FIN STRUCTURE
~~~

## Page 30

~~~text
Un exemple plus compliqué…
 • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes, une adresse
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactère                      Pour indiquer le code postal d’un Etudiant:
           ville : chaîne de caractère
           code : entier                                  VARIABLE
    FIN STRUCTURE                                                   etu1 : Etudiant
                                                          DEBUT
    STRUCTURE Etudiant
                                                                    etu1.add.code <- 95000
             nom : chaîne de caractère
           prenom : chaîne de catactère
           num : entier                                  Se lit : “ le code de l’adresse de l’étudiant etu1”
           groupe : entier
            note[N] : tableau de réél
           add : Adresse
    FIN STRUCTURE
~~~

## Page 31

~~~text
Un exemple plus compliqué…
 • Et pour gérer la promotion de 330 élèves?
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactère
           ville : chaîne de caractère
           code : entier
    FIN STRUCTURE

    STRUCTURE Etudiant
             nom : chaîne de caractère
           prenom : chaîne de catactère
           num : entier
           groupe : entier
            note[N] : tableau de réél
           add : Adresse
    FIN STRUCTURE
~~~

## Page 32

~~~text
Un exemple plus compliqué…
 • Et pour gérer la promotion de 330 élèves?
    Constante NB_ETU <- 330
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactère           VARIABLE
           ville : chaîne de caractère
           code : entier                               prom[NB_ETU] : tableau d’Etudiant
    FIN STRUCTURE                              DEBUT
    STRUCTURE Etudiant
             nom : chaîne de caractère
           prenom : chaîne de catactère
           num : entier
           groupe : entier
            note[N] : tableau de réél
           add : Adresse
    FIN STRUCTURE
~~~

## Page 33

~~~text
Un exemple plus compliqué…
 • Et pour gérer la promotion de 330 élèves?
    Constante NB_ETU <- 330
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactère           VARIABLE
           ville : chaîne de caractère
           code : entier                               prom[NB_ETU] : tableau d’Etudiant
    FIN STRUCTURE                              DEBUT
    STRUCTURE Etudiant                                 prom[0].nom<-“Dupont”
             nom : chaîne de caractère                 prom[5].groupe <- 2
           prenom : chaîne de catactère                prom[1].add.num <- 56
           num : entier
           groupe : entier                             prom[1].num<- 225784
            note[N] : tableau de réél                  …
           add : Adresse
    FIN STRUCTURE
~~~

## Page 34

~~~text
Les structure en C : syntaxe
 ●   Déclaration d’une structure

     struct NomStructure {
         type champ1 ;
         type champ2 ;
         …
     };
 ●   Utilisation d’une structure
     struct NomStructure nomVariable;

 ●   Manipulation :

     nomVariable.champ
~~~

## Page 35

~~~text
Les structure en C : syntaxe
  ●   Exemple

      struct Coordonnée{
            float abscisse;
            float ordonnee;
            };
      int main(){
            struct Coordonnée x;
            scanf("%f",&x.abcisse);
            scanf("%f",&x.ordonnee);
            printf( " les coordonnées du Coordonnée sont (%f, %f)
 \n", x.abcisse, x.ordonnee);
            return 0; }
      }
~~~

## Page 36

~~~text
Les structure en C : syntaxe
  ●   Exemple

 //Attention à l’ordre !!
        struct Adresse{
               int num;
               char rue[200]; // Tableau de caractère
               char ville[200];
               int code;
        };
 struct Etudiant{
               char nom[200];
               char prenom[200];
               int groupe;
               int num;
               struct Adresse add; // Adresse doit etre décrite avant
        };
~~~

## Page 37

~~~text
Types équivalents
 ●   Permet de renommer un type existant
 ●   Permet de simplifier une écriture, de gagner en expressivité
 ●   Exemple :
     typedef type nouveau_nom ;
     typedef type nouveau_nom1, nouveau_nom2, ... ;
~~~

## Page 38

~~~text
Exemple

// Renommage
typedef float reel ;
typedef int entier ;

// Utilisation
entier a ;
reel x ;
~~~

## Page 39

~~~text
Types équivalents
    ●    Déclaration d’une structure + renommage en type :

         // Dorénavant, nous l’écrirons comme ceci
         typedef struct {
             char nom[200] ;
             char prenom[200] ;
         } Auteur;

         // Utilisation
         Auteur tolkien, rowling ;


●       Plus besoin d’utiliser struct à chaque déclaration !
~~~

## Page 40

~~~text
Énumération
 ●   Une énumération définit un nouveau type permettant à une variable de prendre un
     nombre fini de valeurs ;
 ●   Exemples :
      ○   mois : JANVIER, FÉVRIER, MARS, ...
      ○   jours : LUNDI, MARDI, MERCREDI, ...
      ○   couleurCarte : PIQUE, COEUR, CARREAU, TREFLE
      ○   feuTtricolore : ROUGE, ORANGE, VERT
      ○   booléen : VRAI, FAUX
      ○   ...
~~~

## Page 41

~~~text
Syntaxe
 ●   Déclaration d’une énumération

     enum nomEnumeration { VAL1, VAL2, …, VALN };
     ou plutôt :
     typedef enum {
          VAL1, VAL2, …, VALN
     } nomEnumeration;


 ●   Utilisation d’une énumération

     enum nomEnumeration nomVariable;
     ou plutôt :
     nomEnumeration nomVariable;
~~~

## Page 42

~~~text
Exemple

typedef enum { PIQUE, COEUR, CARREAU, TREFLE } Couleur;

typedef struct {
    short valeur ; /∗ short ??    !< 1->10, 11: valet, 12: dame, 13: roi ∗/
    Couleur c_couleur ;
} carte;

typedef carte deck[52]   // deck defini donc un lot de 52 cartes

/∗ Utilisation ∗/
deck jeu ;
jeu[0].valeur = 1;
jeu[0].c_couleur = TREFLE;
~~~

## Page 43

~~~text
Énumération : Sous le capot
  ●   Une valeur est affectée à chaque valeur de l’énumération ;
  ●   Première valeur : 0 ;
  ●   Itération pour les autres (+1 par défaut) ;
  ●   Il est possible de :
       ○   démarrer avec une autre valeur,
       ○   donner une valeur différente à un élément de l’énumération:

                 typedef enum {
                     FAIBLE = 10, MOYEN = 50, FORT = 100
                 }Volume;
~~~

## Page 44

~~~text
Pour completer
 ●   Enumeration des types de rue pour completer la structure Adresse:




                 typedef enum {
                     RUE, BOULEVARD, IMPASSE, CHEMIN, AVENUE
                 } type_rue;
~~~

## Page 45

~~~text
Pour completer
   typedef enum {
       RUE, BOULEVARD, IMPASSE, CHEMIN, AVENUE
   } Type_rue;

   typedef struct{
          int num;
          Type_rue style; // Type de rue de l’adresse
          char rue[200]; // Nom de la rue
          char ville[200];
          int code;
   } Adresse;

   typedef struct {
          char nom[200];
          char prenom[200];
          int groupe;
          int num;
          Adresse add;
   } Etudiant;
~~~

## Page 46

~~~text
Structure générale d’un fichier .c
                  #Instructions du préprocesseur
                      (inclusion bibliothèque)
                       + définition constante
                       Défintions structures
                             + typedef


                       Code de la fonction 1


                       Code de la fonction 2
                              ….

                     Code de la fonction main
~~~

## Page 47

~~~text
Conclusion

• Il est possible de creer/personnaliser ses propres types.
• Une structure est composée de sous-variable appellees champs ou attribus.
• Pour acceder au champs d’une variable de la structure:
                  • nomVariable.champ
• L’énumeration est un type qui permet de prendre un valeur définie parmis
   d’autres.


• On peut faire de l’imbrication de structure/ enumeration pour creer des types
   complexes.
~~~
