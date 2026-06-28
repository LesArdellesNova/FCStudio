"""
FCStudio
Outil : compare_binary.py

Responsabilité :
Comparer deux fichiers binaires en utilisant le SDK.

Version : 0.0.2-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.analysis.binary_comparator import BinaryComparator  # noqa: E402


console = Console()


def show_comparison(file_a: str, file_b: str, block_size: int, header_size: int) -> None:
    comparison = BinaryComparator(file_a, file_b).compare(
        block_size=block_size,
        header_size=header_size,
    )

    info_table = Table(title="FCStudio Binary Comparator v0.0.2-dev")
    info_table.add_column("Info", style="bold")
    info_table.add_column("Fichier A")
    info_table.add_column("Fichier B")

    info_table.add_row("Nom", comparison.file_a_name, comparison.file_b_name)
    info_table.add_row(
        "Taille",
        f"{comparison.file_a_size:,}".replace(",", " "),
        f"{comparison.file_b_size:,}".replace(",", " "),
    )
    info_table.add_row(
        "SHA256",
        comparison.file_a_sha256[:16] + "...",
        comparison.file_b_sha256[:16] + "...",
    )

    console.print(info_table)

    block_table = Table(title=f"Comparaison par blocs de {block_size} octets")
    block_table.add_column("Offset")
    block_table.add_column("Identiques")
    block_table.add_column("Différents")
    block_table.add_column("% identique")

    for block in comparison.blocks[:64]:
        block_table.add_row(
            f"0x{block.offset:08X}",
            f"{block.equal_bytes}/{block.length}",
            str(block.different_bytes),
            f"{block.percent_equal:.1f}%",
        )

    console.print(block_table)

    uint32_table = Table(title="Comparaison uint32 LE - header")
    uint32_table.add_column("Offset")
    uint32_table.add_column("Hex A")
    uint32_table.add_column("uint32 A")
    uint32_table.add_column("Hex B")
    uint32_table.add_column("uint32 B")
    uint32_table.add_column("Statut")

    for value in comparison.uint32_values:
        uint32_table.add_row(
            f"0x{value.offset:08X}",
            value.hex_a,
            str(value.value_a),
            value.hex_b,
            str(value.value_b),
            "IDENTIQUE" if value.is_equal else "DIFFÉRENT",
        )

    console.print(uint32_table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio Binary Comparator")
    parser.add_argument("file_a", help="Premier fichier")
    parser.add_argument("file_b", help="Deuxième fichier")
    parser.add_argument("--block-size", type=int, default=16, help="Taille des blocs comparés")
    parser.add_argument("--header-size", type=lambda x: int(x, 0), default=0x80, help="Taille du header analysé")

    args = parser.parse_args()

    show_comparison(
        file_a=args.file_a,
        file_b=args.file_b,
        block_size=args.block_size,
        header_size=args.header_size,
    )


if __name__ == "__main__":
    main()