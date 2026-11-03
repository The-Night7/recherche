# Fiche Franklin Scala.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1sOuLZPQqzHoUlwcaFrLaAZ9TwmsreZqI) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
           Types primitifs                                                            :        Int Double , Booleam , String
                                                                                                                      ,
                                                                                                                                                                                                                                                                                   =                       sous         classe                           de
                                                                                                                                                                                                                                                                                                                                                                    AngVal
            Declaration :                                                        val : constante , immuable                                                                     /var                               :    variable                         ,
                                                                                                                                                                                                                                                              mutable
           E if enscala                                                          val                                                                                            else
                                                                        :                      res           =
                                                                                                                       if (x) y)                                       v
                                                                                                                                                                                                                   y
           Fonction
                                              pures                     :
                                                                                     me
                                                                                           dépend que                                          de           ses
                                                                                                                                                                       paramètres d'entrée, retourne le même résultat pour les mêmes paramètres                                                                                                                                                                                                            ,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   me              modifie pas les données extérieure
                                                                                                                                                                                          counter
            def Square (X Int) Int                                                                                                                                          var                                                     0
                                                                                                *                                                                                                                           =
                                                      :                 :             =    X         X                =L           pure
                                                                                                                                                                            def increment () Int                                             :                        =           & counter                            +=        1                       =              impure                     car
                                                                                                                                                                                                                                                                                                                                                                                                               modifie                           une     valeur externe
           Inférence de type                                                 :
                                                                                     pas        besoin                        de               val
                                                                                                                                                                stringx-"x"                                                                                                         counter3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                -




                                                                                     suffit de mettre val X                                                 "x" ,           Scala recommait les types                                                                                         primitif.                                                  Évaluation standard                                                 :
                                                                                                                                                                                                                                                                                                                                                                                                                                                 valres                    =
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   (valx                                      =
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              retourne                  3
                                                                                                                                                        =
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             val                                      2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             y
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          =




           Récursivité                            :                                                                                                                                                                                                                                                                                          Éval                  paresseuse : Lazy
                                                                                                                                                                                                                                                                                                                                                                                     vol                                                                                                         x +
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         y3
                                                                                                         def fact (m Fut Inti
                                                                                                                                                                                                                                         (m (1)
                                                              terminale
                                                                                                                                                                                                                                                                                                                                                 Lazy val                                 n'est évalué                               qu'à la               première utilisation, une                                                                          fois calculé ilgarde
                                                                                                                                                        :
                                             Non                                      :
                                                                                                                                                                            :
                                                                                                                                                                                                                                                                                                                                                                                 :
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ,

                                                                                          etailrec                                                                                                                                                                                                                                           la même valeur                                            .       Exemple                   :
                                                                                                                                                                                                                                                                                                                                                                                                                                                     lazy val ex-h                                                                    printem ('Hello" (
                                         Terminale :                                      def fact (m Int                           :
                                                                                                                                                                            Ink) Int
                                                                                                                                                            ac :                               :
                                                                                                                                                                                                                                                                                                                                                     printem (ex)                                          14 domme : Hello
                                                                                                                                                                                                                                                                                                                                                                                                                                                              sava ?
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              3
                                                                                                                                                    ,


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      "ça                     ?
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "

                                                                                                                 if (n
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  va
                                                                                                                                           =
                                                                                                                                               0)           ac
                                                                                                                                                                                                                                                                                                                                                     primble (ex) / domme
                                                                                                                 else
                                                                                                                                                                                    *
                                                                                                                                                                                           ax)
                                                                                                                                                                                                                                                                                                                                                                                                                                     :
                                                                                                                                                                                                                                                                                                                                                                                                                                             ça          va    ?
                                                                                                                               fact (m-1                                ,       m
                                                                                                                                                                                                                                                                          Option [T]                                         :




                                                                                                                                                                                                                                                                              option                           représente                            une            valeur qui peut être                                             présente (Some (value))                                                          au                  absente (Nome) .
       structures de dommées :                                                                                                                                                                                                                                             Utilisée                                     éviter les                                           nulles
                                                                                                                                                                                                                                                                                                               pour                                          erreurs                              on
                                                                                                                                                                                                                                                                                                                                                                                                           exceptions .
       imples                    :
                                                  val                       tuple("Scala" 42 42 0
                                                                                           =
                                                                                                                                    ,               ,
                                                                                                                                                                  .




                                                                                                                                                                                                                                                                      Evaluation                                            des
                                                                                                                                                                                                                                                                                                                                                 paramètres
                                                                            1) affiche le 1oélément de tuple "Scala"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    (message
        printem (tuple                                                                                                                                                                                                                                                                                                                                                                        :



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "Debug') printen
                                                                  -



     Les    huples permettent de stocker plusieurs valeurs de types différents                                                                                                                                                                                            def log (level String                                              :                               ,       message : String)
                                                                                                                                                                                                                                                                                                                                                                                                               condition du if est respectée
                                                                                                                                                                                                                                                                                                                                                                                                                                                           :
                                                                                                                                                                                                                                                                                                                                                                                                                                                               Unitif (level                                          -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      =-




     dans        une                         seule structure                                   immuable                                                                                                                                                               message                                  ne       sera             évalué que                                      si           la




                                                                                                                                                                                                                                                              I
      Pattern matching                                              :
                                                                             =            Régles             :    couvrir tous les                          cas       possibles d'où la case                                                                       Passage de fonction                                                                             en
                                                                                                                                                                                                                                                                                                                                                                                 paramètres                          :



       val number                                                                                                                                                           est exécuté
                                                                                                                      premier pattern
                                                                                                                                                                                                                                                                                                                                                                                                                   Ful) Int f(f(x)
                                              3                                                                                                                       bum

                                                                                                                                                                                                                                                                      def applyTwice (f Int = Int
                                         =                                                      ordre:                                                                                                                                                                                                                                                                                                                           :
                                                                                                                                                                                                                                                                                                                                                                                                           a   :


                                                                        matchs
                                                                                                                                                                                                                                                                                                                                                     :                                            ,

                                                                                                                                               définie qu'une seule fois par pattern
      val    result                           number                                           unicité : variable
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    donne le double
                                     =




             Case                1           =    "Um"                                                                                                                                                                                                                val double                                        =
                                                                                                                                                                                                                                                                                                                                 (X Int) :                          =>           X
                                                                                                                                                                                                                                                                                                                                                                                         *
                                                                                                                                                                                                                                                                                                                                                                                              2                                      ici         double prend                            une
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         fonction Anonyme qui
                                                  "Deux"
             Case

             case- 1
                             2

                                                  "Autres"
                                                                                                                                                                                                                                                                      applyTwice (double 3) / donne 12                                   ,




     Classes et Objets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    abstraite sans paramètres




                                                                                                                                                                                                                                                                                                                                                                                                                                             I
                                                              :
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Classe
                                                      class Point                          (varx Int , vary                                                     Yml/G                                                                   Class                                                          case             class Point (X : Int , y :                                                                       Int) Trait                                        :


      simple                                                                                                      :                                         -
                                                                                                                                                                                                       case                                                           :


                                                                  def        more         (dx        :   Fut
                                                                                                                          ,   dy : Ful) : Unit &                                                                                                                                                      vol pr                     =        Point (1, 2)                                                                                                   trait                      Shape
                                                                             x    + =      dx
                                                                                                                                                                                                           ·



                                                                                                                                                                                                                   copy () pour copier                                             une                 classe                                                                                                                                                                  defarea                   :   Double                               3
                                                                                           dy                                                                                                                                                                                                                                            clason                              classe                    / true or false
                                                                  3y +                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Double) extemds                                   shape
                                                                                      =



                                                                                                                                                                                                                   equals                                                 même chose                                                                                                                                                                                                (val radius
                                                                                                                                                                                                                                                                                                                                                                     =
                                                                                                                                                                                                                                                     =>                                                                que                                                                                                                       class Circle                                                                         :


                                                                                                                                                                                                                                                                                                                                                                                 alors
                                                                                                                                                                                                           ·




                                                              3                                                                                                                                                                                                                                                                      (si l même
                                                                                                                                                                                                                                                                  Code de Hachage
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    *
                                                                                                                                                                                                                   hashcode
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               *
                                                                                                                                                                                                                                                 =>                                                                                                                                                                                                                                                                                               Math PI                          radius                   radius
                                                                                                                                                                                                                                                                                                                                                                                                                                                           def area                      :           Double
                                                                                                 Point (1 2)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          =




                                                                                                                                                                                                        (Aa modifier avec Overside) - Override def
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              .
                                                                                                                                                                                                       ·




                                                              val
                                                                                                                                                                                                                   tosting
                                                                                      new
                                                                            p
                                                                                                                                                                                          juste l'objet
                                                                                 =                                                 ,

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  toshing : St
                                                                                                                                                                                        -en          v        oi
                                                                                                                                                                                                       ·




 simple      :
                                                   eE
                                         Object Singefor                                                                                                                                       Companion Object
                                                                                                                                                                                                                                                                                                                                                                                                                                                     Case Object




                                                                                                                                                                                                                                                                                                                                                                                                                                                 I
                                                          def greet ()                     :   Unit              =
                                                                                                                       primtle ("singlefor")3 objet partageant le même                                                                                                                                nom
                                                                                                                                                                                                                                                                                                                   qu'une classe                         is      peut acceder aux membres privés                                                      Objet immuable et sérialisable                                                                                  .

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Principalement utilisé
                                                                                                                                                                                                                                                                                                                                                                                                                                                      pour représenter des constantes ou états.
                                                                                                                                                                                               class Person (val                                                  name :
                                                                                                                                                                                                                                                                                              String valage Int                  :
                                                                                                                                                                                                                                                                                                                                                             s'utilisepour lemethodedededemt
                         unique (pas de new/ et crée paresseusement
                                                                                                                                                                                                                                                                                                               ,
 Instance
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              2 collections
                                                                                                                                                                                           Object Person                                 &                                                                                                               pas         d'une instance
                                                                                                                                                                                                                                                                                                                                                                                                                   spécifique                         ++       :               Jusion de
 Pas de     constructeur                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          une
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      sea             d'une               collection : --Seg(2 3)
                                                                                                                                                                                                                                                                                                                                                                                                                                                               :
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               supprime                                                                                                                                     ,
                                                                                                                                                                                                                                                                                                                                                                                                                                                     -   >




                                                                                                                          constantes partagée                                                          def apply (name String                                                                     Ink) Person                                        Person (name
                                                                                                                                                                                                                                                                                                                                                                                         age
                 souvent des méthodes utilitaires
                                                                                                                                                                                                                                                                                  age
                                                                                                                                                                                                                                                     :                                        :                :
                                                                                                                                                                                                                                                                          ,                                                          =   new
Contient                                                                                                          ou
                                                                                                                                                                                                                                                                                                                                                                                     ,


                                                                                                                                                                                                       def              adult
                                                                                                                                                                                                                                         (age            :
                                                                                                                                                                                                                                                             Int)             :   Boolean                          =
                                                                                                                                                                                                                                                                                                                       age )
                                                                                                                                                                                                                                                                                                                                         =
                                                                                                                                                                                                                                                                                                                                                 183
                                                                                                                                                                                                   val
Collections
                                                                                                                                                                                                                        moi-Person
                                                                                                                                                                                                                                                              ("Moh" 22)
                                                                                                                                                                                        I printem (Person
                                                                                                                                                                                                                                                                                                                                                                                     table
                                                                                                                                                                                                                                                                                          ,


                                                                                                                                                                                                                                                 .       adult (moi                               .

                                                                                                                                                                                                                                                                                                      age)) I                        true                                                                                                                                                                                                                         valx                  =
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Seg(1               ,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            3)

         Modifiables après la création
      Mutables :                                                                                                                                     .

                                                                                                                                                                                                                                                                                                                                                                                                                                                     Tableau extremise et en                                                                                      domme

Immuables Inchangeables Toutes modifications produit
                                              :                                                          .
                                                                                                                                                                                                                                                 une                  nouvelle collection                                                            .                                                                                                                                                                                                                    List (1 , 2 , 3)
                                                                                                                                                                                                                                                                                                                                                                                     val
                                                                                                                                                                                                                                                                                                                                                                                                           buffer-ArrayBuffer (1                                                     ,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ,   3)
                                                                                          Vector


                                                                                                                                                                        I
                                             List ,
     Les
             Seq             :
                                                                    Array             ,                                                                                         Set :                                  Collections d'élements uniques                                                                                                                                buffer +   4              =



Les Set                  :               sat
                                                          ,
                                                                  hashset , freeset
                                                                                                                                                                                Val set                                                  Set (1                           ,
                                                                                                                                                                                                                                                                            2             3)                                                                                         printem (bugger) Array Buffer (1 , 2 3 , 4                                                                                   ,




                                                                                                                                                                                                                                                                                                                                                                         I
                                                                                                                                                                                                                            =                                                         ,


Les
       Map       :
                                         Map , hashMap s treeMap                                                                                                            val newset-set                                                                        +               4                                                                                                  Mutable                         Set et Map :
                                                                                                                                                                            printem (newset) Set (1, 2 ,3 , 4)                                                                                                                                                                                                                                       mutable Map))
                                                                                                                                                                                                                                                                                                                                                                                     mutable Sell o n                                                                          .




      ·immuables :
                                                                                                                                                                                                                                                                                                                                                                                                               .




                                                                                                                                                                                                                                                                                                                                                                                 Methodes                          get (ekm) et getorElse(elem Oppor                                                                      ,

                                                                                                                 liste chamée                                                                                           Structure de' - e valeur




                                                                                                                                                                        I
            nums-List (1 , 2 , 3)                                                              //                                                                            Map
 vol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              maß
                                                                                                                                                                                                   :
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Les


 val newmums-mums                                                                    :
                                                                                           4 /l ajout
                                                                                                      la Sin                                                                val                map-Map(-1 "6'12)                                                                  ,                                                                                                  val                   list          =               (1           to       1000) Holist                          .




 printen (remmums)                                                                         List (1 , 2 , 3 , 49
                                                                                                                                                                            vol newmap                                      -
                                                                                                                                                                                                                                        map          +
                                                                                                                                                                                                                                                                  ("(                     +
                                                                                                                                                                                                                                                                                                       3)                                                                        val                   parrall                       =           list par          .




                                                                                                                                                                            printen (newmap)                                                             /Kapla                                        1       "Dez, " 3)                                           *
                                                                                                                                                                                                                                                                                                                                                                                                                                  performances (tâches parra
                                                                                                                                                                                                                                                                                                  ~




                     pareil que List mais plus performants
                                                                                                                                                                                                                                                                                                           ,

Vector :                                                                                                                                                                                                                                                                                                                                                                                                             Améliorer                                                                               les
                                                                                                                                                                                                                                                                                                                                                                                                   Pourquoi ?
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                em
                                                                                                                                                                                                                                                                                                                                                                                                                                                       -


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 -

                                                                                                                                                                                                                                                                                                                                                                                                     facilité avec les fonctions pures + multicoeurs emus
     Parallélisme                                                                                                                              parallèles                                (map filter reducef avec
                                                                                                                                                                                                                                                                                                                                                                                                       -




                                                                        :                  Collections                                                                                                                  ,                    ,
                                                                                                                                                                                                                                                                                                                   ·
                                                                                                                                                                                                                                                                                                                       par




                                                                                                                                                                                                               I
                                                                                                                                   le temps de calals-                                                                                                                                                                                                                                        // Affiche les résultats
      Utilisation de System nanotime pour
                                                                                                                                                                                                                   Object Application
                                                                                 .




                                                                                                                                                                                                                                                                                                                                                                                                  totalWordsCount                                                          toSeq SorBy(- 1)foreach [
     Modèle Master-Worker                                                                                                                                                                                               def main (args Array (String]↑ Unit                                                                                                         f
                                                                                                                                                                                                                                                                                                                                                                                                                                                               .                         .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          -




                                                                                                                                                                                                                                                                                                                                                                                                                   (word, count => printem (s"$word : caunt") 3
                                                                                                                                                                                                                                                                                          :                                              :


     Rôles                                                                                                                                                                                                              Il Texte à analyser                                                                                                                                                       3.
                          tâches , collecte et combine  résultats                                                                                               les                                                                                                                                                                                                                                    1) Worker : Get pour                                                        compter les mots
     Master Distribue les
                     :
                                                                                                                                                                                                                        vol              text- "Scala c'est de la merete
                                                                                                                                                                                                                                                                                                                                                                                                       def          countwords (section :                                                                    Sting)                               Map [Sting Int]                                               =
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     E
                                                        de données
                                                                                                                                                                                                                                                                                                                                                             .

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              :                                         ,


     Workers Exécutent les tâches sur des sous-ensemble                                                                                                                                                                            cette matièredonc
                                                                                                                                                                                                                        nique Samere
                         :
                                                                                                                                                                                                                                                                                                                                                                                                               Section               .
                                                                                                                                                                                                                                                                                                                                                                                                                                         split("XW+ ") filter( mon Empfy map (itolowerCase)  .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -                               ·




     Propriétés                      :        fonctions pures + immuables                                                                                                                                                                le texte en sections                                                                                                                                                                             groupBy (identity) view mapValues (- length) toMap]
                                                                                                                                                                                                                       /1 Master divise
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ·
                                                                                                                                                                                                                                                                                                                                                                                                                                         .                                                               .                            .                                                                     ·




                                                                 Car                                                                                                                                                                                                                                                                                                                 trim) tolish
                                                                                                                                                                                                                                .




 Pas de problèmes                                                                                                                                                                                                      val sections = text split(" ") Map
                                                                                                                                                                                                                                                              (                                                                                                                                                                          // Master : Jusiommer 2 maps.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ) Map (shiny In
                                                                                                                                                                                                                                                                                                                                                                                 .                     :

                                                 de concurrences
                                                                                                                                                                                                                                                                                                                                                                                                                                                          (map1 Map[stig Int] maps
                                                                                                                                                                                                                                                                                                                                             .           .
                                                                                                                                                                                                                                                                                                       .




                                                                                                                                                                                                                                                                                                                                                                                                                                         def merge Counts                                                                                                 ,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ...         :                        ,

                                                                                                                                                                                                                                                                                          comptent les mots de chaque sections
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      :                                                   ,


                                                                                                                                                                                                                       1/2               Workers
                                         ("" ","                                                                                                                                                                                                                                                                                                                                                                                                     (map1 KeySet ++ mape Keysetf map &Key
                                                                                               les séparateurs
     Split(" +")                                                                                                                                                                               )
                                                                                                                                                                            "       "
                      supprime
                                                                                                                                                                                                                                                                                                                                                                     (countWords
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            >
                                                                                                                                                                                                                                    .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            -

                                                              =>


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            getOrffn)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      .


                                                                                                                                                                                ;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              .

                                                                                                                                                            ,
                                                                                                                                                                                                                                                                                                      Sections par
                                                                                                                                                                                                                                                                                                                                                                                                                                                                       .

                                                                                                                                                                        ,
 ·
                                                                                                                                                                                        ....


                                                                                                                                                                                                                       val wordCounts                                                 =                                      .                   ·

                                                                                                                                                                                                                                                                                                                                                     map
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      0) + map2
                                                                                                                                                                                                                                                                                                                                                                                                                                                          key (map1 getorElse (key
                                                                                                                                       "
     Split ("N ") =>         sur chaque"                                                                                                                                                                                                     les résultats
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        .




                                                                                                                                                                                                                                        Master

                                                                                                                                                                                                                                                                                                                                                                                                       (mergeCounts)
                                                                                                                                                                                                                                                                                                                                                                                                                                     -




                     divise                                                                                                                                                                                                        regroupe
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               -o
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ,
                                                                                                                                                                                                                       /3
 ·
                                                                                                                                .
                                     .
                                                                                                                                                                                                                                    .




                                                                                                                                                                                                                                                                                                                                                                                                                                                         3 toMaP
                                                                                                                                                                                                                                                                                                                                                                                                                                                         .
     Toujours mestring après un split                                                                                                                                                                                  val totalWord Count = WordCounts reduce                                                                                                       -
~~~

## Page 2

~~~text
                                                                                                                                                                                                                                                                  toMap                   tolist , to set....
                                                                                                                Collections
                                                                                                                                                              conversions                                                     to     tray                     ,                   ,

      Transformation
                                                                                                                                                                                                                  :
                                                                                              des

                                                                                                                                                                                                                                                                                                      nouvelle collection contenant les résultats.
      map                       :
                                                Applique une fonction à chaque élément d'une                                                                                                                collection pour
                                                                                                                                                                                                                                                      produire                            une



      val words-List ("Scala" , "is" ,                                                                              " great'                 flatMap            :               comme
                                                                                                                                                                                               map mais aplatit
                                                                                                                                                                                                                 les collections imbriquées                                                                                                          en   une        seule
                                                                                                                                                                                                                                                                                                                                                                                               mapValue (value        =
                                                                                                                                                                                                                                                                                                                                                                                                                                 transformation
           lengths       map ( longht)
                                                        words
                                                                                                                                                                                        List ("Hello Word" ," Scala c'est guez")
      val                                           =


                                                                                                                                            Val sentences                                                                                                                                                                                                                        mapValne (price                                     9)
                                                                          .


                                                                                                   _                                                                                                                                                                                                                                                                                                                     *
                                                                                                                                                                        =
                                                                                                                                                                                                                                                                                                                                                              prices                                        =
                                                                                                                                                                                                                                                                                                                                                                                                                 price       0

      printem (lenghs) / List (5
                                                                                                                                                                                                                                                                                                                                                                             .
                                                                                                                                                                                                                                                                                                                                                                                                                                 .




                                 5)
                                                                                                                                                                                                                                                                                                           split(""))
                                                                                                           2
                                                                                                       ,        ,
                                                                                                                                            ral     words     -         sentences                            .

                                                                                                                                                                                                                 FlatMap (sentences                                   =>         sentence


ifter
                                                                                                                                            printem(words)                                                  List /Hello , Word , Scala
                                                                                                                                                                                                                                                                                      ,
                                                                                                                                                                                                                                                                                          c'est,
                                                                                                                                                                                                                                                                                                       guez
                                                                                                                                            ici    Hello par exemple est devenu lui même                                                                          une           collection.
 refient uniquement les élements                                                                                     satisfaisant
  la condition
                                                                                                                                                                                                                              (pour calules progressifs
Vol nums                                    -
                                                    List (1 , 2 , 3 , 4 , 5
                                                                                                                                                           Gold Left                                         :
                                                                                                                                                                                                                                                                                                                                                                              fold right (pour récursivite)
Val                                                                   filter (% 2                                         o)
                                                                                                                                                                                                                                                                                                                                                                                      o
        evens                           =           mums          .                                                 = =




primben(evens)List (2, 44)                                                                                                                                                                              gopa
                                                                                                                                                                                            op




                                                                                                                                                                                                                                                                                                                                                                                                    on op
                                                                                                                                                                                                                                                                                                                                                                                                            op




                                                                                                                                                         an
                                                                                                                                                                                                                   a3


foreach
                                                                                                                                                                op



 Permet d'itérer                                                 sur                  chaqu élement
  d'une collection of executer une action
                                                                                                                                                         op   op
                                                                                                                                                                        (op (ac an)                     ,         , an ,
                                                                                                                                                                                                                              a                                                                                                    op(an oplas oplas  ,                  ,             ,
                                                                                                                                                                                                                                                                                                                                                                                               ac)
 Val nums-List (1 2 3)                                                            ,       ,                                                                                                                                                                    Syntaxe                    :
                                                                                                                                                                                                                                                                                                                                                                                                             as                       Acc
 mums           .


                        Joreach (printen)                                                      11                                                                                   Val result                            =   collection              .
                                                                                                                                                                                                                                                              Goldleft (initialValue) (Cac elem)                                    ,                     =       operation)
mums        .

                Joreach (s %                                                                                                                                                            Val             result            =   collection Gold
                                                                                                                                                                                                                                                                              Right (initialValue) ((elem acc =C operation)
                                                                  ) h
                                                                                                                                                                                                                                                          .




                                                                                                                                                                                                                                                                                                                                    ,

or(xx *
                                                                                                           9                                                                                                                                          Exemples                        :




Partition
                                                                                                                                                                                            Val words-List
                                                                                                                                                                                                                                                              ("Scala", "is"                           " great")
                                                                                                                                                                                                                                                                                                       ,



Divise                          une                     collection en 2 collections                                                                                                         val sentence                             --       words Gold Left (1) (Cacc, word) = acc + word
                                                                                                                                                                                                                                                                          .
                                                                                                                                                                                                                                                                                                                                                                                                         "1)
                            la
 selon
           relgle.                                                                                                                                                                      val reversed                            =         words                       -

                                                                                                                                                                                                                                                                              Goldheft ("") ((word                                               ,    acc > acc                                + word +      1111)
val (evens odds)                                                 =    mums                     .

                                                                                                   partition (% 2                 ==
                                                                                                                                       0)
                                                                                                                                                                                            sentence                                      Scala                                 great
                                    ,
                                                                                                                                                                                                                              /                                           is
evens/List (2)
odds                                List (1 3)
                                                                                                                                                                                            reversed
                                                            ,
                                                                                                                                                                                                                              /great is                                          Scala
groupBy
  Regrouper les éléments
                         selon une cle' définie
                                                                                                                                                          Méthodes                                           our          collection                              :

 par        une
                                    fonction                                                                                                                                                                                                                                                                                                                                                              d'une collection
                                                                                                                                                                                                                                                                                                                                minuscule                          tous          les       String
 val            grouped                                 =   mums              .

                                                                                      groupBy (- %
                                                                                                                     2 ==      of                         to UpperCase/Towercase                                                              :               Met en              majuscule                        ou
                                                                                                                                                                                                                                                                                                                                                                                                                 ou   variable
 printem (grouped) Map (false                                                                          --      List (1, 3) , truee List
                                                                                                                                            (12)
    et zip WithIndex
                                                                                                                                                         collect                                :
                                                                                                                                                                                                            Applique                 un       pattern matching pour transformer et filtrer      nouvelle                                                                                                              une
Zip
 zip    :           combine                                     deux                  collections        en
                                                                                                            paires
                                                                                              élèment avec sa position
                                                                                                                                                          nums                  .
                                                                                                                                                                                            collec                    &       Case        X
                                                                                                                                                                                                                                               ifx92               ***
                                                                                                                                                                                                                                                                        & /l donne List (4) liste !
                                                                                                                                                                                                                                                                                      =           0        =


zipWithIndex                                    :       combine                   un



                                                                                                                                                                                                calcule la somme d'éléments                                                                                                                                                                               1172+ 3- 6
Val chars-List ("a" , "b",
val
       zipped                               mums                Zip (chars
                                                                                      <"                                                                 sum :
                                                                                                                                                                                                                                                                                                           numériques                                                        nums sum      .




                                                                                                                                                                                            product 11x2x3 6              produit
                                    =                       .




                                                                                                                                                          Product :                                              Le                                                                       nums
                                                        ((19) (2 b) ) 2)
                                                                                                                                                                                                                                                                                                                                                                                               =
                                        List
                                                                                                                                                                                                                                                                                                           .




Zipped                                                                ,               ,            ,

ral indexed                                                                                                                                                                                             donne les résultats intermédiaires
                                                                                                                                                                      Right Même chose que le fold mais
                                                        chars ZipWithIndex
                                                                                                                                                         Scan  Left
                                            -                         .


                                                                                                                                                                        :                                        ou                               :
indexed                         =               List ((a
                                                                          ,       0) , (b , 1) , (4 ,                2))
                                                                                                                                                          numsScanLeft(0) (-+_)
                                                                                                                                                                            .   // List (0 1 3 6)                                                                                                                  .           ,        ,
                                                                                                                                                                                                                                                                                                                                                                                                        head Option
                                                                                                                                                                                                                                                                                                                               Lead                       /1                                   on
                                                                                                                                                         Lead                       :       donne                     le l'élément                                                                nums                     .




                                                                                                                                                                                                                                                                                                                                                                  List (2 3)
Gorall Vérifie si tous les élements satisfont
                        :
                                                                                                                                                         tail                                       donne bous
                                                                                                                                                                                                                                     sauf te ser                                                  nums                         Fait                   /                                ,




                                                                                                                                                     I
                                                                                                                                                                                                                                                                                                                       .


                                                                                                                                                                                    :


                                    la condition
                                                                                                                                                                                                                                                                                                                               imit                  / List (1 , 2
      mums                  .
                                Jorall (_70)                                                       / true
                                                                                                                                                         imit :                                 donne                     tous
                                                                                                                                                                                                                                      saufle dernier                                              mums

                                                                                                                                                                                                                                                                                                                                                                                                    on
                                                                                                                                                                                                                                                                                                                                                                                                           lastOption
                                                                                                                              élément                                                                                 le dernier                              élément                                                          last 3
                                                                                                                          1                              Post                               donne                                                                                                 nums
ists                                Vérifie                                               au moins
                                                                                                                                                                                                                                                                                                                           .


                                                                                                                                                                    :
                        :                                                 si

                                                                                                                                                                                                                                                                                                                                                                                               // List (1 , 2)
                                                                                                                                                         &




                                    Satisfait la condition                                                                                                                                                                                                                                                                                                        take (2)
                                                                                                                                                                                                                                                      premiers éléments
                                                                                                                                                                                                                                                                                                                                            mums
                                                                                                                                                                                                                               les
                                                                                                                                                                                                                                                                                                                                                                                                                                 dropwhile
                                                                                                                                                                                                                                                                                                                                                              .




                                                                                                                                                         take               :                   retourne                                  n
      nums                          exists ( >3)                                                   //false                                                                                                                                                                                                                                                        drop (2)                     //       List (3) on
                                                                                                                                                                                                                                                  premiers élément
                                .



                                                                                                                                                                                                                                                                                                                                            mums
                                                                 -                                                                                                                                                                                                                                                                                        .




                                                                                                                                                                                                                              les
                                                                                                                                                         drop                                Supprime                                 n



      Empty/nonempty vérifie si collection
                               la
                                                                                                                                                                        :

 is

                                                                                                                                                                                                                            (from until
                                                                                                                                                                                                                                                                                                                                                                             Slice (1 3) //
                                                                          :
                                                                                                                                                                                                                                                                                                                                                                                                             List (2 , 3)
                                                                                                                                                         Slice :                            Extrait une                       sous   collection                                slice                                                                      nums       .

                                                                                                                                                                                                                                                                                                                                                                                                ,

                                                                                      est              vide               on          mom
                                                                                                                                                                                                                                                                                                               ,




                                                                                                                                                                                            retourne nouvelle liste avecmenceeigie
                                                                                                                                                                                                                                                                                              a                                                                                                              List
                                                                                                                                                                                                                                                                                                                                                                                                                      (1 42 , 3)
mkSting                                             convertit                                               collection en chaime
                                                                                                                                                                                                                                                                                                                                                                  update(1 42)
                                                                                                                                                                                                                                                                                                                                                                                                                             ,
                                        :                                                 une                                                                                                                                                                                                                                                                                          ,
                                                                                                                                                         Update :                                                                                                                                                                            mums             .




                                                    avec              un
                                                                                          séparateur                                                                                                                                                                                                                                             position
  nums              .


                            MkString( ; 1) / 1 ;                                                                              2
                                                                                                                                  ;
                                                                                                                                      3
                                                                                                                                                         ted:                   retourne                          une         collection trié Leroissant)

                                                                                                                                  début et               reversed :                             inverse               l'ordre d'une collection
im Supprime les espaces
            :                                                                                                         au


                            à la                                                                                                                         min/max                                            donne te min                                              or         mas
                                                    Sim
                                                                                                                                                                                                    :




var     word=
                                                    "
                                                                Scala"                                                                                   Sindi                              retourne le 1e élément qui                                                                    satisfait une condition                                                                   nums            .


                                                                                                                                                                                                                                                                                                                                                                                                        find ( > 2) / Some (3)
word                    Krim                                                          "Scala"                                                                                                                                         élément est présent                                                                                        contains (2) //true
                                                                 "
                                                                                                                                                         Contains                                   Vérifie si                                                                                                                  nums
                .



                                                                                                                                                                                                                               un
                                                                                                                                                                                                                                                                                                                                             .


                                                                                                                                                                                        :



                                                                                                                          les combinaisons
combinations : return toutes                   distinct       supprime les doublons
                                                                                                                                                                                            :




possibles mums. combinations(2) / List(11) , List 22 3) List (1 35
                                        :
                                                                                                                                                                ,
                                                                                                                                                                            ,
                                                                                                                                                                                                             ,
~~~
