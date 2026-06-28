"""
FCStudio
Module : frostbite/cas.py

Responsabilité :
Interpréter progressivement les fichiers CAS Frostbite.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sdk.binary import BinaryFile


@dataclass(frozen=True)
class CASHeader:
    magic: bytes

    @property
    def magic_hex(self) -> str:
        return self.magic.hex(" ").upper()


class CASReader:
    def __init__(self, file_path: str | Path) -> None:
        self.binary_file = BinaryFile(file_path)
        self.header = self._read_header()

    def _read_header(self) -> CASHeader:
        magic = self.binary_file.read_bytes(0x00, 4)

        return CASHeader(
            magic=magic,
        )