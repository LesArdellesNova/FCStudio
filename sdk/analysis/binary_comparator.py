"""
FCStudio
Analyseur : binary_comparator.py

Responsabilité :
Comparer deux fichiers binaires afin d'identifier les
zones identiques, les différences et les variations
des valeurs du header.

Version : 0.0.1-dev
"""


from __future__ import annotations

from pathlib import Path

from sdk.binary import BinaryFile
from sdk.models.binary_comparison import (
    BinaryBlockComparison,
    BinaryComparison,
    UInt32Comparison,
)


class BinaryComparator:
    def __init__(self, file_a_path: str | Path, file_b_path: str | Path) -> None:
        self.file_a = BinaryFile(file_a_path)
        self.file_b = BinaryFile(file_b_path)

    def compare(self, block_size: int = 16, header_size: int = 0x80) -> BinaryComparison:
        return BinaryComparison(
            file_a_name=self.file_a.name,
            file_b_name=self.file_b.name,
            file_a_size=self.file_a.size,
            file_b_size=self.file_b.size,
            file_a_sha256=self.file_a.sha256,
            file_b_sha256=self.file_b.sha256,
            blocks=self._compare_blocks(block_size),
            uint32_values=self._compare_uint32(header_size),
        )

    def _compare_blocks(self, block_size: int) -> list[BinaryBlockComparison]:
        max_size = min(self.file_a.size, self.file_b.size)
        results: list[BinaryBlockComparison] = []

        for offset in range(0, max_size, block_size):
            length = min(block_size, max_size - offset)
            block_a = self.file_a.read_bytes(offset, length)
            block_b = self.file_b.read_bytes(offset, length)

            equal_bytes = sum(1 for a, b in zip(block_a, block_b) if a == b)

            results.append(
                BinaryBlockComparison(
                    offset=offset,
                    length=length,
                    equal_bytes=equal_bytes,
                )
            )

        return results

    def _compare_uint32(self, header_size: int) -> list[UInt32Comparison]:
        max_size = min(self.file_a.size, self.file_b.size, header_size)
        results: list[UInt32Comparison] = []

        for offset in range(0, max_size - 3, 4):
            raw_a = self.file_a.read_bytes(offset, 4)
            raw_b = self.file_b.read_bytes(offset, 4)

            results.append(
                UInt32Comparison(
                    offset=offset,
                    hex_a=raw_a.hex(" ").upper(),
                    value_a=self.file_a.read_uint32_le(offset),
                    hex_b=raw_b.hex(" ").upper(),
                    value_b=self.file_b.read_uint32_le(offset),
                )
            )

        return results