"""
FCStudio
Analyseur : string_analyzer.py

Responsabilité :
Extraire les chaînes ASCII imprimables présentes dans un
fichier binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

from pathlib import Path

from sdk.binary import BinaryFile
from sdk.models.string_analysis import FoundString, StringAnalysis


class StringAnalyzer:
    def __init__(self, file_path: str | Path, min_length: int = 6) -> None:
        self.binary_file = BinaryFile(file_path)
        self.min_length = min_length

    def analyze(self) -> StringAnalysis:
        return StringAnalysis(
            file_name=self.binary_file.name,
            file_size=self.binary_file.size,
            min_length=self.min_length,
            strings=self._extract_ascii_strings(),
        )

    def _extract_ascii_strings(self) -> list[FoundString]:
        results: list[FoundString] = []
        current = bytearray()
        start_offset: int | None = None

        for index, byte in enumerate(self.binary_file.data):
            if 32 <= byte <= 126:
                if start_offset is None:
                    start_offset = index
                current.append(byte)
            else:
                if start_offset is not None and len(current) >= self.min_length:
                    results.append(
                        FoundString(
                            offset=start_offset,
                            text=current.decode("ascii", errors="ignore"),
                        )
                    )

                current = bytearray()
                start_offset = None

        if start_offset is not None and len(current) >= self.min_length:
            results.append(
                FoundString(
                    offset=start_offset,
                    text=current.decode("ascii", errors="ignore"),
                )
            )

        return results