# FCStudio — Contributing Guide

> Ce document décrit les règles de développement du projet FCStudio.

Le respect de ces règles garantit un projet lisible, maintenable et scientifiquement rigoureux.

---

# 1. Philosophie

FCStudio est un laboratoire d'analyse des formats Frostbite.

Notre objectif est de comprendre les formats avant de les modifier.

Chaque développement doit respecter le cycle suivant :

Observation
↓
Compréhension
↓
Validation
↓
Modification

Toute modification réalisée sans compréhension préalable est considérée comme expérimentale et ne doit pas intégrer le SDK.

---

# 2. Valeurs du projet

Le projet repose sur quatre principes.

## Rigueur

Les conclusions sont basées sur des observations reproductibles.

---

## Simplicité

Une classe doit avoir une responsabilité unique.

---

## Réutilisabilité

Chaque composant doit pouvoir être utilisé dans plusieurs outils.

---

## Documentation

Une découverte qui n'est pas documentée est considérée comme perdue.

---

# 3. Règles de développement

## Une classe = une responsabilité

Exemple :

BinaryFile

↓

Lire un fichier.

CASReader

↓

Interpréter un CAS.

HeaderProbe

↓

Observer un header.

---

## Les outils CLI

Les scripts du dossier tools/

- ne contiennent pas de logique métier ;
- appellent uniquement le SDK ;
- servent d'interface utilisateur.

---

## Le SDK

Toute logique durable appartient au SDK.

Le SDK ne dépend jamais des outils CLI.

---

## Les expériences

Les essais rapides doivent être réalisés dans :

experiments/

Ils ne doivent pas être intégrés au SDK tant qu'ils ne sont pas validés.

---

# 4. Hypothèses

Une hypothèse n'est jamais un fait.

Chaque hypothèse possède un identifiant.

Exemple :

H0001

Chaque hypothèse possède un état.

🟡 En cours

🟢 Confirmée

🔴 Réfutée

⚪ Abandonnée

Les hypothèses sont conservées dans le registre dédié.

---

# 5. Décisions techniques

Toute décision importante doit être documentée.

Exemple :

D0001

Le SDK ne dépend jamais des outils CLI.

Les décisions ne sont pas supprimées.

Si elles deviennent obsolètes, elles sont archivées.

---

# 6. Documentation

Toute évolution importante doit entraîner une mise à jour :

- du CHANGELOG ;
- de la ROADMAP si nécessaire ;
- de la documentation concernée.

---

# 7. Style de code

## Lisibilité

Le code est écrit pour être compris avant d'être optimisé.

---

## Nommage

Les noms doivent décrire ce qui est observé.

Éviter :

SuperBundleEntry

Préférer :

Win32ResourcePath

tant que la structure exacte n'est pas démontrée.

---

## Constantes

Aucun nombre magique dans le code.

Mauvais :

read_uint32(0x18)

Préféré :

RESOURCE_TABLE_OFFSET

---

## Commentaires

Les commentaires expliquent :

Pourquoi

et non

Comment.

Le code doit être suffisamment clair pour expliquer le "comment".

---

# 8. Tests

Toute fonctionnalité importante doit être testée sur plusieurs fichiers.

Une observation réalisée sur un seul fichier ne suffit pas à confirmer une hypothèse.

---

# 9. Processus de développement

Chaque nouvelle fonctionnalité suit les étapes suivantes.

1. Observation

2. Analyse

3. Hypothèse

4. Expérience

5. Validation

6. Documentation

7. Intégration

---

# 10. Définition de terminé (Definition of Done)

Une tâche est considérée comme terminée uniquement si :

✓ Le code fonctionne.

✓ Le code est lisible.

✓ Les noms sont cohérents.

✓ Les tests sont réalisés.

✓ La documentation est mise à jour.

✓ Le CHANGELOG est complété.

✓ Les hypothèses sont documentées si nécessaire.

---

# 11. Devise du projet

Observer.

Comprendre.

Vérifier.

Modifier.

Toujours dans cet ordre.

# 12. Le Manifeste FCStudio

Nous préférons comprendre plutôt que deviner.

Nous préférons mesurer plutôt que supposer.

Nous préférons une hypothèse réfutée à une certitude non vérifiée.

Nous préférons un outil générique à un script spécifique.

Nous construisons des fondations avant d'ajouter des fonctionnalités.

Nous documentons nos découvertes afin qu'elles deviennent un savoir durable.

Notre objectif n'est pas seulement de développer FCStudio.

Notre objectif est de développer une méthode d'ingénierie applicable à tout format binaire.