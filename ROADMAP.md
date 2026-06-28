# FCStudio Roadmap - Project Dashboard

> **Observer. Comprendre. Vérifier. Modifier.**

---

# Mission

FCStudio est un laboratoire d'ingénierie dédié à l'analyse des formats binaires du moteur Frostbite utilisés par les jeux EA SPORTS FC.

L'objectif du projet n'est pas uniquement de modifier le jeu, mais de comprendre son fonctionnement afin de développer des outils fiables, documentés et reproductibles.

---

# Philosophie

Chaque évolution du projet respecte le cycle suivant :

Observation
↓
Compréhension
↓
Validation
↓
Modification

Aucune modification n'est réalisée sans compréhension préalable du format concerné.

---

# État du projet

Version actuelle : **0.0.x-dev**

Phase actuelle :

🟢 Milestone 0 — Fondations

---

# Milestones

## Milestone 0 — Fondations

### Infrastructure

| ID | Tâche | État |
|----|-------|------|
| INF-001 | ROADMAP.md | 🟢 INF-001 terminé |
| INF-002 | ARCHITECTURE.md | 🟢 INF-002 terminé |
| INF-003 | CHANGELOG.md | 🟢 INF-003 terminé |
| INF-004 | CONTRIBUTING.md | 🟢 INF-004 terminé |
| INF-005 | Structure documentaire | 🟢 INF-005 terminé |

### Documentation

| ID | Tâche | État |
|----|-------|------|
| DOC-001 | Glossaire Frostbite | ⚪ |
| DOC-002 | Journal de recherche | ⚪ |
| DOC-003 | Journal des sessions | ⚪ |
| DOC-004 | Registre des décisions | ⚪ |
| DOC-005 | Registre des hypothèses | ⚪ |

### SDK

| ID | Classe | État |
|----|--------|------|
| SDK-001 | BinaryFile | ✅ |
| SDK-002 | HeaderAnalyser | 🟢 SDK-002 première version validée|
| SDK-003 | BinaryComparator | 🟢 SDK-003 terminé |
| SDK-004 | StringAnalyzer | 🟢 SDK-004 terminé |
| SDK-005 | EntropyAnalyzer | 🟢 SDK-005 terminé |
| SDK-006 | ResearchLab | ⚪ SDK-006 | |

### Outils

| ID | Outil | État |
|----|--------|------|
| TOOL-001 | Inspector | ✅ |
| TOOL-002 | TOC Info | ✅ |
| TOOL-003 | CAS Info | ✅ |
| TOOL-004 | Compare Binary | 🟡 |
| TOOL-005 | Header Probe | ⚪  |
| TOOL-006 | Pattern Scanner | 🟢 TOOL-006 terminé  |
| TOOL-007 | Structure Probe | ⚪ |

---

## Milestone 1 — Compréhension des formats Frostbite

### Formats

- [ ] TOC
- [ ] CAS
- [ ] CAT
- [ ] SuperBundle
- [ ] EBX
- [ ] RES
- [ ] CHUNK

Objectif :

Comprendre complètement chaque format avant toute modification.

---

## Milestone 2 — Extraction

Objectif :

Construire les outils permettant d'extraire les ressources du jeu.

Prévision :

- Audio
- Textures
- Meshes
- Animations
- Vidéos
- Localisation

---

## Milestone 3 — Compréhension du gameplay

Objectif :

Identifier les ressources contenant :

- Joueurs
- Clubs
- Championnats
- IA
- Carrière
- Match
- Interface

---

## Milestone 4 — Édition

Objectif :

Modifier les ressources.

Prévision :

- Éditeur EBX
- Éditeur RES
- Repack CAS
- Validation
- Création de mods

---

## Milestone 5 — FCStudio GUI

Objectif :

Développer une interface graphique complète.

Prévision :

- Explorateur Frostbite
- Analyseur graphique
- Comparateur visuel
- Éditeur
- Gestionnaire de projets

---

# Indicateurs de maturité

| Domaine | Progression |
|----------|-------------|
| Architecture | ██░░░░░░░░ 20 % |
| Documentation | █░░░░░░░░░ 10 % |
| SDK | ██░░░░░░░░ 20 % |
| Outils | ███░░░░░░░ 30 % |
| TOC | █░░░░░░░░░ 10 % |
| CAS | █░░░░░░░░░ 10 % |
| CAT | ░░░░░░░░░░ 0 % |
| EBX | ░░░░░░░░░░ 0 % |
| Extraction | ░░░░░░░░░░ 0 % |
| Édition | ░░░░░░░░░░ 0 % |
| Interface graphique | ░░░░░░░░░░ 0 % |

---

# Sprint en cours

## Sprint 0 — Le Laboratoire

### Objectif

Construire les outils génériques permettant d'observer les formats binaires.

### Backlog

| ID | Tâche | État |
|----|-------|------|
| INF-001 | ROADMAP | 🟡 |
| INF-002 | ARCHITECTURE | ⚪ |
| INF-005 | Arborescence documentaire | ⚪ |
| DOC-002 | Journal de recherche | ⚪ |
| SDK-002 | HeaderProbe | ⚪ |

---

# Vision à long terme

FCStudio doit devenir une plateforme d'analyse Frostbite permettant :

- d'observer les formats binaires ;
- de comprendre leurs structures ;
- d'explorer les dépendances entre ressources ;
- d'extraire les données du jeu ;
- de modifier les ressources de manière contrôlée ;
- de reconstruire un projet complet.

Le modding est une conséquence de cette compréhension, jamais un objectif isolé.