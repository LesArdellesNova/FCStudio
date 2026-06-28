"""
FCStudio
Outil : inspector.py

Responsabilité :
Afficher la carte d'identité technique d'un fichier binaire.

Version : 0.0.2-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.binary import BinaryFile, extract_ascii_strings  # noqa: E402

console = Console()


UINT32_OFFSETS = [
    0x00, 0x04, 0x08, 0x0C,
    0x10, 0x14, 0x18, 0x1C,
    0x40, 0x44, 0x48, 0x4C,
    0x50, 0x54, 0x58, 0x5C,
]


def build_info_table(binary_file: BinaryFile) -> Table:
    info = binary_file.info()

    table = Table(title="FCStudio Inspector v0.0.2-dev")
    table.add_column("Champ", style="bold")
    table.add_column("Valeur")

    table.add_row("Nom", info.name)
    table.add_row("Chemin", str(info.path))
    table.add_row("Taille", f"{info.size:,} octets".replace(",", " "))
    table.add_row("SHA256", info.sha256)
    table.add_row("Magic", info.magic_hex)
    table.add_row("Entropie", f"{info.entropy:.4f} / 8.0000")

    return table


def build_uint32_table(binary_file: BinaryFile) -> Table:
    table = Table(title="Interprétation uint32 du début du fichier")
    table.add_column("Offset")
    table.add_column("Hex")
    table.add_column("uint32 LE")
    table.add_column("uint32 BE")

    for offset in UINT32_OFFSETS:
        raw = binary_file.read_bytes(offset, 4)

        table.add_row(
            f"0x{offset:08X}",
            raw.hex(" ").upper(),
            str(binary_file.read_uint32_le(offset)),
            str(binary_file.read_uint32_be(offset)),
        )

    return table


def inspect_file(file_path: str) -> None:
    binary_file = BinaryFile(file_path)
    info = binary_file.info()

    console.print(build_info_table(binary_file))

    console.print(
        Panel(
            binary_file.hexdump(0, min(256, info.size)),
            title="Hexdump - 256 premiers octets",
            expand=False,
        )
    )

    console.print(build_uint32_table(binary_file))

    console.print(build_ascii_strings_table(binary_file))

def build_ascii_strings_table(binary_file: BinaryFile, limit: int = 30) -> Table:
    strings = extract_ascii_strings(binary_file.data, min_length=6)

    table = Table(title=f"Chaînes ASCII détectées - {min(len(strings), limit)} / {len(strings)}")
    table.add_column("Offset")
    table.add_column("Texte")

    for offset, text in strings[:limit]:
        table.add_row(f"0x{offset:08X}", text)

    return table


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio Inspector")
    parser.add_argument("file", help="Fichier à analyser")

    args = parser.parse_args()
    inspect_file(args.file)


if __name__ == "__main__":
    main()