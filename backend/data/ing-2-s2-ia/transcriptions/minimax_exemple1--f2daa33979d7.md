# minimax_exemple1.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14TwvU532DxATsv_rEdQC6sudJE5WPDb3) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Arbre de jeux
                                          A



                     B                                                    C




       D                      E                           F                         G




  H            I         J          K             L               M           N         O



10    11   9       12 14 15       13 14       5       2       4       1   3       22 20 21
~~~

## Page 2

~~~text
MINIMAX
                                           A 10



                       B 10                                             C 2




       D 10                    E    14                    F 2                       G 20



      10           9         14          13           2             1           3          20
  H            I         J           K            L             M           N         O



10    11   9       12 14 15        13 14      5       2    4        1   3       22 20 21
~~~

## Page 3

~~~text
MINIMAX- STRATEGIES
                                           A 10



                       B 10                                             C 2




       D 10                    E    14                    F 2                       G 20



      10           9         14          13           2             1           3          20
  H            I         J           K            L             M           N         O



10    11   9       12 14 15        13 14      5       2    4        1   3       22 20 21
~~~

## Page 4

~~~text
 Alpha-BETA - 1
                                           A



                      B                                                    C




        D                      E                           F                         G


=10
   H            I         J          K             L               M           N         O



10     11   9       12 14 15       13 14       5       2       4       1   3       22 20 21
~~~

## Page 5

~~~text
 Alpha-BETA - 2
                                           A



                      B                                                    C




 =10    D                      E                           F                         G


=10             <10
   H            I         J          K             L               M           N         O



10     11   9       12 14 15       13 14       5       2       4       1   3       22 20 21
~~~

## Page 6

~~~text
 Alpha-BETA - 3
                                          A


            =10       B                                                   C




 =10    D                 >10 E                           F                         G


=10             <10            >10
   H            I          J         K            L               M           N         O



10     11   9       12 14 15      13 14       5       2       4       1   3       22 20 21
~~~

## Page 7

~~~text
 Alpha-BETA - 4
                                     =10 A


            =10       B                                      <10         C




 =10    D                 >10 E              <10         F                         G


=10             <10                       <10            <10
                               >10
   H            I          J          K          L               M           N         O



10     11   9       12 14 15      13 14      5       2       4       1   3       22 20 21
~~~
