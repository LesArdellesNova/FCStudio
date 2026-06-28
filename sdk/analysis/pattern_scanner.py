"""
FCStudio
Analyseur : pattern_scanner.py

Responsabilité :
Rechercher un motif binaire exact dans un fichier.

Version : 0.0.1-dev
"""

from __future__ import annotations

from pathlib import Path

from sdk.binary import BinaryFile
from sdk.models.pattern_analysis import PatternAnalysis, PatternMatch


class PatternScanner:
    def __init__(self, file_path: str | Path) -> None:
        self.binary_file = BinaryFile(file_path)

    def scan_hex(self, pattern_hex: str) -> PatternAnalysis:
        pattern = bytes.fromhex(pattern_hex.replace(" ", ""))

        matches: list[PatternMatch] = []
        start = 0

        while True:
            index = self.binary_file.data.find(pattern, start)

            if index == -1:
                break

            matches.append(PatternMatch(offset=index))
            start = index + 1

        return PatternAnalysis(
            file_name=self.binary_file.name,
            file_size=self.binary_file.size,
            pattern_hex=pattern.hex(" ").upper(),
            matches=matches,
        )