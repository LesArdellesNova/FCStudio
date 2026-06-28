"""
FCStudio
Outil : entropy.py

Responsabilité :
Afficher l'entropie globale et par blocs d'un fichier binaire.

Version : 0.0.1-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.analysis.entropy_analyzer import EntropyAnalyzer  # noqa: E402


console = Console()


def show_entropy(file_path: str, block_size: int, limit: int) -> None:
    analysis = EntropyAnalyzer(file_path, block_size).analyze()

    info_table = Table(title="FCStudio Entropy Analyzer v0.0.1-dev")
    info_table.add_column("Champ", style="bold")
    info_table.add_column("Valeur")

    info_table.add_row("Fichier", analysis.file_name)
    info_table.add_row("Taille", f"{analysis.file_size:,} octets".replace(",", " "))
    info_table.add_row("Taille bloc", f"{analysis.block_size:,} octets".replace(",", " "))
    info_table.add_row("Entropie globale", f"{analysis.global_entropy:.4f} / 8.0000")

    console.print(info_table)

    block_table = Table(title=f"Entropie par blocs - affichage {min(limit, len(analysis.blocks))}/{len(analysis.blocks)}")
    block_table.add_column("Offset")
    block_table.add_column("Taille")
    block_table.add_column("Entropie")

    for block in analysis.blocks[:limit]:
        block_table.add_row(
            f"0x{block.offset:08X}",
            str(block.size),
            f"{block.entropy:.4f}",
        )

    console.print(block_table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio Entropy Analyzer")
    parser.add_argument("file", help="Fichier à analyser")
    parser.add_argument("--block-size", type=lambda x: int(x, 0), default=4096)
    parser.add_argument("--limit", type=int, default=50)

    args = parser.parse_args()

    show_entropy(
        file_path=args.file,
        block_size=args.block_size,
        limit=args.limit,
    )


if __name__ == "__main__":
    main()