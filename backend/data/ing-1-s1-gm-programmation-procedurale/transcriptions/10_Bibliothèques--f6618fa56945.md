# 10_Bibliothèques.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1yLYElXt-0pQTERsmL1W3zEgm1cHjZw3p) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                           v1.00




PROGRAMMATION
PROCEDURALE
1 0. B I B LIOTHEQ UES
_ _ S TAT I Q U E S
__ DYNAMIQUES




                                                                               1
                         Eva ANSERMIN & Romuald GRIGNON
                                                          E. ANSERMIN | R. GRIGNON
~~~

## Page 2

~~~text
Bibliothèques         Headers
  • Fichiers d’entête :
     • Prototypes des fonctions
     • Constantes
     • Types
  • Bibliothèques :
     • Code compilé des fonctions
     • Statique ou Dynamique (cf. diapositives suivantes)

  • Permet le regroupement d’un ensemble de fonctions traitant du même sujet
     • Trigonométrie
     • Entrées / Sorties
     • Calcul Matriciel
     • Tris de données
     • Listes chainées
     • …                                                                                   2
                                                                      E. ANSERMIN | R. GRIGNON
~~~

## Page 3

~~~text
Bibliothèques statiques
  • Le code des fonctions de la bibliothèque est inclus dans l’exécutable

  • Permet d’exécuter le programme sur n’importe quel système
     • (un système qui ne possèderait pas la bibliothèque utilisée)

  • Produit un exécutable de taille plus importante
     • Tout le code utile est stocké dans l’exécutable

  • Utile pour :
     • des fonctions très particulières (spécificité de la bibliothèque)
     • conserver la propriété intellectuelle


                                                                                                 3
                                                                            E. ANSERMIN | R. GRIGNON
~~~

## Page 4

~~~text
Bibliothèques dynamiques
  • Le code des fonctions de la bibliothèque n’est pas inclus dans l’exécutable

  • Chargement de la bibliothèque à l’exécution
     • si le système ne l’a pas déjà chargée en mémoire
     • nécessite de posséder cette bibliothèque dans le système

  • Produit un exécutable plus léger
     • le code de la bibliothèque se situe dans un autre fichier

  • Utile pour :
     • des fonctions très utilisées par plusieurs programmes
     • permet de factoriser la place occupée par ces fonctions

  • Protège un peu moins la propriété intellectuelle                                           4
                                                                          E. ANSERMIN | R. GRIGNON
~~~

## Page 5

~~~text
Bibliothèques statiques : création
   • Création d’un fichier objet comme toute partie de programme C

   • Utilisation de la commande ‘ar’

   • Se référer à la documentation de la commande ‘ar’ pour voir les
     différentes fonctionnalités de création

   • L’extension d’une bibliothèque statique est ‘.a’

   • Exemple :
         • ar r libromu.a <fichiers *.o>


                                                                                            5
                                                                       E. ANSERMIN | R. GRIGNON
~~~

## Page 6

~~~text
Bibliothèques dynamiques : création
  • Compilation des fichiers objet avec l’option –fPIC
     • Position Independent Code
     • permet de simplifier les liens avec les fonctions de la bibliothèque

  • Utilisation de la commande ‘gcc’ avec l’option ‘-shared’

  • L’extension d’une bibliothèque dynamique est ‘.so’
      • l’équivalent sur les systèmes windows est ‘.dll’

  • Exemple :
        • gcc -shared libromu.so <fichiers *.o>


                                                                                                   6
                                                                              E. ANSERMIN | R. GRIGNON
~~~

## Page 7

~~~text
Bibliothèques : utilisation

   • Faire référence aux bibliothèques à utiliser lors de la compilation de l’exécutable
      • Bibliothèques statiques     : gcc –L       <directories> -lromu -lxxx…
      • Bibliothèques dynamiques : gcc –Wl <directories> -lromu –lxxx…


   • Etre rigoureux sur le nommage et la référence des bibliothèques:
      • libxxx en minuscule lors de la création
      • –lxxx lors de la référence
      • xxx étant le nom donné à la bibliothèque



                                                                                                  7
                                                                             E. ANSERMIN | R. GRIGNON
~~~

## Page 8

~~~text
Conclusion

 • Les bibliothèques permettent de regrouper du code compilé pour être partagé

 • Bibliothèques statiques
    • Exécutable autonome : tout est embarqué
    • Nécessité de recompiler l’éxécutable à chaque modification de la bibliothèque
    • Utilisation pour des fonctions spécifiques
    • Propriété intellectuelle protégée (reverse-engineering complexe)

 • Bibliothèques dynamiques
    • Les exécutables sont plus petits (compilation rapide) mais incomplets
    • L’exécutable ne change pas à chaque modification de la bibliothèque
    • Utilisation pour des fonctions communes à pusieurs programmes
    • La propriété intellectuelle est un peu moins protégée                                   8
                                                                         E. ANSERMIN | R. GRIGNON
~~~
