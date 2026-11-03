# CM02-Pointeur_2023-2024_Informatique2_P1S2_EAnsermin-RGrignon.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1bp4kqTRQXFfRs3imqsAQO4kHdCiPRAuM) · Les pages signalées comprennent du texte reconnu automatiquement ou des éléments graphiques. Le fac-similé permet de vérifier chaque lecture.

**Pages avec fac-similé ou lecture OCR** — 1.

## Page 1

![Fac-similé de la page 1](../facsimiles/93b632f6cb0380da1e7f43d3.jpg)

~~~text
INFORMATIQUE 2
II. LES POINTEURS
~~~

**Lecture OCR à contrôler**

~~~text
INFORMATIQUE 2

Il. LES POINTEURS
~~~

## Page 2

~~~text
Les mystères du C
 • Pourquoi scanf(“%d”,&a) alors que printf(“%d”,a)?

 • Pourquoi scanf(“%d”,&c) alors que scanf(“%s”, c)?

 • Comment faire pour retourner plusieurs valeurs depuis une fonction?

 • Pourquoi les éléments d'un tableau passé en paramètre d’une fonction
    sont modifiés et pas les variables « classiques »?
~~~

## Page 3

~~~text
Rappel
 • Une variable est stockée dans la RAM de l’ordinateur

 • Chaque cellule de la mémoire est designée par une adresse.
                                       Adresse            Valeur
                                       1154
       int   a = 2;                a   1155               2
       float b = 10;                   …
                                       …
                                       …
                                   b   10 028             10



 • Une variable est accessible par son nom
~~~

## Page 4

~~~text
Adresse d’une variable
 • On peut acceder à l’adresse d’une variable grace à &



                                       Adresse            Valeur
                                       1154
       int   a = 2;                a   1155               2
       float b = 10;                   …
                                       …
                                       …
                                   b   10 028             10

 • a=2      &a = 1155     b=10      &b=10 028
~~~

## Page 5

~~~text
Adresse d’une variable
 • On peut acceder à l’adresse d’une variable grace à &



                                       Adresse            Valeur
                                       1154
       int   a = 2;                a   1155               2
       float b = 10;                   …
                                       …
                                       …
                                   b   10 028             10

 • a=2      &a = 1155     b=10      &b=10 028
~~~

## Page 6

~~~text
Adresse d’une variable
 • En pratique

    // Programme d'exemple pour afficher
    // les adresses des variables
    int main(){

        int a = 2;
        int b = 10;
        printf("a=%d   b=%d   &a=%p   &b=%p\n", a,
    b, &a, &b);
        return 0;
    }
~~~

## Page 7

~~~text
Adresse d’une variable
 • En pratique

    // Programme d'exemple pour afficher
    // les adresses des variables
    int main(){

        int a = 2;
        int b = 10;
        printf("a=%d      b=%d   &a=%p   &b=%p\n", a,
    b, &a, &b);
        return 0;
    }


                 a=2   b=10   &a=0x7ffde2010c0c   &b=0x7ffde2010c08
~~~

## Page 8

~~~text
Adresse d’une variable
 • En pratique

     // Programme d'exemple pour afficher
     // les adresses des variables
     int main(){

         int a = 2;
         int b = 10;
         printf("a=%d     b=%d   &a=%p    &b=%p\n", a,
     b, &a, &b);
         return 0;
     }


                 a=2   b=10   &a=0x7ffde2010c0c    &b=0x7ffde2010c08


 • %p est le format pour afficher des adresses en hexa-decimal
~~~

## Page 9

~~~text
Adresse d’une variable: scanf

                                            Adresse           Valeur
                                            1154
        int a =2;                       a   1155              2
        float b = 10;
                                            …
                                            …
        scanf(«%d », &a );                  …
                                        b   10 028            10

       Adresse de stockage de la variable saisie au clavier
                                =
       « mettre la valeur saisie à l’adresse &a »
~~~

## Page 10

~~~text
Adresse d’une variable: scanf

                                      Adresse                Valeur
                                      1154
        int a =2;
                                  a   1155                   2
        float b = 10;
                                      …
                                      …
        scanf(«%d », &a );
                                      …
        scanf(« %d »,1155);       b   10 028                 10


        scanf(«%d », a );
                              Espace mémoire non autorisé : erreur de segmentation !
        scanf(« %d »,2);
~~~

## Page 11

~~~text
Les pointeurs
 • Principe : accéder à une variable par son adresse plutôt que par son
   nom.

 • Un pointeur est :
    • Une variable donr la valeur est une adresse mémoire …
~~~

## Page 12

~~~text
Les pointeurs
 • Principe : accéder à une variable par son adresse plutôt que par son
   nom.

 • Un pointeur est :
    • Une variable donr la valeur est une adresse mémoire …
    • L’adresse d’une autre variable !
                Adresse          Valeur
                1154
            a   1155             2
                …                                   On dit que pa pointe sur a.
                …
                …
            pa 10 028            1155
~~~

## Page 13

~~~text
Les pointeurs : déclaration
 • Un pointeur peut pointer sur tout type de données (entier, reel, autre
     pointeur ! …)
 •   Il est déclaré avec le caractère *
 •   Un pointeur est déclaré avec le type de la variable sur laquelle il pointe




                            Type * nomPointeur;



              Type de la variable pointée   Nom du pointeur
~~~

## Page 14

~~~text
Les pointeurs : déclaration
 • Un pointeur peut pointer sur tout type de données (entier, reel, autre
     pointeur ! …)
 •   Il est déclaré avec le caractère *
 •   Un pointeur est déclaré avec le type de la variable sur laquelle il pointe



                         Type * nomPointeur;
                                       ou

                          Type * nomPointeur;
                                        ou

                          Type *nomPointeur;
~~~

## Page 15

~~~text
Les pointeurs : déclaration
 • Exemple :
                                        Adresse   Valeur
 int    a;                          a 1154        ???
 float b;
                                        1155
 int*   p1; // pointeur sur int
 float* p2; // pointeur sur float       …
                                    p2 5340       ???
                                        …
                                        10 028
                                    b   10 029    ???
                                        …
                                        …
                                    p1 22 222     ???
~~~

## Page 16

~~~text
Les pointeurs : déclaration
 • Exemple :
                                        Adresse   Valeur
 int    a;                          a 1154        5
 float b;
                                        1155
 int*   p1; // pointeur sur int
 float* p2; // pointeur sur float       …
                                    p2 5340       ???
 a=5;
                                        …
                                        10 028
                                    b   10 029    ???
                                        …
                                        …
                                    p1 22 222     ???
~~~

## Page 17

~~~text
Les pointeurs : déclaration
 • Exemple :
                                        Adresse   Valeur
 int    a;                          a 1154        5
 float b;
                                        1155
 int*   p1; // pointeur sur int
 float* p2; // pointeur sur float       …
                                    p2 5340       ???
 a=5;
                                        …
 p1=&a; // prend l’adresse de a
                                        10 028
                                    b   10 029    ???
                                        …
                                        …
                                    p1 22 222     1154
~~~

## Page 18

~~~text
Les pointeurs : déclaration
 • Exemple :
                                        Adresse   Valeur
 int    a;                          a 1154        5
 float b;
                                        1155
 int*   p1; // pointeur sur int
 float* p2; // pointeur sur float       …
                                    p2 5340       ???
 a=5;
                                        …
 p1=&a; // prend l’adresse de a
 b=2.5;                                 10 028
                                    b   10 029    2,5
                                        …
                                        …
                                    p1 22 222     1154
~~~

## Page 19

~~~text
Les pointeurs : déclaration
 • Exemple :
                                        Adresse   Valeur
 int    a;                          a 1154        5
 float b;
                                        1155
 int*   p1; // pointeur sur int
 float* p2; // pointeur sur float       …
                                    p2 5340       10 029
 a=5;
                                        …
 p1=&a; // prend l’adresse de a
 b=2.5;                                 10 028
 p2=&b //prend l’adresse de b       b   10 029    2,5
                                        …
                                        …
                                    p1 22 222     1154
~~~

## Page 20

~~~text
Les pointeurs : déclaration
 • Exemple :
                                        Adresse   Valeur
 int    a;                          a 1154        5
 float b;
                                        1155
 int*   p1; // pointeur sur int
 float* p2; // pointeur sur float       …
                                    p2 5340       10 029
 a=5;
                                        …
 p1=&a; // prend l’adresse de a
 b=2.5;                                 10 028
 p2=&b //prend l’adresse de b       b   10 029    2,5
                                        …
                                        …
                                    p1 22 222     1154


          p1 pointe sur a     p2 pointe sur b
~~~

## Page 21

~~~text
Les pointeurs : initialisation
 • Pour initialiser un pointeur (indiquer qu’il ne pointe sur aucune variable),
   on utilise le mot clef NULL (cette constante indique la valeur 0)



       Type * nomPointeur = NULL; //on pointe à l’adresse 0




                    ⚠️ Il est important d’initialiser les pointeurs ⚠️
              pour ne pas risquer de modifier un espace mémoire interdit
~~~

## Page 22

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple
    int    a;
    int*   p1; // pointeur sur int
    a = 5;
    p1 = &a;   // prend l'adresse de a
    printf(" a =%d \n", a);
    printf("*p1=%p \n",*p1);
    *p1 = 10;
    printf(" a =%d \n", a);
~~~

## Page 23

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                   1154             ???
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                        10 029           ???
                                                   …
                                                   …
                                                   22 222
~~~

## Page 24

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              ???
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                        10 029           ???
                                                   …
                                                   …
                                                   22 222
~~~

## Page 25

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              ???
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           ???
                                                   …
                                                   …
                                                   22 222
~~~

## Page 26

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              5
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           ???
                                                   …
                                                   …
                                                   22 222
~~~

## Page 27

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              5
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           1154
                                                   …
                                                   …
                                                   22 222
~~~

## Page 28

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              5
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           1154
                                                   …
                               a=5                 …
                                                   22 222
~~~

## Page 29

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              5
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           1154
                                                   …
                               a=5                 …
                               *p1=5
                                                   22 222
~~~

## Page 30

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              10
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           1154
                                                   …
                               a=5                 …
                               *p1=5
                                                   22 222
~~~

## Page 31

~~~text
Les pointeurs : utilisation
• Un pointeur permet d’accéder à une variable via son adresse
• Le caractère * permet d’accéder à la variable pointée par le pointeur. Sa
  signification est « ce qui est contenu dans l’adresse »

• Exemple                                          Adresse          Valeur
                                                a 1154              10
    int    a;                                      1155
    int*   p1; // pointeur sur int                 …
    a = 5;
    p1 = &a;   // prend l'adresse de a             5340
    printf(" a =%d \n", a);                        …
    printf("*p1=%p \n",*p1);                       10 028
    *p1 = 10;
    printf(" a =%d \n", a);                     p1 10 029           1154
                                                   …
                               a=5                 …
                               *p1=5
                                                   22 222
                               a=10
~~~

## Page 32

~~~text
Les pointeurs : utilisation
• Exercice                                   Adresse   Valeur
                                             1154
                                             1155
     int    a;
                                             …
     float b;
     int*   p1;                              5340
     float* p2;                              …
     a   = 5;
                                             10 028
     p1 = &a;
     b   = 2.5;                              10 029
     p2 = &b;                                …
     *p1 = 4;
                                             …
     b   = 0.3;
                                             22 222

Quelle est la valeur des variables suivantes ?
a=              p1=                          *p1 =

b=             p2 =                         *p2 =
~~~

## Page 33

~~~text
Les pointeurs : utilisation
• Exercice                                       Adresse         Valeur
                                                 1154
                                                 1155
     int    a;
                                                 …
     float b;
     int*   p1;                                  5340
     float* p2;                                  …
     a   = 5;
                                                 10 028
     p1 = &a;
     b   = 2.5;                                  10 029
     p2 = &b;                                    …
     *p1 = 4;
                                                 …
     b   = 0.3;
                                                 22 222

Quelle est la valeur des variables suivantes ?
a= 4             p1= &a                              *p1 = 4

b= 0,3            p2 =&b                             *p2 = 0,3
~~~

## Page 34

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.

 int switch(int a, int b){
        int tmp;
        tmp=a;
        a=b;
        b=tmp;
        return(a);
        return(b);
 }
~~~

## Page 35

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.

 int switch(int a, int b){
        int tmp;
        tmp=a;
        a=b;
        b=tmp;
        return(a);
                           On ne peut pas retourner deux
        return(b);
                           valeurs !
 }


                   Comment faire ?
~~~

## Page 36

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                          Adresse           Valeur
    int switch(int a, int b){
                                          1154
           int tmp;
                                          1158
           tmp=a;
           a=b;                           115C
           b=tmp;                         …
           return(a);
    }                                     5340

                                          …
    int main(){
                                          10 028
           int x=3;
                                          10 02C
           int y=4;
                                          10 030
           int z=switch(x,y);
                                          …
           return 0;
                                          22 222
    }
~~~

## Page 37

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                           Adresse          Valeur
    int switch(int a, int b){
           int tmp;                      x 1154             3

           tmp=a;                          1158

           a=b;                            115C
           b=tmp;
                                           …
           return(a);
    }                                      5340

                                           …
    int main(){
                                           10 028
           int x=3;
                                           10 02C
           int y=4;
                                           10 030
           int z=switch(x,y);
                                           …
           return 0;
                                           22 222
    }
~~~

## Page 38

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                           Adresse          Valeur
    int switch(int a, int b){
           int tmp;                      x 1154             3

           tmp=a;                        y 1158             4

           a=b;                            115C
           b=tmp;
                                           …
           return(a);
    }                                      5340

                                           …
    int main(){
                                           10 028
           int x=3;
                                           10 02C
           int y=4;
                                           10 030
           int z=switch(x,y);
                                           …
           return 0;
                                           22 222
    }
~~~

## Page 39

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                                Adresse             Valeur
    int switch(int a, int b){
           int tmp;                          x 1154                 3

           tmp=a;                            y 1158                 4

           a=b;                                 115C
           b=tmp;
                                                …
           return(a);
    }                                           5340

                                                …
    int main(){                             a   10 028              3
           int x=3;
           int y=4;                         b   10 02C              4
                                                10 030
           int z=switch(x,y);
                                                …
           return 0;
                                                22 222
    }
                   Les valeurs des variables passées en paramètres sont copiées:
                                    c’est un passage par valeur
~~~

## Page 40

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                             Adresse        Valeur
    int switch(int a, int b){
           int tmp;                      x 1154             3

           tmp=a;                        y 1158             4

           a=b;                              115C
           b=tmp;
                                             …
           return(a);
    }                                        5340

                                             …
    int main(){                          a   10 028         3
           int x=3;
           int y=4;                      b 10 02C           4

           int z=switch(x,y);          tmp 10 030
                                             …
           return 0;
                                             22 222
    }
~~~

## Page 41

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                             Adresse        Valeur
    int switch(int a, int b){
           int tmp;                      x 1154             3

           tmp=a;                        y 1158             4

           a=b;                              115C
           b=tmp;
                                             …
           return(a);
    }                                        5340

                                             …
    int main(){                          a   10 028         3
           int x=3;
           int y=4;                      b 10 02C           4

           int z=switch(x,y);          tmp 10 030           3
                                             …
           return 0;
                                             22 222
    }
~~~

## Page 42

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                                   Adresse                 Valeur
    int switch(int a, int b){
           int tmp;                             x 1154                     3

           tmp=a;                               y 1158                     4

           a=b;                                    115C
           b=tmp;
                                                   …
           return(a);
    }                                              5340

                                                   …
    int main(){                                a   10 028                  4
           int x=3;
           int y=4;                            b 10 02C                    4

           int z=switch(x,y);                tmp 10 030                    3
                                                   …
           return 0;
                                                   22 222
    }
             Modifier a ne modifie pas x: les variables sont décorrélées
~~~

## Page 43

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                             Adresse        Valeur
    int switch(int a, int b){
           int tmp;                      x 1154             3

           tmp=a;                        y 1158             4

           a=b;                              115C
           b=tmp;
                                             …
           return(a);
    }                                        5340

                                             …
    int main(){                          a   10 028         4
           int x=3;
           int y=4;                      b 10 02C           3

           int z=switch(x,y);          tmp 10 030           3
                                             …
           return 0;
                                             22 222
    }
~~~

## Page 44

~~~text
Les pointeurs : utilisation
• Objectif : écrire une fonction qui échange deux valeurs passées en paramètre.
• Rappel : ce qui se passe en mémoire
                                             Adresse        Valeur
    int switch(int a, int b){
           int tmp;                      x 1154             3

           tmp=a;                        y 1158             4

           a=b;                              115C
           b=tmp;
                                             …
           return(a);
    }                                        5340

                                             …
    int main(){                          a   10 028         4
           int x=3;
           int y=4;                      b 10 02C           3

           int z=switch(x,y);          tmp 10 030           3
                                             …
           return 0;
                                         z   22 222         4
    }
~~~

## Page 45

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){
    int tmp;
    tmp=*pa;
    *pa=*pb;
    *pb=tmp;
  }

  int main(){
    int x=3;
    int y=4;
    switch(&x,&y);
    return 0;
  }
~~~

## Page 46

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){             Adresse           Valeur

    int tmp;                                 1154
    tmp=*pa;                                 1158
    *pa=*pb;
                                             115C
    *pb=tmp;
  }                                          …

                                             5340
  int main(){
                                             …
    int x=3;
    int y=4;                                 10 028

    switch(&x,&y);                           10 02C

    return 0;                                10 030

  }                                          …
                                             22 222
~~~

## Page 47

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){               Adresse         Valeur

    int tmp;                               x   1154            3
    tmp=*pa;                                   1158
    *pa=*pb;
                                               115C
    *pb=tmp;
  }                                            …

                                               5340
  int main(){
                                               …
    int x=3;
    int y=4;                                   10 028

    switch(&x,&y);                             10 02C

    return 0;                                  10 030

  }                                            …
                                               22 222
~~~

## Page 48

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){               Adresse         Valeur

    int tmp;                               x   1154            3
    tmp=*pa;                               y   1158            4
    *pa=*pb;
                                               115C
    *pb=tmp;
  }                                            …

                                               5340
  int main(){
                                               …
    int x=3;
    int y=4;                                   10 028

    switch(&x,&y);                             10 02C

    return 0;                                  10 030

  }                                            …
                                               22 222
~~~

## Page 49

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){               Adresse         Valeur

    int tmp;                               x   1154            3
    tmp=*pa;                               y   1158            4
    *pa=*pb;
                                               115C
    *pb=tmp;
  }                                            …

                                               5340
  int main(){
                                               …
    int x=3;
    int y=4;                              pa   10 028

    switch(&x,&y);                        pb   10 02C

    return 0;                                  10 030

  }                                            …
                                               22 222
~~~

## Page 50

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){               Adresse         Valeur

    int tmp;                               x   1154            3
    tmp=*pa;                               y   1158            4
    *pa=*pb;
                                               115C
    *pb=tmp;
  }                                            …

                                               5340
  int main(){
                                               …
    int x=3;
    int y=4;                              pa   10 028          1154

    switch(&x,&y);                        pb   10 02C          1158

    return 0;                                  10 030

  }                                            …
                                               22 222
~~~

## Page 51

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){               Adresse         Valeur

    int tmp;                               x   1154            3
    tmp=*pa;                               y   1158            4
    *pa=*pb;
                                               115C
    *pb=tmp;
  }                                            …

                                               5340
  int main(){
                                               …
    int x=3;
    int y=4;                              pa   10 028          1154

    switch(&x,&y);                        pb   10 02C          1158

    return 0;                            tmp   10 030

  }                                            …
                                               22 222
~~~

## Page 52

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){                       Adresse    Valeur

    int tmp;                                       x   1154       3
    tmp=*pa;                                       y   1158       4
    *pa=*pb;
                                                       115C
    *pb=tmp;
  }                                                    …

                                                       5340
  int main(){
                                                       …
    int x=3;
    int y=4;                                      pa   10 028     1154

    switch(&x,&y);                                pb   10 02C     1158

    return 0;                                    tmp   10 030     3

  }                                                    …
                                                       22 222


                     On accède à la valeur de a via son adresse
~~~

## Page 53

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){                             Adresse                  Valeur

    int tmp;                                             x   1154                     4
    tmp=*pa;                                             y   1158                     4
    *pa=*pb;
                                                             115C
    *pb=tmp;
  }                                                          …

                                                             5340
  int main(){
                                                             …
    int x=3;
    int y=4;                                            pa   10 028                   1154

    switch(&x,&y);                                      pb   10 02C                   1158

    return 0;                                          tmp   10 030                   3

  }                                                          …
                                                             22 222



        « la valeur de la variable pointée par pa = la valeur de la variable pointée par pb »
~~~

## Page 54

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){                            Adresse        Valeur

    int tmp;                                            x   1154           4
    tmp=*pa;                                            y   1158           3
    *pa=*pb;
                                                            115C
    *pb=tmp;
  }                                                         …

                                                            5340
  int main(){
                                                            …
    int x=3;
    int y=4;                                           pa   10 028         1154

    switch(&x,&y);                                     pb   10 02C         1158

    return 0;                                         tmp   10 030         3

  }                                                         …
                                                            22 222



                     On modifie la valeur des variables via leur adresse
~~~

## Page 55

~~~text
Les pointeurs : utilisation
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

  void switch(int *pa, int *pb){                         Adresse   Valeur

    int tmp;                                         x   1154      4
    tmp=*pa;                                         y   1158      3
    *pa=*pb;
                                                         115C
    *pb=tmp;
  }                                                      …

                                                         5340
  int main(){
                                                         …
    int x=3;
    int y=4;                                    pa       10 028    1154

    switch(&x,&y);                              pb       10 02C    1158

    return 0;                                  tmp       10 030    3

  }                                                      …
                                                         22 222



                            Pas besoin de return !
~~~

## Page 56

~~~text
Le passage par adresse
• Principe : passer en argument d’une fonction des adresses plutôt que des valeurs.

• La fonction/procédure prends donc des adresses en arguments, soit des types
  pointeurs.

            type nomFonction(int *arg1, float *arg2, …)


• Une variable dont l’adresse passé est modifiable dans la fonction.

• C’est le passage par adresse (en opposition au passage par valeur).
~~~

## Page 57

~~~text
Tableaux et pointeurs
• Rappel : les valeurs d’un tableau sont à la suite dans la mémoire.



                                          Adresse        Valeur

                                 tab[0] 1154             1

                                 tab[1]                  3

                                 tab[2]                  0
  int main(){
                                 tab[3]                  0
    int tab[5]={1,3}
    return 0;                    tab[4]                  0

  }                                       …
                                          …
                                          …
                                          …
                                          22 222
~~~

## Page 58

~~~text
Tableaux et pointeurs
• Rappel : les valeurs d’un tableau sont à la suite dans la mémoire.
• Lorsqu’un tableau est déclaré:
   • Un espace mémoire de la bonne taille est réservé
   • Un pointeur constant (en lecture seule) portant le nom du tableau est crée.
    Il pointe sur la première case du tableau.
                                          Adresse       Valeur

                                 tab[0] 1154            1

                                 tab[1]                 3

  int main(){                    tab[2]                 0
    int tab[5]={1,3}
    return 0;                    tab[3]                 0

  }                              tab[4]                 0

                                          …
                                          …
                                          …
                                          …

                                  tab     22 222        1154
~~~

## Page 59

~~~text
 Tableaux et pointeurs
• Rappel : les valeurs d’un tableau sont à la suite dans la mémoire.
• Lorsqu’un tableau est déclaré:
   • Un espace mémoire de la bonne taille est réservé
   • Un pointeur constant (en lecture seule) portant le nom du tableau est crée.
    Il pointe sur la première case du tableau.

• Manipuler un tableau revient à utiliser un pointeur. On accéde à ses élément par
  adresse.

• On a l’équivalence suivante :
                                  tab[i] ⇔ *(tab+i)
~~~

## Page 60

~~~text
Tableaux et pointeurs
• On a l’équivalence suivante :
                          tab[i] ⇔ *(tab+i)
• Illustration :
                                        Adresse     Valeur

                              tab[0] 1154 = tab+0   1
                                                    3

                                                    0

                                                    0

                                                    0

                                        …
                                        …
                                        …
                                        …
                                  tab   22 222      1154
~~~

## Page 61

~~~text
Tableaux et pointeurs
• La manipulation d’un tableau peut donc se faire en formalisme tableau (avec les
  caractères [ ]) ou en formalisme pointeur.


                                               #define TAILLE 20
       #define TAILLE 20                       int main(){
       int main(){                               int i;
         int i;
         int tab[TAILLE]={0};                   int tab[TAILLE]={0};
                                                 for(i=0;i<TAILLE;i++){
         for(i=0;i<TAILLE;i++){                       *(tab+i)=10;
              tab[i]=10;                         }
         }                                       return 0;
         return 0;                             }
       }
~~~

## Page 62

~~~text
Tableaux et pointeurs
• Exercice : quel résultat donne les commandes en rouges ?
                                                       Adresse   Valeur

    #define TAILLE 20
    int main(){                                        1154
       int tab1[TAILLE]={0};
       int tab2[TAILLE]={0};
       for(int i=0;i<TAILLE;i++){                      …
            tab1[i]=i;
                                                       5340
          }
        tab2=tab1;
        tab2[10]=0;
        return 0;                                      …
    }                                                  …
                                                       …
                                                       22 222
                                                       …
                                                       30 000
~~~

## Page 63

~~~text
 Tableaux et pointeurs
• Exercice : quel résultat donne les commandes en rouges ?
                                                                  Adresse   Valeur

      #define TAILLE 20
      int main(){                                                 1154
         int tab1[TAILLE]={0};
         int tab2[TAILLE]={0};
         for(int i=0;i<TAILLE;i++){                               …
              tab1[i]=i;
                                                                  5340
            }
          tab2=tab1;
          tab2[10]=0;
          return 0;                                               …
      }                                                           …
                                                                  …
                                                                  22 222
On égalise les pointeurs et donc tab2= adresse de tab1[0]
                                                                  …
tab2 pointe sur le 1 er tableau -> le second tableau n’est plus
                                                                  30 000
accessible.
~~~

## Page 64

~~~text
 Tableaux et pointeurs

• Exercice : pourquoi écrit-on :
   • scanf("%c", &nom) pour un caractère ?
   • scanf("%s", nom) pour une chaîne de caractère ?
~~~

## Page 65

~~~text
  Tableaux et pointeurs

• Exercice : pourquoi écrit-on :
   • scanf("%c", &nom) pour un caractère ?
   • scanf("%s", nom) pour une chaîne de caractère ?



• Car une chaine de caractère est un tableau! « nom » est donc un pointeur (l’adresse)
  de la première case de la chaîne de caractère)
~~~

## Page 66

~~~text
 Tableaux, pointeurs et fonctions
• Le passage d’un tableau en paramètre d’une fonction se fait donc par adresse.
  On a l’équivalence:

             type nomFonction(int tab[], int taille …)




                                 ⇔
             type nomFonction(int *tab, int taille…)


• Un tableau, déclaré dans une fonction appelante et, passé en paramètre lors
  d'un appel, peut être modifié dans la fonction appelée.
• Cela permet donc à 2 fonctions (qui possèdent des contextes mémoires
  séparés) de partager un même espace mémoire.
~~~

## Page 67

~~~text
   Conclusion

• Un pointeur est une variable contenant une adresse. Il se déclare avec le type de la variable sur
  laquelle il pointe.

• Le caractère « * » associé au pointeur permet d’avoir accès à la variable pointé. On peut la modifier,
  l’afficher… On accéder alors à cette variable par adresse plutôt que pas son nom.

• Les utilités des pointeurs sont nombreuses: ils permettent de modifier par adresse des variable dans
  des fonctions ou sont à la base de la gestion des tableaux. Plus d’info au prochain cours!

• Il est important de comprendre le fonctionnement de la mémoire pour pouvoir utiliser correctement les
  pointeurs!
~~~
