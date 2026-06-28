# FCStudio — Changelog

Toutes les évolutions importantes du projet sont documentées dans ce fichier.

Le format est inspiré de "Keep a Changelog", mais adapté à un projet de recherche et de reverse engineering.

---

# Versioning

Le projet utilise le format suivant :

MAJEUR.MINEUR.CORRECTIF

Exemples :

0.0.1-dev

0.0.2-dev

0.1.0

1.0.0

Les versions "-dev" correspondent aux versions de développement.

---

# Types de changements

Chaque entrée est classée dans l'une des catégories suivantes.

## Architecture

Évolution de l'organisation du projet.

## SDK

Ajout ou modification des composants internes.

## Outils

Ajout ou évolution des outils CLI.

## Reverse Engineering

Découvertes concernant les formats Frostbite.

## Documentation

Ajout ou amélioration de la documentation.

## Correction

Correction de bugs.

---

# Historique

## [0.0.1-dev]

### Architecture

- Création de la structure initiale du projet.

### SDK

- Création de BinaryFile.
- Mise en place de la lecture binaire.

### Outils

- Création de Inspector.
- Création de TOC Info.

### Reverse Engineering

- Première analyse des fichiers TOC.
- Identification du Magic Number des fichiers TOC.

---

## [0.0.2-dev]

### SDK

- Création de LayoutTOCReader.
- Création de CASReader minimal.

### Outils

- Ajout de CAS Info.
- Ajout du comparateur binaire.

### Reverse Engineering

- Découverte des chemins Win32 présents dans layout.toc.
- Première comparaison de plusieurs fichiers CAS.
- Mise en évidence de champs constants dans le header CAS.
- Identification d'une structure commune entre plusieurs fichiers CAS.

### Documentation

- Début de la documentation du format TOC.
- Début de la documentation du format CAS.

---

## [0.0.3-dev]

### Architecture

- Création de ROADMAP.md.
- Création de ARCHITECTURE.md.
- Création de CHANGELOG.md.

### Documentation

- Définition officielle de la philosophie du projet.
- Mise en place des Milestones.
- Mise en place des Sprints.
- Mise en place des règles d'architecture.

### Reverse Engineering

- Formalisation de la méthode scientifique du projet :

    Observation

    ↓

    Compréhension

    ↓

    Validation

    ↓

    Modification

---

# À venir

Les prochaines versions devraient contenir :

## [0.0.4-dev]

### SDK
- Ajout de HeaderAnalyzer.

### Outils
- `compare_binary.py` utilise désormais le SDK.

### Architecture
- La logique de comparaison binaire a été sortie des outils CLI.


## 0.0.5-dev

- String Analyzer
- Entropy Analyzer
- Pattern Scanner

### SDK
- Ajout de BinaryComparator dans le SDK.
- Ajout de EntropyAnalyzer.
- Ajout des modèles EntropyAnalysis et EntropyBlock.
- Ajout de PatternScanner.
- Ajout des modèles PatternAnalysis et PatternMatch.

### Outils

- Ajout de tools/strings.py.
- Ajout de tools/entropy.py.
- Ajout de tools/pattern.py.

### Reverse Engineering

- Confirmation que layout.toc contient de nombreux chemins Win32.
- Confirmation que le CAS commentarylaunch_tur_tr contient des chemins audio `sound/speech/...`.
- Observation que le petit CAS commentarylaunch_tur_tr contient une zone utile suivie d’un padding nul.
- Confirmation que le magic TOC `00 D1 CE 01` est présent au début de layout.toc.
- Confirmation de deux occurrences du motif ASCII `sound` dans le petit CAS commentarylaunch_tur_tr.

## 0.1.0

Premier SDK stable.