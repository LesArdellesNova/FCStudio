"""
FCStudio
Modèle : entropy_analysis.py

Responsabilité :
Définir les modèles représentant les résultats d'une analyse
d'entropie sur un fichier binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EntropyBlock:
    offset: int
    size: int
    entropy: float


@dataclass(frozen=True)
class EntropyAnalysis:
    file_name: str
    file_size: int
    block_size: int
    global_entropy: float
    blocks: list[EntropyBlock]