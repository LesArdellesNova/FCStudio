"""
FCStudio
Outil : cas_info.py

Responsabilité :
Afficher les premières informations interprétées d'un fichier CAS Frostbite.

Version : 0.0.1-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.frostbite.cas import CASReader  # noqa: E402


console = Console()


def show_cas_info(file_path: str) -> None:
    reader = CASReader(file_path)
    binary_file = reader.binary_file

    table = Table(title="FCStudio CAS Info v0.0.1-dev")
    table.add_column("Champ", style="bold")
    table.add_column("Valeur")

    table.add_row("Nom", binary_file.name)
    table.add_row("Taille", f"{binary_file.size:,} octets".replace(",", " "))
    table.add_row("SHA256", binary_file.sha256)
    table.add_row("Magic / premiers octets", reader.header.magic_hex)
    table.add_row("Entropie", f"{binary_file.entropy:.4f} / 8.0000")

    console.print(table)

    console.print(
        Panel(
            binary_file.hexdump(0, min(256, binary_file.size)),
            title="Hexdump - 256 premiers octets",
            expand=False,
        )
    )

    console.print(build_numeric_probe_table(binary_file))

def build_numeric_probe_table(binary_file, max_offset: int = 0x80) -> Table:
    table = Table(title="Sonde numérique - début du fichier CAS")
    table.add_column("Offset")
    table.add_column("Hex 8 octets")
    table.add_column("uint16 LE")
    table.add_column("uint16 BE")
    table.add_column("uint32 LE")
    table.add_column("uint32 BE")
    table.add_column("uint64 LE")
    table.add_column("uint64 BE")

    for offset in range(0, min(max_offset, binary_file.size - 8 + 1), 4):
        raw8 = binary_file.read_bytes(offset, 8)

        table.add_row(
            f"0x{offset:08X}",
            raw8.hex(" ").upper(),
            str(binary_file.read_uint16_le(offset)),
            str(binary_file.read_uint16_be(offset)),
            str(binary_file.read_uint32_le(offset)),
            str(binary_file.read_uint32_be(offset)),
            str(binary_file.read_uint64_le(offset)),
            str(binary_file.read_uint64_be(offset)),
        )

    return table


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio CAS Info")
    parser.add_argument("file", help="Fichier .cas à analyser")

    args = parser.parse_args()
    show_cas_info(args.file)


if __name__ == "__main__":
    main()