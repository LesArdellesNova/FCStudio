"""
FCStudio
Outil : strings.py

Responsabilité :
Afficher les chaînes ASCII détectées dans un fichier
binaire à l'aide du SDK.

Version : 0.0.1-dev
"""


from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.analysis.string_analyzer import StringAnalyzer  # noqa: E402


console = Console()


def show_strings(file_path: str, min_length: int, limit: int, contains: str | None) -> None:
    analysis = StringAnalyzer(file_path, min_length).analyze()

    strings = analysis.strings

    if contains:
        strings = [
            item for item in strings
            if contains.lower() in item.text.lower()
        ]

    table = Table(title=f"Chaînes ASCII détectées : {len(strings)}")
    table.add_column("Offset")
    table.add_column("Longueur")
    table.add_column("Texte")

    for item in strings[:limit]:
        table.add_row(
            f"0x{item.offset:08X}",
            str(item.length),
            item.text,
        )

    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio String Analyzer")
    parser.add_argument("file", help="Fichier à analyser")
    parser.add_argument("--min-length", type=int, default=6)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--contains", default=None)

    args = parser.parse_args()

    show_strings(
        file_path=args.file,
        min_length=args.min_length,
        limit=args.limit,
        contains=args.contains,
    )


if __name__ == "__main__":
    main()