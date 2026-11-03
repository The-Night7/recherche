# 06a_Compilation_separee.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Y8y7MEFR-Z6fMyqPL7VcqMzbqvxuD7MF) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                            v1.00




PROGRAMMATION
PROCEDURALE
6 A . C O M P I L AT I O N S E P A R E E
__




                                           Eva ANSERMIN & Romuald GRIGNON
~~~

## Page 2

~~~text
Problématiques
 • Code trop long : compliqué de rechercher les différentes
   parties qui nous intéressent / que l’on souhaite modifier

 • Code long : compilation lente tout le code va être inspecté
   même les parties qui ne sont pas utilisées

 • Gestion des fonctions : les différentes fonctions doivent être
   écrites dans le bon ordre si elles s’appellent entre elles




                                                                                         2
                                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 3

~~~text
Problématique : appel croisé
 • S’il existe un appel croisé de fonctions, chacune doit être écrite avant
    l'autre pour que le compilateur puisse les utiliser : ce n'est pas possible
    implicitement.

     void funcA(…){
         …
         funcB(…);           // déclaration implicite !
         …
     }

     void funcB(…){
         …
         funcA(…);          // appel croisé
         …
     }
                                                                                                       3
                                                                                  E. ANSERMIN | R. GRIGNON
~~~

## Page 4

~~~text
Solution : déclaration explicite
 // déclaration explicite des prototypes de fonctions !
 void funcA(…);
 void funcB(…);


 void funcA(…){
     …
     funcB(…);    // pas d'erreur à la compilation
     …
 }


 void funcB(…){
     …
     funcA(…);    // pas d'erreur à la compilation
     …
                                                                               4
 }                                                        E. ANSERMIN | R. GRIGNON
~~~

## Page 5

~~~text
Problématique : modules
 • Il est possible d’écrire un code en plusieurs parties ou modules

 • Chaque module peut être compilé séparément. Cependant séparer le
   code en modules doit s’accompagner d’un moyen pour chacun des
   modules d’interagir avec les autres sans conflit

 • Si l’on souhaite fournir un module de code compilé sans les sources, il
   faut pouvoir au moins fournir les prototypes des fonctions à appeler,
   les constantes utilisées, ou les types redéfinis (comme les structures
   par exemple)



                                                                                                  5
                                                                             E. ANSERMIN | R. GRIGNON
~~~

## Page 6

~~~text
Problématique : modules
 • Il existe 2 grands types de fichiers lorsque l’on écrit un code séparé
   en modules en langage C

 • Les fichiers contenant des instructions classiques, du code. Dans
   notre cas des fichiers *.c (exemple : main.c, tris.c, …)

 • Les fichiers d’entête, ou headers. Ce sont les fichiers *.h. ils
   permettent de rassembler les “entêtes” communs à plusieurs
   fichiers sources et/ou autres fichiers d’entête.




                                                                                                 6
                                                                            E. ANSERMIN | R. GRIGNON
~~~

## Page 7

~~~text
Problématique : modules
 • Le fichier d'entête :
    • est généralement nommé comme le fichier *.c qu'il accompagne
    • contient les inclusions d'autres fichiers d'entête nécessaires
    • contient les déclarations de fonctions (prototypes)
    • contient les définitions de constantes (#define …)
    • contient les variables globales utilisées
    • contient les redéfinitions de types (typedef) notamment celles pour
       les structures
    • ne contient pas la déclaration de la fonction main !
                                                                                                 7
                                                                            E. ANSERMIN | R. GRIGNON
~~~

## Page 8

~~~text
Problématique : modules
  tris.h                          functions_tri.c
  #include<stdio.h>               void triRapide(…){
  #define TAILLE 1000                 …
                                      pivot=partition(…);
  void triSelection(int tab[]);
                                       …
  void triRapide( int tab[],
                                  }
                  int debut,
                                  int partition(…){
                  int fin);
                                      …
  int partition(…);
                                      …
                                  }
  main.c
                                  void triSelection(…){
  int main(){
                                           …
      int tab[TAILLE];
                                  }
           triSelection(tab);
           …
      return 0;                   Problème : comment communiquent
  }                               les fichiers entre eux ?                               8
                                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 9

~~~text
Les directives de pré-processeur
  • Certaines commandes ne sont pas exécutées lors de l’exécution
    mais lors de la première phase de compilation. Ce sont les directives
    de préprocesseurs.
  • Les directives de préprocesseurs sont précédées de #
  • Elles effectuent des modifications textuelles sur le fichier source:
  • Exemple :
     • #define permet de remplacer une expression par une autre
       (définition de constante ou de macro)
     • #include permet d'incorporer dans le fichier source le texte
       figurant dans un autre fichier. (#include<stdio.h> permet d’inclure
       le code de la bibliothèque stdio au code)

                                                                                                  9
                                                                             E. ANSERMIN | R. GRIGNON
~~~

## Page 10

~~~text
Les directives de pré-processeur
 • Il est possible d’obtenir le fichier intermédiaire après la phase de préprocessing
   avec l’option –E dans gcc.
 • Par défaut cette commande renvoie le résultat sur la sortie standard. Il est possible
   de stocker cette sortie dans un fichier toujours avec l‘option -o
main.c
// constante                              gcc -E main.c -o main.i
#define TAILLE 15
// macro
#define COUCOU() printf("Coucou")      main.i

int main(){                            int main(){
    int tab[TAILLE]                        int tab[15]
    for(int i=0; i<TAILLE; i++){           for(int i=0; i<15; i++){
        …                                      …
    }                                      }
    COUCOU();                              printf("Coucou");
    return 0 ;                             return 0 ;                                            10
}                                      }
                                                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 11

~~~text
Problématique : modules

 • Différents modules doivent pouvoir s’échanger des informations : il faut
   notamment que les fichiers .c puisse avoir accès aux information des
   fichiers .h
 • La directive de préprocesseur #include : permet d'inclure un fichier dans
   un autre. Cela permet de fusionner le contenu de plusieurs fichiers de
   manière dynamique et de fournir le résultat à la phase de compilation.


                        #include "fichierHeader.h"


 • Il faut donc inclure, entre autres, les fichiers .h utiles dans les fichiers.c

                                                                                                       11
                                                                                    E. ANSERMIN | R. GRIGNON
~~~

## Page 12

~~~text
Problématique : modules
   tris.h
   #include<stdio.h>               functions_tri.c
                                   #include "tris.h"
   #define TAILLE 1000
                                   void triRapide(…){
   void triSelection(int tab[]);       …
   void triRapide(int tab[],int        pivot=partition(…);
   debut, int fin);
                                        …
   int partition(…);
                                   }
    main.c                         int partition(…){
    #include "tris.h"                  …
    int main(){                        …
        int tab[TAILLE];           }
        triSelection(tab);         void triSelection(…){
        …                                   …
        return 0;                  }
    }                                                                           12
                                                             E. ANSERMIN | R. GRIGNON
~~~

## Page 13

~~~text
Solution : fichiers d’entête
    functions.h                functions.c
    void funcA(…);             #include "functions.h"
    void funcB(…);             void funcA(…){
                                    …
    main.c
                                    funcB(…);
    #include "functions.h"              …
                               }
    int main(){                void funcB(…){
        funcA(…);                   …
        return 0;                   funcA(…);
    }                               …
                               }                                           13
                                                        E. ANSERMIN | R. GRIGNON
~~~

## Page 14

~~~text
Solution : fichiers d’entête
• Il faut donc pouvoir être capable de compiler chaque fichier C
  indépendemment des autres. L'option –c de gcc permet cette opération :
              gcc –c functions.c -o functions.o
              gcc –c main.c -o main.o
• Les fichiers issus de cette compilation sont des fichiers objets (*.o) c’est à
  dire des fichiers intermédiaires dans le processus de compilation


• Il faut maintenant réunir/fusionner tous les "objets" (morceaux de codes
  compilés) en un seul exécutable : toujours grâce à gcc mais cette fois-ci,
  les fichiers d'entrée ne sont plus les fichiers *.c mais les fichiers *.o
  générés précédemment :
              gcc functions.o main.o -o myExec
                                                                                                      14
                                                                                   E. ANSERMIN | R. GRIGNON
~~~

## Page 15

~~~text
Solution : fichiers d’entête
                             gcc –c …


                    main.c                main.o


                                                      gcc …

      functions.h


                             gcc –c …


               functions.c              functions.o
                                                                                 15
                                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 16

~~~text
Problématique : inclusions circulaires
 • Maintenant que nous pouvons compiler indépendamment les différents fichiers C
   de notre application, il apparait un nouveau problème
 • Il est possible que deux modules s'incluent respectivement : création d'une boucle
   d'inclusion infinie
 • Ces inclusions mutuelles ne sont pas forcément directes
     • le Module A est inclus par le module B
     • le module B est inclus par le module C
     • le module C est inclus par le module A
 • Il va donc falloir se prémunir des multiples inclusions en utilisant les instructions de
   compilation conditionnelle
 • Ces instructions permettent de "désactiver" des portions de code en fonction de
   paramètres statiques (configuration du programme)

                                                                                                           16
                                                                                        E. ANSERMIN | R. GRIGNON
~~~

## Page 17

~~~text
Problématique : inclusions circulaires (ex. #1)
    moduleA.h                 moduleC.h
    #include "moduleC.h"      #include "moduleB.h"
     void funcA(…);           void funcC(…);




    main.c
    #include "moduleA.h"      moduleB.h
    int main(){               #include "moduleA.h"
        funcA(…);             void funcB(…);
        return 0;
    }
                                                                        17
                                                     E. ANSERMIN | R. GRIGNON
~~~

## Page 18

~~~text
Solution : compilation conditionnelle
 • Idée: introduire un « ordre » d’inclusion grâce à des conditions.
 • Rappel : #define : permet de définir une macro, qui est une chaine de caractères
   servant à remplacer, soit des constantes, soit des suites d'instructions
 • Les directives préprocesseurs #ifdef / #ifndef … #elif … #else … #endif : ces
   instructions conditionnelles testent l'existence de macros définies (ou non), et
   incluent (ou non) la portion de code C associée.



         #define CONST 15                 #define CONST 15
         #ifdef CONST                     #ifndef CONST
             // Instructions                  // Instructions
             // compilées                     // NON compilées
             …                                …
         #endif                           #endif
                                                                                                 18
                                                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 19

~~~text
 Solution : compilation conditionnelle
              moduleA.h                             moduleB.h

              #ifndef MODULE_A_H                    #ifndef MODULE_B_H
                #define MODULE_A_H                    #define MODULE_B_H
                #include "moduleB.h"                  #include "moduleA.h"
                …                                     …
              #endif                                #endif

• Le fait de définir une constante MODULE_A_H (nom totalement arbitraire dans
  l'absolu, mais dans la pratique on reprend le nom du fichier) la 1ère fois que le
  fichier moduleA.h est inclus, va permettre, lors des prochaines inclusions, de
  "masquer" l'ensemble du contenu du fichier
• Cette méthode permet d'inclure les différentes dépendances dans un ordre
                                                                                                   19
  quelconque et simplifie grandement le développement
                                                                                E. ANSERMIN | R. GRIGNON
~~~

## Page 20

~~~text
Problématique : inclusions circulaires (ex. #1)
 moduleA.h                  moduleC.h
 #ifndef MODULE_A_H         #ifndef MODULE_C_H
     #define MODULE_A_H       #define MODULE_C_H
     #include "moduleC.h"     #include "moduleB.h"
  #endif                    #endif
  void funcA(…);            void funcA(…);


 main.c                     moduleB.h
 #include "moduleA.h"       #ifndef MODULE_B_H
 int main(){                  #define MODULE_B_H
      funcA(…);               #include "moduleA.h"
      return 0;             #endif
                                                                        20
 }                          void funcA(…);
                                                     E. ANSERMIN | R. GRIGNON
~~~

## Page 21

~~~text
Problématique : inclusions multiples (ex. #2)
    moduleA.h                           main.i
    void funcA(…);
                                        ...
                                        void funcA(…);
    main.c                                                ERREUR
                                        void funcA(…);
    #include "functions.h"              ...
    #include "functions.h"              ...
    int main(){                         int main(){
        funcA(…);                             funcA(…);
        return 0;                             return 0;
    }                                   }


                     • gcc –E main.c -o main.i                                        21
                                                                   E. ANSERMIN | R. GRIGNON
~~~

## Page 22

~~~text
Problématique : inclusions multiples (ex. #2)
    functions.h                    main.i
    #ifndef FUNCTIONS_H
                                   …
         #define FUNCTIONS_H
                                   void funcA(…);
         void funcA(…);                              OK
                                   ...
    #endif
                                   ...
    main.c                         ...
    #include "functions.h"         int main(){
    #include "functions.h"               funcA(…);
    int main(){                          return 0;
         funcA(…);                 }
         return 0;
    }                          • gcc –E main.c -o main.i                      22
                                                           E. ANSERMIN | R. GRIGNON
~~~

## Page 23

~~~text
Problématique : code conditionnel (ex. #3)
  system.h                      parameters.h
  #include "parameters.h"       #define WINDOWS 1
  #if OS == WINDOWS             #define LINUX 2
    ...                         #define MACOS 3
  #elif OS == LINUX             #define OS LINUX
    ...
  #elif OS == MACOS
    ...                         main.c
  #else                         #include "system.h"
    #error Bad value for 'OS'   int main(){
  #endif                            …
                                    return 0;
                                }                                        23
                                                      E. ANSERMIN | R. GRIGNON
~~~

## Page 24

~~~text
GCC : phases de compilation
 • Maintenant nous allons voir les différentes phases de l’exécutable gcc et les options
   associées :

    PREMIERE ETAPE :
    gcc –E main.c -o main.i
    L'option –E de gcc (pré-traitement) permet de voir en sortie le programme C qui
    sera effectivement compilé
        • Le code non compilé entre les instructions #ifndef / #ifdef ne va plus
          apparaître
        • Toutes les macros ont été remplacées par leurs valeurs
        • L’ensemble des fichiers inclus par le fichier C est fusionné dans l’ordre
          d’inclusion : il n’y a donc plus qu’un seul fichier à compiler

                                                                                                         24
                                                                                      E. ANSERMIN | R. GRIGNON
~~~

## Page 25

~~~text
GCC : phases de compilation
 • Maintenant nous allons voir les différentes phases de l’exécutable gcc et les options
   associées :

    DEUXIEME ETAPE :
    gcc –S main.i -o main.s
    L'option –S de gcc (compilation), permet de transformer le code C précédent en
    code assembleur (toujours lisible par l'humain… )
        • C’est cette phase qui va donc interpréter la syntaxe du code C et qui écrit
          régulièrement sur la console que vous avez oublié un point-virgule, qu’un
          symbole n’est pas déclaré ou qu’il y a un souci dans l’organisation des
          accolades
        • Un compilateur est spécifique à une cible physique (ou une famille de
          cibles) : le code assembleur généré est donc spécifique à un composant
          physique particulier
                                                                                                      25
                                                                                   E. ANSERMIN | R. GRIGNON
~~~

## Page 26

~~~text
GCC : phases de compilation
 • Maintenant nous allons voir les différentes phases de l’exécutable gcc et les options
   associées :

    TROISIEME ETAPE :
    gcc –c main.s -o main.o
    L'option –c de gcc (compilation) permet de transformer le code assembleur en
    code machine, c’est à dire en un code que seul le composant cible peut interpréter
        • Il est donc difficile ici de pouvoir lire le code généré d’une manière fluide
          comme on pourrait le faire en C
        • C’est donc une partie de notre exécutable qui se trouve dans ce fichier, avec
          certains symboles qui n’ont pas encore été résolus (telles que les fonctions
          appelées qui sont situées dans d’autres modules (d’autres fichiers C) qui ne
          sont pas forcément encore compilés)
                                                                                                             26
                                                                                          E. ANSERMIN | R. GRIGNON
~~~

## Page 27

~~~text
GCC : phases de compilation
 • Maintenant nous allons voir les différentes phases de l’exécutable gcc et les options
   associées :

    QUATRIEME ETAPE :
    gcc main.o -o main.exe
    L’exécutable gcc sans option (édition de liens) permet de fusionner les différents
    codes machines (fichiers objets) dans un seul exécutable que notre machine
    pourra alors exécuter
        • Ici gcc cherche à résoudre tous les symboles pour relier les morceaux de
          code entre eux. Il va “coller” bout à bout l’ensemble des fonctions et va
          déterminer l’adresse de code pour chacune d’entre elles : ensuite lors d’un
          appel de fonction, le code effectue un “saut” de code à la bonne adresse
        • C’est à cette étape que gcc écrit sur le terminal qu’il n’a pas trouvé telle ou
          telle fonction (quand on utilise la bibliothèque math et que l’on ne met pas
                                                                                                         27
          l’option -lm par exemple)
                                                                                      E. ANSERMIN | R. GRIGNON
~~~

## Page 28

~~~text
Quelques directives du pré-processeur
•   #include : permet d'inclure un fichier dans un autre. Cela permet de fusionner le
    contenu de plusieurs fichiers de manière dynamique et de fournir le résultat à la
    phase de compilation
•   #define : permet de définir une macro (terme consacré), qui est une chaine de
    caractères servant à remplacer, soit des constantes, soit des suites d'instructions
    verbeuses et nombreuses. Le but est de fournir le moyen d'écrire un code plus
    concis et lisible
•   #undef : permet "d'oublier" une macro définie précédemment
•   #ifdef / #ifndef … #elif … #else … #endif : ces instructions conditionnelles testent
    l'existence de macros définies (ou non), et permet d’inclure (ou non) la portion de
    code C associée. Nous avons vu leur utilisation lors de la résolution de la
    problématique d'inclusions multiples, mais ces directives servent aussi à fournir
    différentes versions de code en fonction de paramètres utilisateurs
                                                                                                   28
                                                                                E. ANSERMIN | R. GRIGNON
~~~

## Page 29

~~~text
Quelques directives du pré-processeur
•   #if defined(…) : effectue la même action que la directive #ifdef … à la
    différence que la seconde ne peut tester que la définition d’une macro, alors
    que la première peut effectuer plusieurs comparaisons, combinées ensemble
    grâce à des opérateurs logiques :
            #if defined(LINUX) || defined (ANDROID)
            .

•   #if !defined(…) : effectue la même action que la directive #ifndef … avec la
    même spécificité qu’énoncée au pragraphe précédent
•   #if … == … : permet d'effectuer des comparaisons entre des valeurs de
    macros et/ou des valeurs entières, pour construire conditionnellement un
    programme. Fonctionne aussi avec les opérateurs == , != , < , > , <= , >=
•   #error : stoppe la compilation et affiche le message qui suit la directive.
    Permet d'indiquer une mauvaise configuration du programme
                                                                                                     29
                                                                                  E. ANSERMIN | R. GRIGNON
~~~

## Page 30

~~~text
Quelques directives du pré-processeur
•   Macros prédéfinies : il existe des macros qui permettent de récupérer toutes
    sortes d'informations sur votre programme :
     ⚫   __FILE__ : chemin du fichier courant (chaîne)
     ⚫   __LINE__ : numéro de ligne du fichier courant (entier)
     ⚫   __DATE__ : date de compilation (chaîne "Feb 23 2022")
     ⚫   __TIME__ : heure de compilation (chaîne "23:59:59")
•   Ces macros peuvent être utilisées pour afficher des détails sur le programme
    notamment en cas d’erreur par exemple
•   Pour les utiliser comme paramètres de fonctions comme printf, il faudra bien
    entendu indiquer le type adéquat (%d ou %s)
•   Bien évidemment ces valeurs sont des constantes pour le fichier actuellement
    compilé et d’un fichier C à un autre, les valeurs de __DATE__ et __TIME__
    peuvent changer par exemple                                                                 30
                                                                             E. ANSERMIN | R. GRIGNON
~~~

## Page 31

~~~text
Conclusion :
•   La modularité impose de créer des fichiers d’entête qui contiennent les prototypes
    des fonctions, les constantes, les types redéfinis, structures nécessaires à la bonne
    utilisation du module.
•   Chaque module peut être compilé indépendemment des autres à partir du moment
    où les interfaces sont prévues (fichiers d’entête)
•   Les fichiers d’entête doivent être protégés contre les multiples inclusions : cela
    permet de coder les fonctions dans n’importe quel ordre et d’inclure les modules
    dans n’importe quel ordre
•   Travail en équipe plus facile
•   Gestion de version facilitée (git merge)
•   La compilation séparée est obligatoire
•   Compiler manuellement n’est pas une solution
       → Il faut automatiser                                                                      31
                                                                               E. ANSERMIN | R. GRIGNON
~~~
