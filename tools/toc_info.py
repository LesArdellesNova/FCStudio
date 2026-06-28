"""
FCStudio
Outil : toc_info.py

Responsabilité :
Afficher les premières informations interprétées d'un fichier TOC Frostbite.

Version : 0.0.1-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.frostbite.toc import TOCReader  # noqa: E402


console = Console()


def show_toc_info(file_path: str) -> None:
    reader = TOCReader(file_path)

    table = Table(title="FCStudio TOC Info v0.0.1-dev")
    table.add_column("Champ", style="bold")
    table.add_column("Valeur")
    table.add_column("Statut")

    table.add_row("Magic", reader.header.magic_hex, "OK" if reader.header.is_valid_magic else "INVALIDE")
    table.add_row("Champ 0x04", str(reader.header.reserved_or_unknown), "Inconnu")

    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio TOC Info")
    parser.add_argument("file", help="Fichier .toc à analyser")

    args = parser.parse_args()
    show_toc_info(args.file)


if __name__ == "__main__":
    main()