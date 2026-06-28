"""
FCStudio
Modèle : pattern_analysis.py

Responsabilité :
Définir les modèles représentant les résultats d'une recherche
de motif binaire dans un fichier.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PatternMatch:
    offset: int


@dataclass(frozen=True)
class PatternAnalysis:
    file_name: str
    file_size: int
    pattern_hex: str
    matches: list[PatternMatch]

    @property
    def count(self) -> int:
        return len(self.matches)