"""
FCStudio
Outil : layout_info.py

Responsabilité :
Afficher les SuperBundles détectés dans layout.toc.

Version : 0.0.1-dev
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sdk.frostbite.layout_toc import LayoutTOCReader  # noqa: E402


console = Console()


def show_layout_info(file_path: str) -> None:
    reader = LayoutTOCReader()
    paths = reader.extract_win32_paths()
    table = Table(title=f"Win32 Resource Paths : {len(paths)}")
    table.add_column("Offset")
    table.add_column("Path")

    for resource in paths:
        table.add_row(f"0x{resource.offset:08X}", resource.path,)
    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(description="FCStudio Layout TOC Info")
    parser.add_argument("file", help="Fichier layout.toc à analyser")

    args = parser.parse_args()
    show_layout_info(args.file)


if __name__ == "__main__":
    main()