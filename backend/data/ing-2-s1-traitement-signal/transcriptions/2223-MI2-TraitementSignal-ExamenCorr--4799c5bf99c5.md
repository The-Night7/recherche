# 2223-MI2-TraitementSignal-ExamenCorr.pdf

[Ouvrir l’original](https://drive.google.com/open?id=14z6HdLmif30xMrk8w9WRQ6uQxTE1JAxL) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                                                    EXAMEN CORRECTION

                                                 Filière : ING2 MI
                                                 Matière : Traitement du Signal
                                                 Date : 16/12/2022          Durée : 2h
  Département de Mathématiques                   Responsable Cergy : HAJEJ Ahmed
  Année universitaire 2022-2023                  Responsables Pau : BARRAU Nelly ; DESPLAT Lucie

Exercice 1 [5 points] Questions du cours
Les réponses doivent être écrites sur votre copie (et non sur ce sujet).
Aucune justification n’est demandée. Toute erreur peut être sanctionnée de points négatifs.

  PARTIE I Vrai ou Faux ?
       1. L’échantillonnage d’un signal consiste à :
         (a) Prélever la valeur du signal à intervalles de temps réguliers.
         (b) Convertir les nombres binaires en tensions.
         (c) Convertir les valeurs du signal en nombres binaires.

       2. Considérons les trois signaux suivants

                       s1 (t) = cos(2πt),          s2 (t) = 1 + s21 (t),        s3 (t) = signe(s1 (t)).

         (a) s1 est un signal à temps continu et valeurs discrètes.
         (b) s1 est périodique de période 1.
         (c) s2 est périodique de période 1.
         (d) s3 est périodique de période 1 et à valeurs discrètes.

       3. Un signal numérique est un signal qui évolue, au cours du temps, de manière :
         (a) Continue.                                          (b) Discontinue.

  PARTIE II Question de cours
    Définissez la réponse impulsionnelle d’un système (filtre) à temps continu.


Exercice 2 [3 points] Calculer la transformée de Fourier de la fonction suivante
                                            
                                             1 + x si x ∈ [−1; 0]
                                    f (x) =   1 − x si x ∈ [0; 1]
                                                0     sinon
                                            

  La fonction f est dans L2 (R) et admet donc une transformée de Fourier. Il vient, pour ν ̸= 0 :
                                        Z +∞
                         F(f )(ν) =           f (t)e−2iπνt dt
                                        Z−∞
                                          0                     Z 1
                                    =       (1 + t)e−2iπνt dt +     (1 − t)e−2iπνt dt
                                            −1                        0

Traitons chaque intégrale séparément : on la divise en 2 :
                           Z 0                      Z 0               Z 0
                                        −2iπνt            −2iπνt
                               (1 + t)e        dt =     e        dt +     te−2iπνt dt
                             −1                        −1                  −1




                                                         1
~~~

## Page 2

~~~text
puis on effectue une intégration par partie (sur la 2eme intégrale) , il vient
                                        −2iπνt 0                                               !
               Z 0                                                 −2iπνt 0      Z 0    −2iπνt
                                                                          
                                         −e                      −e                  −e
                   (1 + t)e−2iπνt dt =                  +      t               −               dt
                −1                          2iπν     −1           2iπν      −1    −1  2iπν

On obtient donc
                                                                      e−2iπν
                               Z 0
                                                            i     1
                                     (1 + t)e−2iπνt dt =       + 2 2−
                                −1                         2πν  4π ν  4π 2 ν 2
Par un raisonnement analogue, on obtient pour l’autre intégrale :

                                                                    e−2iπν
                             Z 1
                                                        −i        1
                                 (1 − t)e−2iπνt dt =       + 2 2−
                               0                       2πν    4π ν  4π 2 ν 2
Finalement, on obtient
                                               sin2 (πν)
                                    F(f )(ν) =                      (⋆)
                                                  π2ν 2
                                            Z
Notons que si ν = 0, on doit alors calculer   f (t)dt qui vaut 1 (résultat cohérent avec l’expression (⋆) en
                                                 R
faisant tendre ν vers 0).


Exercice 3 [3 points] On rappelle que la fonction de Heaviside H et la fonction rampe R sont données par
                                   
                                      0 si t ≤ 0
                          H(t) =                                 R(t) = tH(t)
                                      1 si t > 0
   1. Montrer que la fonction rampe R définit une distribution.
      La fonction R est localement intégrable donc R définie bien un distribution.
   2. Déterminer R′ et R′′ au sens des distributions.
      Déterminons R′ : Pour tout φ ∈ D(R),
                                                                   Z +∞
                                       ′                       ′
                                 < R , φ >= − < R, φ >= −         R(t)φ′ (t)dt
                                                               −∞
                                      Z +∞                        Z +∞
                                             ′                +∞
                                 =−        tφ (t)dt = −[tφ(t)]0 +       φ(t)dt
                                       0                           0
                                   Z +∞
                                 =       φ(t)dt
                                    0
                                   Z +∞
                                 =       H(t)φ(t)dt.
                                       −∞

      La fonction de Heaviside H est localement intégrable donc elle définit une distribution régulière. On a
      donc pour tout φ ∈ D(R),
                                            < R′ , φ >=< H, φ > .
      La dérivée au sens des distribution de la fonction R est donc la fonction de Heaviside.
      Déterminons maintenant R′′ : Pour cela, il suffit de calculer H ′ . On a pour tout φ ∈ D(R),
                                                                  Z +∞
                                       ′                  ′
                                 < H , φ >= − < H, φ >= −                  H(t)φ′ (t)dt
                                                                    −∞
                                       Z +∞
                                 =−          φ′ (t)dt = −[φ(t)]+∞
                                                                0    = φ(0)
                                           0
                                 =< δ0 , φ > .

      La dérivée de la fonction de Heaviside est donc la distribution de Dirac en 0.

  Remarque. cet exercice a été traité dans le TD2 de Pau


                                                           2
~~~

## Page 3

~~~text
Exercice 4 [4 points] Considérons le système discret suivant :            y[n] = x[n] + x[n − 1]
   1. Déterminer la réponse en fréquence du système.
      En appliquant la transformée de Fourier en z à l’équation ci-dessus, on obtient

                                        Y (z) = X(z) + z −1 X(z) = (1 + z −1 )X(z)

      Donc H(z) = 1 + z −1 .
   2. Calculer la réponse impulsionnelle h[n] du système.

   3. Tracer le diagramme de Bode de h[n].

   4. Donner la bande passante à −3dB du système.

  Remarque. cet exercice a été traité dans le TD5 de Cergy


Exercice 5 [7 points] Soit un circuit formé d’un conducteur ohmique R et d’un condensateur de capacité C,
soumis à une tension sinusoïdale U e = Ue exp(jwt), avec j 2 = −1 :




                                                                             Us
   1. Déterminer la fonction de transfert H du filtre RC :       H(ω) =         .
                                                                             Ue
   2. On écrit la fonction de transfert de la façon suivante :
                                                                     ω
                                                                 j
                                                                     ωc
                                                    H(ω) =            ω
                                                               1+j
                                                                      ωc
      où ωc est la pulsation de coupure. Identifier ωc .
   3. Déduire la fréquence de coupure notée fc .
   4. Calculer le gain GdB en dB à la fréquence de coupure. On rappelle que GdB = 20log(| H |).
   5. Représenter le diagramme de Bode de ce filtre.
   6. Déduire la nature de ce filtre.

[Indication]
                                                                 dUc
   1. La relation courant tension pour un condensateur est : i = C   .
                                                                  dt
   2. En notation complexe, pour n’importe quel dipôle, on a U = ZI..
                                                                                     1
      Pour le conducteur ohmique Z R = R et pour le condensateur Z c =                  .
                                                                                    jCω
   3. Le diagramme de Bode d’un filtre se compose de deux tracés :


                                                           3
~~~

## Page 4

~~~text
— Le gain en décibels (dB) en fonction de ω donné par GdB = 20log(| H(ω) |).
— la phase en degré en fonction de ω, donnée par arg(H(ω))



                                                                               Fin.




                                            4
~~~
