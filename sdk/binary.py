"""
FCStudio
Module : binary.py

Responsabilité :
Fournir une couche propre pour lire et analyser des fichiers binaires.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import math


HEADER_SIZE = 64
MAGIC_SIZE = 4


@dataclass(frozen=True)
class BinaryFileInfo:
    path: Path
    name: str
    size: int
    sha256: str
    magic_hex: str
    entropy: float


class BinaryFile:
    def __init__(self, file_path: str | Path) -> None:
        self.path = Path(file_path)

        if not self.path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {self.path}")

        if not self.path.is_file():
            raise ValueError(f"Le chemin n'est pas un fichier : {self.path}")

        self._data: bytes | None = None

    @property
    def data(self) -> bytes:
        if self._data is None:
            self._data = self.path.read_bytes()
        return self._data

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def magic(self) -> bytes:
        return self.data[:MAGIC_SIZE]

    @property
    def magic_hex(self) -> str:
        return self.magic.hex(" ").upper()

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest().upper()

    @property
    def entropy(self) -> float:
        return calculate_entropy(self.data)

    def read_bytes(self, offset: int, length: int) -> bytes:
        validate_range(offset, length, self.size)
        return self.data[offset:offset + length]
    
    def read_uint16_le(self, offset: int) -> int:
        raw = self.read_bytes(offset, 2)
        return int.from_bytes(raw, byteorder="little", signed=False)

    def read_uint16_be(self, offset: int) -> int:
        raw = self.read_bytes(offset, 2)
        return int.from_bytes(raw, byteorder="big", signed=False)

    def read_uint32_le(self, offset: int) -> int:
        raw = self.read_bytes(offset, 4)
        return int.from_bytes(raw, byteorder="little", signed=False)

    def read_uint32_be(self, offset: int) -> int:
        raw = self.read_bytes(offset, 4)
        return int.from_bytes(raw, byteorder="big", signed=False)
    
    def read_uint64_le(self, offset: int) -> int:
        raw = self.read_bytes(offset, 8)
        return int.from_bytes(raw, byteorder="little", signed=False)

    def read_uint64_be(self, offset: int) -> int:
        raw = self.read_bytes(offset, 8)
        return int.from_bytes(raw, byteorder="big", signed=False)

    def header(self, length: int = HEADER_SIZE) -> bytes:
        return self.read_bytes(0, min(length, self.size))

    def hexdump(self, offset: int = 0, length: int = HEADER_SIZE, width: int = 16) -> str:
        validate_range(offset, length, self.size)

        rows: list[str] = []
        data = self.read_bytes(offset, length)

        for row_offset in range(0, len(data), width):
            chunk = data[row_offset:row_offset + width]
            absolute_offset = offset + row_offset

            hex_part = " ".join(f"{byte:02X}" for byte in chunk)
            ascii_part = "".join(chr(byte) if 32 <= byte <= 126 else "." for byte in chunk)

            rows.append(f"{absolute_offset:08X}  {hex_part:<{width * 3}}  {ascii_part}")

        return "\n".join(rows)

    def info(self) -> BinaryFileInfo:
        return BinaryFileInfo(
            path=self.path,
            name=self.name,
            size=self.size,
            sha256=self.sha256,
            magic_hex=self.magic_hex,
            entropy=self.entropy,
        )
    


def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    occurrences = [0] * 256

    for byte in data:
        occurrences[byte] += 1

    entropy = 0.0
    data_length = len(data)

    for count in occurrences:
        if count == 0:
            continue

        probability = count / data_length
        entropy -= probability * math.log2(probability)

    return entropy


def validate_range(offset: int, length: int, file_size: int) -> None:
    if offset < 0:
        raise ValueError("L'offset ne peut pas être négatif.")

    if length < 0:
        raise ValueError("La longueur ne peut pas être négative.")

    if offset + length > file_size:
        raise ValueError(
            f"Lecture hors limites : offset={offset}, length={length}, taille={file_size}"
        )
    
def extract_ascii_strings(data: bytes, min_length: int = 4) -> list[tuple[int, str]]:
    results: list[tuple[int, str]] = []
    current = bytearray()
    start_offset: int | None = None

    for index, byte in enumerate(data):
        if 32 <= byte <= 126:
            if start_offset is None:
                start_offset = index
            current.append(byte)
        else:
            if start_offset is not None and len(current) >= min_length:
                results.append((start_offset, current.decode("ascii", errors="ignore")))
            current = bytearray()
            start_offset = None

    if start_offset is not None and len(current) >= min_length:
        results.append((start_offset, current.decode("ascii", errors="ignore")))

    return results