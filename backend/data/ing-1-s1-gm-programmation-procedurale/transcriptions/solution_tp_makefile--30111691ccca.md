# solution_tp_makefile.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1rnagr-5XQQtsb7WbmLMapRss5rk0uUwQ) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Solution complète du TP Makefile
Exercice 1 :
toto: main.c score.c gui.c ia.c
gcc main.c score.c gui.c ia.c -o toto
Exercice 2 :
PROG = toto
OBJ = main.o score.o gui.o ia.o
$(PROG): $(OBJ)
gcc $^ -o $@
%.o : %.c
gcc -c $<
Exercice 3 :
clean:
rm -f $(OBJ) $(PROG) *~ *.bak *.old #*#
[...]
Makefile final complet :
(Le Makefile final complet est donné dans la discussion ChatGPT.)
~~~
