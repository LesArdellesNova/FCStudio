"""
FCStudio
Analyseur : entropy_analyzer.py

Responsabilité :
Analyser l'entropie globale et par blocs d'un fichier binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

from pathlib import Path

from sdk.binary import BinaryFile, calculate_entropy
from sdk.models.entropy_analysis import EntropyAnalysis, EntropyBlock


class EntropyAnalyzer:
    def __init__(self, file_path: str | Path, block_size: int = 4096) -> None:
        self.binary_file = BinaryFile(file_path)
        self.block_size = block_size

    def analyze(self) -> EntropyAnalysis:
        return EntropyAnalysis(
            file_name=self.binary_file.name,
            file_size=self.binary_file.size,
            block_size=self.block_size,
            global_entropy=self.binary_file.entropy,
            blocks=self._analyze_blocks(),
        )

    def _analyze_blocks(self) -> list[EntropyBlock]:
        blocks: list[EntropyBlock] = []

        for offset in range(0, self.binary_file.size, self.block_size):
            data = self.binary_file.read_bytes(
                offset,
                min(self.block_size, self.binary_file.size - offset),
            )

            blocks.append(
                EntropyBlock(
                    offset=offset,
                    size=len(data),
                    entropy=calculate_entropy(data),
                )
            )

        return blocks