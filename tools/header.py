"""
FCStudio
Outil : header.py

Responsabilité :
Afficher l'analyse générique du header d'un fichier binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.analysis.header_analyzer import HeaderAnalyzer  # noqa: E402


console = Console()


def show_header(file_path: str, header_size: int) -> None:
    analysis = HeaderAnalyzer(file_path, header_size).analyze()

    info_table = Table(title="FCStudio Header Analyzer v0.0.1-dev")
    info_table.add_column("Champ", style="bold")
    info_table.add_column("Valeur")

    info_table.add_row("Fichier", analysis.file_name)
    info_table.add_row("Taille", f"{analysis.file_size:,} octets".replace(",", " "))
    info_table.add_row("Magic", analysis.magic_hex)
    info_table.add_row("Entropie", f"{analysis.entropy:.4f} / 8.0000")

    console.print(info_table)

    uint_table = Table(title="Valeurs uint32 du header")
    uint_table.add_column("Offset")
    uint_table.add_column("Hex")
    uint_table.add_column("uint32 LE")
    uint_table.add_column("uint32 BE")

    for value in analysis.uint32_values:
        uint_table.add_row(
            f"0x{value.offset:08X}",
            value.hex_value,
            str(value.uint32_le),
            str(value.uint32_be),
        )

    console.print(uint_table)

    ascii_table = Table(title=f"Chaînes ASCII détectées : {len(analysis.ascii_strings)}")
    ascii_table.add_column("Offset")
    ascii_table.add_column("Texte")

    for item in analysis.ascii_strings[:30]:
        ascii_table.add_row(f"0x{item.offset:08X}", item.text)

    console.print(ascii_table)


def show_comparative_table(file_paths: list[str], header_size: int) -> None:
    analyses = [
        HeaderAnalyzer(file_path, header_size).analyze()
        for file_path in file_paths
    ]

    table = Table(title="Comparaison uint32 LE des headers")
    table.add_column("Offset")

    for index, analysis in enumerate(analyses, start=1):
        label = Path(file_paths[index - 1]).parent.name
        table.add_column(label)

    table.add_column("Stable")

    max_values = min(len(analysis.uint32_values) for analysis in analyses)

    for value_index in range(max_values):
        offset = analyses[0].uint32_values[value_index].offset
        values = [
            analysis.uint32_values[value_index].uint32_le
            for analysis in analyses
        ]

        stable = len(set(values)) == 1

        table.add_row(
            f"0x{offset:08X}",
            *[str(value) for value in values],
            "OUI" if stable else "NON",
        )

    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio Header Analyzer")
    parser.add_argument("files", nargs="+", help="Fichiers à analyser")    
    parser.add_argument("--size", type=lambda x: int(x, 0), default=0x100, help="Taille du header à analyser")

    args = parser.parse_args()
    for file_path in args.files:
        show_header(file_path, args.size)
    if len(args.files) > 1:
        show_comparative_table(args.files, args.size)


if __name__ == "__main__":
    main()