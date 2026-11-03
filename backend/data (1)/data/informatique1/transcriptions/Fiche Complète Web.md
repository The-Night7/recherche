---
source: PREING1-S1/Informatique1/Fiche Complète Web.docx
transcription: manuelle
format_source: docx
verification: lecture intégrale du texte et des tableaux Word
---

# 🎓 MASTER FICHE : HTML / CSS / FORMULAIRES

Cette fiche regroupe l'intégralité des notions des TP10, TP11 et TP20 pour le QCM.

## 🟢 PARTIE 1 : HTML (Structure & Contenu)

### 1. Structure de base (Le squelette)

Une page valide commence toujours ainsi :

```html
<!DOCTYPE html>  <!-- Déclare HTML5 -->
<html lang="fr">
  <head>
    <meta charset="utf-8"> <!-- Gère les accents -->
    <title>Titre de l'onglet</title>
    <link rel="stylesheet" href="style.css"> <!-- Lien CSS -->
  </head>
  <body>
    <!-- Tout ce qui est visible à l'écran -->
  </body>
</html>
```

### 2. Block vs Inline (⚠️ CRUCIAL EN QCM)

Il faut savoir par cœur quel élément fait quoi.

| Type | Comportement | Balises (Exemples) |
| --- | --- | --- |
| BLOCK | Prend toute la largeur, va à la ligne avant et après. Accepte width et height. | `<div>`, `<p>`, `<h1>` à `<h6>`, `<ul>`, `<li>`, `<form>`, `<table>`, `<header>`, `<footer>`, `<section>` |
| INLINE | Ne prend que la place du texte. Reste sur la même ligne. Ignore width et height (sauf exception). | `<span>`, `<a>`, `<strong>`, `<em>`, `<label>`, `<img>`, `<input>` |

*Note : img et input sont techniquement des éléments remplacés (inline-block implicite) qui acceptent des dimensions.

### 3. Les Listes

À puces (Non-ordonnée) : `<ul>` avec des `<li>`.

Numérotée (Ordonnée) : `<ol>` avec des `<li>`.

### 4. Les Tableaux (`<table>`)

`<tr>` : Ligne.

`<th>` : En-tête (gras, centré).

`<td>` : Cellule de donnée.

Fusions :

colspan="2" : Fusionne 2 colonnes (horizontal).

rowspan="2" : Fusionne 2 lignes (vertical).

## 🔵 PARTIE 2 : LES FORMULAIRES

Balise conteneur : `<form action="serveur.php" method="POST">`

### 1. Attributs de `<form>`

action="..." : L'adresse du fichier qui reçoit les données.

method="GET" : Données dans l'URL (rapide, peu sécurisé, limité en taille).

method="POST" : Données cachées (sécurisé, illimité, pour mots de passe/fichiers).

enctype="multipart/form-data" : OBLIGATOIRE si le formulaire contient un upload de fichier (`<input type="file">`).

### 2. Les principaux `<input>`

La plupart sont des balises orphelines (pas de fermeture).

type="text" : Texte simple.

type="password" : Ronds noirs.

type="email" : Valide le format a@b.c.

type="radio" : Choix unique. Astuce : Ils doivent avoir le même name pour s'exclure mutuellement.

type="checkbox" : Choix multiples.

type="file" : Envoi de fichier.

type="hidden" : Champ invisible pour l'utilisateur mais envoyé au serveur.

type="submit" : Le bouton d'envoi.

### 3. Autres balises de formulaire

`<textarea>` : Zone de texte multiligne.

Piège : Pas d'attribut value. Le texte par défaut se met entre `<textarea>`Texte ici`</textarea>`.

`<select>` et `<option>` : Liste déroulante.

`<option value="paris" selected>`Paris`</option>` (selected définit le choix par défaut).

`<label for="uid">` : Étiquette liée à un input via son id="uid".

## 🟣 PARTIE 3 : CSS (Styles & Mise en page)

### 1. La "Spécificité" (Le calcul des points) 🏆

Si plusieurs règles s'appliquent, qui gagne ? C'est un calcul mathématique.

!important (Le joker, gagne tout).

Style Inline (`<p style="...">`) : 1000 pts.

ID (#monId) : 100 pts.

Classe / Pseudo-classe / Attribut (.maClasse, :hover, [type="text"]) : 10 pts.

Balise (div, p) : 1 pt.

L'héritage (ex: body { color: red }) a une valeur de 0, il perd contre tout sélecteur direct.

Exemple : #menu a { ... } (100 + 1 = 101 pts) GAGNE contre .menu a { ... } (10 + 1 = 11 pts).

### 2. Sélecteurs Avancés (Vus en TP)

div p (Descendant) : Tous les p dedans, peu importe la profondeur.

div > p (Enfant direct) : Juste les p qui sont fils directs.

h1 + p (Frère adjacent) : Le p collé juste après le h1.

input[type="text"] (Attribut) : Cible selon un attribut précis.

:nth-child(n) : Le n-ième enfant.

tr:nth-child(even) : Lignes paires.

tr:nth-child(odd) : Lignes impaires.

### 3. Le Modèle de Boîte (Box Model)

Ordre depuis le centre :

Content (Largeur/Hauteur du contenu).

Padding (Marge interne - transparent ou couleur du fond).

Border (Bordure).

Margin (Marge externe - espace entre les boîtes).

Important : box-sizing: border-box inclut le padding et la bordure dans la taille totale (width). C'est plus facile à gérer.

### 4. Positionnement (position)

static : Normal (défaut). top/left ne marchent pas.

relative : Décalé par rapport à sa place normale. Laisse un trou vide.

absolute : Sort du flux (flotte). Se place par rapport au parent positionné le plus proche (souvent un parent en relative).

fixed : Collé à l'écran (ne bouge pas au scroll).

### 5. Cacher un élément (Les 3 méthodes)

| Propriété | Visible ? | Place conservée ? |
| --- | --- | --- |
| display: none | Non | Non (supprimé du flux) |
| visibility: hidden | Non | Oui (fantôme) |
| opacity: 0 | Non | Oui (et reste cliquable !) |

## ⚠️ PIÈGES CLASSIQUES (Checklist pré-exam)

Syntaxe CSS : propriété: valeur; (pas de =, pas de text-color).

Unités : px (fixe), % (relatif parent), rem (relatif racine), vw (largeur fenêtre).

Balises orphelines : `<br>`, `<hr>`, `<img>`, `<input>`, `<link>`, `<meta>` n'ont pas de balise fermante `</...>`.

Couleurs : #FF0000 (Hexa), rgb(255,0,0), red (Nom), rgba(...) (avec transparence).

Liens : Pour ouvrir dans un nouvel onglet : `<a href="..." target="_blank">`.

IDs uniques : Un id ne doit apparaître qu'une seule fois par page. Une class peut être partout.

## Rectifications des raccourcis de la fiche

Les formulations du document sont conservées ci-dessus. Les précisions suivantes corrigent les points susceptibles d’induire en erreur :

- **GET et POST :** POST place les données dans le corps de la requête, sans les rendre secrètes. Le chiffrement du transport vient de HTTPS. POST n’a pas une taille « illimitée » : des limites peuvent être imposées par le serveur et les intermédiaires.
- **Spécificité CSS :** les nombres 1000/100/10/1 sont un aide-mémoire, pas une addition décimale générale. On compare séparément les composantes de spécificité ; dix classes ne remplacent pas un identifiant. L’origine, l’importance et les couches de cascade interviennent avant cette comparaison. `!important` ne « gagne » donc pas absolument tout.
- **Éléments remplacés :** une image en ligne peut accepter des dimensions sans que son `display` soit implicitement `inline-block`. Les contrôles de formulaire ont leurs propres comportements selon leur type.
- **Positionnement :** « parent positionné le plus proche » et « collé à l’écran » décrivent les cas usuels ; certains contextes, notamment les transformations, modifient le bloc conteneur des éléments positionnés.
