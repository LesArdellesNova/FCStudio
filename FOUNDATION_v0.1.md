# FOUNDATION v0.1

## FCStudio Foundation Document

**Version :** 0.1
**Statut :** Active
**Dernière mise à jour :** 28/06/2026

---

# 1. Vision

FCStudio est un projet de recherche et de développement consacré à la compréhension des formats de données du moteur **EA Frostbite**.

Le projet ne vise pas uniquement à lire des fichiers binaires. Son ambition est de construire progressivement une plateforme complète permettant :

* d'analyser les formats Frostbite ;
* de documenter les découvertes ;
* de produire un SDK Python réutilisable ;
* de développer des outils d'analyse en ligne de commande ;
* de constituer une base documentaire technique ouverte ;
* de préparer une future interface graphique.

FCStudio est conçu comme un laboratoire de reverse engineering reproductible.

---

# 2. Philosophie du projet

Les principes suivants guident toutes les décisions techniques.

## Documentation avant optimisation

Chaque découverte doit être documentée avant d'être optimisée.

La compréhension du format est prioritaire sur les performances.

---

## Une responsabilité par composant

Chaque module du SDK possède une responsabilité unique.

Exemples :

* HeaderAnalyzer
* BinaryComparator
* PatternScanner
* StringAnalyzer
* EntropyAnalyzer

Cette approche facilite les tests, la maintenance et la réutilisation.

---

## Les faits sont séparés des hypothèses

Le reverse engineering repose sur des observations.

Une différence importante est faite entre :

* un fait confirmé ;
* une hypothèse ;
* une expérimentation.

Aucune hypothèse n'est présentée comme une certitude.

---

## Les analyses doivent être reproductibles

Toute observation doit pouvoir être reproduite.

Chaque outil du SDK est conçu pour produire les mêmes résultats à partir des mêmes fichiers.

---

## GitHub devient la référence du projet

Le dépôt GitHub constitue désormais la source officielle du projet.

Il centralise :

* le code ;
* la documentation ;
* les issues ;
* les milestones ;
* le wiki ;
* le journal de recherche.

---

# 3. État actuel du projet

## Infrastructure

✅ Dépôt GitHub public

✅ Architecture SDK

✅ Documentation technique

✅ Wiki GitHub

✅ GitHub Project

✅ Labels

✅ Milestones

✅ Journal de recherche

---

# 4. SDK actuel

Les composants suivants sont disponibles.

| Composant         | État | Description                               |
| ----------------- | ---- | ----------------------------------------- |
| Header Analyzer   | ✅    | Analyse des headers binaires              |
| Binary Comparator | ✅    | Comparaison binaire détaillée             |
| String Analyzer   | ✅    | Extraction et filtrage des chaînes ASCII  |
| Entropy Analyzer  | ✅    | Calcul de l'entropie globale et par blocs |
| Pattern Scanner   | ✅    | Recherche de signatures binaires          |
| CAS Info          | 🚧   | Analyse préliminaire                      |
| TOC Info          | 🚧   | Analyse préliminaire                      |
| Inspector         | 🚧   | Point d'entrée générique                  |

---

# 5. Architecture actuelle

Le projet est organisé autour des dossiers suivants.

```text
sdk/
    analysis/
    frostbite/
    models/

tools/

docs/

.github/
```

Le SDK contient la logique métier.

Les outils CLI utilisent uniquement le SDK.

---

# 6. Premières découvertes Frostbite

Les observations suivantes sont désormais établies.

## layout.toc

Le fichier contient de nombreuses chaînes ASCII.

Exemple :

```
Win32/commentaryfull_fre_fr
Win32/commentarylaunch_eng_us
Win32/commentarylaunch_tur_tr
```

Ces informations montrent que le fichier référence les différents bundles disponibles.

---

## commentarylaunch

Les fichiers `commentarylaunch_*` possèdent :

* une faible entropie ;
* plusieurs chemins ASCII lisibles ;
* des références directes vers :

```
sound/speech/loccommentary
```

Ils semblent jouer le rôle de fichiers d'index ou de démarrage.

---

## commentaryfull

Les fichiers `commentaryfull_*` présentent :

* une entropie proche de 8 ;
* très peu de texte lisible ;
* des tailles importantes.

Ils semblent contenir les données principales de la ressource.

---

## Headers CAS

Les premières comparaisons montrent :

* plusieurs champs constants ;
* plusieurs champs variables suivant la langue ;
* des structures similaires entre fichiers.

Les offsets suivants présentent déjà un intérêt particulier :

```
0x00
0x08
0x0C
0x10
0x18
```

---

# 7. Documentation

La documentation est désormais organisée autour de plusieurs niveaux.

```
README.md

ROADMAP.md

ARCHITECTURE.md

CHANGELOG.md

PROJECT_STATE.md

FOUNDATION_v0.1.md

docs/
```

Chaque document possède une responsabilité précise.

---

# 8. Organisation GitHub

GitHub devient l'outil central du projet.

Il contient :

* Repository
* Wiki
* Issues
* Labels
* Milestones
* Project
* Documentation

À terme, l'ensemble de la gestion du projet devra être piloté depuis GitHub.

---

# 9. Objectifs immédiats

## Foundation

Finaliser l'infrastructure :

* nettoyage du dépôt ;
* normalisation Git ;
* automatisation GitHub.

---

## Research Lab

Développer le premier moteur de recherche Frostbite.

Objectifs :

* enregistrer les observations ;
* construire des hypothèses ;
* accumuler les preuves ;
* produire automatiquement des rapports de recherche.

---

## TOC Reader

Comprendre entièrement le format `layout.toc`.

---

## CAS Reader

Comprendre entièrement le format CAS.

---

## CAT Reader

Comprendre entièrement le format CAT.

---

## EBX Reader

Comprendre entièrement le format EBX.

---

# 10. Ambition

FCStudio n'est pas simplement un outil d'inspection binaire.

L'objectif est de construire progressivement une plateforme complète de reverse engineering Frostbite reposant sur :

* un SDK Python moderne ;
* une documentation technique exhaustive ;
* des outils d'analyse spécialisés ;
* un laboratoire de recherche reproductible ;
* une base de connaissances ouverte.

Le projet est conçu pour évoluer pendant plusieurs années tout en conservant une architecture simple, documentée et maintenable.
