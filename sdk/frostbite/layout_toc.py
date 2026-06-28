"""
FCStudio
Module : frostbite/layout_toc.py

Responsabilité :
Interpréter progressivement layout.toc et extraire les SuperBundles.

Version : 0.0.1-dev
"""

from __future__ import annotations

from dataclasses import dataclass

from sdk.binary import extract_ascii_strings
from sdk.frostbite.toc import TOCReader


@dataclass(frozen=True)
class Win32ResourcePath:
    offset: int
    path: str


class LayoutTOCReader(TOCReader):

    def extract_win32_paths(self) -> list[Win32ResourcePath]:

        strings = extract_ascii_strings(
            self.binary_file.data,
            min_length=6,
        )

        paths: list[Win32ResourcePath] = []

        for offset, text in strings:

            if text.startswith("Win32/"):

                paths.append(
                    Win32ResourcePath(
                        offset=offset,
                        path=text,
                    )
                )

        return paths