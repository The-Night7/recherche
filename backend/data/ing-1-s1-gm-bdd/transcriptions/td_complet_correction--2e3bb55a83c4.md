# td_complet_correction.html

[Ouvrir l’original](https://drive.google.com/open?id=1d3sivIHdkcHLOOpff8Cv4z8lHriPK_mT) · Texte structuré depuis le fichier original. Les mises en page complexes peuvent nécessiter une vérification.

<div class="container">

<div>

# 📘 TD 01 - Modèle Entités-Associations

ING1 - Bases de données - Correction Complète

CyTech - 2021-2022

</div>

<div class="content">

<div class="exercise">

## Exercice 1 : CyTech

<div class="section">

### Section 1 : Les simples entités

<div class="question">

#### Question 1 : Modélisation d'un Livre

**Énoncé :** Un livre de la bibliothèque de CyTech est renseigné par le titre, l'éditeur, l'année d'édition, le numéro ISBN (unique et normalisé) et un numéro de livre pour l'identifier dans la base.

<div class="answer">

##### ✅ Solution :

<div class="entity-box">

<div class="entity-name">

LIVRE

</div>

<div class="attribute">

<span class="primary-key">\#num_livre</span>

</div>

<div class="attribute">

titre

</div>

<div class="attribute">

editeur

</div>

<div class="attribute">

annee_edition

</div>

<div class="attribute">

ISBN

</div>

</div>

<div class="note">

**Note :** Le `num_livre` est choisi comme clé primaire car il identifie de manière unique chaque exemplaire dans la base. L'ISBN, bien qu'unique, identifie l'édition du livre et non chaque exemplaire physique.

</div>

</div>

</div>

<div class="question">

#### Question 2 : Modélisation d'un Professeur

**Énoncé :** Un professeur à CyTech est renseigné par son nom, prénom, e-mail CyTech, spécialité principale et adresse (rue, ville, code postal).

<div class="answer">

##### ✅ Solution :

<div class="entity-box">

<div class="entity-name">

PROFESSEUR

</div>

<div class="attribute">

<span class="primary-key">\#id_prof</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

prenom

</div>

<div class="attribute">

email

</div>

<div class="attribute">

specialite

</div>

<div class="attribute">

rue

</div>

<div class="attribute">

ville

</div>

<div class="attribute">

code_postal

</div>

</div>

<div class="note">

**Note :** On crée un `id_prof` comme identifiant artificiel plutôt que d'utiliser l'email, pour plus de flexibilité (changement d'email possible). L'adresse est décomposée en trois attributs distincts.

</div>

</div>

</div>

<div class="question">

#### Question 3 : Modélisation d'un Étudiant

**Énoncé :** Un étudiant à CyTech est renseigné par son nom, prénom, date de naissance, e-mail CyTech et adresse (rue, ville, code postal).

<div class="answer">

##### ✅ Solution :

<div class="entity-box">

<div class="entity-name">

ETUDIANT

</div>

<div class="attribute">

<span class="primary-key">\#id_etudiant</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

prenom

</div>

<div class="attribute">

date_naissance

</div>

<div class="attribute">

email

</div>

<div class="attribute">

rue

</div>

<div class="attribute">

ville

</div>

<div class="attribute">

code_postal

</div>

</div>

</div>

</div>

<div class="question">

#### Question 4 : Modélisation d'une Promotion

**Énoncé :** Une promotion (PréIng1, Ing1, ...) est renseignée par son libellé et son cycle.

<div class="answer">

##### ✅ Solution :

<div class="entity-box">

<div class="entity-name">

PROMOTION

</div>

<div class="attribute">

<span class="primary-key">\#libelle</span>

</div>

<div class="attribute">

cycle

</div>

</div>

<div class="note">

**Note :** Le `libelle` peut servir de clé primaire car il est unique (PréIng1, Ing1, Ing2, etc.). Le cycle pourrait être (Prépa, Ingénieur, etc.).

</div>

</div>

</div>

<div class="question">

#### Question 5 : Modélisation d'une Matière

**Énoncé :** Une matière est renseignée par son libellé, sa durée et son syllabus.

<div class="answer">

##### ✅ Solution :

<div class="entity-box">

<div class="entity-name">

MATIERE

</div>

<div class="attribute">

<span class="primary-key">\#id_matiere</span>

</div>

<div class="attribute">

libelle

</div>

<div class="attribute">

duree

</div>

<div class="attribute">

syllabus

</div>

</div>

</div>

</div>

</div>

<div class="section">

### Section 2 : Des associations simples

<div class="question">

#### Question 1 : Une matière est enseignée dans une promotion

<div class="answer">

##### ✅ Solution :

Association **EST_ENSEIGNEE_DANS** entre MATIERE et PROMOTION

Cardinalités : <span class="cardinality">(1,n)</span> côté MATIERE et <span class="cardinality">(1,n)</span> côté PROMOTION

<div class="note">

Une matière peut être enseignée dans plusieurs promotions (ex: Mathématiques en Ing1 et Ing2), et une promotion a plusieurs matières.

</div>

</div>

</div>

<div class="question">

#### Question 2 : Un professeur enseigne un certain nombre de matières

<div class="answer">

##### ✅ Solution :

Association **ENSEIGNE** entre PROFESSEUR et MATIERE

Cardinalités : <span class="cardinality">(1,n)</span> côté PROFESSEUR et <span class="cardinality">(1,n)</span> côté MATIERE

<div class="note">

Un professeur peut enseigner plusieurs matières, et une matière peut être enseignée par plusieurs professeurs.

</div>

</div>

</div>

<div class="question">

#### Question 3 : Un livre de la bibliothèque concerne un certain nombre de matières

<div class="answer">

##### ✅ Solution :

Association **CONCERNE** entre LIVRE et MATIERE

Cardinalités : <span class="cardinality">(1,n)</span> côté LIVRE et <span class="cardinality">(0,n)</span> côté MATIERE

<div class="note">

Un livre concerne au moins une matière (mais peut en concerner plusieurs), et une matière peut avoir 0 ou plusieurs livres associés.

</div>

</div>

</div>

<div class="question">

#### Question 4 : Un livre de la bibliothèque est associé à un ou plusieurs mots-clés

<div class="answer">

##### ✅ Solution :

Il faut créer une nouvelle entité **MOT_CLE** avec l'attribut `mot`

<div class="entity-box">

<div class="entity-name">

MOT_CLE

</div>

<div class="attribute">

<span class="primary-key">\#mot</span>

</div>

</div>

Association **EST_ASSOCIE_A** entre LIVRE et MOT_CLE

Cardinalités : <span class="cardinality">(1,n)</span> côté LIVRE et <span class="cardinality">(1,n)</span> côté MOT_CLE

</div>

</div>

</div>

<div class="section">

### Section 3 : Des associations un peu plus compliquées

<div class="question">

#### Question 1 : Une matière nécessite un certain nombre de pré-requis d'autres matières

<div class="answer">

##### ✅ Solution :

Association **PRE_REQUIS** réflexive sur l'entité MATIERE

Cardinalités : <span class="cardinality">(0,n)</span> pour "nécessite" et <span class="cardinality">(0,n)</span> pour "est pré-requis de"

<div class="note">

**Association réflexive :** MATIERE est reliée à elle-même. Par exemple, "Analyse 2" nécessite "Analyse 1" comme pré-requis.

</div>

</div>

</div>

<div class="question">

#### Question 2 : Pour une année scolaire, un étudiant est dans une promotion avec statut en fin d'année

<div class="answer">

##### ✅ Solution :

Association **EST_INSCRIT** entre ETUDIANT et PROMOTION

Attributs de l'association :

- `annee_scolaire` (ex: "2021-2022")
- `statut` (redoublant, admis, exclus, diplômé)

Cardinalités : <span class="cardinality">(1,n)</span> côté ETUDIANT et <span class="cardinality">(1,n)</span> côté PROMOTION

<div class="note">

**Important :** L'année scolaire et le statut sont des attributs de l'association car ils dépendent du couple (étudiant, promotion).

</div>

</div>

</div>

<div class="question">

#### Question 3 : Gestion des cycles avec ordre des promotions

<div class="answer">

##### ✅ Solution :

Créer une nouvelle entité **CYCLE** :

<div class="entity-box">

<div class="entity-name">

CYCLE

</div>

<div class="attribute">

<span class="primary-key">\#nom_cycle</span>

</div>

<div class="attribute">

description

</div>

</div>

Modifier l'entité **PROMOTION** :

<div class="entity-box">

<div class="entity-name">

PROMOTION

</div>

<div class="attribute">

<span class="primary-key">\#libelle</span>

</div>

<div class="attribute">

ordre

</div>

</div>

Association **APPARTIENT_A** entre PROMOTION et CYCLE

Cardinalités : <span class="cardinality">(1,1)</span> côté PROMOTION et <span class="cardinality">(1,n)</span> côté CYCLE

<div class="note">

L'attribut `ordre` dans PROMOTION permet de spécifier la séquence (1 pour PréIng1, 2 pour PréIng2, etc.).

</div>

</div>

</div>

<div class="question">

#### Question 4 : Évaluation des étudiants avec pondération

<div class="answer">

##### ✅ Solution :

Plusieurs associations sont nécessaires :

1.  **Association EST_ENSEIGNEE_DANS** entre MATIERE et PROMOTION
    - Attribut : `annee_scolaire`
    - Attribut : `ponderation`
2.  **Association EST_EVALUE** ternaire entre ETUDIANT, MATIERE et PROMOTION
    - Attribut : `note`
    - Attribut : `annee_scolaire`

<div class="note">

**Explication :** La pondération dépend de la matière, de la promotion et de l'année scolaire. La note dépend de l'étudiant, de la matière, de la promotion et de l'année scolaire.

</div>

</div>

</div>

</div>

<div class="diagram-container">

<div class="diagram-title">

🎨 Schéma Entité-Association Complet - Exercice 1 (Simplifié)

</div>

![Schéma 1](../supports/608f3fd503d978437b95f33e5b3e5ad6fe83d9de152c1487361523fb2428cd56/diagramme-1.svg)

</div>

</div>

<div class="exercise">

## Exercice 2 : Pokémon Go, partie 1

<div class="section">

### Énoncé

Construire une base de données pour gérer les jeux vidéo en ligne. Pour chaque jeu, on connait son nom, son genre et sa date de sortie, ainsi que les plateformes sur lesquels on peut jouer (iOS, Android). Un jeu peut être écrit par un seul ou plusieurs développeurs, et géré par une société. Il peut être téléchargé sur plusieurs sites tels que 01net, topito, etc. Le nombre de téléchargements est utilisé pour mesurer la popularité du jeu. Nous collectons les données des joueurs comme leur adresse mail, leur date de naissance et leur niveau.

</div>

<div class="section">

### Analyse et Solution

<div class="answer">

##### 🔍 Entités identifiées :

<div class="entity-box">

<div class="entity-name">

JEU

</div>

<div class="attribute">

<span class="primary-key">\#id_jeu</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

genre

</div>

<div class="attribute">

date_sortie

</div>

</div>

<div class="entity-box">

<div class="entity-name">

DEVELOPPEUR

</div>

<div class="attribute">

<span class="primary-key">\#id_dev</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

prenom

</div>

</div>

<div class="entity-box">

<div class="entity-name">

SOCIETE

</div>

<div class="attribute">

<span class="primary-key">\#id_societe</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

adresse

</div>

</div>

<div class="entity-box">

<div class="entity-name">

SITE

</div>

<div class="attribute">

<span class="primary-key">\#id_site</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

url

</div>

</div>

<div class="entity-box">

<div class="entity-name">

JOUEUR

</div>

<div class="attribute">

<span class="primary-key">\#email</span>

</div>

<div class="attribute">

date_naissance

</div>

<div class="attribute">

niveau

</div>

</div>

<div class="entity-box">

<div class="entity-name">

PLATEFORME

</div>

<div class="attribute">

<span class="primary-key">\#id_plateforme</span>

</div>

<div class="attribute">

nom

</div>

</div>

##### 🔗 Associations :

1.  **DEVELOPPE** (DEVELOPPEUR, JEU)  
    Cardinalités : <span class="cardinality">(1,n) - (1,n)</span>
2.  **GERE** (SOCIETE, JEU)  
    Cardinalités : <span class="cardinality">(1,n) - (1,1)</span>
    <div class="note">

    Un jeu est géré par une seule société, mais une société peut gérer plusieurs jeux.

    </div>
3.  **DISPONIBLE_SUR** (JEU, SITE)  
    Attribut : `nb_telechargements`  
    Cardinalités : <span class="cardinality">(1,n) - (1,n)</span>
4.  **JOUE** (JOUEUR, JEU)  
    Cardinalités : <span class="cardinality">(0,n) - (0,n)</span>
5.  **COMPATIBLE** (JEU, PLATEFORME)  
    Cardinalités : <span class="cardinality">(1,n) - (1,n)</span>

</div>

</div>

<div class="diagram-container">

<div class="diagram-title">

🎨 Schéma Entité-Association Complet - Exercice 2

</div>

![Schéma 2](../supports/608f3fd503d978437b95f33e5b3e5ad6fe83d9de152c1487361523fb2428cd56/diagramme-2.svg)

</div>

</div>

<div class="exercise">

## Exercice 3 : Gestion d'un hôpital

<div class="section">

### Énoncé et contraintes

- L'hôpital a des employés qui sont des docteurs et des infirmières
- Chaque employé a : numéro d'employé, nom, prénom, adresse, téléphone
- L'hôpital est composé de plusieurs services (code, nom, bâtiment, directeur)
- Le directeur d'un service est un docteur
- Chaque service contient plusieurs salles (numéro local, surveillant, nombre de lits)
- Le surveillant d'une salle est un infirmier
- Un infirmier est affecté à un seul service
- Les docteurs ne sont pas affectés à un service particulier, mais ont une spécialité
- On connaît la rotation pour chaque infirmier
- Les patients ont un nom et une adresse
- Le suivi médical de chaque patient est dans un dossier sous la responsabilité d'un unique médecin
- Le dossier contient la liste des maladies du patient avec leur date de début
- Une même maladie peut toucher le même patient à deux dates différentes

</div>

<div class="section">

### Solution

<div class="answer">

##### 🔍 Entités identifiées :

<div class="entity-box">

<div class="entity-name">

EMPLOYE

</div>

<div class="attribute">

<span class="primary-key">\#num_employe</span>

</div>

<div class="attribute">

nom, prenom

</div>

<div class="attribute">

adresse

</div>

<div class="attribute">

telephone

</div>

</div>

<div class="entity-box">

<div class="entity-name">

DOCTEUR

</div>

<div class="attribute">

<span class="primary-key">\#num_employe</span>

</div>

<div class="attribute">

specialite

</div>

</div>

<div class="entity-box">

<div class="entity-name">

INFIRMIER

</div>

<div class="attribute">

<span class="primary-key">\#num_employe</span>

</div>

<div class="attribute">

rotation

</div>

</div>

<div class="entity-box">

<div class="entity-name">

SERVICE

</div>

<div class="attribute">

<span class="primary-key">\#code_service</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

batiment

</div>

</div>

<div class="entity-box">

<div class="entity-name">

SALLE

</div>

<div class="attribute">

<span class="primary-key">\#code_service, \#num_salle</span>

</div>

<div class="attribute">

nb_lits

</div>

</div>

<div class="entity-box">

<div class="entity-name">

PATIENT

</div>

<div class="attribute">

<span class="primary-key">\#id_patient</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

adresse

</div>

</div>

<div class="entity-box">

<div class="entity-name">

DOSSIER

</div>

<div class="attribute">

<span class="primary-key">\#id_dossier</span>

</div>

<div class="attribute">

date_creation

</div>

</div>

<div class="entity-box">

<div class="entity-name">

MALADIE

</div>

<div class="attribute">

<span class="primary-key">\#code_maladie</span>

</div>

<div class="attribute">

nom

</div>

<div class="attribute">

description

</div>

</div>

##### 🔗 Associations :

1.  **Héritage :** DOCTEUR et INFIRMIER héritent de EMPLOYE
2.  **DIRIGE** (DOCTEUR, SERVICE)  
    Cardinalités : <span class="cardinality">(0,n) - (1,1)</span>
    <div class="note">

    Un docteur peut diriger 0 ou plusieurs services (dans le temps), un service a un seul directeur.

    </div>
3.  **AFFECTE_A** (INFIRMIER, SERVICE)  
    Cardinalités : <span class="cardinality">(1,1) - (1,n)</span>
    <div class="note">

    Un infirmier est affecté à un seul service, un service a plusieurs infirmiers.

    </div>
4.  **SURVEILLE** (INFIRMIER, SALLE)  
    Cardinalités : <span class="cardinality">(0,n) - (1,1)</span>
    <div class="note">

    Un infirmier peut surveiller plusieurs salles (dans le temps), une salle a un seul surveillant.

    </div>
5.  **CONTIENT** (SERVICE, SALLE)  
    Cardinalités : <span class="cardinality">(1,n) - (1,1)</span>
    <div class="note">

    Un service contient plusieurs salles, une salle appartient à un seul service.

    </div>
6.  **POSSEDE** (PATIENT, DOSSIER)  
    Cardinalités : <span class="cardinality">(1,1) - (1,1)</span>
7.  **RESPONSABLE_DE** (DOCTEUR, DOSSIER)  
    Cardinalités : <span class="cardinality">(1,n) - (1,1)</span>
    <div class="note">

    Un docteur est responsable de plusieurs dossiers, un dossier a un seul médecin responsable.

    </div>
8.  **SOUFFRE_DE** (DOSSIER, MALADIE)  
    Attribut : `date_debut`  
    Cardinalités : <span class="cardinality">(0,n) - (0,n)</span>
    <div class="note">

    Un dossier peut avoir plusieurs maladies, une maladie peut être dans plusieurs dossiers. La date de début permet de gérer les récidives.

    </div>

<div class="note">

**Points importants :**

- SALLE a une clé primaire composite (code_service, num_salle) car le numéro de salle est local au service
- L'héritage entre EMPLOYE, DOCTEUR et INFIRMIER permet de factoriser les attributs communs
- L'attribut `date_debut` dans SOUFFRE_DE permet de gérer le fait qu'un patient peut avoir la même maladie à différentes dates

</div>

</div>

</div>

<div class="diagram-container">

<div class="diagram-title">

🎨 Schéma Entité-Association Complet - Exercice 3

</div>

![Schéma 3](../supports/608f3fd503d978437b95f33e5b3e5ad6fe83d9de152c1487361523fb2428cd56/diagramme-3.svg)

</div>

</div>

<div class="legend">

#### 📖 Légende Générale

<div class="legend-item">

**Rectangle bleu** : Entité

</div>

<div class="legend-item">

**Losange orange** : Association

</div>

<div class="legend-item">

**Texte souligné (#)** : Clé primaire (identifiant unique)

</div>

<div class="legend-item">

**Texte italique** : Attribut d'association

</div>

<div class="legend-item">

**(min, max)** : Cardinalités - indique le nombre minimum et maximum de participations

</div>

<div class="legend-item">

**Ligne pointillée** : Relation d'héritage

</div>

<div class="legend-item">

**Association réflexive** : Association d'une entité avec elle-même

</div>

</div>

<div class="section">

### 💡 Notes Pédagogiques

<div class="note">

**Choix des clés primaires :**

- Privilégier les identifiants artificiels (id_xxx) pour plus de flexibilité
- Utiliser des clés naturelles quand elles sont stables et significatives (ISBN, email)
- Attention aux clés composites pour les entités faibles (comme SALLE)

</div>

<div class="note">

**Cardinalités courantes :**

- <span class="cardinality">(1,1)</span> : Participation obligatoire et unique
- <span class="cardinality">(0,1)</span> : Participation optionnelle et unique
- <span class="cardinality">(1,n)</span> : Participation obligatoire et multiple
- <span class="cardinality">(0,n)</span> : Participation optionnelle et multiple

</div>

<div class="note">

**Attributs d'association :**

Placez un attribut dans une association quand il dépend du couple d'entités et non d'une seule entité. Exemples : note (étudiant, matière), date_debut (patient, maladie), nb_telechargements (jeu, site).

</div>

</div>

</div>

</div>
