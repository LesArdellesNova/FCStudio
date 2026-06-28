"""
FCStudio
Modèle : binary_comparison.py

Responsabilité :
Définir les modèles de données représentant le résultat
d'une comparaison entre deux fichiers binaires.

Version : 0.0.1-dev
"""


from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BinaryBlockComparison:
    offset: int
    length: int
    equal_bytes: int

    @property
    def different_bytes(self) -> int:
        return self.length - self.equal_bytes

    @property
    def percent_equal(self) -> float:
        return (self.equal_bytes / self.length) * 100 if self.length else 0.0


@dataclass(frozen=True)
class UInt32Comparison:
    offset: int
    hex_a: str
    value_a: int
    hex_b: str
    value_b: int

    @property
    def is_equal(self) -> bool:
        return self.hex_a == self.hex_b


@dataclass(frozen=True)
class BinaryComparison:
    file_a_name: str
    file_b_name: str
    file_a_size: int
    file_b_size: int
    file_a_sha256: str
    file_b_sha256: str
    blocks: list[BinaryBlockComparison]
    uint32_values: list[UInt32Comparison]