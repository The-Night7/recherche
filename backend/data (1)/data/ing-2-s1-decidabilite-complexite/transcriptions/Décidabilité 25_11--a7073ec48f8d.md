# Décidabilité 25_11.pdf

[Ouvrir l’original](https://drive.google.com/open?id=17cmm_WUmeRNx6PDtL8CC1eLFBGOaMpsT) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
une machine de Turing est définie par un septuplet
Q, 𝛤, Σ, q0 , B, F, 𝛿
Q un ensemble fini d'états
𝛤 alphabet de ruban
Σ alphabet d'entrée
q0 ∈ Q est l'état initial
B ∈ 𝛤 - Σ est le symbole blanc ('ici ▢')
F ⊆ Q est l'ensemble des états acceptants
𝛿 Q * 𝛤 ⟹ { L, S, R }*Q avec { L, S, R } ≡ { Left, Straight, Right }

NB : Dans l'article de Turing, elle est appelée a-machine pour automatic machine
_______
Il faut que Σ ait au moins 2 symboles/éléments
_______
Elle dispose d'une bande bi - infinie sur laquelle il est possible de lire et d'écrire.
Elle dispose d'une tête de lecture / écriture
Elle recoit en entrée un mot s0 s 1 ... s n où si ∈ Σ
Au départ elle est dans l'état q0
Elle commence la lecture par le symbole le plus à gauche de la chaîne
A chaque fois q'une symbole s est lu
elle trouve la transition (q, s) ⟹ (s'. dep. q') où q est l'état en cours
elle s'écrit s'
elle effectue le déplacement dep
elle passe dans l'état q'
~~~

## Page 2

~~~text
                              1 0 1 1 0

                                       0;1;R



                      917                             923


                                    ◻; ◻;L


                      942                            91327


q0 ⟹ 1, q17,L
                             a n b n |n ⩾ 0 =
                            = { 𝜖, ab, aabb, aaabbb,... }

                            q succès
                            q échec

    1;0;R
    1;0;R


                ◻; ◻;S
        q0                  HALT




Q × 𝛤 ⟹ 𝛤 × dep × Q
Q × 𝛤 ⟹ Q
                             b


             ◻; ◻;S
   q0                   HALT



        a


                b
   q0                    HALT
~~~
