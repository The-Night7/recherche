# cours proba ing1 gm 2425 - sans annotations.docx

[Ouvrir l’original](https://drive.google.com/open?id=1AZe7gmUOwiHCn4VN65IURlg5YwbBUEwz) · Texte structuré depuis le fichier original. Les mises en page complexes peuvent nécessiter une vérification.

A K TA R YA L Ç I N

P R O B A B I L I T É S

C Y T E C H I N G 1 - G M 2 0 2 4 C Y T E C H

> *Table des matières*
>
> *1. Axiomes de Probabilités* 5
>
> *2. Probabilités conditionnelles et indépendance et Probabilités sur un espace fini ou dénombrable* 11
>
> *3. Variables aléatoires sur un espace fini ou dénombrable et Construction d’une mesure de probabilité* 15
>
> *4. Probabilités sur* **R** *et fonctions de répartition* 21
>
> *5. Intégration par rapport à une mesure de probabilité (espérance, variance)* 25
>
> *6. Variables aléatoires indépendantes et Lois de probabilités sur* **R** 29 *7. Fonctions caractéristiques et quelques propriétés* 39
>
> *8. Sommes de variables aléatoires indépendantes et Variables aléatoires gaus siennes* 41
>
> *9. Convergence des variables aléatoires, convergence en loi et applications avec fonctions caractéristiques* 45
>
> 4
>
> *10. Loi des grands nombres et le théorème-limite central* 51 *Bibliographie* 53
>
> *1. Axiomes de Probabilités*
>
> Soit Ω un espace abstrait, i.e. sans structure particulière. Rappelons que *P*(Ω) ou 2<sup>Ω</sup> désigne l’ensemble de tous les sous ensembles de Ω, y compris le sous-ensemble vide noté ∅.
>
> **Définition 1 (tribu (ou** *σ***-algèbre))** *Une partie A ⊆ P*(Ω) *est appelée tribu (ou σ-algèbre) sur* Ω *si elle vérifie les propriétés suivantes :* (1) Ω *∈ A*
>
> \(2\) *A est stable par complémentaire i.e. si A ∈ A alors A<sup>c</sup> ∈ A, où A<sup>c </sup>*= Ω *\\ A.*
>
> \(3\) *A est stable par union dénombrable i.e. si pour tout i ∈* **N***<sup>∗</sup>, A<sub>i</sub> ∈ A,*

*alors* <sup>S</sup> *i∈***N***<sup>∗</sup>*

*A<sub>i</sub> ∈ A.*

> Dans la définition d’une algèbre d’ensembles, "dénombrable" est
>
> remplacé par "finie". En théorie des probabilités, le couple (Ω, *A*) est
>
> appelé espace probabilisable (contrairement à "espace mesurable").
>
> **Exemple 1** *1) La tribu dite grossière : A* = *{*∅, Ω*}.*
>
> *2) La tribu discrète : A* = *P*(Ω)*.*
>
> *3) Si* Ω = *{ω*<sub>1</sub>, *ω*<sub>2</sub>, *ω*<sub>3</sub>, *ω*<sub>4</sub>*} alors A* = *{*∅, *{ω*<sub>1</sub>*}*, *{ω*<sub>2</sub>, *ω*<sub>3</sub>, *ω*<sub>4</sub>*}*, Ω*} est*
>
> *une tribu sur* Ω*.*
>
> *4) A* = *{A ∈ P*(Ω) *t.q. A ou A<sup>c</sup>est dénombrable} est une tribu sur* Ω dans ce dernier exemple, si on change "dénombrable" en "fini" cela devient
>
> **Définition 2 (tribu engendrée)** *Si C ⊂ P*(Ω)*, la tribu engendrée par C* une algèbre mais pas une *σ*-algèbre. *et notée par σ*(*C*) *est la plus petite tribu contenant C. C’est-à-dire*

*σ*(*C*) = <sup>\\</sup> *A tribu t.q.*

*C⊂A*

*A*.

> Remarque : l’intersection d’une famille *quelconque* de tribus est encore une tribu et l’intersection ci-dessus n’est pas vide, car il y a au moins *A* = *P*(Ω).
>
> **Exemple 2** *Si A ⊂* Ω*, alors σ*(*A*) = *{*∅, *A*, *A<sup>c</sup>*, Ω*}.*
>
> *Si* Ω = **R** *(ou plus généralement si* Ω *est un espace topologique), la tribu borélienne, ou de Borel est la tribu B*(**R**) *engendrée par la classe des ouverts (ou de manière équivalente, par la classe des fermés) ; une partie de* **R** *qui est dans la tribu borélienne s’appelle un borélien.*
>
> 6
>
> **Théorème 1** *B*(**R**) = *σ*( <sub>\] *−* ∞, *a*\], *a ∈* **Q**</sub> )*.*
>
> **Définition 3 (Mesure de Probabilité)** *Une mesure de probabilité, ou simplement une probabilité, définie sur une tribu A d’un espace* Ω*, est une application* **P** : *A →* \[0, 1\] *qui vérifie :*
>
> *1.* **P**(Ω) = 1*.*
>
> *2. Pour toute suite A*<sub>1</sub>*, A*<sub>2</sub>*, A*<sub>3</sub>*,* . . . *d’éléments de A (des événements) qui sont deux à deux disjoints (i.e. A<sub>n</sub> ∩ A<sub>m </sub>*= ∅ *si n ̸*= *m), on a*

**P**

<sub>\[</sub>∞ *n*=1

*A<sub>n</sub>*

=

∞

∑

*n*=1

**P**(*A<sub>n</sub>*).

> Le nombre **P**(*A*) s’appelle la probabilité de l’événement *A*. Le point 2. s’appelle *σ*-additivité de **P**.
>
> **Théorème 2** *Si* **P** *est une probabilité sur la tribu A, alors : (i)* **P**(∅) = 0 *;*
>
> *(ii) si A*, *B ∈ A tels que A ∩ B* = ∅*, alors* **P**(*A ∪ B*) = **P**(*A*) + **P**(*B*) *(condition d’ additivité).*
>
> Voici deux conséquences immédiates de l’additivité et de l’axiome **P**(Ω) = 1 :
>
> **Propriété 1** *1. A ∈ A ⇒* **P**(*A<sup>c</sup>*) = 1 *−* **P**(*A*)
>
> *2. A*, *B ∈ A*, *A ⊂ B ⇒* **P**(*A*) *≤* **P**(*B*)
>
> *Preuve:*
>
> 1\. Utiliser l’additivité avec *A*, *A<sup>c</sup>*et **P**(Ω) = 1.
>
> 2\. Utiliser l’additivité avec *A* et *C* := *A<sup>c</sup> ∩ B*.

□

> **Définition 4** *Soient A un ensemble et* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite d’ensembles. On note* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗↘A et on dit que* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ décroît (ou "tend en décroissant") vers A si A<sub>n</sub>*<sub>+1</sub>*⊂A<sub>n</sub> pour tout n ∈* **N***<sup>∗</sup>et si* <sup>T</sup>*n∈***N***<sup>∗ A</sup><sub>n </sub>*= *A. On note* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗↗A et on dit que* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ croît (ou "tend en croissant") vers A si A<sub>n</sub>⊂A<sub>n</sub>*<sub>+1</sub> *pour tout n ∈* **N***<sup>∗</sup>et si* <sup>S</sup>*n∈***N***<sup>∗ A</sup><sub>n </sub>*= *A.*
>
> Remarque : si les *A<sub>n</sub>*, *n ∈* **N***<sup>∗</sup>*sont dans la tribu *A*, il en est de même de *A* dans les deux cas ci-dessus (propriété de *σ*-algèbre de *A*). Le théorème ci-dessous exprime ce qu’il faut exactement ajouter à l’additivité pour obtenir la *σ*-additivité :
>
> **Théorème 3** *Soit A une tribu sur* Ω*. Supposons que* **P** : *A →* \[0, 1\] *satisfasse l’axiome 1 (i.e.* **P**(Ω) = 1*) et soit additive.*
>
> *Les assertions suivantes sont alors équivalentes :*

7

> *(i) on a l’axiome2 (i.e.σ-additivité) ;*
>
> *(ii) si*(*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ A*<sup>**N***∗*</sup>*et décroit vers*∅ *alors***P**(*A<sub>n</sub>*)*↘*0*.*
>
> *(iii) si*(*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ A*<sup>**N***∗*</sup>*et décroit vers A alors***P**(*A<sub>n</sub>*)*↘***P**(*A*)*.*
>
> *(iv) si*(*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ A*<sup>**N***∗*</sup>*et croît vers*Ω *alors***P**(*A<sub>n</sub>*)*↗*1*.*
>
> *(v) si*(*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ A*<sup>**N***∗*</sup>*et croît vers A alors***P**(*A<sub>n</sub>*)*↗***P**(*A*)*.*
>
> *Preuve:* Observons que*A<sub>n</sub>↘A* implique*A<sup>c</sup><sub>n</sub>↗A<sup>c</sup>*. Comme
>
> **P**(*A<sup>c</sup><sub>n</sub>*) =1*−***P**(*A<sub>n</sub>*) et**P**(*A<sup>c</sup>*) =1*−***P**(*A*), on voit que (ii) et (iv) sont
>
> équivalents, ainsi que (iii) et (v). L’implication (v)*⇒* (iv) est évidente.
>
> Supposons maintenant (iv). Soit*A<sub>n</sub> ∈ A* avec*A<sub>n</sub>↗A*. Posons
>
> *B<sub>n</sub>*=*A<sub>n</sub>∪A<sup>c</sup>*. Alors(*B<sub>n</sub>*) croît versΩ, de sorte que**P**(*B<sub>n</sub>*)*↗*1.
>
> Comme*A<sub>n</sub>⊂A*, on a*A<sub>n</sub>∩A<sup>c</sup>*=∅, donc**P**(*A<sub>n</sub>∪A<sup>c</sup>*) =**P**(*A<sub>n</sub>*) +
>
> **P**(*A<sup>c</sup>*) et il vient1= lim <sub>*n→*+∞</sub>**P**(*B<sub>n</sub>*) = lim <sub>*n→*+∞</sub>(**P**(*A<sub>n</sub>*) +**P**(*A<sup>c</sup>*)). Par suite,
>
> <sub>*n→*+∞</sub>**P**(*A<sub>n</sub>*) =1*−***P**(*A<sup>c</sup>*) =**P**(*A*), et on a (v).
>
> lim
>
> Il reste à montrer que (i) et (v) sont équivalents. Supposons
>
> d’abord (v). Soit des*A<sub>n</sub> ∈ A* deux à deux disjoints, et définissons
>
> *B<sub>n</sub>*=<sup>S*n*</sup><sub>*p*=1</sub>*A<sub>p </sub>*et*B*=<sup>S∞</sup><sub>*n*=1</sub>*A<sub>n</sub>*. L’additivité implique**P**(*B<sub>n</sub>*) =
>
> ∑*<sup>n</sup><sub>p</sub>*<sub>=1</sub>**P**(*A<sub>p</sub>*) qui croît vers∑<sup>∞</sup><sub>*p*=1</sub>**P**(*A<sub>p</sub>*) quand*n→*∞ et croît aussi
>
> vers**P**(*B*) par (v), donc**P**(*B*) =**P**(<sup>S∞</sup><sub>*n*=1</sub>*A<sub>n</sub>*) =∑<sup>∞</sup><sub>*n*=1</sub>**P**(*A<sub>n</sub>*), et (i) est
>
> prouvé.
>
> Finalement, supposons (i). Soit*A<sub>n</sub> ∈ A*, avec*A<sub>n </sub>*croissant vers
>
> *A*. On construit une nouvelle suite d’éléments de*A* avec*B*<sub>1</sub>=*A*<sub>1</sub>,
>
> *B<sub>n</sub>*=*A<sub>n</sub>\A<sub>n−</sub>*<sub>1</sub>=*A<sub>n</sub>∩A<sup>c</sup><sub>n−</sub>*<sub>1</sub>. On a<sup>S∞</sup><sub>*n*=1</sub>*B<sub>n</sub>*=*A* et les(*B<sub>n</sub>*)<sub>*n≥*1</sub> sont
>
> deux à deux disjoints. Donc (i) entraine**P**(*A*) = lim<sub>*n→*∞</sub>∑*<sup>n</sup><sub>p</sub>*<sub>=1</sub>**P**(*B<sub>p</sub>*). On
>
> a aussi∑*<sup>n</sup><sub>p</sub>*<sub>=1</sub>**P**(*B<sub>p</sub>*) =**P**(*A<sub>n</sub>*), donc lim<sub>*n→*∞</sub>**P**(*A<sub>n</sub>*) =**P**(*A*) et on a(*v*).□
>
> Si*A* est une partie deΩ, on définit sa fonction indicatrice par
>
> **1***<sub>A</sub>*(*ω*) =1 si*ω∈A* et**1***<sub>A</sub>*(*ω*) =0 si*ω ̸∈A*. Notez qu’une fonction
>
> indicatrice**1***<sub>A</sub>* est*F*-mesurable si et seulement si*A ∈ F*. On associe
>
> aussi à toute suite(*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗* de parties deΩ les ensembles suivants :

lim sup *n→*∞

<sup>déf</sup> =<sup>\\</sup>*n*=1

\[

*m≥n*

*A<sub>m</sub>*=:*A<sup>∗</sup>*; lim inf <sub>*n→*∞</sub><sup>déf</sup> =<sup>\[∞</sup><sub>*n*=1</sub>\\*<sub>m≥n</sub>A<sub>m</sub>*=:*A<sub>∗</sub>*.

> **Propriété2***A<sub>∗</sub>⊂A<sup>∗</sup>et si*(*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ A*<sup>**N***∗*</sup>*alors A<sub>∗</sub>*,*A<sup>∗</sup> ∈ A*. Les règles élémentaires sur*∪*,*∩* et la complémentarité, donnent sans difficulté
>
> (*A<sup>∗</sup>*)*<sup>c</sup>* = (*A<sup>c</sup>*)*<sub>∗</sub>*.
>
> De plus,*A<sup>∗</sup>*et*A<sub>∗ </sub>*ont les interprétations suivantes : **Propriété3** *Soit*(*A<sub>i</sub>*)<sub>*i∈***N **</sub>*une collection infinie d’ensembles. Alors i)ω∈A<sub>∗</sub>⇔ "à partir d’un certain rang,ω est dans tous les A<sub>i</sub>". ii)ω∈A<sup>∗</sup>⇔"ω est dans une infinité de A<sub>m</sub>".*
>
> *On écrit parfois{A<sub>m</sub>i*.*s*.*} où i*.*s*. *signifie "infiniment souvent".*
>
> 8
>
> *Preuve:*
>
> i\) Soit *ω* qui, à partir d’un certain rang, est dans tous les *A<sub>m</sub>*. On traduit cela de la façon suivante (qui est une équivalence) : il existe un rang *n ≥* 1 tel que pour tout *m ≥ n*, *ω* est dans *A<sub>m</sub>*. D’après la signification des symboles *∀*, *∃*, *∩* et *∪*, cela revient à écrire

*ω ∈*<sup>\[</sup> *n≥*1

\|{z}

il existe

*n≥*1

\\

*m≥n*

\|{z} pour tout *m≥n*

*A<sup>m </sup>*\|{z}

*ω* est

dans *A<sub>m</sub>*

.

> ii\) Dire que *ω* est dans une infinité de *A<sub>m </sub>*est équivalent à dire que " pour tout *n*, il existe *m ≥ n* avec *ω* dans *A<sub>m</sub>*”.
>
> En effet, si tel est le cas, *ω* est bien dans une infinité de *A<sub>m </sub>*car, d’après cette propriété,
>
> \- avec *n* = 1, il existe *m*<sub>1</sub> *≥ n* tel que *ω* est dans *A<sub>m</sub>*<sub>1</sub>, *m*<sub>1</sub> *≥* 1. - avec *n* = *m*<sub>1</sub> + 1, il existe *m*<sub>2</sub> *≥ n* tel que *ω* est dans *A<sub>m</sub>*<sub>2</sub>, *m*<sub>2</sub> strictement plus grand que *m*<sub>1</sub>,
>
> \- avec *n* = *m*<sub>2</sub> + 1, il existe *m*<sub>3</sub> *≥ n* tel que *ω* est dans *A<sub>m</sub>*<sub>3</sub>, *m*<sub>3</sub> strictement plus grand que *m*<sub>2</sub>,
>
> \- . . .,
>
> \- avec *n* = *m<sub>k </sub>*+ 1, il existe *m<sub>k</sub>*<sub>+1</sub> *≥ n* tel que *ω* est dans *A<sub>mk</sub>*<sub>+1</sub>, *m<sub>k</sub>*<sub>+1</sub> strictement plus grand que *m<sub>k</sub>*.,
>
> \- . . .,
>
> et finalement, *ω* est dans chaque *A<sub>mk</sub>*avec (*m<sub>k</sub>*)<sub>*k∈***N**</sub>*∗* strictement croissante, c’est-à-dire dans une infinité de *A<sub>m</sub>*.
>
> Réciproquement, s’il est dans une infinité de *A<sub>i</sub>*, alors il existe une suite d’entiers positifs (*i<sub>k</sub>*)<sub>*k≥*1</sub>tel que *ω ∈ A<sub>ik</sub>*pour tout *k ∈* **N***<sup>∗</sup>*. Donc sachant que pour tout *k ∈* **N***<sup>∗</sup>*, *i<sub>k</sub> ≥ k*, il vient que pour tout *n ∈* **N***<sup>∗</sup>* il existe *m ≥ n* tel que *ω ∈ A<sub>m</sub>*, et ce *m* peut être choisi tel que *m* = *i<sub>p</sub>* avec *p ≥ n*.
>
> Donc, pour ce deuxième point, pour tout *n*, on trouve *m ≥ n*, tel que *ω ∈ A<sub>q</sub>*, en langage *∀*, *∃*, cela s’écrit

*ω ∈*<sup>\\</sup> *n≥*1

\|{z}

pour tout

*n≥*1

\[

*m≥n* \|{z} il existe *m≥n*

*A<sup>m </sup>*\|{z}

*ω* est

dans *A<sub>m</sub>*

.

□

> **Lien entre** lim inf**,** lim sup **d’ensembles et de fonctions**

9

> Rappel : Pour une suite réelle *u* = (*u<sub>n</sub>*)<sub>*n∈***N**</sub>, on définit ses limites
>
> supérieur et inférieure par
>
> *u<sub>∗ </sub>*:= lim inf

<sub>*n→*+∞</sub>*u<sub>n </sub>*= sup *n≥*0

*<sub>k≥n</sub>u<sub>k</sub>* inf

*u<sup>∗</sup>*:= lim sup *n→*+∞

*u<sub>n </sub>*= inf

<sub>*n≥*0</sub>sup

*k≥n*

*u<sub>k</sub>*

> Ce sont les plus petite et plus grande valeurs d’adhérence de la suite *u*. On a toujours
>
> *u<sub>∗</sub> ≤ u<sup>∗</sup>*
>
> et il y a égalité ssi la suite *u* converge ; de plus si tel est le cas lim<sub>*n→*+∞</sub> *u<sub>n </sub>*= *u<sub>∗ </sub>*= *u<sup>∗</sup>*. En plus, en changeant le signe, les limites inférieure et supé rieure s’échangent :
>
> (*−u*)*<sup>∗</sup>* = *−u<sub>∗</sub>*
>
> (*−u*)*<sub>∗</sub>* = *−u<sup>∗</sup>*.
>
> Pour une suite de fonctions (*f<sub>n</sub>*)<sub>*n≥*0</sub>, on définit des fonctions limites inférieure et supérieure de la façon suivante :
>
> <sub>*n→*+∞</sub>*f<sub>n</sub>*(*x*), *f<sup>∗</sup>*(*x*) = lim sup

*f<sub>∗</sub>*(*x*) = lim inf

*n→*+∞

*f<sub>n</sub>*(*x*).

> **Propriété 4** *Soit* (*A<sub>n</sub>*)<sub>*n∈***N **</sub>*une suite d’ensemble mesurables, on a* (**1***<sub>A</sub>*)*<sub>∗</sub>* = **1***<sub>A∗</sub>et* (**1***<sub>A</sub>*)*<sup>∗</sup>* = **1***<sub>A</sub>∗* .
>
> *Preuve:* la démonstration complète est à faire soi-même. Pour vous aider : montrer que (**1***<sub>A</sub>*)*<sup>∗</sup>* = **1***<sub>A</sub>∗* revient, par définition et notation, à montrer que (**1***<sub>A</sub>*(*ω*))*<sup>∗</sup>* = **1***<sub>A</sub>∗* (*ω*), qui est équivalent à

<sub>*n≥*1</sub>sup

inf

*m≥n*

**1**<sub>*Am*(*ω*) = **1**</sub> <sub>T*n≥*1</sub>S*<sub>m≥n</sub> A<sub>m</sub>* (*ω*).

□

> **Définition 5 (Convergence d’ensembles)** *On dit qu’une suite d’en semble* (*A<sub>n</sub>*)<sub>*n∈***N **</sub>*converge vers A et on note A<sub>n</sub> → A, n →* +∞*, si A<sup>∗ </sup>*= *A<sub>∗ </sub>*= *A*.
>
> On montre alors aussi :
>
> **Propriété 5** *Soit* **P** *une probabilité et* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ A*<sup>**N***∗*</sup>*qui converge vers A. Alors A ∈ A et* lim<sub>*n→*∞</sub>**P**(*A<sub>n</sub>*) = **P**(*A*)*.*
>
> *Preuve:* D’après la Propriété 2, on a *A<sub>∗ </sub>*= *A<sup>∗</sup> ∈ A*, et donc d’après la définition précédente *A ∈ A*.
>
> Ensuite, soit *B<sub>n </sub>*=<sup>T</sup>*<sub>m≥n</sub> A<sub>m </sub>*et *C<sub>n </sub>*=<sup>S</sup>*<sub>m≥n</sub> A<sub>m</sub>*. Alors (*B<sub>n</sub>*)*<sub>n</sub>* croît vers *A* et (*C<sub>n</sub>*)*<sub>n</sub>* décroît vers *A*, donc lim<sub>*n→*∞</sub> **P**(*B<sub>n</sub>*) = **P**(*A*) = lim<sub>*n→*∞</sub> **P**(*C<sub>n</sub>*) d’après le Théorème 3. Mais *B<sub>n</sub> ⊂ A<sub>n</sub> ⊂ C<sub>n</sub>*, donc **P**(*B<sub>n</sub>*) *≤* **P**(*A<sub>n</sub>*) *≤* **P**(*C<sub>n</sub>*), de sorte que lim<sub>*n→*∞</sub> **P**(*A<sub>n</sub>*) = **P**(*A*). □
>
> *2. Probabilités conditionnelles et indé pendance et Probabilités sur un espace fini ou dénombrable*
>
> Soient *A*, *B ∈* (Ω, *A*, **P**). La fréquence *f<sub>n</sub>*(*A*) de réalisation de *A* lorsqu’on répète *n* fois la même expérience, converge (en un sens à préciser !) vers la probabilité **P**(*A*), qui quantifie "les chances de voir *A* réalisé".
>
> Supposons maintenant qu’on sache que *B* est réalisé. Les chances de voir *A* réalisé vont changer et être quantifiées par un nouveau nombre **P**(*A\|B*), "la probabilité de *A* sachant *B*" : on peut à nouveau considérer la fréquence de *A* lorsque l’expérience est répétée *n* fois, sauf qu’il faut calculer cette fréquence sur l’ensemble des expériences où *B* se réalise.
>
> Il est ainsi naturel de considérer le nombre de fois où *A et B* sont réalisés, c’est-à-dire *n f<sub>n</sub>*(*A ∩ B*); pour obtenir une fréquence il convient de diviser ce nombre par le nombre d’occurrences de *B*, i.e. *n f<sub>n</sub>*(*B*), de sorte qu’en définite on doit avoir
>
> **P**(*A\|B*) *≈<sup>n f</sup><sub>n</sub>*(*A ∩ B*)
>
> *n f<sub>n</sub>*<sub>(*B*)</sub>=*<sup>f</sup><sub>n</sub>*(*A ∩ B*)
>
> *f<sub>n</sub>*(*B*)<sup>.</sup>
>
> La définition ci-dessous est tirée de cette relation en "prenant la limite en *n*".
>
> En particulier, il se peut que le fait de savoir que *B* est réalisé ne donne aucune information sur la réalisation de *A* : on dit alors que *A* est "indépendant" de *B*, et cela se traduit par le fait que **P**(*A\|B*) = **P**(*A*). Et donc <sup>**P**(*A∩B*)</sup>
>
> <sub>**P**(*B*~~) ~~</sub>= **P**(*A*), donc **P**(*A ∩ B*) = **P**(*A*)**P**(*B*). Nous
>
> allons maintenant introduire les définitions proprement dites en commençant par l’indépendance :
>
> **Définition 6 (indépendance)** *a) A et B sont dit indépendants si* **P**(*A ∩ B*) = **P**(*A*)**P**(*B*)*.*
>
> *b) Soit* (*A<sub>i</sub>*)*<sub>i∈I</sub> une famille d’événements, où I ⊂* **N***. Les* (*A<sub>i</sub>*)*<sub>i∈I</sub>sont dits*
>
> 12
>
> *indépendants, ou parfois "mutuellement indépendants" si*

*∀J ⊂ I fini*, **P**



<sup>\\</sup> *j∈J*

*A<sub>j</sub>*



<sup> =</sup> ∏ *j∈J*

**P**(*A<sub>j</sub>*).

> Remarque : Si les (*A<sub>i</sub>*)*<sub>i∈I</sub>* sont indépendants, ils sont aussi deux à deux indépendants, ce qui signifie que *A<sub>i </sub>*et *A<sub>j </sub>*sont indépendants pour tous *i*, *j* avec *i ̸*= *j*, mais la réciproque est fausse.
>
> **Théorème 4** *Si A et B sont indépendants, il en est de même de A et B<sup>c</sup>, de A<sup>c</sup>et B, et de A<sup>c</sup>et B<sup>c</sup>.*
>
> *Preuve:* Pour *A* et *B<sup>c</sup>*, on a **P**(*A ∩ B<sup>c</sup>*) = **P**(*A*) *−* **P**(*A ∩ B*) = **P**(*A*) *−* **P**(*A*)**P**(*B*) = **P**(*A*)(1 *−* **P**(*B*)) = **P**(*A*)**P**(*B<sup>c</sup>*). Les autres propriétés se montrent de manière analogue. □
>
> **Exemple 3** *1. On choisit une carte au hasard parmi* 52 *cartes. A* = *{la carte est un cœur}, et B* = *{la carte est une dame}. Un modèle naturel pour cette expérience consiste à affecter la probabilité* <sup><u>1</u></sup>~~<sub>52</sub>~~ *au choix de chacune des cartes. Par additivité,* **P**(*A*) = <sup><u>13</u></sup>~~<sub>52</sub>~~ *et* **P**(*B*) = <sup><u>4</u></sup>~~<sub>52</sub>~~ *et* **P**(*A ∩ B*) = <sup><u>1</u></sup>~~<sub>52</sub>~~ *, donc A et B sont indépendants.*
>
> *2. Soit* Ω = *{*1, 2, 3, 4*} et A* = *P*(Ω)*. Soit* **P**(*i*) = <sup><u>1</u></sup>~~<sub>4</sub>~~*pour i ∈ {*1, 2, 3, 4*}. Soit enfin A* = *{*1, 2*}, B* = *{*1, 3*} et C* = *{*2, 3*}. Alors A, B, C sont*
>
> *deux à deux indépendants, mais pas (mutuellement) indépendants.*
>
> **Définition 7 (Probabilité conditionnelle)** *Soit A*, *B deux événements, avec* **P**(*B*) *\>* 0*. La probabilité conditionnelle de A sachant B est* **P**(*A\|B*) = **P**(*A ∩ B*)/**P**(*B*)*.*
>
> **Théorème 5 (Probabilité conditionnelle sachant un événement)** *Supposons que* **P**(*B*) *\>* 0*.*
>
> *(a) A et B sont indépendants ⇔* **P**(*A\|B*) = **P**(*A*)*.*
>
> *(b) L’application* **P***<sub>B</sub>* : *A ∋ A 7→* **P**(*A\|B*) *∈* \[0, 1\] *définit une nouvelle me sure de probabilité sur A, appelée la "probabilité conditionnelle sachant B".*
>
> *Preuve:* (*a*) résulte d’un calcul immédiat. Pour (*b*), on doit mon trer que **P***<sub>B</sub>* vérifie les deux axiomes (1) et (2) d’une probabilité de mesure. (1) provient de **P***<sub>B</sub>*(Ω) = **P**(Ω*\|B*) = **P**(Ω *∩ B*)/**P**(*B*) = **P**(*B*)/**P**(*B*) = 1.
>
> Quant à (2), **P***<sub>B</sub>*(*∪<sub>n∈</sub>***<sub>N</sub>***∗ A<sub>n</sub>*) = **P**(*∪<sub>n∈</sub>***<sub>N</sub>***∗* (*A<sub>n</sub> ∩ B*))/**P**(*B*) = ∑<sub>*n∈***N**</sub>*∗* **P**(*A<sub>n</sub> ∩ B*)/**P**(*B*), car les (*A<sub>n</sub> ∩ B*)<sub>*n∈***N**</sub>*∗* sont deux à deux disjoints, d’où **P***<sub>B</sub>*(*∪<sub>n∈</sub>***<sub>N</sub>***∗ A<sub>n</sub>*) = ∑<sub>*n∈***N**</sub>*∗* **P**(*A<sub>n</sub>\|B*) = ∑<sub>*n∈***N**</sub>*∗* **P***<sub>B</sub>*(*A<sub>n</sub>*). □

13

> **Théorème 6 (Théorème des probabilités composées)** *Soit A*<sub>0</sub> = Ω*.*
>
> *Soit n ∈* **N***<sup>∗</sup> \\ {*1*}. On pose I<sub>n </sub>*= *{*1, 2, . . . , *n}. Si* (*A<sub>i</sub>*)*<sub>i∈I</sub> ∈ A<sup>I</sup>et si*
>
> **P**(*∩<sub>i∈In−</sub>*<sub>1</sub>) *\>* 0*, alors*
>
> **P**(*A*<sub>1</sub> *∩ A*<sub>2</sub> *∩ · · · ∩ A<sub>n</sub>*) = **P**(*A*<sub>1</sub>)**P**(*A*<sub>2</sub>*\|A*<sub>1</sub>)**P**(*A*<sub>3</sub>*\|A*<sub>1</sub> *∩ A*<sub>2</sub>)*· · ·* **P**(*A<sub>n</sub>\|A*<sub>1</sub> *∩ · · · ∩ A<sub>n−</sub>*<sub>1</sub>).
>
> *Preuve:* En utilisant la définition de la probabilité conditionnelle la
>
> preuve se fait par récurrence. □
>
> **Théorème 7 (Formule des probabilités totales)** *Soit* (*E<sub>n</sub>*)*<sub>n∈I</sub> ∈ A<sup>I</sup>*
>
> *une partition dénombrable de* Ω*. Pour tout A ∈ A, on a*

<sup>**P**(*A*) =</sup> ∑ *n∈I*

**P**(*A\|E<sub>n</sub>*)**P**(*E<sub>n</sub>*).

> *Preuve:* On a *A* = *A ∩* Ω =<sup>S</sup>*<sub>n∈I</sub>*(*A ∩ E<sub>n</sub>*) et comme les (*A ∩ E<sub>n</sub>*)*<sub>n∈I</sub>* sont deux à deux disjoints, on obtient par *σ*-additivité de **P**, **P**(*A*) = ∑*<sub>n∈I</sub>* **P**(*A ∩ E<sub>n</sub>*) = ∑*<sub>n∈I</sub>* **P**(*A\|E<sub>n</sub>*)**P**(*E<sub>n</sub>*). □
>
> **Théorème 8 (Théorème de Bayes, ou de "probabilité des causes".)** *Soit* (*E<sub>n</sub>*)*<sub>n∈I</sub> ∈ A<sup>I</sup> une partition dénombrable de* Ω*. Pour tout A ∈ A tel que* **P**(*A*) *\>* 0 *on a*
>
> **P**(*E<sub>m</sub>\|A*) = <sup>**P**(*A\|E*</sup>*<sub>m</sub>*)**P**(*E<sub>m</sub>*)
>
> ∑*<sub>n∈I</sub>* **P**(*A\|E<sub>n</sub>*)**P**(*E<sub>n</sub>*)<sup>.</sup>
>
> *Preuve:* Au vu du précédent théorème le dénominateur vaut **P**(*A*), la formule devient donc <sup>**P**(*A\|E*</sup>*<sub><u>m</u></sub>*)**P**(*E<sub><u>m</u></sub>*)
>
> <sub>**P**(*A*~~) ~~</sub>=<sup>**P**(*A∩E*</sup>*<sub><u>m</u></sub>*)

<sub>**P**(*A*~~) ~~</sub>= **P**(*E<sub>m</sub>\|A*). □

> Ce théorème a des conséquences profondes en probabilités et en statistique, voir par exemple les exercices en TD.
>
> **Probabilités sur un espace fini ou dénombrable :**
>
> Dans cette section nous supposons que l’espace d’états Ω est fini ou dénombrable, et nous choisissons pour la tribu la classe *A* = *P*(Ω).
>
> **Théorème 9** *a) Une probabilité sur l’ensemble fini ou dénombrable* Ω *est caractérisée par ses valeurs sur les singletons : p<sub>ω </sub>*:= **P**(*{ω}*)*, ω ∈* Ω*. b) Si* (*p<sub>ω</sub>*)<sub>*ω∈*Ω</sub> *est une famille de réels indéxée par l’ensemble fini ou dénombrable* Ω*, il existe une probabilité* **P** *(nécessairement unique par a*)*) sur* Ω *telle que* **P**(*{ω}*) = *p<sub>ω</sub> pour tout ω ∈* Ω *si et seulement si p<sub>ω</sub> ≥* 0 *et* ∑<sub>*ω∈*Ω</sub> *p<sub>ω </sub>*= 1*.*
>
> *Preuve:* Soit *A ∈ A*; on a *A* =<sup>S</sup>*<sub>ω∈A</sub>{ω}*, réunion finie ou dénom brable de singletons deux à deux disjoints. Si **P** est une probabilité sur Ω, la *σ*-additivité implique **P**(*A*) = *· · ·* = ∑*<sub>ω∈A</sub> p<sub>ω</sub>*. On a donc
>
> *a*). Pour la condition nécessaire de *b*), i.e. l’implication *⇒*, on re marque sur si **P**(*{ω}*) = *p<sub>ω</sub>*, alors par définition *p<sub>ω</sub> ≥* 0, et aussi
>
> 14
>
> 1 = **P**(Ω) = **P**(<sup>S</sup><sub>*ω∈*Ω</sub>*{ω}*) = ∑<sub>*ω∈*Ω</sub> **P**(*ω*) = ∑<sub>*ω∈*Ω</sub> *p<sub>ω</sub>*. Suppo sons inversement que les *p<sub>ω </sub>*vérifient *p<sub>ω</sub> ≥* 0 et ∑<sub>*ω∈*Ω</sub> *p<sub>ω </sub>*= 1. On a pose **P**(*A*) := ∑*<sub>ω∈A</sub> p<sub>ω</sub>*, avec la convention qu’une somme "vide" est nulle. On a donc **P**(Ω) = 1. Pour la *σ*-additivité, elle est évident lorsque Ω est fini, et lorsque Ω est dénombrable elle
>
> provient de ce qu’on peut "sommer par paquets" pour obtenir que ∑*<sub>i∈I</sub>* ∑*<sub>ω∈Ai</sub>p<sub>ω </sub>*= ∑*<sub>ω∈∪i∈I</sub> A<sub>i</sub>p<sub>ω </sub>*si les *A<sub>i </sub>*sont deux à deux disjoints. □ **Exemple 4** *• Prenons* Ω = **N** *et A* = *P*(**N**)*, et* **P**(*{ω}*) = *e<sup>−λ <u>ω</u>n</sup>*

~~<sub>*n*!</sub>~~*pour*

> *tout ω ∈* Ω*.* **P** *est une mesure de probabilité et est appelée la loi de Poisson de paramètre λ \>* 0*.*
>
> *• Prenons* Ω = **N** *et A* = *P*(**N**)*, et* **P**(*{ω}*) = (1 *− α*)*α<sup>ω</sup>, pour tout ω ∈* Ω*.* **P** *est une mesure de probabilité et est appelée La loi géométrique de paramètre α ∈* \[0, 1\[*.*
>
> **Définition 8 (Probabilité uniforme)** *On dit que la probabilité* **P** *sur l’espace fini* Ω *est uniforme si p<sub>ω </sub>*= **P**(*{ω}*) *ne dépend pas de ω.*
>
> Dans ce cas il est immédiait que **P**(*A*) = <sup>card(*A*)</sup>

le "cardinal", ou nombre de points, de *A*.

<sub>card(Ω)</sub>où card(*A*) désigne

> *3. Variables aléatoires sur un espace fini ou dénombrable et Construction d’une mesure de probabilité*
>
> Dans ce chapitre nous supposons encore l’espace d’états Ω dénom brable, et nous choisissons pour tribu la classe *A* = *P*(Ω) de toutes les parties de Ω.
>
> **Définition 9** *Une variable aléatoire X est définie comme une application de* Ω *dans un ensemble E (a priori arbitraire).*
>
> Une variable aléatoire représente une quantité qui dépend de l’issue de l’expérience.
>
> Noter que l’espace d’arrivée *E* n’est pas nécessairement dénom brable. Par exemple *E* = **R** si l’expérience consiste à choisir une personne dans une salle et si *X*(*ω*) représente la taille de la personne *ω* ; mais l’image *E<sup>′ </sup>*de Ω par *X*, i.e. *E<sup>′</sup>*:= *{i ∈ E*, *∃ω ∈* Ω *\| X*(*ω*) = *i}*, est, quant à elle, nécessairement dénombrable.
>
> On peut alors définir la loi de *X*, notée par **P***<sub>X</sub>*, appelée aussi la distribution de *X*, par
>
> **P***<sub>X</sub>*(*A*) = **P**(*X<sup>−</sup>*<sup>1</sup>(*A*)), *∀A ∈ P*(*E<sup>′</sup>*).
>
> Le fait que **P***<sub>X</sub>* définisse une mesure de probabilité sur *E<sup>′</sup>*est évident (muni de la tribu de toutes ses parties *P*(*E<sup>′</sup>*)). Comme *E<sup>′</sup>*est dénom brable, **P***<sub>X</sub>* est complètement déterminé par les nombres

*p<sup>X</sup><sub>j</sub>*<sup>:= **P**(*X* = *j*) =</sup> ∑ *{ω∈*Ω : *X*(*ω*)=*j}*

*p<sub>ω</sub>*,

> et la famille (*p<sup>X</sup><sub>j</sub>*)*<sub>j∈E</sub>′* est aussi appelée la loi de la variable *X*. On a bien sûr **P***<sub>X</sub>*(*A*) = ∑*<sub>j∈A</sub> p<sup>X</sup><sub>j</sub>*pour tout *A ∈ P*(*E<sup>′</sup>*).
>
> Si **P***<sub>X</sub>* est une loi munie d’un nom, par exemple une loi de Poisson, on dit aussi que *X* est une variable aléatoire de Poisson.
>
> **Définition 10** *Soit X une variable aléatoire à valeurs dans E* = **R***, définie sur un espace dénombrable. On appelle espérance, ou espérance mathéma-*

16

*tique, de X le nombre*

<sup>**E**\[*X*\] =</sup> ∑

*ω∈*Ω

*X*(*ω*)*p<sub>ω</sub>*,

> *lorsqu’il est bien défini ; c’est le cas si* Ω *est fini ; c’est aussi le cas, lorsque* Ω *est infini dénombrable, si la série ci-dessus est absolument convergente, ou si X*(*ω*) *≥* 0 *pour tout ω ∈* Ω *(dans ce dernier cas on peut avoir* **E**\[*X*\] = +∞*).*
>
> Notons *L*<sup>1</sup>l’espace de toutes les variables aléatoires réelles qui ont une espérance finie. Il est alors immédiat que :
>
> \(1\) *L*<sup>1</sup>est un espace vectoriel et la fonctionnelle espérance **E** est linéaire.
>
> \(2\) La fonctionnelle espérance **E** est positive : si *X ∈ L*<sup>1</sup>et *X ≥* 0, alors **E**\[*X*\] *≥* 0. Plus généralement si *X*,*Y ∈ L*<sup>1</sup>et *X ≤ Y* alors **E**\[*X*\] *≤* **E**\[*Y*\].
>
> \(3\) *L*<sup>1</sup>contient toutes les variables aléatoires bornées. Si *X ≡ a*, *a ∈* **R**, alors **E**\[*X*\] = *a*.
>
> \(4\) Si *X ∈ L*<sup>1</sup>, son espérance dépend seulement de sa loi, et si *E<sup>′</sup>*est l’image de Ω par *X*, on a

<sup>**E**\[*X*\] =</sup> ∑ *j∈E<sup>′</sup>*

*j***P**(*X* = *j*).

∑

*X*(*ω*)*p<sub>ω </sub>*<sup>=</sup> ∑

*X*(*ω*)*p<sub>ω </sub>*<sup>=</sup> ∑

∑

*X*(*ω*)*p<sub>ω</sub>*

*ω∈*Ω

*ω∈*<sup>S</sup> *<sub>j∈E</sub>′*

*X<sup>−</sup>*<sup>1</sup>(*{j}*)

*j∈E<sup>′</sup>*

*ω∈X<sup>−</sup>*<sup>1</sup>(*{j}*)

<sup>=</sup> ∑ *j∈E<sup>′</sup>*

∑

*ω∈X<sup>−</sup>*<sup>1</sup>(*{j}*)

*jp<sub>ω </sub>*<sup>=</sup> ∑ *j∈E<sup>′</sup>*

*<sup>j</sup>* ∑

*ω∈X<sup>−</sup>*<sup>1</sup>(*{j}*)

*p<sub>ω </sub>*<sup>=</sup> ∑ *j∈E<sup>′</sup>*

*jP*(*X<sup>−</sup>*<sup>1</sup>(*{j}*<sup>) =</sup> ∑ *j∈E<sup>′</sup>*

*jP*(*X* = *j*)

> \(5\) Si *X* = **1***<sub>A</sub>* est l’indicatrice d’un événement *A*, on a **E**\[*X*\] = **P**(*A*). En effet **E**\[*X*\] est bien défini car *X ≥* 0, et on a **E**\[*X*\] = ∑<sub>*ω∈*Ω</sub> **1***<sub>A</sub>*(*ω*)*p<sub>ω </sub>*= ∑*<sub>ω∈A</sub>* 1 *× p<sub>ω </sub>*= **P**(*A*).
>
> **Théorème 10** *Soit h* : **R** *→* \[0, ∞\] *une fonction positive et X une variable aléatoire réelle. On alors*
>
> **P**(*{ω ∈* Ω : *h*(*X*(*ω*)) *≥ a}*) *≤*<sup>**E**\[*h*(*X*)\]</sup>

*a*

> *pour tout a \>* 0*.*
>
> *Preuve:* Comme *X* est une variable aléatoire, il en est de même de *Y* = *h*(*X*); soit *A* = *Y<sup>−</sup>*<sup>1</sup>(\[*a*, ∞\[) = *{ω* : *h*(*X*(*ω*)) *≥ a}* = *{h*(*X*) *≥ a}*, alors on a *h*(*X*) *≥ a***1***<sub>A</sub>*, donc **E**\[*h*(*X*)\] *≥* **E**\[*a***1***<sub>A</sub>*\] = *a***E**\[**1***<sub>A</sub>*\] = *a***P**(*A*) et le résultat suit. □
>
> **Corollaire 1 (Inégalité de Markov)**
>
> **P**(*\|X\| ≥ a*) *≤*<sup>**E**\[*\|X\|*\]</sup>
>
> *<sub>a</sub>*.

17

> *Preuve:* Prendre **R** *∋ x 7→ h*(*x*) := *\|x\|* dans le Théorème 10. □
>
> Remarque : Pour tout réel *x*, *\|x\| ≤* 1 + *x*<sup>2</sup>, donc *X*<sup>2</sup> *∈ L*<sup>1</sup> *⇒ X ∈ L*<sup>1</sup>
>
> d’où
>
> **Définition 11** *Soit X une variable aléatoire réelle telle que X*<sup>2</sup> *∈ L*<sup>1</sup>*. On*
>
> *appelle variance de X le nombre*
>
> *σ*<sup>2</sup>*<sub>X</sub>* = **E**\[(*X −* **E**\[*X*\])<sup>2</sup>\]
>
> *et l’écart-type le nombre σ<sub>X</sub> la racine carrée "positive" de la variance.*
>
> *L’espérance de X, est également appelé la moyenne de X, parfois notée par*
>
> *µ<sub>X</sub>.*
>
> **Corollaire 2 (Inégalités de Bienaymé-Chebyshev)** *Si X*<sup>2</sup> *∈ L*<sup>1</sup>*, on a*
>
> *a)* **P**(*\|X\| ≥ a*) *≤*<sup>**E**\[*X*2</sup>\]
>
> *a*<sup>2</sup>*pour tout a \>* 0*,*
>
> *b)* **P**(*\|X − µ<sub>X</sub>\| ≥ a*) *≤<sup>σ</sup>*<sup>2</sup>*<u>X</u>*
>
> *a*<sup>2</sup>*pour tout a \>* 0*.*
>
> *Preuve:* Pour a), on applique le Théorème 10 avec *h* : *x 7→ x*<sup>2</sup>, ce qui
>
> donne **P**(*\|X\| ≥ a*) = **P**(*h*(*X*) *≥ a*<sup>2</sup>) *≤*<sup>**E**\[*X*2</sup>\]

*a*~~<sup>2</sup>~~. Pour b), on applique a) à

> la variable aléatoire *Y* = *\|X − µ<sub>X</sub>\|*. □
>
> **Exemple 5** 1) *X suit une loi de Poisson de paramètre, que l’on note par*
>
> *X ∼* Poisson(*λ*)*, si pour tout A ⊂* **N***, on a* **P**(*X ∈ A*) = ∑*<sub>j∈A</sub>* **P**(*X* =
>
> *j*) = ∑*<sub>j∈A</sub><u>λ</u><sup>j</sup>~~<sub>j</sub>~~*~~<sub>!</sub>~~*e<sup>−λ</sup>.*
>
> *L’espérance de X est donnée par* **E**\[*X*\] = ∑<sup>∞</sup><sub>*j*=0</sub>*j***P**(*X* = *j*) =
>
> ∑<sup>∞</sup><sub>*j*=0</sub>*j<sup><u>λ</u>j</sup>~~<sub>j</sub>~~*~~<sub>!</sub>~~*e<sup>−λ </sup>*= *λ.*
>
> 2\) *X est de Bernoulli, i.e. elle prend seulement les deux valeurs* 1 *et*
>
> 0 *avec les probabilités respectives p et q* = 1 *− p (avec p ∈*\]0, 1\[*). Alors*
>
> **E**\[*X*\] = 1 *·* **P**(*X* = 1) + 0 *·* **P**(*X* = 0) = *p.*
>
> 3\) *X est binomiale, que l’on écrit X ∼ B*(*p*, *n*)*, i.e. X peut prendre les*
>
> *valeurs* 0, 1, . . . , *n, et* **P**(*X* = *k*) = (*<sup>n</sup><sub>k</sub>*)*p<sup>k</sup>q<sup>n−k</sup>.*
>
> Construction d’une mesure de probabilité
>
> Dans ce chapitre Ω est un espace totalement quelconque, muni
>
> d’une tribu *A*.
>
> Nous nous proposons de construire, ou de caractériser, une me
>
> sure de probabilité sur *A* (on dit aussi sur (Ω, *A*)) à partir de la
>
> connaissance des probabilités **P**(*A*) pour les événements *A* apparte
>
> nant à une certaine sous-classe de *A*, qu’on aimerait être "aussi petite
>
> que possible".
>
> Quand Ω est dénombrable nous avons vu que c’était une chose
>
> simple à réaliser, à partir par exemple de la probabilité *p<sub>ω </sub>*= **P**(*{ω}*)
>
> des singletons.
>
> 18
>
> Mais dans le cas général la même méthode ne marche plus : une probabilité "typique" **P** vérifiera **P**(*{ω}*) = 0 pour tout *ω* et donc les nombres **P**(*{ω}*) ne caractérisent pas **P**.
>
> Pour construire **P** il convient d’abord de préciser les ingrédients de base : on verra dans des cas "concrets" et notamment au chapitre suivant, qu’il est souvent aisé de construire une "probabilité" sur une algèbre qui engendre la tribu *A*, et le problème qu’on se pose ci-dessous est l’extension de cette probabilité à la tribu *A* elle-même.
>
> Soit donc une algèbre *A*<sub>0</sub> qui engendre la tribu *A*, et une probabi lité **P** : *A*<sub>0</sub> *→* \[0, 1\] sur *A*<sub>0</sub>, et donc :
>
> 1\) **P**(Ω) = 1 et 2) pour toute suite (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗* d’éléments de *A*<sub>0</sub> deux à deux disjoints et telle que <sup>S</sup>*n∈***N***<sup>∗ A</sup><sub>n</sub> ∈ A*<sub>0</sub>, on a **P**(<sup>S</sup>*n∈***N***<sup>∗ A</sup><sub>n</sub>*) = ∑<sub>*n∈***N**</sub>*∗* **P**(*A<sub>n</sub>*).
>
> **Théorème 11** *Toute probabilité* **P** *définie sur une algèbre A*<sub>0</sub> *admet une unique extension (notée aussi* **P***) à la tribu A* = *σ*(*A*<sub>0</sub>)*.*
>
> Nous allons démontrer l’unicité de **P** dont l’existence est assez difficile.
>
> Note : pour l’existence vous pouvez vous référer par exemple aux livres suivants :
>
> *•* Théorie de l’intégration ; Vuibert ; Paris - M. Briane, G. Pagès (1998) *•* Bases mathématiques du calcul des probabilités. Paris - J. Neveu (1964).
>
> *•* Introduction to Measure and Integration ; Cambridge University Press ; Cambdrige, Grande-Bretagne - S.J. Taylor (1973).
>
> **Définition 12** *• Une classe C de parties de* Ω *est stable par intersection si pour tous A*, *B ∈ C on a A ∩ B ∈ C (et alors, si A*<sub>1</sub>, . . . , *A<sub>n</sub> ∈ C, on a A*<sub>1</sub> *∩ A*<sub>2</sub> *∩ · · · A<sub>n</sub> ∈ C pour n arbitraire fini).*
>
> *• Une classe C est stable par limite croissante si pour toute suite crois sante* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ ∈ C*<sup>**N***∗*</sup>*on a* <sup>S∞</sup><sub>*n*=1</sub> *A<sub>n</sub> ∈ C.*
>
> *• Une classe C est stable par différence si pour tous A*, *B ∈ C avec A ⊂ B on a B \\ A ∈ C.*
>
> **Théorème 12 (Théorème des classes monotones)** *Soit C une classe de parties de* Ω*, contenant* Ω*, stable par intersection.*
>
> *Soit D la plus petite classe contenant C et stable par limite croissante et par différence. Alors D* = *σ*(*C*)*.*
>
> *Preuve:* Remarquons d’abord que l’intersection d’une famille quel conque de classes qui sont stables par limite croissante et par dif férence est une classe également stable par limite croissante et par différence. Ainsi en prenant l’intersection de toutes les classes ayant ces propriétés et contenant *C* on voit qu’il existe une plus petite classe contenant *C* et stable par limite croissante et par différence.

19

> Pour tout *B ⊂* Ω notons *D<sub>B </sub>*la classe de toutes les parties de
>
> *A* vérifiant *A ∈ D* et *A ∩ B ∈ D*. Étant données les propriétés de
>
> *D*, on voit facilement que *D<sub>B </sub>*est stable par limite croissante et par
>
> différence.
>
> Soit *B ∈ C* : pour chaque *C ∈ C* on a *B ∩ C ∈ C ⊂ D* et *C ∈ D*, donc
>
> *C ∈ D<sub>B</sub>*. Par suite *C ⊂ D<sub>B</sub> ⊂ D*. Donc *D*<sub>=</sub>*D<sub>B</sub>*, grâce aux propriétés de
>
> *D* et *D<sub>B</sub>*.
>
> Maintenant, soit *B* dans *D*. Pour chaque *C ∈ C* on a *B ∈ D<sub>C</sub>*,
>
> et grâce à ce qui précède il vient *B ∩ C ∈ D*, donc *C ∈ D<sub>B</sub>*, donc
>
> *C ⊂ D<sub>B</sub> ⊂ D*.
>
> Comme *D* = *D<sub>B </sub>*pour tout *B ∈ D*, on conclut que *D* est stable par
>
> intersection. De plus Ω *∈ D*, et *D* est stable par différence, donc aussi
>
> par complémentation. Comme *D* est aussi stable par limite croissante,
>
> il s’ensuit que *D* est une tribu, et c’est clairement la plus petite tribu
>
> contenant *C*. □ La preuve de l’unicité dans le Théorème 11 est une
>
> conséquence immédiate du Corollaire 3 ci-dessous, qui est lui-même
>
> une conséquence du Théorème 12.
>
> **Corollaire 3** *Soient* **P** *et* **Q** *deux probabilités définies sur A. Si* **P** *et*
>
> **Q** *coïncident sur une classe C ⊂ A qui est stable par intersection et si*
>
> *σ*(*C*) = *A, alors* **P** = **Q***.*
>
> *Preuve:* Ω *∈ A* parce que *A* est une tribu sur Ω et comme **P**(Ω) =
>
> **Q**(Ω) = 1 on peut supposer sans perte de généralité que Ω *∈ C*.
>
> Soit *B* = *{A ∈ A* : **P**(*A*) = **Q**(*A*)*}*. Par définition d’une mesure
>
> de probabilité et par le Théorème 3, *B* est stable par différence et
>
> par limite croissante. De plus *B* contient *C* par hypothèse. Par suite,
>
> comme *σ*(*C*) = *A*, on a *B* = *A* par application du Théorème des
>
> classes monotone 12. □
>
> Si en général on ne peut pas étendre la probabilité **P** sur la tribu *A*
>
> à la tribu *P*(Ω), on peut néanmoins l’étendre à une tribu un peu plus
>
> grande que *A* :
>
> **Définition 13** *Soit* **P** *une probabilité sur A. Un ensemble négligeable*
>
> *pour* **P** *est une partie A de* Ω *telle qu’il existe un élément B de A vérifiant*
>
> *A ⊂ B et* **P**(*B*) = 0*.*
>
> On dit qu’une propriété est vraie *presque sûrement* (en abrégé : p.s.) si
>
> elle est vraie en dehors d’un ensemble négligeable ; cette notion dé
>
> pend bien sûr de la probabilité, de sorte qu’on dit parfois **P**-presque
>
> sûrement, ou **P**-p.s.
>
> **Théorème 13** *Soit* **P** *une probabilité sur A et N la classe de tous les*
>
> *ensembles* **P***-négligeables. Alors A<sup>′ </sup>*= *{A ∪ N* : *A ∈ A*, *N ∈ N } est une*
>
> *tribu, appelée* **P***-complétition de A. C’est la plus petite tribu contenant A et*
>
> *N , et* **P** *s’étend de manière unique en une mesure de probabilité (notée aussi*
>
> **P***) sur A<sup>′</sup>, en posant* **P**(*A ∪ N*) = **P**(*A*) *pour A ∈ A et N ∈ N .*
>
> 20
>
> *Preuve:* L’unicité de l’extension, si elle existe est triviale ; de même comme ∅ *∈ A* et ∅ *∈ N* , le fait que *A<sup>′</sup>*, si c’est une tribu, soit la plus petite tribu contenant *A* et *N* est trivial. Il nous suffit donc de montrer que *A<sup>′</sup>*est une tribu et que si on pose **Q**(*B*) = **P**(*A*) pour *B* = *A ∪ N* (avec *A ∈ A* et *N ∈ N* ), alors **Q**(*B*) ne dépend pas de la décomposition *B* = *A ∪ N* et **Q** est une probabilité sur *A<sup>′</sup>*.
>
> D’abord, Ω *∈ A ⊂ A<sup>′</sup>*et on a déjà vu que ∅ *∈ A<sup>′</sup>*. Ensuite comme *A* et *N* sont stables par les unions dénombrables, *A<sup>′</sup>*l’est également. Soit *B* = *A ∪ N ∈ A<sup>′</sup>*, avec *A ∈ A* et *N ∈ N* . Il existe
>
> *C ∈ A* avec **P**(*C*) = 0 et *N ⊂ C*. Posons *A<sup>′ </sup>*= *A<sup>c</sup> ∩ C<sup>c</sup> ∈ A* et *N<sup>′ </sup>*= *N<sup>c</sup> ∩ A<sup>c</sup> ∩ C ⊂ C* (donc *∈ N* ) ; comme *B<sup>c </sup>*= *A<sup>′</sup> ∪ N<sup>′</sup>*, on a *B<sup>c</sup> ∈ A<sup>′</sup>*, et *A<sup>′</sup>*est stable par complémentation : ainsi *A<sup>′</sup>*est une tribu.
>
> Supposons maintenant que *A*<sub>1</sub> *∪ N*<sub>1</sub> = *A*<sub>2</sub> *∪ N*<sub>2</sub> avec *A<sub>i</sub> ∈ A* et *N<sub>i</sub> ∈ N* . La différence symétrique *A*<sub>1</sub>∆*A*<sub>2</sub> = (*A*<sub>1</sub> *∩ A<sup>c</sup>*<sub>2</sub>) *∪* (*A<sup>c</sup>*<sub>1</sub> *∩ A*<sub>2</sub>) est contenue dans *N*<sub>1</sub> *∪ N*<sub>2</sub>, lui-même contenu dans un élément *C* de *A* de probabilité nulle : par suite **P**(*A*<sub>1</sub>) = **P**(*A*<sub>2</sub>), ce qui montre que **Q** est défini sans ambiguïté, et coïncide de manière évidente avec **P** sur *A*. Enfin le fait que **Q** soit une probabilité sur *A<sup>′</sup>*est évident. □

*4. Probabilités sur* **R** *et fonctions de ré partition*

*<span class="mark">0.0.1</span> Probabilités sur* **R**

Dans ce chapitre nous travaillerons sur un espace mesurable (Ω, *F*) avec Ω = **R** et *F* = *B*(**R**).

**Définition 14** *Si* **P** *est une probabilité sur* (**R**, *B*(**R**))*, sa fonction de répartition est la fonction F*(*x*) = **P**(\] *−* ∞, *x*\])*.*

**Théorème 14** *La fonction de répartition F caractérise la probabilité, i.e. que si* **Q** *est une autre probabilité sur* (**R**, *B*(**R**))*, de fonction de répartition G*(*x*) = **Q**(\] *−* ∞, *x*\]) *et si F* = *G, alors* **P** = **Q***.*

*Preuve:* la preuve est admise, voir page 41, Théorème 7.1 de 1. □ La signification de ce théorème est que la probabilité est entièrement connu si on connaît seulement *F* : on peut donc en principe retrou ver **P**(*A*) pour n’importe quel borélien *A* à partir de la fonction *F* (déterminer "explicitement" **P**(*A*) en fonction de *F* est une autre chose !).

Il est donc important de savoir caractériser les fonctions *F* qui sont des fonctions de répartition : cela permet en principe de caractériser toutes les probabilités **P**, et cela fait l’objet du théorème suivant.

**Théorème 15** *Une fonction F est la fonction de répartition d’une (unique) probabilité sur* (**R**, *B*(**R**)) *si et seulement si elle vérifie les propriétés sui vantes :*

*(i) F est croissante ;*

*(ii) F est continue à droite ;*

*(iii)* lim<sub>*x→−*∞</sub> *F*(*x*) = 0 *et* lim<sub>*x→*∞</sub> *F*(*x*) = 1*.*

*Preuve:* la preuve est admise, voir page 42, Théorème 7.2 de 1. □

**Propriété 6** *Soit F la fonction de répartition de la probabilité* **P** *sur* **R***. En notant F*(*x<sup>−</sup>*) *la limite à gauche de F au point x (qui existe puisque F est croissante), pour tous x \< y on a*

si égalité fonctions de répartitions alors égalité des probas

> 22
>
> *(i)* **P**(\]*x*, *y*\]) = *F*(*y*) *− F*(*x*)*,*
>
> *(ii)* **P**(\[*x*, *y*\]) = *F*(*y*) *− F*(*x<sup>−</sup>*)*,*
>
> *(iii)* **P**(\[*x*, *y*\[) = *F*(*y<sup>−</sup>*) *− F*(*x<sup>−</sup>*)*,*
>
> *(iv)* **P**(\]*x*, *y*\[) = *F*(*y<sup>−</sup>*) *− F*(*x*)*,*
>
> *(v)* **P**(*{x}*) = *F*(*x*) *− F*(*x<sup>−</sup>*)*,*
>
> *et en particulier* **P**(*{x}*) = 0 *pour tout x si et seulement si la fonction F est continue.*
>
> *Preuve:* (*i*) se démontrer avec *F*(*x*) + **P**(\]*x*, *y*\]) = **P**(\] *−* ∞, *x*\]) + **P**(\]*x*, *y*\]) = **P**(\] *−* ∞, *x*\]*∪*\]*x*, *y*\]) car **P** est une mesure et on a deux ensembles disjoints, et donc *F*(*x*) + **P**(\]*x*, *y*\]) = **P**(\] *−* ∞, *y*\]) = *F*(*y*).
>
> Pour (*ii*) on écrit que **P**(\]*x −* 1/*n*, *y*\]) = *F*(*y*) *− F*(*x −* 1/*n*) par (*i*). Le membre de droite converge quand *n →* ∞ vers *F*(*y*) *− F*(*x<sup>−</sup>*) par définition de la limite à gauche de *F* ; quant au membre de gauche **P**(\]*x −* 1/*n*, *y*\]), il converge vers **P**(\[*x*, *y*\]) par application du théorème vu en cours, en effet *∩<sub>n∈</sub>***<sub>N</sub>***∗* \]*x −* 1/*n*, *y*\] = \[*x*, *y*\] et (\]*x −* 1/*n*, *y*\])<sub>*n∈***N**</sub>*∗* décroit vers \[*x*, *y*\], d’où **P**(*∩<sub>n∈</sub>***<sub>N</sub>***∗* \]*x −* 1/*n*, *y*\]) = lim<sub>*n→*∞</sub> **P**(\]*x −* 1/*n*, *y*\]) = **P**(\[*x*, *y*\]).
>
> Les assertions (*iii*), (*iv*) et (*v*) se montrent de manière analogue. □ <sub>**Exemple 6** *Si f est positive et Riemann-intégrable et *</sub>R**<sub>R</sub>***f*(*x*) *dx* = 1*,*
>
> <sub>*la fonction F*(*x*) =</sub> R *<sup>x</sup><sub>−</sub>*<sub>∞</sub>*f*(*y*) *dy définit la fonction de répartition d’une probabilité* **P** *sur* **R** *(voir le théorème précédent), en effet F est croissante, càd (car continue),* lim<sub>*x→−*∞</sub> *F*(*x*) = 0 *et* lim<sub>*x→*∞</sub> *F*(*x*) = 1*.*
>
> *La fonction f est appelée sa densité. (Il n’est pas vrai que toute probabilité sur* **R** *admet une densité ; en effet s’il existe une densité alors la fonction F est continue, alors qu’il existe beaucoup de fonctions de répartition disconti nues, ainsi que le montre l’exemple suivant.)*
>
> **Exemple 7** *Soit α ∈* **R***. La "masse de Dirac" au point a est la probabilité sur* **R** *qui est donné par* **P**(*A*) = **1***<sub>A</sub>*(*α*)*. Sa fonction de répartition est F*(*x*) = **1**<sub>\[*a*,∞\[</sub>(*x*)*.*
>
> Dans les exemples suivants nous définissons la probabilité (ou "loi") **P** sur **R** par sa densité *f* ; c’est-à-dire que nous définissons la fonction positive *f* d’intégrale 1, et la fonction de répartition *F* de **P** est définie
>
> <sub>par *F*(*x*) =</sub> R *<sup>x</sup><sub>−</sub>*<sub>∞</sub>*f*(*u*) *du*. On commet un léger abus de langage (habituel) en identifiant *f* avec la loi **P** correspondante, puisqu’elle
>
> détermine en fait de manière unique cette loi.
>
> **Exemple 8** *f*(*x*) = <u><sup>1</sup></u>

*uniforme sur* \[*a*, *b*\]*.*

*<sub>b~~−~~a</sub>***1**<sub>\[*a*,*b*\]</sub>(*x*) *pour tout x ∈* **R***, la loi est appelée la loi*

> **Exemple 9** *f*(*x*) = *βe<sup>−βx</sup>***1<sub>R</sub>**<sub>+</sub>(*x*) *pour tout x ∈* **R***, la loi exponentielle de paramètre β \>* 0*.*

23

> **Exemple 10** *f*(*x*) = *<sup>βα</sup>*
>
> <sub>Γ(*α*)</sub>*x<sup>α−</sup>*<sup>1</sup>*e<sup>−βx</sup>***1<sub>R</sub>**<sub>+</sub>(*x*) *pour tout x ∈* **R***, la loi*
>
> *gamma de paramètre α et β avec α*, *β ∈* **R***<sup>∗</sup>*<sub>+</sub>*.* Γ *désigne la fonction gamma,*
>
> <sub>*définie par* Γ(*α*) =</sub> R <sub>∞</sub>
>
> <sub>0</sub>*x<sup>α−</sup>*<sup>1</sup>*e<sup>−x</sup> dx pour tout α \>* 0 *; remarquons que*
>
> Γ(*α*) = (*α −* 1)! *pour tout α ∈* **N***<sup>∗</sup>et* Γ(<sup><u>1</u></sup><sub>~~2~~) =</sub> *√<sub>~~π~~.</sub>*
>
> **Exemple 11** *f*(*x*) = *αβ<sup>α</sup>x<sup>α−</sup>*<sup>1</sup>*e<sup>−</sup>*<sup>(*βx*)*α*</sup>**1<sub>R</sub>**<sub>+</sub>(*x*) *pour tout x ∈* **R***, la loi de*
>
> *Weibull, avec α*, *β ∈* **R***<sup>∗</sup>*<sub>+</sub>*.*

**Exemple 12** *f*(*x*) = <sup><u>*√*1</u></sup>2*πσ*<sup>2</sup>*e<sup>−</sup>*<sup><u>1</u></sup>~~<sub>2</sub>~~ *x−µ ~~σ ~~*

> 2

*pour tout x ∈* **R***, la loi Normale*

> *(ou distribution Gaussienne) avec* (*µ*, *σ*<sup>2</sup>) *∈* **R** *×* **R***<sup>∗</sup>*<sub>+</sub> *; la notation standard est N* (*µ*, *σ*<sup>2</sup>)*.*

**Exemple 13** *En posant g<sub>µ</sub>*<sub>,*σ*</sub>2 (*x*) = <sup><u>*√*1</u></sup>2*πσ*<sup>2</sup>*e<sup>−</sup>*<sup><u>1</u></sup>~~<sub>2</sub>~~ *x−µ ~~σ ~~*

<sub>2</sub>

*pour tout x ∈* **R** *et*

> *en posant f*(*x*) = <sup><u>1</u></sup>*~~<sub>x</sub>~~g<sub>µ</sub>*<sub>,*σ*</sub>2 (ln(*x*))**1<sub>R</sub>***<sup>∗</sup>*<sub>+</sub>(*x*) *pour tout x ∈* **R***, la loi lognormale, avec* (*µ*, *σ*<sup>2</sup>) *∈* **R** *×* **R***<sup>∗</sup>*<sub>+</sub>*.*
>
> **Exemple 14** *f*(*x*) = *<sup>β</sup>*~~<sub>2</sub>~~*e<sup>−β\|x−α\|</sup> pour tout x ∈* **R***, la loi double exponen tielle, avec α*, *β ∈* **R***.*

**Exemple 15** *f*(*x*) = <sup><u>1</u></sup>*~~<sub>βπ</sub>~~*<u>1</u>

~~<sub>2</sub>~~ = <sup><u>1</u></sup>*~~<sub>π</sub>~~*<sup><u>d</u></sup><sub>d*x*</sub>*arctan<u><sup>x−α</sup> </u>*

*pour tout*

1+

*<u>x−α</u> ~~β ~~*

*~~β~~*

> *x ∈* **R***, la loi de Cauchy, avec* (*α*, *β*) *∈* **R** *×* **R***<sup>∗</sup>*<sub>+</sub>*.*
>
> *0.0.2 Variables aléatoires*
>
> Dans un chapitre précédent nous avons considéré des variables aléatoires définies sur un espace dénombrable Ω.
>
> Nous voulons maintenant considérer un espace Ω quelconque, éventuellement non dénombrable, cet espace étant muni d’une tribu *A* d’événements et d’une probabilité **P** (sur *A*).
>
> Comme nous l’avons vu, une variable aléatoire est une application *X* : Ω *→ E*. Ce qui nous intéresse est la détermination de la proba bilité **P**(*{X ∈ A}*) = **P**(*{ω ∈* Ω : *X*(*ω*) *∈ A}*) = **P**(*X<sup>−</sup>*<sup>1</sup>(*A*)) (trois manières équivalent d’écrire le même événement). Pour cela, il faut évidemment que l’ensemble *{X ∈ A}* soit dans la tribu *A*, ce qui a priori n’est pas vrai pour une partie arbitraire *A* de *F*. Cela motive la définition suivante :
>
> **Définition 15 (Variable aléatoire)** *Soit* (Ω, *A*) *un espace mesurable, toute fonction mesurable X* : (Ω, *A*) *→* (**R**, *B*(**R**)) *est appelée variable aléatoire.*
>
> **Remarque** : en probabilités avancées on étudiera les v.a. à valeurs **R***<sup>d</sup>*, i.e. des v.a. *X* : (Ω, *A*) *→* (**R***<sup>d</sup>*, *B*(**R***<sup>d</sup>*)). Rappelons un théorème issu de Mesure et Intégration utile :
>
> 24
>
> **Théorème 16** *Soit C une classe de parties de F telle que σ*(*C*) = *F tribu sur F. Pour qu’une application X* : (*E*, *E*) *→* (*F*, *F*) *soit mesurable ssi X<sup>−</sup>*<sup>1</sup>(*C*) *⊂ E, i.e. X<sup>−</sup>*<sup>1</sup>(*C*) *∈ E pour tout C ∈ C.*
>
> Un cas particulier de ce théorème permet de caractériser de manière particulièrement simple les v.a. à valeurs réelles, i.e. quand *F* = **R**.
>
> **Corollaire 4** *Soit* (*F*, *F*) = (**R**, *B*(**R**)) *et X*, *Xn* : (*E*, *E*) *→* (*F*, *F*)*. On a l’équivalence suivante :*
>
> *X est mesurable ssi {X ≤ a} ∈ E pour tout a ∈* **R** *ssi {X ≤ a} ∈ E pour tout a ∈* **Q***.*
>
> *Preuve:* Il suffit d’appliquer le théorème précédent avec le fait que *B*(**R**) = *σ*(*C*) = *σ*(*C<sup>′</sup>*), où *C* = *{*\] *−* ∞, *a*\], *a ∈* **R***}* et *C<sup>′ </sup>*= *{*\] *−* ∞, *a*\], *a ∈* **Q***}*. □ **Remarque** : grâce au cours de Mesure et Intégration on sait que

sup*<sub>n</sub> X<sub>n</sub>*, inf*<sub>n</sub> X<sub>n</sub>*, lim sup *n→*∞

*X<sub>n</sub>*, lim inf

<sub>*n→*∞</sub>*X<sub>n </sub>*sont toutes mesurables et que

> si (*X<sub>n</sub>*)*<sub>n</sub>* converge simplement vers *X*, alors *X* est mesurable. Soit *X* une v.a. définie sur un espace de probabilité (Ω, *A*, **P**), à valeurs dans un espace mesurable (*E*, *E*). La loi de *X* est alors définie par
>
> **P***<sub>X</sub>*(*B*) = **P**(*X ∈ B*), *∀B ∈ E*.
>
> **P***<sub>X</sub>* est appelée l’image de **P** par *X*, comme *X<sup>−</sup>*<sup>1</sup>commute avec les réunions et les intersections (finies, dénombrables ou infinies non dénombrables !), et comme *X<sup>−</sup>*<sup>1</sup>(*E*) = Ω, on a de manière immédiate :
>
> **Théorème 17** *La loi* **P***<sub>X</sub> de X est une mesure de probabilité sur* (*E*, *E*)*.*
>
> Lorsque *X* est une variable aléatoire réelle, sa loi **P***<sub>X</sub>* est une pro babilité sur **R**, dont on sait qu’elle entièrement caractérisée par sa fonction de répartition :
>
> *F<sub>X</sub>*(*x*) = **P***<sub>X</sub>*(\] *−* ∞, *x*\]) = **P**(*X ≤ x*), *∀x ∈* **R**.
>
> La fonction *F<sub>X </sub>*s’appelle la fonction de répartition de la v.a. *X*. Lorsque *F<sub>X </sub>*admet une densité *f<sub>X </sub>*(i.e. *F<sub>X</sub>*<sub>(*x*) =</sub> R *<sup>x</sup><sub>−</sub>*<sub>∞</sub>*f<sub>X</sub>*(*y*) *dy* pour tout *x ∈* **R**), on dit aussi que la fonction *f<sub>X </sub>*est la densité de la v.a. *X*.
>
> *5. Intégration par rapport à une mesure de probabilité (espérance, variance)*
>
> Soit (Ω, *A*, **P**) un espace de probabilité. Nous voulons définir l’espérance d’une variable aléatoire réelle (puis la variance) sur cet espace de probabilité, en utilisant la notion d’intégrale d’une fonction mesurable (variable aléatoire).
>
> **Définition 16** *a) Soit X* : (Ω, *A*,) *→* (**R**, *B*(**R**)) *variable aléatoire réelle positive. L’espérance de X (ou "espérance mathématique", ou "intégrale" par rapport à* **P** *de X), notée par* **E**\[*X*\]*, est définie par* <sub>**E**\[*X*\] =</sub> R<sub>Ω</sub>*X*(*ω*) *d***P**(*ω*)*, d’après Mesure et Intégration* **E**\[*X*\] *existe et est à valeurs* \[0, +∞\]*.*
>
> *b) On dit qu’une v.a. X réelle (pas forcément positive) a une espérance finie, et on la note par* **E**\[*X*\]*, si* **E**\[*X*<sup>+</sup>\] *et* **E**\[*X<sup>−</sup>*\] *sont toutes deux finies et on la définie par* **E**\[*X*\] = **E**\[*X*<sup>+</sup>\] *−* **E**\[*X<sup>−</sup>*\] *(remarque X* = *X*<sup>+</sup> *− X<sup>−</sup>), qu’on <sub>écrit également sous la forme </sub>*R<sub>Ω</sub>*X*(*ω*) *d***P**(*ω*)*.*
>
> *c) On note L*<sup>1</sup>(Ω, *A*, **P**) *(lorsqu’il n’y a pas d’ambiguïté on note cela par L*<sup>1</sup>*) l’ensemble de toutes les v.a. X réelles intégrables (i.e.* **E**\[*X*\] *est fini). d) Une v.a. réelle X admet une espérance si* **E**\[*X*<sup>+</sup>\] *et* **E**\[*X<sup>−</sup>*\] *ne sont pas*
>
> *toutes deux simultanément égales à* +∞*. Dans ce cas, son espérance* **E**\[*X*\] *est encore définie par* **E**\[*X*\] = **E**\[*X*<sup>+</sup>\] *−* **E**\[*X<sup>−</sup>*\] *(avec les conven tions* +∞ + *α* = +∞ *et −*∞ + *α* = *−*∞ *pour tout α ∈* **R***.*
>
> *Noter que si* **E**\[*X*\] *admet une espérance, on a* **E**\[*X*\] *∈* \[*−*∞, +∞\]*, et X est intégrable si et seulement si son espérance existe et est finie (en effet \|X\|* = *X*<sup>+</sup> + *X<sup>−</sup>, voir Mesure et Intégration).*
>
> Le théorème suivant présente les propriétés les plus importantes de la fonctionnelle espérance. Les preuves des parties se trouvent dans le cours de Mesure et Intégration.
>
> Dans son énoncé, l’assertion "*X* = *Y* presque sûrement", ou en abrégé "p.s.", signifie que l’événement *{X ̸*= *Y}* est négligeable (**P**-négligeable), i.e. **P**(*X ̸*= *Y*) = 0 ou de manière équivalente **P**(*X* = *Y*) = 1 ; de même *X ≥ Y* p.s. signifie que **P**(*X ≥ Y*) = 1, et (*X<sub>n</sub>*)*<sub>n</sub>* converge p.s. vers *X*, signifie que **P**(*{ω ∈* Ω, lim<sub>*n→*∞</sub> *X<sub>n</sub>*(*ω*) = *X}*) = 1.
>
> 26
>
> **Théorème 18**
>
> *a) L*<sup>1</sup>*est un espace vectoriel et l’espérance est une forme linéaire sur L*<sup>1</sup>*, et aussi une fonctionnelle positive (i.e. X ≥* 0 *p.s. implique* **E**\[*X*\] *≥* 0*). Si de plus X et Y sont deux v.a. avec* 0 *≤ X ≤ Y et Y ∈ L*<sup>1</sup>*, alors X ∈ L*<sup>1</sup> *et* **E**\[*X*\] *≤* **E**\[*Y*\]*.*
>
> *b) X ∈ L*<sup>1</sup>*si et seulement si \|X\| ∈ L*<sup>1</sup>*, ou de manière équivalent si* **E**\[*\|X\|*\] *\<* +∞*, et dans ce cas \|***E**\[*X*\]*\| ≤* **E**\[*\|X\|*\]*. En particulier toute v.a. bornée est intégrable.*
>
> *c) Si X* = *Y p.s., alors* **E**\[*X*\] = **E**\[*Y*\]*.*
>
> *d) (Théorème de convergence monotone.) Si les v.a. X<sub>n</sub>*, *n ∈* **N***, sont positives et si la suite* (*X<sub>n</sub>*)*<sub>n</sub> croît p.s. vers X, alors* lim<sub>*n→*∞</sub> **E**\[*X<sub>n</sub>*\] = **E**\[*X*\] *(même si* **E**\[*X*\] = ∞*).*
>
> *e) (Lemme de Fatou.) Si les v.a. X<sub>n</sub>*, *n ∈* **N** *vérifient X<sub>n</sub> ≥ Y p.s. avec Y intégrable, les v.a. X<sub>n</sub> et* lim inf<sub>*n→*∞</sub> *X<sub>n</sub> admettent une espérance, et on a* **E**\[lim inf<sub>*n→*∞</sub> *X<sub>n</sub>*\] *≤* lim inf<sub>*n→*∞</sub> **E**\[*X<sub>n</sub>*\]*. Cela est vraie en particulier si X<sub>n</sub> ≥* 0 *p.s. pour tout n.*
>
> *f) (Théorème de convergence dominée de Lebesgue.) Si* (*X<sub>n</sub>*)*<sub>n</sub> converge p.s. vers X et si \|X<sub>n</sub>\| ≤ Y p.s. pour tout n, où Y est une v.a. intégrable, alors X<sub>n</sub> ∈ L*<sup>1</sup>*, X ∈ L*<sup>1</sup>*, et* **E**\[*X<sub>n</sub>*\] *→* **E**\[*X*\]*.*
>
> Rappelons que comme en Mesure et Intégration, l’égalité p.s. entre v.a. est clairement une relation d’équivalence, et deux v.a. équiva lentes (i.e. p.s. égales) ont la même espérance : On peut donc définie l’espace *L*<sup>1</sup>comme "*L*<sup>1</sup> modulo cette relation d’équivalence".
>
> En d’autres termes un élément de *L*<sup>1</sup>est une classe d’équivalence, c’est-à-dire l’ensemble de toutes les v.a. qui sont p.s ; égales à une v.a. particulière. Vu (*c*) ci-dessus, on peut parler de "l’espérance" de cette classe d’équivalence, qui est l’espéance de n’importe laquelle des v.a. appartenant à cette classe. Comme de plus l’addition de deux v.a. et la multiplication d’une v.a. par une constante préservent l’égalité p.s., l’ensemble *L*<sup>1</sup>est aussi un espace vectoriel. Par suite on commet l’abus (anodin) d’identifier une v.a. avec sa classe d’équivalence, et on écrit d’habitude *X ∈ L*<sup>1</sup> au lieu de *X ∈ L*<sup>1</sup>.
>
> Si 1 *\< p \<* ∞, on définit *L<sup>p</sup>*comme l’ensemble des v.a. *X* telles que *\|X\|<sup>p</sup> ∈ L*<sup>1</sup>; *L<sup>p</sup>*est défini de manière analogue à *L*<sup>1</sup>: c’est *L<sup>p </sup>*modulo la relation d’équivalence "égalité p.s." ; ou de manière équivalente, deux éléments de *L<sup>p </sup>*qui sont p.s. égaux sont considérés comme deux représentants du même élément de *L<sup>p</sup>*.

27

> Une conséquence utile du théorème de convergence dominée de
>
> Lebesgue est le résultat suivant, qui permet d’intervertir sommation
>
> et espérance.
>
> **Théorème 19** *Soit* (*X<sub>n</sub>*)*<sub>n</sub> une suite de v.a.*
>
> *a) Si les X<sub>n</sub> sont toutes positives, alors*

**E**

<sub>∞</sub> ∑

*n*=1

*X<sub>n</sub>*

=

∞

∑

*n*=1

**E**\[*X<sub>n</sub>*\].

> *b) Si* ∑<sup>∞</sup><sub>*n*=1</sub> **E**\[*\|X<sub>n</sub>\|*\] *\<* ∞*, alors la série* ∑<sup>∞</sup><sub>*n*=1</sub> *X<sub>n</sub> converge p.s., sa somme est intégrable et on a l’égalité* **E**\[∑<sup>∞</sup><sub>*n*=1</sub> *X<sub>n</sub>*\] = ∑<sup>∞</sup><sub>*n*=1</sub> **E**\[*X<sub>n</sub>*\]*.*
>
> *Preuve: S<sub>n </sub>*:= ∑*<sup>n</sup><sub>k</sub>*<sub>=1</sub>*\|X<sub>k</sub>\|* et *T<sub>n </sub>*:= ∑*<sup>n</sup><sub>k</sub>*<sub>=1</sub> *X<sub>k</sub>*.
>
> (*S<sub>n</sub>*)*<sub>n</sub>* croît vers *S* := ∑<sup>∞</sup><sub>*k*=1</sub>*\|X<sub>k</sub>\|* donc par TCM on a **E**\[*S*\] = ∑<sup>∞</sup><sub>*k*=1</sub> **E**\[*\|X<sub>k</sub>\|*\] *\<* ∞.
>
> Si les *X<sub>n </sub>*sont toutes positives alors *S<sub>n </sub>*= *T<sub>n </sub>*et donc (*a*) est prouvé. Si les *X<sub>n </sub>*ne sont pas nécessairement positives, mais si on a ∑<sup>∞</sup><sub>*k*=1</sub> **E**\[*\|X<sub>k</sub>\|*\] *\<* ∞, on obtient aussi que **E**\[*S*\] *\<* ∞.
>
> Maintenant pour chaque *ε \>* 0, **P**(*S* = ∞) *≤ ε***E**\[*S*\], et donc **E**\[*S*\] *\<* ∞ et *ε* arbitraire donnent que **P**(*S* = ∞) = 0, donc ∑<sup>∞</sup><sub>*k*=1</sub> *X<sub>k</sub>* est p.s. une série absolument convergente, et sa somme disons *T* est la limite des *T<sub>n</sub>*. De plus *\|T<sub>n</sub>\| ≤ S<sub>n</sub> ≤ S* et *S ∈ L*<sup>1</sup>. Par suite le TCD
>
> implique **E**\[∑<sup>∞</sup><sub>*k*=1</sub> *X<sub>k</sub>*\] = **E**\[lim<sub>*n→*∞</sub> *T<sub>n</sub>*\] = **E**\[*T*\]. □ Rappelons que *L*<sup>1</sup>et *L*<sup>2</sup>sont les ensembles de classes d’équiva lences de v.a. intégrables (respectivement de carré intégrable), pour la relation d’équivalence "égalité p.s.".
>
> **Théorème 20**
>
> *a) Si X et Y sont dans L*<sup>2</sup>*, on a XY ∈ L*<sup>1</sup>*et l’inégalité de Cauchy-Schwarz :* q

*\|***E**\[*XY*\]*\| ≤*

**E**\[*X*<sup>2</sup>\]**E**\[*Y*<sup>2</sup>\].

> *b) On a L*<sup>2</sup> *⊂ L*<sup>1</sup>*et si X ∈ L*<sup>2</sup>*alors* **E**\[*X*\]<sup>2</sup> *≤* **E**\[*X*<sup>2</sup>\]*.*
>
> *c) L’espace L*<sup>2</sup>*est un espace vectoriel : si X*,*Y ∈ L*<sup>2</sup>*et α*, *β ∈* **R***, alors αX* + *βY ∈ L*<sup>2</sup>*(en fait vous verrez que L*<sup>2</sup>*est un espace de Hilbert).*
>
> *Preuve: a*) On a *\|XY\| ≤ X*<sup>2</sup>/2 + *Y*<sup>2</sup>/2 d’où la réponse. La fonction *a 7→* **E**\[(*aX* + *Y*)<sup>2</sup>\] est du second degré en *a* qui est positive pour tout *a ∈* **R**, donc il est de discriminant négatif, d’où la réponse. *b*) Utiliser *a*) avec *X* = *X ×* 1 et 1 *∈ L*<sup>2</sup>.
>
> *c*) Pour tous *X*,*Y ∈ L*<sup>2</sup>et pour tous *α*, *β ∈* **R**, on a (*αX* + *βY*)<sup>2</sup> *≤ α*<sup>2</sup>*X*<sup>2</sup>/2 + *β*<sup>2</sup>*Y*<sup>2</sup>/2 d’où la réponse. □
>
> **Définition 17** *Si X ∈ L*<sup>2</sup>*, la variance de X, notée aussi σ*<sup>2</sup>(*X*) *ou σ*<sup>2</sup>*<sub>X</sub>, est définie par* Var(*X*) = **E**\[(*X −* **E**\[*X*\])<sup>2</sup>\]*.*
>
> 28
>
> **Remarque** : *X ∈ L*<sup>2</sup> *⇒ X ∈ L*<sup>1</sup>, donc **E**\[*X*\] existe. On a Var(*X*) = **E**\[*X*<sup>2</sup>\] *−* **E**\[*X*\]<sup>2</sup>.
>
> **Théorème 21 (Inégalité de Bienaymé-Chebyshev)**
>
> **P**(*\|X\| ≥ a*) *≤*<sup>**E**\[*X*2</sup>\]
>
> *a*<sup>2</sup>, *∀a ∈* **R***<sup>∗</sup>*<sub>+</sub>.
>
> *Preuve: a*<sup>2</sup>**1***<sub>{\|X\|≥a}</sub> ≤ X*<sup>2</sup> pour tout *a ∈* **R***<sup>∗</sup>*<sub>+</sub> d’où la réponse. □ **Corollaire 5**
>
> **P**(*\|X −* **E**\[*X*\]*\| ≥ a*) *≤<sup>σ</sup>*<sup>2</sup>(*X*)
>
> *a*<sup>2</sup>, *∀a ∈* **R***<sup>∗</sup>*<sub>+</sub>.
>
> Le théorème suivant est très utile, de même que le corollaire qui le suit, pour les calculs effectifs d’espérance. Il montre que l’espérance d’une v.a. ne dépend que de sa loi, et il s’agit d’une version de la formule "de changement de variable" dans les intégrables, vue sous un aspect "abstrait".
>
> **Théorème 22** *Soit X une v.a. définie sur* (Ω, *A*, **P**) *à valeurs dans* (*E*, *E*)*, et de loi* **P***<sub>X</sub>. Soit h* : (*E*, *E*) *7→* (**R**, *B*(**R**)) *une application mesurable. a) On a h*(*X*) *∈ L*<sup>1</sup>(Ω, *A*, **P**) *⇔ h ∈ L*<sup>1</sup>(**R**, *B*(**R**), **P***<sub>X</sub>*)*. b) Si h est positive satisfaisant à a*) *alors on a*
>
> Z

**E**\[*h*(*X*)\] =

**R**

*h*(*x*) *d***P***<sub>X</sub>*(*x*).

Sous réserve que a) ou b soit vrai, alors on a l'égalité

> *Preuve:* Rappelons que par définition **P***<sub>X</sub>*(*B*) = **P**(*X<sup>−</sup>*<sup>1</sup>(*B*)) pour tout *B ∈ B*(**R**). Or **E**\[**1***<sub>B</sub>*(*X*)\] = **P**(*X<sup>−</sup>*<sup>1</sup>(*B*)) = **P**<sub>*X*(*B*) =</sub> R**<sub>R</sub>1***<sub>B</sub>*(*x*) *d***P***<sub>X</sub>*(*x*) donc la formule est vraie pour *h* = **1***<sub>B</sub>* simple *n* = 1, pour *h* simple (étagé) quelconque on a la formule valide par linéarité de l’espérance. Si *h* est positive il existe (d’après Mesure et Intégration) une suite croissante (*h<sub>n</sub>*)*<sub>n</sub>* de fonctions mesurables positives simples telles que lim<sub>*n→*∞</sub> *h<sub>n </sub>*= *h*. Donc **E**\[*h*(*X*)\] = **E**\[lim*<sub>n</sub> h<sub>n</sub>*(*X*)\] = lim*<sub>n</sub>* **E**\[*h<sub>n</sub>*(*X*)\] = lim*<sub>n</sub>*R**<sub>R</sub>***h<sub>n</sub>*(*x*) *d***P**<sub>*X*(*x*) =</sub> R**<sub>R</sub>**lim*<sub>n</sub> h<sub>n</sub>*(*x*) *d***P**<sub>*X*(*x*) =</sub> R**<sub>R</sub>***h*(*x*) *d***P***<sub>X</sub>*(*x*), où on a utilisé deux fois le TCM. Cela prouve *b*) quand *h* est positive. En appliquant à *\|h\|*, cela prouve aussi *a*) (rappelons que *X ∈ L*<sup>1</sup>ssi **E**\[*\|X\|*\] *\<* ∞). Enfin en écrivant *h* = *h*<sup>+</sup> *− h<sup>− </sup>*on déduit la formule demandée pour *h* de signe quelconque de la même formule pour *h* positive par soustraction. □
>
> Le résultat suivant peut se déduire de ce théorème, cela sera prouvée plus tard.
>
> **Corollaire 6** *Soit X une v.a. réelle admettant une densité f<sub>X</sub> (i.e.* **P**(*X ≤ <sub>x</sub>*<sub>) =</sub> R *<sup>x</sup><sub>−</sub>*<sub>∞</sub>*f<sub>X</sub>*(*u*) *du pour tout x ∈* **R***). Si* **E**\[*\|h*(*X*)*\|*\] *\<* ∞ *ou si h est <sub>positive, on a </sub>*<sub>**E**\[*h*(*X*)\] =</sub> R**<sub>R</sub>***h*(*x*)*f<sub>X</sub>*(*x*) *dx.*
>
> *6. Variables aléatoires indépendantes et Lois de probabilités sur* **R**
>
> *0.1 Variables aléatoires indépendantes*
>
> Rappelons que deux événements *A* et *B* sont indépendants si la connaissance du fait que *B* est réalisé ne change pas la probabilité de *A*, ce qui revient à dire que **P**(*A ∩ B*) = **P**(*A*)**P**(*B*). De même une famille quelconque (*A<sub>i</sub>*)*<sub>i∈I</sub>* d’événements est indépendante si **P**(*∩<sub>j∈J</sub> A<sub>j</sub>*) = ∏*<sub>j∈J</sub>* **P**(*A<sub>j</sub>*) pour tout sous-ensemble fini *J* de *I*. De manière analogue, deux v.a. *X* et *Y* seront indépendantes si *{Y ∈ A}* et *{X ∈ B}* sont indépendants pour tous *A* et *B* dans les tribus correspondantes.
>
> Si *X* est mesurable de (Ω, *A*) dans (*E*, *E*), on rappelle (voir Mesure et Intégration) que la tribu engendrée par *X* est *X<sup>−</sup>*<sup>1</sup>(*E*) = *{X<sup>−</sup>*<sup>1</sup>(*A*) : *A ∈ E }*.
>
> **Définition 18** *a) Soit* (*A<sub>i</sub>*)*<sub>i∈I</sub> une famille de sous-tribus de A. Les tribus A<sub>i</sub>sont indépendantes si pour tout partie finie de J de I et tous A<sub>i</sub> ∈ A<sub>i</sub> on a*

**P**(*∩<sub>j∈J</sub> A<sub>j</sub>*<sup>) =</sup> ∏ *j∈J*

**P**(*A<sub>j</sub>*).

> *b) Soit* (*X<sub>i</sub>*)*<sub>i∈I</sub> une famille de variables aléatoires, à valeurs respectives dans les* (*E<sub>i</sub>*, *E<sub>i</sub>*)*. Les variables aléatoires X<sub>i</sub>sont indépendantes si les tribus engendrées X<sup>−</sup>*<sup>1</sup>
>
> *<sub>i</sub>*(*E<sub>i</sub>*) *sont indépendantes.*
>
> Dans la suite de ce chapitre nous considérons essentiellement des couples de v.a., de façon à garder des notations simples. Tous les résultats s’étendent de manière évidente aux familles finies de v.a.
>
> Noter que *X* et *Y* prennent leurs valeurs dans (*E*, *E*) et (*F*, *F*) respec tivement : les espace *E* et *F* peuvent être différents.
>
> **Théorème 23** *Pour que X et Y soient indépendantes, il faut et il suffit que l’une des conditions équivalentes ci-dessous soit satisfaite :*
>
> *a)* **P**(*X ∈ A*,*Y ∈ B*) = **P**(*X ∈ A*)**P**(*Y ∈ B*) *pour tous A ∈ E*, *B ∈ F.*
>
> 30
>
> *b)* **P**(*X ∈ A*,*Y ∈ B*) = **P**(*X ∈ A*)**P**(*Y ∈ B*) *pour tous A ∈ C, B ∈ D, où σ*(*C*) = *E et σ*(*D*) = *F avec E et F des classes de parties de* **E** *et F, stables par intersection finie.*
>
> *c) f*(*X*) *et g*(*Y*) *sont indépendantes pour tout couple* (*f* , *g*) *de fonctions mesurables réelles sur E et F respectivement.*
>
> *d)* **E**\[ *f*(*X*)*g*(*Y*)\] = **E**\[ *f*(*X*)\]**E**\[*g*(*Y*)\] *pour tout couple* (*f* , *g*) *de fonctions mesurables réelles, bornées (ou positives) sur E et F respectivement.*
>
> *e) Si de plus E et F sont des espaces métriques avec leurs tribus boréliennes respectives E et F, alors* **E**\[ *f*(*X*)*g*(*Y*)\] = **E**\[ *f*(*X*)\]**E**\[*g*(*Y*)\] *pour tout couple* (*f* , *g*) *de fonctions mesurables continues réelles bornées.*
>
> *Preuve:* Comme *X<sup>−</sup>*<sup>1</sup>(*A*) = *{X ∈ A}* et *X<sup>−</sup>*<sup>1</sup>(*B*) = *{X ∈ B}* pour tous *A ∈ E* et *B ∈ F* d’où *a*).
>
> L’implication *a*) *⇒ b*) est triviale.
>
> Pour l’implication *b*) *⇒ a*) : La classe *C<sub>B </sub>*des ensembles *A ∈ E* vérifiant **P**(*X ∈ A*,*Y ∈ B*) = **P**(*X ∈ A*)**P**(*Y ∈ B*) pour *B ∈ D* donné est stable par limites croissantes et par différence, et contient *C* par hypothèse, tandis que *C* est stable par intersection. Le théorème des classes monotones entraîne alors que *C<sub>B </sub>*= *E*. En d’autres termes on a *b*) avec *C* = *E*. De manière analogue (en fixant *A ∈ E*) on obtient qu’on a *b*) avec de plus *D* = *F* : en d’autres termes, on a *a*).
>
> Pour l’implication *c*) *⇒ a*) : il suffit de prendre *f*(*x*) = *x* et *g*(*y*) = *y* (les applications identité sur *E* et *F* respectivement). Pour l’implication *a*) *⇒ c*) : Ètant données *f* et *g*, on voit que *f*(*X*)<sup>*−*1</sup>(*E*) = *X<sup>−</sup>*<sup>1</sup>(*f<sup>−</sup>*<sup>1</sup>(*E*)) *⊂ X<sup>−</sup>*<sup>1</sup>(*E*), et de même *g*(*Y*)<sup>*−*1</sup>(*F*) *⊂ Y<sup>−</sup>*<sup>1</sup>(*F*) : le résultat est alors évident.
>
> L’implication *d*) *⇒ a*) : Prendre *f*(*x*) = **1***<sub>A</sub>*(*x*) et *g*(*x*) = **1***<sub>B</sub>*(*x*). *a*) *⇒ d*) : Par hypothèse on a *d*) pour *f* et *g* fonctions indicatrices, et donc pour *f* et *g* fonctions simples par linéarité. Si *f* et *g* sont positives il existe des suites (*f<sub>n</sub>*)*<sub>n</sub>* et (*g<sub>n</sub>*)*<sub>n</sub>* de fonctions simples po sitives croissant vers *f* et *g* respectivement. Noter que les produits *f<sub>n</sub>*(*X*)*g<sub>n</sub>*(*Y*) croissent vers *f*(*X*)*g*(*Y*). En appliquant le TCM il vient alors **E**\[ *f*(*X*)*g*(*Y*)\] = **E**\[ lim<sub>*n→*∞</sub>*f<sub>n</sub>*(*X*)*g<sub>n</sub>*(*Y*)\] = lim<sub>*n→*∞</sub>**E**\[ *f<sub>n</sub>*(*X*)*g<sub>n</sub>*(*Y*)\] = lim<sub>*n→*∞</sub>**E**\[ *f<sub>n</sub>*(*X*)\]**E**\[*g<sub>n</sub>*(*Y*)\] = lim<sub>*n→*∞</sub>**E**\[ *f<sub>n</sub>*(*X*)\] lim<sub>*n→*∞</sub>**E**\[*g<sub>n</sub>*(*Y*)\] = **E**\[ *f*(*X*)\]**E**\[*g*(*Y*)\]. On a donc le résultat lorsque *f* et *g* sont positives. Lorsque *f* et *g* sont bornées on écrit *f* = *f*<sup>+</sup> *− f<sup>− </sup>*et *g* = *g*<sup>+</sup> *− g<sup>−</sup>*, et on conclut par linéarité.
>
> *d*) *⇒ e*) : Évident.
>
> *e*) *⇒ b*) : Il suffit de montrer *b*) lorsque *C* et *D* sont les classes de tous les fermés de *E* et *F* (ces classes sont stables par intersection). Soit par exemple *A* un fermé de *E* ; si *f<sub>n</sub>*(*x*) = min(1, *nd*(*x*, *A*)), où *d*(*x*, *A*) désignae la distance du point *x* au fermé *A*, alors *f<sub>n </sub>*est continue, et vérifie 0 *≤ f<sub>n</sub> ≤* 1 et décroît vers l’indicatrice **1***<sub>A</sub>*. Pour

31

> *B* fermé de *F* soit de même une suite (*g<sub>n</sub>*)*<sub>n</sub>* de fonctions continues
>
> 0 *≤ g<sub>n</sub> ≤* 1 et convergeant vers **1***<sub>B</sub>*. On peut reproduire la fin de la
>
> preuve de l’implication *a*) *⇒ d*) en remplaçant le TCM par celui de la

convergence dominée, pour obtenir *b*). □ Rappelons (voir Mesure et Intégration)

Rappel d’un théorème de Mesure et Intégration :

**Théorème 24** *Soit f* : (*E × F*, *E ⊗ F*) *→* (*R*, *B*(**R**)) *mesurable. Pour tout x ∈ E, y 7→ f*(*x*, *y*) *est une fonction F-mesurable ; de même pour tout y ∈ F la fonction x 7→ f*(*x*, *y*) *est E-mesurable.*

**Théorème 25 (Tonelli-Fubini)** *Soient* **P** *et* **Q** *des probabilités sur* (*E*, *E*) *et* (*F*, *F*) *respectivement.*

*(a) Posons R*(*A × B*) = **P**(*A*)**Q**(*B*) *pour tous A ∈ E et B ∈ F. Alors R s’étend de manière unique en une probabilité sur* (*E × F*, *E ⊗ F*)*, notée* **P** *⊗* **Q***.*

*(b) Pour toute fonction f* : (*E × F*, *E ⊗ F*) *→* (**R**, *B*(**R**)) *positive ou* <sub>**P** *⊗* **Q***-intégrable, la fonction x 7→ *</sub>R*<sub>F</sub>f*(*x*, *y*)**Q**(*dy*) *est E-mesurable, la <sub>fonction y 7→ </sub>*R*<sub>E</sub>f*(*x*, *y*)**P**(*dx*) *est F-mesurable, et on a*

qu’en général *E*, *F* tribus respectives sur *E* et *F* n’impliquent pas que le produit cartésien *E × F* est une tribu sur *E × F*. La plus petite tribu de *E × F* contenant *E × F*, soit *σ*(*E × F*) est très fréquemment rencontrée et est notée ainsi : *E ⊗ F* = *σ*(*E × F*).

*Preuve:* (du théorème 24)

Supposons d’abord *f* de la

forme *f*(*x*, *y*) = **1***<sub>C</sub>*(*x*, *y*), pour

*C ∈ E ⊗ F*. Soit *H* = *{C ∈ E ⊗ F* : *y 7→* **1***<sub>C</sub>*(*x*, *y*) est *F*-mesurable pour chaque *x ∈ E* fixé*}*. Alors *H* et une tribue (facile) contenant *E × F*, donc *σ*(*E × F*) *⊂ H*. Comme par construction *H ⊂ σ*(*E × F*), il vient *H* = *E ⊗ F*. On a donc montré le résultat pour les fonctions indicatrices, donc par linéarité pour les fonctions mesurables simples. Par

Z

*<sub>E×F</sub>f d*(**P** *⊗* **Q**) = =

Z

*E*

Z *F*

<sub>Z</sub>

*F*

<sub>Z</sub> *E*

*f*(*x*, *y*)**Q**(*dy*) *f*(*x*, *y*)**P**(*dx*)

**P**(*dx*)

**Q**(*dy*).

limite croissante, on l’obtient aussi pour les fonctions mesurables positives. Enfin par différence *f* = *f*<sup>+</sup> *− f<sup>−</sup>*, on l’obtient pour les fonctions mesurables quelconques.

□

> *Preuve:* Voir Théorème 10.3 p.71 de 1. □
>
> **Corollaire 7** *Soient X et Y deux v.a. sur* (Ω, *A*, **P**) *à valeurs respectives dans* (*E*, *E*) *et* (*F*, *F*)*. Le couple Z* := (*X*,*Y*) *peut être considéré comme une v.a. à valeurs dans* (*E × F*, *E ⊗ F*) *et les deux v.a. X et Y sont indépen dantes si et seulement si la loi* **P**<sub>(*X*,*Y*)</sub>*du couple égale le produit* **P***<sub>X</sub> ⊗* **P***<sub>Y</sub>.*
>
> *Preuve:* Il est évident que *Z<sup>−</sup>*<sup>1</sup>(*A × B*) = *X<sup>−</sup>*<sup>1</sup>(*A*) *∩ Y<sup>−</sup>*<sup>1</sup>(*B*) *∈ A* si *A ∈ E* et *B ∈ F*, de sorte que la mesurabilité de *Z* découle de la définition de la tribu *E ⊗ F* et du Théorème 16. L’indépendance de *X* et *Y* revient au fait que pour tous *A ∈ E* et *B ∈ F* on ait **P**((*X*,*Y*) *∈ A × B*) = **P**(*X ∈ A*)**P**(*Y ∈ B*), ce qui équivaut à **P**<sub>(*X*,*Y*)</sub>(*A × B*) = **P***<sub>X</sub>*(*A*)**P***<sub>Y</sub>*(*B*), de sorte que l’unicité de la probabilité produit dans le théorème de Fubini nous donne la seconde assertion. □
>
> *•* Nous faisons maintenant une légère digression en construi sant un modèle pour des variables aléatoires indépendantes, ce qui permet en particulier de vérifier que cette notion n’est pas vide. *•* Soit d’abord *µ* une probabilité sur un espace mesurable (*E*, *E*). Il est facile de construire une v.a. *X* à valeurs dans *E* et de loi *µ* : prendre
>
> 32
>
> simplement Ω = *E*, *A* = *E*, **P** = *µ*, et prendre pour *X* l’identité (*X*(*x*) = *x*).
>
> *•* Un peu plus compliquée est la construction d’un couple de deux v.a. indépendantes *X* et *Y*, à valeurs dans (*E*, *E*) et (*F*, *F*), et de lois respectives *µ* et *ν* (probabilités données a priori sur *E* et *F*) : on peut prendre Ω = *E × F*, *A* = *E ⊗ F*, **P** = *µ ⊗ ν*, et *X*(*x*, *y*) = *x* et *Y*(*x*, *y*) = *y*, où (*x*, *y*) *∈ E × F*.
>
> Il est malheureusement bien plus compliqué, mais indispensable pour les applications (loi loi des grands nombres par exemple qu’on verra plus tard, ou même l’étude d’une suite infinie de jets de dés, etc. . .) de construire une suite infinie de v.a. indépendantes de lois données. Plus précisément, pour chaque entier *n* on se donne une v.a. *X<sub>n </sub>*définie sur un espace de probabilité (Ω, *A<sub>n</sub>*, **P***<sub>n</sub>*), à valeurs dans (*E<sub>n</sub>*, *E<sub>n</sub>*) et de loi *µ<sub>n </sub>*(pour construire chaque *X<sub>n </sub>*on peut opérer comme ci-dessus).
>
> Ensuite, on pose Ω = ∏<sup>∞</sup><sub>*n*=1</sub> Ω*<sub>n</sub>* (produit cartésien dénombrable), *A* =<sup>N∞</sup><sub>*n*=1</sub> *A<sub>n </sub>*où <sup>N∞</sup><sub>*n*=1</sub> *A<sub>n </sub>*désigne la plus petite tribu de Ω à laquelle appartiennent tous les ensembles suivants : *A*<sub>1</sub> *× A*<sub>2</sub> *× · × A<sub>k</sub> ×* Ω<sub>*k*+1</sub> *×* Ω<sub>*k*+2</sub> *× ·*, *A<sub>i</sub> ∈ A<sub>i</sub>*, *k ∈* **N***<sup>∗</sup>*.
>
> Le théorème suivant constitue un résultat non trivial de la théorie de la Mesure et généralise le théorème de Fubini.
>
> **Théorème 26 (dû à Cassius Ionescu-Tulcea)** *Avec les notations ci dessus, il existe une probabilité* **P** *et une seule sur* (Ω, *A*) *telle que* **P**(*A*<sub>1</sub> *× · × A<sub>k</sub> ×* Ω<sub>*k*+1</sub> *×* Ω<sub>*k*+2</sub> *× ·*) = ∏*<sup>k</sup><sub>i</sub>*<sub>=1</sub> **P***<sub>i</sub>*(*A<sub>i</sub>*) *pour tous k ∈* **N***<sup>∗</sup>, et A<sub>i</sub> ∈ A<sub>i</sub>. Maintenant, on note <sub>X</sub>*e*<sub>n</sub> l’extension naturelle de X<sub>n</sub> à* Ω*, c’est-à-dire que pour chaque ω* := (*ω*<sub>1</sub>, *ω*<sub>2</sub>, . . . , *ω<sub>n</sub>*, . . .) *∈* Ω *avec ω<sub>i</sub> ∈* Ω*<sub>i</sub> on pose <sub>X</sub>*e*<sub>n</sub>*(*ω*) = *X<sub>n</sub>*(*ω<sub>n</sub>*)*.*
>
> *Preuve:* Pour une preuve voir par exemple Theorem 16.6 (p. 150) de 2. □
>
> <sub>**Corollaire 8 (Lomnick-Ulam)** *Les variables aléatoires X*</sub>e*<sub>n</sub> ci-dessus sont <sub>indépendantes, et chaque X</sub>*e*<sub>n</sub> a la loi µ<sub>n</sub>.*
>
> *Preuve:* Soit *B<sub>n</sub> ∈ E<sub>n</sub>*. On a *<sub>X</sub>*e<sup>*−*1</sup>
>
> *<sub>n</sub>*(*B<sub>n</sub>*) = Ω<sub>1</sub> *×* . . . *×* Ω<sub>*n−*1</sub> *× X<sup>−</sup>*<sup>1</sup>

*<sub>n</sub>*(*B<sub>n</sub>*) *×*

> Ω<sub>*n*+1</sub> *×* Ω<sub>*n*+2</sub> *×* . . . et le théorème ci-dessus nous donne que pour tout *k ∈* **N***<sup>∗</sup>*:
>
> **P**(*∩<sup>k</sup><sub>n</sub>*<sub>=1*X*</sub>f*<sub>n</sub><sup>−</sup>*<sup>1</sup>(*B<sub>n</sub>*)) = **P**(*X<sup>−</sup>*<sup>1</sup>
>
> <sub>1</sub>(*B*<sub>1</sub>) *×* . . . *× X<sup>−</sup>*<sup>1</sup>

*<sub>k</sub>*(*B<sub>k</sub>*) *×* Ω<sub>*k*+1</sub> *×* . . .)

=

*k*

∏*n*=1

**P***<sub>n</sub>*(*X<sub>n</sub> ∈ B<sub>n</sub>*) =

*k*

∏*n*=1

*µ<sub>n</sub>*(*B<sub>n</sub>*).

> <sub>En particulier **P**(*X*</sub>e*<sub>n</sub> ∈ B<sub>n</sub>*) = *µ<sub>n</sub>*(*B<sub>n</sub>*).
>
> P.S. Le résultat original est dans 3 (1934). □

33

> **Théorème 27 (Lemme de Borel-Cantelli)** *Soit* (*A<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite*
>
> *d’événements sur* (Ω, *A*, **P**)*. Alors on a :*
>
> *a) Si* ∑<sup>∞</sup><sub>*n*=1</sub> **P**(*A<sub>n</sub>*) *\<* ∞*, alors* **P**(*A<sup>∗</sup>*) = 0*.*
>
> *b) Si* **P**(*A<sup>∗</sup>*) = 0 *et si les A<sub>n</sub>*, *n ∈* **N***<sup>∗</sup>sont indépendants, alors on a*
>
> ∑<sup>∞</sup><sub>*n*=1</sub> **P**(*A<sub>n</sub>*) *\<* ∞*.<sub>{ω ∈ A</sub><sup>∗</sup>}* = *{A<sub>m</sub> i*.*s*.*}*, *A<sup>∗ </sup>*= lim sup<sub>*n→*∞</sub> *A<sub>n </sub>*= *∩*<sup>∞</sup><sub>*n*=1</sub> *∪<sub>m≥n</sub> A<sub>m</sub>*.

*Preuve: a*) : Soit *a<sub>n </sub>*= **P**(*A<sub>n</sub>*) = **E**\[**1***<sub>An</sub>*\], donc d’après *b*) du Théo rème 19 on a ∑<sup>∞</sup><sub>*n*=1</sub>*a<sub>n</sub> \<* ∞ implique ∑<sup>∞</sup><sub>*n*=1</sub>**1***<sub>An</sub> \<* ∞ p.s. Comme ∑<sup>∞</sup><sub>*n*=1</sub>**1***<sub>An</sub>*(*ω*) = ∞ ssi *ω ∈ A<sup>∗ </sup>*d’où *a*) prouvé.

Nous verrons plus bas (comme cas particulier de la "loi 0 *−* 1") que si les *A<sub>n</sub>* sont indépendants, **P**(*A<sup>∗</sup>*) *∈ {*0, 1*}*. Par suite si la série ∑<sup>∞</sup><sub>*n*=1</sub> **P**(*A<sub>n</sub>*) converge

*b*) : **P**(*A<sup>∗</sup>*) = lim<sub>*n→*∞</sub>lim

<sub>*k→*∞</sub>∏*<sup>k</sup><sub>m</sub>*<sub>=*n*</sub>(1 *− a<sub>m</sub>*)

on a **P**(*A<sup>∗</sup>*) = 0, et si elle diverge on a

<sub>*k→*∞</sub>**P**(*∪<sup>k</sup><sub>m</sub>*<sub>=*n*</sub>*A<sub>m</sub>*) = 1 *−* lim<sub>*n→*∞</sub>lim

<sub>*k→*∞</sub>∏*<sup>k</sup><sub>m</sub>*<sub>=*n*</sub>(1 *− a<sub>m</sub>*) = 1, d’où avec *ln*

par indépendance, donc lim<sub>*n→*∞</sub>lim

<sub>*k→*∞</sub>∑*<sup>k</sup><sub>m</sub>*<sub>=*n*</sub>ln(1 *− a<sub>m</sub>*) = 0, i.e. lim<sub>*n→*∞</sub>∑*<sub>m≥n</sub>*ln(1 *− a<sub>m</sub>*) =

on obtient lim<sub>*n→*∞</sub>lim

0, or *\|* ln(1 *− x*)*\| ≥ x* pour 0 *≤ x \<* 1, d’où ∑*<sub>m</sub> a<sub>m </sub>*converge i.e. ∑<sup>∞</sup><sub>*n*=1</sub> **P**(*A<sub>n</sub>*) *\<* ∞. □ Soit maintenant des v.a. *X<sub>n </sub>*définies sur (Ω, *A*, **P**). Soient les tribus *B<sub>n </sub>*= *σ*(*X<sub>n</sub>*), *C<sub>n </sub>*= *σ*(*∪<sub>p≥n</sub>B<sub>p</sub>*) et *C*<sub>∞</sub> = *∩*<sup>∞</sup><sub>*n*=1</sub>*C<sub>n</sub>*.

*C*<sub>∞</sub> est appelée la tribu asymptotique. Un événement est dans cette tribu s’il ne dépend que du comportement de la suite *X<sub>n </sub>*lorsque *n →* ∞ (d’où son nom) : voici des exemples de v.a. *C*<sub>∞</sub>- mesurables juste après le théorème suivant.

**Théorème 28 (Loi** 0 *−* 1**)** *Soit* (*X<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite de v.a. indépendantes définies sur* (Ω, *A*, **P**)*, et soit C*<sub>∞</sub> *la tribu asymptotique associée. Pour tout C ∈ C*<sub>∞</sub>*, on a* **P**(*C*) *∈ {*0, 1*}.*

*Preuve:* Soit *D<sub>n </sub>*= *σ*(*∪<sub>p\<n</sub>B<sub>p</sub>*). Par hypothèse les tribus *C<sub>n </sub>*et *D<sub>n</sub>* sont indépendantes, donc si *A ∈ C<sub>n </sub>*et *B ∈ D<sub>n </sub>*on a **P**(*A ∩ B*) = **P**(*A*)**P**(*B*). Si *A ∈ C*<sub>∞</sub> nous avons donc **P**(*A ∩ B*) = **P**(*A*)**P**(*B*) pour tout *B ∈ D<sub>n </sub>*donc aussi pour tout *B ∈ D* = *σ*(*∪<sub>n</sub>D<sub>n</sub>*), par le théorème des classes monotones. Cependant *C*<sub>∞</sub> *⊂ D*, donc on a *B* = *A ∈ C*<sub>∞</sub>, qui implique **P**(*A ∩ A*) = **P**(*A*)**P**(*A*) = **P**(*A*)<sup>2</sup>, donc **P**(*A*) *∈ {*0, 1*}*. □ **Conséquence.** Si les v.a. *X*<sub>1</sub>, *X*<sub>2</sub>, . . . , *X<sub>n</sub>*, . . . sont indépendantes, on a 1. *{ω ∈* Ω : lim<sub>*n→*∞</sub> *X<sub>n</sub>*(*ω*) existe*} ∈ C*<sub>∞</sub>, donc soit la suite (*X<sub>n</sub>*)*<sub>n</sub>* converge p.s. soit elle diverge p.s.

2\. Chaque v.a. qui est *C*<sub>∞</sub>-mesurable (pour une preuve voir le TD)

**P**(*A<sup>∗</sup>*) = 1.

> est p.s. constante. En particulier pour *Y ∈ {X*, *X}*, lim sup

*Y<sub>n</sub>*,

*n→*∞

> <sub>*n→*∞</sub>*Y<sub>n</sub>*, sont toutes p.s. constantes, où *X<sub>n </sub>*:= <sup><u>1</u></sup>*~~<sub>n</sub>~~* ∑*<sup>n</sup><sub>p</sub>*<sub>=1</sub> *X<sub>p</sub>*. lim inf
>
> *0.2 Lois de probabilités sur* **R**
>
> **Rappel 1** : Les intégrales (dites impropres) sur des intervalles non bornés sont définies de la façon suivante. Soit *f* une fonction définie
>
> 34
>
> sur \[*a*, +∞\[, elle est dite localement Riemann intégrable, si elle est
>
> Riemann intégrable sur tout compact \[*a*, *x*\], avec *x ≥ a*. L’intégrale
>
> R <sub>∞</sub>
>
> *<sub>a</sub>f*(*t*) *dt* est dite convergente (resp. absolument convergente) si
>
> R *<sub>x</sub>*
>
> *<sub>a</sub>f*(*t*) *dt* <sub>(resp.</sub> R *<sup>x</sup><sub>a</sub>\| f*(*t*)*\| dt*) existe et est finie pour tout *x ≥ a* et
>
> admet une limite finie lorsque *x →* ∞.
>
> **Rappel 2** :
>
> **Théorème 29** *Soit f une fonction Riemann intégrable sur* \[*a*, *b*\]*. Alors,*
>
> *il existe g ∈ L*<sup>1</sup>**<sub>R</sub>**(\[*a*, *b*\], *B*(\[*a*, *b*\]), *λ*) *telle que f* = *g λ-p.p., et telle que*
>
> R
>
> <sub>\[*a*,*b*\]*f*(*x*) *dλ*(*x*) =</sub> R<sub>\[*a*,*b*\]</sub>*f*(*x*) *dx.*
>
> *En particulier, si f est en plus mesurable, alors f ∈ L*<sup>1</sup>**<sub>R</sub>**(\[*a*, *b*\], *B*(\[*a*, *b*\]), *λ*)
>
> *et les deux intégrales coïncident.*

Un exemple de fonction Lebesgue

Ce théorème implique que les intégrales de Lebesgue et de Riemann de fonctions admettant une limite à gauche et une limite à droite en tout point (où cela a un sens) de \[*a*, *b*\], coïncident.

**Théorème 30 ( Riemann-Lebesgue (1902))** *Soit f une fonction locale ment Riemann intégrable, d’intégrale absolument convergente sur* \[*a*, +∞\[*. Alors, il existe g ∈ L*<sup>1</sup>**<sub>R</sub>**(\[*a*, +∞\[, *B*(\[*a*, +∞\[, *λ*) *telle que f* = *g λ-p.p., et*

*<sub>telle que</sub>* R <sub>∞</sub>

<sub>*af*(*x*) *dλ*(*x*) =</sub> R <sub>∞</sub>

*<sub>a</sub>f*(*x*) *dx.*

Une fonction borélienne est intégrable au sens de Lebesgue si et seulement si *f*<sup>+</sup> et *f<sup>− </sup>*sont intégrables, où *f* = *f*<sup>+</sup> *− f<sup>− </sup>*avec *f<sup>± </sup>*:= max(*± f* , 0).

**Définition 19** *La densité d’une probabilité* **P** *sur* (**R**, *B*(**R**)) *est une fonction borélienne positive f qui vérifie pour tout x ∈* **R** *:*

intégrable qui n’est pas Riemann inté grable : soit *f*(*x*) = **1<sub>Q</sub>**<sub>*∩*\[0,1\]</sub>(*x*) pour tout

<sub>*x ∈* **R**. Montrer que</sub> R**<sub>R</sub>***f*(*x*) *dλ*(*x*) = 0, mais que *f* n’est pas Riemann inté grable sur \[0, 1\].

localement Riemann intégrable \<=\> intégrable pour tout segment sur la def de f

**P**(\] *−* ∞, *x*\]) =

Z *<sub>x</sub>*

<sub>*−*∞</sub>*f*(*y*) *dy* =

Z

**R**

*f*(*y*)**1**<sub>\]*−*∞,*x*\]</sub>(*y*) *dy*.

> *Si* **P** = **P***<sub>X</sub>, la loi d’une v.a. réelle X, on dit alors que X admet la densité f (on dit aussi f est une densité de X).*
>
> **Remarque** : Comme on l’a déjà vu, il n’est pas vrai que toute pro babilité sur (**R**, *B*(**R**)) admette une densité, puisque dans ce cas la fonction de répartition *F* est continue, ce qui n’est pas vrai de toutes les fonctions de répartition. Il existe même des fonctions de répartition continues qui n’admettent pas de densité.

35

> **Théorème 31** *a) Une fonction borélienne positive f sur* **R** *est la den*
>
> *sité d’une probabilité* **P** *sur* (**R**, *B*(**R**))) *si et seulement si elle vérifie*
>
> R
>
> **<sub>R</sub>***f*(*x*) *dx* = 1*. Dans ce cas elle détermine la probabilité de ma*
>
> *nière unique, et toute autre fonction borélienne positive g vérifiant*
>
> *λ*(*f ̸*= *g*) = 0 *est aussi une densité de* **P***.*
>
> *b) Inversement si une probabilité admet une densité, celle-ci est déterminée*
>
> *de manière unique à un ensemble de mesure de Lebesgue nulle près (i.e. si*
>
> *f et g sont deux densités pour la même probabilié, on a λ*(*f ̸*= *g*) = 0*).*
>
> *Preuve:* Voir le Théorème 11.3 (p.78) de 1. □
>
> **Remarque** : La densité *f* et la fonction de répartition *F* étant
>
> <sub>liées par *F*(*x*) =</sub> R *<sup>x</sup><sub>−</sub>*<sub>∞</sub>*f*(*y*) *dy*, on est tenté de conclure que *F* est
>
> dérivable et que sa dérivée vaut *F<sup>′</sup>*(*x*) = *f*(*x*). C’est vrai en tout
>
> point *x* où la fonction est continue. On peut montrer (c’est un résultat
>
> difficile dû à Lebesgue, Théorème de différentiation de Lebesgue
>
> (1904)) que c’est vrai pour *λ*-presque tout *x*. Comme *f* n’est définie
>
> de manière unique qu’à un ensemble de mesure de Lebesgue nulle
>
> près, "concrètement" si on connaît *F* et si on sait que *f* existe (par
>
> exemple si *F* est continue partout et dérivable par morceaux), on
>
> peut prendre pour *f* la dérivée de *F* partout où celle-ci existe, et des
>
> valeurs arbitraires (par exemple 0) ailleurs.
>
> **Corollaire 9** *Soit X une v.a. réelle admettant la densité de f . Si g est une*
>
> *fonction borélienne sur* **R***, elle est intégrable (resp. admet une intégrale) par*
>
> *rapport à la loi* **P***<sub>X</sub> de X si et seulement si la fonction production g f<sub>X</sub> est*
>
> *intégrable (resp. admet une intégrale) par rapport à la mesure de Lebesgue,*
>
> *et on a alors*

**E**\[*g*(*X*)\] =

Z

**R**

*g*(*x*) **P***<sub>X</sub>*(*dx*) =

Z

**R**

*g*(*x*)*f<sub>X</sub>*(*x*) *dx*.

> *Preuve:* L’égalité est satisfaite pour les fonctions *g* indicatrices grâce <sub>au Théorème 31, car elle se réduit alors à la forme **P**(*A*) =</sub> R*<sub>A</sub>f*(*y*) *dy*. Par linéarité elle est donc vraie pour les fonctions boréliennes
>
> simples, puis par limite croissante pour les fonctions boréliennes positives. Pour les fonctions de signe quelconque, on déduit le résul tat par linéarité encore, en utilisant les décompositions *g* = *g*<sup>+</sup> *− g<sup>− </sup>*et *g f<sub>X </sub>*= *g*<sup>+</sup> *f<sub>X</sub> − g<sup>−</sup> f<sub>X</sub>*. □
>
> Soit *X* une v.a. réelle de densité *f<sub>X</sub>*. Soit *Y* = *g*(*X*) une nouvelle v.a. avec *g* borélienne, peut-on exprimer la densité de *Y* si elle existe, en termes de *f<sub>X </sub>*et *g* ? On le peut dans les "bons cas", par exemple :
>
> **Théorème 32** *Soit X une v.a. de densité f<sub>X</sub> et g une fonction borélienne. Soit Y* = *g*(*X*)*. La fonction de répartition de Y est*
>
> Z

*F<sub>Y</sub>*(*y*) = **P**(*Y ≤ y*) =

*A<sub>y</sub>*

*f<sub>X</sub>*(*u*) *dy*, *où A<sub>y </sub>*= *g<sup>−</sup>*<sup>1</sup>(\] *−* ∞, *y*\]).

> 36
>
> Si *F<sub>Y </sub>*est continue partout et dérivable sauf en un nombre fini de
>
> points, on peut utiliser le résultat ci-dessus pour obtenir la densité *f<sub>Y</sub>*
>
> de *Y*.
>
> **Exemple 16** *Soit X ∼ U*(\[0, 1\]) *et Y* = *−* <sup><u>1</u></sup>*~~<sub>λ</sub>~~*ln(*X*) *où λ \>* 0*. Alors*
>
> *F<sub>Y</sub>*(*y*) = **P**(*X ≥ e<sup>−λy</sup>*) = (1 *− e<sup>−λy</sup>*)**1<sub>R</sub>**<sub>+</sub>(*y*) *pour tout y ∈* **R***.*
>
> *Donc f<sub>Y</sub>*(*y*) = *<sup><u>d</u></sup>~~<sub>dy</sub>~~ F<sub>Y</sub>*(*y*) = *λe<sup>−λy</sup>***1<sub>R</sub>***<sup>∗</sup>*<sub>+</sub>(*y*) *pour tout y ∈* **R** *et on voit que*
>
> *Y ∼* Exp(*λ*)*.*
>
> *Attention : cet exemple est très simple car g est injective. Le résultat*
>
> *général pour g injective est donné ci-dessous, le cas non injectif étant donné*
>
> *plus bas.*
>
> **Corollaire 10** *Soit X une v.a.r. qui admet une densité f<sub>X</sub>. Soit g ∈*
>
> *C*<sup>1</sup>(**R**; **R**) *(on dit aussi continûment dérivable) dont la dérivée ne s’an*
>
> *nule pas (elle est donc strictement monotone), et soit h* = *g<sup>−</sup>*<sup>1</sup>*sa fonction*

*réciproque, qui est définie sur g*(**R**)*, continûment dérivable sur g*(**R**)*.* **Rappel** : Par définition on dit que

*Alors la v.a.r. Y* := *g*(*X*) *admet une densité f<sub>Y</sub> donnée par f<sub>Y </sub>*= *\|h<sup>′</sup>\|*(*f<sub>X</sub> ◦ h*) **1**<sub>*g*(**R**)</sub>.

*Preuve:* Supposons *g* croissante. *g*(**R**) =\]*a*, *b*\[ avec *a*, *b ∈* **R**. Soit *F<sub>Y</sub>* la fonction caractéristique de *Y*. Si *a \< y \< b* on a par la croissance de *h*, *F<sub>Y</sub>*(*y*) = **P**(*g*(*X*) *≤ y*) = **P**(*h*(*g*(*X*)) *≤ h*(*y*)) = **P**(*X ≤ h*(*y*)) = *F<sub>X</sub>*<sub>(*h*(*y*)) =</sub> R <sub>*h*(*y*)</sub>

<sub>*−*∞</sub>*f*(*x*) *dx*. On sait par ailleurs que la dérivée de *h*

est *h<sup>′ </sup>*= <u><sup>1</sup></u>

*f~~<sup>′</sup>~~*<sub>(*h*(*x*))</sub>(en effet *g* est injective, dérivable, de dérivée non nulle, donc *h* dérivable), donc *F<sub>Y </sub>*est dérivable sur \]*a*, *b*\[ et *F<sub>Y</sub>*(*y*) = *f*(*h*(*y*))*h<sup>′</sup>*(*y*) = *f*(*h*(*y*))*\|h<sup>′</sup>*(*y*)*\|*. Enfin *F<sub>Y</sub>*(*y*) = 0 si *y ≤ a*, quand *a \> −*∞, et de même *F<sub>Y</sub>*(*y*) = 1 si *y ≥ b*, quand *b \<* ∞, donc *F<sub>Y</sub>* est également dérivable, et de dérivée nulle, sur \] *−* ∞, *a*\[*∪*\]*b*, ∞\[. On en déduit le résultat. Si *g* est décroissante, pour *y ∈ g*(**R**), le même argument conduit à *F<sub>Y</sub>*(*y*) = *f*(*h*(*y*))(*−h<sup>′</sup>*(*y*)) = *f*(*h*(*y*))*\|h<sup>′</sup>*(*y*)*\|*, et on conclut comme ci-dessus.

□

**Corollaire 11** *Soit X une v.a.r. admettant une densité f<sub>Y</sub> continue par morceaux. Soit g ∈ C*<sup>1</sup>(**R**; **R**) *et strictement monotone par morceaux, i.e. il existe une partition* (*I<sub>i</sub>*)<sub>1*≤i≤n *</sub>*de* **R** *constituée d’intervalles et telle que g ∈ C*<sup>1</sup>(*I<sup>′</sup><sub>i</sub>*; *g*(*I<sup>′</sup><sub>i</sub>*))***-difféomorphisme**, I<sup>′</sup><sub>i</sub>étant l’intervalle ouvert ayant les mêmes extrémités que I<sub>i</sub>. Pour chaque i on note h<sub>i </sub>*= (*g<sub>\|I</sub>′<sub>i</sub>*)<sup>*−*1</sup>*et* Λ*<sub>i</sub>* = *g*(*I<sup>′</sup><sub>i</sub>*)*. Alors la v.a. Y* := *g*(*X*) *admet une densité f<sub>Y</sub>, définie par*

*f* : *I → J* est *C<sup>k</sup>*(*I*; *J*)-difféomorphisme si *f* est une bijection de *I* sur *J*, et si *f* et *f<sup>−</sup>*<sup>1</sup>sont de classe *C<sup>k</sup>*, i.e. *f<sup>i</sup>*existe pour tout *i ≤ k* et *f<sup>k</sup>*est continue.

Tout simplement l’hypothèse du corollaire est :

*g* est *C*<sup>1</sup>(**R**; *g*(**R**))-difféomorphisme, en effet une propriété appelée Caractérisa tion des *C<sup>k</sup>*-difféomorphismes dit que *f ∈ C<sup>k</sup>*(*I*; *f*(*I*))-difféomorphisme ssi *f ∈ C<sup>k</sup>*sur *I* et *f<sup>′</sup> ̸*= 0 sur *I*.

*f<sub>Y </sub>*=

*<sup>n</sup>*∑ *i*=1

*\|h<sup>′</sup><sub>i</sub>\|*(*f<sub>X</sub> ◦ h<sub>i</sub>*)**1**<sub>Λ*i*</sub>.

> *Preuve:* La preuve, analogue à celle du corollaire précédent, est laissée. Cette méthode de démonstration utilise la continuité par

37

> morceaux de *f<sub>X</sub>*, mais le résultat reste vrai quand *f<sub>X </sub>*est borélienne.
>
> □
>
> *7. Fonctions caractéristiques et quelques propriétés*
>
> **Définition 20** *Pour une v.a.r. X on définit* **E**\[*e<sup>iX</sup>*\] := **E**\[cos(*X*)\] + i **E**\[sin(*X*)\] *avec* i<sup>2</sup> = *−*1*.*
>
> **Définition 21** *Soit µ une mesure de probabilité sur* (**R**, *B*(**R**))*. Sa transformée de Fourier, notée µ*b*, est la fonction sur* **R** *définie µ*b(*u*) = R
>
> **<sub>R</sub>***e<sup>iux</sup> dµ*(*x*)*.*
>
> **Remarque** : *µ*b est bien définie puisque *\|e<sup>iux</sup>\| ≤* 1 et 1 *∈ L*<sup>1</sup>(**R**, *B*(*R*), *µ*).
>
> **Définition 22** *Soit X une v.a.r. Sa fonction caractéristique ϕ<sub>X</sub> est la fonction sur* **R** *définie par ϕ<sub>X</sub>*(*u*) = **E**\[*e<sup>iuX</sup>*\]*. En d’autres termes ϕ<sub>X</sub>*(*u*) =
>
> R
>
> *<sub>X</sub>e<sup>iux</sup> d***P**<sub>*X*(*x*) = **P**</sub>c*<sub>X</sub>*(*u*)*.*
>
> Ainsi on remarque que la fonction caractéristique de *X* est la transfor mée de Fourier de sa loi **P***<sub>X</sub>*.
>
> **Théorème 33** *Soit µ une probabilité sur* (**R**, *B*(**R**))*. La fonction µ*b *est bornée (de module inférieur ou égale à* 1*), continue, et vérifie µ*b(0) = 1*.*
>
> *Preuve:* Voir le Théorème 13.1 de 1 (page 111). □
>
> **Définition 23** *On dit qu’une v.a.r. X admet des moments d’ordre jusqu’à l’ordre m si X ∈ L<sup>k</sup>*(Ω) *pour tout* 1 *≤ k ≤ m.*
>
> **Théorème 34** *Soit X une v.a.r. admettant des moments jusqu’à l’ordre m. Alors ϕ<sub>X</sub> est m fois dérivable et*
>
> *ϕ*<sup>(*m*)</sup>
>
> *<sub>X</sub>*(*u*) = i*<sup>m</sup>***E**\[*X<sup>m</sup> e*<sup>i*uX*</sup>\].
>
> **Remarque et Application** :
>
> Si *X ∈ L*<sup>1</sup>(Ω) alors **E**\[*X*\] = *−*i*ϕ<sup>′</sup><sub>X</sub>*(0). Si *X ∈ L*<sup>2</sup>(Ω) alors **E**\[*X*<sup>2</sup>\] = *−ϕ<sup>′′</sup><sub>X</sub>*(0).
>
> **Théorème 35** *Soit X une v.a.r. et a ∈* **R** *avec b ∈* **R***, alors ϕ<sub>a</sub>*<sub>+*bX*</sub>(*u*) = *e*<sup>i*ua*</sup>*ϕ<sub>X</sub>*(*bu*) *pour tout u ∈* **R***.*
>
> 40
>
> **Théorème 36 (Théorème d’unicité)** *La transformée de Fourier µ*b *d’une mesure de probabilité µ sur* (**R**, *B*(**R**)) *caractérises µ : i.e. que si deux mesures de probabilités sur* (**R**, *B*(**R**)) *admettent la même transformée de Fourier, alors elles sont égales.*
>
> *Preuve:* Voir le Théorème 14.1. de 1 (page 117) □
>
> **Corollaire 12** *Deux v.a.r. X et Y sont indépendantes si et seulement si* **E**\[*e*<sup>i(*uX*+*vY*)</sup>\] = *ϕ<sub>X</sub>*(*u*)*ϕ<sub>Y</sub>*(*v*) *pour tous u*, *v ∈* **R***.*
>
> *Preuve:* Si *X* et *Y* sont indépendantes, alors c’est vrai par indépen dance. L’autre sens sera démontré en probabilité avancées lorsque nous manipulerons les vecteurs aléatoires. □
>
> *8. Sommes de variables aléatoires indé pendantes et Variables aléatoires gaus siennes*
>
> *<span class="mark">0.2.1</span> Somme de v.a. indépendantes*
>
> Une part importante des applications des probabilités découle des propriétés des sommes de v.a.r. indépendantes. Un exemple simple apparaît en statistique : si nous répétons *n* fois la même expérience indépendamment et si nous appelons *X<sub>j</sub>*le résultat de la *j*-ième expé rience, la "valeur moyenne" est donnée par *x*¯ = <sup><u>1</u></sup>*~~<sub>n</sub>~~* ∑*<sup>n</sup><sub>j</sub>*<sub>=1</sub> *X<sub>j</sub>*. La v.a. *x*¯ est alors appelée un estimateur de la moyenne *µ* de la loi commune des *X<sub>j</sub>*. La statistique étudie quand (et comment) *x*¯ converge vers *µ* quand *n →* ∞. Même une fois qu’on sait que *x*¯ tend vers *µ*, on a aussi besoin de savoir quelle taille donner à *n* pour être raisonna blement sûr que *x*¯ est proche de la vraie valeur *µ*, qui est en général inconnue. D’autres problèmes difficiles se posent aussi naturelle ment : quelle est la loi de *x*¯ ? Si on ne peut la déterminer, peut-on au moins l’approximer ? Quelle taille doit avoir *n* pour que cette approximation soit bonne ? Si on dispose d’informations complémen taires sur *µ*, comment les utiliser pour améliorer l’estimateur *x*¯ ? Bien évidemment, avant de commencer à résoudre les plus simples de ces questions, il nous faut étudier les sommes de v.a. indépendantes. Voici un premier théorème
>
> **Théorème 37** *Soient X et Y deux v.a. réelles. La loi µ<sub>Z</sub> de Z* := *X* + *Y est le produit de convolution des lois µ<sub>X</sub> et µ<sub>Y</sub> de X et Y, qui est définie par*

*µ<sub>Z</sub>*(*A*) = (*µ<sub>X</sub> ∗ µ<sub>Y</sub>*)(*A*) =

Z

**R**

Z

**R**

**1***<sub>A</sub>*(*x* + *y*) *dµ<sub>X</sub>*(*x*) *dµ<sub>Y</sub>*(*y*),

> *i.e. µ<sub>Z</sub>*<sub>(*A*) =</sub> R<sub>**R**2</sub> *g*(*z*) *d*(*µ<sub>X</sub> ⊗ µ<sub>Y</sub>*)(*z*)*, où g*(*z*) := **1***<sub>A</sub>*(*z*<sub>1</sub> + *z*<sub>2</sub>) *pour tout z ∈* **R**<sup>2</sup>*.*
>
> *Preuve:* preuve admise, sera donnée en probabilités avancées. □ **Remarque** : Donc cela monter que pour *h* : **R** *→* **R** borélienne et *Z* =
>
> 42
>
> <sub>*X* + *Y*, avec *X* et *Y* indépendantes : **E**\[*h*(*Z*)\] =</sub> R<sub>**R**2</sub> *f*(*z*) *d*(*µ<sub>X</sub> ⊗ µ<sub>Y</sub>*)(*z*)
>
> où *f*(*z*) := *h*(*z*<sub>1</sub> + *z*<sub>2</sub>) pour tout *z ∈* **R**<sup>2</sup>.
>
> **Théorème 38** *Soient X et Y deux v.a. réelles indépendantes, et Z* := *X* + *Y.*
>
> *La fonction caractéristique ϕ<sub>Z</sub> est le produit de ϕ<sub>X</sub> et ϕ<sub>Y</sub>, i.e.*
>
> *ϕ<sub>Z</sub>*(*u*) = *ϕ<sub>X</sub>*(*u*)*ϕ<sub>Y</sub>*(*u*) *∀u ∈* **R**.
>
> *Preuve:* Prenez *h*(*u*) = *e*<sup>i*uz *</sup>dans la preuve précédente. □ Remarquons que *ϕ<sub>Z</sub>*(*u*) = *ϕ<sub>X</sub>*(*u*)*ϕ<sub>Y</sub>*(*u*) pour tout *u ∈* **R** où *Z* := *X* + *Y*,

**Théorème 39** *Soient X et Y deux v.a.r. indépendantes, et Z* = *X* + *Y. Alors on a*

*a) Si X admet une densité f<sub>X</sub>, alors Z admet une densité f<sub>Z</sub> donnée par* Z

n’implique pas que *X* et *Y* sont indé pendantes.

*f<sub>Z</sub>*(*z*) =

**R**

*f<sub>X</sub>*(*z − y*) *dµ<sub>Y</sub>*(*y*).

> *b) Si de plus Y admet une densité f<sub>Y</sub>, alors* Z
>
> Z

*f<sub>Z</sub>*(*z*) =

**R**

*f<sub>X</sub>*(*z − y*)*f<sub>Y</sub>*(*y*) *dy* =

**R**

*f<sub>X</sub>*(*x*)*f<sub>Y</sub>*(*z − x*) *dx*.

> *Preuve:* Pour montrer *b*), supposons *a*) démontré, alors on a *f<sub>Z</sub>*(*z*) =
>
> R
>
> **<sub>R</sub>***f<sub>X</sub>*(*z − y*) *dµ<sub>Y</sub>*(*y*), comme *dµ<sub>Y</sub>*(*y*) = *f<sub>Y</sub>*(*y*) *dy* d’où la première égalité de *b*). La seconde s’obtient en échangeant les rôles de *X* et *Y*. Pour montrer *a*), d’après le théorème 37 on a pour tout borélien *A ∈ B*(**R**) :
>
> *µ<sub>Z</sub>*<sub>(*A*) =</sub> R**<sub>R</sub>**R**<sub>R</sub>1***<sub>A</sub>*(*x* + *y*) *dµ<sub>X</sub>*(*x*) *dµ<sub>Y</sub>*(*y*), i.e. *µ<sub>Z</sub>*<sub>(*A*) =</sub> R**<sub>R</sub>** R**<sub>R</sub>1***<sub>A</sub>*(*x* +

*y*)*f<sub>X</sub>*(*x*) *dx*

*dµ<sub>Y</sub>*(*y*), donc en posant *z* = *x* + *y*, on a *dz* = *dx* et

> on obtient *µ<sub>Z</sub>*<sub>(*A*) =</sub> R**<sub>R</sub>** R**<sub>R</sub>1***<sub>A</sub>*(*z*)*f<sub>X</sub>*<sub>(*z − y*) *dz*</sub> *dµ<sub>Y</sub>*(*y*) et avec le théorème de Fubini, on obtient la réponse. □
>
> **Théorème 40** *Soient X et Y deux v.a.r. indépendantes, de carré intégrable, alors on a σ*<sup>2</sup><sub>*X*+*Y *</sub>= *σ*<sup>2</sup>*<sub>X</sub>* + *σ*<sup>2</sup>*<sub>Y</sub>.*
>
> *Preuve:* Facile □
>
> *0.2.2 Variables aléatoires gaussiennes*
>
> Rappelons que la loi normale que l’on désigne par la notation *N* (*µ*, *σ*<sup>2</sup>), où *µ ∈* **R** et *σ*<sup>2</sup> *\>* 0, est la probabilité sur (**R**, *B*(**R**)) de

densité *f* définie par *f*(*x*) = <sup><u>*√*1</u></sup>2*πσ*<sup>2</sup>*e<sup>−</sup>*<sup><u>1</u></sup>~~<sub>2</sub>~~ *x−µ ~~σ ~~*

<sub>2</sub>

.

> Il est commode d’étendre la classe des lois normales de façon à inclure le cas où *σ*<sup>2</sup> = 0, de la manière suivante : on note *N* (*µ*, 0) la loi égale à la masse de Dirac au point *µ*, i.e. la loi d’une v.a. qui est

43

> p.s. égale à la constante *µ*. Cette loi n’admet pas de densité, aussi
>
> parle-t-on parfois de loi normale "dégénérée". La loi *N* (0, 1) s’appelle
>
> la loi normale réduite, ou standard.
>
> Si *X* est une v.a.r. de loi *N* (*µ*, *σ*<sup>2</sup>), sa fonction caractéristique *ϕ<sub>X </sub>*est
>
> *ϕ<sub>X</sub>*(*u*) = *e*<sup>i*uµ−*<u>1</u></sup>~~<sub>2</sub>~~*σ*<sup>2</sup>*u*<sup>2</sup>pour tout *u ∈* **R**.
>
> Rappelons que **E**\[*X*\] = *µ* et Var(*X*) = *σ*<sup>2</sup>.
>
> **Théorème 41** *La fonction caractéristique d’une variable aléatoire X qui*
>
> *suit la loi N* (*µ*, *σ*<sup>2</sup>) *est donnée par ϕ<sub>X</sub>*(*u*) = *e*<sup>i*uµ−*<u>1</u></sup>~~<sub>2</sub>~~*u*<sup>2</sup>*σ*<sup>2</sup>*pour tout u ∈* **R***.*
>
> *Preuve:* à faire via le Théorème de résidu de Cauchy. □
>
> **Théorème 42** *Soit X ∼ N* (*µ*, *σ*<sup>2</sup>) *alors X et µ* + *σY où Y ∼ N* (0, 1)
>
> *suivent la même loi.*
>
> *Preuve:* En effet, d’après le Théorème d’unicité, il suffit de prouver
>
> que *ϕ<sub>X</sub>*(*u*) = *ϕ<sub>µ</sub>*<sub>+*σY*</sub>(*u*) pour tout *u ∈* **R**. Or pour tout *u ∈* **R**, on
>
> a *ϕ<sub>µ</sub>*<sub>+*σY*</sub>(*u*) = **E**\[*e*<sup>i*u*(*µ*+*σY*)</sup>\] = *e*<sup>i*uµ*</sup>**E**\[*e*<sup>i*uσY*</sup>\] = *e*<sup>i*uµ*</sup>*e<sup>−</sup>*<sup><u>1</u></sup>~~<sub>2</sub>~~(*u*<sup>2</sup>*σ*<sup>2)</sup>, d’où la
>
> réponse. □
>
> **Définition 24** *On dit que deux v.a.r. X et Y de carré intégrable sont non*
>
> *corrélées si* Cov(*X*,*Y*) := **E**\[(*X −* **E**\[*X*\])(*Y −* **E**\[*Y*\])\] = 0*.*
>
> *9. Convergence des variables aléatoires, convergence en loi et applications avec fonctions caractéristiques*
>
> **Définition 25** *On dit qu’une suite* (*X<sub>n</sub>*)<sub>*n≥*1</sub> *de v.a.r. converge presque sûrement vers une v.a.r. X si l’ensemble N des ω tels que la suite numérique* (*X<sub>n</sub>*(*ω*))<sub>*n≥*1</sub> *ne converge pas vers X*(*ω*) *vérifie* **P**(*N*) = 0*. Rappelons qu’on dit que N est négligeable.*
>
> Noter qu’on a aussi *N<sup>c </sup>*= Λ = *{ω ∈* Ω : lim<sub>*n→*∞</sub>*X<sub>n</sub>*(*ω*) = *X*(*ω*)*}* vérifie **P**(Λ) = 1. On note la convergence presque sûre ainsi :
>
> lim<sub>*n→*∞</sub>*X<sub>n </sub>*= *X p*.*s*. ou *X<sub>n</sub> → X p*.*s*.
>
> Il apparaît que la convergence presque sûre est parfois forte dans certaines situations, et ce pourquoi nous introduisons deux autres mode de convergence.
>
> **Définition 26** *On dit qu’une suite* (*X<sub>n</sub>*)<sub>*n≥*1</sub> *de v.a.r. converge dans L<sup>p</sup>*(Ω)*, où p ∈* \[1, ∞\[*, vers une v.a.r. X si les X<sub>n</sub> sont dans L<sup>p</sup>*(Ω)*, et si on a*
>
> lim<sub>*n→*∞</sub>**E**\[*\|X<sub>n</sub> − X\|<sup>p</sup>*\] = 0.
>
> *On dit aussi que* (*X<sub>n</sub>*)*<sub>n</sub> converge en moyenne d’ordre p vers X, et on écrit X<sub>n</sub>L<sup>p</sup>*(Ω)
>
> *−−−→ X*
>
> Les cas les plus importants sont *p* = 1 (convergence "en moyenne") et *p* = 2 (convergence "en moyenne quadratique"). Quand *p* = 1, on a *\|***E**\[*X<sub>n</sub> − X*\]*\| ≤* **E**\[*\|X<sub>n</sub> − X\|*\] et *\|***E**\[*\|X<sub>n</sub>\|*\] *−* **E**\[*\|X\|*\]*\| ≤* **E**\[*\|X<sub>n</sub> − X\|*\] parce que *\|\|x\| − \|y\|\| ≤ \|x − y\|*. Donc *X<sub>n</sub>L*<sup>1</sup>(Ω)

*−−−→ X* implique **E**\[*X<sub>n</sub>*\] *→* **E**\[*X*\] et

> **E**\[*\|X<sub>n</sub>\|*\] *→* **E**\[*\|X\|*\].
>
> De même, quand *X<sub>n</sub>L<sup>p</sup>*(Ω)
>
> *−−−→ X* pour *p ∈*\]1, ∞\[, on peut montrer que
>
> **E**\[*\|X<sub>n</sub>\|<sup>p</sup>*\] *→* **E**\[*\|X\|<sup>p</sup>*\].
>
> 46
>
> **Définition 27** *On dit qu’une suite* (*X<sub>n</sub>*)<sub>*n≥*1</sub> *de v.a.r. converge en probabi lité vers une v.a.r. X si*
>
> *∀ ε \>* 0, lim<sub>*n→*∞</sub>**P**(*\|X<sub>n</sub> − X\| \> ε*) = 0,
>
> *ou plus simplement* **P**(*\|X<sub>n</sub> − X\| \> ε*) *→* 0 *quand n →* ∞*. On écrit alors X<sub>n</sub>***<sup>P</sup>***−→ X*
>
> Une autre manière d’écrire les choses est la suivante : *X<sub>n </sub>*converge en probabilité vers *X* lorsque,
>
> *∀ ε*, *δ \>* 0, *∃N<sub>ε</sub>*<sub>,*δ*</sub>, *n ≥ N ⇒* **P**(*\|X<sub>n</sub> − X\| \> ε*) *\< δ*.
>
> Avant d’établir les rapports entre les différents modes de convergence on va donner un critère simple de convergence en probabilité.

**Théorème 43** *On a X<sub>n</sub>***<sup>P</sup>***−→ X si et seulement si* lim<sub>*n→*∞**E**</sub>h*<sub>\|X<u>n</u></sub>−X\|* 1+*\|X<sub>n</sub>−X\|*

i

= 0*.*

> *Preuve:* On ne nuit pas à la généralité en supposant que *X* = 0, de sorte qu’il nous suffit de montrer que *X<sub>n</sub>***<sup>P</sup>***−→ X* équivaut à lim<sub>*n→*∞</sub>**E**\[*<sup>\|X</sup><sub><u>n</u></sub>\|*
>
> 1+*\|X<sub>n\|</sub>*\] = 0. Supposons d’abord que *X<sub>n</sub>***<sup>P</sup>***−→ X*. Pour tout *ε \>* 0, 1+*\|X<sub>n\|</sub> ≤<sup>\|X</sup><sub><u>n</u></sub>\|*

on a lim<sub>*n→*∞</sub>**P**(*\|X<sub>n</sub>\| \> ε*) = 0. Mais *<sup>\|X</sup><sub><u>n</u></sub>\|* **1***<sub>\|Xn\|\>ε</sub>* + *ε*, donc **E**\[*<sup>\|X</sup><sub><u>n</u></sub>\|*

1+*\|X<sub>n\|</sub>***1***<sub>\|Xn\|\>ε</sub>* + *ε***1***<sub>\|Xn\|≤ε</sub> ≤*

> 1+*\|X<sub>n\|</sub>*\] *≤* **P**(*\|X<sub>n</sub>\| \> ε*) + *ε*, en prenant les limites on

arrive à lim sup<sub>*n→*∞</sub> **E**

h*<sub>\|X<u>n</u></sub>\|* 1+*\|X<sub>n</sub>\|*

i

*≤ ε*; comme *ε* est arbitrairement petit

> il vient lim<sub>*n→*∞</sub>**E**\[*\|X<sub>n</sub>\|*/(1 + *\|X<sub>n</sub>\|*)\] = 0.
>
> Supposons à l’inverse que lim<sub>*n→*∞</sub>**E**\[*\|X<sub>n</sub>\|*/(1 + *\|X<sub>n</sub>\|*)\] = 0. La fonction
>
> *f*(*x*) = *x*/(1 + *x*) est strictement croissante, donc *f*(*ε*)**1***<sub>\|Xn\|\>ε</sub> ≤*
>
> *f*(*\|X<sub>n</sub>\|*)**1***<sub>\|Xn\|\>ε</sub> ≤ f*(*\|X<sub>n</sub>\|*). En prenant les espérances, puis les limites,
>
> on arrive à *f*(*ε*) lim<sub>*n→*∞</sub>**P**(*\|X<sub>n</sub>\| \> ε*) *≤* lim<sub>*n→*∞</sub>**E**\[ *f*(*\|X<sub>n</sub>\|*)\] = 0. Comme *ε \>* 0

est fixé, on conclut que lim<sub>*n→*∞</sub>**P**(*\|X<sub>n</sub>\| \> ε*) = 0. □ Ce théorème nous dit que *X<sub>n</sub>***<sup>P</sup>***−→ X* ssi

Le théorème suivant nous indique que la convergence en probabi lité est le mode convergence le plus faible introduit jusqu’à présent. **Théorème 44** *Soit* (*X<sub>n</sub>*)<sub>*n≥*1</sub> *une suite de v.a.r.*

*a) Si X<sub>n</sub>L<sup>p</sup>*(Ω)

*−−−→ X, alors on a X<sub>n</sub>***<sup>P</sup>***−→ X,*

*b) Si X<sub>n</sub> → X p.s., alors on a X<sub>n</sub>***<sup>P</sup>***−→ X.*

*Preuve:* Pour *a*) : **P**(*\|X<sub>n</sub> − X\| \> ε*) *≤* <sup><u>1</u></sup>*~~ε<sup>p </sup>~~***E**\[*\|X<sub>n</sub> − X\|<sup>p</sup>*\] *→* 0 quand *n →* ∞ (pour *ε \>* 0 fixé), d’où le résultat.

Pour *b*) : Posons *f*(*x*) = *\|x\|*/(1 + *\|x\|*), alors on a *f*(*X<sub>n</sub> − X*) *≤* 1, et donc lim<sub>*n→*∞</sub>**E**\[ *f*(*\|X<sub>n</sub> − X\|*)\] = **E**\[ lim<sub>*n→*∞</sub>*f*(*\|X<sub>n</sub> − X\|*)\] = **E**\[0\] = 0, grâce au

**E**\[ *f*(*\|X<sub>n</sub> − X\|*)\]) *→* 0 pour la fonction *f*(*x*) = *\|x\|*/(1 + *\|x\|*). Un examen soigneux de cette preuve montre que la même équivalence reste vraie pour tout fonction *f* sur \[0, ∞\[ qui est bornée, strictement croissante, continue, nulle en 0. Par exemple, *X<sub>n</sub>***<sup>P</sup>***−→ X* ssi **E**\[*\|X<sub>n</sub> − X\| ∧* 1\] *→* 0, et aussi ssi **E**\[arctan(*\|X<sub>n</sub> − X\|*)\] *→* 0.

47

> théorème de convergence dominée de Lebesgue. □ Attention les
>
> réciproques sont fausses en général.
>
> Par contre il existe des réciproques "partielles" :
>
> **Théorème 45** *Supposons que X<sub>n</sub>***<sup>P</sup>***−→ X. Il existe alors une sous-suite*
>
> (*n<sub>k</sub>*)<sub>*k∈***N**</sub>*∗ ∈* **N**<sup>*∗***N***∗*</sup>*telle que X<sub>nk</sub> → X p.s. lorsque k →* ∞*.*
>
> *Preuve: f*(*x*) := *\|x\|*/(1 + *\|x\|*), on a lim<sub>*n→*∞</sub>**E**\[ *f*(*X<sub>n</sub> − X*)\] = 0 par un
>
> théorème précédent et donc on peut trouver suite d’entiers *n<sub>k</sub>*telle
>
> que **E**\[ *f*(*X<sub>nk</sub> − X*)\] *\<* 1/2*<sup>k</sup>*. On a alors ∑<sup>∞</sup><sub>*k*=1</sub> **E**\[ *f*(*X<sub>nk</sub> − X*)\] *\<* ∞, donc
>
> ∑<sup>∞</sup><sub>*k*=1</sub>*f*(*X<sub>nk</sub> − X*) *\<* ∞ p.s. et donc lim<sub>*n→*∞</sub>*\|X<sub>nk</sub> − X\|* = 0 p.s. □
>
> **Théorème 46** *Supposons que X<sub>n</sub>***<sup>P</sup>***−→ X et que \|X<sub>n</sub>\| ≤ Y pour tout n, où*
>
> *Y ∈ L<sup>p</sup>*(Ω) *pour p ∈* \[1, ∞\[*. On a alors X ∈ L<sup>p</sup>*(Ω) *et X<sub>n</sub>L<sup>p</sup>*(Ω)

*−−−→ X*

> *Preuve: X<sub>n</sub> ∈ L<sup>p</sup>*et pour tout *ε \>* 0, **P**(*\|X\| \> Y* + *ε*) *≤* **P**(*\|X −*
>
> *X<sub>n</sub>\| \> ε*) et donc en passant à la limite on obtient **P**(*\|X\| \> Y* + *ε*) *≤*
>
> lim*<sub>n</sub>* . . . = 0, ceci étant vrai pour tout *ε \>* 0 on obtient **P**(*\|X\| \>*
>
> *Y*) *≤* lim<sub>*m→*∞</sub>**P**(*\|X\| \> Y* + <sup><u>1</u></sup>*~~<sub>m</sub>~~*) = 0, et donc *\|X\| ≤ Y* p.s. et donc
>
> *X ∈ L<sup>p</sup>*(Ω). Supposons maintenant que (*X<sub>n</sub>*)*<sub>n</sub>* ne converge pas vers *X*
>
> dans *L<sup>p</sup>*. Il existe alors une suite d’entier strictement croissante *n<sub>k </sub>*et
>
> un *ε \>* 0 tels que **E**\[*\|X<sub>nk</sub> − X\|<sup>p</sup>*\] *≥ ε* pour tout *k*. La sous-suite (*X<sub>nk</sub>*)*<sub>k</sub>*
>
> converge évidemment vers *X* en probabilité, donc elle admet (d’après
>
> le théorème précédent) une sous-sous-suite (*X<sub>nk j</sub>*)*<sub>j</sub>* qui converge p.s.
>
> vers *X*. Donc (*X<sub>nk j</sub> − X*)*<sub>j</sub>* converge p.s. vers 0, tout en restant majorées
>
> en valeurs absolue par 2*Y* : une application du théorème de Lebesgue
>
> donne alors que **E**\[*\|X<sub>nk j</sub> − X\|<sup>p</sup>*\] *→* 0, en contradiction avec le fait que
>
> **E**\[*\|X<sub>nk</sub> − X\|<sup>p</sup>*\] *≥ ε* pour tout *k*. □
>
> Le théorème suivant est facile, mais utile
>
> **Théorème 47** *Soit f une fonction continue.*
>
> *a) Si X<sub>n</sub> → X p.s., alors f*(*X<sub>n</sub>*) *→ f*(*X*) *p.s.*
>
> *b) Si X<sub>n</sub>***<sup>P</sup>***−→ X, alors f*(*X<sub>n</sub>*)**<sup>P</sup>***−→ f*(*X*)*.*
>
> *Preuve:* voir la page 153 de 1. □
>
> 48
>
> *<sup>0.2.3</sup> convergence en loi*
>
> **Définition 28** *Soit µ<sub>n</sub> et µ deux probabilités sur* (**R**, *B*(**R**))*. On dit que* (*µ<sub>n</sub>*)<sub>*n converge étroitement vers µ si* (</sub>R**<sub>R</sub>***f*(*x*) *dµ<sub>n</sub>*(*x*))*<sub>n</sub> converge vers*
>
> R
>
> **<sub>R</sub>***f*(*x*) *dµ*(*x*) *pour toute fonction f réelle continue et bornée.*
>
> **Définition 29** *Soit* (*X<sub>n</sub>*)*<sub>n</sub> et X des v.a.r. On dit que* (*X<sub>n</sub>*)*<sub>n</sub> converge en loi vers X si* (**P***<sub>Xn</sub>*)*<sub>n</sub> converge étroitement vers* **P***<sub>X</sub>, et on écrit X<sub>n</sub>Loi*

*−→ X.*

> Remarque : les *X<sub>n </sub>*et *X* ne sont pas forcément définies sur un même espace de probabilité, puisque seul leurs lois jouent le rôle dans la définition.
>
> **Théorème 48** *Soit* (*X<sub>n</sub>*)*<sub>n</sub> et X des v.a.r. On a X<sub>n</sub>Loi*

*−→ X ssi*

> lim<sub>*n→*∞</sub>**E**\[ *f*(*X<sub>n</sub>*)\] = **E**\[ *f*(*X*)\]
>
> *pour toute fonction réelle f continue et bornée sur* **R***.*
>
> *Preuve:* Il suffit de combiner les deux définitions précédentes et d’observer que **E**\[ *f*(*X<sub>n</sub>*<sub>)\] =</sub> R**<sub>R</sub>***f*(*x*) *d***P**<sub>*X*(*x*) et **E**\[ *f*(*X*)\] =</sub> R**<sub>R</sub>***f*(*x*) *d***P***<sub>X</sub>*(*x*). □
>
> Pour avoir la convergence p.s. ou dans *L<sup>p </sup>*ou en probabilité les v.a. *X<sub>n </sub>*et *X* doivent être définies sur le même espace de probabilité. Donc a priori la convergence en loi n’est pas comparable aux autres. On a cependant le résultat suivant :
>
> **Théorème 49** *Soient* (*X<sub>n</sub>*)*<sub>n</sub> et X des v.a.r. toutes définies sur le même espace de probabilité* (Ω, *A*, **P**)*. Si* (*X<sub>n</sub>*)*<sub>n</sub> converge vers X en probabilité, alors X<sub>n</sub> converge aussi vers X en loi.*
>
> *Preuve:* Soit *f* une fonction réelle bornée et continue sur **R**. Le théorème 47 implique que *f*(*X<sub>n</sub>*) converge vers *f*(*X*) en probabilité également. Comme *f* est bornée, cette convergence a aussi lieu dans *L*<sup>1</sup>(théorème 46). Donc lim<sub>*n→*∞</sub>**E**\[ *f*(*X<sub>n</sub>*)\] = **E**\[ *f*(*X*)\], et le théorème précédent donne le résultat. □
>
> **Théorème 50** *Soit* (*X<sub>n</sub>*)*<sub>n</sub> et X des v.a. définies sur le même espace de probabilité* (Ω, *A*, **P**)*. Si* (*X<sub>n</sub>*)*<sub>n</sub> converge en loi vers X et si de plus X est p.s. constante, alors* (*X<sub>n</sub>*)*<sub>n</sub> converge vers X en probabilité.*
>
> *Preuve:* Supposons que *X* = *a* p.s. La fonction *f*(*x*) = *\|x − a\|*/(1 + *\|x − a\|*) étant bornée et continue, on a lim<sub>*n→*∞</sub>**E**\[ *f*(*X<sub>n</sub> − a*)\] = 0, et donc

49

> *X<sub>n</sub>***<sup>P</sup>***−→ X* en vertu du théorème 43 □
>
> **Théorème 51** *Soient* (*X<sub>n</sub>*)*<sub>n</sub> et X des v.a.r.*
>
> *a) Si X<sub>n</sub>Loi*
>
> *−→ X alors* lim<sub>*n→*∞</sub>*F<sub>Xn</sub>*(*x*) = *F<sub>X</sub>*(*x*) *pour tout x appartenant à un*
>
> *sous-ensemble dense de* **R***, donné par D* = *{x ∈* **R**, *F<sub>X</sub>*(*x<sup>−</sup>*) = *F<sub>X</sub>*(*x*)*},*
>
> *i.e. F<sub>X</sub> est continue pour x ∈ D, qui est appelé l’ensemble des points de*
>
> *continuité de la fonction F<sub>X</sub>.*
>
> *b) Supposons que* lim<sub>*n→*∞</sub>*F<sub>Xn</sub>*(*x*) = *F<sub>X</sub>*(*x*) *pour tout x appartenant à un sous*
>
> *ensemble dense de* **R***. Alors X<sub>n</sub>Loi*
>
> *−→ X.*
>
> *Preuve:* Voir la page 159 de 1. Remarquez que *D ⊂* **R** est dense dans
>
> **R** puisque *D<sup>c</sup>*est dénombrable. □
>
> **Théorème 52 (Théorème de Continuité de P. Lévy)** *Soit* (*µ<sub>n</sub>*)<sub>*n≥*1</sub> *une*
>
> *suite de probabilités sur* (**R**, *B*(**R**))*, et* (*µ*ˆ*<sub>n</sub>*)*<sub>n</sub> la suite de leurs transformées*
>
> *de Fourier (ou fonction caractéristiques).*
>
> *a) Si* (*µ<sub>n</sub>*)*<sub>n</sub> converge étroitement vers une probabilité µ (ou X<sub>n</sub>Loi*

*−→ X, i.e.*

> (**P***<sub>Xn</sub>*)*<sub>n</sub> converge étroitement vers* **P***<sub>X</sub>) alors* (*µ*ˆ*<sub>n</sub>*)*<sub>n</sub> converge simplement*
>
> *vers la transformée de Fourier µ*ˆ *(ou ϕ<sub>Xn</sub> → ϕ<sub>X</sub>)*
>
> *b) Si* (*µ*ˆ*<sub>n</sub>*)*<sub>n</sub> converge simplement vers une fonction f , et si de plus cette*
>
> *fonction est continue au point* 0*, alors il existe une probabilité µ sur*
>
> (**R**, *B*(**R**)) *t.q. µ*ˆ = *f , et* (*µ<sub>n</sub>*)*<sub>n</sub> converge étroitement vers µ.*
>
> *Preuve:* voir le Théorème 19.1. qui se trouve à la page 173 de 1. □
>
> *10. Loi des grands nombres et le théorème limite central*
>
> *<sup>0.2.4</sup> La loi des grands nombres*
>
> **Théorème 53 (Loi forte des grands nombres)** *Soit* (*X<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite de v.a.r. i.i.d. de carré intégrables avec µ* := **E**\[*X*<sub>1</sub>\] *et σ*<sup>2</sup> = *σ*<sup>2</sup>*X*<sub>1</sub>*\<* ∞*. Soit S<sub>n </sub>*:= ∑*<sup>n</sup><sub>i</sub>*<sub>=1</sub> *X<sub>i</sub>. On a alors*
>
> lim<sub>*n→*∞</sub>*S<sup>n</sup><sub>n</sub>*= *µ p*.*s*. *et dans L*<sup>2</sup>(Ω).
>
> *Preuve:* Voir le Théorème 20.1. de la page 179 de 1. □ **Théorème 54 (Loi des grands nombres de Kolmogorov)** *Soit*
>
> (*X<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite de v.a.r. i.i.d. et soit µ ∈* **R***.*
>
> lim<sub>*n→*∞</sub>*S<sup>n</sup><sub>n</sub>*= *µ p*.*s*. *⇔* **E**\[*X*<sub>1</sub>\] = *µ*.
>
> *Dans ce cas, la convergence a aussi lieu dans L*<sup>1</sup>(Ω)*.*
>
> **Théorème 55 (Théorème-limite central-version 1)** *Soit* (*X<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite de v.a.r. i.i.d. avec* **E**\[*X*<sub>1</sub>\] = *µ et* Var(*X*<sub>1</sub>) = *σ*<sup>2</sup> *\>* 0*.*
>
> *<sub>σ</sub><u>√</u>~~<sub>n</sub>~~* *<sub>n</sub>converge en loi vers une v.a. X ∼ N* (0, 1)*.*
>
> *<sub>Alors</sub> <sub>S<u>n</u></sub>−nµ*
>
> *Preuve:* Voir Théorème 21.1. de la page 187 de 1. □ **Théorème 56 (Théorème-limite central-version 1)** *Soit* (*X<sub>n</sub>*)<sub>*n∈***N**</sub>*∗ une suite de v.a.r. indépendantes. Supposons que* **E**\[*X<sub>n</sub>*\] = 0 *pour tout n ∈* **N***<sup>∗</sup>. Supposons que* ∑*<sub>j</sub>* **E**\[*\|X<sub>j</sub>\|*<sup>2+*ε*</sup>\] *\<* ∞ *et* ∑<sup>∞</sup><sub>*n*=1</sub>*σ*<sup>2</sup>*<sub>n</sub>* = ∞ *pour un ε \>* 0*. Alors*

<u><sub>q</sub>*S<sub>n</sub> *</u>

∑*<sup>n</sup><sub>j</sub>*<sub>=1</sub>*σ*<sup>2</sup>*j*

*Loi*

*−−−→<sub>n→</sub>*<sub>∞</sub>*vers une v.a. X ∼ N* (0, 1)*.*

> —————————————————————————————-
>
> *Bibliographie*
>
> Jean Jacod and Philip Protter. *Probability Essentials*. Springer, Berlin, 2nd edition, 2003. ISBN 978-3-540-43188-4.
>
> Aurel Spataru. *Analysis of Probability*. Academic Press, Oxford, UK, 2013. ISBN 978-0-12-401665-4. URL https://www.amazon.fr/ Analysis-Probability-Aurel-Spataru/dp/0124016650.
>
> Z. Łomnicki and Stanisław Ulam. Sur la théorie de la mesure dans les espaces combinatoires et son application au calcul des probabilités. i. variables indépendantes. *Fundamenta Mathematicae*, 23(1) :237–278, 1934. ISSN 0016-2736. URL http://eudml.org/doc/212724.
