"""
FCStudio
Modèle : string_analysis.py

Responsabilité :
Définir les modèles représentant les résultats d'une analyse
des chaînes ASCII détectées dans un fichier binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FoundString:
    offset: int
    text: str

    @property
    def length(self) -> int:
        return len(self.text)


@dataclass(frozen=True)
class StringAnalysis:
    file_name: str
    file_size: int
    min_length: int
    strings: list[FoundString]

    @property
    def count(self) -> int:
        return len(self.strings)