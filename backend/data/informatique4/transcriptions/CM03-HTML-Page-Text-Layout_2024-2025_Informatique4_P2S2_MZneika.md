---
source: "PREING2-S2/Informatique4/CM03-HTML-Page-Text-Layout_2024-2025_Informatique4_P2S2_MZneika.pdf"
pages: 33
transcription: assistée puis relue
transcription_date: 2026-10-04
verification: texte natif confronté visuellement aux trente-trois pages ; exemples en images et tableau des entités retranscrits ; schémas et captures décrits
---

# Programmation Web — Mise en page et mise en forme du texte

> Transcription du support dans son contexte d’origine : les exemples historiques et les formulations du cours sont conservés. Les guillemets typographiques du code sont normalisés et les mots coupés par la mise en page sont réunis. Les autres corrections et différences entre code et captures sont signalées. Logos et éléments décoratifs ne sont pas reproduits.

## Présentation (page 1)

Programmation Web — Page & Text Layout.

Mention latérale : « Course descriptions : semester 1, Data Science and Big Data. »

## Plan (page 2)

- Mise en page (Page layout)

- Mise en forme de texte (Text layout)

- Nouvelles balises en HTML5

## Rappels — Balises (page 3)

- HTML repose sur la notion de Balises (tags).

- les Balises permettent de structurer le contenu d’un document
HTML

- Les balises HTML peuvent être de deux types :

- balises qui sont ouvertes puis fermées, et encadrent du contenu
Example: `<b>` gras texte `</b>`

- balises qui s’ouvrent et se ferment en même temps
Example: `<br />` , `<hr />`, `<meta>`, `<img>`

```html
<h1> Exemple </h1>
 <hr />
 <p>
 <b>gras</b> puis <em>italique</em>, puis <b><em>gras
 et italique</em></b>.
 </p>
```

## Rappels — Attributs et imbrication (page 4)

Les balises HTML peuvent avoir des attributs qui les configurent ou ajustent leur comportement. Les attributs sont déclarés au sein de la balise ouvrante de l’élément :

```html
<p align="right">C'est aligné à droite </p>
```

En HTML, les noms de balise et d’attribut ne sont pas sensibles à la casse, mais la plupart des valeurs d’attribut le sont. Exemples du support :

```html
<B> Valid Text.</B>
<b> valid Text.</b>
```

Il est important de fermer les balises dans l’ordre :

```html
<b><em>gras et italique</em></b>
```

## Squelette d’un document HTML (page 5)

La page HTML contient deux parties principales :

En-tête :

- la tête contient les informations concernant du titre,
du codage, des mots-clés, etc.

- Ces Information sont destinée aux machines
(navigateur, robots, etc.)

Corps(Body) :

- le corps contient le contenu de la page web qui
sera affiché au client

- Information destinée à l’humain et aux machines

**Schéma de structure :**

```text
doctype
html
├── head
│   ├── title
│   └── meta
└── body
```

## Tête — Head (page 6)

- C'est là que nous mettrons des informations sur la page elle-même
(appelées métadonnées).

- Remarque: Il est important que vos balises `<head>` soient toujours le
premier ensemble de balises après `<html>`.

- Il est très fortement conseillé de toujours spécifier:

- Le tittre

- l’auteur,

- la description,

- les mots-clés.

```html
<head>
  <title>Our First Page</title>
  <meta name="keywords" content="beginning html,learning, CSIT-107" />
  <meta name="description" content="A beginning web page for CSIT-107 SUNY Fredonia" />
  <meta name="author" content="Your Name Here" />
</head>
```

> Le titre est défini par `title`. Les guillemets typographiques du code sont normalisés en guillemets droits.

## Corps — Body (page 7)

- Tout le contenu que nous souhaitons avoir à l'écran doit être
englobé par un ensemble de balises corporelles.

```html
<body bgcolor="blue" text="white" link="black">
<a href="page2.html">Hello in Web progrming Class!</a>
<p> Teacher: DR Mussab Zneika </p>
 </body>
```

## Attributs universels (page 8)

Les attributs universels peuvent être ajoutés sur tous les éléments. Le support cite les suivants :

| Attribut | Description |
| --- | --- |
| `class` | Un ou plusieurs noms de classe, en référence à une feuille de style CSS. |
| `id` | Identifiant unique au sein du document. |
| `style` | Style CSS en ligne pour l’élément. |
| `lang` | Langue du contenu de l’élément. |
| `title` | Représentation textuelle de l’information à laquelle il est lié. |
| `dir` | Direction du texte : `ltr` (Left To Right), `rtl` (Right To Left), `auto` (l’agent utilisateur décide). |
| `contenteditable` | Indique si le contenu est modifiable ou non. |

## Attributs universels — Exemple 1 (page 9)

Dans cet exemple, les attributs `class` et `style` modifient le style d’éléments HTML au moyen de CSS. Le CSS sera étudié plus tard.

```html
<head>
  <style>
    .bluetext {color: blue;}
    .greentext {color: green;}
  </style>
</head>
<body>
  <b class="bluetext">bold Text1 1</b><br />
  <i class="greentext">italaic Text 2</i><br />
  <p style="font-size: 40px;">This is paragraph 3</p>
  <p style="color:pink; border-style: dotted; font-size: 30px;">This is a new paragraph 4</p>
</body>
</html>
```

**Capture du résultat :** première ligne bleue et grasse ; deuxième verte et italique ; grand texte noir pour le paragraphe 3 ; texte rose bordé de pointillés pour le paragraphe 4.

> L’ouverture `html` manque dans l’extrait original. La capture affiche « This is a new paragraph 3 », tandis que le code affiche « This is paragraph 3 » ; cette différence vient du support.

## Attributs universels — Exemple 2 (page 10)

```html
<html>
<body>
  <p dir="rtl">Write this text right-to-left!</p>
  <p dir="ltr">Write this text left-to-right!</p>
  <p contenteditable="true">This is an editable paragraph.</p>
</body>
</html>
```

L’attribut `dir` définit le sens du texte : le premier paragraphe de droite à gauche et le second de gauche à droite. La capture montre le premier paragraphe aligné à droite et son point d’exclamation à gauche ; les deux autres paragraphes commencent à gauche.

## Div / Span (page 11)

- Alors que `<p>` nous aide à diviser notre texte, nous avons également
besoin d'un mécanisme pour séparer différents éléments de contenu
comme nous le faisions lorsque nous utilisions l'en-tête et le pied de
page
Cela nous permettra de définir plus qu'un simple haut, milieu et bas de notre
page. Pour ce faire, nous pouvons envelopper ces sections dans des balises
`<div>`.

- Div signifie diviser - il définit une section de contenu qui doit être
traitée séparément des autres contenus. Span est très similaire à div,
sauf qu'il doit identifier le contenu en ligne, c'est-à-dire le matériel qui
se trouve dans un bloc de texte.
En fin de compte, un div placera un saut de ligne avant et après ses balises,
contrairement à un span. En dehors de cela, ces balises sont fonctionnellement
équivalentes
Span sert surtout à associer un style à une partie d'un texte tandis que div sert à
agencer le contenu de la page

- Bien que ces balises semblent très simples maintenant, elles sont
très utiles lors de la création de mises en page complexes et sont les
balises que nous utiliserons le plus souvent

## Div / Span — Exemple 1 (page 12)

```html
<body>
         <header>
                   <h1>This is our first page! </h1>
         </header>
         <div id="left">
                   some menu items
         </div>
         <div id="content">
                   Hello World
         </div>
         <div id="right">
                   and some content on the right
         </div>
         </body>
```

- L'attribut align est désormais obsolète et ne doit plus être appliqué pour un `<div>`

- Vous remarquerez que la mise en page ne va pas à gauche ou à droite lorsque nous
étiquetons nos divs (tout s'organisera de haut en bas)
C'est parce que nous devons ajouter CSS pour le plein effet. Nous reprendrons
cet exemple plus tard pour ajouter le CSS nécessaire à la création de la mise en
page souhaitée :

**Capture :** les textes « some menu items », « Hello World » et « and some content on the right » apparaissent sur trois lignes successives, sans disposition en colonnes.

> Guillemets normalisés et barre oblique isolée devant `</body>` supprimée ; le PDF imprime `/</body>`.

## Div / Span — Exemple 2 (page 13)

Dans cet exemple, trois classes CSS (`righttext`, `lefttext`, `centertext`) définissent l’alignement du texte de trois éléments `div` : gauche, centre, droite.

```html
<html>
<head>
  <style>
    .lefttext {text-align: left;}
    .righttext {text-align: right;}
    .centertext {text-align: center;}
  </style>
</head>
<body>
  <h1>This is our first page!</h1>
  <div id="left" class="lefttext">some menu items</div>
  <div id="content" class="centertext">Hello World</div>
  <div id="right" class="righttext">and some content on the right</div>
</body>
</html>
```

**Capture :** après le titre, les trois textes apparaissent respectivement à gauche, au centre et à droite, chacun à un niveau vertical différent. Les guillemets des identifiants sont normalisés.

## Paragraphes (page 14)

- Pour développer un peu notre structure de base, nous pouvons diviser une
longue section de texte en paragraphes.
Nous pouvons le faire en ajoutant des pauses (`<br/>`) dans notre code.

- Si nous allons le faire plusieurs fois, et si nous voulons styliser nos
paragraphes sur toute la ligne, nous devrions plutôt envelopper chacun
d'eux dans un ensemble de balises de paragraphe, `<p></p>`.
L'utilisation des balises de paragraphe nous permet d'ajouter automatiquement un
espacement autour de notre contenu pour le séparer du reste de la page.

**Avant :**

```html
<body>
This is some text. It is really long. We want to
break this into paragraphs so it looks more like a document.
This is some text. It is really long. We want to break this
into paragraphs so it looks more like a document. This is some
text. It is really long. This is some text. It is really
long. We want to break this into paragraphs so it looks more
like a document. This is some text. It is really long. We want
to break this into paragraphs so it looks more like a
document. This is some text. This is some text. It is really
long. We want to break this into paragraphs so it looks more
like a document. This is some text. It is really long. We want
to break this into paragraphs so it looks more like a
document.
</body>
```

**Après :**

```html
<body>
<p>
This is some text. It is really
long. We want to break this into paragraphs so it looks more
like a document. This is some text. It is really long. We want
to break this into paragraphs so it looks more like a
document. This is some text. It is really long.
</p>
<p>
This is some text. It is really
long. We want to break this into paragraphs so it looks more
like a document. This is some text. It is really long. We want
to break this into paragraphs so it looks more like a
document. This is some text.
</p>
<p>
This is some text. It is really
long. We want to break this into paragraphs so it looks more
like a document. This is some text. It is really long. We want
to break this into paragraphs so it looks more like a
document.
</p>
</body>
```

## Paragraphes — Exemple (page 15)

```html
<div>
<p align="center">Pour développer un peu notre structure de base,
nous pouvons diviser une longue section de texte en paragraphes .</p>

<p align="left">Si nous allons le faire plusieurs fois, et si nous
voulons styliser nos paragraphes sur toute la ligne, nous devrions
plutôt envelopper chacun d'eux dans un ensemble de balises de
paragraphe. </p>
 </div>
```

**Capture :** le premier paragraphe est centré ; le second est aligné à gauche.

> Les attributs `align` sont ceux des exemples historiques du support.

## Éléments de titres HTML (page 16)

- Les titres HTML sont des titres ou des sous-titres que vous souhaitez
afficher sur une page Web :

- `<H1>`...`</H1>` Un titre de premier niveau.

- `<H2>`...`</H2>` Un titre de deuxième niveau.

- `<H3>`...`</H3>` Un titre de troisième niveau .

- `<H4>`...`</H4>` Un titre de quatrième niveau.

- `<H5>`...`</H5>` Un titre de cinquième niveau.

- `<H6>`...`</H6>` Un titre de sixième niveau.

- Toutes les balises de titre acceptent l'attribut suivant :
`ALIGN="..."` Les valeurs possibles sont : Center, left, and right.

> L’attribut `align` présenté ici appartient aux anciennes pratiques de mise en forme HTML.

## Éléments de titres — Exemple (page 17)

```html
<body>
 <H1>A first-level heading.</H1>
 <H2>A second-level heading.</H2>
 <H3>A third-level heading.</H3>
 <H4>A fourth-level heading.</H4>
 <H5>A fifth-level heading.</H5>
 <H6>A sixth-level heading</H6>
 </body>
```

**Capture :** six titres de taille décroissante, de « A first-level heading. » à « A sixth-level heading ».

> La première ligne est corrigée : le support imprime `</body>` avant les titres, au lieu de `<body>`.

## Listes ordonnées et non ordonnées (page 18)

- Nous utilisons les balises `<ol>` (listes ordonnées) ou `<ul>`
(listes non ordonnées)

- Les listes ordonnées, en revanche, concernent les articles qui
doivent être commandés pour une raison, comme des
instructions qui doivent être suivies dans le bon ordre

- Les listes ordonnées et non ordonnées sont respectivement
des listes d'éléments alphanumériques et non ordonnées

- En les utilisant, nous pouvons créer des listes pour les afficher
à l'écran car nous sommes habitués à voir une liste
d'éléments

- L’affichage des listes peut être considérablement personnalisé
par les feuilles de style CSS

- Lorsque, nous avons placé des balises `<li>` imbriquées dans
chacune pour représenter chaque élément de la liste.

## Listes — Exemple 1 (page 19)

```html
<ol>
  <li>First</li>
  <li>Second</li>
  <li>Third</li>
  </ol>

  <ul>
  <li>An item</li>
  <li>Another item</li>
  <li>Yet another item</li>
  </ul>
```

**Capture :** « First », « Second », « Third » sont numérotés 1, 2, 3 ; « An item », « Another item », « Yet another item » sont précédés de puces.

## Listes imbriquées — Exemple 2 (page 20)

```html
<body>
  <h2>A Nested List</h2>
  <p>Lists can be nested (list inside
  list):</p>
  <ul>
    <li>Drink
    <ul>
         <li>Black tea</li>
         <li>Green tea</li>
         <li>Milk </li>
       </ul>
    </li>
    <li>Food
       <ul>
         <li>Chicken</li>
         <li>Meat</li>
       </ul>
    </li>
    <li>Sweetmeats</li>
  </ul>
```

**Capture :** sous « A Nested List », la liste principale contient Drink, Food et Sweetmeats. Drink contient Black tea, Green tea, Milk ; Food contient Chicken, Meat. Les sous-listes ont des puces creuses.

> Le signe diacritique isolé devant « Sweetmeats » est omis du code ; la fermeture `body` n’apparaît pas dans l’extrait source.

## Listes de définitions (page 21)

- Un ensemble de balises associé peut être utilisé lorsque vous
souhaitez répertorier des définitions

- Ce sont

```html
<dl> pour la liste elle-même, avec <dt> imbriqué à
       l'intérieur pour les termes et <dd> également imbriqué, pour la
       définition, à la suite de son <dt> correspondant



<dl>
<dt>Coffee</dt>
 <dd>Bean-based caffeinated beverage </dd>
<dt>Tea</dt>
 <dd>Leaf-based caffeinated beverage</dd>
<dt>Water</dt>
 <dd>Standard H20</dd>
</dl>
```

**Capture :** chaque définition est décalée vers la droite sous son terme. Le texte « Standard H20 » contient le chiffre zéro, comme dans la source.

## Entités (page 22)

Dans les exemples d’en-tête et de pied de page, le symbole de droit d’auteur est inséré avec `&copy;`. Le support présente les entités avec un nom ou un numéro.

Il donne `&nbsp;` comme exemple d’espace insécable permettant d’insérer des espaces supplémentaires. Les noms d’entités sont sensibles à la casse.

| Résultat | Description de la source | Nom | Numéro |
| --- | --- | --- | --- |
| Espace insécable | non-breaking space | `&nbsp;` | `&#160;` |
| `<` | less than | `&lt;` | `&#60;` |
| `>` | greater than | `&gt;` | `&#62;` |
| `&` | ampersand | `&amp;` | `&#38;` |
| © | copyright | `&copy;` | `&#169;` |
| ® | registered trademark | `&reg;` | `&#174;` |
| ™ | trademark | `&trade;` | `&#8482;` |

> La notation abrégée de la source, « &[numéro d’entité ici] », omet le `#` et le point-virgule : une référence numérique décimale s’écrit `&#numéro;`. Un espace insécable n’est pas un espace ordinaire, contrairement à la formulation « ou juste un espace standard » du support.

## Structuration du document HTML5 (page 23)

- Entête : `<header>` `</header>`

- Menu de navigation : `<nav>` `</nav>`

- Section : `<section>` `</section>`

- Article : `<article>` `</article>`

- Encadré : `<aside>` `</aside>`

- Pied de page : `<footer>` `</footer>`

- Boîte de dialogue : `<dialog>` `</dialog>`

**Schéma :** `header` et `nav` occupent chacun toute la largeur en haut ; une colonne gauche contient `section` au-dessus d’`article`, à côté d’une colonne `aside` ; `footer` occupe toute la largeur en bas. La boîte `dialog` figure dans la liste mais pas dans le dessin.

## Adresse (page 24)

La balise d'adresse nous permet de spécifier le texte qui appartient à une adresse ou des informations de contact pour le créateur de contenu, ce qui permet aux applications de trouver plus facilement les informations nécessaires pour des outils tels que la cartographie et la génération de références.

```html
<address>
  Article by <a href="mailto:professor@school.edu">Prof. Essor</a>.<br>
  Fredonia, NY<br>
  USA
</address>
```

**Capture :** « Article by Prof. Essor. », avec un lien sur le nom, puis « Fredonia, NY » et « USA » sur les lignes suivantes.

## Article (page 25)

- Les balises d'article sont destinées à être utilisées sur du
contenu qui peut être réutilisé en dehors de son site d'origine.

- Il est destiné aux articles de presse, aux articles de blog et à
d'autres types de contenu qui seraient republiés à plusieurs
endroits.

```html
<article>
  <h1>Our Blog Post</h1>
  <p>This is our great content that is now identified as something that can exist on its own as a piece of work.</p>
</article>
```

## De côté — Aside (page 26)

- Le côté est destiné à être utilisé lorsque vous souhaitez
marquer un élément de contenu lié au matériel dans lequel il
est imbriqué.

- Il a été créé principalement pour définir des informations
connexes, comme une partie d'un article ou d'un blog.

```html
<p>
This is some text. It is really long. We want to break this into paragraphs so it looks more like a document. This is some text. It is really long. We want to break this into paragraphs so it looks more like a document. This is some text. It is really long. We want to break this into paragraphs so it looks more like a document. This is some text. It is really long. We want to break this into paragraphs so it looks more like a document.
</p>
<aside>
  <h4>Side Bar</h4>
  <p>This is something related to our content that is not actually a part of it</p>
</aside>
```

## Citer (page 27)

- Alors que cite a été inclus dans les versions précédentes de
HTML, la spécification HTML5 actuelle prévoit qu'il soit utilisé
pour définir le titre d'un ouvrage qui est inclus dans le document.

- Les versions précédentes limitaient cette balise aux citations
appropriées de publications écrites.

```html
<img src="scream.jpg">
<p><cite>The Scream</cite> E. Munchapter 1893.</p>
```

**Capture :** reproduction du tableau *Le Cri*, accompagnée de « The Scream E. Munch. 1893. », avec le titre en italique.

> Le `>` manquant après l’attribut `src` est rétabli ; « Munchapter » est conservé dans le code comme imprimé, tandis que la capture porte « Munch. ».

## Figure et Figcaption (page 28)

- La balise figure nous permet d'étiqueter une image, un portrait
ou tout autre art visuel inclus dans une balise d'image pour
identifier le contenu en tant que tel.

Figcaption

- Figcaption, comme caption, nous permet d'ajouter une légende à
notre image comme nous le ferions pour un tableau.

```html
<figure><img src="ourimage.jpg"/></figure>

<figure>
  <img src="ourimage.jpg"/>
  <figcaption>Figure 1</figcaption>
</figure>
```

## Mètre — Meter (page 29)

- La balise meter nous permet de générer une image visuelle
basée sur les valeurs fournies

- Ceci est destiné aux valeurs déjà connues ou chargées à l'écran
comme un tableau ou un graphique

- Il existe également une balise Progress pour surveiller les
actions de fichier en cours, comme un téléchargement

```html
<meter value="3" min="0" max="15">One Fifth</meter>
<br>
<meter value="0.65">65%</meter>
```

**Capture :** deux jauges vertes, remplies respectivement à un cinquième et à 65 %.

## Nav (page 30)

- Si nous avons un groupe de liens que nous voulons au même
endroit (c'est-à-dire un menu ou une liste de références), nous
pouvons les inclure dans les balises de navigation afin que les
navigateurs les reconnaissent comme un groupe de liens

- Ceci est particulièrement utile pour les logiciels de lecture
d'écran, car les balises indiquent à quoi servent les liens

```html
<nav>
  <a href="/">Home</a> |
  <a href="/css/">CSS</a> |
  <a href="/js/">JavaScript</a> |
  <a href="/js/jquery/">jQuery</a>
</nav>
```

## Progress (page 31)

- La balise de progression a été créée pour aider à afficher l'état
d'un téléchargement ou d'un téléchargement. Il prend deux
attributs, y compris le montant actuel (que nous modifierions à
l'aide de JavaScript) et la valeur totale ou la plus élevée de ce
que nous surveillons. Si nous montrons le pourcentage d'un
téléchargement, nous pourrions utiliser :

```html
<progress value="46" max="100"></progress>
```

- Ou, si nous voulons afficher le montant réel déplacé, ou si nous
déplaçons un certain nombre d'éléments, nous pouvons utiliser
le nombre terminé et le nombre total au lieu d'un pourcentage, et
l'image le calculera pour nous :

```html
<progress value="345" max="850"></progress>
```

**Captures :** deux barres vertes partiellement remplies, correspondant à 46/100 et 345/850.

## Time (page 32)

- L'étiquette de temps est flexible dans la mesure où elle peut spécifier
une valeur au format 24 heures, une date de calendrier grégorien
complète ou à la fois une date et une heure

- L'utilisation de cette balise en elle-même ne changera aucun style
visuel sur la page, mais permet aux applications sur nos appareils de
trouver les informations afin de prendre en charge des fonctionnalités
telles que la création d'entrées de calendrier ou de rappels basés sur
les informations

```html
<p>The daily meeting will be at <time>10:00</time> every morning.</p>
<p>The next monthly meeting will be on <time datetime="2013-08-01">August first</time>.</p>
```

## Sources d’informations (page 33)

- `https://www.w3schools.com/html/default.asp`

- `https://developer.mozilla.org/fr/docs/Web/HTML`

- MENDEZ, Michael. *The Missing Link: An Introduction to Web Development and Programming*. 2014, chapitres 9 et 10.
