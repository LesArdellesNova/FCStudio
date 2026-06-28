# FCStudio — Architecture

> Objectif : garder FCStudio lisible, testable et extensible sur la durée.

---

# 1. Principe général

FCStudio est organisé en couches.

Chaque couche a une responsabilité précise et ne doit pas empiéter sur celle des autres.

```text
Interface future / GUI
        ↓
Outils CLI
        ↓
SDK
        ↓
Couche binaire
        ↓
Fichiers du jeu
```

---

# 2. Règle fondamentale

Le flux de dépendance est toujours descendant.

```text
tools → sdk → binary
```

Jamais l’inverse.

Le SDK ne doit jamais dépendre des outils CLI.

---

# 3. Couches du projet

## 3.1 Couche binaire

Dossier :

```text
sdk/binary.py
```

Responsabilité :

- lire les fichiers ;
- lire des octets ;
- lire des entiers ;
- calculer hash et entropie ;
- produire un hexdump.

Ne connaît pas :

- Frostbite ;
- TOC ;
- CAS ;
- EA SPORTS FC.

Question à laquelle elle répond :

> Comment lire proprement un fichier binaire ?

---

## 3.2 Couche analyse

Dossier prévu :

```text
sdk/analysis/
```

Responsabilité :

- comparer des fichiers ;
- analyser des headers ;
- chercher des chaînes ;
- calculer des statistiques ;
- détecter des motifs.

Ne connaît pas forcément Frostbite.

Question à laquelle elle répond :

> Comment observer et mesurer des structures binaires ?

---

## 3.3 Couche formats

Dossier :

```text
sdk/frostbite/formats/
```

Responsabilité :

- documenter les constantes connues ;
- centraliser les offsets ;
- distinguer les champs confirmés des champs inconnus.

Exemples :

```text
toc_format.py
cas_format.py
```

Question à laquelle elle répond :

> Que savons-nous du format ?

---

## 3.4 Couche lecteurs Frostbite

Dossier :

```text
sdk/frostbite/
```

Responsabilité :

- interpréter les formats Frostbite ;
- transformer des octets en objets métier ;
- exposer une API propre.

Exemples :

```text
toc.py
layout_toc.py
cas.py
```

Questions :

> Comment lire un TOC ?
> Comment lire un CAS ?
> Quels chemins Win32 contient layout.toc ?

---

## 3.5 Couche outils CLI

Dossier :

```text
tools/
```

Responsabilité :

- recevoir les arguments utilisateur ;
- appeler le SDK ;
- afficher les résultats.

Les outils CLI ne contiennent pas de logique métier durable.

Exemples :

```text
inspector.py
toc_info.py
cas_info.py
compare_binary.py
```

Question :

> Comment exposer une fonctionnalité du SDK en ligne de commande ?

---

## 3.6 Interface graphique future

Dossier prévu :

```text
gui/
```

Responsabilité :

- offrir une interface graphique ;
- visualiser les ressources ;
- éditer les objets ;
- piloter les outils du SDK.

Elle utilisera le SDK, comme les outils CLI.

---

# 4. Règles de conception

## Règle 1 — Une classe, une question

Chaque classe doit répondre à une question claire.

Exemples :

| Classe | Question |
|---|---|
| BinaryFile | Comment lire un fichier binaire ? |
| TOCReader | Comment interpréter un TOC ? |
| CASReader | Comment interpréter un CAS ? |
| HeaderProbe | Quels champs du header sont stables ? |

---

## Règle 2 — Aucun script jetable

Chaque outil doit pouvoir être réutilisé dans plusieurs mois.

Le code temporaire doit rester dans :

```text
experiments/
```

et ne doit pas entrer dans le SDK.

---

## Règle 3 — Les noms doivent refléter ce que l’on sait

On ne nomme pas une classe selon une hypothèse.

Exemple :

```text
Win32ResourcePath
```

est correct car nous observons des chemins commençant par `Win32/`.

```text
SuperBundle
```

serait prématuré tant que le rôle exact n’est pas confirmé.

---

## Règle 4 — Les hypothèses ne sont pas des faits

Chaque découverte doit être classée :

| Statut | Sens |
|---|---|
| Observé | Vu dans les fichiers |
| Hypothèse | Possible mais non prouvé |
| Confirmé | Vérifié par plusieurs expériences |
| Réfuté | Contredit par les données |

---

## Règle 5 — Pas de nombres magiques dans le code

Mauvais :

```python
read_bytes(0x00, 4)
```

Préféré :

```python
read_bytes(MAGIC_OFFSET, MAGIC_SIZE)
```

Les constantes doivent vivre dans :

```text
sdk/frostbite/formats/
```

---

# 5. Organisation cible

```text
FCStudio/
│
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── CHANGELOG.md
│
├── docs/
│   ├── research/
│   ├── decisions/
│   ├── glossary/
│   ├── sessions/
│   └── formats/
│
├── sdk/
│   ├── binary.py
│   ├── analysis/
│   │   ├── header_probe.py
│   │   ├── compare.py
│   │   ├── strings.py
│   │   └── entropy.py
│   │
│   └── frostbite/
│       ├── formats/
│       │   ├── toc_format.py
│       │   └── cas_format.py
│       ├── toc.py
│       ├── layout_toc.py
│       └── cas.py
│
├── tools/
│   ├── inspector.py
│   ├── toc_info.py
│   ├── cas_info.py
│   ├── compare_binary.py
│   └── header_probe.py
│
├── tests/
└── output/
```

---

# 6. Cycle de développement

Chaque nouvelle fonctionnalité suit ce cycle :

```text
Conception
↓
Implémentation SDK
↓
Outil CLI
↓
Test sur fichiers réels
↓
Documentation
↓
Validation
```

On ne passe pas à l’étape suivante tant que l’étape en cours n’est pas comprise.

---

# 7. État actuel

## Implémenté

- BinaryFile
- Inspector
- TOCReader minimal
- LayoutTOCReader minimal
- CASReader minimal
- Binary Comparator minimal

## En cours

- HeaderProbe
- BinaryComparator structuré
- Documentation projet

## À venir

- StringAnalyzer
- EntropyAnalyzer
- PatternScanner
- TOC format avancé
- CAS format avancé

---

# 8. Décision d’architecture initiale

FCStudio doit être construit comme un SDK d’abord, puis comme un ensemble d’outils.

Les interfaces CLI et GUI ne doivent être que des façades au-dessus du SDK.

Cette décision permet :

- de tester la logique indépendamment de l’affichage ;
- de réutiliser le SDK dans une future interface graphique ;
- d’éviter les scripts difficiles à maintenir ;
- de séparer les responsabilités.