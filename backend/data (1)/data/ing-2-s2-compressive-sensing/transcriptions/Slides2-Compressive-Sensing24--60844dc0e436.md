# Slides2-Compressive-Sensing24.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1pedoDqDl8J6D3hGesIprBt4tIgWGrxZc) · Les deux lectures automatiques du PDF divergent sur les pages indiquées. Leur fac-similé accompagne le texte.

**Pages présentant un écart entre les deux extractions** — 7–9, 13–21, 24–27, 29–36, 38–40, 43–44, 48–52, 56–59, 61, 63–69, 71.

## Page 1

~~~text
                        Introduction
                  Relaxation convexe
   Algorithmes gloutons MP et OMP




          Compressive Sensing
CM2 : Algorithmes de codage parcimonieux

                              CY TECH


                              2022-2023




                          CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 2

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP




1   Introduction


2   Relaxation convexe


3   Algorithmes gloutons MP et OMP




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 3

~~~text
                     Introduction
               Relaxation convexe
Algorithmes gloutons MP et OMP




                          Section 1

                       Introduction




                       CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 4

~~~text
                              Introduction
                        Relaxation convexe
         Algorithmes gloutons MP et OMP


Rappel




                                CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 5

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel


   • On sait que notre signal x possède une représentation α, avec
     très peu de composantes non nulles, dans un dictionnaire D.
     Autrement dit : x = Dα.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 6

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel


   • On sait que notre signal x possède une représentation α, avec
     très peu de composantes non nulles, dans un dictionnaire D.
     Autrement dit : x = Dα.
   • Mais le dictionnaire D est redondant avec beaucoup de
     colonnes.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 7

![Page 7 du PDF](../facsimiles/4978b45622789497cc63973a.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel


   • On sait que notre signal x possède une représentation α, avec
     très peu de composantes non nulles, dans un dictionnaire D.
     Autrement dit : x = Dα.
   • Mais le dictionnaire D est redondant avec beaucoup de
     colonnes.
   • Le système linéaire x = Dα, possède donc une infinité de
     solutions α.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 8

![Page 8 du PDF](../facsimiles/8d739b25ad395937d722cb06.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel


   • On sait que notre signal x possède une représentation α, avec
     très peu de composantes non nulles, dans un dictionnaire D.
     Autrement dit : x = Dα.
   • Mais le dictionnaire D est redondant avec beaucoup de
     colonnes.
   • Le système linéaire x = Dα, possède donc une infinité de
     solutions α.
   • Nous devons donc reformuler notre problème, avec comme
     objectif la parcimonie.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 9

![Page 9 du PDF](../facsimiles/8d739b25ad395937d722cb06.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel


   • On sait que notre signal x possède une représentation α, avec
     très peu de composantes non nulles, dans un dictionnaire D.
     Autrement dit : x = Dα.
   • Mais le dictionnaire D est redondant avec beaucoup de
     colonnes.
   • Le système linéaire x = Dα, possède donc une infinité de
     solutions α.
   • Nous devons donc reformuler notre problème, avec comme
     objectif la parcimonie.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 10

~~~text
                               Introduction
                         Relaxation convexe
          Algorithmes gloutons MP et OMP


Reformulation




                                 CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 11

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 12

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 13

![Page 13 du PDF](../facsimiles/05b5b6c77855a46c6ef002e7.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 14

![Page 14 du PDF](../facsimiles/fe08b4728f0e486c309f457c.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 15

![Page 15 du PDF](../facsimiles/207e2fa8605bc82e6d582604.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 16

![Page 16 du PDF](../facsimiles/c38ffdb98b6ea7030a2d744c.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 
      Plusieurs techniques sont utilisées pour le résoudre :




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 17

![Page 17 du PDF](../facsimiles/745244e243b39e3b96bd9330.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 
      Plusieurs techniques sont utilisées pour le résoudre :
      Relaxation convexe,




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 18

![Page 18 du PDF](../facsimiles/9ee01b663b8242766a3b3622.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 
      Plusieurs techniques sont utilisées pour le résoudre :
      Relaxation convexe, utilisant l’optimisation linéaire,




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 19

![Page 19 du PDF](../facsimiles/2220a21a6e5ec5e5f2c6b647.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 
      Plusieurs techniques sont utilisées pour le résoudre :
      Relaxation convexe, utilisant l’optimisation linéaire, ou la
      méthode LASSO.




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 20

![Page 20 du PDF](../facsimiles/25b1901396887c975329f43d.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 
      Plusieurs techniques sont utilisées pour le résoudre :
      Relaxation convexe, utilisant l’optimisation linéaire, ou la
      méthode LASSO.
      Algorithmes de poursuite gloutonne :



                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 21

![Page 21 du PDF](../facsimiles/ce03c52807c3cf4d3145c0b3.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Reformulation

  Nous introduisons la pseudo-norme kαk0 égale au nombre de
  composantes non nulles de α.
      Le problème devient alors
                        min kαk0 sous contrainte Dα = x
      En tenant compte du bruit, ce problème devient :
                   min kαk0 sous contrainte kx − Dαk2 ⩽ 
      Plusieurs techniques sont utilisées pour le résoudre :
      Relaxation convexe, utilisant l’optimisation linéaire, ou la
      méthode LASSO.
      Algorithmes de poursuite gloutonne : MP et OMP en
      particulier.


                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 22

~~~text
                     Introduction
               Relaxation convexe
Algorithmes gloutons MP et OMP




                          Section 2

                Relaxation convexe




                       CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 23

~~~text
                               Introduction
                         Relaxation convexe
          Algorithmes gloutons MP et OMP


Relaxation convexe




                                 CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 24

![Page 24 du PDF](../facsimiles/c92b3b56a826760a99c2d070.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Relaxation convexe



     La difficulté à manier la pseudo-norme k.k0 nous oblige à la
     remplacer par une norme k.kp avec p ⩾ 1.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 25

![Page 25 du PDF](../facsimiles/5521d521d1cccc4e4bce431c.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Relaxation convexe



     La difficulté à manier la pseudo-norme k.k0 nous oblige à la
     remplacer par une norme k.kp avec p ⩾ 1.
     On obtient alors un problème d’optimisation convexe :
                       min kαkp sous contrainte Dα = x




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 26

![Page 26 du PDF](../facsimiles/00081844a1f7ff72292745cd.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Relaxation convexe



     La difficulté à manier la pseudo-norme k.k0 nous oblige à la
     remplacer par une norme k.kp avec p ⩾ 1.
     On obtient alors un problème d’optimisation convexe :
                   min kαkp sous contrainte Dα = x
               ou min kαkp sous contrainte kx − Dαk2 ⩽ 




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 27

![Page 27 du PDF](../facsimiles/38900b6e917736bb1b286c7c.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Relaxation convexe



     La difficulté à manier la pseudo-norme k.k0 nous oblige à la
     remplacer par une norme k.kp avec p ⩾ 1.
     On obtient alors un problème d’optimisation convexe :
                   min kαkp sous contrainte Dα = x
               ou min kαkp sous contrainte kx − Dαk2 ⩽ 
     On dispose dans cette situation de différentes méthodes
     d’optimisation convexe pour le résoudre.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 28

~~~text
                               Introduction
                         Relaxation convexe
          Algorithmes gloutons MP et OMP


Rappel de quelques méthodes




                                 CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 29

![Page 29 du PDF](../facsimiles/5824890bcae5da223e90d893.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 30

![Page 30 du PDF](../facsimiles/c22732bb38fabddc94ba444f.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 31

![Page 31 du PDF](../facsimiles/5a8146ce675b99dd6488697c.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x
     Avec la régression RIDGE, on obtient :




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 32

![Page 32 du PDF](../facsimiles/01a3429c212c66cea6ca6eb6.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x
     Avec la régression RIDGE, on obtient :
     α∗ = arg min kx−Dαk22 +λkαk22 =⇒




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 33

![Page 33 du PDF](../facsimiles/ddbe5b238bf1c449b9e49628.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x
     Avec la régression RIDGE, on obtient :
     α∗ = arg min kx−Dαk22 +λkαk22 =⇒ α∗ = (D T D+λIk )−1 D T x




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 34

![Page 34 du PDF](../facsimiles/704ee05a69eb0e00a1ac9740.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x
     Avec la régression RIDGE, on obtient :
     α∗ = arg min kx−Dαk22 +λkαk22 =⇒ α∗ = (D T D+λIk )−1 D T x
     La méthode LASSO quant à elle revient à :




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 35

![Page 35 du PDF](../facsimiles/2dc5835d24480f85ff4bb755.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x
     Avec la régression RIDGE, on obtient :
     α∗ = arg min kx−Dαk22 +λkαk22 =⇒ α∗ = (D T D+λIk )−1 D T x
     La méthode LASSO quant à elle revient à :
                      α∗ = arg min 21 kx − Dαk22 + λkαk1




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 36

![Page 36 du PDF](../facsimiles/2cbe8b2a8c59723b005a9ff9.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Rappel de quelques méthodes


     On sait résoudre le problème aux moindres carrés :
          α∗ = arg min kx − Dαk22 =⇒ α∗ = (D T D)−1 D T x
     Avec la régression RIDGE, on obtient :
     α∗ = arg min kx−Dαk22 +λkαk22 =⇒ α∗ = (D T D+λIk )−1 D T x
     La méthode LASSO quant à elle revient à :
                      α∗ = arg min 21 kx − Dαk22 + λkαk1
     Le choix de la norme 1, pour α, est le plus judicieux, comme
     on va le voir.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 37

~~~text
                               Introduction
                         Relaxation convexe
          Algorithmes gloutons MP et OMP


Choix de la norme 1




                                 CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 38

![Page 38 du PDF](../facsimiles/94f321ff60fd27159e45d3ca.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Choix de la norme 1

     Revenons à notre problème sans bruit :
                       min kαkp sous contrainte Dα = x




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 39

![Page 39 du PDF](../facsimiles/4123605ec85fc0bbdf31cf73.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Choix de la norme 1

     Revenons à notre problème sans bruit :
                       min kαkp sous contrainte Dα = x
     Géométriquement, cela revient à chercher, dans un
     sous-espace affine, celui des solutions de Dα = x, le vecteur le
     plus proche de l’origine, pour la norme p.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 40

![Page 40 du PDF](../facsimiles/4597778ddc53f7dd136a278b.webp)

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Choix de la norme 1

     Revenons à notre problème sans bruit :
                       min kαkp sous contrainte Dα = x
     Géométriquement, cela revient à chercher, dans un
     sous-espace affine, celui des solutions de Dα = x, le vecteur le
     plus proche de l’origine, pour la norme p.




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 41

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Choix de la norme 1

     Revenons à notre problème sans bruit :
                       min kαkp sous contrainte Dα = x
     Géométriquement, cela revient à chercher, dans un
     sous-espace affine, celui des solutions de Dα = x, le vecteur le
     plus proche de l’origine, pour la norme p.




     Parmi les normes convexes, c’est bien la 1 qu’il faut retenir.
     C’est celle qui donne des solutions parcimonieuses (avec des
     composantes nulles).
                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 42

~~~text
                                Introduction
                          Relaxation convexe
           Algorithmes gloutons MP et OMP


Optimisation linéaire




                                  CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 43

![Page 43 du PDF](../facsimiles/7474678111e8fd7ec9803382.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Optimisation linéaire

  Autre méthode, avec le choix de la norme 1 : écrire min kαkp sous
  contrainte Dα = x comme un problème d’optimisation linéaire :




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 44

![Page 44 du PDF](../facsimiles/0bf38d831b0a0330cf413eae.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Optimisation linéaire

  Autre méthode, avec le choix de la norme 1 : écrire min kαkp sous
  contrainte Dα = x comme un problème d’optimisation linéaire :




  Et lui appliquer la méthode du simplexe vue l’année dernière.

                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 45

~~~text
                     Introduction
               Relaxation convexe
Algorithmes gloutons MP et OMP




                          Section 3

Algorithmes gloutons MP et OMP




                       CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 46

~~~text
                               Introduction
                         Relaxation convexe
          Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)




                                 CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 47

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)


  Puisque le but est d’écrire x comme combinaison linéaire des
  atomes : x = α1 d1 + ... + αk dk , avec le moins de coefs αj 6= 0,




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 48

![Page 48 du PDF](../facsimiles/8d19d5417d1980ecdf1b5882.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)


  Puisque le but est d’écrire x comme combinaison linéaire des
  atomes : x = α1 d1 + ... + αk dk , avec le moins de coefs αj 6= 0, les
  méthodes de la poursuite adaptative consistent à :




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 49

![Page 49 du PDF](../facsimiles/8cc97c57903fbdad07346ed5.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)


  Puisque le but est d’écrire x comme combinaison linéaire des
  atomes : x = α1 d1 + ... + αk dk , avec le moins de coefs αj 6= 0, les
  méthodes de la poursuite adaptative consistent à :
    1   Trouver, itérativement, dans le dictionnaire D, l’atome le plus
        corrélé avec le signal,




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 50

![Page 50 du PDF](../facsimiles/0b9db523933b6a78819f4bfe.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)


  Puisque le but est d’écrire x comme combinaison linéaire des
  atomes : x = α1 d1 + ... + αk dk , avec le moins de coefs αj 6= 0, les
  méthodes de la poursuite adaptative consistent à :
    1   Trouver, itérativement, dans le dictionnaire D, l’atome le plus
        corrélé avec le signal,
    2   Ôter la contribution de cet atome au signal, et regarder le
        résidu,




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 51

![Page 51 du PDF](../facsimiles/ba0cf43e623f2ac4345bc847.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)


  Puisque le but est d’écrire x comme combinaison linéaire des
  atomes : x = α1 d1 + ... + αk dk , avec le moins de coefs αj 6= 0, les
  méthodes de la poursuite adaptative consistent à :
    1   Trouver, itérativement, dans le dictionnaire D, l’atome le plus
        corrélé avec le signal,
    2   Ôter la contribution de cet atome au signal, et regarder le
        résidu,
    3   Tant que le résidu n’est pas assez faible, recommencer le
        processus jusqu’au critère d’arrêt.




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 52

![Page 52 du PDF](../facsimiles/ba0cf43e623f2ac4345bc847.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe du MP(Matching Pursuit)


  Puisque le but est d’écrire x comme combinaison linéaire des
  atomes : x = α1 d1 + ... + αk dk , avec le moins de coefs αj 6= 0, les
  méthodes de la poursuite adaptative consistent à :
    1   Trouver, itérativement, dans le dictionnaire D, l’atome le plus
        corrélé avec le signal,
    2   Ôter la contribution de cet atome au signal, et regarder le
        résidu,
    3   Tant que le résidu n’est pas assez faible, recommencer le
        processus jusqu’au critère d’arrêt.




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 53

~~~text
                              Introduction
                        Relaxation convexe
         Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)




                                CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 54

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)


   1   On initialise x = 0 + R (0) .




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 55

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)


   1   On initialise x = 0 + R (0) .
   2   A l’étape k, on a : x = zm1 dm1 + ... + zmk dmk + R (k) .




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 56

![Page 56 du PDF](../facsimiles/35bf172ecf7b95ae54645826.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)


   1   On initialise x = 0 + R (0) .
   2   A l’étape k, on a : x = zm1 dm1 + ... + zmk dmk + R (k) .
   3   A chaque étape, on repère l’atome sur lequel la projection du
       résidu R (k) est la plus importante. Ce sera la direction dm qui
       contribue le plus à ce résidu.




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 57

![Page 57 du PDF](../facsimiles/b940d52591c805e91ef2f42a.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)


   1   On initialise x = 0 + R (0) .
   2   A l’étape k, on a : x = zm1 dm1 + ... + zmk dmk + R (k) .
   3   A chaque étape, on repère l’atome sur lequel la projection du
       résidu R (k) est la plus importante. Ce sera la direction dm qui
       contribue le plus à ce résidu.
   4   On calcule la contribution zm de cet atome à R (k) .




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 58

![Page 58 du PDF](../facsimiles/fdace55219226e3305cc2156.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)


   1   On initialise x = 0 + R (0) .
   2   A l’étape k, on a : x = zm1 dm1 + ... + zmk dmk + R (k) .
   3   A chaque étape, on repère l’atome sur lequel la projection du
       résidu R (k) est la plus importante. Ce sera la direction dm qui
       contribue le plus à ce résidu.
   4   On calcule la contribution zm de cet atome à R (k) .
   5   On actualise la représentation α en ajoutant zm , puis
       R (k+1) = R (k) − zm dm .




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 59

![Page 59 du PDF](../facsimiles/857f4318b9f1be942171202e.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Etapes du MP(Matching Pursuit)


   1   On initialise x = 0 + R (0) .
   2   A l’étape k, on a : x = zm1 dm1 + ... + zmk dmk + R (k) .
   3   A chaque étape, on repère l’atome sur lequel la projection du
       résidu R (k) est la plus importante. Ce sera la direction dm qui
       contribue le plus à ce résidu.
   4   On calcule la contribution zm de cet atome à R (k) .
   5   On actualise la représentation α en ajoutant zm , puis
       R (k+1) = R (k) − zm dm .
   6   On s’arrête dès que kR (k) k < .



                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 60

~~~text
                              Introduction
                        Relaxation convexe
         Algorithmes gloutons MP et OMP


Algorithme MP




                                CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 61

![Page 61 du PDF](../facsimiles/b1d1c28ed814257a35f055e5.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Algorithme MP
  Entrées : x signal, D dico, ε (précision), N max itérations,
  Sorties : α (représ. parcimonieuse), R résidu, k nombre itérations

                                   α←0
                                   R←x
                                   k ←0
                         Tant que kRk > ε et k < N
                                                     |d T R|
                                 m ← argmax kdj j k2
                                        1⩽j⩽n
                                            TR
                                           dm
                                      z ← kd    2
                                             m k2
                                     αm ← αm + z
                                     R ← R − zdm
                                       k ←k +1
                                     Fin Tant que

                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 62

~~~text
                               Introduction
                         Relaxation convexe
          Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)




                                 CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 63

![Page 63 du PDF](../facsimiles/4c61c027bf4be5e023e75426.webp)

~~~text
                                 Introduction
                           Relaxation convexe
            Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.




                                   CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 64

![Page 64 du PDF](../facsimiles/5f5c1fa598a840908cfb1a13.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.
  Pour y remédier, on va faire en sorte que le résidu soit toujours
  orthogonal aux directions sélectionnées précédemment.




                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 65

![Page 65 du PDF](../facsimiles/057934ed75c9687c945a6622.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.
  Pour y remédier, on va faire en sorte que le résidu soit toujours
  orthogonal aux directions sélectionnées précédemment.
    1   Le début est le même que pour MP, tout comme la sélection
        d’une nouvelle direction.




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 66

![Page 66 du PDF](../facsimiles/2f476d7600a27188b579c0e4.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.
  Pour y remédier, on va faire en sorte que le résidu soit toujours
  orthogonal aux directions sélectionnées précédemment.
    1   Le début est le même que pour MP, tout comme la sélection
        d’une nouvelle direction.
    2   A chaque étape, on repère l’atome sur lequel la projection du
        résidu R (k) est la plus importante.




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 67

![Page 67 du PDF](../facsimiles/33e74e3b953b3112e9939671.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.
  Pour y remédier, on va faire en sorte que le résidu soit toujours
  orthogonal aux directions sélectionnées précédemment.
    1   Le début est le même que pour MP, tout comme la sélection
        d’une nouvelle direction.
    2   A chaque étape, on repère l’atome sur lequel la projection du
        résidu R (k) est la plus importante.
    3   Mais ensuite, on recalcule les contributions de tous les atomes
        sélectionnés à x, en résolvant un pb. aux moindres carrés.




                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 68

![Page 68 du PDF](../facsimiles/b74826067092bcdd99917ae4.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.
  Pour y remédier, on va faire en sorte que le résidu soit toujours
  orthogonal aux directions sélectionnées précédemment.
    1   Le début est le même que pour MP, tout comme la sélection
        d’une nouvelle direction.
    2   A chaque étape, on repère l’atome sur lequel la projection du
        résidu R (k) est la plus importante.
    3   Mais ensuite, on recalcule les contributions de tous les atomes
        sélectionnés à x, en résolvant un pb. aux moindres carrés.
    4   On actualise alors la représentation α, puis le résidu R (k+1) .



                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 69

![Page 69 du PDF](../facsimiles/37b210c1a64347a6e810987b.webp)

~~~text
                                   Introduction
                             Relaxation convexe
              Algorithmes gloutons MP et OMP


Principe de l’OMP(Orthogonal Matching Pursuit)

  MP converge exponentiellement et a un grand défaut, un même
  atome peut être sélectionné plusieurs fois.
  Pour y remédier, on va faire en sorte que le résidu soit toujours
  orthogonal aux directions sélectionnées précédemment.
    1   Le début est le même que pour MP, tout comme la sélection
        d’une nouvelle direction.
    2   A chaque étape, on repère l’atome sur lequel la projection du
        résidu R (k) est la plus importante.
    3   Mais ensuite, on recalcule les contributions de tous les atomes
        sélectionnés à x, en résolvant un pb. aux moindres carrés.
    4   On actualise alors la représentation α, puis le résidu R (k+1) .
    5   On s’arrête dès que kR (k) k < .

                                     CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 70

~~~text
                              Introduction
                        Relaxation convexe
         Algorithmes gloutons MP et OMP


Algorithme OMP




                                CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~

## Page 71

![Page 71 du PDF](../facsimiles/d0bf45255ef4c8ac4ec35d40.webp)

~~~text
                                  Introduction
                            Relaxation convexe
             Algorithmes gloutons MP et OMP


Algorithme OMP

  Entrées : x signal, D dico, ε (précision), N max itérations,
  Sorties : α, R, k, Index : indices atomes retenus

            α←0         R ← x Index ← [ ] k ← 0 A ← [ ]
                        Tant que kRk > ε et k < N
                                                     dT R
                                  m ← argmax kdj j k2
                                            1⩽j⩽n
                                 Index ← [Index, m]
                                    A ← [A, dm ]
                                 αIndex ← pinv (A)x
                                  R ← x − AαIndex
                                     k ←k +1
                                   Fin Tant que


                                    CY TECH      Compressive Sensing CM2 : Algorithmes de codage parcimonie
~~~
