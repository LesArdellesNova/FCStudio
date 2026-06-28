"""
FCStudio
Module : frostbite/toc.py

Responsabilité :
Interpréter progressivement les fichiers TOC Frostbite.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sdk.binary import BinaryFile

from sdk.frostbite.formats.toc_format import MAGIC_OFFSET, RESERVED_OFFSET, TOC_MAGIC

@dataclass(frozen=True)
class TOCHeader:
    magic: bytes
    reserved_or_unknown: int

    @property
    def magic_hex(self) -> str:
        return self.magic.hex(" ").upper()

    @property
    def is_valid_magic(self) -> bool:
        return self.magic == TOC_MAGIC

class TOCReader:
    def __init__(self, file_path: str | Path) -> None:
        self.binary_file = BinaryFile(file_path)
        self.header = self._read_header()

    def _read_header(self) -> TOCHeader:
        magic = self.binary_file.read_bytes(MAGIC_OFFSET, 4)
        reserved_or_unknown = self.binary_file.read_uint32_le(RESERVED_OFFSET)
        
        return TOCHeader(
            magic=magic,
            reserved_or_unknown=reserved_or_unknown,
        )

    @property
    def is_valid(self) -> bool:
        return self.header.is_valid_magic