# TOC Format - Notes initiales

## Fichiers testés

| Fichier | Taille | Magic | Entropie |
|---|---:|---|---:|
| Data/layout.toc | 85 050 | 00 D1 CE 01 | 5.9964 |
| Data/Win32/fc/fcgame/fcgame.toc | 1 432 476 | 00 D1 CE 01 | 6.0028 |
| Data/Win32/globals.toc | 2 515 114 | 00 D1 CE 01 | 5.6308 |
| Data/Win32/contentsb.toc | 17 671 004 | 00 D1 CE 01 | 6.1786 |
| Patch/layout.toc | 84 540 | 00 D1 CE 01 | 5.9875 |

## Header observé

| Offset | Taille | Valeur observée | Statut |
|---:|---:|---|---|
| 0x00 | 4 | 00 D1 CE 01 | Confirmé : Magic commun |
| 0x04 | 4 | 00 00 00 00 | Confirmé : champ commun, rôle inconnu |
| 0x08 | 56 | Variable | Hypothèse : hash / signature / métadonnées |

## Hypothèses

- Les fichiers `.toc` ne semblent pas entièrement compressés ou chiffrés.
- Le bloc `0x08-0x3F` change pour chaque fichier.
- Le vrai contenu structuré commence probablement après `0x40`.

## Premieres Conclusions 28/06/2026

- Le début du TOC après le magic ne ressemble pas à un header classique lisible.
- Il peut s'agir d'un bloc compressé, signé, hashé, ou d'une structure sérialisée Frostbite.

## Découverte 2026-06-28 - layout.toc

Le fichier `Data/layout.toc` contient des chaînes ASCII lisibles.

Première chaîne significative détectée :

| Offset | Texte |
|---:|---|
| 0x00000231 | superBundles |

Exemples de chaînes suivantes :

- Win32/careermodestorysba
- Win32/careersba
- Win32/chants_dlc
- Win32/chants_full
- Win32/commentaryfull_fre_fr

Hypothèse :
`layout.toc` contient probablement la liste des SuperBundles chargés par le jeu.

Statut :
Confirmé pour la présence des chaînes.
Hypothèse à vérifier pour leur rôle exact.

## Validation TOCReader v0.0.1-dev

Fichiers testés :

- Data/layout.toc
- Data/Win32/fc/fcgame/fcgame.toc
- Data/Win32/globals.toc
- Data/Win32/contentsb.toc
- Patch/layout.toc

Résultat :

- Magic `00 D1 CE 01` confirmé sur 5/5 fichiers.
- Champ `0x04` = `0` confirmé sur 5/5 fichiers.

Statut :

- Magic : confirmé.
- Champ `0x04` : observé, rôle inconnu.