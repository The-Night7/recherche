# 05_Structures.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1a39YZhZJlWcnWLqrhJS23UkpW2dtteK4) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                               v1.00




PROGRAMMATION
PROCEDURALE
5. STRUCTURES
_ _ E N U M E R AT I O N S
__TYPES




                                                                                   1
                             Eva ANSERMIN & Romuald GRIGNON
                                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 2

~~~text
Les différents types en programmation
• Nous avons vu jusqu’à maintenant les types “de base” (int, float, char, double).

• Les différents types sont répartis en deux categories :
     • Les types primitifs : la variable contient directement une valeur (c’est le cas de int, float etc…)
     • Les types références: la variable fait référence à une ou plusieurs valeurs stockées en mémoire.




                                                                                                                            2
                                                                                                       E. ANSERMIN | R. GRIGNON
~~~

## Page 3

~~~text
Les différents types en programmation
• Nous avons vu jusqu’à maintenant les types “de base” (int, float, char, double).

• Les différents types sont répartis en deux categories :
     • Les types primitifs : la variable contient directement une valeur (c’est le cas de int, float etc…)
     • Les types références: la variable fait référence à une ou plusieurs valeurs stockées en mémoire.
           •     Ex : les tableaux !




                                                            tab[0]

               tab  {10, 23, 505 ,8}                       tab[1]
                                                                          tab fait référence à tout
                                                                          cet espace mémoire et à
                                                            tab[2]        toutes ces valeurs
                                                            tab[3]                                                          3
                                                                                                       E. ANSERMIN | R. GRIGNON
~~~

## Page 4

~~~text
Le monde n’est pas fait d’entiers et de réels….




                                   http://www.spencerauthor.com/pblproblems/
                                                                                                    4
                                                                               E. ANSERMIN | R. GRIGNON
~~~

## Page 5

~~~text
Le monde n’est pas fait d’entiers et de réels….
●   En géométrie, nous manipulons des coordonnées, des rectangles, des droites ... ;

●   Un magasin gère des produits, des clients, des factures, des fournisseurs ;

●   Dans une médiathèque, il y a des documents, des usagers, qui louent, réservent ces documents ...

●   Exemple : On souhaite faire un programme qui va gérer des étudiants. Chaque étudiant possède :
      ○   un nom
      ○   un prénom
      ○   un numéro d’étudiant
      ○   un groupe
      ○   une ou plusieurs notes…



                                                                                                               5
                                                                                          E. ANSERMIN | R. GRIGNON
~~~

## Page 6

~~~text
Exemple : gestion des étudiants

Programme gestion_etudiants
     VARIABLE
     nom_etudiant1, nom_etudiant2 : chaîne de caractères
     pnom_etudiant1, pnom_etudiant2 : chaîne de caractères
     num_etudiant1, num_etudiant2 : entier
     gp_etudiants1, gp_etudiant2 : entier
     note_etudiant1, note_etudiant2 : réel

     DEBUT
     …

                                                                                  6
                                                             E. ANSERMIN | R. GRIGNON
~~~

## Page 7

~~~text
Une première définition des structure
Un type structuré représente une donnée complexe, composée de plusieurs valeurs pouvant être de
types différents :

     ● Un nombre Complexe possède une partie réelle et une partie imaginaire ;

     ● Une Coordonnée est composée de coordonnées réelles (x, y) dans un espace de dimension 2, de
     coordonnées réelles (x, y, z) pour une Coordonnée en 3D, etc. ;

     ● Une Date est définie par un jour, un mois, une année, une heure, des minutes, secondes, millisecondes ;

     ● Une Adresse est définie par un numéro et un nom de rue, un code postal et une ville, etc.




                                                                                                                         7
                                                                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 8

~~~text
Une définition étendue des structures
●   Un type structuré définit un type de donnée (au même titre qu’entier, chaîne ou réel) ;


●   À la différence des variables de types primitifs, une variable d’un tel type structuré contient
    plusieurs valeurs stockées dans des champs (ou membres ou attributs) ;


●   Les variables de type structuré sont appelées parfois enregistrements.


●   C’est le programmeur qui definit la structure, lui donne un nom et définit ses champs.




                                                                                                                    8
                                                                                               E. ANSERMIN | R. GRIGNON
~~~

## Page 9

~~~text
Exemple simple
●   Une Coordonnée dans un espace 2D est définie par son abscisse et son ordonnée.
●   On va construire une structure appellee Coordonnée, qui sera definit par deux champs:
    l’abscisse et l’ordonnée.




                         STRUCTURE Coordonnée
                              abscisse : réel
                              ordonnée : réel
                         FIN STRUCTURE

                                                                                                             9
                                                                                        E. ANSERMIN | R. GRIGNON
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
         x : Coordonnée // x et y sont des ‘Coordonnée’
         y : Coordonnée


                                                                             10
                                                          E. ANSERMIN | R. GRIGNON
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
         x : Coordonnée // x et y sont des ‘Coordonnée’
         y : Coordonnée

●   Les Coordonnées sont des variables possédant deux attributs de types réels: abscisse et
                                                                                                            11
    ordonnée.
                                                                                         E. ANSERMIN | R. GRIGNON
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
        x : Coordonnée // x et y sont des ‘Coordonnée’
        y : Coordonnée
  DEBUT
        x.abscisse <- 3 // acceder au champs
        x.ordonnée <- 5,5
        y.abscisse <- x.abscisse +2
        …                                                                   12
                                                         E. ANSERMIN | R. GRIGNON
~~~

## Page 13

~~~text
Syntaxe
 ●   Définition du type structuré
STRUCTURE nomType
       nomChamp1 : TYPE1,
       nomChamp2 : TYPE2,
               ....,
       nomChampn : TYPEn
FIN STRUCTURE


 ●   Déclaration de variable
elt1, elt2 : nomType

 ●   Manipulation :
Accéder au champ nomChampi de la variable elt1 se fait selon : elt1.nomChampi


                                                                                                   13
                                                                                E. ANSERMIN | R. GRIGNON
~~~

## Page 14

~~~text
Manipulation des structure
• Chaque champ d’une occurrence de la structure peut être considérée comme
  une variable indépendante.

• Les opérations se font champ par champ ! (comme les cases pour les tableaux)

   • Exemple : x, y et z sont des Coordonnée


                z  x+y

                z. abscisse  x. abscisse + y. abscisse
                z.ordonnee  x.ordonnee + y.ordonnee


                                                                                            14
                                                                         E. ANSERMIN | R. GRIGNON
~~~

## Page 15

~~~text
Manipulation des structure
• Chaque champ d’une occurrence de la structure peut être considérée comme
  une variable indépendante.

• Les opérations se font champ par champ ! (comme les cases pour les tableaux)

• On a par contre le droit d’écrire :

                               zx
           Les valeurs des champs de z seront égales à ceux de x




                                                                                            15
                                                                         E. ANSERMIN | R. GRIGNON
~~~

## Page 16

~~~text
Constructeur
 ●   Constructeur de variable de type structuré (permet de valider les préconditions sur le type
     et de retourner la variable ou bien de terminer le programme)
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

                                                                                                          16
                                                                                       E. ANSERMIN | R. GRIGNON
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

                                                                                     17
                                                                  E. ANSERMIN | R. GRIGNON
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

                                                                                                      18
                                                                                   E. ANSERMIN | R. GRIGNON
~~~

## Page 19

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a :


    STRUCTURE Etudiant




    FIN STRUCTURE

                                                             19
                                          E. ANSERMIN | R. GRIGNON
~~~

## Page 20

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom


    STRUCTURE Etudiant
              nom : chaîne de caractères




    FIN STRUCTURE

                                                              20
                                           E. ANSERMIN | R. GRIGNON
~~~

## Page 21

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom


    STRUCTURE Etudiant
              nom : chaîne de caractères
              prenom : chaîne de catactères




    FIN STRUCTURE
                                                                 21
                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 22

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant


    STRUCTURE Etudiant
              nom : chaîne de caractères
              prenom : chaîne de catactères
              num : entier



    FIN STRUCTURE
                                                                                   22
                                                                E. ANSERMIN | R. GRIGNON
~~~

## Page 23

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe


    STRUCTURE Etudiant
              nom : chaîne de caractères
              prenom : chaîne de catactères
              num : entier
              groupe : entier


    FIN STRUCTURE
                                                                                              23
                                                                           E. ANSERMIN | R. GRIGNON
~~~

## Page 24

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, des notes


    STRUCTURE Etudiant
              nom : chaîne de caractères
              prenom : chaîne de catactères
              num : entier
              groupe : entier
              note1 : reel


    FIN STRUCTURE
                                                                                                         24
                                                                                      E. ANSERMIN | R. GRIGNON
~~~

## Page 25

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes


    STRUCTURE Etudiant
              nom : chaîne de caractères
           prenom : chaîne de catactères
           num : entier
           groupe : entier
           note1 : reel
           note2: reel
           …
           noteN : reel
                                                                                                       25
    FIN STRUCTURE
                                                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 26

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes


    STRUCTURE Etudiant
              nom : chaîne de caractères
              prenom : chaîne de catactères
              num : entier
              groupe : entier
              note[N] : tableau de rééls

    FIN STRUCTURE
                                                                                                       26
                                                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 27

~~~text
Un exemple plus compliqué…
  • On va écrire la structure Etudiant.
  • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes, une adresse


    STRUCTURE Etudiant
              nom : chaîne de caractères
           prenom : chaîne de catactères
           num : entier
           groupe : entier
            note[N] : tableau de réél
           adresse : ???
    FIN STRUCTURE
                                                                                                               27
                                                                                            E. ANSERMIN | R. GRIGNON
~~~

## Page 28

~~~text
Un exemple plus compliqué…
  • Une adresse est composée de plusieurs informations : le nom de la rue, le numéro de la maison, la
     ville, le code postal…

  • Une structure semble donc appropriée pour représenter une adresse

    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactères
           ville : chaîne de caractères
           code : entier
    FIN STRUCTURE



                                                                                                                   28
                                                                                                E. ANSERMIN | R. GRIGNON
~~~

## Page 29

~~~text
Un exemple plus compliqué…
 • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes, une adresse
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactères
           ville : chaîne de caractères
           code : entier
    FIN STRUCTURE

    STRUCTURE Etudiant
             nom : chaîne de caractères
           prenom : chaîne de catactères
           num : entier
           groupe : entier
            note[N] : tableau de rééls
           add : Adresse
                                                                                                                   29
    FIN STRUCTURE
                                                                                                E. ANSERMIN | R. GRIGNON
~~~

## Page 30

~~~text
Un exemple plus compliqué…
 • Chaque étudiant a : un nom, un prénom, un numéro etudiant, un groupe, N notes, une adresse
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactères                     Pour indiquer le code postal d’un Etudiant:
           ville : chaîne de caractères
           code : entier                                  VARIABLE
    FIN STRUCTURE                                                   etu1 : Etudiant
                                                          DEBUT
    STRUCTURE Etudiant
                                                                    etu1.add.code <- 95000
             nom : chaîne de caractères
           prenom : chaîne de catactères
           num : entier                                  Se lit : “ le code de l’adresse de l’étudiant etu1”
           groupe : entier
            note[N] : tableau de rééls
           add : Adresse
                                                                                                                        30
    FIN STRUCTURE
                                                                                                     E. ANSERMIN | R. GRIGNON
~~~

## Page 31

~~~text
Un exemple plus compliqué…
 • Et pour gérer la promotion de 330 élèves?
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactères
           ville : chaîne de caractères
           code : entier
    FIN STRUCTURE

    STRUCTURE Etudiant
             nom : chaîne de caractères
           prenom : chaîne de catactères
           num : entier
           groupe : entier
            note[N] : tableau de rééls
           add : Adresse
                                                                  31
    FIN STRUCTURE
                                               E. ANSERMIN | R. GRIGNON
~~~

## Page 32

~~~text
Un exemple plus compliqué…
 • Et pour gérer la promotion de 330 élèves?
    Constante NB_ETU <- 330
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactères          VARIABLE
           ville : chaîne de caractères
           code : entier                               prom[NB_ETU] : tableau d’Etudiant
    FIN STRUCTURE                              DEBUT
    STRUCTURE Etudiant
             nom : chaîne de caractères
           prenom : chaîne de catactères
           num : entier
           groupe : entier
            note[N] : tableau de rééls
           add : Adresse                                                                          32
    FIN STRUCTURE                                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 33

~~~text
Un exemple plus compliqué…
 • Et pour gérer la promotion de 330 élèves?
    Constante NB_ETU <- 330
    STRUCTURE Adresse
             num : entier
           rue : chaîne de catactères          VARIABLE
           ville : chaîne de caractères
           code : entier                               prom[NB_ETU] : tableau d’Etudiant
    FIN STRUCTURE                              DEBUT
    STRUCTURE Etudiant                                 prom[0].nom<-“Dupont”
             nom : chaîne de caractères                prom[5].groupe <- 2
           prenom : chaîne de catactères               prom[1].add.num <- 56
           num : entier
           groupe : entier                             prom[1].num<- 225784
            note[N] : tableau de rééls                 …
           add : Adresse                                                                          33
    FIN STRUCTURE                                                              E. ANSERMIN | R. GRIGNON
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

     nomVariable.champ                                     34
                                        E. ANSERMIN | R. GRIGNON
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
             struct Coordonnée c1;
             scanf("%f",&c1.abcisse);
             scanf("%f",&c1.ordonnee);
             printf( "Les coordonnées de c1 sont (%f, %f) \n",
                      c1.abcisse,
                      c1.ordonnee );
             return 0;
                                                                                  35
        }                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 36

~~~text
Les structure en C : syntaxe
  ●   Exemple

        //Attention à l’ordre !!
        struct Adresse{
               int num;
               char rue[200]; // Tableau de caractères
               char ville[200];
               int code;
        };

        struct Etudiant{
               char nom[200];
               char prenom[200];
               int groupe;
               int num;
               struct Adresse add; // Adresse doit etre décrite avant
        };                                                                                 36
                                                                        E. ANSERMIN | R. GRIGNON
~~~

## Page 37

~~~text
Types équivalents
 ●   Permet de renommer un type existant
 ●   Permet de simplifier une écriture, de gagner en expressivité
 ●   Exemple :
     typedef type nouveau_nom ;
     typedef type nouveau_nom1, nouveau_nom2, ... ;




                                                                                       37
                                                                    E. ANSERMIN | R. GRIGNON
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




                                          38
                       E. ANSERMIN | R. GRIGNON
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
                                                                                  39
                                                               E. ANSERMIN | R. GRIGNON
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



                                                                                                     40
                                                                                  E. ANSERMIN | R. GRIGNON
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
                                                                       41
                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 42

~~~text
Exemple

typedef enum { PIQUE, COEUR, CARREAU, TREFLE } Couleur;

typedef struct {
    char valeur ; /∗ 1->10, 11: valet, 12: dame, 13: roi ∗/
    Couleur c_couleur ;
} Carte;

typedef Carte[52] Deck;   // Deck definit un lot de 52 Cartes

/∗ Utilisation ∗/
Deck jeu ;
jeu[0].valeur = 1;
jeu[0].c_couleur = TREFLE;

                                                                                   42
                                                                E. ANSERMIN | R. GRIGNON
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

                                                                                            43
                                                                         E. ANSERMIN | R. GRIGNON
~~~

## Page 44

~~~text
Pour completer
 ●   Enumeration des types de rue pour completer la structure Adresse:




                 typedef enum {
                     RUE, BOULEVARD, IMPASSE, CHEMIN, AVENUE
                 } type_rue;




                                                                                            44
                                                                         E. ANSERMIN | R. GRIGNON
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
   } Etudiant;                                                             45
                                                        E. ANSERMIN | R. GRIGNON
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
                                                                      46
                                                   E. ANSERMIN | R. GRIGNON
~~~

## Page 47

~~~text
Conclusion

• Il est possible de créer/personnaliser ses propres types.
• Une structure est composée de sous-variables appellées champs ou attributs
    ou membres.
•   Pour acceder à un membre d’une variable de type structure:
                  • nomVariable.membre
• L’énumeration est un type qui permet de prendre un valeur définie parmi
    d’autres.
• On peut faire de l’imbrication de structures/énumerations pour créer des types
    complexes.                                                                                 47
                                                                            E. ANSERMIN | R. GRIGNON
~~~
