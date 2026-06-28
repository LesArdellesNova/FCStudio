"""
FCStudio
Modèle : header_analysis.py

Responsabilité :
Décrire les résultats d'une analyse de header binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HeaderUInt32Value:
    offset: int
    hex_value: str
    uint32_le: int
    uint32_be: int


@dataclass(frozen=True)
class HeaderAsciiString:
    offset: int
    text: str


@dataclass(frozen=True)
class HeaderAnalysis:
    file_name: str
    file_size: int
    magic_hex: str
    entropy: float
    uint32_values: list[HeaderUInt32Value]
    ascii_strings: list[HeaderAsciiString]