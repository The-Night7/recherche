# -*- coding: utf-8 -*-
"""
Vidéos liées à chaque passage (exercice, partie de cours…).

Chaque notion du catalogue a des mots-clés ; un passage est relié aux
notions dont les mots-clés apparaissent dans son texte (ou son titre),
pondérées comme en TF-IDF : une notion présente partout (« matrice »)
pèse moins qu'une notion rare (« Cayley-Hamilton »). Le lien ouvre une
vidéo précise des chaînes Maths Adultes ou E-learning physique (VIDEOS) ;
pour une notion qu'elles ne traitent pas, une recherche YouTube :
« <notion> cours » pour un cours, « <notion> exercice corrigé » pour un TD/DS/CC/QCM.

Mots-clés : sans accents, en minuscules, les tirets valent des espaces.
Un mot-clé est un début de mot (« diagonalis » trouve « diagonalisable ») ;
terminé par « $ », il doit être un mot entier (« rang$ » ne trouve pas « range »).
"""
import math
import re
import unicodedata
from collections import Counter
from urllib.parse import quote_plus


MAX_VIDEOS = 3
EXERCISE_KINDS = {"td", "ds", "cc", "qcm", "tp"}

# (notion, domaines, mots-clés, recherche YouTube si différente du nom)
NOTIONS = [
    # ---- logique, ensembles, arithmétique ----
    ("Raisonnement par récurrence", "math", "recurrence, par recurrence, heredite"),
    ("Logique et quantificateurs", "math", "quantificateur, contraposee, raisonnement par l'absurde, table de verite"),
    ("Injection, surjection, bijection", "math", "injecti, surjecti, bijecti, image reciproque, image directe"),
    ("Ensembles et opérations", "math", "sous ensemble, sous ensembles, partition de, complementaire, ensemble des parties, produit cartesien, reunion, intersection, lois de morgan"),
    ("Borne supérieure et borne inférieure", "math", "borne superieure, borne inferieure, bornes superieures, bornes inferieures, majorant, minorant, plus grand element, plus petit element, propriete de la borne"),
    ("Sommes et produits", "math", "changement d'indice, somme telescopique, sommes telescopiques, sommes doubles, somme double, somme des termes, somme des n premiers"),
    ("Relations d'équivalence et d'ordre", "math", "relation d'equivalence, relation d'ordre, classe d'equivalence, classes d'equivalence"),
    ("Dénombrement", "math", "denombrement, coefficient binomial, coefficients binomiaux, binome de newton, factorielle, arrangements, combinaisons, parties a k elements"),
    ("Arithmétique des entiers", "math", "pgcd, ppcm, bezout, nombre premier, nombres premiers, congruence, modulo, theoreme de gauss, algorithme d'euclide, premiers entre eux, diviseur, diviseurs, divise$"),
    ("Groupes", "math", "groupe$, groupes$, sous groupe, morphisme de groupe, groupe symetrique, ordre d'un element"),
    ("Anneaux et corps", "math", "anneau, anneaux, corps commutatif, ideal$, ideaux, anneau integre"),
    # ---- nombres, fonctions usuelles ----
    ("Nombres complexes", "math phys", "nombre complexe, nombres complexes, forme exponentielle, forme trigonometrique, forme algebrique, conjugue, partie reelle, partie imaginaire, racines n iemes, racine n ieme, racines de l'unite, formule de moivre, formule d'euler, re(z), im(z), affixe"),
    ("Trigonométrie", "math", "trigonometr, formules d'addition, cercle trigonometrique, equation trigonometrique, sin(, cos(, tan("),
    ("Fonctions trigonométriques réciproques", "math", "arctan, arcsin, arccos"),
    ("Fonctions hyperboliques", "math", "hyperbolique, argsh, argch, argth"),
    ("Logarithme et exponentielle", "math", "logarithme, exponentielle$, fonction exponentielle, fonction ln, croissances comparees"),
    ("Polynômes", "math", "polynome, racine d'un polynome, racine multiple, racines multiples, degre du polynome, polynomes irreductibles, factorisation dans"),
    ("Division euclidienne de polynômes", "math", "division euclidienne de polynome, division euclidienne de p, division suivant les puissances croissantes"),
    ("Décomposition en éléments simples", "math", "elements simples, fraction rationnelle, fractions rationnelles, partie entiere d'une fraction, pole$, poles$"),
    # ---- analyse réelle ----
    ("Suites numériques", "math", "suite convergente, suites convergentes, suite croissante, suite decroissante, suite monotone, suite majoree, suite minoree, suite bornee, suite extraite, suites extraites, bolzano, suite de cauchy, suites de cauchy, limite de la suite, suite (u_n), suite (un), suite de reels, suites de reels, suite reelle, lim n$"),
    ("Suites adjacentes", "math", "suites adjacentes, adjacentes"),
    ("Suites récurrentes", "math", "suite recurrente, suites recurrentes, u_{n+1} = f(u_n), un+1 = f(un), point fixe de f"),
    ("Suites arithmétiques et géométriques", "math", "suite arithmetique, suites arithmetiques, suite geometrique, suites geometriques, arithmetico geometrique"),
    ("Limites de fonctions", "math", "limite de f, limite en, limites de fonctions, forme indeterminee, formes indeterminees, theoreme des gendarmes, encadrement, lim x$"),
    ("Continuité", "math", "continuit, fonction continue, prolongement par continuite, prolongeable par continuite, theoreme des valeurs intermediaires, tvi$, continue en, est continue"),
    ("Dérivation", "math", "derivable, derivabilite, derivee, nombre derive, derivee seconde, fonction derivee"),
    ("Théorème des accroissements finis et de Rolle", "math", "accroissements finis, theoreme de rolle, rolle$, inegalite des accroissements"),
    ("Convexité", "math", "convexe, convexite, concave, inegalite de jensen"),
    ("Développements limités", "math", "developpement limite, developpements limites, dl$, dl a l'ordre, taylor young, partie reguliere"),
    ("Formules de Taylor", "math", "formule de taylor, formules de taylor, taylor lagrange, reste integral, inegalite de taylor"),
    ("Équivalents et négligeabilité", "math", "equivalent en, equivalents usuels, negligeable, sont equivalentes en, relations de comparaison, fonctions equivalentes, suites equivalentes"),
    ("Calcul de primitives", "math", "primitive, primitives"),
    ("Intégration par parties", "math", "integration par parties, ipp$"),
    ("Changement de variable dans une intégrale", "math", "changement de variable"),
    ("Sommes de Riemann", "math", "somme de riemann, sommes de riemann"),
    ("Intégrales généralisées", "math", "integrale generalisee, integrales generalisees, integrale impropre, integrales impropres, integrale de bertrand, integrales de riemann, integrale de riemann convergente"),
    ("Équations différentielles linéaires", "math phys", "equation differentielle, equations differentielles, variation de la constante, variation des constantes, solution homogene, solution particuliere, equation caracteristique, equation homogene, probleme de cauchy"),
    # ---- algèbre linéaire ----
    ("Systèmes linéaires et pivot de Gauss", "math", "pivot de gauss, systeme lineaire, systemes lineaires, echelonn, methode du pivot, operations elementaires"),
    ("Calcul matriciel", "math", "produit matriciel, produit de matrices, matrice inverse, inverse de la matrice, inversible, transposee, matrice carree, trace de la matrice, trace de a$, matrices nilpotentes, matrice nilpotente, nilpotent"),
    ("Déterminant", "math", "determinant, determinants, cofacteur, comatrice, developpement par rapport, regle de sarrus, sarrus"),
    ("Espaces vectoriels", "math", "espace vectoriel, espaces vectoriels, sous espace vectoriel, sous espaces vectoriels, combinaison lineaire, combinaisons lineaires, sous espace engendre, vect$"),
    ("Famille libre, génératrice et base", "math", "famille libre, famille liee, famille generatrice, familles libres, base de, dimension finie, dimension de, base canonique, sous espaces supplementaires, supplementaire de, supplementaires dans, somme directe, theoreme de la base incomplete"),
    ("Applications linéaires", "math", "application lineaire, applications lineaires, noyau, endomorphisme, isomorphisme, theoreme du rang, rang$, projecteur, symetrie vectorielle"),
    ("Matrice d'une application linéaire et changement de base", "math", "changement de base, matrice de passage, matrice de l'application, matrice dans la base, matrices semblables, semblable"),
    ("Valeurs propres et vecteurs propres", "math", "valeur propre, valeurs propres, vecteur propre, vecteurs propres, sous espace propre, sous espaces propres, polynome caracteristique, spectre$"),
    ("Diagonalisation", "math", "diagonalis"),
    ("Trigonalisation", "math", "trigonalis, triangularis"),
    ("Polynôme annulateur et Cayley-Hamilton", "math", "polynome annulateur, polynomes annulateurs, cayley, polynome minimal, lemme des noyaux"),
    ("Réduction de Jordan et de Dunford", "math", "jordan, dunford, sous espace caracteristique, sous espaces caracteristiques"),
    ("Exponentielle de matrice et systèmes différentiels", "math", "exponentielle de matrice, exponentielle d'une matrice, exponentielle de a, systeme differentiel, systemes differentiels, x' = ax"),
    ("Formes bilinéaires et quadratiques", "math", "forme bilineaire, formes bilineaires, forme quadratique, formes quadratiques, signature, reduction de gauss, forme polaire, matrice de la forme"),
    ("Produit scalaire et espaces euclidiens", "math", "produit scalaire, produits scalaires, prehilbert, euclidien, euclidiens, orthogonal, orthogonaux, orthonorme, inegalite de cauchy schwarz, cauchy schwarz"),
    ("Procédé de Gram-Schmidt", "math", "gram schmidt, orthonormalis"),
    ("Projection orthogonale", "math", "projection orthogonale, projecteur orthogonal, distance a un sous espace"),
    ("Théorème spectral et matrices symétriques", "math", "theoreme spectral, matrice symetrique, matrices symetriques, endomorphisme symetrique, endomorphismes symetriques, autoadjoint, auto adjoint, symetrique reelle"),
    ("Matrices orthogonales et isométries", "math", "matrice orthogonale, matrices orthogonales, isometrie, isometries, groupe orthogonal"),
    # ---- analyse dans Rⁿ ----
    ("Normes", "math", "norme, normes, normes equivalentes, espace vectoriel norme, inegalite triangulaire"),
    ("Topologie de ℝⁿ", "math", "topologi, boule ouverte, boule fermee, boules ouvertes, partie ouverte, partie fermee, ensemble ouvert, ensemble ferme, adherence, interieur de, frontiere, compact"),
    ("Fonctions de plusieurs variables : limites et continuité", "math", "plusieurs variables, deux variables, en (0,0), coordonnees polaires, fonction de r2, fonctions de r^n"),
    ("Dérivées partielles et différentielle", "math", "derivee partielle, derivees partielles, differentiabl, differentielle, gradient, jacobienne, derivee directionnelle, derivee selon un vecteur, classe c1, de classe c^1, regle de la chaine"),
    ("Extrema de fonctions de plusieurs variables", "math", "extremum, extrema, point critique, points critiques, hessienne, maximum local, minimum local, point col, point selle, notations de monge"),
    ("Intégrales doubles et triples", "math phys", "integrale double, integrales doubles, integrale triple, integrales triples, fubini, coordonnees cylindriques, coordonnees spheriques, jacobien"),
    ("Intégrales curvilignes et formule de Green", "math phys", "integrale curviligne, integrales curvilignes, green riemann, formule de green, circulation"),
    # ---- séries ----
    ("Séries numériques", "math", "serie numerique, series numeriques, serie convergente, series convergentes, serie divergente, serie de terme general, terme general, somme partielle, sommes partielles, serie geometrique, series geometriques"),
    ("Critères de convergence des séries", "math", "d'alembert, regle de cauchy, critere de cauchy, serie de riemann, series de riemann, comparaison serie integrale, comparaison serie, series a termes positifs"),
    ("Séries alternées et convergence absolue", "math", "serie alternee, series alternees, critere special, convergence absolue, absolument convergente, semi convergente"),
    ("Séries entières", "math", "serie entiere, series entieres, rayon de convergence, lemme d'abel, developpable en serie entiere"),
    ("Séries de Fourier", "math phys", "serie de fourier, series de fourier, coefficients de fourier, parseval, theoreme de dirichlet, polynome trigonometrique"),
    ("Suites et séries de fonctions", "math", "convergence uniforme, convergence simple, convergence normale, suite de fonctions, suites de fonctions, serie de fonctions, series de fonctions"),
    ("Intégrales à paramètre", "math", "integrale a parametre, integrales a parametre, integrale dependant d'un parametre, convergence dominee, hypothese de domination"),
    # ---- mesure, probabilités, statistique ----
    ("Théorie de la mesure et intégrale de Lebesgue", "math", "tribu, tribus, mesurable, mesure de lebesgue, integrale de lebesgue, lebesgue, lemme de fatou, fatou, convergence monotone, beppo levi, borelien, boreliens"),
    ("Probabilités conditionnelles et formule de Bayes", "math", "probabilite conditionnelle, probabilites conditionnelles, bayes, probabilites totales, evenements independants, independance des evenements, mutuellement independants, variables aleatoires independantes, univers$, evenements"),
    ("Variables aléatoires discrètes", "math", "variable aleatoire discrete, variables aleatoires discretes, loi de x, variable aleatoire, variables aleatoires"),
    ("Lois discrètes usuelles", "math", "loi de bernoulli, bernoulli, loi binomiale, binomiale, loi de poisson, loi geometrique, loi uniforme discrete, loi hypergeometrique"),
    ("Espérance, variance et covariance", "math", "esperance, variance, ecart type, covariance, coefficient de correlation, theoreme de transfert"),
    ("Variables aléatoires à densité", "math", "densite de probabilite, a densite, fonction de densite, fonction de repartition, loi uniforme, loi exponentielle, loi normale, gaussienne, loi gamma"),
    ("Couples de variables aléatoires", "math", "couple de variables, couple aleatoire, loi conjointe, lois conjointes, loi marginale, lois marginales, vecteur aleatoire, vecteurs aleatoires"),
    ("Fonctions génératrices", "math", "fonction generatrice, fonctions generatrices, fonction caracteristique"),
    ("Loi des grands nombres et théorème central limite", "math", "loi des grands nombres, limite centrale, tcl$, bienayme, tchebychev, inegalite de markov, convergence en loi, convergence en probabilite, presque surement"),
    ("Estimation et intervalles de confiance", "math", "intervalle de confiance, intervalles de confiance, estimateur, estimateurs, biais, maximum de vraisemblance, vraisemblance"),
    ("Tests statistiques", "math", "test d'hypothese, tests d'hypothese, hypothese nulle, p valeur, khi deux, khi 2, chi2, test de student, niveau de signification"),
    ("Régression linéaire", "math", "regression lineaire, moindres carres, coefficient de determination, regression multiple, colinearite, residus"),
    ("Statistique descriptive", "math", "statistique descriptive, mediane, quartile, quartiles, histogramme, boite a moustaches, diagramme en boite, effectif"),
    ("Analyse en composantes principales", "math info", "composantes principales, acp$, valeurs singulieres, svd$"),
    ("Séries temporelles", "math", "serie temporelle, series temporelles, autocorrelation, arma$, arima, stationnar, bruit blanc, saisonnalite, lissage exponentiel"),
    # ---- optimisation, analyse numérique, EDP, signal ----
    ("Optimisation sous contraintes et multiplicateurs de Lagrange", "math", "multiplicateurs de lagrange, multiplicateur de lagrange, lagrangien, kkt$, karush, sous contrainte, sous contraintes"),
    ("Descente de gradient", "math info", "descente de gradient, methode du gradient, gradient conjugue, pas optimal, pas fixe"),
    ("Programmation linéaire et simplexe", "math", "programmation lineaire, simplexe, programme lineaire"),
    ("Méthode de Newton et résolution d'équations", "math", "methode de newton, newton raphson, dichotomie, methode du point fixe, methode de la secante"),
    ("Méthodes d'Euler et de Runge-Kutta", "math", "methode d'euler, euler explicite, euler implicite, runge kutta, schema numerique"),
    ("Interpolation polynomiale", "math", "interpolation, polynome de lagrange, polynomes de lagrange, polynome interpolateur, differences divisees"),
    ("Intégration numérique", "math", "methode des trapezes, methode des rectangles, simpson, quadrature"),
    ("Décomposition LU et Cholesky", "math", "decomposition lu, factorisation lu, cholesky, methode de jacobi, gauss seidel, conditionnement"),
    ("Équations aux dérivées partielles", "math phys", "equation de la chaleur, equation des ondes, differences finies, equation aux derivees partielles, equations aux derivees partielles, edp$, equation de transport, equation de laplace"),
    ("Transformée de Fourier", "math phys", "transformee de fourier, transformees de fourier, fft$, spectre du signal"),
    ("Convolution et filtrage", "math phys", "convolution, produit de convolution, filtre, filtrage, reponse impulsionnelle, fonction de transfert"),
    ("Échantillonnage et théorème de Shannon", "math phys", "echantillonnage, shannon, nyquist, repliement"),
    ("Transformée en Z et de Laplace", "math phys", "transformee en z, transformee de laplace"),
    ("Compressed sensing et parcimonie", "math", "compressed sensing, compressive sensing, acquisition comprimee, parcimon, sparse, norme l1, lasso, isometrie restreinte"),
    # ---- informatique ----
    ("Pseudo-code et variables", "info", "pseudo code, algorithme$, declaration de variable, affectation"),
    ("Conditions et boucles", "info", "boucle for, boucle while, boucle pour, boucle tant que, tant que, structure conditionnelle, si alors sinon, do while"),
    ("Fonctions et procédures", "info", "procedure, passage par valeur, passage par adresse, passage par reference, parametre formel, valeur de retour"),
    ("Tableaux", "info", "tableau, tableaux, tableau a deux dimensions, matrice de caracteres"),
    ("Chaînes de caractères en C", "info", "chaine de caracteres, chaines de caracteres, strlen, strcpy, strcmp"),
    ("Pointeurs en C", "info", "pointeur, pointeurs, adresse memoire, dereferencement"),
    ("Allocation dynamique (malloc)", "info", "malloc, calloc, realloc, free(, allocation dynamique, fuite memoire"),
    ("Structures en C", "info", "struct$, typedef, structure de donnees, enregistrement"),
    ("Fichiers en C", "info", "fopen, fclose, fprintf, fscanf, fichier texte, fichier binaire"),
    ("Compilation séparée et Makefile", "info", "makefile, compilation separee, fichier d'en tete, gcc$"),
    ("Récursivité", "info", "recursi, appel recursif, cas de base, recursion terminale"),
    ("Complexité algorithmique", "info", "complexite, grand o, o(n, o(log, o(n^2), cout de l'algorithme, complexite temporelle"),
    ("Algorithmes de tri", "info", "tri par insertion, tri fusion, tri rapide, quicksort, tri a bulles, tri par selection, tri par tas, algorithme de tri, algorithmes de tri"),
    ("Recherche dichotomique", "info", "recherche dichotomique, recherche par dichotomie"),
    ("Listes chaînées", "info", "liste chainee, listes chainees, liste doublement chainee, maillon"),
    ("Piles et files", "info", "pile$, piles$, file d'attente, files d'attente, pile et file, piles et files, empiler, depiler, enfiler, defiler, lifo, fifo", "pile et file structure de données"),
    ("Arbres binaires", "info", "arbre binaire, arbres binaires, parcours prefixe, parcours infixe, parcours postfixe, feuilles de l'arbre, noeud interne, sous arbre, hauteur de l'arbre"),
    ("Arbres binaires de recherche et AVL", "info", "arbre binaire de recherche, arbres binaires de recherche, abr$, avl$, rotation, equilibrage, facteur d'equilibre"),
    ("Tas et files de priorité", "info", "tas$, tas min, tas max, file de priorite, files de priorite"),
    ("Tables de hachage", "info", "table de hachage, tables de hachage, fonction de hachage, hachage, collision"),
    ("Programmation dynamique", "info", "programmation dynamique, memoisation"),
    ("Algorithmes gloutons", "info", "glouton, gloutons, gloutonne"),
    ("Graphes : définitions et représentations", "info", "graphe, graphes, sommet, sommets, arete, aretes, arc$, arcs$, matrice d'adjacence, liste d'adjacence, degre d'un sommet, graphe oriente"),
    ("Parcours de graphes (largeur, profondeur)", "info", "parcours en largeur, parcours en profondeur, bfs$, dfs$, tri topologique"),
    ("Plus court chemin (Dijkstra, Bellman-Ford)", "info", "plus court chemin, plus courts chemins, dijkstra, bellman, floyd warshall"),
    ("Arbres couvrants (Kruskal, Prim)", "info", "arbre couvrant, arbres couvrants, kruskal, prim$"),
    ("Flots et coloration de graphes", "info", "flot, flots, ford fulkerson, coupe minimale, coloration, nombre chromatique"),
    ("Graphes eulériens et hamiltoniens", "info", "eulerien, euleriens, hamiltonien, hamiltoniens, chaine eulerienne, cycle eulerien"),
    ("Automates finis", "info", "automate, automates, etat initial, etats finaux, determinis, minimisation, automate fini"),
    ("Langages et expressions rationnelles", "info", "expression rationnelle, expressions rationnelles, expression reguliere, expressions regulieres, langage rationnel, langages rationnels, kleene, lemme de l'etoile"),
    ("Grammaires formelles", "info", "grammaire, grammaires, hors contexte, algebrique, derivation, arbre de derivation, forme normale de chomsky"),
    ("Machines de Turing et décidabilité", "info", "machine de turing, machines de turing, decidab, indecidab, probleme de l'arret, semi decidable, reduction$"),
    ("Classes de complexité P et NP", "info", "np complet, np complets, np difficile, classe p$, classe np, reduction polynomiale, sat$, 3 sat, cook"),
    ("Commandes Unix et shell", "info", "shell, bash, commande, commandes, chmod, grep, ls$, cd$, terminal, arborescence, chemin absolu, chemin relatif, droits d'acces"),
    ("Redirections, tubes et scripts shell", "info", "redirection, redirections, pipe, tube, tubes, script shell, scripts shell, variable d'environnement, sed$, awk$"),
    ("Processus et fork", "info", "processus, fork, exec$, execlp, execvp, execv$, wait(, pid$, processus fils, processus pere, zombie"),
    ("Threads et synchronisation", "info", "thread, threads, pthread, semaphore, semaphores, mutex, section critique, interblocage, exclusion mutuelle, producteur consommateur"),
    ("Ordonnancement et mémoire", "info", "ordonnancement, round robin, memoire virtuelle, pagination, segmentation, defaut de page"),
    ("Signaux et communication entre processus", "info", "signal$, signaux, kill, sigint, tube nomme, memoire partagee, file de messages"),
    ("Modèle entité-association", "info", "entite association, modele entite, entite, association, cardinalite, cardinalites, mcd$"),
    ("Modèle relationnel et normalisation", "info", "modele relationnel, cle primaire, cle etrangere, dependance fonctionnelle, dependances fonctionnelles, forme normale, normalisation, 3fn$"),
    ("Algèbre relationnelle", "info", "algebre relationnelle, operateur de selection, operateur de projection, jointure naturelle"),
    ("Requêtes SQL", "info", "sql$, select, where, group by, order by, jointure, jointures, requete, requetes, having, insert into"),
    ("Programmation fonctionnelle (OCaml)", "info", "ocaml, let rec, filtrage, pattern matching, match with, ordre superieur, curryfication, fonction anonyme, lambda calcul, haskell"),
    ("Programmation fonctionnelle en Scala", "info", "scala, case class, lazylist, lazy list, evaluation paresseuse, immutable, immuable, higher order, liskov, trait$", "programmation fonctionnelle scala"),
    ("Programmation parallèle (OpenMP, MPI)", "info", "openmp, mpi$, parallelis, speedup, acceleration, loi d'amdahl, amdahl, pragma omp"),
    ("Réseaux : modèle OSI et TCP/IP", "info", "modele osi, tcp, udp, adresse ip, adresses ip, sous reseau, masque de sous reseau, routage, protocole, dns$, couche transport, couche reseau"),
    ("Réseaux de neurones", "info", "reseau de neurones, reseaux de neurones, neurone, perceptron, retropropagation, fonction d'activation, deep learning"),
    ("Apprentissage supervisé", "info math", "apprentissage supervise, classification, k plus proches voisins, knn$, arbre de decision, arbres de decision, random forest, svm$, regression logistique, surapprentissage, validation croisee, matrice de confusion"),
    ("Clustering (k-means, CAH)", "info math", "clustering, k means, kmeans, classification hierarchique, cah$, dendrogramme, apprentissage non supervise"),
    ("Data mining et règles d'association", "info math", "regles d'association, regle d'association, apriori, itemset, support et confiance"),
    ("Méthodes agiles et Scrum", "info", "agile, agiles, scrum, sprint, backlog, user story, kanban"),
    # ---- physique ----
    ("Analyse dimensionnelle", "phys", "analyse dimensionnelle, homogeneite, homogene, equation aux dimensions, unites si, unites du si, dimension physique, pour dimension, ordre de grandeur, ordres de grandeur, radian$"),
    ("Vecteurs, produit scalaire et produit vectoriel", "phys", "produit vectoriel, produit mixte, vecteur unitaire, base orthonormee"),
    ("Cinématique du point", "phys", "cinematique, vecteur vitesse, vecteur acceleration, trajectoire, coordonnees cartesiennes, coordonnees polaires, coordonnees cylindriques, base de frenet, repere de frenet, mouvement rectiligne, mouvement circulaire, orthoradial, radiale, vecteur position, base polaire, vitesse angulaire, acceleration angulaire"),
    ("Changement de référentiel", "phys", "changement de referentiel, referentiel non galileen, force d'inertie, forces d'inertie, force de coriolis, coriolis, force centrifuge, composition des vitesses"),
    ("Principe fondamental de la dynamique", "phys", "principe fondamental de la dynamique, pfd$, lois de newton, deuxieme loi de newton, quantite de mouvement, referentiel galileen, bilan des forces, tension du fil, reaction du support, equation du mouvement, equations du mouvement, chute libre, force de traction, forces qui agissent, reaction du plan, poids$"),
    ("Équilibre et stabilité", "phys", "position d'equilibre, positions d'equilibre, equilibre stable, equilibre instable, stabilite de l'equilibre"),
    ("Gravitation universelle", "phys", "gravitation, gravitationnelle, attraction universelle, champ de gravitation, constante de gravitation"),
    ("Frottements", "phys", "frottement, frottements, frottement fluide, frottement solide, lois de coulomb du frottement"),
    ("Travail, puissance et énergie", "phys", "energie cinetique, energie potentielle, energie mecanique, travail d'une force, theoreme de l'energie, puissance d'une force, force conservative, forces conservatives, travail elementaire"),
    ("Oscillateur harmonique et amorti", "phys", "oscillateur harmonique, oscillateur amorti, oscillateurs, oscillation, oscillations, ressort de raideur, masse ressort, raideur, pendule, pseudo periodique, aperiodique, regime critique, facteur de qualite, resonance, oscillations forcees"),
    ("Moment cinétique et forces centrales", "phys", "moment cinetique, theoreme du moment cinetique, force centrale, forces centrales, lois de kepler, kepler, loi des aires, energie potentielle effective, mouvement a force centrale, satellite"),
    ("Optique géométrique", "phys", "optique geometrique, lentille, lentilles, snell descartes, refraction, reflexion totale, miroir, foyer, relation de conjugaison, grandissement, rayons lumineux, rayon lumineux, point objet, point image, image virtuelle, objet reel"),
    ("Électrocinétique : lois de Kirchhoff", "phys", "loi des mailles, loi des noeuds, kirchhoff, pont diviseur, diviseur de tension, diviseur de courant, resistance equivalente, association de resistances, thevenin, norton"),
    ("Circuits RC, RL et RLC", "phys", "circuit rc, circuit rl, circuit rlc, rlc$, condensateur, bobine, regime transitoire, constante de temps, charge du condensateur"),
    ("Régime sinusoïdal et impédances", "phys", "regime sinusoidal, impedance, impedances, amplitude complexe, notation complexe, diagramme de bode, bode, filtre passe bas, filtre passe haut"),
    ("Champ et potentiel électrostatiques", "phys", "champ electrostatique, champ electrique, loi de coulomb, potentiel electrostatique, potentiel electrique, force electrostatique, charge ponctuelle, charges ponctuelles, distribution de charges, densite de charge, densite lineique, densite surfacique, densite volumique, ligne de champ, lignes de champ, equipotentielle"),
    ("Théorème de Gauss", "phys", "theoreme de gauss, surface de gauss, flux du champ, flux electrique, symetries et invariances, plan de symetrie, plan d'antisymetrie"),
    ("Conducteurs et condensateurs", "phys", "conducteur en equilibre, conducteurs en equilibre, conducteur, capacite, condensateur plan, pression electrostatique"),
    ("Dipôle électrostatique", "phys", "dipole, dipoles, moment dipolaire"),
    ("Magnétostatique : Biot-Savart et Ampère", "phys", "champ magnetique, biot et savart, biot savart, theoreme d'ampere, solenoide, bobines de helmholtz, fil infini, spire"),
    ("Forces de Lorentz et de Laplace", "phys", "force de lorentz, force de laplace, particule chargee, mouvement d'une particule chargee, effet hall, cyclotron"),
    ("Induction électromagnétique", "phys", "induction, loi de faraday, faraday, loi de lenz, lenz, flux magnetique, inductance, auto induction, mutuelle inductance, force electromotrice, fem$"),
    ("Équations de Maxwell", "phys", "equations de maxwell, maxwell gauss, maxwell ampere, maxwell faraday, courant de deplacement"),
    ("Opérateurs gradient, divergence, rotationnel", "phys", "rotationnel, divergence, nabla, laplacien, theoreme de stokes, theoreme d'ostrogradski, ostrogradski, green ostrogradski"),
    ("Ondes progressives et équation de d'Alembert", "phys", "onde progressive, ondes progressives, equation de d'alembert, equation d'onde, celerite, onde plane, ondes planes, longueur d'onde, nombre d'onde, onde sinusoidale, corde vibrante"),
    ("Ondes stationnaires", "phys", "onde stationnaire, ondes stationnaires, noeuds et ventres, modes propres, ventre$, ventres$, corde de melde"),
    ("Interférences et diffraction", "phys", "interference, interferences, diffraction, fentes d'young, trous d'young, difference de marche, figure d'interference, reseau de diffraction, coherence"),
    ("Effet Doppler et battements", "phys", "doppler, battement, battements"),
    ("Ondes électromagnétiques et polarisation", "phys", "onde electromagnetique, ondes electromagnetiques, polarisation, vecteur de poynting, poynting, relation de dispersion, onde dans le vide"),
    ("Effet photoélectrique et photons", "phys", "effet photoelectrique, photon, photons, quanta, constante de planck, planck, effet compton, compton, corps noir"),
    ("Dualité onde-corpuscule", "phys", "dualite onde corpuscule, de broglie, longueur d'onde de de broglie, heisenberg, relation d'incertitude, inegalite de heisenberg"),
    ("Équation de Schrödinger", "phys", "schrodinger, fonction d'onde, puits de potentiel, puits infini, effet tunnel, marche de potentiel, densite de probabilite de presence, etats stationnaires"),
    ("Modèle de Bohr et spectres atomiques", "phys", "modele de bohr, bohr, niveaux d'energie, spectre de raies, atome d'hydrogene, transition electronique, rydberg"),
    ("Relativité restreinte", "phys", "relativite, transformation de lorentz, transformations de lorentz, dilatation du temps, contraction des longueurs, facteur de lorentz, quadrivecteur, einstein"),
    ("Radioactivité et physique nucléaire", "phys", "radioactivite, radioactif, demi vie, desintegration, noyau atomique, fission, fusion nucleaire, energie de liaison, defaut de masse"),
]

# Vidéos des chaînes Maths Adultes (m) et E-learning physique (p), par notion :
# (chaîne, identifiant YouTube, titre, mots-clés). La première vidéo est celle par défaut ;
# une autre est choisie quand ses mots-clés apparaissent davantage dans le passage.
# Les notions absentes ici n'ont pas de vidéo dans ces chaînes : lien vers une recherche YouTube.
VIDEOS = {
    'Raisonnement par récurrence': [
        ('m', 'tIb7OY1To_U', 'La démonstration par récurrence ❤️', ''),
    ],
    'Logique et quantificateurs': [
        ('m', 'laGa8gV2Fcc', 'Langage mathématique épisode 2', 'quantificateur'),
        ('m', 'XSToAHZITPk', 'Langage mathématique épisode 3', 'et ou, negation, connecteur, table de verite'),
        ('m', 'zdW1Nqsg040', 'Langage mathématique épisode 4', 'implication, equivalence'),
        ('m', 'HglbG0vzJM4', 'Langage mathématique épisode 5', 'contraposee, reciproque'),
    ],
    'Injection, surjection, bijection': [
        ('m', 'wO3KzOjQqH0', 'Injection - Surjection - Bijection', ''),
        ('m', 'ziJtJo-OYNw', 'Théorie des ensembles : Image directe et image réciproque', 'image directe, image reciproque'),
    ],
    'Ensembles et opérations': [
        ('m', 'dFTP_ZZhUys', 'Langage mathématiques épisode 1 : Théorie des ensembles', ''),
        ('m', 'r2vcq1jwcno', 'Fonctions indicatrices', 'indicatrice'),
    ],
    "Relations d'équivalence et d'ordre": [
        ('m', 'W7cH06qOImM', 'Relations binaires 1/3 : Les bases', ''),
        ('m', '0qoX6sNm2Jc', "Relations binaires 2/3 : Relations d'équivalence", "relation d'equivalence, classe d'equivalence, classes d'equivalence"),
        ('m', 'g8Tczd1QhJU', "Relations binaires 3/3 : Relations d'ordre", "relation d'ordre, ordre total, ordre partiel"),
        ('m', 'zmJQy0sF4vQ', "Exemples d'ensembles quotients", 'quotient'),
    ],
    'Dénombrement': [
        ('m', 'bx6yFFj5nm4', 'Probabilités 1ère année (2/5) : Dénombrement', ''),
        ('m', 'QUMYiQtz4SE', 'Formule du Binome de Newton', 'binome de newton'),
    ],
    'Arithmétique des entiers': [
        ('m', 'Ist_yFnhDBg', 'Théorème de Bézout', ''),
        ('m', 'uxZAZ4T05wQ', 'Z/nZ : Découverte', 'congruence, modulo, z/nz'),
        ('m', '7o79t2KAKxE', "Z/nZ 3 : Inversibles, calcul de l'inverse", 'inversible'),
        ('m', 'xIzoYxOqmXs', 'Z/nZ 5 : Lemme chinois version pratique', 'chinois'),
        ('m', 'JxmfUhLc3hE', "Z/nZ 6 : Indicatrice d'Euler", "indicatrice d'euler"),
    ],
    'Groupes': [
        ('m', '09BuX_XmNtM', 'Structures algébriques 1 : L.C.I. et Groupes', ''),
        ('m', 'fAqlGVkGpTU', 'Groupe symétrique 1/5 : Permutations', 'groupe symetrique, permutation'),
        ('m', 'Xi0IvDRD8ms', 'Groupe symétrique 2/5 : transpositions et cycles', 'transposition, cycle'),
        ('m', 'zQpUI3_vT-8', 'Groupe symétrique 5/5 : Signature', 'signature'),
        ('m', 'JVcOHqOcxSk', 'Théorème de Lagrange sur les groupes', "lagrange, ordre d'un element"),
        ('m', 'aF33pF6cnUg', 'Structures algébriques 3 : Morphismes et isomorphismes', 'morphisme'),
        ('m', 'Y2m3rQncEJM', 'Groupes monogènes et cycliques', 'cyclique, monogene'),
    ],
    'Anneaux et corps': [
        ('m', '-ZnzKX0I6B8', 'Structures algébriques 2 : Anneaux et Corps', ''),
        ('m', 'IaSVaxl4Sbg', 'Structures algébriques 4 : Idéaux', 'ideal, ideaux'),
        ('m', 'VmjOWHg8FL0', 'Structures Algébriques 5 : Anneaux Quotients', 'quotient'),
    ],
    'Nombres complexes': [
        ('m', 'Iphz0Np1-_k', 'Nombres complexes 1/12 : construction', ''),
        ('m', 'XIHfdJGj9hI', 'Nombres Complexes 3/12 : Calculs et conjuguaison', 'conjugue, forme algebrique'),
        ('m', 'knME7MU3EmQ', 'Nombres complexes 4/12 : Module', 'module'),
        ('m', 'Cgy5KDxRtjI', 'Nombres complexes 5/12 : Équations algébriques', 'equation'),
        ('m', '39Pwt9NzxVA', 'Nombres complexes 6/12 : Argument (la base)', 'argument'),
        ('m', 'sD9bQzxpn2E', 'Nombres complexes (8/12) forme exponentielle', 'forme exponentielle, forme trigonometrique'),
        ('m', '_l9-8b4T9c0', "Nombres complexes 9/12 : Formules de Moivre et D'Euler", "moivre, formule d'euler, linearis"),
        ('m', '7nttqyqc49k', "Nombres complexes 10/12 : Racines n-ièmes de l'unité", "racine n ieme, racines n iemes, racines de l'unite"),
        ('m', 'JdDVizQfL-U', 'Nombres complexes 11/12 : Un peu de géométrie', 'affixe, geometrie'),
    ],
    'Fonctions trigonométriques réciproques': [
        ('m', 'CcHVYVkDKpk', 'Arccos et Arcsin, la réciproque du cosinus et du sinus', ''),
        ('m', '3JDxWR5Ut9E', "Arctan, qu'est-ce que c'est ?", 'arctan'),
    ],
    'Logarithme et exponentielle': [
        ('m', 'TvwUwUo8yRM', 'Règle de croissance comparée pour le calcul de limites', ''),
    ],
    'Polynômes': [
        ('m', 'X30lkvdDCEM', 'Polynômes 1 : définition', ''),
        ('m', 'YqDvomYyygk', 'Polynômes 2 : Degré et valuation', 'degre, valuation'),
        ('m', 'ufg3W4kH4Nk', 'Polynômes 5 : racines', 'racine'),
    ],
    'Division euclidienne de polynômes': [
        ('m', '-1okAlCmCt0', 'Polynômes 4 : Division Euclidienne', ''),
    ],
    'Décomposition en éléments simples': [
        ('m', 'hwAF0INbH3E', 'Fractions Rationnelles', ''),
    ],
    'Limites de fonctions': [
        ('m', 'TvwUwUo8yRM', 'Règle de croissance comparée pour le calcul de limites', ''),
    ],
    'Continuité': [
        ('m', 'xgENfRQvPrA', 'Théorème des valeurs intermédiaires et applications', ''),
    ],
    'Dérivation': [
        ('m', '9uxqE3Ob_h0', "L'application dérivée, qu'est-ce que c'est ?", ''),
    ],
    'Convexité': [
        ('m', 'ffyTqLmImy4', 'Fonctions convexes 1/2', ''),
        ('m', 'mO4jxjJ6IRU', 'Fonctions Convexes 2/2', 'jensen'),
    ],
    'Calcul de primitives': [
        ('m', 'RftTWACh_IY', "Intégrale de Riemann 4/4 : théorème fondamental de l'analyse", ''),
    ],
    'Sommes de Riemann': [
        ('m', 'xLEIKgF5EQ0', 'Intégrale de Riemann 2/4 : Sommes de Darboux et sommes de Riemann', ''),
    ],
    'Intégrales généralisées': [
        ('m', 'neIGPipnfuA', 'Intégrales généralisées 1/3 : Les bases', ''),
        ('m', '3iiHZlU7Y0Y', 'Intégrales généralisées 2/3 : critères de convergences', 'critere, comparaison, equivalent'),
        ('m', 'Nj_slllCStI', 'Intégrales généralisées 3/3 : des exemples et contre-exemples à connaître', 'bertrand, contre exemple'),
    ],
    'Équations différentielles linéaires': [
        ('m', 'BtWqkWzjS6c', "Équation différentielles linéaires d'ordre 1", ''),
        ('m', 'XV6wxwZhyeo', "Équation différentielles linéaires d'ordre 2", "ordre 2, second ordre, equation caracteristique, y''"),
        ('p', 'eWHYnqvp8yI', '3 équations différentielles à maîtriser parfaitement en physique', 'oscillateur, amorti, circuit'),
    ],
    'Systèmes linéaires et pivot de Gauss': [
        ('m', 'b3W_-ux1kwM', 'Systèmes linéaires - pivot de Gauss', ''),
    ],
    'Calcul matriciel': [
        ('m', 'bq_X83YGqHc', 'Applications linéaires (4/15) : Multiplication des matrices', ''),
        ('m', 'k6YHldiEu64', "Calcul de l'inverse d'une matrice", 'inverse, inversible'),
        ('m', 'wWWhepnzzAs', 'Applications linéaires (7/15) : Matrice transposée', 'transposee'),
        ('m', 'Q8u1YOAdyss', "Algèbre linéaire (10/15) : Trace d'une matrice", 'trace'),
    ],
    'Déterminant': [
        ('m', 'kpawePGJrBc', 'Déterminant 3/4 : Pour une matrice', ''),
        ('m', 'hp-qcoHnXV0', 'Déterminants (1/4) : En dimension 2', 'dimension 2'),
        ('m', 'zBgRfRMBUKo', 'Déterminant (2/4) : Pour une famille de vecteur', 'famille'),
        ('m', 'A5NHR_l94zQ', 'Déterminant 4/4 : Rêgles de calculs', 'developpement, cofacteur, sarrus, operations'),
    ],
    'Espaces vectoriels': [
        ('m', 'AFdeofSJEW0', 'Espaces Vectoriels', ''),
        ('m', '_vqRbp96jsc', 'Sous-espaces Vectoriels', 'sous espace'),
        ('m', 'AHlWLCNJOQg', "Somme d'espaces vectoriels", 'somme directe, supplementaire'),
    ],
    'Famille libre, génératrice et base': [
        ('m', 'itfmEiw9UZI', 'Familles libres. Familles Génératrices.', ''),
        ('m', 's49NjJ7--iY', "Bases d'un espace vectoriel", 'base de, base canonique, base incomplete'),
        ('m', 'cloUp6BKMQE', 'Dimension', 'dimension'),
        ('m', 'AHlWLCNJOQg', "Somme d'espaces vectoriels", 'somme directe, supplementaire'),
    ],
    'Applications linéaires': [
        ('m', 'c5z5Xuseu4w', 'Applications linéaires (1/15) : Découverte', ''),
        ('m', '4H4VgJNTcjE', 'Applications linéaires (5/15) : Noyau et Image', 'noyau, image'),
        ('m', 'NOo3YfCBadY', 'Applications linéaire (6/15) : injectivité et surjectivité', 'injective, surjective, injectivite, surjectivite'),
        ('m', 'XZBIuym0LM8', 'Applications linéaires (11/15) : Notion de rang', 'rang'),
        ('m', 'Kmaf_YELLwU', 'Applications linéaires 13/15 : Théorème du rang', 'theoreme du rang'),
        ('m', 'Ii0ry5gsRoc', 'Applications linéaires (14/15) : Projecteurs Vectoriels', 'projecteur, projection'),
        ('m', '-Z6eiJaKF-w', 'Applications linéaire (15/15) : Symétries', 'symetrie'),
    ],
    "Matrice d'une application linéaire et changement de base": [
        ('m', '--w2c-HvnMk', 'Applications linéaires (8/15) : Changement de bases', ''),
        ('m', 'CKFq_nO8JFM', 'Applications linéaires (2/15) : Introduction des matrices', "matrice de l'application, matrice dans la base"),
        ('m', 'yUqTyZsOHw0', 'Applications linéaires (9/15) : Matrices équivalentes et semblables', 'semblable, equivalentes'),
        ('m', 'TMEW5NNL6ak', "Applications linéaire (12/15) : rang d'une matrice", 'rang'),
    ],
    'Valeurs propres et vecteurs propres': [
        ('m', 'jJmXnpjmk_Y', "Valeurs et vecteurs propres d'un endomorphisme", ''),
        ('m', 'Anct7QvAyZQ', 'Valeurs propres et polynôme caractéristique', 'polynome caracteristique'),
    ],
    'Diagonalisation': [
        ('m', 'oS0CyuU6u6Q', 'Diagonalisation', ''),
        ('m', 'vdGWwov_bUo', 'Applications de la diagonalisation', 'puissance, a^n, suite'),
    ],
    'Trigonalisation': [
        ('m', 'mBCwhDXfGDA', 'Trigonalisation', ''),
    ],
    'Polynôme annulateur et Cayley-Hamilton': [
        ('m', 'H4gegIUIPG4', 'Théorème de Cayley-Hamilton', ''),
        ('m', 'XQyI8qiV-qQ', "Polynôme d'endomorphismes", "polynome annulateur, polynome minimal, polynome d'endomorphisme"),
        ('m', 'x3rEOZL_mCk', 'Lemme des Noyaux', 'lemme des noyaux'),
    ],
    'Réduction de Jordan et de Dunford': [
        ('m', 'T10wc9h7Da8', 'Jordanisation', ''),
        ('m', 'GGZNUreafa8', 'Décomposition de Dunford', 'dunford'),
        ('m', '5BW8idHZE3g', 'Indice de Fitting', 'fitting'),
    ],
    'Produit scalaire et espaces euclidiens': [
        ('m', 'vI5hgxY6t80', 'Topologie 2-3 : Produit scalaire et équivalence de normes', ''),
        ('m', 'GCDtF8vMsz8', 'Inégalité de Cauchy-Schwarz', 'cauchy schwarz'),
        ('m', 'RvZakVo2TeE', 'Séries de Fourier (3/7) : Espace préhilbertien et inégalité de Bessel', 'prehilbert, bessel'),
    ],
    'Théorème spectral et matrices symétriques': [
        ('m', 'ubkTd64LRFA', 'Théorème spectral en dimension finie', ''),
    ],
    'Normes': [
        ('m', 'BXefv0FBWRw', 'Topologie 2-1 : Normes en dimension finie', ''),
        ('m', 'vI5hgxY6t80', 'Topologie 2-3 : Produit scalaire et équivalence de normes', 'normes equivalentes, equivalence'),
        ('m', 'uyLXDmQyFr0', 'Topologie 2-2 Normes en dimension infinie', 'dimension infinie'),
        ('m', 'OG8TBIu6u_g', 'Topologie 2-4 : Suites dans un espace vectoriel normé', 'suite'),
    ],
    'Topologie de ℝⁿ': [
        ('m', 'J2wMxCysvJM', 'Topologie 1 : Introduction et motivation', ''),
        ('m', 'lNDxubfVCBg', "Topologie 4-1 : Ouverts d'un espace métrique", 'ouvert, ouverte, boule ouverte'),
        ('m', 'C1AtXG4sZmw', "Topologie 4-2 : Fermés d'un espace métrique", 'ferme, fermee'),
        ('m', 'JhZAkiv9Fko', 'Topologie 7-1 : Adhérence', 'adherence'),
        ('m', 'aqw-Qz1Ghr8', 'Topologie 7-2 : Intérieur - Frontière', 'interieur, frontiere'),
        ('m', 'qdzftwt53PQ', 'Topologie 14.1 : Compacité, introduction et premières propriétés', 'compact'),
        ('m', '8ICh0fC7YMY', 'Topologie 12.1 : Connexité. Définitions et propriétés.', 'connexe'),
        ('m', '5aZuw155RVw', 'Topologie 8 : Densité', 'dense, densite'),
        ('m', 'h7fxvyiB3Wk', 'Topologie 3-1 : notion de distance', 'distance'),
        ('m', 'o5bBfYspllQ', 'Topologie 15.1 Complétude : Introduction de la notion', 'complet, suite de cauchy'),
    ],
    'Fonctions de plusieurs variables : limites et continuité': [
        ('m', 'J6XNQs0AtUU', 'Topologie 9 : Notion de limite', ''),
        ('m', 'IbSthrPTW7U', 'Topologie 10.1 : Introduction à la continuité', 'continu'),
    ],
    'Intégrales doubles et triples': [
        ('p', 'dJyrBn0Z3CU', 'Déplacements, surfaces et volumes élémentaires en cylindriques et sphériques', ''),
    ],
    'Séries numériques': [
        ('m', 'Vs9tBn0rypw', 'Séries numériques 1/6 : Tous les résultats à connaître.', ''),
        ('m', 'NEo9k3D_yM0', 'Séries numériques 2/6 : Propriétés de base.', 'somme partielle, sommes partielles, telescopique'),
        ('m', 'Pbf4w01aI1o', 'Séries numériques 3/6 : Comparaison série - intégrale.', 'comparaison serie integrale'),
        ('m', 'pr49UU_dioM', 'Séries numériques 6/6 : Produit de Cauchy - Sommations par paquets', 'produit de cauchy, paquets'),
    ],
    'Critères de convergence des séries': [
        ('m', 'eCG_d8wyNzo', "Séries numériques 4/6 : Critère de D'Alembert, Cauchy, Riemann.", ''),
        ('m', 'Pbf4w01aI1o', 'Séries numériques 3/6 : Comparaison série - intégrale.', 'comparaison serie integrale'),
    ],
    'Séries alternées et convergence absolue': [
        ('m', 'bzVNvF16k20', 'Séries numériques 5/6 : Séries alternées et semi-convergentes', ''),
    ],
    'Séries entières': [
        ('m', 'rfgSGYXKuWI', "Séries entières : Qu'est-ce que c'est et à quoi ça sert ? #1", ''),
        ('m', 'p_Ux2s8hhMQ', "Rayon de convergence d'une série entière", 'rayon de convergence'),
        ('m', 'KZ-i8NJYBFA', 'Développement en série entière', 'developpable, developpement en serie entiere'),
        ('m', 'N0cjuOYWzEY', 'Calcul de sommes de séries entières', 'somme de la serie, calculer la somme'),
        ('m', 'f3C9enLV5FQ', 'Somme et produit de séries entières', 'produit de cauchy'),
        ('m', '1dVKAN_Cwqk', 'Propriétés analytiques des séries entières', 'terme a terme'),
    ],
    'Séries de Fourier': [
        ('m', '2XvkiMMOLkM', 'Séries de Fourier (1/7)', ''),
        ('m', 'WKYAFoKIBRE', 'Séries de Fourier (2/7) : tous les résultats à connaître', 'theoreme'),
        ('m', 'uKhyXAfLqJw', 'Séries de Fourier (4/7) : Théorème de Dirichlet et applications', 'dirichlet'),
        ('m', 'iD5KAsWsJd8', 'Séries de Fourier (5/7) : Théorème de convergence normale', 'convergence normale'),
        ('m', 'BJPFdqprXwQ', 'Séries de Fourier (6/7) : Théorème de Fejer', 'fejer'),
        ('m', 'qH8ir4pEt1k', 'Séries de Fourier (7/7) : Parseval et applications', 'parseval'),
        ('m', 'RvZakVo2TeE', 'Séries de Fourier (3/7) : Espace préhilbertien et inégalité de Bessel', 'bessel'),
    ],
    'Suites et séries de fonctions': [
        ('m', 'NwqCpjNvArs', 'Suites de fonctions 1/4 : Convergence simple.', ''),
        ('m', '6AFBk8pE4pA', 'Suites de fonctions 2/4 : Convergence uniforme à la base.', 'convergence uniforme'),
        ('m', 'JoX_wXAhlLo', 'Suites de fonctions 4/4 : Théorème de Weierstrass et applications', 'weierstrass'),
        ('m', '8gDDCN8GWCo', 'Séries de fonctions 1/3 : convergence simple et uniforme', 'serie de fonctions, series de fonctions'),
        ('m', 'i9yJGq66AL4', 'Séries de fonctions 2/3 : convergence normale.', 'convergence normale'),
        ('m', 'CpsxQDVE4ok', 'Séries de fonctions 3/3 : Étude la fonction somme', 'fonction somme'),
    ],
    'Intégrales à paramètre': [
        ('m', 'gka1kMe_sis', 'Fonctions définies par une intégrale', ''),
        ('m', 'nD_5dKJ_WA8', 'Théorème de convergence dominée - Lebesgue # 10', 'convergence dominee'),
        ('m', 'Ez55yeGLqrA', 'Fonction Gamma', 'gamma'),
    ],
    'Théorie de la mesure et intégrale de Lebesgue': [
        ('m', 'OmhEVOrHNZY', 'Introduction à la théorie de la mesure - Lebesgue # 1', ''),
        ('m', 'JGrpKYOyeN8', 'Les tribus en mathématiques - Lebesgue # 2', 'tribu'),
        ('m', 'yH8abQTgkDE', 'Fonctions mesurables - Lebesgue # 3', 'mesurable'),
        ('m', 'yBLpevxCicE', 'La mesure de Lebesgue démystifiée ! - Lebesgue # 5', 'mesure de lebesgue'),
        ('m', '3iEP_tXDc_s', 'Fonctions étagées et leur intégrale - Lebesgue # 6', 'etagee'),
        ('m', '3qkRLnVIT9Y', 'Intégrale de Lebesgue des fonctions positives - Lebesgue # 7', 'positive, convergence monotone, beppo levi, fatou'),
        ('m', 'IWP0vyiNpAE', 'Intégrale de Lebesgue - Lebesgue # 8', 'integrable, integrale de lebesgue'),
        ('m', 'DMbFBNiLboA', 'Égalité presque partout- Espace L1 - Lebesgue # 9', 'presque partout'),
        ('m', 'nD_5dKJ_WA8', 'Théorème de convergence dominée - Lebesgue # 10', 'convergence dominee'),
        ('m', 'r2vcq1jwcno', 'Fonctions indicatrices', 'indicatrice'),
    ],
    'Probabilités conditionnelles et formule de Bayes': [
        ('m', 'jlBDx0eQ9dA', 'Probabilités 1ère année (3/5) : Probabilités conditionnelles', ''),
        ('m', 'OhYJrpmEfS4', 'Probabilités 1ère année (1/5) : Introduction de la notion', 'univers, evenement'),
    ],
    'Variables aléatoires discrètes': [
        ('m', 'Vzeax4CDYdY', 'Probabilités 1ère année (4/5) : Variables aléatoires', ''),
    ],
    'Lois discrètes usuelles': [
        ('m', 'Vzeax4CDYdY', 'Probabilités 1ère année (4/5) : Variables aléatoires', ''),
    ],
    'Espérance, variance et covariance': [
        ('m', 'Vzeax4CDYdY', 'Probabilités 1ère année (4/5) : Variables aléatoires', ''),
    ],
    'Loi des grands nombres et théorème central limite': [
        ('m', 'fIlJZ9GUwgE', 'Probabilités 1ère année (5/5) : Loi des grands nombres', ''),
    ],
    'Équations aux dérivées partielles': [
        ('p', 'eMQ4_uRK94Q', "Cours-Diffusion thermique (1): l'équation de diffusion et le bilan thermique", ''),
        ('p', 'EtJjCXH8eYI', "PC/PSI-Physique des ondes-corde vibrante (1/4)- équation de d'Alembert", "equation des ondes, d'alembert"),
        ('p', 'cN6Qkvv0N3s', 'Cours diffusion de particules (1/5) : équation de diffusion de particules', 'diffusion de particules'),
    ],
    'Transformée de Fourier': [
        ('p', 'NbBMOl8oSDc', "Cours diffraction (2/3): optique de Fourier/cas d'un motif non périodique/transformée de Fourier", ''),
    ],
    'Convolution et filtrage': [
        ('p', 'x5T7H7BYCl0', 'MPSI/PCSI-Filtrage linéaire(3/5)-fonction de transfert-diagramme de Bode', ''),
        ('p', 'iaxNL6HWJqA', 'MPSI/PCSI-Filtrage linéaire(2/5)-analyse qualitative-comment mesurer une fréquence de coupure', 'frequence de coupure'),
    ],
    'Échantillonnage et théorème de Shannon': [
        ('p', 'uGTKFBrt0yw', 'Electronique numérique- échantillonnage (1/4)', ''),
        ('p', '8l6meWY2mvI', 'Le critère de Shannon démontré', 'shannon'),
        ('p', 'a1_E4xXNYgQ', 'Cours-Repliement de spectre- échantillonnage (3/4)', 'repliement'),
        ('p', '0UzCmX7dTsg', 'Electronique numérique- échantillonnage (2/4)- échantillonneur bloqueur', 'bloqueur'),
    ],
    'Complexité algorithmique': [
        ('m', 'mOdHdiE0Rlc', 'Décidabilité et complexité 2/4 : Complexité', ''),
    ],
    'Machines de Turing et décidabilité': [
        ('m', 'X610pII4_J8', 'Décidabilité et complexité 1/4 : Machines de Turing', ''),
    ],
    'Classes de complexité P et NP': [
        ('m', 'aPYmHroE0Nw', 'Décidabilité et complexité 3/4 : P vs NP', ''),
        ('m', 'G6G4-tZRBbQ', 'Décidabilité et complexité 4/4 : problèmes NP-complets', 'np complet'),
    ],
    'Analyse dimensionnelle': [
        ('p', 'an3zN3uhDzo', "La puissance de l'analyse dimensionnelle", ''),
        ('p', '_nuMFHPAIE0', "Les 4 utilisations essentielles de l'analyse dimensionnelle", ''),
    ],
    'Cinématique du point': [
        ('p', '4ZW49x6Fp2M', 'MPSI/PCSI Cinématique du point- utilisation des coordonnées polaires', ''),
        ('p', 'gV4arL3KRKQ', 'Cinématique du point matériel (2/3)', 'manege, mouvement circulaire'),
        ('p', 'pIaXG9hoVTw', 'Cinématique du point (3) - mouvement hélicoïdal en cylindriques', 'helicoidal, helice'),
        ('p', '8XGezhEEPUY', "Mécanique- référentiel, base de projection, c'est quoi la différence ?", 'base de projection, referentiel'),
    ],
    'Changement de référentiel': [
        ('p', 'aYRbzMnzr1A', 'Changement de référentiels : ce qu"il faut retenir', ''),
        ('p', 'Uj3kwOyagUk', 'Mécanique - Référentiel non galiléen en TRANSLATION : Les bases', 'translation'),
        ('p', 'qGK2r4qWwQI', "Force de Coriolis- déviation vers l'Est et autres tirs", 'coriolis'),
        ('p', 'wYkkhGZo0BQ', 'Référentiel non galiléen et énergie mécanique', 'energie'),
    ],
    'Principe fondamental de la dynamique': [
        ('p', 'wnZwh_04XC0', 'Mécanique "SOS projection des forces"', ''),
        ('p', 'y0yQpDGNnI8', "L' exo le plus important de la mécanique du point", 'pendule'),
        ('p', '1DOYYTIM5-g', "Mécanique du point : l'exo qui résume tout ! (1)", 'energie'),
    ],
    'Travail, puissance et énergie': [
        ('p', 'RTqckGjUDvI', 'Les 4 énergies potentielles à maîtriser parfaitement', ''),
        ('p', 'HG0oY2-pbFU', 'Comment utiliser efficacement les énergies potentielles en mécanique ?', 'energie mecanique, conservation'),
        ('p', '1DOYYTIM5-g', "Mécanique du point : l'exo qui résume tout ! (1)", ''),
    ],
    'Équilibre et stabilité': [
        ('p', 'HG0oY2-pbFU', 'Comment utiliser efficacement les énergies potentielles en mécanique ?', ''),
    ],
    'Oscillateur harmonique et amorti': [
        ('p', 'xJq9VrOg26A', 'MPSI/PCSI "SOS équa diff " : l\'oscillateur harmonique dévoilé', ''),
        ('p', 't-6ZjOihEiY', 'MPSI/PCSI "J\'aime pas les ressorts"', 'ressort, raideur'),
        ('p', 'y0yQpDGNnI8', "L' exo le plus important de la mécanique du point", 'pendule'),
        ('p', 'TkT_jHgDLNg', "Oscillations non harmoniques d'un pendule-Formule de Borda", 'borda, non harmonique, grande amplitude'),
        ('p', 'yTnX31IfxoY', 'PCSI-MPSI Corde vibrante (3/4) : Oscillations forcées-Résonance', 'forcees, resonance'),
        ('p', 'XPD4kE3TNMQ', 'MP-PC-PSI :Cours : Oscillations couplées - Modes propres.', 'couplees, couples'),
        ('p', 'eWHYnqvp8yI', '3 équations différentielles à maîtriser parfaitement en physique', 'amorti, pseudo periodique, aperiodique'),
    ],
    'Moment cinétique et forces centrales': [
        ('p', 'AaG6luwAbfM', 'Mécanique : Energie potentielle effective- utilité-limite (1/3)', ''),
        ('p', 'NxPahvhj7jI', 'Mécanique- "J\'aime pas les bras de levier" - Moment d\'une force', "moment d'une force, bras de levier"),
        ('p', 'bZ7a8xdybN4', 'Ellipses, paraboles, hyperboles : les propriétés des trajectoires en gravitation', 'kepler, ellipse, conique, trajectoire'),
        ('p', 'EBbx_gslKBM', "Mécanique - Freinage d'un satellite circulaire - oral Centrale", 'satellite'),
    ],
    'Gravitation universelle': [
        ('p', 'bZ7a8xdybN4', 'Ellipses, paraboles, hyperboles : les propriétés des trajectoires en gravitation', ''),
        ('p', 'XKyapPtB83s', 'Constante de gravitation- Oral Centrale MP/PSI/PC', 'constante de gravitation'),
        ('p', 'bFha7COPDNc', 'MP/PC/PSI-Electrostatique-Théorème de Gauss en gravitation- Pb à symétrie sphérique', 'theoreme de gauss'),
    ],
    'Optique géométrique': [
        ('p', 'phksmbx7ZC8', 'Quel rapport entre "Alerte à Malibu" et l\'optique géométrique ? Ppe de Fermat et lois de Descartes', ''),
        ('p', '0WqqLtnMdj0', 'MPSI/PCSI. Optique géométrique. Prisme/Minimum de déviation', 'prisme'),
        ('p', 'I7iNFh7fMsI', 'MPSI/PCSI Elargisseur de faisceau Laser- Optique géométrique', 'lentille, faisceau'),
    ],
    'Électrocinétique : lois de Kirchhoff': [
        ('p', '50kL-LeYy-E', 'Le pont diviseur de tension : un outil essentiel en électricité. Pourquoi ? Comment ?', ''),
        ('p', 'J5KLsenuppc', 'Electricité : le théorème de Thévenin. Pourquoi? Comment ?', 'thevenin, norton'),
        ('p', 'TL_98zHyXOM', 'Electrocinétique : Le théorème de Millman, utilité-difficultés- signification', 'millman'),
    ],
    'Circuits RC, RL et RLC': [
        ('p', '1OKN9AReZn0', "MPSI/PCSI. Electrocinétique. Régime transitoire d'ordre 1. Oscillations de relaxation", ''),
        ('p', 'Ir7y3VcLalo', 'Electricité : les régimes transitoires sans équation différentielle !', 'regime transitoire'),
        ('p', 'Uo60ksLUlzg', 'Utilisation efficace des complexes en électricité (2/2) : circuit R,L,C', 'rlc, sinusoidal'),
        ('p', 'eWHYnqvp8yI', '3 équations différentielles à maîtriser parfaitement en physique', 'equation differentielle'),
    ],
    'Régime sinusoïdal et impédances': [
        ('p', 'SBou-h2q1vA', 'Pourquoi on utilise les nombres complexes en physique ? les bases en électricité (1/2) :', ''),
        ('p', 'Uo60ksLUlzg', 'Utilisation efficace des complexes en électricité (2/2) : circuit R,L,C', 'rlc'),
        ('p', 'x5T7H7BYCl0', 'MPSI/PCSI-Filtrage linéaire(3/5)-fonction de transfert-diagramme de Bode', 'bode, fonction de transfert, filtre'),
        ('p', 'GsKSrAsJtFk', 'Comment construire et utiliser un diagramme de Fresnel en électrocinétique ?', 'fresnel'),
        ('p', 'S_Ij1fqAT1E', 'Les 3 formules de la puissance moyenne en régime sinusoïdal', 'puissance'),
    ],
    'Champ et potentiel électrostatiques': [
        ('p', 'zmkRKhLJmVE', 'MP/PC/PSI/PT Cours électrostatique. Théorème de Gauss (1/3)', ''),
        ('p', 'x0zhe3thgB8', 'La signification physique du gradient', 'gradient'),
    ],
    'Théorème de Gauss': [
        ('p', 'zmkRKhLJmVE', 'MP/PC/PSI/PT Cours électrostatique. Théorème de Gauss (1/3)', ''),
        ('p', 'AQ96B6anIY0', 'MP/PC/PSI Cours Electrostatique : Théorème de Gauss (2/3)', ''),
        ('p', 'bFha7COPDNc', 'MP/PC/PSI-Electrostatique-Théorème de Gauss en gravitation- Pb à symétrie sphérique', 'gravitation, spherique'),
    ],
    'Conducteurs et condensateurs': [
        ('p', 'gNGRI_HOqH8', 'MP/PC/PSI: Cours électrostatique/condensateurs plan et cylindrique', ''),
    ],
    'Dipôle électrostatique': [
        ('p', 'yIsl1qSI4nE', 'Dipôle électrostatique (1/3) : intérêt-définitions', ''),
        ('p', 'QJCrPdExv1U', 'Dipôle électrostatique (2/3) : potentiel et champ', 'potentiel, champ cree'),
        ('p', 'C7-6e6Dh29k', "Action d'un champ électrique sur un dipôle électrostatique (3/3)", 'champ exterieur, couple, energie potentielle'),
        ('p', '8dnib1hzgzk', 'Dipôle électrostatique induit- Polarisabilité- Atome de Thomson', 'induit, polarisabilite'),
    ],
    'Magnétostatique : Biot-Savart et Ampère': [
        ('p', 'Ity400O1xTo', 'MP/PC/PSI Cours Magnétostatique (1) : sources du champ, propriétés de symétrie', ''),
        ('p', 'KfAkhcvw95c', 'Magnétostatique - Formule de Biot et Savart- Champ magnétique créé par une spire', 'biot, spire'),
        ('p', 'TTQY6U0ACi4', "MP/PC/PSI Cours Magnétostatique (2) : Le théorème d'Ampère- analogie avec l'électrostatique", "theoreme d'ampere"),
        ('p', 'wFUi5RZztqI', "MP/PC/PSI-Cours Magnétostatique - Comment utiliser le théorème d'Ampère ?(1/5) Cas du fil infini", 'fil infini'),
        ('p', 'K3OnB0OYVW4', "MP/PSI/PC- Magnétostatique-Théorème d'ampère (2/5)- Cable coaxial", 'coaxial'),
        ('p', 'bjWj_eEkK3A', "MP/PC/PSI Magnétostatique -Théorème d'ampère (3/5)- champ B créé par un tore", 'tore'),
        ('p', 'JnE8WD0Eeik', "MP/PC/PSI Magnétostatique- Théorème d'ampère (4/5) Champ magnétique créé par un solénoïde infini", 'solenoide'),
    ],
    'Forces de Lorentz et de Laplace': [
        ('p', 'uUl6Q5Qedns', 'MPSI/PCSI Particule chargée dans un champ magnétique uniforme- centrale TSI 2005 (1/2)', ''),
        ('p', 'yHCkYBGPGy8', "MP/PC/PSI Électromagnétisme- L' effet Hall", 'effet hall'),
        ('p', 'p_XVrZaaMRo', 'MPSI/PCSI Induction de Lorentz : rails de Laplace', 'rails, force de laplace'),
    ],
    'Induction électromagnétique': [
        ('p', 'NXJY6ZWZmz0', 'Induction : spire en rotation dans un champ magnétique uniforme', ''),
        ('p', 'p_XVrZaaMRo', 'MPSI/PCSI Induction de Lorentz : rails de Laplace', 'rails'),
        ('p', '1NCW6Nvu7h0', 'Induction : régime transitoire dans des circuits couplés par inductance mutuelle', 'mutuelle'),
        ('p', 'Xz60rjIf5O8', 'Battements dans des circuits couplés par inductance mutuelle. Induction de Neumann (PCSI/MPSI/PTSI)', 'neumann'),
        ('p', 'if8vjs1MiJ4', 'Cours : Le transformateur (1), cas idéal', 'transformateur'),
    ],
    'Opérateurs gradient, divergence, rotationnel': [
        ('p', '4xv0TgFozD4', "Nabla, l'outil essentiel pour le gradient, la divergence, le rotationnel...", ''),
        ('p', 'x0zhe3thgB8', 'La signification physique du gradient', 'gradient'),
        ('p', 'ToO8Tlu0gfI', 'La signification physique de la divergence', 'divergence'),
        ('p', 'a7uMhsRw-mI', 'La signification physique du rotationnel', 'rotationnel'),
    ],
    "Ondes progressives et équation de d'Alembert": [
        ('p', 'EtJjCXH8eYI', "PC/PSI-Physique des ondes-corde vibrante (1/4)- équation de d'Alembert", ''),
        ('p', 'lzpkL01hNps', "Cours physique PC/PSI: l'équation des ondes le long d'une chaîne infinie d'oscillateurs", 'chaine, oscillateurs couples'),
        ('p', 'R43hFqFa5jc', "PC-PSI-MP Vitesse de phase /Vitesse de groupe/dispersion d'un paquet d'onde", "vitesse de groupe, vitesse de phase, dispersion, paquet d'onde"),
        ('p', '79GdoNkNFIY', 'Ondes stationnaires- ondes progressives- simulation/explications', 'onde stationnaire'),
    ],
    'Ondes stationnaires': [
        ('p', 'NsITAaCC6k8', "PC-PSI-MP Cours : Ondes stationnaires et modes propres corde d'une corde", ''),
        ('p', '79GdoNkNFIY', 'Ondes stationnaires- ondes progressives- simulation/explications', 'onde progressive'),
        ('p', '4JNsnz9usCI', 'Corde de Melde- résonance-simulation/animation', 'melde'),
        ('p', 'j9F5wNCoeW0', 'Tuyaux sonores(1/2) Ondes stationnaires-Modes propres- Animation', 'tuyau'),
        ('p', 'UsZ-A_O_gT8', 'Corde pincée de guitare (1/2): décomposition en modes propres', 'guitare, pincee'),
    ],
    'Interférences et diffraction': [
        ('p', '9RifDT3eMy4', 'Interférences lumineuses à deux ondes : les bases (1)', ''),
        ('p', 'OGjsHfrWgYQ', "Trous d'Young- Comment calculer la différence de marche de 3 façons différentes ?", 'young, difference de marche'),
        ('p', 'FiEJrfkQ48A', "Optique: les bases (3). Les fentes d'Young à l'infini. Montage de Fraunhofer", 'fraunhofer'),
        ('p', 'iEcw8I-_ty4', "Interféromètre de Michelson (1/5) : les trois configurations qu'il faut retenir", 'michelson'),
        ('p', 'rN7UpLISafg', 'Interférences lumineuses : cohérence temporelle et contraste', 'coherence, contraste'),
        ('p', 'sEKWHIl9t1U', 'Cours : réseaux de diffraction(1) :Présentation- Formule fondamentale', 'reseau'),
        ('p', 'C5z5mkTTh-w', 'Cours de physique : diffraction/optique de Fourier (1/3)', 'diffraction'),
    ],
    'Effet Doppler et battements': [
        ('p', 'lfwQdUNR4EA', 'MPSI/PCSI - Battements en physique- Lien entre physique en maths', ''),
    ],
    'Ondes électromagnétiques et polarisation': [
        ('p', 'HB8P6Btl8iY', 'Ondes électromagnétiques dans le vide- corrigé E3A Physique PC 2005 (1/3)', ''),
        ('p', '_q3GbvYRRyI', 'MP/PC/PSI-Cours optique physique - Polarisation de la lumière (1/10): les états de polarisation', 'polarisation'),
        ('p', '85FfuBHuJ18', "Bilan d'énergie électromagnétique - vecteur de Poynting", 'poynting'),
        ('p', 'G6w5Akgl3qg', "Propagation d'une onde électromagnétique dans un plasma-Mines Physique 1 2015-Toutes filières", 'plasma'),
    ],
    'Effet photoélectrique et photons': [
        ('p', 'bLu4qqJKWq4', "MP/PC - Quantique- L' effet photoélectrique/mesure de la constante de Planck - Centrale MP", ''),
    ],
    'Dualité onde-corpuscule': [
        ('p', '_caf1ADM3xk', "MP/PC- Mécanique quantique- Inégalités d'Heisenberg - Einstein vs Bohr-Centrale MP", ''),
        ('p', 'eDRTlin_75s', "Quantique - Interférences d'ondes de matière - principe de superposition", 'de broglie, interference, ondes de matiere'),
        ('p', 'V0VlX2n7E10', 'Quantique- énergie de confinement et inégalité de Heisenberg', 'confinement'),
    ],
    'Équation de Schrödinger': [
        ('p', 'TUaZBdZSVto', "Quantique - D'où vient l'équation de Schrödinger?", ''),
        ('p', '4jfT10FMTFQ', 'Mécanique quantique- Puits infini - MP/PC', 'puits infini'),
        ('p', 'Y3jxeo2nBiI', "MP/PC - Mécanique quantique- états liés d'un puits fini", 'puits fini'),
        ('p', 'NGLUL7aLhbU', "MP/PC Mécanique quantique (1/3) : l'effet tunnel. Corrigé Mines Ponts Physique 2 PC 2016", 'effet tunnel'),
        ('p', '4u4uNxRI4pU', 'Potentiel harmonique quantique- Simulation/explications', 'harmonique'),
        ('p', 'mB6eAFbVYgc', 'Quantique : états non stationnaires- oscillations quantiques', 'non stationnaire'),
    ],
    'Modèle de Bohr et spectres atomiques': [
        ('p', '_1ohXZN1c4A', 'Corrigé Centrale PC 2018 Phys 2. partie 1. Atome de Bohr et structure hyperfine', ''),
    ],
    'Radioactivité et physique nucléaire': [
        ('p', 'DlU5Lm21Ch4', 'MP/PC : radioactivité alpha/effet tunnel (3/3) , corrigé Mines Ponts physique 2016 PC', ''),
    ],
}

DOMAINS = {
    "math": "algebre1 algebre2 algebre-lineaire algebre analyse1 analyse2 analyse-rn series integration-proba complement-maths mesures-integration probabilites optimisation optimisation-deterministe analyse-numerique equations-differentielles statistique-inferentielle modele-lineaire edp series-temporelles compressive-sensing data-exploration data-mining",
    "info": "informatique1 informatique2 informatique3 informatique4 algorithmique bdd programmation-procedurale programmation-fonctionnelle programmation-parallele unix systeme-exploitation theorie-graphes theorie-langages decidabilite-complexite architecture-reseau ia methodes-agiles data-exploration data-mining",
    "phys": "physique1 mecanique-du-point electromagnetisme ondes physique-moderne traitement-signal",
}
# le traitement du signal relève aussi des maths (Fourier, convolution, échantillonnage)
DOMAINS["math"] += " traitement-signal"
DOMAIN_OF = {}
for _domain, _ids in DOMAINS.items():
    for _id in _ids.split():
        DOMAIN_OF.setdefault(_id, set()).add(_domain)

ING_PREFIX_RE = re.compile(r"^(?:ing-1-s\d-(?:gm|info|data)|ing-\d(?:-s\d)?)-")


def course_domains(course):
    """Domaines d'une matière ; aucun (SHS, éthique, anglais…) = pas de vidéo."""
    return DOMAIN_OF.get(ING_PREFIX_RE.sub("", course), set())


COMBINING_RE = re.compile(r"[\u0300-\u036f]")
SEPARATOR_RE = re.compile(r"[^a-z0-9'(),=^{}+_/]+")


def normalize(text):
    """minuscules sans accents ; tirets, symboles et blancs -> une espace."""
    text = text.lower().replace("’", "'").replace("‘", "'").replace("œ", "oe")
    return SEPARATOR_RE.sub(" ", COMBINING_RE.sub("", unicodedata.normalize("NFD", text)))


def _trie_pattern(words):
    """Expression régulière en arbre : bien plus rapide qu'une alternative par mot-clé.
    words : {mot-clé: entier ?} ; à chaque nœud, la suite la plus longue est essayée d'abord."""
    trie = {}
    for word, whole in words.items():
        node = trie
        for ch in word:
            node = node.setdefault(ch, {})
        node[""] = node.get("", False) or whole

    def build(node):
        alts = [re.escape(ch) + build(child) for ch, child in sorted(node.items()) if ch]
        if "" in node:
            alts.append(r"\b" if node[""] else "")
        if len(alts) == 1 and len(node) == 1:
            return alts[0]
        return "(?:" + "|".join(alts) + ")"

    return build(trie)


def _compile():
    owners = {}  # mot-clé (normalisé) -> indices des notions
    whole = {}
    for i, (_, _, keywords, *_rest) in enumerate(NOTIONS):
        for kw in keywords.split(", "):
            key = normalize(kw.rstrip("$")).strip()
            owners.setdefault(key, set()).add(i)
            # même mot-clé entier pour une notion, début de mot pour une autre : début de mot
            whole[key] = kw.endswith("$") and whole.get(key, True)
    return re.compile(r"\b" + _trie_pattern(whole)), owners


KEYWORD_RE, KEYWORD_NOTIONS = _compile()
NOTION_DOMAINS = [set(domains.split()) for _, domains, *_ in NOTIONS]


CHANNELS = {"m": "Maths Adultes", "p": "E-learning physique"}
_NOTION_INDEX = {notion[0]: i for i, notion in enumerate(NOTIONS)}
assert set(VIDEOS) <= set(_NOTION_INDEX), set(VIDEOS) - set(_NOTION_INDEX)
VIDEO_CHOICES = {
    _NOTION_INDEX[notion]: [(channel, vid, title, [normalize(k).strip() for k in keywords.split(", ") if k])
                            for channel, vid, title, keywords in vids]
    for notion, vids in VIDEOS.items()
}


def notion_hits(text, normalized=False):
    """-> Counter {indice de notion: nombre d'occurrences de ses mots-clés}."""
    hits = Counter()
    for kw in KEYWORD_RE.findall(text if normalized else normalize(text)):
        for i in KEYWORD_NOTIONS[kw]:
            hits[i] += 1
    return hits


def search_url(notion, kind):
    query = NOTIONS[notion][3] if len(NOTIONS[notion]) > 3 else NOTIONS[notion][0]
    suffix = "exercice corrigé" if kind in EXERCISE_KINDS else "cours"
    return "https://www.youtube.com/results?search_query=" + quote_plus(f"{query} {suffix}")


def link(notion, kind, text):
    """Vidéo de la notion la plus proche du passage (texte normalisé), sinon recherche YouTube."""
    choices = VIDEO_CHOICES.get(notion)
    if not choices:
        return {"notion": NOTIONS[notion][0], "url": search_url(notion, kind), "title": None, "channel": None}
    # à égalité (souvent : aucun mot-clé présent), la première vidéo de la liste
    k = max(range(len(choices)), key=lambda k: (sum(text.count(kw) for kw in choices[k][3]), -k))
    channel, vid, title, _ = choices[k]
    return {"notion": NOTIONS[notion][0], "url": f"https://www.youtube.com/watch?v={vid}",
            "title": title, "channel": CHANNELS[channel]}


def annotate(chunks):
    """Ajoute à chaque passage `_videos` : [{"notion", "url", "title", "channel"}], au plus
    MAX_VIDEOS, les notions les plus caractéristiques du passage en premier
    (title et channel valent None pour une recherche YouTube)."""
    found = []
    texts = []
    df = Counter()
    for c in chunks:
        domains = course_domains(c.get("course", ""))
        if not domains:
            found.append(Counter())
            texts.append("")
            continue
        text = normalize(c.get("text", ""))
        texts.append(text)
        hits = notion_hits(text, normalized=True)
        # le titre (section, document) compte triple : il nomme souvent la notion
        for i, n in notion_hits(f"{c.get('section', '')} {c.get('doc_label', '')}").items():
            hits[i] += 3 * n
        hits = Counter({i: n for i, n in hits.items() if NOTION_DOMAINS[i] & domains})
        found.append(hits)
        df.update(hits.keys())
    total = len(chunks)
    previous = None
    for c, hits, text in zip(chunks, found, texts):
        scored = sorted(((min(n, 6) * math.log((1 + total) / (1 + df[i])), i) for i, n in hits.items()),
                        reverse=True)
        links = {}
        for _, i in scored:
            found_link = link(i, c.get("kind"), text)
            links.setdefault(found_link["url"], found_link)  # même vidéo pour deux notions : une fois
            if len(links) == MAX_VIDEOS:
                break
        c["_videos"] = list(links.values())
        # suite d'un exercice coupé en plusieurs passages : mêmes vidéos que son début
        if not c["_videos"] and previous and previous.get("doc") == c.get("doc") \
                and previous.get("section") == c.get("section"):
            c["_videos"] = previous["_videos"]
        previous = c
    return chunks
