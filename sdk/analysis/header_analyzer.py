"""
FCStudio
Analyseur : header_analyzer.py

Responsabilité :
Analyser les premiers octets d'un fichier binaire sans connaître son format.

Version : 0.0.1-dev
"""

from __future__ import annotations

from pathlib import Path

from sdk.binary import BinaryFile, extract_ascii_strings
from sdk.models.header_analysis import (
    HeaderAnalysis,
    HeaderAsciiString,
    HeaderUInt32Value,
)


class HeaderAnalyzer:
    def __init__(self, file_path: str | Path, header_size: int = 0x100) -> None:
        self.binary_file = BinaryFile(file_path)
        self.header_size = min(header_size, self.binary_file.size)

    def analyze(self) -> HeaderAnalysis:
        return HeaderAnalysis(
            file_name=self.binary_file.name,
            file_size=self.binary_file.size,
            magic_hex=self.binary_file.magic_hex,
            entropy=self.binary_file.entropy,
            uint32_values=self._read_uint32_values(),
            ascii_strings=self._extract_ascii_strings(),
        )

    def _read_uint32_values(self) -> list[HeaderUInt32Value]:
        values: list[HeaderUInt32Value] = []

        for offset in range(0, self.header_size - 3, 4):
            raw = self.binary_file.read_bytes(offset, 4)

            values.append(
                HeaderUInt32Value(
                    offset=offset,
                    hex_value=raw.hex(" ").upper(),
                    uint32_le=self.binary_file.read_uint32_le(offset),
                    uint32_be=self.binary_file.read_uint32_be(offset),
                )
            )

        return values

    def _extract_ascii_strings(self) -> list[HeaderAsciiString]:
        header_data = self.binary_file.read_bytes(0, self.header_size)
        strings = extract_ascii_strings(header_data, min_length=6)

        return [
            HeaderAsciiString(offset=offset, text=text)
            for offset, text in strings
        ]