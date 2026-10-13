---
source: "PREING2-S2/Informatique4/CM13-JQuery_2024-2025_Informatique4_P2S2_MZneika.pdf"
pages: 23
transcription: manuelle
transcription_date: 2026-10-04
verification: lecture visuelle des vingt-trois pages ; exemples de code et tableau restitués ; coquilles originales signalées
---

# jQuery et AJAX

Mussab Zneika — CY Cergy Paris Université (page 1).

## jQuery (page 2)

jQuery est une bibliothèque JavaScript légère : « écrivez moins, faites plus ». Son objectif est de faciliter l’utilisation de JavaScript sur votre site web. Elle encapsule les tâches communes qui nécessitent de nombreuses lignes de JavaScript dans des méthodes que l’on peut appeler avec une seule ligne de code.

La bibliothèque contient les fonctionnalités suivantes : manipulation HTML/DOM, manipulation de CSS et méthodes d’événements HTML.

## Principe de jQuery (page 3)

1. Sélectionner une partie du document. `$()` prend en entrée une chaîne de caractères contenant un sélecteur et renvoie un objet jQuery, ensemble de nœuds du DOM (Document Object Model). 2. Agir dessus.

Exemples : `$("div")` renvoie un objet contenant tous les `div` du document ; `$("div").hide()` cache tous les `div`.

## Sélecteurs (page 4)

On peut sélectionner de manière similaire à CSS : par type de bloc avec `$("balise")`, par identifiant avec `$("#id")`, par classe avec `$(".class")`.

```javascript
// <div>Test</div>
$("div")
// <ul id="test">tt</ul>
$("#test")
// <ul class="test">tt</ul>
$(".test")
```

## Sélecteurs de hiérarchie (page 5)

On peut atteindre les fils (`>`), tous les descendants (espace), le frère suivant (`+`) ou les frères suivants (`~`).

```html
<ul>
  <li>item 1</li>
  <li>item 2</li>
  <li class="trois">item 3
    <ol><li>3.1</li></ol></li>
  <li>item 4
    <ol><li>4.1</li></ol></li>
  <li>item 5</li>
</ul>
```

```javascript
// cache 4 et 5
$('li.trois ~ li').hide();
// cache 4
$('li.trois + li').hide();
// cache les <ol>
$("ul ol").hide()
// ne cache rien
$("ul > ol").hide()
```

## Sélecteurs de formulaire (page 6)

```javascript
// sélectionner les cases à cocher
$("input:checkbox")
// sélectionner les boutons radio
$("input:radio")
// sélectionner les boutons
$(":button")
// sélectionner les champs texte
$(":text")
$("input:checked")
$("input:selected")
```

> Le dernier sélecteur est reproduit tel quel. `:selected` concerne les options d’une liste de sélection ; l’exemple suivant utilise bien `select option:selected`.

## Sélecteurs de formulaire — Exemple (page 7)

```html
<html lang="en">
<head>
  <meta charset="utf-8">
  <script src="jquery-3.3.1.min.js"></script>
</head>
<body>
<select name="valeur" onchange="select1()">
  <option value="1">1</option>
  <option value="2" selected="selected">2</option>
  <option value="3">3</option>
</select>
<script>
function select1() {
  alert($("select option:selected").val());
}
</script>
</body>
```

> La fermeture `</html>` n’apparaît pas dans cette diapositive.

## La fonction `each` (page 8)

Elle appelle une fonction pour chaque élément sélectionné. `$(this)` désigne l’élément courant et `i` son index.

```javascript
$("table tr").each(function(i) {
  $(this).addClass("odd");
});
```

> Cet exemple ajoute la classe `odd` à **toutes** les lignes sélectionnées ; il ne filtre pas selon leur parité.

## Modifier le contenu HTML (page 9)

- `.html('[contenu]')` remplace le contenu d’un élément en interprétant les balises comme des balises.

- `.text('[contenu]')` remplace le contenu en considérant tout comme du texte. Le cours décrit les caractères `<` et `>` comme remplacés par les entités XML `&gt;` et `&lt;`.

- `.append('[contenu]')` insère du contenu dans l’élément sélectionné, après les éléments existants.

- `.prepend('[contenu]')` insère du contenu dans l’élément sélectionné, avant les éléments existants.

> La correspondance des entités est `<` → `&lt;` et `>` → `&gt;`. La méthode `.text()` affecte du texte, sans analyser celui-ci comme du HTML.

## Insérer des éléments (page 10)

`append()` insère du contenu à la fin de la sélection : ajout d’une espace et de trois astérisques après le contenu de chaque titre `h2`.

```javascript
$('h2').append(' ***');
```

`prepend()` insère au début : trois astérisques et une espace avant le contenu de chaque titre `h2`.

```javascript
$('h2').prepend('*** ');
```

`before()` insère avant la sélection : une séparation horizontale avant le titre `h2`.

```javascript
$('h2').before('<hr>');
```

`after()` insère après la sélection : un saut de ligne après chaque balise `hr`.

```javascript
$('hr').after('<br>');
```

> Les apostrophes typographiques présentes dans les deux derniers exemples du PDF sont normalisées en apostrophes JavaScript.

## Gestion des attributs et des valeurs (page 11)

Les balises HTML portent des attributs comme `title`, `alt`, `width`, `height`. jQuery permet de les manipuler avec `.attr("name", "parametre")`.

```javascript
// met tous les attributs comme celui du premier bouton
$("button:gt(0)")
  .attr("disabled", $("button:eq(0)").attr("disabled"));
```

> Le guillemet fermant de `"disabled"` manque dans le PDF ; il est rétabli. Le commentaire original dit « tous les attributs », alors que seul `disabled` est visé.

`val()` permet d’obtenir la valeur des objets ; `val(valeur)` permet de la modifier.

## Gestionnaire d’événements (page 12)

Associer une fonction à un événement :

```javascript
$(sel).click(function() { /* … */ });
$(sel).on('click', function() { /* … */ });
```

La méthode `on()` permet de limiter l’écriture en associant des méthodes événementielles à plusieurs éléments. Les deux lignes :

```javascript
$('img.grand').mouseenter(traitement1);
$('img.grand').mousemove(traitement2);
```

peuvent être regroupées :

```javascript
$('img.grand').on({mouseenter: traitement1, mousemove: traitement2});
```

## AJAX et jQuery (page 13)

jQuery fournit plusieurs méthodes pour AJAX. Elles permettent de demander du texte, du HTML, du XML ou du JSON à un serveur distant avec HTTP GET et HTTP POST. Le cours souligne la possibilité d’écrire une fonctionnalité AJAX en une seule ligne de code.

## Méthode `load()` (page 14)

La méthode charge des données à partir d’un serveur et les place dans l’élément sélectionné.

```javascript
$(sélecteur).load(URL, données, callback);
```

- `URL` : URL à charger.

- `données` : paires clé/valeur à envoyer avec la demande.

- `callback` : fonction à exécuter une fois `load()` terminé.

Il est possible d’ajouter un sélecteur jQuery au paramètre URL.

## `load()` — Exemple (page 15)

```html
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function() {
  $("#b1").click(function() {
    $("#div1").load("file1.txt");
  });
});
</script>
</head>
<body>
  <div id="div1"><h2>jQuery et AJAX </h2></div>
  <button id="b1">Changer le contenu</button>
</body>
</html>
```

## `load()` avec sélection d’un fragment (page 16)

Contenu nommé « File1.txt » dans la source :

```html
<div id="div1"> div1 </div>
<div id="div2"> div2</div>
<div id="div3"> dive3</div>
```

Page HTML :

```html
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function() {
  $("#b1").click(function() {
    $("#div1").load("file1.txt #div2");
  });
});
</script>
</head>
<body>
  <div id="div1"><h2>jQuery et AJAX </h2></div>
  <button id="b1">Changer le contenu</button>
</body>
</html>
```

> Les noms « File1.txt » et `file1.txt` diffèrent par la casse dans la source.

## Méthode `ajax()` (page 17)

Syntaxe présentée : `$.ajax({nom: valeur, nom: valeur, ...})`.

| Nom | Description |
| --- | --- |
| `dataType` | Type de données attendu de la réponse du serveur. |
| `data` | Données à envoyer au serveur. |
| `success(result, status, xhr)` | Fonction exécutée lorsque la requête s’est terminée avec succès. |
| `error(xhr, status, error)` | Fonction exécutée en cas d’échec de la demande. |
| `type` | Type de demande : GET ou POST. |
| `Xhr` | Fonction utilisée pour créer l’objet XMLHttpRequest. |

> Le tableau original écrit `Xhr` ; le nom de l’option est `xhr`, en minuscules.

## `$.ajax()` — Exemple (page 18)

```html
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function() {
  $("#b1").click(function() {
    $.ajax({
      url: "file1.txt",
      success: function(results) {
        $("#div1").html(results);
      }
    });
  });
});
</script>
</head>
<body>
  <div id="div1"><h2>jQuery et AJAX </h2></div>
  <button id="b1">Changer le contenu</button>
</body>
</html>
```

## Méthode `$.get()` (page 19)

Elle demande des données au serveur avec une requête HTTP GET. Syntaxe : `$.get(URL, callback);`.

Exemple présenté :

```javascript
$.get("page1.php", function(données, état) {
  /* … */
});
```

> La majuscule de `Function` dans la diapositive est corrigée en `function` ; les points de suspension désignent du code à compléter.

## `$.get()` — Exemple (page 20)

```html
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function() {
  $("#b1").click(function() {
    $.get("page1.php", function(data, status) {
      $("#div1").html("Data: " + data + "\nStatus: " + status);
    });
  });
});
</script>
</head>
<body>
  <div id="div1"><h2>Ajax et JQuery ( Get Methode)</h2></div>
  <button id="b1">Changer le contenu</button>
</body>
</html>
```

« Page1.php » dans la source :

```php
<?php echo "Bonjour M/Mme "; ?>
```

> Le retour à la ligne de la diapositive séparait `\` de `nStatus` : l’échappement `\n` est réuni. Le libellé « Page1.php » et l’URL `page1.php` n’ont pas la même casse dans le PDF.

## Méthode `$.post()` (page 21)

Elle demande des données au serveur avec une requête HTTP POST. La ligne « Syntaxe » affiche `$.get(URL, Données, callback);`.

> Coquille : dans cette section, lire `$.post(URL, Données, callback);`.

Exemple :

```javascript
$.post("page1.asp", {
  nom: "Zneika",
  ville: "Pontoise"
}, function(données, état) {
  /* … */
});
```

> Comme page 19, la majuscule de `Function` est corrigée.

## `$.post()` — Exemple (page 22)

```html
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function() {
  $("#b1").click(function() {
    $.post("page1.php", {nom: "Zneika", ville: "Pontoise"},
      function(data, status) {
        alert("Data: " + data + "\nStatus: " + status);
      });
  });
});
</script>
</head>
<body>
  <div id="div1"><h2>Ajax et JQuery ( POST Methode)</h2></div>
  <button id="b1">Changer le contenu</button>
</body>
</html>
```

Code PHP associé :

```php
<?php
$var1 = $_POST["nom"];
$var2 = $_POST["ville"];
echo "Bonjour $var1 ville $var2";
?>
```

> Les retours à la ligne de mise en page à l’intérieur des URL et des chaînes JavaScript ont été réunis dans les exemples.

## Sources citées dans le support (page 23)

- Cours de Jean-Loup Guillaume : `http://jlguillaume.free.fr/www/documents/teaching/ntw1213/LI385_C5_Jquery.pdf`.

- Cours de programmation web avancée de Thierry Hamon : `https://perso.limsi.fr/hamon/PWA-20122013/Cours/JQuery.pdf`.

- « jQuery : écrivez moins pour faire plus ! » : `http://openclassrooms.com/courses/jquery-ecrivez-moins-pour-faire-plus`.

- « Premiers pas avec AJAX » : `https://openclassrooms.com/fr/courses/1631636-simplifiez-vos-developpements-javascript-avec-jquery/1636305-premiers-pas-avec-ajax`.

- « AJAX Introduction » : `https://www.w3schools.com/xml/ajax_intro.asp`.
