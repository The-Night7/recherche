# -*- coding: utf-8 -*-
"""
Vidéos liées à chaque passage (exercice, partie de cours…).

Chaque notion du catalogue a des mots-clés ; un passage est relié aux
notions dont les mots-clés apparaissent dans son texte (ou son titre),
pondérées comme en TF-IDF : une notion présente partout (« matrice »)
pèse moins qu'une notion rare (« Cayley-Hamilton »). Le lien ouvre une
recherche YouTube ciblée : « <notion> cours » pour un cours,
« <notion> exercice corrigé » pour un TD/DS/CC/QCM.

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


def notion_hits(text):
    """-> Counter {indice de notion: nombre d'occurrences de ses mots-clés}."""
    hits = Counter()
    for kw in KEYWORD_RE.findall(normalize(text)):
        for i in KEYWORD_NOTIONS[kw]:
            hits[i] += 1
    return hits


def search_url(notion, kind):
    query = NOTIONS[notion][3] if len(NOTIONS[notion]) > 3 else NOTIONS[notion][0]
    suffix = "exercice corrigé" if kind in EXERCISE_KINDS else "cours"
    return "https://www.youtube.com/results?search_query=" + quote_plus(f"{query} {suffix}")


def annotate(chunks):
    """Ajoute à chaque passage `_videos` : [{"notion", "url"}], au plus MAX_VIDEOS,
    les notions les plus caractéristiques du passage en premier."""
    found = []
    df = Counter()
    for c in chunks:
        domains = course_domains(c.get("course", ""))
        if not domains:
            found.append(Counter())
            continue
        hits = notion_hits(c.get("text", ""))
        # le titre (section, document) compte triple : il nomme souvent la notion
        for i, n in notion_hits(f"{c.get('section', '')} {c.get('doc_label', '')}").items():
            hits[i] += 3 * n
        hits = Counter({i: n for i, n in hits.items() if NOTION_DOMAINS[i] & domains})
        found.append(hits)
        df.update(hits.keys())
    total = len(chunks)
    previous = None
    for c, hits in zip(chunks, found):
        scored = sorted(((min(n, 6) * math.log((1 + total) / (1 + df[i])), i) for i, n in hits.items()),
                        reverse=True)
        c["_videos"] = [{"notion": NOTIONS[i][0], "url": search_url(i, c.get("kind"))}
                        for _, i in scored[:MAX_VIDEOS]]
        # suite d'un exercice coupé en plusieurs passages : mêmes vidéos que son début
        if not c["_videos"] and previous and previous.get("doc") == c.get("doc") \
                and previous.get("section") == c.get("section"):
            c["_videos"] = previous["_videos"]
        previous = c
    return chunks
