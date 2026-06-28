"""
FCStudio
Outil : pattern.py

Responsabilité :
Afficher les occurrences d'un motif binaire dans un fichier.

Version : 0.0.1-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.analysis.pattern_scanner import PatternScanner  # noqa: E402


console = Console()


def show_pattern_matches(file_path: str, pattern_hex: str, limit: int) -> None:
    analysis = PatternScanner(file_path).scan_hex(pattern_hex)

    info_table = Table(title="FCStudio Pattern Scanner v0.0.1-dev")
    info_table.add_column("Champ", style="bold")
    info_table.add_column("Valeur")

    info_table.add_row("Fichier", analysis.file_name)
    info_table.add_row("Taille", f"{analysis.file_size:,} octets".replace(",", " "))
    info_table.add_row("Motif", analysis.pattern_hex)
    info_table.add_row("Occurrences", str(analysis.count))

    console.print(info_table)

    table = Table(title=f"Occurrences - affichage {min(limit, analysis.count)}/{analysis.count}")
    table.add_column("Offset")

    for match in analysis.matches[:limit]:
        table.add_row(f"0x{match.offset:08X}")

    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio Pattern Scanner")
    parser.add_argument("file", help="Fichier à analyser")
    parser.add_argument("pattern", help="Motif hexadécimal, ex: '00 D1 CE 01'")
    parser.add_argument("--limit", type=int, default=50)

    args = parser.parse_args()

    show_pattern_matches(
        file_path=args.file,
        pattern_hex=args.pattern,
        limit=args.limit,
    )


if __name__ == "__main__":
    main()